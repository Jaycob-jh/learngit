# 微分方程：如果知道“怎样变化”，能否推演“将来怎样”？

> **核心问题**：自然规律经常不给你位置本身，而只告诉你变化率与当前状态的关系。

## 从微积分到动力规律

Newton 力学的自然写法：

\[
m\frac{d^2x}{dt^2}=F(x,t).
\]

给定：

- differential law；
- initial conditions；

就尝试求完整 trajectory。

这使 differential equation 成为近代科学的核心语言。

## ODE

ordinary differential equation 只有一个 independent variable，例如：

\[
\frac{dx}{dt}=f(x,t).
\]

典型问题：

- existence；
- uniqueness；
- stability；
- long-term behavior。

## PDE

若未知量依赖多个变量：

\[
u(x,t)
\]

会出现 partial derivatives。

三大经典原型：

### Heat

\[
u_t=\alpha u_{xx}.
\]

### Wave

\[
u_{tt}=c^2u_{xx}.
\]

### Laplace

\[
\nabla^2u=0.
\]

它们分别体现：

- diffusion；
- propagation；
- equilibrium。

## 求出 closed form 不是唯一目标

很多 nonlinear differential equations 没有漂亮解析解。

现代研究更关注：

- solution 是否存在；
- 是否唯一；
- stability；
- bifurcation；
- qualitative phase portrait；
- numerical approximation。

这就是 dynamical systems 的兴起。

## Phase space

对

\[
\dot x=f(x)
\]

不一定直接求 \(x(t)\)，可以研究 state space 中 trajectory 的结构：

- fixed point；
- limit cycle；
- attractor；
- stable/unstable manifold。

这条路线最终通向 chaos theory。

## PDE 与现代技术

- weather / climate；
- aerodynamics；
- electromagnetic simulation；
- semiconductor；
- biomechanics；
- medical imaging；
- material mechanics；
- acoustics。

## Neural ODE 与 scientific ML

现代机器学习也重新把 neural network 与 differential equations 联系：

- Neural ODE；
- physics-informed neural networks；
- diffusion / SDE models；
- continuous normalizing flows。

但“用神经网络求 PDE”并不消除传统 numerical analysis；稳定性、误差与边界条件仍然存在。

## 与九个核心公式连接

微积分 → differential equations。  
Taylor → numerical integrators。  
Fourier → solve linear PDE in frequency domain。  
散度 → conservation PDE。  
Lebesgue/functional analysis → weak solution。  
chaos → nonlinear ODE。

## 参考

- Boyce & DiPrima, *Elementary Differential Equations*.
- Evans, *Partial Differential Equations*.
- MacTutor historical overview: https://mathshistory.st-andrews.ac.uk/HistTopics/History_overview/