# Research substrate audit — 2026-10-05

Substrate: `ingest/drive-history-v1` at `ffd4ec2c` (PR #25). This audit does not edit source metadata and does not extract DM principles.

A researcher who trusts the readiness label, Discord search, and the files already in `sources/` will reconstruct a thinner and more Discord-shaped history than the Drive record supports.

## What was tested

Eight histories, using `scripts/query_source_history.py` and the metadata it reads:

| History | Prep found | Versions found | Stage | Operations | Live when it exists | Absence stays unknown | Later revision | Back from live | Forward from prep | Where it breaks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S3 Crafting with Class | Yes, `BCS-000077` | Family lists five members. Only `BCS-000080` is a predecessor edge. | Yes for the 2020 docs. `BCS-000020` and `BCS-000080` have no season. | No | Channel `739240413269065890` is on the public doc only | The dev doc's own live list is empty | Public/dev pair, not a later redesign | Open the public doc, then the dev pair | One hop, and only after this audit's family-live field | Early drafts are unordered. Season 4 crafting is a different family. |
| S3 manuscript | `BCS-000045` rough draft. Brainstorm `BCS-000043` is in the family and has no edge. | `BCS-000041` revises the rough draft only | Yes | No | Explicitly not established | Yes | Changelog `BCS-000046` is another family and is not a `REVISES` link | No live edge | No live edge | Brainstorm order is family membership only. The changelog does not point at the manuscript. |
| S3 week operations | Week sheets, casts, and several cited modules | Companions, not a revision chain | Campaign operations | Yes | Not established. A schedule is not play. | Yes | Week 4 cast is still missing. Week 5 map is now `BCS-000130`. | No | Cited modules that were ingested can be opened. Manticore and the elevator module cannot. | Live Discord is a separate search. Week sheets do not point at message ids. |
| Airship qualification | `BCS-000073` | No version chain | Prep | Directory is a companion | `flight-school` messages named in the basis for 2021-07-11 | Later missions stay unresolved | No | The link is on the module | The link is on the module | Airship Rules is named and has no Drive id. |
| Empire City operations and Post | Directory, backlog, eleven issues | Post issues are `COMPANION_TO`, not an order | Yes | Partial | Post distribution is not established | Yes | No supersession | No | No | S4 Master Timeline is not a container. Phrase search for "Master Timeline" in Empire City Dev returns zero. |
| At War's End | Draft 1 | Draft 2 revises draft 1. Draft 5 also revises draft 1. Draft 3 does not revise draft 2. | Stage deliberately unresolved | No | Not established | Yes | Revision edges exist and do not mean the later draft won | No live edge | No live edge | Draft 4 is absent. Draft 3 is off the revision edge. |
| Season 5 Drive to Site | Gun Fu PDF and the changelog | `PUBLISHED_AS` for Gun Fu. Changelog uses `REVISION_CONTEXT_FOR_SOURCE_FAMILY`, which is not a before/after edge. | Publication versus system development | Signup sheet is still a candidate | Not established. No Season 5 harvest. | Yes | The changelog names pages. The readiness label still says longitudinal gap. | No live edge | Publication only, and only if the id is already known | Style guide, DM guide, and internal char-gen doc are not containers. |
| Bastion and Earthfall | Script, introduction, character guide; R.O.D. spec and operator script | Companions | Prep or system development | No | Not established | Yes | No | No live edge | No live edge | No harvest. The chains stop at the document pair. |

## READY

Strong enough to read, with the limit written next to the chain:

- Season 3 public Crafting with Class to the crafting-questions channel. The dev doc, the working copy, and the public doc are the same family. The 2019 attempt and `BCS-000020` are not assigned a season.
- The 2021-07-11 flight-school session named on `BCS-000073`. That is one exercise, not every later flight.
- Way of Gun Fu PDF to the published monk page. Publication is not play.
- Season 3 rough draft to the 2.0 manuscript. The brainstorm is in the family without an order edge.
- At War's End draft 1 to draft 2, if draft 3 and the jump from draft 5 back to draft 1 are kept visible.

Those are reading paths. They are not a sample of Brendon's judgment.

## ARCHIVE GAPS

Ledger: `research/substrate/archive_gaps.jsonl`. 36 rows.

| Status | Rows |
| --- | --- |
| `MISSING_KNOWN_SOURCE` | 21 |
| `POSSIBLE_CANDIDATE_MATCH` | 12 |
| `RESOLVED` | 1 (week 5 map, now `BCS-000130`) |
| `EXTERNAL_OR_UNAVAILABLE` | 1 (Sane Magical Prices) |
| `AMBIGUOUS_REFERENCE` | 1 (Season 3 directory headings with no URL) |

The 21 missing rows include one class, not one file: 259 Google revision rows have `body_fetched: false`. The other 20 name artifacts. Two of those rows cover two Drive files each (hex drawings, week 2 audio).

Highest-cost missing files:

- S4 Master Timeline `1Lk2IkEgh1aHjuUl35g1Huk7oxjNSjhmfsKKaHDL1_K8`
- S5 style guide `1fpOQbmy836cs41ewNXcTUdwdfswuOEETqioshQURcm0`
- Season 5 Dungeon Master's guide `15EqRAkYPaSj8009y_ygsOun3TzKcFoBvcn9Liw7q_MQ`
- Player race edits `11GF5rYImy_jdf7NxAtf5gI-OW2DCTlxjgZCOHLnC3cY`
- The Rowing Oak and its guide (candidates, not containers)
- 2020 house-rules release `19q9mnafswYmNIUK3DK57O2MPqtSl78M4UcJSfBZfhA8`
- Season 5 crafting document, Season 4 and Season 5 character-creation docs
- Tatankan verbatim, while the other three race verbatims are containers
- Bahamut's Folly / manticore module, week 4 cast list, Airship Rules (no id)

The Season 3 directory also names all-hands notes, initiative trackers, week bestiaries, and Season 2 charter/map/crafting files without URLs. That is one ambiguous row. It is not twenty missing files.

## EVIDENCE GAPS

The record that is present does not establish:

- Season 5 live play. The Sites advertise dates. There is no Season 5 harvest.
- Season 2 live play. The registry live window is null.
- That a week sheet was run, except where a message id is already on a link.
- That Empire City Post issues were distributed.
- That Season 4 crafting's harvesting and conversion rules were the rules used. The approval channel is identified. `rule_by_rule_live_identity` is not.
- That later flight-school scenes used the qualification module.
- That a later At War's End draft replaced an earlier one.
- Why mechanics changed. Player race edits, the document that records those changes, is absent. Most revision bodies were not fetched.
- A postmortem of a finished season. The full candidate open found none.

The island bestiary `BCS-000022` is a different kind of gap. The native Google Doc and the DOCX are empty. There is no text to recover. `GAP_REMAINS` is the right label.

## UNREVIEWED RISK

132 ledger rows are still `UNREVIEWED_CANDIDATE`. PR #25 opened them and wrote `research/drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md`. This audit turns that prose into actions. It does not ingest them.

| Action | Rows |
| --- | --- |
| `HIGH_PRIORITY_INGEST` | 28 |
| `LIKELY_FAMILY_MEMBER` | 42 |
| `CONTEXT_ONLY` | 20 |
| `LIKELY_DUPLICATE_OR_VERSION` | 10 |
| `LOW_RESEARCH_VALUE` | 10 |
| `UNRELATED` | 5 |
| `NEEDS_MANUAL_REVIEW` | 17 |

The 28 high-priority rows are the ones that can change a later conclusion: Rowing Oak and its guide, the Almanac, Arcanian lore and the setting book, Ferrytown's schedule and master doc, Hampstead's module and player guide, the elevator gauntlet, Season 5 framing and the Legends signup, species-allowance and allowed-content sheets, Season 5 craft notes, Combat Field Scholar, Monster Chess, Gil's Rebirth notes, an Elijah handoff, a 2026 Kore-A session log, and an Empire City epilogue.

Seventeen rows stay manual: five could not be read (404 or failed extraction), and the full-open narrative did not give the others their own role. `All of Me` may be the Ox Rat sheet the pass mentions. That match is not made here.

No opened candidate is a season postmortem. That absence is established for the opened set only.

## ACCESS BIAS

Discord is the easy corpus. Drive history is an id lookup.

- `scripts/search_corpus.py "Master Timeline" --server empire-city-dev --phrase` returns zero hits and sets `zero_match_means_absence` because the projection search is exhaustive. The timeline URL was posted by bfdm in messages `748279131455881360` and `752645676260917248`. The title is not in the message text. A zero is absence from that phrase search, not absence of the document.
- Before this audit, `query_source_history.py` required a BCS id, hid Season 5 `REVISION_CONTEXT_FOR_SOURCE_FAMILY` inside `other_links`, and did not show that the crafting public doc carries the live channel when the question starts from the dev doc.
- Revision rows record that a file changed. 259 bodies were not fetched, and no query surfaces them.
- Readiness puts seven families in `LONGITUDINAL_RESEARCH_READY`. A researcher who samples "ready" families studies one revision edge or one channel, and misses the Season 5 changelog, which has eleven revision-context links and is labeled a longitudinal gap.
- Season 3 Discord is the largest live harvest. Season 2 and Season 5 have no harvest. Live-play research will be a Season 3 and Empire City study unless the missing Drive design files are ingested first.
- Image evidence is easy to skip. `BCS-000130` is a JPEG. The markdown stub says room names were not transcribed. A text search will not find the map's contents.

`zero_match_means_absence` means the harvest projection was fully searched. It does not mean the historical event did not happen. This audit does not change that flag.

## INTEGRATION DEBT

Present, and not a usable chain:

- `BCS-000043` sits in the manuscript family with no link.
- `BCS-000062` (third draft) companions an outline. It does not revise draft 2.
- `BCS-000046` companions lore documents. It does not revise the manuscript it is the changelog for.
- Empire City Post issues companion the intro or each other. Masthead order is in the titles, not in `SUCCESSOR_OF`.
- `BCS-000115` revises `BCS-000070`. Each family is then labeled longitudinally ready. The edge is a timeline disambiguation.
- `BCS-000001` is longitudinally ready because of an approval-channel link, while the metadata says rule-by-rule identity is not established.
- Season 5 changelog links are real and invisible to `came_before` / `came_after`.
- `BCS-000068` is in the catalog and has no source container. It is a retrospective excerpt record, not a missing Drive file.
- `BCS-000053` still uses the question `referenced_source_absent` after the week 5 map was ingested. The basis text is the accurate part: the map is `BCS-000130`, and the week 4 cast is the remaining hole.
- Race verbatims have no revision edge. The revision document is the missing player-race-edits file. The stage matrix marks that `KNOWN_GAP` on five race families.

## Readiness labels

The definition is internally consistent and too easy to over-read.

`LONGITUDINAL_RESEARCH_READY` means at least one `REVISES`, `SUPERSEDES`, `PREDECESSOR_OF`, `SUCCESSOR_OF`, or live-contact link. A publication, a companion, and an explicit live-use gap do not qualify. That correctly keeps Gun Fu and the Season 5 Sites out of the ready set.

It also does all of the following:

- Marks the timeline and the one-page disambiguation ready.
- Marks the manuscript family ready while the brainstorm has no edge.
- Marks At War's End ready while draft 3 is off the chain.
- Marks Empire City crafting ready from a channel link that the same metadata refuses to treat as the whole system.
- Marks the Season 5 changelog a longitudinal gap even though it names the pages it edits. `REVISION_CONTEXT_FOR_SOURCE_FAMILY` is not in the revision set.

Sampled false-positive risk is in those seven ready families, not in `CONTEXT_ONLY` (`BCS-000059` only) and not in the island bestiary `GAP_REMAINS`. `SOURCE_RESEARCH_READY` means the source is oriented. It does not mean the research has been done. That sentence in the readiness report is accurate. The longitudinal word "ready" is the part a later phase will misuse.

This audit does not redefine the label.

## Historical-function coverage

| Function | Coverage | Why |
| --- | --- | --- |
| Single-table DM | `PARTIAL` | Week modules and the airship drill exist. Most week sheets are not tied to messages. |
| Campaign designer | `PARTIAL` | Season 3 manuscript and directory exist. The Season 4 timeline and the Season 5 style guide do not. |
| Rules and system designer | `PARTIAL` | Season 3 crafting is the best chain. Season 4 crafting is channel-level. Season 5 crafting is missing. Race revisions are missing. |
| Multi-DM coordinator | `PARTIAL` | Season 3 casts, passdowns, and the mod directory are containers. The 2018 three-DM guide is still a candidate. |
| Large persistent-campaign operator | `PARTIAL` | Season 3 and Empire City have directories plus Discord harvests. Season 5 operations are a signup candidate plus published pages. |
| Reviser reacting to live play | `SERIOUS GAP` | Almost no `ALTERED_IN` link. Revision bodies are mostly unfetched. The race-edits document is absent. |
| Designer responding to failure | `SERIOUS GAP` | No season postmortem in the opened candidate set. The Season 3 changelog is not tied to outcomes. |
| Designer abandoning prep | `UNKNOWN` | Early crafting drafts are preserved. Nothing is marked `ABANDONED_IN`. |
| Allocating player attention | `PARTIAL` | Week schedules and set lists exist. They are not joined to who actually received the spotlight. |
| Continuity across sessions | `PARTIAL` | Season 3 timeline and week chain exist. The Season 4 timeline does not. |
| Turning inspiration into playable material | `PARTIAL` | Several cited Season 3 modules are now containers. Manticore and the elevator module are not, and live use of the ingested modules is not established. |

## RECOMMENDED FIXES BEFORE BFDM RESEARCH

### P0 — likely to distort conclusions

1. Do not sample `LONGITUDINAL_RESEARCH_READY` as the research set. Split "has one edge" from "the chain can be followed." Count `REVISION_CONTEXT_FOR_SOURCE_FAMILY` as a visible revision path for the Season 5 changelog.
2. Ingest, or explicitly park, the named lineage files before any judgment pass: S4 Master Timeline, S5 style guide, S5 DM guide, player race edits, The Rowing Oak and its guide, the 2020 house-rules release.
3. Treat Discord `zero_match_means_absence` as absence from the searched harvest, not absence from history. The Master Timeline case is the worked example.
4. Keep Season 4 crafting's channel link from being retold as "the essence economy was implemented."

### P1 — materially improves reconstruction

1. Ingest the high-priority candidate rows that are already cited: Ferrytown schedule, elevator gauntlet, then Hampstead, the Almanac, and the Season 5 framing doc.
2. Fetch revision bodies for the families that will be studied, starting with crafting, the Season 3 changelog, and the race documents.
3. Record the manuscript brainstorm and the At War's End third draft only if a reread supports an order edge. Do not invent one.
4. Point the Season 3 changelog at the manuscript as a companion or revision-context link if the changelog text names those changes. It currently points at lore.
5. Give Airship Rules a Drive id or an explicit unresolved-id gap on the module. The sentence is already in the body.

### P2 — useful, not blocking

1. Resolve the ambiguous Season 3 directory headings by recovering hyperlinks from the DOCX, not by guessing.
2. Compare The Urucokra candidate with `BCS-000120` before a second container.
3. Ingest the Tatankan verbatim so the race set is not missing one sibling.
4. Transcribe nothing from the week 5 JPEG unless someone is looking at the image. The stub already refuses invented room names.

### P3 — cleanup

1. Rename the `BCS-000053` question that still says `referenced_source_absent` after the map landed.
2. Leave `BCS-000068` as a catalog-only retrospective. It is not a Drive hole.
3. Leave SRD, Mad Mage, and blank character-sheet templates as context. They are not precedent.

## STAGE 1 VERDICT

`NOT_READY`

PR #25 makes several chains readable: Season 3 crafting, one airship session, Gun Fu's publication, the Season 3 manuscript edge, and part of the At War's End draft order. The week 5 map is no longer a ghost link. The island bestiary is correctly an empty document.

The substrate is not ready for judgment research. The ready label promotes single edges. The Season 5 changelog is labeled a gap while it points at the pages it edits. The design files that explain earlier seasons and later revisions are still outside the corpus, several of them already identified by Drive id. Discord search will answer first, and it will answer "not found" for a timeline that was posted as a bare URL.

After the P0 items, the verdict can move to `READY_WITH_DOCUMENTED_GAPS`. It should not move there on file count.

## What PR #25 should take before merge

- Say, in the readiness report, that longitudinal ready means one recorded edge. List the seven families under that definition so nobody samples them as finished histories.
- Surface `REVISION_CONTEXT_FOR_SOURCE_FAMILY` in the history query. This branch does that without removing the links from `other_links`, because the existing test requires them there.
- Show family-level live links separately from the document's own live links. The crafting dev doc was failing the forward path.
- The week 5 map commit is right. The leftover `referenced_source_absent` question on `BCS-000053` should be renamed to the week 4 cast.
- Do not describe Empire City crafting as implemented beyond the approval channel. The metadata gap already says this. The family label does not.
- The candidate open in `TRIAGE_PASS_2026-10-05.md` is evidence. It is not ingestion. The 28 high-priority rows in this audit are the ingest queue.

## Tooling added

```bash
python scripts/query_source_history.py BCS-000077 --text
python scripts/query_source_family.py roanoke-crafting-system
python scripts/query_project_history.py roanoke-s3
python scripts/query_archive_gaps.py --project roanoke-s4
python scripts/query_research_readiness.py --longitudinal-ready
```

`--json` is available on each. `query_source_history.py` stays JSON by default so the existing tests keep their shape.
