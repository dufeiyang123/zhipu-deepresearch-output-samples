# Section 1：章节研究计划

## Chapter 1：The Reactive Scaling Gap — Kubernetes Cluster Autoscaler and Its Limitations
### 研究目标
- Cluster Autoscaler (CA) 的反应式循环（pending pods → 节点供给 → pod 调度）端到端延迟量级及其在 EKS/GKE/AKS 上的差异
- CA 架构约束（ASG/MIG 耦合、节点组刚性、scale-from-zero 冷启动）对响应速度的限制
- Karpenter 在去节点组化快速 bin-packing 方面的改进与仍未解决的前瞻性扩缩短板
- 周期性、突发性、事件驱动等负载画像下，纯反应式节点扩缩何时无法满足 SLO

### 关键发现
- CA 默认每 10 秒扫描一次不可调度 pod（`--scan-interval`），官方 SLO 仅覆盖 CA 决策时间（小集群 ≤30s、大集群 ≤60s），不含 VM 供给时间。HPA + CA 组合场景下，从负载增长到新 pod 运行约需 5 分钟（GCE 环境）。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "Official CA FAQ — scan interval, SLO, combined latency")
- **GKE** 节点启动约 80–120 秒，端到端通常 3–4 分钟。[GKE Capacity Provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning "GKE docs: 80-120s boot time")；**EKS** 标准 EC2 节点供给约 1–2 分钟，端到端 2–3 分钟。[AWS Containers Blog](https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning/ "AWS blog: ~1-2 min node provisioning lag")；**AKS** VMSS 供给典型 2–4 分钟，`max-node-provision-time` 默认 15 分钟。[AKS Cluster Autoscaler](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler "AKS CA docs — default parameters and profiles")
- CA 与云厂商节点组（ASG/MIG/VMSS）强耦合，同一节点组内所有节点须具备相同调度属性；节点组过多会严重影响 CA 性能，分片部署被视为"最后手段"。Scale-from-zero 冷启动代价更高，因无运行节点提供调度元数据且容量可能已被回收。[AWS EKS Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html "AWS CA docs — ASG coupling, node group rigidity, scaling from zero")
- Karpenter 最新版本 v1.8.0（kubernetes-sigs/karpenter），CNCF SIG Autoscaling 子项目，2024 年达 v1.0.0 GA。采用无节点组直接供给架构，batch window 默认 1s idle / 10s max，支持工作负载合并（consolidation）与多云（AWS 原生 + AKS NAP）。[Karpenter Core Releases](https://github.com/kubernetes-sigs/karpenter/releases "v1.8.0") [CNCF Karpenter Blog](https://www.cncf.io/blog/2024/11/06/karpenter-v1-0-0-beta/ "Karpenter v1.0.0 and SIG Autoscaling contribution")
- Karpenter **仍然是反应式**——仅监听不可调度 pod，不具备需求预测或时间感知的前瞻性扩缩能力。batch window 最多增加 10 秒有意延迟以优化 bin-packing，不能消除 1–4 分钟的 VM 启动时间。[CNCF Karpenter Blog](https://www.cncf.io/blog/2024/11/06/karpenter-v1-0-0-beta/ "Karpenter reactive by design")
- 实际案例：GitHub Issue #5769 报告一个运行 CA v1.26.1 的大型集群在 3,000+ pending pod 场景下经历长达 15 分钟的扩缩延迟，远超大集群 ≤60s 的 SLO。[CA GitHub Issue #5769](https://github.com/kubernetes/autoscaler/issues/5769 "Real-world CA scale-up delays with 3000+ pending pods on AWS")
- GPU 工作负载冷启动瀑布流总计 3–8 分钟（节点供给 60–120s + 镜像拉取 30–60s + 模型下载 60–180s + CUDA 初始化 5–30s + 权重转移 10–60s）。[ScaleOps Blog](https://scaleops.com/blog/reducing-gpu-cold-start-times-in-kubernetes-patterns-and-solutions/ "Cold start waterfall — 3-8 min for GPU workloads")
- GKE 为 Autopilot 集群推出 fast-starting nodes，兼容 GPU 工作负载（G2/A2 机型）可实现最高 4 倍更快节点启动和 2 倍更快 Pod 调度，但不适用于 Spot VM。[GKE Fast-Starting Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes "GKE docs: up to 4x faster GPU node startup")
- CA v1.35.0 引入 **CapacityBuffer** CRD（v1beta1 API），提供官方超额预留机制，与 ResourceQuota 集成，但仍处于 beta 阶段。[CA GitHub Releases](https://github.com/kubernetes/autoscaler/releases "CA v1.35.0 release notes — CapacityBuffer v1beta1")
- 周期性负载（如每日 9 点高峰）、突发性事件负载（闪购、游戏上线）、scale-to-zero 成本优化场景下，反应式扩缩的 2–5 分钟延迟会导致 SLO 不可接受。AWS 文档明确指出"节点可能需要数分钟才可用，pod 调度延迟可能增加一个数量级"。[AWS EKS Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html "AWS CA docs — overprovisioning rationale")

### 可用图片
（无本地可用图片）

### 仍需补充
- AKS VMSS 精确供给时间基准：2–4 分钟估值来自社区经验，未找到微软官方实测数据
- Karpenter vs. CA 端到端延迟对比基准：无已发表的对照实验或官方基准测试
- GKE fast-starting nodes 对非 GPU 标准 CPU 工作负载的具体延迟改善数据
- AKS Karpenter provider 的精确版本号追踪：NAP 文档未显著标注 Karpenter 版本


## Chapter 2：Predictive (ML / Time-Series-Based) Node Autoscaling
### 研究目标
- 已应用于 Kubernetes 工作负载预测的预测技术（ARIMA、Prophet、LSTM、Transformer 等）的精度与运维开销对比
- 开源项目与框架（KEDA predictive scaler / Kedify、自定义 Prometheus → 模型 → CA/Karpenter 管线）的成熟度评估
- 主流云厂商原生预测扩缩功能（AWS Predictive Scaling for ASG、GCP Predictive Autoscaling for MIG）与 K8S 节点组的集成方式及局限
- 运营化预测节点扩缩所需的数据管线与可观测基础设施（指标采集粒度、模型重训练节奏、反馈环路）

### 关键发现
- KEDA 为 **CNCF Graduated 项目**（2023 年 8 月毕业），最新稳定版 **v2.19.0**（2026 年 2 月发布），约 9,900 GitHub Stars。内置 **PredictKube scaler**（`type: predictkube`，由 Dysnix 开发），通过 Prometheus 查询 7–14 天历史数据并调用 PredictKube SaaS AI 推理服务返回未来预测值（如 2 小时 `predictHorizon`），需 API Key。[KEDA GitHub Releases](https://github.com/kedacore/keda/releases "KEDA v2.19.0, Feb 2026") [KEDA PredictKube Scaler Docs](https://keda.sh/docs/2.19/scalers/predictkube/ "Official PredictKube scaler documentation")
- **Kedify** 是基于 KEDA 的商业平台，2025 年 10 月发布预测扩缩器（`type: kedify-predictive`），默认使用 **Facebook Prophet** 模型。引入 **MetricPredictor CRD**（`apiVersion: kedify.io/v1alpha1`）管理模型生命周期（数据源、保留期、重训练间隔、季节性），90/10 训练测试拆分以 MAPE 评估，`modelMapeThreshold` 作为安全网。支持混合扩缩公式如 `(current + predicted)/2`。[Kedify Predictive Autoscaling Blog](https://kedify.io/resources/blog/predictive-autoscaling/ "Predictive Autoscaling announcement, Oct 2025")
- **AWS Predictive Scaling for ASG**：分析最多 14 天 CloudWatch 历史数据，生成未来 48 小时每小时预测（每 6 小时更新），最低需 24 小时历史数据。`SchedulingBufferTime` 可在预测需求前预启动实例。仅处理 scale-out；scale-in 需单独配置动态策略。适用于 EKS Managed Node Group 底层 ASG，但假设同质实例——混合实例组（Karpenter/Spot 常见模式）会导致预测不准。[AWS Predictive Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html "AWS official documentation")
- **GCP Predictive Autoscaling for MIG**：需最少 3 天 CPU 自动扩缩历史，使用最多 3 周负载历史。每隔数分钟重新计算预测，**免费**。仅支持 CPU 利用率指标，仅预测日/周模式（不含月/年/一次性事件），短于 10 分钟的模式不捕获。MIG 重建会重置历史要求。实际用量超过预测时自动切换为实时数据优先。[GCP Predictive Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling "Official GCP documentation")
- **Azure Predictive Autoscale for VMSS**：需最少 7 天历史（最优 15 天），仅支持 `Percentage CPU` + `Average` 聚合，仅 scale-out，实例可提前 5–60 分钟预启动。不可用于 Azure Government 云。适用于 AKS 节点池底层 VMSS，与 AKS CA 可共存但协调为隐式非显式。[Azure Predictive Autoscale](https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-predictive "Microsoft Learn documentation")
- 学术研究：Guruge & Priyadarshana (2025, *Frontiers in Computer Science*) 提出 **Prophet–LSTM 混合模型**，在 NASA 和 FIFA 数据集上精度（MSE）提升 65–90%，但预测延迟约 3,500ms 远高于单模型 Bi-LSTM 的约 5ms。[Guruge & Priyadarshana 2025](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1509165/full "Prophet-LSTM hybrid for K8s autoscaling") Liao & Yuan (2024, *Electronics*) 实现 Holt–Winters + GRU 多模型 Operator，GRU MSE=0.00166 vs Holt–Winters MSE=0.01756，多模型管理减少冷启动 1 小时 41 分钟、SLA 波动降低 83.3%；同文引用 Shim et al. (IEEE SysCon 2023) 发现 **Transformer 模型**在 ARIMA/LSTM/Bi-LSTM/Transformer 对比中精度最高。[Liao & Yuan 2024](https://www.mdpi.com/2079-9292/13/2/285 "Holt-Winters + GRU multi-model management")
- 开源项目：**PHPA**（`jthomperoo/predictive-horizontal-pod-autoscaler`，v0.13.2）使用 Holt-Winters / Linear Regression，Pod 级；**Crane/EffectiveHPA**（`gocrane/crane`，腾讯开源）使用 DSP 算法，`TimeSeriesPrediction` CRD 支持自定义 Prometheus 指标预测；**Dynatrace obslab**（Apache-2.0，GitOps 模式，Davis AI 预测 → 自动 PR）。[PHPA GitHub](https://github.com/jthomperoo/predictive-horizontal-pod-autoscaler "v0.13.2") [Crane EffectiveHPA](https://gocrane.io/docs/best-practices/effective-hpa-with-prometheus-adapter/ "EffectiveHPA with Prometheus Adapter")
- 规范化预测管线五阶段架构：(1) Prometheus 采集（15–60s scrape interval）→ (2) 预测服务（Prophet/LSTM/etc.）查询 7–14 天历史 → (3) 预测值通过 Pushgateway / custom metrics API / KEDA external scaler 回暴 → (4) HPA/KEDA 调整 pod 副本 → (5) CA/Karpenter 基于 pod 调度压力供给/回收节点。运维要求：历史保留 ≥7–14 天，重训练间隔可配置（如 Kedify 推荐每 6 小时），持续 MAPE/MSE 监控并在置信度低于阈值时回退反应式扩缩。[Kedify Predictive Autoscaling Blog](https://kedify.io/resources/blog/predictive-autoscaling/ "Architecture with KEDA integration")
- 三大云厂商预测扩缩共同局限：(1) 主要/仅支持 CPU 指标（AWS 支持自定义 CloudWatch 但主要面向 CPU/网络）；(2) 无原生 Kubernetes 感知（基于 VM 级指标，不理解 pod 调度压力）；(3) 仅 scale-out；(4) 历史要求 24h–7d；(5) ML 模型完全托管/不透明黑箱。

### 可用图片
（无本地可用图片）

### 仍需补充
- Kedify 确切产品版本号及发布节奏：作为 SaaS/商业产品未公开版本号
- AWS/GCP/Azure 预测扩缩服务的 ML 模型内部算法细节：三家均不公开
- Karpenter + 预测扩缩直接集成：截至 2026 年 4 月无已知开源方案
- 生产环境 Transformer 模型在 K8s 扩缩中的应用：学术证明精度最优但无生产就绪工具
- 节点级 vs. Pod 级区分：多数学术和开源工具聚焦 pod 级 HPA 预测，真正直接预测节点数量的方案主要通过间接路径（预测 pod → CA/Karpenter 反应）
- 量化生产成果：来自 T1/T2 来源的预测节点扩缩具体降本/降延迟指标缺失


## Chapter 3：Scheduled and Calendar-Based Node Autoscaling
### 研究目标
- K8S 中实现定时节点扩缩的机制（KEDA Cron scaler 触发占位 pod、CronJob patch 节点组大小、Karpenter 定时超额预留、云厂商 ASG/MIG scheduled actions）
- 定时扩缩与反应式 autoscaler（CA/Karpenter）的交互方式：如何避免冲突、重复扩缩或过早缩容
- Cron 调度与日历感知逻辑的组合模式（假日日历、促销日历、发布窗口缓冲）
- 缩容调度的成本节约与过早终止节点风险之间的平衡策略

### 关键发现
- **KEDA Cron Scaler**（v2.19）：通过 cron 表达式定义时间窗口（五字段 Linux cron + IANA 时区），设置 `desiredReplicas` 作为 HPA 动态最小值（HPA 取所有指标最大值）。Pod 级触发，间接驱动节点扩缩——增加的 pod 资源请求超出集群容量时，CA/Karpenter 检测到 pending pod 并供给新节点。支持 cron + 其他触发器组合，窗口外可设 `minReplicaCount: 0` 实现 scale-to-zero。[KEDA Cron Scaler Docs](https://keda.sh/docs/2.19/scalers/cron/ "KEDA v2.19 official cron scaler documentation")
- **KEDA Cron + 占位 pod 模式**：使用低优先级 pause pod（`PriorityClass` 值 −10，CA 默认可支出阈值）预留容量，真实工作负载抢占占位 pod，被驱逐的占位 pod 变为 unschedulable 从而触发 CA/Karpenter 供给新节点。此模式在 CA FAQ 中正式记录。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "CA FAQ — overprovisioning with pause pods and PriorityClass −10")
- **AWS ASG Scheduled Actions**：每个 ASG 最多 125 个定时操作，支持 cron 表达式 + IANA 时区（自动处理 DST），可设置 `desiredCapacity`/`minSize`/`maxSize`，执行延迟一般数秒但可达 2 分钟。可与 CA 动态策略共存——定时操作设置地板（`minSize`），CA 在此范围内调整。[AWS Scheduled Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html "AWS EC2 Auto Scaling — Scheduled scaling")
- **GCP MIG Scaling Schedules**：每个 MIG 最多 128 个调度（支持一次性和循环），设置 `minRequiredReplicas` 作为地板；多调度重叠时取最大值。默认 UTC，支持 IANA 时区。调度到期后 10 分钟稳定期再缩容。可单独禁用/启用调度而不删除。适用于 GKE 节点池底层 MIG。[GCP Scaling Schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules "Compute Engine — Scaling based on schedules")
- **Azure VMSS Autoscale Profiles**：三种 profile 类型——默认、固定日期（一次性事件）、循环（周内天数），每 autoscale 设置最多 20 个 profile，按优先级评估（固定日期 > 循环 > 默认）。每个 profile 独立的 `capacity`（min/max/default）和最多 10 条指标规则。AKS 节点池底层为 VMSS。[Azure Autoscale Settings](https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-understanding-settings "Understand autoscale settings in Azure Monitor")
- **Karpenter 无原生定时扩缩**：截至 v1.0+ 无 cron 触发扩容功能，纯反应式。但 **disruption budgets** 支持 `schedule`/`duration` cron 字段（仅 UTC），可在指定时间窗口阻止合并/驱逐（如工作日 9 点起 8 小时内 `nodes: "0"` 禁止中断），可按 `reasons` 选择性阻止特定中断类型。[Karpenter Disruption Docs](https://karpenter.sh/docs/concepts/disruption/ "NodePool Disruption Budgets — schedule and duration fields")
- **Karpenter 定时扩缩社区模式**：(a) CronJob 创建/扩缩 KEDA 触发的占位 pod 触发 Karpenter 供给；(b) CronJob patch NodePool `spec.limits.cpu` 至 "0" 实现定时缩容（Aircall 案例：非生产环境节点成本降约 50%、集群总成本降约 25%）。核心组件（Karpenter、CoreDNS、CronJob pod）应运行在 Fargate 以保证 EC2 全部终止后仍可用。[Aircall Engineering Blog](https://aircall.io/blog/tech-team-stories/scale-karpenter-zero-optimize-costs/ "Aircall: ~50% node cost reduction") [AWS Containers Blog](https://aws.amazon.com/blogs/containers/manage-scale-to-zero-scenarios-with-karpenter-and-serverless/ "Karpenter scale-to-zero with serverless")
- **定时 + 反应式共存原则**：(1) 定时操作设置地板（`minSize`/`minRequiredReplicas`），反应式 autoscaler 负责天花板；(2) 调度到期后应有稳定期（GCP 10 分钟、CA `--scale-down-unneeded-time` 默认 10 分钟、KEDA `cooldownPeriod` 默认 5 分钟）；(3) Karpenter 使用 disruption budget `schedule` + `nodes: "0"` 保护高峰期节点不被合并。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "Key best practices")
- **日历感知扩缩模式**：GCP 支持一次性调度（cron 表达式含年份字段）用于事件预扩缩；Azure 固定日期 profile 覆盖特定活动期；AWS 一次性 scheduled action 无 `Recurrence`。动态日历集成（促销、发布日）通常通过外部控制器读取日历 API → 创建/更新 KEDA ScaledObject 或 scheduled action，截至 2026 年 4 月无 CNCF 成熟的标准化日历 Operator。发布窗口保护：Karpenter `karpenter.sh/do-not-disrupt: "true"` 注解、CA `cluster-autoscaler.kubernetes.io/scale-down-disabled: "true"` 注解。[GCP Scaling Schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules "One-time schedule for events") [CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "scale-down-disabled annotation")
- **缩容风险与缓解**：CA `--max-graceful-termination-sec` 默认 600 秒，Karpenter `terminationGracePeriod`。批处理工作负载用 `do-not-disrupt`/`safe-to-evict: "false"` 注解保护。缩容定时操作应比预期工作负载完成时间保守延后 30–60 分钟。Kubernetes 上游（v1.35）定义节点自动扩缩为供给（provisioning）+ 合并（consolidation）两阶段，本身不提供内建定时扩缩机制。[Kubernetes Node Autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/ "Kubernetes Node Autoscaling concepts")

### 可用图片
（无本地可用图片）

### 仍需补充
- Azure 定时 autoscale profile 与 AKS CA 的冲突细节：官方文档未明确说明二者共存行为
- GKE 节点池 + MIG 调度集成官方指南：机制通过底层 MIG 工作但缺 GKE 品牌专属文档
- KEDA Cron scaler → 新节点 Ready 的端到端延迟量化数据缺失
- 标准化日历感知扩缩 Operator：无 CNCF 成熟的开源方案
- Karpenter disruption budget 时区限制：仅支持 UTC，不支持本地时区


## Chapter 4：Proactive Overprovisioning and Hybrid Architectures
### 研究目标
- pause-container / 低优先级 pod 超额预留技术的机制与缓冲量确定最佳实践（静态 headroom vs. 按比例 headroom）
- 相关开源 Operator（Red Hat Proactive Node Scaling Operator、Cluster Proportional Autoscaler + Karpenter、自定义控制器）的功能与成熟度
- 多层参考架构模式（定时基线 + 预测调整 + 反应式安全网 + 超额预留缓冲）的成本、复杂度与可靠性权衡
- 跨云厂商（EKS + Karpenter、GKE + NAP、AKS 节点自动供给）及混合/本地集群的架构差异

### 关键发现
- **超额预留机制**：使用 `PriorityClass`（value: −10，恰好等于 CA 默认 `--expendable-pods-priority-cutoff`）的 `registry.k8s.io/pause` pod 预占容量。真实高优先级 pod 到达时抢占占位 pod，被驱逐的占位 pod 重新 Pending 触发 CA/Karpenter 供给替代节点，持续维护暖容量缓冲。此模式在 CA FAQ 中有正式文档。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "Official CA FAQ — overprovisioning section") [Kubernetes Pod Priority and Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/ "Stable since v1.14")
- **EKS 实操示例**：EKS Workshop 提供完整 walkthrough：`PriorityClass` "pause-pods" value: −1，全局默认 `PriorityClass` value: 0，2 个 pause pod 各请求 6.5 GiB 内存以占满近一整个 `m5.large` 实例，保持 2 个备用工作节点。[EKS Workshop](https://www.eksworkshop.com/docs/fundamentals/compute/managed-node-groups/cluster-autoscaler/overprovisioning/setting-up "EKS overprovisioning lab")
- **缓冲量确定**：**静态 headroom** 固定副本数+资源请求（如"始终保留 2 个备用节点"），简单但不随集群增长伸缩。**比例 headroom** 使用 Cluster Proportional Autoscaler (CPA) 按 linear 模式（`replicas = max(ceil(cores / coresPerReplica), ceil(nodes / nodesPerReplica))`）或 ladder 模式（阶梯函数）自动调整占位 pod 副本数。资源分配三策略：节点匹配（~75% 单节点 allocatable）、工作负载匹配（镜像目标工作负载请求量）、自定义。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "Dynamic overprovisioning with CPA") [SuperOrbital Blog](https://superorbital.io/blog/scaling-smarter-instant-nodes-zero-wait/ "Node-matching vs workload-matching strategies")
- **CA CapacityBuffer CRD（v1.35.0, v1beta1）**：CA v1.35.0（2026 年 1 月随 Kubernetes 1.35 "Timbernetes" 发布）引入一等 CRD `capacitybuffers.autoscaling.x-k8s.io`，无需手动管理 pause pod Deployment。Namespaced 作用域，与 ResourceQuota 集成，ProvisioningStrategy 暴露为字符串类型。`--capacity-buffer-controller-enabled` 和 `--capacity-buffer-pod-injection-enabled` 标志控制。GKE 在 Preview（≥ 1.35.2-gke.1842000）支持三种模式：固定副本、百分比（基于参考工作负载动态调整）、资源限额。[CA GitHub Releases](https://github.com/kubernetes/autoscaler/releases "CA 1.35.0 release notes") [GKE Capacity Buffer Concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer "GKE official docs, Preview, updated 2026-04-01")
- **开源 Operator**：**Red Hat Proactive Node Scaling Operator**（`redhat-cop/proactive-node-scaling-operator`，Apache 2.0）引入 `NodeScalingWatermark` CRD，通过 `watermarkPercentage`（如 20% 表示用户负载达 80% 即开始扩缩）和 `nodeSelector` 动态调整 pause pod 数量，支持离线环境（可配 `PausePodImage`）。[Red Hat Proactive Node Scaling Operator](https://github.com/redhat-cop/proactive-node-scaling-operator "GitHub repo") [Red Hat Blog](https://www.redhat.com/en/blog/how-full-is-my-cluster-part-6-proactive-node-autoscaling "Design rationale")。**Cluster Proportional Autoscaler (CPA)**（kubernetes-sigs 项目）支持 linear/ladder 模式，常与超额预留 Deployment 配对。**Codecentric cluster-overprovisioner**（Helm chart）将 CPA + pause pod + CronJob 定时切换配置打包为一体化方案。[CPA GitHub](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler "kubernetes-sigs project") [Codecentric GitHub](https://github.com/codecentric/cluster-overprovisioner "Helm chart with CPA + cron scheduling")
- **Karpenter 与超额预留**：截至 2026 年 4 月无原生 headroom 功能（GitHub Issue #3240 仍开放），社区仍推荐 pause pod 模式。Karpenter 优势在于直接调用 EC2 Fleet API 而非 ASG，节点就绪通常 60–90 秒 vs. CA 的 2–5 分钟。[Karpenter Issue #3240](https://github.com/aws/karpenter-provider-aws/issues/3240 "Feature request for native overprovisioning, still open") [AWS Containers Blog](https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning/ "Karpenter + overprovisioning + CPA on EKS")
- **跨云实现**：**GKE** 提供传统 PriorityClass + placeholder pod 模式与 CapacityBuffer CRD（Preview）双路径；Autopilot 按 pod 资源请求计费，Standard 按底层 VM 计费。优先级阈值 −10：低于 −10 的 pod **不触发**新节点创建。[GKE Capacity Provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning "Official GKE guide")。**AKS NAP** 基于 Karpenter，使用 `NodePool` + `AKSNodeClass` CRD，与 CA 互斥不能同时启用；截至 2026 年 2 月不支持 Windows 节点池、IPv6 或 Service Principal。[AKS NAP](https://learn.microsoft.com/en-us/azure/aks/node-auto-provisioning "Microsoft docs, updated 2026-02-15")。**EKS + Karpenter** 是最成熟的 Karpenter 部署，AWS 另提供 EC2 Warm Pools（VM 级停止/休眠预初始化）作为补充。
- **多层参考架构**：四层互补——(1) 反应层（CA/Karpenter 安全网）+ (2) 预测层（ML 预测提前扩缩，见 Ch2）+ (3) 定时层（cron 调度已知模式，见 Ch3）+ (4) 超额预留缓冲层（pause pod 吸收瞬时尖峰）。SuperOrbital 实操示例：基础 pause pod Deployment + KEDA Cron 触发在工作日 08:45 将占位副本从 5 提升至 20 + KEDA CPU 触发应对不可预测突发。[SuperOrbital Blog](https://superorbital.io/blog/scaling-smarter-instant-nodes-zero-wait/ "Concrete KEDA + cron + overprovisioning example")
- **成本开销**：2 节点缓冲（m5.large @$0.096/hr）年成本约 $1,682——以小代价消除 1–2 分钟扩缩延迟。定时超额预留（非高峰时段降低缓冲）可减少 40–60% 成本。GKE 推荐 CapacityBuffer 用于 AI 推理、零售促销、游戏服务器等延迟敏感场景。[AWS Containers Blog](https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning/ "Performance vs cost trade-off") [GKE Capacity Buffer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer "Use cases: AI inference, retail, gaming")
- **本地/混合集群**：裸金属 PXE boot 供给 5–15 分钟（远长于云 1–2 分钟），超额预留在本地更为关键，建议 watermark 20–30%。Cluster API (CAPI) 提供基础设施无关节点生命周期管理（Machine/MachineSet/MachineDeployment）。CA 1.35.0 含 CAPI 特定修复（scale-from-zero 标签传播、竞态/死锁修复）。混合架构中超额预留可在本地维护基线暖容量，云端通过 Karpenter/CA 处理溢出。Kubernetes 上游提供专门的 [Node Overprovisioning 任务指南](https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/ "Official K8s task guide for node overprovisioning")。

### 可用图片
（无本地可用图片）

### 仍需补充
- 具体成本基准研究：无 T1/T2 发表的"X% 超额预留开销带来 Y% P99 调度延迟降低"量化基准
- CapacityBuffer CRD 上游完整 YAML 规格与示例（GKE 外）：仅在 release notes 中概述
- Red Hat Proactive Node Scaling Operator 最新发布版本号：GitHub releases 页未提取到具体 tag
- 裸金属供给延迟精确数据：5–15 分钟为行业通用估计，因硬件和工具差异大
- AKS 专属超额预留指南：微软无与 EKS Workshop / GKE capacity provisioning 对等的专题文档


## Chapter 5：Implementation Best Practices and Operational Playbook
### 研究目标
- 在现有 CA/Karpenter 之上引入预测/定时扩缩的低风险上线策略（影子模式、金丝雀节点池、渐进流量切换）
- 多层 autoscaling 栈的监控、告警与仪表盘模式（扩缩决策审计日志、预测 vs. 实际仪表盘、节点周转指标）
- 安全护栏（最小/最大节点数、扩缩速率限制、断路器、PodDisruptionBudget、优雅排空超时）
- 成本治理结构（节点小时预算告警、Spot/抢占式实例集成、空闲节点回收 SLA）

### 关键发现
- **上线策略**：GCP 预测自动扩缩提供内建 observe-only 模拟（对比过去 7 天实际组大小与预测推荐值），无需实际启用即可评估效果。[GCP Predictive Autoscaling](https://cloud.google.com/compute/docs/autoscaler/predictive-autoscaling "GCP built-in shadow mode")。K8s 原生无内建 shadow mode，推荐**金丝雀节点池**模式：Karpenter `spec.weight` 设低权重测试预测池，或 CA `--expander=priority` 配合 ConfigMap 将预测 ASG 设低优先级回退至反应式 ASG。[Karpenter NodePool Docs](https://karpenter.sh/v1.0/concepts/nodepools/ "NodePool weight") [AWS EKS CA Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html "Priority expander")
- **CA 安全护栏关键标志**：`--max-nodes-total`（默认无限制，全局节点上限）、`--scale-down-utilization-threshold`（默认 0.5，低于此比例的节点可缩容）、`--scale-down-unneeded-time`（默认 10 分钟，节点须持续空闲此时长方可移除）、`--scale-down-delay-after-add`（默认 10 分钟，扩容后暂停缩容评估）、`--max-graceful-termination-sec`（默认 600 秒）、`--max-total-unready-percentage`（默认 45%，超出即停止所有扩缩操作——断路器）、`--cores-total`（默认 0:320000）/ `--memory-total`（默认 0:6400000 GB，全局资源上限）、`--max-empty-bulk-delete`（默认 10，空节点批量删除上限）、`--scan-interval`（默认 10s，AWS 建议 30–60s 降低 API 调用量）。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "Complete CA parameter reference") [AWS EKS CA Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html "Scan interval tradeoff")
- **Karpenter NodePool 限制与 disruption budgets**：`spec.limits`（cpu/memory/GPU 上限，达到即停止供给），disruption budgets 默认 `nodes: 10%`，支持 cron `schedule`+`duration` 窗口阻止中断（如工作日 8 小时内 `nodes: "0"`），可按 `reasons` 选择性阻止。`consolidateAfter` 控制 pod 离开到节点可合并的延迟（设 `Never` 可完全禁用）。`terminationGracePeriod` 设排空上限，超时后强制删除 pod，使节点即使有阻塞 PDB 的 pod 也可在超时后被中断。`karpenter.sh/do-not-disrupt` 注解阻止自愿中断。[Karpenter NodePool Docs](https://karpenter.sh/v1.0/concepts/nodepools/ "spec.limits, consolidateAfter") [Karpenter Disruption Docs](https://karpenter.sh/docs/concepts/disruption/ "Disruption budgets, terminationGracePeriod, do-not-disrupt")
- **CA 事件与可观测性**：CA 发布状态至 ConfigMap `cluster-autoscaler-status`（`--write-status-configmap=true`），事件默认 5 分钟去重（`--record-duplicated-events` 可关闭），Prometheus 指标暴露于 `:8085/metrics`。GKE 额外输出结构化 JSON 可见性事件至 Cloud Logging（`container.googleapis.com/cluster-autoscaler-visibility`），含 `scaleUp`/`scaleDown`/`noScaleUp`/`noScaleDown` 等事件类型及详细上下文（触发 pod、MIG 名称、CPU/内存比率）。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "CA monitoring") [GKE Autoscaler Visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility "Structured visibility events")
- **Karpenter Prometheus 指标**：暴露于 `karpenter.kube-system.svc.cluster.local:8080/metrics`。关键稳定指标：`karpenter_nodeclaims_created/terminated_total`、`karpenter_nodes_created/terminated_total`、`karpenter_pods_startup_duration_seconds`、`karpenter_cluster_state_node_count`。中断指标：`karpenter_voluntary_disruption_decisions_total`、`karpenter_voluntary_disruption_eligible_nodes`。NodePool 容量：`karpenter_nodepools_usage`/`limit`（可告警池接近上限）。云厂商：`karpenter_cloudprovider_errors_total`、`karpenter_cloudprovider_instance_type_offering_price_estimate`。Spot 中断：`karpenter_interruption_received_messages_total`。开源 **kubernetes-autoscaling-mixin** 提供 3 个 Grafana 仪表盘（Overview/Activity/Performance）+ 3 个预置告警（CloudProviderErrors / TerminationDurationHigh / NodepoolNearCapacity）。[Karpenter Metrics Reference](https://karpenter.sh/docs/reference/metrics/ "Official metrics docs") [Karpenter Monitoring Blog](https://hodovi.cc/blog/karpenter-monitoring-with-prometheus-and-grafana/ "Grafana dashboards and alerts")
- **PDB 最佳实践**：CA（v0.5+）和 Karpenter 均通过 Eviction API 尊重 PDB。推荐使用 `maxUnavailable` 而非 `minAvailable`（自动适应副本数变化）。`maxUnavailable: 0` 或 `minAvailable: 100%` 会永久阻塞节点排空。`unhealthyPodEvictionPolicy: AlwaysAllow`（自 K8s v1.31 稳定）允许驱逐不健康 running pod（如 CrashLoopBackOff），防止其通过 PDB 阻塞排空。kube-system pod 应显式创建 PDB 以允许 CA 迁移。[Kubernetes PDB Docs](https://kubernetes.io/docs/tasks/run-application/configure-pdb/ "PDB configuration guide") [CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "CA PDB interaction")
- **Spot/抢占式实例集成**：Karpenter 使用 Price Capacity Optimized (PCO) 策略——先选最高可用容量 Spot 池，再选最低价格。Spot 容量不足时临时移除该池 3 分钟，若无 Spot 可用"通常毫秒级"回退 On-Demand。原生 SQS 中断处理：收到 2 分钟 Spot 中断通知后自动 cordon+drain 并并行供给替代节点（`--interruption-queue-name` 配置）。Spot-to-Spot 合并（`SpotToSpotConsolidation` feature gate，v0.34.0+）需最少 15 种实例类型。CA 环境建议 Spot 与 On-Demand 隔离至独立 ASG，搭配 `--expander=least-waste`。[AWS Spot+Karpenter Blog](https://aws.amazon.com/blogs/containers/using-amazon-ec2-spot-instances-with-karpenter/ "Spot allocation, fallback, interruption handling") [AWS EKS CA Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html "Spot best practices for CA")
- **成本治理**：**OpenCost**（CNCF Sandbox，Apache 2.0）提供按集群/节点/命名空间/pod 的实时成本分配，支持多云计费 API 集成。**Kubecost**（基于 OpenCost 引擎）增加企业级预算告警、RBAC 成本策略、异常检测。AWS 推荐 CloudWatch Billing Alarms + Cost Anomaly Detection + Karpenter `spec.limits` + 日志 Metrics Filter 检测"exceeds limit"消息触发告警。空闲节点回收：Karpenter `WhenEmptyOrUnderutilized` 合并策略搭配 `consolidateAfter`（如 1m），CA 对应 `--scale-down-unneeded-time`（默认 10 分钟）+ `--scale-down-utilization-threshold`（默认 0.5）。[OpenCost GitHub](https://github.com/opencost/opencost "OpenCost repository") [AWS EKS Karpenter Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html "Cost governance with Karpenter")
- **故障模式与断路器**：CA 内建断路器——`--max-total-unready-percentage`（默认 45%）或 `--ok-total-unready-count`（默认 3）超出即停止所有扩缩操作。缩容失败后 backoff `--scale-down-delay-after-failure`（默认 3 分钟），节点组 backoff 从 `--initial-node-group-backoff-duration`（默认 5 分钟）升级至 `--max-node-group-backoff-duration`（默认 30 分钟）。Karpenter **Node Auto Repair**（alpha v1.1.0+）：自动识别不健康节点（如 `Ready=False` 30 分钟），NodePool 内 >20% 不健康时停止修复防级联。GCP 预测扩缩在实际用量偏离预测时数分钟内重算预测，实际超过预测时实时信号优先（不会因预测不足而低供给）。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "Unready nodes, backoff durations") [Karpenter Disruption Docs](https://karpenter.sh/docs/concepts/disruption/ "Node Auto Repair") [GCP Predictive Autoscaling](https://cloud.google.com/compute/docs/autoscaler/predictive-autoscaling "Forecast error adaptation")
- **多层扩缩栈可观测仪表盘推荐**：(a) 预测 vs. 实际节点数时间序列对比；(b) 扩缩决策审计日志（CA 事件 / Karpenter 事件 + 预测模型输出时间戳关联）；(c) 节点周转率（`karpenter_nodes_created/terminated_total` 速率检测振荡）；(d) Pod 调度延迟（`karpenter_pods_startup_duration_seconds`）。CA 栈结合 GKE Cloud Logging 结构化事件或 EKS CloudWatch Logs 转发实现跨层关联。[Karpenter Metrics](https://karpenter.sh/docs/reference/metrics/ "Multi-layer observability metrics") [GKE Autoscaler Visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility "Cloud Logging integration")

### 可用图片
（无本地可用图片）

### 仍需补充
- AKS 专属 CA 可观测性与预测扩缩最佳实践：Azure Monitor / Container Insights 集成细节未深入研究
- 预测模型专用断路器模式：无 T1/T2 权威来源记录具体的"预测误差超阈值自动回退反应式"命名模式
- Kubecost 告警配置详细参数：节点小时预算专项告警的具体配置参数待确认
- 预测精度阈值量化基准：无行业标准的"MAPE 超 X% 即禁用预测扩缩"数值，需按组织 SLO 设定
- AWS Predictive Scaling + EKS 节点组集成模式（蓝绿部署下自定义指标保留）需进一步研究


## Chapter 6：Evaluation Framework and Comparative Analysis
### 研究目标
- 节点级 autoscaling 策略比较的关键评估维度（扩缩延迟、成本效率、SLO 达成率、运维复杂度、跨云可移植性）
- 压力测试/模拟基准设计方法（合成流量回放、混沌工程集成）以现实地检验预测与定时扩缩逻辑
- 各方案在代表性负载原型（日间 Web 流量、批量/ML 训练突发、事件驱动尖峰）上的评估维度对比
- 引导团队根据自身负载画像和运维成熟度选择正确扩缩策略组合的决策框架或流程图

### 关键发现
- **基准测试与模拟工具**：**ClusterLoader2 (CL2)** 是官方 Kubernetes 可扩展性测试框架（`kubernetes/perf-tests`），用于发布阻塞性扩展测试；Amazon EKS 内部使用 CL2 进行 5,000 节点可扩展性验证。[ClusterLoader2 GitHub](https://github.com/kubernetes/perf-tests "Official K8s performance tests") [AWS EKS Scalability Blog](https://aws.amazon.com/blogs/containers/deep-dive-into-amazon-eks-scalability-testing/ "EKS 5000-node scalability testing with CL2, 2024")。**Kube-burner**（CNCF Sandbox，2023 年 12 月接纳）用于 K8s 性能与规模测试编排。[kube-burner GitHub](https://github.com/kube-burner/kube-burner "CNCF Sandbox project")。**KWOK**（SIG 赞助工具集）可在秒级内模拟数千节点（无实际基础设施），AWS 已发布 Karpenter + KWOK 成本建模方法论。[KWOK official blog](https://kubernetes.io/blog/2023/03/01/introducing-kwok/ "KWOK introduction, March 2023") [AWS Karpenter+KWOK Blog](https://aws.amazon.com/blogs/containers/migrate-to-amazon-eks-data-plane-cost-modeling-with-karpenter-and-kwok/ "Cost modeling with Karpenter and KWOK, August 2025")。**SimKube**（v1.0，2024 年 9 月）基于 KWOK 的录制-回放 K8s 模拟器，可在相同工作负载 trace 下对比不同 autoscaling 配置。[SimKube GitHub](https://github.com/acrlabs/simkube "Record-and-replay K8s simulator")
- **CA vs. Karpenter SimKube 模拟对比**：在约 1,000 pending pod 规模下，Karpenter 供给控制器（fast loop）每次调谐最长约 12 秒 vs. CA 主循环 20–60 秒；Karpenter 在 scale-out 过渡期间的 pending pod 约少 75%。Karpenter 使用双循环架构（快速供给循环 + 较慢中断循环），CPU 消耗 1–2 vCPU vs. CA 的 2–3 vCPU。Karpenter 在 10 次 trace 回放中实例类型选择高度一致，CA 因默认随机选择等价类型而不确定性更高。[SimKube CA vs Karpenter](https://blog.appliedcomputing.io/p/using-simkube-10-comparing-kubernetes "SimKube 1.0: CA vs Karpenter, September 2024")
- **Kubernetes 官方 SLI/SLO**：Scalability SIG 定义三项 SLO——(1) API 请求延迟（变更）p99 ≤1s；(2) API 请求延迟（只读）p99 单资源 ≤1s、命名空间/集群范围 ≤30s；(3) Pod 启动延迟 p99 ≤5s（可调度无状态 pod，不含镜像拉取和 init 容器）。SLI 指标 `apiserver_request_sli_duration_seconds` 和 `kubelet_pod_start_sli_duration_seconds`（K8s 1.27+）可用于监控 autoscaler 对控制面性能的影响。[AWS EKS Scalability Blog](https://aws.amazon.com/blogs/containers/deep-dive-into-amazon-eks-scalability-testing/ "K8s SLIs/SLOs defined in EKS scalability testing")
- **SLO 驱动评估框架（学术）**：Punniyamoorthy et al. (IEEE 2025) 提出四维度评估方法——(1) SLO 达成率（违规频率与持续时间）；(2) 扩缩响应性（工作负载变化到资源调整延迟）；(3) 成本效率（平均副本数/节点小时）；(4) 稳定性（扩缩振荡与副本周转）。与 K8s 默认 autoscaling 基线相比，该框架将 SLO 违规持续时间降低最高 **31%**，扩缩响应时间改善 **24%**，基础设施成本降低 **18%**。评估工作负载模式包括突发、队列驱动、混合三类。[Punniyamoorthy et al.](https://arxiv.org/html/2512.23415v1 "SLO Driven and Cost-Aware Autoscaling Framework for Kubernetes, IEEE 2025")
- **混沌工程验证工具**：**LitmusChaos**（CNCF Incubating）提供 `pod-autoscaler` 混沌实验——将 Deployment 扩缩至可配副本数并验证 CA 是否能供给足够节点容量。AWS 发布了 EKS 上的 walkthrough。[AWS LitmusChaos Blog](https://aws.amazon.com/blogs/containers/chaos-engineering-with-litmuschaos-on-amazon-eks/ "LitmusChaos on EKS, Dec 2021")。**Chaos Mesh**（CNCF Incubating）提供 PodChaos/NetworkChaos/StressChaos 及 Workflow 编排，通过 CRD 原生集成，可模拟节点级压力条件触发 autoscaler 响应。[Chaos Mesh](https://chaos-mesh.org/ "CNCF Incubating project")
- **成本效率实际案例**：HP PrintOS 采用 Karpenter (v0.36.1) 后 EKS 工作节点利用率提升 **40%**，结合 Spot 实例非生产工作流年省 **$125K+**，节点升级工程量减少 8 倍（从约 2 小时/集群降至约 15 分钟/集群）。[AWS HP Karpenter Blog](https://aws.amazon.com/blogs/containers/how-hp-achieved-40-improvement-in-kubernetes-node-utilization-utilization-on-amazon-eks-using-karpenter/ "HP PrintOS 40% utilization improvement, Nov 2024")
- **跨云可移植性**：CA 支持所有主要云厂商（AWS/GCP/Azure）及阿里云、DigitalOcean、OCI 等，是多云环境最具可移植性的选择。Karpenter 一等支持 AWS，Azure 有 Karpenter provider（NAP），GCP 目前无原生 Karpenter provider；KWOK provider 支持任意环境的无基础设施模拟。[CA FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md "Cloud provider support listing")
- **建议评估维度（分析性框架）**：(1) 扩缩延迟（检测延迟 + 决策延迟 + 供给延迟 + 注册延迟）；(2) 成本效率（bin-packing 效率、Spot 利用率、空闲节点小时、超额预留开销、合并有效性）；(3) SLO 达成率（Pod 调度失败频率与持续时间、延迟 SLO 违规比例）；(4) 运维复杂度（CRD/配置数量、CI/CD 集成、监控需求、团队技能门槛）；(5) 可移植性（跨云厂商支持、多云/混合云兼容性）；(6) 稳定性与可预测性（振荡频率、节点周转、决策一致性、部分故障行为）；(7) 工作负载原型适配度（日间 Web 流量、批量/ML 突发、事件驱动尖峰、混合负载）
- **策略选择决策框架（分析性，非来源于权威出版物）**：(1) 工作负载可预测性高 → 定时/cron 或云原生预测扩缩；不可预测 → 反应式 + 超额预留缓冲；(2) 延迟敏感（亚分钟扩缩）→ Karpenter (60–90s) + 超额预留（即时暖池）优于 CA (2–5 min)；(3) 多云约束 → CA（最广厂商支持）优于 Karpenter（AWS 优先）；(4) 运维成熟度低 → CA（更简单、文档更全）或云原生托管方案；高 → Karpenter 高级优化；(5) 成本优化优先 → Karpenter bin-packing + Spot 优先供给，或混合多层策略（预测基线 + 反应式突发）

### 可用图片
（无本地可用图片）

### 仍需补充
- GKE NAP / Autopilot 精确延迟基准数据：无公开发布的 pending pod 到节点就绪的具体秒数
- AKS NAP (Karpenter provider) 延迟基准数据：无已发布基准
- 跨全部 7 种策略的统一成本效率对比研究：存在个别数据点但无单一研究在相同工作负载上对比所有策略
- CNCF 或厂商发布的正式策略选择决策树/流程图：未找到官方出版物，本章决策框架为分析性提议
- Karpenter 官方文档中的节点就绪时间 (60–90s) 保证：此数字广泛引用于社区博客但非官方 SLO
- 云原生预测扩缩精度基准：无已发布的 AWS/GCP/Azure 预测扩缩在节点级上下文中的预测准确率或误报率基准


# Section 2：给 Write 阶段的执行建议
- **术语统一**：首次出现使用"Cluster Autoscaler (CA)"，之后统一用"CA"。Karpenter 不缩写。伞形术语使用"node-level autoscaling"而非"cluster scaling"或"infrastructure scaling"。全文区分 pod-level scaling（HPA/VPA/KEDA replica scaling）与 node-level scaling，报告范围是后者，但必须承认前者作为触发机制的角色。
- **范围锚定**：每章简要重申焦点在节点供给与退役，而非 pod 副本数，尤其在 Chapter 2 和 Chapter 3 讨论 KEDA 时。
- **云厂商平衡**：AWS (EKS)、GCP (GKE)、Azure (AKS) 大致等深度覆盖，避免 AWS 中心化叙述。云厂商特有功能需明确标注。
- **时间锚点**：报告锚定于 2026 年 4 月。引用项目版本、GA 日期或生态成熟度时使用具体日期或版本号，避免"最近""即将"等模糊表述。时间口径：回顾过去 12 个月（2025-04 至 2026-04），展望未来 6 个月（至 2026-10）。
- **架构图指引**：Chapter 4 和 Chapter 5 应各包含至少一张参考架构图，展示反应式 + 预测 + 定时层的交互。
- **语气与文体**：全文正式研究报告语气，使用"we assess""evidence suggests""the data indicates"，允许第一人称复数("we") 用于分析性判断。
- **量化严谨性**：比较扩缩延迟、成本或预测模型精度时，坚持使用具体数值、单位、时间范围与引用来源，避免"快很多""便宜许多"等无数据支撑的模糊修饰。
- **跨章连贯**：Chapter 1 界定问题 → Chapter 2–4 按预测 / 定时 / 混合轴呈现方案 → Chapter 5 综合为可操作实践 → Chapter 6 提供评估镜头。各章前后引用，构建连贯叙事。
- **Chapter 2 与 Chapter 3 去重**：KEDA cron scaler 归 Chapter 3；KEDA predictive/AI scaler 归 Chapter 2。交叉引用但不重复描述。
- **开源项目覆盖清单**：至少覆盖 Kubernetes Cluster Autoscaler、Karpenter、KEDA（cron + predictive scalers）、Kedify、Red Hat Proactive Node Scaling Operator、Cluster Proportional Autoscaler，以及研究中发现的新兴项目。每个项目须注明许可证、CNCF 状态、最新发布日期。
