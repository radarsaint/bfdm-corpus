# Source Coverage

This file tracks source families relevant to the BFDM research program. It distinguishes canonical main, backlog, archive gaps, and evidence gaps. It is not a substitute for source metadata.

## LANDED ON MAIN

### Legacy 51-source staging body

The earlier 51-source staging body has been reconciled into the canonical source-history layer on `main` through the Drive-history integration merged in PR #25.

Original staging distribution:
- Roanoke: 37;
- Earthfall: 2;
- Bastion / Redoubt: 3;
- At War's End: 8;
- Exploration Impossible context: 1.

Historical staging/audit files remain under `research/legacy-staging/` for provenance. They should not be read as a current migration blocker.

The old Library staging archive is historical source material, not a second canonical corpus.

### Discord

Roanoke Season 3:
- `discord/roanoke-season-3/roanoke-season-3.sqlite`;
- 197,013 messages;
- 194 text channels;
- 1,421 attachments.

Empire City / Season 4:
- `discord/empire-city/empire-city.sqlite`;
- 189,761 messages;
- 247 text channels;
- 52 threads;
- 3,528 attachments.

Empire City Dev:
- canonical harvest and model-facing projection are registered.

Model-facing retrieval for the major harvested Discord archives is complete. See `MODEL_RETRIEVAL.md`.

### Drive/source-history families

Merged PR #25 provides a researchable historical layer rather than isolated Drive files.

It includes or orients, among other families:
- Roanoke S3 manuscript development;
- directory, timeline, maps, bestiary, public lore, crafting, ancestry/lore families;
- week-level operations, passdowns, set lists, and cited event modules;
- Empire City crafting, directory, backlog, player orientation, signup/operations, airship material, setting lore, and broadsheets;
- At War's End draft/revision families, outlines, cosmology, and writing-process material;
- Bastion/Redoubt and Earthfall source families where evidence supports placement;
- Season 5 Google Sites publication layer, changelog, and Way of Gun Fu Drive/publication relationship.

Important bounded live-contact examples include:
- Empire City Airship Qualification → live `#flight-school` exercise;
- Empire City crafting → approval-step live channel use;
- Roanoke crafting family → live contact/revision trajectory.

A scheduled/prepared event is not automatically marked as played.

### Season 5 / Legends

Canonical project: `roanoke-s5-legends`.

Landed publication/source coverage includes:
- 26 player-facing Google Sites namespaces;
- BCS `000087`–`000112`;
- `BCS-000113` Site changelog/revision bridge;
- `BCS-000114` Way of Gun Fu Drive source and publication relationship.

Publication does not establish live use.

## Readiness model

See `research/drive-integration/RESEARCH_READINESS_2026-10-05.md`.

`SOURCE_RESEARCH_READY` means the source/family is oriented enough for research: identity, placement or explicit unknown, production stage or explicit unknown, and live-use status/locator where established.

`LONGITUDINAL_RESEARCH_READY` currently establishes the presence of at least one qualifying trajectory edge: a revision relation or a bounded live-contact relation. It does not establish a complete longitudinal chain.

Therefore:
- readable/placed source ≠ longitudinal history;
- revision ≠ play;
- publication ≠ play;
- explicit live-use gap ≠ archive gap.

## IDENTIFIED BACKLOG — Drive candidates

The preserved candidate pool has been first-pass triaged:
`research/drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md`.

It contains significant real campaign material for selective later admission, including Ferrytown, Hampstead, Pigeon Lord, Mirabelle, Daysong, Rowing Oak, Arcanian material, and other named sources.

These are candidates, not BCS source containers.

Five candidates could not be read:
- three Drive 404s;
- one image-style PDF with no text layer;
- one DOCX connector read failure.

## EVIDENCE GAPS

Known evidence gaps include:
- live-play linkage for many otherwise source-ready families;
- Season 5 live play;
- Season 2 live play;
- Earthfall, Bastion/Redoubt, and At War's End live evidence sufficient for Phase 2A confirmation. Their existing texts can still support Phase 2B design-method claims. Those claims are not evidence the material was run;
- passage-level authorship for collaborative material where not established;
- broad non-Roanoke live coverage.

Do not fill evidence gaps from titles, folder placement, publication, or later recollection alone.

## ARCHIVE GAPS

Examples:
- the five triaged unreadable/unavailable Drive candidates;
- `BCS-000022` is a genuine blank source, not an extraction failure;
- the complete later Area 6c human-test transcript remains unrecovered.

A blank or missing artifact is not permission to invent its contents.

## Coverage principle

Do not infer importance from what is easiest to search.

S3/S4 currently provide unusually dense live evidence and therefore dominate early comparison work. This creates a format-concentration problem: both are large Roanoke-lineage multi-DM campaigns.

Phase 2A needs live-decision evidence and should seek a format other than S3/S4 when that evidence exists. Phase 2B may use Earthfall, Bastion/Redoubt, and At War's End now. A Discord zero for a phrase is absence from that searched projection, not historical nonexistence of a document that was only linked.
