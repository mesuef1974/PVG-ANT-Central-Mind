#!/usr/bin/env python3
"""Static policy hook for newly added RMG JSON/JSONL records.

This hook intentionally avoids rewriting historical records. It validates only
records supplied on stdin or paths passed on the command line.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterable

BARE_LEVEL = re.compile(r"^L[0-7](?:_|$)")
REQUIRED = {
    "ant_standard_definition",
    "ant_to_pvg_map",
    "pvg_geometric_object",
    "pvg_to_ant_return_map",
    "translation_type",
    "injectivity_status",
    "kernel_or_information_loss",
    "assimilation_level",
    "math_contribution_level",
    "operational_maturity",
    "certificate_strength",
    "claim_ceiling",
}
PVG_CLAIM_WORDS = ("pvg contribution", "pvg-derived", "new pvg theorem", "pvg mechanism")
PVG_REQUIRED = {
    "pvg_necessity_level",
    "removal_test_result",
    "what_breaks_without_pvg",
    "classical_reduction",
    "novelty_class",
    "prior_art_status",
}


def iter_records(path: Path) -> Iterable[dict]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".jsonl":
        for line_no, line in enumerate(text.splitlines(), 1):
            if line.strip():
                obj = json.loads(line)
                obj["__source_line__"] = line_no
                yield obj
    else:
        obj = json.loads(text)
        if isinstance(obj, list):
            yield from obj
        else:
            yield obj


def validate(record: dict) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED - record.keys())
    if missing:
        errors.append("missing canonical fields: " + ", ".join(missing))

    level = str(record.get("assimilation_level", ""))
    if BARE_LEVEL.match(level):
        errors.append(f"ambiguous bare assimilation level: {level}")
    if level and not level.startswith("ASSIM-"):
        errors.append(f"assimilation_level must use ASSIM-* namespace: {level}")

    math_level = str(record.get("math_contribution_level", ""))
    if math_level and not math_level.startswith("MATH-"):
        errors.append(f"math_contribution_level must use MATH-* namespace: {math_level}")

    text = " ".join(str(v).lower() for k, v in record.items() if not k.startswith("__"))
    if any(term in text for term in PVG_CLAIM_WORDS):
        missing_pvg = sorted(PVG_REQUIRED - record.keys())
        if missing_pvg:
            errors.append("PVG claim missing necessity fields: " + ", ".join(missing_pvg))

    evidence = str(record.get("certificate_strength", ""))
    if "REGRESSION" in evidence.upper() and math_level not in {"", "MATH-M0"}:
        errors.append("regression evidence cannot automatically imply mathematical contribution")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: enforce_rmg_new_record_policy.py FILE [FILE ...]", file=sys.stderr)
        return 2
    failed = False
    for raw in argv[1:]:
        path = Path(raw)
        try:
            records = list(iter_records(path))
        except Exception as exc:
            print(f"FAIL {path}: cannot parse: {exc}")
            failed = True
            continue
        for idx, record in enumerate(records, 1):
            errors = validate(record)
            if errors:
                failed = True
                print(f"FAIL {path} record {idx}: " + " | ".join(errors))
            else:
                print(f"PASS {path} record {idx}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
