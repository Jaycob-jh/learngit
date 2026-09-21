# 05｜散度定理：内部发生了什么，可以从边界看出来

> **一句话**：一个区域里所有微小“源和汇”的总和，等于穿过这个区域边界的净通量。

## 1. 核心公式

设 $\Omega\subset\mathbb R^3$，边界为 $\partial\Omega$，向量场 $\mathbf F$ 足够光滑：

$$
\iiint_{\Omega}
\nabla\cdot\mathbf F\,dV
\mathrel{=}
\iint_{\partial\Omega}
\mathbf F\cdot\mathbf n\,dS.
$$

左边：内部每一点的散度累积。  
右边：穿过外边界的净流量。

## 2. 散度到底是什么？

若

$$
\mathbf F=(F_x,F_y,F_z),
$$

则

$$
\nabla\cdot\mathbf F
\mathrel{=}
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}.
$$

它衡量一个极小体积附近是“净流出”还是“净流入”。

- 正散度：像源；
- 负散度：像汇；
- 零散度：局部没有净产生或消失。

## 3. 为什么定理会成立？

把一个大区域切成很多小盒子。

每个小盒子都有六个面。两个相邻盒子共享的内部面：

- 对左盒子是“向外”；
- 对右盒子却是“向内”。

因此内部面通量两两抵消。最终只剩整个区域最外层的边界。

这就是“局部守恒累积成全局守恒”的几何原因。

## 4. 它与微积分基本定理是一回事吗？

在结构上非常接近。

一维：

$$
\int_a^b f'(x)\,dx=f(b)-f(a).
$$

三维：

$$
\int_{\Omega}\nabla\cdot F
\mathrel{=}
\int_{\partial\Omega}F\cdot n.
$$

更高层次上，Green 定理、Stokes 定理、散度定理都可以统一进广义 Stokes 定理：

$$
\int_M d\omega
\mathrel{=}
\int_{\partial M}\omega.
$$

这条结构是现代微分几何的重要桥梁。

## 5. 历史为什么不能只写“高斯定理”？

今天它常叫 Gauss theorem、Gauss–Ostrogradsky theorem 或 divergence theorem。

历史上二维 Green 定理、Gauss 对三维特殊形式的工作、Ostrogradsky 的推广以及更早的流体/力学研究共同构成了发展脉络。数学定理的形成经常不是某一天由单一人物完整写出。

## 6. 现实应用

### 电磁学
Gauss law：

$$
\nabla\cdot\mathbf E=\rho/\varepsilon_0
$$

积分后把体内电荷与边界电通量联系起来。

### 流体
质量守恒可以从积分形式转成局部连续性方程。

### 热传导
控制体积方法通过边界热流和内部能量变化建立数值模型。

### CFD / 有限体积法
工程软件把空间分成许多 control volume，直接利用“流入 - 流出 = 内部变化”。

## 7. 一个重要思想：积分形式 vs 微分形式

物理定律常有两种写法：

- **积分形式**：适合控制体积、全局守恒；
- **微分形式**：适合描述每一点的局部变化。

散度定理负责在二者之间转换。

## 8. 动手实验

\`\`\`bash
python labs/05_divergence_flux.py
\`\`\`

示例使用二维向量场做可视化类比：比较内部离散散度求和和边界通量。

## 参考

- Encyclopedia of Mathematics, Divergence theorem: https://encyclopediaofmath.org/wiki/Divergence_theorem
- Spivak, *Calculus on Manifolds*.
- Griffiths, *Introduction to Electrodynamics*.