# Season 5 Google Sites source inventory

**Project:** `roanoke-s5-legends`  
**Source family:** Google Sites player-facing / rules / homebrew publication layer  
**Status:** archived on ingest branch; 21/21 known sites captured successfully  
**Recorded:** 2026-10-04

## Why this source family matters

Brendon identified the Season 5 Google Sites as containing substantial player-facing material for classes, character creation, homebrew items, life paths, house rules, and setting/world lore. These sites should therefore be treated as a primary Season 5 publication/implementation layer alongside the Drive planning sources and the Season 5 development Discord.

The useful evidence chain may be:

`Drive planning -> dev Discord deliberation -> Google Sites published rules/content -> partial live delivery (where recoverable)`

Because Season 5 did not complete, published Google Sites material is evidence that a design reached a player-facing implementation state; it is not by itself evidence that every published mechanic or page was actually used in live play.

## Known sites

There are 21 unique known Season 5 / Arcanian Google Sites URLs in the current inventory. One URL (`arcanianmonkoptions`) was supplied twice and is deduplicated here.

| Site | URL | 2026-10-04 retrieval status | Preliminary role |
|---|---|---|---|
| Season 5 Catalog | https://sites.google.com/view/catalogs5/home | DIRECTLY_READABLE | items / equipment / catalog |
| S5 Backgrounds | https://sites.google.com/view/s5backgrounds/home | DIRECTLY_READABLE | backgrounds |
| S5 Mining | https://sites.google.com/view/s5mining/home | DIRECTLY_READABLE | life path / economy / mining rules |
| Life Path Rancher | https://sites.google.com/view/lifepathrancher/home | DIRECTLY_READABLE | life path / economy |
| Day 1 S5 | https://sites.google.com/view/day-1s5/home | DIRECTLY_READABLE | launch / player-facing day-one content |
| S5 Bard Colleges | https://sites.google.com/view/s5bardcolleges/home | CAPTURED_DIRECT_HTTP | class/subclass options |
| Homebrew Spells | https://sites.google.com/view/homebrew-spells/home | CAPTURED_DIRECT_HTTP | spells |
| Harbinger S5 | https://sites.google.com/view/harbingers5/home | CAPTURED_DIRECT_HTTP | class/subclass or character option; verify from source |
| Spellshot Wizard | https://sites.google.com/view/spellshotwizard/home | CAPTURED_DIRECT_HTTP | wizard option |
| Life Path Gambler | https://sites.google.com/view/lifepathgambler/home | CAPTURED_DIRECT_HTTP | life path / economy |
| S5 Training | https://sites.google.com/view/s5-training/home | DIRECTLY_READABLE | training rules |
| S5 Warlock Options | https://sites.google.com/view/s5warlockoptions/home | CAPTURED_DIRECT_HTTP | warlock options |
| Path of the Lumber Jacked | https://sites.google.com/view/path-of-the-lumber-jacked/home | CAPTURED_DIRECT_HTTP | barbarian option |
| Oath of the Drifter | https://sites.google.com/view/oath-of-the-drifter/home | CAPTURED_DIRECT_HTTP | paladin option |
| S5 Rogue Options | https://sites.google.com/view/s5rogueoptions/home | CAPTURED_DIRECT_HTTP | rogue options |
| Improvised Weapon for Enforcer | https://sites.google.com/view/improvised-weapon-for-enforcer/home | CAPTURED_DIRECT_HTTP | rule / option; verify from source |
| Arcanian Monk Options | https://sites.google.com/view/arcanianmonkoptions/home | CAPTURED_DIRECT_HTTP | monk options |
| Arcanian House Rules | https://sites.google.com/view/arcanian-house-rules/home | DIRECTLY_READABLE | house rules |
| Tales in Legend | https://sites.google.com/view/tales-in-legend/home | CAPTURED_DIRECT_HTTP | campaign/setting material; verify from source |
| Arcanian World Lore | https://sites.google.com/view/arcanian-worldlore/home | DIRECTLY_READABLE | world lore |
| Homebrew Races | https://sites.google.com/view/homebrew-races/home | CAPTURED_DIRECT_HTTP | race options |

## Confirmed readable examples

The directly readable pages demonstrate that this family contains substantive mechanics rather than link shells:

- `s5backgrounds` contains complete custom backgrounds with proficiencies, equipment, features, and region-specific backgrounds.
- `s5mining` contains the Miner life path, mining procedures, rewards, exhaustion pressure, starting gear, and economic rules.
- `catalogs5` contains substantial player-facing equipment and magic-item/catalog content, including custom firearms, costs, properties, and special effects.
- `arcanian-house-rules`, `s5-training`, `lifepathrancher`, `day-1s5`, and `arcanian-worldlore` are also directly retrievable as full Google Sites pages.

## Archive result

The chat/web crawler was unreliable on a number of these pages, but a repository-side direct HTTP harvest succeeded on all 21 known sites.

- Harvest report: `ingest/reports/2026-10-04-season5-google-sites.md`
- Machine report: `ingest/reports/2026-10-04-season5-google-sites.json`
- Source root: `sources/roanoke-s5-legends/google-sites/`
- Capture: 21/21 sites, 21/21 seed pages, zero fetch failures.
- Each site retains raw HTTP HTML, a normalized readable Markdown mirror, page-level URL/hash/retrieval metadata, outbound links, and Google Drive/Docs links exposed in page anchors.
- The harvester is retained at `ingest/google_sites/harvest_google_sites.py` with the exact user-supplied manifest at `ingest/google_sites/season5_sites.json`.

The earlier `CAPTURED_DIRECT_HTTP` classifications were artifacts of the chat crawler and are superseded by the successful direct harvest. They were not evidence that those Sites were inaccessible.

## Remaining archival work

1. Inspect exposed Drive/Docs links and deduplicate against already-ingested Season 5 Drive sources.
2. Preserve embedded images/assets separately where they carry design evidence not recoverable from the raw HTML snapshot.
3. Cross-link published mechanics to Drive drafts and Season 5 dev-Discord deliberation.
4. Keep `planned`, `published`, `partially delivered`, and `observed in play` as separate evidence states.
5. Allocate canonical source records only after source identity, role, authorship boundaries, and duplication relationships have been reviewed.
