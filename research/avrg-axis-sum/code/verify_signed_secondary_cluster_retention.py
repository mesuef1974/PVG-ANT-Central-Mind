"""Verify signed secondary cluster retention for reduced von-Mangoldt channels.

Range: 2 <= N <= 300, 1 <= r <= 20.
Compares K=0..3 major pairs and J=0..4 additional signed secondary pairs,
ordered by Fourier energy. The unresolved tail uses singleton absolute bounds.
"""

import cmath
import json
import math

MAX_N = 300
MAX_R = 20
TOL = 1e-9


def sieve(n):
    isp = [True] * (n + 1)
    isp[0] = isp[1] = False
    for p in range(2, int(n**0.5) + 1):
        if isp[p]:
            for m in range(p * p, n + 1, p):
                isp[m] = False
    return isp, [i for i, v in enumerate(isp) if v]


def main():
    isprime, primes = sieve(MAX_N)
    lam = [0.0] * (MAX_N + 1)
    is_hpp = [False] * (MAX_N + 1)
    for p in primes:
        x, exponent = p, 1
        while x <= MAX_N:
            lam[x] = math.log(p)
            if exponent >= 2:
                is_hpp[x] = True
            if x > MAX_N // p:
                break
            x *= p
            exponent += 1

    counts = {str(k): {str(j): 0 for j in range(5)} for k in range(4)}
    false = 0
    channels = 0
    prime_positive = 0
    monotonicity_failures = 0

    for N in range(2, MAX_N + 1):
        for r in range(1, MAX_R + 1):
            g = math.gcd(2, r)
            q = r // g
            u = 2 // g
            z = [0.0] * q
            zpp = [0.0] * q
            hpp = [0.0] * q
            for a in range(1, N):
                c = (u * a) % q
                z[c] += lam[a] * lam[N - a]
                if isprime[a] and isprime[N - a]:
                    zpp[c] += lam[a] * lam[N - a]
                if is_hpp[a]:
                    hpp[c] += lam[a]

            zhat = [sum(z[c] * cmath.exp(2j * math.pi * k * c / q) for c in range(q)) for k in range(q)]
            reps = list(range(1, (q - 1) // 2 + 1))
            ordered = sorted(reps, key=lambda k: abs(zhat[k]) ** 2, reverse=True)
            nyquist = q // 2 if q % 2 == 0 else None

            for c in range(q):
                channels += 1
                if zpp[c] > TOL:
                    prime_positive += 1
                contamination = math.log(N) * (hpp[c] + hpp[(u * N - c) % q])
                previous = -float("inf")
                for total_retained in range(0, 8):
                    retained = set(ordered[:total_retained])
                    unresolved = [k for k in ordered if k not in retained]
                    lower = zhat[0].real / q
                    if nyquist is not None:
                        lower += (zhat[nyquist] * cmath.exp(-2j * math.pi * nyquist * c / q)).real / q
                    lower += sum((2 / q) * (zhat[k] * cmath.exp(-2j * math.pi * k * c / q)).real for k in retained)
                    lower -= sum((2 / q) * abs((zhat[k] * cmath.exp(-2j * math.pi * k * c / q)).real) for k in unresolved)
                    if lower + TOL < previous:
                        monotonicity_failures += 1
                    previous = lower

                for k_major in range(4):
                    for j_secondary in range(5):
                        retained_count = k_major + j_secondary
                        retained = set(ordered[:retained_count])
                        unresolved = [k for k in ordered if k not in retained]
                        lower = zhat[0].real / q
                        if nyquist is not None:
                            lower += (zhat[nyquist] * cmath.exp(-2j * math.pi * nyquist * c / q)).real / q
                        lower += sum((2 / q) * (zhat[k] * cmath.exp(-2j * math.pi * k * c / q)).real for k in retained)
                        lower -= sum((2 / q) * abs((zhat[k] * cmath.exp(-2j * math.pi * k * c / q)).real) for k in unresolved)
                        if lower > contamination + TOL:
                            counts[str(k_major)][str(j_secondary)] += 1
                            if zpp[c] <= TOL:
                                false += 1

    result = {
        "schema": "pvg.signed-secondary-cluster-retention.v1",
        "status": "PASS" if false == 0 and monotonicity_failures == 0 else "FAIL",
        "range": {"N": [2, MAX_N], "r": [1, MAX_R]},
        "effective_channels": channels,
        "prime_positive_channels": prime_positive,
        "certificate_counts": counts,
        "false_certificates": false,
        "monotonicity_failures": monotonicity_failures,
        "note": "Counts depend on the total number K+J of exactly retained energy-ordered pairs; exact regrouping into clusters is invariant."
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
