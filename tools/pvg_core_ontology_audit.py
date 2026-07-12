from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registries" / "pvg-core-ontology-v1"
OBJECTS = REGISTRY / "objects.jsonl"
MORPHISMS = REGISTRY / "morphisms.jsonl"
GRAMMAR = ROOT / "maps" / "pvg-core-grammar-v1.md"
EXPECTED = ROOT / "maps" / "pvg-core-ontology-example-expected.json"
GENERATED = ROOT / "maps" / "pvg-core-ontology-example-results.json"
PROGRAM = ROOT / "governance" / "programs" / "PVG-UNDERSTANDING-DEEPENING-001.md"

OBJECT_FIELDS = {
    "id",
    "name",
    "definition",
    "data_level",
    "reconstructs_n",
    "ant_interfaces",
    "loss_warning",
}
MORPHISM_FIELDS = {
    "id",
    "name",
    "source",
    "target",
    "formula",
    "injective",
    "recovery",
    "loss_level",
    "ant_interface",
}
ALLOWED_LOSSES = {"LOSS-0", "LOSS-1", "LOSS-2", "LOSS-3", "LOSS-4"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"Invalid JSONL at {path}:{line_no}: {error}") from error
        require(isinstance(row, dict), f"Expected object at {path}:{line_no}")
        rows.append(row)
    return rows


def main() -> None:
    objects = read_jsonl(OBJECTS)
    morphisms = read_jsonl(MORPHISMS)

    require(len(objects) >= 18, f"Expected at least 18 objects, found {len(objects)}")
    require(len(morphisms) >= 20, f"Expected at least 20 morphisms, found {len(morphisms)}")

    object_ids = [str(row.get("id", "")) for row in objects]
    morphism_ids = [str(row.get("id", "")) for row in morphisms]
    duplicate_objects = sorted(key for key, count in Counter(object_ids).items() if count > 1)
    duplicate_morphisms = sorted(key for key, count in Counter(morphism_ids).items() if count > 1)
    require(not duplicate_objects, f"Duplicate object IDs: {duplicate_objects}")
    require(not duplicate_morphisms, f"Duplicate morphism IDs: {duplicate_morphisms}")

    for row in objects:
        missing = sorted(OBJECT_FIELDS - set(row))
        require(not missing, f"Object {row.get('id')} missing fields: {missing}")
        require(str(row["id"]).startswith("PVG-OBJ-"), f"Bad object ID: {row['id']}")
        require(isinstance(row["ant_interfaces"], list) and row["ant_interfaces"], f"Object {row['id']} needs ANT interfaces")
        require(len(str(row["definition"])) >= 12, f"Object {row['id']} definition too short")
        require(len(str(row["loss_warning"])) >= 12, f"Object {row['id']} loss warning too short")

    known_object_ids = set(object_ids)
    referenced_object_ids: set[str] = set()
    for row in morphisms:
        missing = sorted(MORPHISM_FIELDS - set(row))
        require(not missing, f"Morphism {row.get('id')} missing fields: {missing}")
        require(str(row["id"]).startswith("PVG-MORPH-"), f"Bad morphism ID: {row['id']}")
        require(str(row["loss_level"]) in ALLOWED_LOSSES, f"Bad loss level for {row['id']}")
        require(len(str(row["recovery"])) >= 12, f"Morphism {row['id']} recovery rule too short")
        require(len(str(row["ant_interface"])) >= 5, f"Morphism {row['id']} ANT interface too short")
        for token in str(row["source"]).split():
            if token.startswith("PVG-OBJ-"):
                referenced_object_ids.add(token)
        if str(row["target"]).startswith("PVG-OBJ-"):
            referenced_object_ids.add(str(row["target"]))

    unknown_refs = sorted(referenced_object_ids - known_object_ids)
    require(not unknown_refs, f"Unknown object references in morphisms: {unknown_refs}")

    exact_objects = [row for row in objects if row["reconstructs_n"] is True]
    require(len(exact_objects) >= 4, "Expected several exact reconstruction objects")
    require(any(row["loss_level"] == "LOSS-3" for row in morphisms), "Phase-loss morphism missing")
    require(any(row["loss_level"] == "LOSS-4" for row in morphisms), "Analytic-certificate morphism missing")
    require(any(row["injective"] == "false" for row in morphisms), "Noninjective morphism witnesses missing")

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    require(generated == expected, "Generated ontology examples differ from expected certificate")
    require(all(value is True for key, value in generated["examples"].items() if key != "aggregate_noninjective"), "A deterministic ontology witness failed")
    require(generated["examples"]["aggregate_noninjective"]["distinct"] is True, "Aggregate noninjectivity witness failed")
    require(all(value is False for value in generated["claims"].values()), "Forbidden promotion found in ontology certificate")

    grammar = GRAMMAR.read_text(encoding="utf-8")
    for token in [
        "Six data layers",
        "Reconstruction lattice",
        "Non-reconstruction laws",
        "Materiality gate",
        "no RH/GRH progress",
    ]:
        require(token in grammar, f"Grammar token missing: {token}")

    program = PROGRAM.read_text(encoding="utf-8")
    for token in ["no second theorem target", "no Dataset 004", "no L3 promotion"]:
        require(token in program, f"Program ceiling token missing: {token}")

    print(
        "pvg_core_ontology_audit: PASS — "
        f"{len(objects)} objects, {len(morphisms)} morphisms, reconstruction/loss witnesses verified"
    )


if __name__ == "__main__":
    main()
