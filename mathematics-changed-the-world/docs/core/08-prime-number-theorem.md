# 08｜对数积分、素数定理与 Riemann：无规则的素数为什么有统计规律

> **一句话**：单个素数出现得像“不规则事件”，但整体密度却高度规律；解析数论的重大突破是把整数问题转换为复函数问题。

## 1. 素数最早的问题不是“分布”，而是“有多少”

Euclid 早已证明素数有无穷多个。

但更难的问题是：

> 小于 $x$ 的素数到底有多少？

定义

$$
\pi(x)=\#\{p\le x:p\text{ 是素数}\}.
$$

Gauss、Legendre 等通过计算观察到

$$
\pi(x)
\approx
\frac{x}{\log x}
$$

以及更精细的

$$
\pi(x)\approx \operatorname{li}(x),
$$

其中

$$
\operatorname{li}(x)
\mathrel{=}
\operatorname{PV}\int_0^x\frac{dt}{\log t}
$$

需注意 $t=1$ 的奇点，严格定义要做适当处理。

## 2. 素数定理说的是什么？

$$
\pi(x)\sim\frac{x}{\log x},
$$

意思是

$$
\lim_{x\to\infty}
\frac{\pi(x)}
{x/\log x}
\mathrel{=}
1.
$$

这不是说每个区间都平均分布，而是说在非常大的尺度上，素数密度大约为

$$
\frac{1}{\log x}.
$$

## 3. Euler 的关键桥梁

Euler 发现 zeta function 的乘积结构：

$$
\zeta(s)
\mathrel{=}
\sum_{n=1}^{\infty}\frac1{n^s}
\mathrel{=}
\prod_{p}
\frac{1}{1-p^{-s}}
\quad
(\Re s>1).
$$

左边对所有正整数求和，右边却对所有素数做乘积。

这就是解析数论最深刻的原型之一：

$$
\text{整数加法结构}
\longleftrightarrow
\text{素数乘法结构}.
$$

## 4. Riemann 1859：把素数放进复平面

Riemann 研究 $\zeta(s)$ 在复平面的解析延拓和零点，并建立素数计数与这些零点之间的联系。

这一步的思想极具代表性：

> 为了理解整数里的离散结构，把问题搬到连续的复分析世界里。

Hadamard 和 de la Vallée Poussin 于 1896 年独立证明素数定理，关键是证明 zeta 在 $\Re s=1$ 上没有零点。

## 5. Riemann 假设究竟控制什么？

非平凡零点写成

$$
\rho=\beta+i\gamma.
$$

Riemann hypothesis 猜测：

$$
\beta=\frac12
$$

对所有非平凡零点成立。

它不是“证明素数有规律”——素数定理已经做到了。RH 更深地约束：

> $\pi(x)$ 围绕主趋势波动得有多厉害。

也就是控制素数分布误差项。

## 6. 为什么 $\operatorname{li}(x)$ 往往比 $x/\log x$ 更准？

直觉上素数在尺度 $t$ 附近的“局部密度”约为

$$
\frac1{\log t}.
$$

把这种密度从 2 累积到 $x$：

$$
\int_2^x\frac{dt}{\log t},
$$

自然得到对数积分近似。

这与“局部密度累积成总数量”的微积分思想遥相呼应。

## 7. 与密码学的真实关系

RSA 确实需要大素数，但不能简单说：

> “RSA 是素数定理的直接应用。”

更准确：

- 素数定理告诉我们大数附近素数的平均密度，因此随机找到素数并不会极端困难；
- 实际密钥生成依赖高效 primality testing；
- RSA 安全性主要关联大整数分解困难性，而不是“素数稀少”。

椭圆曲线密码学又使用了另一套代数与数论结构。

## 8. 动手实验

\`\`\`bash
python labs/08_prime_counting.py
\`\`\`

比较：

$$
\pi(x),\qquad
x/\log x,\qquad
\operatorname{li}(x)
$$

随 $x$ 增大时的逼近效果。

## 9. 向外延伸

素数 → Euler product → complex analysis → Riemann zeta → spectral ideas → analytic number theory。

## 参考

- MacTutor, Prime numbers: https://mathshistory.st-andrews.ac.uk/HistTopics/Prime_numbers/
- Clay Mathematics Institute, Riemann manuscript: https://www.claymath.org/collections/riemanns-1859-manuscript/
- Clay Mathematics Institute, Riemann Hypothesis: https://www.claymath.org/millennium/Riemann-Hypothesis/
- Apostol, *Introduction to Analytic Number Theory*.