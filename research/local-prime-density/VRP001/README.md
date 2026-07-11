# Central Mind Vertical Research Pass 001

Research front: `PVG-LOCAL-PRIME-DENSITY-001`

This vertical pass tests whether the Central Mind can turn stored knowledge into a sharper question, an executable experiment, an adversarial refutation protocol, a named barrier, and proof-ready lemmas.

## Dataset 001

- Exact arithmetic through 10,000,000.
- 829 windows: 54 calibration and 775 research windows.
- Research scales: `h=x^0.5`, `h=x^(2/3)`, `h=x^0.75`.
- Numerical-range split: 319 train, 216 validation, 240 held-out test.
- Decision: `NEGATIVE DIAGNOSTIC / UNRESOLVED`.
- Elementary VSDS divisibility-boundary features did not improve held-out prediction beyond the classical baseline.

## Dataset 002

- New features use only intervals ending at `start-1`; no same-window von Mangoldt or character information is admitted as a predictor.
- Past scales: `h`, `2h`, `4h`.
- Character/residue moduli: 3, 4, 5, 7, 8, 11.
- Best model: `Classical + lagged Lambda`.
- Classical RMSE: 0.521294.
- Best RMSE: 0.510878.
- Apparent improvement: 0.010415.
- Paired-bootstrap 95% interval: [-0.000892, 0.021573].
- Probability better: 0.9617.
- Decision remains `NEGATIVE DIAGNOSTIC / UNRESOLVED` because the lower confidence bound is not strictly positive.

## Scientific ceiling

- No new theorem.
- No RH/GRH progress.
- No promotion to Candidate Signal.
- The current negative certificates reject only the tested finite feature families and numerical protocol.

## Next mathematical fork

Prefer a native residue-class target such as `psi(x+h;q,a)` rather than adding more generic machine-learning complexity.