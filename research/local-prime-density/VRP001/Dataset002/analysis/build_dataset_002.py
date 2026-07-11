from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd

MAX_N = 10_000_000
ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT.parent / "Dataset001" / "data" / "pvg_lpd_dataset_001.csv"
OUTPUT = ROOT / "data" / "pvg_lpd_dataset_002.csv"

CHARACTERS = {
    "chi3": (3, np.array([0, 1, -1])),
    "chi4": (4, np.array([0, 1, 0, -1])),
    "chi5": (5, np.array([0, 1, -1, -1, 1])),
    "chi7": (7, np.array([0, 1, 1, -1, 1, -1, -1])),
    "chi8": (8, np.array([0, 1, 0, -1, 0, -1, 0, 1])),
    "chi11": (11, np.array([0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1])),
}
RESIDUE_MODULI = [3, 4, 5, 7, 8, 11]
LAGS = [1, 2, 4]


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


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(
            f"Dataset 001 is missing: {INPUT}. Run Dataset001/analysis/build_dataset_001.py first."
        )
    source = pd.read_csv(INPUT)
    if len(source) != 829:
        raise RuntimeError(f"Expected 829 Dataset 001 rows, found {len(source)}")

    is_prime = sieve_primes(MAX_N)
    lambda_values = von_mangoldt(MAX_N, is_prime)
    positions = np.flatnonzero(lambda_values)
    weights = lambda_values[positions]
    cumulative = np.concatenate(([0.0], np.cumsum(weights)))

    def indices(left: int, right: int) -> tuple[int, int]:
        return (
            int(np.searchsorted(positions, left, side="left")),
            int(np.searchsorted(positions, right, side="right")),
        )

    rows: list[dict[str, object]] = []
    for record in source.to_dict(orient="records"):
        start = int(record["start"])
        h = int(record["h"])
        log_x = math.log(max(start, 3))
        out = dict(record)
        for multiplier in LAGS:
            length = multiplier * h
            left = max(2, start - length)
            right = start - 1
            actual = right - left + 1
            i, j = indices(left, right)
            pos = positions[i:j]
            wt = weights[i:j]
            psi = float(cumulative[j] - cumulative[i])
            residual = psi - actual
            out[f"pre_lambda_density_m{multiplier}"] = psi / actual
            out[f"pre_lambda_residual_per_sqrt_m{multiplier}"] = residual / math.sqrt(actual)
            out[f"pre_context_actual_length_m{multiplier}"] = actual

            character_values: list[float] = []
            for name, (modulus, lookup) in CHARACTERS.items():
                value = float(np.sum(wt * lookup[pos % modulus])) if len(pos) else 0.0
                scaled = value / math.sqrt(actual * log_x)
                out[f"pre_{name}_lambda_scaled_m{multiplier}"] = scaled
                character_values.append(scaled)
            out[f"pre_character_energy_m{multiplier}"] = float(np.dot(character_values, character_values))

            for modulus in RESIDUE_MODULI:
                sums = (
                    np.bincount(pos % modulus, weights=wt, minlength=modulus)
                    if len(pos)
                    else np.zeros(modulus)
                )
                reduced = np.array(
                    [a for a in range(modulus) if math.gcd(a, modulus) == 1],
                    dtype=int,
                )
                values = sums[reduced]
                centered = values - values.mean()
                denominator = max(actual * log_x, 1.0)
                out[f"pre_residue_energy_q{modulus}_m{multiplier}"] = float(
                    np.dot(centered, centered) / denominator
                )
                out[f"pre_residue_max_q{modulus}_m{multiplier}"] = float(
                    np.max(np.abs(centered)) / math.sqrt(denominator)
                )
        rows.append(out)

    data = pd.DataFrame(rows)
    if len(data) != 829:
        raise RuntimeError(f"Expected 829 rows, found {len(data)}")
    required = [f"pre_context_actual_length_m{m}" for m in LAGS]
    if data[required].isna().any().any() or not (data[required] > 0).all().all():
        raise RuntimeError("Invalid past-context lengths")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT, index=False)
    print(f"Wrote {OUTPUT} ({len(data)} rows)")


if __name__ == "__main__":
    main()
