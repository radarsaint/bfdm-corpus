# Source validation and coverage — Worker 2 tranche, 2026-10-16

Mechanical locator checks against `bfdm-corpus` `main` `2a650a735d8e39251979b157cf7aace9f8e443ef`. These checks do not certify interpretation, motive, or transfer. Where a citation is narrower than the sentence that cites it, the exception is recorded here. The historical wording in `records.md` was not silently repaired.

## Catalog

`evidence/catalog.jsonl` contains 195 BCS identities, `BCS-000001` through `BCS-000195`. Every BCS id cited by this tranche is in that catalog. None was missing.

`research/STATUS.md` on this commit says the document index contains 193 source containers, with `BCS-000059` context-only and `BCS-000068` excerpt-only. `python3 scripts/validate_source_history.py --repo .` reported `source containers: 194` and said that count includes context containers and Season 5 site metadata. That difference is a counting definition already present on this commit. It is not evidence the catalog grew after the research snapshot.

## Paths and line windows

Every claimed path exists. Every claimed line window falls inside the file. Line numbers are convenience coordinates, not evidence identity.

| Record | Path | Window | Result |
|---|---|---|---|
| 01 | `sources/roanoke/BCS-000136/source.md` | file, 240 lines | Present. Line 86 states offline production and barter. Lines 22–40 list specialist jobs. Line 204 states a barter economy. |
| 01 | `sources/roanoke/BCS-000137/source.md` | file, 626 lines | Present. Cited as companion early-Roanoke material. Not given a line window in the payload. |
| 01 | `sources/roanoke/BCS-000042/source.md` | 18–52, file ends at 52 | Present. Lines 22–24, 26–28, and 52 contain the chore, the daily roll, vocation bonus, banked work, the gold mistake, unfilled necessary jobs, and expanded NPC labor. |
| 02 | `sources/bowling-event/BCS-000182/source.md` | 8–76, 170–227, 237–252 | Present. Line 219: "No abilities can affect a PC’s ability to roll their second ball." Catalog authorship is `BRENDON`. |
| 03 | `model-index/discord/roanoke-season-3/messages-0050.jsonl` | eight native ids | All eight are in this shard, author `313689699627696139` (`DM radar` / `bfdm`), channel `🕍-the-roseline-temple-of-masons`, 2020-07-22. Neighbor rows in the same channel support the observation: sneak-attack denial, stair positioning, "How do you want to do this?", the blade pulled from the render and the doctor, the archivist's burial speech, and the bottle distribution left to the players. |
| 04 | `model-index/discord/roanoke-season-3/messages-0350.jsonl` | seven native ids | All seven are in this shard on 2020-08-18. See the exception below. |
| 05 | `model-index/discord/empire-city/messages-0009.jsonl` | `863492563784040539` | Present. Author is Brendon. The message pastes the housing ask and his refusal that homes were meant to stay vulnerable. |
| 05 | `model-index/discord/empire-city/messages-0087.jsonl` | five native ids | All five are in this shard, channel `a-fountain-of-player-tears`, 2021-07-16. Brendon authored `865565818481279018`, `865565932783796255` ("yeah"), and `865566464831258674`. `865565663296225280` and `865566812599353354` are hekiryuu. The staff-permission sentence is the second of those. That matches the record's split between DIRECT statements and STRONGLY RECONSTRUCTED staff permission. |
| 06, 07, 14 | `context/exploration-impossible/BCS-000059/comments.json` | cited comment ids | The portable file has 31 comment objects. Ids 0–30 all exist. Cited Brendon ids are Brendon Faulkner. Ids 16 and 24 are Michael Kennish and were not cited as Brendon's. |
| 06, 07 | `context/exploration-impossible/BCS-000059/source.md` | 113, 217, 231–241, 505–523, 575–583, 687–689 | Present. The manuscript remains third-party context. |
| 06, 07 | BCE-000001 | evidence registry | Parent evidence id exists. `item_count` 78. Authorship basis says the Drive comment set reported displayName Brendon Faulkner and `me=true` for all 78. The portable file's 31/29 counts were not merged into that 78. |
| 08 | `sources/roanoke-s5-legends/google-sites/arcanian-server-rules/pages/home.md` | 19–21, 33–49, 61–71 | Present. Line 21 says "24 hour format" and "fear of missing out" and "real time long rest". Lines 33–49 are PvP consent and withdrawal. Lines 61–71 are cliques and the 75/25 story contract. Catalog authorship is `UNKNOWN`. |
| 08 | BCS-000136 line 206 and BCS-000137 | "heard" | BCS-000136 line 206 says everyone deserves to be heard. BCS-000137 also contains the word "heard". |
| 09 | `sources/bastion-redoubt/BCS-000056/source.md` | 8–110, 200–235 | Present. Lines 8–18 assign Lamplighter patrols. Lines 200–228 separate a physical clue, a magical clue, and witness testimony. |
| 09 | `sources/bastion-redoubt/BCS-000057/source.md` | 10–24 | Present. Lines 12–14 tie monarchy and religious doctrine. Catalog authorship for both containers is `UNKNOWN`. |
| 10 | BCS-000060 through BCS-000064 `source.md` | cited opening windows | Present. 060 opens on pre-war cosmic exposition and Queen Seraphine. 061 opens in Lost's collective voice. 062 opens in the Copper Lantern. 063 opens on a Queen-centered aubade. 064 lines 8–20 are an outline of nocturnes rather than a fifth prose opening. Authorship of all five is `UNKNOWN` in the catalog. |
| 11 | `sources/earthfall/BCS-000054/source.md` | 8–118 | Present. Lines 14–20 separate a neutral system banner from R.O.D. commentary. Catalog authorship `UNKNOWN`. |
| 11, 15 | `sources/earthfall/BCS-000055/source.md` | 8–125 and 24–38 | Present. Lines 24–38 require in-character R.O.D., a deterministic economic model, and rarity gating. Catalog authorship `UNKNOWN`. |
| 12 | `sources/chatgpt-project-history/earthfall-live/BCS-000156/source.md` | 44–72 | Present. User lines request a wounded, feral Fryvern for six level-1 characters in a starcade whose games can supply power-ups. The file's own status block says the quarter-powered subsystem was deferred. |
| 12 | `sources/chatgpt-project-history/earthfall-live/BCS-000161/source.md` | 19–42 | Present. User text: the fight "ended in fizzle with the players being OP", then a request for pressure in the transition. The file says assistant responses are not fully exposed. No combat log was added. |
| 13, 14 | `sources/chatgpt-project-history/saturday-dnd/BCS-000172/source.md` | cited windows; file has 3445 lines | Present. Line 534: players missed clues to Tasha's portfolio. Line 717: "you are asuming they mentioned tasha. they didnt and they are just baricaded him in a room." |
| 15 | `sources/chatgpt-project-history/earthfall-live/BCS-000162/source.md` | 19–35 | Present. User lines request achievements for orange chicken fed to Nicolas Cage, a deliberately blank ship name, and collecting human remains. |
| N1 | `sources/roanoke-s5-legends/BCS-000113/source.md` | 1–50 | Present. The window is an editor's notes on ambiguous rules and proposed fixes. Catalog authorship is `UNKNOWN`. The negative finding stands. |
| N2 | `model-index/discord/roanoke-season-3/messages-0200.jsonl` | shard | The shard is 500 messages, all dated 2020-08-04. Exactly six have author id `313689699627696139`. Two of those six have empty content. The others are "Pin wut?", an initiative list, "I remember this now. I forgot this game.", and "Thank you copper". The low-yield window was not replaced. |

`BCS-000042` metadata `authorship.status` is `UNKNOWN`. The first person in line 52 is not, by itself, the native revision attribution W2-01 says is still required. The existing longitudinal note's revision-793 claim was not re-proved here and was not deleted.

`BCS-000156`, `BCS-000161`, `BCS-000162`, and `BCS-000172` are partial mixed conversations. User lines and assistant lines stay distinct.

## Exceptions recorded, not repaired

1. **W2-04 extra ids.** `745112984967446588` is the four-day property progression. `745113564422865027` is the conditional airship. `745113845227585636` is a player, KnightOfCydonia, asking what the crew needs. `745113880753340500` is Brendon's dinner-break note, not the offer. The three "plus" ids, `745124223256756305`, `745124512114147359`, and `745124634092896296`, are Brendon posts the same night in `#dice-tower`. Their text is item troubleshooting, "52 canon. I want oldman copper", and "wheres that con save tho". They do not state the airship condition. They remain in the record because Worker 2 listed them. They are not treated as support for the reward interpretation.

2. **W2-14 line coordinates.** Line 288 is the `### USER` marker. The user sentence "lets do this in a much more grounded way" is line 290. "I need less vibe writing" / "More wotc" is inside 1764–1798 (line 1770). An unhinged Tasha request is inside 1236–1497 (line 1238). "Need some of that unhinged back in the description" is line 1499, two lines after that window. The word "atmosphere" does not appear; "excessive atmosphere" is the worker's paraphrase of the grounded / less-vibe wording. The paraphrase was left in the record and is not a new claim.

3. **W2-10 outline.** `BCS-000064` is an outline in the cited window. The four prose strategies named in the observation are visible in BCS-000060 through BCS-000063. No revision order was invented.

4. **Comment counts.** Portable comments: 31 objects, 29 Brendon Faulkner, 2 Michael Kennish. BCE-000001: 78 comments. These counts describe different retrievals. They were not averaged.

No cited path was inaccessible. No cited native id was absent from the shard Worker 2 named. Nothing met the fail-closed condition of contradictory evidence that would require withholding a record. The exceptions above limit what the extra coordinates prove. They do not delete the records.

## Coverage

This was a bounded, cross-format, mixed-selection pass: source-family discovery, targeted comparison, and fixed-position live shards. It was not an exhaustive read.

Confirmed on this commit by `python3 scripts/validate_model_index.py`:

- Roanoke Season 3 projection: 197,013 messages.
- Empire City / Season 4 projection: 189,761 messages.
- Empire City Dev projection: 12,692 messages.

Worker 2 did not read those populations. The shards actually opened for this validation were `messages-0050`, `messages-0200`, and `messages-0350` in Season 3, and `messages-0009` and `messages-0087` in Empire City, plus the source files named above.

Inspected areas, as the payload defined them: early Roanoke settlement and economy; the Season 2 redesign note; Season 3 battle, aftermath, ordinary activity, and conditional rewards; Season 4 housing refusal and rubble permission; Season 5 published social contract and the provenance-limited editing notes; the 2018 bowling design; 2020 attributable manuscript comments; Bastion/Redoubt design; At War's End openings; Earthfall system text and the September 2026 encounter notes; the Saturday D&D workbench correction; and the existence of the Kit evaluation summary, which was not converted into a new historical record.

The sources do not have equal coverage, attribution, or real-play evidence. This tranche cannot support a corpus-wide behavioral frequency.

## Commands

Run from the repository root on the preservation branch, after these files were added:

- `python3 registry/validate_registry.py`
- `python3 scripts/validate_source_history.py --repo .`
- `python3 scripts/validate_model_index.py`
- `python3 scripts/validate_research_evidence.py --root .`

Results are reported in the pull request. The research-integrity validator is the Season 3 tranche gate. It was run to confirm this index edit did not drop the audit entry path. It does not audit these W2 records, and a pass does not verify them semantically.
