#!/usr/bin/env python3
"""AVRG Research Pass 007: decompose the finite-scale local variance gap."""

from __future__ import annotations

import json
import math
import os

import numpy as np

from avrg_pass003 import fft_self_convolution, prime_sieve, twin_prime_constant
from avrg_pass005 import valuation_array


LOCAL_PRIMES = (3, 5, 7, 11, 13, 17, 19, 23)
LIMIT_EXPONENT = int(os.environ.get("AVRG_LIMIT_EXPONENT", "21"))
MAX_N_RUN = 2**LIMIT_EXPONENT - 1
WINDOW_EXPONENTS_RUN = list(range(14, LIMIT_EXPONENT))


def weighted_sequences(primes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    theta = np.zeros(MAX_N_RUN + 1, dtype=np.float64)
    von_mangoldt = np.zeros(MAX_N_RUN + 1, dtype=np.float64)
    for p_raw in primes:
        p = int(p_raw)
        log_p = math.log(p)
        theta[p] = log_p
        power = p
        while power <= MAX_N_RUN:
            von_mangoldt[power] = log_p
            if power > MAX_N_RUN // p:
                break
            power *= p
    return theta, von_mangoldt


def singular_series(primes: np.ndarray) -> np.ndarray:
    multiplier = np.ones(MAX_N_RUN + 1, dtype=np.float64)
    for p_raw in primes[primes > 2]:
        p = int(p_raw)
        multiplier[p::p] *= (p - 1.0) / (p - 2.0)
    return 2.0 * twin_prime_constant(primes) * multiplier


def group_moments(values: np.ndarray) -> dict:
    mean = float(np.mean(values))
    mse = float(np.mean(values**2))
    variance = float(np.var(values))
    return {"count": int(len(values)), "mean": mean, "mse": mse, "variance": variance}


def ratio(on: float, off: float) -> float:
    return float(on / off)


def residual_factor(residual: np.ndarray, on_mask: np.ndarray) -> dict:
    off = group_moments(residual[~on_mask])
    on = group_moments(residual[on_mask])
    off_cv2 = off["variance"] / (1.0 + off["mean"]) ** 2
    on_cv2 = on["variance"] / (1.0 + on["mean"]) ** 2
    return {
        "off": off,
        "on": on,
        "kappa_mse": ratio(on["mse"], off["mse"]),
        "kappa_centered_variance": ratio(on["variance"], off["variance"]),
        "kappa_conditional_cv2": ratio(on_cv2, off_cv2),
        "conditional_cv2": {"off": off_cv2, "on": on_cv2},
    }


def positive_proxy_factor(proxy: np.ndarray, on_mask: np.ndarray) -> dict:
    off = float(np.mean(proxy[~on_mask]))
    on = float(np.mean(proxy[on_mask]))
    return {"off_mean": off, "on_mean": on, "kappa": ratio(on, off)}


def diagonal_remainder(
    residual: np.ndarray, diagonal_proxy: np.ndarray, on_mask: np.ndarray
) -> dict:
    result = {}
    for label, mask in (("off", ~on_mask), ("on", on_mask)):
        mse = float(np.mean(residual[mask] ** 2))
        diagonal = float(np.mean(diagonal_proxy[mask]))
        remainder = mse - diagonal
        result[label] = {
            "residual_mse": mse,
            "diagonal_mean": diagonal,
            "effective_non_diagonal_remainder": remainder,
            "cancellation_fraction_of_diagonal": -remainder / diagonal,
        }
    result["remainder_on_over_off"] = ratio(
        result["on"]["effective_non_diagonal_remainder"],
        result["off"]["effective_non_diagonal_remainder"],
    )
    c_off = result["off"]["cancellation_fraction_of_diagonal"]
    c_on = result["on"]["cancellation_fraction_of_diagonal"]
    diagonal_kappa = ratio(
        result["on"]["diagonal_mean"], result["off"]["diagonal_mean"]
    )
    correlation_correction = ratio(1.0 - c_on, 1.0 - c_off)
    result["factor_identity"] = {
        "diagonal_kappa": diagonal_kappa,
        "correlation_correction": correlation_correction,
        "reconstructed_kappa": diagonal_kappa * correlation_correction,
    }
    return result


def decomposition(
    prime_residual: np.ndarray,
    prime_power_correction: np.ndarray,
    on_mask: np.ndarray,
) -> dict:
    result = {}
    for label, mask in (("off", ~on_mask), ("on", on_mask)):
        theta = prime_residual[mask]
        delta = prime_power_correction[mask]
        theta_mse = float(np.mean(theta**2))
        delta_mse = float(np.mean(delta**2))
        cross_twice = float(2.0 * np.mean(theta * delta))
        reconstructed = theta_mse + delta_mse + cross_twice
        direct = float(np.mean((theta + delta) ** 2))
        result[label] = {
            "theta_mse": theta_mse,
            "prime_power_delta_mse": delta_mse,
            "twice_cross": cross_twice,
            "reconstructed_full_mse": reconstructed,
            "direct_full_mse": direct,
            "reconstruction_abs_error": abs(reconstructed - direct),
            "delta_share_of_full_mse": delta_mse / direct,
            "cross_share_of_full_mse": cross_twice / direct,
        }
    return result


def main() -> None:
    _, primes = prime_sieve(MAX_N_RUN)
    theta, von_mangoldt = weighted_sequences(primes)
    singular = singular_series(primes)

    theta_conv = fft_self_convolution(theta, MAX_N_RUN)
    lambda_conv = fft_self_convolution(von_mangoldt, MAX_N_RUN)
    theta_diagonal = fft_self_convolution(theta**2, MAX_N_RUN)
    lambda_diagonal = fft_self_convolution(von_mangoldt**2, MAX_N_RUN)

    windows = []
    for exponent in WINDOW_EXPONENTS_RUN:
        lo, hi = 2**exponent, 2 ** (exponent + 1)
        targets = np.arange(lo, hi, 2, dtype=np.int64)
        denominator = singular[targets] * targets

        theta_residual = theta_conv[targets] / denominator - 1.0
        full_residual = lambda_conv[targets] / denominator - 1.0
        prime_power_correction = (lambda_conv[targets] - theta_conv[targets]) / denominator
        theta_diagonal_proxy = theta_diagonal[targets] / denominator**2
        lambda_diagonal_proxy = lambda_diagonal[targets] / denominator**2

        axes = {}
        for prime in LOCAL_PRIMES:
            valuations = valuation_array(targets, prime)
            on_mask = valuations >= 1
            by_depth = {}
            for depth in (1, 2, 3):
                depth_mask = valuations == depth
                if np.any(depth_mask):
                    by_depth[str(depth)] = {
                        "full_mse": float(np.mean(full_residual[depth_mask] ** 2)),
                        "prime_only_mse": float(np.mean(theta_residual[depth_mask] ** 2)),
                    }
            axes[str(prime)] = {
                "poisson_kappa": (prime - 2.0) / (prime - 1.0),
                "full_lambda": residual_factor(full_residual, on_mask),
                "prime_only_theta": residual_factor(theta_residual, on_mask),
                "prime_power_correction": residual_factor(prime_power_correction, on_mask),
                "mse_decomposition": decomposition(
                    theta_residual, prime_power_correction, on_mask
                ),
                "diagonal_proxies": {
                    "lambda_squared": positive_proxy_factor(
                        lambda_diagonal_proxy, on_mask
                    ),
                    "theta_squared": positive_proxy_factor(
                        theta_diagonal_proxy, on_mask
                    ),
                },
                "diagonal_remainders": {
                    "full_lambda": diagonal_remainder(
                        full_residual, lambda_diagonal_proxy, on_mask
                    ),
                    "prime_only_theta": diagonal_remainder(
                        theta_residual, theta_diagonal_proxy, on_mask
                    ),
                },
                "by_positive_depth": by_depth,
            }

        windows.append({"exponent": exponent, "window": [lo, hi], "axes": axes})

    last = windows[-1]
    digest = {}
    for prime in LOCAL_PRIMES:
        axis = last["axes"][str(prime)]
        digest[str(prime)] = {
            "poisson": axis["poisson_kappa"],
            "full_mse": axis["full_lambda"]["kappa_mse"],
            "full_centered": axis["full_lambda"]["kappa_centered_variance"],
            "full_conditional_cv2": axis["full_lambda"]["kappa_conditional_cv2"],
            "prime_only_mse": axis["prime_only_theta"]["kappa_mse"],
            "prime_only_centered": axis["prime_only_theta"][
                "kappa_centered_variance"
            ],
            "lambda_diagonal": axis["diagonal_proxies"]["lambda_squared"][
                "kappa"
            ],
            "theta_diagonal": axis["diagonal_proxies"]["theta_squared"]["kappa"],
            "lambda_cancellation_fraction_off": axis["diagonal_remainders"][
                "full_lambda"
            ]["off"]["cancellation_fraction_of_diagonal"],
            "lambda_cancellation_fraction_on": axis["diagonal_remainders"][
                "full_lambda"
            ]["on"]["cancellation_fraction_of_diagonal"],
            "lambda_remainder_on_over_off": axis["diagonal_remainders"][
                "full_lambda"
            ]["remainder_on_over_off"],
            "lambda_correlation_correction": axis["diagonal_remainders"][
                "full_lambda"
            ]["factor_identity"]["correlation_correction"],
            "lambda_factor_reconstruction": axis["diagonal_remainders"][
                "full_lambda"
            ]["factor_identity"]["reconstructed_kappa"],
            "prime_power_delta_share_off": axis["mse_decomposition"]["off"][
                "delta_share_of_full_mse"
            ],
            "prime_power_delta_share_on": axis["mse_decomposition"]["on"][
                "delta_share_of_full_mse"
            ],
            "prime_power_cross_share_off": axis["mse_decomposition"]["off"][
                "cross_share_of_full_mse"
            ],
            "prime_power_cross_share_on": axis["mse_decomposition"]["on"][
                "cross_share_of_full_mse"
            ],
        }

    result = {
        "parameters": {
            "max_n": MAX_N_RUN,
            "window_exponents": WINDOW_EXPONENTS_RUN,
            "local_primes": LOCAL_PRIMES,
            "normalization": "singular_series(N)*N",
        },
        "definitions": {
            "full_residual": "(Lambda*Lambda)/(S(N)N)-1",
            "prime_only_residual": "(theta*theta)/(S(N)N)-1",
            "prime_power_correction": "((Lambda*Lambda)-(theta*theta))/(S(N)N)",
            "diagonal_proxy": "(weight^2*weight^2)/(S(N)N)^2",
        },
        "windows": windows,
        "last_window_digest": digest,
    }
    output_name = (
        "avrg_pass007_results.json"
        if LIMIT_EXPONENT == 21
        else f"avrg_pass007_results_to_2pow{LIMIT_EXPONENT}.json"
    )
    with open(output_name, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    print(json.dumps(digest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
