# ENGINE-004 PASS-004 — Support-Conditioned Incidence Diagnostics Readiness

```text
Task ID: ENGINE-004-PASS-004-SUPPORT-CONDITIONED-INCIDENCE-DIAGNOSTICS
Parent review: ENGINE-004-PARENT-REVIEW-AFTER-PASS-003-001
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Parent program: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Decision: READY
Status: ACTIVE_CURRENT_SUBPASS
Date: 2026-07-23
Phase D: NOT AUTHORIZED
```

## Research question

Inside the unchanged frozen box, does support information retain any finite diagnostic separation in prime-fiber and centered-radius incidence profiles after deterministic conditioning on integer size and parity route?

This is not a causal question and does not presuppose a positive result.

## Frozen domain

```text
support prime limit = 11
support face sizes = 1,2,3
integer cap = 100000
support faces = 25
integer points = 884
represented points = 745
```

No expansion is permitted.

## Preregistered strata

The production implementation must use exactly these size controls:

```text
decimal bins:
[1,9], [10,99], [100,999], [1000,9999], [10000,99999], [100000,100000]

bit-length strata:
floor(log2 N)+1

parity routes:
even, odd
```

Every conditioned table must identify the stratum definition and cell count. Empty and singleton cells must be retained, not silently dropped.

## Preregistered observables

For every point N, record:

```text
N
support face
support size omega(N)
parity route
decimal bin
bit length
represented flag
multiplicity |D(N)|
min D(N), max D(N), span D(N) when nonempty
shared-coordinate count in D(N)
PASS-003 component identifier
```

## Required exact outputs

1. complete point-level deterministic records;
2. unconditioned profiles by support size and exact support face;
3. parity-conditioned profiles;
4. decimal-bin-and-parity-conditioned profiles;
5. bit-length-and-parity-conditioned profiles;
6. exact counts, sums, minima, maxima, medians, and rational means;
7. represented-rate ratios as exact numerator/denominator pairs;
8. within-stratum support-size rank tables, allowing ties;
9. inventory of rank reversals between raw and conditioned tables;
10. matched-neighborhood witnesses using the deterministic rule below;
11. mandatory counterexample witnesses;
12. independent reconstruction mismatch count;
13. deterministic SHA-256 certificate;
14. claim-ceiling flags.

## Deterministic matched-neighborhood rule

For a point N and a different support size, candidate controls are points M satisfying:

```text
same parity route
same decimal bin
minimum absolute distance |M-N|
```

Retain all tied nearest candidates. This is a finite diagnostic neighborhood, not statistical matching and not a causal estimator.

## Mandatory counterexample search

Search and emit explicit witnesses for:

```text
same exact support face, different multiplicity
same support size, different multiplicity
same parity and decimal bin, different support sizes but equal multiplicity
same parity and decimal bin, same support size but different incidence component when present
raw support-size multiplicity ranking reversed in at least one conditioned stratum, or certify none found
```

## Required separation

```text
association != causation
conditioning != proof of independence
same support != same exponent vector
same size bin != same integer magnitude
same multiplicity != same spectrum
same component != same fiber
finite rank reversal != asymptotic Simpson law
```

## Verification design

Production route:

- reuse certified registered points, spectra, and PASS-003 incidence indexes;
- construct deterministic point records and grouped tables;
- serialize exact rational quantities as numerator/denominator objects.

Independent route:

- rebuild each point from the integer-fiber registry;
- recompute support, parity, size strata, prime pairs, governed coordinates, and component membership without calling the production table builder;
- compare every point record and aggregate.

Required tests:

```text
all 884 points represented exactly once
all 25 support faces present
support sizes exactly 1,2,3
all 218024 coordinate occurrences preserved
all rational summaries exact
empty/singleton strata retained
matched-neighborhood tie handling deterministic
counterexample witnesses validate directly
independent mismatch count = 0
claim ceiling = PASS
```

## Required artifacts

```text
tools/pvg_support_conditioned_incidence.py
tests/test_pvg_support_conditioned_incidence.py
research/pvg-space-deepening/engine-004-pass-004-support-conditioned-incidence.md
research/pvg-space-deepening/data/support-conditioned-incidence-summary.json
.github/workflows/pvg-support-conditioned-incidence-audit.yml
governance/checkpoints/ENGINE-004-PASS-004-SUPPORT-CONDITIONED-INCIDENCE-001.md
```

The checkpoint file must not be created until local or CI verification succeeds.

## Stop rule

Stop and return to ENGINE-004 parent review when the finite certificate is complete, or immediately if a mismatch reveals a defect in PASS-001 through PASS-003. Do not open PASS-005 automatically.

## Claim ceiling

```text
historical originality = false
original lemma/theorem = false
causal support effect = false
general support law = open
asymptotic claim = false
Phase D authorized = false
Goldbach progress = false
PNT progress = false
RH progress = false
GRH progress = false
publication readiness = false
```

**Honest classification:** ready for exact finite support-conditioned diagnostics only.