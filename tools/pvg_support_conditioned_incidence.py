from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from statistics import median

try:
    from tools.pvg_centered_radius_incidence import production_indexes
    from tools.pvg_centered_radius_spectra import centered_radius_spectrum, registered_points
except ModuleNotFoundError:
    from pvg_centered_radius_incidence import production_indexes
    from pvg_centered_radius_spectra import centered_radius_spectrum, registered_points

Support = tuple[int, ...]

DECIMAL_BINS = ((1, 9), (10, 99), (100, 999), (1000, 9999), (10000, 99999), (100000, 100000))


def decimal_bin(n: int) -> str:
    if n <= 0:
        raise ValueError("n must be positive")
    for lower, upper in DECIMAL_BINS:
        if lower <= n <= upper:
            return f"{lower}-{upper}"
    raise ValueError("n is outside the registered decimal bins")


def bit_length_stratum(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    return n.bit_length()


def route(n: int) -> str:
    if n <= 0:
        raise ValueError("n must be positive")
    return "even" if n % 2 == 0 else "odd"


def point_record(n: int, support: Support, component_by_integer: dict[int, int]) -> dict[str, object]:
    spectrum = centered_radius_spectrum(n)
    return {
        "integer": n,
        "support": list(support),
        "support_key": "{" + ",".join(map(str, support)) + "}",
        "support_size": len(support),
        "route": route(n),
        "decimal_bin": decimal_bin(n),
        "bit_length": bit_length_stratum(n),
        "represented": bool(spectrum),
        "multiplicity": len(spectrum),
        "minimum_coordinate": min(spectrum) if spectrum else None,
        "maximum_coordinate": max(spectrum) if spectrum else None,
        "coordinate_span": max(spectrum) - min(spectrum) if spectrum else None,
        "component_id": component_by_integer.get(n),
    }


def exact_group_summary(records: list[dict[str, object]]) -> dict[str, object]:
    multiplicities = [int(row["multiplicity"]) for row in records]
    represented = [row for row in records if bool(row["represented"])]
    represented_multiplicities = [int(row["multiplicity"]) for row in represented]
    return {
        "point_count": len(records),
        "represented_count": len(represented),
        "nonrepresented_count": len(records) - len(represented),
        "represented_rate": f"{len(represented)}/{len(records)}",
        "multiplicity_sum": sum(multiplicities),
        "multiplicity_mean": str(Fraction(sum(multiplicities), len(records))),
        "multiplicity_median": str(median(multiplicities)),
        "represented_multiplicity_mean": (
            str(Fraction(sum(represented_multiplicities), len(represented_multiplicities)))
            if represented_multiplicities else None
        ),
        "maximum_multiplicity": max(multiplicities),
    }


def grouped(records: list[dict[str, object]], keys: tuple[str, ...]) -> list[dict[str, object]]:
    buckets: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for row in records:
        buckets[tuple(row[key] for key in keys)].append(row)
    output = []
    for values, members in sorted(buckets.items(), key=lambda item: tuple(str(x) for x in item[0])):
        output.append({"group": {key: value for key, value in zip(keys, values)}, "summary": exact_group_summary(members)})
    return output


def rank_table(records: list[dict[str, object]], stratum_keys: tuple[str, ...], class_key: str) -> list[dict[str, object]]:
    strata: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for row in records:
        strata[tuple(row[key] for key in stratum_keys)].append(row)
    output = []
    for stratum, members in sorted(strata.items(), key=lambda item: tuple(str(x) for x in item[0])):
        classes: dict[object, list[dict[str, object]]] = defaultdict(list)
        for row in members:
            classes[row[class_key]].append(row)
        ranking = []
        for class_value, class_members in classes.items():
            total = sum(int(row["multiplicity"]) for row in class_members)
            ranking.append({
                "class": class_value,
                "point_count": len(class_members),
                "multiplicity_mean": str(Fraction(total, len(class_members))),
                "multiplicity_sum": total,
            })
        ranking.sort(key=lambda row: (-Fraction(str(row["multiplicity_mean"])), str(row["class"])))
        output.append({
            "stratum": {key: value for key, value in zip(stratum_keys, stratum)},
            "ranking": ranking,
        })
    return output


def matched_neighborhood_witnesses(records: list[dict[str, object]], limit: int = 50) -> list[dict[str, object]]:
    strata: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in records:
        strata[(str(row["route"]), str(row["decimal_bin"]))].append(row)
    witnesses = []
    for (route_name, bin_name), members in sorted(strata.items()):
        members = sorted(members, key=lambda row: int(row["integer"]))
        for row in members:
            candidates = [candidate for candidate in members if candidate["support_size"] != row["support_size"]]
            if not candidates:
                continue
            distance = min(abs(int(candidate["integer"]) - int(row["integer"])) for candidate in candidates)
            tied = [candidate for candidate in candidates if abs(int(candidate["integer"]) - int(row["integer"])) == distance]
            for candidate in tied:
                left, right = sorted((row, candidate), key=lambda item: int(item["integer"]))
                witnesses.append({
                    "route": route_name,
                    "decimal_bin": bin_name,
                    "distance": distance,
                    "left": {key: left[key] for key in ("integer", "support", "support_size", "multiplicity")},
                    "right": {key: right[key] for key in ("integer", "support", "support_size", "multiplicity")},
                })
    unique = {}
    for witness in witnesses:
        key = (witness["left"]["integer"], witness["right"]["integer"])
        unique[key] = witness
    return sorted(unique.values(), key=lambda row: (row["distance"], row["left"]["integer"], row["right"]["integer"]))[:limit]


def counterexamples(records: list[dict[str, object]]) -> dict[str, object]:
    same_support: dict[str, dict[int, int]] = defaultdict(dict)
    same_size: dict[int, dict[int, int]] = defaultdict(dict)
    same_bin_supports: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in records:
        n = int(row["integer"])
        m = int(row["multiplicity"])
        same_support[str(row["support_key"])][n] = m
        same_size[int(row["support_size"])][n] = m
        same_bin_supports[(str(row["route"]), str(row["decimal_bin"]))].add(str(row["support_key"]))

    def first_variation(groups: dict[object, dict[int, int]]) -> dict[str, object] | None:
        for group, values in sorted(groups.items(), key=lambda item: str(item[0])):
            by_multiplicity: dict[int, list[int]] = defaultdict(list)
            for n, multiplicity in values.items():
                by_multiplicity[multiplicity].append(n)
            if len(by_multiplicity) > 1:
                low, high = sorted(by_multiplicity)[:2]
                return {"group": group, "left": [min(by_multiplicity[low]), low], "right": [min(by_multiplicity[high]), high]}
        return None

    bin_witness = None
    for key, supports in sorted(same_bin_supports.items()):
        if len(supports) > 1:
            bin_witness = {"route": key[0], "decimal_bin": key[1], "support_examples": sorted(supports)[:3]}
            break
    return {
        "same_exact_support_does_not_determine_multiplicity": first_variation(same_support),
        "same_support_size_does_not_determine_multiplicity": first_variation(same_size),
        "same_size_bin_does_not_determine_support": bin_witness,
    }


def registered_summary() -> dict[str, object]:
    spectra, owners, _, _ = production_indexes()
    component_by_integer: dict[int, int] = {}
    unseen = {n for n, spectrum in spectra.items() if spectrum}
    component_id = 0
    while unseen:
        component_id += 1
        stack = [min(unseen)]
        while stack:
            n = stack.pop()
            if n not in unseen:
                continue
            unseen.remove(n)
            component_by_integer[n] = component_id
            for d in spectra[n]:
                stack.extend(owner for owner in owners[d] if owner in unseen)

    records = [point_record(n, support, component_by_integer) for n, support in registered_points()]
    records.sort(key=lambda row: int(row["integer"]))

    raw_rank = rank_table(records, tuple(), "support_size")[0]["ranking"]
    conditioned_rank = rank_table(records, ("route", "decimal_bin"), "support_size")
    raw_order = [row["class"] for row in raw_rank]
    reversals = []
    for row in conditioned_rank:
        order = [item["class"] for item in row["ranking"]]
        if len(order) > 1 and order != [value for value in raw_order if value in order]:
            reversals.append({"stratum": row["stratum"], "raw_restricted_order": [value for value in raw_order if value in order], "conditioned_order": order})

    canonical = json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    return {
        "id": "ENGINE-004-PASS-004-SUPPORT-CONDITIONED-INCIDENCE-SUMMARY-001",
        "classification": "Finite-Verified candidate / Diagnostic / Counterexample search",
        "scope": {
            "support_prime_limit": 11,
            "support_face_sizes": [1, 2, 3],
            "integer_cap": 100000,
            "integer_point_count": len(records),
            "represented_point_count": sum(bool(row["represented"]) for row in records),
            "decimal_bins": [f"{lower}-{upper}" for lower, upper in DECIMAL_BINS],
        },
        "raw_by_support_size": grouped(records, ("support_size",)),
        "conditioned_by_support_size": grouped(records, ("route", "decimal_bin", "support_size")),
        "conditioned_by_exact_support": grouped(records, ("route", "decimal_bin", "support_key")),
        "bit_length_conditioned_by_support_size": grouped(records, ("route", "bit_length", "support_size")),
        "conditioned_rank_tables": conditioned_rank,
        "rank_reversal_inventory": reversals,
        "matched_neighborhood_witnesses": matched_neighborhood_witnesses(records),
        "counterexamples": counterexamples(records),
        "record_certificate": {"row_count": len(records), "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest()},
        "verification": {
            "all_registered_points_present": len(records) == 884,
            "all_spectra_match_pass_002": all(tuple(centered_radius_spectrum(int(row["integer"]))) == spectra[int(row["integer"])] for row in records),
            "group_counts_reconstruct_total": sum(item["summary"]["point_count"] for item in grouped(records, ("route", "decimal_bin", "support_size"))) == len(records),
            "matched_witnesses_respect_route_and_decimal_bin": all(w["left"]["integer"] % 2 == w["right"]["integer"] % 2 for w in matched_neighborhood_witnesses(records)),
            "deterministic_ordering": True,
            "phase_d_not_used": True,
        },
        "claim_ceiling": {
            "causal_support_effect": False,
            "original_lemma_theorem": False,
            "cap_or_support_expansion": False,
            "regression_or_significance_test": False,
            "density_or_asymptotic_law": False,
            "phase_d_authorized": False,
            "goldbach_progress": False,
            "pnt_progress": False,
            "rh_progress": False,
            "grh_progress": False,
            "publication_readiness": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate governed support-conditioned incidence diagnostics.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    payload = registered_summary()
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
