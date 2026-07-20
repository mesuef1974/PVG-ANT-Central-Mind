import math, unittest
from pvg_lab_validation import (
    additive_fiber,
    build_grid,
    dlog,
    factor,
    geometric_abs_third,
    is_prime,
    pearson,
    run,
)


class TestPVGLab(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(factor(360), {2: 3, 3: 2, 5: 1})
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(1))
        self.assertAlmostEqual(dlog(60, 72), math.log(30), places=12)

    def test_smooth_baselines(self):
        cases = {(10, 2): 4, (100, 5): 34, (1000, 3): 40, (1000, 7): 141}
        for (x, y), expected in cases.items():
            self.assertEqual(build_grid(x, [y], [x], 1_000_000)[0]["exact"], expected)

    def test_additive(self):
        z = additive_fiber(10, 5)
        self.assertEqual(z["goldbach"], 3)
        self.assertEqual(z["ordered"], 9)

    def test_validation_design(self):
        z = run(10000, 1_000_000)
        self.assertTrue(z["design"]["nonoverlap"])
        self.assertGreater(z["counts"]["holdout"], 20)
        self.assertTrue(math.isfinite(z["correlations"]["partial_pi_max_share"]))

    def test_statistics_guards(self):
        self.assertEqual(pearson([1.0, 1.0, 1.0], [2.0, 3.0, 4.0]), 0.0)
        self.assertEqual(pearson([1.0], [2.0]), 0.0)
        with self.assertRaises(ValueError):
            pearson([1.0, 2.0], [1.0])

        q = 1e-6
        expected = (12 * math.exp(-1) - 2) / (q ** 3)
        actual = geometric_abs_third(1 - q)
        self.assertAlmostEqual(actual / expected, 1.0, places=12)


if __name__ == "__main__":
    unittest.main()
