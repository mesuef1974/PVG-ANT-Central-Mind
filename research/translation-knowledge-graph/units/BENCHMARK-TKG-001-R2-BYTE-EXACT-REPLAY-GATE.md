# BENCHMARK-TKG-001-R2 — Byte-Exact Replay Gate

## Decision

```text
BYTE-EXACT CHECKOUT REPLAY = NOT EXECUTED IN CONNECTOR ENVIRONMENT
REASON = github.com DNS unavailable to local Git client
BENCHMARK SEALED = NO
```

The failed clone command returned:

```text
fatal: unable to access 'https://github.com/mesuef1974/PVG-ANT-Central-Mind.git/':
Could not resolve host: github.com
```

A connector-fetched reconstruction must not be mislabeled as a byte-exact Git checkout.

## Remediation added

The repository now contains:

```text
research/translation-knowledge-graph/code/replay_benchmark_tkg_001_r2.py
```

This harness must be executed from a clean, real Git checkout. It records:

- exact Git HEAD;
- working-tree status;
- SHA-256 of every executed file;
- Git blob SHA-1 of every executed file;
- Python/platform metadata;
- exact runner and verifier commands;
- complete stdout and stderr;
- exit codes;
- generated report hash;
- final replay status.

It produces:

```text
reports/benchmark-tkg-001-r2-byte-exact-report.json
reports/benchmark-tkg-001-r2-byte-exact-evidence.json
```

## Required command

From the repository root:

```bash
python research/translation-knowledge-graph/code/replay_benchmark_tkg_001_r2.py
```

The working tree must be clean unless `--allow-dirty` is explicitly supplied. A dirty-tree execution cannot be used for sealing without a separate justification.

## Seal conditions

R2 remains unsealed until all of the following hold:

1. replay is executed from a real checkout;
2. `overall_pass = true`;
3. runner and verifier exit codes are zero;
4. evidence records the exact HEAD and all source hashes;
5. evidence and generated report are committed without modifying executed sources;
6. an independent reviewer checks replay integrity and case adequacy.

## Scientific ceiling

```text
MATH = MATH-M0
PNT progress = NONE
PNT-AP progress = NONE
Goldbach progress = NONE
RH progress = NONE
GRH progress = NONE
```

A successful replay certifies only the declared routing and bounded-semantic cases. It does not certify a mathematical theorem, general reasoning competence, or MATH promotion.
