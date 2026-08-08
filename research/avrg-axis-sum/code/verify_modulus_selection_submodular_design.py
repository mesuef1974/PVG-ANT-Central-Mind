#!/usr/bin/env python3
"""Finite checks for submodular modulus-selection rank design.

Checks:
1. diminishing returns for frequency-union coverage;
2. exhaustive budgeted optimum versus gain/cost greedy;
3. retention of the first strict greedy counterexample.

This verifier supports but does not replace the proofs in
MODULUS-SELECTION-SUBMODULAR-RANK-DESIGN-v1.1.md.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def lcm_many(values: List[int]) -> int:
    out = 1
    for value in values:
        out = lcm(out, value)
    return out


def run() -> Dict[str, object]:
    summary: Dict[str, object] = {
        "candidate_universes": 0,
        "submodularity_checks": 0,
        "submodularity_mismatches": 0,
        "optimization_instances": 0,
        "greedy_suboptimal_instances": 0,
        "first_greedy_counterexample": None,
    }

    for max_q in range(5, 10):
        candidates = list(range(2, max_q + 1))
        n = len(candidates)
        ambient_period = lcm_many(candidates)

        subgroup_masks: List[int] = []
        for q in candidates:
            mask = 0
            step = ambient_period // q
            for frequency in range(0, ambient_period, step):
                mask |= 1 << frequency
            subgroup_masks.append(mask)

        union_masks = [0] * (1 << n)
        costs = [0] * (1 << n)
        for mask in range(1, 1 << n):
            least_bit = mask & -mask
            index = least_bit.bit_length() - 1
            previous = mask ^ least_bit
            union_masks[mask] = union_masks[previous] | subgroup_masks[index]
            costs[mask] = costs[previous] + candidates[index]

        coverage = [mask.bit_count() for mask in union_masks]
        summary["candidate_universes"] = int(summary["candidate_universes"]) + 1

        for set_a in range(1 << n):
            for set_b in range(1 << n):
                if set_a & ~set_b:
                    continue
                for index in range(n):
                    bit = 1 << index
                    if set_b & bit:
                        continue
                    summary["submodularity_checks"] = int(summary["submodularity_checks"]) + 1
                    gain_a = coverage[set_a | bit] - coverage[set_a]
                    gain_b = coverage[set_b | bit] - coverage[set_b]
                    if gain_a < gain_b:
                        summary["submodularity_mismatches"] = int(summary["submodularity_mismatches"]) + 1

        for N in range(5, 21):
            rank_cap = N - 1
            for budget in range(3, 21):
                summary["optimization_instances"] = int(summary["optimization_instances"]) + 1

                best_rank = -1
                best_cost = 10**9
                best_mask = 0
                for mask in range(1 << n):
                    if costs[mask] > budget:
                        continue
                    rank = min(rank_cap, coverage[mask])
                    if rank > best_rank or (rank == best_rank and costs[mask] < best_cost):
                        best_rank = rank
                        best_cost = costs[mask]
                        best_mask = mask

                selected_mask = 0
                used_cost = 0
                while True:
                    base_rank = min(rank_cap, coverage[selected_mask])
                    best_index = None
                    best_key = None
                    for index, q in enumerate(candidates):
                        bit = 1 << index
                        if selected_mask & bit or used_cost + q > budget:
                            continue
                        gain = min(rank_cap, coverage[selected_mask | bit]) - base_rank
                        key = (gain / q, gain, q)
                        if best_key is None or key > best_key:
                            best_key = key
                            best_index = index
                    if best_index is None or best_key is None or best_key[1] == 0:
                        break
                    selected_mask |= 1 << best_index
                    used_cost += candidates[best_index]

                greedy_rank = min(rank_cap, coverage[selected_mask])
                if greedy_rank < best_rank:
                    summary["greedy_suboptimal_instances"] = int(summary["greedy_suboptimal_instances"]) + 1
                    if summary["first_greedy_counterexample"] is None:
                        summary["first_greedy_counterexample"] = {
                            "candidate_effective_moduli": candidates,
                            "N": N,
                            "budget": budget,
                            "greedy": {
                                "selection": [
                                    candidates[index]
                                    for index in range(n)
                                    if selected_mask & (1 << index)
                                ],
                                "rank": greedy_rank,
                                "cost": used_cost,
                            },
                            "optimal": {
                                "selection": [
                                    candidates[index]
                                    for index in range(n)
                                    if best_mask & (1 << index)
                                ],
                                "rank": best_rank,
                                "cost": best_cost,
                            },
                        }

    summary["status"] = (
        "PASS"
        if summary["submodularity_mismatches"] == 0
        and summary["first_greedy_counterexample"] is not None
        else "FAIL"
    )
    return summary


if __name__ == "__main__":
    result = run()
    output = Path(__file__).resolve().parents[1] / "results" / "modulus_selection_submodular_design_verification_v1.1.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
