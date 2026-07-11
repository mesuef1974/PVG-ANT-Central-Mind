# Task-Triggered Knowledge Activation Policy

**Policy ID:** `POLICY-TASK-KNOWLEDGE-001`  
**Status:** governing  
**Classification:** Governance / Research Operations

## 1. Rule

No new knowledge acquisition, book mining, formalization pass, statistical analysis, or computational experiment begins without a named research task.

The task determines what prior knowledge is required. The repository does not treat all previously encountered knowledge as automatically operational.

## 2. Readiness states

Each prerequisite is classified as one of:

```text
A — operationally_ready
B — known_but_needs_activation
C — source_available_not_extracted
D — missing
```

### A — operationally ready

The mind can state the exact definition or theorem, hypotheses, normalization, error term, source, and role in the current argument.

### B — known but needs activation

The concept is known or already recorded, but the exact version needed by the task has not been retrieved and checked.

### C — source available, not extracted

A local or linked source exists, but the required result is not yet integrated into an operational unit.

### D — missing

No adequate trusted source or implementation is currently available.

## 3. Decision

A task receives one decision:

```text
READY
NOT_READY
```

`READY` requires that every load-bearing prerequisite be in state A. Non-load-bearing context may remain B if it cannot change the proof or classification.

## 4. Minimum sufficient knowledge

When a task is `NOT_READY`, acquisition is limited to the smallest package sufficient to attempt the task rigorously.

The acquisition package must record:

```text
Object
Exact theorem/tool
Hypotheses
Uniformity range
Main term
Error term
Normalization
Primary source
Secondary source if needed
Role in current task
Known limitation
PVG bridge
Honest classification
```

Mining stops when the readiness gate is satisfied. A full book is not mined merely because one theorem is needed.

## 5. Tool activation

### Lean

Activate only for an active research lemma, a reusable structural invariant, or a high-risk formal edge case.

### Python

Activate for deterministic construction, symbolic/numeric checking, experiment, falsification, reproducibility, or CI.

### R

Activate for an independent statistical implementation or a method whose certificate genuinely requires R.

### Literature search

Activate for priority, current best ranges, exact hypotheses, or missing sources.

### Experiment

Activate only when its possible outcomes alter a research decision.

## 6. Knowledge return

Every acquired prerequisite must return to the Central Mind after use in a reusable form. At minimum it records:

- theorem or tool statement;
- assumptions and failure modes;
- source;
- where it was used;
- PVG translation;
- classification;
- whether it is now `operationally_ready` for future tasks.

A result may not remain only inside a one-off notebook, chat, or report.

## 7. Readiness tests

Knowledge is operational only if the mind can:

1. state definitions without ambiguity;
2. state the prior theorem with conditions;
3. explain why it applies;
4. distinguish known input from the new claim;
5. name the remaining gap;
6. give a proof or experiment plan;
7. identify likely failure points;
8. cite the source.

## 8. Prohibitions

- no broad reading program without a current task;
- no claim that local availability equals integration;
- no claim that integration equals mastery;
- no repeated acquisition of knowledge already operational;
- no tool activation for appearance or completeness;
- no delaying a viable lemma attempt to pursue non-load-bearing background.

## 9. Required template

Every new research task uses:

`governance/templates/research-readiness-card.md`

The card is updated when a prerequisite changes state.