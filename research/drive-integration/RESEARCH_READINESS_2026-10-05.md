# Drive history integration — research readiness, 2026-10-05

This pass ports the Drive donor containers onto current `main` and records relationships a researcher would otherwise rebuild from titles and prose. It does not start decision-case research.

Canonical relationship home remains each source `metadata.json`. The machine rollup is [RESEARCH_READINESS_2026-10-05.json](RESEARCH_READINESS_2026-10-05.json).

## What landed

Donor containers from `ingest/drive-project-v3` are now in this branch, including readable bodies, Drive IDs where the donor had them, export snapshots, comments, and revision metadata. Source prose was not summarized.

Seven donor IDs collided with Season 5 sources already on `main` and were remapped. Season 5 IDs were not renumbered.

| Donor ID | Canonical ID | Title |
| --- | --- | --- |
| BCS-000087 | BCS-000115 | Timeline disambiguation |
| BCS-000088 | BCS-000116 | RS3 Public docs copy editing |
| BCS-000089 | BCS-000117 | Island games draft |
| BCS-000090 | BCS-000118 | Golden Dawn quest arc |
| BCS-000091 | BCS-000119 | The Halfwudgie Verbatim |
| BCS-000092 | BCS-000120 | The Urucokra Verbatim |
| BCS-000093 | BCS-000121 | The Jackalope Verbatim |

The 2026-10-03 Drive discovery ledger is preserved at `research/drive-inventory/2026-10-03/`. It still lists 134 `UNREVIEWED_CANDIDATE` rows. Those are not sources yet.

## Status counts

Across 120 source containers:

| Status | Containers | Meaning |
| --- | --- | --- |
| `CROSS_MEDIUM_LINKED` | 7 | Project, family, and a dev/public, publication, or live-evidence link |
| `FAMILY_LINKED` | 84 | Project and family or version links; live use not claimed |
| `PLACED` | 25 | Exact project, mostly Season 5 published Sites |
| `ARCHIVED_ONLY` | 4 | Preserved, season not established |

`FAMILY_LINKED` includes BCS-000020 and BCS-000080. They sit in `roanoke-crafting-system` with no season assignment.

## Families

### Roanoke crafting — ready for the next pass on this system

`BCS-000077` dev doc, `BCS-000079` working copy, and `BCS-000078` public doc belong to `roanoke-s3`. `BCS-000077` is the dev/public pair of `BCS-000078`. `BCS-000079` remains the working companion. `BCS-000080` (2019, "another attempt") is a predecessor of the dev doc and is not assigned a season.

Live use is message-level. The August 1, 2020 announcements post (`739137088594772031`) opens Crafting with Class, and `crafting-questions` (`739240413269065890`) applies the 1,000 gp and labor costs.

`BCS-000020` is an earlier or alternate Roanoke crafting draft (one roll per day, harvester/crafter jobs). It is in the same family and has no season and no order against the others.

Season 4 crafting (`BCS-000001`) is a different essence economy. Nothing in that document cites Crafting with Class, so there is no derivation link.

### Roanoke Season 3 manuscript — prep chain is usable; scene-level live use is not

`BCS-000043` brainstorm → `BCS-000045` rough draft → `BCS-000041` S:3 2.0. `BCS-000046` revises that manuscript and is not treated as replacing it. `BCS-000084` is the week-compiled manuscript, companion to the Week 1 breakdown.

The Season 3 lore index (`BCS-000044`) points at the player backgrounds (`BCS-000085`), the public lore (`BCS-000076`), and the Uru/Halfwudgie lore (`BCS-000086`) by Drive id. Chinnokin (`BCS-000023`) and secret-society lore (`BCS-000027`) are linked from titles, because those legacy containers did not keep Drive ids.

Public lore is player-facing. Empire City's Red Coats document (`BCS-000075`) reuses that cosmology and says this season is the war, after earlier coming-to-America seasons.

Map key `BCS-000081` matches the S3 main map `BCS-000026`. Cryptid guide `BCS-000082` and index `BCS-000083` are one bestiary family. The Morkoth running guide (`BCS-000074`) accompanies the Week 5 Morkoth Lodestone event. The island-games draft (`BCS-000117`) accompanies the Week 4 Lake of the Woes set list.

Week schedules, set lists, casts, passdowns, and the S3 directory are `roanoke-s3-live-operations`. They are campaign machinery. They are not records of what players did.

### Empire City / Season 4 — one module is prep-to-play; the newspaper is not

Planning documents that say Season 4 or Empire City are `roanoke-s4`: the directory, backlog, intro script, signup sheet, and crafting rules. Broad `Empire City` labels on those containers were narrowed only where the text supports it.

`BCS-000073` Airship Qualification is implemented in live `flight-school` (`852796918836232192`). Sgt Manley runs on-the-job training there, and the scene uses the module's Pilot, Gunner, Mechanic, and Captain roles. The module's balloon drill is not what that scene runs.

`BCS-000005` through `BCS-000015` are Empire City Post issues in masthead order. Headline search did not show those issues posted in the harvest, so they stay prepared documents.

Dev Discord discusses Redcoats in August 2020, before the January 2021 Red Coats lore doc. That talk is not linked as discussion of `BCS-000075`.

### Season 5 — publication chain is usable; live play is absent

Published Google Sites are `PUBLIC_PLAYER_FACING_PUBLICATION` for `roanoke-s5-legends`. Publication is not live use.

`BCS-000113` revises the Mining, Blood Magic, bard colleges, Lumber Jacked, and cleric-options pages it actually discusses. `BCS-000114` is published as the Way of Gun Fu page `BCS-000110`.

No Season 5 live Discord harvest is in the corpus. Do not infer that a published subclass was played.

### At War's End — revision lineage is usable

Native titles support first draft → second draft → third draft → draft 5 (`BCS-000060`–`BCS-000063`). Draft 4 is not here. Later is not marked as superseding earlier.

`BCS-000064` outlines the "We are Lost" nocturnes used in the second draft. `BCS-000065` outlines draft 5's Queen Seraphine chapter. Wellsprings (`BCS-000066`) and the writing prompt (`BCS-000067`) are companions, not drafts. Nothing here establishes live play.

### Bastion / Redoubt and Earthfall — document pairs only

The Session 1 script links the introduction Drive file (`BCS-000056` → `BCS-000057`). Character creation (`BCS-000058`) is the third companion. No live evidence.

Earthfall's R.O.D. system spec (`BCS-000054`) and showrunner script (`BCS-000055`) are companions. No live evidence.

### Season 2 — two planning documents

`BCS-000042` states that it is the season-two guide for 2019. `BCS-000024` is titled Roanoke S2; the body is a general Discord DM guide and does not restate the season, so placement is strong rather than confirmed. No Season 2 Discord harvest is in the corpus.

## Still archived without a season

| ID | Why it stays unplaced |
| --- | --- |
| BCS-000017 | Roanoke epilogue fiction. August 21 and Solomon are suggestive of Season 3 and not sufficient. |
| BCS-000019 | City-building rules. The text does not name a season. |
| BCS-000022 | Native title is an island bestiary. The normalized body is empty. |
| BCS-000047 | A Roanoke song with no season. |

## Acceptance check

| Question | Where it now works | Where it still fails |
| --- | --- | --- |
| What campaign? | S3 operations and lore, S4 planning, S5 sites, At War's End, Bastion, Earthfall, S2 guide | Epilogue, city directory, song, empty bestiary, the two unordered crafting drafts |
| What kind of source, and where in production? | Stages on the families above | At War's End chapter drafts have no stage; they are manuscripts, not campaign prep |
| What other versions exist? | Crafting, S3 2.0 chain, Post issues, At War's End drafts, Gun Fu | S4 Master Timeline is named in the directory and is not a container |
| Which was public? | S3 public lore and FAQ, S5 Sites, Crafting with Class public doc | Empire City Post distribution is unproven |
| Live use? | Crafting with Class; airship qualification | Almost every other prepared document |
| Later revision? | S3 changelog; S5 site changelog; At War's End draft numbers | No claim that a later draft won |
| Move prep to live evidence and back? | Crafting announcements and crafting-questions; flight-school | Week operations, Golden Dawn beats, S5 play |

## Not ready for longitudinal BFDM research

Ready means a researcher can follow the preserved chain without reconstructing it, and the unknowns are labeled.

Ready enough to start that work:

- Season 3 Crafting with Class, including the public doc and the live clarifications.
- Season 3 campaign manuscript from brainstorm to 2.0 to changelog.
- Season 3 lore index and the public-lore adaptation into Empire City.
- Empire City airship qualification, from module to flight-school.
- Season 5 changelog to the five published pages it edits, and Way of Gun Fu to its Site.
- At War's End draft order, including the missing fourth draft and the unsuperseded earlier drafts.

Not ready:

- Season 5 live play. The Sites are publications only.
- Season 2 live play. No harvest.
- Golden Dawn quest design. `BCS-000118` has the export and comments, not a text mirror. Live Golden Dawn play exists in channel `698489628289925130` and is not linked, because the quest beats cannot be checked.
- Empire City Post as played artifacts.
- Season 4 crafting as a descendant of Season 3 crafting.
- Scene-level ties from S3 week documents to Discord.
- The 134 unreviewed Drive candidates.
- `indexes/documents.sqlite`. Relationship truth is the metadata. The derived document index was not rebuilt.

Revision bodies are still pending on the Google-native sources that already said so. This pass did not invent them.
