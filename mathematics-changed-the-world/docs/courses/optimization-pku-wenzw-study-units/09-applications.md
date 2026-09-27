# Unit 09｜三个端到端优化应用

> **状态：三个教学合成数据项目已完成单一种子的基线与压力运行。** 本页给出来源页码、模型差异和实测失败案例；[完整运行记录](../optimization-pku-wenzw-unit09-run-log.md)与[原始 CSV](https://github.com/Jaycob-jh/math-atlas/tree/math-changed-world/mathematics-changed-the-world/labs/records/unit09)保留逐步证据。运行成功不等于现实数据验证。

来源为文再文等《最优化：建模、算法与理论》第二版[官方草稿 PDF](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/opt2.pdf)。下文先列正文印刷页码，再列 PDF 文件页码；两者相差 18 页。

## A. 稀疏重建：LASSO

**来源。** §3.2.3，书页 90–92／PDF 108–110；近端梯度 §8.1.2，384／402；FISTA §8.2，394／412。

教学脚本从 $m<n$ 的线性观测 $b=Ax^\star+\varepsilon$ 估计稀疏信号，使用高斯合成测量矩阵、列归一化和固定种子。目标是

$$\min_x \frac{1}{2m}\|Ax-b\|_2^2+\lambda\|x\|_1.$$

书中的平方损失未除以 $m$；本实验的 $\lambda=0.002$ 不能脱离损失缩放直接和书中参数比较。比较 ISTA 与 FISTA，固定 250 步。基线两法相对恢复误差均约 0.116，支持集差异为 0，proximal gradient mapping 约为 $10^{-14}$–$10^{-12}$。压力条件只使第二列近乎第一列，保留同一原始观测噪声；两法误差升至 0.655、0.692，支持集差异仍为 0。这说明支持集正确和最优性残差小均不足以保证系数幅值恢复。早期 $\lambda=0.015$ 探索的基线误差约 0.779，也记录了模型参数选择失败。代码：[项目 A](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/labs/21_optimization_sparse_recovery.py)。

## B. 二值分类：正则化 logistic regression

**来源。** §3.3，书页 93–94／PDF 111–112；SGD §8.7.1，498／516；应用 §8.7.2，505／523。

脚本在合成二分类数据上比较全批量梯度法与 SGD。标签 $y_i\in\{-1,1\}$，目标为

$$\min_{w,c}\;\frac1N\sum_{i=1}^N\log(1+e^{-y_i(x_i^Tw+c)})+\frac\lambda2\|w\|_2^2.$$

脚本采用平均损失、额外的不正则化截距，和教材模型的求和及参数约定有别。固定划分、种子及 40 epoch 后，基线测试准确率两法均为 0.842。压力条件将一列特征乘以 100：全梯度准确率降至 0.517；SGD 仍为 0.842，但测试损失约 0.707、全梯度范数约 6.24，不可视为已收敛。放大特征既改变优化几何，也改变固定 $\ell_2$ 正则项在原始特征尺度上的相对作用，因此不能仅归因于条件数。代码：[项目 B](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/labs/22_optimization_logistic.py)。

## C. 相位恢复：幅值平方观测

**来源。** §3.6，书页 100–102／PDF 118–120；实数模型见式 (3.6.4)，书页 102／PDF 120。谱初始化仅借鉴 [Candès 等的原始论文](https://arxiv.org/abs/1407.1065)思路，本脚本并非该论文理论算法的复现。

脚本在实数高斯测量下生成 $b_i=(a_i^Tx^\star)^2+\varepsilon_i$，优化

$$\min_x\;\frac{1}{4m}\sum_i\bigl((a_i^Tx)^2-b_i\bigr)^2.$$

教材式 (3.6.4) 使用无噪声强度 $b_i^2$；脚本在**平方观测值**上加高斯噪声，并另行缩放目标。比较谱初始化和随机初始化后的同一回溯梯度下降。由于 $x^\star$ 与 $-x^\star$ 不可区分，报告符号不变误差。基线 250 步后两者均约 0.00216。压力条件同时将样本数 240 降至 24、噪声标准差 0.02 升至 0.3；谱/随机误差分别为 1.048/1.075，均未恢复真值。随机初始化的目标值反而更低（0.0553 对 0.0676），表明目标值和真值误差不可混同；这次联合压力不能分离欠采样与噪声的贡献。代码：[项目 C](https://github.com/Jaycob-jh/math-atlas/blob/math-changed-world/mathematics-changed-the-world/labs/23_optimization_phase_retrieval.py)。

## 证据范围

六次运行均使用种子 20260927，Python 3.12.14、NumPy 2.3.5，退出码均为 0。原始 CSV、命令、脚本与 CSV 哈希以及逐方法末行见[运行记录](../optimization-pku-wenzw-unit09-run-log.md)。这些是单一种子、固定预算的合成数据观察；尚无跨种子不确定性估计或真实数据外部验证。
