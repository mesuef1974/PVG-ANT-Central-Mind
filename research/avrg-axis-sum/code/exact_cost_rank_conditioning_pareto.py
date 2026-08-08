#!/usr/bin/env python3
"""Exact finite Pareto optimizer for PVG marginal-modulus designs.

Enumerates all subsets of a finite reduced-period pool and computes
(cost, rank, smallest positive singular value, positive condition number).

This is an exponential certificate generator, not a scalable solver.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np


def marginal_matrix(N: int, periods: Iterable[int]) -> np.ndarray:
    cols = N - 1
    blocks: list[np.ndarray] = []
    for q in periods:
        if q < 1:
            raise ValueError("Periods must be positive integers")
        block = np.zeros((q, cols), dtype=float)
        for a in range(1, N):
            block[(2 * a - N) % q, a - 1] = 1.0
        blocks.append(block)
    return np.vstack(blocks) if blocks else np.zeros((0, cols), dtype=float)


def design_metrics(N: int, periods: tuple[int, ...], tol: float) -> dict:
    matrix = marginal_matrix(N, periods)
    cost = sum(periods)
    if matrix.size == 0:
        return {
            "periods": list(periods), "cost": cost, "rank": 0,
            "sigma_min_positive": 0.0, "sigma_max": 0.0,
            "kappa_positive": None,
        }
    singular = np.linalg.svd(matrix, compute_uv=False)
    positive = singular[singular > tol]
    rank = int(positive.size)
    if rank == 0:
        sigma_min = sigma_max = 0.0
        kappa = None
    else:
        sigma_max = float(positive[0])
        sigma_min = float(positive[-1])
        kappa = sigma_max / sigma_min
    return {
        "periods": list(periods), "cost": cost, "rank": rank,
        "sigma_min_positive": sigma_min, "sigma_max": sigma_max,
        "kappa_positive": kappa,
    }


def dominates(a: dict, b: dict, eps: float = 1e-12) -> bool:
    ka = math.inf if a["kappa_positive"] is None else a["kappa_positive"]
    kb = math.inf if b["kappa_positive"] is None else b["kappa_positive"]
    weak = a["cost"] <= b["cost"] and a["rank"] >= b["rank"] and ka <= kb + eps
    strict = a["cost"] < b["cost"] or a["rank"] > b["rank"] or ka < kb - eps
    return weak and strict


def solve(N: int, candidates: list[int], tol: float) -> dict:
    designs: list[dict] = []
    for mask in range(1 << len(candidates)):
        periods = tuple(candidates[i] for i in range(len(candidates)) if mask & (1 << i))
        designs.append(design_metrics(N, periods, tol))

    frontier = [d for d in designs if not any(dominates(x, d) for x in designs if x is not d)]
    frontier.sort(key=lambda d: (d["cost"], -d["rank"], math.inf if d["kappa_positive"] is None else d["kappa_positive"]))

    full = [d for d in designs if d["rank"] == N - 1]
    minimum_cost = min((d["cost"] for d in full), default=None)
    minimum_cost_full = [d for d in full if d["cost"] == minimum_cost]
    best_conditioned = min(
        full,
        key=lambda d: (math.inf if d["kappa_positive"] is None else d["kappa_positive"], d["cost"]),
        default=None,
    )

    return {
        "N": N,
        "candidate_periods": candidates,
        "tolerance": tol,
        "designs_enumerated": len(designs),
        "pareto_frontier": frontier,
        "minimum_cost_full_rank": minimum_cost,
        "minimum_cost_full_rank_designs": minimum_cost_full,
        "best_conditioned_full_rank_design": best_conditioned,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--candidates", type=int, nargs="+", required=True)
    parser.add_argument("--tol", type=float, default=1e-10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.N < 2:
        raise ValueError("N must be at least 2")
    candidates = sorted(set(args.candidates))
    result = solve(args.N, candidates, args.tol)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
