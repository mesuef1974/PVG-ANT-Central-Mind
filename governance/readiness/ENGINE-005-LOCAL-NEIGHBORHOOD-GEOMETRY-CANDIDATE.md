# ENGINE-005 Candidate — Local Neighborhood Geometry Around an Integer

```text
Candidate ID: ENGINE-005-LOCAL-NEIGHBORHOOD-GEOMETRY
Parent program: GOAL-PVG-INVERSE-GEOMETRY-001
Current governing engine remains: ENGINE-004
Status: CANDIDATE_SUCCESSOR / NOT_ACTIVE
Date: 2026-07-22
Phase D: NOT AUTHORIZED
Primality-test claim: NOT AUTHORIZED
```

## Research question

Given an integer `x`, does the certified local arithmetic geometry of nearby integers

\[
\mathcal E_{h,P}(x)=\bigl(\nu_p(x+k)\bigr)_{|k|\le h,\ p\le P}
\]

contain stable, out-of-sample information that distinguishes primes from carefully matched composite controls?

This is a falsifiable classification question, not a primality theorem and not an authorization to train a production classifier.

## Exact objects

For fixed neighborhood radius `h` and local-prime ceiling `P`, define:

1. **Truncated valuation field**
   \[
   V_{h,P}(x)=\left(\nu_p(x+k)\right)_{|k|\le h,\ p\le P}.
   \]

2. **Smallest-killer map**
   \[
   K_x(k)=\min\{p\in\mathbb P:p\mid x+k\},
   \]
   when such a prime is found below the governed ceiling; otherwise record `UNRESOLVED`.

3. **Residue-obstruction field**
   \[
   R_{h,P}(x)=\left((x+k)\bmod p\right)_{|k|\le h,\ p\le P}.
   \]

4. **Support shadow**
   \[
   S_{h,P}(x)=\left(\{p\le P:p\mid x+k\}\right)_{|k|\le h}.
   \]

5. **Local survival mask**
   \[
   L_{h,P}(x;k)=1
   \]
   exactly when no prime `p<=P` divides `x+k`, with boundary handling for `x+k=p`.

## Immediate scientific hypotheses

```text
H0: After matching by magnitude, parity, and small-prime residue class,
    the proposed neighborhood features do not distinguish primes from composites
    beyond sampling noise or leakage.

H1: At least one preregistered feature family retains stable out-of-sample
    discriminatory information after leakage controls and matched sampling.
```

No claim stronger than finite experimental discrimination is allowed.

## Required controls

The first experiment must compare odd primes against at least three matched composite classes:

1. odd semiprimes of comparable magnitude;
2. odd composites with no prime factor `<=P`;
3. pseudoprime/adversarial composites where feasible.

Mandatory leakage controls:

- remove the center value `k=0` from every feature used for classification;
- do not include the primality label, factorization, `x mod x`, or any feature that directly tests divisibility of `x`;
- match or stratify by digit length, parity, and residue classes modulo a preregistered wheel;
- split by disjoint numeric intervals, not random row splits alone;
- evaluate on a held-out magnitude range;
- include label-shuffle and feature-permutation null tests;
- compare against residue-only and magnitude-only baselines.

## Preregistered pilot

```text
center classes: prime / matched composite
neighborhood radii h: 16, 32, 64
local-prime ceilings P: 29, 97, 251
center feature k=0: forbidden
initial numeric domain: bounded and declared before generation
training use: prohibited until raw deterministic dataset and split manifest are frozen
```

The first pass is data generation and descriptive validation only. Any classifier pass requires a separate readiness card.

## Exact identities and guaranteed structure

For every prime `p<=P` and offset `k`:

\[
p\mid x+k \iff x\equiv-k\pmod p.
\]

Hence the local divisibility pattern is periodic in `x` modulo

\[
W_P=\prod_{p\le P}p.
\]

This periodicity is an exact identity and creates a major confounding risk: apparent class separation may merely reproduce residue-wheel structure already known from elementary sieving.

## Required outputs of the feasibility pass

- deterministic generator for `V`, `K`, `R`, `S`, and `L`;
- matched prime/composite sampling manifest;
- interval-disjoint train/validation/test partitions, even if no model is trained;
- duplicate and leakage audit;
- feature invariance and wheel-periodicity audit;
- descriptive summaries by class and magnitude band;
- explicit negative results;
- compact hashes for every generated artifact;
- a decision: `ADVANCE`, `REDESIGN`, or `KILL`.

## Kill criteria

Kill or redesign the path if any of the following occurs:

1. class separation disappears after matching residue classes and magnitude;
2. performance is explained by forbidden center information or data leakage;
3. held-out interval performance collapses to baseline;
4. features add no stable information beyond a standard small-prime sieve;
5. results vary materially under harmless changes of sampling seed or interval;
6. computational cost scales worse than the information gained.

## Claim ceiling

```text
IDENTITY: exact congruence and periodicity laws
PROVED: elementary consequences only
FINITE-VERIFIED: deterministic pilot summaries
INTERPRETATION: geometric language for the local field
HYPOTHESIS: possible prime/composite discrimination
OPEN: existence of any stable nontrivial signal

new primality criterion = false
primality proof = false
probable-prime test = false
Goldbach progress = false
PNT progress = false
RH/GRH progress = false
historical originality = false
publication readiness = false
```

## Governance relation to current work

`ENGINE-004 PASS-004 — Local Obstruction Geometry` remains the only active subpass. This candidate may become the next engine only after PASS-004 closes and an explicit parent review authorizes activation.
