from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

try:
    from tools.pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        integer_fiber,
        normalize_support,
        support_key,
        support_universe,
    )
    from tools.pvg_local_additive_cell_atlas import is_prime, primes_up_to
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        integer_fiber,
        normalize_support,
        support_key,
        support_universe,
    )
    from pvg_local_additive_cell_atlas import is_prime, primes_up_to

Support = tuple[int, ...]
PrimePair = tuple[int, int]


def prime_pair_fiber(n: int) -> tuple[PrimePair, ...]:
    if n < 4:
        return tuple()
    primes = tuple(primes_up_to(n))
    prime_set = set(primes)
    out: list[PrimePair] = []
    for left in primes:
        right = n - left
        if left >= right:
            break
        if right in prime_set:
            out.append((left, right))
    return tuple(out)


def independent_prime_pair_fiber(n: int) -> tuple[PrimePair, ...]:
    out: list[PrimePair] = []
    for left in range(2, n):
        right = n - left
        if left >= right:
            break
        if is_prime(left) and is_prime(right):
            out.append((left, right))
    return tuple(out)


def representation_count(n: int) -> int:
    return len(prime_pair_fiber(n))


def parity_route(n: int) -> str:
    return "two_plus_odd" if n % 2 else "odd_plus_odd"


def prime_fiber_record(n: int, support: Support) -> dict[str, object]:
    support = normalize_support(support)
    pairs = prime_pair_fiber(n)
    return {
        "integer": n,
        "support": list(support),
        "support_key": support_key(support),
        "parity_route": parity_route(n),
        "representation_count": len(pairs),
        "representable": bool(pairs),
        "prime_pairs": [list(pair) for pair in pairs],
    }


def support_prime_fiber_summary(support: Support, cap: int) -> dict[str, object]:
    support = normalize_support(support)
    values = integer_fiber(support, cap)
    records = [prime_fiber_record(value, support) for value in values]
    representable = [record for record in records if record["representable"]]
    maximum = max(records, key=lambda record: (int(record["representation_count"]), int(record["integer"])), default=None)
    return {
        "support": list(support),
        "support_key": support_key(support),
        "integer_cap": cap,
        "integer_count": len(values),
        "representable_integer_count": len(representable),
        "nonrepresentable_integer_count": len(values) - len(representable),
        "total_representation_count": sum(int(record["representation_count"]) for record in records),
        "maximum_representation_integer": None if maximum is None else maximum["integer"],
        "maximum_representation_count": 0 if maximum is None else maximum["representation_count"],
        "records": records,
    }


def registered_summary() -> dict[str, object]:
    faces = support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES)
    records = [support_prime_fiber_summary(face, REGISTERED_INTEGER_CAP) for face in faces]
    all_integer_records = [record for support_record in records for record in support_record["records"]]
    independent_matches = [
        tuple(tuple(pair) for pair in record["prime_pairs"]) == independent_prime_pair_fiber(int(record["integer"]))
        for record in all_integer_records
    ]
    odd_multiplicity_ok = all(
        int(record["representation_count"]) <= 1
        for record in all_integer_records
        if int(record["integer"]) % 2 == 1
    )
    parity_routing_ok = all(
        all((pair[0] == 2) for pair in record["prime_pairs"])
        if int(record["integer"]) % 2 == 1
        else all((pair[0] % 2 == 1 and pair[1] % 2 == 1) for pair in record["prime_pairs"])
        for record in all_integer_records
    )
    global_max = max(
        all_integer_records,
        key=lambda record: (int(record["representation_count"]), int(record["integer"])),
    )
    return {
        "id": "ENGINE-004-INVERSE-PRIME-FIBERS-SUMMARY-001",
        "classification": "Identity / Finite-Verified / Diagnostic",
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
            "separation": "support class, integer point, and representation multiplicity are distinct data layers",
        },
        "totals": {
            "integer_point_count": len(all_integer_records),
            "representable_integer_count": sum(bool(record["representable"]) for record in all_integer_records),
            "nonrepresentable_integer_count": sum(not bool(record["representable"]) for record in all_integer_records),
            "total_representation_count": sum(int(record["representation_count"]) for record in all_integer_records),
            "independent_scan_match_count": sum(independent_matches),
            "independent_scan_mismatch_count": len(independent_matches) - sum(independent_matches),
        },
        "global_maximum": {
            "integer": global_max["integer"],
            "support": global_max["support"],
            "representation_count": global_max["representation_count"],
        },
        "records": records,
        "verification": {
            "all_prime_fibers_match_independent_scan": all(independent_matches),
            "odd_multiplicity_at_most_one": odd_multiplicity_ok,
            "parity_routing_holds": parity_routing_ok,
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
        support = normalize_support(int(part.strip()) for part in args.support.split(",") if part.strip())
        data = prime_fiber_record(args.integer, support)

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, ensure_ascii=False, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
