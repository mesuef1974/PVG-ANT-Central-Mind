# PASS-004 — Prime-Axis Triangle Composition Atlas

**Program:** `PVG-INVERSE-GEOMETRY-001`  
**Status:** exact triangle identities / finite deterministic atlas  
**Scope:** all unordered prime triples `p < q < r <= 100`  
**Scientific ceiling:** identities and finite diagnostics only; no novelty, asymptotic, factorization-speedup, Goldbach, RH, or GRH claim

---

## 1. From edges to triangles

PASS-003 classified one primitive edge between two prime axes. PASS-004 asks what happens when two edge directions are composed:

\[
p\longrightarrow q\longrightarrow r
\]

and compared with the direct direction

\[
p\longrightarrow r.
\]

For primes

\[
p<q<r,
\]

the triangle contains the three axis pairs

\[
(p,q),\qquad(q,r),\qquad(p,r).
\]

Each edge retains its PASS-003 sum, difference, support, and level-defect signature. The new object is the compatibility among all three edges.

---

## 2. Registered scope

The first triangle atlas is

\[
\{(p,q,r):p<q<r\le100,\ p,q,r\text{ prime}\}.
\]

There are `25` primes and

\[
\binom{25}{3}=2300
\]

unordered prime-axis triangles.

The pass stops after:

1. generating all 2300 records;
2. verifying every exact composition identity;
3. recording finite preservation profiles;
4. testing deterministic CSV and JSON regeneration;
5. running repository governance.

No bound expansion is authorized by this document.

---

## 3. Multiplicative path independence

The three oriented axis ratios are

\[
\rho_{pq}=\frac qp,
\qquad
\rho_{qr}=\frac rq,
\qquad
\rho_{pr}=\frac rp.
\]

They satisfy

\[
\boxed{
\rho_{pq}\rho_{qr}=\rho_{pr}.
}
\]

Therefore a two-step horizontal transfer and the direct transfer agree:

\[
N\frac qp\frac rq=N\frac rp.
\]

Around the closed triangle,

\[
\boxed{
\frac qp\frac rq\frac pr=1.
}
\]

Thus the axis-ratio transport has zero multiplicative holonomy: the final multiplicative factor depends only on the endpoints, not on the chosen path.

**Classification:** exact identity / geometric reinterpretation.

---

## 4. Additive gap composition

Define the ordinary edge gaps

\[
D_{pq}=q-p,
\qquad
D_{qr}=r-q,
\qquad
D_{pr}=r-p.
\]

Then

\[
\boxed{
D_{pq}+D_{qr}=D_{pr}.
}
\]

This is the additive counterpart of ratio multiplication.

The two coordinate systems behave differently:

\[
\text{ratios compose by multiplication,}
\]

while

\[
\text{gaps compose by addition.}
\]

PVG places both descriptions on the same prime-axis triangle.

---

## 5. Normalized-gap composition

For two positive axes `a<b`, define

\[
\delta(a,b)=\frac{b-a}{b+a}.
\]

PASS-003 established the bridge

\[
\delta(a,b)=\frac{b/a-1}{b/a+1}.
\]

For the triangle, write

\[
\delta_{pq}=\delta(p,q),
\quad
\delta_{qr}=\delta(q,r),
\quad
\delta_{pr}=\delta(p,r).
\]

Using

\[
\rho_{pr}=\rho_{pq}\rho_{qr},
\]

one obtains

\[
\boxed{
\delta_{pr}
=
\frac{\delta_{pq}+\delta_{qr}}
{1+\delta_{pq}\delta_{qr}}.
}
\]

This is verified directly on all 2300 triangles.

Equivalently,

\[
\delta(a,b)=\tanh\!\left(\frac12\log\frac ba\right),
\]

so composition of axis ratios becomes the standard addition law for this normalized coordinate.

### Example: `(2,3,5)`

\[
\delta_{23}=\frac15,
\qquad
\delta_{35}=\frac14,
\qquad
\delta_{25}=\frac37.
\]

Indeed,

\[
\frac{\frac15+\frac14}{1+\frac1{20}}
=
\frac37.
\]

**Classification:** exact identity; no novelty claim.

---

## 6. Recovering the vertices from edge sums

Let

\[
S_{pq}=p+q,
\qquad
S_{qr}=q+r,
\qquad
S_{pr}=p+r.
\]

Then the three vertices are reconstructed exactly:

\[
\boxed{
p=\frac{S_{pq}+S_{pr}-S_{qr}}2,
}
\]

\[
\boxed{
q=\frac{S_{pq}+S_{qr}-S_{pr}}2,
}
\]

\[
\boxed{
r=\frac{S_{pr}+S_{qr}-S_{pq}}2.
}
\]

Thus the complete set of three pair sums is an injective encoding of the labeled prime triangle.

The three gaps also reconstruct the vertices once one absolute anchor is supplied, but gaps alone are invariant under common translation and therefore do not determine the absolute axes.

---

## 7. Axis-2 routing on triangles

PASS-003 showed that an edge between two odd prime axes routes both its reduced sum and difference through axis `2`, while an edge incident to axis `2` routes both transitions away from axis `2`.

This yields a complete triangle law.

### 7.1 All-odd triangle

If

\[
3\le p<q<r,
\]

then all three edges are odd-odd. Therefore all six reduced transitions

\[
p+q,\ q-p,
\quad
q+r,\ r-q,
\quad
p+r,\ r-p
\]

contain axis `2`.

### 7.2 Triangle containing axis 2

If

\[
p=2<q<r,
\]

then the four transitions on the two incident edges

\[
q\pm2,\qquad r\pm2
\]

are odd and exclude axis `2`.

The opposite edge `(q,r)` is odd-odd, so both

\[
q+r,\qquad r-q
\]

contain axis `2`.

Hence:

> In a prime-axis triangle containing axis `2`, the axis disappears from all transitions on its two incident edges and reappears exactly on the opposite edge.

This routing law was verified on all 2300 records.

---

## 8. Triangle preservation profile

For each triangle define

\[
S=\#\{\text{edges whose sum preserves }\Omega\},
\]

and

\[
D=\#\{\text{edges whose difference preserves }\Omega\}.
\]

The profile is written

\[
\boxed{Sx\_Dy}.
\]

For example, the triangle `(2,3,5)` has:

- sum preservation on `(2,3)` and `(2,5)`;
- difference preservation on `(3,5)` and `(2,5)`.

Therefore its profile is

\[
S2\_D2.
\]

The profile records only level preservation counts. It does not replace the full six-edge defect vector.

---

## 9. Exact rigidity results

### 9.1 No triangle has three sum-preserving edges

A sum-preserving edge must contain axis `2`. A triangle has only two edges incident to a given vertex, while its opposite edge is odd-odd and has composite even sum. Hence

\[
\boxed{S\le2.}
\]

Triangles with `S=2` are exactly

\[
(2,q,r)
\]

for which both

\[
q+2\quad\text{and}\quad r+2
\]

are prime.

Within the registered range, the eligible odd axes are

\[
3,5,11,17,29,41,59,71,
\]

so there are

\[
\binom82=28
\]

triangles with two sum-preserving edges.

### 9.2 All-odd triangles have at most two difference-preserving edges

For odd prime axes, a difference preserves the level exactly when the difference is `2`.

The long edge `(p,r)` cannot have gap `2` while a distinct prime `q` lies strictly between its endpoints. Therefore two preserved differences can only be

\[
q-p=2,\qquad r-q=2.
\]

Thus

\[
p,\ p+2,\ p+4
\]

are all prime. One of these three odd numbers is divisible by `3`, so the only possibility is

\[
\boxed{(p,q,r)=(3,5,7).}
\]

Hence `(3,5,7)` is the unique all-odd triangle with two difference-preserving edges.

### 9.3 Unique triangle with all three differences preserved

If all three edge differences are prime, an all-odd triangle is impossible by the previous argument. Therefore the triangle contains axis `2`:

\[
(2,q,r).
\]

Since `r-q` is an even prime,

\[
r-q=2.
\]

The other two differences require

\[
q-2,\quad r-2=q
\]

to be prime. Hence

\[
q-2,\quad q,\quad q+2
\]

are all prime. Among three odd numbers spaced by `2`, one is divisible by `3`; the unique possibility is

\[
3,5,7.
\]

Therefore

\[
\boxed{
D=3
\iff
(p,q,r)=(2,5,7).
}
\]

This triangle has profile

\[
S1\_D3.
\]

---

## 10. Finite atlas results for primes at most 100

The 2300 triangles divide by parity class as follows:

```text
contains axis 2 = 276
all odd         = 2024
```

### Sum-preserving edge count

```text
S=0 : 2144 triangles
S=1 :  128 triangles
S=2 :   28 triangles
```

### Difference-preserving edge count

```text
D=0 : 1969 triangles
D=1 :  295 triangles
D=2 :   35 triangles
D=3 :    1 triangle
```

### Complete preservation-profile distribution

```text
S0_D0 : 1885
S0_D1 :  237
S0_D2 :   22
S1_D0 :   63
S1_D1 :   52
S1_D2 :   12
S1_D3 :    1
S2_D0 :   21
S2_D1 :    6
S2_D2 :    1
```

The unique `S2_D2` triangle is

\[
(2,3,5),
\]

and the unique `S1_D3` triangle is

\[
(2,5,7).
\]

Exactly `23` triangles in the registered range contain the unique doubly preserving edge `(2,5)`.

All counts in this section are finite diagnostics tied to the registered bound. They support no density or asymptotic conclusion.

---

## 11. What the triangle adds beyond three independent edges

Three isolated pair records do not explicitly expose:

1. path independence of horizontal ratios;
2. closed-loop multiplicative holonomy;
3. the fractional normalized-gap composition law;
4. vertex recovery from all pair sums;
5. triangle-wide axis-2 routing;
6. compatibility constraints among three preservation profiles;
7. rigidity of `(3,5,7)` and `(2,5,7)`.

The triangle is therefore the first genuinely compositional object in this PVG research line.

---

## 12. Files and regeneration

The executable generator is:

```text
tools/pvg_prime_triangle_atlas.py
```

The deterministic tests are:

```text
tests/test_pvg_prime_triangle_atlas.py
```

The committed finite summary is:

```text
research/pvg-space-deepening/data/
prime-triangle-atlas-primes-le-100-summary.json
```

The generated CSV contains one record for each of the 2300 triangles and is regenerated in CI rather than committed as a large derived table.

---

## 13. Scientific classification

```text
ratio composition              = IDENTITY
closed-loop holonomy            = REINTERPRETATION OF IDENTITY
normalized-gap composition      = IDENTITY
vertex recovery                 = IDENTITY
axis-2 routing                  = IDENTITY / PVG REINTERPRETATION
triangle rigidity statements    = ELEMENTARY EXACT CLASSIFICATION
bound-100 profile counts        = FINITE DIAGNOSTIC
asymptotic triangle distribution = NOT ESTABLISHED
novel theorem or algorithm      = NOT CLAIMED
```

PASS-004 deepens the internal grammar of PVG. It does not by itself create a new theorem target or authorize a larger computation.
