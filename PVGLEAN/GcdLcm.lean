import Mathlib.Data.Nat.Factorization.Basic

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