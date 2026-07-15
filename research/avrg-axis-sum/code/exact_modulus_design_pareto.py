#!/usr/bin/env python3
"""Exact Pareto optimizer for reduced modulus-selection designs.

Candidates are reduced periods q = r/gcd(2,r). The measurement cost defaults
to q. For each subset S, the rank objective is

    R_N(S) = min(N-1, |union_{q in S} H_q|),

where H_q is the order-q Fourier subgroup in Z/LZ and
L = lcm(S).

The script exhaustively enumerates candidate subsets, reports the Pareto
frontier, the best rank for every budget, and the minimum-cost full-rank
families. It is intended for small/medium candidate pools and provides an
exact certificate against which heuristics can be tested.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import lcm
from pathlib import Path
from typing import Iterable, Sequence


def fourier_union_size(periods: Sequence[int]) -> int:
    if not periods:
        return 0
    ambient = 1
    for q in periods:
        if q < 1:
            raise ValueError("periods must be positive")
        ambient = lcm(ambient, q)
    frequencies: set[int] = set()
    for q in periods:
        step = ambient // q
        frequencies.update(range(0, ambient, step))
    return len(frequencies)


def rank_value(N: int, periods: Sequence[int]) -> int:
    if N < 2:
        raise ValueError("N must be at least 2")
    return min(N - 1, fourier_union_size(periods))


def subsets(items: Sequence[int]) -> Iterable[tuple[int, ...]]:
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def exact_design_report(N: int, candidates: Sequence[int]) -> dict:
    candidates = tuple(sorted(set(candidates)))
    designs: list[dict] = []
    for design in subsets(candidates):
        cost = sum(design)
        rank = rank_value(N, design)
        designs.append({"design": list(design), "cost": cost, "rank": rank})

    max_budget = sum(candidates)
    best_by_budget: list[dict] = []
    for budget in range(max_budget + 1):
        feasible = [row for row in designs if row["cost"] <= budget]
        best_rank = max(row["rank"] for row in feasible)
        minimum_cost = min(
            row["cost"] for row in feasible if row["rank"] == best_rank
        )
        optimal = [
            row["design"]
            for row in feasible
            if row["rank"] == best_rank and row["cost"] == minimum_cost
        ]
        best_by_budget.append(
            {
                "budget": budget,
                "best_rank": best_rank,
                "minimum_cost_for_best_rank": minimum_cost,
                "designs": optimal,
            }
        )

    pareto: list[dict] = []
    previous_rank = -1
    for row in best_by_budget:
        if row["best_rank"] > previous_rank:
            pareto.append(
                {
                    "cost": row["minimum_cost_for_best_rank"],
                    "rank": row["best_rank"],
                    "designs": row["designs"],
                }
            )
            previous_rank = row["best_rank"]

    full_rank_rows = [row for row in designs if row["rank"] == N - 1]
    full_rank = None
    if full_rank_rows:
        minimum_cost = min(row["cost"] for row in full_rank_rows)
        full_rank = {
            "minimum_cost": minimum_cost,
            "designs": [
                row["design"]
                for row in full_rank_rows
                if row["cost"] == minimum_cost
            ],
        }

    return {
        "N": N,
        "candidate_periods": list(candidates),
        "cost_model": "cost(q)=q",
        "designs_enumerated": len(designs),
        "pareto_frontier": pareto,
        "best_by_budget": best_by_budget,
        "minimum_cost_full_rank": full_rank,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--candidates", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = exact_design_report(args.N, args.candidates)
    text = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
