# ENGINE-004 PASS-004 — Support-Conditioned Incidence Diagnostics

```text
Goal: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Status: CHECKPOINT_PASS / CLOSED
Frozen box: unchanged
Phase D: NOT AUTHORIZED
```

## Question

After deterministic conditioning on integer size and parity route, does support size or exact support face retain any finite diagnostic separation in prime-fiber multiplicity and centered-radius incidence profiles inside the registered 884-point box?

This pass does not estimate a causal effect. It performs exact finite stratification and counterexample search only.

## Fixed strata

```text
decimal bins = 1-9, 10-99, 100-999, 1000-9999, 10000-99999, 100000
bit-length = floor(log2 N)+1
route = even / odd
support class = support size or exact support face
```

## Certified outputs

```text
integer points = 884
represented points = 745
rank reversal inventory count = 4
matched-neighborhood witness count = 50
canonical point-record rows = 884
point-record SHA-256 = 2da8acb8cf35c66031afa8358fa405a0c63e79f27e1a374496e785f06b9378c1
```

The required finite counterexamples were found:

```text
same exact support does not determine multiplicity
same support size does not determine multiplicity
same route and size bin do not determine exact support
```

These witnesses show non-determinacy inside the frozen box; they do not prove independence or causality.

## Matched-neighborhood rule

```text
same parity route
same decimal bin
different support size
minimum absolute integer distance
all ties retained
```

The 50 emitted witnesses satisfy this deterministic rule. They are descriptive finite comparisons, not causal estimates.

## Verification

Local verification at `b2d277be2c785b12bed9344447423e1cc3c3a36d`:

```text
Python syntax check = PASS
unit tests = 8/8 PASS
certificate generation = PASS
UTF-8 JSON parse = PASS
all registered points present = PASS
all spectra match PASS-002 = PASS
group counts reconstruct total = PASS
matched-neighborhood rule = PASS
claim ceiling = PASS
```

The first CI comparison failed because compact and pretty-printed JSON were compared byte-for-byte. Commit `30836a99f2454d133bd3d1977ed7b4e50befbc2c` corrected the workflow to compare parsed JSON objects.

Corrected CI:

```text
PVG Support-Conditioned Incidence Audit run 7 = SUCCESS
Governance Required Gate run 1002 = SUCCESS
PVG Centered-Radius Spectra Audit run 77 = SUCCESS
PVG Centered-Radius Incidence Audit run 47 = SUCCESS
PVG Inverse Prime Fibers Audit run 107 = SUCCESS
```

The unrelated Local Obstruction Geometry workflow failure is outside PASS-004.

## Classification

```text
stratification definitions = IDENTITY
exact grouped arithmetic = FINITE-VERIFIED
counterexample witnesses = FINITE-VERIFIED
conditioned rank changes = DIAGNOSTIC
support causes fiber richness = NOT ESTABLISHED
any general support law = OPEN
```

No regression, significance test, asymptotic law, Phase-D dynamics, Goldbach/PNT/RH/GRH progress, original theorem, or publication-readiness claim is made.

Checkpoint: `governance/checkpoints/ENGINE-004-PASS-004-SUPPORT-CONDITIONED-INCIDENCE-001.md`.

PASS-004 is closed. No PASS-005 is opened automatically.
