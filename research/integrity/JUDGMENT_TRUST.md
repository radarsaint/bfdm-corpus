# Judgment trust

**Status:** canonical fail-closed contract for derived DM judgment.  
**Practice status:** NOT_A_STANDING_PRACTICE.

A citation is not a verdict. A confidence label is not a verdict. A draft contrast is not a verdict. A finished research pass is not a verdict. None of those authorize Kit.

## What counts as a verdict

Semantic status for a derived proposition lives only in:

- `research/integrity/audit_ledger.jsonl` for the audited Season 3 tranche;
- `research/integrity/contrast-family-verdicts.jsonl` for contrast families CF-01 through CF-10;
- `research/integrity/judgment-claim-register.jsonl` for which files are allowed to state reusable judgments, and at what trust.

Narrative research may keep its original wording. That wording stays derived wording. The register says how it may be used.

## Defaults

| Situation | Status |
|---|---|
| No ledger row | `UNVERIFIED` |
| Confidence label of high or very high | original claim, not a verdict |
| Open or unmerged PR | not canonical |
| `SOURCE_RESEARCH_READY` | the source can be researched, not that a judgment is true |
| Workbench or design text | not live play |
| Assistant text in a ChatGPT recovery | not Brendon authorship |
| Search summary marked non-verbatim | not a quotation |
| One reviewed case | not frequency, typicality, or transfer |
| Reusable judgment inside the Season 3 tranche | overclaimed; not standing practice |
| Contrast family | `NOT_CERTIFIED` until its verdict row says otherwise |
| Kit use | `NOT_AUTHORIZED` |
| Owner attestation of a container | authorship of that container, not verification of a derived judgment |

`NOT_COMPARABLE` means this searched surface cannot decide the hypothesis. It does not mean the behavior is absent from the campaign.

## Contrast families

PR #28 (`research/phase2-decision-trajectories`) states ten hypotheses and labels most of them high confidence. Those labels were not adopted. The adversarial record is `contrast-family-adversarial-v1.md`. No family is standing practice. The hypothesis file on that branch was not rewritten, so a later merge cannot silently become the verdict: `scripts/validate_judgment_trust.py` rejects a research file that states a reusable judgment or a high-confidence claim without `NOT_A_STANDING_PRACTICE` in its opening.

## What would be required before any family becomes practice

`research/METHOD.md` already requires a separate sampling phase before a generalized model: more than one campaign and period, more than one format, ordinary and unsuccessful decisions, restraint and contradiction, written selection rules, tests that can fail, and held-out sources.

Until a file named `research/integrity/SAMPLING_PHASE_COMPLETE` exists, the validator rejects every contrast family whose `practice_status` is anything other than `NOT_A_STANDING_PRACTICE` or whose `kit_status` is anything other than `NOT_AUTHORIZED`. Creating that marker is a deliberate act. This pass does not create it.

## Machine check

`scripts/validate_judgment_trust.py` fails closed when:

- a research Markdown or JSONL file states a reusable judgment, an underlying principle, or a high confidence label without `NOT_A_STANDING_PRACTICE` in the opening;
- a triggered file is missing from the register;
- a register row authorizes practice or Kit;
- a contrast family is missing, adopts its draft confidence label, or is marked as a passed independent test while the sampling marker is absent;
- a training status is approved.

The generated Season 3 review packet is exempt from the banner scan because its digest is bound by `scripts/validate_research_evidence.py`. That validator still requires the curated-sample boundary, including the sentence that a passed evidence chain does not authorize Kit.
