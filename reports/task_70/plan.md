# Section 1：章节研究计划

## Chapter 1：The Servlet Foundation — Java's Answer to Dynamic Web Content
### 研究目标
- Explain why the Servlet specification was created, how it works at a mechanical level (lifecycle, threading model, request/response abstraction), and what pain points it solved compared to CGI — while also identifying the limitations and boilerplate burdens that motivated everything that came after.
- Key subsections: CGI → Servlets (1997), Servlet Architecture & Lifecycle, Request/Response Model, Pain Points Left Unsolved.

### 关键发现
- CGI (Common Gateway Interface) 自 1993 年开始用于 Web 动态内容生成，采用 process-per-request 模型，其规范最终以 [RFC 3875](https://datatracker.ietf.org/doc/html/rfc3875 "The Common Gateway Interface (CGI) Version 1.1, October 2004") 形式发布。CGI 的根本局限包括：每请求 fork 进程的高开销、无内建会话管理、平台依赖（脚本通常绑定 Perl/C/Shell）、以及安全隐患（子进程与服务器共享用户/组权限）。
- James Gosling 于 1995 年最初提出 Servlet 概念，Pavani Diwanji 于 1996 年初将其实现于 Sun Microsystems 内部代号为"Jeeves"的纯 Java HTTP 服务器中。Servlet API 于 1996 年 5 月首届 JavaOne 大会首次公开演示，1997 年 6 月随 JSDK 1.0 正式发布 Servlet 1.0 规范。该技术记录于 [US Patent 5,928,323](https://patents.google.com/patent/US5928323 "Gosling, Diwanji, Connelly — Sun Microsystems, 1999")，明确描述了 servlet 相较 CGI"无进程创建开销"的架构优势。[Eclipse Foundation Newsletter](https://www.eclipse.org/community/eclipse_newsletter/2020/february/3.php "Jakarta EE: Servlets and Tomcat — 23 Years and Counting")
- Servlet 规范版本演进与关键 JSR：Servlet 2.2 (1999, JSR-902/903) 引入 `.war` 打包并纳入 J2EE 1.2；Servlet 2.3 (2001, [JSR-53](https://jcp.org/en/jsr/detail?id=53 "Java Servlet 2.3 and JSP 1.2")) 新增 Filter 和 Listener 组件模型；Servlet 2.4 (2003, [JSR-154](https://jcp.org/en/jsr/detail?id=154 "Java Servlet 2.4 Specification")) 改用 XML Schema 部署描述符；Servlet 3.0 (2009, [JSR-315](https://jcp.org/en/jsr/detail?id=315 "Java Servlet 3.0 Specification")) 引入注解（`@WebServlet`）和异步处理，部署描述符变为可选；Servlet 3.1 (2013, [JSR-340](https://jcp.org/en/jsr/detail?id=340 "Java Servlet 3.1 Specification")) 增加非阻塞 I/O 与 WebSocket 升级；Servlet 4.0 (2017, [JSR-369](https://jcp.org/en/jsr/detail?id=369 "Java Servlet 4.0 Specification")) 支持 HTTP/2 Server Push，是迁移至 Jakarta EE 前的最后一个 Java EE 版本。
- Apache Tomcat 起源于 Sun Microsystems 的 Servlet 参考实现。James Duncan Davidson 开发了 JWSDK，1999 年说服 Sun 将代码捐赠给 Apache 基金会，形成 Tomcat 项目，2005 年成为 Apache 顶级项目。Tomcat 版本与 Servlet 规范的对应关系由 [Apache Tomcat 官方](https://tomcat.apache.org/whichversion.html "Official Tomcat version-to-specification mapping") 权威记录：Tomcat 7.x→Servlet 3.0，8.x→3.1，9.x→4.0，10.1.x→6.0 (Jakarta EE 10)，11.x→6.1 (Jakarta EE 11)。
- Servlet 容器通过 `init()`→`service()`（按 HTTP 方法分派至 `doGet()`/`doPost()` 等）→`destroy()` 三阶段管理 Servlet 生命周期。所有 Servlet 在单一 JVM 进程内运行，容器维护线程池、对每个请求分配线程调用 `service()` 方法，从根本上消除了 CGI 的进程创建开销。应用范围共享状态通过 `ServletContext` 实现，用户会话通过 `HttpSession` 跟踪。
- 核心 API 抽象：`HttpServletRequest`（封装客户端请求数据）、`HttpServletResponse`（构造 HTTP 响应）、`HttpSession`（服务端会话跟踪）、`Filter`（Servlet 2.3 新增，请求/响应拦截链）、`Listener`（Servlet 2.3 新增，生命周期事件回调）。
- Servlet 遗留的核心痛点：(a) 冗长样板代码——每个处理器需继承 `HttpServlet`、覆写方法、手动解析参数；(b) 业务逻辑与 HTTP 协议处理耦合——`service()` 方法混杂应用逻辑与协议处理，难以测试维护；(c) 无声明式服务——事务、安全等横切关注点需手动编码；(d) 手动资源管理——数据库连接、线程管理均由开发者负责；(e) 测试困难——Servlet 代码紧耦合容器，测试需运行完整 Servlet 容器。这些局限直接驱动了 J2EE/EJB（声明式企业服务）和后来 Spring Framework（轻量级 POJO 开发）的诞生。

### 可用图片
- 无本地可用图片。建议创建：(1) CGI vs. Servlet 执行模型对比图（process-per-request vs. thread-per-request），(2) Servlet 生命周期流程图（`init()`→`service()`→`destroy()`），(3) Servlet 规范版本时间线（1996–2017，标注关键特性与 JSR 编号）。

### 仍需补充
- Jetty 容器的首次发布时间（约 1995–1996 年）及版本历史，若需与 Tomcat 并列讨论。
- FastCGI 作为 CGI 到 Servlet 之间的中间方案，若需在 CGI 局限性部分做对比。
- CGI vs. Servlet 的定量性能基准数据（未找到 T1/T2 来源）。

---

## Chapter 2：The J2EE / EJB Era — Enterprise Ambition Meets Accidental Complexity
### 研究目标
- Describe the enterprise problems that J2EE and Enterprise JavaBeans aimed to solve (distributed transactions, remoting, lifecycle management, security) and analyze why the specification became synonymous with heavyweight complexity, XML sprawl, and vendor lock-in — setting the stage for the Spring rebellion.
- Key subsections: The Enterprise Vision, EJB in Practice, The Backlash and Search for Alternatives.

### 关键发现
- J2EE 平台版本演进：J2EE 1.2 (1999-12-17) 为初始版本，捆绑 Servlet 2.2、EJB 1.1 等企业 API；J2EE 1.3 (2001-09-24, [JSR 58](https://jcp.org/en/jsr/platform?listBy=3&listByType=platform "J2EE 1.3 platform JSR")) 新增 JCA 与 EJB 2.0；J2EE 1.4 (2003-11-11, [JSR 151](https://jcp.org/en/jsr/platform?listBy=3&listByType=platform "J2EE 1.4 platform JSR")) 主推 Web Services (JAX-RPC)；Java EE 5 (2006-05-11, [JSR 244](https://jcp.org/en/jsr/platform?listBy=3&listByType=platform "Java EE 5 platform JSR")) 以注解和泛型为核心主题，将"J2EE"更名为"Java EE"。[Jakarta EE — Wikipedia](https://en.wikipedia.org/wiki/Jakarta_EE "J2EE version history table")
- EJB 规范版本：EJB 1.0 (1998-03-24) 于 JavaOne 发布；EJB 1.1 (1999-12-17) 引入 XML 部署描述符和角色驱动安全；EJB 2.0 ([JSR 19](https://www.jcp.org/en/jsr/detail?id=19 "EJB 2.0 Specification"), 2001-08-22) 新增 Local 接口、Message-Driven Bean 和 EJB-QL；EJB 2.1 ([JSR 153](https://www.jcp.org/en/jsr/detail?id=153 "EJB 2.1 Specification"), 2003-11-24) 新增 Web Service 端点和定时器服务；EJB 3.0 ([JSR 220](https://www.jcp.org/en/jsr/detail?id=220 "EJB 3.0 Specification"), 2006-05-11) 以"降低开发者复杂度"为明确目标，废除 Home 接口和 XML 描述符，引入注解驱动、POJO 实体与 JPA。[Jakarta Enterprise Beans — Wikipedia](https://en.wikipedia.org/wiki/Jakarta_Enterprise_Beans "EJB version history")
- EJB 定义三类组件：Session Bean（Stateless/Stateful）、Entity Bean（CMP/BMP）、Message-Driven Bean (EJB 2.0+)。EJB 2.1 及更早版本中，每个 EJB 需开发者提供三个独立 Java 构件（Home 接口、Remote/Local 接口、Bean 实现类）外加 ejb-jar.xml 部署描述符，"triple-class + XML"模式被广泛认为对简单业务逻辑过于繁重。此外还需供应商特定描述符（如 weblogic-ejb-jar.xml、jboss.xml）。
- EJB 测试极其困难：组件无法在应用服务器容器外运行，简单业务逻辑测试也需完整应用服务器启动。Martin Fowler 明确指出"component environments that are very intrusive, such as Java's EJB framework"加剧了测试问题，拖慢了"edit-execute cycle"。[Martin Fowler](https://martinfowler.com/articles/injection.html "Inversion of Control Containers and the Dependency Injection pattern, January 2004")
- CMP Entity Bean 的 SQL 生成被广泛批评为低效且不可移植；Oracle 官方文档亦承认"EJB persistence has long been criticized for its complex development model and for poor performance"。[Oracle](https://www.oracle.com/technical-resources/articles/enterprise-architecture/tuning-cmp-ejbs1.html "Peak performance tuning of CMP 2.0 Entity beans")
- Rod Johnson 于 2002 年 10 月由 Wrox Press 出版 *Expert One-on-One J2EE Design and Development*（ISBN 978-0-7645-4385-2），[ACM Digital Library](https://dl.acm.org/doi/10.5555/996540 "Wrox Press, October 2002") 主张许多 J2EE 应用过度设计，提倡 POJO 模式可实现更好效果。该书附带代码成为 Spring Framework 种子。Spring 0.9 于 2003 年 6 月以 Apache 2.0 许可开源发布，1.0 于 2004 年 3 月发布。[Spring Framework — Wikipedia](https://en.wikipedia.org/wiki/Spring_Framework "Spring origin narrative")
- 轻量级容器运动：Martin Fowler 2004 年 1 月发表影响深远的文章 [Inversion of Control Containers and the Dependency Injection pattern](https://martinfowler.com/articles/injection.html "January 2004")，描述了企业 Java 世界中"a rush of lightweight containers"作为对"heavyweight complexity in the mainstream J2EE world"的反应，并创造了"Dependency Injection"术语。Hibernate ORM 由 Gavin King 于 2001-05-23 首次发布，"as an alternative to using EJB2-style entity beans"。[Hibernate — Wikipedia](https://en.wikipedia.org/wiki/Hibernate_(framework) "Initial release 23 May 2001") Apache Struts 1.0 于 2001 年 6 月发布。[Apache Struts 1 — Wikipedia](https://en.wikipedia.org/wiki/Apache_Struts_1 "Initial release June 2001") PicoContainer 于 2003 年出现。
- EJB 3.0 ([JSR 220](https://www.jcp.org/en/jsr/detail?id=220 "EJB 3.0 purpose statement")) 明确以"improve the EJB architecture by reducing its complexity from the developer's point of view"为目标，引入注解（@Stateless、@Stateful、@MessageDriven、@EJB）、POJO 实体和 JPA 取代 CMP/BMP Entity Bean、依赖注入——深受 Spring 和 Hibernate 的影响。Gavin King 参与了 JSR 220 专家组，Hibernate 许多特性被纳入 JPA。
- EJB 旨在解决五大企业关注点：(a) 事务处理——容器管理（声明式，六种传播类型：MANDATORY, REQUIRED, REQUIRES_NEW, SUPPORTS, NOT_SUPPORTED, NEVER）和 Bean 管理（JTA）；(b) 远程调用——RMI-IIOP 及 Web Services；(c) 并发控制——容器保证同一 Bean 实例不被两个线程同时访问；(d) 安全——基于角色的声明式访问控制；(e) 持久化——Entity Bean (CMP/BMP)，后被 JPA 取代。

### 可用图片
- 无本地可用图片。建议创建：(1) EJB 多层架构图（Client → EJB Container → Database/JMS），(2) EJB 2.x "triple-class" 模式图（Home Interface + Remote/Local Interface + Bean Implementation + ejb-jar.xml），(3) 时间线（EJB 1.0 1998 → Hibernate 2001 → Rod Johnson 2002 → Spring 0.9 2003 → EJB 3.0 / Java EE 5 2006），(4) CMP vs BMP 对比图。

### 仍需补充
- EJB 在 2000–2003 年高峰期的采用率/市场份额定量数据（未找到 T1/T2 来源）。
- Rod Johnson 2002 年书中直接阐述核心论点的原文引用（全文不可读取）。
- TheServerSide.com 上 2002–2004 年 EJB 反思讨论的存档文章（当前无法检索以供 T2 级引用）。

---

## Chapter 3：The Spring Framework — Inversion of Control and the POJO Revolution
### 研究目标
- Trace the origin of the Spring Framework from Rod Johnson's critique of J2EE, explain its founding philosophy (IoC/DI, AOP, POJO-centric programming), and show how it systematically dismantled every pain point of the EJB model while remaining compatible with the broader Java EE ecosystem.
- Key subsections: Origin Story & Design Philosophy, IoC & Dependency Injection, Aspect-Oriented Programming, Integration Without Lock-In.

### 关键发现
- Rod Johnson 2002 年 10 月出版的书附带约 30,000 行框架代码，已包含 IoC 容器（`BeanFactory`、`ApplicationContext`）、Spring MVC 雏形、Template 概念（含 `JdbcTemplate`）和技术无关的数据访问异常。[Spring 官方博客](https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-name "Rod Johnson 亲述 Spring 起源")
- Spring 三位联合创始人：Rod Johnson（原始作者）、Yann Caroff（建议"Spring"之名，寓意 J2EE"寒冬"后的新生）、Juergen Hoeller（核心框架项目负责人，至 2026 年仍在任）。公司从 Interface21 → SpringSource (2007) → VMware 收购 (2009) → Pivotal (2013) → VMware (2019) → Broadcom (2023)。[Spring 官方博客](https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-name "三位联合创始人与命名由来")
- Spring Framework 主要版本时间线：0.9 (2003-06)、1.0 (2004-03-24)、2.0 (2006-10, XML namespace + AspectJ)、2.5 ([2007-11-19](https://spring.io/blog/2007/11/19/spring-framework-2-5-released "Spring 2.5 发布"), 注解驱动 DI)、3.0 ([2009-12-16](https://spring.io/blog/2009/12/16/spring-framework-3-0-goes-ga "Spring 3.0 GA"), Java 5+ 基线 + @Configuration + SpEL)、4.0 ([2013-12-12](https://spring.io/blog/2013/12/12/announcing-spring-framework-4-0-ga-release "Spring 4.0 GA"), Java 8 + WebSocket)、5.0 ([2017-09-28](https://spring.io/blog/2017/09/28/spring-framework-5-0-goes-ga "Spring 5.0 GA"), Java 8+ 基线 + Reactive WebFlux + Kotlin)、6.0 (2022-11-16, Java 17+ 基线 + Jakarta EE 9+)、6.1 (2023-11-16)、6.2 (2024-11-14)、7.0 (2025-11-13)。[Wikipedia](https://en.wikipedia.org/wiki/Spring_Framework "Version history table") [GitHub Wiki](https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-Versions "官方版本支持页面")
- IoC 容器两个核心接口：`BeanFactory`（基础 DI 和生命周期管理）与 `ApplicationContext`（扩展企业特性：事件发布、国际化、`BeanPostProcessor` 自动注册）。配置方式经历三阶段演进：XML `<bean>` (2003–2006) → 注解驱动 `@Component`/`@Autowired` (Spring 2.5, 2007) → Java 配置 `@Configuration`/`@Bean` (Spring 3.0, 2009)。三种 DI 方式：构造器注入（推荐）、setter 注入、字段注入（`@Autowired` on fields，因可测试性差已不鼓励）。同时支持 JSR-250 (`@Resource`) 和 JSR-330 (`@Inject`)。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/overview.html "Core container 模块描述")
- 六种内建 Bean 作用域：singleton（默认，per-container）、prototype（每次请求新实例，Spring 不管理销毁回调）、request、session、application、websocket（后四种仅 web-aware `ApplicationContext`）。可通过实现 `Scope` 接口自定义作用域。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html "Bean Scopes")
- Bean 生命周期回调调用顺序：`BeanFactoryPostProcessor`（bean 定义加载后、实例化前）→ `BeanPostProcessor.postProcessBeforeInitialization()` → `@PostConstruct` (JSR 250) → `InitializingBean.afterPropertiesSet()` → `@Bean(initMethod)` → `BeanPostProcessor.postProcessAfterInitialization()` → ready → `@PreDestroy` (JSR 250) → `DisposableBean.destroy()` → `@Bean(destroyMethod)`。`BeanPostProcessor` 是实现 `@Autowired`、AOP 代理、`@Scheduled` 等特性的核心机制。
- Spring AOP 基于代理模型：默认使用 **JDK 动态代理**（代理接口），当目标对象未实现接口时自动切换为 **CGLIB 代理**（代理类）。运行时代理包装，无需编译步骤或加载时织入。关键限制：**自调用（self-invocation）不经过代理，AOP advice 不生效**。自 Spring 2.0 起支持 `@AspectJ` 注解风格（`@Aspect`、`@Before`、`@After`、`@Around`、AspectJ 切点表达式语法）。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/core/aop/introduction-proxies.html "AOP Proxies")
- `@Transactional` 通过 AOP 代理实现声明式事务管理，直接取代 EJB 的 CMT 而无需应用服务器。默认设置：propagation=REQUIRED、isolation=DEFAULT、read-write、rollback 仅对 `RuntimeException` 和 `Error`（checked exception 默认不触发回滚，Spring 6.2 起可全局配置 `rollbackOn=ALL_EXCEPTIONS`）。自调用同样不触发事务行为。事务抽象通过 `PlatformTransactionManager`（imperative）和 `ReactiveTransactionManager`（reactive）提供。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html "@Transactional 使用指南")
- Spring 集成哲学：**包装而非替代**现有技术。`DataAccessException` 层次结构（源于 Rod Johnson 2002 年书第 9 章）将供应商特定异常（JDBC `SQLException`、Hibernate 异常、JPA 异常）转换为一致的、技术无关的、**unchecked** 运行时异常体系。[Spring Javadoc](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/dao/DataAccessException.html "DataAccessException 类文档") 模板类（`JdbcTemplate`、`JmsTemplate`）提供自动资源管理、一致异常转换和透明事务参与三大收益。
- JSR 330 ("Dependency Injection for Java") 由 Google 和 SpringSource 联合提交，Bob Lee (Google/Guice) 与 Rod Johnson (SpringSource) 任规范领导，2009 年 5 月提交，2009 年 10 月 14 日 Final Release——创下 JCP 最短开发周期纪录。定义 `javax.inject` 包（现 `jakarta.inject`）：`@Inject`、`@Named`、`@Qualifier`、`@Scope`、`@Singleton`、`Provider<T>`。Spring 自 3.0 起支持。[JCP JSR-330](https://www.jcp.org/en/jsr/detail?id=330 "JSR 330 时间线")
- Spring 官方文档列举五项设计原则：提供各层级选择自由、包容多元视角（不固执己见）、保持强向后兼容、注重 API 设计（直觉式、跨版本持久）、高代码质量标准（包间无循环依赖）。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/overview.html "Design Philosophy")

### 可用图片
- 无本地可用图片。建议创建：(1) Spring Framework 版本时间线（2003–2025），(2) Spring IoC 容器 bean 生命周期流程图，(3) Spring AOP 代理模型示意图（JDK dynamic proxy vs. CGLIB；external call → proxy → advice → target），(4) Spring 配置演进图（XML → Annotation → Java Config）。

### 仍需补充
- Interface21 → SpringSource → VMware → Pivotal → VMware → Broadcom 企业收购时间线的精确日期需从企业公告 T1 来源进一步确认。
- Spring 2.0 (约 2006-10) 和 Spring 5.3 (约 2020-10) 的精确 GA 发布日期需从官方博客确认。

---

## Chapter 4：Spring Core Modules — Essential Knowledge for the Working Developer
### 研究目标
- Provide a technical walkthrough of the Spring modules a developer must understand: the container and bean lifecycle, Spring MVC, data access with JDBC and JPA, transaction management, and Spring Security fundamentals — forming the practical knowledge base that underpins Spring Boot.
- Key subsections: ApplicationContext & Bean Lifecycle, Spring MVC (DispatcherServlet to REST Controllers), Data Access (JDBC / ORM / Repository), Transaction Management & Security Fundamentals.

### 关键发现
- **ApplicationContext 启动序列**：bean 定义加载（从 `@Configuration`、`@Bean`、XML/Groovy） → `BeanFactoryPostProcessor` 执行（修改 bean 定义，如 `PropertySourcesPlaceholderConfigurer` 解析 `${...}` 占位符） → bean 实例化 → 依赖注入 → `BeanPostProcessor` 执行（`AutowiredAnnotationBeanPostProcessor` 处理 `@Autowired`、AOP 代理包装） → 初始化回调（`@PostConstruct` → `InitializingBean.afterPropertiesSet()` → 自定义 init 方法） → bean 就绪。AOP 拦截器不在 init 时应用——目标 bean 完全创建后才应用 AOP 代理。`SmartLifecycle` 接口支持有序启动/关闭（`getPhase()` 值最小的最先启动、最后关闭）。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html "Bean lifecycle callback ordering and AOP proxy timing")
- **Spring MVC 前端控制器**：`DispatcherServlet` 采用前端控制器模式，是标准 Servlet，按 Servlet 规范声明和映射。请求处理流程：HTTP 请求 → `DispatcherServlet` → `HandlerMapping`（`RequestMappingHandlerMapping` 用于 `@RequestMapping`；`SimpleUrlHandlerMapping` 用于显式 URI 映射）找到 handler + 拦截器 → `HandlerAdapter` 调用 handler → controller 返回逻辑视图名或 `@ResponseBody` 数据 → `ViewResolver` 解析视图 → 视图渲染响应。对于 `@RestController`/`@ResponseBody` 方法，跳过视图解析，由 `HttpMessageConverter`（通常 Jackson）直接序列化到响应体。`@RestController` = `@Controller` + `@ResponseBody`。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html "DispatcherServlet front controller pattern") [Spring 官方文档](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet/special-bean-types.html "Special Bean Types")
- **@ControllerAdvice** 实现跨控制器的集中式异常处理、数据绑定和模型属性初始化。全局 `@ExceptionHandler` 在局部之后应用，全局 `@ModelAttribute`/`@InitBinder` 在局部之前应用。可通过 `annotations`、`basePackages`、`assignableTypes` 缩窄作用域。`@RestControllerAdvice` = `@ControllerAdvice` + `@ResponseBody`。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-advice.html "Controller Advice")
- **Spring Data JPA Repository 层次**：`Repository<T,ID>`（标记接口）→ `CrudRepository`（`save`、`findById`、`findAll`、`delete`…）→ `PagingAndSortingRepository`（分页和排序）→ `JpaRepository`（JPA 特定：`flush()`、`saveAndFlush()`、批量删除）。运行时由 Spring 生成代理实现，开发者零实现代码。查询派生采用 subject + predicate 解析结构（如 `findByEmailAddressAndLastname`），支持 `Between`、`Like`、`OrderBy`、嵌套属性遍历（`_` 分隔消歧），查找策略默认 `CREATE_IF_NOT_FOUND`（优先 `@Query`，无则从方法名派生）。[Spring Data JPA 官方文档](https://docs.spring.io/spring-data/jpa/reference/repositories/core-concepts.html "Repository hierarchy") [Spring Data JPA 官方文档](https://docs.spring.io/spring-data/jpa/reference/repositories/query-methods-details.html "Query derivation")
- **事务传播级别**（7 种）：`REQUIRED`（默认，加入现有或创建新事务）、`REQUIRES_NEW`（始终创建独立物理事务，挂起外层）、`NESTED`（单一物理事务 + JDBC savepoint）、`SUPPORTS`（有事务则加入，否则非事务）、`NOT_SUPPORTED`（挂起现有事务）、`MANDATORY`（要求现有事务）、`NEVER`（有事务则抛异常）。**事务隔离级别**（5 种）：`DEFAULT`、`READ_UNCOMMITTED`、`READ_COMMITTED`、`REPEATABLE_READ`、`SERIALIZABLE`。隔离属性仅对 `REQUIRED`/`REQUIRES_NEW` 生效；默认参与现有事务时静默忽略本地隔离级别，可设置 `validateExistingTransactions=true` 拒绝不匹配。[Spring 官方文档](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-propagation.html "Transaction Propagation") [Spring 官方文档](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html "@Transactional settings")
- **Spring Security 过滤器链架构**：Servlet `FilterChain` → `DelegatingFilterProxy`（桥接 Servlet 容器与 Spring `ApplicationContext`）→ `FilterChainProxy`（委派给一个或多个 `SecurityFilterChain` 实例；提供单一调试入口、`HttpFirewall` 保护、`RequestMatcher` 匹配）→ 各安全过滤器（`CsrfFilter`、`BasicAuthenticationFilter`、`UsernamePasswordAuthenticationFilter`、`AuthorizationFilter` 等）。多个 `SecurityFilterChain` 可配置，仅第一个匹配链被调用。[Spring Security 官方文档](https://docs.spring.io/spring-security/reference/servlet/architecture.html "Architecture – FilterChain")
- **认证链**：`AuthenticationManager`（API 定义） → `ProviderManager`（最常见实现，委派给 `AuthenticationProvider` 列表）→ 具体 `AuthenticationProvider`（`DaoAuthenticationProvider` 用于用户名/密码，`JwtAuthenticationProvider` 用于 JWT）。`SecurityContextHolder` 默认使用 `ThreadLocal` 存储已认证用户。`UserDetailsService` 核心接口仅一个方法 `loadUserByUsername(String)` 返回 `UserDetails`。[Spring Security 官方文档](https://docs.spring.io/spring-security/reference/servlet/authentication/architecture.html "AuthenticationManager, ProviderManager chain")
- **方法级安全**：`@EnableMethodSecurity`（取代已弃用的 `@EnableGlobalMethodSecurity`）默认启用 `@PreAuthorize`、`@PostAuthorize`、`@PreFilter`、`@PostFilter`。基于 Spring AOP 实现——`AuthorizationManagerBeforeMethodInterceptor` 拦截调用，`PreAuthorizeAuthorizationManager` 评估 SpEL 表达式（如 `hasRole('ADMIN')`、`#param == authentication.name`）。支持元注解（自定义 `@IsAdmin` 封装 `@PreAuthorize`）。Spring Boot Starter Security 默认不激活方法级授权。[Spring Security 官方文档](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html "Method Security")

### 可用图片
- 无本地可用图片。推荐引用或重绘以下官方文档图示：
  - Spring IoC Container 概念图：`https://docs.spring.io/spring-framework/reference/_images/container-magic.png`
  - Spring Security FilterChain 架构图系列：`https://docs.spring.io/spring-security/reference/_images/servlet/architecture/filterchain.png`、`delegatingfilterproxy.png`、`filterchainproxy.png`、`securityfilterchain.png`、`multi-securityfilterchain.png`
  - ProviderManager 链：`https://docs.spring.io/_images/servlet/authentication/architecture/providermanager.png`
  - 事务传播示意图：`tx_prop_required.png`、`tx_prop_requires_new.png`
  - Method Security AOP 流程图：`https://docs.spring.io/spring-security/reference/_images/servlet/authorization/methodsecurity.png`

### 仍需补充
- `JdbcTemplate` 详细用法（`RowMapper`、`NamedParameterJdbcTemplate`、回调接口）——需读取 `https://docs.spring.io/spring-framework/reference/data-access/jdbc/core.html`。
- JPA/Hibernate 集成细节（`LocalContainerEntityManagerFactoryBean`、`@Repository` 异常转换）——需读取 JPA ORM 页面。
- Spring MVC 内容协商（`Accept` header 驱动响应格式）和视图解析器详情（`InternalResourceViewResolver`、`ThymeleafViewResolver`）为次要补充项。

---

## Chapter 5：Spring Boot — Convention Over Configuration and Production Readiness
### 研究目标
- Explain how Spring Boot eliminated the remaining friction of the Spring Framework (XML configuration, dependency version management, WAR deployment, manual server setup) by embracing opinionated defaults, auto-configuration, and an embedded-server model — making Spring accessible for rapid development and cloud-native deployment.
- Key subsections: The Problem Spring Boot Solved, Auto-Configuration & Starter POMs, Embedded Servers & Initializr, Production-Ready Features (Actuator, profiles, externalized config).

### 关键发现
- Spring Boot 起源于 2012 年 10 月 Mike Youngstrom 提交的社区功能请求 [SPR-9888](https://github.com/spring-projects/spring-framework/issues/14521 "Improved support for containerless web application architectures")，要求将 Servlet 容器配置嵌入 Spring 组件模型，消除开发者学习 `web.xml`、WAR 目录结构、容器特定线程池配置和复杂类加载层次的需求，明确以 DropWizard 为灵感。SPR-9888 列举的七大摩擦点涵盖：`web.xml`、`.war` 结构、容器特定配置（端口/线程池）、复杂类加载层次、应用外监控管理、容器特定日志、应用上下文根配置。
- Spring Boot 1.0 GA 于 2014 年 4 月 1 日发布，由 Phil Webb 在官方博客宣布，历时 18 个月开发、1,720 次提交、54 位贡献者、549 个 issue 关闭。Webb 将项目定位为"ultralight container, great for application or service deployment in the cloud"。[Spring Boot 1.0 GA](https://spring.io/blog/2014/04/01/spring-boot-1-0-ga-released "Phil Webb, April 1 2014")
- 主要版本时间线：1.0 (2014-04-01)、1.1 (2014-06-10)、1.5 (约 2017-01)、2.0 ([2018-03-01](https://spring.io/blog/2018/03/01/spring-boot-2-0-goes-ga "Spring Boot 2.0 GA"), Spring Framework 5.0 + Java 8 基线 + WebFlux + Micrometer metrics + 重新设计 Actuator)、2.7 ([2022-05-19](https://spring.io/blog/2022/05/19/spring-boot-2-7-0-available-now "Spring Boot 2.7"))、3.0 ([2022-11-24](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga "Spring Boot 3.0 GA"), Java 17 基线 + Jakarta EE 10 + GraalVM 原生镜像 + Micrometer Tracing)、3.1 (2023-05-18)、3.2 (2023-11-23)、3.3 (2024-05-23)、3.4 (2024-11-21)、3.5 ([2025-05-22](https://spring.io/blog/2025/05/22/spring-boot-3-5-0-available-now "Spring Boot 3.5 GA"))。
- `@SpringBootApplication` 是便捷元注解，组合三个注解：`@EnableAutoConfiguration`（启用自动配置）、`@ComponentScan`（扫描应用类所在包）、`@SpringBootConfiguration`（`@Configuration` 变体，辅助集成测试配置发现）。[Spring Boot 官方文档](https://docs.spring.io/spring-boot/reference/using/using-the-springbootapplication-annotation.html "@SpringBootApplication")
- 自动配置机制：自动配置类使用 `@AutoConfiguration`（元注解含 `@Configuration`），通过 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 文件发现（列出全限定类名，一行一个）。此机制取代了早期 `spring.factories` 方式（Spring Boot 2.7 起弃用，3.0 完全迁移）。六类条件注解门控自动配置：Class 条件（`@ConditionalOnClass`/`@ConditionalOnMissingClass`）、Bean 条件（`@ConditionalOnBean`/`@ConditionalOnMissingBean`）、Property 条件（`@ConditionalOnProperty`）、Resource 条件、Web Application 条件、SpEL 表达式条件。[Spring Boot 官方文档](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html "Auto-configuration mechanism and Condition Annotations")
- Starter POM 架构上是"空 JAR"，仅聚合给定技术所需依赖。命名约定：官方 `spring-boot-starter-*`，第三方 `<technology>-spring-boot-starter`。所有 starter 直接或间接引用核心 `spring-boot-starter`（提供自动配置支持、Logback 日志、YAML 配置支持）。例如 `spring-boot-starter-web` 传递引入 Spring MVC + Jackson + 嵌入式 Tomcat。
- 嵌入式服务器：支持 Apache Tomcat（默认）、Eclipse Jetty、JBoss Undertow（Servlet 容器），以及 Netty（WebFlux reactive）。可执行 JAR（"fat JAR"）打包通过 `spring-boot-maven-plugin` / Gradle 插件实现，将应用、所有依赖和嵌入服务器打包为单一可运行归档，以 `java -jar app.jar` 启动，彻底消除 WAR 部署和外部应用服务器依赖。
- Spring Initializr (https://start.spring.io) 生成预配置 Spring Boot 项目。截至 2015 年 10 月，月生成约 50,000 个项目，98% 面向 Java，80% 使用 Maven，82% 使用 Java 8，83% 选择 JAR 打包。最热门 starter：web (63%)、Spring Data JPA (25%)、Spring Security (21%)、MySQL (19%)。提供 Web UI、IDE 集成和 CLI 工具。[Spring Blog](https://spring.io/blog/2015/10/06/evolving-spring-initializr "October 2015 usage statistics")
- Actuator 内建端点涵盖：`health`（健康检查，支持 Kubernetes liveness/readiness 探针）、`info`、`metrics`、`env`（Environment 属性）、`beans`（所有 Bean）、`configprops`（@ConfigurationProperties）、`conditions`（自动配置评估报告）、`loggers`（查看/修改日志级别）、`mappings`（@RequestMapping 路径）、`threaddump`、`heapdump`、`shutdown`（默认禁用）、`prometheus` 等。默认仅 `health` 端点通过 HTTP 暴露。基路径 `/actuator`。[Spring Boot 官方文档](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html "Actuator Endpoints")
- 外部化配置采用 15 级 `PropertySource` 优先级排序（从低到高：`setDefaultProperties` → `@PropertySource` → config data → 环境变量 → 系统属性 → 命令行参数 → 测试属性等）。Profile 特定文件（`application-{profile}.properties`）覆盖通用文件，JAR 外文件覆盖 JAR 内文件。`@ConfigurationProperties` 提供类型安全绑定（JavaBean 风格、构造器绑定、relaxed binding 规则）。[Spring Boot 官方文档](https://docs.spring.io/spring-boot/reference/features/external-config.html "Externalized Configuration")

### 可用图片
- 无本地可用图片。建议创建：(1) 自动配置决策树图（`@ConditionalOnClass` → `@ConditionalOnMissingBean` → bean 注册流程），(2) Fat JAR vs. WAR 部署模型对比图，(3) Actuator 端点架构概览图。

### 仍需补充
- Spring Initializr 的精确首次上线日期（可能为 2013 年或 2014 年初，与 Spring Boot 早期版本同期），未找到 T1 来源确认具体日期。
- Spring Boot 1.5.0 GA 精确日期（1.5.1 于 2017-01-30 发布，1.5.0 GA 约在其前几天）。

---

## Chapter 6：The Modern Spring Ecosystem — Spring Boot 3.x and Beyond
### 研究目标
- Survey the current state and forward trajectory of the Spring ecosystem as of Spring Boot 3.x / Spring Framework 6.x, covering the Jakarta EE migration, GraalVM native images, virtual threads (Project Loom), and the reactive programming model — placing the evolutionary story into its present context.
- Key subsections: Spring Boot 3.x & Jakarta EE Migration, GraalVM Native Images & AOT, Virtual Threads & Project Loom, The Reactive Stack (WebFlux & R2DBC).

### 关键发现
- Spring Boot 3.0 GA 于 2022 年 11 月 24 日发布，距 2.0 (2018-03-01) 4.5 年，包含 5,700+ 次提交、151 位贡献者。四大头条特性：Java 17 基线、Jakarta EE 10 (EE 9 基线)、GraalVM 原生镜像支持（取代实验性 Spring Native）、Micrometer/Micrometer Tracing 改进的可观测性。[Spring Boot 3.0 GA](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga "Phil Webb, November 24 2022") Spring Framework 6.0 GA 于 2022 年 11 月 16 日发布（早于 Boot 3.0 八天），引入 Java 17+ 基线、`jakarta` 命名空间、AOT 转换基础设施。Juergen Hoeller 描述为"the start of a new framework generation for 2023 and beyond"。[Spring Framework 6.0 GA](https://spring.io/blog/2022/11/16/spring-framework-6-0-goes-ga "Juergen Hoeller, November 16 2022")
- **Jakarta EE 命名空间迁移**：Jakarta EE 9 ([Release review ballot 2020-11-20](https://jakarta.ee/specifications/platform/9/ "Eclipse Foundation")) 将所有 `javax.*` 包重命名为 `jakarta.*`，功能上等同于 Jakarta EE 8/Java EE 8。Jakarta EE 10 ([Release review ballot 2022-09-13](https://jakarta.ee/specifications/platform/10/ "Eclipse Foundation")) 是 `jakarta.*` 下首个功能版本，设定 Java SE 11 最低基线，移除弃用特性（applet、Entity Bean、嵌入式 EJB 容器）。迁移要求开发者更新所有 import 语句（如 `javax.servlet.http.HttpServletRequest` → `jakarta.servlet.http.HttpServletRequest`）、注解、第三方库兼容性——Spring Boot 3.0 / Framework 6.0 强制要求此迁移，无 `javax.*` 向后兼容。
- **GraalVM 原生镜像与 AOT 处理**：原生镜像在"闭世界假设"下运行——bean 定义不可运行时变更、`@Profile` 受限、条件属性创建 bean (`@ConditionalOnProperty .enabled`) 不支持。Spring AOT 在构建时生成三类产物：(a) Java 源码——将 `@Configuration` 解析和 `@Bean` 反射转换为直接静态可分析的 `BeanDefinition` 源码；(b) 运行时代理的字节码（如 CGLIB 代理）；(c) GraalVM JSON hint 文件（`reflect-config.json`、`resource-config.json` 等）。权衡：启动速度极快（毫秒级 vs. 秒级）、更低内存占用、无 JIT 预热 vs. 无运行时反射（需 hint 声明）、构建时间长（分钟级）、动态行为受限、调试更困难。通过 `spring-boot-maven-plugin` (native profile) 或 Cloud Native Buildpacks 构建。[Spring Boot 官方文档](https://docs.spring.io/spring-boot/reference/packaging/native-image/introducing-graalvm-native-images.html "GraalVM Native Images & AOT")
- **虚拟线程 (Project Loom)**：[JEP 444](https://openjdk.org/jeps/444 "Virtual Threads — finalized in JDK 21") 定义虚拟线程，JDK 19 (2022-09) 预览、JDK 21 (2023-09 GA) 正式发布。采用 M:N 调度——大量 (M) 虚拟线程调度到少量 (N) 平台线程上，调度器为 work-stealing `ForkJoinPool` (FIFO 模式)。当虚拟线程调用阻塞 I/O 操作时，运行时自动挂起并释放底层平台线程。关键限制："pinning"——在 `synchronized` 块/方法或本地方法内无法卸载虚拟线程。每个虚拟线程初始仅消耗 ~1 KB 栈（平台线程 ~1 MB），使 thread-per-request 模型可扩展至数千至数百万并发请求。
- **Spring Boot 虚拟线程支持**：Spring Boot 3.2.0 ([2023-11-23](https://spring.io/blog/2023/11/23/spring-boot-3-2-0-available-now "Virtual Threads as headline feature")) 引入一等虚拟线程支持。通过 `spring.threads.virtual.enabled=true` 启用，自动配置 Tomcat/Jetty/Undertow 请求处理和 `@Async` 任务执行的 virtual-thread-per-task executor，Spring MVC 控制器无需代码更改即在虚拟线程上运行。Spring 团队指出"The reasons to use asynchronous programming models go away in many cases if we start with the assumption that our code runs on Virtual Threads"，异步 Servlet API (`ServletRequest.startAsync()`) 在虚拟线程下"subject to be invalidated"。[Spring 官方博客](https://spring.io/blog/2022/10/11/embracing-virtual-threads "Embracing Virtual Threads, October 2022")
- **Reactive 栈**：Project Reactor 提供 `Flux<T>`（0..N 异步序列）和 `Mono<T>`（0..1 异步结果），实现 Reactive Streams 规范，提供非阻塞背压感知数据访问。[Project Reactor](https://projectreactor.io/docs/core/release/reference/coreFeatures/flux.html "Flux reference") R2DBC 1.0.0.RELEASE 规范于 2022-04-25 发布，由 Reactive Foundation 领导，定义 `ConnectionFactory`、`Connection`、`Statement`、`Result`、`Row` 等 SPI。Spring Data R2DBC 提供 `R2dbcEntityTemplate` 和自动 repository 实现，镜像 Spring Data JPA 编程模型但面向非阻塞数据库访问。[R2DBC 1.0 规范](https://r2dbc.io/spec/1.0.0.RELEASE/spec/html/ "R2DBC 1.0.0.RELEASE, 2022-04-25") [Spring Data R2DBC 文档](https://docs.spring.io/spring-data/relational/reference/r2dbc.html "Spring Data R2DBC reference")
- **Reactive vs. 虚拟线程适用场景**：Reactive（WebFlux + Reactor + R2DBC）在高并发 I/O 密集场景、流式数据管道（需背压）、声明式并发组合中最具价值。虚拟线程 (JDK 21+) 显著降低了 I/O 密集负载中 reactive 的核心动机（线程效率），简单请求-响应服务使用 Spring MVC + 虚拟线程可获得等效扩展性且编程模型更简单。CPU 密集型负载两者均无并发收益。Spring 团队立场："ReactiveX-style APIs remain a powerful way to compose concurrent logic and a natural way for dealing with streams"，虚拟线程"complement reactive programming models in removing barriers of blocking I/O"。
- **最新版本** (截至 2026 年 4 月)：Spring Framework 7.0 GA ([2025-11-13](https://spring.io/blog/2025/11/13/spring-framework-7-0-general-availability "Juergen Hoeller")) 引入 Jakarta EE 11 (Servlet 6.1, JPA 3.2)、JSpecify 全面 null safety、Jackson 3.0、Kotlin 2.2、JUnit 6.0 支持，Java 17 基线 / Java 25 推荐 LTS。Spring Boot 4.0.0 GA ([2025-11-20](https://spring.io/blog/2025/11/20/spring-boot-4-0-0-available-now "Phil Webb")) 基于 Framework 7.0，引入代码库完全模块化、JSpecify null safety、API 版本控制。截至 2026 年 3 月 26 日，最新稳定版为 4.0.5 和 3.5.13。[endoflife.date](https://endoflife.date/spring-boot "Version support matrix")

### 可用图片
- 无本地可用图片。建议创建：(1) Spring Boot 版本时间线图 (1.0→4.0)，标注 Jakarta EE、GraalVM、虚拟线程里程碑，(2) GraalVM AOT 处理流程图 (@Configuration → AOT → BeanDefinition source + hint files → native-image)，(3) 虚拟线程 vs. 平台线程架构对比图 (M:N scheduling)，(4) 决策树：何时选择 WebFlux/Reactive vs. Spring MVC + Virtual Threads。

### 仍需补充
- GraalVM native image 实际性能基准数据（如 Spring Petclinic native vs. JVM 启动时间/内存对比），需 T1/T2 来源的具体数字。
- Jakarta EE 11 详细新增 API 特性列表（Servlet 6.1、JPA 3.2 等），需从 Eclipse Foundation 获取。
- Spring Boot 4.0 中虚拟线程是否有超越 3.2 的增强（如默认启用、structured concurrency 集成）。
- Project CRaC (Coordinated Restore at Checkpoint) 在 Spring Boot 中的成熟度与配置方式。

---

# Section 2：给 Write 阶段的执行建议

- **Chronological-then-thematic arc**: Chapters 1–5 follow a continuous evolutionary narrative; each chapter opens by recalling the unresolved pain from the previous era. Chapter 6 pivots to a survey-style treatment of coexisting modern concerns.
- **Tone**: Technically authoritative but pedagogically accessible. Avoid hagiography; present design trade-offs honestly. Use concrete code-level examples (class names, annotations, configuration snippets).
- **Terminological consistency**: Use canonical terms uniformly — "Servlet specification" (not "Servlets spec"), "Spring IoC container" (not "Spring DI container"), "Jakarta EE" for post-2019, "Java EE" / "J2EE" for historical. Pin version references explicitly (e.g., "Servlet 2.3," "EJB 2.0," "Spring Framework 5.3," "Spring Boot 3.2").
- **Authoritative sourcing**: Anchor factual claims to JSR numbers (JSR-154, JSR-330, JSR-317, etc.), official Spring blog announcements, Spring Framework GitHub release notes, and Spring Boot reference documentation. Release dates, version numbers, and specification details all require sourced verification.
- **Diagrams**: Recommended figures — (a) Servlet container request lifecycle, (b) EJB multi-tier vs. Spring simplified model, (c) Spring IoC bean lifecycle flowchart, (d) Spring MVC DispatcherServlet request flow, (e) Spring Boot auto-configuration decision tree, (f) timeline 1997–2026 of major releases.
- **Chapter bridging**: End each chapter with a 1–2 sentence forward pointer naming the specific limitation being carried forward.
- **Chapter 4 distinction**: Chapter 4 is the practitioner-reference chapter — more example-dense and recipe-oriented, while others emphasize rationale and architecture.
- **Spring Boot chapter**: Explain *why* each Boot feature exists (what prior pain it removes), not merely list features. Trace every auto-configuration mechanism or Actuator endpoint back to a concrete frustration from earlier chapters.
