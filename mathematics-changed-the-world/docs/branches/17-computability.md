# 可计算性：有些问题不是“计算机太慢”，而是根本不存在通用算法

> **核心问题**：到底什么叫“算法”？是否每个数学问题原则上都能通过机械步骤解决？

## 20 世纪初的基础危机

Hilbert 等人希望数学拥有机械化 decision procedure：

> 给定形式化命题，是否存在一种通用有限程序判断其真伪？

要回答这个问题，首先必须精确定义“程序”。

## Turing machine

1936 年 Alan Turing 用极简抽象机器刻画机械计算：

- tape；
- finite states；
- read/write head；
- deterministic transition rules。

它不是为了模拟具体电脑硬件，而是为了抓住 algorithmic procedure 的本质。

Church 的 lambda calculus 从另一条路线得到等价计算能力，形成 Church–Turing thesis 的背景。

## Universal machine

Turing 进一步展示：

> 一台通用机器可以把“另一台机器的描述 + 输入”当数据读取并模拟它。

这就是现代 stored-program computer 最重要的概念祖先之一：

\[
\text{program 也可以是 data}.
\]

## Halting problem

问：

> 给定任意程序 \(P\) 和输入 \(x\)，能否写一个通用程序判断 \(P(x)\) 最终是否停止？

Turing 证明：不存在这样的 universal halting decider。

这不是“还没人找到算法”，而是 mathematically impossible。

## Computable vs tractable

两个问题不要混：

### Computability
有没有算法？

### Complexity
有算法，但需要多少：

- time；
- memory；
- communication？

一个 problem 可以 computable，但在现实规模上极难。

## 从 Turing 到现代计算机科学

可计算性催生：

- formal languages；
- compilers 理论；
- complexity；
- verification；
- cryptography foundations；
- computability in analysis。

## AI 能绕过不可计算性吗？

不能。

Machine learning 可以：

- approximate；
- predict common cases；
- exploit distributions；
- use heuristics。

但它不会让 mathematically undecidable problem 变成 universal decidable。

同样，LLM 输出“看起来像证明”不等于拥有 general theorem-deciding oracle。

## Gödel 与 Turing

Gödel incompleteness 和 Turing undecidability 深刻相关但不是同一个定理。

粗略说：

- Gödel：足够强的 formal system 有无法在系统内证明/否证的命题；
- Turing：不存在能解决所有程序 halting instances 的算法。

## 与项目主线连接

数学开始研究“数”；
后来研究“函数与空间”；
20 世纪进一步把“证明与算法自身”变成数学对象。

这是一次对象层级的巨大提升。

## 参考

- Alan Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem* (1936).
- Sipser, *Introduction to the Theory of Computation*.