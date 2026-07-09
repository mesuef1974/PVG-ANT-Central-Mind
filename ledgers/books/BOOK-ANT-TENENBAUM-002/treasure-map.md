# Tenenbaum — Treasure Map

Book ID: `BOOK-ANT-TENENBAUM-002`. **Book Treasure Retrofit Pass 001** — طبقةٌ فوق الوحدات المُغلَقة (003 · 004 · 005-A · 005-B) لا تمسّها. تحكمها `governance/book-treasure-extraction-protocol.md` (Tenenbaum = المعيارُ الجزئيّ للكتاب الكبير: عمقٌ حتى موضعٍ معلَنٍ + صدقُ ما وراءه). كلُّ كنزٍ مؤصَّلٌ على ملفّاتِ الدفتر الفعليّة؛ حزمةُ الحالة الخارجيّة للمطابقة لا للّصق. لا نصٌّ خام، لا ادّعاءُ إتقانٍ كامل.

```text
Treasure ID: TREASURE-TENENBAUM-001
Treasure:    Arithmetic functions as observables
Source:      Tenenbaum-003-Z (Anatomy of an Arithmetic Observable) — transformed notes only
Type:        object / observable framework
Why it matters: shifts the question from "what is f(n)?" to "what kind of observable is f?" — every function passes a 10-axis diagnostic before any claim.
ANT role:    structure / geometry / average / normal order / limiting law / tail / moments / maximal order / wall / certificate.
PVG translation: an arithmetic function is a measurement on the prime-valuation vector of n.
Wall / certificate: none directly; walls appear when cancellation or distribution is demanded.
Classification: Known / Diagnostic.
Normalized output: → Rule RULE-OBSERVABLE-ANATOMY-001 ; → Card arithmetic-observable-diagnostic-card.md.
```

```text
Treasure ID: TREASURE-TENENBAUM-002
Treasure:    Density as population geometry
Source:      Tenenbaum density layer (003–004) — transformed notes only
Type:        diagnostic distinction
Why it matters: prevents confusing "almost all" with "all"; density is a size, not a certainty.
ANT role:    natural / logarithmic density; supports normal-order and typical-behavior analysis.
PVG translation: density = the size of a region inside the prime-valuation population.
Wall / certificate: average/density does not imply pointwise behavior — WALL-AVERAGE-NORMAL.
Classification: Known / Diagnostic.
Normalized output: → Rule RULE-AVERAGE-NORMAL-001 ; feeds TREASURE-TENENBAUM-003.
```

```text
Treasure ID: TREASURE-TENENBAUM-003
Treasure:    Zero-Density-Not-Zero-Impact
Source:      Tenenbaum density / probabilistic-number-theory layer — transformed notes only
Type:        governance operating rule
Why it matters: a rare (zero-density) set can still dominate averages of an unbounded observable; protects against false dismissal of exceptional sets.
ANT role:    central to probabilistic number theory and mean-value diagnostics when f is unbounded.
PVG translation: thin regions of the valuation cone may still carry high-magnitude observable mass.
Wall / certificate: relates to error terms driven by exceptional sets (MC-002 / MC-005 context); a caution, not a certificate.
Classification: Governance / Diagnostic.
Normalized output: → Rule RULE-ZERO-DENSITY-IMPACT-001 (NEW; legacy alias "PVG Operating Rule 105").
```

```text
Treasure ID: TREASURE-TENENBAUM-004
Treasure:    Limiting-distribution orientation (Erdős–Kac, Turán–Kubilius)
Source:      Tenenbaum-004-I/J/K/L — transformed notes only
Type:        distribution-law layer
Why it matters: separates concentration (variance) from a limiting law (CLT); tells you when a function has a Gaussian/Poisson shell.
ANT role:    Turán–Kubilius variance bound; Erdős–Kac CLT for ω(n); moments as tail detectors.
PVG translation: distribution of the valuation-count observable across the population (Gaussian shell on the cone).
Wall / certificate: concentration ≠ cancellation; average ≠ normal order — WALL-AVERAGE-NORMAL.
Classification: Known / Diagnostic.
Normalized output: → Tool TOOL-TURAN-KUBILIUS-001, TOOL-ERDOS-KAC-001 ; → Observable OBS-OMEGA-001 (Ladder Level 5).
```

```text
Treasure ID: TREASURE-TENENBAUM-005
Treasure:    Multiplicative Function Decision Tree (+ Halász phase test)
Source:      Tenenbaum-004-A..F — transformed notes only
Type:        method-selection tool
Why it matters: prevents treating all multiplicative functions alike; forces a phase test before any "randomness / cancellation" claim.
ANT role:    routes f to Wirsing (f≥0) / Halász (|f|≤1, distance to n^{it}) / Selberg–Delange (F=ζ^z G) / Delange criterion.
PVG translation: multiplicative behavior factorizes across valuation coordinates; phase misalignment = Halász distance.
Wall / certificate: phase must be tested before claiming cancellation — WALL-PHASE (RULE-PHASE-TEST-001).
Classification: Known / Tool / Diagnostic.
Normalized output: → Tool TOOL-HALASZ-001, TOOL-WIRSING-001, TOOL-DELANGE-001, TOOL-SELBERG-DELANGE-001 ; → Rule RULE-PHASE-TEST-001 ; → Card multiplicative-function-decision-tree.md.
```

```text
Treasure ID: TREASURE-TENENBAUM-006
Treasure:    Observable Ladder
Source:      Tenenbaum-004-N (observable-ladder.md) — transformed notes only
Type:        ranking diagnostic
Why it matters: ranks observables by required information level (identity → distribution → certificate-required), so you know what a target needs.
ANT role:    Level 0 definition … Level 7 certificate-required; locates whether a result needs algebra, average, normal order, zero-free, or deep distribution.
PVG translation: different measurements of valuation vectors demand different certificates.
Wall / certificate: varies by rung (Level 6 touches a wall; Level 7 = no strong claim without a certificate).
Classification: Diagnostic.
Normalized output: → Card observable-ladder.md ; → Rule RULE-OBSERVABLE-ANATOMY-001 ; anchors OBS-MOBIUS-001, OBS-OMEGA-001, OBS-DIVISOR-001, OBS-SQUAREFREE-001.
```

```text
Treasure ID: TREASURE-TENENBAUM-007
Treasure:    Master Diagnostic Sheet (004-Z)
Source:      Tenenbaum-004-Z (master-diagnostic-sheet.md) — transformed notes only
Type:        unified operational card
Why it matters: one sheet closes the 004 line — any arithmetic function is read through a single fixed template (no missing axis, no silent skip).
ANT role:    Type / PVG geometry / Dirichlet series / pole / average / normal / concentration / limiting law / tail / moments / maximal order / mean-value route / phase test / wall / certificate.
PVG translation: the fixed measurement protocol on a valuation observable.
Wall / certificate: average ≠ normal (WALL-AVERAGE-NORMAL); test phase before cancellation (WALL-PHASE); missing cert → MC-ID.
Classification: Known / Diagnostic.
Normalized output: → Card master-diagnostic-sheet.md ; → Rules RULE-OBSERVABLE-ANATOMY-001, RULE-PHASE-TEST-001, RULE-AVERAGE-NORMAL-001.
```

```text
Treasure ID: TREASURE-TENENBAUM-008
Treasure:    Dirichlet characters as residue-fiber observables
Source:      Tenenbaum-005-A — transformed notes only
Type:        observable / reinterpretation
Why it matters: bridges finite residue geometry and L-functions; characters organize information across residue classes without producing new results.
ANT role:    orthogonality 1_{n≡a(q)} = φ(q)^{-1} Σ_χ conj(χ(a)) χ(n); primes in AP = Siegel–Walfisz (Known).
PVG translation: characters are phase observables on residue fibers attached to integers.
Wall / certificate: AP beyond Siegel–Walfisz needs L(s,χ) zero info or GRH — MC-005 (unsolved).
Classification: Known / Reinterpretation.
Normalized output: → Observable OBS-RESIDUE-FIBER-001, OBS-CHARACTER-001 ; → Tool TOOL-CHARACTER-ORTHOGONALITY-001, TOOL-CHARACTER-SUM-PHASE-001 ; → Wall WALL-SIEGEL, WALL-POSITIVITY-WEIL.
```

```text
Treasure ID: TREASURE-TENENBAUM-009
Treasure:    Character sums as phase tools
Source:      Tenenbaum-005-A — transformed notes only
Type:        tool
Why it matters: reads Σ χ(n) a(n) as a residue-fiber phase; the operational handle on character-weighted cancellation.
ANT role:    character-weighted partial sums; phase reading of arithmetic information mod q.
PVG translation: phase measurement on the residue fiber.
Wall / certificate: large character sums do not prove zero-free / GRH — a diagnostic, not a certificate.
Classification: Known / Tool.
Normalized output: → Tool TOOL-CHARACTER-SUM-PHASE-001.
```

```text
Treasure ID: TREASURE-TENENBAUM-010
Treasure:    L(s,χ) as residue-fiber generating object
Source:      Tenenbaum-005-B — transformed notes only
Type:        generating object / tool
Why it matters: packages character-weighted arithmetic information into one analytic object (Euler product, continuation, zeros) — but organizes the question, does not solve it.
ANT role:    L(s,χ)=Σ χ(n) n^{-s}=Π_p (1−χ(p)p^{-s})^{-1}; partial sums via Perron.
PVG translation: analytic encoding of residue-fiber phase data.
Wall / certificate: zero control of L = GRH-level — MC-005 (unsolved); no free crossing.
Classification: Known / Tool / Reinterpretation.
Normalized output: → Tool TOOL-LFUNCTION-GENERATING-001, TOOL-EULER-PRODUCT-001, TOOL-PERRON-001 ; → Wall WALL-SIEGEL, WALL-POSITIVITY-WEIL.
```

```text
Treasure ID: TREASURE-TENENBAUM-011
Treasure:    MC-005 — AP / GRH-level distribution certificate (missing)
Source:      Tenenbaum-005-A/B — transformed notes only
Type:        missing certificate
Why it matters: names exactly what is NOT proven — prime distribution in AP stronger than Siegel–Walfisz needs L-zero information or GRH.
ANT role:    the certificate that would control ψ(x;q,a) at GRH strength.
PVG translation: residue → spectral crossing (not free).
Wall / certificate: WALL-SIEGEL + WALL-POSITIVITY-WEIL; certificate MC-005 UNSOLVED.
Classification: Missing Certificate.
Normalized output: → Missing Certificate MC-005 (governance/missing-certificates.md).
```

**Honest classification:** Diagnostic (treasure map, retrofit layer). No RH/GRH progress. No complete-mastery claim.
