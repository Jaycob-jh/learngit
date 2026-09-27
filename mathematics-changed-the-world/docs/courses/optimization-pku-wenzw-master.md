# 北京大学文再文最优化资源体系：单文件完整总览（已完成 + 待完成）

> 仓库：Jaycob-jh/math-atlas（原 Jaycob-jh/learngit）
>
> 分支：math-changed-world
>
> 路径：mathematics-changed-the-world/docs/courses/optimization-pku-wenzw-master.md
>
> 整合时间：2026-09-27（UTC+8）
>
> 原总览基线提交：bde35947006ea65ce2902830318624ae24869e6d；Unit 06 草稿基于后续 a2edd95976e17072809974c9ec7fdfc92af22f39


## 1. 文档定位与证据规则

这是一份**单文件总览**：把 Unit 01–06、Unit 07–10 的待审实施稿、电子讲义索引、教材/课程/代码/形式化资源、实验、验收标准和维护规则放在同一份 Markdown 中。Unit 07–10 的独立页面已建立；新脚本未运行，来源未逐页核对。

### 1.1 当前权威来源

- 课程资源总页：docs/courses/optimization-pku-wenzw.md
- 电子讲义索引：docs/courses/optimization-pku-wenzw-lectures.md
- 系统路线：docs/courses/optimization-pku-wenzw-study-roadmap.md
- 已完成 Unit：optimization-pku-wenzw-study-units/01 至 05
- 第二版教材：用户提供的 opt2.pdf，仅用于结构、版本和内容校核，不重新发布完整 PDF。

### 1.2 关键版本事实

第二版《最优化：建模、算法与理论》前言署于 **2025 年 2 月**，已确认新增：

- 流形约束优化；
- 半光滑 Newton；
- 更完善的代码整理、网页、习题答案和电子讲义。

### 1.3 访问状态规则

faculty.bicmr.pku.edu.cn 在自动抓取通道可能出现 502 / timeout。对于用户已经确认可访问的具体 optbook 讲义 URL：

- 只记录“自动抓取不可达”；
- 不判定资源不存在；
- 不删除 URL；
- 不根据命名规律猜新文件。

### 1.4 technical-docs 保真规则

继续遵循 Jaycob-jh/editorial-agent-framework：

- Fidelity before fluency；
- URL、ISBN、课程号、学分、版本、协助准备者严格保护；
- 必要/充分/充要不能互换；
- 局部/全局结论不能互换；
- 理论前提不得在改写时消失；
- 来源不可读不能改写成来源不存在；
- 所有待发现资源必须真实页面确认。



## 2. 资源总入口

### 2.1 教材

**详细版**

- 刘浩洋、户将、李勇锋、文再文：《最优化：建模、算法与理论》
- 高等教育出版社
- ISBN：9787040550351

**简明版**

- 刘浩洋、户将、李勇锋、文再文：《最优化计算方法》
- ISBN：978-7-04-055841-8

**更新/进阶教材**

- 文再文、袁亚湘：《最优化方法与理论》
- ISBN：978-7-04-062561-5
- 高等教育出版社页面记录出版时间：2025-01-16
- 版次：1
- 北大 101 计划入口：https://math101.pku.edu.cn/hxjc/qb/3489f4fc70974d0da96ce949939fd3b8.htm

### 2.2 北京大学课程

**《最优化方法》**

- https://math.pku.edu.cn/bks/sykc/148761.htm
- 课程号：00130630
- 秋季
- 学分：3
- 先修：数学分析、数值代数
- 华文慕课：https://www.chinesemooc.org/web/course_detail.php?courseid=5063

**《大数据分析中的算法》**

- https://math.pku.edu.cn/bks/sykc/148668.htm
- 课程号：00136720
- 秋季
- 学分：3
- 先修：数学分析、数值代数
- 华文慕课：https://www.chinesemooc.org/web/course_detail.php?courseid=4974

### 2.3 optbook 入口

- 主入口：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook.html
- 讲义目录：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/contents/contents.html
- 程序页：http://bicmr.pku.edu.cn/~wenzw/optbook/pages/index.html

### 2.4 已独立登记的程序/演示页

- SGD：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/sgd.html
- Adam：https://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/Adam.html
- FISTA / Nesterov LASSO：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_proxg/LASSO_Nesterov_inn.html
- ADMM demo：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_admm/demo_admm.html

### 2.5 代码与形式化

- optsuite：https://github.com/optsuite
- Optlib：https://github.com/optsuite/optlib
- ARNT：https://github.com/optsuite/ARNT
- OptM：https://github.com/optsuite/OptM
- ReasLab：https://reaslab.io/
- ReasBook：https://github.com/optpku/ReasBook
- M2F：https://github.com/optsuite/M2F
- SITA：https://github.com/chenyili0818/SITA
- lean-tools-mcp：https://github.com/optsuite/lean-tools-mcp
- CAM-Bench：https://github.com/optpku/CAM-Bench

ARNT / OptM 目前只作为流形优化代码证据；不能据此推出独立“流形约束优化电子讲义 PDF”已经发布。


## 3. 全路线状态

| 单元 | 主题 | 状态 | 讲义映射 | 教材映射 | 实验/产出 | 代表提交 |
|---|---|---|---|---|---|---|
| Unit 01 | 基础语言：问题、凸性与数值代数 | **已完成** | 01–04 | 第 1–2 章 + 附录 B.2 | labs/13_optimization_convexity.py | 017b77917dd621b29a083dc654e51843a231fbfe |
| Unit 02 | 优化建模与典型优化问题 | **已完成** | 05–06 | 第 3–4 章 | labs/14_optimization_modeling.py | 2b0ae163c5ba8436c9456d2dba581ab1a31bc233 |
| Unit 03 | 最优性理论 | **已完成** | 07–08 | 第 5 章 | labs/15_optimization_optimality.py | 2c09b114734d544aba3fa08509dc7b0bf49f1155 |
| Unit 04 | 无约束优化算法 | **已完成** | 09、12–15 | 第 6 章（6.3 延后） | labs/16_optimization_unconstrained.py | 209314c601e162979ebe1f724a10e9757e0c8d47 |
| Unit 05 | 约束优化算法 | **已完成** | 16–18 | 第 7.1–7.3 | labs/17_optimization_constrained.py | bde35947006ea65ce2902830318624ae24869e6d |
| Unit 06 | 复合优化：proximal、加速、分裂 | **草稿待审** | 19–25 | 第 8.1–8.6 | labs/18_optimization_composite.py | 038205cdb91b20fa8e3a7cb9e611a24ee40f4c0a |
| Unit 07 | 随机与非光滑高级算法 | **页面/脚本待审，未运行** | 10–11、26–27 | 第 6.3、8.7–8.8 | [独立页](optimization-pku-wenzw-study-units/07-stochastic-nonsmooth.md)、labs/19_optimization_stochastic_nonsmooth.py | 本批待提交 |
| Unit 08 | 流形约束优化 | **页面/脚本待审，未运行** | 当前无单列流形 PDF | 第 7.4 | [独立页](optimization-pku-wenzw-study-units/08-manifold.md)、labs/20_optimization_manifold.py | 本批待提交 |
| Unit 09 | 应用专题 | **三项目实施稿，未运行** | 跨讲义 | 第 3–4 章 + 算法章节 | [独立页](optimization-pku-wenzw-study-units/09-applications.md)、labs/21–23 | 本批待提交 |
| Unit 10 | Lean4 形式化验证 | **学习页待审，未编译** | Optlib/ReasLab/ReasBook | 跨章节 | [独立页](optimization-pku-wenzw-study-units/10-formalization.md) | 本批待提交 |

### 3.1 当前总体进度

- **Unit 01–05：已落库文档 + 配套 Python 实验。**
- **Unit 06：独立文档与实验已合并；来源复核仍待完成。**
- **Unit 07–10：独立页面已写；Unit 07–09 的五个脚本尚未运行，Unit 10 尚无已编译证明。**
- 已登记电子讲义：**27 个主题 / 33 个 PDF URL**。
- 第二版新增半光滑 Newton：已有独立讲义。
- 第二版新增流形约束优化：教材章节已确认，但当前讲义索引**尚无独立 PDF**。



## 4. 电子讲义完整索引

> 来源状态（2026-09-26）：本页依据用户提供并确认可访问的 optbook 讲义清单建立。ChatGPT 当前网页抓取通道访问 `faculty.bicmr.pku.edu.cn` 时仍可能得到 502 或 timeout，因此**工具侧抓取失败不等同于讲义失效**。
>
> 上位课程页：[北大文再文最优化学习体系](optimization-pku-wenzw.md)
>
> 目录入口：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/contents/contents.html

### 1. 讲义总表

当前收录 **27 个教学主题、33 个 PDF 讲义链接**。同一主题若有“北大课程版 / 简略版 / 合并版”，均保留，不互相覆盖。

| # | 主题 | 协助准备 | 讲义 |
|---:|---|---|---|
| 01 | 简介 | 邓展望 | [01-opt-dzw.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/01-opt-dzw.pdf) |
| 02 | 凸集 | 丁思哲 | [02-convex-set.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/02-convex-set.pdf) |
| 03 | 凸函数 | 华奕轩 | [03_functions_newhyx.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/03_functions_newhyx.pdf) |
| 04 | 数值代数基础 | 张轩熙 | [04-num_lin_alg-newl.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/04-num_lin_alg-newl.pdf) |
| 05 | 优化建模 | 华奕轩 | [05-lect1-model.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/05-lect1-model.pdf) |
| 06 | 典型优化问题 | 邓展望 | [讲义](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/06-opt-dzw.pdf) · [北大课程版](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/06-opt-dzw-pku.pdf) |
| 07 | 凸优化最优性理论 | 谢中林 | [07-lect-theory1.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/07-lect-theory1.pdf) |
| 08 | 非凸优化最优性理论 | 谢中林 | [07-lect-theory2.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/07-lect-theory2.pdf) |
| 09 | 梯度下降算法 | 谢中林 | [08-lect-gradient.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/08-lect-gradient.pdf) |
| 10 | 次梯度 | 朱桢源 | [09-lect-sg.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/09-lect-sg.pdf) |
| 11 | 次梯度算法 | 朱桢源 | [10-lect-sgm.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/10-lect-sgm.pdf) · [次梯度+算法合并版](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/09-lect-sg-meth.pdf) |
| 12 | 牛顿类算法 | 陈乐恒、丁思哲 | [11-lect-newton.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/11-lect-newton.pdf) |
| 13 | 信赖域算法 | 邓展望 | [13_trustregion_newdzw.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/13_trustregion_newdzw.pdf) · [牛顿法+信赖域合并版](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/lect-newton-TR.pdf) |
| 14 | 拟牛顿算法 | 丁思哲 | [12-lect-QN.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/12-lect-QN.pdf) |
| 15 | 非线性最小二乘问题 | 张轩熙 | [14-lsp-new-zxx.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/14-lsp-new-zxx.pdf) |
| 16 | 罚函数法 | 陈乐恒、邓展望 | [15-lect-penalty.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/15-lect-penalty.pdf) |
| 17 | 增广拉格朗日函数法 | 陈乐恒、丁思哲 | [16-lect-alm.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/16-lect-alm.pdf) · [简略版](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/16-lect-alm-pku.pdf) |
| 18 | 线性规划内点法 | 谢中林、张轩熙 | [17-lp_ipm-new-zxx-xzl.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/17-lp_ipm-new-zxx-xzl.pdf) |
| 19 | 近似点算子 | 陈乐恒、朱桢源 | [18-lect-prox_map.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/18-lect-prox_map.pdf) |
| 20 | 近似点梯度算法 | 陈乐恒、朱桢源 | [19-lect-proxg.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/19-lect-proxg.pdf) |
| 21 | Nesterov 加速算法 | 李煦恒 | [20-lect-nesterov-ch.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/20-lect-nesterov-ch.pdf) |
| 22 | 近似点算法 | 陈乐恒、邓展望 | [21-lect-prox_point.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/21-lect-prox_point.pdf) |
| 23 | 分块坐标下降法 | 朱桢源 | [22-lect-BCD.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/22-lect-BCD.pdf) · [简略版](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/22-lect-BCD-pku.pdf) |
| 24 | 对偶算法 | 朱桢源 | [23-lect-DualAlgo.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/23-lect-DualAlgo.pdf) |
| 25 | 交替方向乘子法（ADMM） | 华奕轩 | [24-lect-admm-chhyx.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/24-lect-admm-chhyx.pdf) |
| 26 | 随机优化算法 | 李煦恒 | [25-lect-sto-ch.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/25-lect-sto-ch.pdf) |
| 27 | 半光滑牛顿算法 | 李勇锋、邓展望 | [slides-ssm-dzw.pdf](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/slides-ssm-dzw.pdf) · [简略版](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/lect/slides-ssm-dzw-pku.pdf) |

### 2. 与教材章节对齐

建议按教材的知识结构而不是文件编号机械学习。

#### A. 预备知识与凸分析

- 简介；
- 凸集；
- 凸函数；
- 数值代数基础。

对应教材：第一章、第二章与附录 B。

#### B. 建模与问题分类

- 优化建模；
- 典型优化问题。

对应教材：第三章“优化建模”、第四章“典型优化问题”。

#### C. 最优性理论

- 凸优化最优性理论；
- 非凸优化最优性理论。

对应教材：第五章。

#### D. 无约束光滑 / 非光滑算法

- 梯度下降；
- 次梯度与次梯度算法；
- Newton；
- 拟 Newton；
- 信赖域；
- 非线性最小二乘。

对应教材：第六章。

#### E. 约束优化

- 罚函数；
- 增广 Lagrangian；
- 线性规划内点法。

对应教材：第七章。

#### F. 复合、大规模与随机优化

- 近似点算子；
- 近似点梯度；
- Nesterov / FISTA；
- 近似点算法；
- 分块坐标下降；
- 对偶算法；
- ADMM；
- 随机优化；
- 半光滑 Newton。

对应教材：第八章及第二版扩展内容。

### 3. 第二版教材对齐提醒

本次用户提供的《最优化：建模、算法与理论》第二版 PDF 前言署于 **2025 年 2 月**。第二版明确说明：

- 新增**流形约束优化**；
- 新增**半光滑牛顿算法**；
- 完善代码整理、网页、习题答案与电子教案讲义。

第二版目录还把“流形约束优化算法”列为第 7.4 节，把“半光滑牛顿算法”列为第 8.8 节。

当前这批 27 个讲义主题已经明确包含半光滑 Newton，但**没有单独列出流形约束优化 PDF**。因此自动巡检应把“流形约束优化电子讲义”作为明确的待发现项，而不是自行猜测文件名。

### 4. 推荐学习顺序

#### 第一轮：建立可用框架

```text
简介
→ 凸集
→ 凸函数
→ 数值代数
→ 优化建模
→ 典型优化问题
→ 凸优化最优性理论
→ 梯度下降
→ Newton / 拟 Newton / 信赖域
```

#### 第二轮：非光滑与复合优化

```text
次梯度
→ 次梯度算法
→ 近似点算子
→ 近似点梯度
→ Nesterov / FISTA
→ 近似点算法
→ BCD
→ 对偶
→ ADMM
```

#### 第三轮：约束、随机与高级算法

```text
非凸最优性
→ 非线性最小二乘
→ 罚函数
→ 增广 Lagrangian
→ 线性规划内点法
→ 随机优化
→ 半光滑 Newton
→ （第二版补充）流形约束优化
```

### 5. 每节学习模板

每个讲义不只“看完”，至少产出：

1. **问题类**：目标函数与约束长什么样；
2. **核心假设**：凸性、光滑性、Lipschitz、强凸、约束品性等；
3. **算法更新式**：写清每一步实际计算；
4. **收敛结论**：结论成立所需条件；
5. **复杂度 / 局部速度**：若讲义给出则记录；
6. **一个数值实验**：Python/NumPy 实现；
7. **一个失败案例**：破坏关键假设后观察算法表现；
8. **与教材页码/章节对应**；
9. **与本知识库已有专题链接**。




## 5. 已完成 Unit 01–05：完整内容

下面直接整合当前仓库已经完成的学习单元。为避免“总览”和原单元发生语义漂移，本节以仓库现有 Unit 文档为正文来源，仅提升标题层级。




---

## Unit 01｜最优化的基础语言：问题、凸性与数值代数

> 对应电子讲义：01 简介、02 凸集、03 凸函数、04 数值代数基础。
>
> 对应教材：第 1 章“最优化简介”、第 2 章“基础知识”以及附录 B.2“数值代数基础”。
>
> 本页是学习导引与练习设计，不复刻教材或讲义正文。

### 1. 学完后应该会什么？

完成本单元后，应当能：

1. 把一个优化问题写成
   $$
   \min_x f(x),\qquad x\in X;
   $$
2. 说明目标函数、决策变量、可行域分别代表什么；
3. 区分约束/无约束、连续/离散、凸/非凸、确定性/随机问题；
4. 用定义判断简单集合是否凸；
5. 用定义、一阶条件或 Hessian 判断常见函数的凸性；
6. 解释为什么矩阵分解、线性方程组、特征值和 SVD 是优化算法的计算底座；
7. 识别“数学上收敛”与“数值上算得稳定”不是同一件事。

### 2. 第一层：优化问题到底是什么？

一般形式：

$$
\min_{x\in X} f(x).
$$

其中：

- $x$：决策变量；
- $f(x)$：目标函数；
- $X$：可行域。

学习时不要只盯公式，要反复问：

- 谁是变量？
- 什么东西越小/越大越好？
- 什么条件不能违反？
- 这是模型本身的限制，还是为了让算法更容易而人为加入的结构？

#### 快速分类

| 维度 | 两侧 |
|---|---|
| 是否有约束 | unconstrained / constrained |
| 变量空间 | continuous / discrete |
| 几何性质 | convex / nonconvex |
| 信息来源 | deterministic / stochastic |
| 光滑性 | smooth / nonsmooth |

同一个现实问题经过不同建模，可能落入完全不同的类别，因此问题分类本身就是算法选择的一部分。

### 3. 第二层：凸集

集合 $C$ 是凸集，如果对任意 $x,y\in C$ 与 $0\le\theta\le1$，

$$
\theta x+(1-\theta)y\in C.
$$

几何直觉：集合中任意两点之间的整条线段仍留在集合内。

#### 必会例子

通常是凸集：

- 仿射空间；
- 半空间；
- 范数球；
- 多面体；
- 半正定锥。

典型非凸结构：

- 两个彼此分离区域的并集；
- 单位球面 $\{x:\|x\|_2=1\}$；
- 一般整数点集合。

#### 自检

不要把“边界弯曲”与“非凸”等同。圆盘是凸的，圆周不是凸的。

### 4. 第三层：凸函数

函数 $f$ 在凸定义域上是凸函数，如果

$$
f(\theta x+(1-\theta)y)
\le
\theta f(x)+(1-\theta)f(y).
$$

直观上，弦在函数图像之上。

#### 可微函数的一阶判别

对可微凸函数，

$$
f(y)\ge f(x)+\nabla f(x)^T(y-x).
$$

因此切平面是一个全局下界，这也是许多一阶算法能够工作的几何基础。

#### 二阶判别

在相应可微性与凸定义域条件下，

$$
\nabla^2 f(x)\succeq 0
$$

是凸性的核心二阶判据。

需要特别记住：Hessian 判据有前提。不要把“某一点 Hessian 半正定”误写成“函数全局凸”。

### 5. 第四层：范数、梯度、Hessian

#### 范数

范数用于表达“大小”或“距离尺度”。优化中高频出现：

- $\ell_1$：稀疏建模；
- $\ell_2$：欧氏几何、least squares；
- $\ell_\infty$：最大偏差；
- Frobenius norm：矩阵误差；
- nuclear norm：低秩凸松弛。

#### 梯度

梯度回答：在当前点附近，哪个方向让函数增长最快？

负梯度因此给出最基本的下降方向。

#### Hessian

Hessian 描述局部曲率。它同时进入：

- 凸性判断；
- Newton 法；
- conditioning；
- 二阶 Taylor 模型。

这也是本知识库 [Taylor 展开](../core/02-taylor.md) 与 [凸优化](../branches/19-convex-optimization.md) 的直接连接点。

### 6. 第五层：为什么要学数值代数？

优化算法的“数学公式”最终要变成矩阵计算。

#### 线性方程组

Newton 类算法的核心步骤常形如

$$
H_k p_k=-g_k.
$$

这里不是“求逆矩阵”三个字就结束了：实际计算需要选择合适的线性系统求解方法。

#### 矩阵分解

需要建立以下基本对应：

- LU：一般线性系统；
- Cholesky：对称正定系统；
- QR：least squares；
- eigen-decomposition：谱结构；
- SVD：秩、伪逆、低秩近似、conditioning。

#### 条件数

同一个数学问题，数值条件差时可能出现：

- 小输入误差被放大；
- 迭代显著变慢；
- 理论上合理的停止准则在浮点计算中表现不佳。

所以优化学习必须同时问：

> 这个算法收敛吗？

以及：

> 这个线性代数步骤算得稳吗？

### 7. 本单元实验

运行：

```bash
python labs/13_optimization_convexity.py
```

实验包含两个部分：

1. 对 PSD 二次函数与不定二次函数随机检查凸性不等式；
2. 比较不同条件数二次问题上的梯度下降收敛。

实验不是凸性的证明。它的用途是把“凸性”和“conditioning”变成可观察现象。

#### 故意破坏条件

至少改一次：

- 把 PSD 矩阵改成含负特征值；
- 把梯度下降步长改大到超过稳定范围；
- 把条件数从 $10$ 提高到 $10^4$。

观察“理论条件变化 → 数值行为变化”。

### 8. 练习

#### 练习 1｜分类

分别判断 least squares、LASSO、0-1 整数规划、神经网络训练属于哪些类别。不要只写“凸/非凸”，至少从三个分类维度回答。

#### 练习 2｜凸集

证明半空间

$$
C=\{x:a^Tx\le b\}
$$

是凸集。

#### 练习 3｜非例

证明单位球面

$$
S=\{x:\|x\|_2=1\}
$$

一般不是凸集。

#### 练习 4｜一阶条件

对

$$
f(x)=\frac12 x^TQx+b^Tx+c
$$

计算梯度，并说明 $Q\succeq0$ 时一阶凸性条件为什么成立。

#### 练习 5｜数值代数选择

给出以下任务更自然的分解/工具，并解释原因：

- 对称正定 Newton 系统；
- 过定线性 least-squares；
- 低秩矩阵近似。

#### 练习 6｜概念边界

解释下面两句话为什么不同：

1. “这个算法理论上收敛。”
2. “这个实现数值稳定而且收敛得快。”

### 9. 完成检查

能不看资料回答以下问题，才进入 Unit 02：

- 什么是可行域？
- 凸集和仿射集有什么关系？
- 可微凸函数的一阶条件是什么？
- Hessian 半正定的结论需要哪些限定？
- 为什么 LASSO 常出现 $\ell_1$？
- 为什么 Newton 法离不开数值线性代数？
- condition number 对优化计算意味着什么？

下一单元：[Unit 02｜优化建模与典型问题](optimization-pku-wenzw-study-units/02-modeling.md)

---

## Unit 02｜优化建模与典型优化问题

> 对应电子讲义：05 优化建模、06 典型优化问题。
>
> 对应教材：第 3 章“优化建模”、第 4 章“典型优化问题”。
>
> 本页依据教材的建模框架重新组织为学习单元，不复刻教材正文。

### 1. 本单元的核心问题

Unit 01 解决“什么是优化问题、什么是凸性”。Unit 02 要回答更实际的问题：

> 一个现实问题，怎样变成一个值得求解的优化模型？

教材把建模看成从现实需求到数学对象的过程。真正需要决定的不是“套哪个公式”，而是：

1. 决策变量是什么；
2. 什么量应该被最小化或最大化；
3. 哪些条件必须满足；
4. 是否需要正则化、松弛或变量变换；
5. 得到的模型属于哪一类优化问题；
6. 这种模型是否保留了原问题真正重要的结构。

### 2. 建模语法

把一个模型拆成四层：

```text
现实问题
→ 决策变量
→ 目标函数
→ 可行域 / 约束
→ 问题类别
```

一个常见形式是

$$
\min_x \; L(x)+\lambda R(x)
\quad
\text{s.t. }x\in X.
$$

其中：

- $L(x)$：数据误差、代价、负收益或其他任务损失；
- $R(x)$：先验结构或正则项；
- $\lambda$：平衡任务拟合与结构偏好的参数；
- $X$：物理、几何、逻辑或资源约束。

学习任何模型时都要逐项解释这四个部分，而不是只记最终公式。

### 3. 目标函数的六种常见设计思路

教材第 3.1 节依次讨论了多种目标函数设计方式。

#### 3.1 最小二乘

当观测关系近似为

$$
b_i=\phi_i(x)+\varepsilon_i,
$$

最小二乘模型为

$$
\min_x \sum_i \bigl(b_i-\phi_i(x)\bigr)^2.
$$

关键点不是“平方”本身，而是你选择了 $\ell_2$ 型误差度量。

如果换成

$$
\sum_i |b_i-\phi_i(x)|,
$$

或者

$$
\max_i |b_i-\phi_i(x)|,
$$

得到的是不同的建模假设与不同的问题结构。

#### 3.2 正则化

正则化把“希望解具有某种结构”写进目标函数。

典型例子：

$$
\frac12\|Ax-b\|_2^2+\mu\|x\|_2^2
$$

偏向较小的参数范数；而

$$
\frac12\|Ax-b\|_2^2+\mu\|x\|_1
$$

对应 LASSO，利用 $\ell_1$ 项鼓励稀疏结构。

对于矩阵变量，核范数常用于低秩结构的凸松弛。

#### 3.3 最大似然估计

当数据被认为来自参数化概率模型 $p(a;x)$ 时，可通过最大化似然或对数似然估计参数。

教材明确给出一个重要的条件化关系：

> 在线性回归中，当误差假设为高斯白噪声时，最小二乘解与最大似然解对应。

这个结论依赖噪声模型，不能无条件推广为“最小二乘总是最大似然”。

#### 3.4 代价、损失与收益

运筹、机器学习和强化学习中，目标函数常直接来自：

- cost；
- loss；
- reward。

这类模型最重要的是确认“目标函数数值变好”是否真的等价于现实任务变好。

#### 3.5 泛函与变分

物理和工程中的能量极小化问题常首先定义在函数空间上，再通过离散化转化为有限维优化问题。

因此“离散化”不只是数值实现细节：不同离散方式可能产生不同的有限维目标函数。

#### 3.6 松弛

原问题难以求解时，可以用更容易处理的对象替代困难结构。

教材的典型例子包括：

- $\ell_0 \rightarrow \ell_1$；
- rank $\rightarrow$ nuclear norm。

必须保留的边界是：

> 松弛后的问题一般不与原问题自动等价；等价或恢复原解通常需要额外条件。

这条规则对后面的稀疏恢复、低秩恢复和 phase lift 都很重要。

### 4. 约束的三种来源

#### 4.1 问题本身的物理或结构性质

例如：

- 非负性；
- 预算/资源限制；
- 正交性；
- 微分方程约束；
- 正定/半正定约束。

这类约束来自问题本身，不能为了算法方便随意删除。

#### 4.2 等价转换

通过引入辅助变量，把一个复杂表达拆开。

例如

$$
\min_x h(x)+r(x)
$$

可引入 $y$ 与约束 $x=y$，写成

$$
\min_{x,y} h(x)+r(y)
\quad
\text{s.t. }x=y.
$$

后面的 ADMM 就会大量使用这种结构。

#### 4.3 约束松弛

把难约束替换为更容易处理、但可行域更大的约束。

此时必须问：

- 新可行域扩大了多少？
- 是否丢失关键结构？
- 松弛解怎样映射回原问题？

### 5. 教材中的模型地图

教材第 3 章把建模方法放进多类实际问题。

| 模型 | 主要建模思想 | 典型结构 |
|---|---|---|
| 线性回归 | least squares / MLE / regularization | $Ax\approx b$ |
| LASSO | 数据拟合 + $\ell_1$ 正则 | 稀疏参数 |
| logistic regression | 最大似然 + 正则化 | 分类概率 |
| SVM | margin / loss + 约束或罚函数 | 二分类 |
| 概率图模型 | likelihood + 稀疏精度矩阵 | 正定矩阵 |
| phase retrieval | least squares / lifting / relaxation | 二次观测 |
| PCA | 最大投影方差或最小重构误差 | 正交约束 |
| matrix separation | low-rank + sparse | 核范数 + $\ell_1$ |
| dictionary learning | reconstruction + sparsity | 双变量矩阵模型 |
| K-means | 组内距离平方和 | 离散分配 |
| TV imaging | data fidelity + TV regularization | 非光滑复合模型 |
| wavelet model | 变换域稀疏 | $\ell_1$ 小波系数 |
| reinforcement learning | 累积 reward / MDP | 随机动态决策 |

### 6. 几个必须真正理解的模型

#### 6.1 线性回归：误差模型决定损失

线性观测

$$
b=Ax+\varepsilon
$$

并不能唯一决定损失函数。

若使用平方误差：

$$
\min_x \frac12\|Ax-b\|_2^2.
$$

如果误差分布或鲁棒性要求改变，可以得到 $\ell_1$ 残差等其他模型。

因此：

> “数据相同”并不意味着“优化模型唯一”。

#### 6.2 LASSO：把稀疏性写进模型

$$
\min_x
\frac12\|Ax-b\|_2^2+\mu\|x\|_1.
$$

第一项要求拟合数据；第二项要求参数具有稀疏结构。

$\mu$ 不是纯算法参数，而是**模型权衡参数**。改变它，就是改变对“拟合”和“稀疏”的相对重视程度。

#### 6.3 Logistic regression：概率模型变成凸优化

对于二分类，教材由条件概率模型构造对数似然，并得到 logistic loss。

需要能解释：

```text
概率假设
→ likelihood
→ log-likelihood
→ optimization objective
```

这是“统计建模 → 优化”的经典桥梁。

#### 6.4 SVM：几何间隔变成优化约束

SVM 从“找到分类超平面，并让样本离超平面尽量远”出发，经缩放和等价转换得到二次目标 + 线性约束的模型。

软间隔版本再通过松弛变量允许部分分类违反。

因此 SVM 展示的是：

> 几何需求 → margin → 约束 → penalty。

#### 6.5 Phase retrieval：提升与松弛

相位恢复原始观测含二次关系。教材展示两条路线：

- 非线性 least-squares；
- lifting：令 $X=xx^*$，把二次关系转成矩阵上的线性关系，再处理 rank-1 结构。

进一步用核范数/迹等凸结构做松弛时，必须保留“恢复需要条件”的限定。

#### 6.6 PCA：两个表面不同的目标可等价

PCA 可以从：

- 最大化投影后的方差；
- 最小化重构误差；

两个角度建立模型。

这是非常重要的建模经验：

> 两个不同的现实解释，可能导出等价优化问题。

#### 6.7 低秩 + 稀疏分解

矩阵分离把观测矩阵表示成：

$$
M=X+S,
$$

其中 $X$ 希望低秩，$S$ 希望稀疏。

困难的 rank 与 $\ell_0$ 结构可分别用核范数和 $\ell_1$ 做凸松弛。

这里要同时看懂：

- 模型结构；
- 松弛结构；
- 算法结构。

三者不是同一个层次。

### 7. 第 4 章：建模后要做“问题归类”

建立模型后，还必须判断它属于哪一类优化问题。

教材第 4 章的主要分类包括：

- linear programming；
- least-squares；
- composite optimization；
- stochastic optimization；
- semidefinite programming；
- matrix optimization；
- integer programming；
- optimization software / modeling languages。

为什么归类重要？

因为算法通常不是针对“应用名称”设计，而是针对数学结构设计。

例如，“图像恢复”和“稀疏回归”应用领域不同，却可能同时落入

$$
\min_x f(x)+g(x)
$$

这样的复合优化结构，于是可以共享 proximal 类算法。

### 8. 本单元实验：模型选择会改变答案

运行：

```bash
python labs/14_optimization_modeling.py
```

实验包含两部分。

#### 实验 A｜同一组回归数据，不同残差模型

比较：

$$
\min_x \|Ax-b\|_2^2
$$

与

$$
\min_x \|Ax-b\|_1.
$$

在加入少量大离群点后，观察估计直线如何变化。

重点不是宣布某个模型“总是更好”，而是回答：

> 哪种残差结构更符合你对噪声的假设？

#### 实验 B｜同一线性模型，不同正则项

比较 ridge 与 LASSO：

$$
\frac12\|Ax-b\|_2^2+\lambda\|x\|_2^2
$$

和

$$
\frac12\|Ax-b\|_2^2+\lambda\|x\|_1.
$$

观察：

- ridge 倾向于整体收缩；
- LASSO 可以产生精确为零的系数；
- 正则项实际上编码了对解结构的偏好。

实验中的 ISTA 只是用来得到 LASSO 数值解；proximal 算法本身会在 Unit 06 系统学习。

### 9. 建模检查表

以后遇到任何实际问题，都按下面顺序写一遍：

1. **数据/状态是什么？**
2. **决策变量是什么？**
3. **目标是什么？**
4. **损失函数为什么这样选？**
5. **有没有先验结构？**
6. **正则项表达的是什么？**
7. **哪些约束来自现实，哪些只是数学变换？**
8. **有没有做松弛？**
9. **松弛是否等价？若不是，丢了什么？**
10. **模型属于哪类优化问题？**
11. **后续算法应该利用什么结构？**

### 10. 练习

#### 练习 1｜同一数据，不同模型

给定 $b=Ax+\varepsilon$，分别写出：

- least-squares；
- least-absolute-deviation；
- ridge；
- LASSO。

逐项解释每个新增项改变了什么假设。

#### 练习 2｜从需求写模型

“希望预测准确，同时只使用少量特征。”

写出一个合理模型，并解释为什么不是只最小化训练误差。

#### 练习 3｜等价变换与松弛

解释下面两件事的本质区别：

- 引入 $y=Ax+b$ 做等价变量替换；
- 用 $\ell_1$ 代替 $\ell_0$。

#### 练习 4｜模型分类

把以下模型分别归入第 4 章的问题类别：

- ordinary least squares；
- LASSO；
- phase-lift SDP；
- K-means；
- logistic regression 的期望风险形式。

允许一个模型具有多个结构标签，但要说明你关注哪一种结构来选算法。

#### 练习 5｜PCA 的双重解释

说明“最大投影方差”和“最小重构误差”为何可以描述同一任务。

#### 练习 6｜失败案例

举一个正则化参数过大导致模型偏离原任务的例子，并解释这属于：

- 算法失败；
- 还是模型选择失败。

### 11. 完成检查

进入 Unit 03 前，应当能不看资料回答：

- 为什么最小二乘不是唯一合理的误差模型？
- 正则化和约束有什么联系与区别？
- 最大似然如何产生优化目标？
- 等价变换和松弛有什么根本不同？
- $\ell_0\rightarrow\ell_1$ 为什么需要额外恢复条件？
- LASSO 中 $\lambda$ 为什么是模型参数，而不只是算法参数？
- 为什么“问题分类”会决定算法路线？
- 一个应用问题为什么可能对应多个不同的优化模型？

下一单元：[Unit 03｜最优性理论](optimization-pku-wenzw-study-units/03-optimality.md)

---

## Unit 03｜最优性理论：什么时候可以说“这个点是解”？

> 对应电子讲义：凸优化最优性理论、非凸优化最优性理论。
>
> 对应教材：第 5 章“最优性理论”。
>
> 本页以第二版教材第 5 章为依据，保留“必要 / 充分 / 充要”“约束品性”“强对偶”等条件边界。

### 1. 本单元的主线

Unit 02 解决“怎样建立优化模型”。Unit 03 解决：

> 给定一个候选点，凭什么说它是局部最优点、全局最优点，或者仅仅是驻点？

教材第 5 章依次讨论：

```text
解的存在性与唯一性
→ 无约束可微问题
→ 无约束不可微 / 复合问题
→ Lagrangian 与对偶
→ 一般约束问题的 KKT
→ 约束问题的二阶条件
→ 凸约束问题 + Slater + 强对偶
```

学习时，每一个条件都必须同时标明：**必要、充分还是充要，以及它依赖哪些假设。**

### 2. 解的存在性与唯一性

考虑

$$
\min_{x\in X} f(x).
$$

教材的 Weierstrass 型存在性定理针对适当且闭的函数：如果以下三类条件之一成立，则最小值点集非空且紧：

1. $\operatorname{dom} f$ 有界；
2. 存在一个非空且有界的下水平集；
3. $f$ 是强制的，即 $\|x^k\|\to\infty$ 时 $f(x^k)\to+\infty$。

直觉是防止“最小值跑向无穷远”。

教材随后用强拟凸给出唯一性结果：若 $X$ 非空、紧、凸，而 $f$ 适当、闭且强拟凸，则最优解唯一。

需要区分：

- 存在最优点；
- 最优点唯一；
- 多个最优点共享同一个最优值。

### 3. 无约束可微问题：驻点不是最优点

考虑

$$
\min_{x\in\mathbb R^n} f(x).
$$

如果存在方向 $d$ 满足

$$
\nabla f(x)^T d<0,
$$

则 $d$ 是下降方向。

所以局部极小点必须满足一阶必要条件

$$
\nabla f(x^*)=0.
$$

教材把满足该式的点称为稳定点，也可称驻点或临界点。

但这只是必要条件。比如 $f(x)=x^3$ 在 $x=0$ 处导数为零，$0$ 却不是局部极小点。

### 4. 二阶最优性条件

若 $f$ 在 $x^*$ 附近二阶连续可微，教材定理 5.4 给出：

#### 二阶必要条件

若 $x^*$ 是局部极小点，则

$$
\nabla f(x^*)=0,
\qquad
\nabla^2 f(x^*)\succeq0.
$$

#### 二阶充分条件

若

$$
\nabla f(x^*)=0,
\qquad
\nabla^2 f(x^*)\succ0,
$$

则 $x^*$ 是局部极小点。

边界必须保留：

- 二阶必要条件不是充分条件；
- 二阶充分条件不是必要条件。

例如 $x^3$ 在 0 处梯度和 Hessian 都为 0，但不是极小点；$x^4$ 在 0 处是全局极小点，但 Hessian 仍为 0。

### 5. 不可微与复合问题

#### 5.1 凸问题

对适当凸函数，教材定理 5.5：

$$
x^* \text{ 是全局极小点}
\quad\Longleftrightarrow\quad
0\in\partial f(x^*).
$$

这是全局最优的充要条件。

#### 5.2 复合优化

考虑

$$
\psi(x)=f(x)+h(x),
$$

其中 $f$ 光滑（可以非凸），$h$ 凸（可以不可微）。

教材定理 5.6 给出局部最优必要条件

$$
-\nabla f(x^*)\in\partial h(x^*),
$$

即

$$
0\in\nabla f(x^*)+\partial h(x^*).
$$

如果整个目标是凸的，这个条件也可用于刻画全局最优。

### 6. Lagrangian 与对偶

一般约束问题写成

$$
\begin{aligned}
\min_x\quad & f(x)\\
\text{s.t.}\quad
& c_i(x)\le0,\quad i\in I,\\
& c_i(x)=0,\quad i\in E.
\end{aligned}
$$

给不等式约束乘子 $\lambda_i\ge0$，等式约束乘子 $\nu_i\in\mathbb R$，构造

$$
L(x,\lambda,\nu)
=
f(x)
+
\sum_{i\in I}\lambda_i c_i(x)
+
\sum_{i\in E}\nu_i c_i(x).
$$

对偶函数：

$$
g(\lambda,\nu)=\inf_x L(x,\lambda,\nu).
$$

对偶问题：

$$
\max_{\lambda\ge0,\nu} g(\lambda,\nu).
$$

教材指出，对偶函数给原始最优值的下界，而且拉格朗日对偶问题本身是凸优化问题。

若原始最优值为 $p^*$，对偶最优值为 $d^*$，则对偶间隙为

$$
p^*-d^*\ge0.
$$

若

$$
p^*=d^*,
$$

则强对偶成立。

### 7. 约束品性：为什么 KKT 不能无条件使用？

教材先比较：

- 切锥 $T_X(x)$；
- 线性化可行方向锥 $F(x)$。

许多约束品性的作用就是保证

$$
T_X(x^*)=F(x^*).
$$

这样才能用容易计算的线性化方向代表真实可行方向。

#### LICQ

若可行点处积极约束的梯度线性无关，则 LICQ 成立。

教材还讨论：

- MFCQ：LICQ 的弱化版本；
- 线性约束品性：所有约束函数本身是线性的。

这些条件在相应情形下可帮助保证 $T_X=F$。

### 8. KKT：一般约束问题的一阶必要条件

教材定理 5.9：如果 $x^*$ 是局部最优点，并且

$$
T_X(x^*)=F(x^*),
$$

则存在乘子使 KKT 成立。

KKT 四部分：

#### 稳定性

$$
\nabla_xL(x^*,\lambda^*,\nu^*)=0.
$$

#### 原始可行性

$$
c_i(x^*)\le0,\quad i\in I,
$$

$$
c_i(x^*)=0,\quad i\in E.
$$

#### 对偶可行性

$$
\lambda_i^*\ge0,\quad i\in I.
$$

#### 互补松弛

$$
\lambda_i^*c_i(x^*)=0,\quad i\in I.
$$

一般非凸约束问题中，KKT 是必要条件，不是充分条件，因此 KKT 点不自动等于局部最优点。

### 9. 约束问题的二阶条件

教材用临界锥 $C(x^*,\lambda^*)$ 收集“一阶信息无法判定”的线性化可行方向。

#### 二阶必要条件

在局部最优点、相应约束品性以及 KKT 乘子存在时，

$$
d^T\nabla^2_{xx}L(x^*,\lambda^*)d\ge0,
\qquad
\forall d\in C(x^*,\lambda^*).
$$

#### 二阶充分条件

如果 KKT 成立，而且

$$
d^T\nabla^2_{xx}L(x^*,\lambda^*)d>0
$$

对所有非零临界方向成立，则 $x^*$ 是严格局部极小点。

和无约束问题相比，关键变化是：只需要沿临界锥检查二阶曲率，而不是要求整个空间上的正定性。

### 10. Slater：凸约束问题中的关键条件

教材第 5.6 节定义 Slater 条件：在自然定义域的相对内点中，存在点使非仿射不等式严格成立并满足等式约束。对仿射不等式，严格性要求可以适当放宽。

教材定理 5.12：

> 凸优化问题满足 Slater 条件时，强对偶成立。

所以

$$
p^*=d^*.
$$

教材定理 5.13：

> 对凸问题，在 Slater 条件下，KKT 条件成为原始/对偶全局最优的充要条件。

| 问题 | 条件 | KKT 角色 |
|---|---|---|
| 一般约束问题 | 相应约束品性 | 局部最优的必要条件 |
| 凸约束问题 | Slater | 原始/对偶全局最优的充要条件 |

### 11. 同一个可行域，不同约束表达

教材习题 5.8 提醒：约束的代数表达会影响 KKT 分析。

考虑可行域 $X=\{0\}$。

#### 表示 A

$$
c(x)=x=0.
$$

此时 $c'(0)=1$，约束梯度不退化。

对

$$
\min_x x\quad\text{s.t. }x=0,
$$

stationarity 为

$$
1+\nu=0,
$$

存在 $\nu=-1$。

#### 表示 B

把同一个可行域写成

$$
c(x)=x^2=0.
$$

此时

$$
c'(0)=0.
$$

stationarity 变成

$$
1+\nu\cdot0=0,
$$

不存在任何乘子使它成立。

但 $x=0$ 仍然是唯一可行点，也是全局最优点。

这说明：如果约束品性失败，局部/全局最优点不一定是 KKT 点。

### 12. 本单元实验

运行：

```bash
python labs/15_optimization_optimality.py
```

实验有三部分：

1. $x^3$ 与 $x^4$：展示“驻点 ≠ 最优点”以及二阶条件边界；
2. $x=0$ 与 $x^2=0$：展示同一可行域的不同表达如何影响 KKT；
3. 凸问题
   $$
   \min_x (x-2)^2\quad\text{s.t. }x\le1
   $$
   展示 Slater、KKT 与强对偶。

第三个问题有严格可行点 $x=0$。其最优点和乘子为

$$
x^*=1,\qquad \lambda^*=2,
$$

原始最优值 $p^*=1$。对偶函数为

$$
g(\lambda)=\lambda-\frac{\lambda^2}{4},\qquad \lambda\ge0,
$$

最大值也为 $1$，所以对偶间隙为 0。

### 13. 最优性条件速查表

| 问题 | 条件 | 结论性质 |
|---|---|---|
| 无约束光滑 | $\nabla f(x^*)=0$ | 局部最优必要 |
| 无约束光滑 | $\nabla f=0,\nabla^2f\succeq0$ | 二阶必要 |
| 无约束光滑 | $\nabla f=0,\nabla^2f\succ0$ | 局部最优充分 |
| 无约束凸 | $0\in\partial f(x^*)$ | 全局最优充要 |
| 复合 $f+h$ | $-\nabla f(x^*)\in\partial h(x^*)$ | 局部最优必要 |
| 一般约束 | KKT + 相应约束品性 | 局部最优必要 |
| 一般约束 | Lagrangian Hessian 在临界锥上正定 | 严格局部最优充分 |
| 凸约束 | Slater + KKT | 原始/对偶全局最优充要 |

### 14. 练习

1. 对 $f(x)=x^4-2x^2$ 求所有驻点，并分类。
2. 分别举例说明二阶必要条件不是充分条件、二阶充分条件不是必要条件。
3. 对 $f(x)=|x|+\frac12(x-1)^2$ 写出 $0\in\partial f(x)$ 并求最优解。
4. 对 $\min x_1^2+x_2^2$，约束 $x_1+x_2=1,x_1\ge0$，写出完整 KKT。
5. 解释为什么互补松弛不意味着所有不等式约束都必须取等号。
6. 解释 $x=0$ 与 $x^2=0$ 在 KKT 分析中的差别。
7. 判断 $\min x^2$ s.t. $x\le1$ 是否有明显 Slater 点，并说明 Slater 支持什么结论。
8. 判断并补条件：
   - $\nabla f(x)=0$，所以 $x$ 是局部极小点；
   - 一个点满足 KKT，所以它是局部最优点；
   - 凸问题满足 KKT，所以它一定是全局最优；
   - Slater 成立，所以原始问题一定存在唯一最优解。

### 15. 完成检查

进入 Unit 04 前，应能回答：

- 什么条件可以防止最优点跑向无穷远？
- 驻点与局部极小点有什么区别？
- 一阶必要、二阶必要、二阶充分分别是什么？
- 为什么凸问题的 $0\in\partial f(x^*)$ 特别强？
- Lagrangian、对偶函数、对偶间隙分别是什么？
- KKT 四部分是什么？
- LICQ / MFCQ / 线性约束品性的共同作用是什么？
- 为什么一般非凸问题的 KKT 只是必要条件？
- 临界锥为什么出现在约束二阶条件中？
- Slater 如何连接强对偶与凸问题 KKT 的充要性？
- 为什么相同可行域的不同表达可能导致不同 KKT 行为？

下一单元：[Unit 04｜无约束优化算法](optimization-pku-wenzw-study-units/04-unconstrained.md)

---

## Unit 04｜无约束优化算法：从局部模型到全局化与收敛速度

> 对应电子讲义：梯度下降算法、牛顿类算法、拟牛顿算法、信赖域算法、非线性最小二乘问题。
>
> 对应教材：第 6 章“无约束优化算法”，重点覆盖 6.1、6.2、6.4、6.5、6.6、6.7。
>
> 第 6.3 节“次梯度算法”属于本章，但本路线把它放到后续非光滑/随机单元集中学习。本页不删除这一章节，只是暂不展开。

### 1. 一条统一主线

本单元不把算法看成互不相关的配方，而统一成四个问题：

```text
局部模型
→ 搜索方向 / 子问题
→ 全局化策略
→ 收敛速度
```

对当前点 $x_k$，记

$$
g_k=\nabla f(x_k),\qquad B_k\approx\nabla^2 f(x_k).
$$

一个常见的二阶局部模型是

$$
m_k(d)
=
f(x_k)+g_k^Td+\frac12d^TB_kd.
$$

不同算法的差别，往往就是：

- $B_k$ 取什么；
- 怎样从 $m_k$ 得到方向 $d_k$；
- 是否需要额外选择步长；
- 如何防止局部模型在远离当前点时失真；
- 在什么条件下能证明收敛，以及局部速度有多快。

### 2. 两种全局化哲学

#### 2.1 线搜索：先选方向，再决定走多远

教材的基本格式是

$$
x_{k+1}=x_k+\alpha_k d_k,
$$

其中 $d_k$ 是搜索方向，$\alpha_k>0$ 是步长。

如果

$$
g_k^Td_k<0,
$$

则 $d_k$ 是下降方向。

线搜索方法的核心是：

1. 先通过梯度、Newton、BFGS 等规则得到 $d_k$；
2. 再沿射线 $x_k+\alpha d_k$ 选择一个合适的 $\alpha_k$。

#### 2.2 信赖域：限制局部模型“可信”的范围

信赖域直接求

$$
\min_d\;
m_k(d)
\quad
\text{s.t. }\|d\|\le\Delta_k.
$$

它不是先定方向再定步长，而是在半径 $\Delta_k$ 内同时选择方向和步长。

因此可以把两者对照为：

| 思路 | 方向 | 步长/尺度 |
|---|---|---|
| 线搜索 | 先确定 $d_k$ | 再选 $\alpha_k$ |
| 信赖域 | 在子问题里共同确定 | 由 $\Delta_k$ 限制 |

### 3. 线搜索：下降还不够，必须“充分下降”

教材用一个一维例子说明：仅要求

$$
f(x_{k+1})<f(x_k)
$$

仍可能收敛到错误位置，甚至迭代点振荡。

所以需要更强的步长准则。

#### 3.1 Armijo 准则

若

$$
f(x_k+\alpha d_k)
\le
f(x_k)+c_1\alpha g_k^Td_k,
\qquad 0<c_1<1,
$$

则步长满足 Armijo 准则。

它要求的不只是“下降”，而是相对于局部线性模型有**充分下降**。

最常用的实现是回退法：

```text
从一个较大候选步长开始
→ 若 Armijo 不满足则乘一个 0<β<1
→ 直到满足
```

#### 3.2 Wolfe 准则

Wolfe 在充分下降之外增加曲率条件，防止步长过小。

教材后面的 BFGS / L-BFGS 全局收敛分析会显式使用 Wolfe 线搜索，因此不能把“任意能下降的步长”与 Wolfe 混为一谈。

#### 3.3 非单调线搜索

教材还介绍 Grippo 以及 Zhang–Hager 类型的非单调准则。

这类规则允许

$$
f(x_{k+1})>f(x_k)
$$

在某些迭代出现，只要相对于一个历史参考值仍满足控制条件。

这一点和 BB 方法非常契合，因为 BB 本身就是非单调方法。

#### 3.4 Zoutendijk 条件

教材定理 6.1 给出一般线搜索框架下的重要收敛工具：当目标函数下有界、连续可微、梯度 Lipschitz，方向为下降方向且步长满足 Wolfe 时，有

$$
\sum_{k=0}^{\infty}
\cos^2\theta_k\|\nabla f(x_k)\|^2
<\infty,
$$

其中 $\theta_k$ 是负梯度与搜索方向之间的夹角。

这条结论揭示了“方向质量 + 步长规则”共同决定全局收敛性的思想。

### 4. 梯度下降：一阶局部模型

如果只看一阶近似

$$
f(x_k+d)\approx f(x_k)+g_k^Td,
$$

在单位长度约束下，最陡下降方向就是

$$
d_k=-g_k.
$$

于是

$$
x_{k+1}
=
x_k-\alpha_k\nabla f(x_k).
$$

#### 4.1 全局化策略

步长可以：

- 固定；
- 精确线搜索；
- Armijo/Wolfe；
- 由其他谱步长规则产生。

#### 4.2 收敛速度

教材给出几类重要结论。

##### 正定二次函数

精确线搜索的梯度法是 Q-线性收敛的，而且速度显式依赖 Hessian 的条件数。

因此病态问题会出现典型“之字形”。

##### 凸 + 梯度 Lipschitz

若 $f$ 凸且梯度 $L$-Lipschitz，固定步长满足相应条件时，教材给出函数值

$$
O(1/k)
$$

的收敛速度。

##### 强凸 + 梯度 Lipschitz

若进一步 $m$-强凸，则固定合适步长后，迭代点 Q-线性收敛。

所以梯度法的定位是：

> 每步便宜、结构简单、全局行为容易控制，但对条件数较大的问题可能很慢。

### 5. Barzilai–Borwein：用两步信息估计曲率尺度

梯度法可写成

$$
x_{k+1}=x_k-D_k g_k,
\qquad
D_k=\alpha_k I.
$$

BB 的关键不是换方向，而是用前后两步的变化估计一个“标量逆 Hessian”。

定义

$$
s_{k-1}=x_k-x_{k-1},
\qquad
y_{k-1}=g_k-g_{k-1}.
$$

按教材记号，两种步长为

$$
\alpha_k^{\mathrm{BB1}}
=
\frac{s_{k-1}^Ty_{k-1}}
{y_{k-1}^Ty_{k-1}},
$$

以及

$$
\alpha_k^{\mathrm{BB2}}
=
\frac{s_{k-1}^Ts_{k-1}}
{s_{k-1}^Ty_{k-1}}.
$$

#### 5.1 为什么它常比普通梯度快？

它把相邻迭代产生的曲率信息压缩进一个标量步长，不需要显式 Hessian，也不要求每次做完整线搜索。

#### 5.2 但它不是“单调下降法”

教材明确指出 BB 本身是非单调方法，实践中常：

- 给 $\alpha_k$ 设置上下界；
- 搭配非单调线搜索。

教材给出的正定二次函数结果是 R-线性收敛；一般非线性问题需要更多条件，不能把该速度直接推广。

### 6. Newton：直接最小化二阶局部模型

令

$$
B_k=\nabla^2f(x_k).
$$

忽略 Taylor 高阶项后，二阶模型的稳定点满足 Newton 方程

$$
\nabla^2f(x_k)d_k=-\nabla f(x_k).
$$

经典 Newton 更新是

$$
x_{k+1}=x_k+d_k.
$$

即步长固定为 1。

#### 6.1 局部速度

教材定理 6.6 的条件包括：

- $f$ 二阶连续可微；
- 最优点附近 Hessian Lipschitz；
- $\nabla f(x^*)=0$；
- $\nabla^2 f(x^*)\succ0$；
- 初值离 $x^*$ 足够近。

在这些条件下，经典 Newton 的迭代点以及梯度范数都具有 Q-二次局部收敛性质。

#### 6.2 为什么经典 Newton 不能直接当全局算法？

教材列出三个核心问题：

1. Hessian 计算、存储以及线性系统求解昂贵；
2. Hessian 不正定时 Newton 方向未必是下降方向；
3. 距最优点较远时，直接取 $\alpha=1$ 可能不稳定甚至发散。

#### 6.3 修正 Newton

教材的修正框架是

$$
B_k
=
\nabla^2f(x_k)+E_k
\succ0,
$$

再解

$$
B_kd_k=-g_k,
$$

并配线搜索选择 $\alpha_k$。

常见思路是 $E_k=\tau_kI$，把 Hessian 修正到正定且条件数可接受。

所以修正 Newton 可以概括为：

```text
准确二阶局部模型
+ 正定化
+ 线搜索全局化
```

### 7. BFGS：不用真正 Hessian，也学习二阶几何

拟 Newton 的核心是构造

$$
B_k\approx\nabla^2f(x_k)
$$

或

$$
H_k\approx\nabla^2f(x_k)^{-1}.
$$

使用

$$
s_k=x_{k+1}-x_k,
\qquad
y_k=g_{k+1}-g_k,
$$

并要求满足割线方程

$$
B_{k+1}s_k=y_k
$$

或

$$
H_{k+1}y_k=s_k.
$$

BFGS 用秩二更新完成这一点，同时尽量不让新矩阵偏离旧近似矩阵。

#### 7.1 全局化

教材定理 6.8 的 BFGS 全局收敛结论显式要求 Wolfe 线搜索，并对目标函数/下水平集上的 Hessian 给出正定有界条件。

因此：

> BFGS 的好性质不是“更新公式单独保证”的；线搜索和函数结构也是证明的一部分。

#### 7.2 局部速度

教材定理 6.9 在给定收敛及附加条件下得到 Q-超线性速度。

它比 Newton 的 Q-二次慢，但避免了每一步显式计算 Hessian。

#### 7.3 L-BFGS

完整 $B_k/H_k$ 是稠密矩阵，存储成本 $O(n^2)$。

L-BFGS 只保留最近 $m$ 对

$$
(s_i,y_i),
$$

并用双循环递归计算 $H_kg_k$，因此适合大规模问题。

教材的 L-BFGS 框架同样配 Wolfe 线搜索。

### 8. 信赖域：让局部模型自己证明“可信”

考虑二次模型

$$
m_k(d)
=
f(x_k)+g_k^Td+\frac12d^TB_kd
$$

以及约束

$$
\|d\|\le\Delta_k.
$$

求出候选步 $d_k$ 后，比较：

- 实际下降；
- 模型预测下降。

定义比值

$$
\rho_k
=
\frac{f(x_k)-f(x_k+d_k)}
{m_k(0)-m_k(d_k)}.
$$

#### 8.1 半径更新逻辑

- $\rho_k\approx1$：模型可信，可以扩大 $\Delta_k$；
- $\rho_k$ 很小或为负：模型失真，应缩小 $\Delta_k$；
- $\rho_k$ 足够大：接受步长；
- 否则拒绝，保持当前点。

教材常用参数示例为 $0.25$、$0.75$ 等阈值，但这些是算法参数，不是数学常数。

#### 8.2 子问题不一定要精确求解

教材介绍 Cauchy 点和截断共轭梯度等方法。

真正重要的是：

> 子问题只需达到足够的模型下降质量，就可以支撑整个信赖域算法的收敛分析。

### 9. 线搜索与信赖域：同一局部模型的两种全局化

可以把 Newton 类方法统一看成：

#### 线搜索 Newton

$$
\nabla^2f(x_k)d_k=-g_k,
$$

然后寻找 $\alpha_k$：

$$
x_{k+1}=x_k+\alpha_kd_k.
$$

#### 信赖域 Newton

直接求

$$
\min_{\|d\|\le\Delta_k}
g_k^Td+\frac12d^T\nabla^2f(x_k)d.
$$

因此两者不是“有没有二阶信息”的区别，而是：

> 如何限制二阶模型在远离当前点时造成的误导。

### 10. 非线性最小二乘：利用残差结构，不要把它当普通黑箱

考虑

$$
f(x)
=
\frac12\sum_{i=1}^{m}r_i(x)^2
=
\frac12\|r(x)\|_2^2.
$$

记 $J(x)$ 为残差向量 $r(x)$ 的 Jacobian，则教材给出

$$
\nabla f(x)
=
J(x)^Tr(x),
$$

以及

$$
\nabla^2f(x)
=
J(x)^TJ(x)
+
\sum_{i=1}^{m}
r_i(x)\nabla^2r_i(x).
$$

这说明 Hessian 自然分成两部分。

第一部分 $J^TJ$ 在计算梯度时已经“顺带”获得；第二部分需要每个残差的 Hessian，代价更高。

### 11. Gauss–Newton：舍掉难算的二阶残差项

Gauss–Newton 用

$$
J_k^TJ_k
$$

近似真正 Hessian，于是方向满足

$$
J_k^TJ_kd_k=-J_k^Tr_k.
$$

这等价于线性最小二乘子问题

$$
\min_d
\frac12\|J_kd+r_k\|_2^2.
$$

教材把 Gauss–Newton 主要放在**小残量问题**中讨论。

其局部速度结论不能简化成“永远二次收敛”：

- 某个反映被舍弃 Hessian 项大小的量足够小时，可得到 Q-线性；
- 当该项在解处为零时，可以达到 Q-二次；
- 若被舍弃部分较大，Gauss–Newton 可能失效。

### 12. Levenberg–Marquardt：Gauss–Newton 的信赖域化

教材把 LM 描述为信赖域型方法，考虑

$$
\min_d
\frac12\|J_kd+r_k\|_2^2
\quad
\text{s.t. }\|d\|\le\Delta_k.
$$

相应最优性条件可以写为

$$
(J_k^TJ_k+\lambda I)d
=
-J_k^Tr_k,
\qquad
\lambda\ge0,
$$

并满足相应互补条件。

这条式子揭示了 LM 的核心：

- 当 $\lambda$ 小，行为接近 Gauss–Newton；
- 当 $\lambda$ 大，步子更保守、更接近梯度型方向；
- 即使 $J^TJ$ 奇异，加入正则项后仍可能得到稳定方向。

### 13. “局部模型 → 方向 → 全局化 → 速度”总表

| 方法 | 局部模型/曲率 | 方向或子问题 | 全局化 | 教材中的代表速度/性质 |
|---|---|---|---|---|
| Gradient | 一阶 | $-g_k$ | fixed / Armijo / Wolfe | 凸光滑函数值 $O(1/k)$；强凸时 Q-线性 |
| BB | 标量谱曲率 | $-\alpha_k g_k$ | 截断 + 非单调线搜索 | 正定二次情形 R-线性 |
| Newton | 真 Hessian | $H_kd=-g_k$ | 经典版无；实用版线搜索/修正 | 合适局部条件下 Q-二次 |
| BFGS | 拟 Hessian | $B_kd=-g_k$ 或 $-H_kg_k$ | Wolfe | 给定相应条件时 Q-超线性 |
| L-BFGS | 最近若干割线对 | 双循环递归 | Wolfe | 降低内存，面向大规模 |
| Trust region | 二阶模型 | $\min m_k(d),\|d\|\le\Delta_k$ | $\rho_k$ + 半径更新 | 全局化通过模型可信度控制 |
| Gauss–Newton | $J^TJ$ | 线性 least-squares | 通常配线搜索 | 小残量；特定条件下 Q-线性/二次 |
| LM | $J^TJ+\lambda I$ | 正则化 least-squares / TR | 信赖域 | 对奇异/近奇异 $J^TJ$ 更稳健 |

这张表不能理解成“速度排名”。

局部收敛阶数、每步计算代价、内存、全局收敛前提以及问题结构不同，不能只看 Q-二次、Q-超线性、Q-线性几个词就判断实际耗时。

### 14. 一个实用的算法选择视角

#### 梯度 / BB

适合：

- 维度高；
- Hessian 昂贵；
- 中低精度阶段；
- 希望每一步非常便宜。

#### Newton / 修正 Newton

适合：

- Hessian 可获得或可高效作用到向量；
- 需要高精度；
- 已进入较好的局部区域。

#### BFGS / L-BFGS

适合：

- Hessian 不易计算；
- 梯度可计算；
- 希望利用曲率；
- L-BFGS 尤其适合大规模变量。

#### Trust region

适合：

- 二阶局部模型可能在远处不可靠；
- Hessian 可能不定；
- 希望通过“模型预测 vs 实际下降”自动调节尺度。

#### Gauss–Newton / LM

只有当目标确实具有

$$
\frac12\|r(x)\|^2
$$

结构时才应优先考虑，因为它们的优势来自**利用问题结构**，而不是作为任意无约束问题的通用替代。

### 15. 本单元实验

运行：

```bash
python labs/16_optimization_unconstrained.py
```

实验分两组。

#### A｜Rosenbrock：比较五种无约束策略

从同一个初始点出发，比较：

- gradient + Armijo；
- BB + 非单调 Armijo；
- modified Newton + Armijo；
- BFGS + Armijo；
- trust-region Newton model。

记录：

- $\|\nabla f(x_k)\|$；
- 迭代次数；
- 最终函数值。

观察重点：

1. 一阶方法为什么会慢；
2. BB 如何用谱步长改善梯度迭代；
3. Newton 靠近解后为什么非常快；
4. BFGS 如何在不显式使用真 Hessian 的情况下获得二阶加速；
5. trust region 如何根据模型可信度接受/拒绝步长。

> 这个实验只比较一个二维非凸函数，不能据此给算法做普遍排名。

#### B｜非线性曲线拟合：Gauss–Newton vs LM

生成指数衰减模型

$$
y(t)=a\exp(bt)+\varepsilon,
$$

并比较：

- Gauss–Newton；
- LM 型阻尼更新。

记录残差范数以及参数恢复结果。

这里的目标是观察“利用 residual/Jacobian 结构”与普通通用算法的不同。

### 16. 练习

1. 写出 Armijo 准则，并解释“只要求函数下降”为何不足。
2. 在正定二次函数上推导精确线搜索的梯度步长。
3. 解释梯度法的条件数依赖为什么会产生之字形。
4. 写出教材的 BB1/BB2，并说明 $s_k,y_k$ 各代表什么。
5. 为什么经典 Newton 不是一个可靠的全局算法？
6. 修正 Newton 为什么要让 $B_k$ 正定且条件数不要太差？
7. 什么是拟 Newton 的割线方程？
8. 为什么 BFGS 的全局收敛定理不能脱离 Wolfe 条件来复述？
9. L-BFGS 为什么可以节省内存？
10. 信赖域的 $\rho_k$ 接近 1、很小、为负分别意味着什么？
11. 推导非线性 least-squares 的梯度与 Hessian 分解。
12. Gauss–Newton 丢掉了 Hessian 的哪一部分？
13. 为什么“小残量”会让 Gauss–Newton 的近似更合理？
14. LM 中 $\lambda$ 增大时，为什么步骤通常会更保守？
15. “Newton Q-二次，所以永远比 BFGS 快”为什么是错误说法？

### 17. 完成检查

进入 Unit 05 前，应能不看资料回答：

- 线搜索与信赖域在全局化哲学上有什么区别？
- Armijo 与 Wolfe 各控制什么？
- 梯度法、BB、Newton、BFGS 各自用了多少曲率信息？
- 为什么 BB 可以非单调？
- Newton 的 Q-二次结论需要哪些局部条件？
- 修正 Newton 怎样解决 Hessian 不正定？
- BFGS 的割线方程是什么？
- L-BFGS 为什么适合大规模问题？
- 信赖域中的 actual reduction / predicted reduction 是什么？
- Gauss–Newton 为什么能省掉一部分二阶导数？
- LM 和 trust region 的关系是什么？
- 为什么不能仅按“Q-二次 > Q-超线性 > Q-线性”给算法排优劣？

下一单元：[Unit 05｜约束优化算法](optimization-pku-wenzw-study-units/05-constrained.md)

---

## Unit 05｜约束优化算法：罚函数、增广 Lagrangian、原始–对偶与内点法

> 对应电子讲义：罚函数法、增广拉格朗日函数法、线性规划内点法。
>
> 对应教材：第 7 章“约束优化算法”，本单元重点覆盖 7.1、7.2、7.3。
>
> 第二版第 7.4 节“流形约束优化算法”保留到 Unit 08 单独展开，不在本单元重复。

### 1. 一条统一主线

Unit 03 已经给出了 KKT、乘子、对偶和约束品性。Unit 05 开始问：

> 算法怎样逐步同时降低目标值、降低约束违反、逼近正确乘子，并最终满足 KKT？

本单元把三类策略统一为：

```text
外点罚函数：把不可行性变成越来越重的代价
→ 增广 Lagrangian：罚函数 + 乘子更新
→ 原始–对偶内点：同时更新原始变量、对偶变量和互补条件
```

对一般问题

$$
\begin{aligned}
\min_x\quad & f(x)\\
\text{s.t.}\quad
& c_i(x)=0,\quad i\in E,\\
& c_i(x)\le0,\quad i\in I,
\end{aligned}
$$

算法真正要同时控制的是：

- stationarity；
- equality feasibility；
- inequality feasibility；
- dual feasibility；
- complementary slackness。

### 2. 二次罚函数：把约束变成目标的一部分

#### 2.1 等式约束

对

$$
c_i(x)=0,
$$

教材定义二次罚函数

$$
P_E(x,\sigma)
=
f(x)
+
\frac{\sigma}{2}
\sum_{i\in E}c_i(x)^2.
$$

罚因子 $\sigma>0$ 越大，不可行点受到的惩罚越强。

典型外迭代是：

```text
选择 σ_0
→ 近似求解 min P_E(x,σ_k)
→ 增大 σ_k
→ 用上一子问题的解 warm start
→ 重复
```

这也是 continuation 思想的一种形式。

#### 2.2 不等式约束

对

$$
c_i(x)\le0,
$$

不能直接罚 $c_i(x)^2$，否则严格可行的 $c_i(x)<0$ 也会被惩罚。

教材采用

$$
[c_i(x)]_+
=
\max\{c_i(x),0\},
$$

并构造

$$
P_I(x,\sigma)
=
f(x)
+
\frac{\sigma}{2}
\sum_{i\in I}[c_i(x)]_+^2.
$$

这只惩罚违反约束的部分。

教材指出：该平方正部函数可导，但一般不是二阶可导，因此不能简单把普通光滑 Newton 理论原样套上去。

### 3. 二次罚函数为什么会数值变难？

二次罚函数法为了逼近严格可行性，通常需要

$$
\sigma_k\to+\infty.
$$

教材对等式约束给出的 Hessian 结构可写成

$$
\nabla^2_{xx}P_E(x,\sigma)
=
\nabla^2f(x)
+
\sigma\sum_i c_i(x)\nabla^2c_i(x)
+
\sigma\nabla c(x)\nabla c(x)^T.
$$

在接近解时，最后一项随 $\sigma$ 放大，而它通常只在约束法向方向上强化曲率。

结果是：

> 约束违反越来越小，但子问题条件数可能越来越差。

这就是罚函数的核心权衡：

```text
更大的 σ
→ 更接近可行域
→ 但子问题更病态
```

### 4. 罚函数收敛：必须保留前提

教材定理 7.1 的结论不是无条件的。

如果：

- 每个二次罚函数子问题都取得全局极小解；
- $\sigma_k$ 单调趋于 $+\infty$；

那么这些子问题解序列的每个极限点都是原问题的全局极小解。

实际中通常只能近似求子问题。教材定理 7.2进一步要求：

- 子问题一阶残差趋于零；
- $\sigma_k\to+\infty$；
- 极限点处等式约束梯度线性无关；

此时极限点满足原问题 KKT，而且

$$
-\sigma_k c_i(x_{k+1})
\to
\lambda_i^*.
$$

所以罚函数不仅在逼近可行性，还隐式地“制造”出乘子估计。

### 5. 精确罚函数：有限罚因子也可能够用

教材还介绍 $\ell_1$ 精确罚函数：

$$
P(x,\sigma)
=
f(x)
+
\sigma
\left(
\sum_{i\in E}|c_i(x)|
+
\sum_{i\in I}[c_i(x)]_+
\right).
$$

和二次罚函数不同，它是非光滑的。

教材定理 7.3 给出一个局部精确性结论：若 $x^*$ 是严格局部极小点并满足 KKT，乘子为 $\lambda^*$，则当

$$
\sigma>\|\lambda^*\|_\infty
$$

时，$x^*$ 也是该 $\ell_1$ 罚函数的局部极小点。

所以“精确”指的是：

> 不需要让罚因子趋于无穷，有限大的罚因子就可能保留原问题局部解。

但代价是子问题变成非光滑问题，这会和 Unit 06 的 proximal 方法衔接。

### 6. 增广 Lagrangian：用乘子避免一味增大罚因子

对等式约束，教材定义

$$
L_\sigma(x,\lambda)
=
f(x)
+
\sum_{i\in E}\lambda_i c_i(x)
+
\frac{\sigma}{2}
\sum_{i\in E}c_i(x)^2.
$$

给定 $(\lambda_k,\sigma_k)$，先近似求

$$
x_{k+1}
\approx
\arg\min_x
L_{\sigma_k}(x,\lambda_k),
$$

再更新乘子

$$
\lambda_{k+1}
=
\lambda_k
+
\sigma_k c(x_{k+1}).
$$

这里的关键不是“多加了一项”，而是：

```text
二次罚函数
只靠 σ 压约束

增广 Lagrangian
靠 σ + λ_k 一起控制约束
```

教材由

$$
c_i(x_{k+1})
\approx
\frac{\lambda_i^*-\lambda_i^k}{\sigma_k}
$$

解释了这一点：当乘子已经接近真实乘子时，即使 $\sigma_k$ 不是极端大，约束违反也可以很小。

### 7. 增广 Lagrangian 的局部精确性

教材定理 7.4 的条件包括：

- $x^*$ 是等式约束问题局部极小点；
- 对应乘子为 $\lambda^*$；
- LICQ 成立；
- 二阶充分条件成立。

则存在有限的 $\bar\sigma$，使得对

$$
\sigma\ge\bar\sigma,
$$

$x^*$ 是

$$
L_\sigma(x,\lambda^*)
$$

的严格局部极小点。

这正是 ALM 相比纯二次罚函数的重要优势之一：

> 在乘子正确或足够接近时，不必靠 $\sigma\to\infty$ 才能锁定局部解。

### 8. 一般不等式约束的 ALM

教材通过松弛变量把

$$
c_i(x)\le0
$$

改写成

$$
c_i(x)+s_i=0,
\qquad
s_i\ge0.
$$

消去 $s_i$ 后，增广 Lagrangian 中出现

$$
\max\left\{
\frac{\mu_i}{\sigma}+c_i(x),0
\right\}.
$$

对应乘子更新为：

#### 等式约束

$$
\lambda_i^{k+1}
=
\lambda_i^k
+
\sigma_k c_i(x_{k+1}).
$$

#### 不等式约束

$$
\mu_i^{k+1}
=
\max\{
\mu_i^k+\sigma_k c_i(x_{k+1}),
0
\}.
$$

这个投影式更新直接维护

$$
\mu_i^{k+1}\ge0.
$$

教材的算法 7.6 还把“约束违反是否已经足够小”作为参数更新逻辑的一部分：

- 若违反度下降得足够好：更新乘子、提高子问题精度，罚因子可保持；
- 若违反度不够好：暂缓乘子更新并增大罚因子。

所以实际 ALM 是一个双层控制系统：

```text
内层：近似最小化增广 Lagrangian
外层：看约束违反 → 更新 multiplier 或 penalty
```

### 9. 凸问题中的 ALM：原始与对偶同时出现

教材第 7.2.3 对凸问题给出 ALM 收敛结论。

在相应不精确子问题条件下，如果 Slater 成立，则：

- 乘子序列有界并收敛；
- 乘子极限是对偶问题的最优解。

如果再有一个非空有界的适当下水平集，则：

- 原始迭代点序列有界；
- 所有聚点都是原问题最优解。

所以在凸问题中，ALM 的乘子更新不是一个“辅助变量技巧”，而是实实在在地在逼近**对偶最优解**。

教材在基追踪和半定规划中都进一步展示了原始问题与对偶问题两侧的 ALM 结构。

### 10. 原始–对偶结构：从 KKT 到算法

线性规划写成：

#### 原始问题

$$
\begin{aligned}
\min_x\quad & c^Tx\\
\text{s.t.}\quad
& Ax=b,\\
& x\ge0.
\end{aligned}
$$

#### 对偶问题

$$
\begin{aligned}
\max_y\quad & b^Ty\\
\text{s.t.}\quad
& A^Ty+s=c,\\
& s\ge0.
\end{aligned}
$$

KKT 为：

$$
Ax=b,
$$

$$
A^Ty+s=c,
$$

$$
x_i s_i=0,
$$

$$
x\ge0,\quad s\ge0.
$$

这里：

- $x$ 是原始变量；
- $y,s$ 是对偶侧变量；
- $x_i s_i=0$ 是互补松弛。

**原始–对偶算法**的含义就是：

> 不只更新 $x$，而是把原始可行性、对偶可行性和互补性放进同一套方程一起处理。

### 11. 内点法：先不碰边界，再逐渐逼近互补条件

在线性规划最优解处通常有某些分量

$$
x_i=0
$$

或

$$
s_i=0.
$$

而内点法在迭代期间保持

$$
x>0,
\qquad
s>0.
$$

它不能立即满足

$$
x_i s_i=0.
$$

所以教材把互补条件扰动为

$$
x_i s_i=\tau,
\qquad
\tau>0.
$$

于是得到中心路径方程：

$$
Ax=b,
$$

$$
A^Ty+s=c,
$$

$$
x_i s_i=\tau,
$$

$$
x>0,\quad s>0.
$$

当

$$
\tau\downarrow0,
$$

这条路径逼近原始 KKT 系统。

### 12. Barrier 视角与中心路径

教材指出中心路径也可以从对数 barrier 问题理解：

$$
\begin{aligned}
\min_x\quad
& c^Tx
-
\tau\sum_{i=1}^n\log x_i\\
\text{s.t.}\quad
& Ax=b.
\end{aligned}
$$

这里

$$
-\log x_i
$$

在 $x_i\downarrow0$ 时趋于 $+\infty$，所以迭代点被留在严格内部。

随着 $\tau$ 变小，barrier 逐渐减弱，允许解越来越接近边界上的 LP 最优点。

这和外点罚函数正好形成对照：

| 方法 | 迭代位置 |
|---|---|
| 外点罚函数 | 通常在可行域外逐渐逼近 |
| 内点/barrier | 始终在可行域严格内部移动 |

### 13. 原始–对偶 Newton 系统

对扰动 KKT 方程做 Newton 线性化，可以同时求：

$$
(\Delta x,\Delta y,\Delta s).
$$

然后更新

$$
x_{k+1}=x_k+\alpha\Delta x,
$$

$$
y_{k+1}=y_k+\alpha\Delta y,
$$

$$
s_{k+1}=s_k+\alpha\Delta s.
$$

步长 $\alpha$ 必须保证

$$
x_{k+1}>0,
\qquad
s_{k+1}>0.
$$

因此内点法虽然使用 Newton 型方向，但还要做“fraction-to-boundary”式的步长控制，防止走出严格内部。

主要计算代价集中在原始–对偶 Newton 线性系统的求解。

### 14. 对偶间隙与中心路径

若 $(x,y,s)$ 同时满足原始和对偶可行性，则

$$
c^Tx-b^Ty
=
x^Ts.
$$

在中心路径上

$$
x_i s_i=\tau,
$$

因此

$$
x^Ts=n\tau.
$$

这给出了非常直观的停止尺度：

> 当互补乘积和对偶间隙都趋近于零时，原始–对偶对正在逼近 KKT 解。

这里是由教材给出的原始/对偶可行方程与中心路径方程直接推得的代数结果。

### 15. 路径追踪：不是每次从头解 barrier 子问题

实际算法不会为每一个更小的 $\tau$ 完全从头求解。

更常见的路径追踪逻辑是：

```text
选择当前中心参数
→ Newton 校正到中心路径附近
→ 降低中心参数
→ 用当前点 warm start
→ 重复
```

这和罚函数 continuation 在结构上有相似之处：

- 都是一系列参数化子问题；
- 都利用上一阶段解 warm start；
- 但一个从外侧压向可行域，一个从内部沿中心路径走向边界。

### 16. 三类算法的统一比较

| 方法 | 核心参数 | 原始可行性 | 对偶变量 | 主要数值问题 |
|---|---|---|---|---|
| 二次罚函数 | $\sigma\uparrow\infty$ | 渐近逼近 | 隐式出现 | 大 $\sigma$ 导致病态 |
| 精确 $\ell_1$ 罚函数 | 有限 $\sigma$ | 可有限参数精确 | 阈值与乘子相关 | 非光滑子问题 |
| 增广 Lagrangian | $\sigma$ + $\lambda_k$ | 通过乘子反馈逼近 | 显式更新 | 内层子问题与参数协调 |
| 原始–对偶内点 | $\tau\downarrow0$ | 维持严格内部 | 显式同时更新 | Newton/KKT 线性系统 |

### 17. 和前后单元的关系

#### 来自 Unit 03

本单元算法的终点几乎都在逼近：

- stationarity；
- primal feasibility；
- dual feasibility；
- complementary slackness。

也就是 KKT。

#### 通往 Unit 06

ALM 的很多子问题会包含：

- $\ell_1$；
- 投影；
- indicator function；
- 非光滑复合结构。

这正是 proximal / splitting / ADMM 的入口。

#### 通往 Unit 08

第二版第 7.4 节把约束几何推进到流形：

- tangent space；
- Riemannian gradient；
- retraction；
- manifold Newton / trust-region。

这些内容会作为 Unit 08 单独处理。

### 18. 本单元实验

运行：

```bash
python labs/17_optimization_constrained.py
```

实验分两组。

#### A｜二次罚函数 vs 增广 Lagrangian

问题：

$$
\min_x
\frac12\|x-q\|_2^2
\quad
\text{s.t. }
a^Tx=b.
$$

这个问题可以显式求最优解。

实验比较：

##### 纯二次罚函数

$$
\frac12\|x-q\|^2
+
\frac{\sigma}{2}(a^Tx-b)^2.
$$

随着 $\sigma$ 增大：

- 约束违反减小；
- 子问题 Hessian
  $$
  I+\sigma aa^T
  $$
  的条件数增大。

##### ALM

固定一个有限 $\sigma$，重复：

$$
x_{k+1}
=
\arg\min_x
L_\sigma(x,\lambda_k),
$$

$$
\lambda_{k+1}
=
\lambda_k
+
\sigma(a^Tx_{k+1}-b).
$$

观察：

- 约束违反快速下降；
- $\lambda_k$ 逼近真实 KKT 乘子；
- 内层 Hessian 条件数保持固定。

这正好展示“为什么要从 penalty 走向 ALM”。

#### B｜原始–对偶中心路径

线性规划：

$$
\begin{aligned}
\min_{x_1,x_2}\quad & x_1+2x_2\\
\text{s.t.}\quad
& x_1+x_2=1,\\
& x_1,x_2\ge0.
\end{aligned}
$$

最优点在边界：

$$
x^*=(1,0).
$$

实验直接解一系列中心路径方程：

$$
Ax=b,
$$

$$
A^Ty+s=c,
$$

$$
x_i s_i=\tau,
$$

并逐步减小 $\tau$。

观察：

- $x_2\to0$；
- $s_1\to0$；
- $x^Ts=2\tau\to0$；
- 原始目标和对偶目标逐渐靠拢。

### 19. 练习

1. 对等式约束问题写出二次罚函数，并解释为什么需要逐步增大 $\sigma$。
2. 为什么不等式罚函数必须使用 $[c_i(x)]_+$，而不是直接 $c_i(x)^2$？
3. 教材定理 7.1 为什么在实际中较强？它对子问题解要求了什么？
4. 解释
   $$
   -\sigma_k c_i(x_{k+1})\to\lambda_i^*
   $$
   的意义。
5. 为什么二次罚函数在 $\sigma\to\infty$ 时容易病态？
6. 精确 $\ell_1$ 罚函数中的“精确”是什么意思？
7. 推导等式 ALM 的乘子更新
   $$
   \lambda_{k+1}=\lambda_k+\sigma_kc(x_{k+1}).
   $$
8. 不等式 ALM 为什么要做
   $$
   \max\{\mu_i^k+\sigma c_i(x),0\}?
   $$
9. 在凸问题中，ALM 的乘子极限为什么可以解释为对偶最优解？
10. 写出 LP 的原始、对偶和四类 KKT 条件。
11. 为什么内点法在迭代中不能直接满足 $x_is_i=0$？
12. 中心路径为什么使用 $x_is_i=\tau$？
13. 推导可行原始–对偶点的 gap：
    $$
    c^Tx-b^Ty=x^Ts.
    $$
14. 外点罚函数和 log-barrier 在“从哪一侧逼近”上有什么根本区别？
15. 为什么路径追踪和 penalty continuation 都需要 warm start？

### 20. 完成检查

进入 Unit 06 前，应能回答：

- 二次罚函数、精确罚函数、ALM 的差别是什么？
- 为什么 penalty parameter 太大会造成数值困难？
- ALM 的乘子更新在控制什么？
- 一般不等式 ALM 怎样保持乘子非负？
- 原始与对偶变量为什么应该联合看？
- LP 的 KKT 条件是什么？
- 内点法为什么维护 $x>0,s>0$？
- 中心路径和 barrier 子问题是什么关系？
- 原始–对偶 gap 为什么等于 $x^Ts$？
- 为什么 ALM 与内点法都可以看成“直接逼近 KKT”，但采用了完全不同的路径？

下一单元：[Unit 06｜复合优化：proximal、加速与分裂](optimization-pku-wenzw-study-units/06-composite.md)


## 6. Unit 06–10 原施工规格与现行独立页面

> Unit 06 的已合并草稿见[独立学习页](optimization-pku-wenzw-study-units/06-composite.md)及 `labs/18_optimization_composite.py`。本节保留原施工规格；Unit 07–10 的现行独立页面见上表，尚未完成来源和运行验收。

### Unit 06｜复合优化：proximal、加速、分裂

**状态：独立学习页与实验已交付草稿，待来源复核与 PR 验收；下列条目为原施工规格。**

**直接讲义：**

- 19 近似点算子：18-lect-prox_map.pdf；
- 20 近似点梯度算法：19-lect-proxg.pdf；
- 21 Nesterov 加速算法：20-lect-nesterov-ch.pdf；
- 22 近似点算法：21-lect-prox_point.pdf；
- 23 分块坐标下降法：22-lect-BCD.pdf / 22-lect-BCD-pku.pdf；
- 24 对偶算法：23-lect-DualAlgo.pdf；
- 25 ADMM：24-lect-admm-chhyx.pdf。

**教材范围：第 8.1–8.6 节。**

核心问题统一写为

$$
\min_x \psi(x)=f(x)+h(x),
$$

其中 f 通常光滑，h 可以不可微，但要求其结构可利用。

#### 06.1 邻近算子

建立

$$
\operatorname{prox}_{t h}(v)
=
\arg\min_u
\left\{
h(u)+\frac{1}{2t}\|u-v\|^2
\right\}.
$$

必须掌握：

- indicator function 的 prox = projection；
- l1 的 prox = soft-thresholding；
- 为什么 prox 可以理解为“隐式一步”；
- Moreau–Yosida 正则化与 prox 的关系；
- prox 是否单值需要哪些条件，不能把凸情形结论无条件搬到非凸情形。

#### 06.2 Proximal Gradient / ISTA

教材的核心更新：

$$
x_{k+1}
=
\operatorname{prox}_{t_kh}
\bigl(x_k-t_k\nabla f(x_k)\bigr).
$$

统一解释为：

- 对 f 做显式梯度步；
- 对 h 做隐式 prox 步；
- 或者最小化“光滑项线性化 + 二次稳定项 + 原非光滑项”。

重点模型：

$$
\min_x
\frac12\|Ax-b\|^2+\lambda\|x\|_1.
$$

即 LASSO。

待记录：

- 固定步长与线搜索条件；
- 凸光滑情形的代表性函数值速度；
- 非凸 prox-gradient 需要保留的额外条件和多值 prox 边界。

#### 06.3 Nesterov / FISTA

教材明确把 proximal-gradient 的 O(1/k) 凸情形提升到 Nesterov/FISTA 的代表性

$$
O(1/k^2).
$$

学习重点：

- extrapolation point；
- estimate-sequence / 加速思想；
- FISTA 为什么仍然只用一阶信息；
- 非单调目标轨迹与函数值理论保证的区别；
- restart 为什么是实际常见技巧，但不能把经验技巧写成无条件理论结论。

#### 06.4 Proximal Point

学习

$$
x_{k+1}
=
\operatorname{prox}_{t_k f}(x_k).
$$

必须连接 Unit 05：

> 教材后续明确讨论 proximal-point 与 augmented Lagrangian 的对偶关系；原始问题上做 ALM，可对应对偶问题上的 proximal-point 更新。

#### 06.5 Block Coordinate Descent

统一问题：

$$
x=(x_1,\ldots,x_p),
$$

每次只更新一个或一组 block。

要求掌握：

- cyclic / randomized block update；
- block-separable nonsmooth term；
- 为什么“每个子问题都下降”并不自动等于任意非凸问题全局收敛；
- LASSO / dictionary learning 等模型中的 block structure。

#### 06.6 Dual Methods

目标是把 Unit 03 的 duality 从“判定最优”推进到“直接在 dual 上迭代”。

应覆盖：

- dual decomposition；
- primal recovery；
- projection / prox on dual feasible set；
- 对偶残差和原始残差如何一起解释。

#### 06.7 ADMM

标准分裂结构：

$$
\min_{x,z}
f(x)+g(z)
\quad
\text{s.t. }Ax+Bz=c.
$$

通过 augmented Lagrangian 交替最小化：

1. x-update；
2. z-update；
3. multiplier update。

必须和 Unit 05 建立明确联系：

- ADMM 来自 augmented Lagrangian + variable splitting + alternating minimization；
- primal residual / dual residual 是停止准则的一部分；
- penalty parameter rho 会影响数值表现，但不能把某个固定经验值写成理论最优。

**待审实验：** labs/18_optimization_composite.py

同一个 LASSO 问题比较：

- ISTA；
- FISTA；
- coordinate descent；
- ADMM。

记录 objective gap、KKT/prox-gradient residual、sparsity、ADMM primal/dual residual，以及每步成本与迭代数。

**完成标准：**

- 能手推 soft-threshold prox；
- 能从 quadratic upper model 推导 proximal-gradient；
- 能解释 ISTA 与 FISTA 的差别；
- 能从 ALM 推出 ADMM 更新结构；
- 能解释 primal/dual residual；
- 能给出一个“算法迭代次数少但每步更贵”的案例，避免只按迭代数排名。

---

### Unit 07｜随机与非光滑高级算法

**状态：独立页面及脚本已写，未运行；本节为原施工规格。**

**讲义：**

- 10 次梯度；
- 11 次梯度算法；
- 26 随机优化算法；
- 27 半光滑牛顿算法。

**教材范围：第 6.3、8.7、8.8 节。**

#### 07.1 次梯度与次梯度算法

补回 Unit 04 暂缓的第 6.3 节。

$$
g_k\in\partial f(x_k),
\qquad
x_{k+1}=x_k-\alpha_k g_k.
$$

重点是步长：

- 固定步长可能只到邻域；
- diminishing step 需要保留具体求和条件；
- 次梯度法通常非单调；
- 不能把光滑梯度法的 Lipschitz-gradient 速度直接搬过来。

#### 07.2 随机优化

教材第 8.7 采用有限和模型

$$
f(x)=\frac1N\sum_{i=1}^N f_i(x).
$$

要覆盖：

- stochastic gradient estimator；
- unbiasedness / variance；
- batch / mini-batch；
- diminishing learning rate；
- convex / strongly convex / nonconvex 情形分开记录。

#### 07.3 方差减小

教材目录明确包含“方差减小技术”。

学习目标：

- 为什么普通 SGD 接近解时噪声仍存在；
- full-gradient snapshot + stochastic correction 的思想；
- 比较单步成本、epoch 成本和精度区间；
- 不用“方差减小一定更快”这种无条件表述。

#### 07.4 半光滑 Newton

第二版新增重点。教材先引入：

- B-subdifferential；
- Clarke generalized Jacobian；
- semismoothness；
- strong semismoothness。

然后构造 nonsmooth Newton-type 方法。

核心问题：

> 一阶非光滑算法容易得到低精度解，但高精度尾部可能很慢；半光滑 Newton 用广义导数恢复局部高速收敛。

必须保留：

- 超线性/二次局部速度依赖半光滑性与相应正则条件；
- globalized semismooth Newton 还需要线搜索/merit function 等机制；
- 不可把经典光滑 Newton 的 Hessian 理论原样复制。

**建议实验：** labs/19_optimization_stochastic_nonsmooth.py

两组：

1. LASSO：subgradient vs proximal gradient；
2. logistic finite-sum：full gradient vs SGD vs 一个方差减小版本。

可增加一个低维 semismooth equation 演示 generalized Jacobian Newton。

**完成标准：**

- 能写出次梯度算法及步长要求；
- 能解释 stochastic gradient 为什么便宜、为什么有噪声；
- 能解释 variance reduction 的动机；
- 能定义 generalized Jacobian 的角色；
- 能区分 semismooth Newton 的高精度局部区间和 SGD 的大规模低成本区间。

---

### Unit 08｜流形约束优化

**状态：独立页面及脚本已写，未运行；教材内容已登记，独立电子讲义 PDF 尚未确认。**

第二版第 7.4 节目录已确认包括：

- 7.4.1 流形基本概念；
- 7.4.2 典型流形；
- 7.4.3 最优性条件；
- 7.4.4 retraction 与 vector transport；
- 7.4.5 一阶优化方法；
- 7.4.6 二阶优化算法；
- 7.4.7 应用举例；
- 7.4.8 收敛性分析。

**资源边界：**

当前 27 主题 / 33 PDF 中没有单列“流形约束优化”讲义。自动维护只能通过真实目录或页面发现后登记，**禁止猜文件名**。

现有代码入口：

- ARNT：https://github.com/optsuite/ARNT
- OptM：https://github.com/optsuite/OptM

#### 08.1 从欧氏约束到流形

典型正交约束：

$$
X^TX=I.
$$

需要建立：

- manifold；
- tangent space；
- Riemannian metric；
- Riemannian gradient；
- Riemannian Hessian。

#### 08.2 Retraction

切空间方向 xi_k 通过

$$
x_{k+1}=R_{x_k}(t_k\xi_k)
$$

映回流形。

教材确认讨论 exponential map、Cayley transform、polar decomposition 和 QR-based retraction。

#### 08.3 一阶方法

Riemannian gradient descent：

$$
\xi_k=-\operatorname{grad} f(x_k),
$$

配合流形上的 Armijo / nonmonotone search 和 retraction。

#### 08.4 二阶方法

教材明确包含 Riemannian Newton、Riemannian trust-region 以及自适应正则化思路。

**建议实验：** labs/20_optimization_manifold.py

首选 sphere / Stiefel：

$$
\min_{\|x\|=1}x^TAx.
$$

比较 projected Euclidean step 与 Riemannian gradient + retraction，并与最小特征向量解析结果对照。

**完成标准：**

- 能写 sphere / Stiefel tangent space；
- 能解释 Euclidean gradient 与 Riemannian gradient；
- 能解释 projection 和 retraction 的区别；
- 能实现一个 Riemannian gradient method；
- 能把 Unit 03 的 KKT 与 manifold stationarity 联系起来；
- 不把“代码仓库存在”误写成“电子讲义已经发布”。

---

### Unit 09｜应用专题：至少三个端到端项目

**状态：三个独立项目实施稿及脚本已写，未运行；本节为原施工规格。**

统一链条：

$$
\text{问题}
\to
\text{模型}
\to
\text{结构判断}
\to
\text{算法选择}
\to
\text{停止准则}
\to
\text{验证}
\to
\text{失败分析}.
$$

候选项目：

1. compressed sensing / sparse recovery；
2. sparse regression；
3. low-rank matrix recovery / recommendation；
4. phase retrieval；
5. image TV / wavelet denoising；
6. logistic regression / SVM；
7. stochastic optimization；
8. optimal transport；
9. reinforcement learning。

每个项目必须包含：

- 数据或 synthetic data；
- 数学模型；
- loss 选择理由；
- regularizer 选择理由；
- convex / nonconvex 判断；
- optimality/KKT；
- 至少两种算法；
- objective / residual / optimality metric；
- wall-clock 与 iteration 都记录；
- 一个破坏关键假设的失败案例；
- 结果解释，不只给图。

最低交付建议：

- A：LASSO / compressed sensing；
- B：low-rank recovery / recommendation；
- C：phase retrieval 或 stochastic logistic regression。

---

### Unit 10｜Lean4 形式化验证

**状态：独立学习页已写，Lean 证明未编译；本节为原施工规格。**

资源：

- Optlib：https://github.com/optsuite/optlib
- ReasLab：https://reaslab.io/
- ReasBook：https://github.com/optpku/ReasBook
- M2F：https://github.com/optsuite/M2F
- SITA：https://github.com/chenyili0818/SITA
- lean-tools-mcp：https://github.com/optsuite/lean-tools-mcp
- CAM-Bench：https://github.com/optpku/CAM-Bench
- 中文入口：http://faculty.bicmr.pku.edu.cn/~wenzw/formal/index.html

#### 10.1 第一阶段：定义

优先形式化：

- convex set；
- convex function；
- subgradient；
- first-order optimality；
- Lipschitz gradient。

#### 10.2 第二阶段：简单算法

- gradient step；
- descent lemma；
- fixed-step convergence 的局部片段；
- projection / prox 的基本性质。

#### 10.3 第三阶段：复合算法

按照 Optlib 当前公开方向：

- proximal gradient；
- Nesterov；
- block coordinate descent；
- ADMM。

#### 10.4 验收标准

每个 Lean 条目必须对应：

1. 数学陈述；
2. 精确假设；
3. Lean definition；
4. theorem statement；
5. machine-checked proof；
6. 与纸笔证明的差异说明。

不能为了让 Lean 证明通过而静默强化或削弱原数学命题。



## 7. 实验与可执行产出总表

### 已完成

| 实验 | 对应 Unit | 主要观察对象 |
|---|---|---|
| labs/13_optimization_convexity.py | Unit 01 | 凸性抽样检查、条件数与梯度下降 |
| labs/14_optimization_modeling.py | Unit 02 | L2/L1 残差、ridge/LASSO |
| labs/15_optimization_optimality.py | Unit 03 | 驻点、KKT、Slater、duality gap |
| labs/16_optimization_unconstrained.py | Unit 04 | Gradient/BB/Newton/BFGS/TR、Gauss–Newton/LM |
| labs/17_optimization_constrained.py | Unit 05 | quadratic penalty、ALM、primal–dual central path |

### 新写待审与后续规划

| 建议实验 | 对应 Unit | 计划内容 |
|---|---|---|
| labs/18_optimization_composite.py | Unit 06 | ISTA/FISTA/BCD/ADMM on LASSO；已合并 |
| labs/19_optimization_stochastic_nonsmooth.py | Unit 07 | subgradient/SGD/SVRG 与标量半光滑 Newton；新增部分未运行 |
| labs/20_optimization_manifold.py | Unit 08 | sphere/Stiefel Riemannian gradient 与 QR retraction；新增部分未运行 |
| labs/21_optimization_sparse_recovery.py | Unit 09 A | ISTA/FISTA 稀疏重建；新写未运行 |
| labs/22_optimization_logistic.py | Unit 09 B | 全梯度/SGD 二分类；新写未运行 |
| labs/23_optimization_phase_retrieval.py | Unit 09 C | 谱/随机初始化的非凸相位恢复；新写未运行 |
| Lean4 证明目录 | Unit 10 | 尚未建立、尚未编译 |

> 表中 Unit 07–09 的脚本已写入但未执行；任何预设失败均待实测。Unit 10 仍无机器证明。



## 8. 统一学习模板与验收标准

每个主题至少产出九类信息：

1. **问题类**：变量、目标、约束；
2. **核心假设**：凸性、光滑性、Lipschitz、强凸、约束品性、随机假设等；
3. **最优性条件**：必要/充分/充要必须标记；
4. **算法更新式**；
5. **全局化机制**：line search / trust region / penalty / multiplier / projection / prox 等；
6. **收敛结论**及其前提；
7. **复杂度或局部速度**：只有来源支持时才记录；
8. **一个数值实验**；
9. **一个失败案例**：故意破坏关键假设。

一个 Unit 只有在以下条件同时满足时才标记“完成”：

- 能给出定义及非例；
- 能手推核心公式；
- 能解释结论依赖的假设；
- 能独立实现至少一个算法；
- 能写出停止准则；
- 能解释 failure mode；
- 能链接到至少一个实际模型；
- 能和前后单元建立依赖关系；
- 文档、代码、导航、HISTORY 一致。

## 9. 推荐实际学习顺序

### 第一遍：形成骨架

Unit 01 → 02 → 03 → 04 → 05 → 06。

### 第二遍：补非光滑与随机

回到 Unit 07，把 subgradient、SGD、variance reduction、semismooth Newton 纳入同一“低成本一阶 ↔ 高精度二阶广义 Newton”的图景。

### 第三遍：几何与应用

Unit 08 → Unit 09。

### 第四遍：形式化

Unit 10。只形式化已经理解并能纸笔证明的内容。

## 10. 维护与自动巡检

每轮巡检：

1. 检查 optbook 目录页；
2. 检查 27 个主题 / 33 个 PDF；
3. 检查程序页、新电子讲义、教材页；
4. 明确搜索“流形约束优化电子讲义”，但禁止猜 URL；
5. 检查 PKU 官方课程页、华文慕课；
6. 检查 Optlib / ReasLab / ReasBook / optsuite 等资源；
7. 记录 502/timeout 为“自动抓取不可达”，不删除用户确认链接；
8. 做 URL/ISBN/课程号/学分/版本/协助准备者 preservation QA；
9. 做 claim ledger / citation scope / semantic drift / repository QA；
10. 即使无实质变化，也追加 UTC+8 scan log；
11. 每轮只做一个 Git commit。

### Protected elements

不得静默改写：

- 9787040550351
- 978-7-04-055841-8
- 978-7-04-062561-5
- 2025-01-16
- 00130630
- 00136720
- 学分 3
- 27 个主题 / 33 个 PDF 的原 URL
- 每个讲义的协助准备者
- “自动抓取不可达 ≠ 资源失效”
- “流形约束优化讲义尚未真实发现”这一边界

## 11. 后续执行队列

1. **Unit 06**：草稿已合并，来源逐页复核待完成；
2. **Unit 07**：页面及次梯度/SGD/SVRG 脚本已写，标量半光滑 Newton 例已补；新例运行与来源逐页核对待完成；
3. **Unit 08**：流形几何页面及球面/Stiefel 教学脚本已写；来源逐页核对与运行待完成；
4. **Unit 09**：三个项目脚本已写；来源、运行记录与失败案例实测待完成；
5. **Unit 10**：学习页已写；Lean 命题与机器编译待完成。

Unit 06 草稿承接 Unit 02 的 LASSO/composite modeling、Unit 03 的 subgradient optimality 和 Unit 05 的 augmented Lagrangian/variable splitting，仍需按来源复核。

## 12. 文档使用方式

如果只读一个文件，就读本文件。

需要深入时再回到独立 Unit：

- Unit 01–05：当前独立文档是已落库版本；
- Unit 06：独立文档与实验是待审草稿；
- Unit 07–10：已有独立待审页面；本文件中的原施工规格保留作对照，尚未完成来源与运行验收；
- lecture index：本文件保留完整资源表，原索引页继续作为自动维护的机器友好清单。

本文件的目标不是取代独立教学页面，而是提供一个**单一事实入口**：一眼看清资源、进度、已完成内容、待完成范围、实验与验收标准。

