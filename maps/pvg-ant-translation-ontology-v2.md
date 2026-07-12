# PVG–ANT Translation Ontology v2

**Program:** `PVG-ANT-CENTRAL-MIND-MATURATION-002`  
**Pass:** `TRANSLATION-KERNEL-V2-PASS-001`  
**Role:** operational ontology; no new research front.

## 1. Translation object

A translation record is not a synonym pair. It is a typed map

\[
(\text{PVG object},\ \text{retained labels},\ \text{scope})
\longleftrightarrow
(\text{ANT object},\ \text{analytic tool},\ \text{certificate}),
\]

together with an explicit information-loss statement.

Every usable record must answer:

1. What is the exact forward translation?
2. What can be translated back?
3. What information is preserved?
4. What information is lost?
5. Which ANT tools are compatible?
6. Which wall remains?
7. Which certificate is required before theorem use?
8. Which finite example and counterexample test the claim?

## 2. Domains

### 2.1 Geometry–arithmetic structure

Prime support, exponent heights, logarithmic mass, divisor boxes,
margins, faces, powerful support, and valuation decompositions.

### 2.2 Local analytic structure

Prime-power axis values, Bell series, first nonzero local layers, pole
orders, and residual Euler-product cancellation.

### 2.3 Transform layer

Smooth logarithmic half-spaces route to Mellin inversion. Hard
boundaries route to Perron, Tauberian, or desmoothing certificates.
The two normalizations must never be conflated.

### 2.4 Residue layer

Residue fibers require labeled primes modulo \(q\). Full character
coordinates preserve a fiber function; energies and moments lose phase.

### 2.5 Sieve layer

Pointwise truncated divisibility data and aggregate divisor sums are
different objects. Level, remainder norm, target purity, sign, and
bilinear cancellation must remain separate.

### 2.6 Probabilistic layer

Separable coordinate sums may route to additive-function models.
Density statements and weighted averages require separate tail
certificates.

## 3. Information-loss classes

`LOSS-0 EXACT-LABELED`  
The map is invertible while labeled prime coordinates and all local
values are retained.

`LOSS-1 SUMMARY`  
Only a statistic such as \(\omega(n)\), \(\tau(n)\), total logarithmic
mass, or a specialization of a generating polynomial remains.

`LOSS-2 AGGREGATION`  
A population of pointwise profiles is pushed to moments such as
\(A_d\), variances, or character energies.

`LOSS-3 PHASE-SIGN`  
Magnitude, support, or energy remains but sign, phase, or individual
Fourier coordinates are lost.

`LOSS-4 ANALYTIC-CERTIFICATE`  
The coefficient geometry is known, but continuation, growth, zero-free
information, cancellation, boundary control, or an error term is absent.

A card can involve more than one loss class. The registry uses prose
rather than pretending that one scalar loss score is sufficient.

## 4. Direction types

- `bidirectional`: a controlled reverse map is available.
- `pvg_to_ant`: PVG selects or simplifies an ANT object, but the reverse
  object is not unique.
- `ant_to_pvg`: an ANT data product can be interpreted geometrically,
  usually with a nontrivial kernel.

Direction does not imply theorem strength.

## 5. Maturity

`L1` — exact encoding or expository normalization.

`L2` — structural or analytic routing with a named loss and certificate.

`L3` — a reusable transfer principle proved at the stated generality.

Pass 001 makes no L3 promotion. One-Theorem 001 is an internally proved
instance, not a general Translation Kernel v2 theorem.

## 6. Problem-translator procedure

Given a new arithmetic object or sum:

```text
A. Identify the raw object.
B. Decide whether it depends on support, heights, labels, order, phase,
   residue, or interactions.
C. Test multiplicativity or additivity.
D. Compute prime-power axis data when meaningful.
E. Choose the matching translation cards.
F. Intersect their preserved-information sets.
G. Union their loss and wall sets.
H. Select an ANT tool only if its hypotheses can be named.
I. Name the exact missing certificate.
J. Classify the output:
     Known / Identity / Reinterpretation / Diagnostic /
     Boundary / Open Problem / Candidate Mechanism / New Theorem.
K. Run a finite example and a counterexample before research escalation.
```

## 7. Tool-routing matrix

| Trigger | First tools | Mandatory warning |
|---|---|---|
| coordinate product | Bell series, Euler product | convergence is separate |
| coordinate sum | additive-function theory | independence is approximate |
| smooth size weight | Mellin inversion | no \(1/s\) factor |
| sharp cutoff | Perron/Tauberian | smooth error does not transfer automatically |
| reduced residue | characters, \(L\)-functions | labels and bad primes matter |
| fiber variance | Parseval, large sieve | energy loses phase |
| truncated divisibility | sieve | level is not primality |
| two-factor interaction | Type I/II | geometry supplies no cancellation |
| support-only target | Möbius/parity audit | sign may be absent |
| density-zero discard | truncation/tail bound | unbounded weights can survive |

## 8. Research-front firewall

Translation Kernel v2 is a capability-building program. It may:

- encode known translations;
- add finite certificates and counterexamples;
- improve routing and error detection;
- identify gaps for future task-triggered learning.

It may not:

- open a second theorem target;
- claim a new mechanism from a translation card;
- authorize Dataset 004;
- initiate broad book mining;
- promote an internally proved result to certified originality;
- claim RH or GRH progress.

## 9. Pass-001 target and next threshold

Pass 001 adds 24 operational cards to the eight closed v1 families,
for a combined inventory of 32.

Pass 002 should reach at least 50 cards only after a benchmark exposes
real missing translations. Card count is not itself maturity; the
benchmark error profile controls subsequent learning.
