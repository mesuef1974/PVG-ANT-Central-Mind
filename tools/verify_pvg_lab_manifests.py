#!/usr/bin/env python3
"""Verify SHA-256 MANIFEST integrity for the versioned PVG structural laboratory apps.

Governance: versioned lightweight HTML research applications are stored in-repo only under
pvg_ant_structural_laboratory_v*/ and MUST each carry a MANIFEST.json whose recorded size and
SHA-256 match the on-disk files exactly, with no missing and no unauthorized extra files, and a
version consistent with package.json. This guard fails on any drift.

Usage: python tools/verify_pvg_lab_manifests.py
Exit code 0 = all manifests verified; 1 = any failure.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LAB_GLOB = "pvg_ant_structural_laboratory_v*"
IGNORE = {"MANIFEST.json"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def on_disk_files(lab: Path) -> set[str]:
    out: set[str] = set()
    for p in lab.rglob("*"):
        if p.is_dir():
            continue
        rel = p.relative_to(lab).as_posix()
        if rel in IGNORE or rel.startswith("."):
            continue
        out.add(rel)
    return out


def verify_lab(lab: Path) -> list[str]:
    errors: list[str] = []
    man_path = lab / "MANIFEST.json"
    if not man_path.exists():
        return [f"{lab.name}: MANIFEST.json missing"]
    try:
        man = json.loads(man_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{lab.name}: MANIFEST.json invalid JSON ({exc})"]

    listed = {f["path"]: f for f in man.get("files", [])}
    disk = on_disk_files(lab)

    for rel in sorted(set(listed) - disk):
        errors.append(f"{lab.name}: listed file missing on disk: {rel}")
    for rel in sorted(disk - set(listed)):
        errors.append(f"{lab.name}: unauthorized extra file (not in manifest): {rel}")

    for rel in sorted(set(listed) & disk):
        entry, p = listed[rel], lab / rel
        size = p.stat().st_size
        if size != entry.get("size_bytes"):
            errors.append(f"{lab.name}: size mismatch {rel}: disk {size} != manifest {entry.get('size_bytes')}")
        digest = sha256(p)
        if digest != entry.get("sha256"):
            errors.append(f"{lab.name}: sha256 mismatch {rel}")

    # version consistency: MANIFEST.version vs package.json.version
    man_ver = str(man.get("version", ""))
    pkg_path = lab / "package.json"
    if pkg_path.exists():
        try:
            pkg_ver = str(json.loads(pkg_path.read_text(encoding="utf-8")).get("version", ""))
            if man_ver and pkg_ver and man_ver != pkg_ver:
                errors.append(f"{lab.name}: version mismatch MANIFEST {man_ver} != package.json {pkg_ver}")
        except json.JSONDecodeError:
            errors.append(f"{lab.name}: package.json invalid JSON")
    # version should match the directory suffix (v6_1 -> 6.1.x)
    m = re.search(r"_v(\d+)_(\d+)$", lab.name)
    if m and man_ver and not man_ver.startswith(f"{m.group(1)}.{m.group(2)}"):
        errors.append(f"{lab.name}: MANIFEST version {man_ver} inconsistent with directory {lab.name}")
    return errors


def main() -> int:
    labs = sorted(REPO.glob(LAB_GLOB))
    labs = [d for d in labs if d.is_dir()]
    if not labs:
        print("no PVG structural laboratory directories found")
        return 0
    all_errors: list[str] = []
    for lab in labs:
        errs = verify_lab(lab)
        if errs:
            all_errors.extend(errs)
        else:
            n = len(json.loads((lab / "MANIFEST.json").read_text(encoding="utf-8")).get("files", []))
            print(f"OK  {lab.name}: {n} files verified (size + sha256), no missing, no extra")
    if all_errors:
        print("\nFAIL — manifest verification errors:")
        for e in all_errors:
            print("  -", e)
        return 1
    print("\nALL LAB MANIFESTS VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
