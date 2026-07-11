/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# Division in Prime-Valuation Geometry

Under a divisibility certificate `d ∣ n`, natural-number division becomes
coordinatewise truncated subtraction in factorization space:

`factorization (n / d) = factorization n - factorization d`.

The coordinate form is:

`νₚ(n / d) = νₚ(n) - νₚ(d)`.

A converse certificate is also recorded under `d ≠ 0` and `d ≤ n`.
-/

namespace PVGLEAN

/--
`PROOF-PVG-DIVISION-FACTORIZATION-001`

Division by a certified divisor becomes subtraction of factorization vectors.
-/
theorem pvg_factorization_div
    {d n : ℕ}
    (h : d ∣ n) :
    (n / d).factorization =
      n.factorization - d.factorization :=
  Nat.factorization_div h

/--
`PROOF-PVG-DIVISION-VALUATION-001`

At every coordinate, division by a certified divisor becomes subtraction of
the corresponding factorization coordinates.
-/
theorem pvg_valuation_div_eq_sub
    {d n p : ℕ}
    (h : d ∣ n) :
    (n / d).factorization p =
      n.factorization p - d.factorization p := by
  rw [Nat.factorization_div h]
  rfl

/--
`PROOF-PVG-DIVISIBILITY-DIVISION-CERTIFICATE-001`

For nonzero `d` with `d ≤ n`, divisibility is equivalent to the exact
factorization-vector subtraction law for `n / d`.
-/
theorem pvg_dvd_iff_factorization_div_eq_sub
    {d n : ℕ}
    (hd : d ≠ 0)
    (hdn : d ≤ n) :
    d ∣ n ↔
      (n / d).factorization =
        n.factorization - d.factorization :=
  Nat.dvd_iff_div_factorization_eq_tsub hd hdn

end PVGLEAN
