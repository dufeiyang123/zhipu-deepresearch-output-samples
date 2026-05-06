# Section 1：章节研究计划

## Chapter 1：时间序列流失（Churn）的概念与成因

### 研究目标
- 定义 Prometheus 语境下"时间序列 churn"的准确含义，阐明其与高基数（high cardinality）的区别与联系
- 系统梳理在 Kubernetes 云原生环境中导致高流失率的典型成因（Pod 频繁重建、滚动更新、HPA 自动扩缩容、Job/CronJob 生命周期短暂、标签值不受控膨胀等）
- 为后续所有讨论建立共同术语基础

### 关键发现
- 发现 1：Prometheus 数据模型中，每条时间序列由指标名称加标签键值对唯一标识，任何标签值变化都会创建全新序列。[Prometheus 官方数据模型文档](https://prometheus.io/docs/concepts/data_model/ "Prometheus Data Model — 标签变化即创建新序列")
- 发现 2：Churn rate（流失率）的权威定义为"旧时间序列被新时间序列替代的速率"。Kubernetes 滚动更新等操作导致 `pod_name` 等标签值批量变化，引发大规模序列更替。[VictoriaMetrics 作者 Aliaksandr Valialkin 博文](https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48 "Prometheus storage: technical terms for humans")
- 发现 3：Robust Perception 将 churn 定义为"时间序列集合的变化频率"，与 cardinality（基数）并列为 Prometheus 资源使用和效率的两个核心问题。[Robust Perception 博文](https://www.robustperception.io/using-tsdb-analyze-to-investigate-churn-and-cardinality "Using tsdb analyze to investigate churn and cardinality")
- 发现 4：Prometheus TSDB Head Block 是内存中的活跃数据区域，新采集样本先写入 Head Block 活跃 chunk 和 WAL。数据跨度达 3 小时后，最早 2 小时数据压缩为持久化 block。[Ganesh Vernekar 系列博文 Part 1](https://ganeshvernekar.com/blog/prometheus-tsdb-the-head-block/ "Prometheus TSDB The Head Block")
- 发现 5：Prometheus 2.0 引入 staleness 机制，注入 stale marker 标记序列失活。Head Block compaction 时对倒排索引进行 GC，高 churn 意味着创建→标记失活→GC 循环极其频繁，导致 Head Block 倒排索引不断膨胀和重建。[Robust Perception PromCon 2017 演讲](https://promcon.io/2017-munich/slides/staleness-in-prometheus-2-0.pdf "Staleness in Prometheus 2.0")
- 发现 6：TSDB 持久化 block 索引采用 Symbol Table + Postings Lists 结构。高 churn 下每个 2 小时 block 包含大量短命序列，导致 Postings 列表稀疏化、Symbol Table 膨胀、索引体积增大。[Ganesh Vernekar 系列博文 Part 4](https://ganeshvernekar.com/blog/prometheus-tsdb-persistent-block-and-its-index/ "Prometheus TSDB Persistent Block and its Index")
- 发现 7：`promtool tsdb analyze` 工具可诊断 churn 和 cardinality 问题，其输出中"Label pairs most involved in churning"展示各标签对的 sparseness 值——值越高代表序列生命周期越短、churn 越严重。[Robust Perception 博文](https://www.robustperception.io/using-tsdb-analyze-to-investigate-churn-and-cardinality "Using tsdb analyze to investigate churn and cardinality")
- 发现 8：High cardinality 是"静态"规模问题（唯一序列总数过多），churn rate 描述动态更替速率。高 churn rate 持续推高 cardinality，因为在 Head Block retention 窗口（2-3 小时）内新旧序列同时存在，可能导致性能下降、高内存使用和 OOM。[Aliaksandr Valialkin 博文](https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48 "Prometheus storage: technical terms for humans — 'high churn rate increases the cardinality'")
- 发现 9：Grafana Labs 指出 Kubernetes 多层抽象（Pod/Container/Node/Namespace）天然产生高基数，短暂工作负载特性进一步加速序列更替。[Grafana Labs 博文](https://grafana.com/blog/what-is-high-cardinality-and-is-it-as-scary-as-people-make-it-out-to-be-/ "What is high cardinality — Grafana Labs")
- 发现 10：`kube_pod_status_phase` 等 kube-state-metrics 指标在 Pod 状态每次变化时生成新序列，配合大量短运行 Job 产生显著指标增长。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics in Prometheus and Kubernetes")
- 发现 11（Pod 频繁重建）：CrashLoopBackOff 或 OOMKill 导致 Pod 反复重启，每次获得新 Pod 名称后缀，所有包含 `pod` 标签的指标序列被替换。[Prometheus-users 邮件列表讨论](https://groups.google.com/g/prometheus-users/c/wRtG7zq6sZ4 "performance impact of high churn rate")
- 发现 12（滚动更新）：Deployment rollout 时新旧 Pod 名称和 IP 变化，所有以 `pod`/`instance` 为标签的指标序列经历完整 churn。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics")
- 发现 13（自动扩缩容）：HPA 扩缩容、VPA 调整 Pod 规格、Cluster Autoscaler 增减节点均可触发 Pod 和序列变动，在流量波动频繁的微服务架构中反复发生。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics")
- 发现 14（Job/CronJob）：每次 Job 执行创建全新 Pod，完成后序列变为 stale。高频 CronJob（如每分钟执行一次）每次执行产生一批新序列。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics — short running jobs")
- 发现 15（标签值膨胀）：`pod` 名称、container ID、`instance` IP:Port 等标签值在 K8s 环境中动态且无上界。Brian Brazil 建议任何单个指标在 `/metrics` 端点上的基数不应超过 10，超过 100 需格外谨慎。[Robust Perception 博文](https://www.robustperception.io/cardinality-is-key "Cardinality is key — Brian Brazil")
- 发现 16（Sidecar 指标维度爆炸）：Istio Envoy sidecar 生成 `istio_requests_total` 等多维指标。AWS 场景假设：50 微服务 × 10 实例 × 20 sidecar 指标 = 10,000 基础指标，加上标签组合后基数可达数亿。[AWS 博文](https://aws.amazon.com/blogs/mt/how-to-reduce-istio-sidecar-metric-cardinality-with-amazon-managed-service-for-prometheus/ "How to reduce Istio sidecar metric cardinality") [Istio GitHub Issue #19090](https://github.com/istio/istio/issues/19090 "Huge cardinality jump with telemetry v2")
- 发现 17：Prometheus 暴露 `prometheus_tsdb_head_series`（Gauge）、`prometheus_tsdb_head_series_created_total`（Counter）、`prometheus_tsdb_head_series_removed_total`（Counter）用于观测 churn。`rate(prometheus_tsdb_head_series_created_total[5m])` 可估算 churn rate。[Aliaksandr Valialkin 博文](https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48 "Prometheus storage: technical terms for humans")
- 发现 18：自 Prometheus v2.10 起引入 per-target 级 `scrape_series_added` 指标，可按 job 定位高 churn 来源。[Aliaksandr Valialkin 博文](https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48 "scrape_series_added 用于定位 churn 来源")
- 发现 19：GitHub Issue #4547（2018 年 8 月 brancz 提出）最早正式提议在 Prometheus 中添加序列 churn 跟踪能力。[Prometheus GitHub Issue #4547](https://github.com/prometheus/prometheus/issues/4547 "Add ability to track series churn")
- 发现 20：OKD 官方文档提供实用 PromQL `topk(10, sum by(namespace, job) (sum_over_time(scrape_series_added[1h])))` 定位 churn 热点。[OKD 文档](https://docs.okd.io/4.13/support/troubleshooting/investigating-monitoring-issues.html "Investigating monitoring issues")
- 发现 21：Prometheus 官方配置文档在 OTLP 接收器配置中明确提到某些选项"may cause high time series churn"，证明 churn 是官方认可的技术术语。[Prometheus 官方配置文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "Prometheus Configuration — OTLP churn 警告")

### 可用图片
（暂无）

### 仍需补充
- Prometheus 源码 `tsdb/head.go` 中关于 `prometheus_tsdb_head_series_created_total` 和 `_removed_total` 指标注册的具体代码片段（当前仅通过二手文献确认指标名称）
- 关于 churn 对 WAL 体积的具体量化影响的一手数据（目前仅有定性描述）
- VPA 触发 Pod 重建导致 churn 的具体案例数据（目前基于原理推断，未找到带量化数据的一手来源）

---

## Chapter 2：高流失率对 Prometheus 及其上下游的影响

### 研究目标
- 量化和结构化地分析高 churn 对 Prometheus 自身以及上下游系统所造成的具体影响
- 覆盖维度：内存与 CPU 开销（TSDB Head 块膨胀、倒排索引压力）、磁盘存储与压缩效率下降、查询延迟与超时风险、远程写放大（Remote Write 流量激增）、远程长期存储后端的摄取与存储成本膨胀、告警规则评估准确性与可靠性下降
- 将技术机理与可观测的业务后果对应起来

### 关键发现
- 发现 1（每序列内存开销的权威量化）：Prometheus 核心维护者 Ben Kochie 指出，Prometheus 典型的每序列内存占用约为 8 KiB（`process_resident_memory_bytes / prometheus_tsdb_head_series`），主要由索引结构贡献。100 万活跃序列约需 8 GB 内存，1000 万约需 80 GB。[Prometheus-users 邮件列表（Ben Kochie 回复）](https://groups.google.com/g/prometheus-users/c/uaJKg5RcC3g "Prometheus correlation between memory usage and timeseries - 'The current typical use is around 8KiB per series'")
- 发现 2（更细致估算）：Last9 深度技术分析给出更细致的分解：每创建一条新序列需执行哈希计算、分配约 200 字节 series struct、为每个标签创建 Postings 列表条目、写入 WAL、分配至少 128 字节 chunk head——总计约 3-4 KB/活跃序列（Head Block 中）。100 万序列约需 3-4 GB（仅序列元数据开销）。[Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics: How Prometheus and ClickHouse Handle Scale")
- 发现 3（Coveo 生产案例：550 万总序列 → 30+ GB 内存）：Coveo 公司记录了一个高 churn 生产案例：640 个 target、每秒 20,000 samples、100 万活跃序列，但因 churn 导致 Head Block 中累积 550 万总序列。Go profiler 发现 `index.(*decbuf).uvarintStr` 占 15.64%、`seriesHashmap.set` 占 11.52%、`newMemSeries` 占 8.03%、`(*MemPostings).Delete` 占 3.46%——均为高 churn 直接驱动的热点。[Coveo 技术博客](https://source.coveo.com/2021/03/03/prometheus-memory/ "Prometheus - Investigation on high memory consumption")
- 发现 4（去除高 churn 标签后内存立降 375%）：Coveo 案例中通过 `tsdb analyze` 诊断发现 kubelet/cadvisor 的 `id` 标签（container ID，cardinality 达 116,525）是 churn 最大来源。仅通过 `metric_relabel_configs` 丢弃 `id` 标签，样本率降低 75%，内存从约 30 GB 降至约 8 GB。[Coveo 技术博客](https://source.coveo.com/2021/03/03/prometheus-memory/ "Prometheus - Investigation on high memory consumption")
- 发现 5（Last9 案例：200 Pod × pod_id 标签 → 15 万新序列/小时）：某团队为调试添加 `pod_id` 标签，200 Pod × 50 指标，部署期 Pod 每 2 分钟 churn 一次，导致每小时创建 150,000 条新序列。内存一周内从 8 GB 涨至 32 GB，最终 OOMKill 导致告警中断。[Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics")
- 发现 6（Go GC 压力与 CPU 开销）：Percona 基准测试观察到每约 2 分钟出现 CPU 尖峰，与 Go GC 高度相关，尖峰期间至少部分 CPU 核心完全饱和，甚至导致 `/metrics` 端点无响应。[Percona 性能分析](https://www.percona.com/blog/prometheus-2-times-series-storage-performance-analyses/ "Prometheus 2 Times Series Storage Performance Analyses")
- 发现 7（Gorilla XOR 压缩对短命序列效率骤降）：Gorilla 论文（VLDB 2015）报告每数据点从 16 字节压缩至平均 1.37 字节（约 12 倍压缩比），但前提是长命序列。Last9 指出短命序列（5 分钟寿命）仅 20 个样本仍需约 500 字节开销（约 2 倍压缩比），而长命序列（2 小时）480 个样本可压缩至约 1-2 KB（约 10 倍压缩比）。[Gorilla 论文](https://www.vldb.org/pvldb/vol8/p1816-teller.pdf "Gorilla: A Fast, Scalable, In-Memory Time Series Database") [Prometheus 官方存储文档](https://prometheus.io/docs/prometheus/2.55/storage/ "Storage - 'average of only 1-2 bytes per sample'") [Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics")
- 发现 8（Compaction 开销加剧）：Percona 基准测试观察到 compaction 导致巨大磁盘 I/O 和 CPU 尖峰，且 compaction 后大量内存从 Cached 转为 Free，有价值缓存数据被冲刷。Last9 总结高 churn 增加写放大——更多序列意味着更大 Postings 列表和更难压缩的数据。[Percona 性能分析](https://www.percona.com/blog/prometheus-2-times-series-storage-performance-analyses/ "Prometheus 2 TSDB Performance Analyses") [Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics")
- 发现 9（查询窗口越长代价越大）：Chronosphere 阐述核心影响机制——时间窗口内基数只增不减（过期序列仍在窗口内），查询回溯窗口越长需扫描唯一序列越多。即时基数可控的工作负载在长窗口查询时性能可能急剧恶化。[Chronosphere 博文](https://chronosphere.io/learn/how-cloud-native-workloads-affect-cardinality-over-time/ "How cloud native workloads affect cardinality over time")
- 发现 10（Staleness 对 PromQL 的影响）：Brian Brazil 解释 stale marker 注入后 range vector 选择器（`rate()`、`avg_over_time()`）完全忽略 stale marker 仅作用于非 stale 样本。高 churn 下 `rate()` 和 `increase()` 在旧序列和新序列之间产生计算断裂。[Robust Perception 博文](https://www.robustperception.io/staleness-and-promql "Staleness and PromQL")
- 发现 11（倒排索引选择性崩塌）：Last9 分析高 churn 下 Postings 列表稀疏化导致交集操作效率骤降，且 Prometheus 缺乏 value-based predicate pushdown，每条匹配序列须完全加载解压后再过滤。[Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics")
- 发现 12（Grafana Labs 确认查询性能影响）：Grafana Labs 指出随数据库增长查询访问序列数增加，"根本性地拖慢查询和可视化速度"，延长 MTTR。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics")
- 发现 13（Remote Write 1.0 协议每样本携带完整标签集）：Remote Write 1.0 规范要求"The complete set of labels MUST be sent with each sample"。短命序列元数据开销/样本比显著高于长命序列。[Prometheus Remote-Write 1.0 规范](https://prometheus.io/docs/specs/prw/remote_write_spec/ "Prometheus Remote-Write 1.0 specification")
- 发现 14（Remote Write 1.0 必须发送 stale markers）：规范要求发送方在序列失活时必须发送 stale markers。大规模 churn 事件（如滚动更新数百 Pod）期间 stale marker 数量可与正常样本相当，实质使 remote write 流量翻倍。[Prometheus Remote-Write 1.0 规范](https://prometheus.io/docs/specs/prw/remote_write_spec/ "Prometheus Remote-Write 1.0 specification")
- 发现 15（Remote Write 2.0 通过 string interning 缓解但未消除问题）：Remote Write 2.0（实验性）引入 symbols table 和 labels_refs 减少重复标签文本传输量，但短命序列频繁创建发送样本和 stale markers 的根本问题仍在。[Prometheus Remote-Write 2.0 规范](https://prometheus.io/docs/specs/prw/remote_write_spec_2_0/ "Prometheus Remote-Write 2.0 specification")
- 发现 16（WAL 膨胀导致重启盲区 30-90 分钟）：Michal Drozd 记录高 churn 集群 WAL 重放导致 Prometheus Pod 处于 Running 但 NotReady 状态长达 30-90 分钟，告警评估完全停止。重放过程内存消耗远超稳态水平，可能触发 OOMKill 死循环。[Michal Drozd 技术博客](https://www.michal-drozd.com/en/blog/prometheus-wal-replay-slow-startup/ "Prometheus WAL Replay Hell")
- 发现 17（Percona 实测：约 100 万 samples/sec 下 WAL 恢复耗时约 25 分钟）：Percona 基准测试中 SSD 存储上 WAL 恢复耗时约 25 分钟，恢复过程极度消耗内存。[Percona 性能分析](https://www.percona.com/blog/prometheus-2-times-series-storage-performance-analyses/ "Prometheus 2 TSDB Performance Analyses")
- 发现 18（Grafana Labs 确认基数增长直接推高成本）：Grafana Labs 明确指出基数增加意味着需要更多基础设施和计算资源，直接影响可观测平台支出。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics")
- 发现 19（Last9 估算：单个高 churn 标签可导致账单 10 倍暴涨）：Last9 指出在托管 Prometheus 中按活跃序列计费，一个高基数标签可一夜之间将账单提高 10 倍，举例 `request_id` 标签可能导致每月 50,000 美元额外成本。[Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics")
- 发现 20（长期存储后端的 churn 影响）：Last9 分析 Mimir/Cortex、Thanos、VictoriaMetrics 等后端在高 churn 下行为——底层仍使用相同 TSDB 模型，序列仍是成本单位，所有工具都在推高能力边界但没有消除基本权衡。[Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics")
- 发现 21（`for` 子句在 churn 下被重置导致系统性漏报）：当 Pod 被替换时旧告警向量元素消失、新告警需重新经历完整 `for` 等待期。如果 churn 频率高于 `for` 持续时间，告警可能永远无法从 pending 进入 firing 状态。[Prometheus 官方告警规则文档](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/ "Alerting rules - for clause")
- 发现 22（staleness 导致单次 scrape 失败即可中断告警）：Brian Brazil 指出 scrape 失败时前一次所有序列被标记为 stale，需格外小心确保一次 scrape 失败不会中断告警。[Robust Perception 博文](https://www.robustperception.io/staleness-and-promql "Staleness and PromQL")
- 发现 23（`keep_firing_for` 的出现佐证 churn 是公认痛点）：Prometheus 官方文档描述 `keep_firing_for` 子句用于"防止因数据丢失导致的虚假解决"，其存在本身佐证 staleness/churn 导致告警虚假解决是社区公认问题。[Prometheus 官方告警规则文档](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/ "Alerting rules - keep_firing_for clause")
- 发现 24（联邦场景 churn 传导呈乘法效应）：Chronosphere 指出云原生工作负载的高 churn 可轻易压垮老旧 TSDB。联邦架构中上游 churn 通过 federation 或 remote write 传导至下游聚合层，基数膨胀呈乘法效应。[Chronosphere 博文](https://chronosphere.io/learn/how-cloud-native-workloads-affect-cardinality-over-time/ "How cloud native workloads affect cardinality over time")
- 发现 25（分片和联邦不能消除 churn 只能分散）：Last9 指出分片使问题在每节点上变小但总量不变，跨分片聚合查询可能在协调器处超出内存限制，基于标签的一致性哈希分片可能导致热点。[Last9 技术分析](https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse/ "High Cardinality Metrics")

### 可用图片
（暂无）

### 仍需补充
- Head Block 倒排索引的精确内存分解：目前有两种估算（Ben Kochie ~8 KiB/series vs Last9 ~3-4 KB/series），差异可能源于统计口径不同，尚未找到权威解释
- Compaction 频率与 churn 的定量关系：缺乏"X 万 churn 序列导致 compaction 耗时增加 Y%"的定量 benchmark
- Remote Write 流量放大的精确量化：尚未找到"高 churn 环境下 remote write 带宽增加 X 倍"的实测数据
- Thanos/Mimir 在高 churn 下的具体成本对比数据：缺乏 T1/T2 级别量化成本对比
- 联邦场景下 churn 传导的实测案例：尚未找到带具体数字的生产案例

---

## Chapter 3：缓解与治理高流失率的系统性方案

### 研究目标
- 围绕"减少不必要的序列产生"和"降低已产生序列对系统的冲击"两条主线，系统梳理可落地的治理手段
- 覆盖 7 个子方向：(1) 指标设计与标签治理；(2) Relabeling 策略；(3) Prometheus 自身配置调优；(4) Recording Rules 与预聚合；(5) 架构层改进（联邦、分片、Agent 模式）；(6) 远程写与远程存储端的流控与准入策略；(7) 指标生命周期管理与过期序列清理机制

### 关键发现
- 发现 1（官方标签基数控制准则）：Prometheus 官方 Instrumentation 最佳实践文档给出明确准则——"try to keep the cardinality of your metrics below 10"，超过 100 应考虑替代方案。[Prometheus 官方 Instrumentation 文档](https://prometheus.io/docs/practices/instrumentation/ "Instrumentation - cardinality below 10")
- 发现 2（Brian Brazil 的基数乘法效应警告）：各标签维度基数相乘决定序列总数。例如 2 HTTP 方法 × 7 路径 × 5 机器 × 12 直方图桶 = 840 序列；各维度仅各增 1 就翻倍至 1728。任何单指标在 `/metrics` 端点上基数不应超过 10。[Robust Perception 博文](https://www.robustperception.io/cardinality-is-key "Cardinality is key")
- 发现 3（Grafana Labs 三步治理框架）：（1）获得可见性——识别高基数指标和标签；（2）归因——确定贡献最大的团队和环境；（3）优化——调整 scrape_interval、精简直方图桶、丢弃未使用标签。将非关键指标从 15s 提升至 60s "can reduce costs by up to 75%"。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics - 三步治理框架")
- 发现 4（标签治理实操规则）：禁止将无界值（user ID、request ID、session ID、container ID、Pod IP）作为标签；Istio/Envoy sidecar 指标应裁剪不需要的维度组合；直方图桶数量应根据 SLO 需求精简。[Prometheus 官方 Instrumentation 文档](https://prometheus.io/docs/practices/instrumentation/ "Instrumentation - Do not overuse labels") [Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics")
- 发现 5（relabel_configs vs metric_relabel_configs 处理时机）：Brian Brazil 明确区分——"relabel_configs happens before the scrape, metric_relabel_configs happens after the scrape"。在 churn 治理中 `metric_relabel_configs` 是丢弃高基数标签和冗余指标的主要手段。[Robust Perception 博文](https://www.robustperception.io/relabel_configs-vs-metric_relabel_configs "relabel_configs vs metric_relabel_configs")
- 发现 6（Relabeling 三阶段）：Grafana Labs 系统阐述三个阶段——（1）`relabel_configs` 在 scrape 前过滤 target；（2）`metric_relabel_configs` 在 scrape 后选择要摄入的序列；（3）`write_relabel_configs` 在数据发送到远程写端点前过滤，可"filter metrics with high cardinality or route metrics to specific remote_write targets"。[Grafana Labs 博文](https://grafana.com/blog/how-relabeling-in-prometheus-works/ "How relabeling in Prometheus works - 三阶段详解")
- 发现 7（metric_relabel_configs 在 sample_limit 之前执行）：Brian Brazil 指出 `metric_relabel_configs` 在 `sample_limit` 检查之前执行，可先通过 relabeling 丢弃不需要的序列，再由 `sample_limit` 作为最后安全阀。[Robust Perception 博文](https://www.robustperception.io/using-sample_limit-to-avoid-overload "Using sample_limit to avoid overload")
- 发现 8（sample_limit——每 scrape 样本数安全阀）：Prometheus 官方定义——超过阈值则整个 scrape 被视为失败（`up` 设为 0）。Brian Brazil 强调这是"emergency release valve for a sudden increase in cardinality"，不适合精细配额管理。[Prometheus 官方配置文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "Configuration - sample_limit") [Robust Perception 博文](https://www.robustperception.io/using-sample_limit-to-avoid-overload "Using sample_limit to avoid overload")
- 发现 9（target_limit——限制每 scrape_config 的 target 数量）：Prometheus 官方配置中的实验性功能，超过限制则 target 标记为失败不被抓取，防止服务发现返回意外大量 target。[Prometheus 官方配置文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "Configuration - target_limit，标注 experimental")
- 发现 10（label_limit 系列——标签维度限制）：三个配置项 `label_limit`、`label_name_length_limit`、`label_value_length_limit`，均在 metric-relabeling 之后检查，默认无限制，可防止应用端无意引入过多标签维度。[Prometheus 官方配置文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "Configuration - label_limit 系列参数")
- 发现 11（TSDB 存储参数——WAL 压缩）：`--storage.tsdb.wal-compression` 自 Prometheus 2.20.0 默认开启，可将 WAL 体积减半。官方文档指出减少序列数比增加 scrape_interval 更有效——"reducing the number of series is likely more effective, due to compression of samples within a series"。[Prometheus 官方存储文档](https://prometheus.io/docs/prometheus/latest/storage/ "Storage - WAL compression 和摄取速率优化建议")
- 发现 12（Go GC 调优——runtime.gogc）：Prometheus 配置中 `runtime.gogc` 默认值 75。高 churn 下降低 GOGC 值可更频繁回收内存、减少峰值，但增加 CPU 开销。[Prometheus 官方配置文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "Configuration - runtime.gogc 默认 75")
- 发现 13（Recording rules 核心价值）：通过预聚合将高基数指标（含 `pod`、`instance` 等高 churn 标签）压缩为低基数聚合结果（仅保留 `job`、`namespace` 等稳定标签），使仪表板和告警不再直接面对高基数原始数据。[Prometheus 官方 recording rules 文档](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/ "Defining recording rules")
- 发现 14（Recording rules 命名规范——level:metric:operations）：聚合时必须使用 `without` 子句显式指定要聚合掉的标签（而非 `by`），以保留 `job` 等有用标签。对比率类指标应分别聚合分子和分母再相除。[Prometheus 官方 recording rules 最佳实践](https://prometheus.io/docs/practices/rules/ "Recording rules - level:metric:operations 命名规范")
- 发现 15（Recording rules limit 参数）：rule_group 级别 `limit` 参数限制规则可产生的序列数量，超限则所有序列被丢弃并记录评估错误，是防止规则自身序列爆炸的安全机制。[Prometheus 官方 recording rules 文档](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/ "Defining recording rules - rule_group limit 参数")
- 发现 16（层级联邦——通过聚合减少 churn 传导）：官方联邦文档描述层级联邦——全局 Prometheus 从下级仅收集聚合时间序列。下级执行 recording rules 预聚合后仅将聚合结果暴露给上级，大幅减少 churn 上游传导。[Prometheus 官方联邦文档](https://prometheus.io/docs/prometheus/latest/federation/ "Federation - hierarchical federation")
- 发现 17（Brian Brazil 渐进式扩展路径）：单 Prometheus → 按用途拆分 → hashmod 分片 + leader 联邦。单 Prometheus 可处理约千台服务器。[Robust Perception 博文](https://www.robustperception.io/scaling-and-federating-prometheus "Scaling and Federating Prometheus")
- 发现 18（Agent 模式——官方定义）：禁用查询、告警和本地存储，替换为自定义 TSDB WAL。成功写入后立即删除数据，内存占用仅为正常模式的一小部分。本质无状态，易于水平扩展。[Prometheus 官方 Agent Mode 文档](https://prometheus.io/docs/prometheus/latest/prometheus_agent/ "Prometheus Agent Mode")
- 发现 19（Agent 模式局限）：无本地查询、无 recording rules、无告警。预聚合必须在远程存储端执行，增加中心端压力。[Prometheus 官方 Agent Mode 文档](https://prometheus.io/docs/prometheus/latest/prometheus_agent/ "Prometheus Agent Mode - limitations")
- 发现 20（Agent 模式生产验证）：由 Grafana Labs Robert Fratto 于 2019 年创建，经 Grafana Agent 大规模生产验证后于 Prometheus v2.32.0 集成。特别适用于边缘集群、受限网络、大量临时集群。[Prometheus 官方博文](https://prometheus.io/blog/2021/11/16/agent/ "Introducing Prometheus Agent Mode")
- 发现 21（Remote Write 队列调优）：`queue_config` 核心参数包括 `capacity`（建议 max_samples_per_send 的 3-10 倍）、`max_shards`、`min_shards`、`max_samples_per_send`（默认 2000）、`batch_send_deadline`。[Prometheus 官方 Remote Write 调优文档](https://prometheus.io/docs/practices/remote_write/ "Remote write tuning - queue_config 参数")
- 发现 22（Remote Write 与 churn 的内存放大——官方确认）：官方文档明确指出——"For each series in the WAL, the remote write code caches a mapping of series ID to label values, causing large amounts of series churn to significantly increase memory usage."[Prometheus 官方 Remote Write 调优文档](https://prometheus.io/docs/practices/remote_write/ "Remote write tuning - churn 导致 remote write 内存额外放大")
- 发现 23（write_relabel_configs——远程写端最后过滤层）：允许本地保留全量数据，仅将精简后数据发送远程存储，减少远程写流量和远端开销。[Grafana Labs 博文](https://grafana.com/blog/how-relabeling-in-prometheus-works/ "How relabeling in Prometheus works - write_relabel_configs")
- 发现 24（Grafana Mimir per-tenant 多层准入控制）：Distributor 组件提供请求速率限制、摄取速率限制、数据校验（max-label-names-per-series、max-length-label-name、max-length-label-value），超限返回 HTTP 429，支持 per-tenant 覆盖。[Grafana Mimir Distributor 文档](https://grafana.com/docs/mimir/latest/references/architecture/components/distributor/ "Grafana Mimir distributor - per-tenant rate limiting")
- 发现 25（Grafana Adaptive Metrics）：自动分析聚合未使用或部分使用的高基数指标。SailPoint 通过 Adaptive Metrics 指标量减少 33%，Grafana Labs 报告平均 35% 缩减。[Grafana Labs 博文](https://grafana.com/blog/how-to-aggregate-metrics-but-retain-critical-data-introducing-exemptions-in-adaptive-metrics/ "Adaptive Metrics - 35% reduction") [Grafana Labs SailPoint 案例](https://grafana.com/success/sailpoint/ "SailPoint - cut metric volume by 33%")
- 发现 26（Prometheus 原生序列生命周期——staleness 与 GC）：短命序列在 Head Block 中滞留至少一个完整 block 周期（2 小时），期间持续消耗内存。过期 block 清理在后台进行，可能需长达 2 小时。[Prometheus 官方存储文档](https://prometheus.io/docs/prometheus/latest/storage/ "Storage - block cleanup")
- 发现 27（双重保留策略加速清理）：时间保留 + 大小保留可同时配置，先触发的先生效。高 churn 场景应缩短保留时间配合远程存储。[Prometheus 官方存储文档](https://prometheus.io/docs/prometheus/latest/storage/ "Storage - retention.time 和 retention.size")
- 发现 28（mimirtool——发现和清理未使用指标）：Grafana Labs 开源工具，可分析指标使用情况，对比仪表板、告警和 recording rules 中实际引用的指标，生成未使用指标列表以供丢弃。[Grafana Labs 博文](https://grafana.com/blog/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/ "How to manage high cardinality metrics - mimirtool")
- 发现 29（OTLP 配置的 churn 警告）：Prometheus 官方配置中 OTLP 接收器的 `promote_all_resource_attributes` 选项明确警告——将所有资源属性提升为标签会导致每次属性变化产生新序列，直接加剧 churn。[Prometheus 官方配置文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "Configuration - OTLP churn 警告")

### 可用图片
（暂无）

### 仍需补充
- `--storage.tsdb.min-block-duration` 和 `--storage.tsdb.max-block-duration` 在纯 churn 治理语境中的量化效果缺乏一手数据
- VictoriaMetrics vmagent 的 `series_limit` per-target 配置——Prometheus 原生不具备此功能，社区是否有类似 feature proposal 待确认
- Grafana Adaptive Metrics 的具体算法和决策逻辑缺乏技术细节
- Cloudflare 大规模 Prometheus 运营中的 churn 治理策略和配置模板细节

---

## Chapter 4：云厂商与商业产品的托管方案对比

### 研究目标
- 横向对比主要云厂商（AWS AMP、GCP Managed Prometheus、Azure Monitor Managed Prometheus、阿里云 Prometheus 版、腾讯云 Prometheus 监控服务）及 Grafana Cloud 在高 churn 场景下的产品化能力
- 对比维度：基数/系列限额与配额机制、自动基数检测与告警、标签治理工具与用量分析面板、计费模型对 churn 的敏感度、SLA 与性能保障
- 区分 GA 功能与 Preview/Beta 功能

### 关键发现
- 发现 1（AWS AMP 活跃序列限额）：截至 2025 年 7 月默认活跃序列限额提升至 5000 万/workspace，最大可申请至 10 亿/workspace；活跃判定窗口 2 小时。[AWS AMP Quotas](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html "AWS 官方配额文档") [AWS AMP 50M 公告](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-managed-service-prometheus-50M-default-activeserieslimit/ "2025 年 7 月默认限额提升至 50M")
- 发现 2（AWS AMP 按样本阶梯计费）：前 20 亿样本 $0.90/千万样本，之后 2500 亿样本 $0.35/千万样本；存储 $0.03/GB/月；查询 $0.10/十亿样本。Free Tier 含每月 4000 万样本摄取。[AWS AMP Pricing](https://aws.amazon.com/prometheus/pricing/ "AWS 官方定价页面")
- 发现 3（AWS AMP 按样本计费对高 churn 有利）：短命序列只在存活期间产生样本费用，不因新序列注册产生额外基数费用。[GCP Managed Prometheus](https://cloud.google.com/managed-prometheus "GCP 官方说明 per-sample 不罚 HPA")
- 发现 4（AWS AMP label-based series limits，2025 年 4 月 GA）：允许用户按标签组合为 workspace 子集设置独立活跃序列上限，防止单一租户/服务 cardinality 爆炸影响全局。[AWS AMP Label-Based Limits](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-managed-service-prometheus-label-based-series-limits/ "2025 年 4 月发布")
- 发现 5（AWS AMP 配额可视化，2025 年 9 月 GA）：通过 Service Quotas + CloudWatch 监控活跃序列使用量并设置告警。摄取限流基于 token bucket，默认速率为活跃序列限额的 1/30。[AWS AMP Quota Visibility](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-managed-service-prometheus-quota-visibility-aws-service-quotas-cloudwatch/ "2025 年 9 月发布")
- 发现 6（AWS AMP 无内置 cardinality explorer）：用户需依赖 CloudWatch DiscardedSamples 指标或 PromQL 手动检查基数。[AWS AMP Optimizing Ingestion](https://aws.amazon.com/blogs/mt/optimizing-metrics-ingestion-with-amazon-managed-service-for-prometheus/ "AWS 官方博文")
- 发现 7（GCP GMP 活跃序列限制）：per monitored resource 粒度——Prometheus 指标每资源 100 万条，活跃窗口 24 小时，系统级安全限制不可自定义。另有 25,000 metric descriptor/project 限制。[GCP Cloud Monitoring Quotas](https://docs.cloud.google.com/monitoring/quotas "GCP 官方配额文档")
- 发现 8（GCP GMP 按样本阶梯计费 + 存储含在内）：前 500 亿样本 $0.060/百万样本至 5000 亿以上 $0.024/百万样本。所有数据保留 24 个月无额外存储费（含自动降采样）。[GCP Managed Prometheus](https://cloud.google.com/managed-prometheus "GCP 官方产品页面定价表")
- 发现 9（GCP Metrics Management 页面）：Cloud Monitoring 控制台中可显示各指标摄取量、标签和基数信息、读取次数、在告警/仪表板中的使用情况，可直接排除不需要的指标。[GCP Cloud Monitoring Quotas](https://docs.cloud.google.com/monitoring/quotas "Metrics Management 页面功能")
- 发现 10（GCP GMP Monarch 后端）：使用 Google 内部 Monarch 时间序列数据库，可处理超 2 万亿活跃时间序列规模。[GCP Managed Prometheus](https://cloud.google.com/managed-prometheus "Key features 描述")
- 发现 11（Azure 默认 100 万活跃序列/workspace）：活跃窗口约 12 小时，默认摄取速率 100 万事件/分钟，均可申请增加。保留期 18 个月不可更改。[Azure Monitor Service Limits](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/service-limits "Azure 官方服务限制文档")
- 发现 12（Azure 按样本计费，部分来源标注 Preview 定价）：摄取约 $0.16/千万样本，查询 $0.10/十亿样本。[Azure Monitor Pricing 转引](https://adatum.no/azure/azure-monitor/azure-monitor-managed-prometheus "第三方引用 Azure 定价") [Azure Monitor Cost](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/cost-usage "Azure 官方成本管理文档")
- 发现 13（Azure 大小写不敏感）：与原生 Prometheus 不同，仅标签值大小写不同的两条序列被视为同一序列，可能导致数据丢弃。[Azure Monitor Prometheus Details](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-details "Azure 官方技术细节文档")
- 发现 14（Azure 标签限制和查询限制）：标签名≤511 字符、标签值≤1023 字符、每序列最多 63 标签。超限时整个 scrape job 所有指标被丢弃。查询时间范围最长 32 天。[Azure Monitor Prometheus Details](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-details "标签限制") [Azure Monitor Service Limits](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/service-limits "查询限制")
- 发现 15（Azure 无专用 cardinality explorer）：需通过 ActiveTimeSeries / Events ingested per minute 指标配合告警发现配额问题。超 2000 万 ActiveTimeSeries 需特殊审批。[Azure Monitor Workspace Ingest Limits](https://github.com/MicrosoftDocs/azure-monitor-docs/blob/main/articles/azure-monitor/metrics/azure-monitor-workspace-monitor-ingest-limits.md "Azure 文档 GitHub 仓库")
- 发现 16（Grafana Cloud 计费模型——按活跃序列 + DPM）：免费层 10,000 活跃序列（活跃窗口 20 分钟），Pro 层超出部分 $6.50/千序列/月。账单取活跃序列与总 DPM 的较大值，按 P95 计算。高 churn 下此模型可能不利——短命序列在活跃窗口内仍计为活跃。[Grafana Cloud Pricing](https://grafana.com/pricing/ "Grafana Labs 官方定价") [Grafana Cloud Metrics Usage](https://grafana.com/docs/grafana-cloud/cost-management-and-billing/understand-usage-cost/metrics/ "计量和计费文档")
- 发现 17（Grafana Adaptive Metrics GA）：自动推荐将低利用率指标聚合为低基数版本，支持交互式/API/Terraform 应用，官方宣传可优化成本高达 80%。[Grafana Adaptive Metrics](https://grafana.com/docs/grafana-cloud/adaptive-telemetry/adaptive-metrics/ "官方 Adaptive Metrics 文档")
- 发现 18（Grafana Cloud Cardinality Management Dashboard）：专用面板分析指标基数、识别高基数指标和标签，支持按标签维度成本归因。[Grafana Cloud Metrics Usage](https://grafana.com/docs/grafana-cloud/cost-management-and-billing/understand-usage-cost/metrics/ "Usage 监控功能")
- 发现 19（阿里云 Prometheus 版按量/节省计划计费）：自定义指标按写入量或数据点数计费，基础指标（容器服务、自身监控）免费。未公开全局活跃时间线上限。Agent 单副本一次最多采集 350 万数据点、最大 5000 Target。[阿里云 Prometheus 计费概述](https://help.aliyun.com/zh/prometheus/product-overview/billing-overview "阿里云官方计费概述") [阿里云 Prometheus 服务限制](https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/service-limits "阿里云官方服务限制")
- 发现 20（腾讯云 TMP 按数据点阶梯计费）：按量计费以百万条为单位阶梯式递减，套餐包提供体验版（599 元/月）至豪华版（409,999 元/年）。未公开明确的活跃时间序列上限，以上报数据量为限制维度。存储时长 15 天至 2 年可选。[腾讯云 TMP 计费概述](https://cloud.tencent.com/document/product/1416/113555 "腾讯云官方计费概述") [腾讯云 TMP 套餐包](https://cloud.tencent.com/document/product/1416/113560 "腾讯云官方套餐包")
- 发现 21（横向：按样本计费对高 churn 更有利）：AWS AMP、GCP GMP、Azure、阿里云、腾讯云均按样本/数据点计费，短命序列仅产生实际样本费用；Grafana Cloud 按活跃序列计费，20 分钟活跃窗口可能导致短命序列推高 P95 峰值和账单。[Grafana Cloud Metrics Usage](https://grafana.com/docs/grafana-cloud/cost-management-and-billing/understand-usage-cost/metrics/ "活跃窗口 20 分钟")
- 发现 22（横向：活跃序列限额对比）：AWS AMP 默认 5000 万（最高 10 亿）> GCP per-resource 100 万（Monarch 全局 2 万亿+）> Azure 默认 100 万（可申请）> Grafana Cloud 免费 1 万/付费按量 > 阿里云和腾讯云未公开全局限额。[AWS AMP Quotas](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html "AWS 配额") [Azure Monitor Service Limits](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/service-limits "Azure 配额") [GCP Cloud Monitoring Quotas](https://docs.cloud.google.com/monitoring/quotas "GCP 配额")
- 发现 23（横向：Cardinality 工具对比）：Grafana Cloud 最成熟（Adaptive Metrics GA + Cardinality Dashboard + 成本归因）> GCP（Metrics Management 页面）> AWS（label-based limits + CloudWatch 告警）> Azure（通用摄取指标监控）> 阿里云/腾讯云（未发现专用工具）。
- 发现 24（横向：保留期对比）：GCP 24 个月（含降采样无额外费用）> Azure 18 个月 > Grafana Cloud Pro 13 个月 > 腾讯云 15 天–2 年可选 > 阿里云依赖 SLS。AWS AMP 官方未标明最大保留期。

### 可用图片
（暂无）

### 仍需补充
- Azure Monitor Managed Prometheus 的确切官方 GA 计费单价（当前部分来源为 Preview 定价或第三方转引）
- 阿里云 Prometheus 版按量计费具体阶梯单价需从子页面确认
- 腾讯云 TMP 按量计费具体阶梯单价需确认
- 各厂商 SLA 可用性承诺（99.9% / 99.95% 等）需逐一确认
- AWS AMP 最大数据保留期官方文档未明确标注

---

## Chapter 5：开源生态替代方案与工程实践

### 研究目标
- 梳理开源长期存储后端（Grafana Mimir、Thanos、VictoriaMetrics、Cortex）在高 churn 场景下的架构优势与局限
- 对比 Ingester 内存管理、索引分片、压缩策略、查询性能等维度的表现差异
- 收集社区真实工程案例和最佳实践（如大型 Kubernetes 集群的 churn 治理经验）

### 关键发现
- 发现 1（Mimir Ingester 内存管理）：Ingester 将序列存储在内存和磁盘中，默认每 2 小时压缩为 TSDB block 上传至对象存储。高 churn 下大量短命序列在 Ingester 内存中驻留至下一次 block 写入（1-3 小时）。[Mimir Ingester 文档](https://grafana.com/docs/mimir/latest/references/architecture/components/ingester/ "Mimir v3.0 Ingester 组件文档")
- 发现 2（Mimir Ingest Storage/Kafka 架构）：v3.0 引入 Kafka 写入路径——Distributor 写 Kafka partition，Ingester 仅作读路径消费。写入成功仅依赖 Kafka 而非 Ingester 状态，高 churn 下显著提升写入可靠性。[Mimir Ingester 文档](https://grafana.com/docs/mimir/latest/references/architecture/components/ingester/ "Ingest Storage Architecture")
- 发现 3（Mimir split-and-merge compactor）：先将源块拆分为 M 个分片块，再按分片合并，克服 TSDB 索引大小限制。建议每 800 万活跃序列 1 个分片，1 亿活跃序列约需 12 个分片。[Mimir Compactor 文档](https://grafana.com/docs/mimir/latest/references/architecture/components/compactor/ "split-and-merge 压缩策略")
- 发现 4（Mimir OOO samples ingestion）：支持 `out_of_order_time_window` 配置，允许乱序样本摄入。K8s 高 churn 环境中 Pod 重建可能导致 remote write 乱序，该机制避免样本丢弃。[Mimir OOO 文档](https://grafana.com/docs/mimir/latest/configure/configure-out-of-order-samples-ingestion/ "out-of-order samples 配置指南")
- 发现 5（Mimir Shuffle Sharding 多租户隔离）：将每租户序列分配到集群子集。50 partition 中每租户分配 4 个时，两随机租户 71% 概率不共享任何 partition，cardinality 爆炸时影响限制在少数节点。[Mimir Shuffle Sharding 文档](https://grafana.com/docs/mimir/latest/configure/configure-shuffle-sharding/ "Shuffle Sharding 配置")
- 发现 6（Mimir Custom Active Series Trackers）：支持按标签条件分组统计活跃序列，结合 `max_global_series_per_user` 和 `max_global_series_per_metric` per-tenant 限制，在 churn 爆发时提前触发限流。[Mimir Compactor 文档](https://grafana.com/docs/mimir/latest/references/architecture/components/compactor/ "Active Series Trackers")
- 发现 7（Thanos Sidecar vs Receiver 模式）：Sidecar 将 TSDB block 上传对象存储，要求禁用本地 compaction；Receiver 实现 Remote Write API 支持多租户。Receiver 的 Ketama 一致性哈希在节点增减时不导致序列 churn 和内存峰值。[Thanos Receiver 文档](https://thanos.io/tip/components/receive.md/ "Receiver 组件文档")
- 发现 8（Thanos Active Series Limiting 实验性）：Receiver 通过查询元监控端点检查租户活跃序列数，超限时拒绝整个 remote write 请求。为 best-effort 限制——元监控不可用时不施加限制。[Thanos Receiver 文档](https://thanos.io/tip/components/receive.md/ "Active Series Limiting experimental")
- 发现 9（Thanos 三级降采样）：超 40 小时降采样至 5 分钟分辨率，超 10 天降采样至 1 小时分辨率。降采样不节省存储空间（存储总量可能增长约 3 倍），核心价值是加速大时间范围查询。短命序列数据点少，降采样效果有限。[Thanos Compact 文档](https://thanos.io/tip/components/compact.md/ "Downsampling")
- 发现 10（Thanos Compactor 单例限制）：同一块流只能由一个 Compactor 实例处理。可通过 label sharding 分配到不同实例实现水平扩展。支持按分辨率分别配置保留期。[Thanos Compact 文档](https://thanos.io/tip/components/compact.md/ "Scalability 和 Retention")
- 发现 11（Thanos Shuffle Sharding + AZ 感知）：Receiver 支持 Ketama 算法 shuffle sharding，每租户分配 hashring 子集节点，支持 AZ 感知。可通过 Receive Controller 自动化 hashring 管理配合 HPA 扩缩容。[Thanos Receiver 文档](https://thanos.io/tip/components/receive.md/ "Shuffle sharding")
- 发现 12（VictoriaMetrics 独立存储引擎）：从零用 Go 编写，不复用 Prometheus TSDB 源码，借鉴 ClickHouse 设计。indexdb 和 data 两级存储结构。高 churn 下 indexdb 大小可超过数据本身 10 倍（如 Zomato 案例），清理仅在 retention cycle 结束时发生。[VictoriaMetrics FAQ](https://docs.victoriametrics.com/victoriametrics/faq/ "Why IndexDB size is so large")
- 发现 13（vmagent 双层基数限制）：per-target `series_limit` 限制单目标唯一序列数（超限 24 小时窗口内丢弃）；全局 `-remoteWrite.maxHourlySeries` 和 `-remoteWrite.maxDailySeries` 控制活跃序列上限和日度 churn 率。[vmagent 文档](https://docs.victoriametrics.com/vmagent/ "Cardinality limiter")
- 发现 14（vmagent Stream Aggregation）：在数据到达远程存储前按时间和标签预聚合，可丢弃高基数标签将聚合后低基数序列写入后端，显著减少 indexdb 膨胀和查询压力。[vmagent 文档](https://docs.victoriametrics.com/vmagent/ "Stream Aggregation")
- 发现 15（VictoriaMetrics 扩展性）：单节点版可处理最高 1 亿活跃序列和每秒 200 万样本摄入率，集群版可处理数十亿活跃序列。原生支持 backfilling 和 out-of-order 样本无需额外配置。[VictoriaMetrics FAQ](https://docs.victoriametrics.com/victoriametrics/faq/ "What is the scalability limits")
- 发现 16（VictoriaMetrics 劣势——indexdb 和降采样）：典型 K8s 监控场景 indexdb 可达数据目录 2 倍以上。开源版不支持降采样（仅企业版），长保留期场景磁盘成本可能高于 Thanos。[VictoriaMetrics FAQ](https://docs.victoriametrics.com/victoriametrics/faq/ "Why IndexDB size is so large")
- 发现 17（Cortex → Mimir fork 关系）：Mimir 于 2022 年 3 月发布，fork 自 Cortex（2019-2021 间约 87% commits 来自 Grafana Labs）。开源了 split-and-merge compactor（无限基数水平扩展）和 sharded query engine（高基数查询加速最高 40 倍）。AGPLv3 许可证。[Grafana Mimir 发布公告](https://grafana.com/blog/2022/03/30/announcing-grafana-mimir/ "2022 年 3 月 30 日发布")
- 发现 18（Cortex 活跃度已下降）：Cortex 仍在 CNCF 孵化，但活跃开发大幅减少，缺少 split-and-merge compactor 等关键优化，Grafana Labs 建议迁移至 Mimir。[Mimir 迁移文档](https://grafana.com/docs/mimir/latest/set-up/migrate/migrate-from-cortex/ "Cortex 到 Mimir 迁移指南")
- 发现 19（Cloudflare 案例：916 实例 49 亿序列）：维护自定义补丁——TSDB 全局序列上限（达上限时拒绝新序列）和 sample_limit 软降级（超限时继续为已存在序列追加样本）。默认 sample_limit 设为 200/target。配合 CI 校验确保容量。[Cloudflare 工程博客](https://blog.cloudflare.com/how-cloudflare-runs-prometheus-at-scale/ "How Cloudflare runs Prometheus at scale, 2023")
- 发现 20（Cloudflare 短命序列成本分析）：一个仅被采集一次的序列保证在内存中驻留 1-3 小时。Cloudflare 因此将默认 sample_limit 设为 200/target，超过需显式配置。[Cloudflare 工程博客](https://blog.cloudflare.com/how-cloudflare-runs-prometheus-at-scale/ "短命序列成本分析")
- 发现 21（Zomato：Prometheus+Thanos → VictoriaMetrics）：迁移前 144 台 Prometheus（双 AZ）配合 Thanos，面临 OOM、WAL 损坏、查询延迟高。2024 年峰值 22 亿活跃序列、1750 万样本/秒。迁移后查询响应降低约 1/3、活跃序列减少 40%，但 indexdb 大小为数据 10 倍需预留双倍磁盘。开源版不支持降采样。[Zomato 工程博客](https://www.zomato.com/blog/migrating-to-victoriametrics-a-complete-overhaul-for-enhanced-observability "Migrating to VictoriaMetrics, 2024")
- 发现 22（Cloudflare 使用 Thanos 统一查询层）：将数千小型 Prometheus 部署整合为统一查询层，在 KubeCon 2024 分享动态环境中扩展 Thanos 的经验。[Cloudflare 博客](https://blog.cloudflare.com/safe-change-at-any-scale/ "Thanos scaling in dynamic Prometheus environments")
- 发现 23（横向架构差异）：Mimir——微服务化 + Kafka ingest + split-and-merge compactor + 原生多租户 shuffle sharding；Thanos——Sidecar/Receiver 双模式 + 对象存储为中心 + 三级降采样；VictoriaMetrics——独立存储引擎 + 单节点可扩至 1 亿序列 + vmagent 前置基数限制 + 无外部依赖；Cortex——Mimir 前身，缺少后续优化。
- 发现 24（横向 churn 应对能力）：Mimir 通过架构分散大租户负载 + OOO ingestion；Thanos 降采样缓解长窗口查询但 Compactor 单例是瓶颈；VictoriaMetrics 在摄入前端控制 churn（series_limit + maxDailySeries + stream aggregation）但 indexdb 膨胀是长期挑战；Cortex 已不建议新部署。
- 发现 25（横向运维复杂度）：VictoriaMetrics 单节点最简（单二进制无外部依赖）> Thanos 居中（Compactor 单例 + 对象存储依赖）> Mimir 最高（尤其 Kafka 架构）但水平扩展性和多租户隔离最强。

### 可用图片
（暂无）

### 仍需补充
- Mimir per-tenant 活跃序列限制（`max_global_series_per_user` 等）的精确默认值和推荐值
- Thanos Store Gateway 在高 churn 场景下查询短命序列的量化性能数据
- VictoriaMetrics indexdb rotation period 配置和最新版本优化进展
- 更多社区案例（Uber M3/Prometheus 实践、GitLab Thanos 演进细节）——搜索未找到足够详细的一手公开文章
- 各方案在 Native Histograms 支持方面的差异对比

---

# Section 2：给 Write 阶段的执行建议

- 全文统一使用"流失率"对应 churn rate，"高基数"对应 high cardinality，首次出现时附注英文原词，后续正文直接使用中文术语；其余 Prometheus 专有术语（如 Head Block、WAL、Compaction、Remote Write）保留英文原词，首次出现时给出简短中文释义。
- Chapter 1 作为概念基础章，篇幅应控制在全文 15% 以内，重在定义清晰而非面面俱到。
- Chapter 2 和 Chapter 3 是全文核心，合计应占 50% 左右篇幅；Chapter 2 侧重"问题有多严重"，Chapter 3 侧重"如何解决"，两章之间应有清晰的因果呼应（Chapter 3 的每个方案应能对应到 Chapter 2 中提出的某个具体影响）。
- Chapter 4 和 Chapter 5 采用统一的对比维度进行横向分析，避免逐厂商/逐项目罗列式写法；建议使用对比表格辅以文字分析。
- 涉及云厂商产品时，需注意区分"已 GA 的功能"与"Preview/Beta 功能"，标注清楚功能成熟度。
- 全文时间口径以 2025-04 至 2026-10 为窗口，引用数据和版本信息需标注时间点。
- 数值引用须遵循"主体 + 时间 + 单位 + 数值 + 来源"五要素规范，避免模糊表述。
- 对比分析部分避免直接给出"推荐方案"或主观排名，而应基于维度对比让读者根据自身场景做判断。
- Chapter 2 与 Chapter 3 之间应建立因果映射表：Chapter 3 的每个治理手段需明确标注对应 Chapter 2 中的哪些影响维度。
- Chapter 4（云厂商）与 Chapter 5（开源方案）可在结尾各用一张对比表格汇总关键维度差异，表格后附简要文字分析。
- 注意 Azure Managed Prometheus 的计费单价部分来源为 Preview 定价或第三方转引，成稿前需再次核验是否已有 GA 定价。
- 阿里云和腾讯云的按量计费具体阶梯单价在 researcher 补研阶段未完全获取，成稿时可选择仅引用计费模式而不列具体单价，或注明"单价以官方最新文档为准"。
- VictoriaMetrics 的 indexdb 膨胀问题是其在高 churn 场景下的显著劣势，成稿时应与 Mimir 的 split-and-merge compactor 和 Thanos 的降采样形成对比。
- Cloudflare 自定义 Prometheus 补丁（TSDB 全局序列上限 + sample_limit 软降级）是社区中独特的治理实践，值得在 Chapter 5 中详细展开。
