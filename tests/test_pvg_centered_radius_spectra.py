from __future__ import annotations

import unittest
from fractions import Fraction

try:
    from tools.pvg_centered_radius_spectra import (
        encode_spectrum,
        normalized_centered_radius_spectrum,
        registered_points,
        registered_summary,
        spectrum_relation,
    )
    from tools.pvg_inverse_prime_fibers import prime_pair_fiber
except ModuleNotFoundError:
    from pvg_centered_radius_spectra import (
        encode_spectrum,
        normalized_centered_radius_spectrum,
        registered_points,
        registered_summary,
        spectrum_relation,
    )
    from pvg_inverse_prime_fibers import prime_pair_fiber


class CenteredRadiusSpectrumTests(unittest.TestCase):
    def test_small_exact_spectra(self) -> None:
        self.assertEqual(normalized_centered_radius_spectrum(10), (Fraction(2, 5),))
        self.assertEqual(
            normalized_centered_radius_spectrum(24),
            (Fraction(7, 12), Fraction(5, 12), Fraction(1, 12)),
        )
        self.assertEqual(encode_spectrum((Fraction(2, 5),)), ("2/5",))

    def test_exact_reconstruction_ratios(self) -> None:
        for n in (9, 10, 24, 27, 100):
            spectrum = normalized_centered_radius_spectrum(n)
            pairs = prime_pair_fiber(n)
            self.assertEqual(len(spectrum), len(pairs))
            for radius, (left, right) in zip(spectrum, pairs):
                self.assertEqual(Fraction(left, n), (1 - radius) / 2)
                self.assertEqual(Fraction(right, n), (1 + radius) / 2)

    def test_relations(self) -> None:
        a = (Fraction(1, 5),)
        b = (Fraction(1, 5), Fraction(2, 5))
        c = (Fraction(2, 5),)
        self.assertEqual(spectrum_relation(a, a), "equal")
        self.assertEqual(spectrum_relation(a, b), "proper_subset")
        self.assertEqual(spectrum_relation(b, a), "proper_superset")
        self.assertEqual(spectrum_relation(b, c), "proper_superset")
        self.assertEqual(spectrum_relation(a, c), "disjoint")

    def test_registered_box_shape_and_range(self) -> None:
        points = registered_points()
        self.assertEqual(len(points), 884)
        for value, _support in points:
            spectrum = normalized_centered_radius_spectrum(value)
            self.assertTrue(all(0 < radius < 1 for radius in spectrum))

    def test_registered_summary_ceiling(self) -> None:
        data = registered_summary()
        self.assertEqual(data["scope"]["integer_point_count"], 884)
        self.assertEqual(data["totals"]["representable_point_count"], 745)
        self.assertTrue(data["verification"]["all_radii_strictly_between_zero_and_one"])
        self.assertTrue(data["verification"]["phase_d_not_used"])
        self.assertFalse(data["claim_ceiling"]["phase_d_authorized"])
        self.assertFalse(data["claim_ceiling"]["goldbach_progress"])


if __name__ == "__main__":
    unittest.main()
