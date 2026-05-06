# Section 1：章节研究计划

## Chapter 1：数学与量子计算交叉领域——定义边界、演进脉络与当前热点
### 研究目标
- 界定"数学与量子计算交叉领域"的学科范畴，明确包含哪些数学分支（代数拓扑、表示论、概率论与随机矩阵、组合优化、数论与密码学、微分几何等）与量子计算技术栈（量子纠错码、拓扑量子计算、量子算法设计、量子模拟、容错架构等）之间的耦合
- 梳理从量子信息论萌芽到当前多学科深度融合的演进脉络，识别关键里程碑
- 识别 2025-2026 年度最活跃的研究前沿方向

### 关键发现

#### 核心数学分支与量子计算耦合关系
- 编码理论与量子纠错（QEC）是最深入的耦合方向。2021 年 Panteleev 与 Kalachev 利用非阿贝尔群上 lifted product 构造证明了渐近优良量子 LDPC 码的存在性 [Panteleev & Kalachev 原始论文](https://arxiv.org/abs/2111.03654 "Asymptotically Good Quantum and Locally Testable Classical LDPC Codes, 2021")。2022 年 Leverrier 和 Zémor 提出 Quantum Tanner Codes，基于二维 Cayley 复形构造了具有常数率和常数相对距离的量子 LDPC 码族 [Quantum Tanner Codes](https://arxiv.org/abs/2202.13641 "Leverrier & Zémor, FOCS 2022")。
- 代数拓扑与拓扑量子计算：Kitaev 于 1997 年提出 Toric Code 与任意子容错方案 [Kitaev 原始论文](https://arxiv.org/abs/quant-ph/9707021 "Fault-tolerant quantum computation by anyons, 1997/2003")。2025 年 2 月微软发布 Majorana 1 处理器，声称实现首个基于拓扑超导体的硬件保护量子比特，配套论文发表于 Nature [微软公告](https://azure.microsoft.com/en-us/blog/quantum/2025/02/19/microsoft-unveils-majorana-1-the-worlds-first-quantum-processor-powered-by-topological-qubits/ "2025-02-19")；[Nature 论文](https://www.nature.com/articles/s41586-024-08445-2 "Interferometric single-shot parity measurement in InAs–Al hybrid devices")。
- 数论与密码学以 Shor 算法为核心纽带。Shor 1994 年 FOCS 发表，1997 年完整版见 SIAM J. Comput. [Shor 算法](https://epubs.siam.org/doi/10.1137/S0097539795293172 "SIAM J. Comput. 26(5), 1997")。2024 年 8 月 NIST 正式发布首批三项后量子密码学标准 FIPS 203/204/205，数学基础为 Module-LWE 问题 [NIST 官方公告](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards "2024-08-13")。
- 概率论与随机矩阵理论应用于量子纠缠统计刻画、量子信道容量分析、监控量子电路相变等 [Random-Matrix Models of Monitored Quantum Circuits](https://link.springer.com/article/10.1007/s10955-024-03273-0 "J. Stat. Phys., 2024")。
- 表示论近年日益深入：Clifford 群与辛群联系支撑量子态断层扫描与基准测试。IBM 2025 年展示群论指导量子算法设计新方法 [IBM Quantum Blog](https://www.ibm.com/quantum/blog/group-theory "Discovering a new quantum algorithm via group theory, 2025")。Larocca 等人 2025 年 Nature Reviews Physics 综述提出基于李代数的荒原高原统一理论 [Larocca et al.](https://arxiv.org/abs/2405.00781 "Barren plateaus in variational quantum computing, Nature Reviews Physics 7(4), 2025")。
- 组合优化与 QAOA：2024 年 Science Advances 报告了 QAOA 在特定结构化问题上的扩展优势证据 [QAOA 扩展优势](https://www.science.org/doi/10.1126/sciadv.adm6761 "Science Advances, 2024")。
- 微分几何与量子控制论：量子门几何相位设计、量子态流形测地线搜索、Fisher 信息度量。
- 算子代数（C*-代数与 von Neumann 代数）：量子信道刻画、纠缠张量范畴、量子引力新应用。
- 数值分析与量子算法：QSP/QSVT 框架（2018-2019）统一描述几乎所有已知量子算法。2026 年 SIAM G2S3 暑期学校选定"容错量子计算算法"主题 [G2S3 2026](https://sites.duke.edu/siamss2026/ "Duke University, 2026")。

#### 关键里程碑年表
- 1982 年 Feynman 提出量子模拟构想；1984 年 Bennett-Brassard 提出 BB84 协议 [ACM 图灵奖公告](https://www.acm.org/media-center/2026/march/turing-award-2025 "2025 ACM Turing Award, 2026-03-18")
- 1994-1997 年 Shor 算法；1995-1996 年量子纠错码与 CSS 框架、Grover 搜索算法 [Grover](https://dl.acm.org/doi/10.1145/237814.237866 "STOC 1996")
- 1996-1999 年量子纠错阈值定理（Aharonov & Ben-Or, STOC 1997）[阈值定理](https://epubs.siam.org/doi/10.1137/S0097539799359385 "SIAM J. Comput., 2008")
- 1997-2003 年 Kitaev Toric Code；2009 年 HHL 算法
- 2018-2019 年 QSP/QSVT 大一统框架
- 2021-2022 年 qLDPC 码理论突破（Panteleev-Kalachev 和 Leverrier-Zémor）
- 2024 年 8 月 NIST 发布首批 PQC 标准；2024 年 12 月 Google Willow 处理器首次实现低于阈值的表面码量子纠错，distance-7 码逻辑错误率每轮 0.143%±0.003%，误差抑制因子 Λ=2.14±0.02 [Google Willow 论文](https://www.nature.com/articles/s41586-024-08449-y "Nature 638, 920–926, 2025")
- 2025 年 2 月微软 Majorana 1 发布；2025 年 Shor 获 IEEE Shannon 奖 [IEEE 公告](https://www.itsoc.org/news/shannon-award-2025 "Shannon Award 2025: Peter Shor")
- 2026 年 3 月 Bennett-Brassard 获 2025 年图灵奖

#### 标志性学术事件
- 2024 年 10 月 SIAM Quantum Intersections Convening（NSF 资助 DMS-2425995，80+ 与会者），梳理数学可贡献于量子研究的五大方向，建议 NSF 加大交叉资助并创建 SIAM Activity Group on QIS [SIAM QIC 报告](https://www.siam.org/media/orydkrzd/quantum-convening-report.pdf "2024")
- 2025 年联合国"国际量子科学与技术年"（IYQ 2025），开幕仪式 2025 年 2 月巴黎 UNESCO 总部 [UNESCO 页面](https://www.unesco.org/en/years/quantum-science-technology "IYQ 2025")
- 2026 年 7-8 月 Gene Golub SIAM 暑期学校（Duke 大学）主题为容错量子计算算法

#### 2025-2026 年度八大研究前沿
1. 量子 LDPC 码实用化与解码算法（有限长度优化、belief propagation 适配、硬件拓扑协同设计）[IBM qLDPC](https://www.ibm.com/quantum/blog/qldpc-codes "Computing with error-corrected quantum computers")
2. 拓扑量子计算实验验证与数学基础深化（非阿贝尔任意子辫子群完备性、拓扑+qLDPC 码协同）
3. QSP/QSVT 框架深化（多变量推广、最优度数界、block-encoding 拓展）
4. 变分量子算法可训练性与荒原高原数学理论（李代数框架、去量子化边界）
5. 量子学习理论与经典影子断层扫描（信息论最优界）
6. 后量子密码学安全性精细分析（Module-LWE 攻击复杂度、格基约化渐近行为）
7. 量子哈密顿量模拟数学最优性（Trotter-Suzuki 误差界、局部结构利用）
8. 量子优势数学边界与去量子化（可证明超多项式优势的精确条件）

### 可用图片
- 无直接相关图片素材（/data/ 下的图表脚本与量子化学电场相关，与本章不相关）

### 仍需补充
- 量子信息几何方向（Fisher 信息度量在量子参数估计中的应用）的 2025-2026 年度标志性 T1/T2 来源
- Quantum Tanner Codes 单轮解码（Gu, Pattison, Tang 2024）的数学要点详细提取
- SIAM Activity Group on QIS 截至 2026 年 3 月是否已正式成立的核实


## Chapter 2：全球主要研究团队画像——北美与欧洲
### 研究目标
- 系统梳理北美（美国、加拿大）和欧洲主要从事数学-量子计算交叉研究的学术团队与机构
- 建立可比较的团队画像：核心研究方向、带头人、机构定位（纯学术型 vs. 产学研融合型）、比较优势
- 覆盖 MIT、Caltech IQIM、IBM Research、Google Quantum AI、微软 Station Q、Waterloo IQC、Perimeter Institute、Oxford、ETH Zurich、Max Planck、QuTech 等

### 关键发现

#### 北美学术团队
- **MIT QIS 理论群**（纯学术型，跨系协同）：核心人物包括 Peter Shor（数学系，Shor 算法/CSS 码奠基人）、Aram Harrow（HHL 算法共同发明人）、Anand Natarajan（量子复杂性理论，MIP*=RE 核心贡献者，2024 年获 NSF CAREER 基金）、Soonwon Choi（量子多体动力学）[MIT CTP QIS 页面](https://physics.mit.edu/research/labs-centers/mit-center-for-theoretical-physics-leinweber-institute/research-efforts-in-the-center-for-theoretical-physics/quantum-information-science/ "MIT 官方介绍")。在量子复杂性理论与量子算法设计领域居全球领先地位。
- **Caltech IQIM**（纯学术+产学研融合）：John Preskill（量子信息理论开创者，NISQ 概念提出者）、Alexei Kitaev（拓扑量子计算数学奠基人，Toric Code）、Fernando Brandão（同时任 AWS 应用科学总监）、Thomas Vidick（MIP*=RE 核心贡献者）、Urmila Mahadev（可验证量子计算）。2025 年 2 月 Brandão 团队与 AWS 在 Nature 发表 Ocelot 猫态量子比特芯片的硬件高效量子纠错方案 [Nature 论文](https://www.nature.com/articles/s41586-025-08642-7 "Hardware-efficient QEC via concatenated bosonic qubits, 2025")。IQIM 在拓扑理论、复杂性和产学研融合方面具有全球稀有的综合优势。
- **Waterloo IQC + Perimeter Institute**（产学研融合+纯理论）：David Gosset（量子算法与经典模拟）、Daniel Gottesman（Perimeter，稳定子形式主义创始人）、Michele Mosca（后量子密码学）。IQC 自 2002 年成立以来累计发表 3,000 余篇论文、获 119,000 次引用、累计获超 7.8 亿加元研究资金 [IQC 官方页面](https://uwaterloo.ca/institute-for-quantum-computing/about "IQC 关键统计")。在后量子密码学和量子算法复杂性理论方面积累深厚。
- **LANL 量子计算中心**（国家实验室型）：2026 年 2 月正式成立，整合三十余名量子研究人员。研究方向包括变分量子算法数学分析、量子机器学习数学基础；2025 年从数学上证明量子神经网络可形成高斯过程 [LANL 公告](https://www.lanl.gov/media/news/0203-quantum-computing-focused-research-center "2026-02-03")。

#### 北美工业界研究团队
- **IBM Quantum 研究院**（工业研究院）：Sergey Bravyi（bivariate bicycle 码首席设计者）、Andrew Cross、Theodore Yoder。2024 年 3 月在 Nature 627 发表 BB-LDPC 码，实现 0.7% 纠错阈值，仅用 288 个物理量子比特保护 12 个逻辑量子比特近 100 万个综合征测量周期 [Bravyi et al.](https://www.nature.com/articles/s41586-024-07107-7 "Nature 627, 778–782, 2024")。2025 年 8 月发布 Relay-BP 解码算法 [IBM 博客](https://www.ibm.com/quantum/blog/relay-bp-error-correction-decoder "2025-08-04")。全球少数能从码理论到物理实现一体化推进的团队。
- **Google Quantum AI**（工业研究院）：Hartmut Neven（2025 TIME AI 100）、Ryan Babbush（算法与应用总监）、Sergio Boixo（量子优越性理论设计者）、Craig Gidney（表面码资源估计）、Jeongwan Haah（代数量子码）。2024 年 12 月 Nature 发表 Willow 处理器低于阈值的表面码纠错实验 [TIME AI 100](https://time.com/collections/time100-ai-2025/7305880/hartmut-neven/ "Hartmut Neven")。擅长量子资源估计和容错算法的实际开销分析。
- **Microsoft Station Q / Microsoft Quantum**（工业研究院）：Michael Freedman（Fields 奖得主 1986，拓扑量子计算数学奠基人）、Chetan Nayak、Matthew Hastings、Zhenghan Wang（辫子群表示论/模张量范畴）。2025 年 2 月发布 Majorana 1 拓扑量子处理器及 200+ 人合著容错路线图论文 [Nature 论文](https://www.nature.com/articles/s41586-024-08445-2 "Interferometric parity measurement, 2025")。全球唯一以拓扑量子计算为核心路线的主要工业机构，数学理论深度在工业界无出其右。

#### 欧洲学术与研究团队
- **ETH Zurich QIT 组**（纯学术型）：Renato Renner 领导，专攻量子密码学信息论基础（min-entropy 框架、QKD 安全性证明），近年拓展至量子引力信息论视角（WOST 联盟）[ETH Zurich QIT](https://qit.ethz.ch/the-group.html "官方页面")。
- **Oxford 量子计算组**（纯学术型）：Aleks Kissinger（ZX-calculus 核心开发者）、Jonathan Barrett（量子因果结构）。ZX-calculus 是该组原创贡献，已成为 PyZX/QuiZX 等开源量子编译器数学基础，被 Quantinuum 采用 [Oxford CS Quantum](https://www.cs.ox.ac.uk/activities/quantum/ "官方页面")。
- **FU Berlin Eisert 组**（纯学术型）：Jens Eisert 以数学物理严格性为指导，在张量网络理论、量子态认证与设备验证数学框架方面处于欧洲领先 [AG Eisert](https://www.physik.fu-berlin.de/en/einrichtungen/ag/ag-eisert/index.html "官方页面")。
- **INRIA/波尔多大学**（学术+政府研究机构）：Anthony Leverrier（INRIA Paris）与 Gilles Zémor（波尔多大学），2022 年提出 Quantum Tanner Codes（FOCS 2022），基于 Cayley 复形构造常数率常数距离 qLDPC 码族，是渐近优良 qLDPC 码两大突破之一 [arXiv](https://arxiv.org/abs/2202.13641 "Leverrier & Zémor, FOCS 2022")；[INRIA 报道](https://www.inria.fr/en/error-correcting-codes-fundamental-results-quantum-computer "INRIA 官方")。代表纯代数编码理论驱动的量子纠错路线。
- **QuSoft/CWI + QuTech（荷兰）**：Harry Buhrman（1996 年即开始量子计算研究，全球最早的理论研究者之一）、Ronald de Wolf（量子查询复杂性）。QuSoft 约 100 人规模，核心优势在量子算法复杂性理论与量子软件 [QuSoft](https://qusoft.org/ "官方页面")。
- **Max Planck 体系**：量子计算数学力量分散在 MPQ（Garching）、MPL（Erlangen）、MPI-MiS（Leipzig）等所，优势在纯基础研究自由度和长期稳定资金。

#### 以色列
- **Hebrew University QISC**（学术型，2011 年成立，27 个研究组）：Dorit Aharonov（量子计算复杂性理论核心人物，容错阈值定理共同证明者，2023 年当选美国 NAS 外籍院士，同时任 QEDMA 首席科学家）[NAS 页面](https://www.nasonline.org/directory-entry/dorit-aharonov-i0a4uv/ "Dorit Aharonov")。2024 年 12 月联合 Yissum 推出以色列首台国产超导量子计算机（20 量子比特）。

#### 团队差异化定位
- 偏纯数学理论：Caltech IQIM（Kitaev）、Microsoft Station Q（Freedman/Wang）、Oxford（ZX-calculus）、ETH Zurich（Renner）
- 偏算法设计：MIT（Shor/Harrow/Natarajan）、QuSoft/CWI（Buhrman/de Wolf）、Perimeter（Gosset/Gottesman）
- 偏纠错码构造：INRIA/波尔多（Leverrier/Zémor）、IBM（Bravyi/Cross/Yoder）、Google QAI（Gidney/Haah）
- 产学研融合：Caltech/AWS（Brandão）、IBM Quantum、Google QAI、IQC-Waterloo、Hebrew U/QEDMA（Aharonov）

### 可用图片
- 无直接相关图片素材

### 仍需补充
- Weizmann Institute 量子计算理论力量的覆盖（归章待定：Chapter 2 或 Chapter 3）
- 各团队精确规模数据（全职研究人员/博士后数量），多数团队 T1/T2 来源不足
- Max Planck 体系内量子计算数学理论的具体带头人识别
- Jens Eisert 组 2024-2026 年度具体里程碑式数学理论贡献的论文引用
- IQC NRC 1.61 亿加元投资需核实加拿大政府官方 T1 来源（当前仅有 LinkedIn T3 来源）


## Chapter 3：全球主要研究团队画像——亚太地区及其他新兴力量
### 研究目标
- 系统梳理亚太地区及其他新兴力量中从事数学-量子计算交叉研究的主要学术团队与机构
- 建立与 Chapter 2 口径一致的团队画像
- 覆盖中国、日本、澳大利亚、新加坡、以色列等

### 关键发现

#### 中国
- **USTC 潘建伟/陆朝阳团队**（产学研融合型）：2025 年 12 月在 PRL 135 发表全微波泄漏抑制 distance-7 表面码 QEC，逻辑错误抑制因子 Λ=1.40(6)，为美国以外首次实现低于阈值的表面码量子纠错 [He et al., PRL 135, 260601](https://link.aps.org/doi/10.1103/rqkg-dw31 "2025-12-22")。核心优势以实验-工程为主导，数学理论原创性低于 IBM Bravyi 组或 INRIA Leverrier-Zémor 组。
- **清华 IIIS-CQI**（纯学术型）：图灵奖得主姚期智创立，段路明（2024 年获国际量子奖）任执行主任。姚期智是最早将理论计算机科学工具引入量子信息领域的核心人物之一（1993 年量子通信复杂性模型）。2025 年 1 月段路明团队首次在双重编码量子比特间实现高保真度纠缠门 [CQI 官方页面](https://iiis.tsinghua.edu.cn/lzzx/zxjj.htm "CQI 中心简介")。
- **清华 YMSC 刘子文**（纯数学学术型）：2024 年 9 月连续发表两篇 PRL——协变量子纠错码（SU(2) 对称性框架）和镶嵌码（几何旋转实现编码量子逻辑门），代表中国在纯数学驱动 QEC 方面的前沿，最接近 INRIA Leverrier-Zémor 代数编码理论传统 [清华求真书院报道](https://qzc.tsinghua.edu.cn/info/1017/7694.htm "两篇 PRL 论文详细介绍")。
- **BAQIS 北京量子信息科学研究院**（新型研发机构，2017 年成立）：龙桂鲁（量子安全直接通信开创者）任副院长。2024 年接收百度量子实验室捐赠设备 [CSIS 分析报告](https://www.csis.org/analysis/understanding-chinas-quest-quantum-advancement "Understanding China's Quest for Quantum Advancement")。

#### 日本
- **RIKEN RQC**（国家级研究机构）：两大理论团队——藤井啓祐（容错量子计算架构/量子软件，PRA 2018 量子电路学习引用超 2200 次，2025 年入选 IYQ Quantum 100）[IYQ Quantum 100](https://quantum2025.org/quantum-100/professor-keisuke-fujii/ "Keisuke Fujii")；Bartosz Regula（量子资源理论数学基础，2023 年 Nature Physics 否定纠缠操控"第二定律"，属里程碑级成果）[RIKEN 数学量子信息团队](https://www.riken.jp/en/research/labs/rqc/math_qtm_inf_riken_hakubi/index.html "Bartosz Regula")。
- **大阪大学 QIQB**（产学研融合型）：藤井啓祐兼任副主任，2025 年 6 月开发更高效魔态制备方法，与富士通合作推进实用量子计算。
- **名古屋大学 Le Gall 组**（纯学术型）：François Le Gall 专攻量子分布式算法和代数复杂性理论，2024 年发表量子机器学习鲁棒去量子化工作 [Le Gall 出版物](https://francoislegall.com/publications.html "Publications")。
- **NTT CIS Lab**（工业研究院型）：Crypto 2025 发表 23 篇论文（占全部被接收论文约 15%）并获最佳论文奖——首个标准模型下一次性签名方案，解决量子密码学十年未解问题 [NTT 公告](https://ntt-research.com/ntt-presents-23-papers-and-receives-best-paper-award-at-crypto-2025/ "Crypto 2025")。在后量子密码学数学理论方面居全球工业研究机构之首。

#### 澳大利亚
- **悉尼大学量子理论组**（纯学术型）：Stephen Bartlett（引用超 15,400 次）、Dominic Williamson。2024 年 11 月 Williamson 在 Nature Communications 发表 Layer Codes，在三维拓扑码中实现 L² 级错误处理能力，解决十余年公开问题 [悉尼大学报道](https://www.sydney.edu.au/news-opinion/news/2024/11/11/layer-codes-quantum-error-correction-quantum-hard-drive.html "Layer Codes, Nature Communications 2024")。2025 年获 ARC 卓越中心支持，为南半球量子计算数学理论领军力量。
- **UNSW**（产学研融合型）：以硅基量子比特实验为核心（Andrea Morello），理论力量偏实验理论，纯数学原创性低于悉尼大学。

#### 新加坡
- **CQT**（国家旗舰研究中心，约 200 人）：Rahul Jain（QIP=PSPACE 定理证明者之一，FOCS 2024/STOC 2024 发文）、Troy Lee（量子查询复杂性）、Miklos Santha（CNRS 联合任命）。核心优势在量子通信复杂性理论和量子密码学信息论基础 [CQT Rahul Jain](https://www.cqt.sg/people/rahul-jain/ "CQT PI")。2025 年 3 月新加坡 NRF 向量子-超算集成投入 2450 万美元。

#### 韩国
- **KAIST 量子大学院**（学术型，快速建设期）：2026 年 1 月与 MIT 建立量子计算合作关系，启动国家量子制造设施 [朝鲜日报](https://www.chosun.com/english/industry-en/2026/01/26/ZJOK5WFHLRBHTM4VZ7XYDN3U7Y/ "KAIST Quantum, 2026-01-26")。理论积累尚不及 RIKEN/CQT，但加速追赶中。

#### 印度
- **TIFR/IISc**（学术型）：印度国家量子使命 2023 年启动，投资约 60 亿卢比（约 7.3 亿美元）。优势在理论计算机科学人才储备（TIFR-TCS 传统），但受限于实验基础设施，贡献以纯理论为主；人才外溢效应显著（如 Jain 从 TIFR 到 CQT）[The Quantum Insider](https://thequantuminsider.com/2024/11/27/quantum-computing-advancements-in-india/ "Quantum Computing in India, 2024")。

#### 以色列（补充 Chapter 2）
- **Weizmann Institute 量子中心**（纯学术型，22 位 PI）：Thomas Vidick 2024 年从 Caltech 全职转入，使 Weizmann 成为量子复杂性理论全球新高地。Vidick 在 FOCS 2024 发表高维立方复形构造及量子 LTC 应用（与 Dinur、Lin 合作）。Zvika Brakerski 在后量子密码学/格密码学方面居全球前列。Ady Stern 在拓扑量子计算数学物理（任意子理论）方面有核心贡献 [Weizmann 量子中心](https://centers.weizmann.ac.il/quantum-science-technology/members/principal-investigators "PI 列表")。Vidick-Brakerski-Stern 组合使 Weizmann 形成量子复杂性+后量子密码+拓扑物理的多维度集群。

#### 与北美欧洲头部团队的比较
- 纯数学理论深度：Regula（RIKEN）vs. Renner（ETH）、Vidick（Weizmann/原 Caltech）与 MIT Natarajan 同一梯队
- 算法复杂性：CQT Jain 与 CWI Buhrman 同一梯队
- 纠错码构造：悉尼 Layer Codes 与 INRIA Leverrier-Zémor 代数码构成互补路线
- 实验-理论闭环：USTC 表面码 QEC 追平 Google Willow，但纯数学码构造理论弱于 IBM Bravyi 组

### 可用图片
- 无直接相关图片素材

### 仍需补充
- 中科院理论物理研究所（ITP-CAS）量子计算理论团队的具体带头人和近期数学理论成果
- 南方科技大学（SUSTech）在数学-量子计算交叉方向的具体团队画像
- 东京大学 Murao 量子信息组 2024-2025 年度数学理论贡献细节
- Vidick 从 Caltech 转至 Weizmann 的确切时间（需与 Chapter 2 统一口径：注明流动情况）
- CQT 精确资金规模需从新加坡 NRF 官方确认


## Chapter 4：研究产出、影响力与国际合作网络
### 研究目标
- 从论文发表、引用影响力、国际合作网络三个维度对全球主要团队进行横向比较和定量分析
- 识别高影响力期刊/会议（Nature/Science 系列、PRL/PRX Quantum、QIP/STOC/FOCS 等）的发文分布
- 分析国际合著网络的核心节点、主要合作轴线、跨大洲合作密度及演变趋势

### 关键发现

#### 论文产出定量概览
- 2026 年 1 月 EPJ Quantum Technology 发表的综合文献计量研究覆盖 Scopus 1980-2025 年 31,662 篇量子计算论文，显示 2015 年起进入指数增长，2024 年达发文峰值 [EPJ QT](https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4 "Mapping the quantum computing landscape, 2026-01-15")
- 机构层面：USTC 以 1,877 篇居全球首位，其后依次为加州大学系统（1,040）、CNRS（759）、中科院（729）、滑铁卢大学（600）、MIT（593）、牛津大学（534）、新加坡国立大学（493）[EPJ QT](https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4 "Table 2: Most prolific institutions")
- 按国家：美国 27,092 篇（国家-论文实例计数）居首，中国 25,407 篇紧随，但以通讯作者计中国（6,695）略超美国（6,601）[EPJ QT](https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4 "Figs. 5-6")
- 公共资助：NSFC 超 3,000 个量子相关项目居全球首位，美国 NSF 约 2,450 个，欧盟委员会超 2,000 个 [EPJ QT](https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4 "Table 7")
- 学科分布以物理与天文学（30.3%）和计算机科学（24.5%）为主；发文渠道集中于 PRA 系列、PRL、PRR、PRB 等 Q1 期刊

#### 引用影响力
- 31,662 篇论文累计获 804,137 次引用，篇均 25.40 次，h-index=311。按国家：美国篇均 44.0 次，中国篇均 11.9 次，差距与中国强调国内发表有关 [EPJ QT](https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4 "Table 6")
- FWCI（场加权引用影响力，2017-2021 Scopus/SciVal）：加拿大 2.13 > 美国 2.07 > 英国 2.02 > 法国/德国 1.88 > 中国 1.48（均高于世界平均 1.0）[英国国家量子战略附加证据](https://assets.publishing.service.gov.uk/media/6572db4433b7f20012b720b7/national-quantum-strategy-additional-evidence-annex.pdf "DSIT, Table 1, 2023-12")
- ASPI 关键技术追踪器 2025 更新：中国在 74 项关键技术中 66 项领先，但美国在量子计算等 8 项仍领先；中国在前 10% 高质量论文中均超美国 [Nature 报道](https://www.nature.com/articles/d41586-025-04048-7 "Nature 649, 13-14, 2025-12-12")
- 共被引网络呈"双核"结构：基础理论集群（Shor/Grover/Nielsen&Chuang 为中心）+ 近期应用集群（NISQ/变分方法/QML），通过 QAOA 等关键节点耦合

#### 国际合作网络
- 全球量子计算合著网络：密度 0.2174，平均路径长度 1.93，聚类系数 0.7349，小世界 sigma=3.21。度中心性美国最高（0.745），特征向量中心性美国居首（0.198）。中介中心性印度领先（0.114），扮演桥梁角色 [EPJ QT](https://link.springer.com/article/10.1140/epjqt/s40507-026-00464-4 "Fig. 8 & Section 3.2")
- **中美合作收缩**：Kitajima & Okamura（2025 年 3 月 Nature HSSC）研究发现中美合作距离自 2019 年起出现"反转 J 曲线"，为双边关系独有现象。InCites 数据显示中国论文国际合著比从 2018 年 26.6% 降至 2023 年约 19.4%（降 7.2pp），中美合著份额降 6.4pp [Kitajima & Okamura](https://www.nature.com/articles/s41599-025-04550-3 "Nature HSSC, 2025-03-03")；[Scientific American](https://www.scientificamerican.com/article/china-u-s-science-collaborations-are-declining-slowing-key-research/ "2024-07-24")
- 美国 NSTC 2024 年 8 月报告：2018-2022 年美国 QIST 研究约一半涉及国际合作（高于全科学 40% 均值）。联邦 QIST 支出从 2019 年约 4.5 亿美元倍增至 2022 年超 10 亿美元 [NSTC 报告](https://www.quantum.gov/wp-content/uploads/2024/08/Advancing-International-Cooperation-in-QIST.pdf "2024-08")
- 合作伙伴再平衡：中国向 EU 知识流率上升，美国强化与 11 国双边量子合作声明（澳/丹/芬/法/德/日/韩/荷/瑞典/瑞士/英）[NSTC 报告](https://www.quantum.gov/wp-content/uploads/2024/08/Advancing-International-Cooperation-in-QIST.pdf "11 bilateral statements")
- 关键字共现："量子机器学习""后量子密码学"增长最快，"量子计算"与"QML"共现最频（263 篇）

#### 新兴合作模式
- Google QAI 2025 年 Nature Electronics 论文将量子计算比作"CERN/LIGO 级大科学设施"，呼吁加强产学合作
- 学术-工业界界限日趋模糊：Brandão 双重身份模式（Caltech/AWS）、Microsoft 200+ 人合著容错路线图

### 可用图片
- 无直接相关图片素材

### 仍需补充
- PRX Quantum 2020-2025 各年度精确发文量（当前仅有 2022 年约 306 篇的第三方估计）
- STOC/FOCS/QIP/Crypto 在数学-量子计算交叉方向的年度发文趋势（需从 DBLP 或会议官网统计）
- Chapter 2-3 各团队在特定渠道（Nature/Science/PRL/PRX Quantum）的逐团队发文对比
- 中美量子计算子领域专项合著数据（USCC "Vying for Quantum Supremacy" 2024 报告待获取）
- 新兴期刊（PRX Quantum、Quantum、npj QI）的 2024-2025 年度影响因子/CiteScore


## Chapter 5：资金支持、政策环境与工业界合作
### 研究目标
- 比较各主要国家/地区的政府量子计算投资规模和政策框架
- 分析科技巨头的量子数学研究投入和学术合作模式
- 评估资金与政策如何实质性地影响研究方向和团队竞争力

### 关键发现

#### 全球政府量子投资规模
- 截至 2025 年 10 月，全球各国政府自 2013 年以来累计承诺量子科技投资约 557 亿美元，但 OECD 指出这些数字通常反映计划预算而非实际拨付 [OECD 报告](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/an-overview-of-national-strategies-and-policies-for-quantum-technologies_33a0b249/5e55e7ab-en.pdf "OECD Digital Economy Papers No. 379, 2025-12")
- OECD Fundstat 数据库（19 个成员国+欧盟）2015-2023 年识别 12,209 个量子 R&D 项目，累计资助约 111 亿美元（PPP），项目均值 92 万美元/项。2022-2023 年占时段总量三分之一以上 [OECD 报告](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/an-overview-of-national-strategies-and-policies-for-quantum-technologies_33a0b249/5e55e7ab-en.pdf "Figure 3")
- 2025 年初公共融资公告加速：日本 74 亿美元（量子专项约 9 亿美元）、西班牙 9 亿美元，前四个月公共融资已超 100 亿美元 [McKinsey QT Monitor 2025](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-year-of-quantum-from-concept-to-reality-in-2025 "Exhibit 2")

#### 主要国家投资详情
- **美国**：联邦 QIS R&D 从 FY2019 的 4.56 亿美元增至 FY2022 峰值 10.41 亿美元，FY2025 预算申请 9.98 亿美元。NQI 第一期约 12 亿美元（2019-2024），再授权追加 18 亿美元（2025-2029）。DOE 2025 年 11 月宣布 6.25 亿美元续期五个国家 QIS 研究中心。DARPA QBI 最高 3.15 亿美元 [NQI FY2025 报告](https://www.quantum.gov/wp-content/uploads/2024/12/NQI-Annual-Report-FY2025.pdf "Figure 2.1")；[DOE 公告](https://www.energy.gov/articles/energy-department-announces-625-million-advance-next-phase-national-quantum-information "2025-11-04")；[CSIS](https://www.csis.org/analysis/government-demand-creator-quantum-industry "2026-03")
- **中国**：常被引用"150 亿美元"数字存争议，陆朝阳指出实际可能仅为公开数字三分之一左右。NSFC 超 3,000 个量子相关项目居全球首位。2025 年"第二代量子体系"重大研究计划指南涵盖培育/重点/集成项目 [OECD 报告](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/an-overview-of-national-strategies-and-policies-for-quantum-technologies_33a0b249/5e55e7ab-en.pdf "China: actual expenditures unreported")；[NSFC 公告](https://www.nsfc.gov.cn/p1/3381/2824/79525.html "2025-05-13")
- **欧盟**：Quantum Flagship 至少 10 亿欧元（2018-2028）。德国约 20 亿欧元，法国 18 亿欧元，英国 25 亿英镑十年计划（2026 年 3 月追加 20 亿英镑），荷兰 6.15 亿欧元
- **亚太**：韩国约 23 亿美元（至 2035 年），加拿大 2025 年联邦预算拨 3.34 亿加元五年期计划，澳大利亚累计超 23 亿澳元，印度约 10 亿美元，新加坡超 3 亿美元，以色列 VC 驱动超 6.5 亿美元

#### 数学基础研究专项资金与政策
- SIAM QIC 报告（2024 年 10 月）核心发现：数学科学界在量子研究中"基本缺席"。提出四大建议：支持数学-QIS 交叉 R&D、加强教育与劳动力、增加资金与联网机制、与数学学会合作建设社区 [SIAM QIC 报告](https://www.siam.org/media/orydkrzd/quantum-convening-report.pdf "DOI: 10.11337/25M1741017")
- NSF DMS 已资助多个量子交叉项目：C*-代数量子力学（DMS-2406319）、量子拓扑/量子信息（DMS-2350250）、拓扑量子计算（DMS-2327208）等。但 DOE ASCR 明确排除量子算法和密码学资助，使 NSF DMS 成为数学家从事量子算法基础研究的最关键联邦来源 [NQI FY2025 报告](https://www.quantum.gov/wp-content/uploads/2024/12/NQI-Annual-Report-FY2025.pdf "Section 3.2 NSF")
- **FY2026 预算风险**：总统提案将 NSF 总预算从约 90 亿美元削减 55.8% 至 39 亿美元。虽量子被列为"优先领域"，但未提出新投资或提及 NQI，国会将最终决定 [The Quantum Insider](https://thequantuminsider.com/2025/05/02/white-house-budget-preserves-quantum-funding-but-signals-caution-on-emerging-tech-spending-expansion/ "2025-05-02")
- 各国量子战略普遍侧重硬件和应用，对"数学基础"的专门重视程度较低。SIAM QIC 是已知唯一由主要数学学会组织的、以整合数学家进入量子研究为目标的大型行动

#### 工业界合作模式
- 2024 年全球 QT 初创企业融资近 20 亿美元（同比+50%），量子计算公司收入约 6.5-7.5 亿美元。QT 专利 IBM 191 项居首，Google 168 项次之。但量子私人投资 26 亿美元仅占 AI 投资 1,090 亿美元的 2.4% [McKinsey QT Monitor 2025](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-year-of-quantum-from-concept-to-reality-in-2025 "2025")；[CSIS](https://www.csis.org/analysis/government-demand-creator-quantum-industry "2026-03")
- IBM Quantum：开源 Qiskit 生态、Network 200+ 合作伙伴、大学驻地量子系统（2024 年 RPI 首台）、4 万学生教育合作（日本/韩国）[IBM 新闻室](https://newsroom.ibm.com/2024-04-05-Rensselaer-Polytechnic-Institute-and-IBM-unveil-the-worlds-first-IBM-Quantum-System-One-on-a-university-campus "2024-04-05")
- Google QAI 2025 年 Nature Electronics 呼吁产学"大科学设施"式合作
- Microsoft Station Q：科技巨头中对纯数学理论投入最深的案例（Fields 奖得主领衔，自 2006 年持续投资拓扑数学）
- 人才旋转门日趋活跃：Brandão（Caltech/AWS）、Bravyi（IBM）、JPMorgan Chase 量子研究团队参与 SIAM QIC 核心角色

#### 国际合作格局变迁
- OECD 数据：量子研究国际合作强度自 2019 年下降，国际共同作者率从约 33% 降至 2022 年低于 30%，美-EU 量子合作强度 2018-2022 年间降 15% [OECD 报告](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/an-overview-of-national-strategies-and-policies-for-quantum-technologies_33a0b249/5e55e7ab-en.pdf "Figure 5")
- 多国已宣布量子技术出口管制（34 量子比特以上量子计算机禁止出口），但"为什么这一阈值构成有意义的国家安全风险，专家并不清楚"[OECD 报告](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/an-overview-of-national-strategies-and-policies-for-quantum-technologies_33a0b249/5e55e7ab-en.pdf "Section 1.5.1")

### 可用图片
- 无直接相关图片素材

### 仍需补充
- 各国量子投资中"数学基础研究"的具体占比拆分（目前无任何国家单独报告此类数据）
- 中国 NSFC 数理科学部量子交叉方向的精确资助金额和项目数
- Microsoft Station Q 和 AWS 量子理论研究的具体投入规模（未公开披露）
- 百度/阿里巴巴量子研究院 2024-2025 年的合作项目和投入细节
- NSF FY2026 预算最终走向（截至 2026 年 3 月仍在国会审议）
- 日本 Moonshot 计划中量子-数学交叉的专项资金比例


## Chapter 6：突破潜力评估与关键理论/技术预测
### 研究目标
- 综合研判哪些团队/方向最有可能在 2026-2036 年推动重大突破
- 对候选突破方向逐一评估，预测关键性数学理论或应用技术
- 分析实现路径与条件

### 关键发现

#### 候选突破方向成熟度评估

**1. qLDPC 码实用化——"临界突破"状态，最高优先级**
- IBM BB 码（Nature 2024）以 288 物理比特保护 12 逻辑比特，阈值 0.7%，编码效率较表面码提升约 10 倍 [Bravyi et al.](https://www.nature.com/articles/s41586-024-07107-7 "Nature 627, 2024")。2025 年 8 月发布 Relay-BP 解码算法。2025 年 11 月 IBM Loon 实验处理器实现 qLDPC 码实时经典解码（延迟<480ns），比原计划提前一年 [IBM 新闻室](https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance "Loon: one year ahead of schedule")
- Riverlane 2025 年报告：2025 年 1-10 月 QEC 码相关论文达 120 篇（2024 全年仅 36 篇），呈"QEC 码爆炸"趋势，预测 2026 年其他工业玩家将跟进 qLDPC [Riverlane](https://www.riverlane.com/blog/quantum-error-correction-our-2025-trends-and-2026-predictions "QEC code explosion")
- 剩余障碍：有限长度码在真实噪声下的性能优化、高连通性硬件拓扑工程、实时解码延迟匹配
- 核心团队：IBM Bravyi 组、INRIA Leverrier-Zémor、Google Haah、悉尼 Williamson

**2. 拓扑量子计算——高风险/高回报，争议未消**
- Microsoft Majorana 1（2025 年 2 月）8 个拓扑量子比特，配套容错路线图六个里程碑 [Nature 论文](https://www.nature.com/articles/s41586-024-08445-2 "2025")；[路线图](https://quantum.microsoft.com/en-us/vision/quantum-roadmap "Six milestones")
- 学术争议：Science 报道"许多物理学家认为微软尚未提供马约拉纳准粒子存在的确凿证据"[Science](https://www.science.org/content/article/debate-erupts-around-microsoft-s-blockbuster-quantum-computing-claims "2025")。澳大利亚团队指出 1/f 噪声导致退相干时间<1μs，远短于门操作所需 32.5μs [HPCwire](https://www.hpcwire.com/2025/07/02/another-challenge-to-microsofts-majorana-quantum-roadmap/ "2025-07-02")
- 需要数学突破：非阿贝尔任意子辫子群计算完备性证明、拓扑保护在真实材料中的定量理论、拓扑码与 qLDPC 码协同方案
- 核心团队：Microsoft Station Q（Freedman/Nayak/Hastings/Wang）、Caltech Kitaev、Weizmann Stern

**3. QSP/QSVT 框架成熟化——稳步推进**
- 2025 年 Rossi-Ceroni-Chuang 在 Quantum 9:1776 发表模块化多变量 QSP 理论，将 QSP 重构为函数式编程中的单子类型 [Rossi et al.](https://quantum-journal.org/papers/q-2025-06-18-1776/ "Modular QSP in many variables, 2025")。2024 年 Dong-Lin 发表 Infinite QSP [Quantum 8:1558](https://doi.org/10.22331/q-2024-12-10-1558 "2024")
- 剩余障碍：多变量最优度数界不完整、block-encoding 高效构造瓶颈、相位因子计算数值稳定性
- 核心团队：MIT Chuang 组、UC Berkeley Lin Lin、RIKEN Fujii 组

**4. 后量子密码学纵深发展——制度基础就位**
- NIST 2025 年 3 月选定 HQC 为第五个 PQC 算法（ML-KEM 备份），体现"数学多样性"策略（格问题+纠错码两个独立数学基础）[NIST 公告](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption "2025-03-11")
- NTT CIS Lab Crypto 2025 最佳论文：标准模型下一次性签名
- 下一步数学前沿：Module-LWE 量子攻击精确界、同源密码学重建、量子密码原语可证明安全性
- 核心团队：NTT CIS Lab、Weizmann Brakerski、ETH Zurich Renner、Waterloo Mosca

**5. 量子优势数学边界——精确条件逐步明晰**
- 2026 年 2 月 PRL 发表可证明+可验证的样本复杂度量子优势 [Benedetti et al.](https://link.aps.org/doi/10.1103/q55v-wm7y "PRL 2026")。CCC 2025 发表改进的量子-经典查询复杂性分离 [CCC 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339-ccc2025/LIPIcs.CCC.2025.5/LIPIcs.CCC.2025.5.pdf "Improved Separation")
- 真正可证明的超多项式优势仅在有限场景严格成立：Shor 算法、特定量子模拟、采样问题、量子学习任务。组合优化和通用 ML 的量子优势证据仍然薄弱
- 核心团队：MIT Natarajan、CWI/QuSoft Buhrman/de Wolf、CQT Jain、Caltech Mahadev

**6. 量子学习理论——快速发展**
- 经典影子（Huang-Kueng-Preskill 2020）鲁棒化：2025 年 Nature Communications 发表贝叶斯推断鲁棒浅层影子 [Nature Comms](https://www.nature.com/articles/s41467-025-57349-w "2025")。哈密顿量学习新方法持续涌现
- Huang 等 2022 Science 论文（引用 818 次）证明量子实验数据在三类学习任务中提供可证明指数优势 [Huang et al.](https://doi.org/10.1126/science.abn7293 "Science 376, 2022")
- 核心团队：Google QAI Huang/Kueng/Preskill/Babbush、Caltech IQIM、FU Berlin Eisert

**7. 哈密顿量模拟最优性——基础理论突破持续**
- 2025 年 9 月 RIKEN Mizuta-Kuwahara 在 PRL 135 证明低能态 Trotterization 最优误差界，误差至多与初始态能量线性、与系统尺寸多对数关系 [PRL 135, 130602](https://link.aps.org/doi/10.1103/q87n-5xhz "2025-09-23")。2025 年 PRX Quantum 发表 LCU 补偿 Trotter 误差的混合方法
- 核心团队：RIKEN Kuwahara/Mizuta、Google Babbush 组、UC Berkeley Lin Lin

#### 权威机构时间线预测
- McKinsey 2025：量子计算市场 2035 年 280-720 亿美元，量子公司收入 2025 年突破 10 亿美元 [McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-year-of-quantum-from-concept-to-reality-in-2025 "QT Monitor 2025")
- BCG 2024：三阶段划分——NISQ（至 2030）、广泛量子优势（2030-2040）、完全容错（2040 后），总经济价值 4,500-8,500 亿美元 [BCG](https://www.bcg.com/publications/2024/long-term-forecast-for-quantum-computing-still-looks-bright "2024")
- IBM：2026 年底前验证量子优势，2029 年前交付首台大规模容错量子计算机 [IBM](https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance "2025-11-12")
- Microsoft：六里程碑路线图至量子超级计算机（100 万可靠 rQOPS），声称 3 年内解决"不可能的计算"[Microsoft 路线图](https://quantum.microsoft.com/en-us/vision/quantum-roadmap "Six milestones")
- DARPA QBI：2033 年验证量子计算"效用规模运行"
- Riverlane：全球仅约 600-700 名 QEC 专业人员，2030 年需 5,000-16,000 名，培训周期 10 年，人才缺口将成关键瓶颈 [Riverlane](https://www.riverlane.com/press-release/riverlane-report-reveals-scale-of-the-quantum-error-correction-challenge "2025")

#### 2026-2036 年五大里程碑预测
1. **qLDPC 码容错实现**（2026-2030）：首个基于 qLDPC 码的实用容错逻辑量子比特系统（逻辑错误率<10⁻⁶）。核心团队：IBM Bravyi/INRIA Leverrier-Zémor/Google Haah
2. **QSP/QSVT 标准范式化**（2026-2030）：多变量框架在量子化学和组合优化中展示端到端量子算法。核心团队：MIT Chuang/UC Berkeley Lin Lin/RIKEN Fujii
3. **PQC 安全性精细分析**（2026-2032）：Module-LWE 量子攻击精确界重标定，新量子密码原语进入标准化。核心团队：NTT CIS Lab/Weizmann Brakerski/ETH Renner
4. **低能态模拟最优算法**（2026-2032）：统一模拟框架将量子化学核心问题成本降低数个数量级。核心团队：RIKEN Kuwahara/Google Babbush/UC Berkeley Lin Lin
5. **量子学习信息论最优界**（2026-2030）：经典影子在近期量子器件上展示样本复杂度优势的实验验证。核心团队：Google QAI/Caltech IQIM/FU Berlin Eisert

#### 综合团队势能评估（★1-5）
| 团队 | 核心方向 | 势能 | 关键依据 |
|---|---|---|---|
| IBM Quantum Bravyi 组 | qLDPC 码实用化 | ★★★★★ | BB 码 Nature 2024 + Relay-BP + Loon 提前达标 |
| INRIA Leverrier-Zémor | qLDPC 码代数理论 | ★★★★☆ | Quantum Tanner Codes 理论突破 |
| Microsoft Station Q | 拓扑量子计算 | ★★★★☆ | Fields 奖得主领衔，但实验争议未消 |
| MIT Chuang 组 | QSP/QSVT 框架 | ★★★★★ | QSP 创始团队，多变量模块化持续引领 |
| Google QAI | 量子学习+纠错实验 | ★★★★★ | 经典影子发明者 + Willow 实验，理论-实验闭环最强 |
| NTT CIS Lab | 后量子密码学数学 | ★★★★☆ | Crypto 2025 最佳论文，工业界 PQC 理论全球之首 |
| RIKEN RQC | 模拟最优性+资源理论 | ★★★★☆ | PRL 2025 Trotter 最优性 + Nature Physics 2023 资源理论里程碑 |
| Caltech IQIM | 拓扑理论+量子学习 | ★★★★★ | Kitaev/Preskill/Brandão/Mahadev 综合优势 + AWS 融合 |
| 悉尼大学 | 拓扑纠错码 | ★★★☆☆ | Layer Codes 解决十年问题，但团队规模小 |
| Weizmann | 复杂性+PQC+拓扑物理 | ★★★★☆ | Vidick 转入 + Brakerski 格密码学前列 |

### 可用图片
- 无直接相关图片素材

### 仍需补充
- Google Quantum AI 后 Willow 路线图（更高 distance 码或 qLDPC 实验）
- IBM Starling/Flamingo 处理器的 qLDPC 码实现参数
- Microsoft 拓扑量子比特第三方独立验证进展（截至 2026-03）
- 中国团队（清华 YMSC 刘子文/USTC）在 qLDPC 码方向的具体布局
- QAOA/VQE 可训练性理论最新进展（荒原高原后续发展）


## Chapter 7：总结、风险因素与展望
### 研究目标
- 提炼报告核心三到五条结论
- 识别影响预判实现的关键风险与不确定性因素
- 为决策读者提供简明的行动参考框架和后续追踪方向建议

### 关键发现

#### 五大核心结论
1. **qLDPC 码处于"临界跨越"阶段**：2021-2022 理论突破→IBM BB 码 Nature 2024→Loon 提前一年达标→QEC 码论文"爆炸"（120 篇 vs 36 篇），其成败将决定容错量子计算时间表 [IBM](https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance "2025-11-12")；[Riverlane](https://www.riverlane.com/press-release/riverlane-report-reveals-scale-of-the-quantum-error-correction-challenge "2025-11-19")
2. **数学科学界"基本缺席"尚未改变**：SIAM QIC 核心诊断与量子论文指数增长、G2S3 暑期学校、图灵奖形成鲜明对比——数学-量子交叉正从边缘走向核心，但人才供给和资金结构远未匹配需求 [SIAM QIC](https://www.siam.org/media/orydkrzd/quantum-convening-report.pdf "2024")
3. **中美学术合作结构性收缩重塑研究网络**：国际合著比降 7.2pp、中美降 6.4pp、"反转 J 曲线"为双边独有。但 QIST 约半数涉及国际合作，完全脱钩几乎不可能。中国向 EU 知识流上升，美国强化 11 国双边合作 [Kitajima & Okamura](https://www.nature.com/articles/s41599-025-04550-3 "Nature HSSC, 2025-03-03")
4. **量子价值主张面临经典 AI/HPC 和去量子化双重挤压**：Google 自身承认"识别具体优势实例"是"资源不足的核心挑战" [Babbush et al.](https://arxiv.org/abs/2511.09124 "arXiv, 2025-11")。真正可证明的超多项式优势仅限于 Shor 算法、特定量子模拟、采样问题、量子学习任务。量子私人投资仅占 AI 的 2.4% [CSIS](https://www.csis.org/analysis/government-demand-creator-quantum-industry "2026-03")
5. **QEC 人才缺口是最紧迫瓶颈**：全球 600-700 人 vs 2030 年需 5,000-16,000 人，培训周期 10 年，被技术路线图普遍低估 [Riverlane](https://www.riverlane.com/press-release/riverlane-report-reveals-scale-of-the-quantum-error-correction-challenge "2025-11-19")

#### 六大风险因素
1. **技术路线风险**：qLDPC vs 表面码 vs 拓扑码，投注错误路线意味稀缺数学人才和培养周期浪费。拓扑路线争议尤甚——Science 质疑、1/f 噪声挑战 [Science](https://www.science.org/content/article/debate-erupts-around-microsoft-s-blockbuster-quantum-computing-claims "2025")
2. **地缘政治风险**：中美合作收缩（美-EU 量子合作强度 2018-2022 降 15%）。出口管制"双刃剑"：RUSI 分析显示管制正"加速中国国内量子供应链" [RUSI](https://www.rusi.org/explore-our-research/publications/commentary/export-controls-accelerate-chinas-quantum-supply-chain "2025-06")；34 量子比特阈值合理性被 OECD 公开质疑
3. **人才风险**：QEC 人才定量缺口 + 数学家缺席 + AI 虹吸效应（AI 投资 1,090 亿 vs 量子 26 亿美元）
4. **资金风险**：FY2026 NSF 获参议院保护至 87.5 亿美元（仅减 3.85%），但后续年度不确定 [参议院商委](https://www.commerce.senate.gov/2026/1/ves-existential-threat-from-trump-budget-as-senate-rejects-gutting-nasa-nsf-nist "2026-01-15")。中国实际投资 vs 公开承诺差距大（可能仅为三分之一）
5. **替代技术风险**：McKinsey 2035 年预测区间 280-720 亿美元（2.6 倍区间本身即不确定性度量）。BCG 已下调 NISQ 阶段近期价值预期
6. **去量子化风险**：Tang 工作持续收窄优势范围，但最具韧性领域（量子模拟、密码分析）恰是数学密集方向 [Quanta Magazine](https://www.quantamagazine.org/what-is-the-true-promise-of-quantum-computing-20250403/ "2025-04-03")

#### 行动建议
- **科研管理者**：优先投资 qLDPC 码方向数学人才培养；响应 SIAM QIC 建议在数学系建立量子方向明确资助信号；建立"技术路线对冲"的研究组合策略（同时支持代数编码/拓扑学/辫子群方向）
- **政策制定者**：维护 NSF DMS 量子交叉资金稳定性（NQI 再授权 18 亿美元应明确数学交叉优先领域）；审慎评估量子出口管制实际效果；在国家量子战略中增设"数学基础研究"专门条目
- **投资决策者**：关注 qLDPC 码生态链投资机会（实时解码硬件、编译器、协同处理器）；对量子应用落地时间保持审慎预期（DARPA QBI 2033 年才验证效用规模）；将去量子化进展纳入投资假设压力测试

#### 后续追踪方向
1. IBM 2026 年底量子优势验证——qLDPC 码路线首个决定性节点
2. Microsoft 拓扑量子比特第三方独立验证
3. NSF FY2027 预算走向——数学-量子交叉制度建设可持续性指标
4. 中美量子合作"替代通道"演变（中国→EU 知识外溢、美国 11 国双边项目进展）
5. QEC 人才供给年度监测
6. NIST PQC 标准更新周期（HQC 2027 年标准、Module-LWE 参数重标定）

### 可用图片
- 无直接相关图片素材

### 仍需补充
- Microsoft 拓扑量子比特第三方独立验证进展（截至 2026-03 无公开结果）
- 中国在 qLDPC 码方向的具体布局（清华 YMSC 刘子文/USTC）
- AI 对量子人才虹吸效应的专项定量数据（如量子 PhD 转入 AI 行业比例）
- 中国 NSFC 纯数学方向量子资助的精确细分数据


# Section 2：给 Write 阶段的执行建议

## 一、报告整体风格与术语统一
- 全篇采用正式中文研究报告风格，目标读者为具备理工科背景的科研管理者、政策制定者和投资决策者
- 术语统一：首次出现的英文术语须给出中文译名并在括号内保留英文原文，之后统一使用中文简称；已广泛接受的缩写（QEC、NISQ、FTQC）在首次定义后可直接使用
- 机构名称统一：首次出现时给出全称+常用缩写，后续统一用缩写；中国机构以官方中文全称为准，海外机构以英文缩写为主
- 数学分支和量子计算子方向的分类体系应在 Chapter 1 明确建立，后续章节严格沿用

## 二、写稿前需再次核验的关键判断
- 各国/地区量子计算专项投资的最新金额数据（尤其是中美欧 2025-2026 年度拨款），需交叉验证政府官方来源和权威研究机构报告的口径差异
- 特定团队"里程碑式成果"声明中的数学贡献部分（而非仅硬件工程贡献），确保归入本报告的合理性
- Chapter 6 中"突破潜力"评估所依据的事实基础须在前述章节中有数据支撑，不得出现悬空判断
- 中美学术合作受地缘政治影响的最新态势，需以官方政策文件或一手报道为依据

## 三、章节间需统一口径的地方
- Chapter 2-3 按地域分组，Chapter 4 的论文产出与合作网络须覆盖全部团队不遗漏；Chapter 6 势能评估须与团队画像一一对应
- 时间口径：历史回顾可追溯至 1990 年代，核心对比分析以 2025-04 至 2026-03 为锚定区间，论文计量数据标注统计时间窗口
- "数学贡献"认定标准在 Chapter 1 给出，后续严格沿用
- Chapter 4 定量指标体系在该章章首统一定义，Chapter 6 须明确引用 Chapter 4 指标结果
- Thomas Vidick 的归章口径：Chapter 2 中作为 Caltech IQIM 历史成员提及，Chapter 3 中说明 2024 年全职转入 Weizmann。两章须注明人才流动情况，避免矛盾
- 以色列团队归章口径：Hebrew University QISC 在 Chapter 2（北美与欧洲+以色列），Weizmann Institute 在 Chapter 3（亚太及其他）。写作时须说明以色列团队按机构分布在两章的逻辑（Hebrew U 在 Chapter 2 因 Aharonov 与北美学术网络的深度联系，Weizmann 在 Chapter 3 因 Vidick 转入属于新兴变化）

## 四、数据和引用的处理建议
- 核心数据须标注来源和统计口径，优先使用 T1/T2 来源
- 定性描述（如"全球领先""快速追赶"）须有定量数据或同行评价支撑
- 争议性判断须明确事实基础和推理逻辑，允许"我们判断""我们认为"等审慎表述，但须附条件假设
- 国际比较数据统一使用美元计价并标注汇率基准
- 论文计量数据以 Scopus 或 Web of Science 为主要数据库，如使用 Google Scholar 等补充来源须标注
