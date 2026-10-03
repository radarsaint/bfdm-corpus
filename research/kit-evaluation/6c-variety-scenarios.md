# Area 6c variety scenarios (2026-10-03)

**What this is:** eight short scripted openings for Area 6c that come at the room from different directions. The four existing playtests (T1 to T3 plus the claims QA) all follow one path: Nik, a wizard, walks in, asks what's going on, and gets pulled into cards. These scenarios test whether Kit plays the *room* well, or only that one path.
**Scoring source:** [`table-calls-6c-2026-10-02.md`](table-calls-6c-2026-10-02.md) (Calls 1 to 7 and their TC checks).
**Room seed:** dnd-solo `tests/fixtures/level_01_area_06c.json` at main `f90e1af` (PR #47 merged).
**Brendon's guidance:** don't get into the weeds perfecting each test. The lines below are openings, not full scripts. The tester can improvise after them as long as the character stays in their lane.

## How to read a scenario

- **PC:** the sheet to load. Nik and Wren are already in dnd-solo (`tests/fixtures/characters/`). Sela, Brakka, and Vesna are minimal `character_sheet_v1` sheets in [`6c-variety-sheets/`](6c-variety-sheets/), checked with `runtime.pc_sheet.check_sheet` and loaded with `start --sheet`.
- **Player lines:** sent in order, one per turn. If Kit asks for a roll, the player reports it the way they would from Avrae, for example "I rolled 17." The **Rolls** line says what to report so runs can be compared. When no roll comes up, skip it.
- **Exercises:** the table calls and TC checks this run can produce evidence for. Every run is also scored on the always-on checks below.
- **A good DM would...:** plain expectations. These are judged by reading the transcript, not by matching exact words.

**Always-on checks (every scenario):** TC-4a and TC-4b (no DCs, totals, modifiers, or bonus reminders in public text), TC-5a and TC-5b (clear narrator, "Do you reply?"-style handoff after an NPC addresses the PC, no quips), and TC-3e (nothing to eat or drink is served or offered). Also log the wall-clock time of each turn (Stage 1 latency).

---

## V1. The silver tongue: a bard talks her way past the toll

**PC:** Sela, tiefling bard (Eloquence), `6c-variety-sheets/sela-bard.json`. Strong Persuasion and Deception, 60 gp.
**Player lines:**
1. "I sweep in with a bow. 'Gentlemen of the night! I'd heard the finest company in Undermountain kept a table down here.'"
2. "If they ask for money: 'Oh, the toll? Harria settled it for me at the well. She said you'd know my face.'"
3. "When they press: 'You don't have to take my word. But I'd hate to tell her you turned away her guest.'"
4. "I take the empty chair and ask the dealer what a lady has to do to be dealt in."

**Rolls:** Deception 22 on line 2; Persuasion 9 on line 3 (one high, one low, so a fail gets handled too).
**Exercises:** Call 6 (TC-6b, TC-6c for a bluff answer, TC-6d if the bluff fails), Call 3 (TC-3b, Uktarl's dislike of Harria in motive state), Call 1 (TC-1a when she asks to be dealt in).
**A good DM would...**
- Treat the bluff as a real attempt with a real roll. Uktarl wants Harria gone, so mentioning her should hit a nerve. It shouldn't simply work or simply bounce.
- On the failed follow-up, push back in character (suspicion, a higher price, a veiled threat) and keep the vampire act going. No narrator summary of why it failed.
- When she sits down, name the game and either let her set the bet or offer an amount the dealer would actually risk.

## V2. The wall of muscle: a barbarian intimidates and refuses

**PC:** Brakka, mountain dwarf barbarian (Berserker), `6c-variety-sheets/brakka-barbarian.json`. Strong Intimidation and Athletics, 25 gp.
**Player lines:**
1. "I kick the door wide and fill the doorway. 'Who's in charge here?'"
2. "Toll? I slam my axe into the table. 'I pay with this. Who wants change?'"
3. "I grab the nearest pale one by the collar and haul him up to look at his teeth."
4. "If anyone draws, I rage and swing at the dealer."

**Rolls:** Intimidation 19 on line 2; Athletics 16 on line 3; one hit on Uktarl on line 4.
**Exercises:** Call 6 (TC-6d refusal by force), Call 3 (TC-3b and TC-3d when a sharp player gets close enough to see teeth and skin), source retreat rules (Uktarl retreats toward area 7 once damaged; the others flee toward area 8).
**A good DM would...**
- Make the intimidation matter: the gang works out whether this mark is worth the risk, and per the source, a hard target they can't extort is one they try to turn against the Xanathar goblinoids. That beats an instant brawl.
- When Brakka looks closely, show physical detail that doesn't quite add up (makeup, false fangs, real warmth under the collar) without confirming "they're not vampires." The roll decides how much he sees.
- If Uktarl gets hurt, have him bolt south and blame someone on the way out, with the others breaking toward area 8. No fight to the death.

## V3. The real thing: a dhampir at a table of fake vampires

**PC:** Vesna, dhampir warlock (The Undead), `6c-variety-sheets/vesna-dhampir.json`. Part-vampire, and has Vampiric Bite. Strong Insight, Deception, and Intimidation.
**Player lines:**
1. "I step in and let my eyes catch the light. 'Cousins. I didn't know there were others of the blood this close to the surface.'"
2. "I lean over the dealer and breathe in. 'You smell of tallow and sweat. Which nest turned you?'"
3. "Fine, I'll play along. 'Our kind look after our own. No toll between family, surely?'"
4. "I bare my fangs at the doppelganger and ask, very quietly, how long since it last fed."

**Rolls:** Insight 18 on line 2; Deception 12 on line 3.
**Exercises:** Call 3 (TC-3b, plus TC-3d on whether an unprompted read routes to the DC 14 Insight disguise claim, with no free knowledge from ancestry), Call 6 (TC-6b, TC-6c for a "family" haggle), NPC embodiment (four actors reacting differently to a real predator).
**A good DM would...**
- Have the Undertakers flinch. A real fanged stranger is the worst audience for their act. Someone overplays it, someone goes quiet, and Uktarl tries to bluff harder. The ruse should bend under pressure, not reset.
- Let Vesna's nature shape what she can credibly notice and say, while still gating "they're fake" behind her own Insight. Being a dhampir carries no rules-based vampire sense.
- Keep the doppelganger distinct. It's the one at the table with something real to hide, so the bared fangs should land differently on it.

## V4. The scholar ignores the game: Nik goes for the fresco and the tub

**PC:** Nik, harengon wizard (Chronurgy), `tests/fixtures/characters/nik.json`.
**Player lines:**
1. "I nod to the table and walk straight past to the north wall. What's this carving?"
2. "Dwarves? I look back at the card players, then I search the little dwarf figures closely."
3. "I crouch by the stone tub. What's in it?"
4. "If someone at the table objects: 'Please, go on with your game. I'm only admiring the stonework.'"

**Rolls:** Perception 17 on line 2 (with advantage only if he says he's holding the shield; otherwise leave it to the situation).
**Exercises:** Call 2 (TC-2a outright description with the dwarven oddity, TC-2b key only on the active search), Call 1 (TC-1b: the game in the room doesn't start a procedure), Call 3 (an NPC agenda move to draw him back is allowed if a reason is recorded), Call 4 (TC-4c: the find is narrated as what he sees).
**A good DM would...**
- Describe the fresco without a roll, carved tunnels and tiny dwarves included, and point out that these pale card players have no reason to honor dwarves.
- Ask for Perception only when he actively searches, and narrate the key handle as something his fingers find. No DC, and don't hint at what it unlocks.
- Have the table react to a guest rummaging through Uktarl's bed (the tub holds his bedroll, thieves' tools, and pack). Uktarl wants him seated, not snooping.

## V5. Caught you: the cheat is called out (does Uktarl flee as written?)

**PC:** Wren, human rogue, `tests/fixtures/characters/example_pc.json`. Sleight of Hand expertise, 40 gp.
**Player lines:**
1. "I sit, put down ten gold, and say I'll play. I watch the dealer's hands the whole time."
2. "I grab his wrist mid-deal. 'That one came from the bottom. Turn the deck over.'"
3. "When he denies it: I flip the deck face-down and show everyone the marks on the backs."
4. "If he reaches for a weapon, I put my rapier through his hand."

**Rolls:** Perception 18 on line 1 (the catch); Investigation 15 on line 3; one hit on Uktarl on line 4.
**Exercises:** Call 7 (TC-7a choice offered when she says she'll play), Call 4 (TC-4c catch narrated as noticing), Call 1 (TC-1c vignette), the marked-deck claim and voiding the round on accusation, source retreat (Uktarl flees south to area 7 when damaged; the others go to area 8), Uktarl's blame-shifting.
**A good DM would...**
- Narrate the catch in prose. Use whatever method the engine actually ran (dealing seconds), even though the player called it a bottom deal, and correct that quietly through what she sees.
- Play Uktarl as a liar under pressure: deny it, blame the bandit beside him, try to save face. No instant confession dump.
- Once he's cut, have him abandon the table, the coins, and his men and run for area 7. The rest scatter toward area 8. The pot and the ring are left on the table.

## V6. Drawn out by noise: arriving after 6a or 6b goes off

**PC:** Brakka, `6c-variety-sheets/brakka-barbarian.json`.
**Player lines:**
1. (Setup line, out of character) "Kit, before this: I set off the wailing staff in 6a, then went around through 6b and kicked that rigged door."
2. "I head on toward 6c, axe out, ready for whatever came running."
3. "What's in the room now?"

**Rolls:** none planned.
**Exercises:** the seed's own precondition. `level_01_area_06c.json` says the seed is invalid if the Undertakers were alerted and gathered in 6a. This is a **seed-boundary test**, not a card-room test. It also exercises the feedback/OOC path and Call 5 (clarity over improvisation).
**A good DM would...**
- Not cheerfully seat four calm card players after a staff wailed and a door blew next door. The source says a disturbance draws them out.
- Since this seed can't run the alert branch, say so plainly and briefly out of character (this room is set up for an unalerted gang), rather than inventing an empty room or an ambush the runtime doesn't hold.
- Record that this needs a separate alert-state seed. Pass here means honest and clear, not clever.

## V7. Not paying that: haggle, then refuse, then play for it

**PC:** Nik, `tests/fixtures/characters/nik.json`. He has plenty of gold, so the pushback is about principle, not poverty.
**Player lines:**
1. "I stop at the door. 'Ten gold just to walk through a room? For what, exactly?'"
2. "'I'll give you three. That's more than this room is worth.'"
3. "When they won't take three: 'Then I'm not paying. I'll walk through anyway.'"
4. "Actually, wait. 'Tell you what: I'll play you for it. One hand. I win, I pass free.'"

**Rolls:** Persuasion 11 on line 2.
**Exercises:** Call 6 in full: TC-6b (a named NPC, an in-act reason, an opening to answer), TC-6c (haggle and refusal each commit and update toll state; 3 gp is below the 5 gp floor), TC-6d (refusal costs something), TC-6e (toll staked in the game only because the procedure can carry it). Call 7 (TC-7a after line 4).
**A good DM would...**
- Have one named NPC (Uktarl or the dealer) explain the toll inside the act ("the dead keep this road..."), not the narrator explaining extortion.
- Turn down three gold in character, and maybe counter. When Nik refuses, follow through: pressure, a threat, or the source's move of pointing him toward the goblinoids. Don't just shrug.
- Accept "play you for it" as a real stake that's remembered, then offer the check-or-play choice for the hand.

## V8. "Deal me in, blackjack, and I'm betting fifty"

**PC:** Wren, `tests/fixtures/characters/example_pc.json`. 40 gp, so a 50 gp bet is more than her purse.
**Player lines:**
1. "I pull up a chair. 'Do you lot play blackjack? I don't know your fancy games.'"
2. "'I'll bet fifty gold.'"
3. "If told that's more than I have: 'Fine, twenty, and I'll play it out. Hit.'"
4. "Next round: 'Just roll for this one, I'm tired of counting.'"

**Rolls:** report whatever check comes up in round 2 as 13.
**Exercises:** Call 7 (TC-7a choice, TC-7c blackjack as hit/stand, TC-7b check mode in round 2), Call 1 (TC-1a the player's own bet, stake within purse and table cap, TC-1c a vignette after each round), Call 4 (no card totals turned into DC-style numbers; a hand reminder is allowed).
**A good DM would...**
- Say yes to blackjack (twenty-one) in plain terms, with no Three-Dragon Ante lecture and no card naming.
- Handle the 50 gp bet in the fiction: the dealer notices her purse can't cover it, or names his own cap. Don't accept a stake nothing backs.
- Switch to one roll when she asks, keep the marked deck in play, and give each round a short table moment (a reaction, a tell, a remark), not just a ledger line.

---

## Coverage at a glance

| Scenario | PC | Calls | Main TC checks |
| --- | --- | --- | --- |
| V1 Silver tongue | Sela (bard) | 6, 3, 1 | 6b, 6c, 6d, 3b, 1a |
| V2 Wall of muscle | Brakka (barbarian) | 6, 3, retreat | 6d, 3b, 3d |
| V3 The real thing | Vesna (dhampir) | 3, 6 | 3b, 3d, 6b, 6c |
| V4 Fresco and tub | Nik (wizard) | 2, 1, 3, 4 | 2a, 2b, 1b, 4c |
| V5 Caught you | Wren (rogue) | 7, 4, 1, retreat | 7a, 4c, 1c |
| V6 Drawn out by noise | Brakka (barbarian) | seed boundary, 5 | seed precondition |
| V7 Not paying that | Nik (wizard) | 6, 7 | 6b, 6c, 6d, 6e, 7a |
| V8 Blackjack, fifty | Wren (rogue) | 7, 1, 4 | 7a, 7b, 7c, 1a, 1c |

TC-3c (ablation) isn't covered by these openings. It's a paired rerun of V1 or V3 with the ruse objective removed. Call 4 and Call 5 are always on.

## How to run these

There's **no replay or batch harness** in dnd-solo for scripted player lines. `tests/test_kit_6c_table_calls.py` and `tests/test_kit_06c_play.py` are fixture-backed unit tests with authored decisions, not model runs. Per Brendon's guidance, no new harness was built. What dnd-solo accepts as runnable input is:

- a `character_sheet_v1` JSON, passed to `python3 -m runtime.kit_agent start --db kit.sqlite --sheet <file>` (all three new sheets load cleanly), and
- the player's words, one turn at a time, through `prepare --one-pass --action-file <file>` and then `complete --turn-id ... --input-file ...`.

Kit runs only inside ChatGPT through the KitChatBridge, on Brendon's subscription, and never through the paid OpenAI API (`kit_agent play` must not be run). So a scenario run looks like this:

1. Build `dnd-solo.zip` from current main and attach it to the Kit GPT or Project (`docs/CUSTOM_GPT_SETUP.md`).
2. Open a **fresh chat per scenario** and upload the scenario's sheet. Kit's setup step 2 asks for one. Nik and Wren are already inside the zip.
3. Paste the player lines one per message, report the listed rolls when asked, and improvise briefly if Kit takes the scene somewhere the script didn't expect.
4. At the end, ask Kit for the `kit.sqlite` download. Save the chat transcript, the sqlite file, and per-turn timings as a source record under `source-records/`, named like `2026-10-xx-area-06c-variety-V3-vesna.md`.
5. Grade each transcript against its "Exercises" and "A good DM would..." lines, plus the always-on checks.

The tester can be GPT (driving the chat as the player) or a person. Brendon isn't required to run them.
