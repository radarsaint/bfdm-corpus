# Next Handoff

**Status:** Points 1–3 and 7 completed. Point 4 is next.

## Point 1 — retrospective/current-project statements as attributable evidence
**Status: completed.**

Key additions:
- `BCS-000068`;
- `BCE-000005` through `BCE-000013`;
- `BCR-000005` through `BCR-000013`;
- retrospective claims and current-project directives now have bounded attributable evidence rather than surviving only as research paraphrase.

This includes the preserved retrospective/self-report evidence for:
- emergent interpersonal / "dating sim" play;
- changing screen names across seasons;
- Brendon ↔ `DM radar`;
- Roanoke sometimes reaching roughly 30–100 concurrent players;
- desired future Kit/corpus roles;
- the archive-first corpus directive.

## Point 2 — precise Work GPT ingestion contract
**Status: completed.**

Binding files:
- `INGESTION_CONTRACT.md`;
- `ingest/WORK_GPT_TASK.md`;
- `ingest/document_archive_schema.sql`;
- `ingest/source_metadata.schema.json`;
- `ingest/ingest_report.schema.json`;
- `ingest/validate_ingest.py`.

The contract covers legacy BCS reuse, native-ID/hash deduplication, Drive IDs, checksums, revisions/comments, source-form separation, version families, collaborative-authorship safeguards, validation, and ingest reporting.

## Point 3 — machine-readable campaign/project and identity registries
**Status: completed.**

Primary files:
- `registry/projects.jsonl`;
- `registry/series.jsonl`;
- `registry/project_relations.jsonl`;
- `registry/people.jsonl`;
- `registry/identities.jsonl`;
- `registry/discord_servers.jsonl`;
- schemas under `registry/*.schema.json`;
- `registry/validate_registry.py`.

Current counts:
- 11 projects;
- 1 series;
- 4 project relations;
- 4 canonical people;
- 3 identity assertions;
- 2 harvested Discord servers.

Important invariants:
- source-activity dates remain distinct from live campaign windows;
- the retrospective Roanoke 30–100 concurrency range is series-level only;
- early Roanoke remains pre-Season-2 / likely Season 1 lineage rather than being silently renamed;
- Season 5 / Legends retains naming uncertainty;
- S3 Brendon identity is immutable-account-ID scoped;
- Empire City / Season 4 is harvested and linked to `roanoke-s4`; Brendon is now account-ID confirmed there as Discord user `313689699627696139`, username `bfdm`, display name `DM radar`;
- source anchors are project relationships, not passage-level authorship claims;
- developmental ordering is chronology, not a quality/importance score.

## Point 4 — reconcile the old 51-source staging body into canonical bfdm-corpus
**Status: IN PROGRESS — audit and migrator complete; binary-safe transfer pending.**

The 51-record legacy manifest is preserved, but the actual historical source containers/originals/assets remain incompletely reconciled with the canonical private repository.

Requirements:
- preserve every existing BCS ID;
- use `research/legacy-staging/manifest.all.jsonl` as the reconciliation map;
- reconcile originals, normalized/human-readable forms, assets, comments, and provenance where they exist;
- deduplicate against native Drive IDs/checksums rather than minting replacement source IDs;
- do not maintain the Library staging archive as a second canonical source store;
- produce an explicit reconciliation report showing migrated, already-present, duplicate, missing, and unresolved records.

The old Library staging archive remains a source for reconciliation, not a competing canonical corpus.

Current audited state:
- archive SHA-256: `cebe18692ba3b8a2fe220d164cb722e18d81766edcc03f39ae0f18174350ea7a`;
- 51/51 legacy IDs already exist in the evidence catalog;
- 0/51 actual source-container bodies are present in canonical `sources/` / `context/`;
- 284 record files remain pending;
- `ingest/reconcile_legacy_staging.py` is implemented and tested against the real archive;
- the remaining blocker is binary-safe transfer into authenticated Git/GitHub, not source identification or reconciliation logic.

Do not mark Point 4 complete until a final dry-run against the canonical checkout reports all 51 records `ALREADY_RECONCILED`.

## Point 5 — deliberate review and integration of PR #5
**Status: OPEN.**

Durable PR state:
- PR #5 is the integration PR for this research workspace;
- head branch: `research/organize-current-work-v1`;
- it must remain unmerged until deliberate review.

Do not store head SHA, commit count, or changed-file count here: committing this handoff changes those values. Query PR #5 live when beginning Point 5.

Do not blindly merge.

Before Work GPT begins a large ingest against main, review PR #5 for:
- archive-first consistency;
- stale status/provenance statements;
- schema/validator coherence;
- accidental derived-as-source promotion;
- private/public boundary problems;
- duplicated or superseded research files.

After deliberate review, integrate it so agents working only from `main` receive the corpus charter, ingestion contract, registries, methodology, research state, and hygiene rules.

## Point 6 — recover the later Area 6c human-test transcript
**Status: OPEN.**

Current preserved artifact:
- `research/kit-evaluation/playtest-02-followup-human-findings.md`

Current limitation:
- later human findings are preserved;
- one exact quote is retained;
- the complete verbatim test transcript has not been recovered into the workspace.

If recovered:
- archive the transcript separately as source/evaluation evidence;
- preserve timestamps/source locator;
- reconcile the current summary against the transcript;
- do not silently rewrite the historical summary.

## Point 7 — archive-first governing principle
**Status: completed and governing.**

> **bfdm-corpus is not primarily a training dataset. It is the durable research archive of Brendon's D&D creative history. Kit is one consumer of it.**

Preserved as `BCE-000013` and hardened into corpus governance.

Operational consequence:
- archive fidelity outranks current model convenience;
- model-facing/training/RAG/personality artifacts are downstream derivatives;
- a current Kit architecture never determines what historical material survives.

## Current working branch

`research/organize-current-work-v1`

Draft PR:
- #5 — Organize current BFDM research and Kit evaluation

Do not merge without deliberate review.
