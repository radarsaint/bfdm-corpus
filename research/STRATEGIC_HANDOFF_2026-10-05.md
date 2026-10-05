# BFDM / Kit Strategic Handoff — 2026-10-05

**Status:** current project-direction handoff  
**Evidence status:** project decisions, architecture direction, sequencing, and planning context; **not historical BFDM evidence**  
**Canonical code/source state at creation:** `bfdm-corpus main @ 65513f294e72a3eb961d5699c21ddc1f14ceef2c`

This document preserves the high-level planning state that had accumulated in a long-running ChatGPT project thread. It exists so future agents do not have to reconstruct the project's direction from scattered chats, PR descriptions, or stale handoffs.

Read this together with:

- `research/NEXT_HANDOFF.md` for immediate repository state;
- `research/PROJECT_DECISIONS.md` for standing research guardrails;
- `CORPUS_CHARTER.md` for archive invariants;
- `research/RESEARCH_STATE.json` for machine-readable status.

When those documents disagree on current repository state, prefer the newest canonical `main`. When they differ on project intent, this document records the current high-level direction as of 2026-10-05.

---

## 1. North star

The project is not "build a RAG chatbot that imitates Brendon's prose."

The intended end state is one persistent, capable Dungeon Master.

Brendon's own north-star statement from the planning thread should be preserved literally because later paraphrases tend to shrink the ambition:

> Kit. Is a dm.  
> Kit is my dm.  
> Kit is a dm. I'd like to hand to a friend.  
> Kit is a campaign designer.  
> Kit is a roanoke style campaign designer.  
> Kit understands dnd.  
> Kit understands how I handle a table and can do it for others.  
> Kit can globally run a server the way I would run it if I could be multiple places at once.  
> Kit uses my documented experience for the campaign level stuff.  
> Currently kit is a pretty good dm who has some mechanical issues.  
> Kit over the long haul with a large flexibility to do what I wish I could do, but better is where this is going.

The project should not quietly downgrade that target into "a competent solo chatbot." The long-term quality target is a DM capable enough that a player could prefer Kit to an experienced human DM, while retaining the flexibility to design and operate campaigns at scales Brendon cannot personally cover alone.

The long-horizon target is therefore broader than `dnd-solo`, broader than the BFDM corpus, and broader than a personality prompt.

The target is a persistent DM cognition that can scale from:

1. one-player live play;
2. ordinary campaign DMing;
3. campaign co-design;
4. autonomous long-running campaign operation;
5. multi-player / multi-scene persistent operation;
6. Roanoke-scale production and coordination.

The current runtime is already capable enough to fail in specific, diagnosable ways. The work now is increasingly about improving judgment, memory, planning, human usability, and campaign-scale cognition rather than proving that an AI can narrate a D&D room.

---

## 2. Repository roles

### `radarsaint/bfdm-corpus`

This is the durable archive and research environment for Brendon's D&D creative history.

Its governing invariant remains:

> The corpus is a durable research archive. Kit is one consumer of it.

It preserves:

- source history;
- provenance;
- Discord archives and projections;
- Drive documents;
- revisions/comments where available;
- project-history conversations;
- attributable evidence;
- research artifacts;
- evaluation material;
- historical contradictions and failures.

The corpus must remain useful even if Kit is replaced.

### Human / arbitrary-agent accessibility invariant

A second archive invariant emerged from the retrieval failures that motivated this work:

> **No textual historical content may be effectively hidden behind a binary container, Git LFS pointer, opaque database, embedding index, or proprietary retrieval layer as its only practical discovery path.**

Where the canonical source format is binary or otherwise hostile to ordinary model/research access, preserve:

- the canonical/raw source;
- a UTF-8 searchable projection when text exists;
- provenance connecting the projection to the source;
- rebuildable indexes;
- asset metadata where non-text assets matter.

This creates a **research access plane** separate from whatever memory/retrieval architecture Kit eventually uses.

Acceptance test:

> A researcher or arbitrary capable AI with repository access, but without Kit's private memory system, vector database, or special retrieval service, should be able to discover ordinary names, phrases, concepts, mechanics, and ideas and reach enough source context to verify them.

The Sandigil/Git-LFS failure is the canonical warning case: information that technically exists but cannot be inspected by the working research agent is functionally unavailable.

### `radarsaint/dnd-solo`

This is the current executable DM/runtime surface:

- game state;
- room loading;
- adjudication;
- NPC agendas/knowledge;
- turn execution;
- campaign/runtime content;
- player-facing performance;
- tests and playtest traces.

It is not "all of Kit."

### Future Kit cognitive layer

The eventual long-term cognition may sit beneath or alongside `dnd-solo` and future campaign/server surfaces.

Likely concerns include:

- campaign cognition;
- episodic memory;
- semantic/professional memory;
- procedural knowledge;
- entity cognition;
- active attention;
- deferred commitments;
- strategic vs local planning;
- consolidation/learning.

Do not prematurely force these into one database, one RAG layer, or one architecture. Stage 3 experiments should reveal what is actually required.

---

## 3. Canonical corpus state after consolidation

As of this handoff:

- canonical `main`: `65513f294e72a3eb961d5699c21ddc1f14ceef2c`;
- canonical BCS range: `BCS-000001` through `BCS-000172`;
- PR #31 substrate hardening is merged;
- PR #36 reconciled source ingests are merged;
- donor PRs #32, #34, and #35 are closed without merge.

The reconciled additions are:

- `BCS-000131–000151`: 21 historical/research-critical sources;
- `BCS-000152–000162`: 11 Earthfall ChatGPT Project-history sources;
- `BCS-000163–000172`: 10 Saturday D&D ChatGPT Project-history sources.

The combined non-Discord document index was rebuilt after reconciliation.

Known validation at merge time included:

- ingest validation;
- registry validation;
- source-history validation;
- substrate query tests;
- source-readiness tests;
- source-history query tests;
- SQLite integrity and foreign-key checks.

Two catalog-only records remain pre-existing exceptions: `BCS-000059` and `BCS-000068`.

Earthfall and Saturday D&D Project-history recoveries remain explicitly partial.

---

## 4. Research sequence

The project deliberately moved away from "archive -> big cognitive architecture."

The current sequence is:

### Stage 1 — Make history researchable

Includes:

- Discord accessibility;
- Drive/source integration;
- provenance;
- source families;
- source-history traversal;
- archive/evidence gap accounting;
- model-facing projections;
- research usability.

**Current state:** substantially landed and hardened. Remaining gaps are bounded and should not block the next research stages.

### Stage 2 — Reconstruct expert judgment and creative method

This has two distinct lanes.

#### Phase 2A — Live judgment

Question:

> Given a situation at the table, what makes Brendon notice something, care about it, intervene, leave it alone, escalate it, reward it, change preparation, improvise around it, or decide something is not working?

Primary research unit:

```text
situation
-> critical cues
-> recognized problem
-> concern / intent
-> candidate actions
-> intervention or restraint
-> immediate result
-> later consequence
-> correction / reinforcement / change
```

The existing contrast-family draft is PR #28.

Earthfall and Saturday D&D workbench sources should now be used to **attack** the existing S3/S4 findings.

Use classifications such as:

- SUPPORT
- LIMIT
- BREAK
- NEW_DIMENSION
- NOT_COMPARABLE

Do not force new evidence into an existing family merely because it resembles one.

### Current Phase 2A contrast families

These are provisional research products on PR #28, not doctrine. Preserve their actual shape so future agents do not reduce Phase 2 to a vague instruction to "study judgment."

- **CF-01 — Handwave procedure vs preserve the problem.** Procedure can disappear after its uncertainty/function is exhausted; preserve it when it still carries unresolved consequence.
- **CF-02 — Support player-created play vs stop authoring it for them.** Player investment increases the obligation to support the world around the concern, not the DM's right to decide the outcome.
- **CF-03 — Reward creativity vs reject a cool request.** Creative proposals are tested against rules, fairness, intended pressure, collaborator ownership, and future shared cost.
- **CF-04 — Discard/defer prepared form vs preserve delayed prep.** Evaluate whether the purpose and assumptions still survive at delivery time; schedule drift alone does not invalidate useful prep.
- **CF-05 — Patch locally vs rewrite architecture.** Intervention scale should reach the actual causal layer; local failures get local fixes, structural failures can justify structural rewrites.
- **CF-06 — Refuse preclaimed authority vs grant earned authority.** Shared authority is guarded against unilateral preallocation but may be delegated aggressively when earned through live responsibility.
- **CF-07 — Let the world move vs stop simulation at an eligibility boundary.** Autonomous world causality operates only inside actions that are legitimate under table contracts.
- **CF-08 — Preserve intended pressure vs repair illegible pressure.** Challenge can remain while telegraphing/trust is repaired when players could not reasonably perceive the stakes.
- **CF-09 — Reduce authored density vs add missing late structure.** Late-campaign prep may need either more player-led space or more connective structure depending on what the campaign has accumulated and what is missing.
- **CF-10 — Central authority vs collaborator sovereignty.** Central coordination does not imply universal authorship; collaborator ownership and campaign-level stewardship must be distinguished.

The first stress pass did **not** kill any family. It narrowed three, added support to two, and left five substantially unchanged. That result remains lineage-limited because the stress evidence was still within the Roanoke/S3-S4 family. Earthfall and Saturday D&D are valuable precisely because they can break that concentration.

#### Phase 2B — Creative method / worldbuilding

Question:

> Given design artifacts themselves, how does Brendon turn ideas into playable worlds?

Evidence may include:

- authored design artifacts;
- development/revision history;
- worldbuilding structures;
- institutions;
- mechanics;
- campaign premises;
- scenario scaffolding;
- constraints that make ideas playable.

Design evidence can support design-method claims without live-play confirmation.

Do not convert a design claim into "this worked at the table" without separate evidence.

### Stage 3 — Minimal cognition tests

Only after enough strong Stage 2 material exists.

Stage 3 is deliberately earlier than most heavy Stage 4 implementation. The project should discover what cognition is actually required by making cheap candidate systems fail in controlled ways.

Candidate work includes:

- decision recognition/classification;
- compact precedent cards backed by rich cases;
- simple typed retrieval;
- context assembly;
- deferred binding;
- attention representation;
- campaign simulation.

Stage 3 should use the cheapest mechanism that can falsify the hypothesis.

Keep two representations when precedent work begins:

1. the **rich research case** with chronology, evidence, uncertainty, alternatives, retrospective interpretation, and counterfactuals;
2. the **compact precedent card** containing only what comparison/retrieval needs.

The compact card never replaces the rich case.

Historical disagreement should remain representable through relations such as:

- `CORRECTED_BY`;
- `SUPERSEDED_BY`;
- `DIFFERS_BECAUSE`;
- `CONTRADICTS`;
- `COUNTEREXAMPLE_TO`;
- `NEGATIVE_PRECEDENT_FOR`.

A later different decision does not automatically prove the earlier decision was wrong.

Do not jump straight to GraphRAG, spreading activation, learned rerankers, or elaborate memory graphs unless simpler methods fail.

### Stage 4 — Architect from observed failures

Only after Stage 3 reveals actual needs.

Likely later concerns:

- campaign cognition;
- long-term memory;
- strategic/local execution;
- entity cognition;
- durable workflows;
- learning/consolidation;
- server-scale operation.

---

## 5. Contemporaneous DM workbench evidence

A major correction from this planning thread is that ChatGPT Project histories, especially Earthfall and Saturday D&D, are not merely design docs.

They often function as a **contemporaneous DM workbench** immediately before, during, and after sessions.

Treat this as its own evidence family:

`CONTEMPORANEOUS_DM_WORKBENCH`

Useful narrower states include:

- PRE_SESSION_PREP
- LIVE_REACTIVE
- MID_SESSION_SELECTION
- MID_SESSION_ABANDONMENT
- IMMEDIATE_POST_SESSION
- LATER_RETROSPECTIVE

AI-assisted material must preserve the difference between:

1. AI proposed;
2. Brendon requested;
3. Brendon rejected;
4. Brendon modified;
5. Brendon selected;
6. likely intended for imminent use;
7. known table delivery;
8. later evaluation;
9. later change.

Critical rule:

> Generation ≠ authorship ≠ acceptance ≠ implementation.

Explicit rejection can be stronger evidence than the surviving generated artifact.

A useful workbench decision trajectory is:

```text
table/problem context
-> Brendon notices
-> criterion / concern
-> candidate
-> acceptance / rejection / correction
-> replacement/change
-> delivery known or unknown
-> later evaluation
```

Earthfall and Saturday D&D now provide important cross-format evidence because they are recent, table-adjacent, and substantially different from S3/S4 persistent multi-DM Roanoke.

### Evidence families are not one hierarchy

The project should preserve several evidence families because they answer different questions:

- authored design artifacts;
- revision history;
- play records;
- contemporaneous DM-workbench records;
- immediate post-play evaluation;
- corrections and rejection evidence;
- project-development behavior.

There is no single global ordering where one family always outranks the others.

Examples:

- a design artifact can strongly support a creative-method claim while saying nothing about live performance;
- a play record can establish what happened without explaining why Brendon chose it;
- a contemporaneous workbench correction may expose decision criteria more clearly than the polished artifact that survived;
- an explicit rejection can be stronger negative evidence than a later surviving generated proposal;
- a retrospective explanation can illuminate intent while still being retrospective rather than contemporaneous.

Research claims must name the evidence family that can actually support them.

---

## 6. Human-object index: the missing human interface

The corpus is increasingly **source-addressable**:

- BCS IDs;
- Drive IDs;
- Discord message IDs;
- source families;
- revision edges;
- project IDs.

That is necessary for research and provenance.

It is not sufficient for human use.

Brendon thinks in finite nouns and concepts:

- Daysong;
- Sandigil / Gil;
- Ferrytown;
- Golden Dawn;
- Fryvern;
- R.O.D.;
- The Rowing Oak;
- crafting;
- Pale Night;
- House of Measured Coin;
- Mirabelle;
- Monster Chess;
- and hundreds of other people, places, factions, systems, events, and ideas.

The required second axis is a **corpus-wide human-object index**.

PR #33 is the current prototype.

### Governing retrieval rule

> Resolve the human thing first. Then determine where it exists.

Do not search Empire City or S3 first merely because those sources are dense.

The index must be corpus-wide from the outset. Coverage may be uneven; scope must not be.

The human-object layer is a **derived, rebuildable, provenance-backed projection**, not an unsupported wiki and not a replacement for source truth. Automation may propose candidate objects, aliases, assertions, and merges, but it must not silently canonize identity merges.

Ambiguity is a valid result. If two historical objects plausibly share a name or alias, return ambiguity rather than picking the most frequent campaign or the densest source by default.

Expected object classes include:

- CHARACTER / PERSON
- PLACE
- ORGANIZATION / FACTION / INSTITUTION
- ITEM / ARTIFACT
- CREATURE / SPECIES
- MECHANIC / SYSTEM
- EVENT / ARC
- CAMPAIGN / PROJECT
- CONCEPT / LORE IDEA
- ASSET where canonical visual identity matters

Each object should support:

- stable identity;
- canonical name;
- aliases;
- project associations;
- literal facts;
- explicit unknowns;
- conflicts;
- typed relationships;
- source anchors;
- relevant assets.

Facts should support at least:

- KNOWN
- CONFLICTING
- UNKNOWN

The current prototype may also represent cautious inference, but inference must remain visibly distinct from source-supported identity truth.

The v0 seed was deliberately chosen outside the easiest S3/Empire concentration to prove the architecture is corpus-wide. It currently includes objects such as:

- R.O.D.;
- Lamplighters;
- Bastion;
- Redoubt;
- Aric Altovolo;
- Fennic Ingegno;
- The World's Cornerstone;
- The Mason;
- The Hunger;
- Four Primal Wellsprings.

That seed is architectural proof, not meaningful corpus coverage.

A useful next expansion target discussed in planning is roughly 25–50 objects spanning at least five projects/eras, with:

- remembered-name retrieval tests;
- alias collisions;
- typed relationships;
- canonical art for a handful of established characters/entities;
- identity-packet generation;
- candidate-object extraction that never silently promotes merges.

### Mental model

The target is bidirectional:

```text
high-level concept
-> literal human objects
-> relationships
-> specific documents / conversations / assets
-> raw source evidence
```

and upward:

```text
source
-> human object
-> relationship / pattern
-> higher-level concept
```

This is what allows high-level discussion while retaining a mental model of what literally exists.

### Acceptance condition

A core acceptance test is:

> Can Brendon name something from his own history in ordinary language and get the right thing back, with enough provenance and structure to immediately do useful work with it?

A miss means:

> NOT INDEXED YET

It must never silently mean:

> DOES NOT EXIST IN BRENDON'S WORK

---

## 7. Established-character identity resolution

The human-object layer is also the correct foundation for established-character rendering and other established-name tasks.

Before generating or reasoning about an established character, build a canonical identity packet.

Candidate fields:

- entity ID;
- canonical name;
- aliases;
- projects;
- roles;
- species/race;
- sex/gender where known;
- age where known;
- size/build/anatomy;
- class/profession;
- appearance;
- clothing/equipment;
- visual markers;
- behavioral identity;
- canonical art references;
- unknowns;
- conflicts;
- evidence assertions with source and confidence.

Keep **identity truth** separate from **style/art direction**.

Style references may influence:

- line;
- color;
- finish;
- composition;
- asset type.

Style references must never decide:

- race;
- sex;
- anatomy;
- costume facts;
- class;
- props;
- lore identity.

This identity resolution should eventually serve:

- "Draw Sandigil";
- "Who was Gil?";
- "Bring Daysong back";
- "What would this NPC know?";
- any established-name retrieval task.

---

## 8. Campaign simulation as accelerated longitudinal testing

A major planning insight from this thread is that campaign cognition does not need to wait entirely on months of real-world play.

A dedicated Project can operate as a **Kit campaign laboratory**.

The intended setup can mount the **same pinned Kit build across multiple chats / model instances** so many branches can be explored in parallel without confusing differences in Kit version with differences in campaign outcome. The same campaign-state packet and session design can be handed to multiple instances, each receiving a different controlled resolution.

### Basic loop

1. Kit designs a session.
2. Preserve the unresolved structures in that prep:
   - NPC agendas;
   - pressures;
   - clues;
   - threats;
   - player opportunities;
   - intended escalations;
   - deliberately open questions.
3. Supply a plausible session resolution.
4. Kit processes the result and designs the next session.
5. Repeat over several synthetic sessions.

Fork the same preparation into many resolutions.

Examples:

- players kill an intended ally;
- ignore the main hook;
- obsess over a throwaway NPC;
- solve a major problem early;
- fail catastrophically;
- retreat;
- misread a clue;
- ally with the antagonist;
- spend the session on an unexpected side goal;
- discover something expected to remain hidden;
- invent a solution no prep anticipated.

Evaluate whether Kit:

- respects what actually happened;
- recognizes what changed;
- preserves consequences;
- knows what unused prep is still valid;
- abandons invalid preparation;
- notices unexpected player investment;
- does not rig outcomes around that investment;
- advances NPCs and threats independently;
- preserves unresolved uncertainty;
- changes future preparation proportionally;
- remembers future obligations;
- produces a coherent next session.

### Paired and adversarial testing

Use:

- nearly identical histories with one consequential difference;
- very different fiction containing the same underlying DM problem;
- branches where the correct response is restraint;
- branches where previous preparation must be abandoned.

This tests whether Kit learned structural judgment or merely surface cues.

### Human/live validation

Synthetic testing is not the final authority.

Use a promotion ladder:

```text
synthetic branch test
-> unseen regression / holdout
-> sampled human live play
-> Brendon plays the strongest versions
-> harden what survives
```

Some sessions should be played by other humans. Brendon should play the strongest/most interesting surviving versions.

Preserve disagreements between Brendon and Kit. They are research material.

A useful comparison is:

> Why did Brendon care about X while Kit prioritized Y?

Possible explanations include:

- Kit failure;
- missing corpus knowledge;
- bad context assembly;
- memory/attention failure;
- planning failure;
- legitimate alternate judgment;
- eventually, a case where Kit found a better solution.

This simulation harness belongs conceptually in Stage 3.

---

## 9. Campaign cognition candidate model

The planning thread developed a more specific candidate model for campaign cognition than the architecture-layer list alone conveys. This remains a hypothesis to test, not a committed implementation.

### Keep different kinds of state separate

Do not collapse these into one conversational memory:

- authoritative state;
- event history;
- episodic memory;
- semantic/professional memory;
- procedural memory;
- campaign intent;
- active concerns;
- active attention;
- durable workflows/processes;
- entity cognition;
- derived views;
- temporary assembled context.

Persist durable facts, commitments, and processes. Recompute stale judgments when possible rather than preserving every old interpretation as if it were state.

### Attention

Campaign cognition needs both activation and inhibition.

It should track:

- what has become important;
- what is currently unresolved;
- what players repeatedly invest in;
- what should be allowed to recede;
- what deserves no intervention yet;
- what must be surfaced later even if it is not locally relevant now.

Player attention is especially important as a record of unanswered investment and agency, not as permission to predetermine outcomes.

### Time

Represent more than timestamps.

Campaign time may require:

- discrete events;
- intervals / continuing states;
- scheduled or conditional future processes;
- deadlines;
- promises waiting on conditions;
- clocks that survive chat/session boundaries.

Long-running processes should eventually live in durable state/workflows, not depend on an LLM remembering them conversationally.

### Deferred binding

A useful candidate status model for unresolved future facts is:

- `FIXED_AND_KNOWN`
- `FIXED_BUT_HIDDEN`
- `CONSTRAINED_BUT_UNRESOLVED`
- `OPEN`

This distinction matters because a DM must sometimes preserve a hidden fact, sometimes preserve only constraints, and sometimes genuinely leave the future undecided.

Do not accidentally "remember" an open possibility as if it had already become canon.

### Entity cognition

Only important active entities need rich cognition at a given moment.

Candidate entity state can include:

- beliefs;
- goals;
- resources;
- relationships;
- knowledge;
- pressures;
- next likely actions.

Entity cognition should activate selectively rather than flooding every turn with every NPC/faction in the campaign.

### Campaign intent

Campaign intent should preserve:

- purpose;
- opportunities;
- pressures;
- constraints;
- promises/setup/payoffs;
- production obligations;
- cross-scene dependencies.

It must not encode player outcomes that the players have not chosen.

### P0 campaign-cognition failures

The most dangerous failure classes are:

1. authoritative-state corruption;
2. hidden-knowledge leakage;
3. lost obligations / forgotten future processes;
4. player-agency violation.

A clever story move does not compensate for one of these failures.

---

## 10. Learning and promotion

Ordinary play should not silently rewrite professional doctrine.

Preferred direction:

```text
play
-> traces / observations
-> candidate learning
-> BFDM research / evaluation
-> validated release
```

Possible statuses:

- draft;
- candidate;
- validated;
- deprecated;
- superseded.

Preserve:

- scope;
- confidence;
- counterexamples;
- applicability;
- provenance.

Success in one playthrough is not sufficient to become global Kit behavior.

---

## 11. Source and epistemic rules that must survive compression

These distinctions are project-critical:

- source present ≠ live use established;
- preparation ≠ play;
- publication ≠ play;
- revision trajectory ≠ live trajectory;
- candidate ≠ admitted source;
- archive gap ≠ evidence gap;
- source research ready ≠ complete longitudinal history;
- later version ≠ automatically superseding;
- context source ≠ BFDM precedent;
- Discord projection zero ≠ historical nonexistence outside the searched projection;
- generated AI material ≠ Brendon authorship;
- Brendon request ≠ acceptance;
- acceptance ≠ implementation;
- open PR ≠ canonical main;
- human-object projection ≠ source truth;
- research concept ≠ canon fact.

Prefer explicit UNKNOWN over invented continuity.

Preserve contradictions.

Do not average early and late Brendon into one timeless persona.

---

## 12. Work allocation: use scarce tools where they actually matter

Do not equate "important" or "large" with "needs ChatGPT Work."

### Normal high-reasoning ChatGPT / Project chat

Use for work that can be done interactively with existing connectors and reasoning:

- architecture discussion;
- targeted corpus research;
- human-object design and review;
- Phase 2 analysis;
- interpreting agent results;
- campaign-simulation design;
- planning prompts;
- reviewing source evidence;
- incremental GitHub-connected edits where connector capabilities are sufficient.

### Shell-capable agent: Grok / Codex-style environment

Use for repository surgery:

- rebases;
- merges;
- renumbering;
- SQLite rebuilds;
- large deterministic file edits;
- running validators;
- test suites;
- Git conflict resolution;
- mechanical reconciliation.

### ChatGPT Work

Treat Work as a scarce, time-replenishing pool.

Reserve it for tasks that materially benefit from long autonomous execution across many files/apps/sources, for example:

- a broad autonomous research sweep across the full corpus;
- large cross-source synthesis with a finished research artifact;
- large evaluation campaigns;
- multi-step research where repeated manual steering would waste more scarce attention than the Work allocation.

Do not burn Work merely because a task is intellectually important.

"Accumulating tokens" is acceptable project shorthand for a limited Work allowance that replenishes over time.

---

## 13. Immediate active branches

### PR #33 — human-object index

Branch:

`research/human-object-index-v0`

Current status:

- rebased on canonical main after source consolidation;
- clean draft;
- initial seed remains architectural;
- expansion across BCS-000001–000172 has not yet been done.

Next substantive task:

> Expand the corpus-wide human-object representation across multiple eras/projects without privileging S3/Empire.

This can be done iteratively in normal high-reasoning chats. A broad autonomous extraction sweep may justify Work later.

### PR #28 — Phase 2 decision contrast families

Branch:

`research/phase2-decision-trajectories`

Current status:

- rebased on canonical main;
- clean draft;
- original conclusions preserved;
- Earthfall/Saturday follow-up not yet performed.

Next substantive task:

> Use newly canonical Earthfall and Saturday D&D workbench evidence to attack the existing contrast families.

Do not merely append corroborating examples.

### PR #27 — Discord retrieval maintenance

Still contains useful unique maintenance work:

- retrieval verification;
- attachment indexes;
- workflow changes;
- Discord-index improvements.

It is behind current main and should receive its own shell-based reconciliation later.

It is not the primary research priority now.

---

## 14. Near-term project priorities

The highest-value substantive work after Stage 1 consolidation is:

### Priority A — Make the corpus human-usable

Expand the human-object index so the project can reason from literal remembered entities rather than repository coordinates.

This is a bridge between archival substrate and future cognition.

### Priority B — Broaden judgment research

Run the Earthfall/Saturday cross-format Phase 2A pass.

The purpose is to determine which existing S3/S4-derived families:

- survive;
- narrow;
- break;
- gain new dimensions.

### Priority C — Complete Phase 2B creative-method work

Use materially different design traditions such as:

- Earthfall;
- Bastion/Redoubt;
- At War's End;
- early Roanoke;
- S5;
- experimental formats.

Avoid turning one campaign lineage into "Brendon's universal method."

### Priority D — Build the campaign laboratory

Once enough Stage 2 material exists, construct the synthetic longitudinal campaign harness described above.

This becomes a major way to test campaign cognition quickly before expensive real-world longitudinal validation.

---

## 15. What not to do next

Do not default back to:

- broad Empire City discovery;
- broad S3 discovery;
- another generic "Brendon principles" synthesis;
- building one giant vector database;
- premature precedent-card infrastructure;
- large cognitive graphs before tests demand them;
- treating summaries as authoritative state;
- auto-promoting successful behavior;
- ingesting every available source simply because it exists;
- using the densest campaigns as the default mental universe;
- solving repository maintenance with scarce Work capacity when a shell agent can do it.

---

## 16. Provisional architecture direction

A dedicated cognitive-architecture survey exists on branch `research/kit-cognitive-architecture-survey`, primarily in `research/kit-design/kit-cognitive-architecture-survey-v1.md`. It is research input and hypothesis space, not a final implementation specification.

The survey supports a factorized architecture rather than monolithic RAG.

Useful conceptual layers remain:

- AUTHORITATIVE SUBSTRATE
- ENTITY COGNITION
- CAMPAIGN COGNITION
- EPISODIC MEMORY
- SEMANTIC / PROFESSIONAL MEMORY
- PROCEDURAL MEMORY
- RECOGNITION / SALIENCE
- WORKING COGNITION / SITUATION ASSEMBLER
- STRATEGIC / TACTICAL SPLIT
- LEARNING GATE

These are architectural hypotheses, not implementation commitments.

Important principles from the survey:

- episodic memory should remain distinguishable from semantic knowledge;
- procedural knowledge needs versioning/deprecation/counterexamples;
- retrieval should depend on intent;
- attention requires activation and inhibition;
- campaign time requires events, intervals, and future processes;
- entity cognition should activate selectively;
- planning should preserve player openness;
- evaluation should localize failure types;
- provenance and trust must remain structured;
- concrete cases must survive alongside abstractions.

Avoid:

- one vector DB for everything;
- prose summaries as authoritative state;
- semantic-only precedent retrieval;
- local agents freely mutating global truth;
- one representation for all memory types;
- invisible auto-learning.

---

## 17. Provisional version / schedule estimate

This is a planning estimate, not a commitment.

As of 2026-10-05:

- overall Kit project: roughly `v0.35-alpha`;
- corpus/research substrate: roughly `v0.6-alpha`.

A serious friend-testable Kit beta may be plausible around late 2026 if current development pace continues.

A defensible general-purpose v1 is plausibly around January–March 2027.

The campaign-simulation harness may compress validation time substantially because many longitudinal campaign-cognition failures can be explored synthetically rather than waiting months of wall-clock play.

The larger north-star system — persistent campaign designer/operator with scalable campaign cognition — remains a later target and should be judged by demonstrated longitudinal operation rather than calendar optimism.

The largest uncertainty is quality iteration, not basic feasibility.

---

## 18. Success condition for the next era of the project

The next major transition is achieved when all of the following are true:

1. Brendon can name ordinary things from his creative history and the corpus resolves them correctly.
2. High-level concepts can be discussed while remaining grounded in literal people, places, systems, events, and sources.
3. Phase 2 findings survive materially different campaigns and formats.
4. Kit's candidate cognition can be tested through repeatable synthetic campaign branches.
5. Real human play is used to sample and challenge the strongest synthetic results.
6. Brendon's own play and corrections determine what gets hardened.
7. Architecture is added because observed failure demands it, not because a diagram looks complete.

The project should increasingly behave like an empirical DM-development program:

```text
preserved history
-> grounded research
-> candidate judgment
-> simulated stress testing
-> live sampling
-> Brendon validation
-> hardened Kit behavior
-> new observed failures
-> next architectural change
```

That loop is the current direction.
