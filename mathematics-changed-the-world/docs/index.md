# 数学如何改变世界

这个项目不是“著名公式排行榜”，而是一套 **数学思想史 × 数学原理 × 现代技术应用 × 可运行实验** 的中文知识库。

我们用三个问题组织全部资料：

1. **前世**：这个数学概念出现前，人们到底解决不了什么？
2. **今生**：核心定义/公式为什么这样写，它解决了什么结构性难题？
3. **来世**：它后来进入了哪些科学、工程、计算与 AI 系统？

---

## 第一层：九个核心入口

1. [微积分基本定理](core/01-calculus.md)
2. [Taylor 展开](core/02-taylor.md)
3. [Euler 公式](core/03-euler.md)
4. [Fourier 变换](core/04-fourier.md)
5. [散度定理](core/05-divergence.md)
6. [留数定理](core/06-residue.md)
7. [Bayes 公式](core/07-bayes.md)
8. [素数定理、对数积分与 Riemann](core/08-prime-number-theorem.md)
9. [Lebesgue 单调收敛](core/09-lebesgue.md)

这九章分别代表九种高度可迁移的思想：

$$
\boxed{
变化,\ 逼近,\ 旋转,\ 变换,\ 守恒,\ 奇点,\ 更新,\ 渐近,\ 极限
}
$$

---

## 第二层：数学主干地图

### 空间与结构
- [复数](branches/11-complex-numbers.md)
- [线性代数](branches/12-linear-algebra.md)
- [拓扑](branches/01-topology.md)
- [非欧几何](branches/14-non-euclidean-geometry.md)
- [微分几何](branches/02-differential-geometry.md)
- [群论与对称性](branches/15-group-symmetry.md)

### 连续变化
- [微分方程](branches/13-differential-equations.md)
- [泛函分析](branches/03-functional-analysis.md)
- [控制论](branches/06-control-theory.md)
- [混沌](branches/18-chaos.md)
- [数值分析](branches/09-numerical-analysis.md)

### 不确定性与信息
- [概率论](branches/20-probability.md)
- [随机过程](branches/08-stochastic-processes.md)
- [信息论](branches/16-information-theory.md)
- [博弈论](branches/05-game-theory.md)

### 离散、算法与表示
- [图论](branches/04-graph-theory.md)
- [可计算性](branches/17-computability.md)
- [凸优化](branches/19-convex-optimization.md)
- [小波](branches/07-wavelets.md)
- [Transformer 背后的数学](branches/10-transformer-math.md)

---

## 第三层：现实技术

可以从一个现实系统反向追数学：

### MRI
Fourier → linear algebra → inverse problem → optimization → numerical analysis。

### 手机通信
complex number → Fourier → probability → information theory → coding → optimization。

### 自动驾驶/机器人
linear algebra → differential equations → geometry → control → Bayes/Kalman → optimization。

### 现代 AI
linear algebra → calculus → probability → information theory → optimization → numerical analysis → attention。

### 天气与流体
calculus → PDE → divergence/conservation → numerical analysis → chaos → probability ensemble。

### 密码学
number theory → algebra → probability → complexity/computability。

---

## 课程体系

- [北大文再文最优化学习体系](courses/optimization-pku-wenzw.md) — 将教材、课程、代码、进阶算法与形式化入口串成可持续更新的课程路线，并显式记录来源等级与待复核项。

## 实验室

见 [数学实验室](../labs/README.md)。

从动画和数值实验开始，建议重点观察“什么时候理论开始失效”：

- Taylor 离展开中心太远；
- FFT 采样率太低导致 aliasing；
- Bayes 遇到错误 likelihood；
- Kalman filter 遇到错误噪声模型；
- 数值微分遇到 floating-point cancellation。

**理解边界条件，比只得到正确图形更重要。**

---

## 推荐阅读顺序

不知道从哪里开始时，先看 [学习路线](learning-paths.md)。

如果想理解整个项目的横向关系，看 [知识图谱](knowledge-graph.md)。

历史总览见 [时间线与应用地图](03-timeline-applications.md)。

资料出处见 [核心参考](04-references.md) 与 [现代主题参考](05-modern-references.md)。