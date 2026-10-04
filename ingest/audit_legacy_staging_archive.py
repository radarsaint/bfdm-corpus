#!/usr/bin/env python3
"""Audit the legacy 51-source staging archive without requiring a repository checkout.

This validates archive identity, bundle completeness, per-source declared hashes, and emits
an exact file-transfer manifest for the canonical BCS containers.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import sys
import zipfile

EXPECTED_ARCHIVE_SHA256 = "cebe18692ba3b8a2fe220d164cb722e18d81766edcc03f39ae0f18174350ea7a"
MANIFEST_PATH = "brendon-corpus/manifest.all.jsonl"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", required=True)
    ap.add_argument("--output", default="research/legacy-staging/transfer-manifest.jsonl")
    ap.add_argument("--summary", default=None)
    ap.add_argument("--allow-unexpected-archive-sha", action="store_true")
    args = ap.parse_args()

    archive = pathlib.Path(args.archive)
    archive_sha = sha256(archive.read_bytes())
    errors: list[str] = []
    if archive_sha != EXPECTED_ARCHIVE_SHA256 and not args.allow_unexpected_archive_sha:
        errors.append(
            f"archive sha256 {archive_sha} != expected {EXPECTED_ARCHIVE_SHA256}"
        )

    rows: list[dict] = []
    projects = collections.Counter()
    kinds = collections.Counter()
    extensions = collections.Counter()
    total_bytes = 0

    with zipfile.ZipFile(archive) as zf:
        names = {i.filename for i in zf.infolist() if not i.is_dir()}
        if MANIFEST_PATH not in names:
            errors.append(f"missing {MANIFEST_PATH}")
            records = []
        else:
            records = [
                json.loads(line)
                for line in zf.read(MANIFEST_PATH).decode("utf-8").splitlines()
                if line.strip()
            ]

        if len(records) != 51:
            errors.append(f"manifest record count {len(records)} != 51")

        ids = [r.get("corpus_id") for r in records]
        if len(ids) != len(set(ids)):
            errors.append("duplicate corpus_id in manifest")

        for record in records:
            cid = record["corpus_id"]
            projects[record.get("project") or "UNKNOWN"] += 1
            bundle = record["_bundle_path"].rstrip("/")
            prefix = f"brendon-corpus/{bundle}/"
            bundle_names = sorted(n for n in names if n.startswith(prefix))
            rels = [n[len(prefix):] for n in bundle_names]

            mandatory = {
                "source.md",
                "metadata.json",
                "comments.json",
                record["original_stored_as"],
                *record.get("assets", []),
            }
            native_comments = record.get("brendon_native_comments_file")
            if native_comments:
                mandatory.add(native_comments)

            for rel in sorted(mandatory):
                full = prefix + rel
                if full not in names:
                    errors.append(f"{cid}: missing {rel}")
                    continue
                data = zf.read(full)
                if rel == record.get("normalized_file"):
                    got = sha256(data)
                    if got != record.get("normalized_sha256"):
                        errors.append(
                            f"{cid}: normalized hash {got} != {record.get('normalized_sha256')}"
                        )
                if rel == record.get("original_stored_as"):
                    got = sha256(data)
                    if got != record.get("original_sha256"):
                        errors.append(
                            f"{cid}: original hash {got} != {record.get('original_sha256')}"
                        )

            # Every file physically inside the source bundle is canonical reconciliation payload.
            for rel in rels:
                data = zf.read(prefix + rel)
                suffix = pathlib.PurePosixPath(rel).suffix.lower() or "<none>"
                if rel == "source.md":
                    kind = "normalized_source"
                elif rel == "metadata.json":
                    kind = "metadata"
                elif rel == "comments.json":
                    kind = "comments"
                elif rel == native_comments:
                    kind = "brendon_native_comments"
                elif rel.startswith("original/"):
                    kind = "original"
                elif rel.startswith("assets/"):
                    kind = "asset"
                else:
                    kind = "other_bundle_file"
                rows.append(
                    {
                        "corpus_id": cid,
                        "project": record.get("project"),
                        "path": f"{bundle}/{rel}",
                        "relative_path": rel,
                        "kind": kind,
                        "size_bytes": len(data),
                        "sha256": sha256(data),
                    }
                )
                kinds[kind] += 1
                extensions[suffix] += 1
                total_bytes += len(data)

    output = pathlib.Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in rows),
        encoding="utf-8",
    )

    summary = {
        "archive": str(archive),
        "archive_sha256": archive_sha,
        "expected_archive_sha256": EXPECTED_ARCHIVE_SHA256,
        "record_count": len(records),
        "bundle_file_count": len(rows),
        "bundle_bytes": total_bytes,
        "projects": dict(sorted(projects.items())),
        "kinds": dict(sorted(kinds.items())),
        "extensions": dict(sorted(extensions.items())),
        "transfer_manifest": str(output),
        "transfer_manifest_sha256": sha256(output.read_bytes()),
        "errors": errors,
    }

    if args.summary:
        sp = pathlib.Path(args.summary)
        sp.parent.mkdir(parents=True, exist_ok=True)
        sp.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
