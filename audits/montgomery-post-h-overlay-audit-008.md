# Montgomery MNT-II — Post-H Coverage/Overlay Audit 008

**Audit ID:** AUDIT-CM-MONTGOMERY-OVERLAY-008
**Kind:** governance / coverage audit ONLY — no unit, no MNTII-006-I, no new math IDs, no changes to
the six closed units, ceiling unchanged (zero RH progress · zero GRH progress · no secured path).
**Reviewed at:** HEAD `4378061` (clean tree; guards 7/7 at the base gate).
**Deliverable:** a recommendation ONLY. **The status is NOT flipped in this round.**

## 1. Base gate (all held)

```text
HEAD = 4378061 · tree clean · guards 7/7 PASS ·
closed units = exactly MNTII-006-C/D/E/F/G/H (six Status:CLOSED lines, six PASS closure audits) ·
book = partial_overlay / NOT book_overlay_closed · trusted = C,D,E,F,G,H · quarantined = A,B,E-legacy ·
60 unique treasure cards · 9 Montgomery tools (6 live + 3 stamped quarantined_source_mismatch).
```

## 2. Coverage matrix (mandatory 7-category classification)

| ToC item | Source scope | Unit | Unit status | Tool | Cards | Walls in play | Deliberate deferrals (documented) | Category |
|---|---|---|---|---|---|---|---|---|
| Preface / Notation | metadata | — | — | — | — | — | — | **6** non-load-bearing |
| Ch 16 Exponential Sums I (VdC) | §16.1–16.5 | G | CLOSED v0.6-g PASS | VDC-EXPONENTIAL-SUMS | 044–051 | OFF-DIAG·SIEVE-CEIL·PARITY·DENS | derivative-test proofs; exponent-pair optimization; ζ-applications beyond support | **1** covered+closed |
| Ch 17 Sums over Primes | §17.1–17.6 | F | CLOSED v0.6-f PASS | PRIME-SUMS-TYPE-II | 037–043 | OFF-DIAG·PARITY·SIEVE-CEIL·DENS | full Ch-17 proofs; exponent optimization; digit-sum completeness | **1** |
| Ch 18 Additive PNT | §18.1–18.8 | H | CLOSED v0.6-h PASS | ADDITIVE-PRIME-CIRCLE-METHOD | 052–060 | five walls incl. ZERO-FREE | circle-method proofs; §18.3 conditional framework; §18.4 Omega-result; k-tuples; short intervals; **binary Goldbach = OPEN (never claimed — an open problem, not a coverage gap)** | **1** |
| Ch 19 Large Sieve | chapter | C | CLOSED v0.6-c PASS | LARGE-SIEVE | 016–022 | OFF-DIAG·DENS·SIEGEL(ctx) | EH = open conjecture; chapter-by-chapter pass deferred (umbrella) | **1** |
| Ch 20 Primes in APs III (BV) | chapter | C | CLOSED v0.6-c PASS | LARGE-SIEVE | 016–022 | SIEGEL·POSITIVITY(ctx) | individual-modulus case = MC-005 (unsolved) | **1** |
| Ch 21 Fixed-dimension sieves | chapter | D | CLOSED v0.6-d PASS | SIEVE | 023–029 | PARITY·SIEVE-CEIL | — (bounds/almost-primes fenced) | **1** |
| Ch 22 Bounded Gaps | §22.1–22.4 | E | CLOSED v0.6-e PASS | BOUNDED-GAPS | 030–036 | PARITY·SIEVE-CEIL·OFF-DIAG·DENS | Maynard proof reproduction; Polymath; EH-variants; twin primes NOT available | **1** |
| Appendix E Harmonic Analysis II | support | — | — | — | — | — | support_appendix per Coverage Audit 007 | **2/7** deferred; promotion needs packet+permission |
| Appendix F Uniform Distribution | support | — | — | — | — | — | same | **2/7** |
| Appendix G Bilinear Forms | support | — | — | — | — | — | same (Type-II support context) | **2/7** |
| Appendix H Linear Programming | support | — | — | — | — | — | same (Maynard-optimization context) | **2/7** |
| zero-density / large values / Linnik / pair-correlation | deferred by the SOURCE to a later volume | — | — | — | — | — | cross-volume by the source's own preface | **3** out of declared scope |
| A / B / legacy-E artifacts | — | quarantined | QUARANTINED | 3 stamped tools | 001–015 (per-card QUARANTINED) | — | re-trust needs a source-grounded packet | **4** quarantined |
| notes/references sections (16.4–5, 17.5–6, 18.7–8, 22.4) | — | inside units | — | — | — | — | cited context | **6** |

**Category-5 (Actually missing): ZERO items.** The coverage auditor's hunt and the falsifier's
section-level sweep both found no load-bearing in-volume topic without a unit or a documented deferral.

## 3. book_overlay_closed conditions (§5 of the directive) — all verified

```text
[x] every in-scope content chapter (16-22) represented by a CLOSED unit; deferrals documented+legitimate
[x] zero 'Actually missing' gaps of analytic substance
[x] no contradiction among coverage maps, counters, central state (state/counter lens: exact counts hold)
[x] no live phrase calls an executed chapter unmined/unauthorized
[x] every missed-treasures item finally classified and auditable
[x] quarantined items NOT merged into the book's achievements (isolation verified at every layer)
[x] overlay closure implies NO RH/GRH movement and closes NO wall (policy vocabulary confines it)
[x] binary Goldbach stays OPEN; almost-all stays average; conditional stays conditional
[x] MNTII-006-I neither assumed nor created
```

## 4. Adversarial lenses (4 independent)

```text
Coverage auditor ......... PASS — RECOMMEND book_overlay_closed (0 blocking, 3 minors)
State & counter auditor .. PASS — RECOMMEND book_overlay_closed (0 blocking; all counts exact)
Source-grounding auditor . PASS — RECOMMEND book_overlay_closed (0 blocking; ceiling truth verified)
Falsifier ................ refuted = FALSE — RECOMMEND book_overlay_closed
    (eight attack vectors failed: no section gap, no deferral-as-coverage, no card inflation,
     no counter mismatch, no quarantine leak, no gap hidden behind 'historical/deferred/out-of-scope',
     no binary-Goldbach convertibility, no wall/RH reading of overlay closure;
     reverse-risk check: KEEP partial_overlay is NOT forced by any live gap)
```

## 5. Guard adversarial tests (§7 of the directive) — 6/6 FAIL correctly on temp copies

```text
1. closed count six -> five (Arabic) ................. FAIL ('خمس' contradicts actual count 6)
2. G described 'not mined' in a live layer ........... FAIL (executed-unit stale-denial)
3. units/MNTII-006-I.md created ...................... FAIL (no-I check + stale-'No I' check, 3 issues)
4. quarantined A moved into trusted_source_units ..... FAIL (A among trusted source units)
5. books.jsonl status -> book_overlay_closed ......... FAIL (structured status check, 2 issues)
6. live prose 'Montgomery book_overlay_closed' ....... FAIL (prose check — after a hardening found
       during THIS audit: the neighbourhood 'legacy' exemption shielded the injection, so the prose
       check was tightened to a same-line historical marker, mirroring the 006-F lesson; the
       hardening is included in this audit commit)
All states restored; full guards 7/7 PASS after testing.
```

## 6. Legitimate deferrals register (final classification, auditable)

Documented in `missed-treasures.md`: Maynard proof reproduction · Maynard-weight optimization ·
Polymath refinements · EH-conditional variants (EH = open conjecture) · twin primes NOT available ·
parity certificates NOT available (MC-001) · off-diagonal/Kloosterman = quarantined/postponed ·
chapter-by-chapter full pass (umbrella) · Ch-17 proofs/exponents/digit-sums · derivative-test proofs ·
exponent-pair optimization · ζ-exponent-pair applications · circle-method proofs · §18.3 conditional
framework · §18.4 Omega-result · k-tuples framework · short-interval conjectures · binary Goldbach
(OPEN, never claimed) · almost-all→all strengthening NOT available · new minor-arc bound NOT produced ·
MNTII-006-I NOT ALLOWED without packet+permission.

## 7. Quarantine status

A, B (cross-volume zero-density/large-values/pair-correlation) and legacy off-diagonal E
(Kloosterman/Weil) remain quarantined at every truth layer — unit banners, three stamped tools,
per-card QUARANTINED status on 001–015, ledgers, registries, maps, state files. No leak into any
achievement narrative. Re-trust requires a source-grounded Treasure Packet and explicit permission.

## 8. Flip-preconditions (IF the recommendation is accepted — for the independent governance order)

```text
The status flip commit must, in ONE change: books.jsonl status -> book_overlay_closed (+overlay field);
update the guard's two Montgomery book_overlay invariants (structured + prose) to the new state-machine
sense; update every live 'NOT book_overlay_closed' marker and 'the rest of the book is unmined' phrasing;
mark the pinned 'partial_overlay stands' lines in units G/H with same-line historical qualifiers
(they would otherwise become the next stale-layer blockers); reconcile the root README Arabic
structure-table row; keep mastery_deferred explicit. Otherwise the guard will (correctly) block the flip.
Housekeeping (non-blocking): C/D per-section Source Coverage numerals; per-card 'trusted' status lines;
missed-treasures chapter table rows for Ch 19-22; frozen 'not started' checklist markers in C/D/F.
```

## 9. Recommendation (single)

```text
RECOMMEND book_overlay_closed
(the four-file treasure overlay of BOOK-ANT-MONTGOMERY-MNT-II-004 is complete under the declared
scope; mastery stays deferred; the status flip itself awaits an independent governance order.)
```

**Ceiling (unchanged):** overlay closure ≠ mathematical closure. Binary Goldbach OPEN · almost-all =
average · conditional stays conditional · bounded gaps/ternary Goldbach = KNOWN source theorems ·
MC-001..005 unsolved · all walls uncrossed · zero RH progress · zero GRH progress · no secured path.

**Honest classification:** Diagnostic (coverage/overlay audit; recommendation only). No RH/GRH progress.
