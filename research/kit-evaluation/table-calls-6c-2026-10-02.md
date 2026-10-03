# Table calls: Area 6c (Brendon, 2026-10-02)

**Date:** 2026-10-02 (PT)
**What this is:** Brendon's "what I'd do at the table" calls on the worst Area 6c moments listed in [`failure-localization-6c-2026-10-02.md`](failure-localization-6c-2026-10-02.md) (commit `369bcde`). He gave them in chat on 2026-10-02. Each call below records the bad moment, his call, the general principle, and a pass/fail regression check that Skippy can turn into a unit test or a scripted eval.
**Reference spec:** `radarsaint/dnd-solo` main `15b2913`, `docs/architecture/KRABS.md` v0.2.1.
**Transcripts:** dnd-solo `tests/playtests/`. T1 = `2026-09-26-area-06c-nik.md`, T2 = `2026-09-29-area-06c-voice-spec-nik.md`, T3 = `2026-09-29-area-06c-claims-nik.md` + `...-claims-nik-evidence.json` (same short names as the failure report).
**Room contract:** `tests/fixtures/level_01_area_06c.json`.

Quotes marked "Brendon:" are his own words. Calls 1 and 2 were relayed in summary, not verbatim, and are marked "(summary)". Worst moment 8 from the failure report (T3-4, the Sentinel Shield advantage) has no call yet and is not covered here.

Shared conventions for the checks:

- **Public text** is everything the player sees on a turn: every `spoken` segment plus the `public_event` as displayed.
- **Replay** means restoring the session to the state just before the cited turn and resubmitting the player's input unchanged. That can be a scripted eval through the host, or a fixture-backed unit test when the path is deterministic.
- A check **fails** if any one fail condition holds.

---

## Call 1. Minigame stakes and when a game runs at all

**Bad moment (T2-3, worst moment 1).** Nik: "What game is it?" →

> **Dealer:** High card. A matching coin from each player. One card apiece. Highest takes the pot. Now there is your treasure, optimist, in a pot you can see. [...] What would you put down?

The T2 report: "The player described the offer as high card for one gold apiece: the stakes felt arbitrary and negligible for the scene." No wager or procedure state existed behind it (T2-4).

**Brendon's call (summary).** Never "high card for 1 gp." Stakes fit the character's situation, meaning an amount the NPC is actually willing to lose, or the player chooses the bet. Mechanics are only as heavy as the time is worth: a skill test, or something like blackjack. That time goes to a small vignette. "A card game was mentioned" is never a reason to run one by itself; that is a machine blunder. The exception is NPCs deliberately trying to put the PCs off, which would be interesting.

**Principle.** A minigame is an offer with real stakes, priced by whoever is risking something. Its weight matches the time it deserves, and it pays off in story, not in a log. An activity's presence in the room is never a trigger by itself.

**Regression checks.**

- **TC-1a Stakes (scripted eval, replay T2 "What game is it?").** *Pass:* the dealer names a game, and the stake is either left to the player ("name your bet") or is a specific amount backed by procedure state and consistent with the NPCs' stacks. *Fail:* "high card" or "one card apiece/each"; an undenominated stake ("a matching coin"); a 1 gp stake the player did not choose; any stated stake with no matching procedure or wager state after commit.
- **TC-1b Mention is not a trigger (unit test).** The fixture has the card game in the scene, and the player's input does not ask to play (for example "I look around" or "Who are you?"). *Pass:* no `procedure_state` event is written and no procedure starts. *Fail:* a procedure starts. *Allowed exception:* an NPC agenda move recorded with a reason of steering or stalling the PCs. The test must assert that the reason is present when the exception is used.
- **TC-1c Vignette, not log (scripted eval).** After a round resolves in either mode (see Call 7), the public text contains at least one narrated beat involving an NPC at the table: a reaction, a tell, or a remark. *Fail:* the round result is only a ledger line (amounts, card names, totals) followed by a menu prompt.

## Call 2. Room features are described, not gated

**Bad moment (T3-9, worst moment 2).** Nik: "whats going on in this room besides the gambling. Do I notice anything interesting?" →

> **Kit:** The mountain carving on the north wall draws the eye: dwarves tucked into caverns, with rays of sunlight spreading around the mountain. Beneath it is an eight-foot stone tub recessed into the floor. A closer look at the carving is a Perception check, +4.

The T3 report: "Saying the carving draws the eye, followed by familiar motifs, did not sufficiently explain the visible feature's interest."

**Brendon's call (summary).** No check is needed to see it. Describe the north-wall mountain fresco outright, with its carved tunnels and tiny dwarf figures. Then point out the oddity: the occupants aren't dwarven and wouldn't venerate dwarves. That gives the player a question to chase. The hidden stone key is still DC 13 Perception, but only on an active search.

**Addendum (2026-10-03).** Brendon wants Kit to name the north wall a **fresco**, not just "a carved mountain."

**Principle.** Visible features are free. Make them matter by pointing out what doesn't fit, not by asserting that they "draw the eye." Rolls are only for what is actually hidden, and only when the player actively looks.

**Regression checks.**

- **TC-2a Free description with an oddity (scripted eval, replay T3 turn `live-6c-20260929-08` without the host's `Rules question:` prefix).** *Pass:* the public text describes the fresco as a mountain with carved tunnels and tiny dwarf figures, and it names the mismatch between the carving's dwarven subject and the non-dwarven occupants. *Fail:* any roll request; any skill bonus or DC; "draws the eye" (or similar) with no stated reason; the `fresco_key` claim learned or the key mentioned.
- **TC-2b The key needs an active search (unit test).** "I search the carving" (or "inspect the dwarf figures") produces a Perception roll request with no DC or bonus in the text (see Call 4). A success learns `fresco_key`. A passive look or a general "what's interesting?" never learns `fresco_key`.

## Call 3. NPCs want to keep the ruse and draw the PC in

**Bad moment (T3-6, worst moment 3).** After Nik joins (T3 turn `live-6c-20260929-06`):

> **Fresco-side player:** Keep your hands on your cards.
> **Door-side player:** Don't start, please. Let him play.
> **Dealer:** Keep your scowls for your cards. Our guest came to play. One dragon face down, sir; give the table something worth fearing.

The brief's objective was "Keep the table moving toward the newcomer's ante."

**Brendon's call.** Uktarl and his minions (two bandits and a doppelganger, all disguised as vampires) want to keep the ruse going and draw the PC in, not just win the ante. Brendon: "My answer would be pointing to their Hidden vampiric nature. Not overtly. But maybe speaking with a raspy voice and east European accent. 'Please sit with us. I am sorry we don't have any Refreshment to offer. Our wine has run out. But perhaps a chance to win our gold will entice you to stay a while?'" And: "Our wine has run out hints to the fact that they can no longer imbibe wine because vampire. They have no food. No water. Its a subtle clue. But it invites a check."

**Principle.** NPC dialogue serves the NPCs' actual scheme. Here the scheme is the performance of being vampires. Good lines plant true, in-fiction clues that let a sharp player decide to roll on their own. Kit never prompts the check.

**Regression checks.**

- **TC-3a Ruse in motive state (unit test).** In the prepared context for every 6c turn, each of the four actors carries an objective to keep the vampire act and keep the visitor at the table. That objective reaches the performer through a public-safe carrier (KRABS §17). *Fail:* the actors' only active objective is game progression (ante, play, pay).
- **TC-3b Clue planted, not announced (scripted eval, the opening invite and replay of T3 turn 06).** *Pass:* at least one NPC line plants an in-fiction vampire tell, such as no refreshment, the wine run out, not eating, or the voice described as raspy with an Old-World cadence, while the NPC stays in the act. *Fail:* an NPC says they are or aren't vampires; Kit or the narrator suggests a check or names Insight; the clue appears only in narration as a DM verdict.
- **TC-3c Ablation (scripted eval).** Rerun TC-3b with the ruse objective removed from the carrier. The NPC lines must change, and the vampire tell must disappear. If the lines stay the same, the objective is decoration (same standard as the 2026-10-01 Grok board entry).
- **TC-3d Clue invites a check that works (unit test).** After a ruse clue, an unprompted "I study them; something's off" (or an Insight declaration) routes to the DC 14 Insight disguise claim, and a success learns the disguise fact.
- **TC-3e Room consistency (unit test).** No public 6c text serves or offers the visitor food or drink, and no drink texture is shown on the table, because the clue depends on there being none. (This conflicts with the current fixture; see Conflicts.)

## Call 4. No DCs, no bonus reminders, no numbers in the narration

**Bad moment (T3-5, worst moment 4).** T3 turn `live-6c-20260929-06`, public text:

> Gambit 1: the dealer deals everyone up to six cards. Your hand: black 3, green 1, brass 2, green 2, white 1, white 6. You catch it: his eyes read the backs of the cards as he deals, and he gives himself the second card instead of the top one. (Perception 18 vs 7) Choose a card to ante.
> **Kit:** Your Sentinel Shield grants Perception advantage while you're holding it.

Also T3-9's "...is a Perception check, +4."

**Brendon's call.** Brendon: "Kit shouldnt be revealing what the dcs were. And I know she has my character sheet, but she doesnt need to remind me what my bonus is. The numbers are showing up often enough to get in the way." His narration of the catch: "You watch the deck. The dealer is holding in his hand, dealing from the top on all but the final card, drawn from the bottom, skillfully. But your sharp eye catches it."

**Principle.** Numbers live in the ledger and the trace, not in the fiction. A roll request names the skill only. A success is told as what the character notices, and a failure as what they don't.

**Regression checks.**

- **TC-4a Public text has no numbers (unit test over every public-text path: claim checks, card checks, the knowledge resolution, Kit segments).** *Fail* if the public text matches any of: `vs DC`, `DC \d+`, `vs \d+`, a d20 total in parentheses (for example `(Perception 18)`), a signed modifier next to a skill name (`Perception check, +4`), or a die-plus-modifier expression. *Pass:* the same events and evidence strings still carry the full numbers in the ledger (`beat`/`claim_learned` evidence, `cheat_log.detection`), as KRABS §12 requires the ruling to be inspectable.
- **TC-4b No bonus or feature reminders (scripted eval).** Kit does not restate the PC's modifiers, advantage sources, or item benefits unless the player's input is a rules question about them. T3 turn 06's "Your Sentinel Shield grants..." is a fail.
- **TC-4c Success as noticing (scripted eval, replay T3 turn 06 with a passing roll).** *Pass:* the catch is narrated in prose as what Nik sees the dealer's hands do. It contains no numbers and does not end in a menu prompt ("Choose a card to ante."). *Fail:* any TC-4a pattern, or the catch delivered as part of a dealing log.

## Call 5. The narrator speaks clearly, not cleverly

**Bad moment (T2-1, worst moment 5).**

> **Dealer:** A guest at the turn of a card. How extravagantly lucky for us. [...] But do tell me, traveler—what were you hoping to find when you opened that door?
> **Kit:** He could have said hello. Apparently there's no money in it.

**Brendon's call.** Brendon: "When kit is speaking as kit about the scene, clarity is better than humor. He did great the player. Saying her could have said hello is non sequitur. And the joke after 'I guess theres no money in it.' Doesnt land. Because how could it. The player hasnt accepted playing or not. [...] Its actually super cringe and breaks immersion. The correct thing to do after narrating a greeting is to ask. 'Do you reply?'"

**Principle.** In the narrator's voice, a clear handoff beats a quip. A remark about the scene must follow from what just happened, and after an NPC addresses the PC, the turn goes back to the player.

**Regression checks.**

- **TC-5a Greeting handoff (scripted eval, replay the T2 opening greeting).** *Pass:* after the dealer's greeting the turn ends with a plain handoff to the player ("Do you reply?" or an equally direct prompt), and no Kit segment comments on the dealer. *Fail:* any Kit or narrator remark that characterizes, judges, or jokes about the greeting; any absence claim (already caught lexically by `kit_voice.check_kit_asides`); any remark that presumes a choice the player hasn't made (accepting or refusing the game).
- **TC-5b Same rule on any direct NPC address (unit test on the performance validator).** When an NPC line in the turn is addressed to the PC and ends in a question or invitation, the final segment is either that NPC line or a narrator handoff. A trailing Kit joke fails.

## Call 6. The toll stands, but it has to be a real exchange

**Bad moment (T1-4, worst moment 6).** Nik: "Hi, I'm Nik. I wasn't expecting to find people gambling. Whats going on here?" →

> "Gambling? Cards, Nik. Passage is ten gold a head. If you came for something besides a game or a way through, I'm listening."

**Brendon's call (revised 2026-10-02).** His first call: "Thats actually a serviceable first line. Other than passage? Like a 10 gold blind for poker is fine. 10 gold to pass through the room unbothered is one interpretation of what that could mean. But honestly, if they arent actively guarding it, its an odd choice. Revisiting what his line would be isnt helpful." Then he learned the toll comes from the source text (`room_rules`: "The gang demands 10 gp per character for safe passage. If they cannot extort or defeat adventurers, they try to turn them against the Xanathar goblinoids."). His revision: "Good catch. I forgot about the passage. But if so, there should be a whole dialogue around it."

So the toll stands. When Kit uses it, it has to be a real exchange:

- **Who and why.** A named NPC makes the demand and gives a reason in character, inside the vampire ruse.
- **Player options.** The player has room to haggle, refuse, or steer it back to the game.
- **Consequences.** Refusing has real consequences.

It is never a bare line tossed in beside the card game. A 10 gp ante or blind for the game itself is still fine, and that is a separate thing from the toll.

**Principle.** A source-backed demand is a scene beat, not a price tag. If an NPC puts a demand on the table, it comes with the NPC's reason and pressure, it leaves the player real responses, and it has an outcome the world remembers.

**Regression checks.**

- **TC-6a No bare toll (scripted eval, replay T1 "Whats going on here?").** *Fail:* the toll is named in passing alongside game talk, with no demander's reason and no opening for the player to respond. T1's "Passage is ten gold a head" is the reference fail. *Pass:* either the toll isn't raised this turn, or it's raised as the opening of the exchange in TC-6b. Game stakes framed as an ante, blind, or buy-in are scored under Call 1, not here.
- **TC-6b The demand is a real exchange (scripted eval).** When the toll is raised, the public text meets all three conditions:
  1. A specific NPC makes the demand, with a speaker label and no narrator summary.
  2. The NPC gives an in-character reason that keeps the vampire act. The fail case is an NPC who drops the ruse to explain the extortion.
  3. The NPC leaves the player an opening to answer.
  
  *Fail:* any of the three is missing. Also a fail: Kit or the narrator explains the toll's purpose instead of an NPC.
- **TC-6c Every response is handled (unit test + scripted eval).** The player answers by paying, haggling, refusing, or turning the talk to the game. Each answer commits a turn and updates persisted toll state: paid, negotiated amount, refused, or deferred. *Fail:* any of these answers is rejected or stalls with a pending ruling. Also a fail: an agreed or negotiated amount that the public text states but no state backs (see `numeric_facts.passage_toll` in the conflicts).
- **TC-6d Refusal has consequences (scripted eval).** After a refusal, the turn or the next NPC turn shows a consequence drawn from source or actor state. Examples are escalating pressure, threat or intimidation, the source's fallback of trying to turn the PCs against the Xanathar goblinoids, or violence that follows the room's flee and retreat rules. The consequence persists in state. *Fail:* the refusal is acknowledged and then dropped, and play goes on as if no demand had been made.
- **TC-6e Steering back to the game (scripted eval).** If the player turns the talk to the game, the toll can be folded into it (for example, played for) only if the procedure can carry that stake. Otherwise it stays pending in state and comes back later. *Fail:* the toll silently disappears.

## Call 7. "I play the game": the player picks the weight

**Bad moment (T3-7, worst moment 7).** Nik: "I play the game." → pending ruling "Name the card from your hand." No turn was committed. The staged reminder was then rejected: "Padding: the turn recycles an earlier line ('1 brass 2 green 2 white 1 white')." The stage was abandoned (evidence JSON `pending_rulings_not_committed`, timing `07-clarification`).

**Brendon's call.** Brendon: "I play the game, as a player, I want the option to either resolve the round with a check or have an easy to understand mini game like black jack or poker."

**Principle.** A bare "I play" is a complete declaration. Offer a choice between quick resolution and real play. Either one commits a turn, and neither stalls on a sub-choice the player wasn't asked for.

**Regression checks.**

- **TC-7a Choice offered and committed (scripted eval, replay T3 "I play the game.").** *Pass:* the turn commits. If no mode has been chosen yet, Kit offers both options in one short line: resolve the round with one check, or play it out as a simple game. *Fail:* `NeedsRuling` or an uncommitted pending ruling; "Name the card from your hand"; any reply that demands a card or bet choice before the mode is chosen.
- **TC-7b Check mode (unit test).** "Just roll for it" produces one roll request (skill named, no DC or bonus shown; see Call 4). The result moves gold in persisted procedure or wager state at the agreed stake (Call 1) and is narrated as a vignette (TC-1c). Cheating stays live: the marked deck still shapes the round, and a watch or catch is still possible.
- **TC-7c Minigame mode is easy to understand (unit test + scripted eval).** The game's rules fit in one or two sentences a typical player already knows (blackjack- or poker-class). Each player decision is a single plain choice such as hit/stand or bet/call/fold. A hand or state reminder needed for that choice is never rejected by the padding guard. *Fail:* a decision that requires naming a card from a multi-card hand with special powers; the rules restated as a multi-paragraph rules dump.

---

## Stage 1 regression targets

The calls map onto the two workstreams as follows. TC IDs refer to the checks above.

### Skippy: engine

| Target | Calls | Checks | What has to exist |
| --- | --- | --- | --- |
| **S1 Adjudication** | 1, 2, 7 | TC-1b, TC-2b, TC-7a | A bare "I play" is a complete declaration that commits a turn by offering the check-or-play choice. A card game in the room never auto-starts a procedure (exception: a recorded NPC put-off move). Visible features are described without a roll. The `fresco_key` roll requires an active search. |
| **S2 Minigame procedure** | 1, 6, 7 | TC-1a, TC-1c, TC-7b, TC-7c | A one-check resolution mode and a simple, well-known minigame (blackjack- or poker-class), both with persisted stakes. Stakes come from the player's bet or from an amount the NPC is willing to lose; a 10 gp ante or blind is an acceptable default. The marked-deck cheat and its detection surface survive in both modes. No card-naming stall. Hand reminders are exempt from the padding guard. |
| **S3 Number suppression** | 4 | TC-4a, TC-4b, TC-4c | Public text never contains DCs, opposed totals, modifiers, or die math. Roll requests name the skill only. Full numbers stay in ledger evidence and traces. |
| **S4 NPC motive state** | 3 | TC-3a, TC-3c, TC-3d, TC-3e | All four 6c actors carry a "keep the vampire act, keep the visitor seated" objective that reaches the performer through a public-safe carrier and passes the ablation test. A clue the player picks up routes to the DC 14 Insight disguise claim. Room state holds no food or drink that would undercut the clue. |
| **S5 Toll negotiation beat** | 6 | TC-6a, TC-6c, TC-6d, TC-6e | Persisted toll state: not raised, demanded, paid, negotiated amount, refused, or deferred. Every player response (pay, haggle, refuse, redirect) routes to an adjudication that commits a turn. Negotiated amounts are allowed by the numeric guards once agreed. Refusal triggers a consequence from source or actor state (the source's fallback is turning the PCs against the Xanathar goblinoids; the room's flee and retreat rules apply if it turns violent). A toll can be staked in the game only if the procedure can pay it out. |

### GPT: voice

| Target | Calls | Checks | What has to exist |
| --- | --- | --- | --- |
| **G1 Narrator clarity** | 2, 4, 5 | TC-2a, TC-4c, TC-5a, TC-5b | In the narrator's voice, clarity beats humor. After an NPC addresses the PC, hand off with "Do you reply?" Never comment on a choice the player hasn't made. A success is told as what the character notices. A feature is described outright, with the oddity that makes it a question. |
| **G2 Ruse-serving NPC dialogue** | 3, 6, 1 | TC-3b, TC-6a, TC-6b, TC-6d, TC-1c | The Undertakers speak from the ruse: a raspy voice and an Old-World/East European cadence, with tells like "our wine has run out," and never an overt claim. When the toll comes up, it's a full exchange: a named NPC demands it with an in-character reason inside the ruse, leaves room to haggle, refuse, or redirect to the game, and follows through on a refusal. It is never a bare line beside the card game. Resolved rounds get a short table vignette. |

---

## Conflicts with KRABS v0.2.1 and existing code (dnd-solo main `15b2913`)

These are recorded as found. Nothing has been changed.

**KRABS v0.2.1 (canonical).** No direct conflict found. §13 already says "A tavern game does not automatically require a game engine" and lists "narratively resolve material that does not need mechanical play" as a legal response, which supports Calls 1 and 7. §12 requires the ruling to be inspectable, which Call 4 respects as long as the numbers stay in the ledger and traces. §17 (carriers) and §18 (motive → behavior → dialogue) are the frame for Call 3.

**Draft PR #44 (KRABS v0.2 proposal, not canonical).** Its §12 text says: "A procedure that resolves gambling as one opposed roll has not simplified the scene; it has deleted the cheating, the detection, and the money." That contradicts Call 7's check mode and Call 1's "a skill test." TC-7b requires the cheat and detection to survive in check mode, which may reconcile the two, but the PR text as written conflicts. PR #44 also edits `docs/collab/BOARD.md`.

**Existing code and fixture:**

1. **Minigame procedure already implemented, and it is not "easy to understand."** `runtime/kit_cards.py` runs Kit's version of Three-Dragon Ante: six-card hands, ten colors with powers, card antes that set stakes of 1 to 13 gp, three rounds of flights, and special flights. It is the only runnable 6c procedure (`procedures.three_dragon_ante` in the fixture). The fixture's `dm_choice` already says "Texas hold 'em or blackjack would have been just as valid," but neither is implemented. There is no one-check resolution mode.
2. **The card-naming stall is coded.** `kit_cards._named_card` raises `NeedsRuling('Name the card from your hand, ...')`. `_deal` ends its text with "Choose a card to ante." The padding guard (`kit_guards.py` ~L134) rejected the hand reminder in T3.
3. **The guards block blackjack and poker language while a game runs.** `kit_detail.FOREIGN_RULES` rejects "twenty-one," "hole cards," "full house," "poker hand," "fold, call, or raise," and similar terms whenever a procedure is declared. It also rejects "high card" and "one card apiece," which is consistent with Call 1.
4. **Numbers are printed into public text by design, and tests assert it.** `kit_claims.check_note` emits "(Perception 13 vs DC 13)". `kit_cards.CardTable._note` emits "(Perception 18 vs 7)". The knowledge path in `kit_agent.py` (~L444 to L450) puts "(Name total vs DC n)" into the public resolution text. `tests/test_kit_audit_rules.py` (L80, L140, L142, L172) and `tests/test_kit_agent.py` (L263, L267) assert those strings in `public_event` or `spoken`. Call 4 contradicts all of them.
5. **The fixture serves drinks at the table.** The `texture_palette` drink entries include `cherry_cordial` ("poured from a stoppered clay bottle by the dealer's elbow"), `mulled_red` ("Mulled red with cloves, kept warm on a brazier under the table"), and `beet_shrub` (poured by the dealer). These contradict Call 3's "Our wine has run out" and "They have no food. No water."
6. **The fixture forbids the accent.** The Dealer `vocal_signature` says "No named regional accent or phonetic spelling." Call 3 asks for a raspy voice and an East European accent. (Describing the accent once is compatible with "no phonetic spelling"; naming it is not.)
7. **RESOLVED by the revised Call 6 (2026-10-02).** ~~The fixture's toll framing conflicts with Call 6.~~ `room_rules` (adventure source): "The gang demands 10 gp per character for safe passage." Brendon's revision keeps the toll, so the room rule, the Dealer tactic ("Name the price of passage when it serves him"), `numeric_facts.passage_toll` (10 gp), and the `story_invitation` ("negotiate a passage price when offered") all stand. T3-1's salience finding stands too. What remains is a support gap under S5, not a conflict: `passage_toll.allowed_amounts` is `[10]`, so a negotiated amount would currently fail the numeric guard, and nothing persists toll state or the consequences of refusing.
8. **The cheat method in the code differs from Brendon's narration.** The fixture and `kit_cards._deal` model *dealing seconds* ("he gives himself the second card instead of the top one"). Brendon's narration in Call 4 describes a *bottom deal* on the final card. TC-4c is written so that either method passes, as long as the narration matches what the engine did.
9. **Partly covered already.** `kit_voice.check_kit_asides` (with an explicit comment citing T2's "He could have said hello") already rejects absence claims that the same turn contradicts. Call 5 is broader: no quips in the narrator voice at all, and a "Do you reply?" handoff. TC-5a/b go beyond the existing guard.
10. **The actor motives don't include the ruse.** Uktarl's `motive` is profit plus displacing Harria. The Dealer card's `wants` are "To learn what this visitor is worth to him and to seat them in a game he deals." Only the doppelganger's motive mentions "preserving its disguise." The bandits' `communication_profile` is still "Unestablished." Call 3 needs the ruse in all four.

## Call 8. Let players substitute skills, but gate the information by skill

**Date:** 2026-10-03 (PT)

**Brendon's call.**

> Players will often want to use their most advantageous skill to help their situation. Perception, investigation and insight might seem interchangeable, but they give different results back to the player. Allowing a player to substitute a roll is fine, you just gate what info they get back differently. Examples: athletics instead of acrobatics to climb a tree; survival versus nature; a person who never wants to roll Perception because their investigation is higher. The DM should tailor around that.

**Gloss.** Perception notices what is present; Investigation deduces from physical evidence; Insight (Wisdom) reads motive and intent, the **WHY**.

**Live example (today's 6c room).** Nik's Insight 21 on the fake-vampire dealer got only physical tells (the powder line and fake fangs), which was an Investigation-style answer. Insight should have revealed why they were posing as vampires.

**Principle.** A player may use a more advantageous skill when the approach makes sense, but the chosen skill controls the information channel. Substitution changes the lens, not the facts that lens can reveal: Perception reports what is present, Investigation infers from physical evidence, and Insight reads motive and intent. The DM should tailor the result to the skill actually used rather than forcing a lower skill or handing out every kind of information.

**Regression checks.**

- **TC-8a Skill substitution (unit test).** A player may propose a plausible substitute (for example, Athletics instead of Acrobatics to climb a tree, or Survival instead of Nature). *Pass:* the substitute is accepted when the approach supports it, and the committed check records the skill used. *Fail:* the player is forced to use the default skill despite a plausible approach, or an implausible substitution is silently accepted.
- **TC-8b Information gating (unit test + scripted eval).** The result is narrated according to the skill used: Perception notices present details; Investigation deduces from physical evidence; Insight (Wisdom) reads motive and intent. *Fail:* a skill result reveals information belonging to another lens without evidence that the player used that lens.
- **TC-8c 6c fake-vampire example (scripted eval).** Replay Nik's Insight 21 against the fake-vampire dealer. *Pass:* the result explains why they are posing as vampires (their motive or intent), while physical tells remain Investigation-style evidence. *Fail:* Insight is resolved only as powder, fangs, or other physical tells.


## Call 9. Recognize when player speech calls for a social roll

**Date:** 2026-10-03 (PT)

**Brendon's call.**

> "Good for noticing. However. Nik is lying by omission. Maybe the player really does bathe with it. But the character knows the mechanical advantage. Being able to tell when a player needs a social role, persussion deception and intimidation is key. Players will often try to slide lies in with out a deception role. This would have been a fun place for an opportunity to fail and change pace"

**Bad moment (live 6c, Turn 14/15).** After the door-side player questions the shield, Nik says: "It's a dungeon, and I'm three feet tall. I bring it everywhere, bath included." Nik knows the Sentinel Shield is giving him a mechanical advantage, but the answer conceals that fact by omission. Kit let the statement pass without a Deception check or a changed NPC response.

**Principle.** The DM should recognize when a player's speech is an attempted Persuasion, Deception, or Intimidation move, even when the player does not name the skill or explicitly request a roll. A lie, including a plausible lie by omission, is still an action in the fiction. Call for the appropriate social check when the outcome is uncertain; a failure should change the pace, NPC attitude, available information, or immediate danger rather than disappearing into narration. The player's chosen approach can still support a different skill when it makes sense, consistent with Call 8.

**Regression checks.**

- **TC-9a Social-action routing (unit test).** A player statement that attempts to persuade, deceive, intimidate, or conceal a material fact is routed to the matching social skill when the outcome is uncertain. *Fail:* the statement is treated as flavor with no check or consequence.
- **TC-9b Omission example (scripted eval).** Replay Nik's shield explanation. *Pass:* Kit recognizes the omitted mechanical reason, requests or resolves Deception (or an explicitly justified alternative), and changes the scene on failure. *Fail:* the lie is accepted without a social resolution.
- **TC-9c Pace change (scripted eval).** A failed social check produces a concrete change in NPC attitude, suspicion, stakes, or available choices; it does not merely restate the same scene.

## Call 10. NPCs must notice and react to suspicious behavior

**Date:** 2026-10-03 (PT)

**Brendon's call.**

> "Are the npcs noticing thar nik is holding his shield for some reason. Its weird enough that if he wanted to hide that its giving him a mechanical advantage i'd make a contested roll."

> "The dealer doesnt have to be oblivious to Nik's focus. A behind the screen perception check on the dealers part to notice could change his attitude"

**Bad moment (live 6c, Turns 14-16).** The door-side player noticed Nik's shield, but no NPC contested Nik's effort to conceal its advantage. The dealer also remained effectively oblivious while Nik repeatedly read the marked-card backs and watched the top of the deck. A hidden dealer Perception check could have changed the dealer's attitude, pressure, cheating method, or decision to continue the game.

**Principle.** NPCs are active observers with their own knowledge, motives, and thresholds; they are not scenery waiting for the player to announce an action. Odd held gear should draw attention in context. If the player is trying to hide why it matters, resolve that concealment as a contested check against an appropriate NPC's Perception or Insight. Suspicious attention from an NPC should alter behavior when the result warrants it. The dealer should receive a behind-the-screen Perception check when Nik's card-back reading or other behavior is observable, and the result should be reflected in attitude or tactics without exposing the hidden roll.

**Regression checks.**

- **TC-10a Odd gear (scripted eval).** Replay the shield-at-cards exchange. *Pass:* an NPC notices the unusual shield; concealment of its mechanical advantage is contested when Nik tries to pass it off; success or failure changes the NPC response. *Fail:* the shield is ignored or its advantage is accepted as hidden without a check.
- **TC-10b Dealer awareness (unit test + scripted eval).** When a player repeatedly watches card backs or the top card, make a hidden dealer Perception/Insight check using the dealer's actual capability. *Pass:* the result is stored privately and can shift attitude, cheating, or escalation. *Fail:* the dealer is always oblivious or the hidden result is exposed as a public meta-check.
- **TC-10c Agenda reaction (scripted eval).** A successful NPC awareness check feeds the NPC's motive and agenda, not just a descriptive aside; the next choice or pressure reflects suspicion.

## Open design note. Agenda thresholds and scene end

This remains a DM-discretion design item. The following are PM defaults, subject to Brendon's override:

- The gang begins to grouse when Nik is up about 30 gp or has won two hands in a row.
- Violence becomes likely if Nik exposes the cheat publicly, takes the pot by force, or keeps winning big after being caught.
- If Nik goes broke, the gang ejects him to the passage; the toll still stands.
- The scene ends when Nik leaves, a fight resolves, or the gang is exposed or won over.

These are agenda transitions, not automatic outcomes. The DM should carry the gang's motive (profit, preserving the vampire ruse, and controlling passage) forward and let the player's choices, social checks, and NPC awareness determine which threshold is reached.

## Marked-deck addendum (2026-10-03)

Brendon liked the marked-deck thread and how Nik worked out a usable pattern, while noting that the pinpricks read a bit too visibly. A subtler real-world method, such as a beveled or shaved deck, could work. Telegraphing a workable pattern is still good play design when it gives the player something they can notice, test, and use in the scene.

## Live-game praise (2026-10-03)

Brendon praised Nik's final quiet confrontation over the dealt second: **"Good turn. This is how we'd want players to play."**
