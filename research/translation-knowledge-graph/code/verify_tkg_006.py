#!/usr/bin/env python3
"""Finite verifier for TKG-006."""
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("query_tkg_006", HERE / "query_tkg_006.py")
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def close(a: complex | float, b: complex | float, tol: float = 1e-10) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    # Basic character values and zero extension.
    assert M.chi4(1) == 1
    assert M.chi4(3) == -1
    assert M.chi4(15) == -1
    assert M.chi4(6) == 0

    # Complete multiplicativity on a finite grid.
    for m in range(1, 81):
        for n in range(1, 81):
            assert close(M.chi4(m * n), M.chi4(m) * M.chi4(n))

    # Character orthogonality modulo 4.
    chars = M.characters_mod_4()
    units = [1, 3]
    for i, c1 in enumerate(chars):
        for j, c2 in enumerate(chars):
            value = sum(c1(a) * c2(a).conjugate() for a in units)
            assert close(value, 2 if i == j else 0)

    # Residue projectors on units modulo 4.
    for n in range(1, 129, 2):
        for a in [1, 3]:
            expected = 1 if n % 4 == a else 0
            assert close(M.residue_projector_mod4(n, a), expected)

    # Exact decomposition of psi(x;4,a) by principal/nonprincipal twists.
    for x in range(2, 129):
        psi0 = sum(M.von_mangoldt(n) * M.principal(n, 4) for n in range(1, x + 1))
        psi1 = M.psi_twist_chi4(x)
        for a in [1, 3]:
            reconstructed = (psi0 + M.chi4(a).conjugate() * psi1) / 2
            assert close(reconstructed, M.psi_ap(x, 4, a))

    # Explicit reasoning benchmark.
    assert M.chi4(3) * M.chi4(5) == M.chi4(15)
    explanation = M.explain(15)
    assert explanation["asymptotic_inference_authorized"] is False

    print("TKG-006 verifier: PASS on committed finite scope")


if __name__ == "__main__":
    main()
