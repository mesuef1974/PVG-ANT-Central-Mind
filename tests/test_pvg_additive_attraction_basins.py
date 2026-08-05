from __future__ import annotations

import unittest

from tools.pvg_additive_attraction_basins import analyze, analyze_start


class PVGAdditiveAttractionBasinsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(100, 5)

    def test_registered_scope(self) -> None:
        self.assertEqual(
            self.data["scope"],
            {
                "prime_limit": 100,
                "depth_bound": 5,
                "start_face_count": 300,
                "start_family": "all unordered prime-pair faces {p,q} with p<q<=limit",
            },
        )

    def test_terminal_axes(self) -> None:
        self.assertEqual(self.data["terminal_axes"], [2, 3, 5, 7, 13, 19, 31, 43, 61, 73])

    def test_endpoint_multiplicity_distribution(self) -> None:
        self.assertEqual(
            self.data["endpoint_multiplicity_distribution"],
            {"none_observed": 0, "single_terminal": 195, "multiple_terminals": 105},
        )

    def test_bounded_status_distribution(self) -> None:
        self.assertEqual(
            self.data["bounded_status_distribution"],
            {
                "terminal_singleton": 0,
                "transient_face": 290,
                "recurrent_or_reappearing_face": 10,
                "unresolved_at_depth_bound": 0,
            },
        )
        self.assertEqual(self.data["terminal_count_distribution"], {"0": 0, "1": 195, "2": 13, "3": 92})
        self.assertEqual(self.data["unresolved_start_count"], 0)
        self.assertEqual(self.data["observed_cycle_start_count"], 0)

    def test_basin_sizes(self) -> None:
        actual = {
            item["axis"]: (
                item["basin_size"],
                item["exclusive_basin_size"],
                item["shared_basin_size"],
                item["maximum_shortest_depth"],
            )
            for item in self.data["axis_basins"]
        }
        self.assertEqual(
            actual,
            {
                2: (93, 43, 50, 5),
                3: (62, 22, 40, 4),
                5: (153, 53, 100, 3),
                7: (118, 38, 80, 4),
                13: (34, 12, 22, 3),
                19: (18, 8, 10, 3),
                31: (7, 7, 0, 2),
                43: (6, 6, 0, 2),
                61: (3, 3, 0, 2),
                73: (3, 3, 0, 2),
            },
        )

    def test_endpoint_signatures(self) -> None:
        actual = {
            tuple(item["terminal_axes"]): item["start_face_count"]
            for item in self.data["endpoint_signatures"]
        }
        self.assertEqual(len(actual), 19)
        self.assertEqual(actual[(5,)], 53)
        self.assertEqual(actual[(2,)], 43)
        self.assertEqual(actual[(2, 5, 7)], 33)
        self.assertEqual(actual[(3, 5, 7)], 28)
        self.assertEqual(actual[(7, 13, 19)], 1)
        self.assertEqual(actual[(3, 5, 19)], 1)

    def test_depth_four_has_exactly_two_unresolved_starts(self) -> None:
        depth_four = analyze(100, 4)
        unresolved = {
            tuple(record["start_face"])
            for record in depth_four["start_records"]
            if record["bounded_status"] == "unresolved_at_depth_bound"
        }
        self.assertEqual(unresolved, {(37, 97), (61, 73)})

    def test_reappearance_is_not_cycle(self) -> None:
        record = analyze_start((5, 73), 5)
        self.assertEqual(record["terminal_axes"], [2, 5])
        self.assertEqual(record["bounded_status"], "recurrent_or_reappearing_face")
        self.assertEqual(record["reappearing_faces"], [{"face": [2], "depths": [2, 3], "terminal": True}])
        self.assertEqual(record["cycle_faces"], [])

    def test_known_single_terminal_examples(self) -> None:
        self.assertEqual(analyze_start((2, 3), 5)["terminal_axes"], [5])
        self.assertEqual(analyze_start((2, 5), 5)["terminal_axes"], [7])
        self.assertEqual(analyze_start((2, 13), 5)["terminal_axes"], [2])

    def test_all_verifications(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))

    def test_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            analyze(2, 5)
        with self.assertRaises(ValueError):
            analyze(100, -1)
        with self.assertRaises(ValueError):
            analyze_start((5, 3), 5)


if __name__ == "__main__":
    unittest.main()
