from __future__ import annotations

import argparse
import json
from functools import lru_cache
from math import gcd
from pathlib import Path

try:
    from tools.pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        factor_support,
        integer_fiber,
        normalize_support,
        support_key,
        support_universe,
    )
    from tools.pvg_local_additive_cell_atlas import is_prime
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        factor_support,
        integer_fiber,
        normalize_support,
        support_key,
        support_universe,
    )
    from pvg_local_additive_cell_atlas import is_prime

Support = tuple[int, ...]
PrimePair = tuple[int, int]


@lru_cache(maxsize=None)
def _trial_is_prime(n: int) -> bool:
    return is_prime(n)


_sieve_limit = 1
_sieve_flags = bytearray(b"\x00\x00")


def _ensure_independent_sieve(limit: int) -> bytearray:
    global _sieve_limit, _sieve_flags
    if limit <= _sieve_limit:
        return _sieve_flags
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    divisor = 2
    while divisor * divisor <= limit:
        if flags[divisor]:
            start = divisor * divisor
            flags[start : limit + 1 : divisor] = b"\x00" * (((limit - start) // divisor) + 1)
        divisor += 1
    _sieve_limit = limit
    _sieve_flags = flags
    return flags


def prime_pair_fiber(n: int) -> tuple[PrimePair, ...]:
    if n < 4:
        return tuple()
    if n % 2:
        right = n - 2
        return ((2, right),) if right > 2 and _trial_is_prime(right) else tuple()
    out: list[PrimePair] = []
    for left in range(3, n // 2 + 1, 2):
        right = n - left
        if left >= right:
            break
        if _trial_is_prime(left) and _trial_is_prime(right):
            out.append((left, right))
    return tuple(out)


def independent_prime_pair_fiber(n: int) -> tuple[PrimePair, ...]:
    if n < 4:
        return tuple()
    flags = _ensure_independent_sieve(n)
    out: list[PrimePair] = []
    for left in range(2, n):
        right = n - left
        if left >= right:
            break
        if flags[left] and flags[right]:
            out.append((left, right))
    return tuple(out)


def representation_count(n: int) -> int:
    return len(prime_pair_fiber(n))


def parity_route(n: int) -> str:
    return "two_plus_odd" if n % 2 else "odd_plus_odd"


def prime_gap_fiber(n: int) -> tuple[int, ...]:
    """Return the exact doubled-centered coordinates Delta=q-p."""
    return tuple(right - left for left, right in prime_pair_fiber(n))


def prime_pair_from_gap(n: int, gap: int) -> PrimePair:
    """Reconstruct a distinct prime pair from N and Delta=q-p."""
    if n < 4 or gap <= 0 or gap >= n or (n - gap) % 2:
        raise ValueError("invalid centered gap coordinate")
    left = (n - gap) // 2
    right = (n + gap) // 2
    if not (left < right and is_prime(left) and is_prime(right)):
        raise ValueError("gap does not reconstruct a distinct prime pair")
    return left, right


def centered_gap_record(n: int, pair: PrimePair) -> dict[str, object]:
    left, right = pair
    if left + right != n or not (left < right and is_prime(left) and is_prime(right)):
        raise ValueError("pair is not a distinct-prime representation of n")
    gap = right - left
    return {
        "gap": gap,
        "left": left,
        "right": right,
        "reconstructed_pair": list(prime_pair_from_gap(n, gap)),
        "parity_matches_sum": gap % 2 == n % 2,
        "square_difference": n * n - gap * gap,
        "four_prime_product": 4 * left * right,
        "square_difference_identity": n * n - gap * gap == 4 * left * right,
        "gcd_n_gap": gcd(n, gap),
        "expected_gcd": gcd(n, 2),
        "gcd_law_holds": gcd(n, gap) == gcd(n, 2),
        "even_radius_coprime": True if n % 2 else gcd(n // 2, gap // 2) == 1,
    }


def support_route_class(support: Support) -> str:
    support = normalize_support(support)
    return "contains_axis_2_even_route" if 2 in support else "excludes_axis_2_odd_route"


def prime_fiber_record(n: int, support: Support) -> dict[str, object]:
    support = normalize_support(support)
    if n < 1 or factor_support(n) != support:
        raise ValueError("integer does not belong to the requested exact-support fiber")
    pairs = prime_pair_fiber(n)
    gaps = [centered_gap_record(n, pair) for pair in pairs]
    return {
        "integer": n,
        "support": list(support),
        "support_key": support_key(support),
        "support_route_class": support_route_class(support),
        "parity_route": parity_route(n),
        "representation_count": len(pairs),
        "representable": bool(pairs),
        "prime_pairs": [list(pair) for pair in pairs],
        "centered_gap_coordinates": gaps,
    }


def support_prime_fiber_summary(support: Support, cap: int) -> dict[str, object]:
    support = normalize_support(support)
    values = integer_fiber(support, cap)
    records = [prime_fiber_record(value, support) for value in values]
    maximum = max(
        records,
        key=lambda record: (int(record["representation_count"]), int(record["integer"])),
        default=None,
    )

    def compact_example(record: dict[str, object]) -> dict[str, object]:
        pairs = list(record["prime_pairs"])
        gaps = list(record["centered_gap_coordinates"])
        return {
            "integer": record["integer"],
            "representation_count": record["representation_count"],
            "representable": record["representable"],
            "first_prime_pairs": pairs[:5],
            "first_centered_gaps": [item["gap"] for item in gaps[:5]],
        }

    representable_examples = [
        compact_example(record) for record in records if record["representable"]
    ][:5]
    nonrepresentable_examples = [
        compact_example(record) for record in records if not record["representable"]
    ][:5]
    gap_values = [
        int(gap_record["gap"])
        for record in records
        for gap_record in record["centered_gap_coordinates"]
    ]
    return {
        "support": list(support),
        "support_key": support_key(support),
        "integer_cap": cap,
        "integer_count": len(values),
        "representable_integer_count": sum(bool(record["representable"]) for record in records),
        "nonrepresentable_integer_count": sum(not bool(record["representable"]) for record in records),
        "total_representation_count": sum(int(record["representation_count"]) for record in records),
        "centered_gap_coordinate_count": len(gap_values),
        "minimum_centered_gap": min(gap_values, default=None),
        "maximum_centered_gap": max(gap_values, default=None),
        "maximum_representation_integer": None if maximum is None else maximum["integer"],
        "maximum_representation_count": 0 if maximum is None else maximum["representation_count"],
        "representable_examples": representable_examples,
        "nonrepresentable_examples": nonrepresentable_examples,
    }


def registered_summary() -> dict[str, object]:
    faces = support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES)
    compact_records = [support_prime_fiber_summary(face, REGISTERED_INTEGER_CAP) for face in faces]

    all_records: list[dict[str, object]] = []
    independent_matches: list[bool] = []
    gap_bijection_checks: list[bool] = []
    gap_identity_checks: list[bool] = []
    gap_gcd_checks: list[bool] = []
    even_radius_checks: list[bool] = []
    for face in faces:
        for value in integer_fiber(face, REGISTERED_INTEGER_CAP):
            record = prime_fiber_record(value, face)
            all_records.append(record)
            pairs = tuple(tuple(pair) for pair in record["prime_pairs"])
            independent_matches.append(pairs == independent_prime_pair_fiber(value))
            gaps = tuple(int(item["gap"]) for item in record["centered_gap_coordinates"])
            gap_bijection_checks.append(
                gaps == prime_gap_fiber(value)
                and tuple(prime_pair_from_gap(value, gap) for gap in gaps) == pairs
            )
            for item in record["centered_gap_coordinates"]:
                gap_identity_checks.append(
                    bool(item["parity_matches_sum"])
                    and bool(item["square_difference_identity"])
                )
                gap_gcd_checks.append(bool(item["gcd_law_holds"]))
                even_radius_checks.append(bool(item["even_radius_coprime"]))

    odd_multiplicity_ok = all(
        int(record["representation_count"]) <= 1
        for record in all_records
        if int(record["integer"]) % 2 == 1
    )
    parity_routing_ok = all(
        all(pair[0] == 2 for pair in record["prime_pairs"])
        if int(record["integer"]) % 2 == 1
        else all(pair[0] % 2 == 1 and pair[1] % 2 == 1 for pair in record["prime_pairs"])
        for record in all_records
    )
    route_totals: dict[str, dict[str, object]] = {}
    for label, contains_axis_2 in (("contains_axis_2", True), ("excludes_axis_2", False)):
        route_faces = [face for face in faces if (2 in face) is contains_axis_2]
        route_records = [
            record
            for record in all_records
            if (2 in tuple(record["support"])) is contains_axis_2
        ]
        route_totals[label] = {
            "support_face_count": len(route_faces),
            "integer_point_count": len(route_records),
            "representable_integer_count": sum(
                bool(record["representable"]) for record in route_records
            ),
            "nonrepresentable_integer_count": sum(
                not bool(record["representable"]) for record in route_records
            ),
            "total_representation_count": sum(
                int(record["representation_count"]) for record in route_records
            ),
        }

    support_controls_parity = all(
        ((2 in tuple(record["support"])) == (int(record["integer"]) % 2 == 0))
        for record in all_records
    )
    odd_support_reduction = all(
        tuple(tuple(pair) for pair in record["prime_pairs"])
        == (
            ((2, int(record["integer"]) - 2),)
            if is_prime(int(record["integer"]) - 2)
            else tuple()
        )
        for record in all_records
        if 2 not in tuple(record["support"])
    )
    frozen_even_nonrepresentable = sorted(
        int(record["integer"])
        for record in all_records
        if 2 in tuple(record["support"]) and not bool(record["representable"])
    )
    global_max = max(
        all_records,
        key=lambda record: (int(record["representation_count"]), int(record["integer"])),
    )

    return {
        "id": "ENGINE-004-INVERSE-PRIME-FIBERS-SUMMARY-001",
        "classification": "Identity / Proved / Finite-Verified / Diagnostic",
        "scope": {
            "support_prime_limit": REGISTERED_SUPPORT_PRIME_LIMIT,
            "support_face_sizes": list(REGISTERED_SUPPORT_FACE_SIZES),
            "integer_cap": REGISTERED_INTEGER_CAP,
            "support_face_count": len(faces),
        },
        "exact_laws": {
            "prime_fiber": "R_2(N)={{p,q}:p<q primes and p+q=N}",
            "odd_route": "odd N has at most one representation, necessarily 2+(N-2)",
            "even_route": "even N distinct-prime representations use two odd primes",
            "support_controls_route": "N in N(F) is even iff 2 is in F; F without 2 has R_2(N) empty or {{2,N-2}}",
            "centered_gap_coordinate": "Delta_2(N)={q-p:{p,q} in R_2(N)}",
            "centered_gap_reconstruction": "p=(N-Delta)/2 and q=(N+Delta)/2",
            "centered_square_difference": "N^2-Delta^2=4pq",
            "centered_gap_gcd": "gcd(N,Delta)=gcd(N,2)",
            "even_radius_coprimality": "for even N, gcd(N/2,Delta/2)=1",
            "separation": "support class, integer point, representation multiplicity, and centered-gap coordinates are distinct data layers",
        },
        "totals": {
            "integer_point_count": len(all_records),
            "representable_integer_count": sum(bool(record["representable"]) for record in all_records),
            "nonrepresentable_integer_count": sum(not bool(record["representable"]) for record in all_records),
            "total_representation_count": sum(int(record["representation_count"]) for record in all_records),
            "centered_gap_coordinate_count": sum(
                len(record["centered_gap_coordinates"]) for record in all_records
            ),
            "independent_scan_match_count": sum(independent_matches),
            "independent_scan_mismatch_count": len(independent_matches) - sum(independent_matches),
        },
        "support_route_totals": route_totals,
        "frozen_box_exceptions": {
            "contains_axis_2_nonrepresentable_integers": frozen_even_nonrepresentable,
        },
        "global_maximum": {
            "integer": global_max["integer"],
            "support": global_max["support"],
            "representation_count": global_max["representation_count"],
        },
        "records": compact_records,
        "verification": {
            "all_prime_fibers_match_independent_scan": all(independent_matches),
            "odd_multiplicity_at_most_one": odd_multiplicity_ok,
            "parity_routing_holds": parity_routing_ok,
            "support_controls_parity_route": support_controls_parity,
            "odd_support_fiber_reduces_to_n_minus_2_primality": odd_support_reduction,
            "frozen_axis_2_nonrepresentable_points_are_2_4_6": frozen_even_nonrepresentable == [2, 4, 6],
            "centered_gap_bijection_holds": all(gap_bijection_checks),
            "centered_square_difference_holds": all(gap_identity_checks),
            "centered_gap_gcd_law_holds": all(gap_gcd_checks),
            "even_radius_coprimality_holds": all(even_radius_checks),
            "deterministic_ordering": True,
        },
        "claim_ceiling": {
            "historical_originality": False,
            "phase_d_authorized": False,
            "goldbach_progress": False,
            "pnt_progress": False,
            "rh_progress": False,
            "grh_progress": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate and certify PVG inverse prime fibers.")
    parser.add_argument("integer", nargs="?", type=int)
    parser.add_argument("--support")
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    if args.registered_summary:
        data = registered_summary()
    else:
        if args.integer is None or args.support is None:
            parser.error("integer and --support are required unless --registered-summary is used")
        support = normalize_support(
            int(part.strip()) for part in args.support.split(",") if part.strip()
        )
        data = prime_fiber_record(args.integer, support)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(
        json.dumps(
            data,
            ensure_ascii=False,
            separators=(",", ":") if args.compact else None,
            indent=None if args.compact else 2,
        )
    )


if __name__ == "__main__":
    main()
