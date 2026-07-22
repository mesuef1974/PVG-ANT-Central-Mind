from __future__ import annotations

import unittest

try:
    from tools.pvg_centered_radius_spectra import (
        centered_radius_spectrum,
        normalized_centered_radius_spectrum,
        registered_points,
        registered_summary,
        spectrum_relation,
    )
    from tools.pvg_inverse_prime_fibers import prime_gap_fiber
except ModuleNotFoundError:
    from pvg_centered_radius_spectra import (
        centered_radius_spectrum,
        normalized_centered_radius_spectrum,
        registered_points,
        registered_summary,
        spectrum_relation,
    )
    from pvg_inverse_prime_fibers import prime_gap_fiber


class CenteredRadiusSpectrumTests(unittest.TestCase):
    def test_small_exact_spectra(self) -> None:
        self.assertEqual(centered_radius_spectrum(10), (2,))
        self.assertEqual(centered_radius_spectrum(24), (7, 5, 1))
        self.assertEqual(centered_radius_spectrum(9), (5,))
        self.assertEqual(normalized_centered_radius_spectrum(24), (7, 5, 1))

    def test_authorized_even_and_odd_routes(self) -> None:
        for n in (10, 24, 100):
            self.assertEqual(centered_radius_spectrum(n), tuple(gap // 2 for gap in prime_gap_fiber(n)))
        for n in (9, 27, 45):
            self.assertEqual(centered_radius_spectrum(n), prime_gap_fiber(n))

    def test_relations(self) -> None:
        a = (1,)
        b = (1, 2)
        c = (2,)
        self.assertEqual(spectrum_relation(a, a), "equal")
        self.assertEqual(spectrum_relation(a, b), "proper_subset")
        self.assertEqual(spectrum_relation(b, a), "proper_superset")
        self.assertEqual(spectrum_relation(b, c), "proper_superset")
        self.assertEqual(spectrum_relation(a, c), "disjoint")

    def test_registered_box_shape_and_integrality(self) -> None:
        points = registered_points()
        self.assertEqual(len(points), 884)
        for value, _support in points:
            spectrum = centered_radius_spectrum(value)
            self.assertTrue(all(isinstance(radius, int) and radius > 0 for radius in spectrum))

    def test_registered_summary_ceiling(self) -> None:
        data = registered_summary()
        self.assertEqual(data["scope"]["integer_point_count"], 884)
        self.assertEqual(data["totals"]["representable_point_count"], 745)
        self.assertTrue(data["verification"]["even_coordinates_are_positive_integers"])
        self.assertTrue(data["verification"]["phase_d_not_used"])
        self.assertFalse(data["claim_ceiling"]["phase_d_authorized"])
        self.assertFalse(data["claim_ceiling"]["goldbach_progress"])


if __name__ == "__main__":
    unittest.main()
