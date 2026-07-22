# ENGINE-004 PASS-004 — Local Obstruction Geometry

```text
Goal: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Status: IMPLEMENTATION_CHECKPOINT
Decision ceiling: exact identities + finite verification only
Phase D: NOT AUTHORIZED
```

## 1. Governed object

For an even integer \(N=2m\) and a parity-admissible centered radius \(0<d<m\), define

\[
P_-(m,d)=m-d,
\qquad
P_+(m,d)=m+d.
\]

The exact owner relation is

\[
d\in D(2m)
\iff
P_-(m,d),P_+(m,d)
\text{ are distinct primes}.
\]

The factor identity is

\[
m^2-d^2=(m-d)(m+d).
\]

For an actual owner,

\[
\gcd(m,d)=1.
\]

## 2. Local residue geometry

For every odd prime \(\ell\),

\[
\ell\mid m^2-d^2
\iff
m\equiv d\pmod\ell
\quad\text{or}\quad
m\equiv-d\pmod\ell.
\]

The two residue hits have different geometric meanings:

```text
m ≡  d (mod ell)  → ell divides m-d → left obstruction candidate
m ≡ -d (mod ell)  → ell divides m+d → right obstruction candidate
```

A divisibility hit is an exact non-ownership certificate unless the divisible factor equals \(\ell\) itself.

## 3. Boundary exceptions

If

\[
m-d=\ell
\]

or

\[
m+d=\ell,
\]

then divisibility by \(\ell\) does not imply compositeness. These cases are registered separately as boundary exceptions.

Example:

\[
N=16,\quad m=8,\quad d=5,\quad m-d=3.
\]

Although \(3\mid m-d\), the left factor equals the prime 3 and the pair \((3,13)\) is valid.

## 4. Local survival is not ownership

For a local-prime ceiling \(P\), define survival by the absence of a non-boundary obstruction from every odd prime \(\ell\le P\).

This is necessary relative to the tested primes, but not sufficient for simultaneous primality.

Example:

\[
N=160,\quad m=80,\quad d=3.
\]

Then

\[
m-d=77,\qquad m+d=83.
\]

The pair survives local tests at \(3\) and \(5\), but 77 is composite. Therefore local survival may not be promoted to ownership or a primality test.

## 5. Odd route

For odd \(N\), the only possible distinct-prime pair is

\[
(2,N-2).
\]

With the governed odd coordinate \(d=N-4\),

\[
d\in D(N)
\iff
d+2=N-2\text{ is prime}.
\]

## 6. Implemented API

```text
primes_up_to(limit)
registered_even_radii(n)
local_obstruction_record(m,d,ell)
local_obstruction_signature(m,d,prime_limit)
boundary_exception_record(m,d,ell)
even_coordinate_owner_certificate(n,d,prime_limit)
odd_coordinate_owner_certificate(n)
registered_local_obstruction_summary(prime_limit)
```

The default local-prime ceiling is the unchanged registered support-prime limit:

```text
P = 11
local odd primes = 3,5,7,11
```

This is a finite diagnostic choice, not a canonical global cutoff.

## 7. Candidate domain

For every registered even point \(N=2m\), PASS-004 scans every \(d\) satisfying

```text
0 < d < m
m and d have opposite parity
```

so that \(m-d\) and \(m+d\) are odd. It does not restrict the scan to already known owners.

For every candidate it records:

- exact left and right factors;
- owner status by primality;
- owner status by the registered prime-pair fiber;
- square-difference identity;
- midpoint-radius gcd;
- obstructing local primes;
- boundary exceptions;
- local-survival status.

## 8. Required verification

The pass is not closable until CI confirms:

```text
owner_by_primality = owner_by_registered_fiber for every candidate
local residue identities hold
boundary exceptions are separated from obstructions
local survival is demonstrably not sufficient
the odd-route reduction is exact
Phase D is unused
no primality-test claim is made
```

## 9. Scientific classification

```text
Residue and factor laws           = IDENTITY / PROVED
Owner equivalence                 = IDENTITY / PROVED
Frozen-box counts                 = FINITE-VERIFIED after CI
Local-prime signatures            = DIAGNOSTIC
Primality-test interpretation     = NOT ADMITTED
Global density or asymptotics     = NOT AUTHORIZED
```

## 10. Relation to ENGINE-005 candidate

The later local-neighborhood geometry candidate may reuse these obstruction records for values \(x+k\). It is not active until PASS-004 is closed or explicitly stopped. No feature-selection, training, classifier, or primality claim is authorized by this document.
