#!/usr/bin/env python3
"""Show that the reviewed tranche passes, and that a real change would not.

The committed ledger is not rewritten. Mutations are written to a temporary
ledger and then discarded. Semantic statuses are not changed.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import validate_research_evidence as vre


def _load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _dump(records: list[dict], path: Path) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in records), encoding="utf-8")


def _expect(result: vre.ValidationResult, needle: str) -> None:
    if result.ok or not any(needle in error for error in result.errors):
        joined = "\n".join(result.errors[:12])
        raise SystemExit(f"expected {needle!r} and a failed validation.\n{joined}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    ledger_path = root / vre.LEDGER
    original = ledger_path.read_text(encoding="utf-8")
    unchanged = vre.validate_repo(root)
    if not unchanged.ok:
        print("\n".join(unchanged.errors[:20]))
        raise SystemExit("unchanged reviewed evidence failed")
    print("unchanged reviewed evidence: PASS")

    records = _load(ledger_path)
    records[0]["propositions"][0]["digest"] = "sha256:" + ("0" * 64)
    with tempfile.TemporaryDirectory() as tmp:
        changed = Path(tmp) / "ledger.jsonl"
        _dump(records, changed)
        proposition = vre.validate_repo(root, changed)
    _expect(proposition, "REQUIRES_REVALIDATION")
    print("changed proposition digest: REQUIRES_REVALIDATION")

    records = _load(ledger_path)
    source = records[0]["evidence"]["sources"][0]
    source["representation_sha256"] = "0" * 64
    with tempfile.TemporaryDirectory() as tmp:
        changed = Path(tmp) / "ledger.jsonl"
        _dump(records, changed)
        evidence = vre.validate_repo(root, changed)
    _expect(evidence, "REQUIRES_REVALIDATION")
    print("changed evidence representation: REQUIRES_REVALIDATION")

    records = _load(ledger_path)
    identity = next(
        dep for record in records for dep in record.get("dependencies", [])
        if dep.get("type") == "IDENTITY_ASSERTION"
    )
    identity["digest"] = "sha256:" + ("ab" * 32)
    with tempfile.TemporaryDirectory() as tmp:
        changed = Path(tmp) / "ledger.jsonl"
        _dump(records, changed)
        ident = vre.validate_repo(root, changed)
    _expect(ident, "identity dependency changed")
    print("changed identity dependency: FAIL CLOSED")

    if ledger_path.read_text(encoding="utf-8") != original:
        raise SystemExit("the committed ledger was rewritten")
    print("committed ledger unchanged: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
