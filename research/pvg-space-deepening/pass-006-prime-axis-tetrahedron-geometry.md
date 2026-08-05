# PASS-006 — Prime-Axis Tetrahedron Geometry

**Program:** `PVG-INVERSE-GEOMETRY-001`  
**Scope:** all unordered prime quadruples `p<q<r<s<=100`  
**Status:** exact simplex identities plus finite deterministic atlas  
**Scientific ceiling:** no asymptotic, novelty, factorization-speedup, Goldbach, RH, or GRH claim

## 1. Object

A four-axis PVG simplex has vertices

\[
p<q<r<s,
\]

six edges, and four triangular faces. The registered atlas contains

\[
\binom{25}{4}=12650
\]

prime-axis tetrahedra.

## 2. Ratio path independence

Every path from one axis to another has the same multiplicative transport. In particular,

\[
\frac qp\frac rq\frac sr=\frac sp,
\]

and

\[
\frac rp\frac sr=\frac sp.
\]

Every one of the four triangular faces has closed holonomy `1`. Thus PASS-004 face consistency extends coherently to the boundary of the tetrahedron.

## 3. Additive gap compatibility

For consecutive gaps

\[
d_1=q-p,\quad d_2=r-q,\quad d_3=s-r,
\]

all longer gaps are interval sums:

\[
r-p=d_1+d_2,
\]

\[
s-q=d_2+d_3,
\]

\[
s-p=d_1+d_2+d_3.
\]

The difference transform therefore records a translation-invariant shape. It cannot recover the absolute location without one anchor vertex.

## 4. Recovery from six pair sums

Let

\[
S_{ij}=p_i+p_j
\]

for the six unordered pairs. If

\[
T=p+q+r+s,
\]

then

\[
\sum_{i<j}S_{ij}=3T.
\]

For a fixed vertex `p_i`, let `I_i` be the sum of the three incident pair sums. Then

\[
I_i=2p_i+T,
\]

and hence

\[
\boxed{p_i=\frac{I_i-T}{2}.}
\]

Therefore all six pair sums form an injective encoding of the labeled tetrahedron.

## 5. GCD of the sum transform

If all four prime vertices are odd, all six pair sums are even and

\[
\gcd_{i<j}(p_i+p_j)=2.
\]

If the tetrahedron contains axis `2`, three pair sums incident to `2` are odd, and

\[
\gcd_{i<j}(p_i+p_j)=1.
\]

Thus the common gcd of the six sums detects whether axis `2` belongs to the tetrahedron.

## 6. Axis-2 routing

Every odd-odd edge sends both reduced sum and reduced difference through axis `2`. Every edge incident to axis `2` sends both transitions away from axis `2`.

Consequently:

- in an all-odd tetrahedron, all twelve reduced edge transitions contain axis `2`;
- in a tetrahedron containing axis `2`, the six transitions on the three incident edges exclude axis `2`, while the six transitions on the three opposite odd-odd edges contain it.

## 7. Preservation profiles

Each tetrahedron receives a profile

\[
S_xD_y,
\]

where `x` is the number of sum-preserving edges and `y` is the number of difference-preserving edges among the six edges.

Because every sum-preserving prime edge must be incident to axis `2`, a tetrahedron has at most three sum-preserving edges.

Within the registered bound:

```text
SUM-PRESERVED EDGE COUNTS
0 = 11186
1 = 960
2 = 448
3 = 56

DIFFERENCE-PRESERVED EDGE COUNTS
0 = 9386
1 = 2607
2 = 537
3 = 113
4 = 7
```

The maximum observed difference-preservation count is `4`, attained by:

```text
(2,3,5,7)
(2,5,7,13)
(2,5,7,19)
(2,5,7,31)
(2,5,7,43)
(2,5,7,61)
(2,5,7,73)
```

This list is a finite bound-100 result only.

## 8. Structural conclusion

The transition from triangles to tetrahedra adds a genuine compatibility layer:

- six edge records must agree on four shared triangular faces;
- ratio transport remains path independent across multiple routes;
- additive gaps form an interval-sum system;
- sum data is globally invertible;
- difference data preserves shape but loses translation;
- axis `2` routing is determined by incidence.

This is the first explicit four-axis simplex layer in the PVG program. No bound expansion or move to five axes is authorized by this pass alone.
