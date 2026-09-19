# 03｜Euler 公式：复数为什么天然描述旋转与波

> **一句话**：$e^{i\theta}=\cos\theta+i\sin\theta$ 把指数增长、圆周旋转、三角函数和复数统一成同一套语言。

## 1. 复数最初不是为了“旋转”

16 世纪解三次方程时，即便最终答案是实数，中间步骤也会出现 $\sqrt{-1}$。Cardano、Bombelli 等逐渐学会操作这些当时被视为“虚构”的量。

之后 de Moivre、Cotes、Euler 等发现：复数不只是代数技巧，它和圆周运动存在极其自然的联系。

## 2. 从幂级数看 Euler 公式

指数、余弦、正弦的 Taylor 级数分别为

$$
e^x
=
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots,
$$

$$
\cos x
=
1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots,
$$

$$
\sin x
=
x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots.
$$

把 $x$ 换成 $i\theta$，利用 $i^2=-1$：

$$
e^{i\theta}
=
1+i\theta-\frac{\theta^2}{2!}
-i\frac{\theta^3}{3!}
+\frac{\theta^4}{4!}+\cdots.
$$

把实部、虚部分组：

$$
e^{i\theta}
=
\cos\theta+i\sin\theta.
$$

## 3. 为什么复乘法就是旋转？

写

$$
z=re^{i\theta}.
$$

再乘以

$$
w=\rho e^{i\phi},
$$

得到

$$
zw=r\rho e^{i(\theta+\phi)}.
$$

所以复数乘法同时完成两件事：

- 模长相乘；
- 角度相加。

特别地，乘 $e^{i\phi}$ 就是把平面向量旋转 $\phi$。

## 4. 为什么“波”喜欢复指数？

对

$$
e^{i\omega t}
$$

求导：

$$
\frac{d}{dt}e^{i\omega t}
=
i\omega e^{i\omega t}.
$$

也就是说，微分不会改变它的“形状”，只乘上一个常数。这使复指数成为线性微分系统天然的特征函数。

因此正弦振动常写为

$$
A\cos(\omega t+\phi)
=
\Re\{Ae^{i(\omega t+\phi)}\}.
$$

计算时先在复数域做代数，最后取实部即可。

## 5. Euler 恒等式为什么著名？

令 $\theta=\pi$：

$$
e^{i\pi}+1=0.
$$

它把 $e,i,\pi,1,0$ 放进一个极简关系。但其真正价值不是“审美投票”，而是它揭示了多个数学结构之间的统一。

## 6. 现实应用

### 交流电
电压和电流用 phasor 表示，把微分方程转成复数代数。

### 通信
载波、调制、相位、频谱几乎都以复指数为自然语言。

### 控制理论
线性系统的特征值可以是复数；实部决定增长/衰减，虚部决定振荡频率。

### 量子力学
量子态相位和时间演化天然涉及复数 Hilbert space。

### Fourier
Fourier transform 的核就是

$$
e^{-i\omega t}.
$$

## 7. 常见误解

- “虚数”不是“不真实的数”；它只是扩展了实数系统。
- 工程中的复数通常不是声称测量量本身是“虚的”，而是把幅值和相位压缩进一个对象。
- $e^{i\pi}+1=0$ 很漂亮，但 Euler 公式的技术价值远远大于这一个特例。

## 8. 动手实验

\`\`\`bash
python labs/03_euler_phasor.py
\`\`\`

观察单位复数 $e^{i\theta}$ 在复平面旋转，同时比较它在实轴上的投影 $\cos\theta$。

## 参考

- MacTutor, Leonhard Euler: https://mathshistory.st-andrews.ac.uk/Biographies/Euler/
- Needham, *Visual Complex Analysis*.
- Stein & Shakarchi, *Complex Analysis*.