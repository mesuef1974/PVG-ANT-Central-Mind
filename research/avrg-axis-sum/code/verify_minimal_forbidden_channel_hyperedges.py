"""Verify ACTIVE-003-S minimal forbidden channel hyperedges.

Benchmark: 4 <= N <= 120, 3 <= r <= 30, exact budgets B <= 4.
The verifier imports ACTIVE-003-R, extracts the inclusion-minimal forbidden
channel hyperedges at every visited node, and checks that they reproduce the
full higher-order compatibility bound exactly.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "verify_hypergraph_compatibility_certification.py"
spec = importlib.util.spec_from_file_location("active003r", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

EPS = base.EPS


def feasible_channels(closures):
    return [c for c, closure in closures.items() if closure is not None]


def union_cost(channels, closures):
    union = set()
    for c in channels:
        union |= closures[c]
    return len(union)


def all_forbidden_families(closures, slots):
    channels = feasible_channels(closures)
    forbidden = []
    for size in range(1, len(channels) + 1):
        for family in itertools.combinations(channels, size):
            if union_cost(family, closures) > slots:
                forbidden.append(frozenset(family))
    return forbidden


def minimal_forbidden_families(closures, slots):
    channels = feasible_channels(closures)
    minimal = []
    for size in range(1, len(channels) + 1):
        for family_tuple in itertools.combinations(channels, size):
            family = frozenset(family_tuple)
            if any(edge <= family for edge in minimal):
                continue
            if union_cost(family, closures) > slots:
                minimal.append(family)
    return minimal


def bound_from_minimal_cuts(closures, minimal_edges):
    channels = feasible_channels(closures)
    best = 0
    for size in range(0, len(channels) + 1):
        for family_tuple in itertools.combinations(channels, size):
            family = frozenset(family_tuple)
            if not any(edge <= family for edge in minimal_edges):
                best = size
    return best


def audit_minimal_family(closures, slots, forbidden, minimal):
    forbidden_set = set(forbidden)
    minimality_failures = 0
    coverage_failures = 0
    forbidden_failures = 0

    for edge in minimal:
        if union_cost(edge, closures) <= slots:
            forbidden_failures += 1
        for c in edge:
            if union_cost(edge - {c}, closures) > slots:
                minimality_failures += 1

    for family in forbidden_set:
        if not any(edge <= family for edge in minimal):
            coverage_failures += 1

    return forbidden_failures, minimality_failures, coverage_failures


@dataclass
class Stats:
    visited_nodes: int = 0
    leaves: int = 0
    upper_bound_prunes: int = 0
    precedence_prunes: int = 0
    bound_mismatches: int = 0
    forbidden_failures: int = 0
    minimality_failures: int = 0
    coverage_failures: int = 0
    all_forbidden_count: int = 0
    minimal_forbidden_count: int = 0


def search(freqs, budget, lower_empty, gains, contamination, ancestors, descendants, histogram):
    best_value = -1
    best_set = ()
    stats = Stats()
    compression_example = None

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
        return (
            sum(gains[k]) / cost,
            len(ancestors[k]) + len(descendants[k]),
            -cost,
            -k,
        )

    def recurse(included, excluded):
        nonlocal best_value, best_set, compression_example
        stats.visited_nodes += 1
        included, excluded, contradiction = propagate(included, excluded)
        if contradiction:
            stats.precedence_prunes += 1
            return

        undecided = [k for k in freqs if k not in included and k not in excluded]
        slots = budget - len(included)
        if slots < 0 or len(undecided) < slots:
            stats.precedence_prunes += 1
            return

        closures = base.mandatory_closures(
            included, excluded, undecided, slots,
            lower_empty, gains, contamination, ancestors,
        )
        full_bound = base.hypergraph_bound(closures, slots)
        forbidden = all_forbidden_families(closures, slots)
        minimal = minimal_forbidden_families(closures, slots)
        cut_bound = bound_from_minimal_cuts(closures, minimal)

        stats.all_forbidden_count += len(forbidden)
        stats.minimal_forbidden_count += len(minimal)
        for edge in minimal:
            histogram[len(edge)] += 1

        ff, mf, cf = audit_minimal_family(
            closures, slots, forbidden, minimal
        )
        stats.forbidden_failures += ff
        stats.minimality_failures += mf
        stats.coverage_failures += cf
        stats.bound_mismatches += int(full_bound != cut_bound)

        if (
            compression_example is None
            and len(forbidden) > len(minimal)
            and len(forbidden) >= 4
        ):
            compression_example = {
                "included": sorted(included),
                "excluded": sorted(excluded),
                "slots": slots,
                "feasible_channels": feasible_channels(closures),
                "all_forbidden_count": len(forbidden),
                "minimal_forbidden_count": len(minimal),
                "minimal_edges": [sorted(edge) for edge in minimal],
                "full_bound": full_bound,
                "minimal_cut_bound": cut_bound,
            }

        if cut_bound <= best_value:
            stats.upper_bound_prunes += 1
            return
        if slots == 0 or not undecided:
            stats.leaves += 1
            value = base.base.objective(
                included, lower_empty, gains, contamination
            )
            if value > best_value:
                best_value = value
                best_set = tuple(sorted(included))
            return

        frequency = max(undecided, key=lambda k: score(k, included))
        recurse(included | {frequency}, excluded)
        recurse(included, excluded | {frequency})

    recurse(set(), set())
    return best_value, best_set, stats, compression_example


def exhaustive_optimum(freqs, budget, lower_empty, gains, contamination):
    best = -1
    best_set = ()
    for selected in itertools.combinations(freqs, budget):
        value = base.base.objective(selected, lower_empty, gains, contamination)
        if value > best:
            best = value
            best_set = selected
    return best, best_set


def main():
    summary = {
        "optimization_cases": 0,
        "optimum_mismatches": 0,
        "false_certificates": 0,
        "visited_nodes": 0,
        "leaves": 0,
        "upper_bound_prunes": 0,
        "precedence_prunes": 0,
        "bound_mismatches": 0,
        "forbidden_failures": 0,
        "minimality_failures": 0,
        "coverage_failures": 0,
        "all_forbidden_families": 0,
        "minimal_forbidden_families": 0,
    }
    histogram = Counter()
    explicit_example = None

    for N in range(4, 121):
        for r in range(3, 31):
            q, freqs, contamination, lower_empty, gains, prime_prime = (
                base.base.build_instance(N, r)
            )
            if len(freqs) < 2:
                continue
            ancestors, descendants, _ = base.base.precedence_closure(
                freqs, gains, q
            )
            for budget in range(0, min(4, len(freqs)) + 1):
                summary["optimization_cases"] += 1
                exact, _ = exhaustive_optimum(
                    freqs, budget, lower_empty, gains, contamination
                )
                value, selected, stats, example = search(
                    freqs, budget, lower_empty, gains, contamination,
                    ancestors, descendants, histogram,
                )
                summary["optimum_mismatches"] += int(value != exact)
                for c in base.base.certified_channels(
                    selected, lower_empty, gains, contamination
                ):
                    summary["false_certificates"] += int(
                        prime_prime[c] <= EPS
                    )
                summary["visited_nodes"] += stats.visited_nodes
                summary["leaves"] += stats.leaves
                summary["upper_bound_prunes"] += stats.upper_bound_prunes
                summary["precedence_prunes"] += stats.precedence_prunes
                summary["bound_mismatches"] += stats.bound_mismatches
                summary["forbidden_failures"] += stats.forbidden_failures
                summary["minimality_failures"] += stats.minimality_failures
                summary["coverage_failures"] += stats.coverage_failures
                summary["all_forbidden_families"] += stats.all_forbidden_count
                summary["minimal_forbidden_families"] += stats.minimal_forbidden_count
                if example is not None and explicit_example is None:
                    explicit_example = {
                        "N": N,
                        "r": r,
                        "q": q,
                        "budget": budget,
                        **example,
                    }

    all_count = summary["all_forbidden_families"]
    minimal_count = summary["minimal_forbidden_families"]
    summary["representation_reduction_percent"] = (
        100.0 * (all_count - minimal_count) / all_count
        if all_count else 0.0
    )
    summary["minimal_hyperedge_size_histogram"] = {
        str(size): count for size, count in sorted(histogram.items())
    }

    status = "PASS" if all(
        summary[key] == 0
        for key in (
            "optimum_mismatches",
            "false_certificates",
            "bound_mismatches",
            "forbidden_failures",
            "minimality_failures",
            "coverage_failures",
        )
    ) else "FAIL"

    result = {
        "schema": "pvg.minimal-forbidden-channel-hyperedges.v1",
        "status": status,
        "benchmark": {"N": [4, 120], "r": [3, 30], "max_exact_budget": 4},
        "summary": summary,
        "explicit_representation_compression_example": explicit_example,
        "claims": {
            "hypergraph_bound_preserved": summary["bound_mismatches"] == 0,
            "exact_optimum_preserved": summary["optimum_mismatches"] == 0,
            "runtime_speedup_claim": False,
            "polynomial_time_claim": False,
            "goldbach_proof_claim": False,
            "rh_or_grh_progress_claim": False,
        },
    }

    output = HERE.parent / "results" / "minimal_forbidden_channel_hyperedges_verification_v1.0.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
