# ENGINE-004 PASS-001 — Support-Parity Stratification

**Goal:** `GOAL-OP-INVERSE-PRIME-FIBERS-001`  
**Engine:** `ENGINE-004-INVERSE-PRIME-FIBERS`  
**Phase:** C — Inverse Prime Fibers  
**Date:** 2026-07-22

## 1. Purpose

Deepen the internal theory of inverse prime fibers without leaving Phase C and without opening any theorem, asymptotic, or additive-conjecture track.

The Phase-C chain is

```text
support face F
→ integer point N in N(F)
→ prime-pair fiber R_2(N)
→ multiplicity r_2(N).
```

This pass identifies an exact stratification already encoded in the support face.

## 2. Support-parity identity

Let \(N\ge 1\) and let

\[
\operatorname{supp}(N)=\{p:\nu_p(N)>0\}.
\]

Then

\[
N\text{ is even}\iff 2\in\operatorname{supp}(N),
\]

and therefore

\[
N\text{ is odd}\iff 2\notin\operatorname{supp}(N).
\]

### Proof

By the definition of prime support,

\[
2\in\operatorname{supp}(N)
\iff \nu_2(N)>0
\iff 2\mid N
\iff N\text{ is even}.
\]

The odd statement is the complement. ∎

**Classification:** `IDENTITY / PROVED`.

## 3. Fiberwise parity constancy

For an exact support face \(F\), every integer in the inverse integer fiber

\[
\mathcal N(F)=\{N:\operatorname{supp}(N)=F\}
\]

has the same parity. More precisely,

\[
2\in F \Longrightarrow \mathcal N(F)\subset 2\mathbb N,
\]

while

\[
2\notin F \Longrightarrow \mathcal N(F)\subset 2\mathbb N+1.
\]

Thus the support face determines the Phase-C parity route before any prime-pair enumeration is performed.

```text
2 in F     → every N in N(F) is even → odd-prime + odd-prime route
2 not in F → every N in N(F) is odd  → 2 + odd-prime route
```

**Classification:** `PROVED`.

## 4. Exact odd-fiber formula

For odd \(N\), every representation by two primes must contain \(2\). Under the frozen ENGINE-004 convention of unordered distinct-prime pairs,

\[
\mathcal R_2(N)=
\begin{cases}
\{\{2,N-2\}\}, & N-2\text{ is prime},\\
\varnothing, & N-2\text{ is not prime}.
\end{cases}
\]

Consequently,

\[
r_2(N)=\mathbf 1_{\mathbb P}(N-2)
\qquad(N\text{ odd}).
\]

This yields a complete description of the prime-pair fiber on every support face \(F\) with \(2\notin F\).

**Classification:** `IDENTITY / PROVED`.

## 5. New inverse-geometric decomposition

The Phase-C inverse space splits canonically into two support strata:

\[
\mathfrak F_{\mathrm{even}}=\{F:2\in F\},
\qquad
\mathfrak F_{\mathrm{odd}}=\{F:2\notin F\}.
\]

On the odd stratum, the map

\[
N\mapsto\mathcal R_2(N)
\]

is binary-valued: empty or a singleton. On the even stratum, multiplicity can exceed one and requires full enumeration.

Hence the computational complexity of ENGINE-004 is geometrically localized:

```text
odd support stratum  → one primality test at N-2
 even support stratum → full distinct odd-prime pair scan
```

This is a structural reduction inside the inverse geometry engine, not an asymptotic statement.

## 6. Frozen-box verification

The implementation `tools/pvg_inverse_prime_fiber_parity.py` certifies:

- support parity for every integer point in a support fiber;
- equality between the support-forced route and the integer parity route;
- equality of every odd prime fiber with the exact formula above.

The test `tests/test_pvg_inverse_prime_fiber_parity.py` checks all 25 support faces and all 884 Phase-B integer points in the registered box:

```text
support primes <= 11
support sizes = 1,2,3
integer cap = 100000
```

**Classification:** `FINITE-VERIFIED` for the complete registered box.

## 7. Scientific ceiling

This pass establishes only elementary exact identities and their complete finite verification inside ENGINE-004.

It makes no claim concerning:

- Goldbach or any additive conjecture;
- existence of representations for all even integers;
- asymptotic representation counts;
- PNT, RH, or GRH;
- historical originality;
- Phase D authorization.

## 8. Result

```text
ENGINE-004-PASS-001-SUPPORT-PARITY-STRATIFICATION = PROVED_AND_FINITE_VERIFIED
Phase C remains active.
Phase D remains unauthorized.
```
