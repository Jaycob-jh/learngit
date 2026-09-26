# 北大最优化体系：系统学习路线

> 目标：把教材、电子讲义、算法程序和本知识库已有数学专题组合成一条“定义 → 理论 → 算法 → 实验 → 应用”的可执行路线。
>
> 资源总入口：[北大文再文最优化学习体系](optimization-pku-wenzw.md) · [电子讲义索引](optimization-pku-wenzw-lectures.md)

## 学习原则

这条路线不按 PDF 文件名机械前进，而按知识依赖组织。每个单元都应完成四种产出：

1. **概念卡**：定义、条件、反例；
2. **推导卡**：核心公式为什么成立、条件在哪里使用；
3. **算法卡**：更新式、停止准则、收敛条件与计算代价；
4. **实验卡**：正常案例 + 故意破坏一个条件的失败案例。

教材第二版的整体结构可以概括为：

```text
最优化简介
→ 基础知识
→ 优化建模
→ 典型优化问题
→ 最优性理论
→ 无约束优化算法
→ 约束优化算法
→ 复合优化算法
→ 附录：数学 / 数值代数 / 概率基础
```

第二版另增加流形约束优化和半光滑 Newton，因此它们作为后段高级单元处理。

## Unit 01｜基础语言：问题、凸性与数值代数

**资源**：01 简介、02 凸集、03 凸函数、04 数值代数基础；教材第 1–2 章与附录 B.2。

**目标**：写出一般优化问题；区分约束/无约束、凸/非凸、确定性/随机；掌握范数、梯度、Hessian、凸集、凸函数的一阶/二阶判别；知道线性方程组、矩阵分解、特征值/SVD 为什么会进入优化算法实现。

进入：[Unit 01 学习单元](optimization-pku-wenzw-study-units/01-foundations.md)

实验：`labs/13_optimization_convexity.py`

## Unit 02｜建模：把现实问题写成优化问题

**资源**：05 优化建模、06 典型优化问题、教材第 3–4 章。

目标：从现实描述提取变量、目标函数、约束、正则化/松弛/等价变换和问题类别。重点模型包括 least squares、LASSO、logistic regression、SVM、低秩恢复、相位恢复、PCA、TV、小波和随机优化。

进入：[Unit 02 学习单元](optimization-pku-wenzw-study-units/02-modeling.md)

实验：`labs/14_optimization_modeling.py`

## Unit 03｜最优性：什么叫“解对了”

**资源**：凸优化最优性理论、非凸优化最优性理论、教材第 5 章。

目标：存在性与唯一性；一阶/二阶必要与充分条件；对偶；KKT 与约束品性；严格区分局部最优、全局最优和驻点。

进入：[Unit 03 学习单元](optimization-pku-wenzw-study-units/03-optimality.md)

实验：`labs/15_optimization_optimality.py`

## Unit 04｜无约束算法：从梯度到信赖域

**资源**：梯度下降、次梯度及次梯度算法、Newton、拟 Newton、信赖域、非线性最小二乘、教材第 6 章。

统一视角：局部模型 → 搜索方向 → 全局化策略 → 收敛速度。比较 gradient、BB、Newton/modified Newton、BFGS/L-BFGS、trust-region、Gauss-Newton、Levenberg-Marquardt。

进入：[Unit 04 学习单元](optimization-pku-wenzw-study-units/04-unconstrained.md)

实验：`labs/16_optimization_unconstrained.py`

## Unit 05｜约束优化：罚函数、ALM 与内点法

**资源**：罚函数、增广 Lagrangian、线性规划内点法、教材第 7 章。

目标：理解把约束罚进目标、乘子与罚参数联合控制约束违反、从可行域内部沿中心路径逼近边界最优解这三类策略。

## Unit 06｜复合优化：proximal、加速、分裂

**资源**：近似点算子、近似点梯度、Nesterov/FISTA、近似点算法、BCD、对偶算法、ADMM、教材第 8 章。

核心结构：

$$
\min_x f(x)+g(x).
$$

目标：理解 prox、变量分裂和原始—对偶结构如何把复合问题转化为可计算步骤。

## Unit 07｜随机与非光滑高级算法

**资源**：随机优化、半光滑 Newton、第二版相关章节。

目标：SGD 与有限和/期望目标；方差减小；广义导数与半光滑 Newton；比较一阶大规模方法和高精度局部方法。

## Unit 08｜流形约束优化

教材第二版已经包含流形约束优化；当前电子讲义清单暂未单列对应 PDF。

现有代码入口：

- ARNT：https://github.com/optsuite/ARNT
- OptM：https://github.com/optsuite/OptM

目标：从正交约束 $X^TX=I$ 出发，理解切空间、Riemannian gradient、retraction、向量传输以及一阶/二阶方法。

## Unit 09｜应用专题

从压缩感知、低秩恢复、相位恢复、图像 TV/小波、logistic regression/SVM、随机优化/深度学习、强化学习、最优传输中至少完成三个端到端项目。

每个项目必须回答：为什么选这个模型？为什么选这个算法？如果关键假设不满足，会怎样？

## Unit 10｜形式化验证（可选）

进入 Optlib / ReasLab / Lean4 路线，把已经掌握的优化理论转化成机器可检查对象。优先顺序：凸集/凸函数 → 一阶最优性 → 梯度下降 → proximal/Nesterov → BCD/ADMM → 更复杂的收敛证明。

## 完成标准

一项内容只有同时满足下列条件才标记“学完”：

- 能给出定义及至少一个非例；
- 能解释结论使用了哪些假设；
- 能手推一个简单问题；
- 能运行或自己写出一个数值实验；
- 能解释失败案例；
- 能把它连接到至少一个现实模型；
- 能说清它和前后算法的区别。
