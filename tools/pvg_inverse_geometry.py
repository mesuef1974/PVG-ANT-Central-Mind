#!/usr/bin/env python3
"""Exact inverse geometry for Prime Valuation Geometry (PVG).

Automatic factorization is certified for 1 <= n < 2^64 by deterministic
Miller-Rabin plus Pollard-Rho splitting. Larger integers require a complete
factorization supplied with --factors; every supplied prime must itself be
below 2^64 so primality can be certified deterministically.

This tool performs exact encoding and classification only. It makes no
claim about fast worst-case integer factorization.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, prod
from typing import Dict, Iterable, Mapping

UINT64_LIMIT = 1 << 64
_DETERMINISTIC_MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


class GeometryInputError(ValueError):
    """Raised when an exact PVG location cannot be certified."""


def is_prime_64(n: int) -> bool:
    """Deterministically test primality for 0 <= n < 2^64."""
    if n < 2:
        return False
    if n >= UINT64_LIMIT:
        raise GeometryInputError("deterministic primality is limited to factors below 2^64")
    for p in _SMALL_PRIMES:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    for base in _DETERMINISTIC_MR_BASES:
        if base % n == 0:
            continue
        x = pow(base, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def _pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    for c in range(1, 128):
        x = 2
        y = 2
        divisor = 1
        for _ in range(250_000):
            if divisor != 1:
                break
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            divisor = gcd(abs(x - y), n)
        if 1 < divisor < n:
            return divisor
    raise GeometryInputError(f"Pollard-Rho failed to split {n}")


def factorint_64(n: int) -> Dict[int, int]:
    """Return the certified prime factorization of 1 <= n < 2^64."""
    if not 1 <= n < UINT64_LIMIT:
        raise GeometryInputError("automatic exact factorization requires 1 <= n < 2^64")

    factors: list[int] = []

    def split(m: int) -> None:
        if m == 1:
            return
        if is_prime_64(m):
            factors.append(m)
            return
        divisor = _pollard_rho(m)
        split(divisor)
        split(m // divisor)

    split(n)
    answer: Dict[int, int] = {}
    for p in sorted(factors):
        answer[p] = answer.get(p, 0) + 1
    return answer


def parse_factorization(text: str) -> Dict[int, int]:
    """Parse p, p^a entries separated by commas."""
    if not text.strip():
        raise GeometryInputError("the supplied factorization is empty")

    factors: Dict[int, int] = {}
    for raw_term in text.split(","):
        term = raw_term.strip()
        if not term:
            raise GeometryInputError("empty term in factorization")
        if "^" in term:
            prime_text, exponent_text = term.split("^", 1)
        else:
            prime_text, exponent_text = term, "1"
        try:
            prime = int(prime_text)
            exponent = int(exponent_text)
        except ValueError as exc:
            raise GeometryInputError(f"invalid factorization term: {term}") from exc
        if prime < 2 or prime >= UINT64_LIMIT:
            raise GeometryInputError(
                f"each supplied prime must satisfy 2 <= p < 2^64; got {prime}"
            )
        if exponent < 1:
            raise GeometryInputError(f"exponent must be positive; got {term}")
        if not is_prime_64(prime):
            raise GeometryInputError(f"supplied base is not prime: {prime}")
        factors[prime] = factors.get(prime, 0) + exponent
    return dict(sorted(factors.items()))


def validate_complete_factorization(n: int, factors: Mapping[int, int]) -> None:
    reconstructed = prod(p**a for p, a in factors.items())
    if reconstructed != n:
        raise GeometryInputError(
            f"factorization product {reconstructed} does not equal input n={n}"
        )


def _classification(omega: int, exponents: Iterable[int]) -> str:
    exponents = tuple(exponents)
    if omega == 0:
        return "origin"
    if omega == 1:
        return "prime_axis_generator" if exponents[0] == 1 else "prime_axis_point"
    if omega == 2:
        return "relative_interior_of_two_prime_face"
    if omega == 3:
        return "relative_interior_of_three_prime_face"
    return f"relative_interior_of_{omega}_prime_face"


def pvg_passport(n: int, factors: Mapping[int, int], *, source: str) -> dict:
    """Build the exact geometric passport from a complete factorization."""
    if n < 1:
        raise GeometryInputError("PVG positive-integer mode requires n >= 1")
    validate_complete_factorization(n, factors)

    support = list(sorted(factors))
    exponents = [factors[p] for p in support]
    omega = len(support)
    Omega = sum(exponents)

    if n == 1:
        return {
            "schema": "PVG-INVERSE-GEOMETRY-PASSPORT-001",
            "input": 1,
            "factorization_status": source,
            "factorization": [],
            "valuation_vector": {},
            "point_class": "origin",
            "support": [],
            "omega": 0,
            "Omega": 0,
            "radical": 1,
            "repeat_depth": 0,
            "shape_partition": [],
            "minimal_face": {
                "kind": "origin",
                "support": [],
                "face_dimension": 0,
                "horizontal_section_dimension": 0,
            },
            "primitive_ray": None,
            "divisibility_geometry": {
                "divisor_box_side_lengths": [],
                "divisor_count": 1,
                "multiple_cone_anchor": {},
            },
            "scientific_classification": "exact identity and exact labeled encoding",
        }

    radical = prod(support)
    repeat_depth = Omega - omega
    divisor_count = prod(a + 1 for a in exponents)
    ray_index = 0
    for a in exponents:
        ray_index = gcd(ray_index, a)
    primitive_exponents = {str(p): factors[p] // ray_index for p in support}
    primitive_generator = prod(p ** (factors[p] // ray_index) for p in support)
    balanced = len(set(exponents)) == 1
    shape_partition = sorted(exponents, reverse=True)
    barycentric = {str(p): f"{factors[p]}/{Omega}" for p in support}

    return {
        "schema": "PVG-INVERSE-GEOMETRY-PASSPORT-001",
        "input": n,
        "factorization_status": source,
        "factorization": [
            {"prime": p, "valuation": factors[p]} for p in support
        ],
        "valuation_vector": {str(p): factors[p] for p in support},
        "point_class": _classification(omega, exponents),
        "support": support,
        "omega": omega,
        "Omega": Omega,
        "radical": radical,
        "repeat_depth": repeat_depth,
        "shape_partition": shape_partition,
        "minimal_face": {
            "kind": "prime_axis" if omega == 1 else "prime_support_face",
            "support": support,
            "face_dimension": omega,
            "relative_position": "relative_interior",
            "horizontal_simplex_level": Omega,
            "horizontal_section_dimension": max(omega - 1, 0),
            "barycentric_coordinates": barycentric,
        },
        "squarefree_floor": {
            "radical": radical,
            "valuation_vector": {str(p): 1 for p in support},
            "vertical_repeat_depth": repeat_depth,
        },
        "primitive_ray": {
            "ray_index": ray_index,
            "primitive_direction": primitive_exponents,
            "primitive_generator": primitive_generator,
            "power_identity": f"{n} = {primitive_generator}^{ray_index}",
            "balanced_support_diagonal": balanced,
        },
        "divisibility_geometry": {
            "divisor_box_side_lengths": [a + 1 for a in exponents],
            "divisor_count": divisor_count,
            "multiple_cone_anchor": {str(p): factors[p] for p in support},
        },
        "directional_geometry": {
            "origin_ray_sequence": f"{primitive_generator}^k",
            "prime_axis_families_through_point": [
                {
                    "prime": p,
                    "sequence": f"{n}*{p}^k",
                    "direction_vector": {str(p): 1},
                }
                for p in support
            ],
            "law": "nu(n*Q^k)=nu(n)+k*nu(Q)",
        },
        "scientific_classification": "exact identity and exact labeled encoding",
    }


def inverse_geometry(n: int, supplied_factorization: str | None = None) -> dict:
    if n < 1:
        raise GeometryInputError("PVG positive-integer mode requires n >= 1")
    if supplied_factorization is not None:
        factors = parse_factorization(supplied_factorization)
        validate_complete_factorization(n, factors)
        return pvg_passport(
            n,
            factors,
            source="complete_user_supplied_factorization_verified_with_64bit_prime_certificates",
        )
    if n >= UINT64_LIMIT:
        raise GeometryInputError(
            "n >= 2^64: exact automatic location is intentionally refused. "
            "Supply a complete certified factorization with --factors."
        )
    factors = factorint_64(n)
    return pvg_passport(n, factors, source="automatic_certified_factorization_below_2^64")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Locate a positive integer exactly in Prime Valuation Geometry."
    )
    parser.add_argument("n", type=int, help="positive integer")
    parser.add_argument(
        "--factors",
        help="complete factorization such as '2^3,3^2,5'; required for n >= 2^64",
    )
    parser.add_argument(
        "--compact", action="store_true", help="emit compact JSON rather than indented JSON"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        passport = inverse_geometry(args.n, args.factors)
    except GeometryInputError as exc:
        error = {
            "schema": "PVG-INVERSE-GEOMETRY-ERROR-001",
            "input": args.n,
            "status": "exact_location_not_certified",
            "reason": str(exc),
            "principle": "exact PVG point location requires a complete certified prime factorization",
        }
        print(json.dumps(error, ensure_ascii=False, indent=None if args.compact else 2))
        return 2

    print(
        json.dumps(
            passport,
            ensure_ascii=False,
            sort_keys=True,
            indent=None if args.compact else 2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
