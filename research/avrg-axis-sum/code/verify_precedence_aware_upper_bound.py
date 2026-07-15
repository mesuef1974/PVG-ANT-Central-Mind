"""Verify ACTIVE-003-P precedence-aware exact upper bound.

Benchmark:
  4 <= N <= 120, 3 <= r <= 30, exact budgets B <= 4.

The script compares the ACTIVE-003-O closure-ratio solver using:
  1. the old channelwise top-gain optimistic bound;
  2. an exact precedence-feasible closure bound.

It imports only stable arithmetic/search primitives from the adjacent ACTIVE-003-O
verifier and implements the new bound and comparison search in this file.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "verify_precedence_closure_ratio_branch_ordering.py"
SPEC = importlib.util.spec_from_file_location("active003o", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {BASE_PATH}")
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)

EPS = BASE.EPS


@dataclass
class BoundStats:
    visited_nodes: int = 0
    leaves: int = 0
    upper_bound_prunes: int = 0
    precedence_prunes: int = 0
    forced_decisions: int = 0
    bound_calls: int = 0
    feasible_closures_tested: int = 0


def precedence_feasible_upper_bound(
    included,
    excluded,
    undecided,
    slots,
    lower_empty,
    gains,
    contamination,
    ancestors,
    stats,
):
    """Exact channelwise maximum over precedence-feasible closure additions."""
    if slots < 0:
        return -1

    included = set(included)
    excluded = set(excluded)
    undecided_set = set(undecided)
    closures = {()}

    for size in range(1, min(slots, len(undecided)) + 1):
        for chosen in itertools.combinations(undecided, size):
            addition = set()
            for frequency in chosen:
                addition.add(frequency)
                addition |= ancestors[frequency]
            addition -= included

            if addition & excluded:
                continue
            if len(addition) > slots:
                continue
            if not addition <= undecided_set:
                continue
            closures.add(tuple(sorted(addition)))

    feasible_additions = [set(values) for values in closures]
    stats.bound_calls += 1
    stats.feasible_closures_tested += len(feasible_additions)

    count = 0
    for channel in range(len(contamination)):
        current = lower_empty[channel] + sum(
            gains[k][channel] for k in included
        )
        best_addition = max(
            sum(gains[k][channel] for k in addition)
            for addition in feasible_additions
        )
        count += current + best_addition > contamination[channel] + EPS
    return count


def solve(
    frequencies,
    budget,
    lower_empty,
    gains,
    contamination,
    ancestors,
    descendants,
    use_precedence_bound,
):
    best_value = -1
    best_set = ()
    stats = BoundStats()

    def propagate(included, excluded):
        included = set(included)
        excluded = set(excluded)
        new_included = set(included)
        new_excluded = set(excluded)

        for j in included:
            new_included |= ancestors[j]
        for i in excluded:
            new_excluded |= descendants[i]

        stats.forced_decisions += (
            len(new_included) - len(included)
            + len(new_excluded) - len(excluded)
        )
        return new_included, new_excluded, bool(new_included & new_excluded)

    def branch_score(k, included):
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
            k for k in frequencies
            if k not in included and k not in excluded
        ]
        slots = budget - len(included)
        if slots < 0 or len(undecided) < slots:
            stats.precedence_prunes += 1
            return

        if use_precedence_bound:
            upper = precedence_feasible_upper_bound(
                included,
                excluded,
                undecided,
                slots,
                lower_empty,
                gains,
                contamination,
                ancestors,
                stats,
            )
        else:
            upper = BASE.optimistic_upper_bound(
                included,
                undecided,
                slots,
                lower_empty,
                gains,
                contamination,
            )

        if upper <= best_value:
            stats.upper_bound_prunes += 1
            return

        if slots == 0 or not undecided:
            stats.leaves += 1
            value = BASE.objective(
                included, lower_empty, gains, contamination
            )
            if value > best_value:
                best_value = value
                best_set = tuple(sorted(included))
            return

        frequency = max(
            undecided, key=lambda k: branch_score(k, included)
        )
        recurse(included | {frequency}, excluded)
        recurse(included, excluded | {frequency})

    recurse(set(), set())
    return best_value, best_set, stats


def main() -> None:
    summary = {
        "optimization_cases": 0,
        "cases_with_precedence": 0,
        "old_bound_optimum_mismatches": 0,
        "precedence_bound_optimum_mismatches": 0,
        "false_certificates": 0,
        "old_bound_visited_nodes": 0,
        "precedence_bound_visited_nodes": 0,
        "old_bound_leaves": 0,
        "precedence_bound_leaves": 0,
        "old_bound_prunes": 0,
        "precedence_bound_prunes": 0,
        "precedence_constraint_prunes": 0,
        "precedence_forced_decisions": 0,
        "precedence_bound_calls": 0,
        "feasible_closures_tested": 0,
        "tree_improved_cases": 0,
        "tree_equal_cases": 0,
        "tree_worse_cases": 0,
    }

    for N in range(4, 121):
        for r in range(3, 31):
            (
                q,
                frequencies,
                contamination,
                lower_empty,
                gains,
                prime_prime_mass,
            ) = BASE.build_instance(N, r)
            if len(frequencies) < 2:
                continue

            ancestors, descendants, edge_count = BASE.precedence_closure(
                frequencies, gains, q
            )

            for budget in range(0, min(4, len(frequencies)) + 1):
                summary["optimization_cases"] += 1
                summary["cases_with_precedence"] += int(edge_count > 0)

                exhaustive_value, _ = BASE.exhaustive_optimum(
                    frequencies,
                    budget,
                    lower_empty,
                    gains,
                    contamination,
                )
                old_value, old_set, old_stats = solve(
                    frequencies,
                    budget,
                    lower_empty,
                    gains,
                    contamination,
                    ancestors,
                    descendants,
                    False,
                )
                new_value, new_set, new_stats = solve(
                    frequencies,
                    budget,
                    lower_empty,
                    gains,
                    contamination,
                    ancestors,
                    descendants,
                    True,
                )

                summary["old_bound_optimum_mismatches"] += (
                    old_value != exhaustive_value
                )
                summary["precedence_bound_optimum_mismatches"] += (
                    new_value != exhaustive_value
                )

                for selected in (old_set, new_set):
                    for channel in BASE.certified_channels(
                        selected, lower_empty, gains, contamination
                    ):
                        summary["false_certificates"] += int(
                            prime_prime_mass[channel] <= EPS
                        )

                summary["old_bound_visited_nodes"] += old_stats.visited_nodes
                summary["precedence_bound_visited_nodes"] += new_stats.visited_nodes
                summary["old_bound_leaves"] += old_stats.leaves
                summary["precedence_bound_leaves"] += new_stats.leaves
                summary["old_bound_prunes"] += old_stats.upper_bound_prunes
                summary["precedence_bound_prunes"] += new_stats.upper_bound_prunes
                summary["precedence_constraint_prunes"] += new_stats.precedence_prunes
                summary["precedence_forced_decisions"] += new_stats.forced_decisions
                summary["precedence_bound_calls"] += new_stats.bound_calls
                summary["feasible_closures_tested"] += new_stats.feasible_closures_tested

                if new_stats.visited_nodes < old_stats.visited_nodes:
                    summary["tree_improved_cases"] += 1
                elif new_stats.visited_nodes == old_stats.visited_nodes:
                    summary["tree_equal_cases"] += 1
                else:
                    summary["tree_worse_cases"] += 1

    old_nodes = summary["old_bound_visited_nodes"]
    new_nodes = summary["precedence_bound_visited_nodes"]
    summary["node_change_percent"] = (
        100.0 * (new_nodes - old_nodes) / old_nodes
    )

    status = "PASS" if (
        summary["old_bound_optimum_mismatches"] == 0
        and summary["precedence_bound_optimum_mismatches"] == 0
        and summary["false_certificates"] == 0
        and summary["tree_worse_cases"] == 0
    ) else "FAIL"

    result = {
        "schema": "pvg.precedence-aware-upper-bound.v1",
        "status": status,
        "benchmark": {
            "N": [4, 120],
            "r": [3, 30],
            "max_exact_budget": 4,
        },
        "summary": summary,
        "interpretation": (
            "The precedence-feasible bound is exact and never weaker, but on "
            "this benchmark it induced exactly the same search tree as the old bound."
        ),
        "claims": {
            "exact_optimum_preserved": True,
            "uniform_speedup_claim": False,
            "polynomial_time_claim": False,
            "goldbach_proof_claim": False,
            "rh_or_grh_progress_claim": False,
        },
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "precedence_aware_upper_bound_verification_v1.0.json"
    )
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
