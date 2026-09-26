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

多数脚本只依赖 NumPy / Matplotlib / SciPy；wavelet 示例额外依赖 PyWavelets。

> 建议：先阅读对应文档，再运行实验；把参数改坏、加噪声、改变采样率，往往比“得到漂亮图”更能理解数学。