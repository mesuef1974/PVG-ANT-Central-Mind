# LEAN-P3-PASS-004 Closure Certificate

Status: CLOSED / CLEAN / REPRODUCIBLE

Parent HEAD: 99ef1b4b34a09691c9318a69fad01baf36ab8694

## Kernel-checked results

### PROOF-PVG-POWER-FACTORIZATION-001

Declaration:

PVGLEAN.pvg_factorization_pow

Statement:

factorization(a ^ k) = k smul factorization(a)

Hypotheses:

None.

### PROOF-PVG-POWER-VALUATION-001

Declaration:

PVGLEAN.pvg_valuation_pow_eq_mul

Statement:

factorization(a ^ k)(p) = k * factorization(a)(p)

Hypotheses:

None.

### PROOF-PVG-PRIME-POWER-FACTORIZATION-001

Declaration:

PVGLEAN.pvg_prime_factorization_pow

Statement:

factorization(p ^ k) = Finsupp.single p k

Hypothesis:

p is prime.

## Mathlib foundation

- Nat.factorization_pow
- Nat.Prime.factorization_pow
- Finsupp.smul_apply

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

## PVG interpretation

Natural exponentiation becomes scalar dilation:

nu(a ^ k) = k nu(a).

Coordinatewise:

nu_p(a ^ k) = k nu_p(a).

For prime p:

nu(p ^ k) = k e_p.

## Classification

P3 / kernel-checked / Mathlib-backed / PVG power law.
