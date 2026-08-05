#!/usr/bin/env python3

import unittest
from fractions import Fraction

from tools.pvg_arithmetic_terrain import (
    analyze_transfer,
    arithmetic_values,
    transfer,
)
from tools.pvg_inverse_geometry import GeometryInputError


class PVGArithmeticTerrainTests(unittest.TestCase):
    def test_interior_transfer(self) -> None:
        r = analyze_transfer({2: 2, 3: 1, 5: 1}, 2, 3)
        self.assertEqual(r["before"]["n"], 60)
        self.assertEqual(r["after"]["n"], 90)
        self.assertEqual(r["move"]["position_class"], "interior_transfer")
        self.assertEqual(r["ratios"]["n"]["text"], "3/2")
        self.assertEqual(r["ratios"]["tau"]["text"], "1/1")
        self.assertTrue(all(r["verification"].values()))

    def test_boundary_contraction(self) -> None:
        r = analyze_transfer({2: 1, 3: 2, 5: 1}, 2, 3)
        self.assertEqual(r["move"]["position_class"], "boundary_contraction")
        self.assertEqual(r["delta"]["omega"], -1)
        self.assertEqual(r["ratios"]["phi"]["text"], "3/1")

    def test_boundary_expansion(self) -> None:
        r = analyze_transfer({2: 3, 3: 1}, 2, 5)
        self.assertEqual(r["move"]["position_class"], "boundary_expansion")
        self.assertEqual(r["delta"]["omega"], 1)
        self.assertEqual(r["ratios"]["phi"]["text"], "2/1")

    def test_support_swap(self) -> None:
        r = analyze_transfer({2: 1, 3: 1}, 2, 5)
        self.assertEqual(r["move"]["position_class"], "support_swap")
        self.assertEqual(r["delta"]["omega"], 0)
        self.assertEqual(r["before"]["mu"], 1)
        self.assertEqual(r["after"]["mu"], 1)

    def test_liouville_is_level_constant(self) -> None:
        for f, donor, recipient in [
            ({2: 3, 3: 2}, 2, 3),
            ({2: 1, 3: 1}, 2, 5),
            ({3: 4}, 3, 7),
        ]:
            r = analyze_transfer(f, donor, recipient)
            self.assertEqual(r["before"]["lambda"], r["after"]["lambda"])
            self.assertEqual(r["before"]["Omega"], r["after"]["Omega"])

    def test_tau_ratio_formula(self) -> None:
        r = analyze_transfer({2: 4, 3: 2}, 2, 3)
        expected = Fraction(4, 5) * Fraction(4, 3)
        self.assertEqual(r["ratios"]["tau"]["text"], f"{expected.numerator}/{expected.denominator}")

    def test_sigma_exact_values(self) -> None:
        r = analyze_transfer({2: 2, 3: 1}, 2, 3)
        self.assertEqual(r["before"]["sigma"], 28)
        self.assertEqual(r["after"]["sigma"], 39)
        self.assertEqual(r["ratios"]["sigma"]["text"], "39/28")

    def test_mobius_boundary_behavior(self) -> None:
        r = analyze_transfer({2: 2, 3: 1}, 2, 5)
        self.assertEqual(r["before"]["mu"], 0)
        self.assertEqual(r["after"]["mu"], -1)
        self.assertFalse(r["ratios"].get("mu", {"defined": False})["defined"])

    def test_arithmetic_values_at_one(self) -> None:
        self.assertEqual(
            arithmetic_values({}),
            {"n": 1, "omega": 0, "Omega": 0, "tau": 1, "sigma": 1, "phi": 1, "mu": 1, "lambda": 1, "radical": 1},
        )

    def test_invalid_transfer(self) -> None:
        with self.assertRaises(GeometryInputError):
            transfer({2: 1, 3: 1}, 5, 3)
        with self.assertRaises(GeometryInputError):
            transfer({2: 1, 3: 1}, 2, 2)


if __name__ == "__main__":
    unittest.main()
