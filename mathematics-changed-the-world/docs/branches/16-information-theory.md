# 信息论：信息能不能像长度、能量一样被测量？

> **核心问题**：一个符号到底携带多少信息？数据最多能压缩到什么程度？带噪声信道最多能可靠传多少比特？

## 1948：Shannon 把通信从设备问题提升为数学问题

Claude Shannon 在 1948 年的 *A Mathematical Theory of Communication* 中建立现代 information theory 的核心框架。

重要观念是：

> 通信系统首先处理的是“从一个概率分布中选出的消息”，而不是消息的语义。

语义当然重要，但信道容量、编码与压缩可以先在概率层面精确研究。

## Self-information

低概率事件更“意外”。

定义：

$
I(x)=-\log p(x).
$

为什么 logarithm 自然？

因为独立事件概率相乘：

$
p(x,y)=p(x)p(y),
$

而我们希望信息量可加：

$
I(x,y)=I(x)+I(y).
$

log 正好把 multiplication 变 addition。

## Entropy

随机变量 $X$ 的 entropy：

$
H(X)
=
-\sum_x p(x)\log p(x).
$

它可理解为平均 self-information，也是无损压缩理论的核心量。

## 为什么公平硬币 1 bit？

若 heads/tails 各 $1/2$：

$
H
=
-\frac12\log_2\frac12
-\frac12\log_2\frac12
=1.
$

若硬币几乎永远 heads，entropy 接近 0，因为结果几乎可预测。

## Mutual information

$
I(X;Y)
=
H(X)-H(X|Y).
$

它衡量知道 $Y$ 后，对 $X$ 的 uncertainty 减少多少。

这让“相关信息”成为精确 quantity。

## KL divergence

$
D_{\mathrm{KL}}(p\|q)
=
\sum_x p(x)\log\frac{p(x)}{q(x)}.
$

它不是对称 distance，却广泛衡量两个 distributions 的差异。

## Channel capacity

Shannon 最惊人的结论之一是：对给定 noisy channel 存在容量 $C$。

当 transmission rate < $C$，原则上可以通过编码把 error probability 做得任意小；超过容量则无法可靠通信。

这第一次告诉工程师：

> 不是“还没发明足够好的设备”，而是存在数学极限。

## 现实应用

- compression；
- error-correcting codes；
- cellular / satellite communication；
- cryptography；
- statistical inference；
- neuroscience coding；
- machine learning losses；
- representation learning。

## AI 中的 cross-entropy

分类模型常最小化

$
-\sum_i p_i\log q_i.
$

它和 maximum likelihood、KL divergence 直接相关。

语言模型 next-token objective 也本质上是 probability + information theory。

## 与九个核心公式连接

Bayes → probability distribution；  
Fourier → communication signals；  
linear algebra → coding；  
Transformer → cross-entropy；  
statistics → KL / mutual information。

## 参考

- C. E. Shannon, *A Mathematical Theory of Communication* (1948), Bell System Technical Journal, Vol. 27.
- Cover & Thomas, *Elements of Information Theory*.