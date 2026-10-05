#!/usr/bin/env python3
"""Write Discord attachment metadata from a hydrated SQLite harvest.

Does not rewrite message shards and does not copy message text, CDN urls, or file bytes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discord_index import RetrievalError, export_attachments, repo_root_from  # noqa: E402


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Export attachment metadata for one Discord harvest.")
    parser.add_argument("database", type=Path)
    parser.add_argument("--server-slug", default=None)
    parser.add_argument("--repo", type=Path, default=None)
    args = parser.parse_args(argv)
    try:
        repo = Path(args.repo).resolve() if args.repo else repo_root_from(Path.cwd())
        manifest = export_attachments(args.database, repo, args.server_slug)
    except RetrievalError as exc:
        json.dump({"error": exc.code, "message": str(exc)}, sys.stderr, ensure_ascii=False)
        sys.stderr.write("\n")
        return 2
    json.dump(manifest, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
