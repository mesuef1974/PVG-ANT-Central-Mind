# PVG Local Prime Density — Dataset and Diagnostic 001

**Status:** Executed computational intake  
**Classification:** NEGATIVE DIAGNOSTIC / UNRESOLVED  
**New theorem:** No  
**RH/GRH progress:** None

## Dataset

- Exact arithmetic up to `10,000,000`.
- Total windows: `829`.
- Calibration windows: `54`.
- Research windows: `775`.
- Train / validation / test: `319 / 216 / 240`.
- Research families: `h=x^0.5`, `h=x^(2/3)`, `h=x^0.75`.
- Split is by numerical range, not random rows.

## Calibration

Raw prime density decreases with digit length, while `prime_count * log(midpoint) / h` approaches 1.

- Two-digit normalized mean: `0.865894`.
- Seven-digit normalized mean: `0.999941`.

## Held-out models

Target: `(prime_count - Li expectation) / sqrt(Li expectation)`.

- Li zero-residual baseline RMSE: `0.518476`.
- Classical Ridge RMSE: `0.521294`.
- Classical + VSDS Ridge RMSE: `0.521523`.
- VSDS improvement over classical: `-0.000229`.
- Paired-bootstrap 95% interval: `[-0.016959, 0.015641]`.
- Probability VSDS is better: `0.4942`.

## Decision

The present VSDS features do not show stable held-out predictive value beyond the classical baseline. The result rejects only the current low-level family: selected floor remainders, aggregate remainder norms, and sieve-survivor residuals for `z=7,13,19,29` in this protocol.

A stronger candidate needs information not reducible to elementary boundary remainders: multi-scale correlations, weighted von Mangoldt observables, residue/character decompositions, or analytic cancellation information.