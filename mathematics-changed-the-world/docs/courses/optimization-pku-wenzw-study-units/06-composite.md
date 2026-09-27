# Unit 06｜复合优化：近似点、加速与变量分裂

> 对应资源：[电子讲义索引的主题 19–25](../optimization-pku-wenzw-lectures.md)；教材第二版第 8.1–8.6 节。这里是独立导学与可复现实验，不替代教材中的定理及其证明。
>
> 前置：[Unit 02 的 LASSO 建模](02-modeling.md)、[Unit 03 的复合最优性条件](03-optimality.md)、[Unit 05 的 ALM 与对偶变量](05-constrained.md)。实验：`labs/18_optimization_composite.py`。

> PPA 与 ALM 对偶近似点关系可配合 Unit 05 的 `labs/17_optimization_constrained.py` 中等式约束实验观察；本单元的四算法实验聚焦 LASSO。

## 1. 问题与适用边界

考虑

$$
\min_{x\in\mathbb R^n}\ \psi(x)=f(x)+h(x),
$$

其中本单元的**基本凸情形**是：$f$ 凸且可微、$\nabla f$ 为 $L$-Lipschitz 连续；$h$ 是适当、闭、凸函数，其 proximal 子问题容易求解；最优解存在。$h$ 可以非光滑，甚至取集合 $C$ 的指示函数 $\delta_C$。若 $f$ 或 $h$ 非凸，以下凸情形的全局最优和函数值速度结论不可直接搬用。

最优性条件是

$$
0\in\nabla f(x^*)+\partial h(x^*).
$$

这个条件同时覆盖 LASSO 的稀疏解和凸约束问题的投影解。它说明算法不必对整个 $f+h$ 求普通梯度。

## 2. Proximal operator：把非光滑项做成一个步骤

对 $t>0$，定义

$$
\operatorname{prox}_{th}(v)
=\arg\min_u\left\{h(u)+\frac{1}{2t}\|u-v\|_2^2\right\}.
$$

在上述闭凸假设下，二次项使子问题强凸，因此 prox 单值。其一阶条件为

$$
\frac{v-u}{t}\in\partial h(u),\qquad u=\operatorname{prox}_{th}(v).
$$

两个必须手推的例子：

- $h=\delta_C$ 且 $C$ 非空闭凸时，$\operatorname{prox}_{t\delta_C}(v)=\Pi_C(v)$。
- $h(u)=\lambda\|u\|_1$ 时，$\operatorname{prox}_{th}(v)_j=\operatorname{sign}(v_j)(|v_j|-t\lambda)_+$，即 soft threshold。

**非例与边界。** 对非凸集合做投影可能多值；一般非凸 $h$ 的 prox 也可能多值。此时不能沿用“单值且非扩张”的闭凸理论。Moreau envelope

$$
h_t(v)=\min_u\left\{h(u)+\frac{1}{2t}\|u-v\|^2\right\}
$$

在闭凸情形下可微，且 $\nabla h_t(v)=(v-\operatorname{prox}_{th}(v))/t$。它把一个非光滑凸函数关联到平滑近似，但改变 $t$ 会改变该近似。

## 3. ISTA：线性化 $f$，保留 $h$

在 $x_k$ 处把 $f$ 用一阶模型加二次项近似，取 $0<t\le 1/L$：

$$
x_{k+1}=\operatorname{prox}_{th}\bigl(x_k-t\nabla f(x_k)\bigr).
$$

这是 proximal gradient；用于 LASSO 时常称 ISTA。对

$$
f(x)=\tfrac12\|Ax-b\|_2^2,\quad h(x)=\lambda\|x\|_1,
$$

有 $L=\|A\|_2^2$，因此一步是

$$
x_{k+1}=S_{t\lambda}\bigl(x_k-tA^T(Ax_k-b)\bigr).
$$

实际不知道 $L$ 时，可用检查复合目标充分下降的回溯线搜索；不能任意增大步长并仍声称收敛。在上述凸、光滑及存在最优解的条件下，固定 $t=1/L$ 的标准函数值界为 $\psi(x_k)-\psi^*=O(1/k)$。这不是每一步目标都以固定比例下降的断言。

**停止准则。** 采用 proximal gradient mapping

$$
G_t(x)=\frac{x-\operatorname{prox}_{th}(x-t\nabla f(x))}{t}.
$$

在本节凸假设下，$G_t(x)=0$ 等价于复合一阶最优性；记录 $\|G_t(x_k)\|$ 比只记录 $\|x_{k+1}-x_k\|$ 更有可解释性。小残差是数值证据，不等于证明已找到精确解。

## 4. FISTA：外推与它的条件

取 $t=1/L$，$x_0=y_0$，$q_0=1$：

$$
\begin{aligned}
x_{k+1}&=\operatorname{prox}_{th}(y_k-t\nabla f(y_k)),\\
q_{k+1}&=\frac{1+\sqrt{1+4q_k^2}}{2},\\
y_{k+1}&=x_{k+1}+\frac{q_k-1}{q_{k+1}}(x_{k+1}-x_k).
\end{aligned}
$$

在本节凸问题、正确步长及精确 prox 的条件下，函数值有 $O(1/k^2)$ 的标准上界；相同条件下 ISTA 是 $O(1/k)$。这比较的是理论上界，不能据一次实验断言 FISTA 在所有数据或所有迭代上更快。基础 FISTA 的目标值也**不要求逐步单调**。重启、单调变体及回溯需要各自的更新与分析，不能把它们混作上式的无条件性质。

## 5. Proximal point 与 Unit 05 的 ALM

对适当闭凸函数 $F$，proximal point algorithm (PPA) 为

$$
x_{k+1}=\operatorname{prox}_{t_kF}(x_k).
$$

每步求解的是带二次正则的完整子问题；这和 ISTA 仅对 $h$ 做 prox、对 $f$ 做梯度步不同。精确 PPA 的收敛需要最优解存在及适当的正步长条件；实际内层子问题不精确时还需控制误差。

对 Unit 05 的等式约束问题，取 $L_\rho(x,\lambda)=f(x)+\lambda^T(Ax-b)+(\rho/2)\|Ax-b\|^2$，精确 ALM 更新为

$$
x_{k+1}\in\arg\min_x L_\rho(x,\lambda_k),\qquad
\lambda_{k+1}=\lambda_k+\rho(Ax_{k+1}-b).
$$

在凸性、对偶最优解存在以及适当强对偶条件下，该乘子更新可解释为在**凹对偶函数** $d$ 上做 proximal point：

$$
\lambda_{k+1}\in\arg\max_\lambda
\left\{d(\lambda)-\frac{1}{2\rho}\|\lambda-\lambda_k\|^2\right\}.
$$

符号方向取决于 Unit 05 的约定 $L=f+\lambda^T(Ax-b)$。这一关系解释乘子为何也可被视为优化变量；它并不表示有限精度内层求解时上述等式仍无误差成立。

## 6. BCD：利用块结构

将 $x=(x_1,\ldots,x_p)$，循环 BCD 每步只更新一块：

$$
x_i^{k+1}\in\arg\min_{u_i}
\psi(x_1^{k+1},\ldots,x_{i-1}^{k+1},u_i,x_{i+1}^{k},\ldots,x_p^k).
$$

顺序可循环或随机；收敛断言必须同时说明凸性、块子问题可解性、更新精度与选块规则。LASSO 的坐标子问题有 soft threshold 闭式解。若 $a_j$ 是 $A$ 的第 $j$ 列、$r=Ax-b$，则

$$
x_j^{\rm new}=S_{\lambda/\|a_j\|^2}
\left(x_j-\frac{a_j^Tr}{\|a_j\|^2}\right),\quad a_j\ne0.
$$

每次只改一个坐标后同步更新残差，避免重复计算 $Ax$。对于非凸字典学习等问题，“每块目标下降”不能推出全局最优；块最优、驻点和全局解须区分。

## 7. 对偶分解与 ADMM

对 $\min f(x)+g(z)$ 且 $Ax+Bz=c$，Lagrangian 为

$$
\mathcal L(x,z,\lambda)=f(x)+g(z)+\lambda^T(Ax+Bz-c).
$$

当固定 $\lambda$ 时的两个内层极小化可以分开，对偶函数由此构造。对偶可行和对偶目标进展并不自动给出原始可行解；还须检查 $Ax+Bz-c$ 并说明原始解恢复方式。

ADMM 将 Unit 05 的 ALM 内层联合求解改成交替步骤。用 scaled dual variable $u=\lambda/\rho$，$\rho>0$：

$$
\begin{aligned}
x^{k+1}&\in\arg\min_x f(x)+\frac\rho2\|Ax+Bz^k-c+u^k\|^2,\\
z^{k+1}&\in\arg\min_z g(z)+\frac\rho2\|Ax^{k+1}+Bz-c+u^k\|^2,\\
u^{k+1}&=u^k+Ax^{k+1}+Bz^{k+1}-c.
\end{aligned}
$$

LASSO 采用 $x=z$ 分裂：$f(x)=\tfrac12\|Ax-b\|^2$、$g(z)=\lambda\|z\|_1$。此时 $x$ 步解正定线性系统，$z$ 步为 $S_{\lambda/\rho}(x^{k+1}+u^k)$。应同时记录原始残差 $r^{k+1}=x^{k+1}-z^{k+1}$ 与对偶残差 $s^{k+1}=\rho(z^{k+1}-z^k)$ 的范数；后者符号对范数无影响。仅看目标值不足以证明分裂约束满足。

经典两块凸 ADMM 的收敛还要求适当的闭凸性、鞍点存在和子问题可解/足够精确等前提；非凸、多块直接推广或任意调节 $\rho$ 均不由该结论保证。

## 8. 同题实验与失败案例

运行：

```bash
python labs/18_optimization_composite.py --iterations 250 --csv unit06-history.csv
```

脚本固定随机种子生成 $80\times24$ 的 LASSO 问题，对同一 $A,b,\lambda$ 运行 ISTA、FISTA、cyclic coordinate descent 和 ADMM。每轮输出到 CSV 的指标是目标值、$\|G_{1/L}(x)\|$；ADMM 另记录原始及对偶残差。坐标下降的一轮是一个完整 sweep，其他算法的一轮是各自一次更新，因此**迭代数不是等计算量比较**。ADMM 在 $x\ne z$ 时以稀疏候选 $z$ 计算原目标，仍须结合分裂残差判断。

脚本还展示一个明确失败案例：对 $f(x)=x^2/2$，普通梯度法若用 $t=2.2>2/L$，有 $x_{k+1}=-1.2x_k$，从 $x_0=1$ 出发绝对值增长。它说明步长前提的重要性；不代表所有超出 $1/L$ 的步长都必然发散。

实验能验证实现和观察机制，不能代替凸收敛定理，也不能给这四种算法作普遍速度排名。

## 9. 完成检查

1. 从 prox 子问题的一阶条件推导 soft threshold 与投影；说明非凸投影可能多值。
2. 写出 LASSO 的复合最优性条件与 $G_t(x)$，解释为什么 $G_t(x)=0$。
3. 说明 ISTA 与 FISTA 的两个函数值上界各依赖什么条件；解释 FISTA 目标为何可能不单调。
4. 说明 PPA 与 ISTA 的 prox 对象有什么不同，以及 ALM 的对偶 PPA 解释依赖哪些条件。
5. 手推 LASSO 一个坐标的更新，并说明零列为何需要特殊处理。
6. 写出 $x=z$ 分裂下 ADMM 的三个步骤，分别解释 $r$ 和 $s$。
7. 运行实验并检查四种方法的目标与 proximal gradient 残差；改变 $\lambda$ 或 $\rho$ 后重新解释结果。
8. 解释为什么非凸问题的块下降或单次 LASSO 数值实验，都不能推出全局收敛。

下一单元：[Unit 07｜随机与非光滑高级算法](../optimization-pku-wenzw-study-roadmap.md)。
