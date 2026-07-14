#!/usr/bin/env python3
"""PASS028: full on-state residue-fiber scan and sample convergence.

All on-state values in the five locked windows are reconstructed from FFT
convolutions of residue fibers.  The exact finite energy is decomposed into
paired nonzero residue-difference orbits.  A deterministic nested coverage
ladder then measures how quickly samples approach the saved full energies.

Finite computational diagnostic only; no asymptotic or Goldbach proof claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np


EXPS = (15, 16, 17, 18, 19)
TRAIN_EXPS = (15, 16, 17, 18)
ALL_MODULI = (5, 7, 11, 13, 17, 19, 23, 29, 31)
PRIMARY_MODULI = (11, 13, 17, 19, 23, 29, 31)
COVERAGE_LADDER = (
    (1, 64),
    (1, 32),
    (1, 16),
    (1, 8),
    (1, 4),
    (1, 2),
    (1, 1),
)
SAMPLE_CORRELATION_MIN = 0.90
SAMPLE_MEDIAN_RELATIVE_ERROR_MAX = 0.10
FULL_MAX_RELATIVE_ERROR = 1e-10
FULL_CORRELATION_MIN = 1.0 - 1e-10
INDEPENDENCE_TOLERANCE = 1e-12
CLOSURE_TOLERANCE = 1e-10
CONCENTRATION_THRESHOLD = 0.50
CONCENTRATION_MODULUS_COUNT = 5


def default_pass023_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass023_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass023" / "avrg_pass023_results.json"


def default_pass025_holdout_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass025_holdout_e19.json"
    if archive.exists():
        return archive
    return here.parent / "pass025" / "avrg_pass025_holdout_e19.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass028_results.json"
    return here / "avrg_pass028_results.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sieve_theta(n: int) -> np.ndarray:
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = False
    theta = np.zeros(n + 1, dtype=float)
    primes = np.flatnonzero(is_prime)
    theta[primes] = np.log(primes)
    return theta


def singular_main(n_max: int) -> np.ndarray:
    """Hardy--Littlewood main term used unchanged since PASS013."""
    c2 = 0.6601618158468696
    is_prime = np.ones(n_max + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, math.isqrt(n_max) + 1):
        if is_prime[p]:
            is_prime[p * p : n_max + 1 : p] = False
    factor = np.ones(n_max + 1, dtype=float)
    for p in np.flatnonzero(is_prime)[1:]:
        factor[p::p] *= (p - 1) / (p - 2)
    n = np.arange(n_max + 1)
    result = np.zeros(n_max + 1, dtype=float)
    even = (n >= 4) & (n % 2 == 0)
    result[even] = 2 * c2 * n[even] * factor[even]
    return result


def primitive_root(p: int) -> int:
    for g in range(2, p):
        if len({pow(g, exponent, p) for exponent in range(p - 1)}) == p - 1:
            return g
    raise ValueError(f"No primitive root found for {p}")


def discrete_log_table(p: int) -> np.ndarray:
    table = np.full(p, -1, dtype=np.int64)
    g = primitive_root(p)
    value = 1
    for exponent in range(p - 1):
        table[value] = exponent
        value = value * g % p
    return table


def representative_modes(r: int) -> list[int]:
    return [k for k in range(2, r - 1, 2) if k <= r - 1 - k]


def character_on_residues(r: int, k: int) -> np.ndarray:
    logs = discrete_log_table(r)
    values = np.zeros(r, dtype=np.complex128)
    units = logs >= 0
    values[units] = np.exp(2j * np.pi * k * logs[units] / (r - 1))
    return values


def normalize_full_row(raw: dict, exp: int) -> dict:
    r, k = int(raw["r"]), int(raw["k"])
    on_energy = float(raw["on_energy"])
    if r not in ALL_MODULI:
        raise ValueError(f"Unexpected modulus: {(exp, r)}")
    if k <= 0 or k % 2 or k > r - 1 - k:
        raise ValueError(f"Invalid representative: {(exp, r, k)}")
    if not math.isfinite(on_energy) or on_energy <= 0:
        raise ValueError(f"Invalid on energy: {(exp, r, k)}")
    return {"exp": exp, "r": r, "k": k, "saved_on_energy": on_energy}


def load_full_rows(pass023_path: Path, holdout_path: Path) -> list[dict]:
    with pass023_path.open("r", encoding="utf-8") as handle:
        pass023 = json.load(handle)
    config = pass023.get("configuration", {})
    if tuple(config.get("exps", [])) != TRAIN_EXPS:
        raise ValueError("PASS023 windows differ from e=15..18")
    if tuple(config.get("moduli", [])) != ALL_MODULI:
        raise ValueError("PASS023 moduli differ from the locked set")
    windows = pass023.get("windows", [])
    if tuple(int(window["exp"]) for window in windows) != TRAIN_EXPS:
        raise ValueError("PASS023 payload differs from the window lock")
    rows = [
        normalize_full_row(raw, int(window["exp"]))
        for window in windows
        for raw in window.get("rows", [])
    ]

    with holdout_path.open("r", encoding="utf-8") as handle:
        holdout = json.load(handle)
    protocol = holdout.get("protocol", {})
    window = holdout.get("window", {})
    if int(protocol.get("holdout_exp", -1)) != 19 or int(window.get("exp", -1)) != 19:
        raise ValueError("PASS025 holdout is not e=19")
    if tuple(protocol.get("moduli", [])) != ALL_MODULI:
        raise ValueError("PASS025 holdout moduli differ from the lock")
    rows.extend(normalize_full_row(raw, 19) for raw in window.get("rows", []))

    rows = [row for row in rows if row["r"] in PRIMARY_MODULI]
    if len(rows) != 160:
        raise ValueError(f"Expected 160 primary rows, received {len(rows)}")
    keys = {(row["exp"], row["r"], row["k"]) for row in rows}
    if len(keys) != len(rows):
        raise ValueError("Duplicate (e,r,k) rows")
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            observed = sorted(
                row["k"] for row in rows if row["exp"] == exp and row["r"] == r
            )
            if observed != representative_modes(r):
                raise ValueError(f"Representative mismatch at {(exp, r)}")
    return rows


def splitmix64_order(values: np.ndarray, exp: int, r: int) -> np.ndarray:
    """Return a deterministic pseudorandom-looking nested ordering."""
    x = values.astype(np.uint64, copy=True)
    salt = np.uint64((exp << 32) | r)
    with np.errstate(over="ignore"):
        x = x + salt + np.uint64(0x9E3779B97F4A7C15)
        x = (x ^ (x >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9)
        x = (x ^ (x >> np.uint64(27))) * np.uint64(0x94D049BB133111EB)
        x = x ^ (x >> np.uint64(31))
    return np.argsort(x, kind="stable")


def coverage_count(total: int, numerator: int, denominator: int) -> int:
    if total <= 0 or numerator <= 0 or denominator <= 0 or numerator > denominator:
        raise ValueError("Invalid coverage arguments")
    return max(1, (total * numerator + denominator - 1) // denominator)


def decompose_f_matrix(
    f_matrix: np.ndarray, character: np.ndarray, normalization: np.ndarray
) -> dict:
    """Decompose every column into zero and paired nonzero lag orbits."""
    r, count = f_matrix.shape
    if character.shape != (r,) or normalization.shape != (count,):
        raise ValueError("Incompatible decomposition arrays")
    if np.any(normalization <= 0):
        raise ValueError("Nonpositive normalization")
    twisted = character @ f_matrix
    total_values = np.abs(twisted) ** 2 / normalization
    zero_values = np.sum(f_matrix[1:] ** 2, axis=0) / normalization
    orbit_values: dict[int, np.ndarray] = {}
    for b in range(1, (r - 1) // 2 + 1):
        coefficient = character * np.conjugate(np.roll(character, b))
        products = f_matrix * np.roll(f_matrix, b, axis=0)
        q_b = np.sum(coefficient[:, None] * products, axis=0)
        orbit_values[b] = 2.0 * q_b.real / normalization
    reconstructed = zero_values + sum(orbit_values.values())
    return {
        "total_values": total_values,
        "zero_values": zero_values,
        "orbit_values": orbit_values,
        "maximum_pointwise_closure_error": float(
            np.max(np.abs(reconstructed - total_values))
        ),
    }


def residue_fiber_matrix(
    theta: np.ndarray,
    theta_fft: np.ndarray,
    fft_length: int,
    r: int,
    on_values: np.ndarray,
    progress: bool = False,
) -> np.ndarray:
    """Compute all nonzero residue-fiber convolutions on selected N."""
    f_matrix = np.zeros((r, len(on_values)), dtype=float)
    fiber = np.zeros_like(theta)
    for alpha in range(1, r):
        fiber.fill(0.0)
        fiber[alpha::r] = theta[alpha::r]
        convolution = np.fft.irfft(
            np.fft.rfft(fiber, fft_length) * theta_fft, fft_length
        )[: len(theta)]
        f_matrix[alpha] = convolution[on_values]
        if progress and (alpha == 1 or alpha == r - 1 or alpha % 8 == 0):
            print(f"PASS028 fibers r={r} alpha={alpha}/{r-1}", flush=True)
    return f_matrix


def vector_correlation(xs: Sequence[float], ys: Sequence[float]) -> float:
    if len(xs) != len(ys) or not xs:
        raise ValueError("Correlation vectors must be nonempty and equally sized")
    xmean, ymean = statistics.fmean(xs), statistics.fmean(ys)
    xc = [value - xmean for value in xs]
    yc = [value - ymean for value in ys]
    denominator = math.sqrt(
        sum(value * value for value in xc) * sum(value * value for value in yc)
    )
    if denominator == 0:
        raise ValueError("Degenerate correlation")
    return sum(x * y for x, y in zip(xc, yc)) / denominator


def centered_log_vectors(
    rows: Sequence[dict], observed_field: str, reference_field: str
) -> tuple[list[float], list[float]]:
    observed: list[float] = []
    reference: list[float] = []
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            local = [row for row in rows if row["exp"] == exp and row["r"] == r]
            observed_logs = [math.log(row[observed_field]) for row in local]
            reference_logs = [math.log(row[reference_field]) for row in local]
            observed_mean = statistics.fmean(observed_logs)
            reference_mean = statistics.fmean(reference_logs)
            observed.extend(value - observed_mean for value in observed_logs)
            reference.extend(value - reference_mean for value in reference_logs)
    return observed, reference


def calibration_metrics(
    rows: Sequence[dict], observed_field: str, reference_field: str
) -> dict:
    observed, reference = centered_log_vectors(rows, observed_field, reference_field)
    relative_errors = [
        abs(row[observed_field] - row[reference_field]) / row[reference_field]
        for row in rows
    ]
    return {
        "row_count": len(rows),
        "centered_log_correlation": vector_correlation(observed, reference),
        "median_absolute_relative_error": statistics.median(relative_errors),
        "maximum_absolute_relative_error": max(relative_errors),
    }


def full_scan(
    saved_rows: Sequence[dict], progress: bool = False
) -> tuple[list[dict], dict[str, list[dict]], dict]:
    max_hi = 1 << (max(EXPS) + 1)
    min_lo = 1 << min(EXPS)
    theta = sieve_theta(max_hi)
    main = singular_main(max_hi)
    fft_length = 1 << (2 * len(theta) - 2).bit_length()
    theta_fft = np.fft.rfft(theta, fft_length)
    saved_lookup = {
        (row["exp"], row["r"], row["k"]): row["saved_on_energy"]
        for row in saved_rows
    }
    exact_rows: list[dict] = []
    ladder_rows: dict[str, list[dict]] = {
        f"{numerator}/{denominator}": [] for numerator, denominator in COVERAGE_LADDER
    }
    candidate_counts: list[dict] = []
    maximum_pointwise_closure_error = 0.0
    maximum_averaged_closure_error = 0.0

    for r in PRIMARY_MODULI:
        step = 2 * r
        first = ((min_lo + step - 1) // step) * step
        on_all = np.arange(first, max_hi, step, dtype=np.int64)
        if progress:
            print(f"PASS028 modulus r={r} all_on={len(on_all)}", flush=True)
        f_all = residue_fiber_matrix(
            theta, theta_fft, fft_length, r, on_all, progress=progress
        )
        modes = representative_modes(r)
        characters = {k: character_on_residues(r, k) for k in modes}

        for exp in EXPS:
            lo, hi = 1 << exp, 1 << (exp + 1)
            mask = (on_all >= lo) & (on_all < hi)
            on_values = on_all[mask]
            f_matrix = f_all[:, mask]
            normalization = main[on_values] ** 2 * (r - 1)
            order = splitmix64_order(on_values, exp, r)
            candidate_counts.append({"exp": exp, "r": r, "count": len(on_values)})

            for k in modes:
                parts = decompose_f_matrix(f_matrix, characters[k], normalization)
                maximum_pointwise_closure_error = max(
                    maximum_pointwise_closure_error,
                    parts["maximum_pointwise_closure_error"],
                )
                total = float(np.mean(parts["total_values"]))
                zero = float(np.mean(parts["zero_values"]))
                orbits = [
                    {"b": b, "energy": float(np.mean(values))}
                    for b, values in sorted(parts["orbit_values"].items())
                ]
                reconstructed = zero + sum(row["energy"] for row in orbits)
                maximum_averaged_closure_error = max(
                    maximum_averaged_closure_error, abs(reconstructed - total)
                )
                saved = saved_lookup[(exp, r, k)]
                exact_rows.append(
                    {
                        "exp": exp,
                        "r": r,
                        "k": k,
                        "on_value_count": len(on_values),
                        "decomposed_on_energy": total,
                        "saved_on_energy": saved,
                        "absolute_relative_error": abs(total - saved) / saved,
                        "zero_residue_energy": zero,
                        "orbits": orbits,
                        "averaged_closure_error": reconstructed - total,
                    }
                )
                for numerator, denominator in COVERAGE_LADDER:
                    label = f"{numerator}/{denominator}"
                    count = coverage_count(len(on_values), numerator, denominator)
                    sampled = float(np.mean(parts["total_values"][order[:count]]))
                    ladder_rows[label].append(
                        {
                            "exp": exp,
                            "r": r,
                            "k": k,
                            "sample_count": count,
                            "sampled_on_energy": sampled,
                            "saved_on_energy": saved,
                        }
                    )
        del f_all

    diagnostics = {
        "fft_length": fft_length,
        "maximum_pointwise_closure_error": maximum_pointwise_closure_error,
        "maximum_averaged_closure_error": maximum_averaged_closure_error,
        "candidate_counts": candidate_counts,
    }
    return exact_rows, ladder_rows, diagnostics


def full_gate(exact_rows: Sequence[dict], scan_diagnostics: Mapping) -> dict:
    metrics = calibration_metrics(
        exact_rows, "decomposed_on_energy", "saved_on_energy"
    )
    zero_ranges = []
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            values = [
                row["zero_residue_energy"]
                for row in exact_rows
                if row["exp"] == exp and row["r"] == r
            ]
            zero_ranges.append(max(values) - min(values))
    maximum_zero_range = max(zero_ranges)
    conditions = {
        "maximum_relative_error_at_most_1e_10": metrics[
            "maximum_absolute_relative_error"
        ]
        <= FULL_MAX_RELATIVE_ERROR,
        "centered_log_correlation_at_least_1_minus_1e_10": metrics[
            "centered_log_correlation"
        ]
        >= FULL_CORRELATION_MIN,
        "zero_residue_range_at_most_1e_12": maximum_zero_range
        <= INDEPENDENCE_TOLERANCE,
        "maximum_closure_error_at_most_1e_10": max(
            scan_diagnostics["maximum_pointwise_closure_error"],
            scan_diagnostics["maximum_averaged_closure_error"],
        )
        <= CLOSURE_TOLERANCE,
    }
    return {
        **metrics,
        "maximum_zero_residue_range_across_characters": maximum_zero_range,
        "maximum_pointwise_closure_error": scan_diagnostics[
            "maximum_pointwise_closure_error"
        ],
        "maximum_averaged_closure_error": scan_diagnostics[
            "maximum_averaged_closure_error"
        ],
        "thresholds": {
            "maximum_relative_error": FULL_MAX_RELATIVE_ERROR,
            "minimum_centered_log_correlation": FULL_CORRELATION_MIN,
            "maximum_zero_residue_range": INDEPENDENCE_TOLERANCE,
            "maximum_closure_error": CLOSURE_TOLERANCE,
        },
        "conditions": conditions,
        "passed": all(conditions.values()),
    }


def ladder_analysis(ladder_rows: Mapping[str, Sequence[dict]]) -> dict:
    steps = []
    for numerator, denominator in COVERAGE_LADDER:
        label = f"{numerator}/{denominator}"
        rows = ladder_rows[label]
        metrics = calibration_metrics(rows, "sampled_on_energy", "saved_on_energy")
        counts = [int(row["sample_count"]) for row in rows]
        passed = (
            metrics["centered_log_correlation"] >= SAMPLE_CORRELATION_MIN
            and metrics["median_absolute_relative_error"]
            <= SAMPLE_MEDIAN_RELATIVE_ERROR_MAX
        )
        steps.append(
            {
                "fraction": label,
                "numerator": numerator,
                "denominator": denominator,
                "minimum_sample_count": min(counts),
                "maximum_sample_count": max(counts),
                **metrics,
                "passed_pass027_calibration": passed,
            }
        )
    stable = None
    for index, row in enumerate(steps):
        if all(later["passed_pass027_calibration"] for later in steps[index:]):
            stable = row["fraction"]
            break
    return {
        "thresholds": {
            "minimum_centered_log_correlation": SAMPLE_CORRELATION_MIN,
            "maximum_median_absolute_relative_error": SAMPLE_MEDIAN_RELATIVE_ERROR_MAX,
        },
        "first_stable_fraction": stable,
        "steps": steps,
    }


def residual_component_rows(rows: Sequence[dict]) -> tuple[list[dict], dict]:
    centered: list[dict] = []
    maximum_centered_zero = 0.0
    maximum_centered_reconstruction = 0.0
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            local = sorted(
                (row for row in rows if row["exp"] == exp and row["r"] == r),
                key=lambda row: row["k"],
            )
            orbit_ids = list(range(1, (r - 1) // 2 + 1))
            mean_total = statistics.fmean(row["decomposed_on_energy"] for row in local)
            mean_zero = statistics.fmean(row["zero_residue_energy"] for row in local)
            mean_orbits = {
                b: statistics.fmean(
                    next(item["energy"] for item in row["orbits"] if item["b"] == b)
                    for row in local
                )
                for b in orbit_ids
            }
            for row in local:
                total = row["decomposed_on_energy"] - mean_total
                zero = row["zero_residue_energy"] - mean_zero
                orbits = {
                    b: next(item["energy"] for item in row["orbits"] if item["b"] == b)
                    - mean_orbits[b]
                    for b in orbit_ids
                }
                maximum_centered_zero = max(maximum_centered_zero, abs(zero))
                maximum_centered_reconstruction = max(
                    maximum_centered_reconstruction,
                    abs(total - zero - sum(orbits.values())),
                )
                centered.append(
                    {
                        "exp": exp,
                        "r": r,
                        "k": row["k"],
                        "centered_total": total,
                        "centered_zero": zero,
                        "centered_orbits": orbits,
                    }
                )

    means: dict[tuple[int, int], dict] = {}
    for r in PRIMARY_MODULI:
        for k in representative_modes(r):
            local = [row for row in centered if row["r"] == r and row["k"] == k]
            means[(r, k)] = {
                "total": statistics.fmean(row["centered_total"] for row in local),
                "zero": statistics.fmean(row["centered_zero"] for row in local),
                "orbits": {
                    b: statistics.fmean(row["centered_orbits"][b] for row in local)
                    for b in local[0]["centered_orbits"]
                },
            }
    residuals = []
    maximum_residual_reconstruction = 0.0
    for row in centered:
        mean = means[(row["r"], row["k"])]
        total = row["centered_total"] - mean["total"]
        zero = row["centered_zero"] - mean["zero"]
        orbits = {
            b: row["centered_orbits"][b] - mean["orbits"][b]
            for b in row["centered_orbits"]
        }
        maximum_residual_reconstruction = max(
            maximum_residual_reconstruction, abs(total - zero - sum(orbits.values()))
        )
        residuals.append(
            {
                "exp": row["exp"],
                "r": row["r"],
                "k": row["k"],
                "residual_total": total,
                "residual_zero": zero,
                "residual_orbits": orbits,
            }
        )
    return residuals, {
        "maximum_absolute_centered_zero_residue": maximum_centered_zero,
        "maximum_centered_reconstruction_error": maximum_centered_reconstruction,
        "maximum_residual_reconstruction_error": maximum_residual_reconstruction,
    }


def linear_attribution(y: Sequence[float], components: Mapping[int, Sequence[float]]) -> dict:
    if not y or any(len(values) != len(y) for values in components.values()):
        raise ValueError("Attribution vectors must be nonempty and equally sized")
    ss = sum(value * value for value in y)
    if ss <= 0:
        raise ValueError("Degenerate residual energy")
    rows = []
    for b, values in components.items():
        phi = sum(target * value for target, value in zip(y, values))
        rows.append({"b": b, "phi": phi, "signed_share": phi / ss})
    absolute_sum = sum(abs(row["phi"]) for row in rows)
    for row in rows:
        row["absolute_fraction"] = abs(row["phi"]) / absolute_sum
    ranked = sorted(rows, key=lambda row: (-row["absolute_fraction"], row["b"]))
    return {
        "row_count": len(y),
        "residual_sum_of_squares": ss,
        "signed_share_sum": sum(row["signed_share"] for row in rows),
        "absolute_phi_sum": absolute_sum,
        "orbits": sorted(rows, key=lambda row: row["b"]),
        "top_orbit_b": ranked[0]["b"],
        "top_absolute_fraction": ranked[0]["absolute_fraction"],
        "top_three_absolute_fraction": sum(
            row["absolute_fraction"] for row in ranked[:3]
        ),
    }


def concentration_analysis(residuals: Sequence[dict], gate_passed: bool) -> dict:
    by_modulus = []
    for r in PRIMARY_MODULI:
        local = [row for row in residuals if row["r"] == r]
        orbit_ids = list(range(1, (r - 1) // 2 + 1))
        y = [row["residual_total"] for row in local]
        components = {
            b: [row["residual_orbits"][b] for row in local] for b in orbit_ids
        }
        attribution = linear_attribution(y, components)
        attribution["r"] = r
        by_modulus.append(attribution)
    concentrated_count = sum(
        row["top_absolute_fraction"] >= CONCENTRATION_THRESHOLD for row in by_modulus
    )
    if not gate_passed:
        decision = "full_scan_gate_failed_no_concentration_classification"
    elif concentrated_count >= CONCENTRATION_MODULUS_COUNT:
        decision = "single_nonzero_difference_orbit_concentrated"
    else:
        decision = "distributed_across_multiple_nonzero_difference_orbits"
    return {
        "thresholds": {
            "top_absolute_fraction": CONCENTRATION_THRESHOLD,
            "required_modulus_count": CONCENTRATION_MODULUS_COUNT,
        },
        "concentrated_modulus_count": concentrated_count,
        "modulus_count": len(by_modulus),
        "decision": decision,
        "by_modulus": by_modulus,
        "maximum_signed_share_sum_error": max(
            abs(row["signed_share_sum"] - 1.0) for row in by_modulus
        ),
    }


def build_result(
    pass023_path: Path, holdout_path: Path, progress: bool = False
) -> dict:
    saved_rows = load_full_rows(pass023_path, holdout_path)
    exact_rows, ladder_rows, scan_diagnostics = full_scan(saved_rows, progress=progress)
    if len(exact_rows) != 160:
        raise AssertionError(f"Expected 160 exact rows, received {len(exact_rows)}")
    gate = full_gate(exact_rows, scan_diagnostics)
    ladder = ladder_analysis(ladder_rows)
    residuals, residual_diagnostics = residual_component_rows(exact_rows)
    concentration = concentration_analysis(residuals, gate["passed"])
    return {
        "pass": "PASS028",
        "title": "Full on-state residue-fiber scan and sample convergence",
        "classification": "finite complete-range algebraic and computational diagnostic",
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(EXPS),
            "moduli": list(PRIMARY_MODULI),
            "coverage_ladder": [f"{a}/{b}" for a, b in COVERAGE_LADDER],
            "sample_order": "SplitMix64(N with fixed (e,r) salt), nested prefixes",
            "character_selection": "one representative per conjugate pair of even nonprincipal characters",
            "input_sha256": {
                pass023_path.name: sha256_file(pass023_path),
                holdout_path.name: sha256_file(holdout_path),
            },
        },
        "full_scan_gate": gate,
        "sample_convergence": ladder,
        "concentration": concentration,
        "identity_diagnostics": {
            **residual_diagnostics,
            "maximum_pointwise_closure_error": scan_diagnostics[
                "maximum_pointwise_closure_error"
            ],
            "maximum_averaged_closure_error": scan_diagnostics[
                "maximum_averaged_closure_error"
            ],
            "maximum_signed_share_sum_error": concentration[
                "maximum_signed_share_sum_error"
            ],
        },
        "fft_length": scan_diagnostics["fft_length"],
        "candidate_counts": scan_diagnostics["candidate_counts"],
        "exact_rows": exact_rows,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass023", type=Path, default=default_pass023_path())
    parser.add_argument("--holdout", type=Path, default=default_pass025_holdout_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument("--progress", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(args.pass023, args.holdout, progress=args.progress)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS028 result: {args.output}")
    print(
        "full gate:",
        result["full_scan_gate"]["passed"],
        "max_relative_error=",
        f'{result["full_scan_gate"]["maximum_absolute_relative_error"]:.3e}',
    )
    print(
        "sample first stable fraction:",
        result["sample_convergence"]["first_stable_fraction"],
    )
    print("decision:", result["concentration"]["decision"])


if __name__ == "__main__":
    main()
