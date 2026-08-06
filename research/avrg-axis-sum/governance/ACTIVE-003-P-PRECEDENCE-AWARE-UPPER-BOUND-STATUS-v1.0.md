# ACTIVE-003-P — Precedence-Aware Upper Bound Status

## Status

`PASS / CLOSED AS A VERIFIED NEGATIVE PERFORMANCE RESULT`

## Scope completed

- defined the transitive-closure-feasible channelwise upper bound;
- proved validity for every feasible completion;
- proved pointwise domination over the previous unconstrained top-gain bound;
- implemented exact closure enumeration for budgets `B<=4`;
- compared old and new bounds against exhaustive optima;
- independently audited certified channels against prime-prime mass;
- recorded search-tree, pruning, and closure-enumeration metrics.

## Verification envelope

```text
4 <= N <= 120
3 <= r <= 30
exact budget B <= 4
optimization cases = 12,987
cases with precedence = 1,077
```

## Correctness results

```text
old-bound optimum mismatches = 0
precedence-bound optimum mismatches = 0
false certificates = 0
status = PASS
```

## Search results

```text
old-bound visited nodes = 65,971
precedence-bound visited nodes = 65,971
old-bound leaves = 13,746
precedence-bound leaves = 13,746
old-bound prunes = 22,227
precedence-bound prunes = 22,227
improved cases = 0
equal cases = 12,987
worse cases = 0
node change = 0.0%
```

## Bound-work audit

```text
precedence-bound calls = 62,465
feasible closures tested = 2,337,021
```

The stronger bound incurred substantial exact closure-enumeration work but did not change a single branch-and-bound decision on the tested domain.

## Scientific interpretation

The theorem is useful: precedence feasibility can be incorporated directly into the optimistic bound, and the resulting bound is never weaker. The benchmark, however, shows that this extra sharpness is operationally dormant in the present regime. Sparse precedence relations, small budgets, and the strength of the existing channelwise bound make both bounds cross the integer certification threshold on exactly the same channels at every reached node.

This unit therefore closes with a negative performance conclusion rather than a speedup claim.

## Classification

- upper-bound validity: `EXACT THEOREM`;
- pointwise comparison with old bound: `EXACT THEOREM`;
- zero tree change over benchmark: `FINITE COMPUTATIONAL RESULT`;
- universal equality of the two bounds: `NOT CLAIMED`;
- uniform speedup: `NOT ESTABLISHED`;
- polynomial-time complexity: `NOT CLAIMED`;
- Goldbach proof: `NOT CLAIMED`;
- RH/GRH progress: `NONE`.

## Files

```text
research/avrg-axis-sum/theory/PRECEDENCE-AWARE-UPPER-BOUND-v1.0.md
research/avrg-axis-sum/code/verify_precedence_aware_upper_bound.py
research/avrg-axis-sum/results/precedence_aware_upper_bound_verification_v1.0.json
research/avrg-axis-sum/governance/ACTIVE-003-P-PRECEDENCE-AWARE-UPPER-BOUND-STATUS-v1.0.md
```

## Next action

`ACTIVE-003-Q — Certification-Margin-Aware Pruning`

The next useful direction is not another combinatorial tightening of the same bound. It is to track channel margins

\[
M_S(c)=L_S(c)-C(c)
\]

and prioritize or prune using the minimum additional gain required to cross zero. This targets the actual integer certification threshold that made the stronger ACTIVE-003-P bound operationally indistinguishable from the old one.
