# Next Handoff

**Status:** conversation rollover checkpoint.

## Completed in the previous conversation

### Point 1 — retrospective/current-project statements as attributable evidence
Completed.

Key additions:
- `BCS-000068` — curated verbatim ChatGPT project-conversation excerpt source
- `BCE-000005` through `BCE-000013`
- `BCR-000005` through `BCR-000013`
- explicit archive-first directive preserved as `BCE-000013`

### Archive-first invariant
Hardened across repository governance:

> `bfdm-corpus` is not primarily a training dataset. It is the durable research archive of Brendon's D&D creative history. Kit is one consumer of it.

### Point 2 — Work GPT ingestion contract
Completed.

Binding files:
- `INGESTION_CONTRACT.md`
- `ingest/WORK_GPT_TASK.md`
- `ingest/document_archive_schema.sql`
- `ingest/source_metadata.schema.json`
- `ingest/ingest_report.schema.json`
- `ingest/validate_ingest.py`

The contract requires legacy BCS reconciliation, native-ID deduplication, human-readable source containers, revision/comment preservation, one rebuildable non-Discord SQLite index, validation, and explicit ingest reporting.

## NEXT: Point 3

Build the **machine-readable campaign/project registry and identity registry**.

The prior diagnosis was:

> The chronology is human-readable, but campaign and identity structure are not yet properly machine-readable.

### Campaign/project registry should capture at minimum
- stable project/campaign ID
- canonical name
- aliases
- approximate dates
- exact live window when known
- format
- approximate player/concurrency scale
- synchronous/asynchronous
- single-DM/multi-DM
- primary Discord server IDs/slugs
- Drive/source-family relationships
- collaborators/staff
- source coverage status
- known uncertainties
- relationship to other campaigns/seasons
- research-era/developmental ordering

### Identity registry should capture at minimum
- canonical person ID
- canonical name
- platform
- account/user ID
- server/project ID
- username
- display name / nickname
- valid date range
- mapping basis
- confidence
- notes

Known confirmed Brendon S3 mapping:
- Brendon Faulkner
- Discord user ID `313689699627696139`
- username `bfdm`
- display name `DM radar`

Brendon has explicitly stated that his screen names change from season to season and that he is also DM radar. This is preserved as `BCE-000011`.

### Method requirement
The registries must preserve uncertainty. They must not invent exact dates, player counts, or identity mappings from filenames/nickname resemblance.

## Current working branch

`research/organize-current-work-v1`

Draft PR:
- #5 — organized BFDM research/evidence/ingestion governance

Do not merge without deliberate review.
