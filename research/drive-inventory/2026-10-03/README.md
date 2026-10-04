# Google Drive discovery ledger — 2026-10-03

This ledger records Drive search hits that are not represented by a native Google Drive ID in `evidence/catalog.jsonl` at discovery time. A row is a candidate, not an attribution claim, corpus admission, or new BCS assignment.

## Search coverage

- `Roanoke`: 103 results across 2 page(s).
- `Empire City`: 77 results across 1 page(s).
- `Earthfall`: 2 results across 1 page(s).
- `Bastion Redoubt`: 8 results across 1 page(s).
- `At War's End`: 100 results across 2 page(s).

Unique Drive items seen: 224.
Already cataloged by native Drive ID: 66.
Uncataloged candidates recorded: 158.

## Admission rule

Before a candidate receives a BCS ID, verify source identity, campaign/project relationship, authorship/provenance boundaries, duplication/version-family relationships, and whether the item is first-party source material, collaborator context, third-party reference material, or irrelevant search noise.

Machine-readable candidates: `candidates.jsonl`.

## Admission progress

As of 2026-10-04, 8 of the 158 uncataloged candidates have been admitted and ingested as BCS-000069 through BCS-000076 after project-identity review. Admission remains source-by-source rather than title-only.

One exception is BCS-000076 (Public Lore Document.): its rich DOCX export is approximately 4.5 MB and repeatedly failed the connector's inline binary-transfer path. The corpus preserves the full current body, provider text export, comments, revision metadata, and native Drive identity; rich binary/asset mirroring remains explicitly pending.
