# Deferred TODO — Power-of-Two Prime Fibers

```text
TODO-ID: TODO-PVG-POWER-OF-TWO-PRIME-FIBERS-001
Status: DEFERRED / NOT ACTIVE / NOT AUTHORIZED
Captured: 2026-07-22
Parent program: PVG Inverse Geometry
Current governing goal remains: GOAL-OP-INVERSE-PRIME-FIBERS-001 (ENGINE-004)
```

## Deferred object

For an integer \(N\), study the power-of-two subtraction family

\[
N-2^k,
\qquad k\ge 1,
\qquad 2^k<N,
\]

and the associated prime fiber

\[
\mathcal R_{2^\ast}(N)
=
\{(k,p):k\ge1,\ p\text{ prime},\ N=2^k+p\}.
\]

Equivalently,

\[
r_{2^\ast}(N)
=
\#\{k\ge1:N-2^k\text{ is prime}\}.
\]

A broader geometric object to investigate later is

\[
\Phi_2(N)
=
\{\operatorname{supp}(N-2^k):k\ge1,\ 2^k<N\}.
\]

## Exact observations already available

- \(2^k\) lies on the prime-valuation axis of \(2\).
- For \(k\ge1\), subtracting \(2^k\) preserves parity:

\[
N-2^k\equiv N\pmod 2.
\]

- If \(N\) is even and \(N-2^k\) is prime, then necessarily

\[
N-2^k=2,
\]

so

\[
N=2^k+2.
\]

- If \(N\) is odd, every positive candidate \(N-2^k\) is odd and may be tested individually for primality.
- Existence or multiplicity of representations \(N=2^k+p\) is not a general primality criterion for \(N\).

## Questions reserved for later

1. How do the supports \(\operatorname{supp}(N-2^k)\) evolve as \(k\) moves along the \(2\)-axis?
2. Which support invariants are stable across this subtraction family?
3. How does \(r_{2^\ast}(N)\) vary inside a fixed exact-support fiber?
4. Can the family be organized as an inverse-geometry kernel without confusing it with a primality test?
5. What finite frozen box and independent verification protocol would be appropriate?

## Governance ceiling

This item is stored only as a deferred research direction.

```text
No new active goal.
No new engine.
No Phase D authorization.
No claim of a primality criterion.
No Goldbach, PNT, RH, or GRH claim.
No asymptotic or originality claim.
```

Return immediately to the currently governed ENGINE-004 inverse prime-fiber program.
