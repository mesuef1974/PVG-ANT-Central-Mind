"""Verify ACTIVE-003-R hypergraph compatibility certification.

Benchmark: 4 <= N <= 120, 3 <= r <= 30, exact budgets B <= 4.
Compares the ACTIVE-003-Q pairwise compatibility upper bound with an exact
higher-order mandatory-closure union bound. Both searches remain exponential.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
from dataclasses import dataclass
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
    q = len(contamination)
    for c in range(q):
        current = lower_empty[c] + sum(gains[k][c] for k in included)
        if current > contamination[c] + EPS:
            closures[c] = set()
            continue
        available = list(undecided)
        best = sorted((gains[k][c] for k in available), reverse=True)[:slots]
        if current + sum(best) <= contamination[c] + EPS:
            closures[c] = None
            continue
        mandatory = set()
        for k in available:
            without = sorted(
                (gains[j][c] for j in available if j != k), reverse=True
            )[:slots]
            if current + sum(without) <= contamination[c] + EPS:
                mandatory.add(k)
        closure = set()
        for k in mandatory:
            closure |= ancestors[k] | {k}
        closure -= set(included)
        if closure & set(excluded) or len(closure) > slots:
            closures[c] = None
        else:
            closures[c] = closure
    return closures


def pairwise_bound(closures, slots):
    feasible = [c for c, closure in closures.items() if closure is not None]
    best = 0
    for size in range(1, len(feasible) + 1):
        for channels in itertools.combinations(feasible, size):
            if all(
                len(closures[a] | closures[b]) <= slots
                for a, b in itertools.combinations(channels, 2)
            ):
                best = size
    return best


def hypergraph_bound(closures, slots):
    feasible = [c for c, closure in closures.items() if closure is not None]
    best = 0
    for size in range(1, len(feasible) + 1):
        for channels in itertools.combinations(feasible, size):
            union = set()
            for c in channels:
                union |= closures[c]
            if len(union) <= slots:
                best = size
    return best


@dataclass
class Stats:
    visited_nodes: int = 0
    leaves: int = 0
    upper_bound_prunes: int = 0
    precedence_prunes: int = 0
    strict_hypergraph_tightenings: int = 0


def search(frequencies, budget, lower_empty, gains, contamination, ancestors, descendants, bound_kind):
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
        closure_cost = len((ancestors[k] | {k}) - included)
        return (
            sum(gains[k]) / closure_cost,
            len(ancestors[k]) + len(descendants[k]),
            -closure_cost,
            -k,
        )

    def recurse(included, excluded):
        nonlocal best_value, best_set
        stats.visited_nodes += 1
        included, excluded, contradiction = propagate(included, excluded)
        if contradiction:
            stats.precedence_prunes += 1
            return
        undecided = [
            k for k in frequencies if k not in included and k not in excluded
        ]
        slots = budget - len(included)
        if slots < 0 or len(undecided) < slots:
            stats.precedence_prunes += 1
            return

        closures = mandatory_closures(
            included, excluded, undecided, slots,
            lower_empty, gains, contamination, ancestors,
        )
        pair_upper = pairwise_bound(closures, slots)
        if bound_kind == "pairwise":
            upper = pair_upper
        elif bound_kind == "hypergraph":
            upper = hypergraph_bound(closures, slots)
            stats.strict_hypergraph_tightenings += int(upper < pair_upper)
        else:
            raise ValueError(bound_kind)

        if upper <= best_value:
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
            best_value = value
            best_set = selected
    return best_value, best_set


def main():
    summary = {
        "optimization_cases": 0,
        "pairwise_optimum_mismatches": 0,
        "hypergraph_optimum_mismatches": 0,
        "false_certificates": 0,
        "pairwise_visited_nodes": 0,
        "hypergraph_visited_nodes": 0,
        "pairwise_leaves": 0,
        "hypergraph_leaves": 0,
        "strict_hypergraph_tightenings": 0,
        "improved_cases": 0,
        "equal_cases": 0,
        "worse_cases": 0,
    }
    example = None
    largest_reduction = 0

    for N in range(4, 121):
        for r in range(3, 31):
            q, frequencies, contamination, lower_empty, gains, prime_prime = base.build_instance(N, r)
            if len(frequencies) < 2:
                continue
            ancestors, descendants, _ = base.precedence_closure(frequencies, gains, q)
            for budget in range(0, min(4, len(frequencies)) + 1):
                summary["optimization_cases"] += 1
                exact, _ = exhaustive_optimum(frequencies, budget, lower_empty, gains, contamination)
                pair_value, pair_set, pair_stats = search(
                    frequencies, budget, lower_empty, gains, contamination,
                    ancestors, descendants, "pairwise",
                )
                hyper_value, hyper_set, hyper_stats = search(
                    frequencies, budget, lower_empty, gains, contamination,
                    ancestors, descendants, "hypergraph",
                )
                summary["pairwise_optimum_mismatches"] += int(pair_value != exact)
                summary["hypergraph_optimum_mismatches"] += int(hyper_value != exact)
                for selected in (pair_set, hyper_set):
                    for channel in base.certified_channels(selected, lower_empty, gains, contamination):
                        summary["false_certificates"] += int(prime_prime[channel] <= EPS)
                summary["pairwise_visited_nodes"] += pair_stats.visited_nodes
                summary["hypergraph_visited_nodes"] += hyper_stats.visited_nodes
                summary["pairwise_leaves"] += pair_stats.leaves
                summary["hypergraph_leaves"] += hyper_stats.leaves
                summary["strict_hypergraph_tightenings"] += hyper_stats.strict_hypergraph_tightenings
                reduction = pair_stats.visited_nodes - hyper_stats.visited_nodes
                if reduction > 0:
                    summary["improved_cases"] += 1
                elif reduction == 0:
                    summary["equal_cases"] += 1
                else:
                    summary["worse_cases"] += 1
                if reduction > largest_reduction:
                    largest_reduction = reduction
                    example = {
                        "N": N, "r": r, "q": q, "budget": budget,
                        "optimum": exact,
                        "pairwise": {"selected": pair_set, "visited_nodes": pair_stats.visited_nodes, "leaves": pair_stats.leaves},
                        "hypergraph": {"selected": hyper_set, "visited_nodes": hyper_stats.visited_nodes, "leaves": hyper_stats.leaves},
                        "node_reduction": reduction,
                    }

    summary["aggregate_node_change_percent"] = 100.0 * (
        summary["hypergraph_visited_nodes"] - summary["pairwise_visited_nodes"]
    ) / summary["pairwise_visited_nodes"]
    status = "PASS" if (
        summary["pairwise_optimum_mismatches"] == 0
        and summary["hypergraph_optimum_mismatches"] == 0
        and summary["false_certificates"] == 0
    ) else "FAIL"
    result = {
        "schema": "pvg.hypergraph-compatibility-certification.v1",
        "status": status,
        "benchmark": {"N": [4, 120], "r": [3, 30], "max_exact_budget": 4},
        "summary": summary,
        "explicit_improvement_example": example,
        "claims": {
            "exact_optimum_preserved": summary["hypergraph_optimum_mismatches"] == 0,
            "uniform_speedup_claim": False,
            "polynomial_time_claim": False,
            "goldbach_proof_claim": False,
            "rh_or_grh_progress_claim": False,
        },
    }
    output = HERE.parent / "results" / "hypergraph_compatibility_certification_v1.0.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
