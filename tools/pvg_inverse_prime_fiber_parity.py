from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from tools.pvg_inverse_integer_fibers import integer_fiber, normalize_support, support_key
    from tools.pvg_inverse_prime_fibers import parity_route, prime_pair_fiber
    from tools.pvg_local_additive_cell_atlas import is_prime
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import integer_fiber, normalize_support, support_key
    from pvg_inverse_prime_fibers import parity_route, prime_pair_fiber
    from pvg_local_additive_cell_atlas import is_prime

Support = tuple[int, ...]


def support_parity(support: Support) -> str:
    """Return the parity shared by every integer with exactly this prime support."""
    support = normalize_support(support)
    return "even" if 2 in support else "odd"


def support_parity_route(support: Support) -> str:
    """Return the prime-pair parity route forced by the exact support."""
    return "odd_plus_odd" if support_parity(support) == "even" else "two_plus_odd"


def odd_prime_fiber_formula(n: int) -> tuple[tuple[int, int], ...]:
    """Exact distinct-prime fiber formula for odd integers."""
    if n % 2 == 0 or n <= 4:
        return tuple()
    right = n - 2
    return ((2, right),) if right > 2 and is_prime(right) else tuple()


def support_parity_certificate(support: Support, cap: int) -> dict[str, object]:
    support = normalize_support(support)
    values = integer_fiber(support, cap)
    expected_parity = support_parity(support)
    expected_route = support_parity_route(support)

    parity_matches = [
        (value % 2 == 0) == (expected_parity == "even")
        for value in values
    ]
    route_matches = [parity_route(value) == expected_route for value in values]
    odd_formula_matches = [
        prime_pair_fiber(value) == odd_prime_fiber_formula(value)
        for value in values
        if value % 2 == 1
    ]

    return {
        "id": "ENGINE-004-SUPPORT-PARITY-CERTIFICATE-001",
        "support": list(support),
        "support_key": support_key(support),
        "integer_cap": cap,
        "integer_count": len(values),
        "support_parity": expected_parity,
        "forced_prime_pair_route": expected_route,
        "exact_laws": {
            "support_parity": "N is even iff 2 belongs to supp(N)",
            "odd_fiber": "for odd N, R_2(N) is {(2,N-2)} iff N-2 is prime, otherwise empty",
            "odd_multiplicity": "for odd N, r_2(N) is the primality indicator of N-2",
        },
        "verification": {
            "all_integer_parities_match_support": all(parity_matches),
            "all_prime_pair_routes_match_support": all(route_matches),
            "all_odd_fibers_match_exact_formula": all(odd_formula_matches),
        },
        "classification": "Identity / Proved / Finite-Verified",
        "claim_ceiling": {
            "goldbach_progress": False,
            "pnt_progress": False,
            "rh_progress": False,
            "grh_progress": False,
            "phase_d_authorized": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Certify support-parity stratification inside ENGINE-004.")
    parser.add_argument("--support", required=True)
    parser.add_argument("--cap", type=int, default=100_000)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    support = normalize_support(int(part.strip()) for part in args.support.split(",") if part.strip())
    data = support_parity_certificate(support, args.cap)
    rendered = json.dumps(
        data,
        ensure_ascii=False,
        indent=None if args.compact else 2,
        separators=(",", ":") if args.compact else None,
    )
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
