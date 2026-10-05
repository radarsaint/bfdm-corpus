#!/usr/bin/env python3
"""Validate explicit Drive-source historical links and write readiness.

Canonical relationship truth is source metadata. This does not score
research quality. It checks that recorded links point at real records
and that unknown placement was not given a false project id.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

STAGES = {
    "RESEARCH_INSPIRATION",
    "BRAINSTORMING",
    "PREPRODUCTION",
    "SYSTEM_DEVELOPMENT",
    "CAMPAIGN_OPERATIONS",
    "LIVE_USE_ARTIFACT",
    "PUBLIC_PLAYER_FACING_PUBLICATION",
    "POSTMORTEM_CORRECTION",
    "LATER_RETROSPECTIVE",
}
PROJECT_RELS = {"BELONGS_TO_PROJECT", "RELATES_TO_PROJECT", "CROSS_PROJECT"}
LINK_TYPES = {
    "PREDECESSOR_OF",
    "SUCCESSOR_OF",
    "REVISES",
    "SUPERSEDES",
    "DEV_PUBLIC_PAIR",
    "PUBLISHED_AS",
    "DERIVED_FROM",
    "COPY_OF",
    "RESPONSE_TO",
    "COMPANION_TO",
    "IMPLEMENTED_IN",
    "DISCUSSED_IN",
    "ALTERED_IN",
    "ABANDONED_IN",
    "OUTCOME_DOCUMENTED_IN",
    # Already on main before this pass. Do not reject them.
    "SOURCE_VERSION_FAMILY_MEMBER",
    "REVISION_CONTEXT_FOR_SOURCE_FAMILY",
    "VERSION_FAMILY_MEMBER",
    "PUBLISHED_VERSION_OF_OR_RELATED_TO",
}
CONFIDENCE = {"CONFIRMED", "STRONG"}
CROSS_MEDIUM = {
    "IMPLEMENTED_IN",
    "DISCUSSED_IN",
    "ALTERED_IN",
    "ABANDONED_IN",
    "OUTCOME_DOCUMENTED_IN",
    "PUBLISHED_AS",
}
# Donor ids that current main already uses for Season 5.
COLLISION = {
    "BCS-000087": "BCS-000115",
    "BCS-000088": "BCS-000116",
    "BCS-000089": "BCS-000117",
    "BCS-000090": "BCS-000118",
    "BCS-000091": "BCS-000119",
    "BCS-000092": "BCS-000120",
    "BCS-000093": "BCS-000121",
}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def metadata_records(repo: Path) -> dict[str, dict]:
    records = {}
    for path in (repo / "sources").glob("**/metadata.json"):
        meta = json.loads(path.read_text(encoding="utf-8"))
        cid = meta.get("corpus_id")
        if isinstance(cid, str):
            records[cid] = meta
    return records


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate(repo: Path) -> tuple[list[str], dict]:
    errors: list[str] = []
    records = metadata_records(repo)
    catalog = {row["corpus_id"]: row for row in load_jsonl(repo / "evidence" / "catalog.jsonl")}
    projects = {
        row["project_id"]
        for row in load_jsonl(repo / "registry" / "projects.jsonl")
        if row.get("project_id")
    }
    known_ids = set(records) | set(catalog)

    for cid, meta in sorted(records.items()):
        recon = meta.get("reconciliation") or {}
        donor = recon.get("donor_corpus_id")
        if donor in COLLISION and cid != COLLISION[donor]:
            fail(errors, f"{cid}: donor {donor} must reconcile to {COLLISION[donor]}")
        if cid in COLLISION and (donor or cid) == cid and meta.get("project_slug") == "roanoke":
            fail(errors, f"{cid}: Season 5 id still used as a Roanoke Drive container")

        context = meta.get("historical_context") or {}
        for link in context.get("project_links") or []:
            if link.get("relation") not in PROJECT_RELS:
                fail(errors, f"{cid}: bad project relation {link.get('relation')}")
            if link.get("project_id") not in projects:
                fail(errors, f"{cid}: unknown project {link.get('project_id')}")
            if link.get("confidence") not in CONFIDENCE:
                fail(errors, f"{cid}: project link missing usable confidence")
            if not link.get("basis") or not link.get("support_refs"):
                fail(errors, f"{cid}: project link missing basis or support_refs")
        for stage in context.get("production_stages") or []:
            if stage.get("stage") not in STAGES:
                fail(errors, f"{cid}: bad production stage {stage.get('stage')}")
            if stage.get("confidence") not in CONFIDENCE or not stage.get("basis"):
                fail(errors, f"{cid}: production stage missing basis or confidence")
        for item in context.get("not_established") or []:
            if not item.get("question") or not item.get("basis"):
                fail(errors, f"{cid}: not_established entry is incomplete")

        for link in meta.get("source_links") or []:
            if link.get("link_type") not in LINK_TYPES:
                fail(errors, f"{cid}: bad link type {link.get('link_type')}")
            if link.get("confidence") not in CONFIDENCE:
                fail(errors, f"{cid}: link missing usable confidence")
            if not link.get("basis"):
                fail(errors, f"{cid}: link missing basis")
            target = link.get("to_corpus_id")
            external = link.get("external_locator")
            if target and target not in known_ids:
                fail(errors, f"{cid}: link target {target} is not a catalog or container id")
            if not target and not external:
                fail(errors, f"{cid}: link has neither to_corpus_id nor external_locator")
            if link.get("link_type") == "SUPERSEDES" and "newer" in str(link.get("basis", "")).lower():
                fail(errors, f"{cid}: SUPERSEDES basis appears to mean merely newer")

    return errors, readiness(repo, records, catalog)


def readiness(repo: Path, records: dict[str, dict], catalog: dict[str, dict]) -> dict:
    families: dict[str, list[str]] = {}
    for cid, meta in records.items():
        family = meta.get("document_family_id")
        if family:
            families.setdefault(family, []).append(cid)
    family_reports = []
    for family, members in sorted(families.items()):
        metas = [records[cid] for cid in sorted(members)]
        readable = []
        for cid, meta in zip(sorted(members), metas):
            reps = meta.get("representations") or []
            listed = any(
                str(rep.get("path", "")).endswith((".md", ".txt")) for rep in reps
            )
            on_disk = any((repo / "sources").glob(f"**/{cid}/**/*.md")) or any(
                (repo / "sources").glob(f"**/{cid}/*.md")
            )
            readable.append(listed or on_disk)
        placed = []
        unresolved_project = []
        for meta in metas:
            links = (meta.get("historical_context") or {}).get("project_links") or []
            notes = (meta.get("historical_context") or {}).get("not_established") or []
            placed.append(any(link.get("relation") == "BELONGS_TO_PROJECT" for link in links))
            unresolved_project.append(
                any(item.get("question") == "exact_project" for item in notes)
            )
        internal_links = 0
        cross = 0
        member_set = set(members)
        for meta in metas:
            for link in meta.get("source_links") or []:
                if link.get("to_corpus_id") in member_set or link.get("to_corpus_id") in records:
                    if link.get("link_type") in CROSS_MEDIUM or str(
                        link.get("external_locator") or ""
                    ).startswith("discord:"):
                        cross += 1
                    else:
                        internal_links += 1
                elif link.get("link_type") in CROSS_MEDIUM or str(
                    link.get("external_locator") or ""
                ).startswith("discord:"):
                    cross += 1
                elif str(link.get("external_locator") or "").startswith("sources/"):
                    internal_links += 1
        for other_id, other in records.items():
            if other_id in member_set:
                continue
            for link in other.get("source_links") or []:
                if link.get("to_corpus_id") not in member_set:
                    continue
                if link.get("link_type") in CROSS_MEDIUM:
                    cross += 1
                else:
                    internal_links += 1
        all_readable = all(readable)
        any_placed = any(placed)
        project_question_answered = all(
            ok or gap for ok, gap in zip(placed, unresolved_project)
        )
        live_answered = all(
            any(link.get("link_type") in CROSS_MEDIUM for link in (meta.get("source_links") or []))
            or any(
                item.get("question") == "live_use"
                for item in (meta.get("historical_context") or {}).get("not_established") or []
            )
            for meta in metas
        )
        if not all_readable:
            status = "GAP_REMAINS"
        elif cross:
            status = "CROSS_MEDIUM_LINKED"
        elif len(members) > 1 or internal_links:
            status = "FAMILY_LINKED"
        elif any_placed:
            status = "PLACED"
        else:
            status = "GAP_REMAINS"
        connected = internal_links > 0 or cross > 0 or len(members) > 1
        research_ready = (
            all_readable
            and project_question_answered
            and connected
            and live_answered
            and status != "GAP_REMAINS"
        )
        if research_ready:
            status = "RESEARCH_READY"
        family_reports.append(
            {
                "document_family_id": family,
                "status": status,
                "members": sorted(members),
                "readable_body": all_readable,
                "exact_project_members": [
                    cid for cid, ok in zip(sorted(members), placed) if ok
                ],
                "unresolved_project_members": [
                    cid for cid, gap in zip(sorted(members), unresolved_project) if gap
                ],
                "internal_or_version_links": internal_links,
                "cross_medium_links": cross,
                "live_question_answered": live_answered,
            }
        )

    archived_only = sorted(
        cid for cid in catalog if cid not in records
    )
    return {
        "families": family_reports,
        "archived_only_catalog_ids": archived_only,
        "container_count": len(records),
        "catalog_count": len(catalog),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Drive source research readiness — 2026-10-05",
        "",
        "This report is derived from source `metadata.json` files. It does not add relationships that are not stored there.",
        "",
        "A status of `RESEARCH_READY` means a fresh reader can answer project, stage or explicit stage-gap, family, and live-use-or-not-established from the metadata. It does not mean the historical research has been done.",
        "",
        "## Families with containers",
        "",
        "| Family | Status | Members | Readable body | Cross-medium links |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in report["families"]:
        lines.append(
            "| `{family}` | {status} | {n} | {body} | {cross} |".format(
                family=row["document_family_id"],
                status=row["status"],
                n=len(row["members"]),
                body="yes" if row["readable_body"] else "no",
                cross=row["cross_medium_links"],
            )
        )
    lines.extend(["", "## Family detail", ""])
    for row in report["families"]:
        lines.append(f"### `{row['document_family_id']}` — {row['status']}")
        lines.append("")
        lines.append("Members: " + ", ".join(f"`{cid}`" for cid in row["members"]))
        lines.append("")
        if row["unresolved_project_members"]:
            lines.append(
                "Exact project deliberately unresolved: "
                + ", ".join(f"`{cid}`" for cid in row["unresolved_project_members"])
            )
            lines.append("")
        if not row["live_question_answered"]:
            lines.append("Live-use question is not yet explicit on every member.")
            lines.append("")
    lines.extend(
        [
            "## Catalog records with no source container",
            "",
            f"{len(report['archived_only_catalog_ids'])} catalog records have no `metadata.json` container on this branch. They remain `ARCHIVED_ONLY`.",
            "",
            "Highest-value groups still in that state:",
            "",
            "- Empire City session posts and signup, `BCS-000004` through `BCS-000016`, are catalog records only. Season 4 directory, backlog, crafting, airship module, and the player-facing setting text are containerized; the dated post series is not.",
            "- Roanoke week cast lists, passdowns, and set lists from the older staging range are still catalog-only, except the master timeline, changelog, rough draft, 2.0 manuscript, and complete day manuscript ported in this pass.",
            "- `BCS-000059` Exploration Impossible remains a catalog/context record without its donor container.",
            "- Season 5 Google Site sources `BCS-000087` through `BCS-000112` are publication captures. This pass does not treat them as Drive draft families except the already-landed Way of Gun Fu publication link.",
            "",
            "Container count includes Season 5 site metadata as well as Drive containers.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors, report = validate(repo)
    if args.write_report:
        out_dir = repo / "research" / "drive-integration"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "RESEARCH_READINESS_2026-10-05.json").write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8"
        )
        (out_dir / "RESEARCH_READINESS_2026-10-05.md").write_text(
            render_markdown(report), encoding="utf-8"
        )
        print(f"wrote readiness for {len(report['families'])} families")
    print(f"source containers: {report['container_count']}")
    print(f"families: {len(report['families'])}")
    counts: dict[str, int] = {}
    for row in report["families"]:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    print("status counts:", counts)
    if errors:
        print(f"FAILED: {len(errors)} source-history error(s)", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1
    print("OK: source history links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
