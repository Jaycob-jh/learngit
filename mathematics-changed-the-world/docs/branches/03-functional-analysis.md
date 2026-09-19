# 泛函分析：把线性代数搬到无限维

> **核心问题**：函数本身能不能像向量一样做几何？微分方程、Fourier series 和量子态能不能放在同一个“空间”里？

## 为什么有限维线性代数不够？

在普通线性代数中：

\[
x=(x_1,\dots,x_n).
\]

但很多数学对象本身是函数，例如：

- 温度场 \(u(x)\)；
- 波函数 \(\psi(x)\)；
- 信号 \(f(t)\)；
- PDE 的解。

Fourier 告诉我们函数可以像向量那样分解成“基函数”。这推动一个巨大抽象：

> 把函数当成无限维向量。

## Hilbert space

Hilbert space 具有 inner product：

\[
\langle f,g\rangle.
\]

例如

\[
L^2([a,b])
\]

中的典型内积：

\[
\langle f,g\rangle
=
\int_a^b f(x)\overline{g(x)}\,dx.
\]

于是：

- orthogonality；
- projection；
- basis；
- length；

全部可以从有限维向量空间推广到函数空间。

Fourier series 就可以理解为向正交基做投影。

## Banach space

Banach space 只要求 norm 与 completeness：

\[
\|x\|.
\]

不一定有 inner product。

Stefan Banach 在 20 世纪早期把这套框架系统化。1932 年的著作成为 functional analysis 发展的里程碑。

## Operator：无限维的“矩阵”

线性算子

\[
T:X\to Y
\]

对应有限维中的矩阵。

例如微分：

\[
D f=f'
\]

就是一个 operator。

量子力学中的 observable、PDE 中的 differential operator、积分方程中的 integral operator 都属于这一语言。

## 四个基础定理群

泛函分析的骨架包括：

- Hahn–Banach theorem；
- Uniform Boundedness Principle；
- Open Mapping Theorem；
- Closed Graph Theorem。

再加上 spectral theory，它们共同回答：

> 无限维空间里的线性方程什么时候有解、解是否稳定、operator 有什么“特征值结构”？

## 量子力学为什么离不开 Hilbert space？

量子态通常表示为 Hilbert space 中的向量；observables 表示为 self-adjoint operators。

有限维量子计算中就是熟悉的复向量与矩阵，而连续变量系统自然走向无限维。

## PDE

PDE 的 classical solution 往往要求过强的光滑性。

functional analysis 允许在 Sobolev space 中寻找 weak solution：

\[
u\in H^1,\ H^2,\dots
\]

这样“解”可以不拥有每一点上的传统导数，却仍满足积分形式的方程。

## 与机器学习的关系

- kernel methods → reproducing kernel Hilbert spaces；
- Gaussian processes 与 kernel operator；
- neural tangent kernel；
- inverse problems；
- regularization 与 operator theory。

## 一条关键发展链

\[
\text{Fourier}
\to
L^2
\to
\text{Hilbert space}
\to
\text{operators}
\to
\text{spectral theory}.
\]

另一条：

\[
\text{Lebesgue}
\to
L^p
\to
\text{Banach spaces}.
\]

## 参考

- MacTutor, Stefan Banach: https://mathshistory.st-andrews.ac.uk/Biographies/Banach/
- Kreyszig, *Introductory Functional Analysis with Applications*.
- Conway, *A Course in Functional Analysis*.