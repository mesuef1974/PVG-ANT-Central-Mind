# Scale-Heterogeneity Diagnostic and Proof-Strategy Pass

**Pass ID:** `PVG-LPD-SCALE-HETEROGENEITY-001`  
**Parent result:** `CLOSE DATASET 003 — PASS`  
**Status:** `DIAGNOSTIC / PROOF-STRATEGY INTAKE`  
**Scientific ceiling:** no theorem about primes, no replicated candidate signal, no RH/GRH progress.

## 1. Governing question

Dataset 003 produced a mild positive aggregate point estimate, but the effect changed sign by window scale:

```text
h = x^(1/2)    negative
h = x^(2/3)    positive
h = x^(3/4)    positive
```

The correct next question is not whether another model can fit the data. It is:

> What exact covariance object controls whether a past-only arithmetic correction improves a classical local-prime baseline, and why does its gain change with the scale exponent?

## 2. Exact correction-gain identity

Let

```text
y   = observed standardized prime-count residual
c   = classical prediction
d   = primary prediction - classical prediction
e_c = y - c
```

Then the primary error is `e_c-d`, and pointwise

```text
(e_c)^2 - (e_c-d)^2 = 2 e_c d - d^2.
```

Averaging over any finite collection gives the exact identity

```text
MSE_classical - MSE_primary
  = 2 E[e_c d] - E[d^2].
```

Therefore a correction helps exactly when

```text
2 E[e_c d] > E[d^2].
```

The first term is **alignment** with the remaining classical error. The second is **correction energy**. This is an identity, not a statistical model and not a prime-number theorem.

## 3. Dataset 003 decomposition

| Family | MSE gain | Alignment `2E[e_c d]` | Correction energy `E[d²]` | Alignment / energy |
|---|---:|---:|---:|---:|
| overall | 0.0043848996 | 0.0083464404 | 0.0039615408 | 2.1069 |
| `x^(1/2)` | -0.0096869635 | -0.0032291680 | 0.0064577955 | -0.5000 |
| `x^(2/3)` | 0.0108128318 | 0.0139406431 | 0.0031278114 | 4.4570 |
| `x^(3/4)` | 0.0120288306 | 0.0143278461 | 0.0022990155 | 6.2322 |

The shortest-window failure is stronger than “the signal is noisy.” The fitted correction has negative alignment and the largest energy penalty. At the longer scales, alignment is positive and correction energy is smaller.

The alignment itself splits exactly as

```text
2E[e_c d] = 2Cov(e_c,d) + 2E[e_c]E[d].
```

At `x^(1/2)`, the covariance part is negative. At the longer scales it is positive and dominates the penalty.

## 4. Which feature group drives the scale change?

The primary correction was reconstructed exactly from four groups:

1. shift in the three classical coefficients;
2. lagged von Mangoldt features;
3. character-weighted von Mangoldt features;
4. reduced-residue energy features.

The maximum reconstruction error was below `3e-15`.

The lagged-Lambda group has the largest correction variance and carries the main scale change:

| Family | Lagged-Lambda alignment | Lagged-Lambda self-energy | Corr(classical error, Lambda correction) |
|---|---:|---:|---:|
| `x^(1/2)` | -0.001349 | 0.004846 | -0.0137 |
| `x^(2/3)` | 0.008277 | 0.001692 | 0.2023 |
| `x^(3/4)` | 0.010242 | 0.001114 | 0.3662 |

All six frozen lagged-Lambda coefficients are negative. Thus the model is not exploiting positive persistence. It is converting past weighted excess into a downward correction and past weighted deficit into an upward correction.

## 5. Adjacent von Mangoldt increments

Define the adjacent centered increments

```text
A_h(x) = psi(x-1) - psi(x-h-1) - h
B_h(x) = psi(x+h-1) - psi(x-1) - h.
```

They satisfy the pointwise identity

```text
2 A_h(x) B_h(x)
  = (A_h(x)+B_h(x))^2 - A_h(x)^2 - B_h(x)^2.
```

Dataset 003 gave negative adjacent covariance in every scale family:

| Family | Cov(`A_h`,`B_h`) | Corr(`A_h`,`B_h`) | Mean `A_h B_h/(h log x)` |
|---|---:|---:|---:|
| `x^(1/2)` | -2,658.7531 | -0.0533 | -0.01261 |
| `x^(2/3)` | -61,341.7943 | -0.1317 | -0.02627 |
| `x^(3/4)` | -356,217.3861 | -0.2489 | -0.04558 |

This corrects the earlier language of “local memory.” The observed arithmetic pattern is **adjacent anti-persistence**.

The longer-window model gains are compatible with using negative coefficients against a more pronounced negative adjacent relation. The shortest family fails because the learned correction is too energetic and insufficiently aligned with the prime-count residual after the classical baseline.

## 6. Variance-to-covariance bridge

For

```text
E_h(x) = psi(x+h) - psi(x) - h,
```

we have exactly

```text
E_(2h)(x) = E_h(x) + E_h(x+h)
```

and hence

```text
2 E_h(x)E_h(x+h)
  = E_(2h)(x)^2 - E_h(x)^2 - E_h(x+h)^2.
```

After integration over a common domain, this turns adjacent covariance into a difference of three short-interval second moments. It is the correct analytic bridge to the Selberg-type variance problem.

Montgomery and Soundararajan developed evidence that `psi(x+H)-psi(x)` is approximately normal with variance of order `H log(N/H)` for power-sized short intervals. Bui, Keating, and Smith formulate the fixed-length variance

```text
∫[psi(x+h)-psi(x)-h]^2 dx
```

and summarize its connection to pair correlation; they also record a more precise conditional asymptotic in a restricted range. Goldston's notes and Chan's work describe the load-bearing connection between short-interval second moments and pair correlation of zeta zeros.

Primary references:

- H. L. Montgomery and K. Soundararajan, *Primes in short intervals*, arXiv:math/0409258, related DOI `10.1007/s00220-004-1222-4`.
- D. A. Goldston, *Notes on Pair Correlation of Zeros and Prime Numbers*, arXiv:math/0412313.
- T. H. Chan, *More precise pair correlation of zeros and primes in short intervals*, arXiv:math/0206292.
- H. M. Bui, J. P. Keating, D. J. Smith, *On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class*, arXiv:1506.03741.

If one assumes a stable variance law of the schematic form

```text
J(X,h) ~ h X [log(X/h) + C]
```

and negligible shift/boundary differences, the exact doubling identity predicts

```text
Cov(adjacent h-increments) ~ -h X log 2.
```

This last statement is a **conditional heuristic/consequence of the variance asymptotic**, not an unconditional project theorem.

## 7. What PVG contributes here

PVG does not currently improve the classical variance theorem. Its useful role is organizational and diagnostic:

- prime detection is a support-one event in valuation space;
- lagged small-prime and residue observables define geometric coordinate summaries;
- the correction-gain identity tests whether these summaries align with the unresolved analytic residual;
- the failure at `x^(1/2)` identifies a scale where the chosen geometric summary consumes more correction energy than it earns in alignment.

The missing certificate is therefore not “more features.” It is a theorem controlling the covariance between a future prime-count residual and past weighted/residue observables uniformly in `h=x^theta`.

## 8. Honest classification

```text
Exact algebraic identity: PROVED
Adjacent-increment square identity: PROVED
Dataset 003 scale heterogeneity: COMPUTATIONAL DIAGNOSTIC
Adjacent Lambda anti-correlation: COMPUTATIONAL DIAGNOSTIC
Variance-to-anticorrelation transfer: CONDITIONAL PROOF STRATEGY
Uniform covariance estimate for prime-count residuals: MISSING CERTIFICATE
New theorem about primes: NONE
RH/GRH progress: NONE
```

## 9. Next action

The next formal unit should prove the two algebraic identities in Lean over finite sums/reals. The next analytic unit should define a continuous or averaged covariance functional and audit exactly which known second-moment assumptions imply its sign and size.

Do not start Dataset 004 before those two units are closed.
