# Section 1：章节研究计划

## Chapter 1：二维半导体接触物理的基本框架与核心挑战
### 研究目标
- 建立全文的物理语言基础：阐明金属-二维半导体界面区别于传统三维半导体界面的独特之处
- 明确接触电阻的物理组成（肖特基势垒、隧穿势垒、界面态散射等），定义接触电阻分解框架 $R_c = R_{\text{SB}} + R_{\text{tunnel}} + R_{\text{spread}}$
- 回答核心问题：为什么二维半导体的接触电阻远高于理论预期？费米钉扎在TMDCs中的微观起源是什么？
- 子话题覆盖：Schottky-Mott模型、费米钉扎与电荷中性能级、MIGS模型、范德华间隙引入的隧穿势垒、IRDS路线图对接触电阻的要求

### 关键发现
- 经典 Schottky-Mott 模型预测 SBH = Φ_M − χ（n 型），假设钉扎因子 S = 1。该模型在二维体系中严重失效：Das 等人（2013）测得 Sc/Ti/Ni/Au 接触多层 MoS₂ 的 SBH 仅在 0.03–0.2 eV 范围变化（对应功函数 3.5–5.1 eV），远小于 Schottky-Mott 预测 [Das et al., Nano Lett. 2013](https://pubmed.ncbi.nlm.nih.gov/23240655/ "High performance multilayer MoS₂ transistors with scandium contacts, Nano Lett. 13, 100-105") [Tung (2014)](https://pubs.aip.org/aip/are/article/1/1/011304/592540/The-physics-and-chemistry-of-the-Schottky-barrier "Appl. Phys. Rev. 1, 011304")。
- Schultz, Shin, Koch 等人（2022）通过 ARPES 直接测量发现，单层 MoS₂ 在低功函数衬底（Φ_sub < 4.5 eV）上出现强费米钉扎（S ≈ 0），电子势垒钉扎在 ~0.4 eV；高功函数衬底上近似真空能级对齐但电子和空穴 S 不同（电子 S ≈ 0.69，空穴 S ≈ 1.11）。该工作提出扩展 Schottky-Mott 规则，揭示二维半导体独特的介电环境依赖性 [Schultz, Shin, Koch et al., ACS Nano 2022](https://pubs.acs.org/doi/10.1021/acsnano.1c04825 "The Schottky-Mott Rule Expanded for Two-Dimensional Semiconductors")。
- 单层 MoS₂ 光学带隙 ~1.8–1.9 eV（直接带隙，K 点），块体 ~1.2 eV（间接带隙）；准粒子带隙受介电环境强烈影响：金属衬底上 ~2.0 eV，绝缘体衬底上可达 2.5–2.9 eV [Radisavljevic et al., Nat. Nanotechnol. 2011](https://pubmed.ncbi.nlm.nih.gov/21278752/ "Single-layer MoS₂ transistors") [Noori, Xuan & Quek, npj 2D Mater. Appl. 2022](https://www.nature.com/articles/s41699-022-00349-x "Origin of contact polarity at metal-2D TMDC interfaces")。
- 费米钉扎因子实验值：传统蒸镀金属接触单层 MoS₂ 的 S 值通常为 0.02–0.3（强钉扎）。Kim 等人（2017）首次实验测得单层 MoS₂ 的 S = 0.11，单层 MoTe₂ 的 S = −0.07 [Kim et al., ACS Nano 2017](https://pubs.acs.org/doi/10.1021/acsnano.6b07159 "Fermi Level Pinning at Electrical Metal Contacts of Monolayer MoS₂")。Kim（G.-S.）等人（2018）测得多层 MoS₂ 的 MS 直接接触 S = 0.02；引入 1 nm TiO₂ 插层后 S 提升至 0.24 [Kim G.-S. et al., ACS Nano 2018](https://pubs.acs.org/doi/10.1021/acsnano.8b03331 "Schottky Barrier Height Engineering with Reduction of MIGS")。Bampoulis 等人（2017）局域测量发现缺陷位置 S ≈ 0.1，无缺陷区域 S ≈ 0.3，表明缺陷显著增强费米钉扎 [Bampoulis et al., ACS Appl. Mater. Interfaces 2017](https://pubs.acs.org/doi/10.1021/acsami.7b02739 "Defect Dominated Charge Transport and Fermi Level Pinning")。转移金属 vdW 接触可将 S 提升至 ~0.96，趋近 Schottky-Mott 极限。
- 费米钉扎微观起源的综合图景：(1) MIGS 提供部分钉扎（Tersoff 1984 模型，CNL ≈ 4.48 eV）；(2) 硫空位等缺陷态是大多数实验样品中 n 型行为和强钉扎的主导原因——Noori 等人（2022）GW 计算表明无缺陷 MoS₂/Au 为 p 型，含硫空位后变为 n 型 [Noori, Xuan & Quek, npj 2D Mater. Appl. 2022](https://www.nature.com/articles/s41699-022-00349-x "Origin of contact polarity at metal-2D TMDC interfaces")；(3) Gong 等人（2014）DFT 揭示界面偶极子+弱化 S-Mo 键产生带隙态的钉扎机制 [Gong et al., Nano Lett. 2014](https://pubmed.ncbi.nlm.nih.gov/24660782/ "The unusual mechanism of partial Fermi level pinning at metal-MoS₂ interfaces")。三种机制的相对权重取决于界面质量和接触方式。
- vdW 间隙（3–4 Å）构成额外隧穿势垒，但同时抑制 MIGS 穿透使费米钉扎显著减弱。Liu, Stradins & Wei（2016）DFT 计算阐明了 vdW 接触的"去钉扎但增加隧穿"的权衡关系 [Liu, Stradins & Wei, Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "Van der Waals metal-semiconductor junction")。
- 接触电阻分解：R_c = R_SB + R_T + R_spread。传统蒸镀金属接触单层 MoS₂ 典型 R_c 为 0.2–10 kΩ·μm。Shen 等人（2021）Bi 接触实现 123 Ω·μm（SBH = 0）[Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "Bi contact: Rc=123 Ω·μm")；Li 等人（2023）Sb 接触进一步推至 42 Ω·μm [Li et al., Nature 2023](https://pubmed.ncbi.nlm.nih.gov/36631650/ "Approaching the quantum limit: Rc=42 Ω·μm") [Allain et al., Nat. Mater. 2015](https://pubmed.ncbi.nlm.nih.gov/26585088/ "Electrical contacts to two-dimensional semiconductors")。
- 量子极限：R_c^Q = πℏ/(4e²k_F)，在 n_2D ≈ 10¹³ cm⁻² 下约为 36 Ω·μm。Sb 接触的 42 Ω·μm 已非常接近该极限 [Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "量子极限公式") [Akinwande, Biswas & Jena, Nat. Electron. 2025](https://www.nature.com/articles/s41928-024-01335-5 "The quantum limits of contact resistance")。
- IRDS 路线图要求：缩放至亚 10 nm 节点的二维晶体管需 R_c < ~100 Ω·μm；极端缩放（接触长度 < 20 nm）需 R_c < 50 Ω·μm（ρ_c < 10⁻⁹ Ω·cm²）。Li 等人（2023）的 Sb-MoS₂ 器件满足 IRDS 2028 年目标 [Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "引用IRDS 2017路线图") [Li et al., Nature 2023](https://pubmed.ncbi.nlm.nih.gov/36631650/ "满足2028 IRDS目标")。
- Kang 等人（2014）DFT 系统评估 In/Ti/Au/Pd 对单层 MoS₂ 的顶部接触和边缘接触，揭示 vdW 隧穿势垒是限制载流子注入的关键因素，边缘接触可显著优于顶部接触 [Kang et al., Phys. Rev. X 2014](https://link.aps.org/doi/10.1103/PhysRevX.4.031005 "Computational Study of Metal Contacts to Monolayer TMDs")。
- 二维界面与三维界面的根本区别：(1) 原子级厚度使空间电荷区无法沿厚度方向延伸；(2) 介电屏蔽极弱导致准粒子带隙强烈依赖周围环境（金属衬底上带隙可减少 ~0.9 eV）；(3) MIGS 可穿透整个二维薄层，但 vdW 间隙可有效阻断 [Allain et al., Nat. Mater. 2015](https://pubmed.ncbi.nlm.nih.gov/26585088/ "Electrical contacts to 2D semiconductors") [Liu, Stradins & Wei, Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "vdW间隙抑制MIGS")。

### 可用图片
（无与本主题直接相关的本地图片资料）

### 仍需补充
- IRDS 路线图原始文档中各技术节点（2025、2028、2031 年）接触电阻要求的精确数值，需直接查阅 IRDS 官方 PDF
- vdW 间隙隧穿势垒高度的精确定量值（以 eV 为单位），需查阅 Kang 等人（Phys. Rev. X 2014）详细图表
- Sotthewes 等人（2019, J. Phys. Chem. C 123, 5411-5420）报道的 TMDCs"普适费米钉扎"系统性数据（不同 TMDCs 的 CNL 和 S 值）
- Allain 等人（2015, Nat. Mater.）中经典接触电阻分解图示和 TLM 讨论的详细引用

## Chapter 2：降低接触电阻的主流实验方案——方法论全景
### 研究目标
- 系统梳理过去十年（~2014–2026）发展出的各类降低二维半导体接触电阻的实验方法
- 以MoS₂为核心案例，对每种方案的实验构型、代表性成果（接触电阻数值与器件性能）、适用条件与局限性进行客观陈述
- 覆盖方案类型：半金属接触（Bi、Sb）、纯金属范德华接触（转移Au等）、相变工程接触（2H→1T'/1T）、石墨烯/二维金属插层接触、掺杂工程接触、边缘接触、新兴方案（拓扑半金属、电子化合物等）
- n型与p型接触的差异对比

### 关键发现
- **半金属接触（Bi）**：Shen 等人（2021）在单层 MoS₂ 上采用 Bi 电极实现 Rc = 123 Ω·μm、SBH = 0 meV、开态电流 1,135 μA/μm（n₂D ≈ 4×10¹² cm⁻²，室温 TLM），DFT 表明 Bi 的低态密度抑制 MIGS 且使费米能级移入导带形成简并态。Bi 接触对 WS₂、WSe₂ 同样有效，但高质量晶体是前提（硫空位导致性能退化）[Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "Ultralow contact resistance between semimetal and monolayer semiconductors, Nature 593, 211-217")。
- **半金属接触（Sb）**：Li 等人（2023）采用 Sb(01̄12) 晶面接触单层 MoS₂，Rc = 42 Ω·μm（接近量子极限 ~36 Ω·μm），短沟道器件实现开态电流 1.23 mA/μm、开关比 > 10⁸、本征延迟 74 fs，满足 IRDS 2028 目标。Sb(01̄12) 在 125°C 下稳定 24 h+，优于 Bi；Sb(01̄12) 与 Sb(0001) 性能差异显著（前者负 SBH，后者正 SBH），源于晶面电子态密度差异。TSMC 平台上 CVD MoS₂ 验证了 Sb 半金属接触的产业可行性 [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Approaching the quantum limit in 2D semiconductor contacts, Nature 613, 274-279")。
- **纯金属 vdW 接触**：Liu 等人（2018）首次通过机械转移法制备原子级平整金属-TMDCs vdW 结，S ≈ 0.96（vs. 蒸镀 S ≈ 0.09–0.3），证明 vdW 间隙有效抑制 MIGS [Liu et al., Nature 2018](https://www.nature.com/articles/s41586-018-0129-8 "Approaching the Schottky-Mott limit in vdW metal-semiconductor junctions, Nature 557, 696-700")。Wang 等人（2019）用 10 nm In + 100 nm Au 低能沉积在单层 MoS₂ 上形成超洁净 vdW 界面（STEM 确认无化学键合）[Wang et al., Nature 2019](https://www.nature.com/articles/s41586-019-1052-3 "Van der Waals contacts between 3D metals and 2D semiconductors, Nature 568, 70-74")。Jung 等人（2019）转移通孔接触方案实现了高迁移率低接触电阻 [Jung et al., Nat. Electron. 2019](https://www.nature.com/articles/s41928-019-0245-y "Transferred via contacts, Nat. Electron. 2, 187-194")。核心局限：转移法不兼容晶圆级制造；vdW 间隙虽抑制 MIGS 但引入隧穿势垒；界面洁净度对工艺极敏感。
- **相变工程接触**：Kappera 等人（2014）通过 n-丁基锂将 MoS₂ 接触区从 2H 相变为金属性 1T 相，Rc 从 ~1.1 kΩ·μm 降至 ~0.2 kΩ·μm [Kappera et al., Nat. Mater. 2014](https://www.nature.com/articles/nmat4080 "Phase-engineered low-resistance contacts, Nat. Mater. 13, 1128-1134")。Cho 等人（2015）激光诱导 MoTe₂ 2H→1T' 相变构建欧姆同质结接触 [Cho et al., Science 2015](https://www.science.org/doi/10.1126/science.aab3175 "Phase patterning for ohmic homojunction contact in MoTe₂")。核心优势：无缝金属-半导体过渡消除 vdW 隧穿势垒。局限：1T 相热力学亚稳、湿法工艺不利集成、仅适用于多晶型能差小的 TMDCs。
- **石墨烯/二维金属插层接触**：Du 等人（2014）镍刻蚀石墨烯电极 Rc ≈ 460 Ω·μm [Du et al., ACS Nano 2014](https://pubs.acs.org/doi/10.1021/nn506567r "Nickel-Etched-Graphene Electrodes for MoS₂")。Guimarães 等人（2016）石墨烯-TMDCs 原子级薄边缘接触 [Guimarães et al., ACS Nano 2016](https://pubs.acs.org/doi/10.1021/acsnano.6b02879 "Atomically thin ohmic edge contacts")。Vu 等人（2021）一步 CVD 合成 NbSe₂/Nb-WSe₂ vdW 异质结实现欧姆接触 [Vu et al., ACS Nano 2021](https://pubs.acs.org/doi/10.1021/acsnano.1c02038 "NbSe₂/Nb-doped-WSe₂ heterostructure")。石墨烯低态密度抑制 MIGS，但功函数调节范围有限且与 MoS₂ 仍存在 vdW 间隙。
- **掺杂工程接触**：Jiang 等人（2024）Y 掺杂诱导 MoS₂ 金属化（PDA 三步法），2 英寸晶圆上自对准 10 nm 沟道 FET 实现平均 Rc = 69 Ω·μm（最低 43 Ω·μm）、I_on = 1.22 mA/μm、弹道比 79%，兼容先进节点晶圆级集成 [Jiang et al., Nat. Electron. 2024](https://www.nature.com/articles/s41928-024-01176-2 "Yttrium-doping-induced metallization of MoS₂, Nat. Electron. 7, 545-556")。McClellan 等人（2021）AlOₓ 远程掺杂实现高电流密度 [McClellan et al., ACS Nano 2021](https://pubs.acs.org/doi/10.1021/acsnano.0c09078 "High current density via AlOₓ doping")。Fang 等人（2013）K 表面掺杂实现简并 n 型掺杂但空气中不稳定 [Fang et al., Nano Lett. 2013](https://pubs.acs.org/doi/10.1021/nl400044m "Degenerate n-doping by potassium")。
- **边缘接触（1D 接触）**：Cheng 等人（2019）原位边缘接触展示"接触缩放免疫"特性（20 nm 至数百 nm 接触长度性能不变）[Cheng et al., Nano Lett. 2019](https://pubs.acs.org/doi/10.1021/acs.nanolett.9b01355 "Immunity to contact scaling in MoS₂ transistors")。Jain 等人（2019）hBN 封装 MoS₂ 边缘接触实现数 kΩ·μm 级 Rc [Jain et al., Nano Lett. 2019](https://pubs.acs.org/doi/10.1021/acs.nanolett.9b02166 "1D edge contacts to monolayer semiconductor")。边缘接触完全消除 vdW 隧穿势垒，但有效接触面积极小、边缘态化学活性高。
- **新兴方案**：拓扑半金属（Na₃Bi、NbP）电极具有鲁棒表面态但实验数据尚不充分 [Phys. Rev. Appl. 2020](https://link.aps.org/doi/10.1103/PhysRevApplied.13.054030 "Topological Dirac semimetal contacts")。Sn 低功函数金属实现低温欧姆接触 [Cao et al., Appl. Phys. Lett. 2020](https://pubs.aip.org/aip/apl/article/116/2/022101/280121 "Low SBH contacts by Sn")。分子插层（苄基紫精等）通过强掺杂或偶极子调控实现欧姆接触 [Yue et al., Adv. Funct. Mater. 2019](https://onlinelibrary.wiley.com/doi/10.1002/adfm.201807338 "Ohmic contact via BV interlayer")。Lee（2024）Science 展望指出 Bi/Sb 已降低 n 型 Rc 但 p 型仍未实现欧姆接触，呼吁系统理论筛选 [Lee, Science 2024](https://www.science.org/doi/10.1126/science.adq4986 "Approaching quantum limit of contact resistance")。
- **p 型接触**：Wang 等人（2022）通过高速率电子束蒸发 Pt/Pd 实现工业兼容 p 型 vdW 接触，p-WSe₂ FET Rc = 3.3 kΩ·μm、迁移率 ~190 cm²V⁻¹s⁻¹ [Wang et al., Nature 2022](https://www.nature.com/articles/s41586-022-05134-w "P-type electrical contacts for 2D TMDCs, Nature 610, 61-66")。Chuang 等人（2014）MoOₓ 高功函数层实现 MoS₂/WSe₂ p 型导通 [Chuang et al., Nano Lett. 2014](https://pubs.acs.org/doi/10.1021/nl4043505 "MoS₂ p-type by MoOₓ contacts")。Ghosh 等人（2025）NO 掺杂双层 WSe₂ FET 开态电流 ~421 μA/μm [Ghosh et al., Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-59684-4 "High-performance p-type WSe₂ by NO doping")。p 型核心瓶颈：最佳 Rc（~3.3 kΩ·μm）仍比最佳 n 型（~42 Ω·μm）高两个数量级；高 IE（> 5.5 eV）要求极高功函数金属，而此类金属易在界面形成化学键破坏 vdW 间隙。

### 可用图片
（无与本主题直接相关的本地图片资料）

### 仍需补充
- Liu et al. Nature 2018 的具体 Rc 数值（原文侧重 S 值测量，需确认是否报道了 TLM 提取的 Rc）
- Kappera et al. Nat. Mater. 2014 的精确 Rc 数值及测量条件（层数、载流子浓度）
- Cho et al. Science 2015 MoTe₂ 相变接触的 TLM 量化 Rc
- NbS₂ 作为 MoS₂ 二维金属电极的代表性 Rc 数据
- 拓扑半金属接触的系统性 TLM 实验数据
- 各方案在统一载流子浓度下的横向比较表（需归一化整理）
- Wang et al. Nature 2019 In 接触的 TLM 提取 Rc 具体数值
- Sb 接触在 WSe₂ 上的 p 型 Rc 数据

## Chapter 3：共通物理机制的提取——从多样性中寻找统一性
### 研究目标
- 将Chapter 2中各实验方案进行机制层面的横向比较与归纳
- 提取降低接触电阻的几个核心物理机制：（i）费米钉扎的消除或弱化、（ii）肖特基势垒高度的调控、（iii）隧穿势垒的消除或减薄、（iv）界面无序度与缺陷态的最小化、（v）轨道杂化与能带耦合优化
- 论证这些方案在物理本质上并非相互独立，而是分别作用于接触电阻的不同物理分量
- 分析各机制之间的相互关联与竞争

### 关键发现
- **机制一：费米去钉扎的三条路径**：(1) 降低电极材料 DOS（半金属 Bi/Sb），使 MIGS 源强度减弱——Shen 等人（2021）DFT 表明 Bi 低 DOS 抑制 MIGS，费米能级移入导带 [Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "Ultralow contact resistance, Nature 593, 211-217")；Su 等人（2023）系统 DFT 发现半金属-TMDC 界面距离 3.5–4.0 Å 仅产生"弱金属化"，SMIGS 恰延伸至导带底 [Su et al., J. Phys. D 2023](https://arxiv.org/abs/2212.03003 "Weak metalization mechanism, J. Phys. D 56, 234001")。(2) vdW 间隙/介质插层空间阻断波函数渗透——Liu 等人（2016）论证 vdW 结中 MIGS 可忽略 [Liu, Stradins & Wei, Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "vdW metal-semiconductor junction")；Kim G.-S. 等人（2018）TiO₂ 插层使 S 从 0.02 升至 0.24 [Kim G.-S. et al., ACS Nano 2018](https://pubs.acs.org/doi/10.1021/acsnano.8b03331 "SBH Engineering with MIGS Reduction")。(3) 减少界面缺陷密度——Noori 等人（2022）GW 证明硫空位是 n 型钉扎主因 [Noori et al., npj 2D Mater. Appl. 2022](https://www.nature.com/articles/s41699-022-00349-x "Origin of contact polarity")；Bampoulis 等人（2017）局域测量缺陷位 S ≈ 0.1 vs. 无缺陷 S ≈ 0.3 [Bampoulis et al., ACS AMI 2017](https://pubs.acs.org/doi/10.1021/acsami.7b02739 "Defect dominated FLP")。三条路径非互斥，最成功方案同时利用多条。**主要作用于 R_SB。**
- **机制二：SBH 调控**：功函数匹配（Bi ~4.34 eV、Sb ~4.55 eV 与 MoS₂ EA ~4.0–4.2 eV 接近）[Liu et al., Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "Band alignment")；界面偶极子工程（Gong 等人 2014 揭示偶极子+弱化 S-Mo 键的双重修正）[Gong et al., Nano Lett. 2014](https://pubmed.ncbi.nlm.nih.gov/24660782/ "Unusual FLP mechanism")；掺杂诱导势垒变薄（Y 掺杂直接金属化消除 SBH）[Jiang et al., Nat. Electron. 2024](https://www.nature.com/articles/s41928-024-01176-2 "Y-doping metallization")；半金属"带隙态饱和"使费米能级移入导带（Bi: SBH = 0，Sb(01̄12): 负 SBH）[Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "SBH=0") [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Negative SBH")。**主要作用于 R_SB。**
- **机制三：隧穿势垒消除/减薄**：vdW 间隙（3–4 Å）构成额外隧穿势垒，使 Rc 比金属-硅接触高 1–3 个数量级 [Kang et al., Phys. Rev. X 2014](https://link.aps.org/doi/10.1103/PhysRevX.4.031005 "Tunneling barrier analysis")。Su 等人（2023）计算 Sb 隧穿比电阻低于 Bi，解释 Sb(42 Ω·μm) 优于 Bi(123 Ω·μm) [Su et al., J. Phys. D 2023](https://arxiv.org/abs/2212.03003 "Tunneling resistivity comparison")。边缘接触完全消除 vdW 隧穿（共价键注入）[Cheng et al., Nano Lett. 2019](https://pubs.acs.org/doi/10.1021/acs.nanolett.9b01355 "Contact scaling immunity")。相变接触实现无缝过渡（Rc 从 ~1.1 kΩ·μm 降至 ~0.2 kΩ·μm）[Kappera et al., Nat. Mater. 2014](https://www.nature.com/articles/nmat4080 "Phase-engineered contacts")。Sb(01̄12) 的"强 vdW"中间态——非共价但耦合远强于一般 vdW——是其接近量子极限的关键 [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Strong vdW interactions")。**主要作用于 R_tunnel。**
- **机制四：界面无序度与缺陷态最小化**：蒸镀高能原子损伤二维表面引入缺陷 [Kim et al., ACS Nano 2017](https://pubs.acs.org/doi/10.1021/acsnano.6b07159 "STEM界面表征")。清洁转移工艺（Liu 2018）和低能量沉积（Wang 2019 In/Au）可实现原子级洁净界面 [Wang et al., Nature 2019](https://www.nature.com/articles/s41586-019-1052-3 "vdW contacts")。沉积速率影响显著：高速率多步沉积优于低速率 [Wang et al., Nature 2022](https://www.nature.com/articles/s41586-022-05134-w "Deposition rate optimization")。Bi 接触对晶体质量极敏感（缺陷导致从欧姆退化为肖特基）[Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "Sample quality dependence")。WSe₂ 硒空位可被 O 钝化恢复 p 型，MoS₂ 硫空位难钝化持续导致 n 型钉扎 [Noori et al., npj 2D Mater. Appl. 2022](https://www.nature.com/articles/s41699-022-00349-x "Se vacancy passivation vs S vacancy")。**同时作用于 R_SB 和 R_tunnel。**
- **机制五：轨道杂化与能带耦合优化**：Bi(0001) 的 6p 轨道与 MoS₂ 导带 Mo 4d 形成"弱但有效"的杂化，足以产生带隙态饱和但不至于强 MIGS [Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "SAED and PLDOS analysis")。Sb(01̄12) vs. Sb(0001) 差异源于界面 vdW 相互作用强度和电荷转移量的差异——Sb(01̄12) 杂化更强、负 SBH [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Crystal-face-dependent hybridization")。Sb(01̄12) 对 MoSe₂/WS₂/WSe₂ 均形成更强杂化和更低 SBH，具有普适性 [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Extended Data Fig. 2")。石墨烯低 DOS 兼顾 MIGS 抑制和适度耦合 [Liu et al., Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "Graphene as buffer layer")。H-NbS₂ 功函数甚至高于 Pt，理论上可实现 p 型欧姆接触 [Liu et al., Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "H-NbS₂ for p-type contacts")。**作用于 R_SB 和 R_tunnel。**
- **核心权衡关系**：(1) MIGS-隧穿权衡——vdW 间隙抑制 MIGS 但增加隧穿，是最核心的矛盾 [Liu et al., Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "MIGS-tunneling trade-off") [Allain et al., Nat. Mater. 2015](https://pubmed.ncbi.nlm.nih.gov/26585088/ "R_c decomposition")。(2) 强耦合-钉扎增强权衡——Ti/Cr 强化学键降低隧穿距离但弱化 S-Mo 键产生带隙态 [Gong et al., Nano Lett. 2014](https://pubmed.ncbi.nlm.nih.gov/24660782/ "Metal-S bonding creates gap states")。(3) 半金属"恰到好处"平衡——同时实现低 DOS 抑 MIGS、功函数匹配、适度轨道杂化、带隙态饱和，在 R_SB 和 R_tunnel 间取得近最优折中 [Su et al., J. Phys. D 2023](https://arxiv.org/abs/2212.03003 "Sb lower tunneling resistivity than Bi")。(4) 相变/Y 掺杂通过"消除界面过渡"绕过 MIGS-tunneling 权衡，但面临相稳定性/工艺控制的新权衡。(5) p 型接触更难——高 IE 要求极高 Φ_M 金属，此类硬金属易形成化学键触发"强耦合→MIGS 增强"恶性循环 [Wang et al., Nature 2022](https://www.nature.com/articles/s41586-022-05134-w "p-type challenge")。
- **方法-机制映射表关键洞察**：Sb(01̄12) 是唯一在五个机制维度上均为"主要"的方案（Rc = 42 Ω·μm）；Bi 在四维"主要"但隧穿仅"次要"（Rc = 123 Ω·μm）；vdW 转移法去钉扎优异但隧穿维度不利；最成功方案均同时作用于 R_SB 和 R_tunnel 多个分量，仅作用于单一分量的方案效果有限。

### 可用图片
（无与本主题直接相关的本地图片资料）

### 仍需补充
- Bi-MoS₂ 界面 PLDOS 的定量数值（Shen 2021 Extended Data Fig. 4a 难以提取精确 DOS 数值）
- vdW 间隙宽度与隧穿概率的定量解析关系（Simmons 隧穿公式在二维体系中的系统验证）
- 拓扑表面态（Na₃Bi 等）与 TMDCs 界面电子结构的定量 DFT 结果
- Sb(01̄12) 与 Sb(0001) 的界面 MIGS 态密度定量比较数值

## Chapter 4：迈向统一框架——"去钉扎-低隧穿-强耦合"三支柱模型
### 研究目标
- 基于Chapter 3的机制提取，构建一个能够统一解释大多数低接触电阻方案的理论框架
- 核心命题：理想的二维半导体欧姆接触需同时满足三个条件——费米能级去钉扎、隧穿势垒最小化、界面轨道耦合优化
- 用三支柱框架重新审视各实验方案（Bi接触、转移Au接触等），分析其成功的具体原因
- 讨论框架的预测能力、适用边界和潜在局限性
- 与传统三维半导体接触理论（Bardeen模型、Heine模型、Tersoff模型）进行对比

### 关键发现
- **支柱一（去钉扎）定量刻画**：钉扎因子 S 为核心参数。Sotthewes 等人（2019）C-AFM 测量五种 TMDCs 得 S = 0.11–0.30（无缺陷区），含缺陷区 S = 0.04–0.11，且遵循 Mönch 经验关系 S = 1/(1+0.1(ε_∞−1)²)，但数据系统性偏离三维趋势线；MIGS 密度估算 N ≈ 1×10¹⁴ states/eV·cm² [Sotthewes et al., J. Phys. Chem. C 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6410613/ "Universal FLP in TMDCs, J. Phys. Chem. C 123, 5411-5420")。去钉扎阈值：S > 0.5 为"有效去钉扎"，S > 0.9 为"近理想去钉扎"。三条去钉扎路径均可从 S 公式理解为降低有效界面态密度 N。
- **支柱二（低隧穿）定量刻画**：隧穿比电阻为核心判据。Kang 等人（2014）指出 vdW 间隙使接触电阻比金属-硅高 1–3 数量级 [Kang et al., Phys. Rev. X 2014](https://link.aps.org/doi/10.1103/PhysRevX.4.031005 "Metal contacts to TMDs")。Su 等人（2023）定义隧穿比电阻并发现 Sb 低于 Bi [Su et al., J. Phys. D 2023](https://arxiv.org/abs/2212.03003 "Tunneling-specific resistivity")。实现路径：消除 vdW 间隙（相变/边缘接触→R_tunnel≈0）、增强界面耦合减薄等效势垒（Sb(01̄12)"强 vdW"路径）、简并掺杂变薄隧穿宽度。
- **支柱三（强耦合）与"最优耦合强度"**：Su 等人（2023）的"弱金属化"概念提供定量框架——半金属-TMDC 界面距离 3.5–4.0 Å（vs. 传统金属 2.0–2.5 Å），SMIGS 恰延伸至导带底，实现"带隙态饱和而非泛滥" [Su et al., J. Phys. D 2023](https://arxiv.org/abs/2212.03003 "Weak metalization mechanism")。Gong 等人（2014）DFT 表明 Ti/Cr 强化学键虽降低隧穿距离但弱化 S-Mo 键产生带隙态，增强钉扎 [Gong et al., Nano Lett. 2014](https://pubmed.ncbi.nlm.nih.gov/24660782/ "Unusual FLP mechanism")。最优耦合：电荷转移足以使费米能级进入导带但 MIGS 不扩展至整个带隙。
- **三支柱关系：MIGS-隧穿权衡而非不可能三角**：Liu 等人（2016）首次明确去钉扎与低隧穿的内在矛盾 [Liu et al., Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "MIGS-tunneling trade-off")。半金属通过"低 DOS→弱 MIGS+适度杂化"绕过权衡；相变/掺杂通过消除异质界面消解矛盾。**核心命题：凡同时优化三个支柱的方案均实现超低 Rc；仅优化一到两个支柱的方案 Rc 改善有限。**
- **框架审视各方案**：Bi（Rc=123 Ω·μm）——支柱一✓支柱二△支柱三✓，支柱二不足是 Rc 未破 100 的原因 [Shen et al., Nature 2021](https://www.nature.com/articles/s41586-021-03472-9 "Bi: Rc=123 Ω·μm")。Sb(01̄12)（Rc=42 Ω·μm）——三支柱均✓✓，唯一全优方案 [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Sb: Rc=42 Ω·μm")。转移 Au——支柱一✓✓(S≈0.96) 支柱二✗(隧穿瓶颈) 支柱三✗ [Liu et al., Nature 2018](https://www.nature.com/articles/s41586-018-0129-8 "S≈0.96 but tunneling limits Rc")。相变接触——绕过三支柱（消除异质界面），代表框架之外的"另类路径" [Kappera et al., Nat. Mater. 2014](https://www.nature.com/articles/nmat4080 "Phase-engineered contacts")。Y 掺杂（Rc=69 Ω·μm）——三支柱"极端版本"的多机制协同 [Jiang et al., Nat. Electron. 2024](https://www.nature.com/articles/s41928-024-01176-2 "Y-doping: Rc=69 Ω·μm")。边缘接触——支柱二极端优化但支柱一/三潜在缺陷 [Cheng et al., Nano Lett. 2019](https://pubs.acs.org/doi/10.1021/acs.nanolett.9b01355 "Edge contact scaling immunity")。ALB 接触（Rc=70 Ω·μm）——通过超软等离子体刻除表层 S 原子后暴露 Mo 与 Au 形成金属性界面键合，400°C 稳定，代表"局部金属化实现强耦合-去钉扎协同"的新路径 [Gao et al., Science 2025](https://www.science.org/doi/10.1126/science.adz2405 "Atomic layer bonding contacts, Science 390")。
- **框架预测能力**：Is 等人（2025）高通量 DFT 筛选 1,297 种二维半导体与三种二维金属的接触，发现界面静电势差/电荷转移/偶极矩为决定因子，可映射至支柱一和支柱三；760 种可与 PdTe₂ 形成 n 型欧姆，999 种可与 ScS₂ 形成 p 型欧姆 [Is et al., Nanoscale 2025](https://pubs.rsc.org/en/content/articlehtml/2025/nr/d4nr04523h "High throughput screening of Ohmic contacts")。Shu 等人（2025）ML+DFT 策略建立 Rc 与 SBH/隧穿比电阻的物理模型，发现-OH 氢键可增强耦合降低隧穿势垒（支柱二三协同）[Shu et al., JACS 2025](https://pubs.acs.org/doi/10.1021/jacs.5c14180 "Ultralow Rc Approaching Quantum Limit")。Lee（2024）呼吁系统理论筛选 [Lee, Science 2024](https://www.science.org/doi/10.1126/science.adq4986 "Approaching quantum limit of contact resistance")。
- **框架局限**：(1) p 型接触三支柱冲突更尖锐——高 Φ_M 硬金属易化学键合触发 MIGS [Wang et al., Nature 2022](https://www.nature.com/articles/s41586-022-05134-w "p-type Rc=3.3 kΩ·μm")，H-NbS₂ 是框架内理论候选 [Liu et al., Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "H-NbS₂ for p-type")。(2) 多层 TMDCs 中层间耦合可能使 MIGS 回归三维模式 [Kang et al., Phys. Rev. X 2014](https://link.aps.org/doi/10.1103/PhysRevX.4.031005 "Monolayer vs few-layer")。(3) 大面积 CVD 材料缺陷密度高，"界面缺陷最小化"从辅助条件升格为核心约束，或需"第四支柱"——Noori 等人（2022）证明缺陷态可能是主导钉扎来源而非 MIGS [Noori et al., npj 2D Mater. Appl. 2022](https://www.nature.com/articles/s41699-022-00349-x "Defects dominate contact polarity")。(4) 量子极限附近（Rc→36 Ω·μm），瓶颈从界面物理转向 Landauer 量子传输极限 [Akinwande et al., Nat. Electron. 2025](https://www.nature.com/articles/s41928-024-01335-5 "Quantum limits of contact resistance")。
- **与三维理论对比**：Bardeen（1947）本征表面态钉扎在 TMDCs 中由 MIGS+缺陷态替代 [Sotthewes et al., J. Phys. Chem. C 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6410613/ "Bardeen-like mechanism in TMDCs")。Heine（1965）金属波函数指数衰减尾概念直接对应 MIGS，vdW 间隙等效于 Heine 模型中的氧化层 [Heine, Phys. Rev. 1965](https://link.aps.org/doi/10.1103/PhysRev.138.A1689 "Theory of Surface States") [Liu et al., Sci. Adv. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439/ "vdW gap as oxide analog")。Tersoff（1984）CNL 模型对 TMDCs 近似成立但系统偏离 [Tersoff, PRL 1984](https://link.aps.org/doi/10.1103/PhysRevLett.52.465 "Schottky Barrier Heights and Gap States")。二维独特之处：(1) 无空间电荷区 [Allain et al., Nat. Mater. 2015](https://pubmed.ncbi.nlm.nih.gov/26585088/ "2D contacts")；(2) SBH 强依赖衬底介电环境 [Schultz et al., ACS Nano 2022](https://pubs.acs.org/doi/10.1021/acsnano.1c04825 "Extended Schottky-Mott Rule")；(3) vdW 间隙的双重角色（MIGS 抑制+隧穿势垒）。Allain 等人（2015）综述已提出 R_c 分解框架但未发展为多维判据体系；Su 等人（2023）"弱金属化"理论朝统一框架迈进一步；**据检索，尚未有文献提出完整的"三支柱"统一框架，本报告具有独创性贡献。**

### 可用图片
（无本地图片资料。建议写作时设计：三支柱模型示意图、各方案在三支柱空间中的定位图。）

### 仍需补充
- Sb(01̄12) 界面 SMIGS 态密度的定量数值（states/eV/nm²），Li 2023 仅有定性对比
- 隧穿比电阻绝对数值（Ω·cm²），Su 2023 仅报道 Bi 与 Sb 相对比较
- p 型接触的三支柱系统性评估（文献中缺乏先例，需写作时自行构建）
- Mönch 经验公式对 2D 体系拟合偏差的定量解释
- ALB 接触（Gao et al., Science 2025）的完整 DFT 能带结构数据

## Chapter 5：从实验室到产业——可扩展性与集成挑战
### 研究目标
- 评估各类低接触电阻方案在晶圆级制造和后端集成中的可行性
- 分析从原理验证到实际芯片集成所面临的工程瓶颈：晶圆级均匀性、工艺兼容性（BEOL温度预算）、接触尺寸缩放、热稳定性与可靠性
- p型接触的产业挑战及互补逻辑实现
- 标准化测量方法（TLM）中的陷阱与不同文献数据的可比性问题

### 关键发现
- **晶圆级均匀性**：imec 300 mm 平台完整 2D FET 工艺流程，直接沉积 WS₂ 器件良率 >99%（133/133），CoD2W 转移 MoS₂ 良率 97–99%。但 FAB Ti 侧接触 Rc 高达数十至数百 kΩ·μm，与学术最佳值（42–123 Ω·μm）存在 2–3 个数量级差距 [imec 300 mm 集成论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12862033/ "Integration of WS₂ and MoS₂ FETs in 300 mm pilot line, 2026")。TSMC IEDM 2022 展示 GAA 单层 MoS₂ 纳米片 nFET（40 nm 栅长，410 μA/μm 漏电流）[SemiWiki IEDM 2023](https://semiwiki.com/semiconductor-services/techinsights/324910-iedm-2023-2d-materials-intel-and-tsmc/ "TSMC GAA MoS₂ nanosheet nFET")。TSMC IEDM 2024 报道替位掺杂+合金化使双层 WSe₂ p 型 Rc ≈ 98 Ω·μm（34 倍改善）[TSMC 研究页面](https://research.tsmc.com/page/low-dimensional-material/2.html "TSMC p-type Rc ~98 Ω·μm, IEDM 2024")。Y 掺杂方案是目前唯一在晶圆级（2 英寸）验证亚 100 Ω·μm Rc 的方案 [Jiang et al., Nat. Electron. 2024](https://www.nature.com/articles/s41928-024-01176-2 "Wafer-scale demonstration")。CVD vs. 机械剥离晶体的缺陷密度差距是制约晶圆级接触性能的核心瓶颈。
- **BEOL 工艺兼容性**：BEOL 热预算上限通常 <400°C [imec](https://pmc.ncbi.nlm.nih.gov/articles/PMC12862033/ "Targeted thermal budget <500°C")。系统评估各金属：Bi（熔点 271°C）→BEOL 不兼容，125°C 即退化；In（157°C）→工艺窗口极窄；Sb（631°C）→工艺兼容，125°C 24h+ 稳定 [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Sb thermal stability")。ALB 接触工艺温度 <200°C 且 400°C 稳定，是唯一同时满足亚 100 Ω·μm Rc 和 BEOL 热稳定性的方案 [Gao et al., Science 2025](https://www.science.org/doi/10.1126/science.adz2405 "ALB: 70 Ω·μm, stable to 400°C")。CMOS 兼容金属（Ti/TiN/W）与低 Rc 金属（Bi/Sb）的矛盾；学术剥离工艺与 FAB 大马士革工艺的根本差异 [imec](https://pmc.ncbi.nlm.nih.gov/articles/PMC12862033/ "Lift-off unsuitable for 300 mm")。
- **接触尺寸缩放**：Ber 等人（2023）实测 CVD MoS₂/Ni 传输长度 L_T = 240 ± 10 nm（300 K），远超亚 10 nm 节点接触长度要求 [Ber et al., Adv. Electron. Mater. 2023](https://poplab.stanford.edu/pdfs/BerGrady-ComponentsContactResistance-aem23.pdf "L_T = 240 nm for Ni/CVD MoS₂")。边缘接触具有"接触缩放免疫"特性（性能与接触长度无关）[Cheng et al., Nano Lett. 2019](https://pubs.acs.org/doi/10.1021/acs.nanolett.9b01355 "Contact scaling immunity")。imec 侧接触为边缘接触的产业版本，但当前 Rc 远高于学术水平（等离子体损伤+Ti 钉扎）[imec](https://pmc.ncbi.nlm.nih.gov/articles/PMC12862033/ "Side contact in 300 mm FAB")。半金属接触的 L_T 和亚 10 nm 缩放行为尚未系统报道——关键知识缺口。
- **热稳定性与可靠性**：Bi 在 125°C 即退化（低熔点 271°C 致命缺陷）；Sb 在 125°C 24h+ 稳定（熔点 631°C）[Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Bi degrades, Sb stable at 125°C")。ALB 接触 400°C 稳定，金属性相干键合界面解决 vdW 接触在热载荷下的界面滑移问题 [Gao et al., Science 2025](https://www.science.org/doi/10.1126/science.adz2405 "ALB 400°C stability")。TSMC Pd/合金接触热稳定性优于 Bi/Sb [TSMC](https://research.tsmc.com/page/low-dimensional-material/2.html "Pd/alloy thermal stability")。1T 相变接触热力学亚稳，长期可靠性存疑 [Kappera et al., Nat. Mater. 2014](https://www.nature.com/articles/nmat4080 "1T metastability")。imec 300 mm 器件存在显著迟滞和 BTI，批次间变异性大于晶圆内变异性，变异源不明 [imec](https://pmc.ncbi.nlm.nih.gov/articles/PMC12862033/ "Lot-to-lot variability")。
- **p 型接触与 2D CMOS**：p 型最佳 Rc（3.3 kΩ·μm）仍比 n 型（42 Ω·μm）高 ~80 倍 [Wang et al., Nature 2022](https://www.nature.com/articles/s41586-022-05134-w "p-type Rc gap")。TSMC Pd/合金方案将 p 型 Rc 降至 ~98 Ω·μm（34 倍改善），首次在产业机构验证亚 100 Ω·μm p 型接触 [TSMC](https://research.tsmc.com/page/low-dimensional-material/2.html "TSMC p-type Rc ~98 Ω·μm")。拓扑半金属 NbP 作为 p 型候选（高 Φ_M+低 DOS）[Stanford NbP 论文](https://web.stanford.edu/group/OTL/lagan/24009/P-WS2%2520and%2520WSe2%2520with%2520NbP%2520Topological%2520Contacts.pdf "NbP p-type contacts")。2D CMOS n/p 接触不对称性（n: 42–123 Ω·μm vs. p: 98–3,300 Ω·μm）是互补逻辑的主要瓶颈。imec 预测 2D 材料将在 2032 年前后在 BEOL 中找到应用 [PMC 综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC10873265/ "IMEC projects 2D in BEOL by 2032")。
- **标准化测量方法**：Ber 等人（2023）首次分离接触电阻三分量——固有 R_c-i（与栅压无关）和结电阻 R_jun（依赖栅压，至少为 R_c-i 的 5 倍），传统 TLM 必须引入 R_jun 修正。R_jun 框架可统一解释各接触工程方案：氧化物掺杂降低隧穿距离、半金属降低 SBH、边缘接触消除 R_c-i [Ber et al., Adv. Electron. Mater. 2023](https://poplab.stanford.edu/pdfs/BerGrady-ComponentsContactResistance-aem23.pdf "R_jun concept and unified explanation")。实测 CVD MoS₂/Ni ρ_c = 2×10⁻⁶ Ω·cm²；完全去钉扎需 D_it < 10¹¹ cm⁻²，完全钉扎在 D_it > 5×10¹³ cm⁻²。文献间数据可比性受四大因素影响：载流子浓度差异、温度差异、材料质量差异、提取方法差异。imec 四探针方法解耦迁移率与 Rc，发现四探针迁移率系统性高于两端法约 2 倍 [imec](https://pmc.ncbi.nlm.nih.gov/articles/PMC12862033/ "4-probe vs 2-probe mobility")。

### 可用图片
（无本地图片资料。建议写作时设计：BEOL 兼容性矩阵图、接触电阻缩放趋势图、学术 vs. FAB 值差距对比图。）

### 仍需补充
- Sb(01̄12) 在 CVD MoS₂ 上的具体 Rc 数值（需查阅 Chou IEDM 2021 原文）
- Y 掺杂 PDA 工艺最高温度（是否严格满足 <400°C BEOL 约束）
- 长期可靠性测试数据（>1000h HTOL、热循环、电迁移）——所有低 Rc 方案均缺乏
- Samsung 在 2D 半导体接触方面的具体 IEDM/VLSI 论文
- IRDS 路线图中关于 2D FET 接触电阻的精确版本和表格编号

## Chapter 6：未来方向与展望
### 研究目标
- 基于前述统一框架，展望该领域的下一步突破方向
- 识别当前理论与实验中尚未解决的关键科学问题
- 覆盖方向：新型电极材料探索（二维电子化合物、高熵二维金属、拓扑半金属）、原子级界面工程、理论与计算驱动的材料筛选（ML + 高通量DFT）、量子极限下的接触物理、n型/p型同时优化的完整CMOS方案、向其他二维材料体系的推广

### 关键发现
- **新型电极材料**：(1) 二维电子化合物（electrene）Ca₂N——DFT 预测与 MoS₂ 形成 100% 隧穿概率的欧姆接触（"准键"避免 MIGS），且可触发 2H→1T' 相变，对 WS₂/MoSe₂/WSe₂/MoTe₂ 均有效 [Wang et al., PCCP 2023](https://pubs.rsc.org/en/content/articlelanding/2023/cp/d3cp01412f "Ca₂N/MoS₂ donor-acceptor heterostructure, PCCP 25, 15433")。系统筛选 [M₂X]⁺e⁻ 全系列 electrene 作为 Au/Cu-MoS₂ 插层，Ca₂N 为最优（TBW ~0.5 Å，远小于 Sb 1.35 Å/Bi 1.66 Å），但面临空气稳定性挑战 [Rafiee Diznab et al., PCCP 2024](https://pubs.rsc.org/en/content/articlepdf/2024/cp/D3CP06112D "Electrene insertion for barrier-free contacts")。(2) 拓扑半金属——Sb₂Te₃ "T-vdW" 接触在 WSe₂ 上实现 SBH ~24 meV、Rc ~0.71 kΩ·μm，拓扑表面态缓解 MIGS [Ghods et al., ACS Nano 2024](https://pubs.acs.org/doi/10.1021/acsnano.4c07585 "Topological vdW Contact, ACS Nano 18")；NbP 作为 p 型接触在 WS₂ 上实现室温空穴电流 5.8 μA/μm（亚 2 nm WS₂ 最高值），溅射室温沉积兼容 CMOS [Hoang et al., arXiv 2024](https://arxiv.org/abs/2409.18926 "NbP topological semimetal p-type contacts")。(3) 高熵金属电极为空白方向——可能通过调控费米面 DOS 和界面耦合提供新自由度。
- **原子级界面工程**：ALB（原子层键合）路径拓展——推广至其他 TMDCs、探索不同键合金属（Ag/Cu）、评估 CVD 大面积可行性 [Gao et al., Science 2025](https://www.science.org/doi/10.1126/science.adz2405 "ALB: 70 Ω·μm, 400°C stable")。TTT 分子+TiS₂ 半金属缺陷工程策略在 WSe₂ 上实现 ~147 cm²/V·s 空穴迁移率和 200°C 热稳定性，指向分子功能化+缺陷钝化协同 [Zhang et al., Nano Lett. 2025](https://pubs.acs.org/doi/10.1021/acs.nanolett.4c05970 "Defect engineering for p-type WSe₂")。Electrene 插层代表"单原子层→消除 SB+降低隧穿"的新范式。
- **计算驱动材料筛选**：Is 等人（2025）高通量 DFT 筛选 1,297 种二维半导体×3 种二维金属，发现 760 种/999 种分别可形成 n/p 型欧姆接触 [Is et al., Nanoscale 2025](https://pubs.rsc.org/en/content/articlehtml/2025/nr/d4nr04523h "High throughput screening")。Shu 等人（2025）ML+符号回归建立 Rc 物理模型，发现-OH 氢键增强耦合 [Shu et al., JACS 2025](https://pubs.acs.org/doi/10.1021/jacs.5c14180 "ML+DFT for Rc")。Li 等人（2024）主动学习方案（ARANet+FAVAL）仅需 15% 训练数据即可预测 SBH 和隧穿概率 [Li et al., Adv. Mater. 2024](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202312887 "ML screening for 2D contacts")。三支柱框架可具体化为筛选判据：低费米面 DOS+功函数偏差 <0.3 eV+适度界面电荷转移。Lee（2024）呼吁系统理论筛选 vdW 硬金属 [Lee, Science 2024](https://www.science.org/doi/10.1126/science.adq4986 "Systematic screening call")。
- **量子极限与弹道输运**：Sb(01̄12) 的 42 Ω·μm 距量子极限 36 Ω·μm 仅 ~17%。接近量子极限后瓶颈从界面物理转向 Landauer 量子电导（导电模式数和传输概率 T(E)），三支柱框架需从"消除障碍"转向"优化 T(E)→1"的量子传输描述 [Akinwande et al., Nat. Electron. 2025](https://www.nature.com/articles/s41928-024-01335-5 "Quantum limits of contact resistance")。进一步降低 Rc 的路径：更强界面耦合压缩隧穿势垒宽度、提高 n₂D 增加模式数（R_c^Q ∝ 1/√n₂D）、边缘接触的缩放免疫特性 [Li et al., Nature 2023](https://www.nature.com/articles/s41586-022-05431-4 "Sb: 42 Ω·μm") [Cheng et al., Nano Lett. 2019](https://pubs.acs.org/doi/10.1021/acs.nanolett.9b01355 "Edge contact scaling")。弹道器件需关注 k 空间波函数重叠（模式匹配）和 NEGF 模拟常规化应用。
- **n/p 型同时优化与 2D CMOS**：p 型最新突破——NO 掺杂双层 WSe₂ FET 实现 I_ON = 421 μA/μm（冠军器件），TLM Rc = 1.3 kΩ·μm，300 器件统计中位 I_ON > 100 μA/μm [Ghosh et al., Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-59684-4 "NO-doped p-type WSe₂")。TSMC 合金接触将 p 型 Rc 降至 98 Ω·μm [TSMC IEDM 2024](https://research.tsmc.com/page/low-dimensional-material/2.html "p-type Rc ~98 Ω·μm")。p 型路径图：高 Φ_M vdW 拓扑材料（Sb₂Te₃: 0.71 kΩ·μm, NbP）→ p 型掺杂+金属化（NO: 1.3 kΩ·μm, TSMC 合金: 98 Ω·μm）→ 2D 金属 H-NbS₂（理论候选）。p 型 Rc 从 2022 年 3.3 kΩ·μm 快速降至 2024 年 98 Ω·μm，处于快速突破期。n/p 最佳 Rc 差距已缩小至 ~2.3 倍（42 vs. 98 Ω·μm），远好于此前两个数量级。
- **向其他 2D 材料推广**：InSe——高迁移率（~10³ cm²/V·s）、较小 EA 使 n 型匹配容易，但层间耦合强使三支柱权重需重新标定 [Li et al., Sci. China Inf. Sci. 2024](https://cdn.sciengine.com/doi/10.1007/s11432-023-3884-3 "Ohmic-contact ballistic InSe transistors")。Bi₂O₂Se——"普遍欧姆接触"现象（费米钉扎在导带以上），三支柱框架需引入"有利钉扎"概念 [Wang et al., J. Phys. Chem. C 2019](https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.8b12278 "Pervasive Ohmic contacts in Bi₂O₂Se") [Zhao et al., Appl. Phys. Lett. 2025](https://pubs.aip.org/aip/apl/article/127/20/202104/3372800/Bi₂O₂Se/TaNiTe₅ ohmic contact")。黑磷——天然 p 型，Ni/BP 退火 Rc = 0.365 kΩ·μm，但空气不稳定性和界面化学活性使"界面无序度最小化"成为首要瓶颈 [Perello et al., Nat. Commun. 2017](https://www.nature.com/articles/s41598-017-16845-w "BP metallic ohmic contacts")。**三支柱框架核心逻辑具有普适性，但各支柱的阈值和权重需针对不同材料校准。**

### 可用图片
（无本地图片资料。建议写作时设计：新型电极材料候选空间图、p 型 Rc 进展时间线图、三支柱框架在不同 2D 材料体系中的适用性矩阵图。）

### 仍需补充
- 电子化合物（Ca₂N 等）的实验器件验证（目前仅有 DFT 理论预测）
- 高熵金属电极的系统理论工作（当前为空白）
- 贝叶斯优化在接触材料设计中的专门应用文献
- 弹道极限下完整的接触理论模型（Akinwande 2025 为评论性分析）
- Sb₂Te₃ T-vdW 接触的 TLM 系统验证数据及在不同 TMDCs 上的普适性
- TSMC p 型合金接触的完整 DFT/能带结构数据

# Section 2：给 Write 阶段的执行建议

## 全文叙事逻辑
- 全文采用"问题定义→方法全景→机制提取→统一框架→工程落地→未来展望"的递进逻辑
- Chapter 1 奠定物理基础和问题定义，Chapter 2 提供完整的实验事实地图，Chapter 3 从事实中抽象出共通机制，Chapter 4 在机制基础上构建统一框架（本报告的核心智识贡献），Chapter 5 将视角从基础物理转向工程与产业需求，Chapter 6 基于统一框架展望未来
- 各章之间设计明确的逻辑过渡：Chapter 1 结尾引出"针对这些物理瓶颈，研究者发展了哪些方法？"；Chapter 2 结尾提出"这些方法背后是否有共通机制？"；Chapter 3 结尾引出"能否构建统一框架？"；Chapter 4 结尾转向"如何落地？"；Chapter 5 结尾引出"未来方向在哪？"
- Chapter 4 是全文的智识重心——三支柱框架（去钉扎-低隧穿-强耦合）为本报告的独创性贡献，前三章为其提供论据支撑，后两章展示其应用价值和前瞻指引

## 需严格核验的关键数据
- Bi 接触 Rc = 123 Ω·μm、SBH = 0 meV、I_on = 1,135 μA/μm（Shen et al., Nature 2021，已通过 researcher 核验）
- Sb(01̄12) 接触 Rc = 42 Ω·μm、I_on = 1.23 mA/μm（Li et al., Nature 2023，已核验）
- 量子极限 ~36 Ω·μm at n₂D ≈ 10¹³ cm⁻²（已核验）
- Liu et al. Nature 2018 转移金属法 S ≈ 0.96（已核验，但具体 Rc 数值需写作前再次确认原文是否报道 TLM 值）
- Y 掺杂 MoS₂ 平均 Rc = 69 Ω·μm、最低 43 Ω·μm（Jiang et al., Nat. Electron. 2024，已核验）
- ALB 接触 Rc = 70 Ω·μm、400°C 稳定（Gao et al., Science 2025，已核验）
- TSMC p 型合金 Rc ≈ 98 Ω·μm（IEDM 2024，来源为 TSMC 研究页面，写作前需确认是否有完整会议论文公开）
- 相变接触 Rc 从 ~1.1 kΩ·μm 降至 ~0.2 kΩ·μm（Kappera et al., Nat. Mater. 2014，为二手整理数值，写作前需核实原文精确值和测量条件）
- IRDS 路线图中 <100 Ω·μm 要求的具体版本和表格编号（当前引用为 Shen 2021 转述，写作前尝试查阅 IRDS 官方 PDF）
- imec 300 mm 平台 FAB Ti 接触 Rc 在数十至数百 kΩ·μm（imec 2026 论文，已核验）

## 需统一口径的术语与参数
- 接触电阻单位统一使用 Ω·μm（宽度归一化接触电阻 $R_c W$），必要时说明与面电阻率 Ω·cm² 的转换关系
- 肖特基势垒高度单位统一为 eV，标注 n 型或 p 型
- 载流子浓度统一使用 cm⁻² 表示（二维面密度）
- 器件结构参数（沟道长度、栅介质厚度、背栅/顶栅配置）在引用实验数据时需一并说明
- "费米钉扎因子"$S$（$S = d\Phi_B/d\Phi_M$）的定义需在 Chapter 1 首次出现时明确，后续统一使用
- "范德华接触"（接触类型）与"范德华间隙"（界面物理结构）需明确区分
- Bi 接触原文发表在 Nature 2021（非 Science 2021），全文中需统一

## 图表建议
- Chapter 1：金属-2D 半导体界面的能带示意图（含 MIGS 衰减、vdW 间隙、肖特基势垒标注）；接触电阻各分量的等效电路图
- Chapter 2：各方案接触电阻数值的横向对比表（统一归一化条件，标注 n₂D、温度）；关键实验方案的器件结构截面示意图
- Chapter 3：方法-机制映射矩阵图（10 种方案 × 5 个机制维度，标注主要/次要/不涉及/不利，已在 researcher 产出中完成初稿）
- Chapter 4：三支柱模型示意图（图形化表达去钉扎-低隧穿-强耦合三个条件）；各方案在三支柱空间中的定位图（✓✓/✓/△/✗ 评级可视化）
- Chapter 5：BEOL 兼容性矩阵图（接触方案 vs. 熔点/热稳定性/工艺温度）；学术最佳值 vs. FAB 集成值差距对比柱状图
- Chapter 6：新型电极材料候选空间图；p 型接触 Rc 进展时间线图（2014–2025）
- 全文建议包含一张 timeline 图（2014–2026 年关键突破的时间线）

## 关于统一框架（Chapter 4）的写作注意事项
- 三支柱框架尚未有文献提出（据 researcher 检索确认），应以本报告独创性贡献的口径行文
- Allain et al. Nat. Mater. 2015 已提出 R_c 分解框架（R_SB + R_tunnel），可作为三支柱框架的理论前驱致谢
- Su et al. J. Phys. D 2023 的"弱金属化"理论和修正 Schottky-Mott 规则是支柱三的重要理论基础
- 相变接触和 Y 掺杂通过"消除异质界面"绕过三支柱框架，需讨论框架的适用边界（补充"当异质界面被消除时，三支柱约束自动解除"的边界条件）
- "第四支柱"（界面缺陷最小化）的讨论应审慎处理：在学术理想条件下可作为三支柱生效的前提条件，但在 CVD 大面积材料的工程现实中可能需要升格为独立支柱

## 时间口径
- 回顾区间：~2014–2026 年（覆盖过去约 12 年的研究进展）
- 重点关注：2020 年以后的突破性工作
- 当前日期锚点：2026 年 4 月
