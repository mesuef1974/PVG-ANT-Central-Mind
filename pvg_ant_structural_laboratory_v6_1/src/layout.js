// PVG–ANT Structural Laboratory v6.1 — layout geometry and distortion diagnostics.
//
// Corrected framing (see README, corrections 1–3):
//  * Both layouts embed a p_k-smooth integer n as   X(n) = sum_p v_p(n) * log(p) * d_p ,
//    with unit prime directions d_p (|d_p| = 1).
//  * log-p weighting preserves motion length ONLY on a single prime ray. For general
//    points the triangle inequality gives only  |X(m) - X(n)| <= dlog(m, n) , with equality
//    on a single ray and directional compression / cancellation off it. The map to R^3
//    with more than three prime axes is necessarily low-rank: not injective, not isometric.
//  * The central axis of the cone layout is a VISUAL reference / symmetry axis only.
//    The all-ones vector 1 = (1,1,1,...) has infinite prime support, is not a positive
//    rational, and is not in l^1(P, log p) since sum_p log p diverges. It is never treated
//    as a computational PVG object.

import { factor, dlog as dlogInt } from './core/arithmetic.js';

const GOLDEN = 0.618033988749895;

function norm3(v){ const m = Math.hypot(v.x, v.y, v.z) || 1; return { x: v.x / m, y: v.y / m, z: v.z / m }; }

// ---- Legacy quasi-random directions (faithful reproduction of v6.0 primeDir) -------------
// Fixed hand-chosen directions for {2,3,5,7,11,13,19}; all other primes (incl. 17) fall to
// the golden-ratio azimuth + (p mod 11) polar generator. This preserves v6.0 behaviour
// exactly as the comparison baseline. 17 appears as an axis; only its DIRECTION is generated.
const FIXED_LEGACY = {
  2:  { x: -0.90, y:  0.18, z: 0.42 },
  3:  { x: -0.35, y:  0.88, z: 0.45 },
  5:  { x:  0.62, y:  0.72, z: 0.48 },
  7:  { x:  0.93, y:  0.10, z: 0.43 },
  11: { x:  0.58, y: -0.72, z: 0.48 },
  13: { x: -0.18, y: -0.91, z: 0.54 },
  19: { x: -0.78, y: -0.42, z: 0.56 }
};

export function legacyDirection(p){
  if (FIXED_LEGACY[p]) return norm3(FIXED_LEGACY[p]);
  const u = (p * GOLDEN) % 1, phi = u * 2 * Math.PI;
  const z = 0.28 + 0.34 * ((p % 11) / 10);
  const r = Math.sqrt(Math.max(0.05, 1 - z * z));
  return norm3({ x: r * Math.cos(phi), y: r * Math.sin(phi), z });
}

// ---- Symmetric cone: uniform polar angle theta to the visual reference axis y-hat = (0,1,0)
// d_j = ( sin(theta) cos(2*pi*j/k), cos(theta), sin(theta) sin(2*pi*j/k) ).
// Properties: |d_j| = 1 ; d_j · y-hat = cos(theta) (uniform polar angle) ; uniform azimuth ;
// rotational symmetry ; sum_j (d_j.x, d_j.z) = 0. NOT pairwise-equiangular (impossible for an
// arbitrary count of rays in R^3; the non-degenerate simplex construction stops at 4 vectors).
export const CONE_THETA = 60 * Math.PI / 180; // visual layout parameter.
export const REFERENCE_AXIS = { x: 0, y: 1, z: 0 };

export function coneDirections(k, theta = CONE_THETA){
  const s = Math.sin(theta), c = Math.cos(theta), out = [];
  for (let j = 0; j < k; j++) {
    const a = 2 * Math.PI * j / k;
    out.push({ x: s * Math.cos(a), y: c, z: s * Math.sin(a) });
  }
  return out;
}

export function directionsFor(mode, primes, theta = CONE_THETA){
  if (mode === 'cone') {
    const dirs = coneDirections(primes.length, theta), map = {};
    primes.forEach((p, j) => { map[p] = dirs[j]; });
    return map;
  }
  const map = {};
  primes.forEach(p => { map[p] = legacyDirection(p); });
  return map;
}

// ---- Embedding X(n) = sum over the chosen prime axes of v_p * log(p) * d_p ---------------
export function embed(exps, primes, logP, dirMap){
  let x = 0, y = 0, z = 0;
  for (let t = 0; t < primes.length; t++) {
    const e = exps[t];
    if (!e) continue;
    const w = e * logP[t], d = dirMap[primes[t]];
    x += d.x * w; y += d.y * w; z += d.z * w;
  }
  return { x, y, z };
}

// ---- p_k-smooth integers <= limit, with exponent vectors over the chosen primes ----------
export function smoothPoints(primes, limit, budget = 2_000_000){
  const logP = primes.map(p => Math.log(p));
  const points = [];
  const state = { nodes: 0, aborted: false };
  const exps = new Array(primes.length).fill(0);
  (function rec(i, cur){
    if (state.aborted) return;
    if (++state.nodes > budget) { state.aborted = true; return; }
    if (i === primes.length) { points.push({ n: cur, exps: exps.slice() }); return; }
    const p = primes[i];
    let v = cur, e = 0;
    while (v <= limit) {
      exps[i] = e; rec(i + 1, v);
      if (state.aborted) return;
      if (v > Math.floor(limit / p)) break;
      v *= p; e++;
    }
    exps[i] = 0;
  })(0, 1);
  points.sort((a, b) => a.n - b.n);
  return { points, logP, aborted: state.aborted };
}

function dlogExp(a, b, logP){
  let s = 0;
  for (let t = 0; t < logP.length; t++) s += Math.abs(a[t] - b[t]) * logP[t];
  return s;
}

// ---- Spearman rank correlation (self-contained) -----------------------------------------
function ranks(a){
  const z = a.map((v, i) => ({ v, i })).sort((x, y) => x.v - y.v), r = new Array(a.length);
  for (let i = 0; i < z.length;) {
    let j = i + 1;
    while (j < z.length && z[j].v === z[i].v) j++;
    const q = (i + j - 1) / 2 + 1;
    for (let k = i; k < j; k++) r[z[k].i] = q;
    i = j;
  }
  return r;
}
function pearson(x, y){
  const n = Math.min(x.length, y.length);
  if (n < 3) return NaN;
  let mx = 0, my = 0;
  for (let i = 0; i < n; i++) { mx += x[i]; my += y[i]; }
  mx /= n; my /= n;
  let num = 0, dx = 0, dy = 0;
  for (let i = 0; i < n; i++) { const a = x[i] - mx, b = y[i] - my; num += a * b; dx += a * a; dy += b * b; }
  return dx && dy ? num / Math.sqrt(dx * dy) : NaN;
}
export function spearman(x, y){ return pearson(ranks(x), ranks(y)); }

function quantile(sorted, q){
  if (!sorted.length) return NaN;
  const z = (sorted.length - 1) * q, i = Math.floor(z), t = z - i;
  return sorted[i] * (1 - t) + (sorted[i + 1] ?? sorted[i]) * t;
}

// ---- Distortion diagnostics over the (m,n) pairs of an embedded point set ----------------
// rho(m,n) = |X(m) - X(n)| / dlog(m,n) in [0,1] (guaranteed <= 1 by the triangle inequality).
export function distortion(points, primes, logP, dirMap, opts = {}){
  const cap = opts.cap ?? 500;
  const epsilon = opts.epsilon ?? 1e-6;
  const pts = points.slice(0, cap).map(p => ({ n: p.n, exps: p.exps, X: embed(p.exps, primes, logP, dirMap) }));
  const rhos = [], dEs = [], dLs = [];
  let collisions = 0, nearest = null, maxRho = 0;
  for (let i = 0; i < pts.length; i++) {
    for (let j = i + 1; j < pts.length; j++) {
      const a = pts[i], b = pts[j];
      const dE = Math.hypot(a.X.x - b.X.x, a.X.y - b.X.y, a.X.z - b.X.z);
      const dL = dlogExp(a.exps, b.exps, logP);
      if (dL <= 0) continue;
      const rho = dE / dL;
      rhos.push(rho); dEs.push(dE); dLs.push(dL);
      if (rho > maxRho) maxRho = rho;
      if (dE < epsilon) collisions++;
      if (!nearest || dE < nearest.dE) nearest = { a: a.n, b: b.n, dE, dLog: dL, rho };
    }
  }
  const sortedRho = rhos.slice().sort((x, y) => x - y);
  return {
    pairs: rhos.length,
    minRho: sortedRho[0] ?? NaN,
    p5Rho: quantile(sortedRho, 0.05),
    medianRho: quantile(sortedRho, 0.5),
    maxRho,
    spearman: spearman(dEs, dLs),
    collisions,
    epsilon,
    nearest
  };
}

// ---- Mandatory geometric self-checks (mirrored by tests/layout.test.mjs) ------------------
export function coneChecks(k, theta = CONE_THETA, tol = 1e-9){
  const dirs = coneDirections(k, theta), c = Math.cos(theta);
  const checks = { unit: true, polar: true, horizontalSum: true };
  let sx = 0, sz = 0;
  for (const d of dirs) {
    if (Math.abs(Math.hypot(d.x, d.y, d.z) - 1) > tol) checks.unit = false;
    if (Math.abs((d.x * REFERENCE_AXIS.x + d.y * REFERENCE_AXIS.y + d.z * REFERENCE_AXIS.z) - c) > tol) checks.polar = false;
    sx += d.x; sz += d.z;
  }
  if (Math.hypot(sx, sz) > 1e-9) checks.horizontalSum = false;
  checks.pass = checks.unit && checks.polar && checks.horizontalSum;
  return checks;
}
