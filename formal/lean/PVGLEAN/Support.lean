/-
Copyright (c) 2026 PVG-ANT Central Mind Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Contributors
-/
import Mathlib.Data.Nat.Factorization.Basic

/-!
# Support Geometry in Prime-Valuation Space

The support of the factorization vector of a natural number is exactly its
finite set of prime factors.

Thus the active coordinates of `ν(n)` are precisely the prime directions
appearing in `n`.
-/

namespace PVGLEAN

/--
`PROOF-PVG-SUPPORT-FACTORIZATION-001`

The support of the factorization vector is exactly the set of prime factors.
-/
theorem pvg_support_factorization
    (n : ℕ) :
    n.factorization.support =
      n.primeFactors :=
  Nat.support_factorization n

/--
`PROOF-PVG-SUPPORT-MEMBERSHIP-001`

A coordinate belongs to the support exactly when its factorization value is
nonzero.
-/
theorem pvg_mem_factorization_support_iff
    {n p : ℕ} :
    p ∈ n.factorization.support ↔
      n.factorization p ≠ 0 :=
  Finsupp.mem_support_iff

/--
`PROOF-PVG-PRIME-FACTOR-MEMBERSHIP-001`

A natural-number coordinate belongs to the prime-factor set exactly when its
factorization coordinate is nonzero.
-/
theorem pvg_mem_primeFactors_iff_valuation_ne_zero
    {n p : ℕ} :
    p ∈ n.primeFactors ↔
      n.factorization p ≠ 0 := by
  rw [← Nat.support_factorization]
  exact Finsupp.mem_support_iff

end PVGLEAN
