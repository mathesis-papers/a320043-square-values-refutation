# Statement comparison at the pinned public commit

| Result | Verdict | Compared declaration | Commit | Scope |
|---|---|---|---|---|
| counterexample | variant | D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.result | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | The manuscript node s1 states the explicit equality at 708158976; the frozen theorem states the weaker negation of the universal exclusion claim. The witness is used in its proof, but the conclusions are not syntactically identical. |
| lean-refutation | same | D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.result | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | This book environment states the exact frozen conclusion: the Lean definition `claim` is false. |
| prime-criterion | none | — | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | The paper's iff criterion for prime rows and the Pell equation is absent from the frozen public declarations. |
| minimality | none | — | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | The first-new-index claim needs descent completeness, monotonicity, and the finite prime/factor table; none is stated by the frozen theorem. |
| prime-restriction | none | — | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | The Pell prime-index restriction and residue class are not stated by the frozen public declarations. |
| candidate-factor | none | — | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | The modular recurrence certificate for the factor 1310719 is not a frozen declaration. |
| product-identity | none | — | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | The triangle product identity and prime specialization are not stated by the frozen public declarations. |
| all-row-formula | none | — | 73ec20a01fc35e0f53bc258c605821728f3c33b6 | The Euler/Möbius all-row divisor formula is not stated by the frozen public declarations. |

The exact public conclusion is the negation of the original exclusion, with its positive-index domain. The explicit witness is checked inside that proof but has no matching public frozen declaration. Its separate request asks to expose that existing witness, with no new refutation or credit implied. The six other complete manuscript statements retain their own written proofs and canonical requests. The existing version DOI was independently matched against both frozen artifact hashes; publisher metadata is unchanged.
