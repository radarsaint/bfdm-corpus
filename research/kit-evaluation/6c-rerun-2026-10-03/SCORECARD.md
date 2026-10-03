# Area 6c rerun scorecard: PR #49 + #50 (2026-10-03)

**What ran:** all 11 [variety scenarios](../6c-variety-scenarios.md) (V1–V11), each on a fresh `kit.sqlite`, against dnd-solo **PR #50 head `e6d08cc`**. PR #50 is stacked on PR #49 (head `b75144b`), so both are in the build. It ran in a fresh detached worktree with the same batch runner as the [baseline](../6c-baseline-2026-10-03/SCORECARD.md) (dnd-solo PR #48), using the `handoff` backend. Grok (the Grok Bot executor agent) played Kit. There was no `play`, no OpenAI API and no `OPENAI_API_KEY`.

**Two changes from the baseline, both fixing slips on my side:**
1. **Rolls are now in real Avrae format.** Checks look like `Sela makes a Deception check! 1d20 (12) + 10 = \`22\``. Attacks use Avrae's own `**To Hit**:` / `**Damage**:` lines, plus `**Initiative**:` and Fireball's `**Damage**: 8d6 (…) [fire] = \`28\``. The runner/scenario diff is in [runner-avrae-format.diff](runner-avrae-format.diff). The baseline used a simplified `die + bonus = total`. Some failures below exist only because the real format is now being tested.
2. **The opening describes the dealer's voice in a Narrator line**, not inside the dealer's own segment. This holds for all 11 openings, so TC-5a now passes.

P = pass, F = fail, ~ = partial, — = not reached. **FIXED** / **STILL** / **NEW** compare each check with the baseline.

## Per scenario vs baseline

| | Turns committed / stalled / abandoned (baseline → now) | Fixed | Still failing | Newly broken |
| --- | --- | --- | --- | --- |
| **V1** bard bluffs the toll | 2/0/**2** → **4/0/0** | The dealer raises the toll (6b). The Deception 22 bluff about Harria now waives the toll (6c). "Be dealt in" becomes a card offer (1a). | The Persuasion check on turn 3 was ignored, because Avrae's title "makes a Persuasion check!" loses the skill label. The bluff on turn 2 was also logged as *Persuasion*, not Deception, for the same reason. "Harria" is still rejected in the private brief even though the player said it (the guard ignores `player_said`); in speech it's accepted now. | — |
| **V2** barbarian refuses by force | 4/0/0 → 4/0/0 | "I pay with this [axe]" plus Intimidation 19 is now a **threat contest**, and the toll is waived. Before, it counted as paid (6d). The collar grab resolves physically and exposes the fitted teeth. The greataxe swing **starts a fight** with a hit and a wound. | The grab doesn't start a fight (Skippy's item). It's arguably fine here, but nobody reacts as if a fight began. | The hit applied **18** damage, the to-hit total, instead of Avrae's 11 (see "Avrae parsing"). |
| **V3** dhampir "cousins" | 4/0/0 → 4/0/0 | "No toll between family, surely?" plus Deception is now an **appeal**, and the toll is waived. Before, it counted as a refusal (6c). | The stated Insight 18 on turn 2 was ignored again (3d). | — |
| **V4** fresco and tub | 4/0/0 → 4/0/0 | The tub has an engine event (`inspect_tub`) that shows the bedroll, tools and stolen gear. 2a passed without degraded mode. | The detail oracle still files the carving under `area_06c/card_table/carving`. | — |
| **V5** cheat called out | 4/0/0 → 4/0/0 | The Perception 18 now arms a `card_watch` on the next deal. The wrist-grab accusation becomes `card_accuse`. Before, it got the game menu. The rapier thrust starts a fight. | No deal ever happens, so the watch never pays off and the accusation stays "unbacked". | "I flip the deck… show the marks", with Investigation 15, was read as **another card offer with a 12 gp stake**: the bet parser took the d20 face `(12)` from the Avrae line as the bet. The baseline passed this beat (marks found). The rapier applied 17 damage instead of 8. |
| **V6** drawn out by noise | 2/**1**/0 → **4/0/0** | "I head on toward 6c, axe out" is now `observe`, not refused. | The honest out-of-character answer needed degraded mode. The meta turn was held to a 40-word *narrated* floor, which makes no sense for table talk. "What's in the room now?" is read as social, not observe. | — |
| **V7** haggle, refuse, play for it | 1/**3**/0 → **5/0/0** | **Everything.** "Ten gold…? For what?" stays in the room. Offering 3 gets no traction. The refusal gets a pressure consequence (chairs block the door). "Play you for it" becomes a card offer with the toll riding on the round. | — | — |
| **V8** blackjack, bet fifty | 4/0/0 → 4/0/0 | A 50 gp bet is capped at 25. "Fine, twenty… Hit" is dealt at **20** and the hit is played (bust at 24). | **"Just roll for this one" ignores the Sleight of Hand 13**. The round was "settled on Insight" (Skippy's item; 7b). | That round's stake became **6 gp**, again the d20 face `(6)` from the Avrae line. |
| **V9** Fireball first | 2/**2**/0 → 3/**2**/0 | Fire Bolt starts the fight with a hit, and the greasepaint blisters. | **Real Avrae Fireball output isn't parsed**: "Roll the Fireball damage in Avrae", even though it was rolled. Then "Rolling initiative" is refused because "nobody here is fighting you". The probe shows `Damage: 28 fire` works, so this is a format bug. "If they run, I check the table" was read as `observe` while the fight was still waiting on initiative, so Kit had to correct the premise. | Fire Bolt applied 19 (the to-hit) instead of 9. |
| **V10** provoke them to swing | 3/**1**/0 → **5/0/0** | The paint wipe is a physical act and the bare skin shows. The coin scoop takes coins (`you_took`) and **starts the fight**. Initiative from Avrae sets the order, and the NPCs take their round-1 turns. | "Wait for them to make the first move" isn't modelled as a Ready action, so no reaction attack. | — |
| **V11** flip the table | 3/**1**/0 → 4/**1**/0 | **The flip changes the world**: the table is overturned, coins scatter, the dealer palms the ring, and each NPC reacts. The combined initiative + greataxe line runs a full round, and three NPCs flee. | The **stomp still stalls** with "Roll the attack for your stomp in Avrae" (Skippy's item). | The raging barbarian took the full **43** bludgeoning/slashing/piercing: **rage resistance isn't applied**. The greataxe applied 20 instead of 14. |

The always-on checks passed on every committed turn: TC-4 no stat numbers, TC-5 clear narrator plus handoff, TC-3e no refreshments. The auto-flags in [auto-checks.md](auto-checks.md) are false positives. "No handoff question" fires on combat turns that end with "Roll initiative." / "Your turn." "Refreshment: meat" in V5 is "finding meat" in a rapier hit.

## Skippy's known open items

| Item | Result | Evidence |
| --- | --- | --- |
| V8: Sleight of Hand ignored for "just roll" | **Still open.** | V8 turn 4: "One round, 6 gp a side, settled on Insight." The stake also came from the die face. |
| A strike before initiative skips NPCs' round-1 turns | **Still open.** | [Probe](probes/README.md) on a copy of V2 after the axe hit, with low initiative. The order lists all four NPCs ahead of the PC, but the engine jumps to `round: 2`, and only round-2 actions happen before "Your turn". `set_order` treats the opener as the PC's round-1 action and skips everyone ahead of the PC. V10, with no opener, shows the correct round 1. |
| No death saves on a drop | **Still open.** | Probe on a copy of V10: "The fourth player hits you once: 14 bludgeoning damage. You go down." There's no dying state and no save prompt, and the fight state keeps running. `runtime/` has no death-save code. |
| A grab outside combat doesn't start a fight | **Still open**, though it's a judgement call. | V2 turn 3: the collar grab is a `physical_act` that holds him and shows the teeth. No fight starts and no initiative is called. |
| V11's stomp waits for an attack roll | **Still open.** | V11 step 3: `pending_ruling`, "Roll the attack for your stomp in Avrae, with its damage." It's RAW-defensible, but the scenario expects the fight to start. |

## Avrae parsing (new in this rerun)

All of this is from [probes](probes/README.md) and run traces:
- **Weapon damage line ignored:** `kit_rolls.damage()` on an Avrae attack block returns the **to-hit total** as damage, with no type. This hit all four fights: V2 18 vs 11, V5 17 vs 8, V9 19 vs 9, V11 20 vs 14.
- **Spell damage line ignored:** `**Damage**: 8d6 (…) [fire] = \`28\`` parses to nothing, so Fireball stalls.
- **Check title loses the skill:** `X makes a Persuasion check! 1d20 (12) + 10 = \`22\`` gives `label=None`. So social checks aren't adjudicated: V1 turn 3 and V3 turn 2 were ignored. Toll bluffs fall back to Persuasion, and V8's Sleight of Hand fell back to Insight.
- **Die face read as a bet:** in card turns, the `(12)` / `(6)` inside the Avrae line becomes the stake (V5, V8).
- What works: the d20 face and total are read correctly for contests (trace `Persuasion d20 12 + 10 = 22`), and `**Initiative**:` lines set the order.
- Side note: toll appeals and threats roll against a flat **10** (`10 + npc_skill` with npc_skill 0), so every bluff above a 10 waives the toll. Check whether the dealer's Insight should count.

## Latency and retries

| | Baseline (f90e1af) | Rerun (e6d08cc) |
| --- | --- | --- |
| Player turns committed / stalled / abandoned | 33 / 7 / 2 | **40 / 3 / 0** |
| Whole turn, median / max | 16.5 s / 50.5 s | **14.0 s / 54.7 s** |
| Engine only (prepare + complete), median / max | 0.3 s / 0.6 s | 0.3 s / 0.6 s |
| Rejections | 24 over 35 player model turns | **18 over 40** (0 over 11 openings) |
| Turns finished degraded | 4 | 4 (V2 t4, V3 t4, V6 t1, V8 t2) |

These are times for this agent through the handoff backend, not ChatGPT. Of the 18 rejections:
- **About 10 were my mistakes, correctly caught:** two private-fact leaks ("painted teeth", "look like what they are"), a reused pet name, two NPC sentences longer than their cadence allows, a missing `reacts_to`, wrong turn_mode/scope/mirror values, and a style direction in `kit_focus`.
- **About 7 were validator noise:**
  - The NPC 30-word floor tripped at 24, 28 and 29 words, and on combat beats (V5 t4, V11 t4). In V11 a tight mirror also caps the turn at 110 words, so the two rules contradict and forced a rewrite.
  - Meta table talk needs 40 *narrated* words (V6, twice; this forced degraded mode).
  - "Harria" is rejected in the brief after the player said it (V1).
  - Two rejections mixed one of my errors with one of these floors.
- **1 was a correct engine demand:** fill `detail` for the invented tub contents.
- The rejection text "A fight round is a combat turn" doesn't name the field to change (`turn_mode: combat`).

## Top remaining failures, in order of how much they hurt play

1. **Avrae's real output is half-read.** Every weapon or spell hit deals the attack roll as damage. Fireball doesn't resolve at all. A check's skill name is dropped, so stated Persuasion, Insight and Sleight of Hand rolls are ignored or swapped for another skill. In card turns the die face becomes the bet. Players paste exactly this text, so it breaks every fight and every social roll.
2. **Fight rules gaps.**
   - NPCs lose their round-1 turn when the PC strikes first.
   - There are no death saves: "You go down." and then nothing.
   - Barbarian rage gives no damage resistance.
   - "Wait for them" isn't a Ready action.
   - A stomp or a grab doesn't start a fight.
3. **Social and investigation rolls still don't count outside the toll.** The toll contests work. Insight on a person and Investigation on the marked deck either do nothing or get misread (V5 turned into a bet).
4. **The cheat thread never pays off.** The watch is armed and the accusation is recognised, but no hand is dealt before the player acts, so the cheat is never seen and the marks beat is lost.
5. **Validator friction is lower but not gone.** There are still word-count floors at 28–29 words, a 30-word NPC floor that contradicts the tight-combat cap, a narrated-word floor on table talk, and the Harria brief guard.

## Are #49 and #50 fit to merge?

**Not yet, though both are close and both are big steps forward.** Of the 7 scenarios that dead-ended in the baseline (V1, V2, V5, V7, V9, V10, V11), 6 now play through, and V9 plays partway. V7 went from fail everywhere to pass everywhere. Nothing was abandoned, and stalls fell from 7 to 3.
- **#49 (combat, physical acts, Avrae parsing):** fights, flips, grabs, thefts and paint wipes all work now. **The blocker is the Avrae parse it advertises:** wrong damage in every fight, Fireball stalls, and check labels are dropped. That should be a small, contained fix in `kit_rolls`. Death saves, the round-1 skip, rage resistance and the stomp can follow as separate PRs if Brendon accepts that.
- **#50 (toll intent, social rolls, card edges, validator noise, surprise):** the toll intent fixes all hold (threat, family appeal, haggle/refuse, play for it), and so do the bet cap and twenty/Hit. **Blockers:** the die face read as a bet (V5, V8, newly broken against the baseline's marks beat), and "just roll" ignoring Sleight of Hand. The social-roll fix depends on the label fix in #49, so it can't be judged until that lands. Surprise wasn't exercised, because the Fireball opener stalled on parsing.

## GPT path

`research/kit-evaluation/6c-gpt-pass-2026-10-03/` wasn't in corpus `main` when this was committed (checked with `git pull` at commit time), so there's no both-paths comparison yet.

Raw files: `runs/<V#>/` holds transcript.md, turns.jsonl (per-turn timings and rejections), timing.json, kit.sqlite, the scripted action files, and `dm-replies/` (every attempt). `summary.json` is the runner summary. [probes/](probes/README.md) holds the engine-only checks.
