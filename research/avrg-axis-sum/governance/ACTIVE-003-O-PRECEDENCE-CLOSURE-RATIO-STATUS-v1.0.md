# ACTIVE-003-O — Precedence-Closure-Ratio Branch Ordering Status

## Decision

`PASS — exactness preserved; baseline ordering loss removed on the finite benchmark.`

## Scope

This unit refines only the candidate-ordering rule inside the exact
precedence-aware branch-and-bound of `ACTIVE-003-N`.

It does not modify:

- the reduced Fourier channel construction;
- the gain vectors `G_k(c)`;
- the local higher-prime-power contamination threshold;
- the exact objective `F(S)`;
- the optimistic upper bound;
- the dominance replacement theorem.

## New rule

For a candidate frequency `k` at selected set `S`, define

\[
\kappa_S(k)=|(A(k)\cup\{k\})\setminus S|
\]

and

\[
\rho_S(k)=\frac{\sum_cG_k(c)}{\kappa_S(k)}.
\]

The brancher prioritizes the largest gain per newly forced inclusion slot.
This is a heuristic ordering rule inside an exact search.

## Verification domain

```text
4 <= N <= 120
3 <= r <= 30
0 <= exact budget B <= min(4, number of paired frequencies)
optimization cases = 12,987
cases with precedence = 1,077
```

## Exactness and safety

```text
ordinary optimum mismatches = 0
ACTIVE-003-N baseline optimum mismatches = 0
closure-ratio optimum mismatches = 0
false certificates = 0
status = PASS
```

The certified channels were checked against independently reconstructed
prime-prime channel mass.

## Aggregate tree comparison

```text
ordinary visited nodes = 65,975
ACTIVE-003-N baseline precedence nodes = 66,443
closure-ratio precedence nodes = 65,971
```

Therefore:

```text
ACTIVE-003-N versus ordinary = +0.7093596%
closure-ratio versus ACTIVE-003-N = -0.7103833%
closure-ratio versus ordinary = -0.0060629%
```

The new ordering removes essentially all of the aggregate node penalty seen in
`ACTIVE-003-N`, but its aggregate advantage over ordinary branch-and-bound is
only four visited nodes in this benchmark. This must not be described as a
substantial general speedup.

## Leaves and cuts

```text
ordinary leaves = 13,746
ACTIVE-003-N baseline leaves = 13,866
closure-ratio leaves = 13,746

ordinary upper-bound cuts = 22,516
ACTIVE-003-N upper-bound cuts = 22,345
closure-ratio upper-bound cuts = 22,227

ACTIVE-003-N precedence cuts = 3,504
closure-ratio precedence cuts = 3,506
```

The closure-ratio order exactly restores the aggregate leaf count to the
ordinary solver's count on this domain. The distribution of cut types changes;
this is not by itself evidence of asymptotic improvement.

## Per-instance comparison against ACTIVE-003-N

```text
improved cases = 157
equal cases = 12,814
worse cases = 16
```

Thus the rule is strongly favorable relative to the previous precedence order
on this finite domain, but not uniformly better.

## Explicit improvement example

```text
N = 34
r = 25
q = 25
budget = 4
precedence relation = 10 -> 5
exact optimum = 7
selected set = {2,4,8,12}
```

Tree sizes:

```text
ordinary BnB:                 19 visited nodes, 3 leaves
ACTIVE-003-N precedence BnB:  41 visited nodes, 4 leaves
closure-ratio precedence BnB: 19 visited nodes, 3 leaves
```

The new order removes 22 visited nodes relative to the baseline precedence
order for this instance while preserving the same optimum and selected set.

## Scientific classification

- precedence propagation: exact;
- transitive closure: exact;
- optimum preservation under branch reordering: exact;
- closure-ratio score: algorithmic heuristic;
- benchmark: finite computational verification;
- polynomial-time claim: none;
- uniform speedup claim: none;
- Goldbach proof claim: none;
- RH/GRH progress claim: none.

## Files

```text
research/avrg-axis-sum/theory/
PRECEDENCE-CLOSURE-RATIO-BRANCH-ORDERING-v1.0.md

research/avrg-axis-sum/code/
verify_precedence_closure_ratio_branch_ordering.py

research/avrg-axis-sum/results/
precedence_closure_ratio_branch_ordering_v1.0.json

research/avrg-axis-sum/governance/
ACTIVE-003-O-PRECEDENCE-CLOSURE-RATIO-STATUS-v1.0.md
```

## Next research direction

A justified next unit is to strengthen the optimistic bound itself using
precedence-feasible closures, rather than only changing branch order. Such a
bound must remain optimistic after accounting for forced ancestors and cannot
use an incompatible collection of channelwise top gains.
