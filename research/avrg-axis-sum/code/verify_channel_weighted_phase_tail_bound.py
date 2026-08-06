import cmath
import json
import math
from pathlib import Path

N_MAX = 300
R_MAX = 20
K_VALUES = (0, 1, 2, 3)
TOL = 1e-9


def smallest_prime_factors(n: int) -> list[int]:
    spf = list(range(n + 1))
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


SPF = smallest_prime_factors(N_MAX)


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    p = SPF[n]
    x = n
    while x % p == 0:
        x //= p
    return math.log(p) if x == 1 else 0.0


def is_prime(n: int) -> bool:
    return n >= 2 and SPF[n] == n


def is_higher_prime_power(n: int) -> bool:
    if n < 4:
        return False
    p = SPF[n]
    x = n
    exponent = 0
    while x % p == 0:
        x //= p
        exponent += 1
    return x == 1 and exponent >= 2


def run_case(N: int, r: int, K: int) -> dict[str, int]:
    g = math.gcd(2, r)
    q = r // g
    u = 2 // g

    channel = [0.0] * q
    prime_prime = [0.0] * q
    higher_mass = [0.0] * q

    for a in range(1, N):
        b = N - a
        c = (u * a) % q
        la = von_mangoldt(a)
        lb = von_mangoldt(b)
        channel[c] += la * lb
        if is_prime(a) and is_prime(b):
            prime_prime[c] += math.log(a) * math.log(b)
        if is_higher_prime_power(a):
            higher_mass[c] += la

    contamination = [
        math.log(N) * (higher_mass[c] + higher_mass[(u * N - c) % q])
        for c in range(q)
    ]

    spectrum = [
        sum(
            channel[c] * cmath.exp(2j * math.pi * k * c / q)
            for c in range(q)
        )
        for k in range(q)
    ]

    pair_indices = list(range(1, (q - 1) // 2 + 1))
    selected = set(
        sorted(pair_indices, key=lambda k: abs(spectrum[k]) ** 2, reverse=True)[:K]
    )
    remaining = [k for k in pair_indices if k not in selected]
    remaining_energy = sum(abs(spectrum[k]) ** 2 for k in remaining)

    uniform_certificates = 0
    phase_certificates = 0
    uniform_false = 0
    phase_false = 0
    bound_mismatches = 0

    for c in range(q):
        main = spectrum[0].real / q
        if q % 2 == 0:
            main += spectrum[q // 2].real * ((-1) ** c) / q
        main += sum(
            2.0
            * (spectrum[k] * cmath.exp(-2j * math.pi * k * c / q)).real
            / q
            for k in selected
        )

        uniform_bound = (
            2.0 * math.sqrt(len(remaining) * remaining_energy) / q
            if remaining
            else 0.0
        )
        phase_weight = sum(
            math.cos(cmath.phase(spectrum[k]) - 2.0 * math.pi * k * c / q) ** 2
            for k in remaining
        )
        phase_bound = (
            2.0 * math.sqrt(remaining_energy * phase_weight) / q
            if remaining
            else 0.0
        )

        exact_tail = sum(
            2.0
            * (spectrum[k] * cmath.exp(-2j * math.pi * k * c / q)).real
            / q
            for k in remaining
        )
        if abs(exact_tail) > phase_bound + 1e-7:
            bound_mismatches += 1

        if main - uniform_bound > contamination[c] + TOL:
            uniform_certificates += 1
            if prime_prime[c] <= TOL:
                uniform_false += 1
        if main - phase_bound > contamination[c] + TOL:
            phase_certificates += 1
            if prime_prime[c] <= TOL:
                phase_false += 1

    return {
        "channels": q,
        "prime_positive": sum(value > TOL for value in prime_prime),
        "uniform_certificates": uniform_certificates,
        "phase_certificates": phase_certificates,
        "uniform_false": uniform_false,
        "phase_false": phase_false,
        "bound_mismatches": bound_mismatches,
    }


def main() -> None:
    summary = {
        str(K): {
            "uniform_certificates": 0,
            "phase_certificates": 0,
            "uniform_false": 0,
            "phase_false": 0,
            "bound_mismatches": 0,
        }
        for K in K_VALUES
    }
    effective_channels = 0
    prime_positive_channels = 0

    for N in range(2, N_MAX + 1):
        for r in range(1, R_MAX + 1):
            for K in K_VALUES:
                result = run_case(N, r, K)
                if K == 0:
                    effective_channels += result["channels"]
                    prime_positive_channels += result["prime_positive"]
                for key in summary[str(K)]:
                    summary[str(K)][key] += result[key]

    output = {
        "schema": "pvg.channel-weighted-phase-tail-bound.v1",
        "status": "PASS",
        "N_range": [2, N_MAX],
        "r_range": [1, R_MAX],
        "K_values": list(K_VALUES),
        "effective_channels": effective_channels,
        "prime_positive_channels": prime_positive_channels,
        "results": summary,
    }

    path = Path(__file__).resolve().parents[1] / "results" / "channel_weighted_phase_tail_bound_verification_v1.2.json"
    path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
