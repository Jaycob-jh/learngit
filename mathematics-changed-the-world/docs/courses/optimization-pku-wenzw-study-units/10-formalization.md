# Unit 10｜Lean4 形式化验证入口

> **状态：学习与证明义务草稿。** 现有资源入口：[Optlib](https://github.com/optsuite/optlib)、[ReasLab](https://reaslab.io/)、[ReasBook](https://github.com/optpku/ReasBook)、[中文教学页](http://faculty.bicmr.pku.edu.cn/~wenzw/formal/index.html)。本批未读取其当前代码版本、未安装工具链、未编译 Lean 文件，因此不列出“已机器证明”的命题。

## 1. 从纸笔陈述到机器命题

优先选一个范围小而条件清楚的命题。例：对非空闭凸集 $C\subseteq\mathbb R^n$，欧氏投影 $p=\Pi_C(x)$ 满足

$$\langle x-p,y-p\rangle\le 0\quad(\forall y\in C).$$

形式化前须固定：空间与内积的类型、闭性和凸性的定义、投影存在唯一性的前提、投影记号及量词范围。只把纸笔公式改写成 theorem statement，仍不是证明；依赖库引理时应说明其确切版本与导入路径。

## 2. 建议顺序

1. 在已固定 Lean/toolchain 版本的项目里重现一个库中现成的凸集或投影例子，并保存编译日志。
2. 手推上面的投影变分不等式，列出每个使用的假设；在 Lean 中分别写 definition、statement、proof。
3. 对照 [Unit 03](03-optimality.md) 的一阶最优性条件，说明纸笔与形式化陈述是否完全一致。
4. 仅在简单命题真正编译后扩展到梯度下降、proximal gradient、BCD 或 ADMM 的局部引理。不同算法的收敛定理不共用一套未声明的假设。

## 3. 逐项验收记录

| 项 | 需要保存的证据 | 当前状态 |
|---|---|---|
| 数学命题与假设 | 来源章节/页码、纸笔证明 | 待阅读、待编写 |
| Lean definition / theorem | 文件路径、精确 import、工具链版本 | 待编写 |
| 机器检查 | `lake env lean` 或项目指定命令的退出码与完整日志 | **未运行** |
| 语义一致性 | 纸笔与 Lean 的量词、条件、结论逐项对照 | 待核对 |

不允许为使证明通过而静默加强假设、弱化结论，或把 `sorry`/外部自动生成的未检查文本记为 machine-checked proof。形式化资源目前是学习入口，不是本仓库内容已获形式化验收的证据。
