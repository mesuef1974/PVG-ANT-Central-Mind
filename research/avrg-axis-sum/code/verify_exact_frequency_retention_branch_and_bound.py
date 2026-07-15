"""Verify exact frequency-retention branch-and-bound.

Declared benchmark:
  2 <= N <= 120, 1 <= r <= 20, budgets B=0..4.

The verifier reconstructs von Mangoldt additive fibers, reduced paired
frequencies, local higher-prime-power contamination thresholds, exhaustive
exact-size optima, and the branch-and-bound solver. It asserts equality of
optimal certificate counts and zero false certificates.
"""

import cmath
import itertools
import math
from typing import Dict, List, Sequence, Tuple

import numpy as np


def lambda_table(nmax: int):
    lam = [0.0] * (nmax + 1)
    prime = [True] * (nmax + 1)
    prime[0] = prime[1] = False
    for p in range(2, nmax + 1):
        if prime[p]:
            for m in range(p * p, nmax + 1, p):
                prime[m] = False
            x = p
            while x <= nmax:
                lam[x] = math.log(p)
                if x > nmax // p:
                    break
                x *= p
    return lam, prime


LAM, PRIME = lambda_table(120)


def instance(N: int, r: int):
    g = math.gcd(2, r)
    q = r // g
    u = 2 // g
    weights = np.array([LAM[a] * LAM[N - a] for a in range(1, N)])
    hpp = np.zeros(q)
    pp = np.zeros(q)
    for a in range(1, N):
        c = (u * a) % q
        if LAM[a] and not PRIME[a]:
            hpp[c] += LAM[a]
        if PRIME[a] and PRIME[N - a]:
            pp[c] += math.log(a) * math.log(N - a)
    threshold = np.array([
        math.log(N) * (hpp[c] + hpp[(u * N - c) % q]) for c in range(q)
    ])
    hat = np.array([
        sum(weights[a - 1] * cmath.exp(2j * math.pi * k * ((u * a) % q) / q)
            for a in range(1, N))
        for k in range(q)
    ])
    pairs = list(range(1, (q - 1) // 2 + 1))
    base = np.full(q, hat[0].real / q)
    if q % 2 == 0:
        k = q // 2
        base += np.array([(hat[k] * cmath.exp(-2j * math.pi * k * c / q)).real / q
                          for c in range(q)])
    signed: Dict[int, np.ndarray] = {}
    for k in pairs:
        signed[k] = np.array([
            (2.0 / q) * (hat[k] * cmath.exp(-2j * math.pi * k * c / q)).real
            for c in range(q)
        ])
    lower0 = base.copy()
    for k in pairs:
        lower0 -= np.abs(signed[k])
    gains = {k: signed[k] + np.abs(signed[k]) for k in pairs}
    return pairs, lower0, gains, threshold, pp


def score(lower0, gains, threshold, chosen: Sequence[int]) -> int:
    lower = lower0.copy()
    for k in chosen:
        lower += gains[k]
    return int(np.sum(lower > threshold + 1e-12))


def exhaustive(data, budget: int):
    pairs, lower0, gains, threshold, _ = data
    b = min(budget, len(pairs))
    best = (-1, ())
    for chosen in itertools.combinations(pairs, b):
        value = score(lower0, gains, threshold, chosen)
        if value > best[0] or (value == best[0] and chosen < best[1]):
            best = (value, chosen)
    return best, math.comb(len(pairs), b)


def branch_and_bound(data, budget: int):
    pairs, lower0, gains, threshold, _ = data
    b = min(budget, len(pairs))
    order = sorted(pairs, key=lambda k: float(np.sum(gains[k])), reverse=True)
    incumbent = tuple(order[:b])
    best_value = score(lower0, gains, threshold, incumbent)
    best_set = tuple(sorted(incumbent))
    nodes = pruned = leaves = 0

    def visit(i: int, selected: Tuple[int, ...], lower: np.ndarray, need: int):
        nonlocal best_value, best_set, nodes, pruned, leaves
        nodes += 1
        if need == 0:
            leaves += 1
            value = int(np.sum(lower > threshold + 1e-12))
            chosen = tuple(sorted(selected))
            if value > best_value or (value == best_value and chosen < best_set):
                best_value, best_set = value, chosen
            return
        if len(order) - i < need:
            return
        remaining = order[i:]
        matrix = np.stack([gains[k] for k in remaining], axis=0)
        if need >= len(remaining):
            optimistic = lower + matrix.sum(axis=0)
        else:
            optimistic = lower + np.partition(matrix, -need, axis=0)[-need:, :].sum(axis=0)
        upper = int(np.sum(optimistic > threshold + 1e-12))
        if upper <= best_value:
            pruned += 1
            return
        k = order[i]
        visit(i + 1, selected + (k,), lower + gains[k], need - 1)
        visit(i + 1, selected, lower, need)

    visit(0, (), lower0.copy(), b)
    return (best_value, best_set), nodes, pruned, leaves


def main():
    summary = {"instances": 0, "mismatches": 0, "false_certificates": 0,
               "bb_nodes": 0, "bb_pruned_nodes": 0, "bb_leaf_evaluations": 0,
               "exhaustive_leaf_evaluations": 0}
    for N in range(2, 121):
        for r in range(1, 21):
            data = instance(N, r)
            for budget in range(5):
                exact, total = exhaustive(data, budget)
                bb, nodes, pruned, leaves = branch_and_bound(data, budget)
                summary["instances"] += 1
                summary["bb_nodes"] += nodes
                summary["bb_pruned_nodes"] += pruned
                summary["bb_leaf_evaluations"] += leaves
                summary["exhaustive_leaf_evaluations"] += total
                if exact[0] != bb[0]:
                    summary["mismatches"] += 1
                pairs, lower0, gains, threshold, pp = data
                lower = lower0.copy()
                for k in bb[1]:
                    lower += gains[k]
                summary["false_certificates"] += int(np.sum((lower > threshold + 1e-12) & (pp <= 1e-12)))
    assert summary["mismatches"] == 0
    assert summary["false_certificates"] == 0
    summary["leaf_reduction_fraction"] = 1.0 - summary["bb_leaf_evaluations"] / summary["exhaustive_leaf_evaluations"]
    print(summary)


if __name__ == "__main__":
    main()
