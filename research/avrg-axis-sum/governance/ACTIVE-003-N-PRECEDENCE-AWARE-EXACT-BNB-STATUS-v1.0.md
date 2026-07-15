# ACTIVE-003-N — Precedence-Aware Exact Branch-and-Bound Status

**Version:** v1.0  
**Decision:** PASS  
**Classification:** exact optimization theorem + finite computational verification  
**Branch:** `agent/pvg-addition-fibers-theory-001`

## 1. Scope completed

ACTIVE-003-N integrates dominance-derived precedence constraints directly into the exact branch-and-bound tree.

Implemented:

- canonical orientation of channelwise equal-gain frequencies;
- all strict dominance prerequisite edges;
- transitive closure before search;
- selection propagation: selecting `j` forces every dominator/prerequisite of `j`;
- exclusion propagation: excluding `i` excludes every dependent candidate requiring `i`;
- contradiction and budget-feasibility pruning;
- integration with the existing optimistic channelwise upper bound;
- comparison with ordinary exact branch-and-bound and exhaustive enumeration;
- independent false-certificate audit against prime-prime channel mass.

## 2. Verification domain

```text
4 <= N <= 120
3 <= r <= 30
0 <= B <= min(4, number of paired frequencies)
optimization cases = 12,987
cases carrying precedence relations = 1,077
transitive precedence edges counted across cases = 1,632
```

## 3. Exactness results

```text
ordinary BnB optimum mismatches against exhaustive = 0
precedence-aware optimum mismatches against exhaustive = 0
false certificates = 0
status = PASS
```

Thus the implemented propagation and pruning rules preserved the exact optimal value throughout the tested domain.

## 4. Search-tree metrics

```text
ordinary visited nodes = 65,975
precedence-aware visited nodes = 66,443
ordinary upper-bound prunes = 22,516
precedence-aware upper-bound prunes = 22,345
precedence-constraint prunes = 426
precedence-forced decisions = 1,053
ordinary leaves = 13,746
precedence-aware leaves = 13,866
```

Per-case comparison:

```text
precedence-aware tree improved = 16 cases
equal = 12,814 cases
worse = 157 cases
```

Aggregate change:

```text
visited-node change = +0.7093596059%
leaf change = +0.8729812309%
```

The positive aggregate change means that this specific descendant-first branching heuristic is not uniformly superior. Precedence propagation is exact and does remove decisions, but branching order changes the time at which strong upper-bound incumbents are found. In some cases that interaction offsets the structural pruning.

This negative aggregate result is retained as part of the research record. No claim of universal acceleration is made.

## 5. Explicit improvement example

```text
N = 33
r = 24
q = 12
B = 1
precedence relation: 4 -> 2
optimum = 2 certified channels
```

Ordinary exact BnB:

```text
selected = {4}
visited nodes = 5
leaves = 2
upper-bound prunes = 1
```

Precedence-aware exact BnB:

```text
selected = {4}
visited nodes = 3
leaves = 1
upper-bound prunes = 1
```

The optimal value and selected solution agree, while the precedence-aware tree visits two fewer nodes and one fewer leaf.

## 6. Theory status

The following are proved in the accompanying theory file:

1. closure propagation preserves the canonical optimal search space;
2. excluding a prerequisite validly excludes all of its descendants;
3. the optimistic channelwise upper bound remains valid after precedence propagation because it ignores, rather than over-enforces, joint feasibility;
4. no propagation or upper-bound prune can remove a branch containing a strictly better feasible completion;
5. the resulting algorithm is exact.

## 7. Complexity boundary

No polynomial-time claim is authorized. The method remains exponential in the worst case. The verified reductions are finite-domain computational observations and depend on the instance and branching heuristic.

## 8. Number-theoretic boundary

The verifier checks finite local sufficient certificates derived from

```text
L_S(c) > C_hpp(c).
```

It does not prove that such a channel exists for every even `N`.

Therefore:

```text
Goldbach proof = NO
new global Goldbach progress claim = NO
RH progress = NO
GRH progress = NO
```

## 9. Files

```text
research/avrg-axis-sum/theory/
PRECEDENCE-AWARE-EXACT-BRANCH-AND-BOUND-v1.0.md
```

```text
research/avrg-axis-sum/code/
verify_precedence_aware_exact_branch_and_bound.py
```

```text
research/avrg-axis-sum/results/
precedence_aware_exact_branch_and_bound_verification_v1.0.json
```

```text
research/avrg-axis-sum/governance/
ACTIVE-003-N-PRECEDENCE-AWARE-EXACT-BNB-STATUS-v1.0.md
```

## 10. Final decision

```text
ACTIVE-003-N = PASS
exact optimum preserved = YES
false certificates = 0
universal speedup = NOT ESTABLISHED
polynomial complexity = NOT CLAIMED
Goldbach/RH/GRH progress = NOT CLAIMED
```
