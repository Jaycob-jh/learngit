# 06｜留数定理：为什么一整圈积分只“读取”奇点附近的一个系数

> **一句话**：复函数沿闭曲线的积分，在许多情况下由曲线内部少数奇点决定，而每个奇点只需要读取 Laurent 展开的 $(z-z_0)^{-1}$ 系数。

## 1. 从 Cauchy 定理开始

若 $f(z)$ 在闭曲线 $\gamma$ 及其内部全纯，则

$
\oint_\gamma f(z)\,dz=0.
$

这件事与实变积分的直觉非常不同。复可微比实可微强得多；全纯函数受到极强约束。

于是自然问题变成：

> 闭路积分什么时候不为零？

答案往往是：曲线内部出现了奇点。

## 2. Laurent 展开

在孤立奇点 $z_0$ 附近，函数可能写成

$
f(z)=
\cdots+
\frac{a_{-2}}{(z-z_0)^2}
+
\frac{a_{-1}}{z-z_0}
+
a_0+a_1(z-z_0)+\cdots.
$

系数 $a_{-1}$ 就叫

$
\operatorname{Res}(f,z_0).
$

## 3. 为什么只有 $a_{-1}$ 留下来？

沿小圆 $z-z_0=re^{i\theta}$：

$
\oint (z-z_0)^n dz.
$

除了 $n=-1$ 外，其余整数次幂的闭路积分都为 0；而

$
\oint\frac{dz}{z-z_0}
=
2\pi i.
$

因此一整串 Laurent 系数中，闭路积分只“读取” $a_{-1}$。

这就是“留数”一词非常形象的地方：复杂局部结构经过积分后，真正留下的是一个系数。

## 4. 留数定理

若闭曲线内部的孤立奇点为 $z_1,\dots,z_m$：

$
\oint_\gamma f(z)\,dz
=
2\pi i
\sum_{k=1}^{m}
\operatorname{Res}(f,z_k).
$

这是一种极强的局部—全局关系。

## 5. 如何算留数？

### 简单极点

若

$
f(z)=\frac{g(z)}{h(z)},
\quad
h(z_0)=0,\quad h'(z_0)\ne0,
$

则

$
\operatorname{Res}(f,z_0)
=
\frac{g(z_0)}{h'(z_0)}.
$

### $m$ 阶极点

$
\operatorname{Res}(f,z_0)
=
\frac{1}{(m-1)!}
\lim_{z\to z_0}
\frac{d^{m-1}}{dz^{m-1}}
\left[(z-z_0)^m f(z)\right].
$

## 6. 一个经典用途：算实积分

例如

$
\int_{-\infty}^{\infty}\frac{dx}{x^2+1}.
$

把实变量 $x$ 扩展到复平面，考虑

$
f(z)=\frac{1}{z^2+1}
=
\frac{1}{(z-i)(z+i)}.
$

上半平面只有极点 $z=i$。其留数为

$
\operatorname{Res}(f,i)=\frac{1}{2i}.
$

于是半圆轮廓积分给出

$
2\pi i\cdot\frac{1}{2i}=\pi.
$

实轴积分因此等于 $\pi$。

## 7. 现实应用

- Fourier / Laplace 逆变换；
- 线性系统的 poles 与稳定性；
- Green function；
- 波传播与辐射条件；
- 量子场论中的 contour integration；
- 统计物理配分函数的渐近分析。

尤其在系统理论里，“极点”并不只是抽象奇点，它常直接决定系统的衰减、振荡和稳定性。

## 8. 常见误解

**留数不是奇点处的函数值。**  
函数在奇点处往往根本没有普通意义下的值。

**不是所有复积分都该用留数。**  
留数定理适用于闭合轮廓和合适解析结构；选轮廓本身往往才是技巧所在。

## 9. 动手实验

\`\`\`bash
python labs/06_residue_numeric.py
\`\`\`

脚本用数值积分沿圆周计算

$
\oint \frac{dz}{z-z_0}
$

并观察其趋近 $2\pi i$。

## 10. 向外延伸

Euler 公式 → Fourier → 复分析 → 留数 → Laplace / transfer function / Green function。

## 参考

- MacTutor, Cauchy's theorem: https://mathshistory.st-andrews.ac.uk/Diagrams/CauchyTheorem/
- Ahlfors, *Complex Analysis*.
- Stein & Shakarchi, *Complex Analysis*.