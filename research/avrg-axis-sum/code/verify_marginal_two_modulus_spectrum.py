#!/usr/bin/env python3
"""Finite verification for the marginal two-modulus spectral theorems.

The theorem is proved symbolically in
MARGINAL-TWO-MODULUS-SPECTRUM-CONDITIONING-v1.1.md.
This script checks finite parameter ranges only.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def marginal_matrix(N: int, r: int, s: int) -> np.ndarray:
    matrix = np.zeros((r + s, N - 1), dtype=float)
    for a in range(1, N):
        d_r = (2 * a - N) % r
        d_s = (2 * a - N) % s
        matrix[d_r, a - 1] = 1.0
        matrix[r + d_s, a - 1] = 1.0
    return matrix


def graph_laplacians(N: int, r: int, s: int) -> tuple[np.ndarray, np.ndarray]:
    adjacency = np.zeros((r + s, r + s), dtype=float)
    degree = np.zeros(r + s, dtype=float)
    for a in range(1, N):
        u = (2 * a - N) % r
        v = r + (2 * a - N) % s
        adjacency[u, v] += 1.0
        adjacency[v, u] += 1.0
        degree[u] += 1.0
        degree[v] += 1.0
    diagonal = np.diag(degree)
    return diagonal + adjacency, diagonal - adjacency


def positive_singular_values(matrix: np.ndarray, tol: float = 1e-9) -> np.ndarray:
    values = np.linalg.svd(matrix, compute_uv=False)
    return np.sort(values[values > tol])


def predicted_full_period_spectrum(r: int, s: int, t: int) -> np.ndarray:
    q_r = r // math.gcd(2, r)
    q_s = s // math.gcd(2, s)
    g = math.gcd(q_r, q_s)
    m = q_r // g
    n = q_s // g

    values: list[float] = []
    values.extend([math.sqrt(t * (m + n))] * g)
    values.extend([math.sqrt(t * n)] * (g * (m - 1)))
    values.extend([math.sqrt(t * m)] * (g * (n - 1)))
    return np.sort(np.asarray(values, dtype=float))


def verify(max_modulus: int, max_N: int, max_periods: int) -> dict[str, float | int]:
    general_cases = 0
    full_period_cases = 0
    maximum_error = 0.0

    for r in range(1, max_modulus + 1):
        for s in range(1, max_modulus + 1):
            sign = np.diag([1.0] * r + [-1.0] * s)

            for N in range(2, max_N + 1):
                matrix = marginal_matrix(N, r, s)
                signless, ordinary = graph_laplacians(N, r, s)

                maximum_error = max(
                    maximum_error,
                    float(np.max(np.abs(matrix @ matrix.T - signless))),
                    float(np.max(np.abs(sign @ signless @ sign - ordinary))),
                    float(
                        np.max(
                            np.abs(
                                np.sort(np.linalg.eigvalsh(signless))
                                - np.sort(np.linalg.eigvalsh(ordinary))
                            )
                        )
                    ),
                )
                general_cases += 1

            q_r = r // math.gcd(2, r)
            q_s = s // math.gcd(2, s)
            period = math.lcm(q_r, q_s)
            for t in range(1, max_periods + 1):
                N = 1 + t * period
                observed = positive_singular_values(marginal_matrix(N, r, s))
                expected = predicted_full_period_spectrum(r, s, t)
                if observed.shape != expected.shape:
                    raise AssertionError(
                        f"multiplicity mismatch for r={r}, s={s}, t={t}: "
                        f"observed={observed.shape}, expected={expected.shape}"
                    )
                error = float(np.max(np.abs(observed - expected))) if observed.size else 0.0
                maximum_error = max(maximum_error, error)
                if error > 1e-8:
                    raise AssertionError(
                        f"spectral mismatch for r={r}, s={s}, t={t}: error={error}"
                    )
                full_period_cases += 1

    return {
        "general_cases": general_cases,
        "full_period_cases": full_period_cases,
        "maximum_absolute_error": maximum_error,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-modulus", type=int, default=30)
    parser.add_argument("--max-N", type=int, default=41)
    parser.add_argument("--max-periods", type=int, default=5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = verify(args.max_modulus, args.max_N, args.max_periods)
    for key, value in result.items():
        print(f"{key}={value}")
    print("status=PASS")


if __name__ == "__main__":
    main()
