#!/usr/bin/env python3
"""Generate a deterministic PVG atlas for triangles of prime axes.

For primes p < q < r, the three horizontal axis ratios satisfy

    (q/p)(r/q) = r/p,

and the normalized gaps delta(a,b)=(b-a)/(b+a) satisfy the exact composition

    delta(p,r) = (delta(p,q)+delta(q,r)) /
                 (1+delta(p,q)delta(q,r)).

The default registered scope is all unordered prime triples p < q < r <= 100.
The output is a finite diagnostic atlas and does not support asymptotic,
novelty, factorization-speedup, Goldbach, RH, or GRH claims.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path

try:
    from .pvg_prime_pair_edge_atlas import (
        edge_record,
        fraction_payload,
        is_prime,
        primes_up_to,
    )
except ImportError:
    from pvg_prime_pair_edge_atlas import (  # type: ignore
        edge_record,
        fraction_payload,
        is_prime,
        primes_up_to,
    )

SCHEMA = "PVG-PRIME-TRIANGLE-ATLAS-001"
DEFAULT_LIMIT = 100


def normalized_gap(a: int, b: int) -> Fraction:
    return Fraction(b - a, b + a)


def _edge_summary(row: dict) -> dict:
    return {
        "p": row["p"],
        "q": row["q"],
        "ratio": row["axis_ratio"],
        "normalized_gap": row["normalized_gap"],
        "sum": row["sum_transition"],
        "difference": row["difference_transition"],
        "sum_level_preserved": row["sum_level_preserved"],
        "difference_level_preserved": row["difference_level_preserved"],
        "both_level_preserved": row["both_level_preserved"],
    }


def triangle_record(
    p: int,
    q: int,
    r: int,
    *,
    prime_indices: dict[int, int],
    record_id: int,
) -> dict:
    if not (p < q < r and is_prime(p) and is_prime(q) and is_prime(r)):
        raise ValueError("triangle_record requires primes p < q < r")

    edge_pq = edge_record(
        p,
        q,
        prime_index_gap=prime_indices[q] - prime_indices[p],
        record_id=1,
    )
    edge_qr = edge_record(
        q,
        r,
        prime_index_gap=prime_indices[r] - prime_indices[q],
        record_id=2,
    )
    edge_pr = edge_record(
        p,
        r,
        prime_index_gap=prime_indices[r] - prime_indices[p],
        record_id=3,
    )

    ratio_pq = Fraction(q, p)
    ratio_qr = Fraction(r, q)
    ratio_pr = Fraction(r, p)
    delta_pq = normalized_gap(p, q)
    delta_qr = normalized_gap(q, r)
    delta_pr = normalized_gap(p, r)

    composed_delta = (delta_pq + delta_qr) / (1 + delta_pq * delta_qr)

    sum_pq = p + q
    sum_qr = q + r
    sum_pr = p + r
    recovered_p = (sum_pq + sum_pr - sum_qr) // 2
    recovered_q = (sum_pq + sum_qr - sum_pr) // 2
    recovered_r = (sum_pr + sum_qr - sum_pq) // 2

    edges = [edge_pq, edge_qr, edge_pr]
    sum_preserved_count = sum(row["sum_level_preserved"] for row in edges)
    difference_preserved_count = sum(
        row["difference_level_preserved"] for row in edges
    )
    double_preserved_count = sum(row["both_level_preserved"] for row in edges)

    contains_axis_2 = p == 2
    incident_edges = [edge_pq, edge_pr]
    opposite_edge = edge_qr
    incident_transition_flags = [
        transition["contains_axis_2"]
        for edge in incident_edges
        for transition in (edge["sum_transition"], edge["difference_transition"])
    ]
    opposite_transition_flags = [
        opposite_edge["sum_transition"]["contains_axis_2"],
        opposite_edge["difference_transition"]["contains_axis_2"],
    ]
    all_transition_flags = [
        transition["contains_axis_2"]
        for edge in edges
        for transition in (edge["sum_transition"], edge["difference_transition"])
    ]

    axis_two_routing_verified = (
        (not contains_axis_2 and all(all_transition_flags))
        or (
            contains_axis_2
            and not any(incident_transition_flags)
            and all(opposite_transition_flags)
        )
    )

    return {
        "id": f"PT-{record_id:04d}",
        "p": p,
        "q": q,
        "r": r,
        "parity_class": "contains_axis_2" if contains_axis_2 else "all_odd",
        "prime_index_gaps": {
            "pq": prime_indices[q] - prime_indices[p],
            "qr": prime_indices[r] - prime_indices[q],
            "pr": prime_indices[r] - prime_indices[p],
        },
        "axis_ratios": {
            "pq": fraction_payload(ratio_pq),
            "qr": fraction_payload(ratio_qr),
            "pr": fraction_payload(ratio_pr),
        },
        "ratio_composition": {
            "identity": "(q/p)(r/q)=r/p",
            "verified": ratio_pq * ratio_qr == ratio_pr,
            "closed_loop_holonomy": fraction_payload(
                ratio_pq * ratio_qr * Fraction(p, r)
            ),
        },
        "normalized_gaps": {
            "pq": fraction_payload(delta_pq),
            "qr": fraction_payload(delta_qr),
            "pr": fraction_payload(delta_pr),
        },
        "normalized_gap_composition": {
            "identity": "delta_pr=(delta_pq+delta_qr)/(1+delta_pq*delta_qr)",
            "composed": fraction_payload(composed_delta),
            "verified": composed_delta == delta_pr,
        },
        "additive_gap_composition": {
            "pq": q - p,
            "qr": r - q,
            "pr": r - p,
            "identity": "(q-p)+(r-q)=r-p",
            "verified": (q - p) + (r - q) == r - p,
        },
        "pair_sums": {"pq": sum_pq, "qr": sum_qr, "pr": sum_pr},
        "vertex_recovery_from_pair_sums": {
            "p": recovered_p,
            "q": recovered_q,
            "r": recovered_r,
            "verified": (recovered_p, recovered_q, recovered_r) == (p, q, r),
        },
        "edges": {
            "pq": _edge_summary(edge_pq),
            "qr": _edge_summary(edge_qr),
            "pr": _edge_summary(edge_pr),
        },
        "preservation_profile": {
            "sum_preserved_edge_count": sum_preserved_count,
            "difference_preserved_edge_count": difference_preserved_count,
            "double_preserved_edge_count": double_preserved_count,
            "code": f"S{sum_preserved_count}_D{difference_preserved_count}",
        },
        "axis_two_routing": {
            "verified": axis_two_routing_verified,
            "rule": (
                "all six reduced transitions contain axis 2 for all-odd triangles; "
                "for triangles containing axis 2, the four transitions incident to axis 2 "
                "exclude it and the two transitions on the opposite odd-odd edge contain it"
            ),
        },
        "scientific_classification": "exact triangle identities plus finite diagnostic record",
    }


def generate_records(limit: int = DEFAULT_LIMIT) -> tuple[list[int], list[dict]]:
    primes = primes_up_to(limit)
    index = {p: i for i, p in enumerate(primes)}
    records = [
        triangle_record(
            p,
            q,
            r,
            prime_indices=index,
            record_id=record_id,
        )
        for record_id, (p, q, r) in enumerate(combinations(primes, 3), 1)
    ]
    return primes, records


def summarize(limit: int, primes: list[int], records: list[dict]) -> dict:
    parity = Counter(row["parity_class"] for row in records)
    sum_counts = Counter(
        row["preservation_profile"]["sum_preserved_edge_count"] for row in records
    )
    difference_counts = Counter(
        row["preservation_profile"]["difference_preserved_edge_count"]
        for row in records
    )
    profiles = Counter(row["preservation_profile"]["code"] for row in records)

    all_three_difference = [
        [row["p"], row["q"], row["r"]]
        for row in records
        if row["preservation_profile"]["difference_preserved_edge_count"] == 3
    ]
    all_odd_two_difference = [
        [row["p"], row["q"], row["r"]]
        for row in records
        if row["parity_class"] == "all_odd"
        and row["preservation_profile"]["difference_preserved_edge_count"] == 2
    ]
    two_sum_preserved = [
        row
        for row in records
        if row["preservation_profile"]["sum_preserved_edge_count"] == 2
    ]
    double_edge_triangles = [
        row
        for row in records
        if row["preservation_profile"]["double_preserved_edge_count"] > 0
    ]

    return {
        "schema": SCHEMA,
        "scope": {
            "prime_limit": limit,
            "primes": primes,
            "prime_count": len(primes),
            "unordered_triangle_count": len(records),
        },
        "definitions": {
            "axis_triangle": "three distinct prime axes p<q<r",
            "ratio_holonomy": "(q/p)(r/q)(p/r)=1",
            "normalized_gap": "delta(a,b)=(b-a)/(b+a)",
            "normalized_gap_composition": (
                "delta(p,r)=(delta(p,q)+delta(q,r))/(1+delta(p,q)delta(q,r))"
            ),
            "preservation_profile": "Sx_Dy counts sum- and difference-preserving edges",
        },
        "exact_laws": [
            "axis-ratio transport is path independent: (q/p)(r/q)=r/p",
            "closed multiplicative holonomy around every prime-axis triangle is 1",
            "additive gaps compose: (q-p)+(r-q)=r-p",
            "normalized gaps obey the fractional composition law",
            "three pair sums recover the three prime vertices uniquely",
            "all-odd triangles route all six reduced sum/difference transitions through axis 2",
            "when a triangle contains axis 2, only the opposite odd-odd edge routes through axis 2",
            "an all-odd triangle has at most two difference-preserving edges, with equality only for (3,5,7)",
            "all three differences are prime only for the triangle (2,5,7)",
            "no triangle has three sum-preserving edges",
        ],
        "finite_counts": {
            "parity_class": dict(sorted(parity.items())),
            "sum_preserved_edge_count_distribution": {
                str(k): sum_counts[k] for k in sorted(sum_counts)
            },
            "difference_preserved_edge_count_distribution": {
                str(k): difference_counts[k] for k in sorted(difference_counts)
            },
            "preservation_profile_distribution": dict(sorted(profiles.items())),
            "triangles_with_two_sum_preserved_edges": len(two_sum_preserved),
            "triangles_containing_the_unique_double_preserved_edge_2_5": len(
                double_edge_triangles
            ),
        },
        "distinguished_triangles": {
            "all_three_difference_preserved": all_three_difference,
            "all_odd_two_difference_preserved": all_odd_two_difference,
            "ratio_and_gap_composition_example": [2, 3, 5],
        },
        "verification": {
            "all_ratio_compositions": all(
                row["ratio_composition"]["verified"] for row in records
            ),
            "all_closed_holonomies_equal_one": all(
                row["ratio_composition"]["closed_loop_holonomy"]["text"] == "1/1"
                for row in records
            ),
            "all_normalized_gap_compositions": all(
                row["normalized_gap_composition"]["verified"] for row in records
            ),
            "all_additive_gap_compositions": all(
                row["additive_gap_composition"]["verified"] for row in records
            ),
            "all_vertex_recoveries": all(
                row["vertex_recovery_from_pair_sums"]["verified"] for row in records
            ),
            "all_axis_two_routing_checks": all(
                row["axis_two_routing"]["verified"] for row in records
            ),
        },
        "scientific_classification": (
            "exact elementary triangle identities plus a finite deterministic atlas; "
            "no asymptotic, novelty, or major-conjecture claim"
        ),
    }


CSV_FIELDS = [
    "id",
    "p",
    "q",
    "r",
    "parity_class",
    "ratio_pq",
    "ratio_qr",
    "ratio_pr",
    "delta_pq",
    "delta_qr",
    "delta_pr",
    "gap_pq",
    "gap_qr",
    "gap_pr",
    "sum_preserved_edge_count",
    "difference_preserved_edge_count",
    "double_preserved_edge_count",
    "profile",
    "kappa_plus_pq",
    "kappa_plus_qr",
    "kappa_plus_pr",
    "kappa_minus_pq",
    "kappa_minus_qr",
    "kappa_minus_pr",
    "axis_two_routing_verified",
]


def csv_text(records: list[dict]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in records:
        writer.writerow(
            {
                "id": row["id"],
                "p": row["p"],
                "q": row["q"],
                "r": row["r"],
                "parity_class": row["parity_class"],
                "ratio_pq": row["axis_ratios"]["pq"]["text"],
                "ratio_qr": row["axis_ratios"]["qr"]["text"],
                "ratio_pr": row["axis_ratios"]["pr"]["text"],
                "delta_pq": row["normalized_gaps"]["pq"]["text"],
                "delta_qr": row["normalized_gaps"]["qr"]["text"],
                "delta_pr": row["normalized_gaps"]["pr"]["text"],
                "gap_pq": row["additive_gap_composition"]["pq"],
                "gap_qr": row["additive_gap_composition"]["qr"],
                "gap_pr": row["additive_gap_composition"]["pr"],
                "sum_preserved_edge_count": row["preservation_profile"][
                    "sum_preserved_edge_count"
                ],
                "difference_preserved_edge_count": row["preservation_profile"][
                    "difference_preserved_edge_count"
                ],
                "double_preserved_edge_count": row["preservation_profile"][
                    "double_preserved_edge_count"
                ],
                "profile": row["preservation_profile"]["code"],
                "kappa_plus_pq": row["edges"]["pq"]["sum"]["kappa"],
                "kappa_plus_qr": row["edges"]["qr"]["sum"]["kappa"],
                "kappa_plus_pr": row["edges"]["pr"]["sum"]["kappa"],
                "kappa_minus_pq": row["edges"]["pq"]["difference"]["kappa"],
                "kappa_minus_qr": row["edges"]["qr"]["difference"]["kappa"],
                "kappa_minus_pr": row["edges"]["pr"]["difference"]["kappa"],
                "axis_two_routing_verified": str(
                    row["axis_two_routing"]["verified"]
                ).lower(),
            }
        )
    return stream.getvalue()


def json_text(payload: dict) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def build_atlas(limit: int = DEFAULT_LIMIT) -> tuple[str, str, dict]:
    primes, records = generate_records(limit)
    summary = summarize(limit, primes, records)
    return csv_text(records), json_text(summary), summary


def write_atlas(output_dir: Path, limit: int = DEFAULT_LIMIT) -> tuple[Path, Path]:
    csv_payload, summary_payload, _ = build_atlas(limit)
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"prime-triangle-atlas-primes-le-{limit}"
    csv_path = output_dir / f"{stem}.csv"
    summary_path = output_dir / f"{stem}-summary.json"
    csv_path.write_text(csv_payload, encoding="utf-8")
    summary_path.write_text(summary_payload, encoding="utf-8")
    return csv_path, summary_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate the finite PVG prime-axis triangle composition atlas."
    )
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    csv_path, summary_path = write_atlas(args.output_dir, args.limit)
    print(f"wrote {csv_path}")
    print(f"wrote {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
