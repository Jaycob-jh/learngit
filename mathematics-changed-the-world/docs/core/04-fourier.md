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

## 4. 为什么变换之后更好算？

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

## 5. DFT 与 FFT 不要混

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

## 6. 现实应用

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

## 7. 从 Fourier 到现代 AI

卷积神经网络背后的 convolution theorem、spectral convolution、位置编码中的不同频率、神经场的 frequency bias，都能看到 Fourier 思想的影子。

不过“Transformer 就是 Fourier”并不准确：Transformer 的核心是基于数据的 token-to-token 加权交互，而不是固定正弦基分解。

## 8. 动手实验

\`\`\`bash
python labs/04_fourier_decomposition.py
\`\`\`

程序构造多频率信号，并比较时域波形与 FFT 频谱。

## 9. 向外延伸

Fourier → Lebesgue → $L^2$ Hilbert space → 泛函分析 → 小波 → 现代信号处理。

## 参考

- MacTutor, Joseph Fourier: https://mathshistory.st-andrews.ac.uk/Biographies/Fourier/
- Stanford EE261: https://see.stanford.edu/Course/EE261
- Oppenheim & Willsky, *Signals and Systems*.