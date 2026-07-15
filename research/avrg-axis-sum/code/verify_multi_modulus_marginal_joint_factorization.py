#!/usr/bin/env python3
"""Verify multi-modulus marginal/joint factorization and rank-gap identities."""

from __future__ import annotations

import itertools
import json
import numpy as np


def build_matrices(N: int, moduli: tuple[int, ...]):
    signatures = []
    for a in range(1, N):
        d = 2 * a - N
        signatures.append(tuple(d % r for r in moduli))

    sigma = sorted(set(signatures))
    sigma_index = {s: i for i, s in enumerate(sigma)}

    J = np.zeros((len(sigma), N - 1), dtype=int)
    for column, signature in enumerate(signatures):
        J[sigma_index[signature], column] = 1

    marginal_blocks = []
    used_sets = []
    for j, _ in enumerate(moduli):
        used = sorted({signature[j] for signature in sigma})
        used_sets.append(used)
        used_index = {u: i for i, u in enumerate(used)}
        D = np.zeros((len(used), N - 1), dtype=int)
        for column, signature in enumerate(signatures):
            D[used_index[signature[j]], column] = 1
        marginal_blocks.append(D)

    M = np.vstack(marginal_blocks)

    B = np.zeros((sum(map(len, used_sets)), len(sigma)), dtype=int)
    offset = 0
    for j, used in enumerate(used_sets):
        used_index = {u: i for i, u in enumerate(used)}
        for signature, column in sigma_index.items():
            B[offset + used_index[signature[j]], column] = 1
        offset += len(used)

    return J, M, B, len(sigma)


def main() -> None:
    cases = 0
    mismatches = 0
    max_rank_gap = 0

    test_families = [
        (3, range(2, 9), 25),
        (4, range(2, 7), 18),
    ]

    for k, modulus_range, n_max in test_families:
        for moduli in itertools.combinations(modulus_range, k):
            for N in range(2, n_max + 1):
                J, M, B, sigma_size = build_matrices(N, moduli)
                cases += 1

                rank_J = int(np.linalg.matrix_rank(J))
                rank_M = int(np.linalg.matrix_rank(M))
                rank_B = int(np.linalg.matrix_rank(B))
                rank_gap = rank_J - rank_M
                max_rank_gap = max(max_rank_gap, rank_gap)

                valid = (
                    np.array_equal(M, B @ J)
                    and rank_J == sigma_size
                    and rank_M == rank_B
                    and rank_gap == sigma_size - rank_B
                )
                if not valid:
                    mismatches += 1

    result = {
        "status": "PASS" if mismatches == 0 else "FAIL",
        "cases_checked": cases,
        "mismatch_count": mismatches,
        "maximum_observed_rank_gap": max_rank_gap,
        "scope": {
            "three_moduli": "all combinations from 2..8, 2 <= N <= 25",
            "four_moduli": "all combinations from 2..6, 2 <= N <= 18",
        },
        "checked_identities": [
            "M = B J",
            "rank(J) = number of realized signatures",
            "rank(M) = rank(B)",
            "rank(J)-rank(M) = dim ker(B)",
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
