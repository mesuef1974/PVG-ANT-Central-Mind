import unittest

import avrg_pass026 as p26


class Pass026Tests(unittest.TestCase):
    def test_locked_rows_and_energy_identity(self):
        rows = p26.load_rows(p26.default_pass023_path(), p26.default_pass025_holdout_path())
        self.assertEqual(len(rows), 160)
        self.assertEqual(sorted({row["exp"] for row in rows}), list(p26.EXPS))
        self.assertEqual(sorted({row["r"] for row in rows}), list(p26.PRIMARY_MODULI))

    def test_centered_log_identity(self):
        rows = p26.load_rows(p26.default_pass023_path(), p26.default_pass025_holdout_path())
        centered = p26.centered_log_rows(rows)
        self.assertEqual(len(centered), 160)
        for row in centered:
            self.assertAlmostEqual(
                row["y_log_ratio"], row["a_on"] - row["b_off"], places=12
            )

    def test_pure_on_variation(self):
        result = p26.channel_metrics([-1.0, 0.0, 1.0], [0.0, 0.0, 0.0])
        self.assertAlmostEqual(result["on_share"], 1.0)
        self.assertAlmostEqual(result["off_share"], 0.0)
        self.assertAlmostEqual(result["on_only_skill_vs_zero"], 1.0)

    def test_pure_off_variation(self):
        result = p26.channel_metrics([0.0, 0.0, 0.0], [-1.0, 0.0, 1.0])
        self.assertAlmostEqual(result["on_share"], 0.0)
        self.assertAlmostEqual(result["off_share"], 1.0)
        self.assertAlmostEqual(result["off_only_skill_vs_zero"], 1.0)

    def test_attribution_identity_with_covariance(self):
        result = p26.channel_metrics(
            [-1.0, -0.2, 0.4, 0.8], [-0.7, 0.3, -0.1, 0.5]
        )
        self.assertAlmostEqual(
            result["ratio_ss"],
            result["on_ss"] + result["off_ss"] - 2 * result["on_off_covariance_sum"],
            places=12,
        )
        self.assertAlmostEqual(result["on_share"] + result["off_share"], 1.0)

    def test_character_mean_removal(self):
        rows = p26.load_rows(p26.default_pass023_path(), p26.default_pass025_holdout_path())
        residuals = p26.remove_character_means(p26.centered_log_rows(rows))
        for r in p26.PRIMARY_MODULI:
            modes = sorted({row["k"] for row in residuals if row["r"] == r})
            for k in modes:
                local = [row for row in residuals if row["r"] == r and row["k"] == k]
                for field in ("a_on_residual", "b_off_residual", "y_residual"):
                    self.assertAlmostEqual(sum(row[field] for row in local), 0.0, places=12)


if __name__ == "__main__":
    unittest.main()
