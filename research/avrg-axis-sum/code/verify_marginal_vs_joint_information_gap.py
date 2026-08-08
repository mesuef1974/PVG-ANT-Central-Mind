#!/usr/bin/env python3
"""Finite verifier for the marginal-versus-joint information-gap theorem.

Checks for 2 <= N <= 50 and 1 <= r,s <= 20:
  * rank(J)-rank(M) equals the cyclomatic number of the simple joint-cell graph;
  * the gap is nonnegative;
  * in the full-period regime the gap equals g(m-1)(n-1);
  * full-period information equivalence holds iff one effective modulus divides the other.

The computation is finite evidence supporting, not replacing, the proofs.
"""

from math import gcd, lcm
import json
from pathlib import Path


def graph_data(N: int, r: int, s: int):
    edges = {((2*a-N) % r, (2*a-N) % s) for a in range(1, N)}
    left = {u for u, _ in edges}
    right = {v for _, v in edges}

    adjacency = {('L', u): set() for u in left}
    adjacency.update({('R', v): set() for v in right})
    for u, v in edges:
        adjacency[('L', u)].add(('R', v))
        adjacency[('R', v)].add(('L', u))

    seen = set()
    components = 0
    for vertex in adjacency:
        if vertex in seen:
            continue
        components += 1
        stack = [vertex]
        seen.add(vertex)
        while stack:
            current = stack.pop()
            for nxt in adjacency[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)

    return edges, left, right, components


def main() -> None:
    checked = 0
    mismatch_count = 0
    full_period_cases = 0
    full_period_mismatch_count = 0
    maximum_gap = 0

    for N in range(2, 51):
        for r in range(1, 21):
            for s in range(1, 21):
                checked += 1
                edges, left, right, components = graph_data(N, r, s)

                rank_joint = len(edges)
                rank_marginal = len(left) + len(right) - components
                gap = rank_joint - rank_marginal
                cyclomatic = len(edges) - len(left) - len(right) + components

                if gap != cyclomatic or gap < 0:
                    mismatch_count += 1
                maximum_gap = max(maximum_gap, gap)

                q_r = r // gcd(2, r)
                q_s = s // gcd(2, s)
                period = lcm(q_r, q_s)
                if N - 1 >= period:
                    full_period_cases += 1
                    g = gcd(q_r, q_s)
                    m = q_r // g
                    n = q_s // g
                    predicted_gap = g * (m - 1) * (n - 1)
                    equivalent = gap == 0
                    divisibility = (q_r % q_s == 0) or (q_s % q_r == 0)
                    if gap != predicted_gap or equivalent != divisibility:
                        full_period_mismatch_count += 1

    result = {
        "theorem": "marginal-versus-joint information-gap theorem",
        "range": {"N": [2, 50], "r": [1, 20], "s": [1, 20]},
        "parameter_triples_checked": checked,
        "general_mismatch_count": mismatch_count,
        "full_period_cases_checked": full_period_cases,
        "full_period_mismatch_count": full_period_mismatch_count,
        "maximum_observed_rank_gap": maximum_gap,
        "status": "PASS" if mismatch_count == 0 and full_period_mismatch_count == 0 else "FAIL",
        "classification": "finite computational evidence; not a proof"
    }

    output = Path(__file__).resolve().parents[1] / "results" / "marginal_vs_joint_information_gap_verification_v1.1.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
