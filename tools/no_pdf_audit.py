#!/usr/bin/env python3
"""
No-PDF-in-git guard for PVG-ANT Central Mind.

  - No .pdf/.djvu/.epub anywhere in the tree except the gitignored Books_others/.
  - No such file is tracked by git.
  - Books_others/ is actually ignored.

Exit 0 = PASS, 1 = FAIL.  Usage: python tools/no_pdf_audit.py
"""
import os, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAD_EXT = (".pdf", ".djvu", ".epub")


def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")


def main():
    problems = []
    # (1) walk: no book files outside Books_others/
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "Books_others")]
        for name in files:
            if name.lower().endswith(BAD_EXT):
                problems.append(f"[pdf-in-tree] {rel(os.path.join(dirpath, name))}")

    # (2) git-tracked check
    try:
        out = subprocess.run(["git", "-C", ROOT, "ls-files"], capture_output=True, text=True, timeout=30)
        for f in out.stdout.splitlines():
            if f.lower().endswith(BAD_EXT):
                problems.append(f"[pdf-tracked] {f}")
        # (3) Books_others must be ignored
        ci = subprocess.run(["git", "-C", ROOT, "check-ignore", "Books_others"], capture_output=True, text=True, timeout=30)
        if ci.returncode != 0:
            problems.append("[gitignore] Books_others/ is NOT ignored (.gitignore insufficient)")
    except (FileNotFoundError, subprocess.SubprocessError):
        print("no_pdf_audit: git not available; ran filesystem check only.")

    if problems:
        print(f"FAIL - {len(problems)} issue(s):")
        for p in problems:
            print("  " + p)
        return 1
    print("PASS - no PDFs in repository tree or git index.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
