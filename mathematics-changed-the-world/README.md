# 数学如何改变世界
## Mathematics Changed the World

一套中文 **数学思想史 × 核心原理 × 现实应用 × Python 实验** 知识库。

它从九个经典数学公式/定理出发，但目标不是做“公式排行榜”，而是回答四件事：

1. **前世**：这个理论出现前，人类卡在什么问题上？
2. **诞生**：哪些人物、争论和前驱工作共同让它成熟？
3. **原理**：核心公式为什么这样写，背后的结构是什么？
4. **今生**：它今天如何进入物理、工程、通信、医学成像、统计、计算机与 AI？

---

## 当前规模

### 9 个核心专题长章

| # | 专题 | 思想关键词 | 现实落点 |
|---|---|---|---|
| 1 | [微积分基本定理](docs/core/01-calculus.md) | 变化 ↔ 累积 | 力学、PDE、优化 |
| 2 | [Taylor 展开](docs/core/02-taylor.md) | 局部逼近 | 数值计算、控制、优化 |
| 3 | [Euler 公式](docs/core/03-euler.md) | 复数 ↔ 旋转 ↔ 波 | 电路、通信、量子 |
| 4 | [Fourier 变换](docs/core/04-fourier.md) | 时空域 ↔ 频域 | MRI、音视频、通信 |
| 5 | [散度定理](docs/core/05-divergence.md) | 内部 ↔ 边界 | 电磁、流体、守恒律 |
| 6 | [留数定理](docs/core/06-residue.md) | 全局积分 ↔ 奇点 | 复分析、系统、物理 |
| 7 | [Bayes 公式](docs/core/07-bayes.md) | 证据更新 | 统计、诊断、AI |
| 8 | [素数 / li(x) / Riemann](docs/core/08-prime-number-theorem.md) | 局部无序 ↔ 宏观规律 | 数论、密码学背景 |
| 9 | [Lebesgue 单调收敛](docs/core/09-lebesgue.md) | 极限 ↔ 积分 | 概率、Fourier、PDE |

每一章都有：历史前因、推导思路、数学意义、现实应用、常见误解、关联主题和实验入口。

### 20 条数学主干

**空间与结构**

- [拓扑](docs/branches/01-topology.md)
- [微分几何](docs/branches/02-differential-geometry.md)
- [泛函分析](docs/branches/03-functional-analysis.md)
- [图论](docs/branches/04-graph-theory.md)
- [博弈论](docs/branches/05-game-theory.md)
- [复数](docs/branches/11-complex-numbers.md)
- [线性代数](docs/branches/12-linear-algebra.md)
- [非欧几何](docs/branches/14-non-euclidean-geometry.md)
- [群论与对称性](docs/branches/15-group-symmetry.md)

**连续、动态与计算**

- [控制论](docs/branches/06-control-theory.md)
- [小波](docs/branches/07-wavelets.md)
- [随机过程](docs/branches/08-stochastic-processes.md)
- [数值分析](docs/branches/09-numerical-analysis.md)
- [微分方程](docs/branches/13-differential-equations.md)
- [混沌](docs/branches/18-chaos.md)
- [凸优化](docs/branches/19-convex-optimization.md)

**概率、信息与现代计算**

- [Transformer 背后的数学](docs/branches/10-transformer-math.md)
- [信息论](docs/branches/16-information-theory.md)
- [可计算性](docs/branches/17-computability.md)
- [概率论](docs/branches/20-probability.md)

### 12 个可运行实验

见 [labs/README.md](labs/README.md)。

包括：

- 微积分累积函数；
- Taylor 动画；
- Euler phasor 动画；
- FFT 频谱；
- 散度/通量；
- 留数数值积分；
- Bayes sequential update；
- 素数计数与 li(x)；
- 单调收敛；
- Kalman filter；
- wavelet 多尺度分解；
- scaled dot-product attention heatmap。

---

## 从哪里开始？

### 我想理解“数学为什么会这样发展”
看 [学习路线](docs/learning-paths.md) 的“数学世界观”路线。

### 我做信号 / MRI / BCI / 工程
走：

复数 → Euler → 线性代数 → Fourier → 概率 → 随机过程 → 控制 → 小波 → 数值分析。

### 我做 AI / ML
走：

线性代数 → 微积分 → Taylor → 概率/Bayes → 信息论 → 优化 → 数值分析 → Transformer。

### 我想看所有主题怎样连接
直接看 [知识图谱](docs/knowledge-graph.md)。

---

## 三个入口

- [📚 文档首页](docs/index.md)
- [🗺️ 知识图谱](docs/knowledge-graph.md)
- [🧪 Python 实验室](labs/README.md)

历史纵览：
- [数学时间线与现实应用地图](docs/03-timeline-applications.md)

资料来源：
- [核心主题参考](docs/04-references.md)
- [现代主题参考](docs/05-modern-references.md)

开发计划：
- [ROADMAP](ROADMAP.md)

---

## 本地运行文档站

\`\`\`bash
cd mathematics-changed-the-world
python -m venv .venv
source .venv/bin/activate
pip install mkdocs-material
mkdocs serve
\`\`\`

浏览器打开 MkDocs 给出的本地地址即可。

实验环境：

\`\`\`bash
pip install -r requirements-labs.txt
python labs/04_fourier_decomposition.py
\`\`\`

---

## 项目原则

### 1. 不写“单一天才神话”
重大理论通常有前驱、并行发现、符号改进和后续严格化。

### 2. 区分数学对象、算法和实现
例如：

- Fourier transform ≠ DFT ≠ FFT；
- probability theorem ≠ statistical model；
- attention definition ≠ GPU implementation。

### 3. 区分“数学联系”与“直接工程应用”
例如 RSA 使用大素数，但不能简单说“RSA 直接使用素数定理”。

### 4. 公式必须回到问题
每个公式都要回答：

> 为什么当时需要它？它压缩了哪一类问题？换了什么表示？

---

## 核心观点

数学改变世界，往往不是因为某个公式本身“神奇”，而是因为它发明了一种新的表示语言：

- 把运动表示成导数；
- 把复杂函数表示成局部多项式；
- 把波表示成频率；
- 把高维关系表示成向量和矩阵；
- 把不确定性表示成概率分布；
- 把对称性表示成群；
- 把连续形状表示成拓扑不变量；
- 把信息表示成熵；
- 把算法本身变成数学研究对象。

> **选对表示，往往就是解决问题的一半。**
