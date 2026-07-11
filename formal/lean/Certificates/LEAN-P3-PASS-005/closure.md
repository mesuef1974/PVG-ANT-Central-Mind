# LEAN-P3-PASS-005 Closure Certificate

Status: CLOSED / CLEAN / REPRODUCIBLE

Parent HEAD: 90fca92eebb7bb1e6b56bc83b3032820c9b8f73c

## Kernel-checked results

### PROOF-PVG-DIVISION-FACTORIZATION-001

Declaration:

PVGLEAN.pvg_factorization_div

Statement:

factorization(n / d)
= factorization(n) - factorization(d)

Hypothesis:

d divides n.

### PROOF-PVG-DIVISION-VALUATION-001

Declaration:

PVGLEAN.pvg_valuation_div_eq_sub

Statement:

factorization(n / d)(p)
= factorization(n)(p) - factorization(d)(p)

Hypothesis:

d divides n.

### PROOF-PVG-DIVISIBILITY-DIVISION-CERTIFICATE-001

Declaration:

PVGLEAN.pvg_dvd_iff_factorization_div_eq_sub

Statement:

d divides n if and only if

factorization(n / d)
= factorization(n) - factorization(d).

Hypotheses:

- d != 0
- d <= n

## Mathlib foundation

- Nat.factorization_div
- Nat.dvd_iff_div_factorization_eq_tsub
- Nat.factorization_le_iff_dvd
- Nat.factorization_mul

## Verification gates

- corrected local signature discovery: PASS
- individual module check: PASS
- full lake build: SUCCESS
- Lean/build warnings: 0
- project-owned sorry/admit: 0
- axiom audit: SAVED
- build log: SAVED
- source-search evidence: SAVED
- tag created: NO
- push performed: NO

## PVG interpretation

A certified divisibility step becomes vector subtraction:

nu(n / d) = nu(n) - nu(d).

Coordinatewise:

nu_p(n / d) = nu_p(n) - nu_p(d).

The subtraction is natural-number truncated subtraction, but under
d divides n the valuation-vector order guarantees exactness.

## Classification

P3 / kernel-checked / Mathlib-backed / PVG division law.
