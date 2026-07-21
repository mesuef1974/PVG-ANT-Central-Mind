#!/usr/bin/env python3
import unittest

from tools.pvg_multiobjective_geometry import analyze, adjacent, dominates


class PVGMultiobjectiveGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = analyze([2, 3, 5], 6)

    def test_registered_scope(self):
        self.assertEqual(self.report["axes"], [2, 3, 5])
        self.assertEqual(self.report["level"], 6)
        self.assertEqual(self.report["point_count"], 28)
        self.assertEqual(self.report["edge_count"], 63)

    def test_objectives_and_orientation(self):
        self.assertEqual(
            self.report["objectives"],
            ["n", "tau", "sigma_over_n", "phi_over_n"],
        )
        self.assertEqual(self.report["objective_orientation"], "maximize_all")

    def test_edge_partition(self):
        self.assertEqual(self.report["pareto_dominance_edge_count"], 8)
        self.assertEqual(self.report["pareto_tradeoff_or_equal_edge_count"], 55)
        self.assertTrue(self.report["verification"]["edge_partition_closes"])

    def test_edge_signature_classes(self):
        self.assertEqual(
            self.report["edge_class_counts"],
            {
                "aligned_decrease_with_ties": 8,
                "strict_tradeoff": 30,
                "tradeoff_with_ties": 25,
            },
        )

    def test_signature_pattern_distribution(self):
        self.assertEqual(
            self.report["signature_pattern_counts"],
            {
                "(-1,+0,+1,+0)": 6,
                "(-1,+0,+1,-1)": 3,
                "(-1,+1,+1,+0)": 12,
                "(-1,+1,+1,-1)": 15,
                "(-1,-1,+0,+0)": 1,
                "(-1,-1,+1,+0)": 4,
                "(-1,-1,-1,+0)": 7,
                "(-1,-1,-1,+1)": 15,
            },
        )

    def test_global_pareto_frontier(self):
        frontier = {
            tuple(row["exponents"])
            for row in self.report["global_pareto_frontier"]
        }
        self.assertEqual(self.report["global_pareto_frontier_size"], 19)
        self.assertIn((0, 0, 6), frontier)
        self.assertIn((2, 2, 2), frontier)
        self.assertIn((3, 2, 1), frontier)
        self.assertIn((6, 0, 0), frontier)
        self.assertNotIn((1, 4, 1), frontier)

    def test_local_frontier_contains_global_frontier(self):
        global_frontier = {
            tuple(row["exponents"])
            for row in self.report["global_pareto_frontier"]
        }
        local_frontier = {
            tuple(row) for row in self.report["local_pareto_frontier"]
        }
        self.assertEqual(self.report["local_pareto_frontier_size"], 21)
        self.assertTrue(global_frontier <= local_frontier)

    def test_dominated_point_count(self):
        self.assertEqual(self.report["dominated_point_count"], 9)
        self.assertTrue(
            self.report["verification"]["every_nonfrontier_point_is_dominated"]
        )

    def test_all_verifications(self):
        self.assertTrue(all(self.report["verification"].values()))

    def test_adjacency(self):
        self.assertTrue(adjacent((2, 2, 2), (3, 1, 2)))
        self.assertFalse(adjacent((2, 2, 2), (4, 0, 2)))

    def test_dominance_requires_one_strict_gain(self):
        same = {
            "n": 1,
            "tau": 1,
            "sigma_over_n": {"numerator": 1, "denominator": 1},
            "phi_over_n": {"numerator": 1, "denominator": 1},
        }
        self.assertFalse(dominates(same, same))


if __name__ == "__main__":
    unittest.main()
