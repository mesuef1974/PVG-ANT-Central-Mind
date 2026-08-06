# Left Preconditioning and Row Normalization for Marginal Operators

Status: `PROVED CORE + COMPUTATIONAL STUDY`

Version: `v1.1`

## 1. Object

Let

\[
M=M_{N;\mathbf q}
\]

be the stacked marginal operator after replacing each modulus by its effective period

\[
q_j=\frac{r_j}{\gcd(2,r_j)}.
\]

Let \(P\) be any invertible diagonal matrix acting on the measurement rows. Define the left-preconditioned operator

\[
\widetilde M=PM.
\]

## 2. Information-preservation theorem

Because \(P\) is invertible,

\[
\ker(PM)=\ker M,
\qquad
\operatorname{rank}(PM)=\operatorname{rank}M.
\]

Hence invertible left preconditioning changes neither recoverability nor the invisible-deformation space. It changes only the Euclidean geometry of the measurement coordinates and therefore may change the positive singular spectrum and \(\kappa_2^+\).

This is a strict information-preservation statement. Preconditioning cannot create information absent from \(M\).

## 3. Row normalization

For each nonzero row \(m_i^*\), define

\[
p_i=\frac{1}{\|m_i\|_2},
\qquad
P_{\rm row}=\operatorname{diag}(p_i).
\]

Then every row of

\[
M_{\rm row}=P_{\rm row}M
\]

has Euclidean norm one.

For residue aggregation matrices, each row norm is the square root of the number of fiber indices in the corresponding residue class. Thus row normalization compensates for unequal class occupancy.

## 4. Block scaling

If block \(M_j\) corresponds to period \(q_j\), any positive block weights \(\alpha_j>0\) give

\[
M_{\boldsymbol\alpha}
=
\begin{pmatrix}
\alpha_1M_1\\
\vdots\\
\alpha_kM_k
\end{pmatrix}.
\]

This also preserves rank and kernel.

However, Frobenius normalization of entire blocks is vacuous in this model: every column contributes exactly one unit entry to every block, so

\[
\|M_j\|_F^2=N-1
\]

for every \(j\). Therefore all blocks receive the same Frobenius scale, which cannot change the condition number.

This negative result rules out an apparently natural but ineffective normalization.

## 5. Conditioning objective

For any information-preserving preconditioner \(P\), define

\[
\kappa_2^+(PM)
=
\frac{\sigma_{\max}(PM)}{\sigma_{\min}^+(PM)}.
\]

The design problem is

\[
\inf_{P\in\mathcal P}\kappa_2^+(PM)
\]

for a declared admissible class \(\mathcal P\), such as positive diagonal row scalings or positive block-diagonal scalings.

No claim is made here that row normalization is globally optimal over positive diagonal scalings. It is a canonical, information-preserving baseline.

## 6. Verified observations

For the benchmark designs studied in `row_preconditioning_verification_v1.1.json`, row normalization preserved rank in every case and reduced \(\kappa_2^+\) in every listed nontrivial design.

Examples:

- \(N=24,\ \mathbf q=\{5,9,11\}\):
  \[
  108.7134\longrightarrow92.4884.
  \]
- \(N=24,\ \mathbf q=\{7,9,11\}\):
  \[
  32.3756\longrightarrow29.5267.
  \]
- \(N=30,\ \mathbf q=\{5,7,9,11\}\):
  \[
  1938.1831\longrightarrow1763.5913.
  \]

These are computations, not universal monotonicity theorems.

## 7. Scientific ceiling

- Left preconditioning preserves information only when the left multiplier is invertible on the retained measurement rows.
- Row normalization can improve or worsen conditioning in other matrix families; no universal improvement theorem is claimed.
- Numerical singular values depend on a declared tolerance.
- This unit concerns finite linear reconstruction only and makes no Goldbach, sieve, RH, or GRH claim.
