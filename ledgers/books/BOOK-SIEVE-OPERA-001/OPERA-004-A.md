# OPERA-004-A — Sifting Sequences as Main-Term/Remainder Certificates

Book ID: `BOOK-SIEVE-OPERA-001` · Unit: `OPERA-004-A` · Version: v0.7.

**Status:** validated_intake — NOT closed — pending v0.7-A Closure Review (Attempt 2).
`primary_class = core_certificate_theory` · `secondary_role = reference_integration` · `packet_mismatch = true (routing_split)`.

## Source packet (provenance)

```text
Treasure Packet: OPERA-TREASURE-PACKET-001 (Sifting Sequence and the Main-Term/Remainder Certificate)
Range:  Preface orientation + Chapter 1, §§1.1-1.4 (inclusion-exclusion, sieve formulation,
        model sifting sequence). Transformed notes only; source PDF outside git (Books_others/).
```

No raw text is copied; this unit is a normalized reading of the packet.

## 1. Source objects

A sifting problem starts from a sequence `A = (a_n)`, `a_n >= 0`, and a set of primes `P` with
`P(z) = prod_{p<z, p in P} p`. The **sifting function** is

```text
S(A, z) = sum_{n<=x, gcd(n, P(z))=1} a_n
```

and the **congruence sums** are `A_d(x) = sum_{n<=x, d | n} a_n`. The packet's basic model is

```text
A_d(x) = g(d) X + r_d(x)
```

where `X` approximates the total mass `A(x)`, `g(d)` is the local-density function, and `r_d(x)`
is the remainder measuring the failure of the local model.

## 2. Exact identity

With the Möbius coprimality detector `1_{gcd(n,P(z))=1} = sum_{d | gcd(n, P(z))} mu(d)`,

```text
S(A, z) = sum_{d | P(z)} mu(d) A_d(x)
        = X sum_{d | P(z)} mu(d) g(d)  +  sum_{d | P(z)} mu(d) r_d(x).
```

This is **not yet a successful sieve theorem**: it is the decomposition of the proof obligation
into a local main term and an aggregate remainder.

## 3. Central negative certificate

Eratosthenes–Legendre is exact, but replacing `[x/d]` by its expected value produces a main term
with the wrong constant, because the number of remainders is huge and their accumulation is of the
same order as the quantity one wanted to call the main term. Therefore:

> The exact identity and a bound on each individual local error are **not enough**; what is required
> is **aggregate control** over the family `{r_d}`.

The source shows the naive "remainder" is not actually small, and that the failure is known not from
the identity itself but from an **external comparison** (e.g. the prime number theorem).

## 4. Sieve Input Certificate Law (the organizing treasure)

A sieve certificate does not begin at the divisor detector; it begins at the quadruple

```text
( A , g , X , { r_d } )
```

with an explicit statement of: (1) the sequence and its mass, (2) the local densities `g(d)`,
(3) the validity range of `A_d = g(d) X + r_d`, and (4) the TYPE of aggregate control on `{ r_d }`.
The governing inequalities:

```text
exact coprimality identity   != usable sieve certificate
local remainder bounds       != aggregate remainder control
problem formulation          != prime production
```

## 5. Meaning of the density function

The source treats `g(d)` as a local density / probability and usually assumes it multiplicative:
this is the model of independence of divisibility at coprime moduli. It warns that this independence
is limited in applications, and that its limitation is one source of the sieve's shortfall.

```text
multiplicative density = local model, NOT literal global independence
```

## 6. Chapter examples and their fencing

The chapter formulates (not solves) several problems as sieve sequences: integers in an interval;
values `m^2 + 1`; `m(m+2)` (twin-type); the sequence `p - 2` (where remainders tie to primes in
arithmetic progressions); and Goldbach / prime-values-of-polynomials forms. The source's message is
that the sieve **formulation** is easy while the required estimates are very hard.

Fencing (mandatory): no example in this unit is a solution path for twin primes, a solution path for
Goldbach, a crossing of the parity barrier `WALL-PARITY`, or progress on `MC-001`. Formulating a
prime problem as a sieve does not supply the estimate that would solve it.

## 7. Reference model-subtraction diagnostic

In §1.4 the source builds a model sequence `B = (b_n)` carrying the same local density `g(d)` with
suitable control on its average remainders, then compares `A` to a normalized copy of `B` via a
difference `c_n = a_n - (A(x)/x) b_n`. The modeled main terms then cancel in the congruence sums and
the difference is isolated in the remainder layer. The source states this apparatus is used again in
Chapter 18 (asymptotic sieve for primes).

```text
same local density + normalized reference sequence
  -> cancellation of modeled main terms
  -> residual sequence isolates non-model behaviour
```

This is a diagnostic re-organization of the source material, not a new theorem for the project.

## 8. Boundaries exposed by the packet (v0.7-A adjudicated: zero new WALL-IDs, zero silent widening)

The packet exposes three obstruction descriptions. The v0.7-A Closure Review adjudicated each by exact
semantic comparison against the registered walls. Outcome: **zero new WALL-IDs and no silent widening of
an existing wall** — all three stay Boundaries:

```text
aggregate-remainder            : individual r_d control does not give control of their sieve sum.
  fate = Boundary. WALL-SIEVE-CEILING's registered text ("no unconditional sieve reaches RH; only EH
  crosses") speaks of the RH ceiling, NOT of aggregate remainder failure — so NO mapping, no silent widening.
local-model                    : multiplicative g is a local model, not global arithmetic independence.
  fate = Boundary + governance caution. Repairable via external inputs (LB-05) — the opposite of a wall.
formulation-vs-certificate     : rewriting a prime problem as a sieve supplies no estimate to solve it.
  fate = Boundary + governance caution. NOT mapped to WALL-PARITY: this packet has not reached the parity
  mechanism itself, and the formulation/certificate gap is more general than parity (remainder distribution,
  level of distribution, local obstructions, external inputs). Re-examining its relation to WALL-PARITY is
  DEFERRED to the packet that source-grounds the parity phenomenon — not to the mere appearance of prime examples.
```

The registered parity barrier `WALL-PARITY` is NOT crossed here, and this unit maps NO boundary onto it;
the unit only builds the language in which such barriers are later adjudicated.

## 9. Packet-grounded classification (routing_split recorded)

```text
packet_mismatch = true
mismatch_type   = routing_split

original_hypothesis  (v0.7-scope.md, "Early: inclusion-exclusion, Brun, Selberg" row, verbatim):
  primary = reference_integration   ("duplicate-pressure vs Harman / Montgomery D", provisional)

packet_grounded_classification:
  primary   = core_certificate_theory
  secondary = reference_integration

reason:
  the packet established a load-bearing certificate architecture (the sieve INPUT certificate law
  (A,g,X,{r_d}), the model-subtraction diagnostic, three boundary cards) while retaining the expected
  duplicate-pressure integration role only as SECONDARY. The PRIMARY axis changed
  (reference_integration -> core_certificate_theory), so this is routing_split — recorded per the
  source-first / provisional-routing rule, NOT silently rewritten.
```

The frozen hypothesis is preserved verbatim above; it was not erased, only demoted to the secondary
role. (This corrects the v0.7-A Attempt-1 blocker: the earlier phrasing recorded the mismatch as
absent by calling it a mere refinement — but refinement requires the primary class to be unchanged,
and here the primary class changed, so it is a routing_split and the mismatch is true.)

## 10. Load-bearing linkage

```text
LB-04 (level of distribution and its exact function) = primary  (validity range of A_d = g(d)X + r_d)
LB-02 (bilinear remainders)                          = precursor only (remainder layer named, not yet bilinear)
LB-01 (parity obstruction)                           = not yet reached
LB-03 (upper/lower vs asymptotic prime sieve)        = not yet reached
LB-05 (external analytic inputs)                     = not yet reached
LB-06 (application-specific transfer)                = examples expose non-transfer; no application certificate yet
```

No LB node is closed by this intake.

## 11. Mandatory duplicate audit (pre-tool)

No new `TOOL-ID` is minted in this intake. Comparison against existing capabilities:

```text
Möbius coprimality detector      -> existing TOOL-MOBIUS-001 (Overholt); integration link, not a new tool.
inclusion-exclusion / sifting    -> existing TOOL-SIEVE-INFO-CONSUMPTION-001 (Harman); integration card.
A_d = g(d)X + r_d / level grammar -> TOOL-MONTGOMERY-LARGE-SIEVE-DIAGNOSTIC-001 language (level of
                                    distribution) + TOOL-MONTGOMERY-SIEVE-DIAGNOSTIC-001; normalization card.
model-subtraction (B, c_n)       -> candidate treasure, subject to duplicate_concept_audit; carried as a
                                    diagnostic card, NOT yet a tool (returns in Ch 18 per the source).
```

Genuinely new (non-duplicate) organizing content, recorded as provisional-intake cards: the Sieve Input
Certificate Law `(A,g,X,{r_d})` and the model-subtraction diagnostic, plus three boundary cards
(aggregate-remainder, local-model, formulation-vs-certificate). Everything else is an integration /
normalization link to an already-installed tool. No card is trusted / closure-approved before the review.

## 12. Scientific classification

```text
Known:              Möbius identities, sieve formulation, chapter examples, model-sequence construction.
Identity:           S(A,z) = sum_d mu(d) A_d.
Boundary:           the exact identity gives no estimate without aggregate remainder control.
Reinterpretation:   (A, g, X, {r_d}) as a sieve INPUT certificate.
Diagnostic:         model-subtraction to isolate behaviour not explained by local densities.
New Theorem:        none.
Candidate Mechanism: none.
MC-001 progress:    none.
RH/GRH progress:    zero RH progress, zero GRH progress.
```

## 13. Prior review effect (intake correction, NOT a State-Repair)

```text
v0.7-A Closure Review — Attempt 1
  result             = RETURN to validated_intake
  blocking_issue     = incorrect packet_mismatch classification (asserted false; must be routing_split true)
  additional_correction = over-early parity-wall mapping avoided (formulation-vs-certificate NOT mapped
                          to WALL-PARITY; deferred to the parity-grounding packet)
```

This is an intake correction: no closed unit and no trusted claim was altered (the unit was never closed).
It is NOT a State-Repair — no guard invariant or cross-repo truth layer was structurally wrong.

## Next valid action

This unit is a historical intake record. The only authoritative live next action is
`transition-memory/next-action.md` (the v0.7-A Closure Review re-run is pending; this intake does not close it).

**Honest classification:** Reinterpretation / Diagnostic (unit intake, NOT closed). No RH progress. No GRH progress. No mastery.
