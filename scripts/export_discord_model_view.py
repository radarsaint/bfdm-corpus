#!/usr/bin/env python3
"""Export Discord SQLite harvests into GitHub/model-readable JSONL shards.

Canonical SQLite remains authoritative. These files are deterministic projections.
"""
from __future__ import annotations
import argparse, hashlib, json, sqlite3
from pathlib import Path

def rowdict(cur, row):
    return {d[0]: row[i] for i, d in enumerate(cur.description)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("database", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--max-messages", type=int, default=5000)
    args=ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    for p in args.out.glob("messages-*.jsonl"): p.unlink()

    con=sqlite3.connect(args.database)
    con.row_factory=sqlite3.Row
    tables={r[0] for r in con.execute("select name from sqlite_master where type='table'")}
    if "messages" not in tables:
        raise SystemExit("messages table not found")

    cols={r[1] for r in con.execute("pragma table_info(messages)")}
    preferred=["id","channel_id","author_id","author_name","author_display_name","timestamp","created_at","content","reply_to_message_id","thread_id"]
    selected=[c for c in preferred if c in cols]
    if "id" not in selected or "content" not in selected:
        raise SystemExit(f"messages table lacks required id/content columns; has {sorted(cols)}")

    order = "timestamp" if "timestamp" in cols else ("created_at" if "created_at" in cols else "id")
    sql=f"select {','.join(selected)} from messages order by {order}, id"
    count=0; shard=0; fh=None; shard_count=0; shard_meta=[]
    sha=hashlib.sha256()
    try:
        for row in con.execute(sql):
            if fh is None or shard_count >= args.max_messages:
                if fh:
                    fh.close()
                    shard_meta[-1]["messages"]=shard_count
                shard += 1; shard_count=0
                name=f"messages-{shard:04d}.jsonl"
                fh=(args.out/name).open("w",encoding="utf-8",newline="\n")
                shard_meta.append({"path":name,"messages":0})
            obj={k: row[k] for k in selected}
            line=json.dumps(obj,ensure_ascii=False,separators=(",",":"))+"\n"
            fh.write(line); sha.update(line.encode("utf-8"))
            count += 1; shard_count += 1
    finally:
        if fh:
            fh.close(); shard_meta[-1]["messages"]=shard_count
        con.close()

    manifest={
      "schema_version":1,
      "source_database":str(args.database).replace("\\","/"),
      "message_count":count,
      "messages_per_shard":args.max_messages,
      "projection_sha256":sha.hexdigest(),
      "shards":shard_meta,
      "note":"Generated projection. Canonical SQLite is authoritative."
    }
    (args.out/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(manifest,indent=2))

if __name__=="__main__": main()
