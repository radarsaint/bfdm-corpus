# Research Method

## Research purpose

The original narrow question remains useful:

> Given a situation at the table, what makes Brendon notice something, care about it, intervene, leave it alone, escalate it, reward it, change preparation, improvise around it, or decide that something is not working?

The corpus also supports broader questions about:
- creative method
- mechanical design
- campaign architecture
- worldbuilding
- revision/failure diagnosis
- development over time
- unusual experiments with the form of D&D

Do not force every source through one question.

## Archive-first research constraint

The BFDM corpus is a durable historical/research archive first.

Kit is one consumer.

Therefore research must never discard, flatten, or rewrite source material merely because it does not fit a current training, retrieval, prompt, or evaluation format. Model-facing datasets are derived research products and should remain reproducible from the underlying archive/evidence chain.

The method should answer research questions about Brendon's creative history on their own terms, including questions that may have no immediate Kit application.

That archive-first constraint does **not** mean researchers should ignore Kit's future judgment needs. Completing BFDM has several explicit objectives, all of which matter:

1. **Historical understanding.** Reconstruct Brendon's creative methods, demonstrated judgment, decisions, mistakes, development, and their circumstances.
2. **Archival completion.** Extract useful knowledge from large historical sources that also contain substantial unrelated material.
3. **Portable preservation.** Keep the valuable research in a durable form that does not require future systems to ingest the full historical archive.
4. **Archive retirement.** Eventually permit the raw corpus to become private and active excavation to conclude, subject to preserving necessary evidence and provenance.
5. **Future cognition.** Deliberately research knowledge that could inform Candy C's eventual contextual judgments and learning. Candy C, short for candidste c, is the planned name of a future GitHub repository for Kit's planned Bayesian drive. It does not exist. Do not create it. Do not treat a mention of it as an implementation.
6. **Satisfaction.** Investigate why experiences succeed or fail for players, DMs, and Brendon. Distinguish intended effect, expressed preference, immediate response, and longer-term satisfaction.

Completion of archival extraction is a legitimate milestone. It is not proof that the Bayesian drive works. Stage 3/4 cognition implementation remains deferred. Research should still target the future knowledge those stages will need.

The planned Bayesian drive is a KRABS extension intended to support context-sensitive, evidence-informed judgment about which DM interventions, including restraint, are most likely to produce satisfying play. Choosing a Bayesian approach does not establish a model, priors, likelihoods, update rules, or satisfaction measures. Those remain unresolved. The drive is not all of Kit's cognition.

## Observed behavior, reconstructed judgment, effectiveness, and transfer

Keep these four questions distinct in every case, contrast, and synthesis:

1. **Observed behavior.** What did Brendon demonstrably do? Quote or cite the action, restraint, timing, and circumstances from primary evidence.
2. **Reconstructed judgment.** What circumstances and considerations may explain the choice? Separate contemporaneous statements of intent from later recollection and from inferred motive.
3. **Evaluated effectiveness.** What evidence shows whether that choice produced a satisfying or otherwise desirable result? Distinguish player-character reactions from player evaluations, immediate response from longer-term satisfaction, and actual outcomes from imagined counterfactuals.
4. **Transferable knowledge.** What, if anything, could another DM reasonably use in a different situation? A resemblance to historical Brendon is not automatically an example of the best DM decision.

These must not collapse into one another.

Historical choices are not automatically optimal. Kit is intended to become capable of surpassing Brendon's demonstrated expertise. Reproducing Brendon's historical choices is therefore insufficient as a research or product success condition.

Researchers should explore competing explanations, failures, exceptions, and cases where different circumstances produced different interventions. A finding may legitimately conclude that the evidence is insufficient to determine which alternative would have been better.

Do **not** require invented alternatives, numeric probabilities, satisfaction scores, or a premature machine-readable schema.

Do not treat participation, laughter, completion, or continued play as proof of satisfaction.

## Method example: BFDM PR #58 (unapproved)

Use [PR #58](https://github.com/radarsaint/bfdm-corpus/pull/58) as a research-method example of the distinction above. Do not change, merge, restamp, or approve it from this method file. It is unapproved actual-play research, not doctrine, and not a Kit input.

- The **Fishmother oasis** sequence shows a player-created institution receiving faction recognition and a labor-scaled reward.
- The **Twilight Manor** sequence shows a high-investment emotional appeal receiving repeated nonresponses before a mundane development.
- The **Clocktower** sequence shows Kit-relevant distinctions between preserving an obstacle, allowing consequences, and warning a player outside the fiction.

These examples do not establish a universal rule about rewarding investment, refusing intervention, or warning players. They identify different contexts, actions, and possible research questions. No finding from them establishes probabilities of player satisfaction without adequate outcome evidence. An example resembling Brendon's historical behavior is not automatically an example of the best DM decision.

## Four-layer discipline

Keep these layers separate:

1. **Source archive** — what material exists?
2. **Attributable evidence** — what bounded contribution can be tied to Brendon?
3. **Derived research** — what might the evidence mean? Derived research must still mark whether a claim is observation, reconstructed judgment, evaluated effectiveness, or a transfer candidate.
4. **Runtime curation** — what, if anything, should Kit actually use?

The four-layer discipline and the four research questions above are complementary. A source can support an observation without supporting an effectiveness claim. A derived interpretation is not transferable knowledge merely because it is interesting.

Use the existing provenance ontology where available:
- `BCS-######` — source container
- `BCE-######` — attributable evidence
- `BCR-######` — supported relation

Derived research is never a replacement for source/evidence.

## Two axes: confidence and scope

Do not use one ladder for both certainty and generalization.

### Evidence confidence

- **DIRECT / EXPLICIT** — statement, correction, signed contribution, attributable comment, or clear attributable revision.
- **STRONGLY RECONSTRUCTED** — chronology and source comparison support the claim with little ambiguity.
- **SUGGESTIVE** — plausible but meaningful alternative explanations remain.
- **UNRESOLVED** — evidence is insufficient or conflicting.

### Claim scope

- **EVENT_SPECIFIC**
- **CAMPAIGN_SPECIFIC**
- **FORMAT_SPECIFIC**
- **ERA_SPECIFIC**
- **CROSS_CAMPAIGN_CANDIDATE**
- **DEVELOPMENTAL**
- **GENERAL_CURRENT_PRACTICE_CANDIDATE**

A claim can be DIRECT and still remain EVENT_SPECIFIC.

High confidence never silently widens scope.

## Source classes

Distinguish at least:

- contemporaneous prep
- live-play record
- change log / design note
- revision delta
- attributable comment
- playtest correction
- postmortem
- retrospective self-report
- collaborative/project context
- third-party context
- derived analysis
- current project directive

Brendon's present recollections about older games are `RETROSPECTIVE_SELF_REPORT`: direct evidence of his present recollection/interpretation, not a substitute for contemporaneous records.

## Claim-specific source authority

There is no universal source type that always wins.

Ask what claim is being made.

- **What was delivered/recorded in play?** Prefer captured live evidence over stale prep.
- **What was documented before play?** Prefer dated prep/revision history.
- **Why does Brendon say he made a choice?** Prefer an explicit contemporaneous comment or retrospective self-report.
- **What actually caused the change?** Compare chronology, semantic delta, live triggers, and stated reasons; preserve unresolved causes.

A live Discord archive establishes what is **documented in the captured live record**, not everything that happened.

A dated prep artifact establishes what was **documented in that artifact**, not everything Brendon privately intended.

## Revision-aware causality

A timestamp is not a motive.

Useful labels:
- `PREP_DRIVEN`
- `LIVE_OPERATIONAL`
- `LIVE_RESPONSE`
- `PREPARED_ADAPTABILITY`
- `MIXED / UNRESOLVED`

A strong `LIVE_RESPONSE` reconstruction should have:
1. a dated pre-change baseline;
2. a meaningful semantic delta;
3. a live trigger before the change;
4. preferably downstream delivery tied to the same trigger.

If one element is missing, narrow the claim.

## Identity and authorship

Screen names change across seasons.

Use [IDENTITY_RESOLUTION.md](IDENTITY_RESOLUTION.md).

Prefer immutable platform IDs and server/date-specific alias mappings. Do not globally attribute a nickname without a supported identity link.

Keep separate:
- project ownership
- message/passage authorship
- decision authority
- delegated implementation

A collaborator's work can belong to a Brendon-run campaign without becoming Brendon-authored evidence.

## Campaign-context metadata

Research cases should record, when available:
- campaign/project
- approximate date
- table/player scale
- synchronous vs asynchronous
- single-DM vs multi-DM
- live table vs persistent server
- session-time pressure
- degree of authored structure
- relevant collaborators
- evidence phase: prep, live play, postmortem, retrospective

This prevents a Roanoke-scale solution from becoming a universal small-table rule.

## Development over time

Do not flatten early and late Brendon into an average.

Look for:
- persistent traits
- evolved practices
- format-specific adaptations
- abandoned/superseded practices
- explicit later contradictions
- emergent behaviors later formalized

A useful candidate pattern is:

> emergent practice → recognized value → later formalization

The interpersonal/social layer later called the "dating sim" is one candidate, but its chronology still needs source work.

Do not assume "newer always wins." Later work may be different because the task changed.

## Negative-space research

Visible changes are easier to extract than restraint.

Deliberately sample:
- player activity left alone
- prep left unchanged despite attention
- ideas considered but rejected
- hooks allowed to fail
- NPCs/mechanics not promoted
- functioning scenes not "improved"

Without negative-space cases, Kit would be overtrained to intervene.

## Coverage and survivorship

Archive density is not prevalence.

Before making absence/frequency claims across eras, check whether the compared periods have comparable:
- Discord coverage
- revision coverage
- voice/off-platform capture
- document survival
- authorship resolution

S3's density must not masquerade as importance or frequency.

The twenty decision cases in `research/roanoke-s3/decision-cases-v1` are a curated sample. How they were chosen is not documented well enough to call them representative. `research/integrity/README.md` is the contract that keeps that sample from being treated as a model, and it records the separate sampling phase required before any generalized judgment. This method does not start that phase.

## Derived-research independence

Do not count multiple analyses of the same underlying source as independent confirmation.

S3 v1/v2/v3, prior `dnd-solo` studies, syntheses, and longitudinal cases are navigation and hypothesis tools.

New claims should trace to source/evidence:

`derived claim -> BCE/equivalent evidence -> BCS source container -> native/portable source`

If the chain breaks, the conclusion is not source-ready.

## Discovery vs evaluation

Where material has been designated held-out/evaluation-only, respect that partition.

Do not use evaluation-quarantined sources to build the hypothesis that they are meant to test.

The current held-out set is described in `held-out/README.md`. Freeze a held-out set and record its hypothesis commit before anyone reads it. If quarantined material is read without that freeze, record it in `CORRECTIONS_LOG.md` the same day.

When practical, formulate the research question before opening held-out evidence.

## Keep the archive open-ended

The corpus may support:
- human-readable synthesis
- retrieval
- evaluation
- preference/judgment training
- creative apprenticeship
- design assistance
- campaign-format reconstruction
- longitudinal creative research
- voice/style distillation
- later Candy C / Bayesian-drive knowledge requirements, without implementing that drive here

Do not choose one use early and discard information needed for others.

The planned portable research destination is Candy C. Describe it; do not create it. Transfer method, schema, and selection rules remain unresolved.

## Promotion into Kit

No research artifact becomes Kit behavior automatically. A verified evidence chain is not that permission, and a file on canonical main is not Kit configuration. An example that resembles Brendon's historical behavior is not automatically an example of the best DM decision, and is not Candy C.

Future promotion should be deliberate and traceable:

`Kit behavior/seed -> curated derived record -> BCE evidence -> BCS source -> native/portable source`

A compact voice payload is one possible downstream artifact for expressed table voice. It is not a substitute for judgment/personality research.

## Default research posture

Prefer:
- narrower supported claims over elegant broad theories;
- unresolved causality over invented motive;
- contradictory evidence preserved together;
- source history over cleaned narrative;
- explicit correction over silent reconciliation.

The standard is not "does this interpretation sound like Brendon?"

The standard is "can another researcher reconstruct why we believe it, see the limits, and disagree intelligently?"
