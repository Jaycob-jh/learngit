# 02｜Taylor 展开：把复杂世界局部变成多项式

> **一句话**：只要一个函数在某点足够光滑，我们就可以让一个多项式在该点匹配它的函数值、斜率、曲率以及更高阶变化。

## 1. 前世：为什么需要无穷级数？

17–18 世纪的数学家面对大量“没有初等闭式解”的问题：行星轨道、三角函数、对数、微分方程。一个自然策略是把复杂函数写成

$
a_0+a_1x+a_2x^2+\cdots
$

因为多项式容易加减、微分、积分和计算。

Gregory、Newton、Leibniz、Bernoulli 等都发展过级数方法。Brook Taylor 在 1712 年通信和 1715 年著作中系统给出后来以他命名的展开。Maclaurin 展开只是以 $a=0$ 为中心的 Taylor 展开。

## 2. 公式从哪里来？

希望找一个 $n$ 次多项式

$
P_n(x)=c_0+c_1(x-a)+\cdots+c_n(x-a)^n
$

使它在 $x=a$ 处与 $f$ 的前 $n$ 阶导数全部一致：

$
P_n^{(k)}(a)=f^{(k)}(a),\quad k=0,\dots,n.
$

逐阶比较可得

$
c_k=\frac{f^{(k)}(a)}{k!},
$

因此

$
P_n(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k.
$

若余项趋于零，则可以写成无穷级数

$
f(x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k.
$

## 3. 关键不是级数，而是余项

Lagrange 型余项：

$
R_n(x)=
\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$

其中 $\xi$ 位于 $a$ 与 $x$ 之间。

这告诉我们：**近似是否可信，取决于下一阶导数和离展开中心有多远。**

## 4. 一个重要反例：光滑 ≠ 可解析

有些函数无限次可导，但 Taylor 级数仍不能在邻域中还原原函数。

经典例子：

$
f(x)=
\begin{cases}
e^{-1/x^2}, & x\ne0,\\
0,&x=0.
\end{cases}
$

它在 $0$ 处所有阶导数都为 0，所以 Taylor 级数恒为 0，但 $x\ne0$ 时函数并不为 0。

因此：

$
C^\infty \not\Rightarrow \text{analytic}.
$

## 5. 为什么现代计算机离不开 Taylor 思想？

计算机原生只能高效执行有限次算术。很多 transcendental function 的高精度算法，都依赖级数、区间化简、逼近理论或与 Taylor 同源的局部多项式思想。

### 优化
二阶局部模型：

$
f(x+\Delta)
\approx
f(x)+\nabla f(x)^T\Delta
+\frac12\Delta^TH\Delta.
$

这直接连接 Newton optimization、Hessian、Laplace approximation。

### 控制
非线性系统

$
\dot x=f(x,u)
$

在平衡点附近通过 Jacobian 做一阶 Taylor 展开，可以得到线性状态空间模型。

### 物理
“小参数展开”贯穿经典力学、量子力学、场论和天体力学。

## 6. 现实应用

- 自动驾驶与机器人：局部线性化动力学；
- 神经网络：分析损失曲率和优化稳定性；
- 数值 ODE/PDE：高阶时间步进公式；
- 工程误差传播；
- 科学计算中的函数逼近。

## 7. 常见误解

**Taylor 级数不是“万能精确展开”。**  
有限阶 Taylor 是局部近似；无穷 Taylor 是否等于原函数需要额外条件。

**阶数越高不一定数值越好。**  
浮点误差、消去误差和离中心过远都可能破坏效果。

## 8. 动手实验

\`\`\`bash
python labs/02_taylor_animation.py
\`\`\`

程序会逐阶增加 $P_1,P_3,P_5,\dots$，展示多项式如何从展开中心向外逼近 $\sin x$。

## 9. 向外延伸

- Taylor → Newton 法与凸优化；
- Taylor → 数值分析中的截断误差；
- Taylor → 微扰理论；
- Taylor → 深度学习 Hessian / curvature。

## 参考

- MacTutor, Brook Taylor: https://mathshistory.st-andrews.ac.uk/Biographies/Taylor/
- Rudin, *Principles of Mathematical Analysis*.
- Burden & Faires, *Numerical Analysis*.