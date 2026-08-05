#!/usr/bin/env python3
"""General exact laws for a simplex of distinct prime axes.

This module unifies the point/edge/triangle/tetrahedron cases for
P=(p_1,...,p_m), m>=2.  It records only elementary exact identities and
finite verification data; it makes no originality or asymptotic claim.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, prod
from typing import Iterable, Sequence

try:
    from .pvg_inverse_geometry import is_prime_64
except ImportError:
    from pvg_inverse_geometry import is_prime_64  # type: ignore


class SimplexInputError(ValueError):
    pass


def validate_vertices(vertices: Iterable[int]) -> tuple[int, ...]:
    values = tuple(int(x) for x in vertices)
    if len(values) < 2:
        raise SimplexInputError("at least two distinct prime axes are required")
    if tuple(sorted(values)) != values or len(set(values)) != len(values):
        raise SimplexInputError("vertices must be strictly increasing")
    if any(not is_prime_64(x) for x in values):
        raise SimplexInputError("every vertex must be prime")
    return values


def face_counts(m: int) -> dict[str, int]:
    if m < 2:
        raise SimplexInputError("m must be at least 2")
    # A k-dimensional face uses k+1 vertices.
    return {str(k): comb(m, k + 1) for k in range(m)}


def pair_data(vertices: Sequence[int]) -> list[dict]:
    rows: list[dict] = []
    for i, j in combinations(range(len(vertices)), 2):
        p, q = vertices[i], vertices[j]
        total = p + q
        gap = q - p
        rows.append(
            {
                "i": i,
                "j": j,
                "p": p,
                "q": q,
                "ratio": {"numerator": q, "denominator": p, "text": f"{q}/{p}"},
                "sum": total,
                "difference": gap,
                "sum_level_preserved": is_prime_64(total),
                "difference_level_preserved": is_prime_64(gap),
                "sum_contains_axis_2": total % 2 == 0,
                "difference_contains_axis_2": gap % 2 == 0,
            }
        )
    return rows


def consecutive_gaps(vertices: Sequence[int]) -> tuple[int, ...]:
    return tuple(vertices[i + 1] - vertices[i] for i in range(len(vertices) - 1))


def reconstruct_from_anchor(anchor: int, gaps: Sequence[int]) -> tuple[int, ...]:
    values = [int(anchor)]
    for gap in gaps:
        if int(gap) <= 0:
            raise SimplexInputError("consecutive gaps must be positive")
        values.append(values[-1] + int(gap))
    return tuple(values)


def all_pair_sums(vertices: Sequence[int]) -> dict[tuple[int, int], int]:
    return {(i, j): vertices[i] + vertices[j] for i, j in combinations(range(len(vertices)), 2)}


def reconstruct_from_labeled_pair_sums(m: int, sums: dict[tuple[int, int], int]) -> tuple[int, ...]:
    if m < 3:
        raise SimplexInputError("labeled pair sums reconstruct vertices only for m>=3")
    expected = {(i, j) for i, j in combinations(range(m), 2)}
    if set(sums) != expected:
        raise SimplexInputError("complete labeled pair-sum data are required")
    edge_total = sum(sums.values())
    if edge_total % (m - 1):
        raise SimplexInputError("pair-sum total is incompatible with integral vertices")
    vertex_total = edge_total // (m - 1)
    recovered: list[int] = []
    for i in range(m):
        incident = sum(value for (a, b), value in sums.items() if a == i or b == i)
        numerator = incident - vertex_total
        if numerator % (m - 2):
            raise SimplexInputError("pair-sum data are incompatible with integral vertices")
        recovered.append(numerator // (m - 2))
    return tuple(recovered)


def gcd_of_pair_sums(vertices: Sequence[int]) -> int:
    result = 0
    for value in all_pair_sums(vertices).values():
        result = gcd(result, value)
    return result


def path_ratio(vertices: Sequence[int], path: Sequence[int]) -> Fraction:
    if len(path) < 2:
        raise SimplexInputError("path must contain at least two vertex indices")
    m = len(vertices)
    if any(i < 0 or i >= m for i in path):
        raise SimplexInputError("path index outside simplex")
    value = Fraction(1, 1)
    for a, b in zip(path, path[1:]):
        value *= Fraction(vertices[b], vertices[a])
    return value


def normalized_gap(a: int, b: int) -> Fraction:
    return Fraction(b - a, b + a)


def compose_normalized_gaps(left: Fraction, right: Fraction) -> Fraction:
    return (left + right) / (1 + left * right)


def analyze(vertices: Iterable[int]) -> dict:
    p = validate_vertices(vertices)
    m = len(p)
    pairs = pair_data(p)
    sums = all_pair_sums(p)
    gaps = consecutive_gaps(p)
    reconstructed = reconstruct_from_labeled_pair_sums(m, sums) if m >= 3 else None
    all_odd = all(x % 2 == 1 for x in p)
    contains_two = p[0] == 2
    sum_preserved = sum(row["sum_level_preserved"] for row in pairs)
    difference_preserved = sum(row["difference_level_preserved"] for row in pairs)

    path_checks: list[dict] = []
    if m >= 3:
        direct = Fraction(p[-1], p[0])
        consecutive = path_ratio(p, list(range(m)))
        via_each = [path_ratio(p, [0, k, m - 1]) for k in range(1, m - 1)]
        path_checks = [
            {"path": [0, m - 1], "ratio": str(direct)},
            {"path": list(range(m)), "ratio": str(consecutive)},
            *[
                {"path": [0, k, m - 1], "ratio": str(value)}
                for k, value in zip(range(1, m - 1), via_each)
            ],
        ]
        path_independent = consecutive == direct and all(x == direct for x in via_each)
    else:
        path_independent = True

    normalized_composition = True
    for i, j, k in combinations(range(m), 3):
        left = normalized_gap(p[i], p[j])
        right = normalized_gap(p[j], p[k])
        if compose_normalized_gaps(left, right) != normalized_gap(p[i], p[k]):
            normalized_composition = False
            break

    pair_sum_gcd = gcd_of_pair_sums(p)
    expected_gcd = 2 if all_odd else 1

    return {
        "schema": "PVG-PRIME-SIMPLEX-GENERAL-001",
        "vertices": list(p),
        "m": m,
        "dimension": m - 1,
        "root_lattice": f"A_{m - 1}",
        "face_counts_by_dimension": face_counts(m),
        "edge_count": comb(m, 2),
        "ordered_horizontal_neighbor_degree_at_interior": m * (m - 1),
        "difference_coordinate_rank": m - 1,
        "consecutive_gaps": list(gaps),
        "translation_invariant_shape": list(gaps),
        "anchor_reconstruction": list(reconstruct_from_anchor(p[0], gaps)),
        "pair_sums": [
            {"i": i, "j": j, "value": value}
            for (i, j), value in sorted(sums.items())
        ],
        "pair_sum_reconstruction": list(reconstructed) if reconstructed is not None else None,
        "pair_sum_reconstruction_available": m >= 3,
        "pair_sum_gcd": pair_sum_gcd,
        "expected_pair_sum_gcd": expected_gcd,
        "contains_axis_2": contains_two,
        "all_odd": all_odd,
        "pairs": pairs,
        "sum_preserved_edge_count": sum_preserved,
        "difference_preserved_edge_count": difference_preserved,
        "general_sum_preservation_upper_bound": m - 1,
        "sum_bound_verified": sum_preserved <= m - 1,
        "axis_2_transition_routing": {
            "total_reduced_transitions": m * (m - 1),
            "containing_axis_2": m * (m - 1) if all_odd else (m - 1) * (m - 2),
            "excluding_axis_2": 0 if all_odd else 2 * (m - 1),
        },
        "path_checks": path_checks,
        "verification": {
            "face_count_total_is_2^m_minus_1": sum(face_counts(m).values()) == 2**m - 1,
            "anchor_plus_gaps_reconstructs_vertices": reconstruct_from_anchor(p[0], gaps) == p,
            "pair_sums_reconstruct_vertices_for_m_ge_3": reconstructed == p if m >= 3 else True,
            "pair_sum_gcd_rule": pair_sum_gcd == expected_gcd,
            "path_independence": path_independent,
            "normalized_gap_composition": normalized_composition,
            "sum_preservation_bound": sum_preserved <= m - 1,
            "routing_counts_close": (
                (m * (m - 1) if all_odd else (m - 1) * (m - 2))
                + (0 if all_odd else 2 * (m - 1))
                == m * (m - 1)
            ),
        },
        "classification": (
            "exact elementary simplex identities and finite verification; "
            "no originality, asymptotic, or major-conjecture claim"
        ),
    }


def parse_vertices(text: str) -> tuple[int, ...]:
    try:
        return tuple(int(part.strip()) for part in text.split(",") if part.strip())
    except ValueError as exc:
        raise SimplexInputError("vertices must be comma-separated integers") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze general PVG prime-simplex laws.")
    parser.add_argument("vertices", help="strictly increasing comma-separated primes, e.g. 2,3,5,7")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        report = analyze(parse_vertices(args.vertices))
    except SimplexInputError as exc:
        print(json.dumps({"status": "invalid_prime_simplex", "reason": str(exc)}, indent=2))
        return 2
    print(json.dumps(report, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
