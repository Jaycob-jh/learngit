# Unit 07–10｜资料、页面与验证队列

> 2026-09-27 建立初版，随后补入 Unit 09 来源页码与实测证据。按已有 [optbook 讲义索引](optimization-pku-wenzw-lectures.md)、[课程资源页](optimization-pku-wenzw.md)和[学习路线](optimization-pku-wenzw-study-roadmap.md)建立映射；各行分别记录已阅读与待验证状态。总库此前的 [120 行覆盖基线](../coverage-matrix.md)仍为当时快照，不代表全部资料已审读。

| 资料或模型入口 | 已阅读证据 | 对应页面/实验 | 待验证项 |
|---|---|---|---|
| [次梯度](optimization-pku-wenzw-lectures.md)、[次梯度算法](optimization-pku-wenzw-lectures.md)，教材第二版 6.3 | 仅有既有目录和索引；本批未逐页阅读 | [Unit 07](optimization-pku-wenzw-study-units/07-stochastic-nonsmooth.md)、`labs/19_optimization_stochastic_nonsmooth.py` | 具体 PDF 页码、步长条件、定理适用范围；运行输出 |
| [随机优化、半光滑 Newton](optimization-pku-wenzw-lectures.md)，教材第二版 8.7–8.8 | 仅有既有目录和索引；本批未逐页阅读 | Unit 07；脚本包含随机优化比较和独立构造的标量半光滑 Newton 例 | 有限和抽样假设、方差减小速度前提、讲义中广义 Jacobian 与局部正则性；新例尚未运行 |
| 教材第二版 7.4 流形约束优化；[ARNT](https://github.com/optsuite/ARNT)、[OptM](https://github.com/optsuite/OptM) | 章节与仓库入口已由既有资源页登记；本批未读正文/代码 | [Unit 08](optimization-pku-wenzw-study-units/08-manifold.md)、`labs/20_optimization_manifold.py` 的球面和 Stiefel 例 | 度量、QR retraction 约定、数值结果、代码版本；独立 PDF 仍未发现 |
| [教材第二版 PDF](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/opt2.pdf) §3.2.3 LASSO、§8.1.2 近端梯度、§8.2 FISTA | 已核正文书页 90–92／PDF 108–110、384／402、394／412；脚本损失另除以样本数 | [Unit 09 项目 A](optimization-pku-wenzw-study-units/09-applications.md)、[六组原始记录](https://github.com/Jaycob-jh/math-atlas/tree/math-changed-world/mathematics-changed-the-world/labs/records/unit09) | 单一种子近共线时系数幅值恢复差；跨种子稳定性与真实数据待验证 |
| 同 PDF §3.3 logistic、§8.7.1 SGD、§8.7.2 应用 | 已核书页 93–94／PDF 111–112、498／516、505／523；脚本加截距、取平均损失 | [Unit 09 项目 B](optimization-pku-wenzw-study-units/09-applications.md)、同批原始记录 | 特征放大联合改变条件与相对正则作用；一般化结论待验证 |
| 同 PDF §3.6 相位恢复 | 已核书页 100–102／PDF 118–120，式 (3.6.4)；脚本噪声与目标缩放另定 | [Unit 09 项目 C](optimization-pku-wenzw-study-units/09-applications.md)、同批原始记录 | 欠采样与高噪声联合压力失效；各因素贡献与跨种子稳定性待验证 |
| [Optlib](https://github.com/optsuite/optlib)、[ReasBook](https://github.com/optpku/ReasBook)、[ReasLab](https://reaslab.io/) | 仅有既有资源登记；本批未读取当前代码 | [Unit 10](optimization-pku-wenzw-study-units/10-formalization.md) | Lean/toolchain 版本、精确导入、编译日志、纸笔与机器命题一致性 |

Unit 07–08 页面与脚本仍待来源和运行核验；Unit 09 项目 A–C 已有[来源页码、实际运行与失败案例](optimization-pku-wenzw-unit09-run-log.md)，但仅覆盖单一种子的合成数据；Unit 10 尚无机器编译证据。
