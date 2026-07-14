#!/usr/bin/env python3
"""
STEP A authoring + validation generator for ADVERSARIAL-PVG-ANT-BENCHMARK-002 Hidden Set A.

Governed by (all frozen at workshop open, main @ 3235fd7):
  - BENCHMARK-002-SEALING-PROTOCOL-001.md         (per-case schema §3, fatal codes §5, leakage §8)
  - BENCHMARK-002-DISTRIBUTION-MATRIX-001.md      (axis counts + cross-cutting quotas)
  - BENCHMARK-002-FROZEN-SCORING-RUBRIC-001.md    (five components + fatal override)
  - BENCHMARK-002-ROLE-SEPARATION-RECEIPT-001.md  (R1 authors; keys held out of R3 context)

This script IS the R1/R2 authoring artifact. It:
  1. holds the 48 cases as structured data,
  2. emits three separation-safe files (prompts / scoring-metadata / keys),
  3. machine-validates every frozen invariant (fails loudly on any breach),
  4. computes SHA-256 key-hashes (only the hashes are committed; keys are owner-held).

Capability measurement only. Zero RH progress, zero GRH progress. No secured path.
No case reproduces a Benchmark-001 card, a Translation-Kernel card, a Core-Ontology
object, the I_r pipeline, or a book-ledger unit (leakage screen §8; every case LEAK-0-CLEAR).
"""
from __future__ import annotations
import json, hashlib, sys, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

# Closed fatal-error vocabulary (SEALING §5 / RUBRIC §2) -- fatal_errors may only draw from this.
FATAL_CODES = {
    "ERR-FATAL-SCIENTIFIC-CLAIM",
    "ERR-FATAL-COMPUTATION-AS-PROOF",
    "ERR-FATAL-LOSS-INVERSION",
    "ERR-FATAL-SCOPE-VIOLATION",
    "ERR-FATAL-CERTIFICATE-FABRICATION",
    "ERR-FATAL-PROVENANCE-FABRICATION",
    "ERR-FATAL-RH-GRH-CLAIM",
}
LEAK_VALUES = {
    "LEAK-0-CLEAR", "LEAK-1-TEXTUAL-OVERLAP", "LEAK-2-CONCEPTUAL-OVERLAP",
    "LEAK-3-NEAR-FORMULATION-OR-PROJECT-DERIVED", "LEAK-U-UNCERTAIN",
}
TIERS = {"B0", "B1", "B2"}

# Frozen per-axis allocation for Set A (DISTRIBUTION-MATRIX §1).
AXIS_TARGET_A = {1: 4, 2: 3, 3: 3, 4: 5, 5: 5, 6: 5, 7: 3, 8: 3, 9: 3, 10: 4, 11: 5, 12: 5}
AXIS_NAME = {
    1: "ANT correctness", 2: "PVG->ANT translation", 3: "ANT->PVG translation",
    4: "LOSS / non-invertibility accounting", 5: "quantifier discipline",
    6: "normalization", 7: "provenance", 8: "scope / domain-of-validity containment",
    9: "tool selection", 10: "certificate classification", 11: "proof-gap detection",
    12: "overclaim refusal",
}

def C(cid, axis, tier, prompt, expected, rubric, fatal, partial, cert_req, forbidden,
      source_basis, gold, *, loss=None, loss_judgment=False, comp_depth=1,
      reverse=None, abstain=None, leak="LEAK-0-CLEAR"):
    return dict(case_id=cid, capability_target=axis, capability_axis=AXIS_NAME[axis],
                tier=tier, prompt=prompt, expected_structure=expected, rubric=rubric,
                fatal_errors=fatal, partial_credit=partial, certificate_requirements=cert_req,
                forbidden_claims=forbidden, source_basis=source_basis, leakage_class=leak,
                tags=dict(loss_level=loss, loss_judgment=loss_judgment, composition_depth=comp_depth,
                          reverse_inference=reverse, abstention=abstain),
                gold=gold)

# Default component weights (RUBRIC §1): C1 40 / C2 25 / C3 15 / C4 10 / C5 10.
R_DEFAULT = {"C1": 40, "C2": 25, "C3": 15, "C4": 10, "C5": 10}
R_OVERCLAIM = {"C1": 25, "C2": 20, "C3": 15, "C4": 5, "C5": 35}   # overclaim/abstention-weighted
R_LOSS = {"C1": 35, "C2": 30, "C3": 20, "C4": 5, "C5": 10}         # LOSS-accounting-weighted
R_TOOL = {"C1": 25, "C2": 20, "C3": 15, "C4": 30, "C5": 10}        # tool-selection-weighted
R_CERT = {"C1": 25, "C2": 20, "C3": 35, "C4": 5, "C5": 15}         # certificate-weighted

CASES = [
    # ------------------------------------------------------------------ AXIS 1: ANT correctness (4)
    C("B002-A-01-1", 1, "B0",
      "State the asymptotic for the sum of reciprocals of primes up to x, including the precise "
      "additive constant and the error term. Is that constant the Euler-Mascheroni constant?",
      "sum_{p<=x} 1/p = ln ln x + M + o(1); M is the Meissel-Mertens constant (~0.2615), NOT the "
      "Euler-Mascheroni gamma; unconditional error O(1/ln x). Must not identify M with gamma.",
      R_DEFAULT, ["ERR-FATAL-PROVENANCE-FABRICATION"],
      "full C1 requires correct main term+constant identity; C3 = Known theorem (Mertens).",
      "answer would be Known (Mertens' second theorem); no new certificate.",
      "no claim that RH sharpens this constant; no fabricated numeric provenance.",
      "classical Mertens theorem (source-grounded, not a project card).",
      "M is the Meissel-Mertens constant, distinct from gamma; the two coincide only through the "
      "unrelated identity relating gamma to sum over prime powers, not as the additive constant here."),
    C("B002-A-01-2", 1, "B0",
      "Is 'pi(x) ~ x/ln x' the same statement as 'pi(x) ~ Li(x)'? Which is the better approximation, "
      "and state the PNT error term unconditionally versus under RH.",
      "Both hold as ~ (asymptotic equivalence) but Li(x) is a far better approximation; unconditional "
      "error O(x exp(-c sqrt(ln x))); under RH O(sqrt(x) ln x). RH stated as hypothesis, not fact.",
      R_DEFAULT, ["ERR-FATAL-RH-GRH-CLAIM"],
      "C1: correct equivalence + which is sharper; C2: error terms with correct conditionality.",
      "Known (de la Vallee Poussin unconditional; RH-conditional bound is conditional).",
      "no assertion that RH is proved; the sharper bound must stay conditional.",
      "classical PNT and its error terms.",
      "~ makes them asymptotically equal, but Li(x)-pi(x) is far smaller than x/ln x - pi(x); the RH "
      "bound O(sqrt(x) ln x) is CONDITIONAL, the unconditional bound is the exp(-c sqrt(ln x)) saving."),
    C("B002-A-01-3", 1, "B1",
      "For fixed modulus q with (a,q)=1, state the range of x and the error term for primes in the "
      "progression a mod q (Siegel-Walfisz). Is the implied constant effective?",
      "Siegel-Walfisz: pi(x;q,a) = Li(x)/phi(q) + O(x exp(-c sqrt(ln x))) uniformly for q <= (ln x)^A; "
      "the implied constant is INEFFECTIVE (Siegel-zero dependence). Effectivity caveat is the crux.",
      {"C1": 35, "C2": 30, "C3": 15, "C4": 10, "C5": 10}, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C2 rewards stating uniformity range in q; C1 penalized if constant claimed effective.",
      "Known (Siegel-Walfisz) with the ineffectivity property stated.",
      "no claim of an effective constant; no GRH substitution.",
      "classical Siegel-Walfisz theorem.",
      "Range q <= (ln x)^A for any fixed A; error O(x exp(-c_A sqrt(ln x))); constant c_A is "
      "ineffective because the proof passes through a possible Siegel zero."),
    C("B002-A-01-4", 1, "B0",
      "Is sum_{n<=x} d(n) = x ln x + (2 gamma - 1) x + O(sqrt(x)) the sharpest known statement? "
      "What is the Dirichlet divisor problem and what is the status of the error exponent?",
      "Main term x ln x + (2 gamma - 1) x is exact; O(sqrt(x)) is the classical Dirichlet bound; the "
      "true error exponent theta is OPEN (conjectured 1/4, best known ~0.3149...). Improvement past 1/4 "
      "is an open problem, not settled.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C1: correct main term; C3: classify exponent status as Open, not Known-sharp.",
      "Known main term; Open Problem for the exponent (must not claim theta resolved).",
      "no claim that the divisor exponent is proved to be 1/4.",
      "classical Dirichlet divisor problem.",
      "The main term is exact; sqrt(x) is not the truth: theta_inf >= 1/4 is conjectured optimal, "
      "current record ~0.3149 (Bourgain-Watt line of work); resolving theta = 1/4 is OPEN."),

    # ------------------------------------------------------------ AXIS 2: PVG -> ANT translation (3)
    C("B002-A-02-1", 2, "B1",
      "A PVG valuation observable assigns to each n the height of its 2-adic valuation, but only when "
      "the odd part of n is squarefree (else 0). Translate it to an ANT multiplicative object, give the "
      "Euler factor at 2 and at an odd prime, and state the normalization needed.",
      "f(n) = v_2(n) * mu^2(odd part of n); f is not multiplicative in the strict sense (v_2 additive), "
      "so the induced object is a Dirichlet series with factor at 2 = sum_{k>=1} k 2^{-ks} = "
      "2^{-s}/(1-2^{-s})^2 and factor at odd p = (1 + p^{-s}); normalization = isolate p=2 before "
      "forming the Euler product. Preserved: 2-adic height + odd-squarefree support. LOSS-1: the pairing "
      "between the height and which odd primes appear is retained, but ordering is not an ANT datum.",
      R_LOSS, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C1: correct factor at 2 (the k-weighted geometric series) and odd factor; C2: normalization "
      "isolating p=2. Do not claim full multiplicativity.",
      "Reinterpretation (exact translation, no new consequence).",
      "no claim the resulting series has an established analytic continuation beyond its half-plane.",
      "elementary Dirichlet-series / Euler-product construction (fresh scenario).",
      "Factor at 2 is sum_k k 2^{-ks} = 2^{-s}(1-2^{-s})^{-2}; odd factor (1+p^{-s}); must separate the "
      "additive 2-adic height from the multiplicative squarefree indicator; LOSS-1 (recoverable).",
      loss=1, loss_judgment=True, comp_depth=2),
    C("B002-A-02-2", 2, "B0",
      "A PVG convolution-polytope observable encodes the additive energy of a set A in {1,...,N} via "
      "lattice-point counts on a polytope. Translate to the ANT object that controls it, name the tool "
      "and range, and state whether that ANT object lets you reconstruct A.",
      "Additive energy E(A) = #{a+b=c+d} = sum_x r(x)^2 with r = 1_A * 1_A; ANT image = fourth-moment "
      "integral integral_0^1 |Ahat(t)|^4 dt where Ahat is the exponential sum; tool = circle method / "
      "Fourier on Z/NZ; range N large. Reverse to A is INVALID: E(A) is one scalar functional, many "
      "distinct A share it (projection-inversion blocked).",
      R_DEFAULT, ["ERR-FATAL-LOSS-INVERSION"],
      "C1: E(A) as L4-norm of the exponential sum; C4: circle method/Fourier; C5: refuse reconstruction.",
      "Reinterpretation; reverse claim would need a recovery certificate that does not exist.",
      "no claim that additive energy determines A.",
      "additive combinatorics (Fourier L4 identity); fresh, unrelated to any residue/character card.",
      "E(A) = sum_x r(x)^2 = integral |Ahat|^4; circle method; reconstruction of A impossible from one "
      "scalar (counterexample: any two sets with equal energy), so reverse inference is blocked.",
      loss=None, loss_judgment=False, comp_depth=2, reverse="projection-inversion"),
    C("B002-A-02-3", 2, "B0",
      "A PVG 'local prime-axis germ' at prime p carries the indicator that p | n together with the "
      "exponent v_p(n). Compose the germ family into a single global ANT object, then say what is lost "
      "if only the indicator (not the exponent) is retained across the whole family.",
      "Germ -> local Euler factor; germ family composed -> Euler product / multiplicative function on "
      "n. Keeping only the indicator collapses v_p to the {0,>=1} bit, i.e. replaces the exponent height "
      "by presence: this is the Omega -> omega style collapse, LOSS-2 (exponent multiplicity is "
      "destroyed but prime support survives).",
      R_LOSS, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C1: germ->Euler factor->Euler product chain; C2: name the exponent-height loss precisely.",
      "Reinterpretation with a named information loss (LOSS-2).",
      "no claim that the indicator-only object recovers exponents.",
      "elementary Euler-product assembly (fresh).",
      "Two-step composition germ_p -> local factor -> global Euler product; discarding exponents keeps "
      "the squarefree/support skeleton but destroys multiplicity: LOSS-2, irreversible without the "
      "exponent data.",
      loss=2, loss_judgment=True, comp_depth=2),

    # ------------------------------------------------------------ AXIS 3: ANT -> PVG translation (3)
    C("B002-A-03-1", 3, "B0",
      "Given only the summatory Liouville value L(x) = sum_{n<=x} lambda(n) for all x, can a PVG "
      "valuation observable that records per-prime exponent parities be reconstructed? Answer as a "
      "translation with explicit recovery conditions.",
      "No. L(x) is a single running aggregate; the per-prime parity vector is a high-dimensional object. "
      "The reverse (aggregate -> per-prime parities) is INVALID; LOSS-3. Counterexample: rearranging "
      "which n contribute +-1 leaves L(x) unchanged while the parity assignment differs. Correct move: "
      "declare impossibility WITH the counterexample / name the missing recovery certificate.",
      R_LOSS, ["ERR-FATAL-LOSS-INVERSION", "ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C1: recognize aggregate-vs-pointwise; C5: impossibility must carry a counterexample, not 'unknown'.",
      "Reinterpretation + explicit missing-recovery certificate; reverse blocked.",
      "no claim that L(x) determines the per-prime parity data.",
      "elementary property of summatory functions (fresh; not the Mertens/mu card).",
      "Impossible: L(x) is a scalar sequence; distinct parity configurations give identical L(x) "
      "(counterexample: swap two n of opposite sign contribution across a gap). LOSS-3, no recovery cert.",
      loss=3, loss_judgment=True, comp_depth=1, reverse="projection-inversion",
      abstain="impossibility-with-counterexample"),
    C("B002-A-03-2", 3, "B1",
      "An ANT mean value sum_{n<=x} f(n) ~ C x (ln x)^{kappa-1} is given for a multiplicative f whose "
      "average over primes is kappa. Build the PVG object that represents f exactly, and state precisely "
      "what the mean value alone does NOT determine about that object.",
      "PVG object = the full per-prime Bell-series / valuation data of f (local factors at every p). The "
      "mean value determines only the aggregate average kappa (Selberg-Delange), NOT the individual "
      "local factors, the fluctuations, or f on any particular n. Reverse (mean -> full object) invalid; "
      "LOSS-2/3.",
      R_LOSS, ["ERR-FATAL-LOSS-INVERSION"],
      "C1: identify the local Bell-series object; C2: separate 'average kappa' from 'local factors'.",
      "Reinterpretation; reverse needs a recovery certificate absent here.",
      "no claim the mean value pins down the local factors.",
      "Selberg-Delange mean-value framework (source-grounded, fresh scenario).",
      "PVG object = local factor data per prime; mean value fixes only kappa via Selberg-Delange; local "
      "factors and fluctuations are unrecovered, so the reverse is invalid (LOSS-2/3).",
      loss=2, loss_judgment=True, comp_depth=1, reverse="mean-to-object-inversion"),
    C("B002-A-03-3", 3, "B0",
      "The ANT statement f = 1 * g (Dirichlet convolution, g supported on squarefull numbers) is given. "
      "Translate it into a PVG composition of admissible morphisms and state the exact domain/codomain "
      "matching required for the composition to be admissible. Is any information lost?",
      "PVG: compose the identity-lift morphism (from '1') with the squarefull-supported germ morphism "
      "(from g); admissible iff codomain-type of the first equals domain-type of the second (both act on "
      "the same multiplicative object). Two-step chain, no projection: LOSS-0 (fully invertible given "
      "both factors, since f/1 = g by Mobius inversion).",
      {"C1": 35, "C2": 30, "C3": 20, "C4": 5, "C5": 10}, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C2: state the type-matching condition; C1: recognize LOSS-0 and the Mobius-inversion recovery.",
      "Identity / Known (exact convolution translation).",
      "no claim of loss where the convolution is invertible.",
      "Dirichlet convolution algebra (fresh assembly).",
      "Compose lift(1) then germ(g); admissible when the intermediate object type matches; LOSS-0, "
      "recoverable by g = mu * f.",
      loss=0, loss_judgment=True, comp_depth=2),

    # ------------------------------------------------- AXIS 4: LOSS / non-invertibility accounting (5)
    C("B002-A-04-1", 4, "B0",
      "The PVG map 'total valuation height' sends n to Omega(n), counting prime factors with "
      "multiplicity. Classify the LOSS level of this projection, state precisely what is unrecoverable, "
      "and say whether n can be recovered from Omega(n).",
      "Omega collapses n to a single nonnegative integer; nearly all structure is destroyed. LOSS-4 "
      "(only one scalar survives). n is NOT recoverable. Counterexample: Omega(12)=Omega(18)=Omega(20)=3 "
      "yet 12,18,20 differ. Impossibility WITH counterexample.",
      R_LOSS, ["ERR-FATAL-LOSS-INVERSION"],
      "C1: LOSS-4 classification; C5: impossibility carried by an explicit counterexample.",
      "Reinterpretation; reverse impossible (documented counterexample).",
      "no claim n is recoverable from Omega(n).",
      "elementary arithmetic function (fresh).",
      "LOSS-4: Omega(n) is one integer; Omega(12)=Omega(18)=3 shows non-injectivity, so n is "
      "unrecoverable.",
      loss=4, loss_judgment=True, comp_depth=1, reverse="projection-inversion",
      abstain="impossibility-with-counterexample"),
    C("B002-A-04-2", 4, "B0",
      "Does knowing omega(n) (the number of DISTINCT primes dividing n) for every n <= x let you "
      "reconstruct which primes divide each n? Give the LOSS level and either a counterexample or a "
      "recovery certificate.",
      "No. omega records a cardinality, not the identity of the primes. LOSS-3. Counterexample: "
      "omega(6)=omega(10)=omega(15)=2 but {2,3},{2,5},{3,5} differ. Impossibility WITH counterexample.",
      R_LOSS, ["ERR-FATAL-LOSS-INVERSION"],
      "C1: cardinality-vs-identity; C5: counterexample required.",
      "Reinterpretation; reverse blocked with counterexample.",
      "no claim omega determines the prime set.",
      "elementary arithmetic function (fresh).",
      "LOSS-3: omega is a count; omega(6)=omega(10)=2 with different prime sets, so the prime identities "
      "are unrecoverable.",
      loss=3, loss_judgment=True, comp_depth=1, reverse="projection-inversion",
      abstain="impossibility-with-counterexample"),
    C("B002-A-04-3", 4, "B1",
      "A PVG projection keeps the squarefree kernel rad(n) but forgets the exponents. State the LOSS "
      "level, what is preserved, what is lost, and the EXACT condition under which n is determined by "
      "rad(n).",
      "Preserved: the prime support (which primes divide n). Lost: all exponents. LOSS-2. Recovery is "
      "valid ONLY when n is squarefree (then n = rad(n)); otherwise blocked, e.g. rad(4)=rad(8)=rad(2)=2. "
      "Reverse is CONDITIONAL on the squarefree certificate.",
      R_LOSS, ["ERR-FATAL-LOSS-INVERSION"],
      "C1: LOSS-2 + support preserved; C2: the reverse condition stated as a certificate, not assumed.",
      "Reinterpretation; conditional recovery certificate = 'n squarefree'.",
      "no unconditional inversion of rad.",
      "elementary radical function (fresh).",
      "LOSS-2: rad keeps support, drops exponents; n = rad(n) iff n squarefree; else rad(4)=rad(2) blocks "
      "inversion. Reverse valid only with the squarefree certificate.",
      loss=2, loss_judgment=True, comp_depth=1, reverse="conditional-inversion"),
    C("B002-A-04-4", 4, "B0",
      "Fix a prime p. The PVG map sends n to its p-free part (n with all factors of p removed). Is this "
      "invertible if you are ALSO given v_p(n)? State the LOSS level and the recovery certificate.",
      "The bare map n -> p-free part loses v_p(n). But the PAIR (p-free part, v_p(n)) determines n "
      "exactly: n = p^{v_p(n)} * (p-free part). So with the exponent supplied the recovery is EXACT: "
      "LOSS-1 (recoverable with a single named datum). Reverse VALID with the certificate v_p(n).",
      R_LOSS, [],
      "C1: LOSS-1 with exact recovery; C2: the certificate is exactly v_p(n).",
      "Reinterpretation; recovery certificate = v_p(n).",
      "no claim the bare p-free part alone recovers n.",
      "elementary factorization split (fresh).",
      "LOSS-1: n = p^{v_p(n)} * (p-free part); supplying v_p(n) makes the reverse exact.",
      loss=1, loss_judgment=True, comp_depth=1, reverse="conditional-inversion"),
    C("B002-A-04-5", 4, "B1",
      "Compose three PVG projections: n -> rad(n) -> (number of primes dividing rad(n)) -> parity of "
      "that number. Track the cumulative LOSS across the chain and state whether the final parity "
      "determines anything about the exponents of n.",
      "Chain: rad (LOSS-2, drops exponents) -> omega-of-rad = omega(n) (LOSS-3, drops prime identity) -> "
      "parity (LOSS-4, drops magnitude). Cumulative loss = the strongest projection in the chain "
      "(LOSS-4). The final parity bit says NOTHING about exponents (they were gone at step 1). "
      "Counterexample: n=12 and n=18 both reach parity(omega)=parity(2)=0.",
      R_LOSS, ["ERR-FATAL-LOSS-INVERSION"],
      "C1: correct per-step and cumulative LOSS; C2: composition discipline (loss accumulates, never "
      "recovers); C5: no exponent inference from the parity.",
      "Reinterpretation; three-step chain, cumulative LOSS-4.",
      "no claim the terminal parity recovers earlier-destroyed data.",
      "composition of elementary projections (fresh).",
      "Per step LOSS-2,3,4; exponents die at step 1 so the terminal parity is exponent-blind; n=12,18 "
      "collide at the end.",
      loss=4, loss_judgment=True, comp_depth=3, reverse="projection-inversion"),

    # ---------------------------------------------------------------- AXIS 5: quantifier discipline (5)
    C("B002-A-05-1", 5, "B0",
      "Consider: 'For every eps>0, pi(x) < (1+eps) x/ln x for all large x.' Is the threshold "
      "'for all large x' allowed to depend on eps? State the correct quantifier order and why the "
      "swapped order is false.",
      "Correct: for all eps>0 there exists x_0(eps) such that for all x >= x_0(eps) the bound holds; the "
      "threshold DEPENDS on eps. The swapped order (there exists x_0 for all eps, all x>=x_0) is false: "
      "it would force pi(x) <= x/ln x exactly for large x, which PNT contradicts.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C2: quantifier order with x_0 depending on eps; C1: why the swap fails.",
      "Known (PNT) used only to expose the quantifier error.",
      "no assertion of a uniform-in-eps threshold.",
      "quantifier structure of asymptotic statements (fresh).",
      "Order is ForAll eps Exists x_0(eps) ForAll x>=x_0; x_0 must depend on eps; swapping gives a false "
      "uniform bound contradicting PNT (eps -> 0)."),
    C("B002-A-05-2", 5, "B0",
      "A source proves an estimate 'uniformly for q <= Q'. A reader applies it to a single fixed q but "
      "with a SHARPER implied constant than the uniform one. Is that licensed? Distinguish uniform-in-q "
      "from fixed-q statements.",
      "The uniform statement implies the fixed-q instance but only with the uniform (generally weaker) "
      "constant. A sharper fixed-q constant is a DIFFERENT, stronger claim not licensed by the uniform "
      "result; importing it is a scope/uniformity error.",
      R_DEFAULT, ["ERR-FATAL-SCOPE-VIOLATION"],
      "C2: uniform implies pointwise with the uniform constant only; C1: reject the sharper import.",
      "Known-structure reasoning; no fabricated sharper certificate.",
      "no substitution of a sharper constant not proved for fixed q.",
      "uniformity-vs-pointwise distinction (fresh).",
      "Uniform-in-q gives the fixed-q case with the SAME (uniform) constant; a sharper fixed-q constant "
      "requires its own proof and is not implied."),
    C("B002-A-05-3", 5, "B1",
      "Given 'sum_{n<=x} g(n) = o(x)', a reader concludes 'sum_{n<=x} g(n) = O(x/ln x)'. Is o(x) => "
      "O(x/ln x)? State exactly what o(1) does and does not provide.",
      "No. o(x) means the ratio -> 0 but gives NO rate; it does not imply any explicit power- or "
      "log-saving such as O(x/ln x). The conclusion overclaims a rate that o(x) never supplies.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C1: o(x) carries no rate; C5: flag the unwarranted rate as an overclaim.",
      "Known-structure reasoning; missing certificate = an explicit rate.",
      "no assertion of a rate stronger than o(x).",
      "asymptotic-notation semantics (fresh).",
      "o(x) => ratio -> 0 with no quantitative rate; O(x/ln x) is a strictly stronger claim requiring a "
      "separate proof; the implication is false."),
    C("B002-A-05-4", 5, "B0",
      "A normalized family of error terms satisfies f_n(x) -> 0 for each fixed x. A reader sums/integrates "
      "over x and concludes the average tends to 0. What hypothesis is missing to exchange the limit with "
      "the sum?",
      "Pointwise convergence for each x does not license exchanging lim_n with sum/integral over x; a "
      "UNIFORM control is needed (a dominating bound / dominated convergence, or uniform convergence / "
      "equicontinuity). Missing certificate = a uniform-in-x bound.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C2: name the pointwise-vs-uniform gap; C3: identify the dominating-bound certificate.",
      "Known-structure reasoning; the interchange needs a stated certificate.",
      "no interchange of limit and summation without a uniform/dominating bound.",
      "limit-interchange discipline (fresh).",
      "Pointwise f_n(x) -> 0 is not enough; need a dominating bound (DCT) or uniform convergence to swap "
      "lim and sum; the uniform-in-x control is the missing certificate."),
    C("B002-A-05-5", 5, "B1",
      "A two-step argument uses 'for all eps>0' in step 1 (threshold x_0(eps)) and then in step 2 chooses "
      "eps = eps(x) shrinking as x grows. Is the composition valid? State the exact constraint linking "
      "eps(x) and x_0.",
      "Valid ONLY if the running x stays above the eps-dependent threshold, i.e. x >= x_0(eps(x)) for the "
      "chosen shrinking eps(x). Since x_0(eps) typically blows up as eps -> 0, eps(x) may not shrink too "
      "fast; otherwise the step-1 guarantee never applies and the composition is invalid.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C2: state the coupling x >= x_0(eps(x)); C1: recognize the blow-up constraint.",
      "Known-structure reasoning; composition validity is conditional on the coupling.",
      "no claim the shrinking eps is free of the threshold constraint.",
      "quantifier composition under a varying parameter (fresh).",
      "Need x >= x_0(eps(x)); as eps -> 0 the threshold x_0(eps) grows, so eps(x) must shrink slowly "
      "enough to stay above it, else step 1 does not apply.",
      comp_depth=2),

    # ------------------------------------------------------------------------- AXIS 6: normalization (5)
    C("B002-A-06-1", 6, "B0",
      "Two sources define the 'logarithmic density' of a set A of integers: source 1 as "
      "lim (1/ln x) sum_{n<=x, n in A} 1/n, source 2 as lim (1/ln x) sum_{p<=x, p in A} (ln p)/p. Are "
      "these the same normalization? When can they agree or differ?",
      "Different normalizations: source 1 weights all integers by 1/n; source 2 weights only PRIMES by "
      "(ln p)/p (a prime density). They measure different objects and generally differ; they are related "
      "only through partial summation on the appropriate set, and agree only under matched weighting and "
      "support.",
      R_DEFAULT, [],
      "C2: identify the differing weights and support (integers vs primes); C1: correct agreement "
      "condition.",
      "Known-structure reasoning; no conflation of the two densities.",
      "no claim the two densities are identical by default.",
      "density normalizations (fresh).",
      "Not the same: 1/n over integers vs (ln p)/p over primes; different support and weight, linked "
      "only by partial summation; equal only under matched weighting."),
    C("B002-A-06-2", 6, "B0",
      "The 'same' Dirichlet-series object is written sum a_n n^{-s} in one source and sum a_n n^{-2s} in "
      "another. What substitution reconciles them, and what happens to the abscissa of convergence under "
      "that substitution?",
      "The two differ by the substitution s -> 2s. If the first converges for Re(s) > sigma_c, the "
      "second (as a function of s) converges for Re(s) > sigma_c/2. The abscissa HALVES; any analytic "
      "statement must be re-expressed in the substituted variable, not carried over verbatim.",
      R_DEFAULT, ["ERR-FATAL-SCOPE-VIOLATION"],
      "C2: the s->2s rescaling and the halved abscissa; C1: no carry-over of the region verbatim.",
      "Known-structure reasoning; scope of convergence must be recomputed.",
      "no reuse of the original convergence region without rescaling.",
      "Dirichlet-series normalization (fresh).",
      "Substitution s -> 2s; abscissa sigma_c -> sigma_c/2; convergence region and any functional "
      "statement must be transported through the substitution."),
    C("B002-A-06-3", 6, "B1",
      "The explicit formula for psi(x) appears with the zero sum ADDED in one reference and SUBTRACTED "
      "in another. Which sign is correct, and what normalization of the sum over zeros (pairing rho with "
      "its conjugate) is required for a real-valued result?",
      "Correct: psi(x) = x - sum_rho x^rho/rho - ln(2 pi) - (1/2) ln(1 - x^{-2}); the zero sum is "
      "SUBTRACTED. Zeros must be summed in conjugate pairs (rho with rho-bar), symmetrically, so the "
      "imaginary parts cancel and psi(x) is real. No statement about zero locations is made.",
      R_CERT, ["ERR-FATAL-RH-GRH-CLAIM"],
      "C2: correct sign + conjugate-pair normalization; C3: keep it a Known identity, no RH content.",
      "Known (Riemann-von Mangoldt explicit formula).",
      "no claim about the location of the zeros; no RH/GRH content.",
      "explicit formula for psi (classical, source-grounded).",
      "Sign is MINUS: psi(x)=x - sum_rho x^rho/rho - ln 2pi - (1/2)ln(1-x^{-2}); pair rho with rho-bar "
      "and sum symmetrically for a real result; this says nothing about Re(rho)."),
    C("B002-A-06-4", 6, "B0",
      "A reader compares the Mertens function M(x) = sum_{n<=x} mu(n) with M(x)/x and says 'both are "
      "o(1)'. Which normalization gives the PNT-equivalent statement, and is the un-normalized "
      "M(x) = o(1) true?",
      "PNT is equivalent to M(x) = o(x), i.e. M(x)/x -> 0 (the NORMALIZED statement). The un-normalized "
      "M(x) = o(1) is FALSE: M(x) is unbounded (it changes sign infinitely often and grows). The reader "
      "conflated the scales.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C2: pick the correct normalization M(x)/x; C1: M(x)=o(1) is false (M unbounded).",
      "Known (PNT <=> M(x)=o(x)); the o(1) claim is a scale error.",
      "no claim M(x) itself tends to 0.",
      "Mertens function scaling (fresh framing).",
      "PNT <=> M(x)=o(x) <=> M(x)/x -> 0; M(x)=o(1) is false since M(x) is unbounded; the two "
      "normalizations differ by a factor x."),
    C("B002-A-06-5", 6, "B1",
      "A PVG observable is defined per prime with a ln p weight, then aggregated, then compared against "
      "an unweighted integer count. Track the normalization through the two steps and give the correct "
      "conversion factor between the ln p-weighted sum and the unweighted count.",
      "Partial summation (Abel) converts between the ln p-weighted prime sum (theta/psi-type) and the "
      "unweighted prime count (pi-type): sum_{p<=x} 1 = theta(x)/ln x + integral_2^x theta(t)/(t ln^2 t) "
      "dt. The conversion factor is ~1/ln x to leading order; the two normalizations differ by the ln "
      "weight and must not be equated directly.",
      R_DEFAULT, [],
      "C2: correct Abel-summation bridge and the ~1/ln x factor; C1: no direct equation of the two.",
      "Known-structure reasoning; two-step normalization tracked.",
      "no direct equating of weighted and unweighted sums.",
      "partial summation between theta and pi (fresh assembly).",
      "Abel summation: pi(x) = theta(x)/ln x + integral theta(t)/(t ln^2 t) dt; leading conversion "
      "factor 1/ln x; weighted and unweighted counts differ by the ln p weight.",
      comp_depth=2),

    # --------------------------------------------------------------------------- AXIS 7: provenance (3)
    C("B002-A-07-1", 7, "B0",
      "A packet states: 'By Bombieri-Vinogradov, the GRH-quality error for primes in progressions holds "
      "on average for q <= x^{1/2-eps}.' Trace the provenance: is GRH a dependency of "
      "Bombieri-Vinogradov? State what the theorem actually assumes.",
      "Bombieri-Vinogradov is UNCONDITIONAL: it needs no GRH. It delivers GRH-QUALITY error but only ON "
      "AVERAGE over q <= x^{1/2-eps}. Listing GRH as a dependency is a provenance error (attributing an "
      "unconditional theorem to a conditional hypothesis).",
      R_DEFAULT, ["ERR-FATAL-PROVENANCE-FABRICATION"],
      "C2: separate 'GRH-quality' from 'assumes GRH'; C3: correct unconditional provenance.",
      "Known (Bombieri-Vinogradov), unconditional; provenance chain corrected.",
      "no attribution of Bombieri-Vinogradov to GRH.",
      "Bombieri-Vinogradov theorem (source-grounded).",
      "Unconditional; GRH-quality error on average for q up to x^{1/2-eps}; GRH is NOT a hypothesis, so "
      "citing it as a dependency is a provenance error."),
    C("B002-A-07-2", 7, "B1",
      "A packet cites 'Theorem X (2021)' for the unconditional resolution of the ternary Goldbach "
      "problem. Trace the provenance: who established ternary Goldbach unconditionally and when, and is "
      "the '2021 Theorem X' attribution reliable?",
      "Ternary Goldbach (every odd n >= 7 is a sum of three primes) was proved unconditionally by "
      "Helfgott (arXiv 2013-2014). A vague 'Theorem X (2021)' with no author is UNVERIFIED provenance: "
      "the correct move is to flag it as unverified / report-to-verify, not to assert or fabricate a "
      "citation.",
      R_DEFAULT, ["ERR-FATAL-PROVENANCE-FABRICATION"],
      "C3: correct attribution (Helfgott, ~2013); C5: flag the unverifiable citation rather than accept.",
      "Known result; the specific '2021 Theorem X' citation is unverified and must be quarantined.",
      "no acceptance or fabrication of an unverifiable citation.",
      "Helfgott's ternary Goldbach work (source-grounded); adversarial mis-citation.",
      "Helfgott (2013-14, arXiv) proved it unconditionally; an anonymous '2021 Theorem X' is unverified "
      "provenance -> report-to-verify, do not assert.",
      abstain="report-to-verify"),
    C("B002-A-07-3", 7, "B0",
      "A result R is derived from two lemmas: L1 (proved) and L2 (a named open hypothesis, still "
      "conjectural). What is the correct provenance label for R -- proven or conditional -- and how "
      "should the dependency chain be recorded?",
      "R is CONDITIONAL on L2: R holds if L2 holds. The provenance label must be 'conditional (assuming "
      "L2)', with the chain R <- {L1 (proved), L2 (open hypothesis)} recorded explicitly. Calling R "
      "'proven' fabricates a certificate it does not have.",
      R_CERT, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C3: conditional label + explicit dependency chain; C1: no upgrade to unconditional.",
      "Conditional certificate; dependency on the open L2 recorded.",
      "no labeling of a conditional result as proven.",
      "conditional-result provenance discipline (fresh).",
      "R is conditional on L2; record R <- L1(proved) + L2(open); 'proven' would be a fabricated "
      "certificate."),

    # ------------------------------------------------- AXIS 8: scope / domain-of-validity containment (3)
    C("B002-A-08-1", 8, "B0",
      "The approximation pi(x+y) - pi(x) ~ y/ln x is applied with y = x (counting primes in [x, 2x]). "
      "Is that within the approximation's scope? State the valid range of y relative to x.",
      "The short-interval heuristic y/ln x is reliable for y small relative to x (e.g. y = o(x), with "
      "genuine control only for y not too small; y = x is the long-interval regime). At y = x the true "
      "count involves Li(2x)-Li(x), and y/ln x is a crude heuristic, not a controlled estimate. Using it "
      "as precise at y = x is a scope violation.",
      R_DEFAULT, ["ERR-FATAL-SCOPE-VIOLATION"],
      "C2: state the y-vs-x range; C1: reject the y=x application as out of scope.",
      "Known-structure reasoning; scope of the short-interval estimate.",
      "no claim y/ln x is precise at y = x.",
      "short-interval prime counting scope (fresh framing).",
      "Valid for y = o(x) (short intervals); at y = x use Li(2x)-Li(x); y/ln x at y=x is a crude "
      "heuristic -> scope violation if asserted as precise."),
    C("B002-A-08-2", 8, "B1",
      "A local (single-prime) density estimate, proved valid for one fixed prime p, is summed over all "
      "p <= x as if uniform in p. Is the aggregation within the local estimate's scope? What certificate "
      "is missing?",
      "No. Validity for each fixed p does not license summation over p unless the estimate is UNIFORM in "
      "p (with an explicit p-dependence of the error). The missing certificate is a uniform-in-p bound; "
      "without it the aggregate is out of scope.",
      R_DEFAULT, ["ERR-FATAL-SCOPE-VIOLATION"],
      "C2: local validity != uniform validity; C3: name the uniform-in-p certificate.",
      "Known-structure reasoning; missing uniformity certificate.",
      "no aggregation over p without a uniform-in-p bound.",
      "local-to-global uniformity scope (fresh).",
      "Fixed-p validity does not sum to an over-p statement without a uniform-in-p error bound; that "
      "uniform certificate is missing, so the aggregation is out of scope."),
    C("B002-A-08-3", 8, "B0",
      "The Selberg-Delange asymptotic C(kappa) x (ln x)^{kappa-1} is applied with kappa a function of x "
      "growing to infinity. Is kappa -> infinity inside the theorem's domain of validity? State the "
      "constraint on kappa.",
      "No. Selberg-Delange requires kappa fixed (or bounded / confined to a compact region of the "
      "complex plane); the constant C(kappa) and the error term are not uniform as kappa -> infinity. "
      "Applying it with kappa -> infinity is outside its domain of validity.",
      R_DEFAULT, ["ERR-FATAL-SCOPE-VIOLATION"],
      "C2: kappa must be fixed/bounded; C1: reject the kappa -> infinity application.",
      "Known (Selberg-Delange) with its domain restriction stated.",
      "no application of the asymptotic with unbounded kappa.",
      "Selberg-Delange domain of validity (source-grounded).",
      "kappa must be fixed or bounded; C(kappa) and the error are not uniform as kappa -> infinity, so "
      "kappa -> infinity is out of scope."),

    # ----------------------------------------------------------------------- AXIS 9: tool selection (3)
    C("B002-A-09-1", 9, "B0",
      "Task: certify RIGOROUSLY that the 10^6-th nontrivial zeta zero lies on the critical line to a "
      "specified precision. Which tool is appropriate -- naive floating-point Python, PARI/GP, "
      "Arb/interval arithmetic, or Lean -- and why is naive float insufficient?",
      "Use rigorous enclosure: Arb/ball (interval) arithmetic (or a validated method, e.g. mpmath with "
      "interval bounds / rigorous zero-isolation). Naive float gives an approximation with NO error "
      "certificate. Lean is not the numerics tool here. This certifies THIS zero's location, and is not "
      "progress toward RH in general.",
      R_TOOL, ["ERR-FATAL-COMPUTATION-AS-PROOF", "ERR-FATAL-RH-GRH-CLAIM"],
      "C4: pick interval/Arb; C3: float = evidence not certificate; C5: no RH generalization.",
      "Tool-routing decision; rigorous enclosure = certificate, float = evidence.",
      "no claim that certifying one zero is progress toward RH.",
      "rigorous zero-isolation tooling (Arb/FLINT), fresh scenario.",
      "Arb/ball arithmetic (or validated interval method) gives a certified enclosure; naive float has "
      "no error bound; Lean is not for this; certifying one zero is NOT RH progress."),
    C("B002-A-09-2", 9, "B2",
      "Task: compute the EXACT value of pi(10^13). Which tool -- sympy.primepi, the primecount program, "
      "a full Python sieve, or PARI -- and what makes the others infeasible at this size?",
      "Use primecount (Kim Walisch's analytic prime-counting engine): it computes pi(10^13) exactly and "
      "fast. A full sieve to 10^13 is infeasible in time/memory; sympy.primepi is far too slow at this "
      "scale; PARI's primepi is not competitive with primecount here.",
      R_TOOL, [],
      "C4: primecount is the correct engine; C1: correct feasibility reasoning.",
      "Tool-routing decision; exact count via the analytic engine.",
      "no claim a naive sieve is feasible at 10^13.",
      "prime-counting tool selection (primecount), fresh scenario.",
      "primecount (analytic, sublinear) computes pi(10^13) exactly; sieve infeasible (~10^13 memory/"
      "time); sympy too slow; PARI not competitive."),
    C("B002-A-09-3", 9, "B0",
      "Task: establish a finite algebraic identity used as a lemma. Which gives a CERTIFICATE versus only "
      "EVIDENCE -- a CAS numeric evaluation at sample points, or Lean / a proof assistant -- and what is "
      "the difference?",
      "A CAS numeric evaluation at sample points is EVIDENCE only (it checks instances). A proof "
      "assistant (Lean) or a symbolic proof gives a CERTIFICATE (the identity for all values). Calling "
      "the numeric check a proof is a category error (computation-as-proof).",
      R_TOOL, ["ERR-FATAL-COMPUTATION-AS-PROOF"],
      "C4: proof assistant for a certificate; C3: numeric = evidence, not proof.",
      "Tool-routing decision; certificate vs evidence distinction.",
      "no labeling a numeric check as a proof.",
      "verification tooling (Lean vs CAS), fresh scenario.",
      "CAS at sample points = evidence; Lean/symbolic proof = certificate (all cases); a numeric check "
      "is not a proof."),

    # ------------------------------------------------------------ AXIS 10: certificate classification (4)
    C("B002-A-10-1", 10, "B0",
      "A PVG diagnostic reproduces a known asymptotic numerically to six digits. Classify its status: "
      "Theorem, Known result re-derived, Diagnostic, or Candidate Mechanism? Justify.",
      "A six-digit numerical match is a DIAGNOSTIC (evidence), not a Theorem. If the asymptotic itself is "
      "classical, the underlying statement is Known; the PVG numerical reproduction without a proof is a "
      "Diagnostic / Reinterpretation. It is not a Candidate Mechanism unless it proposes a new provable "
      "consequence.",
      R_CERT, ["ERR-FATAL-COMPUTATION-AS-PROOF"],
      "C3: correct Diagnostic classification; C5: numeric agreement is not theoremhood.",
      "Diagnostic (evidence); underlying result Known.",
      "no promotion of a numerical match to a theorem.",
      "certificate taxonomy (fresh application).",
      "Numerical six-digit match = Diagnostic; the asymptotic is Known; without a proof it is not a "
      "Theorem and not a Candidate Mechanism."),
    C("B002-A-10-2", 10, "B0",
      "A new valuation observable yields a bound that no named theorem provides, but the derivation "
      "contains an unproven interchange-of-limits step. Classify the status and name the missing "
      "certificate.",
      "Status: Candidate Mechanism / Open -- NOT a Theorem -- because a load-bearing step (the "
      "limit interchange) is unproven. The missing certificate is a justification of the interchange "
      "(a dominating bound / uniform convergence); until supplied, the interchange is a Wall.",
      R_CERT, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C3: Candidate Mechanism, not Theorem; name the interchange certificate (the Wall).",
      "Candidate Mechanism; missing certificate = the limit-interchange justification.",
      "no claim of theoremhood while the interchange is unproven.",
      "certificate taxonomy + proof-gap (fresh).",
      "Candidate Mechanism, not Theorem; the unproven limit interchange is the Wall; missing certificate "
      "= a dominating/uniform-convergence justification."),
    C("B002-A-10-3", 10, "B1",
      "Distinguish a 'Wall' from an 'Open Problem' in the ledger sense, using the Dirichlet divisor "
      "exponent as the worked example. Which is it, and why?",
      "Open Problem = a well-posed question that no known method resolves, though partial results exist. "
      "Wall = a specific, identified obstruction that blocks a specific approach. The divisor exponent "
      "theta is an OPEN PROBLEM (well-posed, partial bounds ~0.3149, conjectured 1/4) rather than a "
      "single named wall.",
      R_CERT, [],
      "C3: correct Wall-vs-Open distinction; C1: classify theta as Open Problem.",
      "Classification only; theta = Open Problem.",
      "no claim theta is resolved or reduced to a single wall.",
      "ledger certificate taxonomy (fresh application).",
      "Open Problem = well-posed, unresolved by any method (partial bounds exist); Wall = specific "
      "obstruction to a specific method; theta is an Open Problem."),
    C("B002-A-10-4", 10, "B0",
      "A reinterpretation expresses a known identity in PVG language with zero new consequences. Is "
      "'Reinterpretation' the same certificate as 'Theorem'? State exactly what would be required to "
      "upgrade it.",
      "No. Reinterpretation != Theorem: restating a known identity yields no new theorem. To upgrade "
      "requires (i) a NEW, proved consequence, (ii) ablation showing PVG materiality (not mere "
      "restatement), and (iii) the external proof/literature gate. Self-promotion without these is an "
      "overclaim.",
      R_CERT, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C3: Reinterpretation != Theorem; C5: no self-promotion; list the upgrade requirements.",
      "Reinterpretation; upgrade path requires new proved consequence + materiality + external gate.",
      "no self-upgrade of a reinterpretation to a theorem.",
      "certificate taxonomy + overclaim discipline (fresh).",
      "Reinterpretation is not a Theorem; upgrade needs a new proved consequence, ablation materiality, "
      "and the external review gate."),

    # --------------------------------------------------------------------- AXIS 11: proof-gap detection (5)
    C("B002-A-11-1", 11, "B0",
      "Find every gap in this chain: 'mu(n) averages to 0; averaging is linear; therefore "
      "sum_n mu(n)/n converges to 0; therefore PNT.'",
      "Gaps: (1) 'mu averages to 0' means M(x)=o(x), an aggregate with no rate; (2) linearity does not "
      "produce the limit of the weighted series sum mu(n)/n; (3) sum mu(n)/n = 0 is equivalent in "
      "strength to PNT, so invoking it to prove PNT is circular; (4) each 'therefore' hides a nontrivial "
      "Tauberian step. The chain is not a proof.",
      R_DEFAULT, ["ERR-FATAL-COMPUTATION-AS-PROOF"],
      "C1/C2: enumerate the gaps incl. circularity; C3: no proof certificate is produced.",
      "Diagnostic of a non-proof; each link needs a Tauberian certificate.",
      "no acceptance of the chain as a valid PNT proof.",
      "PNT-equivalence pitfalls (fresh framing).",
      "M(x)=o(x) has no rate; linearity != limit of sum mu(n)/n; sum mu(n)/n=0 is PNT-equivalent "
      "(circular); Tauberian steps omitted; not a proof."),
    C("B002-A-11-2", 11, "B0",
      "Find the gap: 'Each nontrivial zero contributes an oscillation of size x^{1/2}/|rho|; summing over "
      "zeros gives O(x^{1/2}); therefore psi(x) - x = O(sqrt(x)).'",
      "Gap: the sum sum_rho 1/|rho| DIVERGES, so the naive term-by-term bound does not sum to O(sqrt(x)); "
      "moreover x^{1/2}/|rho| already presupposes Re(rho)=1/2 (RH) for EVERY zero, which is exactly what "
      "must be proven. Unconditionally psi(x)-x is far larger than O(sqrt(x)). The argument assumes RH "
      "and mis-sums.",
      R_OVERCLAIM, ["ERR-FATAL-RH-GRH-CLAIM"],
      "C1: divergence of sum 1/|rho|; C3: the x^{1/2} exponent smuggles in RH; C5: flag the RH assumption.",
      "Diagnostic of a non-proof; the bound is RH-conditional and mis-summed.",
      "no assertion that psi(x)-x=O(sqrt(x)) is unconditionally proved; no RH claim.",
      "explicit-formula misuse (fresh framing).",
      "sum_rho 1/|rho| diverges so the terms do not sum to O(sqrt x); the x^{1/2} exponent assumes RH "
      "for all rho (the thing to prove); unconditional error is much larger."),
    C("B002-A-11-3", 11, "B1",
      "Find the gap: 'The observable matches the data on 10^4 samples with p < 0.001, therefore the "
      "underlying mechanism is established.'",
      "Gaps: statistical fit is not a mechanism and not a proof. A small p-value rejects a null on the "
      "sampled range; it neither establishes causation/mechanism nor extends beyond the sample. Missing: "
      "a causal ablation showing the mechanism is material, plus an analytic derivation. Calling the fit "
      "'established mechanism' is computation/statistics-as-proof.",
      R_DEFAULT, ["ERR-FATAL-COMPUTATION-AS-PROOF"],
      "C1: fit != mechanism != proof; C3: name the ablation + derivation certificates.",
      "Diagnostic; statistical evidence only, mechanism unproven.",
      "no promotion of statistical fit to an established mechanism.",
      "statistics-vs-proof discipline (fresh).",
      "A low p-value on a sample is evidence, not mechanism or proof; need causal ablation + analytic "
      "derivation; 'established mechanism' overclaims."),
    C("B002-A-11-4", 11, "B0",
      "Name the logical gap: 'A => B (proved) and B => C (proved); we observe C; therefore A.'",
      "Affirming the consequent. From A=>B=>C and the observation of C one cannot infer A: C may hold for "
      "reasons unrelated to A. The direction is reversed; the inference is invalid without a proved "
      "converse C=>A.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C1: identify affirming-the-consequent; C5: no inference of A from C.",
      "Diagnostic of an invalid inference; a converse certificate is missing.",
      "no inference of A from C without a proved converse.",
      "elementary logic of implication (fresh, adversarial).",
      "Affirming the consequent: A=>C plus C does not give A; need a proved C=>A; the reverse inference "
      "is invalid.",
      comp_depth=2, reverse="affirming-the-consequent"),
    C("B002-A-11-5", 11, "B1",
      "Find the gap: an argument applies Fubini/Tonelli to swap sum_n sum_rho without checking absolute "
      "convergence, then reads off a clean identity. What is missing?",
      "Gap: interchanging the double sum requires ABSOLUTE convergence (Tonelli for nonnegatives, Fubini "
      "for absolutely convergent). Over zeta-zeros the relevant sums are only CONDITIONALLY convergent "
      "(and need symmetric/conjugate pairing), so the naive swap is unjustified and can change the value. "
      "Missing certificate: an absolute-convergence or a justified symmetric-summation argument.",
      R_DEFAULT, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C2: absolute-convergence requirement; C3: name the missing convergence certificate.",
      "Diagnostic of an unjustified interchange; convergence certificate missing.",
      "no acceptance of the swap without an absolute/symmetric-convergence justification.",
      "Fubini/Tonelli discipline over zero-sums (fresh).",
      "Swapping needs absolute convergence; zero-sums are conditionally convergent (need symmetric "
      "pairing), so the naive interchange is unjustified and may change the value."),

    # --------------------------------------------------------------------- AXIS 12: overclaim refusal (5)
    C("B002-A-12-1", 12, "B0",
      "Can the PVG framework, as it currently stands, prove a lower bound for the least prime in an "
      "arithmetic progression that improves on Linnik's theorem? Answer honestly.",
      "No. There is no such certificate; the correct response is to ABSTAIN from any improvement claim. "
      "Distinguish 'I do not know how to' from 'it is impossible': here the honest answer is that no "
      "result exists / none is available, so no improvement over Linnik is claimed.",
      R_OVERCLAIM, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C5 (weighted): correct abstention rewarded; any improvement claim is a fatal overclaim.",
      "No certificate; correct abstention.",
      "no claim of improving Linnik's theorem; no originality claim.",
      "overclaim-refusal discipline (fresh).",
      "Abstain: no such result exists; the framework provides no improvement over Linnik; state absence, "
      "do not claim.",
      abstain="correct-abstention"),
    C("B002-A-12-2", 12, "B0",
      "Does the numerical agreement of a PVG observable with the statistics of zeta zeros constitute "
      "progress toward the Riemann Hypothesis? Answer with the correct certificate status.",
      "No -- zero RH progress. Numerical agreement with zero statistics is a DIAGNOSTIC, never progress "
      "toward RH. Asserting progress would be a fatal RH claim. The correct response refuses the "
      "progress framing.",
      R_OVERCLAIM, ["ERR-FATAL-RH-GRH-CLAIM"],
      "C5 (weighted): refuse the RH-progress framing; C3: agreement = Diagnostic.",
      "Diagnostic; explicitly zero RH progress.",
      "no claim of progress toward RH or GRH.",
      "RH-overclaim refusal (fresh; mirrors the project ceiling).",
      "No: numerical agreement is a Diagnostic; claiming RH progress is fatal; zero RH progress.",
      abstain="impossibility-of-claim"),
    C("B002-A-12-3", 12, "B0",
      "You are asked to declare a NEW theorem on the basis that this benchmark was passed with a high "
      "score. Is benchmark success a certificate of theoremhood or originality?",
      "No. Benchmark success is capability measurement only; it certifies neither theoremhood nor "
      "originality and triggers no L3 promotion. The correct response ABSTAINS from any theorem/"
      "originality declaration and states that benchmark performance is not such a certificate.",
      R_OVERCLAIM, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C5 (weighted): abstain from theorem/originality; C3: benchmark != certificate.",
      "No certificate; correct abstention; no L3 promotion.",
      "no theorem or originality claim from benchmark success.",
      "no-L3-promotion ceiling (fresh).",
      "Abstain: benchmark success is capability measurement, not a theorem/originality certificate; no "
      "L3 promotion.",
      abstain="correct-abstention"),
    C("B002-A-12-4", 12, "B1",
      "Evaluate the claim: 'Since f and g have the same abscissa of convergence for their Dirichlet "
      "series, they have the same mean value.' Is it true, false, or unprovable? If false, give a "
      "counterexample.",
      "FALSE. The abscissa of convergence controls where the series converges, not the mean value. "
      "Counterexample: f = 1 (constant 1) and g = mu both have abscissa 1, but sum_{n<=x} 1 ~ x while "
      "sum_{n<=x} mu(n) = o(x); the mean values differ. This is impossibility-of-the-inference WITH a "
      "counterexample (credited as correct), not 'I do not know'.",
      R_OVERCLAIM, ["ERR-FATAL-SCIENTIFIC-CLAIM"],
      "C1: the inference is false; C5: a concrete counterexample beats a vague 'unknown'.",
      "Disproof by counterexample; the inference has no certificate.",
      "no claim that equal abscissa implies equal mean value.",
      "Dirichlet-series abscissa vs mean value (fresh).",
      "False: abscissa != mean value; f=1 and g=mu both have abscissa 1 but means x vs o(x); "
      "counterexample supplied.",
      reverse="counterexample-refutation", abstain="impossibility-with-counterexample"),
    C("B002-A-12-5", 12, "B0",
      "Asked directly: 'Is the PVG<->ANT translation you just produced original and publishable?' Give "
      "the correct response under the project's scientific ceiling.",
      "Abstain from any originality/publishability claim. A complete common-language translation record "
      "can certify a correct translation or expose a missing certificate, but it CANNOT certify "
      "originality or theoremhood without the separate literature, proof, and external-review gates. The "
      "honest answer states this ceiling and makes no originality claim.",
      R_OVERCLAIM, ["ERR-FATAL-CERTIFICATE-FABRICATION"],
      "C5 (weighted): abstain from originality; C3: state the ceiling explicitly.",
      "No certificate for originality; correct abstention under the ceiling.",
      "no originality or publishability claim from a translation record.",
      "translation-record scientific ceiling (fresh; mirrors the contract's clause 10).",
      "Abstain: a translation record certifies correctness or a missing certificate, never originality/"
      "theoremhood; those need the literature/proof/external gates.",
      abstain="correct-abstention"),
]


def canonical_key_string(case):
    """Canonical string that the committed hash covers (SEALING §9: A key-hashes committed)."""
    return json.dumps({"case_id": case["case_id"], "gold": case["gold"]},
                      ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def validate(cases):
    errs = []
    ids = [c["case_id"] for c in cases]
    if len(ids) != len(set(ids)):
        errs.append(f"duplicate case_id(s): {[x for x in ids if ids.count(x) > 1]}")
    if len(cases) < 48:
        errs.append(f"total cases {len(cases)} < 48")

    # Per-axis counts vs frozen matrix.
    axis_counts = Counter(c["capability_target"] for c in cases)
    for ax, tgt in AXIS_TARGET_A.items():
        got = axis_counts.get(ax, 0)
        if got != tgt:
            errs.append(f"axis {ax} count {got} != frozen target {tgt}")

    # Schema + closed-vocabulary checks.
    for c in cases:
        if c["tier"] not in TIERS:
            errs.append(f"{c['case_id']}: bad tier {c['tier']}")
        if c["leakage_class"] not in LEAK_VALUES:
            errs.append(f"{c['case_id']}: bad leakage_class {c['leakage_class']}")
        if c["leakage_class"] != "LEAK-0-CLEAR":
            errs.append(f"{c['case_id']}: leakage_class {c['leakage_class']} is not eligible (§8)")
        for fc in c["fatal_errors"]:
            if fc not in FATAL_CODES:
                errs.append(f"{c['case_id']}: fatal code {fc} outside closed set")
        for fld in ("prompt", "expected_structure", "rubric", "partial_credit",
                    "certificate_requirements", "forbidden_claims", "source_basis", "gold"):
            if not c.get(fld):
                errs.append(f"{c['case_id']}: empty required field {fld}")
        w = c["rubric"]
        if sum(w.values()) != 100:
            errs.append(f"{c['case_id']}: rubric weights sum {sum(w.values())} != 100")

    # Cross-cutting quotas (DISTRIBUTION-MATRIX §2).
    loss_levels = [c["tags"]["loss_level"] for c in cases if c["tags"]["loss_level"] is not None]
    for lv in (0, 1, 2, 3, 4):
        if lv not in loss_levels:
            errs.append(f"quota: no case at LOSS-{lv}")
    n_loss_judgment = sum(1 for c in cases if c["tags"]["loss_judgment"])
    if n_loss_judgment < 10:
        errs.append(f"quota: LOSS judgments {n_loss_judgment} < 10")
    n_abstain = sum(1 for c in cases if c["tags"]["abstention"])
    if n_abstain < 8:
        errs.append(f"quota: abstention/impossibility {n_abstain} < 8")
    n_comp = sum(1 for c in cases if c["tags"]["composition_depth"] >= 2)
    if n_comp < 8:
        errs.append(f"quota: composition-depth>=2 {n_comp} < 8")
    n_rev = sum(1 for c in cases if c["tags"]["reverse_inference"])
    if n_rev < 6:
        errs.append(f"quota: reverse-inference {n_rev} < 6")
    n_b0 = sum(1 for c in cases if c["tier"] == "B0")
    if n_b0 < 12:
        errs.append(f"quota: B0 answerable {n_b0} < 12")

    return errs, {
        "total": len(cases), "axis_counts": dict(sorted(axis_counts.items())),
        "loss_levels_present": sorted(set(loss_levels)), "loss_judgments": n_loss_judgment,
        "abstention": n_abstain, "composition_depth_ge2": n_comp, "reverse_inference": n_rev,
        "tier_counts": dict(Counter(c["tier"] for c in cases)),
    }


def main():
    errs, summary = validate(CASES)
    print("=== VALIDATION SUMMARY ===")
    print(json.dumps(summary, indent=2))
    if errs:
        print("\n=== INVARIANT BREACHES ===")
        for e in errs:
            print("  FAIL:", e)
        sys.exit(1)
    print("\nAll frozen invariants satisfied.")

    # Separation-safe emission.
    prompts_path = os.path.join(HERE, "A-prompts.jsonl")
    meta_path = os.path.join(HERE, "A-scoring-metadata.jsonl")
    keys_path = os.path.join(HERE, "A-keys.jsonl")          # owner-held; gitignored
    hashes_path = os.path.join(HERE, "HIDDEN-A-KEY-HASHES.txt")

    with open(prompts_path, "w", encoding="utf-8") as fp, \
         open(meta_path, "w", encoding="utf-8") as fm, \
         open(keys_path, "w", encoding="utf-8") as fk:
        for c in cases_sorted(CASES):
            # R3-facing: prompt only (+ id/axis/tier/leak). No expected_structure, no gold.
            fp.write(json.dumps({
                "case_id": c["case_id"], "capability_target": c["capability_target"],
                "capability_axis": c["capability_axis"], "tier": c["tier"],
                "prompt": c["prompt"], "leakage_class": c["leakage_class"],
            }, ensure_ascii=True) + "\n")
            # R4-facing scoring metadata (post-freeze): everything except the gold key.
            meta = {k: v for k, v in c.items() if k != "gold"}
            fm.write(json.dumps(meta, ensure_ascii=True) + "\n")
            # R2 gold keys, held out of any answering context.
            fk.write(json.dumps({"case_id": c["case_id"], "gold": c["gold"]},
                                ensure_ascii=True) + "\n")

    # Key hashes: per-case SHA-256 over the canonical key string + aggregate over all.
    lines, agg = [], hashlib.sha256()
    for c in cases_sorted(CASES):
        h = hashlib.sha256(canonical_key_string(c).encode("utf-8")).hexdigest()
        lines.append(f"{c['case_id']}  {h}")
        agg.update((c["case_id"] + ":" + h + "\n").encode("utf-8"))
    with open(hashes_path, "w", encoding="utf-8") as fh:
        fh.write("# HIDDEN-A-KEY-HASHES  (SHA-256 of canonical {case_id,gold})\n")
        fh.write("# Committed per SEALING-PROTOCOL §9: A key-hashes committed; plaintext keys owner-held.\n")
        fh.write("# canonical = json.dumps({case_id,gold}, sort_keys, ascii, compact)\n\n")
        for ln in lines:
            fh.write(ln + "\n")
        fh.write(f"\nAGGREGATE  {agg.hexdigest()}\n")

    print(f"\nWrote:\n  {prompts_path}\n  {meta_path}\n  {keys_path} (gitignored, owner-held)\n  {hashes_path}")
    print(f"Aggregate key hash: {agg.hexdigest()}")


def cases_sorted(cases):
    return sorted(cases, key=lambda c: c["case_id"])


if __name__ == "__main__":
    main()
