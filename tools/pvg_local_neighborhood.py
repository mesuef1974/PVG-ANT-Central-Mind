#!/usr/bin/env python3
"""Exact local-neighborhood geometry for Prime Valuation Geometry (PVG).

The tool requires a complete certified factorization, obtained automatically for
1 <= n < 2^64 or supplied explicitly through --factors under the same prime-
certificate boundary used by pvg_inverse_geometry.py.

It generates the finite horizontal neighborhood inside the minimal support face,
axis-ratio lines, axis-parallel sequences, simplex vertices, and local gcd
signatures. It does not claim a general integer-factorization speedup.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, prod
from typing import Dict, Mapping

try:  # package import in tests
    from .pvg_inverse_geometry import (
        GeometryInputError,
        UINT64_LIMIT,
        factorint_64,
        parse_factorization,
        validate_complete_factorization,
    )
except ImportError:  # direct script execution from tools/
    from pvg_inverse_geometry import (  # type: ignore
        GeometryInputError,
        UINT64_LIMIT,
        factorint_64,
        parse_factorization,
        validate_complete_factorization,
    )


def _fraction_payload(value: Fraction) -> dict:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": f"{value.numerator}/{value.denominator}",
    }


def _normalize_factors(factors: Mapping[int, int]) -> Dict[int, int]:
    answer = {int(p): int(a) for p, a in factors.items() if int(a) > 0}
    return dict(sorted(answer.items()))


def _value_from_factors(factors: Mapping[int, int]) -> int:
    return prod(p**a for p, a in factors.items())


def exact_factors(n: int, supplied_factorization: str | None = None) -> tuple[Dict[int, int], str]:
    if n < 1:
        raise GeometryInputError("PVG positive-integer mode requires n >= 1")
    if supplied_factorization is not None:
        factors = parse_factorization(supplied_factorization)
        validate_complete_factorization(n, factors)
        return factors, "complete_user_supplied_factorization_verified"
    if n >= UINT64_LIMIT:
        raise GeometryInputError(
            "n >= 2^64: exact local geometry is intentionally refused without "
            "a complete certified factorization supplied with --factors"
        )
    return factorint_64(n), "automatic_certified_factorization_below_2^64"


def primitive_ray(factors: Mapping[int, int], steps: int) -> dict | None:
    factors = _normalize_factors(factors)
    if not factors:
        return None
    index = 0
    for exponent in factors.values():
        index = gcd(index, exponent)
    primitive_factors = {p: a // index for p, a in factors.items()}
    generator = _value_from_factors(primitive_factors)
    return {
        "primitive_generator": generator,
        "ray_index_of_input": index,
        "primitive_direction": {str(p): a for p, a in primitive_factors.items()},
        "sequence": [generator**k for k in range(steps + 1)],
        "parameter": "u^k",
    }


def axis_ratio_matrix(support: list[int]) -> list[dict]:
    rows: list[dict] = []
    for donor in support:
        for recipient in support:
            if donor == recipient:
                continue
            ratio = Fraction(recipient, donor)
            rows.append(
                {
                    "donor_axis": donor,
                    "recipient_axis": recipient,
                    "direction": {str(donor): -1, str(recipient): 1},
                    "ratio": _fraction_payload(ratio),
                }
            )
    return rows


def primitive_neighbors(n: int, factors: Mapping[int, int]) -> list[dict]:
    factors = _normalize_factors(factors)
    support = list(factors)
    omega = len(support)
    Omega = sum(factors.values())
    rows: list[dict] = []
    for donor in support:
        for recipient in support:
            if donor == recipient:
                continue
            neighbor = (n // donor) * recipient
            neighbor_factors = dict(factors)
            neighbor_factors[donor] -= 1
            if neighbor_factors[donor] == 0:
                del neighbor_factors[donor]
            neighbor_factors[recipient] = neighbor_factors.get(recipient, 0) + 1
            common = gcd(n, neighbor)
            rows.append(
                {
                    "donor_axis": donor,
                    "recipient_axis": recipient,
                    "neighbor": neighbor,
                    "neighbor_factorization": [
                        {"prime": p, "valuation": a}
                        for p, a in sorted(neighbor_factors.items())
                    ],
                    "ratio": _fraction_payload(Fraction(recipient, donor)),
                    "direction": {str(donor): -1, str(recipient): 1},
                    "level_preserved": sum(neighbor_factors.values()) == Omega,
                    "gcd_recovery": {
                        "gcd": common,
                        "input_over_gcd": n // common,
                        "neighbor_over_gcd": neighbor // common,
                    },
                    "normalized_edge_signature": {
                        "gcd": 1,
                        "input": donor,
                        "neighbor": recipient,
                        "sum": donor + recipient,
                        "absolute_difference": abs(recipient - donor),
                        "lcm": donor * recipient,
                    },
                    "ambient_face_size": omega,
                }
            )
    return rows


def pair_lines_through_point(n: int, factors: Mapping[int, int]) -> list[dict]:
    factors = _normalize_factors(factors)
    support = list(factors)
    rows: list[dict] = []
    for index, donor in enumerate(support):
        for recipient in support[index + 1 :]:
            terms: list[dict] = []
            for k in range(-factors[recipient], factors[donor] + 1):
                exponents = dict(factors)
                exponents[donor] -= k
                exponents[recipient] += k
                exponents = _normalize_factors(exponents)
                terms.append(
                    {
                        "k": k,
                        "value": _value_from_factors(exponents),
                        "valuation_vector": {str(p): a for p, a in exponents.items()},
                    }
                )
            rows.append(
                {
                    "axis_pair": [donor, recipient],
                    "positive_direction": f"{recipient}/{donor}",
                    "ratio": _fraction_payload(Fraction(recipient, donor)),
                    "k_range": [-factors[recipient], factors[donor]],
                    "terms": terms,
                }
            )
    return rows


def axis_parallel_sequences(n: int, support: list[int], steps: int) -> list[dict]:
    return [
        {
            "axis": prime,
            "direction": {str(prime): 1},
            "ratio": prime,
            "sequence": [n * prime**k for k in range(steps + 1)],
            "level_change_per_step": 1,
        }
        for prime in support
    ]


def horizontal_distance(
    left_factors: Mapping[int, int], right_factors: Mapping[int, int]
) -> int:
    left = _normalize_factors(left_factors)
    right = _normalize_factors(right_factors)
    if sum(left.values()) != sum(right.values()):
        raise GeometryInputError("horizontal distance requires equal Omega levels")
    support = set(left) | set(right)
    l1 = sum(abs(left.get(p, 0) - right.get(p, 0)) for p in support)
    if l1 % 2:
        raise GeometryInputError("equal-level valuation difference must have even L1 norm")
    return l1 // 2


def geometric_triplet(left: int, middle: int, right: int) -> dict:
    if min(left, middle, right) < 1:
        raise GeometryInputError("geometric-triplet inputs must be positive")
    return {
        "is_geometric": middle * middle == left * right,
        "ratio_left_to_middle": _fraction_payload(Fraction(middle, left)),
        "ratio_middle_to_right": _fraction_payload(Fraction(right, middle)),
        "midpoint_identity": f"{middle}^2 = {left}*{right}",
    }


def local_geometry(n: int, factors: Mapping[int, int], *, source: str, steps: int = 3) -> dict:
    if steps < 0:
        raise GeometryInputError("steps must be nonnegative")
    factors = _normalize_factors(factors)
    validate_complete_factorization(n, factors)
    support = list(factors)
    omega = len(support)
    Omega = sum(factors.values())

    if n == 1:
        return {
            "schema": "PVG-LOCAL-NEIGHBORHOOD-001",
            "input": 1,
            "factorization_status": source,
            "support": [],
            "omega": 0,
            "Omega": 0,
            "horizontal_root_lattice": None,
            "ordered_horizontal_degree": 0,
            "axis_ratio_matrix": [],
            "primitive_horizontal_neighbors": [],
            "pair_lines_through_point": [],
            "axis_parallel_sequences": [],
            "primitive_composite_ray": None,
            "horizontal_simplex_vertices": [],
            "scientific_classification": "exact identity and finite local encoding",
        }

    vertices = [
        {"axis": p, "vertex": p**Omega, "valuation": {str(p): Omega}}
        for p in support
    ]

    return {
        "schema": "PVG-LOCAL-NEIGHBORHOOD-001",
        "input": n,
        "factorization_status": source,
        "factorization": [
            {"prime": p, "valuation": factors[p]} for p in support
        ],
        "support": support,
        "omega": omega,
        "Omega": Omega,
        "horizontal_root_lattice": f"A_{omega - 1}" if omega >= 2 else "A_0",
        "ordered_horizontal_degree": omega * (omega - 1),
        "axis_ratio_matrix": axis_ratio_matrix(support),
        "primitive_horizontal_neighbors": primitive_neighbors(n, factors),
        "pair_lines_through_point": pair_lines_through_point(n, factors),
        "axis_parallel_sequences": axis_parallel_sequences(n, support, steps),
        "primitive_composite_ray": primitive_ray(factors, steps),
        "horizontal_simplex_vertices": vertices,
        "laws": {
            "primitive_neighbor": "N_(i->j)=N*p_j/p_i",
            "horizontal_direction": "sum(h_i)=0",
            "direction_ratio": "Q(h)=product(p_i^h_i)",
            "horizontal_line": "N_k=N*Q(h)^k while all valuations remain nonnegative",
            "horizontal_distance": "d_H(a,b)=1/2*sum_i|a_i-b_i|",
            "adjacent_axis_recovery": "g=gcd(N,M), p_i=N/g, p_j=M/g",
        },
        "scientific_classification": (
            "exact identities, finite geometric encoding, and diagnostic research substrate; "
            "no general factorization advantage claimed"
        ),
    }


def analyze(n: int, supplied_factorization: str | None = None, *, steps: int = 3) -> dict:
    factors, source = exact_factors(n, supplied_factorization)
    return local_geometry(n, factors, source=source, steps=steps)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze exact local neighborhoods and axis ratios in PVG."
    )
    parser.add_argument("n", type=int, help="positive integer")
    parser.add_argument(
        "--factors",
        help="complete factorization such as '2^2,3,5'; required for n >= 2^64",
    )
    parser.add_argument(
        "--steps", type=int, default=3, help="number of forward terms for infinite rays"
    )
    parser.add_argument(
        "--compact", action="store_true", help="emit compact JSON"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        report = analyze(args.n, args.factors, steps=args.steps)
    except GeometryInputError as exc:
        print(
            json.dumps(
                {
                    "schema": "PVG-LOCAL-NEIGHBORHOOD-ERROR-001",
                    "input": args.n,
                    "status": "exact_local_geometry_not_certified",
                    "reason": str(exc),
                    "principle": (
                        "exact local geometry requires a complete certified prime factorization"
                    ),
                },
                ensure_ascii=False,
                indent=None if args.compact else 2,
            )
        )
        return 2

    print(
        json.dumps(
            report,
            ensure_ascii=False,
            sort_keys=True,
            indent=None if args.compact else 2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
