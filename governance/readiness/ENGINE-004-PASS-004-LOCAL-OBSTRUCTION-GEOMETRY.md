# Deferred Candidate — Local Obstruction Geometry

```text
Former identity: ENGINE-004-PASS-004-LOCAL-OBSTRUCTION-GEOMETRY
Replacement identity: CANDIDATE-LOCAL-OBSTRUCTION-GEOMETRY-001
Parent program: GOAL-PVG-INVERSE-GEOMETRY-001
Former engine: ENGINE-004
Status: DEFERRED_CANDIDATE / NON-GOVERNING
Decision: QUARANTINED_FROM_PHASE_C
Date: 2026-07-23
Phase D: NOT AUTHORIZED
```

## Governance correction

This work was previously assigned the duplicate identity `ENGINE-004 PASS-004` while the admitted PASS-004 is **Support-Conditioned Incidence Diagnostics**.

The duplicate identity is withdrawn. This document does not authorize an active subpass, does not block the scientifically complete Phase C deliverable, and does not create PASS-005.

## Candidate question

Can centered-radius coordinate ownership be explained by midpoint-radius arithmetic and local congruence obstructions, rather than only enumerated?

For even `N=2m`, the candidate studies

```text
P_-(m,d)=m-d
P_+(m,d)=m+d
```

and the exact owner condition that both factors are distinct primes. For odd `N`, ownership reduces to the registered-point condition and primality of `N-2`.

## Preserved exact content

The following elementary facts remain available as non-governing candidate material:

1. `d in D(2m)` iff `m-d` and `m+d` are distinct primes.
2. `m^2-d^2=(m-d)(m+d)`.
3. Actual ownership implies `0<d<m` and `gcd(m,d)=1`.
4. For odd prime `ell`, `ell | m^2-d^2` iff `m = +/-d (mod ell)`.
5. A residue hit away from the boundary equalities `m-d=ell` and `m+d=ell` certifies non-ownership.
6. Finite local survival is necessary relative to the tested primes but is not sufficient for simultaneous primality.

## Quarantine rule

```text
active ENGINE-004 subpass = false
required for Phase-C closure = false
workflow required check = false
new dataset or experiment authorized = false
successor activation = requires a separate parent decision
```

The existing implementation and tests may be preserved for future repair. Their current failing audit is not admitted evidence and is isolated from PR-required checks.

## Scientific ceiling

```text
exact residue/factor laws = IDENTITY / PROVED where already established
finite candidate counts = NOT ADMITTED until a future repaired checkpoint
local signatures = DIAGNOSTIC CANDIDATE
primality-test interpretation = NOT ADMITTED
general density or asymptotics = NOT AUTHORIZED
Goldbach/PNT/RH/GRH progress = false
historical originality = false
publication readiness = false
```

**Classification:** deferred non-governing candidate; not an ENGINE-004 pass.