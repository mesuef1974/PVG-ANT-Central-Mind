#!/usr/bin/env python3
"""Finite verification for the two-modulus marginal rank/nullity formulas.

This script checks, for a finite parameter box, that the stacked marginal
matrix has rank |U|+|V|-c(G) and nullity |E|-|U|-|V|+c(G), where G is the
associated realized bipartite residue-coupling multigraph.

It supports, but does not replace, the symbolic proofs in:
- MARGINAL-TWO-MODULUS-GRAPH-RANK-THEOREM-v1.1.md
- MARGINAL-TWO-MODULUS-KERNEL-CYCLE-BASIS-v1.1.md
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque

import numpy as np


def graph_data(N: int, r: int, s: int):
    if N < 2:
        raise ValueError("N must be at least 2")
    if r < 1 or s < 1:
        raise ValueError("moduli must be positive")

    edges = []
    left = set()
    right = set()
    for a in range(1, N):
        u = (2 * a - N) % r
        v = (2 * a - N) % s
        edges.append((u, v))
        left.add(u)
        right.add(v)
    return sorted(left), sorted(right), edges


def marginal_matrix(N: int, r: int, s: int) -> np.ndarray:
    left, right, edges = graph_data(N, r, s)
    left_index = {u: i for i, u in enumerate(left)}
    right_index = {v: len(left) + i for i, v in enumerate(right)}

    matrix = np.zeros((len(left) + len(right), len(edges)), dtype=float)
    for j, (u, v) in enumerate(edges):
        matrix[left_index[u], j] = 1.0
        matrix[right_index[v], j] = 1.0
    return matrix


def component_count(N: int, r: int, s: int) -> int:
    left, right, edges = graph_data(N, r, s)
    adjacency = defaultdict(list)
    vertices = [("L", u) for u in left] + [("R", v) for v in right]

    for u, v in edges:
        x = ("L", u)
        y = ("R", v)
        adjacency[x].append(y)
        adjacency[y].append(x)

    seen = set()
    components = 0
    for start in vertices:
        if start in seen:
            continue
        components += 1
        seen.add(start)
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
    return components


def verify(max_N: int, max_modulus: int) -> tuple[int, int, int]:
    cases = 0
    rank_mismatches = 0
    nullity_mismatches = 0

    for N in range(2, max_N + 1):
        for r in range(1, max_modulus + 1):
            for s in range(1, max_modulus + 1):
                left, right, edges = graph_data(N, r, s)
                matrix = marginal_matrix(N, r, s)
                observed_rank = int(np.linalg.matrix_rank(matrix))
                observed_nullity = len(edges) - observed_rank
                components = component_count(N, r, s)

                expected_rank = len(left) + len(right) - components
                expected_nullity = (
                    len(edges) - len(left) - len(right) + components
                )

                if observed_rank != expected_rank:
                    rank_mismatches += 1
                    raise AssertionError(
                        "rank mismatch "
                        f"N={N}, r={r}, s={s}: "
                        f"observed={observed_rank}, expected={expected_rank}"
                    )

                if observed_nullity != expected_nullity:
                    nullity_mismatches += 1
                    raise AssertionError(
                        "nullity mismatch "
                        f"N={N}, r={r}, s={s}: "
                        f"observed={observed_nullity}, expected={expected_nullity}"
                    )

                cases += 1

    return cases, rank_mismatches, nullity_mismatches


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-N", type=int, default=35)
    parser.add_argument("--max-modulus", type=int, default=16)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases, rank_bad, nullity_bad = verify(args.max_N, args.max_modulus)
    print(f"verified_cases={cases}")
    print(f"rank_mismatches={rank_bad}")
    print(f"nullity_mismatches={nullity_bad}")
    print("status=PASS")


if __name__ == "__main__":
    main()
