# Kit Cognitive Core — Gap Map Against Current dnd-solo v0.1

**Date:** 2026-10-04  
**Status:** Working research artifact  
**Companion:** `cognitive-architecture-precedent-survey-v0.1.md`

## Purpose

This document compares the strongest mechanisms found in the external architecture survey against what `radarsaint/dnd-solo` already implements or designs.

The goal is to avoid two opposite mistakes:

1. rebuilding mechanisms Kit already has; or
2. forcing future cognitive responsibilities into `dnd-solo` merely because early prototypes happened to live there.

The question is not "what could a new brain service contain?"

The question is:

> **What cognitive responsibilities are already solved well enough to generalize, what remains local to game execution, and what genuinely new capability is still missing?**

---

# 1. Executive result

The current `dnd-solo` runtime is substantially more advanced than a typical LLM/RAG game prototype.

It already contains early forms of:

- authoritative state outside prose;
- append-only event history;
- bounded situation assembly;
- scoped knowledge / knowers;
- explicit NPC/agent wants and agendas;
- background pressures and clocks;
- salience;
- active campaign/level/scene pressures;
- private judgment preceding public performance;
- source provenance and retrieval boundaries;
- rollback / stale-writer / idempotency protections;
- reflection/test telemetry.

These should be **generalized, not discarded**.

The largest missing cognitive systems are not basic persistence or "memory" in the generic sense. They are:

1. **episodic memory across scenes/campaigns;**
2. **professional semantic/procedural knowledge;**
3. **case/precedent retrieval;**
4. **structural and intent-aware analogical matching;**
5. **counterexample retrieval / anti-anchoring controls;**
6. **offline memory consolidation;**
7. **cross-campaign learning with controlled promotion;**
8. **long-horizon campaign cognition above active agendas;**
9. **attention allocation across many simultaneous scenes/processes;**
10. **portable general DM competence separated from Brendon-private provenance;**
11. **large-production durable orchestration beyond one session/runtime;**
12. **trajectory-level evaluation of the cognitive system itself.**

This suggests that the future cognitive core should grow **around and above** the current runtime's strongest contracts.

It should not replace the authoritative event/state layer.

---

# 2. Current dnd-solo capabilities that already map to mature precedents

## 2.1 Authoritative state and event history

### Current system

`docs/architecture/state-context-prototype.md` and `runtime/state_context.py` already provide:

- SQLite persistent snapshots;
- append-only event ledger;
- atomic turn commit;
- stale revision rejection;
- idempotent turn retries;
- source/live-state separation;
- bounded context;
- player-safe projections.

KRABS explicitly requires:

> prose is not authoritative state.

### External analogue

- event sourcing;
- durable state machines;
- transactional workflow/state systems.

### Decision

**Keep in game/world runtime.**

This is not "memory" to move into a cognitive service.

The cognitive system should consume projections of authoritative state and propose actions. It should not become the source of truth for accepted world events.

---

## 2.2 Bounded working situation

### Current system

`runtime/state_context.py` already assembles a bounded current packet rather than replaying full history.

`docs/architecture/runtime-layers.md` separates:
- source;
- campaign state;
- campaign direction;
- scene;
- NPC/opposition;
- personality;
- adjudication;
- presentation.

### External analogue

- Soar working memory;
- Cognitive Scaffold fluid working context;
- bounded context/window management.

### Decision

**Generalize rather than replace.**

The future cognitive core may own or assist a broader situation assembler, but the existing principle is correct:

> current reasoning receives a deliberately assembled situation, not the whole archive.

---

## 2.3 Claims, knowers, and epistemic separation

### Current system

`docs/architecture/kit-claims-knowers.md` models:

- claim source;
- holder/knower;
- concealment;
- knowledge bands;
- truthful/false/hedged performance;
- persistent established definitions.

KRABS requires world truth, PC knowledge, player-visible information, NPC knowledge, faction intelligence, suspicion, misinformation, and director knowledge to remain separable.

### External analogue

- epistemic state / belief-state modeling;
- BDI beliefs;
- knowledge graphs with scoped perspectives.

### Decision

**This is a core primitive worth extracting/generalizing.**

A future cognitive system should not invent a second unrelated "memory fact" schema that discards:
- who believes the claim;
- who knows it;
- provenance;
- confidence;
- scope;
- whether it is current truth or belief.

The existing claims model is room-scale. The cognitive-core research should investigate how far the same conceptual primitive can scale.

---

## 2.4 Agendas, wants, pressures, and clocks

### Current system

`docs/architecture/kit-agendas.md` already represents:

- agents;
- wants;
- moves;
- triggers;
- knowledge prerequisites;
- pressures/clocks;
- offstage operation;
- pacing;
- quiet/hold as valid choices.

Agents can be:
- NPC;
- monster;
- faction;
- environment;
- clock.

### External analogue

- Dungeon World fronts;
- Blades clocks;
- BDI goal/intention state;
- actor systems;
- durable workflow/process engines.

### Decision

**Preserve the conceptual model; split cognition from scheduling.**

An actor/faction may have:
- belief;
- motive;
- intention;
- means.

A countdown/workflow may simply have:
- state;
- trigger;
- deadline;
- next transition.

Do not turn every pressure into an autonomous LLM agent.

At scale, durable scheduling may belong in infrastructure such as a workflow engine rather than the reasoning model.

---

## 2.5 Scene discernment and causal selection

### Current system

`docs/architecture/scene-discernment.md` requires Kit to read together:

1. player bid;
2. available story;
3. actor aim;
4. Kit's interest;
5. playable collision.

It explicitly permits `none`.

### External analogue

- appraisal models such as FAtiMA;
- reactive dramatic beats;
- local narrative affordances;
- intent-conditioned retrieval/selection.

### Decision

**This is a strong seed for cognitive recognition.**

It already demonstrates a general pattern:

> combine current action + valid active pressures + actor cognition + Kit appraisal, then choose whether there is a legitimate causal connection.

The future cognitive system should broaden this beyond NPC improv into a general **recognition / concern-selection** mechanism rather than create an unrelated reasoning framework.

---

# 3. What dnd-solo does not currently have

## 3.1 Episodic memory as precedent

The event ledger records what happened.

That does **not** yet produce an episodic memory capable of answering:

> "Have I encountered a structurally similar situation before?"

An event stream and an episodic memory are not the same representation.

Needed research:
- episode segmentation;
- event-to-episode consolidation;
- cue/intent indexing;
- structural retrieval;
- temporal relationships;
- representative vs exhaustive episode retention.

Candidate precedents:
- Soar EpMem;
- EMA;
- HeLa-Mem;
- Cognitive Scaffold.

---

## 3.2 Professional semantic knowledge

Kit currently has:
- authored rules;
- personality;
- campaign concerns;
- procedural code.

She does not yet possess a mature store of generalized professional concepts distilled from experience, such as:

- design failure types;
- campaign-production patterns;
- table-management heuristics;
- recognition cues;
- scope conditions;
- known counterexamples.

This is distinct from source material and distinct from one historical episode.

Needed research:
- semantic consolidation;
- provenance back to cases;
- versioning;
- confidence;
- contradiction handling;
- privacy-safe public export.

---

## 3.3 Procedural / method memory

Some DM procedures currently exist directly as runtime code or documents.

BFDM may reveal methods that should become reusable procedures rather than prose statements.

Examples of possible method classes:
- campaign launch-readiness review;
- faction activation;
- clue-legibility audit;
- encounter repair;
- emerging-NPC promotion assessment;
- session/campaign health review;
- player-investment diagnosis;
- prep-mutation review.

Needed research:
- method schema;
- applicability conditions;
- required inputs;
- steps;
- stop conditions;
- outputs;
- counterconditions;
- source-case links.

Candidate precedents:
- CTA decision requirements;
- NASA lessons application;
- Voyager skills;
- LifeMem workflow-level skill extraction.

---

## 3.4 Structural precedent retrieval

Current retrieval is source/state oriented.

The future cognitive system needs to retrieve cases by **decision structure**, not merely words.

A current problem may share:
- goal conflict;
- player intent;
- scale;
- pressure;
- actor knowledge;
- campaign layer;
- failure mode;

while sharing almost no vocabulary with the precedent.

Needed design:
1. broad candidate retrieval;
2. intent compatibility check;
3. structural fit;
4. important differences;
5. counterexample retrieval;
6. confidence.

Candidate precedents:
- Case-Based Reasoning;
- Soar cue + graph matching;
- STITCH contextual intent;
- analogical reasoning research.

---

## 3.5 Anti-anchoring / controlled memory reliance

2026 evidence shows highly similar retrieved memories can make agents imitate prior behavior.

Current Kit does not have an explicit mechanism for:

- saying precedent is irrelevant;
- retrieving conflicting precedent;
- comparing differences;
- limiting reliance on a retrieved case.

This becomes especially important because BFDM is intended to influence judgment rather than clone historical actions.

Needed invariant:

> **Historical precedent proposes attention and possibilities. It does not dictate current action.**

---

## 3.6 Offline consolidation

Current live state persists, but the system does not yet have a disciplined separation between:

### Online
- run the game;
- commit facts;
- emit traces;
- retrieve vetted knowledge.

### Offline
- segment episodes;
- summarize;
- link;
- compare outcomes;
- propose lessons;
- revise confidence;
- promote/deprecate methodology.

Candidate precedents:
- LightMem;
- HeLa-Mem;
- NASA continuous capture + reviewed application.

Likely rule:

> ordinary live play may record experience; it does not directly rewrite global professional doctrine.

---

## 3.7 Current campaign cognition above agendas

Agendas answer important questions about active actors and pressures.

The future system needs a broader model of the **campaign as an evolving creative object**, including things such as:

- active story structures;
- unresolved promises;
- player-created investments;
- fragile assumptions;
- abandoned/prepared material;
- potential payoffs;
- campaign rhythm;
- production debt;
- emerging opportunities;
- design risks;
- director priorities;
- material whose purpose is no longer being served.

Some of this exists conceptually in KRABS but not as a mature executable model.

This is one of the largest genuinely new cognitive requirements.

---

## 3.8 Attention allocation across many scenes

The current bounded-scene architecture is a strong base.

Roanoke-scale operation adds a different problem:

> Which of dozens of scenes, actors, processes, failures, and opportunities deserves Kit's attention now?

This is not ordinary retrieval.

It resembles:
- scheduler priority;
- salience/attention systems;
- blackboard control architectures;
- operations monitoring;
- multi-agent supervisory control.

Needed research:
- importance;
- urgency;
- reversibility;
- risk;
- campaign impact;
- director-attention threshold;
- expected value of intervention;
- starvation prevention.

This should be a dedicated architecture track.

---

## 3.9 Durable processes beyond turn/session scale

The agenda system contains clocks and offstage action.

At large scale, some processes need durable execution over:
- hours;
- days;
- weeks;
- restarts;
- periods when no model is active.

Examples:
- ritual completion;
- voting windows;
- player applications;
- travel;
- faction deadlines;
- event phases;
- scene ownership;
- production tasks.

This should likely use workflow/reminder infrastructure rather than context memory.

Candidate precedents:
- Temporal;
- Orleans reminders.

---

## 3.10 Portable competence vs Brendon-private knowledge

The current architecture does not yet define a complete publication boundary between:

### Private BFDM
- attributable historical evidence;
- player messages;
- private source documents;
- detailed cases;
- research uncertainty.

### Portable Kit professional knowledge
- abstract methods;
- sanitized precedents;
- general D&D/DM competence;
- campaign-production knowledge.

### Brendon-directed mode
- optional access to richer director-specific knowledge.

This is mandatory if Kit is to be handed to another person.

---

## 3.11 Cross-campaign identity/memory

Persona continuity is already correctly separated from durable cross-campaign memory.

The missing question is what Kit should remember across campaigns and users.

Possible categories:
- professional learning: global;
- Kit identity/taste: global;
- Brendon relationship history: Brendon-private;
- campaign facts: campaign-scoped;
- another user's preferences: user/campaign-scoped;
- historical BFDM provenance: research-private.

The cognitive core must encode scope and access control rather than relying on prompt discipline.

---

## 3.12 Cognitive-core evaluation

Current dnd-solo has strong local tests and human playtest evaluation.

The future core requires tests that isolate:

- episode segmentation;
- retrieval;
- intent matching;
- structural analogy;
- counterexample use;
- concern selection;
- campaign-level projection;
- memory consolidation;
- doctrine promotion;
- cross-scene prioritization;
- privacy scope.

Historical held-out cases should be a major source of evaluation.

---

# 4. Existing mechanisms that should probably become shared primitives

These deserve special attention because duplicating them in a future service would create architectural drift.

## Claim / belief primitive

Potential shared representation:
- proposition;
- source/provenance;
- truth status if authoritative;
- holder/knower;
- confidence/band;
- scope;
- timestamp/version.

## Event primitive

Potential shared representation:
- immutable event;
- causal evidence;
- actors;
- time;
- scope;
- resulting state references.

## Actor primitive

Potential shared representation:
- identity;
- beliefs/knowledge;
- wants;
- intentions;
- resources/means;
- relationships;
- location/scope;
- next likely actions.

## Concern / agenda primitive

Potential shared representation:
- purpose;
- owner/scope;
- activation conditions;
- pressure/urgency;
- possible moves;
- completion/deactivation criteria.

## Situation packet

Potential shared representation:
- authoritative facts;
- explicit player intent;
- relevant beliefs;
- active concerns;
- actor state;
- recent episode;
- retrieved professional knowledge;
- retrieved precedent;
- uncertainties.

These should not necessarily live in one database.

They should share contracts.

---

# 5. Likely system boundary after the audit

The evidence currently favors a boundary like:

```text
              KIT COGNITIVE CORE
  ------------------------------------------------
  professional semantic/procedural knowledge
  episodic precedent
  structural/intent-aware retrieval
  current campaign cognition
  concern/salience management
  long-horizon projection
  controlled consolidation
  ------------------------------------------------
                 |          ^
     situation   |          | judgment / queries
                 v          |
             DND-SOLO / GAME RUNTIME
  ------------------------------------------------
  authoritative world state
  event ledger
  rules/adjudication
  scene state
  geometry
  claims/knowledge truth
  actor/faction concrete state
  clocks/process adapters
  performance validation
  ------------------------------------------------
```

At large production scale, durable workflow and actor infrastructure may sit beside the game runtime:

```text
        cognitive core
         /         \
   game runtime   production orchestration
                  actors / workflows / timers
```

This is still provisional.

The important conclusion is that the cognitive core should **consume and generalize existing runtime primitives**, not become a second source of world truth.

---

# 6. Research priorities created by the gap map

## Priority 1 — campaign cognition representation

This is less solved than ordinary episodic memory and probably more important.

Research:
- creative project memory;
- project/portfolio cognition;
- blackboard systems;
- hierarchical goals/concerns;
- narrative state;
- design rationale;
- issue/risk/opportunity models;
- attention scheduling.

## Priority 2 — structural precedent retrieval

Prototype a case representation using existing BFDM decision cases.

Test whether:
- embeddings alone;
- structured feature matching;
- graph matching;
- LLM comparison;
- hybrid retrieval

can identify genuinely analogous cases without overfitting surface terms.

## Priority 3 — offline consolidation

Define how:
- raw events;
- episodes;
- cases;
- semantic findings;
- methods

relate and which transformations require human/research review.

## Priority 4 — scope/privacy model

Define which memories/knowledge are:
- global professional;
- Kit-global identity;
- director-private;
- user-private;
- campaign-specific;
- scene-specific;
- research-private.

## Priority 5 — Roanoke attention architecture

Treat global campaign operation as an attention/scheduling problem, not simply "more context."

## Priority 6 — architecture comparison

Compare:
A. orchestrator over specialized stores;
B. persistent cognition service;
C. hybrid actor/workflow fabric.

Use actual current `dnd-solo` interfaces in the comparison.

---

# 7. Strongest conclusion

The next system is **not needed because dnd-solo lacks a brain entirely.**

A meaningful part of Kit's cognition is already being built inside the solo runtime.

The new system becomes justified when we need to make these capabilities:

- persistent beyond one executable game runtime;
- reusable across campaigns and users;
- capable of professional memory and precedent;
- capable of long-horizon campaign cognition;
- capable of supervising multiple concurrent scenes;
- capable of controlled learning from accumulated experience.

That is a narrower, more defensible reason to create a new cognitive-core repository/runtime than simply saying "Kit needs a brain."
