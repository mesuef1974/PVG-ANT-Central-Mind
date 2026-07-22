from __future__ import annotations

import argparse
import json
from collections import Counter
from math import gcd

try:
    from tools.pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        integer_fiber,
        support_key,
        support_universe,
    )
    from tools.pvg_inverse_prime_fibers import prime_pair_fiber
    from tools.pvg_local_additive_cell_atlas import is_prime
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        integer_fiber,
        support_key,
        support_universe,
    )
    from pvg_inverse_prime_fibers import prime_pair_fiber
    from pvg_local_additive_cell_atlas import is_prime


def primes_up_to(limit: int) -> tuple[int, ...]:
    if limit < 2:
        return tuple()
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if flags[p]:
            flags[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
        p += 1
    return tuple(i for i, flag in enumerate(flags) if flag)


def local_obstruction_record(m: int, d: int, ell: int) -> dict[str, object]:
    if m <= 0 or not (0 < d < m) or ell < 2 or not is_prime(ell):
        raise ValueError("invalid midpoint-radius-local-prime input")
    left, right = m - d, m + d
    left_hit = left % ell == 0
    right_hit = right % ell == 0
    left_boundary = left_hit and left == ell
    right_boundary = right_hit and right == ell
    left_obstruction = left_hit and not left_boundary
    right_obstruction = right_hit and not right_boundary
    return {
        "midpoint": m,
        "radius": d,
        "local_prime": ell,
        "left": left,
        "right": right,
        "minus_residue_hit": m % ell == d % ell,
        "plus_residue_hit": m % ell == (-d) % ell,
        "left_divisible": left_hit,
        "right_divisible": right_hit,
        "left_boundary_exception": left_boundary,
        "right_boundary_exception": right_boundary,
        "left_obstruction": left_obstruction,
        "right_obstruction": right_obstruction,
        "obstructed": left_obstruction or right_obstruction,
    }


def boundary_exception_record(m: int, d: int, ell: int) -> dict[str, object]:
    record = local_obstruction_record(m, d, ell)
    return {
        "midpoint": m,
        "radius": d,
        "local_prime": ell,
        "left_boundary_exception": record["left_boundary_exception"],
        "right_boundary_exception": record["right_boundary_exception"],
        "is_boundary_exception": bool(record["left_boundary_exception"] or record["right_boundary_exception"]),
    }


def local_obstruction_signature(m: int, d: int, prime_limit: int) -> dict[str, object]:
    local_primes = tuple(p for p in primes_up_to(prime_limit) if p % 2 == 1)
    records = [local_obstruction_record(m, d, ell) for ell in local_primes]
    obstructing = [int(r["local_prime"]) for r in records if r["obstructed"]]
    boundaries = [int(r["local_prime"]) for r in records if r["left_boundary_exception"] or r["right_boundary_exception"]]
    return {
        "midpoint": m,
        "radius": d,
        "prime_limit": prime_limit,
        "obstructing_primes": obstructing,
        "boundary_exception_primes": boundaries,
        "locally_survives": not obstructing,
    }


def even_coordinate_owner_certificate(n: int, d: int, prime_limit: int = REGISTERED_SUPPORT_PRIME_LIMIT) -> dict[str, object]:
    if n <= 0 or n % 2:
        raise ValueError("even owner certificate requires positive even n")
    m = n // 2
    if not (0 < d < m):
        raise ValueError("radius must satisfy 0<d<n/2")
    left, right = m - d, m + d
    owner = left < right and is_prime(left) and is_prime(right)
    actual_radii = {((q - p) // 2) for p, q in prime_pair_fiber(n)}
    signature = local_obstruction_signature(m, d, prime_limit)
    return {
        "integer": n,
        "midpoint": m,
        "radius": d,
        "left": left,
        "right": right,
        "gcd_midpoint_radius": gcd(m, d),
        "square_difference": m * m - d * d,
        "factor_product": left * right,
        "square_difference_identity": m * m - d * d == left * right,
        "owner_by_primality": owner,
        "owner_by_registered_fiber": d in actual_radii,
        "owner_equivalence": owner == (d in actual_radii),
        "local_signature": signature,
    }


def odd_coordinate_owner_certificate(n: int) -> dict[str, object]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("odd owner certificate requires positive odd n")
    d = n - 4
    owner = d > 0 and is_prime(d + 2)
    pairs = prime_pair_fiber(n)
    return {
        "integer": n,
        "radius": d,
        "candidate_pair": [2, d + 2],
        "owner_by_primality": owner,
        "owner_by_registered_fiber": pairs == ((2, d + 2),) if owner else pairs == tuple(),
        "owner_equivalence": (pairs == ((2, d + 2),)) == owner,
    }


def registered_local_obstruction_summary(prime_limit: int = REGISTERED_SUPPORT_PRIME_LIMIT) -> dict[str, object]:
    faces = support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES)
    obstruction_counts: Counter[int] = Counter()
    boundary_counts: Counter[int] = Counter()
    support_signatures: dict[str, Counter[str]] = {}
    even_candidate_count = 0
    even_owner_count = 0
    even_local_survivor_count = 0
    even_local_survivor_nonowner_count = 0
    owner_equivalence_ok = True
    odd_point_count = 0
    odd_owner_count = 0

    for face in faces:
        key = support_key(face)
        signature_counter: Counter[str] = Counter()
        for n in integer_fiber(face, REGISTERED_INTEGER_CAP):
            if n % 2:
                odd_point_count += 1
                cert = odd_coordinate_owner_certificate(n)
                odd_owner_count += int(bool(cert["owner_by_primality"]))
                owner_equivalence_ok &= bool(cert["owner_equivalence"])
                continue
            m = n // 2
            start = 1 if m % 2 == 0 else 2
            for d in range(start, m, 2):
                even_candidate_count += 1
                cert = even_coordinate_owner_certificate(n, d, prime_limit)
                owner = bool(cert["owner_by_primality"])
                owner_equivalence_ok &= bool(cert["owner_equivalence"])
                even_owner_count += int(owner)
                signature = cert["local_signature"]
                obstructing = tuple(int(p) for p in signature["obstructing_primes"])
                boundaries = tuple(int(p) for p in signature["boundary_exception_primes"])
                for ell in obstructing:
                    obstruction_counts[ell] += 1
                for ell in boundaries:
                    boundary_counts[ell] += 1
                if signature["locally_survives"]:
                    even_local_survivor_count += 1
                    even_local_survivor_nonowner_count += int(not owner)
                signature_counter[",".join(map(str, obstructing)) if obstructing else "SURVIVES"] += 1
        support_signatures[key] = signature_counter

    compact_support_signatures = {
        key: dict(counter.most_common(8)) for key, counter in sorted(support_signatures.items())
    }
    return {
        "id": "ENGINE-004-PASS-004-LOCAL-OBSTRUCTION-GEOMETRY-SUMMARY-001",
        "classification": "Identity / Proved / Finite-Verified / Diagnostic",
        "scope": {
            "support_prime_limit": REGISTERED_SUPPORT_PRIME_LIMIT,
            "support_face_sizes": list(REGISTERED_SUPPORT_FACE_SIZES),
            "integer_cap": REGISTERED_INTEGER_CAP,
            "local_prime_limit": prime_limit,
            "local_primes": [p for p in primes_up_to(prime_limit) if p % 2 == 1],
        },
        "totals": {
            "even_candidate_count": even_candidate_count,
            "even_owner_count": even_owner_count,
            "even_local_survivor_count": even_local_survivor_count,
            "even_local_survivor_nonowner_count": even_local_survivor_nonowner_count,
            "odd_point_count": odd_point_count,
            "odd_owner_count": odd_owner_count,
        },
        "local_obstruction_counts": {str(k): v for k, v in sorted(obstruction_counts.items())},
        "boundary_exception_counts": {str(k): v for k, v in sorted(boundary_counts.items())},
        "support_conditioned_top_signatures": compact_support_signatures,
        "checks": {
            "owner_equivalence_all_candidates": owner_equivalence_ok,
            "local_survival_not_sufficient": even_local_survivor_nonowner_count > 0,
            "phase_d_not_used": True,
            "no_primality_test_claim": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=REGISTERED_SUPPORT_PRIME_LIMIT)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    summary = registered_local_obstruction_summary(args.prime_limit)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
