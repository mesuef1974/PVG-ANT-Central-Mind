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
- **D8. Joint-modulus channel operator**: channel indexed by the full compatible residue signature across a fixed modulus family.
- **D9. Marginal stacked operator**: vertical stack of separate operators \(D_{N,r_j}\).
- **D10. Prime point locus**: \(\mathcal P_1=\{e_p:p\in\mathbb P\}\).
- **D11. Prime-power axis locus**: \(\mathcal A_1=\{k e_p:p\in\mathbb P,\ k\ge1\}\).
- **D12. Difference-phase transform**: weighted transform using \(e(\alpha(a-b))\) on a fixed addition fiber.

## 2. Proved theorems

- **T1. No-information-loss theorem**: \((a,b)\mapsto(\nu(a),\nu(b))\) is a bijection from \(\mathcal F_N^+\) to \(\mathcal G_N\).
- **T2. Fiber convolution identity**: for arithmetic functions \(f,g\),
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
- **T7. Joint-modulus conditioning theorem**: when the joint operator is injective, its nonzero singular values are all equal to \(1\), hence \(\kappa_2=1\).
- **T8. Fourier equivalence of complete difference channels**: applying the full finite Fourier transform to all difference channels preserves rank and information.

## 3. Proved corollaries

- **C1. Full single-modulus reconstruction**: if \(r\) is odd and \(r\ge N-1\), then \(D_{N,r}\) is injective and
  \[
  w_a=(D_{N,r}w)_{2a-N\, (\mathrm{mod}\,r)}.
  \]
- **C2. Full joint reconstruction**: a joint modulus family is injective iff
  \[
  \frac L{\gcd(2,L)}\ge N-1.
  \]
- **C3. Zero frequency is redundant**: the ordinary total sum is the zero Fourier mode of the complete difference-channel vector.
- **C4. Dirichlet-character rows are information-redundant relative to complete odd-modulus difference channels**, while remaining analytically meaningful.

## 4. Exact reformulations, not new theorems about primes

- **R1. Goldbach intersection form**:
  \[
  G(N)>0\iff \mathcal G_N\cap(\mathcal P_1\times\mathcal P_1)\ne\varnothing.
  \]
- **R2. Von Mangoldt support form**: \(\widehat\Lambda\) is supported on \(\mathcal A_1\).
- **R3. Circle-method bridge**: additive convolution equals a Fourier coefficient of the lifted exponential sum.
- **R4. Residue-fiber interpretation of major arcs and local factors**: geometric interpretation of standard analytic structure, not a new major-arc estimate.

## 5. Open problems approved for later activation

- **O1. Marginal stacked rank problem**: determine \(\operatorname{rank}M_{N;\mathbf r}\), its kernel, and its singular spectrum.
- **O2. Natural-basis problem for invisible deformations**: describe geometrically natural generators for kernels of restricted measurement operators.
- **O3. Restricted stable reconstruction**: optimize injectivity and conditioning under a fixed observable budget or structured signal class.
- **O4. Literature-priority problem**: determine whether the combined addition-fiber/reconstruction framework has a precise precedent.

## 6. Frozen research programs

The following remain outside the accepted core during `THEORY-FREEZE-v1.0`:

- observable algebra beyond definitions required by Paper 1;
- fiber signatures and invariant classification;
- inter-fiber dynamics, networks, categories, and morphisms;
- nonlinear manifold models;
- new Goldbach, sieve, or circle-method claims;
- global spectral theories not forced by current proved results.

They are recorded only in `IMPORTANT-IDEAS-TODO.md`.

## 7. Freeze completion checklist

1. Canonical notation ledger — **complete**.
2. Canonical definitions and theorem statements — **v1 complete; final numbering audit pending**.
3. Hand-checkable examples:
   - \(N=10\) — **complete**;
   - \(N=12\) — **complete**;
   - \(N=24\) — **complete**;
   - \(N=30\) — **complete**.
4. Proof audit for hypotheses, edge cases, and hidden conventions — **next**.
5. Cross-links from theorems to computational verification — **pending**.
6. Focused literature review before any priority claim — **pending**.

## 8. Scientific ceiling

No result in this ledger proves Goldbach, improves a known major-arc or minor-arc bound, or constitutes progress on RH/GRH. The current contribution is an exact framework, rank/reconstruction theory for defined channel operators, and a governed research program.