# Research Readiness Card — ONE-LEMMA-TARGET-001

```text
TASK-ID: ONE-LEMMA-TARGET-001
Title: Smoothed torsion layers of margin-interior divisor boxes in arithmetic progressions
Parent goal: GOAL-OP-ORIGINAL-LEMMA-SELECTION-001
Next program: GOAL-OP-ONE-THEOREM-001
Decision: READY WITH EXPLICIT PRIORITY AND SYMBOLIC GATES
Claim ceiling: candidate theorem package only
```

## 1. Exact target

The frozen statement is:

`research/original-lemma-selection/001/ONE-LEMMA-TARGET-001.md`.

It consists of:

1. the exact twisted Euler factorization for `I_r(n)`;
2. absolute convergence of the residual Euler product for `Re(s)>1/(2r+2)`;
3. a fixed-modulus smoothed residue-class asymptotic;
4. explicit torsion-character selection at the `2r` and `2r+1` layers;
5. an error `O(x^(1/(2r+2)+epsilon))`.

## 2. Knowledge readiness

| Prerequisite | State | Evidence/use |
|---|---|---|
| valuation/divisor-box geometry | operationally ready | Language Kernel v1, divisor-box bridge |
| multiplicative local factors | operationally ready | Euler-coordinate bridge |
| Dirichlet characters and orthogonality | operationally ready | residue-character bridge |
| Dirichlet L-functions, principal character | operationally ready | Tenenbaum/Overholt/Davenport layers |
| Mellin inversion and smooth contour shifting | operationally ready | ANT transform layers |
| polynomial vertical growth for fixed-q L-functions | known but must be cited precisely | targeted source activation in proof phase |
| powerful/k-full number literature | partially activated | preliminary audit complete; older exact-priority audit remains |
| double-pole Laurent calculation | derived, needs independent symbolic check | frozen target constants |

## 3. Missing knowledge to acquire inside the program

### Priority gate

Search older journal literature and databases for:

- weighted powerful or k-full numbers with local weight `a-2r+1`;
- divisor-lattice interior or margin-point enumerators;
- fixed-modulus square-full asymptotics with character-power selection;
- exact Dirichlet series matching the frozen local factor.

The theorem may be reclassified as a new geometric corollary of a known general result. That outcome is acceptable.

### Symbolic gate

Independently verify:

- cancellation of local terms through degree `2r+1`;
- residue coefficient at `s=1/(2r)`;
- both coefficients at the double pole `s=1/(2r+1)`;
- the finite part
  `kappa_q=(phi(q)/q)(gamma+sum_{p|q}log(p)/(p-1))`;
- bad-prime conventions for imprimitive characters.

### Analytic gate

Write the exact contour lemma used to bound the shifted line, including:

- rapid decay of `W-hat`;
- fixed-q polynomial growth of each L-factor;
- local uniform bounds for `H_{r,chi}`;
- dependence of the implied constant on `q,r,W,epsilon`.

## 4. PVG necessity

```text
PASS AT MODEST-THEOREM LEVEL
```

Reason:

- the arithmetic function is the count of margin-interior points of a divisor box;
- the exponent layers arise from the geometry rather than from an arbitrary fitted Euler product;
- the residue theorem couples this geometry to character torsion through a certified bridge.

Limit:

- the contour proof is classical after translation;
- the project must not claim a new analytic method.

## 5. Tool activation

| Tool | Decision |
|---|---|
| targeted literature search | REQUIRED first |
| books/ledgers | activate only exact L-function/Mellin prerequisites |
| Python/SymPy | REQUIRED for independent Laurent and local-series checks |
| numerical experiment | optional sanity check only |
| R | NOT REQUIRED |
| Lean | DEFERRED; use only after a manual proof and only for reusable algebraic structure |
| GPU | NOT REQUIRED |

## 6. Proof phases

```text
P0 priority and terminology audit
P1 exact local factorization
P2 convergence of H_{r,chi}
P3 character decomposition
P4 Mellin inversion and contour shift
P5 residue constants
P6 independent symbolic/numerical verification
P7 adversarial proof review
P8 originality classification and closure
```

## 7. Success outcomes

1. **Original theorem candidate survives:** proof complete and no exact prior result found.
2. **Known-method/new-observable theorem:** proof complete but classified as a geometric specialization/corollary.
3. **Known result:** close with exact attribution and integrate the bridge.
4. **Proof failure:** close with a named missing certificate or corrected weaker theorem.
5. **Statement failure:** repair or reject after symbolic/counterexample audit.

## 8. Stop rule

The One-Theorem Program closes only with:

- a complete proof and priority classification;
- an exact known-result attribution;
- a negative certificate;
- or a precisely named missing analytic certificate.

No second target may become active before this closure.

## 9. Readiness decision

```text
READY
```

The mathematical substrate is sufficient to begin. Priority and symbolic work are explicit first phases of the program, not hidden missing knowledge.

## 10. Ceiling

```text
No original lemma certified.
No theorem proved.
No publication claim.
No RH/GRH progress.
```
