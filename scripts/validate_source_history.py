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
    paths = list((repo / "sources").glob("**/metadata.json"))
    paths += list((repo / "context").glob("**/metadata.json"))
    for path in paths:
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


LIVE_TRAJECTORY = {
    "IMPLEMENTED_IN",
    "ALTERED_IN",
    "ABANDONED_IN",
    "OUTCOME_DOCUMENTED_IN",
}
REVISION_TRAJECTORY = {"REVISES", "SUPERSEDES", "PREDECESSOR_OF", "SUCCESSOR_OF"}


def _is_context(meta: dict) -> bool:
    return meta.get("source_role") == "CONTEXT_ONLY_THIRD_PARTY" or meta.get("seed_eligibility") == "CONTEXT_ONLY"


def _questions(meta: dict) -> set[str]:
    return {
        item.get("question")
        for item in (meta.get("historical_context") or {}).get("not_established") or []
        if item.get("question")
    }


def _prose_len(path: Path) -> int:
    if not path.is_file():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2]
    return len(text.strip())


def _body_readable(repo: Path, cid: str, meta: dict) -> bool:
    candidates: list[Path] = []
    for rep in meta.get("representations") or []:
        rel = str(rep.get("path") or "")
        if rel.endswith((".md", ".txt")):
            candidates.append(repo / rel)
    if not candidates:
        candidates.extend((repo / "sources").glob(f"**/{cid}/**/*.md"))
        candidates.extend((repo / "sources").glob(f"**/{cid}/*.md"))
        candidates.extend((repo / "context").glob(f"**/{cid}/**/*.md"))
    return any(_prose_len(path) >= 40 for path in candidates)


def classify_family(
    members: list[str],
    metas: list[dict],
    link_rows: list[dict],
    readable: list[bool],
    live_answered: bool,
) -> dict:
    """Split source orientation from longitudinal trajectory.

    A live-use gap is source orientation. It is not a trajectory.
    Publication is not live contact. Companion links are not revision.
    """
    placed = []
    unresolved_project = []
    for meta in metas:
        links = (meta.get("historical_context") or {}).get("project_links") or []
        questions = _questions(meta)
        placed.append(any(link.get("relation") == "BELONGS_TO_PROJECT" for link in links))
        unresolved_project.append("exact_project" in questions)
    kinds = {row.get("link_type") for row in link_rows}
    live_links = sorted(kinds & LIVE_TRAJECTORY)
    revision_links = sorted(kinds & REVISION_TRAJECTORY)
    context_only = all(_is_context(meta) for meta in metas)
    project_answered = all(
        ok or gap or _is_context(meta)
        for ok, gap, meta in zip(placed, unresolved_project, metas)
    )
    stage_answered = all(
        bool((meta.get("historical_context") or {}).get("production_stages"))
        or "production_stage" in _questions(meta)
        or _is_context(meta)
        for meta in metas
    )
    source_ready = all(readable) and project_answered and stage_answered and live_answered and not context_only
    if context_only:
        longitudinal = "NOT_PRECEDENT"
        trajectory = "context_only"
    elif live_links and revision_links:
        longitudinal = "LONGITUDINAL_RESEARCH_READY"
        trajectory = "live_contact_and_revision"
    elif live_links:
        longitudinal = "LONGITUDINAL_RESEARCH_READY"
        trajectory = "live_contact"
    elif revision_links:
        longitudinal = "LONGITUDINAL_RESEARCH_READY"
        trajectory = "revision"
    elif source_ready:
        longitudinal = "LONGITUDINAL_RESEARCH_GAP"
        trajectory = "none"
    else:
        longitudinal = "NOT_SOURCE_READY"
        trajectory = "none"
    if context_only:
        status = "CONTEXT_ONLY"
    elif not all(readable) or not project_answered:
        status = "GAP_REMAINS"
    elif source_ready and longitudinal == "LONGITUDINAL_RESEARCH_READY":
        status = "SOURCE_RESEARCH_READY"
    elif source_ready:
        status = "SOURCE_RESEARCH_READY"
    else:
        status = "PLACED" if any(placed) else "GAP_REMAINS"
    return {
        "status": status,
        "source_research_ready": source_ready,
        "longitudinal_status": longitudinal,
        "trajectory": trajectory,
        "members": members,
        "readable_body": all(readable),
        "exact_project_members": [cid for cid, ok in zip(members, placed) if ok],
        "unresolved_project_members": [cid for cid, gap in zip(members, unresolved_project) if gap],
        "live_question_answered": live_answered,
        "live_link_types": live_links,
        "revision_link_types": revision_links,
        "context_only": context_only,
    }


def readiness(repo: Path, records: dict[str, dict], catalog: dict[str, dict]) -> dict:
    families: dict[str, list[str]] = {}
    for cid, meta in records.items():
        family = meta.get("document_family_id")
        if family:
            families.setdefault(family, []).append(cid)
    incoming: dict[str, list[dict]] = {}
    for cid, meta in records.items():
        for link in meta.get("source_links") or []:
            target = link.get("to_corpus_id")
            if target:
                incoming.setdefault(target, []).append(link)
    family_reports = []
    for family, members in sorted(families.items()):
        ordered = sorted(members)
        metas = [records[cid] for cid in ordered]
        readable = [_body_readable(repo, cid, meta) for cid, meta in zip(ordered, metas)]
        member_set = set(ordered)
        link_rows = []
        internal = 0
        cross = 0
        for meta in metas:
            for link in meta.get("source_links") or []:
                target = link.get("to_corpus_id")
                external = str(link.get("external_locator") or "")
                if target in records or target in member_set:
                    link_rows.append(link)
                    if link.get("link_type") in CROSS_MEDIUM or external.startswith("discord:"):
                        cross += 1
                    else:
                        internal += 1
                elif link.get("link_type") in CROSS_MEDIUM or external.startswith("discord:"):
                    link_rows.append(link)
                    cross += 1
                elif external.startswith("sources/"):
                    internal += 1
        for other_id, other in records.items():
            if other_id in member_set:
                continue
            for link in other.get("source_links") or []:
                if link.get("to_corpus_id") in member_set:
                    link_rows.append(link)
                    if link.get("link_type") in CROSS_MEDIUM:
                        cross += 1
                    else:
                        internal += 1
        def member_live(cid: str, meta: dict) -> bool:
            own = any(
                link.get("link_type") in LIVE_TRAJECTORY
                for link in (meta.get("source_links") or [])
            )
            cited = any(
                link.get("link_type") in LIVE_TRAJECTORY for link in incoming.get(cid, [])
            )
            return own or cited or "live_use" in _questions(meta) or _is_context(meta)

        live_answered = all(member_live(cid, meta) for cid, meta in zip(ordered, metas))
        report = classify_family(ordered, metas, link_rows, readable, live_answered)
        report["document_family_id"] = family
        report["internal_or_version_links"] = internal
        report["cross_medium_links"] = cross
        family_reports.append(report)

    archived_only = sorted(cid for cid in catalog if cid not in records)
    evidence_gaps = []
    archive_gaps = []
    for cid, meta in sorted(records.items()):
        for item in (meta.get("historical_context") or {}).get("not_established") or []:
            question = item.get("question")
            row = {
                "corpus_id": cid,
                "question": question,
                "status": item.get("status"),
                "basis": item.get("basis"),
                "document_family_id": meta.get("document_family_id"),
            }
            if question == "referenced_source_absent" or item.get("status") == "ARCHIVE_GAP":
                archive_gaps.append(row)
            elif question in {
                "exact_project",
                "exact_week",
                "live_use",
                "week_5_date_alignment",
                "rule_by_rule_live_identity",
                "brendon_authorship",
                "production_stage",
            }:
                evidence_gaps.append(row)
    return {
        "families": family_reports,
        "archived_only_catalog_ids": archived_only,
        "evidence_gaps": evidence_gaps,
        "archive_gaps": archive_gaps,
        "container_count": len(records),
        "catalog_count": len(catalog),
    }


def _family_line(row: dict) -> str:
    longitudinal = row["longitudinal_status"]
    source = "yes" if row["source_research_ready"] else "no"
    return (
        f"| `{row['document_family_id']}` | {row['status']} | {source} | {longitudinal} | "
        f"{row['trajectory']} | {len(row['members'])} |"
    )


def render_markdown(report: dict) -> str:
    lines = [
        "# Drive source research readiness — 2026-10-05",
        "",
        "This report is derived from source `metadata.json` files. It does not add relationships that are not stored there.",
        "",
        "`SOURCE_RESEARCH_READY` means a reader can tell what the source is, where it is placed or that placement is explicitly unknown, what production stage it is or that the stage is explicitly unknown, and whether live use has been tied to a message or channel. It does not mean the research has been done.",
        "",
        "`LONGITUDINAL_RESEARCH_READY` currently means at least one qualifying trajectory edge exists: a revision link (`REVISES`, `SUPERSEDES`, `PREDECESSOR_OF`, `SUCCESSOR_OF`) or a live-contact link (`IMPLEMENTED_IN`, `ALTERED_IN`, `ABANDONED_IN`, `OUTCOME_DOCUMENTED_IN`). It does not mean the family has a complete or representative longitudinal chain. Companion links, publication links, and an explicit live-use gap are not a trajectory.",
        "",
        "An explicit live-use gap is an evidence gap. It does not make a family longitudinally complete.",
        "",
        "Archive gap means a known artifact is still missing from the repository. Evidence gap means the sources that are present do not establish the fact. Those are not the same.",
        "",
        "## Decision-trajectory families",
        "",
        "These are the families a researcher can follow from preparation into revision or into recorded live contact. Revision is not play. Live contact is only as wide as the cited link.",
        "",
        "| Family | Trajectory | Members |",
        "| --- | --- | --- |",
    ]
    ready = [
        row
        for row in report["families"]
        if row["longitudinal_status"] == "LONGITUDINAL_RESEARCH_READY"
    ]
    if not ready:
        lines.append("| none | | |")
    for row in ready:
        lines.append(
            f"| `{row['document_family_id']}` | {row['trajectory']} | "
            + ", ".join(f"`{cid}`" for cid in row["members"])
            + " |"
        )
    lines.extend(
        [
            "",
            "## Source orientation only",
            "",
            "Readable and placed, or explicitly unplaced, but not a revision or live-contact trajectory.",
            "",
            "| Family | Longitudinal | Members |",
            "| --- | --- | --- |",
        ]
    )
    orientation = [
        row
        for row in report["families"]
        if row["source_research_ready"] and row["longitudinal_status"] == "LONGITUDINAL_RESEARCH_GAP"
    ]
    for row in orientation:
        lines.append(
            f"| `{row['document_family_id']}` | LONGITUDINAL_RESEARCH_GAP | "
            + ", ".join(f"`{cid}`" for cid in row["members"])
            + " |"
        )
    lines.extend(["", "## Context, not precedent", ""])
    contexts = [row for row in report["families"] if row["context_only"]]
    if not contexts:
        lines.append("None.")
    for row in contexts:
        lines.append(
            f"`{row['document_family_id']}`: "
            + ", ".join(f"`{cid}`" for cid in row["members"])
            + ". Third-party context. Not BFDM precedent."
        )
        lines.append("")
    lines.extend(
        [
            "## Families",
            "",
            "| Family | Status | Source ready | Longitudinal | Trajectory | Members |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in report["families"]:
        lines.append(_family_line(row))
    lines.extend(["", "## Family detail", ""])
    for row in report["families"]:
        lines.append(
            f"### `{row['document_family_id']}` — {row['status']} / {row['longitudinal_status']}"
        )
        lines.append("")
        lines.append("Members: " + ", ".join(f"`{cid}`" for cid in row["members"]))
        lines.append("")
        lines.append(f"Trajectory: `{row['trajectory']}`.")
        lines.append("")
        if row["unresolved_project_members"]:
            lines.append(
                "Exact project deliberately unresolved: "
                + ", ".join(f"`{cid}`" for cid in row["unresolved_project_members"])
            )
            lines.append("")
        if row["trajectory"] == "revision":
            lines.append("This trajectory is revision history, not live play.")
            lines.append("")
        if row["trajectory"] == "live_contact":
            lines.append(
                "Live contact is only the recorded "
                + ", ".join(row["live_link_types"])
                + " link. It is not a claim that every rule in the family was used."
            )
            lines.append("")
        if not row["live_question_answered"] and not row["context_only"]:
            lines.append("Live-use question is not yet explicit on every member.")
            lines.append("")
    lines.extend(
        [
            "## Evidence gaps",
            "",
            "The source is present. The fact is not established. Do not fill these in by inference.",
            "",
        ]
    )
    if not report["evidence_gaps"]:
        lines.append("None recorded.")
        lines.append("")
    for row in report["evidence_gaps"]:
        lines.append(
            f"- `{row['corpus_id']}` `{row['question']}` ({row['status']}): {row['basis']}"
        )
    lines.extend(
        [
            "",
            "## Archive gaps",
            "",
            f"{len(report['archived_only_catalog_ids'])} catalog records have no `metadata.json` container. They remain `ARCHIVED_ONLY`.",
            "",
        ]
    )
    if report["archived_only_catalog_ids"]:
        lines.append(
            "Catalog-only ids: "
            + ", ".join(f"`{cid}`" for cid in report["archived_only_catalog_ids"])
            + "."
        )
        lines.append("")
    if report["archive_gaps"]:
        lines.append("Containers that cite a source the repository does not hold:")
        lines.append("")
        for row in report["archive_gaps"]:
            lines.append(f"- `{row['corpus_id']}`: {row['basis']}")
        lines.append("")
    lines.extend(
        [
            "Season 5 Google Site sources that are publication captures are not Drive draft families. "
            "Season 5 is not longitudinally ready for prep-to-play judgment. Its live and dev-Discord bridge is an archive gap, not a hidden fact inside the Drive PDFs.",
            "",
            "Container count includes context containers and Season 5 site metadata as well as Drive containers.",
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
