# Engine probes (2026-10-03, dnd-solo e6d08cc)

These are engine-only checks: `python3 -m runtime.kit_agent prepare --one-pass` was run on **copies** of the rerun's `kit.sqlite` files, and nothing was committed. Each one checks one of Skippy's open items, or the Avrae parsing, outside the scripted lines.

| Probe | DB copy | Action file | Engine result |
| --- | --- | --- | --- |
| Strike first, then roll initiative low | V2 after the axe hit (fight awaiting initiative) | `a_init.txt` (`**Initiative**: 1d20 (3) + 2 = 5`) | "Turn order: the fourth player, the dealer, the door-side player, the fresco-side player, you." Next comes one NPC volley, the dealer flees, and then "Your turn." State says `fight.round: 2`. The four NPCs ahead of the PC never got their round-1 turns: the opener counted as the PC's round-1 action, and the order jumped to round 2. **Still open.** |
| PC takes a blow at low HP | V10 after round 1 (Wren 21 hp, 13 taken) | `a_w.txt` (rapier miss) | "Your rapier misses the dealer. The fourth player hits you once: 14 bludgeoning damage. You go down." State: `damage_you_took: 27`, the fight is still running at round 3, and there is no dying or stable status. `runtime/` has no death-save code at all (grep "death": none). **Still open.** |
| PC swings after taking 43 damage while raging | V11 end | `a_atk.txt` | The miss resolved, and the doppelganger fled. Separately, the V11 run itself shows the raging barbarian taking the full 43 bludgeoning/slashing/piercing. **Rage resistance is not applied** (`runtime/` has no "rage" or "resist" handling). |
| Fireball, three formats | V4 end (no fight) | `a_fb.txt` | `Damage: 28 fire` works: two players drop, two are hurt, and the engine asks for initiative. The real Avrae output `**Damage**: 8d6 (4, 3, …) [fire] = \`28\`` gives "Roll the Fireball damage in Avrae". **Real Avrae spell damage isn't parsed.** |

`kit_rolls` direct calls (Python):

| Input | Result |
| --- | --- |
| `Sela makes a Persuasion check! 1d20 (12) + 10 = \`22\`` | `check_roll` → total 22, **label None** (the skill in the Avrae title is dropped) |
| `Persuasion: 22` | total 22, label `persuasion` |
| Avrae attack block `**To Hit**: 1d20 (13) + 7 = \`20\`` / `**Damage**: 1d12 (8) + 6 [slashing] = \`14\`` | `damage()` → `[(20, None)]`: **the to-hit total is used as damage**, and the damage type is lost |
| `**Damage**: 8d6 (…) [fire] = \`28\`` | `damage()` → `[]` |

In the committed runs the wrong damage shows in the trace: V2 dealer `takes 18` (Avrae damage was 11), V5 `takes 17` (8), V9 `takes 19 fire` (9), V11 `takes 20` (14).
