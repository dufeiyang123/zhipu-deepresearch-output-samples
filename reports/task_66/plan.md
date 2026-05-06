# Section 1：章节研究计划

## Chapter 1：Notion's Multi-View Database — The Benchmark

### 研究目标
- Establish a precise, feature-level benchmark of Notion's multi-view database: what the four canonical view types (Table, Board/Kanban, Calendar, List) offer in terms of interactions (inline editing, drag-and-drop, grouping, sub-grouping).
- Document cross-view capabilities: filters, sorts, properties/fields (relation, rollup, formula, select, multi-select, date, person), linked databases, and templates.
- Identify known limitations of Notion's database system (offline access, performance at scale, local data ownership) that motivate users to seek Obsidian alternatives.

### 关键发现
- Notion databases support **10 distinct view types** (Table, Board/Kanban, Timeline, Calendar, List, Gallery, Chart, Form, Map, Feed) plus Dashboards — well beyond the "four canonical views" originally assumed [Notion Help: Views, Filters, Sorts & Groups](https://www.notion.com/help/views-filters-and-sorts "Official documentation listing all database view layouts").
- Table view supports inline editing, column freezing, column calculations (sum/average/median/min/max/count), conditional row/cell coloring, and column reordering via drag. Board (Kanban) view groups by property with drag-and-drop card movement between groups, sub-grouping, and conditional color [Notion Help: Views, Filters, Sorts & Groups](https://www.notion.com/help/views-filters-and-sorts "View interaction details").
- Calendar view displays items by Date property in a monthly grid with click-to-create on any day. List view provides a minimal layout. Gallery view highlights images from Files & media property [Notion Help: Intro to Databases](https://www.notion.com/help/intro-to-databases "Calendar, List, Gallery view descriptions").
- Timeline view plots items chronologically with adjustable timeframe (hours to years), drag-and-drop to adjust duration, and a companion table on the left [Notion Help: Timeline View](https://www.notion.com/help/timelines "Official timeline view documentation").
- Chart view supports Vertical bar, Horizontal bar, Line, and Donut charts, with up to 200 groups and 50 subgroups; 1 chart on Free plan, unlimited on paid [Notion Help: Charts](https://www.notion.com/help/charts "Chart limits and features").
- Notion databases support **22 property types**: Text, Number, Select, Status, Multi-Select, Date, Formula, Relation, Rollup, Person, File, Checkbox, URL, Email, Phone, Created time, Created by, Last edited time, Last edited by, Button, ID (Unique ID), Place [Notion Help: Database Properties](https://www.notion.com/help/database-properties "Official property type enumeration").
- Advanced filters support nested AND/OR logic up to 3 levels deep, applied per-view and saveable as personal or shared [Notion Help: Views, Filters, Sorts & Groups](https://www.notion.com/help/views-filters-and-sorts "Advanced filter nesting").
- Relations support one-way and two-way (bidirectional) linking across databases or within the same database (self-relations), with API limit of 100 related pages per property and 10,000 two-way references [Notion Help: Relations & Rollups](https://www.notion.com/help/relations-and-rollups "Relation mechanics") [Notion API: Request Limits](https://developers.notion.com/reference/request-limits "API relation limits").
- Rollups offer 15+ calculation types including Show original, Count all/values/unique/empty, Sum, Average, Median, Min, Max, Range, Earliest/Latest date, Date range; rollups cannot roll up other rollups [Notion Help: Relations & Rollups](https://www.notion.com/help/relations-and-rollups "Rollup calculation types").
- Formula language includes conditional logic (if/ternary), date math (dateAdd, now), list operations (.length, .first, .every with current keyword), text styling (style() with colors/formatting), and dot-notation property traversal; AI-assisted formula creation is available on Business/Enterprise plans [Notion Help: Formulas](https://www.notion.com/help/formulas "Formula language capabilities").
- Database automations (paid plans, except Slack on Free) support triggers (page added, property edited, recurring time-based) and actions (edit property, add page, send notification/Slack/webhook/Gmail, define variables with formulas) [Notion Help: Database Automations](https://www.notion.com/help/database-automations "Automation triggers and actions").
- Offline access is limited: databases show only the first 50 rows of the first view; paid plans auto-download recent/favorited pages; web browser has no offline support [Notion Help: Use Pages Offline](https://www.notion.com/help/use-pages-offline "Offline database limitations").
- Export limitations: CSV export loses relation links (converted to plain text URLs, non-reimportable); only current/default view can be exported at once; PDF with subpages requires Business/Enterprise; full workspace export can take up to 30 hours [Notion Help: Export Your Content](https://www.notion.com/help/export-your-content "Export constraints").
- Per-page property data limited to 2.5 MB; database schema structure limited to 1.5 MB; API rate limit of 3 requests/second per integration [Notion Help: Optimize Database Performance](https://www.notion.com/help/optimize-database-load-times-and-performance "Size and performance limits") [Notion API: Request Limits](https://developers.notion.com/reference/request-limits "API rate limits").

### 可用图片
（无本地相关图片）

### 仍需补充
- Feed view and Dashboards view detailed capabilities — dedicated help pages not retrieved.
- Map view and Form view specifics beyond sidebar listing confirmation.
- Notion AI autofill for databases: help page returned 404; full details of which property types can be AI-autofilled are unverified.
- Gallery view conditional color support: not explicitly listed among the 6 conditional-color-supported views — needs verification.
- Specific pricing dollar amounts per plan (JavaScript-rendered, not captured in scrape).
- Community-reported performance threshold (~10,000 entries) is T3/T4 only; no T1/T2 source confirms a specific entry limit.

## Chapter 2：The Obsidian Plugin Landscape for Database Functionality

### 研究目标
- Explain how Obsidian's markdown-first, frontmatter/properties architecture differs from Notion's proprietary block model, and what structural advantages/constraints this imposes on database plugins.
- Survey the current plugin ecosystem (as of mid-2026): which plugins are actively maintained, which are archived or stalled, and how the launch of the Bases core plugin (Obsidian 1.9+) has reshaped the landscape.
- Define which plugins will be evaluated in this report and the rationale for inclusion/exclusion.

### 关键发现
- Obsidian stores all data as plain Markdown files with metadata in YAML frontmatter. The **Properties** system was introduced in **Obsidian 1.4** (public release: August 31, 2023), supporting 7 typed property types: Text, List, Number, Checkbox, Date, Date & time, Tags [Obsidian Changelog v1.4](https://obsidian.md/changelog/2023-08-31-desktop-v1.4.5/ "Obsidian 1.4 public release introducing Properties").
- Architectural advantages over Notion: full local data ownership, plaintext interoperability, no vendor lock-in, offline-first (full functionality offline, vs. Notion's 50-row database limit). Constraints: no server-side compute, no native real-time collaboration, no block-level structured data [Obsidian Help: Properties](https://help.obsidian.md/Editing+and+formatting/Properties "Properties stored as YAML frontmatter").
- **Bases** core plugin was introduced in **Obsidian 1.9.0** (early access: May 21, 2025; public: August 18, 2025), described as "a new core plugin that lets you turn any set of notes into a powerful database." It introduced the `.base` file format, table views with filtering, and formula-based dynamic columns [Obsidian Changelog v1.9.0](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/ "Bases introduced in Obsidian 1.9.0").
- Bases received major updates in **v1.10.0** (October 1, 2025): Group By, table summaries, **List view**, initial **Bases API** with `registerView()` for community-developed view types, keyboard navigation, copy/paste, undo/redo, and new formula functions (`reduce()`, `html()`, `random()`). An official **Maps plugin** was released as a Bases API demo [Obsidian Changelog v1.10.0](https://obsidian.md/changelog/2025-10-01-desktop-v1.10.0/ "Bases major update with API and List view").
- In **Obsidian 1.12** (February 27, 2026), Bases gained search toolbar, drag-and-drop file import, and right-click context menus on table rows [Obsidian Changelog v1.12](https://obsidian.md/changelog/ "Bases improvements in v1.12").
- **Dataview** is the most widely installed community database plugin with ~3,272,000 downloads and ~8,700 GitHub stars. Latest release v0.5.70 (~April 2025); 134 days since last commit — effectively in **maintenance mode**. Provides DQL query language and DataviewJS API; renders tables, lists, tasks, calendars, but is **read-only** (no inline editing or drag-and-drop). License: MIT [Obsidian Community Plugin Stats](https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json "Dataview: 3,272,416 downloads") [ObsidianStats: Dataview](https://www.obsidianstats.com/plugins/dataview "v0.5.70, maintenance mode").
- **DB Folder** has ~323,000 downloads; latest release v3.5.1 (~early 2025); 515 days since last commit, 179 open issues — effectively **stalled/unmaintained**. Provides Notion-like database based on folders/links/tags/Dataview queries; depends on Dataview. License: MIT [ObsidianStats: DB Folder](https://www.obsidianstats.com/plugins/dbfolder "Stalled, 515 days since last commit").
- **DataLoom** (formerly "Notion-Like Tables" → "Dashboards" → "DataLoom") was **archived on March 9, 2025** and **removed from the Obsidian plugin directory on May 3, 2025**. Developer cited Obsidian's native table editor (v1.5.0) as a factor. Last release v8.16.1 (June 29, 2024). This is a significant discontinuation [GitHub Issue #958](https://github.com/decaf-dev/obsidian-dataloom/issues/958 "Developer announcement: DataLoom no longer maintained") [Moritz Jung Obsidian Stats](https://www.moritzjung.dev/obsidian-stats/plugins/notion-like-tables/ "Archived Mar 2025, removed May 2025").
- **Projects** (by Marcus Olsson): latest release v1.17.4 (~June 2025). Originally reported as community-maintained, but **Chapter 4 research confirmed Projects was discontinued by the original author in May 2025 and the repository archived July 18, 2025** [Projects GitHub Issues](https://github.com/obsmd-projects/obsidian-projects/issues/1011 "Repository archived Jul 18, 2025"). Provided **four view types**: Table, Board (Kanban), Calendar, Gallery. Supports folder and Dataview query sources, customizable note templates. License: Apache-2.0 [ObsidianStats: Projects](https://www.obsidianstats.com/plugins/obsidian-projects "v1.17.4, 4 view types").
- **Kanban** (by mgmeyers): ~2,100,000 downloads; latest release v2.0.51 (~early 2024) — **~2 years without a release**, effectively stalled. Creates markdown-backed Kanban boards with cards/lanes stored as Markdown lists. License: MIT [ObsidianStats: Kanban](https://www.obsidianstats.com/plugins/obsidian-kanban "2.1M downloads, last release ~2 years ago").
- **Full Calendar** (by davish): latest release v0.10.7 (~mid 2023); 984 days since last release, 5 commits in past year — **functionally abandoned**. Integrates FullCalendar library for day/week/month views; events as notes with frontmatter; read-only ICS/CalDAV support. License: MIT [ObsidianStats: Full Calendar](https://www.obsidianstats.com/plugins/obsidian-full-calendar "984 days since last release").
- The Obsidian community plugin ecosystem had **2,498 plugins** listed as of early 2026. The introduction of Bases as a core plugin represents a significant landscape shift — several major community database plugins stalled coinciding with Bases' release [ObsidianStats](https://www.obsidianstats.com/plugins "2498 plugins listed").
- The Bases API `registerView()` signals Obsidian's intent for Bases to become a platform that community plugins extend (e.g., the Maps plugin), rather than directly competing with community solutions [Obsidian Changelog v1.10.0](https://obsidian.md/changelog/2025-10-01-desktop-v1.10.0/ "Bases API registerView() for community view types").

### 可用图片
（无本地相关图片）

### 仍需补充
- Exact download counts for Projects and Full Calendar (data exists in community-plugin-stats.json but not fully extracted).
- GitHub stars for DB Folder, Projects, Kanban, Full Calendar.
- TileLineBase plugin status — no data found; may be too niche to include.
- Bases official help documentation URL (help.obsidian.md/Plugins/Bases returned 404; docs may not yet be published).
- DataLoom should still be evaluated in Chapter 3 as a historical benchmark for users who have it installed, but must prominently note its discontinued status.

## Chapter 3：Plugin-by-Plugin Deep Dive

### 研究目标
- Provide individually structured evaluations of each major plugin or plugin combination: Bases (core), Dataview/DataviewJS, DB Folder, DataLoom, Projects (Marcus Olsson), Kanban plugin, Full Calendar plugin, and emerging contenders.
- For each: which of the four Notion view types it supports, how faithfully it replicates the Notion experience, how it handles advanced features (relations, rollups, formulas, inline editing, drag-and-drop, filtering, sorting, grouping).
- For each: development status (active, maintenance-mode, archived), release cadence, community size, compatibility with other plugins.
- Compare multi-plugin stacks (Dataview + Kanban + Full Calendar) vs. monolithic solutions (DataLoom, Projects, Bases).

### 关键发现

**3.1 Bases (Core Plugin)**
- Supports **4 built-in views**: Table (v1.9), Cards/Gallery (v1.9), List (v1.10), Map (v1.10, requires Maps plugin). Does **not** natively include Kanban or Calendar views as of v1.12 [Obsidian Bases Guide](https://got.md/obsidian-bases/ "Built-in layouts: Table, Cards, List, Map").
- 3 property categories: note properties (YAML frontmatter), file properties (system metadata like `file.name`, `file.ctime`, `file.tags`, `file.backlinks`), formula properties (computed columns in `.base` file). Inherits 7 core Obsidian property types: Text, List, Number, Checkbox, Date, Date & time, Tags [Obsidian Changelog v1.9.0](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/ "Data backed by YAML properties").
- Formula properties support `reduce()`, `html()`, `random()`, `list()`, `today()`, date arithmetic, string operations, `if()` conditionals [Obsidian Changelog v1.10.0](https://obsidian.md/changelog/2025-10-01-desktop-v1.10.0/ "New formula functions").
- Full inline editing (cell edits persist to YAML frontmatter). Filtering via global + per-view filters with folder/tag/link scope and nested AND/OR/NOT logic. Group By and table summaries (v1.10). Search toolbar and drag-and-drop file import (v1.12) [Obsidian Bases Guide](https://got.md/obsidian-bases/ "Inline editing, 6 filter primitives, nested logic").
- No explicit Relation/Rollup property types — link properties + formulas + `file.hasLink()`/`file.linksTo()` approximate this behavior [Obsidian Bases Guide](https://got.md/obsidian-bases/ "Formulas and link-based filters approximate relations").
- `this` context keyword enables reusable context-aware dashboards. Bases API `registerView()` allows community-developed view types [Obsidian Changelog v1.10.0](https://obsidian.md/changelog/2025-10-01-desktop-v1.10.0/ "Bases API registerView()").
- **Strengths**: First-party with long-term support; extensible API; full inline editing; context-aware `this`. **Weaknesses**: No native Kanban/Calendar; no Relation/Rollup types; still maturing; proprietary formula language.

**3.2 Dataview / DataviewJS**
- 4 query output types: TABLE, LIST, TASK, CALENDAR (monthly calendar with dots on dates; requires date field) [Dataview Docs: Query Types](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/ "Four query types").
- 8 field types: Text, Number, Boolean, Date (with `.year/.month/.day` sub-properties), Duration, Link, List, Object. Indexes both YAML frontmatter and inline fields (`[key:: value]`). Extensive implicit fields (`file.name`, `file.path`, `file.ctime`, `file.tags`, `file.inlinks`, etc.) [Dataview Docs: Types of Metadata](https://blacksmithgu.github.io/obsidian-dataview/annotation/types-of-metadata/ "8 field types").
- DQL data commands: FROM (folder/tag/link + AND/OR/NOT), WHERE, SORT, GROUP BY, FLATTEN, LIMIT. Computed/virtual fields supported inline. DataviewJS provides full JavaScript API (`dv.pages()`, `dv.table()`, `dv.list()`) [Dataview Docs: Query Types](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/ "DQL data commands and computed expressions").
- **Strictly read-only** (no inline editing, no drag-and-drop, no GUI configurator) — except TASK queries allow checkbox toggling in source files [Dataview Docs](https://blacksmithgu.github.io/obsidian-dataview/ "Displaying, not editing").
- Scales to "hundreds of thousands of annotated notes" per documentation [Dataview Docs](https://blacksmithgu.github.io/obsidian-dataview/ "High performance scaling").
- **Strengths**: Most powerful/flexible query language; massive user base (~3.27M); scales to huge vaults; inline fields unique. **Weaknesses**: Read-only; code-only interface; maintenance mode; no Kanban/Gallery/Board views.

**3.3 DB Folder (ARCHIVED July 2025)**
- Single view: **interactive Table** only (no Kanban/Calendar/Gallery) [DB Folder Docs](https://rafaelgb.github.io/obsidian-db-folder/ "Notion's like databases — table view").
- **14 property types** — the richest among community plugins: Text, Number, Checkbox, Date, Time, Select, Tags (multi-select), Formulas (JavaScript-based), Image, Created time, Modified time, Tasks, Inlinks, Outlinks, **Relation**, and **Rollup** [DB Folder Properties Docs](https://rafaelgb.github.io/obsidian-db-folder/features/Properties/ "14 property types including Relation and Rollup").
- **Only community plugin with explicit Relation and Rollup support**, directly mirroring Notion's data model [DB Folder Properties Docs](https://rafaelgb.github.io/obsidian-db-folder/features/Properties/ "Relation and Rollup unique in ecosystem").
- Full inline editing. React-based Notion-style UI. Data sourced from folders, links, tags, or Dataview queries. Depends on Dataview plugin. Supports both YAML frontmatter and Dataview inline fields storage [DB Folder GitHub](https://github.com/RafaelGB/obsidian-db-folder "Dataview as search engine; React UI").
- **Repository archived by owner July 28, 2025** (updated from Chapter 2's "stalled" — now confirmed archived). Last release v3.5.1 (January 19, 2024). 179 open issues, 1.4k stars [DB Folder GitHub](https://github.com/RafaelGB/obsidian-db-folder "Archived Jul 28, 2025").
- **Strengths**: Relation/Rollup support (unique); rich 14-type system; inline editing; multiple data sources. **Weaknesses**: Archived; table-only; Dataview dependency; 179 unresolved issues.

**3.4 DataLoom (⚠️ ARCHIVED March 2025, removed May 2025)**
- Supported **Table view only** — Board/Kanban/Calendar/Gallery were on roadmap but never shipped [DataLoom GitHub](https://github.com/decaf-dev/obsidian-dataloom "View types: Table").
- 12 cell types: Text, Number (with Currency), Checkbox, Embed, File, Date, Tag (single-select), Multi-tag, Last edited time, Creation time, Source, Source file. Custom `.loom` file format (not standard YAML frontmatter) [DataLoom GitHub](https://github.com/decaf-dev/obsidian-dataloom "12 cell types; .loom file format").
- Full inline editing, undo/redo, CSV/Markdown/PDF import/export, mobile support, embeddable. No formulas, relations, or rollups [DataLoom GitHub](https://github.com/decaf-dev/obsidian-dataloom "Features list").
- Developer cited Obsidian's native table editor (v1.5.0) and Bases direction as factors for archival [GitHub Issue #958](https://github.com/decaf-dev/obsidian-dataloom/issues/958 "DataLoom no longer maintained").
- **Strengths** (historical): Clean Notion-like UI; good import/export; mobile support; low barrier to entry. **Weaknesses**: Discontinued; `.loom` format lock-in; table-only; no formulas/relations/rollups.

**3.5 Projects (by Marcus Olsson) — ⚠️ ARCHIVED July 2025**
- **Only community plugin that offered 4 view types**: Table, Board (Kanban), Calendar, Gallery [Projects GitHub](https://github.com/marcusolsson/obsidian-projects "Four views: Table, Board, Calendar, Gallery").
- Reads YAML frontmatter; supports all Obsidian core property types including Date & time (v1.17.4). "Leave no trace" design — no plugin-specific frontmatter [Projects GitHub](https://github.com/marcusolsson/obsidian-projects "Leave no trace design").
- Table inline editing. Board view groups by property with drag-and-drop between columns. Calendar view by date property. Gallery with optional cover images. Data sources: folders and Dataview queries [Projects GitHub](https://github.com/marcusolsson/obsidian-projects "Inline editing, folder and Dataview query sources").
- No formulas, relations, or rollups. Configurable first day of week (v1.17.4). **Discontinued by original author May 2025; repository archived July 18, 2025** [Projects GitHub Issues](https://github.com/obsmd-projects/obsidian-projects/issues/1011 "Repository archived Jul 18, 2025"). Desktop-only (`isDesktopOnly: true`). Apache-2.0 license.
- A "Projects Plus" community fork was posted on the Obsidian forum in October 2025, but maturity and maintenance status are uncertain [Obsidian Forum](https://forum.obsidian.md/t/projects-plus-plugin/106826 "Community fork — October 2025").
- **Strengths** (historical): 4 views in one plugin; leave-no-trace; clean native UI. **Weaknesses**: Archived; no formulas/relations/rollups; desktop-only; fork maturity uncertain.

**3.6 Kanban Plugin (Stalled — seeking maintainers)**
- Single view: **Kanban/Board**. Markdown-backed: headings = lanes, list items = cards. Board settings in YAML frontmatter [Kanban GitHub](https://raw.githubusercontent.com/mgmeyers/obsidian-kanban/main/README.md "Markdown-backed Kanban boards").
- Cards can link to notes, create notes from cards, display dates/times/images. Drag-and-drop between lanes and within lanes. Archive feature for completed cards. Board search [Kanban Plugin Forum](https://forum.obsidian.md/t/kanban-plugin/17082 "Features: dates, images, note creation, archive").
- No WIP limits, swimlanes, label/tag system, or property display from linked notes on cards. Cards are a standalone data silo (don't read frontmatter from linked notes) [Kanban GitHub](https://raw.githubusercontent.com/mgmeyers/obsidian-kanban/main/README.md "No WIP limits or swimlanes").
- README states: "The Kanban plugin is looking for new maintainers." Last release v2.0.51 (~early 2024), ~2 years stalled. ~2.1M downloads. MIT [Kanban GitHub](https://raw.githubusercontent.com/mgmeyers/obsidian-kanban/main/README.md "Seeking new maintainers").
- **Strengths**: Pure Markdown backing; intuitive focused UX; massive user base; note linking. **Weaknesses**: Stalled/seeking maintainers; no advanced Kanban features; standalone data silo; single view type.

**3.7 Full Calendar (Effectively abandoned)**
- Calendar views: **day, week, month** (powered by FullCalendar library). Events as notes with frontmatter, or as list items in daily notes (Dataview inline fields). Supports timed, all-day, single, and recurring events [Full Calendar Docs](https://obsidian-community.github.io/obsidian-full-calendar/ "Day/week/month views; events as notes").
- **ICS integration** (read-only, auto-refresh every 5 min) for Google Calendar, Apple Calendar, etc. **CalDAV** (read-only, basic auth): Apple iCloud and Fastmail confirmed; Google Calendar NOT supported via CalDAV [Full Calendar ICS](https://obsidian-community.github.io/obsidian-full-calendar/calendars/ics/ "ICS read-only") [Full Calendar CalDAV](https://obsidian-community.github.io/obsidian-full-calendar/calendars/caldav/ "CalDAV: iCloud/Fastmail yes, Google no").
- Drag-and-drop rescheduling, click-and-drag creation, sidebar view. No table/list/board views [Full Calendar Events](https://obsidian-community.github.io/obsidian-full-calendar/events/types/ "Drag-and-drop, click-and-drag creation").
- Last release v0.10.7 (~mid 2023), 984 days stale. 5 commits in past year. MIT [Full Calendar Docs](https://obsidian-community.github.io/obsidian-full-calendar/ "Effectively abandoned").
- **Strengths**: Most feature-complete calendar in ecosystem; ICS/CalDAV; rich FullCalendar UI; events as notes. **Weaknesses**: Abandoned (~2.7 years no release); read-only remotes; Google CalDAV unsupported; single view type.

**3.8 Emerging Contenders**
- **Bases Kanban** (ewerx, December 2025): First Bases API Kanban view. Drag-and-drop cards between columns, column reordering, auto-update frontmatter. Uses Bases Group By for columns. Early-stage; empty columns disappear when no cards present [Bases Kanban GitHub](https://github.com/ewerx/obsidian-bases-kanban "First Bases API kanban view; December 2025").
- **DataCards** (Sophokles187): Transforms Dataview queries into card layouts including **kanban preset** with inline editing. Multiple presets (grid, portrait, square, compact, dense, kanban). Requires Dataview. GPL-3.0. Not yet in community plugin store (BRAT/manual install) [DataCards GitHub](https://github.com/Sophokles187/data-cards "Kanban preset, inline editing, card layouts from Dataview").
- **Obsidian Maps**: Official Bases API reference plugin for Map view (October 2025) [Obsidian Changelog v1.10.0](https://obsidian.md/changelog/2025-10-01-desktop-v1.10.0/ "Official Maps plugin").
- **Prisma Calendar**: Emerging calendar plugin (late 2025) with CalDAV sync (iCloud, Google, Nextcloud, Fastmail) and ICS import/export — potential Full Calendar successor [Obsidian Forum](https://forum.obsidian.md/t/prisma-calendar-a-feature-rich-fully-configurable-calendar-plugin-for-obsidian/108788 "CalDAV sync including Google; ICS import/export").
- **Big Calendar**: Community plugin displaying events from daily notes/tasks in calendar format [Obsidian Plugins Directory](https://obsidian.md/plugins?search=Calendar "Big Calendar").
- **TaskForge**: Third-party mobile app (not an Obsidian plugin) providing Kanban and Calendar views for Obsidian Tasks format vaults [TaskForge](https://taskforge.md/obsidian-tasks/ "Mobile Kanban/Calendar for Obsidian Tasks").
- No Bases Calendar view plugin exists yet as of April 2026. Calendar space is fragmented (Full Calendar stalled, Prisma emerging, Big Calendar as alternative).

### 可用图片
（无本地相关图片）

### 仍需补充
- Exact download counts for Projects and Full Calendar from community-plugin-stats.json.
- Prisma Calendar release status — whether it's in the community plugin directory or still in beta.
- Detailed performance benchmarks for Bases vs. Dataview with 1000+ notes (no systematic public tests found).
- Bases Kanban plugin acceptance status in Obsidian community plugin directory.
- Official Bases documentation on help.obsidian.md uses dynamic JS rendering; detailed formula function reference not independently verified from T1 beyond changelogs and got.md guide.

## Chapter 4：Comparative Analysis Across Plugins

### 研究目标
- Synthesize individual evaluations into structured, side-by-side comparison matrices using consistent dimensions: view-type coverage, property/field support depth, filtering/sorting power, inline editing UX, performance at scale, mobile compatibility, inter-plugin compatibility, development health, licensing/cost, learning curve.
- Identify which plugin comes closest to full Notion parity for each view type.
- Assess which plugins offer the best forward path in terms of development momentum and alignment with Obsidian's core roadmap (Bases).

### 关键发现
- **No single Obsidian plugin or stack replicates more than ~48% of Notion's full multi-view database feature set.** The Bases + Bases Kanban stack (~48%) is the closest active option; the archived DB Folder (~43%) would be second due to unique Relation/Rollup support [Obsidian Changelog v1.9.0](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/ "Bases introduced") [DB Folder Properties Docs](https://rafaelgb.github.io/obsidian-db-folder/features/Properties/ "Relation and Rollup property types").
- **Critical ecosystem update: Projects was also archived** (original developer discontinued May 2025; repository archived July 18, 2025), joining DB Folder (archived July 28, 2025) and DataLoom (archived March 9, 2025). The Kanban plugin is seeking new maintainers; Full Calendar has had no release in ~2.7 years. **Only Bases (core) and Dataview remain non-archived**, with Dataview in maintenance mode [Projects GitHub Issues](https://github.com/obsmd-projects/obsidian-projects/issues/1011 "Repository archived Jul 18, 2025").
- **Bases is the only actively developed database solution** in the ecosystem. The Bases API (`registerView()`) enables community view extensions — Bases Kanban (December 2025) and Maps (October 2025) are first examples, demonstrating a viable platform model [Obsidian Roadmap](https://obsidian.md/roadmap/ "Bases API for community view types").
- **DB Folder's unique Relation/Rollup support is now lost to archival.** No active plugin offers explicit Relation/Rollup properties; Bases approximates via link properties + `reduce()` formulas + `file.hasLink()`/`file.linksTo()` filters, but this requires manual formula construction [DB Folder Properties Docs](https://rafaelgb.github.io/obsidian-db-folder/features/Properties/ "Relation and Rollup").
- **Performance diverges**: Bases is "incredibly fast" (native core integration) vs. Dataview (plugin-level index, adds 1–2 seconds on mobile). Bases benefits from native integration with Obsidian's core indexing engine [Obsidian Rocks](https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/ "Bases faster than Datacore; no coding required") [Dataview Docs](https://blacksmithgu.github.io/obsidian-dataview/ "Scales to hundreds of thousands of notes").
- **Mobile**: Bases works on mobile (core plugin). Dataview works but adds load overhead. Projects was desktop-only (`isDesktopOnly: true`). Kanban has reported breakage after mobile v1.11.5 [Obsidian Forum](https://forum.obsidian.md/t/bases-support-export-to-csv-on-mobile/104278 "Bases on Android mobile") [Obsidian Forum](https://forum.obsidian.md/t/projects-plugin-for-ios/47334 "Projects desktop-only").
- **Entire Obsidian stack is free.** Obsidian is free for all use including commercial (since February 2025). Bases is a bundled core plugin requiring no Sync/Publish. All community plugins use MIT or Apache-2.0. This contrasts with Notion where automations, AI formula assist, unlimited charts, and conditional form logic require $10+/user/month paid plans [Obsidian Blog](https://obsidian.md/blog/free-for-work/ "Free for commercial use") [Obsidian Pricing](https://obsidian.md/pricing "Sync/Publish are optional add-ons").
- **GUI vs. code divide**: Bases, DB Folder, DataLoom, Projects provided visual GUI configurators; Dataview requires writing DQL/JavaScript with no visual builder. Bases' visual editor is a key advantage ("no coding required") [Obsidian Rocks](https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/ "Bases: no coding, visual editor").
- **View-Type Coverage Matrix**: No single plugin covers all 4 primary Notion views. Combined Bases + Bases Kanban stack covers 5 functional types (Table, Cards, List, Map, Kanban) — broadest active coverage. Notion's Timeline, Chart, and Form views have no equivalent in any Obsidian plugin.
- **Advanced Feature Comparison**: Largest gaps vs. Notion are in (1) Relations/Rollups (only archived DB Folder had explicit support), (2) Automations (no Obsidian plugin provides trigger-action automation), (3) Conditional color (no Obsidian plugin supports it).
- **Multi-Plugin Stack Analysis**: Stack A (Bases + Bases Kanban) has seamless integration — both operate on the same `.base` file and YAML frontmatter; editing in any view writes back to frontmatter. Stack B (Dataview + Kanban + Full Calendar) operates as **isolated data silos** with no bidirectional sync. Stack C (Projects, archived) had 4 integrated views. Stack D (DB Folder, archived) had the closest Notion data model but table-only view.
- **10 features that remain impossible in Obsidian as of April 2026**: database automations, conditional color, Timeline/Gantt view, Chart view, Form view, real-time multi-user collaboration, sub-grouping, native two-way relations, declarative rollups, AI-assisted formula creation.
- A "Projects Plus" community fork was posted on the Obsidian forum in October 2025, but its maturity and maintenance status are uncertain [Obsidian Forum: Projects Plus](https://forum.obsidian.md/t/projects-plus-plugin/106826 "Community fork — October 2025").
- **Notion Parity Scores** (12-dimension weighted): Bases + Bases Kanban ~48%, DB Folder ~43%, Dataview + Kanban + Full Calendar ~35%, Projects ~30%.

### 可用图片
（无本地相关图片；Chapter 4 matrices are text tables suitable for inline rendering）

### 仍需补充
- Exact download counts for Projects and Full Calendar (not extracted from community-plugin-stats.json but do not change analytical conclusions).
- Whether "Projects Plus" fork has been accepted into community plugin directory or remains BRAT-only.
- Systematic performance benchmarks (Bases vs. Dataview, 100/1,000/10,000 notes) — current data is community anecdotes (T3/T4), not controlled testing.
- Whether any Bases Calendar plugin is in development (feature request is among most upvoted on Obsidian forum but no confirmed plugin announced).
- Prisma Calendar release status (community plugin directory or still beta).

## Chapter 5：Practical Recommendations and Workflow Blueprints

### 研究目标
- Translate analytical findings into actionable guidance for three user profiles: power user (needs full multi-view databases with relations/formulas), casual user (simple table + kanban), team/collaborative user.
- Provide concrete plugin-stack recommendations and example workflow configurations for each profile.
- Address migration workflow from Notion databases to Obsidian vault.
- Offer a forward-looking recommendation given the Bases roadmap trajectory — invest in community plugins now or wait for core maturity?

### 关键发现

**Migration Infrastructure**
- The **Obsidian Importer** (official community plugin, ~1,118,000 downloads, v1.8.4 as of February 2026) supports two methods for Notion import: (1) **API import** (introduced v1.8.0, November 2025) using Notion API with integration token, which converts databases to `.base` files with formula conversion; and (2) **file-based import** (legacy) using HTML/Markdown export [Obsidian Importer GitHub Releases](https://github.com/obsidianmd/obsidian-importer/releases "v1.8.0: Notion API importer with Databases to Bases conversion").
- Obsidian posted a **$5,000 bounty** for the Notion API importer feature, fulfilled by contributor @Xheldon in v1.8.0 [Obsidian LinkedIn](https://www.linkedin.com/posts/obsidianmd_a-new-bounty-is-open-for-obsidian-importer-activity-7373768184228798464-cp90 "$5,000 bounty for Notion Databases to Bases conversion").
- **Data preserved (API import)**: page content (Markdown), properties (YAML frontmatter), database structure (`.base` files), formulas (converted to Bases syntax), timestamps (v1.8.3+), attachments, folder hierarchy. **Data lost**: Relations (plain text URLs, not re-establishable), Rollups, view configurations (partial), automations, comments, version history, conditional color [Obsidian Importer GitHub Releases](https://github.com/obsidianmd/obsidian-importer/releases "v1.8.3: Set and preserve ctime/mtime").
- Real-world migration account: Alberto Gregorio (April 2025) confirmed import is a "10-minute task" for a sizable PKB; friction points include Notion internal links becoming standard Markdown links and cryptic image filenames [Alberto Gregorio blog](https://albertogregorio.com/2025/04/01/obsidian-importer/ "10-minute import task"). Dave Rupert (May 2025), 7+ year Notion user, documented a month-long full migration, citing Notion's price hike from $8 to $12/month (+50%) as tipping point [Dave Rupert](https://daverupert.com/2025/05/notion-to-obsidian/ "Month-long migration; Notion price hike trigger").

**Critical Discovery: Calendar Bases Plugin**
- A **Calendar Bases** community plugin (by Edrick Leong) already exists with **~45,000 downloads**, adding calendar layout to Bases with drag-and-drop rescheduling, start/end dates, and direct note opening [Obsidian Plugins Directory](https://obsidian.md/plugins "Calendar Bases: 45,268 downloads"). This significantly improves the Bases stack's view coverage.
- Practical PKM (March 2026) built a master content calendar using Bases + Calendar Bases, combining notes from multiple folders into one calendar view — functionality the author noted was not achievable in Notion with multiple databases [Practical PKM](https://practicalpkm.com/building-a-content-calendar-in-obsidian-bases/ "Content calendar surpassing Notion's multi-database limitations").

**User Profile Recommendations**
- **Power User**: Recommended stack is **Bases + Bases Kanban + Calendar Bases**, providing 6 functional view types (Table, Cards, List, Map, Kanban, Calendar). Key trade-offs: no explicit Relations/Rollups (approximated via link properties + formulas), no automations, no conditional color. 10 Notion workflows that cannot be replicated enumerated (two-way Relations with Rollups, automations, Timeline/Gantt, Chart, Form, sub-grouping, AI formula creation, conditional color, real-time collaboration, linked database views with independent sources).
- **Casual User**: Recommended minimal stack is **Bases + Bases Kanban** — zero-code, GUI-driven, lowest learning curve. Bases handles table/cards with inline editing; Bases Kanban adds drag-and-drop kanban. Dataview explicitly not recommended for casual users due to code-only interface and read-only output [Obsidian Bases Guide](https://got.md/obsidian-bases/ "No coding required — visual editor").
- **Team/Collaborative User**: Options tiered by need — (1) Relay (real-time CRDT, live cursors, 10K+ users, free for 3 users or $5-18/user/month) is closest to Notion collaboration; (2) Obsidian Sync (async, up to 20 users, $4-8/user/month); (3) Obsidian Git (developer-focused, unreliable on mobile); (4) LiveSync (personal sync only, not multi-user). Critical limitations vs. Notion: no per-database permissions, no @mentions in database context, no inline commenting on rows, no workspace roles [Relay.md](https://relay.md/ "10,000 users; CRDT-based real-time collaboration") [Obsidian Sync](https://obsidian.md/sync "Up to 20 collaborators").

**Bases Roadmap & Forward-Looking Assessment**
- Official Obsidian Roadmap lists **Calendar view for Bases** and **Kanban view for Bases** as "Planned," confirming these will eventually become native features [Obsidian Roadmap](https://obsidian.md/roadmap/ "Planned: Calendar view, Kanban view for Bases").
- Based on ~4-5 month development cadence, native Calendar + Kanban views could arrive H2 2026, bringing active Bases stack to ~55-60% Notion parity. Relations/Rollups (not on roadmap) would push to ~65-70%. 80%+ parity (requiring Relations, Rollups, Automations, Timeline/Chart) is 2027+ at earliest.
- Recommendation: invest in Bases now for new workflows; maintain existing Dataview queries in parallel (both can coexist). No formal Dataview deprecation announced but trajectory clear — Bases is the officially backed solution [Obsidian Roadmap](https://obsidian.md/roadmap/ "Bases API, more views planned").

### 可用图片
（无本地相关图片）

### 仍需补充
- Detailed testing of Notion API import (v1.8.x) with complex workspace containing related databases — to verify `.base` conversion quality and formula conversion gaps.
- Calendar Bases plugin details: all-day events, multi-day spans, click-to-create UX.
- Relay's interaction with Bases — whether real-time collaboration works on `.base` files or frontmatter properties feeding Base views.
- Larger sample of Notion-to-Obsidian migration pain points beyond two documented accounts.
- Official Obsidian team commentary on Dataview's future vs. Bases.

# Section 2：给 Write 阶段的执行建议

- **Terminology**: Standardize on "property" (not "field" or "column"), "entry" (cross-platform generic; use "note" or "page" only when platform-specific), "Kanban view" (after first-mention bridge "Kanban/Board view"), "database" (defined precisely in Ch1/Ch2 then used loosely thereafter).
- **Cross-referencing**: Ch1 defines the benchmark feature list; Ch3 and Ch4 must explicitly reference it when scoring plugins. Consider a "Notion-parity score" introduced in Ch1, reused in Ch3–4. Ch3 sub-sections use a common template (Supported Views → Property Handling → Advanced Features → UX & Performance → Development Status → Strengths → Weaknesses) so Ch4 tables can be derived directly. Ch5 recommendations trace back to Ch4 tables.
- **Comparison dimensions** (10): view-type coverage, property/field type support, interaction quality, filtering & sorting, performance at scale, mobile compatibility, inter-plugin compatibility, development health, licensing & cost, learning curve.
- **Critical ecosystem update**: All major community database plugins except Dataview (maintenance mode) are now archived or stalled — DB Folder (archived Jul 2025), DataLoom (archived Mar 2025), Projects (archived Jul 2025), Kanban (stalled, seeking maintainers), Full Calendar (abandoned ~2.7yr). This must be stated clearly in the executive summary and throughout. Do not present archived plugins as current options for new users.
- **Calendar Bases discovery**: Chapter 5 research uncovered a **Calendar Bases** plugin (~45K downloads) not identified in Chapter 3. The write stage should integrate this into Chapter 3's emerging contenders section (3.8) and update Chapter 4's matrices to include it in the Bases stack analysis, raising the effective view count to 6 (Table, Cards, List, Map, Kanban, Calendar).
- **Notion Importer**: The official Obsidian Importer now supports API-based Notion import (v1.8.0+) converting databases to `.base` files with formula conversion. This should be highlighted in Ch5 and briefly mentioned in Ch2 when discussing migration context.
- **Structural risks**: (1) Bases core plugin is still evolving — timestamp all Bases claims, flag as subject to change; (2) Plugin stacks must be treated as first-class options alongside monolithic solutions; (3) All community database plugins except Dataview are archived/stalled — this is the central ecosystem fact; (4) Ground UX claims in observable interactions (click counts, GUI configurators, drag-and-drop), not aesthetic judgments; (5) Do not declare Dataview "dead" or "replaced by Bases" — present complementary roles and note both can coexist.
- **Language**: English, formal research-report register, "we" for analytical judgments, quantify where possible (e.g., "supports 8 of 11 Notion property types").
- **Each chapter**: Open with orienting paragraph, close with key-takeaway summary.
- **Time scope**: April 2025 – October 2026 (past 12 months + 6-month outlook from current date 2026-04-03).
- **Parity scoring**: Chapter 4 establishes a 12-dimension weighted Notion Parity Score methodology. Present consistently and make methodology transparent. Key scores: Bases + Bases Kanban + Calendar Bases ~48-52% (updated with Calendar), DB Folder ~43%, Dataview + Kanban + Full Calendar ~35%, Projects ~30%.
- **Forward-looking claims**: All roadmap projections (H2 2026 for native Calendar/Kanban, 2027+ for 80%+ parity) should be clearly labeled as estimates based on observed development cadence, not official commitments.
