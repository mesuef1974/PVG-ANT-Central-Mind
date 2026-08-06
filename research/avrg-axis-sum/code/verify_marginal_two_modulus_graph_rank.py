#!/usr/bin/env python3
"""Finite verifier for the two-modulus marginal graph rank theorem.

This script checks the proved identity

    rank M_{N;(r,s)} = |U| + |V| - c(G_{N;r,s})

and the full-period corollary.  Finite verification supports auditing but does
not replace the proof in MARGINAL-TWO-MODULUS-GRAPH-RANK-THEOREM-v1.1.md.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def difference_channel_matrix(N: int, r: int) -> np.ndarray:
    if N < 2:
        raise ValueError("N must be at least 2")
    if r < 1:
        raise ValueError("modulus must be positive")
    matrix = np.zeros((r, N - 1), dtype=float)
    for a in range(1, N):
        matrix[(2 * a - N) % r, a - 1] = 1.0
    return matrix


def graph_rank_prediction(N: int, r: int, s: int) -> int:
    q_r = r // math.gcd(2, r)
    q_s = s // math.gcd(2, s)

    used_left = sorted({a % q_r for a in range(1, N)})
    used_right = sorted({a % q_s for a in range(1, N)})
    left_index = {value: i for i, value in enumerate(used_left)}
    right_index = {value: i for i, value in enumerate(used_right)}

    vertex_count = len(used_left) + len(used_right)
    adjacency = [set() for _ in range(vertex_count)]

    for a in range(1, N):
        left = left_index[a % q_r]
        right = len(used_left) + right_index[a % q_s]
        adjacency[left].add(right)
        adjacency[right].add(left)

    seen: set[int] = set()
    component_count = 0
    for start in range(vertex_count):
        if start in seen or not adjacency[start]:
            continue
        component_count += 1
        seen.add(start)
        stack = [start]
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

    return vertex_count - component_count


def verify(max_N: int, max_modulus: int) -> tuple[int, int]:
    checked = 0
    full_period_checked = 0

    for N in range(2, max_N + 1):
        for r in range(1, max_modulus + 1):
            for s in range(1, max_modulus + 1):
                stacked = np.vstack(
                    [difference_channel_matrix(N, r), difference_channel_matrix(N, s)]
                )
                observed = int(np.linalg.matrix_rank(stacked))
                predicted = graph_rank_prediction(N, r, s)
                if observed != predicted:
                    raise AssertionError(
                        f"graph-rank mismatch N={N}, r={r}, s={s}: "
                        f"observed={observed}, predicted={predicted}"
                    )

                q_r = r // math.gcd(2, r)
                q_s = s // math.gcd(2, s)
                period = math.lcm(q_r, q_s)
                if N - 1 >= period:
                    full_period_predicted = q_r + q_s - math.gcd(q_r, q_s)
                    if observed != full_period_predicted:
                        raise AssertionError(
                            f"full-period mismatch N={N}, r={r}, s={s}: "
                            f"observed={observed}, predicted={full_period_predicted}"
                        )
                    full_period_checked += 1

                checked += 1

    return checked, full_period_checked


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-N", type=int, default=60)
    parser.add_argument("--max-modulus", type=int, default=30)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    checked, full_period_checked = verify(args.max_N, args.max_modulus)
    print(f"verified_parameter_triples={checked}")
    print(f"verified_full_period_cases={full_period_checked}")
    print("rank_mismatch_count=0")
    print("full_period_mismatch_count=0")
    print("status=PASS")


if __name__ == "__main__":
    main()
