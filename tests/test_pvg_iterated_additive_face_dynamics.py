from __future__ import annotations

import unittest

from tools.pvg_iterated_additive_face_dynamics import analyze, successors


class PVGIteratedAdditiveFaceDynamicsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(100, 4)

    def test_registered_scope(self) -> None:
        self.assertEqual(self.data["scope"], {"prime_limit": 100, "depth": 4, "start_face_count": 300})

    def test_layer_contraction(self) -> None:
        self.assertEqual(self.data["layer_face_counts"], [300, 52, 22, 10, 4])

    def test_unique_graph_size(self) -> None:
        self.assertEqual(self.data["unique_face_count"], 323)
        self.assertEqual(self.data["unique_arc_count"], 338)

    def test_dimension_distribution(self) -> None:
        self.assertEqual(self.data["face_dimension_distribution"], {"1": 10, "2": 300, "3": 13})

    def test_terminal_faces(self) -> None:
        self.assertEqual(self.data["terminal_faces"], [[2], [3], [5], [7], [13], [19], [31], [43], [61], [73]])

    def test_known_successor_examples(self) -> None:
        self.assertEqual(successors((2, 3)), ((5,),))
        self.assertEqual(successors((2, 3, 5)), ((2, 3), (5,), (7,)))

    def test_all_verifications(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))


if __name__ == "__main__":
    unittest.main()
