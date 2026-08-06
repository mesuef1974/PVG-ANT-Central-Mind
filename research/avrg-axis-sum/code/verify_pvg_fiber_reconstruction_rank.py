#!/usr/bin/env python3
"""Verify the exact rank formula for PVG difference-channel reconstruction.

Finite verification only.  The theorem itself is proved in
PVG-FIBER-RECONSTRUCTION-RANK-THEOREM-001.md.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def difference_channel_matrix(N: int, r: int) -> np.ndarray:
    if N < 2:
        raise ValueError("N must be at least 2")
    if r < 1:
        raise ValueError("r must be positive")
    matrix = np.zeros((r, N - 1), dtype=float)
    for a in range(1, N):
        d = (2 * a - N) % r
        matrix[d, a - 1] = 1.0
    return matrix


def predicted_rank(N: int, r: int) -> int:
    return min(N - 1, r // math.gcd(2, r))


def verify(max_N: int, max_r: int) -> tuple[int, float]:
    case_count = 0
    maximum_rank_error = 0.0
    for N in range(2, max_N + 1):
        for r in range(1, max_r + 1):
            matrix = difference_channel_matrix(N, r)
            observed = int(np.linalg.matrix_rank(matrix))
            expected = predicted_rank(N, r)
            error = abs(observed - expected)
            maximum_rank_error = max(maximum_rank_error, float(error))
            if observed != expected:
                raise AssertionError(
                    f"rank mismatch for N={N}, r={r}: observed={observed}, expected={expected}"
                )

            # The zero Fourier mode / sum row is already in the row span.
            sum_row = np.ones((1, N - 1), dtype=float)
            augmented = np.vstack([matrix, sum_row])
            if np.linalg.matrix_rank(augmented) != observed:
                raise AssertionError(f"sum row increased rank for N={N}, r={r}")

            # For odd r >= N-1, exact pointwise recovery is immediate.
            if r % 2 == 1 and r >= N - 1:
                if observed != N - 1:
                    raise AssertionError(f"injectivity failed for N={N}, r={r}")
                test_weight = np.arange(1, N, dtype=float)
                channels = matrix @ test_weight
                recovered = np.empty_like(test_weight)
                for a in range(1, N):
                    recovered[a - 1] = channels[(2 * a - N) % r]
                if not np.array_equal(recovered, test_weight):
                    raise AssertionError(f"recovery failed for N={N}, r={r}")

            case_count += 1
    return case_count, maximum_rank_error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-N", type=int, default=100)
    parser.add_argument("--max-r", type=int, default=100)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases, maximum_error = verify(args.max_N, args.max_r)
    print(f"verified_cases={cases}")
    print(f"maximum_rank_error={maximum_error:.1f}")
    print("status=PASS")


if __name__ == "__main__":
    main()
