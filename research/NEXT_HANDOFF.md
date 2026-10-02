# Next Handoff

**Status:** Points 1–3 completed on 2026-10-02.

## Point 1 — attributable retrospective/current-project evidence
Completed.

Key additions:
- `BCS-000068`
- `BCE-000005` through `BCE-000013`
- `BCR-000005` through `BCR-000013`
- archive-first directive preserved as `BCE-000013`

## Point 2 — Work GPT ingestion contract
Completed.

Binding files:
- `INGESTION_CONTRACT.md`
- `ingest/WORK_GPT_TASK.md`
- `ingest/document_archive_schema.sql`
- `ingest/source_metadata.schema.json`
- `ingest/ingest_report.schema.json`
- `ingest/validate_ingest.py`

## Point 3 — machine-readable campaign/project and identity registries
Completed.

Primary files:
- `registry/projects.jsonl`
- `registry/series.jsonl`
- `registry/project_relations.jsonl`
- `registry/people.jsonl`
- `registry/identities.jsonl`
- `registry/discord_servers.jsonl`
- schemas under `registry/*.schema.json`
- `registry/validate_registry.py`

Current counts:
- 11 projects
- 1 series
- 4 canonical people
- 3 identity assertions
- 2 harvested Discord servers

Important invariants:
- source-activity dates are distinct from live campaign windows;
- the Roanoke 30–100 concurrent-player retrospective range is series-level only, never a season count without season-specific evidence;
- early Roanoke remains pre-Season-2 / likely Season 1 lineage rather than being silently renamed Season 1;
- Season 5 / Legends retains its naming uncertainty;
- S3 Brendon identity is account-ID scoped;
- Empire City / Season 4 is harvested and linked to `roanoke-s4`, but Brendon's account mapping there remains unresolved;
- source anchors are project relationships, not passage-level authorship claims;
- developmental ordering is chronology, not a quality/importance score.

## Current working branch

`research/organize-current-work-v1`

Draft PR:
- #5 — organized BFDM research/evidence/ingestion governance

Do not merge without deliberate review.

## Next cleanup boundary

No Point 4 was defined in the prior handoff.

Before inventing a new numbered phase, perform a deliberate PR #5 consistency review against the archive-first invariant and current workstream ownership. Do not duplicate Work GPT's Drive ingestion or Grok's remaining Discord harvesting.

The preservation/research backlog remains in `research/HANDOFF_AND_BACKLOG.md`.
