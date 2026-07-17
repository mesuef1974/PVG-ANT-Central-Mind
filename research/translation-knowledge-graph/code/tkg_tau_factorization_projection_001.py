from __future__ import annotations

from math import prod

from tkg_execution_value_contract_001 import PrimeFactorizationExecutionValue


def project_tau_from_factorization(
    factorization: PrimeFactorizationExecutionValue,
    /,
) -> int:
    """Project the divisor-counting value from a validated factorization.

    This consumer reads only the exponent list supplied by the shared
    PRIME_FACTORIZATION intermediate. It does not read prime labels, reconstruct
    an integer, enumerate divisors, or refactor an integer. Invoke it through
    apply_factorization_consumer so the input and output boundaries remain
    validated and isolated.
    """

    return prod(
        factor["exponent"] + 1
        for factor in factorization["factors"]
    )
