#!/usr/bin/env python3
"""Regenerate the AVRG retained-source manifest and SHA-256 inventory."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path("research/avrg-axis-sum")
CATEGORIES = ("reports", "code", "results", "figures", "protocols")
EXPECTED_COUNTS = {
    "reports": 34,
    "code": 46,
    "results": 52,
    "figures": 1,
    "protocols": 11,
}
EXPECTED_TOTAL = 144
GENERATED_AT = "2026-07-14T18:34:04Z"
PASS034_NOTE = (
    "PASS034 protocol, non-overlapping block code, and tests were committed "
    "before the exact e=14 scan and 5,000-permutation analysis; its locked "
    "negative result and Arabic report were added later."
)


def tracked_archive_paths() -> list[Path]:
    """Return only retained source artifacts, excluding archive index files."""
    command = ["git", "ls-files", *[str(ROOT / category) for category in CATEGORIES]]
    tracked = subprocess.check_output(command, text=True).splitlines()
    return sorted(
        Path(path).relative_to(ROOT)
        for path in tracked
        if Path(path).is_file()
    )


def main() -> None:
    paths = tracked_archive_paths()
    counts = {
        category: sum(path.parts[0] == category for path in paths)
        for category in CATEGORIES
    }
    if counts != EXPECTED_COUNTS or len(paths) != EXPECTED_TOTAL:
        raise SystemExit(
            f"Unexpected archive inventory: counts={counts}, total={len(paths)}"
        )

    entries = []
    checksum_lines = []
    for relative in paths:
        data = (ROOT / relative).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        entries.append(
            {
                "path": relative.as_posix(),
                "sha256": digest,
                "size_bytes": len(data),
            }
        )
        checksum_lines.append(f"{digest}  {relative.as_posix()}")

    old_manifest = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
    adjustments = list(old_manifest.get("archive_layout_adjustments", []))
    if PASS034_NOTE not in adjustments:
        adjustments.append(PASS034_NOTE)

    manifest = {
        "archive": "AVRG Axis-Sum Research Archive",
        "generated_at": GENERATED_AT,
        "scope": "PASS001 through PASS034",
        "retained_source_file_count": len(paths),
        "category_counts": counts,
        "scientific_ceiling": (
            "Finite computational diagnostics only; no asymptotic proof and no "
            "direct progress toward a proof of Goldbach."
        ),
        "published_page": old_manifest.get("published_page"),
        "archive_layout_adjustments": adjustments,
        "files": entries,
    }
    (ROOT / "MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (ROOT / "SHA256SUMS.txt").write_text(
        "\n".join(checksum_lines) + "\n",
        encoding="utf-8",
    )
    print(f"refreshed {len(paths)} AVRG retained source artifacts")
    print(counts)


if __name__ == "__main__":
    main()
