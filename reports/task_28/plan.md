# Section 1：章节研究计划

## Chapter 1：传统药物评估的系统性困境——从多组学到个体异质性的未解难题

### 研究目标
- 阐明传统药物评估范式（从单靶点还原论到多组学整合）在系统性、宏观性评估药物对机体影响方面的根本能力边界：高维数据整合困难、跨尺度因果推断缺失、时间动态建模不足
- 量化呈现新药研发的效率危机：临床各阶段失败率、时间与成本壁垒、疗效不足作为首要终止原因的结构性根源
- 系统论述个体异质性（遗传多态性、表观遗传、肠道微生物组、免疫状态、合并用药、环境暴露等）如何导致药物响应的巨大个体间差异，并以典型案例（伊立替康、地高辛、华法林、ICIs）具象化呈现
- 论证临床试验的内在局限——RCT 设计报告群体平均效应、遮蔽个体响应异质性、罕见不良反应难以在试验阶段充分检测——与个体异质性问题的叠加效应
- 收束全章，提出核心需求命题：为何需要一种能够在多尺度上模拟药物系统性影响、并纳入个体差异变量的新计算范式

### 关键发现

**新药研发成本与时间壁垒**
- 一种新药从研发到获批上市的平均资本化总成本为 25.58 亿美元（2013 年美元），加入上市后研发成本则上升至 28.70 亿美元 [DiMasi et al. 2016](https://pubmed.ncbi.nlm.nih.gov/26928437/ "Innovation in the pharmaceutical industry: New estimates of R&D costs, J Health Econ 2016;47:20-33")
- Deloitte 2024 年度报告显示，全球 20 家最大制药企业开发一种药物的平均成本为 22.3 亿美元，2013–2024 年间研发成本复合年增长率为 6.44% [Deloitte 2024 报告](https://www.fiercebiotech.com/biotech/drug-development-cost-pharma-22b-asset-2024-plus-how-glp-1s-impact-roi-deloitte "Drug development cost pharma $2.2B per asset in 2024, Fierce Biotech 2025-03-25 转引Deloitte")
- 2025 年 JAMA Network Open 基于 268 家药企和 38 种 2019 年 FDA 批准新药的经济评估显示，经资本成本和终止项目调整后，新药研发成本中位数为 7.08 亿美元（IQR 2.47–14.2 亿美元），均值为 13.1 亿美元（SD 19.2 亿美元），表明成本分布高度右偏 [Mulcahy et al. 2025](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2828689 "Use of Clinical Trial Characteristics to Estimate Costs of New Drug R&D, JAMA Netw Open 2025;8:e2453275")
- 2010–2020 年间 FDA 批准的 405 种创新药的临床开发时间中位数为 8.3 年，典型创新药临床开发时间为 9.1 年（95% CI = 8.2–10.0 年）[Brown et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9869766/ "Clinical development times for innovative drugs, Nat Rev Drug Discov 2022;21:793-794")
- 2011–2020 年一种药物从 I 期进入市场的平均总时间为 10.5 年（I 期 2.3 年、II 期 3.6 年、III 期 3.3 年、监管审查 1.3 年）[BIO/QLS/Informa 2021](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf "Clinical Development Success Rates and Contributing Factors 2011-2020")

**临床试验各阶段失败率**
- 2011–2020 年间 9,704 个临床开发项目的总体 I 期到 FDA 批准成功率（LOA）仅为 7.9%；II 期→III 期转换成功率仅 28.9%（所有阶段中最低）[BIO/QLS/Informa 2021](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf "Clinical Development Success Rates and Contributing Factors 2011-2020")
- 18 家领先药企 2006–2022 年间 I 期到 FDA 新药首次批准的平均成功率为 14.3%（中位数 13.8%），企业间差异约 8%–23% [Drug Discovery Today 2025](https://www.sciencedirect.com/science/article/pii/S1359644625000042 "Benchmarking R&D success rates of leading pharmaceutical companies 2006-2022")
- Bowling et al.（2025 Nature Reviews Drug Discovery）对 2013–2023 年 3,180 例 II/III 期终止的更新分析显示：终止率从 ~11% 上升至 ~22%，翻了一番；战略和商业因素已超越临床疗效不足成为首要终止驱动因素 [Bowling et al. 2025](https://www.nature.com/articles/d41573-025-00208-6 "Analysis of phase II and phase III clinical trial terminations from 2013 to 2023, Nat Rev Drug Discov 2025")

**生物标志物预选效果**
- 采用患者预选生物标志物的临床试验 I 期 LOA 为 15.9%，是未使用生物标志物项目（7.6%）的两倍以上；II 期使用生物标志物成功率 46.3% vs 未使用 28.3% [BIO/QLS/Informa 2021](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf "Clinical Development Success Rates and Contributing Factors 2011-2020")

**FDA 药物基因组学标签**
- 截至 2026 年 3 月，FDA 官方"Table of Pharmacogenomic Biomarkers in Drug Labeling"共列出 676 条药物-生物标志物条目 [FDA官方数据](https://www.fda.gov/drugs/science-and-research-drugs/table-pharmacogenomic-biomarkers-drug-labeling "FDA Table of Pharmacogenomic Biomarkers in Drug Labeling")
- 2000–2020 年间约 25.6% 的 FDA 新药初始标签含药物基因组学信息，从 2000 年的 10.3% 增长至 2019 年的 33.9%；肿瘤药物占含药物基因组学标签新药的 49.4% [Kim et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8000585/ "Pharmacogenomic Biomarkers in US FDA-Approved Drug Labels 2000-2020, J Pers Med 2021;11:179")

**个体异质性的多维来源**
- 遗传因素（CYP2C9、CYP2C19、CYP2D6 等高度多态性药物代谢酶）可解释特定药物中 20%–95% 的个体间药代动力学和药效学变异 [Signal Transduct Target Ther 2024](https://www.nature.com/articles/s41392-023-01619-w "Drug-microbiota interactions: an emerging priority for precision medicine")
- 全球荟萃分析（>336,000 名受试者，318 项研究）显示 CYP2D6 非正常代谢表型全球平均概率 36.4%，CYP2C19 为 61.9%；地区间差异巨大（CYP2D6 从冈比亚 2.7% 到阿尔及利亚 61.2%）[Koopmans et al. 2021](https://www.nature.com/articles/s41398-020-01129-1 "Meta-analysis of probability estimates of worldwide variation of CYP2D6 and CYP2C19, Transl Psychiatry 2021;11:141")
- 肠道微生物组包含超过 100 万亿微生物和约 500 万个基因，微生物编码基因对人类血液中小分子代谢物的贡献高达 36% [Signal Transduct Target Ther 2024](https://www.nature.com/articles/s41392-023-01619-w "Drug-microbiota interactions: an emerging priority for precision medicine")
- 不同药物因个体异质性导致的响应率差异巨大：COX-2 抑制剂约 80%，肿瘤化疗约 25%，大多数药物 50%–75% [Signal Transduct Target Ther 2024](https://www.nature.com/articles/s41392-023-01619-w "Drug-microbiota interactions: an emerging priority for precision medicine")

**表观遗传对药物代谢的贡献**
- DNA 甲基化介导的 CYP3A4/CYP3A7 发育性开关解释了儿科与成人药物代谢的显著差异；利福平通过 PXR 激活改变 CYP3A4 启动子组蛋白修饰导致药物-药物相互作用引起的个体内代谢变异 [Jin & Zhong 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197210/ "Epigenetic Mechanisms Contribute to Intraindividual Variations of Drug Metabolism, Drug Metab Dispos 2023;51:749-763")
- 表观遗传信息的组织特异性（无法通过外周血检测肝脏表观遗传状态）使临床开发表观遗传生物标志物具有极高难度 [Jin & Zhong 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10197210/ "同上")

**微生物组影响药物响应的典型案例**
- 伊立替康：肠道微生物 β-葡萄糖醛酸酶将低毒代谢物重新转化为高毒 SN-38
- 地高辛：约 10% 患者中 *Eggerthella lenta* 将地高辛转化为无活性二氢地高辛
- 免疫检查点抑制剂：特定菌群（*Akkermansia muciniphila* 等）与更好的抗肿瘤响应相关
- 华法林：~50% 剂量变异可由 CYP2C9（~18%）和 VKORC1（~30%）解释 [CPIC华法林指南](https://files.cpicpgx.org/data/guideline/publication/warfarin/2011/21900891.pdf "CPIC Guidelines for Warfarin Dosing")；约 35% 响应延迟个体无法用已知遗传因素解释
（以上案例来自 [Signal Transduct Target Ther 2024](https://www.nature.com/articles/s41392-023-01619-w "Drug-microbiota interactions") 和 [Limdi et al. 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2757655/ "Influence of CYP2C9 and VKORC1 on warfarin dose")）

**RCT 设计遮蔽个体响应异质性的系统性证据**
- 2025 年 JAMA Network Open 系统评价（65 篇报告 / 162 项 RCT）：阳性试验中 5%–67% 患者预计无法获益或可能受到净伤害；阴性试验中 25%–60% 患者实际可能获益 [Selby et al. 2025](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2836695 "Predictive Modeling of Heterogeneous Treatment Effects in RCTs, JAMA Netw Open 2025;8:e2522390")

**多组学数据整合的技术挑战**
- 核心挑战包括：数据异质性、跨尺度关联缺失、计算可扩展性和生物学可解释性 [BioData Mining 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11954193/ "Network-based multi-omics integrative analysis methods in drug discovery")
- 传统"一个药物→一个靶点→一种疾病"范式无法覆盖药物与多靶点跨通路的系统性影响；即使采用多组学方法，仍无法实现从分子扰动到表型结果的全链条因果推断 [BioData Mining 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11954193/ "同上")

### 可用图片
（无——本地 /data/ 中无与本章直接相关的图片素材）

### 仍需补充
- Bowling et al. 2025 全文中疗效不足 vs 安全性 vs 战略因素的精确百分比分布（付费墙限制）
- Tufts CSDD 新一轮研发成本更新数据（预计 2025–2026 年发布）
- 表观遗传变异对药物响应影响的全局性量化估计值（文献中缺乏单一权威来源）
- 免疫状态差异对非肿瘤药物响应的更广泛量化数据（超越抗 TNF 治疗案例）

---

## Chapter 2：AI 基础模型技术图谱——面向药物影响模拟的模型族群与能力边界

### 研究目标
- 构建面向药物影响模拟的 AI 基础模型分类图谱，覆盖五大模型族群：生物医学大语言模型（BioGPT、Med-Gemini/MedGemma 系列等）、蛋白质语言模型（ESM 系列、AlphaFold 系列）、化学基础模型（nach0/Nach01、ChemBERTa 等）、单细胞/基因组基础模型（scGPT、scFoundation、Geneformer、Evo 2 等）、多模态生物医学模型（BiomedCLIP、Precious3GPT 等）
- 对每一族群阐明其技术原理（架构、训练数据规模与来源、核心创新点）、能力边界（擅长与不擅长的任务类型）和技术成熟度定位（学术研究/概念验证/早期商业化/临床验证）
- 横向评估五大族群对个体异质性的表征能力差异：哪些模型能够捕获个体间差异（如蛋白质序列变异对功能的影响、单细胞层面的个体特异性转录状态、遗传变异的功能效应预测），哪些模型仍基于"平均患者"假设运行
- 厘清各族群之间的互补关系与整合可能性，为后续章节（应用环节、系统级整合）提供技术基础

### 关键发现

**生物医学大语言模型（Biomedical LLM）**
- BioGPT（Microsoft, 2022）基于 GPT-2 medium 架构，347M 参数，在 15M 篇 PubMed 摘要上从头预训练；在 PubMedQA 问答基准上达到 78.2% 准确率（BioGPT-Large 1.5B 参数达 81.0%）[BioGPT 原始论文](https://arxiv.org/pdf/2210.10341 "BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining, arXiv:2210.10341v3, 2023")
- Med-Gemini（Google, 2024）在 MedQA（USMLE 风格）基准上达到 91.1% 准确率 SOTA；Med-Gemini-Polygenic 是首个能从基因组数据预测疾病和健康结局的语言模型，在 8 种健康结局上优于传统线性多基因评分 [Med-Gemini 官方博客](https://research.google/blog/advancing-medical-ai-with-med-gemini/ "Advancing medical AI with Med-Gemini, Google Research 2024")
- MedGemma（Google, 2025 年 5 月发布，2026 年更新至 v1.5）4B 多模态版本和 27B 文本版本；MedGemma 27B 在 MedQA 上达到 87.7%，推理成本仅为 DeepSeek R1 的十分之一；81% 的 AI 生成胸部 X 光报告被放射科医师评为临床可用 [MedGemma 官方博客](https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/ "MedGemma: Our most capable open models for health AI development, Google Research 2025")
- 能力边界：所有生物医学 LLM 主要处理文本模态，不能直接建模分子-蛋白质互作或细胞层面药物响应，核心价值在于知识推理、文献挖掘和辅助假设生成
- 技术成熟度：BioGPT 属于学术研究阶段；Med-Gemini/MedGemma 处于早期商业化阶段

**蛋白质语言模型（pLM）**
- ESM-3（EvolutionaryScale, 2024）最大 98B 参数，在 2.78B 条蛋白质序列（771B token）上训练，能同时在序列、结构和功能三个模态推理和生成；CAMEO 测试集 LDDT 达 0.880；成功生成全新荧光蛋白 esmGFP（与已知最近荧光蛋白仅 58% 序列一致性）[ESM-3 预印本](https://www.biorxiv.org/content/10.1101/2024.07.01.600583.full "Simulating 500 million years of evolution with a language model, bioRxiv 2024")
- AlphaFold 3（DeepMind/Isomorphic Labs, 2024）采用扩散模型架构预测蛋白质-核酸-小分子-离子复合物联合结构；在 PoseBusters 基准上大幅优于传统对接工具 Vina（P=2.27×10⁻¹³）；2024 年 11 月发布推理代码和权重（非商业/学术使用）[AlphaFold 3 Nature 论文](https://www.nature.com/articles/s41586-024-07487-w "Accurate structure prediction of biomolecular interactions with AlphaFold 3, Nature 2024")
- Boltz-2（MIT/Recursion, 2025）首个将结构预测与结合亲和力预测统一到单一框架的开源模型；FEP+ 基准平均 Pearson 0.66，计算效率提升超 1,000 倍；CASP16 亲和力赛道零调优超越所有参赛者；CC-BY 4.0 完全开源 [Boltz-2 预印本](https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699/ "Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction, bioRxiv 2025")
- 技术成熟度：AlphaFold 3 早期商业化/临床验证阶段；ESM-3 学术研究/早期商业化阶段；Boltz-2 学术研究/概念验证阶段

**化学基础模型**
- nach0（Insilico/NVIDIA, 2024）基于 T5 架构，250M/780M 参数，在 1,300 万篇 PubMed 摘要和约 1 亿条 ZINC 分子 SMILES 上预训练；正向反应预测 88% top-1 准确率，逆合成 53% top-1 准确率 [nach0 论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151847/ "nach0: multimodal natural and chemical languages foundation model, Chemical Science 2024;15:8380")
- ChemBERTa-2（2022）约 46M 参数，在最高 7,700 万条 PubChem SMILES 上预训练，在 MoleculeNet 基准上与 SOTA 竞争性持平 [ChemBERTa-2 论文](https://arxiv.org/abs/2209.01712 "ChemBERTa-2: Towards Chemical Foundation Models, arXiv:2209.01712, 2022")
- 能力边界：核心作用在于分子属性预测（ADMET）、反应预测和分子生成；ADMET 预测中通常假设"平均患者"，缺乏个体化建模机制

**单细胞/基因组基础模型（scFM）**
- scGPT（2024 Nature Methods）在超过 3,300 万个单细胞转录组上预训练，支持细胞类型注释、批次校正、基因网络推断和扰动预测 [scGPT](https://www.nature.com/articles/s41592-024-02201-0 "scGPT: toward building a foundation model for single-cell multi-omics, Nature Methods 2024;21:1470-1480")
- scFoundation（BioMap/清华, 2024 Nature Methods）100M 参数，在超过 5,000 万条单细胞转录组上预训练，在组织药物响应预测等任务上达 SOTA [scFoundation 论文](https://pubmed.ncbi.nlm.nih.gov/38844628/ "Large-scale foundation model on single-cell transcriptomics, Nature Methods 2024;21:1481-1491")
- Geneformer V2（Gladstone/Harvard/Broad, 2026 Nature Computational Science）在 1.04 亿个人类单细胞转录组（150B 基因 token）上预训练，提供 38M–316M 五种参数规模；定义了转录组掩码学习的 scaling laws；GF-316M 零样本超越传统微调方法；4-bit QLoRA 将微调时间缩短至 15%、内存降至 34% [Geneformer V2](https://www.nature.com/articles/s43588-026-00972-4 "Scaling and quantization enables resource-efficient predictions in network biology, Nature Computational Science 2026")
- Evo 2（Arc Institute/NVIDIA/Stanford, 2026 Nature）7B/40B 参数，在 9.3 万亿 DNA 碱基对上训练，覆盖生命三域；上下文窗口 100 万碱基对、单核苷酸分辨率；零样本预测编码区和非编码区致病变异（ClinVar 非 SNV 变异上优于所有其他方法）[Evo 2 Nature 论文](https://www.nature.com/articles/s41586-026-10176-5 "Genome modelling and design across all domains of life with Evo 2, Nature 2026")
- **scFM 扰动预测的关键能力瓶颈**：2025 年 Genome Biology 零样本评估发现 Geneformer V1 和 scGPT 零样本聚类不优于简单基线 [零样本评估论文](https://link.springer.com/article/10.1186/s13059-025-03574-x "Genome Biology 2025;26:101")；2025 年 Nature Methods 基准研究发现全部 7 个深度学习模型在基因扰动预测上均未超越简单线性基线 [Nature Methods 基准](https://www.nature.com/articles/s41592-025-02772-6 "Nature Methods 2025;22:1657-1661")
- 个体异质性表征：最具潜力——Geneformer V2 训练于跨 55 种器官的转录组；Evo 2 可在单核苷酸分辨率预测遗传变异功能效应；但尚未针对"个体间差异"专门优化

**多模态生物医学模型**
- BiomedCLIP（Microsoft, 2024 NEJM AI）基于 CLIP 架构，在 PMC-15M 数据集（1,500 万图文对）上预训练，开源 [BiomedCLIP 论文](https://arxiv.org/html/2303.00915v3 "BiomedCLIP, NEJM AI 2024")
- Precious3GPT（Insilico, 2024 预印本）首个多组学多物种多组织多模态 Transformer，在 120 万组学数据点上训练，可执行靶点识别、药物基因组学预测等任务 [Precious3GPT 预印本](https://www.biorxiv.org/content/10.1101/2024.07.25.605062v1 "Precious3GPT: Multimodal Multi-Species Multi-Omics Multi-Tissue Transformer, bioRxiv 2024")
- Precious3GPT 是当前最接近"多模态药物影响模拟"理念的模型，但仍为预印本阶段

**族群间互补关系**
- 五大族群形成天然互补分层：化学模型处理分子表示 → 蛋白质模型预测药物-靶点互作 → 单细胞模型预测细胞层面转录响应 → LLM 提供知识推理 → 多模态模型尝试跨层级整合
- 主要整合障碍：各层级输入/输出表示不兼容、缺乏统一跨尺度训练框架、分子扰动到表型的因果链条无端到端模型覆盖；CZI Virtual Cell Platform 和 NVIDIA BioNeMo 正尝试构建模块化集成框架

### 可用图片
（无——本地 /data/ 中无与本章直接相关的图片素材）

### 仍需补充
- Geneformer V2（GF-316M）在药物扰动预测专门任务上的定量评估数据（论文主要报告网络生物学任务）
- Boltz-2 的确切模型参数规模（原始论文未明确报告）
- CZI rBio 推理模型（2025 年宣布）的技术细节和评估结果
- Precious3GPT 是否已有同行评审出版版本（截至 2026 年 4 月仍仅为预印本）——大模型在药物评估全链条中的应用现状

### 研究目标
- 沿药物评估全链条（靶点发现与验证 → 药物-靶点互作预测 → ADMET/药代动力学预测 → 细胞/组织层面药物响应预测 → 安全性与毒性评估 → 临床试验设计优化与患者分层）逐环节论述 AI 基础模型的实际应用现状与技术成熟度
- 在每一环节中标注当前代表性模型/工具、已达到的性能基准（结合权威评测结果与局限）、与传统方法的对比优势及差距
- 重点评估两大核心环节：(1) 药物响应预测与个体化评估——单细胞基础模型在预测药物扰动响应中的零样本与微调表现、跨患者群体泛化能力的局限、个体异质性建模的初步尝试；(2) 跨尺度整合的前沿探索——虚拟细胞模型（CZI Virtual Cell Platform、Xaira 等）将分子/细胞层面的模型预测向组织/器官层面延伸的初步进展，以及数字孪生概念在药物评估中的早期应用
- 呈现 AI 驱动临床试验模拟与患者分层的探索性进展，评估其对解决个体异质性问题的潜在价值

### 关键发现
（待 researcher 补研）

### 可用图片
（待 researcher 补研）

### 仍需补充
（待 researcher 补研）

---

## Chapter 4：产业生态与标杆案例——AI 药物评估平台的技术路线与商业化验证

### 研究目标
- 通过对标杆性企业/平台的深度剖析，展示大模型在药物系统性评估中的落地实况、技术路线差异和商业化验证进展，覆盖代表性平台（Insilico Medicine / Pharma.AI、Recursion Pharmaceuticals / Recursion OS、Isomorphic Labs / IsoDDE、NVIDIA BioNeMo 生态、晶泰科技 XtalPi 等）
- 分析各平台在"从 AI 发现到临床验证"这一关键跨越中的进展阶段：哪些平台已有临床数据支撑（如 Rentosertib Phase IIa、REC-4881 Phase 2）、哪些仍处于计算验证阶段、其技术路线选择如何影响系统性评估能力
- 评估产业生态中基础设施层（NVIDIA BioNeMo、Microsoft Discovery）、模型层（ESM/AlphaFold/scGPT 等开放模型）与应用层（Insilico/Recursion 等集成平台）之间的协作关系与价值链结构
- 标识各平台在个体异质性建模方面的技术路线差异（Recursion 的表型数据驱动路线、CZI/Biohub 的虚拟细胞路线、Insilico 的 Precious3GPT 多组学整合路线等）

### 关键发现
（待 researcher 补研）

### 可用图片
（待 researcher 补研）

### 仍需补充
（待 researcher 补研）

---

## Chapter 5：核心挑战与技术瓶颈——从模型能力到临床转化的鸿沟

### 研究目标
- 系统剖析"跨尺度建模鸿沟"——当前各层级模型（分子/蛋白质/细胞/组织/系统）各自为战、尚未实现从分子扰动到表型结果的全链条因果模拟——这是回答"AI 能否模拟药物对机体影响"的核心技术瓶颈；组合式基础模型（compositional foundation models）的探索仍处于概念阶段
- 审视数据层面的结构性挑战：训练数据的人群偏倚（种族、年龄、疾病谱覆盖不足）对个体异质性建模的制约、多组学数据标准化与互操作性问题、高质量标注数据的稀缺与基准评测体系的脆弱性（如排行榜过拟合问题）
- 评估模型可解释性与因果推断的困境：黑箱问题对临床决策信任度的影响、从相关性到因果性的跨越难题对监管认可的影响、当前可解释性方法的不足与改进方向
- 分析监管、伦理与公平性维度的挑战：FDA/EMA 对 AI 辅助药物开发的监管框架演变（2025 年 FDA 首份草案指南的意义与局限）、算法偏见对药物评估公平性的影响、AI 辅助决策中的责任归属

### 关键发现
（待 researcher 补研）

### 可用图片
（待 researcher 补研）

### 仍需补充
（待 researcher 补研）

---

## Chapter 6：未来路径——迈向 AI 驱动的药物系统性评估与个体化模拟

### 研究目标
- 展望中短期（6–18 个月）可期进展：单细胞基础模型扰动预测精度的提升路径、蛋白质-配体互作预测从结构到亲和力的跨越（Boltz-2/IsoDDE 代表的趋势）、ADMET 预测基准体系的规范化重建、首批 AI 设计药物的关键临床数据读出（Phase II/III 结果）
- 展望中长期（3–5 年）技术演进方向：多模态融合深化（基因组 + 蛋白质组 + 单细胞转录组 + 影像 + 电子健康记录的统一建模）、跨尺度基础模型（cross-scale foundation models）从分子到组织的统一表示学习、虚拟细胞模型的成熟度跃升（CZI/NVIDIA 合作、Xaira 等旗舰项目的预期产出）、从器官级到患者级数字孪生在药物评估中的应用前景
- 聚焦"个体异质性"问题的解题路径：大模型如何纳入个体遗传背景（遗传变异功能效应预测模型的技术路线）、微生物组特征和生活方式数据，实现从"平均患者"到个体化的药物响应预测
- 评估从"AI 辅助"到"AI 驱动"的范式转换条件：跨尺度因果模型的可行性、大模型与机制模型（systems biology）的融合路径、监管框架的成熟度要求、实验闭环（lab-in-the-loop）自主实验室的角色

### 关键发现
（待 researcher 补研）

### 可用图片
（待 researcher 补研）

### 仍需补充
（待 researcher 补研）

---

# Section 2：给 Write 阶段的执行建议

## 研究时间口径
- 全文以 2026 年 4 月为时间锚点
- "近一年进展"统一指 2025 年 4 月至 2026 年 4 月
- 展望区分"中短期"（6–18 个月，即 2026 年底至 2027 年底）和"中长期"（3–5 年，即 2029–2031 年）
- 进入临床验证的 AI 药物管线以截至 2026 年 4 月的最新可用数据为准

## 术语规范
- "AI 大模型"仅作为报告标题层面的非正式统称，正文中使用"基础模型"（Foundation Model, FM）
- "大语言模型"（LLM）仅指以自然语言为主要训练数据的模型（GPT 系列、BioGPT、Med-Gemini 等），不包括蛋白质语言模型
- "蛋白质语言模型"（pLM）单独指代以蛋白质序列为训练数据的模型（ESM 系列等）
- "单细胞基础模型"（scFM）用于 scGPT、scFoundation、Geneformer 等
- "组合式基础模型"（Compositional Foundation Model）——指通过模块化组合不同尺度/模态的基础模型来构建跨尺度预测能力的技术路线，区别于单一端到端大模型
- "药物系统性评估"——本报告核心概念，需在 Chapter 1 给出操作性定义
- "个体异质性"（Inter-individual Variability）——贯穿全文的线索概念，需在 Chapter 1 明确操作性定义
- "虚拟细胞"（Virtual Cell）——特指 CZI/Biohub 等推动的 AI 驱动细胞级模拟模型，需与传统系统生物学中的数学模型区分
- "数字孪生"（Digital Twin）——在药物评估语境下需与工业领域的数字孪生区分
- 所有模型名称首次出现时标注开发机构和发布年份
- 商业平台使用官方正式名称；同一模型不同版本需明确标注版本号（如 ESM-2 vs ESM-3、Geneformer V1 vs V2）

## 跨章节口径统一
- **个体异质性贯穿**：Ch1 定义问题 → Ch2 评估各模型表征能力 → Ch3 讨论个体化评估实现程度 → Ch4 标识各平台技术路线 → Ch5 强调数据偏倚核心挑战 → Ch6 聚焦解题路径
- **技术成熟度分级**：统一四级标签——学术研究 / 概念验证 / 早期商业化 / 临床验证
- **核心问题回答口径**：对"AI 能否模拟药物对机体影响"采用分层回答——分子-蛋白质互作层已具备初步能力 → 细胞层面有概念验证 → 组织/器官/系统层面仍为开放问题 → 纳入个体异质性的全人体模拟尚属远期愿景
- **案例去重**：Ch3 以"技术环节"为主线引用平台案例佐证但不展开；Ch4 以"平台/企业"为主线深度剖析
- **数据引用口径**：同一数据点在不同章节引用时保持数值和来源一致；涉及基准测试结果时需注明评测条件（零样本/微调、有无 MSA 输入等）

## 行文风格
- 正式学术研究报告风格，以"我们"作为研究主体
- 量化优先：核心论点以数据支撑，遵循"主体+时间+单位+数值+来源"五要素
- 避免元叙述和营销性措辞
- 中文为主、英文术语保留，关键概念首次出现时中英对照
- 对技术局限和不确定性应坦诚表述，避免过度乐观或过度悲观的倾向性措辞

## 篇幅分配
- Ch1（15%）、Ch2（18%）、Ch3（20%）、Ch4（20%）、Ch5（14%）、Ch6（13%）

## 图表建议
- Chapter 1：临床试验各阶段成功率漏斗图 + 个体异质性多维来源示意图
- Chapter 2：AI 基础模型技术图谱总览图（生物组织层级×模型族群）
- Chapter 3：药物评估全链条与 AI 模型映射关系图
- Chapter 4：产业生态三层架构图（基础设施层-模型层-应用层）+ 代表性平台管线进展时间线
- Chapter 5：跨尺度建模鸿沟示意图（各层级模型覆盖范围与空白地带）
- Chapter 6：技术路线图时间轴（中短期 vs 中长期里程碑）

## 成稿前需再次核验的判断
1. 各代表性平台的最新管线状态和临床阶段
2. FDA/EMA 指导原则的具体发布日期、版本号
3. AlphaFold3 的开源/商用许可状态
4. CZI Virtual Cell Platform 的开放访问状态

## 一致性检查清单
1. "药物系统性评估"的定义在各章引用时含义一致
2. "个体异质性"的操作性定义在各章引用时范围一致
3. 技术成熟度标签在各章对同一模型/平台的标注一致
4. 同一数据点在不同章节引用时数值和来源一致
5. 基准测试结果在引用时注明评测条件，避免不同章节引用不可比数据
6. 对核心问题"能否模拟药物系统性影响"的分层回答在各章保持一致的框架和口径
