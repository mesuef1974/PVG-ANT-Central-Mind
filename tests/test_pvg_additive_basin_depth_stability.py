from __future__ import annotations

import unittest

from tools.pvg_additive_basin_depth_stability import analyze


class PVGAdditiveBasinDepthStabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(100, 0, 5, include_records=True)
        cls.snapshots = {row["depth"]: row for row in cls.data["depth_snapshots"]}
        cls.transitions = {
            (row["from_depth"], row["to_depth"]): row
            for row in cls.data["step_transitions"]
        }
        cls.records = {row["start_key"]: row for row in cls.data["start_records"]}

    def test_registered_scope(self) -> None:
        self.assertEqual(
            self.data["scope"],
            {
                "prime_limit": 100,
                "min_depth": 0,
                "max_depth": 5,
                "depth_values": [0, 1, 2, 3, 4, 5],
                "start_face_count": 300,
                "start_family": "all unordered prime-pair faces {p,q} with p<q<=limit",
            },
        )

    def test_unresolved_contraction(self) -> None:
        self.assertEqual(
            [self.snapshots[d]["unresolved_start_count"] for d in range(6)],
            [300, 276, 115, 25, 2, 0],
        )

    def test_endpoint_multiplicity_evolution(self) -> None:
        self.assertEqual(
            [
                (
                    self.snapshots[d]["no_terminal_observed_start_count"],
                    self.snapshots[d]["single_terminal_start_count"],
                    self.snapshots[d]["multiple_terminal_start_count"],
                )
                for d in range(6)
            ],
            [
                (300, 0, 0),
                (276, 24, 0),
                (44, 164, 92),
                (15, 183, 102),
                (2, 193, 105),
                (0, 195, 105),
            ],
        )

    def test_all_terminal_axes_appear_at_depth_one(self) -> None:
        expected = [2, 3, 5, 7, 13, 19, 31, 43, 61, 73]
        self.assertEqual(self.snapshots[0]["terminal_axes"], [])
        self.assertEqual(self.snapshots[1]["terminal_axes"], expected)
        self.assertTrue(all(self.snapshots[d]["terminal_axes"] == expected for d in range(1, 6)))

    def test_observed_stabilization_depths(self) -> None:
        self.assertEqual(
            self.data["stabilization_depth_distribution"],
            {"0": 0, "1": 24, "2": 171, "3": 80, "4": 23, "5": 2},
        )
        self.assertEqual(
            self.data["bounded_closure_depth_distribution"],
            {"0": 0, "1": 24, "2": 161, "3": 90, "4": 23, "5": 2},
        )
        self.assertEqual(self.data["unresolved_through_max_depth_count"], 0)

    def test_step_change_counts(self) -> None:
        self.assertEqual(
            [
                (
                    self.transitions[(d, d + 1)]["changed_start_count"],
                    self.transitions[(d, d + 1)]["temporarily_unchanged_start_count"],
                )
                for d in range(5)
            ],
            [(24, 276), (232, 44), (87, 18), (23, 2), (2, 0)],
        )

    def test_basin_size_series(self) -> None:
        self.assertEqual(self.data["basin_size_series"]["2"], [0, 12, 61, 87, 91, 93])
        self.assertEqual(self.data["basin_size_series"]["5"], [0, 2, 141, 153, 153, 153])
        self.assertEqual(self.data["basin_size_series"]["7"], [0, 2, 73, 104, 118, 118])

    def test_overlap_graph_emergence(self) -> None:
        self.assertEqual(
            [self.snapshots[d]["overlap_graph"]["edge_count"] for d in range(6)],
            [0, 0, 11, 12, 13, 13],
        )
        self.assertEqual(self.snapshots[2]["overlap_graph"]["component_sizes"], [6, 1, 1, 1, 1])
        self.assertEqual(self.snapshots[2]["overlap_graph"]["strongest_edge"]["axes"], [2, 5])
        self.assertEqual(self.snapshots[2]["overlap_graph"]["strongest_edge"]["weight"], 40)
        self.assertEqual(self.snapshots[3]["overlap_graph"]["strongest_edge"]["axes"], [5, 7])
        self.assertEqual(self.snapshots[3]["overlap_graph"]["strongest_edge"]["weight"], 69)
        self.assertEqual(self.snapshots[4]["overlap_graph"]["strongest_edge"]["weight"], 75)

    def test_axis_five_leadership_emerges_at_depth_two(self) -> None:
        self.assertEqual(self.snapshots[1]["largest_basin_axes"], [2])
        self.assertTrue(all(self.snapshots[d]["largest_basin_axes"] == [5] for d in range(2, 6)))
        self.assertTrue(
            all(
                self.snapshots[d]["overlap_graph"]["maximum_weighted_degree_axes"] == [5]
                for d in range(2, 6)
            )
        )

    def test_last_two_faces(self) -> None:
        self.assertEqual(self.records["{37,97}"]["observed_stabilization_depth"], 5)
        self.assertEqual(self.records["{61,73}"]["observed_stabilization_depth"], 5)
        self.assertEqual(self.records["{37,97}"]["final_terminal_axes"], [2])
        self.assertEqual(self.records["{61,73}"]["final_terminal_axes"], [2])
        self.assertEqual(
            sorted(
                row["start_key"]
                for row in self.data["start_records"]
                if row["observed_stabilization_depth"] == 5
            ),
            ["{37,97}", "{61,73}"],
        )

    def test_all_verifications(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))


if __name__ == "__main__":
    unittest.main()
