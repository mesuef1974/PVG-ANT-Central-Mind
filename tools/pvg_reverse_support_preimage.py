from __future__ import annotations

import argparse
import bisect
import json
from dataclasses import asdict, dataclass
from math import isqrt, prod

try:
    from tools.pvg_deep_orbit_preimage_families import (
        analyze_support_orbit,
        factor_support,
        face_key,
        successors,
    )
except ModuleNotFoundError:
    from pvg_deep_orbit_preimage_families import (
        analyze_support_orbit,
        factor_support,
        face_key,
        successors,
    )

Face = tuple[int, ...]


@dataclass(frozen=True)
class FrozenConfig:
    target_prime_pair_closure_depth: int = 12
    known_tail_support: Face = (2, 167071)
    known_tail_support_closure_depth: int = 10
    reverse_support_depth_budget: int = 1
    predecessor_support_class: str = "binary_prime_faces_only"
    reverse_seed_integer_cap: int = 5_346_272
    candidate_support_node_cap: int = 50_000
    candidate_integer_cap: int = 1_000_000_000_000
    prime_pair_realization_cap: int = 1_000_000_000_000
    orbit_verification_depth_cap: int = 16
    registered_top_witness_count: int = 25
    ranking_rule: str = (
        "exposing_prime_limit,source_sum,predecessor_radical,"
        "predecessor_support,seed_sum"
    )
    pruning_rules: tuple[str, ...] = (
        "binary predecessor supports only",
        "exact support equality required",
        "distinct primes only",
        "deduplicate predecessor supports",
        "candidate integers above cap removed",
        "source primes above realization cap removed",
        "no adaptive cap extension",
        "no multi-axis predecessor expansion",
        "no PASS-026 continuation",
    )


REGISTERED_CONFIG = FrozenConfig()
REGISTERED_OUTCOMES = {
    "DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS",
    "FINITE_ABSENCE_WITHIN_FROZEN_CLASS",
    "CONFIGURATION_CAP_EXCEEDED_NO_RESULT_PROMOTION",
}


def prime_sieve(limit: int) -> tuple[bytearray, list[int]]:
    if limit < 2:
        raise ValueError("prime sieve limit must be at least 2")
    table = bytearray(b"\x01") * (limit + 1)
    table[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if not table[p]:
            continue
        start = p * p
        table[start: limit + 1: p] = b"\x00" * (((limit - start) // p) + 1)
    return table, [n for n in range(2, limit + 1) if table[n]]


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % n == 0:
            continue
        x = pow(base, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def binary_exact_support_powers(a: int, b: int, cap: int) -> list[tuple[int, int, int]]:
    if not (2 <= a < b):
        raise ValueError("binary support must satisfy 2 <= a < b")
    if cap < a * b:
        return []
    rows: list[tuple[int, int, int]] = []
    power_a, exponent_a = a, 1
    while power_a <= cap // b:
        power_b, exponent_b = b, 1
        while power_a <= cap // power_b:
            rows.append((power_a * power_b, exponent_a, exponent_b))
            if power_b > cap // b:
                break
            power_b *= b
            exponent_b += 1
        if power_a > cap // a:
            break
        power_a *= a
        exponent_a += 1
    rows.sort()
    return rows


def distinct_prime_pairs(n: int, is_prime: bytearray, primes: list[int]) -> list[Face]:
    if n < 5 or n >= len(is_prime):
        raise ValueError("n must lie inside the prime sieve")
    out: list[Face] = []
    stop = bisect.bisect_left(primes, (n + 1) // 2)
    for p in primes[:stop]:
        q = n - p
        if p < q and is_prime[q]:
            out.append((p, q))
    return out


def orbit_record(start: Face, max_depth: int) -> dict[str, object]:
    orbit = analyze_support_orbit(start, max_depth)
    closure = orbit["support_closure_depth"]
    layers = orbit["orbit_layers_from_support"]
    used_layers = layers if closure is None else layers[: int(closure) + 1]
    return {
        "source_face": list(start),
        "source_face_key": face_key(start),
        "face_closure_depth": closure,
        "terminal_axes": orbit["final_terminal_axes"],
        "terminal_key": orbit["final_terminal_key"],
        "layers": used_layers,
    }


def witness_sort_key(row: dict[str, object]) -> tuple[object, ...]:
    support = tuple(row["predecessor_support"])
    return (
        int(row["exposing_prime_limit"]),
        int(row["source_sum"]),
        int(row["predecessor_radical"]),
        support,
        int(row["seed_sum"]),
    )


def analyze(config: FrozenConfig = REGISTERED_CONFIG) -> dict[str, object]:
    if config.known_tail_support != tuple(sorted(set(config.known_tail_support))):
        raise ValueError("known_tail_support must be a strictly increasing face")
    if len(config.known_tail_support) != 2:
        raise ValueError("registered reverse pass requires a binary known tail")
    if config.reverse_support_depth_budget != 1:
        raise ValueError("registered reverse pass freezes one reverse support layer")
    if config.target_prime_pair_closure_depth != (
        config.known_tail_support_closure_depth + 2
    ):
        raise ValueError("target depth must equal known tail depth plus two")

    tail_orbit = analyze_support_orbit(
        config.known_tail_support, config.orbit_verification_depth_cap
    )
    if tail_orbit["support_closure_depth"] != config.known_tail_support_closure_depth:
        raise RuntimeError("known tail closure depth does not match the frozen certificate")

    seed_rows = binary_exact_support_powers(
        config.known_tail_support[0],
        config.known_tail_support[1],
        config.reverse_seed_integer_cap,
    )
    seed_integers = [row[0] for row in seed_rows]
    is_prime, primes = prime_sieve(config.reverse_seed_integer_cap)

    predecessor_seed: dict[Face, int] = {}
    seed_representation_counts: dict[str, int] = {}
    seed_power_rows: list[dict[str, object]] = []
    collision_rows: list[dict[str, object]] = []

    for seed, exponent_a, exponent_b in seed_rows:
        if factor_support(seed) != config.known_tail_support:
            raise RuntimeError("generated seed does not have the exact frozen support")
        pairs = distinct_prime_pairs(seed, is_prime, primes)
        seed_representation_counts[str(seed)] = len(pairs)
        seed_power_rows.append({
            "seed_sum": seed,
            "known_tail_exponents": [exponent_a, exponent_b],
            "distinct_prime_pair_count": len(pairs),
        })
        for predecessor in pairs:
            prior = predecessor_seed.get(predecessor)
            if prior is not None and prior != seed:
                collision_rows.append({
                    "predecessor_support": list(predecessor),
                    "first_seed_sum": prior,
                    "second_seed_sum": seed,
                })
                continue
            predecessor_seed[predecessor] = seed

    predecessor_count = len(predecessor_seed)
    cap_exceeded = predecessor_count > config.candidate_support_node_cap
    if collision_rows:
        raise RuntimeError("a predecessor support was associated with multiple seed sums")

    base_result: dict[str, object] = {
        "schema": "PVG-REVERSE-SUPPORT-PREIMAGE-001",
        "classification": (
            "confirmatory exhaustive search inside one frozen binary-predecessor "
            "class; exact construction and forward verification, finite caps, "
            "explicit reconnaissance contamination, no global depth theorem"
        ),
        "configuration": {
            **asdict(config),
            "known_tail_support": list(config.known_tail_support),
            "pruning_rules": list(config.pruning_rules),
            "configuration_id":
                "PASS-025-REVERSE-SUPPORT-PREIMAGE-FROZEN-CONFIG-001",
            "contamination_status":
                "not_blinded_prior_reconnaissance_recorded",
        },
        "target": {
            "known_tail_support": list(config.known_tail_support),
            "known_tail_support_key": face_key(config.known_tail_support),
            "known_tail_support_closure_depth":
                config.known_tail_support_closure_depth,
            "target_prime_pair_closure_depth":
                config.target_prime_pair_closure_depth,
            "reverse_chain":
                "source prime pair -> binary predecessor -> known tail -> terminal",
        },
        "seed_fiber": {
            "seed_integer_count": len(seed_rows),
            "seed_integers": seed_integers,
            "seed_rows": seed_power_rows,
            "total_distinct_prime_pair_representations":
                sum(seed_representation_counts.values()),
        },
        "predecessor_support_count": predecessor_count,
        "predecessor_support_cap_exceeded": cap_exceeded,
    }

    if cap_exceeded:
        return {
            **base_result,
            "outcome": "CONFIGURATION_CAP_EXCEEDED_NO_RESULT_PROMOTION",
            "candidate_exact_support_integer_count": 0,
            "candidate_supports_with_integers": 0,
            "witness_candidate_count": 0,
            "promoted_witnesses": [],
            "first_witness": None,
            "verification": {
                "known_tail_depth_matches_frozen_certificate": True,
                "every_predecessor_has_one_seed_sum": not collision_rows,
                "predecessor_node_cap_respected": False,
                "no_result_promoted_after_cap_failure": True,
            },
            "caution": (
                "The frozen predecessor-node cap was exceeded. The pass stops "
                "without truncation and without result promotion."
            ),
        }

    candidate_integer_count = 0
    candidate_supports_with_integers = 0
    primality_test_count = 0
    witness_candidates: list[dict[str, object]] = []
    per_seed_candidate_counts = {str(seed): 0 for seed in seed_integers}
    per_seed_witness_counts = {str(seed): 0 for seed in seed_integers}

    for predecessor, seed in sorted(
        predecessor_seed.items(), key=lambda item: (item[1], item[0])
    ):
        a, b = predecessor
        if a + b != seed:
            raise RuntimeError("predecessor support was detached from its seed sum")
        if successors(predecessor) != (config.known_tail_support,):
            raise RuntimeError("predecessor does not map to the frozen known tail")
        candidate_rows = binary_exact_support_powers(
            a, b, config.candidate_integer_cap
        )
        if candidate_rows:
            candidate_supports_with_integers += 1
        candidate_integer_count += len(candidate_rows)
        per_seed_candidate_counts[str(seed)] += len(candidate_rows)

        for source_sum, exponent_a, exponent_b in candidate_rows:
            source_prime = source_sum - 2
            if source_prime > config.prime_pair_realization_cap:
                continue
            primality_test_count += 1
            if not is_prime_64(source_prime):
                continue
            row = {
                "source_pair": [2, source_prime],
                "source_sum": source_sum,
                "exposing_prime_limit": source_prime,
                "predecessor_support": list(predecessor),
                "predecessor_support_key": face_key(predecessor),
                "predecessor_radical": prod(predecessor),
                "predecessor_exponents": [exponent_a, exponent_b],
                "seed_sum": seed,
                "known_tail_support": list(config.known_tail_support),
                "primality_certificate":
                    "deterministic Miller-Rabin for unsigned 64-bit integers",
            }
            witness_candidates.append(row)
            per_seed_witness_counts[str(seed)] += 1

    witness_candidates.sort(key=witness_sort_key)
    promoted: list[dict[str, object]] = []
    for row in witness_candidates[: config.registered_top_witness_count]:
        source_pair = tuple(row["source_pair"])
        predecessor = tuple(row["predecessor_support"])
        source_sum = int(row["source_sum"])
        seed = int(row["seed_sum"])
        if sum(source_pair) != source_sum:
            raise RuntimeError("source pair does not reconstruct the source sum")
        if factor_support(source_sum) != predecessor:
            raise RuntimeError("source sum does not have the predecessor support")
        if sum(predecessor) != seed:
            raise RuntimeError("predecessor does not reconstruct its seed sum")
        if factor_support(seed) != config.known_tail_support:
            raise RuntimeError("seed does not have the known tail support")
        orbit = orbit_record(source_pair, config.orbit_verification_depth_cap)
        layers = orbit["layers"]
        if orbit["face_closure_depth"] != config.target_prime_pair_closure_depth:
            raise RuntimeError("promoted witness does not close at target depth")
        if layers[1] != [list(predecessor)]:
            raise RuntimeError("witness first layer is not the predecessor support")
        if layers[2] != [list(config.known_tail_support)]:
            raise RuntimeError("witness second layer is not the frozen known tail")
        promoted.append({**row, "forward_orbit": orbit})

    if witness_candidates:
        outcome = "DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS"
        first_witness = promoted[0]
    else:
        outcome = "FINITE_ABSENCE_WITHIN_FROZEN_CLASS"
        first_witness = None

    verification = {
        "known_tail_depth_matches_frozen_certificate":
            tail_orbit["support_closure_depth"]
            == config.known_tail_support_closure_depth,
        "seed_supports_are_exact": all(
            factor_support(seed) == config.known_tail_support
            for seed in seed_integers
        ),
        "every_predecessor_has_one_seed_sum": not collision_rows,
        "every_predecessor_reconstructs_its_seed": all(
            sum(predecessor) == seed
            for predecessor, seed in predecessor_seed.items()
        ),
        "every_predecessor_maps_to_known_tail": all(
            successors(predecessor) == (config.known_tail_support,)
            for predecessor in predecessor_seed
        ),
        "predecessor_node_cap_respected":
            predecessor_count <= config.candidate_support_node_cap,
        "all_promoted_source_pairs_reconstruct_sums": all(
            sum(row["source_pair"]) == row["source_sum"] for row in promoted
        ),
        "all_promoted_source_sums_have_predecessor_support": all(
            factor_support(row["source_sum"]) == tuple(row["predecessor_support"])
            for row in promoted
        ),
        "all_promoted_predecessors_reconstruct_seed": all(
            sum(row["predecessor_support"]) == row["seed_sum"]
            for row in promoted
        ),
        "all_promoted_orbits_close_at_target": all(
            row["forward_orbit"]["face_closure_depth"]
            == config.target_prime_pair_closure_depth
            for row in promoted
        ),
        "all_promoted_orbits_enter_tail_at_depth_two": all(
            row["forward_orbit"]["layers"][2]
            == [list(config.known_tail_support)]
            for row in promoted
        ),
        "first_witness_is_rank_minimum":
            first_witness is None
            or witness_sort_key(first_witness) == witness_sort_key(witness_candidates[0]),
        "outcome_is_registered": outcome in REGISTERED_OUTCOMES,
    }

    return {
        **base_result,
        "outcome": outcome,
        "candidate_supports_with_integers": candidate_supports_with_integers,
        "candidate_exact_support_integer_count": candidate_integer_count,
        "primality_test_count": primality_test_count,
        "witness_candidate_count": len(witness_candidates),
        "per_seed_candidate_integer_counts": per_seed_candidate_counts,
        "per_seed_witness_candidate_counts": per_seed_witness_counts,
        "promoted_witness_count": len(promoted),
        "promoted_witnesses": promoted,
        "first_witness": first_witness,
        "verification": verification,
        "minimality_scope": (
            "minimum exposing prime limit only within the frozen binary-predecessor "
            "class, seed cap, candidate cap, realization cap, and ranking rule"
        ),
        "caution": (
            "The registered run is confirmatory, not blinded. A depth-12 witness "
            "does not imply globally minimal depth-12 threshold, unbounded depths, "
            "general termination, or progress on Goldbach, PNT, RH, or GRH."
        ),
    }


def registered_summary(data: dict[str, object]) -> dict[str, object]:
    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run the frozen PASS-025 reverse support-preimage search and emit "
            "a deterministic finite certificate."
        )
    )
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    data = analyze()
    if args.registered_summary:
        data = registered_summary(data)
    print(json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        indent=None if args.compact else 2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
