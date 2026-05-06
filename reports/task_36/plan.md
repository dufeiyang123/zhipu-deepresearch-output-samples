# 研究计划：单件小批量离散制造中技能密集型工序的自动化难度调研

> **研究时间口径**：以 2026 年 4 月为锚点，回顾 2021-2026 年技术与产业进展，展望 2026-2030 年趋势。

---

# Section 1：章节研究计划

## Chapter 1：单件小批量离散制造的问题域界定
### 研究目标
- 明确"离散制造—单件小批量（HMLV）"的产业范畴与典型行业，将其与大批量流水线和流程工业做清晰边界切割
- 刻画单件小批量生产模式的核心特征：产品高度定制化、工艺路线多变、批量小至一件、工装夹具频繁切换、对工人经验与现场判断的高度依赖
- 量化该领域的产业规模与劳动力结构概况（全球/中国就业人数量级、技能工人占比等），为后续章节的经济分析提供基线

### 关键发现
- 离散制造以可计数独立单元为产出，流程制造通过配方/连续工艺将原材料转化为不可逆产品；HMLV 制造指产品品种多、单品种批量小（单批次从一件到数千件不等），典型应用于航空航天零部件、医疗器械定制件等领域。[Lumafield](https://www.lumafield.com/article/what-is-high-mix-low-volume-hmlv-manufacturing "HMLV Manufacturing定义，2024年8月")
- MIT 硕士论文对 HMLV 给出操作定义：以 PSI Control Solutions 为例，634 种产品编码在 12 个月内仅生产 346 件、涉及 80 种独特编码，体现工艺路线多变、高度依赖工人经验判断的典型特征。[MIT LGO Thesis](https://dspace.mit.edu/bitstream/handle/1721.1/139593/rodriguez-andrewrd-sm-meche-2021-thesis.pdf "Rodriguez, Applying Lean to HMLV MTO, MIT 2021")
- HMLV 制造面临四大核心挑战：频繁换产的生产复杂度、小批量多品种质量保证困难、组件品种多但单品用量少的库存管理困难、无法获得规模经济导致的高单件成本。[Lumafield](https://www.lumafield.com/article/what-is-high-mix-low-volume-hmlv-manufacturing "HMLV Manufacturing定义，2024年8月")
- 2024 年全球制造业增加值约 16.82 万亿美元（现价）。[Trading Economics/世界银行](https://tradingeconomics.com/world/manufacturing-value-added-us-dollar-wb-data.html "全球制造业增加值，2024年数据，来源世界银行")
- 中国制造业增加值 2022 年占全世界约 30.2%，连续 15 年保持全球第一；2024 年全部工业增加值 40.5 万亿元人民币。[新华社](http://www.news.cn/fortune/20240910/6a24560a504b41f8b5bff8114684d6c9/c.html "我国制造业增加值占全球比重约三成，2024年9月")
- 典型 HMLV 行业全球规模：航空航天零部件约 1,002—1,022 亿美元（2025 年）[AIA](https://www.aia-aerospace.org/news/american-aerospace-defense-industry-continues-economic-dominance/ "AIA 2025年数据")；船舶制造约 1,152—1,572 亿美元（2024-2025 年）[Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/ship-building-market "全球造船市场")；模具与工装约 2,906—2,930 亿美元（2025 年）[IMARC Group](https://www.imarcgroup.com/tooling-market "全球工装市场")；医疗器械约 6,789 亿美元（2025 年）[Precedence Research](https://www.precedenceresearch.com/medical-devices-market "全球医疗器械市场")；发电设备约 993 亿美元（2024 年）[Market.us](https://market.us/report/global-power-generation-equipment-market/ "全球发电设备市场")
- 截至 2025 年 12 月，美国制造业就业约 1,269 万人（BLS 季调）。2024—2033 年美国制造业净新增岗位需求约 380 万个，其中约 190 万个（约 50%）可能因技能缺口无法填补。[Deloitte/Manufacturing Institute](https://www.deloitte.com/us/en/insights/industry/manufacturing-industrial-products/supporting-us-manufacturing-growth-amid-workforce-challenges.html "2024年人才研究") [FRED/BLS](https://fred.stlouisfed.org/series/MANEMP "美国制造业就业，2026年2月")
- 美国焊工约 42.2 万人（BLS 2023 年 5 月），焊接专业人员约 77.1 万人（AWS），2024—2028 年需新增约 33 万名焊接专业人员。[BLS](https://www.bls.gov/oes/2023/may/oes514121.htm "BLS OES焊工数据") [AWS](https://weldingworkforcedata.com/ "AWS焊接劳动力数据，2025年")
- 中国制造业十大重点领域至 2025 年人才缺口近 3,000 万人（缺口率 48%）；截至 2021 年底高技能人才超 6,000 万人，缺口达 2,000 万人。[人民论坛](https://paper.people.com.cn/rmlt/pc/content/202411/18/content_30047208.html "高技能人才供给，2024年11月")
- Deloitte/MI 研究指出，先进制造业中 40% 的当前技能要求将在未来五年内发生变化，但数字技能不够——高度专业化领域（金属结构件、航空航天）中操作焊接机器人仍需扎实的制造基础技能（如焊接经验）。[Deloitte/Manufacturing Institute](https://www.deloitte.com/us/en/insights/industry/manufacturing-industrial-products/supporting-us-manufacturing-growth-amid-workforce-challenges.html "2024年人才研究")

### 可用图片
- 无本地图片资源

### 仍需补充
- 单件小批量占离散制造的产值/就业比重缺乏权威量化来源，建议寻找 McKinsey/BCG 关于 MTO/ETO 占制造业比重的定量估计
- 全球制造业就业的离散 vs. 流程细分数据缺失
- 中国高技能人才存量数据截止至 2021 年底，2022—2025 年更新数据尚未找到一手来源
- 各 HMLV 行业中技能工人的年龄结构数据不足（仅 AWS 有焊工年龄分布）
- 中国单件小批量制造的产业比重缺乏权威来源
- 能源装备中核电设备、风电主轴等典型单件小批量产品的独立市场规模数据缺失

---

## Chapter 2：技能密集型工序的识别与分类
### 研究目标
- 系统梳理单件小批量制造中高度依赖工人个人技能的关键工序（手工焊接、手工装配、目视检测、复杂夹具调整、工艺参数现场调优、手工打磨抛光、管路线缆布线等）
- 解析每类工序中工人技能的具体构成（感知判断、手眼协调、隐性经验知识、现场即兴决策），识别最难被形式化和编码化的技能要素
- 构建"技能依赖—自动化难度"矩阵，作为全文分析主线

### 关键发现
（待 researcher 补研后填写）

### 可用图片
（待 researcher 补研后填写）

### 仍需补充
（待 researcher 补研后填写）

---

## Chapter 3：自动化替代的技术可行性评估
### 研究目标
- 针对第二章识别的各类技能密集型工序，逐一评估当前可用自动化技术的成熟度与适用性
- 分析关键使能技术进展与瓶颈：协作机器人、力控与自适应控制、机器视觉与三维感知、AI 驱动工艺参数优化、离线编程/数字孪生、增材制造替代等
- 识别"最后一公里"问题：非结构化环境适应、小批量编程/调试成本、传感与感知在复杂工况下的可靠性

### 关键发现
（待 researcher 补研后填写）

### 可用图片
（待 researcher 补研后填写）

### 仍需补充
（待 researcher 补研后填写）

---

## Chapter 4：自动化替代的经济可行性与组织障碍
### 研究目标
- 分析单件小批量场景下自动化投资的经济逻辑：高换型成本、低批量摊薄效应弱、ROI 回收周期长等结构性障碍
- 评估不同自动化方案的成本结构（设备采购、系统集成、编程调试、维护培训），与现有人工成本对比
- 剖析非经济障碍：组织惯性、隐性知识难以转移、中小企业数字化基础薄弱、供应链碎片化、行业认证门槛

### 关键发现
（待 researcher 补研后填写）

### 可用图片
（待 researcher 补研后填写）

### 仍需补充
（待 researcher 补研后填写）

---

## Chapter 5：行业实践案例与经验教训
### 研究目标
- 通过 3-5 个代表性案例展示单件小批量场景中自动化落地的真实路径、成效与教训
- 涵盖不同行业（航空航天、船舶、模具/医疗器械等）和不同技术路线（协作机器人、视觉检测、数字孪生等）
- 提炼成功案例共性模式与失败案例典型陷阱

### 关键发现
（待 researcher 补研后填写）

### 可用图片
（待 researcher 补研后填写）

### 仍需补充
（待 researcher 补研后填写）

---

## Chapter 6：趋势展望与战略建议
### 研究目标
- 研判未来 3-5 年（2026-2030）单件小批量制造自动化的技术演进方向与产业变革趋势
- 明确当前的"不可替代区"（中短期仍高度依赖人工技能的工序）与"优先自动化区"
- 提出面向不同利益相关方（制造企业、技术供应商、政策制定者、职业教育机构）的分层战略建议

### 关键发现
（待 researcher 补研后填写）

### 可用图片
（待 researcher 补研后填写）

### 仍需补充
（待 researcher 补研后填写）

---

# Section 2：给 Write 阶段的执行建议

## 术语口径统一
- **离散制造（Discrete Manufacturing）**：以可计数的独立单元为产出的制造方式，区别于流程制造。全文统一使用"离散制造"，首次出现时附英文。
- **单件小批量（High-Mix Low-Volume, HMLV）**：产品品种多、单品种批量小（通常单批次不超过数十件，常至一件）。全文统一使用"单件小批量"，首次出现附"HMLV"。
- **技能密集型工序（Skill-Intensive Process）**：高度依赖工人个人经验、手眼协调、感知判断和隐性知识的制造工序。全文统一使用"技能密集型工序"，首次出现附英文。
- **隐性知识（Tacit Knowledge）**：工人通过长期实践积累的、难以用文字或规则完全表述的操作经验和判断能力。
- **协作机器人（Collaborative Robot / Cobot）**：可与人类在共享工作空间中安全协作的机器人。全文统一使用"协作机器人"，可简称"cobot"。
- **离线编程（Offline Programming, OLP）**：在不中断生产的情况下，通过软件仿真环境生成机器人程序。

## 跨章一致性要求
- 第一章界定的行业范畴和术语定义是全文基线，后续各章引用行业案例时必须落在第一章框定的范围内
- 第二章的"技能依赖—自动化难度"矩阵贯穿第三、四、六章反复引用，保持分析框架连贯性
- 第三章（技术可行性）和第四章（经济可行性）使用一致的工序分类口径，与第二章严格对齐
- 第五章案例必须能回溯到第二章的工序类型和第三/四章的评估结论
- 第六章的趋势判断和建议必须有前五章的事实基础支撑

## 数据引用注意事项
- 核心量化数据须标注来源、时间点和口径，优先引用 T1/T2 来源
- 权威数据源：IFR 年度报告、McKinsey/BCG/Deloitte 制造业自动化研究、各国统计局制造业数据、AWS（美国焊接学会）、CIRP 技术报告
- 中国数据：工信部智能制造统计、中国机器人产业联盟、《中国制造2025》评估报告
- 案例数据应引用企业披露、学术论文或权威媒体的具体数字
- TRL 评估如无权威来源直接定级，需说明评估依据

## 行文风格建议
- 区分"技术可行性"（能不能做到）和"经济可行性"（值不值得做）两个维度，不可混为一谈
- 避免非黑即白的结论，以证据为基础给出审慎、分层的判断
- 承认不确定性：对缺乏充分数据支撑的判断使用"我们认为""预计""有望"等审慎表述
- 图表应作为论证核心工具，每章建议至少 1-2 个有信息量的图表（矩阵图、对比表、TRL 雷达图等）
