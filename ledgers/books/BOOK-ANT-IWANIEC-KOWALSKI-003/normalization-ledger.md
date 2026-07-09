# Iwaniec–Kowalski — Normalization Ledger

Book ID: `BOOK-ANT-IWANIEC-KOWALSKI-003`. **Book Treasure Retrofit Pass 001.** كلُّ كنزٍ في `treasure-map.md` ← ماذا صار داخل العقل (معرِّفاتٌ مسجَّلةٌ حقيقيّة). التطبيعُ إلى: Tool · Observable · Wall · Missing Certificate · Frontier · PVG–ANT Translation.

```text
TREASURE-IK-001  Zero-density estimates as diagnostic support
  → Tool              : TOOL-ZERO-DENSITY-DIAGNOSTIC-001
  → Wall              : WALL-DENSITY-HYP · WALL-ZERO-FREE (contextual)
  → Missing Certificate: MC-002
  → Frontier          : FRONTIER-ANT-PVG-006
  → PVG–ANT           : unconditional measure of "how far from RH"

TREASURE-IK-002  Large values as obstruction / pressure indicators
  → Tool              : TOOL-LARGE-VALUE-DIAGNOSTIC-001
  → Wall              : WALL-OFF-DIAGONAL · WALL-DENSITY-HYP
  → PVG–ANT           : off-diagonal pressure that bounds the zeros

TREASURE-IK-003  Mean values as family-level control
  → Tool              : TOOL-LARGE-VALUE-DIAGNOSTIC-001 (second-moment aspect)
  → PVG–ANT           : family-average control of the off-diagonal observable (not pointwise)

TREASURE-IK-004  L-functions as family-analytic objects
  → Frontier          : FRONTIER-ANT-PVG-006
  → Tool (consumed)   : TOOL-ZERO-DENSITY-DIAGNOSTIC-001 · TOOL-LARGE-VALUE-DIAGNOSTIC-001
  → Wall / cert       : WALL-POSITIVITY-WEIL · MC-005
  → PVG–ANT           : a family of residue-fiber generating objects measured together

TREASURE-IK-005  Character families as distributional test beds
  → Observable        : OBS-CHARACTER-001 · OBS-RESIDUE-FIBER-001
  → Missing Certificate: MC-005
  → Wall              : WALL-SIEGEL
  → PVG–ANT           : residue-fiber families as a distributional test bed (average = "as if GRH")

TREASURE-IK-006  Zero-density does not solve pointwise distribution alone
  → Missing Certificate: MC-002
  → Wall              : WALL-ZERO-FREE (contextual)
  → PVG–ANT           : off-diagonal average ≠ pointwise truth

TREASURE-IK-007  Large-value control does not imply GRH
  → Wall              : WALL-POSITIVITY-WEIL · WALL-SIEGEL
  → Missing Certificate: MC-002 · MC-005
  → PVG–ANT           : pressure bounds do not locate zeros

TREASURE-IK-008  Family average control ≠ individual AP certificate
  → Missing Certificate: MC-005
  → Wall              : WALL-SIEGEL
  → PVG–ANT           : family-average observable ≠ individual residue-fiber certificate

TREASURE-IK-009  MC-002 remains unsolved
  → Missing Certificate: MC-002   (governance/missing-certificates.md) — UNSOLVED
  → Wall              : WALL-ZERO-FREE

TREASURE-IK-010  MC-005 remains unsolved
  → Missing Certificate: MC-005   (governance/missing-certificates.md) — UNSOLVED
  → Wall              : WALL-SIEGEL · WALL-POSITIVITY-WEIL

TREASURE-IK-011  WALL-SIEGEL remains uncrossed
  → Wall              : WALL-SIEGEL — UNCROSSED
  → PVG–ANT           : exceptional-zero fiber anomaly, observed not crossed

TREASURE-IK-012  WALL-POSITIVITY-WEIL remains uncrossed
  → Wall              : WALL-POSITIVITY-WEIL — UNCROSSED
  → PVG–ANT           : residue→spectral crossing not made
```

## Live IDs consolidated (this book)

```text
Tools     : TOOL-ZERO-DENSITY-DIAGNOSTIC-001 · TOOL-LARGE-VALUE-DIAGNOSTIC-001
Walls     : WALL-SIEGEL · WALL-POSITIVITY-WEIL · WALL-ZERO-FREE (contextual) · WALL-DENSITY-HYP · WALL-OFF-DIAGONAL
Missing   : MC-002 · MC-005   (both UNSOLVED)
Frontier  : FRONTIER-ANT-PVG-006
Observable: OBS-CHARACTER-001 · OBS-RESIDUE-FIBER-001
```

**Consistency note:** every tracked-prefix id exists in `registries/*.jsonl` (`registry_sync` gate); no new id introduced by this retrofit. `WALL-ZERO-FREE` is linked as a contextual wall (present in v0.4 units + checkpoint-003) with no crossing claim. MC-002 & MC-005 UNSOLVED per v0.4 closure (AUDIT-CM-V04-CLOSURE-001, PASS 8/8).

**Honest classification:** Diagnostic / Boundary (normalization ledger, retrofit layer). No RH/GRH progress.
