#!/usr/bin/env python3
"""Validate registry/source_relations.jsonl referential integrity."""
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path):
    rows=[]
    for n,raw in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not raw.strip(): continue
        try: rows.append((n,json.loads(raw)))
        except Exception as e:
            print(f"{path}:{n}: invalid JSON: {e}",file=sys.stderr); raise SystemExit(1)
    return rows
def main():
    errors=[]
    catalog={r.get("corpus_id") for _,r in load(ROOT/"evidence/catalog.jsonl")}
    projects={r.get("project_id") for _,r in load(ROOT/"registry/projects.jsonl")}
    seen=set()
    allowed={"SOURCE","PROJECT","PRODUCTION_PHASE","DISCORD_MESSAGE","DISCORD_SERVER","SOURCE_FAMILY","EXTERNAL"}
    rels=load(ROOT/"registry/source_relations.jsonl")
    for n,r in rels:
        rid=r.get("relation_id")
        if not rid: errors.append(f"line {n}: missing relation_id")
        elif rid in seen: errors.append(f"line {n}: duplicate relation_id {rid}")
        else: seen.add(rid)
        if r.get("schema_version")!="bfdm_source_relation/v1": errors.append(f"{rid}: wrong schema_version")
        if r.get("from_source_id") not in catalog: errors.append(f"{rid}: from_source_id does not resolve")
        to=r.get("to") or {}; kind=to.get("kind"); target=to.get("id")
        if kind not in allowed: errors.append(f"{rid}: unsupported target kind {kind!r}")
        if not target: errors.append(f"{rid}: missing target id")
        if kind=="SOURCE" and target not in catalog: errors.append(f"{rid}: source target {target} does not resolve")
        if kind=="PROJECT" and target not in projects: errors.append(f"{rid}: project target {target} does not resolve")
        if r.get("confidence") not in {"CONFIRMED","STRONG","TENTATIVE","UNRESOLVED"}: errors.append(f"{rid}: invalid confidence")
        if not r.get("basis"): errors.append(f"{rid}: missing basis")
        if not r.get("support_refs"): errors.append(f"{rid}: missing support_refs")
    print(f"source relations: {len(rels)}")
    if errors:
        for e in errors: print(" - "+e,file=sys.stderr)
        return 1
    print("OK: BFDM source relation validation passed")
    return 0
if __name__=="__main__": raise SystemExit(main())
