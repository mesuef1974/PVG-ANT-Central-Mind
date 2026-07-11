/-
Copyright (c) 2026 PVG-ANT Central Mind. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Project
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# Prime-Valuation Divisibility Order

This file records the standard equivalence between divisibility of
nonzero natural numbers and coordinatewise order on their prime
factorization vectors.

Classification: known theorem and PVG reinterpretation.
-/

namespace PVGLean

/--
Divisibility of nonzero natural numbers is exactly coordinatewise
order on their prime-factorization vectors.
-/
theorem pvg_divisibility_order
    {a b : ℕ}
    (ha : a ≠ 0)
    (hb : b ≠ 0) :
    a ∣ b ↔ a.factorization ≤ b.factorization := by
  exact (Nat.factorization_le_iff_dvd ha hb).symm

/-- The same equivalence in the orientation used by Mathlib. -/
theorem factorization_order_iff_dvd
    {a b : ℕ}
    (ha : a ≠ 0)
    (hb : b ≠ 0) :
    a.factorization ≤ b.factorization ↔ a ∣ b := by
  exact Nat.factorization_le_iff_dvd ha hb

end PVGLean
