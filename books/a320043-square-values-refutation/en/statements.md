# Exact statements, proofs and formal evidence

These are the precise results behind the story. Written proofs are attributed to the paper and its cited literature; the single Lean result has its narrower public conclusion. Symbols follow the story.

::: {.theorem #counterexample title="The paper's explicit counterexample" mathesis="collected:a320043-square-values-refutation:2:s1" status="written-proof" proof="pf-counterexample" doi="10.5281/zenodo.24058057" source="Theorem 1, Section 1, PDF page 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/100"}
The original exclusion claim is false. The concrete witness supplied by the paper is

$$
\begin{gathered}N=708158976,\\M=144767444036350576,\\a(N)=M^2.\end{gathered}
$$
:::

::: {.proof #pf-counterexample}
For a prime $p$, every common divisor of $p-k$ and $k$, with $1\le k<p$, divides both $p$ and $k$, so it equals one. Expanding the sum using the first three power-sum formulas gives $12a(p-1)=p^2(p^2-1)$. Put $P=708158977$ and $y=204427888$. The complete factorization is $P-1=2^9\cdot3\cdot7^2\cdot97^2$. Modular exponentiation gives $5^{P-1}\equiv1\pmod P$; for $q=2,3,7,97$, respectively, the residues $5^{(P-1)/q}$ are $708158976$, $259204175$, $342172932$, and $617955608$. Each residue minus one is coprime to $P$. For any prime divisor $s$ of $P$, these conditions force the order of $5$ modulo $s$ to contain every prime power in $P-1$, hence to equal $P-1$. As that order divides $s-1$, $s\ge P$ and therefore $s=P$. Thus $P$ is prime. Finally $P^2-12y^2=1$ and $Py=144767444036350576$, so the row identity gives $a(P-1)=(Py)^2$. This is the argument of manuscript Theorem 1; the witness is also constructed inside the existing formal refutation.
:::

::: {.theorem #lean-refutation title="Negation of the original exclusion claim" lean="D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.result" mathesis="collected:a320043-square-values-refutation:2:s1"}
It is false that every integer $n\ge1$ and $m\ge0$ satisfying $a(n)=m^2$ must have $n\in\{1,6,96\}$. This is the universal exclusion that the existing formal proof refutes.
:::

::: {.proposition #prime-criterion title="The paper's prime-row square criterion" mathesis="collected:a320043-square-values-refutation:2:s2" status="written-proof" proof="pf-prime-criterion" doi="10.5281/zenodo.24058057" source="Proposition 2, Section 2, PDF page 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/94"}
For a prime $p\ge5$,

$$
\begin{gathered}
a(p-1)\text{ is an integer square}\\
\Updownarrow\\
\exists y\in\mathbb{Z}_{\ge1},\quad p^2-12y^2=1.
\end{gathered}
$$

When this holds, the nonnegative square root of $a(p-1)$ is $py$. The paper proves this as Proposition 2; its formalization request is [issue 94](https://github.com/the-omega-institute/trureturing-requests/issues/94). The result has a written proof and is linked to the version DOI; it remains separate from the frozen Lean theorem.
:::

::: {.proof #pf-prime-criterion}
A Pell solution gives $a(p-1)=p^2(p^2-1)/12=(py)^2$. Conversely choose the nonnegative integer root $m$ when the row is a square. Then $12m^2=p^2(p^2-1)$. Since $p\ge5$ is prime, $p\nmid12$ and $p\mid m$. Write $m=py$ and cancel $p^2$ to obtain $p^2-12y^2=1$. The row is positive, so $y\ge1$, and its nonnegative root is $py$.
:::

::: {.corollary #minimality title="The first new square index with a prime successor" mathesis="collected:a320043-square-values-refutation:2:s3" status="written-proof" proof="pf-minimality" doi="10.5281/zenodo.24058057" source="Corollary 3, Section 2, PDF page 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/95"}
Among indices $n$ for which $n+1$ is prime, the smallest square index outside $\{1,6,96\}$ is $708158976$. Corollary 3 checks the primality or a proper factor of $x_1$ through $x_8$; the formalization request is [issue 95](https://github.com/the-omega-institute/trureturing-requests/issues/95).
:::

::: {.proof #pf-minimality}
The Pell descent above lists all positive solutions: for $y\ge2$, $x'=7x-24y>0$, $y'=7y-2x\ge0$ and $x'<x$. These inequalities follow from $49x^2-576y^2=12y^2+49>0$, $49y^2-4x^2=y^2-4\ge0$ and $x<4y$. The norm remains one, so descent ends at $(1,0)$; the inverse generates every solution. The $x_t$ increase strictly. The factor table in the story factors $x_3$ through $x_7$, while $x_1=7$, $x_2=97$ and $x_8=708158977$ are prime. The square criterion therefore leaves exactly indices $6$, $96$ and $708158976$ in this prime range. Separately $p=2$ gives index $1$ and $p=3$ gives the nonsquare $a(2)=6$. This proves precisely the prime-successor minimality asserted.
:::

::: {.corollary #prime-restriction title="Prime terms occur only at power-of-two indices" mathesis="collected:a320043-square-values-refutation:2:s4" status="written-proof" proof="pf-prime-restriction" doi="10.5281/zenodo.24058057" source="Corollary 4, Section 2, PDF page 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/96"}
Define

$$r_j=\frac{(2+\sqrt3)^j+(2-\sqrt3)^j}{2},\qquad r_0=1,r_1=2.$$

For a prime $p$, $a(p-1)$ is a square exactly when $p$ is a prime term of this sequence. If $p>2$, then $p=x_{2^h}$ for some $h\ge0$, and $p\equiv7\pmod{30}$. This is the paper's Corollary 4; its formalization request is [issue 96](https://github.com/the-omega-institute/trureturing-requests/issues/96).
:::

::: {.proof #pf-prime-restriction}
The identity $(2+\sqrt3)^2=7+2\sqrt{12}$ gives $r_{2t}=x_t$. The recurrence for $r_j$ makes odd-indexed terms even; after $r_1=2$ they exceed two, hence are composite. Together with the criterion and the small primes, this proves the equivalence. For positive $s$ and odd $d>1$, expanding $(x_s+y_s\sqrt{12})^d$ shows that its rational part is divisible by $x_s$: each even-degree term retains a positive odd power of $x_s$. Thus $x_s\mid x_{ds}$ and $1<x_s<x_{ds}$. A prime $x_t$ can have no odd divisor of $t$ other than one, so $t=2^h$. Finally $x_{2t}=2x_t^2-1$ and $x_1=7$ preserve residue seven modulo thirty.
:::

::: {.corollary #candidate-factor title="A factor excluding the proposed next Pell prime" mathesis="collected:a320043-square-values-refutation:2:s5" status="written-proof" proof="pf-candidate-factor" doi="10.5281/zenodo.24058057" source="Corollary 5, Section 2, PDF page 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/97"}
Let $w_e=r_{2^e}$. Then $w_0=2$ and $w_{e+1}=2w_e^2-1$. Successive reductions modulo $1310719$ give $w_{16}\equiv0$, so

$$1310719\mid r_{65536}.$$

The proposed value $r_{65536}$ is therefore composite. The formalization request for Corollary 5 is [issue 97](https://github.com/the-omega-institute/trureturing-requests/issues/97). This finite residue chain rules out one candidate; it does not decide whether the Pell sequence has any further prime terms.
:::

::: {.proof #pf-candidate-factor}
Repeatedly apply $v\mapsto2v^2-1$ modulo $1310719$, starting at $v=2$. For $e=0,\ldots,16$ the residues are $2$, $7$, $97$, $18817$, $370717$, $481720$, $1068965$, $72611$, $1291005$, $27224$, $1179881$, $1184207$, $192869$, $491881$, $1285182$, $111332$, and $0$. Therefore $1310719\mid w_{16}=r_{65536}$. Strict increase gives $1<1310719<r_{16}=708158977<r_{65536}$, making this a proper factor.
:::

::: {.corollary #product-identity title="The triangle product identity" mathesis="collected:a320043-square-values-refutation:2:s6" status="written-proof" proof="pf-product-identity" doi="10.5281/zenodo.24058057" source="Corollary 6, Section 3, PDF page 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/98"}
For integers $n\ge1$ and $m\ge1$, $X(2m-1,m)=1$. Set

$$B(N)=\prod_{k=1}^{N}\frac{k}{\gcd(k,N)}.$$

Then

$$\prod_{k=1}^{n}X(n,k)^{1/3}=B(n+1),\qquad B(p)=(p-1)!\quad(p\text{ prime}).$$

Corollary 6 proves this identity; its formalization request is [issue 98](https://github.com/the-omega-institute/trureturing-requests/issues/98).
:::

::: {.proof #pf-product-identity}
At the centre of row $2m-1$, numerator and denominator are both $m^3$, giving one. In the full product, $\gcd(n+1-k,k)=\gcd(n+1,k)$ and the factors $n+1-k$ run through $1,\ldots,n$. Therefore
$$\prod_{k=1}^{n}X(n,k)=\left(\frac{n!}{\prod_{k=1}^{n}\gcd(n+1,k)}\right)^3=B(n+1)^3.$$
The final factor of $B(n+1)$ is one. All factors are positive, so taking real cube roots is valid. For prime $p$, all denominators below $p$ equal one and the last factor equals one, giving $B(p)=(p-1)!$.
:::

::: {.corollary #all-row-formula title="An all-row divisor formula" mathesis="collected:a320043-square-values-refutation:2:s7" status="written-proof" proof="pf-all-row-formula" doi="10.5281/zenodo.24058057" source="Corollary 7, Section 3, PDF page 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/99"}
Let $N\ge2$, let $\varphi$ be Euler's totient function, and define

$$E(m)=\prod_{q\mid m,\ q\text{ prime}}(1-q),\qquad E(1)=1.$$

Then

$$12a(N-1)=\sum_{m\mid N}\bigl(m^3\varphi(m)-m^2E(m)\bigr).$$

This is the all-row extension in Corollary 7; its formalization request is [issue 99](https://github.com/the-omega-institute/trureturing-requests/issues/99).
:::

::: {.proof #pf-all-row-formula}
Define $C(1)=0$ and, for $m\ge2$,
$$C(m)=\sum_{\substack{1\le j<m\\\gcd(j,m)=1}}(m-j)^2j.$$
Grouping the original row by $d=\gcd(N,k)$, then setting $m=N/d$, $j=k/d$, gives $a(N-1)=\sum_{m\mid N}C(m)$. Before division by the gcd cube, the same grouping gives
$$U(m)=\frac{m^2(m^2-1)}{12}=\sum_{d\mid m}d^3C(m/d).$$
Möbius inversion, with $\mu$ the Möbius function, yields
$$12C(m)=m^4\sum_{d\mid m}\frac{\mu(d)}d-m^2\sum_{d\mid m}\mu(d)d=m^3\varphi(m)-m^2E(m).$$
The two sums factor over the prime divisors as products of $1-1/q$ and $1-q$. Summing over $m\mid N$ proves the formula; at $m=1$ its contribution is zero.
:::
