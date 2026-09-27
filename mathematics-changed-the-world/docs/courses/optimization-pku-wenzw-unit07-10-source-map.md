# Unit 07–10｜资料、页面与验证队列

> 2026-09-27 推送批次。按已有 [optbook 讲义索引](optimization-pku-wenzw-lectures.md)、[课程资源页](optimization-pku-wenzw.md)和[学习路线](optimization-pku-wenzw-study-roadmap.md)建立映射。本批遵照 Hai 的安排，不重新核验来源、不执行脚本；“已登记”与“已阅读”严格区分。总库此前的 [120 行覆盖基线](../coverage-matrix.md)仍为当时快照。

| 资料或模型入口 | 已阅读证据 | 对应页面/实验 | 待验证项 |
|---|---|---|---|
| [次梯度](optimization-pku-wenzw-lectures.md)、[次梯度算法](optimization-pku-wenzw-lectures.md)，教材第二版 6.3 | 仅有既有目录和索引；本批未逐页阅读 | [Unit 07](optimization-pku-wenzw-study-units/07-stochastic-nonsmooth.md)、`labs/19_optimization_stochastic_nonsmooth.py` | 具体 PDF 页码、步长条件、定理适用范围；运行输出 |
| [随机优化、半光滑 Newton](optimization-pku-wenzw-lectures.md)，教材第二版 8.7–8.8 | 仅有既有目录和索引；本批未逐页阅读 | Unit 07；脚本只覆盖随机优化教学比较 | 有限和抽样假设、方差减小速度前提、广义 Jacobian 与局部正则性；半光滑数值例尚未写入 |
| 教材第二版 7.4 流形约束优化；[ARNT](https://github.com/optsuite/ARNT)、[OptM](https://github.com/optsuite/OptM) | 章节与仓库入口已由既有资源页登记；本批未读正文/代码 | [Unit 08](optimization-pku-wenzw-study-units/08-manifold.md)、`labs/20_optimization_manifold.py` | 度量和 retraction 约定、数值结果、代码版本；独立 PDF 仍未发现 |
| 课程的压缩感知、LASSO、近端优化入口 | 仅有既有课程页/单元；本批未逐页阅读新来源 | [Unit 09 项目 A](optimization-pku-wenzw-study-units/09-applications.md)、`labs/21_optimization_sparse_recovery.py` | 来源页码、数据与噪声设定、重建和失败输出 |
| 课程的 logistic regression、有限和/随机优化入口 | 同上 | Unit 09 项目 B、`labs/22_optimization_logistic.py` | 模型与梯度约定、数据划分、实际泛化与失败输出 |
| 课程的相位恢复、非凸优化入口 | 同上 | Unit 09 项目 C、`labs/23_optimization_phase_retrieval.py` | 来源公式、初始化条件、符号不变误差与失败输出 |
| [Optlib](https://github.com/optsuite/optlib)、[ReasBook](https://github.com/optpku/ReasBook)、[ReasLab](https://reaslab.io/) | 仅有既有资源登记；本批未读取当前代码 | [Unit 10](optimization-pku-wenzw-study-units/10-formalization.md) | Lean/toolchain 版本、精确导入、编译日志、纸笔与机器命题一致性 |

本批新写页面与脚本的存在只说明可供审阅。项目 A–C 的运行记录在[空白模板](optimization-pku-wenzw-unit09-run-log.md)中保留待填；没有合成“运行成功”或“失败已观察”的记录。
