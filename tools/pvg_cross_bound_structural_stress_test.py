from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Any, Iterable

try:
    from tools.pvg_additive_attraction_basins import analyze as analyze_basins
    from tools.pvg_prime_bound_expansion_protocol import (
        _summarize_records,
        analyze as analyze_expansion,
        face_key,
        parse_limits,
    )
except ModuleNotFoundError:
    from pvg_additive_attraction_basins import analyze as analyze_basins
    from pvg_prime_bound_expansion_protocol import (
        _summarize_records,
        analyze as analyze_expansion,
        face_key,
        parse_limits,
    )

REGISTERED_LIMITS = (100, 150, 200, 250, 300, 400)
REGISTERED_DEPTH = 5
REGISTERED_REPAIR_DEPTH_CAP = 8
TARGET_AXIS = 5
TARGET_EDGE = (5, 7)

@dataclass(frozen=True)
class CandidateSpec:
    key: str
    description: str
    scope: str

CANDIDATES = (
    CandidateSpec("largest_basin_axis_5", "axis 5 is the unique largest observed basin axis", "cumulative and incremental cohort snapshots"),
    CandidateSpec("maximum_weighted_degree_axis_5", "axis 5 is the unique maximum weighted-overlap-degree axis", "cumulative and incremental cohort snapshots"),
    CandidateSpec("strongest_overlap_edge_5_7", "{5,7} is the unique strongest positive overlap edge", "cumulative and incremental cohort snapshots"),
    CandidateSpec("maximum_signature_rank_non_decreasing", "maximum observed nonempty endpoint-signature rank is non-decreasing", "cumulative snapshots"),
    CandidateSpec("active_component_size_non_decreasing", "active overlap-component size is non-decreasing", "cumulative snapshots"),
    CandidateSpec("fixed_depth_closure", "every registered start face closes by the fixed depth", "cumulative snapshots"),
)

def _strictly_increasing(values: Iterable[int]) -> bool:
    seq = list(values)
    return all(a < b for a, b in zip(seq, seq[1:]))

def _non_decreasing(values: Iterable[int | float]) -> bool:
    seq = list(values)
    return all(a <= b for a, b in zip(seq, seq[1:]))

def _nonempty_signature_count(snapshot: dict[str, Any]) -> int:
    return sum(1 for row in snapshot["endpoint_signatures"] if int(row["rank"]) > 0)

def _nonempty_maximum_rank(snapshot: dict[str, Any]) -> int:
    return max((int(row["rank"]) for row in snapshot["endpoint_signatures"] if int(row["rank"]) > 0), default=0)

def _snapshot_row(snapshot: dict[str, Any], *, censored: bool) -> dict[str, Any]:
    strongest = snapshot["overlap_graph"]["strongest_edge"]
    return {
        "prime_limit": int(snapshot["prime_limit"]),
        "prime_count": int(snapshot["prime_count"]),
        "start_face_count": int(snapshot["start_face_count"]),
        "unresolved_start_count": int(snapshot["unresolved_start_count"]),
        "is_censored_by_unresolved_starts": censored,
        "single_terminal_start_count": int(snapshot["single_terminal_start_count"]),
        "multiple_terminal_start_count": int(snapshot["multiple_terminal_start_count"]),
        "multiple_terminal_share": float(snapshot["multiplicity_shares"]["multiple"]),
        "terminal_axis_count": int(snapshot["terminal_axis_count"]),
        "observed_nonempty_endpoint_signature_count": _nonempty_signature_count(snapshot),
        "maximum_nonempty_signature_rank": _nonempty_maximum_rank(snapshot),
        "largest_basin_axes": list(snapshot["largest_basin_axes"]),
        "largest_basin_size": int(snapshot["largest_basin_size"]),
        "maximum_weighted_degree_axes": list(snapshot["overlap_graph"]["maximum_weighted_degree_axes"]),
        "maximum_weighted_degree": int(snapshot["overlap_graph"]["maximum_weighted_degree"]),
        "strongest_overlap_edge": strongest,
        "overlap_edge_count": int(snapshot["overlap_graph"]["edge_count"]),
        "active_component": list(snapshot["overlap_graph"]["active_component"]),
        "active_component_size": len(snapshot["overlap_graph"]["active_component"]),
    }

def _cohort_row(cohort: dict[str, Any], *, censored: bool) -> dict[str, Any]:
    strongest = cohort["overlap_graph"]["strongest_edge"]
    return {
        "from_limit_exclusive": int(cohort["from_limit_exclusive"]),
        "to_limit_inclusive": int(cohort["to_limit_inclusive"]),
        "start_face_count": int(cohort["start_face_count"]),
        "unresolved_start_count": int(cohort["unresolved_start_count"]),
        "is_censored_by_unresolved_starts": censored,
        "single_terminal_start_count": int(cohort["single_terminal_start_count"]),
        "multiple_terminal_start_count": int(cohort["multiple_terminal_start_count"]),
        "multiple_terminal_share": float(cohort["multiplicity_shares"]["multiple"]),
        "terminal_axis_count": int(cohort["terminal_axis_count"]),
        "observed_nonempty_endpoint_signature_count": _nonempty_signature_count(cohort),
        "maximum_nonempty_signature_rank": _nonempty_maximum_rank(cohort),
        "largest_basin_axes": list(cohort["largest_basin_axes"]),
        "largest_basin_size": int(cohort["largest_basin_size"]),
        "maximum_weighted_degree_axes": list(cohort["overlap_graph"]["maximum_weighted_degree_axes"]),
        "strongest_overlap_edge": strongest,
    }

def _candidate_observation(*, key: str, closed_cumulative: list[dict[str, Any]], closed_cohorts: list[dict[str, Any]], censored_cumulative: list[dict[str, Any]], censored_cohorts: list[dict[str, Any]]) -> dict[str, Any]:
    spec = next(item for item in CANDIDATES if item.key == key)
    if key == "largest_basin_axis_5":
        cumulative_ok = all(row["largest_basin_axes"] == [TARGET_AXIS] for row in closed_cumulative)
        cohort_ok = all(row["largest_basin_axes"] == [TARGET_AXIS] for row in closed_cohorts)
        provisional = all(row["largest_basin_axes"] == [TARGET_AXIS] for row in censored_cumulative + censored_cohorts)
    elif key == "maximum_weighted_degree_axis_5":
        cumulative_ok = all(row["maximum_weighted_degree_axes"] == [TARGET_AXIS] for row in closed_cumulative)
        cohort_ok = all(row["maximum_weighted_degree_axes"] == [TARGET_AXIS] for row in closed_cohorts)
        provisional = all(row["maximum_weighted_degree_axes"] == [TARGET_AXIS] for row in censored_cumulative + censored_cohorts)
    elif key == "strongest_overlap_edge_5_7":
        cumulative_ok = all(row["strongest_overlap_edge"] and tuple(int(x) for x in row["strongest_overlap_edge"]["axes"]) == TARGET_EDGE for row in closed_cumulative)
        cohort_ok = all(row["strongest_overlap_edge"] and tuple(int(x) for x in row["strongest_overlap_edge"]["axes"]) == TARGET_EDGE for row in closed_cohorts)
        provisional = all(row["strongest_overlap_edge"] and tuple(int(x) for x in row["strongest_overlap_edge"]["axes"]) == TARGET_EDGE for row in censored_cumulative + censored_cohorts)
    elif key == "maximum_signature_rank_non_decreasing":
        cumulative_ok = _non_decreasing(row["maximum_nonempty_signature_rank"] for row in closed_cumulative)
        cohort_ok = True
        provisional = _non_decreasing(row["maximum_nonempty_signature_rank"] for row in closed_cumulative + censored_cumulative)
    elif key == "active_component_size_non_decreasing":
        cumulative_ok = _non_decreasing(row["active_component_size"] for row in closed_cumulative)
        cohort_ok = True
        provisional = _non_decreasing(row["active_component_size"] for row in closed_cumulative + censored_cumulative)
    elif key == "fixed_depth_closure":
        cumulative_ok = all(row["unresolved_start_count"] == 0 for row in closed_cumulative)
        cohort_ok = all(row["unresolved_start_count"] == 0 for row in closed_cohorts)
        provisional = not censored_cumulative
    else:
        raise AssertionError(key)
    survives_closed = cumulative_ok and cohort_ok
    if key == "fixed_depth_closure" and censored_cumulative:
        status = "COUNTEREXAMPLE_FOUND"
    elif survives_closed and censored_cumulative:
        status = "SURVIVES_FULLY_CLOSED_RANGE_PROVISIONAL_AT_DEPTH_WALL"
    elif survives_closed:
        status = "SURVIVES_REGISTERED_RANGE"
    else:
        status = "COUNTEREXAMPLE_FOUND"
    return {"candidate": key, "description": spec.description, "scope": spec.scope, "status": status, "survives_all_fully_closed_cumulative_snapshots": cumulative_ok, "survives_all_fully_closed_cohorts": cohort_ok, "provisional_status_at_censored_snapshots": provisional}

def _repair_depth_wall(limit: int, fixed_depth: int, repair_depth_cap: int, unresolved_keys: list[str]) -> dict[str, Any]:
    before = analyze_basins(limit, fixed_depth, include_records=True)
    before_records = {str(row["start_key"]): row for row in before["start_records"]}
    repair_depth: int | None = None
    repaired_data: dict[str, Any] | None = None
    for depth in range(fixed_depth + 1, repair_depth_cap + 1):
        candidate = analyze_basins(limit, depth, include_records=True)
        if not any(row["unresolved_frontier_faces"] for row in candidate["start_records"]):
            repair_depth = depth
            repaired_data = candidate
            break
    details: list[dict[str, Any]] = []
    if repaired_data is not None:
        repaired_records = {str(row["start_key"]): row for row in repaired_data["start_records"]}
        for key in unresolved_keys:
            before_row = before_records[key]
            after_row = repaired_records[key]
            details.append({"start_key": key, "start_face": list(before_row["start_face"]), "unresolved_frontier_at_fixed_depth": before_row["unresolved_frontier_faces"], "terminal_axes_after_repair": list(after_row["terminal_axes"]), "unresolved_frontier_after_repair": after_row["unresolved_frontier_faces"]})
    repaired_summary = _summarize_records(repaired_data["start_records"]) if repaired_data is not None else None
    return {
        "prime_limit": limit,
        "fixed_depth": fixed_depth,
        "repair_depth_cap": repair_depth_cap,
        "first_closing_depth": repair_depth,
        "repair_succeeded_within_cap": repair_depth is not None,
        "unresolved_start_keys": unresolved_keys,
        "unresolved_start_details": details,
        "repaired_snapshot": ({
            "unresolved_start_count": repaired_summary["unresolved_start_count"],
            "single_terminal_start_count": repaired_summary["single_terminal_start_count"],
            "multiple_terminal_start_count": repaired_summary["multiple_terminal_start_count"],
            "terminal_axis_count": repaired_summary["terminal_axis_count"],
            "observed_nonempty_endpoint_signature_count": _nonempty_signature_count(repaired_summary),
            "maximum_nonempty_signature_rank": _nonempty_maximum_rank(repaired_summary),
            "largest_basin_axes": repaired_summary["largest_basin_axes"],
            "largest_basin_size": repaired_summary["largest_basin_size"],
            "maximum_weighted_degree_axes": repaired_summary["overlap_graph"]["maximum_weighted_degree_axes"],
            "maximum_weighted_degree": repaired_summary["overlap_graph"]["maximum_weighted_degree"],
            "strongest_overlap_edge": repaired_summary["overlap_graph"]["strongest_edge"],
            "active_component": repaired_summary["overlap_graph"]["active_component"],
            "active_component_size": len(repaired_summary["overlap_graph"]["active_component"]),
            "overlap_edge_count": repaired_summary["overlap_graph"]["edge_count"],
        } if repaired_summary is not None else None),
    }

def analyze(limits: tuple[int, ...] = REGISTERED_LIMITS, depth: int = REGISTERED_DEPTH, repair_depth_cap: int = REGISTERED_REPAIR_DEPTH_CAP) -> dict[str, Any]:
    if len(limits) < 3 or not _strictly_increasing(limits):
        raise ValueError("stress limits must contain at least three strictly increasing values")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    if repair_depth_cap < depth:
        raise ValueError("repair depth cap must be at least the fixed depth")
    expansion = analyze_expansion(limits, depth, include_records=True)
    snapshots = expansion["cumulative_snapshots"]
    cohorts = expansion["cohort_snapshots"]
    records_by_limit = {int(item["prime_limit"]): item["start_records"] for item in expansion["start_records_by_limit"]}
    cumulative_rows = [_snapshot_row(snapshot, censored=int(snapshot["unresolved_start_count"]) > 0) for snapshot in snapshots]
    cohort_rows = [_cohort_row(cohort, censored=int(cohort["unresolved_start_count"]) > 0) for cohort in cohorts]
    closed_cumulative = [row for row in cumulative_rows if not row["is_censored_by_unresolved_starts"]]
    censored_cumulative = [row for row in cumulative_rows if row["is_censored_by_unresolved_starts"]]
    closed_cohorts = [row for row in cohort_rows if not row["is_censored_by_unresolved_starts"]]
    censored_cohorts = [row for row in cohort_rows if row["is_censored_by_unresolved_starts"]]
    first_depth_wall = min((row["prime_limit"] for row in censored_cumulative), default=None)
    last_fully_closed_limit = max((row["prime_limit"] for row in closed_cumulative), default=None)
    unresolved_records = [row for row in records_by_limit[first_depth_wall] if row["unresolved_frontier_faces"]] if first_depth_wall is not None else []
    unresolved_keys = sorted(str(row["start_key"]) for row in unresolved_records)
    repair = _repair_depth_wall(first_depth_wall, depth, repair_depth_cap, unresolved_keys) if first_depth_wall is not None else None
    candidate_results = [_candidate_observation(key=spec.key, closed_cumulative=closed_cumulative, closed_cohorts=closed_cohorts, censored_cumulative=censored_cumulative, censored_cohorts=censored_cohorts) for spec in CANDIDATES]
    first_counterexamples = {
        "fixed_depth_closure": first_depth_wall,
        "largest_basin_axis_5": next((row["prime_limit"] for row in closed_cumulative if row["largest_basin_axes"] != [TARGET_AXIS]), None),
        "maximum_weighted_degree_axis_5": next((row["prime_limit"] for row in closed_cumulative if row["maximum_weighted_degree_axes"] != [TARGET_AXIS]), None),
        "strongest_overlap_edge_5_7": next((row["prime_limit"] for row in closed_cumulative if not row["strongest_overlap_edge"] or tuple(int(x) for x in row["strongest_overlap_edge"]["axes"]) != TARGET_EDGE), None),
        "maximum_signature_rank_non_decreasing": None,
        "active_component_size_non_decreasing": None,
    }
    rank_series = [row["maximum_nonempty_signature_rank"] for row in closed_cumulative]
    active_series = [row["active_component_size"] for row in closed_cumulative]
    if not _non_decreasing(rank_series):
        for previous, current in zip(closed_cumulative, closed_cumulative[1:]):
            if current["maximum_nonempty_signature_rank"] < previous["maximum_nonempty_signature_rank"]:
                first_counterexamples["maximum_signature_rank_non_decreasing"] = current["prime_limit"]
                break
    if not _non_decreasing(active_series):
        for previous, current in zip(closed_cumulative, closed_cumulative[1:]):
            if current["active_component_size"] < previous["active_component_size"]:
                first_counterexamples["active_component_size_non_decreasing"] = current["prime_limit"]
                break
    false_expansion_verifications = {key for key, value in expansion["verification"].items() if not value}
    verification = {
        "all_nonclosure_expansion_verifications_hold": false_expansion_verifications <= {"no_registered_bound_has_unresolved_starts"},
        "depth_wall_is_detected_exactly_at_first_unresolved_limit": first_depth_wall == next((row["prime_limit"] for row in cumulative_rows if row["unresolved_start_count"] > 0), None),
        "last_fully_closed_limit_precedes_depth_wall": first_depth_wall is None or (last_fully_closed_limit is not None and last_fully_closed_limit < first_depth_wall),
        "unresolved_record_count_matches_snapshot": first_depth_wall is None or len(unresolved_keys) == next(row["unresolved_start_count"] for row in cumulative_rows if row["prime_limit"] == first_depth_wall),
        "registered_depth_wall_faces_are_exact": limits != REGISTERED_LIMITS or depth != REGISTERED_DEPTH or unresolved_keys == ["{317,389}", "{347,359}"],
        "registered_depth_repair_closes_at_six": limits != REGISTERED_LIMITS or depth != REGISTERED_DEPTH or (repair is not None and repair["first_closing_depth"] == 6 and repair["repair_succeeded_within_cap"]),
        "registered_repair_endpoints_are_axis_seven": limits != REGISTERED_LIMITS or depth != REGISTERED_DEPTH or (repair is not None and all(row["terminal_axes_after_repair"] == [7] for row in repair["unresolved_start_details"])),
        "leader_candidates_have_no_counterexample_before_depth_wall": all(first_counterexamples[key] is None for key in ("largest_basin_axis_5", "maximum_weighted_degree_axis_5", "strongest_overlap_edge_5_7", "maximum_signature_rank_non_decreasing", "active_component_size_non_decreasing")),
        "multiple_terminal_share_is_strictly_increasing_on_closed_cumulative_range": _strictly_increasing([int(round(row["multiple_terminal_share"] * 10**12)) for row in closed_cumulative]),
    }
    return {
        "schema": "PVG-CROSS-BOUND-STRUCTURAL-STRESS-TEST-001",
        "classification": "finite fixed-depth counterexample search with an explicit depth wall; leader patterns are candidates only",
        "protocol": {"registered_limits": list(limits), "fixed_depth": depth, "repair_depth_cap": repair_depth_cap, "target_axis": TARGET_AXIS, "target_edge": list(TARGET_EDGE), "rules": ["search for the first counterexample instead of confirming a preferred pattern", "separate cumulative snapshots from incremental cohorts", "censor structural promotion at any bound with unresolved starts", "record the last fully closed bound and the first fixed-depth wall", "run a local depth repair only to diagnose the wall, not to mix depths in the fixed-depth ladder", "do not convert finite survival into a theorem or asymptotic claim"]},
        "stress_summary": {"last_fully_closed_limit": last_fully_closed_limit, "first_fixed_depth_wall_limit": first_depth_wall, "fixed_depth_wall_found": first_depth_wall is not None, "decisive_result": "DEPTH-WALL" if first_depth_wall is not None else "NO-COUNTEREXAMPLE-IN-REGISTERED-RANGE"},
        "cumulative_table": cumulative_rows,
        "cohort_table": cohort_rows,
        "candidate_tests": candidate_results,
        "first_counterexamples": first_counterexamples,
        "depth_wall_repair": repair,
        "underlying_expansion_verification": expansion["verification"],
        "verification": verification,
        "scientific_interpretation": {"leader_candidate_status": (f"no leader counterexample through the last fully closed bound L={last_fully_closed_limit}; observations at L={first_depth_wall} are censored at D={depth}" if first_depth_wall is not None else "no leader counterexample in the registered fully closed range"), "depth_status": (f"fixed depth D={depth} first fails to close all starts at L={first_depth_wall}" if first_depth_wall is not None else f"fixed depth D={depth} closes all registered starts"), "next_action": ("open a separate depth-extension pass at and beyond the wall before extending the fixed-depth stress ladder" if first_depth_wall is not None else "extend the prime-bound ladder cautiously")},
        "caution": "The apparent survival of axis 5 and edge {5,7} is finite and conditional on fully closed snapshots. The depth-6 repair at L=400 diagnoses the D=5 wall but is not part of the fixed-depth comparison.",
    }

def registered_summary(data: dict[str, Any]) -> dict[str, Any]:
    return data

def main() -> int:
    parser = argparse.ArgumentParser(description="Stress-test cross-bound PVG structural candidates and detect the first fixed-depth wall.")
    parser.add_argument("--limits", default=",".join(str(limit) for limit in REGISTERED_LIMITS), help="strictly increasing comma-separated prime limits")
    parser.add_argument("--depth", type=int, default=REGISTERED_DEPTH)
    parser.add_argument("--repair-depth-cap", type=int, default=REGISTERED_REPAIR_DEPTH_CAP)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        limits = parse_limits(args.limits)
        data = analyze(limits, args.depth, args.repair_depth_cap)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(registered_summary(data), ensure_ascii=False, sort_keys=True, indent=None if args.compact else 2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
