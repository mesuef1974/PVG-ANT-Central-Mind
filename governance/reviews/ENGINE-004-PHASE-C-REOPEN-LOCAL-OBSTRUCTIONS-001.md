# ENGINE-004 Phase C Reopen Review — Local Obstruction Geometry

```text
Review ID: ENGINE-004-PHASE-C-REOPEN-LOCAL-OBSTRUCTIONS-001
Goal: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Decision: REOPEN_PHASE_C_WITH_NAMED_GAP
Date: 2026-07-22
Phase D: NOT AUTHORIZED
```

## Owner direction

The owner explicitly requested deeper mathematical investigation of the inverse geometry after the parent review had judged the original deliverable satisfied.

## Named gap

PASS-003 computed the owner sets

\[
\mathcal O(d)=\{N:d\in D(N)\},
\]

but did not give an exact local-arithmetic characterization of membership in \(\mathcal O(d)\).

For an even point \(N=2m\), the governed coordinate law gives

\[
d\in D(N)
\iff
m-d\text{ and }m+d\text{ are distinct primes}.
\]

Hence

\[
m^2-d^2=(m-d)(m+d)
\]

and every odd prime \(\ell\) gives the exact obstruction

\[
m\equiv \pm d\pmod\ell
\Longrightarrow
\ell\mid(m-d)(m+d).
\]

Except for the boundary cases \(m-d=\ell\) or \(m+d=\ell\), such a residue hit forces one reconstructed factor to be composite. The current repository has not yet organized these exact local obstruction signatures, exceptional boundary cases, or their support-conditioned incidence.

For an odd point, the route is exact and simpler:

\[
d\in D(N)
\iff
N=d+4\text{ is registered and }d+2\text{ is prime}.
\]

## Why this is not merely more finite statistics

This pass seeks exact equivalences and local divisibility certificates explaining owner-set membership and non-membership. It is not another degree table, graph iteration, density estimate, or asymptotic model.

## Decision

The prior closure-review path is suspended, not invalidated. Phase C is reopened for one bounded subpass only:

```text
ENGINE-004 PASS-004 — LOCAL OBSTRUCTION GEOMETRY
```

No further subpass is authorized automatically.

## Ceiling

- exact identities and finite verification only;
- no sieve asymptotics or singular-series claims;
- no Goldbach, PNT, RH, or GRH claim or progress;
- no Phase D dynamics;
- no cap or support-universe expansion;
- no originality or publication-readiness claim.
