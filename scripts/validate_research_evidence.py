#!/usr/bin/env python3
"""Deterministic integrity checks for version-bound BFDM derived research.

This script checks reconstructability and stale state. It does not decide whether
an interpretation of historical evidence is semantically correct.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

TRANCHE_MD = Path("research/roanoke-s3/decision-cases-v1.md")
TRANCHE_JSONL = Path("research/roanoke-s3/decision-cases-v1.jsonl")
LEDGER = Path("research/integrity/audit_ledger.jsonl")
PACKET = Path("research/integrity/generated/roanoke-s3-decision-cases-v1.review.md")
BCS45 = Path("sources/roanoke/BCS-000045/source.md")
BCS45_META = Path("sources/roanoke/BCS-000045/metadata.json")
DISCORD_DB = Path("discord/roanoke-season-3/roanoke-season-3.sqlite")
DISCORD_PROJECTION = Path("model-index/discord/roanoke-season-3")
IDENTITIES = Path("registry/identities.jsonl")
BRENDON_S3_IDENTITY = "identity:brendon:discord:313689699627696139:roanoke-s3"
BRENDON_DISCORD_ID = "313689699627696139"

PROPOSITION_FIELDS = (
    "situation",
    "noticed",
    "values",
    "intervention",
    "observed_result",
    "reusable_judgment",
)

FIELD_LABELS = {
    "Situation": "situation",
    "Prep evidence": "prep_evidence",
    "Live evidence": "live_evidence",
    "What Brendon noticed": "noticed",
    "What mattered": "values",
    "Intervention": "intervention",
    "Observed result": "observed_result",
    "Reusable judgment": "reusable_judgment",
    "Representative line": "representative_line",
    "Confidence": "confidence",
}

SEMANTIC_STATUSES = {
    "VERIFIED_DIRECT",
    "VERIFIED_STRONG_RECONSTRUCTION",
    "PARTIALLY_SUPPORTED",
    "LOCATOR_BROKEN_SUPPORT_RECOVERED",
    "LOCATOR_BROKEN_CLAIM_UNSUPPORTED",
    "ATTRIBUTION_UNRESOLVED",
    "CHRONOLOGY_UNRESOLVED",
    "CAUSALITY_OVERCLAIMED",
    "SCOPE_OVERCLAIMED",
    "CONTEXT_CHANGES_INTERPRETATION",
    "CONTRADICTED",
    "SOURCE_UNAVAILABLE",
    "DERIVED_ONLY_NO_PRIMARY_CHAIN",
    "REQUIRES_REVALIDATION",
    "UNVERIFIED",
}
VERIFIED_STATUSES = {"VERIFIED_DIRECT", "VERIFIED_STRONG_RECONSTRUCTION", "PARTIALLY_SUPPORTED", "LOCATOR_BROKEN_SUPPORT_RECOVERED"}
LOCATOR_OUTCOMES = {
    "CURRENTLY_VALID",
    "MOVED_EXACT_EVIDENCE",
    "REPRESENTATION_DRIFT_RECOVERED",
    "WRONG_ORIGINAL_LOCATOR",
    "WRONG_SOURCE",
    "ORIGINAL_REPRESENTATION_UNAVAILABLE",
    "SUPPORT_NOT_FOUND",
    "UNRESOLVED",
}

CASE_RE = re.compile(r"^### (BDC-S3-\d{3}) — ([^\n]+)$", re.M)
BCS_REF_RE = re.compile(r"(BCS-\d{6}):L(\d+)-L(\d+)")
DISCORD_ID_RE = re.compile(r"`(\d{17,20})`")
PACKET_META_RE = re.compile(r"<!-- BFDM_INTEGRITY_PACKET_META\n(\{.*?\})\n-->", re.S)
NEGATIVE_RE = re.compile(r"\b(no|not|never|none|without|didn't|did not|wasn't|was not|cannot|can't|absent|absence)\b", re.I)
CAUSAL_RE = re.compile(r"\b(because|caused|therefore|led to|resulted in|so that|in response to)\b", re.I)


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def normalize_text(text: str) -> str:
    return " ".join(text.replace("“", '"').replace("”", '"').replace("’", "'").split())


def proposition_digest(text: str) -> str:
    return "sha256:" + sha256_text(normalize_text(text))


def canonical_json_digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "sha256:" + sha256_text(payload)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    if not path.exists():
        return rows
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{n}: invalid JSON: {exc}") from exc
    return rows


def parse_cases_jsonl(path: Path) -> dict[str, dict[str, Any]]:
    rows = read_jsonl(path)
    return {row["id"]: row for row in rows}


def parse_cases_markdown(path: Path) -> dict[str, dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    matches = list(CASE_RE.finditer(text))
    out: dict[str, dict[str, Any]] = {}
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        record: dict[str, Any] = {"id": match.group(1), "title": match.group(2).strip()}
        for label, key in FIELD_LABELS.items():
            pattern = re.compile(r"^\*\*" + re.escape(label) + r"\.\*\*\s*(.*?)$", re.M)
            hit = pattern.search(body)
            if hit:
                record[key] = hit.group(1).strip()
        out[record["id"]] = record
    return out


def compare_markdown_json(md: dict[str, dict[str, Any]], js: dict[str, dict[str, Any]]) -> list[str]:
    issues: list[str] = []
    if list(md) != list(js):
        issues.append(f"Markdown/JSON case IDs diverge: md={list(md)} json={list(js)}")
    for case_id in sorted(set(md) & set(js)):
        keys = set(md[case_id]) | set(js[case_id])
        for key in sorted(keys):
            if normalize_text(str(md[case_id].get(key, ""))) != normalize_text(str(js[case_id].get(key, ""))):
                issues.append(f"{case_id}:{key}: Markdown/JSON divergence")
    return issues


def parse_prep_refs(text: str) -> list[dict[str, Any]]:
    return [
        {"source_id": m.group(1), "line_start": int(m.group(2)), "line_end": int(m.group(3))}
        for m in BCS_REF_RE.finditer(text or "")
    ]


def parse_live_ids(text: str) -> list[str]:
    return [m.group(1) for m in DISCORD_ID_RE.finditer(text or "")]


def excerpt(source_text: str, start: int, end: int) -> str:
    lines = source_text.splitlines()
    if start < 1 or end < start or end > len(lines):
        raise IndexError(f"invalid line range L{start}-L{end}; source has {len(lines)} lines")
    return "\n".join(lines[start - 1:end])


def lfs_oid(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^oid sha256:([0-9a-f]{64})$", text, re.M)
    return m.group(1) if m else None


def identity_row(root: Path, identity_id: str = BRENDON_S3_IDENTITY) -> dict[str, Any] | None:
    for row in read_jsonl(root / IDENTITIES):
        if row.get("identity_id") == identity_id:
            return row
    return None


def find_discord_messages(root: Path, wanted: Iterable[str]) -> dict[str, dict[str, Any]]:
    wanted_set = set(wanted)
    found: dict[str, dict[str, Any]] = {}
    if not wanted_set:
        return found
    base = root / DISCORD_PROJECTION
    for shard in sorted(base.glob("messages-*.jsonl")):
        shard_digest: str | None = None
        for line_no, line in enumerate(shard.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            row = json.loads(line)
            msg_id = str(row.get("id", ""))
            if msg_id not in wanted_set:
                continue
            if shard_digest is None:
                shard_digest = sha256_bytes(shard.read_bytes())
            found[msg_id] = {
                "row": row,
                "row_digest": canonical_json_digest(row),
                "shard_path": shard.relative_to(root).as_posix(),
                "shard_sha256": shard_digest,
                "line": line_no,
            }
        if len(found) == len(wanted_set):
            break
    return found


def evidence_state_digest(record: dict[str, Any]) -> str:
    evidence = record.get("evidence", {})
    stable = {
        "proposition_digest": record.get("proposition", {}).get("digest"),
        "prep": [
            {
                "source_id": x.get("source_id"),
                "representation_path": x.get("representation_path"),
                "representation_sha256": x.get("representation_sha256"),
                "line_start": x.get("line_start"),
                "line_end": x.get("line_end"),
                "excerpt_digest": x.get("excerpt_digest"),
            }
            for x in evidence.get("prep", [])
        ],
        "live": [
            {
                "message_id": x.get("message_id"),
                "canonical_database_sha256": x.get("canonical_database_sha256"),
                "projection_row_digest": x.get("projection_row_digest"),
                "expected_author_id": x.get("expected_author_id"),
            }
            for x in evidence.get("live", [])
        ],
        "dependencies": [
            {"type": x.get("type"), "id": x.get("id"), "digest": x.get("digest")}
            for x in record.get("dependencies", [])
        ],
    }
    return canonical_json_digest(stable)


def global_packet_state(records: Iterable[dict[str, Any]]) -> str:
    states = sorted((r["audit_id"], r.get("prepared_state_sha256")) for r in records)
    return canonical_json_digest(states)


def infer_flags(text: str) -> list[str]:
    flags: list[str] = []
    if NEGATIVE_RE.search(text or ""):
        flags.append("NEGATIVE_OR_ABSENCE_CLAIM")
    if CAUSAL_RE.search(text or ""):
        flags.append("CAUSALITY_CLAIM")
    return flags


def default_semantic_status() -> str:
    return "UNVERIFIED"


def classify_historical_locator(
    *,
    current_excerpt: str | None,
    expected_excerpt: str | None,
    historical_excerpts: list[str] | None = None,
    original_representation_available: bool = True,
) -> str:
    """Small deterministic helper used by forensic tests.

    Semantic support is deliberately outside this function. It only compares exact
    evidence text across representations.
    """
    historical_excerpts = historical_excerpts or []
    if expected_excerpt is not None and current_excerpt == expected_excerpt:
        return "CURRENTLY_VALID"
    if expected_excerpt is not None and expected_excerpt in historical_excerpts:
        return "REPRESENTATION_DRIFT_RECOVERED"
    if not original_representation_available:
        return "ORIGINAL_REPRESENTATION_UNAVAILABLE"
    if expected_excerpt is not None and current_excerpt is not None:
        return "SUPPORT_NOT_FOUND"
    return "UNRESOLVED"


def packet_meta(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    m = PACKET_META_RE.search(path.read_text(encoding="utf-8"))
    return json.loads(m.group(1)) if m else None


def validate_repo(root: Path, ledger_path: Path | None = None, packet_path: Path | None = None) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    ledger_path = ledger_path or (root / LEDGER)
    packet_path = packet_path or (root / PACKET)

    for rel in (TRANCHE_MD, TRANCHE_JSONL):
        if not (root / rel).exists():
            errors.append(f"missing audited artifact: {rel}")
    if errors:
        return ValidationResult(errors, warnings)

    md = parse_cases_markdown(root / TRANCHE_MD)
    js = parse_cases_jsonl(root / TRANCHE_JSONL)
    errors.extend(compare_markdown_json(md, js))

    records = read_jsonl(ledger_path)
    by_key = {(r.get("artifact", {}).get("case_id"), r.get("artifact", {}).get("field")): r for r in records}
    expected = {(case_id, field) for case_id in js for field in PROPOSITION_FIELDS}
    actual = set(by_key)
    for missing in sorted(expected - actual):
        errors.append(f"{missing[0]}:{missing[1]}: missing audit record; new propositions default to UNVERIFIED")
    for extra in sorted(actual - expected):
        errors.append(f"{extra[0]}:{extra[1]}: audit record has no current proposition")

    source_path = root / BCS45
    source_text = source_path.read_text(encoding="utf-8") if source_path.exists() else None
    source_sha = sha256_text(source_text) if source_text is not None else None
    db_sha = lfs_oid(root / DISCORD_DB)

    all_ids = set()
    for case in js.values():
        all_ids.update(parse_live_ids(case.get("live_evidence", "")))
    discord = find_discord_messages(root, all_ids)
    ident = identity_row(root)
    ident_digest = canonical_json_digest(ident) if ident else None

    for key in sorted(expected & actual):
        case_id, field = key
        rec = by_key[key]
        prop = rec.get("proposition", {})
        current_text = js[case_id].get(field, "")
        current_prop_digest = proposition_digest(current_text)
        if prop.get("digest") != current_prop_digest:
            errors.append(f"{case_id}:{field}: claim-version drift; REQUIRES_REVALIDATION")
        if normalize_text(str(prop.get("text", ""))) != normalize_text(str(current_text)):
            errors.append(f"{case_id}:{field}: stored proposition text differs from current artifact")

        semantic = rec.get("semantic", {})
        status = semantic.get("status", "UNVERIFIED")
        if status not in SEMANTIC_STATUSES:
            errors.append(f"{case_id}:{field}: unknown semantic status {status!r}")

        for prep in rec.get("evidence", {}).get("prep", []):
            p = root / prep.get("representation_path", "")
            if not p.exists():
                errors.append(f"{case_id}:{field}: missing source representation {p}")
                continue
            text = p.read_text(encoding="utf-8")
            actual_sha = sha256_text(text)
            if actual_sha != prep.get("representation_sha256"):
                errors.append(f"{case_id}:{field}: source-version drift for {prep.get('source_id')}")
            try:
                ex = excerpt(text, int(prep["line_start"]), int(prep["line_end"]))
            except (IndexError, KeyError, ValueError) as exc:
                errors.append(f"{case_id}:{field}: impossible locator: {exc}")
                continue
            if "sha256:" + sha256_text(ex) != prep.get("excerpt_digest"):
                errors.append(f"{case_id}:{field}: source/excerpt mismatch at L{prep.get('line_start')}-L{prep.get('line_end')}")

        for live in rec.get("evidence", {}).get("live", []):
            mid = str(live.get("message_id", ""))
            item = discord.get(mid)
            if not item:
                errors.append(f"{case_id}:{field}: Discord lookup failure for {mid}")
                continue
            if db_sha is None:
                errors.append(f"{case_id}:{field}: canonical Discord LFS identity unavailable")
            elif db_sha != live.get("canonical_database_sha256"):
                errors.append(f"{case_id}:{field}: canonical Discord source-version drift for {mid}")
            if item["row_digest"] != live.get("projection_row_digest"):
                errors.append(f"{case_id}:{field}: Discord message-version drift for {mid}")
            expected_author = live.get("expected_author_id")
            if expected_author and str(item["row"].get("author_id")) != str(expected_author):
                errors.append(f"{case_id}:{field}: immutable-author mismatch for {mid}")

        for dep in rec.get("dependencies", []):
            if dep.get("type") == "IDENTITY_ASSERTION":
                if not ident:
                    errors.append(f"{case_id}:{field}: missing identity dependency {dep.get('id')}")
                elif dep.get("id") != BRENDON_S3_IDENTITY or dep.get("digest") != ident_digest:
                    errors.append(f"{case_id}:{field}: identity dependency changed or unresolved")
            elif dep.get("type") == "AUDITED_PROPOSITION":
                dep_id = dep.get("id")
                if dep_id not in {r.get("audit_id") for r in records}:
                    errors.append(f"{case_id}:{field}: missing derived dependency {dep_id}")

        flags = set(rec.get("review_flags", []))
        if "DERIVED_ONLY_SUPPORT" in flags and status in VERIFIED_STATUSES:
            errors.append(f"{case_id}:{field}: derived-only evidence chain cannot be verified as primary support")
        if "NEGATIVE_OR_ABSENCE_CLAIM" in flags and status in VERIFIED_STATUSES:
            coverage = rec.get("negative_coverage") or {}
            if not coverage.get("complete"):
                errors.append(f"{case_id}:{field}: negative claim has insufficient searched coverage")

        locator = rec.get("forensics", {}).get("locator_classification")
        if locator is not None and locator not in LOCATOR_OUTCOMES:
            errors.append(f"{case_id}:{field}: unknown locator-forensics outcome {locator}")

        current_state = evidence_state_digest(rec)
        if current_state != rec.get("prepared_state_sha256"):
            errors.append(f"{case_id}:{field}: prepared state digest is stale")
        review_state = semantic.get("review_packet_state_sha256")
        if status in VERIFIED_STATUSES and not review_state:
            errors.append(f"{case_id}:{field}: verified status lacks version-bound review packet state")

    # Known regression must remain fail-closed until semantic adjudication.
    for field in PROPOSITION_FIELDS:
        rec = by_key.get(("BDC-S3-004", field))
        if not rec:
            continue
        forensic = rec.get("forensics", {})
        if forensic.get("original_representation") != "ORIGINAL_REPRESENTATION_UNAVAILABLE":
            errors.append(f"BDC-S3-004:{field}: original representation must not be invented")
        if forensic.get("current_support") != "SUPPORT_NOT_FOUND":
            errors.append(f"BDC-S3-004:{field}: known current locator failure was lost")
        if forensic.get("representation_drift_established") is not False:
            errors.append(f"BDC-S3-004:{field}: representation drift must remain unestablished")

    meta = packet_meta(packet_path)
    if meta is None:
        errors.append(f"missing or malformed review packet metadata: {packet_path}")
    elif records:
        current_global = global_packet_state(records)
        if meta.get("packet_state_sha256") != current_global:
            errors.append("stale review packet: packet state does not match audit ledger")
        for rec in records:
            semantic = rec.get("semantic", {})
            if semantic.get("status") in VERIFIED_STATUSES:
                if semantic.get("review_packet_state_sha256") != current_global:
                    errors.append(f"{rec['audit_id']}: stale verdict integration")

    # Cheap source-level sanity check used to make drift diagnostics clearer.
    if source_text is not None and source_sha:
        for rec in records[:1]:
            for prep in rec.get("evidence", {}).get("prep", []):
                if prep.get("source_id") == "BCS-000045" and prep.get("representation_sha256") != source_sha:
                    warnings.append("BCS-000045 current source digest differs from staged evidence state")

    return ValidationResult(errors, warnings)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--ledger", default=None)
    ap.add_argument("--packet", default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    ledger = Path(args.ledger).resolve() if args.ledger else None
    packet = Path(args.packet).resolve() if args.packet else None
    result = validate_repo(root, ledger, packet)
    payload = {"ok": result.ok, "errors": result.errors, "warnings": result.warnings}
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        for warning in result.warnings:
            print(f"WARNING: {warning}")
        for error in result.errors:
            print(f"ERROR: {error}")
        print(f"research evidence integrity: {'PASS' if result.ok else 'FAIL'}")
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
