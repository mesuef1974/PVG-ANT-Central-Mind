# Scale-Heterogeneity Closure Review

**Review ID:** `PVG-LPD-SCALE-HETEROGENEITY-CLOSURE-001`  
**Decision:** `CLOSE — PASS AS DIAGNOSTIC, NOT AS MECHANISM`

## Gates

| Gate | Result |
|---|---|
| Parent Dataset 003 is frozen, reproduced, and closed | PASS |
| Analysis rebuilds from certified Dataset 003 outputs | PASS |
| Finite correction-gain identity checked | PASS |
| Correction reconstructed from frozen coefficient groups | PASS |
| Adjacent increment identity checked with declared mixed tolerance | PASS |
| Committed certificate equals regenerated certificate | PASS |
| Exact, empirical, conditional, and missing-certificate layers separated | PASS |
| PVG necessity/originality ceiling explicit | PASS |
| Dataset 004 remains unauthorized | PASS |
| No RH/GRH or theorem promotion | PASS |

## Numeric repair

The former absolute-only check was invalid for the large adjacent-square computation. The repaired check records:

```text
maximum adjacent absolute error = 1.862645149230957e-09
maximum adjacent relative error = 3.7473279654308245e-14
relative tolerance              = 5.684341886080802e-14
```

The error is within the declared float64 mixed criterion. No exact-zero numerical claim remains.

## Scientific finding

The frozen correction is scale heterogeneous: harmful at `x^0.5`, helpful in point estimate at `x^0.666667` and `x^0.75`. Adjacent centered von Mangoldt increments have negative empirical covariance in all three tested families. This is evidence about the frozen dataset and model only.

The exact second-moment identity provides a route to a shifted Selberg covariance question, but the needed uniform variance, shift, boundary, and weighted-to-unweighted certificates are absent. **PVG necessity is not established.**

## Closure effect

- The local-prime-density scale pass is closed.
- It is not promoted to Candidate Mechanism.
- The covariance question is retained as an inactive candidate for targeted literature/assumption audit.
- Dataset 004 remains unauthorized.
- The active operational goal advances to `GOAL-OP-LANGUAGE-KERNEL-V1-001`.
