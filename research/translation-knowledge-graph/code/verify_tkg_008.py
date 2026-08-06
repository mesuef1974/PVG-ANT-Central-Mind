#!/usr/bin/env python3
"""Finite deterministic verifier for TKG-008."""
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("query_tkg_008", HERE / "query_tkg_008.py")
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def main() -> None:
    # Conductor examples.
    assert mod.explain_character("principal4")["conductor"] == 1
    assert mod.explain_character("chi4")["conductor"] == 4
    assert mod.explain_character("chi4mod8")["conductor"] == 4
    assert mod.explain_character("principal4")["extra_bad_primes"] == [2]
    assert mod.explain_character("chi4mod8")["extra_bad_primes"] == []

    # Induced values agree with the primitive source on units modulo q.
    for n in range(1, 257):
        if n % 2 == 1:
            assert mod.induced_chi4_mod8(n) == mod.chi4(n)
        else:
            assert mod.induced_chi4_mod8(n) == 0

    # Principal mod 4 differs from trivial mod 1 exactly on even integers.
    comp = mod.compare("principal4", 128)
    assert comp["differences"]
    assert all(row["n"] % 2 == 0 for row in comp["differences"])

    # Twisted Mangoldt coefficients are masked exactly on newly bad axes.
    for n in range(1, 513):
        primitive = mod.von_mangoldt(n) * mod.chi_trivial_mod1(n)
        induced = mod.coefficient("principal4", n)["twisted_mangoldt"]
        if n % 2 == 0 and mod.von_mangoldt(n) != 0:
            assert induced == 0.0
        elif n % 2 == 1:
            assert abs(induced - primitive) < 1e-12

    # Concrete examples.
    assert mod.coefficient("principal4", 8)["twisted_mangoldt"] == 0.0
    assert mod.coefficient("principal4", 9)["twisted_mangoldt"] > 0.0
    assert mod.coefficient("chi4mod8", 27)["twisted_mangoldt"] < 0.0
    assert mod.coefficient("chi4mod8", 9)["twisted_mangoldt"] > 0.0

    # Governance ceiling remains closed.
    assert mod.coefficient("principal4", 9)["asymptotic_inference_authorized"] is False
    print("TKG-008 finite verifier: PASS")


if __name__ == "__main__":
    main()
