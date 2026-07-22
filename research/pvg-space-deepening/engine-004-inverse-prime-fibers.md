# ENGINE-004 — Inverse Prime Fibers

**Goal:** `GOAL-OP-INVERSE-PRIME-FIBERS-001`  
**Parent:** `GOAL-PVG-INVERSE-GEOMETRY-001`  
**Phase:** C — Inverse Prime Fibers  
**Status:** active current checkpoint  
**Date:** 2026-07-22

## 1. Object and data separation

For every certified Phase-B integer point \(N\in\mathcal N(F)\), define the unordered distinct-prime fiber

\[
\mathcal R_2(N)=\{\{p,q\}:p<q,\ p+q=N\}.
\]

The engine preserves four distinct layers:

```text
support face F
→ exact-support integer N in N(F)
→ prime-pair fiber R_2(N)
→ multiplicity and centered-gap coordinates
```

The implementation now rejects a record whenever the supplied integer does not belong to the supplied exact-support fiber. This closes a data-integrity gap in the earlier API: a correct prime-pair calculation may not be attached to a false support label.

## 2. Exact support-controlled routing

For every \(N\in\mathcal N(F)\),

\[
N\equiv0\pmod 2\quad\Longleftrightarrow\quad 2\in F.
\]

Therefore the support face determines the parity route, although it does not determine the multiplicity.

### Route A — faces excluding axis 2

If \(2\notin F\), every \(N\in\mathcal N(F)\) is odd. Hence any distinct-prime representation must contain 2:

\[
\mathcal R_2(N)=
\begin{cases}
\{\{2,N-2\}\},&N-2\text{ is prime},\\
\varnothing,&N-2\text{ is not prime}.
\end{cases}
\]

Thus \(r_2(N)=|\mathcal R_2(N)|\in\{0,1\}\) on every support fiber excluding axis 2.

### Route B — faces containing axis 2

If \(2\in F\), every \(N\in\mathcal N(F)\) is even. A distinct-prime representation cannot contain 2, because the other summand would also have to be even. Therefore every representation uses two odd primes.

**Classification:** `IDENTITY / PROVED`. These statements are elementary parity consequences, not conjectural claims.

## 3. Centered-gap coordinate

For each representation \(p<q\) of \(N\), define

\[
\Delta=q-p>0.
\]

The centered-gap fiber is

\[
\Delta_2(N)=\{q-p:\{p,q\}\in\mathcal R_2(N)\}.
\]

The map

\[
\{p,q\}\longmapsto \Delta=q-p
\]

is a bijection from \(\mathcal R_2(N)\) to \(\Delta_2(N)\), because the inverse is exact:

\[
p=\frac{N-\Delta}{2},
\qquad
q=\frac{N+\Delta}{2}.
\]

Hence a prime-pair fiber over fixed \(N\) is equivalently a one-dimensional discrete centered-radius fiber.

### Exact identities

For every \(\Delta\in\Delta_2(N)\):

\[
\Delta\equiv N\pmod2,
\]

\[
N^2-\Delta^2=4pq,
\]

and

\[
\gcd(N,\Delta)=\gcd(N,2).
\]

The gcd law follows because every common divisor of \(p+q\) and \(q-p\) divides both \(2p\) and \(2q\); distinct primality forces that divisor to divide 2. Parity then selects 1 for odd \(N\) and 2 for even \(N\).

For even \(N\), writing \(m=N/2\) and \(d=\Delta/2\) gives the normalized form

\[
p=m-d,
\qquad
q=m+d,
\qquad
m^2-d^2=pq,
\qquad
\gcd(m,d)=1.
\]

**Classification:** `IDENTITY / PROVED`. No originality claim is made.

## 4. Frozen complete box

```text
support primes <= 11
support sizes = 1,2,3
integer cap = 100000
support faces = 25
integer points = 884
```

Every prime fiber is compared with an independent full scan. The production path uses parity routing with cached trial primality; the independent path uses a separately constructed sieve.

## 5. Registered finite results

```text
integer points                         = 884
representable integer points           = 745
nonrepresentable integer points        = 139
total unordered distinct-prime pairs   = 218024
centered-gap coordinates               = 218024
independent-scan mismatches             = 0
maximum multiplicity                   = 1557
maximum point                          = 97200
support of maximum point               = {2,3,5}
```

### Support-route decomposition

```text
faces containing axis 2                = 11
integer points on those faces          = 653
representable points                   = 650
nonrepresentable points                = 3
total representations                  = 217929
finite nonrepresentable points         = 2,4,6

faces excluding axis 2                 = 14
integer points on those faces          = 231
representable points                   = 95
nonrepresentable points                = 136
total representations                  = 95
```

The statement about \(2,4,6\) is only a complete fact about this frozen box. It is not promoted beyond the registered finite domain.

**Classification:** `FINITE-VERIFIED`.

## 6. Verification completed

- exact-support membership is enforced;
- all 884 production fibers equal the independent scans;
- all 218,024 prime pairs reconstruct from their centered gaps;
- all parity, square-difference, gcd, and normalized-radius identities pass;
- support membership of axis 2 controls the parity route on every point;
- every odd-support fiber reduces exactly to the primality test for \(N-2\);
- deterministic ordering and compact certificate generation pass;
- all claim-ceiling flags remain false.

## 7. Current checkpoint and next Phase-C question

ENGINE-004 remains the active operational goal. This checkpoint does not authorize Phase D and does not return to the archived theorem path.

The next bounded Phase-C question is:

> Which exact invariants and collisions are carried by the normalized centered-radius spectra
> \(D(N)=\{\Delta/2:\Delta\in\Delta_2(N)\}\) on the already frozen 884-point box?

The admissible next work is limited to exact incidence, equality, containment, compression, and finite verification inside the existing box. No cap expansion and no orbit-dynamics phase are implied.

## 8. Claim ceiling

- no Goldbach claim or progress;
- no asymptotic estimate;
- no PNT, RH, or GRH claim;
- no historical originality claim;
- no Phase-D authorization;
- no original lemma or theorem certification.

**Honest classification:** exact inverse-coordinate theory plus complete finite-box verification and reusable infrastructure. ENGINE-004 remains active; Phase D remains blocked pending a separate readiness decision.
