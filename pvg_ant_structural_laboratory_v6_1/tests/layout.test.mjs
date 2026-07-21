// PVG–ANT Structural Laboratory v6.1 — mandatory geometry + core tests.
// Run: node --test
import test from 'node:test';
import assert from 'node:assert/strict';
import { dlog, factor, firstPrimes } from '../src/core/arithmetic.js';
import {
  coneDirections, coneChecks, CONE_THETA, REFERENCE_AXIS,
  directionsFor, smoothPoints, embed
} from '../src/layout.js';

const EPS = 1e-9;

test('core: dlog(60,72) = log 30', () => {
  assert.ok(Math.abs(dlog(60, 72) - Math.log(30)) < 1e-12);
});

test('core: factor(360) = 2^3 * 3^2 * 5', () => {
  assert.deepEqual(factor(360), { 2: 3, 3: 2, 5: 1 });
});

test('core: firstPrimes(8) includes 17, no skip', () => {
  assert.deepEqual(firstPrimes(8), [2, 3, 5, 7, 11, 13, 17, 19]);
});

test('cone: |d_j| = 1 for all axes', () => {
  for (const k of [2, 3, 4, 5, 6, 7, 9, 12, 16, 20]) {
    for (const d of coneDirections(k)) {
      assert.ok(Math.abs(Math.hypot(d.x, d.y, d.z) - 1) < EPS);
    }
  }
});

test('cone: d_j · y-hat = cos(theta) (uniform polar angle)', () => {
  const c = Math.cos(CONE_THETA);
  for (const k of [2, 3, 4, 5, 6, 7, 9, 12, 16, 20]) {
    for (const d of coneDirections(k)) {
      const dot = d.x * REFERENCE_AXIS.x + d.y * REFERENCE_AXIS.y + d.z * REFERENCE_AXIS.z;
      assert.ok(Math.abs(dot - c) < EPS);
    }
  }
});

test('cone: sum of horizontal components ~ 0', () => {
  for (const k of [2, 3, 4, 5, 6, 7, 9, 12, 16, 20]) {
    let sx = 0, sz = 0;
    for (const d of coneDirections(k)) { sx += d.x; sz += d.z; }
    assert.ok(Math.hypot(sx, sz) < EPS);
  }
});

test('cone: aggregate self-check passes for every supported axis count', () => {
  for (const k of [2, 3, 4, 5, 6, 7, 9, 12, 16, 20]) {
    assert.equal(coneChecks(k).pass, true, `coneChecks(${k})`);
    assert.equal(coneDirections(k).length, k);
    assert.equal(firstPrimes(k).length, k);
  }
});

test('bound: d_E(m,n) <= d_log(m,n) + eps for BOTH layouts', () => {
  const primes = firstPrimes(9); // includes 17, 19, 23
  const logP = primes.map(p => Math.log(p));
  const { points } = smoothPoints(primes, 5000, 500000);
  const sample = points.slice(0, 260);
  for (const mode of ['legacy', 'cone']) {
    const dirs = directionsFor(mode, primes);
    const X = sample.map(p => embed(p.exps, primes, logP, dirs));
    for (let i = 0; i < sample.length; i++) {
      for (let j = i + 1; j < sample.length; j++) {
        const dE = Math.hypot(X[i].x - X[j].x, X[i].y - X[j].y, X[i].z - X[j].z);
        let dL = 0;
        for (let t = 0; t < primes.length; t++) dL += Math.abs(sample[i].exps[t] - sample[j].exps[t]) * logP[t];
        assert.ok(dE <= dL + 1e-9, `${mode}: dE ${dE} > dLog ${dL} for ${sample[i].n},${sample[j].n}`);
      }
    }
  }
});

test('equality: on a single prime ray rho = 1 (e.g. 2 vs 4 vs 8)', () => {
  const primes = firstPrimes(6);
  const logP = primes.map(p => Math.log(p));
  const dirs = directionsFor('cone', primes);
  const expOf = n => primes.map(p => { let e = 0, x = n; while (x % p === 0) { e++; x /= p; } return e; });
  const pairs = [[2, 4], [2, 8], [4, 8], [3, 9]];
  for (const [a, b] of pairs) {
    const Xa = embed(expOf(a), primes, logP, dirs), Xb = embed(expOf(b), primes, logP, dirs);
    const dE = Math.hypot(Xa.x - Xb.x, Xa.y - Xb.y, Xa.z - Xb.z);
    let dL = 0;
    const ea = expOf(a), eb = expOf(b);
    for (let t = 0; t < primes.length; t++) dL += Math.abs(ea[t] - eb[t]) * logP[t];
    assert.ok(Math.abs(dE / dL - 1) < 1e-12, `rho(${a},${b}) = ${dE / dL}`);
  }
});
