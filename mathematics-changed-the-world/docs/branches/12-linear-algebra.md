# 线性代数：现代科技最常用的“高维关系语言”

> **核心问题**：当变量很多、关系又近似线性时，怎样把整个系统压缩成向量、矩阵和线性变换？

## 线性方程组比“矩阵”古老得多

中国《九章算术》等古代数学传统已经包含系统消元思想。

后来 determinant、simultaneous equations、geometry 等路线逐渐汇流。19 世纪 matrix 才成为独立对象：

- Sylvester 在 1850 年使用 matrix 一词；
- Cayley 1858 年系统发展 abstract matrix algebra。

这提醒我们：

> “矩阵记号”出现得很晚，但线性问题存在了很久。

## 矩阵真正代表什么？

最重要的理解不是“二维数字表”，而是：

\[
A:\mathbb R^n\to\mathbb R^m
\]

表示 linear transformation。

矩阵乘法

\[
AB
\]

对应变换 composition。

因此“为什么矩阵乘法规则看起来怪”，答案是：它必须让 composition 正确工作。

## Ax=b

\[
Ax=b
\]

是 scientific computing 的基础结构。

问题包括：

- 是否有解？
- 解唯一吗？
- 对输入误差敏感吗？
- 怎样在百万/十亿维上高效求解？

## Eigenvalue

\[
Av=\lambda v.
\]

\(v\) 是被变换后方向不变的特殊向量，只被 scale。

现实意义：

- vibration modes；
- quantum energy states；
- stability；
- PCA；
- graph spectrum；
- PageRank。

## SVD：最重要的矩阵分解之一

\[
A=U\Sigma V^T.
\]

SVD 把任意矩阵分成：

1. 旋转/正交变换；
2. 按不同方向缩放；
3. 再旋转。

它揭示：

- rank；
- dominant directions；
- best low-rank approximation；
- condition number。

## PCA

中心化数据矩阵 \(X\) 的 principal components 与 covariance eigenvectors / SVD 密切相关。

本质上：

> 找到数据方差最大的正交方向。

## AI 为什么基本等于大规模线性代数 + 非线性？

神经网络层：

\[
h=\sigma(Wx+b).
\]

Transformer 的：

\[
Q=XW_Q,\quad
K=XW_K,\quad
V=XW_V
\]

仍是矩阵乘法。

GPU/TPU 的核心价值之一，就是把大规模 matrix/tensor operations 做得极快。

## 现实应用

- graphics 3D transformations；
- MRI inverse problems；
- machine learning；
- recommendation；
- control；
- quantum mechanics；
- network analysis；
- least squares；
- statistics。

## 与其他主干连接

线性代数 + 微积分 → optimization。  
线性代数 + probability → statistics。  
线性代数 + graphs → spectral graph theory。  
线性代数 + functions → functional analysis。  
线性代数 + geometry → manifolds / Lie groups。

## 参考

- MacTutor, Matrices and determinants: https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/
- Strang, *Linear Algebra and Its Applications*.
- Trefethen & Bau, *Numerical Linear Algebra*.