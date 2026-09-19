# 小波：Fourier 看“有什么频率”，小波还问“这个频率在什么时候出现”

> **核心问题**：怎样同时获得频率信息与局部时间/空间位置？

## Fourier 的局限不是“错误”，而是全局性

Fourier basis：

$
e^{i\omega t}
$

在整个时间轴上延伸。

若信号是 stationary 的，这非常合适；但如果一个高频事件只在很短时间出现，单纯 global spectrum 会告诉你“有高频”，却不直接告诉你“在哪里出现”。

## Windowed Fourier

一种改进是短时 Fourier：

$
\operatorname{STFT}_x(\tau,\omega)
=
\int
x(t)w(t-\tau)e^{-i\omega t}\,dt.
$

问题在于固定 window width 意味着所有频率使用同样的时间—频率分辨率。

## Wavelet transform

连续小波：

$
W_x(a,b)
=
\frac1{\sqrt{|a|}}
\int
x(t)
\overline{
\psi\left(\frac{t-b}{a}\right)
}
dt.
$

其中：

- $b$：位置；
- $a$：scale；
- $\psi$：mother wavelet。

改变 scale 相当于“伸缩观察镜头”。

## 多分辨率思想

粗尺度看趋势，细尺度看局部细节。

这与图像金字塔和 signal processing 的 filter bank 产生深刻联系。

Mallat 与 Meyer 在 1980s 形成 multiresolution analysis 框架；Daubechies 构造了紧支撑正交 wavelet，令理论更适合数值实现和压缩。

## Haar wavelet

最简单 wavelet：

$
\psi(t)=
\begin{cases}
1,&0\le t<1/2,\\
-1,&1/2\le t<1,\\
0,&\text{otherwise}.
\end{cases}
$

它计算的本质是“左半平均与右半平均之差”。

因此 wavelet coefficient 天然对局部变化、边缘和突变敏感。

## 现实应用

- JPEG 2000；
- 图像去噪；
- ECG/EEG 瞬态检测；
- 地震信号；
- 多尺度 PDE；
- 压缩感知的稀疏表示；
- texture 与 edge analysis。

## 为什么小波与现代机器学习仍有关？

深度网络中很多层级特征也具有多尺度结构。scattering transform 把 wavelet 与非线性层级表示连接起来。

CNN 并不等于 wavelet transform，但二者共享：

- local filters；
- translation structure；
- multi-scale representation。

## Fourier vs Wavelet

| 问题 | Fourier | Wavelet |
|---|---|---|
| 频率分解 | 强 | 强 |
| 时间定位 | 弱 | 强 |
| 固定/可变分辨率 | 全局频率 | 多尺度 |
| 突变检测 | 可做但不局部 | 天然适合 |
| 理论结构 | harmonic analysis | multiresolution / harmonic analysis |

## 与九个核心公式的连接

Fourier → function spaces → wavelet basis。  
Lebesgue → $L^2$ 正交基。  
Taylor → local approximation。  
signal processing → filter banks。

## 参考

- Ingrid Daubechies, *Ten Lectures on Wavelets*, SIAM: https://epubs.siam.org/doi/book/10.1137/1.9781611970104
- Mallat, *A Wavelet Tour of Signal Processing*.