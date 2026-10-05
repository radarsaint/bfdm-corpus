#!/usr/bin/env python3
"""Report mechanical integration problems. Does not edit source metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def prose_len(path: Path) -> int:
    if not path.is_file():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2]
    return len(text.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    records = {}
    for base in (repo / "sources", repo / "context"):
        for path in base.glob("**/metadata.json"):
            meta = json.loads(path.read_text(encoding="utf-8"))
            cid = meta.get("corpus_id")
            if isinstance(cid, str):
                records[cid] = meta
    catalog = {}
    for line in (repo / "evidence" / "catalog.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            catalog[row["corpus_id"]] = row
    findings = []
    for cid in sorted(set(catalog) - set(records)):
        findings.append(
            {
                "kind": "CATALOG_WITHOUT_CONTAINER",
                "corpus_id": cid,
                "detail": catalog[cid].get("title"),
            }
        )
    for cid in sorted(set(records) - set(catalog)):
        findings.append({"kind": "CONTAINER_WITHOUT_CATALOG", "corpus_id": cid, "detail": records[cid].get("title")})
    revision_pending = []
    for path in sorted((repo / "sources").glob("**/revisions.jsonl")):
        pending = 0
        total = 0
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            total += 1
            if item.get("body_fetched") is False:
                pending += 1
        if pending:
            revision_pending.append({"corpus_id": path.parent.name, "pending": pending, "rows": total})
    unreadable = []
    for cid, meta in sorted(records.items()):
        paths = []
        for rep in meta.get("representations") or []:
            rel = str(rep.get("path") or "")
            if rel.endswith((".md", ".txt")):
                paths.append(repo / rel)
        if not paths:
            paths = list((repo / "sources").glob(f"**/{cid}/source.md"))
            paths += list((repo / "context").glob(f"**/{cid}/source.md"))
        if not any(prose_len(path) >= 40 for path in paths):
            unreadable.append({"corpus_id": cid, "title": meta.get("title")})
    channel_only_live = []
    for cid, meta in sorted(records.items()):
        for link in meta.get("source_links") or []:
            if link.get("link_type") != "IMPLEMENTED_IN":
                continue
            locator = str(link.get("external_locator") or "")
            basis = str(link.get("basis") or "")
            if "/channel/" in locator and "message" not in basis.lower() and not any(ch.isdigit() for ch in basis):
                channel_only_live.append({"corpus_id": cid, "locator": locator})
    payload = {
        "catalog_without_container": [row for row in findings if row["kind"] == "CATALOG_WITHOUT_CONTAINER"],
        "container_without_catalog": [row for row in findings if row["kind"] == "CONTAINER_WITHOUT_CATALOG"],
        "unreadable_body": unreadable,
        "revision_bodies_pending": revision_pending,
        "revision_bodies_pending_count": sum(row["pending"] for row in revision_pending),
        "channel_live_links_without_a_digit_in_the_basis": channel_only_live,
    }
    if args.write:
        dest = repo / "research" / "substrate" / "integration_findings.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        f"catalog-only {len(payload['catalog_without_container'])} "
        f"unreadable {len(payload['unreadable_body'])} "
        f"revision-bodies-pending {payload['revision_bodies_pending_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
