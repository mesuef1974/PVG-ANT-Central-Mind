# LEAN-P3-PASS-002 Closure Certificate

Status: CLOSED / CLEAN / REPRODUCIBLE

Original proof commit: a5b1d48
Cleanup parent HEAD: a5b1d48086756b95faab40eb1776d519d9353acd

## Kernel-checked results

- PROOF-PVG-GCD-VALUATION-001
  - declaration: PVGLEAN.pvg_valuation_gcd_eq_min
  - source: PVGLEAN/GcdLcm.lean
  - statement:
    factorization(gcd(a,b))(p)
    = min(factorization(a)(p), factorization(b)(p))
  - hypotheses: a != 0, b != 0

- PROOF-PVG-LCM-VALUATION-001
  - declaration: PVGLEAN.pvg_valuation_lcm_eq_max
  - source: PVGLEAN/GcdLcm.lean
  - statement:
    factorization(lcm(a,b))(p)
    = max(factorization(a)(p), factorization(b)(p))
  - hypotheses: a != 0, b != 0

## Mathematical structure

The two results establish the coordinatewise lattice laws:

- factorization(gcd(a,b)) = factorization(a) inf factorization(b)
- factorization(lcm(a,b)) = factorization(a) sup factorization(b)

No primality hypothesis on the coordinate p is required.

## Verification gates

- installed Mathlib signature discovery: PASS
- individual module check: PASS
- full lake build: SUCCESS
- project-owned sorry/admit: 0
- axiom audit: SAVED
- honesty gate: SAVED
- build log: SAVED
- signature log: SAVED
- local source-search log: SAVED
- lint cleanup: PASS
- tag created: NO
- push performed: NO

## Axiom profile

Both declarations depend on the standard Mathlib/Lean axioms:

- propext
- Classical.choice
- Quot.sound

Exact output is stored in:

Certificates/LEAN-P3-PASS-002/axiom-audit.log

## Classification

P3 / kernel-checked / Mathlib-backed / reproducible.
