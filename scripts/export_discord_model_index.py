#!/usr/bin/env python3
"""Export a Discord SQLite harvest into model-readable JSONL plus deterministic term routing.

The SQLite database remains canonical. The projection is deterministic and rebuildable.
Message shards are byte-capped for direct retrieval. The term index lets a GitHub-connected
model route an exact term to the shard(s) containing it without depending on code search.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, sqlite3
from collections import Counter, defaultdict
from pathlib import Path

TOKEN_RE=re.compile(r"[A-Za-z0-9][A-Za-z0-9_'’-]{2,}")

def dump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def tokens(obj):
    values=(obj.get("content"),obj.get("display_name"),obj.get("username"),
            obj.get("channel"),obj.get("category"),obj.get("thread"))
    out=set()
    for value in values:
        if not value:
            continue
        for m in TOKEN_RE.finditer(str(value)):
            out.add(m.group(0).casefold().replace("’","'"))
    return out

def prefix_for(token):
    head=token[:3].ljust(3,"_")
    return "".join(ch if ("a" <= ch <= "z" or "0" <= ch <= "9") else "_" for ch in head)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("database")
    ap.add_argument("--out-root", default="model-index/discord")
    ap.add_argument("--shard-messages", type=int, default=500,
                    help="Maximum messages per shard")
    ap.add_argument("--shard-bytes", type=int, default=250_000,
                    help="Target maximum UTF-8 bytes per shard")
    args=ap.parse_args()
    db=Path(args.database)
    if args.shard_messages < 1 or args.shard_bytes < 1:
        ap.error("Shard limits must be positive")
    with db.open("rb") as source:
        if source.read(16) != b"SQLite format 3\x00":
            ap.error("Hydrated SQLite bytes are required; an LFS pointer cannot be exported")
    source_hash=hashlib.sha256(db.read_bytes()).hexdigest()
    slug=db.stem
    out=Path(args.out_root)/slug
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("messages-*.jsonl"):
        old.unlink()
    terms_dir=out/"terms"
    if terms_dir.exists():
        shutil.rmtree(terms_dir)
    terms_dir.mkdir()

    con=sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    con.row_factory=sqlite3.Row
    q="""SELECT m.id,m.created_at,m.edited_at,m.content,m.reply_to_id,
                m.channel_id,c.name channel,c.category,
                m.thread_id,t.name thread,
                m.author_id,u.username,u.display_name,u.is_bot
         FROM messages m
         JOIN channels c ON c.id=m.channel_id
         LEFT JOIN threads t ON t.id=m.thread_id
         LEFT JOIN users u ON u.id=m.author_id
         ORDER BY m.created_at,m.id"""
    cur=con.execute(q)
    files=[]; count=0; first=None; last=None
    fh=None; h=None; shard_bytes=0; shard_messages=0; shard_no=0
    term_shards=defaultdict(set)
    term_messages=Counter()

    def close_shard():
        nonlocal fh, h
        if fh:
            fh.close()
            files[-1]["sha256"]=h.hexdigest()
            fh=None
            h=None

    def open_shard():
        nonlocal fh, h, shard_bytes, shard_messages, shard_no
        shard_no += 1
        path=out/f"messages-{shard_no:04d}.jsonl"
        fh=path.open("w",encoding="utf-8",newline="\n")
        h=hashlib.sha256()
        shard_bytes=0
        shard_messages=0
        files.append({"path":path.as_posix(),"messages":0,"bytes":0,"sha256":None})

    try:
        for row in cur:
            obj=dict(row)
            line=(dump(obj)+"\n").encode("utf-8")
            if fh is None:
                open_shard()
            elif shard_messages >= args.shard_messages or (shard_bytes + len(line) > args.shard_bytes and shard_messages > 0):
                close_shard()
                open_shard()
            shard_name=Path(files[-1]["path"]).name
            fh.write(line.decode("utf-8"))
            h.update(line)
            shard_bytes += len(line)
            shard_messages += 1
            files[-1]["messages"] += 1
            files[-1]["bytes"] = shard_bytes
            for token in tokens(obj):
                term_shards[token].add(shard_name)
                term_messages[token] += 1
            first=first or obj["created_at"]
            last=obj["created_at"]
            count += 1
    finally:
        close_shard()
        con.close()

    buckets=defaultdict(list)
    for token in sorted(term_shards):
        buckets[prefix_for(token)].append({
            "token":token,
            "message_count":term_messages[token],
            "shards":sorted(term_shards[token])
        })
    term_files=[]
    for prefix, entries in sorted(buckets.items()):
        path=terms_dir/f"{prefix}.jsonl"
        data="".join(dump(entry)+"\n" for entry in entries)
        path.write_text(data,encoding="utf-8")
        term_files.append({"prefix":prefix,"path":path.as_posix(),"terms":len(entries),"bytes":len(data.encode("utf-8")),"sha256":hashlib.sha256(data.encode("utf-8")).hexdigest()})

    manifest={
        "schema_version":4,
        "source_database":db.as_posix(),
        "source_database_sha256":source_hash,
        "server_slug":slug,
        "message_count":count,
        "date_coverage":{"first":first,"last":last},
        "shard_limits":{"messages":args.shard_messages,"bytes":args.shard_bytes},
        "term_index":{
            "normalization":"casefold; curly apostrophe -> ASCII apostrophe; tokens are 3+ chars",
            "routing":"first 3 normalized token characters, non-[a-z0-9] replaced with _, padded with _",
            "directory":terms_dir.as_posix(),
            "term_count":len(term_shards),
            "file_count":len(term_files),
            "files":term_files
        },
        "files":files
    }
    if hashlib.sha256(db.read_bytes()).hexdigest() != source_hash:
        raise RuntimeError("Canonical SQLite changed during export; rerun the export")
    (out/"manifest.json").write_text(
        json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
        encoding="utf-8"
    )
    print(f"{slug}: {count} messages -> {len(files)} shards; {len(term_shards)} terms -> {len(term_files)} routing files")

if __name__=="__main__":
    main()
