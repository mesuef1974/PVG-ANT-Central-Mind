from __future__ import annotations

import unittest

try:
    from tools.pvg_centered_radius_spectra import (
        centered_radius_spectrum,
        normalized_centered_radius_spectrum,
        reconstruct_prime_pairs,
        registered_points,
        registered_summary,
        spectrum_record,
        spectrum_relation,
    )
    from tools.pvg_inverse_prime_fibers import prime_gap_fiber, prime_pair_fiber
except ModuleNotFoundError:
    from pvg_centered_radius_spectra import (
        centered_radius_spectrum,
        normalized_centered_radius_spectrum,
        reconstruct_prime_pairs,
        registered_points,
        registered_summary,
        spectrum_record,
        spectrum_relation,
    )
    from pvg_inverse_prime_fibers import prime_gap_fiber, prime_pair_fiber


class CenteredRadiusSpectrumTests(unittest.TestCase):
    def test_small_exact_spectra(self) -> None:
        self.assertEqual(centered_radius_spectrum(10), (2,))
        self.assertEqual(centered_radius_spectrum(24), (7, 5, 1))
        self.assertEqual(centered_radius_spectrum(9), (5,))
        self.assertEqual(centered_radius_spectrum(27), tuple())
        self.assertEqual(normalized_centered_radius_spectrum(24), (7, 5, 1))

    def test_authorized_even_and_odd_routes(self) -> None:
        for n in (10, 24, 100):
            self.assertEqual(
                centered_radius_spectrum(n),
                tuple(gap // 2 for gap in prime_gap_fiber(n)),
            )
        for n in (9, 27, 45):
            self.assertEqual(centered_radius_spectrum(n), prime_gap_fiber(n))

    def test_exact_reconstruction(self) -> None:
        for n in (5, 8, 9, 10, 12, 24, 27, 100):
            self.assertEqual(reconstruct_prime_pairs(n), prime_pair_fiber(n))
            record = spectrum_record(n)
            self.assertTrue(record["reconstruction_holds"])
            self.assertEqual(record["multiplicity"], len(prime_pair_fiber(n)))
        with self.assertRaises(ValueError):
            reconstruct_prime_pairs(10, (6,))
        with self.assertRaises(ValueError):
            reconstruct_prime_pairs(9, (4,))

    def test_relations(self) -> None:
        a = (1,)
        b = (1, 2)
        c = (2,)
        self.assertEqual(spectrum_relation(a, a), "equal")
        self.assertEqual(spectrum_relation(a, b), "proper_subset")
        self.assertEqual(spectrum_relation(b, a), "proper_superset")
        self.assertEqual(spectrum_relation(b, c), "proper_superset")
        self.assertEqual(spectrum_relation(a, c), "disjoint")

    def test_complete_registered_box_reconstruction(self) -> None:
        points = registered_points()
        self.assertEqual(len(points), 884)
        pair_count = 0
        for value, _support in points:
            spectrum = centered_radius_spectrum(value)
            pairs = prime_pair_fiber(value)
            self.assertTrue(all(isinstance(radius, int) and radius > 0 for radius in spectrum))
            self.assertEqual(reconstruct_prime_pairs(value, spectrum), pairs)
            self.assertEqual(len(spectrum), len(pairs))
            if value % 2:
                self.assertTrue(all(radius == value - 4 for radius in spectrum))
            pair_count += len(pairs)
        self.assertEqual(pair_count, 218_024)

    def test_registered_summary_exact_counts(self) -> None:
        data = registered_summary()
        self.assertEqual(data["scope"]["integer_point_count"], 884)
        totals = data["totals"]
        self.assertEqual(totals["representable_point_count"], 745)
        self.assertEqual(totals["nonrepresentable_point_count"], 139)
        self.assertEqual(totals["total_coordinate_occurrence_count"], 218_024)
        self.assertEqual(totals["unique_coordinate_value_count"], 36_797)
        self.assertEqual(totals["unique_even_coordinate_value_count"], 36_787)
        self.assertEqual(totals["unique_odd_coordinate_value_count"], 95)
        self.assertEqual(totals["cross_route_coordinate_value_count"], 85)
        self.assertEqual(totals["odd_only_coordinate_value_count"], 10)
        self.assertEqual(totals["unique_spectrum_count_including_empty"], 744)
        self.assertEqual(totals["unique_nonempty_spectrum_count"], 743)
        self.assertEqual(totals["nonempty_spectrum_collision_class_count"], 1)
        self.assertEqual(totals["empty_spectrum_class_size"], 139)
        self.assertEqual(totals["proper_containment_edge_count"], 2_048)
        self.assertEqual(totals["singleton_subset_containment_edge_count"], 2_038)
        self.assertEqual(totals["non_singleton_subset_containment_edge_count"], 10)
        self.assertEqual(totals["shared_coordinate_value_count"], 27_799)
        self.assertEqual(totals["even_even_shared_coordinate_value_count"], 27_714)
        self.assertEqual(totals["odd_even_shared_coordinate_value_count"], 85)
        self.assertEqual(totals["odd_odd_shared_coordinate_value_count"], 0)

    def test_collision_containment_and_ceiling(self) -> None:
        data = registered_summary()
        collision = data["only_nonempty_spectrum_collision"]
        self.assertEqual(collision["spectrum"], [1])
        self.assertEqual(collision["class_size"], 3)
        self.assertEqual(
            [member["integer"] for member in collision["members"]],
            [5, 8, 12],
        )
        profile = data["containment_profile"]
        self.assertEqual(profile["non_singleton_subset_spectrum_count"], 3)
        self.assertEqual(profile["non_singleton_subset_spectra"], [[4, 2], [9, 3], [45, 33, 3]])
        self.assertEqual(len(profile["non_singleton_edges"]), 10)
        self.assertEqual(data["largest_shared_coordinates"][0]["coordinate"], 7)
        self.assertEqual(data["largest_shared_coordinates"][0]["integer_count"], 64)
        self.assertTrue(all(data["verification"].values()))
        self.assertFalse(data["claim_ceiling"]["phase_d_authorized"])
        self.assertFalse(data["claim_ceiling"]["goldbach_progress"])
        self.assertFalse(data["claim_ceiling"]["pnt_progress"])
        self.assertFalse(data["claim_ceiling"]["rh_progress"])
        self.assertFalse(data["claim_ceiling"]["grh_progress"])


if __name__ == "__main__":
    unittest.main()
