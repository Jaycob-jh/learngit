# Fourier–Laplace–Z：从复指数到极点、采样与数字系统

> **核心问题**：为什么频谱、微分方程、控制系统、数字滤波和递推关系，会反复出现同一批复指数、极点和收敛域？

Fourier、Laplace 与 Z 变换不是三个互不相干的“公式技巧”。更统一的看法是：它们都在寻找一种表示，使**平移、微分、差分和卷积**变成更简单的乘法或代数运算。真正的分叉来自连续/离散时间、变换变量所在的空间，以及什么范围内变换真正收敛。

本页把三种变换放到同一张地图里，并继续连接到采样、控制、数字滤波、生成函数与概率论。

---

## 1. 为什么复指数总会出现？

连续时间指数

$$
e^{st},
\qquad
s=\sigma+i\omega
$$

同时编码两件事：

$$
e^{st}
=
e^{\sigma t}e^{i\omega t}.
$$

其中 $e^{\sigma t}$ 描述增长或衰减，$e^{i\omega t}$ 描述旋转或振荡。

它还是微分算子的特征函数：

$$
\frac{d}{dt}e^{st}
=
s e^{st}.
$$

所以当一个线性常系数微分方程作用在 $e^{st}$ 上时，微分会直接变成关于 $s$ 的多项式。

离散时间也有完全平行的结构。对序列

$$
z^n,
$$

延迟一个采样点只会乘一个常数：

$$
z^{n-1}
=
z^{-1}z^n.
$$

这正是 Z 变换里 $z^{-1}$ 代表单位延迟的根本原因。

> **统一视角**：连续时间里，复指数让“微分”对角化；离散时间里，几何序列让“移位/差分”对角化。

---

## 2. 三种变换放在一起

### Fourier：只观察纯振荡方向

$$
X_F(\omega)
=
\int_{-\infty}^{\infty}
x(t)e^{-i\omega t}\,dt.
$$

它沿着复 $s$ 平面的虚轴

$$
s=i\omega
$$

观察信号。

常见逆变换归一化为

$$
x(t)
=
\frac{1}{2\pi}
\int_{-\infty}^{\infty}
X_F(\omega)e^{i\omega t}\,d\omega.
$$

### Laplace：把虚轴扩展成整个复平面的一部分

双边 Laplace 变换为

$$
X_L(s)
=
\int_{-\infty}^{\infty}
x(t)e^{-st}\,dt,
\qquad
s=\sigma+i\omega.
$$

因为

$$
e^{-st}
=
e^{-\sigma t}e^{-i\omega t},
$$

它相当于先用 $e^{-\sigma t}$ 对信号做指数加权，再做 Fourier 分析。

逆变换可写成 Bromwich 积分：

$$
x(t)
=
\frac{1}{2\pi i}
\int_{\gamma-i\infty}^{\gamma+i\infty}
X_L(s)e^{st}\,ds,
$$

其中竖直积分线必须选在合适的收敛区域内。

### Z：离散时间的复变量变换

双边 Z 变换：

$$
X_Z(z)
=
\sum_{n=-\infty}^{\infty}
x[n]z^{-n}.
$$

写

$$
z=re^{i\Omega}
$$

后，

$$
z^{-n}
=
r^{-n}e^{-i\Omega n}.
$$

所以 Z 变换可以理解为：对离散序列先乘指数权重 $r^{-n}$，再做离散时间 Fourier 分析。

逆 Z 变换可写成

$$
x[n]
=
\frac{1}{2\pi i}
\oint_C
X_Z(z)z^{n-1}\,dz,
$$

其中闭合路径 $C$ 要位于 ROC 中。

---

## 3. Fourier 是 Laplace 的“切片”，但必须带 ROC 条件

若 Laplace 变换的收敛域包含虚轴 $\sigma=0$，则

$$
X_F(\omega)
=
X_L(i\omega).
$$

这时 Fourier 频率响应就是 Laplace 变换沿虚轴的取值。

关键是“**ROC 包含虚轴**”。如果虚轴不在收敛域里，普通意义下就不能直接把 $s=i\omega$ 代进去。

同理，对离散时间：

$$
X_{\mathrm{DTFT}}(\Omega)
=
X_Z(e^{i\Omega})
$$

只在 Z 变换的 ROC 包含单位圆 $|z|=1$ 时成立。

因此：

- Fourier ↔ Laplace 的特殊边界：虚轴；
- DTFT ↔ Z 的特殊边界：单位圆。

---

## 4. 为什么 ROC 不是附属信息？

只写代数表达式可能不够，因为**同一个公式可以对应不同的时域信号**。

### Laplace 例子

考虑

$$
X(s)
=
\frac{1}{s+a}.
$$

若

$$
\operatorname{Re}(s)>-a,
$$

它对应

$$
x_1(t)=e^{-at}u(t).
$$

但若

$$
\operatorname{Re}(s)<-a,
$$

同一个代数式对应

$$
x_2(t)=-e^{-at}u(-t).
$$

### Z 例子

同样，

$$
X(z)
=
\frac{1}{1-a z^{-1}}
$$

若 ROC 为

$$
|z|>|a|,
$$

则对应

$$
x_1[n]=a^n u[n].
$$

若 ROC 为

$$
|z|<|a|,
$$

则对应

$$
x_2[n]=-a^n u[-n-1].
$$

所以在 Laplace/Z 变换里，**表达式 + ROC** 才是完整信息。

---

## 5. 双边与单边：为什么工程教材有时写法不一样？

双边变换更适合讨论：

- 信号本身；
- 频率响应；
- 因果性；
- ROC；
- 双向时间序列。

但解初值问题时，单边变换往往更方便。

单边 Laplace：

$$
X_+(s)
=
\int_{0^-}^{\infty}
x(t)e^{-st}\,dt.
$$

它把初值直接带进导数公式：

$$
\mathcal L_+\{x'(t)\}
=
sX_+(s)-x(0^-).
$$

于是

$$
y'(t)+ay(t)=u(t)
$$

会变成

$$
sY(s)-y(0^-)+aY(s)=U(s).
$$

这解释了为什么 Laplace 变换在电路、控制和 ODE 初值问题中如此常见：它把**微分方程 + 初始条件**一起变成代数方程。

单边 Z 变换对差分方程扮演类似角色；初始样本会作为边界项进入变换后的代数关系。

---

## 6. 卷积为什么会被“消掉”？

对 LTI 系统，

$$
y(t)=(h*x)(t)
$$

或离散时间

$$
y[n]=(h*x)[n].
$$

在适当条件下，三类变换都会把卷积变成乘法：

$$
Y_F(\omega)
=
H_F(\omega)X_F(\omega),
$$

$$
Y_L(s)
=
H_L(s)X_L(s),
$$

$$
Y_Z(z)
=
H_Z(z)X_Z(z).
$$

所以“变换域”不是为了把公式写得更漂亮，而是在把一个积分/求和运算变成普通乘法。

---

## 7. 从微分方程到 transfer function

考虑线性常系数方程

$$
a_2y''+a_1y'+a_0y=u.
$$

在零初值条件下做 Laplace 变换：

$$
(a_2s^2+a_1s+a_0)Y(s)
=
U(s).
$$

因此

$$
H(s)
=
\frac{Y(s)}{U(s)}
=
\frac{1}{a_2s^2+a_1s+a_0}.
$$

原本的微分算子被多项式

$$
a_2s^2+a_1s+a_0
$$

取代。

离散差分方程也完全类似。若

$$
y[n]-\alpha y[n-1]=u[n],
$$

在零初值下：

$$
Y(z)-\alpha z^{-1}Y(z)
=
U(z),
$$

于是

$$
H(z)
=
\frac{1}{1-\alpha z^{-1}}.
$$

这就是“微分/差分方程 → 代数分式 → 极点与零点”的核心路径。

---

## 8. 极点、零点与频率响应的几何意义

对有理系统，可以写

$$
H(s)
=
K
\frac{\prod_k(s-z_k)}
{\prod_m(s-p_m)}
$$

或

$$
H(z)
=
K
\frac{\prod_k(z-z_k)}
{\prod_m(z-p_m)}.
$$

这里 $z_k$ 是 zeros，$p_m$ 是 poles。

在频率轴上评估时：

- 连续系统看 $s=i\omega$；
- 离散系统看 $z=e^{i\Omega}$。

频率响应的幅度可理解为“评价点到所有零点距离的乘积 / 到所有极点距离的乘积”。

因此 pole-zero plot 不只是画点：它直接编码系统在哪些频率附近放大、衰减或产生共振。

---

## 9. 稳定性为什么变成“看极点位置”？

BIBO 稳定的本质条件仍是冲激响应绝对可积/绝对可和。

对于**因果有理系统**，这进一步简化为：

### 连续时间

全部极点位于左半 $s$ 平面：

$$
\operatorname{Re}(p_k)<0.
$$

### 离散时间

全部极点位于单位圆内部：

$$
|p_k|<1.
$$

更一般的非因果系统不能只看“极点在哪一边”；还必须连同 ROC 判断。真正通用的说法是：

- 连续时间稳定 ⇒ ROC 包含虚轴；
- 离散时间稳定 ⇒ ROC 包含单位圆。

---

## 10. 采样为什么自然产生 $z=e^{sT}$？

连续时间单个模态

$$
e^{st}
$$

以采样周期 $T$ 取样：

$$
e^{s nT}
=
\left(e^{sT}\right)^n.
$$

因此离散模态自然满足

$$
z=e^{sT}.
$$

若

$$
s=\sigma+i\omega,
$$

则

$$
z
=
e^{\sigma T}e^{i\omega T}.
$$

于是：

- $\sigma=0$ 的虚轴 → 单位圆；
- $\sigma<0$ 的左半平面 → 单位圆内部；
- $\sigma>0$ 的右半平面 → 单位圆外部。

这就是连续稳定极点与离散稳定极点对应关系的几何来源。

---

## 11. 一个更精确的 Laplace–Z 连接：采样脉冲列

把离散序列表示成连续时间冲激列

$$
x_s(t)
=
\sum_{n=-\infty}^{\infty}
x[n]\delta(t-nT).
$$

对它做双边 Laplace 变换：

$$
\mathcal L\{x_s\}(s)
=
\sum_{n=-\infty}^{\infty}
x[n]e^{-snT}.
$$

而 Z 变换是

$$
X_Z(z)
=
\sum_{n=-\infty}^{\infty}
x[n]z^{-n}.
$$

因此令

$$
z=e^{sT},
$$

得到

$$
\mathcal L\{x_s\}(s)
=
X_Z(e^{sT}).
$$

这比“Z 变换就是 Laplace 变换的离散版”更准确：Z 变换与**序列对应的冲激列**的 Laplace 变换，通过变量替换 $z=e^{sT}$ 联系起来。

---

## 12. 为什么采样会有 aliasing？

因为指数映射在虚部方向具有周期性：

$$
e^{i(\omega+2\pi k/T)T}
=
e^{i\omega T},
\qquad
k\in\mathbb Z.
$$

所以相差整数倍采样角频率

$$
\frac{2\pi}{T}
$$

的连续频率会映到同一个单位圆角度。

这正是频率混叠的复平面版本。

Nyquist 条件不是一个孤立的“采样口诀”；它是在阻止多个连续频率被压到同一个离散频率上。

---

## 13. “连续系统变成离散系统”不只有一种方法

### 13.1 精确模态映射

单个连续极点

$$
p
$$

采样后自然映为

$$
z=e^{pT}.
$$

但只知道极点映射，并不自动给出完整的输入保持模型。

### 13.2 Zero-order hold（ZOH）

状态空间

$$
\dot x=Ax+Bu
$$

若输入在每个采样区间保持常数，则精确离散模型为

$$
x_{k+1}
=
A_dx_k+B_du_k,
$$

其中

$$
A_d=e^{AT},
$$

$$
B_d
=
\int_0^T e^{A\tau}B\,d\tau.
$$

所以矩阵指数直接进入数字控制。

### 13.3 Impulse invariance

一种思路是让离散系统冲激响应取自连续冲激响应的采样。它会保留相应的指数模态，因此极点出现 $z=e^{pT}$ 映射；但模拟频谱会周期复制，因此可能发生 aliasing。

### 13.4 Bilinear / Tustin transform

常见代换：

$$
s
=
\frac{2}{T}
\frac{1-z^{-1}}{1+z^{-1}}
=
\frac{2}{T}
\frac{z-1}{z+1}.
$$

它把：

- 左半 $s$ 平面映到单位圆内部；
- 虚轴映到单位圆；
- 整条模拟频率轴一一压缩到数字频率区间。

代价是 frequency warping。沿频率轴有

$$
\omega
=
\frac{2}{T}\tan\frac{\Omega}{2},
$$

即

$$
\Omega
=
2\arctan\frac{\omega T}{2}.
$$

所以 bilinear transform 避免了 impulse-invariance 式的频谱周期重叠，但频率刻度不再线性。

---

## 14. 一个一阶系统把整张图串起来

考虑低通系统

$$
\tau \dot y+y=u.
$$

连续 transfer function：

$$
H(s)
=
\frac{1}{\tau s+1}.
$$

唯一极点为

$$
p=-\frac1\tau.
$$

因为 $p<0$，它位于左半平面。

若采用 ZOH，精确状态递推为

$$
y[k+1]
=
\alpha y[k]
+
(1-\alpha)u[k],
$$

其中

$$
\alpha=e^{-T/\tau}.
$$

因为

$$
0<e^{-T/\tau}<1,
$$

离散极点

$$
z=\alpha
$$

自动落在单位圆内。

这就是

$$
-\frac1\tau
\quad\longrightarrow\quad
e^{-T/\tau}
$$

从连续衰减率到离散衰减因子的直接对应。

---

## 15. Z 变换还有一个“非工程”身份：生成函数

对单边序列，

$$
X_Z(z)
=
\sum_{n=0}^{\infty}
x[n]z^{-n}.
$$

令

$$
w=z^{-1},
$$

就得到普通生成函数

$$
G(w)
=
\sum_{n=0}^{\infty}
x[n]w^n.
$$

所以

$$
X_Z(z)
=
G(z^{-1}).
$$

这意味着 Z 变换不仅属于 DSP，也与：

- 递推关系；
- 组合数学；
- 动态系统；
- 算法复杂度中的序列分析；

有直接联系。

例如 Fibonacci 递推可以通过生成函数求解，本质上与用 Z 变换解差分方程是同一种代数策略。

---

## 16. 概率论里也藏着 Fourier/Laplace 的亲戚

随机变量 $X$ 的 characteristic function：

$$
\varphi_X(\omega)
=
\mathbb E[e^{i\omega X}]
$$

本质上是概率分布的 Fourier 型变换。

moment-generating function：

$$
M_X(t)
=
\mathbb E[e^{tX}]
$$

则具有 Laplace 型结构，但它未必对所有 $t$ 存在。

对非负整数随机变量，probability-generating function：

$$
G_X(s)
=
\mathbb E[s^X]
=
\sum_{n=0}^{\infty}
P(X=n)s^n
$$

又与普通生成函数/Z 变换形式高度相似。

所以“复指数变换”的思想并不局限于信号处理；它同样渗入概率、统计与组合数学。

---

## 17. Fourier、Laplace、Z 与小波不是竞争关系

Fourier/Laplace/Z 的共同优势是把全局指数模态组织得非常清楚。

但如果你关心：

> 某个频率**什么时候**出现？

则需要时间—频率局部化。

STFT 用固定窗：

$$
\operatorname{STFT}_x(\tau,\omega)
=
\int
x(t)w(t-\tau)e^{-i\omega t}\,dt.
$$

Wavelet 则使用随尺度变化的局部基函数。

因此可以把这条路线理解为：

$$
\text{全局复指数表示}
\to
\text{变换域代数}
\to
\text{采样与数字系统}
\to
\text{局部时频表示}.
$$

---

## 18. 最容易混淆的八件事

| 容易混淆 | 更准确的说法 |
|---|---|
| Fourier = Laplace | Fourier 可在 ROC 包含虚轴时视为 Laplace 的虚轴切片 |
| Z = Laplace 采样 | 更精确的是序列冲激列的 Laplace 变换与 Z 通过 $z=e^{sT}$ 联系 |
| Z = DFT | Z 的变量是复数；DFT 只在有限个离散频点上工作 |
| 单位圆 = 所有离散系统 | 单位圆是 DTFT 评价路径，也是稳定性判断中的关键边界 |
| 极点在左边/圆内就一定稳定 | 对因果有理系统成立；一般情况还要结合 ROC |
| $z=e^{sT}$ 就等于完整离散化 | 它精确描述模态/极点映射；输入保持方式还需另行规定 |
| Tustin 不改变频率 | 它保持稳定域映射，但会造成 frequency warping |
| FFT 是一种新变换 | FFT 是高效计算 DFT 的算法族 |

---

## 19. 一张总表

| 对象 | 连续/离散 | 变量 | 关键边界 | 典型作用 |
|---|---|---|---|---|
| Fourier transform | 连续 | $\omega$ | 实频率轴 | 频谱、卷积、PDE |
| Laplace transform | 连续 | $s=\sigma+i\omega$ | 虚轴 | ODE、控制、极点、暂态 |
| DTFT | 离散 | $\Omega$ | 单位圆上的角度 | 离散频谱 |
| Z transform | 离散 | $z=re^{i\Omega}$ | 单位圆 | 差分方程、数字控制、DSP |
| DFT | 有限离散数据 | $k$ | 单位圆上的有限采样点 | 数值频谱 |
| FFT | 算法 | — | — | 快速计算 DFT |

---

## 20. 动手实验

运行：

```bash
python labs/24_transform_family.py
```

实验观察四件事：

1. 连续一阶稳定极点位于左半平面；
2. 经过 $z=e^{sT}$ 后落到单位圆内部；
3. 同一一阶系统的模拟与采样后频率响应如何对应；
4. bilinear/Tustin 映射如何产生 frequency warping。

建议继续改坏参数：

- 增大采样周期 $T$；
- 比较 $T\ll\tau$ 与 $T\approx\tau$；
- 把模拟频率提高到 Nyquist 附近；
- 比较 ZOH、impulse invariance 与 bilinear 的差别。

---

## 21. 推荐学习顺序

如果目标是工程/信号/控制：

$$
\text{复数}
\to
\text{Euler}
\to
\text{ODE}
\to
\text{Fourier}
\to
\text{Laplace}
\to
\text{采样}
\to
\text{Z}
\to
\text{极点/零点}
\to
\text{数字滤波/控制}.
$$

如果目标是更抽象的数学理解：

$$
\text{特征函数/特征模态}
\to
\text{积分变换}
\to
\text{卷积代数}
\to
\text{复分析}
\to
\text{谱理论/泛函分析}.
$$

---

## 参考

- MIT OpenCourseWare, RES.6-007 *Signals and Systems*, Lecture 16 — Sampling:  
  https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-16-sampling/
- MIT OpenCourseWare, Lecture 20 — The Laplace Transform:  
  https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-20-the-laplace-transform/
- MIT OpenCourseWare, Lecture 22 — The z-Transform:  
  https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-22-the-z-transform/
- MIT OpenCourseWare, Lecture 23 — Mapping Continuous-Time Filters to Discrete-Time Filters:  
  https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-23-mapping-continuous-time-filters-to-discrete-time-filters/
- MIT OpenCourseWare, RES.6-007 readings for Laplace/Z ROC, inverse transforms and bilinear transformation:  
  https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/pages/readings/
- SciPy documentation, scipy.signal.bilinear_zpk:  
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bilinear_zpk.html
- Oppenheim, Willsky & Nawab, *Signals and Systems*.
- Oppenheim & Schafer, *Discrete-Time Signal Processing*.
