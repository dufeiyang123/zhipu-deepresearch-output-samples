# Section 1：章节研究计划

## Chapter 1：Taxonomy of Advanced Quantitative Strategies and Their Evaluation Challenges
### 研究目标
- 建立主要量化策略族群（多因子、统计套利、高频/做市、CTA/趋势跟踪、机器学习驱动、混合方法）的清晰分类体系
- 针对每个策略族群，梳理其典型绩效特征、风险画像和运营特征，阐明为何单一度量无法实现统一评价
- 界定本报告所提评价框架必须容纳的异质性维度

### 关键发现
- 全球对冲基金行业资产于 2025 年 Q3 末达到创纪录的 4.98 万亿美元，Q4 突破 5 万亿美元里程碑；2025 年前三季度净流入 710 亿美元，为 2007 年以来最高 [HFR Global Hedge Fund Industry Report](https://www.hfr.com/media/market-commentary/global-hedge-fund-industry-capital-surges-nears-historic-5-trillion-milestone/ "HFR Q3 2025 Industry Report")
- HFR Q3 2025 按策略分类：Equity Hedge 1.50 万亿美元、Event-Driven 1.41 万亿美元、Relative Value 1.32 万亿美元（其中 Multi-Strategy 8073 亿美元）、Macro 7590 亿美元 [HFR Global Hedge Fund Industry Report](https://www.hfr.com/media/market-commentary/global-hedge-fund-industry-capital-surges-nears-historic-5-trillion-milestone/ "HFR Q3 2025 Industry Report")
- "十亿美元俱乐部"551 家机构在 2025 H1 管理 3.6 万亿美元，占全行业约 86%；多策略基金首次在增量资产上超越纯股票多空 [With Intelligence BDC Report](https://www.withintelligence.com/insights/billion-dollar-club-h1-2025/ "Billion Dollar Club Report H1 2025")
- Aurum 将量化策略分为五个互斥子策略：统计套利、CTA/管理期货、量化股票市场中性（QEMN）、量化宏观/全球资产配置、风险溢价/另类风险溢价 [Aurum Quant Strategy Deep Dive](https://www.aurum.com/wp-content/uploads/210831-Aurum-Hedge-Fund-Data-Engine-Strategy-Deep-Dive_Quant.pdf "Aurum Quant Deep Dive, August 2021")；CCMR 2025 年 2 月报告则将对冲基金分为 Long/Short Equity、Global Macro、Event-Driven、Fixed-Income Relative Value、Managed Futures、Quantitative、Distressed Securities 七类 [CCMR Report](https://capmktsreg.org/wp-content/uploads/2025/02/CCMR-Hedge-Fund-Report-Final-02.28.259144.pdf "CCMR, February 2025")
- 量化股票五年年化收益 11.31%（2025 年 11.20%），超过三分之一配置者在 2025 年加仓；Man Group 分析显示传统因子策略在 2020 年前后经历约 -29% 峰谷回撤，随后至 2025 年 4 月反弹 +84% [BNP Paribas 2026 Hedge Fund Outlook](https://globalmarkets.cib.bnpparibas/2026-hedge-fund-outlook/ "BNP Paribas, January 2026")；[Man Group Research](https://www.man.com/insights/is-this-time-different "Man Group: Is This Time Different?, June 2025")
- 统计套利策略 2025 年前 4 个月回报 7.79%，典型特征为市场中性（beta ±0.10）、短持仓周期（小时至天）、高换手、目标 Sharpe≥1.5，Aurum 数据显示其为量化子策略中费用最高者（管理费 2.18%、业绩费 23.32%） [Aurum Quant Strategy Deep Dive](https://www.aurum.com/wp-content/uploads/210831-Aurum-Hedge-Fund-Data-Engine-Strategy-Deep-Dive_Quant.pdf "Aurum Quant Deep Dive, August 2021")
- 全球高频交易市场 2024 年收入规模 103.6 亿美元，预计到 2030 年达 160.3 亿美元（CAGR 7.7%），做市细分占 72.3%；HFT 约占全球股票交易量一半 [Grand View Research](https://www.grandviewresearch.com/industry-analysis/high-frequency-trading-market-report "Grand View Research HFT Market Report, 2025–2030")
- CFA Institute 2026 年研究将 CTA 回报分解为快速（20–60 天）、中速（~125 天）和慢速（250–500 天）趋势跟踪层级，慢速趋势策略五年 Sharpe 达 0.75、回报/最大回撤比 0.84，远高于 SG CTA Trend Index（Sharpe 0.38） [CFA Institute](https://rpc.cfainstitute.org/blogs/enterprising-investor/2026/decoding-cta-allocations-by-trend-horizon "Decoding CTA Allocations by Trend Horizon, CFA Institute, 2026")
- 2025 年 HKUST/IDEA 综述将 AI 量化投资划分为三阶段：传统统计+人工特征 → 深度学习全流程建模 → LLM 驱动的自主代理工作流 [Cao et al. 2025](https://arxiv.org/html/2503.21422v1 "From Deep Learning to LLMs: A survey of AI in Quantitative Investment, 2025")
- 量化多策略五年年化 12.76%（2025 年 11.49%），24% 配置者计划 2026 年增配 [BNP Paribas 2026 Hedge Fund Outlook](https://globalmarkets.cib.bnpparibas/2026-hedge-fund-outlook/ "BNP Paribas, January 2026")
- HFRI FWC 截至 2025 年 10 月的 12 个月头尾十分位差达 56.5 个百分点，量化子策略内部（QEMN 峰值 37.5pp）亦存在巨大业绩离散度 [HFR Market Commentary](https://www.hfr.com/media/market-commentary/hfri-macro-extends-surge-leading-industry-wide-gains-navigating-technology-tariff-volatility/ "HFR October 2025")；[Aurum Quant Strategy Deep Dive](https://www.aurum.com/wp-content/uploads/210831-Aurum-Hedge-Fund-Data-Engine-Strategy-Deep-Dive_Quant.pdf "Aurum Quant Deep Dive, August 2021")
- Sharpe ratio 仅考虑前两阶矩，对尾部肥厚、偏度显著的对冲基金回报分布不适用；不同策略需要不同的专属指标（HFT→延迟/成交率，CTA→层级分解，统计套利→Alpha 归因，ML→过拟合诊断），当前不存在跨策略类型的统一复合评价框架 [BNP Paribas 2026 Hedge Fund Outlook](https://globalmarkets.cib.bnpparibas/2026-hedge-fund-outlook/ "BNP Paribas, January 2026")
- GIPS 标准原为传统多头设计，在对冲基金场景下面临组合定义、非流动资产估值和策略漂移等挑战；HFR 指数存在存活偏差、选择偏差和回填偏差 [CFA Institute GIPS Standards](https://rpc.cfainstitute.org/gips-standards "GIPS Standards")；[CCMR Report](https://capmktsreg.org/wp-content/uploads/2025/02/CCMR-Hedge-Fund-Report-Final-02.28.259144.pdf "CCMR, February 2025")
- 64% 受访配置者计划 2026 年净增加对冲基金敞口，对应约 240 亿美元新增净流入 [BNP Paribas 2026 Hedge Fund Outlook](https://globalmarkets.cib.bnpparibas/2026-hedge-fund-outlook/ "BNP Paribas, January 2026")

### 可用图片
- 无本地可用图片

### 仍需补充
- 2025 年纯量化子策略（stat arb、CTA、QEMN、quant macro、risk premia）各自精确 AUM 分布（Aurum 数据停留在 2021 年 8 月，新版需付费获取）
- Goldman Sachs Prime Services 或 JP Morgan Quant & Derivatives 2025–2026 年量化策略研究报告（付费墙）
- HFT 策略 Sharpe>5 的 2025 年 T1 级实证来源
- 多策略基金 2025 年 22.7% 加权平均回报的 T1/T2 确认（现有来源为 T4 LinkedIn）
- Preqin 2025 全球对冲基金报告完整版（付费墙）


## Chapter 2：Risk-Adjusted Return Metrics — Properties, Pitfalls, and Recent Advances
### 研究目标
- 对 Sharpe ratio、Sortino ratio、Calmar ratio、Omega ratio、Gain-to-Pain ratio 及新近的熵/高阶矩调整变体进行系统比较
- 审视每个指标的统计假设、对回报分布形状的敏感性、有限样本估计误差和已知失效模式
- 调查 2025–2026 年学术和业界在修正或统一指标方面的最新进展

### 关键发现
- Sharpe ratio 定义为 SR = E[Rp−Rb]/σ(Rp−Rb)，t 统计量 = SR×√T；Sortino ratio 以目标半方差替代总方差，惩罚下行风险；Calmar ratio = CAGR / 36 个月最大回撤；Omega ratio = ∫_r^∞[1−F(x)]dx / ∫_{−∞}^r F(x)dx，纳入完整分布；Gain-to-Pain ratio = 月度总回报 / |月度负回报之和|，模型无关 [Sharpe (1994)](https://web.stanford.edu/~wfsharpe/art/sr/sr.htm "The Sharpe Ratio, JPM")；[Keating & Shadwick (2002)](https://people.duke.edu/~charvey/Teaching/BA453_2005/Keating_An_introduction_to.pdf "An Introduction to Omega")
- Smetters & Zhang (2013) 证明 Sharpe ratio 对所有椭圆分布（含 Student-t 等肥尾分布）均可给出正确排序，但同时证明了不可能定理：对一般非正态分布，任何有效的排序度量都不可能与投资者偏好无关 [Smetters & Zhang (2013)](https://www.nber.org/system/files/working_papers/w19500/revisions/w19500.rev0.pdf "A Sharper Ratio, NBER WP 19500")
- Benhamou, Guez & Paris (2020) 证明在椭圆分布下 Omega ratio 与 Sharpe ratio 最优组合完全一致，否定了 Omega 声称的"纳入全分布"优势；Caporin et al. (2018) 进一步证明 Omega ratio 与二阶随机占优不一致 [Benhamou et al. (2020)](https://hal.science/hal-02886481/file/omega-ratio.pdf "Omega and Sharpe ratio")；[Caporin et al. (2018)](https://www.sciencedirect.com/science/article/abs/pii/S0927539817301111 "On the (Ab)use of Omega?")
- Lo (2002) 给出 Sharpe ratio 有限样本渐近标准误 σ_SR = √((1+SR²/2)/n)；基于 12 个月数据、实证 SR=1.0 时，95% 置信区间宽达 [0.21, 1.79]；正自相关回报使朴素 √12 年化高估 Sharpe [Benhamou (2021)](https://hal.science/hal-03207169v1/file/DistributionOfTheSharpeRatio.pdf "Distribution and statistics of the Sharpe Ratio")
- 非正态 IID 下 Sharpe 估计量偏差依赖偏度 γ₁ 和峰度 γ₂（Bao 2009）；错误假设正态可致渐近方差误估达 70%（Mertens 2002）[Two Sigma Technical Report](https://www.twosigma.com/wp-content/uploads/sharpe-tr-1.pdf "Riondato 2018, Sharpe Ratio Estimation")
- Goetzmann et al. (2007) 证明卖出虚值期权可操纵 Sharpe ratio，提出基于幂效用的 Manipulation-Proof Performance Measure (MPPM) [Goetzmann et al. (2007)](https://academic.oup.com/rfs/article-abstract/20/5/1503/1592381 "Portfolio Performance Manipulation, RFS")；Sortino ratio 对 MAR 选择敏感、Calmar ratio 对回溯窗口和单一极端事件敏感
- Bailey & López de Prado (2014) 提出 Deflated Sharpe Ratio (DSR)，同时校正多重检验选择偏差与非正态性：DSR = Φ[(SR̂−SR̂₀)√T / √(1−γ̂₁SR̂+((γ̂₂−1)/4)SR̂²)]；数值示例中 SR̂=2.5、N=88 次独立试验后 DSR 仅 0.90，低于 95% 阈值 [Bailey & López de Prado (2014)](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf "The Deflated Sharpe Ratio, JPM")
- 2026 年 Bajo Traver & Rodriguez 提出 Sharpe Stability Ratio (SSR)，评估风险调整回报的时间一致性，实证显示高但不稳定 Sharpe 的基金在样本外倾向于表现不佳 [Bajo Traver & Rodriguez (2026)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6344658 "The Sharpe Stability Ratio, SSRN")
- Shin (2025) 扩展 Generalized Sharpe-Parity Principle，将风险平价配置与非正态分布下的 Sharpe 推广相统一 [Shin (2025)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5721562 "On the Limits and Extensions of the Generalized Sharpe-Parity Principle, SSRN")
- Oxford 2026 年大规模基准研究以 Sharpe ratio 优化为深度学习策略的首要训练目标，涵盖 RNN、Transformer、状态空间模型等架构，确认 Sharpe 在 ML 策略评估中的核心地位 [Saly-Kaufmann et al. (2026)](https://arxiv.org/pdf/2603.01820 "Deep Learning for Financial Time Series, arXiv")
- 框架分类建议：普适指标（Sharpe、Omega、GPR）+ 策略条件指标（Sortino、Calmar、Treynor、IR）+ 统计校正层（DSR、Lo 置信区间、Ledoit-Wolf bootstrap）+ 理论理想指标（MPPM、Sharper Ratio——计算密集、实际采用率低）

### 可用图片
- 无本地可用图片

### 仍需补充
- Sharpe Stability Ratio (Bajo Traver & Rodriguez 2026) 的精确数学公式与实证结果（SSRN 全文受限）
- AQR、Man Group、Robeco 等头部机构 2025–2026 年是否有新提出的风险调整指标
- Challet (2015) 基于回撤久期的 moment-free Sharpe 估计量的精确公式与实证验证
- MPPM 与 DSR 在实践中能否联合使用的问题尚未在文献中得到解答
- Kappa 指标族（Kaplan & Knowles 2004）——Sortino 为 Kappa₂ 特例——可丰富框架分类但未深入调查
- 2025–2026 年尚未发现被广泛接受的单一"统一"风险调整指标，领域仍以 Sharpe 为主+辅助指标格局


## Chapter 3：Tail-Risk, Drawdown Analysis, and Stress-Testing Protocols
### 研究目标
- 定义并比较尾部风险指标（VaR、CVaR/ES、最大回撤、回撤久期、Ulcer Index）与压力测试方法
- 评估不同策略类型下各指标对极端事件脆弱性的捕捉能力
- 提出结构化压力测试协议（含 2008 GFC、2020 COVID、2022 加息冲击、2025 关税/地缘事件等情景）

### 关键发现
- VaR 定义为损失分布的 α-分位数，满足平移不变性和正齐次性但**不满足次可加性**，因此非一致性风险度量（Artzner et al. 1999）；ES/CVaR 定义为 ES_α = (1/(1−α))∫_α^1 VaR_u du，是满足全部四公理的一致性风险度量 [Artzner et al. (1999)](https://people.math.ethz.ch/~delbaen/ftp/preprints/CoherentMF.pdf "Coherent Measures of Risk, Mathematical Finance")
- 最大回撤 MDD = max_{0≤s≤t≤T}[W(s)−W(t)]，路径依赖但非一致性度量；Ulcer Index = √(1/n·Σ D_i²) 对大回撤施加更重惩罚；Conditional Drawdown-at-Risk (CDaR) 由 Chekhlov-Uryasev-Zabarankin (2005) 提出，是 CVaR 在回撤域的类比，β→1 退化为 MDD、β→0 退化为平均回撤 [Chekhlov et al. (2005)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=223323 "Portfolio Optimization with Drawdown Constraints")
- Acerbi & Szekely (2014) 提出三种 ES 无模型回测方法（Z₁/Z₂/Z₃），比 Basel VaR 检验更强，证明可诱导性（elicitability）对监管风险标准选择无关 [Acerbi & Szekely (2014)](https://www.msci.com/documents/10199/238916/Research_Insight_Backtesting_Expecting_Shortfall_December_2014.pdf "Backtesting Expected Shortfall, MSCI")
- FRTB 以 97.5% ES 取代 99% VaR 作为内部模型法的市场风险资本计量标准，要求直接在 10 日视野下估计（禁止 √t 缩放），并按资产类别设置差异化流动性视野（10–120 个交易日）；Basel III 监测报告估计 FRTB 将使 Group 1 银行加权平均市场风险资本增加 63.2% [BPI](https://bpi.com/why-is-the-frtb-expected-shortfall-calculation-designed-as-it-is/ "FRTB ES Calculation Design")
- 全球 FRTB 落地时间线分化：截至 2025 年 9 月仅 8/20 巴塞尔成员辖区完成最终 Basel III，EU/UK 推迟至 2027 年 1 月，美国 Basel III Endgame 尚未定稿 [European Parliament EGOV (2025)](https://www.europarl.europa.eu/RegData/etudes/IDAN/2025/773694/ECTI_IDA(2025)773694_EN.pdf "The implementation of Basel III, September 2025")
- CTA 策略呈正偏度和"危机 Alpha"特性（Man AHL 研究证实极端市场分位下表现最优），但在 V 型反转中易受鞭打 [Man Group AHL](https://www.man.com/insights/trend-following-equity-and-bond-crisis-alpha "Trend Following: Equity and Bond Crisis Alpha")
- 统计套利/股票市场中性策略面临拥挤驱动的左尾风险，2026 年初 prime broker 数据显示系统性多空在拥挤头寸和因子反转中遭受自 10 月以来最大短期回撤 [HedgeCo (2026)](https://www.hedgeco.net/news/01/2026/2026-challenging-for-quant-hedge-funds.html "2026 Challenging for Quant Hedge Funds")
- 多因子量化在 2018 年 6 月至 2020 年 8 月经历 27 个月量化危机，为 50 年来首次动量因子无法补偿价值因子损失 [Blitz (2021)](https://www.robeco.com/docm/docu-202102-the-quant-crisis-of-2018-2020-cornered-by-big-growth.pdf "The Quant Crisis of 2018–2020, JPM")
- 2025 年 4 月 "Liberation Day" 关税冲击为政策黑天鹅，打破量化模型历史相关性假设；宏观对冲基金当月亏损 2.7%（等同 2023 年 3 月区域银行危机） [Reuters (2025)](https://www.reuters.com/business/finance/macro-hedge-funds-mauled-april-mcgeever-2025-05-08/ "Macro hedge funds mauled in April 2025")
- Zabarankin-Pavlikov-Uryasev (2022) 提出 Drawdown Beta，以 Expected Regret of Drawdown (ERoD) 为风险度量定义 CAPM 类比，实证显示比标准 Beta 对回撤更敏感 [Zabarankin et al. (2022)](http://uryasev.ams.stonybrook.edu/wp-content/uploads/2021/10/Drawdown_Portfolio_Optimization_Problems_and_Drawdown_Betas.pdf "Drawdown Beta and Portfolio Optimization")
- IOSCO 2025 工作计划纳入系统性压力测试方法论讨论，覆盖对冲基金和另类投资基金 [IOSCO (2025)](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD789.pdf "2025 IOSCO Work Program")；SEC Form PF 修正案（2024 年 2 月生效）要求大型对冲基金顾问在 72 小时内报告超过 NAV 20% 的非常损失等事件 [SEC (2026)](https://www.sec.gov/files/2025-pf-report-congress.pdf "Form PF Annual Staff Report")
- Resonanz Capital 2026 年提出五桶分类法尽调框架，强调量化策略压力测试应超越宏观压力、纳入微观结构压力（轧空、流动性缺口、因子崩溃） [Resonanz Capital (2026)](https://resonanzcapital.com/insights/quant-hedge-funds-in-2026-a-due-diligence-framework-by-strategy-type "Quant Hedge Funds in 2026: A Due Diligence Framework")
- 建议标准化四情景压力测试协议：(1) 2008 GFC——信用传染与流动性冻结；(2) 2020 COVID——23 交易日 −34%、跨资产相关性飙升；(3) 2022 加息冲击——联邦基金利率 16 个月从 0% 升至 5.25%；(4) 2025 关税/地缘——政策黑天鹅与模型外样本韧性

### 可用图片
- 无本地可用图片

### 仍需补充
- Chekhlov-Uryasev-Zabarankin (2005) CDaR 原文 PDF 未能直接获取，定义依赖 SSRN 摘要与二手引用
- Breuer & Csiszár (2023) 反向压力测试方法论全文受 Wiley 付费墙限制
- 2020 年 3 月 COVID 期间主要量化基金（Citadel、D.E. Shaw、Two Sigma）具体回撤数据无 T1/T2 来源
- RIEF "Liberation Day" 亏损约 16 亿美元 / ~8% 回撤的数据来源为 T4（Medium）；Bloomberg 标题确认量化基金抛售但全文付费
- 尚未发现 2025–2026 年同行评审的、专门面向多策略对冲基金的完整统一压力测试框架学术论文


## Chapter 4：Transaction Costs, Market Impact, and Execution Quality Assessment
### 研究目标
- 构建涵盖显性成本、隐性成本和延迟相关成本的统一成本评估层
- 调查主流市场影响模型（Almgren-Chriss、传播子/瞬态影响模型、ML-based impact estimators）及其对不同频率策略的适用性
- 定义执行质量指标（Implementation Shortfall、VWAP 偏差、参与率基准）

### 关键发现
- Almgren-Chriss (1999/2001) 将最优执行建模为均值-方差优化，最优轨迹 x_j = sinh(κ(T−t_j))/sinh(κT)·X；假设线性永久影响 g(v)=γv 与临时影响 h(v)=ε+ηv；局限性在于线性影响假设在大宗元指令下被经验否定 [Almgren & Chriss (1999)](https://quantitativebrokers.com/s/Optimal-Execution-of-Portfolio-Transaction-_-AlmgrenChriss-1999.pdf "Almgren-Chriss 1999 working paper")
- Kyle (1985) λ 模型预测线性永久影响 ΔP=λ·Q，但经验上元指令影响遵循平方根律 ΔP∝σ·√(Q/V)；Bouchaud (2024) 称其为"过去 30 年最令人着迷的稳健经验规律"，2024 年 Sato & Kanazawa 用东京证券交易所 ID 级数据确认指数 δ≈1/2 [Bouchaud (2024)](https://bouchaud.substack.com/p/the-square-root-law-of-market-impact "The Square-Root Law of Market Impact")
- 传播子/瞬态影响模型（Bouchaud-Farmer-Lillo）将中间价建模为过去交易符号的加权和，核函数 G(t)~t^{−β}（β≈0.5–0.7）呈幂律衰减，捕获单笔交易影响的短暂特性；Said (2022) 提出统一粗粒化理论以单参数 ρ 解释供需均衡与平方根律 [Taranto et al. (2016)](https://arxiv.org/abs/1602.02735 "Propagators: Transient vs. History Dependent Impact")
- Abbade & Costa (2026) 提出 MACE 框架，集成非线性市场影响模型于 RL 交易环境，证明成本模型选择实质性改变 DRL 算法排名（AC 成本模型 vs 固定 10 bps：日均成本从 $200k 降至 $8k、换手率从 19% 降至 1%） [Abbade & Costa (2026)](https://arxiv.org/abs/2603.29086 "Realistic Market Impact Modeling for RL Trading Environments")
- Implementation Shortfall (Perold 1988) = 纸面组合回报 − 实际组合回报；Hendershott-Jones-Menkveld (2013) 将其分解为流动性成本、信息成本和时机成本三部分，实例中总 IS 262 bps = 48 bps 流动性 + 219 bps 信息 + (−5 bps) 时机 [Hendershott et al. (2013)](https://faculty.haas.berkeley.edu/hender/chapter_ELOv5.pdf "Implementation Shortfall with Transitory Price Effects")
- 执行基准：到达价格（信号生成时中间报价）、VWAP（成交量加权均价）、TWAP（时间加权均价）、参与率（POV）；Talos (2025) 案例显示 TWAP 策略 1000+ 笔母单（$10 亿名义）到达滑点 13 bps 但优于市场 TWAP/VWAP [Talos (2025)](https://www.talos.com/insights/execution-insights-through-transaction-cost-analysis-tca-benchmarks-and-slippage "Talos – TCA Benchmarks and Slippage, April 2025")
- TCA 行业格局：TT TCA（前 Abel Noser）年处理约 $50 万亿交易本金，2026 年获 TradingTech Insight 欧洲最佳 TCA 工具奖；OneTick 集成 ML/MLOps 流水线用于预测性成本建模，2025 年获 RegTech Insight 欧洲最佳 TCA 方案；其他主要供应商包括 Virtu、BestX、KX [Trading Technologies (2026)](https://www.prnewswire.com/news-releases/trading-technologies-wins-best-tca-tool-and-best-sell-side-oms-at-tradingtech-insight-europe-awards-2026-302699498.html "TT wins Best TCA Tool 2026")
- 交易成本随频率剧变：HFT 成本以交易所费用和价差捕获为主，日内换手可超 100x；Novy-Marx & Velikov (2016, RFS) 发现月换手率低于 50% 的异象通常可存活于交易成本中，更高换手率的极少存活；AQR 实际交易成本比学术 TAQ 估计低一个数量级，动量策略盈亏平衡容量达 $561.6 亿（vs 学术估计 ~$50 亿） [Novy-Marx & Velikov (2016)](https://academic.oup.com/rfs/article-abstract/29/1/104/1844518 "A Taxonomy of Anomalies and Their Trading Costs, RFS")
- 回测嵌入交易成本最佳实践：使用非线性成本模型（非固定 bps）、建模策略自身交易的永久影响、防范前瞻偏差、模拟成交率退化、将策略参与率限制在日均成交量的 5–15%
- 交易成本分类法：显性（佣金、交易所费用、融资）、隐性（买卖价差、滑点、市场影响）、延迟相关（信号延迟、成交率退化、逆向选择）

### 可用图片
- 无本地可用图片

### 仍需补充
- Almgren et al. (2005) 永久/临时影响参数的经验校准论文未获取
- Kyle (1985) 原始 Econometrica 论文全文未直接访问
- Perold (1988) "The Implementation Shortfall" 原文（6 页）未直接访问，定义依赖 Hendershott et al. 复述
- Gârleanu & Pedersen (2013) 动态组合交易与二次成本的闭式解——将执行理论与组合级成本嵌入桥接
- 2025–2026 年 TCA 市场规模或机构采用率的 T1/T2 量化数据未找到


## Chapter 5：Regime Adaptability, Robustness, and Strategy Capacity Evaluation
### 研究目标
- 使用 HMM、变点检测、聚类方法等形式化市场体制分类
- 定义策略跨体制稳健性指标（条件 Sharpe、体制切换衰减率、条件回撤）
- 估算策略容量天花板并将可扩展性纳入评价维度

### 关键发现
- Hamilton (1989) 体制转换模型将观测变量 y_t 置于隐含离散 Markov 链 s_t 驱动下，过滤概率 ξ_{j,t}=Pr(s_t=j|Ω_t;θ) 通过矩阵递推迭代计算，扩展至 N 状态和向量观测不增加计算复杂度 [Hamilton (2005)](https://econweb.ucsd.edu/~jhamilto/palgrav1.pdf "Regime-Switching Models, Palgrave Dictionary")
- Two Sigma 使用 GMM 对 17 因子透镜输入进行聚类，识别四种数据驱动市场状态：Crisis、Steady State、Inflation、Walking on Ice，自 1971 年以来 Steady State 频率最高 [Two Sigma (2021)](https://www.twosigma.com/articles/a-machine-learning-approach-to-regime-modeling/ "A Machine Learning Approach to Regime Modeling")
- SSGA 2025 年 2 月研究采用 t 分布混合模型+GARCH、23 个特征（含 CDS 价差、期权偏度、经济不确定性指数），在 1995–2024 美国数据上识别四体制：Emerging Expansion (42.3%)、Robust Expansion (25.4%)、Cautious Decline (19.2%)、Market Turmoil (13.2%)，Turmoil 体制对 NBER 衰退和 S&P 500 最大回撤的 F1 ≈ 73–78% [SSGA (2025)](https://www.ssga.com/library-content/assets/pdf/global/pc/2025/decoding-market-regimes-with-machine-learning.pdf "Decoding Market Regimes with Machine Learning")
- PELT 算法（Killick et al. 2012）以 O(n) 实现精确多变点检测，2025 年 ACM 研究在金融时间序列上优化其惩罚参数 [ACM (2025)](https://dl.acm.org/doi/10.1145/3773365.3773532 "Change-Point Detection in Financial Time Series Using PELT")；2025 年 MDPI Systems 论文以拓扑数据分析检测 2011 欧债、2016 Brexit、2020 COVID、2022 加息四次极端事件 [MDPI Systems (2025)](https://www.mdpi.com/2079-8954/13/10/875 "Change Point Detection Using TDA")
- 条件 Sharpe ratio S_t ≡ E_t(R−R_f)/SD_t(R−R_f)；Tang & Whitelaw (2011) 估计月度条件 Sharpe 范围约 −0.2 至 0.9，年化峰谷变动超 0.85；条件均值（非波动率）是驱动 Sharpe 变化的主因 [Tang & Whitelaw (2011)](https://pages.stern.nyu.edu/~rwhitela/papers/tvsharpe.pdf "Time-Varying Sharpe Ratios and Market Timing")
- Singha (2025) 发现体制条件因子（仅在漂移体制激活价值和短期反转信号）实现样本外 Sharpe>13，年化回报 158.6%/波动率 12.0%/最大回撤 −11.9%，容量估计 $1–5 亿（$10 亿时回报压缩至 33.6%） [Singha (2025)](https://arxiv.org/abs/2511.12490 "Discovery of a 13-Sharpe OOS Factor, arXiv")
- SSGA 体制分析显示美股月均回报在 Expansion 体制 +2.1%–+2.9%，在 Turmoil 体制 −3.4%；长期美债在 Turmoil 中月均 +1.11%；回报离散度在 Turmoil 中约为 Expansion 的两倍 [SSGA (2025)](https://www.ssga.com/library-content/assets/pdf/global/pc/2025/decoding-market-regimes-with-machine-learning.pdf "Decoding Market Regimes with Machine Learning")
- Vangelisti (2006, GMO) 提出三种容量定义：阈值容量（alpha 不低于目标）、财富最大化容量（alpha×AUM 最大化）、终端容量（净 alpha=0）；GMO 新兴市场策略模拟显示 AUM 从 $10 亿升至 $200 亿时总 alpha 从 11.1% 降至 7.86%、交易成本从 1.68% 升至 2.62%，阈值容量约 $220 亿 [Vangelisti (2006)](https://sanfrancisco.qwafafew.org/wp-content/uploads/sites/9/2017/01/sf-20041018-vangelisti.pdf "The Capacity of an Equity Strategy, GMO")
- Naik-Ramadorai-Stromqvist (2007) 对 7610 只基金（1994–2004）的实证表明，在 8 个策略类别中有 4 个（相对价值、方向性交易、新兴市场、固定收益）资金流入统计显著先于 alpha 下降；年度流入增加 10% 对应后续月度 alpha 下降 36–94 bps [Naik et al. (2007)](https://www.researchgate.net/publication/227358514_Capacity_Constraints_and_Hedge_Fund_Strategy_Returns "Capacity Constraints and Hedge Fund Strategy Returns, EFM")
- 按策略类型的典型容量范围：HFT $5000 万–$5 亿、统计套利 $5 亿–$50 亿、系统性多因子 $100–$500 亿+、宏观/CTA $10–$200 亿
- El Badraoui et al. (2026) 实施 5 折步进验证协议（4 年训练/1 年验证/1 年测试），严格保证体制后验概率和情绪特征在训练窗口内计算无泄漏；体制感知代理方法将 NSGA-3 Sharpe 从 0.780 提升至 1.153（Δ=+0.373），Jobson-Korkie 检验 p<0.01 [El Badraoui et al. (2026)](https://link.springer.com/article/10.1007/s41060-026-01066-0 "Toward a unified agentic framework for regime-aware portfolio optimization, 2026")
- 2026 年 3 月 arXiv 预印本提出基于因果 Wasserstein HMM 的可解释体制感知投资框架，强调因果约束以防止前瞻偏差 [arXiv 2603.04441](https://arxiv.org/abs/2603.04441 "Explainable Regime Aware Investing, March 2026")
- 稳健性评价指标：条件 Sharpe ratio（按体制分别计算）、体制转换衰减率（转换后 N 天累积 alpha 衰减斜率）、条件回撤（体制切换窗口内最大回撤）、Regime Classification Measure (RCM)

### 可用图片
- 无本地可用图片

### 仍需补充
- Robotti (2024) "Comparing factor models under regime switching" 全文未获取，含体制特定切线组合间相关性指标 ρ_{AB,ℓ}
- HFT 容量天花板的 2025–2026 年微观结构实证数据（按交易所/资产类别细分）
- Perold & Salomon (1991) 原文未直接访问，容量框架数学规格依赖间接引用
- "体制转换衰减率"为建议构造而非既有学术术语，需搜索类似形式化指标（如 alpha half-life post-regime-switch）
- Caron (2024) 贝叶斯在线变点检测论文（Communications in Nonlinear Science）未完整访问


## Chapter 6：Overfitting Detection, Out-of-Sample Validation, and Statistical Significance
### 研究目标
- 构建框架的"认知完整性"维度：防范数据挖掘和过拟合绩效声称的测试与诊断体系
- 覆盖 CSCV、PBO、Deflated Sharpe Ratio、多重检验校正、Walk-forward 验证、Purged k-fold 交叉验证、置换检验等
- 调查 2025–2026 年 AI 策略验证的新进展

### 关键发现
- CSCV（Bailey, Borwein, López de Prado, Zhu 2017）将 N 个策略试验的绩效矩阵 T×N 按行分为 S 个子矩阵，穷举 C(S,S/2) 组合各取半为 IS/OOS，记录 IS 最优策略在 OOS 的相对排名 ω̄_c 并取 logit λ_c=ln[ω̄_c/(1−ω̄_c)]；PBO = ∫_{−∞}^0 f(λ)dλ，即 IS 最优策略 OOS 排名低于中位数的组合比例；推荐 S=16（4 年日数据→季度分区，生成 12,780 logits），拒绝阈值 PBO>0.05 [Bailey et al. (2017)](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf "The Probability of Backtest Overfitting, JCF")
- DSR = Z[(SR̂−SR₀)√(T−1) / √(1−γ̂₃SR̂+(γ̂₄−1)/4·SR̂²)]，SR₀ 为 K 次独立试验下期望最大 Sharpe（对数增长于 K）；PBO 提供非参数选择过程诊断，DSR 提供参数化单策略 Sharpe 校正，二者互补；López de Prado (2019) 实例：6385 次试验聚类为 K=4，DSR≈1.0 [Bailey & López de Prado (2014)](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf "The Deflated Sharpe Ratio, JPM")；[López de Prado (2019)](https://www.aqr.com/-/media/AQR/Documents/Journal-Articles/JFDS_Winter2019_A-Data-Science-Solution-to-Multiple-Testing-Crisis---Lopez_de_Prado.pdf "A Data Science Solution to the Multiple-Testing Crisis, JFDS")
- Harvey, Liu & Zhu (2016) 系统考察 316 个因子（1967–2012 年 313 篇论文），确立新因子 t 统计量≥3.0 的最低门槛；Bonferroni（FWER 单步）调整后基准达 3.78，BHY（FDR 1%）为 3.39；计入隐性未发表检验后升至 3.18–3.96；FWER 在金融中比 FDR 更合适——单个假阳性可影响万亿美元配置 [Harvey et al. (2016)](https://people.duke.edu/~charvey/Research/Published_Papers/P118_and_the_cross.PDF "…and the Cross-Section of Expected Returns, RFS")
- Purged k-fold CV（López de Prado 2018）从训练集中清除与测试集标签形成窗口重叠的观测，Embargo 机制进一步移除测试折后的缓冲带；CPCV 扩展为 C(N,k) 组合并生成 φ[N,k]=(k/N)·C(N,k) 条回测路径分布 [López de Prado (2018)](https://en.wikipedia.org/wiki/Purged_cross-validation "Purged cross-validation")
- Walk-forward 分析三变体：锚定（扩展窗口）、滚动（固定窗口）、静态（单次拆分）；Monte Carlo 回测需指定数据生成过程（DGP），合成数据方面 Joubert et al. (2024) 构建综合合成控制环境（Heston SV + Merton 跳扩散 + 投机泡沫 + Markov 体制转换） [Joubert et al. (2024)](https://www.hillsdaleinv.com/uploads/The_Three_Types_of_Backtests.pdf "The Three Types of Backtests, JPM")；[Joubert et al. (2024, KBS)](https://www.sciencedirect.com/science/article/abs/pii/S0950705124011110 "Backtest overfitting in the ML era, Knowledge-Based Systems")
- 2025 年 12 月 arXiv 论文提出金融表格 ML 的对抗鲁棒性流水线（FGSM/PGD，ε=0.05），微小扰动使 AUC 降约 10.6%、Portfolio Expected Loss 增约 5%；SHAP 稳定性常先于 AUROC 退化，可作为预警指标 [arXiv (2025)](https://arxiv.org/html/2512.15780v1 "Adversarial Robustness in Financial ML, December 2025")
- NIST AI 100-2 E2025（2025 年 3 月）建立对抗性 ML 攻击与缓解标准分类法，金融监管机构和模型风险管理团队正在采纳 [NIST (2025)](https://csrc.nist.gov/pubs/ai/100/2/e2025/final "NIST AI 100-2 E2025")
- Sheppert (2026) Frontiers in AI 综述整合约 95 项研究（1943–2026），将过拟合缓解技术分为五族：参数、训练、数据、集成、目标正则化 [Sheppert (2026)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1794271/full "Techniques for Mitigating Overfitting, Frontiers in AI")
- 因果因子投资：López de Prado (2023) 和 López de Prado & Zoonekynd (2024) 要求在运行任何回测前先创建描述异象的因果图，从先验理论而非后验模式出发，约束搜索空间并降低假阳性概率 [Joubert et al. (2024)](https://www.hillsdaleinv.com/uploads/The_Three_Types_of_Backtests.pdf "The Three Types of Backtests, JPM")
- 文献趋同的多重门控诊断框架：(1) PBO<0.05；(2) DSR>0.95；(3) 因子 t-stat≥3.0；(4) MinTRL 满足（Bailey & López de Prado 2012 公式）；(5) 置换检验 p<0.05；(6) IS 最优策略 OOS 表现一阶随机占优其余策略分布；金融场景偏好 FWER（Bonferroni/Holm/DSR）而非 FDR

### 可用图片
- 无本地可用图片

### 仍需补充
- 2025–2026 年专门应用于量化策略验证流水线的 ML 可解释性工具（LIME、SHAP 等）的详细调研
- 头部量化机构（AQR、ADIA、Two Sigma）在生产环境中对 CPCV/PBO 的校准实践（大部分为专有信息）
- EU AI Act 对算法交易模型验证的具体要求和执行时间线
- PBO 框架与结构性断点的交互——原框架承认数据边界外的断点无法捕获，可能存在更新的体制感知扩展


## Chapter 7：Composite Scoring Methodology and Practical Framework Implementation
### 研究目标
- 将前述各维度综合为可操作的复合评分与排名方法
- 解决异质指标的标准化（z-score、排名百分位、min-max）、权重方案（等权、PCA）、聚合函数（TOPSIS、PROMETHEE）
- 设计分层评分架构，并提供风格化工作示例
- 讨论治理问题：版本控制、定期再校准和机构采用的透明度要求

### 关键发现
- TOPSIS 以正负理想解的欧氏距离排序，闭合系数 C_i=D_i^−/(D_i^++D_i^−)∈[0,1]；优点为计算简单、几何直观，缺点为对标准化方法敏感且存在排名反转 [TOPSIS guide (2023)](https://www.researchgate.net/publication/374540287_A_comprehensive_guide_to_the_TOPSIS_method_for_multi-criteria_decision_making "Comprehensive guide to TOPSIS, ResearchGate")
- PROMETHEE（Brans & Vincke 1985）构建成对偏好指数 π(a,b)=Σw_j·P_j(a,b)，净流 φ(a)=φ^+(a)−φ^−(a) 给出完整排名；GAIA 主成分可视化模块支持交互灵敏度分析；优点为偏好建模透明、无分布假设，缺点为对阈值参数敏感且 O(n²×k) 计算复杂度 [Brans & Mareschal](https://www.cin.ufpe.br/~if703/aulas/promethee.pdf "PROMETHEE Methods")
- ELECTRE-TRI 支持将策略分入有序类别（如"投资/持有/回避"），具有否决阈值的非补偿特性；Doumpos et al. (2021) 在雅典交易所实证中产生统计显著 alpha [Doumpos et al. (2021)](https://link.springer.com/article/10.1186/s40854-021-00318-1 "ELECTRE-TRI for stock portfolio, Financial Innovation")；AHP（Saaty 1977）通过层次结构和一致性比率 CR>0.10 标记不一致判断，AHP-PROMETHEE 混合方案结合结构化权重获取与丰富偏好建模 [Garousi Mokhtarzadeh et al. (2023)](https://www.mdpi.com/2227-7072/11/1/46 "AHP-PROMETHEE for Portfolio, JRFM")
- Pätäri et al. (2018, EJOR) 系统比较 TOPSIS、PROMETHEE、ELECTRE、AHP、SAW 在美股组合选择中的表现，MCDA 选择的组合年化超额收益优于基准 2–4%；TOPSIS 和 PROMETHEE 表现最稳定 [Pätäri et al. (2018)](https://www.sciencedirect.com/science/article/abs/pii/S0377221717307129 "Comparison of MCDA methods, EJOR")
- Morningstar 星级评级基于 CRRA 效用函数（γ=2）计算 MRAR，在同业组内按 MRAR 百分位分配星级（强制钟形分布：5★=top 10%、4★=22.5%、3★=35%、2★=22.5%、1★=bottom 10%），总评为 3/5/10 年评级的加权平均（20%/30%/50%） [Morningstar Rating Methodology (2021)](https://www.morningstar.com/content/dam/marketing/shared/research/methodology/771945_Morningstar_Rating_for_Funds_Methodology.pdf "Morningstar Rating for Funds")
- Morningstar Scorecards 提供更丰富的多维复合：12 个因子、5 个支柱（Process/Performance/People/Parent/Price），权重通过线性回归和随机森林在 22 万+观测（14 年无存活偏差数据）上标定，Price（费率）获最高权重；前 30% 评分基金在后续 5 年跑赢类别平均的概率 78% [Morningstar Scorecards (2019)](https://morningstardirect.morningstar.com/clientcomm/Fund_Scorecards_Methodology.pdf "Scorecard Methodology")
- MSCI ESG Ratings 展示三层分层架构：33 个 Key Issue Score (0-10) → E/S/G 支柱得分 → 行业调整最终分（以第 5/95 百分位标准化）→ AAA–CCC 七级字母评级；治理支柱权重下限 33%；权重设定采用 2×3 框架（影响级别×时间跨度） [MSCI ESG Ratings Methodology (2024)](https://www.msci.com/documents/1296102/34424357/MSCI+ESG+Ratings+Methodology.pdf "MSCI ESG Ratings, April 2024")
- OECD 复合指标手册 (2008) 建议至少测试两种标准化方案（z-score vs min-max vs rank-percentile）；z-score 对异常值敏感但保留分布信息，min-max 压缩极端值范围，rank-percentile 对异常值稳健但丢弃差异幅度 [OECD Handbook (2008)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf "OECD Handbook on Constructing Composite Indicators")
- 权重方案分类（Greco et al. 2018）：等权（最常见但"被普遍认为是错误的"）、专家获取（BAP、AHP——指标超 10 个时认知过载）、数据驱动（PCA——反映统计方差而非概念重要性、熵——奖励区分度但可能低估普遍重要但同质的指标、DEA/BoD——给每个单元最有利权重）；结论为无单一最优权重方案、多方案稳健性测试必不可少 [Greco et al. (2018)](https://link.springer.com/article/10.1007/s11205-017-1832-9 "On the Methodological Framework of Composite Indices, Social Indicators Research")
- 聚合函数补偿性谱：加权线性（全补偿）→ 几何均值（部分补偿，HDI 2010 年切换）→ 超级化方法/ELECTRE/PROMETHEE（非补偿）；加权线性中权重充当替代率而非重要性系数（Paruolo et al. 2013） [Greco et al. (2018)](https://link.springer.com/article/10.1007/s11205-017-1832-9 "Social Indicators Research")
- 维度间相关与重复计算处理：PCA/因子分析识别潜在维度，对共线指标在聚合前取平均或降低权重；Morningstar Scorecards 通过 Pearson 相关检验和随机森林变量重要性分析确认无单一因子与未来表现强相关，但弱相关因子组合产生单调预测 [Morningstar Scorecards (2019)](https://morningstardirect.morningstar.com/clientcomm/Fund_Scorecards_Methodology.pdf "Scorecard Methodology")
- 稳健性检验金标准为 Sobol' 方差分解：一阶灵敏度指数 S_i=V[E(y|x_i)]/V(y)；COINr 框架对 ASEM 可持续连接指数的 Monte Carlo 分析（500+ 次复制，权重扰动 ±25%）显示标准化选择解释排名方差>50%，权重~23%，插补<4%；逐支柱移除测试显示单个支柱移除可导致平均排名变化达 4 倍差异 [COINr (2022)](https://bluefoxr.github.io/COINrDoc/sensitivity-analysis.html "COINr Sensitivity Analysis")
- S&P 企业信用评级方法论展示机构分层架构：业务风险+财务风险→锚定分→修正因子（多元化、资本结构、流动性等）→独立信用画像→叠加集团/政府支持→发行人信用评级 [S&P Global Ratings](https://www.spglobal.com/content/dam/spglobal/ratings/en/documents/pdfs/041019_howweratenonfinancialcorporateentities.pdf "How We Rate Nonfinancial Corporate Entities")
- 治理最佳实践：Morningstar 维护方法论变更日志，MSCI 每年 Q4 审查 Key Issue 选择和权重并提供 30 天客户咨询期；OECD 手册要求披露权重理由、聚合方法和灵敏度分析结果作为机构采用前提
- Xidonas et al. (2025, EJOR) 将 MCDA 与前瞻性预测集成用于组合构建，证明 MCDA 评分包含超越原始数据和预测本身的增量信息，具有领先指标特性 [Xidonas et al. (2025)](https://ideas.repec.org/a/eee/ejores/v321y2025i2p516-528.html "MCDA + forecasting for portfolio selection, EJOR 2025")
- 建议的量化策略复合评分框架流程：(1) 维度评分——5–7 个支柱（风险调整回报、尾部风险、交易成本效率、体制适应性、过拟合检测）；(2) 标准化——rank-percentile 以保稳健；(3) 权重——等权基线+熵/PCA 调整+AHP 专家验证；(4) 聚合——几何均值限制补偿性；(5) 稳健性——Monte Carlo 权重扰动 ±25% + 逐支柱移除；(6) 治理——版本化、年度再校准、透明度报告

### 可用图片
- 无本地可用图片

### 仍需补充
- 2025–2026 年 SSRN/arXiv 上专门将 MCDA 复合评分应用于对冲基金或 CTA 策略评估的论文
- S&P 基金质量评级方法论文档（非公开）
- 使用实际或风格化策略表现数据的数值工作示例（Chapter 7 概念框架需配以表格化假设数字）
- OECD 手册第 5 章 Monte Carlo 不确定性框架的完整细节


# Section 2：给 Write 阶段的执行建议

## 语气与风格
- 全文采用"实务+学术"混合语气：正式且循证，同时提供机构量化团队可执行的实施指导
- 框架不做策略优劣判断，只提供评价工具；避免出现"最优策略"等规范性结论

## 指标与定义规范
- 框架推荐的每个指标或测试必须附带数学定义（紧凑符号即可）、关键假设和至少一个已知局限
- 明确区分普适性指标（Sharpe、Omega、GPR——适用于所有策略）与策略条件指标（Sortino、Calmar、Treynor、IR——受频率/资产类别/持仓周期约束），在首次出现时即标注适用范围
- DSR 在 Chapter 2（指标属性）和 Chapter 6（过拟合检测）中均有涉及——确保两处叙述互补而非重复：Chapter 2 聚焦其作为 Sharpe 校正的统计属性，Chapter 6 聚焦其在多重检验框架中的诊断用途

## 分类体系一致性
- 策略类型命名须与 Chapter 1 建立的六大族群分类（多因子、统计套利、HFT/做市、CTA/趋势跟踪、ML 驱动、混合/多策略）保持全文一致
- Chapter 1 的 Aurum 五子策略分类与 CCMR 七类分类并存——在后续章节中以 Aurum 的量化子策略分类为主线，CCMR 分类用于更广泛的对冲基金行业语境

## 引用与时间口径
- 优先引用 2025–2026 年学术论文和行业报告；基础文献（Sharpe 1966、Almgren-Chriss 2001、Bailey-López de Prado PBO 2014 等）以先行研究定位
- 时间口径：以 2026-04-03 为锚点，回顾约 2025 年 4 月至 2026 年 4 月，必要时引用更早的奠基文献

## 可视化与可读性
- 大量使用表格和比较矩阵：建议至少包含以下核心表格——(1) 策略族群特征矩阵（Ch1）；(2) 风险调整指标属性比较表（Ch2）；(3) 尾部风险指标一致性属性对比表（Ch3）；(4) 交易成本组件与策略频率关系矩阵（Ch4）；(5) 复合框架维度×策略适用性矩阵（Ch7）

## 跨章节协调要点
- Chapter 2 的 Smetters-Zhang 不可能定理（偏好无关的排序度量对一般非正态分布不存在）是 Chapter 7 选择多维度复合而非单一指标路线的理论基础——需在 Chapter 7 开篇引用
- Chapter 3 的标准化四情景压力测试协议需与 Chapter 5 的体制分类方法对齐——每个压力情景应能映射到至少一个 Chapter 5 定义的体制状态
- Chapter 4 的交易成本模型参数（Almgren-Chriss γ、η）应在 Chapter 7 的工作示例中被实际使用，体现框架各维度的端到端集成
- Chapter 6 的多重门控诊断阈值（PBO<0.05、DSR>0.95、t-stat≥3.0）应作为 Chapter 7 复合评分的准入条件（"认知完整性门槛"），即策略通过 Chapter 6 检验后方可进入复合评分流程
- Chapter 7 须含可复现的数值工作示例，使用 5–6 个风格化策略（覆盖主要族群）穿越全部评价维度

## 设计选择透明度
- 对所有设计选择（默认权重方案、标准化方法、聚合函数、统计阈值）须透明陈述理由并注明替代方案
- 建议在 Chapter 7 中包含一个灵敏度分析段落，展示权重扰动 ±25% 和标准化方法切换对最终排名的影响
