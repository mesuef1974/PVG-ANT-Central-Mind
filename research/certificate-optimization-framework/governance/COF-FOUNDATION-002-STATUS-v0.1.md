# COF-FOUNDATION-002 Status

Status: `VALIDATED_FOUNDATION`

Unit: `COF-FOUNDATION-002`

Title: `Exact Branch-and-Bound and Precedence Propagation`

## Added

- abstract finite certificate optimization problem;
- search-node and completion-family definitions;
- admissible upper-bound definition;
- safe-pruning theorem;
- exact branch-and-bound theorem;
- coordinatewise optimistic upper bound for additive cardinality-budget structures;
- canonical dominance and precedence closure;
- inclusion and exclusion propagation theorems;
- contradiction and budget pruning after propagation;
- exactness theorem for precedence-aware search;
- dependency matrix separating abstract search correctness from additive and precedence assumptions;
- exact Fourier/PVG realization.

## Principal dependency correction

Branch-and-bound exactness does **not** require:

- additive certificate bounds;
- nonnegative contributions;
- Fourier structure;
- PVG structure;
- dominance.

It requires only:

1. a finite exhaustively branched feasible search space;
2. exact evaluation of terminal feasible configurations;
3. an admissible upper bound for every pruned node.

The additive certificate structure and cardinality budget are sufficient ingredients for the verified coordinatewise optimistic bound. Dominance and the exchange theorem are sufficient ingredients for canonical precedence propagation.

## Scientific classification

- abstract safe pruning: proved;
- abstract exact BnB: proved;
- additive cardinality upper bound: proved;
- precedence propagation: proved under canonical exchange;
- Fourier/PVG mapping: exact realization;
- general COF theory: not yet complete;
- transfer test: not passed;
- second independent application: absent.

## Claims excluded

- no polynomial-time claim;
- no universal acceleration claim;
- no arbitrary-constraint generalization claim;
- no Goldbach proof;
- no RH/GRH progress.

## Next action

`COF-FOUNDATION-003 — Mandatory Closures, Compatibility Hypergraphs, and Minimal Obstructions`.

The next unit must distinguish:

- exact target reachability bounds;
- mandatory object sets;
- precedence closure of mandatory sets;
- pairwise compatibility as a relaxation;
- higher-order compatibility as an exact finite union-budget model;
- minimal forbidden hyperedges as an exact antichain compression.