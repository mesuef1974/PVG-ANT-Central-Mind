import unittest

import numpy as np

import avrg_pass034 as p34


class Pass034Tests(unittest.TestCase):
    def test_locked_pass028_hash(self):
        self.assertEqual(
            p34.sha256_file(p34.default_pass028_path()),
            p34.EXPECTED_PASS028_SHA256,
        )

    def test_blocks_are_disjoint_and_cover_six_windows(self):
        self.assertTrue(set(p34.EARLY_EXPS).isdisjoint(p34.LATE_EXPS))
        self.assertEqual(
            sorted(p34.EARLY_EXPS + p34.LATE_EXPS), list(p34.ALL_EXPS)
        )

    def test_structural_rank_max_for_three_windows(self):
        self.assertEqual(p34.structural_rank_max(11, 2), 2)
        self.assertEqual(p34.structural_rank_max(31, 7), 12)

    def test_block_arrays_use_source_mean_only(self):
        class FakeP29:
            @staticmethod
            def representative_modes(r):
                return [2, 4]

        centered = {}
        for exp in p34.ALL_EXPS:
            centered[(exp, 11, 2)] = np.asarray([float(exp), 2.0])
            centered[(exp, 11, 4)] = np.asarray([-float(exp), -2.0])
        train, target, means = p34.block_arrays(
            centered, 11, p34.EARLY_EXPS, p34.LATE_EXPS, FakeP29
        )
        np.testing.assert_allclose(means[2], np.asarray([15.0, 2.0]))
        np.testing.assert_allclose(train[0], np.asarray([-1.0, 0.0]))
        np.testing.assert_allclose(target[0], np.asarray([2.0, 0.0]))

    def test_cosine_keeps_sign(self):
        first = np.asarray([1.0, 0.0, 0.0])
        self.assertAlmostEqual(p34.cosine(first, first), 1.0, places=12)
        self.assertAlmostEqual(p34.cosine(first, -first), -1.0, places=12)

    def test_rank_selection_reaches_locked_energy(self):
        rng = np.random.default_rng(340701)
        train = rng.normal(size=(18, 8))
        rank, explained = p34.select_block_rank(train, rank_max=7)
        self.assertGreaterEqual(explained, p34.TRAIN_EXPLAINED_THRESHOLD)
        self.assertLessEqual(rank, 7)


if __name__ == "__main__":
    unittest.main()
