# Coverage for the player-option inventory

Date of search: 2026-10-09. Authority commit: `6795362e967e89230086afc28c04450cc7d0cce4` on `main`.

This inventory does not reindex the corpus. It reads sources that existing tools and files already expose.

## What was searched exhaustively

| Family | What was searched | Result |
|---|---|---|
| Season 5 Google Sites | All 26 `pages/home.md` files under `sources/roanoke-s5-legends/google-sites/`. Each site has one captured page. | Read. These 26 containers are **not** in `source_fts` (167 of 193 containers are indexed). A document-index search alone would have missed them. |
| Other BCS containers | `source_fts` queries: ability score, hit dice, subclass, background, feat, wellspring, pigeon lord, combat field / field scholar, urucokra, mudskipper, bullygrung, clerrook, path of, oath of, college of, domain of, subrace, class features, hit points at 1st, life path. | 167 indexed bodies. Zero for mudskipper and clerrook. Mudskipper exists only on the unindexed race site. Clerrook is absent. |
| Option-bearing containers opened beyond the index | Race verbatim and edits, Almanac, Pigeon Lord draft and v2, CFS, S3 and S4 backgrounds, Wellsprings, isekai reskins, allow-lists, bowling event, BaR character creation, S5 character-creation Drive text, Gun Fu PDF extract, S5 changelog, Rowing Oak mention check, Hampstead module check (NPC class column, not a player option). | Used as anchors where they contain rules. |
| Discord, three harvests | Hydrated SQLite. Phrase match on `messages_fts` for the term list in `discord-mentions.jsonl`. Roanoke Season 3: 197,013 messages. Empire City: 189,761. Empire City Dev: 12,692. | Exhaustive **for those phrases**. A zero count means that phrase is absent from that harvest's message text. It does not mean an unlisted name is absent. |
| Attachment metadata | `attachments` tables in all three SQLite files. Filename `LIKE` for jackalope, tatankan, chinnokin, harbinger, pigeon, gun, subclass, race, background, feat, cleric, bard, homebrew, spell, wellspring, almanac, uru. | Metadata searched. **Bytes not opened.** Checked local files are Git LFS pointers (about 130 bytes, `version https://git-lfs.github.com/spec/v1`). |

`model-index/discord/roanoke-season-3/attachments.jsonl` exists. Empire City and Empire City Dev have no `attachments.jsonl`. Their attachment metadata was read from SQLite, which this environment hydrated. A model that cannot open SQLite still has the Roanoke attachment projection and does not have those two projections.

## What was not exhaustive

- Discord was not read message by message for homebrew that does not use a searched phrase. Do not call the Discord discovery of unknown option names exhaustive.
- `catalogs5` (BCS-000087) is an item catalog. It was opened far enough to see it is equipment, not a race or class list. Individual catalog rows were not copied and were not each classified.
- `day-1s5` is session fiction and prompts, including an NPC called Ace the Gambler. That NPC is not the Gambler life path.
- House rules, server rules, and world lore were not treated as player options. Training (BCS-000097) is included because it is a character-advancement procedure.
- BCS-000192, BCS-000193, and BCS-000194 list external published species, classes, feats, spells, and backgrounds. Those external names are not homebrew options and were not enumerated.
- Feats: no original homebrew feat list was found. `feat` hits in the document index are the allow-lists, the isekai file's use of the word, the changelog, and unrelated prose. There is no feat section to inventory.
- Attachment images were not viewed. A filename such as `Jackalopes_Max_edit_page1.jpg` is a lead, not a readable rules text, until the LFS object is hydrated.
- Clerrook remains an archive gap. The research lead is not a source body.
- Bullygrung is a name on char-gen without a trait block in the captured race page.
- Urucokra has verbatim and edit notes and is not on the Season 5 race page.
- Reporter and panhandler are todo names in BCS-000184 without rules.
- Gamesmen and Falconers, and the Royal Academy of Naturalistic studies, are name stubs in BCS-000085.

## Play

Publication is not play. Preparation is not play. Name hits in `town-square`, location channels, `out-of-character`, `playable-races`, or `character-introduction` are recorded as phrase hits only. No option in this inventory is marked play-observed.

## Counts by campaign label

| Campaign label | Records |
|---|---|
| roanoke-s5-legends | 64 |
| at-wars-end | 49 |
| later-play | 26 |
| empire-city | 10 |
| roanoke | 6 |
| unassigned | 2 |
| bastion-redoubt | 1 |
| bowling-event | 1 |

The At War's End count is mostly archetype names without level rules. Subtract `class_archetype_name` before treating that count as finished classes.

