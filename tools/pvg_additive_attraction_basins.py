from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from collections.abc import Iterable

try:
    from tools.pvg_additive_face_transition_graph import analyze as analyze_one_step
    from tools.pvg_iterated_additive_face_dynamics import successors
except ModuleNotFoundError:
    from pvg_additive_face_transition_graph import analyze as analyze_one_step
    from pvg_iterated_additive_face_dynamics import successors

Face = tuple[int, ...]


def face_key(face: Face) -> str:
    return "{" + ",".join(str(x) for x in face) + "}"


def _cycle_faces(arcs: set[tuple[Face, Face]]) -> set[Face]:
    adjacency: dict[Face, set[Face]] = defaultdict(set)
    nodes: set[Face] = set()
    for source, target in arcs:
        adjacency[source].add(target)
        nodes.update((source, target))

    cyclic: set[Face] = set()
    for start in nodes:
        stack = list(adjacency[start])
        visited: set[Face] = set()
        while stack:
            node = stack.pop()
            if node == start:
                cyclic.add(start)
                break
            if node in visited:
                continue
            visited.add(node)
            stack.extend(adjacency[node] - visited)
    return cyclic


def _shortest_depths(levels: list[set[Face]]) -> dict[Face, int]:
    out: dict[Face, int] = {}
    for depth, level in enumerate(levels):
        for face in level:
            out.setdefault(face, depth)
    return out


def analyze_start(start: Face, depth: int) -> dict[str, object]:
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    if not start:
        raise ValueError("start face must be nonempty")
    if tuple(sorted(set(start))) != start:
        raise ValueError("start face must be a strictly increasing tuple")

    levels: list[set[Face]] = [{start}]
    occurrence_depths: dict[Face, set[int]] = defaultdict(set)
    occurrence_depths[start].add(0)
    arcs: set[tuple[Face, Face]] = set()

    for current_depth in range(depth):
        next_level: set[Face] = set()
        for face in levels[-1]:
            for target in successors(face):
                arcs.add((face, target))
                next_level.add(target)
                occurrence_depths[target].add(current_depth + 1)
        levels.append(next_level)

    shortest = _shortest_depths(levels)
    all_faces = set(shortest)
    terminal_faces = sorted(face for face in all_faces if len(face) == 1)
    expanded_before_bound = {
        face for level in levels[:-1] for face in level if len(face) >= 2
    }
    unresolved_frontier = sorted(
        face
        for face in levels[-1]
        if len(face) >= 2 and face not in expanded_before_bound
    )
    reappearing_faces = sorted(
        face for face, depths in occurrence_depths.items() if len(depths) > 1
    )
    cyclic_faces = sorted(_cycle_faces(arcs))

    if len(start) == 1:
        bounded_status = "terminal_singleton"
    elif unresolved_frontier:
        bounded_status = "unresolved_at_depth_bound"
    elif reappearing_faces:
        bounded_status = "recurrent_or_reappearing_face"
    else:
        bounded_status = "transient_face"

    terminal_axes = [face[0] for face in terminal_faces]
    endpoint_multiplicity = (
        "none_observed"
        if not terminal_axes
        else "single_terminal"
        if len(terminal_axes) == 1
        else "multiple_terminals"
    )

    return {
        "start_face": list(start),
        "start_key": face_key(start),
        "depth_bound": depth,
        "bounded_status": bounded_status,
        "endpoint_multiplicity": endpoint_multiplicity,
        "terminal_axes": terminal_axes,
        "terminal_key": face_key(tuple(terminal_axes)),
        "shortest_terminal_depths": {
            str(face[0]): shortest[face] for face in terminal_faces
        },
        "reachable_face_count": len(all_faces),
        "reachable_faces": [list(face) for face in sorted(all_faces)],
        "layer_faces": [[list(face) for face in sorted(level)] for level in levels],
        "arc_count": len(arcs),
        "arcs": [
            {"source": list(source), "target": list(target)}
            for source, target in sorted(arcs)
        ],
        "unresolved_frontier_faces": [list(face) for face in unresolved_frontier],
        "reappearing_faces": [
            {
                "face": list(face),
                "depths": sorted(occurrence_depths[face]),
                "terminal": len(face) == 1,
            }
            for face in reappearing_faces
        ],
        "cycle_faces": [list(face) for face in cyclic_faces],
        "bounded_closure_reached": not unresolved_frontier,
    }


def _registered_starts(limit: int) -> list[Face]:
    first = analyze_one_step(limit)
    return sorted(
        {tuple(int(x) for x in row["source_face"]) for row in first["transitions"]}
    )


def _axis_basin_records(records: list[dict[str, object]]) -> list[dict[str, object]]:
    axes = sorted({axis for record in records for axis in record["terminal_axes"]})
    out: list[dict[str, object]] = []
    for axis in axes:
        members = [record for record in records if axis in record["terminal_axes"]]
        exclusive = [record for record in members if record["terminal_axes"] == [axis]]
        depth_distribution = Counter(
            int(record["shortest_terminal_depths"][str(axis)]) for record in members
        )
        out.append(
            {
                "axis": axis,
                "basin_size": len(members),
                "exclusive_basin_size": len(exclusive),
                "shared_basin_size": len(members) - len(exclusive),
                "shortest_depth_distribution": {
                    str(k): v for k, v in sorted(depth_distribution.items())
                },
                "minimum_shortest_depth": min(depth_distribution),
                "maximum_shortest_depth": max(depth_distribution),
            }
        )
    return out


def _endpoint_signatures(records: list[dict[str, object]]) -> list[dict[str, object]]:
    counts = Counter(tuple(record["terminal_axes"]) for record in records)
    return [
        {
            "terminal_axes": list(axes),
            "terminal_key": face_key(axes),
            "start_face_count": count,
        }
        for axes, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    ]


def analyze(limit: int = 100, depth: int = 5, include_records: bool = True) -> dict[str, object]:
    if limit < 3:
        raise ValueError("limit must be at least 3")
    if depth < 0:
        raise ValueError("depth must be nonnegative")

    starts = _registered_starts(limit)
    records = [analyze_start(start, depth) for start in starts]
    basins = _axis_basin_records(records)
    signatures = _endpoint_signatures(records)
    status_counts = Counter(record["bounded_status"] for record in records)
    status_distribution = {
        status: status_counts[status]
        for status in (
            "terminal_singleton",
            "transient_face",
            "recurrent_or_reappearing_face",
            "unresolved_at_depth_bound",
        )
    }
    multiplicity_counts = Counter(record["endpoint_multiplicity"] for record in records)
    multiplicity_distribution = {
        status: multiplicity_counts[status]
        for status in ("none_observed", "single_terminal", "multiple_terminals")
    }
    terminal_count_distribution = Counter(len(record["terminal_axes"]) for record in records)

    result: dict[str, object] = {
        "schema": "PVG-ADDITIVE-ATTRACTION-BASINS-001",
        "classification": (
            "finite verified depth-bounded additive-face reachability; "
            "no general termination, convergence, asymptotic, or novelty claim"
        ),
        "scope": {
            "prime_limit": limit,
            "depth_bound": depth,
            "start_face_count": len(starts),
            "start_family": "all unordered prime-pair faces {p,q} with p<q<=limit",
        },
        "terminal_axes": [record["axis"] for record in basins],
        "terminal_axis_count": len(basins),
        "axis_basins": basins,
        "endpoint_signature_count": len(signatures),
        "endpoint_signatures": signatures,
        "endpoint_multiplicity_distribution": multiplicity_distribution,
        "terminal_count_distribution": {
            str(count): terminal_count_distribution[count]
            for count in range(max(terminal_count_distribution, default=0) + 1)
        },
        "bounded_status_distribution": status_distribution,
        "single_terminal_start_count": multiplicity_counts["single_terminal"],
        "multiple_terminal_start_count": multiplicity_counts["multiple_terminals"],
        "no_terminal_observed_start_count": multiplicity_counts["none_observed"],
        "unresolved_start_count": sum(bool(record["unresolved_frontier_faces"]) for record in records),
        "reappearing_start_count": sum(bool(record["reappearing_faces"]) for record in records),
        "observed_cycle_start_count": sum(bool(record["cycle_faces"]) for record in records),
        "maximum_reachable_face_count_per_start": max(record["reachable_face_count"] for record in records),
        "verification": {
            "registered_start_count_matches_one_step_atlas": len(starts) == analyze_one_step(limit)["source_face_count"],
            "status_partition_closes": sum(status_distribution.values()) == len(starts),
            "endpoint_multiplicity_partition_closes": sum(multiplicity_distribution.values()) == len(starts),
            "terminal_count_partition_closes": sum(terminal_count_distribution.values()) == len(starts),
            "endpoint_signature_counts_close": sum(item["start_face_count"] for item in signatures) == len(starts),
            "basin_membership_matches_records": all(
                basin["basin_size"]
                == sum(basin["axis"] in record["terminal_axes"] for record in records)
                for basin in basins
            ),
            "exclusive_and_shared_basins_close": all(
                basin["exclusive_basin_size"] + basin["shared_basin_size"] == basin["basin_size"]
                for basin in basins
            ),
            "terminal_singletons_have_no_successors": all(
                not successors((int(basin["axis"]),)) for basin in basins
            ),
            "shortest_terminal_depths_match_layers": all(
                all(
                    any(level_face == [axis] for level_face in record["layer_faces"][int(depth_value)])
                    for axis, depth_value in (
                        (int(axis_text), depth_value)
                        for axis_text, depth_value in record["shortest_terminal_depths"].items()
                    )
                )
                for record in records
            ),
            "unresolved_status_matches_frontier": all(
                (record["bounded_status"] == "unresolved_at_depth_bound")
                == bool(record["unresolved_frontier_faces"])
                for record in records
                if record["bounded_status"] != "terminal_singleton"
            ),
        },
        "caution": (
            "A face may reappear at several depths without lying on a directed cycle. "
            "Reappearance and recurrence are therefore reported separately through occurrence depths and cycle_faces."
        ),
    }
    if include_records:
        result["start_records"] = records
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute finite additive attraction basins for PVG support faces.")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--depth", type=int, default=5)
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        data = analyze(args.limit, args.depth, include_records=not args.summary_only)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
