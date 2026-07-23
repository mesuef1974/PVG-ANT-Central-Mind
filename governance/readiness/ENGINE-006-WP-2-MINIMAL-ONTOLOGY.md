# ENGINE-006 WP-2 — Minimal Ontology Readiness

```text
Task ID: ENGINE-006-WP-2-MINIMAL-ONTOLOGY
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-006
Basis: ENGINE-006-WP-1-PARENT-REVIEW-001
Decision: READY
Status: ACTIVE_CURRENT_SUBPASS
Date: 2026-07-23
Experimental expansion: NOT AUTHORIZED
Phase D: NOT AUTHORIZED
```

## Governing question

What is the smallest nonredundant collection of objects and maps needed to recover every exact ENGINE-004 reconstruction and information-loss statement?

## Candidate core objects

The review must begin from, but may reduce, the following candidate list:

```text
valuation vector nu(N)
support supp(N)
integer base point N
prime-pair fiber R_2(N)
centered coordinate Delta or d
governed coordinate row D(N)
integer-coordinate incidence relation I
support projection sigma
parity route rho
```

No candidate is retained merely because it appeared in prior terminology.

## Required tests for each retained object

Every retained object must have:

1. a precise definition;
2. a distinct mathematical role;
3. a dependency list;
4. at least one claim that cannot be stated as cleanly after removing it;
5. a statement of whether it is primitive, derived, or an alias;
6. a statement of what information it retains and loses.

## Required map audit

At minimum, define and classify:

```text
valuation vector -> integer
integer -> support
integer -> parity route
prime pair over N -> centered coordinate
(N, centered coordinate) -> prime pair
(N, D(N)) -> complete prime-pair fiber
incidence relation -> spectrum rows
integer-owner incidence -> support-owner incidence
support -> parity route
```

Each map must be marked as one of:

```text
BIJECTION
INJECTION
SURJECTION
LOSSY PROJECTION
PARTIAL MAP
TYPED EQUIVALENCE
```

The classification must state all retained labels. A map may be lossless only relative to a fixed base or typed fiber.

## Alias audit

The following pairs must be tested as possible aliases rather than retained as separate primitives:

```text
centered gap / centered radius
prime-pair fiber / fixed-base spectrum
owner graph / incidence matrix
support owner / support projection
static component / connected component
```

## Required artifact

```text
research/pvg-space-deepening/engine-006-minimal-ontology.md
```

The artifact must contain:

- primitive objects;
- derived objects;
- aliases removed;
- maps and their types;
- dependency diagram in text form;
- minimality witnesses;
- information-retention ledger;
- unresolved ontology questions.

## Prohibitions

```text
new arithmetic experiment = false
new finite count = false
new dataset = false
cap/support expansion = false
weighting/asymptotics = false
classifier work = false
new theorem target = false
novelty promotion = false
Phase D = false
```

## Stop and return rule

Stop after the ontology artifact is complete. Return to ENGINE-006 parent review. WP-3 is not authorized automatically.

## Scientific classification

```text
definitions and typed maps = IDENTITY
proved recoverability/minimality consequences = PROVED
terminological choices = INTERPRETATION
independent-theory status = OPEN
```

No original theorem, publication-readiness, Goldbach, PNT, RH, or GRH claim is authorized.