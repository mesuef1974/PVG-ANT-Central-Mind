# ENGINE-004 PASS-004 — Support-Conditioned Incidence Checkpoint

```text
Checkpoint ID: ENGINE-004-PASS-004-SUPPORT-CONDITIONED-INCIDENCE-001
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Program: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Decision: CHECKPOINT_PASS
Stage decision: return_to_engine_004_parent_review
Phase D: NOT AUTHORIZED
Date: 2026-07-23
```

## Frozen scope

```text
support prime limit = 11
support face sizes = 1,2,3
integer cap = 100000
support faces = 25
integer points = 884
represented points = 745
```

No cap, support, weighting, regression, significance-test, asymptotic, iterative, or phase expansion occurred.

## Certified finite outputs

```text
rank reversal inventory count = 4
matched-neighborhood witness count = 50
canonical point-record rows = 884
point-record SHA-256 = 2da8acb8cf35c66031afa8358fa405a0c63e79f27e1a374496e785f06b9378c1
```

Mandatory counterexamples were found:

```text
same exact support does not determine multiplicity
same support size does not determine multiplicity
same parity and decimal bin do not determine exact support
```

These are finite diagnostic witnesses only.

## Verification

Local verification at commit `b2d277be2c785b12bed9344447423e1cc3c3a36d`:

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

The certificate-comparison workflow initially failed only because it compared compact and pretty-printed JSON byte-for-byte. Commit `30836a99f2454d133bd3d1977ed7b4e50befbc2c` replaced that invalid byte-format comparison with semantic JSON equality.

Corrected CI:

```text
PVG Support-Conditioned Incidence Audit run 7 = SUCCESS
Governance Required Gate run 1002 = SUCCESS
PVG Centered-Radius Spectra Audit run 77 = SUCCESS
PVG Centered-Radius Incidence Audit run 47 = SUCCESS
PVG Inverse Prime Fibers Audit run 107 = SUCCESS
```

The unrelated `PVG Local Obstruction Geometry Audit` failure is outside this checkpoint and is not treated as PASS-004 evidence.

## Honest classification

```text
stratification definitions = IDENTITY
exact grouped arithmetic = FINITE-VERIFIED
counterexample witnesses = FINITE-VERIFIED
conditioned rank changes = DIAGNOSTIC
causal support effect = NOT ESTABLISHED
any general support law = OPEN
```

No original lemma or theorem, causal claim, general law, Goldbach/PNT/RH/GRH progress, or publication readiness is certified.

PASS-004 is closed. No PASS-005 is opened automatically.
