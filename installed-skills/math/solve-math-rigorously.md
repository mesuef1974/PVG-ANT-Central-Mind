# Skill Interface Card

**Skill ID:** SKILL-MATH-RIGOR-001
**Name:** solve-math-rigorously
**Layer:** rigor
**Purpose inside Central Mind:** read, map, solve, and check nontrivial math tasks; separate proof from heuristic.

**Inputs:** a problem, derivation, or claimed solution.
**Outputs:** a checked solution or an explicit gap statement.

**Allowed use:** solving, verifying, and refuting; marking where a step is heuristic not proven.
**Forbidden use:** presenting a heuristic or numerical check as a proof or certificate.

**PVG connection:** enforces that PVG derivations are actually derived, not asserted.
**ANT connection:** the checker for ANT computations.
**Certificate role:** distinguishes proof from guess; a solver-side gate before promotion.

**Main walls:** none specific (cross-cutting).
**Related diagnostic cards:** proof/certificate discipline (v0.2, planned).
**Related registry IDs:** RULE-PVG-001.

**Status:** installed.
**Honest classification:** Diagnostic (skill interface). No RH/GRH progress.
