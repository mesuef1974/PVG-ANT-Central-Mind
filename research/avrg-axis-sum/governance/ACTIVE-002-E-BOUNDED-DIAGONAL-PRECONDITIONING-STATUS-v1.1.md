# ACTIVE-002-E — Bounded Diagonal Preconditioning Status

Status: `CLOSED — PASS-WITH-NUMERICAL-CLASSIFICATION`

## Completed

- invertible positive diagonal left scaling preserves rank and kernel — **proved**;
- gauge normalization `sum(log weights)=0` — **defined**;
- unrestricted optimization boundary risk — **identified and governed**;
- bounded log-spread problem `|log p_i|<=tau` — **defined**;
- existence of a bounded minimizer — **proved by compactness and continuity**;
- multi-start numerical optimizer — **implemented**;
- raw / row-normalized / bounded-optimized comparison — **completed**;
- five benchmark designs — **PASS**;
- N=30 conditioning inconsistency — **corrected with visible history**.

## Benchmark conclusion at tau=4

The best values found improved on row normalization in all five benchmark cases, while preserving rank and kernel.

Representative results:

- `N=24`, periods `[5,9,11]`: `108.7134 -> 92.4884 -> 84.3783`;
- `N=24`, periods `[7,9,11]`: `32.3756 -> 29.5267 -> 26.3236`;
- `N=30`, periods `[5,7,9,11]`: `1938.1831 -> 1763.5913 -> 1501.0369`;
- `N=30`, periods `[7,8,9,11,12]`: `589.0130 -> 507.2448 -> 417.8319`.

The three values in each chain are raw, row-normalized, and bounded optimized.

## Classification ceiling

The bounded problem has an attained minimum, but the implemented solver is nonconvex and multi-start. Therefore the reported optimized values are:

`COMPUTATIONAL UPPER BOUNDS ON THE BOUNDED OPTIMUM`.

No global-optimality certificate is claimed.

## Correction record

An intermediate claim that the raw condition number for `N=30`, periods `[7,8,9,11,12]`, was about `98.17` was erroneous. Independent reconstruction under the declared reduced-period convention gives approximately `589.0130`. The result ledger has been corrected without deleting the correction history.

## Controlling files

- `theory/BOUNDED-DIAGONAL-PRECONDITIONING-v1.1.md`;
- `code/optimize_bounded_diagonal_preconditioner.py`;
- `results/bounded_diagonal_preconditioning_verification_v1.1.json`;
- corrected `results/cost_rank_conditioning_pareto_summary_v1.1.json`.

## Next target

`ACTIVE-002-F — visible-subspace spectral whitening`.

Study non-diagonal left preconditioners that act as an exact or regularized whitener on the row space, while preserving the kernel and explicitly accounting for implementation cost and noise amplification.

## Scientific ceiling

This unit improves finite numerical conditioning only. It creates no new arithmetic information and makes no Goldbach, sieve, prime-distribution, RH, or GRH claim.
