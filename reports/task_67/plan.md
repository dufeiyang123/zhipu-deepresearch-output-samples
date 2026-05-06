# Section 1：章节研究计划

## Chapter 1：Background and Motivation — The Exploration Challenge in Sparse-Reward and Constrained Reinforcement Learning

### 研究目标
- Define the sparse-reward MDP problem and canonical failure modes of standard exploration strategies (ε-greedy, Boltzmann, Gaussian noise) under reward sparsity
- Formalize the constrained RL problem (CMDPs, chance constraints, state-wise safety constraints) and explain why constraint structure conflicts with broad exploration
- Motivate the connection to trajectory planning: why robotic, autonomous driving, and drone planning naturally exhibit both sparse rewards and hard safety constraints
- Establish survey scope and time horizon (April 2025 – March 2026 literature, 6-month forward outlook to September 2026)

### 关键发现
- A sparse-reward MDP is one where the reward function r(s,a) returns a non-zero signal only at a small fraction of state-action pairs (typically task completion); in many problems, "thousands of decisions might need to be made before outcomes are visible" [Ladosz et al., Exploration in Deep RL Survey](https://www.sciencedirect.com/science/article/abs/pii/S1566253522000288 "2022 Information Fusion survey on exploration in deep RL"). Diaz-Bone et al. (2025) characterize sparse-reward RL as intractable without structured curricula of simpler sub-tasks [Diaz-Bone et al., Automated Curricula for Sparse-Reward RL](https://arxiv.org/html/2505.19850v2 "2025 ETH Zürich paper on automated curricula for sparse-reward RL").
- Dann et al. (2022) prove that ε-greedy RL requires O((A/ε)^H) episodes to find the optimal policy in worst-case sparse-reward MDPs—exponential in horizon H. Boltzmann exploration suffers the same exponential lower bound with gap scaling α ∝ (Ae^{-β})^{-H/2}. Gaussian noise policies perturb the greedy policy only locally, unable to discover distant high-reward states [Dann et al., Guarantees for Epsilon-Greedy RL](https://proceedings.mlr.press/v162/dann22a/dann22a.pdf "ICML 2022 paper on theoretical guarantees for ε-greedy RL").
- The "noisy-TV problem" is a complementary empirical failure mode: prediction-error intrinsic rewards (e.g., ICM) can fixate on inherently unpredictable but task-irrelevant stimuli [Ladosz et al., Exploration in Deep RL Survey](https://www.sciencedirect.com/science/article/abs/pii/S1566253522000288 "2022 Information Fusion survey").
- ICM (Pathak et al. 2017) formulates curiosity as the prediction error of action consequences in a self-supervised feature space, enabling exploration in VizDoom and Super Mario Bros under sparse reward [Pathak et al., Curiosity-driven Exploration](https://arxiv.org/abs/1705.05363 "ICML 2017 ICM paper"). RND (Burda et al. 2018) defines the exploration bonus as the distillation error of a fixed random network, achieving first better-than-average human performance on Montezuma's Revenge without demonstrations [Burda et al., Exploration by Random Network Distillation](https://arxiv.org/abs/1810.12894 "ICLR 2019 RND paper").
- The CMDP framework (Altman 1999) extends MDPs with m cost functions c^{(i)} and thresholds d_i, optimizing max_π J(π) s.t. J_{c^{(i)}}(π) ≤ d_i. Strong Lagrange duality holds under mild conditions, enabling the penalized-reward approach r_λ = r − Σ_i λ_i c^{(i)} that underpins CPO, RCPO, and PID-Lagrangian methods [Ravish et al., Safe RL and CMDPs Survey](https://arxiv.org/html/2505.17342v1 "2025 survey formalizing CMDPs after Altman 1999").
- Wachi, Shen, and Sui (IJCAI 2024) identify seven constraint formulations in safe RL across two families: expectation-based (cumulative cost, state indicator, joint chance, instantaneous) and almost-sure (cumulative, instantaneous time-invariant, generalized safe exploration with time-variant thresholds), proving that two formulations (expected instantaneous and almost-sure instantaneous with time-variant thresholds) are IoMG-SafeRL problems subsuming the others [Wachi et al., Constraint Formulations in Safe RL](https://www.ijcai.org/proceedings/2024/0913.pdf "IJCAI 2024 survey on constraint formulations").
- Zhao et al. (IJCAI 2023) identify an "inherent conflict between exploration for learning optimal RL policies and the need for safety." Safety filters distort reward signals intractably; gradually expanding safe regions highly limit reward exploration. An explicit trade-off exists: strong-guarantee methods (control barrier functions) require significant prior knowledge and restrict exploration; weaker-assumption methods (Lagrangian) explore more broadly but lose formal safety guarantees [Zhao et al., State-wise Safe RL Survey](https://www.ijcai.org/proceedings/2023/0763.pdf "IJCAI 2023 survey on state-wise safe RL from CMU").
- Trajectory planning in robotics, autonomous driving, and UAV navigation naturally exhibits both sparse rewards and hard safety constraints. Robotic manipulation receives reward only upon task completion while requiring joint torque limits ‖τ_t‖ ≤ τ_max at every timestep [Ravish et al.](https://arxiv.org/html/2505.17342v1 "2025 survey, Section 3.3"). Autonomous driving has sparse destination-arrival reward with instantaneous collision avoidance distance(s_t) ≥ d_safe [Kiran et al., Deep RL for Autonomous Driving](https://arxiv.org/abs/2002.00444 "IEEE TITS 2021 survey"). UAV trajectory optimization faces 3-D continuous action spaces, energy constraints, and dynamic obstacle fields with altitude corridor restrictions [Shi et al., Trajectory Planning for UAVs](https://www.sciencedirect.com/science/article/abs/pii/S0957417425042642 "Expert Systems with Applications, 2025").
- As of Q1 2026, the safe RL landscape features a proliferation of open-source benchmarks—Safety Gymnasium, OmniSafe (PKU-Alignment), FSRL/OSRL—and growing emphasis on during-training safety guarantees rather than convergence-only guarantees [Wachi et al.](https://www.ijcai.org/proceedings/2024/0913.pdf "IJCAI 2024 survey, Table 1").

### 可用图片
None found relevant in `/data/` or `/assets/`.

### 仍需补充
- A verified direct citation from Altman (1999) *Constrained Markov Decision Processes* (CRC Press) for the original CMDP definition and strong duality theorem; current citations use proxy surveys.
- Empirical data on sample-complexity ratios between sparse-reward and dense-reward settings from a canonical benchmark (e.g., Montezuma's Revenge, MiniGrid-MultiRoom) to quantify the exploration challenge magnitude beyond theoretical bounds.
- A recent (2025–2026) paper that explicitly unifies the sparse-reward exploration problem with the constrained RL problem in a single formal framework.
- Quantitative bibliometric data on the fraction of RL-based trajectory planning papers employing sparse vs. dense reward formulations.
- The Garcia and Fernandez (2015) JMLR survey "A Comprehensive Survey on Safe Reinforcement Learning" for historical grounding on the four safety criteria.


## Chapter 2：Exploration Under Sparse Rewards — Intrinsic Motivation, Curiosity, and Count-Based Methods

### 研究目标
- Survey recent advances (Apr 2025 – Mar 2026) in exploration strategies overcoming sparse extrinsic rewards
- Cover intrinsic motivation / curiosity-driven methods (prediction-error bonuses, RND variants, information-gain), count-based / pseudo-count exploration, reward-free / task-agnostic exploration, goal-conditioned / hindsight methods
- Organize methods by core mechanism; analyze comparative strengths, limitations, and computational overhead
- Assess scalability to high-dimensional state spaces and robustness to the "noisy-TV" problem
- Identify unifying frameworks or taxonomies reconciling different intrinsic motivation approaches

### 关键发现

**Intrinsic Motivation & Curiosity-Driven Methods**
- Learning Progress Monitoring (LPM) addresses the noisy-TV problem by rewarding model *improvement* rather than prediction error. A dual-network design yields intrinsic reward that is zero-equivariant and a monotone indicator of information gain. LPM outperforms RND and ICM on MNIST-noise, 3D mazes (160×120 RGB), and Atari in state coverage and extrinsic reward [LPM at ICLR 2026](https://openreview.net/forum?id=wzm38DRLhC "Beyond Noisy-TVs: Noise-Robust Exploration Via Learning Progress Monitoring, ICLR 2026").
- Hyper (ICML 2025) solves the hyperparameter sensitivity problem for curiosity-based exploration by regularizing visitation distributions and decoupling exploitation, with provable efficiency guarantees under function approximation and empirical robustness without environment-specific tuning [Hyper at ICML 2025](https://icml.cc/virtual/2025/poster/44124 "Hyperparameter Robust Efficient Exploration in RL, ICML 2025").
- CERMIC (NeurIPS 2025) extends curiosity to multi-agent RL with sparse rewards, enabling agents to calibrate intrinsic curiosity using inferred peer-behavior context without explicit communication. Outperforms SOTA MARL exploration on VMAS, Meltingpot, and SMACv2 [CERMIC at NeurIPS 2025](https://openreview.net/forum?id=1fOGTbO5Sx "Curiosity-Driven Exploration through Multi-Agent Contextual Calibration, NeurIPS 2025").
- Temporal Contrastive Representations (ICLR 2026) guide exploration by prioritizing states with unpredictable future outcomes, achieving complex exploratory behaviors (locomotion gaits, object manipulation) without extrinsic rewards on locomotion, manipulation, and embodied-AI tasks [Temporal Representations at ICLR 2026](https://openreview.net/forum?id=KjYpHySlb0 "Temporal Representations for Exploration, ICLR 2026").
- Graph-Theoretic Intrinsic Reward via Effective Resistance (ICLR 2026) uses spectral graph theory to guide agents toward goal-correlated configurations, with theoretical convergence guarantees and up to 59% success rate improvement and 56% timestep reduction vs. SOTA baselines [Graph-Theoretic IR at ICLR 2026](https://iclr.cc/virtual/2026/poster/10009071 "Graph-Theoretic Intrinsic Reward: Guiding RL with Effective Resistance, ICLR 2026").
- KEA (ICML 2025) coordinates a novelty-augmented SAC agent with a standard SAC agent via proactive switching: bold random moves in high-novelty regions, refined actions in familiar regions. Significant improvements on DeepSea hard-exploration and sparse-reward DMC tasks [KEA at ICML 2025](https://icml.cc/virtual/2025/poster/44965 "KEA: Keeping Exploration Alive, ICML 2025").
- VIB-IG (2025) grounds intrinsic motivation in the Information Bottleneck principle, defining rewards as pointwise mutual information estimated via MINE. On TSP-50/100/200 and SDVRP benchmarks, reduces average tour length on TSP-200 from 11.15 (Attention Model) to 10.82 [VIB-IG](https://pmc.ncbi.nlm.nih.gov/articles/PMC12939797/ "Information-Theoretic Intrinsic Motivation for RL in Combinatorial Routing, 2025").
- OMBRL (ICLR 2025 Workshop) achieves scalable optimism-based exploration for model-based RL with sublinear regret guarantees for nonlinear dynamics, validated on visual control tasks and a hardware RC car [OMBRL at ICLR 2025 Workshop](https://openreview.net/forum?id=VGdqa79ugx "Optimism via Intrinsic Rewards for Model-based RL, ICLR 2025 Workshop").
- Strategy-aware Surprise (SuS, arXiv Jan 2026) decomposes surprise into Strategy Stability and Strategy Surprise, achieving 17.4% Pass@1 and 26.4% Pass@5 improvements over baselines on mathematical reasoning with LLMs [SuS on arXiv](https://arxiv.org/abs/2601.10349 "SuS: Strategy-aware Surprise for Intrinsic Exploration, Jan 2026").

**Count-Based & Pseudo-Count Exploration**
- Kayal et al. (2025) show State Count leads to best exploration in low-dimensional observations but degrades severely under high-dimensional RGB (SimHash failure), while Maximum Entropy proves most robust under RGB. DIAYN (skill-level) does not promote effective exploration in structured grid environments [Kayal et al. 2025](https://link.springer.com/article/10.1007/s00521-025-11340-0 "Impact of intrinsic rewards on exploration in RL, Neural Computing and Applications, 2025").
- SIERL (arXiv Feb 2026) uses frontier-based sub-goal selection prioritized via cost-to-come and cost-to-go Q-value estimates, outperforming novelty-bonus baselines and HER on MiniGrid variants. Currently limited to discrete state-action spaces [SIERL on arXiv](https://arxiv.org/html/2602.00460v1 "Search Inspired Exploration in RL, Feb 2026").

**Reward-Free / Task-Agnostic Exploration**
- Ridel & Cohen (ICML 2026) establish the tight minimax lower bound Ω(|S|²|A|H³/ε²) for reward-free exploration in time-inhomogeneous episodic MDPs, resolving an open conjecture, and achieve optimal high-order sample complexity Õ(|S||A|H³/ε²) with reduced low-order terms [Ridel & Cohen at ICML 2026](https://arxiv.org/html/2602.16363v1 "Improved Bounds for Reward-Agnostic and Reward-Free Exploration, ICML 2026").
- SUPE (ICML 2025) leverages unlabeled offline trajectory data for online exploration via VAE skill extraction and optimistic pseudo-labeling, consistently outperforming prior strategies across 42 long-horizon sparse-reward robotic tasks [SUPE at ICML 2025](https://icml.cc/virtual/2025/poster/43987 "Skills from Unlabeled Prior Data for Exploration, ICML 2025").
- SODP (ICML 2025) pretrains a diffusion planner on sub-optimal multi-task trajectories, then fine-tunes with RL. Outperforms SOTA on Meta-World and Adroit with limited reward-guided fine-tuning data [SODP at ICML 2025](https://icml.cc/virtual/2025/poster/43821 "Task-Agnostic Pre-training and Task-Guided Fine-tuning for Versatile Diffusion Planner, ICML 2025").

**Goal-Conditioned & Hindsight-Based Methods**
- DISCOVER (NeurIPS 2025) extracts a "sense of direction" for directed goal selection toward the target task, with formal bounds on time-to-target independent of the full task space volume, solving problems beyond the reach of prior SOTA in high-dimensional long-horizon settings [DISCOVER at NeurIPS 2025](https://neurips.cc/virtual/2025/poster/116697 "Directed Sparse-Reward GCRL, NeurIPS 2025").
- TMD (NeurIPS 2025) unifies contrastive representations and quasimetric temporal distances for offline GCRL, combining Monte Carlo contrastive RL stability with quasimetric stitching capabilities [TMD at NeurIPS 2025](https://neurips.cc/virtual/2025/poster/118249 "Offline GCRL with Quasimetric Representations, NeurIPS 2025").
- OTA (NeurIPS 2025) addresses long-horizon GCRL via option-aware temporal abstraction that contracts effective horizon length, improving over HIQL on OGBench maze navigation and visual robotic manipulation [OTA at NeurIPS 2025](https://neurips.cc/virtual/2025/poster/116719 "Option-aware Temporally Abstracted Value for Offline GCRL, NeurIPS 2025").
- MSR (ICML 2025) solves the discontinuity problem in goal-achievement (success at 30° turn, failure at 30.1°) via margin-based policy self-regularization, evaluated on robotic arm and fixed-wing aircraft control [MSR at ICML 2025](https://icml.cc/virtual/2025/poster/43583 "Policy Self-Regularization for GCRL, ICML 2025").
- GOPlan (ICLR 2025) proposes model-based offline GCRL using advantage-weighted conditioned GAN and reanalysis planning, achieving SOTA on multi-goal navigation and manipulation with superior out-of-distribution goal generalization [GOPlan at ICLR 2025](https://iclr.cc/virtual/2025/poster/31488 "Goal-conditioned Offline RL by Planning with Learned Models, ICLR 2025").

**Unifying Frameworks**
- Kayal et al. (2025) propose a diversity-level taxonomy (State / State+Dynamics / Policy / Skill) that reveals markedly different exploration impacts per level and offers a more granular framework than the traditional "knowledge-based" vs. "competence-based" division [Kayal et al. 2025](https://link.springer.com/article/10.1007/s00521-025-11340-0 "Impact of intrinsic rewards on exploration in RL, 2025").
- OpenDILab Awesome Exploration RL repository (updated Dec 2025) serves as a community-maintained taxonomy by mechanism type: count-based, prediction-based, information-theoretic, skill-discovery, hybrid [OpenDILab](https://github.com/opendilab/awesome-exploration-rl "Community-maintained exploration RL collection, updated 2025.12.02").
- VIB-IG partially unifies exploration and representation learning under a single information-theoretic objective (IB principle), connecting count-based intuitions with information gain [VIB-IG](https://pmc.ncbi.nlm.nih.gov/articles/PMC12939797/ "2025").

### 可用图片
None found relevant in `/data/` or `/assets/`.

### 仍需补充
- No major new pseudo-count or hash-based method for continuous/image-based state spaces was identified in the survey period; the fragility of count-based methods under high-dimensional observations remains unresolved.
- No single dedicated survey covering all five sub-topics (intrinsic motivation, count-based, reward-free, goal-conditioned, unifying frameworks) published within April 2025 – March 2026 was found.
- Quantitative noisy-TV robustness comparisons among newer methods (temporal contrastive, graph-theoretic IR, Hyper) are lacking beyond LPM's direct demonstration.
- The improved reward-free bounds (Ridel & Cohen, ICML 2026) apply to tabular MDPs; scalable deep-RL instantiations with provable or strong empirical guarantees remain open.
- No fundamentally new HER relabeling strategy beyond MSR's policy self-regularization was identified; the sub-topic appears mature with incremental refinements.
- No single formal framework published in April 2025 – March 2026 comprehensively reconciles all intrinsic motivation families under one theoretical umbrella.


## Chapter 3：Foundation-Model-Guided and Hybrid Exploration Strategies for Sparse-Reward Settings

### 研究目标
- Focus on the use of LLMs and foundation models to guide RL exploration in sparse-reward environments
- Cover hybrid approaches combining multiple exploration signals (evolutionary + gradient, search-inspired, preference-based RL reward shaping)
- Identify key architectural patterns (hierarchical LLM programs, residual RL on top of FM policies, code-generation for policy initialization)
- Assess reported sample-efficiency gains and conditions under which FM-guided methods outperform/underperform classical intrinsic motivation
- Analyze limitations of FM-guided exploration (hallucination, domain mismatch, computational cost)

### 关键发现

**FM-Guided Exploration: LLM/VLM-Driven Reward Shaping & Sub-Goals**
- SENSEI (ICML 2025) distills VLM "interestingness" rewards via GPT-4 pairwise image annotations into a DreamerV3 world model, jointly maximizing semantic rewards and epistemic uncertainty via adaptive Go-Explore switching. On MiniHack KeyRoom, SENSEI solves the task in ~500K steps vs. >20M for PPO (~100× sample efficiency). An ablation shows VLM-Motif reward alone (without information gain) causes local-optima trapping, demonstrating FM guidance complements but cannot replace novelty-driven exploration [SENSEI at ICML 2025](https://arxiv.org/html/2503.01584v2 "Semantic Exploration Guided by Foundation Models, ICML 2025").
- STO-RL (arXiv Jan 2026) leverages LLMs (ChatGPT 5.0, Grok 3, DeepSeek-R1, Qwen3-Max) to decompose tasks into temporally ordered subgoal sequences with potential-based reward shaping (PBRS) for offline RL. Achieves 0.68 success rate on PointMaze-UMaze and 0.55 on Medium vs. near-zero for standard IQL with sparse rewards [STO-RL](https://arxiv.org/html/2601.08107v1 "Offline RL via LLM-Guided Subgoal Temporal Order, Jan 2026").
- RG-VLM (arXiv Apr 2025) uses LVLMs (Gemini 1.5 Pro, GPT-4, Qwen2-VL-72B) to generate dense reward labels from offline visual data. IQL with Sparse + RG-VLM reward achieves 1.12×–3.15× higher returns than other VLM-based methods (CLIP, BLIP2, RoboCLIP) on ALFRED tasks [RG-VLM](https://arxiv.org/html/2504.08772v1 "Reward Generation via Large Vision-Language Model in Offline RL, Apr 2025").
- VARL (arXiv Sep 2025) uses VLMs as action advisors rather than reward shapers, preserving RL optimality and convergence guarantees while increasing sample diversity and efficiency in sparse-reward tasks [VARL](https://arxiv.org/abs/2509.21126 "VLM as Action Advisor for Online RL, Sep 2025").
- VIRAL (arXiv May 2025) generates and iteratively refines reward functions through multi-modal LLMs, with human feedback or Video-LLM-based policy description, evaluated across five Gymnasium environments [VIRAL](https://arxiv.org/abs/2505.22092 "VIRAL: Vision-grounded Integration for Reward design And Learning, May 2025").
- LMGT (Knowledge-Based Systems, 2025) aligns LLM reward-shift with the theoretical principle of Q-function initialization modification, outperforming RUDDER on Housekeep embodied robotics and Google's SlateQ recommendation [LMGT](https://www.sciencedirect.com/science/article/abs/pii/S095070512500735X "LMGT: LLM-Guided reward Tuning, KBS 2025").
- Memory-Based Advantage Shaping (AAAI 2026) constructs a memory graph encoding subgoals/trajectories from offline LLM input and agent rollouts, shaping the advantage function (not reward) without altering optimal policy guarantees [Memory-Based Advantage Shaping](https://ojs.aaai.org/index.php/AAAI/article/view/42261 "AAAI 2026 Student Abstract").

**Architectural Patterns**
- LDSC (arXiv Mar 2025) proposes three-stage hierarchical RL: LLM-generated subgoals → reusable option learning → action-level execution, outperforming baselines by 55.9% in average reward [LDSC](https://arxiv.org/abs/2503.19007 "LLM-guided Semantic Hierarchical RL Option Discovery, Mar 2025").
- LLMs-augmented Hierarchical RL with Action Primitives (Nature Scientific Reports, 2025) combines LLM task decomposition with action primitives and hierarchical RL for long-horizon manipulation [LLMs-augmented HRL](https://www.nature.com/articles/s41598-025-20653-y "Scientific Reports, 2025").
- Residual Off-Policy RL (arXiv Sep 2025) learns lightweight per-step residual corrections on BC policies using only sparse binary rewards, including the first successful real-world RL training on a humanoid robot with dexterous hands [Residual Off-Policy RL](https://arxiv.org/abs/2509.19301 "Residual Off-Policy RL for Finetuning BC Policies, Sep 2025").
- Found-RL (arXiv Feb 2026) integrates VLMs into RL for autonomous driving via asynchronous batch inference (~500 FPS), Value-Margin Regularization, Advantage-Weighted Action Guidance, and CLIP-based dense reward addressing CLIP's dynamic blindness [Found-RL](https://arxiv.org/abs/2602.10458 "Foundation Model-Enhanced RL for Autonomous Driving, Feb 2026").

**Sample Efficiency: FM vs. Classical Intrinsic Motivation**
- Quadros et al. (ENIAC 2025) directly compare LLM rewards + VSIMR vs. either alone in MiniGrid DoorKey: the combined strategy significantly outperforms both, providing direct evidence that FM guidance and classical intrinsic motivation are complementary [LLM-Driven Intrinsic Motivation](https://arxiv.org/abs/2508.18420 "ENIAC 2025, Aug 2025").
- SENSEI ablations show ~100× sample efficiency over PPO but require the information-gain component; VLM guidance alone is insufficient.
- RG-VLM's reasoning-based reward generation outperforms embedding-similarity VLM methods (CLIP/BLIP2/RoboCLIP) by 1.12–3.15× on ALFRED.

**Hybrid Evolutionary-RL**
- LaRes (NeurIPS 2025) bridges evolutionary algorithms and RL via LLM-generated reward function populations with evolutionary search, shared experience buffers, and Thompson sampling. Achieves SOTA across initialized and non-initialized settings [LaRes at NeurIPS 2025](https://neurips.cc/virtual/2025/poster/116462 "LLM-based Reward Search for Evolutionary RL, NeurIPS 2025").
- Li et al. (IEEE TNNLS, 2024/2025) survey ERL approaches, identifying four categories: EA-assisted policy optimization, EA-assisted reward design, RL-assisted EA, and Quality-Diversity methods. Most focus on parameter-space rather than reward-function exploration [ERL Survey](https://arxiv.org/abs/2401.11963 "Bridging Evolutionary Algorithms and RL Survey, IEEE TNNLS").

**Preference-Based RL for Sparse Rewards**
- IMAP (arXiv Sep 2025) integrates inverse preference learning with multi-agent optimization for cooperative MARL with sparse rewards, learning implicit rewards from trajectory-level preferences [IMAP](https://arxiv.org/html/2509.21828v1 "Preference-Guided Learning for Sparse-Reward MARL, Sep 2025").
- Vakkapatla et al. (ICAART 2026) demonstrate that self-supervised sparse-to-preference conversion enables PbRL methods to substantially outperform sparse-reward SAC on MuJoCo. In Swimmer, learned reward functions surpass even ground-truth dense rewards [Sparse Rewards as Preferences](https://www.scitepress.org/Papers/2026/142216/142216.pdf "ICAART 2026").
- NeurIPS 2025 work on preference-based exploration addresses the exp(R) scaling problem in online RLHF, improving sample efficiency by avoiding exponential scaling with reward range [Preference-Based Exploration](https://neurips.cc/virtual/2025/poster/117857 "Avoiding exp(R) Scaling in RLHF, NeurIPS 2025").

**Limitations of FM-Guided Exploration**
- Hallucination/domain mismatch: LLMs can generate partially incorrect subgoal sequences due to environmental distractions (STO-RL ablation across 4 LLMs).
- Local optima: VLM rewards alone cause agents to hover near rewarding states without task completion (SENSEI ablation on MiniHack KeyChest).
- Computational latency: Found-RL's asynchronous framework addresses billion-parameter VLM inference latency, a first-order engineering concern.
- OOD degradation: Semantic rewards degrade as the agent explores beyond initial annotation distributions (SENSEI on Pokémon Red).
- Non-transferability: FM-guided policies are typically task-specific, not generalizing across domains (STO-RL).
- Reward noise: VLM-generated rewards benefit from grounding in sparse environmental success signals (RG-VLM: combined > VLM-only by 1.14×).

### 可用图片
None found relevant in `/data/` or `/assets/`.

### 仍需补充
- No comprehensive head-to-head benchmark comparison across multiple FM-guided and multiple classical intrinsic motivation methods on the same environments exists.
- No paper specifically combining quality-diversity evolutionary methods with sparse-reward exploration was identified in the survey period.
- No major paper from Apr 2025 – Mar 2026 uses LLM code generation specifically to initialize RL policies (as opposed to reward functions).
- FM-guided exploration evidence for high-dimensional continuous control (locomotion, dexterous manipulation) remains limited; most evaluations target grid worlds or structured environments.
- No formal sample-complexity or regret bounds for FM-guided exploration exist; all results are empirical.
- Multi-agent FM-guided exploration beyond IMAP's preference-based approach remains unexplored.


## Chapter 4：Exploration Under Constraints — Safe RL, Constrained MDPs, and Safety-Aware Exploration

### 研究目标
- Survey recent work (Apr 2025 – Mar 2026) on efficient exploration while respecting safety constraints
- Cover primal-dual / Lagrangian methods, CPO successors, trust-region approaches with embedded safety, safety critics / shielding, barrier-function and control-theoretic methods, off-policy safe RL with constrained optimistic exploration
- Distinguish methods guaranteeing constraint satisfaction during training vs. only at convergence
- Assess progress on safe exploration during training, including active safe exploration and probabilistic safety guarantees
- Examine interaction between offline/batch RL safety methods and online safe exploration
- Identify open problems: scalability to high-dimensional constraints, multi-constraint settings, non-stationary constraints

### 关键发现

**Primal-Dual / Lagrangian Methods**
- PLO (Jan 2025) establishes a generic equivalence between constrained optimization and feedback control, showing PID-Lagrangian as a special case. Using MPC for multiplier updates, PLO achieves a feasible region up to 7.2% larger than PID-Lagrangian while maintaining comparable reward [PLO](https://arxiv.org/abs/2501.15217 "Predictive Lagrangian Optimization for Constrained RL, Jan 2025").
- Utke et al. (NeurIPS 2025) reformulate constrained RL as a linear program over state–action occupancy measures, enabling convex optimization of returns subject to linear constraints with greater robustness to hyperparameters than standard Lagrangian baselines [Safe RL via LP](https://neurips.cc/virtual/2025/133789 "NeurIPS 2025 — Safe RL via LP Formulation").
- Seo and Choi (Oct 2025) introduce state-dependent Lagrange multipliers to enforce point-wise (instantaneous) safety constraints rather than only expected cumulative cost limits [State-Dependent Lagrange](https://www.techrxiv.org/doi/full/10.36227/techrxiv.175979326.64150311 "State-wise Safety via State-Dependent Lagrange Multipliers, Oct 2025").

**CPO Successors & Trust-Region Methods**
- C-TRPO (ICML 2025) reshapes trust regions to contain only safe policies, guaranteeing constraint satisfaction throughout training with formal connections to TRPO, NPG, and CPO [C-TRPO](https://icml.cc/virtual/2025/poster/46451 "ICML 2025 — Embedding Safety via Trust Region Methods").
- sTRPO (NeurIPS 2025) learns an auxiliary unsafe policy to estimate high-risk regions and explicitly excludes them from trust-region updates, achieving monotonic improvement in both reward and safety. Outperforms seven SOTA baselines on Safety-Gymnasium [sTRPO](https://neurips.cc/virtual/2025/136134 "NeurIPS 2025 — Safe Trust Region Policy Optimization").
- SB-TRPO biases each TRPO step toward the feasible region, targeting hard-constraint satisfaction in CMDPs [SB-TRPO](https://openreview.net/forum?id=4zRb89SbzG "Hard-Constrained RL via Trust Regions").

**Safety Critics, Shielding & Chance-Constrained Methods**
- MAXSAFE (ICML 2025) uses chance-constrained bi-level optimization with safety polarization and safety-prioritized experience replay to handle sparse cost signals. Near-maximal safety on autonomous driving and safe control tasks [MAXSAFE](https://icml.cc/virtual/2025/poster/43599 "ICML 2025 — Safety-Polarized and Prioritized RL").
- Probabilistic Shielding (AAAI 2025) introduces scalable state-augmentation shields with strict formal safety guarantees at both training and test time, when safety dynamics are known [Probabilistic Shielding](https://ojs.aaai.org/index.php/AAAI/article/view/33767 "AAAI 2025 — Probabilistic Shielding for Safe RL").
- MICE (ICML 2025) identifies cost value function underestimation as a key driver of training-time violations and constructs flashbulb-memory modules of unsafe states with worst-case violation bounds tighter than baselines [MICE](https://icml.cc/virtual/2025/poster/44096 "ICML 2025 — Controlling Underestimation Bias in Constrained RL").

**Barrier-Function & Control-Theoretic Approaches**
- CBF-RL (Oct 2025) embeds Control Barrier Functions directly into RL training (not just runtime filters), enabling safe deployment on a Unitree G1 humanoid robot without a runtime safety filter [CBF-RL](https://arxiv.org/abs/2510.14959 "CBF-RL: Safety Filtering RL in Training, Oct 2025").
- RLBUS (L4DC 2025) integrates Backup Control Barrier Functions with model-free RL to guarantee zero training-time safety violations while enlarging the forward-invariant safe set for broader exploration [RLBUS](https://proceedings.mlr.press/v283/rabiee25a.html "L4DC 2025 — Safe Exploration via Backup CBFs").
- HMARL-CBF (NeurIPS 2025) hierarchically coordinates multi-agent RL with CBFs, achieving near-perfect (within 5%) success/safety rates on multi-agent road-network navigation [HMARL-CBF](https://neurips.cc/virtual/2025/poster/116828 "NeurIPS 2025 — Hierarchical Multi-Agent RL with CBFs").
- Adaptive Safety-Certified RL (IEEE, 2025) decouples safety and RL convergence via a high-order robust adaptive CBF with prescribed-time adaptation under parametric uncertainties [Adaptive Safety-Certified RL](https://ieeexplore.ieee.org/document/10947350/ "IEEE 2025 — Adaptive Safety-Certified RL with CBFs").
- Kushwaha and Biron (Aug 2025) survey Lyapunov/barrier-based safe RL in four categories: Lyapunov-based reward shaping, CLF-RL-QP, candidate Lyapunov as value function, and CLF-based loss. Open challenges include conservatism-performance tradeoffs and scalability [Lyapunov-Barrier Review](https://arxiv.org/html/2508.09128v1 "Review on Safe RL Using Lyapunov and Barrier Functions, Aug 2025").

**Off-Policy Safe RL with Constrained Optimistic Exploration**
- COX-Q (ICLR 2026) addresses cost-agnostic exploration and underestimation bias in off-policy safe RL via cost-constrained optimistic exploration, gradient-conflict resolution, adaptive trust regions, and truncated quantile critics. High sample efficiency on safe velocity, navigation, and autonomous driving tasks [COX-Q](https://iclr.cc/virtual/2026/poster/10010695 "ICLR 2026 — Off-Policy Safe RL with Constrained Optimistic Exploration").

**Safe Exploration During Training**
- NeurIPS 2025 work establishes near-optimal sample complexity for online CMDPs: Õ(SAH³/ε²) for relaxed feasibility (matching unconstrained lower bound) and Õ(SAH⁵/(ε²ζ²)) for strict feasibility where ζ is the Slater constant [Near-Optimal CMDP](https://neurips.cc/virtual/2025/poster/116370 "NeurIPS 2025 — Near-Optimal Sample Complexity for Online CMDPs").
- Efficient Action-Constrained RL (ICLR 2025) uses acceptance-rejection on the unconstrained policy and an augmented two-objective MDP to improve acceptance rates, achieving faster training and lower action inference time [Action-Constrained RL](https://iclr.cc/virtual/2025/poster/30623 "ICLR 2025 — Efficient Action-Constrained RL").
- SCARED (Sep 2025) proposes the first method promoting safety during in-context RL's parameter-update-free adaptation within the CMDP framework, actively adjusting aggressiveness based on cost budget [Safe ICRL](https://arxiv.org/abs/2509.25582 "Safe In-Context RL, Sep 2025").

**Offline/Batch RL Safety**
- O3SRL (NeurIPS 2025) frames offline safe RL as minimax optimization, combining offline RL with online optimization, with proven approximate optimality and reliable safety enforcement on DSRL benchmarks [O3SRL](https://neurips.cc/virtual/2025/poster/116952 "NeurIPS 2025 — Online Optimization for Offline Safe RL").
- TraC (AAAI 2025) partitions trajectories into desirable/undesirable subsets using classifier-based scoring, bypassing min-max instability [TraC](https://ojs.aaai.org/index.php/AAAI/article/view/33855 "AAAI 2025 — Offline Safe RL via Trajectory Classification").
- CAPS (AAAI 2025) learns multiple policies with shared representations and switches at deployment based on varying cost constraints without retraining, outperforming baselines on 38 DSRL tasks [CAPS](https://ojs.aaai.org/index.php/AAAI/article/view/33726 "AAAI 2025 — Constraint-Adaptive Policy Switching").

**Constraint Inference**
- PbCRL (Mar 2026) infers unknown safety constraints from human preferences, introducing dead-zone preference modeling and SNR loss for cost-variance-based exploration to address Bradley-Terry risk underestimation [PbCRL](https://arxiv.org/abs/2603.23565 "Preference-based Constrained RL, Mar 2026").
- Inverse Constrained RL (ICML 2025) proposes strategic exploration for recovering constraints from expert demonstrations with tractable sample complexity bounds [Inverse Constrained RL](https://icml.cc/virtual/2025/poster/44588 "ICML 2025 — Provably Efficient Exploration in Inverse Constrained RL").

### 可用图片
None found relevant in `/data/` or `/assets/`.

### 仍需补充
- Specific new Lyapunov-based algorithmic contributions beyond CLF-CBF-QP formulations in the survey period need deeper coverage.
- Limited coverage of methods explicitly designed for many (>2) simultaneous safety constraints.
- No paper targeting time-varying or non-stationary safety constraints in RL was found in the survey period; this is a genuine open problem.
- Systematic comparison across all algorithmic families (Lagrangian, trust-region, CBF, distributional) on the same benchmark suite within the survey period is lacking.
- Most validated results remain on relatively low-dimensional tasks; broader high-dimensional continuous control validation (beyond CBF-RL on Unitree G1) is sparse.
- Explicit methods for safely bridging offline-to-online transitions under constraints need further investigation.


## Chapter 5：Implications for Trajectory Planning — Bridging RL Exploration Advances and Real-World Path Planning

### 研究目标
- Analytical/integrative chapter examining how exploration advances from Chapters 2–4 translate to trajectory planning across three domains: (a) robotic manipulator/mobile-robot path planning, (b) autonomous driving motion planning, (c) UAV/drone trajectory optimization
- For each domain, discuss which RL exploration innovations are most applicable, required domain-specific adaptations, and remaining gaps
- Analyze recurring patterns where combining sparse-reward exploration with safety constraints yields synergistic or antagonistic effects
- Assess practical deployment barriers: sim-to-real transfer, verification & validation, regulatory acceptance

### 关键发现

**Robotic Manipulator & Mobile-Robot Path Planning**
- SUPE (ICML 2025) extracts skills from unlabeled data and outperforms prior strategies across 42 long-horizon sparse-reward robotic tasks, demonstrating skill-based decomposition as effective for managing joint-space dimensionality [SUPE](https://proceedings.mlr.press/v267/wilcoxson25a.html "Skills from Unlabeled Prior Data for Exploration, ICML 2025").
- Residual Off-Policy RL (Sep 2025) achieves the first real-world RL training on a humanoid robot with dexterous hands using sparse binary rewards, establishing the residual-on-BC architecture as the dominant pattern for high-dimensional contact-rich planning [Residual Off-Policy RL](https://arxiv.org/abs/2509.19301 "Residual RL for Finetuning BC Policies, Sep 2025").
- RFS (arXiv Feb 2026) adapts pretrained flow-matching generative policies for dexterous manipulation via joint residual action and latent noise optimization, enabling complementary local/global exploration [RFS](https://arxiv.org/abs/2602.01789 "Residual Flow Steering for Dexterous Manipulation, Feb 2026").
- ManipTrans (CVPR 2025) applies residual learning on imitation models for bimanual manipulation at 52 DoF, demonstrating the architecture scales to the most challenging dexterous scenarios [ManipTrans](https://arxiv.org/abs/2503.21860 "Dexterous Bimanual Manipulation Transfer via Residual Learning, CVPR 2025").
- CBF-RL (Oct 2025) embeds CBFs during training for safe robotic navigation on Unitree G1 humanoid, eliminating runtime safety filters [CBF-RL](https://arxiv.org/abs/2510.14959 "CBF-RL: Safety Filtering RL in Training, Oct 2025").
- Temporal Contrastive Representations (ICLR 2026) discover manipulation-relevant locomotion gaits and object interaction behaviors without extrinsic rewards [Temporal Representations](https://openreview.net/forum?id=KjYpHySlb0 "ICLR 2026").
- SR2 (IJCAI 2025) uses a meta-policy to revisit high-quality states from offline data for targeted online re-exploration, bridging sim-to-real gaps in robotic skill acquisition [SR2](https://www.ijcai.org/proceedings/2025/970 "State Revisit and Re-explore, IJCAI 2025").

**Autonomous Driving Motion Planning**
- CarPlanner (CVPR 2025) is the first RL planner to surpass both imitation learning and rule-based SOTA on the large-scale nuPlan benchmark, using consistent auto-regressive trajectory generation with expert-guided rewards [CarPlanner](https://arxiv.org/abs/2502.19908 "Consistent Auto-regressive Trajectory Planning for Large-scale RL, CVPR 2025").
- Plan-R1 (arXiv May 2025) decouples principle alignment from behavior learning via Variance-Decoupled GRPO (VD-GRPO), preserving absolute reward magnitudes for rare safety-critical objectives. Achieves SOTA planning safety on nuPlan [Plan-R1](https://arxiv.org/abs/2505.17659 "Safe and Feasible Trajectory Planning as Language Modeling, May 2025").
- Found-RL (arXiv Feb 2026) integrates VLMs into RL for driving at ~500 FPS via asynchronous batch inference, VMR, AWAG, and CLIP-based dense reward with dynamic-blindness correction [Found-RL](https://arxiv.org/abs/2602.10458 "Foundation Model-Enhanced RL for Autonomous Driving, Feb 2026").
- COX-Q (ICLR 2026) resolves gradient conflicts between reward and cost via cost-constrained optimistic exploration with truncated quantile critics for safe driving trajectories [COX-Q](https://iclr.cc/virtual/2026/poster/10010695 "Off-Policy Safe RL with Constrained Optimistic Exploration, ICLR 2026").
- MAXSAFE (ICML 2025) achieves near-maximal safety on driving benchmarks via chance-constrained bi-level optimization with safety polarization [MAXSAFE](https://icml.cc/virtual/2025/poster/43599 "ICML 2025").
- HMARL-CBF (NeurIPS 2025) achieves near-perfect (within 5%) success/safety on multi-agent road navigation via hierarchical RL + CBFs [HMARL-CBF](https://neurips.cc/virtual/2025/poster/116828 "NeurIPS 2025").
- C-TRPO (ICML 2025) and sTRPO (NeurIPS 2025) guarantee constraint satisfaction during training, directly applicable to driving planners needing safety throughout learning [C-TRPO](https://icml.cc/virtual/2025/poster/46451 "ICML 2025"); [sTRPO](https://neurips.cc/virtual/2025/136134 "NeurIPS 2025").

**UAV/Drone Trajectory Optimization**
- Xiong et al. (Communications Engineering, 2025) present an RL drone landing planner validated on a physical quadrotor in 5 m/s wind, balancing safety, energy, and smoothness. Velocity sensing is critical (94% failure without it), while wind sensing is less important for local planning [Xiong et al.](https://www.nature.com/articles/s44172-025-00531-1 "Trajectory planning for drone landing with RL, Communications Engineering, 2025").
- Entropy Explorer (Meas. Sci. Technol., 2024) generates intrinsic rewards combining state entropy and action entropy for UAV path planning in sparse-reward 3-D environments [Entropy Explorer](https://iopscience.iop.org/article/10.1088/1361-6501/ad2663 "Entropy-based exploration for UAV path planning, 2024").
- Afzal et al. (Drones, June 2025) find DDPG and MADDPG outperform PPO/SAC/TRPO in multi-UAV path efficiency; 2D→3D transition introduces severe challenges from expanded state-action spaces (54-dim observation) [Afzal et al.](https://www.mdpi.com/2504-446X/9/6/438 "Comparative RL for Multi-Agent UAV Path Planning, Drones, 2025").
- 3D RVO-Enhanced MARL (Aerospace Sci. Technol., 2025) combines Reciprocal Velocity Obstacles with deep RL for multi-UAV conflict resolution under energy constraints, using geometric priors to constrain exploration [3D RVO-MARL](https://www.sciencedirect.com/science/article/abs/pii/S1270963825004493 "Multi-UAV conflict resolution, 2025").
- Energy exhaustion in UAVs causes crashes (unlike ground robots), making energy a uniquely hard constraint requiring CMDP formulations or implicit penalty-based reward design.

**Cross-Domain Patterns**
- Residual RL emerges as the dominant architecture for trajectory planning under sparse rewards across robotics domains, constraining exploration to a residual manifold around competent base policies and naturally limiting safety-violating deviations.
- FM-guided exploration + classical intrinsic motivation are complementary across domains: VLM-only or curiosity-only approaches underperform combined strategies (SENSEI, Found-RL, LDSC all demonstrate this pattern).
- CBF integration is migrating from post-hoc runtime filter to training-time constraint: CBF-RL, HMARL-CBF, and RLBUS demonstrate this cross-domain trend. CBFs constrain exploration space (potentially antagonistic) but focus exploration within safe regions (synergistic with sample efficiency).
- Sparse rewards + safety constraints are theoretically antagonistic but practically manageable via: MICE (memory-based intrinsic cost bridging sparse cost), COX-Q (gradient conflict resolution), hierarchical decomposition (safety at lower level, exploration at higher level).
- Goal-conditioned RL (DISCOVER, GOPlan, TMD, OTA) maps naturally to start-goal trajectory planning; graph-theoretic IR (ICLR 2026) with 59% success rate improvement suggests graph-based bonuses are effective for structured environments.

**Deployment Barriers**
- Da et al. (Feb 2025) present the first comprehensive sim-to-real taxonomy through MDP elements (State/Action/Transition/Reward gaps), identifying foundation models as increasingly bridging these gaps via zero-shot transfer and semantic grounding [Da et al.](https://arxiv.org/abs/2502.13187 "Sim-to-Real Survey with Foundation Models, Feb 2025").
- Lin and Sun (Jun 2025) reveal MBRL faces worse sim-to-real challenges than model-free approaches because planning amplifies transition-model errors [Lin & Sun](https://arxiv.org/abs/2506.12735 "Sim-to-Real Challenges in MBRL, Jun 2025").
- SR2 (IJCAI 2025) addresses sim-to-real by targeted re-exploration of high-quality offline states in imperfect simulators [SR2](https://www.ijcai.org/proceedings/2025/970 "IJCAI 2025").
- Marchesini et al. (ACM TIST, 2025) integrate formal verification of neural network safety properties during RL training via violation-value sample-based verification with probabilistic guarantees, demonstrated on real-world robotic navigation [Marchesini et al.](https://dl.acm.org/doi/10.1145/3770068 "Verifying Online Safety for Safe Deep RL, ACM TIST, 2025").
- Le et al. (ECAI 2025) propose hybrid verification-guided falsification with PAC-style guarantees and lightweight safety shields for runtime fallback [Verification-Guided Falsification](https://arxiv.org/abs/2506.03469 "ECAI 2025").
- RLQP (SERC/DEVCOM AC, Sep 2025) proposes a 7-stage V-model framework for qualifying RL agents in safety-critical applications, finding drone navigation success drops from 100% to 55% under heavy wind, restored to 95% with curriculum learning [RLQP](https://sercuarc.org/wp-content/uploads/2025/09/Senczyszyn_Reinforcement_Learning_Qualification_Process.pdf "RL Qualification Process, Sep 2025").
- Regulatory acceptance remains the least developed barrier: no regulatory framework specifically accepting RL-based trajectory planners exists. Current frameworks (DO-178C, ISO 26262) assume deterministic or well-characterized stochastic systems incompatible with opaque neural policies.

### 可用图片
None found relevant in `/data/` or `/assets/`.

### 仍需补充
- Quantitative sim-to-real performance degradation data for trajectory planning (specific sim-vs-real success rate comparisons) is sparse; most papers discuss qualitatively.
- No published regulatory guidance specifically addressing RL-based trajectory planners was identified.
- No systematic comparison of exploration methods (curiosity vs. goal-conditioned vs. FM-guided) on standardized trajectory planning benchmarks exists.
- No paper provides formal energy constraint satisfaction guarantees (vs. expected cost bounds) for UAV trajectory planning.
- Limited coverage of multi-constraint safe RL handling >2 simultaneous constraints in a single trajectory planning formulation.


## Chapter 6：Synthesis, Open Challenges, and Forward-Looking Outlook

### 研究目标
- Synthesize cross-cutting themes from Chapters 1–5
- Identify 3–5 most impactful methodological advances from the survey period and explain why
- Analyze intersections and tensions between sparse-reward exploration and constrained RL (exploration breadth vs. constraint conservatism)
- Assess the expanding role of foundation models in both exploration guidance and safety specification for trajectory planning
- Identify most critical gaps for the research community to prioritize in the next 6 months (Apr – Sep 2026)
- Evaluate signs of convergence toward unified frameworks handling sparse rewards and constraints simultaneously

### 关键发现

**Top 5 Most Impactful Advances**
- Training-time safety guarantees matching unconstrained sample complexity: C-TRPO (ICML 2025) + sTRPO (NeurIPS 2025) + near-optimal CMDP sample complexity Õ(SAH³/ε²) (NeurIPS 2025) collectively close the gap, proving safe RL during training is no harder than unconstrained RL in the tabular/linear regime [C-TRPO](https://icml.cc/virtual/2025/poster/46451 "ICML 2025"); [Near-Optimal CMDP](https://neurips.cc/virtual/2025/poster/116370 "NeurIPS 2025").
- Residual RL as dominant real-world deployment architecture: first humanoid RL with sparse binary rewards (Sep 2025), RFS for dexterous manipulation (Feb 2026), ManipTrans at 52 DoF (CVPR 2025), CarPlanner beating IL+rule-based SOTA on nuPlan (CVPR 2025) [Residual Off-Policy RL](https://arxiv.org/abs/2509.19301 "Sep 2025"); [CarPlanner](https://arxiv.org/abs/2502.19908 "CVPR 2025").
- Noise-robust intrinsic motivation: LPM (ICLR 2026) proves zero-equivariant information-gain-monotone intrinsic reward, solving the noisy-TV problem theoretically. Complemented by Hyper (ICML 2025) for hyperparameter robustness and CERMIC (NeurIPS 2025) for multi-agent calibration [LPM](https://openreview.net/forum?id=wzm38DRLhC "ICLR 2026").
- FM-guided exploration at ~100× sample efficiency, but only when combined with classical intrinsic motivation: SENSEI (ICML 2025) VLM-only → local optima; combined VLM + information gain → ~100× over PPO. Pattern replicated by Found-RL (~500 FPS driving), LLM-Driven Intrinsic Motivation (ENIAC 2025) [SENSEI](https://arxiv.org/html/2503.01584v2 "ICML 2025"); [Found-RL](https://arxiv.org/abs/2602.10458 "Feb 2026").
- Tight minimax bounds Ω(|S|²|A|H³/ε²) for reward-free exploration (ICML 2026) resolving an open conjecture, plus graph-theoretic intrinsic reward via effective resistance with 59% success rate improvement and convergence guarantees (ICLR 2026) [Ridel & Cohen](https://arxiv.org/html/2602.16363v1 "ICML 2026"); [Graph-Theoretic IR](https://iclr.cc/virtual/2026/poster/10009071 "ICLR 2026").

**Sparse-Reward × Safe RL Intersections**
- Productive: Hierarchical decomposition (SOOPER, NeurIPS 2025, ETH Zürich) unifies pessimistic safety priors and optimistic planning in a single objective, proving safe exploration with sublinear regret, validated on a real-world 60 Hz race car [SOOPER](https://arxiv.org/html/2601.19612v1 "Safe Exploration via Policy Priors, NeurIPS 2025").
- Productive: MICE (ICML 2025) parallels intrinsic reward with intrinsic cost—memory-based estimation bridges sparse cost signals just as curiosity bridges sparse rewards, suggesting a unified dual-memory architecture [MICE](https://icml.cc/virtual/2025/poster/44096 "ICML 2025").
- Productive: COX-Q (ICLR 2026) resolves gradient conflicts between reward maximization and cost minimization via cost-constrained optimistic exploration with truncated quantile critics [COX-Q](https://iclr.cc/virtual/2026/poster/10010695 "ICLR 2026").
- Tension: No unified theoretical framework characterizes the optimal exploration-safety tradeoff. State-wise constraints restrict exploration to known-safe sets. SOOPER provides the closest analysis but relies on epistemic uncertainty shrinking with data—slow in high-dimensional spaces.
- Tension: Multi-constraint settings remain under-addressed; GradS (L4DC 2024) and multi-constraint CBF (L4DC 2025) are initial steps [GradS](https://proceedings.mlr.press/v242/yao24a/yao24a.pdf "L4DC 2024"); [Multi-Constraint CBF](https://arxiv.org/abs/2505.00671 "L4DC 2025").

**Foundation Model Role Outlook**
- "Training-only FM" paradigm consolidating: VLM/LLM used during training, removed at deployment (Found-RL ~500 FPS, DriveVLM-RL Mar 2026, LMGT). Likely to become default architecture for FM-guided RL in trajectory planning [DriveVLM-RL](https://arxiv.org/abs/2603.18315 "Neuroscience-Inspired RL with VLMs for Safe Driving, Mar 2026").
- SafeVLA (NeurIPS 2025 Spotlight, PKU) establishes CMDP + VLA paradigm: first integration of safety constraints into Vision-Language-Action models, reducing cumulative safety violation cost by 83.58% vs. SOTA while maintaining task success (+3.85%) [SafeVLA](https://arxiv.org/abs/2503.03480 "Safety Alignment of VLA via Constrained Learning, NeurIPS 2025 Spotlight").
- Natural-language constraint specification emerging but unproven: DriveVLM-RL decomposes semantic rewards into spatial safety + temporal risk via VLM/CLIP; PbCRL explores preference-based constraint inference. No provably correct safety constraint extraction from language yet.
- Silver and Sutton's "Era of Experience" vision (DeepMind, Apr 2025) reinforces FM-RL convergence: FM priors accelerate early learning, RL experience overcomes FM limitations (hallucination, local optima) [Silver & Sutton](https://theaiinnovator.com/welcome-to-the-era-of-experience/ "Era of Experience, DeepMind, Apr 2025").

**Convergence Signals Toward Unified Frameworks**
- SOOPER unifies safe exploration, optimistic planning, and pessimistic safety priors in a single objective with provable safety and sublinear regret on real hardware [SOOPER](https://arxiv.org/html/2601.19612v1 "NeurIPS 2025").
- CBF integration migrating from runtime to training-time across domains (CBF-RL, HMARL-CBF, multi-constraint CBF), converging control theory and RL.
- SafeVLA demonstrates FM + CMDP convergence where the foundation model is both policy and subject of constrained optimization.
- Residual RL + safety constraints emerging as de facto unified architecture across humanoid manipulation, dexterous tasks, and driving.
- Dual memory-augmented estimation (intrinsic reward buffers for novel states + intrinsic cost buffers for unsafe states) as potential unified framework addressing both reward and cost sparsity.
- Preference-based methods unify reward specification and constraint inference via a common feedback modality (PbCRL + Sparse Rewards as Preferences).
- Gazi et al. (Harvard, Jan 2026) frame practical RL as a deployment-redeployment cycle of online learning, offline analysis, and continual improvement—directly applicable to iterative trajectory planner refinement [Gazi et al.](https://arxiv.org/html/2601.15353v1 "Statistical RL in the Real World, Jan 2026").

**Critical Gaps for Apr – Sep 2026**
- No unified theoretical framework for sample complexity under both sparse rewards and safety constraints simultaneously.
- Multi-constraint safe RL at scale (>2 constraints in high-dimensional continuous control) lacks empirical validation.
- No formal sample-complexity or regret bounds exist for FM-guided exploration.
- Sim-to-real transfer for safe RL planners lacks systematic quantification (RLQP reveals 100%→55% drone success under wind).
- No regulatory framework specifically accepting RL-based trajectory planners; current certification paradigms (DO-178C, ISO 26262) incompatible with opaque neural policies.
- Non-stationary safety constraints in RL remain entirely unaddressed.
- Reward-free exploration theory does not scale to deep RL; the ICML 2026 bounds are tabular.

### 可用图片
None found relevant in `/data/` or `/assets/`.

### 仍需补充
- A structured comparison matrix (method, venue, key metric, domain, guarantee type) for the five most impactful advances would strengthen the synthesis; data exists across chapters but requires consolidation.
- Concrete 6-month timeline grounded in confirmed venue announcements (ICML 2026 Seoul Jul, NeurIPS 2026); no specific safe RL + sparse-reward challenge tracks announced yet.
- Industry/regulatory body statements (NHTSA, EASA, SAE) on RL-based systems not identified.
- No single benchmark simultaneously evaluates sparse-reward exploration, FM-guided exploration, safe RL, and trajectory planning on the same environments.
- Non-stationary constraint methods are a pure gap without any attempted solutions in the survey period.


# Section 2：给 Write 阶段的执行建议

## Cross-Chapter Consistency
- **Terminology**: Define each term once in Chapter 1 and use consistently: "sparse reward," "intrinsic reward / intrinsic motivation," "extrinsic reward," "constrained MDP (CMDP)," "safety constraint," "cost function," "exploration bonus." Do not alternate synonyms without clarifying relationships.
- **Notation**: Establish unified MDP notation in Ch 1 (state s, action a, reward r, transition T, discount γ, cost c, constraint threshold d). Constrained RL notation (Lagrange multipliers λ, cost-value functions V_c) introduced formally in Ch 4.
- **Abbreviations**: Define all abbreviations at first use in each chapter. Standardize: RL, MDP, CMDP, CPO, PPO, SAC, HER, RND, ICM, LLM, FM, UAV.
- **Time references**: Use explicit date references (e.g., "as of Q1 2026") rather than vague "recently" or "in recent months."

## Source Verification Notes
- Sample-efficiency improvement claims (e.g., "N× faster") from FM-guided exploration papers must be verified against original publications (preprint vs. camera-ready discrepancies).
- Constraint-satisfaction guarantees ("zero violation during training") must be checked for whether they hold in expectation, with high probability, or almost surely.
- Sim-to-real transfer claims for RL-based trajectory planning must be verified for environment fidelity, domain randomization regime, and real-world vs. simulation-only deployment.
- Referenced benchmarks (Safety Gymnasium, MiniGrid, D4RL, MetaDrive) should cite correct version numbers (several underwent revisions during survey period).

## Structural and Tonal Advice
- Ch 2 focuses on methods with intellectual lineage within RL exploration literature (curiosity, counts, information gain). Ch 3 focuses on methods importing external priors from foundation models or combining multiple paradigms.
- Ch 5 is highest-value for practitioners: go beyond "method X applied to domain Y" and provide analytical discussion of why certain methods are well/ill-suited for specific trajectory planning settings.
- Maintain neutral, analytical tone. Present comparative results without advocating for particular approaches; reserve evaluative language for Ch 6 synthesis.
- Avoid excessive paper enumeration without analytical commentary. Each method discussed should include brief assessment of contribution, novelty, and limitations.
- Forward outlook (Ch 6) should frame projections as logical extrapolations of observed trends, grounded in specific current developments.
