# RMG-002-B — Dirichlet Convolution Lean Candidate Pack

Status: candidate pack only / no L6 promotion

## Purpose

This file identifies exact finite algebraic statements suitable for future Lean formalization. It is not a proof certificate and does not claim that these theorems are already formalized in the project.

## Existing formal dependency

The current Lean layer supplies project-owned valuation infrastructure, including multiplication-to-valuation addition, support geometry, cardinality, mass, and division laws. Those results support the intended PVG encoding, but they do not by themselves formalize arithmetic functions or Dirichlet convolution.

## Candidate theorem sequence

1. `dirichletConvolution_apply`
   - encode `(f * g)(n) = sum_{d | n} f d * g (n / d)` under the selected Mathlib representation.

2. `dirichletConvolution_comm`
   - prove commutativity by the involution `d ↦ n/d` on divisors.

3. `dirichletConvolution_assoc`
   - prove associativity by finite reindexing of triples `abc=n`.

4. `dirichletConvolution_epsilon_left` and `dirichletConvolution_epsilon_right`
   - certify the convolution identity.

5. `mobius_convolution_one`
   - certify `mu * 1 = epsilon` using the divisor-sum identity for Möbius.

6. `one_convolution_one_eq_tau`
   - certify divisor-counting interpretation.

7. `totient_convolution_one_eq_id`
   - certify `phi * 1 = id`.

8. `vonMangoldt_convolution_one_eq_log`
   - certify `Lambda * 1 = log`.

9. `multiplicative_dirichletConvolution`
   - prove closure of multiplicative functions under convolution.

10. `not_completelyMultiplicative_tau`
    - formal counterexample from `tau(4)=3` and `tau(2)^2=4`.

11. `divisorBox_equiv_divisors`
    - for `v=nu(n)`, construct the equivalence between divisors `d|n` and vectors `u` with `0<=u<=v`.

12. `dirichletConvolution_eq_boxConvolution`
    - prove the ANT-to-PVG transport through the divisor-box equivalence.

## Dependency order

```text
valuation round trip
→ divisor / coordinatewise-order equivalence
→ divisor-box finite equivalence
→ box-convolution identity
→ algebraic laws
→ named arithmetic-function identities
→ multiplicativity closure
```

## Promotion gate

No statement in this pack receives `L6_FORMALLY_VERIFIED` until all of the following exist:

- a committed Lean source file;
- successful `lake build` or narrower certified build;
- zero project-owned `sorry`/`admit` for the claimed theorem;
- a committed verification receipt naming the exact theorem and commit.

Current state:

```text
LEAN_CANDIDATES = 12
PROJECT_OWNED_PROOFS_ADDED = 0
L6_PROMOTION = NOT AUTHORIZED
```
