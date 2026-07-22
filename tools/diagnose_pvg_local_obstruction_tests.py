from __future__ import annotations

import traceback

from tests import test_pvg_local_obstruction_geometry as suite


def main() -> None:
    tests = [
        (name, getattr(suite, name))
        for name in sorted(dir(suite))
        if name.startswith("test_") and callable(getattr(suite, name))
    ]
    for name, fn in tests:
        try:
            fn()
        except Exception:
            print(f"FAIL: {name}")
            traceback.print_exc()
            raise
        else:
            print(f"PASS: {name}")
    print(f"PASS: all {len(tests)} focused PASS-004 tests")


if __name__ == "__main__":
    main()
