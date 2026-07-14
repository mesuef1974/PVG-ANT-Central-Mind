# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS034.

## Scope

- PASS001–PASS034 research reports: 34
- Python programs and reproducibility tests: 46
- Saved JSON experiment outputs: 53
- Figures: 1
- Preregistered diagnostic protocols: 11
- Retained source artifacts before this archive index: 145

PASS001–PASS004 are preserved as full research reports containing their finite calculations and derivations. Standalone scripts were first retained from PASS005 onward. No missing standalone PASS001–PASS004 scripts are claimed.

## Layout

- `reports/`: the Arabic research reports in chronological order.
- `code/`: executable Python programs, plotting code, artifact builders, and tests.
- `results/`: all retained JSON outputs, including sampled, full-window, and held-out runs.
- `figures/`: generated static figures.
- `protocols/`: diagnostic protocols fixed before the corresponding detailed analysis.
- `site/`: publication record for the PASS023 reader page.
- `MANIFEST.json` and `SHA256SUMS.txt`: exact inventory and integrity hashes.

## Scientific ceiling

This archive contains finite computational diagnostics, structural reformulations, refutations of intermediate empirical laws, and reproducible evidence. It contains no asymptotic proof, no proof of Goldbach, and no claim of direct progress toward a proof of Goldbach.

## Current stopping point

PASS034 is complete. Its e=14 scan and disjoint-block transport protocol, implementation, and tests were committed before either numerical outcome.

The exact e=14 orbit window passes every closure gate. It enables reciprocal transport between early (14–16) and late (17–19) training blocks with no shared window.

The locked transport claim is rejected:

- aggregate scalar skill: -0.136844;
- scalar-skill permutation p-value: 0.000400;
- mean signed functional cosine: 0.207815;
- cosine permutation p-value: 0.092981;
- positive scalar skill in 2/7 moduli;
- nonnegative aggregate skill in 0/2 directions.

The real alignment is stronger than restricted permutations but remains worse than the predictive zero baseline. This is finite partial structure, not successful linear cancellation transport.

The next proposed diagnostic is PASS035: model the scalar cancellation channel independently of the amplitude subspace and test low-rank window-by-character factorization under holdout.

## Reproduction

```bash
python code/avrg_pass034.py
python -m unittest discover -v -s code -p 'test_avrg_pass034.py'
```
