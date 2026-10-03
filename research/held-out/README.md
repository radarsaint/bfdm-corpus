# Held-out evaluation sets

This directory holds the corpus's current held-out set: evidence kept away from hypothesis building so it can test those hypotheses later.

## Current set: `HO-2026-10-03-prospective-table-rulings`

Machine record: [`partition-2026-10-03.json`](partition-2026-10-03.json).

**What it is.** Brendon's first-person rulings on specific Kit table moments, recorded verbatim with their own timestamp, where the timestamp is later than the freeze point. That covers table calls, adjudication rulings, "this is how I would run it" corrections, and praise or rejection of a specific Kit move.

**Freeze point.** The author timestamp of the commit that adds `partition-2026-10-03.json`. The discovery baseline is `main` `6337f81`, and the hypothesis files it tests are listed with SHA-256 digests in the JSON.

**Why this set.**

- It is unread by construction. No item exists before the freeze, so nothing in it can have shaped the hypotheses it tests. No historical source in the corpus can make that claim. Every one has at least title and date exposure, and the legacy staging pipeline normalized the bodies of the Drive families nobody has researched yet.
- It is the best kind of evidence the corpus has: direct, first-person, contemporaneous Brendon judgment (corpus review finding 1).
- It comes from a materially different operating environment (solo, current-era, Kit-mediated), which is the comparison `longitudinal/roanoke-s3-to-s4-judgment-v1.md` says is needed next.

**Order rule (`partition_order`).** Freeze before collection. For each item:

1. Capture the ruling verbatim, with its timestamp and a reference to the Kit moment it rules on.
2. Make a blind prediction from the frozen hypotheses, given the Kit moment with the ruling withheld.
3. Score the prediction against the ruling.
4. Only after scoring may the item inform corpus hypotheses. It then moves to `DISCOVERY` with an append-only `partition_history` entry.

**Not eligible.** Anything dated at or before the freeze, including Calls 1–10, the addenda and the live-game praise in `kit-evaluation/table-calls-6c-2026-10-02.md`. Also excluded: relayed summaries, rulings given after Brendon saw a prediction for the same moment, any Kit output, and any Empire City or other historical material.

**Runtime use.** Kit engineering may act on a ruling immediately. The restriction binds the research layer: no hypothesis file under `research/` may be revised from an item until that item has been scored.

Items go in `items.jsonl` in this directory, which is created with the first item.

## Historical held-out candidate (not designated)

At War's End (`BCS-000060`–`BCS-000067`) is the least-read historical family. Only titles and dates appear in the research. It was not designated because its bodies were normalized in the legacy staging bundle, its authorship is `UNKNOWN`, and it is prep material, not live play. Brendon can designate it separately if he wants a historical held-out set as well.

## Voided sets

- `empire-city-entire-project` (2026-10-01): voided on 2026-10-03 by Brendon's ruling. See `../CORRECTIONS_LOG.md` and `../prior-dnd-solo/pr36-kit-decision-extraction/research/decision-corpus/2026-10-01/evaluation/partition.json`.
