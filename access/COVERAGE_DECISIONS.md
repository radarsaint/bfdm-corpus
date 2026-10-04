# Coverage decisions

Gemini's Corpus Accessibility Inventory was design input. It was not adopted as a second registry.

## Adopted

- A search result now carries `coverage_report.status`: `EXHAUSTIVE`, `PARTIAL`, `INACCESSIBLE`, or `UNKNOWN`.
- `zero_match_means_absence` is true only for `EXHAUSTIVE`. `absence_is_not_evidence` is the inverse.
- One family can be mixed. `drive_bcs_bodies` lists `body_present`, `catalog_only`, and `missing_target` separately. Reason codes attach only to the states that were not searched.
- Controlled reasons: `lfs_pointer_only`, `missing_readable_projection`, `external_auth`, `missing_target`, `intentionally_excluded`, `unmerged_workstream`.
- `python -m access audit` counts searchable records, catalog-only records, pointer databases versus databases with bytes, excluded files, and the open Discord-export and Drive-body gaps.

## Modified

- Statuses live on the existing `coverage.families` objects. There is no `bfdm_inventory.jsonl` and no per-source inventory id.
- `NOT_SEARCHED` and `EXCLUDED` sit beside the four required statuses. Exclusion is not the same thing as an unreadable file.
- `external_auth` is used only where a catalog row's body is absent and the catalog names an external locator. It is not applied to rows that already have a local body.
- `unmerged_workstream` names `ingest/discord-retrieval-v1` and `ingest/drive-project-v3`. This layer still does not do that work.

## Rejected

- A standalone JSONL inventory, stub generator, and 90-day verification clock. The access index and live coverage report already answer the operational question.
- `ERR_FMT_BINARY_DB`. SQLite is inaccessible here only while the file is an LFS pointer. If the bytes are present, coverage is `NOT_SEARCHED` and `query_path` is true.
- A file-size threshold for model readability, including the 400 KB cap this tool previously used when `--include-evaluation` or `--include-imported` was set. Text files are read. There is no byte cutoff.
- `ERR_EXTREME_SIZE`, `ERR_UNINDEXED_FRAGMENTS`, and `ERR_MISSING_PROVENANCE` as automatic failures. Provenance stays on record `cites`. Fragmented Discord text is the other branch's export, reported as `missing_readable_projection` plus `unmerged_workstream`.
- Accessibility profiles named `human_local` and `model_cloud`. The report instead says whether this checkout has bytes and whether this command searched them.
