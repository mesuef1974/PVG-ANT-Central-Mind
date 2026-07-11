/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib

/-!
# Valuation Mass in Prime-Valuation Geometry

The valuation mass of a natural number is the sum of all coordinates of its
factorization vector.

It equals the length of `primeFactorsList`, so it counts prime factors with
multiplicity.
-/

namespace PVGLEAN

/--
The total mass of the prime-valuation vector.
-/
def valuationMass (n : ℕ) : ℕ :=
  n.factorization.sum fun _ exponent => exponent

/--
`PROOF-PVG-FACTORIZATION-MASS-001`

The sum of all factorization coordinates equals the length of the
prime-factor list.
-/
theorem pvg_factorization_mass_eq_primeFactorsList_length
    (n : ℕ) :
    n.factorization.sum (fun _ exponent => exponent) =
      n.primeFactorsList.length := by
  rw [Nat.factorization_eq_primeFactorsList_multiset]
  simpa [Function.id_def] using
    (Finsupp.card_toMultiset
      (Multiset.toFinsupp
        (n.primeFactorsList : Multiset ℕ))).symm

/--
`PROOF-PVG-VALUATION-MASS-001`

The PVG valuation mass equals the number of prime factors counted with
multiplicity.
-/
theorem pvg_valuation_mass_eq_primeFactorsList_length
    (n : ℕ) :
    valuationMass n =
      n.primeFactorsList.length := by
  unfold valuationMass
  exact pvg_factorization_mass_eq_primeFactorsList_length n

end PVGLEAN
