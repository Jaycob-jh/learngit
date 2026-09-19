# 拓扑：当长度和角度都不重要时，还剩下什么？

> **核心问题**：如果一个物体可以连续拉伸、弯曲，但不允许撕裂或粘合，哪些性质仍然不变？

## 从 Königsberg 七桥到“位置的几何”

1736 年 Euler 研究七桥问题：能否从某处出发，每座桥恰好经过一次？关键突破是他意识到桥的具体长度、河岸形状、角度都不重要，只需要保留：

- 陆地区域；
- 桥；
- 连接关系。

这是后来图论和拓扑思想的重要源头。问题第一次明确展示：有一种几何学研究的不是距离，而是“连接方式”。

## Euler characteristic

对凸多面体：

$$
V-E+F=2.
$$

这里 $V,E,F$ 分别是顶点、边、面。

后来这个量被推广到更一般的空间，成为 topological invariant 的原型。

## Poincaré：把拓扑变成系统学科

Poincaré 在 1895 年《Analysis Situs》中系统发展拓扑方法，并引入 fundamental group 等代数工具。

核心策略：

$$
\text{空间}
\longrightarrow
\text{群、同调等代数对象}.
$$

两个空间若拓扑结构不同，往往可以通过这些 invariants 区分。

## 什么叫“同一个拓扑空间”？

若存在连续双射且逆映射也连续，两个空间 homeomorphic。

经典直觉：咖啡杯和甜甜圈都只有一个“洞”，可在不撕裂粘合的连续变形中互相变换。

但注意：这个比喻只表达 homeomorphism 的直觉，不是拓扑的完整定义。

## 为什么今天重要？

### 数据分析
Topological Data Analysis 使用 persistent homology 追踪点云在不同尺度下的连通分支、洞和高维空腔。

### 机器人
机械臂配置空间可能具有复杂拓扑；路径规划本质上是在 configuration space 中寻找可行路径。

### 物理
拓扑绝缘体、topological phase、缺陷与 winding number 都用拓扑不变量描述“连续扰动下不会轻易消失”的结构。

### 神经科学与复杂系统
高维数据中的环、空腔和 connectivity 可以作为网络或状态空间的结构特征。

## 与九个核心公式的连接

- 微积分 → differential topology；
- Euler 公式 → winding number；
- Fourier / functional analysis → topological vector spaces；
- 复分析 → argument principle 与拓扑绕数；
- 数据分析 → probability + topology。

## 常见误解

**“拓扑就是甜甜圈和咖啡杯。”**  
这是入门类比。现代拓扑包括 point-set topology、algebraic topology、differential topology、geometric topology 等大量分支。

**“只要洞的数量一样就是同一个空间。”**  
不对。Euler characteristic 或 Betti numbers 都只是部分 invariants。

## 参考

- MacTutor, *A history of Topology*: https://mathshistory.st-andrews.ac.uk/HistTopics/Topology_in_mathematics/
- MacTutor, Henri Poincaré: https://mathshistory.st-andrews.ac.uk/Biographies/Poincare/
- Hatcher, *Algebraic Topology*.