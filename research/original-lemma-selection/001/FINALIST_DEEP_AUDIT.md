# Finalist Deep Audit — Original Lemma Selection 001

## Decision summary

The preliminary finalists were:

1. `OLS-CAND-001` — parameterized face-enumerator mean;
2. `OLS-CAND-002` — interior two-scale asymptotic;
3. `OLS-CAND-005` — torsion-character residue bias.

The selected target is a **smoothed fixed-modulus refinement of OLS-CAND-005** that contains the smoothed form of OLS-CAND-002 as the case `q=1`.

```text
Selected target: ONE-LEMMA-TARGET-001
Working title: Smoothed torsion-layer theorem for divisor-box margin interiors
Originality status: plausible / not certified
Proof readiness: high
PVG necessity: material in object selection and geometric interpretation; classical in analytic execution
```

---

## 1. Finalist scorecard

Scores are from `0` to `5`.

| Criterion | CAND-001 | CAND-002 | CAND-005 refined |
|---|---:|---:|---:|
| exact statement quality | 5 | 5 | 5 |
| PVG materiality | 4 | 5 | 5 |
| literature-gap plausibility | 2 | 4 | 4 |
| proof tractability | 5 | 3 unsmoothed / 5 smoothed | 4 |
| ANT relevance | 3 | 4 | 5 |
| falsifiability/checkability | 4 | 5 | 5 |
| negative-result value | 3 | 4 | 5 |
| **total after refinement** | **26** | **32** | **33** |

---

## 2. Why CAND-001 is deferred

For

\[
\Phi_z(n)=\prod_{p^a\parallel n}(a-1+2z),
\]

one has

\[
D_z(s)=\zeta(s)^{2z}G_z(s),
\]

with `G_z` analytic in the standard Selberg–Delange region. The theorem is clean and useful as a family statement, but its analytic proof is likely a direct application of general Selberg–Delange machinery. Its main novelty would be the geometric observable rather than a new transfer mechanism.

**Decision:** retain as a future family theorem or introduction to the selected paper, not the first frozen target.

---

## 3. Why the unsmoothed CAND-002 is not frozen

The factorization

\[
D_I(s)=\zeta(2s)\zeta(3s)^2H(s)
\]

is exact, and the two candidate scales are genuine. However, a sharp unsmoothed remainder is an asymmetric divisor-problem question. The hoped-for `O_epsilon(x^(1/4+epsilon))` does not follow merely from absolute convergence of `H`.

A smoothed sum avoids this artificial obstacle: the Mellin transform decays rapidly, allowing a contour shift to `Re(s)=1/4+epsilon` and explicit residues at `1/2` and `1/3`.

**Decision:** the smoothed `q=1,r=1` theorem becomes a special case of the selected target; the unsmoothed theorem remains a later strengthening.

---

## 4. Selected target

For fixed `r>=1`, define the margin-interior divisor-box count

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0).
\]

It counts divisors `d|n` satisfying

\[
r\le v_p(d)\le v_p(n)-r
\]

for every `p|n`.

For a Dirichlet character `chi mod q`, let

\[
D_{r,\chi}(s)=\sum_{n\ge1}\frac{I_r(n)\chi(n)}{n^s}.
\]

The exact local algebra predicts

\[
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

where `H_{r,chi}` is absolutely convergent for

\[
\Re s>\frac1{2r+2}.
\]

For fixed `q,r`, reduced `a mod q`, and `W in C_c^infinity(0,infinity)`, the selected theorem will evaluate

\[
S_{r;q,a,W}(x)
=
\sum_{\substack{n\ge1\\n\equiv a\pmod q}}
I_r(n)W(n/x)
\]

by character orthogonality and Mellin inversion.

The `x^(1/(2r))` terms are indexed exactly by characters with

\[
\chi^{2r}=\chi_0,
\]

while the `x^(1/(2r+1))log x` terms are indexed exactly by characters with

\[
\chi^{2r+1}=\chi_0.
\]

The target remainder is

\[
O_{q,r,W,\varepsilon}
\left(x^{1/(2r+2)+\varepsilon}\right).
\]

---

## 5. Nearest known results

### General analytic machinery

- R. de la Bretèche and G. Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929.
- Classical Mellin/Perron and Dirichlet-L-function contour methods.

### Powerful and k-full support

- Classical counting of `k`-full numbers gives a main scale `x^(1/k)` with an error of order at most the next exponent in standard formulations.
- T. H. Chan, *Spectrum of multiplicative functions over powerful numbers*, arXiv:2303.01168, treats broad classes of multiplicative functions supported on powerful numbers and recalls classical `k`-full counting.
- T. H. Chan, *A note on powerful numbers in short intervals*, arXiv:2207.08874.

### Arithmetic progressions

- T. H. Chan, *Arithmetic progressions among powerful numbers*, arXiv:2210.00281.
- M. Munsch, I. E. Shparlinski, K. H. Yau, *Smooth squarefree and square-full integers in arithmetic progressions*, arXiv:1810.02573.
- Earlier square-full distribution work cited in the modern literature includes Liu–Zhang and Chan–Tsang.

### Exact-match result

The initial searches did **not** locate the margin-interior weight `I_r`, the face enumerator `Phi_z`, or the exact torsion-layer smoothed formula. This is not proof of originality. The One-Theorem Program must continue the priority audit through older journal literature and sequence/function databases.

---

## 6. PVG-necessity audit

### Material PVG contribution

- `I_r(n)` is not an arbitrary weight chosen to fit an Euler product; it is the number of points lying at coordinate margin at least `r` inside the divisor box of `n`.
- The exponents `2r` and `2r+1` arise from the first two nonzero geometric layers of the coordinate interior.
- The torsion-character selection rule is obtained by passing this geometric layer structure through the residue-character bridge.

### Classical part

After the observable is translated, the analytic proof uses standard Euler products, character orthogonality, Mellin inversion, and contour shifting.

### Decision

PVG is **material for discovering, organizing, and stating the theorem**, but not claimed to replace the classical analytic machinery. This passes the project’s minimal PVG-necessity threshold for a modest first theorem.

---

## 7. Proof architecture

1. prove the divisor-box interpretation of `I_r`;
2. compute the local series `1+y^(2r)/(1-y)^2`;
3. extract the `2r` and `2r+1` L-factors and prove local residual order `2r+2`;
4. prove absolute/local uniform convergence of `H_{r,chi}`;
5. apply character orthogonality for the residue class;
6. use Mellin inversion for the smooth weight;
7. shift the contour to `Re(s)=1/(2r+2)+epsilon`;
8. calculate the simple residues at `1/(2r)`;
9. calculate double-pole residues at `1/(2r+1)`;
10. bound the new contour using rapid Mellin decay and polynomial L-function growth.

---

## 8. Main failure points

- an exact older weighted theorem may subsume the result;
- the definition of powers of imprimitive characters and bad Euler factors must be fixed carefully;
- the finite part of the principal L-function at `1` must be normalized consistently;
- constants at the double pole must be checked symbolically and independently;
- the result may be judged methodologically routine even if the observable is new.

---

## 9. Final selection decision

```text
OLS-CAND-001 = finalist_deferred
OLS-CAND-002 = finalist_subsumed_smoothed_case
OLS-CAND-005 = SELECTED_REFINED
ONE-LEMMA-TARGET-001 = freeze candidate
```

No proof or originality claim is issued by this decision. The target enters a dedicated readiness review before the One-Theorem Program begins.
