# PASS-003 — Prime-Pair Edge Transition Atlas

**Program:** `PVG-INVERSE-GEOMETRY-001`  
**Status:** finite deterministic atlas / exact edge identities  
**Scope:** all unordered prime pairs `p < q <= 100`  
**Scientific ceiling:** identities and finite diagnostics only; no novelty, asymptotic, factorization-speedup, Goldbach, RH, or GRH claim

---

## 1. Question

A primitive horizontal edge above a common base `g` has endpoints

\[
N=gp,\qquad M=gq,
\]

where `p<q` are prime axes. The horizontal direction is encoded by

\[
\rho(p,q)=\frac qp.
\]

Addition and subtraction leave that horizontal edge and generate

\[
N+M=g(p+q),\qquad M-N=g(q-p).
\]

PASS-003 asks:

1. How does the axis ratio relate to additive separation?
2. Which new prime axes occur in `p+q` and `q-p`?
3. When does addition or subtraction preserve the original `Omega` level?
4. What role does axis `2` play?
5. Which statements are universal identities, and which are merely finite distributions in the registered range?

---

## 2. Registered scope and stopping rule

The first atlas is exactly

\[
\{(p,q):p<q\le100,\ p,q\text{ prime}\}.
\]

There are `25` primes and

\[
\binom{25}{2}=300
\]

unordered axis pairs.

The pass stops after:

- generating all 300 records;
- verifying the universal identities below on every record;
- recording the finite defect distributions;
- testing deterministic regeneration;
- running repository governance.

No bound expansion is authorized by this document.

---

## 3. Edge invariants

For each pair define

\[
S=p+q,\qquad D=q-p,\qquad \rho=\frac qp,
\]

and the normalized additive separation

\[
\delta=\frac{q-p}{q+p}.
\]

The exact multiplicative-additive bridge is

\[
\boxed{\delta=\frac{\rho-1}{\rho+1}.}
\]

Conversely,

\[
\boxed{\rho=\frac{1+\delta}{1-\delta}.}
\]

Thus the axis ratio and normalized gap carry the same pairwise information.

The prime axes themselves are recovered from `S,D` by

\[
\boxed{p=\frac{S-D}{2},\qquad q=\frac{S+D}{2}.}
\]

This is an exact coordinate change between multiplicative direction data and additive edge data.

---

## 4. Level defects

The endpoints `gp,gq` lie at height

\[
\Omega(g)+1.
\]

Define

\[
\kappa_+(p,q)=\Omega(p+q)-1,
\]

\[
\kappa_-(p,q)=\Omega(q-p)-1.
\]

Then

\[
\Omega(N+M)-\Omega(N)=\kappa_+(p,q),
\]

\[
\Omega(M-N)-\Omega(N)=\kappa_-(p,q).
\]

Therefore both defects depend only on the prime-axis pair, not on the common base `g`.

Interpretation:

- `kappa = 0`: the operation preserves the horizontal level;
- `kappa > 0`: the operation rises by `kappa` levels;
- `kappa < 0`: the operation descends.

---

## 5. Support orthogonality

For distinct primes `p,q`,

\[
\gcd(pq,p+q)=1,
\]

and

\[
\gcd(pq,q-p)=1.
\]

Hence the reduced transition factors `p+q` and `q-p` contain neither edge axis `p` nor edge axis `q`.

This means that addition and subtraction do not recycle their two active edge axes in the reduced factor. They route the edge into a disjoint set of prime directions, while any support already present in the common base `g` remains attached.

**Classification:** `IDENTITY / PVG REINTERPRETATION`.

---

## 6. Axis-2 routing law

### 6.1 Edge between two odd prime axes

If `p,q` are odd, then both

\[
p+q\quad\text{and}\quad q-p
\]

are even. Therefore both reduced transitions contain axis `2`.

Moreover,

\[
\boxed{\gcd(p+q,q-p)=2.}
\]

Thus their reduced supports intersect exactly in axis `2`.

### 6.2 Edge involving axis 2

If `p=2` and `q` is odd, then

\[
q+2\quad\text{and}\quad q-2
\]

are odd. Therefore both reduced transitions exclude axis `2`, and

\[
\boxed{\gcd(q+2,q-2)=1.}
\]

Geometric interpretation:

> Axis `2` is the universal common mediator of sum and difference transitions between two odd prime axes, but disappears from both reduced transitions when it is itself an edge axis.

**Classification:** `IDENTITY / PVG REINTERPRETATION`.

---

## 7. Complete level-preservation classification

### 7.1 Addition

Addition preserves the level exactly when

\[
\Omega(p+q)=1,
\]

that is, when `p+q` is prime.

Two odd primes have even sum greater than `2`, so this is impossible unless `p=2`. Therefore

\[
\boxed{
\kappa_+(p,q)=0
\iff
p=2\text{ and }q+2\text{ is prime}.
}
\]

Thus sum-preserving primitive edges are exactly the edges `(2,q)` whose other axis begins a twin-prime pair `(q,q+2)`.

### 7.2 Subtraction

Subtraction preserves the level exactly when

\[
q-p
\]

is prime.

For odd `p,q`, the difference is even, so it is prime exactly when

\[
q-p=2.
\]

Therefore

\[
\boxed{
\kappa_-(p,q)=0
\iff
q-p\text{ is prime}.
}
\]

and, on odd-odd edges,

\[
\boxed{
\kappa_-(p,q)=0
\iff
q-p=2.
}
\]

### 7.3 Simultaneous preservation

If both operations preserve the level, then `p=2` and all three numbers

\[
q-2,\quad q,\quad q+2
\]

are prime.

Among three odd numbers spaced by `2`, one is divisible by `3`. The only prime triple of this form is

\[
3,5,7.
\]

Hence

\[
\boxed{
\kappa_+(p,q)=\kappa_-(p,q)=0
\iff
(p,q)=(2,5).
}
\]

This is an elementary exact classification, not an originality claim.

---

## 8. Distinguished examples

### Edge `(2,3)`

\[
\rho=\frac32,\qquad S=5,\qquad D=1.
\]

Therefore

\[
\kappa_+=0,\qquad \kappa_-=-1.
\]

Addition preserves the level; subtraction drops one level.

### Edge `(2,5)`

\[
\rho=\frac52,\qquad S=7,\qquad D=3.
\]

Therefore

\[
\kappa_+=\kappa_-=0.
\]

This is the unique prime-axis pair with simultaneous preservation.

### Edge `(3,7)`

\[
S=10=2\cdot5,
\]

\[
D=4=2^2.
\]

Therefore

\[
\kappa_+=1,\qquad \kappa_-=1.
\]

Both operations rise by one level, and both routes pass through axis `2`.

### Edge `(101,103)` outside the registered finite atlas

\[
S=204=2^2\cdot3\cdot17,
\]

\[
D=2.
\]

Thus

\[
\kappa_+=3,\qquad \kappa_-=0.
\]

The identities are universal even though this pair is outside the first registered bound.

---

## 9. Finite atlas results for `q <= 100`

The 300 pairs split into:

- `24` edges involving axis `2`;
- `276` odd-odd edges.

### Sum transitions

- level preserved: `8`;
- level raised: `292`;
- level lowered: `0`.

Defect distribution:

```text
kappa_plus = 0 : 8
kappa_plus = 1 : 57
kappa_plus = 2 : 96
kappa_plus = 3 : 81
kappa_plus = 4 : 40
kappa_plus = 5 : 16
kappa_plus = 6 : 2
```

The maximum observed sum defect is `6`, attained when

\[
p+q=128=2^7
\]

for the pairs

\[
(31,97),\qquad(61,67).
\]

### Difference transitions

- level lowered: `1`;
- level preserved: `16`;
- level raised: `283`.

Defect distribution:

```text
kappa_minus = -1 : 1
kappa_minus =  0 : 16
kappa_minus =  1 : 95
kappa_minus =  2 : 107
kappa_minus =  3 : 61
kappa_minus =  4 : 17
kappa_minus =  5 : 3
```

The unique downward edge is `(2,3)`, since its difference is `1`.

The maximum observed difference defect is `5`, attained when

\[
q-p=64=2^6
\]

for

\[
(3,67),\qquad(7,71),\qquad(19,83).
\]

These counts are finite diagnostics tied to the registered bound. They are not asymptotic claims.

---

## 10. Generated artifacts

The executable generator is

```text
tools/pvg_prime_pair_edge_atlas.py
```

It emits:

```text
prime-pair-edge-atlas-primes-le-100.csv
prime-pair-edge-atlas-primes-le-100-summary.json
```

The CSV records every pair and both reduced transitions. The JSON records definitions, universal identities, finite distributions, distinguished pairs, and maximum observed defects.

---

## 11. Tests and kill conditions

The pass must fail if any of the following occurs:

1. the registered scope does not contain exactly 25 primes and 300 pairs;
2. the ratio-gap bridge fails;
3. a reduced transition reuses edge axis `p` or `q`;
4. the sum-difference gcd law fails;
5. an odd-odd transition omits axis `2`;
6. an edge involving axis `2` retains axis `2` in the reduced transition;
7. the level-preservation classifications fail;
8. a pair other than `(2,5)` preserves both operations;
9. deterministic regeneration changes the committed atlas;
10. governance detects an unsupported promotion.

---

## 12. Next questions, not conclusions

1. How do the defect distributions change with a preregistered larger bound?
2. What is the joint distribution of `(kappa_plus,kappa_minus)`?
3. How do `v_2(p+q)` and `v_2(q-p)` interact for odd-odd edges?
4. Which axis pairs maximize or minimize support dimension at a fixed ratio or gap?
5. Can edge transitions be composed into paths between support faces?
6. How do arithmetic functions on `p+q` and `q-p` correlate with the geometric ratio `q/p` after proper normalization?
7. Which observations reduce immediately to standard prime-gap, Goldbach-type, cyclotomic, or additive-function questions?

Any expansion requires a separate scope, source audit, and stopping rule.
