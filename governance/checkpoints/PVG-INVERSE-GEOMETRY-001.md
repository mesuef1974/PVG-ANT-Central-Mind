# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002 + PASS-003 + PASS-004 + PASS-005 + PASS-006 + PASS-007 + PASS-008-ARITHMETIC-FUNCTION-TERRAIN
BRANCH = agent/pvg-point-classification-inverse-geometry-001
BASE = main
STATUS = CHECKPOINT_PASS_ON_BRANCH
PR = 63
ONTOLOGY-V1 = UNCHANGED
NEW-THEOREM-TARGET = NOT_AUTHORIZED
DATASET-004 = NOT_AUTHORIZED
LEAN-EXPANSION = NOT_AUTHORIZED
BOUND-EXPANSION = NOT_AUTHORIZED
MERGE = NOT_AUTHORIZED
```

## Installed capability ladder

### PASS-001 — exact point passport

Exact support, `omega`, `Omega`, exponent shape, primitive ray, divisor box, multiple cone, barycentric position, and certified inverse geometry.

### PASS-002 — local neighborhood

Axis ratios, primitive neighbors, root-lattice directions, gcd axis recovery, horizontal distance, pair-lines, simplex vertices, and geometric-mean identities.

### PASS-003 — prime-pair edges

For all `p<q<=100`, classify ratios, gaps, sums, differences, supports, level defects, axis-2 routing, and preservation classes.

### PASS-004 — prime-axis triangles

For all `p<q<r<=100`, verify ratio and normalized-gap composition, closed holonomy, pair-sum recovery, axis-2 routing, and preservation profiles.

### PASS-005 — triangle dynamics

Classify difference and sum transforms. The unique prime-triangle difference transition is `(2,5,7)->(2,3,5)`, followed by terminal `(1,2,3)`, with no prime-triangle cycle.

### PASS-006 — prime-axis tetrahedra

For all `p<q<r<s<=100`, verify six-edge and four-face compatibility, path independence, pair-sum recovery, axis-2 routing, and preservation profiles across `12650` tetrahedra.

### PASS-007 — general prime-simplex laws

For arbitrary ordered distinct prime axes

\[
p_1<\cdots<p_m,
\qquad m\ge2,
\]

install:

- dimension `m-1` and root lattice `A_(m-1)`;
- `k`-face count `C(m,k+1)` and total `2^m-1` nonempty faces;
- edge count `C(m,2)` and ordered interior degree `m(m-1)`;
- path-independent ratio transport;
- `m-1` consecutive-gap coordinates and anchor reconstruction;
- reconstruction from labeled pair sums for `m>=3`;
- pair-sum gcd rule for `m>=3`;
- axis-2 routing counts;
- sum-preserving-edge ceiling `m-1`;
- normalized-gap composition on every triangular subface.

### PASS-008 — arithmetic-function terrain

For one horizontal transfer

\[
N'=N\frac qp,
\qquad a=v_p(N)>0,
\qquad b=v_q(N)\ge0,
\]

install exact values, ratios, and boundary classes for

\[
n,\ \omega,\ \Omega,\ \tau,\ \sigma,\ \varphi,\ \mu,\ \lambda,\ \operatorname{rad}.
\]

The four move classes are:

```text
INTERIOR_TRANSFER     a>1, b>0
BOUNDARY_CONTRACTION  a=1, b>0
BOUNDARY_EXPANSION    a>1, b=0
SUPPORT_SWAP          a=1, b=0
```

## Exact PASS-008 laws

### Shell constants

\[
\Omega(N')=\Omega(N),
\qquad
\lambda(N')=\lambda(N)=(-1)^{\Omega(N)}.
\]

### Arithmetic size

\[
\frac{N'}N=\frac qp,
\qquad
\log N'-\log N=\log q-\log p.
\]

### Divisor count

\[
\boxed{
\frac{\tau(N')}{\tau(N)}
=
\frac{a}{a+1}\frac{b+2}{b+1}.
}
\]

Hence

\[
\tau(N')>\tau(N)\iff a>b+1,
\]

\[
\tau(N')=\tau(N)\iff a=b+1,
\]

\[
\tau(N')<\tau(N)\iff a<b+1.
\]

This is the exact local balancing law for the exponent-shape terrain.

### Sum of divisors

\[
\boxed{
\frac{\sigma(N')}{\sigma(N)}
=
\frac{p^a-1}{p^{a+1}-1}
\frac{q^{b+2}-1}{q^{b+1}-1}.
}
\]

### Euler totient

\[
\frac{\varphi(N')}{\varphi(N)}=
\begin{cases}
q/p,&a>1,b>0,\\
q/(p-1),&a=1,b>0,\\
(q-1)/p,&a>1,b=0,\\
(q-1)/(p-1),&a=1,b=0.
\end{cases}
\]

### Support-sensitive fields

- `mu` is supported on the squarefree skeleton and may undergo `0↔±1` at its boundary;
- `omega` changes by `-1`, `0`, or `+1` according to the four move classes;
- the radical is unchanged in the interior, divided by `p` under contraction, multiplied by `q` under expansion, and multiplied by `q/p` under a support swap.

## Installed files

```text
tools/pvg_arithmetic_terrain.py
tests/test_pvg_arithmetic_terrain.py
research/pvg-space-deepening/pass-008-arithmetic-function-terrain.md
```

The audit workflow and safe detached-worktree synchronization now execute PASS-008 tests and the `60 -> 90` arithmetic-terrain smoke test.

## Scientific classification

The formulas are exact elementary identities organized as scalar fields and edge gradients on PVG levels. This pass supplies no asymptotic estimate, factorization speedup, originality certificate, or progress on Goldbach, RH, or GRH.

## Validation on pre-closure head

```text
HEAD = 11469f4a570beb99b08de17166887839156a22a6
PVG Inverse Geometry Audit run 64 = PASS
Governance Required Gate run 656 = PASS
Python = 3.12
PASS-001 tests = 11/11 PASS
PASS-002 tests = 11/11 PASS
PASS-003 tests = 14/14 PASS
PASS-004 tests = 14/14 PASS
PASS-005 tests = 13/13 PASS
PASS-006 tests = 12/12 PASS
PASS-007 tests = 14/14 PASS
PASS-008 tests = 10/10 PASS
Combined deterministic tests = 99/99 PASS
Arithmetic terrain smoke test (60 -> 90) = PASS
General simplex smoke test = PASS
All committed/generated summaries = PASS
Safe PowerShell worktree execution = PASS
Large unfactored exact-input refusal = PASS
```

The closure commit changes only this checkpoint state. PR #63 remains draft and unmerged. The canonical worktree branch, structural-laboratory branch, and protected stash remain untouched.
