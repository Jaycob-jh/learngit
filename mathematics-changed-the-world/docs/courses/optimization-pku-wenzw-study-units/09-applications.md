# Unit 09｜三个端到端优化应用

> **状态：模型与脚本草稿，全部未运行。** 依据课程总览登记的压缩感知、相位恢复、logistic regression 应用方向，结合 [Unit 02 建模](02-modeling.md)、[Unit 06 复合优化](06-composite.md)和 [Unit 07 随机优化](07-stochastic-nonsmooth.md)组织。此处的合成数据与失败情形均是实验设计，不是已取得的结果；现有资料尚未逐页审读。运行时应按[记录模板](../optimization-pku-wenzw-unit09-run-log.md)保存实际输出。

每个项目统一报告：数据产生规则、随机种子、目标函数、算法与基线、停止准则、目标值或最优性残差、重建/分类误差、迭代次数、wall-clock、失败案例及局限。不能只凭目标值判断现实任务质量。

## A. 稀疏重建：LASSO

**问题。** 从 $m<n$ 的线性观测 $b=Ax^\star+\varepsilon$ 估计稀疏信号。教学脚本生成高斯测量矩阵并归一化列，真实向量只含少量非零位置。模型为

$$\min_x \frac{1}{2m}\|Ax-b\|_2^2+\lambda\|x\|_1.$$

数据项对应平方噪声假设，$\ell_1$ 是稀疏结构的凸松弛。比较 ISTA 与 FISTA，并记录目标值、proximal gradient mapping、相对重建误差及支持集误差。若噪声分布显著偏离平方损失假设或列高度相关，支持集可能不稳定；脚本通过提高列相关性设计失败条件，但实际结果待运行。代码：[项目 A](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/labs/21_optimization_sparse_recovery.py)。

## B. 二值分类：正则化 logistic regression

**问题。** 在合成二分类数据上比较全批量梯度法与 SGD。令标签 $y_i\in\{-1,1\}$，截距不正则化，模型为

$$\min_{w,c}\;\frac1N\sum_{i=1}^N\log(1+e^{-y_i(x_i^Tw+c)})+\frac\lambda2\|w\|_2^2.$$

该目标在参数上凸；有正则项不代表截距方向也强凸。报告训练/测试损失、准确率及目标进展，保留固定划分与随机种子。两种算法必须在相同数据上比较；SGD 的每步成本小但噪声大，不能仅看迭代轮数。失败条件设计为特征尺度失衡并保持未标准化；需在运行后检查其影响，不能预先声称失败已发生。代码：[项目 B](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/labs/22_optimization_logistic.py)。

## C. 相位恢复：幅值平方观测

**问题。** 给定 $b_i=(a_i^Tx^\star)^2+\varepsilon_i$，在不观测符号的条件下恢复 $x^\star$。使用

$$\min_x\;\frac{1}{4m}\sum_i\bigl((a_i^Tx)^2-b_i\bigr)^2.$$

这是**非凸**模型；$x^\star$ 与 $-x^\star$ 无法由这种观测区分，因此误差按符号等价类计算。比较谱初始化后的梯度下降与随机初始化后的同一算法；两者使用同一目标、梯度和步长，比较的是初始化。记录观测残差、符号不变恢复误差与目标。失败案例为样本不足或高噪声下的随机初始化，实际表现须运行后记录。代码：[项目 C](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/labs/23_optimization_phase_retrieval.py)。

## 资料与断言边界

| 项目 | 当前参考逻辑 | 待阅读与验证 |
|---|---|---|
| A | 课程的稀疏恢复/复合优化目录；Unit 02、06 的 LASSO 推导 | 教材具体章节/页码；两算法与失败条件的真实输出 |
| B | 课程的 logistic regression 与随机优化目录；Unit 07 的有限和模型 | 教材/讲义的模型约定；特征尺度、停止准则与泛化结果 |
| C | 课程的相位恢复应用目录与非凸最优性框架 | 来源公式与噪声假设；初始化策略、局部极值及恢复误差 |

三个脚本与本页是**可供审阅的实施稿**。只有实际运行并填写日志后，才可称为完成端到端实验；不得把合成数据实验推广为真实应用效果。
