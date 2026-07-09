# Latest State

```text
Version:  v0.6 Montgomery MNT-II (source-grounding-corrected; E CLOSED)
Home:     D:\PVG-ANT-Central-Mind (standalone git repo)
HEAD ref: latest baseline = Montgomery Book Coverage Audit 007
          (audits/montgomery-book-coverage-audit-007.md), after the v0.6-E Closure PASS (9d059f2,
          third attempt) on top of Correction 006 (fa279a3) -> Repair 006-B (afd5b6c) -> Repair 006-C
          (959e417). Coverage map: trusted Ch 19-22 (C/D/E) · unmined candidates Ch 17 (strongest),
          Ch 18, Ch 16 · appendices E-H support-only · zero-density/large-values = later volume.

Books (registries/books.jsonl is the source of truth):
  Mined, treasure overlay closed (AUDIT-CM-TREASURE-RETROFIT-CLOSURE-001), mastery deferred:
    - Overholt   (ANT operational; reference model)
    - Tenenbaum  (probabilistic / observable)
    - Mileti     (logic / certificate; v0.2-A/B closed)
    - Iwaniec-Kowalski (zero-density / large values; v0.4 closed)
    - Harman     (sieve information / Type-I-II; v0.5 closed)
  Partial overlay (source-grounding-corrected):
    - Montgomery MNT-II (v0.6) — Level 2, sieves-and-gaps pillar (Ch 19-22):
        TRUSTED source-grounded units (all three closure-reviewed):
          C (Ch 19-20 large sieve / Bombieri-Vinogradov, v0.6-c-closure PASS),
          D (Ch 21 Selberg / combinatorial sieve, v0.6-d-closure PASS),
          E (Ch 22 bounded gaps / GPY / Maynard, v0.6-e-closure PASS, third attempt;
            entered as validated_intake).
        QUARANTINED (source-mismatch / cross-volume, NOT trusted):
          A, B (zero-density / large-values / pair-correlation are deferred by the source
            to a LATER volume; prior A/B closure audits were safety/coherence checks only,
            SUPERSEDED by Correction 006, do NOT certify source-grounded extraction),
          legacy off-diagonal E (Kloosterman) in units/_quarantine/.
        NOT book_overlay_closed; the rest of the book is unmined.
  Available, not imported: Motohashi, Opera de Cribro, Hodel, Mendelson, Buss, Kossak, Stewart, Fesenko.

Governing protocol:
  Book import = treasure mining + normalization + integration + missed-treasures + guards + closure
  (governance/book-treasure-extraction-protocol.md). From Course Correction 005:
    ChatGPT   = mathematical treasure analyst / PVG-ANT interpreter (supplies Treasure Packets).
    Local agent = repository engineer / registry maintainer / guard runner / coherence auditor.
  No new mathematical unit without a ChatGPT Treasure Packet.

Guards (7): honesty · registry_sync · no_pdf · forbidden_promotion · duplicate_concept · citation · state_coherence.

Standing missing certificates (all UNSOLVED): MC-001 (parity) · MC-002 (psi(x)-x / RH) ·
  MC-003 (Weil positivity) · MC-004 (Artin holomorphy) · MC-005 (AP / GRH-level).
Walls: all uncrossed. Frontier FRONTIER-ANT-PVG-007 (spectral) = FROZEN (cited, not reopened).

Ceiling: zero RH progress · zero GRH progress · no secured path.
```

**Honest classification:** Diagnostic (state snapshot). No RH/GRH progress.
