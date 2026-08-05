from __future__ import annotations

import argparse
import json
from collections import Counter
from math import prod


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factorint(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("factorint expects a positive integer")
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def omega(factors: dict[int, int]) -> int:
    return len(factors)


def Omega(factors: dict[int, int]) -> int:
    return sum(factors.values())


def primes_up_to(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime(n)]


def encoded_factors(factors: dict[int, int]) -> list[dict[str, int]]:
    return [{"prime": p, "exponent": e} for p, e in sorted(factors.items())]


def analyze_pair(p: int, q: int) -> dict[str, object]:
    if not (is_prime(p) and is_prime(q) and p < q):
        raise ValueError("expected distinct primes p < q")
    s, d = p + q, q - p
    sf, df = factorint(s), factorint(d)
    sum_prime, difference_prime = is_prime(s), is_prime(d)
    return {
        "p": p,
        "q": q,
        "sum": s,
        "difference": d,
        "sum_factors": encoded_factors(sf),
        "difference_factors": encoded_factors(df),
        "sum_omega": omega(sf),
        "sum_Omega": Omega(sf),
        "difference_omega": omega(df),
        "difference_Omega": Omega(df),
        "sum_is_prime": sum_prime,
        "difference_is_prime": difference_prime,
        "pascal_cell_closed": sum_prime,
        "sum_level_preserved": Omega(sf) == 1,
        "difference_level_preserved": Omega(df) == 1,
        "sum_destination_axes": sorted(sf),
        "difference_destination_axes": sorted(df),
        "sum_identity": f"{p}g + {q}g = {s}g",
        "difference_identity": f"{q}g - {p}g = {d}g",
        "classification": (
            "closed_prime_axis_pascal_cell"
            if sum_prime
            else "composite_destination_additive_cell"
        ),
    }


def analyze(limit: int = 100) -> dict[str, object]:
    ps = primes_up_to(limit)
    cells = [analyze_pair(p, q) for i, p in enumerate(ps) for q in ps[i + 1 :]]
    closed = [c for c in cells if c["pascal_cell_closed"]]
    both = [c for c in cells if c["sum_level_preserved"] and c["difference_level_preserved"]]
    return {
        "schema": "PVG-LOCAL-ADDITIVE-CELL-ATLAS-001",
        "limit": limit,
        "prime_count": len(ps),
        "cell_count": len(cells),
        "closed_pascal_cell_count": len(closed),
        "difference_prime_cell_count": sum(bool(c["difference_is_prime"]) for c in cells),
        "double_preservation_count": len(both),
        "closed_pascal_triples": [[c["p"], c["q"], c["sum"]] for c in closed],
        "double_preservation_pairs": [[c["p"], c["q"]] for c in both],
        "sum_Omega_distribution": dict(sorted(Counter(int(c["sum_Omega"]) for c in cells).items())),
        "difference_Omega_distribution": dict(sorted(Counter(int(c["difference_Omega"]) for c in cells).items())),
        "sum_support_size_distribution": dict(sorted(Counter(int(c["sum_omega"]) for c in cells).items())),
        "difference_support_size_distribution": dict(sorted(Counter(int(c["difference_omega"]) for c in cells).items())),
        "theorems": {
            "closed_pascal_cell": "pg+qg=(p+q)g is a one-axis level-preserving cell iff p+q is prime",
            "prime_triple_shape": "for prime p<q with p+q prime, necessarily p=2 and q,q+2 are twin primes",
            "difference_preservation": "qg-pg=(q-p)g preserves Omega iff q-p is prime",
        },
        "verification": {
            "all_closed_cells_contain_axis_2": all(c["p"] == 2 for c in closed),
            "closed_cells_are_twin_prime_triples": all(c["sum"] == c["q"] + 2 for c in closed),
            "factorizations_reconstruct": all(
                prod(x["prime"] ** x["exponent"] for x in c["sum_factors"]) == c["sum"]
                and prod(x["prime"] ** x["exponent"] for x in c["difference_factors"]) == c["difference"]
                for c in cells
            ),
            "sum_preservation_matches_primality": all(c["sum_level_preserved"] == c["sum_is_prime"] for c in cells),
            "difference_preservation_matches_primality": all(c["difference_level_preserved"] == c["difference_is_prime"] for c in cells),
        },
        "cells": cells,
        "scientific_classification": "exact elementary identities plus finite atlas verification; no originality, asymptotic, or twin-prime claim",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a finite atlas of local additive PVG cells.")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    if args.limit < 3:
        parser.error("--limit must be at least 3")
    print(json.dumps(analyze(args.limit), ensure_ascii=False, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
