# BRIDGE-SIEVE-INFORMATION-001

**Family:** sieve visibility / aggregation / certificates  
**Maturity:** L2 analytic diagnostic  
**Classification:** Exact pointwise bridge plus aggregation-loss diagnostic

## Classical object

Divisibility indicators through level `D`, Type-I family sums, sieve main terms, and remainders.

## PVG object

The truncated profile

\[
\nu^{(D)}(n)=
\left(
\min\left(v_p(n),\left\lfloor\frac{\log D}{\log p}\right\rfloor\right)
\right)_{p\le D}
\]

followed by a pushforward from pointwise profiles to aggregate data.

## Exact forward map

The pointwise indicators `1_{d|n}`, `d≤D`, and `ν^(D)(n)` contain the same visible divisibility information.

For a sequence `(a_n)`, the aggregate

\[
A_d=\sum_{d\mid n}a_n
\]

is a further map and need not be injective.

## Reverse map and information loss

All pointwise indicators recover the truncated profile. Aggregate `A_d` values generally lose individual profiles, sign, phase, ordering, correlations, and target purity.

## Analytic transform

A usable sieve certificate must name the sequence, main-term model, weights, sieve level, remainder norm, and sign/one-sided status. A sifted-set certificate is not a prime-producing certificate.

## Simplification gain

**Analytic diagnostic:** locates exactly where information is lost before assigning a parity or distribution wall.

## Finite counterexample

`EX-SIEVE-LOSS-001`: on `{1,2,3,6}`, weights `(1,-1,-1,1)` are invisible to aggregates at `d=1,2,3` but visible at `d=6`. Thus low-level aggregate data has a nontrivial kernel.

## Research use

Highest-priority language bridge for future information-deficiency lemmas. It is not itself a solution to the parity problem.

## Sources

Harman, Opera de Cribro, PVG-Sieve-Interface reconciliation.
