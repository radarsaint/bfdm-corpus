# Research Corrections Log

Purpose: preserve moments where Brendon corrects the research model itself.

These are valuable because they prevent a plausible-sounding interpretation from hardening into corpus truth.

They are **current project evidence about how to interpret the archive**, not automatically historical evidence about the campaigns.

## 2026-10-01 — S3 was being hardened into a universal model

### Overreach
Research discussion began turning:
> "this is what Brendon did in Roanoke Season 3"

into:
> "this is how Brendon DMs."

### Brendon correction
There are other seasons, and Brendon has grown substantially from Season 1 to Earthfall.

### Method change
- treat S3 as a methodology testbed / historical case study;
- compare across eras before generalizing;
- explicitly model persistent, evolved, format-specific, and abandoned practices.

---

## 2026-10-01 — Roanoke scale is a major confound

### Missing context
Some S3 conclusions were being interpreted as though they came from an ordinary 4–6 player table.

### Brendon correction
Roanoke games sometimes contained **30–100 concurrent players**.

### Method change
Every case should retain enough table/campaign context to judge transferability:
- approximate player scale;
- synchronous/asynchronous;
- single/multi-DM;
- persistent server/live table;
- operational load.

Evidence density and unusual operating constraints must not silently become universal DM preference.

---

## 2026-10-01 — "Dating sim" interpersonal play was emergent

### Risky interpretation
Social/interpersonal play could easily be described as a designed Roanoke feature.

### Brendon correction
The interpersonal material later coined the **"dating sim" was entirely emergent**.

### Method change
Research should distinguish:
- authored initial feature;
- emergent player behavior;
- DM accommodation;
- later recognition/naming;
- later formalization.

Candidate pattern to test:
> emergent practice → recognized value → later formalization

Do not assume the later label existed at the start.

---

## 2026-10-01 — Kit may need campaign-design lineage, not only DM judgment

### Narrow framing
Corpus work was centered on moment-to-moment DM decision extraction.

### Brendon correction / future use
Kit may eventually be expected to design a **Roanoke-style adventure / future Season 6**.

### Method change
Preserve a distinct campaign-design research lens:
- scheduling;
- factions;
- free play;
- multi-DM operation;
- persistent locations;
- invitationals;
- adaptive capacity;
- scale-specific mechanics.

Do not discard architecture/operations evidence merely because it does not answer a narrow DM-judgment question.

---

## 2026-10-01 — Preserve coverage before grand synthesis

### Temptation
Write a human-readable Brendon model for Kit from S3.

### Brendon correction
Other Discords still need harvesting; Drive/project sources are much broader; raw data may support uses we do not yet understand.

### Method change
- preserve first;
- normalize provenance;
- broaden source coverage;
- run multiple research lenses;
- synthesize later.

A future human-readable synopsis remains desirable, but should not be written as a final model from S3 alone.

---

## 2026-10-01 — Bowling is evidence of a wider creative search space

### Previous blind spot
The bowling conversion existed in Drive and was referenced by S3 material, but had not actually been examined.

### New evidence
The 2018 Bowling Event converts real bowling performance into D&D's resolution engine rather than merely setting an adventure in a bowling alley.

### Method change
Add a broad research question:
> What kinds of boundaries does Brendon repeatedly try to push, and how does he turn a strange idea into something playable?

This is a lead, not yet a conclusion.

---

## 2026-10-03 — The Empire City held-out set was spent, and the records said it wasn't

### What happened
On 2026-10-01, `prior-dnd-solo/pr36-kit-decision-extraction/research/decision-corpus/2026-10-01/evaluation/partition.json` quarantined the whole Empire City project (`IMP-001`–`IMP-015`, catalog `BCS-000001`–`BCS-000015`) as `EVALUATION_QUARANTINE`. The plan was to build hypotheses from Roanoke and then test them against Empire City material no one had read.

On 2026-10-02 the Empire City Discord harvest was ingested (`888c0e7`) and a deep pass read the project and built discovery research from it. The promotion gate ("freeze discovery hypotheses and record their commit before reading quarantine content") was not followed. Nothing recorded the change, and all 15 catalog records kept saying `EVALUATION_QUARANTINE` / `NOT_READ_THIS_PASS`. The 2026-10-03 corpus review (dnd-solo draft PR #67, finding 2) caught it.

### Brendon ruling
> Void the Empire City quarantine, log what was gained, and name a new held-out set.

### What was gained from reading Empire City (all now discovery)
- `empire-city/decision-cases-v1.md`: 8 bounded decision cases (`BDC-S4-001`–`BDC-S4-008`).
- `empire-city/longitudinal-decision-cases-v1.md`: 17 prep → play → aftermath cases (`BDC-S4-L01`–`BDC-S4-L17`) plus a cross-case distillation.
- `empire-city/design-method-synthesis-v1.md`: the S4 design-method model.
- `empire-city/source-fragment-map-v1.md`: the map from historical and folkloric fragments to table functions.
- `empire-city/player-feedback-v1.md`.
- `longitudinal/roanoke-s3-to-s4-judgment-v1.md`: the S3 → S4 comparison and its persistence and scope labels.
- `creative-method/historical-mythologization-v1.md`, `cryptids-s3-s4-v1.md` and `mythic-institutions-s3-s4-v1.md`: the Empire City halves of the cross-season comparisons.
- Facts resolved: Brendon's S4 Discord identity (user ID `313689699627696139`), the July 10, 2021 Week One boundary (`BCS-000003`), the stock-market implementation, and the "seat of the empire" naming explanation.

That is the first cross-season comparison the corpus has had. Without it, every claim would still be S3-only.

### What was lost
- No clean historical test set remains. Any hypothesis that S3 and S4 now share was built with both, so agreement between them is a developmental lead, not a held-out confirmation.
- Whether the Drive bodies of `BCS-000001`–`BCS-000015` were read, or only their titles and dates were cited, was never recorded. All 15 are now treated as exposed.

### Method change
- The quarantine is void. `partition.json` keeps its 2026-10-01 fields and gains an append-only `status_history` and `void` block. The 15 catalog records move to `DISCOVERY` / `EXPOSED_QUARANTINE_VOIDED`, with their prior values kept in `partition_history`.
- New held-out set: `HO-2026-10-03-prospective-table-rulings` (`held-out/partition-2026-10-03.json`). It covers Brendon's verbatim rulings on Kit table moments dated after the freeze commit, scored by blind prediction before they may inform any hypothesis.
- Freeze before reading. A held-out set has to be frozen, with its hypothesis commit recorded, before anyone reads its contents. Reading quarantined material without a recorded freeze is a correction-log event, logged the same day.

---

## Rule

When later research invalidates or substantially refines an earlier synthesis:
1. preserve the old interpretation in history;
2. record the correction;
3. state what evidence caused the change;
4. update current synthesis;
5. do not silently rewrite the record as though the earlier mistake never happened.
