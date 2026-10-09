#!/usr/bin/env python3
"""Build compact first-tranche audit state and a bounded UTF-8 review packet."""
from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import validate_research_evidence as vre

OUTPUT_PACKET = Path("research/integrity/generated/roanoke-s3-decision-cases-v1.review.md")

DERIVED_LINEAGE = {
    "original_pr": 2,
    "markdown_first_seen_commit": "22c1b645db850fc4934680c569ba6adc9b1b0bb8",
    "jsonl_first_seen_commit": "af160d7d93d8e632fbcff2a22adfe92f7314d3f8",
    "current_canonical_path_introduced_commit": "35b23ce73ba46f7937d3695f2a67f10a57eda033",
}
SOURCE_LINEAGE = {
    "source_id": "BCS-000045",
    "current_canonical_path_introduced_commit": "bdfbbf1a34e142b63b7e752033c67d5b7176c9b2",
    "legacy_staging_normalized_sha256": "adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166",
    "legacy_staging_original_sha256": "9ba280ea54b9c13312db5ced664f3bcff48b3c3b8640568fec2f42ea7bf4edcb",
    "citation_creation_representation_preserved_in_pr2": False,
}
BDC004_NOTES = [
    "The disputed locators were present in the first v1 Markdown commit.",
    "PR #2 preserved no BCS-000045 source representation at its base, first commit, or final head.",
    "The later preserved normalized and export representations resolve the cited coordinates to unrelated material.",
    "Searches of both preserved representations found no relevant limb-loss/handwave prep passage.",
    "Representation drift is possible in the abstract but is not established by preserved evidence.",
]


def git_dependency_commit(root: Path) -> str:
    paths = [
        str(vre.TRANCHE_MD), str(vre.TRANCHE_JSONL), str(vre.BCS45),
        str(vre.BCS45_META), str(vre.DISCORD_DB),
        str(vre.DISCORD_PROJECTION / "manifest.json"), str(vre.IDENTITIES),
    ]
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", *paths],
            cwd=root, text=True,
        ).strip()
    except Exception:
        return "UNKNOWN"


def source_quality(meta: dict[str, Any]) -> dict[str, Any]:
    cap = meta.get("capture_status", {})
    norm = meta.get("normalization", {})
    history = meta.get("historical_context", {})
    return {
        "source_kind": meta.get("source_kind"),
        "authorship": meta.get("authorship"),
        "capture_status": {
            "current_body": cap.get("current_body"),
            "comments": cap.get("comments"),
            "revision_metadata": cap.get("revision_metadata"),
            "revision_bodies": cap.get("revision_bodies"),
            "assets": cap.get("assets"),
        },
        "normalization_method": norm.get("method"),
        "normalization_warnings": norm.get("warnings", []),
        "production_stages": history.get("production_stages", []),
        "not_established": history.get("not_established", []),
        "reconciliation": meta.get("reconciliation"),
    }


def load_snapshot(root: Path) -> dict[str, Any]:
    md = vre.parse_cases_markdown(root / vre.TRANCHE_MD)
    js = vre.parse_cases_jsonl(root / vre.TRANCHE_JSONL)
    divergence = vre.compare_markdown_json(md, js)
    if divergence:
        raise SystemExit("Cannot stage divergent Markdown/JSON:\n" + "\n".join(divergence))

    source_bytes = (root / vre.BCS45).read_bytes()
    source_text = source_bytes.decode("utf-8")
    meta_bytes = (root / vre.BCS45_META).read_bytes()
    meta = json.loads(meta_bytes.decode("utf-8"))
    db_sha = vre.lfs_oid(root / vre.DISCORD_DB)
    if not db_sha:
        raise SystemExit("Canonical S3 Discord LFS pointer is unavailable")

    ident = vre.identity_row(root)
    if not ident:
        raise SystemExit("Confirmed S3 Brendon identity mapping is unavailable")
    ident_digest = vre.canonical_json_digest(ident)

    live_ids = sorted({
        mid for case in js.values()
        for mid in vre.parse_live_ids(case.get("live_evidence", ""))
    })
    messages = vre.find_discord_messages(root, live_ids)
    missing = sorted(set(live_ids) - set(messages))
    if missing:
        raise SystemExit("Missing cited Discord messages: " + ", ".join(missing))

    return {
        "md": md,
        "js": js,
        "source_text": source_text,
        "source_sha256": vre.sha256_bytes(source_bytes),
        "source_meta_sha256": vre.sha256_bytes(meta_bytes),
        "source_quality": source_quality(meta),
        "db_sha256": db_sha,
        "identity": ident,
        "identity_digest": ident_digest,
        "messages": messages,
        "dependency_commit": git_dependency_commit(root),
    }


def review_flags(case_id: str, text: str) -> list[str]:
    flags = set(vre.infer_flags(text))
    if case_id == "BDC-S3-004":
        flags.add("KNOWN_LOCATOR_FAILURE")
    return sorted(flags)


def make_locator_results(case_id: str, prep: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results = []
    for loc in prep:
        ref = f"{loc['source_id']}:L{loc['line_start']}-L{loc['line_end']}"
        if case_id == "BDC-S3-004":
            results.append({
                "ref": ref,
                "classification": "ORIGINAL_REPRESENTATION_UNAVAILABLE",
                "current_support": "SUPPORT_NOT_FOUND",
                "representation_drift_established": False,
            })
        else:
            results.append({
                "ref": ref,
                "classification": "UNRESOLVED",
                "current_support": "UNRESOLVED",
                "representation_drift_established": False,
            })
    return results


def representative_message(case: dict[str, Any], snap: dict[str, Any]) -> str | None:
    target = vre.normalize_text(case.get("representative_line", "")).strip('"')
    if not target:
        return None
    for mid in vre.parse_live_ids(case.get("live_evidence", "")):
        content = vre.normalize_text(str(snap["messages"][mid]["row"].get("content", "")))
        if target == content or target in content or content in target:
            return mid
    return None


def make_unit(root: Path, snap: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    prep_refs = vre.parse_prep_refs(case.get("prep_evidence", ""))
    source_ids = list(dict.fromkeys(x["source_id"] for x in prep_refs))
    sources: list[dict[str, Any]] = []
    for source_id in source_ids:
        if source_id != "BCS-000045":
            sources.append({
                "source_id": source_id,
                "representation_path": None,
                "representation_sha256": None,
                "source_metadata_path": None,
                "source_metadata_sha256": None,
                "source_quality": {"status": "SOURCE_UNAVAILABLE"},
            })
        else:
            sources.append({
                "source_id": source_id,
                "representation_path": vre.BCS45.as_posix(),
                "representation_sha256": snap["source_sha256"],
                "source_metadata_path": vre.BCS45_META.as_posix(),
                "source_metadata_sha256": snap["source_meta_sha256"],
                "source_quality": snap["source_quality"],
                "representation_lineage": SOURCE_LINEAGE,
            })

    prep_locators = []
    for loc in prep_refs:
        ex = vre.excerpt(snap["source_text"], loc["line_start"], loc["line_end"]) if loc["source_id"] == "BCS-000045" else None
        prep_locators.append({
            **loc,
            "excerpt_digest": "sha256:" + vre.sha256_text(ex) if ex is not None else None,
        })

    live = []
    for mid in vre.parse_live_ids(case.get("live_evidence", "")):
        item = snap["messages"][mid]
        row = item["row"]
        author_id = str(row.get("author_id")) if row.get("author_id") is not None else None
        live.append({
            "message_id": mid,
            "canonical_database_path": vre.DISCORD_DB.as_posix(),
            "canonical_database_sha256": snap["db_sha256"],
            "projection_path": item["shard_path"],
            "projection_line": item["line"],
            "projection_row_digest": item["row_digest"],
            "author_id": author_id,
            "attribution_person_id": "person:brendon-faulkner" if author_id == vre.BRENDON_DISCORD_ID else None,
            "created_at": row.get("created_at"),
            "channel_id": row.get("channel_id"),
            "channel": row.get("channel"),
            "category": row.get("category"),
        })

    props = []
    for field in vre.PROPOSITION_FIELDS:
        text = case.get(field, "")
        flags = review_flags(case["id"], text)
        props.append({
            "field": field,
            "audit_id": f"audit:{case['id']}:{field}",
            "text": text,
            "normalized_text": vre.normalize_text(text),
            "digest": vre.proposition_digest(text),
            "review_flags": flags,
            "negative_coverage": {
                "complete": False,
                "surface": "Only cited evidence is staged; no corpus-wide absence search is implied.",
            } if "NEGATIVE_OR_ABSENCE_CLAIM" in flags else None,
            "dependencies": [],
            "semantic": {
                "status": vre.default_semantic_status(),
                "evidence_confidence": None,
                "claim_scope": None,
                "review_packet_state_sha256": None,
                "reviewed_at_commit": None,
                "reviewer": None,
            },
        })

    record = {
        "schema": "bfdm_integrity_audit/v1",
        "audit_id": f"audit:{case['id']}",
        "artifact": {
            "markdown_path": vre.TRANCHE_MD.as_posix(),
            "jsonl_path": vre.TRANCHE_JSONL.as_posix(),
            "unit_kind": "derived_case",
            "unit_id": case["id"],
            "locator": {"case_id": case["id"]},
            "case_serialization_digest": vre.case_serialization_digest(case),
            "staged_at_dependency_commit": snap["dependency_commit"],
        },
        "derived_lineage": DERIVED_LINEAGE,
        "legacy_claimed_confidence": case.get("confidence"),
        "propositions": props,
        "evidence": {
            "sources": sources,
            "prep_locators": prep_locators,
            "live": live,
        },
        "dependencies": [{
            "type": "IDENTITY_ASSERTION",
            "id": vre.BRENDON_S3_IDENTITY,
            "digest": snap["identity_digest"],
        }],
        "forensics": {
            "locator_results": make_locator_results(case["id"], prep_refs),
            "representative_message_id": representative_message(case, snap),
            "bounded_search_notes": BDC004_NOTES if case["id"] == "BDC-S3-004" else [],
        },
    }
    record["prepared_state_sha256"] = vre.record_state_digest(record)
    return record


def old_semantics(rows: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    semantics: dict[str, dict[str, Any]] = {}
    shared: dict[str, str] = {}
    for row in rows:
        if row.get("artifact", {}).get("field"):
            semantic = row.get("semantic", {})
            if semantic.get("status") not in (None, "UNVERIFIED"):
                raise SystemExit("Refusing automatic compaction of semantically reviewed legacy ledger")
            semantics[row.get("audit_id")] = copy.deepcopy(semantic)
            continue
        shared[row.get("audit_id")] = vre.evidence_dependency_digest(row)
        for prop in row.get("propositions", []):
            semantics[prop.get("audit_id")] = copy.deepcopy(prop.get("semantic", {}))
    return semantics, shared


def build_records(root: Path, previous_rows: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    snap = load_snapshot(root)
    previous_rows = previous_rows or []
    semantics, shared = old_semantics(previous_rows)
    old_units = {
        row.get("audit_id"): row for row in previous_rows
        if not row.get("artifact", {}).get("field")
    }
    records = []

    for case in snap["js"].values():
        fresh = make_unit(root, snap, case)
        old_unit = old_units.get(fresh["audit_id"])
        fresh_shared = vre.evidence_dependency_digest(fresh)
        old_shared = shared.get(fresh["audit_id"])

        for prop in fresh["propositions"]:
            old_semantic = semantics.get(prop["audit_id"])
            if not old_semantic:
                continue
            old_prop = None
            if old_unit:
                old_prop = next(
                    (p for p in old_unit.get("propositions", []) if p.get("audit_id") == prop["audit_id"]),
                    None,
                )
            if old_prop is not None and old_prop.get("digest") == prop.get("digest") and old_shared == fresh_shared:
                prop["semantic"] = old_semantic
            elif old_semantic.get("status") in vre.VERIFIED_STATUSES:
                prop["semantic"]["status"] = "REQUIRES_REVALIDATION"

        fresh["prepared_state_sha256"] = vre.record_state_digest(fresh)
        records.append(fresh)
    return records


def write_ledger(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in records) + "\n",
        encoding="utf-8",
    )


def same_channel_context(root: Path, item: dict[str, Any], radius: int = 2) -> list[dict[str, Any]]:
    path = Path(item["shard_path"])
    match = re.search(r"messages-(\d{4})\.jsonl$", path.name)
    shard_no = int(match.group(1)) if match else None
    candidates = []
    if shard_no is None:
        candidates = [root / path]
    else:
        for n in (shard_no - 1, shard_no, shard_no + 1):
            candidate = root / path.parent / f"messages-{n:04d}.jsonl"
            if candidate.exists():
                candidates.append(candidate)

    target = item["row"]
    rows = []
    for candidate in candidates:
        for line in candidate.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("channel_id") == target.get("channel_id"):
                rows.append(row)
    rows.sort(key=lambda row: (row.get("created_at", ""), str(row.get("id", ""))))
    idx = next((i for i, row in enumerate(rows) if str(row.get("id")) == str(target.get("id"))), None)
    return [target] if idx is None else rows[max(0, idx - radius): idx + radius + 1]


def one_line(value: Any) -> str:
    return str(value if value is not None else "").replace("\n", " ").strip()


def render_packet(root: Path, records: list[dict[str, Any]]) -> str:
    snap = load_snapshot(root)
    by_case = {record["artifact"]["unit_id"]: record for record in records}
    state = vre.global_packet_state(records)
    proposition_count = sum(len(r.get("propositions", [])) for r in records)

    body = [
        "# Roanoke S3 decision cases v1 — semantic review packet",
        "",
        "Generated view only. Historical truth remains in BCS/native sources; canonical audit state remains in research/integrity/audit_ledger.jsonl.",
        "",
        "Every proposition is UNVERIFIED unless its nested ledger verdict explicitly says otherwise. Mechanical reconstruction does not certify motive, causality, scope, transfer, or expert principle.",
        "",
        "## Tranche facts",
        "",
        f"- Cases: {len(records)}.",
        f"- Audit propositions: {proposition_count}.",
        "- Markdown/JSON relationship: exact synchronized equivalents at staging time; neither declares itself generated from the other.",
        f"- BCS-000045 normalized body SHA-256: {snap['source_sha256']}.",
        f"- Canonical S3 Discord database LFS SHA-256: {snap['db_sha256']}.",
        f"- Confirmed Brendon S3 Discord identity: {vre.BRENDON_S3_IDENTITY} / immutable user {vre.BRENDON_DISCORD_ID}.",
        "",
        "### BDC-S3-004 forensic boundary",
        "",
        "The disputed prep locators were already present in the first v1 Markdown commit. PR #2 preserved no BCS-000045 representation. The later preserved normalized and export snapshots both resolve those coordinates to unrelated material and contain no relevant limb-loss/handwave prep passage. Both locators are ORIGINAL_REPRESENTATION_UNAVAILABLE; their current support result is SUPPORT_NOT_FOUND; representation drift is not established.",
        "",
    ]

    labels = [
        ("Situation", "situation"),
        ("What Brendon noticed", "noticed"),
        ("What mattered", "values"),
        ("Intervention", "intervention"),
        ("Observed result", "observed_result"),
        ("Reusable judgment", "reusable_judgment"),
    ]

    for case_id, case in snap["js"].items():
        record = by_case[case_id]
        prop_by_field = {p["field"]: p for p in record["propositions"]}
        body.extend(["---", "", f"## {case_id} — {case.get('title', '')}", "", f"Legacy confidence: {case.get('confidence')}", ""])

        for label, field in labels:
            prop = prop_by_field[field]
            body.extend([
                f"**{label}.** {case.get(field, '')}",
                f"- audit: {prop['audit_id']}",
                f"- proposition: {prop['digest']}",
                f"- semantic status: {prop['semantic']['status']}",
                f"- flags: {', '.join(prop.get('review_flags', [])) or 'none'}",
                "",
            ])

        body.append(f"**Claimed prep evidence.** {case.get('prep_evidence', '')}")
        source_by_id = {s["source_id"]: s for s in record["evidence"]["sources"]}
        for loc in record["evidence"]["prep_locators"]:
            body.extend(["", f"### Prep excerpt — {loc['source_id']}:L{loc['line_start']}-L{loc['line_end']}"])
            source = source_by_id.get(loc["source_id"])
            if not source or not source.get("representation_path"):
                body.append("- source representation unavailable in this staging pass.")
                continue
            ex = vre.excerpt(snap["source_text"], loc["line_start"], loc["line_end"])
            body.extend([
                f"- representation: {source['representation_path']}",
                f"- representation SHA-256: {source['representation_sha256']}",
                f"- source metadata SHA-256: {source['source_metadata_sha256']}",
                f"- excerpt digest: {loc['excerpt_digest']}",
                "- source quality: " + json.dumps(source["source_quality"], ensure_ascii=False, sort_keys=True),
                "",
                "~~~text",
                *ex.splitlines(),
                "~~~",
            ])

        body.extend(["", f"**Claimed live evidence.** {case.get('live_evidence', '')}"])
        for live in record["evidence"]["live"]:
            mid = live["message_id"]
            item = snap["messages"][mid]
            row = item["row"]
            body.extend([
                "",
                f"### Discord evidence — {mid}",
                f"- canonical source: {vre.DISCORD_DB.as_posix()} @ LFS SHA-256 {snap['db_sha256']}",
                f"- retrieval projection: {item['shard_path']}:{item['line']} @ row {item['row_digest']}",
                f"- timestamp: {row.get('created_at')}",
                f"- channel: {row.get('category')} / {row.get('channel')} ({row.get('channel_id')})",
                f"- immutable author: {row.get('author_id')} — {row.get('display_name')} / {row.get('username')}",
                "",
                "Bounded same-channel context:",
                "",
                "~~~text",
            ])
            for ctx in same_channel_context(root, item):
                mark = ">>" if str(ctx.get("id")) == mid else "  "
                body.append(f"{mark} {ctx.get('created_at')} | {ctx.get('display_name')} [{ctx.get('author_id')}] | {one_line(ctx.get('content'))}")
            body.append("~~~")

        body.extend(["", f"**Representative line.** {case.get('representative_line', '')}", "", "### Mechanical warnings / lineage", ""])
        for result in record["forensics"]["locator_results"]:
            body.append(
                f"- {result['ref']}: {result['classification']}; current support {result['current_support']}; "
                f"representation drift established {str(result['representation_drift_established']).lower()}."
            )
        body.append(f"- representative-message match: {record['forensics'].get('representative_message_id')}")
        for note in record["forensics"].get("bounded_search_notes", []):
            body.append(f"- {note}")

        body.extend([
            "",
            "### Semantic review questions",
            "",
            "1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?",
            "2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?",
            "3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?",
            "4. What evidence confidence survives?",
            "5. What claim scope survives? One event does not become general-current-practice by default.",
            "6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?",
        ])

    payload = "\n".join(body).rstrip() + "\n"
    meta = {
        "schema": "bfdm_integrity_review_packet/v1",
        "tranche": vre.TRANCHE_JSONL.as_posix(),
        "dependency_commit": snap["dependency_commit"],
        "packet_state_sha256": state,
        "packet_payload_sha256": "sha256:" + vre.sha256_text(payload),
        "unit_count": len(records),
        "proposition_count": proposition_count,
        "evidence_dependency_summary": {
            "bcs_000045_sha256": snap["source_sha256"],
            "bcs_000045_metadata_sha256": snap["source_meta_sha256"],
            "discord_s3_database_sha256": snap["db_sha256"],
            "identity_assertion_digest": snap["identity_digest"],
        },
    }
    return "<!-- BFDM_INTEGRITY_PACKET_META\n" + json.dumps(meta, ensure_ascii=False, sort_keys=True) + "\n-->\n\n" + payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--bootstrap-ledger", action="store_true")
    group.add_argument("--refresh-ledger", action="store_true")
    parser.add_argument("--output", default=str(OUTPUT_PACKET))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    ledger_path = root / vre.LEDGER
    previous_rows = vre.read_jsonl(ledger_path) if ledger_path.exists() else []

    if args.bootstrap_ledger:
        if previous_rows:
            raise SystemExit("Refusing to bootstrap over an existing audit ledger; use --refresh-ledger")
        records = build_records(root)
        write_ledger(ledger_path, records)
    elif args.refresh_ledger:
        records = build_records(root, previous_rows)
        write_ledger(ledger_path, records)
    else:
        records = previous_rows
        if not records:
            raise SystemExit("Audit ledger is missing. Bootstrap it deliberately before packet generation.")

    output = root / args.output
    rendered = render_packet(root, records)
    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != rendered:
            print(f"stale packet: regenerate {output.relative_to(root)}")
            return 1
        print("review packet: PASS")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    print(f"wrote {output.relative_to(root)}")
    print(f"packet state {vre.global_packet_state(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
