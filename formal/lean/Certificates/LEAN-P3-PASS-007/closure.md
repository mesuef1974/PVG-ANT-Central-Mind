# LEAN-P3-PASS-007 Closure Certificate

Status: CLOSED / CLEAN / REPRODUCIBLE

Parent HEAD: 68236336e999aa37f9254503dbde92f08614ba1b

## Kernel-checked results

### PROOF-PVG-SUPPORT-CARDINALITY-001

Declaration:

PVGLEAN.pvg_factorization_support_card_eq_primeFactors_card

Statement:

card(support(factorization(n)))
= card(primeFactors(n))

Hypotheses:

None.

### PROOF-PVG-ACTIVE-COORDINATE-COUNT-001

Declaration:

PVGLEAN.pvg_active_coordinate_count_eq_primeFactors_card

Statement:

activeCoordinateCount(n)
= card(primeFactors(n))

Hypotheses:

None.

## Definition

PVGLEAN.activeCoordinateCount(n)
:= card(support(factorization(n))).

## Mathlib foundation

- Nat.support_factorization

## Discovery discipline

- direct Lean #check: PASS
- regex theorem discovery: NOT USED
- namespace guessing: NOT USED

## Verification gates

- individual module check: PASS
- full lake build: SUCCESS
- Lean/build warnings: 0
- project-owned sorry/admit: 0
- axiom audit: SAVED
- tag created: NO
- push performed: NO

## PVG interpretation

The dimension of the active valuation support is the number of distinct
prime directions occurring in the integer:

card(supp(nu(n))) = card(primeFactors(n)).

This is the PVG version of the distinct-prime-factor count.

## Classification

P3 / kernel-checked / Mathlib-backed / support-cardinality geometry.
