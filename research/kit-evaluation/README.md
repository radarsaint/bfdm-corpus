# Kit Evaluation

This directory preserves **development and playtest evidence about Kit herself**.

It is deliberately separate from the historical Brendon corpus.

Historical corpus question:
> What can we learn from Brendon's body of work?

Kit evaluation question:
> When we put the current system in front of a player, what actually works, what fails, and what must not regress?

Do not use Kit failures as evidence about Brendon's historical DM behavior.

## Current records

- [playtest-01-character-onboarding.md](playtest-01-character-onboarding.md) — 2026-09-23 character creation → campaign handoff.
- [playtest-02-area-6c-gambling.md](playtest-02-area-6c-gambling.md) — 2026-09-29 Area 6c gambling/marked-deck test.
- [6c-variety-scenarios.md](6c-variety-scenarios.md) — 2026-10-03 eleven varied Area 6c openings (bard, barbarian, dhampir, fresco, cheat, noise, toll, blackjack, three combat openers) for scripted ChatGPT runs.
- [6c-baseline-2026-10-03/SCORECARD.md](6c-baseline-2026-10-03/SCORECARD.md) — 2026-10-03 first batch run of all eleven variety scenarios (Grok as Kit via the dnd-solo batch runner, PR #48): pass/fail per check, latency, top five failures.
- [6c-rerun-2026-10-03/SCORECARD.md](6c-rerun-2026-10-03/SCORECARD.md): 2026-10-03 rerun of V1–V11 against dnd-solo PR #50 (stacked on #49), with real Avrae roll format. Fixed / still failing / newly broken per scenario vs the baseline, Skippy's open items, Avrae parsing probes, and merge readiness.
- [REGRESSION_TARGETS.md](REGRESSION_TARGETS.md) — cross-test behavioral targets.

## Evaluation discipline

Preserve:
- the user-facing failure;
- the relevant source/runtime expectation;
- whether the failure was competence, state control, voice, source use, or adjudication;
- direct user correction;
- whether a later fix was actually retested.

Do not convert every failure into a narrow sentence patch.

A recurring goal is to diagnose the **class of failure** and then test whether later versions solve it in genuinely different situations.
