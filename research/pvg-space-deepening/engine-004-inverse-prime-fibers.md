# ENGINE-004 — Inverse Prime Fibers

**Goal:** `GOAL-OP-INVERSE-PRIME-FIBERS-001`  
**Parent:** `GOAL-PVG-INVERSE-GEOMETRY-001`  
**Phase:** C  
**Date:** 2026-07-22

## 1. Object

For every Phase-B integer point \(N\), define the unordered distinct-prime fiber

\[
\mathcal R_2(N)=\{\{p,q\}:p<q,\ p+q=N\}.
\]

The data layers remain separate:

```text
support face F
→ integer N in N(F)
→ prime fiber R_2(N)
→ multiplicity r_2(N)=|R_2(N)|
```

Support alone does not determine representation multiplicity.

## 2. Exact parity routing

If \(N\) is odd, one prime must be 2, so

\[
\mathcal R_2(N)\subseteq\{\{2,N-2\}\}
\]

and \(r_2(N)\le1\).

If \(N\) is even and the primes are distinct, both are odd.

## 3. Frozen complete box

```text
support primes <= 11
support sizes = 1,2,3
integer cap = 100000
integer points = 884
```

Every prime fiber is compared with an independent full scan.

## 4. Registered finite results

```text
representable integer points = 745
nonrepresentable integer points = 139
total unordered distinct-prime representations = 218024
maximum multiplicity in the box = 1557
maximum point = 97200
support of maximum point = {2,3,5}
```

These are finite-box facts only.

## 5. Interpretation

Phase C adds a third inverse layer:

```text
support predecessor
← integer fiber
← prime-pair fiber
```

It allows the engine to distinguish geometric type from representation count and prepares Phase D orbit certificates. It does not prove a Goldbach statement or any asymptotic estimate.

## 6. Stop rule

Close after complete-box equality, deterministic regeneration, parity verification, and governance audit. Phase D requires separate authorization.

**Classification:** exact definitions and parity identities plus finite verified infrastructure. No theorem or originality claim.
