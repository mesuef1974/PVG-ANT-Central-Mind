# Dataset 002 — Past-only Multiscale von Mangoldt and Residue-Character Features

**Decision:** UNRESOLVED WITH EXPLORATORY UNADJUSTED SIGNAL  
**Promotion:** Not promoted to Candidate Signal  
**New theorem:** No  
**RH/GRH progress:** None

## Leakage control

No same-window von Mangoldt or character-weighted prime information was used as a predictor. All new analytic features end at `start-1` and use lengths `h`, `2h`, and `4h`.

## Lowest-RMSE model

The model with the lowest held-out RMSE was:

`Classical + lagged Lambda`

- Classical RMSE: `0.521294`.
- Model RMSE: `0.510878`.
- Improvement: `0.010415`.
- Bootstrap 95% CI: `[-0.000892, 0.021573]`.
- Probability better: `0.9617`.

This model does not pass the predeclared unadjusted promotion rule because the bootstrap lower bound is not strictly positive.

## Exploratory secondary model

A different model,

`Classical + Lambda + characters + residue energy`,

showed:

- Improvement: `0.007473`.
- Bootstrap 95% CI: `[0.000385, 0.015105]`.
- Probability better: `0.98`.
- One-sided bootstrap p-value: `0.02`.

This passes the unadjusted rule. However, four nonclassical model families were tested on the same held-out range. After multiplicity correction:

- Bonferroni-adjusted p-value: `0.08`.
- Holm-adjusted p-value: `0.08`.

Therefore the exploratory model does not pass the multiplicity-adjusted threshold of `0.05`.

## Scientific interpretation

The correct classification is neither a clean negative result nor a promoted candidate mechanism. Dataset 002 contains an exploratory signal that requires an independently frozen replication dataset.

The next experiment must:

1. freeze the two candidate families before inspecting new outcomes;
2. use a numerically disjoint range;
3. avoid retuning model families on the replication test set;
4. preserve the same leakage controls;
5. predeclare the multiplicity rule.

Classification: numerical/statistical diagnostic only; replication required; no new theorem; no RH/GRH progress.
