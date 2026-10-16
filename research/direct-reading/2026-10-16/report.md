# Direct reading — ordinary posts, 2026-10-16

**Status.** Draft. Not canonical until this pull request merges. Not a sample of the corpus. Not Kit configuration.

**Consumption.** `KIT_CONSUMPTION=NOT_APPROVED` on every row. `dnd-solo` was not edited.

**Identities.** `DR-20261016-*` ids are research-record ids. They are not BCS, BCE, or BCR ids. No source body, Discord projection, catalog row, or integrity verdict was edited.

**Held-out.** Prospective held-out items were not opened.

**Base.** `main` `2a650a735d8e39251979b157cf7aace9f8e443ef`.

A sentence below is included only where the cited row was read. `semantic_audit=NOT_PERFORMED`.

## Sample rule, fixed before the read

Brendon is Discord author `313689699627696139`.

Sample A. These shard files, the message at file line 100, then the next 40 messages in that message's channel inside the same shard. If the channel ran out, the window is shorter.

- `model-index/discord/roanoke-season-3/messages-0050.jsonl`
- `model-index/discord/roanoke-season-3/messages-0150.jsonl`
- `model-index/discord/roanoke-season-3/messages-0250.jsonl`
- `model-index/discord/roanoke-season-3/messages-0350.jsonl`
- `model-index/discord/empire-city/messages-0200.jsonl`

Sample B. These other shards. His first non-empty post at or after file line 200, then his later posts in that same channel until seven posts or the end of the shard.

- `messages-0075.jsonl`, `messages-0125.jsonl`, `messages-0225.jsonl`, `messages-0325.jsonl` (Roanoke Season 3)
- `model-index/discord/empire-city/messages-0100.jsonl`

Shards were chosen by round index. They were not chosen because a scene looked important.

## What the windows did

| Window | Channel | His posts in the window | Same minutes, other channel in the same shard |
|---|---|---|---|
| S3 0050, line 100, 40 messages, 2020-07-22 20:55–21:15Z | `🕍-the-roseline-temple-of-masons` | 8 | Not required. He is in the window. |
| S3 0150, line 100, 40 messages, 2020-07-30 21:43–22:00Z | `🙋-out-of-character` | 0 | 7 posts in `⚒-free-masons` |
| S3 0250, line 100, 11 messages, 2020-08-09 01:20–02:13Z | `🤖-bot-commands` | 0 | 100 posts in `hex-r-look-out-hill` |
| S3 0350, line 100, 37 messages, 2020-08-18 03:06–03:36Z | `hex-e-falling-skies` | 0 | 2 posts in `dice-tower` |
| EC 0200, line 100, 40 messages, 2021-07-27 04:00–04:20Z | `grove-keeper` | 0 | 1 post in `interrogation`, 5 in `gigglewood-glen` |
| S3 0225, entire shard, 500 messages, 2020-08-06 05:26–06:42Z | — | 0 in the shard | Sample B found no anchor. The other authors' text was not read. |

File-adjacent rows are not one channel. A missing post in the anchored channel is not a decision to leave play alone. In all four Sample A windows where he was absent, he was posting somewhere else in the same shard during the same minutes. Those other-channel scenes were not turned into records. Seeing them was the check against a false restraint claim.

`hex-e-falling-skies` in that window is players, `benevolentdm`, and Noah (`king.crusader`, "No enemies"). Those lines are not his. `grove-keeper` in that window is players talking about Niflhel, a speaker, and a prosthetic. Those lines are not his. Noah's Hunger explanation in the 0150 out-of-character window is Noah's, not his.

## Already on main, not reopened

- `735604604548546602` and the funeral scheduling are already `BDC-S3-L09`. Not a new record.
- `737751675762114581` is already `BDC-S3-012`. The reusable judgment on that case was overclaimed. It is not revived. The contested Dexterity line `737751942985678991` is already in the integrity review of that case. Not a new record.

## DR-20261016-01 — Channel absence is not restraint

**Type.** Sample result. Not a DM trait.

**Supported facts.** The table above. Counts are posts with his author id.

**Interpretation.** This draw does not show him choosing silence. It shows that a line-100 anchor often opens a channel he is not running.

**Confidence.** DIRECT for these nine shard files only.

**Scope.** These windows. Not a rate for Season 3 or Empire City.

**Limitations.** Five plus four shards are not the harvest. The other-channel text was used to test presence, then dropped.

**Exclusions.** Do not teach Kit to stay quiet because these channels had no post from him.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-02 — Roseline lines that are not the funeral case

**Type.** One-channel inventory.

**Context.** `🕍-the-roseline-temple-of-masons`, 2020-07-22, the Sample A window.

**References.** His posts in the window: `735603956478378154`, `735604604548546602`, `735604684290654292`, `735605667745759252`, `735605764038590546`, `735605836214173766`, `735605859521921054`, `735606048332709961`.

**Supported facts.** `735603956478378154`: "The smell of myrrh fills the temple as the Archivist prepares her body." `735605667745759252`, after AlfaMuffin's post that Kyrre identified the ooze and assumed the DDB text: "One time use lasting one day, no attunement needed." AlfaMuffin replies "(Got it)". Three later posts by him have empty `content` and no embed or attachment field in this projection. `735605764038590546` replies to the one-time-use post. `735605836214173766` replies to `735599943544471692`, his earlier note of three bottles of Kyrzin's Ooze, not ready until day 15. `735605859521921054` replies to `735600209790369792`, his note that everyone in last night's game is entitled to a piece of Ionaic Delight. `735606048332709961`: "A temple servant begins cleaning the blood from the steps." In the same window, players divide candy, whisper, and leave for a meeting. He does not narrate those beats.

**Interpretation.** Inside this window he adds a preparation image, one use-limit sentence, and a cleaning image. The empty replies have no stored text here. Do not invent images for them.

**Confidence.** DIRECT for the quoted lines. The use-limit sentence is his reply to that identify post. It is not a general item policy.

**Scope.** EVENT_SPECIFIC.

**Limitations.** The funeral sentences in this window belong to `BDC-S3-L09`. The Kyrzin's Ooze note and the Ionaic Delight note are reply parents just before line 100. They are not extra sample members.

**Exclusions.** Do not merge the day-15 fermentation note with the one-day use limit. They are different sentences.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-03 — One sentence about burning the store

**Type.** Ordinary out-of-character post.

**Context.** `🙋-out-of-character`, 2020-07-24. Just before it, `justjack420` says he wants to stop being the shopkeep and RP as Kiln. `mistahnoodles`: "There is no Kiln, only Jack."

**References.** `736344482999697499`.

**Supported facts.** He writes: "hey, i just offered to set the store on fire so kiln could get more screen time. kiln is dope og brunelock lore." The next same-channel posts are jokes (`736344717687521350` "A R S O N", and the lines through `736345152087654444`). No post in that stretch says the store burned.

**Interpretation.** None beyond the sentence. Screen time is his phrase for giving Kiln play. The arson is what he says he offered. This window does not show it done.

**Confidence.** DIRECT for the sentence and those next jokes.

**Scope.** EVENT_SPECIFIC.

**Limitations.** Later days were not searched.

**Exclusions.** Do not treat this as a tactic of destroying shops to force spotlight.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-04 — Stork talk is not a species ruling

**Type.** Ordinary out-of-character talk.

**Context.** `🙋-out-of-character`, 2020-08-15. `aerith_of_aer` has just said he doesn't know how fiends and kenku reproduce.

**References.** `744275533562380288`, `744275577674006627`, `744275624667119708`, `744276484402970794`, `744276568125472769`.

**Supported facts.** He posts "lol", "stork", "from stork", "A kenku with devil horns?", and "a fiend with flightless wings?" `nut_wizard` says "we have no idea" between the last two. `aerith_of_aer` jokes that Cato will suggest an omelet. Earlier in the same stretch he also posts "hello", "lol", "i mean", "i was up till 330" (`744275134063444098`, `744275382420635689`, `744275391396446259`, `744275416029724773`). Those four sit just before the sample anchor and were read because they are the same exchange.

**Interpretation.** These are questions and a joke in a conversation that already said the reproduction is unknown. They do not state a creature's biology as canon.

**Confidence.** DIRECT for the quotes.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not add a kenku-fiend ancestry to a setting from this exchange.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-05 — "How are you" gets a life answer

**Type.** Ordinary out-of-character reply.

**Context.** Empire City `out-of-character`, 2021-07-17. `starpilot94`: "How’re you doing Radar?"

**References.** `866097807630532638`, `866098081778106378`.

**Supported facts.** He answers: "Not bad. Chilling with other adult s irl. Its weird". Then: "I mean its post covid". `starpilot94` says "Wack". `minapoe` jokes about having to act like an adult.

**Interpretation.** Asked how he is, he answers about being with adults in person. This is not a ruling and not a creative-method statement.

**Confidence.** DIRECT for the two posts.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not infer a preference about play from small talk.

**KIT_CONSUMPTION.** NOT_APPROVED.

## Not read, on purpose

The rest of each shard. Season 2 live play, Season 5 live play, voice, and the held-out partition. The look-out-hill, free-masons, gigglewood, interrogation, and dice-tower posts were counted and not written up.

## Validation commands

- `python3 registry/validate_registry.py`
- `python3 scripts/validate_source_history.py --repo .`
- `python3 scripts/validate_model_index.py`
- `python3 scripts/validate_research_evidence.py --root .`

The last script guards the Season 3 audit entry path. A pass does not verify these rows.

Results on this branch, before commit: `validate_registry.py` PASS; `validate_source_history.py` PASS (194 containers, 82 families); `validate_model_index.py` PASS; `validate_research_evidence.py` PASS.
