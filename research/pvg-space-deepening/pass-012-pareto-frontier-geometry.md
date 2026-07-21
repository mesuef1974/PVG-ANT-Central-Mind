# PASS-012 — Geometry of the PVG Pareto Frontier

**Registered scope:** axes `(2,3,5)`, level `Omega=6`  
**Objectives:** maximize `n`, `tau`, `sigma(n)/n`, and `phi(n)/n`  
**Status:** exact finite induced-subgraph analysis; no asymptotic or originality claim

## 1. Object

PASS-011 identified 19 globally nondominated points among the 28 points of the level. PASS-012 studies the graph induced by those 19 points under primitive horizontal adjacency.

Two frontier points are adjacent when their exponent vectors differ by one unit transfer:

\[
\frac12\|a-b\|_1=1.
\]

## 2. Exact finite results

```text
frontier vertices = 19
frontier edges    = 27
components        = 3
component sizes   = 17, 1, 1
cycle rank        = 11
```

The isolated globally Pareto-optimal points are

\[
(0,6,0),\qquad(6,0,0).
\]

Thus global nondominance does not imply adjacency-connectivity. The remaining 17 frontier points form one connected component.

The three leaves of the nontrivial frontier component are

\[
(0,4,2),\qquad(2,4,0),\qquad(4,0,2).
\]

The articulation points are

\[
(0,3,3),\ (2,2,2),\ (3,0,3),\ (3,2,1),\ (3,3,0).
\]

The four bridges are

\[
(0,3,3)-(0,4,2),
\]

\[
(2,2,2)-(3,2,1),
\]

\[
(2,4,0)-(3,3,0),
\]

\[
(3,0,3)-(4,0,2).
\]

## 3. Objective peaks on the frontier

```text
n peak             = (0,0,6)
phi(n)/n peak      = (0,0,6)
tau peak           = (2,2,2)
sigma(n)/n peak    = (3,2,1)
```

The `n`, `tau`, and `sigma(n)/n` peaks lie in the connected 17-point component, so transitions between those objective optima can remain entirely on the global Pareto frontier. The `n` and `phi(n)/n` peaks coincide in this registered scope.

## 4. Interpretation

The Pareto frontier is not a smooth curve and not a single path. It is a finite graph with:

- two isolated extreme strategies;
- one cyclic core;
- three terminal branches;
- articulation points that mediate movement between tradeoff regions;
- bridges whose removal disconnects part of the frontier.

Hence the correct object is

\[
\boxed{\text{Pareto set} + \text{induced PVG adjacency graph}.}
\]

Global Pareto dominance and local navigability are distinct. A point may be globally optimal yet unreachable from another frontier point without temporarily leaving the frontier.

## 5. Scientific boundary

These results are exact for the declared axes, level, objectives, and maximize-all convention. They do not establish a general connectivity theorem, limiting frontier shape, asymptotic law, canonical continuous manifold, or originality claim.
