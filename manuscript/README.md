# OEIS A320043, COMMENTS, revision 43: refutation extending Zhu (2011)

Haobo Ma (ChronoAI Pte Ltd, Singapore) and Wenlin Zhang (National University
of Singapore; ChronoAI Pte Ltd, Singapore). November 5, 2026.

## Result

For the row sum defined in the first FORMULA of
[OEIS A320043, revision 43](https://oeis.org/A320043/internal),

```text
a(708158976) = 144767444036350576^2
            = 20957612852817895952216852375531776.
```

This refutes the COMMENTS exclusion of all square indices except 1, 6, 96.
The row-value wording was introduced in revision 31 on December 16, 2018,
and remains in revision 43 of September 8, 2022.
[Zhu (2011), Section 4, p. 200](https://doi.org/10.4064/aa146-2-6),
proved the Pell-prime index restriction and the ordering of the first three
odd Pell primes. The prime was recorded in
[A177879 (2010)](https://oeis.org/A177879/internal), then in
[Tiffin's A277434 (2016)](https://oeis.org/A277434/internal);
later arguments and computations are credited in the note.

The note connects this known prime to the row sum, gives a complete
prime-row square criterion, and proves restricted minimality by Pell descent.
The prime-successor square indices are exactly one less than the prime
terms of A001075, including the exceptional prime 2. It also proves the
triangle's diagonal and product formulas and an all-row divisor formula.
The specific candidate A001075(65536) is composite, with proper factor
1310719, as in Andrews's 2019 answer. Existence of further Pell primes and
unrestricted minimality are not consequences of these results.

## Build the PDF

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard LaTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is contained in `note.tex`; no BibTeX step or external
bibliography file is needed. All mathematical content is in the main source.

## Check the arithmetic

Python 3.9 or later, with its standard library, is sufficient:

```sh
python3 verify.py > verification-current.txt
diff -u verification.txt verification-current.txt
```

The expected JSON has `status` equal to `PASS`. Checks include all 42
displayed terms of A320043, exact rational and integer sums for indices
1 through 256, all 55 prime rows through prime 257, the polynomial
telescope, the modular certificate and independent trial division for
708158977, and the first nine Pell pairs. Additional checks cover the all-row
divisor formula and triangle/totative product formulas for successors 2 through
257, the diagonal and adjacent-gcd identities through 256, the even-index Pell
identity through 64, odd-multiple divisibility for base indices 1 through 16
and odd multipliers 3 through 15, and the complete 17-residue certificate for
the excluded candidate. The large row is evaluated by the proved prime-row
identity; finite checks do not replace the universal written proofs.

## Statement coverage

The pinned
[Lean file](https://github.com/the-omega-institute/trureturing/blob/73ec20a01fc35e0f53bc258c605821728f3c33b6/D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.lean)
defines the literal sum and exclusion as `a` and `claim`; `result` states
the negation of `claim`. Its helper declarations `prime_row`, `prime_pell`
and `witness_prime` express the prime-row identity, the sufficient Pell
implication and the witness's primality. The prime-row converse, Pell
descent, restricted minimality, prime-index restriction, triangle identities
and divisor formula are written proofs. The candidate's compositeness follows
from the displayed finite modular certificate and the proved doubling identity.
These extensions are distinct from the scope of the Lean declarations.
The program checks the listed finite arithmetic facts.

## Contents and license

`note.tex`, `verify.py`, `verification.txt`, `metadata.json`, and this
README are the complete source package. `note.pdf` is supplied separately.
All original text and code in this package are licensed CC BY 4.0
(`cc-by-4.0`). Scientific sources retain their stated attribution.
