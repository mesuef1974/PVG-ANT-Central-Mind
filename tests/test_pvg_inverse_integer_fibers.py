from __future__ import annotations

import json
import unittest
from math import gcd
from pathlib import Path

try:
    from tools.pvg_inverse_integer_fibers import (
        REGISTERED_DIRICHLET_S,
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        brute_force_integer_fiber,
        dirichlet_closed_form,
        dirichlet_partial_sum,
        divides_in_fiber,
        exponent_vector,
        exponent_vectors,
        factor_support,
        fiber_record,
        hasse_edges,
        integer_fiber,
        reconstruct,
        registered_summary,
        support_universe,
    )
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import (
        REGISTERED_DIRICHLET_S,
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        brute_force_integer_fiber,
        dirichlet_closed_form,
        dirichlet_partial_sum,
        divides_in_fiber,
        exponent_vector,
        exponent_vectors,
        factor_support,
        fiber_record,
        hasse_edges,
        integer_fiber,
        reconstruct,
        registered_summary,
        support_universe,
    )

ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "research/pvg-space-deepening/data/inverse-integer-fibers-summary.json"
DOC_PATH = ROOT / "research/pvg-space-deepening/engine-003-inverse-integer-fibers.md"


class InverseIntegerFiberTests(unittest.TestCase):
    def test_registered_support_universe_has_25_faces(self) -> None:
        faces = support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES)
        self.assertEqual(len(faces), 25)

    def test_generator_equals_complete_scan_for_every_face(self) -> None:
        for face in support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES):
            self.assertEqual(
                integer_fiber(face, REGISTERED_INTEGER_CAP),
                brute_force_integer_fiber(face, REGISTERED_INTEGER_CAP),
                face,
            )

    def test_exponent_bijection_and_reconstruction(self) -> None:
        for face in support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES):
            vectors = exponent_vectors(face, REGISTERED_INTEGER_CAP)
            values = integer_fiber(face, REGISTERED_INTEGER_CAP)
            self.assertEqual(len(vectors), len(values))
            self.assertEqual(len(set(vectors)), len(vectors))
            for value, vector in zip(values, vectors):
                self.assertEqual(reconstruct(face, vector), value)
                self.assertEqual(exponent_vector(value, face), vector)
                self.assertEqual(factor_support(value), face)

    def test_radical_is_minimum(self) -> None:
        for face in support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES):
            record = fiber_record(face, REGISTERED_INTEGER_CAP)
            radical = 1
            for prime in face:
                radical *= prime
            self.assertEqual(record["minimum"], radical)

    def test_divisibility_is_coordinatewise(self) -> None:
        face = (2, 3, 5)
        vectors = exponent_vectors(face, REGISTERED_INTEGER_CAP)
        for left in vectors[:25]:
            for right in vectors[:25]:
                left_value = reconstruct(face, left)
                right_value = reconstruct(face, right)
                self.assertEqual(divides_in_fiber(left, right), right_value % left_value == 0)

    def test_hasse_edges_increment_one_coordinate(self) -> None:
        face = (2, 3, 5)
        for left, right in hasse_edges(face, REGISTERED_INTEGER_CAP):
            differences = [b - a for a, b in zip(left, right)]
            self.assertEqual(sum(differences), 1)
            self.assertEqual(sum(1 for value in differences if value == 1), 1)
            self.assertTrue(all(value in (0, 1) for value in differences))

    def test_multiplication_gcd_lcm_are_closed(self) -> None:
        for face in support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES):
            values = integer_fiber(face, REGISTERED_INTEGER_CAP)
            sample = values[: min(6, len(values))]
            for left in sample:
                for right in sample:
                    self.assertEqual(factor_support(left * right), face)
                    self.assertEqual(factor_support(gcd(left, right)), face)
                    lcm = left * right // gcd(left, right)
                    self.assertEqual(factor_support(lcm), face)

    def test_addition_and_quotient_are_not_generally_closed(self) -> None:
        self.assertNotEqual(factor_support(2 + 4), (2,))
        self.assertEqual(factor_support(4 // 2), (2,))
        self.assertEqual(4 // 4, 1)
        self.assertEqual(factor_support(1), tuple())

    def test_dirichlet_partial_sum_is_below_closed_form(self) -> None:
        for face in support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES):
            partial = dirichlet_partial_sum(face, REGISTERED_DIRICHLET_S, REGISTERED_INTEGER_CAP)
            closed = dirichlet_closed_form(face, REGISTERED_DIRICHLET_S)
            self.assertGreaterEqual(closed, partial)
            self.assertGreater(closed, 0.0)

    def test_registered_summary_invariants(self) -> None:
        summary = registered_summary()
        self.assertEqual(summary["scope"]["support_face_count"], 25)
        self.assertEqual(summary["totals"]["total_fiber_points_across_faces"], 884)
        self.assertEqual(summary["totals"]["complete_scan_match_count"], 25)
        self.assertEqual(summary["totals"]["complete_scan_mismatch_count"], 0)
        self.assertTrue(all(summary["verification"].values()))
        self.assertFalse(summary["claim_ceiling"]["phase_c_authorized"])

    def test_registered_json_matches_regeneration(self) -> None:
        expected = registered_summary()
        stored = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

    def test_research_note_contains_required_ceiling(self) -> None:
        text = DOC_PATH.read_text(encoding="utf-8")
        for token in (
            "Exponent-lattice bijection",
            "Dirichlet-series identity",
            "Phase C is not authorized",
            "No originality claim",
        ):
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
