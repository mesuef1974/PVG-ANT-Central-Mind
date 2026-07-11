from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.special import expi

ROOT = Path(__file__).resolve().parent.parent
PROTOCOL_PATH = ROOT / "protocol.json"
OUTPUT = ROOT / "data" / "pvg_lpd_dataset_003.csv"
METADATA = ROOT / "data" / "pvg_lpd_dataset_003_metadata.json"
SEGMENT_SIZE = 1_000_000

CHARACTERS = {
    "chi3": (3, np.array([0, 1, -1], dtype=np.float64)),
    "chi4": (4, np.array([0, 1, 0, -1], dtype=np.float64)),
    "chi5": (5, np.array([0, 1, -1, -1, 1], dtype=np.float64)),
    "chi7": (7, np.array([0, 1, 1, -1, 1, -1, -1], dtype=np.float64)),
    "chi8": (8, np.array([0, 1, 0, -1, 0, -1, 0, 1], dtype=np.float64)),
    "chi11": (
        11,
        np.array([0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1], dtype=np.float64),
    ),
}
RESIDUE_MODULI = [3, 4, 5, 7, 8, 11]
LAGS = [1, 2, 4]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def simple_primes(limit: int) -> np.ndarray:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = False
    return np.flatnonzero(sieve).astype(np.int64)


def segmented_primes(limit: int, segment_size: int = SEGMENT_SIZE) -> np.ndarray:
    base = simple_primes(int(math.isqrt(limit)))
    chunks: list[np.ndarray] = []
    for low in range(2, limit + 1, segment_size):
        high = min(limit, low + segment_size - 1)
        block = np.ones(high - low + 1, dtype=bool)
        for prime in base:
            p = int(prime)
            start = max(p * p, ((low + p - 1) // p) * p)
            if start <= high:
                block[start - low :: p] = False
        chunks.append(np.flatnonzero(block).astype(np.int64) + low)
    require(chunks, "Segmented sieve produced no chunks")
    primes = np.concatenate(chunks)
    require(len(primes) > 0 and primes[0] == 2, "Segmented sieve failed")
    return primes


def lambda_support(primes: np.ndarray, limit: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    base_positions = primes
    base_weights = np.log(primes.astype(np.float64))
    power_positions: list[int] = []
    power_weights: list[float] = []
    for prime in primes[primes <= math.isqrt(limit)]:
        p = int(prime)
        value = p * p
        weight = math.log(p)
        while value <= limit:
            power_positions.append(value)
            power_weights.append(weight)
            if value > limit // p:
                break
            value *= p
    if power_positions:
        positions = np.concatenate(
            [base_positions, np.asarray(power_positions, dtype=np.int64)]
        )
        weights = np.concatenate(
            [base_weights, np.asarray(power_weights, dtype=np.float64)]
        )
        order = np.argsort(positions, kind="mergesort")
        positions = positions[order]
        weights = weights[order]
    else:
        positions = base_positions.copy()
        weights = base_weights.copy()
    require(np.all(positions[1:] > positions[:-1]), "Lambda support is not unique and sorted")
    cumulative = np.concatenate(([0.0], np.cumsum(weights)))
    return positions, weights, cumulative


def complete_windows(lower: int, upper_exclusive: int, theta: float) -> list[tuple[int, int, int]]:
    windows: list[tuple[int, int, int]] = []
    start = lower
    upper = upper_exclusive - 1
    while True:
        h = max(10, int(round(start**theta)))
        end = start + h - 1
        if end > upper:
            break
        windows.append((start, end, h))
        start = end + 1
    return windows


def select_evenly(items: list[tuple[int, int, int]], count: int) -> list[tuple[int, int, int]]:
    require(len(items) >= count, f"Only {len(items)} windows are available; need {count}")
    indices = np.linspace(0, len(items) - 1, count, dtype=int)
    require(len(set(int(index) for index in indices)) == count, "Even selection produced duplicate indices")
    return [items[int(index)] for index in indices]


def slice_indices(positions: np.ndarray, left: int, right: int) -> tuple[int, int]:
    return (
        int(np.searchsorted(positions, left, side="left")),
        int(np.searchsorted(positions, right, side="right")),
    )


def main() -> None:
    require(PROTOCOL_PATH.exists(), "Frozen protocol is missing")
    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
    require(protocol["status"] == "FROZEN_BEFORE_DATA", "Protocol is not frozen")

    lower = int(protocol["numerical_range"]["start_inclusive"])
    upper_exclusive = int(protocol["numerical_range"]["end_exclusive"])
    theta_families = [float(value) for value in protocol["window_design"]["theta_families"]]
    windows_per_family = int(protocol["window_design"]["windows_per_family"])
    expected_total = int(protocol["window_design"]["expected_total_windows"])

    windows: list[dict[str, object]] = []
    complete_counts: dict[str, int] = {}
    for theta in theta_families:
        complete = complete_windows(lower, upper_exclusive, theta)
        complete_counts[f"{theta:.12g}"] = len(complete)
        selected = select_evenly(complete, windows_per_family)
        for selection_index, (start, end, h) in enumerate(selected):
            windows.append(
                {
                    "window_id": f"LPD3-{len(windows) + 1:04d}",
                    "family": f"x^{theta:.6g}",
                    "theta_nominal": theta,
                    "selection_index": selection_index,
                    "complete_family_size": len(complete),
                    "start": start,
                    "end": end,
                    "h": h,
                }
            )
    require(len(windows) == expected_total, f"Expected {expected_total} windows, found {len(windows)}")

    maximum = upper_exclusive - 1
    primes = segmented_primes(maximum)
    lambda_positions, lambda_weights, lambda_cumulative = lambda_support(primes, maximum)

    rows: list[dict[str, object]] = []
    for window in windows:
        start = int(window["start"])
        end = int(window["end"])
        h = int(window["h"])
        left = start - 1
        midpoint = (left + end) / 2
        log_x = math.log(start)

        prime_i, prime_j = slice_indices(primes, start, end)
        prime_count = prime_j - prime_i
        li_expected = float(expi(math.log(end)) - expi(math.log(left)))
        lambda_i, lambda_j = slice_indices(lambda_positions, start, end)
        target_positions = lambda_positions[lambda_i:lambda_j]
        target_weights = lambda_weights[lambda_i:lambda_j]
        psi_interval = float(lambda_cumulative[lambda_j] - lambda_cumulative[lambda_i])

        record: dict[str, object] = {
            **window,
            "role": "confirmatory",
            "analysis_split": "independent_test",
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
        }

        for multiplier in LAGS:
            length = multiplier * h
            context_left = start - length
            context_right = start - 1
            require(context_left >= 2, "Past context extends below 2")
            i, j = slice_indices(lambda_positions, context_left, context_right)
            positions = lambda_positions[i:j]
            weights = lambda_weights[i:j]
            psi = float(lambda_cumulative[j] - lambda_cumulative[i])
            residual = psi - length
            record[f"pre_lambda_density_m{multiplier}"] = psi / length
            record[f"pre_lambda_residual_per_sqrt_m{multiplier}"] = residual / math.sqrt(length)
            record[f"pre_context_actual_length_m{multiplier}"] = length

            character_values: list[float] = []
            for name, (modulus, lookup) in CHARACTERS.items():
                value = float(np.sum(weights * lookup[positions % modulus])) if len(positions) else 0.0
                scaled = value / math.sqrt(length * log_x)
                record[f"pre_{name}_lambda_scaled_m{multiplier}"] = scaled
                character_values.append(scaled)
            record[f"pre_character_energy_m{multiplier}"] = float(
                np.dot(character_values, character_values)
            )

            for modulus in RESIDUE_MODULI:
                sums = (
                    np.bincount(positions % modulus, weights=weights, minlength=modulus)
                    if len(positions)
                    else np.zeros(modulus)
                )
                reduced = np.asarray(
                    [residue for residue in range(modulus) if math.gcd(residue, modulus) == 1],
                    dtype=int,
                )
                values = sums[reduced]
                centered = values - values.mean()
                denominator = length * log_x
                record[f"pre_residue_energy_q{modulus}_m{multiplier}"] = float(
                    np.dot(centered, centered) / denominator
                )
                record[f"pre_residue_max_q{modulus}_m{multiplier}"] = float(
                    np.max(np.abs(centered)) / math.sqrt(denominator)
                )

        for modulus in RESIDUE_MODULI:
            reduced = [residue for residue in range(modulus) if math.gcd(residue, modulus) == 1]
            sums = (
                np.bincount(target_positions % modulus, weights=target_weights, minlength=modulus)
                if len(target_positions)
                else np.zeros(modulus)
            )
            phi = len(reduced)
            expected = h / phi
            scale = math.sqrt(h * log_x / phi)
            for residue in reduced:
                value = float(sums[residue])
                record[f"target_psi_q{modulus}_a{residue}"] = value
                record[f"target_psi_std_q{modulus}_a{residue}"] = (value - expected) / scale

        rows.append(record)

    data = pd.DataFrame(rows)
    require(len(data) == expected_total, "Dataset 003 row count changed")
    counts = data.groupby("family").size().to_dict()
    require(set(counts.values()) == {windows_per_family}, f"Unbalanced families: {counts}")
    require(data.isna().sum().sum() == 0, "Dataset 003 contains missing values")
    require(np.isfinite(data.select_dtypes(include=[np.number]).to_numpy()).all(), "Dataset 003 contains non-finite numbers")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT, index=False)
    metadata = {
        "protocol_id": protocol["protocol_id"],
        "rows": len(data),
        "columns": len(data.columns),
        "range": [lower, upper_exclusive],
        "complete_window_counts": complete_counts,
        "selected_per_family": windows_per_family,
        "prime_count_to_limit": int(len(primes)),
        "lambda_support_count": int(len(lambda_positions)),
        "protocol_sha256": sha256(PROTOCOL_PATH),
        "dataset_sha256": sha256(OUTPUT),
        "builder": "deterministic_segmented_sieve",
        "segment_size": SEGMENT_SIZE,
    }
    METADATA.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(data)} rows, {len(data.columns)} columns)")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
