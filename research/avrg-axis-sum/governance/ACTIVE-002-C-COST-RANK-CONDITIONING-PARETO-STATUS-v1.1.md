# ACTIVE-002-C — Cost–Rank–Conditioning Pareto Design Status

Status: `CLOSED — EXACT FINITE BENCHMARK PASS`

## Completed

- three-objective design metrics defined;
- exact Pareto dominance defined;
- reusable exhaustive optimizer added;
- benchmark over reduced periods \(2,\dots,12\) completed for \(N=8,12,16,24,30\);
- 10,240 designs evaluated;
- minimum-cost full-rank and best-conditioned full-rank designs separated explicitly;
- numerical-summary correction for \(N=30\) committed before closure.

## Key outcome

Rank alone is not a sufficient design objective. For \(N=24\), the minimum-cost full-rank design \(\{5,9,11\}\) has

\[
\kappa_2^+\approx108.713,
\]

whereas \(\{7,9,11\}\), at cost \(27\) instead of \(25\), has

\[
\kappa_2^+\approx32.376.
\]

For \(N=30\), even the best-conditioned full-rank design inside the restricted pool remains poorly conditioned, showing that candidate-pool expansion or weighted/preconditioned measurements are required.

## Controls

- Candidate pool: \(Q=\{2,\dots,12\}\).
- Cost model: \(c(q)=q\).
- SVD tolerance: \(10^{-9}\).
- Exhaustive search: exact for this finite declared pool.
- No universal optimum or scalable polynomial algorithm is claimed.

## Controlling files

- `theory/COST-RANK-CONDITIONING-PARETO-DESIGN-v1.1.md`
- `code/exact_cost_rank_conditioning_pareto.py`
- `results/cost_rank_conditioning_pareto_summary_v1.1.json`

## Next target

`ACTIVE-002-D — weighted rows and preconditioning`:

1. determine whether row normalization improves \(\kappa_2^+\);
2. compare raw, degree-normalized, and noise-weighted marginal operators;
3. preserve rank while quantifying stability gains;
4. distinguish genuine information improvement from mere rescaling.

## Scientific ceiling

This unit is finite-dimensional measurement design. It does not prove Goldbach, improve prime-distribution estimates, or advance RH/GRH.
