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

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/a320043-square-values-refutation/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/a320043-square-values-refutation/a320043-square-values-refutation/zh/) · [Read in English](https://papers.trureturing.org/a320043-square-values-refutation/a320043-square-values-refutation/en/)

[Slides](https://papers.trureturing.org/a320043-square-values-refutation/a320043-square-values-refutation/slides/) ([sources](books/a320043-square-values-refutation/slides/)) · [Videos](https://papers.trureturing.org/a320043-square-values-refutation/a320043-square-values-refutation/films/) ([sources](books/a320043-square-values-refutation/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/a320043-square-values-refutation/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `counterexample` | variant | `D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.result` |
| `lean-refutation` | same | `D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.result` |
| `prime-criterion` | none | — |
| `minimality` | none | — |
| `prime-restriction` | none | — |
| `candidate-factor` | none | — |
| `product-identity` | none | — |
| `all-row-formula` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/a320043-square-values-refutation/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
