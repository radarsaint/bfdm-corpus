#!/usr/bin/env python3
"""Search model-readable corpus projections and always report retrieval coverage."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--root",default="model-index/discord")
    ap.add_argument("--server",action="append",default=[])
    ap.add_argument("--limit",type=int,default=50)
    ap.add_argument("--context",type=int,default=2)
    args=ap.parse_args()
    root=Path(args.root); rx=re.compile(re.escape(args.query),re.I)
    dirs=[p for p in root.iterdir() if p.is_dir()] if root.exists() else []
    if args.server: dirs=[p for p in dirs if p.name in set(args.server)]
    matches=[]; searched=[]; omitted=[]
    for d in sorted(dirs):
        manifest=d/"manifest.json"
        shards=sorted(d.glob("messages-*.jsonl"))
        if not manifest.exists() or not shards:
            omitted.append({"family":f"Discord Harvests/{d.name}","reason":"ERR_MISSING_MIRROR","impact":"Projection manifest or message shards are missing."}); continue
        searched.append(f"Discord Harvests/{d.name}")
        rows=[]
        for shard in shards:
            for line in shard.read_text(encoding="utf-8").splitlines():
                if line.strip(): rows.append(json.loads(line))
        hit_idx=[i for i,r in enumerate(rows) if rx.search(r.get("content") or "")]
        for i in hit_idx[:max(0,args.limit-len(matches))]:
            lo=max(0,i-args.context); hi=min(len(rows),i+args.context+1)
            matches.append({"server":d.name,"match_message_id":rows[i]["id"],"context":rows[lo:hi]})
        if len(matches)>=args.limit: break
    status="EXHAUSTIVE" if searched and not omitted else ("PARTIAL" if searched else ("INACCESSIBLE" if omitted else "UNKNOWN"))
    report={"status":status,"searched_families":searched,"omitted_families":omitted,
            "zero_match_confidence":"HIGH" if status=="EXHAUSTIVE" else "LOW"}
    print(json.dumps({"query":args.query,"matches":matches,"coverage_report":report},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
