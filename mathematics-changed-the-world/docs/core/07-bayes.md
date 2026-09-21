# 07｜Bayes 公式：把“看到新证据后该怎么改主意”写成数学

> **一句话**：Bayes 定理不是“相信主观先验”，而是一条条件概率恒等式；Bayesian inference 则把它扩展成持续更新不确定性的建模框架。

## 1. 从条件概率直接推导

定义：

$$
P(A|B)=\frac{P(A\cap B)}{P(B)},
$$

$$
P(B|A)=\frac{P(A\cap B)}{P(A)}.
$$

所以

$$
P(A\cap B)
\mathrel{=}
P(B|A)P(A)
\mathrel{=}
P(A|B)P(B).
$$

整理得

$$
P(A|B)
\mathrel{=}
\frac{P(B|A)P(A)}{P(B)}.
$$

公式本身并不神秘；真正困难的是如何建立合理模型、选择变量以及计算高维后验。

## 2. 历史脉络

Thomas Bayes 的相关论文在他去世后由 Richard Price 整理发表，讨论从观察结果反推未知概率的问题。

Pierre-Simon Laplace 随后大幅推广“逆概率”方法，把它应用到天文学、人口统计和误差问题。现代 Bayesian inference 因此不能简单写成“Bayes 一个人创建了一整套现代统计”。

20 世纪概率论经 Kolmogorov 测度公理化后，条件概率、随机变量和期望获得严格统一基础。

## 3. 统计版本

参数 $\theta$，数据 $D$：

$$
p(\theta|D)
\mathrel{=}
\frac{p(D|\theta)p(\theta)}{p(D)}.
$$

通常写成

$$
\text{posterior}
\propto
\text{likelihood}\times\text{prior}.
$$

其中：

- prior：观察当前数据前对参数的不确定性；
- likelihood：不同参数产生当前数据的能力；
- posterior：结合数据后的更新结果；
- evidence：归一化常数，同时在模型比较中很重要。

## 4. 为什么医学检测最能体现它？

假设：

- 患病率 1%；
- 灵敏度 99%；
- 特异度 95%。

即便测试很“灵敏”，阳性后患病概率仍不是 99%。

$$
P(D|+)
\mathrel{=}
\frac{P(+|D)P(D)}
{P(+|D)P(D)+P(+|\neg D)P(\neg D)}.
$$

代入：

$$
\frac{0.99\times0.01}
{0.99\times0.01+0.05\times0.99}
\approx16.7\%.
$$

原因是基准率很低，大量健康人中的少数假阳性也会形成可观数量。

## 5. 顺序更新

Bayesian 方法天然适合连续学习。

第一批数据得到 posterior 后，它可以作为下一批数据的 prior：

$$
p(\theta|D_1,D_2)
\propto
p(D_2|\theta)p(\theta|D_1).
$$

这让“学习”成为数学上的信息累积。

## 6. 共轭先验：为什么有些 Bayes 可以手算？

若

$$
p\sim\operatorname{Beta}(\alpha,\beta),
$$

观察 Bernoulli 数据中成功 $s$ 次、失败 $f$ 次，则

$$
p|D
\sim
\operatorname{Beta}(\alpha+s,\beta+f).
$$

后验仍属于 Beta family，这叫 conjugacy。

现代复杂模型往往不再有解析后验，需要：

- MCMC；
- variational inference；
- sequential Monte Carlo；
- Laplace approximation。

## 7. 现实应用

- 医疗诊断；
- 传感器融合和机器人定位；
- A/B testing；
- 科学参数估计；
- Gaussian processes；
- Bayesian neural networks；
- 风险分析与决策；
- spam filtering 和分类。

## 8. 与机器学习的关系

监督学习常求

$$
\theta_{\text{MLE}}
\mathrel{=}
\arg\max_\theta p(D|\theta).
$$

若加入 prior：

$$
\theta_{\text{MAP}}
\mathrel{=}
\arg\max_\theta
p(D|\theta)p(\theta).
$$

许多正则化可以解释成 MAP 中的先验结构。例如高斯 prior 常对应 $L_2$ penalty。

## 9. 常见误解

**先验不等于随便猜。**  
它可以来自历史数据、物理约束、层级模型或弱信息分布。

**Bayes 不能自动消除模型错误。**  
若 likelihood 建模错了，后验也可能非常自信地错。

**Bayesian 不等于永远比 frequentist 好。**  
两套框架解决问题的哲学和工具不同，具体方法应按任务选择。

## 10. 动手实验

\`\`\`bash
python labs/07_bayes_update.py
\`\`\`

观察抛硬币数据一批批进入后，Beta posterior 如何逐渐集中。

## 参考

- MacTutor, Thomas Bayes: https://mathshistory.st-andrews.ac.uk/Biographies/Bayes/
- MacTutor, Laplace: https://mathshistory.st-andrews.ac.uk/Biographies/Laplace/
- Gelman et al., *Bayesian Data Analysis*.