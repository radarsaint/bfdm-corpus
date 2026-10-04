#!/usr/bin/env python3
"""Validate bfdm_inventory.jsonl and report accessibility failures."""
from __future__ import annotations
import argparse, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

VALID={"DIRECT","AWKWARD","OPAQUE","UNKNOWN"}

def tracked():
    p=subprocess.run(["git","ls-files"],check=True,text=True,capture_output=True)
    return set(p.stdout.splitlines())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--inventory",default="bfdm_inventory.jsonl")
    args=ap.parse_args(); paths=tracked(); rows=[]; errors=[]; warnings=[]
    for n,line in enumerate(Path(args.inventory).read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: r=json.loads(line)
        except Exception as e: errors.append(f"line {n}: invalid JSON: {e}"); continue
        rows.append(r)
    ids={r.get("id") for r in rows}
    for r in rows:
        rid=r.get("id","<missing-id>"); s=r.get("storage",{}); a=r.get("accessibility_profiles",{}); d=r.get("dependencies",{}); p=r.get("provenance",{})
        for key in ("human_local","model_cloud"):
            if a.get(key) not in VALID: errors.append(f"{rid}: invalid {key}={a.get(key)!r}")
        check=[s.get("repository_path"),*(s.get("generated_mirrors") or [])]
        for path in filter(None,check):
            if path not in paths and not any(x.startswith(path.rstrip("/")+"/") for x in paths):
                errors.append(f"{rid}: Path Resolution Error: {path}")
        if s.get("is_git_lfs") and a.get("model_cloud")=="DIRECT" and not s.get("generated_mirrors"):
            errors.append(f"{rid}: Silent LFS Trap")
        if a.get("model_cloud")=="OPAQUE" and not d.get("failure_reasons"):
            errors.append(f"{rid}: Opaque Paradox")
        for cited in p.get("cites_sources") or []:
            if cited not in ids: errors.append(f"{rid}: Dangling Reference: {cited}")
        if r.get("source_family") in {"Discord Harvests","Session Records"} and not s.get("date_coverage"):
            warnings.append(f"{rid}: Missing Chronology")
        if a.get("model_cloud")=="DIRECT" and (s.get("scale_bytes") or 0)>5_000_000:
            warnings.append(f"{rid}: Size Warning")
    for x in errors: print("ERROR",x)
    for x in warnings: print("WARN ",x)
    print(f"{len(rows)} records; {len(errors)} errors; {len(warnings)} warnings")
    return 1 if errors else 0
if __name__=="__main__": sys.exit(main())
