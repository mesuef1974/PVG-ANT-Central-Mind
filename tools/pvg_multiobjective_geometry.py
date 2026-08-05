#!/usr/bin/env python3
"""Multiobjective edge signatures and Pareto geometry on a fixed PVG level.

All registered objectives are maximized.  The default objective vector is

    (n, tau, sigma(n)/n, phi(n)/n).

The module distinguishes global Pareto dominance from adjacency-local Pareto
improvement.  It is an exact finite analyzer; it makes no asymptotic or novelty
claim.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from typing import Iterable

try:
    from .pvg_level_terrain import analyze as terrain_analyze, parse_primes
    from .pvg_inverse_geometry import GeometryInputError
except ImportError:
    from pvg_level_terrain import analyze as terrain_analyze, parse_primes  # type: ignore
    from pvg_inverse_geometry import GeometryInputError  # type: ignore

OBJECTIVES = ("n", "tau", "sigma_over_n", "phi_over_n")


def value(row: dict, field: str) -> Fraction:
    raw = row[field]
    if isinstance(raw, dict):
        return Fraction(raw["numerator"], raw["denominator"])
    return Fraction(raw, 1)


def adjacent(a: tuple[int, ...], b: tuple[int, ...]) -> bool:
    return sum(a) == sum(b) and sum(abs(x - y) for x, y in zip(a, b)) == 2


def sign(delta: Fraction) -> int:
    return (delta > 0) - (delta < 0)


def dominates(left: dict, right: dict, objectives: Iterable[str] = OBJECTIVES) -> bool:
    """Return whether left weakly dominates right, with one strict gain."""
    comparisons = [value(left, f) - value(right, f) for f in objectives]
    return all(d >= 0 for d in comparisons) and any(d > 0 for d in comparisons)


def signature_class(signature: tuple[int, ...]) -> str:
    nonzero = {s for s in signature if s}
    zeros = sum(s == 0 for s in signature)
    if not nonzero:
        return "all_equal"
    if nonzero == {1}:
        return "aligned_increase_with_ties" if zeros else "aligned_increase"
    if nonzero == {-1}:
        return "aligned_decrease_with_ties" if zeros else "aligned_decrease"
    return "tradeoff_with_ties" if zeros else "strict_tradeoff"


def analyze(primes: list[int], level: int) -> dict:
    terrain = terrain_analyze(primes, level)
    rows = {tuple(row["exponents"]): row for row in terrain["points"]}
    nodes = sorted(rows)
    edges = [
        (nodes[i], nodes[j])
        for i in range(len(nodes))
        for j in range(i + 1, len(nodes))
        if adjacent(nodes[i], nodes[j])
    ]

    edge_records = []
    class_counts: Counter[str] = Counter()
    pattern_counts: Counter[str] = Counter()
    dominance_edges = 0
    tradeoff_edges = 0

    for a, b in edges:
        deltas = {f: value(rows[b], f) - value(rows[a], f) for f in OBJECTIVES}
        sig = tuple(sign(deltas[f]) for f in OBJECTIVES)
        classification = signature_class(sig)
        class_counts[classification] += 1
        pattern = "(" + ",".join(f"{x:+d}" for x in sig) + ")"
        pattern_counts[pattern] += 1

        if dominates(rows[b], rows[a]):
            relation = "b_dominates_a"
            dominance_edges += 1
        elif dominates(rows[a], rows[b]):
            relation = "a_dominates_b"
            dominance_edges += 1
        else:
            relation = "tradeoff_or_equal"
            tradeoff_edges += 1

        edge_records.append(
            {
                "a": list(a),
                "b": list(b),
                "a_n": rows[a]["n"],
                "b_n": rows[b]["n"],
                "signature": {f: sig[i] for i, f in enumerate(OBJECTIVES)},
                "signature_pattern": pattern,
                "classification": classification,
                "pareto_relation": relation,
                "delta": {
                    f: {
                        "numerator": deltas[f].numerator,
                        "denominator": deltas[f].denominator,
                        "text": f"{deltas[f].numerator}/{deltas[f].denominator}",
                    }
                    for f in OBJECTIVES
                },
            }
        )

    global_frontier = []
    dominated_by: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    local_frontier = []
    local_dominators: dict[tuple[int, ...], list[tuple[int, ...]]] = {}

    neighbors = {node: [] for node in nodes}
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    for node in nodes:
        global_ds = [other for other in nodes if other != node and dominates(rows[other], rows[node])]
        dominated_by[node] = global_ds
        if not global_ds:
            global_frontier.append(node)

        local_ds = [other for other in neighbors[node] if dominates(rows[other], rows[node])]
        local_dominators[node] = local_ds
        if not local_ds:
            local_frontier.append(node)

    frontier_records = [
        {
            "exponents": list(node),
            "n": rows[node]["n"],
            "objectives": {
                f: (
                    rows[node][f]
                    if not isinstance(rows[node][f], dict)
                    else rows[node][f]["text"]
                )
                for f in OBJECTIVES
            },
        }
        for node in global_frontier
    ]

    return {
        "schema": "PVG-MULTIOBJECTIVE-GEOMETRY-001",
        "axes": primes,
        "level": level,
        "point_count": len(nodes),
        "edge_count": len(edges),
        "objectives": list(OBJECTIVES),
        "objective_orientation": "maximize_all",
        "edge_class_counts": dict(sorted(class_counts.items())),
        "signature_pattern_counts": dict(sorted(pattern_counts.items())),
        "pareto_dominance_edge_count": dominance_edges,
        "pareto_tradeoff_or_equal_edge_count": tradeoff_edges,
        "global_pareto_frontier": frontier_records,
        "global_pareto_frontier_size": len(global_frontier),
        "local_pareto_frontier": [list(node) for node in local_frontier],
        "local_pareto_frontier_size": len(local_frontier),
        "dominated_point_count": sum(bool(v) for v in dominated_by.values()),
        "edge_records": edge_records,
        "verification": {
            "edge_partition_closes": dominance_edges + tradeoff_edges == len(edges),
            "global_frontier_is_nondominated": all(not dominated_by[n] for n in global_frontier),
            "local_frontier_has_no_adjacent_dominator": all(not local_dominators[n] for n in local_frontier),
            "every_nonfrontier_point_is_dominated": all(dominated_by[n] for n in nodes if n not in global_frontier),
        },
        "classification": (
            "exact finite multiobjective graph geometry on one PVG level; "
            "Pareto results depend on the registered objective list and maximize-all convention"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze multiobjective PVG edge geometry and Pareto fronts.")
    parser.add_argument("axes", help="comma-separated prime axes, e.g. 2,3,5")
    parser.add_argument("level", type=int, help="fixed Omega level")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        report = analyze(parse_primes(args.axes), args.level)
    except (GeometryInputError, ValueError) as exc:
        print(json.dumps({"status": "invalid_multiobjective_input", "reason": str(exc)}, indent=2))
        return 2
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
