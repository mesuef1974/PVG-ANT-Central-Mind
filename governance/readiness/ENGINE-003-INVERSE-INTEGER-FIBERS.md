# ENGINE-003 — Inverse Integer Fibers Readiness Card

```text
TASK-ID: ENGINE-003-INVERSE-INTEGER-FIBERS
Title: Build the exact integer-fiber kernel for inverse PVG
Research front: PVG-INVERSE-INTEGER-FIBERS-001
Strategic-goal link: GOAL-PVG-ANT-STRATEGIC-001
Parent goals: GOAL-PVG-INVERSE-GEOMETRY-001; GOAL-PVG-FOUNDATIONS-001; GOAL-PVG-ANT-LANGUAGE-001
Owner/status: project owner / READY and active_current
Date/version: 2026-07-22 / v1
```

## 1. Research question

For a finite prime support face \(F\), can the exact integer fiber

\[
\mathcal N(F)=\{n\ge1:\operatorname{supp}(n)=F\}
\]

be represented, generated, ordered, and certified as a positive exponent lattice, with a reproducible bounded implementation and a precise Dirichlet-series translation?

## 2. Exact mathematical core

For \(F=\{p_1,\ldots,p_k\}\):

\[
\boxed{
\mathcal N(F)
=
\left\{\prod_{j=1}^k p_j^{e_j}:e_j\ge1\right\}
}
\]

and the exponent map is a bijection:

\[
\mathbb N_{\ge1}^{k}
\longleftrightarrow
\mathcal N(F).
\]

For \(\Re(s)>0\):

\[
\boxed{
\sum_{n\in\mathcal N(F)}n^{-s}
=
\prod_{p\in F}\frac{1}{p^s-1}
}
\]

because the series factors into finitely many absolutely convergent geometric series.

## 3. Frozen verification box

```text
support_prime_limit = 11
support_face_sizes = 1,2,3
integer_cap = 100000
dirichlet_test_s = 2.0
complete_integer_scan = true
```

This gives 25 support faces. Every generated fiber is compared with an independent scan of all integers \(1\le n\le100000\).

## 4. Required API

```text
normalize_support(face)
exponent_vectors(face, cap)
integer_fiber(face, cap)
fiber_record(face, cap)
hasse_edges(face, cap)
dirichlet_partial_sum(face, s, cap)
dirichlet_closed_form(face, s)
registered_summary()
```

## 5. Exact structural laws to certify

1. **Exponent-lattice bijection:** positive exponent vectors correspond uniquely to exact-support integers.
2. **Radical minimum:** the smallest fiber element is \(\operatorname{rad}(F)=\prod_{p\in F}p\).
3. **Coordinate order:** divisibility inside one fiber is coordinatewise order on exponent vectors.
4. **Hasse law:** cover edges increment exactly one exponent by one.
5. **Closure:** multiplication, gcd, and lcm preserve the exact support fiber.
6. **Non-closure:** addition and integer quotient need not preserve the fiber.
7. **Dirichlet identity:** the infinite fiber series equals \(\prod_{p\in F}(p^s-1)^{-1}\) for \(\Re(s)>0\).

## 6. Deliverables

- `tools/pvg_inverse_integer_fibers.py`
- `tests/test_pvg_inverse_integer_fibers.py`
- `research/pvg-space-deepening/engine-003-inverse-integer-fibers.md`
- `research/pvg-space-deepening/data/inverse-integer-fibers-summary.json`
- `.github/workflows/pvg-inverse-integer-fibers-audit.yml`
- closure or negative-certificate review

## 7. Success and stop rules

- **Success:** exact generator equals the independent scan for all 25 faces; lattice reconstruction, divisibility, Hasse edges, closure laws, deterministic JSON, and Dirichlet checks pass.
- **Stop:** close after this frozen box. Do not increase the prime or integer cap because patterns appear.
- **Negative certificate:** record any mismatch with the first counterexample and do not promote Phase B.
- **Claim ceiling:** exact classical identities plus finite verified implementation. No originality claim from the product formula alone.

## 8. Out of scope

```text
Phase C prime fibers
Goldbach representation search
new depth search
asymptotic fiber counting
probabilistic claims
historical originality
publication claim
PNT, RH, or GRH progress
```

## 9. Return gate

After ENGINE-003, Stage Review must choose:

1. return to `GOAL-OP-ONE-THEOREM-001`;
2. authorize a separately named analytic transfer task if the fiber Dirichlet structure serves a specific lemma;
3. close the inverse-engine branch at Phase B.

Phase C is not authorized automatically.

## 10. Readiness decision

```text
READY
```

ENGINE-002 supplied the support layer; the Phase B identities follow from unique factorization and are independently checkable in a complete finite box.

**Honest classification:** exact integer-fiber infrastructure and bounded verification; no new theorem claimed.
