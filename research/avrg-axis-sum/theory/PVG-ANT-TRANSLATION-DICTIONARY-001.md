# PVG–ANT Translation Dictionary 001

Status: exact dictionary where stated; research interpretations labeled separately.

## Core dictionary

| Analytic number theory | Prime-valuation geometry |
|---|---|
| integer \(n\) | valuation vector \(\nu(n)\) |
| recovery of \(n\) | \(\rho(x)=\prod_p p^{x_p}\) |
| pair \(a+b=N\) | point \((\nu(a),\nu(b))\in\mathcal G_N\) |
| additive convolution at \(N\) | weighted counting integral on \(\mathcal G_N\) |
| swap \(a\leftrightarrow N-a\) | reflection \(\sigma(x,y)=(y,x)\) |
| prime \(p\) | axis vertex \(e_p\) |
| prime power \(p^k\) | axis point \(k e_p\) |
| \(\mathbf1_{\mathbb P}\) | indicator of \(\mathcal P_1=\{e_p\}\) |
| \(\Lambda\) | weight supported on \(\mathcal A_1=\{k e_p\}\) |
| Goldbach representation | intersection of \(\mathcal G_N\) with \(\mathcal P_1^2\) |
| residue class \(n\bmod r\) | color of \(x\) determined by \(\rho(x)\bmod r\) |
| Dirichlet character \(\chi(n)\) | phase field \(\widehat\chi(x)=\chi(\rho(x))\) |
| arithmetic-progression decomposition | decomposition into residue subfibers |
| additive Fourier phase \(e(\alpha n)\) | nonlinear valuation wave \(\mathcal E_\alpha(x)=e(\alpha\rho(x))\) |
| circle-method major arc | resonance with a small-modulus residue-fiber partition |
| circle-method minor arc | nonresonant cancellation across valuation waves |
| singular series | Euler product of normalized local residue-fiber densities |

## Translation law

For arithmetic weights \(f,g\),

\[
(f*_+g)(N)
=
\int_{\mathcal G_N}
\widehat f(x)\widehat g(y)\,d\mu_N.
\]

This is the master exact translation law.

## Two representations of an integer

Every positive integer has two complementary PVG representations.

### Point representation

\[
N\longmapsto\nu(N).
\]

This is best suited to multiplicative structure because

\[
\nu(ab)=\nu(a)+\nu(b).
\]

### Addition-fiber representation

\[
N\longmapsto\mathcal G_N.
\]

This is best suited to additive convolutions because it contains every decomposition \(a+b=N\).

The project should not collapse these two layers. The point representation handles multiplicative geometry; the fiber representation handles additive geometry.

## Exact versus interpretive claims

### Exact

- \(\nu\) is injective on positive integers.
- \(\mathcal F_N^+\cong\mathcal G_N\).
- additive convolutions are weighted sums over \(\mathcal G_N\).
- residue decompositions and character twists lift exactly.
- Fourier orthogonality and the circle-method integral lift exactly through \(\rho\).

### Interpretive/research language

- "prime-axis waves" for the terms \(\widehat\Lambda(x)\mathcal E_\alpha(x)\).
- "residue-fiber resonance" for major-arc behavior.
- "fiber geometry" as a source of new observables or diagnostics.
- comparison of fibers by distance spectra, support overlap, height, or graph structure.

These interpretations are useful only if they lead to identities, estimates, or predictive diagnostics beyond a relabeling of known arithmetic.

## Candidate geometric observables

For \((x,y)=(\nu(a),\nu(N-a))\), possible observables include

\[
D_q(x,y)=\|x-y\|_q,
\]

\[
H(x,y)=\Omega(a)+\Omega(N-a)
=\sum_p x_p+\sum_p y_p,
\]

\[
C(x,y)=|\operatorname{supp}(x)\cap\operatorname{supp}(y)|,
\]

and residue-orbit coordinates such as

\[
\rho(x)-\rho(y)\pmod r.
\]

These are diagnostics, not established drivers of Goldbach representation counts.

## Governance rule

Every future PVG–ANT translation should state:

1. the original arithmetic object;
2. the lifted PVG object;
3. whether the relation is an exact identity, a reinterpretation, a finite diagnostic, or a conjectural mechanism;
4. the information gained beyond invertible re-encoding;
5. the analytic wall still missing.
