# 文再文 optbook 程序资源索引

> 核对时间：2026-09-27 19:56–20:00（UTC+8）。本页从 [optbook 官方目录页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/contents/contents.html) 的真实锚点提取，去重后得到 42 个程序说明页；逐页读取后对应到 42 个 `.m` 文件。说明页本轮返回 HTTP 200，程序文件本轮 Range 请求返回 HTTP 206。此为**本轮工具侧可读性**，不保证后续持续可用，也不等于程序已运行或数值结果已验证。

> [上位课程页](optimization-pku-wenzw.md) · [电子讲义索引](optimization-pku-wenzw-lectures.md)。程序资源和讲义资源分别计数；下列程序不能作为“流形约束优化电子讲义已发布”的证据。

## 官方目录列出的程序

| # | 目录中的名称 | 官方说明页 | 页面所链程序 |
|---:|---|---|---|
| 1 | LASSO 问题的梯度下降法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_grad/LASSO_grad_huber_inn.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_grad/LASSO_grad_huber_inn.m) |
| 2 | 实例：利用梯度法解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_grad/demo.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_grad/demo.m) |
| 3 | LASSO 连续化策略 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/LASSO_con/LASSO_con.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/LASSO_con/LASSO_con.m) |
| 4 | BB 步长梯度下降法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/TV_denoise/fminGBB.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/TV_denoise/fminGBB.m) |
| 5 | 实例：Tikhonov 正则化模型用于图片去噪 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/TV_denoise/demo_denoising.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/TV_denoise/demo_denoising.m) |
| 6 | LASSO 问题的次梯度解法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_subgrad/l1_subgrad.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_subgrad/l1_subgrad.m) |
| 7 | 实例：次梯度法解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_subgrad/demo.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_subgrad/demo.m) |
| 8 | LASSO 问题的连续化次梯度法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_subgrad/LASSO_subgrad_inn.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_subgrad/LASSO_subgrad_inn.m) |
| 9 | 实例：连续化次梯度法解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_subgrad/demo_cont.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_subgrad/demo_cont.m) |
| 10 | 牛顿-共轭梯度法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/newton/fminNewton.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/newton/fminNewton.m) |
| 11 | 实例：牛顿-共轭梯度法解逻辑回归问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/newton/demo_lr_Newton.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/newton/demo_lr_Newton.m) |
| 12 | L-BFGS 算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lbfgs/fminLBFGS_Loop.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lbfgs/fminLBFGS_Loop.m) |
| 13 | 实例：L-BFGS算法解基追踪问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lbfgs/demo_bp_lbfgs.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lbfgs/demo_bp_lbfgs.m) |
| 14 | 实例：L-BFGS算法解逻辑回归问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lbfgs/demo_lr_lbfgs.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lbfgs/demo_lr_lbfgs.m) |
| 15 | 信赖域算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/trust_region/fminTR.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/trust_region/fminTR.m) |
| 16 | 实例：信赖域算法解逻辑回归问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/trust_region/demo_lr_tr.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/trust_region/demo_lr_tr.m) |
| 17 | 编码衍射模型的 Wirtinger 梯度下降算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/phase_LM/WF_C.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/phase_LM/WF_C.m) |
| 18 | 编码衍射模型的 Nesterov 加速算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/phase_LM/Nes_C.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/phase_LM/Nes_C.m) |
| 19 | 编码衍射模型的 LM 算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/phase_LM/LM_C.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/phase_LM/LM_C.m) |
| 20 | 实例：编码衍射模型求解 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/phase_LM/demo.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/phase_LM/demo.m) |
| 21 | 实例：罚函数法解基追踪问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/pm_bp/demo_cont.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/pm_bp/demo_cont.m) |
| 22 | 基追踪问题的增广拉格朗日函数法解法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/alm_bp/BP_ALM.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/alm_bp/BP_ALM.m) |
| 23 | 实例：增广拉格朗日函数法解基追踪问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/alm_bp/demo_alm.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/alm_bp/demo_alm.m) |
| 24 | LASSO 问题的近似点梯度法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_proxg/LASSO_proximal_grad_inn.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_proxg/LASSO_proximal_grad_inn.m) |
| 25 | LASSO 问题的 FISTA 算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_proxg/LASSO_Nesterov_inn.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_proxg/LASSO_Nesterov_inn.m) |
| 26 | LASSO 问题的第二类 Nesterov 加速算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_proxg/LASSO_Nesterov2nd_inn.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_proxg/LASSO_Nesterov2nd_inn.m) |
| 27 | 实例：近似点梯度法及其 Nesterov 加速算法求解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_proxg/demo_proxg.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_proxg/demo_proxg.m) |
| 28 | LASSO 问题的近似点算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_ppa/LASSO_ppa.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_ppa/LASSO_ppa.m) |
| 29 | 实例：近似点算法解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_ppa/demo_ppa.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_ppa/demo_ppa.m) |
| 30 | LASSO 问题的分块坐标下降法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_bcd/LASSO_bcd_inn.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_bcd/LASSO_bcd_inn.m) |
| 31 | 实例：分块坐标下降法求解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_bcd/demo_bcd.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_bcd/demo_bcd.m) |
| 32 | LASSO 问题的原始-对偶混合梯度算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_dualalg/LASSO_pdhg_inn.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_dualalg/LASSO_pdhg_inn.m) |
| 33 | 实例：原始-对偶混合梯度算法求解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_dualalg/demo_dualalg.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_dualalg/demo_dualalg.m) |
| 34 | LASSO 原问题的交替方向乘子法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_admm/LASSO_admm_primal.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_admm/LASSO_admm_primal.m) |
| 35 | LASSO 对偶问题的交替方向乘子法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_admm/LASSO_admm_dual.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_admm/LASSO_admm_dual.m) |
| 36 | 实例：交替方向乘子法解 LASSO 问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/lasso_admm/demo_admm.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/lasso_admm/demo_admm.m) |
| 37 | 随机梯度下降算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/sgd.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/stograd/sgd.m) |
| 38 | AdaGrad 算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/Adagrad.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/stograd/Adagrad.m) |
| 39 | RMSProp 算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/RMSProp.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/stograd/RMSProp.m) |
| 40 | AdaDelta 算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/AdaDelta.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/stograd/AdaDelta.m) |
| 41 | Adam 算法 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/Adam.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/stograd/Adam.m) |
| 42 | 实例：随机优化算法求解逻辑回归问题 | [说明页](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/stograd/demo_lr_sg.html) | [MATLAB 程序](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/stograd/demo_lr_sg.m) |

## 整包下载与维护边界

- 官方目录页另列 [程序压缩包](http://faculty.bicmr.pku.edu.cn/~wenzw/optbook/pages/download_code/archive.zip)；本轮 Range 请求返回 HTTP 206，未解压或运行。
- 目录页还列出若干按问题汇总的重复入口，表中按说明页 URL 去重，不将重复锚点计为新程序。
- 本轮目录中确实出现 AdaGrad、RMSProp、AdaDelta、Adam 的说明页和程序文件；此前未证实的路径现有官方页面作一手来源。
- 本轮目录未列出独立流形约束优化讲义 PDF，仍将其保持为待发现项；未通过文件名规律猜测链接。
- 后续若出现 502 或 timeout，仅记录自动抓取状态，不能据此删除官方目录曾列出的资源。
