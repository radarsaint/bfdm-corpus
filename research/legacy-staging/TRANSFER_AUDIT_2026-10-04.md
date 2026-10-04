# Legacy staging archive audit — 2026-10-04

## Result

The exact Library staging archive has been recovered and independently audited:

- file: `brendon-corpus-staging.zip`
- size: 86,948,434 bytes
- SHA-256: `cebe18692ba3b8a2fe220d164cb722e18d81766edcc03f39ae0f18174350ea7a`
- manifest: `brendon-corpus/manifest.all.jsonl`
- manifest records: **51**
- manifest IDs: `BCS-000017`–`BCS-000058`, `BCS-000060`–`BCS-000067`, plus `BCS-000059` as Exploration Impossible context. The archive order places `BCS-000059` last; do not infer a missing or duplicate ID from ordering.

The prior handoff's **284 pending record files** count is reproduced directly from the archive.

## Exact bundle payload

Across the 51 source containers, the archive contains exactly:

| Kind | Files |
| --- | ---: |
| `source.md` normalized bodies | 51 |
| `metadata.json` | 51 |
| `comments.json` | 51 |
| `brendon-comments.native.json` | 5 |
| originals | 51 |
| assets | 75 |
| **Total** | **284** |

Total bytes inside the 51 canonical bundle directories: **88,791,012**.

Original representations are:
- 49 DOCX;
- 1 XLSX;
- 1 TXT.

Assets are:
- 39 JPG;
- 33 PNG;
- 3 GIF.

The normalized/human-readable bodies total 51 Markdown files. Five bundles preserve a separate Brendon-native-comment representation in addition to the bundle comment export.

## Integrity checks performed

The recovered archive was opened directly with Python's ZIP reader. For every manifest record:

1. the declared normalized body exists;
2. the declared original exists;
3. `metadata.json` exists;
4. `comments.json` exists;
5. every declared asset exists;
6. every declared `brendon_native_comments_file` exists;
7. the normalized body's SHA-256 matches `normalized_sha256`;
8. the original's SHA-256 matches `original_sha256`.

Result: **0 missing files and 0 declared-hash mismatches.**

This is stronger than the previous state, which knew the archive checksum and pending count but had not preserved an independent archive-only validation command in the repository.

## Project distribution

- Roanoke: 37 records
- At War's End: 8 records
- Bastion/Redoubt: 3 records
- Earthfall: 2 records
- Exploration Impossible: 1 context record

The Exploration Impossible manuscript remains under `context/exploration-impossible/BCS-000059`; do not silently promote it into Brendon-authored source material.

## Transfer state

The blocker is now narrowly defined.

The Work environment can materialize and verify the exact 86.9 MB archive, but its shell has:
- no authenticated Git credential helper;
- no `gh` client/auth session;
- no outbound DNS/network access.

The authenticated GitHub connector can create Git blobs, trees, commits, and refs, but it accepts blob content as UTF-8/base64 strings rather than a local file reference. That is practical for small text artifacts and impractical for the ~85 MB of DOCX/XLSX/image payload without an explicit binary file-reference upload action.

A connected Google Drive route was also inspected. Available sharing controls do not expose anonymous public sharing suitable for an unauthenticated GitHub Actions runner, so Drive is not being introduced as a brittle transport dependency.

This is a transport limitation only. Source identity, archive identity, bundle layout, checksums, and the exact 284-file import target are resolved.

## New reproducible audit

Use:

```bash
python ingest/audit_legacy_staging_archive.py \
  --archive /path/to/brendon-corpus-staging.zip \
  --output research/legacy-staging/transfer-manifest.jsonl \
  --summary research/legacy-staging/transfer-summary.json
```

The script fails on archive SHA mismatch, duplicate BCS IDs, missing mandatory bundle files, normalized hash mismatch, or original hash mismatch. It emits a file-level transfer manifest containing canonical path, kind, byte count, and SHA-256 for every bundle file.

## Definition-of-done impact

Point 4 remains **IN PROGRESS** until the 284 bundle files exist in canonical `sources/` / `context/` and a final reconciliation dry-run reports all 51 records `ALREADY_RECONCILED`.

Do not regress the status to “archive unavailable” or “source identification pending.” The exact archive is available and validated. The remaining issue is authenticated binary transport into Git history.
