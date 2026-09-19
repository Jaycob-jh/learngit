# 博弈论：当结果取决于“别人也在思考”时

> **核心问题**：如果我的最佳选择取决于你的选择，而你又在预测我的选择，该怎样建立数学模型？

## 与普通优化有什么不同？

普通优化：

$$
\min_x f(x).
$$

变量由一个决策者控制。

博弈中玩家 $i$ 的收益：

$$
u_i(a_1,\dots,a_n)
$$

同时依赖所有人的 action。

因此每个人都在优化，但优化目标互相耦合。

## 早期系统化

von Neumann 在 1928 年证明 two-player zero-sum game 的 minimax theorem。

1944 年 von Neumann 与 Morgenstern 的 *Theory of Games and Economic Behavior* 把博弈论推向经济学系统框架。

## Nash equilibrium

策略组合 $s^*=(s_1^*,\dots,s_n^*)$ 若满足：

$$
u_i(s_i^*,s_{-i}^*)
\ge
u_i(s_i,s_{-i}^*)
$$

对每个玩家 $i$ 和任何 unilateral deviation $s_i$ 成立，则为 Nash equilibrium。

直觉：

> 在其他人策略不变时，没有任何玩家能通过单独改变策略让自己更好。

## Nash equilibrium 不等于“社会最优”

Prisoner's dilemma 的典型教训就是：

- 每个个体的 equilibrium behavior；
- 整体最佳 outcome；

可能完全不同。

因此 equilibrium 是稳定性概念，不自动包含公平、效率或道德评价。

## 不完全信息

现实玩家不知道：

- 对方类型；
- 成本；
- 偏好；
- 私有信息。

Harsanyi 把 incomplete information 转换为 Bayesian game，为 auction、mechanism design、information economics 奠定重要基础。

## Sequential game

若行动有先后顺序，需要 extensive-form game、subgame perfect equilibrium 等概念。Selten 对 equilibrium refinement 作出关键贡献。

1994 年 Economics Prize 授予 Harsanyi、Nash、Selten，以表彰他们对 non-cooperative games equilibrium analysis 的先驱贡献。

## 现实应用

### 拍卖与广告
Google/广告竞价、频谱拍卖都涉及机制设计与策略行为。

### 市场
企业定价、竞争、进入退出。

### 网络
拥堵博弈与 routing。

### 安全
攻防策略、security games。

### 多智能体 AI
multi-agent reinforcement learning 中，各 agent 的 environment 包含其他正在学习的 agent，因此环境不是固定的。

### 进化
evolutionary game theory 研究策略比例如何在群体中变化。

## 与机器学习的连接

GAN 可以写成 min-max：

$$
\min_G\max_D V(D,G).
$$

强化学习中的 policy competition、self-play、adversarial training 都包含博弈结构。

但现实大模型训练不能简单归结为“一个 Nash equilibrium 问题”；只有特定互动结构才适合如此建模。

## 参考

- Nobel Prize 1994 summary: https://www.nobelprize.org/prizes/economic-sciences/1994/summary/
- von Neumann & Morgenstern, *Theory of Games and Economic Behavior*.
- Osborne & Rubinstein, *A Course in Game Theory*.