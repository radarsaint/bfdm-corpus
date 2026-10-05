#!/usr/bin/env python3
"""Search Discord harvests through a hydrated SQLite file or the JSONL projection."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discord_index import RetrievalError, repo_root_from, search  # noqa: E402


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Search a Discord harvest without treating an LFS pointer as absence.")
    parser.add_argument("query")
    parser.add_argument("--repo", type=Path, default=None)
    parser.add_argument("--server", required=True, help="Slug, server name, or project id. Example: roanoke-s3")
    parser.add_argument("--channel")
    parser.add_argument("--author")
    parser.add_argument("--phrase", action="store_true")
    parser.add_argument("--attachments", action="store_true", dest="attachments_only")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--source", choices=("auto", "sqlite", "projection"), default="auto")
    parser.add_argument("--database", type=Path, default=None)
    args = parser.parse_args(argv)
    try:
        root = Path(args.repo).resolve() if args.repo else repo_root_from(Path.cwd())
        payload = search(
            root,
            args.query,
            server=args.server,
            channel=args.channel,
            author=args.author,
            phrase=args.phrase,
            attachments_only=args.attachments_only,
            limit=args.limit,
            full=args.full,
            source=args.source,
            database=args.database,
        )
    except RetrievalError as exc:
        json.dump({"error": exc.code, "message": str(exc)}, sys.stderr, ensure_ascii=False)
        sys.stderr.write("\n")
        return 2
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
