# Direct reading — ordinary posts, 2026-10-16

**Status.** Unapproved draft. Not a sample of the corpus. Not Kit configuration. Not a certified practice.

**Consumption.** `KIT_CONSUMPTION=NOT_APPROVED` on every row. `dnd-solo` was not edited.

**Overlap.** DR-20261016-41 is the same three Empire City posts as RL-03 in `research/phase2/consolidation-longitudinal-2026-10-26.md`. It is not a second event.

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

Sample E's London, Roseline, Auntie Mavis, broom closet, Kvatch, lamplighter, and Golden Voice sentences. The engine-room rows inside the cut are other people. Not records.

## Sample E

Same cut. These files were named before the read.

| Window | Channel | His posts inside the cut | Check |
|---|---|---|---|
| S3 0052, line 100, 40 messages, 2020-07-22 23:56Z–2020-07-23 00:04Z | `🌁-london` | 0 | Within 15 minutes he posts in other channels in this shard. Those sentences were not written up. |
| S3 0152, line 100, 40 messages, 2020-07-31 01:36–01:46Z | `🎛-engine-room` | 0 | About 10 minutes before the cut, in this channel, he closes initiative. Those four posts were read. The cut itself is other people. |
| S3 0252, line 100, 40 messages, 2020-08-09 03:45–03:54Z | `hex-r-look-out-hill` | 18 | He is in the cut. Further posts of his in this channel outside the cut were counted, not read. |
| S3 0352, line 100, 14 messages, 2020-08-18 05:03–05:34Z | `town-square` | 0 | Within 15 minutes this shard has no post from him. The channel runs out at 14 messages. Other shards were not opened. |
| EC 0150, line 100, 40 messages, 2021-07-22 17:51–18:19Z | `the-golden-voice` | 0 | Within 15 minutes he is posting in other channels in this shard. Those sentences were not written up. |

## DR-20261016-15 — One cut is empty because he is elsewhere, one is empty in the shard

**Type.** Sample result. Not a DM trait.

**Supported facts.** The table above. Town square's speakers are `nobleindie`, a deleted account, and `sketchybee`.

**Interpretation.** London and the Golden Voice are the case where he is in another channel. Town square is the case where this shard does not show him. The engine room is neither: he spoke there before the cut.

**Confidence.** DIRECT for these five files only.

**Scope.** These windows.

**Exclusions.** Do not call the town-square gap a choice.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-16 — Initiative closed, no late entries

**Type.** Two posts read while checking an empty cut. Not inside the 40 rows.

**Context.** `🎛-engine-room`, 2020-07-31, about ten minutes before line 100.

**References.** `738567761436999731`, `738567780881924148`, `738568127641813102`, `738568159673712720`.

**Supported facts.** He posts the names "Baeshra Nico Wren Castor Pierce Wynne Traxim Web Rigatony". The next post has empty `content`. He writes "(closing init. No late entries.)" The next post is empty again. This projection stores no embed on either empty row.

**Interpretation.** He closes that initiative and says no late entries. The forty rows after line 100 do not contain another post from him.

**Confidence.** DIRECT for those four posts.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not turn one close into a rule that late arrivals never join a fight. Do not fill the empty posts.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-17 — Later on Look Out Hill

**Type.** One combat slice. Not the pudding exchange.

**Context.** `hex-r-look-out-hill`, 2020-08-09, 03:45–03:54Z. `DR-20261016-14` is earlier the same night and was not reopened. `hekiryuu` asks how large the cleanroom is.

**References.** `741864858097811477`, `741865667720118293`, `741865752650448938`, `741865820975530085`, `741865846544269382`, `741866014920146975`, `741866066908807279`, `741866266268270606`, `741866330579271743`, `741866361663520798`, `741866378184622261`, `741866422510026758`, `741866948375347243`.

**Supported facts.** He answers "20X20". After "Flurry of Chomp" he writes "hit, it tastes soapy" and "bashra washes their mouth out with detergent". `hekiryuu` describes a silent image on the walls and floor of a 15×15×15 corner. He answers "(sure)". Asked "(Is the monster making concentration checks?)" he answers "(the monster actually doesn't need to)". He writes "Roll d20+!" and then "Roll 1d20+1". Avrae shows `1d20 (2) + 1`, total 3, on his user id. He writes "it fails" and "Kloroxx yells nooooooo". After Kloroxx targets Sandi, a hit is called by `hekiryuu`, and an `8d8` total of 34 is shown, he writes "(he doesn't use eyes to see)".

**Interpretation.** The room size, the soapy bite, the waived concentration check, the failed roll, and the eyes line are this slice. The parenthetical does not name who "he" is. The posts before it are Kloroxx's attack. No difficulty class is stated for the roll of 3.

**Confidence.** DIRECT for the quotes. The two Avrae totals are the rows as stored.

**Scope.** EVENT_SPECIFIC.

**Limitations.** Posts outside this cut were not read. Turn-calls in the cut ("pass", "hit", "got it", "bae", "web") are not separate claims.

**Exclusions.** Do not export 20×20, detergent, or eyeless sight to other fights. Do not merge this with the pudding ruling.

**KIT_CONSUMPTION.** NOT_APPROVED.

## Sequence closed

Sample F was the next named cut. After it, the same cut was applied to every remaining file in the four counters, and to the two Empire City files still on the 50-step.

- Sample F: Season 3 `messages-0053`, `0153`, `0253`, `0353`, and Empire City `messages-0350`.
- Then Season 3 indexes 54–99, 154–199, 254–299, and 354–395, where the file exists.
- Empire City `messages-0050`.

`messages-0395.jsonl` has 13 lines. It has no line 100. That is the short file.

186 windows. 66 contain a post of his. 12 contain none, but he posted in that same channel within 15 minutes, and those posts were stored. 72 contain none, and he posted in another channel in the shard; those other-channel sentences were not stored. 35 contain none, and this shard has no post from him within 15 minutes. That last class was not called a choice.

Every stored post is in [sequence-windows.jsonl](sequence-windows.jsonl). A turn-call ("hit", "got it", a name) stays there and is not given its own record below. The records are the sentences that set a limit. They are not a model, and they do not expand the twenty Season 3 judgments.

## DR-20261016-18 — The counters are finished

**Type.** Sample result. Not a DM trait.

**Supported facts.** The counts above. The file list is the JSONL.

**Interpretation.** This is the end of this counter sequence. It is not a reading of every shard.

**Confidence.** DIRECT for these 186 files only.

**Scope.** These windows.

**Exclusions.** Do not treat a shard with no post from him as silence. Shards outside these indexes were not opened.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-19 — The banner's gift does not destroy the chisel

**Type.** Parentheticals after a pasted item.

**Context.** `leafs-lookout`, 2020-08-09. He posts a long banner description, message `741920057021562913`, including a Gift of Battle that destroys the banner after 8 hours.

**References.** `741920316082618380`, `741920617766322232`, `741920737555775550`.

**Supported facts.** He writes "(the chisel is not destroyed however for the gift of battle)", "(this one of the most powerful artifacts in the game)", and "(you can use the gift more than once. it just takes 8 hours of set up)". He also writes "(welcome to the masons)" and "(the hunger)".

**Interpretation.** The parentheticals change the pasted gift: the chisel survives, and the gift can be used again after another 8 hours. "The hunger" is two words. They do not say what the hunger is.

**Confidence.** DIRECT for those sentences. The banner paragraph is his paste, not a book checked here.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not give this banner to another table from this window.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-20 — Nothing hidden, and still something off

**Type.** One bunny scene.

**Context.** `a-hatch`, 2020-08-18. He has described 30 bunnies and "This is fine."

**References.** `745385629629546567`, `745385663767249056`, `745385811301892200`, `745386419253542954`.

**Supported facts.** He asks "true sight doesn't give you information about creatures, right?" He then writes "there is nothing hidden or invisible" and "but there is something off about these bunnies". A later check in the same cut is "dc 19".

**Interpretation.** The question is a question. The two statements are what he asserts about that scene: nothing hidden or invisible, and something off about the bunnies. The DC is for the sleight-of-hand call just before it.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not answer his question about truesight from this window. Do not export DC 19.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-21 — A commoner is all 10s

**Type.** Out-of-character stat directions.

**Context.** `🙋-out-of-character`, 2020-08-09.

**References.** `742127507536347186`, `742127694300446771`, `742128077089276061`, `742128296266825900`, `742128319247679538`.

**Supported facts.** He writes "it be all 10s", "get ready to die to some cr 1/4", "Make sure to take a set of tools", posts `https://roll20.net/compendium/dnd5e/Commoner#content`, and "feel free to roll for hp". He also writes "actually I need to adjust one thing" with no statement of the adjustment in that post.

**Interpretation.** For this commoner, the abilities are 10s, tools are required, and hit points may be rolled. The adjustment is unnamed here.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not treat "die to some cr 1/4" as a promise about every fight.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-22 — Call the end of your turn, and the plant is not blind

**Type.** Two combat asides.

**Context.** `a-hatch`, 2020-08-18, later than the bunnies.

**References.** `745407684018438145`, `745407878051004456`.

**Supported facts.** He writes "you never called eot" and then "go ahead". He writes "(tremorsense and truesight. I don't do blind as plantman)".

**Interpretation.** In this stretch, skipping the end-of-turn call is noticed, and the turn is allowed to continue. The sense line is about the plantman in this fight.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not make "never blind" a rule for every plant.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-23 — Consent to contest is not consent to be rescued

**Type.** One parenthetical. Not the observation-deck case.

**Context.** `hex-b-leviathans-call`, 2020-08-03. The same cut includes a dexterity comparison, "who wants to call it, high or low", "web called first", people pushed back, and "35 feet and counting."

**References.** `739693279901122560`.

**Supported facts.** He writes "(lol consent to contest. not consent to be rescued.)"

**Interpretation.** This sentence splits contesting from being rescued. `BDC-S3-012` is a different day and a different sentence. Its reusable judgment stays overclaimed. This line does not revive it.

**Confidence.** DIRECT for this sentence.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not promote this to a standing consent rule. Do not merge it into the twenty.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-24 — Pairs in the woods

**Type.** One aside during a drag.

**Context.** `hex-m-howling-woods`, 2020-08-03.

**References.** `739952415637504001`.

**Supported facts.** He writes "(Roanoke is dangerous. pairs of people walking in the woods are likely to get killed with smaller party sizes. I threw out dire bears and other such things yesterday.)"

**Interpretation.** He describes that day's woods and says he used dire bears the day before. "Likely" is his word for small parties. It is not a measured rate.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not spawn dire bears because this sentence exists.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-25 — The lake's clock

**Type.** Four limits in one underwater stretch.

**Context.** `hex-l-lake-of-woes`, 2020-08-12.

**References.** `743242729487859853`, `743243763404636291`, `743244812471238767`, `743244923662499944`.

**Supported facts.** He writes "make a death save, don't roll a 1". He writes "(underwater, drowning rules begin, don't worry minutes take forever in dnd)". He writes "(end encounter until 6, take a short rest)" and "(max healing on hit die)".

**Interpretation.** The death-save line tells the player what not to roll; it does not show the die. Drowning starts, and he says minutes are long in the game. The encounter stops until 6, with a short rest and maximum healing on hit dice.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not apply maximum hit-dice healing to every rest.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-26 — The mainland entrance, and sinking is not receding

**Type.** Place and schedule.

**Context.** `town-hall`, 2020-08-12, and `hex-l-lake-of-woes`, 2020-08-13.

**References.** `743203172532748321`, `743307210721067119`, `743307278220001321`, `743307547900903496`.

**Supported facts.** He writes "(the closest entrance to the feywild is on the main land.)" He writes "The island has stopped sinking." Then "(but this isn't the same as the waters receeding)" and "(for times sake, yes, lets not have endless meetings.)"

**Interpretation.** One entrance is named, on the mainland. Stopping the sink is distinguished from the water receding. The meeting line is about that day's time.

**Confidence.** DIRECT. Spellings are his: "main land", "receeding".

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not invent other feywild entrances. Do not treat the meeting line as a ban on planning.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-27 — Inside the hunger

**Type.** One voice-event round.

**Context.** `week-5-voice-event-main`, 2020-08-22.

**References.** `746559816515977358`, `746560671977701486`, `746561550634188821`, `746561777722195989`.

**Supported facts.** He writes "Ozgur is inside the beast." "You will take bite damage for entering." "(at the top of the hunger's turn if you are still inside, skitter and ozgur take 3d6 acid.)" "(ozgur is still blinded and restrained, but for his bold courage, skitter is not.)"

**Interpretation.** Entering costs a bite. Staying inside until the hunger's turn costs 3d6 acid to those two. Ozgur stays blinded and restrained. Skitter does not, and the reason he gives is "bold courage."

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not reuse 3d6 or "bold courage" for a different creature.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-28 — Solomon, Rah, and a question for Rob

**Type.** Two parentheticals. Not the observation-deck PvP case.

**Context.** `🔭-the-observation-deck`, 2020-07-31.

**References.** `738662396838543373`, `738662553529352213`.

**Supported facts.** He writes "(Solomon isn't done with you. The precedent set with Rah for spilling secrets is rough.)" and "(I'll talk to rob and get his input)".

**Interpretation.** He points at a prior precedent and says he will ask Rob. The precedent is not quoted here. `BDC-S3-012` was not reopened.

**Confidence.** DIRECT for the two sentences. What Rah did is not in this cut.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not invent the Rah scene. Do not record Rob's answer. It is not in this window.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-29 — No one in melee

**Type.** One targeting sentence.

**Context.** `hex-i-wychwood-forest`, 2020-08-03. He has asked "(who is in melee?)".

**References.** `739968197603754086`.

**Supported facts.** He writes "with no one claiming melee, the beast scampers up to the last person to attack it."

**Interpretation.** In this round, an unclaimed melee means the beast goes to the last attacker.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not make "last attacker" the default for every monster.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-30 — Meteorites, demons, and co-DMing

**Type.** Three separate asides. Not one doctrine.

**References.** `742109487137292420` in `⚒-free-masons`, 2020-08-09. `736790327322476644`, `736790623365103646`, and `736791077293522945` in `🌚-bulwark-hallways`, 2020-07-26. `743267369761112125`, `743267432273150062`, `743267468310740996`, `743267487264669736`, and `743267528926691440` in `🙋-out-of-character`, 2020-08-13.

**Supported facts.** "(meteorites aren't stars, copper)". "the contract is so magical that its hard to see anything else". "(no, im just playing the world)". "(to be clear. the lesser demons give valuble things)". "Where as there is a novel of world building just sitting in mason chat". "secrets". "I know what noah is doing." "and its good story telling". "I have never been so happy to co-dm with some one".

**Interpretation.** Meteorites are not stars, in that correction. The contract hides other details. Lesser demons give valuable things, spelled as he spelled it. He says he is playing the world, not a character, in the Astella aside. He praises Noah's storytelling and says he is happy to co-DM. He does not describe Noah's method beyond "secrets" and "good story telling."

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC. Three windows, not one practice.

**Exclusions.** Do not turn the co-DM sentence into a division of authority. Do not stock every demon with treasure from this line.

**KIT_CONSUMPTION.** NOT_APPROVED.

## The rest of the two harvests

The counter sequence left the other shard indexes unread. Those files were then cut in index order. Same rule. `empire-city-dev` was not opened.

568 windows. 140 contain a post of his. 15 contain none inside the cut, and he had posted in that channel within 15 minutes; those posts were stored. 197 contain none, and he was in another channel; those sentences were not stored. 216 contain none in that shard within 15 minutes. That was not called a choice.

Three files had lines that are not valid JSON. Those lines were skipped, not repaired: 14 in Season 3 `messages-0143`, 13 in `messages-0144`, and 2 in Empire City `messages-0242`. The other rows in those files were read.

Every stored post is in [rest-windows.jsonl](rest-windows.jsonl). Turn-calls and scene lines stay there. The records below are the sentences that set a limit. They do not expand the twenty.

## DR-20261016-31 — Blooming is not producing

**Type.** One spell reading, outside the cut.

**Context.** `🙋-out-of-character`, 2020-07-19, within 15 minutes before the line-100 cut. Read because the cut itself had no post from him.

**References.** `734249740803506221`.

**Supported facts.** He writes "You arent even producing the flowers, your just making them bloom per the wording of the spell. Totally cool."

**Interpretation.** For that spell, in that exchange, making flowers bloom is allowed and is not the same as producing them. Spellings are his.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not apply this reading to a different spell.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-32 — The manor lamp, and lore he does not know

**Type.** Two separate limits.

**References.** `734514829175554149` in `🏚-twilight-manor`, 2020-07-19. `735449559890919525` in the same channel, 2020-07-22.

**Supported facts.** "A new Gas lamp appears next to the manor. Gas lamp for gas lighting. No one will be able to remember future attacks on the Manor even when I'm not on the server." "(I can only give out lore that I know. If its from another dm, I may have to recluse myself)".

**Interpretation.** The lamp sentence is what the new lamp does, including attacks he is not present for. The later parenthetical limits lore to what he knows, and says another DM's lore may make him recuse himself. "Recluse" is his spelling.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC. Two days, not one policy manual.

**Exclusions.** Do not erase memory of every attack in every building. Do not treat recusal as automatic.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-33 — The White Hart is not tracked

**Type.** One parenthetical.

**Context.** `highgate-cemetery`, 2020-07-22.

**References.** `735399230406918214`.

**Supported facts.** "(Baeshra will never find tracks, the White Hart can only be hunted by those who are not looking)".

**Interpretation.** In this sentence Baeshra's tracking fails, and the hunt is restricted to people who are not looking.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not make every hunt fail for a tracker.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-34 — Duck points, meta, and a one-use vial

**Type.** Three small corrections.

**References.** `738234461057056808` in `duckton`, 2020-07-30. `738250294693199926` in `🎛-engine-room`, the same night. `743879427607363685` in `the-wastewater-weaver`, 2020-08-14.

**Supported facts.** "per the raw they do not. Call it a duck point instead". "(no more meta)". "(This is a one use small vial. Dont worry about other things)".

**Interpretation.** Something in the rules text does not apply, and he renames the remainder a duck point. Meta talk is stopped in that engine-room moment. The vial is one use, and he declines the other questions.

**Confidence.** DIRECT. The thing the RAW does not do is the prior line, which is a question, not restated here.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not invent a duck-point economy. Do not ban table talk from one parenthetical.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-35 — The meteorite, locked to Baeshra

**Type.** An item, then a lock.

**Context.** `town-square`, 2020-08-14. The lock line is outside the cut, same channel, within 15 minutes. The item line is inside the cut.

**References.** `743926717105700924`, `743927902218748025`.

**Supported facts.** "(locked for Baeshra only)". "When Identified and attuned, this meteorite of the Kaiju will allow you to cast Enlarge/reduce 2 times per day. As well as dragon's breath 4 times per day."

**Interpretation.** That meteorite has those two daily limits, and he had just locked it to Baeshra.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not hand the meteorite to anyone else from this window.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-36 — A reaction still requires the save

**Type.** One ruling, labeled by him.

**Context.** `hex-e-falling-skies`, 2020-08-18.

**References.** `745098518317891585`.

**Supported facts.** "(this is causing a bottle neck, and going against the spirit of suggestion. dm rulling, you can't take a reaction with out making the save. otherwise I'd have to let everyone else use your reasoning.)"

**Interpretation.** He calls this a DM ruling for that bottleneck. A reaction is not available unless the save is made. "Rulling" is his spelling. The spell named in the sentence is suggestion.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not extend this to every spell that offers a save.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-37 — One coupon, and the sandwich job

**Type.** Two Empire City limits.

**References.** `863520655952576512` in `the-dock`, 2021-07-10. `863527523894558731` and `863527778467840012` in `coppers-sandwiches-🥪`, the same night.

**Supported facts.** "(There was only 1 coupon, no more need to roll)". "(You may have a job here that earns 2 gold per day 5 days a week, you may not moon light at other establishments. Maximum 1 despondent server, 1 sus janitor, and 1 overwhelmed cook.)" "(Yes, 8 hours for 2 gold, cannot overlap with your long rest.)"

**Interpretation.** The coupon does not get another roll. The job pays 2 gold for 8 hours, five days, does not share a clock with a long rest, and forbids a second job. The staff caps are those three roles.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not set every wage in Empire City from this shop.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-38 — Rule 1 applies to him

**Type.** Server-time rule.

**Context.** `fountain-of-spam`, 2021-07-12.

**References.** `864145755031470081`, `864146577438015498`, `864146910449369098`.

**Supported facts.** He writes "Rule one". Then "Tim. If you don't get 8 hours off the server, Bo will take a rank of exhaustion." Then "But rule 1 is for even me."

**Interpretation.** Missing 8 hours off the server costs Bo one rank of exhaustion, and he says the rule binds him too.

**Confidence.** DIRECT. The text of server rule 1 is not pasted in these three posts.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not invent ranks beyond the one he named.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-39 — Puns are not illegal

**Type.** One correction of a joke.

**Context.** `out-of-character`, 2021-07-12.

**References.** `864250822446940250`.

**Supported facts.** "The running joke is that puns are banable depending on how groan worthy they are. It is not actually illegal. Just remember, if you entertain yourself by making us groan, I reserve the right to entertain myself by making you groan."

**Interpretation.** He separates the joke from a rule. Puns are not illegal. He keeps a right to answer a groan with a groan.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not write a punishment table for puns.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-40 — Obstacles are not there to stop play

**Type.** Two posts and a link.

**Context.** `out-of-character`, 2021-07-16. Both posts are outside the line-100 cut, same channel, within 15 minutes.

**References.** `865474136716345365`, `865474608361766920`.

**Supported facts.** "I don't put obstacles out there to keep you from playing." "This sounds like you are intimidated. Not that there was in game reasons. I can't have a game with out players. And I direct you to server rule 1 https://discord.com/channels/850779382791536640/850795683534602251/850795988486586448"

**Interpretation.** He denies that the obstacles are meant to stop play, says he cannot run a game without players, and points at server rule 1. The page at that link was not opened.

**Confidence.** DIRECT for the two sentences. Not for the rule text behind the link.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not remove obstacles from play because of this denial.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-41 — The 25% / 75% rule

**Type.** Three posts about what this server is not.

**Context.** `fountain-of-esteem`, 2021-07-16.

**References.** `865744435732283392`, `865745512719974410`, `865746119207026715`.

**Supported facts.** "The 25% 75% percent rule is my way of begging the community to understand that this is not dominion level play. That we have to have some linear rails. That we are telling a story and that story sometimes means that despite their exploits and tricks, the game must move forward and can't always swing to adjust for players who can out wit us? I'm absolutely not as good at this game as some of my players. Noah, devon, ethan. But just Because, I might not be able to out wit them on the fly, should major game play plans be scrapped on the fly?" Then "And its not their fault that this game can't swerve like a home game". Then "But it can't ever be real dnd. The expectations are something I have tried to address. I poured my heart into the server rules. And I don't know how to commicate it better? We might be bumping up against my autism here."

**Interpretation.** He names a 25% / 75% rule as his plea for rails: the story moves, and a plan is not scrapped on the fly because a player outwits him. He says that is not the players' fault, and that this game cannot swerve like a home game and cannot be "real dnd." He does not, in these three posts, define which 25% or which 75%.

**Confidence.** DIRECT for the sentences. The percentage split is not defined here.

**Scope.** EVENT_SPECIFIC.

**Exclusions.** Do not invent the missing split. Do not treat "not real dnd" as a ban on using the books.

**KIT_CONSUMPTION.** NOT_APPROVED.

## DR-20261016-42 — No wild shape, no persuasion, silence fails, plots stay hidden

**Type.** Four separate sentences.

**References.** `867288868185440296` in `kingsbridge-ring-road-lamps`, 2021-07-21: "(no wild shape)". `868006105786232852` in `sandys-umbral-cup`, 2021-07-23: "go for it apgan. (dox, in this case this person is being unreasonable and therefor cannot be persuaded. Perhaps in a moment rephrase as an intimidation or deception.)" `879587149727539211` in `fontaine-de-florian`, 2021-08-24: "silence doesnt work". `879471038461796442` in `out-of-character`, 2021-08-23: "Dont give away plots".

**Supported facts.** Those four sentences.

**Interpretation.** Wild shape is refused in that lamp scene. That person cannot be persuaded, and he offers intimidation or deception instead. Silence does not work on Finny in that moment. Plots are not to be given away in that scheduling talk.

**Confidence.** DIRECT.

**Scope.** EVENT_SPECIFIC. Four windows.

**Exclusions.** Do not ban wild shape, persuasion, or the silence spell at every table.

**KIT_CONSUMPTION.** NOT_APPROVED.

## Not read, on purpose

The rest of each Sample A and Sample B shard. Season 2 live play, Season 5 live play, `empire-city-dev`, voice beyond the rows inside these cuts, and the held-out partition.

The beach, the oasis, the treehouse scene, the `#quotes` alliteration, and the other-channel sentences already left unstored.

The unparseable lines in `messages-0143`, `messages-0144`, and Empire City `messages-0242`.

## Validation commands

- `python3 registry/validate_registry.py`
- `python3 scripts/validate_source_history.py --repo .`
- `python3 scripts/validate_model_index.py`
- `python3 scripts/validate_research_evidence.py --root .`

The last script guards the Season 3 audit entry path. A pass does not verify these rows.

Results on this branch, before the rest-of-harvest commit: `validate_registry.py` PASS; `validate_source_history.py` PASS (194 containers, 82 families); `validate_model_index.py` PASS; `validate_research_evidence.py` PASS.



