# Area 6c baseline scorecard (2026-10-03)

**What ran:** all 11 [variety scenarios](../6c-variety-scenarios.md) (V1–V11), each on a fresh `kit.sqlite`, against dnd-solo `main` at `f90e1af` (PR #47 merged), using the new batch runner (`scripts/kit_batch_runner.py`, dnd-solo PR [#48](https://github.com/radarsaint/dnd-solo/pull/48)). Player lines went in one per turn as scripted, with rolls reported Avrae-style as `die + bonus = total`.
**DM model:** Grok (the Grok Bot executor agent running inside Cursor) played Kit through the runner's `handoff` backend: `start` / `prepare --one-pass` / `complete`, the full packet, and the engine's own validators and retry rules (degraded after 2 rejections, abandon after 4). No `play`, no OpenAI API, no `OPENAI_API_KEY`. This box has no `cursor-agent` CLI and no CloudAgent tool, so the runner's `command` backend went unused.
**Graded against:** [table calls](../table-calls-6c-2026-10-02.md) TC checks plus each scenario's "A good DM would…". P = pass, F = fail, ~ = partial, — = not reached. "Engine" means the runtime decided the outcome before the model wrote a word.

## Pass/fail per scenario

| | Turns committed / stalled / abandoned | Scenario checks | TC-4 no numbers | TC-5 clear narrator, "Do you reply?" handoff | TC-3e no refreshments |
| --- | --- | --- | --- | --- | --- |
| **V1** bard bluffs the toll | 2 / 0 / **2** | 6b F (the demand turn was abandoned, so the toll was never raised) · 6c bluff ~ (played in speech; engine ignored the Deception roll) · 6d — · 3b Harria nerve P · 1a F ("be dealt in" isn't treated as a request to play) | P | P | P |
| **V2** barbarian refuses by force | 4 / 0 / 0 | 6d **F** (engine read "I pay with this [axe]" as *toll paid* and narrated the PC counting out 10 gp) · 3b/3d F (collar grab became "You take a look") · retreat F (axe swing treated as talk) | P | P | P |
| **V3** dhampir "cousins" | 4 / 0 / 0 | 3b ruse bends P · 3d F (stated Insight 18 ignored; only the passive tell was usable) · 6b F (no NPC demand first) · 6c F ("No toll between family, surely?" read as a *refusal*) · doppelganger distinct P | P | P | P |
| **V4** fresco and tub | 4 / 0 / 0 | 2a P (needed degraded mode; oracle filed the carving under `card_table`) · 2b key on search P · 1b P · 4c P · tub ~ (no engine path to show what's in it) · agenda pull-back P (toll raised in the act) | P | P | P |
| **V5** cheat called out | 4 / 0 / 0 | 7a P · 4c catch F (no deal ever happened, so the Perception 18 watch never paid) · accuse/void F (wrist-grab accusation replaced by the game menu) · marks found P · blame-shift P · retreat F (rapier thrust treated as talk) | P | P | P |
| **V6** drawn out by noise | 2 / 1 / 0 | seed boundary ~ (honest out-of-character line only got through via `ask_clarification`; engine first forced an in-fiction reply, and "I head on toward 6c" was refused) | P | P | P |
| **V7** haggle, refuse, play for it | 1 / **3** / 0 | **F everywhere:** line 1 "I stop at the door. 'Ten gold…?'" was resolved as *leaving through the south door*; every later line stalled with "covers area 6c only" · 6b–6e, 7a — | P | P | P |
| **V8** blackjack, bet fifty | 4 / 0 / 0 | 7c plain yes P · 1a stake F (accepted 50 gp over purse and cap, then dealt at 25 when she said twenty) · "Hit" ignored F · 7b switch to one roll F (game backgrounded mid-hand) · 1c vignette P | P | P | P |
| **V9** Fireball first | 2 / **2** / 0 | combat start F (Fireball and initiative: "Fights are not run in this slice yet"; Fire Bolt then treated as talk) · retreat/loot — | P | P | P |
| **V10** provoke them to swing | 3 / **1** / 0 | act holds P · paint wipe as evidence F (no physical resolution) · theft line ~ (NPC moves on her, but no coins leave the pot) · combat start F (stall) | P | P | P |
| **V11** flip the table | 3 / **1** / 0 | NPC instincts P · flip F (no world change; Kit had to tell the player the table still stands) · money tracking F · combat start F (stall) | P | P | P |

The always-on checks passed on every committed turn. Kit-side slip, same in all 11 openings: the dealer's segment opens with a narrated description of his voice, which should have been a Narrator line (TC-5a ~).

## Latency (wall clock, 33 committed player turns)

| | median | max |
| --- | --- | --- |
| Whole turn (prepare + model + complete) | **16.5 s** | **50.5 s** |
| Engine only (prepare + complete) | 0.3 s | 0.6 s |
| Model (Grok writing decision + performance, incl. retries) | 16.2 s | 50.2 s |

The engine adds almost no time; the model step is the whole cost. These numbers are for this agent with tools, through the handoff backend, and can't be compared with ChatGPT's 81–213 s. 24 rejections across 35 model turns, 4 turns finished in degraded mode, and 2 were abandoned. Retries account for most of the max.

## Top 5 failures, ranked by how much they hurt play

1. **Fights and physical actions don't happen.** "Swing my greataxe", "rapier through his hand", "Fire Bolt", and "stomp on their hand" are read as plain talk, with no hit, no wound, and no retreat. Fireball and initiative hard-stall. Grabs, the table flip, the coin grab, and the paint wipe change nothing in the world. This dead-ends V2, V5, V9, V10, and V11, so five of eleven scenarios hit it.
2. **The toll misreads what the player meant.** A threat with an axe is recorded as payment, and the narration says the PC counted out the gold (an agency violation). "No toll between family, surely?" is recorded as a refusal. "I stop at the door. 'Ten gold…?'" walks Nik *out of the room* and ends V7. The NPC demand only registers with exact phrasing (amount + toll word + a question, no game words nearby), and the rejection message names the wrong cause.
3. **Players' rolls don't count in conversation.** Stated Deception, Persuasion, Insight, Intimidation, and Athletics totals on social turns are ignored, so there's no contest and no result. Avrae's real output, `1d20 (12) + 10 = 22`, isn't parsed at all. A bare "I rolled 17" is taken as the natural die, so the bonus gets added twice, and anything over 20 is rejected. That means bluffing, intimidating, and reading people have no mechanics.
4. **Card game state is fragile.** "What does a lady have to do to be dealt in" isn't treated as asking to play. A 50 gp bet over purse and cap is accepted, "twenty" becomes 25, "Hit" is ignored, and "just roll for this one" isn't recognized, so the game goes to the background mid-hand. A cheating accusation gets the game menu in reply.
5. **Guard friction burns the retries.** Rejections report one error at a time with misleading text. There are false positives: "dwarf" rejected for a mountain dwarf, the label "Fresco-side player" next to "lifted" counted as a key leak, and a name the player said ("Harria") only usable in that same turn. Some rules contradict each other: a detail is demanded for the tub contents while the leak guard forbids them, and the "reject the most typical candidate" rule pushes against the one game the room can run. This is why V1 lost two turns.

**Model-side errors** (caught correctly by the guards): repeated pet names, a banned word ("honestly"), and DM-only words ("bandit", "disguise") in the private brief. Raw files: `runs/<V#>/` holds transcript.md, turns.jsonl (per-turn timings and rejections), timing.json, kit.sqlite, and the model's replies. [auto-checks.md](auto-checks.md) shows how the engine read each line.
