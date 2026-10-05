# Saturday D&D ChatGPT Project History — Ingest Batch 3

**Local date:** 2026-10-04  
**Repository date / UTC:** 2026-10-05  
**Project:** Saturday D&D  
**Branch:** `ingest/chatgpt-project-saturday-dnd-history`  
**Recovery status:** `PROJECT_HISTORY_RECOVERY_PARTIAL`

## Scope

Batch 3 preserves two June 2026 Project-history clusters:

- 2026-06-13 — Tasha / Iggwilv head-in-a-jar tarot development and subsequent prose-format correction;
- 2026-06-27 — House of Measured Coin / Tasha portfolio / vault-heist development.

## New source containers

- `BCS-000137` — June 13 Tasha tarot partial recovery
- `BCS-000138` — June 27 House of Measured Coin / portfolio-heist partial recovery note

## Provenance handling

`BCS-000137` preserves only the exact assistant fragments exposed by the historical-context recovery. The user’s tarot request and later rejection of staccato/short-line prose are retained as non-verbatim retrieval context because their exact bodies were not exposed.

`BCS-000138` intentionally contains no fabricated June 27 transcript turns. It preserves search-recovered chronology and topic context for the portfolio objective, House vault work, heist routes, Lord Caradoc Vell development, and weakened intellect devourer encounter.

AI-generated material remains `PROPOSED / DELIVERY_UNKNOWN` unless later evidence establishes selection or use.

## Asset references

- June 13 Project upload `file_00000000a3f471fd8a5515e0777e9be0` and adjacent generated-image records are referenced for provenance without being interpreted.
- June 27 Project upload `file_000000002b0071fd929fa5a1fde66ab7` (`5419.png`) is referenced by stable file ID only; no image content is inferred.

## Counts

- new BCS containers: 2
- BCS range: `BCS-000137`–`BCS-000138`
- total catalog rows after batch: 138
- manifest conversation clusters moved QUEUED → PARTIAL: 2
- binary assets copied: 0
- BCE records minted: 0
- Phase 2 claims minted: 0

## Source hashes

- `BCS-000137/source.md` — `f840ff2f50b144f4ee3652d14172f1f758e489ab33ea93778e0e53ece5457122`
- `BCS-000138/source.md` — `7da9676c593d267423cc73b1c74971b7a6b0ca23698f8ebdcd10a48af85082b9`

## Known limitations

- exact conversation titles and native message IDs remain unavailable;
- June 13 exposes only bounded exact assistant fragments;
- June 27 exposes no reliable verbatim chat-turn bodies in the current recovery;
- table delivery and implementation are not established;
- `indexes/documents.sqlite` has not been rebuilt in this connector-only environment.

## Validation boundary

Connector-level validation checks file presence, JSON/JSONL parsing, BCS uniqueness, manifest mappings, and branch diff shape.

Repository-local shell checks remain unclaimed:

- `python ingest/validate_ingest.py`;
- `python registry/validate_registry.py`;
- document-index rebuild / SQLite integrity / FTS checks.

No BCE, personality, training, precedent-card, or Phase 2 judgments were minted.
