from __future__ import annotations

from math import prod
from typing import Any

PRIME_FACTORIZATION_KIND = "PRIME_FACTORIZATION"


def is_prime(n: int) -> bool:
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def validate_prime_factorization_value(value: Any) -> dict[str, Any]:
    """Validate and return a canonical PRIME_FACTORIZATION execution value.

    Canonical schema:
      {"kind": "PRIME_FACTORIZATION",
       "factors": [{"prime": p, "exponent": e}, ...]}

    The factors list is strictly increasing by prime. This simultaneously
    enforces deterministic order and rejects duplicate prime components.
    The empty list is the canonical factorization of 1.
    """

    if not isinstance(value, dict):
        raise ValueError("prime factorization value must be an object")
    if set(value) != {"kind", "factors"}:
        raise ValueError("prime factorization value must contain exactly kind and factors")
    if value.get("kind") != PRIME_FACTORIZATION_KIND:
        raise ValueError(f"unsupported execution value kind: {value.get('kind')!r}")

    factors = value.get("factors")
    if not isinstance(factors, list):
        raise ValueError("factors must be a list")

    canonical_factors: list[dict[str, int]] = []
    previous_prime = 1
    for index, factor in enumerate(factors):
        if not isinstance(factor, dict):
            raise ValueError(f"factor {index} must be an object")
        if set(factor) != {"prime", "exponent"}:
            raise ValueError(f"factor {index} must contain exactly prime and exponent")

        prime = factor.get("prime")
        exponent = factor.get("exponent")
        if isinstance(prime, bool) or not isinstance(prime, int):
            raise ValueError(f"factor {index} prime must be an integer")
        if not is_prime(prime):
            raise ValueError(f"factor {index} prime is not prime: {prime!r}")
        if prime <= previous_prime:
            raise ValueError("factor primes must be strictly increasing")
        if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 1:
            raise ValueError(f"factor {index} exponent must be a positive integer")

        canonical_factors.append({"prime": prime, "exponent": exponent})
        previous_prime = prime

    return {"kind": PRIME_FACTORIZATION_KIND, "factors": canonical_factors}


def reconstruct_n(value: Any) -> int:
    validated = validate_prime_factorization_value(value)
    return prod(
        factor["prime"] ** factor["exponent"]
        for factor in validated["factors"]
    )
