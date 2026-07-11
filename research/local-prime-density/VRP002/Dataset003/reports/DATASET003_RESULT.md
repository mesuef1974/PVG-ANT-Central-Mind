# Dataset 003 — Independent Replication Result

**Protocol:** `PVG-LPD-DATASET-003-PROTOCOL-001`  
**Execution status:** reproducible Python/R pass  
**Scientific decision:** `UNRESOLVED IN INDEPENDENT REPLICATION`  
**Promotion:** no

## 1. Independent sample

- numerical range: `10,000,000 <= x < 100,000,000`;
- 480 frozen windows;
- 160 windows for each of `theta = 1/2, 2/3, 3/4`;
- 147 generated columns;
- exact segmented sieve to `99,999,999`;
- primes generated: `5,761,455`;
- von Mangoldt support points: `5,762,859`.

Dataset SHA-256:

```text
cce7968b95d4ebc18dcc7d3890400e17f753295c973994bceb4695cef78775d8
```

## 2. Frozen model results

| Model | Features | Alpha | RMSE | MAE | R² |
|---|---:|---:|---:|---:|---:|
| Classical Ridge | 3 | 300 | 0.5305422949 | 0.4143279764 | -0.0155225945 |
| Primary Lambda + characters + residue energy | 66 | 3000 | 0.5263936047 | 0.4090163144 | 0.0002975055 |
| Secondary lagged Lambda | 9 | 1000 | 0.5275129509 | 0.4084956115 | -0.0039586364 |

The primary overall RMSE improvement was

```text
Delta = 0.0041486902
```

which is approximately `0.78%` of the classical RMSE.

## 3. Frozen bootstrap

The predeclared 10,000-replicate paired stratified bootstrap gave

```text
95% interval = [-0.0015440013, 0.0100357438]
median       =  0.0041767723
P(Delta > 0) =  0.9210
```

The lower endpoint is not positive. Therefore the confirmatory uncertainty condition failed.

## 4. Family stability

| Window family | Classical RMSE | Primary RMSE | Delta |
|---|---:|---:|---:|
| `h = x^(1/2)` | 0.6543085467 | 0.6616695836 | -0.0073610368 |
| `h = x^(2/3)` | 0.4969436146 | 0.4859425114 | 0.0110011033 |
| `h = x^(3/4)` | 0.4115249077 | 0.3966407934 | 0.0148841143 |

The candidate improved the two longer-window families but worsened the `x^(1/2)` family. The predeclared family-stability condition therefore also failed.

Because the overall bootstrap interval contains zero, the governing label is the protocol's unresolved label rather than the heterogeneous-pass label.

## 5. Cross-language certificate

Python and R agreed within `1e-7` on:

- all 480 responses;
- classical, primary, and secondary predictions;
- model metrics;
- family metrics;
- all bootstrap statistics;
- the final decision.

The largest reported prediction difference was below `7e-16`, and the bootstrap probability difference was exactly zero.

## 6. Scientific interpretation

Dataset 002's exploratory unadjusted signal did not satisfy the frozen independent replication rule.

The result is not a strong negative result because:

- the overall point estimate remains positive;
- the bootstrap probability of improvement is `0.921`;
- two of three predeclared scales improved.

But it is not a candidate signal because:

- the 95% interval crosses zero;
- the shortest-window family has negative improvement;
- the frozen promotion rule fails.

The honest interpretation is a scale-dependent pattern requiring analytic explanation, not another immediate model search.

## 7. Scientific ceiling

- no new theorem;
- no replicated candidate signal;
- no claim that PVG predicts local prime counts;
- no RH/GRH progress;
- the residue-class results remain secondary and descriptive.

## 8. Recommended next gate

Do not launch Dataset 004 immediately.

The next unit should be a **Scale-Heterogeneity Diagnostic and Proof-Strategy Pass** asking why past weighted activity behaves differently for

```text
h = x^(1/2), x^(2/3), x^(3/4).
```

Its output should be an analytic covariance decomposition, a literature-grounded barrier statement, and one or more precise lemmas that can be proved or formally checked.
