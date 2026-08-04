# IGD001 — Pre-Run Specification

```text
STATUS =
  TRANSCRIBED-AFTER-EXECUTION-FROM-TIMESTAMPED-PRE-RUN-CONVERSATION

REPOSITORY-FREEZE =
  NOT-PERFORMED-BEFORE-RUN

PARAMETERS-CHANGED-AFTER-DATA =
  NO, ACCORDING-TO-SESSION-RECORD
```

This file is **not** a repository freeze certificate. The protocol below was fixed in the
working session before any number was computed, but it entered the repository only after
execution. Anyone auditing this pass should treat the pre-registration claim as resting on
the session record, not on a Git timestamp.

## 1. Purpose and non-purpose

Purpose: detect order-one transcription, sign, or coefficient corruption in the constants
that later derivation work would rest on.

Non-purpose: this experiment does **not** certify decimal places, does not verify the
theorem, does not read the primary texts, and does not attempt the Ingham gate.

## 2. Target and reference constants

```text
K_star = 2(2 gamma - 1 - 2 zeta'(2)/zeta(2)) = 2.5887066320...
a_0    = 6/pi^2 = 0.6079271018540...
```

`a_1(h)` status at time of run: `DERIVED / CROSS-CONSISTENT-WITH-TAO / PENDING-PRIMARY-TEXT`.
Primary texts (Ingham 1927 `10.1112/jlms/s1-2.3.202`; Estermann 1931
`10.1515/crll.1931.164.173`; Estermann 1932 correction `10.1515/crll.1932.166.64`;
Motohashi 1994) were **not** read before the run and remain unread.

## 3. Phase 1 — h = 1 only

```text
Y_1(x)        = D_1(x)/x - a_0 log^2 x
Khat(x1,x2)   = [Y_1(x2) - Y_1(x1)] / (a_0 log(x2/x1))
```

Judgment family (three estimators, moving both endpoints):

```text
Khat(1e6,1e10)   primary
Khat(1e7,1e10)   probes low-end pre-asymptotic contamination
Khat(1e6,1e9)    probes upper-endpoint stability
U_K^judgment = max - min over that family
```

`U_K` is tagged `OPERATIONAL / INTERNAL-TO-PREREGISTERED-ESTIMATORS`,
`NOT-A-CONFIDENCE-INTERVAL`, `NOT-A-THEORETICAL-ERROR-BOUND`.

Drift diagnostic, reported separately and **not** entering `U_K`:

```text
Khat(1e6,1e7), Khat(1e7,1e8), Khat(1e8,1e9), Khat(1e9,1e10)
d_j = |Khat(1e j,1e j+1) - K_star|
acceptance signal: d_9 < d_6, and no two consecutive rises at the end of the sequence
```

Strict monotonicity `d_6 > d_7 > d_8 > d_9` was explicitly **rejected** as a criterion
before the run, because a crossing of `K_star` would break it spuriously.

## 4. Reference scenarios (frozen before run)

| scenario | K |
|---|---|
| CLAIMED | +2.5887 |
| Z-TERM-OMITTED | +0.3089 |
| Z-COEFFICIENT-HALF | +1.4488 |
| Z-SIGN-REVERSED | −1.9710 |

No scenario may be added after seeing the data and then claimed as discriminated.

## 5. Phase 2 — blinded shift set

Opened **only** on verdict `K-H1-DATA-CONSISTENT`.

```text
blinded shifts h in {2, 6, 12, 30}
prediction    R_h(x) = sigma_{-1}(h) - 4 sigma'_{-1}(h)/log x + O(1/log^2 x)
slope test    M_h(x1,x2) -> -4 sigma'_{-1}(h)
second order  Q_h -> 2 K rho_h + 4 tau_h
```

| h | sigma_{-1}(h) | sigma'_{-1}(h) | rho_h | tau_h |
|---|---|---|---|---|
| 2 | 3/2 | 0.34657359 | 0.23104906 | 0.16015100 |
| 6 | 2 | 1.01140427 | 0.50570213 | 0.58880491 |
| 12 | 7/3 | 1.56505341 | 0.67073718 | 0.93112554 |
| 30 | 12/5 | 1.85746029 | 0.77394178 | 1.29181871 |

Calibration shifts `h in {3,4,5,8}` were provided for in the protocol but were **not**
needed and were **not** run, because the tolerance was ultimately defined operationally
from the estimator spread rather than calibrated empirically. This deviation is recorded
here rather than silently dropped.

## 6. Computational registration

```text
X_max        = 1e10
checkpoints  = 1e6, 1e7, 1e8, 1e9, 1e10
segment size = 1e6
language     = C (gcc), OpenMP, release optimisation
integer type = uint64 sums (D_1(1e10) ~ 3.6e12, far below 2^64)
validation   = independent O(x log x) divisor count at x = 1e6
```

## 7. Verdict vocabulary (frozen before run)

```text
K-H1-DATA-CONSISTENT
K-H1-DATA-INCONSISTENT
K-H1-INSUFFICIENT-RANGE
K-H1-IMPLEMENTATION-ERROR-SUSPECTED
```

A numerical pass never promotes `PENDING-PRIMARY-TEXT` to `PRIMARY-VERIFIED`.

## 8. Standing dated prediction

```text
PVG-CONTRIBUTION = NOT-SHOWN   (dated 2026-08-04, before any computation)
```

Rationale recorded in advance: stratifying the pair of divisor boxes by the meet `u AND v`
appears equivalent to the classical grouping by `g = (a,b)`, so the lattice picture is
expected to reproduce an existing step rather than produce a new one. This prediction is
only discharged by an estimate, saving, or error-splitting that does not reduce literally
to setting `g = (a,b)`.
