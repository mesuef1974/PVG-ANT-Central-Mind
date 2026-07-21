# PASS-009 — Global Arithmetic Terrain on a Fixed PVG Level

## Scope

The preregistered first atlas uses the prime face

\[
P=\{2,3,5\}
\]

and level

\[
\Omega=6.
\]

The closed simplex section contains

\[
\binom{6+3-1}{3-1}=28
\]

lattice points.

## Purpose

PASS-008 computed exact changes on one horizontal edge. PASS-009 enumerates the whole fixed-level simplex and records global extrema of

\[
n,\ \tau,\ \sigma,\ \varphi,\ \sigma(n)/n,\ \varphi(n)/n,\ \omega.
\]

## Exact structural laws

For fixed axes and fixed \(\Omega=r\):

1. \(\Omega\) and \(\lambda=(-1)^r\) are constant on the whole level.
2. \(\log n=\sum a_i\log p_i\) is linear, so the smallest and largest integers occur at the smallest- and largest-prime vertices.
3. \(\tau=\prod(a_i+1)\) is maximized by balanced exponent vectors; a unit transfer from \(a\) to \(b\) raises \(\tau\) exactly when \(a>b+1\).
4. \(\varphi(n)/n=\prod_{p\mid n}(1-1/p)\) is constant on each support stratum and changes only when the support changes.
5. \(\sigma(n)/n\) depends on both exponents and prime labels and therefore has a genuinely weighted terrain.

## Exact finite atlas for axes 2,3,5 and level 6

- point count: 28;
- minimum integer: \(2^6=64\) at exponent vector \((6,0,0)\);
- maximum integer: \(5^6=15625\) at \((0,0,6)\);
- minimum \(\tau\): 7 at the three vertices;
- maximum \(\tau\): 27 at the balanced point \((2,2,2)\), corresponding to \(900\);
- minimum \(\sigma(n)/n\): \(19531/15625\) at \((0,0,6)\);
- maximum \(\sigma(n)/n\): \(13/4\) at \((3,2,1)\), corresponding to \(360\);
- minimum \(\varphi(n)/n\): \(4/15\) on every full-support point;
- maximum \(\varphi(n)/n\): \(4/5\) at the vertex \((0,0,6)\).

## Interpretation

The level carries several different landscapes:

- `n`: a linear log-height field controlled by prime weights;
- `tau`: an unlabeled shape field controlled by balance of exponents;
- `phi/n`: a support-stratum field;
- `sigma/n`: a weighted multiplicity field;
- `mu`: a field concentrated on the squarefree skeleton;
- `lambda`: a shell constant.

This separation is the main conceptual result of the pass.

## Files

```text
tools/pvg_level_terrain.py
tests/test_pvg_level_terrain.py
research/pvg-space-deepening/pass-009-global-level-terrain.md
```

## Scientific boundary

This is an exact finite enumeration and geometric organization of elementary arithmetic identities. It supplies no asymptotic estimate, extremal theorem beyond the explicitly proved local balancing statements, originality certificate, factorization speedup, or progress on Goldbach, RH, or GRH.
