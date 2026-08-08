# ACTIVE-002-B — Exact Pareto Modulus-Design Optimizer Status

Status: `CLOSED-PASS-WITH-CORRECTED-SUMMARY`

Date: 2026-07-15

## 1. Object

For a fixed fiber size parameter \(N\), candidate reduced periods \(Q\), and cost model

\[
\operatorname{cost}(q)=q,
\]

the unit solves exactly

\[
\max_{S\subseteq Q,\ \operatorname{cost}(S)\le B} R_N(S),
\qquad
R_N(S)=\min\left(N-1,\left|\bigcup_{q\in S}H_q\right|\right).
\]

It also computes:

1. the complete cost-rank Pareto frontier;
2. the best rank for every budget;
3. the minimum cost for every attainable rank threshold;
4. all minimum-cost full-rank designs within the candidate pool.

## 2. Delivered implementation

- `code/exact_modulus_design_pareto.py`

The implementation exhaustively enumerates all subsets of the declared candidate pool. Therefore its output is exact, not heuristic, for that finite instance.

## 3. Benchmark certificate

- candidate reduced periods: \(Q=\{2,3,\ldots,12\}\);
- tested range: \(2\le N\le30\);
- subsets per instance: \(2^{11}=2048\);
- instances: 29;
- total designs enumerated: 59,392.

Result file:

- `results/exact_modulus_design_pareto_summary_v1.1.json`.

The result summary was corrected after an internal review found that the first handwritten condensation omitted tied optima and misstated several costs. The corrected file is canonical.

## 4. Representative exact optima

Under the declared candidate pool and cost model:

\[
N=16:\quad \min \operatorname{cost}=16,
\]
with two optimal full-rank designs

\[
\{7,9\},\qquad \{5,11\}.
\]

For \(N=24\):

\[
\min \operatorname{cost}=25,
\qquad S=\{5,9,11\}.
\]

For \(N=30\):

\[
\min \operatorname{cost}=32,
\qquad S=\{5,7,9,11\}.
\]

These are finite optimization results, not asymptotic theorems.

## 5. Scientific classification

- exact optimizer for finite candidate pools — **complete**;
- Pareto frontier extraction — **complete**;
- minimum-cost full-rank certificate — **complete**;
- benchmark over 59,392 designs — **PASS**;
- heuristic comparison baseline — **available**;
- polynomial-time exact optimization — **not claimed**;
- large-scale approximation guarantee under knapsack cost — **not yet developed**;
- joint optimization of rank and conditioning — **still open**.

## 6. Limitation

The exhaustive method has exponential complexity in the number of candidates. It is a certificate generator for moderate pools, not a scalable solver for arbitrarily large pools.

The optimum also depends on:

- the candidate reduced periods;
- the chosen cost model;
- the target \(N\);
- whether rank alone or rank plus conditioning is optimized.

## 7. Next authorized target

`ACTIVE-002-C — Rank-conditioning Pareto design`:

1. compute singular values for each feasible design;
2. discard rank-deficient designs when full reconstruction is required;
3. construct a three-objective frontier involving cost, rank, and condition number;
4. determine whether minimum-cost full-rank designs can be severely ill-conditioned.

## 8. Scientific ceiling

This optimization layer concerns finite measurement design for the defined residue-channel operators. It does not prove Goldbach, improve prime-distribution estimates, or establish novelty/priority for the broader PVG program.
