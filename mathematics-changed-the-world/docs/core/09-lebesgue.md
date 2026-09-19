# 09｜Lebesgue 单调收敛定理：什么时候“先取极限再积分”等于“先积分再取极限”

> **一句话**：现代分析的难点常常不是把某个积分算出来，而是证明无穷极限、求和、积分这些操作能否安全交换。

## 1. Fourier 把旧积分理论逼到了边界

19 世纪的分析越来越多地遇到：

- 不连续函数；
- 函数列；
- Fourier series；
- pointwise limit；
- 无穷求和和积分交换。

Riemann 积分非常成功，但对于“坏函数”和极限问题不够灵活。

Lebesgue 的革命性想法可以粗略描述为：

> 与其按 $x$-轴把定义域切成小区间，不如研究函数取值落在哪些集合上，并给这些集合赋予“大小”。

于是 measure theory 与 Lebesgue integration 结合起来。

## 2. 从简单函数开始

若

$$
\phi
=
\sum_{k=1}^{m}a_k\mathbf 1_{E_k},
\qquad a_k\ge0,
$$

定义

$$
\int\phi\,d\mu
=
\sum_{k=1}^{m}a_k\mu(E_k).
$$

对一般非负可测函数 $f$，用越来越好的简单函数从下方逼近，定义其积分为这些简单积分的 supremum。

因此 Lebesgue 积分天生适合“单调逼近”。

## 3. 单调收敛定理

若

$$
0\le f_1\le f_2\le\cdots
$$

且

$$
f_n(x)\to f(x),
$$

则

$$
\int f\,d\mu
=
\lim_{n\to\infty}
\int f_n\,d\mu.
$$

常写作

$$
f_n\uparrow f.
$$

## 4. 为什么它如此重要？

“函数逐点收敛”一般**不足以**推出积分也收敛。

MCT 提供一种非常干净的充分条件：

- 非负；
- 单调增加。

在这两个条件下，极限可以安全地穿过积分号。

## 5. 与另外两个核心收敛定理

### Fatou lemma

对非负 $f_n$：

$$
\int\liminf f_n\,d\mu
\le
\liminf\int f_n\,d\mu.
$$

### Dominated Convergence Theorem

若

$$
f_n\to f
$$

几乎处处，且存在可积 $g$ 使

$$
|f_n|\le g,
$$

则

$$
\int f_n\to\int f.
$$

现代分析中这三者是一组极重要工具。

## 6. 为什么概率论本质上是测度论？

现代概率空间写成

$$
(\Omega,\mathcal F,P),
$$

其中 $P$ 是一个 measure。

随机变量

$$
X:\Omega\to\mathbb R
$$

是可测函数，而期望

$$
E[X]
=
\int_\Omega X\,dP
$$

就是 Lebesgue integral。

因此概率论中的：

- 期望；
- 条件期望；
- 几乎处处收敛；
- $L^p$ 收敛；
- martingale；

都直接生活在测度论语言中。

## 7. 与 Fourier 的深层关系

Fourier 问题迫使数学家研究：

- 什么叫函数相等？
- 什么叫积分存在？
- 什么叫级数收敛？
- 可否逐项积分？
- 函数空间应该怎样定义距离？

最终形成 $L^1,L^2,L^p$ 空间。尤其 $L^2$ 是 Hilbert space，Fourier analysis 因而可以理解为无限维正交投影。

这直接通向 functional analysis。

## 8. 现实应用

Lebesgue theory 很少以“某设备直接调用 MCT”的方式出现，它更像基础设施：

- stochastic processes；
- Bayesian integration；
- signal theory；
- PDE weak solutions；
- Sobolev spaces；
- quantum mechanics Hilbert spaces；
- statistical learning theory。

就像操作系统内核：普通用户可能看不见，但高层工具依赖它。

## 9. 常见误解

**Lebesgue 积分不是单纯“能积更多奇怪函数”。**  
更大的优势是极限操作更稳定。

**measure 不等于 length。**  
概率就是一种 measure；Dirac measure 等对象甚至不对应普通几何长度。

## 10. 动手实验

\`\`\`bash
python labs/09_monotone_convergence.py
\`\`\`

构造一列从下方逼近目标函数的阶梯函数，观察积分随 $n$ 单调趋近目标积分。

## 11. 向外延伸

Lebesgue → $L^p$ spaces → Hilbert/Banach spaces → functional analysis → PDE / probability / quantum theory / wavelets。

## 参考

- MacTutor, Henri Lebesgue: https://mathshistory.st-andrews.ac.uk/Biographies/Lebesgue/
- Royden & Fitzpatrick, *Real Analysis*.
- Folland, *Real Analysis*.