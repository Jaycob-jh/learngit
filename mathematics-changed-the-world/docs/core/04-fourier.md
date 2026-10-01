# 04｜Fourier 变换：把“看起来复杂”改写成“由哪些频率组成”

> **一句话**：Fourier 的革命不是“正弦函数很多”，而是发现换到频率坐标后，大量微分、卷积、滤波和传播问题会显著简化。

## 1. 起点其实是热

Joseph Fourier 研究一根金属杆如何传热，得到热方程

$$
\frac{\partial u}{\partial t}
\mathrel{=}
\alpha\frac{\partial^2u}{\partial x^2}.
$$

为了求解，他把初始温度分布写成正弦/余弦的叠加。今天看来这是“标准方法”，当时却极具争议：**一个带尖角、甚至不连续的函数，怎么能由光滑三角波叠加出来？**

这个问题反过来推动了函数概念、收敛理论、Riemann 积分和 Lebesgue 积分的发展。

## 2. Fourier 级数

对周期 $2\pi$ 的函数，可尝试

$$
f(x)
\sim
\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
(a_n\cos nx+b_n\sin nx).
$$

系数来自正交性，例如

$$
a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx.
$$

本质上是在无限维函数空间里做“投影”。

## 3. Fourier 变换

非周期情形下，离散频率变为连续频率：

$$
F(\omega)
\mathrel{=}
\int_{-\infty}^{\infty}
f(t)e^{-i\omega t}\,dt.
$$

逆变换在一种常见归一化下：

$$
f(t)
\mathrel{=}
\frac{1}{2\pi}
\int_{-\infty}^{\infty}
F(\omega)e^{i\omega t}\,d\omega.
$$

不同教材会把 $2\pi$ 放在不同位置，思想不变。

## 4. Fourier、Laplace 与 Z：同一族复指数变换

这三种变换确实有统一结构，但“同源”要说得更精确：它们都利用复指数把信号或系统改写到更适合分析的坐标中；真正区分它们的是**连续/离散时间、复变量所在的平面，以及收敛域（ROC）**。下面统一使用数学记号 $i=\sqrt{-1}$；电气工程教材常写 $j$。

### Fourier：沿实频率轴观察连续时间信号

$$
X_F(\omega)
\mathrel{=}
\int_{-\infty}^{\infty}
x(t)e^{-i\omega t}\,dt.
$$

这里 $\omega\in\mathbb R$。Fourier 变换直接描述频率组成，但普通积分形式要求相应的收敛条件；更一般的信号还可以在 $L^2$ 或分布意义下讨论。

### Laplace：把频率轴扩展到复 $s$ 平面

双边 Laplace 变换写作

$$
X_L(s)
\mathrel{=}
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

所以对固定的 $\sigma$，Laplace 变换可以看成对指数加权信号 $x(t)e^{-\sigma t}$ 做 Fourier 变换。只有当 Laplace 的收敛域包含虚轴 $\sigma=0$ 时，才可以写

$$
X_F(\omega)
=
X_L(i\omega).
$$

因此“Fourier 是 Laplace 在虚轴上的切片”是一个**带 ROC 条件的关系**，不是无条件恒等式。

### Z：把离散时间 Fourier 从单位圆扩展到整个复 $z$ 平面

双边 Z 变换为

$$
X_Z(z)
\mathrel{=}
\sum_{n=-\infty}^{\infty}
x[n]z^{-n},
\qquad
z=re^{i\Omega}.
$$

由于

$$
z^{-n}
=
r^{-n}e^{-i\Omega n},
$$

Z 变换可以看成对指数加权序列 $x[n]r^{-n}$ 做离散时间 Fourier 分析。当 Z 变换的 ROC 包含单位圆 $|z|=1$ 时，

$$
X_{\mathrm{DTFT}}(\Omega)
=
X_Z(e^{i\Omega}).
$$

这也是为什么单位圆在数字信号处理中如此重要。注意 **Z 变换不是 DFT**：DFT 处理有限长度数据并只取有限个离散频率点，而 Z 变换的自变量 $z$ 是复数，通常还必须连同 ROC 一起指定。

### 连续系统与离散系统之间：$z=e^{sT}$

若以采样周期 $T$ 观察连续时间模态 $e^{st}$，采样后得到

$$
e^{snT}
=
\left(e^{sT}\right)^n.
$$

因此连续时间极点/指数模态与离散时间极点之间自然出现映射

$$
z=e^{sT}
=
e^{\sigma T}e^{i\omega T}.
$$

它把：

- $s$ 平面的虚轴 $\sigma=0$ 映到 $z$ 平面的单位圆；
- 左半平面 $\sigma<0$ 映到单位圆内部；
- 右半平面 $\sigma>0$ 映到单位圆外部。

但这不意味着“Z 变换就是把 Laplace 变换简单采样一下”。从连续系统构造离散系统还涉及具体离散化方法；而且 $e^{i(\omega+2\pi/T)T}=e^{i\omega T}$，所以该映射在虚部方向是周期的，采样频率与混叠仍必须单独处理。

### ROC 为什么不能省略？

对 Laplace 与 Z 变换，同一个代数表达式可能对应不同的时域信号，区别就在 ROC。对 LTI 系统的冲激响应而言：

- 连续时间系统稳定时，其 Laplace ROC 必须包含虚轴；对因果有理系统，这等价于全部极点位于左半平面；
- 离散时间系统稳定时，其 Z 变换 ROC 必须包含单位圆；对因果有理系统，这等价于全部极点位于单位圆内部。

所以极点图、ROC、频率响应并不是三件互不相关的工具，而是同一变换结构的不同视角。

| 变换 | 时间变量 | 变换变量 | Fourier 关系 | 常见工程用途 |
|---|---|---|---|---|
| Fourier | 连续 $t$ | $\omega\in\mathbb R$ | 本体 | 频谱、滤波、PDE、成像 |
| Laplace | 连续 $t$ | $s=\sigma+i\omega$ | ROC 含虚轴时取 $s=i\omega$ | 微分方程、连续控制、极点稳定性 |
| Z | 离散 $n$ | $z=re^{i\Omega}$ | ROC 含单位圆时取 $z=e^{i\Omega}$ 得 DTFT | 数字滤波、差分方程、离散控制 |

## 5. 为什么变换之后更好算？

### 微分变乘法

$$
\mathcal F\{f'(t)\}
\mathrel{=}
i\omega F(\omega).
$$

原本的微分运算变成乘法。

### 卷积变乘法

$$
\mathcal F\{f*g\}
\mathrel{=}
F(\omega)G(\omega).
$$

因此线性时不变系统、滤波、模糊、响应都可以在频域中高效分析。

## 6. DFT 与 FFT 不要混

### DFT
对有限序列 $x_0,\dots,x_{N-1}$ 定义

$$
X_k=
\sum_{n=0}^{N-1}
x_n e^{-2\pi i kn/N}.
$$

直接计算约需 $O(N^2)$ 运算。

### FFT
FFT 是一族快速计算 DFT 的算法，把典型复杂度降到约

$$
O(N\log N).
$$

**Fourier transform 是数学对象，DFT 是离散版本，FFT 是算法。**

## 7. 现实应用

### 音频
频谱分析、均衡器、去噪、声纹。

### 通信
OFDM、频谱分配、调制解调、信道估计。

### 图像
低频常描述大尺度结构，高频常包含边缘和细节。

### MRI
MRI 采集的数据天然处于 k-space；图像重建与 Fourier 变换紧密相关。

### 光学与晶体学
衍射图样与空间结构之间具有 Fourier 关系。

### PDE
频域把某些偏微分方程化成代数方程或常微分方程。

## 8. 从 Fourier 到现代 AI

卷积神经网络背后的 convolution theorem、spectral convolution、位置编码中的不同频率、神经场的 frequency bias，都能看到 Fourier 思想的影子。

不过“Transformer 就是 Fourier”并不准确：Transformer 的核心是基于数据的 token-to-token 加权交互，而不是固定正弦基分解。

## 9. 动手实验

\`\`\`bash
python labs/04_fourier_decomposition.py
\`\`\`

程序构造多频率信号，并比较时域波形与 FFT 频谱。

## 10. 向外延伸

Fourier → Lebesgue → $L^2$ Hilbert space → 泛函分析 → 小波 → 现代信号处理。

## 参考

- MacTutor, Joseph Fourier: https://mathshistory.st-andrews.ac.uk/Biographies/Fourier/
- Stanford EE261: https://see.stanford.edu/Course/EE261
- MIT OpenCourseWare RES.6-007, Lecture 20 — The Laplace Transform: https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-20-the-laplace-transform/
- MIT OpenCourseWare RES.6-007, Lecture 22 — The z-Transform: https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-22-the-z-transform/
- MIT OpenCourseWare RES.6-007, Lecture 23 — Mapping Continuous-Time Filters to Discrete-Time Filters: https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-23-mapping-continuous-time-filters-to-discrete-time-filters/
- Oppenheim & Willsky, *Signals and Systems*.