/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# LEAN-P3-PASS-004 Mathlib Discovery

Local signature discovery for natural-number factorization of powers.
-/

#check Nat.factorization_pow
#check @Nat.factorization_pow

#check Nat.Prime.factorization_pow
#check @Nat.Prime.factorization_pow

#check Finsupp.smul_apply

example (n : ℕ) (f : ℕ →₀ ℕ) (p : ℕ) :
    (n • f) p = n • f p := by
  rfl
