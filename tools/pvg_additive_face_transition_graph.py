from __future__ import annotations

import argparse
import json
from collections import Counter

try:
    from tools.pvg_local_additive_cell_atlas import analyze as analyze_cells
except ModuleNotFoundError:
    from pvg_local_additive_cell_atlas import analyze as analyze_cells


def face_key(axes: list[int] | tuple[int, ...]) -> str:
    return "{" + ",".join(str(x) for x in axes) + "}"


def analyze(limit: int = 100) -> dict[str, object]:
    atlas = analyze_cells(limit)
    cells = atlas["cells"]

    destination_counts: Counter[tuple[int, ...]] = Counter()
    destination_axis_frequency: Counter[int] = Counter()
    source_axis_frequency: Counter[int] = Counter()
    transition_types: Counter[str] = Counter()
    records: list[dict[str, object]] = []

    for cell in cells:
        p = int(cell["p"])
        q = int(cell["q"])
        destination = tuple(int(x) for x in cell["sum_destination_axes"])
        destination_counts[destination] += 1
        destination_axis_frequency.update(destination)
        source_axis_frequency.update((p, q))

        if len(destination) == 1:
            transition_type = "prime_axis" if bool(cell["sum_is_prime"]) else "prime_power_axis"
        else:
            transition_type = "composite_face"
        transition_types[transition_type] += 1

        records.append(
            {
                "source_face": [p, q],
                "destination_face": list(destination),
                "source_key": face_key((p, q)),
                "destination_key": face_key(destination),
                "sum": int(cell["sum"]),
                "sum_Omega": int(cell["sum_Omega"]),
                "sum_omega": int(cell["sum_omega"]),
                "transition_type": transition_type,
                "source_destination_disjoint": not ({p, q} & set(destination)),
                "contains_axis_2_at_destination": 2 in destination,
            }
        )

    ranked_faces = [
        {"face": list(face), "key": face_key(face), "indegree": count}
        for face, count in sorted(destination_counts.items(), key=lambda item: (-item[1], item[0]))
    ]
    ranked_axes = [
        {"axis": axis, "weighted_indegree": count}
        for axis, count in sorted(destination_axis_frequency.items(), key=lambda item: (-item[1], item[0]))
    ]

    odd_odd_count = sum(1 for r in records if r["source_face"][0] != 2)
    return {
        "schema": "PVG-ADDITIVE-FACE-TRANSITION-GRAPH-001",
        "limit": limit,
        "source_face_count": len(records),
        "unique_destination_face_count": len(destination_counts),
        "transition_type_distribution": dict(sorted(transition_types.items())),
        "destination_face_dimension_distribution": dict(
            sorted(Counter(len(r["destination_face"]) for r in records).items())
        ),
        "destination_faces_ranked": ranked_faces,
        "destination_axes_ranked": ranked_axes,
        "source_axes_ranked": [
            {"axis": axis, "weighted_outdegree": count}
            for axis, count in sorted(source_axis_frequency.items(), key=lambda item: (-item[1], item[0]))
        ],
        "axis_2_destination_count": destination_axis_frequency[2],
        "odd_odd_source_count": odd_odd_count,
        "axis_2_routing_identity": "every odd-odd prime pair has even sum, so its destination support contains axis 2",
        "bipartite_structure": {
            "source_partition": "unordered prime-pair faces {p,q}",
            "destination_partition": "support faces supp(p+q)",
            "directed_edge_count": len(records),
            "acyclic_by_typing": True,
        },
        "verification": {
            "all_source_destination_faces_are_disjoint": all(r["source_destination_disjoint"] for r in records),
            "all_odd_odd_sources_route_to_axis_2": all(
                r["contains_axis_2_at_destination"] for r in records if r["source_face"][0] != 2
            ),
            "axis_2_destination_count_matches_odd_odd_sources": destination_axis_frequency[2] == odd_odd_count,
            "destination_counts_close": sum(destination_counts.values()) == len(records),
            "transition_types_close": sum(transition_types.values()) == len(records),
        },
        "transitions": records,
        "scientific_classification": "exact face-transition encoding plus finite verification; no asymptotic, centrality theorem, or novelty claim",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the additive face-transition graph for prime-pair PVG cells.")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    if args.limit < 3:
        parser.error("--limit must be at least 3")
    print(json.dumps(analyze(args.limit), ensure_ascii=False, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
