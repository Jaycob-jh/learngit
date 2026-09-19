# 微分几何：在弯曲空间里做微积分

> **核心问题**：曲线、曲面乃至高维空间自身可以弯曲时，长度、角度、最短路径和“曲率”怎样定义？

## 从地图测量开始

微分几何不是先从相对论出现的。地球测量、地图投影、曲面曲率早已提出问题：

- 怎样在球面上测最短路？
- 能不能把地球表面无失真摊平？
- 曲面的弯曲是依赖嵌入空间，还是可以只从曲面内部感知？

Gauss 在 1827/1828 年的 curved surfaces 工作中系统发展曲面内在几何。其著名 Theorema Egregium 表明 Gaussian curvature 是内在量：只住在曲面上的“二维生物”也能通过测量判断曲面是否弯曲。

## Riemann 的升级：空间本身也可以弯

1854 年 Riemann 的 habilitation lecture 把曲面思想推广到任意维：

- 每一点附近像 $\mathbb R^n$；
- 但全局可能弯曲；
- 用 metric tensor 决定局部长度和角度。

局部线元素：

$
ds^2
=
\sum_{i,j}
g_{ij}\,dx^i dx^j.
$

这就是 Riemannian geometry 的核心入口。

## Geodesic：弯曲空间里的“直线”

平面最短路是直线；球面上是大圆弧。

在一般 manifold 上，geodesic 满足

$
\frac{d^2x^k}{dt^2}
+
\Gamma^k_{ij}
\frac{dx^i}{dt}
\frac{dx^j}{dt}
=
0.
$

Christoffel symbols $\Gamma^k_{ij}$ 编码坐标下的连接结构。

## 从曲率到广义相对论

Einstein 的关键思想之一是：引力不再单纯被视作普通力，而与 spacetime geometry 联系。

极简口号是：

$
\text{物质告诉时空怎样弯，时空告诉物质怎样运动}.
$

数学语言需要 Riemann curvature、tensor calculus、geodesic 等。

## 今天的应用

### 机器人
姿态属于 rotation group $SO(3)$，不是普通欧氏向量空间。导航和优化需要在 manifold 上计算。

### 计算机视觉
相机姿态、三维重建、shape space 都大量使用 Lie group / manifold。

### 机器学习
- Riemannian optimization；
- manifold learning；
- SPD matrix geometry；
- information geometry。

### 神经影像
dMRI 中 diffusion tensor 是正定矩阵；直接用普通欧氏平均可能破坏几何结构，因此常考虑其 manifold geometry。

## 与拓扑区别

拓扑允许连续变形，不关心长度角度。  
微分几何要求更细的 smooth structure 和 metric，因此可以谈导数、曲率、geodesic。

可以粗略理解：

$
\text{topology}
\subset
\text{smooth structure}
+
\text{metric geometry}.
$

这不是严格集合包含关系，而是“结构逐层增加”的概念图。

## 与九个核心公式的连接

微积分 → multivariable calculus → tensor → differential geometry。  
散度定理 → Stokes theorem on manifolds。  
Euler / complex → Lie groups 与旋转。  
Lebesgue → integration on manifolds。

## 参考

- MacTutor, Gauss: https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/
- MacTutor, Riemann: https://mathshistory.st-andrews.ac.uk/Biographies/Riemann/
- do Carmo, *Riemannian Geometry*.
- Lee, *Introduction to Riemannian Manifolds*.