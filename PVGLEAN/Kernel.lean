/-
Copyright (c) 2026 PVG-ANT Central Mind. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: PVG-ANT Central Mind Project
-/
import Mathlib

/-!
# Kernel-Checked Basic Proofs

Small foundational proofs used to establish the first Lean P3 checkpoint.
-/

namespace PVGLean

/-- Composition of implications. -/
theorem logic_composition
    (P Q R : Prop) :
    (P → Q) → (Q → R) → P → R := by
  intro hPQ hQR hP
  exact hQR (hPQ hP)

/-- Transitivity of equality on natural numbers. -/
theorem equality_transitivity
    (a b c : ℕ)
    (hab : a = b)
    (hbc : b = c) :
    a = c := by
  exact hab.trans hbc

/-- A minimal arithmetic kernel certificate. -/
theorem one_plus_one : 1 + 1 = 2 := by
  rfl

end PVGLean
