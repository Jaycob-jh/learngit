# 群论与对称性：把“允许哪些变换”变成数学对象

> **核心问题**：一个系统在什么变换下保持不变？这些变换如何组合？

## 从解方程到 permutation

多项式方程长期追问：

> 五次方程为什么没有像二、三、四次方程那样的通用根式公式？

Lagrange 等人发现 roots 的 permutations 与公式结构密切相关。

Galois 的突破是把“根之间允许的置换”组织成 group，并证明：

> equation 是否 solvable by radicals 与其 Galois group 的结构有关。

这使“解方程”变成“研究 symmetry structure”。

## Group 定义

集合 $G$ 配 operation $*$，满足：

1. closure；
2. associativity；
3. identity；
4. inverse。

例子：

- integers under addition；
- rotations of a square；
- permutation group；
- invertible matrices；
- continuous Lie groups。

## 对称性为什么是 group？

正方形的旋转/反射可以连续做两次，结果仍是一个 symmetry。

这些变换：

- 能组合；
- 有 identity；
- 每个有 inverse。

因此自然构成 dihedral group。

## Representation

抽象 group 可以通过 matrices 作用在 vector space：

$$
\rho:G\to GL(V).
$$

representation theory 让抽象 symmetry 进入 linear algebra。

## Lie group

rotation group：

$$
SO(3)
$$

既是 group，又是 smooth manifold。

它连接：

- group theory；
- differential geometry；
- differential equations。

机器人姿态和 3D vision 因此自然生活在 $SO(3)$、$SE(3)$ 上。

## 物理：对称性比方程更深

20 世纪物理不断发现：

- rotational symmetry；
- translation symmetry；
- gauge symmetry；

可以强烈约束物理规律。

Noether theorem 更把 continuous symmetry 与 conservation law 连接起来。

例如时间平移对称性与能量守恒相关。

## 晶体

crystal 的空间对称性通过 group 分类。材料性质与允许的 symmetry 直接相关。

## 粒子物理

Standard Model 使用 Lie groups：

$$
SU(3)\times SU(2)\times U(1).
$$

这里 group 不只是“漂亮分类”，而是决定允许相互作用的结构语言。

## AI 中的 symmetry

若模型尊重数据的 symmetry，可以降低学习负担。

典型：

- CNN 对 translation 具有 equivariance；
- graph networks 对 node permutation 设计 invariance/equivariance；
- equivariant neural networks 面向 rotations / 3D geometry。

## 与九个核心公式的连接

Euler complex rotation → $U(1)$。  
linear algebra → group representations。  
geometry → Lie groups。  
physics → symmetry + conservation。  
GNN/CNN → equivariant learning。

## 参考

- MacTutor, Development of group theory: https://mathshistory.st-andrews.ac.uk/HistTopics/Development_group_theory/
- Armstrong, *Groups and Symmetry*.
- Hall, *Lie Groups, Lie Algebras, and Representations*.