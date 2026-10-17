#!/usr/bin/env python3
"""The judgment-trust checker rejects the upgrade from wording to practice."""
from __future__ import annotations

import json
import tempfile
import textwrap
import unittest
from pathlib import Path

import validate_judgment_trust as gate


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def minimal_repo(root: Path, claim: str, verdict_override: dict | None = None) -> None:
    write(
        root / "research/integrity/JUDGMENT_TRUST.md",
        "> **Judgment status: NOT_A_STANDING_PRACTICE.**\n",
    )
    write(
        root / "research/integrity/contrast-family-adversarial-v1.md",
        "> **Judgment status: NOT_A_STANDING_PRACTICE.**\n\nNo family is certified.\n",
    )
    rows = []
    for index in range(1, 11):
        row = {
            "family_id": f"CF-{index:02d}",
            "draft_confidence_adopted": False,
            "earthfall_saturday_verdict": "NOT_COMPARABLE",
            "family_certification": "NOT_CERTIFIED",
            "practice_status": "NOT_A_STANDING_PRACTICE",
            "kit_status": "NOT_AUTHORIZED",
            "independent_test_passed": False,
            "record": "research/integrity/contrast-family-adversarial-v1.md",
        }
        if verdict_override and index == 1:
            row.update(verdict_override)
        rows.append(row)
    write(
        root / "research/integrity/contrast-family-verdicts.jsonl",
        "\n".join(json.dumps(row) for row in rows) + "\n",
    )
    write(root / "research/claims.md", claim)
    register = {
        "path": "research/claims.md",
        "trust": "UNVERIFIED_DERIVED_WORDING",
        "practice_status": "NOT_A_STANDING_PRACTICE",
        "kit_status": "NOT_AUTHORIZED",
    }
    write(root / "research/integrity/judgment-claim-register.jsonl", json.dumps(register) + "\n")


class JudgmentTrustTest(unittest.TestCase):
    def test_bare_reusable_judgment_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            minimal_repo(root, "**Reusable judgment.** Always adapt to the players.\n")
            errors = gate.validate(root)
            self.assertTrue(any("claims.md" in error and "NOT_A_STANDING_PRACTICE" in error for error in errors))

    def test_banner_and_register_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            claim = textwrap.dedent(
                """\
                # Claims

                > **Judgment status: NOT_A_STANDING_PRACTICE.** Derived wording only.

                **Reusable judgment.** This sentence is not a practice.
                """
            )
            minimal_repo(root, claim)
            self.assertEqual(gate.validate(root), [])

    def test_support_cannot_authorize_kit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            claim = "> **Judgment status: NOT_A_STANDING_PRACTICE.**\n\n**Reusable judgment.** Local.\n"
            minimal_repo(
                root,
                claim,
                {
                    "earthfall_saturday_verdict": "SUPPORT",
                    "kit_status": "AUTHORIZED",
                    "practice_status": "STANDING_PRACTICE",
                    "independent_test_passed": True,
                    "family_certification": "CERTIFIED",
                    "draft_confidence_adopted": True,
                },
            )
            errors = "\n".join(gate.validate(root))
            self.assertIn("kit_status", errors)
            self.assertIn("practice_status", errors)
            self.assertIn("draft confidence", errors)
            self.assertIn("independent_test_passed", errors)
            self.assertIn("NOT_CERTIFIED", errors)

    def test_unregistered_high_confidence_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            minimal_repo(
                root,
                "> **Judgment status: NOT_A_STANDING_PRACTICE.**\n\n**Reusable judgment.** Local.\n",
            )
            extra = root / "research/other.md"
            extra.write_text("# Other\n\n**Confidence:** high.\n", encoding="utf-8")
            errors = gate.validate(root)
            self.assertTrue(any("other.md" in error and "register" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
