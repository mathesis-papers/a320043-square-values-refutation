# OEIS A320043, COMMENTS, revision 43: a square-value refutation extending Zhu's Pell-prime result (2011)

**Authors:** Haobo Ma, Wenlin Zhang

Extending Zhu's Pell-prime result (2011), we refute the conjecture in OEIS A320043, COMMENTS, revision 43 (September 8, 2022; posed December 16, 2018), by a(708158976)=144767444036350576^2. For every prime p, its preceding row has sum p^2(p^2-1)/12; for p>=5, this sum is a square exactly when p^2-12y^2=1 for an integer y. An elementary descent recovers the known Pell sequence and proves that this is the smallest additional square index whose successor is prime. We also reprove the known power-of-two index restriction, give a factor excluding the proposed next candidate in A277434, and prove the triangle's product identity and an all-row divisor formula.

- PDF: [frozen public file](paper.pdf)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [a320043-square-values-refutation](https://mathesis-omega-research.apps.chrono-ai.fun/papers/a320043-square-values-refutation?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). OEIS A320043, COMMENTS, revision 43: a square-value refutation extending Zhu's Pell-prime result (2011). Mathesis, version 2. https://mathesis-omega-research.apps.chrono-ai.fun/papers/a320043-square-values-refutation?version=2

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean) | No public receipt |
| Proposition (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean) | No public receipt |
| Corollary (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean) | No public receipt |
| Corollary (s6) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean) | No public receipt |
| Corollary (s7) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
