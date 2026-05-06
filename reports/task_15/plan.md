# 量子网络全球研究课题组横向比较与潜力评估——研究计划

> 时间口径：以 2026 年 4 月为锚点。"近期进展"指 2025-04 至 2026-04（12 个月）；"展望"指 2026-04 至 2026-10（6 个月）。

---

# Section 1：章节研究计划

## Chapter 1：量子网络领域概述与技术路线图

### 研究目标
- 为读者建立量子网络/量子互联网的概念框架和技术全景
- 回答"量子网络是什么、为何重要、目前处于哪个发展阶段"
- 厘清量子网络与 QKD 网络、分布式量子计算、量子传感网络的关系与区分
- 梳理核心技术栈（物理平台、量子存储器、量子中继器、纠缠交换与纯化、量子纠错码）
- 定义关键性能指标（纠缠分发速率、保真度、量子存储寿命、网络节点数、通信距离）
- 概述 2025-04 至 2026-04 期间的里程碑事件

### 关键发现

**定义与边界**
- 量子网络利用量子力学原理（叠加、纠缠、不可克隆定理）在节点之间传输量子态，核心目标是作为经典互联网的补充层提供新功能。[Wehner, Elkouss & Hanson, Science 362, eaam9288 (2018)](https://qutech.nl/wp-content/uploads/2018/10/Quantum-internet-A-vision.pdf "Quantum internet: A vision for the road ahead")
- 三大网络类型：（1）QKD 网络（最成熟，已商用，仅限密钥分发，需可信中继）；（2）量子互联网/纠缠型网络（通过纠缠分发连接量子设备，支持分布式量子计算等，处于早期实验阶段）；（3）量子传感网络（纠缠连接传感器突破经典精度极限）。[The Quantum Insider](https://thequantuminsider.com/2026/03/09/understanding-quantum-networking-and-its-industrial-potential/ "Understanding Quantum Networking, 2026年3月")
- 纠缠型网络与 QKD 网络的关键区别：前者是多用途网络，使用量子中继器而非可信中继节点，即使中继器被攻破也不泄露信息。[Aliro Quantum](https://www.aliroquantum.com/blog/quantum-networking-101-entanglement-based-quantum-networks "Entanglement-Based Quantum Networks")

**Wehner 六阶段路线图**
- Wehner et al. (2018) 提出六个功能性阶段：可信中继网络→准备-测量网络→纠缠分发网络→量子存储网络→少量比特容错网络→量子计算网络，每阶段提供前一阶段不具备的本质性新功能。截至 2026 年 4 月，该框架未有正式更新版本，仍是社区最广泛引用的路线图。[Wehner, Elkouss & Hanson, Science 362, eaam9288 (2018)](https://qutech.nl/wp-content/uploads/2018/10/Quantum-internet-A-vision.pdf "原始论文 Table 1 和正文")
- 截至 2026 年初，全球实验整体处于第一阶段（可信中继网络）向第二/第三阶段过渡的关键期：QuTech 于 2024 年 10 月实现 Delft–Den Haag 25 km 部署光纤量子处理器间纠缠（第三阶段核心演示），中科大于 2024 年实现城域多节点量子存储纠缠网络（触及第四阶段要素）。[QuTech 2024](https://qutech.nl/2024/10/30/a-rudimentary-quantum-network-link-between-dutch-cities/ "Science Advances 2024, DOI: 10.1126/sciadv.adp6442")；[中国科学院](https://english.cas.cn/special-reports/Highlights_2024/202512/t20251219_1138401.shtml "Nature 2024")

**物理平台优劣势**
- **NV 色心**：室温长相干时间（>1s），已演示三节点网络和 25 km 城市间纠缠，但光子收集效率极低。2026 年 1 月 QuTech 将腔增强 NV 中心有用光子收集概率从约 0.05% 提升至约 0.5%（10 倍）。[QuTech](https://qutech.nl/2026/01/15/more-photons-faster-links-a-laser-focused-nv-centre/ "Nature Communications 2026")
- **离子阱**：最长相干时间（清华 2025 年演示 Yb+ 多离子存储 >2 小时），高保真门操作，但需频率转换。USTC 潘建伟团队 2026 年 2 月在 Nature 展示 10 km 光纤离子-离子纠缠，纠缠存活时间首超建立时间，并实现设备无关 QKD 验证（10 km 正密钥率，101 km 渐近极限正密钥率）。[Liu et al., Nature (2026)](https://www.nature.com/articles/s41586-026-10177-4 "DOI: 10.1038/s41586-026-10177-4")；[Quantum Zeitgeist](https://quantumzeitgeist.com/cryogenic-dual-ion-trap-extends-quantum-memory-coherence-beyond-two-hours/ "Tsinghua/HYQ 2025")
- **中性原子（Yb-171）**：内在电信波长兼容性、可并行化阵列架构。2025 年 10 月 Illinois 大学 Covey 组在 Nature Physics 首次实现电信波长并行原子-光子纠缠。[Li et al., Nature Physics (2025)](https://phys.org/news/2025-10-parallel-atom-photon-entanglement-paves.html "DOI: 10.1038/s41567-025-03022-4")
- **量子点**：确定性按需生成纠缠光子对。2025 年 11-12 月欧洲团队首次实现不同量子点间量子隐形传态（270 m，保真度 82±1%）；2026 年 1 月 Stuttgart/Würzburg 展示电信 C 波段单光子源双光子干涉可见度约 92%。[Phys.org](https://phys.org/news/2025-12-photon-teleportation-distant-quantum-dots.html "Nature Communications 2025")；[Uni Stuttgart](https://www.uni-stuttgart.de/en/university/news/all/Record-breaking-photons-at-telecom-wavelengths--on-demand/ "Nature Communications 2026")
- **超导量子比特**：极快门速度，成熟工艺，但工作在微波频段需微波-光学转换。Princeton 2025 年 11 月实现 transmon 1 ms+ 相干时间（此前记录 3 倍）。[Princeton](https://www.princeton.edu/news/2025/11/05/princeton-puts-quantum-computing-fast-track-new-qubit "Nature 2025")
- **稀土铒掺杂晶体**：直接在电信 C 波段发光，UChicago PME 2025 年 11 月将铒原子自旋相干时间从 0.1 ms 提升至 >10 ms（最高 24 ms），理论网络距离 2,000-4,000 km。[UChicago PME](https://pme.uchicago.edu/news/breakthrough-could-connect-quantum-computers-200x-distance "Nature Communications 2025")

**关键性能记录**
- 通信距离：卫星 QKD 12,900 km（中国-南非，济南一号微卫星，2025 年 3 月 Nature）[ScienceDaily](https://www.sciencedaily.com/releases/2025/03/250319142833.htm "DOI: 10.1038/s41586-025-08739-z")；光纤异构网络 410 km（UK Bristol-Cambridge，2025 年 4 月 OFC）[Phys.org](https://phys.org/news/2025-04-uk-distance-ultra-communication-quantum.html "UK quantum network")；设备无关 QKD 11 km（USTC，2026 年初）[The Quantum Insider](https://thequantuminsider.com/2026/02/06/chinese-researchers-clear-hurdles-for-long-distance-quantum-networks/ "Nature & Science论文")
- 量子存储相干时间：离子阱 >2 小时（清华 Yb+，2025 年）；铒原子 >10 ms/24 ms（UChicago MBE，2025 年 11 月）；NV 色心 >1 秒（传统体系）
- 纠缠分发距离：量子处理器间 25 km 部署光纤（QuTech NV 色心，2024 年 10 月 Science Advances）；城域多节点存储纠缠 12.5 km（中科大，2024 年 5 月 Nature）；离子-离子 10 km 光纤（USTC，2026 年 2 月 Nature）

**2025.04–2026.04 里程碑时间线**
- 2025-04：UK Bristol-Cambridge 410 km 光纤异构量子网络演示
- 2025-09：IonQ 实现捕获钡离子光子→电信波长频率转换，AFRL 交付首台集成光子接口离子阱量子计算机 [IonQ](https://investors.ionq.com/news/news-details/2025/IonQ-Achieves-Significant-Quantum-Internet-Milestone-Demonstrates-Quantum-Frequency-Conversion-to-Telecom-Wavelengths/default.aspx "IonQ 2025年9月")
- 2025-10：Illinois Covey 组 Yb-171 原子阵列电信波长并行原子-光子纠缠（Nature Physics）
- 2025-11：Princeton transmon 1 ms+ 相干时间（Nature）；UChicago 铒原子 >10 ms（Nature Comms）；欧洲团队首次不同量子点间隐形传态（Nature Comms）
- 2026-01：QuTech NV 色心光子收集效率 10 倍提升（Nature Comms）；Stuttgart/Würzburg 电信 C 波段量子点单光子源 92% 可见度（Nature Comms）
- 2026-02：USTC 10 km 离子-离子纠缠+DI-QKD（Nature）；USTC 11 km 设备无关 QKD（Nature & Science）；Oxford 启动"分布式安全量子计算"项目 [Oxford](https://www.ox.ac.uk/news/2026-02-03-new-project-aims-build-foundations-quantum-internet "Oxford 2026")
- 2026-03：Google Quantum AI 宣布增加中性原子模态，双轨量子路线图 [The Quantum Insider](https://thequantuminsider.com/2026/03/24/google-paves-a-two-lane-quantum-roadmap-by-adding-neutral-atom-systems/ "Google 2026年3月")

### 可用图片
- 无本地可用图片。建议写作时自制：Wehner 六阶段路线图示意图、各物理平台性能指标对比表、2025.04–2026.04 里程碑时间线图。

### 仍需补充
- 纠缠分发速率（pairs/sec）的系统性横向比较数据，需从各实验论文 supplementary 中逐一提取
- 超导量子比特用于量子网络的微波-光学转换效率最新记录（Yale、ETH、Delft 等），缺乏 2025-2026 年间的突破性 T1/T2 来源
- 中国京沪量子骨干网 2025 年后的官方运行状态数据，缺乏 T1 来源
- 各平台最新实验的纠缠保真度统一横向比较，缺乏第三方综述

---

## Chapter 2：全球量子网络研究生态与资助格局

### 研究目标
- 系统梳理全球量子网络研究的政策环境、资金投入和组织架构
- 回答"哪些国家/地区在投入、投了多少、通过什么机制组织研究"
- 覆盖美国、欧盟、中国、英国、日本、韩国、新加坡、加拿大、荷兰、德国、澳大利亚等
- 比较组织模式、军方角色、产业界参与度

### 关键发现

**美国：多机构协同的联邦资助体系**
- 联邦 QIS 研发总支出从 FY2019 的 4.56 亿美元增长至 FY2022 的 10.41 亿美元高点，此后维持约 10 亿美元水平（FY2025 请求 9.98 亿美元），"量子网络"（QNET）是五大 NQI 项目领域之一。[NQI FY2025 年度报告](https://www.quantum.gov/wp-content/uploads/2024/12/NQI-Annual-Report-FY2025.pdf "National Quantum Initiative Supplement to the President's FY 2025 Budget")
- 2025 年 11 月 DOE 宣布 6.25 亿美元续期五个 NQISRCs（最长 5 年），其中 SQMS（费米实验室）和 Q-NEXT（阿贡实验室）与量子网络技术关系最直接。[美国能源部官方公告](https://www.energy.gov/articles/energy-department-announces-625-million-advance-next-phase-national-quantum-information "DOE $625M 续期公告, 2025年11月")
- NSF 通过 QLCI（5 所研究所）、NQVL、核心项目（约 1,600 个 QIS 项目）、ExpandQISE（9,900 万美元/56 个项目）、NQN（2,000 万美元纳米加工设施）等多机制支持量子网络研究。[NQI FY2025 年度报告](https://www.quantum.gov/wp-content/uploads/2024/12/NQI-Annual-Report-FY2025.pdf "NSF QIS R&D Programs 章节")
- DOE 专项资助包括 4,500 万美元量子计算加速研究、7,000 万美元 QIS 赋能高能物理发现（5 年）、6,500 万美元量子计算研究（10 项目/38 子奖励）。[NQI FY2025 年度报告](https://www.quantum.gov/wp-content/uploads/2024/12/NQI-Annual-Report-FY2025.pdf "DOE QIS R&D 章节")
- DOD 通过 DARPA QBI（2024 年启动）、AFRL、ARO 等多机构系统性投入，DARPA 2025 年与新墨西哥州签署最多 6,000 万美元匹配框架协议。[NQI FY2025 年度报告](https://www.quantum.gov/wp-content/uploads/2024/12/NQI-Annual-Report-FY2025.pdf "DOD QIS R&D 章节")；[DARPA](https://www.darpa.mil/news/2025/darpa-new-mexico-establish-framework-advance-quantum-computing "DARPA 2025")

**欧盟：量子旗舰与 QIA**
- 量子旗舰计划（2018 年启动）总预算 10 亿欧元/10 年。QIA 第一阶段（2022-2026）获 Horizon Europe 资助 2,400 万欧元（Grant 101102140），此前在 H2020 下获约 1,000 万欧元。[CORDIS](https://cordis.europa.eu/project/id/101102140/reporting "QIA Phase 1 Grant €24M")；[QIA 项目页](https://quantuminternetalliance.org/projects/ "Quantum Flagship €1B/10yr")
- 2025 年 7 月欧盟委员会发布《量子欧洲战略》（COM(2025) 363），EuroQCI 倡议（27 成员国）建设全欧量子安全通信基础设施。[欧盟量子欧洲战略](https://qt.eu/media/pdf/Quantum_Europe_Strategy_July_2025.pdf "Quantum Europe Strategy, July 2025")

**中国：国家战略驱动**
- 据 CSIS 2026 年 1 月报告（T2），中国政府累计量子投资估计约 150 亿美元（未经官方确认）。中国已建成全球最大量子通信网络 CN-QCN（145 光纤节点、6 地面站、20 城域网、覆盖 17 省 80 城、光纤超 12,000 公里）。[CSIS 报告](https://www.csis.org/analysis/understanding-chinas-quest-quantum-advancement "CSIS, 2026年1月")
- 2025 年 3 月宣布国家创业引导基金近 1 万亿元人民币（1,380 亿美元），量子技术是重点领域。中国电信量子集团（CTQG）已成为国盾量子控股股东，QKD 服务覆盖 550 万+用户。[CSIS 报告](https://www.csis.org/analysis/understanding-chinas-quest-quantum-advancement "同上")

**英国：新一轮量子投资**
- 2025 年 4 月启动 IQN Hub（Heriot-Watt 牵头，EPSRC 2,200 万英镑+行业配套合计 4,200 万+英镑，联合 13 所大学、2 国家实验室、40+产业伙伴）。[Heriot-Watt](https://www.hw.ac.uk/news/2025/new-uk-quantum-hub-launches-to-pioneer-secure-networks-and-advance-the-quantum-internet "IQN Hub 2025年4月")
- 2026 年 3 月宣布 20 亿英镑量子投资计划，其中 1.25 亿英镑专门用于量子网络，累计公共量子投资超 10 亿英镑、新计划总量达约 35 亿英镑。[The Quantum Insider](https://thequantuminsider.com/2026/03/17/uk-pledges-2-billion-for-quantum-innovation/ "UK £2B 量子投资, 2026年3月")

**日本**
- 2025 年 11 月补充预算拨付约 1,300 亿日元（约 8.55 亿美元）用于量子技术，含 1,004 亿日元用于 AIST 研发基地。此前有 Moonshot 计划（150-200 亿日元）、Q-LEAP 计划，以及 1.05 万亿日元芯片与量子计算专项。[The Quantum Insider](https://thequantuminsider.com/2025/11/28/japan-channels-almost-900-million-u-s-into-quantum-push/ "Japan $900M quantum push, 2025年11月")

**其他国家/地区**
- 韩国 3 万亿韩元/2035 计划；新加坡近 3 亿新元国家量子战略+1 亿新元金融量子专项；加拿大 3.6 亿加元国家量子战略+累计 10 亿+加元；荷兰 6.15 亿欧元 Quantum Delta NL+1.35 亿欧元 QuTech；德国 30 亿欧元行动计划；澳大利亚 8.93 亿澳元（至 2024 年 1 月）。[Qureca](https://www.qureca.com/quantum-initiatives-worldwide/ "Quantum Initiatives Worldwide 2025")

**军方角色**
- 美国 DOD 30+年量子投入历史，通过 DARPA、AFRL、ARO 等多渠道；中国国防-安全需求驱动量子通信投资；欧洲 EuroQCI 具战略安全含义，英国 GCHQ、NCSC、Dstl 参与 IQN Hub。[NQI FY2025 年度报告](https://www.quantum.gov/wp-content/uploads/2024/12/NQI-Annual-Report-FY2025.pdf "DOD 章节")

**产业界参与**
- 2025 年 11 月 IBM 与 Cisco 宣布合作构建分布式容错量子计算机网络（2030 年代初概念验证），Cisco 开发"量子数据中心"架构，为目前产业界最大规模量子网络合作。[IBM 新闻室](https://newsroom.ibm.com/2025-11-20-ibm-and-cisco-announce-plans-to-build-a-network-of-large-scale,-fault-tolerant-quantum-computers "IBM-Cisco 2025年11月")
- Cisco 投资 Qunnect（室温量子网络），Nu Quantum 完成 6,000 万美元融资（纠缠织物技术），CTQG 运营中国最大量子通信网络，IonQ 2026 年 3 月在剑桥设立创新中心。[CRN](https://www.crn.com/news/networking/2025/cisco-reveals-history-making-investment-in-quantum-networking-upstart-qunnect "Cisco-Qunnect 2025")

**组织模式**
- 四种模式：国家实验室主导（美国 DOE 体系/5 个 NQISRCs）、大学联盟（欧洲 QIA/英国 IQN Hub）、企业主导/公私合作（IBM-Cisco、CTQG）、国家战略垂直整合（中国中科院→国盾量子全链条）。

### 可用图片
- 无本地可用图片。建议写作时制作：各国/地区量子网络资助规模对比柱状图、组织模式对比图。

### 仍需补充
- 美国 QNET 专项预算从 NQI 总预算中的具体分拆金额（图表数据需人工估读）
- 中国量子网络方向的具体政府资助金额（科技部专项、基金委重大项目、中科院先导专项），CSIS 的"约 150 亿美元"为总体估计且未经官方确认
- DARPA 是否有独立的量子网络/量子通信专项及其具体预算
- QIA Phase 2 的具体资助金额和时间表
- 欧洲防务局（EDA）在量子网络方面的专项投入数据
- 日本 Moonshot 计划中量子网络子方向专项金额；NTT-东大 IOWN 量子网络合作投入金额
- IBM-Cisco 合作具体投资金额；各电信运营商量子网络资本支出细分数据

---

## Chapter 3：全球主要量子网络课题组全景扫描

### 研究目标
- 建立一份尽可能完整的全球量子网络研究课题组清单（目标 20-30 个）
- 对每个课题组进行标准化画像：所属机构、核心领导人、学术背景、主攻技术路线、核心研究方向、代表性成果、主要资助来源
- 按地理区域分组呈现（北美、欧洲、亚太、其他）
- 明确课题组筛选标准与入选门槛

### 关键发现

共收录 **28 个课题组**，筛选标准：近 3 年（2023-2026）在量子网络/量子互联网方向有实质性实验或理论贡献，在高影响力期刊有相关发表。

**北美（10 组）**

1. **Harvard — Lukin Group**：PI Mikhail Lukin，NAS 院士，Google Scholar ~163,654 次引用，QuEra 联合创始人。技术路线 SiV 色心+纳米光腔。2024 年 Nature 发表 35 km 波士顿部署光纤 SiV 节点电信波段纠缠；2025 年 Science 发表分布式盲量子计算；2026 年 Nature 发表纠缠辅助非局域光学干涉。资助：NSF CQN ERC、DOE、DARPA。[Lukin Group](https://lukin.physics.harvard.edu/quantum-networking-siv "Quantum Networks with SiV Centers")

2. **MIT — Englund QPAI Group**：PI Dirk Englund，~56,197 次引用，NSF CQN Co-Deputy Director。技术路线金刚石色心集成光子学。资助：NSF CQN ERC (~$26M)、DARPA、DOE。[MIT EECS](https://www.eecs.mit.edu/people/dirk-r-englund/ "Dirk Englund")

3. **UIUC — Covey Group**：PI Jacob Covey，Assistant Professor，2024 NSF CAREER。技术路线 Yb-171 中性原子阵列。2025 年 Nature Physics 首次实现电信波长并行原子-光子纠缠。资助：NSF CAREER、DOE（Q-NEXT/SQMS）、DARPA。[IQUIST](https://iquist.illinois.edu/people/jacob-covey "Jacob Covey")

4. **UChicago — Zhong Lab**：PI Tian Zhong，2025 Sturge Prize。技术路线稀土离子掺杂晶体纳米光子学。2025 年 Nature Comms 展示量子连接距离扩展至 2,000 km（200 倍提升）。资助：NSF CAREER、DOE Q-NEXT。[UChicago PME](https://pme.uchicago.edu/faculty/tian-zhong "Tian Zhong")

5. **UChicago — Bernien Lab**：PI Hannes Bernien（博士 Delft/Hanson 组，博后 Harvard/Lukin 组）。技术路线中性 Rb 原子纳米光子腔。2023 年 npj Quantum Information 合著中性原子量子网络综述。资助：NSF CAREER、DOE Q-NEXT、AFOSR。[Bernien Lab](https://bernienlab.com/research/21-quantum-networks "Quantum Networks")

6. **UChicago-ANL — Awschalom / Q-NEXT**：PI David Awschalom，NAS/NAE/AAAS 三院院士，Q-NEXT 主任。2021 年 PRX Quantum 发表 QuICs 量子互联路线图。资助：DOE Q-NEXT（$125M/5 年续期）、NSF、DOD。[PRX Quantum](https://link.aps.org/doi/10.1103/PRXQuantum.2.017002 "QuICs 路线图, 2021")

7. **Stony Brook/BNL — Figueroa Group / SCY-QNet**：PI Eden Figueroa，量子研究所所长（$300M 投资）。领导 SCY-QNet——连接 Stony Brook/Columbia/Yale/BNL 的 10 节点广域量子网络原型。资助：NSF NQVL、DOE C2QA。[SCY-QNet](https://www.stonybrook.edu/commcms/physics/figueroa-research-group/scy-qnet/ "SCY-QNet")

8. **Caltech — Faraon Group**：PI Andrei Faraon。技术路线稀土离子纳米光子学。2018 年 PRL 开创单稀土离子光寻址。资助：NSF、DOE、AFOSR、IQIM。[Caltech](http://photonics.caltech.edu/rareearth.html "Faraon Group")

9. **Princeton — Thompson Group**：PI Jeff Thompson，NSF CQN Co-PI。技术路线 Yb-171 中性原子。2024 年 PRX Quantum 发表模块化高保真互联方案。资助：NSF CQN、DARPA、DOE。[PRX Quantum 2024](https://link.aps.org/doi/10.1103/PRXQuantum.5.020363 "Modular Interconnects")

10. **Duke — Kim Group / IonQ**：PI Jungsang Kim，~15,808 次引用，IonQ 联合创始人。技术路线离子阱。IonQ 2026 年在剑桥设立创新中心。资助：NSF、DOE、DARPA、IonQ。[Duke](https://quantum.duke.edu/profile/jungsang-kim/ "Jungsang Kim")

**欧洲（12 组）**

11. **TU Delft/QuTech — Hanson Lab**：PI Ronald Hanson，Spinoza Prize (2019)、Bell Prize (2017)，KNAW 院士。技术路线 NV 色心。2024 年 Science Advances 实现 25 km 部署光纤量子处理器纠缠（最远记录）；2021 年 Nature 首个三节点纠缠网络。2024 年联合创立 Delft Networks 公司。资助：EU QIA 协调人、Quantum Delta NL（€6.15 亿）、ERC。[QuTech](https://qutech.nl/person/ronald-hanson/ "Ronald Hanson")

12. **TU Delft/QuTech — Wehner Group（理论）**：PI Stephanie Wehner，2025 Körber European Science Prize。2018 年 Science 发表量子互联网六阶段路线图（领域标准框架）；2024 年创建首个量子网络操作系统 QNodeOS。资助：EU QIA、ERC。[Körber Prize](https://koerber-stiftung.de/en/projects/koerber-european-science-prize/all-prizewinners/2025-stephanie-wehner/ "2025 Körber Prize")

13. **Oxford — Lucas Group**：PI David Lucas。技术路线离子阱。2025 年创单量子比特操控精度世界纪录；2026 年 2 月获 EPSRC £4.5M 联合领导 UK-Japan 量子互联网项目。资助：EPSRC、IQN Hub。[Oxford](https://www.ox.ac.uk/news/2026-02-03-new-project-aims-build-foundations-quantum-internet "UK-Japan 项目 2026")

14. **Innsbruck — Northup & Lanyon Groups**：PI Tracy Northup & Ben Lanyon（师从 Blatt/Roos）。技术路线离子阱-光腔耦合。2023 年实现 230 m 离子纠缠；曾实现 50 km 光纤离子-光子纠缠。资助：EU QIA、FWF、ERC。[Innsbruck](https://www.uibk.ac.at/en/newsroom/2023/entangled-atoms-across-the-innsbruck-quantum-network/ "230m 离子纠缠 2023")

15. **MPQ Garching — Rempe Group**：PI Gerhard Rempe，量子网络先驱。技术路线 Rb 原子光学腔。2024 年 Science 发表光学腔内光镊原子阵列量子网络寄存器；2024 年 Nature 发表光子图态融合。资助：Max Planck Society、EU QIA、BMBF。[Science 2024](https://www.science.org/doi/10.1126/science.ado6471 "Quantum-network register")

16. **LMU Munich — Weinfurter Group**：PI Harald Weinfurter。技术路线 Rb 原子+量子频率转换。2022 年 Nature 实现 33 km 电信光纤两原子纠缠。资助：DFG、BMBF、MCQST。[Nature 2022](https://www.nature.com/articles/s41586-022-04764-4 "33 km 原子纠缠")

17. **TU Munich — Reiserer Group**：PI Andreas Reiserer。技术路线铒离子掺杂硅纳米光子。铒是唯一已知在电信波长具相干跃迁的系统，与硅光子技术直接兼容。资助：TUM、MCQST、Munich Quantum Valley、ERC。[TUM](https://www.ph.nat.tum.de/en/quantum-networks/homepage/ "Quantum Networks")

18. **ICFO Barcelona — de Riedmatten Group**：PI Hugues de Riedmatten，ICREA Research Professor。技术路线稀土离子+离子阱混合。2024 年巴塞罗那城市光纤物质-光纠缠远距传输。资助：EU QIA、ICREA、ERC。[QIA 新闻](https://quantuminternetalliance.org/2024/04/02/icfo-researchers-demonstrate-long-distance-transmission-of-matter-light-entanglement-through-optical-fiber-in-barcelona/ "ICFO 2024")

19. **Sapienza Rome — Sciarrino Lab**：PI Fabio Sciarrino。技术路线光子/量子点。2025 年 Nature Comms 首次不同量子点间量子隐形传态。资助：EU EPIQUE、ERC（>€275 万）。[Nature Comms 2025](https://www.nature.com/articles/s41467-025-65911-9 "Quantum teleportation with quantum dots")

20. **Sorbonne/LKB Paris — Laurat Group**：PI Julien Laurat，2024 Jean Jerphagnon Prize，Welinq 联合创始人。技术路线冷铯原子量子存储器。2025 年 Science Advances 首次演示集成量子存储层的密码协议。资助：EU QIA、ANR、ERC。[Science Advances 2025](https://www.science.org/doi/10.1126/sciadv.adx3223 "Quantum cryptography with memory")

21. **Paderborn — Silberhorn Group**：PI Christine Silberhorn。技术路线集成光子（铌酸锂）。领导 PhoQSNET 城市量子系统网络基础设施。资助：DFG、BMBF、EU。[PhoQSNET](https://www.uni-paderborn.de/en/project/204 "PhoQSNET")

22. **ETH Zurich — Wallraff Group**：PI Andreas Wallraff。技术路线超导量子电路。2023 年 Nature 首次超导电路无漏洞贝尔检验。资助：SNSF、ERC、NCCR QSIT。[Nature 2023](https://www.nature.com/articles/s41586-023-05885-0 "Superconducting loophole-free Bell test")

**亚太（5 组）**

23. **USTC — 潘建伟团队**：PI 潘建伟，中科院院士，2025 Falling Walls 物理科学突破奖。技术路线卫星光子+光纤+离子阱。2026 年 Nature+Science 同时发表可扩展量子中继器和 11 km DI-QKD；2025 年 Nature 12,900 km 卫星 QKD；建成 CN-QCN（145 节点/12,000+ km）。资助：科技部、基金委、中科院先导专项。[The Quantum Insider](https://thequantuminsider.com/2026/02/06/chinese-researchers-clear-hurdles-for-long-distance-quantum-networks/ "USTC 双重突破 2026")

24. **清华大学 — 段路明团队**：PI 段路明，中科院院士，~47,768 次引用，2024 International Quantum Prize。技术路线离子阱。2024 年 Nature 512 离子二维量子模拟器（全球最大离子阱量子模拟）；DLCZ 量子中继器方案原始提出者（2001）。资助：基金委、科技部、清华。[Nature 2024](https://www.nature.com/articles/s41586-024-07459-0 "512-ion simulator")

25. **NTT — 量子网络研究**：企业研发。技术路线光子/连续变量。2025 年 1 月实现 60 GHz 光学量子纠缠实时生成（世界最快）；与东大 IOWN 合作开发光量子网络架构。资助：NTT 企业研发、JST Moonshot。[NTT](https://group.ntt/en/newsrelease/2025/01/29/250129a.html "60 GHz 纠缠 2025")

26. **东京大学 — Murao Group**：PI Mio Murao，量子通信理论。2026 年与 Oxford Lucas 组联合获 EPSRC/JST 资助 UK-Japan 量子互联网项目。资助：JST、MEXT、RIKEN。[Oxford](https://www.ox.ac.uk/news/2026-02-03-new-project-aims-build-foundations-quantum-internet "UK-Japan 项目")

27. **NUS Singapore — Ling Group / CQT**：PI Alexander Ling，2024 RAEng Distinguished International Associate。技术路线卫星量子通信。SpooQy-1 纳米卫星首次轨道量子纠缠光子源。资助：NRF（~S$3 亿量子战略）、CQT。[CQT](https://www.cqt.sg/highlight/2024-07-raeng-distinguished-associate/ "Ling 2024")

**其他（1 组）**

28. **Weizmann Institute — Ozeri Group**（以色列）：PI Roee Ozeri。技术路线离子阱。2022 年 PRX Quantum 建成以色列首台量子计算机；2024 年 PRX 可扩展离子阱架构。资助：Israel Innovation Authority、ERC、Weizmann。[PRX 2024](https://link.aps.org/doi/10.1103/PhysRevX.14.041017 "可扩展离子阱架构")

### 可用图片
- 无本地可用图片。建议写作时制作：全球课题组地理分布图、技术路线分布饼图。

### 仍需补充
- Stanford 是否有专门的量子网络方向实验课题组（有量子计算但量子网络方向不明确）
- Yale/Hong Tang 在 SCY-QNet 中的角色及独立量子网络贡献
- Cambridge/Atatüre Group 近 3 年量子网络方向实质性贡献确认
- FNAL SQMS 核心量子网络 PI（中心主攻超导腔，由 Anna Grassellino 领导）
- KAIST（韩国）量子网络方向课题组信息
- ANU/Ping Koy Lam（现转至 A*STAR）近 3 年量子网络实验贡献
- 各课题组 PI 的精确 H-index 值（多数仅有 Google Scholar 总引用估算）
- 欧洲各课题组从 QIA 获得的具体分拨金额
- 中国各课题组具体项目金额
- PsiQuantum、IonQ 内部量子网络研发详细信息
- Stuttgart/Wrachtrup 近年量子网络 vs 量子传感方向确认

---

## Chapter 4：多维度评估框架设计

### 研究目标
- 构建一套透明、可复现的课题组综合评估方法论
- 设计 7 个一级评估维度并定义量化指标
- 制定权重分配方案（主方案 + 敏感性分析）
- 说明数据采集方法论和局限性

### 关键发现

**评估方法论文献基础**
- CWTS Leiden Ranking 提供成熟的科学评估指标体系，包括 PP(top 10%)、MNCS 等影响力指标和 PP(int collab) 等合作指标，采用分数计数法和按领域/年份的引用标准化。[Leiden Ranking 指标说明](https://traditional.leidenranking.com/information/indicators "CWTS Leiden Ranking 2025")
- Nature Index 采用 Count 和 Share（分数计数）两个核心指标，可为"学术影响力"维度提供操作化参考。[Nature Index 方法论](https://www.nature.com/nature-index/research-leaders/2025/a-guide-to-the-nature-index.html "Nature Index 2025")
- Leiden Manifesto (Hicks et al., Nature 520, 429-431, 2015) 确立研究评估十项原则：定量评估应支持而非替代定性判断、应考虑领域差异、保持透明等。[Leiden Manifesto](https://www.leidenmanifesto.org/ "十项评估原则")
- h-index 存在可靠性问题：Akhtar (2024, Frontiers in Research Metrics and Analytics) 指出 h-index 未区分原创研究与综述贡献；Koltun & Hafner (2021, PLoS ONE) 发现 h-index 已不再与科学声誉有效相关。[Akhtar 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11294107/ "H-index unreliability")
- FWCI（领域加权引用影响）内在控制了领域、年份和文献类型差异，更适合跨学科公平比较。[Elsevier FWCI](https://helpcenter.pure.elsevier.com/en_US/data-sources-and-integrations/field-weighted-citation-impact-fwci-metrics "FWCI 定义")

**学术影响力指标最佳组合**
- 建议采用多指标组合：（1）顶刊发表数量（Nature/Science/PRL/PRX Quantum 等）；（2）近 3 年引用表现（优先 FWCI 或 PP(top 10%)）；（3）h-index 仅作辅助参考。多机构合作采用分数计数法。[Leiden Ranking](https://traditional.leidenranking.com/information/indicators "分数计数法")

**技术成熟度——TRL 适配**
- NASA TRL 9 级体系从 TRL 1（基本原理观察）到 TRL 9（成功任务运行验证），为本框架提供基础。[NASA TRL](https://esto.nasa.gov/trl/ "NASA ESTO TRL")
- Teitsma et al. (2025, arXiv:2502.16489) 提出量子组织准备度等级（QORLs），指出量子技术的非线性发展使线性 TRL 不完全适用。[arXiv:2502.16489](https://arxiv.org/html/2502.16489v1 "QORLs 2025")
- 量子网络 TRL 映射建议：TRL 1-2 = Bell 实验验证；TRL 3 = 单节点纠缠生成概念验证；TRL 4-5 = 多节点原型/短距纠缠；TRL 6 = 城市尺度 testbed（如 Delft-The Hague 25km）；TRL 7-8 = 部署光纤系统原型（如 Harvard 35km）；TRL 9 = 商用量子网络。当前全球整体处于 TRL 3-5，最先进实验达 TRL 5-6。

**技术路线前瞻性评估**
- Ruf et al. (2021, J. Appl. Phys. 130, 070901) 综述金刚石色心量子网络，明确三项核心要求：光子高效接口、量子存储、多量子比特操作。SiV ZPL 发射率 65-90%（需稀释制冷），NV ZPL 仅 ~3% 但有最成熟多量子比特寄存器。[J. Appl. Phys.](https://pubs.aip.org/aip/jap/article/130/7/070901/1061464/Quantum-networks-based-on-color-centers-in-diamond "Ruf et al. 2021")
- QIA D1.5 报告评估三种端节点平台下一代器件，指出"仅建造更多现有硬件副本不够，需重大技术创新"。[QIA D1.5](https://quantuminternetalliance.org/wp-content/uploads/sites/6/2022/05/D1.5-Comparison-report-on-next-generation-devices.pdf "QIA 平台比较 2022")
- Lee, Dai, Towsley & Englund (2024, PNAS 121(17)) 提出量子网络效用（UQN）框架，首个跨平台通用基准：双量子比特门误差 ε_eff>0 时最大联盟规模上限为 ⌊1/ε_eff⌋。[PNAS 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11047070/ "Quantum Network Utility, PNAS 2024")
- 平台可扩展性分级：**高前景**——SiV 色心（C_coh>100, 35km 纠缠）、Yb-171 中性原子（电信波段原生兼容+并行化）、离子阱+光腔（确定性光子图态）；**中等前景**——NV 色心（最成熟网络记录但 ZPL 3%）、稀土离子（理论 2000km 但早期）、铒/硅（唯一电信波长相干跃迁但相干时间待提升）；**待验证**——超导（需微波-光子转换）、量子点（确定性纠缠待突破）、卫星光子（属可信中继范式）。

**权重方案**
- 基于 AHP 方法论 (Saaty, 1980)，建议 7 维度主方案：技术成熟度 25%、学术影响力 20%、技术路线前瞻性 15%、团队实力 15%、经费与资源 10%、项目网络与合作 10%、专利与产业化 5%。[Saaty 1990](https://www.sciencedirect.com/science/article/pii/037722179090057I "AHP, European Journal of OR")
- 敏感性方案 A（学术优先）：学术影响力 30%、技术成熟度 20%、技术路线前瞻性 20%、其余调低。
- 敏感性方案 B（工程优先）：技术成熟度 35%、经费与资源 15%、专利与产业化 10%、学术影响力 15%、其余调低。

**数据采集与缺失处理**
- 各维度数据来源：Google Scholar/Scopus（学术）、课题组官网/论文（技术成熟度）、NSF Award Search/CORDIS（经费）、Google Patents/EPO（专利）。
- 中国经费数据不透明：ITIF (2024) 指出中国量子研究经费"仍然模糊"，国际合作论文比例仅 19%（美国约 50%）。替代策略：NSFC 公开数据库+新闻交叉验证+中位数赋值。[ITIF 2024](https://itif.org/publications/2024/09/09/how-innovative-is-china-in-quantum/ "How Innovative Is China in Quantum?")

**方法论局限性**
- 六项固有局限：引用滞后效应、h-index 学科偏差/可博弈性、TRL 映射主观性、经费数据不对称、产业化指标早期局限性、快照偏差。
- 稳健性增强策略：三方案交叉验证、最优/最劣/中位数三情景模拟、报告排名区间而非唯一排名、识别"排名稳健型"vs"排名敏感型"课题组。

### 可用图片
- 无本地可用图片。建议写作时制作：评估维度与权重体系示意图、TRL 映射对照表、AHP 权重对比表。

### 仍需补充
- Scopus FWCI 在量子物理子领域的基准值（设定评分阈值所需）
- Wehner 六阶段路线图作为 TRL 补充参考的具体映射（在写作时与 Chapter 1 交叉引用）
- 完整 AHP 7×7 成对比较矩阵及一致性验证（留给 Chapter 5 执行）
- 产业化指标细化标准（专利数量分档、合作深度定义等）

---

## Chapter 5：横向比较分析

### 研究目标
- 基于 Chapter 4 的评估框架，对 Chapter 3 收录的 28 个课题组进行系统化横向比较
- 产出各维度分项排名与得分分布
- 按技术路线聚类分析、按地理区域聚类分析
- 输出综合得分总排名表及敏感性分析
- 讨论学术产出 vs 实验进展、经费规模 vs 技术突破、老牌强组 vs 新兴团队等关键议题

### 关键发现

**综合排名 Top 10（主方案 7 维度加权 1-10 分制）**

| 排名 | 课题组 | 主方案 | 方案A(学术优先) | 方案B(工程优先) | 稳健性 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Harvard/Lukin | 9.33 | 第1 (9.47) | 第1 (9.10) | 稳健——三方案均第1 |
| 2 | USTC/潘建伟 | 9.05 | 第2 (8.90) | 第2 (9.22) | 稳健——三方案均 Top 2 |
| 3 | QuTech/Hanson | 8.75 | 第3 (8.55) | 第3 (8.92) | 稳健——三方案均 Top 3 |
| 4 | MPQ/Rempe | 7.75 | 第4 (7.92) | 第5 (7.40) | 稳健——三方案均 Top 5 |
| 5 | MIT/Englund | 7.57 | 第5 (7.70) | 第6 (7.30) | 基本稳健——第5-6名 |
| 6 | UChicago/Awschalom | 7.38 | 第6 (7.28) | 第7 (7.20) | 基本稳健——第6-7名 |
| 7 | Duke/Kim (IonQ) | 7.20 | 第8 (7.05) | 第4 (7.47) | 敏感——工程优先升至第4 |
| 8 | 清华/段路明 | 6.92 | 第7 (7.30) | 第10 (6.37) | 敏感——学术强/工程弱 |
| 9 | ETH/Wallraff | 6.88 | 第8 (7.05) | 第8 (6.75) | 基本稳健——Top 8-10 |
| 9 | Innsbruck/Northup-Lanyon | 6.88 | 第9 (6.92) | 第9 (6.58) | 基本稳健——Top 9-10 |

边缘组：QuTech/Wehner（主方案第11, 6.50）、Stony Brook/Figueroa（第12, 6.43）、Sorbonne/Laurat（第13, 6.35）。

评分数据来源包括：[Google Scholar](https://scholar.google.com "各PI引用数据, 2026年4月读取")、[NSF Award Search](https://www.nsf.gov/awardsearch/ "美国NSF资助数据")、[CORDIS](https://cordis.europa.eu "欧盟资助数据")、[IonQ 投资者关系](https://investors.ionq.com/news/news-details/2025/IonQ-Expands-Quantum-Networking-Patent-Portfolio-to-Meet-Strong-Market-Demand-for-Secure-Communications/default.aspx "IonQ ~400项量子网络专利")、[Argonne Q-NEXT](https://www.anl.gov/article/argonneled-qnext-quantum-center-renewed-for-five-years "Q-NEXT $125M续期")、[Stony Brook SCY-QNet](https://news.stonybrook.edu/newsroom/stony-brook-university-led-team-receives-4m-nsf-grant-to-develop-10-node-quantum-network/ "SCY-QNet NSF $4M")、[CQN ERC](https://app.dimensions.ai/details/grant/grant.9381310 "CQN $32.4M, 2020-2026")。

**分维度关键观察**
- **学术影响力**（20%）：Top 3 为 Lukin（10, h-207, ~163K 引用）、潘建伟（9.5, ~100K 引用）、Englund（9, h-116）。色心和离子阱阵营学术积累最深。
- **技术成熟度**（25%）：Top 3 为潘建伟（10, CN-QCN 145 节点已部署 TRL 7-8）、Hanson（9.5, 三节点网络+25km 城市链路 TRL 5-6）、Lukin（9, 35km 电信网络 SiV 纠缠 TRL 5-6）。
- **团队实力**（15%）：Top 3 为 Lukin（10, NAS 院士）、潘建伟（10, CAS 院士）、Awschalom（9.5, NAS+NAE+AAAS 三院院士）。
- **经费与资源**（10%）：Top 3 为 Awschalom（10, Q-NEXT $125M/5yr）、潘建伟（9.5, 国家实验室级别）、Hanson（9, Quantum Delta NL €6.15 亿生态）。
- **项目网络**（10%）：Hanson 最高（10, QIA 协调人+Quantum Delta NL）、潘建伟/Lukin/Awschalom 并列（9）。
- **专利产业化**（5%）：Duke/Kim(IonQ) 遥遥领先（10, ~400 项量子网络专利+NYSE 上市）、Lukin（8, QuEra $230M 融资）、Hanson（7.5, Delft Networks 2024 创立）。
- **技术路线前瞻性**（15%）：Lukin(SiV) 9.5、Covey(Yb-171)/Rempe(Rb 光腔) 并列 9、Thompson/Innsbruck 8.5。

**技术路线聚类分析**
- **金刚石色心（4组, 平均 8.26）**：综合最强阵营。含 Top 1（Lukin）和 Top 3（Hanson）。SiV C_coh>100、35km 电信纠缠为领域最高成就。劣势：SiV 需稀释制冷 <0.1K。趋势：NV→SiV/SnV 转型中。
- **中性原子（5组, 平均 6.10）**：技术前瞻性最高（D7 平均 8.3）。MPQ/Rempe 光腔内 2D 原子阵列+确定性光子图态引领方向。Yb-171 电信原生兼容+并行化极具潜力，但多数仍在 TRL 3-4。
- **离子阱（5组, 平均 6.47）**：多量子比特操控最成熟，IonQ 已商业化（~400 专利）。但光互联 TRL 3-4，最长网络链路仅 230m（Innsbruck），远逊色心阵营。
- **稀土离子（4组, 平均 5.58）**：与硅光子工业天然兼容，理论可扩展至 2,000km。但单离子控制仍早期（TRL 2-3），里程碑最少的阵营。长期看好、短期缺里程碑。
- **卫星/QKD（2组）**：USTC 拥有最大规模部署网络，但基于可信中继非量子网络范式。2026 年量子中继器突破标志战略转型。
- **超导（1组）**：ETH/Wallraff 首次超导无漏洞 Bell 检验，但微波-光子转换是核心瓶颈。

**地理区域聚类**
- **北美（10组, 平均 6.59）**：资金最大（DOE $625M+NSF CQN $32M+NQVL）、PI 集中度最高、产业生态最成熟。但部分新锐组起步阶段，testbed 建设起步较晚。
- **欧洲（12组, 平均 6.37）**：数量最多但质量分化。Hanson+Rempe 世界顶级，QIA 提供统一协调。产业化/专利维度薄弱。理论/协议方向全球领先。
- **亚太+其他（6组, 平均 5.99）**：USTC 一枝独秀。中国部署规模全球第一但国际合作封闭（~19% vs 美国 ~50%），经费不透明。参考 [ITIF 2024](https://itif.org/publications/2024/09/09/how-innovative-is-china-in-quantum/ "中国量子创新评估")。

**关键议题**
- **学术 vs 实验**：两维均强者为真正全能型（Lukin/潘建伟/Hanson）。清华/段路明和 ETH/Wallraff 学术强但量子网络实验偏弱（引用主要来自其他方向）。
- **经费 vs 突破**：超过 ~$10M/年后，突破更依赖聚焦度而非资金量。Awschalom(Q-NEXT $125M) D2 仅 5 分是最显著反例。MPQ/Rempe 中等经费但高产出。
- **老牌 vs 新兴**：老牌组占 Top 10 的 7 席，但新兴团队（Covey/Zhong/Bernien/Thompson/Reiserer）技术路线前瞻性维度平均 8.1，高于老牌组 7.2。代际切换正在发生：Bernien（博士 Hanson→博后 Lukin）、Reiserer（博后 Rempe）。

### 可用图片
- 无本地可用图片。建议写作时制作：Top 5-6 组雷达图、技术路线聚类气泡图、地理区域堆叠条形图、三方案排名热力图、排名敏感性河流图。

### 仍需补充
- 各 PI 在量子网络子领域的 Scopus FWCI 精确值（当前基于 Google Scholar 总引用间接估算，跨领域通胀效应未消除）
- 2024-2026 年顶刊发表精确计数（需 Scopus/WoS 系统检索过滤）
- 中国课题组具体资助金额（USTC、清华均采用高位估算）
- 除 IonQ 外各学术课题组专利持有精确数据（需 USPTO/EPO 系统检索）
- QuTech/Wehner 的 QNodeOS 和 SimulaQron 的 TRL 映射需进一步讨论（软件类成果评估标准与硬件不同）

---

## Chapter 6：Top 10 最具潜力课题组深度剖析

### 研究目标
- 对综合评估排名前十的课题组逐一深度分析
- 每个课题组统一结构：核心技术突破、代表性论文、团队脉络、经费与项目、合作网络、专利与产业化、未来 6 个月预期
- 分析十组之间的互动关系（合作、竞争、互补）
- 从 Top 10 整体看量子网络领域的技术方向收敛趋势

### 关键发现

**1. Harvard/Lukin（主方案 9.33, SiV 色心）**
- 近 12 个月三连发：Science 2025 首次固态量子比特盲量子计算 (doi:10.1126/science.adu6894)；Nature 2026 纠缠辅助非局域光学干涉术 1.55km 基线 (doi:10.1038/s41586-026-10171-w)；延续 Nature 2024 35km 电信网络 SiV 纠缠 (doi:10.1038/s41586-024-07252-z)。[Science 2025](https://www.science.org/doi/10.1126/science.adu6894 "盲量子计算")；[Nature 2026](https://www.nature.com/articles/s41586-026-10171-w "非局域干涉术")
- 师承 Scully→Lukin；培养 Bernien(→UChicago)、Bhaskar、Knaut 等下一代。多名核心成员被 IonQ 招揽（Machielse、Riedel、Borregaard）。
- 经费：NSF CQN ERC ~$32.4M (2020-2026)、AWS 量子网络中心、DOE、DARPA。[Dimensions](https://app.dimensions.ai/details/grant/grant.9381310 "CQN $32.4M")
- 衍生企业 QuEra $230M 融资（2025 年 2 月）。[QuEra](https://www.quera.com/press-releases/quera-computing-completes-230m-financing-to-accelerate-development-of-large-scale-fault-tolerant-quantum-computers "$230M 融资")
- 未来预期：向三节点以上 SiV 网络推进；量子增强成像后续工作；可能探索 SnV 降低冷却要求。

**2. USTC/潘建伟（9.05, 卫星+光纤+离子阱）**
- 2026 年 2 月 Nature+Science 同时发表：可扩展量子中继器核心组件（陷俘离子长寿命存储器）和 11km DI-QKD（此前记录 ~50 倍提升）。[CAS 新闻](https://english.cas.cn/newsroom/cas-in-media/202602/t20260206_1149922.shtml "USTC 2026 双重突破")；[The Quantum Insider](https://thequantuminsider.com/2026/02/06/chinese-researchers-clear-hurdles-for-long-distance-quantum-networks/ "长距离量子网络突破")
- "济南一号"卫星 12,900km QKD（Nature 2025）；CN-QCN 145 节点/12,000km 运营中。
- 师承 Zeilinger(2022 诺奖)→潘建伟；核心团队：陆朝阳、彭承志、陈宇翱、包小辉。2025 Falling Walls Prize。国际合作论文比例仅 ~19%。
- 经费：国家量子信息科学实验室（合肥）、科技部/基金委/中科院先导专项、安徽省量子基金。具体金额未公开。
- 未来预期：量子中继器多节点串联；DI-QKD 向 200+km 推进；"墨子二号"或新一代卫星可能进入准备阶段。

**3. QuTech/Hanson（8.75, NV 色心→SnV 转型）**
- 2026 年 1 月 Nature Comms：腔增强 NV 光子收集概率从 0.05% 提升至 0.5%（10 倍），保持 T₂>100μs。[QuTech](https://qutech.nl/2026/01/15/more-photons-faster-links-a-laser-focused-nv-centre/ "腔增强 NV 2026")
- 延续 Science Advances 2024 25km 城市链路（doi:10.1126/sciadv.adp6442）和 Nature 2021 三节点网络（被引 876 次）。
- 师承 Awschalom(博后)→Hanson；培养 Bernien(博士)。Spinoza Prize 2019、Bell Prize 2017、KNAW 院士。2024 年创立 Delft Networks 商业化。
- 经费：QIA 协调人（€24M）、Quantum Delta NL（€6.15 亿）、NWO、ERC。
- 未来预期：腔增强 NV+部署光纤高速纠缠；SnV 1.8K 运行温度节点验证；Delft Networks 首款产品原型。

**4. MPQ/Rempe（7.75, Rb 原子光腔）**
- PRL 2025 (doi:10.1103/5zk9-3rpv) 宣告式原子-光子纠缠源；Science 2024 光腔内光镊 2D 原子阵列网络寄存器 (doi:10.1126/science.ado6471)；Nature 2024 确定性光子图态融合 (doi:10.1038/s41586-024-07357-5)。[PRL 2025](https://link.aps.org/doi/10.1103/5zk9-3rpv "宣告式纠缠源")
- 师承 Kimble(量子互联网概念提出者)→Rempe，MPQ Director。与段路明有共同 Kimble 渊源。
- 经费：Max Planck Society+DFG+QIA+BMBF。
- 未来预期：光镊阵列+远程纠缠结合；宣告式纠缠+电信波段频率转换整合；多原子图态融合扩展。

**5. MIT/Englund（7.57, 金刚石色心集成光子）**
- 2025 年 Nature Comms 硅色心纳米定位与光谱调谐 (doi:10.1038/s41467-025-63871-8)；推进"ski jump"光子芯片互联技术。[MIT RLE](https://www.rle.mit.edu/quantum-photonics-and-ai-group-achieves-breakthrough-in-controlling-silicon-color-centers-for-scalable-quantum-technologies/ "硅色心突破")
- 与 Lukin 深度合作（CQN 核心 PI，波士顿 50km 测试床联合开发）。PNAS 量子网络效用框架。
- 经费：CQN ERC Co-Deputy Director、DARPA、DOE、MIT AI Hardware Program。
- 未来预期：集成光子量子网络芯片里程碑；波士顿测试床节点扩展。

**6. UChicago/Awschalom（7.38, Q-NEXT/固态缺陷）**
- 2025 年 11 月 Q-NEXT $125M/5yr 续期。碳化硅钒缺陷（V⁴⁺ in 4H-SiC）电信频率自旋量子比特新进展。[Argonne](https://www.anl.gov/article/argonneled-qnext-quantum-center-renewed-for-five-years "Q-NEXT 续期")；[Q-NEXT](https://q-next.org/vanadium-in-silicon-carbide-for-scalable-quantum-networks/ "SiC 钒缺陷")
- PRX Quantum 2021 QuICs 路线图（被引 500+次）。三院院士。Awschalom→Hanson 师承关系。
- 经费：Q-NEXT $125M+Chicago Quantum Exchange。管理角色可能稀释直接研究产出（D2 仅 5 分）。
- 未来预期：芝加哥-Argonne 跨城市纠缠实验；SiC 钒缺陷量子网络节点原型；分子量子比特突破。

**7. Duke/Kim (IonQ)（7.20, 离子阱/产业化）**
- IonQ 量子网络专利 ~400 项（含 Qubitekk+IDQ ~250 项），专利总数破 1,000 项 (2025 年 8 月)。AFRL 合同 $54.5M+$21.1M+ARLIS $5.7M。[IonQ IR](https://investors.ionq.com/news/news-details/2025/IonQ-Expands-Quantum-Networking-Patent-Portfolio-to-Meet-Strong-Market-Demand-for-Secure-Communications/default.aspx "IonQ 专利")
- Kim+Monroe(Maryland) 联合创立 IonQ (2015)。2026 年 3 月与 Cambridge 建立战略合作。EPB Chattanooga 量子网络商用运营。
- 排名敏感型：工程优先方案下升至第 4，学术优先下降至第 8。
- 未来预期：量子网络产品线发布；Cambridge 中心启动；离子阱光互联关键演示。

**8. 清华/段路明（6.92, 离子阱/理论）**
- Science Advances 2025 双类型量子比特离子阱网络节点 (doi:10.1126/sciadv.aeb4076)；Nature 2024 512 离子 2D 量子模拟器。[Science Advances 2025](https://www.science.org/doi/abs/10.1126/sciadv.aeb4076 "双类型网络节点")
- CAS 院士，h-92，DLCZ 方案原始提出者（被引 4,566 次）。博后 Zoller(Innsbruck)+Kimble(Caltech)。2024 International Quantum Prize。
- 排名敏感型：学术优先第 7，工程优先降至第 10。量子网络实验相对少是短板。
- 未来预期：双类型节点+远程光纤纠缠结合；512 离子平台向纠错推进。

**9（并列）. ETH/Wallraff（6.88, 超导量子电路）**
- Nature Comms 2025 确定性 2D 多光子集群态（20 光子量子比特）(doi:10.1038/s41467-025-60472-3)；Nature Physics 2026 格子手术量子纠错 (doi:10.1038/s41567-025-03090-6)；Nature 2023 首次超导无漏洞 Bell 检验 (doi:10.1038/s41586-023-05885-0)。[Nature Comms 2025](https://www.nature.com/articles/s41467-025-60472-3 "2D 集群态")
- 博后 Yale/Schoelkopf，cQED 奠基人之一（2004 Nature 被引 >10,000 次）。
- 经费：SNSF+ERC SuperQuNet+NCCR QSIT+ETH。微波-光子转换瓶颈是核心限制。
- 未来预期：2D 集群态+微波-光子转换整合；格子手术扩展；超导跨稀释制冷机纠缠速率提升。

**9（并列）. Innsbruck/Northup-Lanyon（6.88, 离子阱光腔）**
- PRL 2025 10 量子比特光子接口网络节点（92% 纠缠保真度，可扩展至数百离子）(doi:10.1103/v5k1-whwz)；2023 年 230m 校园离子纠缠网络；曾实现 50km 光纤离子-光子纠缠。[Innsbruck](https://www.uibk.ac.at/en/newsroom/2025/powerful-nodes-for-quantum-networks/ "10 量子比特节点 PRL 2025")
- Blatt 学派传承（离子阱 QC 发源地之一），与 Zoller 理论组结合。
- 经费：QIA+FWF+ERC。
- 未来预期：10 量子比特节点+远程纠缠结合；向数十量子比特扩展；钙离子→电信波段频率转换。

**十组互动关系**
- **合作链**：Lukin↔Englund（CQN，波士顿测试床）；Hanson↔Innsbruck（QIA）；段路明↔潘建伟（DLCZ 理论→实验）；段路明与 Rempe/Kimble 体系有共同渊源。
- **师承网络**：Awschalom→Hanson→Bernien→(Harvard/Lukin 博后)；Kimble→Rempe；Zeilinger→潘建伟；Scully→Lukin；Schoelkopf→Wallraff；Blatt→Northup/Lanyon；Zoller↔段路明。
- **竞争**：Lukin(SiV) vs Hanson(NV→SnV) 在色心城域纠缠距离竞争；USTC vs 西方组在网络规模和范式上竞争；Rempe(中性原子腔) vs Innsbruck(离子阱腔) 在腔 QED 网络节点路线上竞争。
- **互补**：IonQ 提供产业化通道（~400 专利+NYSE 上市）；Awschalom/Q-NEXT 为多组提供基础设施；Wallraff 超导方向与固态/原子平台互补（若微波-光子瓶颈突破）。

**五大技术方向收敛趋势**
1. 从单/双节点演示→三节点以上网络推进
2. 量子网络应用多样化：纠缠分发→盲量子计算、天文干涉术、DI-QKD
3. 电信波段兼容性成为硬约束：几乎所有平台都在解决 1350-1550nm 兼容
4. 腔增强成为共识路径：QuTech/Hanson、MPQ/Rempe、Innsbruck 均转向腔增强方案
5. 学术-产业双轨加速：IonQ(~400 专利)、Delft Networks(2024)、QuEra($230M)

### 可用图片
- 无本地可用图片。建议写作时制作：每个 Top 10 课题组合作网络图、论文发表时间线、师承关系谱系图、技术路线收敛趋势图。

### 仍需补充
- 各课题组近 12 个月论文精确引用数据（部分 2025-2026 论文尚无足够引用积累）
- USTC/潘建伟和清华/段路明具体项目金额和周期
- 除 IonQ 外各学术组量子网络方向专利精确数量
- Delft Networks 和 QuEra 最新商业化进展细节
- ETH/Wallraff 微波-光子转换最新实验数据
- 段路明团队双类型网络节点后续远程纠缠实验进展
- MPQ/Rempe 具体经费数额（MPI Director 级别基础资助+DFG/EU 分拨）

---

## Chapter 7：未来展望与战略研判

### 研究目标
- 研判量子网络领域未来 12-18 个月的发展趋势与关键变量
- 技术瓶颈突破展望、政策资金趋势、竞争格局演变、产业化路径与时间窗口
- 风险因素分析和值得持续关注的跟踪指标清单
- 局限性声明

### 关键发现

**技术瓶颈与突破展望**
- 腔增强光子收集效率是近期最有望突破的瓶颈：QuTech 2026 年 1 月实现 10 倍提升至 0.5%，预计 12-18 个月内有望突破 1%/脉冲，直接转化为纠缠速率量级提升。[QuTech](https://qutech.nl/2026/01/15/more-photons-faster-links-a-laser-focused-nv-centre/ "腔增强 NV 2026")
- 量子中继器从原理验证向工程化推进：USTC 2026 年 2 月首次演示可扩展核心组件，预计向多节点串联推进。[CAS](https://english.cas.cn/newsroom/cas-in-media/202602/t20260206_1149922.shtml "USTC 量子中继器 2026")
- SnV 色心替代 NV 色心趋势明确（预期运行温度 ~1.8K vs SiV 的 ~100mK），预计 12-18 个月内可能实现首个远程纠缠演示。
- Yb-171 中性原子电信原生兼容+并行化（UIUC/Covey 2025 Nature Physics），预计可能实现首个远程原子-原子纠缠。
- QNodeOS 量子网络操作系统于 2025 年 3 月在 Nature 发表，首个全可编程量子网络 OS，预计部署到 QuTech Quantum Network Explorer 测试平台。[QIA](https://quantuminternetalliance.org/2025/03/12/qia-researchers-create-first-operating-system-for-quantum-networks/ "QNodeOS Nature 2025")；[Nature](https://www.nature.com/articles/s41586-025-08704-w "QNodeOS 论文")
- 微波-光子转换仍是超导平台核心瓶颈，短期 12-18 个月内预计仍将限制超导参与量子网络，但 IBM-Cisco 合作（2025 年 11 月）可能加速工程投入。
- 12-18 个月内首个四节点以上纠缠量子网络演示是可期待的里程碑。

**政策与资金趋势**
- 美国 NQI 重新授权法案（S.3597）2026 年 1 月 8 日由两党参议员提出，拟延长至 2034 年，新增 NASA 量子研发授权、NIST 量子中心、量子人才协调中心等条款，已获 IBM/Microsoft/Google/IonQ 等背书。[Quantum Computing Report](https://quantumcomputingreport.com/senators-introduce-bipartisan-national-quantum-initiative-reauthorization-act-of-2026/ "NQI 重新授权 2026")
- 关键政策节点展望：（1）NQI 重新授权预计 2026 年内通过；（2）QIA Phase 2 资助规模是欧洲量子网络研究关键变量；（3）NSF CQN ERC 2026 年到期，续期结果直接影响 Harvard/Lukin 和 MIT/Englund；（4）英国 £1.25 亿量子网络专项分配方案预计 2026 年下半年明确。
- Welinq QDrive 量子存储器 2026 年 1 月完成首个商业交付（斯洛伐克科学院，skQCI 项目），标志 EuroQCI 从规划向部署转型。[The Quantum Insider](https://thequantuminsider.com/2026/01/14/welinq-qdrive-sale-slovak-academy/ "Welinq 首次商业交付 2026")

**竞争格局演变预判**
- 核心稳健 Top 3（Harvard/Lukin、USTC/潘建伟、QuTech/Hanson）预计 12-18 个月内维持领先。
- 排名敏感型变动因素：IonQ 量子网络产品线发布进度；清华/段路明双类型节点+远程纠缠结合；MIT/Englund CQN 到期后资金走向。
- 三大黑马团队：UIUC/Covey（Yb-171 远程纠缠可能改变格局，Google 2026 年 3 月增加中性原子模态可能带来产业资源）[The Quantum Insider](https://thequantuminsider.com/2026/03/24/google-paves-a-two-lane-quantum-roadmap-by-adding-neutral-atom-systems/ "Google 中性原子 2026")；Princeton/Thompson（超导 1ms+ 相干+微波-光子转换结合）；TUM/Reiserer（铒离子电信 C 波段原生+硅光子兼容）。
- 人才流动：Harvard/Lukin→IonQ（Machielse、Riedel、Borregaard）反映 SiV 技术产业吸引力；Hanson→Bernien(UChicago) 形成学术扩散。

**产业化路径与时间窗口**
- 量子通信市场 2023 年 $9-10 亿，预计 CAGR 23-25%，2035 年可达 $105-149 亿（McKinsey 2025 年 2 月）。[McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/quantum-communication-growth-drivers-cybersecurity-and-quantum-computing "McKinsey 量子通信 2025")
- 量子网络细分市场 2026 年 $18.22 亿，预计 2034 年达 $364.21 亿，CAGR 45.41%（Fortune Business Insights）。[Fortune BI](https://www.fortunebusinessinsights.com/quantum-networking-market-115145 "量子网络市场 2026-2034")
- 量子计算整体 2040 年创造 $4,500-8,500 亿经济价值（BCG 2024 年 7 月），但 NISQ 时代近期价值低于预期（因 AI 竞争超预期）。[BCG](https://www.bcg.com/publications/2024/long-term-forecast-for-quantum-computing-still-looks-bright "BCG 量子计算展望 2024")
- 首批实用量子优势预期 2028-2029 年（~100 逻辑量子比特），商业影响级应用（1,000-10,000 逻辑量子比特）2030 年代中期（Bain & Company）。[CNBC](https://www.cnbc.com/2026/03/30/quantum-computing-firms-go-public-breakthroughs-commercialization.html "Bain 量子时间线 2026")
- 关键里程碑时间窗口：2026 年 Welinq/IonQ/Delft Networks 首批产品；2027-2028 年 QIA Phase 2 多城市网络部署；2028-2030 年 IBM-Cisco 概念验证+SCY-QNet 10 节点全面运行；2030 年代商用城域量子网络规模化部署。
- 2026 年量子公司上市潮（Xanadu、Horizon、Infleqtion 通过 SPAC 上市），产业叙事从"科学项目"转向"商业化轨迹"。

**风险因素**
- 人才短缺：NIST 主任 Kushmerick 2026 年 1 月国会听证会警告"不折不扣的短缺"，NQI 以来学生/教职几乎翻倍但仍不足。[The Quantum Insider](https://thequantuminsider.com/2026/01/23/experts-tell-u-s-lawmakers-quantums-next-bottleneck-isnt-hardware-its-people/ "量子人才短缺 2026")
- 地缘政治与供应链：NQI 重新授权专设供应链强化条款；2025 年 4 月关税冲击致 IonQ 等股价大跌；中美量子竞争加剧可能影响国际合作和人才交流。
- AI 竞争超预期：BCG 指出 NISQ 时代近期价值创造低于预期，AI 为原本量子独占的问题提供"足够好"替代。
- 量子纠错开销巨大：30+ 量子比特电路最高仅 99.5% 保真度，有用算法需百万-数十亿次门操作。分布式量子计算的跨网络高保真门操作同样严苛。
- 资金持续性：NQI 重新授权尚未完成；CQN ERC 2026 年到期；QIA Phase 2 规模未定。长研发周期（BCG 预计 2040 年前全面容错）要求资金持续性。
- 技术路线不确定性：部分不成熟量子比特模态预计 2026 年底可能被放弃（Safe Quantum 预测），依赖该路线的课题组面临调整风险。[TQI](https://thequantuminsider.com/2025/12/30/tqis-expert-predictions-on-quantum-technology-in-2026/ "TQI 2026 专家预测")

**跟踪指标清单（21 项）**

*技术*：(1) 各平台纠缠速率与保真度进展；(2) 量子存储/相干时间记录更新；(3) 多节点网络规模（突破 3 节点）；(4) 量子中继器多跳串联进展；(5) 腔增强光子收集突破 1%/脉冲；(6) 微波-光子转换效率突破。

*政策与资金*：(7) NQI 重新授权法案立法进展；(8) NSF CQN ERC 续期结果；(9) QIA Phase 2 资助确认；(10) 英国 £1.25 亿量子网络分配方案；(11) 各国量子年度预算变化。

*竞争格局*：(12) Top 10 课题组顶刊发表动态（季度跟踪）；(13) 关键人才学术→产业流动趋势；(14) 新兴组论文突破（UIUC/Covey、Princeton/Thompson、TUM/Reiserer）；(15) Google 中性原子项目量子网络关联进展。

*产业化*：(16) Welinq 产品线商业交付数量；(17) IonQ 量子网络产品线发布；(18) Delft Networks 首款硬件原型；(19) 量子公司 IPO/SPAC 和估值变化；(20) IBM-Cisco 量子网络技术演示进度；(21) ITU-T/ETSI/IEEE 量子网络标准化进展。

**局限性声明**
- 信息不对称：中国课题组经费/专利/军方项目数据因透明度限制可能被低估或高估；俄罗斯、印度等国未纳入分析。
- 语言偏差：以英文和中文文献为主，日文/韩文/德文文献覆盖不足。
- 时效性：截止 2026 年 4 月初，下半年新突破可能改变判断。
- 市场预测差异：McKinsey/BCG/Fortune BI 等对量子网络市场的定义边界和预测方法不同，2025 年市场规模估算从 $5.86 亿到 $11.5 亿不等。

### 可用图片
- 无本地可用图片。建议写作时制作：技术突破时间线预测图、产业化里程碑路线图、跟踪指标仪表盘模板。

### 仍需补充
- McKinsey 量子通信完整报告的量子网络 vs PQC vs QKD 细分数据和地区拆分
- QIA Phase 2 正式公告（Phase 1 2026 年 3 月完成后）
- IonQ 2026 年量子网络产品具体技术参数
- ITU-T/ETSI 量子网络标准化最新会议纪要和工作文件
- 各课题组 2026 年下半年 arXiv 预印本中的重要成果

---

# Section 2：给 Write 阶段的执行建议

1. **时间口径**：全文所有时间表述必须与"近期进展 = 2025-04 至 2026-04；展望 = 2026-04 至 2026-10"口径一致。
2. **评估方法论口径**：Chapter 4 定义的框架是全报告方法论基石，Chapter 5/6 必须严格依照 Chapter 4 的维度、权重和评分标准执行，不得在后续章节临时引入新维度或修改权重。
3. **课题组口径**：Chapter 3 的清单是 Chapter 5/6 的唯一输入源。Top 10 必须从 Chapter 3 清单中产生。同一课题组在不同章节中的名称、机构、PI 姓名拼写必须完全一致。
4. **数据核验要求**：论文数据需交叉验证（至少两个来源）；经费数据优先使用官方公告（DOE/NSF award database、CORDIS、中国科技部公示）；专利数据使用 Google Patents/USPTO/EPO/CNIPA。
5. **定量与定性判断边界**：凡涉及排名、评分、"最具潜力"等判断须基于 Chapter 4 的量化得分；数据不足时须明确标注"基于有限公开信息的估算"。
6. **术语一致性**：首次出现时给出中英对照，后续统一使用中文。
7. **图表建议**：Ch1-路线图/技术栈图；Ch2-各国资助规模柱状图；Ch3-全球课题组地理分布图；Ch5-雷达图/热力图/排名表；Ch6-合作网络图/论文时间线。
8. **局限性声明**：在 Chapter 4 和 Chapter 7 各包含对评估局限性的坦诚说明（信息不对称、语言偏差、时效性）。
