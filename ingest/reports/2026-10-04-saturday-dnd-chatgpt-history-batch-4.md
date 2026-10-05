# Saturday D&D ChatGPT Project History — Ingest Batch 4

**Local date:** 2026-10-04  
**Repository date / UTC:** 2026-10-05  
**Project:** Saturday D&D  
**Branch:** `ingest/chatgpt-project-saturday-dnd-history`  
**Recovery status:** `PROJECT_HISTORY_RECOVERY_PARTIAL`

## Scope

Batch 4 preserves the 2026-07-11 Evernight House of the Measuring Coin dungeon-development cluster.

## New source container

- `BCS-000139` — July 11 House of the Measuring Coin partial conversation-and-artifact recovery.

## Preserved corrections and state

The source preserves bounded exact user fragments correcting the House name and rejecting vibe-writing, while keeping the remainder of the July 11 state as explicitly nonverbatim search-recovered context.

Recovered state includes:
- party already in the Evernight foyer;
- intellect devourer attack already happened there;
- House is not Raven Queen property;
- House protects deposited memories against alteration/loss/theft/collection, including Raven Queen collection;
- existing PCs had already deposited memories;
- new PC was being introduced;
- Tasha’s portfolio remained in the Material Plane House;
- Evernight objective was to discover the correspondence mechanism;
- existing-map / top-down / 5-foot-grid / non-isometric production corrections.

No later summary detail was silently promoted into timestamped transcript.

## Artifact references

Two July 11 Project files were matched to persistent Library titles by exact file ID:

- `file_00000000829c71f89b8dce60e3e86fbd` → `The house of the measuring coin.png`
  - Library ID: `libfile_b6972b6dde488191b90c7b13605beef3`
- `file_00000000e0b471fd90f2f25591422e9c` → `Arcane temple dungeon map.png`
  - Library ID: `libfile_c79a19fae4c08191b369b0550c4cd965`

The first artifact exposes the text “Tasha’s portfolio should be here. It is not.” This is preserved as artifact text, not proof of table delivery.

## Counts

- new BCS containers: 1
- highest BCS after batch: `BCS-000139`
- total catalog rows after batch: 139
- manifest conversation clusters moved QUEUED → PARTIAL: 1
- Project file records enriched with recovered Library aliases: 2
- binary assets copied: 0
- BCE records minted: 0
- Phase 2 claims minted: 0

## Source hash

- `BCS-000139/source.md` — `faf90ddf307773718639b454ba229594838330b669e0654f23740d7a00fff54c`

## Known limitations

- exact native conversation title and message IDs remain unavailable;
- most July 11 turn bodies are search-recovered context rather than exact transcript;
- the two image artifacts are referenced and textually described but not copied into GitHub in this connector-only batch;
- table delivery / final selection is not established;
- repository-local source-index rebuild and validators remain unrun.

## Validation boundary

Connector-level validation checks source/metadata presence, JSON/JSONL parsing, BCS uniqueness, manifest relation, and branch diff shape.

Not claimed:
- `python ingest/validate_ingest.py`;
- `python registry/validate_registry.py`;
- `indexes/documents.sqlite` rebuild / integrity / FTS checks.

No BCE, personality, training, precedent-card, or Phase 2 judgments were minted.
