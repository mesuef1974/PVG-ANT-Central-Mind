# IGD001 — Result

Date: 2026-08-04. Front: `PVG-Additive` (still **not opened**).

## Verdicts

```text
K-H1 =
  DATA-CONSISTENT

C1-STAR =
  NUMERICALLY-CORROBORATED-AT-H1

FIRST-ORDER-ALONE =
  INSUFFICIENT-AT-XMAX-1E10

TWO-TERM-WITH-PREDICTED-Q =
  STRONGLY-DATA-CONSISTENT
  ZERO-FITTED-PARAMETERS

H-DEPENDENCE-SIGMA-SIGMAP-SIGMAPP =
  STRONGLY-CORROBORATED-ON-H={2,6,12,30}

THIRD-ORDER-INTERPRETATION =
  CONSISTENT-WITH-O(1/LOG^3-X)
  NOT-UNIQUELY-IDENTIFIED

M-H-ORIGINAL =
  UNFIT-AT-THIS-RANGE
  QUADRATIC-CONTAMINATION-IDENTIFIED

M-H-SECOND-ORDER-CORRECTED =
  POST-RUN-DIAGNOSTIC
  NOT-PART-OF-PREREGISTERED-VERDICT
  ALSO-UNFIT-AT-THIS-RANGE

OBSERVED-CONVERGENCE =
  MUCH-FASTER-THAN-CONSERVATIVE-EXPECTATION
  ERROR-EXPONENT-NOT-DETERMINED

INGHAM-GATE =
  NOT-ATTEMPTED

PVG-CONTRIBUTION =
  NOT-SHOWN
```

## 1. Raw data

Segmented divisor sieve, `X_max = 1e10`, segment `1e6`, 20 threads, 199 s.
Cross-validated at `x = 1e6` against an independent `O(x log x)` divisor count:
both give `D_1(1e6) = 137253454`.

| x | D_1 | D_2 | D_6 | D_12 | D_30 |
|---|---|---|---|---|---|
| 1e6 | 137253454 | 193727308 | 240214410 | 268030025 | 268701440 |
| 1e7 | 1827763836 | 2600743464 | 3255918570 | 3654961003 | 3675551922 |
| 1e8 | 23474766980 | 33609091666 | 42387205118 | 47799821509 | 48188469534 |
| 1e9 | 293165392748 | 421776367846 | 535043281868 | 605541958217 | 611686772934 |
| 1e10 | 3580291981124 | 5171317191902 | 6591079045034 | 7481279298497 | 7569597106188 |

## 2. Phase 1 — h = 1

`Y_1(x) = D_1(x)/x - (6/pi^2) log^2 x`:
21.219422, 24.841174, 28.464946, 32.088821, 35.712443.

Judgment family:

| estimator | Khat | dev from K_star |
|---|---|---|
| Khat(1e6,1e10) *primary* | 2.58840201 | −3.046e−04 |
| Khat(1e7,1e10) | 2.58876010 | +5.347e−05 |
| Khat(1e6,1e9) | 2.58831470 | −3.919e−04 |

`U_K^judgment = 4.4541e-04` (relative 1.72e−04), tagged
`OPERATIONAL / INTERNAL-TO-PREREGISTERED-ESTIMATORS`, not a confidence interval.

Drift diagnostic: `d_6 = 1.379e-03`, `d_7 = 6.52e-05`, `d_8 = 1.379e-04`, `d_9 = 4.27e-05`.
`d_9 < d_6` holds by a factor 32; there is one rise (`d_7 -> d_8`) but no two consecutive
rises. The pre-run decision to reject strict monotonicity is what saved the criterion here —
a strict test would have produced a spurious failure.

Reference scenarios, distance from the primary estimator: `Z-TERM-OMITTED` 2.2795,
`Z-COEFFICIENT-HALF` 1.1396, `Z-SIGN-REVERSED` 4.5594. All excluded by 2.5e3 to 1.0e4
times the estimator spread.

Second-order constant at h = 1: `C_1* = -0.8625768` predicted from the transcribed
`C_h*` formula versus `-0.8625592` measured — difference 1.8e−05.

## 3. Phase 2 — blinded shifts

Opened only after the h = 1 verdict, as specified.

| h | R_h(1e10) | first-order pred | rel | 3-term model | rel |
|---|---|---|---|---|---|
| 2 | 1.4443842 | 1.4397940 | +3.19e−03 | 1.4449907 | −4.20e−04 |
| 6 | 1.8409334 | 1.8243011 | +9.12e−03 | 1.8430621 | −1.15e−03 |
| 12 | 2.0895724 | 2.0614557 | +1.36e−02 | 2.0931301 | −1.70e−03 |
| 30 | 2.1142402 | 2.0773261 | +1.78e−02 | 2.1188552 | −2.18e−03 |

The first-order model alone deviates by 0.32 %–1.78 % at `X_max`. Every residual is
positive and decreases monotonically with x. The ratio of the observed residual to the
**predicted** second-order term `sigma_{-1}(h) Q_h / log^2 x` is

```text
h =  2 : 0.8833
h =  6 : 0.8865
h = 12 : 0.8877
h = 30 : 0.8889      spread = 0.0056
```

constant to 0.6 % across shifts whose second-order terms differ by a factor 8. The
h-dependence carried by `sigma_{-1}`, `sigma'_{-1}`, `sigma''_{-1}` is therefore strongly
corroborated on the tested shifts; the uniform 11 % shortfall is h-independent.
Extrapolating `Q_h(x)` linearly in `1/log x` from the last two checkpoints gives residuals
−1.33 %, −1.38 %, −1.36 %, −1.35 % against the predicted limits — again h-independent.

This shortfall is **consistent with** a neglected `O(1/log^3 x)` term but is not uniquely
identified by these five cumulative checkpoints.

## 4. Protocol defect found

The pre-registered slope estimator

```text
M_h(x1,x2) = [R_h(x2) - R_h(x1)] / [1/log x2 - 1/log x1]
```

does not measure what it was registered to measure at this range. With
`R_h(u) = s_h - 4 s'_h u + s_h Q_h u^2 + O(u^3)` the secant slope is
`-4 s'_h + s_h Q_h (u_1+u_2) + O(u^2)`, and at `u ~ 0.05` the quadratic contamination is
about 18 %:

| h | M_h(1e6,1e10) | M_h corrected | target −4 sigma'_{-1}(h) |
|---|---|---|---|
| 2 | −1.137276 | −1.456367 | −1.386294 |
| 6 | −3.135477 | −4.287446 | −4.045617 |
| 12 | −4.723579 | −6.668458 | −6.260214 |
| 30 | −5.406617 | −7.956597 | −7.429841 |

The raw estimator undershoots by ≈18 %; the post-run corrected estimator, which subtracts
`s_h Q_h (u_1+u_2)` using the **asymptotic** `Q_h`, overshoots by 5–7 % because `Q_h(x)`
has itself reached only ≈89 % of its limit at `1e10`. Neither form is usable here. The
correction is a post-run diagnostic and carries no verdict weight.

## 5. Integrity notes

- The tolerance was never frozen as a number; it was defined operationally as the spread of
  the pre-registered estimators, which came out at 1.7e−04. Imported literally into the
  shift test, that tolerance makes the **first-order model fail by two orders of magnitude**.
  The pass is obtained only by including the second-order term. Including it is legitimate
  because `Q_h = 2 K rho_h + 4 tau_h` was derived and recorded before the data existed —
  but the honest headline is "two-term model consistent", not "first-order model passed".
- A conservative pre-run guess of 1 %–3 % numerical uncertainty for the h = 1 test was wrong
  by two orders of magnitude in the conservative direction. That the observed convergence is
  much faster than the `x^{11/12}` exponent would suggest is recorded as an observation only;
  it does **not** determine the error exponent, and no claim about `x^{1/2}` is made.
- Calibration shifts `{3,4,5,8}` were declared in the protocol but never run, because the
  tolerance ended up defined from the estimator spread instead. Recorded, not dropped.
- Nothing in this computation used the PVG lattice. The dated prediction
  `PVG-CONTRIBUTION = NOT-SHOWN` stands undisturbed.
- No primary text was read. `a_1(h)` remains `PENDING-PRIMARY-TEXT`. A numerical pass never
  promotes that tag.

## 6. Related

Structural bridge [`BRIDGE-DIVISOR-BOX-CONVOLUTION-001`](../../../../../maps/bridges/BRIDGE-DIVISOR-BOX-CONVOLUTION-001.md).
Its maturity is unchanged by this pass; it already records that the divisor-box image alone
does not yield an asymptotic.
