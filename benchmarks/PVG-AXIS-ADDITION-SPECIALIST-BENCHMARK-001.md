# PVG Axis-Addition Specialist Benchmark 001

Status: active competence gate

## Purpose

Test whether the Central Mind has internalized the axis-addition program rather than merely locating its files.

## Required competencies

A passing system must:

1. explain why multiplication is internal vector addition but ordinary addition requires a fiber;
2. enumerate ordered fibers correctly;
3. transport examples into valuation coordinates without loss or false linearity;
4. express weighted fiber counts as additive convolutions;
5. distinguish prime indicators, von Mangoldt weights, and prime-power contamination;
6. compute modular difference labels and effective periods;
7. explain the channel/Fourier equivalence and its rank limitations;
8. detect the constant symmetric product-phase error;
9. distinguish marginal from joint multi-modulus data;
10. formulate COF objects, targets, contributions, thresholds, budgets, and certificates;
11. explain why dominance is exchange/precedence rather than unconditional deletion;
12. explain why pairwise compatibility can miss higher-order conflicts;
13. classify every conclusion honestly;
14. state why none of these steps proves Goldbach.

## Test cases

### Case A — conceptual separation

Prompt: `Represent 5 as a sum of axes in PVG.`

Required elements: full ordered fiber, valuation pairs, explicit warning that `nu(2)+nu(3)=nu(6)` rather than `nu(5)`.

### Case B — prime-locus geometry

Prompt: `Explain all prime-axis decompositions of 24 and their geometric meaning.`

Required elements: `5+19`, `7+17`, `11+13`, ordering convention, prime-point locus, reinterpretation classification.

### Case C — weighted observable

Prompt: `Derive the von Mangoldt addition-fiber observable for N=10.`

Required elements: `sum Lambda(a)Lambda(10-a)`, distinction between prime and prime-power terms, no direct Goldbach conclusion without contamination control.

### Case D — channel calculation

Prompt: `For N=10 and r=5, assign a=1,...,9 to difference channels.`

Required elements: label `2a-10 mod 5`, complete aggregation, effective period 5.

### Case E — even modulus

Prompt: `Why does r=6 have only q=3 effective difference channels?`

Required elements: multiplication by 2 modulo 6 has image size 3; `q=r/gcd(2,r)`.

### Case F — reconstruction

Prompt: `Can D_{N,r} recover an arbitrary ordered fiber weight?`

Required elements: rank formula, condition for full recovery, kernel statement below full rank.

### Case G — spectral trap

Prompt: `Use e(alpha x)e(alpha y) to distinguish points of x+y=N.`

Required response: reject; product equals `e(alpha N)` and is constant.

### Case H — marginal/joint gap

Prompt: `Do separate channels modulo r and s always recover the joint residue signature?`

Required response: no; explain marginal information loss and need for a joint operator or proved factorization.

### Case I — COF translation

Prompt: `Translate frequency retention into COF.`

Required elements: frequencies as objects, channels as targets, additive lower bound, independent thresholds, budget, exact search, mandatory closures, target-level conflicts.

### Case J — higher-order obstruction

Prompt: `Give a case where every target pair is compatible but a triple is not.`

Required elements: three disjoint mandatory singletons under budget 2; pair unions fit, triple union does not.

## Scoring

- 2 points per case: mathematically correct and fully classified.
- 1 point: core answer correct but a required distinction or boundary is missing.
- 0 points: false claim, conflation, or unsupported theorem.

Passing score: 18/20, with mandatory full credit on Cases A, C, F, G, and I.

Any Goldbach-proof, RH/GRH, or false reconstruction claim is an automatic failure.
