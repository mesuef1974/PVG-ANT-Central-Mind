from __future__ import annotations

from tkg_execution_value_contract_001 import (
    ExecutionValue,
    PrimeFactorizationExecutionValue,
)


def project_lambda_from_factorization(
    factorization: PrimeFactorizationExecutionValue,
    /,
) -> ExecutionValue:
    """Project the symbolic von Mangoldt value from a factorization.

    The projection reads the support cardinality and, only for one-axis
    support, the prime label. It is independent of the exponent magnitude:
    every positive power of the same prime maps to the same LOG_PRIME value.
    Invoke it through apply_factorization_consumer so the input and output
    boundaries remain validated and isolated.
    """

    factors = factorization["factors"]
    if len(factors) != 1:
        return {"kind": "ZERO"}
    return {"kind": "LOG_PRIME", "prime": factors[0]["prime"]}
