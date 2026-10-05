# Saturday D&D ChatGPT Project History Ingest Report

**Date:** 2026-10-05  
**Project:** Saturday D&D  
**Branch:** `ingest/chatgpt-project-saturday-dnd-history`  
**Base branch:** `main`  
**Base SHA inspected before branch creation:** `7e6b2dccf73efe70a01caf69ecd4a6e39e4c3f53`  
**Recovery status:** `PROJECT_HISTORY_RECOVERY_PARTIAL`

## Scope

This ingest preserves accessible Saturday D&D ChatGPT Project history as a distinct `CONTEMPORANEOUS_DM_WORKBENCH` source family.

It does **not** claim a complete ChatGPT export. The current Project/history surface is search-based for historical conversations and does not expose an exhaustive conversation list, exact native titles for the recovered clusters, or stable native message IDs.

## Source surfaces searched

- current ChatGPT Project conversation/history context;
- historical conversation-context retrieval;
- current Project file/asset surface;
- canonical `radarsaint/bfdm-corpus` `main` for deduplication and conventions.

## Batch 1

Conversation material:
- May 28–31, 2026 Neverwinter / House of Measured Coin / Warehouse 9 / “The Witch in the Jar” / “The Knife Through Evernight” / “The Wrong Crate” cluster.

New source container:
- `BCS-000131` — partial ChatGPT project-conversation recovery.

Manifest:
- 11 currently discovered conversation clusters;
- 41 current Project file/asset records;
- conversation clusters not yet source-containerized remain `QUEUED`;
- current ingestion-directive attachment is inventoried as `OUT_OF_SCOPE` for campaign-history source ingestion.

## Counts

- candidate conversation clusters discovered: 11
- current Project file/asset records inventoried: 41
- new BCS containers: 1
- reconciled/reused BCS containers: 0
- possible duplicates: 0 currently identified
- clearly unrelated/current-ingest-directive files excluded from campaign source ingestion: 1
- comments captured: 0
- revision metadata rows captured: 0
- revision bodies captured: 0
- binary assets copied into repo in this batch: 0
- highest BCS allocated: `BCS-000131`

## Provenance / authorship handling

The conversation source is mixed-speaker material. User and assistant roles remain distinct where exact excerpts are available.

Assistant-generated material is not treated as user authorship, acceptance, selection, implementation, or table delivery. Search summaries are segregated from verbatim excerpts and labeled as non-transcript retrieval context.

No BCE records, personality conclusions, training examples, precedent cards, or Phase 2 decision claims were minted.

## Validation completed in this environment

- inspected current `main` before branch creation;
- confirmed highest pre-ingest BCS was `BCS-000130`;
- confirmed no existing Saturday D&D / Neverwinter-Evernight / House of Measured Coin source match in the canonical catalog;
- confirmed `saturday-dnd` did not already exist in `registry/projects.jsonl`;
- source normalized SHA-256 recorded for `BCS-000131/source.md`: `0d001bb58c46f39cdcf311a1538bdf7b316ff16dcf0f9f86cc56ead629aa5abb`;
- project-history manifest records the current access limitation explicitly.

## Validation still required before merge

The GitHub connector does not provide a checked-out repository shell in this chat. Therefore the following repository-local acceptance checks are **not yet claimed complete**:

- `python ingest/validate_ingest.py`;
- `python registry/validate_registry.py`;
- rebuild/update and integrity checks for `indexes/documents.sqlite`;
- any repository-local checks that depend on the full working tree.

These are merge-readiness gaps, not silently passed checks.

## Known gaps

- no exhaustive native conversation enumeration;
- no stable native ChatGPT message IDs;
- exact conversation titles unavailable for all currently recovered Saturday D&D clusters;
- most May 28–31 message bodies are only partially exposed;
- additional discovered Saturday D&D clusters remain queued;
- Project binary/generated assets are inventoried but not yet copied or related to source units;
- source index SQLite has not yet been rebuilt for the new container.

## Explicit boundary

This ingest is source preservation. It does not perform Phase 2 research, extract principles, train Kit, or generalize about Brendon’s DM judgment.
