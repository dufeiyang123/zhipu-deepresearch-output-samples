# Section 1：章节研究计划

## Chapter 1：Introduction — 3D Grain Reconstruction and Phenotypic Analysis Through the Lens of Modern Control Theory

### 研究目标
- Survey the state of the art in 3D crop grain reconstruction, high-throughput phenotyping, and the emerging application of systems-and-control theory to sensing and reconstruction pipelines.
- Motivate why treating a multi-sensor, multi-stage phenotyping workflow as a dynamic system opens access to a mature control-theoretic toolkit.
- Identify the literature gap: most existing work treats the pipeline as feed-forward; very few formalize it as a closed-loop system.
- Provide a scope and contribution statement for the report.

### 关键发现

**A. 3D Imaging Modalities for Grain-Scale Phenotyping**

1. Structured-light scanning is the most cost-effective high-precision modality for grain-level 3D phenotyping. Qin et al. (2022) used a structured-light scanner (Reeyee Pro, single-sided accuracy 0.05 mm) coupled with a 6-DOF robot arm to scan 2,200 cereal grains (rice, wheat, corn), achieving measurement errors of 2.07% (length), 0.97% (width), and 1.13% (thickness), with average throughput of **9.6 s per grain**. Surface area and volume errors against a standard sphere were 2.83% and 1.75%, respectively. [Qin et al. 2022](https://www.nature.com/articles/s41598-022-07221-4 "Scientific Reports, Cereal grain 3D point cloud analysis via structured light imaging")

2. Huang et al. (2022) extracted 32 phenotypic traits (16 basic + 16 derived) from wheat grains via structured-light scanning, including ventral sulcus depth/area/perimeter. MAPE for wheat length, width, thickness, and ventral sulcus depth was 1.83%, 1.86%, 2.19%, and 4.81%, respectively. Throughput was **12 s per grain** (~4,000 grains/8-hr day). System cost ~$20,000, approximately one-tenth of a μCT system. [Huang et al. 2022](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full "Frontiers in Plant Science, 3D wheat grain and ventral sulcus traits via structured light")

3. X-ray micro-CT achieves higher spatial resolution for grain internal structure. Zhou et al. (2024) reconstructed wheat grain internal morphology (endosperm ~80%, pericarp ~12%, embryo ~2%, scutellum ~2%, pores ~4% of total volume) at **25.23 μm per pixel** spatial resolution, but throughput was ~24 s per grain. [Zhou et al. 2024](https://ifst.onlinelibrary.wiley.com/doi/10.1111/ijfs.17500 "Int J Food Sci Technol, 3D reconstruction of wheat grains by X-ray μCT")

4. X-ray microscopy (XRM) achieves **1.86 μm pixel pitch** (Zeiss Xradia 520 Versa XRM) for seed cellular analysis, enabling individual cell segmentation. However, throughput is severely limited: 5 seeds required **10 hours** per batch. [Griffiths et al. 2025](https://www.nature.com/articles/s41598-025-88482-7 "Scientific Reports, Evaluation of 3D seed structure using X-ray microscopy")

5. Deep-learning-based 3D reconstruction from 3 images (instead of 36 for volume carving) reduces imaging time by **10×** while maintaining relative volume error of ~2.36% and per-point mean L1 error of ~40 μm. Inference time 49 ms per seed on NVIDIA A100. [Cherepashkin et al. 2023](https://openaccess.thecvf.com/content/ICCV2023W/CVPPA/papers/Cherepashkin_Deep_Learning_Based_3d_Reconstruction_for_Phenotyping_of_Wheat_Seeds_ICCVW_2023_paper.pdf "ICCV 2023 Workshop, Deep learning based 3D reconstruction for wheat seed phenotyping")

**B. Phenotypic Traits Extracted at Grain Level**

6. Qin et al. (2022) defined 25 grain phenotypic traits (11 basic + 14 derived). With XGBoost, filled/unfilled grain classification reached 90.184% accuracy; indica/japonica classification reached 99.950% via SVM. Thickness was the dominant trait for filled/unfilled classification (weight 0.34). [Qin et al. 2022](https://www.nature.com/articles/s41598-022-07221-4 "Scientific Reports, 25 phenotypic traits from 3D point cloud")

7. Roundness and sphericity are key 3D shape descriptors. Grain weight prediction using 32 traits achieved R² = 0.83 (gradient boosting, MAPE 3.37%, RMSE 2.45 mg). [Huang et al. 2022](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full "Frontiers in Plant Science, 32 wheat grain phenotypic traits")

**C. Pipeline Architecture**

8. The canonical phenotyping pipeline: acquisition → preprocessing → segmentation → 3D reconstruction → trait extraction → statistical analysis/ML classification, is independently documented in Qin et al. (2022), Huang et al. (2022), and generalized in the comprehensive review by Pieters et al. (2023). [Pieters et al. 2023](https://link.springer.com/article/10.1186/s13007-023-01031-z "Plant Methods, How to make sense of 3D representations for plant phenotyping")

9. The most-cited crop phenomics survey by Yang et al. (2020, Molecular Plant 13:187–214) covers high-throughput phenotyping platforms and imaging modalities but does not discuss any control-theoretic or feedback-loop perspective. [Yang et al. 2020](https://www.sciencedirect.com/science/article/pii/S1674205220300083 "Molecular Plant, Crop phenomics review")

**D. Control Theory Gap Analysis**

10. In SLAM, EKF was the dominant approach from 1986 through the mid-2000s, treating robot pose + landmarks as joint state vector with Kalman prediction-correction. Multi-sensor fusion of LiDAR + camera + IMU for 3D reconstruction is well established. [Xu et al. 2022](https://www.mdpi.com/2072-4292/14/23/6033 "Remote Sensing, SLAM Overview")

11. Kalman filters applied to dynamic MRI: Feng et al. (2013) treated each MR image frame as a state estimated from sequential k-space measurements (identity state transition + 1D Fourier observation model), achieving 50 ms per-frame reconstruction — a directly transferable template for sequential 3D reconstruction. [Feng et al. 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536913/ "Magnetic Resonance in Medicine, Kalman filter for dynamic cardiac MRI")

12. Next-Best-View (NBV) planning formulates viewpoint selection as optimization to maximize information gain, paralleling MPC. However, **no existing NBV work in plant phenotyping has been formulated in explicit state-space or control-theoretic terms**. [Attention-driven NBV](https://www.sciencedirect.com/science/article/pii/S1537511024001740 "Biosystems Engineering, Attention-driven NBV planning")

13. **Critical gap: no published work formalizes a grain phenotyping pipeline as a closed-loop control system.** All grain 3D reconstruction papers treat the pipeline as a feed-forward sequence with no feedback from trait-extraction uncertainty to acquisition parameters, no state-space formulation of the evolving 3D estimate, and no observability/controllability analysis.

**E. Adjacent-Domain Analogues**

14. MSCKF (Multi-State Constraint Kalman Filter) by Mourikis and Roumeliotis (2007) achieves real-time visual-inertial estimation with linear complexity growth. EKF-based LiDAR+camera+IMU fusion deployed on UAVs for 6-DOF pose estimation. [Xu et al. 2022](https://www.mdpi.com/2072-4292/14/23/6033 "Remote Sensing, SLAM Overview — VI-SLAM section")

15. The Kalman filter model in dynamic MRI (Feng et al. 2013) provides a directly transferable template: diagonal Q from training data distinguishes dynamic vs. static regions, allocating measurement information adaptively — an exact analogue to allocating more views to morphologically complex grains. [Feng et al. 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536913/ "Magnetic Resonance in Medicine, Kalman filter for dynamic cardiac MRI")

16. The Pieters et al. (2023) 3D plant phenotyping review contains **no mention of control theory, Kalman filtering, state-space modeling, observability, or feedback-loop design**, confirming the gap even in the most comprehensive phenotyping processing reviews. [Pieters et al. 2023](https://link.springer.com/article/10.1186/s13007-023-01031-z "Plant Methods, How to make sense of 3D representations for plant phenotyping")

**F. Quantitative Benchmarks**

17. Cross-modality comparison (2022–2025): Structured light: accuracy 0.05 mm, throughput ~10–12 s/grain, cost ~$20k. μCT: resolution 25 μm/pixel, throughput ~24 s/grain, cost ~$200k. XRM: 1.86 μm pitch, throughput ~7200 s/grain, cost >$500k. Deep-learning 3-view: L1 error ~40 μm, volume error ~2.36%, throughput ~2 s + 49 ms inference. Sources: [Qin 2022](https://www.nature.com/articles/s41598-022-07221-4 "structured light"), [Huang 2022](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840908/full "structured light vs CT"), [Griffiths 2025](https://www.nature.com/articles/s41598-025-88482-7 "XRM"), [Cherepashkin 2023](https://openaccess.thecvf.com/content/ICCV2023W/CVPPA/papers/Cherepashkin_Deep_Learning_Based_3d_Reconstruction_for_Phenotyping_of_Wheat_Seeds_ICCVW_2023_paper.pdf "deep learning 3D")

### 可用图片
无（文献综述型章节，无本地数据图片。撰写时建议制作：传统开环表型流程 vs. 控制论闭环流程对比框图）

### 仍需补充
- Multiscale grain crop phenotyping review (2025, Computers and Electronics in Agriculture) 因访问限制未能获取全文，可能提供多尺度3D表型技术的额外背景。
- 未找到在农业传感器规划中明确应用状态空间建模、可观性 Gramian 分析或 LQG/MPC 的论文；可进一步检索 IEEE Trans. Automation Science and Engineering 或 Journal of Field Robotics。
- 未找到 photogrammetry/SfM 专门用于单粒级（非整株）3D 重建的独立基准数据。
- 椭圆傅里叶描述子 (EFD) 在 3D 谷物形状分析中的应用在 2020–2026 窗口期内未找到专门论文（EFD 多用于 2D 轮廓，如 SmartGrain）。
- 估计/重建场景下的 Lyapunov 稳定性分析：SLAM 文献提及 EKF-SLAM 收敛分析，但未找到针对 3D 形状重建估计器的正式 Lyapunov 稳定性证明。

---

## Chapter 2：State-Space Modeling of the Grain 3D Reconstruction Pipeline

### 研究目标
- Formulate the grain imaging and 3D reconstruction process as a discrete-time state-space system.
- Define state representations (voxel grid, TSDF, superellipsoid, spherical harmonics) and analyze dimensionality trade-offs.
- Derive state transition and observation models with process and measurement noise.
- Perform observability and controllability analysis (Gramian rank conditions, minimum number of views).
- Discuss linearization strategies for high-dimensional implicit surfaces.

### 关键发现

**A. State Representations**

1. TSDF as state vector: Curless & Levoy (1996) introduced volumetric integration using cumulative weighted signed distance. Each voxel stores D(x) and W(x); the update rule D_new = [W_old·D_old + w_i·d_i]/(W_old + w_i) is directly a state-transition equation x[k+1] = f(x[k], u[k]). For 256³ grid, state dimension ≈ 16.7M scalars. The isosurface (zero-crossing) is optimal in the least-squares sense. [Curless & Levoy 1996](https://graphics.stanford.edu/papers/volrange/paper_2_levels/paper.html "SIGGRAPH 1996, A Volumetric Method for Building Complex Models from Range Images")

2. KinectFusion demonstrated real-time TSDF fusion at 30 Hz with a four-stage closed loop: surface measurement → sensor pose estimation (ICP) → TSDF integration → surface prediction (raycasting). This architecture is structurally analogous to a Kalman prediction-correction cycle; the key difference is that KinectFusion does not propagate an explicit error covariance. [Newcombe et al. 2011](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ismar2011.pdf "ISMAR 2011, KinectFusion")

3. Superellipsoid parametric model: 11 parameters (3 semi-axes a₁,a₂,a₃; 2 shape exponents ε₁,ε₂; 3 position; 3 orientation). An extreme dimensionality reduction vs. TSDF, covering shapes from cuboids to ellipsoids to octahedra. Recovery via least-squares minimization of inside-outside function. [Solina & Bajcsy 1990](https://dl.acm.org/doi/abs/10.1109/34.44401 "IEEE TPAMI 12(2), Recovery of Parametric Models from Range Images")

4. Spherical harmonic (SH) shape descriptors: tunable resolution via maximum degree ℓ_max. State dimension = (ℓ_max+1)² coefficients. Cherepashkin et al. (2023) used ℓ=20 (441 coefficients) for wheat seeds, achieving L1 error ~40 μm. [Kazhdan et al. 2003](https://gfx.cs.princeton.edu/pubs/Kazhdan_2003_RIS/index.php "Eurographics SGP 2003, Rotation Invariant SH Shape Descriptors"); [Cherepashkin et al. 2023](https://openaccess.thecvf.com/content/ICCV2023W/CVPPA/papers/Cherepashkin_Deep_Learning_Based_3d_Reconstruction_for_Phenotyping_of_Wheat_Seeds_ICCVW_2023_paper.pdf "ICCV 2023W, SH for wheat seeds")

5. SH applied specifically to agricultural grain shapes: González-Montellano et al. (2017) demonstrated SH for bean, chickpea, and maize, capturing convexities, concavities, and tip cap features. Confirms viability of SH coefficients as state vector for grain reconstruction. [González-Montellano et al. 2017](https://www.sciencedirect.com/science/article/abs/pii/S016816991630730X "Computers and Electronics in Agriculture, SH for agricultural grain shapes")

**B. State-Update Equations**

6. TSDF fusion update is formally linear in the state (weighted average): D_{k+1} = α_k·D_k + (1−α_k)·d_k where α_k = W_k/(W_k + w_k). Weight w_k encodes directional uncertainty (cosine angle), serving as inverse-variance weighting analogous to Kalman gain. Process noise can be added for registration error and calibration drift. [Curless & Levoy 1996](https://graphics.stanford.edu/papers/volrange/paper_2_levels/paper.html "SIGGRAPH 1996")

7. Bayesian occupancy grid: recursive log-odds update L(o_i|z_{1:k}) = L(o_i|z_k) + L(o_i|z_{1:k−1}) − L(o_i), which is a recursive Bayesian filter operating as x[k+1] = x[k] + Δ(u[k]). Foundation of probabilistic mapping since Elfes (1989). [Elfes 1989](https://www.researchgate.net/publication/2953854_Using_Occupancy_Grids_for_Mobile_Robot_Perception_and_Navigation "Computer 22(6), Occupancy Grids")

**C. Observation Models**

8. Pinhole camera projection: p' = K·[R|t]·P̃, nonlinear due to Z-division (u = α_x·X/Z + c_x). Jacobian ∂h/∂P = (1/Z)·[α_x, 0, −α_x·X/Z; 0, α_y, −α_y·Y/Z] is straightforward for EKF. [Stanford CS231A](https://web.stanford.edu/class/cs231a/course_notes/01-camera-models.pdf "Stanford CS231A, Camera Models")

9. CT/X-ray Beer-Lambert: y_i = Σ_j l_{ij}·μ_j + noise (log-domain), a **linear** observation model y = Ax + v. System matrix A encodes projection geometry via ray-tracing. Directly amenable to standard Kalman filtering for grain μCT. [De Man & Fessler 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3725149/ "Phys Med Biol 58(12):R63–R96, Physics models in iterative CT reconstruction")

**D. Observability and Controllability**

10. FIM ↔ observability equivalence: Jauffret (2007) proved FIM F_μ = ∇h·R_ε⁻¹·∇hᵀ is nonsingular iff the system is locally observable. CRLB = F_μ⁻¹ gives minimum estimation variance. Directly applicable to determining which grain shape parameters are estimable from a given sensor configuration. [Jauffret 2007](https://univ-tln.hal.science/hal-01820468/document "IEEE Trans. AES 43(2):756–759, Observability and FIM in Nonlinear Regression")

11. Observability Gramian for sensor placement: Brace et al. (2025) derived metrics including local unobservability index J_ν = 1/λ_min(W_o) and estimation condition number J_κ = λ_max/λ_min. Optimal placement formulated as convex SDP relaxation. UKF demonstrated that observability-optimal placement significantly reduces estimation error vs. random placement. [Brace et al. 2025](https://arxiv.org/html/2501.01726v1 "arXiv:2501.01726, Sensor Placement via Observability Gramians")

12. FIM applied to medical image reconstruction: Li et al. (2004) estimated FIM for PET reconstruction, using it to achieve near-uniform image resolution. Directly analogous to grain μCT — FIM quantifies which voxels/regions are most precisely estimable. [Li et al. 2004](https://pubmed.ncbi.nlm.nih.gov/15377114/ "IEEE Trans Med Imaging 23(9):1057–1064, FIM for PET reconstruction")

**E. Dimensionality Comparison**

13. State dimension spans five orders of magnitude: TSDF 256³ → 16.7M; TSDF 128³ → 2.1M; point cloud (10k pts) → 30k; SH ℓ=20 → 441; SH ℓ=10 → 121; superellipsoid → 11; triaxial ellipsoid → 9. EKF computational cost scales O(n³): n=441 is feasible (~86M ops/update); n=16.7M is intractable. This motivates parametric reduced-order state representations.

**F. Linearization**

14. TSDF update is inherently linear in the state; nonlinearity arises only in the observation model h(x). For parametric shapes, Jacobian ∂h/∂θ = (∂h/∂P)·(∂P/∂θ) is computable via chain rule. SH and superellipsoid with 11–441 parameters yield tractable Gramians for direct eigenvalue analysis.

**G. KinectFusion–Kalman Structural Analogy**

15. KinectFusion's four-stage loop is structurally isomorphic to Kalman prediction-correction. The weights W(v) serve as implicit confidence but lack cross-correlation tracking. Formalizing this as a state-space system with covariance propagation is the core contribution opportunity for this chapter. [Newcombe et al. 2011](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ismar2011.pdf "ISMAR 2011, KinectFusion pipeline structure")

### 可用图片
无（建议撰写时制作：(1) 状态表示维度对比图, (2) TSDF 更新规则示意图, (3) 观测模型（针孔投影 / CT 投影）示意图, (4) KinectFusion 流程与 Kalman 滤波器循环的结构对比图）

### 仍需补充
- Elfes 1989 原始论文 PDF 无法直接访问，当前关键发现基于多个转述来源；撰写时如需精确引用原始公式应获取原论文。
- Solina & Bajcsy 1990 原始论文 PDF 访问受限，inside-outside function 精确形式应从教科书或可访问综述验证。
- 观测模型 Jacobian 的完整显式计算示例（针对体积重建或形状估计上下文）尚未找到已发表参考；可能需要在报告中自行推导。
- 可控性（controllability）在 3D 重建上下文中的文献极为稀少；概念性映射（"给定可选视角能否到达任意目标3D状态"）需在报告中自行构建。
- Lie-algebraic 非线性可观性条件 (Hermann & Krener 1977) 仅在参考文献列表中出现，如需正式讨论需直接引用原文。

---

## Chapter 3：Observer and Estimator Design for Multi-Sensor Grain Reconstruction

### 研究目标
- Design Kalman filter variants (KF, EKF, UKF) for optimal fusion of multi-view and multi-modal sensor data to estimate grain 3D geometry.
- Address multi-rate and asynchronous fusion challenges.
- Analyze convergence conditions and connect to detectability of the state-space pair (A, C).
- Compare EKF, UKF, and information-form filter approaches in terms of accuracy and computational cost.

### 关键发现

**A. Standard Kalman Filter**

1. Kalman (1960) derived the optimal linear minimum-variance estimator: prediction x̂[k|k−1] = A·x̂[k−1], P[k|k−1] = A·P·Aᵀ+Q; correction K = P·Cᵀ·(C·P·Cᵀ+R)⁻¹, x̂[k|k] = x̂[k|k−1]+K·(y−C·x̂). For the grain CT model y = Ax+v (linear in log domain), KF applies directly. Steady-state gain exists when (A,C) is detectable. [Kalman 1960](https://asmedigitalcollection.asme.org/fluidsengineering/article/82/1/35/397706/A-New-Approach-to-Linear-Filtering-and-Prediction "ASME J. Basic Eng. 82(1):35–45")

2. Simon (2006) provides unified textbook treatment of KF, EKF, UKF, H∞ filter, and particle filters, including stability conditions and numerical issues (Joseph stabilized form, square-root implementations). [Simon 2006](https://onlinelibrary.wiley.com/doi/book/10.1002/0470045345 "Optimal State Estimation, Wiley")

**B. EKF for 3D Shape Estimation**

3. Yu, Wong & Chang (2005) demonstrated a two-step EKF for recursive 3D reconstruction from monocular images: Step 1 uses 12-state EKF for pose estimation; Step 2 runs N independent 3-state EKFs for per-point structure refinement. O(N) complexity vs. O(N³) for monolithic EKF. Achieved 0.69% mean 3D model error within 10 frames for 300-point models, 0.5 s per frame. [Yu et al. 2005](http://www.cse.cuhk.edu.hk/~khwong/j2004_IEEE_yu_SMC_B_kalman_draft.pdf "IEEE Trans. SMC-B 35(3), Recursive 3D Model Reconstruction Based on Kalman Filtering")

4. Pinhole camera Jacobian ∂h/∂P = (1/Z)·[fₓ, 0, −fₓX/Z; 0, fy, −fyY/Z] is analytically tractable. For parametric shapes, chain rule ∂h/∂θ = (∂h/∂P)·(∂P/∂θ) enables EKF for superellipsoid/SH grain tracking.

**C. UKF — Theory and Comparison**

5. Julier & Uhlmann (2004) established the unscented transformation: 2n+1 sigma points propagated through true nonlinear function, achieving second-order mean/covariance accuracy without Jacobian computation. O(n³) cost same as EKF. In reentry tracking benchmark, EKF peak MSE was **100× larger than its estimated covariance**, while UKF maintained close consistency. [Julier & Uhlmann 2004](https://www.cs.ubc.ca/~murphyk/Papers/Julier_Uhlmann_mar04.pdf "Proc. IEEE 92(3):401–422, Unscented Filtering and Nonlinear Estimation")

6. Wan & van der Merwe (2000) showed UKF converges faster and to lower MSE than EKF in dual estimation of chaotic Mackey-Glass time series. UKF directly approximates expected Hessian via sigma-point propagation. [Wan & van der Merwe 2000](https://groups.seas.harvard.edu/courses/cs281/papers/unscented.pdf "Proc. IEEE, The UKF for Nonlinear Estimation")

7. For superellipsoid (n=11): 23 sigma-point evaluations per update. For SH (n=441): 883 evaluations — heavier but feasible. Key tradeoff: EKF requires deriving 441-dim Jacobian; UKF replaces this with forward model evaluations, decisive when analytical Jacobian is unavailable (e.g., differentiable rendering).

**D. Multi-Rate Fusion**

8. Multi-rate KF: state prediction at fastest sensor rate; measurement updates applied only when each sensor delivers data. For grain phenotyping: RGB at 30 Hz drives predictions; CT data as asynchronous high-information measurement with its own Cᵢ, Rᵢ. Ghahremani et al. (2014) formalized the multirate multisensor framework via LCM-based state lifting. [Ghahremani et al. 2014](https://www.sciencedirect.com/science/article/abs/pii/S1270963814001126 "Aerospace Sci. Technol. 39:482–489")

**E. Information-Form Filter**

9. Information filter: H = P⁻¹, b = μᵀH. Measurement update is **additive**: H[k] = H̄[k] + CᵀR⁻¹C, enabling parallel multi-sensor computation. Thrun et al. (2004) SEIF achieved O(1) per-update in SLAM with only 14.6% higher error than full EKF, using constant time/memory vs. O(N²). Ideal for high-throughput multi-grain parallel scanning. [Thrun et al. 2004](http://robots.stanford.edu/papers/thrun.seif.pdf "IJRR, SLAM with Sparse Extended Information Filters")

10. Kim, Lee & Lee (2025) applied per-voxel 1D KF to TSDF with covariance intersection (CI) for collaborative map merging. Dynamically adjusted noise based on TSDF value (lower variance near zero-crossing). Demonstrated monotonic covariance convergence. Directly relevant: replaces heuristic TSDF weighted-average with explicit uncertainty tracking. [Kim et al. 2025](https://link.springer.com/article/10.1007/s11370-025-00586-1 "Intelligent Service Robotics, TSDF merging with KF+CI")

11. BayesFusion-SDF (Mazumdar et al. 2026) proposed probabilistic SDF fusion as sparse Gaussian random field with heteroscedastic Bayesian formulation. Posterior uncertainty enables next-best-view planning. State of the art in probabilistic volumetric fusion. [Mazumdar et al. 2026](https://arxiv.org/abs/2602.19697 "arXiv:2602.19697, BayesFusion-SDF")

**F. Convergence Analysis**

12. Reif et al. (1999/2000) proved EKF estimation error is exponentially bounded in mean square under: (i) uniform detectability of [∂f/∂z, ∂h/∂z], (ii) sufficiently small initial error, (iii) sufficiently small noise. Riccati solution bounded: pI ≤ P(t) ≤ p̄I. Divergence confirmed for large initial errors or noise. Detectability condition is the nonlinear analogue of (A,C) detectability — directly connecting to Ch. 2 observability analysis. [Reif et al. 2000](https://epublications.marquette.edu/cgi/viewcontent.cgi?article=1762&context=electric_fac "IEE Proc. CTA 147(1):45–52"); [Reif et al. 1999](https://ieeexplore.ieee.org/iel4/9/16302/00754809.pdf "IEEE TAC 44(4):714–728")

**G. CRLB Benchmark**

13. CRLB = F⁻¹ where F = JᵀR⁻¹J. Cumulative multi-view FIM: F_total = Σₖ Jₖᵀ Rₖ⁻¹ Jₖ. KF achieves CRLB for linear systems (minimum-variance unbiased estimator). For nonlinear camera observations, EKF/UKF covariance is benchmarked against CRLB. [Jauffret 2007](https://univ-tln.hal.science/hal-01820468/document "IEEE Trans. AES, FIM and Observability"); [Li et al. 2004](https://pubmed.ncbi.nlm.nih.gov/15377114/ "IEEE Trans. Med. Imaging, FIM for PET")

**H. TSDF as Special Case of KF**

14. Standard TSDF weighted-average update is formally a 1D KF: P[k|k−1] = 1/W[k], R = 1/w[k], K = w[k]/(W[k]+w[k]). The critical limitation: no cross-voxel correlation tracking. Three mitigation strategies: (a) parametric state reduction (SH 441-dim or superellipsoid 11-dim) for full-covariance KF, (b) independent per-voxel 1D KF (Kim et al. 2025), (c) information-form exploiting sparsity (SEIF).

**I. Physical Noise Parameters**

15. Q/R tuning grounded in physical noise: Q models registration error (σ ~ 0.01–0.1 mm for turntable positioning); R models sensor noise — RGB reprojection error (σ ~ 0.5–2 pixels), depth sensor (σ ~ 0.5–5 mm), μCT photon counting (Gaussian after log-transform, variance ≈ 1/N_photons).

### 可用图片
无（建议撰写时制作：(1) KF prediction-correction vs. TSDF update loop 对比图, (2) EKF vs. UKF sigma-point propagation示意图, (3) 多速率异步融合时间线图, (4) 信息矩阵稀疏性示意, (5) EKF 收敛曲线）

### 仍需补充
- 未找到专门针对3D形状参数（超二次曲面或SH系数）的 EKF vs. UKF 精度定量对比文献；建议通过仿真产生此数据。
- 未找到直接将多速率 KF 应用于"快速RGB + 慢速CT"3D重建的已发表文献；该概念映射需在报告中自行构建。
- Reif et al. (1999) 离散时间版本受 IEEE 访问限制，核心定理已从连续时间版本确认。
- CRLB 应用于谷物形状估计的数值示例需在撰写阶段自行推导。
- 协方差交叉 (CI) 原始理论参考 Julier & Uhlmann (1997, IEEE ACC) 未直接阅读，建议补充。

---

## Chapter 4：Optimal Control and Optimization-Based Design for the Phenotyping Pipeline

### 研究目标
- Apply optimal control and mathematical optimization for active improvement of the phenotyping pipeline.
- Formulate optimal sensor placement as maximizing the observability Gramian's minimum eigenvalue or minimizing trace of steady-state error covariance.
- Cast next-best-view (NBV) planning as a receding-horizon MPC problem.
- Design adaptive sampling strategies balancing reconstruction quality and throughput constraints.
- Optimize scanning trajectories for rotating stages or robotic arms.

### 关键发现

**A. Optimal Experimental Design for Sensor Placement**

1. Joshi & Boyd (2009) formulated sensor selection as convex optimization with D-optimal (max det(FIM)), A-optimal (min trace(Σ)), E-optimal (max λ_min(FIM)) criteria. Convex relaxation solvable in O(m³); for m=100 sensors, runs in milliseconds. Gap between relaxation and achieved objective ~5.3% for k=30 from m=100. Robust sensor selection under uncertainty via SDP. [Joshi & Boyd 2009](https://web.stanford.edu/~boyd/papers/pdf/sensor_selection.pdf "IEEE Trans. SP 57(2):451–462, Sensor Selection via Convex Optimization")

2. For grain phenotyping, measurement vector aᵢ maps to observation Jacobian ∂h/∂θ at viewpoint i. FIM F_total = Σ JₖᵀRₖ⁻¹Jₖ (from Ch. 2–3) is the optimization objective. D/A/E criteria directly determine optimal camera placement around the grain.

**B. Submodular Optimization**

3. Krause, Singh & Guestrin (JMLR 2008) proved MI-based sensor placement is NP-complete but greedy achieves (1−1/e)≈63% guarantee via submodularity. On Intel Berkeley Lab dataset, greedy was within 95% of optimal for 1–5 sensors. MI placements outperformed D/A/E-optimal in prediction RMSE. Lazy evaluation reduced complexity to O(kn). [Krause et al. 2008](https://www.jmlr.org/papers/volume9/krause08a/krause08a.pdf "JMLR 9:235–284, Near-Optimal Sensor Placements in Gaussian Processes")

4. Shamaiah, Banerjee & Vikalo (CDC 2010) proved log det(P⁻¹) is monotone submodular in selected sensor set for KF, enabling greedy with (1−1/e) guarantee. O(n²mk) complexity. Outperformed Joshi & Boyd convex relaxation in RMSE, especially when k ≈ n — precisely the regime for grain reconstruction (k≈10–20 views, n=11 superellipsoid). [Shamaiah et al. 2010](https://sidbanerjee.orie.cornell.edu/docs/CDC_sensorsel.pdf "CDC 2010, Greedy Sensor Selection: Leveraging Submodularity")

**C. Next-Best-View Planning**

5. Isler et al. (ICRA 2016) proposed 5 volumetric information formulations for active reconstruction on OctoMap: occlusion-aware, unobserved voxel, rear-side voxel, rear-side entropy, proximity count. Utility U_v = G_v/ΣG − C_v/ΣC balances information vs. movement cost. Achieved ~89–93% coverage within 20 views. Validated on KUKA YouBot. [Isler et al. 2016](https://rpg.ifi.uzh.ch/docs/ICRA16_Isler.pdf "ICRA 2016, Information Gain for Active Volumetric 3D Reconstruction")

6. GenNBV (Chen et al., CVPR 2024): RL-based generalizable NBV policy achieving **98.26% coverage** vs. 89.71% (uniform hemisphere), 91.19% AUC vs. 82.91%. Chamfer distance 0.37 cm vs. 0.44 cm (16% improvement). Generalizes across unseen objects and categories. Outperformed per-scene-optimized information-gain baselines. [Chen et al. 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_GenNBV_Generalizable_Next-Best-View_Policy_for_Active_3D_Reconstruction_CVPR_2024_paper.pdf "CVPR 2024, GenNBV")

**D. NBV as MPC / Trajectory Optimization**

7. Charrow et al. (RSS 2015) combined CSQMI information-theoretic planning with SQP trajectory optimization. Achieved mapping 2.3× faster than global-only, 3.3× faster than closest-frontier. Trajectory optimization reduced aerial robot distance by 36% (26.4 m vs. 41.4 m). [Charrow et al. 2015](https://www.roboticsproceedings.org/rss11/p03.pdf "RSS 2015, Information-Theoretic Planning with Trajectory Optimization")

8. Bircher et al. (ICRA 2016) proposed receding-horizon NBV via RRT — the canonical MPC–NBV connection: finite-horizon optimization with replanning, naturally trading exploitation vs. exploration. [Bircher et al. 2016](https://dl.acm.org/doi/10.1109/ICRA.2016.7487281 "ICRA 2016, Receding Horizon NBV Planner")

**E. Submodular Trajectory Optimization**

9. Roberts et al. (ICCV 2017) formulated aerial scanning trajectory as submodular orienteering solved via ILP (Gurobi, <10% optimality gap). Achieved 20% more coverage than NBV baseline, accuracy 115.2 mm vs. 170.2 mm (overhead, 32% improvement), visual error 3.3% vs. 7.1% (54% reduction). Key contribution: joint view selection + routing optimization. [Roberts et al. 2017](https://openaccess.thecvf.com/content_ICCV_2017/papers/Roberts_Submodular_Trajectory_Optimization_ICCV_2017_paper.pdf "ICCV 2017, Submodular Trajectory Optimization for Aerial 3D Scanning")

**F. Cost Function and LQG Analogy**

10. The optimal view planning cost J = Σ[α·trace(P[k|k]) + β·c(u[k])] directly parallels LQR cost Σ[xᵀQx + uᵀRu]: trace(P) as state cost, c(u) as control cost. Separation principle (LQG): estimator (Ch. 3 KF/EKF) and controller (view planner) designed independently — exact for linear-Gaussian, approximate for EKF under small noise.

**G. Adaptive Sampling**

11. Batch-level resource allocation: min Σ trace(Pᵢ[Kᵢ]) s.t. Σ Kᵢ ≤ K_total. Submodularity (Krause et al., Shamaiah et al.) implies diminishing returns → greedy allocation optimal: allocate next view to grain with highest marginal FIM gain. Simple grains (near-spherical) need few views; complex grains (elongated, with ventral sulcus) need more. Per-grain stopping: trace(Pᵢ) < ε or λ_min(Fᵢ) > threshold.

**H. Trajectory as Orienteering/TSP**

12. Given selected viewpoints, minimum-time scanning trajectory is TSP on the viewpoint graph. Roberts et al. (2017) used ILP for orienteering with travel-budget constraint. For turntable-based grain scanning, TSP reduces to minimum-rotation-angle sequence, solvable by Christofides algorithm or nearest-neighbor heuristic.

**I. Quantitative Improvement Summary**

13. Consistent 20–50% improvement from optimization over heuristics: GenNBV +8.55 pp coverage, +16% accuracy; Roberts +32% accuracy over overhead; Charrow 2.3× faster mapping; Krause within 95% of optimal; Shamaiah outperforms convex relaxation across all tested configurations.

### 可用图片
无（建议撰写时制作：(1) D/A/E-optimal 置信椭球与视角配置, (2) 贪心子模算法流程与(1−1/e)保证, (3) NBV 规划循环, (4) 信息增益递减收益曲线, (5) 均匀 vs. 优化采样对比）

### 仍需补充
- 未找到将 D-optimal/NBV/子模优化直接应用于谷物或种子 3D 扫描的文献；需自行构建从通用理论到谷物表型的映射。
- Olague & Mohr (2002, Pattern Recognition) 经典相机放置论文未直接阅读，可能包含与本章相关的 FIM-based 相机网络设计方法。
- 自适应采样在实际高通量表型流水线中的吞吐量数据缺失（如不同复杂度谷物的视角分配、每小时处理量等）。
- Pontryagin 最小值原理在 3D 扫描轨迹优化中的直接应用文献未找到；Roberts et al. 使用 ILP 而非连续最优控制。如需引入 Pontryagin 原理，需自行推导离散类比。

---

## Chapter 5：System Performance Analysis — Stability, Robustness, and Sensitivity of the Phenotyping Pipeline

### 研究目标
- Analyze the closed-loop phenotyping system for stability (Lyapunov-based EKF/UKF error covariance boundedness), robustness to modeling errors (lens distortion, non-Lambertian surfaces), and sensitivity to parameter uncertainties.
- Quantify how 3D reconstruction uncertainties propagate to phenotypic trait extraction errors.
- Evaluate robustness of optimal sensor configurations to perturbations in grain size, cultivar variability, and mechanical positioning errors.
- Define performance metrics: reconstruction completeness, trait accuracy, throughput, and their trade-offs.

### 关键发现

**A. Lyapunov Stability**

1. Haring & Johansen proved exponential ISS of discrete-time KF: under uniform controllability (W_c ≥ c_c·I) and observability (W_o ≥ c_o·I), estimation error satisfies ‖e_k‖ ≤ max{c_e·ρ_e^{k−k₀}·‖e_{k₀}‖, c_w·max‖wᵢ‖, c_v·max‖vⱼ‖} with ρ_e<1. Lyapunov function V_k = eₖᵀP_k⁻¹eₖ. ISS formulation enables small-gain analysis of cascaded estimator+controller. [Haring & Johansen](https://torarnj.folk.ntnu.no/KF_paper_v8.pdf "On the stability bounds of Kalman filters for linear deterministic discrete-time systems")

2. Karvonen, Bonnabel, Moulines & Särkkä (2020) unified stability framework for EKF, UKF, and Gaussian integration filters: E(‖Eₖ‖²) ≤ ρ^{2k}·(‖μ₀−x̂₀‖²+tr(Σ₀)) + [σ²(tr(Q)+C_f·ū_P) + κ²·tr(R)]/(1−ρ²), where C_f=0 for EKF, C_f=‖J_f‖ for UKF. Requires ρ = sup‖J_f‖·‖I−K_kH‖ < 1. [Karvonen et al. 2020](https://arxiv.org/pdf/1809.05667 "arXiv:1809.05667, Stability of Nonlinear Kalman Filters")

3. Bonnabel & Slotine (2015) via contraction theory: EKF converges exponentially with rate γ ≤ q/(2p̄) when virtual system is contracting. Yields global convergence without bounded Hessians. Directly provides disturbance rejection bound: ‖x_p − x̂‖ ≤ √(p̄/p)·γ·‖b‖_max. [Bonnabel & Slotine 2015](https://arxiv.org/pdf/1211.6624 "IEEE TAC 60(2):565–569, Contraction-based EKF stability")

4. Reif et al. (1999) discrete-time EKF bounded stability: E{‖ξ‖²} ≤ (β̄/β)·‖ξ(0)‖²·exp(−γt) + ν under uniform detectability + small initial error + small noise. Connects to Ch. 2 observability analysis. [Reif et al. 1999](https://ieeexplore.ieee.org/iel4/9/16302/00754809.pdf "IEEE TAC 44(4):714–728")

**B. Robustness — H∞ and μ-Analysis**

5. H∞ filter: minimax estimation minimizing worst-case error ratio J = [Σ‖x−x̂‖²]/[Σ‖w‖²+Σ‖v‖²] < 1/γ for all disturbances. Does not require known noise statistics or zero-mean assumption. Outperforms KF under misspecified noise (non-Gaussian, doubled process noise). Relevant for grain reconstruction when Lambertian assumption or calibration deviate. [Simon 2006](https://onlinelibrary.wiley.com/doi/book/10.1002/0470045345 "Optimal State Estimation, Wiley")

6. Structured singular value μ: necessary and sufficient for robust stability/performance with block-diagonal perturbations Δ. For grain pipeline: Δ₁ (lens distortion calibration error), Δ₂ (non-Lambertian reflectance), Δ₃ (turntable positioning error). μ(M) ≤ inf_D σ_max(D⁻¹MD) via D-scaling. Robust performance condition: |W₁·T| + |W₂·S| ≤ 1. [Dahleh et al., MIT OCW](https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/e93427e1e654f3c9fb86edcd3215206a_MIT6_241JS11_chap21.pdf "MIT 6.241J, Structured Singular Value")

7. Small-gain theorem: cascaded estimator-controller stable if γ_est·γ_ctrl < 1, via Haring & Johansen ISS framework. Conservative for unstructured Δ; μ-analysis tightens for structured perturbations.

**C. Sensitivity Analysis**

8. GUM (JCGM 100:2008) standard: Cov(φ) = (∂g/∂x)·P[k]·(∂g/∂x)ᵀ where φ = g(x) is trait extraction. Expanded uncertainty U = k·u_c with coverage factor k = 2–3 (95–99% confidence). Type A (statistical) and Type B (calibration, specs) uncertainty sources. [JCGM 100:2008](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf "GUM, BIPM/ISO/IEC 2008")

9. For superellipsoid (11 params): volume V = 2a₁a₂a₃ε₁ε₂B(...)B(...), with ∂V/∂aᵢ = V/aᵢ analytically. For SH (441 coefficients): volume involves integrals of triple SH products (Gaunt coefficients). First-order analysis identifies dominant uncertainty sources: semi-axis lengths dominate volume uncertainty; higher-order SH coefficients dominate shape descriptor uncertainty.

10. Monte Carlo propagation (GUM Supplement 1): M = 10⁴–10⁶ samples from P[k], evaluate φ = g(x+δx), derive empirical distribution. Captures nonlinear effects for ratios like sphericity φ = π^{1/3}(6V)^{2/3}/S. Comparison with linearized GUM quantifies first-order approximation adequacy.

**D. Robust Sensor Placement**

11. Attia, Leyffer & Munson (2023): max-min robust A-optimal design for misspecified priors/noise. Alternates stochastic gradient ascent (sensor activation) with gradient descent (worst-case parameters). Redundancy ratio >80%. For grain phenotyping, uncertain parameters: cultivar shape variability, surface reflectance R, positioning error. [Attia et al. 2023](https://arxiv.org/pdf/2305.03855 "arXiv:2305.03855, Robust A-Optimal Experimental Design")

12. FIM condition number κ(F_total) = λ_max/λ_min measures information balance. E-optimal criterion (max λ_min) is inherently most robust to worst-case. Placement should maintain κ ≤ threshold across grain morphologies (spherical ε≈1 to elongated a₁/a₃>2). Joshi & Boyd (2009) robust sensor selection via SDP handles measurement matrix uncertainty.

**E. Performance Metrics**

13. 3D reconstruction metrics: Chamfer Distance (average bidirectional NN distance, resilient to noise), Hausdorff Distance (worst-case, sensitive to outliers), Cloud-to-Mesh Distance (superior across perturbation types). Alibekov et al. (VISAPP 2024): C2M mean 0.03–0.42 mm; Hausdorff 9.56–48.98 mm for industrial objects. [Alibekov et al. 2024](https://www.scitepress.org/Papers/2024/124213/124213.pdf "VISAPP 2024, Evaluation of 3D Point Cloud Distances")

14. Benchmarks from grain domain: Chamfer 0.37 cm (GenNBV), L1 ~40 μm and volume error ~2.36% (wheat seeds SH ℓ=20). Sources: [Chen et al. 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_GenNBV_Generalizable_Next-Best-View_Policy_for_Active_3D_Reconstruction_CVPR_2024_paper.pdf "CVPR 2024"), [Cherepashkin et al. 2023](https://openaccess.thecvf.com/content/ICCV2023W/CVPPA/papers/Cherepashkin_Deep_Learning_Based_3d_Reconstruction_for_Phenotyping_of_Wheat_Seeds_ICCVW_2023_paper.pdf "ICCV 2023W")

15. Phenotypic trait metrics: bias E[φ̂−φ_true], RMSE, σ_φ precision, surface coverage ratio, throughput = 3600/(K·t_view + t_process). Accuracy–throughput tradeoff governed by submodular diminishing returns (Ch. 4). Superellipsoid K=10 views → ~360 grains/hr; SH ℓ=20 K=20–30 views → ~120–180 grains/hr.

**F. Disturbance Rejection**

16. Environmental disturbances modeled as exogenous inputs: vibration w_vibration (σ~0.01–0.1 mm), lighting variation (5–20% intensity), thermal drift (0.01–0.05 mm/°C). Sensitivity function S(z) maps process disturbances to estimation error; complementary sensitivity T(z) maps measurement noise. Robust performance: ‖W₁T‖ + ‖W₂S‖ ≤ 1.

17. Contraction framework quantifies: steady-state error ≤ √(p̄/p)·γ·‖b‖_max. Faster contraction (higher Q or more informative measurements) and better-conditioned P improve disturbance rejection.

**G. System Integration**

18. Cascaded ISS analysis: estimation (ISS gain γ_est) → control (gain γ_ctrl) → trait extraction (linear gain ‖∂g/∂x‖). Overall stable if γ_est·γ_ctrl < 1 (small-gain) or cascade ISS conditions met. Provides end-to-end bounded trait error under bounded disturbances.

### 可用图片
无（建议撰写时制作：(1) Lyapunov 函数 V_k 演化与边界图, (2) M-Δ 反馈结构图标注表型流水线扰动, (3) 不确定性传播流程图 x→P→∂g/∂x→Cov(φ), (4) 精度 vs. 吞吐量权衡曲线, (5) Chamfer/Hausdorff/C2M 对比图）

### 仍需补充
- H∞ 滤波器应用于 3D 形状估计的定量对比文献未找到，需在报告中自行推导超二次曲面状态估计的 H∞ 公式。
- μ-分析在状态估计环路（而非控制器）中的直接应用文献稀少，需类比推导。
- 谷物表型特征的定量蒙特卡罗不确定性仿真结果需在撰写阶段通过仿真产生。
- Taguchi 方法在 3D 测量灵敏度分析中的应用参考未找到（该方法在制造质量控制广泛使用），需类比引用。
- 传感器热漂移和振动的定量规格数据需在 Ch. 6 案例研究中根据具体硬件补充。

---

## Chapter 6：Integrated Design Case Study — A Complete Control-Theoretic Phenotyping Pipeline for Rice Grain 3D Reconstruction

### 研究目标
- Synthesize models, estimators, controllers, and analysis tools from Chapters 2–5 into a fully specified end-to-end pipeline for rice grain phenotyping.
- Instantiate concrete state-space model with numerical parameters for a rice grain scanning setup.
- Implement and tune EKF/UKF for the rice grain system; evaluate real-time feasibility.
- Compare the optimal scanning protocol (from Ch. 4) against a baseline uniform-spacing protocol.
- Evaluate performance via Chamfer distance, Hausdorff distance, phenotypic trait errors, and throughput.
- Validate robustness predictions of Ch. 5 under perturbed conditions.

### 关键发现

**A. Rice Grain Morphology**

1. Indica vs. japonica differ markedly: Nipponbare (japonica reference) 5.17±0.07 × 2.67±0.03 × 2.01±0.03 mm, volume 14.83 mm³; indica long-grain (At 378) 6.07±0.07 × 2.44±0.09 × 1.82±0.14 mm, volume 14.48 mm³. OECD/IRRI classification by length and LWR (slender >3.0, medium 2.4–3.0, bold 2.0–2.4, round <2.0). [OECD 2021](https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/04/reviewing-indica-and-japonica-rice-market-developments_4d78ea81/0c500e05-en.pdf "OECD Rice Report"); [Manamgoda et al. 2024](https://www.mdpi.com/2673-4591/67/1/58 "Eng. Proc. 67(1):58, Rice Grain Quality")

2. Superellipsoid mapping: indica long-grain a₁≈3.0–3.5 mm, a₂≈1.2–1.5 mm, a₃≈0.8–1.0 mm; japonica round a₁≈2.6 mm, a₂≈1.3 mm, a₃≈1.0 mm. Shape exponents ε₁≈0.8–1.2, ε₂≈0.8–1.0 (slightly sub-ellipsoidal to ellipsoidal).

3. Grain traits highly heritable: grain length h²=0.915, width h²=0.885, thickness h²=0.852, TGW h²=0.831. Grain width shows strongest TGW correlation (R²=0.392, p<0.001). 43 QTLs identified; qGL1-1BFSG explains 65.2–72.5% of length variance. [Kabange et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10708019/ "Plants 12(23):4044, GWAS for rice grain traits")

**B. Existing 3D Scanning Setups**

4. Qin et al. (2022) structured-light benchmark: Reeyee Pro + 6-DOF robot arm, 2,200 cereal grains, accuracy 0.05 mm, point spacing 0.16 mm. Rice grain MAPE: length 2.07%, width 0.97%, thickness 1.13%. Volume/SA error vs. sphere: 1.75%/2.83%. Throughput 9.6 s/grain. Indica/japonica classification 99.95% (SVM, 25 traits). [Qin et al. 2022](https://www.nature.com/articles/s41598-022-07221-4 "Scientific Reports")

5. Reeyee Pro specs: precision 0.1 mm (fixed), 550k pts/s, 15 fps, scan range 210×150 mm, cost ~$20k. Turntable rotation 30° increments (12 views/360°). [Wiiboox](https://www.wiiboox.com/3d-scanner-reeyee-pro.php "Reeyee Pro specs")

6. Hu et al. (2020) X-ray CT pipeline: 22 grain traits from intact panicles, 90 kV/3.2 mA, 450 projections, ~0.3 mm resolution. R² grain number 0.980, length 0.960. Volume–weight R²>0.98. 9-variety classification 94.2% (SVM, LOO-CV). [Hu et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7706343/ "Plant Phenomics, Rice grain X-ray CT pipeline")

**C. State-Space Model Parameters**

7. Superellipsoid (n=11): nominal x = [3.3, 1.3, 0.9, 1.0, 1.0, 0, 0, 0, 0, 0, 0]ᵀ mm. Predicted volume ≈16.1 mm³. Process noise Q: σ_position≈0.01–0.05 mm, σ_angle≈0.01–0.1° for turntable; shape parameters Q≈0 (stationary grain).

8. SH model: ℓ_max=10 (121 coefficients) likely sufficient for smooth rice morphology; ℓ_max=20 (441) for fine features. Rice grains are smoother than wheat (no ventral sulcus), favoring lower ℓ_max.

9. Camera parameters: f=16–25 mm macro, 5 MP (2448×2048), pixel pitch 3.45 μm, WD 200–300 mm, spatial resolution ~0.05–0.10 mm/pixel. R: σ_pixel≈0.5–1.0 px (structured light subpixel accuracy), σ_spatial≈0.025–0.10 mm.

**D. Performance Evaluation**

10. Reconstruction accuracy: structured light ~0.05 mm (Qin 2022), X-ray CT ~0.3 mm (Hu 2020), deep-learning SH ~40 μm L1 error (Cherepashkin 2023). Ground truth: Mitutoyo micrometer ±0.01 mm, standard sphere validation, YTS machine vision.

11. Accuracy–throughput frontier: (a) Structured light: ~10 s/grain, ~360/hr, MAPE 1–2%; (b) μCT: ~24 s/grain, ~150/hr, MAPE <1%; (c) DL 3-view: ~2 s, ~1500/hr, volume error ~2.4%. Control-theoretic pipeline targets (a) with accuracy approaching (b).

**E. Computational Cost**

12. EKF O(n³): superellipsoid (n=11) → 1,331 ops/update (trivial); SH ℓ=10 (n=121) → 1.77M ops (~100 Hz on CPU); SH ℓ=20 (n=441) → 86M ops (~10–50 Hz on CPU). P matrix memory: 441² × 8 bytes ≈ 1.56 MB. All comfortably real-time at 1 view/s scanning rate.

13. UKF: superellipsoid 23 sigma points (~2.3 ms); SH ℓ=10: 243 points (~24 ms); SH ℓ=20: 883 points (~0.4 s on single CPU core). Marginal for ℓ=20 but feasible at 1 Hz.

14. D-optimal placement: O(m³) = 360³ ≈ 47M ops (milliseconds). Greedy submodular O(n²mk): 441²×360×12 ≈ 840M ops (~1 s). Offline computation, not a bottleneck.

**F. Breeding Relevance**

15. Volume is the most important 3D trait for yield: total grain volume R²>0.98 with weight (Hu et al. 2020). 5 selected 3D traits explain 98.6% of weight variance. 3D measurement surpasses 2D imaging for yield assessment.

16. China GB/T 1354-2018 classifies milled rice quality; GB/T 17891-2017 classifies high-quality rice by length (long ≥6.5 mm, medium 5.5–6.5 mm, short <5.5 mm). Structured-light MAPE 2.07% on length (±0.12 mm on 6 mm grain) exceeds regulatory precision requirements. [USDA/FAS](https://www.fas.usda.gov/data/china-national-standard-rice "China GB/T 1354-2018 translation")

**G. End-to-End Pipeline**

17. Complete pipeline: (a) State: superellipsoid n=11 (fast) or SH n=121–441 (high-fidelity); (b) Observation: structured-light depth via pinhole projection; (c) Estimator: EKF (superellipsoid) or UKF (SH); (d) Placement: D-optimal or greedy submodular K=8–12 from m=360; (e) Online NBV: receding-horizon max trace(P⁻¹) reduction, adaptive stop at trace(P)<ε; (f) Trajectory: min-time turntable TSP; (g) Stability: Reif et al. conditions; (h) Uncertainty: GUM Cov(φ) = (∂g/∂x)P(∂g/∂x)ᵀ; (i) Robustness: H∞ filter for non-Lambertian surfaces.

18. Timing budget: placement ~2 s, viewpoint computation <0.1 s, 12 views × 0.5 s = 6 s, EKF <1.2 s (concurrent), trait extraction <0.1 s. Total ~8–10 s/grain. Adaptive stopping: simple grains 6–8 views (5–6 s), complex 12 views. Throughput: ~400–700 grains/hr.

19. Expected improvements: (a) Optimal viewpoints: 10–20% MAPE reduction at same view count (analogous to GenNBV 16% improvement); (b) EKF/UKF: principled multi-view fusion reduces outlier-driven errors; (c) Adaptive stopping: 20–40% throughput increase at equivalent accuracy via submodular diminishing returns.

### 可用图片
无（建议撰写时制作：(1) 端到端流水线框图标注 Ch. 2–5 组件, (2) 稻谷粒超二次曲面参数化示意图, (3) D-optimal vs. 均匀视角配置对比, (4) MAPE vs. 视角数权衡曲线, (5) trace(P[k]) 随 k 递减至阈值的自适应停止时序图）

### 仍需补充
- 稻谷粒超二次曲面形状指数 ε₁、ε₂ 的精确拟合值基于形态推断，未找到直接将超二次曲面拟合到稻谷粒 3D 数据的文献；建议通过数值拟合实验确认。
- SH ℓ_max 对稻谷粒重建精度的消融研究（ℓ=5,10,15,20）缺乏实验数据；Cherepashkin et al. 仅报告了 ℓ=20 用于小麦。
- 控制论流水线相比常规流水线的定量对比实验数据基于类比推断，需通过仿真验证。
- Reeyee Pro 热漂移和振动规格未在制造商产品页面公开。
- GB/T 17891-2017 全文受付费墙限制，分类阈值已从多来源交叉确认。

---

## Chapter 7：Conclusions and Future Directions

### 研究目标
- Summarize main results and identify which control-theoretic tools proved most impactful.
- Distill actionable design guidelines for practitioners.
- Discuss limitations (grain opacity, computational cost, calibration reliance).
- Outline future directions: field-level phenotyping, genomic integration, deep-learning observation models, reinforcement-learning scanning policies, edge deployment.

### 关键发现

**A. Extension to Panicle/Field-Level Phenotyping**

1. PanicleNeRF (Yang et al., Plant Phenomics 2024): NeRF-based 3D reconstruction of intact rice panicles from smartphone video. Panicle length rRMSE 2.94% (indica), 1.75% (japonica). Volume correlated with grain number (R²=0.85 indica, 0.82 japonica) and grain mass (R²=0.80, 0.76). Control-theoretic framework could extend to panicle-level state vector with NeRF-based observation model. [PanicleNeRF](https://www.sciopen.com/article/10.34133/plantphenomics.0279 "Plant Phenomics 2024, PanicleNeRF")

2. Panicle-3D (Gong et al., Plant Phenomics 2021): first DL-based 3D point cloud segmentation for rice panicle phenotyping. PointConv-based architecture achieved 93.4% accuracy, 86.1% IoU. Panicle-level state-space modeling requires capturing branching topology — substantially higher-dimensional than single-grain models. [Panicle-3D](https://spj.science.org/doi/10.34133/2021/9838929 "Plant Phenomics 2021, Panicle-3D")

3. Hu et al. (2020) CT of intact panicles (22 traits, 104 panicles) demonstrates non-destructive panicle-level phenotyping. CT observation model (Beer-Lambert) maps directly to Ch. 2 state-space framework; D-optimal design could optimize projection count/angles. [Hu et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7706343/ "Plant Phenomics, Rice grain X-ray CT")

**B. Genomics Integration**

4. Chen et al. (Plant Phenomics 2024): UAV 3D point cloud → PointNet++ segmentation → dynamic 3D phenotypes → GWAS. Successfully mapped Rht12 (chr5A, −log₁₀P=6.32) for height and TaDWF4-3A for nitrogen use efficiency in wheat (160 varieties, 660k SNPs). Demonstrates that control-theoretic 3D reconstruction with uncertainty quantification (Ch. 5 GUM) could directly feed GWAS with per-trait confidence intervals. [Chen et al. 2024](https://spj.science.org/doi/10.34133/plantphenomics.0270 "Plant Phenomics 2024, 3D Phenotyping to GWAS for Wheat NUE")

5. Kabange et al. (2023) GWAS on 143 RILs: 43 QTLs for grain traits, h²=0.831–0.915 for L/W/T/TGW. High heritability confirms biological utility of precise 3D phenotyping for QTL mapping.

**C. NeRF/3DGS as Learned Observation Models**

6. Arshad et al. (Plant Phenomics 2024): NeRF evaluation for plant reconstruction — NeRFacto achieved 82.8% F1 (indoor), 74.6% F1 (outdoor field). LPIPS early stopping reduced training by 61.1% with only 7.4% F1 reduction. NeRF as differentiable h(x) enables automatic Jacobian computation for EKF via backpropagation. [Arshad et al. 2024](https://spj.science.org/doi/10.34133/plantphenomics.0235 "Plant Phenomics 2024, NeRF for Plant Reconstruction")

7. Gao et al. (Agriculture 2025): 3D Gaussian Splatting for seed phenotyping (maize, wheat, rice) — R²=0.936 (length), 0.889 (width), 0.946 (height), PSNR 35–37 dB. 3DGS state = set of Gaussians (μ, Σ, α, SH color coefficients), differentiable splatting enables EKF integration. [Gao et al. 2025](https://www.mdpi.com/2077-0472/15/22/2329 "Agriculture 15(22):2329, Seed 3D Phenotyping via 3DGS")

8. Learned observation models (NeRF/3DGS) capture non-Lambertian reflectance, translucency, and grain surface texture that analytical models cannot, potentially reducing model mismatch addressed by H∞ framework (Ch. 5). Tradeoff: ~30 min GPU training per scene vs. zero training for analytical model.

**D. RL-Based Scanning Policies**

9. GenNBV (CVPR 2024): 98.26% coverage with PPO-trained policy, constant-time inference (amortized computation) vs. O(n²m) per step for MPC-based NBV. Could generalize across cultivars without per-grain replanning.

10. RL-NBV (Wang et al., Pattern Recognition Letters 2024): raw point cloud input to DQN agent, eliminating ray casting overhead. RL agent observation could include superellipsoid/SH state estimate + P[k], learning MPC cost function from data. [RL-NBV](https://www.sciencedirect.com/science/article/abs/pii/S0167865524001582 "Pattern Recogn. Lett. 2024, RL-NBV")

11. MPC vs. RL complementary strengths: MPC offers interpretable cost functions, provable (1−1/e) guarantees, no training data; RL offers constant-time inference, learnable non-analytical rewards, cross-cultivar generalization. Hybrid approach: use MPC for initial development, then distill into RL policy.

**E. Edge Deployment**

12. NVIDIA Jetson AGX Orin: 275 TOPS (INT8), 5.3 TFLOPS (FP32), 64 GB LPDDR5, 15–60 W. EKF at n=441: ~86M ops → ~0.02 ms at 5.3 TFLOPS, enabling >1 kHz update rate. UKF 883 sigma points: ~0.1 ms. P matrix memory 1.56 MB. Jetson Orin Nano ($249, 2.1 TFLOPS) also sufficient. [NVIDIA Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/ "NVIDIA Jetson Orin specifications")

13. Ibrahim et al. (2025): YOLOX on Jetson AGX Orin achieved 107 FPS, 0.58 J/frame for potato harvesting. Validates edge AI for agricultural automation at throughputs far exceeding grain scanning ~1 view/s. [Ibrahim et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349356/ "AgriEngineering 2025, Real-Time Object Detection on Jetson")

**F. Synthesis**

14. The report's central contribution: formalization of grain 3D phenotyping as a closed-loop control problem, a perspective absent from all prior phenotyping literature (confirmed by Yang et al. 2020 and Pieters et al. 2023 comprehensive reviews). Fills the gap with: state-space formulations (Ch. 2), EKF/UKF estimators with convergence guarantees (Ch. 3), optimal placement + NBV with submodular guarantees (Ch. 4), stability/robustness/uncertainty frameworks (Ch. 5), integrated case study at 400–700 grains/hr (Ch. 6).

15. Three core design principles: (a) **Separation of estimation and control** (LQG separation principle); (b) **Covariance as universal optimization objective** — P[k] unifies estimation quality (Ch. 3), sensor placement (Ch. 4), adaptive stopping (Ch. 4), and GUM uncertainty propagation (Ch. 5); (c) **Submodular diminishing returns** — rigorous basis for heterogeneous view allocation across grain complexity levels.

**G. Limitations**

16. Three principal limitations: (a) Lack of experimental validation — predicted 10–20% accuracy improvement and 20–40% throughput increase are based on analogy with NBV literature, not direct experiments; (b) Linearity assumptions — EKF convergence (Reif et al.) requires small initial error/noise, conditions potentially violated with poor initial shape guess; (c) Parametric model restriction — superellipsoid/SH assume star-convex shapes; deep concavities (wheat ventral sulcus) may require hybrid representations.

### 可用图片
无

### 仍需补充
- 控制论流水线 vs. 常规流水线的直接实验对比数据尚不存在；Ch. 6 定量预期基于类比推断。
- NeRF/3DGS 作为 EKF 观测模型的集成实验尚无已发表文献；需量化 Jacobian 计算开销与解析模型的对比。
- RL 策略在毫米级种子扫描场景（低维动作空间、<0.05 mm 精度）中的训练和泛化数据缺失。
- Jetson 平台上 EKF/UKF 的实际基准测试需通过实际部署确认（矩阵运算库效率、CUDA 调度开销等）。

---

# Section 2：给 Write 阶段的执行建议

- **时间口径**：研究时间范围为 2025 年 4 月至 2026 年 10 月（回顾近一年 + 展望半年），当前日期 2026-04-03。文献检索覆盖 2020–2026 年，核心引用集中于 2022–2026 年。
- **写作语言**：全文使用英文（English），因用户请求为英文。
- **跨章节符号一致性**：Chapters 2–6 共用同一套状态空间模型。状态向量 x、输入 u、输出 y、过程噪声 w、量测噪声 v 的定义必须在 Chapter 2 一次性确立，后续章节严格引用。误差协方差矩阵 P 在 Chapter 3（估计器输出）和 Chapter 4（代价函数）之间必须保持同一符号和维度。
- **符号表约定**：x[k] ∈ ℝⁿ（状态向量）、u[k]（控制输入/视角选择）、y[k] ∈ ℝᵐ（观测）、f(·)/h(·)（非线性状态转移/观测函数）、A[k]/C[k]（雅可比矩阵）、w[k]~𝒩(0,Q)、v[k]~𝒩(0,R)、P[k]（误差协方差）、K[k]（卡尔曼增益）、𝒪（可观性 Gramian）、𝒞（可控性 Gramian）、φ = g(x)（表型特征提取函数）。统一使用方括号 [k] 表示离散时间步。
- **定量 vs. 概念分布**：Chapters 1, 7 以概念性综述为主；Chapter 2 混合（含至少一个可观性 Gramian 数值算例）；Chapter 3 偏定量（EKF 收敛仿真）；Chapter 4 偏定量（最优 vs. 均匀传感器配置比较）；Chapter 5 混合（解析稳定性证明 + 蒙特卡洛灵敏度分析）；Chapter 6 重度定量（完整案例研究含表格、误差度量、对比图）。
- **写作顺序建议**：Chapter 2 须先定稿（锁定符号和模型结构）。Chapters 3 和 4 可并行起草。Chapter 5 依赖 3 和 4。Chapter 6 最后撰写。
- **图表建议**：Ch. 1 需要开环 vs. 闭环管道对比框图；Ch. 2 需要状态空间模型信号图 + 不同状态表征图解 + Gramian 特征值柱状图；Ch. 3 需要 EKF 框图 + 收敛曲线 + EKF/UKF/批量最小二乘对比图；Ch. 4 需要最优 vs. 均匀相机配置可视化 + 信息增益热力图 + MPC 滚动时域图解；Ch. 5 需要灵敏度蛛网图/龙卷风图 + 鲁棒性包络图 + 蒙特卡洛散点图；Ch. 6 需要扫描装置示意图 + 渐进重建快照 + 精度对比表 + Pareto 曲线。
