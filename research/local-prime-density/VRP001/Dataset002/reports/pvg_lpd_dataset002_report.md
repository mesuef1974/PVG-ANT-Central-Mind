# Dataset 002 — Past-only Multiscale von Mangoldt and Residue-Character Features

**Decision:** NEGATIVE DIAGNOSTIC / UNRESOLVED

No same-window Lambda or character-weighted prime information was used as a predictor. All new analytic features end at `start-1` and use lengths `h`, `2h`, and `4h`.

- Classical RMSE: `0.521294`.
- Best nonclassical model: `Classical + lagged Lambda`.
- Best RMSE: `0.510878`.
- Improvement: `0.010415`.
- Bootstrap 95% CI: `[-0.000892, 0.021573]`.
- P(best better): `0.9617`.

Promotion required lower RMSE, a strictly positive bootstrap interval, and probability at least 0.95. The conditions were not all met.

Classification: numerical/statistical diagnostic only; no new theorem; no RH/GRH progress.