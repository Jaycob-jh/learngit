# 控制论：不是“预测系统”，而是让系统按目标行动

> **核心问题**：一个会随时间演化的系统，怎样利用反馈，把它稳定、跟踪到目标、抵抗扰动？

## 从自动调节到数学控制

控制思想早于现代数学：蒸汽机 governor、航海舵机、机械调速器都依赖 feedback。

20 世纪通信和电子工程发展后，控制理论逐渐形成两条经典路线：

1. **频域方法**：Nyquist、Bode 等；
2. **状态空间方法**：Kalman 等。

两条路线分别擅长不同问题，今天仍同时存在。

## 状态空间

连续线性系统：

$
\dot x(t)=Ax(t)+Bu(t),
$

$
y(t)=Cx(t)+Du(t).
$

其中：

- $x$：内部 state；
- $u$：control input；
- $y$：observation；
- $A,B,C,D$：系统结构。

这个写法把 ODE 与线性代数结合起来。

## 稳定性

若无输入：

$
\dot x=Ax.
$

解涉及

$
e^{At}.
$

矩阵 $A$ 的 eigenvalues 决定系统模式：

- 实部 < 0：衰减；
- 实部 > 0：发散；
- 虚部：振荡频率。

因此 Euler 公式、特征值与微分方程在控制理论中自然汇合。

## Feedback

最简单状态反馈：

$
u=-Kx.
$

闭环变成

$
\dot x=(A-BK)x.
$

控制器设计的目标之一，是选择 $K$ 改变系统闭环特征，使其满足稳定性和性能要求。

## Kalman filter：控制与 Bayes 的交汇

Kalman 1960 年提出的经典线性滤波方法，在 state-space model 下递归估计不可直接观测的 state。

预测：

$
\hat x_{k|k-1}=A\hat x_{k-1|k-1}
$

更新：

$
\hat x_{k|k}
=
\hat x_{k|k-1}
+
K_k(y_k-H\hat x_{k|k-1}).
$

它可以被理解为：

- 线性系统；
- Gaussian probability；
- Bayesian update；
- least squares；

四者的结合。

## Optimal control

若要最小化

$
J
=
\int
(x^TQx+u^TRu)\,dt,
$

得到 LQR 一类问题。

更一般的 optimal control 连接：

- calculus of variations；
- Hamiltonian；
- dynamic programming；
- Bellman equation。

## 现代应用

- 飞机、火箭、卫星；
- 无人机和机器人；
- 自动驾驶；
- 电网；
- 工业过程；
- 脑机接口与神经调控闭环；
- camera stabilization；
- 数据中心温控；
- autonomous systems。

## 与强化学习的关系

control theory 通常假设系统模型已知或部分已知；RL 更强调通过交互学习 policy。

二者共享：

- state；
- action；
- dynamics；
- cost/reward；
- Bellman recursion。

现代研究中 model predictive control、system identification、RL 正在不断交叉。

## 与九个核心公式的连接

微积分 → ODE；  
Euler → eigenmodes；  
Fourier → frequency response；  
Bayes → state estimation；  
Taylor → nonlinear system linearization。

## 参考

- R. E. Kalman, *A New Approach to Linear Filtering and Prediction Problems* (1960), DOI: 10.1115/1.3662552
- Ogata, *Modern Control Engineering*.
- Åström & Murray, *Feedback Systems*.