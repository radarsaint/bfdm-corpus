#!/usr/bin/env python3
"""Readiness split: an explicit gap is not a trajectory."""

import unittest

from validate_source_history import classify_family


def meta(cid, links=None, gaps=None, stages=None, role=None):
    return {
        "corpus_id": cid,
        "source_role": role,
        "historical_context": {
            "project_links": [
                {
                    "relation": "BELONGS_TO_PROJECT",
                    "project_id": "roanoke-s3",
                    "confidence": "STRONG",
                    "basis": "test",
                    "support_refs": [cid],
                }
            ],
            "production_stages": stages
            or [{"stage": "PREPRODUCTION", "confidence": "STRONG", "basis": "test", "support_refs": [cid]}],
            "not_established": gaps or [],
        },
        "source_links": links or [],
    }


class ReadinessSplitTest(unittest.TestCase):
    def test_live_gap_is_not_longitudinal(self):
        row = classify_family(
            ["BCS-1"],
            [meta("BCS-1", gaps=[{"question": "live_use", "status": "NOT_ESTABLISHED", "basis": "none"}])],
            [],
            [True],
            True,
        )
        self.assertTrue(row["source_research_ready"])
        self.assertEqual(row["longitudinal_status"], "LONGITUDINAL_RESEARCH_GAP")

    def test_revision_without_play(self):
        link = {"link_type": "REVISES", "to_corpus_id": "BCS-1", "confidence": "STRONG", "basis": "test"}
        row = classify_family(
            ["BCS-1", "BCS-2"],
            [
                meta("BCS-1", gaps=[{"question": "live_use", "status": "NOT_ESTABLISHED", "basis": "x"}]),
                meta("BCS-2", links=[link], gaps=[{"question": "live_use", "status": "NOT_ESTABLISHED", "basis": "x"}]),
            ],
            [link],
            [True, True],
            True,
        )
        self.assertEqual(row["longitudinal_status"], "LONGITUDINAL_RESEARCH_READY")
        self.assertEqual(row["trajectory"], "revision")

    def test_publication_is_not_live_contact(self):
        link = {"link_type": "PUBLISHED_AS", "to_corpus_id": "BCS-9", "confidence": "STRONG", "basis": "test"}
        row = classify_family(
            ["BCS-1"],
            [meta("BCS-1", links=[link], gaps=[{"question": "live_use", "status": "NOT_ESTABLISHED", "basis": "x"}])],
            [link],
            [True],
            True,
        )
        self.assertEqual(row["longitudinal_status"], "LONGITUDINAL_RESEARCH_GAP")

    def test_implemented_in_is_live_contact(self):
        link = {
            "link_type": "IMPLEMENTED_IN",
            "external_locator": "discord://1/channel/2",
            "confidence": "STRONG",
            "basis": "test",
        }
        row = classify_family(
            ["BCS-1"],
            [meta("BCS-1", links=[link])],
            [link],
            [True],
            True,
        )
        self.assertEqual(row["trajectory"], "live_contact")

    def test_context_is_not_precedent(self):
        row = classify_family(
            ["BCS-59"],
            [meta("BCS-59", role="CONTEXT_ONLY_THIRD_PARTY", stages=[], gaps=[
                {"question": "production_stage", "status": "NOT_ESTABLISHED", "basis": "x"}
            ])],
            [],
            [True],
            True,
        )
        self.assertFalse(row["source_research_ready"])
        self.assertEqual(row["longitudinal_status"], "NOT_PRECEDENT")


if __name__ == "__main__":
    unittest.main()
