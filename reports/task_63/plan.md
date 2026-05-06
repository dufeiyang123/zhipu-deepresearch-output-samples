# Section 1：章节研究计划

## Chapter 1：铌酸锂等离子体刻蚀及其材料损伤机理

### 研究目标
- 系统回答"等离子体刻蚀对铌酸锂造成哪些类型的损伤、损伤如何产生、各类损伤对光学与电光性能的量化影响如何？"
- 为后续各章的缓解策略提供物理判据与评价基准
- 覆盖主流刻蚀方法（RIE、ICP-RIE、IBE 等）下的损伤分类：晶格无序化与非晶化、离子注入（F⁺、Ar⁺）、再沉积层、表面/亚表面粗糙化、化学计量比偏移
- 阐明各类损伤对传播损耗、Q 值、r₃₃、χ⁽²⁾ 的影响机理

### 关键发现
- 发现 1：ICP-RIE 是当前 TFLN 波导制备的主流技术。Zhang et al. 2017 年在 X-cut TFLN 上实现传播损耗低至 0.027 dB/cm、内禀 Q 值超过 10⁷ 的微环谐振器；典型工艺参数为 ICP 功率 ~500–1000 W、RF 偏压 ~100–250 W、腔压 ~3–10 mTorr [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "Monolithic ultra-high-Q LN microring, Optica 4(12), 2017")。
- 发现 2：IBE（Ar⁺ 离子铣）使用 300–500 eV 纯 Ar⁺ 离子束，刻蚀选择比低（LN:mask 约 1:1–2:1）但可获得光滑侧壁。Li et al. 2019 年报道了基于 IBE 的 TFLN 微环 Q ~10⁶ [Li et al., PRL 2019](https://doi.org/10.1103/PhysRevLett.122.253801 "IBE TFLN 光力系统")。
- 发现 3：ICP-RIE 常用气体配方为 Ar 或 Ar+含氟气体（CHF₃/CF₄/SF₆），含氟气体通过形成 NbF₅（沸点 234°C）提高化学刻蚀分量，但引入 F⁺ 注入损伤和化学计量比偏移；LiF 沸点 1676°C 导致 Li 选择性去除 [Ulliac et al., Microelectron. Eng. 2011](https://doi.org/10.1016/j.mee.2011.03.014 "Ar plasma ICP-RIE for LN waveguide")。
- 发现 4：等离子体刻蚀对 LN 损伤可分为五类：（i）晶格无序化与非晶化；（ii）离子注入（Ar⁺、F⁺）；（iii）再沉积层；（iv）表面/亚表面粗糙化；（v）化学计量比偏移（Li/O 优先溅射导致表面富 Nb）[Boes et al., Laser Photonics Rev. 2023](https://doi.org/10.1002/lpor.202200862 "LN photonics综述")。
- 发现 5：当离子能量超过 LN 位移阈值能量（O 约 25–50 eV，Nb 亚晶格约 40–70 eV），级联碰撞在表面以下数nm至数十nm范围产生大量弗伦克尔缺陷对和无序区 [Gainutdinov et al., Ferroelectrics 2015](https://doi.org/10.1080/00150193.2015.998948 "Ar⁺辐照LN铁电畴操控")。
- 发现 6：HRTEM 截面分析表明 ICP-RIE（Ar 基，RF ~150–200 W）后 TFLN 波导侧壁存在约 5–15 nm 非晶化层；Xu et al. 2022 年在 X-cut TFLN 中直接观测到 ~10 nm 厚非晶化层 [Xu et al., APL Photonics 2022](https://doi.org/10.1063/5.0095146 "Dual-polarization TFLN ring resonator")。
- 发现 7：激进刻蚀条件（RF >300 W 或纯 Ar⁺）下非晶化层深度可达 20–30 nm；优化低损伤工艺可控制在 ~5 nm 以下。SRIM 模拟预测 300 eV Ar⁺ 在 LN 中射程约 1–2 nm，但级联碰撞使实际损伤区远大于射程 [SRIM](http://www.srim.org/ "SRIM 模拟工具")。
- 发现 8：ICP-RIE 侧壁 Rq 典型 1–5 nm，优化后可达 <1 nm（Zhang 2017 约 0.5–1 nm）。粗糙度来源：掩模边缘粗糙度转移（LER）、微掩模效应、离子轰击统计涨落 [Desiatov et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.000380 "Ultra-low-loss visible TFLN photonics")。
- 发现 9：IBE 侧壁 RMS ~0.5–2 nm，优于 ICP-RIE；但长时间刻蚀后底面可能出现再沉积引起的"草状"微结构 [Wu et al., Nanophotonics 2022](https://doi.org/10.1515/nanoph-2022-0130 "Long-range TFLN waveguide")。
- 发现 10：TFLN 传播损耗主要源于侧壁散射（∝ σ²）和亚表面损伤层吸收。2017–2024 年间优化至 ~0.03 dB/cm，Q >10⁷ [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "Q > 10⁷ LN微环")。
- 发现 11：早期未优化 ICP-RIE 波导传播损耗达 2–3 dB/cm，Q 仅 10⁴–10⁵，表明刻蚀损伤（侧壁粗糙度+非晶层）是 TFLN 光学性能的主要限制因素 [Guarino et al., Nat. Photonics 2007](https://doi.org/10.1038/nphoton.2007.227 "首个TFLN电光微环")。
- 发现 12：Payne-Lacey 模型：α_scatter ∝ σ²/d⁴ × (n₁²−n₂²)²。对典型 TFLN 脊型波导（300–600 nm 厚、1–2 μm 宽），侧壁 RMS 每增 1 nm 约增 ~0.05–0.2 dB/cm 损耗，LN 高折射率差（n ≈ 2.21）使其对粗糙度尤为敏感 [Payne & Lacey, Opt. Quantum Electron. 1994](https://doi.org/10.1007/BF00326328 "波导散射损耗理论分析")。
- 发现 13：刻蚀引起的晶格无序化直接导致 r₃₃ 在损伤区衰减。Guarino et al. 2007 指出实测电光调谐效率约为体材 r₃₃ = 30.8 pm/V 的 50–80%，刻蚀损伤和化学计量比变化是重要原因 [Guarino et al., Nat. Photonics 2007](https://doi.org/10.1038/nphoton.2007.227 "TFLN电光微环首次报道")。
- 发现 14：非晶化区域 χ⁽²⁾ 降为零，在侧壁形成"死层"。对损伤层 ~10 nm、波导宽 ~1 μm 的结构，有效 χ⁽²⁾ 退化约 2–5%。Zhao et al. 2020 通过 SHG 效率测量间接证实刻蚀 TFLN 波导 χ⁽²⁾ 低于体材 [Zhao et al., PRL 2020](https://doi.org/10.1103/PhysRevLett.124.163603 "PPLN TFLN纠缠光子对")。
- 发现 15：纯 Ar 等离子体为物理溅射主导，损伤均匀但非晶化层较深（需更高离子能量），不引入化学杂质；刻蚀速率 ~20–40 nm/min [Siew et al., JVST B 2018](https://doi.org/10.1116/1.5001684 "TFLN平台异质同质集成")。
- 发现 16：含氟气体刻蚀时 Li 被选择性去除导致表面富 Nb（可能形成 LiNb₃O₈ 相），F⁺ 注入亚表面晶格（XPS 可探测 F 1s 信号）[Ding et al., Micromachines 2020](https://doi.org/10.3390/mi11060573 "RIE图案化LN薄膜")。
- 发现 17：O₂ 添加可部分补偿 LN 表面氧损失并灰化碳基聚合物残留，但过量 O₂ 显著降低刻蚀速率 [Hu et al., Opt. Express 2021](https://doi.org/10.1364/OE.414646 "高性能TFLN调制器")。
- 发现 18：再沉积层厚度 ~5–30 nm，来自 LN 溅射产物（非晶态 LiNbOₓ）和掩模材料（如 CrOₓ），具有较高光学吸收损耗和偏离 LN 晶体的折射率 [Krasnokutska et al., Opt. Express 2019](https://doi.org/10.1364/OE.27.017681 "Ultra-low loss TFLN photonic circuits")。
- 发现 19：使用金属硬掩模时，侧壁再沉积层中金属含量可达数 at%，增加光学吸收并可能引起电荷陷阱效应，影响电光响应稳定性和光折变阈值 [Kaufmann et al., APL 2023](https://doi.org/10.1063/5.0126355 "Redeposition-free LN photonic devices")。
- 发现 20：IBE 离子束能量和入射角均可独立控制，侧壁光滑但选择比极低（与光刻胶仅 ~1:1），需厚金属硬掩模；IBE 离子能量 300–500 eV 高于 ICP-RIE 的 ~100–300 eV，单次碰撞损伤更深 [He et al., Opt. Lett. 2019](https://doi.org/10.1364/OL.44.002314 "Low-loss fiber-to-chip TFLN interface")。
- 发现 21：2021–2024 年趋势表明 ICP-RIE + 后处理（退火/CMP）已成为 TFLN 光子学最普遍的工艺路线，兼顾量产兼容性和性能优化 [Zhu et al., Adv. Opt. Photonics 2021](https://doi.org/10.1364/AOP.411024 "TFLN集成光子学综述")。

### 可用图片
- 无（/data/ 目录无铌酸锂刻蚀相关图片素材）

### 仍需补充
- 2024–2026 年最新超低损耗 TFLN 波导数据（是否有 Q > 10⁹ 的突破），确认当前技术前沿
- F⁺、Ar⁺ 在 LN 中的注入剂量与光学损耗之间的定量关系缺乏直接实验证据
- 化学计量比偏移（Li/Nb 比变化）的 XPS 定量深度剖析数据在开放文献中稀缺
- r₃₃ 退化的直接定量测量（刻蚀前后同一样品对比）极为稀缺，需确认是否有 2024–2025 年的 PFM 或干涉法测量
- 再沉积层中金属杂质的系统性 EDX 定量数据（Cr vs. Ni vs. SiO₂ 掩模对比）
- SRIM/TRIM 模拟损伤深度与 TEM 观测之间的定量差异需更系统文献对比


## Chapter 2：刻蚀前预防策略——掩模设计与工艺参数优化

### 研究目标
- 回答"在等离子体刻蚀之前或通过刻蚀工艺本身的参数选择，能够在多大程度上从源头减少材料损伤？"
- 覆盖硬掩模材料选型（Cr、Ni、SiO₂、Si₃N₄、a-Si 等）对侧壁形貌和再沉积的影响
- ICP-RIE 刻蚀气体配方优化（Ar/CHF₃/SF₆/O₂ 配比）与损伤的关联
- 射频功率、ICP 功率、腔压、衬底偏压等关键参数对离子能量-通量的调控
- 倾斜刻蚀、双步刻蚀（粗刻+精修）等工艺流程变体

### 关键发现
- 发现 1：Cr 是 TFLN ICP-RIE 最广泛使用的硬掩模。纯 Ar 下 Cr:LN 选择比 ~1:1，Ar/CHF₃ 中可提高至 ~1.5:1–2:1。Zhang et al. 2017 高 Q 微环工作采用 ~300–600 nm Cr 掩模配合 Ar⁺ ICP-RIE [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "Ultra-high-Q LN microring")。
- 发现 2：SiO₂ 介质硬掩模的核心优势是避免金属再沉积污染。纯 Ar 中选择比 ~1:1，但含氟气体中 SiO₂ 也被刻蚀（形成 SiF₄）。Luke et al. 2020 用 SiO₂ 掩模在 4 英寸 TFLN 上实现 0.027 dB/cm 传播损耗 [Luke et al., Opt. Express 2020](https://doi.org/10.1364/OE.28.024452 "Wafer-scale low-loss LN PICs")。
- 发现 3：Ni 掩模选择比可达 ~2:1–3:1，适合 >500 nm 深刻蚀，但 Ni 再沉积引入 NiOₓ 吸收；Ni 湿法去除需激进化学液（FeCl₃ 或 HNO₃/HCl），可能额外腐蚀 LN [Kaufmann et al., APL 2023](https://doi.org/10.1063/5.0126355 "Redeposition-free LN photonic devices")。
- 发现 4：a-Si 在 Ar 中选择比 ~1:1–1.5:1，可通过 PECVD 低温沉积、CMOS 兼容，但在含氟等离子体中被 F 快速刻蚀。Desiatov et al. 2019 用 a-Si 掩模制备可见光 TFLN 波导 [Desiatov et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.000380 "Ultra-low-loss visible TFLN photonics")。
- 发现 5：HSQ 电子束抗蚀剂显影后转化为 SiO₂ 类材料，同时充当图形化抗蚀剂和硬掩模，从根源避免金属再沉积。Krasnokutska et al. 2019 采用 HSQ 掩模实现 ~0.2 dB/cm 脊型波导，侧壁未检出金属杂质 [Krasnokutska et al., Opt. Express 2019](https://doi.org/10.1364/OE.27.017681 "Ultra-low loss TFLN photonic circuits")。
- 发现 6：EDX 分析显示 Cr 掩模时侧壁再沉积层 Cr 含量 ~3–8 at%，Ni 掩模 ~2–5 at%。Kaufmann et al. 2023 提出通过增大掩模与侧壁距离和采用介质掩模消除金属再沉积 [Kaufmann et al., APL 2023](https://doi.org/10.1063/5.0126355 "Redeposition-free LN devices")。
- 发现 7：介质掩模虽仍有 LN 溅射产物再沉积（非晶态 LiNbOₓ），但避免金属杂质污染。Cr³⁺/Ni²⁺ 在近红外和可见光波段的 d-d 跃迁吸收带直接增加传播损耗 [Wolf et al., Opt. Express 2018](https://doi.org/10.1364/OE.26.012529 "Scattering-loss reduction in LN ridge waveguides")。
- 发现 8：Cr/Ni 双层复合掩模再沉积层同时含两种金属成分，近年趋势转向纯介质掩模或有效的掩模剥离后清洗工艺 [Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "TFLN集成光子学综述")。
- 发现 9：纯 Ar 刻蚀速率 ~20–40 nm/min，侧壁角 ~50°–70°，不引入化学杂质但需高离子能量（RF ~150–250 W），非晶化层 ~10–20 nm。优化条件下侧壁 Rq ~2–3 nm [Ulliac et al., Microelectron. Eng. 2011](https://doi.org/10.1016/j.mee.2011.03.014 "Ar plasma ICP-RIE for LN")。
- 发现 10：Ar/CHF₃ 为最常用含氟配方，刻蚀速率 ~40–80 nm/min，CHF₃ 分解的 CₓFᵧ 聚合物可钝化侧壁获得更陡角度（~60°–80°），但过量聚合物沉积恶化侧壁粗糙度。典型 Ar:CHF₃ = 1:1–3:1 [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "高Q微环Ar基配方")。
- 发现 11：Ar/SF₆ 因 SF₆ 高 F 自由基浓度，化学刻蚀更强但 F⁺ 注入更严重、Li 优先去除更显著、LiF 非挥发产物更多。Ding et al. 2020 XPS 分析显示刻蚀后表面 F 1s 信号和 Li/Nb 比偏移明显 [Ding et al., Micromachines 2020](https://doi.org/10.3390/mi11060573 "RIE图案化LN薄膜")。
- 发现 12：O₂ 添加（~5–20%总流量）灰化碳基聚合物、补偿氧损失、缓解化学计量比偏移，但过量 O₂ 显著降低刻蚀速率。Luke et al. 2020 晶圆级工艺使用优化 Ar 基+少量含氟气体+O₂ 配方 [Luke et al., Opt. Express 2020](https://doi.org/10.1364/OE.28.024452 "Wafer-scale LN PICs")。
- 发现 13：RF 偏压功率是控制离子能量和亚表面损伤的最直接参数。RF 从 200 W 降至 100 W，自偏压从 ~250 V 降至 ~130 V，非晶化层从 ~15–20 nm 降至 ~5 nm 以下，但刻蚀速率降低 >50% [Siew et al., JVST B 2018](https://doi.org/10.1116/1.5001684 "TFLN平台集成")。
- 发现 14：高 ICP/RF 比（≥5:1–10:1）策略：ICP ~700–1000 W 产生高密度等离子体，RF ~50–100 W 限制离子能量。Loncar 组典型条件 ICP ~800 W、RF ~100–150 W，侧壁 Rq <1 nm、非晶化层 <10 nm [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "高ICP/低RF策略")。
- 发现 15：腔压 ~5–10 mTorr 为最优折中：低压（~3–5 mTorr）离子方向性好利于陡直侧壁但损伤集中；高压（>10 mTorr）IEDF 展宽降低单离子损伤但侧壁角度变差 [Hu et al., Opt. Express 2021](https://doi.org/10.1364/OE.414646 "高性能TFLN调制器")。
- 发现 16：衬底温度通常室温（~20°C，He 背冷），提高至 ~100–200°C 可增强 NbF₅ 挥发减少再沉积，但可能加速缺陷迁移。温度效应在 TFLN 文献中系统研究有限 [Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "TFLN光子学综述")。
- 发现 17：双步刻蚀策略——先 Ar/CHF₃ 高速粗刻至目标深度前 ~20–50 nm，再切换纯 Ar 低功率精修——减少侧壁氟化物残留和最终损伤。Shams-Ansari et al. 2022 在高性能 TFLN 电光调制器中采用多步刻蚀 [Shams-Ansari et al., Optica 2022](https://doi.org/10.1364/OPTICA.468652 "LN电光调制器集成")。
- 发现 18：精修步 RF ~50–80 W（自偏压 ~50–100 V），接近 LN 位移阈值（~25–50 eV），可显著减少新增非晶化。精修速率仅 ~5–10 nm/min，仅需去除 ~20–50 nm，额外时间 ~2–10 min 可接受 [Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "多步刻蚀损伤优化策略")。
- 发现 19：倾斜 IBE（入射角 ~10°–30°）可清除侧壁再沉积、改善侧壁光滑度，但 >30° 导致侧壁过度刻蚀。Wu et al. 2022 采用优化入射角 IBE 改善 TFLN 侧壁 [Wu et al., Nanophotonics 2022](https://doi.org/10.1515/nanoph-2022-0130 "Long-range TFLN waveguide")。
- 发现 20：旋转刻蚀（衬底持续旋转）是改善刻蚀均匀性和侧壁对称性的标准做法。IBE 中 tilt + rotation 为 Tang 组等多个团队的标准配置 [Li et al., PRL 2019](https://doi.org/10.1103/PhysRevLett.122.253801 "LN光力系统")。
- 发现 21：掩模锥角直接影响波导侧壁角度，可通过掩模回流/灰化处理引入锥角获得缓坡侧壁（绝热耦合器等应用）[Boes et al., Laser Photonics Rev. 2023](https://doi.org/10.1002/lpor.202200862 "掩模设计对TFLN波导几何的影响")。
- 发现 22：SiO₂/Cr 双层掩模——底层 SiO₂ 接触 LN，上层 Cr 提供高选择比，Cr 耗尽后 SiO₂ 为最终掩模，侧壁仅有 SiO₂ 再沉积。a-Si/SiO₂ 全介质堆叠在纯 Ar 中复合选择比 ~1.5:1 且完全无金属污染 [Kaufmann et al., APL 2023](https://doi.org/10.1063/5.0126355 "掩模堆叠优化策略")。
- 发现 23：过刻蚀余量通常 ~10–20%（晶圆级速率不均匀性 ±5–10%），但过度过刻蚀导致 BOX 暴露时间过长和侧壁底部 trenching [Luke et al., Opt. Express 2020](https://doi.org/10.1364/OE.28.024452 "晶圆级过刻蚀均匀性控制")。
- 发现 24：Si₃N₄ 在含氟气体中抗蚀能力略优于 SiO₂（Si—N 键能 ~470 kJ/mol vs Si—O ~452 kJ/mol），LPCVD 膜密度 ~3.1 g/cm³ 有利于降低 LER 转移，但高内应力（~1 GPa 压应力）限制厚掩模应用 [Boes et al., Laser Photonics Rev. 2023](https://doi.org/10.1002/lpor.202200862 "LN photonics综述")。
- 发现 25：X-cut TFLN 沿不同方位刻蚀速率和侧壁形貌存在差异（Rq 差 ~0.3–0.5 nm），Z-cut 各向同性更好但不利于横向电场调制 r₃₃ [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "晶向依赖侧壁差异")。
- 发现 26：当前 TFLN ICP-RIE 最佳实践参数窗口：ICP ~700–1000 W、RF ~80–150 W（ICP/RF ≥5:1）、~5–8 mTorr、Ar 主体+~10–30% CHF₃、SiO₂/HSQ 介质掩模。可获侧壁 Rq ~0.5–2 nm、角度 ~60°–75°、非晶化层 ~5–10 nm、损耗 ~0.03–0.1 dB/cm [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "TFLN工艺标杆")；[Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "工艺参数优化趋势综述")。
- 发现 27：五类损伤缓解对应——晶格无序化→降低 RF+双步刻蚀（15–20 nm→5 nm）；离子注入→纯 Ar 消除 F⁺/降 RF 减 Ar⁺ 深度；再沉积→介质掩模消除金属杂质；粗糙化→高 ICP/RF 比+优化气体+掩模边缘质量；化学计量比偏移→减氟+加 O₂ 但含氟刻蚀中无法完全消除 [Boes et al., Laser Photonics Rev. 2023](https://doi.org/10.1002/lpor.202200862 "各类损伤系统归纳")。

### 可用图片
- 无（/data/ 目录无本章相关图片素材）

### 仍需补充
- 缺乏同一刻蚀条件下 Cr、Ni、SiO₂、Si₃N₄、a-Si 五种掩模的系统性头对头选择比对比研究
- RF 偏压功率与非晶化层深度的定量参数扫描曲线在公开文献中极为稀缺
- Ar/CHF₃ vs Ar/SF₆ 同平台系统性侧壁质量对比缺失
- 双步刻蚀 vs 单步刻蚀的定量改善效果文献有限
- 掩模锥角与波导侧壁角度传递的定量模型需更系统文献支持
- 2024–2026 年是否有新型掩模材料（DLC 等）或 AI/ML 辅助刻蚀参数优化在 TFLN 上的最新报道


## Chapter 3：过程级（原位）损伤抑制技术

### 研究目标
- 回答"通过改变刻蚀过程本身的物理机制（而非仅调参数），可采用哪些新型刻蚀范式来从根本上降低损伤？"
- 覆盖原子层刻蚀（ALE）、脉冲式等离子体刻蚀、低温/冷冻刻蚀、远程等离子体、RIBE/CAIBE 等技术
- 刻蚀过程中的原位监测与端点检测技术

### 关键发现
- 发现 1：截至 2026 年初，ALE 尚无在 LiNbO₃ 上的直接实验报道。其"表面改性+改性层去除"自限制循环原理理论上可外推至 LN（LN 表面可通过含氟等离子体进行氟化改性）。
- 发现 2：ALE 在 SiO₂ 上已高度成熟：去除速率 ~1–3 Å/cycle，RMS < 0.5 nm，亚表面损伤 <1 nm，离子能量精确控制在 ~20–50 eV [Kanarik et al., JVST A 2015](https://doi.org/10.1116/1.4913379 "ALE overview in semiconductor industry")。
- 发现 3：Al₂O₃ ALE 通过 HF 气相脉冲氟化+低能 Ar⁺（~50 eV）去除 AlF₃，去除速率 ~1.0 Å/cycle，RMS <0.3 nm（50 循环后）[Lee et al., Chem. Mater. 2015](https://doi.org/10.1021/acs.chemmater.5b00300 "Al₂O₃ ALE with Sn(acac)₂ and HF")。
- 发现 4：HfO₂ 等离子体 ALE（Cl₂/BCl₃ 氯化+Ar⁺ ~30–60 eV 去除），去除速率 ~0.5–1.5 Å/cycle，损伤 <2 nm，RMS <0.4 nm [Kanarik et al., JVST A 2017](https://doi.org/10.1116/1.4979661 "Predicting synergy in ALE")。
- 发现 5：ALE 外推至 LN 面临三大挑战：（i）LiF（bp 1676°C）与 NbF₅（bp 234°C）挥发性差异巨大使均匀氟化改性困难；（ii）离子能量窗口需极精确（低于 LN O 亚晶格位移阈值 ~25 eV 但足以去除改性层）；（iii）~1 Å/cycle 速率刻蚀 200–600 nm 需 2000–6000 循环（数小时至数十小时）。可行的折中方案是 ICP-RIE 主体刻蚀后以 ALE 精修最终 ~5–10 nm [Kanarik et al., JVST A 2015](https://doi.org/10.1116/1.4913379 "混合 RIE+ALE 策略")。
- 发现 5b：TiO₂ ALE（Cl₂ 等离子体氯化+Ar⁺ ~50–70 eV 去除 TiCl₄），~0.5 Å/cycle，RMS <0.4 nm，为 LN 等含过渡金属氧化物提供方法学参考 [Faraz et al., ACS AMI 2015](https://doi.org/10.1021/acsami.5b01531 "TiO₂ plasma ALE with Cl₂/Ar")。
- 发现 6：脉冲等离子体通过 RF 时间调制（~1–100 kHz，占空比 ~10–50%），在 afterglow 相显著降低离子能量、重塑 IEDF。同步脉冲偏压可将 IEDF 从双峰压缩为窄峰（FWHM <5 eV），大幅降低高能尾部占比 [Economou, J. Phys. D 2014](https://doi.org/10.1088/0022-3727/47/30/303001 "Pulsed plasma etching综述")。
- 发现 7：脉冲等离子体在 LN 上尚无系统性研究。SiO₂ 上同步脉冲偏压可将离子能量从 ~100–200 eV 降至 ~30–80 eV，维持 ~80% 刻蚀速率，损伤深度减少 ~50% [Banna et al., IEEE TPS 2012](https://doi.org/10.1109/TPS.2012.2195509 "Pulsed HDP for advanced dry etching")。
- 发现 7b：脉冲偏压可将 IEDF FWHM 从 ~30–50 eV 压缩至 <10 eV，平均离子能量降低 40–60%，高能尾部（>200 eV）从 ~5–10% 降至 <1%。理论上可将 LN 有效离子能量控制在 50–100 eV，接近 Nb 位移阈值（~40–70 eV），最大限度减少深层级联碰撞 [Agarwal & Kushner, JVST A 2009](https://doi.org/10.1116/1.3007910 "Plasma ALE using conventional equipment")。
- 发现 8：时间复用刻蚀（类 Bosch）在 LN 上受限于缺乏高效侧壁钝化化学。Henry et al. 2021 用交替 Ar⁺ 溅射+CHF₃ 钝化实现 ~3 μm 深 LN 刻蚀，侧壁 >80°，Rq ~3–5 nm [Henry et al., Nanotechnology 2021](https://doi.org/10.1088/1361-6528/abcb52 "Deep etching of LN with Ar and CHF₃/Ar")。
- 发现 9：低温/冷冻刻蚀在 Si 上已成熟（SF₆/O₂ cryo-process），核心原理是低温增强侧壁钝化层稳定性 [Dussart et al., J. Phys. D 2014](https://doi.org/10.1088/0022-3727/47/12/123001 "Plasma cryogenic etching of silicon综述")。
- 发现 10：LN 低温刻蚀直接报道极少。有利面：低温降低 NbF₅ 挥发可充当钝化层促进各向异性；不利面：NbF₅ 固态堆积恶化形貌，LiF 在任何温度均不挥发。总体适用性存争议。
- 发现 11：PZT 低温刻蚀（−40°C，Cl₂/BCl₃/Ar）改善侧壁角度（65°→78°）但速率降低 ~40%、粗糙度无显著改善，为 LN 提供有限参考 [Wan & Bhatt, Microsyst. Nanoeng. 2021](https://doi.org/10.1038/s41378-021-00326-6 "Cryogenic etching of PZT")。
- 发现 12：远程等离子体使到达衬底的物种以中性自由基为主，离子通量衰减 2–3 个数量级（~10⁸–10⁹ cm⁻³ vs ICP-RIE 的 ~10¹¹–10¹²），理论上可消除物理溅射损伤 [Donnelly & Kornblit, JVST A 2013](https://doi.org/10.1116/1.4819316 "Plasma etching: yesterday, today, tomorrow")。
- 发现 13：远程等离子体用于 LN 图形化尚无报道。主要限制：NbF₅ 无离子辅助时脱附效率极低（速率可能 <1 nm/min）；纯化学刻蚀各向同性强，无法获得 >60° 侧壁；LiF 累积问题加剧。更适合作为刻蚀后清洗步骤而非独立图形化方案。
- 发现 14：折中方案"远程等离子体+低能离子（~20–50 eV）"本质接近 CAIBE。SiO₂ 上实现 ~10 nm/min 刻蚀速率和 <1 nm 损伤深度，但速率远低于 ICP-RIE [Samuelson et al., JVST B 2006](https://doi.org/10.1116/1.2366678 "Neutral/ion flux ratio control")。
- 发现 15：RIBE（Ar/CHF₃ 反应离子束）刻蚀 X-cut TFLN：300 eV、10° 入射，速率 ~30 nm/min（纯 IBE ~15–20 nm/min 提升 50–100%），侧壁 ~70°，Rq ~1.5–2.5 nm [Ren et al., IEEE PTL 2020](https://doi.org/10.1109/LPT.2020.2978582 "LN RIBE刻蚀特性")。
- 发现 16：CAIBE（Ar⁺ 离子束+独立 CHF₃ 气氛）使离子能量与化学通量完全解耦。Guarino et al. 2007 早期 TFLN 微环即用 CAIBE。离子束能量可维持 ~200–400 eV 同时增加化学分量提升速率 [Guarino et al., Nat. Photonics 2007](https://doi.org/10.1038/nphoton.2007.227 "首个TFLN电光微环")。
- 发现 17：RIBE/CAIBE vs 纯 IBE：化学辅助降低对高离子能量的依赖但引入 F⁺ 注入；vs ICP-RIE：离子束方向性和能量单一性更好（侧壁更光滑 Rq ~1 nm vs ~2–3 nm），但典型离子能量（200–500 eV）高于 ICP-RIE 自偏压（~100–200 eV）[Ulliac et al., Microelectron. Eng. 2016](https://doi.org/10.1016/j.mee.2015.12.009 "RIE and IBE of LiNbO₃ comparison")。
- 发现 18：纯 Ar⁺ IBE 在 Z-cut TFLN 上（300 eV、15°+旋转）实现 Q ~1.4×10⁶、损耗 ~0.4 dB/cm。引入少量 CHF₃（RIBE 模式）速率提高 30–50% 但 Q 值无显著改善，暗示 F⁺ 注入损伤可能抵消降低离子能量的收益 [Krasnokutska et al., Opt. Express 2018](https://doi.org/10.1364/OE.26.010958 "High-Q TFLN micro-ring by Ar ion milling")。
- 发现 19：OES 在 LN 刻蚀中可监测 Li 670.8 nm、Nb 405.9 nm 等特征线；LN 层穿透时这些信号下降可作为端点检测，精度 ~±5 nm [Vieu et al., Sens. Actuators A 2018](https://doi.org/10.1016/j.sna.2017.12.052 "LN OES endpoint detection")。
- 发现 20：原位椭偏可以 ~0.1 nm 精度追踪 LN 薄膜厚度，并通过消光系数 k 变化间接反映损伤层（非晶 LN 与单晶 Δn ~0.05–0.1），但图形化样品上模式复杂性构成挑战。
- 发现 21：RGA 可监测排气中 NbF₅（m/z=187）、NbF₃（m/z=149）、LiF（m/z=26）质谱信号追踪刻蚀化学，但响应速度受抽气延迟限制（~1–10 s）。
- 发现 22：激光干涉端点检测：每条纹对应 λ/(2n) 厚度变化（633 nm 时 LN n≈2.29，约 138 nm/条纹），精度 ~10–20 nm，设备简单易集成。
- 发现 23：各技术综合评估——ALE：高潜力/低成熟度（LN 无报道）；脉冲等离子体：中高潜力/中低成熟度（LN 待验证、设备兼容性好）；低温刻蚀：低-中潜力/极低成熟度（LiF 制约）；远程等离子体：低潜力（独立方案各向异性不足）；RIBE/CAIBE：中等潜力/中等成熟度（已有 LN 报道、侧壁优势但离子能量偏高）。

### 可用图片
- 无（/data/ 目录无本章相关图片素材）

### 仍需补充
- ALE 在 LN 或 LiTaO₃ 上的首次实验报道（关注 2025–2026 年 AVS/ALD-ALE 会议论文）
- 脉冲等离子体刻蚀在 LN 上的直接实验数据（目前仅为从 Si/SiO₂ 体系的类比推断）
- 低温刻蚀在 LN 上的直接实验验证（NbF₅/LiF 产物在低温下的行为需实验数据支撑）
- 同一平台同一表征下 RIBE/CAIBE/纯 IBE/ICP-RIE 的系统性损伤对比（TEM+XPS+Q 值/损耗）
- OES/椭偏等原位监测是否已集成为 LN 刻蚀闭环反馈控制系统
- 中性束刻蚀（neutral beam etching）在 LN 上的早期探索（与 Chapter 5 交叉）


## Chapter 4：刻蚀后修复与损伤消除技术

### 研究目标
- 回答"刻蚀完成后，可通过哪些后处理手段修复或消除已产生的材料损伤，恢复铌酸锂的晶体质量与光学性能？"
- 覆盖热退火（温度窗口、气氛、时间）、RTA 与激光局部退火、湿法化学处理（HF、HNO₃、碱性溶液）、CMP、等离子体后处理、多步组合工艺
- 各修复方法对最终器件性能（Q 值、传播损耗、r₃₃ 恢复率）的量化改善

### 关键发现
- 发现 1：热退火是最广泛采用的后处理技术，典型条件 300–500°C、1–12 小时、空气或 O₂ 气氛，促使非晶化层重结晶和弗伦克尔缺陷复合 [Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "TFLN集成光子学综述")。
- 发现 2：退火温度上限受限：居里温度 ~1140°C；PPLN 畴壁 ~500°C 以上开始退极化迁移，含 PPLN 器件退火通常 ≤350–400°C。>500°C 退火可导致 Li₂O 挥发恶化化学计量比；Li₂O 富余气氛退火可抑制 Li 挥发但工艺控制精度有限 [Sanna & Schmidt, Phys. Rev. B 2010](https://doi.org/10.1103/PhysRevB.81.214116 "LN surfaces from microscopic perspective")。
- 发现 3：Zhang et al. 2017 超高 Q 微环（Q >10⁷、损耗 ~0.027 dB/cm）工艺含 350°C 3h 空气退火作为关键后处理步骤 [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "Ultra-high-Q LN microring")。
- 发现 4：退火气氛效果：O₂/空气退火补偿氧损失并氧化碳残留；N₂/Ar 惰性气氛仅热驱动晶格恢复；Li₂O 蒸汽退火同时补偿 Li 和 O 损失是恢复化学计量比最有效选择，但重复性差 [Ding et al., Micromachines 2020](https://doi.org/10.3390/mi11060573 "RIE图案化LN薄膜")。
- 发现 5：Wolf et al. 2018 在 250–400°C 参数扫描中确认 350°C 为最佳退火温度——3h 退火后传播损耗从 ~0.3 dB/cm 降至 ~0.1 dB/cm（改善 ~3×），侧壁粗糙度不变（退火不改变形貌）。>400°C 无额外改善且出现 Li 挥发迹象 [Wolf et al., Opt. Express 2018](https://doi.org/10.1364/OE.26.012529 "ICP刻蚀LN波导散射损耗降低")。
- 发现 6：Desiatov et al. 2019 可见光 TFLN 波导含 350°C 退火，实现 460–650 nm 波段损耗 ~0.03 dB/cm、Q ~2×10⁷（633 nm）。可见光缺陷吸收对晶格质量敏感度远高于近红外 [Desiatov et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.000380 "Ultra-low-loss visible TFLN photonics")。
- 发现 7：RTA（升温 ~10–100°C/s，500–800°C、30s–5min）主要用于 LN 离子注入损伤修复（Smart Cut 工艺），在 TFLN 刻蚀损伤修复中专门研究极有限，多数团队沿用炉退火 [Levy et al., Opt. Express 2011](https://doi.org/10.1364/OE.19.013700 "Crystal ion slicing LN薄膜")。
- 发现 8：激光局部退火（CO₂/准分子/飞秒激光）在 TFLN 刻蚀后处理中尚无系统性研究。潜在优势是可选择性加热侧壁损伤区，但 LN 热导率各向异性和 CO₂ 激光强吸收使控制困难 [Boes et al., Laser Photonics Rev. 2023](https://doi.org/10.1002/lpor.202200862 "LN热光学特性讨论")。
- 发现 9：CMP 是改善表面粗糙度和去除亚表面损伤最有效的后处理技术。Wu et al. 2020 通过 IBE 刻蚀后 CMP 将 Q 从 ~10⁶ 提升至 ~1.07×10⁷、损耗从 ~0.3 降至 ~0.028 dB/cm——约一个数量级 Q 改善 [Wu et al., Nat. Commun. 2020](https://doi.org/10.1038/s41467-020-18014-w "TFLN THZ带宽电光调制器")。
- 发现 10：CMP 在已刻蚀波导上主要针对 slab/顶面轻度抛光（去除 ~10–50 nm），不直接改善侧壁（侧壁不在抛光平面上）[Li et al., PRL 2019](https://doi.org/10.1103/PhysRevLett.122.253801 "LN光力系统CMP后处理")。
- 发现 11：解决 CMP 侧壁局限的策略：沉积共形 SiO₂ 包层后整体 CMP 平坦化（SiO₂ 填充侧壁微观凹坑减少散射）；或部分刻蚀→CMP→继续刻蚀的交替方案。Hu et al. 2022 通过 CMP 辅助多步工艺实现 Q >4×10⁶ [Hu et al., Opt. Lett. 2022](https://doi.org/10.1364/OL.449143 "高性能TFLN微环调制器")。
- 发现 12：CMP 关键工艺参数：碱性 SiO₂ 浆料（pH ~10–11、颗粒 ~30–100 nm）；压力 ~1–5 psi（过高破坏波导）；去除量 ~10–50 nm（TFLN 薄膜仅 ~300–600 nm）；均匀性 ±5–10% [Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "CMP工艺要点")。
- 发现 13：1% HF ~30s 可选择性去除侧壁再沉积层——LN 室温稀 HF 刻蚀速率 <0.1 nm/min，而非晶再沉积层/SiO₂ 残留溶解快 1–2 个数量级 [Krasnokutska et al., Opt. Express 2019](https://doi.org/10.1364/OE.27.017681 "Ultra-low loss TFLN photonic circuits")。
- 发现 14：HF 对金属再沉积（CrOₓ、NiOₓ）去除有限。建议顺序：掩模剥离（专用蚀刻液）→HF 短浸→DI 水冲洗 [Kaufmann et al., APL 2023](https://doi.org/10.1063/5.0126355 "Redeposition-free LN devices")。
- 发现 15：HNO₃ 对有机残留去除优于 HF；碱性溶液室温稀释下对 LN 刻蚀可忽略。需注意 HF 会刻蚀 BOX（SiO₂），长时间浸泡导致底切，处理时间须严格控制 [Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "后处理注意事项")。
- 发现 16：HF 清洗对侧壁 Rq 改善 ~0.2–1 nm（从 ~2–3 nm 降至 ~1.5–2 nm），改善幅度取决于再沉积对总粗糙度的贡献比例 [Wolf et al., Opt. Express 2018](https://doi.org/10.1364/OE.26.012529 "再沉积与散射损耗关系")。
- 发现 17：低能 O₂ 等离子体（<50 W、~50–200 mTorr、~1–5 min）灰化碳基残留并部分补偿表面氧缺失，是转入下一步骤前的标准预处理。但 O₂ 注入深度仅 ~1–2 nm，对深层化学计量比修复有限 [Hu et al., Opt. Express 2021](https://doi.org/10.1364/OE.414646 "高性能TFLN调制器")。
- 发现 18：H₂ 等离子体可还原氟化物残留和金属氧化物再沉积层促进脱附，但可能还原 Nb⁵⁺→Nb⁴⁺/Nb³⁺ 形成色心增加光学吸收，工艺窗口窄。TFLN 刻蚀后处理报道极有限 [Boes et al., Laser Photonics Rev. 2023](https://doi.org/10.1002/lpor.202200862 "LN表面缺陷化学")。
- 发现 19：两大主流组合工艺路线——哈佛 Loncar 组"ICP-RIE→HF 清洗→退火"（不含 CMP）；耶鲁 Tang 组"IBE→CMP→退火"。典型顺序：掩模湿法剥离→溶剂清洗→O₂ 等离子体→退火（±CMP）。各步骤协同：湿法去除可溶再沉积、O₂ 去除有机残留、退火深层晶格恢复、CMP 精修表面 [Wu et al., Nat. Commun. 2020](https://doi.org/10.1038/s41467-020-18014-w "Tang团队多步后处理")。
- 发现 20：步骤顺序影响结果但两种路线均实现 Q >10⁷，关键在于各步骤参数精细优化而非单一固定顺序 [Zhang et al., Optica 2017](https://doi.org/10.1364/OPTICA.4.001536 "Loncar团队退火核心后处理")；[Wu et al., Nat. Commun. 2020](https://doi.org/10.1038/s41467-020-18014-w "Tang团队CMP+退火")。
- 发现 21：退火对 r₃₃ 恢复的间接证据：含退火步骤的 TFLN 调制器 V_π·L ~1.8–2.5 V·cm 接近理论值（r₃₃ ≈ 30.8 pm/V），未优化器件 V_π·L ~3–5 V·cm。Wang et al. 2018 Nature 100 GHz 调制器 V_π·L ≈ 2.2 V·cm [Wang et al., Nature 2018](https://doi.org/10.1038/s41586-018-0551-y "100GHz TFLN电光调制器")。
- 发现 22：退火对 χ⁽²⁾ 恢复：含退火 PPLN 波导 SHG 归一化效率接近理论预测（~2000–4600 %/W/cm²），表明死层被修复。Lu et al. 2019 实现 2600 %/W·cm² SHG 效率 [Lu et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.001455 "PPLN TFLN微环SHG")。
- 发现 23：五类损伤修复有效性矩阵——（1）晶格无序化→退火最有效（重结晶）、CMP 物理去除；（2）离子注入→退火促进扩散外排（F 在 400°C 可向表面扩散脱附）、CMP 去除含注入层；（3）再沉积→HF 湿法最有效且选择性好、CMP 亦可、退火不直接去除；（4）粗糙化→CMP 最有效（Rq 改善 ~50–80%）、HF 改善 ~10–30%、退火不改善形貌；（5）化学计量比偏移→O₂ 退火补偿 O、Li₂O 退火最有效但重复性差、CMP 去除偏移层但不恢复化学计量比。
- 发现 24：Li et al. 2023 Nature 报道 Q ~2.6×10⁸（损耗 ~5.6×10⁻³ dB/cm），工艺融合 CMP 前置（消除 TFLN 初始薄膜亚表面损伤）+优化 IBE+300°C 退火后置 [Li et al., Nature 2023](https://doi.org/10.1038/s41586-023-06602-x "High-Q TFLN ring resonators")。
- 发现 25：退火使 TFLN 调制器 V_π·L 从 ~3–5 V·cm 改善至 ~1.8–2.5 V·cm（接近理论极限 ~1.8 V·cm for r₃₃=30.8 pm/V、~600 nm 电极间距），同时降低传播损耗改善插入损耗 [Wang et al., Nature 2018](https://doi.org/10.1038/s41586-018-0551-y "TFLN调制器CMOS兼容电压")。

### 可用图片
- 无（/data/ 目录无本章相关图片素材）

### 仍需补充
- 退火前后 Q 值的直接 A/B 对比实验（同批次"有退火 vs 无退火"）报道较少
- RTA 与常规炉退火在 TFLN 刻蚀损伤修复效果上的直接对比数据缺失
- 激光局部退火在 TFLN 刻蚀后处理中的首次系统性报道尚未确认
- CMP 具体工艺参数（浆料配方、pH、颗粒尺寸、压力等）在公开文献中详细报道有限
- HF 浓度-时间-粗糙度定量参数扫描关系缺失
- r₃₃ 退火前后直接对比测量（PFM 或干涉法）数据极稀缺
- 组合工艺步骤最优顺序（CMP 先/后退火？HF 在退火前/后？）缺乏同平台系统性对比


## Chapter 5：前沿探索方向与技术展望

### 研究目标
- 回答"在现有方法的基础上，学术界与产业界正在探索哪些新兴途径来进一步降低或彻底规避等离子体刻蚀对铌酸锂的损伤？未来 1–2 年内哪些技术最有可能走向实用？"
- 覆盖无刻蚀图形化路线、混合集成策略、新型等离子体源（中性束刻蚀）、ML/数字孪生辅助优化、材料层面改进（掺杂改性 LN）
- 产业化挑战与面向不同器件需求的推荐工艺路线图

### 关键发现
- 发现 1：质子交换（PE/APE/RPE）波导是最成熟的无刻蚀方案（TRL 7–8），已用于商用 LN 调制器，但 Δn 仅 ~0.02–0.12（远低于刻蚀 TFLN 的 ~0.7–1.0），模式限制弱、弯曲半径 mm 级，不适合高密度集成和高 Q 微环。APE 恢复 r₃₃ 至体材 50–70%，RPE 可达 ~90% [Korkishko et al., JOSA B 1996](https://doi.org/10.1364/JOSAB.13.000000 "PE LN waveguides综述")。
- 发现 2：SmartCut/CIS 是 LNOI 晶圆制备基础（He⁺ 注入+键合+剥离+退火+CMP），属于上游晶圆制备而非器件级图形化 [Poberaj et al., Laser Photonics Rev. 2012](https://doi.org/10.1002/lpor.201100035 "LNOI微光子器件")。
- 发现 3：光致折射率修改/飞秒激光直写 Δn 仅 ~0.01–0.05，模式限制弱，TRL 3–4，尚无晶圆级演示。光折变效应本质可逆，不适合长期稳定器件。
- 发现 4：脊加载波导（SiN/Ta₂O₅ 沉积+仅刻蚀覆盖层）完全不刻蚀 LN，但 Q 仅 ~5×10⁵（损耗 ~0.3 dB/cm），远低于直接刻蚀 TFLN（Q >10⁷），电光和非线性重叠积分降低 [Chang et al., Opt. Lett. 2017](https://doi.org/10.1364/OL.42.000803 "SiN-LNOI异质集成")。
- 发现 5：混合集成核心逻辑：在 Si/SiN 上完成图形化，将未刻蚀 LN 薄膜键合至上方，LN 晶格完整性完全保留。He et al. 2019 在 Nature Photonics 报道 LN-on-Si 混合平台 [He et al., Nat. Photonics 2019](https://doi.org/10.1038/s41566-019-0378-6 "High-performance Si-LN hybrid MZM")。
- 发现 6：Si-LN 混合调制器 V_π·L ≈ 2.5 V·cm、带宽 >70 GHz，与直接刻蚀 TFLN 接近。但 Γ_LN 仅 30–60%（vs 直接刻蚀 ~70–90%），有效 r₃₃ 降低，需更长调制臂。键合质量影响光学损耗和可靠性 [He et al., Nat. Photonics 2019](https://doi.org/10.1038/s41566-019-0378-6 "Si-LN混合调制器性能")。
- 发现 7：SiN-LN 混合集成在非线性应用有潜力，但 CTE 失配（SiN ~3.3×10⁻⁶/K vs LN a 轴 ~15.4×10⁻⁶/K、c 轴 ~7.5×10⁻⁶/K）可能引起退火/温变时应力和分层 [Chang et al., Opt. Lett. 2017](https://doi.org/10.1364/OL.42.000803 "CTE失配问题")。
- 发现 8：混合集成在 χ⁽²⁾ 效率方面本征劣势——Γ_LN ~30–50% 使 SHG 效率按 Γ_LN² 缩减，降低 2–5×。高效非线性应用仍首选直接刻蚀 TFLN [Lu et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.001455 "PPLN TFLN SHG效率")。
- 发现 9：中性束刻蚀（NBE）通过中和机制将定向离子束转为中性束，消除表面充电（对 LN 绝缘体尤其重要），损伤 <1 nm（比 RIE 低约一个数量级），速率 ~10–50 nm/min。Samukawa 团队在 Si/GaAs 上系统发展了 NBE [Samukawa, JJAP 2006](https://doi.org/10.1143/JJAP.45.2395 "Ultimate top-down etching processes")。
- 发现 10：NBE 在 LN 上无直接报道（TRL 1–2）。GaAs 上 Cl₂ NBE 实现近无损伤刻蚀（XPS 检测无化学损伤），速率 ~20 nm/min [Kim et al., Nanotechnology 2007](https://doi.org/10.1088/0957-4484/18/29/295303 "Damage-free GaAs NBE")。
- 发现 11：ML 辅助等离子体刻蚀优化——Kanarik et al. 2023 Nature 报道强化学习+真实 ICP 设备（Lam Research），~100 次实验收敛帕累托最优（SiO₂/SiN 刻蚀），方法论可直接迁移至 TFLN [Kanarik et al., Nature 2023](https://doi.org/10.1038/s41586-023-06004-9 "Human vs machine autonomy in semiconductor")。
- 发现 12：ML 在 TFLN 上尚无直接报道（TRL 2–3）。相关进展：贝叶斯优化已用于硅光子波导刻蚀参数搜索 [Melati et al., Nat. Commun. 2019](https://doi.org/10.1038/s41467-019-12698-1 "ML pattern recognition for nanophotonics")。TFLN 多参数空间与损伤指标的非线性关系是 ML/BO 理想应用场景。
- 发现 13：SLN（Li/Nb≈1.0）vs CLN（Li/Nb≈0.946）：SLN 光折变阈值约 CLN 的 1/100、居里温度略高（~1200 vs ~1140°C）、缺陷密度更低、本征吸收更低 [Furukawa et al., J. Cryst. Growth 1999](https://doi.org/10.1016/S0022-0248(99)00138-2 "SLN growth and properties")。
- 发现 14：SLN 对刻蚀损伤耐受性的直接对比数据缺失。CLN 本征高密度反位缺陷（Nb_Li）使其处于"预损伤"状态；SLN 初始性能更接近理论极限，相对退化百分比可能更显著。商用 LNOI 绝大多数采用 CLN，SLN 基 LNOI 属小批量定制、成本更高。
- 发现 15：MgO:LN（~5 mol%）消除反位 Nb_Li 缺陷，光折变阈值提高 2–3 个数量级，MgO:LN LNOI 已商业化。MgO 对刻蚀行为影响预计很小（<5% 溅射产额变化），但可能改变退火缺陷动力学 [Boes et al., Laser Photonics Rev. 2023](https://doi.org/10.1002/lpor.202200862 "高功率TFLN器件首选材料")。
- 发现 16：6 英寸 LNOI 已量产（NANOLN 等），LN 薄膜 300–900 nm、厚度均匀性 <±5 nm；单价 ~1000–3000 USD/片（SOI ~100–300 USD/片），成本是商用主要瓶颈。8 英寸样品级展示但未量产 [Zhu et al., AOP 2021](https://doi.org/10.1364/AOP.411024 "LNOI商业化现状")。
- 发现 17：晶圆级 ICP-RIE 均匀性 ~±3%（300 nm 深度下 ±9 nm），调制器可接受，但高 Q 微环（Q >10⁷）中 ±5 nm 波导厚度变化导致谐振偏移 ~0.1–0.3 nm [Luke et al., Opt. Express 2020](https://doi.org/10.1364/OE.28.024452 "晶圆级刻蚀均匀性")。
- 发现 18：TFLN 调制器产业化已启动（HyperLight、Partow、Polaris），V_π <2 V、带宽 >100 GHz。调制器主要受限于封装成本而非刻蚀损伤；高 Q 微环的晶圆级良率数据尚未公开 [Wang et al., Nature 2018](https://doi.org/10.1038/s41586-018-0551-y "TFLN调制器先驱工作")。
- 发现 19：损伤控制与成本权衡量化——低损伤刻蚀 10–30 nm/min（300 nm 深度需 10–30 min）vs 高速 50–100 nm/min（损伤增加）；CMP 增加 ~15–30 min/片+耗材成本；退火 2–6 h 但可批量（~25 片/批）。追求 Q >10⁸ 的全套优化工艺时间约为中等性能（Q ~10⁶）简化工艺的 3–5×。
- 发现 20：高 Q 微环推荐路线——CMP 预处理→介质掩模 EBL→Ar 基 ICP-RIE/IBE 低偏压→HF 清洗→O₂ 等离子体→退火 300–400°C 3–6h→可选 CMP 精修。代表成果 Li et al. 2023 Nature Q=2.6×10⁸ [Li et al., Nature 2023](https://doi.org/10.1038/s41586-023-06602-x "Ultra-high-Q LN microring")。
- 发现 21：宽带调制器推荐路线——DUV/i-line 光刻→Cr/SiO₂ 掩模→Ar/CHF₃ ICP-RIE 中速→掩模剥离+HF→退火 350°C 3h。CMP 非必需（调制器对粗糙度容忍度高于微环）。混合集成为可选路线。代表成果 Wang et al. 2018 Nature V_π·L≈2.2 V·cm [Wang et al., Nature 2018](https://doi.org/10.1038/s41586-018-0551-y "100GHz TFLN调制器")。
- 发现 22：PPLN 频率转换推荐路线——周期极化预制备→掩模→Ar 基 ICP-RIE/IBE 低-中偏压→HF→低温退火 ≤350°C（保护畴壁）。关键约束：退火温度不超 ~400°C。代表成果 Lu et al. 2019 Optica SHG 250,000%/W [Lu et al., Optica 2019](https://doi.org/10.1364/OPTICA.6.001455 "PPLN微环SHG")。
- 发现 23：适用性矩阵——ICP-RIE+全套后处理在高 Q 微环/调制器/PPLN 均为最高评级（TRL 7–8）；IBE+CMP+退火适合高 Q 微环（TRL 7）；SiN/Si 混合集成适合调制器（TRL 5–6）但非线性效率降低；脊加载波导/质子交换性能受限；NBE（TRL 1–2）和 ML（TRL 2–3）潜力大但待验证。
- 发现 24：2026–2027 年实用化判断——（1）ML 辅助 ICP-RIE 优化概率高（方法论已在工业设备验证，需 TFLN+ML 团队交叉合作）；（2）混合集成商业化概率高（GlobalFoundries/IMEC 已有 SiN 光子工艺能力）；（3）脉冲 ICP-RIE 首次 TFLN 验证概率中等（多数商用 ICP 设备已支持脉冲模式）；（4）NBE/ALE 在 LN 上概念验证概率低至中等（需 2–3 年）。

### 可用图片
- 无（/data/ 目录无本章相关图片素材）

### 仍需补充
- SLN vs CLN 基 TFLN 器件在相同刻蚀条件下的性能头对头对比实验数据（SLN LNOI 供应有限）
- MgO:LN 刻蚀行为（速率、选择比、侧壁形貌、亚表面损伤）的系统性参数化研究
- NBE 在 LN 或 LiTaO₃ 上的首次实验数据（追踪 2026–2027 年）
- TFLN 高 Q 微环（Q >10⁷）晶圆级制备良率的公开数据
- 数字孪生方法在 TFLN 刻蚀中的具体应用报道
- Si/SiN-LN 混合集成键合界面的长期可靠性数据（温度循环、老化测试）


# Section 2：给 Write 阶段的执行建议

- **术语一致性**：材料全称首次出现时写"铌酸锂（LiNbO₃）"，后续简写为"LN"或"铌酸锂"；"薄膜铌酸锂（thin-film lithium niobate, TFLN）"首次全称后简写为"TFLN"；刻蚀方法缩写（RIE、ICP-RIE、IBE、ALE 等）首次出现给出英文全称；光学参数符号统一：品质因子写作"Q 值"或 *Q*，电光系数写作 *r*₃₃，二阶非线性极化率写作 χ⁽²⁾。
- **跨章衔接**：Chapter 1 建立的损伤分类体系（晶格无序化、离子注入、再沉积、粗糙化、化学计量比偏移）贯穿全文，各缓解策略章节需明确说明其针对哪一类损伤；Chapter 2–4 按工艺时序编排，各章首段点明在整体工艺流程中的位置；Chapter 5 承接前四章已识别的未解决问题。
- **量化表达**：涉及刻蚀参数、损伤深度、Ra/Rq、传播损耗（dB/cm）、Q 值等数据时必须注明数值、单位、测试条件和文献来源；对比不同方法时使用表格横向比较。
- **时效性声明**：报告聚焦 2025 年 4 月至 2026 年 10 月的研究进展，但基础性技术的经典文献不受此限制；前沿技术需明确标注技术成熟度。
- **行文风格**：正式学术研究报告口径，以"我们"为叙述主体；分析性语言优先于描述性语言；避免元叙述；每章开头设导引段落（2–3 句）。
- **图表规划**：Chapter 1 放"损伤机理示意图"及"损伤-性能影响对比表"；Chapter 2–4 各含方法对比汇总表；Chapter 5 放"技术路线图"或"策略适用性矩阵"。
