# COF-FOUNDATION-002 Dependency Matrix

Status: `validated`

| Result | Finite search | Admissible upper bound | Additive certificate form | Nonnegative contributions | Exact cardinality budget | Canonical dominance/exchange | Fourier/PVG |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Safe pruning | yes | yes | no | no | no | no | no |
| Abstract branch-and-bound exactness | yes | yes | no | no | only for the displayed tree | no | no |
| Coordinatewise optimistic bound | yes | constructed | yes | used in the verified monotone-gain realization | yes | no | no |
| Canonical optimal solution | yes | no | yes | not required by exchange itself | exchange preserves cardinality | yes | no |
| Inclusion propagation | yes | no | no | no | no | yes | no |
| Exclusion propagation | yes | no | no | no | no | yes | no |
| Contradiction pruning | yes | no | no | no | no | yes | no |
| Budget pruning after propagation | yes | no | no | no | yes | yes | no |
| Precedence-aware BnB exactness | yes | yes | only through exchange realization | no | yes | yes | no |
| Fourier-frequency realization | yes | yes | yes | yes, because G_k(c)=P_k(c)+|P_k(c)| | yes | yes | yes |

## Main audit conclusion

The exact-search theorem is more general than the additive COF realization. Additivity, nonnegative gains, and precedence are construction tools for useful bounds and canonical reductions, not axioms of branch-and-bound correctness.

## Boundary

This matrix does not authorize arbitrary nonlinear feasibility constraints. Such a generalization requires a separately proved completion oracle, admissible bound, and propagation soundness theorem.