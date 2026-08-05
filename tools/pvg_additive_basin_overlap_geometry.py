from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

try:
    from tools.pvg_additive_attraction_basins import analyze as analyze_basins
    from tools.pvg_additive_attraction_basins import face_key
except ModuleNotFoundError:
    from pvg_additive_attraction_basins import analyze as analyze_basins
    from pvg_additive_attraction_basins import face_key

AxisSet = tuple[int, ...]


def signature_key(axes: AxisSet) -> str:
    return face_key(axes)


def _components(nodes: list[object], edges: list[tuple[object, object]]) -> list[list[object]]:
    adjacency: dict[object, set[object]] = {node: set() for node in nodes}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen: set[object] = set()
    out: list[list[object]] = []
    for start in nodes:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        component: list[object] = []
        while stack:
            node = stack.pop()
            component.append(node)
            for neighbor in adjacency[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        out.append(sorted(component))
    return sorted(out, key=lambda component: (-len(component), component))


def _component_count(
    nodes: list[object],
    edges: list[tuple[object, object]],
    removed_node: object | None = None,
    removed_edge: tuple[object, object] | None = None,
) -> int:
    active = [node for node in nodes if node != removed_node]
    filtered: list[tuple[object, object]] = []
    removed_edge_set = set(removed_edge) if removed_edge is not None else None
    for left, right in edges:
        if removed_node in (left, right):
            continue
        if removed_edge_set is not None and {left, right} == removed_edge_set:
            continue
        filtered.append((left, right))
    return len(_components(active, filtered))


def _articulations_and_bridges(
    nodes: list[object], edges: list[tuple[object, object]]
) -> tuple[list[object], list[tuple[object, object]]]:
    base_components = _component_count(nodes, edges)
    articulations = [
        node
        for node in nodes
        if _component_count(nodes, edges, removed_node=node) > base_components
    ]
    bridges = [
        edge
        for edge in edges
        if _component_count(nodes, edges, removed_edge=edge) > base_components
    ]
    return sorted(articulations), sorted(bridges)


def _signature_poset(signature_counts: Counter[AxisSet]) -> dict[str, object]:
    signatures = sorted(signature_counts, key=lambda axes: (len(axes), axes))
    comparable_pairs: list[tuple[AxisSet, AxisSet]] = []
    covers: list[tuple[AxisSet, AxisSet]] = []
    for lower in signatures:
        lower_set = set(lower)
        for upper in signatures:
            upper_set = set(upper)
            if not lower_set < upper_set:
                continue
            comparable_pairs.append((lower, upper))
            if not any(lower_set < set(middle) < upper_set for middle in signatures):
                covers.append((lower, upper))

    predecessor_map: dict[AxisSet, list[AxisSet]] = defaultdict(list)
    successor_map: dict[AxisSet, list[AxisSet]] = defaultdict(list)
    for lower, upper in covers:
        predecessor_map[upper].append(lower)
        successor_map[lower].append(upper)

    longest: dict[AxisSet, int] = {}
    for signature in signatures:
        longest[signature] = 1 + max(
            (longest[pred] for pred in predecessor_map[signature]),
            default=0,
        )

    components = _components(signatures, covers)
    articulations, bridges = _articulations_and_bridges(signatures, covers)
    minimal = [sig for sig in signatures if not predecessor_map[sig]]
    maximal = [sig for sig in signatures if not successor_map[sig]]
    triple_signatures = [sig for sig in signatures if len(sig) == 3]
    triples_with_pair_predecessor = [
        sig
        for sig in triple_signatures
        if any(len(pred) == 2 for pred in predecessor_map[sig])
    ]

    return {
        "signature_count": len(signatures),
        "rank_distribution": {
            str(rank): sum(len(sig) == rank for sig in signatures)
            for rank in sorted({len(sig) for sig in signatures})
        },
        "comparable_pair_count": len(comparable_pairs),
        "cover_edge_count": len(covers),
        "component_count": len(components),
        "component_sizes": [len(component) for component in components],
        "cycle_rank": len(covers) - len(signatures) + len(components),
        "longest_chain_node_count": max(longest.values(), default=0),
        "minimal_signatures": [list(sig) for sig in minimal],
        "maximal_signatures": [list(sig) for sig in maximal],
        "articulation_signatures": [list(sig) for sig in articulations],
        "bridge_cover_relations": [
            {"lower": list(lower), "upper": list(upper)} for lower, upper in bridges
        ],
        "triple_signature_count": len(triple_signatures),
        "triple_signatures_with_observed_pair_predecessor_count": len(
            triples_with_pair_predecessor
        ),
        "triple_signatures_with_observed_pair_predecessor": [
            list(sig) for sig in triples_with_pair_predecessor
        ],
        "nodes": [
            {
                "terminal_axes": list(sig),
                "terminal_key": signature_key(sig),
                "start_face_count": signature_counts[sig],
                "rank": len(sig),
                "cover_indegree": len(predecessor_map[sig]),
                "cover_outdegree": len(successor_map[sig]),
                "longest_chain_ending_here": longest[sig],
            }
            for sig in signatures
        ],
        "cover_relations": [
            {
                "lower": list(lower),
                "lower_key": signature_key(lower),
                "upper": list(upper),
                "upper_key": signature_key(upper),
            }
            for lower, upper in covers
        ],
    }


def analyze(
    limit: int = 100,
    depth: int = 5,
    include_records: bool = True,
    include_unobserved_signatures: bool = True,
) -> dict[str, object]:
    if limit < 3:
        raise ValueError("limit must be at least 3")
    if depth < 0:
        raise ValueError("depth must be nonnegative")

    basin_data = analyze_basins(limit, depth, include_records=True)
    records = basin_data["start_records"]
    terminal_axes = tuple(int(axis) for axis in basin_data["terminal_axes"])
    basin_sets: dict[int, set[tuple[int, ...]]] = {
        axis: {
            tuple(int(x) for x in record["start_face"])
            for record in records
            if axis in record["terminal_axes"]
        }
        for axis in terminal_axes
    }
    basin_lookup = {int(item["axis"]): item for item in basin_data["axis_basins"]}
    signature_counts: Counter[AxisSet] = Counter(
        tuple(int(axis) for axis in record["terminal_axes"]) for record in records
    )

    pair_records: list[dict[str, object]] = []
    positive_pair_edges: list[tuple[int, int]] = []
    pair_weights: dict[tuple[int, int], int] = {}
    for left, right in combinations(terminal_axes, 2):
        intersection = basin_sets[left] & basin_sets[right]
        intersection_size = len(intersection)
        if not intersection_size:
            continue
        union_size = len(basin_sets[left] | basin_sets[right])
        pair = (left, right)
        pair_weights[pair] = intersection_size
        positive_pair_edges.append(pair)
        exact_pair_signature_count = signature_counts[pair]
        pair_records.append(
            {
                "axes": [left, right],
                "key": signature_key(pair),
                "intersection_size": intersection_size,
                "union_size": union_size,
                "jaccard_numerator": intersection_size,
                "jaccard_denominator": union_size,
                "jaccard": intersection_size / union_size,
                "exact_pair_signature_count": exact_pair_signature_count,
                "higher_order_mediated_count": intersection_size
                - exact_pair_signature_count,
            }
        )
    pair_records.sort(key=lambda item: (-int(item["intersection_size"]), item["axes"]))

    triple_records: list[dict[str, object]] = []
    for triple in combinations(terminal_axes, 3):
        intersection = set.intersection(*(basin_sets[axis] for axis in triple))
        if not intersection:
            continue
        triple_records.append(
            {
                "axes": list(triple),
                "key": signature_key(triple),
                "intersection_size": len(intersection),
                "exact_triple_signature_count": signature_counts[triple],
            }
        )
    triple_records.sort(key=lambda item: (-int(item["intersection_size"]), item["axes"]))

    adjacency: dict[int, set[int]] = {axis: set() for axis in terminal_axes}
    for left, right in positive_pair_edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    axis_nodes: list[dict[str, object]] = []
    for axis in terminal_axes:
        weighted_degree = sum(
            pair_weights[tuple(sorted((axis, neighbor)))] for neighbor in adjacency[axis]
        )
        basin = basin_lookup[axis]
        axis_nodes.append(
            {
                "axis": axis,
                "basin_size": int(basin["basin_size"]),
                "exclusive_basin_size": int(basin["exclusive_basin_size"]),
                "shared_basin_size": int(basin["shared_basin_size"]),
                "overlap_degree": len(adjacency[axis]),
                "weighted_overlap_degree": weighted_degree,
                "overlap_partner_axes": sorted(adjacency[axis]),
            }
        )

    components = _components(list(terminal_axes), positive_pair_edges)
    articulations, bridges = _articulations_and_bridges(
        list(terminal_axes), positive_pair_edges
    )
    isolated_axes = sorted(axis for axis in terminal_axes if not adjacency[axis])

    observed_pairs = {sig for sig in signature_counts if len(sig) == 2}
    observed_triples = {sig for sig in signature_counts if len(sig) == 3}
    all_pairs = set(combinations(terminal_axes, 2))
    all_triples = set(combinations(terminal_axes, 3))
    unobserved_pairs = sorted(all_pairs - observed_pairs)
    unobserved_triples = sorted(all_triples - observed_triples)

    poset = _signature_poset(signature_counts)
    gateway_signatures = [
        {
            "terminal_axes": list(signature),
            "terminal_key": signature_key(signature),
            "start_face_count": count,
            "endpoint_pair_count": comb(len(signature), 2),
            "routed_pair_memberships": count * comb(len(signature), 2),
        }
        for signature, count in signature_counts.items()
        if len(signature) >= 2
    ]
    gateway_signatures.sort(
        key=lambda item: (
            -int(item["routed_pair_memberships"]),
            -int(item["start_face_count"]),
            item["terminal_axes"],
        )
    )

    result: dict[str, object] = {
        "schema": "PVG-ADDITIVE-BASIN-OVERLAP-GEOMETRY-001",
        "classification": (
            "finite verified overlap geometry of depth-bounded additive attraction basins; "
            "unobserved signatures are not declared impossible and no general centrality, "
            "termination, convergence, asymptotic, or novelty claim is made"
        ),
        "scope": {
            "prime_limit": limit,
            "depth_bound": depth,
            "start_face_count": int(basin_data["scope"]["start_face_count"]),
            "terminal_axis_count": len(terminal_axes),
            "endpoint_signature_count": len(signature_counts),
        },
        "terminal_axes": list(terminal_axes),
        "axis_overlap_graph": {
            "node_count": len(terminal_axes),
            "edge_count": len(positive_pair_edges),
            "component_count": len(components),
            "component_axes": [list(component) for component in components],
            "component_sizes": [len(component) for component in components],
            "isolated_axes": isolated_axes,
            "cycle_rank": len(positive_pair_edges) - len(terminal_axes) + len(components),
            "articulation_axes": articulations,
            "bridge_edges": [list(edge) for edge in bridges],
            "axis_nodes": sorted(axis_nodes, key=lambda item: int(item["axis"])),
            "pair_overlaps": pair_records,
            "basin_size_ranking": sorted(
                axis_nodes,
                key=lambda item: (-int(item["basin_size"]), int(item["axis"])),
            ),
            "overlap_degree_ranking": sorted(
                axis_nodes,
                key=lambda item: (
                    -int(item["overlap_degree"]),
                    -int(item["weighted_overlap_degree"]),
                    int(item["axis"]),
                ),
            ),
            "weighted_overlap_degree_ranking": sorted(
                axis_nodes,
                key=lambda item: (
                    -int(item["weighted_overlap_degree"]),
                    -int(item["overlap_degree"]),
                    int(item["axis"]),
                ),
            ),
        },
        "triple_overlaps": triple_records,
        "signature_observation": {
            "possible_exact_pair_signature_count": len(all_pairs),
            "observed_exact_pair_signature_count": len(observed_pairs),
            "unobserved_exact_pair_signature_count": len(unobserved_pairs),
            "possible_exact_triple_signature_count": len(all_triples),
            "observed_exact_triple_signature_count": len(observed_triples),
            "unobserved_exact_triple_signature_count": len(unobserved_triples),
            "all_terminal_axes_observed_as_exact_singletons": all(
                signature_counts[(axis,)] > 0 for axis in terminal_axes
            ),
            "warning": (
                "Unobserved means absent from the registered 300-start, depth-bounded family; "
                "it does not mean mathematically impossible."
            ),
        },
        "signature_poset": poset,
        "gateway_signature_count": len(gateway_signatures),
        "gateway_start_count": sum(
            count
            for signature, count in signature_counts.items()
            if len(signature) >= 2
        ),
        "gateway_signatures": gateway_signatures,
        "verification": {
            "pass016_verification_flags_hold": all(basin_data["verification"].values()),
            "pair_overlap_weight_closes": sum(
                int(item["intersection_size"]) for item in pair_records
            )
            == sum(comb(len(record["terminal_axes"]), 2) for record in records),
            "triple_overlap_weight_closes": sum(
                int(item["intersection_size"]) for item in triple_records
            )
            == sum(comb(len(record["terminal_axes"]), 3) for record in records),
            "weighted_degrees_close": sum(
                int(item["weighted_overlap_degree"]) for item in axis_nodes
            )
            == 2 * sum(int(item["intersection_size"]) for item in pair_records),
            "signature_counts_close": sum(signature_counts.values()) == len(records),
            "gateway_memberships_close": sum(
                int(item["routed_pair_memberships"]) for item in gateway_signatures
            )
            == sum(int(item["intersection_size"]) for item in pair_records),
            "pair_signature_decomposition_closes": all(
                int(item["exact_pair_signature_count"])
                + int(item["higher_order_mediated_count"])
                == int(item["intersection_size"])
                for item in pair_records
            ),
            "all_exact_singletons_observed": all(
                signature_counts[(axis,)] > 0 for axis in terminal_axes
            ),
            "positive_edges_match_positive_intersections": len(pair_records)
            == sum(
                bool(basin_sets[left] & basin_sets[right])
                for left, right in combinations(terminal_axes, 2)
            ),
        },
        "caution": (
            "Overlap centrality is relative to the registered initial family and depth bound. "
            "A zero edge or unobserved exact signature is a finite absence, not a prohibition theorem."
        ),
    }
    if include_unobserved_signatures:
        result["signature_observation"]["unobserved_exact_pair_signatures"] = [
            list(pair) for pair in unobserved_pairs
        ]
        result["signature_observation"]["unobserved_exact_triple_signatures"] = [
            list(triple) for triple in unobserved_triples
        ]
    if include_records:
        result["start_gateway_records"] = [
            {
                "start_face": record["start_face"],
                "start_key": record["start_key"],
                "terminal_axes": record["terminal_axes"],
                "terminal_key": record["terminal_key"],
                "gateway": len(record["terminal_axes"]) >= 2,
                "endpoint_pair_count": comb(len(record["terminal_axes"]), 2),
            }
            for record in records
        ]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute finite overlap geometry for PVG additive attraction basins."
    )
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--depth", type=int, default=5)
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        data = analyze(
            args.limit,
            args.depth,
            include_records=not args.summary_only,
            include_unobserved_signatures=not args.summary_only,
        )
    except ValueError as exc:
        parser.error(str(exc))
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
