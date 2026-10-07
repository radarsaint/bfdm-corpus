#!/usr/bin/env python3
"""Build the first-tranche audit ledger and bounded semantic-review packet."""
from __future__ import annotations

import argparse
import copy
import hashlib
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
BDC004_FORENSICS = {
    "locator_classification": "ORIGINAL_REPRESENTATION_UNAVAILABLE",
    "original_representation": "ORIGINAL_REPRESENTATION_UNAVAILABLE",
    "current_support": "SUPPORT_NOT_FOUND",
    "representation_drift_established": False,
    "bounded_search": [
        "PR #2 base/head and commits",
        "current Git path history",
        "legacy staging manifest",
        "ingest/drive-project-v3 donor",
        "current normalized source and preserved export snapshot",
    ],
    "notes": [
        "The disputed locators were present in the first Markdown commit.",
        "PR #2 preserved no BCS-000045 source representation.",
        "The later preserved normalized/export representations do not contain limb-loss or handwave prep evidence at the cited coordinates.",
        "Do not infer representation drift without the missing citation-time representation.",
    ],
}


def git_state_commit(root: Path) -> str:
    deps = [
        str(vre.TRANCHE_MD),
        str(vre.TRANCHE_JSONL),
        str(vre.LEDGER),
        str(vre.BCS45),
        str(vre.BCS45_META),
        str(vre.DISCORD_DB),
        str(vre.DISCORD_PROJECTION / "manifest.json"),
        str(vre.IDENTITIES),
    ]
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", *deps],
            cwd=root,
            text=True,
        ).strip()
    except Exception:
        return "UNKNOWN"


def source_quality(root: Path) -> dict[str, Any]:
    meta = json.loads((root / vre.BCS45_META).read_text(encoding="utf-8"))
    cap = meta.get("capture_status", {})
    prov = meta.get("provenance", {})
    rel = meta.get("relationships", {})
    return {
        "status": "RECONCILED_CONTAINER",
        "body": cap.get("current_body"),
        "comments": cap.get("comments"),
        "revision_metadata": cap.get("revision_metadata"),
        "revisions": cap.get("revisions"),
        "normalization_method": prov.get("normalization_method"),
        "extraction_warning": prov.get("extraction_warning"),
        "historical_context": rel.get("historical_context"),
        "live_use": rel.get("live_use"),
    }


def case_flags(field: str, text: str, case_id: str, prep_refs: list[dict[str, Any]]) -> list[str]:
    flags = set(vre.infer_flags(text))
    if case_id == "BDC-S3-004":
        flags.update({"KNOWN_LOCATOR_FAILURE", "SOURCE_UNAVAILABLE"})
    if not prep_refs:
        flags.add("NO_PREP_PRIMARY_LINK")
    if field == "reusable_judgment":
        flags.add("GENERALIZATION_REVIEW")
    return sorted(flags)


def load_snapshot(root: Path) -> dict[str, Any]:
    md = vre.parse_cases_markdown(root / vre.TRANCHE_MD)
    js = vre.parse_cases_jsonl(root / vre.TRANCHE_JSONL)
    divergence = vre.compare_markdown_json(md, js)
    if divergence:
        raise SystemExit("Cannot stage divergent Markdown/JSON:\n" + "\n".join(divergence))

    source_text = (root / vre.BCS45).read_text(encoding="utf-8")
    source_sha = vre.sha256_text(source_text)
    db_sha = vre.lfs_oid(root / vre.DISCORD_DB)
    if not db_sha:
        raise SystemExit("Canonical S3 Discord LFS pointer is unavailable")
    ident = vre.identity_row(root)
    if not ident:
        raise SystemExit("Confirmed S3 Brendon identity mapping is unavailable")
    ident_digest = vre.canonical_json_digest(ident)

    live_ids = sorted({mid for case in js.values() for mid in vre.parse_live_ids(case.get("live_evidence", ""))})
    messages = vre.find_discord_messages(root, live_ids)
    missing = sorted(set(live_ids) - set(messages))
    if missing:
        raise SystemExit("Missing cited Discord messages: " + ", ".join(missing))

    return {
        "md": md,
        "js": js,
        "source_text": source_text,
        "source_sha": source_sha,
        "db_sha": db_sha,
        "identity": ident,
        "identity_digest": ident_digest,
        "messages": messages,
        "source_quality": source_quality(root),
        "md_sha256": vre.sha256_bytes((root / vre.TRANCHE_MD).read_bytes()),
        "jsonl_sha256": vre.sha256_bytes((root / vre.TRANCHE_JSONL).read_bytes()),
    }


def make_record(root: Path, snap: dict[str, Any], case: dict[str, Any], field: str) -> dict[str, Any]:
    prep: list[dict[str, Any]] = []
    for ref in vre.parse_prep_refs(case.get("prep_evidence", "")):
        if ref["source_id"] != "BCS-000045":
            prep.append({
                **ref,
                "representation_path": None,
                "representation_sha256": None,
                "excerpt_digest": None,
                "locator_resolves": False,
            })
            continue
        ex = vre.excerpt(snap["source_text"], ref["line_start"], ref["line_end"])
        prep.append({
            **ref,
            "representation_path": vre.BCS45.as_posix(),
            "representation_sha256": snap["source_sha"],
            "line_count": len(snap["source_text"].splitlines()),
            "excerpt_digest": "sha256:" + vre.sha256_text(ex),
            "locator_resolves": True,
            "source_quality": snap["source_quality"],
        })

    live: list[dict[str, Any]] = []
    for mid in vre.parse_live_ids(case.get("live_evidence", "")):
        item = snap["messages"][mid]
        row = item["row"]
        live.append({
            "message_id": mid,
            "canonical_database_path": vre.DISCORD_DB.as_posix(),
            "canonical_database_sha256": snap["db_sha"],
            "projection_path": item["shard_path"],
            "projection_shard_sha256": item["shard_sha256"],
            "projection_line": item["line"],
            "projection_row_digest": item["row_digest"],
            "expected_author_id": str(row.get("author_id")) if row.get("author_id") is not None else None,
            "created_at": row.get("created_at"),
            "channel_id": row.get("channel_id"),
            "channel": row.get("channel"),
            "category": row.get("category"),
        })

    text = case.get(field, "")
    representative = vre.normalize_text(case.get("representative_line", "")).strip('"')
    rep_message = None
    if representative:
        for mid in vre.parse_live_ids(case.get("live_evidence", "")):
            row_text = vre.normalize_text(str(snap["messages"][mid]["row"].get("content", "")))
            if representative == row_text or representative in row_text or row_text in representative:
                rep_message = mid
                break

    forensics = {
        "locator_classification": "UNRESOLVED",
        "original_representation": "UNRESOLVED",
        "current_support": "UNRESOLVED",
        "representation_drift_established": False,
        "representative_message_id": rep_message,
    }
    if case["id"] == "BDC-S3-004":
        forensics.update(BDC004_FORENSICS)

    record: dict[str, Any] = {
        "schema": "bfdm_integrity_audit/v1",
        "audit_id": f"audit:{case['id']}:{field}",
        "artifact": {
            "markdown_path": vre.TRANCHE_MD.as_posix(),
            "jsonl_path": vre.TRANCHE_JSONL.as_posix(),
            "case_id": case["id"],
            "field": field,
            "markdown_sha256": snap["md_sha256"],
            "jsonl_sha256": snap["jsonl_sha256"],
            "staged_at_repository_state_commit": git_state_commit(root),
        },
        "derived_lineage": DERIVED_LINEAGE,
        "proposition": {
            "text": text,
            "normalized_text": vre.normalize_text(text),
            "digest": vre.proposition_digest(text),
        },
        "legacy_claimed_confidence": case.get("confidence"),
        "evidence": {
            "prep": prep,
            "live": live,
            "source_representation_lineage": SOURCE_LINEAGE,
        },
        "dependencies": [{
            "type": "IDENTITY_ASSERTION",
            "id": vre.BRENDON_S3_IDENTITY,
            "digest": snap["identity_digest"],
        }],
        "forensics": forensics,
        "review_flags": case_flags(field, text, case["id"], prep),
        "negative_coverage": {
            "complete": False,
            "surface": "Only the proposition's cited evidence is staged; no corpus-wide absence search is implied.",
        } if "NEGATIVE_OR_ABSENCE_CLAIM" in case_flags(field, text, case["id"], prep) else None,
        "semantic": {
            "status": vre.default_semantic_status(),
            "evidence_confidence": None,
            "claim_scope": None,
            "review_packet_state_sha256": None,
            "reviewed_at_commit": None,
            "reviewer": None,
        },
    }
    record["prepared_state_sha256"] = vre.evidence_state_digest(record)
    return record


def build_records(root: Path, previous: dict[str, dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    snap = load_snapshot(root)
    previous = previous or {}
    records: list[dict[str, Any]] = []
    for case_id, case in snap["js"].items():
        for field in vre.PROPOSITION_FIELDS:
            fresh = make_record(root, snap, case, field)
            old = previous.get(fresh["audit_id"])
            if old:
                unchanged = old.get("prepared_state_sha256") == fresh.get("prepared_state_sha256")
                if unchanged:
                    fresh["semantic"] = copy.deepcopy(old.get("semantic", fresh["semantic"]))
                else:
                    old_status = old.get("semantic", {}).get("status", "UNVERIFIED")
                    fresh["semantic"]["status"] = "REQUIRES_REVALIDATION" if old_status in vre.VERIFIED_STATUSES else "UNVERIFIED"
            records.append(fresh)
    return records


def write_ledger(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in records) + "\n"
    path.write_text(text, encoding="utf-8")


def load_context(root: Path, item: dict[str, Any], radius: int = 2) -> list[dict[str, Any]]:
    p = Path(item["shard_path"])
    m = re.search(r"messages-(\d{4})\.jsonl$", p.name)
    shard_no = int(m.group(1)) if m else None
    paths = []
    if shard_no is not None:
        for n in (shard_no - 1, shard_no, shard_no + 1):
            candidate = root / p.parent / f"messages-{n:04d}.jsonl"
            if candidate.exists():
                paths.append(candidate)
    else:
        paths.append(root / p)

    rows: list[dict[str, Any]] = []
    target = item["row"]
    for path in paths:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("channel_id") == target.get("channel_id"):
                rows.append(row)
    rows.sort(key=lambda r: (r.get("created_at", ""), str(r.get("id", ""))))
    idx = next((i for i, r in enumerate(rows) if str(r.get("id")) == str(target.get("id"))), None)
    if idx is None:
        return [target]
    return rows[max(0, idx - radius): idx + radius + 1]


def q(text: Any) -> str:
    value = str(text if text is not None else "")
    return value.replace("\n", " ").strip()


def render_packet(root: Path, records: list[dict[str, Any]]) -> str:
    snap = load_snapshot(root)
    by_case: dict[str, list[dict[str, Any]]] = {}
    for rec in records:
        by_case.setdefault(rec["artifact"]["case_id"], []).append(rec)
    state = vre.global_packet_state(records)

    body: list[str] = []
    body.append("# Roanoke S3 decision cases v1 — semantic review packet")
    body.append("")
    body.append("Generated view only. Historical truth remains in BCS/native sources; canonical audit state remains in `research/integrity/audit_ledger.jsonl`.")
    body.append("")
    body.append("Every proposition in this packet is **UNVERIFIED** unless its ledger record explicitly says otherwise. Mechanical reconstruction does not certify motive, causality, scope, or transfer.")
    body.append("")
    body.append("## Tranche facts")
    body.append("")
    body.append(f"- Cases: {len(snap['js'])}.")
    body.append(f"- Audit propositions: {len(records)}.")
    body.append(f"- Markdown/JSON relationship: synchronized equivalent representations; neither declares itself generated.")
    body.append(f"- BCS-000045 normalized source SHA-256: `{snap['source_sha']}`.")
    body.append(f"- Canonical S3 Discord database LFS SHA-256: `{snap['db_sha']}`.")
    body.append(f"- Confirmed Brendon S3 Discord identity: `{vre.BRENDON_S3_IDENTITY}` / immutable user `{vre.BRENDON_DISCORD_ID}`.")
    body.append("")
    body.append("### BDC-S3-004 forensic boundary")
    body.append("")
    body.append("The disputed prep citation was present in the first v1 Markdown commit (`22c1b645...`). PR #2 preserved no BCS-000045 body at its base or head. The later preserved Library/Drive normalized and export representations both resolve those coordinates to unrelated material and contain no relevant limb-loss/handwave prep passage. Classification: `ORIGINAL_REPRESENTATION_UNAVAILABLE`; current cited support: `SUPPORT_NOT_FOUND`; representation drift is **not established**.")
    body.append("")

    for case_id, case in snap["js"].items():
        body.append(f"---\n\n## {case_id} — {case.get('title','')}")
        body.append("")
        body.append(f"**Legacy confidence:** {case.get('confidence')}")
        body.append("")
        for label, key in [
            ("Situation", "situation"),
            ("What Brendon noticed", "noticed"),
            ("What mattered", "values"),
            ("Intervention", "intervention"),
            ("Observed result", "observed_result"),
            ("Reusable judgment", "reusable_judgment"),
        ]:
            rec = next(r for r in by_case[case_id] if r["artifact"]["field"] == key)
            body.append(f"**{label}.** {case.get(key,'')}")
            body.append(f"- audit: `{rec['audit_id']}`")
            body.append(f"- proposition: `{rec['proposition']['digest']}`")
            body.append(f"- semantic status: `{rec['semantic']['status']}`")
            body.append(f"- flags: {', '.join(rec.get('review_flags', [])) or 'none'}")
            body.append("")

        body.append(f"**Claimed prep evidence.** {case.get('prep_evidence','')}")
        prep_seen = set()
        exemplar = by_case[case_id][0]
        for ev in exemplar["evidence"]["prep"]:
            key = (ev.get("source_id"), ev.get("line_start"), ev.get("line_end"))
            if key in prep_seen:
                continue
            prep_seen.add(key)
            body.append("")
            body.append(f"### Prep excerpt — {ev.get('source_id')}:L{ev.get('line_start')}-L{ev.get('line_end')}")
            if ev.get("representation_path"):
                ex = vre.excerpt(snap["source_text"], int(ev["line_start"]), int(ev["line_end"]))
                body.append(f"- representation: `{ev['representation_path']}`")
                body.append(f"- representation SHA-256: `{ev['representation_sha256']}`")
                body.append(f"- excerpt digest: `{ev['excerpt_digest']}`")
                body.append("- source quality: " + json.dumps(ev.get("source_quality"), ensure_ascii=False, sort_keys=True))
                body.append("")
                body.append("~~~text")
                body.extend(ex.splitlines())
                body.append("~~~")
            else:
                body.append("- source representation unavailable in this staging pass.")

        body.append("")
        body.append(f"**Claimed live evidence.** {case.get('live_evidence','')}")
        for mid in vre.parse_live_ids(case.get("live_evidence", "")):
            item = snap["messages"][mid]
            row = item["row"]
            body.append("")
            body.append(f"### Discord evidence — {mid}")
            body.append(f"- canonical source: `{vre.DISCORD_DB.as_posix()}` @ LFS SHA-256 `{snap['db_sha']}`")
            body.append(f"- retrieval projection: `{item['shard_path']}:{item['line']}` @ row `{item['row_digest']}`")
            body.append(f"- timestamp: {row.get('created_at')}")
            body.append(f"- channel: {row.get('category')} / {row.get('channel')} (`{row.get('channel_id')}`)")
            body.append(f"- immutable author: `{row.get('author_id')}` — {row.get('display_name')} / {row.get('username')}")
            body.append("")
            body.append("Bounded same-channel context:")
            body.append("")
            body.append("~~~text")
            for ctx in load_context(root, item):
                mark = ">>" if str(ctx.get("id")) == mid else "  "
                body.append(f"{mark} {ctx.get('created_at')} | {ctx.get('display_name')} [{ctx.get('author_id')}] | {q(ctx.get('content'))}")
            body.append("~~~")

        body.append("")
        body.append(f"**Representative line.** {case.get('representative_line','')}")
        body.append("")
        forensic = exemplar.get("forensics", {})
        body.append("### Mechanical warnings / lineage")
        body.append("")
        body.append(f"- locator classification: `{forensic.get('locator_classification')}`")
        body.append(f"- original representation: `{forensic.get('original_representation')}`")
        body.append(f"- current support: `{forensic.get('current_support')}`")
        body.append(f"- representation drift established: `{str(forensic.get('representation_drift_established')).lower()}`")
        body.append(f"- representative-message match: `{forensic.get('representative_message_id')}`")
        if case_id == "BDC-S3-004":
            for note in forensic.get("notes", []):
                body.append(f"- {note}")
        body.append("")
        body.append("### Semantic review questions")
        body.append("")
        body.append("1. Which field-level propositions are directly supported, strongly reconstructed, only suggestive, contradicted, or unresolved by the staged evidence?")
        body.append("2. Does the case attribute Brendon's noticing/motive/choice more strongly than the primary evidence permits?")
        body.append("3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?")
        body.append("4. What evidence confidence survives?")
        body.append("5. What claim scope survives? Do not promote one event to a general-current-practice rule.")
        body.append("6. If the prep locator is broken, does the live evidence independently preserve some proposition, or must the claim be downgraded?")

    payload = "\n".join(body).rstrip() + "\n"
    meta = {
        "schema": "bfdm_integrity_review_packet/v1",
        "tranche": vre.TRANCHE_JSONL.as_posix(),
        "repository_state_commit": git_state_commit(root),
        "packet_state_sha256": state,
        "packet_payload_sha256": "sha256:" + vre.sha256_text(payload),
        "proposition_count": len(records),
        "evidence_dependency_summary": {
            "bcs_000045_sha256": snap["source_sha"],
            "discord_s3_database_sha256": snap["db_sha"],
            "identity_assertion_digest": snap["identity_digest"],
        },
    }
    return "<!-- BFDM_INTEGRITY_PACKET_META\n" + json.dumps(meta, ensure_ascii=False, sort_keys=True) + "\n-->\n\n" + payload


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--bootstrap-ledger", action="store_true")
    group.add_argument("--refresh-ledger", action="store_true")
    ap.add_argument("--output", default=str(OUTPUT_PACKET))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    ledger_path = root / vre.LEDGER
    previous: dict[str, dict[str, Any]] = {}

    if ledger_path.exists():
        previous = {r["audit_id"]: r for r in vre.read_jsonl(ledger_path)}

    if args.bootstrap_ledger:
        if ledger_path.exists() and previous:
            raise SystemExit("Refusing to bootstrap over an existing audit ledger; use --refresh-ledger")
        records = build_records(root)
        write_ledger(ledger_path, records)
    elif args.refresh_ledger:
        records = build_records(root, previous)
        write_ledger(ledger_path, records)
    else:
        records = list(previous.values())
        if not records:
            raise SystemExit("Audit ledger is missing. Bootstrap it deliberately before packet generation.")

    output = root / args.output
    rendered = render_packet(root, records)

    if args.check:
        if not output.exists():
            print(f"stale packet: missing {output.relative_to(root)}")
            return 1
        existing = output.read_text(encoding="utf-8")
        if existing != rendered:
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
