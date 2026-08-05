# ENGINE-005 Candidate — Local Neighborhood Geometry Around an Integer

```text
Candidate ID: ENGINE-005-LOCAL-NEIGHBORHOOD-GEOMETRY
Parent program: GOAL-PVG-INVERSE-GEOMETRY-001
Current governing engine: ENGINE-004 pending Phase-C administrative closure
Status: CANDIDATE_SUCCESSOR / NOT_ACTIVE
Date: 2026-07-23
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

## Exact candidate objects

For fixed neighborhood radius `h` and local-prime ceiling `P`, the candidate may later define:

1. truncated valuation field `V_{h,P}(x)`;
2. smallest-killer map `K_x(k)`;
3. residue-obstruction field `R_{h,P}(x)`;
4. support shadow `S_{h,P}(x)`;
5. local survival mask `L_{h,P}(x;k)`.

For every prime `p<=P` and offset `k`, the exact identity

\[
p\mid x+k \iff x\equiv-k\pmod p
\]

shows that the local divisibility pattern is periodic modulo the corresponding prime wheel. This creates a major confounding risk: apparent discrimination may merely reproduce elementary residue-wheel information.

## Governance relation

```text
ENGINE-004 Phase-C scientific deliverable = COMPLETE
ENGINE-004 administrative closure = correction-only review in progress
CANDIDATE-LOCAL-OBSTRUCTION-GEOMETRY-001 = DEFERRED / NON-GOVERNING
ENGINE-005 activation = NOT AUTHORIZED
```

The earlier statement that `ENGINE-004 PASS-004 — Local Obstruction Geometry` was active is withdrawn. That material now has a unique deferred candidate identity and does not control this candidate.

ENGINE-005 may be activated only after:

1. final Phase-C closure;
2. explicit parent selection of a successor engine;
3. a new readiness card freezing domain, data, controls, and claim ceiling.

## Mandatory future controls

Any future pilot must:

- remove center information `k=0` from classification features;
- match magnitude, parity, and preregistered residue classes;
- use disjoint numeric intervals for validation;
- include residue-only and magnitude-only baselines;
- include label-shuffle and feature-permutation null tests;
- prohibit a primality-test or theorem claim.

## Kill criteria

Kill or redesign the path if any apparent signal disappears after residue and magnitude matching, depends on leakage, collapses out of interval, or adds no stable information beyond a standard small-prime sieve.

## Claim ceiling

```text
IDENTITY = exact congruence and periodicity laws
PROVED = elementary consequences only
FINITE-VERIFIED = none yet under ENGINE-005
HYPOTHESIS = possible nontrivial local signal
OPEN = existence of stable incremental information
new primality criterion = false
Goldbach/PNT/RH/GRH progress = false
historical originality = false
publication readiness = false
```

**Classification:** successor candidate only; inactive.