# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS031.

## Scope

- PASS001–PASS031 research reports: 31
- Python programs and reproducibility tests: 40
- Saved JSON experiment outputs: 49
- Figures: 1
- Preregistered diagnostic protocols: 8
- Retained source artifacts before this archive index: 129

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

PASS031 is complete. Its one-extra-coordinate protocol, implementation, and tests were committed before the locked analysis.

Keeping the full PASS029 amplitude rank d and adding the normalized all-ones direction as coordinate d+1 succeeds on all six preregistered conditions:

- augmented held-out vector skill: 0.677262;
- scalar orbit-sum skill: 1.000000 by construction;
- skill difference versus the original rank-d SVD: +0.000686;
- loss versus free rank-(d+1) SVD: 0.079234;
- constrained-random p-value: 0.000200;
- modulus-level vector skill >= 0.60 in 5/7 moduli.

The aggregate rank overhead is 22.73%. The supported finite-range description is an amplitude subspace plus one explicit cancellation coordinate.

The next proposed diagnostic is PASS032: test whether the cancellation coefficient can be predicted from amplitude coordinates under a completely held-out window, rather than merely preserved after observing the orbit vector.

## Reproduction

```bash
python code/avrg_pass031.py
python -m unittest discover -v -s code -p 'test_avrg_pass031.py'
```
