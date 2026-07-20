// PVG–ANT Structural Laboratory v6.1 — exact arithmetic / PVG core.
// Identical proven logic to v6.0 arithmetic.js (verified). No claim beyond finite exact identities.

export function factor(n){
  n = Math.trunc(Number(n));
  const f = {};
  let x = n;
  for (let p = 2; p * p <= x; p++) {
    while (x % p === 0) { f[p] = (f[p] || 0) + 1; x /= p; }
  }
  if (x > 1) f[x] = (f[x] || 0) + 1;
  return f;
}

export function isPrime(n){
  n = Math.trunc(Number(n));
  if (n < 2) return false;
  if (n % 2 === 0) return n === 2;
  for (let p = 3; p * p <= n; p += 2) if (n % p === 0) return false;
  return true;
}

export function isPrimePower(n){
  if (n < 2) return false;
  return Object.keys(factor(n)).length === 1;
}

export function omega(f){ return Object.keys(f).length; }
export function bigOmega(f){ return Object.values(f).reduce((a, b) => a + b, 0); }
export function maxPrime(f){ const a = Object.keys(f).map(Number); return a.length ? Math.max(...a) : 1; }

export function factText(f){
  const a = Object.entries(f);
  return a.length ? a.map(([p, e]) => e === 1 ? p : `${p}^${e}`).join(' × ') : '1';
}

export function gcd(a, b){ a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; }

// dlog(a,b) = sum_p |v_p(a) - v_p(b)| log p = log( lcm(a,b) / gcd(a,b) ).
export function dlog(a, b){
  const fa = factor(a), fb = factor(b);
  const ps = new Set([...Object.keys(fa), ...Object.keys(fb)]);
  let s = 0;
  for (const ps0 of ps) {
    const p = Number(ps0);
    s += Math.abs((fa[p] || 0) - (fb[p] || 0)) * Math.log(p);
  }
  return s;
}

export function primesUpTo(y){
  const a = [];
  for (let n = 2; n <= y; n++) if (isPrime(n)) a.push(n);
  return a;
}

// First k primes in order — NO skips (2,3,5,7,11,13,17,19,23,...).
export function firstPrimes(k){
  const a = [];
  for (let n = 2; a.length < k; n++) if (isPrime(n)) a.push(n);
  return a;
}
