# ACTIVE-001-E — Multi-Modulus Marginal versus Joint Factorization Status

Status: `COMPLETE — PROVED WITH FINITE VERIFICATION`

## Completed results

For every modulus family

\[
\mathbf r=(r_1,\dots,r_k),\qquad k\ge2,
\]

with realized joint-signature operator \(J_{N;\mathbf r}\), stacked marginal operator \(M_{N;\mathbf r}\), and cell-to-marginal incidence operator \(B_{N;\mathbf r}\):

1. **Exact factorization**
   \[
   M_{N;\mathbf r}=B_{N;\mathbf r}J_{N;\mathbf r}.
   \]

2. **Kernel inclusion**
   \[
   \ker J_{N;\mathbf r}\subseteq\ker M_{N;\mathbf r}.
   \]

3. **Joint-cell surjectivity**
   \[
   J_{N;\mathbf r}:V_N\twoheadrightarrow\mathbb C^{\Sigma_{N;\mathbf r}}.
   \]

4. **Exact information quotient**
   \[
   \ker M_{N;\mathbf r}/\ker J_{N;\mathbf r}
   \cong
   \ker B_{N;\mathbf r}.
   \]

5. **Exact rank gap**
   \[
   \operatorname{rank}J_{N;\mathbf r}
   -
   \operatorname{rank}M_{N;\mathbf r}
   =
   \dim\ker B_{N;\mathbf r}.
   \]

6. **Information-equivalence criterion**
   Separate marginals contain the same information as coupled cells exactly when the only realized cell array with all one-coordinate marginals zero is the zero array.

## Geometric interpretation

- For two moduli, \(B\) is a bipartite graph-incidence matrix and its kernel is the alternating cycle space.
- For three or more moduli, \(B\) is a \(k\)-partite \(k\)-uniform hypergraph-incidence matrix.
- No ordinary-graph cycle formula is claimed for \(k\ge3\).

## Verification

- cases checked: `925`;
- three-modulus families: all combinations from `2..8`, with `2 <= N <= 25`;
- four-modulus families: all combinations from `2..6`, with `2 <= N <= 18`;
- mismatches: `0`;
- maximum observed rank gap: `16`;
- result: `PASS`.

## Controlling files

- `theory/MULTI-MODULUS-MARGINAL-VS-JOINT-FACTORIZATION-v1.1.md`;
- `code/verify_multi_modulus_marginal_joint_factorization.py`;
- `results/multi_modulus_marginal_joint_factorization_verification_v1.1.json`.

## Next target

`ACTIVE-001-F — Rank structure of multi-partite signature incidence matrices.`

The next step is to determine which combinatorial invariants control

\[
\operatorname{rank}B_{N;\mathbf r}
\]

for \(k\ge3\), beginning with exact row-dependency spaces and full-period families. No closed formula is claimed yet.

## Scientific ceiling

No Goldbach proof, prime-producing estimate, sieve improvement, circle-method improvement, RH/GRH progress, novelty claim, or priority claim is made by this unit.
