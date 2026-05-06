# 低代码/无代码平台对传统开发流程影响的深度研究报告——研究计划

> **研究时间口径**：以 2026-04-02 为锚点，回顾 2025 年 4 月 — 2026 年 3 月（过去 12 个月），展望至 2026 年 10 月（未来 6 个月）。
> **本地资料**：/data/ 目录无与本课题相关的素材；所有事实素材需通过外部研究获取。

---

# Section 1：章节研究计划

## Chapter 1：低代码/无代码平台的定义、分类与市场全景
### 研究目标
- 建立"低代码"与"无代码"的统一概念定义与边界划分
- 呈现 2025-2026 年全球及中国市场规模、增速与竞争格局
- 梳理行业渗透率与企业规模分布

### 关键发现
- Gartner 将企业级低代码应用平台（Enterprise LCAP）定义为"利用模型驱动开发工具、生成式 AI 和预构建组件目录，加速开发和维护应用程序的软件平台"，强制特征包括可视化开发工具/IDE、数据虚拟化能力、AI 辅助开发功能等 [Gartner MQ LCAP 报告](https://www.processexcellencenetwork.com/low-code-automation/news/gartner-releases-magic-quadrant-for-low-code-application-platforms "2025年Gartner Magic Quadrant报告评估12家LCAP厂商")。
- Gartner 明确区分低代码与无代码："'无代码'是一个营销术语，意指面向非专业开发者的工具"；低代码面向专业与准专业开发者、允许自定义代码扩展，无代码完全面向业务用户、以拖拽式可视化构建为核心 [Kissflow Gartner 分析](https://kissflow.com/low-code/gartners-magic-quadrant-about-low-code-vs-no-code-2025/ "Gartner关于低代码vs无代码的定义，2025-2026更新")。
- Gartner 将低代码开发技术市场细分为六大品类：LCAP、BPA、MXDP、RPA、iPaaS、CADP，其中 LCAP 是最大子市场 [InfoWorld](https://www.infoworld.com/article/2337677/low-code-development-technologies-market-forecast-to-hit-445-billion-by-2026.html "Gartner低代码市场分类与预测")。
- Gartner 预测全球低代码开发技术市场（广义口径，含六大子品类）2029 年达 582 亿美元，2024-2029 年 CAGR 为 14.1% [Gartner 文档摘要](https://www.gartner.com/en/documents/7146430 "Gartner Forecast Analysis: Low-Code Development Technologies, Worldwide")。LCAP 子市场 2027 年将达 165 亿美元，CAGR 16.3% [Gartner Risk and Opportunity Index](https://www.gartner.com/en/documents/5459763 "Gartner LCAP子市场预测")。
- Forrester 预测低代码市场（含公民开发工具）2028 年逼近 500 亿美元，公民开发用例将以约 21% 的增速持续增长 [App Builder 统计汇编](https://www.appbuilder.dev/low-code-statistics "引用Forrester 2024年1月报告")。
- 不同机构口径差异显著：2025 年市场规模估算从 129 亿美元（Precedence Research 窄口径）到 455 亿美元（Gartner 广义口径）不等，差异超 3 倍 [App Builder 统计汇编](https://www.appbuilder.dev/low-code-statistics "Grand View Research低代码市场估算")。
- IDC 数据显示 2024 年中国低代码与零代码软件市场规模为 40.3 亿元人民币（约 5.5 亿美元），预计到 2029 年达 129.8 亿元，未来 5 年 CAGR 为 26.4%。其中低代码占比 85.6%，零代码占比 14.4% [IDC 中国](https://mfe-prod.idc.com/getdoc.jsp?containerId=prCHC53666825 "IDC：低代码与零代码深度融合生成式AI，2025年7月发布")。
- 简道云以 34.5% 市占率连续四年蝉联中国零代码平台整体市场第一；奥哲蝉联中国低零代码软件市场独立厂商第一 [帆软社区](https://auth.fanruan.com/thread-152080-1-1.html "简道云蝉联中国零代码市场占有率第一") [新浪财经](https://finance.sina.cn/tech/2025-07-11/detail-inffafmt1009343.d.html "奥哲获得独立厂商第一")。
- 2025 年 Gartner MQ for Enterprise LCAP 评估 12 家厂商：领导者 6 家（Microsoft、OutSystems、Mendix、Salesforce、ServiceNow、Appian），挑战者 2 家（Oracle、Zoho），远见者 2 家（Pegasystems、SAP），利基厂商 2 家（Creatio、Retool）[Process Excellence Network](https://www.processexcellencenetwork.com/low-code-automation/news/gartner-releases-magic-quadrant-for-low-code-application-platforms "Gartner 2025 MQ LCAP完整评估结果")。
- Microsoft Power Platform 拥有超过 5600 万月活跃用户（MAU），同比增长 27%，FY25 期间用户已创建超过 300 万个 AI Agent [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/microsoft-recognized-as-a-leader-in-the-2025-gartner-magic-quadrant-for-enterprise-low-code-application-platforms/ "微软2025年Gartner MQ领导者公告")。
- Forrester Wave™ Low-Code Platforms for Professional Developers, Q2 2025 将 Microsoft 评为领导者（战略与产品两个维度均排名第一），OutSystems 和 ServiceNow 亦为领导者 [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/microsoft-is-a-leader-in-2025-forrester-wave-low-code-platforms-for-professional-developers/ "Microsoft 2025 Forrester Wave领导者公告")。
- Forrester 调查显示 87% 的企业开发者至少在部分开发工作中使用低代码开发平台 [Forrester 报告页](https://www.forrester.com/report/the-state-of-low-code-global-2025/RES186709 "Forrester State of Low-Code Global 2025")。
- Gartner 预测到 2025 年 70% 的企业新开发应用将使用低代码或无代码技术（2020 年不足 25%），2026 年该比例将达 75%，届时 80% 的低代码工具用户将来自 IT 部门以外 [InfoWorld](https://www.infoworld.com/article/2337677/low-code-development-technologies-market-forecast-to-hit-445-billion-by-2026.html "Gartner预测75%新应用用低代码/2026")。
- 84% 的企业已采用低代码或无代码工具以减轻 IT 积压、加速内部应用交付 [Kissflow 统计汇编](https://kissflow.com/low-code/low-code-trends-statistics/ "84%企业采用低代码数据")。
- 金融服务、医疗健康和制造业是 LCNC 采用最快的行业；近 60% 的定制企业应用由非 IT 专业开发者构建，30% 由几乎无技术技能的员工构建 [Kissflow 统计汇编](https://kissflow.com/low-code/low-code-trends-statistics/ "行业采用率与公民开发者占比数据")。
- Gartner 预测到 2028 年近 80% 的企业将依赖 LCAP；Agentic AI 将通过 LCAP 在全球五分之四的企业中得到实施 [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/microsoft-recognized-as-a-leader-in-the-2025-gartner-magic-quadrant-for-enterprise-low-code-application-platforms/ "Gartner 2028年80%企业采用LCAP预测")。
- 中国市场厂商格局多元化：独立厂商（奥哲、得帆、简道云）、应用软件/SaaS 厂商（金蝶、用友）、平台型厂商（华为、浪潮），以及钉钉宜搭、飞书多维表格、明道云、轻流等知名玩家 [IDC 中国](https://mfe-prod.idc.com/getdoc.jsp?containerId=prCHC53666825 "IDC 2024年中国低零代码厂商格局")。
- IDC 中国报告指出整合生成式 AI 能力是当前低零代码产品的重要发展方向 [IDC 中国](https://mfe-prod.idc.com/getdoc.jsp?containerId=prCHC53666825 "IDC：低零代码融合生成式AI趋势")。

### 可用图片
- 无（本地无相关图片素材；外部 Gartner MQ 象限图和 IDC 市场份额饼图受版权保护）

### 仍需补充
- Gartner 最新低代码技术市场预测原始新闻稿（582 亿美元/2029 年数据来自付费文档，缺少原始新闻稿直接链接）
- Forrester 2025 全球低代码状态报告具体数据（付费报告，87% 开发者使用低代码等结论来自 T2/T3 转述）
- 中国市场按行业（金融/制造/零售/政务）拆分的低代码采用率数据（缺乏 2024-2025 年最新版本）
- 大型企业 vs 中小企业的采用率分布（缺乏 T1/T2 来源的权威细分统计）
- Gartner 70%/75% 新应用低代码化预测的实际达成情况回顾评估（原预测分别为 2021 年发布）
- 不同机构市场规模口径对照说明（建议正文中制作口径对照表）

---

## Chapter 2：对传统软件开发流程的冲击——效率提升的真实图景
### 研究目标
- 量化低代码/无代码平台在各开发环节的提速幅度（实证数据）
- 分析"公民开发者"崛起对开发团队构成的影响
- 界定效率提升的适用边界：哪些项目类型受益最大，哪些不适用

### 关键发现
- Forrester 2021 年 Appian TEI 研究（基于 5 家企业客户访谈和复合组织建模）显示，使用 Appian 低代码平台相比传统编码，应用开发速度提升 17 倍（从平均每项目 5 周/6 名开发者缩短至约 12 小时/4 名开发者），开发资源需求减少 40%，三年风险调整后开发成本节约 495.7 万美元 [Forrester TEI of Appian](https://media.trustradius.com/product-downloadables/HT/WZ/KLUZNTWL24T2.pdf "Forrester TEI of Appian, 2021年6月, 受Appian委托")。
- 2024 年 9 月 Forrester 受 Microsoft 委托的 Power Platform TEI 研究显示，企业使用 Power Platform 低代码工具可将开发流程加速 35%，三年风险调整后直接开发和 IT 成本节约达 4360 万美元，整体 ROI 为 224%，投资回收期不到 6 个月 [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2024/09/03/reduce-development-times-and-increase-roi-with-microsoft-power-platform/ "2024 Forrester TEI of Microsoft Power Platform")。
- Forrester 受 Microsoft 委托的 Power Apps Premium TEI 研究（2024 年 9 月，基于 13 家组织代表访谈，复合组织 30,000 员工/100 亿美元年收入）表明，专业开发者使用 Power Apps Premium 后应用开发时间缩短 50%，高影响场景中用户每人每年节省 250 小时，三年 ROI 为 206% [Microsoft Power Apps Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/millions-of-hours-saved-50-faster-app-development-and-206-roi-achieved-with-microsoft-power-apps-premium/ "Forrester TEI of Power Apps Premium, 2024年9月")。
- Forrester 2021 年 OutSystems TEI 研究（基于 4 家企业组织访谈，复合组织为 30 亿美元全球工业企业/10,000 员工）显示三年 ROI 达 506%，开发效率提升高达 66%，投资回收期不到 6 个月 [OutSystems 官方](https://www.outsystems.com/news/tei-low-code-roi/ "Forrester TEI of OutSystems, 2021年")。
- Forrester 2022 年 Mendix TEI 研究显示，传统编程每个应用需 2.4 名开发者，Mendix 平台下降至 0.96 名；以 5 个应用为例，传统开发成本 126 万美元，使用 Mendix 后降至 45.6 万美元，三年应用交付节约达 808 万美元 [Mendix Blog](https://www.mendix.com/blog/quantifiable-impact-how-todays-enterprise-landscape-benefits-from-low-code/ "Forrester TEI of Mendix, 2022年9月")。
- Gartner 定义公民开发者为"使用未被 IT 或业务部门明确禁止的工具，为自身或他人创建应用程序能力的员工"，并预测到 2026 年大型企业中公民开发者将以 4:1 的比例超过专业软件开发者 [Kissflow 引述 Gartner](https://kissflow.com/citizen-development/gartner-on-citizen-development/ "Kissflow引述Gartner预测")。
- Gartner 预测到 2026 年 80% 的低代码用户将来自 IT 部门以外的非技术专业人员 [byteiota 引述 Gartner](https://byteiota.com/low-code-hits-44-5b-gartner-2026-forecast-explained-2/ "byteiota综述Gartner 2026预测")。
- Forrester 2023 年开发者调查显示 87% 的企业开发者在至少部分开发工作中使用低代码开发平台 [Forrester Blog](https://www.forrester.com/blogs/the-low-code-market-could-approach-50-billion-by-2028/ "Forrester博客, 2024年1月29日")。
- Forrester Appian TEI 数据揭示各环节具体提升：编码阶段从传统 200 小时缩减至 48 小时（约缩短 94%）；新开发者培训缩减 90%；应用上市时间从 6 个月缩短 50% 至 3 个月 [Forrester TEI of Appian](https://media.trustradius.com/product-downloadables/HT/WZ/KLUZNTWL24T2.pdf "Forrester TEI of Appian, 2021年6月")。
- Microsoft Power Apps TEI 案例：某金融服务公司将原需 3-6 周/10 名全职员工的 HR 手工流程压缩至 1 小时/2 名员工；EY 使用 Power Platform 将 SAP 系统自动支付清算率从 30% 提升至 80%，匹配支付率达 95%，预计年节省 23 万小时 [Microsoft Power Apps Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/millions-of-hours-saved-50-faster-app-development-and-206-roi-achieved-with-microsoft-power-apps-premium/ "Forrester TEI of Power Apps Premium, 2024年9月")。
- McKinsey 2022 年分析指出低代码/无代码平台核心价值体现在三个方面：增强现有应用、快速原型验证（验证后可快速转化为生产应用）、以及企业级协作共建（业务开发者负责需求定义和低代码逻辑，IT 负责架构和复杂技术工作）[McKinsey Tech Forward](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/low-code-no-code-a-way-to-transform-shadow-it-into-a-next-gen-technology-asset "McKinsey, 2022年8月19日")。
- 低代码效率提升最显著的场景包括：内部工具和业务流程自动化、客户门户和表单驱动应用、系统集成和工作流编排（Appian 客户通过低代码实现应用组合精简 50%）、遗留系统替换（OutSystems TEI 中替换遗留应用节省 76.5 万美元）[Forrester TEI of Appian](https://media.trustradius.com/product-downloadables/HT/WZ/KLUZNTWL24T2.pdf "Forrester TEI of Appian") [OutSystems Blog](https://www.outsystems.com/blog/posts/low-code-roi/ "OutSystems引述Forrester TEI")。
- 效率提升有限甚至适得其反的场景包括：需要复杂算法和高性能计算的系统、深度定制超出平台预设模式的应用、遗留系统深度集成中的特殊协议处理、以及对规模和并发有极端要求的核心交易系统 [byteiota](https://byteiota.com/low-code-hits-44-5b-gartner-2026-forecast-explained-2/ "byteiota综述平台局限性")。
- 开发者社区对低代码质量评价分裂：39% 认为改善了软件质量，26% 认为不变，23% 认为降低了质量；82% 的软件专业人士使用过低代码平台，42% 的低代码使用者报告较高工作满意度（高于仅使用传统编码者的 31%）[byteiota 引述行业调查](https://byteiota.com/low-code-hits-44-5b-gartner-2026-forecast-explained-2/ "byteiota综述开发者调查数据")。
- Appian TEI 中某金融服务公司 CIO 指出："过去需要五周才能开发的东西，使用 Appian 可以在第二天就完成"，50% 的上市时间缩短意味着应用可提前数月投入使用 [Forrester TEI of Appian](https://media.trustradius.com/product-downloadables/HT/WZ/KLUZNTWL24T2.pdf "Forrester TEI of Appian, 2021年6月")。
- Power Platform 2024 TEI 研究证实，7% 的营收增长直接归因于加速上市流程，三年风险调整后额外营收达 1540 万美元；某制造业客户报告营收增长 18%-20% [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2024/09/03/reduce-development-times-and-increase-roi-with-microsoft-power-platform/ "2024 Forrester TEI of Microsoft Power Platform")。
- G&J Pepsi-Cola Bottlers 使用 Power Platform 实现超过 150 万美元节约，Store Audit 应用节省 10 万美元外部开发成本，Parking Lot 应用仅用一天完成开发 [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2024/09/03/reduce-development-times-and-increase-roi-with-microsoft-power-platform/ "Microsoft博客引述客户案例")。

### 可用图片
- 无

### 仍需补充
- Gartner"公民开发者 4:1 预测"和"75% 新应用使用低代码"预测的一手原始出处（目前均为二手转述，原始报告需付费访问）
- 低代码在"需求分析-设计-编码-测试-部署"各独立 SDLC 阶段的系统性量化拆分数据（现有 TEI 报告主要聚焦总体经济影响）
- 大规模样本的独立学术研究（现有 TEI 研究均为供应商委托，样本量 4-13 家企业）
- 开发者满意度调查的原始出处确认（"82% 使用过""39% 认为改善质量"等数据未标明具体调查名称和样本量）

---

## Chapter 3：隐性成本与技术风险——维护成本、技术债与供应商锁定
### 研究目标
- 系统梳理 LCNC 应用中长期运维中的维护成本问题与技术债表现形式
- 评估供应商锁定的风险严重程度与迁移退出成本
- 分析安全漏洞、数据合规与"影子 IT"对企业 IT 治理的影响

### 关键发现
- 渥太华大学 Timothy C. Lethbridge 在 2021 年学术论文中指出，低代码平台上的软件"往往积累大量复杂代码，其维护难度可能高于传统语言编写的代码"，原因在于低代码平台普遍缺乏版本控制、关注点分离、自动化测试和文学编程等工程实践的支持 [Lethbridge 2021](https://www.site.uottawa.ca/~tcl/papers/ISola2021-LowCodeisHighCode-Lethbridge-CameraReady.pdf "Low-Code Is Often High-Code, ISoLA 2021")。
- 该论文论证了"低代码最终变成高代码"的普遍模式：低代码应用的代码量可增长至数千行脚本甚至数十万行，且缺乏模块化、注释和可重用能力，一旦底层平台版本更新，应用被迫进行大规模维护或重写 [Lethbridge 2021](https://www.site.uottawa.ca/~tcl/papers/ISola2021-LowCodeisHighCode-Lethbridge-CameraReady.pdf "ISoLA 2021 案例分析")。
- 2024 年 Morning Consult 受 Unqork 委托对美国 500 名商业和技术领导者调查显示，超过 90% 的受访者表示其组织承受某种形式的技术债务，近 80% 表示技术债在过去 12 个月内导致了业务关键项目的取消或延迟 [Morning Consult/Unqork 2024 调查](https://unqork.com/resource-center/guides/2024-morning-consult-unqork-survey-tech-debt-stifles-innovation-at-80-of-enterprises-surveyed/ "2024年技术债对企业创新的影响调查")。
- HFS Research 与 Publicis Sapient 2025 年联合报告（基于 608 位全球 2000 强企业高管调查）估计，全球 2000 强企业累积了 1.5 至 2 万亿美元的技术债务，近 30% 的 IT 预算投入现代化改造，但仅约三成组织完成了核心应用现代化 [HFS/Publicis Sapient 2025 报告](https://www.publicissapient.com/content/dam/ps-reinvent/us/en/2025/05/insights-lp/hfs-ai-tech-debt-report/docs/HFS-PS-Report-SmashTechDebt-2025.pdf "基于608位高管调查")。
- BCG 研究发现 79% 的企业认为平台价值足以证明成本合理，但 70% 仍在积极寻找替代方案；62% 的 IT 决策者对供应商锁定表示担忧；企业更换平台的三大顾虑为技术迁移复杂性（75%）、过渡期生产力损失（64%）、运营停机（63%）[Betty Blocks 引用 BCG 研究](https://blog.bettyblocks.com/breaking-low-code-why-vendor-lock-in-is-the-hidden-cost-you-cant-ignore "BCG供应商锁定研究")。
- 83% 的企业数据迁移项目失败或超出预算；大型技术项目失败的年均成本可超过 2000 万美元 [Betty Blocks 引用 BCG 研究](https://blog.bettyblocks.com/breaking-low-code-why-vendor-lock-in-is-the-hidden-cost-you-cant-ignore "迁移失败率与成本")。
- 五年期 TCO 模拟对比显示，Appian 低代码平台开发 150 用户应用五年总成本约 686,700 美元，.NET 传统开发约 618,000 美元——低代码方案反高约 11%，主要因年均约 75,000 美元许可费和更高维护人员成本 [Unstoppable Software 成本分析](https://unstoppablesoftware.com/the-real-costs-of-low-code-development/ "低代码vs传统开发五年TCO对比")。
- OWASP 维护了"Low-Code/No-Code Top 10"安全风险项目，列出十大风险：账户模拟、授权滥用、数据泄露与意外后果、身份验证与安全通信失败、安全配置错误、注入处理失败、易受攻击和不可信组件、数据与密钥处理失败、资产管理失败、安全日志与监控失败 [OWASP LCNC Top 10 项目](https://github.com/OWASP/www-project-top-10-low-code-no-code-security-risks "OWASP官方GitHub仓库")。
- LCNC-SEC-01（账户模拟）尤为突出：开发者使用管理员身份连接数据库时，终端用户共享同一身份访问数据；LCNC-SEC-09（资产管理失败）对应"无代码蔓延"——大量应用缺乏清单管理被遗忘 [Cloud Wars 解读](https://cloudwars.com/cybersecurity/top-10-low-code-no-code-risks-and-how-to-secure-rapid-development/ "OWASP LCNC Top 10详细解读")。
- Gartner 研究发现影子 IT 占大型企业 IT 总支出的 30%-40%；到 2027 年 75% 的员工将自行获取或创建 IT 部门不知情的技术资产 [Auvik Shadow IT 统计汇编](https://www.auvik.com/franklyit/blog/shadow-it-stats/ "引用Gartner数据")。
- Gartner 预测到 2030 年超过 40% 的全球组织将因未经授权的"影子 AI"工具（包含 LCNC 蔓延）而遭遇安全或合规事件 [Gartner 2025 新闻稿](https://www.gartner.com/en/newsroom/press-releases/2025-11-19-gartner-identifies-critical-genai-blind-spots-that-cios-must-urgently-address0 "Gartner预测40%企业将遭遇影子AI安全事件")。
- EMC 研究显示因影子 IT 导致的数据丢失和停机年度成本高达 1.7 万亿美元 [Auvik Shadow IT 统计汇编](https://www.auvik.com/franklyit/blog/shadow-it-stats/ "影子IT年度损失")。
- 学术研究（Tadi 2021, JSER）通过技术对比分析指出：低代码平台自动生成的数据库查询在处理大数据量和复杂连接时效率较低，在延迟敏感、计算密集型的企业应用中明显不足 [Tadi 2021](https://www.researchgate.net/publication/390204681_Scalability_and_Performance_Benchmarking_of_Low-Code_Platforms_vs_Traditional_Development_in_Large-Scale_Enterprise_Applications "JSER 2021")。
- 低代码平台自动生成代码性能通常为手工优化代码的 60%-80%；当超过 30% 的应用需要自定义代码时，低代码优势将消失 [ByteIota 市场分析](https://byteiota.com/low-code-hits-75-enterprise-adoption-66b-market-2026/ "低代码性能与定制化临界点")。
- 75% 的大型企业到 2026 年将使用至少四种低代码工具，多平台策略降低单一锁定风险但增加治理复杂度 [ByteIota 市场分析](https://byteiota.com/low-code-hits-75-enterprise-adoption-66b-market-2026/ "多平台策略与治理复杂度")。
- Lethbridge 论文案例：一位 Excel 专家在两天内构建了一个预估需一个人年开发的应用，但仅其本人能维护，两年内便不得不被更传统的系统取代 [Lethbridge 2021](https://www.site.uottawa.ca/~tcl/papers/ISola2021-LowCodeisHighCode-Lethbridge-CameraReady.pdf "Excel案例：维护知识过度集中")。
- 真实案例：一家全球保险公司使用低代码平台构建了管理约 400 万件洪水索赔的应用，维护人员修复 bug 时意外删除整个数据库且无备份，丢失全部记录 [Unstoppable Software 案例分析](https://unstoppablesoftware.com/the-real-costs-of-low-code-development/ "保险公司低代码应用灾难性数据丢失案例")。
- HFS/Publicis Sapient 2025 调查：49% 的领导者表示 IT 聚焦于维护遗留系统而非推动变革，36% 表示技术债务未因当前服务模式减少，71% 愿意更换服务商以获得更好的 AI 执行力 [HFS/Publicis Sapient 2025 报告](https://www.publicissapient.com/content/dam/ps-reinvent/us/en/2025/05/insights-lp/hfs-ai-tech-debt-report/docs/HFS-PS-Report-SmashTechDebt-2025.pdf "企业对技术债务与维护模式的不满")。

### 可用图片
- 无

### 仍需补充
- BCG 供应商锁定研究原始 PDF 链接（当前数据来自 Betty Blocks 博客转引）
- Gartner"影子 IT 占 30-40% IT 支出"的原始报告直链（多家 T2/T3 来源交叉验证但缺原始链接）
- 低代码应用与传统应用的跨平台、跨行业长期维护成本大规模定量对比研究
- 具体企业从低代码平台迁移到传统开发的公开成本案例
- Gartner 或 Forrester 对低代码技术债积累速度的定量评估
- OWASP LCNC Top 10 官方页面状态确认（原始 owasp.org 页面返回 404，已用 GitHub 仓库替代）

---

## Chapter 4：立场分歧——企业管理者视角 vs 开发者视角
### 研究目标
- 拆解管理者推动 LCNC 采用的核心诉求（降本、提速、减少 IT 瓶颈）的合理性与盲区
- 呈现开发者核心顾虑（可扩展性受限、代码质量不可控、职业价值被低估）的事实支撑
- 梳理已出现的协调机制与最佳实践（如融合开发团队）

### 关键发现
- Gartner 2025 年度全球 CIO 调查（覆盖 88 国 3,186 名 CIO/技术高管 + 1,126 名非 IT 高管）显示仅 48% 的数字化举措达到或超过业务成果目标，凸显管理层对加速数字交付工具的强烈需求 [Gartner CIO Survey 2025](https://www.gartner.com/en/newsroom/press-releases/2024-10-22-gartner-survey-reveals-that-only-48-percent-of-digital-initiatives-meet-or-exceed-their-business-outcome-targets "N=4,312")。
- 72% 的 IT 领导者报告因项目积压无法投入战略性工作，这是管理者推动低代码采纳的首要驱动力 [Spidya 低代码 ROI 分析](https://spidya.com/en/blog/cheetah-low-code-development-platform-en/low-code-platforms-rois-insights-from-50-enterprise-projects "引用Forrester Research数据")。
- Caspio/StarCIO 对 268 名 IT 决策者调查显示 90% 认为定制软件应用是战略赋能工具，但仅 41% 对自身应用交付能力具有高度信心 [Caspio 调查报告](https://www.caspio.com/reports/low-code-the-business-transformation-game-changer/ "N=268 IT决策者")。
- 管理者的盲区：高 ROI 数字高度依赖成熟治理框架，拥有成熟治理的组织实施成功率为 81%，缺乏治理者仅为 43% [Spidya 低代码 ROI 分析](https://spidya.com/en/blog/cheetah-low-code-development-platform-en/low-code-platforms-rois-insights-from-50-enterprise-projects "治理成熟度对成功率的影响")。
- Appian 对 400 名开发者调查发现 64% 在学习低代码前持怀疑态度，但学习后 42% 表示"非常满意"（纯高代码开发者仅 31%）；75% 的低代码开发者参与了创新项目（高代码为 64%）[Appian 开发者调查](https://appian.com/blog/2022/low-code-vs--high-code--compare-developer-careers--earning-poten "N=400+开发者, 2022年")。
- 专业开发者核心技术顾虑集中在三方面：代码质量不可控（低代码生成的代码优化程度低于手写代码）、定制化受限（功能边界问题）、厂商锁定（平台代码仅在该平台内可用且需持续付费）[CSHARK 分析](https://www.cshark.com/are-we-doomed-to-low-code-platforms/ "专业开发团队视角的低代码评估")。
- IDG/Appian 对 300 名 IT 从业者调查显示，开发者最不满的工作方面为：排障时间、截止日期压力、重复编码任务、缺乏参与战略项目的机会；80% 认同低代码有助于自动化重复开发任务 [IDG/Appian 调查](https://appian.gcs-web.com/news-releases/news-release-details/survey-79-it-developers-say-low-code-can-improve-key-aspects-job "N=300, 2019年")。
- 87% 的企业开发者在部分开发工作中使用低代码平台，说明抵触并非全面拒绝，而是对使用方式和治理的关切 [ToolJet 转引 Forrester](https://blog.tooljet.com/forrester-wave-on-low-code-development-platforms/ "转引自Forrester报告")。
- Mendix 调查（N=2,000，1,000 名业务人员 + 1,000 名 IT 人员）揭示认知鸿沟：仅 9.4% 的业务人员认为开发者需要理解业务，但 66% 期望开发者解决业务问题；仅 24% 认为开发者"善于沟通"[Mendix 调查](https://www.mendix.com/press/new-survey-illuminates-gap-in-priorities-between-business-stakeholders-and-application-developers-in-todays-upended-business-landscape/ "N=2,000, 2020年4月")。
- Gartner 研究显示"Digital Vanguard"组织（CIO 与 CxO 共同领导数字交付）71% 的数字化举措达标（对比全体平均 48%），CxO 将 35% 的业务员工分配到技术工作中（普通仅 21%）[Gartner CIO Survey 2025](https://www.gartner.com/en/newsroom/press-releases/2024-10-22-gartner-survey-reveals-that-only-48-percent-of-digital-initiatives-meet-or-exceed-their-business-outcome-targets "Digital Vanguard模式")。
- Gartner 将"融合团队"（Fusion Teams）定义为"分布式和多学科的数字业务团队，融合技术和其他类型的领域专长"，核心理念是 IT 与业务人员组成跨职能团队共同承担数字产品交付 [Microsoft Learn 转引 Gartner](https://learn.microsoft.com/en-us/power-platform/developer/fusion-development "Gartner 2019 Digital Business Teams Survey")。
- Microsoft Power Platform 融合开发模型定义三类角色：公民开发者/Maker、专业开发者、IT 专业人员/DevOps 工程师，核心原则是"所有人应使用与其任务匹配的工具"[Microsoft Learn](https://learn.microsoft.com/en-us/power-platform/developer/fusion-development "Power Platform融合开发概述")。
- Mendix 提出"低代码卓越中心"（CoE）模型采用"启动-结构化-规模化"三阶段方法论，以 Portfolio/People/Process/Platform/Promotion 五组件为框架 [Mendix CoE 指南](https://www.mendix.com/blog/how-to-build-a-low-code-center-of-excellence/ "2024年2月发布")。
- 使用低代码平台的组织在按时按范围按预算交付、跟上业务需求、具备所需技能和资源等维度上表现显著优于未使用者 [Caspio 调查报告](https://www.caspio.com/reports/low-code-the-business-transformation-game-changer/ "N=268，低代码用户vs非用户对比")。
- 近 9/10 的业务人员表示如有不需要专业编程技能的工具愿意自行尝试开发应用，揭示公民开发需求的巨大潜力，但也解释了为什么专业开发者感到自身价值可能被低估 [Mendix 调查](https://www.mendix.com/press/new-survey-illuminates-gap-in-priorities-between-business-stakeholders-and-application-developers-in-todays-upended-business-landscape/ "N=2,000, 2020年")。

### 可用图片
- 无

### 仍需补充
- State of Frontend 2024 调查（N=6,028）完整数据（大多数受访者不使用 LCNC 平台的具体百分比未获取）
- Forrester 2024 State of Low-Code 详细数据（付费报告，"87% 企业开发者使用低代码"来自二手转引）
- 同一调查中管理者与开发者对同一 LCNC 项目评价差异的直接对比数据集
- 开发者"被迫使用"低代码的大样本定量数据
- Gartner Fusion Teams 预测的一手原文确认（如"到 2025 年 80% 以上组织采用融合团队"）

---

## Chapter 5：AI 时代的变量——生成式 AI 对低代码/无代码的重塑
### 研究目标
- 分析生成式 AI 对 LCNC 价值主张的强化或替代效应
- 评估 AI 辅助编程工具（Copilot、Cursor 等）与 LCNC 平台的互补/竞争关系
- 梳理主流 LCNC 平台整合 AI 能力的进展与效果

### 关键发现
- 截至 2025 年 10 月 GitHub Copilot 用户超 2600 万（微软 CEO Nadella 披露），FY2026 Q2 付费订阅者达 470 万（同比增长约 75%）；Fortune 100 企业中 90% 已采用 [TechCrunch](https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/ "GitHub Copilot crosses 20M users") [CNBC](https://www.cnbc.com/2026/02/24/cursor-announces-major-update-as-ai-coding-agent-battle-heats-up.html "Nadella 2025年10月数据")。
- AI 编码工具 Cursor 增长极为迅猛：ARR 从 2023 年约 100 万美元飙升至 2025 年 11 月突破 10 亿美元，截至 2026 年 2 月据报道达 20 亿美元 ARR；估值从 2024 年 4 亿美元攀升至 2025 年 11 月 293 亿美元 [Cursor 官方博客](https://cursor.com/blog/series-d "Cursor Series D, 2025年11月") [CNBC](https://www.cnbc.com/2026/02/24/cursor-announces-major-update-as-ai-coding-agent-battle-heats-up.html "Cursor $29.3B valuation")。
- GitHub 与 Accenture 联合研究显示，企业环境中开发者对 Copilot 建议的平均采纳率约 30%，PR 数量提升 8.69%，成功构建率提升 84%，95% 开发者表示编码更愉悦 [GitHub Blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/ "Quantifying Copilot's impact, 2024年5月")。
- AI 编码市场竞争升温：Anthropic Claude Code 运行收入超 25 亿美元，OpenAI Codex 周活超 150 万，Google 收购 Windsurf 核心团队 [CNBC](https://www.cnbc.com/2026/02/24/cursor-announces-major-update-as-ai-coding-agent-battle-heats-up.html "AI coding agent battle, 2026年2月")。
- Microsoft Power Platform 拥有超 5600 万 MAU，FY2025 构建超 300 万个 agent；Copilot 使 Power Apps 构建成功率提高 60%，数据输入速度提升 30% [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/microsoft-recognized-as-a-leader-in-the-2025-gartner-magic-quadrant-for-enterprise-low-code-application-platforms/ "2025 Gartner MQ Leader")。
- Mendix AI 助手 Maia 嵌入 Studio Pro IDE，提供全生命周期 AI 辅助（对话问答、逻辑推荐可提速 30%、自然语言生成应用架构等）[Mendix 官网](https://www.mendix.com/platform/ai/aiad/ "Maia for Smart Development")。
- OutSystems 提供 AI Agent Builder（无代码构建 AI agent）和 Agent Workbench（自定义与编排工具），支持自然语言定义 agent 行为 [OutSystems 官网](https://www.outsystems.com/low-code-platform/gen-ai/ "Go agentic with OutSystems")。
- Appian 2025 年 11 月宣布 Agent Studio 正式上线（GA），100% Beta 测试用户反馈"直观或非常直观"；Appian Composer 已被 130+ 组织用于构建 1300+ 应用 [Appian 官方公告](https://appian.com/about/explore/press-releases/2025/appian-launches-new-ai-capabilities-to-automate-complex-work "2025年11月")。
- ServiceNow Now Assist 将 GenAI 嵌入全线产品，开发了自有领域特定 LLM（Now LLM），同时支持 Azure OpenAI、Gemini、WatsonX 等第三方模型 [ServiceNow 官网](https://www.servicenow.com/platform/now-assist.html "Now Assist platform overview")。
- Forrester 明确判断"AI 不会杀死低代码市场"，认为自然语言将成为低代码平台的关键互补性开发体验，但不能替代可视化开发工具 [Forrester Blog](https://www.forrester.com/blogs/new-research-will-ai-kill-the-low-code-market/ "Will AI Kill The Low-Code Market, 2023年9月")。
- G2 研究指出 AI 代码生成与低代码短期各有使用场景，但预测 AI 代码生成最终将改变低代码概念本身——问题是"何时"而非"是否" [G2 Research](https://research.g2.com/insights/ai-code-generation-to-replace-low-code "Will AI Code Generation Replace Low Code")。
- AI 编码工具与低代码平台正从不同起点向对方领域趋同：Cursor 约 35% 的 PR 已由 agent 在独立虚拟机上生成，同时低代码平台全面整合 GenAI 和 agent 能力 [CNBC](https://www.cnbc.com/2026/02/24/cursor-announces-major-update-as-ai-coding-agent-battle-heats-up.html "Cursor agent updates")。
- Gartner 预测到 2026 年末 40% 的企业应用将集成任务特定 AI agent（2025 年不到 5%）；到 2035 年 Agentic AI 可驱动约 30% 的企业应用软件收入（超 4500 亿美元）[Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 "2025年8月")。
- Gartner 将"AI 原生开发平台"列为 2026 年十大战略技术趋势之一，预测到 2030 年 80% 的组织将大型软件工程团队转变为更小更灵活的 AI 增强团队 [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-10-20-gartner-identifies-the-top-strategic-technology-trends-for-2026 "2025年10月")。
- Gartner 在 2025 年 LCAP MQ 中预测"到 2028 年全球五分之四的企业将通过企业 LCAP 实施 Agentic AI"，LCAP 被视为 Agentic AI 落地的主要基础设施 [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/microsoft-recognized-as-a-leader-in-the-2025-gartner-magic-quadrant-for-enterprise-low-code-application-platforms/ "引述Gartner MQ报告")。
- Gartner 描述 Agentic AI 五阶段演进路径：AI 助手嵌入（2025）→任务特定 agent（2026, 40%）→协作式 AI agent（2027）→跨应用 agent 生态系统（2028）→民主化企业应用新常态（2029, 50%+ 知识工作者拥有 agent 协作技能）[Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 "Agentic AI五阶段路径")。
- 国内平台竞争激烈：钉钉推出超过 200 个 AI 助理，飞书升级 AI Agent 平台"飞书 Aily"和低代码"AI 专区"[新浪财经](https://finance.sina.cn/stock/jdts/2025-07-14/detail-inffmyaq2952174.d.html "飞书钉钉正面硬刚, 2025年7月")。

### 可用图片
- 无

### 仍需补充
- GitHub Copilot 2600 万用户数据的一手确认（当前来自 CNBC 对 Nadella 发言转述）
- Gartner"4/5 企业通过 LCAP 实施 Agentic AI"预测的付费报告原文确认
- Forrester 2024-2025 年关于 AI 与低代码关系的最新完整报告
- 国内平台（钉钉/飞书）AI 集成的官方一手公告
- Amazon CodeWhisperer（现 Amazon Q Developer）最新采用率数据
- AI 对"公民开发者"vs"专业开发者"差异化影响的定量调研

---

## Chapter 6：企业采用策略与落地实践——从决策到治理的全链条
### 研究目标
- 建立企业评估是否采用 LCNC 平台的决策框架与关键评估维度
- 提炼成功落地案例的共性最佳实践与失败案例的共性教训
- 设计 LCNC 治理体系框架（赋能业务与控制风险的平衡）

### 关键发现
- Gartner 2025 年 MQ for Enterprise LCAP 以"执行能力"和"愿景完整性"两大维度评估 12 家厂商；入选门槛包括 LCAP 年收入至少 6000 万美元且拥有 100 家以上大型企业客户 [Pretius Gartner LCAP 分析](https://pretius.com/blog/gartner-quadrant-low-code "2025 Gartner MQ详细解读")。
- Forrester 2025 Wave™ 采用 39 项评估标准，数据建模与管理、集成能力和数字流程自动化各占 10% 权重为最高三项 [OutSystems Forrester Wave 解读](https://www.outsystems.com/blog/posts/recognized-forrester-wave-low-code/ "OutSystems对Forrester Wave Q2 2025的解读")。
- PwC Italy CoE 学术研究提出五维度结构化选型框架（BPO、UCF、I&I、G&S、AEA），实证发现金融服务业最重治理与安全（28%），制造业最重集成（26%），框架应用后决策信心提升 30%-40%，评估周期缩短 25%-35% [Lamanna, PwC Italy](https://www.researchgate.net/publication/396747680_A_Structured_Evaluation_Framework_for_Low-Code_Platform_Selection_A_Multi-Criteria_Decision_Model_for_Enterprise_Digital_Transformation "2025年发表")。
- Gartner 2025 年标注三大趋势：AI 辅助开发成为领导者关键差异化能力、融合团队成为核心受众、治理与合规从差异化优势演变为基线要求 [Kissflow Gartner 分析](https://kissflow.com/low-code/gartners-magic-quadrant-about-low-code-vs-no-code-2025/ "Gartner 2025 MQ三大趋势")。
- 金融案例：FirstBank 使用 Appian 构建 AML 系统，从构想到上线仅 12 周，每年节省 1,000 工时，实现 100% AML 合规率 [Appian 案例](https://appian.com/blog/acp/low-code/low-code-examples "Appian官方案例集")。
- 国防案例：美国空军使用 Appian 开发 CON-IT 合同撰写系统，取代超 100 个遗留系统/环境，耗时仅 9 个月，节省 8,300 万美元 [Appian 案例](https://appian.com/blog/acp/low-code/low-code-examples "美国空军CON-IT案例")。
- 保险案例：Aviva（3,300 万客户、16 个国家）使用 Appian 将 22 个独立系统整合为呼叫中心单一统一界面，客户服务响应速度提升 9 倍 [Appian 案例](https://appian.com/blog/acp/low-code/low-code-examples "Aviva Insurance案例")。
- Power Apps Premium TEI 研究（2024 年 7 月，复合组织 30,000 员工/100 亿美元年收入）：三年 ROI 206%，NPV 3,100 万美元，第三年累计节省超 100 万工时 [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/millions-of-hours-saved-50-faster-app-development-and-206-roi-achieved-with-microsoft-power-apps-premium/ "Forrester TEI 2024年7月")。
- Mendix TEI 显示三年总净收益超 2,000 万美元：应用交付节省 808 万、运营效率节省 597 万、客户参与度 314 万、上市加速 333 万美元 [Mendix TEI 博客](https://www.mendix.com/blog/quantifiable-impact-how-todays-enterprise-landscape-benefits-from-low-code/ "Forrester TEI of Mendix")。
- OutSystems TEI 显示三年 ROI 506%，NPV 1,477 万美元：应用开发维护节省 550 万、业务增长 460 万、运营效率 670 万美元 [OutSystems TEI](https://www.outsystems.com/news/tei-low-code-roi/ "Forrester TEI of OutSystems")。
- Power Platform 整体 TEI（2024 年 7 月）：三年总收益 1.182 亿美元，NPV 8,170 万美元，ROI 224% [Forrester TEI of Power Platform](https://tei.forrester.com/go/Microsoft/PowerPlatform2024/ "Forrester TEI 2024年7月")。
- Panorama Consulting（2026 年 3 月）指出低代码平台已成"新型影子 IT"主要来源，典型失控模式包括：财务团队自建例外审批路径、HR 搭建案件管理工具、运维构建服务请求工作流——造成同一流程多个版本且控制假设和问责结构不同 [Panorama Consulting](https://www.panorama-consulting.com/the-new-shadow-it-low-code-platforms/ "2026年3月")。
- LCNC 平台十大常见失败模式：有限灵活性和定制能力、扩展性差、集成能力浅层化、安全合规不足、厂商锁定、平台特定技能不可迁移、知识瓶颈、技术债积累、不一致实践、隐性成本 [Dagster Blog](https://dagster.io/blog/why-no-code-solutions-almost-always-fail "技术分析角度的失败模式汇总")。
- Gartner 建议将公民开发活动划分为"绿色/黄色/红色"三区治理框架：绿色区可自由创建，黄色区协作构建，红色区需 IT 全面监督 [CIO.com](https://www.cio.com/article/189651/8-tips-for-managing-low-code-citizen-developers.html "Gartner分析师Jason Wong的三区治理建议")。
- Forrester 分析师提出三种公民开发管理策略：小型自治团队、自助服务模式、联邦模式（最成熟，由 CoE 管理平台并实施护栏）[CIO.com](https://www.cio.com/article/189651/8-tips-for-managing-low-code-citizen-developers.html "Forrester分析师Bratincevic")。
- Microsoft Power Platform 采用三区治理模型并于 2025 年 7 月扩展到 AI Agent：Zone One（个人生产力/隔离实验）、Zone Two（协作/团队级开发）、Zone Three（企业托管/生产级）[Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2025/07/31/evolving-power-platform-governance-for-ai-agents/ "2025年7月治理博客")。
- 成功的 LCNC CoE 应包含推广冠军、战略师、治理负责人、运营专家等角色；70% 的零编程背景开发者在一个月内学会使用低代码平台 [Kissflow CoE 指南](https://kissflow.com/no-code/how-to-set-up-a-no-code-coe/ "Kissflow关于建立无代码CoE的框架")。
- 低代码适合场景：内部业务应用、流程自动化、客户门户、MVP、遗留系统现代化；不适合场景：复杂算法、极端规模性能要求、完全定制 UI/UX、深度代码控制 [LogRocket Blog](https://blog.logrocket.com/low-code-decision-guide/ "2025年7月低代码决策指南")。
- Gartner 分析师建议不要强制标准化到单一低代码平台，而应依赖治理框架让业务用户选择适合其需求的工具 [CIO.com](https://www.cio.com/article/189651/8-tips-for-managing-low-code-citizen-developers.html "Gartner分析师混合策略建议")。
- Panorama Consulting 建议四步恢复流程治理：指派跨职能高管负责人、按关键性分类应用、要求涉及业务规则变更的应用进行设计审查、为临时性工具建立退役规则 [Panorama Consulting](https://www.panorama-consulting.com/the-new-shadow-it-low-code-platforms/ "2026年3月治理建议")。

### 可用图片
- 无

### 仍需补充
- Gartner 付费治理专题报告原文（"How to Effectively Govern Low-Code Platforms"等）
- 公开署名的大型企业弃用/迁移低代码平台的详细案例报告
- KPMG 公民开发者治理白皮书完整内容
- 中国市场 LCNC 平台采用落地案例（如钉钉宜搭、简道云、明道云等）

---

## Chapter 7：前景展望——低代码/无代码的演进路径与产业格局预判
### 研究目标
- 预判 LCNC 平台的技术演进方向与未来 1-3 年的关键突破点
- 回答"完全低代码化"的可行性范围与长期依赖传统编码的场景
- 分析产业格局演变趋势（平台整合、开源 vs 闭源、AI 原生平台的颠覆潜力）

### 关键发现
- Gartner 将"AI 原生开发平台"列为 2026 年十大战略技术趋势，预测到 2030 年 80% 的组织将大型软件工程团队演变为 AI 增强的更小更灵活团队；到 2030 年 40% 的企业应用组合将由 AI 原生开发平台构建的自定义应用组成 [Gartner 2026 战略技术趋势](https://www.gartner.com/en/newsroom/press-releases/2025-10-20-gartner-identifies-the-top-strategic-technology-trends-for-2026 "2025年10月20日")。
- Forrester 2024 年 5 月提出"应用生成平台"（AppGen）概念，将整合软件分析、开发、安全、测试和交付各步骤，核心创作体验为自然语言提示与视觉媒介的迭代循环，估计 3 年内成熟 [Forrester AppGen 报告](https://www.forrester.com/blogs/the-rise-of-application-generation-platforms/ "2024年5月7日")。
- Forrester 分析师 2026 年 2 月进一步指出"AppGen 正在吞噬低代码"，但明确表态"这不是开发者的终结"——AppGen 能加速创建但无法替代业务上下文理解、合规治理和人类判断力 [Forrester AppGen 博文](https://www.forrester.com/blogs/appgen-is-eating-low-code-what-it-means-to-you/ "2026年2月5日")。
- Gartner 预测到 2026 年末 40% 的企业应用将集成任务专用 AI Agent（2025 年不到 5%）；到 2035 年 Agentic AI 可驱动约 30% 的企业应用软件收入（超 4500 亿美元）[Gartner Agentic AI 预测](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 "2025年8月26日")。
- Mordor Intelligence 预测 2025 年全球低代码开发平台市场估值 263 亿美元，到 2030 年达 671.2 亿美元，CAGR 20.61%，与 Gartner 2029 年 582 亿美元（CAGR 14.1%）可交叉验证 [Mordor Intelligence](https://finance.yahoo.com/news/low-code-development-platform-market-093200522.html "2025年10月24日")。
- 开源低代码/AI 平台生态活跃：n8n（约 157k GitHub stars）、Dify（约 119k）、NocoDB（约 59k）、Appsmith（约 38k）、ToolJet（约 37k），呈现三大分化方向——业务应用构建器、AI 工作流/Agent 编排、数据表应用 [NocoBase 开源平台盘点](https://www.nocobase.com/en/blog/14-ai-low-code-platforms-github "2026年1月更新")。
- 开源低代码存在"伪开源"争议：部分平台自托管版本存在实质性功能限制，完整功能需付费 [Reddit 讨论](https://www.reddit.com/r/selfhosted/comments/1f4mb9b/genuinely_opensource_selfhostable_lowcode/ "开源低代码平台真实性讨论")。
- Morgan Stanley Research 认为 AI 将提升生产力并带动更多开发者招聘而非取代；软件开发者岗位预计扩大，增速范围从美国劳工统计局年均 1.6%（至 2033 年）到 IDC 年均 10%（至 2029 年）[Morgan Stanley](https://www.morganstanley.com/insights/articles/ai-software-development-industry-growth "How AI Coding Is Creating Jobs, 2025年10月29日")。
- Gartner 2025 年 7 月调查（700+ CIO）：到 2030 年 0% 的 IT 工作将由人类独立完成，75% 由 AI 增强人类完成，25% 完全由 AI 独立完成；AI 到 2028 年创造的就业将多于其消灭的 [Gartner IT 工作调查](https://www.gartner.com/en/newsroom/press-releases/2025-11-10-gartner-survey-finds-artificial-intelligence-will-touch-all-information-technology-work-by-2030 "2025年11月10日")。
- Gartner 指出 AI 将使某些技能变得不那么重要，但创造全新技能需求——"不是关于更好地执行任务，而是关于成为更好的激励者、思考者和沟通者"[Gartner IT 工作调查](https://www.gartner.com/en/newsroom/press-releases/2025-11-10-gartner-survey-finds-artificial-intelligence-will-touch-all-information-technology-work-by-2030 "2025年11月")。
- 中国低/零代码市场规模从 2021 年 31.0 亿元增长至预计 2029 年 131.2 亿元，约 61% 的组织用户认可低代码价值并愿意持续投资；76% 的用户希望通过 GenAI 提升开发效率，67% 关注降低成本 [腾讯云开发者社区](https://cloud.tencent.com/developer/article/2576443 "AI时代下中国低代码市场发展研究, 2025年10月")。
- 中国市场差异化行业需求：金融最重视合规与系统集成，制造聚焦生产流程与 IoT，零售追求快速迭代与高并发；65% 用户关注体验与学习成本，57% 关注功能拓展性，52% 关注 AI 赋能水平 [腾讯云开发者社区](https://cloud.tencent.com/developer/article/2576443 "AI时代下中国低代码市场发展研究")。
- Microsoft 收购 Clear Software 强化跨平台集成和工作流自动化能力，体现大厂通过并购补齐生态短板的趋势 [ChannelE2E](https://www.channele2e.com/news/microsoft-buys-oracle-salesforce-sap-workflow-automation-startup "Microsoft Acquires Clear Software")。
- Gartner Agentic AI 五阶段演进路径：AI 助手（2025）→ 任务专用 Agent（2026, 40%）→ 应用内协作 Agent（2027）→ 跨应用 Agent 生态系统（2028, 1/3 用户体验从原生应用转向 Agentic 前端）→ 民主化企业应用新常态（2029, 50%+ 知识工作者具备 Agent 协作技能）[Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 "Agentic AI五阶段")。
- Gartner 预测到 2028 年超过 50% 的企业 GenAI 模型将是领域专用的（DSLMs），将深刻影响低代码平台的 AI 能力架构 [Gartner 2026 战略技术趋势](https://www.gartner.com/en/newsroom/press-releases/2025-10-20-gartner-identifies-the-top-strategic-technology-trends-for-2026 "Gartner Top Strategic Trends")。

### 可用图片
- 无

### 仍需补充
- Gartner "Software Engineering 2030" 完整六大立场（付费内容，仅获取摘要）
- Fortune Business Insights 2034 年 3769 亿美元预测与 Gartner 口径差异的方法论确认
- 中国市场 2021-2029 年预测的一手报告来源确认（当前为 T3 来源转引）
- 中国 AI 代码生成市场数据（65 亿→330 亿元）的原始券商研报确认
- 2024-2026 年 LCNC 领域系统性并购事件清单

---

# Section 2：给 Write 阶段的执行建议

## 术语定义与分类标准统一
- 全文在 Chapter 1 中明确建立"低代码"与"无代码"的定义边界，后续各章统一使用。**低代码**面向有编程基础的开发者，提供可视化开发环境同时保留代码扩展能力；**无代码**面向业务人员，完全通过图形化界面完成应用构建，不要求编程能力。
- 统一缩写规范：首次出现写全称"低代码/无代码（Low-Code/No-Code，以下简称 LCNC）"，后续统一使用"LCNC"。
- "公民开发者"（Citizen Developer）在 Chapter 2 首次使用时给出定义，后续章节直接引用。

## 章节间逻辑衔接
- Chapter 1→2→3 构成"全景→正面→反面"的辩证递进。
- Chapter 4 是 Chapter 2 和 Chapter 3 的"观点整合层"，需显式引用前两章关键论据。
- Chapter 5 是全文的"时间维度变量"，需适当回溯前文论点。
- Chapter 6 自然承接 Chapter 3（风险应对）和 Chapter 4（分歧协调）的结论。
- Chapter 7 综合所有前序章节的关键发现支撑展望判断。

## 平衡性与多元视角
- 每个核心判断都需同时呈现支持证据和反对/质疑证据。
- Chapter 4 须避免隐性偏向管理者或开发者任一方。
- 中国市场与海外市场需注意差异性描述，避免将海外数据直接套用到中国语境。
- 行业案例的选取应覆盖不同行业和企业规模。

## 数据与判断的审慎性
- 市场规模数据需注意不同来源口径差异（如 Fortune Business Insights 与 Precedence Research 对同一年估值可能差异数倍），选定主要数据源并说明口径差异。
- Chapter 7 的前瞻判断必须以已核验趋势数据为基础，展望性表述使用"预计""有望"等审慎措辞。
- 所有效率提升的百分比数据均需标注样本来源与统计口径。

## 跨章节统一口径的要点
- "效率提升"的衡量标准在 Chapter 2 定义（开发周期缩短、交付速度、人力投入减少等），Chapter 4-7 引用时保持一致。
- "技术债"的界定在 Chapter 3 明确范围（代码层面 + 架构、运维、安全等维度），全文统一。
- "适用场景 vs 不适用场景"的分类框架在 Chapter 2 首次建立、Chapter 3 反向验证、Chapter 6 实践建议复用、Chapter 7 展望引用。
- 对 AI 影响的讨论集中在 Chapter 5，但 Chapter 2（AI 对效率的二次提升）、Chapter 7（AI 改变 LCNC 格局）也会涉及，需保持 AI 角色定位的一致性论述。

## 中国与全球市场的差异化处理
- 中国 LCNC 市场在平台生态、政策环境、企业数字化基础等方面与欧美市场存在显著差异。
- Chapter 1 市场概览中设置中国市场专门段落，后续引用中国案例或数据时明确标注地域口径。
