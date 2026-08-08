# PVG Addition Fibers — Canonical Notation

Status: `LOCKED-FOR-THEORY-FREEZE-v1.0`

This file fixes the notation used in Paper 1 and the supporting theory files. Alternative symbols may appear in historical documents, but new core work must use this ledger.

## 1. Basic arithmetic and valuation notation

| Symbol | Meaning |
|---|---|
| \(\mathbb P\) | Set of prime numbers |
| \(v_p(n)\) | Exponent of the prime \(p\) in \(n\) |
| \(\nu(n)\) | Prime-valuation vector \((v_p(n))_{p\in\mathbb P}\) |
| \(e_p\) | Unit vector on the prime axis \(p\) |
| \(\rho(x)\) | Recovery map \(\prod_p p^{x_p}\) |
| \(\operatorname{supp}(x)\) | \(\{p:x_p\ne0\}\) |
| \(\Omega(n)\) | Total number of prime factors counted with multiplicity |
| \(\omega(n)\) | Number of distinct prime factors |

Conventions:

- \(\nu(1)=0\).
- All valuation vectors have finite support.
- The recovery map is used only on finite-support nonnegative integer vectors unless explicitly extended.

## 2. Addition fibers

| Symbol | Meaning |
|---|---|
| \(N\) | Fixed integer fiber index, usually \(N\ge2\) |
| \(\mathcal F_N^+\) | Positive ordered addition fiber \(\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}\) |
| \(\mathcal G_N\) | Prime-valuation addition fiber \((\nu\times\nu)(\mathcal F_N^+)\) |
| \(P_a\) | Fiber point \((\nu(a),\nu(N-a))\), \(1\le a\le N-1\) |
| \(\sigma\) | Coordinate swap \(\sigma(x,y)=(y,x)\) |
| \(\mu_N\) | Counting measure \(\sum_{a=1}^{N-1}\delta_{P_a}\) |

The ordered fiber is canonical for reconstruction theory. Unordered quotients must be written explicitly as

\[
\mathcal G_N/\langle\sigma\rangle.
\]

## 3. Lifted arithmetic functions and additive convolution

| Symbol | Meaning |
|---|---|
| \(f,g\) | Arithmetic functions on \(\mathbb N\) |
| \(\widehat f(x)\) | Lift \(f(\rho(x))\) to valuation space |
| \((f*_+g)(N)\) | Additive convolution \(\sum_{a+b=N}f(a)g(b)\) |
| \(\mathbf1_{\mathbb P}\) | Prime indicator |
| \(\Lambda\) | Von Mangoldt function |
| \(\mathcal P_1\) | Prime point locus \(\{e_p:p\in\mathbb P\}\) |
| \(\mathcal A_1\) | Prime-power axis locus \(\{k e_p:p\in\mathbb P,\ k\ge1\}\) |

Do not use \(*\) without a subscript for additive convolution in Paper 1; write \(*_+\).

## 4. Fiber weights and measurement spaces

| Symbol | Meaning |
|---|---|
| \(V_N\) | Fiber weight space \(\mathbb C^{N-1}\) |
| \(w\) | Weight vector \((w_a)_{a=1}^{N-1}\in V_N\) |
| \(L_0(w)\) | Total-weight observable \(\sum_a w_a\) |
| \(A\) | Generic linear measurement operator |
| \(\ker A\) | Invisible-deformation space for that operator |
| \(\operatorname{rank}A\) | Linear rank over \(\mathbb C\) unless specified otherwise |
| \(\sigma_{\min}^+(A)\) | Smallest positive singular value |
| \(\kappa_2(A)\) | Spectral condition number on the injective/nonzero singular subspace |

The phrase “minimal reconstruction” must distinguish:

- number of scalar measurements;
- number of vector-valued channel families;
- structured versus arbitrary weights.

## 5. Difference channels

For a modulus \(r\ge1\), define the difference label

\[
d_{N,r}(a)=2a-N\pmod r.
\]

| Symbol | Meaning |
|---|---|
| \(D_{N,r}\) | Complete difference-channel operator modulo \(r\) |
| \((D_{N,r}w)_d\) | \(\sum_{d_{N,r}(a)=d}w_a\) |
| \(F_r\) | Full discrete Fourier transform on \(\mathbb Z/r\mathbb Z\) |
| \(\widehat M_{N,r,w}\) | Fourier transform of the difference-channel vector, when needed |

The symbol \(M\) is reserved for measured channel data or stacked marginal operators, not for the basic single-modulus operator.

## 6. Multiple moduli

Let \(\mathbf r=(r_1,\dots,r_s)\) and

\[
L=\operatorname{lcm}(r_1,\dots,r_s).
\]

| Symbol | Meaning |
|---|---|
| \(J_{N;\mathbf r}\) | Joint-signature channel operator preserving the full compatible residue tuple |
| \(M_{N;\mathbf r}\) | Marginal stacked operator \(\begin{pmatrix}D_{N,r_1}\\ \vdots\\ D_{N,r_s}\end{pmatrix}\) |
| \(L\) | Least common multiple of the modulus family |

Never identify \(J_{N;\mathbf r}\) with \(M_{N;\mathbf r}\). The former preserves cross-modulus coupling; the latter retains only separate marginals.

## 7. Fourier and phase notation

| Symbol | Meaning |
|---|---|
| \(e(t)\) | \(e^{2\pi i t}\) |
| \(\mathcal E_\alpha(x)\) | Lifted additive phase \(e(\alpha\rho(x))\) |
| \(\mathcal A_\alpha w(N)\) | Difference-phase transform \(\sum_{a=1}^{N-1}w_a e(\alpha(a-(N-a)))\) |

On a fixed exact fiber,

\[
\mathcal E_\alpha(x)\mathcal E_\alpha(y)=e(\alpha N),
\]

so this symmetric product phase is constant and must not be presented as a nontrivial fiber spectral observable.

## 8. Residues and characters

| Symbol | Meaning |
|---|---|
| \(r,q\) | Moduli; use \(r\) in reconstruction sections and \(q\) in circle-method sections |
| \(\chi\) | Dirichlet character modulo the stated modulus |
| \(\widehat\chi(x)\) | Lift \(\chi(\rho(x))\) |
| \(\mathcal G_{N;r}^{c,N-c}\) | Residue subfiber with first coordinate \(c\pmod r\) |
| \(c_q(N)\) | Ramanujan sum |
| \(\mathfrak S(N)\) | Singular series, only in ANT/circle-method sections |

## 9. Result labels

Use these prefixes consistently:

- **Definition** for introduced objects.
- **Theorem** only for proved statements.
- **Corollary** for immediate proved consequences.
- **Proposition** for auxiliary proved statements.
- **Exact reformulation** for logically equivalent restatements of known arithmetic questions.
- **Computational observation** for finite verified patterns without proof.
- **Conjecture** only when an explicit unproved mathematical statement is intentionally advanced.
- **Open problem** for a precise unresolved question.
- **Research program** for a broader direction not yet reduced to one claim.

## 10. Prohibited ambiguity during the freeze

- Do not use “axis addition” as if \(\nu(a+b)=\nu(a)+\nu(b)\); this is false in general.
- Do not call a reformulation of Goldbach a proof or progress toward a proof.
- Do not call a set of all functions on a finite fiber a novel observable algebra without a restricted natural generating class.
- Do not use “fiber bundle,” “category,” “gauge theory,” or “manifold” as technical claims unless the required structures are formally defined and proved.
- Do not change the symbols in this ledger without a dedicated notation-migration commit.
