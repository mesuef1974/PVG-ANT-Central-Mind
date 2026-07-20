# PVG–ANT Structural Laboratory v6.1 — Test Report

Date: 2026-07-21

## Software checks

- `node --check src/core/arithmetic.js`: PASS
- `node --check src/layout.js`: PASS
- `node --check src/app.js`: PASS
- `node --check tests/layout.test.mjs`: PASS
- `node --test`: 9/9 PASS

## Core exact checks

- `factor(360) = 2^3 * 3^2 * 5`
- `dlog(60,72) = log(30)`
- `firstPrimes(8) = [2,3,5,7,11,13,17,19]` (17 present, no skip)

## Mandatory geometry checks (cone, k ∈ {4,7,12,15,20})

- `|d_j| = 1` for all axes: PASS
- `d_j · ŷ = cos(θ)` (uniform polar angle): PASS
- `Σ_j (d_{j,x}, d_{j,z}) ≈ 0`: PASS
- `d_E(m,n) ≤ d_log(m,n) + ε` for sampled pairs, BOTH layouts: PASS
- `ρ = 1` on a single prime ray (2↔4, 2↔8, 4↔8, 3↔9): PASS

## Distortion snapshot (k = 9, primes 2..23, n ≤ 5000, 951 smooth points, 79,800 pairs)

| metric            | Legacy   | Cone     |
|-------------------|----------|----------|
| min ρ             | 0.0122   | 0.0070   |
| 5th percentile ρ  | 0.1739   | 0.1728   |
| median ρ          | 0.5280   | 0.5186   |
| max ρ (≤ 1)       | 1.000000 | 1.000000 |
| Spearman(d_E,d_log)| 0.4544  | 0.4605   |
| collisions (d_E<1e-6)| 0     | 0        |

## Honest observation

At these parameters the symmetric cone does **not** materially reduce projection distortion
relative to the legacy quasi-random layout (median ρ ≈ 0.52 for both; Spearman ≈ 0.45–0.46 for
both). Both are low-rank R³ shadows and lose most of the metric. The cone's contribution is
**interpretability** — uniform polar angle, azimuth = prime order, vertical = log n, all axes
visible — not a smaller distortion. `ρ ≤ 1` holds exactly, confirming the triangle-inequality
bound and refuting any "Euclidean ≈ d_log" reading.

## Scientific ceiling

Finite exact identities and computational diagnostics only. No uniform error theorem, geometry
preservation, Goldbach proof, RH/GRH progress, or originality claim.
