# ENGINE-005 Local-Neighborhood Incremental-Information Pilot

```text
Readiness ID: ENGINE-005-LOCAL-NEIGHBORHOOD-INCREMENTAL-INFORMATION-PILOT-001
Parent: GOAL-PVG-INVERSE-GEOMETRY-001
Status: PREPARED_NOT_ACTIVE
Date: 2026-07-22
Prerequisite: close or explicitly suspend ENGINE-004 PASS-004
Phase D: NOT AUTHORIZED
```

## Research question

After exact matching of declared center residue information, does neighborhood information outside that matched residue basis improve finite held-out discrimination between primes and difficult composites?

## Exact negative control

For local primes `L` and offsets `K`, the mask

\[
(1_{\ell\mid x+k})_{\ell\in L,k\in K}
\]

is determined by `(x mod ell)_{ell in L}`. Therefore it is a mandatory negative control and must not improve over the center-residue baseline.

## Pilot population

The pilot must use odd centers only and exclude the center from all neighborhood features.

Two labels:

```text
P: proved primes in the declared finite interval
C: proved composites with no prime divisor <= P_match
```

The composite class must not be dominated by easy small-factor examples. Preferred subclasses:

- semiprimes with both factors above `P_match`;
- composites surviving trial division through `P_match`;
- size-matched Carmichael or strong-pseudoprime examples when available in range.

## Deterministic split

Use disjoint numerical intervals, not random row splitting:

```text
train interval
validation interval
held-out test interval
```

No center, neighbor, or translated copy may cross from one split into another within the maximum radius `h_max`.

## Matching

Within every split, match prime and composite centers by:

1. narrow magnitude bin;
2. exact residue class modulo

\[
M_{match}=\prod_{p\le P_{match}}p^{a_p};
\]

3. identical parity, with all centers odd;
4. identical declared center feature vector.

Unmatched samples are discarded, not imputed.

## Nested feature sets

```text
B0 = magnitude bin only
B1 = B0 + matched center residue / truncated valuation data
B2 = B1 + neighborhood data generated only by the same matched moduli
B3 = B1 + genuinely new neighborhood data outside the matched basis
```

Examples permitted in `B3`:

- least detected prime factor of `x+k` above `P_match`, censored at `P_probe`;
- truncated valuations for probe primes in `(P_match,P_probe]`;
- proved prime/composite status of selected neighbors, never the center;
- support-size shadows of neighbors using probe factors above `P_match`;
- multi-radius summaries using only the permitted probe information.

## Leakage prohibitions

Forbidden features include:

- any divisibility, valuation, factor, probable-prime, or prime label of the center;
- any transformation from which the center's factorization or primality label is directly recoverable;
- complete factorization of neighbors when only censored probe information is declared;
- sampling or feature normalization using the held-out labels;
- random splitting that places adjacent centers across train and test.

## Evaluation

Primary statistic:

\[
\Delta=AUC(B3)-AUC(B1)
\]

on the untouched held-out interval.

Also report:

- balanced accuracy;
- log loss or Brier score;
- confidence interval by block bootstrap over center intervals;
- permutation-label null distribution;
- stability across at least three choices of `(h,P_match,P_probe)`.

The mandatory validity condition is:

```text
B2 and B1 are prediction-equivalent up to numerical tolerance.
```

If not, stop and diagnose leakage or incorrect residue matching.

## Decisions

```text
PROMOTE_DIAGNOSTIC:
  B3 beats B1 on the held-out interval, survives permutation and parameter changes,
  and the gain cannot be reconstructed from omitted center residues.

NULL_RESULT:
  no stable held-out gain over B1.

INVALID_EXPERIMENT:
  B2 beats B1, split leakage exists, matching fails, or the center label leaks.
```

A positive pilot remains `FINITE-VERIFIED / DIAGNOSTIC`. It does not establish a deterministic primality test, asymptotic law, or complexity improvement.

## Current authorization

This card prepares the experiment only. Execution is not active until ENGINE-004 PASS-004 is closed or explicitly suspended by a separate governance decision.