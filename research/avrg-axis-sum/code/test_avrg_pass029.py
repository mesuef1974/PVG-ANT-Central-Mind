import unittest

import numpy as np

import avrg_pass029 as p29


class Pass029Tests(unittest.TestCase):
    def test_locked_pass028_vectors(self):
        vectors = p29.load_vectors(p29.default_pass028_path())
        self.assertEqual(len(vectors), 160)
        self.assertEqual(sorted({key[0] for key in vectors}), list(p29.EXPS))
        self.assertEqual(sorted({key[1] for key in vectors}), list(p29.PRIMARY_MODULI))

    def test_centered_vectors_sum_to_zero(self):
        vectors = p29.load_vectors(p29.default_pass028_path())
        centered = p29.centered_vectors(vectors)
        for exp in p29.EXPS:
            for r in p29.PRIMARY_MODULI:
                matrix = np.vstack(
                    [centered[(exp, r, k)] for k in p29.representative_modes(r)]
                )
                np.testing.assert_allclose(np.sum(matrix, axis=0), 0.0, atol=1e-14)

    def test_rank_selection_hits_ninety_percent(self):
        rank, explained = p29.select_rank([3.0, 1.0, 0.1])
        self.assertEqual(rank, 2)
        self.assertGreaterEqual(explained, 0.90)
        previous = 9.0 / 10.01
        self.assertLess(previous, 0.90)

    def test_projection_skill_is_one_inside_basis(self):
        basis = np.asarray([[1.0], [0.0], [0.0]])
        matrix = np.asarray([[2.0, 0.0, 0.0], [-1.0, 0.0, 0.0]])
        metrics = p29.projection_metrics(matrix, basis)
        self.assertAlmostEqual(metrics["vector_skill"], 1.0)
        self.assertAlmostEqual(metrics["scalar_skill"], 1.0)

    def test_structural_rank_uses_centering_constraints(self):
        self.assertEqual(p29.structural_rank_max(11, 2), 3)
        self.assertEqual(p29.structural_rank_max(13, 3), 6)
        self.assertEqual(p29.structural_rank_max(31, 7), 15)

    def test_random_null_is_seed_reproducible(self):
        basis = np.eye(3)[:, :1]
        matrix = np.asarray([[1.0, 0.4, -0.2], [-0.5, 0.2, 0.3]])
        metrics = p29.projection_metrics(matrix, basis)
        fold = {
            "orbit_count": 3,
            "selected_rank": 1,
            "_test": matrix,
            "metrics": metrics,
        }
        first = p29.random_subspace_null([fold], iterations=50, seed=123)
        second = p29.random_subspace_null([fold], iterations=50, seed=123)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
