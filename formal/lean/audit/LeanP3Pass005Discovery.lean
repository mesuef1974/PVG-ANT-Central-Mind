/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# LEAN-P3-PASS-005 Mathlib Discovery

Exact local signatures for division in natural-number factorization.
-/

#check Nat.factorization_div
#check @Nat.factorization_div

#check Nat.dvd_iff_div_factorization_eq_tsub
#check @Nat.dvd_iff_div_factorization_eq_tsub

#check Nat.factorization_le_iff_dvd
#check @Nat.factorization_le_iff_dvd

#check Nat.factorization_mul
#check @Nat.factorization_mul

example (f g : ℕ →₀ ℕ) (p : ℕ) :
    (f - g) p = f p - g p := by
  rfl
