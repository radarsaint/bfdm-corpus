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

## Sample C, named before this read

Same cut as Sample A. The message on file line 100, then at most 40 later messages in that same channel inside the same shard.

- `model-index/discord/roanoke-season-3/messages-0101.jsonl`
- `model-index/discord/roanoke-season-3/messages-0201.jsonl`
- `model-index/discord/roanoke-season-3/messages-0301.jsonl`
- `model-index/discord/roanoke-season-3/messages-0375.jsonl`
- `model-index/discord/empire-city/messages-0300.jsonl`

These five were the next round indexes after Samples A and B. They were not opened to find a scene.

| Window | Channel | His posts inside the 40-row cut | Check against a false absence |
|---|---|---|---|
| S3 0101, line 100, 40 messages, 2020-07-26 22:02–22:32Z | `⚒-free-masons` | 18 | Not required. He is in the cut. |
| S3 0201, line 100, 29 messages, 2020-08-04 07:39–08:19Z | `🙋-out-of-character` | 14 | Not required. He is the line-100 post. |
| S3 0301, line 100, 40 messages, 2020-08-13 07:56–08:00Z | `château-de-léclipse` | 0 | He posted in that same channel 8 minutes before the cut and again 7 minutes after it. |
| S3 0375, line 100, 3 messages, 2020-08-20 08:50–15:38Z | `the-treehouse` | 0 | The channel has only those 3 messages from line 100 to the end of the shard. Within 15 minutes of the anchor, this shard has no post from him. |
| EC 0300, line 100, 21 messages, 2021-08-18 20:21–23:05Z | `public-library` | 9 | Not required. He is in the cut. The channel runs out at 21 messages. |

Thirty of the forty `château-de-léclipse` rows are Avrae dice lines. A cut full of dice is not a decision to leave the scene. The treehouse cut is too sparse to call absence or presence. No other shard was opened to fill it.

## DR-20261016-06 — A dice cut is not absence

**Type.** Sample result. Not a DM trait.

**Supported facts.** The table above.

**Interpretation.** Sample A showed that a line-100 anchor can open a channel he is not in. Sample C's château cut shows the opposite mistake: he can be in the channel and still be missing from the 40 rows, because the rows are the dice bot.

**Confidence.** DIRECT for these five shard files only.

**Scope.** These windows. Not a rate.

**Limitations.** The treehouse check stopped at this shard.

**Exclusions.** Do not teach Kit that a quiet stretch of the log is him choosing silence.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-07 — One Free Masons stretch

**Type.** One-channel inventory.

**Context.** `⚒-free-masons`, 2020-07-26, the Sample C cut. The line-100 post is a deleted account speaking Ebuc, not him.

**References.** `737067493625036822`, `737067755660116108`, `737067835603550228`, `737068074347528355`, `737068137236660245`, `737068757784199198`, `737069413139742823`, `737069706279649340`, `737069833362866245`, `737070131984859207`, `737071050608607242`, `737071226543144982`, `737071795043303495`, `737071922419990639`, `737072783527510156`, `737072991866847333`, `737073565173678160`, `737074097015619676`.

**Supported facts.** He asks "(roll deception?)" and "Traxim passive insight?" Traxim's player answers "(14)". He writes "(You notice the tell tale signs of deceit.)" The Archivist tells Ebuc to go on, names Sir Percival rather than Lugh as the more likely tormentor, and stoops with Ebuc. He writes "THEY ATE IT! STARS AND STONES!" and "(stars and stones is his curse word)". He asks "(hows the kit work, does he get to save?)". The Archivist gives the Grail sentence, says "Not for now Ebuc", and turns to Traxim's questions. Parentheticals: "(he helps Ebuc up)", "He waits until Ebuc is gone", "(cool. if you want to wait on the writing on the window, let me know. Can I go play amaya?)", and "got it". Traxim's player answers "(Yeah. Just @ me when someone needs to hammer on his head until he realizes he didn’t just find a riddle written on a window)". He pings user id `360967589511561218`. The Avrae row in this cut has empty `content`. This projection has no embed field.

**Interpretation.** In this stretch he runs the Archivist's lines, calls for two checks, and asks the player a question about a kit and a save. The save is not given a result here. "Kit" in that sentence is not identified as anything but the word he typed.

**Confidence.** DIRECT for the quotes. The deception result is not in this projection.

**Scope.** EVENT_SPECIFIC.

**Limitations.** Lines outside the 40-row cut were not used.

**Exclusions.** Do not turn "stars and stones" into a table rule. Do not invent the missing roll. Do not treat the Amaya question as a record that he left.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-08 — An item list is not a ban

**Type.** Ordinary out-of-character posts.

**Context.** `🙋-out-of-character`, 2020-08-04. The post on the line before the cut is also his: `740111490618621974`, a list that starts "Haste>Instant fortress>" and ends with counterspell.

**References.** `740111584676020226`, `740111637230649364`, `740111815333117982`, `740111891031916685`, `740112260986306610`, `740112602696384522`, `740112932754554880`.

**Supported facts.** Inside the cut he posts "Sword of Zariel", "Staff of the Magi", "He doesn't have to attack to win", "DORMOMU I HAVE COME TO BARGIN", "From inside I can hit you with magic mouth and skywrite to say what ever I want.", "Or if I wanted I could cast fabricate just to make a chili dog stand", and "magic circle, force cage and globe of invulnerability should be banned". Later in the same cut, after other people ask about Daysong, Solomon, Rope Trick, and Grimlock, he posts ">.>", "the real questions over here", "Shenanigens", "yes this", "I saw", "Thanks for adding to it", and "This is good." Those later lines answer `nobleindie`, not the item list.

**Interpretation.** "Should be banned" is one sentence in a list of item and spell jokes. This window does not show those spells removed from play.

**Confidence.** DIRECT for the quotes. "He" in "He doesn't have to attack to win" has no name in these posts.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not ban magic circle, forcecage, or globe of invulnerability from this sentence. Do not merge the Grimlock replies into the item list.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-09 — Two books, one per week

**Type.** One library exchange.

**Context.** Empire City `public-library`, 2021-08-18. `king.crusader` has Finn ask, by sign language, for Mason history, current Mason public works, the sending spell, and whether the library accommodates bardic knowledge.

**References.** `877673357913505843`, `877673610259628033`, `877674146610421781`, `877674239782690816`, `877675736922750987`, `877678300296777819`, `877679116512550924`, `877684243428425758`.

**Supported facts.** He offers two titles: "The Clock Tower conspiracy" and "The Grand Lodge of New Amsterdam." He writes "The spells available are any spells a wizard can learn with out taking extra feats." "Histories of the Masons are conspicuously missing." "One book per week may be researched." Asked "(do retainers get extras?)" he answers "(I'm not giving a lore dump for people's puppets, or every familiar and kegbot or boxdog will show up here.)" He then posts two paragraphs of the clocktower book: built overnight, traps and treasure, Elk's lodge acolytes and Oddfellows, doors at random times, "the most viscous traps", wealth, a possible test. Finn's player strikes a second checkout and writes "(wait nevermind, if only 1 book per week may be researched then he just has the clocktower to look through)". He answers "(Correct)".

**Interpretation.** The limit he states here is one book in a week, and he refuses the extra for retainers, familiars, and the two named puppet types. The clocktower paragraphs are the text he supplied for that book. They are not a separate ruling.

**Confidence.** DIRECT for those posts.

**Scope.** EVENT_SPECIFIC.

**Limitations.** Later library visits were not searched.

**Exclusions.** Do not apply one-book-a-week to every library. Do not treat the clocktower paragraph as a fact he asserted outside the book he was reading aloud.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-10 — Pie, before the dice cut

**Type.** Two sentences read while checking the château cut.

**Context.** `château-de-léclipse`, 2020-08-13, about eight minutes before line 100. The 40-row cut after that line is the pie fight's dice. These two sentences are not inside the cut. They were read because a zero-post cut had to be checked against the same channel.

**References.** `743375563460182037`, `743375912690778173`.

**Supported facts.** He writes "pie pvp is only enable against people who pick up a pie." Next he writes "(in the morning this will be clean and the building repaired, because warden reasons.)"

**Interpretation.** The first sentence sets who can be hit with a pie in this fight. The second says the mess is gone by morning and gives "warden reasons" as the because. Neither sentence states a rule for other fights or other damage.

**Confidence.** DIRECT for the two sentences.

**Scope.** EVENT_SPECIFIC.

**Limitations.** Not members of the 40-row sample. `BDC-S3-012` is a different day and a different sentence. It was not reopened.

**Exclusions.** Do not extend this to weapons, spells, or consent beyond pie. Do not invent what a warden is from the two words "warden reasons."

**KIT_CONSUMPTION.** NOT_APPROVED.

## Sample D, named before this read

Same cut as Sample A. File line 100, then at most 40 later messages in that channel inside the same shard.

- `model-index/discord/roanoke-season-3/messages-0051.jsonl`
- `model-index/discord/roanoke-season-3/messages-0151.jsonl`
- `model-index/discord/roanoke-season-3/messages-0251.jsonl`
- `model-index/discord/roanoke-season-3/messages-0351.jsonl`
- `model-index/discord/empire-city/messages-0250.jsonl`

| Window | Channel | His posts inside the cut | Check |
|---|---|---|---|
| S3 0051, line 100, 40 messages, 2020-07-22 22:30–23:10Z | `🧀-the-fat-friar` | 2 | He is in the cut. |
| S3 0151, line 100, 40 messages, 2020-07-31 00:01–00:12Z | `the-kvatch-hatch-memorial` | 2 | He is in the cut. Three more of his posts in this channel sit outside the cut. Their text was not read. |
| S3 0251, line 100, 40 messages, 2020-08-09 02:28–02:35Z | `hex-r-look-out-hill` | 19 | He is in the cut. Further posts of his in this channel outside the cut were counted, not read. |
| S3 0351, line 100, 40 messages, 2020-08-18 04:19–04:30Z | `team-2-tent` | 0 | Within 15 minutes he is posting in other channels in this shard, including `hex-e-falling-skies`. Those sentences were not written up. |
| EC 0250, line 100, 40 messages, 2021-08-01 02:03–02:25Z | `level-20-boss-takedown` | 0 | Within 15 minutes this shard has no post from him. The cut is other people. Other shards were not opened. |

## DR-20261016-11 — Two empty cuts, two different checks

**Type.** Sample result. Not a DM trait.

**Supported facts.** The table above. The Empire City cut's speakers are `effervescenteloise`, `mistahnoodles`, `divinedefault`, `damnzam`, and `minapoe`.

**Interpretation.** The tent cut is the Sample A case again: he is somewhere else in the same shard. The boss-takedown cut is not that case. This shard does not show where he was.

**Confidence.** DIRECT for these five files only.

**Scope.** These windows.

**Exclusions.** Do not call the boss-takedown silence a choice. Do not import the falling-skies lines into this record.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-12 — A roll of 10, then "bad tippers"

**Type.** Two sentences after a roll.

**Context.** `🧀-the-fat-friar`, 2020-07-22. `thatpersonlogan` tells him Wren is done with work for the day and worked 4 hours.

**References.** `735629861854642177`, `735629893911445566`, `735629967047786620`, `735630013063364620`.

**Supported facts.** Avrae posts a roll attributed to his user id: `1d400 (10)`, total 10. He answers "oof" and "a rough day with bad tippers". Wren's player then has Wren take her tips and begin to cry. He does not narrate that.

**Interpretation.** He glosses that roll as a bad tip day. He does not state a coin amount in these two sentences.

**Confidence.** DIRECT for the roll line and the two sentences. The command that produced the roll is not a separate row in this cut.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not build a wage table from this. Do not treat the crying as his narration.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-13 — "Don't worry about it"

**Type.** One parenthetical, plus an empty post.

**Context.** `the-kvatch-hatch-memorial`, 2020-07-31. Players are arguing whether to go after the hunger. `izarsystem` asks "(Why can’t the archivist help again?)" and "(How are we lampshading)".

**References.** `738547155442335785`, `738548652372656129`, `738548685884882996`, `738548699155660911`.

**Supported facts.** His earlier post in the cut, `738547155442335785`, has empty `content`. It replies to `738456797530161233`. This projection stores no embed. That parent was not opened. After the two questions he writes "(don't worry about it)". `effervescenteloise` then writes "(he could)" and "(he just doesn't think we can win)".

**Interpretation.** He declines those two questions. He does not, in this post, say why the Archivist will not help.

**Confidence.** DIRECT for the empty row and the parenthetical.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not teach Kit to refuse explanations. Do not fill in the empty post.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-14 — The pudding still hurts, and the sneak attack stays forgotten

**Type.** One combat exchange.

**Context.** `hex-r-look-out-hill`, 2020-08-09. `ozenannwn` has just said "sharpness dagger".

**References.** `741845519168700416`, `741845743354249217`, `741845851995111534`, `741845965400571945`, `741845980361785425`, `741846815552438332`, `741846903846600765`.

**Supported facts.** He pastes the Corrosive Form text: a touch or a melee hit from within 5 feet deals 4 (1d8) acid, and a nonmagical metal or wood weapon takes a cumulative −1 penalty to damage, destroyed at −5. The player asks "(so no damage since magic weapon but I take 4 damage?)". He answers "(it does the damage, but your weapon has a -1 bonus)". The player asks if it affects magic weapons. Another player pastes a magic-sword description. He writes "got it" and "so it is magical". Later the player says they forgot 2d6 sneak attack on the backstab. He answers "(sorry that I can't retcon selene)".

**Interpretation.** In this exchange a magic weapon still delivers the acid, and he still applies a −1 to the weapon. He does not revise the turn for the forgotten sneak attack. "−1 bonus" is the phrase he used.

**Confidence.** DIRECT for those posts. The pasted Corrosive Form text is what he posted, not a separate book citation checked here.

**Scope.** EVENT_SPECIFIC.

**Limitations.** The rest of this fight is outside the cut and was not read.

**Exclusions.** Do not make "no retcons" a standing rule. Do not apply this weapon result to other oozes.

**KIT_CONSUMPTION.** NOT_APPROVED.

## Not read, on purpose

The rest of each Sample A and Sample B shard. Season 2 live play, Season 5 live play, voice, and the held-out partition. The look-out-hill, free-masons, gigglewood, interrogation, and dice-tower posts from those windows were counted and not written up.

The beach, the oasis, the treehouse scene, the `#quotes` alliteration, and his other-channel posts in the 0101 and 0201 spans. Those were counted or skipped. Their sentences are not records.

Sample D's falling-skies loot lines, the tent's neighboring channels, and the look-out-hill posts outside the 40-row cut. Counted or skipped. Not records.

## Sample E, named and not opened

Same cut. Not read in this commit.

- `model-index/discord/roanoke-season-3/messages-0052.jsonl`
- `model-index/discord/roanoke-season-3/messages-0152.jsonl`
- `model-index/discord/roanoke-season-3/messages-0252.jsonl`
- `model-index/discord/roanoke-season-3/messages-0352.jsonl`
- `model-index/discord/empire-city/messages-0150.jsonl`

## Validation commands

- `python3 registry/validate_registry.py`
- `python3 scripts/validate_source_history.py --repo .`
- `python3 scripts/validate_model_index.py`
- `python3 scripts/validate_research_evidence.py --root .`

The last script guards the Season 3 audit entry path. A pass does not verify these rows.

Results on this branch, before the Sample D commit: `validate_registry.py` PASS; `validate_source_history.py` PASS (194 containers, 82 families); `validate_model_index.py` PASS; `validate_research_evidence.py` PASS.

