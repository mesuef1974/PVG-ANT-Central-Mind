# BRIDGE-RESIDUE-CHARACTER-FOURIER-001

**Family:** residue fibers / characters  
**Maturity:** L2 analytic  
**Classification:** Known exact Fourier bridge / normalization diagnostic

## Classical object

Reduced residue classes, Dirichlet characters, and variance across residue fibers.

## PVG object

Labeled valuation points projected modulo `q`, followed by finite Fourier coordinates on `(Z/qZ)^×`.

## Exact forward map

For reduced residues,

\[
\mathbf1_{n\equiv a\pmod q}
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n).
\]

Subtracting the principal component isolates non-principal character fluctuations. Parseval converts fiber `L²` energy into a character second moment, with the normalization written explicitly.

## Reverse map and loss

The complete set of character coefficients reconstructs a function on the reduced residue group. Taking only total energy loses character phase and identity. Unlabeled exponent multisets do not determine a residue class.

## Hypotheses

Reduced residues, fixed character convention, fixed normalization, and explicit handling of `χ₀`.

## Simplification gain

**Analytic:** arithmetic fibers diagonalize into finite Fourier coordinates.

## Finite certificate

`EX-RESIDUE-001`: all four residue indicators modulo `5` are reconstructed from the four characters of `(Z/5Z)^×`.

## Research use

Supports residue-fiber observables and character moment problems. It does not imply GRH or a distribution theorem without bounds on the character coordinates.

## Sources

Tenenbaum residue-fiber layer and reconciled OP-005 normalization/Parseval bridges.
