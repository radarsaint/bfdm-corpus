# Area 6c rerun 2 scorecard: PR #49 `6ee802b` + PR #50 `246779a` (2026-10-03)

**What ran:** all 11 [variety scenarios](../6c-variety-scenarios.md) (V1–V11), each on a fresh `kit.sqlite`, against dnd-solo **PR #50 head `246779a`**. #50 is stacked on **PR #49 head `6ee802b`**, which is in its history along with current `main`. This ran in a fresh detached worktree (`/workspace/dnd-solo-rerun2`) with the merged batch runner (PR #48, plus the Avrae-format runner change folded in as `4fcca30`) and the `handoff` backend. Grok (the Grok Bot executor agent) played Kit. There was no `play`, no OpenAI API and no `OPENAI_API_KEY`. The scenario file and runner are byte-identical to the [previous rerun](../6c-rerun-2026-10-03/SCORECARD.md) (`e6d08cc`), so every player line and Avrae block is the same.

Engine-only checks ran on **both heads** (#49 alone at `6ee802b`, and #50 at `246779a`): the scenario probe, direct `kit_rolls` calls, state probes with exact HP deltas, and fight probes on copies of this run's databases. See [probes/](probes/).

**Test suites:** `python3 -m unittest discover -s tests -p 'test_*.py'`
- #49 `6ee802b`: **450 tests, OK**
- #50 `246779a`: **492 tests, OK**

P = pass, F = fail. **FIXED**, **STILL** and **NEW** compare each check with the previous rerun.

## Skippy's claimed blocker fixes

| PR | Claim | Result | Evidence |
| --- | --- | --- | --- |
| #49 | Avrae damage reads the `**Damage**:` line (V2 deals 11) | **PASS** | V2 DB: dealer took **11** (was 18). Same fix holds everywhere: V5 **8** (was 17), V9 Fire Bolt **9** (was 19), V11 greataxe **14** (was 20). `damage()` on the block gives `[(11, 'slashing')]`. CRIT lines (`**Damage (CRIT!)**`) parse too. This passes on #49 alone. |
| #49 | A real Fireball resolves its DC, per-target saves and damage (V9 28 fire) | **PASS** | V9 now plays through. Fireball deals **28 fire**: two players drop, and the fourth player (failed save) and the dealer take 28 each. Initiative is accepted and the fight runs to the end. Targeted probe (`DC 15`, `Dealer … Failure! … 28`, `Fourth player … Success! … / 2 = 14`): each listed target takes Avrae's number. With **DC 25**, an unlisted target's own save (forced to 20) fails against Avrae's DC and takes the full 28, so the DC line is used. Both heads behave the same. |
| #49 | `X makes a Persuasion check!` sets the skill | **PASS** | `check_roll` → `label='persuasion'`, and `Sleight of Hand` → `sleight_of_hand`. On #49 this is parse-only. The social roll is adjudicated through #50: V1 t3 is now `social_check` (it used to be ignored). |
| #50 | Numbers inside Avrae or dice output are never bets, stakes or toll offers (V5 marks restored, V8 stays 20 gp) | **PASS** | V5 t3 is a `check` again: "Faint marks run along the card backs, and the dealer reads them as he deals." (it was a 12 gp card offer). V8 t4 stays at **20 gp** (it was 6). Probe: the toll haggle "three" plus `1d20 (12) + 1` stays an offer of 3, and "Fifteen gold … just roll" plus `1d20 (18)` gives a 15 gp stake. |
| #50 | "Just roll" honors a stated or implied skill (V8 settles on Sleight of Hand) | **PASS** | V8 t4: "settled on Sleight of Hand. You lose 20 gp to the house." (#49 alone: Insight). The probe "I'll palm a card if I have to" with a bare d20 line settles on Sleight of Hand. A bare d20 line with no skill named falls back to Insight, which is reasonable. |

## Per scenario vs the previous rerun

Turns committed / stalled / abandoned (openings excluded): previous **40 / 3 / 0** → now **42 / 1 / 0**. The only stall is the V11 stomp (known follow-up).

| | Committed / stalled (prev → now) | Fixed | Still | New |
| --- | --- | --- | --- | --- |
| **V1** bard bluffs the toll | 4/0 → 4/0 | The Persuasion check on t3 is now adjudicated (`social_check`). The toll bluff resolves as an appeal. | The Persuasion roll was `1d20 (1) + 10 = 11`, and "The dealer comes around to it.": a natural 1 beats a flat 10 (see "Other findings"). The brief guard still rejects "Harria" after the player said it. Speech accepts it now, but `check_brief_public` doesn't get `player_said`. It cost one real rejection. | — |
| **V2** barbarian refuses by force | 4/0 → 4/0 | **The axe deals 11.** | The grab doesn't start a fight (judgement call, recorded on BOARD for later). | — |
| **V3** dhampir "cousins" | 4/0 → 4/0 | **The stated Insight 18 now resolves** (`check`; it used to be ignored). | — | **TC-8c fail (engine side):** the Insight event is "Their pallor and fangs are theatrical. They are posing as vampires." That's *what*, not *why*. It's the same raw-sounding line Brendon flagged in the live room. Kit (me) narrated the motive (a costume worn for coin, and fear of the real thing), but the engine event gives no motive. This counts as NEW only because Insight used to be ignored. It isn't a regression. |
| **V4** fresco and tub | 4/0 → 4/0 | — | The detail oracle still files the carving under `area_06c/card_table/carving`. The fixture's known fact still says "A carved mountain scene", not "fresco" (TC-2 addendum). My opening named it a fresco. | — |
| **V5** cheat called out | 4/0 → 4/0 | **The marks beat is restored.** **The rapier deals 8.** | The watch is armed but no deal happens before the accusation (scenario order), so the accusation stays "unbacked" until the flip. | — |
| **V6** drawn out by noise | 3/0 → 3/0 | — | The table-talk turn still needs 40 *performed* (non-Kit) words: the previous reply failed the dry run at 37. "What's in the room now?" is still read as `social`. | — |
| **V7** haggle, refuse, play for it | 4/0 → 4/0 | (Was already all pass; it still is.) | — | — |
| **V8** blackjack, bet fifty | 4/0 → 4/0 | **20 gp stake, settled on Sleight of Hand.** | — | — |
| **V9** Fireball first | 2/**2** → **4/0** | **The whole opener works:** Fireball deals 28 fire, initiative is accepted, the fourth player and dealer take their turns, and the dealer flees blaming the others. Fire Bolt deals 9. The doppelganger blinks to the door and escapes. "Check the table" is a clean `observe` on a finished fight. | — | — |
| **V10** provoke them to swing | 4/0 → 4/0 | (Unchanged and passing.) | "Wait for them" isn't a Ready action. | — |
| **V11** flip the table | 3/1 → 3/1 | **The greataxe deals 14.** | **Stomp stall** (known follow-up, not a blocker). **Rage resistance isn't applied:** the raging barbarian took **34** bludgeoning/piercing/slashing. Strictly, rage starts on her own turn, so only the 7 after her swing should halve. `runtime/` still has no rage/resist code. | — |

The always-on checks passed on every committed turn: TC-4 no stat numbers or DCs, TC-5 narrator plus handoff, TC-3e no refreshments. The auto-flags in [auto-checks.md](auto-checks.md) are the same false positives as before: "no handoff question" on combat turns ending "Roll initiative." / "Your turn.", and "meat" in V5 is from the rapier narration.

## Skippy's known open items (non-blockers)

| Item | Result | Evidence |
| --- | --- | --- |
| A strike before initiative skips NPCs' round-1 turns | **Still open** | [fight-probes](probes/fight-probes-pr50-246779a.txt): a V2 copy after the axe hit, initiative 5. Only one NPC blow happens, three NPCs flee, and the state jumps to `round: 2`. |
| No death saves on a drop | **Still open** | A V10 copy, rapier miss: "The fourth player hits you twice: 21 bludgeoning damage. You go down." There's no dying state and the fight keeps `status: running`. |
| V11 stomp waits for an attack roll | **Still open** (known follow-up) | V11 t3 `pending_ruling`. |
| A grab doesn't start a fight | **Still open**, recorded on BOARD as for-later | V2 t3. |
| Rage resistance | **Still open** | V11: 34 taken while raging. |

## Other findings (none blocks #49 or #50)

1. **A plain stated total is read as the stake (#50, new, minor).** In a card game, "'Just roll for it. Sleight of hand, 13.'" settles "13 gp a side" instead of the agreed 10. Real Avrae output is excluded correctly, but a typed `Skill, N` total isn't. The fix is a small extension of the same exclusion. Players mostly paste Avrae, so this isn't a blocker.
2. **Insight is gated as Investigation (Call 8 / TC-8c).** The engine's Insight event on the fake vampires reports physical tells, not motive. This matches table-calls note 10: the actor motives don't include the ruse. It's the same issue Brendon raised live today. It needs its own PR (motive text for the ruse, plus skill-gated events).
3. **Flat DC 10 for social contests.** A natural 1 Persuasion (11) persuades the dealer. That's RAW-legal (no auto-fail on checks), but the dealer's Insight should probably set the DC.
4. **Validator friction caught in my dry runs.** I dry-ran every reply against a copy of the DB, so these never reached the runner:
   - "a different pattern for every high card" (describing the marks) was rejected as "Rules the running game does not use".
   - A meta table-talk turn must be `turn_mode: meta`, and only 1 Kit segment is allowed under `brief`.
   - The 40-word performed floor on table talk.
   - A `bored` mood forces a tight mirror.
5. **"Just roll" outside a card offer is `social` on #50.** On #49 any "just roll" became a card round. That's arguably better on #50, and not a regression for the scenarios.

## Method notes and comparability

- **I reused the previous rerun's committed DM replies where the engine read was byte-identical.** I wrote new replies only where the engine event changed (14 turns), using [dm-helpers/replay.py](dm-helpers/replay.py). [submit.py](dm-helpers/submit.py) dry-runs `complete` on a DB copy before handing a reply in.
  - **Rejection counts and DM latency are therefore not comparable** with the earlier runs. This run had 2 real rejections, both on V1 t3: the Harria brief guard, and my own mood-cue paraphrase. Turn times are mostly replay speed (median 3.5 s).
  - Engine time is comparable and unchanged: median 0.3 s, max 0.6 s per turn.
- **Kit-side change:** following Brendon's fresco addendum, the opening now says "a fresco of a carved mountain covers the whole north wall".
- Card deals use the engine's own random deck, so V8's hand differs from the previous run (8 → hit 10, instead of a bust). NPC attack rolls also differ (V10, V11). Damage *parsing* is deterministic and checked above.

## Verdict: are #49 and #50 mergeable?

**Yes, both are mergeable. Every blocker from the previous rerun is fixed and verified,** with no regressions in V1–V11 and green suites on both heads (450 and 492).
- **#49 `6ee802b`:** the Avrae damage line, real Fireball (DC, per-target saves, damage) and check-title skill all pass, on #49 alone and stacked. The remaining combat gaps (round-1 skip, death saves, rage resistance, stomp, grab) are the agreed follow-ups.
- **#50 `246779a`:** Avrae output is never a bet (V5 marks restored, V8 at 20 gp), and "just roll" honors the skill (V8 on Sleight of Hand), and both pass. The one new finding, a plain typed total read as a stake, is minor and fits a follow-up.
- **Merge order:** #49, then #50 (it's stacked). Brendon approves merges. Nothing was merged here.
- **Suggested next PR, not gating:** Call 8 skill gating (Insight → motive, which fixes the live-room complaint), the plain-total stake exclusion, the brief guard's `player_said`, and the combat follow-ups.

## Files

- `runs/<V#>/`: transcript.md, turns.jsonl, timing.json, kit.sqlite, action files, and `dm-replies/` (every attempt).
- `summary.json`, `auto-checks.md/json`: runner summary and auto-grade.
- `probes/`:
  - `engine-probe-pr49-6ee802b.*` and `engine-probe-pr50-246779a.*`: the scenario engine probe on each head.
  - `kit_rolls-*.txt`: direct parser calls.
  - `state-probe*-*.txt`: HP deltas, targeted Fireball, skills and stakes.
  - `fight-probes-pr50-246779a.txt`: round-1 skip and death saves.
- `dm-helpers/`: the Kit-side scripts and my running notes ([dm-notes.md](dm-helpers/dm-notes.md)).
