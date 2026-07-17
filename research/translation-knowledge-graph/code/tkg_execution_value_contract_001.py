from __future__ import annotations

from typing import Any, Literal, TypeAlias, TypedDict, cast

from tkg_composite_value_contract_001 import (
    PRIME_FACTORIZATION_KIND,
    is_prime,
    validate_prime_factorization_value,
)

ZERO_KIND = "ZERO"
LOG_PRIME_KIND = "LOG_PRIME"


class ZeroExecutionValue(TypedDict):
    kind: Literal["ZERO"]


class LogPrimeExecutionValue(TypedDict):
    kind: Literal["LOG_PRIME"]
    prime: int


class PrimeFactorComponent(TypedDict):
    prime: int
    exponent: int


class PrimeFactorizationExecutionValue(TypedDict):
    kind: Literal["PRIME_FACTORIZATION"]
    factors: list[PrimeFactorComponent]


ExecutionValue: TypeAlias = (
    int
    | ZeroExecutionValue
    | LogPrimeExecutionValue
    | PrimeFactorizationExecutionValue
)


def validate_execution_value(value: Any) -> ExecutionValue:
    """Validate and return a canonical execution result value.

    Supported result families:
    - integer scalars used by tau and mu;
    - {"kind": "ZERO"};
    - {"kind": "LOG_PRIME", "prime": p};
    - canonical PRIME_FACTORIZATION values.

    Booleans are rejected even though bool is a subclass of int.
    """

    if isinstance(value, bool):
        raise ValueError("boolean is not an integer execution value")
    if isinstance(value, int):
        return value
    if not isinstance(value, dict):
        raise ValueError("execution value must be an integer or a structured object")

    kind = value.get("kind")
    if kind == ZERO_KIND:
        if set(value) != {"kind"}:
            raise ValueError("ZERO value must contain exactly kind")
        return {"kind": ZERO_KIND}

    if kind == LOG_PRIME_KIND:
        if set(value) != {"kind", "prime"}:
            raise ValueError("LOG_PRIME value must contain exactly kind and prime")
        prime = value.get("prime")
        if isinstance(prime, bool) or not isinstance(prime, int):
            raise ValueError("LOG_PRIME prime must be an integer")
        if not is_prime(prime):
            raise ValueError(f"LOG_PRIME prime is not prime: {prime!r}")
        return {"kind": LOG_PRIME_KIND, "prime": prime}

    if kind == PRIME_FACTORIZATION_KIND:
        return cast(PrimeFactorizationExecutionValue, validate_prime_factorization_value(value))

    raise ValueError(f"unsupported execution value kind: {kind!r}")
