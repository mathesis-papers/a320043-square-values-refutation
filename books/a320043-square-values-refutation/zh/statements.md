# 精确陈述、证明与形式化证据

这里列出故事背后的完整结果。书面论证归功于原论文及其引用的文献；唯一引用 Lean 的结果保留其较窄的公开结论。符号沿用正文。

::: {.theorem #counterexample title="论文的显式反例" mathesis="collected:a320043-square-values-refutation:2:s1" status="written-proof" proof="pf-counterexample" doi="10.5281/zenodo.24058057" source="Theorem 1, Section 1, PDF page 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/100"}
原来的排除命题是假的。具体见论文给出的见证：

$$
\begin{gathered}N=708158976,\\M=144767444036350576,\\a(N)=M^2.\end{gathered}
$$
:::

::: {.proof #pf-counterexample}
若 $p$ 是素数、$1\le k<p$，同时整除 $p-k$ 与 $k$ 的数也整除 $p$ 和 $k$，因此只能是一。用前三次幂的求和公式展开，得到 $12a(p-1)=p^2(p^2-1)$。令 $P=708158977$、$y=204427888$，则 $P-1=2^9\cdot3\cdot7^2\cdot97^2$。模幂运算给出 $5^{P-1}\equiv1\pmod P$；对应 $q=2,3,7,97$，$5^{(P-1)/q}$ 的余数分别是 $708158976$、$259204175$、$342172932$、$617955608$，每个余数减一都与 $P$ 互素。对 $P$ 的任意素因子 $s$，这些条件迫使 $5$ 模 $s$ 的阶包含 $P-1$ 的每个素数幂，故该阶就是 $P-1$。阶又整除 $s-1$，所以 $s\ge P$；由 $s\mid P$ 得到 $s=P$，这就证明 $P$ 是素数。最后，$P^2-12y^2=1$ 且 $Py=144767444036350576$，代入行和公式即得 $a(P-1)=(Py)^2$。这是原文定理 1 的论证；现有形式化反证内部也构造了这个具体见证。
:::

::: {.theorem #lean-refutation title="原排除命题的否定" lean="D5/S3/ArithSums/SpeziaA320043SquareValuesRefutation.result" mathesis="collected:a320043-square-values-refutation:2:s1"}
现有形式化证明确认：“每个满足 $n\ge1$、$m\ge0$ 且 $a(n)=m^2$ 的整数对，都必须有 $n\in\{1,6,96\}$”这条排除规则是错误的。证明内部使用了具体平方见证；后面的分类与最小性结论仍作为独立的书面结果呈现。
:::

::: {.proposition #prime-criterion title="论文命题：素数行的平方判据" mathesis="collected:a320043-square-values-refutation:2:s2" status="written-proof" proof="pf-prime-criterion" doi="10.5281/zenodo.24058057" source="Proposition 2, Section 2, PDF page 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/94"}
若 $p\ge5$ 为素数，则

$$
\begin{gathered}
a(p-1)\text{ 是整数的平方}\\
\Updownarrow\\
\exists y\in\mathbb{Z}_{\ge1},\quad p^2-12y^2=1.
\end{gathered}
$$

在这种情况下，非负平方根就是 $py$。论文在 Proposition 2 给出了证明；其形式化请求见 [issue 94](https://github.com/the-omega-institute/trureturing-requests/issues/94)。这是有论文论证并有版本 DOI 的结果，但仍与冻结的 Lean 定理分开。
:::

::: {.proof #pf-prime-criterion}
若有 Pell 方程的解，行和公式立即给出 $a(p-1)=p^2(p^2-1)/12=(py)^2$。反过来，若行和为平方，取非负整数平方根 $m$，则 $12m^2=p^2(p^2-1)$。因为 $p\ge5$ 是素数且不整除 $12$，可知 $p\mid m$。写成 $m=py$ 并约去 $p^2$，便得 $p^2-12y^2=1$。行和为正，因此 $y\ge1$，非负平方根就是 $py$。
:::

::: {.corollary #minimality title="论文推论：素数后继条件下的最小新平方索引" mathesis="collected:a320043-square-values-refutation:2:s3" status="written-proof" proof="pf-minimality" doi="10.5281/zenodo.24058057" source="Corollary 3, Section 2, PDF page 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/95"}
在 $n+1$ 为素数的索引中，排除 $1,6,96$ 后最小的平方索引是 $708158976$。论文 Corollary 3 逐项检查 $x_1$ 到 $x_8$ 的素性或因子；形式化请求见 [issue 95](https://github.com/the-omega-institute/trureturing-requests/issues/95)。
:::

::: {.proof #pf-minimality}
上文的下降确实列尽所有正解：当 $y\ge2$ 时，$x'=7x-24y>0$、$y'=7y-2x\ge0$ 且 $x'<x$。这些不等式分别来自 $49x^2-576y^2=12y^2+49>0$、$49y^2-4x^2=y^2-4\ge0$ 以及 $x<4y$。变换保持范数为一，最终到达 $(1,0)$，逆变换生成每一个解。数列 $x_t$ 严格递增。正文的表格分解了 $x_3$ 到 $x_7$，而 $x_1=7$、$x_2=97$、$x_8=708158977$ 是素数。由平方判据，在这一素数范围内只留下下标 $6$、$96$ 和 $708158976$。另外，$p=2$ 对应下标 $1$，$p=3$ 给出非平方的 $a(2)=6$。因此得到的正是“后继为素数”的最小性。
:::

::: {.corollary #prime-restriction title="论文推论：素数项只能出现在二的幂次位置" mathesis="collected:a320043-square-values-refutation:2:s4" status="written-proof" proof="pf-prime-restriction" doi="10.5281/zenodo.24058057" source="Corollary 4, Section 2, PDF page 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/96"}
令

$$r_j=\frac{(2+\sqrt3)^j+(2-\sqrt3)^j}{2},\qquad r_0=1,r_1=2.
$$

对素数 $p$，$a(p-1)$ 为平方当且仅当 $p$ 是这个序列中的素数项。若 $p>2$，则 $p=x_{2^h}$（某个 $h\ge0$），且 $p\equiv7\pmod{30}$。这是论文 Corollary 4 的书面论证；形式化请求见 [issue 96](https://github.com/the-omega-institute/trureturing-requests/issues/96)。
:::

::: {.proof #pf-prime-restriction}
由 $(2+\sqrt3)^2=7+2\sqrt{12}$ 得 $r_{2t}=x_t$。$r_j$ 的递推使奇数下标项为偶数，除 $r_1=2$ 外都大于二，因而不是素数。结合平方判据与小素数检查，便得等价关系。对正整数 $s$ 和奇数 $d>1$，展开 $(x_s+y_s\sqrt{12})^d$：有理部分的每一项都保留 $x_s$ 的正奇数次幂，因此 $x_s\mid x_{ds}$，且 $1<x_s<x_{ds}$。若 $x_t$ 为素数，$t$ 就不能有大于一的奇因子，故 $t=2^h$。最后，$x_{2t}=2x_t^2-1$ 和 $x_1=7$ 使模三十余七的性质保持不变。
:::

::: {.corollary #candidate-factor title="论文推论：排除 A277434 的下一个候选项" mathesis="collected:a320043-square-values-refutation:2:s5" status="written-proof" proof="pf-candidate-factor" doi="10.5281/zenodo.24058057" source="Corollary 5, Section 2, PDF page 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/97"}
设 $w_e=r_{2^e}$，则 $w_0=2$ 且 $w_{e+1}=2w_e^2-1$。逐次模 $1310719$ 计算得到 $w_{16}\equiv0$，即

$$1310719\mid r_{65536}.
$$

因此候选项 $r_{65536}$ 是合数。论文 Corollary 5 的请求见 [issue 97](https://github.com/the-omega-institute/trureturing-requests/issues/97)。这个有限余数链排除一个候选项，却没有决定 Pell 序列是否还会出现别的素数。
:::

::: {.proof #pf-candidate-factor}
从 $2$ 开始，在模 $1310719$ 下反复做 $v\mapsto2v^2-1$。$e=0,\ldots,16$ 的余数依次为 $2$、$7$、$97$、$18817$、$370717$、$481720$、$1068965$、$72611$、$1291005$、$27224$、$1179881$、$1184207$、$192869$、$491881$、$1285182$、$111332$、$0$。因此 $1310719\mid w_{16}=r_{65536}$。严格递增性又给出 $1<1310719<r_{16}=708158977<r_{65536}$，所以这是真因子。
:::

::: {.corollary #product-identity title="论文推论：三角形的乘积恒等式" mathesis="collected:a320043-square-values-refutation:2:s6" status="written-proof" proof="pf-product-identity" doi="10.5281/zenodo.24058057" source="Corollary 6, Section 3, PDF page 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/98"}
对整数 $n\ge1$、$m\ge1$，有 $X(2m-1,m)=1$。令

$$B(N)=\prod_{k=1}^{N}\frac{k}{\gcd(k,N)}.
$$

则

$$\prod_{k=1}^{n}X(n,k)^{1/3}=B(n+1),\qquad B(p)=(p-1)!\quad(p\text{ 为素数}).$$

论文 Corollary 6 给出证明；形式化请求见 [issue 98](https://github.com/the-omega-institute/trureturing-requests/issues/98)。
:::

::: {.proof #pf-product-identity}
在第 $2m-1$ 行的中央，分子、分母同为 $m^3$，商就是一。对整行乘积，利用 $\gcd(n+1-k,k)=\gcd(n+1,k)$，以及 $n+1-k$ 也遍历 $1,\ldots,n$，得到
$$\prod_{k=1}^{n}X(n,k)=\left(\frac{n!}{\prod_{k=1}^{n}\gcd(n+1,k)}\right)^3=B(n+1)^3.$$
$B(n+1)$ 的最后一个因子为一。所有因子为正，可以取实数立方根。若 $p$ 为素数，小于 $p$ 的各项分母都为一，最后一项也为一，因此 $B(p)=(p-1)!$。
:::

::: {.corollary #all-row-formula title="论文推论：适用于所有行的约数公式" mathesis="collected:a320043-square-values-refutation:2:s7" status="written-proof" proof="pf-all-row-formula" doi="10.5281/zenodo.24058057" source="Corollary 7, Section 3, PDF page 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/99"}
令 $N\ge2$，$\varphi$ 为 Euler 函数，并令

$$E(m)=\prod_{q\mid m,\ q\text{ 为素数}}(1-q),\qquad E(1)=1.
$$

则

$$12a(N-1)=\sum_{m\mid N}\bigl(m^3\varphi(m)-m^2E(m)\bigr).$$

这是论文 Corollary 7 的全行推广；形式化请求见 [issue 99](https://github.com/the-omega-institute/trureturing-requests/issues/99)。
:::

::: {.proof #pf-all-row-formula}
定义 $C(1)=0$；当 $m\ge2$ 时，令
$$C(m)=\sum_{\substack{1\le j<m\\\gcd(j,m)=1}}(m-j)^2j.$$
把原始行按 $d=\gcd(N,k)$ 分组，再令 $m=N/d$、$j=k/d$，便有 $a(N-1)=\sum_{m\mid N}C(m)$。在除以最大公因数的立方之前，同样的分组给出
$$U(m)=\frac{m^2(m^2-1)}{12}=\sum_{d\mid m}d^3C(m/d).$$
用 Möbius 反演，其中 $\mu$ 是 Möbius 函数，得到
$$12C(m)=m^4\sum_{d\mid m}\frac{\mu(d)}d-m^2\sum_{d\mid m}\mu(d)d=m^3\varphi(m)-m^2E(m).$$
两个约数和分别按素因子分解为 $1-1/q$ 与 $1-q$ 的乘积。最后对 $m\mid N$ 求和便得结论；$m=1$ 的贡献为零。
:::
