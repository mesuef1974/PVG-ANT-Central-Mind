from __future__ import annotations

from typing import Any, Callable, TypeAlias, cast

from tkg_composite_value_contract_001 import validate_prime_factorization_value
from tkg_execution_value_contract_001 import (
    ExecutionValue,
    PrimeFactorizationExecutionValue,
    validate_execution_value,
)


FactorizationConsumer: TypeAlias = Callable[
    [PrimeFactorizationExecutionValue],
    ExecutionValue,
]


def validate_factorization_consumer_input(
    value: Any,
) -> PrimeFactorizationExecutionValue:
    """Validate the sole input authorized for a factorization consumer.

    The consumer-facing intermediate is the existing canonical
    PRIME_FACTORIZATION execution value. No integer input is accepted by this
    contract, so a conforming consumer cannot silently refactor an integer.
    """

    return cast(
        PrimeFactorizationExecutionValue,
        validate_prime_factorization_value(value),
    )


def apply_factorization_consumer(
    consumer: FactorizationConsumer,
    factorization: Any,
    /,
) -> ExecutionValue:
    """Apply a typed consumer to a validated factorization intermediate.

    Validation occurs on both sides of the consumer boundary:
    - the input must be a canonical PRIME_FACTORIZATION value;
    - the returned value must satisfy the unified ExecutionValue contract.

    The callable receives exactly one argument: the validated factorization.
    """

    if not callable(consumer):
        raise TypeError("factorization consumer must be callable")
    validated_factorization = validate_factorization_consumer_input(factorization)
    return validate_execution_value(consumer(validated_factorization))
