#!/usr/bin/env python3
"""Validate BFDM machine-readable project, server, and identity registries."""

from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry"


def load_jsonl(name: str, id_key: str, errors: list[str]) -> list[dict]:
    path = REG / name
    if not path.exists():
        errors.append(f"missing {path}")
        return []
    rows = []
    seen = set()
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except Exception as exc:
            errors.append(f"{path}:{n}: invalid JSON: {exc}")
            continue
        rid = row.get(id_key)
        if not rid:
            errors.append(f"{path}:{n}: missing {id_key}")
        elif rid in seen:
            errors.append(f"{path}:{n}: duplicate {id_key} {rid}")
        else:
            seen.add(rid)
        rows.append(row)
    return rows


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    projects = load_jsonl("projects.jsonl", "project_id", errors)
    relations = load_jsonl("project_relations.jsonl", "relation_id", errors)
    people = load_jsonl("people.jsonl", "person_id", errors)
    identities = load_jsonl("identities.jsonl", "identity_id", errors)
    servers = load_jsonl("discord_servers.jsonl", "server_id", errors)

    project_ids = {r["project_id"] for r in projects if r.get("project_id")}
    person_ids = {r["person_id"] for r in people if r.get("person_id")}
    server_ids = {r["server_id"] for r in servers if r.get("server_id")}

    # Source-container anchors should resolve against current evidence catalog.
    catalog_path = ROOT / "evidence" / "catalog.jsonl"
    bcs_ids = set()
    if catalog_path.exists():
        for n, raw in enumerate(catalog_path.read_text(encoding="utf-8").splitlines(), 1):
            if not raw.strip():
                continue
            try:
                row = json.loads(raw)
                cid = row.get("corpus_id")
                if cid:
                    bcs_ids.add(cid)
            except Exception as exc:
                errors.append(f"{catalog_path}:{n}: invalid JSON: {exc}")
    else:
        warnings.append("evidence/catalog.jsonl missing; BCS anchor resolution skipped")

    for p in projects:
        pid = p.get("project_id")
        for sid in p.get("discord_servers", []):
            if sid not in server_ids:
                errors.append(f"{pid}: discord server ref {sid} not found in registry/discord_servers.jsonl")
        for anchor in p.get("source_anchors", []):
            if anchor.get("kind") == "BCS":
                cid = anchor.get("id")
                if cid not in bcs_ids:
                    errors.append(f"{pid}: BCS anchor {cid} not found in evidence/catalog.jsonl")

        live = (p.get("dates") or {}).get("live_window")
        if live is not None:
            if not live.get("start"):
                errors.append(f"{pid}: live_window exists without start")
            if not live.get("basis"):
                errors.append(f"{pid}: live_window exists without basis")
            if not live.get("source_refs"):
                errors.append(f"{pid}: live_window exists without source_refs")

        # Guard against pretending retrospective Roanoke range is an exact season count.
        scale = p.get("scale") or {}
        if scale.get("exact_concurrent_players") in ("30-100", "30–100"):
            errors.append(f"{pid}: 30–100 retrospective Roanoke range cannot be stored as an exact project count")

    for rel in relations:
        a = rel.get("from_project_id")
        b = rel.get("to_project_id")
        if a not in project_ids:
            errors.append(f"{rel.get('relation_id')}: missing from_project_id {a}")
        if b not in project_ids:
            errors.append(f"{rel.get('relation_id')}: missing to_project_id {b}")
        if a == b:
            errors.append(f"{rel.get('relation_id')}: self-relation is not allowed")

    for s in servers:
        sid = s.get("server_id")
        for pid in s.get("project_ids", []):
            if pid not in project_ids:
                errors.append(f"server {sid}: project ref {pid} not found")
        stored = s.get("attachments_stored")
        expected = s.get("attachments_expected")
        if stored is not None and expected is not None and stored > expected:
            errors.append(f"server {sid}: attachments_stored > attachments_expected")

    for ident in identities:
        iid = ident.get("identity_id")
        pid = ident.get("person_id")
        if pid not in person_ids:
            errors.append(f"{iid}: person_id {pid} not found")
        if ident.get("platform") == "DISCORD":
            scope = ident.get("server_or_project_id")
            if scope and scope not in server_ids and scope not in project_ids:
                errors.append(f"{iid}: Discord server/project scope {scope} does not resolve")
            if not ident.get("account_id"):
                warnings.append(f"{iid}: Discord identity has no immutable account_id")
        if ident.get("confidence") == "TENTATIVE" and "ATTRIBUTION_ALLOWED" in str(ident.get("attribution_use")):
            errors.append(f"{iid}: tentative identity cannot authorize attribution")

    print(f"projects: {len(projects)}")
    print(f"project relations: {len(relations)}")
    print(f"people: {len(people)}")
    print(f"identity assertions: {len(identities)}")
    print(f"Discord servers: {len(servers)}")
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    if errors:
        print(f"FAILED: {len(errors)} registry error(s)", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1

    print("OK: BFDM registry validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
