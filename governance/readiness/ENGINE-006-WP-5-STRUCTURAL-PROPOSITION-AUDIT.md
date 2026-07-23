# ENGINE-006 WP-5 — Structural Proposition Audit Readiness

```text
Task ID: ENGINE-006-WP-5-STRUCTURAL-PROPOSITION-AUDIT
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-006
Basis: ENGINE-006-WP-4-PARENT-REVIEW-001
Decision: READY
Status: ACTIVE_CURRENT_SUBPASS
Date: 2026-07-24
Experimental expansion: NOT AUTHORIZED
Phase D: NOT AUTHORIZED
```

## Governing question

Which exact propositions survive after removing terminological duplication and reducing every statement to its standard antecedents?

The audit must identify whether any proposition uses the interaction between valuation geometry and additive prime-pair incidence essentially.

## Required artifact

```text
research/pvg-space-deepening/engine-006-structural-proposition-audit.md
```

## Required candidate families

At minimum, audit candidates concerning:

1. valuation/integer reconstruction;
2. fixed-base pair/coordinate reconstruction;
3. spectrum/fiber reconstruction;
4. incidence/row-family reconstruction with empty-row registry;
5. support and parity factorization;
6. failure of base reconstruction from a bare spectrum;
7. failure of integer-owner reconstruction from support incidence;
8. commutativity of valuation-to-support-to-route maps;
9. necessity of retained labels for inverse maps;
10. whether any proposition is genuinely interaction-essential.

## Candidate record schema

Every candidate must contain:

```text
Proposition ID
Statement
Dependencies
Proof or counterargument
Classification
Valuation-essential: YES/NO
Additive-essential: YES/NO
Interaction-essential: YES/NO
Standard reconstruction status
Proof-strength status
Finite-scope dependence
```

## Required classification vocabulary

```text
IDENTITY
PROVED
FINITE-VERIFIED
INTERPRETATION
HYPOTHESIS
OPEN
REDUNDANT_STANDARD_FACT
NOT_WELL_POSED
```

## Interaction-essential criterion

A proposition is `interaction-essential = YES` only if deleting either the valuation-side data or the additive-incidence-side data destroys the proposition's content or proof, and the result cannot be restated as two independent standard facts.

Merely writing `nu(N)` and `D(N)` in one formula is insufficient.

## Required negative audit

The artifact must explicitly record candidates rejected because they are:

```text
aliases
standard identities
finite observations only
claims caused by forgotten labels
claims with no well-defined domain
claims that silently mix ordered and unordered prime pairs
claims that omit the empty-row registry
```

## No-new-data rule

WP-5 must use only:

- exact definitions;
- proved statements already present in ENGINE-004 and ENGINE-006;
- the frozen finite registry when a counter-witness is already recorded;
- logical consequences of the typed map system.

No new computation or enumeration is authorized.

## Required end-state decision

The checkpoint must return exactly one recommendation:

```text
OPEN_WP_6_FINAL_RESEARCH_VALUE_DECISION
REVISE_WP_5
TERMINATE_ENGINE_006_AS_STANDARD_REINTERPRETATION
```

This recommendation is advisory to the parent review. WP-6 is not opened automatically.

## Prohibitions

```text
new experiment = false
new finite count = false
new dataset = false
cap/support expansion = false
weighting/asymptotics = false
classifier work = false
new conjecture = false
novelty promotion = false
Phase D = false
WP-6 automatic opening = false
```

## Scientific classification

```text
definitions and direct inverse formulas = IDENTITY
complete logical consequences = PROVED
frozen-registry-only witnesses = FINITE-VERIFIED
terminological synthesis = INTERPRETATION
unproved interaction advantage = OPEN
```

No original theorem, independent-theory, publication-readiness, Goldbach, PNT, RH, or GRH claim is authorized.
