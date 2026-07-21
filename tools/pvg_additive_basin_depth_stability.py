from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations

try:
    from tools.pvg_additive_attraction_basins import analyze as analyze_basins
except ModuleNotFoundError:
    from pvg_additive_attraction_basins import analyze as analyze_basins


def face_key(axes: tuple[int, ...] | list[int]) -> str:
    return "{" + ",".join(str(axis) for axis in axes) + "}"


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


def _depth_snapshot(depth: int, data: dict[str, object]) -> dict[str, object]:
    records = data["start_records"]
    signatures = Counter(tuple(int(x) for x in record["terminal_axes"]) for record in records)
    axes = sorted({axis for signature in signatures for axis in signature})
    basin_members = {
        axis: {record["start_key"] for record in records if axis in record["terminal_axes"]}
        for axis in axes
    }
    basin_sizes = {str(axis): len(basin_members[axis]) for axis in axes}

    overlap_edges: list[dict[str, object]] = []
    for a, b in combinations(axes, 2):
        overlap = basin_members[a] & basin_members[b]
        if overlap:
            overlap_edges.append(
                {
                    "axes": [a, b],
                    "key": face_key((a, b)),
                    "weight": len(overlap),
                    "union_size": len(basin_members[a] | basin_members[b]),
                }
            )
    overlap_edges.sort(key=lambda edge: (-int(edge["weight"]), edge["axes"]))

    degree = Counter()
    weighted_degree = Counter()
    for edge in overlap_edges:
        a, b = (int(x) for x in edge["axes"])
        weight = int(edge["weight"])
        degree[a] += 1
        degree[b] += 1
        weighted_degree[a] += weight
        weighted_degree[b] += weight
    for axis in axes:
        degree[axis] += 0
        weighted_degree[axis] += 0

    components = _components(axes, overlap_edges)
    largest_basin_size = max(basin_sizes.values(), default=0)
    largest_basin_axes = sorted(
        int(axis) for axis, size in basin_sizes.items() if size == largest_basin_size
    )
    maximum_weighted_degree = max(weighted_degree.values(), default=0)
    maximum_weighted_degree_axes = sorted(
        axis for axis, value in weighted_degree.items() if value == maximum_weighted_degree
    )

    signature_records = [
        {
            "terminal_axes": list(signature),
            "terminal_key": face_key(signature),
            "start_face_count": count,
        }
        for signature, count in sorted(
            signatures.items(), key=lambda item: (len(item[0]), item[0])
        )
    ]

    return {
        "depth": depth,
        "unresolved_start_count": int(data["unresolved_start_count"]),
        "no_terminal_observed_start_count": int(data["no_terminal_observed_start_count"]),
        "single_terminal_start_count": int(data["single_terminal_start_count"]),
        "multiple_terminal_start_count": int(data["multiple_terminal_start_count"]),
        "terminal_count_distribution": dict(data["terminal_count_distribution"]),
        "terminal_axes": axes,
        "terminal_axis_count": len(axes),
        "endpoint_signature_count_including_empty": len(signatures),
        "nonempty_endpoint_signature_count": sum(bool(signature) for signature in signatures),
        "endpoint_signatures": signature_records,
        "basin_sizes": basin_sizes,
        "largest_basin_size": largest_basin_size,
        "largest_basin_axes": largest_basin_axes,
        "overlap_graph": {
            "node_count": len(axes),
            "edge_count": len(overlap_edges),
            "edges": overlap_edges,
            "components": components,
            "component_count": len(components),
            "component_sizes": [len(component) for component in components],
            "cycle_rank": len(overlap_edges) - len(axes) + len(components),
            "degrees": {str(axis): degree[axis] for axis in axes},
            "weighted_degrees": {str(axis): weighted_degree[axis] for axis in axes},
            "maximum_weighted_degree": maximum_weighted_degree,
            "maximum_weighted_degree_axes": maximum_weighted_degree_axes,
            "strongest_edge": overlap_edges[0] if overlap_edges else None,
        },
    }


def _signature_transition_records(
    start_keys: list[str],
    signatures_by_depth: list[dict[str, tuple[int, ...]]],
    min_depth: int,
    max_depth: int,
) -> list[dict[str, object]]:
    final_signatures = signatures_by_depth[-1]
    out: list[dict[str, object]] = []
    for offset, depth in enumerate(range(min_depth, max_depth)):
        current = signatures_by_depth[offset]
        following = signatures_by_depth[offset + 1]
        transitions = Counter((current[key], following[key]) for key in start_keys)
        changed = sum(current[key] != following[key] for key in start_keys)
        temporarily_unchanged = sum(
            current[key] == following[key] and current[key] != final_signatures[key]
            for key in start_keys
        )
        out.append(
            {
                "from_depth": depth,
                "to_depth": depth + 1,
                "changed_start_count": changed,
                "unchanged_start_count": len(start_keys) - changed,
                "temporarily_unchanged_start_count": temporarily_unchanged,
                "became_nonempty_start_count": sum(
                    not current[key] and bool(following[key]) for key in start_keys
                ),
                "became_multiple_terminal_start_count": sum(
                    len(current[key]) < 2 <= len(following[key]) for key in start_keys
                ),
                "signature_transition_count": len(transitions),
                "signature_transitions": [
                    {
                        "from_axes": list(source),
                        "from_key": face_key(source),
                        "to_axes": list(target),
                        "to_key": face_key(target),
                        "start_face_count": count,
                    }
                    for (source, target), count in sorted(
                        transitions.items(),
                        key=lambda item: (-item[1], item[0][0], item[0][1]),
                    )
                ],
            }
        )
    return out


def analyze(
    limit: int = 100,
    min_depth: int = 0,
    max_depth: int = 5,
    include_records: bool = True,
) -> dict[str, object]:
    if limit < 3:
        raise ValueError("limit must be at least 3")
    if min_depth < 0:
        raise ValueError("min_depth must be nonnegative")
    if max_depth < min_depth:
        raise ValueError("max_depth must be at least min_depth")

    raw_by_depth = [
        analyze_basins(limit, depth, include_records=True)
        for depth in range(min_depth, max_depth + 1)
    ]
    start_keys = [record["start_key"] for record in raw_by_depth[0]["start_records"]]
    records_by_depth = [
        {record["start_key"]: record for record in data["start_records"]}
        for data in raw_by_depth
    ]
    if any(list(records) != start_keys for records in records_by_depth):
        raise RuntimeError("registered start ordering changed across depths")

    signatures_by_depth = [
        {
            key: tuple(int(x) for x in records[key]["terminal_axes"])
            for key in start_keys
        }
        for records in records_by_depth
    ]
    final_signatures = signatures_by_depth[-1]

    start_records: list[dict[str, object]] = []
    stabilization_depth_distribution: Counter[int] = Counter()
    closure_depth_distribution: Counter[int] = Counter()
    unresolved_through_max_depth = 0

    for key in start_keys:
        signatures = [mapping[key] for mapping in signatures_by_depth]
        stabilization_offset = next(
            offset
            for offset in range(len(signatures))
            if all(signatures[index] == signatures[-1] for index in range(offset, len(signatures)))
        )
        stabilization_depth = min_depth + stabilization_offset
        stabilization_depth_distribution[stabilization_depth] += 1

        closure_depth = next(
            (
                min_depth + offset
                for offset, records in enumerate(records_by_depth)
                if bool(records[key]["bounded_closure_reached"])
            ),
            None,
        )
        if closure_depth is None:
            unresolved_through_max_depth += 1
        else:
            closure_depth_distribution[closure_depth] += 1

        change_depths = [
            min_depth + offset + 1
            for offset in range(len(signatures) - 1)
            if signatures[offset] != signatures[offset + 1]
        ]
        temporarily_unchanged_depths = [
            min_depth + offset
            for offset in range(len(signatures) - 1)
            if signatures[offset] == signatures[offset + 1]
            and signatures[offset] != signatures[-1]
        ]
        first_terminal_depth = next(
            (
                min_depth + offset
                for offset, signature in enumerate(signatures)
                if signature
            ),
            None,
        )
        start_records.append(
            {
                "start_key": key,
                "start_face": records_by_depth[0][key]["start_face"],
                "endpoint_signatures_by_depth": [
                    {
                        "depth": min_depth + offset,
                        "terminal_axes": list(signature),
                        "terminal_key": face_key(signature),
                    }
                    for offset, signature in enumerate(signatures)
                ],
                "final_terminal_axes": list(signatures[-1]),
                "final_terminal_key": face_key(signatures[-1]),
                "first_terminal_depth": first_terminal_depth,
                "observed_stabilization_depth": stabilization_depth,
                "first_bounded_closure_depth": closure_depth,
                "endpoint_change_depths": change_depths,
                "temporarily_unchanged_depths": temporarily_unchanged_depths,
                "observed_stable_through_max_depth": True,
                "resolved_by_max_depth": closure_depth is not None,
            }
        )

    depth_snapshots = [
        _depth_snapshot(depth, data)
        for depth, data in zip(range(min_depth, max_depth + 1), raw_by_depth)
    ]
    transitions = _signature_transition_records(
        start_keys, signatures_by_depth, min_depth, max_depth
    )

    basin_series = {
        str(axis): [
            int(snapshot["basin_sizes"].get(str(axis), 0))
            for snapshot in depth_snapshots
        ]
        for axis in sorted(
            {axis for snapshot in depth_snapshots for axis in snapshot["terminal_axes"]}
        )
    }
    overlap_weight_series: dict[str, list[int]] = {}
    all_pairs = sorted(
        {
            tuple(int(x) for x in edge["axes"])
            for snapshot in depth_snapshots
            for edge in snapshot["overlap_graph"]["edges"]
        }
    )
    for pair in all_pairs:
        key = face_key(pair)
        overlap_weight_series[key] = []
        for snapshot in depth_snapshots:
            weights = {
                tuple(int(x) for x in edge["axes"]): int(edge["weight"])
                for edge in snapshot["overlap_graph"]["edges"]
            }
            overlap_weight_series[key].append(weights.get(pair, 0))

    verification = {
        "all_pass016_verifications_hold": all(
            all(data["verification"].values()) for data in raw_by_depth
        ),
        "start_family_is_constant_across_depths": all(
            list(records) == start_keys for records in records_by_depth
        ),
        "endpoint_sets_are_monotone": all(
            set(signatures_by_depth[offset][key])
            <= set(signatures_by_depth[offset + 1][key])
            for offset in range(len(signatures_by_depth) - 1)
            for key in start_keys
        ),
        "unresolved_counts_are_nonincreasing": all(
            depth_snapshots[offset]["unresolved_start_count"]
            >= depth_snapshots[offset + 1]["unresolved_start_count"]
            for offset in range(len(depth_snapshots) - 1)
        ),
        "basin_sizes_are_nondecreasing": all(
            series[offset] <= series[offset + 1]
            for series in basin_series.values()
            for offset in range(len(series) - 1)
        ),
        "overlap_weights_are_nondecreasing": all(
            series[offset] <= series[offset + 1]
            for series in overlap_weight_series.values()
            for offset in range(len(series) - 1)
        ),
        "stabilization_partition_closes": sum(stabilization_depth_distribution.values())
        == len(start_keys),
        "closure_partition_closes": sum(closure_depth_distribution.values())
        + unresolved_through_max_depth
        == len(start_keys),
        "transition_partitions_close": all(
            transition["changed_start_count"] + transition["unchanged_start_count"]
            == len(start_keys)
            for transition in transitions
        ),
        "final_signatures_match_max_depth": all(
            tuple(record["final_terminal_axes"]) == final_signatures[record["start_key"]]
            for record in start_records
        ),
    }

    result: dict[str, object] = {
        "schema": "PVG-ADDITIVE-BASIN-DEPTH-STABILITY-001",
        "classification": (
            "finite verified depth-window evolution through the registered maximum depth; "
            "observed stability is not a general stabilization theorem"
        ),
        "scope": {
            "prime_limit": limit,
            "min_depth": min_depth,
            "max_depth": max_depth,
            "depth_values": list(range(min_depth, max_depth + 1)),
            "start_face_count": len(start_keys),
            "start_family": "all unordered prime-pair faces {p,q} with p<q<=limit",
        },
        "depth_snapshots": depth_snapshots,
        "step_transitions": transitions,
        "stabilization_depth_distribution": {
            str(depth): stabilization_depth_distribution[depth]
            for depth in range(min_depth, max_depth + 1)
        },
        "bounded_closure_depth_distribution": {
            str(depth): closure_depth_distribution[depth]
            for depth in range(min_depth, max_depth + 1)
        },
        "unresolved_through_max_depth_count": unresolved_through_max_depth,
        "basin_size_series": basin_series,
        "overlap_weight_series": overlap_weight_series,
        "verification": verification,
        "caution": (
            "A signature can remain unchanged for one step and change later. "
            "Observed stabilization means equality only through the registered max_depth."
        ),
    }
    if include_records:
        result["start_records"] = start_records
    return result


def registered_summary(data: dict[str, object]) -> dict[str, object]:
    snapshots = data["depth_snapshots"]
    return {
        "schema": data["schema"],
        "classification": data["classification"],
        "scope": data["scope"],
        "depth_table": [
            {
                "depth": snapshot["depth"],
                "unresolved_start_count": snapshot["unresolved_start_count"],
                "no_terminal_observed_start_count": snapshot["no_terminal_observed_start_count"],
                "single_terminal_start_count": snapshot["single_terminal_start_count"],
                "multiple_terminal_start_count": snapshot["multiple_terminal_start_count"],
                "terminal_axis_count": snapshot["terminal_axis_count"],
                "nonempty_endpoint_signature_count": snapshot["nonempty_endpoint_signature_count"],
                "largest_basin_axes": snapshot["largest_basin_axes"],
                "largest_basin_size": snapshot["largest_basin_size"],
                "overlap_edge_count": snapshot["overlap_graph"]["edge_count"],
                "overlap_component_sizes": snapshot["overlap_graph"]["component_sizes"],
                "strongest_overlap_edge": snapshot["overlap_graph"]["strongest_edge"],
                "maximum_weighted_degree_axes": snapshot["overlap_graph"][
                    "maximum_weighted_degree_axes"
                ],
                "maximum_weighted_degree": snapshot["overlap_graph"][
                    "maximum_weighted_degree"
                ],
            }
            for snapshot in snapshots
        ],
        "stabilization_depth_distribution": data[
            "stabilization_depth_distribution"
        ],
        "bounded_closure_depth_distribution": data[
            "bounded_closure_depth_distribution"
        ],
        "unresolved_through_max_depth_count": data[
            "unresolved_through_max_depth_count"
        ],
        "step_change_table": [
            {
                "from_depth": transition["from_depth"],
                "to_depth": transition["to_depth"],
                "changed_start_count": transition["changed_start_count"],
                "unchanged_start_count": transition["unchanged_start_count"],
                "temporarily_unchanged_start_count": transition[
                    "temporarily_unchanged_start_count"
                ],
                "became_nonempty_start_count": transition[
                    "became_nonempty_start_count"
                ],
                "became_multiple_terminal_start_count": transition[
                    "became_multiple_terminal_start_count"
                ],
            }
            for transition in data["step_transitions"]
        ],
        "basin_size_series": data["basin_size_series"],
        "overlap_weight_series": data["overlap_weight_series"],
        "verification": data["verification"],
        "caution": data["caution"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Measure finite additive-basin stability across a registered depth window."
    )
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--min-depth", type=int, default=0)
    parser.add_argument("--max-depth", type=int, default=5)
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        data = analyze(
            args.limit,
            args.min_depth,
            args.max_depth,
            include_records=not args.summary_only,
        )
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
