# Section 1：章节研究计划

## Chapter 1: Origins and Context — The Rise of Agent Interoperability Protocols
### 研究目标
- Establish the technological and industry backdrop that motivated the creation of both MCP and A2A.
- Cover what each protocol is (MCP as Anthropic's Model Context Protocol released late 2024; A2A as Google's Agent-to-Agent protocol announced April 2025), the organizations behind them, and the state of AI-agent ecosystems at the time of their respective launches.
- Explain why standardized agent communication became an urgent industry need.

### 关键发现
- Anthropic 于 2024 年 11 月 25 日公开发布 MCP，将其定位为"AI 模型连接数据源和工具的通用开放标准"，采用客户端-服务器架构，旨在解决 LLM 应用与外部数据源/工具之间的"M×N 集成碎片化"问题。核心原语包括 Resources、Tools、Prompts，消息格式为 JSON-RPC 2.0。[Anthropic 官方博客](https://www.anthropic.com/news/model-context-protocol "Introducing the Model Context Protocol, 2024-11-25")
- MCP 初始发布即提供 Python 和 TypeScript SDK，以及面向 Google Drive、Slack、GitHub、Postgres 等的预构建服务器；首批客户端包括 Claude Desktop、Cursor、Sourcegraph Cody。Anthropic 将 MCP 类比为"AI 的 USB-C 端口"。[Anthropic 官方博客](https://www.anthropic.com/news/model-context-protocol "Introducing the Model Context Protocol, 2024-11-25")
- 2025 年 3 月 26 日，Anthropic 发布 MCP 重大更新：引入 Streamable HTTP 传输和 OAuth 2.1 认证，使 MCP 从本地开发工具演进为企业级协议。同时宣布 OpenAI、Google DeepMind、Microsoft、Amazon 等加入 MCP 生态。[Anthropic 官方博客](https://www.anthropic.com/news/model-context-protocol-enterprise "MCP 企业级更新公告, 2025-03-26")
- Google 于 2025 年 4 月 9 日在 Cloud Next '25 大会上发布 A2A 协议，定义为"使 AI 代理能够跨不同框架和供应商相互通信、安全交换信息并协调行动的开放协议"。发布时获得超过 50 家合作伙伴支持（Salesforce、SAP、Atlassian、LangChain 等）。[Google Cloud 博客](https://cloud.google.com/blog/products/ai-machine-learning/a2a-a-new-era-of-agent-interoperability "Announcing the Agent2Agent Protocol (A2A), 2025-04-09")
- A2A 五大设计原则：(1) 拥抱代理能力（代理作为不透明实体协作）；(2) 基于现有 Web 标准（HTTP、JSON-RPC 2.0、SSE）；(3) 默认安全；(4) 支持长时运行任务；(5) 模态无关。引入 Agent Card（`/.well-known/agent.json`）机制实现动态能力发现。由 Saurabh Tiwary 主导设计。[Google A2A GitHub](https://github.com/google/A2A "A2A 协议 GitHub 仓库")
- 2023-2025 年间，LLM 驱动的 AI 代理从单一对话系统快速演进为自治系统，LangChain、CrewAI、AutoGen、OpenAI Assistants API 等框架涌现，但各框架间缺乏统一互操作标准。之前的工具集成主要依赖各框架自定义的 API 封装和函数调用接口（如 OpenAI Function Calling、LangChain Tool 抽象），导致严重的集成碎片化。
- 历史上的代理互操作尝试包括 FIPA ACL（1990s-2000s，基于言语行为理论）、KQML（1990s）、W3C Web Services（WSDL/SOAP/UDDI）、OpenAPI/Swagger，但均未覆盖 LLM 代理所需的动态上下文管理和自主协作能力。[FIPA 官方标准](http://www.fipa.org/specs/fipa00061/SC00061G.html "FIPA ACL Message Structure Specification")
- Gartner 在 2025 年技术趋势预测中将 Agentic AI 列为年度十大战略技术趋势之首，预计到 2028 年至少 15% 的日常工作决策将由自主代理完成。[Gartner 2025 技术趋势](https://www.gartner.com/en/newsroom/press-releases/2024-10-21-gartner-identifies-the-top-10-strategic-technology-trends-for-2025 "Gartner Top 10 Strategic Technology Trends for 2025, 2024-10-21")
- Google 官方明确将 A2A 与 MCP 定位为互补关系（"better together"）：MCP 聚焦 Agent-to-Tool（代理与工具/数据的连接），A2A 聚焦 Agent-to-Agent（代理间自主协作）。[Google Developers 博客](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ "A2A 开发者博客, 2025-04-09")

### 可用图片
无

### 仍需补充
- OpenAI 在 2025 年 1 月宣布支持 MCP 的官方博客文章确切 URL 需确认（事件已知但缺 T1 链接）。
- Gartner/IDC 等机构关于 2025-2026 年 AI 代理市场规模和采用率的最新定量预测数据（当前引用为 2024 年 10 月预测，可能有更新版本）。
- 注：MCP 版本历史（5 版 + draft）和 A2A 版本历史（0.1.0→1.0.0）及 GitHub 指标已在 Chapter 2 和 Chapter 6 中补全，写作时可直接引用。

---

## Chapter 2: Architectural Design and Technical Comparison
### 研究目标
- Provide a rigorous side-by-side comparison of the two protocols across clearly defined technical dimensions: communication model, capability discovery and exchange mechanisms, message and task lifecycle management, supported transport layers, and security/authentication models.
- Make explicit where the two protocols occupy different layers of the agent stack and where they overlap, using concrete protocol-level details.

### 关键发现
- **Communication model**: MCP follows a client-host-server architecture where the host controls tool invocation flow (asymmetric, host-managed). A2A adopts a client-server model enabling symmetric peer-to-peer agent collaboration — any agent can be client or server, treating remote agents as opaque autonomous entities rather than deterministic tools. [MCP Architecture Spec](https://github.com/modelcontextprotocol/specification/blob/main/docs/specification/2025-11-25/architecture/index.mdx "MCP 2025-11-25 Architecture") [A2A Specification](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A v1.0 Specification — Section 1")
- **Capability discovery**: MCP uses runtime capability negotiation during session initialization (`initialize` handshake) + listing methods (`tools/list`, `resources/list`, `prompts/list`). A2A uses Agent Cards — JSON metadata at `/.well-known/agent-card.json` — enabling pre-connection discovery of identity, skills, security schemes, and supported modalities. A2A additionally supports Extended Agent Cards for authenticated tiered disclosure. [MCP Lifecycle Spec](https://github.com/modelcontextprotocol/specification/blob/main/docs/specification/2025-11-25/basic/lifecycle.mdx "MCP Capability Negotiation") [A2A Specification](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A Specification — Section 3.1.11")
- **Message format**: Both use JSON-RPC 2.0, but A2A v1.0 additionally defines gRPC and HTTP+JSON/REST bindings with Protocol Buffers (a2a.proto) as the canonical data model. [A2A Specification](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A Specification — Section 1.3")
- **Task lifecycle**: MCP's base interaction is stateless request-response; experimental Tasks (added in spec 2025-11-25) provide 5 states (working → input_required → completed/failed/cancelled). A2A's task lifecycle is a first-class concept with an 8-state machine: unspecified, submitted, working, completed, failed, canceled, input_required, rejected, auth_required — with clear terminal vs. interrupted state semantics. A2A separates Messages (communication turns) from Artifacts (output deliverables). [MCP Tasks Spec](https://github.com/modelcontextprotocol/specification/blob/main/docs/specification/2025-11-25/basic/utilities/tasks.mdx "MCP Tasks — experimental") [A2A Proto](https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto "A2A a2a.proto — TaskState enum")
- **Transport layers**: MCP supports stdio (local subprocess) + Streamable HTTP (stateless/stateful modes with SSE). A2A supports HTTP(S) with three bindings (JSON-RPC, gRPC, HTTP+JSON/REST) but no stdio. A2A natively supports push notifications via webhooks; MCP has no webhook mechanism. [MCP Transports Spec](https://github.com/modelcontextprotocol/specification/blob/main/docs/specification/2025-11-25/basic/transports.mdx "MCP Transports") [A2A Specification](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A — Section 3.5 Task Update Delivery")
- **Security/Auth**: MCP prescribes OAuth 2.1 + RFC 9728 Protected Resource Metadata, with DNS rebinding protections. A2A uses a declarative model via Agent Card supporting API Key, HTTP Auth, OAuth 2.0, OpenID Connect, and mTLS — more flexible and scheme-agnostic. A2A also supports Agent Card signing (JWS/RFC 7515) and webhook SSRF protections. [MCP Authorization Spec](https://github.com/modelcontextprotocol/specification/blob/main/docs/specification/2025-11-25/basic/authorization.mdx "MCP Authorization") [A2A Proto](https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto "A2A — SecurityScheme definition")
- **Content exchange**: MCP uses three server primitives (Resources, Tools, Prompts) + Sampling (client-side), with typed content items (text, image, audio, resource). A2A uses a unified Part model (text, raw bytes, URL, structured data) with per-agent/per-skill MIME type negotiation, making it modality-agnostic. [MCP Tools Spec](https://github.com/modelcontextprotocol/specification/blob/main/docs/specification/2025-11-25/server/tools.mdx "MCP Tools") [A2A Proto](https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto "A2A — Part message")
- **Stack positioning**: MCP occupies the agent-to-tool/data layer; A2A occupies the agent-to-agent collaboration layer. The A2A spec explicitly documents this complementarity in Appendix B, describing a reference architecture where an A2A Server agent uses MCP internally to interact with tools/data needed to fulfill tasks. However, MCP's experimental Tasks feature (2025-11-25) introduces growing overlap in the task management layer. [A2A Specification](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A Specification — Appendix B: Relationship to MCP")
- **Version history**: MCP has four spec versions (2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25) plus a draft. A2A progressed from 0.1.0 (April 2025) → 0.2.6 → 0.3.0 → 1.0.0 (current), moving from Google's GitHub to the Linux Foundation's `a2aproject/A2A` repository. [A2A GitHub README](https://github.com/a2aproject/A2A/blob/main/README.md "A2A README — Linux Foundation")
- **Comparison table**: A dimension-by-dimension comparison table is available covering architecture, core abstraction, message format, capability discovery, task lifecycle (5 vs. 8 states), transports, streaming, async notifications, auth model, content types, agent opacity, stack layer, local process support, and multi-turn support.

### 可用图片
无（A2A spec 包含 Mermaid 图描述可供渲染：3 层规范结构图和任务状态机图）

### 仍需补充
- MCP content type schema 的完整定义（TextContent, ImageContent, AudioContent, EmbeddedResource）以强化内容交换对比。
- A2A Agent Card 发现机制的未来扩展（注册中心、目录、DNS 发现等，在 spec roadmap 中提及但未规范化）。
- MCP 2025-11-25 之后的演进（draft 版本和 2026 年 3 月 roadmap 更新的具体内容）。
- A2A Extension 系统的具体使用示例（proto 中定义但 spec 中无详细案例）。

---

## Chapter 3: Complementarity and Convergence — How A2A and MCP Relate
### 研究目标
- Analyze the relationship between the two protocols beyond simple feature comparison.
- Examine how A2A and MCP can coexist in a single architecture — MCP connecting an agent to its tools/data sources while A2A governs inter-agent collaboration.
- Explore real or proposed reference architectures that layer both protocols, joint community or standards-body efforts, and whether technical convergence or formal interoperability bridges are emerging as of mid-2026.

### 关键发现
- A2A Spec Appendix B 明确声明两协议互补："A2A and MCP are complementary protocols designed for different aspects of agentic systems." 描述了标准集成模式：A2A Client 请求 A2A Server 执行任务，Server 内部使用 MCP 访问工具/数据。[A2A Specification — Appendix B](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A v1.0 Specification — Appendix B: Relationship to MCP")
- A2A v1.0 发布公告（2026 年 3 月）包含专节"Complementary to MCP, not a replacement"，明确指出两协议解决不同层级问题：MCP 用于 tool/context 集成，A2A 用于代理间通信协调。[A2A v1.0 Announcement](https://github.com/a2aproject/A2A/blob/main/docs/announcing-1.0.md "A2A Protocol Ships v1.0")
- A2A 官方文档首页提出三层心智模型："Build with ADK (or any framework), equip with MCP (or any tool), and communicate with A2A"——框架→工具→代理间通信的分层定位。[A2A Documentation Index](https://github.com/a2aproject/A2A/blob/main/docs/index.md "A2A official docs landing page")
- A2A 项目发布了详细的分层参考架构图和"Auto Repair Shop"多层场景示例：(1) Customer↔Shop Manager 通过 A2A 多轮对话；(2) Shop Manager 通过 A2A 委派 Mechanic 代理；(3) Mechanic 通过 MCP 调用诊断工具/维修手册/升降平台；(4) Mechanic 通过 A2A 与 Parts Supplier 代理通信订购零件。[A2A and MCP Guide](https://github.com/a2aproject/A2A/blob/main/docs/topics/a2a-and-mcp.md "A2A — Auto Repair Shop scenario")
- Google ADK 作为具体参考实现，源码同时包含 `src/google/adk/a2a/`（A2A 客户端/服务器）和 `src/google/adk/tools/mcp_tool/`（MCP 工具集成），使单个 ADK agent 可同时作为 A2A 端点和 MCP 工具消费者。[ADK Python Repository](https://github.com/google/adk-python "Google ADK Python — dual-protocol support")
- a2a-samples 仓库包含 5 个具体的双协议示例：(1) a2a_mcp（MCP 作为 A2A Agent Card 注册中心）；(2) Airbnb Planner Multi-Agent（ADK+A2A+MCP 多代理）；(3) AG2+MCP+A2A（AG2 框架桥接两协议）；(4) Java weather agent（跨语言双协议）；(5) Azure AI Foundry multi-agent（Microsoft Semantic Kernel+A2A+MCP）。[A2A Samples](https://github.com/a2aproject/a2a-samples "A2A 官方示例仓库")
- A2A 归属 Linux Foundation，由 8 席 TSC 治理（Google、Microsoft、Cisco、AWS、Salesforce、ServiceNow、SAP、IBM Research）。IBM 的 ACP（Agent Communication Protocol）已正式合并入 A2A。目前无单一联合标准机构同时治理 MCP 和 A2A。A2A 拥有 160+ 合作伙伴。[A2A Governance](https://github.com/a2aproject/A2A/blob/main/GOVERNANCE.md "A2A GOVERNANCE.md") [LF AI & Data Blog](https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/ "ACP joins forces with A2A")
- MCP 实验性 Tasks 功能（2025-11-25 spec）是最显著的技术收敛：由 Amazon 工程师提出，6 个生产用例之一即"Agent-to-Agent Communication"——承认 MCP 在实践中已被用于代理间通信。但架构差异仍显著：MCP Tasks 5 states vs. A2A 8 states，MCP 无 webhook 推送通知，MCP Tasks 作用域限于包装已有请求而非自主代理间协作。[MCP SEP-1686](https://github.com/modelcontextprotocol/specification/blob/main/docs/seps/1686-tasks.mdx "MCP SEP-1686: Tasks")
- 存在哲学性张力：A2A 文档警告不应将代理降级为工具（"wrapping agents as tools limits their capabilities"），但实践中为兼容性考虑可能推动将 A2A 代理包装为 MCP 工具——这违背 A2A 的核心设计原则。[A2A What is A2A](https://github.com/a2aproject/A2A/blob/main/docs/topics/what-is-a2a.md "A2A — 'Problems that A2A Solves'")
- 治理不对称：A2A 拥有 Linux Foundation TSC 正式多公司治理，MCP 仍由 Anthropic 主导无对等治理结构。多家组织（Microsoft、AWS、Salesforce）同时参与两生态但仅在 A2A 拥有正式 TSC 席位。
- 至少 12 个主流代理框架已内建 A2A 集成（ADK、Agno、AG2、CrewAI、LangGraph、LiteLLM、Microsoft Agent Framework 等），多数同时支持 MCP 工具集成，使其成为实际的双协议桥接层。[A2A Community Hub](https://github.com/a2aproject/A2A/blob/main/docs/community.md "A2A Community Hub")

### 可用图片
- A2A GitHub 仓库中的参考架构图可通过 URL 引用：`docs/assets/a2a-mcp.png`（User→Agent A(A2A)→Agent B(A2A)→Tools(MCP) 分层图）、`docs/assets/a2a-mcp-readme.png`、`docs/assets/agentic-stack.png`

### 仍需补充
- Anthropic 官方对 A2A 的明确表态（目前 MCP spec 未提及 A2A，Anthropic 未发布相关博客文章）。
- 双协议生产部署的定量采用数据（目前仅有示例和框架能力层面的证据）。
- IETF/W3C 是否有针对 A2A-MCP 互操作性的标准化工作（目前未发现）。
- 通用的 A2A↔MCP 协议翻译中间件或桥接项目（目前集成模式为框架特定的，无通用开源桥接器）。

---

## Chapter 4: A2A's Innovations and Unique Design Choices
### 研究目标
- Isolate and evaluate the novel contributions A2A brings relative to prior agent-communication approaches (including but not limited to MCP).
- Focus areas: Agent Card mechanism, multi-turn task lifecycle with explicit state transitions, native multimodal content support, push-notification and async completion model, and the opaque-agent philosophy.
- Assess which design choices represent genuinely new architectural ideas versus adaptations of existing patterns.

### 关键发现
- **Agent Card 创新**：Agent Card 在 `/.well-known/agent-card.json`（RFC 8615）实现去中心化、零握手的预连接发现，区别于 UDDI（中心化注册、WSDL 接口描述、已废弃）、FIPA Directory Facilitator（中心化、本体论描述）和 OpenAPI（确定性 API schema）。核心创新点：语义层级的能力描述（自然语言 + tags + examples，适合 LLM 代理解读）、去中心化自托管、安全方案与能力声明捆绑在单一文档中、JWS + JCS 密码学签名验证代理身份。[A2A Specification — Section 5](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A v1.0 — Agent Discovery") [A2A Agent Discovery Guide](https://github.com/a2aproject/A2A/blob/main/docs/topics/agent-discovery.md "A2A — Agent Discovery strategies")
- **Extended Agent Cards** 提供两级发现模式：公开卡片用于通用发现，认证后的扩展卡片暴露敏感能力——在 UDDI、FIPA、OpenAPI 发现机制中无直接对应物，满足企业分级信息披露需求。[A2A Specification — Section 3.1.11](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A — Get Extended Agent Card")
- **不透明代理哲学（Opaque-Agent Philosophy）**：代理作为不透明自主实体协作，不暴露内部推理链、工具或记忆。概念上继承 FIPA 的自主代理模型，但 A2A 的创新在于将其嵌入现代 Web 原生协议机制：无协议级内部访问、REJECTED 状态编码代理拒绝权、AUTH_REQUIRED 编码任务中凭证升级。A2A 文档明确反对"wrapping agents as tools"的做法。[A2A What is A2A](https://github.com/a2aproject/A2A/blob/main/docs/topics/what-is-a2a.md "A2A — Problems that A2A Solves") [A2A Enterprise Guide](https://github.com/a2aproject/A2A/blob/main/docs/topics/enterprise-ready.md "A2A — Enterprise Implementation")
- **8 状态任务状态机**：SUBMITTED → WORKING → COMPLETED/FAILED/CANCELED/REJECTED（终态）+ INPUT_REQUIRED/AUTH_REQUIRED（中断态）。其中 REJECTED（代理可自主拒绝任务）和 AUTH_REQUIRED（任务中凭证升级）是代理特有的创新状态，在 MCP、REST API、FIPA 中无对应物。终态不可变——后续操作创建新任务于同一 contextId 下，形成 DAG 式任务依赖模型。[A2A Proto — TaskState](https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto "A2A — TaskState enum") [A2A Life of a Task](https://github.com/a2aproject/A2A/blob/main/docs/topics/life-of-a-task.md "A2A — Task Immutability")
- **Messages vs Artifacts 架构分离**：Messages 承载沟通（指令、澄清、状态更新），Artifacts 承载任务输出物（文档、图片、结构化数据）。规范明确要求"Messages SHOULD NOT be used to deliver task outputs"。此分离在 MCP、REST API、FIPA ACL 中无直接对应。[A2A Specification — Section 3.7](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A — Messages and Artifacts separation")
- **统一 Part 模型与三级模态协商**：Part 为 oneof 联合体（text/raw/url/data），通过 MIME 类型在三个层级协商模态（Agent Card 全局默认 → AgentSkill 级覆盖 → 请求级 acceptedOutputModes），实现模态无关设计。相比 MCP 的固定类型集（TextContent/ImageContent/AudioContent），A2A 不需协议 schema 变更即可支持新模态。[A2A Proto — Part, AgentCard, SendMessageConfiguration](https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto "A2A — Part model and MIME negotiation")
- **Push 通知系统**：三级任务更新交付（polling → SSE → webhooks），统一 StreamResponse 格式跨所有机制。Webhook 支持完整 CRUD 操作和详尽安全规范（SSRF 防护、JWT/JWKS 互认证、重放攻击防护）。MCP 无 webhook 机制。创新不在 webhook 本身（已有成熟模式），而在将其作为一等协议特性与任务生命周期深度集成。[A2A Streaming & Async Guide](https://github.com/a2aproject/A2A/blob/main/docs/topics/streaming-and-async.md "A2A — Streaming and Async Operations")
- **Extension 机制**：四种扩展范围（数据扩展、Profile 约束、方法扩展/Extended Skills、状态机扩展），HTTP header 激活协议，URI 标识，TSC 治理生命周期（提案→实验→毕业→可选核心纳入）。已有具体扩展：AGP（Cisco，层级路由/Autonomous Squads）、Secure Passport（密码学签名的上下文状态共享）、Timestamp、Traceability。扩展不可修改核心数据结构，保持向后兼容。[A2A Extensions Guide](https://github.com/a2aproject/A2A/blob/main/docs/topics/extensions.md "A2A — Extensions specification")
- **Protobuf 作为规范数据模型**：v1.0 将 a2a.proto 提升为所有数据结构的唯一规范来源，三层架构（Data Model → Operations → Protocol Bindings）确保 JSON-RPC/gRPC/HTTP+JSON/REST 三种绑定的一致性。ADR-001 决定使用 ProtoJSON 作为 JSON 序列化规范。Google API annotations 自动生成 RESTful HTTP 绑定。此模式在代理间通信协议中罕见。[A2A ADR-001](https://github.com/a2aproject/A2A/blob/main/adrs/adr-001-protojson-serialization.md "ADR-001: ProtoJSON") [A2A v1.0 What's New](https://github.com/a2aproject/A2A/blob/main/docs/whats-new-v1.md "A2A v1.0 — protobuf as normative model")
- **非创新的标准模式采用**：JSON-RPC 2.0、SSE、OAuth 2.0/OIDC、RFC 8615 well-known URI、HTTP 缓存、gRPC、protobuf、webhooks、google.rpc.Status 错误模型——均为成熟的现有标准，A2A 未在这些层面做出本质创新。
- **创新光谱总结**：(1) 真正新颖——Agent Cards 去中心化语义能力广告、Extended Agent Cards 分级发现、REJECTED/AUTH_REQUIRED 状态、Messages/Artifacts 分离、Extension 机制、三级 MIME 协商、统一 StreamResponse 格式；(2) 显著适配——protobuf 规范模型+三绑定、任务不可变性+contextId DAG、webhook CRUD 集成、JWS+JCS 签名、multi-tenancy；(3) 标准采用——JSON-RPC、SSE、OAuth、gRPC 等。

### 可用图片
无（A2A GitHub 仓库中有相关图示如 `docs/assets/a2a-actors.png`、`docs/assets/agentic-stack.png`，可通过 URL 引用）

### 仍需补充
- FIPA ACL 的 performative 消息模式（inform, request, propose, accept-proposal）与 A2A 任务模式的深度技术对比。
- A2A 8 状态与 Kubernetes Job states/AWS Step Functions/BPMN 流程状态的详细对比以量化状态机创新程度。
- Extension 机制的实际生产采用数据（目前已有扩展均在 a2a-samples 仓库，处于早期/参考实现阶段）。
- ProtoJSON vs 原生 JSON 的序列化性能基准。

---

## Chapter 5: Problem Space — What A2A Is Designed to Solve
### 研究目标
- Define the concrete problems and gaps in the pre-A2A landscape that the protocol targets.
- Cover multi-agent orchestration in heterogeneous environments, enterprise interoperability requirements, limitations of tool-centric protocols when the counterpart is an autonomous agent, and scalability challenges in complex agentic workflows.
- Ground each problem statement in documented industry pain points or use-case scenarios.

### 关键发现
- **异构代理孤岛问题**：A2A 发布前，不同供应商（Google、Microsoft、Salesforce、SAP 等）和框架（LangChain、CrewAI、AutoGen、ADK 等至少 12 个主流框架）构建的代理之间无标准通信方式，各连接需定制开发，形成 N²集成负担。Google 在 A2A 发布公告中将此识别为核心问题：代理被"锁定在各自生态系统中"形成新的"信息孤岛"。[Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/a2a-a-new-era-of-agent-interoperability "A2A 发布公告, 2025-04-09") [A2A Community Hub](https://github.com/a2aproject/A2A/blob/main/docs/community.md "A2A — 12+ 框架集成列表")
- **"代理即工具"反模式**：A2A 文档明确指出将代理包装为工具的做法存在根本缺陷——"wrapping agents as tools limits their capabilities"。具体能力损失包括：(1) 失去协商能力（工具基于 schema 验证而非自主判断）；(2) 失去多轮交互（工具调用为单次请求-响应）；(3) 失去自主拒绝权；(4) 失去长时执行支持（受工具调用超时限制）；(5) 失去不透明性和 IP 保护（工具接口暴露形式参数 schema）。[A2A What is A2A](https://github.com/a2aproject/A2A/blob/main/docs/topics/what-is-a2a.md "A2A — Problems that A2A Solves")
- **MCP 生态自身承认该缺口**：MCP SEP-1686（Tasks 提案，Amazon 工程师编写）将"Agent-to-Agent Communication"列为显式用例，描述 Amazon 内部多代理系统中"slow agents cause cascading delays"——确认工具中心协议用于代理间通信存在具体运营问题。[MCP SEP-1686](https://github.com/modelcontextprotocol/specification/blob/main/docs/seps/1686-tasks.mdx "MCP SEP-1686 — Agent-to-Agent Communication 用例")
- **企业跨组织协作需求**：企业环境要求不同组织的代理在信任和合规边界内交互。A2A 通过将远程代理视为"standard HTTP-based enterprise applications"解决此问题，使企业可复用现有安全基础设施（防火墙、API 网关、身份提供商）。不透明代理哲学直接满足数据主权需求（如 GDPR）——代理间不共享内部数据处理。[A2A Enterprise Guide](https://github.com/a2aproject/A2A/blob/main/docs/topics/enterprise-ready.md "A2A — Enterprise Implementation")
- **合规与审计**：任务不可变性设计（终态任务不可修改/重启）直接支持审计需求——每个任务提供可靠的输入-输出映射作为可审计记录。规范明确以"reliable input-to-output mapping for traceability"作为首要设计理由。[A2A Life of a Task](https://github.com/a2aproject/A2A/blob/main/docs/topics/life-of-a-task.md "A2A — Task Immutability")
- **长时运行任务管理缺口**：同步请求-响应模式无法满足需要数分钟至数天的代理任务（复杂研究、多步分析、文档生成、采购流程等）。Amazon MCP SEP-1686 记录了 6 个生产用例需要异步执行。移动端、Serverless 函数、浏览器应用无法维持长时 HTTP 连接——A2A 的推送通知系统（webhook + CRUD 生命周期管理 + JWT 互认证 + SSRF 防护）提供标准化解决方案。[A2A Streaming & Async Guide](https://github.com/a2aproject/A2A/blob/main/docs/topics/streaming-and-async.md "A2A — Push Notifications") [MCP SEP-1686](https://github.com/modelcontextprotocol/specification/blob/main/docs/seps/1686-tasks.mdx "MCP SEP-1686 — 6 生产用例")
- **代理发现与信任缺口**：A2A 前无标准化代理能力发现机制。UDDI（中心化、已废弃）和 FIPA DF（中心化）均需注册基础设施。A2A Agent Card 实现去中心化预连接发现，JWS+JCS 签名实现密码学身份验证。Extended Agent Card 实现分级能力披露——在先前所有代理发现机制中无对应物。[A2A Specification — Section 5](https://github.com/a2aproject/A2A/blob/main/docs/specification.md "A2A — Agent Discovery")
- **规模化挑战**：160+ 合作伙伴组织间若维持双边定制集成将在计算上不可行（N×(N-1)/2 合约）。A2A 将其简化为 N 个实现。Cisco AGP 扩展引入层级路由/Autonomous Squads 解决互联网级代理通信路由问题——证明跨网络代理路由需求已被实际感知。[A2A Partners](https://github.com/a2aproject/A2A/blob/main/docs/partners.md "A2A — 160+ partners") [AGP Extension](https://github.com/a2aproject/a2a-samples/tree/main/extensions/agp "AGP — capability-based routing")
- **行业用例驱动**：A2A 官方示例展示具体企业场景——旅行规划（多代理协调航班/酒店/租车）、Auto Repair Shop（跨组织供应链）、Azure AI Foundry 多代理路由。金融服务合规工作流（贷款审批跨代理审查、Chinese Wall 要求代理间不透明）直接受益于任务不可变性、不透明代理模型和长时任务支持。
- **行业共识验证**：(1) 50+ 发布合作伙伴 → 160+ 当前合作伙伴的快速增长表明问题的广泛紧迫性；(2) IBM 将独立开发的 ACP 合并入 A2A 而非维持竞争标准——确认问题被多家主要技术公司独立识别；(3) Microsoft 明确采用 A2A 并获得 TSC 席位，承认企业客户需要跨生态系统代理协作。[Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/a2a-a-new-era-of-agent-interoperability "A2A — 50+ partners") [LF AI & Data Blog](https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/ "ACP 合并入 A2A") [Microsoft Cloud Blog](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/05/07/empowering-multi-agent-apps-with-the-open-agent2agent-a2a-protocol/ "Microsoft — A2A 支持")

### 可用图片
无

### 仍需补充
- 关于 A2A 前定制代理集成具体成本的定量数据（工程工时、代码行数、维护成本），目前无公开来源。
- 2025-2026 年独立分析师报告（IDC、Forrester、McKinsey）对代理互操作性问题的专项分析。
- 因缺乏代理互操作标准导致企业项目失败或严重延误的具体案例研究（目前仅有设计场景而非真实部署事后分析）。
- 金融服务和医疗行业关于代理间审计追踪的具体监管要求文件。

---

## Chapter 6: Ecosystem Adoption, Industry Momentum, and Outlook
### 研究目标
- Survey the current adoption landscape for both protocols as of early-to-mid 2026: major platforms, cloud providers, and agent frameworks that have integrated A2A or MCP; notable enterprise deployments or pilot programs; open-source community activity and governance structure.
- Assess forward trajectory over the next six months: upcoming specification milestones, competitive dynamics, risks that could slow adoption, and conditions under which one protocol could subsume the other.

### 关键发现
- **A2A 采用指标（截至 2026 年 4 月）**：主仓库约 23,000 GitHub stars、2,339 forks、138 contributors；Python SDK（a2a-sdk）PyPI 月下载量约 420 万次；5 种语言官方 SDK + 3 种社区 SDK；a2a-samples 仓库含 32 个 Python 示例、7 个 Java 示例、4 个协议扩展；166 家合作伙伴组织；Inspector 和 TCK 工具已发布。[GitHub API — a2aproject/A2A](https://api.github.com/repos/a2aproject/A2A "A2A repo stats, April 2026") [PyPI Stats — a2a-sdk](https://pypistats.org/api/packages/a2a-sdk/recent "a2a-sdk monthly downloads")
- **MCP 采用指标（截至 2026 年 4 月）**：servers 仓库约 82,800 stars、10,173 forks；spec 仓库约 7,700 stars、326 contributors；10 种语言官方 SDK；Python SDK 月下载量约 1.75 亿次，TypeScript SDK 约 1.42 亿次——是 A2A 的 30-40 倍。官方 Server Registry 于 2025 年 9 月发布预览版，含数百个第三方集成服务器。MCP Inspector 9,309 stars。[GitHub API — modelcontextprotocol](https://api.github.com/repos/modelcontextprotocol/servers "MCP servers repo stats") [PyPI Stats — mcp](https://pypistats.org/api/packages/mcp/recent "MCP Python SDK downloads")
- **云提供商集成**：Google Cloud 为 A2A 发起方，原生集成至 ADK、Vertex AI、Cloud Run；Microsoft 于 2025 年 5 月为 Semantic Kernel 添加 A2A 支持并获 TSC 席位；AWS 获 TSC 席位，开发 Strands Agents 框架（A2A 集成），且 AWS 工程师编写了 MCP Tasks（SEP-1686）；Cisco 获 TSC 席位，开发 AGP 扩展；Oracle、Salesforce、SAP、ServiceNow、IBM Research 均为 TSC 成员或合作伙伴。[Microsoft Cloud Blog](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/05/07/empowering-multi-agent-apps-with-the-open-agent2agent-a2a-protocol/ "Microsoft A2A 支持, 2025-05-07") [A2A Governance](https://github.com/a2aproject/A2A/blob/main/GOVERNANCE.md "A2A TSC 组成")
- **治理对比**：A2A 采用 Linux Foundation 下多利益相关方 TSC（8 席位、多数投票+50% 法定人数），将于 2026 年中从"启动阶段"转向"稳态"治理。MCP 采用 Anthropic 主导的分层治理（Lead Maintainers 持否决权），通过 Working Groups/Interest Groups 邀请社区参与（Agents WG 由 AWS+Anthropic 联合维护）。[A2A Governance](https://github.com/a2aproject/A2A/blob/main/GOVERNANCE.md "A2A 治理") [MCP Governance SEP-932](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/932 "MCP 治理 SEP")
- **规范路线图**：A2A 在不到 12 个月内经历 10 个版本迭代（0.1.0→1.0.0），v1.0 于 2026 年 3 月 12 日发布。MCP 已发布 5 个规范版本 + 活跃 draft。MCP SEP 管道约 290 个提案，关键在进 SEP 包括 SEP-2127（Server Cards/.well-known/mcp.json 发现——类似 A2A Agent Cards）、SEP-2339（Task Continuity）、SEP-2268（Subtasks）、SEP-2229（Unsolicited Tasks）。A2A 后续重点为多语言 v1.0 SDK 支持和扩展生态建设。[A2A v1.0 Announcement](https://github.com/a2aproject/A2A/blob/main/docs/announcing-1.0.md "A2A v1.0, March 2026") [SEP-2127](https://github.com/modelcontextprotocol/modelcontextprotocol/pulls/2127 "MCP Server Cards 提案")
- **竞争格局**：无重大竞争标准——IBM ACP 已合并入 A2A。IETF 已正式介入：Rosenberg & Jennings 的 Internet-Draft（2025 年 5 月）调查 MCP/A2A 并识别缺口；CATALIST（Coordinating Agent To Agent List of efforts）BoF 计划于 IETF 125 举行，可能成立工作组标准化代理通信组件。多个 MCP SEP 向 A2A 已有能力方向收敛（Tasks、Server Cards、Subtasks），表明功能收敛趋势，但设计哲学差异仍然显著。[IETF I-D — Rosenberg & Jennings](https://www.ietf.org/archive/id/draft-rosenberg-ai-protocols-00.txt "AI Agent Protocols 框架, May 2025") [IETF CATALIST](https://datatracker.ietf.org/group/catalist/ "CATALIST BoF")
- **企业信号**：TSC 组成本身即为企业采用信号——全球 8 家最大企业技术公司承诺工程领导力；6 家主要咨询公司（Accenture、Deloitte、McKinsey、BCG、PwC、KPMG）列为 A2A 合作伙伴；MCP 成立金融服务 Interest Group。[A2A Partners](https://github.com/a2aproject/A2A/blob/main/docs/partners.md "A2A — 166 partners") [MCP Financial Services IG](https://github.com/modelcontextprotocol/financial-services-interest-group "MCP 金融服务 IG")
- **采用风险**：(1) 功能重叠导致开发者困惑（MCP Tasks/Server Cards 与 A2A 核心功能重叠）；(2) MCP 治理集中于 Anthropic（Lead Maintainers 否决权）；(3) A2A 生态规模显著小于 MCP（SDK 下载量差 40 倍）；(4) 两协议均未经历大规模安全事件考验；(5) 企业可观测性/管理/合规工具尚不成熟。
- **前瞻展望**：至 2026 年 10 月，两协议将大概率维持互补定位——"MCP inside agents, A2A between agents"分层架构已成为两社区认可的标准参考模型。MCP Tasks 的演进（是否添加任务拒绝、多轮协商、推送通知）是关键变量。IETF CATALIST BoF 结果可能影响长期标准化格局。完全替代条件苛刻——需一方完全实现另一方的核心功能集并凭更大生态驱动采用。更可能的轨迹是持续专业化 + 互操作桥接增强，类似 HTTP 与 SMTP 在互联网通信不同层级的共存。

### 可用图片
无

### 仍需补充
- 具名企业的 A2A/MCP 生产部署案例研究（目前仅有合作伙伴列表和 TSC 组成作为间接证据）。
- MCP 官方 Registry 的注册服务器确切总数（T1 来源确认）。
- Oracle Cloud 对 A2A/MCP 的具体集成文档。
- 独立分析师（Gartner、IDC、Forrester）关于 A2A vs MCP 采用轨迹的专项分析报告。
- IETF CATALIST BoF 于 IETF 125 的实际结果（尚未召开）。

---

# Section 2：给 Write 阶段的执行建议
- **Language and register**: Use formal, analytical English throughout — the tone of a technology research report. Avoid first-person singular; use "we assess," "we observe," or passive constructions for analytical judgments.
- **Terminology consistency**: Use "A2A" (not "Agent2Agent" or "A-to-A") and "MCP" as primary abbreviations after first full expansion. Use "agent" for autonomous AI actors and "tool" for deterministic external services/APIs.
- **Balanced framing**: Analyze both protocols on their own terms. Avoid language that positions one protocol as inherently superior; articulate design trade-offs and contexts in which each excels.
- **Cross-chapter coherence**: Chapter 2 (comparison) establishes the factual technical baseline; Chapters 3–5 build on it. Writers of Chapters 3–5 should reference specific technical details from Chapter 2 rather than re-describing them.
- **Concreteness over abstraction**: Support capability differences with protocol-level mechanisms (e.g., "A2A's `TaskStatus` state machine defines five explicit states…") rather than vague characterizations. Every quantitative claim must include subject, time, unit, value, and source citation.
- **Avoid speculative predictions without grounding**: The outlook chapter should anchor forward-looking statements in observable evidence (announced roadmaps, public commitments, measurable community metrics).
- **No dangling references**: Every factual claim must carry an inline citation at the point of use.
- **Visual aids**: Include comparison tables (especially Chapter 2) and reference architectural diagrams where they clarify the text. Tables comparing protocol features dimension-by-dimension are strongly encouraged.
- **Time scope**: Research window covers April 2025 – October 2026 (past 12 months to 6 months ahead from current date 2026-04-03).
