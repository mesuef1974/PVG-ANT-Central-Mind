/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# GCD and LCM in Prime-Valuation Geometry

This module records kernel-checked coordinate formulas for greatest common
divisors and least common multiples under natural-number factorization.

For nonzero natural numbers `a` and `b`, the factorization vector of `gcd a b`
is the coordinatewise infimum of their factorization vectors, while the
factorization vector of `lcm a b` is their coordinatewise supremum.

Consequently, at every natural-number coordinate `p`:

* `νₚ(gcd(a,b)) = min(νₚ(a), νₚ(b))`
* `νₚ(lcm(a,b)) = max(νₚ(a), νₚ(b))`

The coordinate is not required to be prime: Mathlib's factorization function
vanishes automatically at non-prime coordinates.
-/

namespace PVGLEAN

/--
`PROOF-PVG-GCD-VALUATION-001`

For nonzero natural numbers, every factorization coordinate of the gcd
is the minimum of the corresponding coordinates.
-/
theorem pvg_valuation_gcd_eq_min
    {a b p : ℕ}
    (ha : a ≠ 0)
    (hb : b ≠ 0) :
    (a.gcd b).factorization p =
      Nat.min (a.factorization p) (b.factorization p) := by
  have h :
      (a.gcd b).factorization p =
        (a.factorization ⊓ b.factorization) p :=
    congrArg
      (fun f : ℕ →₀ ℕ => f p)
      (Nat.factorization_gcd ha hb)

  simpa using h

/--
`PROOF-PVG-LCM-VALUATION-001`

For nonzero natural numbers, every factorization coordinate of the lcm
is the maximum of the corresponding coordinates.
-/
theorem pvg_valuation_lcm_eq_max
    {a b p : ℕ}
    (ha : a ≠ 0)
    (hb : b ≠ 0) :
    (a.lcm b).factorization p =
      Nat.max (a.factorization p) (b.factorization p) := by
  have h :
      (a.lcm b).factorization p =
        (a.factorization ⊔ b.factorization) p :=
    congrArg
      (fun f : ℕ →₀ ℕ => f p)
      (Nat.factorization_lcm ha hb)

  simpa using h

end PVGLEAN
