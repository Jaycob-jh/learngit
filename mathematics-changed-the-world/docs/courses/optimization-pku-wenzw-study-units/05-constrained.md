# Unit 05｜约束优化算法：罚函数、增广 Lagrangian、原始–对偶与内点法

> 对应电子讲义：罚函数法、增广拉格朗日函数法、线性规划内点法。
>
> 对应教材：第 7 章“约束优化算法”，本单元重点覆盖 7.1、7.2、7.3。
>
> 第二版第 7.4 节“流形约束优化算法”保留到 Unit 08 单独展开，不在本单元重复。

## 1. 一条统一主线

Unit 03 已经给出了 KKT、乘子、对偶和约束品性。Unit 05 开始问：

> 算法怎样逐步同时降低目标值、降低约束违反、逼近正确乘子，并最终满足 KKT？

本单元把三类策略统一为：

```text
外点罚函数：把不可行性变成越来越重的代价
→ 增广 Lagrangian：罚函数 + 乘子更新
→ 原始–对偶内点：同时更新原始变量、对偶变量和互补条件
```

对一般问题

$$
\begin{aligned}
\min_x\quad & f(x)\\
\text{s.t.}\quad
& c_i(x)=0,\quad i\in E,\\
& c_i(x)\le0,\quad i\in I,
\end{aligned}
$$

算法真正要同时控制的是：

- stationarity；
- equality feasibility；
- inequality feasibility；
- dual feasibility；
- complementary slackness。

## 2. 二次罚函数：把约束变成目标的一部分

### 2.1 等式约束

对

$$
c_i(x)=0,
$$

教材定义二次罚函数

$$
P_E(x,\sigma)
=
f(x)
+
\frac{\sigma}{2}
\sum_{i\in E}c_i(x)^2.
$$

罚因子 $\sigma>0$ 越大，不可行点受到的惩罚越强。

典型外迭代是：

```text
选择 σ_0
→ 近似求解 min P_E(x,σ_k)
→ 增大 σ_k
→ 用上一子问题的解 warm start
→ 重复
```

这也是 continuation 思想的一种形式。

### 2.2 不等式约束

对

$$
c_i(x)\le0,
$$

不能直接罚 $c_i(x)^2$，否则严格可行的 $c_i(x)<0$ 也会被惩罚。

教材采用

$$
[c_i(x)]_+
=
\max\{c_i(x),0\},
$$

并构造

$$
P_I(x,\sigma)
=
f(x)
+
\frac{\sigma}{2}
\sum_{i\in I}[c_i(x)]_+^2.
$$

这只惩罚违反约束的部分。

教材指出：该平方正部函数可导，但一般不是二阶可导，因此不能简单把普通光滑 Newton 理论原样套上去。

## 3. 二次罚函数为什么会数值变难？

二次罚函数法为了逼近严格可行性，通常需要

$$
\sigma_k\to+\infty.
$$

教材对等式约束给出的 Hessian 结构可写成

$$
\nabla^2_{xx}P_E(x,\sigma)
=
\nabla^2f(x)
+
\sigma\sum_i c_i(x)\nabla^2c_i(x)
+
\sigma\nabla c(x)\nabla c(x)^T.
$$

在接近解时，最后一项随 $\sigma$ 放大，而它通常只在约束法向方向上强化曲率。

结果是：

> 约束违反越来越小，但子问题条件数可能越来越差。

这就是罚函数的核心权衡：

```text
更大的 σ
→ 更接近可行域
→ 但子问题更病态
```

## 4. 罚函数收敛：必须保留前提

教材定理 7.1 的结论不是无条件的。

如果：

- 每个二次罚函数子问题都取得全局极小解；
- $\sigma_k$ 单调趋于 $+\infty$；

那么这些子问题解序列的每个极限点都是原问题的全局极小解。

实际中通常只能近似求子问题。教材定理 7.2进一步要求：

- 子问题一阶残差趋于零；
- $\sigma_k\to+\infty$；
- 极限点处等式约束梯度线性无关；

此时极限点满足原问题 KKT，而且

$$
-\sigma_k c_i(x_{k+1})
\to
\lambda_i^*.
$$

所以罚函数不仅在逼近可行性，还隐式地“制造”出乘子估计。

## 5. 精确罚函数：有限罚因子也可能够用

教材还介绍 $\ell_1$ 精确罚函数：

$$
P(x,\sigma)
=
f(x)
+
\sigma
\left(
\sum_{i\in E}|c_i(x)|
+
\sum_{i\in I}[c_i(x)]_+
\right).
$$

和二次罚函数不同，它是非光滑的。

教材定理 7.3 给出一个局部精确性结论：若 $x^*$ 是严格局部极小点并满足 KKT，乘子为 $\lambda^*$，则当

$$
\sigma>\|\lambda^*\|_\infty
$$

时，$x^*$ 也是该 $\ell_1$ 罚函数的局部极小点。

所以“精确”指的是：

> 不需要让罚因子趋于无穷，有限大的罚因子就可能保留原问题局部解。

但代价是子问题变成非光滑问题，这会和 Unit 06 的 proximal 方法衔接。

## 6. 增广 Lagrangian：用乘子避免一味增大罚因子

对等式约束，教材定义

$$
L_\sigma(x,\lambda)
=
f(x)
+
\sum_{i\in E}\lambda_i c_i(x)
+
\frac{\sigma}{2}
\sum_{i\in E}c_i(x)^2.
$$

给定 $(\lambda_k,\sigma_k)$，先近似求

$$
x_{k+1}
\approx
\arg\min_x
L_{\sigma_k}(x,\lambda_k),
$$

再更新乘子

$$
\lambda_{k+1}
=
\lambda_k
+
\sigma_k c(x_{k+1}).
$$

这里的关键不是“多加了一项”，而是：

```text
二次罚函数
只靠 σ 压约束

增广 Lagrangian
靠 σ + λ_k 一起控制约束
```

教材由

$$
c_i(x_{k+1})
\approx
\frac{\lambda_i^*-\lambda_i^k}{\sigma_k}
$$

解释了这一点：当乘子已经接近真实乘子时，即使 $\sigma_k$ 不是极端大，约束违反也可以很小。

## 7. 增广 Lagrangian 的局部精确性

教材定理 7.4 的条件包括：

- $x^*$ 是等式约束问题局部极小点；
- 对应乘子为 $\lambda^*$；
- LICQ 成立；
- 二阶充分条件成立。

则存在有限的 $\bar\sigma$，使得对

$$
\sigma\ge\bar\sigma,
$$

$x^*$ 是

$$
L_\sigma(x,\lambda^*)
$$

的严格局部极小点。

这正是 ALM 相比纯二次罚函数的重要优势之一：

> 在乘子正确或足够接近时，不必靠 $\sigma\to\infty$ 才能锁定局部解。

## 8. 一般不等式约束的 ALM

教材通过松弛变量把

$$
c_i(x)\le0
$$

改写成

$$
c_i(x)+s_i=0,
\qquad
s_i\ge0.
$$

消去 $s_i$ 后，增广 Lagrangian 中出现

$$
\max\left\{
\frac{\mu_i}{\sigma}+c_i(x),0
\right\}.
$$

对应乘子更新为：

### 等式约束

$$
\lambda_i^{k+1}
=
\lambda_i^k
+
\sigma_k c_i(x_{k+1}).
$$

### 不等式约束

$$
\mu_i^{k+1}
=
\max\{
\mu_i^k+\sigma_k c_i(x_{k+1}),
0
\}.
$$

这个投影式更新直接维护

$$
\mu_i^{k+1}\ge0.
$$

教材的算法 7.6 还把“约束违反是否已经足够小”作为参数更新逻辑的一部分：

- 若违反度下降得足够好：更新乘子、提高子问题精度，罚因子可保持；
- 若违反度不够好：暂缓乘子更新并增大罚因子。

所以实际 ALM 是一个双层控制系统：

```text
内层：近似最小化增广 Lagrangian
外层：看约束违反 → 更新 multiplier 或 penalty
```

## 9. 凸问题中的 ALM：原始与对偶同时出现

教材第 7.2.3 对凸问题给出 ALM 收敛结论。

在相应不精确子问题条件下，如果 Slater 成立，则：

- 乘子序列有界并收敛；
- 乘子极限是对偶问题的最优解。

如果再有一个非空有界的适当下水平集，则：

- 原始迭代点序列有界；
- 所有聚点都是原问题最优解。

所以在凸问题中，ALM 的乘子更新不是一个“辅助变量技巧”，而是实实在在地在逼近**对偶最优解**。

教材在基追踪和半定规划中都进一步展示了原始问题与对偶问题两侧的 ALM 结构。

## 10. 原始–对偶结构：从 KKT 到算法

线性规划写成：

### 原始问题

$$
\begin{aligned}
\min_x\quad & c^Tx\\
\text{s.t.}\quad
& Ax=b,\\
& x\ge0.
\end{aligned}
$$

### 对偶问题

$$
\begin{aligned}
\max_y\quad & b^Ty\\
\text{s.t.}\quad
& A^Ty+s=c,\\
& s\ge0.
\end{aligned}
$$

KKT 为：

$$
Ax=b,
$$

$$
A^Ty+s=c,
$$

$$
x_i s_i=0,
$$

$$
x\ge0,\quad s\ge0.
$$

这里：

- $x$ 是原始变量；
- $y,s$ 是对偶侧变量；
- $x_i s_i=0$ 是互补松弛。

**原始–对偶算法**的含义就是：

> 不只更新 $x$，而是把原始可行性、对偶可行性和互补性放进同一套方程一起处理。

## 11. 内点法：先不碰边界，再逐渐逼近互补条件

在线性规划最优解处通常有某些分量

$$
x_i=0
$$

或

$$
s_i=0.
$$

而内点法在迭代期间保持

$$
x>0,
\qquad
s>0.
$$

它不能立即满足

$$
x_i s_i=0.
$$

所以教材把互补条件扰动为

$$
x_i s_i=\tau,
\qquad
\tau>0.
$$

于是得到中心路径方程：

$$
Ax=b,
$$

$$
A^Ty+s=c,
$$

$$
x_i s_i=\tau,
$$

$$
x>0,\quad s>0.
$$

当

$$
\tau\downarrow0,
$$

这条路径逼近原始 KKT 系统。

## 12. Barrier 视角与中心路径

教材指出中心路径也可以从对数 barrier 问题理解：

$$
\begin{aligned}
\min_x\quad
& c^Tx
-
\tau\sum_{i=1}^n\log x_i\\
\text{s.t.}\quad
& Ax=b.
\end{aligned}
$$

这里

$$
-\log x_i
$$

在 $x_i\downarrow0$ 时趋于 $+\infty$，所以迭代点被留在严格内部。

随着 $\tau$ 变小，barrier 逐渐减弱，允许解越来越接近边界上的 LP 最优点。

这和外点罚函数正好形成对照：

| 方法 | 迭代位置 |
|---|---|
| 外点罚函数 | 通常在可行域外逐渐逼近 |
| 内点/barrier | 始终在可行域严格内部移动 |

## 13. 原始–对偶 Newton 系统

对扰动 KKT 方程做 Newton 线性化，可以同时求：

$$
(\Delta x,\Delta y,\Delta s).
$$

然后更新

$$
x_{k+1}=x_k+\alpha\Delta x,
$$

$$
y_{k+1}=y_k+\alpha\Delta y,
$$

$$
s_{k+1}=s_k+\alpha\Delta s.
$$

步长 $\alpha$ 必须保证

$$
x_{k+1}>0,
\qquad
s_{k+1}>0.
$$

因此内点法虽然使用 Newton 型方向，但还要做“fraction-to-boundary”式的步长控制，防止走出严格内部。

主要计算代价集中在原始–对偶 Newton 线性系统的求解。

## 14. 对偶间隙与中心路径

若 $(x,y,s)$ 同时满足原始和对偶可行性，则

$$
c^Tx-b^Ty
=
x^Ts.
$$

在中心路径上

$$
x_i s_i=\tau,
$$

因此

$$
x^Ts=n\tau.
$$

这给出了非常直观的停止尺度：

> 当互补乘积和对偶间隙都趋近于零时，原始–对偶对正在逼近 KKT 解。

这里是由教材给出的原始/对偶可行方程与中心路径方程直接推得的代数结果。

## 15. 路径追踪：不是每次从头解 barrier 子问题

实际算法不会为每一个更小的 $\tau$ 完全从头求解。

更常见的路径追踪逻辑是：

```text
选择当前中心参数
→ Newton 校正到中心路径附近
→ 降低中心参数
→ 用当前点 warm start
→ 重复
```

这和罚函数 continuation 在结构上有相似之处：

- 都是一系列参数化子问题；
- 都利用上一阶段解 warm start；
- 但一个从外侧压向可行域，一个从内部沿中心路径走向边界。

## 16. 三类算法的统一比较

| 方法 | 核心参数 | 原始可行性 | 对偶变量 | 主要数值问题 |
|---|---|---|---|---|
| 二次罚函数 | $\sigma\uparrow\infty$ | 渐近逼近 | 隐式出现 | 大 $\sigma$ 导致病态 |
| 精确 $\ell_1$ 罚函数 | 有限 $\sigma$ | 可有限参数精确 | 阈值与乘子相关 | 非光滑子问题 |
| 增广 Lagrangian | $\sigma$ + $\lambda_k$ | 通过乘子反馈逼近 | 显式更新 | 内层子问题与参数协调 |
| 原始–对偶内点 | $\tau\downarrow0$ | 维持严格内部 | 显式同时更新 | Newton/KKT 线性系统 |

## 17. 和前后单元的关系

### 来自 Unit 03

本单元算法的终点几乎都在逼近：

- stationarity；
- primal feasibility；
- dual feasibility；
- complementary slackness。

也就是 KKT。

### 通往 Unit 06

ALM 的很多子问题会包含：

- $\ell_1$；
- 投影；
- indicator function；
- 非光滑复合结构。

这正是 proximal / splitting / ADMM 的入口。

### 通往 Unit 08

第二版第 7.4 节把约束几何推进到流形：

- tangent space；
- Riemannian gradient；
- retraction；
- manifold Newton / trust-region。

这些内容会作为 Unit 08 单独处理。

## 18. 本单元实验

运行：

```bash
python labs/17_optimization_constrained.py
```

实验分两组。

### A｜二次罚函数 vs 增广 Lagrangian

问题：

$$
\min_x
\frac12\|x-q\|_2^2
\quad
\text{s.t. }
a^Tx=b.
$$

这个问题可以显式求最优解。

实验比较：

#### 纯二次罚函数

$$
\frac12\|x-q\|^2
+
\frac{\sigma}{2}(a^Tx-b)^2.
$$

随着 $\sigma$ 增大：

- 约束违反减小；
- 子问题 Hessian
  $$
  I+\sigma aa^T
  $$
  的条件数增大。

#### ALM

固定一个有限 $\sigma$，重复：

$$
x_{k+1}
=
\arg\min_x
L_\sigma(x,\lambda_k),
$$

$$
\lambda_{k+1}
=
\lambda_k
+
\sigma(a^Tx_{k+1}-b).
$$

观察：

- 约束违反快速下降；
- $\lambda_k$ 逼近真实 KKT 乘子；
- 内层 Hessian 条件数保持固定。

这正好展示“为什么要从 penalty 走向 ALM”。

### B｜原始–对偶中心路径

线性规划：

$$
\begin{aligned}
\min_{x_1,x_2}\quad & x_1+2x_2\\
\text{s.t.}\quad
& x_1+x_2=1,\\
& x_1,x_2\ge0.
\end{aligned}
$$

最优点在边界：

$$
x^*=(1,0).
$$

实验直接解一系列中心路径方程：

$$
Ax=b,
$$

$$
A^Ty+s=c,
$$

$$
x_i s_i=\tau,
$$

并逐步减小 $\tau$。

观察：

- $x_2\to0$；
- $s_1\to0$；
- $x^Ts=2\tau\to0$；
- 原始目标和对偶目标逐渐靠拢。

## 19. 练习

1. 对等式约束问题写出二次罚函数，并解释为什么需要逐步增大 $\sigma$。
2. 为什么不等式罚函数必须使用 $[c_i(x)]_+$，而不是直接 $c_i(x)^2$？
3. 教材定理 7.1 为什么在实际中较强？它对子问题解要求了什么？
4. 解释
   $$
   -\sigma_k c_i(x_{k+1})\to\lambda_i^*
   $$
   的意义。
5. 为什么二次罚函数在 $\sigma\to\infty$ 时容易病态？
6. 精确 $\ell_1$ 罚函数中的“精确”是什么意思？
7. 推导等式 ALM 的乘子更新
   $$
   \lambda_{k+1}=\lambda_k+\sigma_kc(x_{k+1}).
   $$
8. 不等式 ALM 为什么要做
   $$
   \max\{\mu_i^k+\sigma c_i(x),0\}?
   $$
9. 在凸问题中，ALM 的乘子极限为什么可以解释为对偶最优解？
10. 写出 LP 的原始、对偶和四类 KKT 条件。
11. 为什么内点法在迭代中不能直接满足 $x_is_i=0$？
12. 中心路径为什么使用 $x_is_i=\tau$？
13. 推导可行原始–对偶点的 gap：
    $$
    c^Tx-b^Ty=x^Ts.
    $$
14. 外点罚函数和 log-barrier 在“从哪一侧逼近”上有什么根本区别？
15. 为什么路径追踪和 penalty continuation 都需要 warm start？

## 20. 完成检查

进入 Unit 06 前，应能回答：

- 二次罚函数、精确罚函数、ALM 的差别是什么？
- 为什么 penalty parameter 太大会造成数值困难？
- ALM 的乘子更新在控制什么？
- 一般不等式 ALM 怎样保持乘子非负？
- 原始与对偶变量为什么应该联合看？
- LP 的 KKT 条件是什么？
- 内点法为什么维护 $x>0,s>0$？
- 中心路径和 barrier 子问题是什么关系？
- 原始–对偶 gap 为什么等于 $x^Ts$？
- 为什么 ALM 与内点法都可以看成“直接逼近 KKT”，但采用了完全不同的路径？

下一单元：[Unit 06｜复合优化：proximal、加速与分裂](06-composite.md)
