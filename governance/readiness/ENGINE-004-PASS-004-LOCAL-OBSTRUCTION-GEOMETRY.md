# ENGINE-004 PASS-004 — Local Obstruction Geometry Readiness

```text
Task ID: ENGINE-004-PASS-004-LOCAL-OBSTRUCTION-GEOMETRY
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Decision: READY
Status: ACTIVE_CURRENT_SUBPASS
Date: 2026-07-22
Phase D: NOT AUTHORIZED
```

## Research question

Can coordinate ownership be explained exactly by midpoint-radius arithmetic and local congruence obstructions, rather than only enumerated?

For even \(N=2m\), define

\[
P_-(m,d)=m-d,
\qquad
P_+(m,d)=m+d.
\]

The governed owner relation is

\[
d\in D(2m)
\iff
P_-(m,d),P_+(m,d)\text{ are distinct primes}.
\]

For odd \(N\),

\[
d\in D(N)
\iff
N=d+4\text{ and }d+2\text{ is prime}.
\]

## Required exact objects

```text
local_obstruction_record(m,d,ell)
local_obstruction_signature(m,d,prime_limit)
boundary_exception_record(m,d,ell)
even_coordinate_owner_certificate(N,d)
odd_coordinate_owner_certificate(N,d)
registered_local_obstruction_summary()
```

## Exact identities to prove and verify

1. \(d\in D(2m)\iff m-d,m+d\) are distinct primes.
2. \(m^2-d^2=(m-d)(m+d)\).
3. If \(d\in D(2m)\), then \(0<d<m\) and \(\gcd(m,d)=1\).
4. For every odd prime \(\ell\),
   \[
   \ell\mid m^2-d^2\iff m\equiv d\pmod\ell\text{ or }m\equiv-d\pmod\ell.
   \]
5. If \(m\equiv d\pmod\ell\), then \(\ell\mid m-d\); primality permits this only when \(m-d=\ell\).
6. If \(m\equiv-d\pmod\ell\), then \(\ell\mid m+d\); primality permits this only when \(m+d=\ell\).
7. Away from these boundary equalities, any residue hit is an exact certificate of non-ownership.
8. Odd-route ownership is equivalent to the single primality test on \(d+2\), together with registered-point membership of \(d+4\).

## Frozen domain

```text
support primes <= 11
support face sizes = 1,2,3
integer cap = 100000
integer points = 884
coordinate occurrences = 218024
```

No domain expansion is permitted.

## Required finite outputs

- complete owner/non-owner verification for all registered \((N,d)\) candidates used by the pass;
- counts of obstruction certificates by local prime \(\ell\), separated from boundary exceptions;
- exact inventory of boundary exceptions;
- support-conditioned obstruction signatures;
- independent reconstruction from prime-pair fibers;
- deterministic certificate and SHA-256;
- explicit statement of what local obstruction data does not decide.

## Non-claims

A finite collection of local obstruction tests is generally necessary but not sufficient for simultaneous primality of \(m-d\) and \(m+d\). The pass must not market local survival as ownership, primality, or a global representation theorem.

## Stop rule

Stop after exact local-obstruction identities and frozen-box certification. Do not open weighted sieves, densities, singular series, asymptotics, graph dynamics, or Phase D.

## Claim ceiling

```text
historical originality = false
original lemma/theorem = false
Phase D authorized = false
Goldbach progress = false
PNT progress = false
RH progress = false
GRH progress = false
publication readiness = false
```
