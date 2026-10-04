# Source Coverage

This file tracks known corpus coverage relevant to the research program. It is not a substitute for the source manifest.

## Earlier normalized/staged body

Before the S3 Discord harvest, the working corpus staging contained **51 normalized source containers**:

- Roanoke: 37
- Earthfall: 2
- Bastion / Redoubt: 3
- At War's End: 8
- Exploration Impossible context: 1

The staging status records:
- 75 embedded assets;
- 62 export comments;
- 17 native Brendon comment supplements.

Those 17 supplements are a staging metric, **not the total known Brendon-comment corpus**.

Later `dnd-solo` attribution work (merged PR #40) identified **78 attributable Brendon editorial comments** on Michael Kennish's *Exploration Impossible* while keeping the manuscript itself third-party/context-only. The older staging bundle did not exhaustively mirror all native Drive comments/replies.

The prior consolidated staging archive was maintained in the ChatGPT Library as:

`/Brendon Corpus Staging/Current/brendon-corpus-staging.zip`

This staging body should eventually be reconciled/migrated into the canonical private repository rather than maintained as a parallel corpus.

## Canonical private repository

`radarsaint/bfdm-corpus`

Current known major source families include:
- Discord server harvests under `discord/`;
- campaign planning under `campaigns/`;
- derived research on draft/research branches.

## Roanoke Season 3 Discord

`discord/roanoke-season-3/roanoke-season-3.sqlite`

Known harvest:
- 197,013 messages;
- 194 text channels;
- 1,421 attachments captured;
- time window 2020-07-18 through 2020-08-22.

## Roanoke Season 4 / Empire City Discord

`discord/empire-city/empire-city.sqlite`

Known harvest:
- server ID `850779382791536640`;
- 189,761 messages;
- 247 text channels;
- 52 threads;
- 3,528 attachments captured;
- observed message range 2021-06-05 through 2026-10-01.

The server explicitly identifies the campaign as **Season 4, Empire City**. The observed server range is not treated as the campaign live window. Brendon's account mapping is now confirmed from the server users table by immutable Discord user ID `313689699627696139`.

## Roanoke Season 5 / Legends — Drive + Google Sites

Canonical project: `roanoke-s5-legends`.

The player-facing Google Sites publication layer is now canonically admitted rather than preserved only as a source lead:

- 26 linked Google Sites namespaces captured;
- 26/26 seed pages fetched successfully;
- zero fetch failures in the final harvest;
- raw HTML and normalized readable Markdown retained for every site;
- BCS range `BCS-000087`–`BCS-000112` assigned to the 26 published Sites;
- `BCS-000113` preserves **S5 Site Changelog / To Change**, the July 2023 revision/proofing bridge;
- `BCS-000114` preserves the readable Drive extraction of **Subclass - Monk - The Way of Gun Fu - The Homebrewery.pdf** and links it to the published Monk version family.

The published landing page states that signups were limited to 30 spots, servers opened July 28, and advertised game dates ran July 30 through August 19. The page itself does not state the year; the 2023 year is a strong chronology inference from the contemporaneous July 2023 Site changelog and Season 5 planning cluster.

This source family provides strong evidence for **published/player-facing implementation state**. It does not establish that every published rule was used, or that the campaign completed its advertised schedule.

Season 5 development Discord coverage remains pending canonical ingest/registration.


## Google Drive / project corpus

Connected Drive contains a much broader creative record than S3 alone, including:
- campaign planning;
- custom races/classes/subclasses;
- worldbuilding and lore;
- adventure drafts;
- change logs;
- revision histories;
- homebrew mechanics;
- writing;
- unusual format experiments.

Full repository ingestion is still pending/in progress.

## S3 normalization / reconciliation status

The legacy staging manifest confirms the week documents used by the revision-family pass already have formal source containers:

- `BCS-000029` — Roanoke S3 v2 W2 Breakdown;
- `BCS-000037` — Roanoke s3w4 Break down.

Other confirmed mappings:
- `BCS-000045` — Roanoke Season 3 Rough Draft;
- `BCS-000046` — Roanoke Season3 Change Log;
- `BCS-000048` — RoanokeS3 doc V2 W1;
- `BCS-000052` — RoanokeS3W3 Breakdown;
- `BCS-000053` — RoanokeS3W5 Break Down.

The gap is now **repository reconciliation**: ensure the older staged containers and their originals/assets/comments are represented in canonical `bfdm-corpus` without changing their BCS IDs.

## Other Discords

S3 and Empire City / Season 4 are harvested. Remaining game servers still need harvesting. Until broader live coverage is present, cross-season conclusions should remain provisional.

## Coverage principle

Do not infer importance from what is easiest to search.

S3 remains unusually dense and methodologically mature, while Empire City now provides a second large live/server archive. Evidence density still must not be mistaken for importance. Later work—especially Earthfall—may be more representative of Brendon's current practice despite having fewer normalized records at present.
