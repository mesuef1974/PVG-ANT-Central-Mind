# VRP001 Closure Review 001

**Research front:** `PVG-LOCAL-PRIME-DENSITY-001`  
**Vertical pass:** `Central Mind Vertical Research Pass 001`  
**Decision:** `CLOSE VRP001 — PASS`  
**Research-front status:** remains open for independent replication; this closure does not claim a theorem or confirmed signal.

## Scope closed

- Dataset 001 construction, verification, analysis, report, and certificate.
- Dataset 002 leakage-controlled construction, verification, analysis, report, and certificate.
- Repair Pass 001 for review feedback, reproducibility, and classification consistency.
- Book-catalog audit accompanying the pull request.

## Reproduction evidence

GitHub Actions workflow `VRP001 Reproduction` executed on the pull-request merge reference:

- run id: `29160013786`
- job id: `86563374150`
- merge reference: `5910183a3adb8625fb22f97e8a685676819e7d50`
- tested head: `04ac4903174bf3a3e876e1369786408d60a07faf`
- tested base: `501d693f417c2711f6f8d4c410fb9bd231ec573f`
- conclusion: `success`

Successful gates:

1. Install Python dependencies.
2. Build Dataset 001.
3. Verify Dataset 001.
4. Analyze Dataset 001 in Python.
5. Build Dataset 002.
6. Verify Dataset 002.
7. Analyze Dataset 002 in Python.
8. Set up R.
9. Analyze Dataset 001 in R.
10. Analyze Dataset 002 in R.

Because GitHub checked out `pull/1/merge`, this validates the research branch combined with the then-current `main`, including the independent Lean additions on the base branch.

## Scientific decisions

### Dataset 001

`NEGATIVE DIAGNOSTIC / UNRESOLVED`

The elementary VSDS divisibility-boundary features do not improve held-out prediction beyond the classical baseline in the tested protocol.

### Dataset 002

`UNRESOLVED WITH EXPLORATORY UNADJUSTED SIGNAL`

- The predeclared lowest-RMSE lagged-Lambda model has a bootstrap interval crossing zero.
- The residue-energy model passes an unadjusted rule.
- Across four nonclassical families, Bonferroni and Holm adjusted values are `0.08`.
- No model is promoted to `Candidate Signal`.

## Reproducibility and integrity

- Dataset 001 builder matches the original dataset exactly.
- Dataset 002 builder matches the original schema and nonnumeric fields; maximum numeric difference is below `9e-16`.
- Full datasets are regenerated deterministically from committed source.
- Python verifiers use explicit exceptions.
- R scripts fail fast on missing feature groups, vector-length mismatch, and non-finite values.
- External Excel/ZIP convenience artifacts remain outside Git; their SHA-256 values are recorded in `ARTIFACTS.md`.

## Review findings

All actionable review findings in scope were addressed:

- empty feature-group detection;
- safe R metrics;
- explicit Python verification failures;
- clean-checkout dataset generation;
- R path resolution under CI;
- multiple-comparison correction;
- repair of the Dataset 002 classification.

## Scientific ceiling

- No new theorem.
- No confirmed Candidate Signal.
- No RH/GRH progress.
- No claim that PVG predicts local prime counts.

## Next action after merge

Freeze the Dataset 003 protocol before generating any new test data. Dataset 003 should be an independent replication on a higher numerical range, with a small predeclared model set and a native residue-class target such as

\[
\psi(x+h;q,a).
\]

The merge closes the first vertical pass as a reproducible negative/unresolved research result; it does not close the local-prime-density research front.
