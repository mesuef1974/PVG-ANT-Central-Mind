# Opera de Cribro — Treasure Map

Book ID: `BOOK-SIEVE-OPERA-001` · Version: v0.7 · **Status: partial_overlay — one CLOSED unit (`OPERA-004-A`, v0.7-A Closure Review PASS).**

First mined unit `OPERA-004-A` (Sifting Sequences as Main-Term/Remainder Certificates), grounded in `OPERA-TREASURE-PACKET-001` (Preface + Ch 1 §§1.1-1.4), transformed notes only, PDF outside git. **Routing (v0.7-A adjudicated): `packet_mismatch = true`, `mismatch_type = routing_split`** — the frozen hypothesis predicted primary `reference_integration`; the packet grounded primary `core_certificate_theory` with `reference_integration` retained as secondary. Cards are classified from the packet content, not the table of contents. No new `TOOL-ID` minted; **zero new `WALL-ID` and no silent widening** of an existing wall (all three boundaries stay Boundaries). Every card is `trusted_status = closure_approved` (v0.7-A Closure Review PASS, AUDIT-CM-V07-A-CLOSURE-001).

```text
Treasure ID: TREASURE-OPERA-001
Status:      closure_approved (v0.7-A Closure Review PASS; unit closed)
Treasure:    Sifting function and the Möbius decomposition
Source:      OPERA-004-A (Ch 1 §§1.1-1.2) — transformed notes only
Type:        identity / reference integration
Why it matters: S(A,z) = sum_{d|P(z)} mu(d) A_d(x) turns the coprimality condition into congruence
             sums — the exact skeleton every sieve certificate is built on.
ANT role:    Möbius inversion of a coprimality indicator over P(z).
PVG translation: the exact (lossless) decomposition layer, before any estimate.
Wall / certificate: none crossed; exactness is not an estimate.
Classification: Known / Identity.
Review fields: source_grounded=true · duplicate_status=integration_only · scientific_class=Identity · trusted_status=closure_approved
Normalized output: → integration link TOOL-MOBIUS-001 ; → integration link TOOL-SIEVE-INFO-CONSUMPTION-001.
```

```text
Treasure ID: TREASURE-OPERA-002
Status:      closure_approved (v0.7-A Closure Review PASS; unit closed)
Treasure:    Main-term / remainder model  A_d = g(d) X + r_d
Source:      OPERA-004-A (Ch 1 §1.3) — transformed notes only
Type:        reinterpretation / normalization
Why it matters: splits the proof obligation into a local main term (g(d) X) and an aggregate
             remainder; the sieve stands or falls on the TYPE of control over the remainder family.
ANT role:    local density model + remainder; the level-of-distribution grammar.
PVG translation: main-term/remainder split as the pre-certificate ledger of a sequence.
Wall / certificate: aggregate-remainder boundary — see TREASURE-OPERA-004.
Classification: Known / Reinterpretation.
Review fields: source_grounded=true · duplicate_status=integration_only · scientific_class=Reinterpretation · trusted_status=closure_approved
Normalized output: → normalization vs TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 (level of distribution)
             ; → normalization vs TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001.
```

```text
Treasure ID: TREASURE-OPERA-003
Status:      closure_approved (v0.7-A Closure Review PASS; unit closed)
Treasure:    Sieve Input Certificate Law  ( A , g , X , { r_d } )
Source:      OPERA-004-A (Ch 1, packet law) — transformed notes only
Type:        reinterpretation (primary organizing treasure)
Why it matters: a sieve certificate begins not at the divisor detector but at the quadruple
             (sequence+mass, local densities, validity range, TYPE of aggregate remainder control).
ANT role:    the minimal input structure of any sieve argument.
PVG translation: the certificate's input contract; "exact identity != usable certificate".
Wall / certificate: formulation-vs-certificate boundary — see TREASURE-OPERA-006.
Classification: Reinterpretation.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Reinterpretation · trusted_status=closure_approved
Normalized output: → LB-04 (primary) ; → LB-02 (precursor) ; → integration with the sieve pillar (Harman / Montgomery).
```

```text
Treasure ID: TREASURE-OPERA-004
Status:      closure_approved (v0.7-A Closure Review PASS; unit closed)
Treasure:    Aggregate-remainder boundary
Source:      OPERA-004-A (Ch 1 §1.3, negative certificate) — transformed notes only
Type:        boundary
Why it matters: bounding each r_d individually does NOT bound their sieve sum; the naive remainder
             is of main-term order — the failure is known by external comparison (PNT), not the identity.
ANT role:    control of sum_d mu(d) r_d, not of individual r_d.
PVG translation: aggregate control is the real obligation; individual bounds are a decoy.
Wall / certificate: Boundary. NOT mapped to WALL-SIEVE-CEILING — its registered text ("no unconditional
             sieve reaches RH; only EH crosses") speaks of the RH ceiling, not aggregate remainder failure;
             no silent widening. Zero new WALL-ID.
Classification: Boundary.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Boundary · trusted_status=closure_approved
Normalized output: → Boundary (no wall mapping) ; → LB-04.
```

```text
Treasure ID: TREASURE-OPERA-005
Status:      closure_approved (v0.7-A Closure Review PASS; unit closed)
Treasure:    Local-model boundary
Source:      OPERA-004-A (Ch 1, density meaning) — transformed notes only
Type:        boundary + governance caution
Why it matters: multiplicative g(d) is a local independence MODEL, not literal global arithmetic
             independence; the gap between model and reality is a source of the sieve's shortfall.
ANT role:    multiplicativity of g as a modelling assumption with limited validity.
PVG translation: local density = model; global independence is not granted.
Wall / certificate: Boundary + governance caution. Repairable via external inputs (LB-05) — the opposite
             of a wall. Zero new WALL-ID.
Classification: Boundary.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Boundary · trusted_status=closure_approved
Normalized output: → Boundary / governance caution ; → LB-05 (precursor, external inputs repair the model).
```

```text
Treasure ID: TREASURE-OPERA-006
Status:      closure_approved (v0.7-A Closure Review PASS; unit closed)
Treasure:    Formulation-vs-certificate boundary
Source:      OPERA-004-A (Ch 1 §§1.1-1.2 examples) — transformed notes only
Type:        boundary + governance caution
Why it matters: rewriting twin-primes / Goldbach / prime-values as a sieve is easy and supplies NO
             estimate; formulation is not production. Fenced: no example is a solution path or a parity crossing.
ANT role:    separation of problem statement from the estimate that would resolve it.
PVG translation: a sieve formulation is a question, not an answer.
Wall / certificate: Boundary + governance caution. NOT mapped to WALL-PARITY in this packet — the
             formulation/certificate gap is more general than parity (remainder distribution, level of
             distribution, local obstructions, external inputs); re-examining its relation to WALL-PARITY
             is DEFERRED to the packet that source-grounds the parity phenomenon. Zero new WALL-ID.
Classification: Boundary.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Boundary · trusted_status=closure_approved
Normalized output: → Boundary / governance caution ; → Missing Certificate MC-001 (context only, added post-normalization).
```

```text
Treasure ID: TREASURE-OPERA-007
Status:      closure_approved (v0.7-A Closure Review PASS; unit closed)
Treasure:    Model-subtraction diagnostic  ( B , c_n = a_n - (A(x)/x) b_n )
Source:      OPERA-004-A (Ch 1 §1.4) — transformed notes only
Type:        diagnostic (subject to duplicate audit)
Why it matters: a normalized reference sequence with the same local density cancels the modeled main
             terms, isolating non-model behaviour in the remainder layer; the source reuses this in Ch 18.
ANT role:    reference-sequence subtraction; main-term cancellation, residual isolation.
PVG translation: subtract the model to see what the model cannot explain.
Wall / certificate: none crossed; a diagnostic, not a mechanism.
Classification: Diagnostic.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Diagnostic · trusted_status=closure_approved
Normalized output: → LB-02 / LB-06 precursor ; forward link to Ch 18.
```

**Card summary:** 5 `new_function` (003 certificate law · 004/005/006 boundaries · 007 diagnostic) + 2 `integration_only` (001 identity · 002 normalization). All `trusted_status = closure_approved`. Zero new TOOL-ID, zero new WALL-ID.

**Honest classification:** Reinterpretation / Diagnostic (treasure map, one intake unit, NOT closed). No RH progress. No GRH progress. No new tool minted; no new wall.
