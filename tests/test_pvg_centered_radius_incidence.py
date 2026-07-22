from __future__ import annotations

import unittest

from tools.pvg_centered_radius_incidence import (
    governed_coordinate,
    independent_indexes,
    production_indexes,
    registered_summary,
)


class CenteredRadiusIncidenceTests(unittest.TestCase):
    def test_governed_coordinate_examples(self) -> None:
        self.assertEqual(governed_coordinate(12, 5, 7), 1)
        self.assertEqual(governed_coordinate(19, 2, 17), 15)
        with self.assertRaises(ValueError):
            governed_coordinate(10, -1, 11)
        with self.assertRaises(ValueError):
            governed_coordinate(10, 3, 11)

    def test_independent_indexes_match(self) -> None:
        self.assertEqual(production_indexes(), independent_indexes())

    def test_registered_scope_and_incidence(self) -> None:
        summary = registered_summary()
        scope = summary["scope"]
        self.assertEqual(scope["integer_point_count"], 884)
        self.assertEqual(scope["represented_point_count"], 745)
        self.assertEqual(scope["coordinate_occurrence_count"], 218024)
        self.assertEqual(scope["unique_coordinate_count"], 36797)

    def test_preregistered_maxima(self) -> None:
        maxima = registered_summary()["maxima"]
        self.assertEqual(maxima["maximum_integer_owner_degree"], 64)
        self.assertEqual(maxima["coordinates_attaining_maximum_integer_degree"], [7])
        self.assertEqual(maxima["maximum_support_owner_degree"], 8)
        self.assertEqual(maxima["coordinates_attaining_maximum_support_degree"], [3, 51, 2691, 3021])

    def test_route_and_component_counts(self) -> None:
        summary = registered_summary()
        self.assertEqual(summary["route_coordinate_classes"], {
            "cross_route": 85,
            "even_only": 36702,
            "odd_only": 10,
        })
        self.assertEqual(summary["totals"]["bipartite_component_count"], 12)
        self.assertEqual(summary["bipartite_components"][0]["integer_count"], 620)
        self.assertEqual(summary["bipartite_components"][1]["integer_count"], 115)

    def test_projection_and_cooccurrence_certificate(self) -> None:
        summary = registered_summary()
        self.assertEqual(
            summary["totals"]["coordinates_collapsing_multiple_integers_to_one_support"],
            22423,
        )
        self.assertEqual(summary["totals"]["support_pair_with_nonzero_intersection_count"], 131)
        self.assertEqual(summary["totals"]["cooccurrence_pair_occurrence_count"], 78736278)
        self.assertEqual(
            summary["lossless_cooccurrence_certificate"]["sha256"],
            "ca63d9767c96fe16593666586be6996868bb68d9e32c52a233f0e779292a8512",
        )

    def test_verification_and_ceiling(self) -> None:
        summary = registered_summary()
        self.assertTrue(all(summary["verification"].values()))
        self.assertFalse(any(summary["claim_ceiling"].values()))


if __name__ == "__main__":
    unittest.main()
