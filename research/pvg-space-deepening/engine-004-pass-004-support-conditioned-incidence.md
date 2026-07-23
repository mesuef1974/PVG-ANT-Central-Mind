# ENGINE-004 PASS-004 — Support-Conditioned Incidence Diagnostics

```text
Goal: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Status: IMPLEMENTED / LOCAL AND CI CERTIFICATION PENDING
Frozen box: unchanged
Phase D: NOT AUTHORIZED
```

## Question

After deterministic conditioning on integer size and parity route, does support size or exact support face retain any finite diagnostic separation in prime-fiber multiplicity and centered-radius incidence profiles inside the registered 884-point box?

The pass does not estimate a causal effect. It performs exact finite stratification and counterexample search only.

## Fixed strata

```text
decimal bins = 1-9, 10-99, 100-999, 1000-9999, 10000-99999, 100000
bit-length = floor(log2 N)+1
route = even / odd
support class = support size or exact support face
```

## Exact outputs

For every registered group the implementation records:

- point, represented, and nonrepresented counts;
- represented-rate ratio as exact integers;
- multiplicity sum;
- multiplicity mean as a reduced rational;
- multiplicity median;
- represented-point multiplicity mean;
- maximum multiplicity;
- conditioned rankings by support size;
- rank reversals relative to the raw support-size ranking;
- deterministic nearest-neighborhood witnesses;
- explicit counterexamples to support determinacy;
- SHA-256 of the complete canonical point-record table.

## Matched-neighborhood rule

For each point, comparison candidates must have:

```text
same parity route
same decimal bin
different support size
minimum absolute integer distance
all ties retained
```

The resulting witnesses are descriptive finite comparisons. They are not matched causal estimates.

## Required counterexamples

The implementation searches for witnesses showing:

```text
same exact support does not determine multiplicity
same support size does not determine multiplicity
same route and size bin do not determine exact support
```

A missing witness is a test failure and must be investigated rather than silently interpreted.

## Separation from previous passes

PASS-004 reuses the certified objects from PASS-002 and PASS-003 but does not redefine them:

```text
D(N) = governed centered-radius spectrum
O(d) = integer-owner set
static component id = PASS-003 incidence component
```

Every point spectrum is checked against the PASS-002/PASS-003 production index.

## Classification ceiling

```text
stratification definitions = IDENTITY
exact grouped arithmetic = FINITE-VERIFIED after execution
counterexample witnesses = FINITE-VERIFIED after execution
conditioned rank changes = DIAGNOSTIC after execution
support causes fiber richness = NOT ESTABLISHED
any general support law = OPEN
```

No regression, significance test, density estimate, asymptotic law, Phase-D dynamics, Goldbach/PNT/RH/GRH progress, originality, theorem, or publication-readiness claim is made.

## Required gate

```powershell
python -m py_compile tools/pvg_support_conditioned_incidence.py tests/test_pvg_support_conditioned_incidence.py
python -m unittest -v tests/test_pvg_support_conditioned_incidence.py
python tools/pvg_support_conditioned_incidence.py `
  --output research/pvg-space-deepening/data/support-conditioned-incidence-summary.json `
  > $null
python -m json.tool research/pvg-space-deepening/data/support-conditioned-incidence-summary.json > $null
```

PASS-004 remains open until the generated certificate is committed, regenerated independently, and the checkpoint is created.
