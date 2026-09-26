# 学习路线：不用从第一页读到最后一页

## 路线 A｜想建立“数学世界观”

适合：对历史、思想、科学哲学感兴趣，但不要求马上推很复杂公式。

顺序：

1. 微积分基本定理
2. Euler 公式
3. Fourier
4. Bayes
5. 素数与 Riemann
6. 非欧几何
7. 拓扑
8. 信息论
9. 可计算性
10. 混沌

目标是理解十次观念变化：

- 连续变化可以计算；
- 虚数可以有几何意义；
- 复杂信号可以换坐标；
- 不确定性可以更新；
- 随机外观可能有宏观规律；
- 几何不是唯一；
- 形状可以研究不变量；
- 信息可以量化；
- 算法有根本边界；
- 确定性不等于可预测。

---

## 路线 B｜工程 / 信号 / MRI / BCI

建议：

1. 复数
2. Euler
3. 微积分
4. 线性代数
5. 微分方程
6. Fourier
7. 散度定理
8. 概率
9. Bayes
10. 随机过程
11. 控制论
12. 小波
13. 数值分析
14. 凸优化

建议同步运行：

- Fourier decomposition；
- wavelet demo；
- Kalman filter；
- Taylor approximation。

你应该最终能回答：

> 一个真实传感器信号从采集、滤波、特征、状态估计到控制，分别用了哪些数学？

---

## 路线 C｜机器学习 / AI

先修链：

$$
\text{线性代数}
\to
\text{微积分}
\to
\text{概率}
\to
\text{优化}.
$$

然后：

1. Taylor：理解梯度、Hessian、局部曲率；
2. Bayes：理解 likelihood/prior/posterior；
3. 信息论：cross-entropy、KL；
4. 数值分析：floating point、conditioning；
5. 图论：GNN；
6. Transformer 数学；
7. 随机过程：diffusion model；
8. 微分几何：manifold / equivariant learning；
9. 泛函分析：kernel / operator viewpoints。

不要把 AI 数学学成“背反向传播公式”。真正需要的是：

- representation；
- uncertainty；
- optimization；
- generalization；
- computation。

---

## 路线 D｜物理

1. 微积分
2. Euler/complex
3. 微分方程
4. 线性代数
5. Fourier
6. 散度 / Stokes
7. 非欧几何
8. 微分几何
9. 群论
10. 泛函分析
11. 概率/随机过程
12. 数值分析

连接：

- classical mechanics → ODE；
- electromagnetism → vector calculus；
- quantum → complex Hilbert space；
- relativity → differential geometry；
- particle physics → Lie groups；
- statistical physics → probability。

---

## 路线 E｜纯数学 / 理论路线

1. real analysis；
2. complex analysis；
3. Lebesgue measure；
4. linear algebra；
5. abstract algebra / groups；
6. topology；
7. functional analysis；
8. differential geometry；
9. analytic number theory；
10. probability measure theory。

这个路线会逐渐看到一个重要转变：

> 数学从“算一个答案”变成“研究对象所属空间、允许的变换和保持不变的结构”。

---

## 如何使用实验

每读一章做四件事：

1. 跑通默认实验；
2. 改一个参数；
3. 故意破坏一个条件；
4. 解释“为什么坏了”。

例如：

- Taylor 把范围扩大到很远；
- FFT 改采样率；
- Bayes 改 prior 和 false-positive；
- Kalman 把 $R,Q$ 设错；
- attention 去掉 $1/\sqrt{d_k}$。

最后一步通常最有学习价值。

---

## 路线 F｜系统学习最优化

如果希望从“凸优化概念”进一步进入完整课程体系，可沿 [北大文再文最优化学习体系](courses/optimization-pku-wenzw.md) 学习。

建议顺序：

线性代数/数值代数 → 微积分/Taylor → 概率 → 凸分析 → 最优性与对偶 → 无约束算法 → 约束算法 → 复合/近端算法 → 随机与大规模优化 → 稀疏/低秩/最优传输等数据问题。

该路线尤其适合把路线 B 的工程优化与路线 C 的机器学习优化补成一套可实现、可验证的课程链。
