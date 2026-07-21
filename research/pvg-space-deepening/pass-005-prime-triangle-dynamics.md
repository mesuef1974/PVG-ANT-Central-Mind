# PASS-005 — Prime-Triangle Dynamics

**Program:** `PVG-INVERSE-GEOMETRY-001`  
**Scope:** all prime triangles `p<q<r<=100`  
**Status:** exact transform identities plus finite deterministic atlas  
**Scientific ceiling:** no asymptotic, novelty, factorization-speedup, Goldbach, RH, or GRH claim

## 1. Two transforms

For a prime-axis triangle define

\[
T_-(p,q,r)=(q-p,\ r-q,\ r-p)
\]

and

\[
T_+(p,q,r)=(p+q,\ q+r,\ p+r).
\]

The two transforms have fundamentally different information behavior.

## 2. Difference transform

Writing

\[
d_1=q-p,\qquad d_2=r-q,\qquad d_3=r-p,
\]

we have

\[
\boxed{d_3=d_1+d_2}.
\]

The transform is invariant under common translation:

\[
T_-(p+c,q+c,r+c)=T_-(p,q,r).
\]

Therefore it records triangle shape but loses absolute position. An anchor is required to reconstruct the source.

The gcd

\[
g=\gcd(d_1,d_2,d_3)=\gcd(d_1,d_2)
\]

extracts a primitive gap shape

\[
(d_1/g,d_2/g,d_3/g).
\]

## 3. Sum transform

Writing

\[
s_{pq}=p+q,\quad s_{qr}=q+r,\quad s_{pr}=p+r,
\]

we recover the source exactly:

\[
p=\frac{s_{pq}+s_{pr}-s_{qr}}2,
\]

\[
q=\frac{s_{pq}+s_{qr}-s_{pr}}2,
\]

\[
r=\frac{s_{pr}+s_{qr}-s_{pq}}2.
\]

Thus `T_+` is injective on labeled triangles.

For all-odd prime triangles,

\[
\gcd(p+q,q+r,p+r)=2.
\]

For triangles containing axis `2`, the common gcd is `1`.

## 4. Prime-output rigidity

`T_+` never produces three prime values: an all-odd source gives three even sums, while a source containing `2` still has the opposite odd-odd sum even and greater than `2`.

For `T_-`, all three entries can be distinct primes only for

\[
\boxed{(p,q,r)=(2,5,7)}.
\]

Proof sketch: an all-odd source gives three even differences, so it cannot work. If `p=2`, then `r-q` is even and prime, hence `r-q=2`. The other two differences require `q-2`, `q`, and `q+2` prime; among three odd numbers spaced by two, one is divisible by `3`, forcing the unique triple `3,5,7` and hence `q=5,r=7`.

The unique prime-triangle transition is

\[
(2,5,7)\xrightarrow{T_-}(3,2,5)\sim(2,3,5).
\]

The next step is

\[
(2,3,5)\xrightarrow{T_-}(1,2,3),
\]

which is not a prime triangle. Therefore no prime-triangle cycle occurs.

## 5. Finite atlas results

For the `2300` source triangles:

```text
number of prime differences
0 -> 1969
1 -> 295
2 -> 35
3 -> 1

number of prime sums
0 -> 2144
1 -> 128
2 -> 28
3 -> 0
```

The sole source with three prime differences is `(2,5,7)`. No sum transform is a prime triangle, and no prime-triangle cycle was detected or is possible under the exact rigidity above.

## 6. Interpretation

The difference transform is a **shape projection**: it forgets translation and retains gap geometry. The sum transform is an **injective edge encoding**: it retains the full labeled triangle.

This provides the first controlled dynamical layer in PVG:

```text
prime vertices
→ edge data
→ triangle transforms
→ information loss or exact recovery
→ termination / cycle classification
```

The executable atlas is `tools/pvg_prime_triangle_dynamics.py`; deterministic tests are in `tests/test_pvg_prime_triangle_dynamics.py`.
