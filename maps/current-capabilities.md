# Current Capabilities

Live capability snapshot. Registry files remain the machine truth.

## 1. Governed research cycle

```text
named task
→ readiness and priority audit
→ certified PVG–ANT bridge selection
→ exact frozen statement
→ manual proof and independent checks
→ source/originality classification
→ theorem / known-result / negative closure
```

Canonical references:

- `maps/pvg-ant-language-kernel-v1-release-index.md`
- `governance/closures/ORIGINAL-LEMMA-SELECTION-001-CLOSURE.md`
- `research/original-lemma-selection/001/ONE-LEMMA-TARGET-001.md`
- `governance/readiness/ONE-LEMMA-TARGET-001.md`
- `research/one-theorem/001/P0_P6_CHECKPOINT.md`
- `registries/program-goals.jsonl`

## 2. Closed Language Kernel v1

Eight reusable bridge families remain closed: multiplication/order, divisor boxes/convolution, Euler factors, logarithmic size geometry, Möbius support, residue-character Fourier analysis, sieve information, and analytic transfer.

Maturity:

```text
L1: 1 expository family
L2: 7 structural/analytic families
L3: 0 certified-original transfer families
```

## 3. Closed Original Lemma Selection 001

```text
10 exact candidates
4 killed as known/trivial
1 dependent corollary
3 finalists
1 frozen target
```

The selected observable is

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0),
\]

the number of divisor-box points at coordinate margin at least `r` from every facet.

## 4. Manual theorem-proof capability reached

For fixed `q,r`, reduced `a mod q`, and smooth compactly supported `W`, the repository now contains a complete manual proof candidate for the smoothed sum

\[
\sum_{n\equiv a\pmod q} I_r(n)W(n/x).
\]

The proved candidate factorization is

\[
D_{r,\chi}(s)=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

with `H` holomorphic for `Re(s)>1/(2r+2)`.

The manual expansion has:

- an `x^(1/(2r))` layer for `chi^(2r)=chi_0`;
- an `x^(1/(2r+1)) log x` layer for `chi^(2r+1)=chi_0`;
- a fixed-parameter smoothed error `O(x^(1/(2r+2)+epsilon))`.

## 5. Completed checks

- exact geometric counting and multiplicativity;
- Bell-series derivation;
- local residual order and Euler-product convergence;
- character decomposition;
- Mellin inversion and contour shift;
- simple- and double-pole constants;
- principal-character finite part;
- independent SymPy/mpmath certificate;
- internal adversarial proof review;
- CI phase audit.

## 6. Priority correction

Quadratic/cubic torsion-character selection is known from classical square-full progression work. The possible contribution is narrower:

- the divisor-box margin-interior weight;
- the general `2r`/`2r+1` hierarchy for that weight;
- the explicit smoothed weighted constants;
- the PVG geometric interpretation.

The project does not claim a new torsion mechanism or a new contour method.

## 7. Active operational goal

```text
GOAL-OP-ONE-THEOREM-001 = active
P0–P6 checkpoint = PASS
P7 source-grounded external review = next
P8 final classification = pending
```

## 8. Remaining capabilities needed

- exact older-literature priority audit;
- source-grounded citations for standard analytic prerequisites;
- independent line-by-line mathematical review;
- final originality classification.

R, GPU, and new datasets are not needed. Lean remains deferred until the result is classified and a reusable formal target is justified.

## 9. Scientific ceiling

```text
Complete manual proof candidate.
Originality plausible and narrowed, not certified.
No certified original lemma.
No certified theorem.
No publication claim.
No RH progress.
No GRH progress.
```

**Classification:** Diagnostic capability snapshot.
