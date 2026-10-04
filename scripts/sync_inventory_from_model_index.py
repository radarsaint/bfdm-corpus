#!/usr/bin/env python3
"""Synchronize Discord accessibility inventory rows from the canonical registry and model projections."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

INV=Path("bfdm_inventory.jsonl")
REG=Path("registry/discord_servers.jsonl")
ROOT=Path("model-index/discord")

def rows(path):
    if not path.exists(): return []
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def is_lfs_pointer(path: Path) -> bool:
    try:
        return path.read_bytes()[:128].startswith(b"version https://git-lfs.github.com/spec/v1")
    except OSError:
        return False

def main():
    existing=rows(INV)
    by_path={r.get("storage",{}).get("repository_path"):r for r in existing}
    other=[r for r in existing if r.get("source_family")!="Discord Harvests"]
    out=[]
    now=datetime.now(timezone.utc).isoformat().replace("+00:00","Z")
    for s in rows(REG):
        db=s["database_path"]; slug=s["server_slug"]; p=Path(db)
        prior=by_path.get(db,{})
        mirror_dir=ROOT/slug
        manifest=mirror_dir/"manifest.json"
        mirrored=manifest.exists() and any(mirror_dir.glob("messages-*.jsonl"))
        size=prior.get("storage",{}).get("scale_bytes",0)
        if p.exists() and not is_lfs_pointer(p):
            size=p.stat().st_size
        observed=s.get("observed_message_window") or {}
        first=observed.get("earliest"); last=observed.get("latest")
        coverage=f"{first}/{last}" if first and last else prior.get("storage",{}).get("date_coverage")
        rid=prior.get("id") or f"src_discord_{slug.replace('-','_')}_db"
        generated=[mirror_dir.as_posix()] if mirrored else []
        row={
            "id":rid,
            "name":prior.get("name") or s.get("corpus_name") or s.get("server_name") or slug,
            "campaign":prior.get("campaign") or ",".join(s.get("project_ids") or []),
            "source_family":"Discord Harvests",
            "source_class":"chat_log",
            "storage":{
                "repository_path":db,"raw_location":None,"generated_mirrors":generated,
                "format":"application/x-sqlite3","is_git_lfs":True,"scale_bytes":size,
                "date_coverage":coverage
            },
            "accessibility_profiles":{"human_local":"DIRECT","model_cloud":"AWKWARD" if mirrored else "OPAQUE"},
            "capabilities":{"text_searchable":mirrored,"structured_query":True,"context_retrieval":True,"stable_citation":True},
            "dependencies":{
                "access_mechanism":"jsonl_mirror_fallback" if mirrored else "sqlite3",
                "required_tools":[] if mirrored else ["sqlite3"],
                "failure_reasons":["ERR_LFS_POINTER_ONLY"] if mirrored else ["ERR_LFS_POINTER_ONLY","ERR_FMT_BINARY_DB","ERR_MISSING_MIRROR"],
                "coverage_limitations":("Canonical SQLite is LFS-backed; model retrieval uses generated JSONL shards." if mirrored else
                    "GitHub-connected model environments see only the Git LFS pointer until a generated text projection is committed.")
            },
            "provenance":prior.get("provenance") or {"has_provenance":True,"derived_artifacts":[],"cites_sources":[]},
            "audit":{"last_verified_at":now,"notes":prior.get("audit",{}).get("notes","")}
        }
        out.append(row)
    out.extend(other)
    INV.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in out),encoding="utf-8")
    print(f"inventory: synchronized {len(out)} records ({sum(1 for r in out if r.get('storage',{}).get('generated_mirrors'))} mirrored)")

if __name__=="__main__": main()
