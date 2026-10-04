#!/usr/bin/env python3
"""Mark an exported Discord projection readable in the corpus inventory."""
import json, sys
from pathlib import Path
slug=sys.argv[1]
inv=Path("bfdm_inventory.jsonl")
rows=[json.loads(x) for x in inv.read_text(encoding="utf-8").splitlines() if x.strip()]
target=f"discord/{slug}/{slug}.sqlite"; mirror=f"model/discord/{slug}"
manifest=json.loads((Path(mirror)/"manifest.json").read_text(encoding="utf-8"))
for r in rows:
    if r.get("storage",{}).get("repository_path")==target:
        r["storage"]["generated_mirrors"]=[mirror]
        r["storage"]["scale_bytes"]=Path(target).stat().st_size
        r["accessibility_profiles"]["model_cloud"]="DIRECT"
        r["capabilities"]["text_searchable"]=True
        r["dependencies"]["access_mechanism"]="jsonl_mirror_fallback"
        r["dependencies"]["failure_reasons"]=["ERR_LFS_POINTER_ONLY","ERR_FMT_BINARY_DB"]
        r["dependencies"]["coverage_limitations"]="Canonical SQLite is LFS/binary; model access uses deterministic JSONL projection."
        r["audit"]["last_verified_at"]="2026-10-04T22:50:00Z"
        r["audit"]["notes"]=f"Projection contains {manifest['message_count']} messages in {len(manifest['shards'])} shards."
        break
else: raise SystemExit(f"inventory record not found for {target}")
inv.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in rows),encoding="utf-8")
