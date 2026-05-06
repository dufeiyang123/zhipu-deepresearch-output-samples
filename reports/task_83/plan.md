# Section 1：章节研究计划

## Chapter 1：Device Taxonomy & Form-Factor Landscape

### 研究目标
- 建立平板式支付/SaaS设备的完整分类体系（smart POS、mPOS tablet、tablet kiosk、all-in-one countertop、rugged field tablet），为后续章节提供统一术语
- 厘清"smart POS terminal"（集成打印/扫码/NFC的Android/Linux设备）与"通用平板+POS软件"（如iPad+读卡器）的边界
- 梳理各形态对应的外设生态（读卡器、打印机、扫码枪、钱箱、客显）
- 概述主流操作系统与平台分布（Android AOSP、Android GMS、iOS/iPadOS、Linux、Windows IoT）

### 关键发现
- PCI PTS POI v6.1 将支付设备分为 stand-alone POS terminal、UPT（无人值守支付终端）、EPP（加密PIN pad）、SCR/SCRP（安全读卡器）及 non-PED POI。同时将 COTS 定义为"面向大众市场的移动设备（如智能手机或平板），非专门为支付处理设计" [PCI SSC PTS POI v6.1](https://listings.pcisecuritystandards.org/documents/PCI_PTS_POI_SRs_v6-1_Final.pdf "PCI PTS POI安全要求v6.1, 2022年3月")。
- PCI SSC 发布了三套 COTS 支付标准：CPoC（仅限NFC非接触受理）、SPoC（COTS触屏PIN输入+外接PCI认证读卡器）、MPoC（2022年11月发布的模块化标准，整合并取代前两者）[U.S. Payments Forum](https://www.uspaymentsforum.org/introduction-to-mpos-and-taptomobile-solutions/ "Introduction to mPOS and TapToMobile Solutions, 2023年4月")。
- EMVCo 通过 Tag 9F35（Terminal Type）使用两位数代码分类终端：Types 21/22 为有人值守商户POS，Types 24/25/26 为无人值守终端（kiosk/自动售货），Types 34/35/36 为持卡人自助设备（SoftPOS）[MST Company](https://mstcompany.net/blog/acquiring-types-of-pos-terminals-classification-of-emvco-and-payment-systems "EMVCo POS终端类型分类")。
- 本报告提出五类互斥形态分类：(1) Smart POS Terminal — 5"–8"屏、集成打印/NFC/EMV/MSR/扫码的PCI认证Android/Linux设备；(2) mPOS Tablet — 通用COTS平板+外接读卡器；(3) Tablet Kiosk — 10"–32"平板固定安装于自助服务外壳；(4) All-in-One Countertop POS — 10"–22"大屏集成收银站含客显；(5) Rugged Field Tablet — IP65/67/68+MIL-STD-810G/H认证的户外/现场作业加固平板。该分类体系与 PAX Technology 的产品线划分（Android SmartPOS → Mobile/MiniPOS/Countertop, SmartTablet → Multilane, Unattended → IM/SK系列）相互印证 [PAX Technology](https://www.paxglobal.com.hk/en/latest-news/is-softpos-the-payment-industry-s-hot-new-thing/ "PAX产品线分类")。
- U.S. Payments Forum 正式区分三种受理方式：(1) Traditional POS — 专用支付设备；(2) mPOS — COTS设备+外接读卡/PIN输入/打印硬件；(3) TapToMobile — 仅利用COTS设备内置NFC完成非接触交易 [U.S. Payments Forum](https://www.uspaymentsforum.org/introduction-to-mpos-and-taptomobile-solutions/ "Introduction to mPOS and TapToMobile Solutions, 2023年4月")。
- 2024年全球共出货 1.281 亿台 PCI 认证 POS 终端，另有 3,690 万台非PCI认证设备出货（其中QR码读取器占63.35%，dongle占24.48%）[Nilson Report Issue 1296](https://nilsonreport.com/articles/pos-terminal-manufacturer-shipments-worldwide-2024/ "2024年全球POS终端制造商出货量") [Nilson Report Issue 1297](https://nilsonreport.com/articles/pos-device-shipments-2024-part-2/ "2024年POS设备出货量-第二部分")。
- 2023年全球POS终端安装基数约 2.92 亿台；蜂窝POS终端安装基数达 1.461 亿台（53%出货设备含蜂窝连接），预计以9.4% CAGR增长至2028年的2.293亿台；mPOS终端安装基数 1.1 亿台，预计2028年达1.52亿台 [Berg Insight via BusinessWire](https://www.businesswire.com/news/home/20250428903740/en/Connected-POS-Terminals-Market-Report-2025-Installed-Base-of-Cellular-POS-Terminals-to-Reach-229-Million-in-2028-mPOS-Terminals-Worldwide-to-Reach-152-Million-Units-by-2028---ResearchAndMarkets.com "Berg Insight第8版连接POS终端报告, 2025年4月")。
- 2023年全球POS终端出货中约 40% 为Android POS终端，较2022年的27%显著上升。顶级Android SmartPOS制造商依次为 Sunmi、Tianyu、PAX Technology、Verifone、Castles Technology、Ingenico、Landi、Newland [Berg Insight via BusinessWire](https://www.businesswire.com/news/home/20250428903740/en/Connected-POS-Terminals-Market-Report-2025-Installed-Base-of-Cellular-POS-Terminals-to-Reach-229-Million-in-2028-mPOS-Terminals-Worldwide-to-Reach-152-Million-Units-by-2028---ResearchAndMarkets.com "Berg Insight第8版, 2025年4月")。
- SoftPOS（Tap-to-Phone）截至2023年运行设备数仍不到 1,000 万台，属新兴品类 [Berg Insight via BusinessWire](https://www.businesswire.com/news/home/20250428903740/en/Connected-POS-Terminals-Market-Report-2025-Installed-Base-of-Cellular-POS-Terminals-to-Reach-229-Million-in-2028-mPOS-Terminals-Worldwide-to-Reach-152-Million-Units-by-2028---ResearchAndMarkets.com "Berg Insight第8版, 2025年4月")。
- 各形态OS格局：Smart POS以Android为主（~40%出货且快速增长）；mPOS Tablet分为iOS/iPadOS阵营（Square、Lightspeed、Shopify POS）和Android阵营（Toast）；Tablet Kiosk存量中Windows占45–55%，但新出货中Android已占35–45%；All-in-One Countertop为Android/Windows/Linux三分；Rugged Field Tablet为Android与Windows并存 [Kiosk Industry/KMA](https://kioskindustry.org/which-os-for-my-kiosk-is-best/ "Which OS For My Kiosk Is Best?, 2025年12月")。
- PCI PTS认证是区分"支付终端"与"运行POS软件的商用平板"的核心分界线：PCI PTS认证设备需通过物理防篡改、固件认证、加密PIN处理等硬件级安全测试；COTS平板则受MPoC/CPoC/SPoC软件安全标准约束 [PCI SSC PTS POI v6.1](https://listings.pcisecuritystandards.org/documents/PCI_PTS_POI_SRs_v6-1_Final.pdf "PCI PTS POI v6.1物理/逻辑安全要求")。

### 可用图片
- 无本地图片可用
- 外部参考：Kiosk OS市场份额图 `https://kioskindustry.org/wp-content/uploads/2025/12/2025-OS-market-share-665x443.png`（2025年全球kiosk OS分布）

### 仍需补充
- Berg Insight 报告中 Android POS 终端的年度出货量绝对数字（而非仅百分比）为付费内容，缺乏具体出货量数据量化2024年Android SmartPOS出货规模
- Nilson Report Issue 1296/1297 的完整制造商出货排名和设备分类细分数据为订阅者专属
- IDC 对 POS 终端设备的正式分类框架未能通过公开渠道获取
- iOS/iPadOS 在POS领域的精确全球安装基数占比缺乏权威T1/T2来源
- 2024–2025年最新 Android POS 出货占比（可能已超过50%）尚无公开权威来源确认

---

## Chapter 2：Major Manufacturers & Device Portfolio

### 研究目标
- 编制 Tier-1 全球 OEM（PAX、Sunmi、Ingenico、Verifone、Newland、Clover/Fiserv、Square/Block、Toast 等）的平板形态设备产品线目录
- 汇总旗舰机型的核心硬件规格（屏幕尺寸、处理器、内存/存储、电池、连接性、支付受理方式、认证）
- 收录各区域/细分 OEM（Telpo、Bematech/TOTVS、Castles Technology、Elo Touch、BBPOS/Stripe 等）
- 跟踪 2025年4月–2026年10月窗口期内的新品发布与路线图
- 收集各主要设备的官方产品图片

### 关键发现
（待 researcher 补充）

### 可用图片
（待 researcher 补充）

### 仍需补充
（待 researcher 补充）

---

## Chapter 3：Primary Use Cases & Deployment Scenarios

### 研究目标
- 将各设备品类映射到真实部署场景：零售、餐饮/快餐、酒店、医疗、现场服务、交通、政务
- 区分 SaaS-first 部署模式（云端POS、订阅计费、自助点餐）与传统收单机构终端投放模式的设备需求差异
- 识别驱动新增部署的新兴场景（自助结账、桌边支付、路边/外卖、无人售卖、年龄验证、数字小费）
- 分析部署环境（柜台、移动/排队、户外、壁挂、顾客自助）对防护、电池、连接性的要求

### 关键发现
（待 researcher 补充）

### 可用图片
（待 researcher 补充）

### 仍需补充
（待 researcher 补充）

---

## Chapter 4：Regional Market Landscape — Penetration, Installed Base & Pricing

### 研究目标
- 量化四大目标区域（北美、日韩、东南亚、南美）截至2025年中的平板式POS/kiosk设备存量，及至2026年10月的预测存量
- 按区域统计市场收入和出货量规模，给出CAGR预期
- 整理各区域各品类的典型价格区间（硬件裸机 & 硬件+SaaS捆绑），统一以USD标注
- 梳理区域特有的监管、认证、基础设施因素（EMV强制令、QR码主导、税控/财政模块要求、连接性缺口）

### 关键发现
（待 researcher 补充）

### 可用图片
（待 researcher 补充）

### 仍需补充
（待 researcher 补充）

---

## Chapter 5：Competitive Dynamics & Value-Chain Analysis

### 研究目标
- 描绘从芯片到商户的完整价值链（芯片→ODM/OEM→软件平台→支付处理商/收单机构→ISV/VAR→商户），识别利润集中环节
- 分析关键厂商联盟与生态合作（PAX+支付网关、Sunmi+SaaS ISV、Clover+Fiserv 收单）
- 研究商业模式演进：硬件直购 vs. HaaS vs. SaaS捆绑订阅 vs. 收单机构补贴投放
- 跟踪2025年4月–2026年10月窗口期内的并购、战略投资、合作关系变动

### 关键发现
（待 researcher 补充）

### 可用图片
（待 researcher 补充）

### 仍需补充
（待 researcher 补充）

---

## Chapter 6：Forward Outlook & Strategic Implications

### 研究目标
- 研判未来12–18个月最可能重塑设备设计的技术趋势（端侧AI、生物识别、5G/eSIM、模块化硬件、可持续性/可回收）
- 分析支付标准演进（Tap-to-Phone/SoftPOS、CBDC就绪、离线非接触）对硬件需求的影响
- 识别各区域/垂直行业中被现有产品覆盖不足的空白机会
- 为考虑自建/合作/收购决策的硬件PM提供战略建议

### 关键发现
（待 researcher 补充）

### 可用图片
（待 researcher 补充）

### 仍需补充
（待 researcher 补充）

---

# Section 2：给 Write 阶段的执行建议

1. **术语一致性**：Chapter 1 须产出一张设备分类矩阵，后续所有章节中提及的设备都必须标注到 Chapter 1 定义的形态类别。统一使用 "smart POS""mPOS tablet""tablet kiosk""all-in-one countertop" 等写法。明确区分 "terminal"（支付认证设备）与 "tablet"（运行POS SaaS的通用平板）。

2. **区域划分统一**：全报告使用四区域框架——(1) North America: 美国+加拿大；(2) Japan & Korea: 仅日本+韩国；(3) Southeast Asia: ASEAN-10；(4) South America: 包含墨西哥、中美洲和加勒比地区的广义 LATAM。当来源数据使用不同区域分组时，须注明映射假设。

3. **货币与定价**：所有价格以 USD 标注，必要时括号内加本币等值（¥/₩/R$）。区分"硬件裸机MSRP""采购实际价格""硬件+SaaS捆绑价格"三种口径。

4. **数据密集度**：Chapter 4（市场规模/存量/定价）和 Chapter 5（并购/合作）对外部数据依赖最重，需 Nilson、Berg Insight、Juniper、Grand View Research、IDC 等来源。Chapter 2 中等依赖（厂商官网+新品报道）。Chapter 1 和 Chapter 3 最低依赖。

5. **交叉验证**：Chapter 4 存量数据 ↔ Chapter 5 市场份额须一致；Chapter 2 设备目录 ↔ Chapter 3 场景映射须完整覆盖；Chapter 4 定价 ↔ Chapter 5 商业模式须口径一致；Chapter 4 监管要求 ↔ Chapter 2 认证列须对应。

6. **文风与深度**：面向高级硬件PM受众，权威、数据驱动、分析性口吻。硬件规格需到BOM级（处理器系列、RAM/存储档位、连接射频、认证），但非工程数据手册——聚焦商业化差异。

7. **时间口径**：明确区分已观测数据（2025年4月至今）和前瞻性估计（当前至2026年10月）。引用分析师预测时注明发布日期与预测时间窗。

8. **图片规范**：Chapter 2 须包含各主要 OEM 和形态的代表性设备图片。图片来源为厂商新闻素材或官方产品页。每张图须注明厂商、型号、形态分类（按 Chapter 1 分类）和大致上市年份。
