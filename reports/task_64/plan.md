# Section 1：章节研究计划

## Chapter 1：UAV Attitude Control Fundamentals and the Cascaded PID Architecture

### 研究目标
- What is the standard 6-DOF rigid-body dynamics model of a multirotor UAV, and how are attitude (roll, pitch, yaw) dynamics decoupled for control design?
- Why has the cascaded (inner-rate / outer-angle) PID structure become the de facto standard in open-source flight controllers (ArduPilot, PX4, Betaflight)?
- What are the inherent limitations of a fixed-gain PID controller when operating conditions change — varying payloads, center-of-gravity shifts, battery voltage sag, aerodynamic disturbances, and aggressive maneuvering?
- Present the standard block-diagram of the cascaded PID loop, define notation for PID gains (Kp, Ki, Kd), and articulate the "parameter sensitivity problem" that motivates the rest of the report.

### 关键发现
- Bouabdallah (2007) 的 EPFL 博士论文系统给出了基于 Euler-Lagrange 和 Newton-Euler 双形式的四旋翼完整 6-DOF 动力学模型，Newton-Euler 旋转动力学方程含陀螺耦合项和螺旋桨反扭矩，是该领域最被广泛引用的建模参考之一 [Bouabdallah 博士论文](https://infoscience.epfl.ch/server/api/core/bitstreams/3f219824-6427-4d0f-bbd9-fc0812358b2b/content "Design and Control of Quadrotors with Application to Autonomous Flying, EPFL Thesis No. 3727, 2007")。
- Bouabdallah, Noth & Siegwart (2004) 在 IROS 发表的开创性论文（被引超 3000 次）基于简化旋转动力学给出了近悬停解耦模型，PID 实验参数为 P=0.9/I=0.3/D=0.2（roll/pitch），论文明确指出 "this controller will not be able to stabilize the robot in presence of strong perturbations" [Bouabdallah et al. IROS 2004](https://infoscience.epfl.ch/bitstreams/fd82638f-4e59-4c04-ad06-89215ed8ef88/download "PID vs LQ Control Techniques Applied to an Indoor Micro Quadrotor, IEEE/RSJ IROS 2004")。
- Mahony, Kumar & Corke (2012) 在 IEEE RAM 发表的权威教程论文给出了 SE(3) 上的刚体动力学方程及分层/级联控制架构（Figure 5: Trajectory Planner → Position Controller → Attitude Controller → Motor Controller），这正是当今开源飞控的标准架构原型 [Mahony et al. IEEE RAM 2012](http://www.kostasalexis.com/uploads/5/8/4/4/58449511/ram_paper.pdf "Multirotor Aerial Vehicles: Modeling, Estimation, and Control of Quadrotor, IEEE RAM, vol. 19, no. 3, 2012")。
- Beard & McLain (2012) *Small Unmanned Aircraft: Theory and Practice*（Princeton University Press）是小型无人机动力学与控制领域的标准教科书 [Beard & McLain 教材](https://press.princeton.edu/books/hardcover/9780691149219/small-unmanned-aircraft "Small Unmanned Aircraft: Theory and Practice, 2012")。
- ArduPilot 姿态控制采用外环 P / 内环 PID 级联结构，400Hz 控制频率，外环使用 "square root controller" 做非线性映射以改善大角度响应，最终通过 AP_Motors 库混控输出 PWM [ArduPilot 官方文档](https://ardupilot.org/dev/docs/apmcopter-programming-attitude-control-2.html "Copter Attitude Control — ArduPilot Dev Documentation")。
- PX4 采用位置→速度→姿态→角速率四层级联，角速率控制器为 K-PID 形式（支持 Parallel 和 Standard 两种等效形式），提供推力曲线补偿参数 THR_MDL_FAC 应对 PWM-推力非线性，文档指出"the mapping between PWM and static thrust depends highly on the battery voltage" [PX4 官方文档](https://docs.px4.io/main/en/flight_stack/controller_diagrams "PX4 Controller Diagrams") [PX4 PID 调参指南](https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter "Multicopter PID Tuning Guide — PX4")。
- Betaflight 主要工作在角速率模式（Rate/Acro），引入 TPA（Throttle PID Attenuation）机制——高油门时按比例衰减 PID 增益以消除振荡（本质是简化的增益调度），还引入 FeedForward 前馈通道和多级陀螺仪滤波链 [Betaflight PID 文档](https://betaflight.com/docs/development/PID-tuning "PID tuning | Betaflight Official Documentation")。
- PX4 文档指出在悬停点调好的 PID 在满油门时可能出现振荡，电池电压下降会直接改变 PWM-推力映射使已调 PID 不再最优 [PX4 PID 调参指南](https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter "PX4 — PWM to thrust depends on battery voltage")。
- Roy et al. (2021) 综述系统指出经典 PID 仅适用于线性模型，非线性条件下增益无法系统化选择，线性控制器（PID/LQR）"are not able to ensure the robustness of the system" [Roy et al. 2021](https://www.mdpi.com/2227-7080/9/2/37 "A Review on Comparative Remarks, Performance Evaluation and Improvement of Quadrotor Controllers, Technologies, vol. 9, no. 2, 2021")。
- Zhang et al. (2025) 提出的仿真基准框架（基于 RotorPy）在 payload mass ratio 从 0% 增至 200% 的压力测试中，非自适应控制器跟踪性能显著退化，而自适应控制器（INDI-a, xadap）仍保持较高成功率；阵风测试中风速从 0 增至 5 m/s 时所有方法的跟踪误差均随风速增加而增大 [Zhang et al. 2025](https://arxiv.org/html/2510.03471v1 "A Simulation Evaluation Suite for Robust Adaptive Quadcopter Control, arXiv:2510.03471")。

### 可用图片
无本地可用图片。可引用的外部架构图（需核实版权）：
- PX4 多旋翼控制架构图：https://docs.px4.io/main/assets/mc_control_arch.DPb5OeqV.jpg
- ArduPilot 姿态 PID 控制框图：https://ardupilot.org/_images/Copter_CodeOverview_AttitudeControlPID.png

### 仍需补充
- Beard & McLain (2012) 教材中的具体建模公式未能获取全文，写作时可参考其公开课程资料或直接引用章节号。
- 更精确的定量性能退化数据（如"载荷增加 X% 时超调量从 Y% 增至 Z%"），当前最具体的定量证据来自 Zhang et al. (2025) 的仿真框架。
- 电池电压对 PID 性能的定量飞行测试数据（PX4 文档仅定性描述）。
- 需在最终写作中统一 Bouabdallah（Euler 角）与 Mahony（旋转矩阵 R ∈ SO(3)）两种表示方式，建立统一符号表。


## Chapter 2：Classical PID Tuning Methods and Their Applicability to UAVs

### 研究目标
- How do Ziegler–Nichols (step-response and ultimate-gain), Cohen–Coon, relay-feedback (Åström–Hägglund), and manual/iterative tuning work in principle?
- What assumptions do these classical methods make (linearity, SISO, time-invariant plant), and to what extent do those assumptions hold for a multirotor attitude loop?
- What practical results and limitations have been reported when applying these methods to real or simulated quadrotors — in terms of overshoot, settling time, robustness margins, and ease of in-field deployment?
- This chapter serves as the baseline against which all advanced methods in later chapters are benchmarked.

### 关键发现
- Ziegler & Nichols (1942) 提出两种经典调参方法：开环阶跃响应法（从 S 形曲线提取 L、T，PID: Kp=1.2T/L, Ti=2L, Td=0.5L）和闭环极限增益法（Kp=0.6Ku, Ti=0.5Tu, Td=0.125Tu），设计目标为 quarter-amplitude damping。Z-N 方法针对干扰抑制优化，设定值跟踪性能通常较差，且极限增益法存在安全风险 [Ziegler & Nichols 1942](https://skoge.folk.ntnu.no/puublications_others/1942_ziegler-nichols.pdf "Optimum Settings for Automatic Controllers, Trans. ASME, 1942") [Hornsey 2012](https://warwick.ac.uk/fac/cross_fac/iatl/research/reinvention/archive/volume5issue2/hornsey/ "A Review of Relay Auto-tuning Methods, Reinvention, vol. 5, no. 2, 2012")。
- Cohen & Coon (1953) 基于开环阶跃响应提出改进公式，引入 r=td/τ 参数，适用范围比 Z-N 更广（死区时间可达时间常数两倍），但仍基于 FOPTD 模型假设，与 UAV 姿态回路的双积分器动力学严重不匹配 [Cohen & Coon 1953](https://skoge.folk.ntnu.no/puublications_others/1953_Cohen%20and%20Coon%20-%20Theoretical%20Consideration%20of%20Retarded%20Control.pdf "Theoretical Consideration of Retarded Control, Trans. ASME, 1953")。
- Åström & Hägglund (1984) 提出继电器反馈 PID 自整定方法，用继电器在闭环中产生极限环以安全确定 Ku 和 ωu（Ku=4d/(πa)），避免将系统推至不稳定；标准理想继电器估计误差为 5–20%，改进继电器（预加载、饱和型）可进一步降低误差 [Hornsey 2012](https://warwick.ac.uk/fac/cross_fac/iatl/research/reinvention/archive/volume5issue2/hornsey/ "Table 2: identification errors for relay variants")。
- CHR (1952) 区分设定值和扰动响应两类目标，提供 0% 和 20% 超调两套参数表；IMC-PID (Rivera, Morari & Skogestad, 1986) 仅有一个调参参数（闭环时间常数 λ），具有明确频域意义，但需要准确的过程模型 [Rivera et al. 1986](https://skoge.folk.ntnu.no/publications/1986/Rivera86/Rivera86.pdf "Internal Model Control. 4. PID Controller Design, Ind. Eng. Chem., 1986")。
- He & Zhao (2014) 将 Z-N 应用于四旋翼仿真，ZN-PID 仅能将姿态角控制到 0.24 rad（约 13.8°）即失稳，ZN-PD 效果显著优于 ZN-PID 且甚至优于 GA 优化的 PD（后者偏航轴大超调）。论文强调"the larger overshoot is fatal since it often leads to instability" [He & Zhao 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4295143/ "A Simple Attitude Control Based on Ziegler-Nichols Rules, Scientific World Journal, 2014")。
- Canal, Reimbold & de Campos (2020) 指出原始 Z-N 应用于四旋翼 pitch/roll 时"not satisfactory"，提出定制变体 ZNAQ/ZNAQL 实现高达 75% 的性能改善 [Canal et al. 2020](https://www.techscience.com/CMES/v125n1/40211 "Z-N Customization for Quadrotor Attitude Control, CMES, vol. 125, no. 1, 2020")。
- ArduPilot AutoTune 源自继电器反馈方法的变体，采用 ±20° "twitch" 激励，基于角速率超调量迭代调整增益（超调>0.1s 则 P 降 8%，欠调>0.2s 则 P 增 5%），D 和 I 通过经验比例推算。Matt et al. (2025) 评估显示 Level 6 时 GM=15.2 dB, PM=91.0°, DRB=1.71 rad/s [ArduPilot AutoTune 文档](https://ardupilot.org/copter/docs/autotune.html "AutoTune — Copter documentation") [Matt et al. 2025](https://engrxiv.org/preprint/download/4462/7760/6405 "Evaluation of ArduPilot Automatic Tuning Algorithm, engrXiv, 2025")。
- 经典方法与 UAV 的系统性假设不匹配：线性 vs. 非线性、SISO vs. MIMO 耦合、FOPTD vs. 双积分器动力学、时不变 vs. 时变参数、安全开环测试 vs. 飞行中不可执行。搜索未找到 Cohen-Coon 或 CHR 直接应用于 UAV 的文献——FOPTD 假设不匹配程度过大，研究者通常直接跳过这些方法。
- Lopez-Sanchez & Moreno-Valenzuela (2023) 在 Annual Reviews in Control 发表的综述系统回顾了 PID 控制在四旋翼上的应用，覆盖线性、非线性、不连续、分数阶和智能 PID 变体 [Lopez-Sanchez & Moreno-Valenzuela 2023](https://www.sciencedirect.com/science/article/abs/pii/S1367578823000640 "PID Control of Quadrotor UAVs: A Survey, Annual Reviews in Control, vol. 56, 2023")。
- Betaflight 手动调参代表 FPV 社区实践智慧：从低 P 值开始逐步增大至振荡后回退 70%，通过 bank-and-punch 测试检查 I 增益，D 增益需平衡反弹抑制与电机过热风险。典型 5 寸机起始值 Roll: P=46/I=45/D=25，完全不依赖模型但高度依赖飞行员经验 [Betaflight PID Tuning Guide](https://betaflight.com/docs/wiki/guides/current/PID-Tuning-Guide "Betaflight Community Wiki")。
- Hornsey (2012) 在耦合水箱实验中对比：Z-N 规则给出最激进参数（PM 仅 18.4%，超调 11%），Enhanced Åström 双频点法提供最佳时域性能（超调 3.20%，PM=63.8°）[Hornsey 2012](https://warwick.ac.uk/fac/cross_fac/iatl/research/reinvention/archive/volume5issue2/hornsey/ "Table 5: practical comparison results")。

### 可用图片
无本地可用图片。

### 仍需补充
- Z-N 方法应用于真实四旋翼硬件飞行测试的定量数据（当前 He & Zhao 2014 和 Canal et al. 2020 均为仿真结果）。
- ArduPilot Copter AutoTune 的源代码级算法细节（twitch 波形参数、收敛判据），需从 AC_AutoTune 库提取。
- Cohen-Coon/CHR 直接应用于 UAV 的文献（搜索未找到——这本身是重要发现，可在正文中作为批判性论述）。
- Lopez-Sanchez & Moreno-Valenzuela (2023) 综述全文（ScienceDirect 付费墙限制）。


## Chapter 3：Advanced and Adaptive PID Control Strategies for UAVs

### 研究目标
- How does gain scheduling work, and what flight-envelope partitioning strategies have been used for UAVs?
- What are the architectures and convergence properties of self-tuning / model-reference adaptive PID (MRAC-PID) controllers applied to UAV attitude dynamics?
- How do fuzzy-logic-augmented PID (Fuzzy-PID) controllers adjust gains in real time, and what design trade-offs exist in rule-base complexity vs. performance?
- How have neural-network-based PID variants (NN-PID, ANFIS-PID) been applied to UAV control, and what are their training-data and computational requirements?
- What role does fractional-order PID (FOPID / PI^λD^μ) play in UAV attitude control, and what additional tuning degrees of freedom does it introduce?
- How do robust PID formulations (H∞-based PID, μ-synthesis-informed PID) address parametric uncertainty in UAV plants?
- Produce a structured comparison table of these methods along dimensions of complexity, real-time feasibility, robustness, and flight-test maturity.

### 关键发现
- Betaflight TPA（Throttle PID Attenuation）是最广泛部署的增益调度机制，高油门时按比例衰减 P/D 增益（典型设置 tpa_rate=0.6 即满油门衰减 60%），还支持按电池节数自动切换 PID Profile（auto_profile_cell_count），本质是基于油门和电压的离散增益调度 [Betaflight PID Tuning Guide](https://betaflight.com/docs/wiki/guides/current/PID-Tuning-Guide "Betaflight Official — TPA and auto-profile sections")。
- Melo et al. (2022) 设计了模糊增益调度 PID，在 Pixhawk 2.4.8 + ArduPilot 上进行了实际飞行测试：高度超调从常规 PID 的 13% 降至 1%；在临界载荷条件（载荷升至设计载荷 95%）下，模糊调度控制器平均高度误差 0.765 m vs. 无调度的 2.038 m [Melo et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8954855/ "Fuzzy Gain-Scheduling PID for UAV, Sensors, vol. 22, no. 6, 2022")。
- Bakshi & Ramachandran (2018) 提出基于神经网络的间接 MRAC 架构（双隐层 MLP, 44 neurons/layer），参考模型为一阶传递函数 G(s)=0.5/(s+0.5)，在线学习约 10 秒收敛（100Hz），电机质量增加 40% 后仍保持跟踪（仿真验证）[Bakshi & Ramachandran 2018](https://www.intechopen.com/chapters/57843 "Model Reference Adaptive Control of Quadrotor UAVs, IntechOpen, 2018")。
- Wu et al. (2020) 开发了 SO(3) 上的几何 L1 自适应姿态控制器，通过低通滤波器分离快/慢适应动态，具有 Lyapunov 稳定性保证，已在自定义四旋翼平台上完成飞行测试 [Wu et al. 2020](https://hybrid-robotics.berkeley.edu/publications/JDSMC2020_GeometricL1.pdf "Geometric L1 Adaptive Attitude Control, ASME JDSMC, 2020")。
- Eltayeb et al. (2021) 的双环模糊 PID 在仿真中将位置误差降低 87%、姿态误差降低 70%（相对传统 PID）。典型模糊 PID 采用 7×7 规则库（49 条规则）、Mamdani 推理 + 重心解模糊，平衡分辨率与计算复杂度 [Gebeyehu et al. 2025 引用](https://pmc.ncbi.nlm.nih.gov/articles/PMC12396714/ "Hybrid adaptive PID control strategy, PLOS ONE, 2025")。
- Gebeyehu et al. (2025) 提出 NNPID+FPID 混合控制策略：单层前馈 NN（10 hidden neurons）调整 y/ψ 增益，模糊逻辑调整 x/z/ϕ/θ 增益。螺旋轨迹仿真中 roll 轴 MSE：混合 6.87×10⁻⁷ vs. NNPID 4.81×10⁴ vs. FPID 8.96×10⁻⁶；25% 质量增加 + 10% 惯量变化下 x 轴 MSE：混合 2.145 vs. NNPID 4470 vs. FPID 3.128（仿真验证）[Gebeyehu et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12396714/ "PLOS ONE, 2025")。
- Kim & Suh (2024) 提出 I-PID + RBF 神经网络控制器（2-5-1 架构），仿真中 roll 最大误差 0.008 vs. PID 的 0.173（改善 95%），yaw 超调 39% vs. PID 66%，具有完整的 Lyapunov 稳定性证明 [Kim & Suh 2024](https://www.mdpi.com/2504-446X/8/5/179 "Model-Free RBF NN I-PID for Quadrotor, Drones, vol. 8, no. 5, 2024")。
- Ortiz (2018) 在 Raspberry Pi 3 上实现了 ANFIS 四旋翼高度控制器，证明了神经模糊推理在低成本 ARM 嵌入式平台上的实时可行性 [Ortiz 2018](https://www.researchgate.net/publication/323700075_ANFIS_based_quadrotor_drone_altitude_control_implementation_on_Raspberry_Pi_platform "ANFIS on Raspberry Pi, ResearchGate, 2018")。
- FOPID（PI^λD^μ）引入 λ、μ 两个额外参数（共 5 参数），2025 年 Wiley 研究使用 Bonobo 优化对比：roll ITAE 改善 21%（3.62 vs. 4.59），pitch 37%，yaw 74%（0.79 vs. 3.02），高度 45%；调节时间改善 60-75%。但优化计算时间增加约 77%（15,438s vs. 8,712s），且分数阶算子需 Oustaloup 近似（3-5 阶），目前无开源飞控原生支持 [Quadrotor FOPID 2025](https://onlinelibrary.wiley.com/doi/full/10.1155/jom/2065604 "Quadrotor Robust FOPID Based on Bonobo Optimization, J. Optimization and Modeling, 2025")。
- Kumar et al. (2025) 使用 LPV-LFT 框架建模多旋翼非线性并通过 H∞ 综合设计鲁棒控制器（9 状态），在 Dryden 湍流（阵风速 15 m/s）下峰值姿态误差降低一个数量级（PID 峰值误差超 30°），RMSE 改善约 10 倍，闭环 γ₀=0.25（仿真验证）[Kumar et al. 2025](https://arxiv.org/html/2510.00208v1 "Robust Attitude Control with LFT Models and H∞, arXiv, 2025")。
- Lopez-Sanchez & Moreno-Valenzuela (2023) 综述覆盖线性/非线性/不连续/分数阶/智能 PID 变体，指出传统 PID 在风速增加时姿态角误差增加 52% [Lopez-Sanchez & Moreno-Valenzuela 2023](https://www.sciencedirect.com/science/article/abs/pii/S1367578823000640 "PID Control of Quadrotor UAVs: A Survey, Annual Reviews in Control, vol. 56, 2023")。
- 飞行测试验证方法：TPA（百万级飞控部署）、模糊增益调度 PID（Pixhawk 实飞）、ANN-PD（Patel et al. 2019 六旋翼实飞）、L1 自适应（Wu et al. 2020 实飞）。仅仿真验证：FOPID、H∞、混合 NN+Fuzzy PID。计算成本近似排序：PID < TPA < Fuzzy-PID < MRAC-PID < NN-PID < FOPID < H∞ < Hybrid NN+Fuzzy。

### 可用图片
无本地可用图片。

### 仍需补充
- MRAC-PID 的定量性能指标（如 ITAE、ISE、超调百分比对比），当前仅有定性结果。
- Ortiz (2018) 嵌入式 ANFIS 的定量性能数据（延迟、循环速率、跟踪精度）需全文验证。
- 截至 2025 年无飞行测试验证的 FOPID 四旋翼姿态控制实现。
- H∞ 固定结构 PID 综合（hinfstruct 约束为 PID 形式）的 UAV 应用参考缺失。
- 超越 TPA 的增益调度策略（按速度、载荷状态、气动工况划分飞行包线）的多旋翼实例较少。
- Lopez-Sanchez & Moreno-Valenzuela (2023) 52% 误差增加数据来自二手来源，需全文验证。


## Chapter 4：Optimization-Based PID Parameter Tuning — Metaheuristics, Bayesian Methods, and Simulation-in-the-Loop

### 研究目标
- How are PID tuning problems formulated as optimization problems — what objective functions (ISE, ITAE, IAE, multi-objective composites), constraints, and search spaces are commonly used?
- What are the working principles, convergence behaviors, and comparative performance of major metaheuristic algorithms applied to UAV PID tuning: GA, PSO, DE, GWO, and other recent swarm/evolutionary variants?
- How does Bayesian Optimization (GP-based) differ from population-based metaheuristics in sample efficiency, and what are its advantages for expensive SIL/HIL UAV tuning?
- What is the SIL and HIL workflow for iterative PID optimization, and what fidelity requirements does the UAV dynamic model need to satisfy for optimized gains to transfer to real flight?
- How does reinforcement learning (RL) serve as an emerging optimization paradigm for online PID gain adaptation, and what are its current limitations in UAV deployment?

### 关键发现
- UAV PID 优化最常用的六种目标函数为 IAE、ISE、ITAE、ITSE、MSE、IE，约 90% 的工业 PID 控制器采用积分误差类代价函数进行自动调参。单一指标（如 ISE）往往无法覆盖所有性能维度 [Oladimeji et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9120253/ "Metaheuristic algorithms for PID controller parameters tuning: review, Heliyon, vol. 8, no. 5, 2022")。
- Wang et al. (2016) 提出的复合代价函数 J = w₁·ITAE + w₂·Max_Overshoot + w₃·Settling_Time + w₄·‖Gains‖ 是 UAV PID 优化中多准则公式的代表；Immordino et al. (2025) 进一步扩展为包含声学排放和功耗的 8 项复合代价，是目前最全面的单一代价函数 [Wang et al. 2016](http://vigir.missouri.edu/~gdesouza/Research/Conference_CDs/IEEE_SSCI_2016/pdf/SSCI16_paper_384.pdf "Automatic PID Tuning via DE for Quadrotor, IEEE SSCI, 2016") [Immordino et al. 2025](https://arxiv.org/html/2509.17423v1 "Multi-objective Optimization PID for quadrotor, arXiv, 2025")。
- Demir & Demir (2023) 对比 GA/ABC/PSO/FA 用 ITAE 准则调四旋翼 PID：各算法各擅一轴（ABC 最优于高度、FA 于 roll、GA 于 pitch、PSO 于 yaw），无单一算法全面胜出，说明元启发式性能具有问题依赖性 [Demir & Demir 2023](https://hrcak.srce.hr/en/305453 "Comparison of Metaheuristic Optimization Algorithms for Quadrotor PID, Tehnički vjesnik, vol. 30, no. 4, 2023")。
- Immordino et al. (2025) 进行了最全面的三方对比（元启发式 GA/PSO/GWO、贝叶斯优化、深度强化学习 SAC/TD3），6,000 次评估中 GWO 达到最优代价 271.9；有界暖启动条件下 GWO 较 Z-N 基线降低约 23-27%。RL 一次性静态优化模式下未超越 Z-N 基线。单次仿真约 15 秒（125Hz，DJI Matrice 300 模型）[Immordino et al. 2025](https://arxiv.org/html/2509.17423v1 "Tables 4-5, Figures 5-7")。
- Gün (2023) 对比 DE/PSO/GSA/CSS 调四旋翼姿态 PID，DE 优化的增益以更低的总力矩（更高能效）达到目标 [Gün 2023](https://www.sciencedirect.com/science/article/abs/pii/S0957417423010205 "Attitude control via PID based on DE, Expert Systems with Applications, vol. 229, 2023")。
- Khodja et al. (2017) 在 QAV250 + Arduino Due 平台上实验验证 PSO 调参 PID：PSO1（ISE+超调优化）稳态 ISE=0.6842 vs. Z-N 的 1.4437，稳态 pitch 误差均在 ~0.3° 以内，是少数在真实四旋翼上验证元启发式 PID 的研究 [Khodja et al. 2017](https://www.ijsmdo.org/articles/smdo/full_html/2017/01/smdo160015/smdo160015.html "PSO tuning PID for quadrotor, Int. J. SMDO, vol. 8, A8, 2017")。
- Berkenkamp et al. (2016) 提出 SafeOpt——基于高斯过程的安全贝叶斯优化，无需系统模型，仅需初始稳定控制器和性能度量，通过安全约束避免评估不稳定参数，在真实四旋翼上实现了无人干预的快速安全自动调参，是 BO 用于实际 UAV 控制器调参的奠基性工作 [Berkenkamp et al. 2016](https://las.inf.ethz.ch/files/berkenkamp16safe.pdf "Safe Controller Optimization for Quadrotors with GP, IEEE ICRA, 2016")。
- Gu et al. (2025) 提出 HBO-PID（异方差贝叶斯优化），在 PyBullet 仿真中位置误差 0.137 m vs. BO-PID 0.185 m（改善 26%）、标准 PID 0.233 m（41%）；真实四旋翼实验（PX4 + NOKOV 动捕）中均位置误差降低 61.2%、角度误差降低 34.7% [Gu et al. 2025](https://arxiv.org/html/2512.24249v1 "Heteroscedastic BO-Based Dynamic PID Tuning for UAV, arXiv, 2025")。
- Sönmez et al. (2025) 将 DDPG 离线训练的 RL 代理（128×128 神经网络）直接部署在 Pixhawk 2.1 上（无伴随计算机），户外飞行测试中姿态 RMSE 从 33.93×10⁻² 降至 22.55×10⁻²（改善 33%），位置误差改善 37%，是首次在嵌入式飞控硬件上直接部署 RL 调参 PID 的验证 [Sönmez et al. 2025](https://www.mdpi.com/2504-446X/9/8/581 "RL-Based PD Controller Gains Prediction for Quadrotor, Drones, vol. 9, no. 8, 2025")。
- RL 一次性静态优化（SAC/TD3 作为单步 MDP 提出完整 15 参数 PID 向量）在三种测试配置中均未超越 Z-N 基线，说明 RL 更适合多步状态依赖的自适应增益调度而非离线参数选择 [Immordino et al. 2025](https://arxiv.org/html/2509.17423v1 "Section 3.2")。
- SIL 工作流关键发现：Wang et al. (2016) 的两阶段方法（先内环姿态 PD → 再外环位置 PID）降低了各子问题维度；Sönmez et al. (2025) 发现仿真模型中包含 PWM 信号量化（UINT16 转换）是 sim-to-real 迁移成功的关键因素。
- Immordino et al. (2025) 开源 Python 框架支持模块化替换空气动力学/声学/控制器/优化算法模块；MathWorks 提供 PID Autotuning for UAV Quadcopter 示例 [MathWorks](https://www.mathworks.com/help/slcontrol/ug/pid-controller-tuning-for-a-uav-quadcopter.html "PID Autotuning for UAV Quadcopter — MATLAB")。
- 综合评估：PSO 使用最广泛（收敛速度与解质量平衡好）；GWO 在多目标综合对比中表现最优但问题依赖；BO 样本效率最高但单次迭代成本高（>34s vs. ~17s）；RL 在在线自适应场景有潜力但静态优化中表现不佳。文献综述涵盖 73 种以上元启发式算法。

### 可用图片
无本地可用图片。

### 仍需补充
- Demir & Demir (2023) 各轴各算法的具体 ITAE 数值表（全文 PDF 未获取）。
- 目前无类似 CEC 测试函数的标准化 UAV PID 优化基准套件，这是文献的真实空白。
- NSGA-II 等多目标进化算法对 UAV PID 的 Pareto 前沿分析文献不足。
- HIL 优化闭环（优化器对接真实自驾仪硬件）的详细案例较少，大多数来源要么纯 SIL 要么直接真机优化（Berkenkamp）。


## Chapter 5：Practical Implementation in Open-Source Flight Stacks — AutoTune, Deployment, and Validation

### 研究目标
- How does ArduPilot's AutoTune algorithm work internally — what excitation signals does it inject, how does it identify system dynamics, and how does it set/back off PID gains for stability margins?
- How does PX4's auto-tuning module differ in approach and user workflow?
- What is Betaflight's tuning philosophy (RPM filtering, feed-forward, slider-based tuning), and why does it diverge from ArduPilot/PX4?
- What are practical considerations for in-field PID tuning: safety constraints, sensor noise/filtering (notch filters, D-term low-pass), actuator saturation/anti-windup, computational budget on embedded MCUs, and regulatory/airworthiness implications?
- What HIL and SIL validation pipelines exist, and what best practices have emerged for verifying tuned PID gains before flight?

### 关键发现
- ArduPilot AutoTune（Leonard Hall 设计）通过注入约 ±20° "twitch" 角脉冲测量瞬态响应（超调、反弹、稳定），调参顺序为 RATE_D_UP → RATE_D_DOWN → RATE_P_UP → ANGLE_P_DOWN → ANGLE_P_UP → TUNE_COMPLETE，每步需 4 次连续成功 twitch 方可推进。AUTOTUNE_AGGR（0.05-0.10，默认 0.1）控制超调/反弹检测阈值，gain_backoff 提供额外稳定裕度。Rate I = Rate P（roll/pitch），I = 0.1×P（yaw）[ArduPilot AutoTune 文档](https://ardupilot.org/copter/docs/autotune.html "Official ArduPilot Copter AutoTune") [AC_AutoTune_Multi.h 源码](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AC_AutoTune/AC_AutoTune_Multi.h "ArduPilot AutoTune source")。
- ArduPilot AutoTune 已知限制：强风降低 twitch 分析可靠性、高陀螺噪声/振动混淆算法、ESC 非线性（MOT_THST_EXPO 不当）产生误导、柔性机架引入未建模动态、可能不总是收敛 [ArduPilot AutoTune 文档](https://ardupilot.org/copter/docs/autotune.html "Limitations section")。
- ArduPilot Methodic Configurator（IAV GmbH）提供 53 步系统化调参工作流：初始参数设置 → 陷波滤波器标定（Filter Review Tool）→ QuikTune（基于外部风扰的 Lua 脚本替代方案）→ 逐轴 AutoTune → 系统辨识飞行（chirp 信号）→ 解析 PID 优化，代表当前产品级 ArduPilot 调参最佳实践 [Methodic Configurator](https://ardupilot.github.io/MethodicConfigurator/TUNING_GUIDE_ArduCopter.html "IAV GmbH systematic ArduCopter tuning guide")。
- PX4 自整定模块（mc_autotune_attitude_control）采用基于模型的系统辨识方法：施加小扰动 → 辨识每轴 2 极点 2 零点线性 SISO 模型 → 计算 PID 增益，全程约 40 秒（19-68 秒范围），假设轴间无耦合。MC_AT_APPLY=2 支持空中即时应用并自动回退（4 秒稳定性监测）[PX4 Auto-Tuning 文档](https://docs.px4.io/main/en/config/autotune_mc "PX4 official MC auto-tuning") [Auterion 文档](https://docs.auterion.com/hardware-integration/additional-resources/controllers-auto-tuning "Auterion PX4 auto-tuning details")。
- PX4 vs. ArduPilot 自整定对比：PX4 为参数化系统辨识（基于模型），ArduPilot 为迭代 twitch 测试（基于实验，类继电器反馈）；PX4 约 40 秒完成 vs. ArduPilot 数分钟；PX4 单一辨识模型同时调速率和姿态控制器，ArduPilot 分阶段顺序调 D/P/Angle P。
- Betaflight 4.3 引入滑块式 PID 调参系统（PI gain、D gain、FeedForward 及专家模式滑块），可通过 OSD 或 Lua 脚本在飞行现场快速迭代，面向 FPV 竞速/自由飞需求 [Betaflight 4.3 Tuning Notes](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes "slider system, presets, tuning methods")。
- Betaflight RPM 滤波使用双向 DShot ESC 遥测获取实时逐电机 RPM，在旋转频率及谐波处放置陷波滤波器；RPM 交叉衰落（crossfading）在低 RPM（低于 rpm_filter_min_hz，默认 80 Hz）时平滑禁用滤波器以消除低油门滤波引入的延迟。多动态陷波使用 SDFT 算法同时跟踪多达 5 个独立噪声峰 [Betaflight 4.3 Tuning Notes](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes "RPM crossfading and SDFT multi-dynamic notch")。
- Betaflight FeedForward 2.0 与设定值导数成比例（比 P 项更快），ff_boost 正比于摇杆加速度（二阶导数），ff_max_rate_limit 在接近最大速率时预测性衰减 FF 以防超调。D_min/D_Max 实现 D 项增益调度：平滑飞行时取低值减少噪声/电机发热，快速机动时升至 D_Max 增强阻尼 [Betaflight FF 2.0](https://betaflight.com/docs/wiki/guides/current/Feed-Forward-2-0 "Feed Forward 2.0 guide")。
- Betaflight 与 ArduPilot/PX4 架构差异根源于任务特性：FPV 需要亚毫秒延迟（PID 循环 4-8 kHz vs. ArduPilot 400 Hz）、DShot 数字 ESC 协议、以及最小相位滞后的滤波设计。
- 陀螺仪滤波链对比：ArduPilot 支持动态谐波陷波（5 种跟踪方式含逐电机 ESC 遥测和 FFT），PX4 有 2 个静态陷波 + 动态陷波 + 完整 IMU 管线（标定→偏差→陷波→低通→导数→D项低通），Betaflight 用 RPM 陷波 + SDFT + PT2/PT3 低通（移除了双二次低通以避免过冲/共振）。PX4 30Hz 陀螺低通引入约 8ms 延迟，120Hz 约 1.9ms [PX4 Filter Tuning](https://docs.px4.io/main/en/config_mc/filter_tuning "MC Filter Tuning & Control Latency") [ArduPilot Notch Filter](https://ardupilot.org/copter/docs/common-imu-notch-filtering.html "Dynamic Harmonic Notch Filters")。
- PX4 速率控制器积分项使用抗复位饱和（ARW）钳位法，推力饱和遵循优先级：垂直推力 → MPC_THR_MAX 饱和 → 水平推力按剩余容量饱和。ArduPilot 外环使用 "square root controller" 进行非线性角度-速率映射，AP_Motors "stability patch" 在输出超限时优先保障姿态控制 [PX4 Controller Diagrams](https://docs.px4.io/main/en/flight_stack/controller_diagrams "ARW and saturation") [ArduPilot Attitude Control](https://ardupilot.org/dev/docs/apmcopter-programming-attitude-control-2.html "P→PID cascade and AP_Motors mixing")。
- MCU 算力约束：STM32F411 仅限 4k PID + DShot300，F405 开启 RPM 滤波时也限 4k，F7/H7 可运行 8k PID；PX4 推荐 4kHz+ 仅限 H7；CPU 使用超 75% 有任务饥饿风险；ArduPilot F4 不建议每 IMU 开陷波或跑 FFT [Betaflight 4.3 Tuning Notes](https://betaflight.com/docs/wiki/tuning/4-3-Tuning-Notes "Processor requirements") [PX4 Filter Tuning](https://docs.px4.io/main/en/config_mc/filter_tuning "Latency constraints")。
- ArduPilot SITL 支持多种外部仿真器（Gazebo、RealFlight、AirSim、MATLAB/Simulink 等）；PX4 HITL 在真实飞控硬件上运行固件但用模拟传感器数据替代真实数据。Methodic Configurator 的系统辨识工作流提供结构化 SIL 验证：chirp 激励 → 传递函数提取 → 多目标优化/闭环预测 → 验证飞行 + PID Review Tool 频域分析 [ArduPilot SITL](https://ardupilot.org/dev/docs/simulation-2.html "ArduPilot simulation overview") [PX4 HITL](https://docs.px4.io/main/en/simulation/hitl "PX4 HITL documentation")。
- 实际部署要点：MOT_THST_EXPO 推力线性化错误（过高→低油门不稳，过低→高油门不稳）会阻止 AutoTune 收敛；电池电压 PID 缩放补偿飞行中电压下降；RATE.*out 超过 0.15 表示默认 PID 与飞行器特性不匹配，需先降低增益 50%+ [ArduPilot AutoTune 文档](https://ardupilot.org/copter/docs/autotune.html "MOT_THST_EXPO and voltage scaling") [Methodic Configurator](https://ardupilot.github.io/MethodicConfigurator/TUNING_GUIDE_ArduCopter.html "Motor output oscillation diagnostics")。

### 可用图片
无本地可用图片。

### 仍需补充
- PX4 自整定器的系统辨识算法实现细节（在线最小二乘？频率响应拟合？）——官方文档描述模型结构但未说明估计方法。
- ArduPilot AC_PID 库的积分器限幅/钳位代码实现细节。
- AutoTune vs. 手动调参 vs. 优化调参的定量对比飞行测试数据（响应时间、调节时间、增益裕度）。
- Betaflight Blackbox 日志分析工作流和调参调试模式的详细说明。
- 自动调参 PID 增益在商业 UAV 运营中的适航/法规影响（FAA Part 107、EASA 要求）。


## Chapter 6：Comparative Synthesis and Future Directions

### 研究目标
- How do the surveyed methods compare across a standardized set of evaluation criteria — tracking accuracy, disturbance rejection, robustness to parameter variation, computational cost, ease of deployment, and flight-test maturity?
- What is the current consensus on which method families are best suited for which UAV mission profiles (precision agriculture payload changes vs. FPV racing agility vs. long-endurance inspection)?
- What are the most promising open research directions — integration of learning-based methods into certified flight stacks, transfer learning across UAV platforms, real-time adaptive methods with formal stability guarantees, and convergence of MPC with PID architectures?
- What standardized benchmarking frameworks or community challenges could accelerate progress in this field?

### 关键发现
- Rinaldi et al. (2023) 在同一非线性四旋翼模型上定量对比 PID/LQR/FL/SMC/MPC：跟踪精度排序 SMC (L₂x=0.36) > LQR (0.41) > FL (0.64) ≈ MPC (0.65) > PID (1.40)；控制代价排序 PID (L₂u=1.60) < MPC (3.70) < SMC (4.35) < LQR (4.53) < FL (5.60)。PID 跟踪精度最差但控制代价最低（能效最高）[Rinaldi et al. 2023](https://www.mdpi.com/2076-3417/13/6/3464 "A Comparative Study for Control of Quadrotor UAVs, Applied Sciences, vol. 13, no. 6, 2023")。
- Lopez-Sanchez & Moreno-Valenzuela (2023) 在 Annual Reviews in Control（270 篇引用）系统覆盖线性/非线性/不连续/分数阶/智能 PID 变体，是 PID 族方法最权威的分类框架 [Lopez-Sanchez & Moreno-Valenzuela 2023](https://www.sciencedirect.com/science/article/abs/pii/S1367578823000640 "PID Control of Quadrotor UAVs: A Survey, Annual Reviews in Control, vol. 56, 2023")。
- Khalid et al. (2023) 在 ACM Computing Surveys 中按类型（经典线性、非线性基于模型、智能/学习、混合）分类四旋翼控制方案，发现 BP 神经网络性能优于传统 PID 但 PID 因简单性仍主导实际部署 [Khalid et al. 2023](https://dl.acm.org/doi/full/10.1145/3617652 "Control Schemes for Quadrotor UAV: Taxonomy and Survey, ACM Computing Surveys, vol. 56, no. 5, 2023")。
- Zhou et al. (2026) 提出 MPC-PID 混合架构：上层 MPC + H∞ 鲁棒优化生成参考控制、下层 Transformer 注意力网络在线调 PID 增益 + 滑模扰动观测器前馈补偿。AirSim 仿真中路径跟踪 RMSE 从 5.87 m 降至 3.92 m（改善 33%），调节时间改善 21.6%，扰动抑制比 0.92（改善 17.3%），展示了"预测-学习-补偿"闭环的 MPC+PID 融合趋势 [Zhou et al. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC12820076/ "Robust MPC-PID hybrid control for UAV, Scientific Reports, vol. 16, 2585, 2026")。
- Molchanov et al. (2019) 通过域随机化 RL 训练低层鲁棒控制策略并成功迁移到多个不同物理四旋翼，无需 PD 骨架控制器，展示了 sim-to-multi-real 迁移消除逐平台 PID 调参的可能性 [Molchanov et al. 2019](https://ieeexplore.ieee.org/document/8967695/ "Sim-to-(Multi)-Real Transfer of Low-Level Control Policies, IEEE/RSJ IROS, 2019")。
- Gu, Primatesta & Rizzo (2024) 提出物理信息神经网络（PINN）用于四旋翼动力学建模，将动量守恒定律嵌入为学习偏置，相比纯数据驱动 ANN 获得更好精度和物理一致性，为具有性能保证的学习控制模型提供基础 [Gu et al. 2024](https://www.sciencedirect.com/science/article/pii/S0921889023002087 "PINN for Quadrotor Modeling, Robotics and Autonomous Systems, vol. 171, 2024")。
- Wu et al. (2025) 的 L₁Quad（IEEE TCST）提供可计算的一致/最终一致界，保证四旋翼沿期望轨迹的"安全管"，通过低通滤波器解耦鲁棒性与自适应速度，在 Pixhawk + PX4 上完成敏捷飞行实验——自适应控制器获得形式化稳定性保证的关键进展，对适航认证具有潜在价值 [Wu et al. 2025](https://arxiv.org/abs/2302.07208 "L1Quad: L1 Adaptive Augmentation with Performance Guarantees, IEEE TCST, vol. 33, no. 2, 2025")。
- 标准化基准平台：AdaptiveQuadBench (2025, 基于 RotorPy) 提供模块化控制库 + 可配置扰动模型 + 自动化压力测试 + 标准化指标，解决"碎片化评估阻碍系统性比较"的问题 [Zhang et al. 2025](https://arxiv.org/html/2510.03471v1 "AdaptiveQuadBench, arXiv:2510.03471, 2025")；safe-control-gym (Yuan et al. 2022) 扩展 OpenAI Gym 提供约束规格和可重复扰动注入 [Yuan et al. 2022](https://arxiv.org/abs/2109.06325 "safe-control-gym, IEEE RA-L, 2022")；RotorPy 提供含空气动力学的开源多旋翼仿真 [RotorPy](https://github.com/spencerfolk/rotorpy "RotorPy, arXiv:2306.04485, 2023")。
- Pyrgies (2020) 探索基于认知架构（SOAR）的自适应学习 UAV 代理的 DO-178C 认证路径，通过使学习过程确定化和可审计来桥接 DO-178C 要求与神经网络随机性之间的矛盾。L₁ 自适应控制（Lyapunov 分析 + 可计算性能界）是认证-自适应桥梁的潜在中间方案 [Pyrgies 2020](https://www.researchgate.net/publication/346042754_Towards_DO-178C_certification_of_adaptive_learning_UAV_agents "ACM/IEEE ICSE-NIER, 2020")。
- 任务匹配综合：FPV 竞速 → Betaflight 手动/滑块 PID + TPA + D_min/D_Max + RPM 滤波（极端延迟需求排除自适应方法）；精准农业/变载荷 → 增益调度 PID、模糊 PID、MRAC-PID（Melo et al. 实飞验证超调 13%→1%）；长航时巡检 → 标准 PID（控制代价最低 L₂u=1.60）+ 电压补偿 + TPA；快递配送 → MPC-PID 混合 + SafeOpt/HBO + L₁ 自适应（安全约束+载荷变化+认证需求）；通用自主 → ArduPilot/PX4 AutoTune + 离线优化（GWO/BO）+ 系统辨识工作流。
- 商业/工业现状：固定增益 PID + 自动调参（ArduPilot AutoTune、PX4 autotuner）仍是主流，Methodic Configurator（IAV GmbH 53 步工作流含 SysID + 解析优化）代表产品级调参最高水平。NN-PID、Fuzzy-PID、FOPID、RL-PID 几乎全部停留在仿真阶段，无开源飞控原生支持；唯一例外为 Sönmez et al. (2025) 在 Pixhawk 上部署预训练 DDPG。商业平台（DJI、Skydio）控制算法不公开。

### 可用图片
无本地可用图片。

### 仍需补充
- 尚无单一研究在同一物理四旋翼上对比经典 PID、Fuzzy-PID、NN-PID、FOPID、PSO-PID 和 RL-PID，统一比较表需跨研究综合并标注非同一测试条件的局限。
- DJI、Skydio 等商业制造商的控制算法内部细节不公开，关于商业采用先进 PID 方法的论断仍为推测性。
- DO-178C 认证路径参考（Pyrgies 2020 仅为 4 页 workshop 短文），需要更成熟的适航认证与自适应控制交叉研究。
- 目前无类似 ImageNet/CARLA 的广泛认可的 UAV PID/姿态控制基准竞赛，AlphaPilot 等竞赛聚焦全栈自主而非控制算法对比。
- PID 调参知识（最优增益调度表、学习的增益自适应策略）跨不同多旋翼平台迁移学习的已发表工作有限。


# Section 2：给 Write 阶段的执行建议

## 术语一致性
- 在 Chapter 1 统一定义所有 PID 增益符号并全文复用：**Kp**, **Ki**, **Kd**（正体、非斜体、下标形式）。涉及具体回路层级时使用上标或前缀，如 Kp^rate, Kp^angle。
- 统一使用 "cascaded PID"（不用 "cascade PID" 或 "nested PID"）。
- 标准化使用 "multirotor UAV" 作为主要载体描述；仅在特指四旋翼构型时使用 "quadrotor"。正文中避免使用 "quad" 或 "drone" 等非正式用语。
- 开源飞控栈统一写法：ArduPilot、PX4、Betaflight（注意大小写）。
- 分数阶 PID 统一采用 PI^λD^μ 记法，首次出现时定义 λ、μ。

## 统一符号表
- Chapters 1–4 均涉及 PID 增益符号与闭环传递函数表达。在 Chapter 1 放置统一符号表，定义：被控对象传递函数 G(s)、控制器传递函数 C(s)、误差信号 e(t)、参考信号 r(t)、干扰信号 d(t)、各 PID 增益。
- 优化章节（Chapter 4）统一使用 J 表示代价函数，下标区分具体准则（J_ISE, J_ITAE, J_IAE）。
- 元启发式算法统一使用 N_pop（种群规模）、T_max（迭代/代数上限）、f(·)（适应度函数）。

## 跨章节一致性
- Chapter 2 建立基线性能指标；Chapters 3–4 应明确引用并对比这些基线，使用相同的度量定义。
- Chapter 3 的自适应/先进方法比较表应与 Chapter 6 的综合比较表使用相同列标题，确保读者可追溯。
- Chapter 5 应交叉引用 Chapters 2–4 中的特定算法概念（如 relay feedback → ArduPilot AutoTune 的渊源）。
- 避免跨章节重复相同背景材料；使用前向/后向引用。

## 篇幅平衡
- Chapter 1（基础）：中等深度，简洁 — 约占总篇幅 12–15%
- Chapter 2（经典方法）：中等深度，侧重 UAV 适用性 — 约占 12–15%
- Chapter 3（先进/自适应方法）：高深度，方法论核心 — 约占 22–25%
- Chapter 4（优化调参）：高深度，另一方法论核心 — 约占 20–22%
- Chapter 5（实践与开源）：中高深度，实操价值 — 约占 15–18%
- Chapter 6（综合与展望）：中等深度，比较表为核心 — 约占 8–10%

## 范围边界
- 报告聚焦 PID 族控制器（含 PID 增强和 PID 混合方法）。纯非 PID 控制器（独立 MPC、滑模控制、反步法、H∞ 状态反馈）仅作背景提及，不深入综述。
- 姿态控制（内环）为主要范围。位置/轨迹控制（外环）仅在影响姿态环 PID 设计时讨论。
- 以旋翼 UAV（多旋翼）为主要平台。固定翼和 VTOL 过渡飞行控制仅简要提及。
- 优先覆盖有仿真或飞行测试验证的方法；纯理论提案引用但不详述。

## 时间口径
- 用户未指定时间范围。以当前日期（2026-04-03）为锚点，研究区间覆盖过去 12 个月至未来 6 个月（即 2025 年 4 月 — 2026 年 10 月），经典方法的历史文献不受此限制。
