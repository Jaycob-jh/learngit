# 图论：把世界压缩成“节点 + 关系”

> **核心问题**：当对象之间“谁和谁连接”比它们的位置更重要时，怎样进行数学推理？

## 起点：七桥问题

Euler 在 1736 年处理 Königsberg bridges 时，把陆地压成 vertices，把桥压成 edges。

现实地图被抽象成：

\[
G=(V,E).
\]

这个抽象非常激进：距离、角度、桥的长度全部丢掉，只保留 connectivity。

## Euler path

Euler path：每条 edge 恰走一次。

对连通图，存在 Euler circuit 的经典条件是所有 vertex degree 都是偶数；存在非闭 Euler trail 时恰有两个奇度顶点。

这说明一个全局旅行问题可以由局部 degree 信息判断。

## 图论如何成熟？

19 世纪图结构进入化学、组合数学等领域。Sylvester 在 1878 年把 graph 一词用于与化学结构有关的表示。20 世纪 König 等推动系统化；随后 Erdős 等人的组合方法使图论成为庞大独立领域。

## 树

Tree 是无环连通图。

对 \(n\) 个顶点的树：

\[
|E|=n-1.
\]

树结构无处不在：

- 文件系统；
- 决策树；
- 编译器 AST；
- 系统发育树；
- hierarchical clustering。

## 最短路径

Dijkstra、Bellman–Ford、A* 等算法解决不同条件下的 shortest path。

这把“图论”连接到 algorithmics：

\[
\text{结构}
+
\text{复杂性}
+
\text{数据结构}.
\]

## 网络科学

现实网络通常不是单纯规则图：

- social network；
- brain connectome；
- internet；
- transportation；
- protein interaction。

需要研究：

- degree distribution；
- community；
- centrality；
- diffusion；
- robustness。

## PageRank 的数学

网页作为节点，超链接作为边。PageRank 本质上与随机游走和 Markov chain 的 stationary distribution 有关。

因此图论又与概率论、线性代数相连。

## Graph Neural Networks

GNN 常把邻居信息聚合：

\[
h_v^{(l+1)}
=
\operatorname{UPDATE}
\left(
h_v^{(l)},
\operatorname{AGG}_{u\in N(v)}h_u^{(l)}
\right).
\]

它把“学习”从网格数据扩展到任意 graph structure。

## 常见应用

- 路由导航；
- 推荐系统；
- 社交关系；
- 分子性质预测；
- fraud detection；
- 脑连接网络；
- dependency analysis。

## 与拓扑的关系

Euler 七桥同时被视作 graph theory 和 topology 的重要源头。

图论通常研究离散有限结构；拓扑研究更一般的连续空间，但二者在 simplicial complexes、network topology、TDA 中重新汇合。

## 参考

- MacTutor, *A history of Topology*: https://mathshistory.st-andrews.ac.uk/HistTopics/Topology_in_mathematics/
- MacTutor, Sainte-Laguë / graph history: https://mathshistory.st-andrews.ac.uk/Extras/Les_reseaux/
- Diestel, *Graph Theory*.