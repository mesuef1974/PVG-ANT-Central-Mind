/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib

/-!
# LEAN-P3-PASS-008 Direct Proof Discovery

Lean-checked bridge from total factorization mass to the length of the
prime-factor list.
-/

#check Nat.factorization_eq_primeFactorsList_multiset
#check @Nat.factorization_eq_primeFactorsList_multiset

#check Finsupp.card_toMultiset
#check @Finsupp.card_toMultiset

def valuationMassProbe (n : ℕ) : ℕ :=
  n.factorization.sum fun _ exponent => exponent

example (n : ℕ) :
    valuationMassProbe n =
      n.primeFactorsList.length := by
  unfold valuationMassProbe
  rw [Nat.factorization_eq_primeFactorsList_multiset]
  simpa [Function.id_def] using
    (Finsupp.card_toMultiset
      (Multiset.toFinsupp
        (n.primeFactorsList : Multiset ℕ))).symm
