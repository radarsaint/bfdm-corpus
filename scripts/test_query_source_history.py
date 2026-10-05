#!/usr/bin/env python3
"""Source-history questions follow recorded links, including incoming ones."""

import unittest
from pathlib import Path

from query_source_history import orient


ROOT = Path(__file__).resolve().parents[1]


class QuerySourceHistoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from query_source_history import load_records

        cls.records = load_records(ROOT)

    def test_revision_is_visible_from_the_earlier_manuscript(self):
        report = orient(self.records, "BCS-000045")
        owners = {row["owner"] for row in report["came_after"]}
        self.assertIn("BCS-000041", owners)
        self.assertTrue(all(row["link_type"] == "REVISES" for row in report["came_after"]))

    def test_brainstorm_is_not_given_a_predecessor_link_it_does_not_have(self):
        report = orient(self.records, "BCS-000043")
        self.assertEqual(report["came_before"], [])
        self.assertEqual(report["came_after"], [])
        self.assertIn("BCS-000045", report["family_members"])

    def test_airship_module_names_flight_school_and_not_the_whole_directory(self):
        report = orient(self.records, "BCS-000073")
        self.assertEqual(report["document_family_id"], "empire-city-airship-qualification")
        locators = {row["external_locator"] for row in report["live_contact"]}
        self.assertIn("discord://850779382791536640/channel/852796918836232192", locators)
        self.assertFalse(report["live_use_unresolved"])
        questions = {item["question"] for item in report["not_established"]}
        self.assertIn("rule_by_rule_live_identity", questions)
        directory = orient(self.records, "BCS-000072")
        self.assertNotEqual(directory["document_family_id"], report["document_family_id"])
        self.assertEqual(directory["live_contact"], [])

    def test_novel_draft_stage_stays_unresolved(self):
        report = orient(self.records, "BCS-000060")
        self.assertEqual(report["production_stages"], [])
        self.assertTrue(report["production_stage_unresolved"])
        self.assertTrue(report["came_after"])


if __name__ == "__main__":
    unittest.main()
