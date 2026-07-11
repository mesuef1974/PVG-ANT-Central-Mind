# Dataset 003 Closure Review

**Closure ID:** `CLOSE-PVG-LPD-DATASET003-001`  
**Protocol:** `PVG-LPD-DATASET-003-PROTOCOL-001`  
**Execution branch:** `agent/local-prime-density-dataset003-execution`  
**Decision:** `CLOSE DATASET 003 — PASS`  
**Scientific result:** `UNRESOLVED IN INDEPENDENT REPLICATION`

## Closure gates

| Gate | Result |
|---|---|
| Protocol merged before data generation | PASS |
| Independent numerical range `[10^7,10^8)` | PASS |
| 480 frozen windows, 160 per family | PASS |
| Deterministic segmented sieve | PASS |
| Dataset 001 and 002 training sources rebuilt | PASS |
| Dataset 003 schema verification | PASS |
| Same-window leakage guard | PASS |
| Frozen alphas and feature families | PASS |
| Python confirmatory analysis | PASS |
| Independent R analysis | PASS |
| Python/R agreement | PASS |
| Committed result matches regenerated output | PASS |
| Generated artifact uploaded | PASS |
| Promotion rule respected | PASS |

## Reproduction evidence

GitHub Actions run:

```text
29164273761
```

Tested head:

```text
93d6c628b9562dbfd9e08e204196a84d82d02bb8
```

Artifact:

```text
id     = 8251699912
digest = sha256:9fd56a0b99b198e44ebeaa73fb3bf36b69a5e3d40425e1d7c76cec23a493c889
```

All workflow steps completed successfully, including the committed-result verification gate.

## Governing numerical result

```text
Classical RMSE = 0.5305422949233406
Primary RMSE   = 0.5263936046962887
Delta          = 0.004148690227051888
95% CI         = [-0.0015440013059201756, 0.010035743817573954]
P(Delta > 0)   = 0.921
```

Family deltas:

```text
x^(1/2)   = -0.007361036848689828
x^(2/3)   =  0.01100110326931758
x^(3/4)   =  0.014884114272684157
```

The bootstrap lower bound is not positive and family stability fails. Therefore promotion is forbidden by the frozen protocol.

## Honest classification

```text
UNRESOLVED IN INDEPENDENT REPLICATION
```

This means:

- Dataset 002's exploratory signal was not independently confirmed;
- the point estimate remains mildly positive overall;
- the effect is scale-dependent and reverses for `h=x^(1/2)`;
- no replicated candidate signal exists.

## Scientific ceiling

- no theorem;
- no proof strategy validated by the experiment;
- no claim that PVG predicts local prime counts;
- no RH/GRH progress;
- no promotion from diagnostic to mechanism.

## Next action

Open a separate **Scale-Heterogeneity Diagnostic and Proof-Strategy Pass**. Do not start Dataset 004 or retune the failed model before that analytic pass identifies a precise covariance object, a classical comparison theorem, and a missing certificate.

## Closure decision

```text
CLOSE DATASET 003 — PASS
LOCAL PRIME DENSITY FRONT — REMAINS OPEN
NEXT ACTION — SCALE-HETEROGENEITY DIAGNOSTIC
```
