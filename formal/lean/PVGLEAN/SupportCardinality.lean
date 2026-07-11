/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# Support Cardinality in Prime-Valuation Geometry

The number of active coordinates of the factorization vector of `n` is
exactly the number of distinct prime factors of `n`.

This is the support-cardinality layer of prime-valuation geometry.
-/

namespace PVGLEAN

/--
The number of active prime-valuation coordinates of a natural number.
-/
def activeCoordinateCount (n : ℕ) : ℕ :=
  n.factorization.support.card

/--
`PROOF-PVG-SUPPORT-CARDINALITY-001`

The cardinality of the factorization support equals the cardinality of the
finite set of prime factors.
-/
theorem pvg_factorization_support_card_eq_primeFactors_card
    (n : ℕ) :
    n.factorization.support.card =
      n.primeFactors.card := by
  rw [Nat.support_factorization]

/--
`PROOF-PVG-ACTIVE-COORDINATE-COUNT-001`

The PVG active-coordinate count is exactly the number of distinct prime
factors.
-/
theorem pvg_active_coordinate_count_eq_primeFactors_card
    (n : ℕ) :
    activeCoordinateCount n =
      n.primeFactors.card := by
  unfold activeCoordinateCount
  rw [Nat.support_factorization]

end PVGLEAN
