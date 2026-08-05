from __future__ import annotations

import unittest
from itertools import combinations

try:
    from tools.pvg_inverse_support_kernel import (
        REGISTERED_FACE_SIZES,
        REGISTERED_PREDECESSOR_PRIME_LIMIT,
        REGISTERED_TARGET_PRIME_LIMIT,
        brute_force_predecessors,
        compression_certificate,
        exact_support_numbers,
        factor_support,
        predecessor_certificate,
        predecessors,
        registered_analysis,
        successors,
        target_universe,
        witness_edges,
    )
    from tools.pvg_local_additive_cell_atlas import primes_up_to
except ModuleNotFoundError:
    from pvg_inverse_support_kernel import (
        REGISTERED_FACE_SIZES,
        REGISTERED_PREDECESSOR_PRIME_LIMIT,
        REGISTERED_TARGET_PRIME_LIMIT,
        brute_force_predecessors,
        compression_certificate,
        exact_support_numbers,
        factor_support,
        predecessor_certificate,
        predecessors,
        registered_analysis,
        successors,
        target_universe,
        witness_edges,
    )
    from pvg_local_additive_cell_atlas import primes_up_to


class PVGInverseSupportKernelTests(unittest.TestCase):
    def test_exact_support_fiber(self) -> None:
        self.assertEqual(exact_support_numbers((2, 3), 30), (6, 12, 18, 24))
        self.assertEqual(exact_support_numbers((2, 5), 40), (10, 20, 40))
        self.assertEqual(exact_support_numbers((31,), 60), (31,))

    def test_successor_examples(self) -> None:
        self.assertEqual(successors((3, 7)), ((2, 5),))
        self.assertEqual(successors((2, 3, 5)), ((2,), (5,), (7,)))

    def test_parity_routing(self) -> None:
        with_two = witness_edges((2, 5), 31)
        without_two = witness_edges((3, 5), 31)
        self.assertTrue(with_two)
        self.assertTrue(without_two)
        self.assertTrue(all(left != 2 and right != 2 for left, right in with_two))
        self.assertTrue(all(left == 2 for left, _ in without_two))

    def test_radical_bound_negative_certificate(self) -> None:
        certificate = compression_certificate((2, 3, 11), 31)
        self.assertGreater(certificate["radical"], certificate["sum_cap"])
        self.assertFalse(certificate["radical_bound_feasible"])
        self.assertEqual(witness_edges((2, 3, 11), 31), tuple())

    def test_witness_edge_law_soundness(self) -> None:
        for target in ((2,), (2, 3), (2, 5), (3, 5), (2, 3, 5)):
            for face in predecessors(target, 31, (2, 3, 4)):
                self.assertIn(target, successors(face))
                certificate = predecessor_certificate(target, face)
                self.assertTrue(certificate["is_predecessor"])
                self.assertGreaterEqual(certificate["witness_count"], 1)

    def test_multiaxis_generation_is_real(self) -> None:
        generated = predecessors((2, 5), 31, (2, 3, 4))
        self.assertTrue(any(len(face) == 3 for face in generated))
        self.assertTrue(any(len(face) == 4 for face in generated))
        self.assertIn((3, 7, 11), generated)
        self.assertIn((3, 7, 11, 13), generated)

    def test_completeness_for_every_registered_target(self) -> None:
        for target in target_universe(REGISTERED_TARGET_PRIME_LIMIT, 4):
            compressed = predecessors(
                target,
                REGISTERED_PREDECESSOR_PRIME_LIMIT,
                REGISTERED_FACE_SIZES,
            )
            brute = brute_force_predecessors(
                target,
                REGISTERED_PREDECESSOR_PRIME_LIMIT,
                REGISTERED_FACE_SIZES,
            )
            self.assertEqual(compressed, brute, target)

    def test_deduplication(self) -> None:
        # A face may contain multiple witness edges for the same target.
        face = (5, 7, 13)
        target = (2, 3)
        certificate = predecessor_certificate(target, face)
        self.assertGreaterEqual(certificate["witness_count"], 2)
        generated = predecessors(target, 31, (3,))
        self.assertEqual(len(generated), len(set(generated)))
        self.assertEqual(generated.count(face), 1)

    def test_registered_analysis_counts(self) -> None:
        summary = registered_analysis()
        self.assertEqual(summary["registered_box"]["target_prime_limit"], 31)
        self.assertEqual(summary["registered_box"]["predecessor_prime_limit"], 31)
        self.assertEqual(summary["registered_box"]["predecessor_face_sizes"], [2, 3, 4])
        self.assertEqual(summary["predecessor_face_count"], 550)
        self.assertEqual(summary["brute_force_pair_evaluation_count"], 2530)
        self.assertEqual(summary["target_count"], 561)
        self.assertEqual(summary["reachable_target_count"], 20)
        self.assertEqual(summary["unreachable_target_count"], 541)
        self.assertEqual(summary["reachable_target_size_distribution"], {"1": 7, "2": 11, "3": 2})
        self.assertEqual(
            summary["predecessor_incidence_count_by_face_size"],
            {"2": 55, "3": 457, "4": 1656},
        )
        self.assertTrue(all(
            value is True
            for key, value in summary["verification"].items()
            if key in {
                "soundness",
                "completeness_against_full_forward_enumeration",
                "deduplication",
                "determinism",
            }
        ))
        self.assertEqual(summary["verification"]["soundness_failures"], [])
        self.assertEqual(summary["verification"]["completeness_failures"], [])

    def test_unreachable_means_inside_box_only(self) -> None:
        summary = registered_analysis()
        self.assertIn("{2,3,11}", summary["unreachable_target_keys"])
        self.assertEqual(summary["claim_ceiling"]["unreachability"], "inside_frozen_box_only")
        self.assertFalse(summary["claim_ceiling"]["general_inverse_theorem"])

    def test_forward_pair_count_oracle(self) -> None:
        primes = primes_up_to(31)
        expected = sum(
            len(tuple(combinations(face, 2)))
            for size in (2, 3, 4)
            for face in combinations(primes, size)
        )
        self.assertEqual(expected, 2530)

    def test_factor_support(self) -> None:
        self.assertEqual(factor_support(24), (2, 3))
        self.assertEqual(factor_support(30), (2, 3, 5))
        self.assertEqual(factor_support(31), (31,))


if __name__ == "__main__":
    unittest.main()
