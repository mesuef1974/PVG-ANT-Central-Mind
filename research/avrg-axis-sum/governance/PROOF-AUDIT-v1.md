# Proof Audit v1 — PVG Addition Fibers

Status: `THEORY-FREEZE-v1.0 / completed first-pass audit`

Scope: the canonical core in `CANONICAL-DEFINITIONS-AND-RESULTS-v1.md`, covering Proposition 1.3, Theorem 2.3, Proposition 2.5, Theorem 3.4, Proposition 4.3, Theorem 5.4, Corollaries 5.5–5.6, Proposition 5.7, Theorem 6.2, Corollary 6.3, Proposition 6.4, and Proposition 7.2.

This audit checks hypotheses, edge cases, hidden conventions, proof completeness, and classification. It introduces no new research direction.

## 1. Global conventions that must remain explicit

1. \(\mathbb N_{\ge1}\) denotes the positive integers.
2. The valuation vectors lie in the finitely supported direct sum \(\mathbb N_0^{(\mathbb P)}\), not the unrestricted product.
3. Addition fibers are ordered and positive unless explicitly stated otherwise.
4. All vector-space ranks are over \(\mathbb C\); the channel matrices have entries in \(\{0,1\}\), so the same rank also holds over every characteristic-zero field.
5. Every modulus satisfies \(r\ge1\).
6. Channel coordinates are indexed by residue classes in \(\mathbb Z/r\mathbb Z\), even when some rows are zero.
7. The discrete Fourier transform in Proposition 5.7 need only be invertible for rank preservation. Unitary normalization is required only for singular-value preservation.

## 2. Proposition 1.3 — exact recovery

**Verdict:** PASS.

**Hypotheses:** \(n\ge1\); \(x\) finitely supported.

**Dependency:** uniqueness of prime factorization.

**Edge case:** \(n=1\) gives \(\nu(1)=0\) and \(\rho(0)=1\).

**Hidden convention repaired:** the empty product equals \(1\).

## 3. Theorem 2.3 — no-information-loss theorem

**Verdict:** PASS.

**Dependencies:** Definition 2.2 and Proposition 1.3.

**Edge case \(N=2\):**

\[
\mathcal F_2^+=\{(1,1)\},
\qquad
\mathcal G_2=\{(0,0)\},
\]

and the map remains bijective.

**No hidden multiplicity:** because \(\nu\) is injective, the set-valued image \(\mathcal G_N\) has exactly \(N-1\) points. Consequently, the counting measure in Definition 3.1 has unit mass at each point.

## 4. Proposition 2.5 — reflection structure

**Verdict:** PASS.

**Dependencies:** ordered-fiber definition and injectivity of \(\nu\).

**Odd case:** no fixed point because \(2a=N\) has no integral solution.

**Even case:** exactly one fixed point, indexed by \(a=N/2\).

**Edge case \(N=2\):** the sole point is fixed, consistent with the proposition.

## 5. Theorem 3.4 — fiber convolution identity

**Verdict:** PASS.

**Dependencies:** exact recovery and the atomic definition of \(\mu_N\).

**Hidden convention:** the displayed integral is integration against a finite atomic counting measure. No analytic convergence issue occurs.

**Function class:** arbitrary functions \(f,g:\mathbb N\to\mathbb C\) are sufficient because the sum contains only \(N-1\) terms. No growth or summability hypothesis is needed.

**Edge case \(N=2\):** both sides reduce to \(f(1)g(1)\).

## 6. Proposition 4.3 — von Mangoldt support

**Verdict:** PASS WITH TERMINOLOGY NOTE.

The statement is correct provided “support” means the set on which the function is nonzero:

\[
\operatorname{supp}\widehat\Lambda=\mathcal A_1.
\]

Since \(k\ge1\), every point \(k e_p\) recovers the prime power \(p^k\), and \(\Lambda(p^k)=\log p\).

**Edge case:** \(x=0\) recovers \(1\), and \(\Lambda(1)=0\), so the origin is not in the support.

## 7. Exact reformulation 4.4 — binary Goldbach

**Verdict:** PASS AS REFORMULATION ONLY.

**Required scope:** even \(N\ge4\).

The intersection is nonempty exactly when there exists an ordered prime pair \((p,q)\) satisfying \(p+q=N\). This makes no existence claim beyond the original Goldbach statement.

**Counting warning:** the size of the intersection counts ordered representations. A diagonal representation \(N=2p\) contributes one point, while a representation with \(p\ne q\) contributes two reflected points.

## 8. Theorem 5.4 — single-modulus rank formula

**Verdict:** PASS.

Let

\[
q=\frac r{\gcd(2,r)}.
\]

Two columns coincide exactly when \(a\equiv b\pmod q\). Because \(1,\dots,N-1\) is a consecutive interval, it meets exactly \(\min(N-1,q)\) residue classes modulo \(q\). Distinct nonzero columns are distinct standard basis vectors and hence linearly independent.

Therefore

\[
\operatorname{rank}D_{N,r}=\min(N-1,q).
\]

### Edge cases

- \(r=1\): \(q=1\), rank \(1\).
- \(N=2\): one column, rank \(1\) for every \(r\ge1\).
- even \(r\): only one parity class of output residues is reachable; the maximum rank is \(r/2\).
- odd \(r\): every residue class is reachable over a complete period, and the maximum rank is \(r\).

**Proof-strengthening note:** the current proof should explicitly state that distinct occupied rows give linearly independent standard-basis columns. Merely counting distinct columns is sufficient here because each column has exactly one entry equal to \(1\).

## 9. Corollary 5.5 — kernel dimension

**Verdict:** PASS.

This follows from rank-nullity on the \((N-1)\)-dimensional space \(V_N\).

No additional hypothesis is needed.

## 10. Corollary 5.6 — full reconstruction

**Verdict:** PASS, BUT THE GENERAL CRITERION SHOULD BE RECORDED.

The stated assumptions “\(r\) odd and \(r\ge N-1\)” imply

\[
\frac r{\gcd(2,r)}=r\ge N-1,
\]

so the labels are distinct and

\[
w_a=(D_{N,r}w)_{2a-N\pmod r}.
\]

The exact necessary-and-sufficient injectivity criterion is the stronger statement

\[
D_{N,r}\text{ is injective}
\iff
\frac r{\gcd(2,r)}\ge N-1.
\]

Thus sufficiently large even moduli are also injective; for even \(r\), the condition is \(r\ge2(N-1)\). This is a clarification of an existing theorem, not a new concept.

## 11. Proposition 5.7 — Fourier equivalence

**Verdict:** PASS FOR RANK.

Since \(F_r\) is invertible,

\[
\ker(F_rD_{N,r})=\ker D_{N,r}
\]

and the ranks agree.

**Normalization warning:** singular values are preserved only if \(F_r\) is normalized to be unitary. The proposition currently asserts rank only, so it is correct as written.

## 12. Theorem 6.2 — joint-modulus rank theorem

**Verdict:** PASS AFTER CODOMAIN CLARIFICATION.

For \(L=\operatorname{lcm}(r_1,\dots,r_s)\), equality of full signatures is equivalent to congruence modulo every \(r_j\), hence to congruence modulo \(L\):

\[
2a-N\equiv2b-N\pmod{r_j}\ \forall j
\iff
2a-N\equiv2b-N\pmod L.
\]

The rank therefore equals that of \(D_{N,L}\).

**Required wording repair:** Definition 6.1 must specify the codomain as the vector space indexed by the set of compatible residue tuples, or equivalently by \(\mathbb Z/L\mathbb Z\). Without this, the matrix representation is conceptually clear but not fully formal.

**No pairwise-coprime assumption is needed.** The lcm congruence equivalence holds for arbitrary positive moduli.

## 13. Corollary 6.3 — joint reconstruction criterion

**Verdict:** PASS.

It follows immediately from Theorem 6.2 because the domain dimension is \(N-1\).

## 14. Proposition 6.4 — conditioning in the injective case

**Verdict:** PASS WITH MATRIX-CONVENTION NOTE.

In the injective case each column occupies a distinct output row. After deleting zero rows and ordering occupied rows according to the input index, the matrix is exactly \(I_{N-1}\). Therefore all singular values of the reduced matrix are \(1\).

Keeping zero rows does not change the nonzero singular values, so the original rectangular operator also has all \(N-1\) singular values equal to \(1\).

**Condition number convention:** \(\kappa_2\) is the ratio of largest to smallest singular value on an injective map; under this convention it equals \(1\).

## 15. Proposition 7.2 — phase correction

**Verdict:** PASS, WITH AN EXACT NONCONSTANCY CRITERION AVAILABLE.

The symmetric phase is constant because

\[
e(\alpha a)e(\alpha(N-a))=e(\alpha N).
\]

For the difference phase, consecutive terms differ by the factor \(e(2\alpha)\). Hence, when \(N\ge3\), the phase is constant on the whole fiber exactly when

\[
2\alpha\in\mathbb Z.
\]

For \(N=2\), every function on the one-point fiber is constant. The phrase “generally nonconstant” is correct but should be replaced by this exact criterion in the final paper.

## 16. Audit of the status-ledger claims T1–T8 and C1–C4

| Ledger item | Audit verdict | Action |
|---|---|---|
| T1 no information loss | PASS | retain |
| T2 convolution identity | PASS | retain |
| T3 symmetry | PASS | retain |
| T4 rank formula | PASS | strengthen proof sentence |
| T5 kernel dimension | PASS | retain |
| T6 joint rank | PASS WITH CLARIFICATION | formalize codomain |
| T7 joint conditioning | PASS | state condition-number convention |
| T8 Fourier rank equivalence | PASS | specify rank, not unnormalized singular values |
| C1 large odd modulus reconstruction | PASS | add general iff criterion nearby |
| C2 joint reconstruction | PASS | retain |
| C3 zero frequency redundancy | PASS IN PRINCIPLE | add an explicit formula and Fourier normalization |
| C4 character-row redundancy | NOT YET CERTIFIED IN CANONICAL CORE | downgrade to pending derived observation until a precise statement and proof are inserted |

### Required repair for C3

For any channel vector,

\[
\sum_{d\bmod r}(D_{N,r}w)_d=\sum_{a=1}^{N-1}w_a.
\]

Under the unnormalized Fourier convention, this is the \(k=0\) Fourier coordinate. Under a unitary convention it differs by the expected factor \(r^{-1/2}\).

### Required repair for C4

The status ledger currently calls character rows a proved corollary, but the canonical core does not define the character measurement operator or prove the factorization through complete residue channels. The intended statement is plausible and elementary, but governance requires one of two actions:

1. insert a precise operator definition and proof; or
2. relabel C4 as `pending derived observation`.

Until that repair is committed, C4 must not be advertised as a proved corollary of Paper 1.

## 17. Final audit result

- Core propositions/theorems audited: **12**.
- Fully valid as written or with harmless convention notes: **10**.
- Valid but requiring explicit formal clarification: **2** — joint-signature codomain and exact phase criterion.
- Status-ledger item requiring downgrade or proof insertion: **C4**.
- Counterexamples found to T1–T8: **none**.
- New mathematical claims introduced by this audit: **none**; all strengthened statements are immediate consequences of the existing formulas.

## 18. Mandatory next repairs

1. Formalize the codomain of \(J_{N;\mathbf r}\).
2. Add the exact injectivity criterion for \(D_{N,r}\), retaining the large-odd-modulus statement as a convenient special case.
3. Add the explicit zero-frequency formula with a Fourier-normalization note.
4. Replace “generally nonconstant” by the exact criterion \(2\alpha\notin\mathbb Z\) for \(N\ge3\).
5. Downgrade C4 or supply its missing definition and proof.
6. Only after these repairs mark the proof audit closed.