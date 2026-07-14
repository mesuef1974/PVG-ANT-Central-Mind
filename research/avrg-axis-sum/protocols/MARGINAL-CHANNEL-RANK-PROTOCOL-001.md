# Marginal-Channel Rank Study 001

## Status

Preregistered next theorem/computation target. No general formula is asserted here.

## 1. Object

For \(N\ge2\) and moduli \(\mathbf r=(r_1,\ldots,r_s)\), define the vertically stacked marginal operator

\[
M_{N;\mathbf r}
=
\begin{pmatrix}
D_{N,r_1}\\
\vdots\\
D_{N,r_s}
\end{pmatrix}
:
\mathbb C^{N-1}
\longrightarrow
\bigoplus_{j=1}^s\mathbb C^{r_j}.
\]

Unlike the joint operator, \(M_{N;\mathbf r}\) records each modular histogram separately and does not record joint residue tuples.

## 2. Primary questions

Determine:

\[
\operatorname{rank}M_{N;\mathbf r},
\qquad
\dim\ker M_{N;\mathbf r},
\qquad
\sigma_{\min}^+(M_{N;\mathbf r}),
\]

where \(\sigma_{\min}^+\) is the smallest nonzero singular value.

## 3. Locked distinctions

The study must not conflate:

1. separate marginals \(M_{N;\mathbf r}\);
2. the joint signature operator \(J_{N;\mathbf r}\);
3. a single lcm channel \(D_{N,L}\);
4. Fourier transforms of the same full channel data.

Only items 2 and 3 are equivalent up to row relabeling.

## 4. Baseline bounds

The following bounds are immediate and will be used only as checks:

\[
\max_j\operatorname{rank}D_{N,r_j}
\le
\operatorname{rank}M_{N;\mathbf r}
\le
\min\left(N-1,\sum_j\operatorname{rank}D_{N,r_j}\right).
\]

Since each block contains the all-ones row in its row span, the naive upper sum generally overcounts at least repeated total-mass information.

## 5. Computational scan

The first scan will cover:

- \(2\le N\le200\);
- modulus sets of size \(1\) through \(4\);
- moduli \(2\le r_j\le25\);
- ordered sets removed by canonical sorting;
- exact rational rank where feasible;
- floating singular values only as secondary diagnostics.

For each case, record:

- \(N\);
- modulus set;
- single-block ranks;
- stacked rank;
- kernel dimension;
- lcm;
- joint-channel rank;
- marginal-to-joint rank gap;
- smallest nonzero singular value;
- condition number on the row-space image.

## 6. Pattern search

Test candidate dependencies on:

- divisibility lattice among the moduli;
- \(\gcd(r_i,r_j)\);
- \(\operatorname{lcm}(r_1,\ldots,r_s)\);
- parity;
- truncation length \(N-1\);
- inclusion-exclusion of periodic row spaces.

No candidate formula becomes a theorem until it has an independent proof.

## 7. Exact algebraic viewpoint

Rows of \(D_{N,r}\) are restrictions to \(\{1,\ldots,N-1\}\) of indicator functions of congruence classes of \(2a-N\pmod r\). Therefore the row space of \(M_{N;\mathbf r}\) is the sum of several finite periodic-function spaces restricted to a finite interval.

The likely proof language is:

- periodic subspace intersections;
- divisor lattices;
- finite Fourier characters;
- and restriction maps from functions on \(\mathbb Z/L\mathbb Z\).

## 8. Success criteria

The pass succeeds scientifically if it produces at least one of:

1. a proved exact rank formula for a nontrivial class of modulus sets;
2. a proved upper/lower bound sharper than the baseline;
3. a complete characterization of when stacked marginals are injective;
4. a rigorous counterexample to a natural candidate formula;
5. a stable computational conjecture with all exceptions explicitly catalogued.

## 9. Governance

- Exact identities, computational observations, conjectures, and theorems must be labeled separately.
- No claim of originality or priority is made before a targeted literature review.
- No Goldbach, RH, or GRH progress follows from a finite marginal-rank result alone.
