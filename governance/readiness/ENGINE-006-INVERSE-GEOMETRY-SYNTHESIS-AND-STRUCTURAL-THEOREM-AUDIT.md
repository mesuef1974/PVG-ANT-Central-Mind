# ENGINE-006 — Inverse-Geometry Synthesis and Structural Theorem Audit

```text
Task ID: ENGINE-006-INVERSE-GEOMETRY-SYNTHESIS-AND-STRUCTURAL-THEOREM-AUDIT
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Basis: GOAL-PVG-INVERSE-GEOMETRY-POST-ENGINE-004-SUCCESSOR-REVIEW-001
Decision: READY
Status: ACTIVE_CURRENT
Date: 2026-07-23
Experimental expansion: NOT AUTHORIZED
Phase D: NOT AUTHORIZED
```

## Governing question

What, after removing elementary identities, finite-box artifacts, duplicated terminology, and unsupported interpretation, is the smallest mathematically durable structure contributed by the completed inverse-geometry program?

## Input boundary

The primary governed inputs are the admitted ENGINE-004 chain:

```text
PASS-001 centered-gap prime fibers
PASS-002 centered-radius spectra
PASS-003 centered-radius incidence
PASS-004 support-conditioned incidence diagnostics
ENGINE-004 Phase-C final closure review
```

Earlier Phase-A and Phase-B definitions may be used only where necessary to trace dependencies.

## Work packages

### WP-1 — Claim inventory

Create a complete ledger with one row per material claim:

```text
claim id
source artifact
object
statement
classification
proof/certificate basis
standard antecedent
information added
information lost
scope ceiling
```

### WP-2 — Minimal ontology

Determine the smallest nonredundant object set needed to recover the ENGINE-004 language, including at minimum:

```text
valuation vector
support face
integer owner
prime-pair fiber
centered gap/radius
spectrum
incidence owner relation
support projection
route class
```

Every additional term must be justified by a distinct mathematical role.

### WP-3 — Reconstruction and loss audit

Verify precisely which maps are lossless and which are not, including:

```text
pair -> integer
integer -> support
support -> parity route
(N, D(N)) -> prime-pair fiber
D(N) without N
incidence projection and co-occurrence summaries
```

### WP-4 — Standard-structure comparison

Compare the framework against established structures without claiming novelty:

```text
finite-support valuation vectors
free commutative monoid on primes
divisor lattice / coordinatewise order
support stratification
additive prime-pair parametrization
bipartite incidence structures
```

The output must distinguish equivalence, specialization, reinterpretation, and genuinely unresolved comparison.

### WP-5 — Structural proposition audit

Candidate propositions must be classified separately by:

```text
truth status
proof status
finite verification status
known-prior-art status
PVG usefulness
novelty status
```

No proposition may be called new merely because it has a new geometric phrasing.

### WP-6 — Research-value decision

Rank possible successors and choose no more than one:

```text
ADVANCE_ONE_QUESTION
REVISE_FRAMEWORK
STOP_AND_ARCHIVE
```

## Required artifacts

```text
research/pvg-space-deepening/engine-006-synthesis-ledger.md
research/pvg-space-deepening/engine-006-minimal-ontology.md
research/pvg-space-deepening/engine-006-reconstruction-loss-map.md
research/pvg-space-deepening/engine-006-standard-structure-comparison.md
research/pvg-space-deepening/engine-006-structural-proposition-audit.md
governance/reviews/ENGINE-006-FINAL-RESEARCH-VALUE-REVIEW-001.md
```

A machine-readable ledger may be added only if it records the same reviewed claims; it must not become a new experimental dataset.

## Stop conditions

Stop and return to the parent goal if:

1. all candidate structure reduces to standard identities plus finite visualization;
2. candidate propositions lack a clear theorem statement;
3. novelty cannot be separated from terminology;
4. a proposed next question requires unauthorized expansion;
5. the framework adds no recoverability, compression, obstruction, or proof advantage.

## Scientific classification

```text
standard valuation identities = IDENTITY / KNOWN
proved consequences = PROVED
complete-box observations = FINITE-VERIFIED
geometric language = INTERPRETATION unless stronger status is established
novelty = OPEN until prior-art audit
new theory = NOT ESTABLISHED
```

## Prohibitions

```text
new numerical experiments = false
cap expansion = false
support expansion = false
weighting/asymptotics = false
classifier training = false
Phase D = false
Goldbach progress = false
PNT progress = false
RH/GRH progress = false
publication readiness = false
```

## Active-state rule

ENGINE-006 is the only active governed engine. ENGINE-005 and Local Obstruction Geometry remain inactive candidates. No subpass beyond the synthesis work packages is authorized automatically.
