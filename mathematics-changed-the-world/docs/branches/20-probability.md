# 概率论：把不确定性从直觉变成可计算结构

> **核心问题**：随机事件能否像长度、面积一样拥有一致的数学规则？

## 从赌博问题开始，但没有停在那里

17 世纪 Pascal 与 Fermat 关于赌博分赌金问题的通信，是 probability history 的经典起点之一。

早期概率长期与：

- gambling；
- insurance；
- mortality tables；
- astronomy errors；

紧密相关。

## Bernoulli：大数规律

若独立重复试验成功概率为 $p$，样本比例：

$$
\hat p_n
\mathrel{=}
\frac1n\sum_{i=1}^n X_i
$$

会随着 $n$ 增大趋近 $p$。

这揭示概率学的核心张力：

> 单次事件不可确定，大量重复却出现稳定规律。

## 从组合概率到 distribution

18–19 世纪 De Moivre、Laplace、Gauss 等发展：

- normal approximation；
- error distribution；
- limit ideas；
- inverse probability。

统计学开始与 probability 深度融合。

## Kolmogorov 1933

现代 probability space：

$$
(\Omega,\mathcal F,P).
$$

其中：

- $\Omega$：sample space；
- $\mathcal F$：events 的 sigma-algebra；
- $P$：probability measure。

公理：

$$
P(A)\ge0,
$$

$$
P(\Omega)=1,
$$

对互斥 $A_i$：

$$
P\left(\bigcup_iA_i\right)
\mathrel{=}
\sum_iP(A_i).
$$

这把 probability 建立在 measure theory 上。

## Random variable

随机变量不是“一个随机变化的数字”，而是函数：

$$
X:\Omega\to\mathbb R.
$$

distribution：

$$
P_X(B)
\mathrel{=}
P(X\in B).
$$

这种抽象让我们不必追踪 sample space 的所有细节，而专注观测量的概率规律。

## Expectation

$$
E[X]
\mathrel{=}
\int_\Omega X\,dP.
$$

这就是 Lebesgue integral。

因此现代 probability 不是 analysis 的旁支，而与 measure theory 深度统一。

## 三类基本问题

### 描述
distribution 是什么？

### 推断
观察 data 后 unknown parameters 是什么？

### 预测
future / unseen variable 的分布是什么？

Bayesian statistics、frequentist statistics、stochastic processes 都是在这些问题上发展出的不同工具。

## Probability 与 randomness 的哲学

同一套 probability calculus 可以有不同解释：

- frequentist；
- Bayesian degree of belief；
- propensity 等。

数学公理与“概率究竟意味着什么”的哲学解释需要区分。

## 现实应用

- clinical trials；
- reliability；
- finance；
- genetics；
- weather ensemble；
- communications；
- AI；
- randomized algorithms；
- quantum measurement。

## 一条主链

Pascal/Fermat  
→ Bernoulli/Laplace/Gauss  
→ measure theory  
→ Kolmogorov  
→ stochastic processes / modern statistics / ML。

## 与核心九章连接

Bayes 公式是 probability 的 conditional update。  
Lebesgue integral 给 expectation 基础。  
Fourier transform 进入 characteristic function。  
随机过程把 probability 放入 time dynamics。

## 参考

- MacTutor, Kolmogorov: https://mathshistory.st-andrews.ac.uk/Biographies/Kolmogorov/
- Billingsley, *Probability and Measure*.
- Durrett, *Probability: Theory and Examples*.