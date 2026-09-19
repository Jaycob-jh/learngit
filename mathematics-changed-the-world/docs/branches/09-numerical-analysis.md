# 数值分析：数学公式到了计算机里，为什么会“变质”？

> **核心问题**：当实数变成有限精度浮点数、连续对象变成离散网格、无限过程变成有限迭代时，怎样保证结果可靠？

## 数值计算比电子计算机古老得多

古代求平方根、天文表、插值、数值积分都是 numerical mathematics。

但电子计算机出现后，问题发生质变：

> 不是“能不能手算”，而是“算法在有限精度机器上是否稳定、复杂度是否可接受”。

现代 numerical analysis 因此同时研究：

- approximation；
- error；
- stability；
- conditioning；
- complexity。

## 误差至少有三类

### 建模误差
现实被数学模型简化。

### 离散化/截断误差
例如导数：

$$
f'(x)
\approx
\frac{f(x+h)-f(x)}{h}.
$$

这不是精确等式。

### floating-point roundoff
计算机不能精确表示大多数实数。

## 一个反直觉：$h$ 越小不一定越好

差分导数中：

- $h$ 太大 → truncation error 大；
- $h$ 太小 → 两个非常接近的数相减，roundoff / catastrophic cancellation 放大。

因此最佳 $h$ 常是折中，而不是趋近机器能表示的最小数。

## Conditioning vs stability

**condition number** 描述“问题本身”对输入扰动敏感不敏感。

**algorithm stability** 描述“算法实现”是否额外放大误差。

一个 ill-conditioned problem，即便算法很好，也可能无法从噪声输入得到高精度答案。

一个 well-conditioned problem，也可能被 bad algorithm 算坏。

## Linear systems 是核心基础设施

$$
Ax=b.
$$

Gaussian elimination、LU、QR、Cholesky、iterative methods、Krylov methods 是 scientific computing 的骨架。

很多 PDE 离散后最终都会变成巨大的 sparse linear system。

## Eigenvalue problems

$$
Av=\lambda v.
$$

出现在：

- vibration；
- quantum mechanics；
- PCA；
- stability；
- graph spectral analysis；
- PageRank。

## 数值 PDE

连续 PDE 需要离散化：

- finite difference；
- finite element；
- finite volume；
- spectral methods。

散度定理直接影响 finite volume；Fourier directly connects spectral methods。

## 为什么现代 AI 也是数值分析问题？

训练大模型本质上执行海量 floating-point linear algebra。

实际系统关注：

- mixed precision；
- conditioning；
- gradient scaling；
- optimizer stability；
- iterative convergence；
- matrix multiplication error；
- hardware-aware algorithms。

因此“AI 工程”和传统 numerical linear algebra 并不是两套世界。

## 一条现代历史线

手工表格  
→ mechanical computation  
→ early electronic computer  
→ floating-point analysis  
→ numerical linear algebra  
→ scientific computing / HPC  
→ GPU tensor computing。

SIAM 的 numerical analysis history 项目记录了现代 scientific computing 多位开拓者的口述史。

## 与九个核心公式的连接

Taylor → truncation error；  
Fourier → spectral method / FFT；  
散度 → finite volume；  
Lebesgue → function space 与收敛；  
线性代数 → 所有大规模离散计算。

## 参考

- SIAM, History of Numerical Analysis and Scientific Computing: https://history.siam.org/
- Higham, *Accuracy and Stability of Numerical Algorithms*.
- Trefethen & Bau, *Numerical Linear Algebra*.