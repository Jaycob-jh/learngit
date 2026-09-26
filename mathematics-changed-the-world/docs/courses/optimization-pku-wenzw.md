# 北大文再文最优化学习体系：教材、课程、代码与形式化

> 采集状态：2026-09-26（UTC+8）。
>
> 原始入口 `http://faculty.bicmr.pku.edu.cn/~wenzw/optbook.html` 在本次抓取中返回 502 / 暂不可访问。这里将**原站 URL、北京大学官方页面、华文慕课页面、搜索索引/镜像证据**分层记录。暂时不可访问不等于资源不存在；未被独立验证的猜测路径不会列为事实。
>
> 编辑策略遵循 `Jaycob-jh/editorial-agent-framework` 的 `technical-docs` 路线：证据优先、轻量改写、数字/引用/版本/公式/代码严格保留；来源记录不做“润色式重写”。

## 1. 这套体系放在知识库的什么位置？

建议把它作为“凸优化”之后的一条课程化主线：

```text
数学分析 / 微积分
→ 线性代数 / 数值代数
→ 概率基础
→ 凸优化基础
→ 最优性理论
→ 无约束 / 约束 / 复合优化算法
→ 大规模与随机优化
→ 稀疏、低秩、最优传输、组合优化等数据问题
→ 可选：Lean4 形式化验证
```

它与本库已有内容的连接：

- [微积分基本定理](../core/01-calculus.md)
- [Taylor 展开](../core/02-taylor.md)
- [线性代数](../branches/12-linear-algebra.md)
- [数值分析](../branches/09-numerical-analysis.md)
- [概率论](../branches/20-probability.md)
- [凸优化](../branches/19-convex-optimization.md)
- [随机过程](../branches/08-stochastic-processes.md)
- [Transformer 背后的数学](../branches/10-transformer-math.md)

## 2. optbook 主页面所描述的教材结构

### 详细版

- 刘浩洋、户将、李勇锋、文再文：《最优化：建模、算法与理论》
- 高等教育出版社
- ISBN：`9787040550351`

主页面将详细版组织为四部分：

1. **基础知识**：范数、导数、凸集、凸函数、次梯度、共轭函数；附录补线性代数、数值代数、概率等。
2. **优化建模**：从应用问题到数学模型；覆盖线性规划、半正定规划、最小二乘、复合优化、矩阵优化、随机优化等模型。
3. **最优性理论**：讨论无约束、约束及相关模型的最优性条件。
4. **优化算法**：包括线搜索、梯度/次梯度、Newton、信赖域、非线性最小二乘、罚函数、增广 Lagrangian、内点法、近端梯度、Nesterov 加速、近端方法、坐标下降、对偶、ADMM、随机方法等。

主页面还列出压缩感知、低秩恢复、回归、logistic regression、SVM、相位恢复、字典学习、图像处理、深度学习、强化学习等建模/应用例子。

### 简明版

- 刘浩洋、户将、李勇锋、文再文：《最优化计算方法》
- ISBN：`978-7-04-055841-8`

简明版适合作为算法入口；详细版更适合作为“建模—理论—算法”完整主线。

## 3. 主页面外链清单

下面 12 个链接来自 optbook 主页面的可访问镜像/索引记录。由于原站本轮不可直连，状态栏只说明证据来源，不把“镜像出现”误写成“原站本轮已成功访问”。

| # | 类型 | URL | 本轮证据状态 |
|---|---|---|---|
| 1 | 详细版目录 PDF | http://bicmr.pku.edu.cn/~wenzw/optbook/opt1-content.pdf | 主页面镜像列出；原站待复核 |
| 2 | 简明版目录 PDF | http://bicmr.pku.edu.cn/~wenzw/opt2015/opt1-short-content.pdf | 主页面镜像列出；原站待复核 |
| 3 | 教材 PDF/资源入口 | http://bicmr.pku.edu.cn/~wenzw/optbook/opt1.pdf | 主页面镜像列出；原站待复核 |
| 4 | 高教社购买页 | http://www.hepmall.com/index.php/product-34415.html | 主页面镜像列出 |
| 5 | 微店 | https://weidian.com/item.html?itemID=4276223598 | 主页面镜像列出 |
| 6 | 京东 | https://item.jd.com/13064530.html | 主页面镜像列出 |
| 7 | 当当 | http://product.dangdang.com/29185022.html | 主页面镜像列出 |
| 8 | 读者问卷 | https://www.wenjuan.com/s/UZBZJvK0lr/ | 主页面镜像列出 |
| 9 | 勘误/反馈表 | https://docs.qq.com/form/page/DWWhDR2JySVFjQlNm | 主页面镜像列出 |
| 10 | 算法程序索引 | http://bicmr.pku.edu.cn/~wenzw/optbook/pages/index.html | 主页面镜像列出；原站待复核 |
| 11 | 2020 秋：凸优化 | http://bicmr.pku.edu.cn/~wenzw/opt-2020-fall.html | 主页面镜像列出；课程历史入口 |
| 12 | 2020 春：大数据分析中的算法 | http://bicmr.pku.edu.cn/~wenzw/bigdata2020.html | 主页面镜像列出；课程历史入口 |

主入口：

- http://faculty.bicmr.pku.edu.cn/~wenzw/optbook.html

## 4. 电子讲义：已确认可用的课程主线

用户补充并确认了一套可访问的 optbook 电子讲义清单，目前整理为 **27 个教学主题、33 个 PDF 链接**：

- [文再文 optbook 电子讲义索引](optimization-pku-wenzw-lectures.md)
- 目录入口：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/contents/contents.html

这批资源现在作为自动维护的**主抓取目标**。即使 optbook 首页在自动抓取环境中返回 502，也不影响继续使用这些确定 URL；失败只记录为“自动抓取不可达”，不会把链接误删。

### 第二版教材校正

本次用户提供的第二版教材 PDF 前言署于 **2025 年 2 月**。第二版明确新增流形约束优化、半光滑 Newton，并完善代码、网页、习题答案与电子讲义。当前用户提供的讲义清单已经包含半光滑 Newton，但暂未单列“流形约束优化”讲义，因此后续巡检把它设为明确待发现项。

## 5. 被独立索引到的 optbook 内部子页

以下路径除主页面链接外，还被搜索索引或学术材料独立指向，因此单独登记：

- 目录页：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/contents/contents.html
- SGD：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/sgd.html
- Adam：https://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/Adam.html
- FISTA / Nesterov（LASSO）：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_proxg/LASSO_Nesterov_inn.html
- ADMM demo：http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_admm/demo_admm.html

这不是对 `pages/` 的“已证明穷尽”。原站恢复可爬取后，自动巡检会继续递归核对；未验证的 AdaGrad、RMSProp 等猜测路径不会提前写入。

## 6. 课程体系

### 6.1 北京大学《最优化方法》

北京大学数学科学学院课程页：

- https://math.pku.edu.cn/bks/sykc/148761.htm
- 课程号：`00130630`
- 学期：秋季
- 学分：`3`
- 先修：数学分析、数值代数

课程主线可以压缩成四层：

1. **凸分析与模型**：凸集、凸函数、线性规划、SOCP、SDP；
2. **理论**：对偶性与最优性条件；
3. **经典数值算法**：线搜索、梯度、次梯度、Newton、拟 Newton、信赖域、非线性最小二乘；
4. **约束与复合优化**：罚函数、增广 Lagrangian、近端/近端梯度、Nesterov、对偶、ADMM、坐标下降、半光滑 Newton。

华文慕课课程页：

- https://www.chinesemooc.org/web/course_detail.php?courseid=5063
- 2023 课程历史页：http://faculty.bicmr.pku.edu.cn/~wenzw/opt-2023-fall.html

建议做法：把本库 [凸优化](../branches/19-convex-optimization.md) 当作概念入口，再用这门课补齐完整算法链。

### 6.2 北京大学《大数据分析中的算法》

北京大学数学科学学院课程页：

- https://math.pku.edu.cn/bks/sykc/148668.htm
- 课程号：`00136720`
- 学期：秋季
- 学分：`3`
- 先修：数学分析、数值代数

课程把优化算法推进到数据与计算问题，包括：

- 线性/半正定优化与对偶；
- 单纯形与内点方法；
- 压缩感知与稀疏优化；
- 最优传输；
- 整数规划；
- 图与网络流；
- 次模优化；
- 随机数值线性代数；
- 随机优化；
- 高维降维；
- 推荐系统与低秩恢复；
- 相位恢复；
- 强化学习。

华文慕课课程页：

- https://www.chinesemooc.org/web/course_detail.php?courseid=4974
- 2020 历史页：http://faculty.bicmr.pku.edu.cn/~wenzw/bigdata2020.html

搜索索引还显示一个 2025 春课程入口：

- http://faculty.bicmr.pku.edu.cn/~wenzw/bigdata2025.html

但本轮无法从原站直接打开，所以该条目前标记为**二级证据，待原站恢复后复核**。

### 6.3 更新教材入口：《最优化方法与理论》

北京大学“101 计划”教材页：

- https://math101.pku.edu.cn/hxjc/qb/3489f4fc70974d0da96ce949939fd3b8.htm
- 文再文、袁亚湘：《最优化方法与理论》
- ISBN：`978-7-04-062561-5`

高等教育出版社当前产品页：

- https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=66be39c274ce561611bda4a1
- 出版时间：`2025-01-16`
- 版次：1

它可作为 optbook 体系之后的更新/进阶教材入口；本页不假定它替代旧教材，而把它作为后续资源并列保留。出版社页与北大“101 计划”页对作者和 ISBN 的记录一致。

### 6.4 可选研究线：Lean4 形式化

核心入口：

- Optlib：https://github.com/optsuite/optlib
- ReasLab：https://reaslab.io/
- ReasBook：https://github.com/optpku/ReasBook
- 中文安装/训练入口：http://faculty.bicmr.pku.edu.cn/~wenzw/formal/index.html

Optlib 当前公开说明把凸分析、最优性条件和算法收敛统一纳入 Lean4 形式化，已经列出梯度下降、近似点梯度 / Nesterov、分块坐标下降和 ADMM 等算法方向；其教材形式化项目还覆盖数值线性代数和高维概率。当前公开工具链还包括：

- M2F：https://github.com/optsuite/M2F
- SITA：https://github.com/chenyili0818/SITA
- lean-tools-mcp：https://github.com/optsuite/lean-tools-mcp

这些资源适合放在“已经会推导和实现算法”之后，用来训练机器可检查的定义、定理和收敛证明；它们不替代常规分析与数值训练。

### 6.5 代码资源：流形优化与正交约束

文再文公开的 optsuite 代码组织：

- https://github.com/optsuite
- ARNT：https://github.com/optsuite/ARNT
- OptM：https://github.com/optsuite/OptM

其中 ARNT 是面向 Riemannian manifold optimization 的 MATLAB 软件，OptM 面向正交约束优化。它们可作为第二版“流形约束优化”章节的算法实现补充；**这里仅把它们作为代码入口，不把它们当作“流形约束优化电子讲义已经存在”的证据**。

## 7. 系统学习入口

资源索引已经具备后，下一阶段转向课程化学习：

- [系统学习路线](optimization-pku-wenzw-study-roadmap.md)
- [Unit 01｜最优化的基础语言](optimization-pku-wenzw-study-units/01-foundations.md)
- [Unit 02｜优化建模与典型优化问题](optimization-pku-wenzw-study-units/02-modeling.md)
- [Unit 03｜最优性理论](optimization-pku-wenzw-study-units/03-optimality.md)
- [Unit 04｜无约束优化算法](optimization-pku-wenzw-study-units/04-unconstrained.md)
- 配套实验：`labs/13_optimization_convexity.py`、`labs/14_optimization_modeling.py`、`labs/15_optimization_optimality.py`、`labs/16_optimization_unconstrained.py`

学习路线按“问题与基础 → 建模 → 最优性 → 无约束 → 约束 → 复合 → 随机/非光滑 → 流形 → 应用 → 形式化”组织，不要求按照 PDF 文件编号机械阅读。

## 8. 建议的学习任务顺序

### 阶段 A｜会识别问题

目标：

- 给定实际问题，能写出变量、目标函数、约束；
- 能区分 LP / least squares / composite / stochastic / matrix optimization；
- 能判断“凸性”为什么改变算法保证。

### 阶段 B｜会推理论

目标：

- 熟悉凸集/凸函数、次梯度、共轭；
- 能写一阶最优性条件；
- 能解释 Lagrange duality、KKT、强/弱对偶；
- 保留条件：不要把“在适当条件下”改写成无条件结论。

### 阶段 C｜会实现算法

至少独立实现并比较：

- gradient / subgradient；
- Newton / quasi-Newton / trust-region；
- proximal gradient；
- Nesterov accelerated gradient / FISTA；
- ADMM；
- coordinate descent；
- stochastic gradient。

每个算法都记录：

1. 目标模型；
2. 收敛条件；
3. 每步计算代价；
4. 停止准则；
5. 一个故意破坏条件的反例实验。

### 阶段 D｜会把优化用于数据问题

从下面选 2–3 个做完整小项目：

- compressed sensing；
- sparse regression；
- low-rank recovery / recommendation；
- optimal transport；
- phase retrieval；
- stochastic optimization；
- reinforcement learning。

### 阶段 E｜可选：形式化验证

选择一个小定理或算法步骤，用 Lean4 写出：

- 定义；
- 假设；
- 结论；
- 机器可检查证明。

## 9. 证据与保真台账

这是按 `editorial-agent-framework` 对“来源型技术文档”做的最小 claim ledger。

| ID | 关键陈述 | 类型 | 证据等级 | 风险/处理 |
|---|---|---|---|---|
| C1 | 详细版教材及 ISBN `9787040550351` | 描述性 | 高 | 北大/BICMR 页面与主页面镜像交叉核对；数字严格保留 |
| C2 | 《最优化方法》课程号 `00130630`、3 学分及课程模块 | 描述性 | 高 | 北京大学数学科学学院官方页 |
| C3 | 《大数据分析中的算法》课程号 `00136720`、3 学分及课程模块 | 描述性 | 高 | 北京大学数学科学学院官方页 |
| C4 | `bigdata2025.html` 及其课程主题 | 描述性 | 中 | 当前仅搜索索引/二级页面可见；原站恢复后复核 |
| C5 | optbook 的 12 个主页面外链 | 来源记录 | 中高 | 可访问主页面镜像逐项记录；原始域本轮 502 |
| C6 | 5 个算法/目录内部子页 | 来源记录 | 中 | 独立搜索/文献索引到；不据此推断未出现的路径 |
| C7 | optlib 的 Lean4 方向 | 描述性 | 高 | 项目仓库与公开说明 |
| C8 | 27 个讲义主题 / 33 个 PDF URL | 来源记录 | 高（用户提供并确认可访问） | 保留原 URL 与协助准备者；自动抓取 502 不等同失效 |
| C9 | 第二版新增流形约束优化、半光滑 Newton 并完善教学资源 | 描述性 | 高 | 用户提供的第二版 PDF，2025-02 前言 |
| C10 | 《最优化方法与理论》ISBN `978-7-04-062561-5`、版次 1、出版时间 `2025-01-16` | 描述性 | 高 | 高等教育出版社产品页；北大“101 计划”页交叉核对作者与 ISBN |
| C11 | Optlib / ReasLab / ReasBook 及 M2F、SITA、lean-tools-mcp 构成当前公开形式化资源链 | 来源记录 | 高 | Optlib 当前 README 逐项链接 |
| C12 | ARNT / OptM 是 optsuite 下的流形优化与正交约束公开代码资源 | 来源记录 | 高 | optsuite GitHub 公开仓库；不据此推断流形讲义 PDF 已发布 |

### Protected elements

自动编辑时不得静默改变：

- `9787040550351`
- `978-7-04-055841-8`
- `978-7-04-062561-5`
- `2025-01-16`
- `00130630`
- `00136720`
- 本页所有 URL
- 课程学分 `3`
- “2025 课程入口仅二级证据、待复核”这一不确定性边界

## 10. 自动巡检约定

每次巡检执行：

1. 重新访问 optbook 主入口与本页登记的全部链接；
2. 若原站恢复，递归检查主页面和 `pages/` 中可发现的子链接；
3. 搜索新的官方课程页、更新教材页、代码/形式化资源；
4. 新信息必须记录来源等级；不能通过命名规律猜 URL；
5. 对数字、ISBN、课程号、URL、版本和不确定性做 preservation QA；
6. 有变化时更新本页及必要的导航/参考/学习路线；
7. 无内容变化时也在 [巡检日志](optimization-pku-wenzw-scan-log.md) 追加一行，以形成每小时运行记录；
8. 每轮只提交一个 Git commit。

> 自动巡检是“发现变化 + 保留证据边界”的维护流程，不把网页可访问性当成资源真实性的唯一判断。
