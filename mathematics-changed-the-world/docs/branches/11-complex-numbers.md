# 复数：从“荒谬的平方根”到旋转、波和量子态

> **核心问题**：为什么把实数轴扩展成二维数系，反而让许多现实问题变得更自然？

## 一开始是三次方程逼出来的

16 世纪求 cubic equations 时，Cardano 公式会在某些最终具有实根的情形中出现

$$
\sqrt{-1}.
$$

这些量最初令人不安，因为它们似乎不对应普通长度。

Bombelli 系统整理了相关运算规则，逐渐让 complex arithmetic 成为可操作对象。

## 从代数怪物到平面几何

写

$$
z=x+iy.
$$

复数可以对应平面点 $(x,y)$。

于是：

- 加法 = 平移式向量加法；
- 模长

$$
|z|=\sqrt{x^2+y^2};
$$

- argument = 方向角；
- multiplication = 缩放 + 旋转。

极坐标：

$$
z=re^{i\theta}.
$$

这让 complex number 从“多出来的根”变成二维 geometry 的自然 algebra。

## Fundamental theorem of algebra

在 complex numbers 中，每个非零次数 polynomial 都能完全分解为一次因子：

$$
p(z)
\mathrel{=}
a\prod_{k=1}^{n}(z-z_k).
$$

复数因此给 polynomial equations 提供代数闭包。

## Euler 公式是转折点之一

$$
e^{i\theta}
\mathrel{=}
\cos\theta+i\sin\theta.
$$

复指数把：

- exponentials；
- trigonometry；
- rotations；
- oscillations；

连接起来。

详见 [Euler 公式](../core/03-euler.md)。

## 复可微为什么比实可微强？

若

$$
f(z)=u(x,y)+iv(x,y)
$$

complex differentiable，实部虚部需满足 Cauchy–Riemann equations：

$$
u_x=v_y,\qquad
u_y=-v_x.
$$

满足适当条件后，holomorphic function 会具有极强结构：

- 无限次可微；
- 局部 power series；
- contour integral theory；
- maximum principle。

因此 complex analysis 远不只是“二维微积分”。

## 现实应用

- AC circuits 与 phasors；
- Fourier / Laplace transforms；
- control poles；
- wave propagation；
- quantum mechanics；
- fluid potential flow；
- conformal mapping；
- electrical impedance。

## 一条知识链

$$
\text{三次方程}
\to
i
\to
\text{复平面}
\to
e^{i\theta}
\to
\text{complex analysis}
\to
\text{residue/Fourier/control}.
$$

## 参考

- Needham, *Visual Complex Analysis*.
- Ahlfors, *Complex Analysis*.
- MacTutor, Euler: https://mathshistory.st-andrews.ac.uk/Biographies/Euler/