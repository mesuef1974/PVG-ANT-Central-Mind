# PVG Inverse Geometry 001

## Priority

Native understanding of Prime Valuation Geometry is the active priority. The program studies
individual integer points, their local neighborhoods, and the higher-dimensional geometry of
prime-support faces before opening another theorem target.

## Purpose

Build a governed forward-and-reverse grammar:

```text
complete factorization
→ labeled valuation vector
→ support face
→ horizontal level
→ squarefree floor and repeat depth
→ exponent shape
→ primitive ray
→ divisor box and multiple cone
→ axis-ratio matrix
→ primitive horizontal neighbors
→ local arithmetic transition families
```

and the reverse computational routes:

```text
decimal integer
→ certified factorization
→ exact PVG passport
```

```text
certified adjacent pair
→ gcd base
→ reduced prime axes
→ local transfer direction
```

## Pass-001 deliverables — exact point passport

1. Canonical point classification by support dimension, total height, shape, and primitive ray.
2. Exact treatment of lattice lines as geometric sequences.
3. Exact local-operator identity for sums, differences, and finite linear filters.
4. The \(2,3\)-face as the first controlled case study.
5. A canonical JSON geometric passport.
6. An executable exact inverse-geometry prototype.
7. Deterministic tests including origin, prime axis, two-prime face, balanced composite ray,
   three-prime face, a difficult 64-bit composite, and a supplied factorization above \(2^{64}\).
8. Explicit refusal and uncertainty discipline when factorization is incomplete.

## Pass-002 deliverables — local neighborhood and axis ratios

1. Define the axis-ratio matrix \(R_{ij}=p_j/p_i\) and its cocycle laws.
2. Define primitive horizontal neighbors \(N_{i\to j}=Np_j/p_i\).
3. Identify fixed-level directions with the root lattice \(A_{s-1}\).
4. Prove that horizontal lines are finite geometric sequences.
5. Record the interior ordered degree \(s(s-1)\).
6. Recover adjacent local axes using gcd and reduced quotients.
7. Define horizontal graph distance as half the exponent-vector \(L^1\) distance.
8. Record midpoint and barycentric multiplicative identities.
9. Separate horizontal, axis-parallel, and primitive-ray sequences.
10. Add an executable local-neighborhood analyzer and deterministic examples for
    \((2,3)\), \((2,5)\), \((3,7)\), \((2,3,5)\), and \(10403=101\cdot103\).
11. Add a governed research agenda covering arithmetic functions, additive support transitions,
    local inverse problems, factorization diagnostics, graph spectra, and analytic distributions.

## Governance constraints

- Do not modify the frozen PVG Core Ontology v1 registry in these passes.
- Treat new names as working terminology until a separate ontology-extension audit.
- Separate exact identities from conjectures, diagnostics, candidate mechanisms, and novelty questions.
- No new theorem target is authorized.
- No Dataset 004 is authorized.
- No Lean expansion is authorized in this program.
- No claim that visualization is injective or isometric.
- No claim that inverse geometry bypasses integer factorization.
- No claim that neighbor generation yields a general factorization speedup.
- Any factorization experiment must be benchmarked against appropriate classical baselines.
- Keep this branch separate from the structural-laboratory branch and the protected recovery stash.

## Exit criteria

- documentation and executable tools agree on every emitted field;
- all unit tests pass on Python 3.12;
- exact mode never emits a point or neighborhood without a complete verified factorization;
- large unsupported inputs fail honestly;
- the \(s(s-1)\) neighbor law, axis-ratio lines, gcd recovery, vertices, and distance law are tested;
- research questions are labeled by maturity rather than promoted from visual evidence;
- branch remains separate from structural-laboratory and axis-sum recovery work;
- review decides whether a future Core Ontology v2 extension is warranted.

## Classification

Capability maturation / exact encoding / local inverse-problem discipline / finite-face geometry /
research-program foundation. No theorem, originality, publication, Goldbach, RH, or GRH claim.
