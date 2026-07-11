from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CERTIFICATES = ROOT / "certificates"
COMMITTED = CERTIFICATES / "DATASET003_EXECUTION_CERTIFICATE.json"
GENERATED = DATA / "python_result_003.json"
METADATA = DATA / "pvg_lpd_dataset_003_metadata.json"
CROSS_LANGUAGE = CERTIFICATES / "DATASET003_CROSS_LANGUAGE_CERTIFICATE.json"
TOLERANCE = 1e-12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def close(left: float, right: float, label: str) -> None:
    difference = abs(float(left) - float(right))
    require(difference <= TOLERANCE, f"{label} differs by {difference}")


def main() -> None:
    for path in [COMMITTED, GENERATED, METADATA, CROSS_LANGUAGE]:
        require(path.exists(), f"Missing result-verification input: {path}")

    committed = json.loads(COMMITTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    cross_language = json.loads(CROSS_LANGUAGE.read_text(encoding="utf-8"))

    require(committed["protocol_id"] == generated["protocol_id"], "Protocol ID mismatch")
    require(committed["status"] == generated["decision"].replace(" ", "_").replace("—", "_").upper(), "Decision/status mismatch")
    require(committed["promoted"] is False, "Unexpected promotion flag")
    require(generated["decision"] == "UNRESOLVED IN INDEPENDENT REPLICATION", "Generated decision changed")

    require(committed["dataset"]["rows"] == metadata["rows"] == 480, "Row count mismatch")
    require(committed["dataset"]["columns"] == metadata["columns"] == 147, "Column count mismatch")
    require(committed["dataset"]["dataset_sha256"] == metadata["dataset_sha256"], "Dataset hash mismatch")
    require(committed["dataset"]["protocol_sha256"] == metadata["protocol_sha256"], "Protocol hash mismatch")

    close(committed["overall_delta"], generated["overall_delta"], "overall_delta")
    for family, value in committed["family_delta"].items():
        close(value, generated["family_delta"][family], f"family_delta[{family}]")
    for key in ["ci_lower", "median", "ci_upper", "probability_better"]:
        close(committed["bootstrap"][key], generated["bootstrap"][key], f"bootstrap[{key}]")

    generated_models = {row["model"]: row for row in generated["model_results"]}
    mapping = {
        "classical": "Classical Ridge",
        "primary": "Primary Lambda + characters + residue energy",
        "secondary": "Secondary lagged Lambda",
    }
    for committed_name, generated_name in mapping.items():
        committed_model = committed["model_results"][committed_name]
        generated_model = generated_models[generated_name]
        require(committed_model["features"] == generated_model["feature_count"], f"Feature count mismatch for {committed_name}")
        close(committed_model["alpha"], generated_model["alpha"], f"alpha[{committed_name}]")
        for metric in ["rmse", "mae", "r2"]:
            close(committed_model[metric], generated_model[metric], f"{metric}[{committed_name}]")

    require(cross_language["status"] == "PASS", "Cross-language certificate is not PASS")
    require(cross_language["decision"] == generated["decision"], "Cross-language decision mismatch")
    require(committed["promotion_gates"]["python_r_agreement"] is True, "Python/R gate not recorded")
    require(committed["promotion_gates"]["bootstrap_lower_positive"] is False, "Bootstrap gate changed")
    require(committed["promotion_gates"]["all_family_deltas_positive"] is False, "Family gate changed")

    print("Dataset 003 committed result verification: PASS")
    print("Decision:", generated["decision"])
    print("Dataset SHA-256:", metadata["dataset_sha256"])


if __name__ == "__main__":
    main()
