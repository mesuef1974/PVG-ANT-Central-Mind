"""Optimized full-domain verifier for ACTIVE-003-S.

Benchmark: 4 <= N <= 120, 3 <= r <= 30, exact budgets B <= 4.
Uses bit masks and direct minimal-antichain generation. It verifies that the
minimal forbidden hyperedges reproduce the exact higher-order compatibility
bound without enumerating every forbidden superset.
"""
from __future__ import annotations

import functools
import importlib.util
import itertools
import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "verify_certification_margin_aware_pruning.py"
spec = importlib.util.spec_from_file_location("active003q", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

EPS = base.EPS


def mandatory_closures(included, excluded, undecided, slots, lower_empty, gains, contamination, ancestors):
    closures = {}
    for channel in range(len(contamination)):
        current = lower_empty[channel] + sum(gains[k][channel] for k in included)
        if current > contamination[channel] + EPS:
            closures[channel] = set()
            continue
        available = list(undecided)
        best = sorted((gains[k][channel] for k in available), reverse=True)[:slots]
        if current + sum(best) <= contamination[channel] + EPS:
            closures[channel] = None
            continue
        mandatory = set()
        for k in available:
            without = sorted((gains[j][channel] for j in available if j != k), reverse=True)[:slots]
            if current + sum(without) <= contamination[channel] + EPS:
                mandatory.add(k)
        closure = set()
        for k in mandatory:
            closure |= ancestors[k] | {k}
        closure -= set(included)
        closures[channel] = None if closure & set(excluded) or len(closure) > slots else closure
    return closures


def closure_masks(closures, frequencies):
    index = {k: i for i, k in enumerate(frequencies)}
    masks = []
    for closure in closures.values():
        if closure is None:
            continue
        mask = 0
        for k in closure:
            mask |= 1 << index[k]
        masks.append(mask)
    return masks


def exact_union_bound_and_forbidden_count(masks, slots):
    # DP by union mask; stores maximum channel count and multiplicity of subsets.
    dp = {0: (0, 1)}
    for mask in masks:
        next_dp = dict(dp)
        for union, (best, count) in dp.items():
            new_union = union | mask
            old_best, old_count = next_dp.get(new_union, (-1, 0))
            next_dp[new_union] = (max(old_best, best + 1), old_count + count)
        dp = next_dp
    upper = max(best for union, (best, _) in dp.items() if union.bit_count() <= slots)
    feasible_count = sum(count for union, (_, count) in dp.items() if union.bit_count() <= slots)
    return upper, (1 << len(masks)) - feasible_count


def minimal_forbidden_edges(masks, slots):
    # A minimal forbidden family has size at most slots+1: every member must
    # contribute a private closure element, while the union has size > slots.
    nonzero = [(i, mask) for i, mask in enumerate(masks) if mask]
    edges = []
    for size in range(2, min(slots + 1, len(nonzero)) + 1):
        for combination in itertools.combinations(nonzero, size):
            indices = tuple(i for i, _ in combination)
            selected_masks = [mask for _, mask in combination]
            union = 0
            for mask in selected_masks:
                union |= mask
            if union.bit_count() <= slots:
                continue
            minimal = True
            for dropped in range(size):
                reduced = 0
                for j, mask in enumerate(selected_masks):
                    if j != dropped:
                        reduced |= mask
                if reduced.bit_count() > slots:
                    minimal = False
                    break
            if minimal:
                edges.append(indices)
    return edges


def bound_from_minimal_edges(vertex_count, edges):
    edge_masks = [sum(1 << i for i in edge) for edge in edges]
    if not edge_masks:
        return vertex_count

    @functools.lru_cache(None)
    def solve(available):
        edge = next((e for e in edge_masks if e & available == e), None)
        if edge is None:
            return available.bit_count()
        best = 0
        remaining = edge
        while remaining:
            bit = remaining & -remaining
            best = max(best, solve(available ^ bit))
            remaining -= bit
        return best

    return solve((1 << vertex_count) - 1)


@dataclass
class Stats:
    visited_nodes: int = 0
    leaves: int = 0
    upper_bound_prunes: int = 0
    precedence_prunes: int = 0
    bound_calls: int = 0
    all_forbidden_families: int = 0
    minimal_forbidden_hyperedges: int = 0
    bound_equivalence_failures: int = 0
    edge_sizes: Counter = field(default_factory=Counter)


def search(frequencies, budget, lower_empty, gains, contamination, ancestors, descendants):
    best_value = -1
    best_set = ()
    stats = Stats()

    def propagate(included, excluded):
        new_included = set(included)
        new_excluded = set(excluded)
        for j in included:
            new_included |= ancestors[j]
        for i in excluded:
            new_excluded |= descendants[i]
        return new_included, new_excluded, bool(new_included & new_excluded)

    def score(k, included):
        cost = len((ancestors[k] | {k}) - included)
        return (sum(gains[k]) / cost, len(ancestors[k]) + len(descendants[k]), -cost, -k)

    def recurse(included, excluded):
        nonlocal best_value, best_set
        stats.visited_nodes += 1
        included, excluded, contradiction = propagate(included, excluded)
        if contradiction:
            stats.precedence_prunes += 1
            return
        undecided = [k for k in frequencies if k not in included and k not in excluded]
        slots = budget - len(included)
        if slots < 0 or len(undecided) < slots:
            stats.precedence_prunes += 1
            return

        closures = mandatory_closures(
            included, excluded, undecided, slots,
            lower_empty, gains, contamination, ancestors,
        )
        masks = closure_masks(closures, frequencies)
        exact_upper, forbidden_count = exact_union_bound_and_forbidden_count(masks, slots)
        minimal_edges = minimal_forbidden_edges(masks, slots)
        minimal_upper = bound_from_minimal_edges(len(masks), minimal_edges)
        stats.bound_calls += 1
        stats.all_forbidden_families += forbidden_count
        stats.minimal_forbidden_hyperedges += len(minimal_edges)
        stats.edge_sizes.update(map(len, minimal_edges))
        stats.bound_equivalence_failures += int(exact_upper != minimal_upper)

        if minimal_upper <= best_value:
            stats.upper_bound_prunes += 1
            return
        if slots == 0 or not undecided:
            stats.leaves += 1
            value = base.objective(included, lower_empty, gains, contamination)
            if value > best_value:
                best_value = value
                best_set = tuple(sorted(included))
            return
        frequency = max(undecided, key=lambda k: score(k, included))
        recurse(included | {frequency}, excluded)
        recurse(included, excluded | {frequency})

    recurse(set(), set())
    return best_value, best_set, stats


def exhaustive_optimum(frequencies, budget, lower_empty, gains, contamination):
    best_value = -1
    best_set = ()
    for selected in itertools.combinations(frequencies, budget):
        value = base.objective(selected, lower_empty, gains, contamination)
        if value > best_value:
            best_value, best_set = value, selected
    return best_value, best_set


def main():
    summary = Counter()
    edge_sizes = Counter()
    example = None
    largest_compression = -1

    for N in range(4, 121):
        for r in range(3, 31):
            q, frequencies, contamination, lower_empty, gains, prime_prime = base.build_instance(N, r)
            if len(frequencies) < 2:
                continue
            ancestors, descendants, _ = base.precedence_closure(frequencies, gains, q)
            for budget in range(0, min(4, len(frequencies)) + 1):
                summary["optimization_cases"] += 1
                exact_value, _ = exhaustive_optimum(frequencies, budget, lower_empty, gains, contamination)
                value, selected, stats = search(
                    frequencies, budget, lower_empty, gains, contamination, ancestors, descendants
                )
                summary["optimum_mismatches"] += int(value != exact_value)
                for channel in base.certified_channels(selected, lower_empty, gains, contamination):
                    summary["false_certificates"] += int(prime_prime[channel] <= EPS)
                for field_name in (
                    "visited_nodes", "leaves", "upper_bound_prunes", "precedence_prunes",
                    "bound_calls", "all_forbidden_families", "minimal_forbidden_hyperedges",
                    "bound_equivalence_failures",
                ):
                    summary[field_name] += getattr(stats, field_name)
                edge_sizes.update(stats.edge_sizes)
                compression = stats.all_forbidden_families - stats.minimal_forbidden_hyperedges
                if compression > largest_compression:
                    largest_compression = compression
                    example = {
                        "N": N, "r": r, "q": q, "budget": budget,
                        "optimum": exact_value, "selected": selected,
                        "all_forbidden_families": stats.all_forbidden_families,
                        "minimal_forbidden_hyperedges": stats.minimal_forbidden_hyperedges,
                        "minimal_edge_sizes": dict(stats.edge_sizes),
                        "visited_nodes": stats.visited_nodes,
                    }

    total = summary["all_forbidden_families"]
    minimal = summary["minimal_forbidden_hyperedges"]
    summary["representation_reduction_percent"] = 100.0 * (total - minimal) / total
    status = "PASS" if (
        summary["optimum_mismatches"] == 0
        and summary["false_certificates"] == 0
        and summary["bound_equivalence_failures"] == 0
    ) else "FAIL"
    result = {
        "schema": "pvg.minimal-forbidden-channel-hyperedges.v1.1",
        "status": status,
        "benchmark": {"N": [4, 120], "r": [3, 30], "max_exact_budget": 4},
        "summary": dict(summary),
        "minimal_hyperedge_size_distribution": {str(k): v for k, v in sorted(edge_sizes.items())},
        "largest_compression_example": example,
        "claims": {
            "exact_optimum_preserved": summary["optimum_mismatches"] == 0,
            "minimal_bound_equals_full_hypergraph_bound": summary["bound_equivalence_failures"] == 0,
            "polynomial_time_claim": False,
            "goldbach_proof_claim": False,
            "rh_or_grh_progress_claim": False,
        },
    }
    output = HERE.parent / "results" / "minimal_forbidden_channel_hyperedges_verification_v1.1.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
