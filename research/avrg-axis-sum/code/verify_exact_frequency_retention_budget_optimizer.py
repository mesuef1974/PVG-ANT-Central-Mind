"""Exact finite benchmark for frequency-retention design.

Range: 2<=N<=200, 1<=r<=20, budgets 0..4.
Outputs aggregate certificate counts for energy, greedy, and exhaustive exact selection.
"""
from __future__ import annotations
import cmath, itertools, json, math
from pathlib import Path

MAX_N, MAX_R, BUDGETS = 200, 20, range(5)
TOL = 1e-10


def sieve(n: int) -> list[bool]:
    p = [True] * (n + 1); p[0] = p[1] = False
    for a in range(2, int(n**0.5) + 1):
        if p[a]:
            for b in range(a*a, n + 1, a): p[b] = False
    return p

PRIME = sieve(MAX_N)


def lam(n: int) -> float:
    if n < 2: return 0.0
    if PRIME[n]: return math.log(n)
    for p in range(2, int(n**0.5) + 1):
        if not PRIME[p]: continue
        x = p * p
        while x < n: x *= p
        if x == n: return math.log(p)
    return 0.0

LAMBDA = [lam(n) for n in range(MAX_N + 1)]


def case_data(N: int, r: int):
    g = math.gcd(2, r); q = r // g; u = 2 // g
    weights = [LAMBDA[a] * LAMBDA[N-a] for a in range(1, N)]
    channels = [(u*a) % q for a in range(1, N)]
    zhat = []
    for k in range(q):
        zhat.append(sum(weights[j] * cmath.exp(2j*math.pi*k*channels[j]/q) for j in range(N-1)))
    base = [sum(weights)/q] * q
    if q % 2 == 0:
        k = q // 2
        for c in range(q): base[c] += (zhat[k] * cmath.exp(-2j*math.pi*k*c/q) / q).real
    pairs = list(range(1, (q-1)//2 + 1))
    contrib = {k: [(2/q) * (zhat[k] * cmath.exp(-2j*math.pi*k*c/q)).real for c in range(q)] for k in pairs}
    hpp = [0.0] * q
    for a in range(1, N):
        if LAMBDA[a] and not PRIME[a]: hpp[(u*a) % q] += LAMBDA[a]
    contam = [math.log(N) * (hpp[c] + hpp[(u*N-c) % q]) for c in range(q)]
    pp = [0.0] * q
    for a in range(1, N):
        if PRIME[a] and PRIME[N-a]: pp[(u*a) % q] += math.log(a) * math.log(N-a)
    return q, pairs, zhat, base, contrib, contam, pp


def certificate(base, contrib, contam, chosen):
    keys = list(contrib)
    low = base[:]
    for k in keys:
        v = contrib[k]
        if k in chosen:
            low = [x+y for x,y in zip(low, v)]
        else:
            low = [x-abs(y) for x,y in zip(low, v)]
    cert = [low[c] > contam[c] + TOL for c in range(len(low))]
    return sum(cert), cert


def main() -> None:
    agg = {m:{str(b):0 for b in BUDGETS} for m in ("energy","greedy","exact")}
    false = {m:{str(b):0 for b in BUDGETS} for m in agg}
    positive = channels_total = greedy_suboptimal = 0
    witness = None
    for N in range(2, MAX_N + 1):
        for r in range(1, MAX_R + 1):
            q, keys, zhat, base, contrib, contam, pp = case_data(N, r)
            channels_total += q; positive += sum(x > TOL for x in pp)
            energy_order = sorted(keys, key=lambda k: abs(zhat[k])**2, reverse=True)
            greedy_sets = {0:set()}; G = set()
            for b in range(1, 5):
                rem = [k for k in keys if k not in G]
                if rem:
                    k = max(rem, key=lambda j: (certificate(base,contrib,contam,G|{j})[0], j))
                    G.add(k)
                greedy_sets[b] = set(G)
            exact_sets = {}
            for b in BUDGETS:
                best = (-1, set())
                for size in range(min(b, len(keys)) + 1):
                    for tup in itertools.combinations(keys, size):
                        count, _ = certificate(base, contrib, contam, set(tup))
                        if count > best[0]: best = (count, set(tup))
                exact_sets[b] = best[1]
            for b in BUDGETS:
                choices = {"energy":set(energy_order[:b]), "greedy":greedy_sets[b], "exact":exact_sets[b]}
                for name, chosen in choices.items():
                    count, cert = certificate(base, contrib, contam, chosen)
                    agg[name][str(b)] += count
                    false[name][str(b)] += sum(cert[c] and pp[c] <= TOL for c in range(q))
                if certificate(base,contrib,contam,greedy_sets[b])[0] < certificate(base,contrib,contam,exact_sets[b])[0]:
                    greedy_suboptimal += 1
                    if witness is None:
                        witness = {"N":N,"r":r,"q":q,"budget":b,"greedy":sorted(greedy_sets[b]),"exact":sorted(exact_sets[b]),"greedy_count":certificate(base,contrib,contam,greedy_sets[b])[0],"exact_count":certificate(base,contrib,contam,exact_sets[b])[0]}
    out = {"schema":"pvg.frequency-retention.exact-budget.v1","status":"PASS" if all(v==0 for m in false.values() for v in m.values()) else "FAIL","range":{"N":[2,MAX_N],"r":[1,MAX_R],"budgets":list(BUDGETS)},"effective_channels":channels_total,"prime_positive_channels":positive,"certificate_counts":agg,"false_certificates":false,"greedy_suboptimal_instances":greedy_suboptimal,"first_witness":witness}
    path = Path(__file__).resolve().parents[1] / "results" / "exact_frequency_retention_budget_optimizer_verification_v1.2.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))

if __name__ == "__main__": main()
