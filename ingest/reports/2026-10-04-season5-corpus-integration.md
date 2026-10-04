# Season 5 corpus integration report

- Project: `roanoke-s5-legends`
- Google Sites canonically admitted: **26**
- Site BCS range: `BCS-000087`–`BCS-000112`
- Revision bridge: `BCS-000113`
- Gun-Fu Drive version-family source: `BCS-000114`
- IDs `BCS-000069`–`BCS-000086` deliberately reserved for records already allocated on `ingest/drive-project-v3`.

## Integration completed

The Season 5 Sites now participate in the same source-container/provenance model as the rest of BFDM: catalog IDs, source metadata, raw and normalized representations, project registry anchors, source coverage, chronology, and handoff state.

The old Google Sites scraper metadata is preserved as `capture.json`; canonical BCS metadata now occupies the standard `metadata.json` path.

Two Drive bridge sources were also admitted:
- `BCS-000113` — **S5 Site Changelog / To Change**
- `BCS-000114` — **Subclass - Monk - The Way of Gun Fu - The Homebrewery.pdf**

## Evidence boundary

Publication means a rule or design reached a player-facing state. It does not prove that it was used in live play or that the campaign completed the advertised schedule.

## Remaining gaps

- Season 5 dev Discord: scrape/ingest/registration still pending.
- `indexes/documents.sqlite`: repo-wide index remains pending; do not build a misleading S5-heavy partial index before the active Drive-ingest branch is consolidated.
- Original PDF bytes for `BCS-000114`: provider-side, pending binary-safe reconciliation.
- Passage-level authorship remains unresolved where source evidence does not establish it.
