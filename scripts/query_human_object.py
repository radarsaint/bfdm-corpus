#!/usr/bin/env python3
"""Resolve a BFDM human object by ordinary remembered name.

This is a derived human-facing projection over corpus provenance. A miss means
"not indexed yet", not "does not exist in Brendon's work".
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            rows.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_number}: invalid JSON: {exc}") from exc
    return rows


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = value.replace("’", "'").replace("‘", "'")
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return " ".join(value.split())


def candidate_names(obj: dict) -> list[tuple[str, str]]:
    names = [(obj.get("canonical_name", ""), "canonical")]
    for alias in obj.get("aliases") or []:
        name = alias.get("name")
        if name:
            names.append((name, "alias"))
    return [(name, kind) for name, kind in names if name]


def resolve(
    objects: list[dict],
    query: str,
    project: str | None = None,
    contains: bool = False,
) -> dict:
    needle = normalize_name(query)
    matches: list[dict] = []

    for obj in objects:
        if project and project not in (obj.get("project_ids") or []):
            continue

        matched_names = []
        for name, kind in candidate_names(obj):
            normalized = normalize_name(name)
            matched = needle in normalized if contains else needle == normalized
            if matched:
                matched_names.append({"name": name, "kind": kind})

        if matched_names:
            matches.append({"object": obj, "matched_names": matched_names})

    if not matches:
        return {
            "status": "NOT_INDEXED",
            "query": query,
            "project": project,
            "message": (
                "No human object is indexed under this name yet. "
                "This is not evidence that the thing does not exist in the corpus."
            ),
        }

    if len(matches) > 1:
        return {
            "status": "AMBIGUOUS",
            "query": query,
            "project": project,
            "candidates": [
                {
                    "object_id": item["object"]["object_id"],
                    "canonical_name": item["object"]["canonical_name"],
                    "object_type": item["object"]["object_type"],
                    "project_ids": item["object"].get("project_ids") or [],
                    "matched_names": item["matched_names"],
                }
                for item in matches
            ],
        }

    return {
        "status": "RESOLVED",
        "query": query,
        "project": project,
        **matches[0],
    }


def build_report(
    repo: Path,
    query: str,
    project: str | None = None,
    contains: bool = False,
) -> dict:
    registry = repo / "registry"
    objects = load_jsonl(registry / "human_objects.jsonl")
    assertions = load_jsonl(registry / "human_object_assertions.jsonl")
    relations = load_jsonl(registry / "human_object_relations.jsonl")

    result = resolve(objects, query, project=project, contains=contains)
    if result["status"] != "RESOLVED":
        return result

    obj = result["object"]
    object_id = obj["object_id"]
    by_id = {row["object_id"]: row for row in objects}

    object_assertions = [
        row for row in assertions if row.get("object_id") == object_id
    ]

    relation_rows = []
    for row in relations:
        if row.get("from_object_id") == object_id:
            target = by_id.get(row.get("to_object_id"))
            relation_rows.append(
                {
                    **row,
                    "direction": "OUTGOING",
                    "other_name": target.get("canonical_name") if target else row.get("to_object_id"),
                }
            )
        elif row.get("to_object_id") == object_id:
            source = by_id.get(row.get("from_object_id"))
            relation_rows.append(
                {
                    **row,
                    "direction": "INCOMING",
                    "other_name": source.get("canonical_name") if source else row.get("from_object_id"),
                }
            )

    source_refs = set(obj.get("source_refs") or [])
    for row in object_assertions:
        source_refs.update(row.get("support_refs") or [])
    for row in relation_rows:
        source_refs.update(row.get("support_refs") or [])

    return {
        "status": "RESOLVED",
        "query": query,
        "matched_names": result["matched_names"],
        "object": obj,
        "assertions": object_assertions,
        "relations": relation_rows,
        "source_refs": sorted(source_refs),
        "coverage_warning": (
            "The human-object registry is experimental and incomplete. "
            "Missing facts or relations may exist in unindexed corpus sources."
        ),
    }


def render_value(value: dict) -> str:
    kind = value.get("kind")
    if kind == "TEXT":
        return str(value.get("text", ""))
    if kind == "LIST":
        return ", ".join(str(item) for item in value.get("items") or [])
    return json.dumps(value, ensure_ascii=False)


def render_text(report: dict) -> str:
    status = report["status"]

    if status == "NOT_INDEXED":
        return f"{report['query']}: NOT INDEXED\n{report['message']}\n"

    if status == "AMBIGUOUS":
        lines = [f"{report['query']}: AMBIGUOUS"]
        for row in report["candidates"]:
            projects = ", ".join(row["project_ids"]) or "unscoped"
            lines.append(
                f"- {row['canonical_name']} [{row['object_type']}] "
                f"{row['object_id']} projects={projects}"
            )
        lines.append("Use --project or a more specific name.")
        return "\n".join(lines) + "\n"

    obj = report["object"]
    lines = [
        obj["canonical_name"],
        f"id: {obj['object_id']}",
        f"type: {obj['object_type']}",
    ]

    facets = obj.get("facets") or []
    if facets:
        lines.append("facets: " + ", ".join(facets))

    projects = obj.get("project_ids") or []
    if projects:
        lines.append("projects: " + ", ".join(projects))

    aliases = [row.get("name") for row in obj.get("aliases") or [] if row.get("name")]
    if aliases:
        lines.append("aliases: " + ", ".join(aliases))

    lines.append("")
    lines.append("assertions:")
    if not report["assertions"]:
        lines.append("  (none indexed)")
    for row in report["assertions"]:
        status_label = row.get("epistemic_status", "UNKNOWN")
        confidence = row.get("confidence", "")
        lines.append(
            f"  {row.get('predicate')}: {render_value(row.get('value') or {})} "
            f"[{status_label}; {confidence}]"
        )
        refs = row.get("support_refs") or []
        if refs:
            lines.append("    sources: " + ", ".join(refs))

    lines.append("")
    lines.append("relations:")
    if not report["relations"]:
        lines.append("  (none indexed)")
    for row in report["relations"]:
        if row["direction"] == "OUTGOING":
            lines.append(
                f"  -> {row.get('relation')} -> {row.get('other_name')} "
                f"[{row.get('confidence')}]"
            )
        else:
            lines.append(
                f"  <- {row.get('relation')} <- {row.get('other_name')} "
                f"[{row.get('confidence')}]"
            )
        refs = row.get("support_refs") or []
        if refs:
            lines.append("    sources: " + ", ".join(refs))

    lines.append("")
    lines.append("all source refs: " + ", ".join(report["source_refs"]))
    lines.append("")
    lines.append("coverage: " + report["coverage_warning"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Resolve a remembered BFDM person/place/thing/concept to literal corpus grounding."
    )
    parser.add_argument("query")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--project", help="Optional project id used for disambiguation.")
    parser.add_argument(
        "--contains",
        action="store_true",
        help="Allow substring matching. Exact canonical/alias matching is safer and remains the default.",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    report = build_report(
        Path(args.repo).resolve(),
        args.query,
        project=args.project,
        contains=args.contains,
    )

    if args.json:
        json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_text(report))

    if report["status"] == "RESOLVED":
        return 0
    if report["status"] == "AMBIGUOUS":
        return 3
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
