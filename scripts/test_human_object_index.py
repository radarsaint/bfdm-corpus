#!/usr/bin/env python3
"""Regression tests for the experimental BFDM human-object index."""

from __future__ import annotations

import unittest
from pathlib import Path

from query_human_object import build_report


ROOT = Path(__file__).resolve().parents[1]


class HumanObjectIndexTest(unittest.TestCase):
    def test_rod_alias_resolves(self):
        report = build_report(ROOT, "rod")
        self.assertEqual(report["status"], "RESOLVED")
        self.assertEqual(report["object"]["object_id"], "hobj:earthfall:rod")

    def test_cornerstone_short_name_resolves(self):
        report = build_report(ROOT, "World's Cornerstone")
        self.assertEqual(report["status"], "RESOLVED")
        self.assertEqual(
            report["object"]["object_id"],
            "hobj:at-wars-end:worlds-cornerstone",
        )

    def test_mason_relation_reaches_cornerstone(self):
        report = build_report(ROOT, "The Mason")
        outgoing = {
            (row["relation"], row["other_name"])
            for row in report["relations"]
            if row["direction"] == "OUTGOING"
        }
        self.assertIn(("INSCRIBES", "The World's Cornerstone"), outgoing)

    def test_lamplighters_have_literal_role_assertion(self):
        report = build_report(ROOT, "Lamplighters")
        predicates = {row["predicate"] for row in report["assertions"]}
        self.assertIn("role", predicates)
        self.assertIn("player_role", predicates)
        self.assertIn("BCS-000057", report["source_refs"])

    def test_project_scope_can_resolve(self):
        report = build_report(ROOT, "Bastion", project="bastion-redoubt")
        self.assertEqual(report["status"], "RESOLVED")
        self.assertEqual(report["object"]["object_type"], "PLACE")

    def test_missing_object_is_not_claimed_absent_from_corpus(self):
        report = build_report(ROOT, "definitely not an indexed object")
        self.assertEqual(report["status"], "NOT_INDEXED")
        self.assertIn("not evidence", report["message"].lower())


if __name__ == "__main__":
    unittest.main()
