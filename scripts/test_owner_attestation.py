#!/usr/bin/env python3
"""Owner attestation must not be confused with archival provenance."""

import hashlib
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from build_documents_sqlite import build


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "ingest" / "reports" / "2026-10-09-owner-attestation.json"


def metadata(corpus_id: str, report: dict | None = None) -> dict:
    if report is not None:
        row = next(item for item in report["records"] if item["corpus_id"] == corpus_id)
        return json.loads((ROOT / row["metadata_path"]).read_text(encoding="utf-8"))
    matches = list(ROOT.glob(f"sources/**/{corpus_id}/metadata.json"))
    if len(matches) != 1:
        raise AssertionError(matches)
    return json.loads(matches[0].read_text(encoding="utf-8"))


def catalog_row(corpus_id: str) -> dict:
    for line in (ROOT / "evidence" / "catalog.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("corpus_id") == corpus_id:
            return row
    raise AssertionError(corpus_id)


class OwnerAttestationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(REPORT.read_text(encoding="utf-8"))
        cls.tmp = tempfile.TemporaryDirectory()
        cls.db_path = Path(cls.tmp.name) / "documents.sqlite"
        cls.result = build(ROOT, cls.db_path)
        cls.conn = sqlite3.connect(cls.db_path)
        cls.conn.row_factory = sqlite3.Row

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        cls.tmp.cleanup()

    def test_inventory_count(self):
        records = self.report["records"]
        self.assertEqual(self.report["before_unknown_authorship"], 171)
        self.assertEqual(self.report["records_corrected"], 171)
        self.assertEqual(len(records), 171)
        self.assertEqual(len({row["corpus_id"] for row in records}), 171)

    def test_attested_records_are_brendon_and_archival_gaps_stay_gaps(self):
        self.assertEqual(self.result["integrity_check"], "ok")
        for row in self.report["records"]:
            corpus_id = row["corpus_id"]
            meta = metadata(corpus_id, self.report)
            authorship = meta["authorship"]
            archival = meta["archival_provenance"]
            self.assertEqual(authorship["status"], "BRENDON")
            self.assertEqual(authorship["creator"], "Brendon Faulkner")
            self.assertEqual(authorship["copyright_owner"], "Brendon Faulkner")
            self.assertEqual(authorship["attribution"]["basis_kind"], "owner_attestation")
            self.assertEqual(authorship["attribution"]["attested_on"], "2026-10-09")
            self.assertEqual(authorship["attribution"]["attested_by"], "Brendon Faulkner")
            self.assertNotEqual(authorship["status"], archival["status"])
            self.assertEqual(archival["unresolved_fields"], row["unresolved_archival_fields"])
            self.assertEqual(archival["status"], row["archival_provenance_status"])
            if not meta.get("original_filename"):
                self.assertIn("original_filename", archival["unresolved_fields"])
                self.assertEqual(authorship["status"], "BRENDON")
            catalog = catalog_row(corpus_id)
            self.assertEqual(catalog["authorship"], "BRENDON")
            self.assertEqual(catalog["creator"], "Brendon Faulkner")
            self.assertEqual(catalog["copyright_owner"], "Brendon Faulkner")
            self.assertNotEqual(catalog["authorship"], "UNKNOWN")
            indexed = self.conn.execute(
                """
                SELECT authorship_status, creator, copyright_owner, attribution_basis_kind,
                       attested_on, archival_provenance_status
                FROM source_containers WHERE corpus_id = ?
                """,
                (corpus_id,),
            ).fetchone()
            self.assertEqual(indexed["authorship_status"], "BRENDON")
            self.assertEqual(indexed["creator"], "Brendon Faulkner")
            self.assertEqual(indexed["copyright_owner"], "Brendon Faulkner")
            self.assertEqual(indexed["attribution_basis_kind"], "owner_attestation")
            self.assertEqual(indexed["attested_on"], "2026-10-09")
            self.assertEqual(indexed["archival_provenance_status"], archival["status"])
            self.assertNotEqual(indexed["authorship_status"], indexed["archival_provenance_status"])
            for rep in meta.get("representations") or []:
                payload = (ROOT / rep["path"]).read_bytes()
                digest = hashlib.sha256(payload).hexdigest()
                self.assertEqual(digest, rep["sha256"])
            frozen = {item["path"]: item["sha256"] for item in row["representation_sha256"]}
            for rep in meta.get("representations") or []:
                self.assertEqual(rep["sha256"], frozen[rep["path"]])

    def test_other_statuses_were_not_relabeled(self):
        self.assertEqual(metadata("BCS-000182")["authorship"]["status"], "BRENDON")
        self.assertNotIn("attribution", metadata("BCS-000182")["authorship"])
        self.assertNotIn("archival_provenance", metadata("BCS-000182"))
        collaborative = [
            meta
            for meta_path in ROOT.glob("sources/**/metadata.json")
            if (meta := json.loads(meta_path.read_text(encoding="utf-8")))
            and (
                meta.get("authorship", {}).get("status")
                if isinstance(meta.get("authorship"), dict)
                else meta.get("authorship")
            )
            == "COLLABORATIVE"
        ]
        self.assertEqual(len(collaborative), 5)
        for meta in collaborative:
            self.assertNotIn("attribution", meta["authorship"])

    def test_superseded_record_is_not_the_live_status(self):
        meta = metadata("BCS-000149")
        superseded = meta["authorship"]["superseded_authorship_record"]
        self.assertEqual(superseded["former_status"], "UNKNOWN")
        self.assertIn("Anthony S", superseded["former_basis"])
        questions = [
            item.get("question")
            for item in meta["historical_context"]["not_established"]
        ]
        self.assertNotIn("brendon_authorship", questions)
        self.assertIn("exact_project", questions)
        self.assertEqual(meta["authorship"]["project_ownership_context"], "Owned and last modified by Anthony S.")


if __name__ == "__main__":
    unittest.main()
