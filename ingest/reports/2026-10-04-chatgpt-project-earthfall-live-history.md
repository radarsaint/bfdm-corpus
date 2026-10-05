# ChatGPT Project History Ingest — Earthfall:live

**Date:** 2026-10-04 (America/Los_Angeles)  
**Branch:** `ingest/chatgpt-project-earthfall-live-history`  
**Base:** `main@7e6b2dccf73efe70a01caf69ecd4a6e39e4c3f53`  
**Recovery class:** PROJECT_HISTORY_RECOVERY_PARTIAL

## Batch 1

Ingested:
- BCS-000131 — Area 16 Survival Challenge
- BCS-000132 — Polish Session Draft
- BCS-000133 — Game Tracking Update

The source bodies preserve Project-visible user-message excerpts in exposed order. Missing assistant messages and unavailable conversation IDs are recorded explicitly rather than inferred.

One Area 16 user message contains a detailed third-party personal profile. Because this repository is currently public, that profile is explicitly redacted from the public source snapshot rather than silently omitted; the surrounding message order is preserved.

## Inventory state

Discovered conversation units or bounded retrieval fragments: 20  
Ingested in Batch 1: 3  
Project-backed files discovered: 52  
Existing Earthfall canonical sources referenced: BCS-000054, BCS-000055

## Known gaps

- No complete Project export.
- Older Feb–May conversation raw transcripts unavailable through the current surface.
- Assistant-side transcript coverage is incomplete.
- Project-file duplicate identity requires evidence beyond matching filenames.
- `indexes/documents.sqlite` is not updated in this connector-only batch; human-readable Git source remains searchable, and this draft PR should not be treated as merge-ready until index policy is resolved.

## Research-layer restraint

No BCE records, personality conclusions, decision principles, precedent cards, or Phase 2 claims were created.

## Batch 2

Ingested:
- BCS-000134 — Build Earthfall App
- BCS-000135 — Build Fryvern Fight
- BCS-000136 — Dnd Arcade Consumables

This batch preserves the implementation/art workflow, Fryvern encounter-development corrections, explicit abandonment of the in-thread Fryvern art direction, Starcade power-up telegraphing, safe-room prep, and arcade consumable work.

Conversation-source count now ingested: 6.

## Batch 3

Ingested:
- BCS-000137 — Caribbean Pirate Theme
- BCS-000138 — Show Aggro Level 2 Art
- BCS-000139 — New chat / Floor 2 Aggro art example
- BCS-000140 — Plan Dead Turtle Transition
- BCS-000141 — Rod Voice Achievement Generator

This batch preserves Floor 2 pirate/Skullport direction, art-retrieval threads, the explicit immediate post-session judgment that the Fryvern fight “ended in fizzle” because the players were overpowered, the Nassau/Dead Turtle transition, and achievement/loot/player-created-skill work.

Conversation-source count now ingested: 11.

## Batch 4

Added:
- older-history recovery fragment log for nine February–May discovered conversation clusters whose raw transcripts are not exposed;
- Earthfall project-registry anchors for BCS-000131 through BCS-000141;
- explicit registry coverage state for partial ChatGPT Project history and the 52 discovered Project-backed files.

No new BCS IDs were minted for retrieval-summary-only fragments.

## Validation before PR

Connector-visible checks:
- current `main` remains `7e6b2dccf73efe70a01caf69ecd4a6e39e4c3f53`;
- branch is ahead of `main` and not behind;
- `evidence/catalog.jsonl` parses successfully;
- no duplicate BCS IDs were found;
- highest BCS is `BCS-000141`;
- all 11 new metadata files parse, match their BCS IDs, contain the validator-required metadata keys, and have nonempty locator arrays;
- `registry/projects.jsonl` parses and Earthfall contains 11 new ChatGPT-history anchors;
- manifest counts: 20 discovered units/fragments, 11 INGESTED, 9 PARTIAL raw-transcript gaps, 52 Project-backed files.

Local validator limitation:
- the shell runtime could not resolve `github.com`, so it could not clone this branch and run `python ingest/validate_ingest.py`;
- `indexes/documents.sqlite` was not modified in this connector-only pass;
- therefore the PR should remain unmerged until normal repo-side validation/index policy is completed.

## Pull request

Draft PR: https://github.com/radarsaint/bfdm-corpus/pull/32

The PR is intentionally unmerged.
