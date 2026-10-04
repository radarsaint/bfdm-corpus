# Roanoke Season 5 / Legends — Google Sites archive

This directory preserves the known public Google Sites publication layer for `roanoke-s5-legends`.

## Capture

- 26 linked Google Sites namespaces are in the manifest.
- Canonical BCS IDs are `BCS-000087`–`BCS-000112`.
- 26/26 seed pages were fetched successfully on 2026-10-04.
- Fetch failures: 0.
- The final link-graph check found no Google Sites `/view/` namespaces linked by captured pages that were absent from the manifest.

Authoritative harvest report:

- `../../../ingest/reports/2026-10-04-season5-google-sites.md`
- `../../../ingest/reports/2026-10-04-season5-google-sites.json`

Manifest and reusable harvester:

- `../../../ingest/google_sites/season5_sites.json`
- `../../../ingest/google_sites/harvest_google_sites.py`

## Per-site layout

Each site directory contains:

- `raw/` — source-faithful HTTP HTML snapshot.
- `pages/` — normalized readable Markdown for search/research.
- `capture.json` — original harvester metadata: page URL, final URL, HTTP status, retrieval time, SHA-256 hashes, same-site links, outbound links, and exposed Google Drive/Docs links.
- `metadata.json` — canonical `bfdm_source_metadata/v1` BCS metadata used by the corpus ingestion/provenance layer.
- `README.md` — site-level capture summary.

The raw HTML is the preserved web-source snapshot. The Markdown mirror is a retrieval aid and must not silently replace the raw source when exact presentation or embedding matters.

## Evidence boundary

These pages establish **published/player-facing implementation state**. They do not prove that every published mechanic, class, race, item, rule, or story element was actually delivered or used during live Season 5 play.

Research should preserve the distinction:

`planned -> debated/revised -> published -> partially delivered -> observed in play`

## Known version/relationship issue

Two Monk URLs exist:

- `arcanianmonkoptions` — thin/stale shell containing the Way of Gun-Fu heading.
- `arcanian-monk-options` — linked from the Season 5 Character Creation page and containing the complete published Way of Gun Fu subclass.

A matching Drive PDF exists as a supporting/version-family source:

- `Subclass - Monk - The Way of Gun Fu - The Homebrewery.pdf`
- Drive ID `1qL8Q1E4gnDwlk37uOAXjk9A2cMEdHI6l`

Do not count the repeated content as independent corroboration without a separate evidentiary basis.

## Revision bridge

Google Drive also contains `S5 Site Changelog / To Change` (Drive ID `1Dk0JwcnTxVW41c1wHlnEoURrE2qkkEUBdMYQCSOUTuI`), a 2023-07-28 to 2023-07-31 revision document discussing proposed corrections, wording fixes, unresolved mechanics, and page-access state. It should be reconciled against these snapshots and the Season 5 development Discord.
