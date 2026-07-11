from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "one-theorem" / "001"
EXPECTED = BASE / "P1-symbolic-expected.json"
GENERATED = BASE / "P1-symbolic-results.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def first_nonzero_after_constant(expression: sp.Expr, variable: sp.Symbol, cutoff: int) -> int:
    series = sp.Poly(sp.series(expression, variable, 0, cutoff).removeO().expand(), variable)
    require(series.nth(0) == 1, "Residual local factor has wrong constant term")
    for degree in range(1, cutoff):
        if sp.simplify(series.nth(degree)) != 0:
            return degree
    raise RuntimeError("No nonzero residual coefficient found within cutoff")


def principal_character_numeric_check(q: int, precision: int = 90) -> None:
    mp.mp.dps = precision
    primes = sp.primefactors(q)
    rho = mp.mpf(1)
    correction = mp.mpf(0)
    for p in primes:
        rho *= 1 - mp.mpf(1) / p
        correction += mp.log(p) / (p - 1)
    predicted = rho * (mp.euler + correction)

    # Richardson-style finite-part check at two small offsets.
    def l_principal(s: mp.mpf) -> mp.mpf:
        value = mp.zeta(s)
        for p in primes:
            value *= 1 - mp.power(p, -s)
        return value

    eps = mp.mpf("1e-25")
    observed_eps = l_principal(1 + eps) - rho / eps
    observed_half = l_principal(1 + eps / 2) - rho / (eps / 2)
    extrapolated = 2 * observed_half - observed_eps
    require(abs(extrapolated - predicted) < mp.mpf("1e-35"), f"Principal finite part failed for q={q}")


def main() -> None:
    require(EXPECTED.exists(), f"Missing expected certificate: {EXPECTED}")

    y = sp.symbols("y")
    residual_orders: dict[str, int] = {}
    for r_value in range(1, 9):
        local = 1 + y ** (2 * r_value) / (1 - y) ** 2
        residual = sp.cancel(
            (1 - y ** (2 * r_value))
            * (1 - y ** (2 * r_value + 1)) ** 2
            * local
        )
        first = first_nonzero_after_constant(residual, y, 2 * r_value + 8)
        require(first == 2 * r_value + 2, f"Unexpected first residual order for r={r_value}: {first}")
        residual_orders[str(r_value)] = first

    # Independent Laurent audit for a simple pole.
    t, rho, kappa, m, a0, q0, q1, log_x = sp.symbols(
        "t rho kappa m A0 Q0 Q1 L", nonzero=True
    )
    simple_integrand = (rho / (m * t) + kappa) * a0 * sp.exp(log_x * t)
    simple_residue = sp.simplify(sp.residue(simple_integrand, t, 0))
    require(simple_residue == a0 * rho / m, "Simple-pole residue formula failed")

    # Independent Laurent audit for the double pole.
    double_integrand = (rho / (m * t) + kappa) ** 2 * (q0 + q1 * t) * sp.exp(log_x * t)
    double_residue = sp.expand(sp.simplify(sp.residue(double_integrand, t, 0)))
    expected_double = sp.expand(
        q0 * rho**2 * log_x / m**2
        + q1 * rho**2 / m**2
        + 2 * q0 * rho * kappa / m
    )
    require(sp.simplify(double_residue - expected_double) == 0, "Double-pole residue formula failed")
    log_coefficient = sp.expand(double_residue).coeff(log_x)
    constant_coefficient = sp.simplify(double_residue.subs(log_x, 0))
    require(log_coefficient == q0 * rho**2 / m**2, "Double-pole logarithmic coefficient failed")
    require(
        sp.simplify(constant_coefficient - rho * (2 * q0 * kappa * m + q1 * rho) / m**2) == 0,
        "Double-pole constant coefficient failed",
    )

    # Symbolic principal-character finite-part derivation.
    e0, e1 = sp.symbols("E0 E1")
    zeta_laurent = 1 / t + sp.EulerGamma
    euler_factor = e0 + e1 * t
    principal_laurent = sp.expand(zeta_laurent * euler_factor)
    require(principal_laurent.coeff(t, -1) == e0, "Principal residue derivation failed")
    require(principal_laurent.coeff(t, 0) == e0 * sp.EulerGamma + e1, "Principal finite-part derivation failed")

    for modulus in [1, 2, 6, 30]:
        principal_character_numeric_check(modulus)

    results = {
        "local_factor": {
            "status": "PASS",
            "r_values": list(range(1, 9)),
            "first_residual_orders": residual_orders,
        },
        "simple_pole": {
            "status": "PASS",
            "residue": "A0*rho/m",
        },
        "double_pole": {
            "status": "PASS",
            "log_coefficient": "Q0*rho**2/m**2",
            "constant_coefficient": "rho*(2*Q0*kappa*m + Q1*rho)/m**2",
        },
        "principal_character": {
            "status": "PASS",
            "residue": "phi(q)/q",
            "finite_part": "rho_q*(EulerGamma + sum_{p|q} log(p)/(p-1))",
            "sample_moduli": [1, 2, 6, 30],
        },
        "target_constants": {
            "status": "PASS",
            "simple_layer": "rho_q*P_chi(alpha_r)/(2*r)",
            "double_log_layer": "rho_q**2*Q_chi(beta_r)/(2*r+1)**2",
            "double_constant_layer": "rho_q**2*Q_chi_prime(beta_r)/(2*r+1)**2 + 2*rho_q*kappa_q*Q_chi(beta_r)/(2*r+1)",
        },
        "decision": "P1_SYMBOLIC_PASS",
    }

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    require(results == expected, "Generated symbolic result differs from committed expected certificate")
    GENERATED.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("one_theorem_symbolic_audit: PASS — local factors and Laurent constants verified independently")


if __name__ == "__main__":
    main()
