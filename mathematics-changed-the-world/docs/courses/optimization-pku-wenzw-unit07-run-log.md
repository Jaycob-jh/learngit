# Unit 07｜半光滑 Newton 数值例运行记录

> 本文件是待填记录，不包含脚本运行结果。教学构造见 [Unit 07](optimization-pku-wenzw-study-units/07-stochastic-nonsmooth.md)；脚本为 `labs/19_optimization_stochastic_nonsmooth.py`。参考范围为既有讲义索引主题 27 与教材第二版 8.8，尚未逐页核对。

## 解析基准

标量 LASSO 目标 $\tfrac12(2x-1)^2+0.3|x|$ 的正半轴候选点为 $x=0.425$。方程 $H(x)=x-S_{0.03}(0.6x+0.2)=0$ 的活动区 Jacobian 为 $0.4$。这些数值由本页代数定义直接推导，**不是脚本输出**。

独立失败例 $Q(x)=\max(x,0)-1$ 在 $x_0=-1$ 处有 $Q(x_0)=-1$、导数 $0$，因此经典 Newton 线性步骤不可解。这是事先构造的退化情形，实际脚本是否按预期记录仍待检查。

## 运行时填写

| 项目 | 待填内容 |
|---|---|
| 日期、commit、Python/NumPy 版本 | 待运行 |
| 命令 | `python labs/19_optimization_stochastic_nonsmooth.py --iterations 120 --csv <output.csv>` |
| 随机种子与全部参数 | 待运行 |
| 标量 proximal 与半光滑 Newton 的逐步 $x,|H(x)|,V_k$ | 待运行；CSV 预留 `state`、`metric` 和 `generalized_jacobian` 列 |
| 是否到达解析基准及所需步数 | 待运行 |
| 奇异导数例的实际停止行为 | 待运行 |
| 原始 CSV 路径、失败日志、解释 | 待运行 |
| 来源页码与讲义定理条件 | 待逐页核对 |

本例只演示分段仿射的低维机制；不能用于比较一般半光滑 Newton 与随机优化方法的速度。
