# Section 1：章节研究计划

## Chapter 1：非接触式感知技术总览与分类体系

### 研究目标
- 建立非接触式感知的统一定义与技术边界，明确报告所涵盖的感知模态（射频、光学、声学）及其物理原理
- 按信号模态构建分类框架（射频类：WiFi CSI / mmWave / UWB；光学类：RGB / 红外 / ToF / LiDAR；声学类：超声波 / 可听声），梳理各模态适用的典型感知任务
- 概述 2025—2026 年该领域整体技术演进趋势，包括基础模型进入感知领域、Transformer 架构主导化、跨域泛化成为核心挑战等宏观动向
- 定义本报告使用的核心评估维度：输入信号类型、感知任务类型、准确率/精度指标、评测基准、算法架构、部署约束

### 关键发现
- 非接触式感知的工作定义在近期多项顶刊综述中趋于一致：指"不要求在人体上佩戴或物理接触传感器，利用环境中已有或专设信号的传播特性变化来推断人体状态"的感知范式。Li et al.（2026）在一项涵盖 150+ 篇文献的综述中明确区分了 vision-based 和 RF-based 两大非接触路线，指出二者在隐私性、光照鲁棒性、穿透遮挡能力上存在本质互补 [非接触生命体征综述](https://www.sciencedirect.com/science/article/abs/pii/S0925231226002742 "Li et al., Neurocomputing 2026, 覆盖1975-2025的150+篇综述")
- 摄像头方案属于非接触但并非"无感"（unobtrusive）。Radwan et al.（2025）在 IEEE COMST 发表的 Wi-Fi 感知自监督学习 tutorial 中指出，Wi-Fi CSI 感知相比摄像头的核心优势包括：隐私保护（CSI 不含面部信息）、非视线穿透能力（可穿墙）、不受光照条件限制 [Wi-Fi SSL 综述](https://arxiv.org/html/2506.12052v1 "Radwan et al., IEEE COMST Vol.28, 2026")
- Wang et al.（2025）发表了目前最全面的 Wi-Fi 感知泛化性综述，系统回顾 200+ 篇论文，沿四阶段流水线（设备部署、信号预处理、特征学习、模型部署）对泛化技术进行分类 [Wi-Fi泛化性综述](https://arxiv.org/html/2503.08008v2 "Wang et al., 2025, 200+篇论文")
- Radwan et al.（2025）在 IEEE COMST（Vol.28, 2026年刊出）发表首篇聚焦 Wi-Fi 感知自监督学习的 tutorial-cum-survey，全面介绍 Wi-Fi 标准演进（802.11n 至 802.11bf/802.11be）、CSI 测量方法、预处理技术及自监督学习应用，已获 17 次引用 [Wi-Fi SSL Tutorial](https://arxiv.org/html/2506.12052v1 "Radwan et al., IEEE COMST Vol.28, 2026, 已被引17次")
- Cheraghinia et al. 在 IEEE COMST（Vol.27, 2025）发表 UWB 雷达全面综述，覆盖 UWB 雷达基础概念、标准化进程、应用场景、信号处理技术及数据集 [UWB综述](https://arxiv.org/abs/2402.05649 "Cheraghinia et al., IEEE COMST 2025, DOI: 10.1109/COMST.2024.3488173")
- Alijani et al.（2025）在 IEEE COMST（Vol.28, 2026年刊出）发表无设备可见光感知综述，已获 18 次引用 [可见光感知综述](https://ieeexplore.ieee.org/document/10904171/ "Alijani et al., IEEE COMST Vol.28, 2026, 已被引18次")
- Li et al.（2025）在 IEEE Access 发表综述"Acoustic Sensing for Contactless Health Monitoring"，提出声学非接触健康监测的统一框架 [声学感知综述](https://ieeexplore.ieee.org/document/11164293/ "Li et al., IEEE Access Vol.13, 2025")
- CSI-Bench 在 NeurIPS 2025 D&B Track 被接收，是首个大规模 in-the-wild WiFi 感知基准，涵盖 26 个室内环境、35 名用户、461 小时有效数据，任务覆盖跌倒检测、呼吸监测、室内定位和运动源识别 [CSI-Bench](https://openreview.net/forum?id=W1WJeqsxnX "Zhu et al., NeurIPS 2025 D&B Track")
- RAPTR（NeurIPS 2025 主会议）提出基于 Transformer 的毫米波雷达 3D 人体姿态估计方法，在 HIBER 数据集上关节位置误差降低 34.3%，在 MMVR 数据集上降低 76.9% [RAPTR](https://arxiv.org/abs/2511.08387 "Kato et al., NeurIPS 2025")
- WiFi CSI 工作于 2.4 GHz（波长 ~12.5 cm）和 5 GHz（波长 ~6 cm），802.11n 20 MHz 带宽下含 56 个子载波，802.11ac 80 MHz 可达 256 个子载波；空间分辨率受限于信号波长（厘米级），但通过多径效应和多普勒频移可实现亚波长级运动检测 [Wi-Fi SSL Tutorial](https://arxiv.org/html/2506.12052v1 "Radwan et al., IEEE COMST Vol.28, 2026")
- mmWave FMCW 雷达工作于 60 GHz（7 GHz 带宽）和 77 GHz（4-5 GHz 带宽），可实现 ~3 cm 距离分辨率，距离精度达 ~1 mm，角度精度在波束正面约 ±1° [TI mmWave技术报告](https://www.ti.com/lit/pdf/swra841 "Texas Instruments, SWRA841A, 2025/2026")
- UWB 脉冲雷达工作于 3.1-10.6 GHz，大带宽使距离分辨率可达 ~2 cm（7.5 GHz 带宽时），典型无设备定位精度 10-30 cm [UWB综述](https://arxiv.org/abs/2402.05649 "Cheraghinia et al., IEEE COMST 2025")
- 声学非接触感知通常利用 18-24 kHz 近超声频段，20 kHz 对应波长 ~17 mm，有效距离通常 1-5 m，可利用现有智能音箱/手机麦克风阵列实现零额外硬件成本部署 [声学感知综述](https://ieeexplore.ieee.org/document/11164293/ "Li et al., IEEE Access 2025")
- AM-FM 是首个面向 WiFi 环境智能的基础模型（2026年2月），在 920 万条未标注 CSI 样本上预训练（跨 439 天、20 种商用设备），在 9 个下游任务上展现强跨任务性能 [AM-FM](https://arxiv.org/abs/2602.11200 "Zhu et al., arXiv, Feb 2026")
- Large Wireless Model（LWM）是全球首个面向无线信道的基础模型，采用 Transformer 架构自监督预训练，LWM 1.1 版本于 2025 年发布 [LWM](https://arxiv.org/abs/2411.08872 "Alikhani et al., arXiv, Nov 2024/Apr 2025")
- NeurIPS 2025 AI4NextG Workshop 接收了面向 FMCW 雷达感知的基础模型先导研究，学习到的嵌入在存在检测任务上与 DINO 和 LWM 等预训练模型具有竞争性表现 [FMCW基础模型](https://neurips.cc/virtual/2025/123209 "Serbetci et al., NeurIPS 2025 AI4NextG Workshop")
- Transformer 架构在非接触感知领域已呈主导化趋势，Wi-Fi 感知泛化研究自 2019 年起论文爆发式增长；跨模态方面，Wi-Chat 利用 GPT-4o 实现零样本动作识别，Wi-Fringe 使用 BERT 嵌入指导 WiFi 特征学习 [Wi-Fi泛化性综述](https://arxiv.org/html/2503.08008v2 "Wang et al., 2025")
- 感知任务评测指标对应：分类任务（HAR、手势、跌倒检测）→ Accuracy/F1；回归任务（姿态估计）→ MPJPE（mm）；生命体征→ MAE/RMSE/Pearson r；定位→ 平均距离误差（m） [Wi-Fi泛化性综述](https://arxiv.org/html/2503.08008v2 "Wang et al., 2025") [Wi-Fi SSL Tutorial](https://arxiv.org/html/2506.12052v1 "Radwan et al., IEEE COMST 2026")
- 泛化性已成为 WiFi CSI 方向最核心的开放挑战，三大障碍为：设备异构性、人体多样性、环境多样性 [Wi-Fi泛化性综述](https://arxiv.org/html/2503.08008v2 "Wang et al., 2025")

### 可用图片
- 无（/data/ 目录中仅有量子化学相关的图表生成脚本，与本章无关）

### 仍需补充
- IEEE 802.11bf 标准正式文本或 Wi-Fi Alliance 官方公告——目前描述来自综述论文二手引用，需一手标准文档确认
- M4Human 大规模多模态 mmWave 基准数据集——未找到已发表的一手描述文档，需确认发表状态和规模
- mmChainPose 和 mmDEAR——几何感知时序链和点云密度增强方法未在搜索中找到已公开一手来源
- LiDAR 室内人体感知的具体点云密度参数——不同型号在特定距离下的点云密度缺少统一 T1/T2 来源
- 声学感知精确空间分辨率的实测数据——缺少不同频率下手势识别精度 vs 距离的系统性对比
- 非接触感知市场规模数据——如需引用需查找 Gartner/IDC/MarketsandMarkets 等 T2 来源


## Chapter 2：基于射频信号的感知算法

### 研究目标
- 系统评估 WiFi CSI、毫米波雷达（mmWave）、超宽带（UWB）三类射频信号上的 SOTA 算法，覆盖 HAR、HPE、手势识别、生命体征监测等核心任务
- 对比各算法在标准评测基准上的准确率/精度，列出当前最优方法及其性能数字
- 分析射频感知领域的关键技术突破，包括：基于 Transformer 的 CSI 时序建模、mmWave 点云的稀疏增强方法、域泛化/跨场景迁移方案
- 评估射频感知方法的实际部署约束：硬件成本、环境鲁棒性、隐私保护优势、多人场景可扩展性

### 关键发现
- WiFi CSI HAR 在 Widar 3.0 数据集上，WiGRUNT 采用 ResNet+空间-时间双注意力机制实现域内 99.67% 准确率，跨环境 96%、跨位置 92.6%、跨方向 93.15% [WiGRUNT](https://www.techrxiv.org/users/679475/articles/676837-wigrunt-wifi-enabled-gesture-recognition-using-dual-attention-network "Gu et al., TechRxiv 2023")
- Wi-CBR 采用跨域对比学习在 Widar 3.0 上域内 99.54%，跨环境 98.34%、跨位置 96.30%、跨方向 96.57%，在跨域场景中刷新 SOTA [Wi-CBR](https://arxiv.org/html/2506.11616v1 "arXiv:2506.11616, 2025")
- SenseFi 是首个面向 WiFi CSI 人体感知的开源基准库（PyTorch），系统评测了 MLP、CNN、LSTM、BiLSTM、CNN+GRU、Transformer 等架构，发表于 Cell Patterns（2023）[SenseFi](https://arxiv.org/abs/2207.07859 "Yang et al., Patterns 2023")
- 基于自注意力机制的 WiFi CSI HAR 方法在 UT-HAR 数据集上达到 99.41% 平均识别准确率 [IEEE Access](https://ieeexplore.ieee.org/document/10559586/ "IEEE Access Vol.12, 2024, UT-HAR 99.41%")
- GLSDA 利用 GPT-2 作为教师模型引导 WiFi 手势识别泛化，在 Widar 3.0 上域内 97.78%、跨位置 95.59%、跨方向 92.80%（均值 95.39%），相比无蒸馏基线提升 1.31%–2.88% [GLSDA](https://arxiv.org/html/2510.13390v1 "Huang et al., arXiv:2510.13390, 2025")
- AM-FM 基础模型通过瓶颈适配在 SignFi 276 类手语手势上达到 AUROC 0.999（从随机初始化的 0.564 大幅提升）[AM-FM](https://arxiv.org/html/2602.11200v1 "Hu et al., arXiv:2602.11200, Feb 2026")
- PhaseBeat 系统利用商用 WiFi CSI 相位差数据，呼吸率检测中位误差 0.25 次/分钟 [PhaseBeat](https://www.eng.auburn.edu/~szm0001/papers/PhaseBeat_ACMHealth20.pdf "Wang et al., ACM Trans. Computing for Healthcare 2020")
- WiFi CSI 心率检测方法（2024 年 Sensors 发表），通过子载波选择策略实现心率估计准确率 96.8%，中位误差 0.8 bpm [WiFi HR](https://www.mdpi.com/1424-8220/24/7/2111 "Sensors Vol.24, 2024")
- AM-FM 基础模型在 920 万条 CSI 样本上预训练，9 个下游任务 AUROC：HAR 0.923、跌倒检测 0.919、手势识别 0.999（SignFi）、定位 0.995、用户识别 0.993；相比从零训练 HAR 从 0.527 提升至 0.923，few-shot K=25 样本/类时跌倒检测达 0.822 [AM-FM](https://arxiv.org/html/2602.11200v1 "Hu et al., arXiv:2602.11200, Feb 2026")
- RadMamba（2025）面向 FMCW 雷达 HAR，采用 Mamba SSM 架构：DIAT 数据集 99.8%（仅 21.7k 参数）、CI4R 91.2%（71.4k 参数）、UoG2020 89.3%（6.7k 参数），参数量较此前 SOTA 降低 1-2 个数量级 [RadMamba](https://arxiv.org/html/2504.12039v1 "Wu et al., arXiv:2504.12039, 2025")
- RadHAR 原始基准（ACM ICDLT 2019）最佳深度学习方法准确率 92%；后续 mPCT-LSTM（2025）在三个数据集上平均达 97.26% [RadHAR](https://dl.acm.org/doi/10.1145/3349624.3356768 "Singh et al., 2019") [mPCT-LSTM](https://www.sciencedirect.com/science/article/abs/pii/S1051200425002854 "Digital Signal Processing 2025")
- RAPTR（NeurIPS 2025）采用两阶段 Transformer 解码器+伪 3D 可变形注意力进行 mmWave 3D HPE：HIBER 数据集 WALK MPJPE 22.32 cm（降低 34.3%）、MULTI MPJPE 18.99 cm（降低 42.7%）；MMVR 中心距离误差降低 76.9%；全监督下 HIBER MULTI 可达 8.93 cm [RAPTR](https://arxiv.org/html/2511.08387 "Kato et al., NeurIPS 2025")
- mmWave HPE 架构演进：CNN（RF-Pose 3D）→ HRNet 风格（HRRadarPose）→ DETR 风格查询（QRFPose）→ 两阶段 Transformer（RAPTR），输入从稀疏点云扩展到原始雷达热图 [RAPTR](https://arxiv.org/html/2511.08387 "Kato et al., NeurIPS 2025, Section 2")
- 基于 TI IWR1642BOOST（77-81 GHz）的多人生命体征监测：呼吸率准确率 97.94%、心率准确率 93.43%，可同时监测 3 人，有效距离 5 m [mmWave Vital Signs](https://arxiv.org/html/2511.21255v1 "Benny et al., arXiv, 2025")
- mmWave 雷达心率检测（Nature Scientific Reports 2024）：不同距离和角度下心率估计误差率仅 1.69%–2.61% [mmWave HR](https://www.nature.com/articles/s41598-024-77683-1 "Wang et al., Scientific Reports 2024")
- Google Research（2025）证明消费级 UWB 雷达可用于非接触心率测量：FMCW 雷达 MAE 0.85 bpm，经迁移学习的 UWB 雷达 MAE 4.1 bpm、MAPE 6.3%，满足 CTA 消费电子标准（≤5 bpm MAE, ≤10% MAPE）[Google UWB HR](https://research.google/blog/measuring-heart-rate-with-consumer-ultra-wideband-radar/ "Google Research 2025")
- 射频感知三模态互补格局：WiFi CSI 适合大覆盖/零成本粗粒度感知（空间分辨率最低）；mmWave 适合中等距离高精度 HPE 和多人场景（单模块 $15–50、功耗 1–3 W）；UWB 适合近距离高精度定位和生命体征检测（mW 功耗、已嵌入消费级芯片但有效距离 1–5 m）
- 射频感知领域 Transformer 主导化：WiFi 方向自注意力/ViT 达 UT-HAR 99.41%；mmWave HPE 方向 RAPTR 降低 MPJPE 34–77%；基础模型方向 AM-FM 6 层 Transformer 统一 9 任务骨干；Mamba SSM（RadMamba）在轻量化部署中展现竞争性能
- 域泛化为 WiFi 感知核心瓶颈，解决路线包括：大模型语义蒸馏（GLSDA 跨方向提升 2.88%）、基础模型预训练（AM-FM HAR 从 0.527→0.923）、跨域对比学习（Wi-CBR 跨域 96–98%）

### 可用图片
- 无（/data/ 目录中无 Chapter 2 相关图片资源）

### 仍需补充
- WiGRUNT 正式发表版本确认——目前引用 TechRxiv 预印本，需确认最终发表版中 99.67% 数据是否有更新
- NTU-Fi 数据集上各模型的具体 SOTA 准确率——SenseFi 涵盖 NTU-Fi-HAR 和 NTU-Fi-HumanID 但完整基准数字未读取
- WiFi CSI 生命体征 MAE/RMSE 系统性多方法对比——目前仅有 PhaseBeat 和单篇心率检测数据
- CSI-Bench（NeurIPS 2025 D&B）各子任务的 baseline 性能数字
- M4Human 数据集发表状态和规模确认
- mmDEAR 点云密度增强方法的具体性能数字
- mmChainPose 几何感知时序链在 HPE 任务上的具体 MPJPE 数字


## Chapter 3：基于视觉与光学信号的感知算法

### 研究目标
- 系统评估 RGB 相机、红外热成像、结构光/ToF 深度相机、LiDAR 等光学传感器上的 SOTA 非接触感知算法
- 重点覆盖三大任务：(1) 视觉 HAR 与姿态估计、(2) 远程光电容积脉搏波（rPPG）生命体征监测、(3) LiDAR/深度相机的人体感知
- 分析视觉方法的精度上限与固有局限（光照敏感性、遮挡问题、隐私争议），及最新的隐私保护技术路线
- 评估部署约束：计算量、实时性、对光照/距离/角度的鲁棒性

### 关键发现
- NTU RGB+D 120 骨架 HAR：DeGCN 以 Cross-Subject 91.0%、Cross-Setup 92.1% 位居榜首；InfoGCN（CVPR 2022）Cross-Subject 89.8%、Cross-Setup 91.2%；CTR-GCN（ICCV 2021）Cross-Subject 88.9%、Cross-Setup 90.6% [HyperAI SOTA 排行榜](https://hyper.ai/en/sota/tasks/skeleton-based-action-recognition/benchmark/skeleton-based-action-recognition-on-ntu-rgb-d-120 "NTU RGB+D 120 骨架 HAR 排行，截至 2026 年 4 月")
- InfoGCN（CVPR 2022）采用信息瓶颈优化骨架特征表示，NTU RGB+D 60 Cross-Subject 93.0%、Cross-View 97.1%，NTU RGB+D 120 Cross-Subject 89.8%（4 模型集成）[InfoGCN](https://openaccess.thecvf.com/content/CVPR2022/papers/Chi_InfoGCN_Representation_Learning_for_Human_Skeleton-Based_Action_Recognition_CVPR_2022_paper.pdf "Chi et al., CVPR 2022")
- 骨架 HAR 架构演进：ST-GCN（AAAI 2018, ~85%）→ CTR-GCN（ICCV 2021, 88.9%）→ InfoGCN（CVPR 2022, 89.8%）→ DeGCN（2024, 91.0%），每代提升 1–2 个百分点
- Kinetics-700 视频 HAR：InternVideo2-1B（ECCV 2024）Top-1 85.4%，K400 Top-1 92.1%；InternVideo2 采用渐进式训练（掩码视频建模+跨模态对比+下一 token 预测），参数量 1B–6B [InternVideo2](https://arxiv.org/html/2403.15377v2 "Wang et al., ECCV 2024") [HyperAI](https://hyper.ai/en/sota/tasks/action-classification/benchmark/action-classification-on-kinetics-700 "Kinetics-700 排行")
- 骨架方法 vs 视频方法互补：骨架方法在受控环境精细动作识别中 SOTA ~92%（NTU120），天然隐私保护且对光照/外观变化鲁棒；视频方法在大规模开放场景中领先（K700 85.4%），但对光照/遮挡敏感且隐私风险更高
- COCO test-dev HPE：ViTPose（ViTAE-G 集成）AP 81.1%、AP50 95.0%；单模型 ViTPose-G AP 80.9%，为 COCO HPE 首次突破 80 AP；HRNet-W48+DARK AP 77.4% [HyperAI](https://hyper.ai/en/sota/tasks/pose-estimation/benchmark/pose-estimation-on-coco-test-dev "COCO HPE 排行")
- ViTPose++（IEEE TPAMI 2024）将朴素 ViT 扩展为通用身体姿态估计框架，支持多任务（人体、手部、面部、动物），ViTPose-G ~1B 参数、ViTPose-B ~86M 参数达 75.8 AP [ViTPose++](https://arxiv.org/html/2212.04246v3 "Xu et al., IEEE TPAMI 2024")
- HPE 计算量对比：ViTPose-G（~1B 参数）用于性能上限探索；Lite-HRNet-30（~1.8M 参数）COCO AP 69.7% 适合移动端部署
- rPPG 综述（WIREs 2025）系统回顾了从传统信号处理（GREEN、ICA、CHROM、POS）到深度学习（CNN、Transformer、Mamba、Diffusion）的完整技术演进 [WIREs rPPG 综述](https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/widm.70039 "Sakib et al., WIREs Data Mining 2025")
- ME-rPPG（清华大学, 2025 年 4 月）基于时空状态空间对偶性，在 PURE MAE 0.25 bpm（R=1.00）、VitalVideo MAE 0.70 bpm（R=0.98）、MMPD MAE 5.38 bpm，相比基线方法准确率提升 21.3%–60.2%；仅 580K 参数、3.6 MB 内存、9.46 ms CPU 推理延迟 [ME-rPPG](https://arxiv.org/html/2504.01774v2 "Tang et al., arXiv:2504.01774, 2025")
- PhysFormer（CVPR 2022）首个基于 Transformer 的 rPPG 方法，VIPL-HR 数据集 MAE 2.84 bpm、RMSE 5.36 bpm、r=0.92 [PhysFormer](https://openaccess.thecvf.com/content/CVPR2022/papers/Yu_PhysFormer_Facial_Video-Based_Physiological_Measurement_With_Temporal_Difference_Transformer_CVPR_2022_paper.pdf "Yu et al., CVPR 2022")
- FrePhys（提交至 ICLR 2026）提出频率感知扩散模型用于 rPPG，将生理频率先验嵌入扩散过程，相比 PhysFormer MAE 降低 31% [FrePhys](https://openreview.net/pdf/d12d99cd9bebacd5b62faaa8c8e3685e539a0613.pdf "FrePhys, ICLR 2026 审稿中")
- rPPG 演进路线：传统信号处理（GREEN 2008、POS 2017）→ CNN（DeepPhys 2018、PhysNet 2019）→ Transformer（PhysFormer 2022）→ Mamba/SSM（ME-rPPG 2025）→ 扩散模型（FrePhys 2025–2026）；受控环境下心率 MAE <0.3 bpm，运动/多光照场景 MAE 仍为 5–6 bpm
- Georgia Tech（2025 年 3 月）在 Cell Reports Physical Science 发表超光谱脉冲热成像技术，使用 LWIR 相机通过热脉冲分析实现心率/呼吸率/体温非接触测量，可在低光/无光环境工作，多人场景有效 [Georgia Tech 热成像](https://coe.gatech.edu/news/2025/03/thermal-imaging-could-be-simple-highly-accurate-way-track-vital-signs "Han et al., Cell Reports Physical Science 2025")
- LiveHPS（CVPR 2024）是首个基于单 LiDAR 的场景级人体姿态与形状估计方法，45 fps 实时推理，在 FreeMotion 数据集（578,775 帧，1–7 人/场景）上达到 SOTA [LiveHPS](https://arxiv.org/html/2402.17171v1 "Ren et al., CVPR 2024")
- LiDAR 人体感知综述（arXiv, 2025 年 9 月）建立方法分类体系，核心挑战：远距离人体仅 50–200 个点、视角依赖自遮挡、携带物品噪声 [LiDAR HPE 综述](https://arxiv.org/html/2509.12197v1 "Galaaoui et al., arXiv:2509.12197, 2025")
- LiDAR 独特优势：不受光照限制、精确深度（厘米级分辨率）、天然隐私保护（无面部纹理）、大场景覆盖（50–100 m），但点云远距离稀疏、设备成本高（机械 LiDAR $1,000+），Apple dToF LiDAR 在近距离<5 m 展现消费级应用潜力
- FSAR（ICCV 2023）将联邦学习引入骨架动作识别，NTU RGB+D 60 准确率 91.30%（比 Vanilla FL 提升 10.22%）、NTU RGB+D 120 准确率 84.31%（提升 9.54%）[FSAR](https://openaccess.thecvf.com/content/ICCV2023/papers/Guo_FSAR_Federated_Skeleton-based_Action_Recognition_with_Adaptive_Topology_Structure_and_ICCV_2023_paper.pdf "Guo et al., ICCV 2023")
- 视觉感知隐私保护四层体系：传感器层（LiDAR/深度/红外替代 RGB）→ 表征层（骨架化去除外观信息，NTU120 ~91% 接近 RGB）→ 模型层（联邦学习，精度损失约 7 个百分点）→ 后处理层（面部模糊/去标识化）
- 视觉方法固有局限：光照敏感（低光下性能骤降）、遮挡（HPE/HAR 性能下降）、隐私争议（GDPR 限制）、距离/角度限制（rPPG 典型 0.5–2 m）[rPPG 低光可靠性](https://www.nature.com/articles/s41746-025-02192-y "Nature npj Digital Medicine 2025")
- 光学 vs 射频 trade-off：视觉 HAR ~92%（NTU120）和 HPE 80.9 AP（COCO）精度显著高于射频；rPPG MAE 0.25 bpm（PURE）与 WiFi 0.8 bpm 和 mmWave 1.69%–2.61% 同量级；但射频不受光照影响、支持穿墙、全天候工作
- ME-rPPG 仅 580K 参数可在消费级 CPU 实时运行；骨架 GCN 方法 1–5M 参数/数百 FPS 适合边缘部署；InternVideo2（1B 参数）和 ViTPose-G（1B 参数）需 GPU 推理

### 可用图片
- 无（/data/ 目录中无 Chapter 3 相关图片资源）

### 仍需补充
- DeGCN/ProtoGCN 原始论文精确数字——当前排行数据来自 HyperAI（T3），需确认 IEEE TIP 2024 原文数据
- rPPG 方法系统对比表格——缺少 RhythmFormer、RADIANT 等 2024 年方法在相同数据集上的精度数字
- 热成像生命体征检测的量化精度（MAE/RMSE）——Georgia Tech 论文需阅读 Cell Reports Physical Science 原文
- LiveHPS 具体 MPJPE 数字——论文 Table 2 表格数据待精确提取
- VIPL-HR 数据集上的系统方法对比——当前仅有 PhysFormer 精度数字
- 2025–2026 HPE 新进展——PoseSynVIT 等轻量化方法的 COCO AP 待确认
- 骨架化隐私保护的精度损失量化——需更系统的骨架 vs RGB 精度差异对比


## Chapter 4：基于声学信号的感知算法

### 研究目标
- 系统评估超声波、可听声（audible sound）、声纳信号在非接触感知中的 SOTA 算法，覆盖手势识别、活动识别、呼吸/心率监测等任务
- 分析声学感知的独特优势（低成本、利用现有扬声器/麦克风硬件、穿透遮挡能力）和局限性（多径干扰、环境噪声敏感、感知距离受限）
- 对比声学方案与射频/视觉方案在相同任务上的精度差距和互补性

### 关键发现
- ULTRAWX（Scientific Reports 2025）基于多普勒目标检测+YOLOv7-Tiny，发射 20 kHz 超声波，5 种手势连续识别准确率 93.6%，跨设备平均 95.6%，跨用户+设备 88.6%；有效距离 ≤40 cm，超 60 cm 精度下降显著；20 名志愿者 5,787 样本 [ULTRAWX](https://www.nature.com/articles/s41598-025-93837-1 "Zhang et al., Scientific Reports 2025")
- UltrasonicGS（Sensors 2023）采用 CNN+LSTM 处理超声多普勒频谱图，5 类手势和 10 类手语手势均 >90% 准确率
- UltraGesture（IEEE TMC 2022）利用超声波多普勒效应+深度学习实现细粒度手势感知 [UltraGesture](https://pmc.ncbi.nlm.nih.gov/articles/PMC10064623/ "Ling et al., IEEE TMC 2022, 引自 Huang et al. JCST 2023 综述")
- UW 智能音箱心律监测（Communications Biology 2021）：发射 18–22 kHz FMCW 声学信号，7 麦克风阵列+波束成形。26 名健康人 12,280 次心搏 R-R 间期 MAE 28 ms，心率 MAE 1 BPM；24 名心脏病患者 5,639 次心搏 R-R 间期 MAE 30 ms，心率 MAE 2 BPM；有效距离 40–60 cm [智能音箱心律监测](https://www.nature.com/articles/s42003-021-01824-9 "Wang et al., Communications Biology 2021")
- LoEar（ACM IMWUT 2022）通过 OFDM 多子载波相干叠加（Carrierforming）增强 SNR，将声学感知范围扩展至呼吸 7 m、心搏 6.5 m（此前系统约 2 m 和 1.2 m）；3 m 处呼吸误差 <0.5 BPM、心搏误差 <1 BPM；支持最多 4 人同时监测（间距 ≥60 cm），4 人时心搏中位误差 1.39 BPM [LoEar](https://samsonsjarkal.github.io/KeSun/files/ubicomp22loear.pdf "Wang et al., ACM IMWUT 2022")
- Li et al.（IEEE Access 2025）发表声学非接触健康监测综述，系统回顾主动/被动声学感知全链路 [IEEE Access 声学综述](https://dblp1.uni-trier.de/rec/journals/access/LiLHLXW25.html "Li et al., IEEE Access Vol.13, 2025")
- 基于环境声学的 HAR 框架（Journal of Computational Design and Engineering 2025）整合声事件检测与活动识别，强调可解释性 [Sound-based HAR](https://academic.oup.com/jcde/article/12/8/252/8215199 "JCDE 2025")
- 智能设备心脏骤停检测（npj Digital Medicine 2019, UW/Chan et al.）：Amazon Echo/iPhone 检测濒死呼吸，灵敏度 97.24%、特异性 99.51%、AUC 0.9993；3 m 内准确率 >96.63%；82 h 睡眠数据误报率 0–0.14% [心脏骤停检测](https://www.nature.com/articles/s41746-019-0128-7 "Chan et al., npj Digital Medicine 2019")
- Google Nest 已在商用产品中部署超声波存在感知功能，利用内置扬声器/麦克风发射和分析反射信号，完全设备端执行 [Google Nest](https://support.google.com/googlenest/answer/9509981?hl=en "Google Nest 超声波存在感知")
- SonarBeat（ACM Trans. Computing for Healthcare 2021）利用智能手机扬声器发射不可听声学信号+相位分析，0.5 m 内可靠呼吸率估计 [SonarBeat](https://www.eng.auburn.edu/~szm0001/papers/ACMTCH2021.pdf "Wang et al., ACM THCH 2021")
- 声学感知算法架构演进：传统信号处理（MFCC+SVM）→ CNN+LSTM（频谱图输入）→ 目标检测迁移（ULTRAWX 使用 YOLOv7-Tiny）→ 声学嵌入+视觉模型迁移（VGGish/ViT），轻量化 Transformer 应用尚处早期 [声学感知综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC10064623/ "Huang et al., JCST 2023")
- 信号处理技术：CW 多普勒（如 ULTRAWX 20 kHz 单频）、FMCW 啁啾（如 UW 系统 18–22 kHz 可实现距离+速度二维感知）、OFDM 多子载波（如 LoEar，多径鲁棒性更优但计算复杂度更高）
- 有效距离对比：手势识别 <1 m（ULTRAWX ≤40 cm）、呼吸监测最远 7 m（LoEar）、心搏最远 6.5 m（LoEar）、追踪精度 3.5–8 mm（FingerIO/LLAP）；空气中超声衰减是根本物理限制
- 环境噪声影响：UW 系统背景音乐 75 dB(A) 下 R-R 误差从 25 ms 增至 32 ms；LoEar 在常见室内噪声下性能下降很小但机械振动家电有影响
- 多人支持：LoEar 最多 4 人（间距 ≥60 cm），核心限制为反射路径重叠时无法区分个体
- 安全性：18–24 kHz 近超声对多数成年人不可听，系统声压级 55–75 dB 远低于 WHO/NIOSH 85 dB(A) 安全阈值
- 心率检测跨模态对比：声学（UW）健康人心率 MAE 1 BPM、心脏病患者 2 BPM；雷达健康人 R-R 间期 8–44 ms 但房颤患者 186 ms；rPPG（ME-rPPG）受控 MAE 0.25 BPM 但运动场景 5.38 BPM。声学在不规则心律监测上具有独特优势
- 声学 vs WiFi CSI 物理互补：WiFi 可穿墙、大覆盖但空间分辨率有限（波长 6–12 cm）；声学分辨率高（波长 ~17 mm at 20 kHz）可感知亚毫米位移（心搏 0.3–0.8 mm）但覆盖范围小且不可穿墙
- 声学核心优势：零额外硬件成本、隐私保护（不可听频段）、不受光照限制、毫米级运动检测、可穿透轻薄遮挡；核心局限：有效距离短（通常 <1 m）、环境噪声敏感、多径效应、不支持运动场景

### 可用图片
- 无（/data/ 目录中无声学感知相关图片资料）

### 仍需补充
- IEEE Access 声学综述全文性能对比表——受 IEEE Xplore PDF 访问限制未获取
- 声学 FMCW 啁啾手势识别独立系统数据——纯声学 FMCW 用于手势识别的独立系统较少
- 声学 HAR 具体准确率数字——被动环境声学 HAR 缺乏统一大规模评测基准
- Apple HomePod 和 Amazon Echo 官方声学感知功能确认——目前仅有学术验证而非官方产品功能
- DCASE 2024 Task 4 SED 方法在 HAR 交叉应用中的具体精度数字


## Chapter 5：跨模态融合与新兴方法

### 研究目标
- 分析多模态融合策略（信号级、特征级、决策级融合）在非接触感知中的 SOTA 方法及其精度增益
- 评估基础模型 / 大语言模型（LLM）进入非接触感知领域的新范式，包括：无线感知基础模型（如 LWM）、LLM 驱动的晚期融合、大模型辅助的语义蒸馏与泛化
- 梳理跨模态知识迁移（如用视觉标签训练射频模型）、自监督/对比学习、合成数据增强等前沿方法
- 展望 2026 下半年的技术走向

### 关键发现
- 多模态 WiFi 感知综述（arXiv:2505.06682, 2025 年 5 月）将融合归纳为两大范式：输入级融合（如 MaskFi 将 CSI+RGB 拼接送入 ViT）和特征级融合（如 X-Fi、Babel、HDANet 各模态独立编码后嵌入空间融合），目前尚无决策级融合被应用于多模态 WiFi 感知 [多模态WiFi综述](https://arxiv.org/html/2505.06682v1 "Zhao et al., arXiv:2505.06682, 2025")
- 雷达+WiFi 互补融合跨场景 HAR（Electronics 2025）：GCN 处理 WiFi CSI + CNN 处理雷达 + DANN 域对抗训练，在零样本跨场景中优于单模态 [雷达+WiFi融合HAR](https://www.mdpi.com/2079-9292/14/8/1518 "Chen et al., Electronics 2025")
- WiFi+视觉蒸馏+融合混合方法（ICASSP 2024, Hori et al.）：间接传感器（WiFi/深度/热成像）与直接传感器（视觉/音频）通过教师-学生架构，相比纯 WiFi 方法精度提升 28% [多模态WiFi综述](https://arxiv.org/html/2505.06682v1 "Zhao et al., arXiv:2505.06682, Section 3.3")
- X-Fi（ICLR 2025）：首个模态不变感知基础模型，X-fusion 机制支持 RGB/深度/LiDAR/mmWave/WiFi 五种模态独立或任意组合使用无需重训练；HPE 任务 MPJPE 降低 24.8%、PA-MPJPE 降低 21.4%，HAR 准确率提升 2.8% [X-Fi](https://xyanchen.github.io/X-Fi/ "Chen & Yang, ICLR 2025")
- Babel（SenSys 2025, Microsoft Research/UW-Madison/HKUST）：首个可扩展多模态感知预训练框架，对齐 6 种模态（WiFi/mmWave/IMU/LiDAR/视频/深度骨架），多模态融合精度提升 22%（XRF55 WiFi+mmWave 达 58.97%），单模态平均提升 12%；one-shot 设置下超越 MLLM（OneLLM/M4）达 25.2% [Babel](https://arxiv.org/html/2407.17777v1 "Dai et al., SenSys 2025")
- Apple Research（NeurIPS 2025 Workshop）验证 LLM 作为音频+运动时序数据晚期融合器，12 类活动零样本/单样本 F1 显著高于随机基线，无需对齐训练 [Apple LLM融合](https://machinelearning.apple.com/research/multimodal-sensor-fusion "Demirel et al., Apple Research, NeurIPS 2025 Workshop")
- Wi-Chat（arXiv:2502.12421, 2025）：首个 LLM 驱动 WiFi HAR 系统，将物理模型知识融入提示词，GPT-4o 零样本 62%、4-shot 77%；GPT-4o-mini+视觉 CoT 达 90%，接近有监督方法 [Wi-Chat](https://arxiv.org/html/2502.12421v1 "Zhang et al., arXiv:2502.12421, 2025")
- SensorLLM（EMNLP 2025 主会议）：两阶段框架将 LLM 与运动传感器数据对齐，使 LLM 成为传感器学习器和分类器 [SensorLLM](https://aclanthology.org/2025.emnlp-main.19/ "Li et al., EMNLP 2025")
- GLSDA（arXiv:2510.13390, 2025）：GPT-2 语义蒸馏引导 WiFi 手势泛化，Widar 3.0 均值 95.39%，跨方向提升 2.88% [GLSDA](https://arxiv.org/html/2510.13390v1 "Huang et al., 2025")
- FM-Fi（SenSys 2024）：首个 CLIP→RF 跨模态蒸馏系统，对比知识蒸馏（CKD），零样本 HAR 72.5%、3-shot 94.4%；RF 编码器仅 6.9M 参数（CLIP 140M）；10 环境×10 受试者泛化测试中 3-shot >90% [FM-Fi](https://arxiv.org/html/2410.19766v1 "Weng et al., SenSys 2024")
- RF-Pose（CVPR 2018, MIT CSAIL）：跨模态监督奠基工作，用 OpenPose 视觉标注训练 RF 模型实现穿墙 2D 人体姿态估计，确立"视觉教师-射频学生"范式 [RF-Pose](https://rfpose.csail.mit.edu/ "Zhao et al., CVPR 2018")
- 跨模态蒸馏系列：XFall（IEEE JSAC 2024, 视频→WiFi 跌倒检测，零样本跨域）、AutoDLAR（ACM TOSN 2024, 分类+特征蒸馏）、LoFi（视觉辅助 WiFi 定位标签 <20 cm 误差）[多模态WiFi综述](https://arxiv.org/html/2505.06682v1 "Zhao et al., arXiv:2505.06682, Section 3.2")
- RF-ACCLDM 潜在扩散模型生成合成 RF 数据：FID 10.45（接近真实数据 6.22），HAR F1 93.0%（+2.0%），HPE 误差 4.23 cm，训练时间比标准扩散减少 40%+；支持 WiFi CSI、RFID、FMCW 三平台 [RF合成数据](https://www.oaepublish.com/articles/ces.2024.97 "Wang & Mao, Complex Engineering Systems 2025")
- 潜在扩散 Transformer（LDT）实现 RFID 3D 姿态补全（12→25 关节），首次用生成式 AI 检测 >20 骨骼关节，已见场景关节误差 11.74 cm、未见场景 19.23 cm [RF合成数据](https://www.oaepublish.com/articles/ces.2024.97 "Wang & Mao, CES 2025")
- CARING（IEEE TMC 2024）：联邦学习协作跨域 WiFi 感知，OPERANet 上联邦训练在跨域设置中优于传统域适应 [CARING](https://eprints.whiterose.ac.uk/id/eprint/196030/1/caring.pdf "Li et al., IEEE TMC 2024")
- pFL-Sensing（Tsinghua Sci. Tech. 2026）：边缘-云协同个性化联邦学习感知，为每个边缘设备生成个性化模型 [pFL-Sensing](https://www.sciopen.com/article/10.26599/TST.2024.9010251 "Mao et al., 2026")
- 2026 下半年展望：基础模型统一化（AM-FM/X-Fi/Babel 三模型已出现，预期更大预训练数据集和更多下游任务覆盖）；LLM 感知从概念验证走向实用化（Wi-Chat 62-90%，但推理延迟和成本仍是瓶颈）；生成式 AI 深化（扩散模型向跨模态数据生成和实时增强扩展）；跨域泛化+联邦学习融合为组合解决方案

### 可用图片
- 无（/data/ 目录中无 Chapter 5 相关图片资源）

### 仍需补充
- X-Fi 在 MM-Fi 上各模态组合的具体 MPJPE/PA-MPJPE 精确数值——论文网页中为图片格式，需 ICLR 2025 正式版 PDF
- Babel 在 OPERANet/XRF55 各模态 one-shot 准确率的完整数值表——论文篇幅较长需进一步确认
- SensorLLM 具体 HAR 准确率/F1 数字——EMNLP 2025 原文需提取
- Apple Research LLM 融合的具体 F1 分数——目前仅有"显著高于随机"描述
- CARING 在 OPERANet 上的具体联邦学习精度和通信效率数字
- 决策级融合在更广义多模态感知中的应用实例确认


## Chapter 6：综合评估与系统对比

### 研究目标
- 构建"输入信号 × 感知任务 × SOTA 算法 × 准确率"的系统对比矩阵表，一站式呈现各技术路线的竞争力
- 从多维度（精度、鲁棒性、隐私性、成本、实时性、可扩展性）给出各模态/算法的综合评价
- 识别当前技术瓶颈与开放问题（如泛化性不足、缺乏统一基准、实验室-现实部署差距）
- 基于现有证据给出技术路线选型建议：不同应用场景（智能家居、医疗健康、安防、车载）下的推荐方案

### 关键发现
- 跨模态对比的核心方法论挑战：Cui（2025）指出同一任务在不同技术路线论文中使用不同指标和阈值，WiFi HPE 报告 PCK/MPJPE 阈值不一致，雷达论文 MPJPE 阈值可能为 20 cm 或 50 px，HAR 在 Accuracy/F1/AUC 之间混用 [非侵入式感知对比](https://www.researchgate.net/publication/399071339_Non-intrusive_Human_Pose_Sensing_A_Comparative_Review_of_Wi-Fi_Radar_and_Inertial_Sensing "Cui, Trans. Computer Sci. Intelligent Systems Research Vol.11, 2025")
- 对比矩阵框架（7 模态 × 6 任务）：WiFi CSI — HAR 域内 99.67%（WiGRUNT）/跨域 96-98%（Wi-CBR）、手势 95.39%（GLSDA）/AUROC 0.999（AM-FM SignFi）、HR MAE 0.8 bpm、BR MAE 0.25 bpm；mmWave — HAR 99.8%（RadMamba DIAT）/97.26%（mPCT-LSTM）、HPE MPJPE 18.99 cm（RAPTR）/全监督 8.93 cm、多人 HR 93.43%/BR 97.94%；UWB — HR MAE 4.1 bpm、定位 10-30 cm；RGB — 骨架 HAR 91.0%（DeGCN NTU120）/视频 85.4%（InternVideo2 K700）、HPE AP 80.9%（ViTPose）、rPPG HR PURE MAE 0.25 bpm/MMPD 5.38 bpm；LiDAR — LiveHPS 45fps SMPL 估计；热成像 — 心率/呼吸/体温（具体 MAE 待确认）；声学 — 手势 93.6%（ULTRAWX ≤40cm）、HR MAE 1/2 BPM、呼吸距离 7 m（LoEar）。矩阵中数字不可直接横向比较因数据集和任务粒度差异
- 六维多模态评价（5 分制）：WiFi CSI 精度 3/鲁棒 2/隐私 5/成本 5/实时 3/可扩展 4；mmWave 精度 4/鲁棒 4/隐私 5/成本 3/实时 5/可扩展 3；UWB 精度 3/鲁棒 3/隐私 5/成本 4/实时 4/可扩展 2；RGB 视觉 精度 5/鲁棒 2/隐私 1/成本 4/实时 3/可扩展 3；LiDAR 精度 4/鲁棒 4/隐私 4/成本 2/实时 4/可扩展 3；热成像 精度 3/鲁棒 4/隐私 3/成本 1/实时 3/可扩展 2；声学 精度 3/鲁棒 2/隐私 5/成本 5/实时 4/可扩展 1 [非侵入式感知对比](https://www.researchgate.net/publication/399071339_Non-intrusive_Human_Pose_Sensing_A_Comparative_Review_of_Wi-Fi_Radar_and_Inertial_Sensing "Cui, 2025, 6维定性评价框架")
- 瓶颈1 跨域泛化鸿沟：WiFi CSI 域内 99%+但跨域降至 92-98%（Wang et al. 2025 综述 200+ 篇论文），CSI-Bench（NeurIPS 2025, 26 环境/35 用户/461 小时）为首个 in-the-wild 基准；rPPG 从 PURE MAE 0.25 bpm 跨域到 MMPD 升至 5.38 bpm [WiFi泛化综述](https://arxiv.org/html/2503.08008v2 "Wang et al., 2025") [CSI-Bench](https://arxiv.org/html/2505.21866v1 "Zhu et al., NeurIPS 2025 D&B")
- 瓶颈2 缺乏统一 Benchmark 与可复现性：SDP（arXiv:2601.08463, 2026 年 1 月）指出无线感知领域硬件依赖的信道测量导致数据表示和评估协议差异巨大，提出协议级抽象框架；跨模态层面不存在同时覆盖 WiFi/mmWave/UWB/视觉/声学的标准化评测平台 [SDP](https://arxiv.org/abs/2601.08463 "Zhang et al., arXiv:2601.08463, 2026")
- 瓶颈3 实验室到部署现实鸿沟：多模态融合系统面临传感器异构同步、校准漂移、冲突融合决策等工程挑战 [多模态室内监测综述](https://www.sciencedirect.com/science/article/pii/S1566253524002355 "Nguyen et al., Information Fusion Vol.110, 2024")；非接触生命体征监测在真实世界面临环境噪声、运动伪影、跨被试变异性等系统性挑战 [非接触生命体征综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349365/ "Hassani & Ytterdal, Sensors 2025")
- 瓶颈4 多人/动态场景可扩展性：mmWave 已报告 3 人/5 m 场景（BR 97.94%/HR 93.43%）但精度随人数增加下降；声学 LoEar 最多 4 人（间距≥60 cm）；rPPG 运动场景 MAE 从 0.25→5.38 bpm
- 瓶颈5 基础模型数据效率与部署权衡：AM-FM 920 万样本/439 天预训练达 9 任务 AUROC>0.9 但数据采集成本高；InternVideo2 1B 参数需 GPU vs ME-rPPG 580K 参数可 CPU 实时
- 开放问题：跨模态统一评测框架缺位（MM-Fi/XRF55 仅初步探索）；隐私-精度根本张力（视觉 HAR ~92% 精度最高但隐私风险最高，跨模态蒸馏 FM-Fi 3-shot 94.4% 为弥合路径）；动态环境持续学习尚无成熟边缘方案
- 场景选型-智能家居：推荐 WiFi CSI（零成本/全屋覆盖/隐私保护）+ 声学辅助（智能音箱近距离 HR MAE 1 BPM），不建议 RGB 摄像头 [Cui 2025 场景选型](https://www.researchgate.net/publication/399071339_Non-intrusive_Human_Pose_Sensing_A_Comparative_Review_of_Wi-Fi_Radar_and_Inertial_Sensing "Cui, 2025, 场景驱动选型工作流")
- 场景选型-医疗健康：分层方案——mmWave 高精度（多人 BR 97.94%）、UWB 持续监测（Google HR MAE 4.1 bpm 满足 CTA 标准）、rPPG 精细生理（ME-rPPG PURE MAE 0.25 bpm）、热成像无光环境，声学适合居家睡眠筛查 [非接触生命体征综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349365/ "Hassani & Ytterdal, Sensors 2025")
- 场景选型-安防：mmWave 雷达为主（实时/穿墙/全天候）+ WiFi CSI 大范围存在检测，视觉方法在光照良好且隐私合规区域作补充
- 场景选型-车载：mmWave+视觉融合已成为主导架构，TI 60 GHz mmWave 单传感器实现乘员检测/分类/生命体征，CES 2026 多家展示量产方案，Euro NCAP 2026 CPD 要求驱动 [TI mmWave车载](https://www.ti.com/document-viewer/lit/html/SSZT307 "TI, SSZT307, 60GHz车载感知") [CES 2026](https://anyverse.ai/in-cabin-monitoring-ces-2026/ "CES 2026 车载座舱监测趋势")
- MVDoppler-Pose（CVPR 2025）首次系统对比 mmWave 与相机进行步行姿态估计，证明 mmWave 在长距离和自遮挡场景中优于相机，具备距离无关和遮挡鲁棒优势 [MVDoppler-Pose](https://openaccess.thecvf.com/content/CVPR2025/html/Choi_MVDoppler-Pose_Multi-Modal_Multi-View_mmWave_Sensing_for_Long-Distance_Self-Occluded_Human_Walking_CVPR_2025_paper.html "Choi et al., CVPR 2025")
- 融合增量价值：X-Fi 五模态融合 HPE MPJPE 降低 24.8%；Babel WiFi+mmWave 融合提升 22%；FM-Fi CLIP→RF 3-shot 94.4%；但尚无决策级融合用于 WiFi 感知，融合层级间系统精度对比缺失 [多模态WiFi综述](https://arxiv.org/html/2505.06682v1 "Zhao et al., arXiv:2505.06682, 2025")

### 可用图片
- 无（/data/ 目录中无 Chapter 6 相关图片资源）

### 仍需补充
- 热成像生命体征检测的量化精度（MAE/RMSE）——需阅读 Cell Reports Physical Science 原文
- WiFi CSI HPE 的 MPJPE 数字——Person-in-WiFi 3D（CVPR 2024）和 DT-POSE 需原文提取
- LiDAR HPE 精确关节误差数字——LiveHPS Table 2 需精确提取
- 声学 HAR 精度数字——被动声学 HAR 缺乏统一大规模基准
- 多人场景各模态精度退化的定量数据——目前仅有 mmWave 3 人和 LoEar 4 人数据
- Cui（2025）六维雷达图原图——可能用于视觉呈现，需确认版权


# Section 2：给 Write 阶段的执行建议

- **统一术语定义**：报告开头（Chapter 1）必须明确定义"非接触式感知"的边界——仅包含无需人体佩戴/物理接触的感知方式，摄像头方案属于非接触但需讨论隐私维度。同时统一缩写：HAR、HPE、rPPG、CSI、FMCW。
- **准确率指标口径统一**：不同任务使用不同指标（分类任务用 Accuracy/F1，回归任务用 MAE/RMSE/MPJPE，相关性用 Pearson r），Chapter 1 中应建立指标-任务对应表，后续章节严格遵循。禁止出现"准确率 95%"但不注明数据集、任务、划分方式的模糊表述。
- **SOTA 基准时间锚点**：所有 SOTA 声明以 2026 年 4 月为截止时间，必须注明论文发表/预印本时间和评测数据集。对于快速更新的领域需标注"截至 2026 年 Q1"等时间限定。
- **实验条件标注**：引用准确率数据时，必须注明关键实验条件——受试者数量、环境数量、是否跨域测试、训练/测试划分方式。实验室 controlled 条件下的数字和 in-the-wild 条件下的数字需明确区分。
- **章节间交叉引用**：Chapter 2-4 各自评估单模态方法，但在 Chapter 5（融合）和 Chapter 6（综合对比）中需回溯引用前序章节的数据。写作时需确保数字一致性。
- **避免模态偏见**：射频方向论文数量远多于声学方向，写作时不因论文数量差异暗示技术成熟度高低。
- **隐私讨论的平衡**：摄像头方案的隐私问题需公正讨论，不因此否定其技术价值；射频和声学方案的隐私优势也需注明并非绝对。
- **部署约束的务实评估**：学术精度数字通常在理想条件下取得，报告中应讨论实验室到实际部署的性能衰减问题。
- **对比表质量**：Chapter 6 的对比表应覆盖至少 30-40 个代表性方法，按模态和任务双维度组织，使用多张细分表。
- **展望审慎性**：对 2026 下半年的技术展望应基于已公开的研究计划、预印本趋势，避免无依据预测。
- **时间范围**：以 2026-04-02 为锚点，回顾过去 12 个月（2025年4月—2026年4月），展望至 2026 年 10 月。
