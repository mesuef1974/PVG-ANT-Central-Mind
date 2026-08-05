from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import gcd, prod
from pathlib import Path
from typing import Iterable, Iterator

try:
    from tools.pvg_local_additive_cell_atlas import is_prime, primes_up_to
except ModuleNotFoundError:
    from pvg_local_additive_cell_atlas import is_prime, primes_up_to

Support = tuple[int, ...]
ExponentVector = tuple[int, ...]

REGISTERED_SUPPORT_PRIME_LIMIT = 11
REGISTERED_SUPPORT_FACE_SIZES = (1, 2, 3)
REGISTERED_INTEGER_CAP = 100_000
REGISTERED_DIRICHLET_S = 2.0


def support_key(face: Support) -> str:
    return "{" + ",".join(str(value) for value in face) + "}"


def normalize_support(values: Iterable[int]) -> Support:
    face = tuple(sorted(set(int(value) for value in values)))
    if not face:
        raise ValueError("support must be nonempty")
    if any(not is_prime(value) for value in face):
        raise ValueError("every support coordinate must be prime")
    return face


def factor_support(n: int) -> Support:
    if n < 1:
        raise ValueError("factor_support expects a positive integer")
    out: list[int] = []
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            out.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        out.append(remaining)
    return tuple(out)


def exponent_vector(n: int, face: Support) -> ExponentVector:
    face = normalize_support(face)
    if n < 1:
        raise ValueError("n must be positive")
    exponents: list[int] = []
    remaining = n
    for prime in face:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        exponents.append(exponent)
    if remaining != 1 or any(exponent < 1 for exponent in exponents):
        raise ValueError("n does not have the requested exact support")
    return tuple(exponents)


def reconstruct(face: Support, exponents: ExponentVector) -> int:
    face = normalize_support(face)
    if len(face) != len(exponents):
        raise ValueError("face and exponent vector lengths differ")
    if any(int(exponent) < 1 for exponent in exponents):
        raise ValueError("all exponents must be positive")
    return prod(prime ** int(exponent) for prime, exponent in zip(face, exponents))


def exponent_vectors(face: Support, cap: int) -> tuple[ExponentVector, ...]:
    face = normalize_support(face)
    if cap < 1 or prod(face) > cap:
        return tuple()
    out: list[ExponentVector] = []

    def visit(index: int, current: int, exponents: tuple[int, ...]) -> None:
        if index == len(face):
            out.append(exponents)
            return
        prime = face[index]
        value = current * prime
        exponent = 1
        while value <= cap:
            visit(index + 1, value, (*exponents, exponent))
            if value > cap // prime:
                break
            value *= prime
            exponent += 1

    visit(0, 1, tuple())
    return tuple(sorted(out, key=lambda vector: (reconstruct(face, vector), vector)))


def integer_fiber(face: Support, cap: int) -> tuple[int, ...]:
    face = normalize_support(face)
    return tuple(reconstruct(face, vector) for vector in exponent_vectors(face, cap))


def brute_force_integer_fiber(face: Support, cap: int) -> tuple[int, ...]:
    face = normalize_support(face)
    if cap < 1:
        return tuple()
    return tuple(n for n in range(1, cap + 1) if factor_support(n) == face)


def divides_in_fiber(left: ExponentVector, right: ExponentVector) -> bool:
    if len(left) != len(right):
        raise ValueError("exponent vectors must have equal length")
    return all(a <= b for a, b in zip(left, right))


def hasse_edges(face: Support, cap: int) -> tuple[tuple[ExponentVector, ExponentVector], ...]:
    face = normalize_support(face)
    vectors = set(exponent_vectors(face, cap))
    edges: list[tuple[ExponentVector, ExponentVector]] = []
    for vector in sorted(vectors):
        for index in range(len(face)):
            successor = list(vector)
            successor[index] += 1
            successor_tuple = tuple(successor)
            if successor_tuple in vectors:
                edges.append((vector, successor_tuple))
    return tuple(edges)


def dirichlet_partial_sum(face: Support, s: float, cap: int) -> float:
    face = normalize_support(face)
    if s <= 0:
        raise ValueError("s must be positive")
    return sum(n ** (-s) for n in integer_fiber(face, cap))


def dirichlet_closed_form(face: Support, s: float) -> float:
    face = normalize_support(face)
    if s <= 0:
        raise ValueError("s must be positive")
    return prod(1.0 / (prime ** s - 1.0) for prime in face)


def fiber_record(face: Support, cap: int, *, s: float = REGISTERED_DIRICHLET_S) -> dict[str, object]:
    face = normalize_support(face)
    vectors = exponent_vectors(face, cap)
    values = tuple(reconstruct(face, vector) for vector in vectors)
    edges = hasse_edges(face, cap)
    partial = dirichlet_partial_sum(face, s, cap)
    closed = dirichlet_closed_form(face, s)
    return {
        "support": list(face),
        "support_key": support_key(face),
        "radical": prod(face),
        "integer_cap": cap,
        "fiber_count": len(values),
        "minimum": values[0] if values else None,
        "maximum": values[-1] if values else None,
        "maximum_total_exponent": max((sum(vector) for vector in vectors), default=0),
        "hasse_edge_count": len(edges),
        "dirichlet_s": s,
        "dirichlet_partial_sum": partial,
        "dirichlet_closed_form": closed,
        "dirichlet_gap": closed - partial,
        "first_values": list(values[:12]),
        "last_values": list(values[-5:]),
    }


def support_universe(prime_limit: int, face_sizes: Iterable[int]) -> tuple[Support, ...]:
    primes = tuple(primes_up_to(prime_limit))
    out: list[Support] = []
    for size in sorted(set(int(size) for size in face_sizes)):
        if size < 1:
            raise ValueError("support sizes must be positive")
        out.extend(combinations(primes, size))
    return tuple(out)


def registered_summary() -> dict[str, object]:
    faces = support_universe(REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES)
    records = [fiber_record(face, REGISTERED_INTEGER_CAP) for face in faces]
    exact_matches = []
    for face in faces:
        exact_matches.append(integer_fiber(face, REGISTERED_INTEGER_CAP) == brute_force_integer_fiber(face, REGISTERED_INTEGER_CAP))

    closure_examples = []
    for face in faces:
        values = integer_fiber(face, REGISTERED_INTEGER_CAP)
        if len(values) < 2:
            continue
        left, right = values[0], values[min(1, len(values) - 1)]
        closure_examples.append({
            "support": list(face),
            "left": left,
            "right": right,
            "product_support": list(factor_support(left * right)),
            "gcd_support": list(factor_support(gcd(left, right))),
            "lcm_support": list(factor_support(left * right // gcd(left, right))),
        })

    return {
        "id": "ENGINE-003-INVERSE-INTEGER-FIBERS-SUMMARY-001",
        "classification": "Identity / Finite-Verified / Diagnostic",
        "scope": {
            "support_prime_limit": REGISTERED_SUPPORT_PRIME_LIMIT,
            "support_face_sizes": list(REGISTERED_SUPPORT_FACE_SIZES),
            "integer_cap": REGISTERED_INTEGER_CAP,
            "dirichlet_test_s": REGISTERED_DIRICHLET_S,
            "support_face_count": len(faces),
        },
        "exact_laws": {
            "fiber": "N(F)={prod(p^e_p): e_p>=1}",
            "exponent_lattice": "N_{>=1}^{|F|} bijects with N(F)",
            "divisibility": "coordinatewise exponent order",
            "hasse_cover": "increment exactly one exponent by one",
            "closed_operations": ["multiplication", "gcd", "lcm"],
            "not_generally_closed": ["addition", "integer_quotient"],
            "dirichlet_series": "sum_{n in N(F)} n^{-s}=prod_{p in F}(p^s-1)^{-1}, Re(s)>0",
        },
        "totals": {
            "total_fiber_points_across_faces": sum(int(record["fiber_count"]) for record in records),
            "total_hasse_edges_across_faces": sum(int(record["hasse_edge_count"]) for record in records),
            "complete_scan_match_count": sum(exact_matches),
            "complete_scan_mismatch_count": len(exact_matches) - sum(exact_matches),
        },
        "records": records,
        "closure_examples": closure_examples,
        "verification": {
            "all_generators_match_complete_scan": all(exact_matches),
            "all_radical_minima_hold": all(record["minimum"] == record["radical"] for record in records),
            "all_dirichlet_partial_sums_below_closed_form": all(
                0.0 <= float(record["dirichlet_gap"]) for record in records
            ),
            "deterministic_ordering": True,
        },
        "claim_ceiling": {
            "historical_originality": False,
            "phase_c_authorized": False,
            "goldbach_progress": False,
            "pnt_progress": False,
            "rh_progress": False,
            "grh_progress": False,
        },
    }


def write_registered_summary(output: Path) -> dict[str, object]:
    summary = registered_summary()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def parse_support(text: str) -> Support:
    return normalize_support(int(part.strip()) for part in text.split(",") if part.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate and certify exact PVG integer fibers.")
    parser.add_argument("support", nargs="?", help="comma-separated prime support, for example 2,3,5")
    parser.add_argument("--cap", type=int, default=REGISTERED_INTEGER_CAP)
    parser.add_argument("--s", type=float, default=REGISTERED_DIRICHLET_S)
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    if args.registered_summary:
        summary = registered_summary()
        if args.output is not None:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2))
        return

    if not args.support:
        parser.error("support is required unless --registered-summary is used")
    record = fiber_record(parse_support(args.support), args.cap, s=args.s)
    print(json.dumps(record, ensure_ascii=False, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
