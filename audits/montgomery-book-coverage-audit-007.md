# Montgomery MNT-II — Book Coverage Audit 007

**Audit ID:** AUDIT-CM-MONTGOMERY-COVERAGE-007
**Scope:** map the whole MNT-II table of contents against the repository's trusted/quarantined overlay.
**Kind:** coverage audit ONLY — no unit mined, no MNTII-006-F created, no new book, no theorem claim.
**Baseline:** `9d059f2` (v0.6-E closure PASS) + `081894e` (hygiene); tree clean; guards 7/7 at start.
**Source ToC (supplied by Sufyan; the source is the governor):** Preface/Notation · Ch 16 Exponential Sums I
(Van der Corput's Method) · Ch 17 Estimates for Sums over Primes · Ch 18 Additive Prime Number Theory ·
Ch 19 The Large Sieve · Ch 20 Primes in Arithmetic Progressions III · Ch 21 Sieves of Fixed Dimension and
Applications · Ch 22 Bounded Gaps between Primes · Appendices E Harmonic Analysis II · F Uniform Distribution ·
G Bounds for Bilinear Forms · H Linear Programming.

## Classification vocabulary

```text
covered_trusted       : source-grounded by a trusted closure-reviewed unit (C/D/E).
covered_quarantined   : only ever represented by quarantined material; NOT actually covered.
missing_candidate     : in-volume treasure exists; eligible for a FUTURE ChatGPT Treasure Packet.
deferred_cross_volume : the topic is deferred by the source to a LATER volume; not minable here.
support_appendix      : technical support for the content chapters; not mined as a standalone unit.
not_for_pvg_now       : metadata / navigation; no unit, no card.
```

## Coverage map

| ToC item | Classification | Evidence / notes |
|---|---|---|
| Preface / Notation | not_for_pvg_now | metadata; feeds citation hygiene only. |
| Ch 16 Exponential Sums I (Van der Corput) | **missing_candidate** (or support-to-17/18) | UNMINED. The quarantined legacy-E *mixed* Ch-16 material (Weyl / van der Corput) with later-volume Kloosterman/Weil framing — its quarantine does NOT count as coverage of Ch 16. A fresh packet would read Van der Corput's method as an in-volume cancellation tool feeding Ch 17/18; NOT a revival of legacy-E. |
| Ch 17 Estimates for Sums over Primes | **missing_candidate — strongest F candidate** | UNMINED. Vinogradov-style Type I / Type II decompositions of sums over primes: the canonical analytic source of the Type-II information that `FRONTIER-ANT-PVG-004` (sieve information, Harman overlay) treats as an EXTERNAL missing certificate (MC-001 context). Directly complements the trusted C/D/E sieves-and-gaps pillar. |
| Ch 18 Additive Prime Number Theory | **missing_candidate** (second) | UNMINED. Circle method / ternary Goldbach (three-primes = KNOWN theorem). Ceiling-sensitive: binary Goldbach is OPEN and must never be claimed; a packet here needs the strictest known-vs-open fencing. |
| Ch 19 The Large Sieve | **covered_trusted (C)** | `MNTII-006-C` (v0.6-c-closure PASS) → `TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001`; cards 016–022. |
| Ch 20 Primes in APs III (Bombieri–Vinogradov) | **covered_trusted (C)** | same unit; BV = average distribution input, NOT individual GRH; MC-005 unsolved. |
| Ch 21 Sieves of Fixed Dimension | **covered_trusted (D)** | `MNTII-006-D` (v0.6-d-closure PASS) → `TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001`; cards 023–029; parity uncrossed. |
| Ch 22 Bounded Gaps (GPY / Maynard) | **covered_trusted (E)** | `MNTII-006-E` (v0.6-e-closure PASS, third attempt) → `TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001`; cards 030–036; KNOWN theorem, not ours. |
| Appendix E Harmonic Analysis II | support_appendix | supports the large-sieve / exponential-sum machinery (Ch 16, 19). |
| Appendix F Uniform Distribution | support_appendix | Weyl equidistribution; supports Ch 16. |
| Appendix G Bounds for Bilinear Forms | support_appendix | supports Type-II bilinear estimates (Ch 17); watch: bilinear-forms language must not resurrect the quarantined off-diagonal framing without a packet. |
| Appendix H Linear Programming | support_appendix | supports the Maynard optimization step (Ch 22); already fenced in unit E as an optimization device, not a certificate. |

Zero-density / large values / Linnik / pair-correlation: **deferred_cross_volume** — no ToC row; this is
exactly the material the quarantined A/B pretended to cover (see Q2).

## Answers

```text
Q1. Source-grounded now: Ch 19-20 (C) · Ch 21 (D) · Ch 22 (E). Three trusted closure-reviewed units.
Q2. Wrongly represented by quarantined material:
      A, B  -> claimed mean-value / large-value / zero-density machinery: maps to NO chapter of THIS
               volume (deferred_cross_volume). They covered nothing here; cards 001-015 stay quarantined.
      legacy-E -> mixed Ch-16 Weyl/van-der-Corput material with later-volume Kloosterman/Weil/off-diagonal
               framing; its quarantine leaves Ch 16 genuinely UNMINED.
Q3. Next best Treasure Packet candidates (recommendation only; ChatGPT selects, Sufyan permits):
      1st: Ch 17 (sums over primes / Type I-II) — feeds FRONTIER-ANT-PVG-004, complements Harman + C/D/E.
      2nd: Ch 18 (additive / circle method) — new observable family; heaviest ceiling fencing needed.
      3rd: Ch 16 (Van der Corput) — either its own small unit or support-to-17/18 inside their packets.
Q4. Support-only, never standalone units (absent a later promoting packet): Appendices E, F, G, H;
      Preface/Notation is metadata.
Q5. Missed-treasures to record BEFORE any future unit (recorded in missed-treasures.md in this commit):
      Ch 16 Van der Corput method (unmined candidate) · Ch 17 prime-sum estimates (unmined candidate) ·
      Ch 18 additive prime number theory (unmined candidate; binary Goldbach OPEN, never claimed) ·
      Appendices E-H as support-only. Existing deferred items stand.
Q6. Should MNTII-006-F exist? ONLY IF ChatGPT supplies a source-grounded Treasure Packet for a specific
      chapter, with explicit permission. If it exists, its source must be Ch 17 (recommended), else
      Ch 18 or Ch 16. Until then F stays NOT ALLOWED. This audit creates nothing.
Q7. Overlay status: partial_overlay STANDS. 4 of 7 content chapters are trusted-covered (19-22);
      Ch 16-18 are unmined; appendices unprocessed as support. NOT book_overlay_closed — and it cannot
      approach overlay closure before Ch 16-18 are either mined or explicitly recorded as declined.
```

## Guard rules honored

```text
A/B/legacy-E remain QUARANTINED · E remains CLOSED/PASS · no F created · NOT book_overlay_closed ·
no theorem claim · no RH/GRH progress · no parity breakthrough · no PNT/AP improvement ·
transformed notes only · the source is the governor.
```

## Guard results (at commit)

```text
honesty_audit PASS · registry_sync_audit PASS · no_pdf_audit PASS · forbidden_promotion_audit PASS ·
duplicate_concept_audit PASS · citation_audit PASS · state_coherence_audit PASS (repo-wide sweep).
```

**Next after this audit:** ChatGPT selects the next Treasure Packet candidate from this coverage map;
nothing is mined without the packet and explicit permission.

**Honest classification:** Diagnostic (book coverage audit). No RH/GRH progress. No complete mastery.
