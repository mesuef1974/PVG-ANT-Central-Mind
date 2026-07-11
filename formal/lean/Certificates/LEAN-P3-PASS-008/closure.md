# LEAN-P3-PASS-008 Closure Certificate

Status: CLOSED / CLEAN / REPRODUCIBLE

Parent HEAD: a0f93f46b01ba4743c2348e5ddbadf4522aed29a

## Definition

PVGLEAN.valuationMass(n)
:= sum over p of factorization(n)(p).

## Kernel-checked results

### PROOF-PVG-FACTORIZATION-MASS-001

Declaration:

PVGLEAN.pvg_factorization_mass_eq_primeFactorsList_length

Statement:

sum_p factorization(n)(p)
= length(primeFactorsList(n)).

Hypotheses:

None.

### PROOF-PVG-VALUATION-MASS-001

Declaration:

PVGLEAN.pvg_valuation_mass_eq_primeFactorsList_length

Statement:

valuationMass(n)
= length(primeFactorsList(n)).

Hypotheses:

None.

## Mathlib foundation

- Nat.factorization_eq_primeFactorsList_multiset
- Finsupp.card_toMultiset
- Multiset.toFinsupp

## Discovery discipline

- direct Lean proof probe: PASS
- regex theorem discovery: NOT USED
- namespace guessing: NOT USED
- Parent HEAD: recorded dynamically

## Verification gates

- individual module check: PASS
- full lake build: SUCCESS
- Lean/build warnings: 0
- project-owned sorry/admit: 0
- axiom audit: SAVED
- tag created: NO
- push performed: NO

## PVG interpretation

The total valuation mass equals the number of prime factors counted with
multiplicity:

sum_p nu_p(n)
= length(primeFactorsList(n)).

## Classification

P3 / kernel-checked / Mathlib-backed / valuation-mass geometry.
