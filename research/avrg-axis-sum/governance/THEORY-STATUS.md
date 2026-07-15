# PVG Addition Fibers Theory — Status

Status: `THEORY-FREEZE-v1.0`

This file is the canonical classification ledger for the current theory. New concepts must not enter the core theory during the freeze unless they repair a logical gap.

## 1. Accepted definitions

- **D1. Prime valuation vector**: \(\nu(n)=(v_p(n))_{p\in\mathbb P}\).
- **D2. Recovery map**: \(\rho(x)=\prod_p p^{x_p}\).
- **D3. Positive addition fiber**: \(\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}\).
- **D4. Prime-valuation addition fiber**: \(\mathcal G_N=(\nu\times\nu)(\mathcal F_N^+)\).
- **D5. Fiber counting measure**: \(\mu_N=\sum_{a=1}^{N-1}\delta_{(\nu(a),\nu(N-a))}\).
- **D6. Fiber weight space**: \(V_N=\mathbb C^{N-1}\), indexed by \(1\le a\le N-1\).
- **D7. Difference-channel operator**: \((D_{N,r}w)_d=\sum_{2a-N\equiv d\,(\mathrm{mod}\,r)}w_a\).
- **D8. Joint-modulus channel operator**: formally defined on the realized joint-signature set \(\Sigma_{\mathbf r}\).
- **D9. Marginal stacked operator**: vertical stack of separate operators \(D_{N,r_j}\).
- **D10. Prime point locus**: \(\mathcal P_1=\{e_p:p\in\mathbb P\}\).
- **D11. Prime-power axis locus**: \(\mathcal A_1=\{k e_p:p\in\mathbb P,\ k\ge1\}\).
- **D12. Difference-phase transform**: weighted transform using \(e(\alpha(a-b))\) on a fixed addition fiber.

## 2. Proved theorems

- **T1. No-information-loss theorem**: \((a,b)\mapsto(\nu(a),\nu(b))\) is a bijection from \(\mathcal F_N^+\) to \(\mathcal G_N\).
- **T2. Fiber convolution identity**:
  \[
  (f*_+g)(N)=\int_{\mathcal G_N}\widehat f(x)\widehat g(y)\,d\mu_N.
  \]
- **T3. Fiber symmetry theorem**: swapping the two coordinates preserves \(\mathcal G_N\) and induces a \(\mathbb Z/2\mathbb Z\)-action.
- **T4. Single-modulus rank theorem**:
  \[
  \operatorname{rank}D_{N,r}=\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
  \]
- **T5. Kernel-dimension formula**:
  \[
  \dim\ker D_{N,r}=N-1-\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
  \]
- **T6. Joint-modulus rank theorem**: for \(L=\operatorname{lcm}(r_1,\dots,r_s)\),
  \[
  \operatorname{rank}J_{N;\mathbf r}=\min\!\left(N-1,\frac L{\gcd(2,L)}\right).
  \]
- **T7. Joint-modulus conditioning theorem**: when the joint operator is injective, its singular values are all equal to \(1\), hence \(\kappa_2=1\).
- **T8. Fourier equivalence of complete difference channels**: applying the full finite Fourier transform preserves rank and information.

## 3. Proved corollaries and propositions

- **C1. Exact single-modulus reconstruction criterion**:
  \[
  D_{N,r}\text{ injective}\iff \frac r{\gcd(2,r)}\ge N-1.
  \]
- **C2. Full joint reconstruction**:
  \[
  J_{N;\mathbf r}\text{ injective}\iff \frac L{\gcd(2,L)}\ge N-1.
  \]
- **C3. Zero-frequency identity**:
  \[
  \sum_{d\bmod r}(D_{N,r}w)_d=\sum_{a=1}^{N-1}w_a.
  \]
- **C4. Difference-phase constancy criterion**: the phase \(a\mapsto e(\alpha(2a-N))\) is constant on the whole fiber exactly when \(2\alpha\in\mathbb Z\).

## 4. Pending derived observations

- **P1. Character-row redundancy**: not certified in the canonical Paper 1 core. It remains deferred until the operator, nonunit convention, and exact factorization are defined and proved.

## 5. Exact reformulations, not new theorems about primes

- **R1. Goldbach intersection form**:
  \[
  G(N)>0\iff \mathcal G_N\cap(\mathcal P_1\times\mathcal P_1)\ne\varnothing.
  \]
- **R2. Von Mangoldt support form**: \(\widehat\Lambda\) is supported on \(\mathcal A_1\).
- **R3. Circle-method bridge**: additive convolution equals a Fourier coefficient of the lifted exponential sum.
- **R4. Residue-fiber interpretation of major arcs and local factors**: interpretation only, not a new estimate.

## 6. Open problems approved for later activation

- **O1. Marginal stacked rank problem**.
- **O2. Natural-basis problem for invisible deformations**.
- **O3. Restricted stable reconstruction**.
- **O4. Literature-priority problem**.

## 7. Frozen research programs

The following remain outside the accepted core during `THEORY-FREEZE-v1.0`:

- observable algebra beyond Paper 1;
- fiber signatures and invariant classification;
- inter-fiber dynamics, networks, categories, and morphisms;
- nonlinear manifold models;
- new Goldbach, sieve, or circle-method claims;
- global spectral theories not forced by current proved results.

They are recorded only in `IMPORTANT-IDEAS-TODO.md`.

## 8. Freeze completion checklist

1. Canonical notation ledger — **complete**.
2. Canonical definitions and theorem statements — **repairs integrated**.
3. Hand-checkable examples \(N=10,12,24,30\) — **complete**.
4. Proof audit for hypotheses, edge cases, and hidden conventions — **first pass complete**.
5. Dependency and numbering audit — **complete; PASS**.
6. Theorem-to-evidence and computational cross-links — **complete for the single-modulus theory**.
7. Dedicated joint-modulus worked example for T6, T7, and C2 — **next; documentation/test task only**.
8. Focused literature review before any priority claim — **pending**.

## 9. Evidence coverage outcome

- T1, T2, T3, T4, T5, C1, C3, R1, and R2 have proof plus hand-checkable evidence.
- T4, T5, C1, and C3 are additionally linked to a finite verifier covering 9,900 pairs \((N,r)\) with \(2\le N\le100\) and \(1\le r\le100\), with zero rank mismatches.
- T6, T7, and C2 are proved, but still need one dedicated worked joint-modulus example for exposition and test coverage.
- T8 follows from invertibility of the full DFT and does not require a numerical certificate.
- P1 remains correctly excluded from the proved core.
- Canonical evidence registry: `THEOREM-EVIDENCE-CROSSLINKS-v1.md`.

## 10. Audit outcome

- No counterexample was found to the canonical proved results.
- Joint-signature codomain is explicit.
- Exact phase constancy and general injectivity criteria are integrated.
- Zero-frequency identity is proved in the canonical core.
- Character-row redundancy remains correctly deferred.
- Numbering, dependencies, hidden conventions, and evidence cross-links pass the current structural audit.

## 11. Scientific ceiling

No result in this ledger proves Goldbach, improves a known major-arc or minor-arc bound, or constitutes progress on RH/GRH. The current contribution is an exact framework, rank/reconstruction theory for defined channel operators, and a governed research program.
