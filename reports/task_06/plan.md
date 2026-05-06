# Section 1：章节研究计划

## Chapter 1：具身智能产业全景——定义、技术栈与发展阶段
### 研究目标
- 明确具身智能的定义边界：与传统工业机器人、纯软件AI Agent的区分
- 梳理具身智能技术栈全貌：感知层、认知/决策层、控制/执行层、仿真/数据层的关系
- 界定当前产业所处的发展阶段（从实验室原型→有限场景商用→规模化部署），以及2025-2026年的关键里程碑事件
- 呈现全球投融资规模与节奏，勾勒产业热度的量化轮廓

### 关键发现
- 发现 1（定义）：具身智能在学术界的共识定义为：其认知和决策能力源于与物理环境的持续交互，依托传感器、执行器和自适应控制机制实现感知—决策—执行闭环，区别于仅依赖静态数据的"离身智能"。[Springer百科](https://link.springer.com/rwe/10.1007/978-981-97-8440-0_8-1 "Embodied Intelligence 百科条目，2025年")
- 发现 2（中国定义）：中国信通院（CAICT）2026年1月发布的《具身智能发展报告》将具身智能定义为"以物理身体为载体，身体形态取决于应用场景，数据来源于身体与环境交互，智能在交互反馈中得以进化"的系统。[CAICT具身智能发展报告](http://www.caict.ac.cn/kxyj/qwfb/bps/202601/P020260130541978285206.pdf "中国信通院，2026年1月发布")
- 发现 3（边界区分）：与传统工业机器人的核心区分在于：传统机器人依赖预编程指令在结构化环境中执行固定任务，具身智能通过多模态感知和自适应控制在动态非结构化环境中泛化执行。与纯软件AI Agent相比，本质差异在于物理实体的存在。[Springer百科](https://link.springer.com/rwe/10.1007/978-981-97-8440-0_8-1 "Embodied vs Disembodied AI 对比") [PMC三层框架综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC12631203/ "2025年学术综述")
- 发现 4（学术技术栈）：2025年发表的综述论文提出"DP-TA"三层架构框架：感知与对齐层、世界建模与结构预测层、策略生成与适应层。[PMC三层框架综述](https://pmc.ncbi.nlm.nih.gov/articles/PMC12631203/ "A review of embodied intelligence systems: a three-layer framework, 2025")
- 发现 5（产业技术栈）：产业实践中技术栈通常分四层：感知层（CV/LiDAR/触觉）、认知/决策层（VLA/LLM/世界模型）、控制/执行层（运动控制/灵巧操作）、仿真/数据层（仿真平台/Sim-to-Real）。NVIDIA GR00T N1.6（22亿参数）和Physical Intelligence pi-0.5（30亿参数）是2025-2026年VLA领域的代表性模型。[RAISE Summit报告](https://www.raisesummit.com/post/robotics-humanoids-physical-ai-leaders "Physical AI Leaders 2026")
- 发现 6（发展阶段）：当前处于"有限场景商用/量产元年"阶段。Gartner 2026年1月预测，至2028年将有不到100家公司能将人形机器人推进到实验之外，不到20家公司能在制造和供应链场景实现规模化生产部署。[Gartner新闻稿](https://www.gartner.com/en/newsroom/press-releases/2026-01-21-gartner-predicts-fewer-than-20-companies-will-scale-humanoid-robots-for-manufacturing-and-supply-chain-to-production-stage-by-2028 "Gartner预测，2026年1月21日")
- 发现 7（出货量）：2025年全球人形机器人出货量达约1.8万台。智元机器人（AgiBot）以约5168台出货量位列全球第一（约39%），宇树科技4200台居第二，优必选1000台居第三。[Forbes](https://www.forbes.com/sites/johnkoetsier/2026/01/09/top-10-humanoid-robot-companies-by-shipments-revealed/ "Forbes引述出货量排名，2026年1月")
- 发现 8（2025里程碑）：2025年关键事件：具身智能首次写入中国《政府工作报告》；16台宇树H1在央视春晚表演；智元机器人完成5000台量产交付；优必选Walker S2开启量产；"具身智能"入选中国"2025年十大流行语"第二名；Figure AI完成超10亿美元C轮（估值390亿美元）。[人民网/新华社](https://world.people.com.cn/n1/2026/0227/c1002-40671139.html "2026年2月综述") [AI Insider](https://theaiinsider.tech/2025/12/31/ai-insiders-robotics-funding-year-in-review/ "2025年度融资回顾")
- 发现 9（2026里程碑）：2026年初事件：CES多家中国企业亮相；特斯拉计划年底前Optimus产线扩展至数千台并限量外部销售；智平方（AI² Robotics）完成B轮系列超10亿元人民币成为深圳首个百亿级具身智能独角兽；Boston Dynamics电动Atlas进入商业试点。[RAISE Summit报告](https://www.raisesummit.com/post/robotics-humanoids-physical-ai-leaders "2026年行业概览") [南方+](https://www.nfnews.com/content/LownkR5D6J.html "智平方融资报道，2026年2月")
- 发现 10（全球融资总量）：2025年全球机器人领域风险投资总额达约386亿欧元（约410亿美元），其中人形机器人细分领域融资从2022年的2.39亿美元增长15倍至2025年的约37亿美元。[RAISE Summit报告](https://www.raisesummit.com/post/robotics-humanoids-physical-ai-leaders "2025年机器人融资数据") [AI Insider](https://theaiinsider.tech/2025/12/31/ai-insiders-robotics-funding-year-in-review/ "2025年度融资回顾")
- 发现 11（中国融资）：2025年中国人形机器人与具身智能领域融资金额超300亿元人民币，约占中国机器人行业融资过亿事件总额的90%。[agent.ren](https://agent.ren/2026/0104/3926.shtml "2025年12月融资月报")
- 发现 12（主要融资案例）：Figure AI Series C超10亿美元（估值390亿美元）；优必选获10亿美元信贷额度；FieldAI两轮合计4.05亿美元；银河通用（Galbot）单轮超3亿美元（总融资约8亿美元，估值30亿美元）；Robotera约1.4亿美元A+轮；宇树科技C轮后估值超100亿元人民币。[AI Insider](https://theaiinsider.tech/2025/12/31/ai-insiders-robotics-funding-year-in-review/ "2025年12大融资事件汇总")
- 发现 13（估值梯队）：截至2025年底/2026年初，估值最高的公司：Figure AI 390亿美元；银河通用30亿美元；宇树科技约14亿美元；优必选IPO前累计融资超9.4亿美元（港股上市）。[Robozaps](https://blog.robozaps.com/b/humanoid-robot-companies "估值排名，2026年3月更新")
- 发现 14（市场预测）：MarketsandMarkets预测人形机器人市场2025年29.2亿美元→2030年152.6亿美元（CAGR 39.2%）；Goldman Sachs预测TAM到2035年将达380亿美元；Morgan Stanley预测2030年全球人形机器人保有量达90万台。[MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/humanoid-robot-market-99567653.html "人形机器人市场报告") [Goldman Sachs](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 "Goldman Sachs Research预测")
- 发现 15（广义市场规模）：MarketsandMarkets 2025年6月报告显示具身智能全球市场规模2025年约44.4亿美元，CAGR约39%，预计2030年达230亿美元。[人民网/新华社](https://world.people.com.cn/n1/2026/0227/c1002-40671139.html "引述M&M报告")
- 发现 16（技术瓶颈）：关键瓶颈：电池续航仅90-120分钟（远低于工业班次8-20小时）；实验室任务成功率可达95%但真实世界降至约60%（sim-to-real gap）；灵巧操作能力远落后于人类手部；执行器成本占制造总成本60-70%，但2023-2024年间制造成本已下降约40%。[RAISE Summit报告](https://www.raisesummit.com/post/robotics-humanoids-physical-ai-leaders "技术成熟度分析，2026年")

### 可用图片
（无，/data/ 目录为空）

### 仍需补充
- IFR（国际机器人联合会）对人形机器人的独立市场预测数据：IFR 2025年报告主要聚焦传统工业机器人，尚未找到单独的人形机器人市场规模预测
- 2025-2026年投融资的精确轮次分布数据（天使轮/A轮/B轮/C轮及以上占比）：缺乏权威机构的系统性轮次分布统计
- 中国信通院（CAICT）2026年1月报告全文的详细数据：PDF读取受限，未能获取报告中的市场规模预测具体数字
- Tesla Optimus 2025年实际产量数据：马斯克在2025 Q4财报电话会表示尚未"实质性方式"使用，但RAISE Summit引述2026年1月已部署超1000台，两个来源口径存在差异

## Chapter 2：核心技术路线（上）——端到端VLA模型与分层大模型架构
### 研究目标
- 深度解析端到端VLA（Vision-Language-Action）模型路线：将视觉感知、语言理解、动作生成统一到单一模型的技术范式
- 深度解析分层大模型（大脑+小脑）架构路线：高层语义理解/任务规划由LLM/VLM承担，底层运动控制由专用策略网络承担
- 比较两条路线在泛化能力、实时性、数据效率、部署成本上的差异
- 梳理各路线的代表性公司/团队及其技术选择，覆盖技术路径、产品进度、商业化进度、融资情况、团队背景

### 关键发现
- 发现 1（VLA技术范式）：VLA（Vision-Language-Action）模型通过将视觉感知、语言理解、动作生成统一到单一模型实现端到端机器人控制，由Google DeepMind于2023年7月通过RT-2首创。动作表征设计是关键分野：离散Token输出（RT-2、OpenVLA）与连续输出（π₀采用流匹配，可达50Hz）。架构上存在单模型设计与双系统设计两条子路线。[VLA模型维基百科](https://en.wikipedia.org/wiki/Vision-language-action_model "VLA模型技术综述")
- 发现 2（代表性模型参数规模）：OpenVLA 7B参数，在97万条真实机器人轨迹上训练，训练成本约21,500 A100-GPU小时；Octo 27M-93M参数轻量级开源策略；SmolVLA 450M参数可在消费级GPU运行。[OpenVLA论文](https://arxiv.org/abs/2406.09246 "OpenVLA: An Open-Source Vision-Language-Action Model")
- 发现 3（Physical Intelligence）：π₀（2024年10月）采用PaliGemma+流匹配，参数约3B-5B，50Hz控制频率。π₀.5（2025年4月）通过异构数据协同训练实现开放世界泛化。融资：种子轮7000万美元→A轮4亿美元（估值24亿）→B轮6亿美元（估值56亿）→2026年3月洽谈约10亿美元（估值超110亿）。团队：Sergey Levine（UC Berkeley）、Chelsea Finn（Stanford）、Karol Hausman（前Google DeepMind）、Lachy Groom（前Stripe）。商业模式B2B SaaS每台300美元/月，目前无商业化时间表。[Physical Intelligence π₀.5博客](https://www.pi.website/blog/pi05 "π0.5技术博客") [TechCrunch报道](https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/ "2026年3月融资报道")
- 发现 4（Google DeepMind RT系列→Gemini Robotics）：RT-1→RT-2→Open X-Embodiment/RT-X（21家机构合作，超100万条真实轨迹）→Gemini Robotics（2025年3月，基于Gemini 2.0，综合泛化基准性能为SOTA VLA的2倍以上，支持多语种指令和精细灵巧操作）→Gemini Robotics On-Device（2025年6月，轻量化设备端版本）。合作伙伴包括Apptronik、Boston Dynamics、Agility Robotics。[Google DeepMind官方博客](https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/ "Gemini Robotics发布")
- 发现 5（NVIDIA GR00T N1系列）：GR00T N1（2025年3月GTC发布），全球首个开源通用人形机器人基础模型，双系统架构（慢思维VLM + 快思维动作模型）。合成数据78万条轨迹（等效6500小时人类演示，仅11小时GPU渲染），性能提升40%。N1.6升级：Cosmos-2B VLM骨干、DiT从16层扩至32层。早期接入伙伴包括1X Technologies、Agility Robotics、Boston Dynamics。[NVIDIA官方新闻稿](https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks "GR00T N1发布") [NVIDIA GR00T N1.6研究页](https://research.nvidia.com/labs/gear/gr00t-n1_6/ "N1.6技术细节")
- 发现 6（Figure AI Helix系列）：Helix（2025年2月）开创双系统VLA架构，System 2为7B参数VLM（7-9Hz），System 1为80M参数视觉运动策略（200Hz），约500小时遥操作数据训练。Helix 02新增System 0层（10M参数，1kHz），替代109,504行手工C++运动控制代码，实现4分钟连续自主操控61个动作。[Figure AI Helix官方博客](https://www.figure.ai/news/helix "Helix技术详情") [Figure AI Helix 02官方博客](https://www.figure.ai/news/helix-02 "Helix 02技术详情")
- 发现 7（银河通用Galbot）：技术从"大脑+小脑"分离架构演进至AstraBrain端到端具身大模型，采用99%合成数据+1%真实数据训练配比。主力产品Galbot G1轮式双臂（173cm/85kg/续航10小时），工业重载S1双臂负载50kg。已在宁德时代、博世、丰田等部署，累计订单数千台。成立于2023年5月，累计融资居中国具身智能首位，估值突破200亿元（最新B++轮25亿元由国家大基金三期首投）。创始人王鹤（清华/Stanford博士），联合创始人姚腾洲（北航/ABB背景）。[华尔街见闻报道](https://wallstreetcn.com/articles/3766500 "银河通用商业化及融资") [量子位报道](https://www.qbitai.com/2026/02/380787.html "AstraBrain技术详解")
- 发现 8（智元机器人AgiBot）：ViLLA架构GO-1模型（2025年9月开源），在VLA基础上引入隐式动作标记。2025年全球出货量第一（5100+台/39%份额），2024年销售额超1亿元。10+轮融资总额超30亿元，最新估值约150亿元人民币，计划2026年港股IPO。创始人邓泰华（前华为副总裁），CTO彭志辉（稚晖君，前华为天才少年）。[智元机器人官网](https://www.zhiyuan-robot.com/article/188/detail/96.html "智元机器人发展历史") [证券时报](https://stcn.com/article/detail/1605342.html "腾讯领投，150亿估值")
- 发现 9（星动纪元RobotEra）：清华大学交叉信息研究院孵化，端到端VLA大模型ERA-42，A轮近5亿元+A+轮近10亿元，估值突破百亿元。创始人陈建宇，清华助理教授/UC Berkeley博士。[36氪](https://eu.36kr.com/zh/p/3369771506779912 "星动纪元技术路线") [泰伯网](https://www.taibo.cn/newsflashes/29519120 "A+轮融资")
- 发现 10（灵初智能PsiBot）：VLA+强化学习路线，2026年3月完成天使轮+Pre-A轮共计20亿元融资，投资方包括国开金融、国中资本等国家级资本。[灵初智能官网](https://www.psibot.ai/%E7%81%B5%E5%88%9D%E6%99%BA%E8%83%BD%E5%B7%B2%E5%AE%8C%E6%88%9020%E4%BA%BF%E8%9E%8D%E8%B5%84%EF%BC%8C%E8%8E%B7%E5%9B%BD%E5%AE%B6%E9%98%9F%E8%B5%84%E6%9C%AC%E9%87%8D%E7%A3%85%E6%8A%95/ "融资公告")
- 发现 11（智平方AI² Robotics）：快慢系统VLA模型GOVLA 0.5，一年内完成12轮融资，估值超百亿元。创始人郭彦东博士（前微软/小鹏/OPPO首席科学家）。[证券时报](https://www.stcn.com/article/detail/3646400.html "智平方融资与技术")
- 发现 12（路线对比）：泛化能力方面端到端VLA语义泛化更强（π₀.5展示零样本跨环境能力）；实时性方面双系统更优（System 1可达200Hz-1kHz）；数据效率方面分层架构各层可独立优化数据源（合成数据验证有效，NVIDIA 11小时生成78万条轨迹）；部署成本方面单模型VLA更简洁但大参数需量化，双系统需至少双GPU。行业趋势：双系统设计正成为人形机器人VLA主流选择，但端到端与分层的边界正在模糊化。[新浪财经对话王鹤](https://finance.sina.cn/tech/2025-06-23/detail-infazmiq9709925.d.html "技术路线收敛判断")

### 可用图片
（无，/data/ 目录为空）

### 仍需补充
- Physical Intelligence 2026年3月约10亿美元轮的最终交割金额和确认估值（目前仅为Bloomberg报道的谈判阶段信息）
- 银河通用2026年3月B++轮后的累计估值确切数字
- 智元机器人GO-1 ViLLA模型的具体参数规模（官方未披露）
- Figure AI的累计融资总额和最新估值
- Google DeepMind Gemini Robotics的模型参数规模（官方未公开）
- 1X Technologies、Skild AI、Covariant等海外VLA/分层架构公司的最新进展

## Chapter 3：核心技术路线（下）——世界模型、仿真基础设施与Sim-to-Real迁移
### 研究目标
- 解析世界模型（World Model）在具身智能中的角色与技术路线：基于视频生成的世界模型、基于潜在动力学的世界模型等
- 梳理仿真平台与Sim-to-Real迁移技术的最新进展：仿真环境构建、域随机化、域适应、零样本迁移等
- 分析仿真-现实迁移作为"数据基础设施"对各技术路线的支撑作用
- 梳理代表性公司/团队在世界模型与仿真领域的布局，覆盖技术路径、产品进度、商业化进度、融资情况、团队背景

### 关键发现
- 发现 1（世界模型定义与分类）：世界模型充当"内部模拟器"，使智能体在潜在空间中预测未来状态并规划行为。两大技术分支：基于视频生成的世界模型（NVIDIA Cosmos、Google DeepMind Genie 系列）和基于潜在动力学的世界模型（DreamerV3、TD-MPC2）。[DreamerV3论文(Nature)](https://www.nature.com/articles/s41586-025-08744-2 "Hafner et al., Nature 640, 647-653, 2025")
- 发现 2（DreamerV3里程碑）：DreamerV3于2025年4月发表于Nature，是第一个以单一固定超参数配置在超过150项任务中超越专用算法的通用世界模型RL算法，首个从零在Minecraft中采集钻石的算法，仅需1块A100训练9天。[DreamerV3论文(Nature)](https://www.nature.com/articles/s41586-025-08744-2 "DOI:10.1038/s41586-025-08744-2")
- 发现 3（NVIDIA Cosmos平台）：2025年1月CES首发，三大模型族：Cosmos Predict（预测视频）、Cosmos Transfer（合成数据生成）、Cosmos Reason（70亿参数推理VLM）。1X、Agility、Figure AI、Skild AI等为早期采用者。[NVIDIA官方新闻稿(GTC 2025)](https://nvidianews.nvidia.com/news/nvidia-announces-major-release-of-cosmos-world-foundation-models-and-physical-ai-data-tools "March 18 2025")
- 发现 4（NVIDIA Cosmos演进）：2026年1月CES发布Cosmos Transfer 2.5/Predict 2.5/Reason 2开放模型；2026年3月GTC发布Cosmos 3——首个统一合成世界生成、视觉推理和动作仿真的世界基础模型，同时预览GR00T N2（新任务成功率为领先VLA模型的2倍以上）。[NVIDIA官方新闻稿(GTC 2026)](http://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world "March 16 2026")
- 发现 5（Newton物理引擎）：2026年3月GTC发布Newton 1.0 GA版，NVIDIA/Google DeepMind/Disney Research共同创建的开源GPU加速物理仿真框架。MuJoCo 3.5（MJWarp）在NVIDIA RTX PRO 6000上运动控制加速252倍、操作任务加速475倍。支持SDF碰撞检测和水弹性接触模型。[NVIDIA技术博客](https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/ "Newton 1.0 GA, March 16 2026")
- 发现 6（仿真平台对比）：Isaac Lab 3.0（Newton+PhysX后端，侧重工业级操作和全身控制）、MuJoCo 3.6（高精度接触动力学，学术标准）、Meta Habitat 3.0（家庭环境协作仿真，数千FPS渲染效率）各有适用场景。[MuJoCo变更日志](https://mujoco.readthedocs.io/en/stable/changelog.html "MuJoCo 3.6.0, March 10 2026") [Meta AI Habitat 3.0](https://ai.meta.com/research/publications/habitat-3-0-a-co-habitat-for-humans-avatars-and-robots/ "Habitat 3.0论文")
- 发现 7（Google DeepMind Genie 3）：2025年8月发布，首个支持实时交互的通用世界模型，24 FPS/720p实时导航，环境一致性可维持数分钟，一致性为涌现能力而非显式3D表征，已与SIMA 2具身智能体集成训练。[Google DeepMind官方博客](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ "August 5 2025")
- 发现 8（合成数据量化证据）：NVIDIA用Isaac GR00T Blueprint在11小时内生成78万条合成轨迹（等效6500小时人类遥操作），GR00T N1性能提升40%。GR00T-Dreams Blueprint实现"真实到真实"工作流，36小时生成GR00T N1.5所需全部合成训练数据（传统方式需近3个月）。[NVIDIA技术博客](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/ "Synthetic Motion Generation Pipeline, 2025")
- 发现 9（Sim-to-Real关键技术）：三大核心方法：域随机化（随机化物理+视觉参数覆盖真实世界变异空间）、师生蒸馏（教师用特权信息训练→蒸馏至仅用真实传感器的学生）、渐进迁移/课程学习。Newton的SDF碰撞和水弹性接触模型直接瞄准缩小sim-to-real gap。[NVIDIA Newton技术博客](https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/ "Newton sim-to-real capabilities, 2026")
- 发现 10（World Labs）：创始人李飞飞，构建空间智能基础模型。2024年9月融资2.3亿美元（估值10亿）；2026年2月融资10亿美元（估值50亿），投资方含AMD、Autodesk、NVIDIA。[Reuters报道](https://www.reuters.com/business/ai-pioneer-fei-fei-lis-world-labs-raises-1-billion-funding-2026-02-18/ "World Labs raises $1B, Feb 18 2026")
- 发现 11（AMI Labs）：图灵奖得主Yann LeCun任董事长，基于JEPA架构构建世界模型。2026年3月完成10.3亿美元种子轮（欧洲最大种子轮），估值35亿美元，投资方含NVIDIA、Samsung、Temasek、Toyota Ventures。明确表示短期不产生收入。[TechCrunch报道](https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/ "March 10 2026")
- 发现 12（Skild AI）：构建统一机器人基础模型"Skild Brain"，支持四足/人形/机械臂等多种形态。2025年活跃收入约3000万美元。2026年1月完成14亿美元C轮（估值超140亿美元），SoftBank领投。与ABB、Universal Robots、富士康合作部署。创立于2023年CMU。[Skild AI官方公告](https://www.skild.ai/blogs/series-c "Skild AI Series C, Jan 14 2026")
- 发现 13（世界模型投资热潮）：2026年Q1主要融资事件：World Labs 10亿、AMI Labs 10.3亿、Runway 3.15亿美元，加上2025年Luma AI 9亿和Skild AI 14亿美元，合计超47亿美元。PitchBook数据显示2025年全球AI VC投资达创纪录2439亿美元，其中机器人创业公司138亿美元（2024年78亿）。[PitchBook数据](https://pitchbook.com/news/articles/artificial-intelligence-market-map-startups-venture-capital "2025 AI VC deal value $243.9B")

### 可用图片
（无，/data/ 目录为空）

### 仍需补充
- "世界模型投资从2024年13亿欧元增长至2025年65亿欧元"这一数据口径在T1/T2来源中未找到原始出处
- TD-MPC2作为潜在空间世界模型代表的定量对比数据
- OpenAI在世界模型方向的具体布局（Sora与物理AI的关系）缺乏2025-2026年T1/T2来源
- 清华/北大等国内团队在世界模型领域的具体研究进展和产业布局

## Chapter 4：硬件本体与形态路线——人形、四足、灵巧手及专用形态
### 研究目标
- 梳理具身智能硬件本体的主要形态路线及其技术特点：人形双足机器人、四足机器人、灵巧手/操作臂、轮式/复合移动平台、专用形态
- 分析不同硬件形态与软件技术路线的适配关系
- 梳理各形态路线的代表性公司，涵盖技术路径、产品进度、量产成本、融资情况与团队背景
- 对比中外公司在硬件工程化能力上的差异与各自优势

### 关键发现
- 发现 1（Figure AI）：三代产品演进（01→02→03）。Figure 03身高173cm/61kg/负载20kg/续航5小时，搭载触觉传感器（检测低至3克力）、掌部相机、无线感应充电。累计融资约19亿美元，Series C超10亿美元（2025年9月，估值390亿美元）。BotQ工厂初始年产能12,000台。创始人Brett Adcock（Archer Aviation/Vettery创始人）。2025年初终止与OpenAI合作，转向自研Helix系统。[Reuters](https://www.reuters.com/business/robotics-startup-figure-valued-39-billion-latest-funding-round-2025-09-16/ "Figure AI Series C $39B估值") [Figure AI官方](https://www.figure.ai/news/introducing-figure-03 "Figure 03发布与BotQ量产规划")
- 发现 2（Tesla Optimus）：2024年推出Gen 3手部（22自由度/50个执行器含触觉传感器）。2025年计划生产10,000台但夏季放弃（手部开发困难），Optimus项目负责人Milan Kovac离职。截至2026年1月在Giga Texas和Fremont工厂部署超1,000台Gen 3。Musk预计最终售价2-3万美元，2027年开始对外销售，长期年产100万台。[Wikipedia Optimus](https://en.wikipedia.org/wiki/Optimus_(robot) "Optimus机器人页面") [Sherwood News](https://sherwood.news/tech/tesla-abandoned-plans-to-make-thousands-of-optimus-robots-this-year/ "Tesla放弃2025年量产计划")
- 发现 3（Agility Robotics）：Digit双足步行机器人（鸟类仿生反关节腿，175cm/负载16kg/多阵列摄像头+LiDAR）。Series B 1.5亿美元（Amazon Industrial Innovation Fund），正在融资4亿美元Series C（WP Global领投/SoftBank参投，投前估值17.5亿美元）。Salem工厂最终年产能目标10,000台以上。已在Amazon仓库测试料箱整理。CEO Peggy Johnson（前Microsoft高管）。[GeekWire](https://www.geekwire.com/2025/agility-robotics-reportedly-raising-400m-for-humanoid-warehouse-robots/ "Agility $400M融资报道")
- 发现 4（Boston Dynamics电动Atlas）：2026年1月CES发布量产版。56自由度、臂展2.3米、举重50kg、工作温度-20℃至40℃。执行器由Hyundai Mobis供应。Hyundai规划年产30,000台机器人工厂。2026年部署已满额预订，首批客户含Hyundai RMAC和Google DeepMind。与Google DeepMind合作集成基础模型。[Boston Dynamics官方](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ "CES 2026 Atlas产品发布")
- 发现 5（1X Technologies）：NEO人形机器人定位家用，售价20,000美元或499美元/月订阅，168cm/22自由度手部/续航4小时，专利肌腱驱动系统。累计融资超1.3亿美元（EQT Ventures/Tiger Global/OpenAI Startup Fund）。2025年12月与EQT达成协议计划2026-2030年部署最多10,000台NEO。[TechCrunch](https://techcrunch.com/2025/12/11/1x-struck-a-deal-to-send-its-home-humanoids-to-factories-and-warehouses/ "1X NEO与EQT合作")
- 发现 6（Apptronik）：Apollo人形机器人，源于UT Austin/NASA Valkyrie项目。Series A总额超9.35亿美元（含2026年2月5.2亿美元扩展轮，B Capital与Google联合领投），估值50亿美元。已在Mercedes-Benz、GXO Logistics、Jabil工厂试点。与Google DeepMind合作使用Gemini Robotics。预计2027年开始量产，年租赁价约8万美元。CEO Jeff Cardenas，约300名员工。[CNBC](https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html "Apptronik $5B估值") [Apptronik官方](https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a "Series A $935M官方公告")
- 发现 7（宇树科技Unitree）：2016年创立，创始人王兴兴（1990年生，浙江理工/上海大学硕士）。产品线：四足（Go/B系列）+人形（H1/G1 9.9万元起/R1）。2025年人形出货超5,500台全球第一，四足累计超3万台。营收从2022年1.23亿增至2025年17.08亿元（3年增13倍），2025年净利润约6亿元。人形毛利率62.91%。核心部件自研率超95%。2026年3月科创板IPO受理，拟募资42.02亿元，整体估值约420亿元。C轮6.94亿元（中国移动/腾讯/阿里等），累计13轮融资。[瑞财经](https://m.rccaijing.com/news-7441267069385635239.html "宇树科技IPO与财务数据") [国际电子商情](https://www.esmchina.com/news/14030.html "宇树招股书核心数据")
- 发现 8（乐聚机器人）：2016年创立，哈工大团队，深圳。核心产品夸父（KUAVO）人形机器人，国内首款具备跳跃能力的开源鸿蒙人形机器人。国产化率从2018年10%→2025年90%，成本从300万元降至十几万元。2025年10月Pre-IPO轮近15亿元（估值约120亿元），累计7轮融资。华为重要生态伙伴，联合发布全球首款5G-A人形机器人。[21世纪经济报道](https://m.21jingji.com/article/20251022/herald/2f5212453ea1d399421007c41d79d8cf_zaker.html "乐聚机器人融资与团队")
- 发现 9（傅利叶智能）：2015年创立，创始人顾捷，从康复机器人转型通用人形。GR-2（53自由度，高度仿生）、GR-3（2025年9月预售），GR-1/GR-2均已量产交付。累计约11轮融资，公开金额超16亿元，估值约80亿元。[傅利叶官网](https://www.fftai.cn/about-medium-company/32 "傅利叶E系列融资近8亿元")
- 发现 10（Sanctuary AI灵巧手）：Phoenix人形机器人（170cm/70kg/负载25kg），核心差异化为21自由度液压阀驱动五指手，功率密度比电机/腱绳驱动高一个数量级，20亿次循环测试无泄漏或退化。累计融资超1.4亿美元。总部温哥华。[Sanctuary AI官方博客](https://www.sanctuary.ai/blog/sanctuary-ai-demonstrates-in-hand-manipulation-capabilities-for-improved-general-purpose-robot-dexterity "灵巧手技术")
- 发现 11（四足机器人格局）：宇树科技四足2022-2025年销量从2,403台增至17,946台（单年前三季度），均价从3.86万元降至2.72万元。Boston Dynamics Spot售价约7.5万美元定位高端工业市场，宇树Go2以1,600美元起占据消费级和中端工业市场。[瑞财经](https://m.rccaijing.com/news-7441267069385635239.html "宇树四足销量与定价")
- 发现 12（中外工程化差异）：中国优势——执行器/关节模组自研与垂直整合（宇树自研率95%+/国产化85%/人形均价16.76万元仍保持62.91%毛利率），量产规模领先（中国企业2025年出货占全球绝对主体）。海外优势——AI/软件栈更成熟（Helix/FSD迁移/DeepMind合作/Gemini集成），品牌与企业级渠道（Spot/Amazon合作），Hyundai汽车级供应链（年产3万台规划）。[国际电子商情](https://www.esmchina.com/news/14030.html "宇树自研率数据")
- 发现 13（2025全球出货格局）：Omdia数据2025年全球人形机器人总出货约1.33万台，智元超5,100台（39%）、宇树4,200台（34%，宇树自述超5,500台口径差异）、优必选约1,000台（7%）。赛迪传媒报告显示全球约1.7万台、宇树占32.4%。中国企业占据绝对主体。[36氪](https://eu.36kr.com/zh/p/3709666119479682 "Omdia 2025全球出货数据")

### 可用图片
（无，/data/ 目录为空）

### 仍需补充
- Tesla Optimus 2026年实际部署数量的T1/T2来源确认（现有"超1,000台"来源可信度偏低）
- Agility Robotics $400M融资是否正式完成（截至研究时为"reportedly raising"状态）
- Apollo机器人详细技术规格（身高、自由度、重量完整参数表）
- Boston Dynamics电动Atlas定价和具体产能数据
- 优必选（UBTECH）产品线和融资详情（本章尚未充分覆盖）
- 傅利叶智能GR-2/GR-3的续航、负载、定价和出货量数据

## Chapter 5：商业化落地与应用场景——从工厂到生活的渗透路径
### 研究目标
- 系统梳理具身智能当前已实现或正在推进商业化落地的核心场景：工业制造、仓储物流、零售服务、医疗康复、家庭服务、农业、特种作业等
- 分析各场景的需求特征、技术成熟度、商业模式（销售 vs 租赁 vs RaaS）
- 评估商业化进展中的核心瓶颈：成本、可靠性、安全合规、客户接受度
- 呈现中国与海外市场在商业化路径上的差异

### 关键发现
- 发现 1（Figure AI-BMW部署）：Figure 02在BMW斯帕坦堡工厂完成11个月部署，每日10小时班次，累计运行1,250+小时，搬运90,000+个钣金零件，参与生产30,000+辆X3，精度要求5mm公差内2秒完成。BMW随后在莱比锡工厂启动首个欧洲人形机器人试点。[Figure AI官方公告](https://www.figure.ai/news/production-at-bmw "Figure 02 BMW部署成果") [BMW集团官方新闻稿](https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time "BMW莱比锡试点")
- 发现 2（雷诺大规模部署）：雷诺2026年3月宣布18个月内部署350台Calvin人形机器人（与Wandercraft合作），聚焦重复性高体力消耗的"棕地"任务，是汽车行业规模最大的人形机器人部署计划之一。[Metrology News](https://metrology.news/renault-to-deploy-350-humanoid-robots-in-industrial-automation-push/ "雷诺350台人形机器人，2026年3月")
- 发现 3（丰田-Agility商业协议）：2026年2月丰田加拿大制造公司与Agility Robotics签署商业协议，计划部署7台Digit用于RAV4生产线的制造、供应链和物流运营，采用RaaS模式。[Agility Robotics官方公告](https://www.agilityrobotics.com/content/agility-robotics-announces-commercial-agreement-with-toyota-motor-manufacturing-canada "丰田加拿大商业协议")
- 发现 4（中国工业部署）：银河通用已获宁德时代/博世/丰田/现代/北汽等深度合作，累计订单数千台，与百达精工签署1000+台协议。智元近百台远征A2-W落地富临精工工厂（4个工位/三条装配线/20余种物料/14kg负载/零倾倒事故），2025年订单金额接近14亿元。优必选第1,000台Walker S2下线，2025年交付超500台，订单金额近14亿元。[人民网](http://finance.people.com.cn/n1/2026/0303/c1004-40673745.html "银河通用商业化") [半月谈/新华社](http://www.banyuetan.org/kj/detail/20260108/1000200033136211767861634411891100_1.html "2026产业展望")
- 发现 5（仓储物流）：Agility Digit在GXO Logistics配送中心累计搬运超100,000个周转箱，是全球首个在仓储场景产生商业收入的人形机器人部署。已部署于GXO/Schaeffler/Amazon/丰田加拿大等Fortune 500客户。[Agility Robotics官方博客](https://www.agilityrobotics.com/content/digit-moves-over-100k-totes "Digit搬运超10万周转箱，2025年11月")
- 发现 6（零售场景）：银河通用"银河太空舱"便利店在20余城市超100家门店，7×24小时不间断运营超一年，智慧药房24个城市、单店管理超5,000种SKU。北京出现机器人4S体验店"机械伊甸"模式，汇聚近30家厂商约30余种机型，带动进店客流环比提升15%。[人民网](http://finance.people.com.cn/n1/2026/0303/c1004-40673745.html "银河通用零售") [北京市政府网站](https://www.beijing.gov.cn/fuwu/bmfw/sy/jrts/202603/t20260307_4551538.html "机器人4S店")
- 发现 7（医疗康复）：傅利叶智能2026年1月发布"脑机具身智能康复港"，将GR-3引入康复认知训练并联合瑞金医院/复旦类脑研究院发起联合创新计划。银河通用与宣武医院/华西医院深度合作。[傅利叶官网](https://www.fftai.cn/about-medium-company/53 "傅利叶十年核心战略，2026年1月")
- 发现 8（RaaS商业模式）：RaaS月费通常2,000-8,000美元，包含硬件/软件/维护/保险。以Digit为例购买价约25万美元、RaaS月费6,000-8,000美元，对比美国仓库工人完全成本约7,800美元/月可实现"Day 1正ROI"。IDTechEx预测RaaS将在2028年占人形机器人部署的40%以上。[Robozaps ROI分析](https://blog.robozaps.com/b/roi-of-humanoid-robots "人形机器人ROI指南2026")
- 发现 9（ROI测算）：按10万美元机器人/日运行16小时/5年寿命计算，TCO约18.75万美元，折合有效时薪约6.70美元，远低于美国仓储劳动力35-45美元/时。在中国一线城市（劳动力6-8美元/时）回本期需60个月以上，导致中美落地策略分化。[Robozaps ROI分析](https://blog.robozaps.com/b/roi-of-humanoid-robots "按地区ROI差异")
- 发现 10（中国政策支持）：工信部宣布国内整机企业超140家、产品超330款，将发布标准化体系建设指南并设立千亿元产业基金。地方层面北京200亿基金+10平方公里"机器人谷"，深圳规划百万台年产能。[新浪新闻/工信部](https://news.sina.cn/bignews/insight/2026-01-31/detail-inhkeaqr2995928.d.html "工信部官宣")
- 发现 11（国际安全标准）：ISO/TC299 WG12于2025年7月启动人形/四足机器人安全标准制定（预计2028年发布）。中国占38%专家席位，主导5项国际标准。欧盟AI Act高风险AI义务2026年8月2日全面适用。[Novanta](https://novanta.com/news/how-global-safety-standards-for-humanoid-robotics-are-being-built/ "ISO标准制定进展") [欧盟官方](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai "EU AI Act时间线")
- 发现 12（核心瓶颈）：高端机型成本仍超60万元（约8万美元+），家庭任务成功率低于60%，灵巧手寿命仅约1,000小时（工业需超10,000小时）。Figure 02在BMW部署中发现前臂是最主要硬件故障点。头部企业优必选2024年净利率约-28%，行业尚处以亏损换规模阶段。[新浪新闻](https://news.sina.cn/bignews/insight/2026-01-31/detail-inhkeaqr2995928.d.html "成本与可靠性瓶颈") [Figure AI官方](https://www.figure.ai/news/production-at-bmw "硬件可靠性经验")
- 发现 13（中外市场差异）：中国2025年出货占全球67%，国产关节模组价格为海外1/3，打样到量产45天（海外120天）。高工机器人预测2025年国内出货1.8万台（同比+650%），2026年有望达6.25万台。海外以B2B工业/物流大客户为主，中国呈现B2B+B2C多元格局（工业制造+新零售+消费体验），政策端直接驱动力度远超海外。[新浪新闻](https://news.sina.cn/bignews/insight/2026-01-31/detail-inhkeaqr2995928.d.html "中国供应链优势") [半月谈/新华社](http://www.banyuetan.org/kj/detail/20260108/1000200033136211767861634411891100_1.html "2026产量预测")

### 可用图片
（无，/data/ 目录为空）

### 仍需补充
- Amazon对Digit的具体部署规模和最新进展（Amazon官方未公开详细数据）
- Tesla Optimus在自有工厂的部署详情和2026年量产目标进展
- 人形机器人专用保险产品的公开数据
- 优必选2.5亿元最大单笔订单的客户名称

## Chapter 6：技术路线对比与趋势展望
### 研究目标
- 横向对比全部技术路线在关键维度上的表现：泛化能力、数据效率、部署成本、实时性、安全性、可解释性
- 分析技术路线的融合趋势：端到端与分层的边界模糊化、世界模型嵌入VLA等
- 展望2026-2027年的关键技术节点与产业拐点判断
- 总结全球竞争格局：中美在不同环节的优劣势分布

### 关键发现
- 发现 1（VLA架构三分路线）：当前"大脑"技术路线可归纳为三种范式：单模型端到端VLA（π₀/π₀.5，架构简洁，50Hz控制）、双系统VLA（Helix/GR00T N1，VLM 7-9Hz + 动作策略200Hz，兼顾泛化与实时性）、分层大模型（Gemini Robotics-ER，生成抓取姿态/轨迹/代码对接底层控制器）。自变量机器人创始人王潜指出传统分层方法信息传递效率低且误差累积。[新华网](http://www.news.cn/20250915/620a6301a3844e3a91ce63ada3b759d3/c.html "机器人跨越三重门，2025年9月")
- 发现 2（VLA标准化评测缺失）：VLA模型领域尚缺乏统一基准评测体系，Allen AI的VLA Leaderboard处于beta状态。原力灵机创始人唐文斌指出"行业里连一个真正大规模的Benchmark都没有"。[21世纪经济报道](https://www.21jingji.com/article/20260329/herald/61ea6560498528bcc8906a533f71053a.html "百亿估值具身智能创企圆桌，2026年3月29日")
- 发现 3（GR00T N2 DreamZero架构）：NVIDIA于2026年3月GTC预览GR00T N2，采用全新"世界动作模型"（WAM）架构，将世界模型的环境预测与VLA的动作生成统一，新任务成功率为领先VLA的2倍以上，MolmoSpaces和RoboArena排名第一，预计2026年底可用。[NVIDIA官方新闻稿](http://nvidianews.nvidia.com/news/nvidia-expands-open-model-families-to-power-the-next-wave-of-agentic-physical-and-healthcare-ai "GTC 2026发布，2026年3月16日")
- 发现 4（世界模型+VLA融合学术趋势）：银河通用王鹤团队提出DreamVLA框架将世界模型预测功能嵌入VLA流程。自变量机器人将世界模型和端到端通用模型整合于同一架构。清华大学王鑫团队在IEEE发表综述认为"联合MLLM-WM驱动的具身AI架构将主导下一代具身系统"。[知乎/王鹤团队盘点](https://zhuanlan.zhihu.com/p/2009655362840712006 "王鹤团队2025年工作盘点")
- 发现 5（技术路线收敛：数据决胜共识）：银河通用王鹤明确表示"起决定性作用的是数据"。千寻智能高阳、自变量王潜、星动纪元席悦均印证这一判断。CES 2026将训练数据采集识别为与AI模型和硬件并列的核心基础设施层。[新华网](http://www.news.cn/20250915/620a6301a3844e3a91ce63ada3b759d3/c.html "王鹤：数据决定机器人能力下限，2025年9月") [21世纪经济报道](https://www.21jingji.com/article/20260329/herald/61ea6560498528bcc8906a533f71053a.html "百亿估值具身智能创企圆桌，2026年3月")
- 发现 6（端到端与分层边界模糊化）：Figure AI Helix 02新增System 0层（10M参数/1kHz），替代10万行C++代码，即便在端到端框架内也出现类分层多系统协作。GR00T从N1双系统到N2 WAM架构演进体现从分层向世界模型融合的方向收敛。[EE Times](https://www.eetimes.com/humanoid-robots-exit-labs-mapping-the-technical-path-to-embodied-ai-at-aw-2026/ "AW 2026技术路径报道")
- 发现 7（发展阶段判断：GPT-2至GPT-3前夜）：千寻智能高阳将当前阶段类比为"GPT-2时代"，预计2026年末至2027年中迎来"GPT-3级别"突破。宇树王兴兴认为"真正的ChatGPT时刻"将在"机器人在陌生环境中凭指令完成约80%任务"时到来。[21世纪经济报道](https://www.21jingji.com/article/20260329/herald/61ea6560498528bcc8906a533f71053a.html "高阳GPT-2判断") [新华社](https://english.news.cn/20251231/0a082888ab384fcaa572ee7a11ae7d9d/c.html "王兴兴ChatGPT时刻判断")
- 发现 8（出货量预测）：Goldman Sachs预测2026年全球人形机器人出货5-10万台，2030年代初中期年出货100万台。高工机器人预测2026年中国国内6.25万台。RAISE Summit称2026年初全球保有量约16,000台，预计2030年达200万台。[Leo Wealth研究](https://leowealth.com/insights/the-dawn-of-humanoid-robots-and-physical-ai/ "引述Goldman Sachs预测") [Goldman Sachs Research](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 "TAM $38B by 2035")
- 发现 9（成本曲线趋势）：Goldman Sachs预测单位经济将改善至1.5-2万美元。2023-2024年间制造成本已下降约40%。宇树均价从2023年59.34万元/台降至2025年16.76万元/台（约2.3万美元），毛利率仍达62.91%。Gartner预测至2028年不到20家公司能实现规模化部署。[Gartner新闻稿](https://www.gartner.com/en/newsroom/press-releases/2026-01-21-gartner-predicts-fewer-than-20-companies-will-scale-humanoid-robots-for-manufacturing-and-supply-chain-to-production-stage-by-2028 "Gartner预测2026年1月")
- 发现 10（关键技术观察指标）：2026-2027年关注：VLA scaling law首次系统验证（DiffusionVLA已从2B扩展至72B）；灵巧手MTBF乐聚已超1,000小时但工业需超10,000小时；触觉VLA（Tactile-VLA充电器插入90%成功率vs π₀基线25-40%）；UBTECH预计人形机器人平均生产率从30-40%提升至2027年初约80%。[EE Times](https://www.eetimes.com/humanoid-robots-exit-labs-mapping-the-technical-path-to-embodied-ai-at-aw-2026/ "乐聚MTBF数据") [新华社](https://english.news.cn/20251231/0a082888ab384fcaa572ee7a11ae7d9d/c.html "UBTECH生产率预测")
- 发现 11（长程任务链瓶颈）：即便单步任务成功率95%，10步任务链累积成功率仅约60%。当前VLA演示多为单任务或短链（3-5步），复合误差问题是从演示走向部署的核心瓶颈。[Dylan Bourgeois预测](https://dtsbourg.me/en/articles/predictions-embodied-ai "长程任务链挑战，2025年12月")
- 发现 12（SCSP中美竞争评估）：SCSP 2026年3月评估认为中国在先进制造业机器人领域"决定性领先"。五维评估：创新领导力（美国窄幅领先但趋势指向中国追赶）、工业产能（中国决定性领先）、市场生态（中国领先，2024年占全球工业机器人安装54%）、人才管道（中国领先，约100所高校新设机器人专业）、国家杠杆（中国领先，举国体制+十五五规划）。[SCSP技术竞争评分卡](https://scorecard.scsp.ai/publications/robotics "The Robot Deficit, 2026年3月")
- 发现 13（中国优势量化）：Morgan Stanley数据：中国过去5年人形机器人专利7,705项（美国5倍）。中国2024年占全球工业机器人安装54%。发改委数据：超150家人形机器人企业，行业年增速超50%，预计2030年市场规模1,000亿元。Carnegie报告指出中国优势在于"强大的硬件制造基础和供应链"。[新华社](https://english.news.cn/20251231/0a082888ab384fcaa572ee7a11ae7d9d/c.html "Morgan Stanley专利数据") [Carnegie报告](https://carnegieendowment.org/research/2025/11/embodied-ai-china-smart-robots "Embodied AI: China's Big Bet, 2025年11月")
- 发现 14（美国优势）：美国在"认知大脑"层面窄幅领先——主导VLA模型（π₀、Gemini Robotics）和仿真平台（NVIDIA Isaac/Cosmos）。DreamerV3（Nature 2025）、Gemini Robotics、GR00T N2 DreamZero等标志性突破均出自美国团队。Goldman Sachs指出"没有一个国家或地区具有完全主导地位"。[Goldman Sachs Research](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 "全球人形机器人市场预测") [SCSP评分卡](https://scorecard.scsp.ai/publications/robotics "美国创新领导力评估")
- 发现 15（中国算法追赶态势）：中国VLA模型（AstraBrain、ERA-42、GO-1、GOVLA 0.5等）密集涌现，Spirit AI Spirit v1.5登上全球排行榜首。但在VLA原创性、世界模型前沿、仿真平台等"认知层"与美国仍有差距。Carnegie指出中国劣势包括先进AI芯片获取受限、高精度力矩传感器等依赖进口。SCSP趋势显示中国正在追赶。[Carnegie报告](https://carnegieendowment.org/research/2025/11/embodied-ai-china-smart-robots "中国比较劣势") [SCSP评分卡](https://scorecard.scsp.ai/publications/robotics "创新领导力趋势")
- 发现 16（多维技术路线对比矩阵）：端到端VLA泛化中高/实时性高/部署成本低/可解释性低；双系统VLA泛化高/实时性高/部署成本中/可解释性中；WAM（GR00T N2）泛化极高（2x+ SOTA）但多项待验证；分层大模型泛化中/可解释性高/安全性高/实时性低。各路线均在快速迭代中。

### 可用图片
（无，/data/ 目录为空）

### 仍需补充
- GR00T N2 DreamZero的详细架构论文（截至2026年3月底仅GTC keynote预览，完整论文未公开）
- VLA模型标准化基准对比数据（Allen AI Leaderboard处于beta，需更权威独立评测）
- IDC对2026-2027年人形机器人出货量的独立预测具体数字
- 中美在具身智能AI顶会论文发表数量的精确对比数据

# Section 2：给 Write 阶段的执行建议
- **技术路线主线贯穿**：全文以技术路线为组织主线，公司案例服务于技术路线的阐释。每提及一家公司，必须先明确其所采用的技术路线归属，再展开技术路径、产品、融资等信息。
- **中外双线并行**：每条技术路线下均需同时覆盖海外与中国的代表性公司，避免单边叙事。
- **时间锚定严格**：所有数据、事件、产品进度均需标注明确时间点（精确到季度或月份）。融资信息需注明轮次、金额、估值、投资方。产品进度需区分"发布""量产""出货""客户部署"等不同阶段。
- **术语统一**：VLA（Vision-Language-Action）、世界模型（World Model）、Sim-to-Real（仿真到现实迁移）、端到端（End-to-End）、分层架构（Hierarchical Architecture）、大脑/小脑（High-level planner / Low-level controller）。首次出现给出完整定义。
- **公司信息五要素模板**：每家代表性公司统一覆盖——①技术路径 ②产品进度 ③商业化进度 ④融资情况 ⑤团队背景。
- **数据交叉验证**：融资金额、出货量、估值等核心数字需多源交叉验证，优先采信公司官方披露和权威媒体/研究机构报告。
- **审慎表述前瞻判断**：使用"预计""有望""存在可能"等审慎措辞，不做确定性断言。
- **避免技术路线的简单优劣判断**：不同技术路线适用于不同场景和发展阶段，行文应呈现各路线的适用条件与局限。
- **图表建议**：Chapter 1 设置技术栈分层图，Chapter 2-3 设置技术路线架构对比图，Chapter 4 设置公司/产品对比表，Chapter 6 设置多维度矩阵图。
- **章节衔接**：各章开头需有承上启下的导引段落，说明本章在整体框架中的位置。
- **时间口径**：研究区间覆盖 2025年4月至2026年9月（过去12个月至未来6个月），以当前日期 2026-03-30 为锚点。
