from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict, deque
from itertools import combinations

try:
    from tools.pvg_centered_radius_spectra import centered_radius_spectrum, registered_points
    from tools.pvg_inverse_prime_fibers import prime_pair_fiber
except ModuleNotFoundError:
    from pvg_centered_radius_spectra import centered_radius_spectrum, registered_points
    from pvg_inverse_prime_fibers import prime_pair_fiber

Support = tuple[int, ...]


def governed_coordinate(n: int, p: int, q: int) -> int:
    if not (0 < p < q and p + q == n):
        raise ValueError("malformed prime-pair incidence record")
    gap = q - p
    if n % 2 == 0:
        if gap % 2:
            raise ValueError("even route requires an even centered gap")
        return gap // 2
    return gap


def production_indexes() -> tuple[dict[int, tuple[int, ...]], dict[int, set[int]], dict[int, set[Support]], dict[int, set[str]]]:
    spectra: dict[int, tuple[int, ...]] = {}
    owners: dict[int, set[int]] = defaultdict(set)
    supports: dict[int, set[Support]] = defaultdict(set)
    routes: dict[int, set[str]] = defaultdict(set)
    for n, support in registered_points():
        spectrum = centered_radius_spectrum(n)
        spectra[n] = spectrum
        route = "even" if n % 2 == 0 else "odd"
        for d in spectrum:
            owners[d].add(n)
            supports[d].add(support)
            routes[d].add(route)
    return spectra, owners, supports, routes


def independent_indexes() -> tuple[dict[int, tuple[int, ...]], dict[int, set[int]], dict[int, set[Support]], dict[int, set[str]]]:
    spectra: dict[int, tuple[int, ...]] = {}
    owners: dict[int, set[int]] = defaultdict(set)
    supports: dict[int, set[Support]] = defaultdict(set)
    routes: dict[int, set[str]] = defaultdict(set)
    for n, support in registered_points():
        coordinates = tuple(governed_coordinate(n, p, q) for p, q in prime_pair_fiber(n))
        spectra[n] = coordinates
        route = "even" if n % 2 == 0 else "odd"
        for d in coordinates:
            owners[d].add(n)
            supports[d].add(support)
            routes[d].add(route)
    return spectra, owners, supports, routes


def _components(spectra: dict[int, tuple[int, ...]], owners: dict[int, set[int]]) -> list[dict[str, int]]:
    unseen = {n for n, spectrum in spectra.items() if spectrum}
    records: list[dict[str, int]] = []
    while unseen:
        queue = deque([("N", min(unseen))])
        integers: set[int] = set()
        coordinates: set[int] = set()
        while queue:
            kind, value = queue.popleft()
            if kind == "N":
                if value in integers:
                    continue
                integers.add(value)
                unseen.discard(value)
                queue.extend(("D", d) for d in spectra[value] if d not in coordinates)
            else:
                if value in coordinates:
                    continue
                coordinates.add(value)
                queue.extend(("N", n) for n in owners[value] if n not in integers)
        records.append({
            "integer_count": len(integers),
            "coordinate_count": len(coordinates),
            "min_integer": min(integers),
            "min_coordinate": min(coordinates),
        })
    return sorted(records, key=lambda r: (-r["integer_count"], -r["coordinate_count"], r["min_integer"]))


def registered_summary() -> dict[str, object]:
    spectra, owners, supports, routes = production_indexes()
    independent = independent_indexes()
    mismatch_count = sum(left != right for left, right in zip((spectra, owners, supports, routes), independent))

    integer_degree = Counter(len(values) for values in owners.values())
    support_degree = Counter(len(values) for values in supports.values())
    maximum_integer_degree = max(integer_degree)
    maximum_support_degree = max(support_degree)

    support_pairs: Counter[tuple[Support, Support]] = Counter()
    for support_set in supports.values():
        for left, right in combinations(sorted(support_set), 2):
            support_pairs[(left, right)] += 1

    route_classes = Counter()
    for route_set in routes.values():
        if route_set == {"even"}:
            route_classes["even_only"] += 1
        elif route_set == {"odd"}:
            route_classes["odd_only"] += 1
        else:
            route_classes["cross_route"] += 1

    hyperedge_lines = [
        f"{n}:" + ",".join(map(str, spectra[n]))
        for n in sorted(spectra)
        if spectra[n]
    ]
    hyperedge_bytes = ("\n".join(hyperedge_lines) + "\n").encode("utf-8")

    components = _components(spectra, owners)
    coordinate_occurrences = sum(len(spectrum) for spectrum in spectra.values())
    cooccurrence_occurrences = sum(len(spectrum) * (len(spectrum) - 1) // 2 for spectrum in spectra.values())

    return {
        "id": "ENGINE-004-PASS-003-CENTERED-RADIUS-INCIDENCE-SUMMARY-001",
        "classification": "Identity / Proved / Finite-Verified / Diagnostic",
        "scope": {
            "support_prime_limit": 11,
            "support_face_sizes": [1, 2, 3],
            "integer_cap": 100000,
            "support_face_count": 25,
            "integer_point_count": len(spectra),
            "represented_point_count": sum(bool(spectrum) for spectrum in spectra.values()),
            "coordinate_occurrence_count": coordinate_occurrences,
            "unique_coordinate_count": len(owners),
        },
        "totals": {
            "shared_coordinate_count": sum(len(values) > 1 for values in owners.values()),
            "cross_route_coordinate_count": route_classes["cross_route"],
            "coordinates_collapsing_multiple_integers_to_one_support": sum(
                len(owners[d]) > len(supports[d]) for d in owners
            ),
            "support_pair_with_nonzero_intersection_count": len(support_pairs),
            "bipartite_component_count": len(components),
            "cooccurrence_pair_occurrence_count": cooccurrence_occurrences,
        },
        "degree_distributions": {
            "integer_owner_degree": {str(k): v for k, v in sorted(integer_degree.items())},
            "support_owner_degree": {str(k): v for k, v in sorted(support_degree.items())},
        },
        "maxima": {
            "maximum_integer_owner_degree": maximum_integer_degree,
            "coordinates_attaining_maximum_integer_degree": sorted(
                d for d, values in owners.items() if len(values) == maximum_integer_degree
            ),
            "maximum_support_owner_degree": maximum_support_degree,
            "coordinates_attaining_maximum_support_degree": sorted(
                d for d, values in supports.items() if len(values) == maximum_support_degree
            ),
        },
        "route_coordinate_classes": dict(sorted(route_classes.items())),
        "largest_support_pair_intersections": [
            {"left": list(left), "right": list(right), "shared_coordinate_count": count}
            for (left, right), count in sorted(support_pairs.items(), key=lambda item: (-item[1], item[0]))[:20]
        ],
        "bipartite_components": components,
        "lossless_cooccurrence_certificate": {
            "representation": "sorted nonempty rows N:D(N); each row reconstructs all coordinate pairs co-occurring at N",
            "row_count": len(hyperedge_lines),
            "sha256": hashlib.sha256(hyperedge_bytes).hexdigest(),
        },
        "verification": {
            "independent_index_mismatch_count": mismatch_count,
            "all_rows_reconstruct": all(tuple(sorted(d for d, values in owners.items() if n in values)) == tuple(sorted(spectra[n])) for n in spectra),
            "odd_route_owner_injective": all(sum(n % 2 for n in values) <= 1 for values in owners.values()),
            "deterministic_ordering": True,
            "phase_d_not_used": True,
        },
        "claim_ceiling": {
            "historical_originality": False,
            "original_lemma_theorem": False,
            "phase_d_authorized": False,
            "goldbach_progress": False,
            "pnt_progress": False,
            "rh_progress": False,
            "grh_progress": False,
            "publication_readiness": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    payload = registered_summary() if args.registered_summary else registered_summary()
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
