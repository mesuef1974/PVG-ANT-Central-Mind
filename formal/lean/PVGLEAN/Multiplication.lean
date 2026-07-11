/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# Multiplication in Prime-Valuation Geometry

This module records the kernel-checked multiplicative law for natural-number
factorization.

For nonzero natural numbers `a` and `b`, multiplication of integers becomes
addition of their factorization vectors:

`factorization (a * b) = factorization a + factorization b`.

Evaluating at any natural-number coordinate `p` gives the corresponding
prime-valuation geometry law:

`νₚ(a * b) = νₚ(a) + νₚ(b)`.

No primality hypothesis on `p` is required because factorization vanishes at
non-prime coordinates.
-/

namespace PVGLEAN

/--
`PROOF-PVG-MULTIPLICATIVE-FACTORIZATION-001`

For nonzero natural numbers, factorization sends multiplication to
coordinatewise addition.
-/
theorem pvg_factorization_mul
    {a b : ℕ}
    (ha : a ≠ 0)
    (hb : b ≠ 0) :
    (a * b).factorization =
      a.factorization + b.factorization :=
  Nat.factorization_mul ha hb

/--
`PROOF-PVG-MULTIPLICATIVE-VALUATION-001`

For nonzero natural numbers, every factorization coordinate of a product is
the sum of the corresponding coordinates.
-/
theorem pvg_valuation_mul_eq_add
    {a b p : ℕ}
    (ha : a ≠ 0)
    (hb : b ≠ 0) :
    (a * b).factorization p =
      a.factorization p + b.factorization p := by
  have h :=
    congrArg
      (fun f : ℕ →₀ ℕ => f p)
      (Nat.factorization_mul ha hb)
  simpa using h

end PVGLEAN
