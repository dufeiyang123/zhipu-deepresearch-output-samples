# Section 1：章节研究计划

## Chapter 1：Application Context — Why Hollow Shafts in NEV Electric Drive Units
### 研究目标
- What is the role of the motor shaft within an integrated NEV electric drive unit (power path, torque/speed envelope, packaging)?
- What are the functional drivers for adopting a hollow design (weight reduction, oil-cooling channels, wiring/sensor routing, NVH)?
- What are the critical performance requirements (fatigue life, tolerances, surface integrity, residual stress, material grades)?
- Synthesize a concise "requirement checklist" (geometry envelope, tolerances, material grade, production volume range, cost target class) to serve as the evaluation benchmark for Chapters 3–4.

### 关键发现

**A. Power Transmission Path & Architecture**
- In a modern NEV integrated electric drive unit (EDU), the rotor shaft is the sole mechanical link converting electromagnetic torque into drivetrain motion. The power path runs: stator/rotor → rotor shaft → single-speed or two-stage reduction gearbox (via spline/gear interface) → differential → half-shafts → wheels [thyssenkrupp Dynamic Components](https://www.thyssenkrupp.com/en/stories/automotive-and-new-mobility/the-perfect-rotor-shaft "The perfect rotor shaft").
- EDUs are typically "3-in-1" packages (motor + inverter + single-speed reducer). Common architectures: coaxial (longer through-shaft), offset (shorter shaft, offset gear loads), offset-coaxial [Punch Powertrain](https://punchpowertrain.com/products/integrated-edrive-unit/ "Integrated eDrive"); [GM Ultium EDU](https://news.gm.com/home.detail.html/Pages/topic/us/en/2025/dec/1218-Plugged-in-EV-drive-units-work.html "How EV drive units work").

**B. Torque/Speed Envelopes**
- BorgWarner production PMSM portfolio: 100–650 Nm peak torque, 14,000–18,000 rpm max, 45–500 kW, 96–800 V platforms [BorgWarner](https://www.borgwarner.com/technologies/electric-drive-motors "Electric Drive Motors").
- Tesla Model S Plaid: 20,000 rpm with carbon-fiber-sleeved IPM rotors, combined 760 kW and 1,420 Nm system torque [MotorTrend](https://www.motortrend.com/reviews/2022-tesla-model-s-plaid-first-test-review "Model S Plaid test").
- Xiaomi HyperEngine V8s (2025): 27,200 rpm, 431 kW, 635 Nm per motor, 98.11% peak efficiency, 10.14 kW/kg [Xiaomi Global](https://www.mi.com/global/discover/article?id=3768 "SU7 Ultra specs").
- BYD (March 2025): 30,511 rpm, 580 kW per module, dynamic balance precision within 50 mg (vs. industry standard 100 mg) [CarNewsChina](https://carnewschina.com/2025/03/20/byd-releases-ground-breaking-30511-rpm-motor/ "BYD 30,511 rpm motor").
- GAC Quark Electric Drive 2.0 (August 2024): 30,000 rpm, 13 kW/kg motor power density, 98.5% peak efficiency [InsideEVs](https://insideevs.com/news/731663/gac-new-advanced-electric-motor/ "GAC advanced motor").
- IDTechEx (Dec 2025): average EV motor at 10,000–15,000 rpm, frontier at 20,000–30,000+ rpm. Increasing from 10k to 20k rpm yields 69% power density gain; 20k to 30k rpm adds 41%. Over 140 million EV motors required globally by 2036 [IDTechEx](https://www.idtechex.com/en/research-article/the-need-for-speed-ev-motors-breaking-the-30-000rpm-barrier/34219 "EV Motors Breaking 30,000rpm").

**C. Functional Drivers for Hollow Design**
- Three primary drivers: (a) weight reduction via material-efficient design, (b) oil-cooling through coolant injection into hollow bore using centrifugal force, (c) assembled multi-material construction (higher-alloy steel at gearing end, lower-alloy for tube section) [thyssenkrupp](https://www.thyssenkrupp.com/en/stories/automotive-and-new-mobility/the-perfect-rotor-shaft "The perfect rotor shaft").
- Hollow shaft enables production lines with 11 short operations in 47-second total cycle time (soft turning, laser welding, induction hardening, finish turning, grinding) [EMAG](https://www.emag.com/industries-solutions/workpieces/assembled-rotor-shaft-electric-motor/ "Assembled Rotor Shaft — EMAG").
- Typical hollow shaft: ~50 mm OD, 5–10 mm wall thickness, up to 30% weight reduction vs. solid equivalent [KeSu Group](https://kesugroup.com/motor-shaft-guide/ "Motor Shaft Guide").
- Hollow shafts (ID = 60% of OD) demonstrate 18.7% better strength-to-mass ratio in torsion vs. solid shafts; solid shafts show 12.4% higher bending deflection resistance [Sujita & Sutanto, IJEI 2025](http://www.ijeijournal.com/papers/Vol14-Issue8/14086265.pdf "Solid vs. Hollow Shaft Performance").

**D. Oil Cooling Through Hollow Shaft**
- Porsche US Patent 9,148,041 B2: hollow rotor shaft with stationary cooling lance, eliminating rotating seals [Porsche Patent](https://patents.google.com/patent/US9148041B2/en "Cooled rotor shaft — Porsche").
- BMW Patent DE102015214309A1: hollow shaft cooling system for EV drives [BMW Patent](https://patents.google.com/patent/DE102015214309A1/en "Hollow shaft cooling — BMW").
- EP 4145683 (2023): hollow shaft with integrated cooling ducts and radial openings for simultaneous rotor/stator/winding cooling [EP4145683](https://data.epo.org/publication-server/rest/v1.2/publication-dates/20231122/patents/EP4145683NWB1/document.pdf "Hollow shaft for rotor — EPO").
- Novel tooth-guided liquid-cooling shaft (2025, 20MnCr5): 110% higher cooling efficiency at low RPM vs. conventional hollow shaft; shaft dimensions 340–359 mm length, 11 mm inlet bore, 52–98 mm OD [Goetz et al., arXiv 2510.22029](https://arxiv.org/html/2510.22029v1 "Ducted Liquid Cooling in Cold-Formed Motor Shaft").
- Hollow-shaft rotor cooling is established in production (Tesla, Audi Q8 e-tron induction machines) and being adopted for PMSM where rotor eddy-current losses heat rare-earth magnets at high speed [Goetz et al., arXiv 2510.22029](https://arxiv.org/html/2510.22029v1 "Adoption status").

**E. Material Grades**
- 20MnCr5 (DIN 1.7147): case-hardening steel, density 7,850 kg/m³, thermal conductivity 45.9 W/(m·K), preferred for cold-forming processes [Goetz et al., arXiv 2510.22029](https://arxiv.org/html/2510.22029v1 "20MnCr5 properties").
- AISI 4140 / 42CrMo4 (DIN 1.7225): tensile strength 800–1,000 MPa, de facto standard for high-torque EV motor shafts [Ovako](https://steelnavigator.ovako.com/steel-grades/42crmo4/ "42CrMo4"); [AmTech OEM](https://www.amtechinternational.com/project/ev-motor-shaft/ "EV Motor Shaft case study").
- S45C (JIS) / AISI 1045: medium carbon steel for lower-cost, moderate-load applications [KeSu Group](https://kesugroup.com/motor-shaft-guide/ "Material comparison").

**F. Tolerances & Surface Integrity**
- CNC machining achieves ±0.01 mm for critical diameters; Ra 0.4–0.8 µm for bearing seats/seal surfaces after grinding; hardness 20–40 HRC (through-hardened) or 58–62 HRC (induction-hardened bearing seats); dynamic balancing to ISO 1940 G2.5 or better for motors >3,000 rpm [KeSu Group](https://kesugroup.com/motor-shaft-guide/ "Tolerances and surface finish").
- BYD 30,511 rpm motor: 50 mg balance precision vs. 100 mg industry standard [CarNewsChina](https://carnewschina.com/2025/03/20/byd-releases-ground-breaking-30511-rpm-motor/ "Balance precision").
- At 25,000+ rpm, concentricity of splined gearing is top priority; rotor shaft torques are 3–5× greater than conventional camshafts [thyssenkrupp](https://www.thyssenkrupp.com/en/stories/automotive-and-new-mobility/the-perfect-rotor-shaft "Tolerance requirements").
- Production case: AmTech EV motor shaft — OD 64 mm, length 305 mm, tolerance ±0.076 mm (~IT8–IT9); processes: gun drilling, hobbing, shaping, milling, grinding, heat treating [AmTech OEM](https://www.amtechinternational.com/project/ev-motor-shaft/ "Production specifications").

**G. Geometry Envelope**
- Representative: OD 40–100 mm (most common 50–70 mm); bore diameter 10–30 mm (oil cooling) or up to 60% of OD (structural); wall thickness 5–15 mm; length 250–400 mm. Features: splined output, 2–3 bearing seats, lamination stack mounting surfaces [synthesized from AmTech, arXiv, KeSu, thyssenkrupp sources].

**H. Production Volumes**
- Global EV sales exceeded 17.8 million in 2024 (~20% of all new cars); each EV requires 1–3 motor/shaft assemblies; IDTechEx forecasts 140M+ EV motors/year by 2036 [EV-Volumes](https://ev-volumes.com/ "Global EV sales 2024"); [IDTechEx](https://www.idtechex.com/en/research-article/the-need-for-speed-ev-motors-breaking-the-30-000rpm-barrier/34219 "140M motors by 2036").
- BYD alone: 3.28 million NEV units in first 10 months of 2024, implying shaft volumes >3M/year for a single OEM [PR Newswire](https://www.prnewswire.com/news-releases/global-times-the-power-of-planning-chinese-nevs-rewrite-the-global-automotive-landscape-302702112.html "BYD 2024 production data").

**I. Rotor Dynamics & NVH**
- At 20,000–30,000+ rpm: centrifugal force on rotor structure, bearing stress, and rotor imbalance become dominant constraints. Solutions: smaller rotor diameters, carbon-fiber wrapping, ceramic hybrid bearings, direct oil cooling [IDTechEx](https://www.idtechex.com/en/research-article/the-need-for-speed-ev-motors-breaking-the-30-000rpm-barrier/34219 "High-speed challenges").
- Without combustion engine masking noise, NVH requirements in EVs tightened further, imposing stricter concentricity and balance quality demands on rotor shafts [thyssenkrupp](https://www.thyssenkrupp.com/en/stories/automotive-and-new-mobility/the-perfect-rotor-shaft "NVH requirements").

### 可用图片
（无相关本地图片素材）

### 仍需补充
- Quantified rotational inertia reduction percentage for specific OD/ID ratios — derivable analytically (J_hollow/J_solid = 1 - (d/D)^4) but needs a cited automotive engineering T1/T2 reference for the EV shaft context.
- Precise IT-grade tolerance specifications from OEM or standards bodies (IT5–IT6 for bearing seats, TIR for concentricity in µm) — AmTech data gives ~IT8–IT9 for OD, but bearing seat and bore tolerances at IT5–IT6 level need T1 confirmation.
- Bore surface roughness (Ra) requirements specifically for oil-cooling passages (likely Ra 1.6–3.2 µm vs. Ra 0.4–0.8 µm for bearing seats) — no T1/T2 source found.
- Fatigue life specifications (e.g., 10^7 cycles at X% of yield) specific to NEV rotor shafts — no T1/T2 data.
- Residual stress targets post-heat-treatment/grinding (e.g., compressive stress at surface) — not available from T1/T2.
- Per-unit cost target class for NEV motor shafts — no T1/T2 data (industry estimates suggest $15–$50 per shaft).


## Chapter 2：Taxonomy and Process Descriptions of Hollow Shaft Forming Technologies
### 研究目标
- Provide an exhaustive catalogue of every industrially relevant and credibly emerging technique for producing hollow shafts.
- Group processes into families: subtractive, bulk forming, incremental/tube forming, joining-based, and emerging/non-conventional.
- Describe mechanism, equipment, typical parameters, achievable geometries, and grain flow effects for each process — without evaluative judgment.

### 关键发现

**A. Subtractive / Material-Removal Processes**

- **Gun drilling**: Single-flute tool with internal coolant/external chip evacuation; effective in diameters 1–50 mm, L/D ratios commonly 100:1 (up to 400:1 on extreme setups); L/D > 20:1 generally requires dedicated gun-drilling equipment. Confirmed in production for EV motor shaft bores (AmTech: 64 mm OD, 305 mm long, AISI 4140) [UNISIG](https://unisig.com/information-and-resources/what-is-deep-hole-drilling/what-is-gun-drilling/ "Gun Drilling — UNISIG"); [AmTech OEM](https://www.amtechinternational.com/project/ev-motor-shaft/ "EV Motor Shaft — AmTech").
- **BTA/STS drilling**: Specialized drill head on long drill tube; external coolant/internal chip evacuation (reverse of gun drilling); effective 20–200 mm diameter; feed rates 5–7× faster than gun drilling at equivalent diameters [UNISIG](https://unisig.com/information-and-resources/what-is-deep-hole-drilling/what-is-bta-drilling/ "BTA Drilling — UNISIG").
- **Trepanning**: Removes annular ring, leaving a reclaimable solid core — significant material recovery for expensive alloys; diameters up to 300–630 mm, depths to 10,000–20,000 mm [UNISIG](https://unisig.com/information-and-resources/deep-hole-processes/trepanning/ "Trepanning — UNISIG").
- **Boring and honing**: Conventional reference process — solid billet bored on lathe/boring mill, then honed; achievable bore Ra 0.4–1.6 µm, bore straightness ≤ 0.05 mm/100 mm; fully mature but inherently material-wasteful.

**B. Bulk Metal Forming Processes**

- **Radial forging (GFM/SMS)**: Four radially oscillating hammers; cold/warm/hot regimes; with mandrels, produces net-shape inner contours and near-net-shape outer contours; hollow shafts closed on one/both sides are possible; internal splines feasible. GFM explicitly targets EV rotor shafts at semihot 700–850°C: "hollow & bottle-shaped contour... produced quite easily by radial forging." Over 200 GFM machines installed in automotive industry; >10 million driveshafts/year produced by GFM radial forging. "Distinctively higher fatigue strength" than machining-only [GFM](https://www.gfm.at/products/radial-forging-automotive/?lang=en "Radial Forging Automotive — GFM").
- **SMS SMX hydraulic radial forging**: Four hydraulic cylinders, up to 300 strokes/min; tube forging with third manipulator holding mandrel bar; eccentricity reduction from ±15 mm to max ±2.6 mm demonstrated; ComForge® software for microstructure optimization (closure of casting pores/voids) [SMS group](https://www.sms-group.com/plants/radial-forging-machines "SMX Radial Forging — SMS group").
- **Rotary swaging (Felss)**: Multiple die segments oscillate radially at >1,000 strokes/min; incremental forming of 0.25–1.5 mm per stroke; cold-forming with/without mandrel for internal splines/tapers; fatigue strength increase up to 30%, weight reduction up to 50% vs. machined; in series production for automotive components [Felss](https://felss.com/en/technologies/rotary-swaging/ "Rotary Swaging — Felss").
- **Hot extrusion**: Ugine-Sejournet process, 1,000–1,300°C for steel, glass lubricant; mandrel for hollow bore; extrusion ratios up to 100:1; exit speeds 1–2 m/s; economically viable only for alloy steels or small lot sizes where rolling/welded tube is impractical [IspatGuru](https://www.ispatguru.com/hot-extrusion-process-and-its-application-for-steel/ "Hot Extrusion — IspatGuru").
- **Cross-wedge rolling (CWR)**: Han et al. (2024, Chinese Academy of Sciences) FEM simulation of CWR for hollow motor shafts using 45 steel at 1,000°C, 300 mm/s; OD deviation < 0.8%; avoids central defects of solid-billet CWR. Remains at simulation stage. Fraunhofer has published on modified CWR for hollow shafts; Lublin Univ. of Technology studied CWR for Ti6Al4V and steels [Han et al., Metal Forming 2024](https://www.researchgate.net/publication/384053671_Design_and_simulation_of_cross_wedge_rolling_process_for_hollow_motor_shaft "CWR for hollow motor shaft"); [Fraunhofer](https://publica.fraunhofer.de/entities/publication/def1f3c2-1974-490d-9eef-1dee3c0a377e "Modified CWR for hollow shafts").
- **Skew rolling / Mannesmann**: Foundational seamless tube piercing process; two barrel-shaped rolls inclined 3–12°; piercing temperature 1,100–1,250°C for steel; industrial standard for seamless tube mother tubes (typically >50 mm OD).
- **Mandrel forging / upset forging with piercing**: Forging over internal mandrel for thick-walled tubes; upset forging + punching as preforming step before extrusion or ring rolling; SMS SMX machines configured for mandrel-assisted tube forging [SMS group](https://www.sms-group.com/plants/radial-forging-machines "SMX tube forging with mandrel").

**C. Incremental & Sheet/Tube Forming Processes**

- **Flow forming (Leifeld)**: Three or more rotating rollers on mandrel; forward and backward stretching variants; wall-thickness reductions up to 90%; can produce internal teeth/gears; enhanced material properties via work hardening. GFM uses flow-formed blanks as input for radial forging of hollow gear shafts [Leifeld](https://leifeldms.com/en/flow-forming.html "Flow Forming — Leifeld"); [GFM](https://www.gfm.at/products/radial-forging-automotive/?lang=en "Flow-formed blanks for gear shaft radial forging").
- **Tube hydroforming**: Internal hydraulic pressure 50–400 MPa + axial feeding; produces complex hollow shapes with variable cross-sections; well-established for automotive structural parts; less common for rotational powertrain shafts due to limited wall thickness control.
- **Cold drawing over mandrel**: Tube pulled through die over mandrel; achieves IT8–IT10 tolerances, Ra 0.4–1.6 µm, 20–40% cross-section reduction per pass; mandrel drawing gives better wall thickness uniformity than hollow sinking [The Fabricator](https://www.thefabricator.com/tubepipejournal/article/tubepipeproduction/cold-drawing-principles "Cold Drawing Principles").
- **Cold pilgering (SMS Meer)**: Oscillating ring dies + tapered mandrel; cross-section reductions >90% in single pass; wall thickness variations <0.5 µm at medium ODs; Ra <0.5 nm for stainless steel; suitable for all metals, virtually no material loss [The Fabricator / SMS Meer](https://www.thefabricator.com/tubepipejournal/article/tubepipeproduction/introducing-cold-pilger-mill-technology "Cold Pilger Mill Technology").

**D. Joining-Based and Hybrid Approaches**

- **Rotary friction welding (KUKA/Thompson)**: >1,200 machines installed in 44+ countries; full-section solid-state joint with narrow HAZ; can join dissimilar metals — enabling high-alloy steel at spline/gear ends with lower-alloy tube section; used in automotive for assembled shafts, piston rods, valves [KUKA](https://www.kuka.com/en-us/products/production-machines/rotary-friction-welding-machines "Rotary Friction Welding — KUKA").
- **Laser welding — assembled rotor shafts (EMAG)**: ELC 6 machine for high-volume production; rotary indexing table; up to 500,000 rotor shafts/year; 11 operations in 47-second total cycle time (soft turning, laser cleaning, laser welding, induction hardening, finish turning, grinding). "All leading automotive manufacturers have the associated systems in use." Dominant series-production solution for assembled rotor shafts [EMAG LaserTec](https://www.engineering.com/manufacturing-rotor-shafts-at-the-speed-of-light-with-laser-welding/ "EMAG rotor shaft laser welding"); [EMAG](https://www.emag.com/company/news-media/press/single-view/article/elc-6-from-emag-lasertec-perfecting-the-welding-process-for-rotor-shafts/ "ELC 6 — EMAG").
- **Linear friction welding / FSW / EBW**: LFW for non-axisymmetric joints (primarily aerospace); FSW for aluminum, limited for steel shafts due to tool wear; EBW for deep narrow welds (20:1 aspect ratio) in vacuum — used for turbocharger shafts but higher cost/cycle time than laser welding [EB Industries](https://ebindustries.com/welding-specifications-for-electron-beam-welding/ "EBW specs").
- **Shrink-fit / interference-fit**: Thermal clearance assembly; no metallurgical bond; used for rotor lamination stack mounting and multi-material shaft designs; joint integrity depends on interference pressure and friction coefficient.

**E. Non-Conventional / Emerging Processes**

- **Centrifugal casting (Spuncast)**: Molten metal in spinning mold (250–1,500 rpm); OD up to 1,092 mm, lengths to 7,620 mm; impurities driven inward; coarser than wrought microstructure; better suited for large-diameter thick-walled parts than precision EV motor shafts [Spuncast](https://spuncast.com/capabilities/centrifugal-casting/ "Centrifugal Casting — Spuncast").
- **Additive manufacturing (WAAM/L-PBF)**: WAAM: 1–10 kg/h deposition, large-scale components; BMW Group has adopted WAAM for vehicle components/tools. L-PBF: complex internal cooling channels possible but limited by build volume (<500 mm), slow rates, high cost. Neither technology currently viable for series production of motor shafts at >1,000/year [Metal AM / BMW](https://www.metal-am.com/bmw-group-looks-to-wire-arc-additive-manufacturing-for-lightweight-and-sustainable-vehicle-components/ "BMW WAAM").
- **Electromagnetic forming**: Pulsed Lorentz forces expand/compress tubes at 100–300 m/s at room temperature in microseconds; primarily for aluminum/copper due to conductivity requirements; limited applicability to high-strength steel shafts [Belgian Welding Institute](https://bil-ibs.be/en/project/magpuls-electromagnetic-pulse-forming "MAGPULS — EM forming").
- **Rotary compression**: Three radially arranged rolls for hollow parts; studied by Lublin Univ. of Technology; primarily academic research stage [Pater et al., JMRT 2020](https://www.researchgate.net/publication/384053671_Design_and_simulation_of_cross_wedge_rolling_process_for_hollow_motor_shaft "Rotary compression — Pater et al.").

### 可用图片
（无相关本地图片素材）

### 仍需补充
- Radial forging quantitative parameters: specific forging forces (kN), achievable IT grades, Ra values for EV rotor shaft geometries — customer-specific data not publicly disclosed by GFM/SMS.
- Flow forming machine specifications for shaft-sized tubes (50–100 mm OD, 250–400 mm length) — Leifeld data focuses on larger wheels/cylinders.
- CWR experimental validation: Han et al. (2024) is simulation-only; physical rolling trials for motor shaft geometry not yet published.
- Friction welding cycle time and per-weld cost for assembled automotive shafts — not publicly available from KUKA/Thompson.
- Mannesmann/skew rolling applicability for small-diameter motor shafts (50–100 mm OD) vs. role as tube preform supplier.
- Hydroforming for shaft geometries: limited documentation for high L/D, thick-walled, stepped shaft profiles.
- AM for automotive motor shafts: no published case study found; confirmed as developmental.
- Cold drawing/pilgering produce constant or tapered cross-sections; ability to produce multi-stepped motor shaft profiles without secondary machining is limited.


## Chapter 3：Multi-Criteria Technical Comparison
### 研究目标
- Define each evaluation axis precisely: material compatibility, dimensional accuracy, wall-thickness uniformity, surface integrity, grain structure enhancement, minimum wall thickness, maximum L/D ratio.
- Build a Geometry & Quality comparison matrix (rows = processes, columns = criteria).
- Build an Economics & Industrialisation comparison matrix: tooling cost, cycle time, material yield, capex class, volume bands, energy intensity.
- Map secondary processing requirements for each primary forming route: CNC machining allowances, heat treatment, surface finishing, NDE inspection.

### 关键发现

**Matrix 1: Geometry & Quality — Key Comparative Data**

- **GD (Gun drilling)**: Bore ∅1–50 mm, L/D up to 100:1 (400:1 extreme), bore tolerance ±0.008 mm, bore Ra 0.4–0.5 µm. Neutral grain structure (subtractive). No stepped/internal features. Confirmed in production for EV motor shafts [AMG](https://www.amgundrilling.com/technical-gundrilling-information.html "Gun drilling specifications"); [AmTech OEM](https://www.amtechinternational.com/project/ev-motor-shaft/ "EV Motor Shaft").
- **BTA**: Bore ∅20–200 mm (8–630 mm specialized), feed rates 5–7× faster than gun drilling; bore tolerance ±0.025–0.05 mm; Ra 0.4–1.6 µm [UNISIG](https://unisig.com/information-and-resources/what-is-deep-hole-drilling/what-is-bta-drilling/ "BTA Drilling — UNISIG").
- **RF (Radial forging)**: OD 30–150 mm (GFM automotive), net-shape inner contour, near-net-shape outer; cold-forged inner ∅ ±0.025 mm, OD ±0.1 mm, Ra 3.2–0.4 µm; improved grain structure with continuous grain flow and pore closure (ComForge®); compressive residual stress at surface; stepped/bottle-shaped and internal splines feasible [GFM](https://www.gfm.at/products/radial-forging-automotive/?lang=en "Radial Forging Automotive"); [SMS group](https://www.sms-group.com/plants/radial-forging-machines "SMX Radial Forging"); [CT Forge](https://www.creatorcomponents.com/news/what-is-radial-forging-technology.html "Radial forging tolerances").
- **RS (Rotary swaging)**: OD 3–120 mm; ID over mandrel IT7, OD by recess swaging IT8, infeed swaging IT9; Ra <0.1 µm (recess/mandrel swaging, comparable to grinding); fatigue strength +30%, weight reduction up to 50%; variable wall thickness, internal splines feasible; 22-second cycle for EV rotor shaft from tube 60×6.0 mm [Felss Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3043336/Tube-2026-Felss-Group-GmbH-Paper-tube2026.3043336-FZ2ApYTISNirA9GZOxe72g.pdf "Felss Tube 2026 paper").
- **FF (Flow forming)**: ID 6.35–584 mm, wall 0.20–38 mm, length to 12 m; standard tolerances: ID ±0.127 mm, wall ±0.127 mm, straightness 0.076 mm/m; wall reduction up to 90%; improved grain structure and work hardening (160 ksi UTS at 60% reduction); internal teeth/gears feasible via profiled mandrels; GFM uses flow-formed blanks as input for radial forging [ATI](https://www.atimaterials.com/markets/energy/Documents/Flowform_Datasheet.pdf "ATI Flowform specs"); [Leifeld](https://leifeldms.com/en/flow-forming.html "Flow Forming — Leifeld"); [PMF Industries](https://www.pmfind.com/news/flowforming-yields-precision-accuracy-and-keeps-an-operation-competitive "Flowforming properties").
- **CP (Cold pilgering)**: Cross-section reduction >90% single pass; wall thickness variation <0.5 µm at medium ODs; Ra ~0.5 nm (stainless steel); virtually no material loss; constant/tapered section only [SMS Meer / The Fabricator](https://www.thefabricator.com/tubepipejournal/article/tubepipeproduction/introducing-cold-pilger-mill-technology "Cold Pilger Mill").
- **CD (Cold drawing)**: IT8–IT10; Ra 0.4–1.6 µm; 20–40% reduction per pass; constant/tapered section only [The Fabricator](https://www.thefabricator.com/tubepipejournal/article/tubepipeproduction/cold-drawing-principles "Cold Drawing").
- **CWR**: FEM simulation for hollow motor shaft: OD deviation <0.8%; stepped profiles demonstrated; remains at simulation stage [Han et al., 2024](https://www.researchgate.net/publication/384053671_Design_and_simulation_of_cross_wedge_rolling_process_for_hollow_motor_shaft "CWR for hollow motor shaft").
- **RFW (Friction welding)**: Forged quality joint, 100% butt section, narrow HAZ; weld-to-finished-length ±0.38 mm; angular orientation ±1°; can join dissimilar metals; 45 s/assembly (two welds) [MTI](https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf "Friction Welding — MTI"); [KUKA](https://www.kuka.com/en-us/products/production-machines/rotary-friction-welding-machines "KUKA").
- **LW (Laser welding — EMAG assembled)**: 500,000 shafts/year per ELC 6; 47-second total cycle across 11 operations; EC Seam position control (20 measurements/circumference); complex internal cooling channels possible; all leading OEMs use ELC systems [EMAG](https://www.emag.com/industries-solutions/workpieces/assembled-rotor-shaft-electric-motor/ "EMAG Assembled Rotor Shaft"); [Engineering.com](https://www.engineering.com/manufacturing-rotor-shafts-at-the-speed-of-light-with-laser-welding/ "EMAG laser welding").
- **CC (Centrifugal casting)**: OD up to 1,092 mm; coarser microstructure than wrought; IT14–IT16 as-cast; better suited for large/thick-walled parts [Spuncast](https://spuncast.com/capabilities/centrifugal-casting/ "Centrifugal Casting").
- **AM**: WAAM buy-to-fly <2:1; as-built IT14–IT16 (WAAM) or IT12–IT14 (L-PBF); not viable for >1,000/year automotive shafts [Gefertec](https://www.gefertec.de/en/buy-to-fly-ratio/ "WAAM buy-to-fly").

**Matrix 2: Economics & Industrialisation — Key Comparative Data**

- **Material yield**: GD from solid bar ~40–60% (worst); RF from tube/preform ~85–95% (30–50% material savings vs. machining); RS from tube ~95–100% ("no waste of material"); FF ~90–98%; CP virtually no loss; WAAM buy-to-fly <2:1 [Felss Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3043336/Tube-2026-Felss-Group-GmbH-Paper-tube2026.3043336-FZ2ApYTISNirA9GZOxe72g.pdf "Felss zero waste"); [CT Forge](https://www.creatorcomponents.com/news/what-is-radial-forging-technology.html "Radial forging material savings").
- **Cycle time (automotive-sized shaft)**: RS 22 s (EV rotor shaft); LW 47 s (11 operations total); RF est. 30–120 s; RFW 45 s (2 welds); GD bore alone 2–5 min + full machining 10–30 min; FF 1–5 min [Felss Tube 2026]; [EMAG](https://www.emag.com/industries-solutions/workpieces/assembled-rotor-shaft-electric-motor/ "EMAG cycle"); [MTI](https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf "MTI cycles").
- **Capex class**: GD low–medium ($50k–$500k); RF very high ($2M–$25M+); RS high (Felss HA-series with NC/automation); HE very high (15–25 MN presses); FF high (CNC multi-roller); LW high (EMAG ELC 6 + full production line); EBW very high (vacuum); AM high (L-PBF) to medium (WAAM) [Surplus Record](https://surplusrecord.com/machinery-equipment/horizontal-deep-hole-gun-drilling-machines/ "Used gun drilling machines"); [Dataintelo](https://dataintelo.com/report/radial-forging-machines-market "Radial forging machine capex").
- **Volume suitability**: GD/BTA: all volumes (but high per-part cost); RF/RS: mid–high (>10k/yr for capex justification); FF: low–high; LW (EMAG): high (500k/yr); RFW: mid–high (250–300/hr); CWR: high (if industrialized); AM: prototype–low (<1k/yr).
- **Energy**: RS medium (cold, Felss e4.1 electric); RFW low (20% of conventional welding energy); LW low–medium; GD medium; RF high; HE very high [Felss Tube 2026]; [MTI](https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf "Friction welding energy").
- **Design flexibility**: GD/BTA high (CNC program); LW/RFW high (component mix); AM very high (digital); RS medium (NC but geometry-specific dies); RF/HE low (tooling change) [Felss Tube 2026].

**Secondary Processing Map — Key Findings**

- **GD/BTA from solid**: Full turning is the primary process; HT (through-hardening or induction); grinding of bearing seats/splines; shot peening optional; UT bore inspection.
- **RF**: CNC machining 0.5–2.0 mm OD (inner can be net-shape); HT depends on forging regime; grinding of bearing seats to IT6–IT7; shot peening of fatigue zones; UT bore wall uniformity.
- **RS**: Minimal machining (0.1–0.5 mm) or none — surfaces can be "ready for installation"; HT may be unnecessary (cold work hardening); grinding only for IT6 bearing seats; surface Ra already grinding-equivalent [Felss Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3043336/Tube-2026-Felss-Group-GmbH-Paper-tube2026.3043336-FZ2ApYTISNirA9GZOxe72g.pdf "Felss ready-for-installation").
- **FF**: 0.2–1.0 mm machining; stress relief/aging after heavy cold work; grinding OD functional surfaces; UT wall measurement [ATI](https://www.atimaterials.com/markets/energy/Documents/Flowform_Datasheet.pdf "ATI Flowform HT note").
- **LW (EMAG assembled)**: Full process chain documented: OP10/20 soft turning → OP30 cleaning → OP40 laser welding → OP50 induction hardening → OP60 finish turning → OP70 interior geometry → OP80/90 gearing → OP100 grinding → cleaning; EC Seam + UT weld inspection [EMAG](https://www.emag.com/industries-solutions/workpieces/assembled-rotor-shaft-electric-motor/ "EMAG OP sequence").
- **RFW**: Flash removal at weld (on-machine); turning/grinding functional surfaces; weld monitoring (torque, upset, RPM); UT/radiographic weld inspection [MTI](https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf "MTI weld monitoring").
- **HE**: 2–5 mm machining; HT required (normalizing or Q&T); grinding all functional surfaces; UT for internal defects.

### 可用图片
（无相关本地图片素材）

### 仍需补充
- Radial forging achievable IT grades: CT Forge (T3) reports inner ∅ ±0.025 mm (cold); GFM confirms "net-shape inner contour" but does not publish explicit IT data — direct manufacturer confirmation would strengthen this.
- Head-to-head flow forming vs. radial forging wall thickness tolerance comparison for same shaft geometry — not found.
- Quantified gun drilling material waste for specific EV shaft geometry (40–60% is derived from general engineering knowledge).
- Laser-welded assembled shaft fatigue life vs. monolithic formed shaft: no published S-N curve comparison found — critical reliability gap.
- Radial forging press capex: $2M–$25M+ range from Dataintelo (T3); GFM/SMS do not publish prices.
- CWR and skew rolling tolerance data for hollow motor shaft applications — no series production data.
- EBW cycle time and capex for EV rotor shaft geometry — not found.
- thyssenkrupp assembled rotor shaft comparison data: qualitative advantages confirmed but no quantitative tolerances, material savings %, or cost comparison vs. monolithic [thyssenkrupp](https://www.thyssenkrupp.com/en/stories/automotive-and-new-mobility/the-perfect-rotor-shaft "The perfect rotor shaft").


## Chapter 4：Integrated Manufacturing Route Assessment for NEV Hollow Motor Shafts
### 研究目标
- Identify best-fit primary forming processes for three volume tiers: low (< 10k/yr), mid (10–100k/yr), high (> 100k/yr).
- Lay out representative end-to-end process chains (raw material → primary forming → heat treatment → machining → surface treatment → inspection).
- Discuss sensitivity factors: which parameters most shift the optimal route (bore tolerance, wall thickness < 5 mm, integrated splines, dual-material)?
- Assess risk and maturity: which routes are in serial automotive production, which are pilot-scale, which are developmental?

### 关键发现

**Volume-Tiered Route Recommendations**

- **Low volume / prototype (< 10k/yr)**: Gun-drilling-from-solid-bar (Route A) remains most accessible — universally available CNC equipment, no dedicated forming tooling, maximum design flexibility for geometry iterations. AmTech OEM confirms this route in production for AISI 4140 EV motor shaft (OD 64 mm, length 305 mm). Material yield 40–60%, cycle time 10–30 min [AmTech OEM](https://www.amtechinternational.com/project/ev-motor-shaft/ "EV Motor Shaft"); flow forming (FF) is a viable alternative even at low volume (aerospace heritage) with near-net-shape output [ATI](https://www.atimaterials.com/markets/energy/Documents/Flowform_Datasheet.pdf "ATI Flowform specs").
- **Mid volume (10–100k/yr)**: Radial forging (RF) and rotary swaging (RS) become economically justified. GFM ESA-series machines target EV rotor shafts explicitly: 90–440 tons forging force, up to 1,450 strokes/min [GFM Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3048758/Tube-2026-GFM-GmbH-Paper-tube2026.3048758-RHn6chgbSQyspVyFD9vihQ.pdf "GFM ESA-series — Tube 2026"). Felss demonstrates rotor shaft swaging from tube 60×6.0 mm in 22 s with IT7 ID tolerance; Generation E10 specifically designed for rotor shafts (6,000 kN, 6-jaw, 50 Hz, 30% energy reduction) [Felss Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3043336/Tube-2026-Felss-Group-GmbH-Paper-tube2026.3043336-FZ2ApYTISNirA9GZOxe72g.pdf "Felss rotor shaft"); [The Fabricator](https://www.thefabricator.com/tubepipejournal/product/tubepipefabrication/modular-rotary-swaging-machine-is-fully-electric "Felss E10 — March 2026"). Friction welding is also viable for assembled designs at 250–300 assemblies/hr [MTI](https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf "MTI").
- **High volume (> 100k/yr)**: Laser-welded assembled rotor shaft (EMAG ELC 6) is the most widely adopted route in serial production. ~45 s/shaft, ~360k parts/yr per line. Full turnkey line integrates soft turning (VLC 200), laser cleaning (LC 4-2), laser welding (ELC 6), hard turning (VTC 200 CD), gear cutting (HLC 150 H), and grinding (HG 310). "All leading automotive manufacturers" use ELC systems. Linamar Hungary targets 430k parts/type/year on EMAG lines [EMAG](https://www.emag.com/industries-solutions/workpieces/rotor-shaft-electric-motor/ "EMAG rotor shaft line"); [EMAG/Linamar](https://www.emag.com/blog/en/linamar-relies-on-emag-for-e-mobility/ "Linamar 430k/yr target"); [Production Machining](https://www.productionmachining.com/articles/automated-high-production-welding-of-ev-rotor-shafts "EMAG welding — Production Machining 2024"). For monolithic high-volume, radial forging (GFM) produces >10 million automotive driveshafts/year globally [GFM](https://www.gfm.at/products/radial-forging-automotive/?lang=en "GFM 10M+ driveshafts/yr").

**End-to-End Process Chains (6 Routes)**

- **Route A — Gun drilling from solid bar** (low vol): Solid 42CrMo4 bar → gun drilling (2–5 min) → CNC turning → Q&T / induction hardening → hobbing → grinding (IT5–IT6, Ra 0.4–0.8 µm) → shot peening → UT + CMM + dynamic balancing. Yield ~40–60%, total 10–30 min.
- **Route B — Laser-welded assembled shaft** (high vol, most adopted): Two near-net-shape components (tube + flanged end, different materials) → OP10/20 soft turning (4× VLC) → OP30 laser cleaning (LC 4-2) → OP40 laser welding (ELC 6, EC Seam 20 measurements/circumference) → OP50 induction hardening (MIND) + hard turning (VTC 200 CD) → OP60 gear cutting (HLC 150 H) → OP70 grinding (HG 310) → EC Seam + UT weld inspection + CMM + balancing. ~45 s/shaft, 360k/yr per line [EMAG](https://www.emag.com/industries-solutions/workpieces/rotor-shaft-electric-motor/ "EMAG line").
- **Route C — Radial forging from tube/preform** (mid–high vol, monolithic): Pre-pierced billet or flow-formed blank (42CrMo4/20MnCr5) → semi-hot radial forging at 700–850°C on GFM ESA (30–120 s, net-shape inner, near-net outer) → HT (normalizing/Q&T or induction) → CNC turning OD 0.5–2.0 mm stock → hobbing → grinding → shot peening → UT + CMM + balancing. Yield 85–95%. Tsuzuki Manufacturing (Nagano, Japan) confirmed torsional fatigue testing on real specimens: max torque 802.5 Nm, yield torque 352.5 Nm, unbroken at 1M cycles at 200 Nm [Shimadzu](https://www.shimadzu.com/an/sites/shimadzu.com.an/files/pim/pim_document_file/applications/application_note/22205/an_01-00620-en.pdf "Shimadzu/Tsuzuki fatigue test 2023").
- **Route D — Rotary swaging from seamless tube** (mid–high vol, monolithic): Seamless tube (60×6 mm) → cold rotary swaging with mandrel (22 s, stepped profile, ball closure) → induction hardening bearing seats (cold-swaged base may not need bulk HT due to +30% fatigue) → minimal machining (0.1–0.5 mm) or none ("ready for installation") → grinding only if IT6 required → UT + CMM + balancing. Yield 95–100% [Felss Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3043336/Tube-2026-Felss-Group-GmbH-Paper-tube2026.3043336-FZ2ApYTISNirA9GZOxe72g.pdf "Felss rotor shaft — Tube 2026").
- **Route E — Friction-welded assembled shaft** (mid–high vol): 2–3 individually formed components (dissimilar metals possible) → rotary friction welding (2 welds, 45 s) → flash removal → CNC turning/grinding functional surfaces → HT per spec → UT/radiographic weld inspection + CMM + balancing [MTI](https://www.mtiwelding.com/wp-content/uploads/2015/11/mti-friction-welding-technology-brochure.pdf "MTI"); [KUKA](https://www.kuka.com/en-us/products/production-machines/rotary-friction-welding-machines "KUKA").
- **Route F — Cold-formed modular with guided cooling** (emerging): 20MnCr5, tube-in-tube construction, cold-formed inner channels → assembly → cold-formed outer profile. 110% cooling efficiency gain at low RPM. Research stage [Goetz et al., arXiv 2510.22029](https://arxiv.org/html/2510.22029v1 "Cold-formed modular shaft 2025").

**Trade-off Analysis**

- **Bore tolerance tightening**: GD achieves ±0.008 mm; RS over mandrel IT7 (±0.01–0.05 mm); RF cold inner ∅ ±0.025 mm. Tight bore tolerance shifts route away from hot forming toward cold forming (RS, cold RF) or subtractive finishing [AMG](https://www.amgundrilling.com/technical-gundrilling-information.html "GD bore tolerance"); [Felss Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3043336/Tube-2026-Felss-Group-GmbH-Paper-tube2026.3043336-FZ2ApYTISNirA9GZOxe72g.pdf "RS ID tolerance").
- **Wall < 5 mm**: Favors flow forming (min 0.20 mm) and rotary swaging (variable wall). RF limited by mandrel rigidity at thin walls. GD increasingly wasteful as bore grows. Assembled route accommodates thin-walled tube sections [ATI](https://www.atimaterials.com/markets/energy/Documents/Flowform_Datasheet.pdf "ATI min wall").
- **Integrated splines**: RF with profiled mandrel and RS with profiled mandrel eliminate separate hobbing. FF forward forming produces internal teeth. GD and LW routes always require separate hobbing [GFM](https://www.gfm.at/products/radial-forging-automotive/?lang=en "GFM internal splines"); [Leifeld](https://leifeldms.com/en/flow-forming.html "FF internal teeth").
- **Dual-material / bimetallic**: Assembled routes (LW, RFW) have clear advantage — thyssenkrupp explicitly designs with higher-alloy steel at gear end, lower-alloy for tube section. Monolithic routes limited to single grade [thyssenkrupp](https://www.thyssenkrupp.com/en/stories/automotive-and-new-mobility/the-perfect-rotor-shaft "Bimetallic shaft advantages").
- **Oil cooling complexity**: LW assembled route offers greatest design freedom for internal cooling channels ("geometries that cannot be machined in a solid part"). Simple straight-through bore achievable by any hollow route [EMAG](https://www.emag.com/industries-solutions/workpieces/assembled-rotor-shaft-electric-motor/ "EMAG internal cooling").
- **30,000+ rpm**: Tightens balance to 50 mg, concentricity critical. Favors forming processes with compressive residual stress and improved grain flow (RS, RF) for fatigue under centrifugal load. Weld-zone-induced imbalance is a theoretical concern for assembled routes at extreme speeds [CarNewsChina](https://carnewschina.com/2025/03/20/byd-releases-ground-breaking-30511-rpm-motor/ "BYD 50 mg balance").

**Risk & Maturity Assessment**

- **Serial production (TRL 9)**: (1) Laser-welded assembled shaft — thyssenkrupp since 2013, 10 global locations including China (Dalian, Changzhou); EMAG ELC used by "all leading automotive manufacturers"; Linamar Hungary 430k/yr [thyssenkrupp Dynamic Components](https://www.thyssenkrupp-automotive-technology.com/en/company/organizational-structure/dynamic-components "thyssenkrupp 10 locations"); [EMAG/Linamar](https://www.emag.com/blog/en/linamar-relies-on-emag-for-e-mobility/ "Linamar EMAG"). (2) Gun drilling from solid — universally available. (3) Radial forging for automotive driveshafts — >10M/yr globally (GFM).
- **Late pilot / early serial (TRL 7–8)**: (1) Radial forging for EV rotor shafts — Tsuzuki Manufacturing (Japan) with GFM machine since 2019, confirmed fatigue testing on real specimens [Shimadzu](https://www.shimadzu.com/an/sites/shimadzu.com.an/files/pim/pim_document_file/applications/application_note/22205/an_01-00620-en.pdf "Shimadzu/Tsuzuki 2023"); [DMG MORI/Tsuzuki](https://en.dmgmori.com/news-and-media/customer-stories/tsuzuki-manufacturing-co-ltd "Tsuzuki"). (2) Rotary swaging for EV rotor shafts — Felss Tube 2026 demonstration + Generation E10 machine; full serial for other automotive shafts; Tian et al. (2025) validated for railway motor shafts [Felss Tube 2026]; [ScienceDirect / Tian et al.](https://www.sciencedirect.com/science/article/abs/pii/S0959652625003610 "Rotary swaging hollow motor shafts 2025"). (3) Friction welding for EV shafts — full serial for other automotive components, not confirmed specifically for EV rotor shafts.
- **Developmental (TRL 4–6)**: CWR (simulation only, Han et al. 2024); cold-formed modular (Goetz et al. 2025, research stage); AM for motor shafts (no demonstrator).

**Supply Chain Structure**

- Equipment: GFM (Austria/USA, radial forging), SMS Group (Germany, SMX), Felss (Germany, rotary swaging), EMAG LaserTec (Germany, laser welding/full lines), KUKA/Thompson (UK, friction welding), MTI (USA, friction welding), UNISIG (USA, gun/BTA drilling), Leifeld/Nihon Spindle (Germany, flow forming).
- Tier-1 contract manufacturers: thyssenkrupp Dynamic Components (10 global locations, assembled rotor shafts), Tsuzuki Manufacturing (Japan, radial-forged), Linamar (Hungary, EMAG lines), AmTech (USA, gun-drilled/machined).

### 可用图片
（无相关本地图片素材）

### 仍需补充
- Specific OEM names using each route are not publicly disclosed (supply chain confidentiality).
- Per-unit cost data across routes: no T1/T2 source; relative material savings (RF 30–50% vs. machining) available but not fully loaded cost models.
- Rotary swaging serial production for EV rotor shafts specifically (vs. other automotive shafts) — Felss demonstrates but confirmed OEM serial reference not public.
- Fatigue life comparison across all five routes (GD, LW, RF, RS, RFW) for identical shaft geometry — only RF fatigue data available (Shimadzu/Tsuzuki).
- Quantified threshold at which monolithic formed route becomes necessary vs. assembled route for rotor speed reasons (30k+ rpm weld-zone imbalance concern is theoretical).
- Chinese NEV OEM route selections (BYD, NIO, Xiaomi) not publicly documented.
- Whether cold-swaged work hardening can fully replace Q&T for 42CrMo4 at 30,000+ rpm fatigue regime — needs metallurgical T1 validation.


## Chapter 5：Outlook — Technology Trends and Future Directions
### 研究目标
- Identify credible near-term process innovation trends (CWR advances, next-gen radial forging/swaging machines, intelligent process control, servo-press technology).
- Cover material and design trends (bimetallic shafts, assembled multi-material, topology-optimized cooling, AHSS evaluation, integrated rotor-shaft).
- Address industry and supply-chain considerations (market sizing, regionalization, sustainability, vertical integration, high-speed motor implications).

### 关键发现

**Process Innovation Trends**

- **CWR progressing from simulation toward experimental**: Zhu et al. (May 2025) published first experimental CWR of bimetallic hollow shaft (304SS/45 steel) with mandrel, investigating interfacial bonding quality. Lei et al. (July 2025) proposed flat-corrugated CWR for 42CrMo4/45 hollow laminated shafts explicitly targeting NEV applications (simulation stage, max rolling force ~290 kN). However, no experimental CWR trial has produced a complete motor shaft geometry with stepped profile, bearing seats, and splined ends. Assessed at TRL 3–4; industrialization unlikely before 2028–2029 [Zhu et al., ACME 2025](https://ui.adsabs.harvard.edu/abs/2025ACME...25..178Z/abstract "CWR bimetallic hollow shaft — experimental, 2025"); [Lei et al., J. Netshape Forming Eng. 2025](https://www.nsforming.com/EN/10.3969/j.issn.1674-6457.2025.07.003 "Corrugated CWR for NEV laminated shaft, 2025").
- **GFM ESA-series radial forging**: New platform launched at Tube 2026, explicitly for EV rotor shafts (90–440 tons, 1,450 strokes/min, cold/semi-hot/hot). Represents expansion from driveshaft production (>10M shafts/yr on 200+ machines) into EV rotor shaft segment [GFM Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3048758/Tube-2026-GFM-GmbH-Paper-tube2026.3048758-RHn6chgbSQyspVyFD9vihQ.pdf "GFM ESA-series — Tube 2026").
- **SMS ComForge® Property Predictor**: Digital twin for radial forging enabling property-based process optimization (strain + temperature distribution prediction within seconds, 200+ material database, pore closure verification) [SMS Group](https://www.sms-group.com/en-es/services/comforge "ComForge® intelligent process control").
- **Felss Generation E10**: Fully electric modular rotary swaging machine launched March 2026; 6-jaw, 6,000 kN, up to 50 Hz, 5 NC axes, 50% higher runout accuracy, ≥30% energy reduction, component condition monitoring. Specifically designed for rotor shafts, side shafts, transmission shafts [FFJournal March 2026](https://www.ffjournal.net/industry-news/5-news/generation-e10-felss-advances-rotary-swaging-technology "Felss E10 — March 2026"); [The Fabricator March 2026](https://www.thefabricator.com/tubepipejournal/product/tubepipefabrication/modular-rotary-swaging-machine-is-fully-electric "Felss E10 fully electric").
- **EMAG ELC 6i**: Next-generation compact laser welding integrating up to 6 process steps in one machine; cycle time <20 seconds (vs. 45 s for ELC 6); 36% smaller footprint; 15% lower investment; changeover <20 min; Siemens Sinumerik One CNC [EMAG](https://www.emag.com/products-services/machines/laser-machines/laser-welding-machines/elc-6i/ "ELC 6i compact laser welding 2026").
- **EMAG EDNA ONE**: Full Industry 4.0 ecosystem — IoT data acquisition, real-time production display, workpiece tracking, predictive condition monitoring (traffic-light system for machine axis status), applies across VLC turning, ELC welding, MIND induction hardening, HG grinding [EMAG](https://www.emag.com/products-services/digitalization/ "EDNA ONE Industry 4.0").
- **Servo press in forging**: Maturing technology (Fagor Arrasate since 2005); servo-hydraulic presses save >50% energy vs. conventional hydraulic; enables speed adaptation during stroke for quality improvement [Fagor Arrasate](https://fagorarrasate.com/solution/spt-servo-press-technology-in-forging/ "SPT Servo Press"); [Baumüller](https://www.baumueller.com/en/news/press/releases/2022/hydraulics-vs-servo-hydraulics-calculate-energy-saving-quickly-and-easily "Servo-hydraulic >50% savings").
- **Hybrid AM**: Remains impractical for motor shafts in 2026–2028 horizon; no demonstrator exists; nearest potential role is rapid tooling/prototype mandrels, not shafts themselves.

**Material and Design Trends**

- **Bimetallic shafts via CWR**: Active research frontier (Zhu et al. 2025 experimental, Lei et al. 2025 simulation) — could combine 42CrMo4 outer fatigue resistance with 45 steel core ductility/cost. Laboratory stage [Zhu et al., ACME 2025](https://ui.adsabs.harvard.edu/abs/2025ACME...25..178Z/abstract "CWR bimetallic — 2025").
- **Assembled multi-material in production**: thyssenkrupp Dynamic Components produced ~1.5 million rotor shafts in FY2023/2024 at 10 global locations; first Volvo production at Changzhou (China) in 2023; CEO targets "electric drive components to account for ~30% of sales" within five years [thyssenkrupp](https://www.thyssenkrupp-automotive-technology.com/en/press-detail/thyssenkrupp-dynamic-components-celebrates-10-years-of-rotor-shafts-for-electric-motors-and-continues-its-global-expansion-strategy-229318 "thyssenkrupp 10 years of rotor shafts, ~1.5M planned, Volvo China").
- **Topology-optimized cooling**: Goetz et al. (2025) tooth-guided liquid-cooling channel in 20MnCr5, 110% cooling improvement at low RPM via cold-formed tube-in-tube construction. Research stage [Goetz et al., arXiv 2510.22029](https://arxiv.org/html/2510.22029v1 "Cold-formed modular cooling shaft 2025").
- **AHSS for motor shafts**: No evidence of evaluation found as of early 2026. 42CrMo4/20MnCr5/S45C remain dominant; AHSS multiphase microstructure suitability for high-cycle torsional fatigue at 30k+ rpm is uncharacterized.
- **Integrated rotor-shaft**: GFM and Felss produce rotor mounting OD profiles during primary forming (eliminating secondary machining for lamination retention surfaces), but true single-piece rotor-shaft eliminating interference-fit assembly of lamination stack has not been demonstrated.

**Industry and Supply-Chain Considerations**

- **Market size**: Global EV rotor shaft market valued ~$423M (2024), projected $1.14B by 2031 (~15.3% CAGR) [OpenPR/QYResearch](https://www.openpr.com/news/4441570/global-ev-rotor-shaft-market-to-surge-from-us-423-million-to-us "EV rotor shaft market — $423M to $1.14B"). Alternative estimate: $3.03B (2026) → $5.14B (2032) at 9% CAGR [Research and Markets](https://www.researchandmarkets.com/reports/6126803/ev-rotor-shaft-market-global-forecast "EV rotor shaft market alternative estimate"). Wide range reflects different scope definitions. Global e-motor demand to treble within next decade; European e-motor market to exceed £27B by 2035; PMSM remains leading motor type [APC E-Motors Report May 2024](https://www.apcuk.co.uk/wp-content/uploads/2024/05/2024-e-motors-value-chain-insight.pdf "APC E-Motors Value Chain Insight").
- **Regionalization**: thyssenkrupp at 10 global locations including China/USA/Mexico/Brazil/Hungary; Linamar Hungary 430k EV parts/yr on EMAG lines; Ford Halewood (UK) converting to 400k e-drive units/yr [thyssenkrupp](https://www.thyssenkrupp-automotive-technology.com/en/press-detail/thyssenkrupp-dynamic-components-celebrates-10-years-of-rotor-shafts-for-electric-motors-and-continues-its-global-expansion-strategy-229318 "thyssenkrupp regionalization"); [APC 2024](https://www.apcuk.co.uk/wp-content/uploads/2024/05/2024-e-motors-value-chain-insight.pdf "Ford Halewood").
- **Vertical integration**: Mixed model — Tesla highly vertically integrated but specific in-house shaft manufacturing unconfirmed; most major OEMs (VW, Volvo) use Tier-1 suppliers (thyssenkrupp confirmed for VW e-UP since 2013, Volvo Changzhou since 2023). Chinese OEM routes undocumented publicly.
- **Sustainability**: Felss E10 achieves ≥30% energy reduction; servo-hydraulic >50% savings vs. conventional hydraulic. Cold forming eliminates heating energy (700–1,300°C) entirely. Material yield: 95–100% (RS) vs. 40–60% (GD) — proportionally lower embodied energy in raw material [Felss Tube 2026](https://www.wire.de/vis-content/event-tube2026/exh-tube2026.3043336/Tube-2026-Felss-Group-GmbH-Paper-tube2026.3043336-FZ2ApYTISNirA9GZOxe72g.pdf "Felss sustainability"); [Baumüller](https://www.baumueller.com/en/news/press/releases/2022/hydraulics-vs-servo-hydraulics-calculate-energy-saving-quickly-and-easily "Servo-hydraulic savings").
- **30,000+ rpm trend favors monolithic forming**: Higher speeds tighten balance (50 mg) and fatigue requirements; monolithic formed shafts (RF, RS) avoid weld-zone discontinuities, produce compressive residual stresses and refined grain flow. However, no published study quantifies the speed threshold at which monolithic routes become necessary vs. assembled routes [CarNewsChina](https://carnewschina.com/2025/03/20/byd-releases-ground-breaking-30511-rpm-motor/ "BYD 30,511 rpm"); [IDTechEx Dec 2025](https://www.idtechex.com/en/research-article/the-need-for-speed-ev-motors-breaking-the-30-000rpm-barrier/34219 "IDTechEx 30,000 rpm barrier").

### 可用图片
（无相关本地图片素材）

### 仍需补充
- Per-shaft energy consumption (kWh/shaft) across routes — no T1/T2 data; only relative improvements available (Felss 30%, servo-hydraulic 50%).
- CO₂ footprint per shaft / lifecycle assessment for motor shaft manufacturing — no shaft-specific LCA published.
- CWR experimental validation for complete motor shaft geometry (stepped profile + bearing seats + splines) — critical gap before industrial consideration.
- AHSS evaluation for motor shafts at 30k+ rpm fatigue conditions — uncharacterized.
- Equipment lead times and pricing for GFM ESA, Felss E10, EMAG ELC 6i — commercially sensitive.
- Chinese OEM manufacturing route specifics (BYD, NIO, Xiaomi, GAC) — not publicly documented.
- Workforce forming vs. machining skill gap quantification — no industry survey data.
- Advanced bore surface treatments (DLC, nitriding, internal shot peening) for cooling passages — no published trends found.


# Section 2：给 Write 阶段的执行建议

1. **Cross-referencing consistency**: Chapter 1 produces a "requirement checklist" (RP-1 … RP-n) that must be explicitly referenced in every Chapter 3 comparison row and every Chapter 4 route recommendation. Chapter 2 assigns each process a short code (RF = Radial Forging, FF = Flow Forming, etc.) reused consistently throughout.

2. **Terminology standardisation**: Disambiguate easily confused pairs — "rotary swaging" vs. "radial forging"; "flow forming" vs. "tube spinning" vs. "spin forming"; "gun drilling" vs. "BTA drilling" vs. "deep-hole drilling." Use ISO/DIN tolerance notation (IT7, Ra 1.6 µm). Standardise on SI units; provide SI equivalents where industry convention uses imperial.

3. **Comparison matrix design**: Chapter 3 uses a descriptive matrix (not weighted-score), letting readers apply their own weighting. Two separate tables: (a) Geometry & Quality, (b) Economics & Industrialisation. Add a "Secondary Processing Map" table. Rows = process short codes, columns = criteria, plus a "Notes/Limitations" column. Design for A4/Letter landscape (≤ 12 columns).

4. **Content overlap avoidance**: Chapter 2 describes *how each process works* (no evaluation). Chapter 3 *compares outcomes* (no re-explanation). Chapter 4 focuses on sequencing/integration of recommended routes, referencing Chapter 3 data. Chapter 5 must not introduce new processes not already catalogued in Chapter 2 Section 5.

5. **Style**: Engineering-focused, quantitative ranges preferred over qualitative adjectives. Concise, technically precise, no marketing superlatives. Trade-offs stated as explicit engineering statements ("Increasing X improves Y but degrades Z").

6. **Time scope**: The report covers approximately April 2025 – October 2026, anchored to the current date of 2026-04-07. Historical context may extend further back where needed to explain established processes.

7. **Process short codes**: Use these consistently throughout the report — GD (gun drilling), BTA (BTA/STS drilling), TR (trepanning), BH (boring/honing), RF (radial forging), RS (rotary swaging), HE (hot extrusion), CWR (cross-wedge rolling), SR (skew rolling/Mannesmann), MF (mandrel forging), FF (flow forming), HF (hydroforming), CD (cold drawing), CP (cold pilgering), RFW (rotary friction welding), LW (laser welding assembled), EBW (electron beam welding), SF (shrink-fit), CC (centrifugal casting), AM (additive manufacturing), EMF (electromagnetic forming).

8. **Key source hierarchy for verification during writing**: (a) Equipment manufacturer technical papers presented at Tube 2026 (GFM, Felss) — T1/T2 for process capability claims; (b) EMAG product pages and customer case studies — T1/T2 for assembled shaft production data; (c) thyssenkrupp press releases and corporate website — T1 for production volumes and global footprint; (d) Shimadzu/Tsuzuki application note — T1 for fatigue test data on radial-forged shafts; (e) ATI/PMF datasheets — T2 for flow forming specifications; (f) UNISIG/AMG — T1/T2 for drilling specifications; (g) Academic papers (Han et al. 2024, Zhu et al. 2025, Lei et al. 2025, Goetz et al. 2025, Tian et al. 2025) — T1 for research-stage processes. KeSu Group, CT Forge, Dataintelo, CarNewsChina are T3 sources — acceptable for background but not for core numbers without corroboration.

9. **Critical unresolved question for the report**: No published fatigue life comparison exists across all recommended routes (GD, LW, RF, RS, RFW) for identical shaft geometry. The Shimadzu/Tsuzuki data covers RF vs. conventional forging only. The report should explicitly acknowledge this gap and frame route recommendations as based on process capability, material yield, cycle time, and maturity — not fatigue equivalence, which remains unvalidated across routes.

10. **Market data caveat**: Two conflicting EV rotor shaft market estimates exist ($423M→$1.14B vs. $3.03B→$5.14B). Present both with scope differences noted. Prefer IDTechEx motor demand data (140M motors/year by 2036) as the more authoritative demand indicator (T2).
