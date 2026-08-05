#!/usr/bin/env python3
import unittest
from fractions import Fraction

from tools.pvg_level_terrain import analyze, parse_primes


class PVGLevelTerrainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = analyze([2, 3, 5], 6)

    def test_point_count(self) -> None:
        self.assertEqual(self.report["point_count"], 28)
        self.assertTrue(self.report["verification"]["point_count"])

    def test_shell_constants(self) -> None:
        self.assertTrue(self.report["verification"]["Omega_constant"])
        self.assertTrue(self.report["verification"]["lambda_constant"])

    def test_size_extrema_are_vertices(self) -> None:
        e = self.report["extrema"]["n"]
        self.assertEqual(e["minimum"], 64)
        self.assertEqual(e["minimum_points"], [[6, 0, 0]])
        self.assertEqual(e["maximum"], 15625)
        self.assertEqual(e["maximum_points"], [[0, 0, 6]])

    def test_tau_balanced_maximum(self) -> None:
        e = self.report["extrema"]["tau"]
        self.assertEqual(e["minimum"], 7)
        self.assertEqual(e["maximum"], 27)
        self.assertEqual(e["maximum_points"], [[2, 2, 2]])
        self.assertTrue(self.report["verification"]["tau_balanced_maximum"])

    def test_sigma_over_n_extrema(self) -> None:
        e = self.report["extrema"]["sigma_over_n"]
        self.assertEqual((e["minimum"]["numerator"], e["minimum"]["denominator"]), (19531, 15625))
        self.assertEqual(e["minimum_points"], [[0, 0, 6]])
        self.assertEqual((e["maximum"]["numerator"], e["maximum"]["denominator"]), (13, 4))
        self.assertEqual(e["maximum_points"], [[3, 2, 1]])

    def test_phi_over_n_support_field(self) -> None:
        e = self.report["extrema"]["phi_over_n"]
        self.assertEqual((e["minimum"]["numerator"], e["minimum"]["denominator"]), (4, 15))
        self.assertEqual((e["maximum"]["numerator"], e["maximum"]["denominator"]), (4, 5))
        self.assertEqual(e["maximum_points"], [[0, 0, 6]])

    def test_all_verifications(self) -> None:
        self.assertTrue(all(self.report["verification"].values()))

    def test_invalid_axes(self) -> None:
        with self.assertRaises(Exception):
            parse_primes("2,4,5")


if __name__ == "__main__":
    unittest.main()
