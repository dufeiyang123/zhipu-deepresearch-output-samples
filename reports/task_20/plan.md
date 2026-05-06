# Section 1：章节研究计划

## Chapter 1：从 HTTP+SSE 到 Streamable HTTP——背景与动机
### 研究目标
- 阐明 MCP 在 2024-11-05 版本中采用 HTTP+SSE 双端点传输方案时遭遇的架构瓶颈：双连接管理复杂度高、长连接在负载均衡与横向扩展中的困难、连接断开后无法恢复导致消息丢失、以及与 HTTP/2 和 HTTP/3 的兼容性摩擦
- 解释 Anthropic/MCP 团队在 2025-03-26 版规范中引入 Streamable HTTP 的核心驱动力
- 梳理 Streamable HTTP 在 MCP 整体演进路线（2025-03-26 → 2025-06-18 → 2025-11-25 三版迭代）中的定位

### 关键发现
- 发现 1：MCP 2024-11-05 规范定义了 HTTP+SSE 传输层的双端点强制架构——服务端 MUST 提供一个 SSE 端点（供客户端建立连接并接收服务端消息）和一个 HTTP POST 端点（供客户端发送消息）。连接时服务端 MUST 首先通过 SSE 发送 `endpoint` 事件，包含后续 POST 请求所用 URI。[MCP 规范 2024-11-05 Transports](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports "MCP 2024-11-05 版传输层规范原文")
- 发现 2：PR #206 作者 Justin Spahr-Summers（Anthropic/MCP 核心团队）在 PR 描述中明确指出旧版三大核心缺陷：(1) 不支持可恢复性（resumability）；(2) 要求服务端维持高可用的长连接；(3) 只能通过 SSE 通道投递服务端消息。[PR #206](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206 "RFC: Replace HTTP+SSE with new Streamable HTTP transport")
- 发现 3：旧版架构在生产环境造成显著痛点——双连接管理复杂、长连接 SSE 消耗大量资源且难以水平扩展、连接断开时响应直接丢失无恢复机制、部分 SSE 实现在 HTTP/2 和 HTTP/3 上存在兼容性问题、不支持 Serverless 部署。[fka.dev 技术分析](https://blog.fka.dev/blog/2025-06-06-why-mcp-deprecated-sse-and-go-with-streamable-http/ "Why MCP Deprecated SSE and Went with Streamable HTTP")
- 发现 4：Streamable HTTP 由 @jspahrsummers 于 2025-03-17 以 RFC 形式提交 PR #206，经 24 次提交和超过 205 条讨论评论后于 2025-03-24 合入主分支，纳入 2025-03-26 版规范。PR 获得 321 个 👍 反应。设计是 Shopify、Pydantic、Cloudflare、LangChain、Vercel 等多方协作成果。[PR #206](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206 "RFC: Replace HTTP+SSE with new Streamable HTTP transport, merged Mar 24 2025")
- 发现 5：Streamable HTTP 5 项核心设计变更：(1) 移除 `/sse` 端点；(2) 所有消息通过单一端点的 POST 发送；(3) 服务端可将响应升级为 SSE 流发送通知/请求；(4) 服务端可选择建立 `Mcp-Session-Id` 维持状态；(5) 客户端可通过 GET 请求发起 SSE 流。允许服务端完全无状态运行。[PR #206](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206 "TL;DR section of the RFC")
- 发现 6：PR #206 明确解释不选择 WebSocket 的理由：(1) RPC 风格无状态调用中 WebSocket 引入不必要开销；(2) 浏览器环境中 WebSocket 无法附加 Authorization 等自定义 Header；(3) POST 端点升级为 WebSocket 需两步过程引入额外复杂性。[PR #206](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206 "Why not WebSocket section")
- 发现 7：2025-03-26 版 changelog 第 2 项 major change 为"Replaced the previous HTTP+SSE transport with a more flexible Streamable HTTP transport"，同版本引入 OAuth 2.1 授权框架、JSON-RPC 批处理和工具注解。[MCP 2025-03-26 Changelog](https://modelcontextprotocol.io/specification/2025-03-26/changelog "2025-03-26 版官方变更日志")
- 发现 8：2025-06-18 版移除 JSON-RPC 批处理支持（PR #416），引入 `MCP-Protocol-Version` HTTP 头部要求（PR #548），POST 请求体改为仅接受单个 JSON-RPC 消息。[MCP 2025-06-18 Changelog](https://modelcontextprotocol.io/specification/2025-06-18/changelog "2025-06-18 版官方变更日志")
- 发现 9：2025-11-25 版关键增强：(1) SSE 轮询机制（SEP-1699）——服务端可在发送初始带 event ID 的事件后主动关闭连接，客户端通过轮询重连；(2) 服务端关闭前 SHOULD 发送 `retry` 字段；(3) `Mcp-Session-Id` 标准化为 `MCP-Session-Id`；(4) 增强 Origin 头校验（无效 Origin MUST 返回 403）；(5) 新增实验性 Task 支持（SEP-1686）。[MCP 2025-11-25 Changelog](https://modelcontextprotocol.io/specification/2025-11-25/changelog "2025-11-25 版官方变更日志")
- 发现 10：截至 2025-11-25，MCP 拥有超过 9,700 万月度 SDK 下载量、10,000+ 活跃服务端，获 ChatGPT、Claude、Cursor、Gemini、Microsoft Copilot、VS Code 等主流客户端一级支持。[MCP 官方博客](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/ "One Year of MCP: November 2025 Spec Release")
- 发现 11：SEP-1335（2025-08-12）揭示 Streamable HTTP 发布后仍存在问题：SSE 流启动后断连前无事件则客户端无法恢复、规范不允许服务端主动关闭连接导致必须维持长连接、缺少重连等待指导。其核心提议被采纳进入 2025-11-25 版规范。[SEP-1335](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1335 "Address Streamable HTTP transport issues")
- 发现 12：HTTP+SSE 废弃演进路径：2024-11-05 版作为唯一远程传输方式 → 2025-03-26 版被 Streamable HTTP 替代并标记为 deprecated → 后续版本持续保持废弃状态并强化 Streamable HTTP。所有后续版本的 Backwards Compatibility 章节均标注 HTTP+SSE 为 deprecated。[MCP 2025-03-26 Transports](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports "Backwards Compatibility 章节")
- 发现 13：Anthropic 于 2024-11-25 首次公开发布 MCP，首版规范（2024-11-05）仅定义 stdio 和 HTTP+SSE 两种传输方式。TypeScript SDK 1.10.0（2025-04-17）是首个支持 Streamable HTTP 的 SDK 版本。[Anthropic 官方公告](https://www.anthropic.com/news/model-context-protocol "Introducing the Model Context Protocol, 2024-11-25")

### 可用图片
（无相关本地图片素材）

### 仍需补充
- MCP GitHub Discussion 中关于传输层迁移的早期讨论帖具体链接（PR #206 提到但未直接给出）
- 2025-06-18 版中 HTTP+SSE deprecated 的精确措辞——是否存在单独废弃声明文档未能确认

## Chapter 2：Streamable HTTP 协议设计与传输机制
### 研究目标
- 系统拆解 Streamable HTTP 传输层的协议规范设计：单一 MCP 端点（POST + GET）的统一端点模型
- 分析客户端到服务端的消息发送机制（POST 请求承载 JSON-RPC 消息，响应可为 application/json 或 text/event-stream）以及服务端到客户端的监听机制（GET 请求开启 SSE 流）
- 还原 SSE 流的动态升降级设计以及规范中的 MUST/SHOULD/MAY 约束层级

### 关键发现
- 发现 1：Streamable HTTP 要求服务端提供单一 HTTP 端点路径（"MCP endpoint"，示例 `https://example.com/mcp`），MUST 同时支持 POST 和 GET 两种方法，将所有通信统一到同一 URL 路径。设计意图是支持从最基础（仅 POST+JSON 响应）到功能丰富（SSE 流式+主动推送）的多种服务端实现。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "Streamable HTTP 统一端点定义")
- 发现 2：客户端每条 JSON-RPC 消息 MUST 通过新的 HTTP POST 发送，MUST 包含 Accept 头同时列出 `application/json` 和 `text/event-stream`。POST 请求体格式在 2025-06-18 版起从允许批处理数组收窄为仅允许单个 JSON-RPC request/notification/response。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "POST 请求 Accept 头部约束")
- 发现 3：移除批处理由 ihrpr 在 PR #416（2025-04-25 合并）提出，理由是实现 TypeScript 和 Python SDK 时未发现批处理的 compelling use case，且并行工具调用可通过水平扩展实现。部分社区成员认为此举偏离了 JSON-RPC 2.0 规范。[PR #416](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/416 "Remove batching requirement")
- 发现 4：服务端对 POST 中不同类型 JSON-RPC 消息的响应存在差异化处理——notification/response 被接受时 MUST 返回 202 Accepted（无响应体），被拒绝时 MUST 返回 HTTP 错误状态码；request 类型 MUST 返回 `application/json`（单个 JSON 对象）或 `text/event-stream`（启动 SSE 流）二者之一。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "POST 响应规则")
- 发现 5：客户端 MAY 向 MCP 端点发起 GET 请求以开启 SSE 流，MUST 包含 `Accept: text/event-stream`。服务端 MUST 以 `text/event-stream` 响应启动 SSE 流或返回 405 Method Not Allowed。GET 流上可发送 request 和 notification，但 MUST NOT 发送 response（恢复场景除外）。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "GET 请求开启 SSE 流")
- 发现 6：SSE 动态升降级是核心特性——对 request 类型 POST，服务端自主决定返回 JSON 还是 SSE 流。简单同步操作走 JSON（"降级"），长耗时操作升级为 SSE 流。SSE 流 SHOULD 最终包含对应的 JSON-RPC response，可在 response 前先发送中间 request/notification（如进度通知），response 发送后 SHOULD 终止流。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "SSE 流生命周期")
- 发现 7：SSE 事件使用 `event: message` 作为事件类型，`data:` 字段承载完整的 JSON-RPC 消息（JSON 序列化），可选包含 `id` 字段（用于可恢复性）和 `retry` 字段（用于轮询间隔控制）。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "SSE 事件格式")
- 发现 8：2025-11-25 版引入 SSE 轮询机制（SEP-1699）：服务端启动 SSE 流时 SHOULD 立即发送一个仅含事件 ID 和空 data 的预备事件（prime），之后 MAY 在任何时候关闭连接（而非终止流），断连前 SHOULD 发送含 `retry` 字段的事件，客户端 MUST 遵守 retry 值。该机制解决了服务端必须维持长连接的负担，向后兼容。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "SSE 轮询机制") [SEP-1699](https://github.com/modelcontextprotocol/specification/discussions/1699 "Support SSE polling via server-side disconnect")
- 发现 9：断开连接 SHOULD NOT 被解释为客户端取消请求，取消需显式发送 `CancelledNotification`。客户端 MAY 同时维持多个 SSE 流，服务端 MUST 将每条消息仅在一个流上发送（不广播）。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "断连语义与多连接约束")
- 发现 10：可恢复性机制——服务端 MAY 为 SSE 事件附加 `id` 字段，该 ID MUST 在会话内所有流中全局唯一，SHOULD 编码流标识信息。恢复始终通过 HTTP GET 加 `Last-Event-ID` 执行（无论原始流通过 POST 还是 GET 启动），事件 ID 按每流（per-stream）基准分配作为流内游标。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "恢复始终通过 GET")
- 发现 11：HTTP 状态码语义——200（成功 JSON/SSE 响应）、202 Accepted（notification/response 被接受）、400 Bad Request（缺少 Session ID/无效 Protocol-Version）、403 Forbidden（无效 Origin，2025-11-25 新增明确要求）、404 Not Found（会话已终止）、405 Method Not Allowed（不支持 GET SSE/不允许 DELETE）。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "HTTP 状态码使用约束")
- 发现 12：2025-06-18 版引入 `MCP-Protocol-Version` 头部——客户端 MUST 在初始化后所有请求中携带，服务端未收到时 SHOULD 假定版本为 2025-03-26，无效版本 MUST 返回 400。[MCP 规范 2025-06-18 版 Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports "MCP-Protocol-Version 头部要求")
- 发现 13：向后兼容检测机制——客户端先 POST InitializeRequest，若成功则确认新版 Streamable HTTP；若返回 400/404/405（2025-11-25 版明确为这三个码，之前版本笼统为 4xx），则发起 GET 期望打开旧版 SSE 流并接收 `endpoint` 事件。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "向后兼容检测协商流程")
- 发现 14：MUST/SHOULD/MAY 约束分布——客户端 MUST 8 项（POST 发送、Accept 双类型、单消息体、支持双响应格式、GET Accept、遵守 retry、携带 Protocol-Version、404 时重新初始化）；服务端 MUST 12 项（单端点双方法、Origin 验证、403 响应、202/错误码响应、JSON 或 SSE 响应、GET 处理、单流投递、ID 唯一性等）。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "完整 MUST/SHOULD/MAY 约束")
- 发现 15：MCP Transport Working Group（2025-12-19）指出 Streamable HTTP 在大规模部署中面临挑战：负载均衡器须解析完整 JSON-RPC 负载才能路由、有状态连接迫使粘性路由阻碍自动扩缩容。未来方向包括协议无状态化、会话提升至数据模型层、JSON-RPC 路由信息暴露至 HTTP 路径/头部，计划 2026 年 6 月下一版规范落地。[MCP Transport Future Blog](https://mcpcn.com/en/blog/transport-future/ "MCP Transport Working Group 路线图")

### 可用图片
（无相关本地图片素材；规范中的 Sequence Diagram 可在写作阶段重新绘制）

### 仍需补充
- 规范原文中 Sequence Diagram（Mermaid/图片）未能通过 web reader 提取，建议写作阶段自行绘制 POST/GET/SSE 交互时序图
- 406 Not Acceptable 状态码在 Accept 协商失败场景下是否被规范有意省略——需确认
- SSE 事件 `event` 字段类型名称（`message`）仅从 SDK 实现推断，规范原文未显式规定——建议从 SDK 源码确认

## Chapter 3：会话管理、可恢复性与状态机制
### 研究目标
- 深入分析 MCP-Session-Id 头部的分配规则、全局唯一性与安全性要求（UUID/JWT/加密哈希）
- 梳理会话生命周期管理（初始化分配、客户端附带、服务端终止 404 响应、客户端主动 DELETE 销毁）
- 分析 SSE 流的可恢复性与重投递机制（事件 ID 按流分配策略、Last-Event-ID 恢复断点续传）以及无状态/有状态模式的取舍

### 关键发现
- 发现 1：服务端在初始化阶段 MAY 分配 Session ID，方式为在 `InitializeResult` 响应中附加 `MCP-Session-Id` 头部。不分配则实现无状态模式。若分配，客户端 MUST 在后续所有请求中附带；需要 Session ID 的服务端 SHOULD 对缺少该头部的非初始化请求返回 400 Bad Request。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "Session Management")
- 发现 2：Session ID 格式两层约束——安全性层面 SHOULD 全局唯一且密码学安全（UUID/JWT/加密哈希）；编码层面 MUST 仅包含可见 ASCII 字符（0x21-0x7E）。2025-11-25 版新增客户端 MUST 安全处理 Session ID 的要求，安全最佳实践要求 MUST 使用不可确定的 ID，SHOULD 使用安全随机数生成器，SHOULD 将 ID 绑定用户信息（推荐 `<user_id>:<session_id>` 格式）。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "Session ID 格式") [MCP 安全最佳实践](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices "Session Hijacking 缓解")
- 发现 3：头部名称从 `Mcp-Session-Id`（2025-03-26/2025-06-18 版）改为 `MCP-Session-Id`（2025-11-25 版）。由于 HTTP/1.1 头部名称不区分大小写（RFC 9110）、HTTP/2 强制小写，该变更在协议兼容性上无影响。[MCP 规范 2025-03-26 版 Transports](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports "Mcp-Session-Id") [MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "MCP-Session-Id")
- 发现 4：服务端终止会话——MAY 在任何时候终止，终止后 MUST 对包含该 Session ID 的请求返回 404 Not Found。客户端收到 404 后 MUST 发送新的 `InitializeRequest` 开始新会话。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "服务端终止会话")
- 发现 5：客户端终止会话——SHOULD 发送 HTTP DELETE 并附带 `MCP-Session-Id`。服务端 MAY 返回 405 Method Not Allowed 表示不允许客户端主动终止。会话过期时服务端 MAY 终止所有活跃 SSE 流（级联影响）。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "客户端终止会话")
- 发现 6：无状态模式通过服务端选择不分配 Session ID 隐式实现，规范未显式定义"无状态模式"。PR #206 原始提案明确："Stateless servers are now possible—eliminating the requirement for high availability long-lived connections"，并给出 "Stateless server" 和 "Stateless server with streaming" 两种示例范式。[PR #206](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206 "Stateless servers are now possible")
- 发现 7：有状态模式下 Session ID 用于路由——PR #206 描述 "server can use session ID for sticky routing or routing messages on a message bus"，POST 消息可到达水平扩展部署中任一节点，须通过 Redis 等 broker 路由到已有会话。Sentry 创始人 mitsuhiko 建议确保 Session ID 可被基本负载均衡器读取。[PR #206](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206 "Stateful server 路由")
- 发现 8：Session ID 从客户端生成改为服务端分配——PR #206 初始版本采用客户端生成方案，daviddenton 质疑其安全性并建议改为服务端在 initialize 响应中生成和签名，获 12 赞同后被采纳。[PR #206](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206 "daviddenton 建议改为服务端生成")
- 发现 9：SSE 事件 ID 的可恢复性——服务端 MAY 为事件附加 `id`，该 ID MUST 在会话内所有流中全局唯一，SHOULD 编码流标识信息。事件 ID 按 per-stream 基准分配充当流内游标。Issue #1847 建议格式如 `streamId::sequence`。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "事件 ID 全局唯一性与 per-stream cursor") [Issue #1847](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1847 "事件 ID 格式建议")
- 发现 10：恢复始终通过 HTTP GET + `Last-Event-ID` 执行，无论原始流通过 POST 还是 GET 启动。此为 2025-11-25 版新增澄清。服务端 MAY 重放断连点后的消息并恢复流，MUST NOT 重放不同流的消息。Issue #1847 指出旧版 TypeScript SDK 错误地使用 POST 恢复。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "恢复始终通过 GET") [Issue #1847](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1847 "建议所有恢复统一走 GET")
- 发现 11：SSE 轮询机制（SEP-1699，2025-11-25 新增）与可恢复性深度耦合——服务端启动 SSE 流时 SHOULD 立即发送含事件 ID 和空 data 的预备事件（解决 SEP-1335 识别的"无初始事件则无法恢复"缺陷），之后 MAY 随时关闭连接，断连前 SHOULD 发送含 `retry` 字段的事件，客户端 MUST 遵守 retry 值。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "SSE 轮询")
- 发现 12：2025-11-25 版引入"连接"关闭与"流"终止的概念区分——服务端可关闭 HTTP 连接而不终止逻辑 SSE 流，客户端通过重连继续接收。该区分在 2025-03-26/2025-06-18 版中不存在。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "连接关闭 vs 流终止")
- 发现 13：Session Hijack Prompt Injection 攻击路径——攻击者获取 Session ID 后向其他服务端发送恶意事件，通过共享队列传递给原始客户端。可恢复性机制增加了消息注入攻击面。[MCP 安全最佳实践](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices "Session Hijack Prompt Injection")
- 发现 14：SEP-1335（2025-08-12）首次系统识别可恢复性四大问题（无初始事件无法恢复、必须维持长连接、可能过度重连、缺乏垃圾回收）。SEP-1699（2025-10-22）声明部分取代 SEP-1335，采用更宽松约束（SHOULD 而非 MUST），聚焦轮询机制。[SEP-1335](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1335 "首次识别可恢复性问题") [SEP-1699](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1699 "部分取代 SEP-1335")

### 可用图片
（无相关本地图片素材）

### 仍需补充
- 无状态模式下"特定客户端"的识别方式——规范未定义（IP？OAuth token？）
- DELETE 成功时的响应状态码未明确（200? 202? 204?）
- 消息垃圾回收策略在 2025-11-25 版中仍未纳入规范——SEP-1335 提出的问题仅部分解决

## Chapter 4：官方 SDK 工程实现
### 研究目标
- 对比分析 TypeScript SDK（自 1.10.0 起支持 Streamable HTTP）与 Python SDK 的工程实现细节
- 涵盖客户端侧 StreamableHTTPClientTransport 的连接建立与协议协商、服务端侧 StreamableHTTPServerTransport 的请求路由与多连接管理
- 覆盖 Java SDK、C# SDK 等社区 SDK 的实现进展，关注 SDK 对规范 MUST/SHOULD 条款的实际落地差异

### 关键发现
- 发现 1：TypeScript SDK 于 2025-04-17 发布 v1.10.0 首次引入 Streamable HTTP，最新稳定版 v1.22.0（周下载量 880 万+）。NPM 包名 `@modelcontextprotocol/sdk`。[NPM @modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk "版本历史")
- 发现 2：TypeScript 客户端 `StreamableHTTPClientTransport` 构造函数接受 `URL` 和可选配置（`authProvider`、自定义 `fetch`），调用 `client.connect(transport)` 连接，断开时先 `terminateSession()`（HTTP DELETE）再 `client.close()`。[TypeScript SDK Client Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/client.md "StreamableHTTPClientTransport 用法")
- 发现 3：TypeScript SDK 提供 Streamable HTTP 优先、SSE 回退的标准模式——先尝试 `StreamableHTTPClientTransport`，失败则回退 `SSEClientTransport`，通过 try/catch 实现。提供 `streamableHttpWithSseFallbackClient.ts` 示例。[TypeScript SDK Client Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/client.md "SSE fallback")
- 发现 4：可恢复性通过 `resumptionToken` 和 `onresumptiontoken` 回调支持——开发者在 `client.request()` 选项中传入上次断开时保存的 token，每次收到新事件 ID 时触发回调以持久化 token。提供 `ssePollingClient.ts` 示例。[TypeScript SDK Client Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/client.md "Resumption tokens")
- 发现 5：TypeScript 服务端 `NodeStreamableHTTPServerTransport` 关键参数：`sessionIdGenerator`（undefined=无状态，`() => randomUUID()`=有状态）、`enableJsonResponse`（true 则所有 POST 返回纯 JSON、GET 返回 405）、`enableDnsRebindingProtection`、`allowedHosts`/`allowedOrigins`。核心方法 `handleRequest(req, res, body)` 路由 POST/GET/DELETE。[TypeScript SDK Server Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server.md "NodeStreamableHTTPServerTransport")
- 发现 6：无状态模式下每个 POST 创建新 transport 实例（防止请求 ID 冲突），有状态模式通过 `onsessioninitialized` 回调存储 transport 到 `Map<string, Transport>`，后续通过 `mcp-session-id` 头部查找。[NPM @modelcontextprotocol/sdk](https://www.npmjs.com/package/@modelcontextprotocol/sdk "Session Management 示例")
- 发现 7：SDK 提供 `createMcpExpressApp()` 和 `createMcpHonoApp()` 框架集成，默认启用 DNS 重绑定防护。Hono 集成支持 Cloudflare Workers/Deno/Bun Web Standard 运行时。服务端可恢复性通过 EventStore 抽象支持，内置 `inMemoryEventStore.ts` 参考实现。[TypeScript SDK Server Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server.md "Express/Hono 集成与 EventStore")
- 发现 8：Python SDK（`mcp` PyPI 包）v1.26.0，核心依赖为 httpx + httpx-sse（客户端）、Starlette（服务端 ASGI）、anyio、pydantic。自 v1.8.0 起支持 Streamable HTTP。v1.x 为当前稳定版，main 分支开发 v2 pre-alpha。[PyPI mcp](https://pypi.org/project/mcp/ "mcp 包依赖与版本") [Python SDK GitHub](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md "v1.x 稳定版")
- 发现 9：Python SDK 通过 `FastMCP` 高级接口，`mcp.run(transport="streamable-http")` 启动。关键配置：`stateless_http=True`（无状态）、`json_response=True`（纯 JSON 响应）、`streamable_http_path`（默认 `/mcp`）。文档推荐生产部署使用 `stateless_http=True` + `json_response=True`。[Python SDK README](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md "Streamable HTTP 配置")
- 发现 10：Python SDK 使用 Starlette ASGI，`mcp.streamable_http_app()` 返回 ASGI 应用，可挂载到 Starlette `Mount` 路由。CORS 配置需显式暴露 `Mcp-Session-Id` 头部。TypeScript SDK 与 Python SDK 均要求 CORS `allowedMethods` 包含 GET/POST/DELETE。[Python SDK README](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md "Starlette/CORS 配置")
- 发现 11：TypeScript SDK 不绑定特定框架（`handleRequest` 接受标准 Node.js req/res），Python SDK 直接基于 Starlette。认证方面，TypeScript 提供丰富内置认证体系（AuthProvider/ClientCredentials/PrivateKeyJwt/OAuth），Python 通过 `mcp.server.auth` 模块的 `TokenVerifier` + `AuthSettings` 实现。[TypeScript SDK Server Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server.md "框架无关") [Python SDK README](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md "Authentication")
- 发现 12：Java SDK 由 Anthropic 与 Spring AI 协作维护，客户端使用 JDK 11+ HttpClient，服务端使用 Jakarta Servlet API，编程模型基于 Project Reactor。Spring AI 2.0+ 提供 WebClient/WebFlux/WebMVC 集成。要求 Java 17+。[Java SDK GitHub](https://github.com/modelcontextprotocol/java-sdk "架构与设计")
- 发现 13：Kotlin SDK 由 Anthropic 与 JetBrains 协作维护，客户端 Streamable HTTP 自 v0.6.0 支持，服务端仍在开发中，使用 Ktor 框架。[Kotlin SDK GitHub Issue #346](https://github.com/modelcontextprotocol/kotlin-sdk/issues/346 "客户端 v0.6.0，服务端开发中")
- 发现 14：C# SDK 由 Microsoft 维护，v1.0 于 2026-03-05 发布，完整支持 2025-11-25 规范。通过 `ISseEventStreamStore` 抽象 SSE 事件存储（内置 `DistributedCacheEventStreamStore`），`EnablePollingAsync()` 释放 SSE 连接实现轮询模式。实现实验性 Task 原语（`IMcpTaskStore`，五种状态生命周期）。[.NET Blog](https://devblogs.microsoft.com/dotnet/release-v10-of-the-official-mcp-csharp-sdk/ "C# SDK v1.0")

### 可用图片
（无相关本地图片素材）

### 仍需补充
- TypeScript SDK `StreamableHTTPClientTransport` 完整构造函数签名（源码文件路径可能已重组）
- Python SDK 低级别 HTTP transport 类名（FastMCP 封装了底层实现，类名需从源码确认）
- Java SDK 中 Streamable HTTP transport 具体类名和首次引入版本号
- 各 SDK 对 `MCP-Protocol-Version` 头部和批处理移除后的具体处理逻辑

## Chapter 5：安全机制与生产部署
### 研究目标
- 系统梳理 DNS 重绑定攻击防护（Origin 头校验、localhost 绑定策略）及已知漏洞案例
- 分析 OAuth 2.0 授权框架在 MCP 中的集成演进（2025-03-26 引入到 2025-11-25 增强）
- 评估生产部署模式（无状态 Serverless 部署、有状态长连接部署、API 网关配置要点）及性能考量

### 关键发现
- 发现 1：DNS 重绑定攻击利用 DNS 记录操控使恶意网站访问运行在 localhost 的 MCP 服务端。MCP 安全最佳实践明确列出 "DNS rebinding" 为已知攻击向量。[MCP 安全最佳实践](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices "DNS rebinding 攻击向量")
- 发现 2：CVE-2025-66416（Python SDK）——影响 `mcp` 包 <1.23.0 版本，CVSS v4 7.6（High），CWE-1188。FastMCP 默认不启用 DNS 重绑定防护。修复后 `host` 为 localhost 时默认启用防护。2025-12-02 披露。[GitHub Security Advisory GHSA-9h52-p55h-vw2f](https://github.com/modelcontextprotocol/python-sdk/security/advisories/GHSA-9h52-p55h-vw2f "CVE-2025-66416")
- 发现 3：CVE-2025-66414（TypeScript SDK）——影响 `@modelcontextprotocol/sdk` <1.24.0 版本，CVSS v4 7.6（High），CWE-1188。`StreamableHTTPServerTransport` 默认不启用 `enableDnsRebindingProtection`。修复后 `createMcpExpressApp()` 绑定 localhost 时默认启用防护。2025-12-02 披露。注意：general-purpose 子智能体提到的 CVE-2025-59163 实际为第三方 vet MCP Server 漏洞，非 TypeScript SDK。[GitHub Security Advisory GHSA-w48q-cv73-mx4w](https://github.com/modelcontextprotocol/typescript-sdk/security/advisories/GHSA-w48q-cv73-mx4w "CVE-2025-66414")
- 发现 4：CVE-2025-49596（MCP Inspector RCE）——CVSS 9.4（Critical），影响 Inspector <0.14.1。攻击者利用 Inspector Proxy 的 `0.0.0.0:6277` 端口缺乏认证，通过 CSRF 执行任意命令。可与浏览器 0.0.0.0-day 缺陷链式利用。修复后新增会话令牌认证和 Origin 校验。[Oligo Security](https://www.oligo.security/blog/critical-rce-vulnerability-in-anthropic-mcp-inspector-cve-2025-49596 "CVE-2025-49596") [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-49596 "NVD 记录")
- 发现 5：防御机制核心为 Host 头部验证白名单——TypeScript SDK 提供 `enableDnsRebindingProtection`/`allowedHosts`/`allowedOrigins`，Express/Hono 集成绑定 localhost 时自动启用。[TypeScript SDK Server Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server.md "DNS rebinding protection 配置")
- 发现 6：OAuth 三版演进——2025-03-26 版首次引入，MCP 服务端可兼任授权服务器，依赖 OAuth 2.1/RFC 8414/RFC 7591。2025-06-18 版关键重构：引入 RFC 9728（Protected Resource Metadata），MCP 服务端明确定位为 Resource Server，MUST 实现 Protected Resource Metadata，新增 RFC 8707 Resource Indicators 要求。2025-11-25 版引入 Client ID Metadata Documents（去中心化注册）、Step-Up Authorization、Cross App Access (XAA) 企业授权。[MCP 规范 2025-03-26 版 Authorization](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization "初版 OAuth") [MCP 规范 2025-06-18 版 Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization "引入 RFC 9728") [MCP 规范 2025-11-25 版 Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization "CIMD、XAA")
- 发现 7：Aaron Parecki 指出 Client ID Metadata Documents 是首次在主流协议中大规模采用"基于 DNS 的去中心化信任模型"，解决了 DCR 在大规模开放生态中的注册膨胀问题。XAA 基于 ID-JAG 实现四步无用户交互的企业级授权流程。[Aaron Parecki 博文](https://aaronparecki.com/2025/11/25/1/mcp-authorization-spec-update "CIMD 和 XAA 分析")
- 发现 8：AWS Bedrock AgentCore 支持 stateless 模式（`stateless_http=True`，推荐）和 stateful 模式。协议合约要求 `0.0.0.0:8000/mcp` 上 streamable-http 传输。平台使用 `Mcp-Session-Id` 实现 MicroVM 亲和路由。OAuth 认证通过 RFC 9728 的 `WWW-Authenticate` + `resource_metadata` URL。[AWS Bedrock AgentCore MCP 部署文档](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html "stateless/stateful 模式与 MicroVM 亲和")
- 发现 9：Cloudflare Workers + Durable Objects 方案——每个 MCP 会话映射到一个 Durable Object 实例，内置 OAuth Provider 库 `workers-oauth-provider`。2025-04-30 更新支持 Streamable HTTP，可同时提供两种传输实现向后兼容。支持 Python Workers。[Cloudflare Blog](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/ "Durable Objects MCP") [Cloudflare Blog](https://blog.cloudflare.com/streamable-http-mcp-servers-python/ "Streamable HTTP 支持")
- 发现 10：AWS Lambda 部署面临冷启动延迟、API Gateway 对 SSE 有限支持（需 `json_response=True` 或 Lambda URL）、15 分钟执行超时限制。[GitHub: streamable-mcp-serverless](https://github.com/aarora79/streamable-mcp-serverless "Lambda 部署方案")
- 发现 11：API 网关配置要点——会话亲和性（基于 `Mcp-Session-Id` 头部的一致性哈希）、SSE 超时配置（避免网关过早终止流）、Content-Type 透传（禁用 response buffering）、CORS 暴露 `Mcp-Session-Id`。[AWS Bedrock AgentCore 协议合约](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp-protocol-contract.html "MicroVM Stickiness")
- 发现 12：JSON 响应模式适合简单请求-响应和 Serverless 部署（无长连接开销），SSE 模式适合长耗时操作。Streamable HTTP 在 HTTP/1.1 上即可工作，HTTP/2 多路复用可降低多流并发连接开销。2025-11-25 版 SSE 轮询机制将长连接模型转变为短连接+重连，大幅降低并发连接数。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "SSE 轮询性能影响")
- 发现 13：安全最佳实践覆盖五大攻击向量——Confused Deputy Problem、Token Passthrough（MUST NOT）、SSRF、Session Hijacking、Local Server Compromise。SSRF 防御四层：强制 HTTPS、阻止私有 IP 范围（RFC 9728 Section 7.7）、验证重定向目标、出口代理。[MCP 安全最佳实践](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices "五大攻击向量与 SSRF 防御")

### 可用图片
（无相关本地图片素材）

### 仍需补充
- TypeScript/Python SDK DNS 重绑定防护的源码级 Host 头部匹配逻辑
- AWS Lambda 部署的实测性能数据（冷启动 P99 等）缺少权威量化基准
- HTTP/2 vs HTTP/1.1 下 MCP SSE 流连接开销的量化对比数据

## Chapter 6：迁移路径与向后兼容策略
### 研究目标
- 还原规范定义的向后兼容检测机制（客户端先尝试 POST InitializeRequest，失败后回退 GET 打开旧版 SSE 流）
- 分析服务端双模式并行托管策略以及 SDK 层面的兼容性封装
- 梳理从 2025-06-18 规范正式废弃 HTTP+SSE 到 2025-11-25 进一步强化 Streamable HTTP 的时间线与迁移窗口

### 关键发现
- 发现 1：MCP 规范 2025-03-26/2025-06-18/2025-11-25 三个版本的 Backwards Compatibility 章节文本结构完全一致，均以"deprecated HTTP+SSE transport (from protocol version 2024-11-05)"开篇。HTTP+SSE 自 2025-03-26 版引入 Streamable HTTP 时即被标记为 deprecated。[MCP 规范 2025-03-26 版 Transports](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports "Backwards Compatibility") [MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "Backwards Compatibility")
- 发现 2：客户端协议协商流程——(1) 向服务端 URL 发送 POST `InitializeRequest`（Accept: application/json, text/event-stream）；(2) 成功则确认 Streamable HTTP；(3) 失败时回退触发条件版本间有差异：2025-03-26/2025-06-18 版为笼统 "4xx"，2025-11-25 版缩窄为 400/404/405 三个特定状态码；(4) 回退时向同一 URL 发送 GET 期望打开 SSE 流并收到 `endpoint` 事件。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "客户端回退流程")
- 发现 3：规范推荐的服务端双模式策略为维护独立端点——旧版 SSE 端点 + POST 端点与新版 MCP 端点并行存在，而非在同一端点合并两种传输。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "服务端向后兼容指导")
- 发现 4：TypeScript SDK 的 SSE 回退通过 try/catch 实现——先尝试 `StreamableHTTPClientTransport` + `connect()`，失败则创建新 `Client` 实例用 `SSEClientTransport` 连接。回退需创建全新 Client 实例，原实例不可复用。SDK 提供 `streamableHttpWithSseFallbackClient.ts` 示例。代码片段：
```typescript
try {
    const client = new Client({ name: 'my-client', version: '1.0.0' });
    const transport = new StreamableHTTPClientTransport(baseUrl);
    await client.connect(transport);
} catch {
    const client = new Client({ name: 'my-client', version: '1.0.0' });
    const transport = new SSEClientTransport(baseUrl);
    await client.connect(transport);
}
```
[TypeScript SDK Client Guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/client.md "SSE fallback")
- 发现 5：Python SDK 不提供内置自动回退，需手动实现。官方示例通过环境变量 `MCP_TRANSPORT_TYPE` 以 if/else 选择 `streamable_http_client` 或 `sse_client`。[Python SDK simple-auth-client 示例](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/simple-auth-client/mcp_simple_auth_client/main.py "if/else 选择逻辑")
- 发现 6：Cloudflare Agents SDK 双传输模式——`MyMCP.serveSSE('/sse')` 处理旧版 SSE，`MyMCP.serve('/mcp')` 处理 Streamable HTTP，通过 URL 路径路由。SSE 标记为"Legacy compatibility"。[Cloudflare Agents Transport 文档](https://developers.cloudflare.com/agents/model-context-protocol/transport/ "双传输模式")
- 发现 7：Session ID 头部名称从 `Mcp-Session-Id`（2025-03-26 至 2025-11-25 版）改为 `MCP-Session-Id`（draft 版）。HTTP/1.1 头部大小写不敏感但某些中间件可能敏感，实现应确保大小写不敏感解析。各 SDK 使用不同大小写形式（TypeScript 用 `mcp-session-id`，Python 用 `Mcp-Session-Id`，AWS AgentCore 用 `Mcp-Session-Id`）。[MCP 规范 draft 版 Transports](https://modelcontextprotocol.io/specification/draft/basic/transports "MCP-Session-Id 重命名")
- 发现 8：`MCP-Protocol-Version` 头部（2025-06-18 版引入）的向后兼容——服务端未收到时 SHOULD 假定 2025-03-26 版，确保从旧客户端到新服务端的平滑迁移。[MCP 规范 2025-06-18 版 Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports "MCP-Protocol-Version 默认回退")
- 发现 9：JSON-RPC 批处理于 2025-06-18 版移除（PR #416），使用批处理的旧客户端连接新服务端时会出错。迁移建议：将批量调用拆分为多个并行 POST 请求，利用 HTTP/2 多路复用降低开销。[MCP 规范 2025-06-18 版 Changelog](https://modelcontextprotocol.io/specification/2025-06-18/changelog "移除批处理")
- 发现 10：从双端点到单端点的路由变更——旧版需维护 SSE 端点和动态传递的 POST 端点 URI，新版统一到单一 MCP 端点（POST/GET/DELETE）。迁移时不再需要动态端点 URI 传递，同一端点处理三种 HTTP 方法。[MCP 规范 2025-11-25 版 Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports "单端点模型")
- 发现 11：截至 draft 版（2026 年 4 月），Backwards Compatibility 章节仍完整保留，规范中不存在明确的 HTTP+SSE 移除时间线。[MCP 规范 draft 版 Transports](https://modelcontextprotocol.io/specification/draft/basic/transports "draft 版 Backwards Compatibility 仍在")
- 发现 12：draft 版新增 SSE 流配置指导——服务端 SHOULD 发送 `X-Accel-Buffering: no` 指示反向代理禁用缓冲。GET 流约束收紧：仅允许 notifications 和 pings（不再允许 requests）。405 响应 MUST 包含 `Allow` 头部。[MCP 规范 draft 版 Transports](https://modelcontextprotocol.io/specification/draft/basic/transports "draft 版新增约束")
- 发现 13：LangChain `langchain-mcp-adapters` 内置 Streamable HTTP → SSE 自动回退，表明协议协商回退已成为生态标准行为。[langchain-mcp-adapters 文档](https://reference.langchain.com/javascript/langchain-mcp-adapters "自动回退")

### 可用图片
（无相关本地图片素材）

### 仍需补充
- `Mcp-Session-Id` → `MCP-Session-Id` 重命名的具体 PR 编号未能定位
- Python SDK 是否在 v2 分支中新增了自动回退机制
- HTTP+SSE 最终移除时间线——截至 draft 版仍无迹象，需追踪规范仓库相关 issue

# Section 2：给 Write 阶段的执行建议
- 受众定位为具备 HTTP 协议基础和后端工程经验的中高级开发者与架构师，避免对 HTTP、SSE、JSON-RPC 等基础概念做冗余科普
- 涉及规范条文时，区分 MUST、SHOULD、MAY 三个约束层级并明确标注，Chapter 2 已整理了完整的约束分布（客户端 MUST 8 项、服务端 MUST 12 项），写作时可直接引用
- 代码示例精选而非堆砌：Chapter 2 用请求/响应示例演示 POST/GET 交互流程（建议自行绘制时序图替代规范中未能提取的 Mermaid 图）；Chapter 4 引入 TypeScript `StreamableHTTPClientTransport`/`NodeStreamableHTTPServerTransport` 和 Python `FastMCP` 的关键配置；Chapter 6 直接使用 researcher 获取的 SSE fallback try/catch 代码片段和 Cloudflare 双传输路由代码
- 统一术语：「MCP 端点」指 Streamable HTTP 的单一端点、「旧版传输」或「HTTP+SSE 传输」指 2024-11-05 版方案、「会话 ID」指 MCP-Session-Id 头部值（注意 draft 版已从 `Mcp-Session-Id` 改为 `MCP-Session-Id`，写作时以最新命名为准并注明历史变更）
- 规范版本精确对应四个关键节点：2025-03-26（引入 Streamable HTTP + OAuth 2.1）、2025-06-18（移除批处理 + 引入 MCP-Protocol-Version + MCP 服务端定位为 OAuth Resource Server）、2025-11-25（SSE 轮询 + Task 支持 + 增强恢复机制 + CIMD/XAA）、draft 版（GET 流约束收紧 + X-Accel-Buffering + 405 Allow 头部）
- CVE 编号与 SDK 版本精确对应：CVE-2025-66416（Python SDK <1.23.0）、CVE-2025-66414（TypeScript SDK <1.24.0）、CVE-2025-49596（MCP Inspector <0.14.1，Critical）。注意之前流传的 CVE-2025-59163 实际属于第三方 vet MCP Server，非 TypeScript SDK
- 有状态与无状态部署模式对比应结合 AWS Bedrock AgentCore（stateless_http + MicroVM 亲和路由）和 Cloudflare Workers（Durable Objects 有状态）两个具体方案给出选型建议
- Chapter 3 关于"连接关闭 vs 流终止"的概念区分（2025-11-25 版新增）是理解 SSE 轮询机制的前提，建议在 Chapter 2 讨论 SSE 轮询时先建立此概念
- 写作前需再次核验的关键事项：(1) SSE 事件 `event` 字段类型名称是否为 `message`（规范未显式规定，仅 SDK 推断）；(2) DELETE 成功的响应状态码（规范未明确）；(3) 无状态模式下"特定客户端"的识别方式（规范未定义）——这些缺口可在写作中以"规范未显式约定"的方式如实说明
- 全文时间口径：以 2026-04-02 为锚点，回顾 2024-11-25（MCP 首次发布）至今的完整演进，重点覆盖 2025-03-26 至 2025-11-25 三版规范迭代
