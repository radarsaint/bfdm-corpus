#!/usr/bin/env python3
"""Discovery queries answer the questions the audit actually failed."""

import json
import unittest
from pathlib import Path

from query_archive_gaps import load_gaps, select
from query_project_history import project_report
from query_research_readiness import report
from query_source_family import family_report
from query_source_history import load_records, orient


ROOT = Path(__file__).resolve().parents[1]


class SubstrateQueryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_records(ROOT)

    def test_dev_crafting_doc_does_not_claim_its_own_live_link(self):
        dev = orient(self.records, "BCS-000077")
        self.assertEqual(dev["live_contact"], [])
        locators = {row["external_locator"] for row in dev["family_live_contact"]}
        self.assertIn("discord://636012145204527125/channel/739240413269065890", locators)

    def test_season_five_changelog_is_visible_as_revision_context(self):
        changelog = orient(self.records, "BCS-000113")
        targets = {row["to_corpus_id"] for row in changelog["revision_context"]}
        self.assertIn("BCS-000089", targets)
        self.assertEqual(changelog["came_before"], [])
        self.assertEqual(changelog["came_after"], [])

    def test_family_query_lists_crafting_members(self):
        family = family_report(self.records, "roanoke-crafting-system")
        ids = {row["corpus_id"] for row in family["members"]}
        self.assertEqual(ids, {"BCS-000020", "BCS-000077", "BCS-000078", "BCS-000079", "BCS-000080"})

    def test_project_query_does_not_invent_unplaced_crafting(self):
        project = project_report(self.records, "roanoke-s3")
        ids = {row["corpus_id"] for family in project["families"] for row in family["members"]}
        self.assertNotIn("BCS-000080", ids)
        self.assertIn("BCS-000077", ids)

    def test_archive_gap_ledger_has_the_season_four_timeline(self):
        rows = select(load_gaps(ROOT), "roanoke-s4", None)
        ids = {row["gap_id"] for row in rows}
        self.assertIn("GAP-S4-MASTER-TIMELINE", ids)

    def test_readiness_ready_set_is_thin_edges(self):
        payload = report(ROOT)
        ready = {
            row["document_family_id"]
            for row in payload["families"]
            if row["longitudinal_status"] == "LONGITUDINAL_RESEARCH_READY"
        }
        self.assertIn("roanoke-s3-timeline", ready)
        self.assertNotIn("roanoke-s5-google-sites-revision-process", ready)
        changelog = next(
            row for row in payload["families"] if row["document_family_id"] == "roanoke-s5-google-sites-revision-process"
        )
        self.assertEqual(changelog["longitudinal_status"], "LONGITUDINAL_RESEARCH_GAP")

    def test_candidate_triage_covers_every_unreviewed_row(self):
        ledger = ROOT / "research" / "drive-inventory" / "2026-10-03" / "candidates.jsonl"
        triage = ROOT / "research" / "substrate" / "candidate_triage.jsonl"
        unreviewed = {
            json.loads(line)["drive_id"]
            for line in ledger.read_text(encoding="utf-8").splitlines()
            if line.strip() and json.loads(line)["status"] == "UNREVIEWED_CANDIDATE"
        }
        labeled = [json.loads(line) for line in triage.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual({row["candidate"] for row in labeled}, unreviewed)
        actions = {row["recommended_action"] for row in labeled}
        self.assertIn("HIGH_PRIORITY_INGEST", actions)
        self.assertIn("NEEDS_MANUAL_REVIEW", actions)


if __name__ == "__main__":
    unittest.main()
