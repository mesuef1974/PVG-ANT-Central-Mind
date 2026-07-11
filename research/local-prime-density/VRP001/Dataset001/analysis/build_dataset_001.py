from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.special import expi

MAX_N = 10_000_000
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "pvg_lpd_dataset_001.csv"


def sieve_primes(limit: int) -> np.ndarray:
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p :: p] = False
    return is_prime


def von_mangoldt(limit: int, is_prime: np.ndarray) -> np.ndarray:
    values = np.zeros(limit + 1, dtype=np.float64)
    for p in np.flatnonzero(is_prime):
        p = int(p)
        q = p
        log_p = math.log(p)
        while q <= limit:
            values[q] = log_p
            if q > limit // p:
                break
            q *= p
    return values


def nonoverlap(lower: int, upper: int, theta: float) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    start = lower
    while True:
        h = max(10, int(round(start**theta)))
        end = start + h - 1
        if end > upper:
            break
        result.append((start, end, h))
        start = end + 1
    return result


def even_pick(items: list[tuple[int, int, int]], count: int = 80) -> list[tuple[int, int, int]]:
    if len(items) <= count:
        return items
    indices = np.linspace(0, len(items) - 1, count, dtype=int)
    return [items[i] for i in sorted(set(indices))]


def squarefree_divisors(primes: list[int]) -> list[tuple[int, int]]:
    divisors = [(1, 1)]
    for p in primes:
        old = list(divisors)
        divisors.extend((d * p, -mu) for d, mu in old)
    return divisors


def main() -> None:
    is_prime = sieve_primes(MAX_N)
    pi_prefix = np.cumsum(is_prime, dtype=np.int32)
    lambda_values = von_mangoldt(MAX_N, is_prime)
    psi_prefix = np.cumsum(lambda_values)

    windows: list[dict[str, object]] = []
    for digits in range(2, 8):
        h = 10 ** (digits - 1)
        for k in range(1, 10):
            start = k * h
            windows.append({
                "family": "digit_block",
                "role": "calibration",
                "theta_nominal": 1.0,
                "scale_exponent": digits - 1,
                "start": start,
                "end": (k + 1) * h - 1,
                "h": h,
            })

    for theta in (0.5, 2 / 3, 0.75):
        for exponent in range(3, 7):
            candidates = nonoverlap(10**exponent, 10 ** (exponent + 1) - 1, theta)
            for start, end, h in even_pick(candidates):
                windows.append({
                    "family": f"x^{theta:.6g}",
                    "role": "research",
                    "theta_nominal": theta,
                    "scale_exponent": exponent,
                    "start": start,
                    "end": end,
                    "h": h,
                })

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    divisors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 6, 10, 14, 15, 21, 22, 30, 35, 42, 66, 70, 105, 210]
    z_levels = [7, 13, 19, 29]
    z_divisors: dict[int, list[tuple[int, int]]] = {}
    z_density: dict[int, float] = {}
    for z in z_levels:
        ps = [p for p in small_primes if p <= z]
        z_divisors[z] = squarefree_divisors(ps)
        density = 1.0
        for p in ps:
            density *= 1 - 1 / p
        z_density[z] = density

    rows: list[dict[str, object]] = []
    for index, window in enumerate(windows, 1):
        start = int(window["start"])
        end = int(window["end"])
        h = int(window["h"])
        left = start - 1
        midpoint = (left + end) / 2
        prime_count = int(pi_prefix[end] - pi_prefix[left])
        psi_interval = float(psi_prefix[end] - psi_prefix[left])
        li_expected = float(expi(math.log(end)) - expi(math.log(left)))
        split = (
            "calibration" if window["role"] == "calibration"
            else "train" if start < 100_000
            else "validation" if start < 1_000_000
            else "test"
        )
        row: dict[str, object] = {
            **window,
            "window_id": f"LPD-{index:04d}",
            "left_exclusive": left,
            "right_inclusive": end,
            "midpoint": midpoint,
            "log_x": math.log(left),
            "log_h": math.log(h),
            "theta_empirical": math.log(h) / math.log(left),
            "prime_count": prime_count,
            "prime_density": prime_count / h,
            "normalized_log_density": prime_count * math.log(midpoint) / h,
            "li_expected": li_expected,
            "li_residual": prime_count - li_expected,
            "li_std_residual": (prime_count - li_expected) / math.sqrt(li_expected),
            "psi_interval": psi_interval,
            "lambda_density": psi_interval / h,
            "lambda_residual": psi_interval - h,
            "analysis_split": split,
        }
        all_r: list[float] = []
        prime_r: list[float] = []
        for divisor in divisors:
            remainder = (end // divisor - left // divisor) - h / divisor
            row[f"r_d_{divisor}"] = remainder
            all_r.append(remainder)
            if divisor in small_primes:
                prime_r.append(remainder)
        row["vsds_rp_l1"] = sum(abs(v) for v in prime_r)
        row["vsds_rp_l2"] = math.sqrt(sum(v * v for v in prime_r))
        row["vsds_rp_signed"] = sum(prime_r)
        row["vsds_rp_maxabs"] = max(abs(v) for v in prime_r)
        row["vsds_rd_l1"] = sum(abs(v) for v in all_r)
        row["vsds_rd_l2"] = math.sqrt(sum(v * v for v in all_r))
        for z in z_levels:
            survivors = sum(mu * (end // divisor - left // divisor) for divisor, mu in z_divisors[z])
            expected = h * z_density[z]
            row[f"sift_survivors_z{z}"] = survivors
            row[f"sift_residual_z{z}"] = survivors - expected
            row[f"sift_ratio_z{z}"] = survivors / expected
        rows.append(row)

    data = pd.DataFrame(rows)
    if len(data) != 829:
        raise RuntimeError(f"Expected 829 rows, found {len(data)}")
    counts = data[data["role"] == "research"]["analysis_split"].value_counts().to_dict()
    if counts != {"train": 319, "test": 240, "validation": 216}:
        raise RuntimeError(f"Unexpected split counts: {counts}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT, index=False)
    print(f"Wrote {OUTPUT} ({len(data)} rows)")


if __name__ == "__main__":
    main()
