# Canonical Repairs v1 — Post Proof Audit

Status: `required integration before proof-audit closure`

This file records exact repairs forced by `PROOF-AUDIT-v1.md`. It adds no new research program.

## Repair R1 — general single-modulus injectivity criterion

For every \(N\ge2\) and \(r\ge1\),

\[
D_{N,r}\text{ is injective}
\iff
\frac r{\gcd(2,r)}\ge N-1.
\]

The existing large-odd-modulus corollary remains valid as a convenient sufficient case. For even \(r\), injectivity is equivalent to \(r\ge2(N-1)\).

## Repair R2 — formal codomain of the joint-signature operator

Let

\[
L=\operatorname{lcm}(r_1,\dots,r_s)
\]

and define the compatible-signature set

\[
\mathscr C_{\mathbf r}
=
\left\{(d\bmod r_1,\dots,d\bmod r_s):d\in\mathbb Z/L\mathbb Z\right\}.
\]

Then

\[
J_{N;\mathbf r}:V_N\longrightarrow\mathbb C^{\mathscr C_{\mathbf r}}
\]

is defined by

\[
(J_{N;\mathbf r}w)_{\mathbf d}
=
\sum_{\substack{1\le a\le N-1\\
(d_{N,r_1}(a),\dots,d_{N,r_s}(a))=\mathbf d}}
w_a.
\]

The map \(d\bmod L\mapsto(d\bmod r_1,\dots,d\bmod r_s)\) identifies \(\mathbb Z/L\mathbb Z\) bijectively with \(\mathscr C_{\mathbf r}\). Under this identification, \(J_{N;\mathbf r}\) is a row relabeling of \(D_{N,L}\).

## Repair R3 — explicit zero-frequency identity

For every \(w\in V_N\),

\[
\sum_{d\bmod r}(D_{N,r}w)_d
=
\sum_{a=1}^{N-1}w_a.
\]

Thus the total fiber weight is the \(k=0\) coordinate of the unnormalized discrete Fourier transform of \(D_{N,r}w\). Under unitary Fourier normalization, the coordinate differs by the factor \(r^{-1/2}\).

## Repair R4 — exact difference-phase criterion

Assume \(N\ge3\). The phase

\[
a\longmapsto e(\alpha(2a-N))
\]

is constant on \(1\le a\le N-1\) if and only if

\[
2\alpha\in\mathbb Z.
\]

Indeed, the ratio of two consecutive phase values is \(e(2\alpha)\). For \(N=2\), the fiber has one point, so every phase is constant.

## Repair R5 — character rows: classification correction

The prior status ledger classified the following as a proved corollary:

> Dirichlet-character rows are information-redundant relative to complete odd-modulus difference channels.

This statement is removed from the proved-corollary list until the relevant measurement operator is defined and the factorization is proved. During `THEORY-FREEZE-v1.0` it is classified as:

`pending derived observation — not part of the certified Paper 1 core`.

A future certification must specify:

1. the modulus and character convention;
2. whether the character acts on \(a\), \(N-a\), or the difference coordinate;
3. the treatment of nonunits;
4. the exact linear factorization through residue-channel data;
5. the scope in which “redundant” means no additional linear information.

## Integration rule

The proof audit is not closed merely by creating this repair note. Closure requires these repairs to be incorporated into the canonical core or explicitly cross-referenced from its theorem statements, followed by a numbering and dependency audit.