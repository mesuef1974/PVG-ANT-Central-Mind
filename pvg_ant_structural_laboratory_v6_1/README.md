# PVG–ANT Structural Laboratory v6.1 — comparison layout experiment

External research application. v6.0 is **frozen and unchanged**; v6.1 is a new, independent asset
that studies how much a chosen 3-D layout distorts the PVG log-weighted valuation metric. It does
**not** replace v6.0 and makes **no** claim of preserving the geometry.

## Run

```bash
python -m http.server 8010    # then open http://localhost:8010
node --test                   # mandatory geometry + core tests
```

## Modules

- `src/core/arithmetic.js` — exact arithmetic / PVG core (identical proven logic to v6.0).
- `src/layout.js` — legacy and cone directions, embedding, distortion diagnostics, self-checks.
- `src/app.js` — comparison UI (lattice, distortion panel, geometry checks, export).
- `tests/layout.test.mjs` — mandatory tests.

## Embedding

Each `p_k`-smooth integer is embedded as `X(n) = Σ_p v_p(n)·log(p)·d_p`, `|d_p| = 1`, with the
**same** log-weighting in both layouts; only the unit directions `d_p` differ.

- **Legacy quasi-random**: faithful reproduction of the v6.0 `primeDir` (fixed directions for
  {2,3,5,7,11,13,19}; golden-ratio azimuth + `p mod 11` polar for the rest). Every prime up to
  `p_k` — including 17 — is an axis; in this mode only its *direction* is generated.
- **Symmetric cone**: `d_j = (sinθ·cos(2πj/k), cosθ, sinθ·sin(2πj/k))`, uniform polar angle `θ`
  (default 60°) to the visual reference axis `ŷ`. This is a *symmetric conic layout with uniform
  polar angle* — **not** a pairwise-equiangular frame (impossible for an arbitrary number of rays
  in R³). Prime order maps to azimuth. The vertical coordinate is `X_y(n) = cos(θ)·log n`
  (proportional to log n, not log n literally). The layout is **distinct per k** (axis j at azimuth
  2πj/k), not a nested embedding — changing k re-places most existing primes.

## Corrections embodied (vs the earlier review)

1. **The Euclidean distance does not approximate `d_log`.** Only the triangle-inequality bound
   `|X(m)−X(n)| ≤ d_log(m,n)` holds, with equality on a single prime ray. With more than three
   axes the map to R³ is low-rank: not injective, not isometric. The distortion panel reports
   `ρ(m,n) = |X(m)−X(n)| / d_log(m,n) ∈ [0,1]`.
2. **Symmetry name.** Uniform polar angle, uniform azimuth, rotational symmetry — not pairwise
   equiangular.
3. **The central axis is visual only.** `1 = (1,1,1,…)` has infinite prime support, is not a
   positive rational, and is not in `ℓ¹(P, log p)` since `Σ_p log p` diverges. It is a reference /
   symmetry axis for the drawing, never a computational PVG object.
4. **No skipped primes.** The axis set is the first `k` primes in order (…, 13, 17, 19, …).

## Distortion diagnostics (per layout, over a 400-point sample)

Sample modes: `logstrat` (default — log-stratified across the range), `first` (biased to the low
end), `all` (when the count is small). Reported per layout: `min ρ`, 5th-percentile `ρ`, median `ρ`,
max `ρ` (≤ 1), `Spearman(d_E, d_log)`, collision count (`d_E < 1e-6`), and the nearest pair **in the
R³ embedding** (before camera rotation / 2-D screen projection — not a screen-space pair). The
sample's n-values are exported in the JSON. If the smooth-number enumeration exceeds the node budget
(`aborted`), the metrics are disabled and the panel shows `PARTIAL ENUMERATION — DIAGNOSTICS INVALID`.

## Mandatory geometric tests

`|d_j| = 1`, `d_j·ŷ = cosθ`, `Σ_j (d_{j,x}, d_{j,z}) ≈ 0`, and `d_E(m,n) ≤ d_log(m,n) + ε` for
sampled pairs in **both** layouts.

## Scientific ceiling

Finite exact identities and computational diagnostics only. No uniform error theorem, geometry
preservation, Goldbach proof, RH/GRH progress, or originality claim.
