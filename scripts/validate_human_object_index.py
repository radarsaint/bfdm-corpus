#!/usr/bin/env python3
"""Validate the experimental BFDM human-object registry."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from query_human_object import load_jsonl, normalize_name


OBJECT_TYPES = {
    "CHARACTER",
    "PERSON",
    "PLACE",
    "ORGANIZATION",
    "FACTION",
    "ITEM",
    "ARTIFACT",
    "CREATURE",
    "SPECIES",
    "MECHANIC",
    "SYSTEM",
    "EVENT",
    "ARC",
    "CONCEPT",
    "ENTITY",
}
OBJECT_STATUS = {"ESTABLISHED", "PROVISIONAL", "DEPRECATED"}
EPISTEMIC_STATUS = {"KNOWN", "UNKNOWN", "CONFLICTING", "INFERRED"}
CONFIDENCE = {"CONFIRMED", "STRONG", "WEAK", "UNRESOLVED"}
BCS_RE = re.compile(r"^BCS-\d{6}$")


def ids_from_jsonl(path: Path, key: str) -> set[str]:
    return {row[key] for row in load_jsonl(path) if row.get(key)}


def validate(repo: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    registry = repo / "registry"

    objects = load_jsonl(registry / "human_objects.jsonl")
    assertions = load_jsonl(registry / "human_object_assertions.jsonl")
    relations = load_jsonl(registry / "human_object_relations.jsonl")
    projects = ids_from_jsonl(registry / "projects.jsonl", "project_id")
    catalog = ids_from_jsonl(repo / "evidence" / "catalog.jsonl", "corpus_id")

    object_ids: set[str] = set()
    alias_buckets: dict[str, list[tuple[str, set[str]]]] = {}

    for row in objects:
        oid = row.get("object_id")
        if not oid:
            errors.append("human object missing object_id")
            continue
        if oid in object_ids:
            errors.append(f"duplicate object_id: {oid}")
        object_ids.add(oid)

        if row.get("object_type") not in OBJECT_TYPES:
            errors.append(f"{oid}: unsupported object_type {row.get('object_type')!r}")
        if row.get("status") not in OBJECT_STATUS:
            errors.append(f"{oid}: unsupported status {row.get('status')!r}")
        if not row.get("canonical_name"):
            errors.append(f"{oid}: missing canonical_name")

        for project_id in row.get("project_ids") or []:
            if project_id not in projects:
                errors.append(f"{oid}: unknown project_id {project_id}")

        refs = row.get("source_refs") or []
        if not refs:
            warnings.append(f"{oid}: no source_refs")
        for ref in refs:
            if BCS_RE.match(str(ref)) and ref not in catalog:
                errors.append(f"{oid}: source ref not in catalog: {ref}")

        names = [(row.get("canonical_name"), "canonical")]
        names.extend((alias.get("name"), "alias") for alias in row.get("aliases") or [])
        scopes = set(row.get("project_ids") or [])
        for name, kind in names:
            if not name:
                continue
            normalized = normalize_name(name)
            alias_buckets.setdefault(normalized, []).append((oid, scopes))
            if kind == "alias":
                alias = next(
                    item for item in row.get("aliases") or [] if item.get("name") == name
                )
                for ref in alias.get("support_refs") or []:
                    if BCS_RE.match(str(ref)) and ref not in catalog:
                        errors.append(f"{oid}: alias source ref not in catalog: {ref}")

    assertion_ids: set[str] = set()
    for row in assertions:
        aid = row.get("assertion_id")
        if not aid:
            errors.append("human-object assertion missing assertion_id")
            continue
        if aid in assertion_ids:
            errors.append(f"duplicate assertion_id: {aid}")
        assertion_ids.add(aid)

        oid = row.get("object_id")
        if oid not in object_ids:
            errors.append(f"{aid}: unknown object_id {oid}")
        if row.get("epistemic_status") not in EPISTEMIC_STATUS:
            errors.append(
                f"{aid}: unsupported epistemic_status {row.get('epistemic_status')!r}"
            )
        if row.get("confidence") not in CONFIDENCE:
            errors.append(f"{aid}: unsupported confidence {row.get('confidence')!r}")
        if not row.get("predicate"):
            errors.append(f"{aid}: missing predicate")
        if not isinstance(row.get("value"), dict):
            errors.append(f"{aid}: value must be an object")

        refs = row.get("support_refs") or []
        if row.get("epistemic_status") != "UNKNOWN" and not refs:
            errors.append(f"{aid}: supported assertion has no support_refs")
        for ref in refs:
            if BCS_RE.match(str(ref)) and ref not in catalog:
                errors.append(f"{aid}: support ref not in catalog: {ref}")

    relation_ids: set[str] = set()
    for row in relations:
        rid = row.get("relation_id")
        if not rid:
            errors.append("human-object relation missing relation_id")
            continue
        if rid in relation_ids:
            errors.append(f"duplicate relation_id: {rid}")
        relation_ids.add(rid)

        source = row.get("from_object_id")
        if source not in object_ids:
            errors.append(f"{rid}: unknown from_object_id {source}")

        target_kind = row.get("target_kind")
        if target_kind == "HUMAN_OBJECT":
            target = row.get("to_object_id")
            if target not in object_ids:
                errors.append(f"{rid}: unknown to_object_id {target}")
        elif target_kind == "PROJECT":
            target = row.get("to_project_id")
            if target not in projects:
                errors.append(f"{rid}: unknown to_project_id {target}")
        else:
            errors.append(f"{rid}: unsupported target_kind {target_kind!r}")

        if not row.get("relation"):
            errors.append(f"{rid}: missing relation")
        if row.get("confidence") not in CONFIDENCE:
            errors.append(f"{rid}: unsupported confidence {row.get('confidence')!r}")

        refs = row.get("support_refs") or []
        if not refs:
            errors.append(f"{rid}: relation has no support_refs")
        for ref in refs:
            if BCS_RE.match(str(ref)) and ref not in catalog:
                errors.append(f"{rid}: support ref not in catalog: {ref}")

    for normalized, candidates in sorted(alias_buckets.items()):
        unique_ids = {oid for oid, _ in candidates}
        if len(unique_ids) < 2:
            continue
        overlapping = False
        candidate_list = list(candidates)
        for index, (_, left_scope) in enumerate(candidate_list):
            for _, right_scope in candidate_list[index + 1 :]:
                if not left_scope or not right_scope or left_scope & right_scope:
                    overlapping = True
        if overlapping:
            warnings.append(
                f"ambiguous human name {normalized!r}: {', '.join(sorted(unique_ids))}"
            )

    return errors, warnings


def main() -> int:
    repo = Path(".").resolve()
    errors, warnings = validate(repo)

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    if errors:
        print(f"FAILED: {len(errors)} human-object validation error(s)", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1

    print("OK: BFDM human-object index validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
