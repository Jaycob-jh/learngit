# 项目历史记录 / HISTORY

> 项目：`mathematics-changed-the-world`  
> 仓库：`Jaycob-jh/learngit`  
> 分支：`math-changed-world`  
> 时间统一按 UTC+8 描述；GitHub Commit API 原始时间使用 UTC。

---

## 2026-09-19：项目起点

### 14:29 左右｜从短视频开始

最初输入是一条抖音视频链接。视频主题围绕“数学曾多次改变我们认识世界的方式”，涉及多个经典数学公式与定理。

由于抖音网页没有可靠返回字幕，后续通过用户提供的视频文件进行实际核对。

### 视频内容核对

从上传的视频中确认九个核心数学主题：

1. 微积分基本定理；
2. Taylor 展开；
3. Euler 公式；
4. Fourier 变换；
5. 散度定理；
6. 留数定理；
7. Bayes 公式；
8. 对数积分 / 素数分布；
9. Lebesgue 单调收敛定理。

这一阶段同时修正了早期仅凭主题推测可能造成的不准确项，例如确认最后一项是 Lebesgue 单调收敛定理，而不是其他近似名称。

---

## 2026-09-19 14:57｜GitHub 项目正式建立

GitHub 连接器不能直接创建全新仓库，因此采用安全方式：

```text
仓库：Jaycob-jh/learngit
分支：math-changed-world
目录：mathematics-changed-the-world/
```

未修改原仓库的默认主分支内容。

首个项目提交：

```text
080dcca  add math knowledge base: mathematics-changed-the-world/README.md
时间：2026-09-19 14:57:05 UTC+8
```

随后建立第一版基础结构：

```text
3d910ed  docs/01-nine-core.md
fe0f1c2  docs/02-beyond.md
653a917  docs/03-timeline-applications.md
fe64f59  docs/04-references.md
844e4aa  examples/taylor_demo.py
feb6b8a  examples/bayes_demo.py
8a56a43  requirements.txt
```

这一阶段的目标是先建立一个可持续扩展的知识库骨架。

---

## 2026-09-19 15:05–15:06｜九个核心专题拆分为独立长章

九个主题开始从总览文档升级为独立专题。

代表性提交：

```text
c07f9bb  01-calculus.md
00a7518  02-taylor.md
62caad4  03-euler.md
5e17cd1  04-fourier.md
be673c1  05-divergence.md
d9ee49b  06-residue.md
4db7cb5  07-bayes.md
49d1aab  08-prime-number-theorem.md
5f34f08  09-lebesgue.md
```

每章逐步加入：

- 前史；
- 关键数学家；
- 核心公式；
- 原理解释；
- 发展过程；
- 现实应用；
- 常见误解；
- 延伸路线。

这一步标志着项目从“公式列表”进入“课程型资料”的阶段。

---

## 2026-09-19 15:07–15:13｜现代数学主干快速扩展

第一批现代主干：

```text
拓扑
微分几何
泛函分析
图论
博弈论
控制论
小波
随机过程
数值分析
Transformer 数学
```

代表提交从：

```text
b108b71  add modern math branch: 01-topology.md
```

扩展到：

```text
09f8746  add modern math branch: 10-transformer-math.md
```

随后继续加入第二批基础主干：

```text
复数
线性代数
微分方程
非欧几何
群论与对称性
信息论
可计算性
混沌
凸优化
概率论
```

最终形成 20 条主干。

其中部分代表提交：

```text
bb89306  11-complex-numbers.md
1433912  12-linear-algebra.md
e06ebd5  13-differential-equations.md
5b8a2fe  14-non-euclidean-geometry.md
3cf99ab  15-group-symmetry.md
9073f83  16-information-theory.md
eb97662  17-computability.md
d7e3af3  18-chaos.md
43cd9fd  19-convex-optimization.md
0d97211  20-probability.md
```

---

## 2026-09-19 15:09–15:11｜建立数学实验室

项目从纯文本资料扩展为可运行实验体系。

最早建立：

```text
labs/README.md
requirements-labs.txt
```

随后加入九个核心实验：

```text
01_calculus_accumulation.py
02_taylor_animation.py
03_euler_phasor.py
04_fourier_decomposition.py
05_divergence_flux.py
06_residue_numeric.py
07_bayes_update.py
08_prime_counting.py
09_monotone_convergence.py
```

再加入三个现代实验：

```text
10_kalman_filter.py
11_wavelet_demo.py
12_attention_heatmap.py
```

实验体系完成后，项目已经具备“读理论 + 跑实验”的双层学习结构。

---

## 2026-09-19｜实验代码质量修正

在实验运行和检查过程中进行了多次修正。

### 单调收敛实验

修正积分表达，并把 NumPy 已弃用接口：

```python
np.trapz(...)
```

升级为：

```python
np.trapezoid(...)
```

### Wavelet 实验

最初版本依赖 PyWavelets。为了降低安装成本，后改为纯 NumPy 实现 Haar 多尺度分解。

对应提交：

```text
5733109  simplify wavelet lab to pure NumPy Haar transform
152be34  remove optional PyWavelets dependency
```

### 散度实验

原始离散求和存在端点面积近似带来的轻微偏差，后改成二维梯形积分，使数值结果更贴近理论值。

代表提交：

```text
d969cc5  improve divergence theorem numerical integration
```

### Fourier 实验

将输出从容易混入浮点残差的多个峰值，调整为展示真正构造信号中的三个主频。

代表提交：

```text
be6e58a  clarify FFT lab dominant frequencies
```

---

## 2026-09-19｜建立导航、学习路线和知识图谱

项目新增：

```text
docs/index.md
docs/knowledge-graph.md
docs/learning-paths.md
docs/05-modern-references.md
ROADMAP.md
mkdocs.yml
```

这一阶段的目标是把“很多文章”升级成“有路径的知识系统”。

### 学习路线

建立了：

- 数学世界观路线；
- 工程 / 信号 / MRI / BCI 路线；
- AI / 机器学习路线；
- 物理路线；
- 纯数学 / 理论路线。

### 知识图谱

建立主要连接链，例如：

```text
微积分 → 微分方程 → 控制 / 混沌
复数 → Euler → Fourier → 复分析
Fourier → Lebesgue → 泛函分析 → 小波
概率 → Bayes → 随机过程
线性代数 + 优化 + 信息论 + 数值分析 → Transformer
```

---

## 2026-09-19 晚间｜数学公式显示问题被发现

用户提供截图，指出页面中出现类似：

```text
[ A(x)=\int_a^x f(t)\,dt, ]
```

和：

```text
\frac{A(x+h)-A(x)}{h}
```

直接显示为文本的问题。

问题本质是 Markdown / MathJax 数学分隔符兼容性不统一。

---

## 2026-09-19 23:00–23:25 左右｜全项目公式渲染专项修复

### 第一阶段：统一公式语法

将文档中的：

```text
\( ... \)
\[ ... \]
```

统一转换为：

```text
$...$
$$...$$
```

处理范围包括：

- 9 个核心专题；
- 20 个主干专题；
- index；
- knowledge graph；
- learning paths；
- labs README；
- 其他包含公式的 Markdown 页面。

### 第二阶段：增加 MathJax 显式配置

新增：

```text
docs/javascripts/mathjax.js
```

代表提交：

```text
367b0e1  add explicit MathJax configuration
4f3e2db  configure MathJax for rendered formulas
```

### 第三阶段：发现并修正批量转换细节

在转换过程中发现 JavaScript `String.replace()` 对替换字符串 `$$` 有特殊语义，可能将预期的两个美元符号转换成一个。

随后执行第二轮修复，将独立单行 `$` 恢复为正确的：

```markdown
$$
...
$$
```

相关提交大量使用：

```text
repair display math delimiters
```

### 第四阶段：全仓静态扫描

最终对 40 个 Markdown 文件进行了多轮扫描。

检查项：

```text
\[
\]
\(
\)
单独的 $
数学环境外的 \frac
数学环境外的 \int
数学环境外的 \sum
数学环境外的 \nabla
数学环境外的 \mathbb
以及其他常见 LaTeX 命令
```

最终检查结果：

```text
残留 legacy delimiter：0
错误 single-dollar display block：0
检测到的裸露主要 LaTeX 数学命令：0
```

公式渲染问题至此完成全项目级修复。

---

## Git 历史统计

在本 HISTORY 文档写入之前，项目目录：

```text
mathematics-changed-the-world/
```

共查询到 **131 条提交记录**。

最早项目提交：

```text
080dcca
2026-09-19 14:57:05 UTC+8
add math knowledge base: mathematics-changed-the-world/README.md
```

公式修复完成后的最新提交（在报告文档加入之前）：

```text
28dadfe
2026-09-19 23:24:56 UTC+8
repair display math delimiters
```

从项目第一份 README 到公式全仓修复，主要开发工作集中在约 8.5 小时内完成。

---

## 当前项目状态

截至 2026-09-20：

```text
9   个核心数学长章
20  个数学主干专题
12  个正式 Python 实验
40  个 Markdown 文件
58  个项目文件
1   套 MkDocs 文档网站结构
1   套 MathJax 数学公式配置
```

项目已经完成第一阶段基础建设。

下一阶段将从“覆盖广度”逐步转向：

```text
内容深度
教学结构
可视化
练习体系
原始论文导读
现实技术案例
自动化文档发布
```

---

## 维护约定

以后重要项目修改建议继续记录到本文件，格式建议：

```markdown
## YYYY-MM-DD

### Added
新增了什么

### Changed
修改了什么

### Fixed
修复了什么

### Verified
进行了什么检查
```

这样 `HISTORY.md` 将同时承担项目开发日志和内容版本历史的作用。


---

## 2026-09-26｜纳入北大最优化课程体系

新增 `docs/courses/optimization-pku-wenzw.md`，把文再文 optbook 教材、北京大学《最优化方法》、北京大学《大数据分析中的算法》、算法代码入口与 Lean4 形式化方向接入现有数学知识库。

本轮原始 `faculty.bicmr.pku.edu.cn/~wenzw/optbook.html` 返回 502 / 不可访问，因此按来源等级处理：

- 主页面镜像逐项保留 12 个外链；
- 独立搜索/文献索引确认 5 个内部算法/目录子页；
- 北京大学数学科学学院与北京大学“101 计划”页面作为高等级课程/教材证据；
- 2025 春 `bigdata2025.html` 暂列二级证据，等待原站恢复后复核；
- 不根据命名规律猜测未验证 URL。

编辑与 QA 采用 `Jaycob-jh/editorial-agent-framework` 的 technical-docs 路线：数字、ISBN、课程号、URL 和不确定性边界严格保留。同步更新 MkDocs 导航、凸优化章节、学习路线、现代参考资料与文档首页，并建立每小时巡检日志。
