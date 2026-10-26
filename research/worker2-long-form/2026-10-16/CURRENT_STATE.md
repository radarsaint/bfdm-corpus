# Current state — Worker 2 tranche, 2026-10-16

This note is the consumption boundary for the records in this directory. It is not a Kit configuration change.

## Consumption

`KIT_CONSUMPTION=NOT_APPROVED` for all 15 interpretive candidates and both negative findings.

Nothing in this directory is approved for runtime consumption. Nothing here was injected into Kit. `radarsaint/dnd-solo` was not edited. Kit pull request #126 was not edited. Kit's persona and runtime were not changed.

A file on a research branch does not authorize Kit to use it. A later, separate approval, plus Skippy-owned engineering and evaluation, would be required before any of these records could be consumed. This pull request does not do that work, and it is not evidence that Kit became a better Dungeon Master.

## What was preserved

- W2-20261016-01 through W2-20261016-15, as positive or interpretive candidates.
- W2-20261016-N1 and W2-20261016-N2, as negative findings.

Those ids are research-record ids only. Existing BCS, BCE, and BCR identities were not reassigned.

## What was not imported

`FULL_REPORT_NOT_IMPORTED`.

The longer analytical report from the research chat was not available in this execution environment. The embedded candidate records were preserved instead. Do not treat this directory as that longer report.

## What this is not

- Not canonical `main` until a reviewer merges it.
- Not a representative sample of the corpus.
- Not a frequency estimate.
- Not a replacement for the Season 3 integrity ledger, the landed Empire City cases, the economy longitudinal note, the bowling lead, open PR #43, or draft PR #28.
- Not semantic certification. Locator checks are in `validation-and-coverage.md`. They do not decide motive, typicality, or transfer.
- Not a reading of the prospective held-out partition. Item bodies were not opened. `research/held-out/` was not modified.

## Live authority at preservation

Checked before this branch was cut:

| Repo | `main` SHA | Compared with the research snapshot |
|---|---|---|
| `radarsaint/bfdm-corpus` | `2a650a735d8e39251979b157cf7aace9f8e443ef` | Same SHA. No drift. |
| `radarsaint/dnd-solo` | `93453a0b7cc04bfd69d7243b00dc60c0818ed740` | Same SHA. No drift. |

`bfdm-corpus` `PROJECT_CONTROL.md` on that commit still names an inspected SHA of `2b68820d445e9f6d99d021463bfd76b2f7bb257d`. That commit is the parent integrity-staging commit. `2a650a73` is the following STATUS update already contained in the inspected snapshot. It is not new drift after the research.

## Related pull requests, as they stood

- BFDM **#38** is merged (2026-10-16). It is the first-tranche Season 3 integrity staging now on `main`. It is not still a draft. This directory does not edit that ledger.
- BFDM **#43** is open and not merged (`research/bounded-judgment-2026-10-15`). BJ-001, BJ-002, BJ-005, and BJ-010 overlap records here. They were not edited.
- BFDM **#28** is an open draft and not merged (`research/phase2-decision-trajectories`). CF-03 Case B is the same housing message as W2-20261016-05. That draft was not edited and is not treated as doctrine.
- dnd-solo **#126** is open and not merged (`kit/bounded-dm-judgment`). It already points at a subset of PR #43. It was not changed, and these W2 records were not added to it.

## Held-out partition

`research/held-out/README.md` was read because the research method requires it. `partition-2026-10-03.json` was not opened. No `items.jsonl` is present. No held-out item body was read or modified.
