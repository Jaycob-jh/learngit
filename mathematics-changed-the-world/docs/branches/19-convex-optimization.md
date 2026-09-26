# 凸优化：怎样把“找最好”变成可证明可靠的算法

> **核心问题**：什么时候一个高维 optimization problem 不会到处都是糟糕 local minima？

## 一般优化

$$
\min_x f(x)
$$

subject to constraints.

若 $f$ 与 feasible region 都非常复杂，local optimum 未必 global optimum。

## Convex set

集合 $C$ convex，若任意 $x,y\in C$ 与 $0\le\theta\le1$：

$$
\theta x+(1-\theta)y\in C.
$$

直觉：任意两点之间整条线段仍在集合内。

## Convex function

$$
f(\theta x+(1-\theta)y)
\le
\theta f(x)+(1-\theta)f(y).
$$

几何上函数图像位于任意 chord 下方。

## 为什么 convex 特别？

在适当条件下：

> local minimum 就是 global minimum。

这把“搜索最好答案”从极不可靠问题变成有坚实理论的算法问题。

## First-order condition

可微 convex $f$：

$$
f(y)
\ge
f(x)+\nabla f(x)^T(y-x).
$$

函数永远位于 tangent hyperplane 之上。

若

$$
\nabla f(x^*)=0,
$$

则 $x^*$ 为 global minimizer。

## Lagrange duality

带 constraints：

$$
\min_x f_0(x)
$$

s.t.

$$
f_i(x)\le0.
$$

构造 Lagrangian：

$$
L(x,\lambda)
\mathrel{=}
f_0(x)+\sum_i\lambda_i f_i(x).
$$

dual problem 不仅用于求解，也能给 lower bound 和 optimality certificate。

## KKT

Karush–Kuhn–Tucker conditions 把：

- stationarity；
- primal feasibility；
- dual feasibility；
- complementary slackness；

组合成 constrained optimization 的核心条件。

## Machine learning

很多经典模型是 convex：

- linear regression；
- logistic regression；
- SVM；
- Lasso；
- ridge regression。

deep neural networks 通常 nonconvex，但 convex optimization 的：

- gradient methods；
- duality；
- regularization；
- proximal algorithms；
- conditioning；

仍深刻影响训练理论和算法。

## 工程应用

- resource allocation；
- portfolio；
- signal processing；
- control；
- network flow；
- experiment design；
- power systems；
- model fitting。

Stanford 的 Boyd 等推动 convex optimization 成为现代工程的通用工具箱。

## 与 Taylor 的关系

二阶 Taylor：

$$
f(x+\Delta)
\approx
f(x)
+
\nabla f^T\Delta
+
\frac12\Delta^TH\Delta.
$$

Hessian：

$$
H\succeq0
$$

是二阶可微 convex function 的重要判据。

因此 Taylor curvature 与 convexity 直接相连。

## 参考

- Boyd & Vandenberghe, *Convex Optimization*: https://web.stanford.edu/~boyd/cvxbook/
- Boyd, *Overview of Convex Optimization*: https://web.stanford.edu/~boyd/papers/cvx_opt_overview.html

## 课程化学习入口

如果希望把本章扩展成完整课程路线，进入 [北大文再文最优化学习体系](../courses/optimization-pku-wenzw.md)。

该路线把凸分析、最优性理论、无约束/约束/复合优化、大规模与随机算法，以及数据问题中的优化串成一条主线；同时保留教材、课程、代码与来源的证据状态。
