# Montgomery MNT-II — Normalization Ledger

Book ID: `BOOK-ANT-MONTGOMERY-MNT-II-004`. **v0.6 unit MNTII-006-A.** كلُّ كنزٍ في `treasure-map.md` ← ماذا صار داخل العقل (معرِّفاتٌ حيّة). المخرجُ الأساسُ الجديد: `TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001` (live، مسجَّلٌ في `registries/tools.jsonl`).

```text
TREASURE-MNTII-001  Montgomery-style analytic tools as distribution diagnostics
  → Tool (NEW)        : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001
  → Frontier          : FRONTIER-ANT-PVG-006
  → Wall              : WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL
  → PVG–ANT           : off-diagonal / family-level support observable for frontier 006

TREASURE-MNTII-002  Distribution estimates as certificate pressure, not proof
  → Tool (NEW)        : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001 (pressure reading)
  → Missing Certificate: MC-002
  → PVG–ANT           : certificate pressure on the off-diagonal, not a certificate

TREASURE-MNTII-003  Mean / large-value control as family-level support
  → Tool (NEW)        : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001
  → Tool (neighbour)  : TOOL-LARGE-VALUE-DIAGNOSTIC-001
  → Wall              : WALL-OFF-DIAGONAL · WALL-DENSITY-HYP
  → PVG–ANT           : family-average control of the off-diagonal observable

TREASURE-MNTII-004  Zero-density context as partial support, not pointwise resolution
  → Tool (neighbour)  : TOOL-ZERO-DENSITY-DIAGNOSTIC-001
  → Missing Certificate: MC-002
  → Wall              : WALL-ZERO-FREE · WALL-DENSITY-HYP
  → PVG–ANT           : off-diagonal average ≠ pointwise truth

TREASURE-MNTII-005  Prime / sieve interface as diagnostic bridge
  → Frontier          : FRONTIER-ANT-PVG-006 (bridge to FRONTIER-ANT-PVG-004)
  → Wall              : WALL-PARITY (contextual)
  → PVG–ANT           : diagnostic bridge between analytic and sieve support geometries

TREASURE-MNTII-006  MC-002 remains unsolved
  → Missing Certificate: MC-002   (governance/missing-certificates.md) — UNSOLVED
  → Wall              : WALL-ZERO-FREE

TREASURE-MNTII-007  MC-005 remains unsolved
  → Missing Certificate: MC-005   (governance/missing-certificates.md) — UNSOLVED
  → Wall              : WALL-SIEGEL · WALL-POSITIVITY-WEIL

TREASURE-MNTII-008  Three walls uncrossed
  → Wall              : WALL-SIEGEL · WALL-POSITIVITY-WEIL · WALL-ZERO-FREE — UNCROSSED
  → PVG–ANT           : walls observed, not crossed
```

## Live IDs consolidated (this unit)

```text
Tool (NEW, live)  : TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001   (Diagnostic / Frontier Support)
Tools (neighbour) : TOOL-ZERO-DENSITY-DIAGNOSTIC-001 · TOOL-LARGE-VALUE-DIAGNOSTIC-001
Walls             : WALL-ZERO-FREE · WALL-SIEGEL · WALL-POSITIVITY-WEIL · WALL-DENSITY-HYP · WALL-OFF-DIAGONAL
Missing           : MC-002 · MC-005   (both UNSOLVED)
Frontier          : FRONTIER-ANT-PVG-006   (+ bridge FRONTIER-ANT-PVG-004)
```

**Consistency note:** `TOOL-MONTGOMERY-DISTRIBUTION-DIAGNOSTIC-001` was registered as the single planned target then promoted to live in `registries/tools.jsonl` on honest completion of MNTII-006-A; `planned.jsonl` is empty. All neighbour ids pre-exist. MC-002 & MC-005 UNSOLVED.

**Honest classification:** Diagnostic / Boundary (normalization ledger, v0.6 unit A). No RH/GRH progress.
