# RMG-004-C — Type I / Type II Information, Bilinear Decomposition, and Level-of-Distribution Transfer Graph

**Status:** COMPLETED  
**Branch:** `agent/pvg-axis-sum-continuation-002`  
**Scientific class:** symbolic integration + finite computational regression  
**Claim ceiling:** no new Type I/II theorem, no level-of-distribution theorem, no prime-producing result, no parity-barrier progress.

## 1. Purpose

This unit integrates the existing Harman, Montgomery, Opera de Cribro, and PVG sieve interfaces into the executable Research Memory Graph. It does not create a parallel sieve ontology.

The governing distinction is:

```text
finite factor-pair identity
!=
uniform bilinear cancellation estimate
!=
level-of-distribution certificate
!=
prime-producing certificate
```

## 2. ANT objects

A Type I expression has one short or structurally simple factor variable. A Type II expression is genuinely bilinear, with both variables in intermediate ranges. Typical forms are

\[
\sum_m \alpha_m\sum_n \beta_n\,K(mn)
\]

with explicit ranges and coefficient norms.

A usable certificate must state:

- the decomposition identity;
- supports and variable ranges;
- coefficient norms;
- modulus family and range;
- main-term model;
- remainder norm;
- whether control is pointwise, averaged, upper-bound, or lower-bound.

## 3. PVG translation

Because

\[
\nu(mn)=\nu(m)+\nu(n),
\]

factor pairs become vector splittings

\[
w=u+v.
\]

Thus a finite bilinear sum may be reindexed exactly as a sum over pairs of valuation profiles whose vector sum lies in the target region. This preserves factorization bookkeeping, weights, and signs.

It does not create cancellation. Cancellation remains an analytic property of coefficients, phases, ranges, and averaging.

## 4. Information loss

After pushforward to residue or divisibility aggregates, the map is generally noninjective. It may lose:

- the original factor pairing;
- phase and sign;
- order;
- individual valuation profiles;
- correlations between the two factor populations;
- target purity.

Therefore aggregate distribution control cannot generally be inverted to recover the original bilinear structure.

## 5. Level-of-distribution transfer

A transfer from Type I/II estimates to a level of distribution is conditional on a complete proof route. The registry rejects transfer when any required range, norm, or uniformity condition is missing.

A level-of-distribution statement controls averaged residue errors relative to a named sequence and main term. It does not by itself distinguish primes from almost-primes and does not bypass the parity barrier.

## 6. Computational regression

The public harness checks:

1. registry count and unique identifiers;
2. an exact finite bilinear identity for explicit coefficient arrays;
3. the valuation splitting law on 2500 factor pairs;
4. computability of a finite residue-discrepancy norm for a toy sequence;
5. presence of object, identity, certificate, dependency, integration, loss, rejection, and boundary records;
6. explicit rejection of claim inflation;
7. preservation of the parity claim ceiling.

Recorded result:

```text
PASS 8/8
finite bilinear direct    = -18
finite bilinear regrouped = -18
valuation pairs checked   = 2500
finite toy discrepancy    = 9372.544025203495
```

The toy discrepancy is not a theorem about asymptotic distribution. It only confirms the executable definition and aggregation path.

## 7. Assimilation status

```text
finite bilinear identity and PVG reindexing = L5
valuation factor splitting regression       = L5
aggregation-loss diagnostic                 = L5
Type I / Type II conceptual graph           = L3
level-of-distribution transfer discipline   = L3
Vaughan/Harman decomposition dependency     = L2
parity and target-purity boundary            = L2
Lean proof added                            = none
L6 promotion                                = not authorized
```

## 8. Sources reused

- Harman sieve ledgers and installed tools;
- Montgomery distribution and large-sieve layers;
- Opera de Cribro certificate separation;
- `BRIDGE-SIEVE-INFORMATION-001`;
- `RMG-004-A` and `RMG-004-B`.

## 9. Negative benchmarks

Rejected:

```text
finite bilinear cancellation
=> uniform Type II estimate
```

Rejected:

```text
level of distribution
=> prime production
```

Rejected:

```text
exact PVG factor splitting
=> parity-barrier solution
```

## 10. Next unit

```text
RMG-004-D
Large Sieve, Bombieri–Vinogradov,
Average Distribution, and Certificate Transfer Boundary
```
