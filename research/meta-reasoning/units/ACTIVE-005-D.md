# ACTIVE-005-D — Governed Strategy Planner and Route Selection Layer

Status: specification complete / implementation not yet built
Classification: Architecture / Diagnostic
Validation status: architecture_only_unbenchmarked
Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Build the strategy-selection layer for the broader PVG–ANT Research Mind. The planner must choose and justify a route for a number-theoretic problem before detailed derivation begins.

This unit is not Goldbach-specific. It supports analytic number theory, prime-valuation geometry, their translation interface, computation, formal proof, and hybrid workflows.

## 2. Governing principle

The planner does not ask only:

```text
Can this method be used?
```

It asks:

```text
Which route best preserves the target object,
reaches the requested certificate,
controls information loss,
and minimizes scientific risk?
```

## 3. Input packet

```text
STRATEGY_QUERY
- problem_statement
- target_object
- target_claim
- domain
- scale: finite / asymptotic / uniform / local / average
- available_data
- known_hypotheses
- requested_output
- required_certificate
- computational_budget
- formalization_requirement
- novelty_question
```

Unspecified load-bearing fields remain `UNSPECIFIED`.

## 4. Strategy families

The planner may generate candidates from the following families.

### S-PVG — Prime-Valuation Geometry primary

Use when the central task concerns:

- valuation vectors and support geometry;
- divisor boxes, heights, masses, or loci;
- multiplicative structure inside integers;
- geometric organization of arithmetic fibers;
- PVG-native invariants or translations.

### S-ANT — Analytic Number Theory primary

Use when the requested certificate depends on:

- Dirichlet series or Euler products;
- character sums or L-functions;
- contour, Tauberian, or zero-density methods;
- circle method and major/minor arcs;
- sieve estimates;
- asymptotic main terms and error control;
- density, distribution, or positivity at scale.

### S-HYBRID — PVG ↔ ANT hybrid

Use when PVG organizes or transforms the arithmetic object while ANT supplies the analytic certificate, or when analytic observables require geometric interpretation.

### S-COMP — Computational / experimental

Use for:

- finite enumeration;
- conjecture generation;
- counterexample search;
- numerical diagnostics;
- matrix rank, kernel, conditioning, and spectral experiments;
- reproducibility checks.

Computational evidence must not be promoted beyond its tested domain.

### S-FORMAL — Formal proof primary

Use when the target is exact identity verification, foundational closure, machine-checked proof, dependency extraction, or proof-assistant integration.

### S-COF — Certificate optimization

Use when multiple measurements, channels, observables, or proof routes compete and the task is to optimize information retained subject to certificate constraints.

### S-LITERATURE — Bibliographic / priority route

Use when the load-bearing question is novelty, attribution, prior art, theorem scope, or historical precedence.

## 5. Candidate generation

The planner must generate at least one viable candidate and, when materially useful, competing alternatives.

Canonical candidate packet:

```text
STRATEGY_CANDIDATE
- candidate_id
- route_family
- target_representation
- required_tools
- required_inputs
- expected_information_gain
- expected_information_loss
- certificate_reach
- computational_cost
- formalization_cost
- literature_dependency
- failure_modes
- overclaim_risk
```

## 6. Evaluation dimensions

Each candidate is evaluated on separate dimensions rather than one opaque score:

```text
representation_fidelity
translation_loss
certificate_alignment
analytic_reach
computational_feasibility
formal_verifiability
stability_or_conditioning
literature_grounding
novelty_relevance
scientific_risk
reversibility
reuse_value
```

No weighted total is authoritative until weights and normalization are declared.

## 7. Hard gates

A candidate is rejected or quarantined if any hard gate fails.

```text
GATE-OBJECT-MISMATCH
GATE-CERTIFICATE-UNREACHABLE
GATE-INFORMATION-LOSS-UNSTATED
GATE-HYPOTHESIS-UNDECLARED
GATE-FINITE-TO-UNIVERSAL
GATE-NOVELTY-WITHOUT-LITERATURE
GATE-RECONSTRUCTION-WITHOUT-KERNEL
GATE-NUMERICAL-WITHOUT-CONDITIONING
GATE-FORMAL-PROOF-NOT-BUILT
GATE-TRAINING-CORPUS-NOT-AUTHORIZED
```

## 8. Route-selection rules

### Rule 1 — Certificate first

Choose according to the strongest justified output requested, not the most visually attractive representation.

### Rule 2 — Geometry does not replace analysis

A PVG reformulation may expose structure but does not by itself supply an asymptotic or positivity certificate.

### Rule 3 — Analysis does not erase geometry

An ANT route that proves an estimate may still lose structural information valuable for explanation, reconstruction, or transfer.

### Rule 4 — Computation is a bounded certificate

Finite experiments certify only the declared range and environment.

### Rule 5 — Formalization is not discovery by itself

Formal proof verifies a stated theorem and dependencies; it does not automatically establish novelty or mathematical significance.

### Rule 6 — Hybrid routes need interface contracts

Every PVG ↔ ANT hybrid route must state:

```text
source object
translation map
target observable
information preserved
information lost
inverse availability
certificate supplied by each side
```

## 9. Selection output

```text
STRATEGY_DECISION
- problem_class
- target_claim
- required_certificate
- selected_strategy
- selected_route_family
- selection_reason
- rejected_alternatives
- preserved_information
- lost_information
- required_inputs
- tools_to_invoke
- hypotheses
- expected_output_class
- confidence_ceiling
- scientific_ceiling
- next_checkpoint
```

## 10. Canonical examples

### Example D1 — Exact valuation identity

Target: prove a multiplicative valuation law.

Preferred route:

```text
PVG + FORMAL
```

Reason: exact structural theorem with machine-checkable dependencies.

### Example D2 — Average order of an arithmetic function

Preferred route:

```text
ANT primary, PVG interpretive secondary
```

Reason: the main term and error require analytic estimates; PVG may organize the observable.

### Example D3 — Local prime-density experiment

Preferred route:

```text
COMP + ANT diagnostic + PVG exploratory
```

Reason: finite data supports diagnostics and hypothesis generation, not a universal density theorem.

### Example D4 — Additive fiber reconstruction

Preferred route:

```text
PVG/HYBRID + linear algebra + COF
```

Reason: geometry defines the fiber, channel maps define measurements, and rank/kernel govern recoverability.

### Example D5 — Historical novelty claim

Preferred route:

```text
LITERATURE first
```

Reason: no mathematical derivation alone certifies priority.

## 11. Meta-review integration

The selected route must be reviewed by ACTIVE-005-A, confidence-bounded by ACTIVE-005-B, and corrected through ACTIVE-005-C when an error is found.

```text
strategy proposal
→ certificate check
→ meta-review
→ confidence calibration
→ governed release
→ error-memory update if needed
```

## 12. Future neural interface

The planner should eventually produce training-ready but not yet training-authorized records containing:

- problem features;
- candidate strategies;
- selected route;
- rejected routes with reasons;
- certificate targets;
- outcome and correction history.

These records can support future route-selection models only after corpus governance and leakage controls are established.

## 13. Acceptance criteria

ACTIVE-005-D is specification-complete when:

1. strategy families cover PVG, ANT, hybrid, computational, formal, COF, and literature routes;
2. candidate evaluation separates fidelity, certificate reach, cost, and risk;
3. hard gates prevent scientifically invalid route selection;
4. hybrid interfaces require explicit preservation/loss contracts;
5. the output is machine-readable;
6. no autonomous strategy competence is claimed.

## 14. Honest state

```text
ACTIVE-005-D = SPECIFICATION_COMPLETE
STRATEGY_ENGINE_CODE = NOT_BUILT
ROUTE_SCORING_WEIGHTS = NOT_CALIBRATED
PUBLIC_CASES = NOT_RUN
LOCKED_BENCHMARK = NOT_BUILT
AUTONOMOUS_STRATEGY_SELECTION = NOT_GRANTED
TRAINING_DATASET = NOT_AUTHORIZED
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
NEXT_ACTION = RMG-001-A
```

## 15. Next action

```text
RMG-001-A
Research Memory Graph Core Ontology and Typed Edge Schema
```
