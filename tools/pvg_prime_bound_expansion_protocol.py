from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from math import comb

try:
    from tools.pvg_additive_attraction_basins import analyze as analyze_basins
except ModuleNotFoundError:
    from pvg_additive_attraction_basins import analyze as analyze_basins


REGISTERED_LIMITS = (100, 150, 200)
REGISTERED_DEPTH = 5


def face_key(axes: tuple[int, ...] | list[int]) -> str:
    return "{" + ",".join(str(axis) for axis in axes) + "}"


def parse_limits(text: str) -> tuple[int, ...]:
    try:
        values = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    except ValueError as exc:
        raise ValueError("limits must be comma-separated integers") from exc
    if len(values) < 2:
        raise ValueError("at least two prime limits are required")
    if any(limit < 3 for limit in values):
        raise ValueError("every prime limit must be at least 3")
    if tuple(sorted(set(values))) != values:
        raise ValueError("limits must be strictly increasing with no duplicates")
    return values


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_count(limit: int) -> int:
    return sum(is_prime(n) for n in range(2, limit + 1))


def _share(count: int, total: int) -> float:
    return round(count / total, 12) if total else 0.0


def _components(nodes: list[int], edges: list[dict[str, object]]) -> list[list[int]]:
    adjacency = {node: set() for node in nodes}
    for edge in edges:
        a, b = (int(x) for x in edge["axes"])
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen: set[int] = set()
    out: list[list[int]] = []
    for start in nodes:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        component: list[int] = []
        while stack:
            node = stack.pop()
            component.append(node)
            for target in sorted(adjacency[node], reverse=True):
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
        out.append(sorted(component))
    return sorted(out, key=lambda component: (-len(component), component))


def _record_signature(record: dict[str, object]) -> tuple[int, ...]:
    return tuple(int(x) for x in record["terminal_axes"])


def _summarize_records(records: list[dict[str, object]]) -> dict[str, object]:
    total = len(records)
    signatures = Counter(_record_signature(record) for record in records)
    axes = sorted({axis for signature in signatures for axis in signature})
    basin_members = {
        axis: {str(record["start_key"]) for record in records if axis in record["terminal_axes"]}
        for axis in axes
    }
    basin_sizes = {str(axis): len(basin_members[axis]) for axis in axes}
    basin_shares = {
        str(axis): _share(len(basin_members[axis]), total)
        for axis in axes
    }

    pair_overlaps: list[dict[str, object]] = []
    for a, b in combinations(axes, 2):
        intersection = basin_members[a] & basin_members[b]
        if not intersection:
            continue
        union = basin_members[a] | basin_members[b]
        exact_count = signatures[(a, b)]
        pair_overlaps.append(
            {
                "axes": [a, b],
                "key": face_key((a, b)),
                "intersection_size": len(intersection),
                "start_share": _share(len(intersection), total),
                "union_size": len(union),
                "jaccard": round(len(intersection) / len(union), 12),
                "exact_signature_count": exact_count,
                "higher_signature_mediation_count": len(intersection) - exact_count,
            }
        )
    pair_overlaps.sort(
        key=lambda row: (-int(row["intersection_size"]), row["axes"])
    )

    degree = Counter()
    weighted_degree = Counter()
    for edge in pair_overlaps:
        a, b = (int(x) for x in edge["axes"])
        weight = int(edge["intersection_size"])
        degree[a] += 1
        degree[b] += 1
        weighted_degree[a] += weight
        weighted_degree[b] += weight
    for axis in axes:
        degree[axis] += 0
        weighted_degree[axis] += 0

    components = _components(axes, pair_overlaps)
    largest_basin_size = max(basin_sizes.values(), default=0)
    maximum_weighted_degree = max(weighted_degree.values(), default=0)
    maximum_degree = max(degree.values(), default=0)

    signature_records = [
        {
            "terminal_axes": list(signature),
            "terminal_key": face_key(signature),
            "rank": len(signature),
            "start_face_count": count,
            "start_share": _share(count, total),
        }
        for signature, count in sorted(
            signatures.items(), key=lambda item: (len(item[0]), item[0])
        )
    ]
    rank_distribution = Counter(len(signature) for signature in signatures)
    single_count = sum(len(_record_signature(record)) == 1 for record in records)
    multiple_count = sum(len(_record_signature(record)) >= 2 for record in records)
    none_count = sum(not _record_signature(record) for record in records)
    unresolved_count = sum(bool(record["unresolved_frontier_faces"]) for record in records)

    return {
        "start_face_count": total,
        "unresolved_start_count": unresolved_count,
        "no_terminal_observed_start_count": none_count,
        "single_terminal_start_count": single_count,
        "multiple_terminal_start_count": multiple_count,
        "multiplicity_shares": {
            "none": _share(none_count, total),
            "single": _share(single_count, total),
            "multiple": _share(multiple_count, total),
        },
        "terminal_axes": axes,
        "terminal_axis_count": len(axes),
        "endpoint_signature_count": len(signatures),
        "signature_rank_distribution": {
            str(rank): rank_distribution[rank] for rank in sorted(rank_distribution)
        },
        "maximum_signature_rank": max(rank_distribution, default=0),
        "endpoint_signatures": signature_records,
        "axis_basins": [
            {
                "axis": axis,
                "basin_size": len(basin_members[axis]),
                "start_share": basin_shares[str(axis)],
                "degree": degree[axis],
                "weighted_degree": weighted_degree[axis],
            }
            for axis in axes
        ],
        "largest_basin_size": largest_basin_size,
        "largest_basin_axes": sorted(
            int(axis) for axis, size in basin_sizes.items()
            if size == largest_basin_size
        ),
        "overlap_graph": {
            "node_count": len(axes),
            "edge_count": len(pair_overlaps),
            "pair_overlaps": pair_overlaps,
            "components": components,
            "component_count": len(components),
            "component_sizes": [len(component) for component in components],
            "active_component": components[0] if components else [],
            "isolated_axes": sorted(
                component[0] for component in components if len(component) == 1
            ),
            "cycle_rank": len(pair_overlaps) - len(axes) + len(components),
            "maximum_degree": maximum_degree,
            "maximum_degree_axes": sorted(
                axis for axis in axes if degree[axis] == maximum_degree
            ),
            "maximum_weighted_degree": maximum_weighted_degree,
            "maximum_weighted_degree_axes": sorted(
                axis for axis in axes
                if weighted_degree[axis] == maximum_weighted_degree
            ),
            "strongest_edge": pair_overlaps[0] if pair_overlaps else None,
        },
    }


def _signature_set(summary: dict[str, object]) -> set[tuple[int, ...]]:
    return {
        tuple(int(x) for x in row["terminal_axes"])
        for row in summary["endpoint_signatures"]
    }


def _edge_set(summary: dict[str, object]) -> set[tuple[int, int]]:
    return {
        tuple(int(x) for x in row["axes"])
        for row in summary["overlap_graph"]["pair_overlaps"]
    }


def _axis_share_map(summary: dict[str, object]) -> dict[int, float]:
    return {
        int(row["axis"]): float(row["start_share"])
        for row in summary["axis_basins"]
    }


def analyze(
    limits: tuple[int, ...] = REGISTERED_LIMITS,
    depth: int = REGISTERED_DEPTH,
    include_records: bool = True,
) -> dict[str, object]:
    if tuple(sorted(set(limits))) != limits or len(limits) < 2:
        raise ValueError("limits must be a strictly increasing tuple with at least two values")
    if any(limit < 3 for limit in limits):
        raise ValueError("every prime limit must be at least 3")
    if depth < 0:
        raise ValueError("depth must be nonnegative")

    raw = [
        analyze_basins(limit, depth, include_records=True)
        for limit in limits
    ]
    records_by_limit = [
        {str(record["start_key"]): record for record in data["start_records"]}
        for data in raw
    ]

    snapshots: list[dict[str, object]] = []
    for limit, data in zip(limits, raw):
        records = list(data["start_records"])
        summary = _summarize_records(records)
        count = prime_count(limit)
        summary.update(
            {
                "prime_limit": limit,
                "prime_count": count,
                "expected_start_face_count": comb(count, 2),
                "underlying_pass016_verification": all(data["verification"].values()),
            }
        )
        snapshots.append(summary)

    cohorts: list[dict[str, object]] = []
    transitions: list[dict[str, object]] = []
    for index in range(1, len(limits)):
        previous_limit = limits[index - 1]
        current_limit = limits[index]
        previous_records = records_by_limit[index - 1]
        current_records = records_by_limit[index]
        cohort_records = [
            record for key, record in current_records.items()
            if key not in previous_records
        ]
        cohort_summary = _summarize_records(cohort_records)
        previous_prime_count = prime_count(previous_limit)
        current_prime_count = prime_count(current_limit)
        cohort_summary.update(
            {
                "from_limit_exclusive": previous_limit,
                "to_limit_inclusive": current_limit,
                "added_prime_count": current_prime_count - previous_prime_count,
                "expected_cohort_start_face_count": (
                    comb(current_prime_count, 2) - comb(previous_prime_count, 2)
                ),
            }
        )
        cohorts.append(cohort_summary)

        previous_summary = snapshots[index - 1]
        current_summary = snapshots[index]
        previous_axes = set(int(x) for x in previous_summary["terminal_axes"])
        current_axes = set(int(x) for x in current_summary["terminal_axes"])
        previous_signatures = _signature_set(previous_summary)
        current_signatures = _signature_set(current_summary)
        previous_edges = _edge_set(previous_summary)
        current_edges = _edge_set(current_summary)
        previous_shares = _axis_share_map(previous_summary)
        current_shares = _axis_share_map(current_summary)
        persistent_axes = sorted(previous_axes & current_axes)

        retained_consistency = all(
            tuple(previous_records[key]["terminal_axes"])
            == tuple(current_records[key]["terminal_axes"])
            and previous_records[key]["unresolved_frontier_faces"]
            == current_records[key]["unresolved_frontier_faces"]
            for key in previous_records
        )
        transitions.append(
            {
                "from_limit": previous_limit,
                "to_limit": current_limit,
                "retained_start_count": len(previous_records),
                "added_start_count": len(cohort_records),
                "retained_start_dynamics_unchanged": retained_consistency,
                "new_terminal_axes": sorted(current_axes - previous_axes),
                "removed_terminal_axes": sorted(previous_axes - current_axes),
                "new_endpoint_signatures": [
                    {
                        "terminal_axes": list(signature),
                        "terminal_key": face_key(signature),
                    }
                    for signature in sorted(
                        current_signatures - previous_signatures,
                        key=lambda signature: (len(signature), signature),
                    )
                ],
                "removed_endpoint_signatures": [
                    {
                        "terminal_axes": list(signature),
                        "terminal_key": face_key(signature),
                    }
                    for signature in sorted(
                        previous_signatures - current_signatures,
                        key=lambda signature: (len(signature), signature),
                    )
                ],
                "new_overlap_edges": [
                    {"axes": list(edge), "key": face_key(edge)}
                    for edge in sorted(current_edges - previous_edges)
                ],
                "removed_overlap_edges": [
                    {"axes": list(edge), "key": face_key(edge)}
                    for edge in sorted(previous_edges - current_edges)
                ],
                "active_component_before": previous_summary["overlap_graph"][
                    "active_component"
                ],
                "active_component_after": current_summary["overlap_graph"][
                    "active_component"
                ],
                "maximum_signature_rank_before": previous_summary[
                    "maximum_signature_rank"
                ],
                "maximum_signature_rank_after": current_summary[
                    "maximum_signature_rank"
                ],
                "multiple_terminal_share_before": previous_summary[
                    "multiplicity_shares"
                ]["multiple"],
                "multiple_terminal_share_after": current_summary[
                    "multiplicity_shares"
                ]["multiple"],
                "persistent_axis_basin_share_changes": {
                    str(axis): round(
                        current_shares[axis] - previous_shares[axis], 12
                    )
                    for axis in persistent_axes
                },
            }
        )

    all_axis_sets = [set(int(x) for x in snapshot["terminal_axes"]) for snapshot in snapshots]
    all_signature_sets = [_signature_set(snapshot) for snapshot in snapshots]
    all_edge_sets = [_edge_set(snapshot) for snapshot in snapshots]

    axis_first_appearance: dict[str, int] = {}
    for limit, axes in zip(limits, all_axis_sets):
        for axis in axes:
            axis_first_appearance.setdefault(str(axis), limit)
    signature_first_appearance: dict[str, int] = {}
    for limit, signatures in zip(limits, all_signature_sets):
        for signature in signatures:
            signature_first_appearance.setdefault(face_key(signature), limit)
    edge_first_appearance: dict[str, int] = {}
    for limit, edges in zip(limits, all_edge_sets):
        for edge in edges:
            edge_first_appearance.setdefault(face_key(edge), limit)

    largest_basin_series = [
        snapshot["largest_basin_axes"] for snapshot in snapshots
    ]
    strongest_edge_series = [
        snapshot["overlap_graph"]["strongest_edge"]["axes"]
        if snapshot["overlap_graph"]["strongest_edge"]
        else []
        for snapshot in snapshots
    ]
    maximum_weighted_degree_axis_series = [
        snapshot["overlap_graph"]["maximum_weighted_degree_axes"]
        for snapshot in snapshots
    ]

    verification = {
        "all_underlying_pass016_verifications_hold": all(
            snapshot["underlying_pass016_verification"] for snapshot in snapshots
        ),
        "start_counts_match_prime_pair_counts": all(
            snapshot["start_face_count"] == snapshot["expected_start_face_count"]
            for snapshot in snapshots
        ),
        "start_families_are_nested": all(
            set(records_by_limit[index - 1]) <= set(records_by_limit[index])
            for index in range(1, len(records_by_limit))
        ),
        "retained_start_dynamics_are_bound_independent": all(
            transition["retained_start_dynamics_unchanged"]
            for transition in transitions
        ),
        "cohort_partitions_close": all(
            snapshots[index]["start_face_count"]
            == snapshots[index - 1]["start_face_count"]
            + cohorts[index - 1]["start_face_count"]
            for index in range(1, len(snapshots))
        ),
        "cohort_counts_match_combinatorics": all(
            cohort["start_face_count"] == cohort["expected_cohort_start_face_count"]
            for cohort in cohorts
        ),
        "terminal_axis_sets_are_nested": all(
            all_axis_sets[index - 1] <= all_axis_sets[index]
            for index in range(1, len(all_axis_sets))
        ),
        "endpoint_signature_sets_are_nested": all(
            all_signature_sets[index - 1] <= all_signature_sets[index]
            for index in range(1, len(all_signature_sets))
        ),
        "positive_overlap_edge_sets_are_nested": all(
            all_edge_sets[index - 1] <= all_edge_sets[index]
            for index in range(1, len(all_edge_sets))
        ),
        "no_registered_bound_has_unresolved_starts": all(
            snapshot["unresolved_start_count"] == 0 for snapshot in snapshots
        ),
        "all_normalized_shares_are_probabilities": all(
            0.0 <= value <= 1.0
            for snapshot in snapshots + cohorts
            for value in (
                list(snapshot["multiplicity_shares"].values())
                + [row["start_share"] for row in snapshot["axis_basins"]]
                + [
                    row["start_share"]
                    for row in snapshot["overlap_graph"]["pair_overlaps"]
                ]
            )
        ),
    }

    result: dict[str, object] = {
        "schema": "PVG-PRIME-BOUND-EXPANSION-PROTOCOL-001",
        "classification": (
            "finite verified registered prime-bound pilot at fixed depth; "
            "no asymptotic, general bound-stability, or termination claim"
        ),
        "protocol": {
            "registered_limits": list(limits),
            "fixed_depth": depth,
            "cumulative_family": "all unordered prime-pair faces {p,q} with p<q<=L",
            "cohort_family": "new faces in F(L_i) minus F(L_{i-1})",
            "rules": [
                "keep the depth fixed while changing the prime bound",
                "report cumulative and incremental-cohort statistics separately",
                "compare raw counts and normalized start shares",
                "record every new axis, endpoint signature, and positive overlap edge",
                "treat absence at a smaller bound as unobserved rather than impossible",
                "if any registered bound is unresolved, stop promotion and open a separate depth-extension pass",
                "do not extrapolate the finite ladder to an asymptotic law",
            ],
        },
        "cumulative_snapshots": snapshots,
        "cohort_snapshots": cohorts,
        "bound_transitions": transitions,
        "first_appearance": {
            "terminal_axes": dict(sorted(axis_first_appearance.items(), key=lambda x: int(x[0]))),
            "endpoint_signatures": dict(sorted(signature_first_appearance.items())),
            "overlap_edges": dict(sorted(edge_first_appearance.items())),
        },
        "cross_bound_candidates": {
            "largest_basin_axis_series": largest_basin_series,
            "strongest_overlap_edge_series": strongest_edge_series,
            "maximum_weighted_degree_axis_series": maximum_weighted_degree_axis_series,
            "largest_basin_axis_is_constant": len({tuple(x) for x in largest_basin_series}) == 1,
            "strongest_overlap_edge_is_constant": len({tuple(x) for x in strongest_edge_series}) == 1,
            "maximum_weighted_degree_axis_is_constant": (
                len({tuple(x) for x in maximum_weighted_degree_axis_series}) == 1
            ),
        },
        "verification": verification,
        "caution": (
            "Nested cumulative counts are monotone by construction because older starts remain present. "
            "Structural stability must therefore be judged with cohort statistics, normalized shares, "
            "component growth, signature rank, and first-appearance records rather than raw counts alone."
        ),
    }
    if include_records:
        result["start_records_by_limit"] = [
            {"prime_limit": limit, "start_records": data["start_records"]}
            for limit, data in zip(limits, raw)
        ]
    return result


def registered_summary(data: dict[str, object]) -> dict[str, object]:
    snapshots = data["cumulative_snapshots"]
    cohorts = data["cohort_snapshots"]
    return {
        "schema": data["schema"],
        "classification": data["classification"],
        "protocol": data["protocol"],
        "cumulative_table": [
            {
                "prime_limit": snapshot["prime_limit"],
                "prime_count": snapshot["prime_count"],
                "start_face_count": snapshot["start_face_count"],
                "unresolved_start_count": snapshot["unresolved_start_count"],
                "single_terminal_start_count": snapshot["single_terminal_start_count"],
                "multiple_terminal_start_count": snapshot["multiple_terminal_start_count"],
                "multiplicity_shares": snapshot["multiplicity_shares"],
                "terminal_axis_count": snapshot["terminal_axis_count"],
                "terminal_axes": snapshot["terminal_axes"],
                "endpoint_signature_count": snapshot["endpoint_signature_count"],
                "signature_rank_distribution": snapshot["signature_rank_distribution"],
                "maximum_signature_rank": snapshot["maximum_signature_rank"],
                "largest_basin_axes": snapshot["largest_basin_axes"],
                "largest_basin_size": snapshot["largest_basin_size"],
                "overlap_edge_count": snapshot["overlap_graph"]["edge_count"],
                "overlap_component_sizes": snapshot["overlap_graph"]["component_sizes"],
                "active_component": snapshot["overlap_graph"]["active_component"],
                "isolated_axes": snapshot["overlap_graph"]["isolated_axes"],
                "strongest_overlap_edge": snapshot["overlap_graph"]["strongest_edge"],
                "maximum_weighted_degree_axes": snapshot["overlap_graph"][
                    "maximum_weighted_degree_axes"
                ],
                "maximum_weighted_degree": snapshot["overlap_graph"][
                    "maximum_weighted_degree"
                ],
                "core_axis_basin_shares": {
                    str(row["axis"]): row["start_share"]
                    for row in snapshot["axis_basins"]
                    if int(row["axis"]) in (2, 3, 5, 7, 13, 19)
                },
            }
            for snapshot in snapshots
        ],
        "cohort_table": [
            {
                "from_limit_exclusive": cohort["from_limit_exclusive"],
                "to_limit_inclusive": cohort["to_limit_inclusive"],
                "added_prime_count": cohort["added_prime_count"],
                "start_face_count": cohort["start_face_count"],
                "unresolved_start_count": cohort["unresolved_start_count"],
                "single_terminal_start_count": cohort["single_terminal_start_count"],
                "multiple_terminal_start_count": cohort["multiple_terminal_start_count"],
                "multiplicity_shares": cohort["multiplicity_shares"],
                "terminal_axis_count": cohort["terminal_axis_count"],
                "endpoint_signature_count": cohort["endpoint_signature_count"],
                "signature_rank_distribution": cohort["signature_rank_distribution"],
                "maximum_signature_rank": cohort["maximum_signature_rank"],
                "largest_basin_axes": cohort["largest_basin_axes"],
                "largest_basin_size": cohort["largest_basin_size"],
                "strongest_overlap_edge": cohort["overlap_graph"]["strongest_edge"],
                "maximum_weighted_degree_axes": cohort["overlap_graph"][
                    "maximum_weighted_degree_axes"
                ],
                "core_axis_basin_shares": {
                    str(row["axis"]): row["start_share"]
                    for row in cohort["axis_basins"]
                    if int(row["axis"]) in (2, 3, 5, 7, 13, 19)
                },
            }
            for cohort in cohorts
        ],
        "bound_transitions": data["bound_transitions"],
        "first_appearance": data["first_appearance"],
        "cross_bound_candidates": data["cross_bound_candidates"],
        "verification": data["verification"],
        "caution": data["caution"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a governed fixed-depth pilot for expanding the prime bound."
    )
    parser.add_argument(
        "--limits",
        default=",".join(str(limit) for limit in REGISTERED_LIMITS),
        help="strictly increasing comma-separated prime limits",
    )
    parser.add_argument("--depth", type=int, default=REGISTERED_DEPTH)
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        limits = parse_limits(args.limits)
        data = analyze(limits, args.depth, include_records=not args.summary_only)
    except ValueError as exc:
        parser.error(str(exc))
    if args.registered_summary:
        data = registered_summary(data)
    print(
        json.dumps(
            data,
            ensure_ascii=False,
            sort_keys=True,
            indent=None if args.compact else 2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
