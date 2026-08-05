from __future__ import annotations

import json
import unittest
from dataclasses import replace
from pathlib import Path

try:
    from tools.pvg_reverse_support_preimage import (
        REGISTERED_CONFIG,
        analyze,
        binary_exact_support_powers,
        is_prime_64,
    )
except ModuleNotFoundError:
    from pvg_reverse_support_preimage import (
        REGISTERED_CONFIG,
        analyze,
        binary_exact_support_powers,
        is_prime_64,
    )


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = (
    ROOT
    / "research/pvg-space-deepening/data/reverse-support-preimage-summary.json"
)
FROZEN_CONFIG = (
    ROOT
    / "governance/frozen-config/PASS-025-REVERSE-SUPPORT-PREIMAGE-FROZEN-CONFIG.md"
)


def summary_projection(data: dict[str, object]) -> dict[str, object]:
    return {
        "schema": data["schema"],
        "classification": data["classification"],
        "configuration": data["configuration"],
        "target": data["target"],
        "seed_fiber": data["seed_fiber"],
        "predecessor_support_count": data["predecessor_support_count"],
        "predecessor_support_cap_exceeded": data["predecessor_support_cap_exceeded"],
        "candidate_supports_with_integers": data["candidate_supports_with_integers"],
        "candidate_exact_support_integer_count":
            data["candidate_exact_support_integer_count"],
        "primality_test_count": data["primality_test_count"],
        "witness_candidate_count": data["witness_candidate_count"],
        "per_seed_candidate_integer_counts":
            data["per_seed_candidate_integer_counts"],
        "per_seed_witness_candidate_counts":
            data["per_seed_witness_candidate_counts"],
        "promoted_witness_count": data["promoted_witness_count"],
        "registered_top_witnesses": [
            {
                "source_pair": row["source_pair"],
                "source_sum": row["source_sum"],
                "exposing_prime_limit": row["exposing_prime_limit"],
                "predecessor_support": row["predecessor_support"],
                "predecessor_radical": row["predecessor_radical"],
                "predecessor_exponents": row["predecessor_exponents"],
                "seed_sum": row["seed_sum"],
                "face_closure_depth":
                    row["forward_orbit"]["face_closure_depth"],
                "terminal_axes": row["forward_orbit"]["terminal_axes"],
            }
            for row in data["promoted_witnesses"]
        ],
        "first_witness": data["first_witness"],
        "outcome": data["outcome"],
        "verification": data["verification"],
        "minimality_scope": data["minimality_scope"],
        "caution": data["caution"],
    }


class PVGReverseSupportPreimageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze()

    def test_registered_configuration_is_frozen(self) -> None:
        config = REGISTERED_CONFIG
        self.assertEqual(config.target_prime_pair_closure_depth, 12)
        self.assertEqual(config.known_tail_support, (2, 167071))
        self.assertEqual(config.known_tail_support_closure_depth, 10)
        self.assertEqual(config.reverse_seed_integer_cap, 5_346_272)
        self.assertEqual(config.candidate_support_node_cap, 50_000)
        self.assertEqual(config.candidate_integer_cap, 10**12)
        self.assertEqual(config.prime_pair_realization_cap, 10**12)
        self.assertEqual(config.orbit_verification_depth_cap, 16)
        self.assertTrue(FROZEN_CONFIG.is_file())

    def test_binary_exact_support_generation(self) -> None:
        self.assertEqual(
            binary_exact_support_powers(2, 5, 100),
            [
                (10, 1, 1),
                (20, 2, 1),
                (40, 3, 1),
                (50, 1, 2),
                (80, 4, 1),
                (100, 2, 2),
            ],
        )
        self.assertEqual(
            binary_exact_support_powers(41, 668243, 27_397_963),
            [(27_397_963, 1, 1)],
        )

    def test_deterministic_primality(self) -> None:
        for prime in (2, 3, 41, 167071, 668243, 27_397_961):
            self.assertTrue(is_prime_64(prime), prime)
        for composite in (0, 1, 4, 341, 167071 * 41, 27_397_963):
            self.assertFalse(is_prime_64(composite), composite)

    def test_registered_scope_counts(self) -> None:
        data = self.data
        self.assertEqual(data["outcome"], "DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS")
        self.assertEqual(data["seed_fiber"]["seed_integer_count"], 5)
        self.assertEqual(
            data["seed_fiber"]["seed_integers"],
            [334142, 668284, 1336568, 2673136, 5346272],
        )
        self.assertEqual(
            data["seed_fiber"]["total_distinct_prime_pair_representations"],
            35_936,
        )
        self.assertEqual(data["predecessor_support_count"], 35_936)
        self.assertFalse(data["predecessor_support_cap_exceeded"])
        self.assertEqual(data["candidate_supports_with_integers"], 14_500)
        self.assertEqual(data["candidate_exact_support_integer_count"], 14_589)
        self.assertEqual(data["primality_test_count"], 14_589)
        self.assertEqual(data["witness_candidate_count"], 1_106)
        self.assertEqual(data["promoted_witness_count"], 25)

    def test_per_seed_counts(self) -> None:
        self.assertEqual(
            self.data["per_seed_candidate_integer_counts"],
            {
                "334142": 1617,
                "668284": 2946,
                "1336568": 5153,
                "2673136": 3419,
                "5346272": 1454,
            },
        )
        self.assertEqual(
            self.data["per_seed_witness_candidate_counts"],
            {
                "334142": 67,
                "668284": 360,
                "1336568": 287,
                "2673136": 327,
                "5346272": 65,
            },
        )

    def test_first_witness_and_seed_association(self) -> None:
        witness = self.data["first_witness"]
        self.assertEqual(witness["source_pair"], [2, 27_397_961])
        self.assertEqual(witness["source_sum"], 27_397_963)
        self.assertEqual(witness["predecessor_support"], [41, 668243])
        self.assertEqual(witness["predecessor_exponents"], [1, 1])
        self.assertEqual(witness["seed_sum"], 668_284)
        self.assertEqual(sum(witness["predecessor_support"]), witness["seed_sum"])
        self.assertEqual(
            witness["predecessor_support"][0] * witness["predecessor_support"][1],
            witness["source_sum"],
        )

    def test_first_witness_forward_orbit(self) -> None:
        witness = self.data["first_witness"]
        orbit = witness["forward_orbit"]
        self.assertEqual(orbit["face_closure_depth"], 12)
        self.assertEqual(orbit["terminal_axes"], [2])
        self.assertEqual(
            orbit["layers"],
            [
                [[2, 27397961]],
                [[41, 668243]],
                [[2, 167071]],
                [[3, 55691]],
                [[2, 27847]],
                [[3, 9283]],
                [[2, 4643]],
                [[5, 929]],
                [[2, 467]],
                [[7, 67]],
                [[2, 37]],
                [[3, 13]],
                [[2]],
            ],
        )

    def test_every_promoted_witness_is_consistent(self) -> None:
        for witness in self.data["promoted_witnesses"]:
            self.assertEqual(sum(witness["source_pair"]), witness["source_sum"])
            self.assertEqual(
                sum(witness["predecessor_support"]), witness["seed_sum"]
            )
            self.assertEqual(
                witness["forward_orbit"]["face_closure_depth"], 12
            )
            self.assertEqual(
                witness["forward_orbit"]["layers"][1],
                [witness["predecessor_support"]],
            )
            self.assertEqual(
                witness["forward_orbit"]["layers"][2], [[2, 167071]]
            )

    def test_all_verification_flags_pass(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))
        self.assertIn(
            "only within the frozen binary-predecessor class",
            self.data["minimality_scope"],
        )
        self.assertIn("confirmatory, not blinded", self.data["caution"])

    def test_configuration_cap_failure_does_not_promote(self) -> None:
        tiny_cap = replace(REGISTERED_CONFIG, candidate_support_node_cap=1)
        result = analyze(tiny_cap)
        self.assertEqual(
            result["outcome"],
            "CONFIGURATION_CAP_EXCEEDED_NO_RESULT_PROMOTION",
        )
        self.assertTrue(result["predecessor_support_cap_exceeded"])
        self.assertEqual(result["promoted_witnesses"], [])
        self.assertIsNone(result["first_witness"])

    def test_invalid_depth_relation_is_rejected(self) -> None:
        bad = replace(REGISTERED_CONFIG, target_prime_pair_closure_depth=13)
        with self.assertRaises(ValueError):
            analyze(bad)

    def test_committed_summary_matches_regeneration(self) -> None:
        self.assertTrue(SUMMARY.is_file())
        committed = json.loads(SUMMARY.read_text(encoding="utf-8"))
        self.assertEqual(committed, summary_projection(self.data))


if __name__ == "__main__":
    unittest.main()
