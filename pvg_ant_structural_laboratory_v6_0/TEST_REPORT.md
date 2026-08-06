# PVG–ANT Structural Laboratory v6.0 — Test Report

Date: 2026-07-20

## Software checks

- `node --check src/app.js`: PASS
- `node --check src/legacy-app.js`: PASS
- `npm test`: PASS
- browser smoke test: PASS
- browser console errors: 0
- browser page errors: 0
- independent Python unit tests: 4/4 PASS

## Exact reference checks

- `factor(360) = 2^3 * 3^2 * 5`
- `dlog(60,72) = log(30)`
- `Psi(10,2) = 4`
- `Psi(100,5) = 34`
- `Psi(1000,3) = 40`
- `Psi(1000,7) = 141`
- ordered prime-prime pairs for `N=10`: 3

## Independent holdout

- calibration cases: 60
- holdout cases: 66
- Pearson(B,error): 0.8058846295
- Spearman(B,error): 0.7330967540
- partial(B,error | pi(y), max-share): -0.1646316285
- partial(B,error | pi(y), max-share, alpha): 0.1661740560

The raw association reproduces, but does not survive the main controls. `B` remains a companion diagnostic rather than a standalone certificate.

## Counterexample witness

- delta B: 0.0065453343
- delta saddle error: 0.0472699796

## Scientific ceiling

Finite exact identities and computational diagnostics only. No uniform error theorem, Goldbach proof, RH/GRH progress, or originality claim.
