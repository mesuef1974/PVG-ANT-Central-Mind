# RMG-004-A — Sieve Objects, Levels of Distribution, and Certificate Separation Graph

**Status:** COMPLETED  
**Branch:** `agent/pvg-axis-sum-continuation-002`  
**Verification:** `PASS 8/8`  
**Scientific classification:** standard sieve knowledge + exact PVG visibility bridge + computational regression + claim-boundary enforcement

## Purpose

Integrate the repository's mature Harman / Opera de Cribro / PVG-sieve material into the executable Research Memory Graph without creating a parallel sieve ontology.

The unit reuses `BRIDGE-SIEVE-INFORMATION-001` as its governing translation:

- pointwise divisibility indicators through level `D`;
- truncated valuation profiles;
- aggregation to `A_d`;
- information loss after aggregation;
- certificate separation.

## Core objects

For a weighted sequence `A=(a_n)`, the divisibility aggregate is

\[
A_d=\sum_{d\mid n}a_n.
\]

For a set or sequence sieved by primes below `z`, the sifted condition is pointwise equivalent to

\[
v_p(n)=0\qquad(p<z).
\]

At finite visibility level `D`, the profile

\[
\nu^{(D)}(n)=
\left(
\min\left(v_p(n),\left\lfloor\frac{\log D}{\log p}\right\rfloor\right)
\right)_{p\le D}
\]

contains exactly the same pointwise divisibility information as all indicators `1_{d|n}` for `d<=D`.

## What is exact

The following is an exact finite bidirectional translation:

```text
pointwise divisibility indicators through D
<->
truncated valuation profile nu^(D)(n)
```

It preserves visible divisibility data.

The following map is not generally injective:

```text
pointwise weighted profiles
->
aggregate values A_d
```

## Explicit aggregation-kernel witness

On support

\[
\{1,2,3,6\}
\]

with weights

\[
(1,-1,-1,1),
\]

we obtain

\[
A_1=A_2=A_3=0,
\qquad
A_6=1.
\]

Thus observations restricted to `d=1,2,3` cannot recover the pointwise sequence. The lost information can include sign, phase, ordering, correlations, and target purity.

## Certificate ladder

The unit records the following distinct certificate classes:

1. **Pointwise visibility certificate** — which divisibility coordinates are visible.
2. **Aggregate remainder certificate** — which weighted sums over moduli are controlled and in what norm.
3. **One-sided sieve certificate** — upper or lower bound only.
4. **Sifted-set asymptotic certificate** — asymptotic for the sifted object.
5. **Prime-producing asymptotic certificate** — target purity and prime production.

The governing non-equivalences are

```text
one-sided sieve certificate
!=
sifted-set asymptotic certificate
!=
prime-producing asymptotic certificate
```

No promotion is permitted without matching hypotheses and evidence.

## Level of distribution

A level-of-distribution statement is represented as aggregate control over moduli up to a scale `D`, with mandatory metadata:

- target sequence;
- main-term/local-density model;
- modulus range;
- remainder norm;
- weights;
- uniformity parameters;
- sign or one-sided status.

In PVG language it measures the reliable depth of aggregated residue/divisibility channels. It is not a pointwise prime guarantee.

## Parity boundary

The parity barrier is recorded as a limitation of the available aggregate certificate channel. Exact PVG encoding of factorization does not automatically create a statistic capable of isolating primes from almost-primes of opposite factor-parity.

Therefore:

```text
representation completeness
!=
analytic discrimination power
```

This unit makes no claim of progress on the parity problem.

## Type I / Type II interface

Type I and Type II information is registered as distinct structured estimates:

- Type I: linear/one-variable distribution control;
- Type II: bilinear correlation and cancellation control.

The labels alone are not certificates. Each use must name the exact sum, ranges, coefficients, and bound.

## Computational verification

The executable harness checks:

- registry schema and unique IDs;
- equivalence of truncated profiles and all divisibility indicators for `D=12`, `1<=n<=300`;
- the explicit nontrivial aggregation kernel;
- equality of direct and PVG sifted-set definitions on `1<=n<=500`, `z=11`;
- presence of certificate separation records;
- mandatory rejection of level-of-distribution -> prime production;
- mandatory rejection of PVG visibility -> parity solution.

Result:

```text
PASS 8/8
```

## Assimilation state

```text
sifted-set object                         = L3
finite truncated visibility equivalence  = L5
aggregation-kernel diagnostic            = L5
certificate separation discipline        = L5
level-of-distribution dependency          = L3
Type I / Type II interface               = L2
parity barrier translation               = L2
Lean proof added                         = none
L6 promotion                             = not authorized
```

## Claim ceiling

This unit adds no:

- new sieve asymptotic;
- prime-producing theorem;
- improvement to a level of distribution;
- solution or progress certificate for the parity problem;
- Goldbach result;
- RH or GRH result.

## Files

- `registry/sieve-objects-levels-certificates.jsonl`
- `code/verify_rmg_004_a.py`
- `results/rmg_004_a_verification.json`
- `units/RMG-004-A.md`

## Next unit

```text
RMG-004-B
Sieve Weights, Fundamental Lemma,
Upper/Lower Bound Functions, and Remainder-Norm Graph
```
