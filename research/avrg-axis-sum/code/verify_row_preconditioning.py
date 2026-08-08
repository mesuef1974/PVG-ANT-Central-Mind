#!/usr/bin/env python3
"""Verify information preservation and conditioning changes under row normalization.

The effective-period marginal block for q has one row per realized residue class of
(a-1) mod q and one column per fiber index a=1,...,N-1.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import numpy as np

TOL = 1e-10


def marginal_matrix(N: int, periods: Iterable[int]) -> tuple[np.ndarray, list[tuple[int, int]]]:
    n = N - 1
    blocks: list[np.ndarray] = []
    slices: list[tuple[int, int]] = []
    start = 0
    for q in periods:
        block = np.zeros((q, n), dtype=float)
        for column in range(n):
            block[column % q, column] = 1.0
        keep = np.linalg.norm(block, axis=1) > 0
        block = block[keep]
        blocks.append(block)
        slices.append((start, start + block.shape[0]))
        start += block.shape[0]
    return np.vstack(blocks), slices


def spectrum_metrics(A: np.ndarray) -> dict[str, float | int]:
    singular_values = np.linalg.svd(A, compute_uv=False)
    positive = singular_values[singular_values > TOL]
    if positive.size == 0:
        return {"rank": 0, "sigma_min_positive": 0.0, "sigma_max": 0.0, "kappa_positive": 0.0}
    return {
        "rank": int(positive.size),
        "sigma_min_positive": float(positive.min()),
        "sigma_max": float(positive.max()),
        "kappa_positive": float(positive.max() / positive.min()),
    }


def row_normalize(A: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(A, axis=1)
    if np.any(norms <= 0):
        raise ValueError("zero rows must be removed before row normalization")
    return A / norms[:, None]


def frobenius_block_normalize(A: np.ndarray, slices: list[tuple[int, int]]) -> np.ndarray:
    result = A.copy()
    for start, stop in slices:
        norm = np.linalg.norm(result[start:stop], ord="fro")
        result[start:stop] /= norm
    return result


def run() -> dict:
    cases = [
        (16, [5, 11]),
        (16, [7, 9]),
        (24, [5, 9, 11]),
        (24, [7, 9, 11]),
        (30, [5, 7, 9, 11]),
        (30, [7, 8, 9, 11, 12]),
    ]
    records = []
    rank_mismatches = 0
    kernel_projector_errors = []
    frobenius_condition_errors = []

    for N, periods in cases:
        A, slices = marginal_matrix(N, periods)
        row_A = row_normalize(A)
        fro_A = frobenius_block_normalize(A, slices)

        raw = spectrum_metrics(A)
        row = spectrum_metrics(row_A)
        fro = spectrum_metrics(fro_A)

        if raw["rank"] != row["rank"] or raw["rank"] != fro["rank"]:
            rank_mismatches += 1

        # Orthogonal projectors onto the numerical nullspaces must agree.
        def null_projector(X: np.ndarray) -> np.ndarray:
            _, s, vh = np.linalg.svd(X, full_matrices=True)
            rank = int(np.sum(s > TOL))
            Z = vh[rank:].T
            return Z @ Z.T

        kernel_error = float(np.linalg.norm(null_projector(A) - null_projector(row_A), ord=2))
        kernel_projector_errors.append(kernel_error)
        frobenius_condition_errors.append(abs(raw["kappa_positive"] - fro["kappa_positive"]))

        records.append(
            {
                "N": N,
                "periods": periods,
                "raw": raw,
                "row_normalized": row,
                "frobenius_block_normalized": fro,
                "row_condition_ratio": row["kappa_positive"] / raw["kappa_positive"],
                "kernel_projector_error": kernel_error,
            }
        )

    return {
        "schema": "pvg.row-preconditioning.verification.v1",
        "status": "PASS" if rank_mismatches == 0 and max(kernel_projector_errors) < 1e-8 else "FAIL",
        "tolerance": TOL,
        "cases_checked": len(records),
        "rank_mismatches": rank_mismatches,
        "maximum_kernel_projector_error": max(kernel_projector_errors),
        "maximum_frobenius_block_kappa_error": max(frobenius_condition_errors),
        "records": records,
        "notes": [
            "Positive diagonal left scaling preserves the exact kernel and rank algebraically.",
            "Numerical projector comparison is a finite floating-point cross-check.",
            "Frobenius block normalization is a common scalar in this model and leaves kappa unchanged.",
            "No global optimality claim is made for row normalization.",
        ],
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).resolve().parents[1] / "results" / "row_preconditioning_verification_v1.1.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
