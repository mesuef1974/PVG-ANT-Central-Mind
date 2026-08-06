"""Verify ACTIVE-003-O precedence-closure-ratio branch ordering.

Benchmark:
  4 <= N <= 120, 3 <= r <= 30, exact budgets B <= 4.

The verifier compares:
  1. ordinary exact branch-and-bound;
  2. ACTIVE-003-N baseline precedence-aware branch-and-bound;
  3. closure-ratio precedence-aware branch-and-bound.

It independently reconstructs prime-prime channel mass and rejects any false
certificate. The closure-ratio rule changes branching order only; all solvers
remain exact exponential algorithms.
"""

from __future__ import annotations

import cmath
import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path

EPS = 1e-10
STRICT_EPS = 1e-8


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            x = n
            while x % p == 0:
                x //= p
            return math.log(p) if x == 1 else 0.0
    return math.log(n)


def build_instance(N: int, r: int):
    g = math.gcd(2, r)
    q = r // g
    u = 2 // g

    reduced_mass = [0.0] * q
    higher_prime_power_mass = [0.0] * q
    prime_prime_mass = [0.0] * q

    for a in range(1, N):
        la = von_mangoldt(a)
        lb = von_mangoldt(N - a)
        channel = (u * a) % q
        reduced_mass[channel] += la * lb
        if is_prime(a) and is_prime(N - a):
            prime_prime_mass[channel] += la * lb
        if la > 0.0 and not is_prime(a):
            higher_prime_power_mass[channel] += la

    contamination = [
        math.log(N)
        * (
            higher_prime_power_mass[c]
            + higher_prime_power_mass[(u * N - c) % q]
        )
        for c in range(q)
    ]

    fourier = [
        sum(
            reduced_mass[c] * cmath.exp(2j * math.pi * k * c / q)
            for c in range(q)
        )
        for k in range(q)
    ]

    frequencies = list(range(1, (q - 1) // 2 + 1))
    base = [sum(reduced_mass) / q] * q

    if q % 2 == 0:
        nyquist = fourier[q // 2].real / q
        base = [base[c] + nyquist * ((-1) ** c) for c in range(q)]

    contributions = {
        k: [
            (2.0 / q)
            * (
                fourier[k]
                * cmath.exp(-2j * math.pi * k * c / q)
            ).real
            for c in range(q)
        ]
        for k in frequencies
    }

    gains = {
        k: [value + abs(value) for value in contributions[k]]
        for k in frequencies
    }

    lower_empty = [
        base[c]
        - sum(abs(contributions[k][c]) for k in frequencies)
        for c in range(q)
    ]

    return (
        q,
        frequencies,
        contamination,
        lower_empty,
        gains,
        prime_prime_mass,
    )


def objective(selected, lower_empty, gains, contamination) -> int:
    return sum(
        lower_empty[c] + sum(gains[k][c] for k in selected)
        > contamination[c] + EPS
        for c in range(len(contamination))
    )


def certified_channels(selected, lower_empty, gains, contamination):
    return [
        c
        for c in range(len(contamination))
        if lower_empty[c] + sum(gains[k][c] for k in selected)
        > contamination[c] + EPS
    ]


def precedence_closure(frequencies, gains, q):
    """Build an acyclic canonical dominance relation and its closure.

    Strict dominance is retained. Exact equal-gain classes are oriented from
    smaller to larger frequency index so that a canonical optimum exists
    without introducing two-cycles.
    """

    descendants = {k: set() for k in frequencies}

    for i, j in itertools.permutations(frequencies, 2):
        weakly_dominates = all(
            gains[i][c] >= gains[j][c] - EPS for c in range(q)
        )
        strictly_dominates = any(
            gains[i][c] > gains[j][c] + STRICT_EPS for c in range(q)
        )
        equal_gain = all(
            abs(gains[i][c] - gains[j][c]) <= EPS for c in range(q)
        )
        if weakly_dominates and (
            strictly_dominates or (equal_gain and i < j)
        ):
            descendants[i].add(j)

    changed = True
    while changed:
        changed = False
        for i in frequencies:
            implied = set()
            for j in list(descendants[i]):
                implied |= descendants[j]
            old_size = len(descendants[i])
            descendants[i] |= implied
            changed |= len(descendants[i]) != old_size

    ancestors = {k: set() for k in frequencies}
    for i in frequencies:
        for j in descendants[i]:
            ancestors[j].add(i)

    edge_count = sum(len(values) for values in descendants.values())
    return ancestors, descendants, edge_count


def optimistic_upper_bound(
    included,
    undecided,
    slots,
    lower_empty,
    gains,
    contamination,
) -> int:
    if slots < 0:
        return -1

    count = 0
    for c in range(len(contamination)):
        value = lower_empty[c] + sum(gains[k][c] for k in included)
        available = sorted(
            (gains[k][c] for k in undecided), reverse=True
        )
        value += sum(available[:slots])
        if value > contamination[c] + EPS:
            count += 1
    return count


@dataclass
class SearchStats:
    visited_nodes: int = 0
    leaves: int = 0
    upper_bound_prunes: int = 0
    precedence_prunes: int = 0
    infeasible_prunes: int = 0
    forced_decisions: int = 0


def ordinary_branch_and_bound(
    frequencies,
    budget,
    lower_empty,
    gains,
    contamination,
):
    best_value = -1
    best_set = ()
    stats = SearchStats()
    order = sorted(
        frequencies,
        key=lambda k: (sum(gains[k]), -k),
        reverse=True,
    )

    def recurse(position, included):
        nonlocal best_value, best_set
        stats.visited_nodes += 1
        slots = budget - len(included)
        remaining = order[position:]

        if slots < 0 or len(remaining) < slots:
            stats.infeasible_prunes += 1
            return

        upper = optimistic_upper_bound(
            included,
            remaining,
            slots,
            lower_empty,
            gains,
            contamination,
        )
        if upper <= best_value:
            stats.upper_bound_prunes += 1
            return

        if position == len(order) or slots == 0:
            stats.leaves += 1
            value = objective(
                included, lower_empty, gains, contamination
            )
            if value > best_value:
                best_value = value
                best_set = tuple(sorted(included))
            return

        frequency = order[position]
        recurse(position + 1, included | {frequency})
        recurse(position + 1, included)

    recurse(0, set())
    return best_value, best_set, stats


def precedence_branch_and_bound(
    frequencies,
    budget,
    lower_empty,
    gains,
    contamination,
    ancestors,
    descendants,
    ordering,
):
    best_value = -1
    best_set = ()
    stats = SearchStats()

    def propagate(included, excluded):
        included = set(included)
        excluded = set(excluded)

        new_included = set(included)
        for j in included:
            new_included |= ancestors[j]

        new_excluded = set(excluded)
        for i in excluded:
            new_excluded |= descendants[i]

        stats.forced_decisions += (
            len(new_included)
            - len(included)
            + len(new_excluded)
            - len(excluded)
        )

        if new_included & new_excluded:
            return None, None, True
        return new_included, new_excluded, False

    def baseline_score(k):
        return (
            len(descendants[k]),
            len(ancestors[k]),
            sum(gains[k]),
            -k,
        )

    def closure_ratio_score(k, included):
        forced_inclusion = (
            ancestors[k] | {k}
        ) - included
        closure_cost = len(forced_inclusion)
        ratio = sum(gains[k]) / closure_cost
        return (
            ratio,
            len(ancestors[k]) + len(descendants[k]),
            -closure_cost,
            -k,
        )

    def recurse(included, excluded):
        nonlocal best_value, best_set
        stats.visited_nodes += 1

        included, excluded, contradiction = propagate(
            included, excluded
        )
        if contradiction:
            stats.precedence_prunes += 1
            return

        undecided = [
            k
            for k in frequencies
            if k not in included and k not in excluded
        ]
        slots = budget - len(included)

        if slots < 0 or len(undecided) < slots:
            stats.precedence_prunes += 1
            return

        upper = optimistic_upper_bound(
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
            value = objective(
                included, lower_empty, gains, contamination
            )
            if value > best_value:
                best_value = value
                best_set = tuple(sorted(included))
            return

        if ordering == "baseline":
            frequency = max(undecided, key=baseline_score)
        elif ordering == "closure_ratio":
            frequency = max(
                undecided,
                key=lambda k: closure_ratio_score(k, included),
            )
        else:
            raise ValueError(f"unknown ordering: {ordering}")

        recurse(included | {frequency}, excluded)
        recurse(included, excluded | {frequency})

    recurse(set(), set())
    return best_value, best_set, stats


def exhaustive_optimum(
    frequencies,
    budget,
    lower_empty,
    gains,
    contamination,
):
    best_value = -1
    best_set = ()
    for selected in itertools.combinations(frequencies, budget):
        value = objective(
            selected, lower_empty, gains, contamination
        )
        if value > best_value:
            best_value = value
            best_set = selected
    return best_value, best_set


def empty_summary():
    return {
        "optimization_cases": 0,
        "cases_with_precedence": 0,
        "ordinary_optimum_mismatches": 0,
        "baseline_optimum_mismatches": 0,
        "closure_ratio_optimum_mismatches": 0,
        "false_certificates": 0,
        "ordinary_visited_nodes": 0,
        "baseline_precedence_visited_nodes": 0,
        "closure_ratio_visited_nodes": 0,
        "ordinary_leaves": 0,
        "baseline_precedence_leaves": 0,
        "closure_ratio_leaves": 0,
        "ordinary_upper_bound_prunes": 0,
        "baseline_upper_bound_prunes": 0,
        "closure_ratio_upper_bound_prunes": 0,
        "baseline_precedence_prunes": 0,
        "closure_ratio_precedence_prunes": 0,
        "baseline_forced_decisions": 0,
        "closure_ratio_forced_decisions": 0,
        "closure_ratio_improved_cases": 0,
        "closure_ratio_equal_cases": 0,
        "closure_ratio_worse_cases": 0,
    }


def main() -> None:
    summary = empty_summary()
    explicit_example = None
    largest_reduction = -1

    for N in range(4, 121):
        for r in range(3, 31):
            (
                q,
                frequencies,
                contamination,
                lower_empty,
                gains,
                prime_prime_mass,
            ) = build_instance(N, r)

            if len(frequencies) < 2:
                continue

            ancestors, descendants, edge_count = precedence_closure(
                frequencies, gains, q
            )

            for budget in range(
                0, min(4, len(frequencies)) + 1
            ):
                summary["optimization_cases"] += 1
                summary["cases_with_precedence"] += int(
                    edge_count > 0
                )

                exhaustive_value, _ = exhaustive_optimum(
                    frequencies,
                    budget,
                    lower_empty,
                    gains,
                    contamination,
                )

                ordinary_value, ordinary_set, ordinary_stats = (
                    ordinary_branch_and_bound(
                        frequencies,
                        budget,
                        lower_empty,
                        gains,
                        contamination,
                    )
                )

                baseline_value, baseline_set, baseline_stats = (
                    precedence_branch_and_bound(
                        frequencies,
                        budget,
                        lower_empty,
                        gains,
                        contamination,
                        ancestors,
                        descendants,
                        "baseline",
                    )
                )

                ratio_value, ratio_set, ratio_stats = (
                    precedence_branch_and_bound(
                        frequencies,
                        budget,
                        lower_empty,
                        gains,
                        contamination,
                        ancestors,
                        descendants,
                        "closure_ratio",
                    )
                )

                summary["ordinary_optimum_mismatches"] += (
                    ordinary_value != exhaustive_value
                )
                summary["baseline_optimum_mismatches"] += (
                    baseline_value != exhaustive_value
                )
                summary["closure_ratio_optimum_mismatches"] += (
                    ratio_value != exhaustive_value
                )

                for selected in (
                    ordinary_set,
                    baseline_set,
                    ratio_set,
                ):
                    for channel in certified_channels(
                        selected,
                        lower_empty,
                        gains,
                        contamination,
                    ):
                        summary["false_certificates"] += int(
                            prime_prime_mass[channel] <= EPS
                        )

                summary["ordinary_visited_nodes"] += (
                    ordinary_stats.visited_nodes
                )
                summary["baseline_precedence_visited_nodes"] += (
                    baseline_stats.visited_nodes
                )
                summary["closure_ratio_visited_nodes"] += (
                    ratio_stats.visited_nodes
                )
                summary["ordinary_leaves"] += ordinary_stats.leaves
                summary["baseline_precedence_leaves"] += (
                    baseline_stats.leaves
                )
                summary["closure_ratio_leaves"] += ratio_stats.leaves
                summary["ordinary_upper_bound_prunes"] += (
                    ordinary_stats.upper_bound_prunes
                )
                summary["baseline_upper_bound_prunes"] += (
                    baseline_stats.upper_bound_prunes
                )
                summary["closure_ratio_upper_bound_prunes"] += (
                    ratio_stats.upper_bound_prunes
                )
                summary["baseline_precedence_prunes"] += (
                    baseline_stats.precedence_prunes
                )
                summary["closure_ratio_precedence_prunes"] += (
                    ratio_stats.precedence_prunes
                )
                summary["baseline_forced_decisions"] += (
                    baseline_stats.forced_decisions
                )
                summary["closure_ratio_forced_decisions"] += (
                    ratio_stats.forced_decisions
                )

                if (
                    ratio_stats.visited_nodes
                    < baseline_stats.visited_nodes
                ):
                    summary["closure_ratio_improved_cases"] += 1
                elif (
                    ratio_stats.visited_nodes
                    == baseline_stats.visited_nodes
                ):
                    summary["closure_ratio_equal_cases"] += 1
                else:
                    summary["closure_ratio_worse_cases"] += 1

                reduction = (
                    baseline_stats.visited_nodes
                    - ratio_stats.visited_nodes
                )
                if edge_count > 0 and reduction > largest_reduction:
                    largest_reduction = reduction
                    explicit_example = {
                        "N": N,
                        "r": r,
                        "q": q,
                        "budget": budget,
                        "optimum": exhaustive_value,
                        "relations": {
                            str(k): sorted(descendants[k])
                            for k in frequencies
                            if descendants[k]
                        },
                        "ordinary": {
                            "selected": ordinary_set,
                            "visited_nodes": ordinary_stats.visited_nodes,
                            "leaves": ordinary_stats.leaves,
                        },
                        "baseline_precedence": {
                            "selected": baseline_set,
                            "visited_nodes": baseline_stats.visited_nodes,
                            "leaves": baseline_stats.leaves,
                        },
                        "closure_ratio": {
                            "selected": ratio_set,
                            "visited_nodes": ratio_stats.visited_nodes,
                            "leaves": ratio_stats.leaves,
                        },
                        "node_reduction_vs_baseline": reduction,
                    }

    ordinary_nodes = summary["ordinary_visited_nodes"]
    baseline_nodes = summary["baseline_precedence_visited_nodes"]
    ratio_nodes = summary["closure_ratio_visited_nodes"]

    summary["baseline_node_change_vs_ordinary_percent"] = (
        100.0 * (baseline_nodes - ordinary_nodes) / ordinary_nodes
    )
    summary["closure_ratio_node_change_vs_ordinary_percent"] = (
        100.0 * (ratio_nodes - ordinary_nodes) / ordinary_nodes
    )
    summary["closure_ratio_node_change_vs_baseline_percent"] = (
        100.0 * (ratio_nodes - baseline_nodes) / baseline_nodes
    )

    status = (
        "PASS"
        if summary["ordinary_optimum_mismatches"] == 0
        and summary["baseline_optimum_mismatches"] == 0
        and summary["closure_ratio_optimum_mismatches"] == 0
        and summary["false_certificates"] == 0
        else "FAIL"
    )

    result = {
        "schema": "pvg.precedence-closure-ratio-ordering.v1",
        "status": status,
        "benchmark": {
            "N": [4, 120],
            "r": [3, 30],
            "max_exact_budget": 4,
        },
        "branch_score": {
            "gain": "sum_c G_k(c)",
            "inclusion_closure_cost": "|(A(k) union {k}) minus S|",
            "primary_score": "gain / inclusion_closure_cost",
        },
        "summary": summary,
        "explicit_tree_improvement_example": explicit_example,
        "claims": {
            "exact_optimum_preserved": (
                summary["closure_ratio_optimum_mismatches"] == 0
            ),
            "false_certificates": summary["false_certificates"],
            "uniform_speedup_claim": False,
            "polynomial_time_claim": False,
            "goldbach_proof_claim": False,
            "rh_or_grh_progress_claim": False,
        },
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "precedence_closure_ratio_branch_ordering_v1.0.json"
    )
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
