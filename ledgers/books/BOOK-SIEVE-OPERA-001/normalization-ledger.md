# Opera de Cribro — Normalization Ledger

Book ID: `BOOK-SIEVE-OPERA-001` · Version: v0.7 · **partial_overlay — `OPERA-004-A` CLOSED (v0.7-A PASS) + `OPERA-004-B` CLOSED (v0.7-B PASS).** Routing (both units): `packet_mismatch = true`, `routing_split`.

Each treasure in `treasure-map.md` normalized against the twelve targets. No new `TOOL-ID` and no new `WALL-ID` in this intake; reference material links to already-installed tools, the genuinely new content is carried as `provisional_intake` cards, and the three boundaries stay Boundaries (zero silent wall widening) pending the closure review.

```text
TREASURE-OPERA-001  Sifting function and the Möbius decomposition        [duplicate_status=integration_only]
  → Tool (link)       : TOOL-MOBIUS-001 (Overholt) — Möbius inversion, already installed
  → Tool (link)       : TOOL-SIEVE-INFO-CONSUMPTION-001 (Harman) — sifting as information
  → PVG–ANT           : exact lossless decomposition layer, pre-estimate
  → Classification    : Known / Identity

TREASURE-OPERA-002  Main-term / remainder model  A_d = g(d) X + r_d       [duplicate_status=integration_only]
  → Tool (normalize)  : TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 — level-of-distribution grammar
  → Tool (normalize)  : TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001 — combinatorial sieve remainder handling
  → Load-bearing      : LB-04 (level of distribution)
  → PVG–ANT           : main-term/remainder split as a sequence's pre-certificate ledger
  → Classification    : Known / Reinterpretation

TREASURE-OPERA-003  Sieve Input Certificate Law ( A , g , X , { r_d } )    [duplicate_status=new_function]
  → Load-bearing      : LB-04 (primary) · LB-02 (precursor)
  → Frontier          : FRONTIER-ANT-PVG-004 (sieve information / support geometry)
  → PVG–ANT           : the certificate input contract; exact identity != usable certificate
  → Classification    : Reinterpretation  (primary organizing treasure)

TREASURE-OPERA-004  Aggregate-remainder boundary                          [duplicate_status=new_function]
  → Wall              : none — Boundary; WALL-SIEVE-CEILING text (RH / EH) does not cover aggregate
                        remainder failure, so NO mapping and no silent widening
  → Load-bearing      : LB-04
  → PVG–ANT           : aggregate control is the obligation; individual r_d bounds are a decoy
  → Classification    : Boundary

TREASURE-OPERA-005  Local-model boundary                                  [duplicate_status=new_function]
  → Wall              : none — Boundary + governance caution; repairable via external inputs (LB-05)
  → Load-bearing      : LB-05 (precursor)
  → PVG–ANT           : multiplicative g is a local model, not global independence
  → Classification    : Boundary

TREASURE-OPERA-006  Formulation-vs-certificate boundary                   [duplicate_status=new_function]
  → Wall              : none — Boundary + governance caution; NOT mapped to WALL-PARITY (the gap is more
                        general than parity; parity re-examination deferred to the parity-grounding packet)
  → Missing Certificate: MC-001 — unsolved (context only, post-normalization; not a selection criterion)
  → PVG–ANT           : a sieve formulation is a question, not an answer
  → Classification    : Boundary

TREASURE-OPERA-007  Model-subtraction diagnostic ( B , c_n )              [duplicate_status=new_function]
  → Load-bearing      : LB-02 / LB-06 (precursor)
  → Forward link      : Chapter 18 (asymptotic sieve for primes) — the source reuses this apparatus
  → PVG–ANT           : subtract the model to isolate what the model cannot explain
  → Classification    : Diagnostic
```

## OPERA-004-B normalization (provisional_intake, v0.7-B pending)

```text
TREASURE-OPERA-008  One-Sided Sieve Certificate C_± = (C_input, λ^±, sign, V^±, R^±)  [duplicate_status=new_function]
  → Tool (link)       : TOOL-SIEVE-INFO-CONSUMPTION-001 (Harman) — integration-heavy; C_± is the new record
  → Load-bearing      : LB-03 (primary)
  → PVG–ANT           : direction comes only via weight support + convolution sign + orientation

TREASURE-OPERA-009  Three-Level Certificate Ladder                                    [duplicate_status=new_function]
  → Load-bearing      : LB-03 (primary)
  → PVG–ANT           : bound / sifted-set asymptotic / prime-producing asymptotic — the gap is two steps

TREASURE-OPERA-010  Sandwich-Collapse Criterion                                        [duplicate_status=new_function]
  → Tool (compare)    : Fundamental Lemma cards — collapse-as-criterion is the new framing, not the lemma
  → Load-bearing      : LB-03
  → PVG–ANT           : V^± = V(z)(1+o(1)) + R^± = o(XV(z)) is a criterion to meet, not automatic

TREASURE-OPERA-011  Positive Lower-Bound Gate                                          [duplicate_status=new_function]
  → Load-bearing      : LB-03
  → PVG–ANT           : a lower formula != a positive lower bound (tied to the sifting limit)

TREASURE-OPERA-012  Sifting-Budget Ratio s = log D / log z                             [duplicate_status=integration_only]
  → Normalize         : z != level of distribution (vs Montgomery / Harman); D consumes the distribution budget
  → Load-bearing      : LB-03
  → PVG–ANT           : C_input + D + z + λ^± => the type of result possible

TREASURE-OPERA-013  Target-Purity Certificate                                          [duplicate_status=new_function]
  → Certificate slot  : survivors-are-primes (a named gap, level 2 -> level 3)
  → Wall              : none — Boundary inside LB-03; NOT mapped to WALL-PARITY (z>sqrt(x) avoids, not answers)
  → PVG–ANT           : sifted-set asymptotic + target-purity => prime-producing asymptotic

TREASURE-OPERA-014  Positivity Information-Loss Diagnostic                             [duplicate_status=absorbed]
  → Tool (absorbed)   : TOOL-SIEVE-INFO-CONSUMPTION-001 — no new tool
  → PVG–ANT           : what is discarded for a valid bound is not recoverable for an asymptotic
```

**Duplicate-audit outcome:** A cards 001-002 = `integration_only`, 003-007 = `new_function` (all now `closure_approved`, v0.7-A). B cards: 008/009/010/011/013 = `new_function` (one-sided certificate record, ladder, sandwich-collapse, positive-lower gate, target-purity slot); 012 = `integration_only` (s is standard); 014 = `absorbed` (into TOOL-SIEVE-INFO-CONSUMPTION-001). No `TOOL-ID` or `WALL-ID` minted; B cards `provisional_intake`.

**Honest classification:** Reinterpretation / Diagnostic (normalization ledger, intake). No RH progress. No GRH progress.
