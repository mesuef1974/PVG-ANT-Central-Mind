#!/usr/bin/env python3
"""Verify the exact multi-modulus marginal-rank theorem.

Checks, over many finite parameter families:
1. numerical rank of M_{N;r};
2. min(N-1, size of union of Fourier subgroups H_j);
3. inclusion-exclusion gcd formula for that union size;
4. numerical rank of J_{N;r} = min(N-1, lcm(q_j));
5. exact marginal/joint rank gap.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np


def effective_period(r: int) -> int:
    return r // math.gcd(2, r)


def lcm_many(values: tuple[int, ...]) -> int:
    out = 1
    for value in values:
        out = math.lcm(out, value)
    return out


def build_marginal_matrix(N: int, moduli: tuple[int, ...]) -> np.ndarray:
    n = N - 1
    rows: list[np.ndarray] = []
    for r in moduli:
        for d in range(r):
            row = np.zeros(n, dtype=float)
            for idx, a in enumerate(range(1, N)):
                if (2 * a - N - d) % r == 0:
                    row[idx] = 1.0
            if np.any(row):
                rows.append(row)
    return np.vstack(rows) if rows else np.zeros((0, n), dtype=float)


def build_joint_matrix(N: int, moduli: tuple[int, ...]) -> np.ndarray:
    signatures: dict[tuple[int, ...], list[int]] = {}
    for idx, a in enumerate(range(1, N)):
        sig = tuple((2 * a - N) % r for r in moduli)
        signatures.setdefault(sig, []).append(idx)
    matrix = np.zeros((len(signatures), N - 1), dtype=float)
    for row_idx, indices in enumerate(signatures.values()):
        matrix[row_idx, indices] = 1.0
    return matrix


def fourier_union_size(qs: tuple[int, ...]) -> int:
    L = lcm_many(qs)
    union: set[int] = set()
    for q in qs:
        union.update(range(0, L, L // q))
    return len(union)


def inclusion_exclusion_size(qs: tuple[int, ...]) -> int:
    total = 0
    indices = range(len(qs))
    for size in range(1, len(qs) + 1):
        sign = 1 if size % 2 == 1 else -1
        for subset in itertools.combinations(indices, size):
            g = 0
            for idx in subset:
                g = math.gcd(g, qs[idx])
            total += sign * g
    return total


def main() -> None:
    cases_checked = 0
    mismatch_count = 0
    max_rank_error = 0
    max_observed_gap = 0
    family_counts: dict[str, int] = {}
    examples: list[dict[str, object]] = []

    modulus_pools = {
        2: range(2, 13),
        3: range(2, 11),
        4: range(2, 9),
        5: range(2, 8),
    }

    for family_size, pool in modulus_pools.items():
        count = 0
        for moduli in itertools.combinations(pool, family_size):
            qs = tuple(effective_period(r) for r in moduli)
            L = lcm_many(qs)
            union_size = fourier_union_size(qs)
            ie_size = inclusion_exclusion_size(qs)
            for N in range(2, 31):
                M = build_marginal_matrix(N, moduli)
                J = build_joint_matrix(N, moduli)
                rank_m = int(np.linalg.matrix_rank(M, tol=1e-9))
                rank_j = int(np.linalg.matrix_rank(J, tol=1e-9))
                predicted_m = min(N - 1, union_size)
                predicted_j = min(N - 1, L)
                error = abs(rank_m - predicted_m)
                max_rank_error = max(max_rank_error, error)
                gap = rank_j - rank_m
                max_observed_gap = max(max_observed_gap, gap)

                ok = (
                    union_size == ie_size
                    and rank_m == predicted_m
                    and rank_j == predicted_j
                    and gap == predicted_j - predicted_m
                )
                if not ok:
                    mismatch_count += 1
                    if len(examples) < 20:
                        examples.append(
                            {
                                "N": N,
                                "moduli": moduli,
                                "effective_periods": qs,
                                "L": L,
                                "union_size": union_size,
                                "inclusion_exclusion_size": ie_size,
                                "rank_M": rank_m,
                                "predicted_rank_M": predicted_m,
                                "rank_J": rank_j,
                                "predicted_rank_J": predicted_j,
                            }
                        )
                cases_checked += 1
                count += 1
        family_counts[str(family_size)] = count

    result = {
        "theorem": "multi-modulus exact marginal rank via Fourier-subgroup union",
        "cases_checked": cases_checked,
        "family_case_counts": family_counts,
        "mismatch_count": mismatch_count,
        "maximum_rank_error": max_rank_error,
        "maximum_observed_rank_gap": max_observed_gap,
        "status": "PASS" if mismatch_count == 0 else "FAIL",
        "mismatch_examples": examples,
    }

    output = Path(__file__).resolve().parents[1] / "results" / "multi_modulus_exact_rank_fourier_union_verification_v1.1.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
