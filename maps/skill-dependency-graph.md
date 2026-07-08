# Skill Dependency Graph

```text
analytic-number-theory      <- latex, bibliographic-verification, certificate-ledger
prime-valuation-geometry    <- analytic-number-theory, combinatorial-sieve, computational-number-theory, certificate-ledger
solve-math-rigorously       <- latex, certificate-ledger, bibliographic-verification
polymath-advanced-math      <- solve-math-rigorously, bibliographic-verification, certificate-ledger
numerical-assistant         <- computational-number-theory, certificate-ledger
computational-number-theory <- numerical-assistant, analytic-number-theory, certificate-ledger
combinatorial-sieve         <- analytic-number-theory, prime-valuation-geometry, certificate-ledger
operator-theory             <- solve-math-rigorously, spectral-operator-no-go
spectral-analysis           <- operator-theory, numerical-assistant, spectral-operator-no-go
bibliographic-verification  <- research-release-governance
certificate-ledger          <- claim-classification-matrix
spectral-operator-no-go     <- certificate-ledger, research-release-governance
research-release-governance <- claim-classification-matrix, what-not-to-import, no-go-memory
```

**Honest classification:** Diagnostic (dependency map). No RH/GRH progress.
