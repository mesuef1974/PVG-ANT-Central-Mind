# LEAN-P3-PASS-002 Closure Certificate

Status: CLOSED

Parent HEAD: 67d4533fb535bb7bdee7e1b13fd31716de6a4ace

## Kernel-checked results

- PROOF-PVG-GCD-VALUATION-001
  - theorem: PVGLEAN.pvg_valuation_gcd_eq_min
  - statement:
    factorization(gcd(a,b))(p)
    = min(factorization(a)(p), factorization(b)(p))
  - hypotheses: a != 0, b != 0

- PROOF-PVG-LCM-VALUATION-001
  - theorem: PVGLEAN.pvg_valuation_lcm_eq_max
  - statement:
    factorization(lcm(a,b))(p)
    = max(factorization(a)(p), factorization(b)(p))
  - hypotheses: a != 0, b != 0

## Gates

- local Mathlib source discovery: PASS
- exact signature check: PASS
- module check: PASS
- lake build: SUCCESS
- project-owned sorry/admit: 0
- axiom audit: SAVED
- build log: SAVED
- tag created: NO
- push performed: NO

## Classification

P3 / kernel-checked / Mathlib-backed.

The exact axiom dependencies are recorded in:
certificates/LEAN-P3-PASS-002/axiom-audit.log