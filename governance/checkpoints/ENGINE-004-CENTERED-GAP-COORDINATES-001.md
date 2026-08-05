# ENGINE-004 Centered-Gap Coordinates — Checkpoint 001

```text
Checkpoint ID: ENGINE-004-CENTERED-GAP-COORDINATES-001
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Program: GOAL-PVG-INVERSE-GEOMETRY-001
Phase: C — Inverse Prime Fibers
Decision: CHECKPOINT_PASS
Goal status after checkpoint: active_current
Phase D: NOT AUTHORIZED
Date: 2026-07-22
```

## Scope preserved

```text
support primes <= 11
support sizes = 1,2,3
integer cap = 100000
support faces = 25
integer points = 884
prime-pair convention = unordered, distinct, p<q
```

No cap was expanded.

## Exact results admitted

For a fixed integer \(N\), every pair \(p<q\) in the prime fiber has the centered-gap coordinate

\[
\Delta=q-p.
\]

The coordinate is lossless over fixed \(N\):

\[
p=(N-\Delta)/2,
\qquad
q=(N+\Delta)/2.
\]

Every admitted coordinate satisfies

\[
\Delta\equiv N\pmod2,
\qquad
N^2-\Delta^2=4pq,
\qquad
\gcd(N,\Delta)=\gcd(N,2).
\]

For even \(N\), the normalized radius \(d=\Delta/2\) is coprime to the midpoint \(m=N/2\).

The support face determines the route:

```text
2 in F     => every N in N(F) is even; all distinct-prime pairs are odd+odd
2 not in F => every N in N(F) is odd; the fiber is empty or {2,N-2}
```

These statements are classified `IDENTITY / PROVED`. No originality is claimed.

## Data-integrity correction

`prime_fiber_record(n, support)` now verifies

```text
factor_support(n) == support
```

and rejects a mismatched support label. This preserves the separation between support class, integer point, and representation data.

## Frozen finite certificate

```text
integer points                         = 884
prime-pair fibers matching full scan   = 884
mismatches                             = 0
unordered distinct-prime pairs         = 218024
centered-gap coordinates               = 218024
maximum multiplicity                   = 1557
maximum point                          = 97200
maximum support                        = {2,3,5}
```

Support-route decomposition:

```text
contains axis 2: 11 faces, 653 points, 650 representable, 217929 pairs
excludes axis 2: 14 faces, 231 points, 95 representable, 95 pairs
```

Inside the frozen box, the only nonrepresentable points on supports containing axis 2 are `2,4,6`. This is a finite-box observation only.

## Reproducibility

```text
python -m unittest -v tests/test_pvg_inverse_prime_fibers.py
python tools/pvg_inverse_prime_fibers.py --registered-summary --compact
```

Local validation before push:

```text
8 tests = PASS
runtime = approximately 14–16 seconds in the validation container
```

Registered compact certificate SHA-256, including the trailing newline:

```text
5abfc26288b8e3d9fee33a6372cd8b7066c158b3fc54ce59475e1c8d7a465489
```

## Stage decision

```text
continue_within_phase_c
```

The next authorized question is the exact finite geometry of normalized centered-radius spectra on the same 884-point box: equality, containment, collisions, and compression only.

This checkpoint does not authorize:

- Phase D orbit dynamics;
- cap expansion;
- return to the archived theorem goal;
- a new theorem target;
- any Goldbach, PNT, RH, or GRH claim.

## Honest classification

Exact elementary identities, corrected inverse-fiber data contract, and complete finite verification. No original lemma or theorem is certified.
