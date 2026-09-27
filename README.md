# Math Atlas｜数学知识与应用实验

这个仓库将数学概念、历史背景、核心推导与可复现应用实验放在同一条学习路径中。主要内容位于 [`mathematics-changed-the-world/`](mathematics-changed-the-world/)。

## 从哪里开始

| 目标 | 入口 |
|---|---|
| 按数学主题学习 | [知识库首页](mathematics-changed-the-world/docs/index.md) · [九个核心专题与数学主干](mathematics-changed-the-world/README.md) |
| 从最优化教材与课程进入 | [文再文最优化课程资源](mathematics-changed-the-world/docs/courses/optimization-pku-wenzw.md) · [学习路线](mathematics-changed-the-world/docs/courses/optimization-pku-wenzw-study-roadmap.md) |
| 运行应用实验 | [Python 实验目录](mathematics-changed-the-world/labs/README.md) |
| 核对资料使用程度 | [覆盖情况与证据边界](mathematics-changed-the-world/docs/coverage-matrix.md) · [逐项清单 TSV](mathematics-changed-the-world/docs/coverage-matrix.tsv) |

## 本地使用

```bash
cd mathematics-changed-the-world
python -m pip install -r requirements.txt -r requirements-labs.txt
python -m mkdocs serve
```

实验脚本位于 `labs/`；运行前先阅读对应页面的假设、输入和停止准则。网页构建成功或示例数值运行成功，不代表原始教材与讲义已全部审读，也不代表算法在其他数据上得到相同结果。

## 当前状态

知识库包含九个核心专题、二十条数学主干、十八个既有 Python 实验，以及 Unit 07–09 的五个待审脚本。最优化 Unit 07–10 已建立独立学习页，其中 Unit 09 有三个端到端项目实施稿；新脚本未运行，Unit 10 没有已编译证明。资料索引中的“链接可读”“内容已审读”“代码已运行”分别记录，不互相替代。仓库历史上的 `readme.txt` 保留为早期 Git 练习记录。
