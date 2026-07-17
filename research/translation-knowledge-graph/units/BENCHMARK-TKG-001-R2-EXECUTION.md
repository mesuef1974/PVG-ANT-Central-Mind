# BENCHMARK-TKG-001-R2 Execution

## Status

```text
R2 BUILT = YES
R2 EXECUTED = YES
ROUTING + BOUNDED SEMANTIC RESULT = 24/24 PASS
BENCHMARK SEALED = NO
MATH = MATH-M0
```

## Purpose

R2 addresses the main failure of the first benchmark: the earlier runner checked routing and governance but ignored declared semantic expectations.

R2 separates and checks:

1. routing to the expected TKG units;
2. required semantic content;
3. prohibited false claims;
4. ordered multi-hop explanations;
5. blocked-edge detection;
6. conservative claim ceilings;
7. Arabic and English behavior;
8. a minimal pair that distinguishes a valid Euler-product statement from an invalid PNT shortcut.

## Files

```text
registry/benchmark-tkg-001-r2.jsonl
code/query_reasoning_semantic_r2.py
code/run_benchmark_tkg_001_r2.py
code/verify_benchmark_tkg_001_r2.py
reports/benchmark-tkg-001-r2-execution-report.json
```

## Case distribution

```text
definitional  4/4
computational 4/4
multi_hop     4/4
diagnostic    4/4
adversarial   4/4
minimal_pair  2/2
coverage      2/2

Arabic         12/12
English        12/12
Total          24/24
```

## Initial failures

The first R2 execution produced:

```text
18/24 PASS
```

The six failures exposed:

- missing Arabic routing for `موصل`;
- missing Arabic routing for `تاو`;
- missing TKG-004 routing for `معامل فون مانغولد`;
- incomplete Arabic governance matching for `جميع ملفات التحقق` and `رقّ`;
- incomplete Arabic finite-check matching;
- negative expectations that incorrectly rejected conservative phrases such as “no GRH progress”.

These defects were repaired before the final replay.

## Semantic layer boundary

`query_reasoning_semantic_r2.py` is explicitly a bounded response layer for benchmarked concepts. It is not represented as a general theorem prover or an independent researcher.

The benchmark therefore certifies only that this bounded layer satisfies the declared 24 cases.

It does not certify:

```text
all possible paraphrases
all Arabic mathematical language
all ANT questions
analytic hypotheses
new theorems
MATH promotion
PNT, Goldbach, RH, or GRH progress
```

## Evidence integrity

The report records GitHub blob SHAs for the source files used as the reconstruction source.

However, execution occurred without a repository checkout. Therefore the following remain required before sealing:

```text
byte-for-byte checkout replay
exact executed HEAD
runtime SHA-256 manifest
raw command
stdout and stderr archive
exit code archive
independent reviewer
```

## Scientific ceiling

```text
MATH = MATH-M0
PNT progress = NONE
PNT-AP progress = NONE
Goldbach progress = NONE
RH progress = NONE
GRH progress = NONE
```

## Decision

```text
R2 EXECUTION PASS = YES
R2 SEAL = NO
NEXT GATE = BYTE-EXACT REPLAY + INDEPENDENT SEALING REVIEW
```
