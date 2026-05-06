# Section 1：章节研究计划

## Chapter 1: Theoretical Foundations of Quantitative Asset Allocation
### 研究目标
- Establish the conceptual and mathematical groundwork: formal definition of portfolio optimization, risk measurement taxonomy (variance, VaR, CVaR, tail-risk), return prediction paradigms, and evaluation criteria (Sharpe, Sortino, turnover, transaction-cost-adjusted returns).
- Explain why ML entered portfolio optimization: curse of dimensionality in covariance estimation, non-linearity, regime changes.
- Set unified vocabulary and notation for the entire report.

### 关键发现
- Markowitz (1952) formulated portfolio construction as: **maximize μᵀw** s.t. **wᵀΣw ≤ σ²_tar**, **1ᵀw = 1**; equivalently, maximize **μᵀw − γwᵀΣw**. Key assumptions: single-period horizon, E–V rule (mean-variance utility), symmetric risk measure. Gaussian returns are sufficient but not necessary — the "Great Confusion." Analytical solution **w⋆ = (1/2γ)Σ⁻¹(μ + ν1)** reveals dependence on Σ⁻¹, hence sensitivity to estimation error [Boyd et al. 2024](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf "Markowitz Portfolio Construction at Seventy, Stanford, January 2024").
- Risk measurement taxonomy: (a) Variance/covariance **σ² = wᵀΣw** — symmetric, penalizes upside and downside equally; (b) VaR — quantile-based, not subadditive, fails coherence axioms; (c) CVaR/Expected Shortfall — coherent risk measure per Artzner et al. (1999) four axioms (translation invariance, subadditivity, positive homogeneity, monotonicity), computable via convex optimization per [Rockafellar & Uryasev 2000](https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf "Optimization of Conditional Value-at-Risk, The Journal of Risk, 2(3), 2000"); (d) Maximum drawdown — path-dependent, extended to CDaR [Palomar 2025](https://portfoliooptimizationbook.com/book/6.3-performance-measures.html "Portfolio Optimization textbook, Section 6.3").
- Artzner, Delbaen, Eber & Heath (1999) established the coherent risk measure axioms and proved VaR is not coherent (fails subadditivity), motivating CVaR adoption [Artzner et al. 1999](https://people.math.ethz.ch/~delbaen/ftp/preprints/CoherentMF.pdf "Coherent Measures of Risk, Mathematical Finance 9(3): 203–228, 1999").
- Basel FRTB (finalized January 2019, BIS d457) replaced 10-day 99% VaR with **Expected Shortfall at 97.5% confidence** as the standard metric for internal model approach market risk capital [Finalyse FRTB Guide](https://www.finalyse.com/blog/var-an-introductory-guide-in-the-context-of-frtb "VaR: An Introductory Guide in the context of FRTB, citing BIS d457").
- Michaud (1989) termed MVO optimizers **"estimation-error maximizers"** — systematically overweighting assets with largest estimation errors. DeMiguel, Garlappi & Uppal (2009) found that **none of 14 optimized strategies consistently beat naïve 1/N** across seven datasets; sample-based MVO needs ~3,000 months for 25 assets and ~6,000 months for 50 assets to outperform 1/N [DeMiguel et al. 2009](https://academic.oup.com/rfs/article/22/5/1915/1592901 "Optimal Versus Naive Diversification, Review of Financial Studies, 22(5): 1915–1953").
- Ledoit-Wolf (2004) shrinkage estimator: "nobody should be using the sample covariance matrix" — shrinking toward structured target dramatically improves out-of-sample performance [Ledoit & Wolf 2004](https://econ.uzh.ch/dam/jcr:8a18d37f-3238-4c14-a276-66392e82961b/jpm_2004..pdf "Honey, I Shrunk the Sample Covariance Matrix, Journal of Portfolio Management, 2004").
- ML entered portfolio optimization due to: (a) curse of dimensionality in covariance estimation (n(n+1)/2 parameters for n assets), (b) non-linearity/skewness/kurtosis in returns, (c) regime changes violating stationarity, (d) alternative data explosion. Key milestone: Gu, Kelly & Xiu (2020) benchmarked ML methods for return prediction, showing deep neural networks deliver the highest out-of-sample predictive R² [CFA Institute 2024](https://rpc.cfainstitute.org/blogs/enterprising-investor/2024/how-machine-learning-is-transforming-portfolio-optimization "How Machine Learning Is Transforming Portfolio Optimization, September 2024").
- ML taxonomy for allocation: supervised learning (return/covariance prediction via LASSO, trees, NNs), unsupervised learning (regime detection, PCA, HRP), reinforcement learning (MDP-based sequential allocation with DDPG, PPO, A2C).
- Evaluation criteria: Sharpe Ratio **SR = (wᵀμ − r_f)/√(wᵀΣw)**, Sortino Ratio (downside semi-variance only), Calmar Ratio (return/max drawdown), Information Ratio (active return/tracking error), Turnover **T = ½||z||₁**, transaction-cost-adjusted returns [Palomar 2025](https://portfoliooptimizationbook.com/book/6.3-performance-measures.html "Portfolio Optimization textbook, Section 6.3").

### 可用图片
（无直接相关本地图片）

### 仍需补充
- Markowitz (1952) original paper full text (JSTOR paywall): key facts confirmed through multiple T1/T2 secondary sources but direct reading not achieved.
- Michaud (1989) original paper full text (ResearchGate forbidden): "estimation-error maximizer" characterization confirmed through secondary sources.
- Gu, Kelly & Xiu (2020) exact out-of-sample R² numbers not directly verified from paper itself.
- Precise dates for early ML-finance milestones (1990s): relies on secondary sources; primary papers (Trippi & Turban 1992, Refenes 1995) could strengthen historical narrative.


## Chapter 2: Classic Portfolio Optimization Models — Mean-Variance and Black-Litterman
### 研究目标
- Rigorous exposition of MVO (efficient frontier derivation, sensitivity to estimation error, corner solutions, instability) and BL (Bayesian updating, equilibrium returns, Ω matrix, subjective view integration).
- Regularization techniques for MVO: Ledoit-Wolf shrinkage, resampled efficient frontier, robust optimization.
- Empirical track record across asset classes; when these models beat or lose to naïve benchmarks (1/N, risk parity).
- Identified shortcomings that motivate ML alternatives: linearity, static single-period, Gaussian assumptions, inability to handle unstructured data.

### 关键发现
- MVO 基本数学公式：风险约束型 maximize **μᵀw** s.t. **wᵀΣw ≤ (σ_tar)²**, **1ᵀw = 1**；风险调整收益型 maximize **μᵀw − γwᵀΣw** s.t. **1ᵀw = 1**。解析解 **w⋆ = (1/2γ)Σ⁻¹(μ + ν⋆1)** 中 Σ⁻¹ 暗示对协方差矩阵近奇异的敏感性。实际约束（长仓、权重上限、杠杆、换手率、流动性、因子中性）保持凸性，现代求解器亚秒级处理万级资产 [Boyd et al. 2024](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf "Markowitz Portfolio Construction at Seventy, Stanford, January 2024")。
- MVO "estimation-error maximizer" 本质：Michaud (1989) 命名。Idzorek 八资产示例中历史收益输入导致美国债券配置 1144%、国际债券 -105%，而隐含均衡收益输入则回归市值权重 [Idzorek 2004](https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf "A Step-by-Step Guide to the Black-Litterman Model, July 2004")。
- Chopra & Ziemba (1993) 量化了三类输入误差影响：中等风险厌恶下，**均值估计误差影响 ≈ 方差误差的 10 倍 ≈ 协方差误差的 20 倍**。高风险厌恶时差距缩小 [Chopra & Ziemba 1993](https://people.duke.edu/~charvey/Teaching/BA453_2006/Chopra_The_effect_of_1993.pdf "The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice, JPM Winter 1993")。
- Best & Grauer (1991) 证明微幅上调某一资产预期收益可导致一半资产权重从正变零。Idzorek (2004) 示例：相关系数 99.8% 的预期收益向量产生的最优权重相关系数仅 66% [Idzorek 2004](https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf "A Step-by-Step Guide to the Black-Litterman Model, July 2004")。
- DeMiguel et al. (2009)：14 种优化策略在 7 个数据集上无一始终优于 1/N；样本 MVO 需约 3,000 月（25 资产）/ 6,000 月（50 资产）才能超越 1/N [DeMiguel et al. 2009](https://academic.oup.com/rfs/article/22/5/1915/1592901 "Optimal Versus Naive Diversification, RFS, 22(5): 1915–1953, 2009")。
- Ledoit-Wolf (2004) 收缩估计量 **Σ̂_shrink = α̂F + (1−α̂)S**：N=100 时年化信息比率 0.91 vs. 样本协方差 0.59，提升约 54%。收缩目标为常相关模型 [Ledoit & Wolf 2004](http://www.ledoit.net/honey.pdf "Honey, I Shrunk the Sample Covariance Matrix, JPM, 2004")。
- Michaud (1998) 重采样有效前沿（REF）：蒙特卡洛多次抽样 → 计算多条有效前沿 → 权重取平均。REF 包含所有资产非零配置，不确定性 100% 时退化为 MVO、0% 时退化为等权。模拟表明 REF 样本外更优 [Michaud & Michaud 2007](https://newfrontieradvisors.com/media/rxbld4hq/estimation-error-and-portfolio-optimization-12-05.pdf "Estimation Error and Portfolio Optimization: A Resampling Solution, JIM, 2007")。
- Jagannathan & Ma (2003)：非负约束 w ≥ 0 等价于对协方差矩阵的隐式收缩，即使约束"错误"也能系统性降低样本外风险 [Ledoit & Wolf 2004](http://www.ledoit.net/honey.pdf "引用 Jagannathan & Ma 2003, Journal of Finance 58(4)")。
- Goldfarb & Iyengar (2003) 鲁棒优化：均值属于椭球不确定集 {μ̂+δ: ||δ||≤ρ}。鲁棒收益 **R_wc = μᵀw − ρᵀ|w|**，鲁棒方差 **(σ_wc)² = σ² + ϱ(Σ¹/²|w|)²** [Boyd et al. 2024](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf "Markowitz Portfolio Construction at Seventy, §1.3")。
- 最小方差组合实证：Clarke, de Silva & Thorley (2006/2011)，1968–2005 美股年化波动率比市值加权低约 25%，收益率相当甚至更高（低波动率异象）[Clarke et al. 2006](https://www.scirp.org/reference/referencespapers?referenceid=2837300 "Minimum-Variance Portfolios in the US Equity Market, JPM 33(1), 2006")。
- Black-Litterman 完整后验公式：**μ_BL = [(τΣ)⁻¹ + PᵀΩ⁻¹P]⁻¹[(τΣ)⁻¹Π + PᵀΩ⁻¹Q]**，等价形式 **μ_BL = Π + τΣPᵀ(PτΣPᵀ + Ω)⁻¹(Q − PΠ)**，其中 Π = λΣw_mkt 为隐含均衡收益 [Idzorek 2004](https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf "A Step-by-Step Guide to the Black-Litterman Model") [Palomar 2019](https://palomar.home.ece.ust.hk/MAFS6010R_lectures/slides_shrinkage_n_BL.pdf "Shrinkage and BL, HKUST")。
- BL τ 与 Ω 校准：τ 文献建议从 0.01–0.05（Black & Litterman 1992）到 1（Satchell & Scowcroft 2000）不等。Idzorek (2004) 提出基于 0%–100% 直觉置信度的方法绕过 τ 指定 [Idzorek 2004](https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf "A Step-by-Step Guide to the Black-Litterman Model, Section 3")。
- BL 与收缩估计的统一视角：BL 后验可表示为 **μ_BL = W_mkt·μ̂_mkt + W_views·μ̂_views**，本质为 James-Stein 收缩推广。τ→0 时退化为市场均衡，τ→∞ 时退化为纯观点收益 [Palomar 2019](https://palomar.home.ece.ust.hk/MAFS6010R_lectures/slides_shrinkage_n_BL.pdf "Shrinkage and BL, HKUST")。
- BL 核心局限：(1) 观点主观性（Herold 2003 认为仅适合量化基金经理）；(2) Ω 校准敏感，Litterman (2003) 承认无通用答案；(3) 静态单期；(4) 正态分布假设；(5) 非观点资产权重不变 [Idzorek 2004](https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf "A Step-by-Step Guide to the BL Model, endnote 11")。
- 风险平价 ERC 组合：要求 **w_i·(Σw)_i / √(wᵀΣw) = (1/N)·√(wᵀΣw)** ∀i。位于等权与最小方差之间。完全避免预期收益估计 [Maillard, Roncalli & Teiletche 2010](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1271972 "On the Properties of ERC Portfolios, JPM, 36(4), 2010")。
- Markowitz++ 现代实践（Boyd et al. 2024）：鲁棒化惩罚 + 因子模型降维 + 交易成本（含冲击项 κ_impact·|z|^{3/2}）+ 滚动回测。2004–2023 美股约 1,500 只股票回测，各指标显著优于基本 MVO [Boyd et al. 2024](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf "Markowitz Portfolio Construction at Seventy, §5")。
- MVO 单期局限的回应：特殊条件下随机最优控制 = 单期 Markowitz（Gârleanu & Pedersen 2020）。Moallemi et al. (2013) 证明单期策略接近完全随机控制的表现上界 [Boyd et al. 2024](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf "Markowitz Portfolio Construction at Seventy, §1.2")。
- RMT 与非线性收缩：Marcenko-Pastur 定律表明当 q=N/T 不趋于零时样本特征值系统性失真。非线性收缩（Ledoit & Wolf 2017）对每个特征值施加不同修正，在 Sharpe 优化下更优 [Palomar 2019](https://palomar.home.ece.ust.hk/MAFS6010R_lectures/slides_shrinkage_n_BL.pdf "Shrinkage and BL, HKUST, RMT Section")。
- 因子模型协方差估计 Σ = FΣ_fFᵀ + D：参数从 O(n²) 降至 O(nk)，n=10,000/k=100 时可加速约 10,000 倍 [Boyd et al. 2024](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf "Markowitz Portfolio Construction at Seventy, §3.3")。
- 催生 ML 的六大根本局限：(1) 线性/二次假设无法捕捉非线性市场动态；(2) 静态单期无法内生处理交易成本和时序依赖；(3) 高斯假设忽视厚尾（Fama 1965）；(4) 协方差维度灾难（500 资产信息比率从 1.24 降至 0.30）；(5) 无法处理非结构化/替代数据；(6) 无法适应体制变化和非平稳性 [Boyd et al. 2024](https://web.stanford.edu/~boyd/papers/pdf/markowitz.pdf "Markowitz Portfolio Construction at Seventy") [Ledoit & Wolf 2004](http://www.ledoit.net/honey.pdf "Honey, I Shrunk the Sample Covariance Matrix")。

### 可用图片
（无直接相关本地图片）

### 仍需补充
- Chopra & Ziemba (1993) 原文中精确数值表格尚未直接确认，"10 倍""20 倍"基于多个二手来源的一致表述。
- Clarke, de Silva & Thorley (2006/2011) 精确年化收益差和波动率差需从原文获取，当前引用基于摘要和二手来源。
- post-2020 对 MVO、BL、1/N、risk parity 的统一基准比较的独立第三方学术文献缺失。
- Bertsimas & Brown (2009) 鲁棒优化论文未找到完整内容。
- He & Litterman (1999) "The Intuition Behind Black-Litterman" Goldman Sachs 内部报告未在公开网络找到完整版本。


## Chapter 3: Emerging Machine Learning and Deep Learning Models for Portfolio Optimization
### 研究目标
- Survey LSTM, Transformer, and RL-based approaches to asset allocation: architectures, formulations, empirical findings.
- LSTM for temporal dependencies and regime-change detection; Transformer for cross-asset attention and long-range dependency; RL as MDP-based sequential allocation (DDPG, PPO, A2C).
- Hybrid DL architectures: LSTM-Transformer combos, RL with DL state representations.
- New failure modes: overfitting, data hunger, non-stationarity, concept drift, interpretability deficit, reward shaping sensitivity.

### 关键发现
- Fischer & Krauss (2018) LSTM 基准：S&P 500 成分股 1992–2015 日频数据，多空策略日均收益 0.46%、年化 SR 5.8（交易成本前）。但 2010 年后超额收益显著衰减，扣除交易成本后盈利能力在零附近波动 [Fischer & Krauss 2018](https://ideas.repec.org/a/eee/ejores/v270y2018i2p654-669.html "Deep learning with LSTM for financial market predictions, EJOR, 270(2): 654-669, 2018")。
- LSTM 两种范式：(a) predict-then-optimize——预测收益/协方差后输入传统优化器；(b) end-to-end——直接输出组合权重，通过 Sharpe 等金融目标反向传播。范式(b)可能减少误差累积但训练更复杂、可解释性更差 [Fischer & Krauss 2018](https://ideas.repec.org/a/eee/ejores/v270y2018i2p654-669.html "EJOR, 2018")。
- Gu, Kelly & Xiu (2020) 里程碑基准：近 30,000 只美国个股、60 年数据（1957–2016）。基准 OLS R² 0.16%，900+ 因子 OLS R² 转负，弹性网络恢复至 0.11%，PCA/PLS 0.26–0.27%，**回归树和神经网络 0.33%–0.40%**。NN3（32-16-8）表现最优。S&P 500 择时 SR 0.77（vs 买入持有 0.51）；多空十分位策略 **SR 1.35**（vs OLS 0.61）。最具预测力信号：动量、流动性、波动率 [Gu, Kelly & Xiu 2020](https://dachxiu.chicagobooth.edu/download/ML.pdf "Empirical Asset Pricing via ML, RFS, 33(5): 2223-2273, 2020")。
- Gu et al. (2020) 方法论：训练/验证/测试三分法；R²_oos = 1 − Σ(r−r̂)²/Σr²（零预测基准）；Diebold-Mariano 检验比较模型；广义线性模型（含样条但无交叉项）未稳健超越线性——**预测因子非线性交互项是关键非线性来源** [Gu, Kelly & Xiu 2020](https://dachxiu.chicagobooth.edu/download/ML.pdf "RFS, 2020")。
- Jiang, Xu & Liang (2017) DRL 框架：EIIE 拓扑（资产独立评估器）+ PVM（权重记忆）+ OSBL（在线随机批学习）+ 对数收益策略梯度。CNN/RNN/LSTM 三个实例在加密货币（30 分钟频率）50 天内≥4 倍收益（佣金 0.25%）[Jiang et al. 2017](https://arxiv.org/abs/1706.10059 "A DRL Framework for Financial Portfolio Management, arXiv:1706.10059, 2017")。
- RL MDP 公式化：状态 s_t = (P_t, a_{t-1})，动作 a_t ∈ simplex，奖励 r_t = ln(a_tᵀy_t(1−c_t))。Moody & Saffell (2001) 提出 RRL + differential Sharpe ratio 作为奖励，在 1970–1994 美国国债市场优于买入持有和 Q-learning [Moody & Saffell 2001](https://pubmed.ncbi.nlm.nih.gov/18249919/ "Learning to Trade via Direct Reinforcement, IEEE Trans. NN, 12(4): 875-889, 2001")。
- DDPG/PPO/A2C 比较：FinRL 库在 DJIA 30 股票上实证比较。RAT (IJCAI 2020) 发现 DDPG 和 PPO **通常难以收敛**，选用更简单的直接策略梯度。RL 算法选择本身是高风险决策 [FinRL: Liu et al. 2020](https://arxiv.org/abs/2011.09607 "FinRL, NeurIPS 2020 DRL Workshop") [Xu et al. 2020](https://www.ijcai.org/proceedings/2020/0641.pdf "RAT, IJCAI 2020")。
- FinRL 框架：首个开源 DRL 全流程金融框架，支持 DQN/DDPG/PPO/SAC/A2C/TD3，涵盖 NASDAQ-100、DJIA、S&P 500、HSI、SSE 50、CSI 300 环境，内置交易成本和流动性约束处理 [Liu et al. 2020](https://arxiv.org/abs/2011.09607 "FinRL, arXiv:2011.09607, NeurIPS 2020")。
- TFT 架构（Lim et al. 2021）：变量选择网络 + 门控残差网络 + 循环层（局部）+ 自注意力层（长期依赖）。支持三类输入（静态协变量、已知未来、仅历史观测）。注意力权重提供时间维度可解释性。虽设计用于通用时序，天然适合金融多资产收益预测 [Lim et al. 2021](https://arxiv.org/abs/1912.09363 "TFT, IJF 37(4): 1748-1764, 2021")。
- Portfolio Transformer（Kisiel & Gorse 2022）：首个编码器-解码器 Transformer 端到端组合优化，直接优化 Sharpe 比率。在三个数据集上风险调整绩效优于 LSTM 基准 [Kisiel & Gorse 2022](https://arxiv.org/abs/2206.03246 "Portfolio Transformer, arXiv:2206.03246, 2022")。
- RAT 跨资产注意力（Xu et al. IJCAI 2020）：Sequential Attention（上下文注意力替代点积注意力）+ Relation Attention（资产维度自注意力捕捉动态相关性）。Crypto-A 上 APV 156.53 vs EIIE 16.04，SR 7.13% vs 6.87% [Xu et al. 2020](https://www.ijcai.org/proceedings/2020/0641.pdf "RAT, IJCAI 2020, pp. 4647-4653")。
- Transformer vs RNN 结构优势：(1) 并行训练（自注意力 vs 顺序处理）；(2) 长程依赖路径 O(1) vs O(n)；(3) 注意力权重可解释性 [Xu et al. 2020](https://www.ijcai.org/proceedings/2020/0641.pdf "RAT, IJCAI 2020")。
- HRP（López de Prado 2016）：三步法——层级聚类（相关距离）→ 拟对角化 → 递归二分（逆方差加权）。**完全避免协方差矩阵求逆**，可在奇异矩阵上计算权重。蒙特卡洛实验：HRP 样本外方差低于 CLA [López de Prado 2016](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678 "Building Diversified Portfolios, JPM, 42(4): 59-69, 2016")。
- HRP 实证：Bocconi BSIC 2025 约 1,292 只美股回测（2005–2025）HRP 累积回报 1,299.67%，但 2008 年最大回撤 -60%，均值 SR 0.4711 [López de Prado 2016](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678 "JPM, 2016") [BSIC 2025](https://bsic.it/wp-content/uploads/2025/03/Article-HRP-1.pdf "Advanced Portfolio Optimization: HRP, Bocconi BSIC, 2025")。
- GNN 组合优化：资产为图节点，通过相关性/行业/供应链边传递信息。RAT Relation Attention 概念上类似图注意力，动态学习资产间关系 [Xu et al. 2020](https://www.ijcai.org/proceedings/2020/0641.pdf "RAT, IJCAI 2020")。
- RL 交易成本处理：(1) 乘法因子 r_t = ln(a_tᵀy_t(1−c_t))（Jiang 2017, RAT 2020 佣金 0.25%）；(2) 递归机制——拼接 a_{t-1} 入特征图约束激进交易。RL 显式交易成本建模是相对静态优化器的重要优势 [Xu et al. 2020](https://www.ijcai.org/proceedings/2020/0641.pdf "RAT, IJCAI 2020") [Jiang et al. 2017](https://arxiv.org/abs/1706.10059 "DRL Framework, 2017")。
- PBO（Bailey et al. 2015）：CSCV 方法评估回测过拟合。随机游走上优化可获 SR 1.27（样本内），但 PBO 55%、约 53% 样本外 SR 为负。**高样本内 SR 可能对应低样本外 SR** [Bailey et al. 2015](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf "The Probability of Backtest Overfitting, J. Computational Finance, 2015")。
- Deflated Sharpe Ratio（Bailey & López de Prado 2014）：校正多重比较偏差、非正态性偏差、短样本偏差。对评估 ML/DL 策略至关重要 [Bailey & López de Prado 2014](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf "JPM, 40(5): 94-107, 2014")。
- 系统性失败模式六类：(1) 数据饥渴——NN3 优于更深网络（金融数据小且信噪比低）；(2) 非平稳性——Fischer & Krauss 记录 2010 后 LSTM alpha 衰减；(3) 过拟合——Bailey et al. (2014) 警告测试数十亿变体必然产生虚假发现；(4) 可解释性——SHAP/注意力权重/变量重要性为部分解决方案；(5) RL 奖励敏感性——不同奖励函数导致完全不同策略；(6) 灾难性遗忘——在线 RL 学新体制时遗忘旧体制 [Gu et al. 2020](https://dachxiu.chicagobooth.edu/download/ML.pdf "RFS, 2020") [Bailey et al. 2015](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf "J. Computational Finance, 2015")。
- Gu et al. (2020) 正则化策略：弹性网络（L1+L2）、早停（隐式收缩）、批归一化、集成学习（多种子平均）、Huber 鲁棒损失。系统组合使 60 年数据上实现可靠样本外预测 [Gu, Kelly & Xiu 2020](https://dachxiu.chicagobooth.edu/download/ML.pdf "RFS, 2020, Section 1.7")。
- LSTM-Transformer 混合：TFT 本身即为 LSTM+Transformer 混合（循环层处理局部模式，自注意力处理长程依赖）。RAT context attention 类似设计思路 [Lim et al. 2021](https://arxiv.org/abs/1912.09363 "TFT, 2021") [Xu et al. 2020](https://www.ijcai.org/proceedings/2020/0641.pdf "RAT, IJCAI 2020")。

### 可用图片
（无直接相关本地图片）

### 仍需补充
- Fischer & Krauss (2018) 精确方向性准确率数字（如 55%–56%）原文受访问限制未直接确认。
- Kim & Won (2018) LSTM 体制检测与动态配置的确切引用未找到匹配的高影响力论文。
- GAN 用于组合优化在当前文献中影响有限，主要用于合成数据生成而非权重优化。
- post-2023 RL 组合优化的突破性论文未在顶级期刊/会议发现具体量化结果。
- Jiang et al. (2017) 报告加密市场累积收益倍数而非标准年化 Sharpe 比率。
- López de Prado (2016) HRP 蒙特卡洛实验精确数值差异百分比需从原文获取。


## Chapter 4: Cross-Model Comparative Analysis — Risk, Return, and Allocation
### 研究目标
- Systematic multi-dimensional comparison of classic vs. emerging models along: risk measurement, return prediction accuracy, allocation methodology.
- Unified evaluation framework: benchmark datasets, backtesting protocol (walk-forward, expanding window), statistical significance tests (Diebold-Mariano, bootstrap).
- Comparison on: tail risk handling, forecast accuracy (MSE, directional accuracy), portfolio weight stability/turnover, diversification, max drawdown, transaction-cost-adjusted performance.
- Interpretability and regulatory considerations (SHAP, attention weights vs. closed-form).
- Computational cost, latency, and infrastructure requirements.

### 关键发现
（待 researcher 补充）

### 可用图片
（待 researcher 补充）

### 仍需补充
（待 researcher 补充）


## Chapter 5: Toward a Hybrid Modeling Framework — Architecture, Integration, and Outlook
### 研究目标
- Synthesize Chapters 2–4 into a concrete hybrid framework proposal combining BL Bayesian view integration + DL pattern extraction + RL sequential optimization + MVO risk constraints.
- Proposed modular pipeline: DL views → BL allocation engine → RL meta-optimizer → classical risk overlays.
- Training/deployment considerations: end-to-end vs. staged, drift detection, fail-safe fallback.
- Survey existing hybrid experiments (DRL+BL, decision-tree+Markowitz, LSTM+MVO) and reported performance gains.
- Open challenges: Bayesian-frequentist coherence, regulatory acceptance, scalability, standardized benchmarking.
- Forward-looking: foundation models for financial time series, multi-agent RL, alternative data integration, real-time adaptive portfolios.

### 关键发现
（待 researcher 补充）

### 可用图片
（待 researcher 补充）

### 仍需补充
（待 researcher 补充）


# Section 2：给 Write 阶段的执行建议
- **Unified terminology:** Define key terms (views, expected returns, risk budget, reward function, portfolio weights, rebalancing frequency) in Chapter 1 and use consistently throughout. Avoid confusing synonyms (e.g., "alpha signal" vs. "return forecast").
- **Consistent notation:** Adopt a single notation system in Chapter 1 (**w** for weight vector, **Σ** for covariance, **μ** for expected return, **π** for equilibrium returns). Enforce across all chapters.
- **Cross-chapter metric consistency:** Evaluation criteria from Chapter 1 and Chapter 4's comparison framework must use identical metric definitions. Chapters 2–3 should reference the same metrics for mental cross-comparison.
- **Avoid advocacy bias:** Present each model family's strengths and weaknesses with balanced, evidence-based analysis. Chapter 4 must not be a straw-man setup for Chapter 5.
- **Separate empirical claims from proposals:** Chapters 2–4 cite evidence; Chapter 5's hybrid proposal must clearly distinguish published results from speculative components.
- **Estimation-error as binding thread:** Each chapter should address how its featured model class handles (or fails to handle) estimation error — this is the narrative thread.
- **Time-window discipline:** Always specify asset universe, time period, and rebalancing frequency when citing performance. Research window: April 2025–October 2026 for frontier developments; foundational concepts from before 2025 are expected.
- **Practical grounding:** Address real-world frictions (transaction costs, liquidity, short-selling constraints, regulatory limits) throughout.
- **Chapter 4 is the linchpin:** Most rigorously structured; include a summary comparison table/matrix comparing all model families across all dimensions.
- **Chapter 5 should be concrete:** The hybrid framework should be specific enough for a quant team to use as a blueprint, with clearly stated assumptions and limitations.
