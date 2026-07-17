from __future__ import annotations

from tkg_execution_value_contract_001 import PrimeFactorizationExecutionValue


def project_mu_from_factorization(
    factorization: PrimeFactorizationExecutionValue,
    /,
) -> int:
    """Project the Mobius value from a validated prime factorization.

    This consumer reads only the exponent list supplied by the shared
    PRIME_FACTORIZATION intermediate. It does not reconstruct or refactor an
    integer. Invoke it through apply_factorization_consumer so the input and
    output boundaries remain validated and isolated.
    """

    factors = factorization["factors"]
    if any(factor["exponent"] > 1 for factor in factors):
        return 0
    return -1 if len(factors) % 2 else 1
