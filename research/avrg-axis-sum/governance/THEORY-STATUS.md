# PVG Addition Fibers Theory — Status

Status: `ACTIVE-RESEARCH-v1.1`

Freeze status: `LIFTED` by explicit owner instruction on 2026-07-15.

The v1.0 Paper 1 core remains a stable audited baseline. New work is developed in separate v1.1 research units before later canonical integration.

## 1. Stable v1.0 baseline

### Accepted definitions

- **D1. Prime valuation vector**: \(\nu(n)=(v_p(n))_{p\in\mathbb P}\).
- **D2. Recovery map**: \(\rho(x)=\prod_p p^{x_p}\).
- **D3. Positive addition fiber**: \(\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}\).
- **D4. Prime-valuation addition fiber**: \(\mathcal G_N=(\nu\times\nu)(\mathcal F_N^+)\).
- **D5. Fiber counting measure**: \(\mu_N=\sum_{a=1}^{N-1}\delta_{(\nu(a),\nu(N-a))}\).
- **D6. Fiber weight space**: \(V_N=\mathbb C^{N-1}\).
- **D7. Difference-channel operator**: \((D_{N,r}w)_d=\sum_{2a-N\equiv d\,(\mathrm{mod}\,r)}w_a\).
- **D8. Joint-modulus operator**: \(J_{N;\mathbf r}\) on full compatible residue signatures.
- **D9. Marginal stacked operator**: \(M_{N;\mathbf r}=(D_{N,r_1}^{\mathsf T},\dots,D_{N,r_s}^{\mathsf T})^{\mathsf T}\).
- **D10. Prime point locus**: \(\mathcal P_1=\{e_p:p\in\mathbb P\}\).
- **D11. Prime-power axis locus**: \(\mathcal A_1=\{k e_p:p\in\mathbb P,\ k\ge1\}\).
- **D12. Difference-phase transform**.

### Proved results

- **T1.** No-information-loss theorem.
- **T2.** Fiber convolution identity.
- **T3.** Fiber reflection theorem.
- **T4.**
  \[
  \operatorname{rank}D_{N,r}=\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
  \]
- **T5.** Kernel-dimension formula by rank-nullity.
- **T6.** For \(L=\operatorname{lcm}(r_1,\dots,r_s)\),
  \[
  \operatorname{rank}J_{N;\mathbf r}=\min\!\left(N-1,\frac L{\gcd(2,L)}\right).
  \]
- **T7.** Injective joint-signature operators have singular values all equal to \(1\).
- **T8.** Full finite Fourier transformation preserves channel rank and information.

### Exact reformulations and scientific ceiling

- Goldbach is represented exactly by intersection with \(\mathcal P_1\times\mathcal P_1\), not proved.
- Von Mangoldt support is represented by \(\mathcal A_1\).
- No new major-arc, minor-arc, sieve, Goldbach, RH, or GRH claim is authorized by the finite framework alone.
- Novelty and priority claims remain unauthorized pending deeper literature review.

## 2. Completed v1.0 controls

- canonical notation — **complete**;
- canonical definitions and proofs — **complete**;
- examples \(N=10,12,24,30\) — **complete**;
- joint-modulus example \((N;r_1,r_2)=(10;3,5)\) — **complete**;
- proof audit through second pass — **PASS**;
- dependency and numbering audit — **PASS**;
- theorem/evidence cross-links — **complete**;
- finite single-modulus verification over 9,900 cases — **PASS**;
- focused preliminary literature review — **complete**;
- Paper 1 textual consistency audit — **PASS**;
- professional LaTeX source — **complete**.

## 3. Freeze-lift decision

Controlling decision:

`research/avrg-axis-sum/governance/THEORY-FREEZE-LIFT-v1.1.md`

```text
THEORY-STATE = ACTIVE-RESEARCH-v1.1
FREEZE = LIFTED
OWNER AUTHORIZATION = GRANTED
```

The v1.0 baseline is preserved. New statements must be classified as definition, proved theorem, candidate theorem, conjecture, computation, or open problem.

## 4. Active v1.1 research program

### ACTIVE-001 — Marginal stacked operator

Object:

\[
M_{N;\mathbf r}
=
\begin{pmatrix}
D_{N,r_1}\\
\vdots\\
D_{N,r_s}
\end{pmatrix}.
\]

#### Completed for two moduli

1. **Graph/incidence representation — proved.**
   The nonzero-row matrix of \(M_{N;(r,s)}\) is the unsigned vertex-edge incidence matrix of the realized bipartite residue-coupling multigraph \(G_{N;r,s}\).

2. **Exact rank — proved.**
   \[
   \operatorname{rank}M_{N;(r,s)}
   =|U|+|V|-c(G_{N;r,s}).
   \]

3. **Full-period rank formula — proved.** If
   \[
   q_r=\frac r{\gcd(2,r)},\qquad
   q_s=\frac s{\gcd(2,s)},
   \]
   and \(N-1\ge\operatorname{lcm}(q_r,q_s)\), then
   \[
   \operatorname{rank}M_{N;(r,s)}
   =q_r+q_s-\gcd(q_r,q_s).
   \]

4. **Kernel description — proved.**
   \[
   \ker M_{N;(r,s)}
   =\text{alternating cycle space of }G_{N;r,s}.
   \]

5. **Natural basis — proved.** Fundamental alternating cycles relative to any spanning forest form a basis of the kernel.

6. **Injectivity criterion — proved.**
   \[
   M_{N;(r,s)}\text{ is injective}
   \iff
   G_{N;r,s}\text{ is a forest}.
   \]

7. **Signless-Laplacian identity — proved.**
   \[
   M_{N;(r,s)}M_{N;(r,s)}^{*}=Q_G=D_G+A_G.
   \]
   Since \(G\) is bipartite, \(Q_G\) is diagonally similar to the ordinary Laplacian \(L_G=D_G-A_G\).

8. **Exact singular-spectrum formula — proved.** The nonzero singular values are
   \[
   \left\{\sqrt{\lambda_k(G_j)}:2\le k\le |V(G_j)|\right\}
   \]
   over all connected components \(G_j\).

9. **Exact conditioning formula — proved.**
   \[
   \kappa_2^{+}(M)
   =
   \sqrt{
   \frac{\max_j\lambda_{\max}(G_j)}
   {\min_j\lambda_2(G_j)}
   }.
   \]

10. **Full-period graph and spectrum — proved.** With
    \[
    g=\gcd(q_r,q_s),\quad m=q_r/g,\quad n=q_s/g,
    \]
    and \(N-1=t\operatorname{lcm}(q_r,q_s)\), the graph is \(g\) copies of \(K_{m,n}\) with edge multiplicity \(t\). The positive singular values are
    \[
    \sqrt{t(m+n)}^{\,[g]},\qquad
    \sqrt{tn}^{\,[g(m-1)]},\qquad
    \sqrt{tm}^{\,[g(n-1)]}.
    \]

11. **Finite verification — PASS.**
    - rank theorem verifier: 53,100 triples, zero mismatches;
    - kernel/nullity verifier: 8,704 triples, zero mismatches;
    - spectral verifier: 36,000 general cases and 4,500 full-period cases, zero mismatches.

Controlling files:

- `theory/MARGINAL-TWO-MODULUS-GRAPH-RANK-THEOREM-v1.1.md`;
- `theory/MARGINAL-TWO-MODULUS-KERNEL-CYCLE-BASIS-v1.1.md`;
- `theory/MARGINAL-TWO-MODULUS-SPECTRUM-CONDITIONING-v1.1.md`;
- `code/verify_marginal_two_modulus_graph_rank.py`;
- `code/verify_marginal_two_modulus_kernel_cycles.py`;
- `code/verify_marginal_two_modulus_spectrum.py`;
- `results/marginal_two_modulus_graph_rank_verification_v1.1.json`;
- `results/marginal_two_modulus_kernel_cycle_verification_v1.1.json`;
- `results/marginal_two_modulus_spectrum_verification_v1.1.json`.

#### Current target

**ACTIVE-001-D — Marginal versus coupled information.**

Compare \(M_{N;(r,s)}\) with \(J_{N;(r,s)}\) at the level of kernels, recoverability, and explicit information loss. Determine exactly when separate marginals recover the same information as the coupled joint signature.

#### Still open

- exact closed forms for arbitrary modulus families with three or more marginals;
- optimal conditioning under a measurement budget;
- comparison of marginal and coupled joint-signature information beyond rank;
- structured prime-supported weight classes.

### Deferred but available after ACTIVE-001

- character-row factorization through residue channels;
- restricted stable reconstruction;
- structured prime-supported weights;
- inter-fiber maps only after explicit definitions.

## 5. Continuous preservation rule

Every completed definition, experiment, proof attempt, counterexample, and audit unit must be committed to GitHub promptly. Failed conjectures and negative computations are retained rather than silently discarded.
