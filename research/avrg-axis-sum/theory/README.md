# AVRG / PVG Addition-Fiber Theory

This directory preserves the theory developed for translating additive number theory into prime-valuation geometry.

## Canonical documents

1. `PVG-ADDITION-FIBERS-FOUNDATIONS-001.md`
   - positive addition fibers;
   - no-loss valuation translation;
   - symmetry and counting measure;
   - additive convolution theorem;
   - prime and prime-power loci;
   - Goldbach intersection form;
   - residue subfibers and Dirichlet-character lifts.

2. `PVG-ANT-TRANSLATION-DICTIONARY-001.md`
   - precise PVG–ANT dictionary;
   - distinction between exact identities and interpretations;
   - candidate geometric observables;
   - governance rule for future translations.

3. `PVG-CIRCLE-METHOD-BRIDGE-001.md`
   - Fourier phases lifted through the recovery map;
   - circle-method identity;
   - major arcs as residue-fiber resonance;
   - local densities and the singular-series interpretation;
   - minor-arc wall;
   - correction showing that a symmetric product phase is constant on an exact addition fiber.

4. `PVG-ADDITION-FIBER-OPERATOR-001.md`
   - ambient pair space and exact fiber projection;
   - nontrivial difference-phase transform;
   - reflection parity and cosine/sine decomposition;
   - residue-difference channels and their finite Fourier transform;
   - joint Dirichlet-character/additive-difference transform;
   - exact bridge to prior AVRG orbit calculations.

## Central exact identity

For arithmetic functions \(f,g\),

\[
(f*_+g)(N)
=
\int_{\mathcal G_N}
\widehat f(x)\widehat g(y)\,d\mu_N.
\]

## Goldbach form

For even \(N\ge4\), binary Goldbach is equivalent to

\[
\mathcal G_N\cap(\mathcal P_1\times\mathcal P_1)\neq\varnothing.
\]

This is an exact reformulation, not a proof.

## Nontrivial internal transform

The symmetric product phase is constant on a fixed exact fiber. The nontrivial internal transform is instead

\[
\mathcal A_\alpha W(N)
=
\int_{\mathcal G_N}
W(x,y)e\bigl(\alpha(\rho(x)-\rho(y))\bigr)
\,d\mu_N.
\]

At rational frequencies \(\alpha=k/r\), this is the finite Fourier transform of the residue-difference channel masses modulo \(r\).

## Current next action

Build the exact reconstruction layer for the joint matrix

\[
\mathcal J_{\chi,k}(N)
=
\sum_{a+b=N}
\chi(a)W(\nu(a),\nu(b))e(k(a-b)/r).
\]

The immediate target is to prove which PASS013–PASS035 quantities are recovered by special rows, columns, parity sectors, and difference channels. No predictive model should be fitted before this reconstruction is complete.

## Scientific ceiling

No Goldbach proof, no new major-arc or minor-arc theorem, and no RH/GRH progress are claimed.
