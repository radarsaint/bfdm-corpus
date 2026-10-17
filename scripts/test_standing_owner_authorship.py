#!/usr/bin/env python3
"""A new first-party container is Brendon's without another attestation."""

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "ingest"))
sys.path.insert(0, str(ROOT / "scripts"))

from authorship_policy import (  # noqa: E402
    OBSOLETE_BOILERPLATE,
    container_authorship,
    ingest_first_party_container,
)
from build_documents_sqlite import authorship_status, build  # noqa: E402


ATTESTATION = ROOT / "ingest" / "reports" / "2026-10-09-owner-attestation.json"
LIVE_POLICY_FILES = (
    ROOT / "INGESTION_CONTRACT.md",
    ROOT / "ingest" / "WORK_GPT_TASK.md",
    ROOT / "ingest" / "validate_ingest.py",
    ROOT / "ingest" / "document_archive_schema.sql",
    ROOT / "ingest" / "source_metadata.schema.json",
    ROOT / "scripts" / "port_operational_sources.py",
    ROOT / "scripts" / "build_documents_sqlite.py",
    ROOT / "research" / "drive-inventory" / "2026-10-17" / "README.md",
    ROOT / "research" / "drive-inventory" / "2026-10-03" / "candidates.jsonl",
    ROOT / "PROJECT_CONTROL.md",
    ROOT / "research" / "STATUS.md",
)


def metadata(corpus_id: str) -> dict:
    matches = list(ROOT.glob(f"sources/**/{corpus_id}/metadata.json"))
    matches += list(ROOT.glob(f"context/**/{corpus_id}/metadata.json"))
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


class StandingOwnerAuthorshipTest(unittest.TestCase):
    def test_new_first_party_document_is_brendon_without_a_new_attestation(self):
        admitted = ingest_first_party_container(
            {
                "corpus_id": "BCS-999999",
                "title": "Hypothetical new BFDM note",
                "original_filename": None,
                "source_relationship": None,
                "archival_provenance": {
                    "status": "UNKNOWN",
                    "unresolved_fields": ["source_relationship", "revision_bodies"],
                },
                "authorship": {
                    "status": "UNKNOWN",
                    "basis": "not in the 2026-10-09 owner-attestation set",
                    "project_ownership_context": "Drive file owner at capture: someone else.",
                },
            }
        )
        authorship = admitted["authorship"]
        self.assertEqual(authorship["status"], "BRENDON")
        self.assertEqual(authorship["creator"], "Brendon Faulkner")
        self.assertEqual(authorship["copyright_owner"], "Brendon Faulkner")
        self.assertEqual(authorship["attribution"]["basis_kind"], "standing_owner_declaration")
        self.assertNotIn("attested_on", authorship["attribution"])
        self.assertEqual(
            authorship["project_ownership_context"],
            "Drive file owner at capture: someone else.",
        )
        archival = admitted["archival_provenance"]
        self.assertEqual(archival["status"], "UNKNOWN")
        self.assertIn("original_filename", archival["unresolved_fields"])
        self.assertIn("source_relationship", archival["unresolved_fields"])
        self.assertNotEqual(authorship["status"], archival["status"])
        report = ATTESTATION.read_text(encoding="utf-8")
        self.assertNotIn("BCS-999999", report)
        blob = json.dumps(admitted["authorship"])
        for phrase in OBSOLETE_BOILERPLATE:
            self.assertNotIn(phrase, blob)

    def test_missing_status_does_not_invent_unknown(self):
        self.assertEqual(authorship_status({}), "BRENDON")
        self.assertEqual(container_authorship(None, None)["status"], "BRENDON")
        self.assertEqual(container_authorship("UNKNOWN", "not yet attested")["status"], "BRENDON")
        kept = container_authorship("OTHER_AUTHOR", "The manuscript is credited to Michael Kennish.")
        self.assertEqual(kept["status"], "OTHER_AUTHOR")
        collaborative = container_authorship("COLLABORATIVE", "Named byline.")
        self.assertEqual(collaborative["status"], "COLLABORATIVE")
        schema = (ROOT / "ingest" / "document_archive_schema.sql").read_text(encoding="utf-8")
        self.assertIn("DEFAULT 'BRENDON'", schema)
        self.assertNotIn("DEFAULT 'UNKNOWN'", schema)

    def test_obsolete_boilerplate_is_gone_from_live_policy(self):
        for path in LIVE_POLICY_FILES:
            text = path.read_text(encoding="utf-8")
            for phrase in OBSOLETE_BOILERPLATE:
                self.assertNotIn(phrase, text, f"{path} still contains {phrase}")
        port = (ROOT / "scripts" / "port_operational_sources.py").read_text(encoding="utf-8")
        self.assertNotIn('or "UNKNOWN"', port)
        builder = (ROOT / "scripts" / "build_documents_sqlite.py").read_text(encoding="utf-8")
        self.assertNotIn('return "UNKNOWN"', builder)

    def test_admitted_batch_is_brendon_and_other_attributions_stay(self):
        for number in range(196, 258):
            corpus_id = f"BCS-{number:06d}"
            meta = metadata(corpus_id)
            authorship = meta["authorship"]
            archival = meta["archival_provenance"]
            self.assertEqual(authorship["status"], "BRENDON", corpus_id)
            self.assertEqual(authorship["attribution"]["basis_kind"], "standing_owner_declaration")
            self.assertNotIn("attested_on", authorship["attribution"])
            self.assertNotEqual(authorship["status"], archival["status"])
            self.assertTrue(archival["unresolved_fields"])
            questions = [item.get("question") for item in meta["historical_context"]["not_established"]]
            self.assertNotIn("authorship", questions)
            public = {key: value for key, value in authorship.items() if key != "superseded_authorship_record"}
            blob = json.dumps({"authorship": public, "warnings": meta["normalization"]["warnings"]})
            for phrase in OBSOLETE_BOILERPLATE:
                self.assertNotIn(phrase, blob, corpus_id)
            self.assertEqual(authorship["superseded_authorship_record"]["former_status"], "UNKNOWN")
            catalog = catalog_row(corpus_id)
            self.assertEqual(catalog["authorship"], "BRENDON")
            self.assertEqual(catalog["attribution_basis_kind"], "standing_owner_declaration")
            self.assertNotIn("attribution_attested_on", catalog)
            self.assertEqual(catalog["creator"], "Brendon Faulkner")
        self.assertEqual(metadata("BCS-000077")["authorship"]["status"], "COLLABORATIVE")
        self.assertEqual(metadata("BCS-000059")["authorship"]["status"], "OTHER_AUTHOR")
        self.assertEqual(metadata("BCS-000118")["authorship"]["status"], "OTHER_AUTHOR")
        self.assertEqual(metadata("BCS-000046")["authorship"]["status"], "MIXED_OR_PARTIALLY_VERIFIED")
        self.assertEqual(catalog_row("BCS-000152")["authorship"], "MIXED_CONVERSATION_PARTIAL")
        self.assertEqual(catalog_row("BCS-000172")["authorship"], "MIXED_ROLE_TRANSCRIPT")
        # The October 9 correction batch stays a dated attestation, not the standing default.
        attested = metadata("BCS-000001")["authorship"]
        self.assertEqual(attested["status"], "BRENDON")
        self.assertEqual(attested["attribution"]["basis_kind"], "owner_attestation")
        self.assertEqual(attested["attribution"]["attested_on"], "2026-10-09")

    def test_rebuilt_index_keeps_standing_authorship_off_archival_gaps(self):
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "documents.sqlite"
            result = build(ROOT, db_path)
            self.assertEqual(result["integrity_check"], "ok")
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                """
                SELECT authorship_status, attribution_basis_kind, attested_on,
                       archival_provenance_status, creator
                FROM source_containers WHERE corpus_id = 'BCS-000196'
                """
            ).fetchone()
            self.assertEqual(row["authorship_status"], "BRENDON")
            self.assertEqual(row["attribution_basis_kind"], "standing_owner_declaration")
            self.assertIsNone(row["attested_on"])
            self.assertNotEqual(row["authorship_status"], row["archival_provenance_status"])
            self.assertEqual(row["creator"], "Brendon Faulkner")
            unknown = conn.execute(
                "SELECT COUNT(*) FROM source_containers WHERE authorship_status = 'UNKNOWN'"
            ).fetchone()[0]
            self.assertEqual(unknown, 0)
            conn.close()


if __name__ == "__main__":
    unittest.main()
