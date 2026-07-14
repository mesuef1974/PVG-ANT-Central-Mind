#!/usr/bin/env python3
"""PASS026: exact log-energy separation of on and off character variation.

For every row, log(rho) = log(E_on) - log(E_off).  The program centers
these quantities within each modulus/window, removes each character's
five-window mean, and symmetrically allocates the remaining sum of squares
between the on and off channels.

Finite computational diagnostic only; no asymptotic or Goldbach proof claim.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Sequence


EXPS = (15, 16, 17, 18, 19)
TRAIN_EXPS = (15, 16, 17, 18)
ALL_MODULI = (5, 7, 11, 13, 17, 19, 23, 29, 31)
PRIMARY_MODULI = (11, 13, 17, 19, 23, 29, 31)


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
        return archive_results / "avrg_pass026_results.json"
    return here / "avrg_pass026_results.json"


def normalize_row(raw: dict, exp: int) -> dict:
    r, k = int(raw["r"]), int(raw["k"])
    rho = float(raw["energy_ratio"])
    on_energy = float(raw["on_energy"])
    off_energy = float(raw["off_energy"])
    if r not in ALL_MODULI:
        raise ValueError(f"Unexpected modulus: {(exp, r)}")
    if k <= 0 or k % 2 or k > r - 1 - k:
        raise ValueError(f"Invalid character representative: {(exp, r, k)}")
    if any(not math.isfinite(value) or value <= 0 for value in (rho, on_energy, off_energy)):
        raise ValueError(f"Nonpositive or nonfinite energy at {(exp, r, k)}")
    reconstructed = on_energy / off_energy
    relative_error = abs(reconstructed - rho) / rho
    if relative_error > 1e-12:
        raise ValueError(f"rho != on/off at {(exp, r, k)}: {relative_error}")
    return {
        "exp": exp,
        "r": r,
        "k": k,
        "rho": rho,
        "on_energy": on_energy,
        "off_energy": off_energy,
    }


def load_rows(pass023_path: Path, holdout_path: Path) -> list[dict]:
    with pass023_path.open("r", encoding="utf-8") as handle:
        pass023 = json.load(handle)
    config = pass023.get("configuration", {})
    if tuple(config.get("exps", [])) != TRAIN_EXPS:
        raise ValueError("PASS023 windows differ from e=15..18")
    if tuple(config.get("moduli", [])) != ALL_MODULI:
        raise ValueError("PASS023 moduli differ from the locked set")
    windows = pass023.get("windows", [])
    if tuple(int(window["exp"]) for window in windows) != TRAIN_EXPS:
        raise ValueError("PASS023 window payload differs from the lock")
    rows = [
        normalize_row(raw, int(window["exp"]))
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
    rows.extend(normalize_row(raw, 19) for raw in window.get("rows", []))

    rows = [row for row in rows if row["r"] in PRIMARY_MODULI]
    if len(rows) != 160:
        raise ValueError(f"Expected 160 primary rows, received {len(rows)}")
    keys = {(row["exp"], row["r"], row["k"]) for row in rows}
    if len(keys) != len(rows):
        raise ValueError("Duplicate (e,r,k) rows")
    return rows


def centered_log_rows(rows: Sequence[dict]) -> list[dict]:
    output: list[dict] = []
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            local = sorted(
                (row for row in rows if row["exp"] == exp and row["r"] == r),
                key=lambda row: row["k"],
            )
            if not local:
                raise ValueError(f"No rows for {(exp, r)}")
            log_on = [math.log(row["on_energy"]) for row in local]
            log_off = [math.log(row["off_energy"]) for row in local]
            log_ratio = [math.log(row["rho"]) for row in local]
            mean_on = sum(log_on) / len(log_on)
            mean_off = sum(log_off) / len(log_off)
            mean_ratio = sum(log_ratio) / len(log_ratio)
            for row, raw_a, raw_b, raw_y in zip(local, log_on, log_off, log_ratio):
                a = raw_a - mean_on
                b = raw_b - mean_off
                y = raw_y - mean_ratio
                if abs(y - (a - b)) > 2e-12:
                    raise AssertionError("Centered log identity failed")
                output.append(
                    {
                        "exp": exp,
                        "r": r,
                        "k": row["k"],
                        "a_on": a,
                        "b_off": b,
                        "y_log_ratio": y,
                    }
                )
            for field in ("a_on", "b_off", "y_log_ratio"):
                if abs(sum(row[field] for row in output if row["exp"] == exp and row["r"] == r)) > 1e-12:
                    raise AssertionError(f"Within-(e,r) centering failed: {(exp, r, field)}")
    return output


def remove_character_means(centered: Sequence[dict], exps: Sequence[int] = EXPS) -> list[dict]:
    selected = [row for row in centered if row["exp"] in exps]
    means: dict[tuple[int, int], dict[str, float]] = {}
    for r in PRIMARY_MODULI:
        modes = sorted({row["k"] for row in selected if row["r"] == r})
        for k in modes:
            local = [row for row in selected if row["r"] == r and row["k"] == k]
            if len(local) != len(exps):
                raise ValueError(f"Incomplete window history for {(r, k)}")
            means[(r, k)] = {
                field: sum(row[field] for row in local) / len(local)
                for field in ("a_on", "b_off", "y_log_ratio")
            }
    output = []
    for row in selected:
        mean = means[(row["r"], row["k"])]
        a = row["a_on"] - mean["a_on"]
        b = row["b_off"] - mean["b_off"]
        y = row["y_log_ratio"] - mean["y_log_ratio"]
        if abs(y - (a - b)) > 2e-12:
            raise AssertionError("Window-residual log identity failed")
        output.append({**row, "a_on_residual": a, "b_off_residual": b, "y_residual": y})
    return output


def channel_metrics(a_values: Sequence[float], b_values: Sequence[float]) -> dict:
    if len(a_values) != len(b_values) or not a_values:
        raise ValueError("Channel vectors must be nonempty and have equal length")
    ss_a = sum(value * value for value in a_values)
    ss_b = sum(value * value for value in b_values)
    covariance_sum = sum(a * b for a, b in zip(a_values, b_values))
    y_values = [a - b for a, b in zip(a_values, b_values)]
    ss_y = sum(value * value for value in y_values)
    identity_error = ss_y - (ss_a + ss_b - 2.0 * covariance_sum)
    if abs(identity_error) > 1e-11 * max(1.0, ss_y):
        raise AssertionError("Log-energy sum-of-squares identity failed")
    on_attribution = ss_a - covariance_sum
    off_attribution = ss_b - covariance_sum
    if ss_y <= 0:
        raise ValueError("Degenerate ratio variation")
    on_share = on_attribution / ss_y
    off_share = off_attribution / ss_y
    if abs(on_share + off_share - 1.0) > 1e-12:
        raise AssertionError("Attribution shares do not sum to one")
    return {
        "row_count": len(a_values),
        "ratio_ss": ss_y,
        "on_ss": ss_a,
        "off_ss": ss_b,
        "on_off_covariance_sum": covariance_sum,
        "on_attribution": on_attribution,
        "off_attribution": off_attribution,
        "on_share": on_share,
        "off_share": off_share,
        "on_only_sse": ss_b,
        "off_only_sse": ss_a,
        "on_only_skill_vs_zero": 1.0 - ss_b / ss_y,
        "off_only_skill_vs_zero": 1.0 - ss_a / ss_y,
        "identity_error": identity_error,
    }


def metrics_from_rows(rows: Sequence[dict], residual: bool) -> dict:
    a_field = "a_on_residual" if residual else "a_on"
    b_field = "b_off_residual" if residual else "b_off"
    return channel_metrics([row[a_field] for row in rows], [row[b_field] for row in rows])


def dominance_decision(global_metrics: dict, by_window: Sequence[dict], loo: Sequence[dict]) -> dict:
    off_windows = sum(row["metrics"]["off_share"] > 0.50 for row in by_window)
    on_windows = sum(row["metrics"]["on_share"] > 0.50 for row in by_window)
    off_conditions = {
        "global_off_share_gt_0_60": global_metrics["off_share"] > 0.60,
        "off_majority_in_at_least_four_windows": off_windows >= 4,
        "all_leave_one_out_off_share_gt_0_50": all(
            row["metrics"]["off_share"] > 0.50 for row in loo
        ),
        "off_only_sse_lt_on_only_sse": global_metrics["off_only_sse"] < global_metrics["on_only_sse"],
    }
    on_conditions = {
        "global_on_share_gt_0_60": global_metrics["on_share"] > 0.60,
        "on_majority_in_at_least_four_windows": on_windows >= 4,
        "all_leave_one_out_on_share_gt_0_50": all(
            row["metrics"]["on_share"] > 0.50 for row in loo
        ),
        "on_only_sse_lt_off_only_sse": global_metrics["on_only_sse"] < global_metrics["off_only_sse"],
    }
    off_passed = all(off_conditions.values())
    on_passed = all(on_conditions.values())
    if off_passed:
        label = "off_channel_dominates_window_instability"
    elif on_passed:
        label = "on_channel_dominates_window_instability"
    else:
        label = "mixed_no_channel_meets_dominance_rule"
    return {
        "off_conditions": off_conditions,
        "on_conditions": on_conditions,
        "off_majority_window_count": off_windows,
        "on_majority_window_count": on_windows,
        "decision": label,
        "off_dominance_passed": off_passed,
        "on_dominance_passed": on_passed,
    }


def analyze(rows: Sequence[dict]) -> dict:
    centered = centered_log_rows(rows)
    residuals = remove_character_means(centered)
    global_residual = metrics_from_rows(residuals, residual=True)
    total_heterogeneity = metrics_from_rows(centered, residual=False)
    by_window = [
        {
            "exp": exp,
            "metrics": metrics_from_rows(
                [row for row in residuals if row["exp"] == exp], residual=True
            ),
        }
        for exp in EXPS
    ]
    by_modulus = [
        {
            "r": r,
            "metrics": metrics_from_rows(
                [row for row in residuals if row["r"] == r], residual=True
            ),
        }
        for r in PRIMARY_MODULI
    ]
    leave_one_out = []
    for omitted in EXPS:
        kept = tuple(exp for exp in EXPS if exp != omitted)
        local_residuals = remove_character_means(centered, exps=kept)
        leave_one_out.append(
            {
                "omitted_exp": omitted,
                "kept_exps": list(kept),
                "metrics": metrics_from_rows(local_residuals, residual=True),
            }
        )
    decision = dominance_decision(global_residual, by_window, leave_one_out)
    return {
        "pass": "PASS026",
        "title": "On/off log-energy decomposition of window instability",
        "classification": "finite exact algebraic computational diagnostic",
        "claim_ceiling": (
            "No asymptotic proof and no direct progress toward a proof of Goldbach."
        ),
        "locked_protocol": {
            "exps": list(EXPS),
            "moduli": list(PRIMARY_MODULI),
            "row_count": len(rows),
            "identity": "centered log(rho) = centered log(E_on) - centered log(E_off)",
            "primary_target": "five-window residual after removing each (r,k) mean",
            "off_dominance_rule": [
                "global off share > 0.60",
                "off share > 0.50 in at least four of five windows",
                "off share > 0.50 in every leave-one-window-out recomputation",
                "off-only SSE < on-only SSE",
            ],
        },
        "window_instability": {
            "global": global_residual,
            "by_window": by_window,
            "by_modulus": by_modulus,
            "leave_one_window_out": leave_one_out,
            "decision": decision,
        },
        "total_within_modulus_heterogeneity": total_heterogeneity,
        "decomposition_rows": residuals,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass023", type=Path, default=default_pass023_path())
    parser.add_argument(
        "--pass025-holdout", type=Path, default=default_pass025_holdout_path()
    )
    parser.add_argument("--output", type=Path, default=default_output_path())
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = load_rows(args.pass023, args.pass025_holdout)
    result = analyze(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    global_result = result["window_instability"]["global"]
    decision = result["window_instability"]["decision"]["decision"]
    print(f"PASS026 complete: {args.output}")
    print(
        f"on_share={global_result['on_share']:.6f} "
        f"off_share={global_result['off_share']:.6f} "
        f"off_only_skill={global_result['off_only_skill_vs_zero']:.6f}"
    )
    print(f"decision={decision}")


if __name__ == "__main__":
    main()
