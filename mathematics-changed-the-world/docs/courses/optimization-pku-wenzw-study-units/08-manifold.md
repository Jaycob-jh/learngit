# Unit 08｜流形约束优化

> **状态：内容草稿，未核验。** 来源入口为课程总览登记的教材第二版第 7.4 节，以及 [ARNT](https://github.com/optsuite/ARNT)、[OptM](https://github.com/optsuite/OptM) 两个代码仓库。现有 optbook 讲义索引没有独立的流形优化 PDF；这里没有推测其 URL。教材正文与代码未在本批阅读或运行。

## 1. 从正交约束到切空间

球面 $\mathcal S^{n-1}=\{x\in\mathbb R^n:\|x\|_2=1\}$ 的切空间是 $T_x\mathcal S^{n-1}=\{\xi:x^T\xi=0\}$。在欧氏诱导度量下，欧氏梯度 $\nabla f(x)$ 的切向投影为

$$\operatorname{grad}f(x)=(I-xx^T)\nabla f(x).$$

Stiefel 集合 $\mathrm{St}(n,p)=\{X:X^TX=I_p\}$ 的切向条件为 $X^T\Xi+\Xi^TX=0$。对欧氏诱导度量，可用 $\nabla f(X)-X\operatorname{sym}(X^T\nabla f(X))$ 表示 Riemannian gradient。不同度量会改变梯度表达式，因此引用实现时必须记录其度量约定。

**非例。** 直接作 $x-\alpha\nabla f(x)$ 通常离开球面；把该点归一化是一次回到流形的操作，不能把原始欧氏步长当成流形上的向量。

## 2. Retraction 与一阶算法

在球面上取 $R_x(\xi)=(x+\xi)/\|x+\xi\|$（在分母非零的局部定义域内）。它满足 $R_x(0)=x$，且沿切向量的一阶导数为恒等。Riemannian gradient descent 可写作

$$x_{k+1}=R_{x_k}\bigl(-\alpha_k\operatorname{grad}f(x_k)\bigr).$$

Retraction 是局部几何近似；它不等同于一般情况下的指数映射。若使用 Armijo 条件或非单调搜索，应说明比较的是 retraction 曲线上的函数值。向量传输用于在不同切空间比较方向，不能直接将两个切向量当作处于同一线性空间。

## 3. 可手推的特征向量模型

令 $A=A^T$，考虑 $\min_{\|x\|=1}f(x)=x^TAx$。有 $\nabla f(x)=2Ax$，故

$$\operatorname{grad}f(x)=2\bigl(Ax-(x^TAx)x\bigr).$$

驻点满足 $Ax=(x^TAx)x$，即为特征向量；全局最小值是 $A$ 的最小特征值。**驻点并不都对应全局最小值**，最大特征向量也是驻点。这一模型可把 [Unit 03](03-optimality.md) 的一阶必要条件与流形几何联系起来。

[实验脚本](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/labs/20_optimization_manifold.py)拟从不同初值比较 Riemannian gradient 与最小特征值，并记录切向残差。它尚未运行；若初始化在其他特征向量，梯度为零却不对应全局最小值，这是预设的失败案例，不是已观测结果。

## 4. 来源与待核对项

| 概念或主张 | 登记来源 | 待核对 |
|---|---|---|
| 流形、切空间、retraction、向量传输、一二阶方法 | 教材第二版 7.4 目录 | 逐页核对定义、符号、算法假设与收敛论证 |
| ARNT、OptM 的实现与适用范围 | 上述代码仓库 | 版本、许可证、实际接口与数值结果；不能推断独立讲义存在 |
| 球面 Rayleigh quotient 教学模型 | 本页手推 | 脚本复跑、驻点分类与不同初值边界 |

本页只建立独立学习入口；未完成教材、代码和数值验收。
