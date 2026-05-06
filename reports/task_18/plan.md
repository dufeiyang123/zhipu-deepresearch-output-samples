# Section 1：章节研究计划

## Chapter 1：GCS 算法数学基础与核心原理
### 研究目标
- 建立 GCS（Graph of Convex Sets）算法的完整数学框架认知，回答"GCS 如何将离散图搜索与连续凸优化统一为一个可求解的优化问题"
- 子话题：凸集图的形式化定义、SPP-GCS 的 MICP 建模、凸松弛与求解策略、Bézier 曲线参数化与轨迹优化

### 关键发现
- 发现 1：GCS 定义为有向图 $\mathcal{G}:=(\mathcal{V},\mathcal{E})$，每个顶点 $v$ 关联非空紧凸集 $\mathcal{X}_v \subseteq \mathbb{R}^n$ 和连续决策变量 $x_v \in \mathcal{X}_v$；每条边 $e=(u,v)$ 关联凸边长度函数 $\ell_e(x_u,x_v)$。SPP-GCS 同时优化离散路径 $p$ 和连续顶点位置 $x_v$，在固定路径时退化为凸优化，在固定位置时退化为经典最短路 [Marcucci et al. 2024 SIAM](https://epubs.siam.org/doi/10.1137/22M1523790 "Shortest Paths in Graphs of Convex Sets, SIAM J. Optim. 34(1):507-532")。
- 发现 2：SPP-GCS 的 MICP 公式（Equation 5.5）引入二值流变量 $y_e \in \{0,1\}$ 和辅助变量 $z_e:=y_e x_u$，目标函数使用边长度函数的**透视函数**（perspective function），约束包括流守恒、度约束和透视锥约束。MICP 规模为 $O(|\mathcal{E}|)$ 个二值变量、$O(n|\mathcal{E}|)$ 个连续变量。Theorem 5.7 证明 MICP 最优值等于原始 SPP-GCS 最优值 [Marcucci et al. 2024 SIAM](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci21.pdf "Equation (5.5), Theorem 5.7")。
- 发现 3：SPP-GCS 是 NP-hard 问题（Theorem 3.1，通过哈密顿路径问题归约证明）；即使图为无环、凸集两两不相交、边长度正齐次，仍为 NP-hard（Theorem 3.2）[Marcucci et al. 2024 SIAM](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci21.pdf "Theorems 3.1-3.2")。
- 发现 4：凸松弛仅需将 $y_e \in \{0,1\}$ 放松为 $y_e \geq 0$。紧度保证条件（Lemma 7.4）：当 $Y$ 为多面体且 $\hat{y}$ 为极端点时松弛精确。实验表明在欧氏距离下凸松弛几乎总是精确的；欧氏距离平方下名义参数最大松弛间隙为 2.1%，高维(n=20)最大 28.9%。透视公式显著优于 McCormick 包络松弛（McCormick 中位间隙 29%–34%，求解时间慢 10–13 倍）[Marcucci et al. 2024 SIAM](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci21.pdf "Lemma 7.4, Section 9.2")。
- 发现 5：运动规划中每个安全凸区域关联 Bézier 曲线（轨迹段和时间缩放），碰撞规避通过 Bézier 凸包性质保证（所有控制点 $\in Q_i$ 则整条曲线 $\subseteq Q_i$），$C^\kappa$ 连续性通过匹配端点各阶导数控制点实现（线性等式约束）。安全集为多面体时生成 MILP，为二次曲面时生成 MI-SOCP，均有高效求解器支持 [Marcucci et al. 2023 Science Robotics](https://arxiv.org/abs/2205.04422 "Motion Planning around Obstacles with Convex Optimization, Sections 5.2-5.6")。
- 发现 6：实际求解采用"凸松弛 + 随机化深度优先舍入"策略，默认运行 10 条路径或 100 次试探。最优性界自动获得：$C_{\text{relax}} \leq C_{\text{opt}} \leq C_{\text{round}}$。7-DOF KUKA 臂上 GCS 轨迹短于 PRM 且运行时间更低（0.01–0.14s vs 0.20–0.26s），舍入解全局最优；14-DOF 双臂任务 4.0–12.9s 完成，最优性间隙 ≤3.3%；四旋翼 100 个随机环境中 95% 实例最优性间隙 <1% [Marcucci et al. 2023 Science Robotics](https://arxiv.org/abs/2205.04422 "Sections 7.3-7.5")。

### 可用图片
- 无本地可直接使用的图片素材

### 仍需补充
- Marcucci 2024 MIT 博士论文全文可能包含更系统的复杂度分析和额外紧度定理，本次未获取全文
- 对偶方法在原文仅涉及 Lemma 4.9（透视锥与有效不等式锥的对偶关系），无独立成章的对偶求解策略描述
- 原文使用 MOSEK 默认分支定界策略，无针对 SPP-GCS 的定制分支定界算法描述

## Chapter 2：GCS 在机器人路径规划中的应用现状
### 研究目标
- 系统梳理 GCS 框架在机器人运动规划领域的应用全景，回答"GCS 已在哪些场景中验证了有效性、当前技术边界在哪里"
- 子话题：操作臂避障轨迹规划标杆应用、GCS 扩展变体概览（GCS*、ST-GCS、GGCS 等）、与采样规划器的性能对比、pipeline 瓶颈识别

### 关键发现
- 发现 1：在 7-DOF KUKA iiwa 的 5 个操控任务中，GCS 运行时间 0.01–0.14 秒低于 PRM（0.20–0.26 秒），轨迹长度均短于 PRM，全部舍入解全局最优（$\delta_{\text{opt}}=0\%$），认证最优性间隙平均 4.1%、最大 13.0% [Marcucci et al. 2023 Science Robotics](https://arxiv.org/abs/2205.04422 "Section 7.4")。14-DOF 双臂任务 4.0–12.9 秒完成，最优性间隙 ≤3.3%；四旋翼 100 个随机环境中 95% 实例 $\delta_{\text{opt}}<1\%$ [Marcucci et al. 2023 Science Robotics](https://arxiv.org/abs/2205.04422 "Sections 7.3-7.5")。
- 发现 2：GCS*（Chia et al. 2024, WAFR）将 A* 推广到 GCS，可处理隐式超大规模图（STACK 任务 $1.3\times10^9$ 顶点/$8.5\times10^{17}$ 边）。采样版 GCS* 在 21.9 秒内求解，而 IxG* 超 10 小时未解出 [Chia et al. 2024](https://arxiv.org/abs/2407.08848 "GCS*, WAFR 2024, Table 2")。
- 发现 3：IxG/IxG*（Natarajan et al. 2024, RSS）交替执行图搜索和轨迹优化避免完整 MICP，在多臂装配任务中显著加速，但完备性依赖边约束可联合满足的假设 [Natarajan et al. 2024 RSS](https://arxiv.org/abs/2410.08909 "INSATxGCS, RSS 2024")。
- 发现 4：Multi-Query GCS（Morozov et al. 2024, WAFR）通过 SDP 预计算 cost-to-go 下界、在线短视界凸规划增量生成路径，在线规划速度快达两个数量级 [Morozov et al. 2024](https://arxiv.org/abs/2409.19543 "Multi-Query SPP in GCS, WAFR 2024")。
- 发现 5：GGCS（Cohn et al. 2023 RSS / 2024 IJRR）将 GCS 推广到黎曼流形，处理含移动底座或连续旋转关节的机器人 [Cohn et al. 2023/2024](https://arxiv.org/abs/2305.06341 "GGCS, RSS 2023 / IJRR 2024")。
- 发现 6：Fast Path Planning（Marcucci et al. 2024 IEEE TRO）针对大量轴对齐盒（25,600 个盒子离线仅 25 秒），在线阶段比 MICP 快 6–26 倍，路径代价接近全局最优（1.0001 vs 1.0）[Marcucci et al. 2024 TRO](https://www-leland.stanford.edu/~boyd/papers/pdf/fpp.pdf "Fast Path Planning, IEEE TRO 40, pp.3795-3809")。
- 发现 7：ST-GCS（Tang et al. 2025, IROS 2025）将 GCS 扩展至时空域解决多机器人运动规划。PBS+ST-GCS 在 complex 地图 10 机器人时保持 100% 成功率，而 SP+ST-RRT* 和 SP+T-PRM 在 $n>2$ 时几乎完全失败，运行时间快 1–2 个数量级 [Tang et al. 2025](https://arxiv.org/abs/2503.00583 "ST-GCS, IROS 2025")。
- 发现 8：GHOST（Tang & Ma 2025, AAAI 2026）定义并求解 GCS-TSP（凸集图上的旅行商问题），采用分层搜索架构，比统一 MICP 基线快数个数量级 [Tang & Ma 2025](https://arxiv.org/abs/2511.06471 "GHOST, AAAI 2026")。
- 发现 9：PGD-GCS（Garg et al.）通过后处理"去畸变"策略扩展 GCS 至非凸目标函数，在双臂搬运和 3D 旋转规划中显著改善路径质量 [Garg, Cohn & Tedrake 2024](https://shrutigarg914.github.io/pgd-gcs-results/ "PGD-GCS 项目页")。TL-GCS（Kurtz & Lin 2023 IEEE TRO 39(5):3791-3804）将 LTL 运动规划转化为 GCS 问题 [Kurtz & Lin 2023](https://doi.org/10.1109/TRO.2023.3299753 "TL-GCS, IEEE TRO")。
- 发现 10：GCS pipeline 核心瓶颈在于凸集生成阶段——依赖用户提供种子点，人工成本高且覆盖率不确定。Marcucci et al. 2024 TRO 明确指出 GCS-Opt 无法扩展至大量安全集 [Marcucci et al. 2024 TRO](https://www-leland.stanford.edu/~boyd/papers/pdf/fpp.pdf "Section I-A")。GCS* 中多面体包含检查成本极高（AROUND 任务 7.5 小时 vs 采样版 26.2 秒）[Chia et al. 2024](https://arxiv.org/abs/2407.08848 "Table 2")。ST-GCS 中图膨胀问题在多机器人场景下构成瓶颈 [Tang et al. 2025](https://arxiv.org/abs/2503.00583 "Figure 5")。

### 可用图片
- 无本地可直接使用的图片素材

### 仍需补充
- GCS* 与标准 GCS 凸松弛的直接加速倍数对比数据（标准 GCS 在超大规模图上不可行，缺乏直接对比）
- IxG 在 7-DOF 操作臂上相对 GCS-Opt 的具体加速倍数需从论文 PDF 提取
- GGCS 的具体求解时间和路径质量定量数据需从论文实验部分补充
- Multi-Query GCS 的绝对求解时间和路径代价数值需从论文实验表格补充
- 更高维度（>14-DOF）的 GCS 系统性实验数据尚缺
- 凸集生成阶段（C-IRIS/IRIS-NP）的具体离线时间数据需从原始论文补充

## Chapter 3：凸集生成方法现状与局限性分析
### 研究目标
- 深入剖析 GCS pipeline 中凸集（安全区域）生成环节的技术现状及其瓶颈，回答"为什么凸集生成是当前 GCS 实用化的主要障碍"
- 子话题：IRIS 系列算法演进（IRIS → C-IRIS → IRIS-NP → FastIRIS）、种子点依赖问题、凸集质量对 GCS 求解的影响、GPU 加速凸集计算的最新进展

### 关键发现
- 发现 1：IRIS（2014）是凸集生成领域的奠基工作，核心为 QP（分离超平面生成）与 SDP（最大体积内接椭球）的交替迭代，要求障碍物为显式凸集，且需用户提供种子点。2D/3D 环境中对 $10^6$ 个障碍物仅需几秒收敛，但无法处理多连杆机器人的非凸配置空间障碍物，且 5% 情况下最终区域可能不包含初始种子点 [Deits & Tedrake 2014](https://groups.csail.mit.edu/robotics-center/public_papers/Deits14.pdf "Computing Large Convex Regions of Obstacle-Free Space through Semidefinite Programming, WAFR 2014")。
- 发现 2：C-IRIS（2023）首次在配置空间中生成经数学证明（certified）无碰撞凸多面体，使用有理参数化和 SOS 规划，适用于任意维度，已在 7-DOF KUKA、6-DOF UR3e、12-DOF 双臂上验证。但计算时间极高——在约束双臂场景中，IRIS-NP 平均 305.97 秒/区域，而较新的 IRIS-ZO 仅需 1.82 秒/区域，C-IRIS/IRIS-NP 比新算法慢约 100–500 倍 [Dai et al. 2023 IJRR](https://arxiv.org/abs/2302.12219 "Certified Polyhedral Decompositions of Collision-Free Configuration Space, IJRR 43(9):1322-1341, 2024") [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "Faster Algorithms for Growing Collision-Free Regions, Table I")。
- 发现 3：IRIS-NP（2023）用非线性优化（NLP）替代 QP 寻找分离超平面，在任务空间中编码碰撞约束，以概率方式保证无碰撞，速度远快于 C-IRIS。但终止条件依赖连续不可行次数的手工调参，NLP 局部性导致无法保证全局可行性，且大量碰撞对求解不可行 NLP 造成严重计算浪费 [Petersen & Tedrake 2023](https://arxiv.org/abs/2303.14737 "Growing Convex Collision-Free Regions in Configuration Space using Nonlinear Programming")。
- 发现 4：FastIRIS（2024）包含 IRIS-ZO（零阶优化）和 IRIS-NP2 两个算法。IRIS-ZO 完全绕过 NLP 求解器，仅用采样+碰撞检测+二分搜索，引入 Chernoff 界概率终止条件（用户可指定碰撞体积分数 $\varepsilon$ 和置信度 $\delta$）。在 8 个基准环境（2–14 DOF）上，IRIS-ZO 比 IRIS-NP 快 15.5 倍，超平面数减少 1.4 倍；在约束双臂场景中 IRIS-ZO 平均 1.82 秒/区域（85 个超平面）、IRIS-NP2 Greedy 平均 1.65 秒/区域（56 个超平面），碰撞违反率均低于 1% [Werner et al. 2024](https://arxiv.org/html/2410.12649v1 "Faster Algorithms for Growing Collision-Free Convex Polytopes, arXiv:2410.12649") [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "Table I")。
- 发现 5：种子点依赖是所有 IRIS 系列算法的共同瓶颈。在高维配置空间（≥7-DOF）中人类无法直觉选择好的种子分布，随机播种导致"非常低效的分解"。VCC（Visibility Clique Cover，ICRA 2024）是首个系统化自动种子方案：在 $\mathcal{C}_{\text{free}}$ 中均匀采样构建可见性图、分解为大团、以团质心初始化 IRIS。在 7-DOF 场景中约 46 个区域 1 小时覆盖 70% 自由空间，比随机种子 IRIS-NP 减少 10 倍区域数和计算时间 [Werner et al. 2024 VCC](https://groups.csail.mit.edu/robotics-center/public_papers/Werner23.pdf "Approximating Robot Configuration Spaces with few Convex Sets using Clique Covers of Visibility Graphs, ICRA 2024")。
- 发现 6：VCC 自身面临可扩展性限制——在约束双臂场景中可见性图构建成为主要瓶颈，437 秒仅生成 8 个区域、覆盖率不足 1%，其中仅 21 秒用于区域生成，其余全部用于可见性图构建 [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "Section VI Discussion, VCC bottleneck analysis")。
- 发现 7：凸集质量直接影响 GCS 性能——每个凸集的超平面数决定约束规模，集合总数决定图顶点和边数，两者共同控制 MICP/凸松弛的计算复杂度。标准 GCS-Opt 在凸集数量极大时不可扩展（10,150 盒子场景即无法求解）[Werner et al. 2024](https://arxiv.org/html/2410.12649v1 "Section 1, arXiv:2410.12649") [Marcucci et al. 2024 TRO](https://www-leland.stanford.edu/~boyd/papers/pdf/fpp.pdf "Section I-A")。
- 发现 8：GPU 加速的 EI-ZO（RSS 2025）将种子从"点"扩展为"线段"，在 DRM 路径的每个线段周围膨胀凸多面体，所有操作在 GPU 上并行。Franka 7-DOF 仿真中平均仅生成 3.49 个凸集，凸集构建 135.1 ms，端到端规划 152.5±89.1 ms（最短路径），比非线性轨迹优化快约 20 倍，成功率从 72.5% 提升至 100%。硬件验证（KUKA 7-DOF + RTX 2080Ti）15 次规划平均 0.82 秒 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Superfast Configuration-Space Convex Set Computation on GPUs, RSS 2025, Tables I-II")。
- 发现 9：EI-ZO 的关键局限是路径依赖性——凸集仅覆盖初始 DRM 路径附近空间，若初始路径质量差则可能不包含高质量轨迹。膨胀多条路径并用完整 GCS 求解的改善仅为边际 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Section VIII Limitations, RSS 2025")。
- 发现 10：Drake 框架中 C-IRIS 和 IRIS-NP 均已集成可用；FastIRIS（IRIS-ZO/IRIS-NP2）位于独立仓库；GPU 加速的 CSDecomp 工具箱已开源于 https://github.com/wernerpe/csdecomp [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Section IV-D, CSDecomp GitHub")。

### 可用图片
- 无本地可直接使用的图片素材

### 仍需补充
- C-IRIS 在 7-DOF/12-DOF 上的具体计算时间数据需从 Dai et al. IJRR 2024 原文实验表格补充
- 凸集覆盖率与 GCS 求解质量的定量关系（如"覆盖率 X% 对应最优性间隙 Y%"）目前无直接实验数据
- FastIRIS 在标准 7-DOF 单臂基准上的绝对计算时间需从 Werner et al. 2024 Figure 6 精确读取
- IRIS-NP 原始论文中未发现种子点自动选取的系统讨论，该议题首次出现在 VCC 论文中

## Chapter 4：PRM 算法原理及其作为自动种子生成器的可行性
### 研究目标
- 从 PRM 算法的理论性质出发，论证其作为 GCS 凸集自动种子生成器的可行性与适配条件，回答"PRM 生成的路线图节点是否适合作为 IRIS 类算法的种子点"
- 子话题：PRM 核心机制回顾、PRM 变体与采样增强策略、PRM 节点作为 IRIS 种子点的理论分析、耦合挑战（采样密度与凸集数量权衡等）

### 关键发现
- 发现 1：PRM（1996）分为学习阶段（$\mathcal{C}_{\text{free}}$ 中均匀采样 + 碰撞检测 + $r$-邻域局部规划器建边）和查询阶段（起终点连接 + 图搜索），是面向静态多查询场景的采样规划方法 [Kavraki et al. 1996](https://www.kavrakilab.org/publications/kavraki-svestka1996probabilistic-roadmaps-for.pdf "Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces, IEEE Trans. Robotics 12(4):566-580, 1996")。
- 发现 2：PRM 概率完备性（Kavraki et al. 1998）：对于鲁棒可行的规划问题（存在强 $\delta$-clearance 路径），失败概率随样本数指数衰减 $P > 1 - e^{-an}$。关键前提为路径需距碰撞边界至少 $\delta > 0$，均匀随机采样自然满足稠密性要求 [Karaman & Frazzoli 2011](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa19/optreadings/rrtstar.pdf "Theorem 15, IJRR 30(7):846-894, 2011")。
- 发现 3：标准 PRM 不是渐近最优的（Theorem 29），其跳过同分量连接的策略使路径代价不收敛到最优值。PRM* 通过连接半径 $r(n) = \gamma(\log(n)/n)^{1/d}$ 实现渐近最优（Theorem 34），计算复杂度 $O(n\log n)$，$k$-近邻版本取 $k(n) = k_{\text{PRM}} \log(n)$（$k_{\text{PRM}} = 2e$ 为通用有效选择）[Karaman & Frazzoli 2011](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa19/optreadings/rrtstar.pdf "Theorems 29, 30, 34, Algorithm 4: PRM*, IJRR 2011")。
- 发现 4：Gaussian PRM（Boor et al. 1999）以高斯分布采样点对、仅保留一碰一非碰的那个无碰撞配置，使采样偏向障碍物边界/窄通道附近。Bridge PRM（Hsu et al. 2003）采样两个碰撞点的无碰撞中点，针对窄通道内部采样。Lazy PRM（Bohlin & Kavraki 2000）延迟碰撞检测到路径验证阶段，减少碰撞检查次数 [Orthey, Chamzas & Kavraki 2024](https://www.kavrakilab.org/publications/orthey2024-review-sampling.pdf "Sampling-Based Motion Planning: A Comparative Review, Annual Reviews 2024")。
- 发现 5：PRM 节点天然满足 IRIS 种子点的无碰撞约束，均匀采样提供对 $\mathcal{C}_{\text{free}}$ 的渐近均匀覆盖。PRM 路线图的连通性为凸集图连通性提供先验保证——通过 PRM 边连接的相邻节点膨胀出的凸集倾向覆盖它们之间的直线路径区域，大概率产生非空交集 [Werner et al. 2024 VCC](https://groups.csail.mit.edu/robotics-center/public_papers/Werner23.pdf "Section I, ICRA 2024") [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "EI-ZO pipeline 连通性保证, RSS 2025")。
- 发现 6：采样密度与凸集数量存在关键权衡——节点过密导致大量冗余凸集，GCS 求解不可扩展。EI-ZO 的路径引导策略将 7-DOF 场景凸集数量控制在平均 3.49 个（对比 VCC 的 46 个）。冗余控制可采用空间稀疏化、贪心增量覆盖或路径引导策略 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Table I, RSS 2025") [Werner et al. 2024 VCC](https://groups.csail.mit.edu/robotics-center/public_papers/Werner23.pdf "VCC 冗余消除, ICRA 2024")。
- 发现 7：端到端计算时间估计——使用 IRIS-ZO（1.82 秒/区域）膨胀 50 个 PRM 种子点约需 91 秒；使用 GPU 加速 EI-ZO 膨胀 3–4 个线段仅需 135.1 ms。传统 IRIS-NP（305.97 秒/区域）膨胀 50 个种子约 4.25 小时，不可接受 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Table I, RSS 2025") [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "Table I")。
- 发现 8：EI-ZO pipeline（RSS 2025）是目前 PRM 与凸集生成结合最成熟的实例。其 DRM 本质为 PRM + 体素碰撞查找表（3000–12000 节点），使用线段（而非点）作为种子，相邻凸集在路径节点处自动相交保证连通。PRM 的多查询特性允许路线图在不同障碍物配置下复用，仅需剪枝碰撞节点 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Section V, Figure 3, RSS 2025")。
- 发现 9：EI-ZO 路径依赖性局限——膨胀多条路径并用完整 GCS 求解改善仅为边际（代价降 3.7%，时间增 29 倍），暗示需更智能的互补路径选择策略（如覆盖不同同伦类）[Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Table I LSCS vs LGCS, Section VIII, RSS 2025")。
- 发现 10：PRM 高维可扩展性挑战——7-DOF Franka 场景中 PRM 成功率和收敛速度不如 RRT-Connect，但 PRM* 在路径代价上收敛更快（4/6 场景最优）；14-DOF 场景 PRM 成功率显著下降 [Orthey, Chamzas & Kavraki 2024](https://www.kavrakilab.org/publications/orthey2024-review-sampling.pdf "Section 6.2: Manipulation Experiments, Figure 5, Annual Reviews 2024")。

### 可用图片
- 无本地可直接使用的图片素材

### 仍需补充
- Kavraki et al. 1996 原始论文概率完备性定理原文（本次通过 Karaman & Frazzoli 2011 间接获取）
- Gaussian PRM 和 Bridge PRM 在窄通道场景的定量加速倍数和成功率提升数据
- PRM 节点密度与 IRIS 凸集覆盖率的直接定量关系（目前无实验数据）
- PRM 在 ≥14-DOF 系统上的路线图构建时间数据

## Chapter 5：PRM + 凸分解 + GCS 自动化 Pipeline 技术方案设计
### 研究目标
- 给出"PRM 自动采样 → 凸集自动生成 → GCS 求解"全自动 pipeline 的完整技术架构设计，回答"这条自动化路径在工程上如何落地、关键技术接口如何衔接"
- 子话题：Pipeline 总体架构（采样-膨胀-求解三阶段）、智能采样策略、凸集自动膨胀与后处理、GCS 求解集成

### 关键发现
- 发现 1：EI-ZO pipeline（RSS 2025）是目前最成熟的端到端参照架构——离线构建 DRM（PRM + 体素碰撞查找表），在线三步执行：DRM 路径查找（毫秒级）→ EI-ZO 凸集膨胀（135.1 ms）→ 轨迹优化（17.4–189.1 ms），端到端 152.5±89.1 ms。碰撞恢复机制在 40.22% 实例中被触发 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Superfast SCS on GPU, RSS 2025, Section VI & Table I")。
- 发现 2：Drake 提供了构建 pipeline 所需的完整 API——`IrisZo()`/`IrisNp2()` 生成凸集，`SetEdgeContainmentTerminationCondition()` 支持以 PRM 边为种子的线段膨胀，`GcsTrajectoryOptimization::AddRegions(regions, order)` 自动基于凸集交集（LP 可行性检查）构建 GCS 边。`GraphOfConvexSets` 底层支持手动图构建和求解 [Drake IRIS API](https://drake.mit.edu/doxygen_cxx/group__planning__iris.html "Drake IRIS 算法族 API") [Drake GcsTrajectoryOptimization](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html "GcsTrajectoryOptimization Class")。
- 发现 3：GCS 边定义基于凸集交集非空——若 $Q_i \cap Q_j \neq \emptyset$ 则建边。边约束集编码 Bézier 控制点的连续性约束（$r_{i,d} = r_{j,0}$ 等线性等式）。边代价为时间 + 路径长度 + 能量的加权组合。安全集为多面体时生成 MILP/MI-SOCP [Marcucci et al. 2023 Science Robotics](https://arxiv.org/abs/2205.04422 "Sections 5.2-5.4, Equations (7)-(10)")。
- 发现 4：凸集图连通性保证策略——(a) PRM 边继承假说（相邻节点凸集大概率交集非空，但非严格保证），(b) 线段种子策略（改用 PRM 边作为 IRIS 种子，利用 `SetEdgeContainmentTerminationCondition()` 或 EI-ZO 严格保证相邻凸集在路径节点处相交），(c) 后验交集检测 + 补膨胀（LP 检查不相交的对在 PRM 边中点补膨胀）[Drake API](https://drake.mit.edu/doxygen_cxx/group__planning__iris.html "SetEdgeContainmentTerminationCondition") [Werner et al. 2024 VCC](https://groups.csail.mit.edu/robotics-center/public_papers/Werner23.pdf "VCC ICRA 2024")。
- 发现 5：采样密度与凸集数量权衡——EI-ZO 路径引导策略平均 3.49 个凸集，VCC 全覆盖需 46 个。稀疏种子策略（均匀网格/最远点/Poisson 盘采样）、贪心增量策略（新凸集显著增加覆盖率时才保留）、混合策略（先路径级膨胀 + 再未覆盖区域补充点种子）均为可行选择。GCS 可扩展性约束凸集总数在数十至低百量级 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Table I, RSS 2025") [Marcucci et al. 2024 TRO](https://www-leland.stanford.edu/~boyd/papers/pdf/fpp.pdf "Section I-A")。
- 发现 6：IRIS 变体选择——IRIS-ZO 最适合大规模批量膨胀（零阶、可 GPU 化、1.82 秒/区域），IRIS-NP2 区域体积更大但依赖 NLP 求解器（1.65 秒/区域 Greedy 模式）。批量并行化三层策略：GPU 内并行（EI-ZO/CSDecomp）、CPU 多线程并行（Drake `parallelism` 参数）、任务级分批并行 [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "Table I") [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Section IV-D CUDA Implementation")。
- 发现 7：冗余凸集处理——体积包含检测（LP 检查）、覆盖增量阈值（蒙特卡洛采样估计重叠比例）、超平面复杂度简化。覆盖率验证使用蒙特卡洛方法，可复用 PRM 未选为种子的节点作为免费测试样本 [Werner et al. 2024 VCC](https://groups.csail.mit.edu/robotics-center/public_papers/Werner23.pdf "VCC 覆盖率评估, ICRA 2024")。
- 发现 8：窄通道检测信号——(a) PRM 采样拒绝率异常高，(b) IRIS 区域体积异常小，(c) PRM 边长且局部连通度低。检测后触发 Gaussian/Bridge PRM 局部加密采样 [Orthey, Chamzas & Kavraki 2024](https://www.kavrakilab.org/publications/orthey2024-review-sampling.pdf "Section 4.1, Annual Reviews 2024")。
- 发现 9：与 EI-ZO pipeline 对比——PRM + IRIS 全覆盖方案离线代价更高（数十秒到数分钟）但覆盖率更高，给 GCS 更多路径选择空间。EI-ZO 膨胀两条路径（LGCS）相比单条仅降低代价 3.7% 但时间增 29 倍，暗示简单增加路径数量回报递减 [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Table I LSCS vs LGCS, Section VIII")。与 VCC 对比——PRM + IRIS 使用标准 PRM $O(N\log N)$ 连接替代 VCC 的 $O(N^2)$ 完全可见性图，可改善高维可扩展性 [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "Section VI VCC bottleneck")。
- 发现 10：NGCSTrajOpt（von Wrangel & Tedrake 2024）扩展 GCS 到非凸代价/约束（如加速度约束），使用凸代理引导 + NLP 舍入。KUKA iiwa 实验 8.4 秒（带加速度约束）vs 纯凸 GCS 5.4 秒，已集成入 Drake [von Wrangel & Tedrake 2024](https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf "Using Graphs of Convex Sets to Guide Nonconvex Trajectory Optimization, 2024")。
- 发现 11：凸集图自动构建四步流程——(1) 种子选定 + IRIS 膨胀生成 `HPolyhedron`，(2) `AddRegions(regions, order)` 自动交集检测建边（$O(N^2)$ LP，$N \leq 100$ 时秒级），(3) 起终点作为 `Point` 嵌入图中，(4) BFS/DFS 连通性验证，断裂处补膨胀 [Drake GcsTrajectoryOptimization](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html "AddRegions 自动边构建")。
- 发现 12：GCS 松弛策略选择——(1) 凸松弛 + 随机化舍入（默认，欧氏距离下几乎精确，Drake 默认 `max_rounded_paths = 5`），(2) 凸限制（已知路径时最快），(3) 完整 MICP（全局最优但 4236.5 ms）。50–100 凸集的中等规模图推荐凸松弛 + 舍入 [Marcucci et al. 2024 SIAM](https://groups.csail.mit.edu/robotics-center/public_papers/Marcucci21.pdf "Section 5.3 & 9.2") [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Table I: LGCS 4236.5 ms")。
- 发现 13：CSDecomp 工具箱（Python/C++/CUDA）提供 GPU 加速碰撞检测、DRM 和 EI-ZO，支持盒体和球体碰撞几何，需 NVIDIA GPU + CUDA 12.x。可与 Drake 的 `IrisZo()` 互补——CSDecomp 负责路径级膨胀，Drake 负责补充覆盖膨胀 [CSDecomp GitHub](https://github.com/wernerpe/csdecomp "CSDecomp: Configuration Space Decomposition Toolbox")。

### 可用图片
- 无本地可直接使用的图片素材

### 仍需补充
- PRM 节点密度与 IRIS 凸集覆盖率的定量关系（目前无直接实验数据）
- PRM 边继承到凸集交集的成功率（文献中缺乏系统实验）
- CSDecomp 与 Drake 的集成接口细节（HPolyhedron 转换）
- 大规模（>100 区域）Drake `AddRegions` 自动交集检测性能数据
- 以"标准 PRM 节点 + IRIS + GCS"完整流程的端到端实验验证（文献中尚无）

## Chapter 6：其他 GCS 优化方向与前沿探索
### 研究目标
- 全景扫描 GCS 算法体系中其他具备潜力的优化方向，回答"除了自动化凸集生成，GCS 框架还有哪些值得关注的改进路径"
- 子话题：求解效率优化（GCS*、Multi-Query GCS）、动态与时变场景扩展（ST-GCS、在线更新）、高维与非欧空间适配（GGCS）、任务级扩展（GCS-TSP/GHOST、多机器人协同）、学习驱动优化

### 关键发现
- 发现 1：GCS*（WAFR 2024）通过两种支配检查实现高效剪枝——ReachesCheaper（代价支配，保最优+完备）和 ReachesNew（可达支配，牺牲最优保完备）。采样版支配检查相对精确版实现约 1000 倍加速。GCS* 是唯一同时支持隐式图、完备和最优的 GCS 求解器，在 STACK 任务（1.3×10⁹ 顶点）中 21.9 秒找到解 [GCS* 原文](https://arxiv.org/abs/2407.08848 "GCS*: Forward Heuristic Search on Implicit Graphs of Convex Sets, WAFR 2024")。
- 发现 2：Multi-Query GCS（WAFR 2024）离线 SDP 预计算凸二次 cost-to-go 下界（6 秒），在线贪心 lookahead 查询中位数 5 ms，比标准 GCS 快约 40 倍、比 PRM（10,000 节点）快约 110 倍，路径长度仅增 7%。二次下界远优于仿射下界（后者 1-step 失败率 27.2%）[Multi-Query GCS](https://arxiv.org/abs/2409.19543 "Multi-Query SPP in GCS, WAFR 2024, Table 1")。
- 发现 3：ST-GCS（IROS 2025）通过将空间凸集沿时间维挤出为时空凸集、引入时间正向流和速度界的线性约束实现时空域规划。ECD 算法每段最多分割为 $2d+2$ 个新凸集，代价 $O(k \cdot d)$ 切割 + $O(|V'|^2)$ 交集检查。图膨胀问题（>1000 边时求解器开始失败）由 PBS 框架有效缓解，PBS+ST-GCS 10 机器人保持 100% 成功率 [ST-GCS 原文](https://arxiv.org/abs/2503.00583 "ST-GCS, IROS 2025, Algorithms 1-3, Figure 5")。
- 发现 4：在线凸集更新仍为开放问题。EI-ZO 碰撞恢复机制仅限局部路径修补，Multi-Query GCS 讨论了在线策略滚动的方向，DRM 可实时剪枝但操作离散节点而非凸集。核心矛盾在于凸集重构计算代价与在线响应时间 [Multi-Query GCS](https://arxiv.org/abs/2409.19543 "Section 6: 在线环境适应讨论") [Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Section VI-B")。
- 发现 5：GGCS（RSS 2023/IJRR 2024）在零曲率流形上可精确归约为标准 GCS（Theorem 3），适用于 SE(2)、所有 1-DOF 关节及其乘积空间。正曲率流形（如 SO(3)/球关节）不可处理（Theorem 5）。PR2（15-DOF）验证平均 25.75 秒 [GGCS 原文](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23.pdf "RSS 2023, Theorems 2-3-5, Table I-II")。
- 发现 6：当前 GCS 最高维度验证为 15-DOF（GGCS PR2），14-DOF 双臂 KUKA 求解 4.0–12.9 秒。>20-DOF 面临凸集生成和求解双重瓶颈 [Marcucci et al. 2023](https://arxiv.org/abs/2205.04422 "14-DOF 实验") [GGCS](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23.pdf "15-DOF 实验")。
- 发现 7：GHOST（AAAI 2026）的分层搜索——高层 Lawler-Murty 按 lower-bound tour cost 枚举抽象 tour，低层 abstract-path-unfolding（多标签 A* 式搜索 + LBG 启发式）展开为可行路径。所有 Bézier-GCS 实例上 MICP 基线失败，GHOST 全部成功。应用覆盖 2D/3D 覆盖规划、巡检和 7-DOF TAMP [GHOST 原文](https://arxiv.org/abs/2511.06471 "GHOST, AAAI 2026, Algorithms 1-2, Theorems 1-4")。
- 发现 8：学习驱动优化方向——Multi-Query GCS 的 SDP cost-to-go 合成可视为结构化学习；学习暖启动轨迹优化、学习采样策略可迁移至 GCS pipeline。目前无论文将深度学习直接用于 GCS 路径搜索或凸集质量优化 [Multi-Query GCS](https://arxiv.org/abs/2409.19543 "Section 6: future work on MCTS-inspired rollouts")。
- 发现 9：PGD-GCS 解决非欧参数化下的路径畸变问题（投影梯度下降后处理），与 GGCS 互补。NGCSTrajOpt 将 GCS 扩展至非凸约束（加速度等），KUKA 实验 8.4 秒含加速度约束 [PGD-GCS](https://shrutigarg914.github.io/pgd-gcs-results/ "PGD-GCS 2024") [NGCSTrajOpt](https://groups.csail.mit.edu/robotics-center/public_papers/Wrangel24.pdf "NGCSTrajOpt, IROS 2024")。
- 发现 10：Fast Path Planning（TRO 2024）绕过完整 GCS，用线图+凸交替法处理 25,600 盒子场景（离线 25 秒，在线 7.72 秒），代价 1.0001 vs 最优 1.0。表明特殊结构凸集可用专用算法突破通用 GCS 规模瓶颈 [Fast Path Planning](https://www-leland.stanford.edu/~boyd/papers/pdf/fpp.pdf "IEEE TRO 40:3795-3809, 2024")。
- 发现 11：凸集质量的形式化理论下界（如"给定 $\mathcal{C}_{\text{free}}$ 复杂度，GCS 至少需要多少凸集保证指定最优性间隙"）仍为开放理论问题。

### 可用图片
- 无本地可直接使用的图片素材

### 仍需补充
- GCS* 在标准运动规划场景（操作臂避障）与凸松弛的直接定量对比数据（论文实验集中于接触规划）
- "Augmented Graphs of Convex Sets" 优先级约束论文完整内容
- >20-DOF 系统的 GCS 端到端性能数据
- 专门用于 GCS 路径搜索的机器学习方法（GNN/Transformer 等）
- ECD 在 7-DOF 或更高维时空中的计算代价实测数据

## Chapter 7：综合可行性评估与实施路线图
### 研究目标
- 对全文各优化方向进行系统性的可行性评估，回答"哪些方案在现有技术条件下可优先落地、实施路径和预期收益如何"
- 子话题：PRM+凸分解+GCS 方案综合评估、各优化方向横向对比、分阶段实施路线图、开放问题与未来研究方向

### 关键发现
- 发现 1：Drake 中 `GcsTrajectoryOptimization`、`IrisZo()`、`IrisNp2()` 三大核心 API 均标记为 **experimental**（API 可能不经兼容过渡直接更改），但功能链已完整——`AddRegions()` 自动建边、`SolvePath()` 凸松弛+舍入、`SetEdgeContainmentTerminationCondition()` 线段种子等均可用 [Drake GcsTrajectoryOptimization](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html "experimental 标记") [Drake IRIS API](https://drake.mit.edu/doxygen_cxx/group__planning__iris.html "IrisZo/IrisNp2 experimental 标记")。
- 发现 2：Marcucci 发布独立 Python 库 `gcsopt`（MIT 许可证，CVXPY 语法），可作为 Drake 之外的轻量级 GCS 原型验证工具 [gcsopt GitHub](https://github.com/TobiaMarcucci/gcsopt "GCSOPT: Python library for optimization over GCS")。
- 发现 3：CSDecomp 当前仅支持盒体和球体碰撞几何（圆柱/胶囊在 TODO 中），需 Ubuntu 22.04 + NVIDIA GPU（RTX 3090/2080Ti）+ CUDA 12.x，从源码编译。网格碰撞体的复杂工业场景无法使用 [CSDecomp GitHub](https://github.com/wernerpe/csdecomp "碰撞几何限制, TODO, 硬件要求")。
- 发现 4：截至 2026 年 4 月，公开文献中尚无"标准 PRM 节点 → IRIS 批量膨胀 → GCS 求解"完整 pipeline 的端到端实验。最接近的是 EI-ZO（DRM 线段膨胀，152.5 ms）、VCC（可见性团覆盖，46 区域 70% 覆盖率 1 小时）和 Multi-Query GCS（IRIS clique seeding + SDP 预计算）[Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "RSS 2025") [Werner et al. 2024 VCC](https://groups.csail.mit.edu/robotics-center/public_papers/Werner23.pdf "ICRA 2024") [Morozov 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Morozov25b.pdf "MIT 硕士论文")。
- 发现 5：GCS* 开源于 `shaoyuancc/large_gcs`（Python，依赖 Drake），未集成入 Drake 主仓库。ST-GCS 开源于 `reso1/stgcs`（GPL-3.0，纯 Python）。Multi-Query GCS 无独立公开代码 [large_gcs GitHub](https://github.com/shaoyuancc/large_gcs "GCS* 实现") [stgcs GitHub](https://github.com/reso1/stgcs "ST-GCS 实现")。
- 发现 6：PRM+IRIS+GCS 技术成熟度——三个核心组件在 Drake 生态中均有原生接口（CollisionChecker 采样 + IrisZo 膨胀 + GcsTrajectoryOptimization 自动建图求解），但端到端整合尚未有人验证。
- 发现 7：性能收益估算——50 个 PRM 种子 + IRIS-ZO 膨胀约 91 秒无并行（CPU 多线程降至 10–20 秒），覆盖率有望接近 VCC 的 70%（46 区域基准），PRM 的 $O(N\log N)$ 连接比 VCC 的 $O(N^2)$ 可见性检查更快。全覆盖方案给 GCS 更多路径选择空间，比 EI-ZO 单路径方案潜在路径质量改善更大 [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "IRIS-ZO 1.82 s/region") [Werner et al. 2024 VCC](https://groups.csail.mit.edu/robotics-center/public_papers/Werner23.pdf "46 regions/70% coverage")。
- 发现 8：主要技术风险——(a) 凸集数量可扩展性（GCS MICP 数百凸集时瓶颈），(b) 点种子连通性非严格保证需后验检测+补膨胀，(c) 14-DOF 以上 IRIS 区域体积指数缩小，(d) CSDecomp 碰撞几何限制 [Marcucci et al. 2024 TRO](https://www-leland.stanford.edu/~boyd/papers/pdf/fpp.pdf "Section I-A: GCS 不可扩展")。
- 发现 9：横向对比——EI-ZO 适合在线实时（152.5 ms，3.49 凸集，路径依赖），VCC 适合离线高覆盖但高维不可扩展（437 秒 8 区域 <1% 覆盖率于约束双臂），PRM+IRIS 介于两者（离线数分钟，覆盖率接近 VCC，采样效率优于 VCC）[Werner et al. 2025](https://arxiv.org/html/2504.10783v1 "Table I") [Cohn, Werner & Tedrake 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Cohn25a.pdf "Section VI")。
- 发现 10：Multi-Query GCS 在静态多查询场景独特价值——离线 SDP 6 秒，在线 5 ms，快 GCS 40 倍、快 PRM 110 倍，路径增 7%。PRM+IRIS 全覆盖方案 + Multi-Query 预计算可达工业级在线响应 [Morozov 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Morozov25b.pdf "Section 4.3")。
- 发现 11：短期原型（3–6 个月）——纯 Drake API 实现，200–300 行 Python：CollisionChecker 均匀采样 → 贪心选种子 → IrisZo 批量膨胀（CPU 多线程）→ AddRegions 自动建图 → SolvePath 求解 [Drake IRIS API](https://drake.mit.edu/doxygen_cxx/group__planning__iris.html "IrisZo, IrisFromCliqueCoverOptions") [Drake GcsTrajectoryOptimization](https://drake.mit.edu/doxygen_cxx/classdrake_1_1planning_1_1trajectory__optimization_1_1_gcs_trajectory_optimization.html "AddRegions")。
- 发现 12：中期集成（6–12 个月）——引入线段种子策略（`SetEdgeContainmentTerminationCondition()` 保证连通）+ Multi-Query SDP 预计算实现在线 <10 ms 查询 [Drake API](https://drake.mit.edu/doxygen_cxx/group__planning__iris.html "SetEdgeContainmentTerminationCondition") [Morozov 2025](https://groups.csail.mit.edu/robotics-center/public_papers/Morozov25b.pdf "Section 3.4: SDP synthesis")。
- 发现 13：远期目标（1–2 年）——离线高覆盖率基底 + 在线 EI-ZO 增量膨胀的混合架构，需 CSDecomp 扩展碰撞几何支持 + Drake API 从 experimental 毕业 [CSDecomp GitHub](https://github.com/wernerpe/csdecomp "TODO: cylinder/capsule")。
- 发现 14：Drake 生态内可直接集成——IrisZo/IrisNp2/IrisNp、IrisFromCliqueCover、SetEdgeContainmentTerminationCondition、GcsTrajectoryOptimization、GraphOfConvexSets。Drake 外需独立维护——CSDecomp（GPU EI-ZO）、GCS*（large_gcs）、Multi-Query GCS（需自行实现）、ST-GCS（stgcs，GPL-3.0）、gcsopt（MIT）。

### 可用图片
- 无本地可直接使用的图片素材

### 仍需补充
- PRM 节点密度与 IRIS 凸集覆盖率的定量关系（需实验验证）
- GCS* 在操作臂避障场景下与凸松弛的直接性能对比数据
- Multi-Query GCS 的开源代码可用性（论文未附独立仓库）
- CSDecomp 在 14-DOF 以上场景的 GPU 加速效果和内存需求

# Section 2：给 Write 阶段的执行建议

- **时间口径**：研究区间覆盖 2025年4月至2026年10月（过去12个月 + 未来6个月），以当前日期 2026-04-02 为锚点。
- **逻辑递进与章节衔接**：Chapter 1-2 建立"GCS 是什么、能做什么"的认知基础；Chapter 3 承上启下提炼凸集生成瓶颈；Chapter 4-5 围绕用户核心关切（PRM + 凸分解自动化方案）逐层展开；Chapter 6 拓宽视野提供横向对比；Chapter 7 回收全文做决策总结并给出分阶段实施路线图。各章末段应设置过渡语句。
- **核心口径统一**：Chapter 3 对凸集生成瓶颈的定性结论（种子点依赖、IRIS-ZO 1.82 秒/区域、VCC 高维不可扩展）须与 Chapter 5 方案设计中的假设前提保持一致；Chapter 2 中 GCS 与 PRM 的性能对比数据（GCS 0.01–0.14s vs PRM 0.20–0.26s）应与 Chapter 4 中 PRM 能力描述呼应。
- **关键判断核验清单**：(1) IRIS-ZO/IRIS-NP2 在约束双臂场景的时间数据已核实至 Cohn et al. 2025 Table I（1.82s/1.65s/区域）；(2) PRM 概率完备性已通过 Karaman & Frazzoli 2011 Theorem 15 间接确认（Kavraki 1996 原文待补充原始定理表述）；(3) GPU 加速方案（EI-ZO）已确认适用 7-DOF + RTX 3090/2080Ti，14-DOF 以上未验证；(4) GCS* 支配检查机制已核实至 Chia et al. 2024 原文，但缺少操作臂避障场景的定量对比。
- **Drake API experimental 状态**：`GcsTrajectoryOptimization`、`IrisZo()`、`IrisNp2()` 均标记为 experimental，写作时应明确提示接口稳定性风险，避免给出"生产就绪"的判断。
- **端到端实验空白**：全文须明确指出截至 2026 年 4 月，"标准 PRM 节点 + IRIS + GCS"完整 pipeline 尚无公开实验数据，方案可行性论证基于组件级证据的合理外推和工程推理，应标注为"理论分析"或"工程推测"。
- **术语符号体系**：全文在 Chapter 1 建立统一符号表（$\mathcal{G} = (\mathcal{V}, \mathcal{E})$、$\mathcal{X}_v$、$y_e$ 等），后续章节严格复用；"凸集""凸区域""安全区域"等近义术语应在首次出现时明确等价关系。
- **受众定位**：具备运动规划基础知识的机器人工程师或研究者。Chapter 1 数学推导兼顾严谨与可读性（关键推导给直觉解释）；Chapter 5 方案设计达到可指导原型实现的粒度（含 Drake API 调用示意和四步自动构建流程）。
- **避免过度承诺**：对缺乏实验验证的环节（PRM 节点密度与覆盖率关系、PRM 边继承到凸集交集的成功率、>14-DOF 场景端到端性能）明确标注为"理论分析"或"工程推测"并说明验证路径。
- **最新文献对齐**：2025 年以来关键工作已覆盖——EI-ZO/Superfast SCS on GPU（RSS 2025）、ST-GCS（IROS 2025）、GHOST（AAAI 2026）、Cohn et al. FastIRIS 约束双臂实验（2025）、Morozov Multi-Query 硕士论文（MIT 2025）、gcsopt 工具库（2025）。
