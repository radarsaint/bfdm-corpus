#!/usr/bin/env python3
"""Deterministic integrity checks for version-bound BFDM derived research.

Mechanical reconstructability only. This module never decides whether historical
evidence semantically supports motive, causality, scope, transfer, or expert judgment.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
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
VERIFIED_STATUSES = {
    "VERIFIED_DIRECT",
    "VERIFIED_STRONG_RECONSTRUCTION",
    "PARTIALLY_SUPPORTED",
    "LOCATOR_BROKEN_SUPPORT_RECOVERED",
}
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
    rows: list[dict[str, Any]] = []
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
    return {row["id"]: row for row in read_jsonl(path)}


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
            hit = re.search(r"^\*\*" + re.escape(label) + r"\.\*\*\s*(.*?)$", body, re.M)
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
    match = re.search(r"^oid sha256:([0-9a-f]{64})$", text, re.M)
    return match.group(1) if match else None


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
    for shard in sorted((root / DISCORD_PROJECTION).glob("messages-*.jsonl")):
        shard_digest: str | None = None
        for line_no, line in enumerate(shard.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                # Unrelated malformed rows do not make a cited row disappear.
                # A malformed cited row remains missing and therefore fails closed.
                continue
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
    """Classify exact-text locator history without making a semantic judgment."""
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


def case_serialization_digest(case: dict[str, Any]) -> str:
    return canonical_json_digest(case)


def evidence_dependency_digest(record: dict[str, Any]) -> str:
    return canonical_json_digest({
        "legacy_claimed_confidence": record.get("legacy_claimed_confidence"),
        "evidence": record.get("evidence", {}),
        "dependencies": record.get("dependencies", []),
        "forensics": record.get("forensics", {}),
    })


def record_state_digest(record: dict[str, Any]) -> str:
    return canonical_json_digest({
        "case_serialization_digest": record.get("artifact", {}).get("case_serialization_digest"),
        "propositions": [
            {"field": p.get("field"), "digest": p.get("digest")}
            for p in record.get("propositions", [])
        ],
        "evidence_dependency_digest": evidence_dependency_digest(record),
    })


def global_packet_state(records: Iterable[dict[str, Any]], actual_states: dict[str, str] | None = None) -> str:
    rows = []
    for record in records:
        aid = record["audit_id"]
        state = actual_states.get(aid) if actual_states else record.get("prepared_state_sha256")
        rows.append((aid, state))
    return canonical_json_digest(sorted(rows))


def packet_meta(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    match = PACKET_META_RE.search(path.read_text(encoding="utf-8"))
    return json.loads(match.group(1)) if match else None


def _currentize_record(
    root: Path,
    record: dict[str, Any],
    case: dict[str, Any],
    discord: dict[str, dict[str, Any]],
    db_sha: str | None,
    ident_digest: str | None,
) -> dict[str, Any]:
    current = copy.deepcopy(record)
    current["artifact"]["case_serialization_digest"] = case_serialization_digest(case)
    by_field = {p["field"]: p for p in current.get("propositions", [])}
    for field in PROPOSITION_FIELDS:
        if field in by_field:
            by_field[field]["digest"] = proposition_digest(case.get(field, ""))

    for source in current.get("evidence", {}).get("sources", []):
        body_path = root / source.get("representation_path", "")
        meta_path = root / source.get("source_metadata_path", "")
        source["representation_sha256"] = sha256_bytes(body_path.read_bytes()) if body_path.exists() else None
        source["source_metadata_sha256"] = sha256_bytes(meta_path.read_bytes()) if meta_path.exists() else None

    source_text_cache: dict[str, str] = {}
    for locator in current.get("evidence", {}).get("prep_locators", []):
        source = next(
            (s for s in current.get("evidence", {}).get("sources", []) if s.get("source_id") == locator.get("source_id")),
            None,
        )
        if not source or not source.get("representation_path"):
            locator["excerpt_digest"] = None
            continue
        path = source["representation_path"]
        if path not in source_text_cache:
            p = root / path
            source_text_cache[path] = p.read_text(encoding="utf-8") if p.exists() else ""
        try:
            ex = excerpt(source_text_cache[path], int(locator["line_start"]), int(locator["line_end"]))
            locator["excerpt_digest"] = "sha256:" + sha256_text(ex)
        except (IndexError, KeyError, ValueError):
            locator["excerpt_digest"] = None

    for live in current.get("evidence", {}).get("live", []):
        mid = str(live.get("message_id", ""))
        item = discord.get(mid)
        live["canonical_database_sha256"] = db_sha
        live["projection_row_digest"] = item["row_digest"] if item else None
        live["author_id"] = str(item["row"].get("author_id")) if item else None

    for dep in current.get("dependencies", []):
        if dep.get("type") == "IDENTITY_ASSERTION" and dep.get("id") == BRENDON_S3_IDENTITY:
            dep["digest"] = ident_digest
    return current


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
    by_unit = {r.get("artifact", {}).get("unit_id"): r for r in records}
    if len(by_unit) != len(records):
        errors.append("duplicate or missing unit_id in audit ledger")
    expected_units = set(js)
    for missing in sorted(expected_units - set(by_unit)):
        errors.append(f"{missing}: missing audit unit; new propositions default to UNVERIFIED")
    for extra in sorted(set(by_unit) - expected_units):
        errors.append(f"{extra}: audit unit has no current derived case")

    all_ids = {mid for case in js.values() for mid in parse_live_ids(case.get("live_evidence", ""))}
    discord = find_discord_messages(root, all_ids)
    db_sha = lfs_oid(root / DISCORD_DB)
    ident = identity_row(root)
    ident_digest = canonical_json_digest(ident) if ident else None
    actual_states: dict[str, str] = {}

    for case_id in sorted(expected_units & set(by_unit)):
        record = by_unit[case_id]
        case = js[case_id]
        if record.get("schema") != "bfdm_integrity_audit/v1":
            errors.append(f"{case_id}: unsupported audit schema {record.get('schema')!r}")
        if record.get("artifact", {}).get("unit_kind") != "derived_case":
            errors.append(f"{case_id}: S3 locator leaked into unit kind instead of generic derived_case")

        current_case_digest = case_serialization_digest(case)
        if record.get("artifact", {}).get("case_serialization_digest") != current_case_digest:
            errors.append(f"{case_id}: derived-unit serialization changed; refresh/revalidate")

        propositions = record.get("propositions", [])
        by_field = {p.get("field"): p for p in propositions}
        if len(by_field) != len(propositions):
            errors.append(f"{case_id}: duplicate proposition field in audit unit")
        for field in PROPOSITION_FIELDS:
            prop = by_field.get(field)
            if not prop:
                errors.append(f"{case_id}:{field}: missing proposition; defaults to UNVERIFIED")
                continue
            current_text = case.get(field, "")
            if normalize_text(str(prop.get("text", ""))) != normalize_text(str(current_text)):
                errors.append(f"{case_id}:{field}: stored proposition text differs from current artifact")
            if prop.get("digest") != proposition_digest(current_text):
                errors.append(f"{case_id}:{field}: claim-version drift; REQUIRES_REVALIDATION")
            semantic = prop.get("semantic", {})
            status = semantic.get("status", "UNVERIFIED")
            if status not in SEMANTIC_STATUSES:
                errors.append(f"{case_id}:{field}: unknown semantic status {status!r}")
            flags = set(prop.get("review_flags", []))
            if "DERIVED_ONLY_SUPPORT" in flags and status in VERIFIED_STATUSES:
                errors.append(f"{case_id}:{field}: derived-only evidence chain cannot be verified as primary support")
            if "NEGATIVE_OR_ABSENCE_CLAIM" in flags and status in VERIFIED_STATUSES:
                coverage = prop.get("negative_coverage") or {}
                if not coverage.get("complete"):
                    errors.append(f"{case_id}:{field}: negative claim has insufficient searched coverage")

        expected_prep = [
            (x["source_id"], x["line_start"], x["line_end"])
            for x in parse_prep_refs(case.get("prep_evidence", ""))
        ]
        stored_prep = [
            (x.get("source_id"), x.get("line_start"), x.get("line_end"))
            for x in record.get("evidence", {}).get("prep_locators", [])
        ]
        if expected_prep != stored_prep:
            errors.append(f"{case_id}: prep citation set changed")

        source_by_id = {s.get("source_id"): s for s in record.get("evidence", {}).get("sources", [])}
        for source_id, start, end in stored_prep:
            source = source_by_id.get(source_id)
            if not source:
                errors.append(f"{case_id}: missing source identity {source_id}")
                continue
            body_path = root / source.get("representation_path", "")
            meta_path = root / source.get("source_metadata_path", "")
            if not body_path.exists():
                errors.append(f"{case_id}: missing source representation {body_path}")
                continue
            if sha256_bytes(body_path.read_bytes()) != source.get("representation_sha256"):
                errors.append(f"{case_id}: source-version drift for {source_id}; REQUIRES_REVALIDATION")
            if not meta_path.exists():
                errors.append(f"{case_id}: missing source metadata {meta_path}")
            elif sha256_bytes(meta_path.read_bytes()) != source.get("source_metadata_sha256"):
                errors.append(f"{case_id}: source-quality metadata changed; REQUIRES_REVALIDATION")
            loc = next(
                (x for x in record["evidence"]["prep_locators"]
                 if x.get("source_id") == source_id and x.get("line_start") == start and x.get("line_end") == end),
                None,
            )
            try:
                ex = excerpt(body_path.read_text(encoding="utf-8"), int(start), int(end))
            except (IndexError, ValueError) as exc:
                errors.append(f"{case_id}: impossible locator {source_id}:L{start}-L{end}: {exc}")
                continue
            if not loc or loc.get("excerpt_digest") != "sha256:" + sha256_text(ex):
                errors.append(f"{case_id}: source/excerpt mismatch at {source_id}:L{start}-L{end}")

        expected_live = parse_live_ids(case.get("live_evidence", ""))
        stored_live = [str(x.get("message_id")) for x in record.get("evidence", {}).get("live", [])]
        if expected_live != stored_live:
            errors.append(f"{case_id}: live citation set changed")
        for live in record.get("evidence", {}).get("live", []):
            mid = str(live.get("message_id", ""))
            item = discord.get(mid)
            if not item:
                errors.append(f"{case_id}: Discord lookup failure for {mid}")
                continue
            if db_sha is None:
                errors.append(f"{case_id}: canonical Discord LFS identity unavailable")
            elif db_sha != live.get("canonical_database_sha256"):
                errors.append(f"{case_id}: canonical Discord source-version drift for {mid}")
            if item["row_digest"] != live.get("projection_row_digest"):
                errors.append(f"{case_id}: Discord message-version drift for {mid}")
            actual_author = str(item["row"].get("author_id"))
            if actual_author != str(live.get("author_id")):
                errors.append(f"{case_id}: immutable-author mismatch for {mid}")
            if live.get("attribution_person_id") == "person:brendon-faulkner" and actual_author != BRENDON_DISCORD_ID:
                errors.append(f"{case_id}: asserted Brendon attribution has wrong immutable author for {mid}")

        for dep in record.get("dependencies", []):
            if dep.get("type") == "IDENTITY_ASSERTION":
                if not ident:
                    errors.append(f"{case_id}: missing identity dependency {dep.get('id')}")
                elif dep.get("id") != BRENDON_S3_IDENTITY or dep.get("digest") != ident_digest:
                    errors.append(f"{case_id}: identity dependency changed or unresolved")
            elif dep.get("type") == "AUDITED_PROPOSITION":
                target = dep.get("id")
                all_prop_ids = {
                    p.get("audit_id")
                    for r in records
                    for p in r.get("propositions", [])
                }
                if target not in all_prop_ids:
                    errors.append(f"{case_id}: missing derived dependency {target}")

        for locator in record.get("forensics", {}).get("locator_results", []):
            if locator.get("classification") not in LOCATOR_OUTCOMES:
                errors.append(f"{case_id}: unknown locator-forensics outcome {locator.get('classification')}")

        if case_id == "BDC-S3-004":
            results = record.get("forensics", {}).get("locator_results", [])
            if len(results) != 2:
                errors.append("BDC-S3-004: expected two disputed prep locator results")
            for loc in results:
                if loc.get("classification") != "ORIGINAL_REPRESENTATION_UNAVAILABLE":
                    errors.append("BDC-S3-004: original representation must not be invented")
                if loc.get("current_support") != "SUPPORT_NOT_FOUND":
                    errors.append("BDC-S3-004: known current locator failure was lost")
                if loc.get("representation_drift_established") is not False:
                    errors.append("BDC-S3-004: representation drift must remain unestablished")

        currentized = _currentize_record(root, record, case, discord, db_sha, ident_digest)
        state = record_state_digest(currentized)
        actual_states[record["audit_id"]] = state
        if state != record.get("prepared_state_sha256"):
            errors.append(f"{case_id}: prepared state is stale; REQUIRES_REVALIDATION")

    meta = packet_meta(packet_path)
    if meta is None:
        errors.append(f"missing or malformed review packet metadata: {packet_path}")
    elif records:
        current_global = global_packet_state(records, actual_states)
        if meta.get("packet_state_sha256") != current_global:
            errors.append("stale review packet: proposition/evidence dependency state changed")
        for record in records:
            for prop in record.get("propositions", []):
                semantic = prop.get("semantic", {})
                if semantic.get("status") in VERIFIED_STATUSES:
                    if semantic.get("review_packet_state_sha256") != current_global:
                        errors.append(f"{prop.get('audit_id')}: stale verdict integration")

    return ValidationResult(errors, warnings)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--ledger")
    parser.add_argument("--packet")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    result = validate_repo(
        root,
        Path(args.ledger).resolve() if args.ledger else None,
        Path(args.packet).resolve() if args.packet else None,
    )
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
