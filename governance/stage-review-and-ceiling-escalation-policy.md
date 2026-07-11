# Stage Review and Ceiling Escalation Policy

**Policy ID:** `POLICY-STAGE-REVIEW-001`  
**Classification:** Governance / Research Operations

## 1. Purpose

The strategic compass remains fixed while operational goals evolve. This policy prevents both rigidity and repeated redefinition of the project.

## 2. Goal layers

### Strategic goal

Fixed unless changed by an explicit strategic decision:

> Produce an original ANT contribution through a materially useful PVG language and method.

### General goals

Long-lived:

- master bidirectional PVG–ANT translation;
- build reusable transfer principles;
- identify the true domain of strength and limits of PVG;
- prove an original lemma;
- prove one modest original theorem;
- produce a reviewable mathematical paper.

### Operational goals

Flexible, stage-bound, and machine-registered. They may be added, revised, blocked, or retired after a Stage Review.

## 3. Required operational-goal fields

Every operational goal records:

```text
id
title
status
parent strategic goal
research front
deliverable
measurable exit criterion
prerequisites
claim ceiling
maturity target
blocked by
next review
```

## 4. Stage Review questions

A stage closes only after answering:

1. What is now operational and reusable?
2. Which outputs are only exposition or reinterpretation?
3. Which transfer principle, mechanism, or lemma survived?
4. What failed, and what certificate records the failure?
5. What prerequisites are missing for the next stage?
6. What is the current maturity level?
7. What higher ceiling must the next stage meet?
8. Which work is stopped to preserve focus?

## 5. Ceiling escalation

The next stage must demand a stronger output than the completed stage.

```text
L0 vocabulary          → next requires exact translation
L1 exact translation   → next requires structural gain
L2 structural gain     → next requires a transfer lemma
L3 transfer principle  → next requires a research mechanism or serious lemma
L4 research mechanism  → next requires an original lemma
L5 original lemma      → next requires theorem/generalization
L6 original theorem    → next requires a reusable program
```

Repeated production at the same level does not count as strategic progress unless it completes a predefined kernel release.

## 6. One active research front

Only one original-research front may have `status=active` in `registries/program-goals.jsonl`.

Governance repair, CI maintenance, and source correction may coexist, but they may not create a second research question or consume the proof budget of the active front.

## 7. Adding a new goal

A new goal is accepted only if:

- it directly serves the strategic goal;
- its deliverable is measurable;
- its exit criterion is explicit;
- it names what existing work is paused or closed;
- it does not duplicate an existing bridge or task;
- it has passed a readiness audit.

## 8. Updating a goal

A goal may be updated when:

- a prerequisite changes;
- literature closes or reshapes the originality gap;
- a proof attempt reveals a sharper lemma;
- a negative certificate eliminates a route;
- a stage review raises the required ceiling.

Updates preserve history; they do not rewrite failed predictions as successes.

## 9. Closing a goal

Allowed closure classes:

```text
proved
reproduced
negative_certificate
known_classical_consequence
blocked_by_named_certificate
superseded_by_stronger_goal
```

`abandoned` is not sufficient without a reason and recorded state.

## 10. Project-level progress metrics

The canonical metrics are:

- certified reusable bridges;
- certified transfer lemmas;
- originality-audited questions;
- proved or refuted lemmas;
- active maturity level;
- materially PVG-dependent results;
- original theorems.

Book count, file count, and closure count are capacity indicators, not research-success metrics.