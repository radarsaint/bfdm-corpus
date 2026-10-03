# Document / Project Ingestion

Work GPT's executable assignment is:

- [WORK_GPT_TASK.md](WORK_GPT_TASK.md)

Binding rules:

- [../INGESTION_CONTRACT.md](../INGESTION_CONTRACT.md)

Schemas:

- [document_archive_schema.sql](document_archive_schema.sql) — SQLite document index
- [source_metadata.schema.json](source_metadata.schema.json) — per-BCS metadata
- [ingest_report.schema.json](ingest_report.schema.json) — machine-readable run report

The non-Discord document index lives at:

- `indexes/documents.sqlite`

Human-readable source containers remain outside the database under `sources/` or `context/`.

The database is a searchable representation, not the sole archive.

## Current Work GPT instruction

If PR #5 has not yet merged, base `ingest/drive-project-v1` on `research/organize-current-work-v1`.

If PR #5 has merged, base it on current `main`.

Before writing, reconcile existing BCS IDs against both:
- `evidence/catalog.jsonl`
- `research/legacy-staging/manifest.all.jsonl`

For the 51-source legacy staging body, use:
- `reconcile_legacy_staging.py`
- `../research/legacy-staging/RECONCILIATION_2026-10-02.md`

Do not begin overlapping mass ingestion while those source bodies remain only in the Library staging ZIP.

Do not mint BCE or Kit personality/training conclusions during source ingestion.
