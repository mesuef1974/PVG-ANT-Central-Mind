#!/usr/bin/env python3
"""Generate a deterministic PVG atlas for primitive edges between prime axes.

For primes p < q, a primitive horizontal edge above a common base g is

    gp  <->  gq.

Its reduced additive and subtractive transitions are p+q and q-p.  This tool
records their prime supports, omega/Omega values, level defects

    kappa_+(p,q) = Omega(p+q) - 1
    kappa_-(p,q) = Omega(q-p) - 1,

and the exact bridge between the multiplicative axis ratio q/p and the
normalized additive gap (q-p)/(q+p).

The committed default atlas is finite and diagnostic: all unordered prime
pairs p < q <= 100.  No asymptotic, novelty, factorization-speedup, Goldbach,
RH, or GRH claim is made.
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
from typing import Iterable, Mapping

try:
    from .pvg_inverse_geometry import factorint_64
except ImportError:
    from pvg_inverse_geometry import factorint_64  # type: ignore

SCHEMA = "PVG-PRIME-PAIR-EDGE-ATLAS-001"
DEFAULT_LIMIT = 100


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            start = p * p
            count = ((limit - start) // p) + 1
            sieve[start : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return factorint_64(n) == {n: 1}


def factorization(n: int) -> dict[int, int]:
    if n == 1:
        return {}
    return dict(sorted(factorint_64(n).items()))


def factorization_text(factors: Mapping[int, int]) -> str:
    if not factors:
        return "1"
    return "*".join(str(p) if a == 1 else f"{p}^{a}" for p, a in factors.items())


def fraction_payload(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": f"{value.numerator}/{value.denominator}",
    }


def transition_payload(value: int, axes: tuple[int, int]) -> dict:
    factors = factorization(value)
    support = list(factors)
    omega = len(support)
    Omega = sum(factors.values())
    kappa = Omega - 1
    relation = "down" if kappa < 0 else "preserved" if kappa == 0 else "up"
    axis_set = set(axes)
    return {
        "value": value,
        "factorization": [
            {"prime": p, "valuation": a} for p, a in factors.items()
        ],
        "factorization_text": factorization_text(factors),
        "support": support,
        "omega": omega,
        "Omega": Omega,
        "kappa": kappa,
        "level_relation": relation,
        "reused_edge_axes": sorted(axis_set.intersection(support)),
        "new_reduced_axes": sorted(set(support).difference(axis_set)),
        "contains_axis_2": 2 in factors,
    }


def edge_record(p: int, q: int, *, prime_index_gap: int, record_id: int) -> dict:
    if not (p < q and is_prime(p) and is_prime(q)):
        raise ValueError("edge_record requires distinct primes p < q")

    edge_sum = p + q
    edge_gap = q - p
    plus = transition_payload(edge_sum, (p, q))
    minus = transition_payload(edge_gap, (p, q))
    ratio = Fraction(q, p)
    normalized_gap = Fraction(edge_gap, edge_sum)
    support_intersection = sorted(set(plus["support"]).intersection(minus["support"]))

    return {
        "id": f"PP-{record_id:03d}",
        "p": p,
        "q": q,
        "axis_ratio": fraction_payload(ratio),
        "gap": edge_gap,
        "sum": edge_sum,
        "normalized_gap": fraction_payload(normalized_gap),
        "ratio_gap_bridge": {
            "identity": "(q-p)/(q+p)=(q/p-1)/(q/p+1)",
            "verified": normalized_gap == (ratio - 1) / (ratio + 1),
        },
        "prime_index_gap": prime_index_gap,
        "consecutive_prime_axes": prime_index_gap == 1,
        "twin_axis_pair": edge_gap == 2,
        "parity_class": "contains_axis_2" if p == 2 else "odd_odd",
        "sum_transition": plus,
        "difference_transition": minus,
        "transition_coupling": {
            "gcd_sum_difference": gcd(edge_sum, edge_gap),
            "support_intersection": support_intersection,
            "expected_gcd": 1 if p == 2 else 2,
            "gcd_law_verified": gcd(edge_sum, edge_gap) == (1 if p == 2 else 2),
        },
        "sum_level_preserved": plus["kappa"] == 0,
        "difference_level_preserved": minus["kappa"] == 0,
        "both_level_preserved": plus["kappa"] == 0 and minus["kappa"] == 0,
        "reduced_transition_support_disjoint_from_edge_axes": (
            not plus["reused_edge_axes"] and not minus["reused_edge_axes"]
        ),
    }


def generate_records(limit: int = DEFAULT_LIMIT) -> tuple[list[int], list[dict]]:
    primes = primes_up_to(limit)
    index = {p: i for i, p in enumerate(primes)}
    records = [
        edge_record(
            p,
            q,
            prime_index_gap=index[q] - index[p],
            record_id=record_id,
        )
        for record_id, (p, q) in enumerate(combinations(primes, 2), 1)
    ]
    return primes, records


def pair_list(records: Iterable[dict], predicate) -> list[list[int]]:
    return [[row["p"], row["q"]] for row in records if predicate(row)]


def defect_examples(records: list[dict], transition: str) -> dict:
    key = f"{transition}_transition"
    maximum = max(row[key]["kappa"] for row in records)
    examples = [
        {
            "p": row["p"],
            "q": row["q"],
            "value": row[key]["value"],
            "factorization": row[key]["factorization_text"],
        }
        for row in records
        if row[key]["kappa"] == maximum
    ]
    return {"maximum": maximum, "examples": examples}


def summarize(limit: int, primes: list[int], records: list[dict]) -> dict:
    plus_kappa = Counter(row["sum_transition"]["kappa"] for row in records)
    minus_kappa = Counter(row["difference_transition"]["kappa"] for row in records)
    plus_relation = Counter(row["sum_transition"]["level_relation"] for row in records)
    minus_relation = Counter(
        row["difference_transition"]["level_relation"] for row in records
    )

    return {
        "schema": SCHEMA,
        "scope": {
            "prime_limit": limit,
            "primes": primes,
            "prime_count": len(primes),
            "unordered_pair_count": len(records),
        },
        "definitions": {
            "primitive_edge": "gp <-> gq for distinct primes p<q",
            "axis_ratio": "q/p",
            "normalized_gap": "(q-p)/(q+p)",
            "kappa_plus": "Omega(p+q)-1",
            "kappa_minus": "Omega(q-p)-1",
        },
        "exact_laws": [
            "axis ratio and normalized gap satisfy (q-p)/(q+p)=(q/p-1)/(q/p+1)",
            "gcd(p+q,q-p)=1 when p=2 and equals 2 when p,q are odd",
            "gcd(pq,p+q)=gcd(pq,q-p)=1",
            "sum-level preservation holds iff p=2 and q+2 is prime",
            "difference-level preservation holds iff q-p is prime",
            "for odd p,q, difference-level preservation is equivalent to q-p=2",
            "both sum and difference preserve the level only for the axis pair (2,5)",
            "for odd p,q, both reduced transitions contain axis 2",
            "for p=2, both reduced transitions are odd and exclude axis 2",
            "kappa_plus and kappa_minus depend only on the prime-axis pair, not on the common base g",
        ],
        "finite_counts": {
            "parity_class": dict(sorted(Counter(row["parity_class"] for row in records).items())),
            "sum_level_relation": dict(sorted(plus_relation.items())),
            "difference_level_relation": dict(sorted(minus_relation.items())),
            "kappa_plus_distribution": {
                str(k): plus_kappa[k] for k in sorted(plus_kappa)
            },
            "kappa_minus_distribution": {
                str(k): minus_kappa[k] for k in sorted(minus_kappa)
            },
        },
        "distinguished_pairs": {
            "sum_level_preserved": pair_list(records, lambda row: row["sum_level_preserved"]),
            "difference_level_preserved": pair_list(
                records, lambda row: row["difference_level_preserved"]
            ),
            "both_level_preserved": pair_list(
                records, lambda row: row["both_level_preserved"]
            ),
            "difference_level_down": pair_list(
                records,
                lambda row: row["difference_transition"]["level_relation"] == "down",
            ),
        },
        "maximum_observed_defects": {
            "sum": defect_examples(records, "sum"),
            "difference": defect_examples(records, "difference"),
        },
        "scientific_classification": (
            "exact elementary identities plus a finite deterministic diagnostic atlas; "
            "no asymptotic, novelty, or major-conjecture claim"
        ),
    }


CSV_FIELDS = [
    "id",
    "p",
    "q",
    "ratio",
    "normalized_gap",
    "prime_index_gap",
    "consecutive_prime_axes",
    "twin_axis_pair",
    "parity_class",
    "sum",
    "sum_factorization",
    "sum_omega",
    "sum_Omega",
    "kappa_plus",
    "sum_level_relation",
    "difference",
    "difference_factorization",
    "difference_omega",
    "difference_Omega",
    "kappa_minus",
    "difference_level_relation",
    "gcd_sum_difference",
    "transition_support_intersection",
    "both_level_preserved",
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
                "ratio": row["axis_ratio"]["text"],
                "normalized_gap": row["normalized_gap"]["text"],
                "prime_index_gap": row["prime_index_gap"],
                "consecutive_prime_axes": str(row["consecutive_prime_axes"]).lower(),
                "twin_axis_pair": str(row["twin_axis_pair"]).lower(),
                "parity_class": row["parity_class"],
                "sum": row["sum_transition"]["value"],
                "sum_factorization": row["sum_transition"]["factorization_text"],
                "sum_omega": row["sum_transition"]["omega"],
                "sum_Omega": row["sum_transition"]["Omega"],
                "kappa_plus": row["sum_transition"]["kappa"],
                "sum_level_relation": row["sum_transition"]["level_relation"],
                "difference": row["difference_transition"]["value"],
                "difference_factorization": row["difference_transition"]["factorization_text"],
                "difference_omega": row["difference_transition"]["omega"],
                "difference_Omega": row["difference_transition"]["Omega"],
                "kappa_minus": row["difference_transition"]["kappa"],
                "difference_level_relation": row["difference_transition"]["level_relation"],
                "gcd_sum_difference": row["transition_coupling"]["gcd_sum_difference"],
                "transition_support_intersection": "*".join(
                    str(p) for p in row["transition_coupling"]["support_intersection"]
                )
                or "none",
                "both_level_preserved": str(row["both_level_preserved"]).lower(),
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
    csv_path = output_dir / f"prime-pair-edge-atlas-primes-le-{limit}.csv"
    summary_path = output_dir / f"prime-pair-edge-atlas-primes-le-{limit}-summary.json"
    csv_path.write_text(csv_payload, encoding="utf-8", newline="")
    summary_path.write_text(summary_payload, encoding="utf-8")
    return csv_path, summary_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--print-summary", action="store_true", help="print deterministic JSON summary"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.limit < 3:
        raise SystemExit("--limit must be at least 3")
    csv_payload, summary_payload, summary = build_atlas(args.limit)
    if args.output_dir is not None:
        csv_path, summary_path = write_atlas(args.output_dir, args.limit)
        print(f"wrote {csv_path}")
        print(f"wrote {summary_path}")
    if args.print_summary or args.output_dir is None:
        print(summary_payload, end="")
    assert summary["scope"]["unordered_pair_count"] == csv_payload.count("\n") - 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
