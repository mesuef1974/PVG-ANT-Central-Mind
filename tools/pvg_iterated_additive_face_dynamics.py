from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations

try:
    from tools.pvg_additive_face_transition_graph import analyze as analyze_one_step
    from tools.pvg_local_additive_cell_atlas import factorint
except ModuleNotFoundError:
    from pvg_additive_face_transition_graph import analyze as analyze_one_step
    from pvg_local_additive_cell_atlas import factorint


def support(n: int) -> tuple[int, ...]:
    return tuple(sorted(int(p) for p in factorint(n))) if n > 1 else tuple()


def successors(face: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    if len(face) < 2:
        return tuple()
    return tuple(sorted({support(a + b) for a, b in combinations(face, 2)}))


def analyze(limit: int = 100, depth: int = 4) -> dict[str, object]:
    if depth < 1:
        raise ValueError("depth must be at least 1")
    first = analyze_one_step(limit)
    starts = {tuple(int(x) for x in row["source_face"]) for row in first["transitions"]}
    levels: list[set[tuple[int, ...]]] = [set(starts)]
    arcs: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    all_faces = set(starts)
    for _ in range(depth):
        nxt: set[tuple[int, ...]] = set()
        for face in levels[-1]:
            for target in successors(face):
                arcs.add((face, target))
                nxt.add(target)
                all_faces.add(target)
        levels.append(nxt)

    terminals = sorted(face for face in all_faces if len(face) < 2)
    dimension_distribution = Counter(len(face) for face in all_faces)
    return {
        "schema": "PVG-ITERATED-ADDITIVE-FACE-DYNAMICS-001",
        "classification": "exact finite depth-truncated face dynamics; no asymptotic, termination, or novelty claim",
        "scope": {"prime_limit": limit, "depth": depth, "start_face_count": len(starts)},
        "layer_face_counts": [len(layer) for layer in levels],
        "layer_faces": [[list(face) for face in sorted(layer)] for layer in levels],
        "unique_face_count": len(all_faces),
        "unique_arc_count": len(arcs),
        "face_dimension_distribution": {str(k): v for k, v in sorted(dimension_distribution.items())},
        "terminal_faces": [list(face) for face in terminals],
        "terminal_face_count": len(terminals),
        "verification": {
            "registered_start_count": len(starts) == first["source_face_count"],
            "all_arcs_are_generated_by_pair_sums": all(v in successors(u) for u, v in arcs),
            "singletons_are_terminal": all(not successors(face) for face in terminals),
            "depth_layers_close": all(levels[i + 1] == {v for u, v in arcs if u in levels[i]} for i in range(depth)),
            "no_observed_self_loops": all(u != v for u, v in arcs),
        },
        "caution": "Layer membership is not a global topological rank because a face may reappear at multiple depths.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Explore finite iterated additive face dynamics in PVG.")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    print(json.dumps(analyze(args.limit, args.depth), ensure_ascii=False, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
