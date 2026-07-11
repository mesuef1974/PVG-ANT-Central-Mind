/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# Powers in Prime-Valuation Geometry

This module records kernel-checked power laws for natural-number
factorization.

For all natural numbers `a` and `k`, exponentiation becomes scalar
multiplication of the factorization vector:

`factorization (a ^ k) = k • factorization a`.

At each coordinate `p`, this becomes:

`νₚ(a ^ k) = k * νₚ(a)`.

Unlike the product law, no nonzero hypothesis on `a` is required by the
installed Mathlib theorem.
-/

namespace PVGLEAN

/--
`PROOF-PVG-POWER-FACTORIZATION-001`

Factorization sends natural-number exponentiation to natural scalar
multiplication of factorization vectors.
-/
theorem pvg_factorization_pow
    (a k : ℕ) :
    (a ^ k).factorization =
      k • a.factorization :=
  Nat.factorization_pow a k

/--
`PROOF-PVG-POWER-VALUATION-001`

At every natural-number coordinate, the factorization coordinate of a power
is the exponent multiplied by the original coordinate.
-/
theorem pvg_valuation_pow_eq_mul
    (a k p : ℕ) :
    (a ^ k).factorization p =
      k * a.factorization p := by
  simp [Nat.factorization_pow]

/--
`PROOF-PVG-PRIME-POWER-FACTORIZATION-001`

A prime power has a factorization vector supported only at its prime base,
with coordinate equal to the exponent.
-/
theorem pvg_prime_factorization_pow
    {p k : ℕ}
    (hp : Nat.Prime p) :
    (p ^ k).factorization =
      Finsupp.single p k :=
  hp.factorization_pow

end PVGLEAN
