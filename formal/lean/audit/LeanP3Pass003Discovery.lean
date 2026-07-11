import Mathlib

/-!
# LEAN-P3-PASS-003 Mathlib Discovery

Locally discovered multiplication and factorization declarations.
-/

#check Nat.exponent_eq_exponent_mul_factorization_of_prime_pow_eq_base_pow
#check @Nat.exponent_eq_exponent_mul_factorization_of_prime_pow_eq_base_pow

#check Nat.factorization_eq_primeFactorsList_multiset
#check @Nat.factorization_eq_primeFactorsList_multiset

#check Nat.factorization_le_factorization_mul_left
#check @Nat.factorization_le_factorization_mul_left

#check Nat.factorization_le_factorization_mul_right
#check @Nat.factorization_le_factorization_mul_right

#check Nat.factorization_mul
#check @Nat.factorization_mul

#check Nat.factorization_mul_apply_of_coprime
#check @Nat.factorization_mul_apply_of_coprime

#check Nat.factorization_mul_of_coprime
#check @Nat.factorization_mul_of_coprime

#check Nat.factorizationLCMLeft_mul_factorizationLCMRight
#check @Nat.factorizationLCMLeft_mul_factorizationLCMRight

#check Nat.multiplicative_factorization
#check @Nat.multiplicative_factorization

#check Nat.multiplicative_factorization'
#check @Nat.multiplicative_factorization'

#check Nat.multiplicity_eq_factorization
#check @Nat.multiplicity_eq_factorization

-- Verify coordinatewise evaluation of Finsupp addition
example (f g : ℕ →₀ ℕ) (p : ℕ) : (f + g) p = f p + g p := by
  rfl
