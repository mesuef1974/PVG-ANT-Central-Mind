#!/usr/bin/env python3
"""Bounded diagonal left-preconditioner search for PVG marginal operators.

The optimization is numerical. It returns a computational upper bound on the
best condition number under a declared log-weight spread bound.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
from scipy.optimize import minimize


@dataclass(frozen=True)
class SpectrumSummary:
    rank: int
    sigma_min_positive: float
    sigma_max: float
    kappa_positive: float


def build_marginal_matrix(N: int, periods: Sequence[int]) -> np.ndarray:
    if N < 2:
        raise ValueError("N must be at least 2")
    if not periods or any(q < 1 for q in periods):
        raise ValueError("periods must be a nonempty sequence of positive integers")

    rows: list[np.ndarray] = []
    for q in periods:
        for residue in range(q):
            row = np.zeros(N - 1, dtype=float)
            for a in range(1, N):
                if (2 * a - N) % q == residue:
                    row[a - 1] = 1.0
            if np.any(row):
                rows.append(row)
    return np.vstack(rows)


def spectrum_summary(matrix: np.ndarray, tolerance: float = 1e-10) -> SpectrumSummary:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    positive = singular_values[singular_values > tolerance]
    if positive.size == 0:
        return SpectrumSummary(0, 0.0, 0.0, math.inf)
    return SpectrumSummary(
        rank=int(positive.size),
        sigma_min_positive=float(positive[-1]),
        sigma_max=float(positive[0]),
        kappa_positive=float(positive[0] / positive[-1]),
    )


def row_normalize(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1)
    if np.any(norms == 0):
        raise ValueError("zero rows must be removed before row normalization")
    return matrix / norms[:, None]


def centered(log_weights: np.ndarray) -> np.ndarray:
    return log_weights - np.mean(log_weights)


def optimize(
    matrix: np.ndarray,
    tau: float,
    starts: int,
    seed: int,
    tolerance: float,
) -> tuple[np.ndarray, SpectrumSummary, dict]:
    if tau <= 0:
        raise ValueError("tau must be positive")
    if starts < 1:
        raise ValueError("starts must be positive")

    rng = np.random.default_rng(seed)
    best: tuple[float, np.ndarray, SpectrumSummary, dict] | None = None

    def objective(raw: np.ndarray) -> float:
        logs = centered(raw)
        scaled = np.exp(logs)[:, None] * matrix
        return math.log(spectrum_summary(scaled, tolerance).kappa_positive)

    for start_index in range(starts):
        if start_index == 0:
            x0 = np.zeros(matrix.shape[0], dtype=float)
        else:
            x0 = rng.uniform(-min(tau, 0.25), min(tau, 0.25), matrix.shape[0])

        result = minimize(
            objective,
            x0,
            method="L-BFGS-B",
            bounds=[(-tau, tau)] * matrix.shape[0],
            options={"maxiter": 4000, "ftol": 1e-13, "gtol": 1e-9},
        )
        logs = centered(np.asarray(result.x, dtype=float))
        scaled = np.exp(logs)[:, None] * matrix
        summary = spectrum_summary(scaled, tolerance)
        record = {
            "start_index": start_index,
            "success": bool(result.success),
            "message": str(result.message),
            "iterations": int(result.nit),
            "objective_log_kappa": float(math.log(summary.kappa_positive)),
        }
        candidate = (summary.kappa_positive, logs, summary, record)
        if best is None or candidate[0] < best[0]:
            best = candidate

    assert best is not None
    return best[1], best[2], best[3]


def run_case(N: int, periods: Sequence[int], tau: float, starts: int, seed: int, tolerance: float) -> dict:
    matrix = build_marginal_matrix(N, periods)
    raw = spectrum_summary(matrix, tolerance)
    normalized = spectrum_summary(row_normalize(matrix), tolerance)
    logs, optimized, optimizer_record = optimize(matrix, tau, starts, seed, tolerance)

    return {
        "N": N,
        "periods": list(periods),
        "matrix_shape": list(matrix.shape),
        "tau": tau,
        "starts": starts,
        "raw": asdict(raw),
        "row_normalized": asdict(normalized),
        "bounded_optimized": asdict(optimized),
        "log_weight_min": float(np.min(logs)),
        "log_weight_max": float(np.max(logs)),
        "log_weight_sum": float(np.sum(logs)),
        "optimizer": optimizer_record,
        "classification": "computational upper bound on bounded optimum",
    }


def parse_periods(text: str) -> list[int]:
    values = [int(part.strip()) for part in text.split(",") if part.strip()]
    if not values:
        raise argparse.ArgumentTypeError("provide at least one comma-separated period")
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--periods", type=parse_periods, required=True)
    parser.add_argument("--tau", type=float, default=4.0)
    parser.add_argument("--starts", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20260715)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = run_case(args.N, args.periods, args.tau, args.starts, args.seed, args.tolerance)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
