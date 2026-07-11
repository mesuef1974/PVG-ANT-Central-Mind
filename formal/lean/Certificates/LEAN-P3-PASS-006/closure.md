# LEAN-P3-PASS-006 Closure Certificate

Status: CLOSED / CLEAN / REPRODUCIBLE

Parent HEAD: 1ee612d3f1a642a6b0f2fabbe6ff358ecea002e3

## Kernel-checked results

### PROOF-PVG-SUPPORT-FACTORIZATION-001

Declaration:

PVGLEAN.pvg_support_factorization

Statement:

support(factorization(n)) = primeFactors(n)

Hypotheses:

None.

### PROOF-PVG-SUPPORT-MEMBERSHIP-001

Declaration:

PVGLEAN.pvg_mem_factorization_support_iff

Statement:

p belongs to support(factorization(n))
if and only if factorization(n)(p) != 0.

Hypotheses:

None.

### PROOF-PVG-PRIME-FACTOR-MEMBERSHIP-001

Declaration:

PVGLEAN.pvg_mem_primeFactors_iff_valuation_ne_zero

Statement:

p belongs to primeFactors(n)
if and only if factorization(n)(p) != 0.

Hypotheses:

None.

## Mathlib foundation

- Nat.support_factorization
- Finsupp.mem_support_iff

## Discovery discipline

- Lean direct #check: PASS
- regex theorem discovery: NOT USED
- namespace guessing: NOT USED
- source text parsing as a blocking gate: NOT USED

## Verification gates

- individual module check: PASS
- full lake build: SUCCESS
- Lean/build warnings: 0
- project-owned sorry/admit: 0
- axiom audit: SAVED
- tag created: NO
- push performed: NO

## PVG interpretation

The active coordinates of the valuation vector are exactly the prime
directions dividing the integer:

supp(nu(n)) = primeFactors(n).

Equivalently:

p is an active coordinate of nu(n)
if and only if nu_p(n) != 0.

## Classification

P3 / kernel-checked / Mathlib-backed / PVG support geometry.
