import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from access.corpus import (
    assess_database_access,
    audit,
    build_index,
    coverage,
    entity,
    evidence,
    export_bundle,
    related,
    repo_root_from,
    search,
    sources,
    timeline,
)

ROOT = repo_root_from(Path(__file__).resolve())


class AccessAcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        build_index(ROOT)

    def test_rebuild_is_deterministic(self):
        first = (ROOT / "indexes" / "access" / "records.jsonl").read_bytes()
        manifest = (ROOT / "indexes" / "access" / "manifest.json").read_bytes()
        build_index(ROOT)
        self.assertEqual(first, (ROOT / "indexes" / "access" / "records.jsonl").read_bytes())
        self.assertEqual(manifest, (ROOT / "indexes" / "access" / "manifest.json").read_bytes())

    def test_sandigil_does_not_imply_absence(self):
        found = search(ROOT, "Sandigil")
        self.assertEqual(found["total"], 0)
        families = {item["family"]: item for item in found["coverage"]["families"]}
        self.assertTrue(found["coverage"]["absence_is_not_evidence"])
        self.assertEqual(families["discord_messages"]["status"], "not_searched")
        self.assertEqual(families["discord_text_export"]["status"], "absent")
        self.assertIn("ingest/discord-retrieval-v1", families["discord_text_export"]["reason"])
        self.assertEqual(families["discord_messages"]["coverage"], "INACCESSIBLE")
        self.assertEqual(families["discord_messages"]["reasons"], ["lfs_pointer_only"])
        self.assertEqual(families["discord_messages"]["access"], "pointer_only")
        self.assertEqual(families["discord_text_export"]["reasons"], ["missing_readable_projection", "unmerged_workstream"])
        self.assertEqual(families["discord_attachments"]["coverage"], "INACCESSIBLE")
        self.assertIn("lfs_pointer_only", families["discord_attachments"]["reasons"])
        drive = families["drive_bcs_bodies"]
        self.assertEqual(drive["coverage"], "PARTIAL")
        self.assertGreater(drive["bodies_present"], 0)
        self.assertGreater(drive["catalog_only"], 0)
        self.assertIn("missing_readable_projection", drive["reasons"])
        self.assertIn("external_auth", drive["reasons"])
        self.assertIn("unmerged_workstream", drive["reasons"])
        present_state = next(item for item in drive["states"] if item["state"] == "body_present")
        self.assertTrue(present_state["searched"])
        self.assertNotIn("reasons", present_state)
        report = found["coverage"]["coverage_report"]
        self.assertEqual(report["status"], "PARTIAL")
        self.assertFalse(report["zero_match_means_absence"])
        self.assertIn("discord_messages", [item["family"] for item in report["omitted_families"]])
        self.assertIn("drive_bcs_bodies", report["partial_families"])

    def test_entity_dm_radar_is_scoped_not_global(self):
        found = entity(ROOT, "DM radar")
        self.assertFalse(found["ambiguous"])
        self.assertEqual([person["record_id"] for person in found["people"]], ["person:brendon-faulkner"])
        identities = {row["record_id"]: row for row in found["identities"]}
        alias = identities["identity:brendon:alias:dm-radar"]
        self.assertEqual(alias["attributes"]["confidence"], "CONFIRMED")
        self.assertEqual(alias["attributes"]["attribution_use"], "ALIAS_RESOLUTION_WITH_CONTEXT_ONLY")
        scoped = [
            row
            for row in found["identities"]
            if row["attributes"].get("attribution_use") == "ATTRIBUTION_ALLOWED_WITHIN_S3_SERVER_SCOPE"
        ]
        self.assertEqual(len(scoped), 1)
        self.assertEqual(scoped[0]["attributes"]["project_id"], "roanoke-s3")
        self.assertIn("not identity assertions", found["identity_note"])
        self.assertTrue(any(item["family"] == "discord_messages" and item["status"] == "not_searched" for item in found["coverage"]["families"]))

    def test_cross_source_cryptid(self):
        found = search(ROOT, "cryptid", limit=50)
        classes = {hit["record_class"] for hit in found["hits"]}
        self.assertIn("source_container", classes)
        self.assertIn("evidence", classes)
        self.assertTrue(any(hit["record_id"] == "BCE-000014" for hit in found["hits"]))
        self.assertTrue(any(hit["path"].startswith("sources/roanoke-s5-legends/google-sites/") for hit in found["hits"]))
        authorities = {hit["authority"] for hit in found["hits"]}
        self.assertIn("source_catalog", authorities)
        self.assertIn("attributable_evidence", authorities)
        self.assertNotIn("evaluation", authorities)

    def test_project_filter_splits_golden_dawn(self):
        season3 = search(ROOT, "Golden Dawn", project="Roanoke S3", limit=50)
        self.assertEqual(season3["project"], "roanoke-s3")
        self.assertTrue(any(hit["record_class"] == "derived_case" for hit in season3["hits"]))
        self.assertFalse(any(hit["path"].startswith("sources/roanoke-s5-legends/") for hit in season3["hits"]))
        season5 = search(ROOT, "Golden Dawn", project="roanoke-s5-legends", limit=50)
        self.assertTrue(any(hit["record_id"] == "BCS-000106" and hit["body_status"] == "present" for hit in season5["hits"]))
        self.assertFalse(any(hit["record_id"].startswith("BDC-S3-") for hit in season5["hits"]))

    def test_provenance_from_case_to_inaccessible_evidence(self):
        found = evidence(ROOT, "BDC-S3-001")
        self.assertTrue(found["found"])
        self.assertEqual(found["record"]["authority"], "derived_case")
        resolved = {item["cite"]: item for item in found["cites_resolved"]}
        self.assertIn("BCS-000045", resolved)
        self.assertEqual(resolved["BCS-000045"]["body_status"], "catalog_only")
        self.assertEqual(resolved["BCS-000045"]["record"]["attributes"]["project_label"], "Roanoke")
        messages = [item for item in found["cites_resolved"] if item["kind"] == "discord_message_candidate"]
        self.assertTrue(any(item["cite"] == "discord-message:741819860043956335" for item in messages))
        self.assertTrue(all(item["body_status"] == "inaccessible" for item in messages))

    def test_reverse_provenance_from_catalog_container(self):
        found = evidence(ROOT, "BCS-000045")
        self.assertTrue(found["found"])
        self.assertEqual(found["record"]["body_status"], "catalog_only")
        incoming = {item["record_id"] for item in found["cited_by"]}
        self.assertIn("BDC-S3-001", incoming)
        linked = related(ROOT, "BCS-000045")
        self.assertTrue(any(link.get("record", {}).get("record_id") == "BDC-S3-001" for link in linked["links"]))

    def test_timeline_separates_capture_time_from_evidence_dates(self):
        found = timeline(ROOT, "cryptid", limit=50)
        dated_ids = [item["record_id"] for item in found["dated"]]
        self.assertIn("BCE-000014", dated_ids)
        self.assertEqual(dated_ids, sorted(dated_ids, key=lambda item: (next(row["date_start"] for row in found["dated"] if row["record_id"] == item), item)))
        self.assertTrue(all(item["date_kind"] != "archive_capture" for item in found["dated"]))
        capture_paths = {item["path"] for item in found["capture_time_only"]}
        self.assertTrue(any("google-sites/" in item for item in capture_paths))
        self.assertTrue(found["capture_time_only"])
        self.assertTrue(all(not item.get("date_start") for item in found["capture_time_only"]))

    def test_halfwudgie_uses_canonical_bcs_instead_of_a_minted_id(self):
        found = search(ROOT, "Halfwudgie", limit=20)
        self.assertGreater(found["total"], 0)
        self.assertTrue(any(hit["record_id"] == "BCS-000107" and hit["body_status"] == "present" for hit in found["hits"]))
        self.assertFalse(any(hit["record_id"].startswith("access:site:") for hit in found["hits"]))

    def test_evaluation_is_excluded_unless_requested(self):
        hidden = search(ROOT, "persona-continuity")
        self.assertEqual(hidden["total"], 0)
        families = {item["family"]: item for item in hidden["coverage"]["families"]}
        self.assertEqual(families["kit_evaluation"]["status"], "not_in_default_search")
        self.assertEqual(families["kit_evaluation"]["coverage"], "EXCLUDED")
        self.assertEqual(families["kit_evaluation"]["reasons"], ["intentionally_excluded"])
        shown = search(ROOT, "persona-continuity", include_evaluation=True, limit=5)
        self.assertGreater(shown["total"], 0)
        self.assertTrue(all(hit["path"].startswith("research/kit-evaluation/") for hit in shown["hits"]))
        shown_families = {item["family"]: item for item in shown["coverage"]["families"]}
        self.assertEqual(shown_families["kit_evaluation"]["coverage"], "EXHAUSTIVE")
        self.assertEqual(shown_families["kit_evaluation"]["reasons"], [])

    def test_sqlite_bytes_are_not_treated_as_inaccessible(self):
        hydrated = assess_database_access({"hydrated_sqlite": 3})
        self.assertEqual(hydrated["coverage"], "NOT_SEARCHED")
        self.assertEqual(hydrated["bytes"], "present")
        self.assertEqual(hydrated["reasons"], [])
        self.assertTrue(hydrated["query_path"])
        mixed = assess_database_access({"hydrated_sqlite": 1, "git_lfs_pointer": 1})
        self.assertEqual(mixed["coverage"], "PARTIAL")
        self.assertEqual(mixed["reasons"], ["lfs_pointer_only"])
        self.assertNotIn("binary", " ".join(mixed["reasons"]))

    def test_audit_reports_mixed_drive_and_open_gaps(self):
        found = audit(ROOT)
        self.assertGreater(found["counts"]["searchable_records"], 0)
        self.assertGreater(found["counts"]["catalog_only_records"], 0)
        self.assertEqual(found["counts"]["inaccessible_databases"], 3)
        self.assertEqual(found["counts"]["databases_with_bytes"], 0)
        self.assertGreater(found["counts"]["excluded_files"]["research/kit-evaluation"], 0)
        gap_ids = {item["id"] for item in found["gaps"]}
        self.assertEqual(gap_ids, {"discord_text_export", "legacy_drive_bodies"})
        self.assertEqual(found["coverage_report"]["status"], "PARTIAL")

    def test_sources_for_season_5_lists_sites_and_omits_ambiguous_roanoke(self):
        found = sources(ROOT, "Season 5")
        self.assertEqual(found["project_id"], "roanoke-s5-legends")
        published = [row for row in found["source_containers"] if row["body_status"] == "present" and "google-sites/" in row["path"]]
        self.assertGreater(len(published), 0)
        self.assertEqual(found["counts"]["discord_servers"], 0)
        self.assertGreaterEqual(found["omitted_ambiguous_catalog"]["count"], 1)

    def test_export_bundle_is_machine_readable(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "golden-dawn.json"
            bundle = export_bundle(ROOT, "Golden Dawn", project="roanoke-s3", limit=10, out_path=destination)
            self.assertEqual(bundle["bundle_type"], "bfdm_access_export/v1")
            written = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(written["project"], "roanoke-s3")
            self.assertTrue(written["coverage"]["absence_is_not_evidence"])
            self.assertGreater(written["total"], 0)
            self.assertTrue(any(item["cite"] == "BCS-000045" for item in written["provenance"]))

    def test_cli_coverage_json(self):
        completed = subprocess.run(
            [sys.executable, "-m", "access", "coverage"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertIn("families", payload)
        self.assertTrue(payload["absence_is_not_evidence"])


if __name__ == "__main__":
    unittest.main()
