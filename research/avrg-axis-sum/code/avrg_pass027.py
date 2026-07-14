#!/usr/bin/env python3
"""PASS027: decompose sampled on energy by residue-difference orbits.

For r | N, T_k(N) is first compressed into residue sums f_alpha.  Its
energy is then split exactly into b = alpha-beta (mod r), with b and -b
paired into real orbits.  The b=0 channel is character-independent, so all
within-modulus character variation comes from the nonzero orbits.

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
SAMPLE_COUNT = 16
CALIBRATION_CORRELATION_MIN = 0.90
CALIBRATION_MEDIAN_RELATIVE_ERROR_MAX = 0.10
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
        return archive_results / "avrg_pass027_results.json"
    return here / "avrg_pass027_results.json"


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
    """Even nonprincipal k, one representative per conjugate pair."""
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
    return {"exp": exp, "r": r, "k": k, "full_on_energy": on_energy}


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


def choose_on_values(exp: int, r: int, count: int = SAMPLE_COUNT) -> np.ndarray:
    """Choose deterministic, equally spaced even multiples of r."""
    lo, hi = 1 << exp, 1 << (exp + 1)
    step = 2 * r
    first = ((lo + step - 1) // step) * step
    candidates = np.arange(first, hi, step, dtype=np.int64)
    if len(candidates) < count:
        raise ValueError(f"Only {len(candidates)} on values for {(exp, r)}")
    indices = np.linspace(0, len(candidates) - 1, count, dtype=np.int64)
    selected = candidates[indices]
    if len(set(int(value) for value in selected)) != count:
        raise AssertionError("Equally spaced selection produced duplicates")
    return selected


def residue_components(f: np.ndarray, character: np.ndarray) -> dict:
    """Return the exact b=0 and paired nonzero difference contributions."""
    if f.ndim != 1 or character.shape != f.shape or len(f) % 2 == 0:
        raise ValueError("Expected equal one-dimensional arrays of odd prime length")
    z = character * f
    q = np.asarray(
        [np.sum(z * np.conjugate(np.roll(z, b))) for b in range(len(f))]
    )
    zero = float(q[0].real)
    orbits = {
        b: float((q[b] + q[-b]).real)
        for b in range(1, (len(f) - 1) // 2 + 1)
    }
    total_direct = float(abs(np.sum(z)) ** 2)
    reconstructed = zero + sum(orbits.values())
    return {
        "zero": zero,
        "orbits": orbits,
        "total": total_direct,
        "closure_error": reconstructed - total_direct,
        "zero_identity_error": zero - float(np.sum(f[1:] ** 2)),
    }


def sample_window(
    exp: int, full_lookup: Mapping[tuple[int, int, int], float], progress: bool = False
) -> tuple[list[dict], list[dict], dict]:
    lo, hi = 1 << exp, 1 << (exp + 1)
    theta = sieve_theta(hi)
    main = singular_main(hi)
    n = np.arange(hi + 1, dtype=np.int64)
    rows: list[dict] = []
    selections: list[dict] = []
    maximum_closure_error = 0.0
    maximum_zero_identity_error = 0.0

    for r in PRIMARY_MODULI:
        selected = choose_on_values(exp, r)
        selections.append({"exp": exp, "r": r, "N": [int(value) for value in selected]})
        modes = representative_modes(r)
        characters = {k: character_on_residues(r, k) for k in modes}
        accumulators = {
            k: {
                "total": 0.0,
                "zero": 0.0,
                "diagonal": 0.0,
                "orbits": {b: 0.0 for b in range(1, (r - 1) // 2 + 1)},
            }
            for k in modes
        }
        residues = n % r
        if progress:
            print(f"PASS027 sample e={exp} r={r} N={len(selected)} k={len(modes)}", flush=True)

        for raw_N in selected:
            N = int(raw_N)
            weights = theta[: N + 1] * theta[N::-1]
            f = np.bincount(residues[: N + 1], weights=weights, minlength=r)
            diagonal = float(np.sum(weights[residues[: N + 1] != 0] ** 2))
            norm = float(main[N] ** 2 * (r - 1))
            if norm <= 0:
                raise ValueError(f"Nonpositive normalization at {(exp, r, N)}")
            for k in modes:
                parts = residue_components(f, characters[k])
                maximum_closure_error = max(
                    maximum_closure_error, abs(parts["closure_error"] / norm)
                )
                maximum_zero_identity_error = max(
                    maximum_zero_identity_error, abs(parts["zero_identity_error"] / norm)
                )
                acc = accumulators[k]
                acc["total"] += parts["total"] / norm
                acc["zero"] += parts["zero"] / norm
                acc["diagonal"] += diagonal / norm
                for b, value in parts["orbits"].items():
                    acc["orbits"][b] += value / norm

        for k in modes:
            acc = accumulators[k]
            sampled = acc["total"] / SAMPLE_COUNT
            zero = acc["zero"] / SAMPLE_COUNT
            diagonal = acc["diagonal"] / SAMPLE_COUNT
            orbit_rows = [
                {"b": b, "energy": acc["orbits"][b] / SAMPLE_COUNT}
                for b in sorted(acc["orbits"])
            ]
            reconstructed = zero + sum(row["energy"] for row in orbit_rows)
            full = full_lookup[(exp, r, k)]
            rows.append(
                {
                    "exp": exp,
                    "r": r,
                    "k": k,
                    "sampled_on_energy": sampled,
                    "full_on_energy": full,
                    "absolute_relative_error": abs(sampled - full) / full,
                    "zero_residue_energy": zero,
                    "diagonal_energy": diagonal,
                    "zero_residue_offdiagonal_energy": zero - diagonal,
                    "orbits": orbit_rows,
                    "averaged_closure_error": reconstructed - sampled,
                }
            )

    diagnostics = {
        "window": [lo, hi],
        "maximum_single_N_normalized_closure_error": maximum_closure_error,
        "maximum_single_N_normalized_zero_identity_error": maximum_zero_identity_error,
    }
    return rows, selections, diagnostics


def centered_pairs(rows: Sequence[dict]) -> tuple[list[float], list[float]]:
    sampled_centered: list[float] = []
    full_centered: list[float] = []
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            local = [row for row in rows if row["exp"] == exp and row["r"] == r]
            sample_logs = [math.log(row["sampled_on_energy"]) for row in local]
            full_logs = [math.log(row["full_on_energy"]) for row in local]
            sample_mean = statistics.fmean(sample_logs)
            full_mean = statistics.fmean(full_logs)
            sampled_centered.extend(value - sample_mean for value in sample_logs)
            full_centered.extend(value - full_mean for value in full_logs)
    return sampled_centered, full_centered


def vector_correlation(xs: Sequence[float], ys: Sequence[float]) -> float:
    if len(xs) != len(ys) or not xs:
        raise ValueError("Correlation vectors must be nonempty and equally sized")
    xmean, ymean = statistics.fmean(xs), statistics.fmean(ys)
    xc = [value - xmean for value in xs]
    yc = [value - ymean for value in ys]
    denominator = math.sqrt(sum(value * value for value in xc) * sum(value * value for value in yc))
    if denominator == 0:
        raise ValueError("Degenerate correlation")
    return sum(x * y for x, y in zip(xc, yc)) / denominator


def calibration_summary(rows: Sequence[dict]) -> dict:
    sampled, full = centered_pairs(rows)
    correlation = vector_correlation(sampled, full)
    median_error = statistics.median(row["absolute_relative_error"] for row in rows)
    by_window = []
    for exp in EXPS:
        local = [row for row in rows if row["exp"] == exp]
        local_sampled, local_full = centered_pairs_for_groups(local)
        by_window.append(
            {
                "exp": exp,
                "centered_log_correlation": vector_correlation(local_sampled, local_full),
                "median_absolute_relative_error": statistics.median(
                    row["absolute_relative_error"] for row in local
                ),
                "maximum_absolute_relative_error": max(
                    row["absolute_relative_error"] for row in local
                ),
            }
        )
    conditions = {
        "centered_log_correlation_at_least_0_90": correlation >= CALIBRATION_CORRELATION_MIN,
        "median_absolute_relative_error_at_most_0_10": median_error
        <= CALIBRATION_MEDIAN_RELATIVE_ERROR_MAX,
    }
    return {
        "row_count": len(rows),
        "centered_log_correlation": correlation,
        "median_absolute_relative_error": median_error,
        "maximum_absolute_relative_error": max(row["absolute_relative_error"] for row in rows),
        "thresholds": {
            "minimum_centered_log_correlation": CALIBRATION_CORRELATION_MIN,
            "maximum_median_absolute_relative_error": CALIBRATION_MEDIAN_RELATIVE_ERROR_MAX,
        },
        "conditions": conditions,
        "passed": all(conditions.values()),
        "by_window": by_window,
    }


def centered_pairs_for_groups(rows: Sequence[dict]) -> tuple[list[float], list[float]]:
    sampled_centered: list[float] = []
    full_centered: list[float] = []
    for r in sorted({int(row["r"]) for row in rows}):
        local = [row for row in rows if row["r"] == r]
        sample_logs = [math.log(row["sampled_on_energy"]) for row in local]
        full_logs = [math.log(row["full_on_energy"]) for row in local]
        sample_mean = statistics.fmean(sample_logs)
        full_mean = statistics.fmean(full_logs)
        sampled_centered.extend(value - sample_mean for value in sample_logs)
        full_centered.extend(value - full_mean for value in full_logs)
    return sampled_centered, full_centered


def residual_component_rows(rows: Sequence[dict]) -> tuple[list[dict], dict]:
    centered: list[dict] = []
    maximum_zero_centered = 0.0
    maximum_diagonal_centered = 0.0
    maximum_centered_reconstruction = 0.0
    zero_ranges = []

    for exp in EXPS:
        for r in PRIMARY_MODULI:
            local = sorted(
                (row for row in rows if row["exp"] == exp and row["r"] == r),
                key=lambda row: row["k"],
            )
            orbit_ids = list(range(1, (r - 1) // 2 + 1))
            means = {
                "total": statistics.fmean(row["sampled_on_energy"] for row in local),
                "zero": statistics.fmean(row["zero_residue_energy"] for row in local),
                "diagonal": statistics.fmean(row["diagonal_energy"] for row in local),
                "orbits": {
                    b: statistics.fmean(
                        next(item["energy"] for item in row["orbits"] if item["b"] == b)
                        for row in local
                    )
                    for b in orbit_ids
                },
            }
            zero_values = [row["zero_residue_energy"] for row in local]
            diagonal_values = [row["diagonal_energy"] for row in local]
            zero_ranges.append(
                {
                    "exp": exp,
                    "r": r,
                    "zero_residue_range_across_characters": max(zero_values) - min(zero_values),
                    "diagonal_range_across_characters": max(diagonal_values) - min(diagonal_values),
                }
            )
            for row in local:
                total = row["sampled_on_energy"] - means["total"]
                zero = row["zero_residue_energy"] - means["zero"]
                diagonal = row["diagonal_energy"] - means["diagonal"]
                orbit_values = {
                    b: next(item["energy"] for item in row["orbits"] if item["b"] == b)
                    - means["orbits"][b]
                    for b in orbit_ids
                }
                maximum_zero_centered = max(maximum_zero_centered, abs(zero))
                maximum_diagonal_centered = max(maximum_diagonal_centered, abs(diagonal))
                maximum_centered_reconstruction = max(
                    maximum_centered_reconstruction,
                    abs(total - zero - sum(orbit_values.values())),
                )
                centered.append(
                    {
                        "exp": exp,
                        "r": r,
                        "k": row["k"],
                        "centered_total": total,
                        "centered_zero": zero,
                        "centered_diagonal": diagonal,
                        "centered_orbits": orbit_values,
                    }
                )

    means: dict[tuple[int, int], dict] = {}
    for r in PRIMARY_MODULI:
        for k in representative_modes(r):
            local = [row for row in centered if row["r"] == r and row["k"] == k]
            if len(local) != len(EXPS):
                raise ValueError(f"Incomplete history for {(r, k)}")
            means[(r, k)] = {
                "total": statistics.fmean(row["centered_total"] for row in local),
                "zero": statistics.fmean(row["centered_zero"] for row in local),
                "diagonal": statistics.fmean(row["centered_diagonal"] for row in local),
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
        diagonal = row["centered_diagonal"] - mean["diagonal"]
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
                "residual_diagonal": diagonal,
                "residual_orbits": orbits,
            }
        )

    diagnostics = {
        "maximum_zero_residue_range_across_characters": max(
            row["zero_residue_range_across_characters"] for row in zero_ranges
        ),
        "maximum_diagonal_range_across_characters": max(
            row["diagonal_range_across_characters"] for row in zero_ranges
        ),
        "maximum_absolute_centered_zero_residue": maximum_zero_centered,
        "maximum_absolute_centered_diagonal": maximum_diagonal_centered,
        "maximum_centered_reconstruction_error": maximum_centered_reconstruction,
        "maximum_residual_reconstruction_error": maximum_residual_reconstruction,
        "by_window_modulus": zero_ranges,
    }
    return residuals, diagnostics


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


def concentration_analysis(residuals: Sequence[dict], calibration_passed: bool) -> dict:
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
    if not calibration_passed:
        decision = "sample_calibration_failed_no_concentration_classification"
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


def zero_channel_summary(rows: Sequence[dict]) -> dict:
    ratios = [row["diagonal_energy"] / row["zero_residue_energy"] for row in rows]
    return {
        "median_diagonal_fraction_of_zero_residue_energy": statistics.median(ratios),
        "minimum_diagonal_fraction_of_zero_residue_energy": min(ratios),
        "maximum_diagonal_fraction_of_zero_residue_energy": max(ratios),
    }


def build_result(
    pass023_path: Path, holdout_path: Path, progress: bool = False
) -> dict:
    full_rows = load_full_rows(pass023_path, holdout_path)
    full_lookup = {
        (row["exp"], row["r"], row["k"]): row["full_on_energy"]
        for row in full_rows
    }
    sampled_rows: list[dict] = []
    selections: list[dict] = []
    window_diagnostics = []
    for exp in EXPS:
        rows, selected, diagnostics = sample_window(exp, full_lookup, progress=progress)
        sampled_rows.extend(rows)
        selections.extend(selected)
        window_diagnostics.append({"exp": exp, **diagnostics})
    if len(sampled_rows) != len(full_rows):
        raise AssertionError("Sampled/full row count mismatch")

    calibration = calibration_summary(sampled_rows)
    residuals, identity_diagnostics = residual_component_rows(sampled_rows)
    concentration = concentration_analysis(residuals, calibration["passed"])
    return {
        "pass": "PASS027",
        "title": "On-energy residue-difference orbit decomposition",
        "classification": "finite algebraic and computational diagnostic",
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(EXPS),
            "moduli": list(PRIMARY_MODULI),
            "sample_count_per_window_modulus": SAMPLE_COUNT,
            "character_selection": "one representative per conjugate pair of even nonprincipal characters",
            "selection": "deterministic equally spaced even multiples of r",
            "input_sha256": {
                pass023_path.name: sha256_file(pass023_path),
                holdout_path.name: sha256_file(holdout_path),
            },
        },
        "algebraic_identity": {
            "zero_residue_character_independent": True,
            "all_within_modulus_character_variation_from_nonzero_orbits": True,
            "orbit_pairing": "b with r-b, contribution 2 Re Q_b",
        },
        "calibration": calibration,
        "concentration": concentration,
        "zero_channel": zero_channel_summary(sampled_rows),
        "identity_diagnostics": {
            **identity_diagnostics,
            "maximum_single_N_normalized_closure_error": max(
                row["maximum_single_N_normalized_closure_error"]
                for row in window_diagnostics
            ),
            "maximum_single_N_normalized_zero_identity_error": max(
                row["maximum_single_N_normalized_zero_identity_error"]
                for row in window_diagnostics
            ),
            "maximum_averaged_closure_error": max(
                abs(row["averaged_closure_error"]) for row in sampled_rows
            ),
        },
        "window_diagnostics": window_diagnostics,
        "sample_selections": selections,
        "sampled_rows": sampled_rows,
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
    print(f"PASS027 result: {args.output}")
    print(
        "calibration:",
        result["calibration"]["passed"],
        "correlation=",
        f'{result["calibration"]["centered_log_correlation"]:.6f}',
        "median_relative_error=",
        f'{result["calibration"]["median_absolute_relative_error"]:.6f}',
    )
    print("decision:", result["concentration"]["decision"])


if __name__ == "__main__":
    main()
