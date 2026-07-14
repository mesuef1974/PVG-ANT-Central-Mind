#!/usr/bin/env python3
"""AVRG Pass 012: covariance spectra in multiplicative residue coordinates."""

from __future__ import annotations

import json
import math
import os

import numpy as np

from avrg_pass003 import fft_self_convolution, prime_sieve, twin_prime_constant
from avrg_pass011 import fft_convolution


LIMIT_EXPONENT = int(os.environ.get("AVRG_LIMIT_EXPONENT", "21"))
MAX_N = 2**LIMIT_EXPONENT - 1
AXIS_PRIMES = (3, 5, 7, 11)


def build_theta_and_singular(primes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    theta = np.zeros(MAX_N + 1, dtype=np.float64)
    for p_raw in primes:
        p = int(p_raw)
        theta[p] = math.log(p)
    multiplier = np.ones(MAX_N + 1, dtype=np.float64)
    for p_raw in primes[primes > 2]:
        p = int(p_raw)
        multiplier[p::p] *= (p - 1.0) / (p - 2.0)
    singular = 2.0 * twin_prime_constant(primes) * multiplier
    return theta, singular


def primitive_root(prime: int) -> int:
    factors = []
    n = prime - 1
    candidate = 2
    remaining = n
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            factors.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    if remaining > 1:
        factors.append(remaining)
    for root in range(2, prime):
        if all(pow(root, n // factor, prime) != 1 for factor in factors):
            return root
    raise RuntimeError("primitive root not found")


def covariance(matrix: np.ndarray, mask: np.ndarray) -> np.ndarray:
    selected = matrix[:, mask]
    return selected @ selected.T / selected.shape[1]


def matrix_diagnostics(covariance_matrix: np.ndarray, prime: int) -> dict:
    root = primitive_root(prime)
    order = [pow(root, exponent, prime) for exponent in range(prime - 1)]
    block = covariance_matrix[np.ix_(order, order)]
    dimension = prime - 1

    circulant_coefficients = []
    circulant_fit = np.zeros_like(block)
    for delta in range(dimension):
        values = [block[row, (row + delta) % dimension] for row in range(dimension)]
        coefficient = float(np.mean(values))
        circulant_coefficients.append(coefficient)
        for row in range(dimension):
            circulant_fit[row, (row + delta) % dimension] = coefficient

    diagonal_mean = float(np.mean(np.diag(block)))
    off_diagonal_mean = float(
        (np.sum(block) - np.trace(block)) / (dimension * (dimension - 1))
    )
    compound_fit = np.full_like(block, off_diagonal_mean)
    np.fill_diagonal(compound_fit, diagonal_mean)

    norm = float(np.linalg.norm(block, ord="fro"))
    circulant_error = float(np.linalg.norm(block - circulant_fit, ord="fro") / norm)
    compound_error = float(np.linalg.norm(block - compound_fit, ord="fro") / norm)
    eigenvalues = np.linalg.eigvalsh(block)[::-1]
    character_eigenvalues = np.real(np.fft.fft(circulant_coefficients))
    trivial_vector = np.ones(dimension) / math.sqrt(dimension)
    trivial_rayleigh = float(trivial_vector @ block @ trivial_vector)
    full_total_variance = float(np.sum(covariance_matrix))
    active_total_variance = float(np.sum(block))

    return {
        "primitive_root": root,
        "multiplicative_order": order,
        "active_block": block.tolist(),
        "eigenvalues_descending": eigenvalues.tolist(),
        "circulant_coefficients": circulant_coefficients,
        "character_eigenvalues_by_frequency": character_eigenvalues.tolist(),
        "trivial_character_rayleigh": trivial_rayleigh,
        "nontrivial_character_mean": float(np.mean(character_eigenvalues[1:])),
        "nontrivial_character_std": float(np.std(character_eigenvalues[1:])),
        "circulant_relative_frobenius_error": circulant_error,
        "compound_symmetry_relative_frobenius_error": compound_error,
        "full_total_variance": full_total_variance,
        "active_total_variance": active_total_variance,
        "zero_coordinate_relative_trace": float(
            covariance_matrix[0, 0] / np.trace(covariance_matrix)
        ),
    }


def main() -> None:
    _, primes = prime_sieve(MAX_N)
    theta, singular = build_theta_and_singular(primes)
    total_convolution = fft_self_convolution(theta, MAX_N)
    lo, hi = 2 ** (LIMIT_EXPONENT - 1), 2**LIMIT_EXPONENT
    targets = np.arange(lo, hi, 2, dtype=np.int64)
    main_term = singular[targets] * targets
    prime_residual = total_convolution[targets] / main_term - 1.0
    integers = np.arange(MAX_N + 1, dtype=np.int64)

    axes = {}
    for prime in AXIS_PRIMES:
        target_residue = targets % prime
        allowed_count = np.where(target_residue == 0, prime - 1, prime - 2)
        normalized_vectors = np.empty((prime, len(targets)), dtype=np.float64)
        for residue in range(prime):
            restricted = np.where(integers % prime == residue, theta, 0.0)
            class_convolution = fft_convolution(restricted, theta, MAX_N)[targets]
            allowed = (residue != 0) & ((target_residue - residue) % prime != 0)
            expected = np.where(allowed, main_term / allowed_count, 0.0)
            normalized_vectors[residue] = (class_convolution - expected) / main_term

        on = target_residue == 0
        off = ~on
        sigma_on = covariance(normalized_vectors, on)
        sigma_off = covariance(normalized_vectors, off)
        on_diag = matrix_diagnostics(sigma_on, prime)
        off_diag = matrix_diagnostics(sigma_off, prime)
        mode_ratios = [
            on_value / off_value
            for on_value, off_value in zip(
                on_diag["character_eigenvalues_by_frequency"],
                off_diag["character_eigenvalues_by_frequency"],
            )
        ]
        total_ratio = on_diag["full_total_variance"] / off_diag["full_total_variance"]
        axes[str(prime)] = {
            "on": on_diag,
            "off": off_diag,
            "mode_on_over_off": mode_ratios,
            "trivial_mode_on_over_off": (
                on_diag["trivial_character_rayleigh"]
                / off_diag["trivial_character_rayleigh"]
            ),
            "total_residual_mse_on_over_off": total_ratio,
            "checks": {
                "max_abs_total_residual_reconstruction_error": float(
                    np.max(np.abs(np.sum(normalized_vectors, axis=0) - prime_residual))
                ),
                "trivial_vs_total_ratio_abs_error": abs(
                    total_ratio
                    - on_diag["trivial_character_rayleigh"]
                    / off_diag["trivial_character_rayleigh"]
                ),
            },
        }

    result = {
        "parameters": {
            "limit_exponent": LIMIT_EXPONENT,
            "window": [lo, hi],
            "axis_primes": AXIS_PRIMES,
        },
        "axes": axes,
    }
    output_name = (
        "avrg_pass012_results.json"
        if LIMIT_EXPONENT == 21
        else f"avrg_pass012_results_to_2pow{LIMIT_EXPONENT}.json"
    )
    with open(output_name, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    digest = {
        prime: {
            "total_ratio": axis["total_residual_mse_on_over_off"],
            "trivial_ratio": axis["trivial_mode_on_over_off"],
            "mode_ratios": axis["mode_on_over_off"],
            "circulant_error_on": axis["on"]["circulant_relative_frobenius_error"],
            "circulant_error_off": axis["off"]["circulant_relative_frobenius_error"],
            "compound_error_on": axis["on"][
                "compound_symmetry_relative_frobenius_error"
            ],
            "compound_error_off": axis["off"][
                "compound_symmetry_relative_frobenius_error"
            ],
        }
        for prime, axis in axes.items()
    }
    print(json.dumps(digest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
