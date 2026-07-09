# Montgomery MNT-II Frontier Support Layer — Book ANT (v0.6, source-grounding-corrected: trusted C/D/E, quarantined A/B + legacy E)

## Source

```text
Hugh Montgomery (with R. Vaughan lineage), Multiplicative Number Theory II: Primes and Sieves.
Book ID: BOOK-ANT-MONTGOMERY-MNT-II-004.  Status: partial_overlay / source-grounding-corrected (trusted C/D/E-intake; quarantined A/B + legacy E).
Local source present outside git in Books_others/.
PDF is excluded from repository by .gitignore.
Ledger will contain transformed notes only, no book text.
```

## Role

**Sieves-and-gaps frontier-support layer** (source-grounded). The Montgomery MNT-II volume focuses on **sieves and bounded gaps** (Ch 19 large sieve · Ch 20 Bombieri–Vinogradov · Ch 21 fixed-dimension sieves · Ch 22 bounded gaps / GPY / Maynard) and **defers zero-density / large values / Linnik / pair-correlation to a later volume**. Trusted units feed `FRONTIER-ANT-PVG-004` (sieve information), with distribution as external input; `FRONTIER-ANT-PVG-007` (spectral) stays frozen.

## Status

**v0.6 — SOURCE-GROUNDING-CORRECTED (Correction 006).**

**Trusted source-grounded units** (sieves-and-gaps pillar): `units/MNTII-006-C.md` (large sieve / Bombieri–Vinogradov, Ch 19–20) → `TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001`; `units/MNTII-006-D.md` (Selberg / combinatorial sieve, Ch 21) → `TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001`; `units/MNTII-006-E.md` (**bounded gaps / GPY / Maynard, Ch 22 — validated_intake, NOT closed**, pending v0.6-E Closure Review) → `TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001`. Trusted treasure cards `TREASURE-MNTII-016..036` (C 016–022 · D 023–029 · E bounded gaps 030–036).

**Quarantined (source-mismatch / cross-volume, NOT trusted):** `units/MNTII-006-A.md`, `units/MNTII-006-B.md` (zero-density / large values / pair-correlation — deferred by the source to a later volume; prior A/B closure audits were safety/coherence checks only, SUPERSEDED by this correction, and do NOT certify source-grounded extraction; cards `TREASURE-MNTII-001..015`); and the legacy off-diagonal E (`units/_quarantine/MNTII-006-E-legacy-offdiagonal-source-mismatch.md` · `TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001`).

**partial_overlay, Level 2, source-grounding-corrected** — NOT book_overlay_closure, NOT mastery. The rest of the book is unmined (see `missed-treasures.md`). Bounded gaps is a KNOWN theorem — not our result, not twin primes, not a parity breakthrough; BV = average input; EH = conditional. Plan in `v0.6-scope.md` / `v0.6-scope-freeze.md`. **No MNTII-006-F; no new book; no v0.6-E closure before review.**

**Honest classification:** Diagnostic (book ledger, source-grounding-corrected; trusted C/D/E-intake, quarantined A/B + legacy E). No RH/GRH progress. No complete mastery.
