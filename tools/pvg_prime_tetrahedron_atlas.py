#!/usr/bin/env python3
"""Deterministic PVG atlas for four prime axes p<q<r<s<=limit.

The atlas studies six edges and four triangular faces of each prime-axis
tetrahedron. It verifies ratio path-independence, face holonomy, additive-gap
composition, vertex recovery from pair sums, axis-2 routing, and finite edge
preservation profiles. No asymptotic or originality claim is made.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path

try:
    from .pvg_prime_pair_edge_atlas import edge_record, is_prime, primes_up_to
except ImportError:
    from pvg_prime_pair_edge_atlas import edge_record, is_prime, primes_up_to  # type: ignore

SCHEMA = "PVG-PRIME-TETRAHEDRON-ATLAS-001"
DEFAULT_LIMIT = 100


def _gcd_all(values: list[int]) -> int:
    g = 0
    for value in values:
        g = gcd(g, value)
    return g


def tetrahedron_record(vertices: tuple[int, int, int, int], *, prime_indices: dict[int, int], record_id: int) -> dict:
    p, q, r, s = vertices
    if not (p < q < r < s and all(is_prime(x) for x in vertices)):
        raise ValueError("tetrahedron_record requires distinct primes p<q<r<s")

    pairs = list(combinations(vertices, 2))
    edge_rows = {}
    for a, b in pairs:
        edge_rows[f"{a}_{b}"] = edge_record(
            a, b,
            prime_index_gap=prime_indices[b] - prime_indices[a],
            record_id=len(edge_rows) + 1,
        )

    pair_sums = {(a, b): a + b for a, b in pairs}
    pair_differences = {(a, b): b - a for a, b in pairs}
    total_vertex_sum = sum(pair_sums.values()) // 3
    recovered = []
    for x in vertices:
        incident_sum = sum(a + b for a, b in pairs if x in (a, b))
        recovered.append((incident_sum - total_vertex_sum) // 2)

    faces = list(combinations(vertices, 3))
    face_checks = []
    for a, b, c in faces:
        holonomy = Fraction(b, a) * Fraction(c, b) * Fraction(a, c)
        face_checks.append({
            "face": [a, b, c],
            "ratio_holonomy": f"{holonomy.numerator}/{holonomy.denominator}",
            "verified": holonomy == 1,
        })

    chain_ratio = Fraction(q, p) * Fraction(r, q) * Fraction(s, r)
    alternate_ratio = Fraction(r, p) * Fraction(s, r)
    direct_ratio = Fraction(s, p)
    consecutive_gaps = [q - p, r - q, s - r]

    sum_preserved = sum(row["sum_level_preserved"] for row in edge_rows.values())
    difference_preserved = sum(row["difference_level_preserved"] for row in edge_rows.values())

    transition_axis_two_flags = []
    for (a, b), row in zip(pairs, edge_rows.values()):
        transition_axis_two_flags.append({
            "edge": [a, b],
            "sum_contains_2": row["sum_transition"]["contains_axis_2"],
            "difference_contains_2": row["difference_transition"]["contains_axis_2"],
            "expected_contains_2": a != 2,
        })

    sums = list(pair_sums.values())
    differences = list(pair_differences.values())
    contains_two = p == 2

    return {
        "id": f"P4-{record_id:05d}",
        "vertices": list(vertices),
        "contains_axis_2": contains_two,
        "edge_count": 6,
        "face_count": 4,
        "path_independence": {
            "chain": f"{chain_ratio.numerator}/{chain_ratio.denominator}",
            "alternate": f"{alternate_ratio.numerator}/{alternate_ratio.denominator}",
            "direct": f"{direct_ratio.numerator}/{direct_ratio.denominator}",
            "verified": chain_ratio == alternate_ratio == direct_ratio,
        },
        "face_holonomies": face_checks,
        "consecutive_gaps": consecutive_gaps,
        "gap_composition": {
            "q_minus_p_plus_r_minus_q": (q - p) + (r - q) == r - p,
            "r_minus_q_plus_s_minus_r": (r - q) + (s - r) == s - q,
            "all_three_to_s_minus_p": sum(consecutive_gaps) == s - p,
        },
        "pair_sums": {f"{a}_{b}": value for (a, b), value in pair_sums.items()},
        "pair_differences": {f"{a}_{b}": value for (a, b), value in pair_differences.items()},
        "sum_transform": {
            "gcd": _gcd_all(sums),
            "expected_gcd": 1 if contains_two else 2,
            "vertex_sum": total_vertex_sum,
            "recovered_vertices": recovered,
            "recovery_verified": tuple(recovered) == vertices,
        },
        "difference_transform": {
            "gcd": _gcd_all(differences),
            "translation_invariant_shape": True,
            "anchor_required_for_absolute_recovery": True,
        },
        "axis_two_routing": {
            "checks": transition_axis_two_flags,
            "verified": all(
                x["sum_contains_2"] == x["expected_contains_2"]
                and x["difference_contains_2"] == x["expected_contains_2"]
                for x in transition_axis_two_flags
            ),
        },
        "preservation_profile": {
            "sum_preserved_edge_count": sum_preserved,
            "difference_preserved_edge_count": difference_preserved,
            "code": f"S{sum_preserved}_D{difference_preserved}",
        },
        "scientific_classification": "exact simplex identities plus finite deterministic atlas",
    }


def generate_records(limit: int = DEFAULT_LIMIT) -> tuple[list[int], list[dict]]:
    primes = primes_up_to(limit)
    index = {p: i for i, p in enumerate(primes)}
    records = [
        tetrahedron_record(vertices, prime_indices=index, record_id=i)
        for i, vertices in enumerate(combinations(primes, 4), 1)
    ]
    return primes, records


def summarize(limit: int, primes: list[int], records: list[dict]) -> dict:
    sum_counts = Counter(r["preservation_profile"]["sum_preserved_edge_count"] for r in records)
    diff_counts = Counter(r["preservation_profile"]["difference_preserved_edge_count"] for r in records)
    profiles = Counter(r["preservation_profile"]["code"] for r in records)
    max_sum = max(sum_counts)
    max_diff = max(diff_counts)
    return {
        "schema": SCHEMA,
        "scope": {
            "prime_limit": limit,
            "prime_count": len(primes),
            "unordered_tetrahedron_count": len(records),
            "edge_count_per_tetrahedron": 6,
            "triangle_face_count_per_tetrahedron": 4,
        },
        "exact_laws": [
            "all ratio transports between fixed endpoints agree",
            "all four triangular face holonomies equal 1",
            "consecutive additive gaps compose to every longer gap",
            "six pair sums recover all four vertices exactly",
            "gcd of all pair sums is 2 for all-odd tetrahedra and 1 when axis 2 is present",
            "difference data is translation invariant and requires an anchor for absolute recovery",
            "axis-2 routing is determined edgewise by whether the edge is incident to axis 2",
            "at most three sum-preserving edges can occur because all such edges are incident to axis 2",
        ],
        "finite_counts": {
            "contains_axis_2": sum(r["contains_axis_2"] for r in records),
            "all_odd": sum(not r["contains_axis_2"] for r in records),
            "sum_preserved_edge_count_distribution": {str(k): sum_counts[k] for k in sorted(sum_counts)},
            "difference_preserved_edge_count_distribution": {str(k): diff_counts[k] for k in sorted(diff_counts)},
            "preservation_profile_distribution": dict(sorted(profiles.items())),
            "maximum_sum_preserved_edges": max_sum,
            "maximum_difference_preserved_edges_observed": max_diff,
        },
        "distinguished_tetrahedra": {
            "maximum_difference_preservation": [r["vertices"] for r in records if r["preservation_profile"]["difference_preserved_edge_count"] == max_diff],
            "maximum_sum_preservation_count": sum(1 for r in records if r["preservation_profile"]["sum_preserved_edge_count"] == max_sum),
        },
        "verification": {
            "all_path_independence": all(r["path_independence"]["verified"] for r in records),
            "all_face_holonomies": all(all(f["verified"] for f in r["face_holonomies"]) for r in records),
            "all_gap_compositions": all(all(r["gap_composition"].values()) for r in records),
            "all_vertex_recoveries": all(r["sum_transform"]["recovery_verified"] for r in records),
            "all_sum_gcd_rules": all(r["sum_transform"]["gcd"] == r["sum_transform"]["expected_gcd"] for r in records),
            "all_axis_two_routing": all(r["axis_two_routing"]["verified"] for r in records),
        },
        "scientific_classification": "exact elementary identities plus finite bound-100 diagnostics; no asymptotic or novelty claim",
    }


CSV_FIELDS = ["id", "p", "q", "r", "s", "contains_axis_2", "sum_preserved", "difference_preserved", "profile", "sum_gcd", "difference_gcd"]


def build_atlas(limit: int = DEFAULT_LIMIT) -> tuple[str, str, dict]:
    primes, records = generate_records(limit)
    summary = summarize(limit, primes, records)
    handle = io.StringIO()
    writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in records:
        p, q, r, s = row["vertices"]
        writer.writerow({
            "id": row["id"], "p": p, "q": q, "r": r, "s": s,
            "contains_axis_2": str(row["contains_axis_2"]).lower(),
            "sum_preserved": row["preservation_profile"]["sum_preserved_edge_count"],
            "difference_preserved": row["preservation_profile"]["difference_preserved_edge_count"],
            "profile": row["preservation_profile"]["code"],
            "sum_gcd": row["sum_transform"]["gcd"],
            "difference_gcd": row["difference_transform"]["gcd"],
        })
    summary_text = json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    return handle.getvalue(), summary_text, summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the PVG prime-axis tetrahedron atlas")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    csv_text, summary_text, _ = build_atlas(args.limit)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"prime-tetrahedron-atlas-primes-le-{args.limit}"
    csv_path = args.output_dir / f"{stem}.csv"
    summary_path = args.output_dir / f"{stem}-summary.json"
    csv_path.write_text(csv_text, encoding="utf-8")
    summary_path.write_text(summary_text, encoding="utf-8")
    print(f"wrote {csv_path}")
    print(f"wrote {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
