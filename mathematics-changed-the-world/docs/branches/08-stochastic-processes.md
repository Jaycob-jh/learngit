# 随机过程：把“随时间变化的不确定性”变成数学对象

> **核心问题**：一个系统既随时间变化、又包含随机性时，怎样描述它的路径、记忆、波动和长期行为？

## 从随机变量到随机过程

随机变量：

$$
X:\Omega\to\mathbb R.
$$

随机过程是一族随机变量：

$$
\{X_t:t\in T\}.
$$

每个 $t$ 有一个随机变量；一次真实观察则产生整条 trajectory：

$$
t\mapsto X_t(\omega).
$$

这一步把 probability 从“单次不确定量”扩展为“随机动态系统”。

## Markov property

Markov process 的核心条件可粗略写为：

$$
P(X_{t+1}|X_t,X_{t-1},\dots)
=
P(X_{t+1}|X_t).
$$

即给定当前状态后，过去不再提供额外预测信息。

这不是说系统“没有历史”，而是说当前 state 已经压缩了与未来有关的历史信息。

## Brownian motion

Wiener process 满足：

- $W_0=0$；
- independent increments；
- $W_t-W_s\sim N(0,t-s)$；
- paths 几乎处处连续。

但其路径几乎处处不可导。

因此普通微积分不能直接处理

$$
dW_t/dt.
$$

这催生 stochastic calculus。

## Itô calculus

典型 SDE：

$$
dX_t
=
\mu(X_t,t)\,dt
+
\sigma(X_t,t)\,dW_t.
$$

Itô formula 类似 stochastic 版本的 chain rule，但多出二阶项。

若

$$
dX_t=\mu\,dt+\sigma\,dW_t,
$$

则

$$
df(X_t)
=
f'(X_t)dX_t
+
\frac12f''(X_t)\sigma^2dt.
$$

这个额外项来自 Brownian increment 的尺度：

$$
(dW_t)^2\sim dt.
$$

## Kolmogorov 的作用

1933 年 measure-theoretic axioms 为 probability 提供统一基础。Kolmogorov 同时在 Markov process、diffusion 等方向做出奠基工作。

## 现实应用

### 金融
asset price、interest rate、option pricing。

### 生物
population stochasticity、ion channel、neural spike variability。

### 通信
noise process、channel modeling。

### 排队系统
网络服务器、呼叫中心、交通。

### 物理
diffusion、thermal fluctuation。

### 机器学习
diffusion models、stochastic gradient、state-space model。

## Diffusion models 与经典随机过程

现代生成式 diffusion model 不是凭空出现。其数学连接包括：

- Markov chains；
- SDE；
- Fokker–Planck equation；
- reverse-time dynamics；
- score estimation。

因此它是现代深度学习与百年随机过程理论的汇合点。

## 与九个核心公式的连接

Bayes → probability update；  
Lebesgue → probability measure / expectation；  
微积分 → SDE；  
Taylor → Itô formula 的局部展开直觉；  
Fourier → characteristic functions / spectral processes。

## 参考

- MacTutor, Kiyosi Itô: https://mathshistory.st-andrews.ac.uk/Biographies/Ito/
- MacTutor, Kolmogorov: https://mathshistory.st-andrews.ac.uk/Biographies/Kolmogorov/
- Øksendal, *Stochastic Differential Equations*.