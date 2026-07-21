# PASS-011 — Multiobjective and Pareto Geometry on a PVG Level

**Program:** `PVG-INVERSE-GEOMETRY-001`  
**Registered scope:** axes `2,3,5`, level `Omega=6`  
**Status:** exact finite graph analysis  
**Scientific class:** finite multiobjective geometry / diagnostic organization; no asymptotic or novelty claim

---

## 1. Purpose

PASS-010 oriented each horizontal edge using one scalar arithmetic field at a time. PASS-011 studies several fields simultaneously.

For every horizontal edge between exponent vectors `a` and `b`, record

\[
\left(
\operatorname{sgn}\Delta n,
\operatorname{sgn}\Delta\tau,
\operatorname{sgn}\frac{\sigma}{n},
\operatorname{sgn}\frac{\varphi}{n}
\right).
\]

All four registered objectives are treated as quantities to maximize. This convention is explicit and is not claimed to be canonical for every application.

---

## 2. Dominance definitions

A point `x` weakly dominates `y` when

\[
f_i(x)\ge f_i(y)
\]

for every registered objective and

\[
f_j(x)>f_j(y)
\]

for at least one objective.

The global Pareto frontier consists of points not dominated by any point in the level. The local Pareto frontier consists of points not dominated by any horizontal neighbor.

Global nondominance implies local nondominance, but the converse need not hold.

---

## 3. Edge classes

An edge is classified from its sign vector.

- `aligned_increase`: every objective increases.
- `aligned_increase_with_ties`: no objective decreases and at least one increases.
- `aligned_decrease`: every objective decreases.
- `aligned_decrease_with_ties`: no objective increases and at least one decreases.
- `strict_tradeoff`: at least one objective increases and at least one decreases, with no ties.
- `tradeoff_with_ties`: both gains and losses occur, with at least one tied objective.
- `all_equal`: all objectives tie.

The stored edge orientation is the lexicographic order of exponent vectors. Therefore the raw sign pattern depends on that bookkeeping orientation. Pareto dominance and tradeoff status do not.

---

## 4. Exact finite results

The level contains

\[
\binom{8}{2}=28
\]

points and `63` undirected horizontal edges.

Under the registered objective vector:

```text
Pareto-dominance edges       = 8
tradeoff-or-equal edges      = 55
strict-tradeoff edges        = 30
tradeoff-with-ties edges     = 25
aligned-decrease-with-ties   = 8
```

The global Pareto frontier contains `19` points. The local Pareto frontier contains `21` points. Thus two points are locally nondominated but globally dominated by nonadjacent points.

Nine of the twenty-eight points are globally dominated.

The global frontier includes the distinguished single-field optima:

```text
(0,0,6)  = maximum n and maximum phi(n)/n
(2,2,2)  = maximum tau
(3,2,1)  = maximum sigma(n)/n
(6,0,0)  = minimum n, but still globally nondominated because of its objective tradeoffs
```

The last example is important: a point may be poor for one field and remain Pareto-efficient because no other point improves every registered field simultaneously.

---

## 5. Interpretation

The dominant phenomenon is conflict, not universal ascent:

\[
55/63
\]

edges fail to provide a Pareto improvement in either direction. Most horizontal moves improve some arithmetic observables while worsening others.

Consequently, PVG has no objective-independent gradient. A flow exists only after choosing:

1. one scalar field;
2. a weighted scalarization;
3. a lexicographic priority;
4. a Pareto rule;
5. or another decision convention.

This establishes a precise distinction between intrinsic horizontal geometry and observer-dependent arithmetic optimization.

---

## 6. Local versus global efficiency

A locally Pareto-efficient point has no improving adjacent transfer. It may still be dominated by a distant point requiring several transfers.

This produces a new inverse and dynamic question:

> Which locally efficient points are genuine global frontier points, and what minimum path length is required to reach a global dominator of a false local optimum?

PASS-011 records the two frontier sets but does not yet install a theorem or a general-distance analysis.

---

## 7. Installed analyzer

```text
tools/pvg_multiobjective_geometry.py
tests/test_pvg_multiobjective_geometry.py
```

Example:

```powershell
py.exe -3.12 tools\pvg_multiobjective_geometry.py "2,3,5" 6
```

The JSON report includes every edge signature, objective differences as exact rational numbers, dominance relations, global and local frontiers, and deterministic verification flags.

---

## 8. Scientific boundary

PASS-011 is an exact finite computation on one fixed face and level. Pareto membership depends on the chosen objective list and on treating all objectives as quantities to maximize. The pass does not provide asymptotic laws, a canonical utility function, a general extremal theorem, an originality certificate, or progress on Goldbach, RH, or GRH.
