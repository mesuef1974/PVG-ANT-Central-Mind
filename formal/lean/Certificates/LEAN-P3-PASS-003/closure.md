# LEAN-P3-PASS-003 Closure Certificate

Status: CLOSED / CLEAN / REPRODUCIBLE

Parent HEAD: 6ac6a34d1316943c9c4c8fb02575ca43fecd1acb

## Kernel-checked results

### PROOF-PVG-MULTIPLICATIVE-FACTORIZATION-001

Lean declaration:

PVGLEAN.pvg_factorization_mul

Statement:

factorization(a * b)
= factorization(a) + factorization(b)

Hypotheses:

- a != 0
- b != 0

### PROOF-PVG-MULTIPLICATIVE-VALUATION-001

Lean declaration:

PVGLEAN.pvg_valuation_mul_eq_add

Statement:

factorization(a * b)(p)
= factorization(a)(p) + factorization(b)(p)

Hypotheses:

- a != 0
- b != 0

No primality hypothesis on p is required.

## Mathlib foundation

The installed local declaration used is:

Nat.factorization_mul

Exact signature:

Nat.factorization_mul {a b : Nat}
  (ha : a != 0)
  (hb : b != 0) :
  (a * b).factorization
    = a.factorization + b.factorization

## Verification gates

- local Mathlib source discovery: PASS
- exact signature discovery: PASS
- individual module check: PASS
- full lake build: SUCCESS
- Lean/build warnings: 0
- project-owned sorry/admit: 0
- axiom audit: SAVED
- build log: SAVED
- discovery evidence: SAVED
- tag created: NO
- push performed: NO

## Axiom profile

The exact axiom output is stored in:

Certificates/LEAN-P3-PASS-003/axiom-audit.log

## PVG interpretation

Multiplication of nonzero natural numbers becomes vector addition in
prime-valuation coordinates:

nu(a * b) = nu(a) + nu(b).

## Classification

P3 / kernel-checked / Mathlib-backed / multiplicative PVG law.
