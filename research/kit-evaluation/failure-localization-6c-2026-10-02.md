# Failure localization: Kit in Area 6c (Stage 1)

**Date:** 2026-10-02 (PT)
**Scope:** KRABS v0.2.1 §27 failure localization over every Area 6c live playtest on record. No new play, no model calls, no `play` CLI.
**Reference spec:** `radarsaint/dnd-solo` main `15b2913`, `docs/architecture/KRABS.md` §27.
**Room contract:** `tests/scenarios/level-01-area-06c-uktarl.md` and `tests/fixtures/level_01_area_06c.json`.

## Sources examined

| Short name | File (dnd-solo `tests/playtests/`) | Header name | Evidence depth |
| --- | --- | --- | --- |
| **T1** | `2026-09-26-area-06c-nik.md` | "Kit playtest 02" | Narrative report + quoted trace fields. No packets or ledger. |
| **T2** | `2026-09-29-area-06c-voice-spec-nik.md` | "Kit playtest 03" | Exact transcript + quoted trace fields + timings. No packets or ledger. |
| **T3** | `2026-09-29-area-06c-claims-nik.md` + `...-claims-nik-evidence.json` | "Kit playtest 04" | Report + **evidence export**: 7 committed turns with full private traces (`improv_read`, `public_brief`, `detail`, `claims`), 10 timing records, 6 feedback notes, host interventions, final state. No raw prepared packets. |

Also read: `2026-09-29-claims-qa.md` (automated bridge QA, not a live playtest; not scored). In the corpus mirror `corpus/bfdm/research/kit-evaluation/`: `playtest-02-area-6c-gambling.md` (same session as T2), `playtest-02-followup-human-findings.md` (same session as T3; feedback matches T3's notes n4 to n15), `REGRESSION_TARGETS.md`, and `source-records/` (byte-identical to the dnd-solo copies). `playtest-01-character-onboarding.md` is not Area 6c and is excluded. No 6c playtest later than T3 exists on main.

**Naming hazard:** the corpus mirror calls T2 "Playtest 02"; dnd-solo calls T1 "playtest 02" and T2 "playtest 03". This file uses T1 to T3.

### How the categories were separated

KRABS §27 asks whether a failure is retrieval (A), salience (B), judgment (C), and so on. To tell them apart:

- **Was the fact in the packet?** On current main, `StateContext.context()` (`runtime/state_context.py` ~L843) places `level_context` (Uktarl vs. Harria and the extortion pressure), `room_rules` (10 gp toll, cheating, DC 13 key, DC 14 Insight), all unrevealed facts (marked deck, false vampires, key, stash), and full actor records (motives, knowledge, secrets) in every turn's `dm_context`. T3's traces show the room facts in use (for example, the opening's `marked_deck` fingerprint claim). I could not re-verify the packet at T3's tested commit `217fa76` from a raw packet, because none was exported. Treat "present in packet" for T3 as **inferred from the code and the trace contents**. For T1 and T2 it is inferred from the code lineage alone.
- **Did the private decision see it?** That comes from the `improv_read` and `public_brief` fields. If the decision never mentions an available fact that should have mattered, it is **B**. If the decision names the right concern but picks the wrong move, it is **C**. If the decision is sound but the spoken turn doesn't carry it, it is **F**.
- Without traces (T1's opening, for example), B, C, and F can't be cleanly separated. Those calls are marked *provisional*.

Each moment gets one primary category. Secondaries are noted where they matter.

## Moment log

### T1: 2026-09-26, Nik, staged prepare/decide/finish

**T1-1. Room opening read as an inventory.** *Primary F (provisional), secondary C.*
Quote (report): "The opening listed four pale card players, their coins, the fresco, tub, and south door."
What went wrong: The opening gave visible facts with no people in motion, no pressure, and no invitation. It was also narrated **outside the saved turn loop**.
Evidence: All of the facts were present, and they were what got delivered, so this is not A. There is no trace for this turn because it bypassed the loop, so B, C, and F can't be separated. The report itself diagnoses "the opening treated the room as an inventory". The actor-card and entry-frame fields that now exist did not exist then.

**T1-2. Insight ruling never saved; the next trace claims continuity it doesn't have.** *Primary E.*
Quote: "This ruling was made in chat and **was not saved in the SQLite turn history** ... The next private trace mentioned Nik's cautious look despite having no saved memory reference for it."
What went wrong: The 7 + 4 = 11 Insight roll and its result existed only in chat.
Evidence: The ledger lacks the event, and the trace's `memory_refs` was empty while its prose cited the event. The correct result was never represented, so this is E and not A.

**T1-3. Insight called for "are they friendly?" with no procedure behind it.** *Primary D.*
Quote: "The current room router lacks an operation for reading general intent, and the keyed DC 14 check covers the disguise rather than friendliness."
What went wrong: The check was improvised outside the procedures the runtime supports. That is why it couldn't persist (T1-2).
Evidence: The only keyed Insight is the DC 14 disguise check in `room_rules`, and the router had no intent-reading route. Neither knowledge nor intent was missing. The procedure was.

**T1-4. The dealer's first real line was a toll announcement.** *Primary F, secondary C.*
Quote: "Gambling? Cards, Nik. Passage is ten gold a head. If you came for something besides a game or a way through, I'm listening."
What went wrong: The NPC was flat. The player said: "The npcs were flat and lifeless ... its an it, not a she yet."
Evidence: The trace's `goal` was `npc_embodiment`, but the `public_brief` told the dealer only to name the toll. The decision named the right concern, and the carrier sent to the performer reduced it to a price. That is the definition of F. At that time the actor card had no voice, objective, tactic, or touchstone.

**T1-L. 81-second turn with process chatter visible.** *Outside A to I (§29 latency).*
Quote: "Worked for 1m 21s" / "First issue is how much time this takes."

### T2: 2026-09-29, `kit-voice-spec` 4dd3dc4, one-pass

**T2-1. Kit's aside contradicts the greeting in the same turn.** *Primary F.*
Quote: Dealer: "A guest at the turn of a card. How extravagantly lucky for us..." → Kit: "He could have said hello. Apparently there's no money in it."
What went wrong: A non sequitur joke that depended on forgetting what had just been said.
Evidence: The greeting is in the **same committed performance**, so retrieval, salience, and state are ruled out. The performer contradicted its own output, and the validator passed it, which also illustrates the §4.10 gate gap.

**T2-2. Router rejected Nik's in-character reply as an unsupported physical action.** *Primary D.*
Quote: Nik: "I was hoping to find. I dunno. An exceedingly hot elvin maiden..." → "The first `prepare` misclassified that unquoted answer as an unsupported physical action and recorded a refused attempt."
What went wrong: An obviously social reply was adjudicated as a refused action. The host replayed it prefixed with "I answer the dealer,".
Evidence: The player's declaration was intact (§4.3). The classification step produced the wrong adjudicative result.

**T2-3. "What game is it?" → high card, one card each, matching coin.** *Primary B, secondary C and D.*
Quote: "High card. A matching coin from each player. One card apiece. Highest takes the pot."
What went wrong: This flattened the marked-deck cheating encounter into a game with no decision in it (§13).
Evidence: The marked deck (unrevealed fact) and "lies and cheats for fun" (room rule) were in `dm_only`. The trace's `kit_choice` allowed "a small, playable wager" and the brief asked for "the simple stakes of the current hand". **Neither one references the deck or the cheating.** The fact was available and its relevance wasn't recognized, so the primary is B. The result also destroyed room structure (D) and was the wrong intervention (C).

**T2-4. Invented stakes became public canon with no state behind them.** *Primary E.*
Quote: "a matching coin" (no denomination) / "If Nik had accepted the offer, this slice has no durable wager, dealing, or payout adjudication."
What went wrong: Dialogue promised play the runtime couldn't carry, and the unsupported rule was elevated into public fiction (§4.5, §4.7).
Evidence: No wager or procedure object existed in world state. The validator checked shape and voice only.

**T2-5. Cheating had no in-play detection surface.** *Primary D.*
Quote: "No actual round, cheating move, observation opportunity, or check during gambling was available."
What went wrong: Hidden wrongdoing produced no discoverable evidence (Regression Target 10).
Evidence: This was a missing procedure (no cheat or watch mechanic existed at that commit; it was added before T3), not a knowledge gap.

**T2-L. 135.6 s, 132.8 s, and 96.5 s prepare-to-commit.** *Outside A to I (§29).*

### T3: 2026-09-29, `kit-claims-knowers` 217fa76, one-pass, full traces

**T3-1. Over seven turns, the toll, the fraud, and the Uktarl/Harria pressure never reached play.** *Primary B, secondary C.*
Quote (feedback n15): "The room has a point. The point was not evident."
What went wrong: The dealer never named the 10 gp passage price. No companion acted on its own want. Nothing signaled that this table controls passage.
Evidence: `level_context.pressure_here` ("The Undertakers extort newcomers ... Uktarl and Harria privately compete for control") and the 10 gp toll room rule were in the packet. The actor card lists "Name the price of passage" as a tactic. **All 7 committed traces have `story_anchor: scene`, `story_basis: scene_state`**, so the level anchor was never selected, and no brief mentions toll, passage, or rivalry. Available but never weighed means B. T1's dealer *did* name the toll, so the fact was retrievable.

**T3-2. "Do I know who this is?" → correct, but a slow non-answer.** *Primary C (minor).*
Quote: "You don't recognise the dealer, and he hasn't given you a name yet."
What went wrong: The ruling was right (no unearned identity). The player wanted "a simple no and then prompted a relevant check" (n4), and no check was offered (for example, Insight on the pale "vampires", DC 14 in the room rules).
Evidence: The trace understood the question (`fair_challenge`, `ruling`). The move left out the next playable handle, so this is C and not B or F.

**T3-3. The game became the scene's spine.** *Primary C.*
Quote: Dealer: "Three-Dragon Ante. The strongest ante dragon sets the gold; three rounds build your flight..." / Kit: "If you join, you can watch his hands. That's a Perception check."
What went wrong: The answer was a rules summary plus a meta check prompt. From here on, every brief served the minigame.
Evidence: The `kit_choice` was "Declare a playable dragon game ... bring the table into play", which was a deliberate move. The procedure itself was sound (cheat mechanic, detection surface), so this isn't D. The judgment to make the procedure the room's center was the failure, per n13: "Card games must remain optional."

**T3-4. Shield advantage assumed while seated at cards.** *Primary E, secondary D.*
Quote: "Roll Perception with advantage, +4, for his hands." → "Your Sentinel Shield grants Perception advantage while you're holding it."
What went wrong: This was an unsupported mechanical benefit (n10).
Evidence: The trace says "Nik's **loaded** advantage". The session sheet represented a conditional item benefit as an unconditional Perception advantage, and the host later removed it ("advantage_on": [] in final state). The state was wrong, and the ruling trusted it without checking the physical condition (secondary D).

**T3-5. The cheat discovery landed as raw engine output.** *Primary F.*
Quote: "Gambit 1: the dealer deals everyone up to six cards. Your hand: black 3, green 1, brass 2... You catch it: his eyes read the backs of the cards... (Perception 18 vs 7) Choose a card to ante."
What went wrong: The best earned moment in all three runs, catching the cheat, was delivered as a log line with a roll comparison and a menu prompt.
Evidence: The adjudication was correct and persisted (`cheat_seen: true`, `marked_deck` known). The automatic event text *was* the performance, so the internal result was sound and the delivery wasn't.

**T3-6. NPC wants collapsed into "ante up".** *Primary C, secondary F.*
Quote: Fresco-side player: "Keep your hands on your cards." / Door-side: "Don't start, please. Let him play." / Dealer: "One dragon face down, sir; give the table something worth fearing."
What went wrong: The companions had one line each, and everyone's objective was the next card (n8: "After the initial third-person description their personality fell flat").
Evidence: The brief's objective was "Keep the table moving toward the newcomer's ante." Kit *chose* game progression as the actors' goal even though the actor records carry motives (Uktarl: displace Harria; doppelganger: protect the arrangement). Selecting the wrong goal is C. The bandits' `communication_profile` is "Unestablished" in the fixture, which is an authoring gap that makes the F side harder.

**T3-7. "I play the game." stalled at "Name the card from your hand."** *Primary D.*
Quote: pending ruling "Name the card from your hand." / the guard rejected the clarification: "Padding: the turn recycles an earlier line ('1 brass 2 green 2 white 1 white')."
What went wrong: The procedure demanded a sub-choice instead of abstracting it, and the repetition guard blocked the hand reminder the player needed. No reply was ever committed.
Evidence: Timing record `07-clarification` was abandoned with `rejected_attempts: 1`. A validator false positive blocked a legitimate procedural reminder.

**T3-8. Natural inputs needed host rescue throughout.** *Primary D.*
Quote: "Host added `Rules question:` after direct Kit address and OOC: failed to admit a short ruling." / "'Whats the game?' did not trigger the detail oracle." / two session-only adjudicators for buy-in and card-watch.
What went wrong: Five of the seven committed turns needed host intervention to be adjudicated at all.
Evidence: See `host_interventions` in the evidence JSON. Every declaration was preserved verbatim. The routing to an adjudication path failed.

**T3-9. "What's going on besides the gambling?" → carving description + Perception check.** *Primary B, secondary F.*
Quote: "The mountain carving on the north wall draws the eye: dwarves tucked into caverns, with rays of sunlight spreading around the mountain... A closer look at the carving is a Perception check, +4."
What went wrong: The player explicitly asked for another avenue and got scenery and a roll. "Draws the eye" was asserted without a reason (n14), and the session ended.
Evidence: The trace had `actor_ref: none`, `story_anchor: scene`, and `kit_choice` "Spotlight the carved dwarven scene". The extortion and rivalry pressure that answers "what's going on" was in the packet (see T3-1) and wasn't weighed, so the primary is B. The thin description is the F secondary.

**T3-L. 92.7 s, 212.7 s, 187.0 s, and 211.5 s prepare-to-commit, and the reply length didn't justify the wait (n13).** *Outside A to I (§29).*

## Counts by primary category

| Category | Count | Moments |
| --- | ---: | --- |
| A Retrieval | 0 | none |
| B Salience | 3 | T2-3, T3-1, T3-9 |
| C Judgment | 3 | T3-2, T3-3, T3-6 |
| D Adjudication/procedure | 5 | T1-3, T2-2, T2-5, T3-7, T3-8 |
| E State | 3 | T1-2, T2-4, T3-4 |
| F Expression | 4 | T1-1, T1-4, T2-1, T3-5 |
| G Scene/concurrency | 0 | not exercised (single scene) |
| H Escalation/director | 0 | not exercised |
| I Publication | 0 | none (the T3 display shortening was deliberate and is documented) |
| Latency (§29, outside A to I) | 3 | T1-L, T2-L, T3-L |

**Total: 18 categorized moments and 3 latency findings.** Zero retrieval failures is itself a finding. In every case with a trace, the relevant fact was in the packet. Kit's problems start after retrieval.

## Recurring patterns

1. **The room's facts are present but never made to matter (B + C, 6 moments).** The marked deck was ignored when choosing the game (T2). The toll, fraud, and Harria rivalry never surfaced across T3's seven turns, and every trace's story anchor was `scene`. When the player asked what else was going on, Kit answered with scenery. When Kit did pick something, it picked the minigame as the scene's spine. This is the direct cause of "the point was not evident." Note: dnd-solo `52ab1c8` (2026-09-30 11:03 PT, after T3) added an agenda engine, backgrounded activities, salience, conditioned advantage, and natural routing. Those target patterns 1 and 3 and T3-4, but **no live 6c run has exercised them yet**, so every moment above is still open until a new run shows otherwise.
2. **The private decision is fine and the table hears something thinner (F, plus the F secondaries in C, 4+ moments).** T1 had `npc_embodiment` in the trace and a toll announcement in the output. In T3 the cheat discovery came out as an engine log line, the companions got one line each, and "draws the eye" came with no reason. The carrier (`public_brief`) keeps narrowing to the next mechanical step (toll, ante, roll). Validators check shape, not meaning: T2's self-contradicting aside passed, and T3's needed reminder was blocked.
3. **Natural play needs host rescue, and rulings fall outside state (D + E, 8 moments).** Social replies were misrouted (T2). OOC questions needed a `Rules question:` prefix, "Whats the game?" missed the detail path, and two session-only adjudicators were written mid-session (T3). An Insight ruling was never saved (T1). Invented stakes had no state (T2). A conditional item bonus was stored as unconditional (T3). Each one breaks the flow of play and costs wait time.

Also recurring: **latency in every run**, 81 s to 213 s per reply, with turns getting slower as more machinery was added (T1 81 s → T2 ~97 to 136 s → T3 ~93 to 213 s). §29 currently has no budget.

## Worst moments for Brendon's one-line answers

Each is phrased as "what would you have done at the table?"

1. **T2-3 (B).** Nik: "What game is it?" → Dealer: "High card. A matching coin from each player... Highest takes the pot." Kit ignored the marked deck when picking the game. *How do you answer "what game is it?" at this table?*
2. **T3-9 (B).** Nik: "What's going on in this room besides the gambling?" → Kit: "The mountain carving on the north wall draws the eye... A closer look is a Perception check." The extortion and rivalry were available and went unused. *What do you tell him is going on?*
3. **T3-6 (C).** After Nik joins: "Keep your hands on your cards." / "Don't start, please. Let him play." / Dealer: "One dragon face down, sir." Every NPC just wants the ante. *What do the other three want, and what does one of them say?*
4. **T3-5 (F).** Nik's 18 vs 7 catches the cheat, and it's delivered as "Your hand: black 3, green 1... You catch it: ...he gives himself the second card... (Perception 18 vs 7) Choose a card to ante." *How do you narrate him catching the second deal?*
5. **T2-1 (F).** Dealer: "A guest at the turn of a card. How extravagantly lucky for us..." → Kit: "He could have said hello. Apparently there's no money in it." *Does Kit say anything here, and if so what?*
6. **T1-4 (F).** Nik: "Whats going on here?" → Dealer: "Gambling? Cards, Nik. Passage is ten gold a head." *What's Uktarl's first real line to Nik?*
7. **T3-7 (D).** Nik: "I play the game." → Kit: "Name the card from your hand." The game stalled and nothing was committed. *Do you abstract the hand, and how?*
8. **T3-4 (E).** Seated at cards: "Roll Perception with advantage, +4... Your Sentinel Shield grants advantage while you're holding it." *What's the call: straight roll, ask if he's holding it, or something else?*

## Limits

- This is an analysis of three unblinded runs, all with the same player and character and no paired controls. Counts describe these runs, not Kit in general.
- The prepared packets for T3 were not exported, so "present in packet" relies on the current-main code and on T3's trace contents. A future playtest export should include the prepared `dm_context` for each turn so that B vs. A can be verified directly.
- T1's opening and T2's turns have only quoted trace fields, so B, C, and F splits there are lower-confidence.
- This file changes nothing in dnd-solo or any other corpus file.
