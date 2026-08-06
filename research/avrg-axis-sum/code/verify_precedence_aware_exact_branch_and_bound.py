"""Verify ACTIVE-003-N precedence-aware exact branch-and-bound.

Benchmark:
  4 <= N <= 120, 3 <= r <= 30, budgets B <= 4.

The verifier reconstructs von Mangoldt channel data, paired-frequency gains,
canonical dominance precedence, exhaustive optima, ordinary exact
branch-and-bound, and precedence-aware exact branch-and-bound. It also audits
certified channels against independently reconstructed prime-prime mass.
"""

from __future__ import annotations

import cmath
import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path

EPS = 1e-10


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
    z = [0.0] * q
    h = [0.0] * q
    prime_prime = [0.0] * q

    for a in range(1, N):
        la = von_mangoldt(a)
        lb = von_mangoldt(N - a)
        c = (u * a) % q
        z[c] += la * lb
        if is_prime(a) and is_prime(N - a):
            prime_prime[c] += la * lb
        if la > 0.0 and not is_prime(a):
            h[c] += la

    contamination = [
        math.log(N) * (h[c] + h[(u * N - c) % q]) for c in range(q)
    ]
    hat = [
        sum(z[c] * cmath.exp(2j * math.pi * k * c / q) for c in range(q))
        for k in range(q)
    ]
    frequencies = list(range(1, (q - 1) // 2 + 1))
    base = [sum(z) / q] * q
    if q % 2 == 0:
        nyquist = hat[q // 2].real / q
        base = [base[c] + nyquist * ((-1) ** c) for c in range(q)]

    contributions = {
        k: [
            (2.0 / q)
            * (hat[k] * cmath.exp(-2j * math.pi * k * c / q)).real
            for c in range(q)
        ]
        for k in frequencies
    }
    gains = {
        k: [x + abs(x) for x in contributions[k]] for k in frequencies
    }
    lower0 = [
        base[c] - sum(abs(contributions[k][c]) for k in frequencies)
        for c in range(q)
    ]
    return q, frequencies, contamination, lower0, gains, prime_prime


def objective(selected, lower0, gains, contamination) -> int:
    return sum(
        lower0[c] + sum(gains[k][c] for k in selected)
        > contamination[c] + EPS
        for c in range(len(contamination))
    )


def certified_channels(selected, lower0, gains, contamination):
    return [
        c
        for c in range(len(contamination))
        if lower0[c] + sum(gains[k][c] for k in selected)
        > contamination[c] + EPS
    ]


def precedence_closure(frequencies, gains, q):
    """Return transitive ancestors and descendants.

    Strict channelwise dominance is retained in full. Equal-gain candidates are
    canonically oriented from smaller to larger frequency index to avoid cycles
    while preserving an optimal canonical representative.
    """
    edges = {k: set() for k in frequencies}
    for i, j in itertools.permutations(frequencies, 2):
        ge = all(gains[i][c] >= gains[j][c] - EPS for c in range(q))
        strict = any(gains[i][c] > gains[j][c] + 1e-8 for c in range(q))
        equal = all(abs(gains[i][c] - gains[j][c]) <= EPS for c in range(q))
        if ge and (strict or (equal and i < j)):
            edges[i].add(j)

    changed = True
    while changed:
        changed = False
        for i in frequencies:
            implied = set()
            for j in list(edges[i]):
                implied |= edges[j]
            old_size = len(edges[i])
            edges[i] |= implied
            changed |= len(edges[i]) != old_size

    ancestors = {j: set() for j in frequencies}
    descendants = {i: set(edges[i]) for i in frequencies}
    for i in frequencies:
        for j in edges[i]:
            ancestors[j].add(i)
    return ancestors, descendants, sum(len(v) for v in edges.values())


def optimistic_upper_bound(
    included, undecided, slots, lower0, gains, contamination
) -> int:
    if slots < 0:
        return -1
    count = 0
    for c in range(len(contamination)):
        value = lower0[c] + sum(gains[k][c] for k in included)
        available = sorted(
            (gains[k][c] for k in undecided), reverse=True
        )
        value += sum(available[:slots])
        if value > contamination[c] + EPS:
            count += 1
    return count


@dataclass
class SearchStats:
    visited: int = 0
    leaves: int = 0
    bound_prunes: int = 0
    precedence_prunes: int = 0
    infeasible_prunes: int = 0


def ordinary_branch_and_bound(
    frequencies, budget, lower0, gains, contamination
):
    best = -1
    best_set = ()
    stats = SearchStats()
    order = sorted(
        frequencies, key=lambda k: sum(gains[k]), reverse=True
    )

    def recurse(position, included):
        nonlocal best, best_set
        stats.visited += 1
        slots = budget - len(included)
        remaining = order[position:]
        if slots < 0 or len(remaining) < slots:
            stats.infeasible_prunes += 1
            return
        upper = optimistic_upper_bound(
            included, remaining, slots, lower0, gains, contamination
        )
        if upper <= best:
            stats.bound_prunes += 1
            return
        if position == len(order) or slots == 0:
            stats.leaves += 1
            value = objective(included, lower0, gains, contamination)
            if value > best:
                best, best_set = value, tuple(sorted(included))
            return
        frequency = order[position]
        recurse(position + 1, included | {frequency})
        recurse(position + 1, included)

    recurse(0, set())
    return best, best_set, stats


def precedence_aware_branch_and_bound(
    frequencies,
    budget,
    lower0,
    gains,
    contamination,
    ancestors,
    descendants,
):
    best = -1
    best_set = ()
    stats = SearchStats()
    implications = 0

    def propagate(included, excluded):
        nonlocal implications
        included = set(included)
        excluded = set(excluded)
        changed = True
        while changed:
            changed = False
            new_included = set(included)
            for j in included:
                new_included |= ancestors[j]
            new_excluded = set(excluded)
            for i in excluded:
                new_excluded |= descendants[i]
            implications += (
                len(new_included) - len(included)
                + len(new_excluded) - len(excluded)
            )
            if new_included & new_excluded:
                return None, None, True
            if new_included != included or new_excluded != excluded:
                included, excluded = new_included, new_excluded
                changed = True
        return included, excluded, False

    def recurse(included, excluded):
        nonlocal best, best_set
        stats.visited += 1
        before = (len(included), len(excluded))
        included, excluded, contradiction = propagate(included, excluded)
        if contradiction:
            stats.precedence_prunes += 1
            return

        undecided = [
            k
            for k in frequencies
            if k not in included and k not in excluded
        ]
        slots = budget - len(included)
        if slots < 0:
            stats.precedence_prunes += int(len(included) > before[0])
            stats.infeasible_prunes += int(len(included) == before[0])
            return
        if len(undecided) < slots:
            stats.precedence_prunes += int(len(excluded) > before[1])
            stats.infeasible_prunes += int(len(excluded) == before[1])
            return

        upper = optimistic_upper_bound(
            included, undecided, slots, lower0, gains, contamination
        )
        if upper <= best:
            stats.bound_prunes += 1
            return
        if slots == 0 or not undecided:
            stats.leaves += 1
            value = objective(included, lower0, gains, contamination)
            if value > best:
                best, best_set = value, tuple(sorted(included))
            return

        frequency = max(
            undecided,
            key=lambda k: (
                len(descendants[k]),
                len(ancestors[k]),
                sum(gains[k]),
                -k,
            ),
        )
        recurse(included | {frequency}, excluded)
        recurse(included, excluded | {frequency})

    recurse(set(), set())
    return best, best_set, stats, implications


def exhaustive_optimum(frequencies, budget, lower0, gains, contamination):
    best = -1
    best_set = ()
    for selected in itertools.combinations(frequencies, budget):
        value = objective(selected, lower0, gains, contamination)
        if value > best:
            best, best_set = value, selected
    return best, best_set


def main() -> None:
    summary = {
        "optimization_cases": 0,
        "cases_with_precedence": 0,
        "ordinary_optimum_mismatches": 0,
        "precedence_optimum_mismatches": 0,
        "false_certificates": 0,
        "ordinary_visited_nodes": 0,
        "precedence_visited_nodes": 0,
        "ordinary_upper_bound_prunes": 0,
        "precedence_upper_bound_prunes": 0,
        "precedence_constraint_prunes": 0,
        "precedence_forced_decisions": 0,
        "ordinary_leaves": 0,
        "precedence_leaves": 0,
        "transitive_precedence_edges": 0,
        "tree_improved_cases": 0,
        "tree_equal_cases": 0,
        "tree_worse_cases": 0,
    }
    improvement_example = None

    for N in range(4, 121):
        for r in range(3, 31):
            (
                q,
                frequencies,
                contamination,
                lower0,
                gains,
                prime_prime,
            ) = build_instance(N, r)
            if len(frequencies) < 2:
                continue
            ancestors, descendants, edge_count = precedence_closure(
                frequencies, gains, q
            )

            for budget in range(0, min(4, len(frequencies)) + 1):
                summary["optimization_cases"] += 1
                summary["cases_with_precedence"] += int(edge_count > 0)
                summary["transitive_precedence_edges"] += edge_count

                exhaustive_value, _ = exhaustive_optimum(
                    frequencies, budget, lower0, gains, contamination
                )
                ordinary_value, ordinary_set, ordinary_stats = (
                    ordinary_branch_and_bound(
                        frequencies, budget, lower0, gains, contamination
                    )
                )
                (
                    precedence_value,
                    precedence_set,
                    precedence_stats,
                    forced_decisions,
                ) = precedence_aware_branch_and_bound(
                    frequencies,
                    budget,
                    lower0,
                    gains,
                    contamination,
                    ancestors,
                    descendants,
                )

                summary["ordinary_optimum_mismatches"] += (
                    ordinary_value != exhaustive_value
                )
                summary["precedence_optimum_mismatches"] += (
                    precedence_value != exhaustive_value
                )

                for selected in (ordinary_set, precedence_set):
                    for channel in certified_channels(
                        selected, lower0, gains, contamination
                    ):
                        summary["false_certificates"] += (
                            prime_prime[channel] <= EPS
                        )

                summary["ordinary_visited_nodes"] += ordinary_stats.visited
                summary["precedence_visited_nodes"] += precedence_stats.visited
                summary["ordinary_upper_bound_prunes"] += (
                    ordinary_stats.bound_prunes
                )
                summary["precedence_upper_bound_prunes"] += (
                    precedence_stats.bound_prunes
                )
                summary["precedence_constraint_prunes"] += (
                    precedence_stats.precedence_prunes
                )
                summary["precedence_forced_decisions"] += forced_decisions
                summary["ordinary_leaves"] += ordinary_stats.leaves
                summary["precedence_leaves"] += precedence_stats.leaves
                summary["tree_improved_cases"] += (
                    precedence_stats.visited < ordinary_stats.visited
                )
                summary["tree_equal_cases"] += (
                    precedence_stats.visited == ordinary_stats.visited
                )
                summary["tree_worse_cases"] += (
                    precedence_stats.visited > ordinary_stats.visited
                )

                if (
                    edge_count > 0
                    and precedence_stats.visited < ordinary_stats.visited
                    and improvement_example is None
                ):
                    improvement_example = {
                        "N": N,
                        "r": r,
                        "q": q,
                        "budget": budget,
                        "transitive_edges": edge_count,
                        "optimum": exhaustive_value,
                        "ordinary": {
                            "selected": ordinary_set,
                            "visited_nodes": ordinary_stats.visited,
                            "leaves": ordinary_stats.leaves,
                            "upper_bound_prunes": ordinary_stats.bound_prunes,
                        },
                        "precedence_aware": {
                            "selected": precedence_set,
                            "visited_nodes": precedence_stats.visited,
                            "leaves": precedence_stats.leaves,
                            "upper_bound_prunes": (
                                precedence_stats.bound_prunes
                            ),
                            "precedence_prunes": (
                                precedence_stats.precedence_prunes
                            ),
                        },
                        "relations": {
                            str(k): sorted(descendants[k])
                            for k in frequencies
                            if descendants[k]
                        },
                    }

    ordinary_nodes = summary["ordinary_visited_nodes"]
    precedence_nodes = summary["precedence_visited_nodes"]
    ordinary_leaves = summary["ordinary_leaves"]
    precedence_leaves = summary["precedence_leaves"]
    summary["aggregate_node_change_percent"] = (
        100.0 * (precedence_nodes - ordinary_nodes) / ordinary_nodes
    )
    summary["aggregate_leaf_change_percent"] = (
        100.0 * (precedence_leaves - ordinary_leaves) / ordinary_leaves
    )

    status = (
        "PASS"
        if summary["ordinary_optimum_mismatches"] == 0
        and summary["precedence_optimum_mismatches"] == 0
        and summary["false_certificates"] == 0
        else "FAIL"
    )
    result = {
        "schema": "pvg.precedence-aware-exact-bnb.v1",
        "status": status,
        "benchmark": {"N": [4, 120], "r": [3, 30], "max_budget": 4},
        "summary": summary,
        "explicit_tree_improvement_example": improvement_example,
        "claims": {
            "exact_optimum_preserved": (
                summary["precedence_optimum_mismatches"] == 0
            ),
            "false_certificates": summary["false_certificates"],
            "polynomial_time_claim": False,
            "goldbach_proof_claim": False,
            "rh_or_grh_progress_claim": False,
        },
    }
    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "precedence_aware_exact_branch_and_bound_verification_v1.0.json"
    )
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
