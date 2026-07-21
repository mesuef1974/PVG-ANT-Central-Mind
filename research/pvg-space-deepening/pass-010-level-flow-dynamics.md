# PASS-010 — PVG Level Flow Dynamics

**Scope:** axes `{2,3,5}`, level `Omega=6`, 28 lattice points.  
**Status:** exact finite graph dynamics.  
**Scientific class:** finite identities and deterministic diagnostics; no asymptotic or novelty claim.

## 1. Flow construction

For a scalar arithmetic field `f` on one fixed PVG level, orient every primitive horizontal edge by

\[
x\to y\iff f(y)>f(x).
\]

Equal-value edges form plateau components. Contracting each plateau produces the plateau-condensation graph.

Because `f` strictly increases along every oriented edge, the strict flow and the plateau condensation are directed acyclic graphs. This is a theorem of the construction, not an empirical pattern.

## 2. Registered fields

The first pass studies

\[
n,\qquad \tau(n),\qquad \frac{\sigma(n)}n,\qquad \frac{\varphi(n)}n.
\]

They represent four geometrically distinct regimes:

- `n`: log-linear axis-weighted size field;
- `tau`: exponent-shape balancing field;
- `sigma/n`: axis-weighted interior abundance field;
- `phi/n`: support-stratified plateau field.

## 3. Exact finite extrema

On `{2,3,5}`, `Omega=6`:

- `n` has unique minimum `(6,0,0)` and unique maximum `(0,0,6)`;
- `tau` has unique global maximum `(2,2,2)`;
- `sigma/n` has unique global maximum `(3,2,1)`;
- `phi/n` has a ten-point global-minimum plateau consisting exactly of full-support points.

## 4. Strongest ascent

At each non-sink point choose an outgoing neighbor with maximal immediate increase in the field. Deterministic tie-breaking yields one strongest-ascent path from every point. Every such path terminates at a local maximum because the strict flow is finite and acyclic.

The resulting terminal partition is the strongest-ascent basin decomposition. It is algorithm-dependent when immediate increases tie, whereas the set of strict sinks and plateau components is intrinsic to the field.

## 5. Geometric interpretation

The same PVG level supports incompatible winds:

- size pushes valuation mass toward the largest prime axis;
- divisor count pushes toward balanced exponents;
- abundance pushes toward a weighted balance favoring small primes;
- normalized totient is constant on support strata and changes only when a boundary is crossed.

Thus a PVG point can be uphill for one arithmetic field and downhill for another. There is no field-independent notion of ascent.

## 6. Installed capability

`tools/pvg_level_flow.py` emits, for each field:

- strict and equal edge counts;
- local and global maxima/minima;
- plateau components;
- acyclicity certificates;
- strongest-ascent paths;
- strongest-ascent basins;
- sink counts.

`tests/test_pvg_level_flow.py` verifies the registered scope, extrema, plateau behavior, path termination, and acyclicity.

## 7. Boundaries

This pass does not establish limiting flow laws as the level or number of axes grows. It does not identify a canonical continuous differential structure. Strongest-ascent basins depend on the declared tie-break rule. No claim is made about originality, factorization speedup, Goldbach, RH, or GRH.
