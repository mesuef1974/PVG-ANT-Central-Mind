# Opera de Cribro — Treasure Map

Book ID: `BOOK-SIEVE-OPERA-001` · Version: v0.7 · **Status: partial_overlay — `OPERA-004-A` CLOSED (v0.7-A PASS) + `OPERA-004-B` validated_intake (v0.7-B pending).**

First mined unit `OPERA-004-A` (Sifting Sequences as Main-Term/Remainder Certificates), grounded in `OPERA-TREASURE-PACKET-001` (Preface + Ch 1 §§1.1-1.4), transformed notes only, PDF outside git. **Routing (v0.7-A adjudicated): `packet_mismatch = true`, `mismatch_type = routing_split`** — the frozen hypothesis predicted primary `reference_integration`; the packet grounded primary `core_certificate_theory` with `reference_integration` retained as secondary. Cards are classified from the packet content, not the table of contents. No new `TOOL-ID` minted; **zero new `WALL-ID` and no silent widening** of an existing wall (all three boundaries stay Boundaries). A's cards (001-007) are `trusted_status = closure_approved` (v0.7-A Closure Review PASS, AUDIT-CM-V07-A-CLOSURE-001).

**Second unit `OPERA-004-B`** (One-Sided Sieve Certificates and the Prime-Asymptotic Gap), grounded in `OPERA-TREASURE-PACKET-002` (Ch 5 §§5.2-5.4 + Ch 6 §§6.1/6.5, Brun's pure sieve + Fundamental Lemma), transformed notes only. **Routing: `packet_mismatch = true`, `mismatch_type = routing_split`** (frozen hypothesis primary `reference_integration`; packet grounded primary `core_certificate_theory`, secondary `reference_integration`) — recorded from the packet, not discovered late. Target `LB-03`. No new `TOOL-ID`, no new `WALL-ID` (the prime-asymptotic gap is a Boundary INSIDE LB-03, not a wall; no link to WALL-PARITY). B's cards (008-014) are `trusted_status = provisional_intake` (v0.7-B pending).

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

## OPERA-004-B cards (provisional_intake, v0.7-B pending)

```text
Treasure ID: TREASURE-OPERA-008
Status:      validated_intake (live intake route; OPERA-004-B not yet closed)
Treasure:    One-Sided Sieve Certificate  C_± = (C_input, λ^±, sign(θ^±), V^±, R^±)
Source:      OPERA-004-B (Ch 5 §§5.2-5.4) — transformed notes only
Type:        reinterpretation (organizing record)
Why it matters: sign-directed weights turn the directionless input certificate into an upper OR lower
             certificate; "one-sided" is a sign fact, not an estimate-quality description.
ANT role:    weighted sieve sums S^± = X V^± + R^±, sandwich S^- <= S <= S^+.
PVG translation: direction comes only from weight support + convolution sign + orientation.
Wall / certificate: none crossed; a direction record, not a bound value.
Classification: Reinterpretation.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Reinterpretation · trusted_status=provisional_intake
Normalized output: → LB-03 (primary) ; integration-heavy vs Harman upper/lower handling ; mirrors C_input (A).
```

```text
Treasure ID: TREASURE-OPERA-009
Status:      validated_intake (live intake route; OPERA-004-B not yet closed)
Treasure:    Three-Level Certificate Ladder
Source:      OPERA-004-B (Ch 5-6 ladder) — transformed notes only
Type:        diagnostic
Why it matters: separates one-sided bound / sifted-set asymptotic / prime-producing asymptotic — the gap
             is TWO steps, not one; conflating any two is the central LB-03 error.
ANT role:    bound -> (collapse) -> sifted asymptotic -> (target-purity) -> prime asymptotic.
PVG translation: each level requires strictly more; naming the ladder blocks silent promotion.
Wall / certificate: prime-asymptotic gap = Boundary INSIDE LB-03 (not a wall).
Classification: Diagnostic.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Diagnostic · trusted_status=provisional_intake
Normalized output: → LB-03 (primary) ; anchor of the LB-03 semantic check.
```

```text
Treasure ID: TREASURE-OPERA-010
Status:      validated_intake (live intake route; OPERA-004-B not yet closed)
Treasure:    Sandwich-Collapse Criterion
Source:      OPERA-004-B (Ch 6 §6.5, Fundamental Lemma) — transformed notes only
Type:        diagnostic
Why it matters: names WHEN the sandwich collapses to an asymptotic — V^± = V(z)(1+o(1)), R^± = o(XV(z)) —
             the Fundamental Lemma supplying it when s = log D/log z is large.
ANT role:    collapse of V^+ and V^- with negligible weighted remainders.
PVG translation: collapse is a criterion to be met, not an automatic consequence of having weights.
Wall / certificate: none crossed; a criterion, not a result.
Classification: Diagnostic.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Diagnostic · trusted_status=provisional_intake
Normalized output: → LB-03 ; checked vs Fundamental Lemma cards (collapse-as-criterion is the new framing).
```

```text
Treasure ID: TREASURE-OPERA-011
Status:      validated_intake (live intake route; OPERA-004-B not yet closed)
Treasure:    Positive Lower-Bound Gate
Source:      OPERA-004-B (Ch 5-6, lower sieve) — transformed notes only
Type:        boundary / diagnostic
Why it matters: a lower FORMULA (S >= XV^- + R^-) is useless unless XV^- + R^- > 0; a lower-bound formula
             does not grant positivity (tied to the sifting limit).
ANT role:    positivity of the lower main term as a separate gate.
PVG translation: "we have a lower bound" != "we have a positive lower bound".
Wall / certificate: Boundary; ties to the sifting limit, not a wall.
Classification: Boundary.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Boundary · trusted_status=provisional_intake
Normalized output: → LB-03 ; → sifting-limit context.
```

```text
Treasure ID: TREASURE-OPERA-012
Status:      validated_intake (live intake route; OPERA-004-B not yet closed)
Treasure:    Sifting-Budget Ratio  s = log D / log z
Source:      OPERA-004-B (§7 packet) — transformed notes only
Type:        known / reinterpretation (integration)
Why it matters: distinguishes sifting level z (removed primes) from weight/distribution level D; s measures
             the proof room between known distribution and demanded sifting.
ANT role:    large s -> bounds approach; small s -> gap persists, lower main term may lose positivity.
PVG translation: C_input + D + z + λ^± => the TYPE of result possible.
Wall / certificate: none crossed; a standard ratio, recorded not minted.
Classification: Known / Reinterpretation.
Review fields: source_grounded=true · duplicate_status=integration_only · scientific_class=Reinterpretation · trusted_status=provisional_intake
Normalized output: → LB-03 ; z != level of distribution (normalization vs Montgomery / Harman).
```

```text
Treasure ID: TREASURE-OPERA-013
Status:      validated_intake (live intake route; OPERA-004-B not yet closed)
Treasure:    Target-Purity Certificate
Source:      OPERA-004-B (level-3 packet) — transformed notes only
Type:        reinterpretation (named certificate slot)
Why it matters: the extra certificate to move from a sifted-set asymptotic to prime production — the
             survivors ARE the target (or composite survivors negligible). A named certificate GAP.
ANT role:    survivors-are-primes as a named, missing certificate slot.
PVG translation: sifted-set asymptotic + target-purity => prime-producing asymptotic; without it, no primes claim.
Wall / certificate: Boundary inside LB-03; z>sqrt(x) AVOIDS the question (drops s), NOT a parity claim; NOT mapped to WALL-PARITY.
Classification: Reinterpretation.
Review fields: source_grounded=true · duplicate_status=new_function · scientific_class=Reinterpretation · trusted_status=provisional_intake
Normalized output: → LB-03 ; parity re-examination DEFERRED to the parity-grounding packet.
```

```text
Treasure ID: TREASURE-OPERA-014
Status:      validated_intake (live intake route; OPERA-004-B not yet closed)
Treasure:    Positivity Information-Loss Diagnostic
Source:      OPERA-004-B (Ch 6 §6.1, Brun) — transformed notes only
Type:        diagnostic (absorbed)
Why it matters: positivity lets Brun discard uncontrolled pieces -> one-sided truth, but does NOT recover
             the discarded information; discarding can preserve inequality validity while blocking asymptotic recovery.
ANT role:    the epistemic price of positivity.
PVG translation: what is discarded for a valid bound is not recoverable for an asymptotic.
Wall / certificate: none crossed; a diagnostic.
Classification: Diagnostic.
Review fields: source_grounded=true · duplicate_status=absorbed · scientific_class=Diagnostic · trusted_status=provisional_intake
Normalized output: → absorbed by TOOL-SIEVE-INFO-CONSUMPTION-001 (no new tool).
```

**Card summary:** A (001-007, `closure_approved`): 5 new_function + 2 integration_only. B (008-014, `provisional_intake`, v0.7-B pending): 5 new_function (008 one-sided certificate · 009 ladder · 010 sandwich-collapse · 011 positive-lower-gate · 013 target-purity) + 1 integration_only (012 sifting-budget ratio) + 1 absorbed (014 positivity info-loss). **Zero new TOOL-ID, zero new WALL-ID across both units.**

**Honest classification:** Reinterpretation / Diagnostic (treasure map; A closed, B intake NOT closed). No RH progress. No GRH progress. No new tool minted; no new wall.
