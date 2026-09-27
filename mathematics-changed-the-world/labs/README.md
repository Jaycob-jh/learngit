# 数学实验室

这些脚本不是为了替代证明，而是把“抽象结构”变成可观察对象。

## 安装

\`\`\`bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-labs.txt
\`\`\`

## 九个核心实验

1. \`01_calculus_accumulation.py\`：累积函数与导数互逆。
2. \`02_taylor_animation.py\`：Taylor 多项式逐阶逼近。
3. \`03_euler_phasor.py\`：复指数旋转与 cosine 投影。
4. \`04_fourier_decomposition.py\`：时域信号与 FFT 频谱。
5. \`05_divergence_flux.py\`：内部散度和边界通量。
6. \`06_residue_numeric.py\`：数值闭路积分读取留数。
7. \`07_bayes_update.py\`：Beta-Bernoulli 顺序更新。
8. \`08_prime_counting.py\`：$\pi(x)$、$x/\log x$、$\operatorname{li}(x)$。
9. \`09_monotone_convergence.py\`：单调简单函数逼近与积分收敛。

## 现代扩展示例

10. \`10_kalman_filter.py\`：状态空间 + Gaussian update。
11. \`11_wavelet_demo.py\`：离散小波多尺度分解。
12. \`12_attention_heatmap.py\`：scaled dot-product attention。
13. \`13_optimization_convexity.py\`：凸性不等式抽样检查 + 条件数对梯度下降收敛的影响。
14. \`14_optimization_modeling.py\`：比较 L2/L1 残差与 ridge/LASSO，观察建模选择如何改变解。
15. \`15_optimization_optimality.py\`：驻点/二阶条件、约束品性与 KKT、Slater 与强对偶。
16. \`16_optimization_unconstrained.py\`：统一比较 Gradient/BB/Newton/BFGS/Trust Region，并演示 Gauss-Newton/LM 非线性最小二乘。
17. \`17_optimization_constrained.py\`：比较二次罚函数与 ALM，并沿 LP 原始–对偶中心路径观察可行性、互补性与 duality gap。
18. \`18_optimization_composite.py\`：同一 LASSO 比较 ISTA、FISTA、循环坐标下降与 ADMM，记录目标值、proximal gradient mapping 及 ADMM 分裂残差。

## Unit 07–09 新脚本

19. \`19_optimization_stochastic_nonsmooth.py\`：次梯度/近端梯度、全梯度/SGD/SVRG，以及标量半光滑 Newton 与奇异导数停止例。
20. \`20_optimization_manifold.py\`：球面与 Stiefel Rayleigh quotient 的 Riemannian gradient、retraction 和非最优驻点教学例。
21. \`21_optimization_sparse_recovery.py\`：Unit 09 项目 A，稀疏重建的 ISTA/FISTA。
22. \`22_optimization_logistic.py\`：Unit 09 项目 B，logistic 分类的全梯度/SGD。
23. \`23_optimization_phase_retrieval.py\`：Unit 09 项目 C，谱初始化/随机初始化的非凸相位恢复。

Unit 07–08 的脚本 19–20 尚未运行。Unit 09 的脚本 21–23 已在固定种子下完成基线和压力运行；[实际运行记录](../docs/courses/optimization-pku-wenzw-unit09-run-log.md)与[原始 CSV](records/unit09/README.md)包含来源页码、命令和失败案例。单次合成数据观察不代表跨种子或真实数据验收。

多数脚本只依赖 NumPy / Matplotlib / SciPy；wavelet 示例额外依赖 PyWavelets。

> 建议：先阅读对应文档，再运行实验；把参数改坏、加噪声、改变采样率，往往比“得到漂亮图”更能理解数学。
