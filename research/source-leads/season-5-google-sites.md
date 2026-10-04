# Season 5 Google Sites source inventory

**Project:** `roanoke-s5-legends`  
**Source family:** Google Sites player-facing / rules / homebrew publication layer  
**Status:** archived on ingest branch; 26/26 linked sites captured successfully  
**Recorded:** 2026-10-04

## Why this source family matters

Brendon identified the Season 5 Google Sites as containing substantial player-facing material for classes, character creation, homebrew items, life paths, house rules, server rules, and setting/world lore. These sites are therefore a primary Season 5 publication/implementation layer alongside Drive planning sources and the Season 5 development Discord.

The useful evidence chain is:

`Drive planning -> dev Discord deliberation -> Google Sites published rules/content -> partial live delivery (where recoverable)`

Because Season 5 did not complete, publication establishes that a design reached a player-facing implementation state. It does not establish that every published mechanic or page was used in live play.

## Discovery and coverage

Brendon supplied 21 unique Season 5 / Arcanian Google Sites URLs. One supplied URL (`arcanianmonkoptions`) was duplicated and was deduplicated.

Following the captured player-facing link graph discovered five additional sites:

- `arcanian-server-rules` — linked from `tales-in-legend`
- `char-gen` — linked from `tales-in-legend`
- `arcanian-monk-options` — linked from `char-gen`
- `s5-codebound` — linked from `char-gen`
- `s5homebrewclericoptions` — linked from `char-gen`

The final manifest contains 26 sites. The post-harvest link-graph check found **no additional Google Sites /view/ namespaces linked from the captured pages**.

## Known sites

| Site slug | URL | Role | Acquisition |
|---|---|---|---|
| `catalogs5` | https://sites.google.com/view/catalogs5/home | items / equipment / catalog | user supplied |
| `s5backgrounds` | https://sites.google.com/view/s5backgrounds/home | backgrounds / character creation | user supplied |
| `s5mining` | https://sites.google.com/view/s5mining/home | life path / mining / economy | user supplied |
| `lifepathrancher` | https://sites.google.com/view/lifepathrancher/home | life path / ranching / economy | user supplied |
| `day-1s5` | https://sites.google.com/view/day-1s5/home | day-one player-facing content | user supplied |
| `s5bardcolleges` | https://sites.google.com/view/s5bardcolleges/home | bard options | user supplied |
| `homebrew-spells` | https://sites.google.com/view/homebrew-spells/home | homebrew spells | user supplied |
| `harbingers5` | https://sites.google.com/view/harbingers5/home | character option | user supplied |
| `spellshotwizard` | https://sites.google.com/view/spellshotwizard/home | wizard option | user supplied |
| `lifepathgambler` | https://sites.google.com/view/lifepathgambler/home | life path / gambling / economy | user supplied |
| `s5-training` | https://sites.google.com/view/s5-training/home | training rules | user supplied |
| `s5warlockoptions` | https://sites.google.com/view/s5warlockoptions/home | warlock options | user supplied |
| `path-of-the-lumber-jacked` | https://sites.google.com/view/path-of-the-lumber-jacked/home | barbarian option | user supplied |
| `oath-of-the-drifter` | https://sites.google.com/view/oath-of-the-drifter/home | paladin option | user supplied |
| `s5rogueoptions` | https://sites.google.com/view/s5rogueoptions/home | rogue options | user supplied |
| `improvised-weapon-for-enforcer` | https://sites.google.com/view/improvised-weapon-for-enforcer/home | improvised-weapon / enforcer rules | user supplied |
| `arcanianmonkoptions` | https://sites.google.com/view/arcanianmonkoptions/home | thin/stale Monk shell; see relationship note | user supplied |
| `arcanian-house-rules` | https://sites.google.com/view/arcanian-house-rules/home | house rules | user supplied |
| `tales-in-legend` | https://sites.google.com/view/tales-in-legend/home | Season 5 landing / player orientation | user supplied |
| `arcanian-worldlore` | https://sites.google.com/view/arcanian-worldlore/home | world lore | user supplied |
| `homebrew-races` | https://sites.google.com/view/homebrew-races/home | homebrew races | user supplied |
| `arcanian-server-rules` | https://sites.google.com/view/arcanian-server-rules/home | server/social rules | link-graph discovery |
| `char-gen` | https://sites.google.com/view/char-gen/home | character creation / difficulty / allowed options | link-graph discovery |
| `arcanian-monk-options` | https://sites.google.com/view/arcanian-monk-options/home | full Way of Gun Fu monk option | link-graph discovery |
| `s5-codebound` | https://sites.google.com/view/s5-codebound/home | Oath of the Codebound paladin option | link-graph discovery |
| `s5homebrewclericoptions` | https://sites.google.com/view/s5homebrewclericoptions/home | homebrew cleric / Calico domains | link-graph discovery |

## Archive result

The chat/web crawler was unreliable on a number of pages, but the repository-side direct HTTP harvest succeeded across the full linked family.

- Harvest report: `ingest/reports/2026-10-04-season5-google-sites.md`
- Machine report: `ingest/reports/2026-10-04-season5-google-sites.json`
- Source root: `sources/roanoke-s5-legends/google-sites/`
- Capture: **26/26 sites, 26/26 seed pages, zero fetch failures**
- Each site retains raw HTTP HTML, a normalized readable Markdown mirror, page-level URL/hash/retrieval metadata, outbound links, and Google Drive/Docs links exposed in page anchors.
- The harvester is retained at `ingest/google_sites/harvest_google_sites.py`.
- The exact harvest manifest is retained at `ingest/google_sites/season5_sites.json`.
- The harvester reports linked Google Sites that are absent from the manifest; the final pass reported none.

The earlier crawler failures were artifacts of the chat/web retrieval surface, not evidence that the Sites were inaccessible.

## Important source relationships

### Monk URL/version family

The user-supplied `arcanianmonkoptions` site is a thin page whose readable body contains only the heading for **The Way of Gun-Fu**. The Season 5 Character Creation page instead links to `arcanian-monk-options`, which contains the complete published Way of Gun Fu subclass.

A matching earlier/source copy also exists in connected Google Drive:

- Title: `Subclass - Monk - The Way of Gun Fu - The Homebrewery.pdf`
- Drive ID: `1qL8Q1E4gnDwlk37uOAXjk9A2cMEdHI6l`
- Created: 2022-03-24
- Modified: 2022-03-24
- Relationship: supporting/version-family source; do not count it as independent confirmation merely because the same rules appear in both places.

### Season 5 Site Changelog

Connected Google Drive contains a directly relevant revision source:

- Title: `S5 Site Changelog / To Change`
- Drive ID: `1Dk0JwcnTxVW41c1wHlnEoURrE2qkkEUBdMYQCSOUTuI`
- Created: 2023-07-28
- Modified: 2023-07-31
- Current readable body: 24,153 characters
- Role: proposed corrections, wording fixes, unresolved questions, and site-by-site revision discussion.

This is a high-value bridge between development deliberation and the published Site state and should be reconciled with the Site snapshots and Season 5 dev Discord during decision-case research.

## Player-facing season anchors exposed by the Sites

The `tales-in-legend` landing page states that signups were limited to 30 spots, game dates were July 30 through August 19, servers opened July 28, and the event was a free play-by-post with 24-hour RP. Treat these as published player-facing statements; they do not by themselves establish the exact observed live-play window.

The `char-gen` page records a three-tier difficulty scheme (Tenderfoot, Aces, Desperado), Life Paths, approved/unapproved/homebrew races, no multiclassing, level 6 start, ammunition and encumbrance tracking, XP advancement, and class/subclass restrictions/options.

The `arcanian-server-rules` page records the campaign's explicit social/operational contract, including player spotlight, real-time-rest rationale, PvP consent, inventory honesty, exploit reporting, clique handling, and the stated split of roughly 75% freeplay/character-driven play and 25% DM-authored story.

These are unusually strong sources for reconstructing intended Season 5 operating philosophy, but must remain distinct from evidence of what actually happened in play.

## Remaining archival/research work

1. Deduplicate and reconcile linked Drive files against already-ingested Season 5 Drive sources.
2. Preserve embedded images/assets separately where they carry design evidence not recoverable from raw HTML.
3. Reconcile `S5 Site Changelog / To Change` against the captured published pages to recover revision decisions.
4. Cross-link published mechanics to Season 5 dev-Discord deliberation when Grok's scrape lands.
5. Keep `planned`, `published`, `partially delivered`, and `observed in play` as separate evidence states.
6. Allocate canonical source records only after source identity, role, authorship boundaries, and duplication relationships have been reviewed.
