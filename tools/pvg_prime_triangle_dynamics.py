#!/usr/bin/env python3
"""Deterministic dynamics of prime-axis triangle transforms.

For p<q<r prime, study

    T_minus = (q-p, r-q, r-p)
    T_plus  = (p+q, q+r, p+r)

The registered scope is p<q<r<=100.  The atlas separates exact invertibility
statements from finite diagnostic counts.  No asymptotic or novelty claim is
made.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path

try:
    from .pvg_prime_pair_edge_atlas import is_prime, primes_up_to
except ImportError:
    from pvg_prime_pair_edge_atlas import is_prime, primes_up_to  # type: ignore

SCHEMA = "PVG-PRIME-TRIANGLE-DYNAMICS-001"
DEFAULT_LIMIT = 100


def triple_gcd(values: tuple[int, int, int]) -> int:
    return gcd(gcd(values[0], values[1]), values[2])


def primitive_shape(values: tuple[int, int, int]) -> tuple[int, int, int]:
    g = triple_gcd(values)
    return tuple(v // g for v in values)


def recover_from_sums(sums: tuple[int, int, int]) -> tuple[int, int, int]:
    s_pq, s_qr, s_pr = sums
    p = (s_pq + s_pr - s_qr) // 2
    q = (s_pq + s_qr - s_pr) // 2
    r = (s_pr + s_qr - s_pq) // 2
    return p, q, r


def difference_transform(p: int, q: int, r: int) -> tuple[int, int, int]:
    return q - p, r - q, r - p


def sum_transform(p: int, q: int, r: int) -> tuple[int, int, int]:
    return p + q, q + r, p + r


def all_distinct_prime(values: tuple[int, int, int]) -> bool:
    return len(set(values)) == 3 and all(is_prime(v) for v in values)


def sorted_prime_triangle(values: tuple[int, int, int]) -> tuple[int, int, int] | None:
    if not all_distinct_prime(values):
        return None
    return tuple(sorted(values))


def difference_chain(p: int, q: int, r: int, max_steps: int = 8) -> list[dict]:
    current = (p, q, r)
    chain: list[dict] = []
    for step in range(max_steps):
        raw = difference_transform(*current)
        target = sorted_prime_triangle(raw)
        chain.append(
            {
                "step": step + 1,
                "source": list(current),
                "raw_difference_triple": list(raw),
                "prime_triangle_target": list(target) if target else None,
            }
        )
        if target is None:
            break
        current = target
    return chain


def dynamics_record(p: int, q: int, r: int, record_id: int) -> dict:
    if not (p < q < r and is_prime(p) and is_prime(q) and is_prime(r)):
        raise ValueError("dynamics_record requires primes p<q<r")

    differences = difference_transform(p, q, r)
    sums = sum_transform(p, q, r)
    difference_prime_flags = tuple(is_prime(v) for v in differences)
    sum_prime_flags = tuple(is_prime(v) for v in sums)
    difference_target = sorted_prime_triangle(differences)
    recovered = recover_from_sums(sums)
    difference_gcd = triple_gcd(differences)
    sum_gcd = triple_gcd(sums)

    return {
        "id": f"PTD-{record_id:04d}",
        "source": [p, q, r],
        "parity_class": "contains_axis_2" if p == 2 else "all_odd",
        "difference_transform": {
            "labeled": list(differences),
            "sorted": sorted(differences),
            "relation": "d_pr=d_pq+d_qr",
            "relation_verified": differences[2] == differences[0] + differences[1],
            "gcd": difference_gcd,
            "primitive_shape": list(primitive_shape(differences)),
            "prime_flags": list(difference_prime_flags),
            "prime_count": sum(difference_prime_flags),
            "is_distinct_prime_triangle": difference_target is not None,
            "prime_triangle_target": list(difference_target) if difference_target else None,
            "translation_invariant": True,
            "absolute_position_recoverable_without_anchor": False,
        },
        "sum_transform": {
            "labeled": list(sums),
            "gcd": sum_gcd,
            "prime_flags": list(sum_prime_flags),
            "prime_count": sum(sum_prime_flags),
            "is_distinct_prime_triangle": all_distinct_prime(sums),
            "recovered_source": list(recovered),
            "recovery_verified": recovered == (p, q, r),
            "injective_on_labeled_triangles": True,
        },
        "support_routing": {
            "sum_common_gcd_rule": "2 for all-odd source triangles; 1 when source contains axis 2",
            "sum_common_gcd_verified": sum_gcd == (1 if p == 2 else 2),
        },
        "difference_chain": difference_chain(p, q, r),
        "scientific_classification": "exact transform identities plus finite diagnostic record",
    }


def generate_records(limit: int = DEFAULT_LIMIT) -> tuple[list[int], list[dict]]:
    primes = primes_up_to(limit)
    records = [
        dynamics_record(p, q, r, i)
        for i, (p, q, r) in enumerate(combinations(primes, 3), 1)
    ]
    return primes, records


def summarize(limit: int, primes: list[int], records: list[dict]) -> dict:
    difference_prime_counts = Counter(
        row["difference_transform"]["prime_count"] for row in records
    )
    sum_prime_counts = Counter(row["sum_transform"]["prime_count"] for row in records)
    difference_gcds = Counter(row["difference_transform"]["gcd"] for row in records)
    sum_gcds = Counter(row["sum_transform"]["gcd"] for row in records)

    prime_difference_targets = [
        {
            "source": row["source"],
            "target": row["difference_transform"]["prime_triangle_target"],
            "chain": row["difference_chain"],
        }
        for row in records
        if row["difference_transform"]["is_distinct_prime_triangle"]
    ]

    cycles = []
    for item in prime_difference_targets:
        seen = {tuple(item["source"])}
        for step in item["chain"]:
            target = step["prime_triangle_target"]
            if target is None:
                break
            t = tuple(target)
            if t in seen:
                cycles.append({"source": item["source"], "repeated": target})
                break
            seen.add(t)

    return {
        "schema": SCHEMA,
        "scope": {
            "prime_limit": limit,
            "primes": primes,
            "prime_count": len(primes),
            "unordered_triangle_count": len(records),
        },
        "exact_laws": [
            "T_minus(p,q,r)=(q-p,r-q,r-p) satisfies d3=d1+d2",
            "T_minus is invariant under common translation and therefore loses absolute position",
            "T_plus(p,q,r)=(p+q,q+r,p+r) is injective on labeled triangles",
            "T_plus inverse is p=(s_pq+s_pr-s_qr)/2 and cyclic analogues",
            "the three sums have gcd 2 for all-odd prime triangles and gcd 1 for triangles containing axis 2",
            "T_plus never produces three prime values",
            "T_minus produces a distinct prime triangle iff the source is (2,5,7)",
            "the unique prime-triangle transition is (2,5,7)->(2,3,5), then the next difference triple is (1,2,3)",
        ],
        "finite_counts": {
            "difference_prime_count_distribution": {
                str(k): difference_prime_counts[k] for k in sorted(difference_prime_counts)
            },
            "sum_prime_count_distribution": {
                str(k): sum_prime_counts[k] for k in sorted(sum_prime_counts)
            },
            "difference_gcd_distribution": {
                str(k): difference_gcds[k] for k in sorted(difference_gcds)
            },
            "sum_gcd_distribution": {
                str(k): sum_gcds[k] for k in sorted(sum_gcds)
            },
            "prime_difference_triangle_count": len(prime_difference_targets),
            "detected_cycle_count": len(cycles),
        },
        "distinguished_dynamics": {
            "prime_difference_transitions": prime_difference_targets,
            "cycles": cycles,
        },
        "verification": {
            "all_difference_relations": all(
                row["difference_transform"]["relation_verified"] for row in records
            ),
            "all_sum_recoveries": all(
                row["sum_transform"]["recovery_verified"] for row in records
            ),
            "all_sum_gcd_rules": all(
                row["support_routing"]["sum_common_gcd_verified"] for row in records
            ),
            "no_sum_prime_triangles": not any(
                row["sum_transform"]["is_distinct_prime_triangle"] for row in records
            ),
            "unique_prime_difference_source": [
                item["source"] for item in prime_difference_targets
            ] == [[2, 5, 7]],
            "no_detected_cycles": not cycles,
        },
        "scientific_classification": (
            "exact elementary transform identities plus a finite deterministic atlas; "
            "no asymptotic, novelty, or major-conjecture claim"
        ),
    }


CSV_FIELDS = [
    "id", "p", "q", "r", "parity_class",
    "d_pq", "d_qr", "d_pr", "difference_gcd", "difference_primitive_shape",
    "difference_prime_count", "difference_prime_triangle_target",
    "s_pq", "s_qr", "s_pr", "sum_gcd", "sum_prime_count",
    "sum_recovery_verified", "difference_chain_length",
]


def csv_text(records: list[dict]) -> str:
    handle = io.StringIO(newline="")
    writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
    writer.writeheader()
    for row in records:
        p, q, r = row["source"]
        d = row["difference_transform"]
        s = row["sum_transform"]
        writer.writerow(
            {
                "id": row["id"], "p": p, "q": q, "r": r,
                "parity_class": row["parity_class"],
                "d_pq": d["labeled"][0], "d_qr": d["labeled"][1], "d_pr": d["labeled"][2],
                "difference_gcd": d["gcd"],
                "difference_primitive_shape": ":".join(map(str, d["primitive_shape"])),
                "difference_prime_count": d["prime_count"],
                "difference_prime_triangle_target": (
                    ":".join(map(str, d["prime_triangle_target"])) if d["prime_triangle_target"] else ""
                ),
                "s_pq": s["labeled"][0], "s_qr": s["labeled"][1], "s_pr": s["labeled"][2],
                "sum_gcd": s["gcd"], "sum_prime_count": s["prime_count"],
                "sum_recovery_verified": str(s["recovery_verified"]).lower(),
                "difference_chain_length": len(row["difference_chain"]),
            }
        )
    return handle.getvalue()


def build_atlas(limit: int = DEFAULT_LIMIT) -> tuple[str, str, dict]:
    primes, records = generate_records(limit)
    summary = summarize(limit, primes, records)
    return csv_text(records), json.dumps(summary, indent=2, sort_keys=True) + "\n", summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate PVG prime-triangle dynamics atlas")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    csv_payload, summary_payload, _ = build_atlas(args.limit)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"prime-triangle-dynamics-primes-le-{args.limit}"
    csv_path = args.output_dir / f"{stem}.csv"
    summary_path = args.output_dir / f"{stem}-summary.json"
    csv_path.write_text(csv_payload, encoding="utf-8", newline="")
    summary_path.write_text(summary_payload, encoding="utf-8")
    print(f"wrote {csv_path}")
    print(f"wrote {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
