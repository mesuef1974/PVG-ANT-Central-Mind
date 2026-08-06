import assert from 'node:assert/strict';
import {factor,isPrime,isPrimePower,dlog} from '../src/core/arithmetic.js';
import {additiveFiber} from '../src/core/additive.js';
import {pearson,partialCorrelation} from '../src/core/statistics.js';
import {grid,geometricPoints} from '../src/core/smooth.js';
assert.deepEqual(factor(360),{'2':3,'3':2,'5':1});
assert.equal(isPrime(97),true);assert.equal(isPrime(1),false);assert.equal(isPrimePower(27),true);assert.equal(isPrimePower(12),false);
assert.ok(Math.abs(dlog(60,72)-Math.log(30))<1e-12);
const a=additiveFiber(10,5);assert.equal(a.counts.goldbach,3); // (3,7),(5,5),(7,3)
assert.equal(a.residue.reduce((s,r)=>s+r.all,0),9);
assert.ok(Number.isFinite(pearson([1,2,3],[2,4,6])));assert.ok(Number.isFinite(partialCorrelation([1,2,4,8],[1,2,3,7],[[1],[2],[3],[4]])));
const cells=grid(1000,[2,3,5],geometricPoints(10,1000,5),1000000);assert.ok(cells.length>=12);assert.ok(cells.every(c=>c.exact>=1&&Number.isFinite(c.error)));
console.log('PVG v6 core tests PASS');
