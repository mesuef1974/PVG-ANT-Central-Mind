# PVG Inverse Geometry 001

## Priority

Native understanding of Prime Valuation Geometry is the active priority. The program studies
individual integer points, local neighborhoods, prime-axis edge transitions, and composition on
prime-axis triangles before opening another theorem target.

## Governed grammar

```text
complete factorization
→ labeled valuation vector
→ support face and horizontal level
→ primitive ray and local neighborhood
→ prime-pair edge signatures
→ prime-axis triangle composition
```

Reverse routes remain:

```text
decimal integer → certified factorization → exact PVG passport
certified adjacent pair → gcd base → reduced prime axes → local transfer direction
```

## PASS-001 — exact point passport

Classify support, `omega`, `Omega`, squarefree floor, repeat depth, exponent shape, primitive ray,
divisor box, multiple cone, and directional geometric sequences. Exact point location requires a
complete certified factorization.

## PASS-002 — local neighborhood and axis ratios

Define `R_ij=p_j/p_i`, primitive transfers `N_(i->j)=Np_j/p_i`, the horizontal root lattice
`A_(s-1)`, graph distance, simplex vertices, gcd recovery from adjacent pairs, and the three distinct
geometric-sequence families: horizontal, axis-parallel, and primitive-ray.

## PASS-003 — prime-pair edge transition atlas

Registered scope: all `p<q<=100`, giving 25 primes and 300 unordered pairs. Record ratio, normalized
gap, sum and difference factorizations, support, `omega`, `Omega`, and defects

\[
\kappa_+=\Omega(p+q)-1,\qquad \kappa_-=\Omega(q-p)-1.
\]

Exact classifications:

- sum preservation iff `p=2` and `q+2` is prime;
- difference preservation iff `q-p` is prime;
- odd-odd difference preservation iff `q-p=2`;
- simultaneous preservation only for `(2,5)`.

## PASS-004 — prime-axis triangle composition atlas

Registered scope: all `p<q<r<=100`, giving

\[
\binom{25}{3}=2300
\]

unordered prime-axis triangles.

Deliverables:

1. Verify multiplicative path independence
   \[
   \frac qp\frac rq=\frac rp
   \]
   and closed holonomy
   \[
   \frac qp\frac rq\frac pr=1.
   \]
2. Verify additive gap composition
   \[
   (q-p)+(r-q)=r-p.
   \]
3. Define normalized gaps
   \[
   \delta(a,b)=\frac{b-a}{b+a}
   \]
   and verify
   \[
   \delta(p,r)=\frac{\delta(p,q)+\delta(q,r)}{1+\delta(p,q)\delta(q,r)}.
   \]
4. Recover the three prime vertices from the three pair sums.
5. Verify complete axis-2 routing on all-odd triangles and triangles containing axis 2.
6. Record preservation profiles `Sx_Dy` counting sum- and difference-preserving edges.
7. Prove and test:
   - no triangle has three sum-preserving edges;
   - the unique triangle whose three differences preserve level is `(2,5,7)`;
   - the unique all-odd triangle with two difference-preserving edges is `(3,5,7)`.
8. Generate a deterministic 2300-record CSV and committed JSON summary.

## Governance constraints

- PVG Core Ontology v1 remains unchanged.
- New names are working terminology until a separate ontology-extension audit.
- No new theorem target, Dataset 004, or Lean expansion is authorized.
- No bound expansion beyond 100 without a separate registered protocol.
- Finite counts support no asymptotic inference.
- No general factorization speedup, originality, publication, Goldbach, RH, or GRH claim.
- Keep this branch separate from the structural-laboratory branch and protected recovery stash.

## Exit criteria

- documentation, generators, tests, and committed summaries agree;
- all four deterministic test suites pass on Python 3.12;
- the 300-edge and 2300-triangle atlases regenerate exactly;
- all ratio, gap, vertex-recovery, axis-2-routing, and preservation checks pass;
- unsupported exact inverse inputs fail honestly;
- finite diagnostics remain labeled by scope and maturity.

## Classification

Capability maturation / exact encoding / local inverse geometry / finite edge and triangle atlases /
research-program foundation. No theorem novelty or major-conjecture claim.
