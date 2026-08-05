from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import prod
from pathlib import Path
from typing import Iterable

try:
    from tools.pvg_local_additive_cell_atlas import is_prime, primes_up_to
except ModuleNotFoundError:
    from pvg_local_additive_cell_atlas import is_prime, primes_up_to

Face = tuple[int, ...]
Edge = tuple[int, int]

REGISTERED_TARGET_PRIME_LIMIT = 31
REGISTERED_PREDECESSOR_PRIME_LIMIT = 31
REGISTERED_FACE_SIZES = (2, 3, 4)
REGISTERED_MAX_TARGET_FACE_SIZE = 4


def face_key(face: Face) -> str:
    return "{" + ",".join(str(value) for value in face) + "}"


def normalize_face(values: Iterable[int], *, allow_empty: bool = False) -> Face:
    face = tuple(sorted(set(int(value) for value in values)))
    if not face and not allow_empty:
        raise ValueError("face must be nonempty")
    if any(not is_prime(value) for value in face):
        raise ValueError("every face coordinate must be prime")
    return face


def factor_support(n: int) -> Face:
    if n < 1:
        raise ValueError("factor_support expects a positive integer")
    out: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            out.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        out.append(n)
    return tuple(out)


def successors(face: Face) -> tuple[Face, ...]:
    face = normalize_face(face)
    if len(face) < 2:
        return tuple()
    return tuple(sorted({factor_support(a + b) for a, b in combinations(face, 2)}))


def exact_support_numbers(target: Face, cap: int) -> tuple[int, ...]:
    """Return all n <= cap with exact prime support target.

    This implements the support-fiber law n = product(p**e_p), e_p >= 1.
    """
    target = normalize_face(target)
    if cap < 1:
        return tuple()
    radical = prod(target)
    if radical > cap:
        return tuple()

    values: set[int] = set()

    def visit(index: int, current: int) -> None:
        if index == len(target):
            values.add(current)
            return
        prime = target[index]
        value = current * prime
        while value <= cap:
            visit(index + 1, value)
            if value > cap // prime:
                break
            value *= prime

    visit(0, 1)
    return tuple(sorted(values))


def parity_feasible(target: Face) -> bool:
    """A target support is parity-feasible in a distinct-prime universe.

    Targets containing 2 require an odd+odd witness. Targets excluding 2
    require a 2+odd witness. Both are possible in principle, so the rule is
    recorded as a routing law rather than an exclusion except for the empty
    target, which normalization already rejects.
    """
    normalize_face(target)
    return True


def compression_certificate(target: Face, prime_limit: int) -> dict[str, object]:
    target = normalize_face(target)
    if prime_limit < 2:
        raise ValueError("prime_limit must be at least 2")
    sum_cap = 2 * prime_limit
    radical = prod(target)
    target_contains_two = 2 in target
    return {
        "target": list(target),
        "target_key": face_key(target),
        "prime_limit": prime_limit,
        "sum_cap": sum_cap,
        "radical": radical,
        "radical_bound_feasible": radical <= sum_cap,
        "maximum_axis_bound_feasible": max(target) <= sum_cap,
        "parity_route": (
            "odd_plus_odd"
            if target_contains_two
            else "two_plus_odd"
        ),
        "support_fiber_numbers": list(exact_support_numbers(target, sum_cap)),
    }


def witness_edges(target: Face, prime_limit: int) -> tuple[Edge, ...]:
    """Generate every prime edge {a,b} with supp(a+b)=target.

    The generator enumerates the exact support fiber below 2*prime_limit,
    then realizes those sums by distinct primes in the finite universe.
    """
    target = normalize_face(target)
    primes = tuple(primes_up_to(prime_limit))
    prime_set = set(primes)
    sum_cap = 2 * prime_limit
    if prod(target) > sum_cap or max(target) > sum_cap:
        return tuple()

    edges: set[Edge] = set()
    contains_two = 2 in target
    for total in exact_support_numbers(target, sum_cap):
        if contains_two:
            # An even total can only use two odd distinct primes.
            candidates = (p for p in primes if p != 2 and p < total - p)
        else:
            # An odd total must be 2 + an odd prime.
            candidates = (2,) if 2 < total - 2 else tuple()
        for left in candidates:
            right = total - left
            if left < right <= prime_limit and right in prime_set:
                edges.add((left, right))
    return tuple(sorted(edges))


def predecessors(
    target: Face,
    prime_limit: int,
    face_sizes: Iterable[int] = REGISTERED_FACE_SIZES,
) -> tuple[Face, ...]:
    """Generate all predecessor faces containing a witness edge.

    Witness-edge law:
        target in T(E) iff E contains a pair {a,b} with supp(a+b)=target.
    """
    target = normalize_face(target)
    sizes = tuple(sorted(set(int(size) for size in face_sizes)))
    if not sizes or any(size < 2 for size in sizes):
        raise ValueError("face sizes must be integers at least 2")
    universe = tuple(primes_up_to(prime_limit))
    edges = witness_edges(target, prime_limit)
    out: set[Face] = set()
    for edge in edges:
        remaining = tuple(value for value in universe if value not in edge)
        for size in sizes:
            extra_count = size - 2
            if extra_count > len(remaining):
                continue
            for extras in combinations(remaining, extra_count):
                out.add(tuple(sorted((*edge, *extras))))
    return tuple(sorted(out, key=lambda face: (len(face), face)))


def predecessor_certificate(target: Face, predecessor: Face) -> dict[str, object]:
    target = normalize_face(target)
    predecessor = normalize_face(predecessor)
    witnesses = []
    for left, right in combinations(predecessor, 2):
        total = left + right
        if factor_support(total) == target:
            witnesses.append({
                "edge": [left, right],
                "sum": total,
                "sum_support": list(target),
            })
    return {
        "target": list(target),
        "target_key": face_key(target),
        "predecessor": list(predecessor),
        "predecessor_key": face_key(predecessor),
        "is_predecessor": bool(witnesses),
        "witness_count": len(witnesses),
        "witnesses": witnesses,
        "forward_successors": [list(face) for face in successors(predecessor)],
    }


def brute_force_predecessors(
    target: Face,
    prime_limit: int,
    face_sizes: Iterable[int],
) -> tuple[Face, ...]:
    """Independent full forward enumeration used only as an oracle."""
    target = normalize_face(target)
    universe = tuple(primes_up_to(prime_limit))
    out = []
    for size in sorted(set(int(size) for size in face_sizes)):
        for face in combinations(universe, size):
            if target in successors(face):
                out.append(face)
    return tuple(out)


def target_universe(prime_limit: int, max_face_size: int) -> tuple[Face, ...]:
    primes = tuple(primes_up_to(prime_limit))
    out: list[Face] = []
    for size in range(1, max_face_size + 1):
        out.extend(combinations(primes, size))
    return tuple(out)


def reachability_table(
    prime_limit: int,
    face_sizes: Iterable[int],
    *,
    target_prime_limit: int | None = None,
    max_target_face_size: int = REGISTERED_MAX_TARGET_FACE_SIZE,
    include_predecessors: bool = False,
) -> dict[str, object]:
    sizes = tuple(sorted(set(int(size) for size in face_sizes)))
    target_limit = prime_limit if target_prime_limit is None else target_prime_limit
    records = []
    reachable_count = 0
    predecessor_count_by_size: Counter[int] = Counter()
    witness_edge_count = 0
    for target in target_universe(target_limit, max_target_face_size):
        edges = witness_edges(target, prime_limit)
        generated = predecessors(target, prime_limit, sizes)
        if generated:
            reachable_count += 1
        witness_edge_count += len(edges)
        for face in generated:
            predecessor_count_by_size[len(face)] += 1
        record: dict[str, object] = {
            "target": list(target),
            "target_key": face_key(target),
            "reachable_inside_box": bool(generated),
            "witness_edge_count": len(edges),
            "predecessor_count": len(generated),
            "predecessor_count_by_size": {
                str(size): sum(len(face) == size for face in generated)
                for size in sizes
            },
            "compression_certificate": compression_certificate(target, prime_limit),
        }
        if include_predecessors:
            record["predecessors"] = [list(face) for face in generated]
        records.append(record)
    return {
        "configuration": {
            "target_prime_limit": target_limit,
            "predecessor_prime_limit": prime_limit,
            "predecessor_face_sizes": list(sizes),
            "max_target_face_size": max_target_face_size,
            "complete_enumeration": True,
        },
        "target_count": len(records),
        "reachable_target_count": reachable_count,
        "unreachable_target_count": len(records) - reachable_count,
        "total_witness_edge_count_across_targets": witness_edge_count,
        "predecessor_incidence_count_by_face_size": {
            str(size): predecessor_count_by_size[size] for size in sizes
        },
        "records": records,
    }


def registered_analysis() -> dict[str, object]:
    table = reachability_table(
        REGISTERED_PREDECESSOR_PRIME_LIMIT,
        REGISTERED_FACE_SIZES,
        target_prime_limit=REGISTERED_TARGET_PRIME_LIMIT,
        max_target_face_size=REGISTERED_MAX_TARGET_FACE_SIZE,
        include_predecessors=False,
    )
    targets = target_universe(
        REGISTERED_TARGET_PRIME_LIMIT,
        REGISTERED_MAX_TARGET_FACE_SIZE,
    )
    completeness_failures = []
    soundness_failures = []
    for target in targets:
        generated = predecessors(
            target,
            REGISTERED_PREDECESSOR_PRIME_LIMIT,
            REGISTERED_FACE_SIZES,
        )
        oracle = brute_force_predecessors(
            target,
            REGISTERED_PREDECESSOR_PRIME_LIMIT,
            REGISTERED_FACE_SIZES,
        )
        if generated != oracle:
            completeness_failures.append(face_key(target))
        for face in generated:
            if target not in successors(face):
                soundness_failures.append({
                    "target": face_key(target),
                    "predecessor": face_key(face),
                })

    reachable_records = [
        record for record in table["records"] if record["reachable_inside_box"]
    ]
    target_size_distribution = Counter(
        len(record["target"]) for record in reachable_records
    )
    universe = tuple(primes_up_to(REGISTERED_PREDECESSOR_PRIME_LIMIT))
    face_count = sum(
        1 for size in REGISTERED_FACE_SIZES for _ in combinations(universe, size)
    )
    brute_force_pair_evaluations = sum(
        sum(1 for _ in combinations(face, 2))
        for size in REGISTERED_FACE_SIZES
        for face in combinations(universe, size)
    )
    return {
        "schema": "PVG-INVERSE-SUPPORT-KERNEL-ENGINE-002",
        "classification": "finite_exact_inside_frozen_box",
        "compression_laws": [
            {
                "id": "LAW-INVERSE-WITNESS-EDGE-001",
                "statement": "F in T(E) iff E contains an edge {a,b} with supp(a+b)=F.",
                "status": "exact",
            },
            {
                "id": "LAW-INVERSE-SUPPORT-FIBER-001",
                "statement": "Witness sums lie in the exact support fiber product(r^e_r), e_r>=1, below 2P.",
                "status": "exact",
            },
            {
                "id": "LAW-INVERSE-PARITY-ROUTING-001",
                "statement": "2 in F routes to odd+odd witnesses; 2 not in F routes to 2+odd witnesses.",
                "status": "exact",
            },
            {
                "id": "LAW-INVERSE-RADICAL-BOUND-001",
                "statement": "rad(F)>2P or max(F)>2P implies no witness edge in the prime universe <=P.",
                "status": "exact_inside_box",
            },
        ],
        "registered_box": table["configuration"],
        "prime_universe": list(universe),
        "predecessor_face_count": face_count,
        "brute_force_pair_evaluation_count": brute_force_pair_evaluations,
        "target_count": table["target_count"],
        "reachable_target_count": table["reachable_target_count"],
        "unreachable_target_count": table["unreachable_target_count"],
        "reachable_target_size_distribution": {
            str(size): target_size_distribution[size]
            for size in sorted(target_size_distribution)
        },
        "predecessor_incidence_count_by_face_size": table[
            "predecessor_incidence_count_by_face_size"
        ],
        "reachable_targets": reachable_records,
        "unreachable_target_keys": [
            record["target_key"]
            for record in table["records"]
            if not record["reachable_inside_box"]
        ],
        "verification": {
            "soundness": not soundness_failures,
            "completeness_against_full_forward_enumeration": not completeness_failures,
            "deduplication": all(
                len(predecessors(target, REGISTERED_PREDECESSOR_PRIME_LIMIT, REGISTERED_FACE_SIZES))
                == len(set(predecessors(target, REGISTERED_PREDECESSOR_PRIME_LIMIT, REGISTERED_FACE_SIZES)))
                for target in targets
            ),
            "determinism": table == reachability_table(
                REGISTERED_PREDECESSOR_PRIME_LIMIT,
                REGISTERED_FACE_SIZES,
                target_prime_limit=REGISTERED_TARGET_PRIME_LIMIT,
                max_target_face_size=REGISTERED_MAX_TARGET_FACE_SIZE,
                include_predecessors=False,
            ),
            "multi_axis_predecessor_sizes_checked": [3, 4],
            "soundness_failures": soundness_failures,
            "completeness_failures": completeness_failures,
        },
        "claim_ceiling": {
            "reachability": "inside_frozen_box_only",
            "unreachability": "inside_frozen_box_only",
            "general_inverse_theorem": False,
            "ant_progress": False,
            "goldbach_progress": False,
            "pnt_progress": False,
            "rh_grh_progress": False,
        },
    }


def parse_face(raw: str) -> Face:
    return normalize_face(int(part.strip()) for part in raw.split(",") if part.strip())


def parse_sizes(raw: str) -> tuple[int, ...]:
    sizes = tuple(sorted(set(int(part.strip()) for part in raw.split(",") if part.strip())))
    if not sizes or any(size < 2 for size in sizes):
        raise ValueError("face sizes must be comma-separated integers >=2")
    return sizes


def main() -> None:
    parser = argparse.ArgumentParser(description="PVG ENGINE-002 inverse support kernel")
    parser.add_argument("--target", help="comma-separated target face")
    parser.add_argument("--prime-limit", type=int, default=REGISTERED_PREDECESSOR_PRIME_LIMIT)
    parser.add_argument("--face-sizes", default=",".join(map(str, REGISTERED_FACE_SIZES)))
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--output")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    if args.registered_summary:
        result = registered_analysis()
    elif args.target:
        target = parse_face(args.target)
        sizes = parse_sizes(args.face_sizes)
        generated = predecessors(target, args.prime_limit, sizes)
        result = {
            "target": list(target),
            "target_key": face_key(target),
            "compression_certificate": compression_certificate(target, args.prime_limit),
            "witness_edges": [list(edge) for edge in witness_edges(target, args.prime_limit)],
            "predecessor_count": len(generated),
            "predecessors": [
                predecessor_certificate(target, face) for face in generated
            ],
        }
    else:
        parser.error("provide --target or --registered-summary")

    text = json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2, sort_keys=True)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
