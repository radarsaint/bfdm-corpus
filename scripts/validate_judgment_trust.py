#!/usr/bin/env python3
"""Fail closed when derived wording is treated as verified DM judgment.

This checker does not decide whether a historical claim is true. It rejects
the upgrade from citation, confidence label, or draft contrast to standing
practice or a Kit instruction.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TOKEN = "NOT_A_STANDING_PRACTICE"
KIT_FORBIDDEN = "NOT_AUTHORIZED"
SAMPLING_MARKER = Path("research/integrity/SAMPLING_PHASE_COMPLETE")
REGISTER = Path("research/integrity/judgment-claim-register.jsonl")
VERDICTS = Path("research/integrity/contrast-family-verdicts.jsonl")
PACKET = Path("research/integrity/generated/roanoke-s3-decision-cases-v1.review.md")
OPENING_LINES = 80

MD_TRIGGERS = (
    re.compile(r"Reusable judgment", re.I),
    re.compile(r"\*\*Confidence:\*\*\s+(very\s+)?high\b", re.I),
    re.compile(r"(?m)^Confidence:\s+high\b", re.I),
    re.compile(r"high-signal findings"),
    re.compile(r"Provisional S4 model"),
    re.compile(r"Phase 2 hypothesis"),
    re.compile(r"Strong persistence candidate"),
    re.compile(r"Current S3 judgment hypotheses"),
    re.compile(r"Underlying principle", re.I),
    re.compile(r"GENERAL_DM_INSTINCT_CANDIDATE"),
    re.compile(r"GENERAL_DM_AND_SYSTEM_JUDGMENT_CANDIDATE"),
)
JSON_CONFIDENCE = re.compile(r'"confidence"\s*:\s*"(?:very\s+)?high\b', re.I)
JSON_JUDGMENT_KEY = re.compile(
    r'"(?:reusable_judgment|decision_rule|judgment|underlying_principle)"\s*:',
    re.I,
)
ALLOWED_TRUST = {
    "AUDITED_REUSABLE_JUDGMENTS_OVERCLAIMED",
    "UNVERIFIED_DERIVED_WORDING",
    "PROVISIONAL_SYNTHESIS",
    "ADVERSARIAL_RECORD",
    "DEPENDENCY_NOTE",
    "HISTORICAL_SNAPSHOT",
    "CONTROL_SURFACE",
}
ALLOWED_VERDICTS = {"SUPPORT", "LIMIT", "BREAK", "NEW_DIMENSION", "NOT_COMPARABLE"}
FAMILIES = tuple(f"CF-{i:02d}" for i in range(1, 11))
EXEMPT_PREFIXES = (
    "research/legacy-staging/",
    "research/kit-evaluation/",
)
APPROVED_TRAINING = re.compile(r'"training_status"\s*:\s*"([^"]*APPROVED[^"]*)"')


def opening(text: str, limit: int = OPENING_LINES) -> str:
    return "\n".join(text.splitlines()[:limit])


def triggered_markdown(text: str) -> bool:
    return any(pattern.search(text) for pattern in MD_TRIGGERS)


def triggered_jsonl(text: str) -> bool:
    general = "GENERAL_DM_INSTINCT_CANDIDATE" in text or "GENERAL_DM_AND_SYSTEM_JUDGMENT_CANDIDATE" in text
    return general or (JSON_CONFIDENCE.search(text) is not None and JSON_JUDGMENT_KEY.search(text) is not None)


def iter_research_files(root: Path):
    research = root / "research"
    if not research.is_dir():
        return
    for path in sorted(research.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if rel == PACKET.as_posix():
            continue
        if any(rel.startswith(prefix) for prefix in EXEMPT_PREFIXES):
            continue
        if path.suffix in {".md", ".jsonl"}:
            yield rel, path


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{number}: invalid JSON: {exc}") from exc
    return rows


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    register_path = root / REGISTER
    verdict_path = root / VERDICTS
    if not register_path.is_file():
        return [f"missing judgment register: {REGISTER.as_posix()}"]
    if not verdict_path.is_file():
        return [f"missing contrast verdicts: {VERDICTS.as_posix()}"]

    try:
        register_rows = load_jsonl(register_path)
        verdict_rows = load_jsonl(verdict_path)
    except ValueError as exc:
        return [str(exc)]

    registered: dict[str, dict] = {}
    for row in register_rows:
        path = row.get("path")
        if not path or path in registered:
            errors.append(f"register: duplicate or missing path {path}")
            continue
        registered[path] = row
        if row.get("practice_status") != TOKEN:
            errors.append(f"{path}: register practice_status must be {TOKEN}")
        if row.get("kit_status") != KIT_FORBIDDEN:
            errors.append(f"{path}: register kit_status must be {KIT_FORBIDDEN}")
        if row.get("trust") not in ALLOWED_TRUST:
            errors.append(f"{path}: register trust {row.get('trust')!r} is not fail-closed")
        target = root / path
        if not target.is_file():
            errors.append(f"register path missing: {path}")
            continue
        text = target.read_text(encoding="utf-8")
        if TOKEN not in opening(text) and TOKEN not in text[:4000]:
            errors.append(f"{path}: registered file does not open with {TOKEN}")

    triggered: set[str] = set()
    for rel, path in iter_research_files(root):
        text = path.read_text(encoding="utf-8")
        is_trigger = triggered_markdown(text) if path.suffix == ".md" else triggered_jsonl(text)
        if not is_trigger:
            continue
        triggered.add(rel)
        if TOKEN not in opening(text):
            errors.append(f"{rel}: states a judgment claim without {TOKEN} in the first {OPENING_LINES} lines")
        if rel not in registered:
            errors.append(f"{rel}: judgment claim is not in the register")
        for match in APPROVED_TRAINING.finditer(text):
            status = match.group(1)
            if "NOT_APPROVED" not in status:
                errors.append(f"{rel}: training_status {status} is approved")

    for rel in sorted(registered):
        if rel in triggered:
            continue
        text = (root / rel).read_text(encoding="utf-8") if (root / rel).is_file() else ""
        if TOKEN not in text:
            errors.append(f"{rel}: register entry has no {TOKEN}")

    by_family = {}
    for row in verdict_rows:
        family = row.get("family_id")
        if family in by_family:
            errors.append(f"duplicate contrast verdict {family}")
        by_family[family] = row
    for family in FAMILIES:
        row = by_family.get(family)
        if row is None:
            errors.append(f"missing contrast verdict {family}")
            continue
        if row.get("earthfall_saturday_verdict") not in ALLOWED_VERDICTS:
            errors.append(f"{family}: verdict is not in the allowed set")
        if row.get("draft_confidence_adopted") is not False:
            errors.append(f"{family}: draft confidence label was adopted")
        if row.get("family_certification") != "NOT_CERTIFIED":
            errors.append(f"{family}: family_certification must stay NOT_CERTIFIED until a sampling phase exists")
        if row.get("practice_status") != TOKEN:
            errors.append(f"{family}: practice_status must stay {TOKEN}")
        if row.get("kit_status") != KIT_FORBIDDEN:
            errors.append(f"{family}: kit_status must stay {KIT_FORBIDDEN}")
        if row.get("independent_test_passed") is not False:
            errors.append(f"{family}: independent_test_passed cannot be true in this record")
        record = root / row.get("record", "")
        if not record.is_file():
            errors.append(f"{family}: verdict record missing")
    extra = sorted(set(by_family) - set(FAMILIES))
    if extra:
        errors.append(f"unexpected contrast families: {extra}")

    if (root / SAMPLING_MARKER).exists():
        errors.append(
            f"{SAMPLING_MARKER.as_posix()} exists; this checker will not treat that marker as "
            "certification unless a later explicit sampling review replaces this fail-closed rule"
        )

    packet = root / PACKET
    if packet.is_file():
        packet_text = packet.read_text(encoding="utf-8")
        if "does not authorize Kit to use the claim" not in packet_text:
            errors.append("review packet no longer says a passed chain does not authorize Kit")
        if "not a comprehensive model" not in packet_text:
            errors.append("review packet no longer marks the tranche as nonrepresentative")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    errors = validate(Path(args.root).resolve())
    for error in errors:
        print(f"ERROR: {error}")
    print(f"judgment trust: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
