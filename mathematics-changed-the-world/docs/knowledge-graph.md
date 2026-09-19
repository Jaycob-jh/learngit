# 知识图谱：数学不是章节树，而是相互连接的网络

下面这张图强调“思想流向”，不是严格的历史先后，也不是全部依赖关系。

\`\`\`mermaid
flowchart LR
    Calc[微积分] --> Taylor[Taylor 展开]
    Calc --> ODE[微分方程]
    Calc --> Div[散度 / Stokes]
    ODE --> Control[控制论]
    ODE --> Chaos[混沌]
    ODE --> PDE[PDE]

    Complex[复数] --> Euler[Euler 公式]
    Euler --> Fourier[Fourier]
    Fourier --> Residue[复分析 / 留数]
    Fourier --> Wavelet[小波]
    Fourier --> Func[泛函分析]

    Leb[Lebesgue / 测度] --> Prob[概率论]
    Leb --> Func
    Prob --> Bayes[Bayes]
    Prob --> Stoch[随机过程]
    Stoch --> Kalman[Kalman / 状态估计]

    LA[线性代数] --> Func
    LA --> Graph[图论 / 谱图]
    LA --> Optim[优化]
    LA --> Transformer[Transformer]

    Geometry[非欧几何] --> DiffGeo[微分几何]
    Topology[拓扑] --> DiffGeo
    Group[群与对称] --> DiffGeo
    Group --> Physics[现代物理]

    Number[数论 / 素数] --> Riemann[Riemann zeta]
    Complex --> Riemann
    Riemann --> Prime[素数分布]

    Info[信息论] --> Coding[通信 / 编码]
    Prob --> Info
    Info --> Transformer
    Optim --> Transformer
    Num[数值分析] --> Transformer
    Computability[可计算性] --> CS[计算机科学]

    Graph --> GNN[GNN / 网络科学]
    Wavelet --> Signal[信号 / 图像]
    Control --> Robotics[机器人 / 自动系统]
    DiffGeo --> Robotics
    Fourier --> MRI[MRI / 成像]
\`\`\`

## 五条最值得记住的“纵向主链”

### 1. 连续变化链

$
\text{微积分}
\to
\text{ODE/PDE}
\to
\text{守恒律}
\to
\text{数值计算}
\to
\text{控制/天气/工程}.
$

### 2. 频率与函数空间链

$
\text{Euler/复数}
\to
\text{Fourier}
\to
L^2
\to
\text{泛函分析}
\to
\text{小波/量子/PDE}.
$

### 3. 不确定性链

$
\text{概率}
\to
\text{Bayes}
\to
\text{随机过程}
\to
\text{状态估计}
\to
\text{现代统计/生成模型}.
$

### 4. 空间与对称链

$
\text{非欧几何}
+
\text{拓扑}
+
\text{群论}
\to
\text{微分几何/Lie group}
\to
\text{相对论/机器人/3D vision}.
$

### 5. 计算与 AI 链

$
\text{线性代数}
+
\text{微积分}
+
\text{概率}
+
\text{信息论}
+
\text{优化}
+
\text{数值分析}
\to
\text{现代机器学习}.
$

## 横向观察：数学不断重复四种策略

### 换表示
Fourier、Laplace、SVD、eigenbasis、wavelet。

### 局部化
derivative、Taylor、local coordinate、wavelet。

### 把结构抽象出来
group、graph、topology、vector space、probability space。

### 把“过程”本身数学化
differential equation、stochastic process、algorithm、optimization dynamics。