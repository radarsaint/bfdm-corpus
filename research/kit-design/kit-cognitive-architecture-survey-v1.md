# Kit Cognitive Architecture Survey v1

**Status:** research draft, not canonical architecture  
**Date:** 2026-10-04  
**Purpose:** identify mature research and systems worth stealing for Kit's long-term cognitive architecture, especially where BFDM-derived expertise, live campaign cognition, precedent, memory, world state, large-scale orchestration, and evaluation meet.

## 1. Problem statement

Kit is not being designed as a single-task assistant.

The long-term target is one persistent Dungeon Master identity capable of:
- running a one-player D&D game;
- running ordinary multiplayer D&D for other people;
- designing campaigns;
- collaborating on large campaign preproduction;
- operating persistent campaigns across many simultaneous scenes;
- maintaining continuity, NPC/faction cognition, clocks, shared-world consequences, and campaign-level concerns;
- using Brendon's documented historical experience as professional precedent and production methodology;
- improving from new experience without allowing one unusual incident to rewrite global behavior.

BFDM is the private research archive used to recover historical evidence, cases, failures, corrections, and creative methodology. Ordinary Kit operation should not require unrestricted access to the private BFDM archive.

The architectural question is therefore not "which vector database should Kit use?" It is:

> What cognitive and operational subsystems allow Kit to combine current authoritative game state, campaign history, professional knowledge, historical precedent, active concerns, and long-horizon judgment without collapsing them into one lossy memory store?

## 2. Main finding

The strongest precedent is a **factorized cognitive architecture**, not a monolithic RAG system.

Several independent research traditions converge on this:

- Soar separates working, semantic, episodic, and procedural knowledge and makes decisions by combining current state with relevant retrieved knowledge at runtime.
- Current 2026 agent-memory research increasingly separates episodic, semantic, temporal, salience/control, and procedural memory rather than treating all history as one embedding index.
- Case-Based Reasoning preserves concrete prior cases and adapts them to new situations instead of replacing experience with rules.
- Cognitive Task Analysis and the Critical Decision Method recover tacit expertise as cues, situation assessments, decision requirements, expectations, and alternatives.
- NASA's lessons-learned lifecycle distinguishes collection, recording, dissemination, and actual application to procedures and policy.
- Orleans and Temporal solve durable identity/state/process problems that should not be delegated to an LLM's conversational memory.
- Recent multi-agent research suggests memory and global context are disproportionately important at the planner/orchestrator layer, while bounded executors can stay comparatively local.

The emerging design principle is:

> **Kit should feel like one mind while being implemented as coordinated, typed cognitive and state systems.**

## 3. Workstream A — tacit expert knowledge

### Cognitive Task Analysis / Critical Decision Method

**Problem solved:** experts often cannot state the knowledge they actually use as clean rules.

The Critical Decision Method uses repeated passes over a real incident and probe questions to recover:
- important cues;
- situation assessment;
- goals;
- expectations;
- information sought;
- alternatives considered or rejected;
- points where another choice could have been made;
- what a novice would likely miss.

The 1998 Hoffman, Crandall, and Shadbolt paper explicitly describes outputs including Situation Assessment Records, timelines, and decision requirements.

Primary source:
- Hoffman, Crandall, Shadbolt, "Use of the Critical Decision Method to Elicit Expert Knowledge," Human Factors 40(2), 1998.
- https://journals.sagepub.com/doi/10.1518/001872098779480442

### What to steal

BFDM case reconstruction should use CTA-style probes, but archive-first:

1. reconstruct the event from contemporaneous material before interviewing Brendon;
2. identify decision points and information actually available at the time;
3. use present-day Brendon only to resolve missing rationale, competing interpretations, or tacit recognition;
4. keep retrospective explanation labeled as retrospective evidence rather than silently rewriting the historical record.

### What not to steal

Do not treat retrospective expert explanation as infallible. BFDM often has better contemporaneous evidence than classical CTA studies have.

## 4. Workstream B — organizational experience into reusable practice

### NASA Lessons Learned

NASA uses a lifecycle of:
- **Collect**
- **Record**
- **Disseminate**
- **Apply**

NASA's public Lessons Learned Information System contains reviewed lessons derived from program/project events, and lessons feed into training, best practices, policies, procedures, handbooks, and checklists.

Primary sources:
- https://www.nasa.gov/learning-resources/for-professionals/appel-lessons-learned/
- https://llis.nasa.gov/

### What to steal

BFDM should preserve a hard distinction between:
- raw historical source;
- reconstructed case;
- reviewed lesson/method;
- operational application.

A lesson is not complete merely because it exists in a research report. There must be a traceable path showing where it becomes:
- a Kit recognition pattern;
- a production procedure;
- a campaign review;
- a runtime retrieval rule;
- an evaluation scenario;
- or another actual capability.

### What not to steal

Do not flatten BFDM into a conventional lessons database. NASA lessons are often intentionally compact and prescriptive; BFDM needs richer contradictory cases because DM judgment is highly conditional.

## 5. Workstream C — cognitive architecture

### Soar

Soar is unusually relevant because it has spent decades separating kinds of cognition that current LLM systems often conflate.

Current Soar documentation distinguishes:
- working memory;
- semantic memory;
- episodic memory;
- procedural/production memory;
- decision procedures and learning.

Its episodic memory records the stream of agent experience and permits deliberate retrieval of prior episodes. Semantic memory stores context-independent declarative knowledge. Soar's design explicitly combines current state with relevant retrieved knowledge at decision time.

Primary sources:
- https://soar.eecs.umich.edu/soar_manual/01_Introduction/
- https://soar.eecs.umich.edu/soar_manual/06_SemanticMemory/
- https://soar.eecs.umich.edu/soar_manual/07_EpisodicMemory/

### What to steal

Do not literally implement Soar.

Steal the ontology:
- **working cognition** = what Kit needs for the current decision;
- **episodic memory** = what happened in specific prior situations;
- **semantic/professional knowledge** = general facts and concepts independent of one incident;
- **procedural knowledge** = learned "how to" methods;
- **authoritative external state** = world truth that should not depend on any memory type.

This is a useful boundary for BFDM distillation and Kit runtime design.

### What not to steal

Soar's production-rule architecture is not automatically appropriate for an LLM-centric creative DM. The useful precedent is separation of memory functions and runtime combination, not the implementation substrate.

## 6. Workstream D — modern episodic and semantic memory

### EMA

EMA organizes conversation into Episodic Memory Units and uses a MemDecider to filter memory so the model does not consume everything.

Source:
- Lan et al., "EMA: An Episodic Memory Agent for Efficient and Selective Memory," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.250/

**Steal:** explicit episode units plus a relevance/filtering stage before prompt assembly.

### HeLa-Mem

HeLa-Mem uses:
1. an episodic memory graph;
2. semantic memory distilled from densely connected episodic hubs;
3. associative retrieval and consolidation.

Source:
- Zhu et al., "HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents," ACL 2026.
- https://aclanthology.org/2026.acl-long.625/

**Steal:** preserve concrete episodes separately from consolidated reusable knowledge. Consolidation should be a distinct operation with lineage.

### Synapse

Synapse models memory as a dynamic graph and uses spreading activation, embeddings, temporal decay, and inhibition rather than relying only on nearest-neighbor similarity.

Source:
- Jiang et al., "Synapse: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.1108/

**Steal:** relevance can emerge from connected cues, not merely textual similarity. A current situation may activate player, faction, promise, prior failure, and campaign concern simultaneously.

### Temporal Semantic Memory

TSM distinguishes dialogue time from actual event time and models both point events and durative states.

Source:
- Su et al., "Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.1496/

**Steal:** Kit must represent:
- when a message was received;
- when the described event actually happened;
- intervals/states that persist through time.

This is especially important for persistent campaigns where delayed reporting and asynchronous scenes are normal.

### BMAM

BMAM explicitly separates episodic, semantic, salience-aware, and control-oriented memory components operating over different time scales.

Source:
- Li et al., "BMAM: Brain-inspired Multi-Agent Memory Framework," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.1973/

**Steal:** salience/control deserves its own treatment. "What deserves attention now?" is not identical to memory retrieval.

### LightMem

LightMem separates short-, mid-, and long-term memory and performs offline consolidation into reusable long-term knowledge.

Source:
- Zhang et al., "Lightweight LLM Agent Memory with Small Language Models," ACL 2026.
- https://aclanthology.org/2026.acl-long.588/

**Steal:** expensive consolidation need not happen synchronously during play. Online DM operation should remain fast; background/research consolidation can be separated.

### Amory

Amory constructs episodic narratives during offline reasoning and converts peripheral facts into semantic memory.

Source:
- Zhou et al., "Amory: Building Coherent Narrative-Driven Agent Memory through Agentic Reasoning," EACL 2026.
- https://aclanthology.org/2026.eacl-long.183/

**Steal carefully:** an episode sometimes needs coherent narrative structure rather than disconnected snippets.

**Do not steal:** freeform memory rewriting without provenance controls. BFDM and authoritative game history need recoverable source lineage.

## 7. Workstream E — intent-aware retrieval

### STITCH

STITCH addresses a major failure mode: semantically similar memories can be wrong because they arose under different goals and constraints.

It indexes trajectory steps using:
- current latent goal;
- action type;
- salient entity types.

Retrieval then prioritizes intent-compatible history.

Source:
- Yang et al., "Grounding Agent Memory in Contextual Intent," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.584/

### What to steal

BFDM cases and live campaign episodes should be indexed by more than topic.

Possible Kit retrieval keys:
- play mode: combat/social/exploration/investigation/production/ops;
- current goal;
- director intent;
- scale: scene/session/arc/campaign/server;
- intervention type;
- salient actor types;
- campaign lifecycle phase;
- uncertainty type;
- failure mode;
- resource/time pressure;
- player comprehension state.

This allows "structurally similar" precedent retrieval even when the fantasy nouns are unrelated.

## 8. Workstream F — procedural memory

### Memp

Memp distills agent trajectories into:
- fine-grained step-by-step instructions;
- higher-level script-like abstractions.

It supports update, correction, and deprecation as experience accumulates.

Source:
- Fang et al., "Memp: Exploring Agent Procedural Memory," Findings ACL 2026.
- ACL author records and proceedings.

### ReMe

ReMe explicitly rejects passive append-only procedural memory. It uses:
1. multi-faceted distillation of success patterns, failure triggers, and comparative insights;
2. context-adaptive reuse;
3. utility-based refinement, including pruning outdated knowledge.

Source:
- Cao et al., "Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.829/

### MAGNET

MAGNET separates stable functional semantics from changing workflows and maintains procedural memory of task intent across distribution shifts.

Source:
- Sun et al., "MAGNET: Towards Adaptive GUI Agents with Memory-Driven Knowledge Evolution," ACL 2026.
- https://aclanthology.org/2026.acl-long.1299/

### What to steal

BFDM-derived methods should be versioned lifecycle objects, not permanent commandments.

A method needs:
- scope conditions;
- evidence lineage;
- supporting cases;
- counterexamples;
- confidence;
- last review;
- supersedes/superseded-by;
- failure triggers;
- adaptation guidance;
- utility evidence.

Procedural knowledge should be able to be corrected or deprecated without deleting the historical cases that produced it.

### What not to steal

Do not allow live Kit to autonomously promote every successful local behavior into global professional doctrine. BFDM's research/review gate should remain between experience and durable methodology.

## 9. Workstream G — case-based reasoning and precedent

Case-Based Reasoning solves new problems by retrieving similar past cases, adapting prior solutions, revising based on outcome, and retaining experience.

A 2025 review specifically examines CBR integrated with LLM agents as an alternative/complement to generic RAG.

Source:
- Hatalis, Christou, Kondapalli, "Review of Case-Based Reasoning for LLM Agents," 2025.
- https://arxiv.org/abs/2504.06943

### What to steal

Kit should retain representative cases even after general methods are distilled.

A useful precedent object should preserve:
- situation structure;
- salient cues;
- goals/intent;
- constraints;
- uncertainty;
- options;
- action;
- result;
- later revision;
- transfer conditions.

Retrieval should combine:
- semantic similarity;
- structured similarity;
- goal/intent compatibility;
- actor relationships;
- temporal/campaign context;
- known differences from the current situation.

Then Kit adapts rather than copies.

### What not to steal

Do not define "similarity" as embedding distance over prose. That would retrieve superficially similar fantasy content rather than similar decision structures.

## 10. Workstream H — hierarchical retrieval and corpus sensemaking

### GraphRAG

GraphRAG was designed partly because conventional RAG performs poorly on global questions about an entire corpus. It constructs an entity graph and community summaries for broader sensemaking.

Source:
- Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization," 2024.
- https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/

### RAPTOR

RAPTOR recursively clusters and summarizes text into a hierarchy and retrieves at different abstraction levels.

Source:
- Sarthi et al., "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval," ICLR 2024.
- https://proceedings.iclr.cc/paper_files/paper/2024/hash/8a2acd174940dbca361a6398a4f9df91-Abstract-Conference.html

### Cognitive Scaffold

Cognitive Scaffold separates:
- Fluid Working Context for immediate reasoning;
- persistent structured Knowledge Graph for long-term retention;
and crystallizes saturated context into atomic event snapshots.

Source:
- Ai et al., "Cognitive Scaffold: From Fluid Context to Crystallized Memory for Long-Horizon DeepResearch Agents," ACL 2026.
- https://aclanthology.org/2026.acl-long.1170/

### What to steal

Kit needs multi-level retrieval:
- atomic fact/event;
- episode;
- case;
- relationship cluster;
- campaign-level pattern;
- professional method.

The query layer should choose retrieval granularity based on the cognitive question.

### What not to steal

GraphRAG itself is not a complete memory architecture, and Microsoft now explicitly describes the project as research/maintenance mode. Treat it as a pattern for graph-based global sensemaking, not the foundation of Kit.

## 11. Workstream I — memory management as action

### AgeMem

AgeMem treats memory operations themselves as agent actions: store, retrieve, update, summarize, discard.

Source:
- Yu et al., "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents," ACL 2026.
- https://aclanthology.org/2026.acl-long.981/

### AMA

AMA separates constructor, retriever, judge, and refresher roles. A judge verifies relevance/consistency and triggers further retrieval or targeted memory refresh when evidence conflicts.

Source:
- Huang et al., "AMA: Adaptive Memory via Multi-Agent Collaboration," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.152/

### What to steal

Kit's cognition should be capable of explicit metacognitive operations such as:
- retrieve more context;
- test whether retrieved precedent is actually compatible;
- recognize insufficient evidence;
- request a different granularity;
- identify a memory conflict;
- mark a candidate update for later research.

### What not to steal

Do not give a single generative process unrestricted authority to rewrite authoritative world state or professional doctrine.

## 12. Workstream J — persistent world/state infrastructure

### Orleans / virtual actors

Orleans provides:
- stable logical identity for grains;
- persistent state;
- single-activation semantics;
- timers and durable reminders;
- event-sourcing support.

Official documentation:
- https://learn.microsoft.com/en-us/dotnet/orleans/
- https://learn.microsoft.com/en-us/dotnet/orleans/grains/grain-identity
- https://learn.microsoft.com/en-us/dotnet/orleans/grains/grain-persistence
- https://learn.microsoft.com/en-us/dotnet/orleans/grains/event-sourcing/

### What to steal

The actor model is a strong candidate for persistent active entities:
- NPCs;
- factions;
- parties;
- locations with active processes;
- campaign subsystems.

Each entity can retain identity/state and react to messages/events without requiring its entire history in an LLM context.

Do not decide yet that Orleans itself is the implementation. Steal the architectural model first.

### Temporal / durable workflows

Temporal persists workflow history and can resume long-running processes after failures. Workflow tasks are triggered by events such as signals, timers, activity completion, and child workflows.

Official documentation:
- https://docs.temporal.io/
- https://docs.temporal.io/temporal
- https://docs.temporal.io/tasks

### What to steal

A campaign contains long-running processes that are better represented as durable workflows than "things the model remembers":
- countdowns;
- rituals;
- investigations;
- travel;
- elections;
- scheduled reveals;
- multi-stage events;
- promises waiting on conditions;
- director approval/escalation flows.

The LLM should reason about these processes; it should not be responsible for keeping them alive.

## 13. Workstream K — global planning and local execution

### COMPASS

COMPASS separates:
- a Main Agent for tactical work;
- a Meta-Thinker for strategic oversight;
- a Context Manager maintaining concise progress briefs.

Source:
- Wan et al., "COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving Context," ACL 2026.
- https://aclanthology.org/2026.acl-long.152/

### PEAR

PEAR evaluates planner-executor systems and reports that planner weakness is especially damaging; planner memory is important while executor memory yields smaller gains in the tested setting.

Source:
- Dong et al., "PEAR: Planner-Executor Agent Robustness Benchmark," Findings EACL 2026.
- https://aclanthology.org/2026.findings-eacl.237/

### LEGOMem

LEGOMem studies where procedural memory should live in multi-agent workflow systems and finds orchestrator memory particularly important for decomposition/delegation, with fine-grained agent memory aiding execution.

Source:
- Han et al., "LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation," 2025.
- https://arxiv.org/abs/2510.04851

### What to steal

For Roanoke-scale operation, distinguish:
- **campaign cognition / strategic oversight**;
- **scene cognition / tactical execution**.

The campaign-level layer should track:
- global pressures;
- shared consequences;
- conflicts between scenes;
- player/faction trajectories;
- director concerns;
- resource/attention allocation;
- upcoming production obligations.

Local scene execution should receive a bounded situation package and return committed events plus attention-worthy observations.

This supports "one Kit" without requiring one prompt to contain the entire server.

## 14. Workstream L — hierarchical planning

### ReAcTree / GoalAct / HTN work

Recent systems improve long-horizon planning by decomposing larger goals into subgoals rather than maintaining a monolithic trajectory.

Sources:
- ReAcTree, 2025: https://arxiv.org/abs/2511.02424
- GoalAct, 2025: https://arxiv.org/abs/2504.16563
- Meneguzzi et al., "Hierarchical Task Network Planning with LLM-Generated Heuristics," 2026: https://arxiv.org/abs/2605.07707

### What to steal

Campaign production is naturally hierarchical:
campaign purpose
→ production phase
→ system/faction/location workstream
→ artifact
→ task.

A method library can supply decomposition patterns without forcing the LLM to rediscover every production workflow.

Likewise server operation can decompose:
campaign concern
→ affected scenes/entities
→ required checks/actions
→ local execution.

### What not to steal

D&D is not a deterministic project plan. Planning must preserve open-ended player action and support revision when the world changes.

## 15. Workstream M — evaluation

### RAGChecker

RAGChecker's key lesson is architectural: modular systems need modular evaluation. It separately diagnoses retrieval and generation rather than scoring only final answers.

Source:
- Ru et al., "RAGChecker," NeurIPS 2024.
- https://proceedings.neurips.cc/paper_files/paper/2024/hash/27245589131d17368cccdfa990cbf16e-Abstract-Datasets_and_Benchmarks_Track.html

### Plan-RewardBench

Trajectory-level judging becomes substantially harder as trajectories lengthen; evaluator performance degrades on long-horizon tasks.

Source:
- Wang et al., "Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling," ACL 2026.
- https://aclanthology.org/2026.acl-long.1062/

### AgencyBench

AgencyBench targets real-world long-horizon agent tasks requiring many tool calls and very large context.

Source:
- Li et al., "AgencyBench," ACL 2026.
- https://aclanthology.org/2026.acl-long.337/

### What to steal

Kit evaluation must localize failure.

At minimum:
- authoritative-state failure;
- retrieval failure;
- salience/recognition failure;
- precedent mismatch;
- planning/judgment failure;
- rules/adjudication failure;
- local execution failure;
- expression/performance failure;
- campaign-level coordination failure;
- long-horizon consequence failure.

Historical BFDM cases should be turned into partially held-out trajectory tests, not only style examples.

Hard negatives are particularly important:
- plausible but wrong precedent;
- correct local move that damages campaign intent;
- good dramatic move built on false world state;
- correct historical analogy under materially different current constraints.

## 16. Proposed information architecture for BFDM distillation

This survey suggests a richer chain than:

source → quote → method.

Recommended research representation:

### Layer A — source/evidence
High-fidelity archive and attributable evidence.

### Layer B — atomic historical events
What happened, when, who/what was involved, source lineage.

### Layer C — episodes
Coherent bounded sequences with:
- start/end;
- participants;
- goals;
- actions;
- outcomes;
- relevant context.

### Layer D — decision / production cases
Structured expert cases:
- situation;
- intent;
- salient cues;
- recognition;
- missing information;
- alternatives;
- intervention/design choice;
- expected effect;
- outcome;
- hindsight;
- counterfactual;
- transfer conditions.

### Layer E — semantic concepts and relations
Reusable concepts:
- player investment;
- campaign pressure;
- prep mutation;
- story-bearing capacity;
- telegraphing failure;
- operational bottleneck;
etc.

### Layer F — procedural methods
Versioned "how-to" knowledge, with scope and evidence lineage.

### Layer G — abstract precedents
Sanitized cases that can travel outside the private archive.

### Layer H — evaluations
Held-out or partially held-out historical situations and hard negatives.

This allows a future private BFDM corpus to publish a safe cognitive package without exposing raw historical data.

## 17. Provisional Kit cognitive architecture

This is a research hypothesis, not a final implementation.

### 17.1 Authoritative substrate

Outside the LLM:
- world event ledger;
- current materialized state;
- time and chronology;
- geometry;
- entity identity;
- knowledge/permission boundaries;
- durable workflows.

### 17.2 Entity cognition

Persistent models for important:
- NPCs;
- factions;
- parties;
- locations/processes.

Represent beliefs, goals, resources, relationships, next actions, and entity-specific knowledge.

### 17.3 Campaign cognition

A higher-order model that tracks:
- campaign intent;
- active story structures;
- pressures;
- unresolved consequences;
- promises/setup/payoffs;
- emerging opportunities;
- risks/design debt;
- production obligations;
- cross-scene dependencies;
- director-attention candidates.

### 17.4 Episodic memory

Specific experiences from the current campaign and reusable historical/abstract precedents.

Episodes remain linked to time and context.

### 17.5 Semantic/professional memory

Context-independent domain knowledge:
- D&D concepts;
- campaign-design concepts;
- general DM principles;
- BFDM-derived concepts.

### 17.6 Procedural memory

Versioned production and DM methods.

Examples:
- investigate a stalled social scene;
- telegraph severe danger;
- evaluate promotion of incidental material;
- mutate prep while preserving purpose;
- conduct campaign launch readiness review.

### 17.7 Recognition / salience layer

Determines:
- what matters now;
- what type of situation this is;
- what additional memory/state must be retrieved;
- what deserves no intervention;
- whether concern belongs at scene, arc, campaign, or server level.

This should not be reduced to vector similarity.

### 17.8 Working cognition / situation assembler

Builds the bounded context Kit actually reasons over:
- current authoritative facts;
- relevant beliefs;
- explicit player intent;
- current campaign concerns;
- retrieved precedents;
- applicable methods;
- uncertainties;
- likely future processes.

### 17.9 Strategic / tactical separation

One Kit identity, but different cognitive scopes:
- strategic campaign oversight;
- bounded local scene execution.

Local scenes commit events and surface candidate concerns upward.

### 17.10 Learning gate

Ordinary play may:
- write episodes;
- record traces;
- produce candidate lessons;
- flag anomalies.

Ordinary play may **not** silently rewrite global professional doctrine.

Durable method changes flow through:
experience → research/evaluation → validated update → new methodology release.

## 18. Things we should explicitly avoid

1. **One vector database as "Kit's brain."**
2. **Summaries as authoritative state.**
3. **Automatically promoting every successful trajectory into a rule.**
4. **Letting local scene agents independently mutate global campaign knowledge.**
5. **Retrieving precedent only by semantic similarity.**
6. **Flattening player knowledge, NPC belief, world truth, and director knowledge.**
7. **Treating long-running clocks/processes as conversational memory.**
8. **Evaluating only final prose quality.**
9. **Building a BFDM export that loses private provenance internally.**
10. **Assuming one representation should serve archive, research, runtime memory, and evaluation equally well.**

## 19. Highest-value mechanisms to prototype

The survey currently suggests these prototypes before choosing a final platform:

### Prototype A — typed memory/situation assembly

Given a live situation, retrieve separately:
- authoritative facts;
- current campaign concern;
- relevant current-campaign episode;
- BFDM-derived abstract precedent;
- applicable procedural method.

Measure whether separated retrieval improves judgment over a flat RAG baseline.

### Prototype B — structure-aware precedent retrieval

Create a small case set indexed by:
- goal;
- cues;
- intervention type;
- scale;
- constraints;
- outcome;
- campaign lifecycle stage.

Compare:
- embedding-only retrieval;
- structured filtering + embedding;
- graph/associative retrieval.

### Prototype C — campaign cognition loop

Maintain a campaign-level concern model independent of scene transcripts.

Local scenes emit:
- committed events;
- changed relationships;
- new pressures;
- unresolved consequences;
- possible director-worthy flags.

Campaign cognition decides what matters globally and what to surface back into future scene contexts.

### Prototype D — research-to-procedural-memory pipeline

Take a small validated BFDM cluster and produce:
- source-linked cases;
- one or more procedural methods;
- counterexamples;
- a sanitized runtime export;
- held-out evaluations.

This tests the complete BFDM → cognition path before mass extraction.

## 20. Open questions

1. Should the cognitive core be a standalone service or a set of libraries/interfaces around authoritative stores?
2. Should entity cognition use actor-style runtime objects, relational state, event projections, or a hybrid?
3. How much of precedent retrieval should occur automatically versus through explicit metacognitive actions?
4. How should salience be represented and updated?
5. How should the system model uncertainty and competing interpretations?
6. What is the correct granularity of an episode for live play versus BFDM research?
7. How do we prevent distorted consolidation from slowly rewriting campaign history?
8. Which professional methods are portable to other users and which are Brendon/director-specific?
9. How do strategic and tactical Kit instances share one identity without sharing uncontrolled context?
10. How do we evaluate campaign quality over weeks when there is no single scalar objective?

## 21. Current bottom line

The architecture we should investigate is not "LLM + RAG + bigger context."

The strongest evidence points toward:

> **authoritative event/state infrastructure + typed multi-timescale memory + campaign cognition + intent-aware precedent retrieval + versioned procedural knowledge + hierarchical strategic/tactical reasoning + gated learning + trajectory-level evaluation**

Kit can still appear to the player as one Dungeon Master.

The complexity belongs behind the screen.


## 22. Provenance, permissions, and the private-to-portable boundary

The private BFDM corpus creates an additional requirement that ordinary agent-memory benchmarks often ignore: some knowledge may be useful to Kit while the underlying evidence remains private, person-specific, or inappropriate to expose in another user's game.

Recent work strengthens the case for making provenance operational rather than decorative.

### SEEM

Structured Episodic Event Memory (SEEM) converts interaction streams into structured Episodic Event Frames anchored by precise provenance pointers, then reconstructs broader narrative context through graph/episode interaction and reverse provenance expansion.

Source:
- Lu et al., "Structured Episodic Event Memory," ACL 2026.
- https://aclanthology.org/2026.acl-long.277/

**Steal:** episodes and distilled knowledge should maintain machine-readable pointers back to the evidence/cases they were derived from.

### MemORAI

MemORAI uses a provenance-enriched multi-relational graph with factual origins tracked at turn level and query-adaptive subgraph retrieval.

Source:
- Pham Van et al., "MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.1408/

**Steal:** provenance should coexist with relationships and query-time retrieval rather than being stored in a disconnected citation table.

### Hindsight

Hindsight separates world, experience, observation, and opinion networks, making objective fact versus subjective belief explicit.

Source:
- Latimer et al., "Hindsight: Structured Agent Memory that Retains, Recalls, and Reflects," ACL 2026 Demo.
- https://aclanthology.org/2026.acl-demo.27/

**Steal:** Kit should not flatten world fact, player/NPC belief, Kit hypothesis, director preference, and research conclusion. These should be separately typed and carry confidence/source lineage.

### MAP-Graph / permission-aware provenance

MAP-Graph is recent preprint work exploring provenance-aware shared memory where ancestry, permissions, trust, and action risk participate directly in retrieval/action gating.

Source:
- Wang et al., "MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows," 2026.
- https://arxiv.org/abs/2608.10509

This is not mature enough to adopt wholesale, but the design question is directly relevant.

### Security implication

Research on tool-using agents has demonstrated that agents with memory-access tools can become data-exfiltration surfaces.

Source:
- Zhang and Pei, "Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use," Findings ACL 2026.
- https://aclanthology.org/2026.findings-acl.1257/

Therefore the BFDM-to-Kit boundary should not rely only on prompting Kit "not to reveal private history."

A portable runtime should receive sanitized methods, abstract precedents, approved concepts, and privacy-safe provenance handles. Direct raw BFDM access, when used for research/director work, should be a separately permissioned capability.

### Proposed provenance fields for exported cognition

Every distilled object should be capable of carrying:
- `knowledge_id`
- `knowledge_type`
- `visibility_scope`
- `derived_from_private`
- `evidence_handles` (resolvable only in privileged research context)
- `confidence`
- `review_status`
- `created_by_process`
- `last_reviewed`
- `supersedes`
- `allowed_use_modes`
- `redaction/sanitization_version`

This permits Kit to use a professional lesson without exposing the historical private incident that produced it.

## 23. Revised principle: provenance is part of cognition

For Kit, provenance serves at least four functions:
1. **truth support** — why should this fact or method be trusted?
2. **scope** — is this historical Brendon-specific evidence, portable professional knowledge, or current campaign truth?
3. **permissions** — may this information be used or surfaced in the present context?
4. **revision** — when a method is challenged, which underlying cases must be re-examined?

This means provenance belongs in the cognitive data model, not only in BFDM's archive layer.

## 24. Additional research implication

The BFDM research program should test whether a distilled method remains useful **after historical names, campaign lore, and private source text are removed**.

If utility collapses after sanitization, we have probably encoded anecdote rather than transferable expertise.

A useful export test is:

> Can Kit apply the derived method to a structurally similar synthetic or unrelated D&D situation without access to the original campaign nouns?

That should become part of methodology validation before a BFDM finding graduates into portable Kit cognition.


## 25. Human and agent research access is a first-class subsystem

The architecture survey originally underweighted a basic requirement: the corpus must remain directly searchable and inspectable by humans and research agents, independently of Kit's runtime retrieval stack.

This is required for discovery, source checking, provenance review, ad hoc exploration, debugging, and reproducible research. A researcher must be able to find facts, ideas, characters, mechanics, phrases, places, and historical connections without first running Kit or a custom retrieval service.

The existing ingestion contract already requires human-readable `source.md` representations and a searchable SQLite representation. The LFS-pointer incident demonstrates that those guarantees are insufficient if ordinary repository/code-search interfaces expose only an LFS pointer.

### Access-plane invariant

> **No textual historical content may be effectively hidden behind a binary container, LFS pointer, opaque database, embedding index, or proprietary retrieval layer as its only practical discovery path.**

Raw/binary preservation and machine indexes remain valuable, but text-extractable material must also have a directly searchable human-readable representation.

### Required representations

For textual or text-extractable sources, maintain:
1. canonical/raw bytes or provider snapshot, which may live in LFS;
2. UTF-8 Markdown/text suitable for ordinary repository/code search;
3. structured provenance and metadata tied to the BCS identity;
4. rebuildable machine indexes such as SQLite FTS or later search services;
5. searchable metadata/description for binaries and assets linked to their source container.

Search must work across current bodies, available revisions, comments/replies, Discord messages, research artifacts, and metadata where technically appropriate.

Results should resolve to stable source identities and readable context, not merely opaque database rows.

### Human-readable projections

Machine-readable research objects also require inspectable projections:
- case records → readable case pages;
- method records → readable methods with scope, evidence lineage, and counterexamples;
- graph links → inspectable source/case relationships;
- evaluation objects → readable scenarios, with hidden answer keys separated where necessary.

### Two distinct planes

The **BFDM research access plane** optimizes for broad discovery, transparency, provenance inspection, exploratory search, reproducibility, and human review.

The **Kit cognition plane** optimizes for bounded context, salience, intent compatibility, latency, permissions, and structured precedent retrieval.

The cognitive runtime must never become the only practical way to interrogate the archive.

### Acceptance test

A researcher with repository access but without Kit, a vector database, an embedding model, the live cognitive runtime, or knowledge of internal row IDs should still be able to search for a name, phrase, concept, mechanic, or idea and reach readable source context with stable provenance.

If that fails, the corpus is not sufficiently observable even if the underlying data technically exists.
