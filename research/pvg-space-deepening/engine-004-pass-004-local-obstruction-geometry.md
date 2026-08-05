# Local Obstruction Geometry — Deferred Candidate Note

```text
Former label: ENGINE-004 PASS-004
Current label: CANDIDATE-LOCAL-OBSTRUCTION-GEOMETRY-001
Status: DEFERRED_CANDIDATE / NON-GOVERNING
Phase-C role: NOT REQUIRED
Phase D: NOT AUTHORIZED
```

## Governance correction

This note formerly used a duplicate `ENGINE-004 PASS-004` identity. The admitted PASS-004 is **Support-Conditioned Incidence Diagnostics**, which is closed and certified.

The local-obstruction material is retained only as a future candidate. It is not an active subpass, is not admitted finite evidence, and cannot block closure of the declared Phase-C deliverable.

## Candidate mathematics preserved

For even `N=2m` and `0<d<m`, define

```text
P_-(m,d)=m-d
P_+(m,d)=m+d
```

The exact owner relation is

```text
d in D(2m) iff P_-(m,d) and P_+(m,d) are distinct primes.
```

Also:

```text
m^2-d^2=(m-d)(m+d)
```

and actual ownership implies `gcd(m,d)=1`.

For each odd prime `ell`,

```text
ell | m^2-d^2 iff m = d (mod ell) or m = -d (mod ell).
```

A residue hit certifies non-ownership unless the divisible factor equals `ell` itself. Those boundary equalities must be recorded separately.

Finite local survival remains only a necessary condition relative to the tested primes. It is not ownership and is not a primality test.

## Preserved implementation

```text
tools/pvg_local_obstruction_geometry.py
tests/test_pvg_local_obstruction_geometry.py
tools/diagnose_pvg_local_obstruction_tests.py
```

These files remain quarantined candidate assets. Their results are not promoted while the candidate audit is failing or until a future readiness decision assigns a unique successor identity.

## Current classification

```text
factor and residue identities = IDENTITY / PROVED where elementary
frozen-box counts = NOT ADMITTED
local obstruction signatures = DIAGNOSTIC CANDIDATE
primality criterion = NOT ADMITTED
global law = OPEN / NOT AUTHORIZED
```

No new experiment, checkpoint, classifier, sieve claim, Goldbach/PNT/RH/GRH progress, originality, or publication-readiness claim is made.