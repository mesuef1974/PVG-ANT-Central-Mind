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

Targets:

1. exact rank for two moduli;
2. kernel description;
3. graph/incidence representation;
4. singular spectrum and conditioning;
5. comparison with the coupled joint-signature operator \(J_{N;\mathbf r}\).

Current classification: `ACTIVE RESEARCH — NO GENERAL THEOREM CLAIM YET`.

### Deferred but available after ACTIVE-001

- character-row factorization through residue channels;
- natural kernel bases;
- restricted stable reconstruction;
- structured prime-supported weights;
- inter-fiber maps only after explicit definitions.

## 5. Continuous preservation rule

Every completed definition, experiment, proof attempt, counterexample, and audit unit must be committed to GitHub promptly. Failed conjectures and negative computations are retained rather than silently discarded.
