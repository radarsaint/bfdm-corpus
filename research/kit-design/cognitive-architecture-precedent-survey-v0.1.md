# Kit Cognitive Architecture — Precedent Survey v0.1

**Date:** 2026-10-04  
**Status:** Working research artifact, not an implementation specification  
**Branch:** `research/kit-cognitive-architecture-survey-v1`

## Research question

Kit is intended to become one persistent Dungeon Master identity that can scale from:

- running a single-player D&D game;
- running ordinary multiplayer D&D for other people;
- designing campaigns;
- collaborating with a human director during preproduction;
- operating persistent campaigns over weeks;
- globally running Roanoke-style many-player productions with concurrent scenes, NPCs, factions, clocks, shared consequences, guest DMs, and campaign-level events;
- using Brendon's documented historical experience without requiring unrestricted access to the private BFDM archive during ordinary operation.

The purpose of this survey is not to find one existing system that already does this. None identified so far does. The useful question is:

> Which mature mechanisms from cognitive architectures, expert-knowledge research, memory systems, case-based reasoning, distributed systems, planning, interactive narrative, and evaluation should Kit steal rather than reinvent?

The current strongest conclusion is that Kit's eventual "brain" should **not** be modeled as one database, one vector store, one prompt, or one model instance. The strongest precedents consistently separate current state, working context, episodic experience, generalized knowledge, procedures, goals/intentions, and durable world processes.

This is still a research conclusion, not a final technical design.

---

# 1. Expert knowledge extraction: Cognitive Task Analysis

## Closest precedent

**Critical Decision Method (CDM)** is a Cognitive Task Analysis method specifically developed to elicit tacit expert knowledge from difficult real-world incidents.

Hoffman, Crandall, and Shadbolt describe CDM as a **multiple-pass retrospective analysis of an event**, guided by probes that recover cues, assessments, goals, expectations, options, and decisions. The method can produce timelines, Situation Assessment Records, and decision-requirement representations.

Primary source:

- Hoffman, Crandall & Shadbolt (1998), *Use of the Critical Decision Method to Elicit Expert Knowledge*  
  https://journals.sagepub.com/doi/10.1518/001872098779480442

A systematic review of CTA use in clinical and health-services research found CTA especially useful where expert performance occurs under complexity, uncertainty, and time pressure, and documented uses for intervention design, protocols, and practice guidance.

- https://pmc.ncbi.nlm.nih.gov/articles/PMC8903544/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10012243/

## What it solves for Kit

BFDM does not merely need statements about what Brendon likes. It needs to reconstruct:

- what he noticed;
- what he believed was happening;
- what information he sought;
- what competing goals mattered;
- what alternatives were considered or ignored;
- what he expected would happen;
- what action he chose;
- what later evidence changed his view.

This is exactly the class of knowledge CTA was built to expose.

## What to steal

1. **Multiple-pass reconstruction.** Never trust the first summary of an event as the complete analysis.
2. **Timeline first.** Reconstruct what happened before asking why.
3. **Cue extraction.** Record what facts became salient to the expert.
4. **Expectation probes.** Ask what the expert expected next and what would have surprised them.
5. **Counterfactual probes.** Ask what a less experienced DM might have done and why that would have been weaker.
6. **Decision requirements.** Distill what information a competent system would need in order to make the decision.
7. **Artifact-aware elicitation.** Use the actual historical documents, chat logs, drafts, maps, and results to reconstruct the incident before asking Brendon for retrospective interpretation.

## What not to steal blindly

CDM commonly depends on retrospective expert memory. BFDM often has something better: the actual historical record. Retrospective statements should therefore be one evidence type, not an automatic override of contemporaneous evidence.

## BFDM implication

The primary research object should be a **creative/DM decision trajectory**, not an isolated quote.

---

# 2. Organizational learning: NASA and military lessons-learned systems

## Closest precedent

NASA explicitly separates a lessons-learned lifecycle into:

**Collect → Record → Disseminate → Apply**

NASA states that lessons are drawn from actual programs/projects, recorded in reviewed systems such as LLIS, disseminated to practitioners, and then integrated into processes, checklists, handbooks, policy, training, and other operational artifacts.

Primary sources:

- NASA Lessons Learned lifecycle  
  https://www.nasa.gov/learning-resources/for-professionals/appel-lessons-learned/
- NASA LLIS overview  
  https://www.nasa.gov/nasa-lessons-learned/
- NASA knowledge management  
  https://www.nasa.gov/learning-resources/for-professionals/appel-knowledge-management/

NASA also documents a specific lesson that **continuous capture throughout the project lifecycle is more effective than waiting until the end**, because staff transition and memory decay make later reconstruction difficult.

- https://llis.nasa.gov/lesson/600

The U.S. Army's After Action Review (AAR) tradition similarly focuses on reconstructing what happened and why, with multiple participants discovering strengths and weaknesses rather than receiving a single top-down critique.

- Center for Army Lessons Learned AAR material  
  https://api.army.mil/e2/c/downloads/2023/01/31/e747aebc/22-05.pdf

## What it solves for Kit

This is the best precedent for the boundary between:

- private archive;
- researched lesson;
- operational method;
- changed practice.

A raw historical incident is not itself a reusable doctrine. A lesson must be reviewed and then translated into forms practitioners can actually use.

## What to steal

1. **Archive != lesson.**
2. **Lesson != policy.**
3. **Reviewed application layer.** A lesson becomes operational only after deliberate validation.
4. **Continuous capture.** Kit's current campaigns should emit traces while events are fresh.
5. **Multiple output forms.** A validated finding may become a procedure, checklist, evaluation scenario, retrieval cue, training example, or architecture requirement.
6. **Push as well as pull.** Mature knowledge systems do not rely only on users knowing what to search for; relevant knowledge can be surfaced when a matching situation appears.

## What not to steal blindly

Institutional lessons-learned systems often become graveyards of documents that users technically *can* search but rarely do. Kit needs recognition-triggered retrieval, not merely an indexed library.

---

# 3. Cognitive architectures: Soar as the strongest structural precedent

## Closest precedent

Soar is a long-running general cognitive architecture. Of particular relevance, it evolved beyond a single memory mechanism because that proved insufficient in complex tasks.

Soar now distinguishes:

- working memory;
- procedural knowledge;
- semantic memory;
- episodic memory;
- reinforcement learning.

Soar's own documentation notes that early versions used a single permanent-knowledge representation and a single temporary-knowledge representation, but complex applications forced the architecture to add semantic and episodic long-term memories and additional learning mechanisms.

Primary sources:

- Soar introduction  
  https://soar.eecs.umich.edu/soar_manual/01_Introduction/
- Soar overview  
  https://soar.eecs.umich.edu/home/About/
- Episodic memory  
  https://soar.eecs.umich.edu/soar_manual/07_EpisodicMemory/
- Semantic memory  
  https://soar.eecs.umich.edu/soar_manual/06_SemanticMemory/

Soar's episodic memory automatically records the agent's stream of experience and allows deliberate retrieval of prior episodes. It supports cue-based retrieval, negative cues, temporal constraints, surface matching, and optional structural graph matching.

## What it solves for Kit

The conceptual distinction is almost exactly what Kit requires:

- **working state:** what matters right now;
- **episodic memory:** what happened in particular past situations;
- **semantic knowledge:** generalized facts and concepts;
- **procedural knowledge:** how to do things;
- **decision cycle:** combine current perception with relevant retrieved knowledge.

## What to steal

1. **Explicit memory types.** Do not flatten all remembered material into documents plus embeddings.
2. **Current working context distinct from long-term stores.**
3. **Cue-based episodic retrieval.**
4. **Negative cues.** "Find similar cases, but not cases where X was true."
5. **Structural matching.** Surface similarity should be followed by a deeper fit test.
6. **Temporal retrieval.** Recency and chronology matter.
7. **Retrieved memory is advisory, not authoritative current reality.**
8. **Decisions assembled at runtime.** Do not compile all possible judgments into rigid scripts.

## What not to steal blindly

Soar is not an LLM-native architecture, and reproducing its production-rule machinery wholesale would likely create unnecessary complexity. The useful part is the cognitive decomposition and retrieval concepts.

---

# 4. Modern agent memory: 2026 evidence

The strongest current work rejects the idea that "memory" means a single vector database.

## 4.1 HeLa-Mem: episodic + semantic consolidation

HeLa-Mem maintains:

1. an episodic graph of experiences and associations;
2. a semantic store created by distilling dense recurring episodic structure.

It uses association, consolidation, and spreading activation.

- Zhu et al. (ACL 2026)  
  https://aclanthology.org/2026.acl-long.625/

### Steal

- Keep episodes and generalized knowledge separately.
- Let repeated relationships/associations help reveal what deserves semantic consolidation.
- Preserve the episodes underneath the distilled rule.

### Caution

Repeated co-activation is not automatically causal or important. BFDM's research review must still distinguish repetition from genuine transferable method.

---

## 4.2 Cognitive Scaffold: fluid working context + crystallized knowledge

Cognitive Scaffold separates:

- a **Fluid Working Context** for immediate reasoning;
- a persistent **Knowledge Graph** for long-term retention.

It crystallizes saturated context into structured atomic event snapshots and uses thought-driven retrieval to recover evidence later.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.1170/

### Steal

- Current cognitive state should be compact and fluid.
- Durable memory should be structured rather than an endlessly growing transcript.
- Consolidation should preserve atomic entities, numbers, relationships, and events.
- Retrieval can be initiated by reasoning when the agent realizes it needs something.

### Caution

Deep-research tasks are not campaigns. We should steal the memory boundary, not assume its exact knowledge graph schema fits roleplaying worlds.

---

## 4.3 EMA: episodic memory units + memory filtering

EMA converts dialogue/history into **Episodic Memory Units** and uses a MemDecider to suppress unnecessary memories.

- ACL Findings 2026  
  https://aclanthology.org/2026.findings-acl.250/

### Steal

Kit needs a first-class decision about **whether a memory belongs in the current situation at all**. More retrieved context is not necessarily better.

---

## 4.4 LightMem: online/offline split

LightMem separates:

- short-term memory;
- mid-term reusable summaries;
- long-term consolidated knowledge.

Critically, it separates low-latency **online retrieval** from **offline consolidation**.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.588/

### Steal

This maps cleanly to Kit:

**during play:** retrieve quickly and avoid expensive self-research.

**between scenes/sessions/production intervals:** consolidate, summarize, link, and reconsider what should become durable.

This is likely important for both latency and epistemic safety.

---

## 4.5 STITCH: retrieve by intent, not words

STITCH indexes trajectory steps using structured **contextual intent**, including:

- latent goal;
- action type;
- salient entity types.

It suppresses history that is semantically similar but intent-incompatible.

- ACL Findings 2026  
  https://aclanthology.org/2026.findings-acl.584/

### Steal aggressively

This is one of the closest mechanisms to Kit's needs.

A "marked deck" situation should not retrieve every gambling scene. The system needs to know whether the present goal is:

- detecting cheating;
- winning money;
- building an NPC relationship;
- learning rules;
- escaping a room;
- testing an exploit.

Intent should be part of the retrieval key.

---

## 4.6 Nemori: what deserves memory?

Nemori treats memory value as a future-utility question. It integrates raw interactions into episodes and then distills semantic knowledge according to prediction error / informational utility.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.1607/

### Steal conceptually

Do not store everything forever merely because it happened.

But for Kit, retention policy must differ by layer:

- authoritative game events may need permanent storage;
- ephemeral working thoughts should not;
- professional lessons require review;
- player preference hypotheses need confidence and revision;
- BFDM raw history is preserved independently for archival reasons.

"Memory value" is domain-specific, not one universal score.

---

## 4.7 Memory anchoring is a real danger

A 2026 empirical study found strong **experience-following behavior**: when a retrieved memory looks highly similar to the current task, agents tend to produce highly similar behavior.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.27/

A separate 2026 study on controllable memory use calls out **Memory Anchoring**, where accumulated history can make an agent over-rely on the past and reduce innovation.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.670/

### Major Kit implication

Precedent cannot mean:

> retrieve most similar case → imitate it.

Kit needs:

1. candidate precedents;
2. structural-fit analysis;
3. differences;
4. counterexamples;
5. current campaign intent;
6. explicit permission to ignore precedent.

This may be one of the central cognitive safeguards.

---

# 5. Case-Based Reasoning and analogy

## Closest precedent

Classical Case-Based Reasoning follows the 4R cycle:

**Retrieve → Reuse → Revise → Retain**

A 2025 review explicitly argues that CBR is a useful architecture for LLM agents because it provides structured precedent, adaptation, and accountable learning rather than simple RAG.

- Hatalis, Christou & Kondapalli (2025)  
  https://arxiv.org/abs/2504.06943

A 2025 experimental study of strategic analogical reasoning found a useful asymmetry: LLMs produced broad candidate analogies with high recall but often matched on superficial similarities, while humans were more precise at identifying causal/structural fit.

- Puranam, Sen & Workiewicz (2025)  
  https://arxiv.org/abs/2505.00603

Soar's episodic memory also demonstrates a practical two-stage idea: inexpensive surface matching first, followed by optional structural graph matching.

## What it solves for Kit

A veteran DM frequently thinks through precedent without obeying a universal rule:

> "I've seen something like this before. What's the same? What's different?"

That is closer to CBR than ordinary RAG.

## What to steal

### Two-stage precedent retrieval

**Stage A — broad recall**

Retrieve several candidate cases using:
- entities;
- situation type;
- goals;
- pressure;
- player intent;
- campaign layer;
- mechanics;
- outcome class;
- embeddings.

**Stage B — structural fit**

Compare:
- causal structure;
- competing goals;
- constraints;
- knowledge boundaries;
- scale;
- intended experience;
- what would happen if no intervention occurred.

Then retrieve at least one **negative or contrasting case** when available.

### Adapt, don't copy

A precedent should output:
- transferable structure;
- relevant difference;
- candidate implication;
- confidence.

Not:
- "do what happened last time."

---

# 6. Learning experience into reusable skill

## Voyager

Voyager stores successful complex behaviors as an executable **skill library**. Skills are compositional and can be reused in new environments.

- https://arxiv.org/abs/2305.16291

### Steal

Some Kit knowledge should become reusable procedures rather than prose reminders.

Examples may eventually include:
- launch-readiness review;
- faction activation;
- encounter postmortem;
- scene recovery;
- clue-legibility audit;
- campaign-health review.

These need not all be executable code, but they should have inputs, conditions, steps, and outputs.

---

## LifeMem

LifeMem (September 2026) clusters accumulated trajectories by their **underlying workflow** to extract reusable skills, then retrieves both skills and relevant trajectories on new tasks.

- https://arxiv.org/abs/2609.12655

### Steal aggressively

This suggests an eventual BFDM pipeline:

**many historical trajectories**
→ cluster by decision/workflow structure
→ derive candidate procedures
→ keep representative source cases
→ use both method + precedent at runtime.

That is much closer to BFDM's real goal than flattening everything into "principles."

---

## External memory does not solve continual learning automatically

A 2026 study argues that moving learning into external memory merely relocates the stability/plasticity problem: old and new experiences compete at retrieval time. It found abstract procedural memories often transfer better than detailed trajectories, while negative transfer particularly harms hard cases.

- https://arxiv.org/abs/2604.27003

### Kit implication

We likely need both:

- detailed episodes for fidelity and precedent;
- abstract procedures for transfer.

And retrieval must decide which level of abstraction is useful.

---

# 7. Retrieval over very large archives

## GraphRAG

GraphRAG was designed to answer **global questions over large private corpora**, where naive top-k vector retrieval fails. It builds entity/relationship graphs, hierarchical communities, and community summaries.

- Microsoft Research, 2024  
  https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/

Microsoft later introduced dynamic and hybrid local/global search approaches such as DRIFT.

- https://www.microsoft.com/en-us/research/blog/introducing-drift-search-combining-global-and-local-search-methods-to-improve-quality-and-efficiency/

## RAPTOR

RAPTOR recursively clusters and summarizes documents into a tree so retrieval can operate at multiple levels of abstraction.

- ICLR 2024  
  https://openreview.net/pdf?id=GN921JHCRw

## What they solve for BFDM

BFDM must support questions at radically different scales:

**local:**  
"What was actually said during this scene?"

**episode:**  
"How did this mechanic change from design through play?"

**cross-campaign:**  
"What patterns exist in how Brendon turns historical source material into gameable structures?"

**global:**  
"What changed in campaign-production practice from early Roanoke through Empire City?"

One retrieval mode will not answer all four well.

## What to steal

- hierarchical retrieval;
- graph relationships;
- local vs global query modes;
- summaries as derived navigation layers;
- source-level fallback.

## What not to steal

Do not treat LLM-generated graph edges or summaries as source truth. BFDM needs provenance beneath every derived representation.

---

# 8. Persistent world and many simultaneous actors

## 8.1 Virtual actors: Microsoft Orleans

Orleans implements the **virtual actor** model. A grain represents an independently addressable entity that can activate on demand, hold persistent state, receive messages, and use durable reminders.

Relevant docs:

- overview  
  https://learn.microsoft.com/en-us/dotnet/orleans/overview
- persistence  
  https://learn.microsoft.com/en-us/dotnet/orleans/grains/grain-persistence
- timers/reminders  
  https://learn.microsoft.com/en-us/dotnet/orleans/grains/timers-and-reminders

Durable reminders can reactivate inactive grains after time passes.

## What it solves for Kit

Roanoke-scale operation may include many things that conceptually persist independently:

- NPCs;
- factions;
- parties;
- locations;
- organizations;
- businesses;
- rituals;
- investigations;
- wars;
- pursuits.

Not all should literally become software actors, but the virtual-actor model is a strong architectural precedent for independently persistent entities that need not all remain "awake" simultaneously.

## What to steal

- stable entity identity independent of process lifetime;
- lazy activation;
- persistent per-entity state;
- message-based interaction;
- durable low-frequency reminders.

## What not to steal

Do not model every goblin as an autonomous grain simply because the framework allows it. Persistence should follow gameplay need.

---

## 8.2 Durable workflows: Temporal

Temporal provides durable execution for workflows whose state and progress survive server crashes or outages.

- https://docs.temporal.io/temporal

## What it solves for Kit

Some campaign processes are better modeled as workflows than as autonomous minds:

- "ritual completes in three days unless interrupted";
- "send result after voting closes";
- "faction checks for response after 24 hours";
- "campaign event advances through stages";
- "player application waits for approval";
- "guest DM owns scene until completion";
- "ship arrives after travel time."

## What to steal

Use durable workflow machinery for **processes**, rather than forcing the LLM to remember that something should happen later.

This is an engineering system, not cognition.

---

# 9. Actor cognition: BDI remains useful

The Belief–Desire–Intention tradition models agents in terms of:

- **beliefs:** what the actor thinks is true;
- **desires/goals:** what it wants;
- **intentions:** what it is currently committed to doing;
- **plans:** ways to pursue those goals.

Modern agent-programming research still treats BDI as useful for integrating reactive and proactive behavior in dynamic environments.

Sources:

- Georgeff et al., *The Belief-Desire-Intention Model of Agency*  
  https://link.springer.com/book/10.1007/3-540-49057-4
- review of BDI agent programming  
  https://link.springer.com/article/10.1007/s10458-020-09453-y
- 2026 BDI simulation work  
  https://link.springer.com/article/10.1007/s10458-026-09744-w

## What to steal

KRABS already points in this direction.

Important NPC/faction state should explicitly distinguish:

- world truth;
- actor belief;
- actor goal;
- current intention/commitment;
- available means;
- relationships;
- reconsideration triggers.

Dialogue should be downstream of that cognition.

## What not to steal

Pre-authored BDI plan libraries are too rigid for much of D&D. The representation is more useful than treating classical BDI execution as the whole solution.

---

# 10. Interactive narrative and experience management

## CALYPSO

CALYPSO studies LLMs as Dungeon Master's assistants and recognizes DMing as a simultaneous cognition problem: absorb setting/monster information, synthesize scenes, and respond consistently to players.

- AIIDE 2023  
  https://ojs.aaai.org/index.php/AIIDE/article/view/27534

It is much narrower than Kit but directly validates the domain difficulty.

---

## Narrative planning

A 2024 survey covers the use of automated planning to construct and reason about stories.

- https://ojs.aaai.org/index.php/ICAPS/article/view/31509

Recent interactive-story research increasingly treats narrative control as a spectrum between:

- emergent local-agent simulation;
- reactive rules;
- centralized narrative planning.

A 2025 "triangle" framework argues that none of these extremes is sufficient for scalable controllable interactive storytelling.

- https://ojs.aaai.org/index.php/AIIDE/article/view/36858

## Major Kit implication

This is extremely close to the architectural tension of a large D&D campaign.

**Pure local simulation** can produce coherent NPC behavior but lose the campaign through-line.

**Pure central story planning** preserves structure but can fight player-created history.

**Pure reactivity** handles immediate events but drifts over long horizons.

Kit likely needs a hybrid:

- local actor autonomy;
- campaign-level concerns and intended experiences;
- reactive scene judgment;
- selective longer-horizon planning;
- no precomputed player story.

That is a research direction worth pursuing explicitly.

---

## Strong story experience management

2025 work in experience management models an automated storytelling agent trying to preserve player autonomy while avoiding narrative dead-ends.

- https://ojs.aaai.org/index.php/AIIDE/article/view/36828

A separate 2025 human study examined player/GM improvisation and found meaningful relationships between perceived structure and agency.

- https://ojs.aaai.org/index.php/AIIDE/article/view/36827

## What to steal

Not "plot planning."

Steal the idea that **campaign health can have protected constraints**:

- unresolved but still playable;
- important material remains reachable;
- player agency remains meaningful;
- campaign cannot soft-lock;
- operational obligations eventually complete.

This maps well to KRABS's distinction between director intent and scripts.

---

# 11. Evaluation must be trajectory-level

## Plan-RewardBench

Plan-RewardBench evaluates whether judges can distinguish good and deceptively bad **agent trajectories**, including complex planning and error recovery. Performance declines as trajectories get longer.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.1062/

## DeepPlanning

DeepPlanning evaluates long-horizon planning requiring:

- active information gathering;
- local constraints;
- global constraints;
- optimization across the whole plan.

Frontier agents still struggle.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.335/

## AgencyBench

AgencyBench uses realistic scenarios averaging roughly 90 tool calls and very large contexts, evaluating several agentic capabilities over extended tasks.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.337/

## LoCoMo-Plus

LoCoMo-Plus tests whether agents can remember and apply **latent constraints** when later queries do not explicitly restate the original cue.

- ACL 2026  
  https://aclanthology.org/2026.acl-long.1150/

## What to steal

Kit evaluation should not primarily ask:

> Did this answer sound like a good DM?

It should evaluate trajectories.

A held-out historical case can test separately:

1. did Kit retrieve the relevant facts?
2. did she notice the important cue?
3. did she identify what kind of situation this was?
4. did she seek missing information?
5. did she retrieve useful precedent?
6. did she distinguish precedent from current reality?
7. did she choose a defensible intervention?
8. did she adjudicate correctly?
9. did she update authoritative state?
10. did she express the result clearly?
11. did the decision remain defensible several steps later?
12. did she avoid needless intervention?
13. did she preserve campaign-level constraints?

This supports and extends KRABS's existing failure taxonomy.

---

# 12. Preliminary subsystem map

This is **not** yet a final architecture.

| Kit need | Strongest precedents | Candidate mechanism |
| --- | --- | --- |
| Current authoritative world truth | event sourcing / structured game runtime | external symbolic state |
| Immediate cognitive situation | Soar working memory; Cognitive Scaffold | bounded fluid working context |
| Particular past experiences | Soar EpMem; EMA; HeLa-Mem | episodic store |
| General facts/concepts | Soar semantic memory; HeLa-Mem | semantic knowledge |
| Reusable DM/design methods | CTA + NASA lessons + Voyager/LifeMem | procedural/method library |
| Historical precedent | CBR; Soar structural match | case bank + structural retrieval |
| Retrieve the right thing | STITCH; agentic RAG | intent-aware active retrieval |
| Avoid precedent overfitting | memory-anchoring research | differences + counterexamples + reliance control |
| NPC/faction cognition | BDI | belief/goal/intention/means state |
| Independent persistent entities | Orleans | virtual-actor-like persistence where justified |
| Long-running clocks/processes | Temporal; Orleans reminders | durable workflows/reminders |
| Campaign-level narrative health | experience management + narrative planning | global concern layer, not fixed plot |
| Learning from new campaigns | LightMem; LifeMem; NASA LL | offline consolidation/research loop |
| Evaluating judgment | Plan-RewardBench; DeepPlanning; held-out history | trajectory evaluation |

---

# 13. Architecture patterns we should steal aggressively

## 13.1 Separate truth from memory

Current authoritative world state is not an LLM recollection.

Memory may describe or retrieve world history, but it does not define truth.

---

## 13.2 Separate working context from durable knowledge

The reasoning model should receive a deliberately assembled situation, not the entire campaign history.

---

## 13.3 Separate episodic from semantic/procedural knowledge

Kit should be able to know both:

> "This happened before."

and:

> "Across many cases, this is usually the important structure."

Neither should replace the other.

---

## 13.4 Retrieve by intent and decision structure

Search must include what Kit is currently trying to accomplish, not merely shared nouns.

---

## 13.5 Use multiple abstraction levels

A single query may need:
- verbatim source;
- event;
- episode;
- precedent case;
- generalized method;
- campaign-level synthesis.

---

## 13.6 Precedent retrieval should be adversarial

For consequential judgments, retrieve:

- best matching precedent;
- important differences;
- at least one counterexample or incompatible case when available.

This directly combats memory anchoring.

---

## 13.7 Consolidation should usually be offline

Ordinary play can record experience.

It should not casually rewrite professional doctrine.

Proposed loop:

**play → trace → outcome → review/research → candidate lesson → validation → published knowledge release**

---

## 13.8 Actor state and workflow state are different things

A faction may need beliefs/goals/intentions.

A countdown may only need durable process state.

Do not turn every moving world process into an LLM agent.

---

## 13.9 Narrative management should constrain, not script

Campaign intent should identify:
- experiences worth producing;
- protected relationships/structures;
- active pressures;
- important possible payoffs;
- unacceptable dead-ends.

It should not precompute the players' story.

---

## 13.10 Evaluation needs hidden historical futures

Use history as a natural experiment.

Give Kit only what was knowable at historical time T.

Hide what Brendon actually did and what later happened.

Evaluate Kit's recognition, retrieval, judgment, execution, and long-horizon consequences before revealing the historical continuation.

---

# 14. Architectures to avoid

## One giant RAG index

Fails to distinguish:
- truth vs memory;
- current campaign vs old precedent;
- episode vs generalized method;
- player belief vs world truth;
- private archive vs distributable competence.

## Raw archive access as ordinary cognition

Creates privacy, latency, contamination, and anchoring problems.

## Nearest-neighbor precedent = decision

High risk of superficial analogy and behavior copying.

## LLM prose as world state

Narrative output must not become the only authoritative state representation.

## Automatic self-modifying doctrine

One session should not rewrite Kit's general DM methodology.

## Every entity as an autonomous agent

Wasteful and difficult to control. Use actor-like persistence only when independent cognition/process truly matters.

## Central plot planner

Risks converting director intent into railroading and suppressing emergent play.

## Summaries replacing evidence

Derived summaries are navigation and compression layers, not the archive.

---

# 15. Strongest provisional architecture hypothesis

The evidence currently favors a **cognitive orchestration architecture**, not a monolithic "brain database."

Conceptually:

```text
AUTHORITATIVE GAME / WORLD STATE
    entities, geometry, rules, event history, clocks
                    |
                    v
          SITUATION ASSEMBLER
                    |
          FLUID WORKING CONTEXT
                    |
                    v
             KIT JUDGMENT
          /        |        \
         /         |         \
  EPISODIC     PROFESSIONAL   CURRENT
  PRECEDENT      KNOWLEDGE    CAMPAIGN MODEL
         \         |         /
          \        |        /
           ACTIVE RETRIEVAL
                    |
                    v
              ACTION / PLAN
                    |
                    v
              EVENT COMMIT
                    |
          +---------+---------+
          |                   |
          v                   v
   PLAYER PERFORMANCE      NEW TRACE
                              |
                              v
                    OFFLINE CONSOLIDATION
                              |
                    BFDM / REVIEW / LEARNING
```

At larger scale, actor/faction persistence and durable workflows sit **around** this cognitive loop rather than inside one prompt.

---

# 16. What remains genuinely open

1. Whether the future Kit cognitive core should be one service or an orchestration layer spanning several services.
2. Exact representation for professional methods: JSON methods, graph nodes, executable procedures, production-like rules, or hybrid.
3. Exact representation for historical cases.
4. How to perform structural precedent matching cheaply enough for live play.
5. How much autonomous memory writing Kit should be allowed during ordinary play.
6. How campaign-level concerns should compete for salience.
7. Whether important NPC/faction cognition should use an explicit BDI-like representation or a simpler state schema.
8. Which world entities justify actor-style persistent runtime objects.
9. How to preserve creative novelty while still benefiting strongly from precedent.
10. How to evaluate week-scale or month-scale campaign quality without reducing it to local proxies.
11. How to export BFDM-derived professional knowledge without leaking private provenance while maintaining an internal trace to the evidence.
12. Where exactly the boundary should fall between `dnd-solo`, the future cognitive core, and product-specific execution surfaces.

---

# 17. Immediate research recommendation

Do **not** implement the cognitive core yet.

The next research pass should convert this broad survey into competing architectural designs.

At minimum:

### Architecture A — cognitive orchestrator over specialized stores
Kit reasoning remains in the active model/runtime. A cognitive service assembles state and retrieves specialized memory.

### Architecture B — persistent cognition service
A dedicated Kit cognitive runtime owns professional memory, campaign cognition, episodic memory, retrieval, consolidation, and long-horizon concern tracking, while game runtimes provide authoritative world state and execution.

### Architecture C — hybrid actor/workflow cognitive fabric
Persistent campaign actors and processes run independently; Kit's cognitive coordinator supervises attention and judgment across them.

Each should be evaluated against:
- solo latency;
- ordinary multiplayer use;
- portability to another user's campaign;
- campaign-design workflow;
- Roanoke-scale concurrency;
- privacy boundary with BFDM;
- inspectability;
- failure recovery;
- cost;
- ease of evaluation;
- ability to evolve without rewriting historical data.

Only after that comparison should we commit to the new repository/runtime boundary.
