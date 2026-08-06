# ACTIVE-003-M — Frequency Dominance Precedence Status v1.2

## Status
CLOSED — PASS

## Completed
- Defined channelwise paired-frequency gain dominance.
- Proved the replacement theorem.
- Proved safe precedence constraints for exact budget optimization.
- Disproved naive global deletion of dominated candidates.
- Added a complete verifier and finite benchmark certificate.

## Benchmark
- 4 <= N <= 120.
- 3 <= r <= 30.
- Budgets B <= 4.
- Optimization cases: 12,987.
- Unrestricted subsets: 975,078.
- Canonical precedence-respecting subsets: 964,377.
- Subsets removed: 10,701.
- Exact-optimum mismatches: 0.

## Mandatory counterexample
At N=15, r=12, q=6, B=2, frequency 2 dominates frequency 1, but the optimum needs both:

- F(empty)=0.
- F({1})=0.
- F({2})=0.
- F({1,2})=2.

Therefore dominance is a branching precedence rule, not a candidate-deletion certificate.

## Honest classification
- Exact combinatorial optimization result: yes.
- Search-space reduction: finite and verified, modest on the declared benchmark.
- General polynomial-time claim: no.
- New analytic lower bound for Goldbach: no.
- RH/GRH progress: none.

## Next action
Integrate precedence constraints into the existing Branch-and-Bound solver and measure node reduction beyond the standalone canonical-subset benchmark.
