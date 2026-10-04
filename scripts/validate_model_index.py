#!/usr/bin/env python3
"""Validate generated model-facing Discord projections against registry and manifests."""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT=Path("model-index/discord")
REG=Path("registry/discord_servers.jsonl")

def jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def fail(errors,msg):
    errors.append(msg)

def main():
    errors=[]
    servers=jsonl(REG)
    for server in servers:
        slug=server["server_slug"]
        expected=server.get("message_count")
        base=ROOT/slug
        mf=base/"manifest.json"
        if not mf.exists():
            fail(errors,f"{slug}: missing manifest")
            continue
        m=json.loads(mf.read_text(encoding="utf-8"))
        if expected is not None and m.get("message_count") != expected:
            fail(errors,f"{slug}: manifest message_count {m.get('message_count')} != registry {expected}")
        total=0
        shard_names=set()
        limit=(m.get("shard_limits") or {}).get("bytes")
        for item in m.get("files") or []:
            p=Path(item["path"])
            if not p.exists():
                fail(errors,f"{slug}: missing shard {p}")
                continue
            data=p.read_bytes()
            shard_names.add(p.name)
            total += item.get("messages",0)
            if item.get("bytes") != len(data):
                fail(errors,f"{slug}: byte count mismatch {p}")
            if item.get("sha256") != hashlib.sha256(data).hexdigest():
                fail(errors,f"{slug}: sha256 mismatch {p}")
            if limit and len(data) > limit:
                fail(errors,f"{slug}: shard exceeds byte limit {p}: {len(data)} > {limit}")
        if total != m.get("message_count"):
            fail(errors,f"{slug}: shard message total {total} != manifest {m.get('message_count')}")

        ti=m.get("term_index") or {}
        tdir=Path(ti.get("directory",""))
        if not tdir.exists():
            fail(errors,f"{slug}: missing term index directory")
            continue
        seen_terms=0
        for tf in tdir.glob("*.jsonl"):
            prefix=tf.stem
            for n,line in enumerate(tf.read_text(encoding="utf-8").splitlines(),1):
                if not line.strip():
                    continue
                try:
                    row=json.loads(line)
                except Exception as e:
                    fail(errors,f"{slug}: invalid term JSON {tf}:{n}: {e}")
                    continue
                seen_terms += 1
                token=row.get("token","")
                head=token[:3].ljust(3,"_")
                expected_prefix="".join(ch if ("a" <= ch <= "z" or "0" <= ch <= "9") else "_" for ch in head)
                if expected_prefix != prefix:
                    fail(errors,f"{slug}: term {token!r} routed to {prefix}, expected {expected_prefix}")
                for shard in row.get("shards") or []:
                    if shard not in shard_names:
                        fail(errors,f"{slug}: term {token!r} references missing shard {shard}")
        if seen_terms != ti.get("term_count"):
            fail(errors,f"{slug}: term count {seen_terms} != manifest {ti.get('term_count')}")
        print(f"OK {slug}: {m.get('message_count')} messages, {len(shard_names)} shards, {seen_terms} terms")
    for e in errors:
        print("ERROR",e)
    return 1 if errors else 0

if __name__=="__main__":
    sys.exit(main())
