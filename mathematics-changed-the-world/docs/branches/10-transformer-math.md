# Transformer 背后的数学：不是“新数学”，而是多条成熟数学主干的组合

> **核心问题**：Transformer 为什么能让每个 token 动态“读取”其他 token 的信息？它具体调用了哪些数学结构？

## 2017：Attention Is All You Need

Transformer 在 2017 年的论文 *Attention Is All You Need* 中系统提出。原始架构的关键变化是：

- 不再依赖 recurrent network 顺序传播状态；
- 不再以 convolution 作为主要 token mixing；
- 核心交互由 attention 完成。

## 1. Linear algebra：最底层语言

输入 token embedding：

\[
X\in\mathbb R^{n\times d}.
\]

通过 learned linear maps：

\[
Q=XW_Q,\qquad
K=XW_K,\qquad
V=XW_V.
\]

这里没有神秘操作，本质是 matrix multiplication。

## 2. Dot product：相似性与匹配

attention logits：

\[
S
=
\frac{QK^T}{\sqrt{d_k}}.
\]

第 \(i,j\) 项是 query \(q_i\) 与 key \(k_j\) 的 dot product。

若向量尺度相近，dot product 大致反映方向匹配。

### 为什么除以 \(\sqrt{d_k}\)？

若分量独立、均值约 0、方差约 1，则 dot product 的 variance 会随维数 \(d_k\) 增长。

缩放

\[
1/\sqrt{d_k}
\]

让 logits 数值尺度更稳定，避免 softmax 太容易进入极端饱和区。

## 3. Softmax：把 score 变成权重

\[
A_{ij}
=
\frac{e^{S_{ij}}}
{\sum_j e^{S_{ij}}}.
\]

每一行形成 probability-like weights：

\[
\sum_j A_{ij}=1.
\]

输出：

\[
O=AV.
\]

所以单个 token 的新表示，是其他 value vectors 的数据依赖加权平均。

## 4. Multi-head attention

不是只做一次 \(Q,K,V\)，而是多个 head：

\[
\operatorname{head}_h
=
\operatorname{Attention}(Q_h,K_h,V_h).
\]

然后 concatenate + linear projection。

不同 head 可以学习不同关系，但不应把“某个 head 一定对应语法/实体”等解释当作普遍定律；representation 往往是 distributed。

## 5. Positional information

纯 self-attention 对 token permutation 本身缺乏序列顺序感，因此需要加入 position structure。

原论文使用 sinusoidal positional encoding：

\[
PE(pos,2i)
=
\sin
\left(
pos/10000^{2i/d}
\right),
\]

\[
PE(pos,2i+1)
=
\cos
\left(
pos/10000^{2i/d}
\right).
\]

这里能看到 Euler/Fourier 相关的周期表示思想，但 positional encoding 并不等于 Fourier transform。

后续模型还出现 learned position、relative position、rotary positional embedding 等路线。

## 6. Probability 与 information theory

语言模型训练常最小化 negative log-likelihood：

\[
L
=
-\sum_t \log p(x_t|x_{<t}).
\]

分类形式常表现为 cross-entropy：

\[
H(p,q)
=
-\sum_i p_i\log q_i.
\]

因此 Shannon information、maximum likelihood、probability modeling 都直接进入训练目标。

## 7. Calculus 与 optimization

参数量可能达到极大规模，但训练仍建立在：

\[
\nabla_\theta L
\]

与 chain rule 上。

backpropagation 本质上是高效组织 chain rule 的算法。

优化器如 SGD、Adam 则在 noisy gradient 下迭代寻找低损失区域。

## 8. Numerical linear algebra

真正运行 Transformer 时，绝大多数计算成本来自：

- GEMM / matrix multiplication；
- attention matrix operation；
- normalization；
- vectorized elementwise operation。

FlashAttention 一类技术的创新往往不是改变 attention 数学定义，而是改变 memory access、tiling 和 exact computation order，从而提高硬件效率。

## 9. Attention 与 kernel / graph 的类比

每个 token 与其他 token 建立 weighted interaction，可视为动态、data-dependent complete graph。

因此它与：

- kernel methods；
- message passing；
- graph neural networks；

存在结构类比，但不能简单等同。

## 10. Transformer 知识树

\[
\text{线性代数}
\to
Q,K,V
\]

\[
\text{概率/信息论}
\to
softmax,\ cross\ entropy
\]

\[
\text{微积分}
\to
backprop
\]

\[
\text{优化}
\to
SGD/Adam
\]

\[
\text{Fourier/Euler}
\to
periodic positional representations
\]

\[
\text{数值分析}
\to
mixed precision,\ stability,\ efficient kernels.
\]

所以“Transformer 背后的数学”不是一条公式，而是多条数学文明主干在现代计算机上的汇流。

## 参考

- Vaswani et al., *Attention Is All You Need*: https://arxiv.org/abs/1706.03762
- Goodfellow, Bengio & Courville, *Deep Learning*.
- Dive into Deep Learning: https://d2l.ai/