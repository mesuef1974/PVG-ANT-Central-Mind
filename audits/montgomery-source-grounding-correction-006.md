# Montgomery MNT-II — Source-Grounding Correction 006

**Audit ID:** AUDIT-CM-MONTGOMERY-SOURCE-GROUNDING-006
**Scope:** `ledgers/books/BOOK-ANT-MONTGOMERY-MNT-II-004/` and its registry / state files.
**Trigger:** ChatGPT Treasure Packet for MNTII-006-E + source confirmation of the volume's actual contents.
**Kind:** repository-truth correction (Coherence PASS class). **Not** a mathematical result.

## 1. Why this correction

The Montgomery MNT-II volume (*Multiplicative Number Theory II: Primes and Sieves*) is, by its
own table of contents, a **sieves-and-bounded-gaps** volume:

```text
Ch 19  the large sieve
Ch 20  the Bombieri–Vinogradov theorem (average distribution of primes)
Ch 21  fixed-dimension (Selberg / combinatorial) sieves
Ch 22  bounded gaps between primes (GPY / Maynard)
```

It **defers** zero-density estimates, large-value theory, Linnik's theorem, and pair-correlation
statistics to a **later volume**. Those topics are therefore **not source-grounded** in this book.

Units A and B were mined as "distribution diagnostics" and "distributional limits / barriers"
built on zero-density / large-values / pair-correlation. That framing is **cross-volume**: the
material is deferred by the source, so A and B were invented ahead of the source, not extracted
from it. The earlier off-diagonal / Kloosterman E (exponential-sum cancellation) is likewise a
later-volume topic, so it is **source-mismatched** too.

Only **C** (Ch 19–20 large sieve / Bombieri–Vinogradov) and **D** (Ch 21 Selberg / combinatorial
sieve) sit squarely inside this volume. The Treasure Packet supplies the correct E treasure:
**bounded gaps between primes as a Maynard / GPY sieve diagnostic (Ch 22).**

## 2. What was done (13 directive actions)

```text
 1. Created this audit report (AUDIT-CM-MONTGOMERY-SOURCE-GROUNDING-006).
 2. Quarantine banners added to units/MNTII-006-A.md and units/MNTII-006-B.md
    (source-mismatch / cross-volume / not trusted; prior A/B closure audits superseded).
 3. Old off-diagonal E moved via git mv to
    units/_quarantine/MNTII-006-E-legacy-offdiagonal-source-mismatch.md (Registry ID -> ...-E-LEGACY).
 4. New units/MNTII-006-E.md written from the Treasure Packet: bounded gaps / GPY / Maynard (Ch 22),
    Status = validated_intake, NOT closed, NOT PASS, pending v0.6-E Closure Review.
 5. registries/tools.jsonl: TOOL-MONTGOMERY-EXPSUM-DIAGNOSTIC-001 marked quarantined
    (source-mismatch); added TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 (Diagnostic, Frontier Support,
    source montgomery:006-E-intake).
 6. treasure-map.md: E cards 030-036 replaced with the bounded-gaps cards; quarantined-cards section added.
 7. normalization-ledger.md: E section replaced; normalized phrases (Treasure Packet) added;
    consolidated table updated (trusted C/D/E, quarantined A/B/legacy-E).
 8. integration-links.md and missed-treasures.md rewritten (trusted C/D/E; quarantined A/B/legacy-E;
    deferred Maynard proof / Polymath / EH / twin-prime / parity).
 9. README.md, registries/books.jsonl, transition-memory/latest-state.md and next-action.md updated:
    status partial_overlay + source-grounding-corrected; trusted_source_units = C, D, E-intake;
    quarantined_units = A, B, E-legacy; next_required_action = v0.6-E Closure Review; NOT book_overlay_closed.
10. tools/state_coherence_audit.py extended: fail if A/B counted trusted; fail if legacy-E counted trusted;
    fail if E-intake called closed/PASS (v0.6-e-closure.md present); fail if MNTII-006-F exists;
    fail if Montgomery marked book_overlay_closed.
11. Seven guards run (gated) — see section 4.
12. One commit: "Correct Montgomery MNT-II source grounding".
13. Stop. Next after this commit = v0.6-E Closure Review only. No F. No new book.
```

## 3. Resulting trusted / quarantined map

```text
TRUSTED (source-grounded, sieves-and-gaps pillar):
  C  Ch 19-20  large sieve / Bombieri–Vinogradov     -> TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001  (closed, v0.6-c PASS)
  D  Ch 21     Selberg / combinatorial sieve          -> TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001        (closed, v0.6-d PASS)
  E  Ch 22     bounded gaps / GPY / Maynard           -> TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 (validated_intake, NOT closed)

QUARANTINED (source-mismatch / cross-volume, NOT trusted):
  A            zero-density / large-values pressure    (deferred by source to a later volume)
  B            distributional limits / barriers        (deferred by source to a later volume)
  legacy E     off-diagonal / Kloosterman cancellation (deferred by source; units/_quarantine/)
```

## 4. Guard results

```text
  honesty_audit ............ PASS
  registry_sync_audit ...... PASS  (103 ids in sync)
  no_pdf_audit ............. PASS
  forbidden_promotion_audit  PASS
  duplicate_concept_audit .. PASS
  citation_audit ........... PASS
  state_coherence_audit .... PASS  (source-grounding invariants: A/B/legacy-E not trusted;
                                    E-intake not closed; no MNTII-006-F; not book_overlay_closed)
  ---------------------------------
  7 / 7 PASS
```

## 5. Ceiling (unchanged)

```text
Bounded gaps (GPY / Maynard) is a KNOWN classical theorem, recorded as known mathematics — NOT our result.
NOT the twin-prime conjecture; NOT a parity breakthrough; NOT a prime detector.
Bombieri–Vinogradov = average distribution input, NOT individual GRH. Elliott–Halberstam = conditional (unproven).
No new theorem; no RH/GRH progress; no secured path.
MC-001, MC-002, MC-005 stay UNSOLVED. WALL-PARITY / WALL-SIEVE-CEILING / WALL-OFF-DIAGONAL / WALL-DENSITY-HYP UNCROSSED.
FRONTIER-ANT-PVG-007 (spectral) stays FROZEN.
The source is the governor, not the local agent's imagination or mining speed.
```

**Honest classification:** Diagnostic (source-grounding correction audit). No RH/GRH progress. No complete mastery.
