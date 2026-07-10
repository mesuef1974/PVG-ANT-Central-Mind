# OPERA-004-B — One-Sided Sieve Certificates and the Prime-Asymptotic Gap

Book ID: `BOOK-SIEVE-OPERA-001` · Unit: `OPERA-004-B` · Version: v0.7.

**Status:** validated_intake — NOT closed — pending v0.7-B Closure Review.
`primary_class = core_certificate_theory` · `secondary_role = reference_integration` · `packet_mismatch = true (routing_split)` · `trusted_status = provisional_intake` · `load_bearing_target = LB-03`.

## Source packet (provenance)

```text
Treasure Packet: OPERA-TREASURE-PACKET-002 (One-Sided Sieve Certificates and the Prime-Asymptotic Gap)
Range:  Chapter 5 §§5.2-5.4 (Cast of Characters / Sifting Weights / Main Terms and Remainders),
        Chapter 6 §6.1 (Brun's Pure Sieve) and §6.5 (Fundamental Lemma), + Preface orientation on
        Brun's decision to replace asymptotic formulae by upper and lower bounds.
        Transformed notes only; source PDF outside git (Books_others/). Brun selected; Selberg deferred
        (not rejected); no Chapter 16, no parity mechanism.
```

No raw text is copied; this unit is a normalized reading of the packet.

## 1. Inherited object from OPERA-004-A

The unit begins at the closed input certificate of A: `C_input = ( A , g , X , { r_d } )`, with
`A_d = g(d) X + r_d`. This certificate names the available arithmetic material but gives NO direction:
it does not decide whether an upper bound, a lower bound, an asymptotic, or an inconclusive estimate
will follow. B adds the weight-and-sign layer.

## 2. Sieve weights and the direction of the certificate

Let `λ_d` be weights supported on `d < D`, and `θ_n = sum_{d | n} λ_d = (1 * λ)(n)`. Choosing the
weights so that `θ_1 = 1`, the SIGN of `θ_n` for `n > 1` fixes the sieve direction:

```text
θ_n^+ >= 0  (n > 1)  ->  upper sieve
θ_n^- <= 0  (n > 1)  ->  lower sieve
```

With `S^±(A, z) = sum_{d | P(z)} λ_d^± A_d`, this yields the sandwich

```text
S^-(A, z)  <=  S(A, z)  <=  S^+(A, z).
```

So "upper" and "lower" are NOT loose descriptions of estimate quality; they are **sign certificates**
produced by the weights.

### Certificate-direction law

```text
small numerical error   != upper-bound certificate
good heuristic          != lower-bound certificate
one-sided legitimacy requires: weight support + convolution sign + correct orientation of the inequality
```

## 3. Main-term / remainder split of the weighted sums

Inserting `A_d = g(d) X + r_d`:

```text
S^±(A, z) = X V^±(D, z) + R^±(A; D, z),
  V^±(D, z) = sum_{d | P(z)} λ_d^± g(d),
  R^±(A; D, z) = sum_{d | P(z)} λ_d^± r_d.
```

Therefore the one-sided certificate is not "we have weights" but the record

```text
C_± = ( C_input , λ^± , sign(θ^±) , V^± , R^± ).
```

This is a diagnostic record for the project, not a new theorem.

## 4. Three levels that must not be conflated (the certificate ladder)

```text
Level 1  legitimate upper / lower bound
  S(A,z) <= X V^+(D,z) + R^+   or   S(A,z) >= X V^-(D,z) + R^-.
  A real result even if far from the true value. But a lower bound is USELESS unless
  X V^-(D,z) + R^- > 0 — a lower FORMULA does not guarantee positivity (tied to the sifting limit).

Level 2  sifted-set asymptotic
  Needs the sandwich to collapse: V^+(D,z) = V(z)(1+o(1)), V^-(D,z) = V(z)(1+o(1)), R^± = o(X V(z)).
  Only then S(A,z) ~ X V(z). The Fundamental Lemma supplies this collapse when s = log D / log z is large.

Level 3  prime-producing asymptotic
  Even S(A,z) ~ X V(z) does NOT say S counts primes: it counts elements with no prime factor below z,
  which may still include composites with large prime factors. It needs an extra target-purity certificate.
```

## 5. Governing semantic boundary for LB-03

```text
one-sided sieve certificate != sifted-set asymptotic certificate != prime-producing asymptotic certificate
```

**Promotion conditions** (each level requires strictly more):

```text
upper/lower bound      = sign-valid weights + main-term evaluation + controlled weighted remainder
sifted-set asymptotic  = valid upper AND lower certificates + collapse of V^+ and V^- + both remainders negligible
prime-producing asymp. = sifted-set asymptotic + target-purity certificate
```

**Statements the LB-03 semantic check forbids promoting** (both transitions guarded):

```text
S(A,z) <= main term            does NOT imply an asymptotic.
S(A,z) >= positive quantity    does NOT imply the survivors are primes.
S(A,z) ~ X V(z)                does NOT imply a prime-counting asymptotic.
Fundamental Lemma              does NOT imply production of primes.
correct order of magnitude     does NOT imply the correct asymptotic constant.
```

## 6. What positivity actually does

Brun's strength is discarding pieces that cannot be estimated, thanks to their favourable sign. This
yields a valid bound but pays an epistemic price: `positivity -> discard uncontrolled pieces ->
one-sided truth`, and NOT `positivity -> recovery of the discarded information`.

### Positivity information-loss diagnostic

```text
what is discarded can preserve inequality validity while preventing asymptotic recovery.
```

This is functionally consistent with the installed sieve-information-consumption tool, so no new tool
is proposed here.

## 7. The ratio s = log D / log z

Two parameters that are often conflated:

```text
z : sifting level          — up to which primes we remove factors.
D : weight / distribution level — up to which moduli we can run the weights and remainders.
s = log D / log z : the "proof room" between what we know about distribution and what we demand of sifting.
  large s -> upper/lower bounds can approach one another.
  small s -> the gap can stay substantial and the lower main term may cease to be positive.
```

This is the real link between A and LB-03: `C_input + D + z + λ^±  =>  the TYPE of result possible`.

## 8. Target-purity gap is NOT a parity claim (ceiling fence)

Level 2 -> Level 3 needs a **target-purity certificate**: the survivors at the chosen sifting level ARE
the intended target (or the composite survivors' contribution is bounded and negligible against the main
term). In the simple model `n <= x`, taking `z > sqrt(x)` makes every composite `n <= x` have a prime
factor below `z`, so the survivors become primes (up to edge cases) — but raising `z` that far lowers
`s = log D / log z` and may leave the range where the sandwich collapses. This is a **certificate gap**,
NOT a statement about the parity obstruction: `z > sqrt(x)` **avoids** the question (leaves the sieve
range) rather than answering it. No link to `WALL-PARITY` is made here; that is a later packet.

## 9. Reuse of OPERA-004-A treasures (measured, not impressionistic)

```text
reused_object                          shortened_step  missing_field_detected                error_prevented                          changes_without_A
C_input = (A,g,X,{r_d})                yes             weights + sign absent from A's cert.  treating A_d=g(d)X+r_d as a finished sieve result   yes
aggregate-remainder Boundary           yes             control of R^± = Σ λ_d^± r_d, not r_d individually   promoting local bounds to a sieve bound            yes
formulation-vs-certificate Boundary    yes             S(A,z) does not fix the certificate type            conflating a sieve problem with a prime asymptotic yes
local-model Boundary                   partial         V^± depends on g, but direction comes from weights   treating the local model alone as a one-sided bound partial
model-subtraction diagnostic           no              no new field in this material                        forcing A's card into a slot it does not need      no
```

Explicit outcome: `C_input`, aggregate-remainder, and formulation-vs-certificate are **live reusable
functions**; local-model is partial; **model-subtraction is NOT reused in Packet 002** and remains an
open, named test debt (not closed by assertion — it awaits a unit that actually computes `c_n`).

## 10. Normalization with Harman / Montgomery (structured, not prose-only)

```text
Opera object       role                                  in-mind normalization
z (sifting level)  range of removed primes               != level of distribution
D (sieve level)    weight support / modulus range        consumes the available distribution budget
A_d=g(d)X+r_d      input certificate                     inherited from A; meets Montgomery remainder diagnostics
λ^±                sign-directed weights                  a layer the distribution certificate alone does not supply
V^±(D,z)           weight-distorted main term            not automatically V(z)
R^±                remainders after weight consumption    audited weight-wise, not term-by-term
S^- <= S <= S^+    one-sided certificate                 agrees functionally with Harman's information-consumption view
s = log D / log z  distribution-budget-to-sifting ratio  not reducible to "we have a level of distribution"
```

### Negative normalization (no early links)

```text
Type I/II or bilinear input : not part of this packet.
parity principle            : not part of this packet.
asymptotic sieve for primes : not part of this packet.
```

No links to those layers are created before their own source packets.

## 11. Governance dimensions (from the packet)

```text
novelty_claim_risk      = low       (Brun is classical)
semantic_overclaim_risk = medium    (S ~ X V(z) is easily misread as a prime asymptotic)
load_bearing_impact     = high      (LB-03 is a frozen load-bearing node)
state_transition_impact = medium
```

`packet_mismatch = true` triggers the automatic escalation rule, so this intake does NOT use a fully
lightened governance profile.

## 12. Mandatory duplicate audit (pre-tool)

No new `TOOL-ID` and no new `WALL-ID` is minted in this intake. Comparison:

```text
One-Sided Sieve Certificate     -> integration-heavy vs Harman upper/lower-bound handling; the unifying
                                   record C_± is the new organizing content (mirrors C_input in A).
Positivity Information-Loss      -> absorbed by TOOL-SIEVE-INFO-CONSUMPTION-001 (no new tool).
Sandwich-Collapse Criterion      -> checked against Fundamental Lemma cards; the collapse-as-criterion
                                   framing is the new content, not the lemma itself.
Target-Purity Certificate        -> a new named certificate slot (survivors = target), not an old constraint renamed.
Sifting-Budget Ratio (s)         -> integration_only; s is standard, recorded not minted.
Symbol differences (D, z, s, V^±, R^±) are NOT tool differences when the function already exists.
```

## 13. Scientific classification

```text
Known:               sieve weights, sign-directed sandwich, Brun's pure sieve, Fundamental Lemma, the ratio s.
Identity:            S^± = X V^± + R^± ; S^- <= S <= S^+.
Reinterpretation:    C_± as a one-sided certificate record; target-purity as a named certificate slot.
Diagnostic:          the three-level ladder; sandwich-collapse criterion; positivity information-loss.
Boundary:            positive-lower-bound gate (a lower formula != a positive lower bound);
                     the prime-asymptotic gap (a Boundary INSIDE LB-03, not a wall).
New Theorem:         none.
Candidate Mechanism: none.
MC-001 progress:     none.
RH/GRH progress:     zero RH progress, zero GRH progress.
```

## Next valid action

This unit is a historical intake record. The only authoritative live next action is
`transition-memory/next-action.md` (the v0.7-B Closure Review is pending; this intake does not close it).

**Honest classification:** Reinterpretation / Diagnostic (unit intake, NOT closed). No RH progress. No GRH progress. No mastery.
