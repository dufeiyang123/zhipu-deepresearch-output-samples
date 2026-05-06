# Section 1：章节研究计划

## Chapter 1：Defining the 500,000-Passenger Airport Tier

### 研究目标
- Establish what a 500,000 annual-passenger airport is in global aviation taxonomy (FAA, ACI, ICAO, European frameworks)
- Determine how many such airports exist worldwide and what communities they typically serve
- Clarify terminology: "enplanements" vs "passenger movements" vs "passenger throughput"
- Profile the typical catchment area: population size, distance from major hubs, economic base

### 关键发现
- Under 49 U.S.C. § 47102, the FAA classifies primary airports by share of total U.S. enplanements: Large Hub (≥1.0%), Medium Hub (0.25%–<1.0%), Small Hub (0.05%–<0.25%), Nonhub Primary (>10,000 but <0.05%). With CY 2023 total enplanements at 944.9 million, the Small Hub floor is ~472K enplanements. An airport with 500K total passengers (≈250K enplanements) sits firmly in the **Nonhub Primary** tier. [FAA NPIAS 2023–2027 Appendix C](https://www.faa.gov/sites/faa.gov/files/NPIAS-2023-2027-Appendix-C.pdf "Statutory definitions") and [FAA CY 2023 All Enplanements](https://www.faa.gov/sites/faa.gov/files/2024-10/cy23-all-enplanements.pdf "944,891,353 total enplanements")
- The NPIAS 2025–2029 identifies 3,287 NPIAS airports, of which 390 are primary (31 Large, 33 Medium, 74 Small, 252 Nonhub Primary). Nonhub Primary airports account for 3% of enplanements and 12% ($8 billion) of NPIAS development needs. [FAA NPIAS 2025–2029 Narrative](https://www.faa.gov/sites/faa.gov/files/airports/planning_capacity/npias/current/ARP-NPIAS-2025-2029-Narrative.pdf "Published September 30, 2024")
- Specific U.S. airports near the 250K-enplanement mark (≈500K total passengers) include Monterey Regional (MRY, 259,778), Bismarck Municipal (BIS, 258,780), Montrose Regional (MTJ, 244,266), and Grand Junction Regional (GJT, 243,808) — all classified Nonhub Primary. [FAA CY 2023 All Enplanements](https://www.faa.gov/sites/faa.gov/files/2024-10/cy23-all-enplanements.pdf "Airport-level CY 2023 data")
- Terminology: "Enplanements" count departing passengers only (FAA metric); "passenger movements" count arrivals + departures (≈2× enplanements); "passenger throughput" is used interchangeably with "passenger movements" by ACI World and most international bodies. This report's "500,000 annual passengers" = ~500K movements = ~250K FAA enplanements.
- ACI World segments airports by total passenger throughput; the 500K–1M bracket is the lowest named group in WATR traffic analyses. ACI's "Small and Emerging Airports" programme targets sub-5M airports with no rigid numeric threshold. The 2024 global total was 9.4 billion passengers across ~2,800 airports. [ACI World WATR 2023](https://store.aci.aero/wp-content/uploads/2023/09/Preview-2023-ACI-WATR-09-2023.pdf "ACI size brackets") and [ACI 2024 Traffic Blog](https://blog.aci.aero/airport-economics/busiest-airports-in-the-world-2024/ "9.4B passengers in 2024")
- ACI Europe classifies members into Group 1 (>25M), Group 2 (10–25M), Group 3 (5–10M), Group 4 (<5M). A 500K airport is deep within Group 4, the largest category by airport count. [ACI Europe Connectivity Report 2023](https://www.aci-europe.org/downloads/resources/ACI%20EUROPE%20Airport%20Industry%20Connectivity%20Report%202023.pdf "Group 4 = <5M pax")
- EUROCONTROL classifies by IFR movements, not passengers. A 500K-passenger airport (~5,000–8,000 IFR movements) falls in the "Other" or low "Small" tier. EU Slot Regulation and Ground Handling Directive thresholds (5M and 2M passengers respectively) are far above 500K, meaning these airports face a lighter regulatory environment. [EUROCONTROL Standard Inputs Ed. 9](https://ansperformance.eu/economics/cba/standard-inputs/v9.0.3/chapters/airport_classification.html "IFR movement-based classification") and [Council Directive 96/67/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:31996L0067 "Ground handling thresholds")
- Approximately 15–20 U.S. airports sit in the 400K–600K total-passenger band; globally, an estimated 150–250 airports fall in this range, distributed across North America (15–25), Europe (40–70), Asia-Pacific (30–60), and other regions (20–50). The global estimate is inferred from FAA data and ACI's known dataset size/power-law distribution.
- Typical community profiles for 500K-airport catchments include: (1) mid-size cities/state capitals with metro populations of 50K–250K; (2) tourism-dependent resort areas with seasonal traffic (e.g., Vail, Montrose/Telluride); (3) peripheral/rural regions with no nearby major hub (e.g., Juneau, AK); (4) island/archipelago communities where air is the only fast link; (5) secondary/university cities near metropolitan regions.
- Cherry Capital Airport (TVC), Traverse City, MI, exemplifies the tier: 347,763 enplanements (CY 2023) and a record 787,114 total passengers in 2024, serving a ~100K metro area in a tourism-driven region, with 6 airlines and 20 nonstop destinations. [Cherry Capital Airport 2024 Annual Report](https://tvcairport.com/wp-content/uploads/2025/10/TVC-AnnualReport-2024-final.pdf "Record 787,114 passengers in 2024")
- Per NPIAS 2025–2029, 330 Nonhub airports reported FY 2022 total revenue of $3.336 billion and total expenses of $1.274 billion. Many depend heavily on grants ($1.437 billion, highest across hub categories) and PFC collections ($98 million). [FAA NPIAS 2025–2029 Narrative, Table 3](https://www.faa.gov/sites/faa.gov/files/airports/planning_capacity/npias/current/ARP-NPIAS-2025-2029-Narrative.pdf "FY 2022 financial data")

### 可用图片
- None identified (local chart scripts pertain to unrelated projects)

### 仍需补充
- Exact global count of airports in 400K–600K band requires ACI's paywalled dataset; the 150–250 estimate is inferred, not citable to a single authoritative figure
- ACI World "small and emerging airports" programme lacks a formal numeric threshold
- ICAO has no passenger-volume-based airport classification (Annex 14 classifies by physical characteristics only)
- Non-US examples at 500K level (e.g., Inverness, Tromsø, Indian UDAN airports) need individual verification through primary sources

---

## Chapter 2：Frameworks and Methodologies for Measuring Airport Economic Impact

### 研究目标
- Survey the four-tier impact taxonomy: direct, indirect, induced, catalytic
- Critically appraise input-output models (IMPLAN, RIMS II), ACI/ATAG catalytic frameworks, and counterfactual approaches
- Assess whether standard methodologies and multipliers behave differently at the 500K-airport scale vs. large hubs
- Identify data availability challenges unique to small airports

### 关键发现
- The standard framework classifies airport impacts into four tiers: **direct** (on-airport employment, payroll, expenditures), **indirect** (off-site supplier and visitor spending), **induced** (multiplier effects from successive spending rounds), and **catalytic** (wider connectivity benefits — tourism, trade, FDI, productivity). The first three were codified in the FAA's 1992 guide (DOT/FAA/PP-92-6); ACI Europe/York Aviation added the catalytic tier in 2004. [FAA 1992 Guide](https://gardnermagazine.com/wp-content/uploads/2024/02/Airports-1992-Report-dot_35802_DS1.pdf "DOT/FAA/PP-92-6") and [Forsyth & Niemeier 2016](http://www.verkehrskonferenz.de/fileadmin/archiv/konferenz_2016/Papers/forsyth_et_al-wider_economic_benefits_or_catalytic_effects_of_air_transport.pdf "citing ACI Europe/York 2004")
- RIMS II (BEA) and IMPLAN are the dominant I-O models for U.S. airport studies. RIMS II provides ~60 industry sectors at low cost and is used by the FAA; IMPLAN covers 540+ NAICS sectors at higher cost and is used by ACI-NA. Both are static models with well-known limitations: fixed coefficients, perfectly elastic supply assumptions, double-counting risk, and no crowding-out effects. [FAA Economic Impact Report 2024](https://www.faa.gov/2024-economic-impact-report.pdf "FAA uses RIMS II with 2012 I-O benchmark and 2022 regional accounts") and [ACI-NA 2024 Study](https://www.mvcommission.org/sites/default/files/docs/ACI-NA-The-Economic-Impact-of-U.S.-Commercial-Service-Airports-in-2024.pdf "487 airports, IMPLAN-based")
- Forsyth & Niemeier (2016) summarize the academic critique: I-O-based EIA is "useful for economic significance and regional agglomeration" but "should not be used to assess decisions on investment, night curfews and subsidies for regional airports" because direct+indirect effects are proportional to cost, induced effects are investment-agnostic, and substitution/price effects are neglected. [Forsyth & Niemeier 2016](http://www.verkehrskonferenz.de/fileadmin/archiv/konferenz_2016/Papers/forsyth_et_al-wider_economic_benefits_or_catalytic_effects_of_air_transport.pdf "Wider Economic Benefits or Catalytic Effects")
- ATAG's *Aviation: Benefits Beyond Borders* 2024 estimates aviation supports 86.5 million jobs and $4.1 trillion globally (3.9% of GDP) for 2023, using OECD ICIO tables. The catalytic tier alone accounts for 37.3 million jobs. ATAG's employment rule of thumb is scale-dependent: 1.20 jobs per 1,000 passengers at 0–1M airports, declining to 0.85 at >10M airports. [ATAG ABBB 2024](https://aviationbenefits.org/media/e5ynn4x0/abbb2024_full_report.pdf "ABBB 2024, Oxford Economics")
- Catalytic impacts vary wildly across studies — from 25% additional jobs (Infras 2005) to 142–177% (Baum 2005; InterVISTAS/ACI Europe 2015). ACI Europe & InterVISTAS acknowledged that economic impact assessments "are easily abused." The core attribution problem is reverse causality: does connectivity cause growth, or does growth attract air service? [Forsyth & Niemeier 2016](http://www.verkehrskonferenz.de/fileadmin/archiv/konferenz_2016/Papers/forsyth_et_al-wider_economic_benefits_or_catalytic_effects_of_air_transport.pdf "catalytic effect range comparison")
- Campante & Yanagizawa-Drott (2018, QJE) provide the most influential quasi-experimental study, using new long-haul route introductions (instrumented by aircraft range improvements) as natural experiments to show air connectivity increases bilateral business links and economic activity. Gibbons & Wu (2020, JEG) used difference-in-differences on China's airport expansion program and found airports boosted local economic activity. [Campante & Yanagizawa-Drott 2018](https://www.researchgate.net/publication/328768499_Long-Range_Growth_Economic_Development_in_the_Global_Network_of_Air_Links "QJE 133(3)") and [Gibbons & Wu 2020](https://academic.oup.com/joeg/article/20/4/903/5692238 "JEG 20(4)")
- The FAA 1992 guide provides population-based multiplier shortcuts reflecting scale sensitivity: regions <100K population → 0.5 multiplier; 100K–500K → 0.6; 500K–3M → 0.75; >3M → 1.0. Since 500K-passenger airports typically serve smaller communities, their induced impacts are proportionally smaller due to higher economic leakage. [FAA 1992 Guide](https://gardnermagazine.com/wp-content/uploads/2024/02/Airports-1992-Report-dot_35802_DS1.pdf "population-based shortcut multipliers")
- ACI-NA 2024 national averages: 1,000 additional enplanements produce $387,200 in on-airport output and 1.2 on-airport jobs, plus $290,500 in visitor output and 4.6 visitor-related jobs (5.8 total jobs per 1,000 enplanements). System-wide employment multiplier: 1.96; payroll multiplier: 2.24; output multiplier: 2.51. [ACI-NA 2024 Study](https://www.mvcommission.org/sites/default/files/docs/ACI-NA-The-Economic-Impact-of-U.S.-Commercial-Service-Airports-in-2024.pdf "incremental metrics and Table 21")
- 27% of U.S. commercial airports (130 of 487) lack direct impact data, predominantly smaller airports. For these, regression analysis is used (R²=0.91 with enplanements). The FAA 1992 guide acknowledges its 650-jobs-per-million-passengers rule "does not apply to smaller commercial service airports." The TTI developed a web-based Small Airport Economic Impact Model to address this gap. [ACI-NA 2024 Study](https://www.mvcommission.org/sites/default/files/docs/ACI-NA-The-Economic-Impact-of-U.S.-Commercial-Service-Airports-in-2024.pdf "regression section") and [TTI Report 0-7066-R1](https://static.tti.tamu.edu/tti.tamu.edu/documents/0-7066-R1.pdf "small airport model, 2020")

### 可用图片
- None identified

### 仍需补充
- ACI Europe/York Aviation (2004) and ACI Europe/InterVISTAS (2015) catalytic methodology documents not directly accessible; cited via Forsyth & Niemeier 2016
- A 2026 ScienceDirect literature review covering 96 airport economic impact studies is paywalled
- No study directly compares IMPLAN/RIMS II multiplier magnitudes specifically at a 500K-passenger airport vs. large hub; scale sensitivity evidence is assembled from indirect sources
- No GAO audit of airport economic impact methodology was located
- Social Accounting Matrices (SAM) are rarely used in airport studies; primarily developing-country applications

---

## Chapter 3：Direct Economic Contributions of 500K-Passenger Airports

### 研究目标
- Quantify on-airport employment benchmarks (job counts, jobs-per-thousand-passengers ratios) for the 400K–600K range
- Assess payroll, labor income, and wage levels relative to regional medians
- Examine airport operating economics at this scale (revenue sources, operating margins, ACI data on loss-making airports)
- Estimate direct GDP contribution and tax/fiscal contribution
- Address the proportionality question: how large are direct effects relative to the total local economy?

### 关键发现
- At the 500K-passenger level (~250K enplanements), two benchmark approaches yield different direct on-airport job estimates: ACI-NA's system-wide ratio (1.2 jobs per 1,000 enplanements) implies ~300 direct on-airport jobs and ~$97M in on-airport output; ATAG's scale-dependent ratio (1.20 jobs per 1,000 passenger movements for 0–1M airports) implies ~600 direct jobs. The divergence reflects definitional differences (enplanements vs. total movements) and scope variations. [ACI-NA 2024 Study](https://www.mvcommission.org/sites/default/files/docs/ACI-NA-The-Economic-Impact-of-U.S.-Commercial-Service-Airports-in-2024.pdf "incremental ratios") and [ATAG ABBB 2024](https://aviationbenefits.org/media/e5ynn4x0/abbb2024_full_report.pdf "scale-dependent employment ratios")
- Yellowknife Airport (YZF, Canada), processing 532,689 passengers in 2014, directly employed 1,001 FTE (1.8 per 1,000 passengers), generated $72M in direct labor income (~$71,600/FTE), $171M in direct GDP (4.5% of NWT territorial GDP), and $45M in taxes. Including multiplier effects: 2,072 total jobs, $612M total output, $307M total GDP (8.0% of territorial GDP). [Yellowknife Airport EIS](https://www.inf.gov.nt.ca/sites/inf/files/resources/final_economic_impact_analysis_14-12-15_5.pdf "Lindbergh Group, December 2015")
- Montrose Regional Airport (MTJ, Colorado), ~449K passengers in 2020, supported 449 direct on-airport jobs ($18.5M payroll, ~$41,200/job) and 2,850 total jobs including visitor spending ($327.3M business revenues). The 2025 Colorado CEIS updated to 4,323 total jobs, $231M payroll, $713.1M business revenues, and $421.5M value-added — heavily driven by ski-tourism visitor spending. [Colorado CEIS 2020](http://www.coloradoaviationsystem.com/wp-content/uploads/2024/09/Montrose-Regional-MTJ.pdf "MTJ report") and [2025 Colorado CEIS](http://www.coloradoaviationsystem.com/wp-content/uploads/2025/02/CEIS-Executive-Summary_FINAL_021925.pdf "executive summary")
- Other Colorado airports near the 500K threshold in 2025 CEIS: Durango-La Plata (DRO) — 1,993 total jobs, $111.8M payroll, $342.1M revenues; Gunnison-Crested Butte (GUC) — 958 total jobs, $54.5M payroll, $154.9M revenues. [2025 Colorado CEIS](http://www.coloradoaviationsystem.com/wp-content/uploads/2025/02/CEIS-Executive-Summary_FINAL_021925.pdf "individual airport totals")
- NPIAS FY 2022 data for 330 nonhub airports: aeronautical revenue $783M, non-aeronautical revenue $594M, operating expenses $1,320M, grants $1,437M, PFC collections $98M. Per-airport averages: ~$4.2M operating revenue, ~$4.0M expenses, ~$4.4M grants. Revenue split: 57% aeronautical / 43% non-aeronautical among operating revenues. [FAA NPIAS 2025–2029](https://www.faa.gov/sites/faa.gov/files/airports/planning_capacity/npias/current/ARP-NPIAS-2025-2029-Narrative.pdf "Table 3, FY 2022")
- Globally, 68% of airports operating at a net loss handle fewer than 1 million passengers (ACI World). In Europe, Oxera/ACI Europe (2024) confirmed that airports under 1M passengers are broadly unable to achieve consistent profitability, a finding underpinning EU Aviation State Aid Guidelines that permit operating aid to airports under 3M passengers through April 2027. [ACI World 2025](https://aci.aero/2025/04/28/airports-face-financial-challenges-despite-air-traffic-rebound-aci-world-economics-report-reveals/ "FY 2023 data") and [Oxera/ACI Europe 2024](https://www.oxera.com/insights/reports/economic-analysis-of-the-profitability-of-regional-airports/ "regional airport profitability")
- Proportionality varies dramatically by context: Yellowknife Airport's 1,001 direct FTE = 4.4% of local employment; Montrose's 2,850 total jobs = 13–14% of county employment (tourism outlier). For a non-tourism 500K airport serving a 250K–500K metro area, 300–600 direct on-airport jobs represent <0.5% of regional employment — economically meaningful but not dominant.
- National context: FAA 2024 reports U.S. civil aviation supported $1.8T in output and 9.4M jobs (4.0% of GDP) in 2022; airport operations specifically contributed $48.1B in value-added. ACI-NA 2024 reports 487 airports support 12.8M total jobs and $1.844T total output. [FAA 2024](https://www.faa.gov/2024-economic-impact-report.pdf "2022 data") and [ACI-NA 2024](https://www.mvcommission.org/sites/default/files/docs/ACI-NA-The-Economic-Impact-of-U.S.-Commercial-Service-Airports-in-2024.pdf "Table 2")

### 可用图片
- None identified (Colorado CEIS infographics are embedded in PDFs, not extractable)

### 仍需补充
- No airport-size-tier breakdown in FAA or ACI-NA national reports; per-1,000-enplanement ratios are system-wide averages
- NPIAS nonhub category spans 10K–472K enplanements; a 250K-enplanement airport sits at the upper end and differs substantially from the category average
- Full Oxera 2024 report on European regional airport profitability is paywalled; 500K-band-specific data not obtained
- Most available state studies with 500K-airport data feature tourism-heavy airports; non-tourism 500K airports are underrepresented
- Tax/fiscal data at the individual 500K-airport level is sparse outside the Yellowknife study

---

## Chapter 4：Indirect, Induced, and Catalytic Economic Effects

### 研究目标
- Report employment and output multiplier magnitudes for small/regional airports and compare to large-hub multipliers
- Assess supply-chain (indirect) effects and local spending leakage rates
- Quantify tourism facilitation: visitor arrivals attributable to air access, visitor spending
- Evaluate trade/cargo relevance at the 500K scale
- Examine catalytic effects: FDI attraction, business location decisions linked to air connectivity

### 关键发现
- Yellowknife Airport (532K pax, 2014) employment multiplier was 2.07 (1,001 direct → 2,072 total jobs); the 2024 InterVISTAS update using narrower NWT-only scope yielded lower multipliers (~1.27–1.48). ACI-NA system-wide employment multiplier (1.96) likely overstates the effect at small airports. FAA 1992 guide shortcut multipliers for communities <100K pop = 0.5; 100K–500K = 0.6 — meaning indirect + induced effects equal only 50–60% of direct effects at typical 500K-airport catchments. A Wisconsin study reported 1.27 sales / 1.5 employment multipliers. [Yellowknife EIS 2015](https://www.inf.gov.nt.ca/sites/inf/files/resources/final_economic_impact_analysis_14-12-15_5.pdf "Table E-5"), [YZF 2024](https://www.inf.gov.nt.ca/sites/inf/files/resources/facilitating_economic_and_social_connectivity_yzf_final_13sep2024.pdf "Figure 1-2"), [FAA 1992](https://gardnermagazine.com/wp-content/uploads/2024/02/Airports-1992-Report-dot_35802_DS1.pdf "Step 5")
- Pot & Koster (2022) studied 274 European NUTS-2 regions (2000–2018) and found GDP-per-capita elasticity to air accessibility of 0.022 for small airports (<1M pax) vs. 0.179 for large airports (>5M) — small airports produce roughly one-eighth the GDP elasticity. In 67% of regions, causality ran from GDP to small-airport accessibility, not the reverse. Only in lagging but densely populated regions did small airports show evidence of being a "pillar of growth." [Pot & Koster 2022](https://www.researchgate.net/publication/357405362_Small_airports_Runways_to_regional_economic_growth "J. Transport Geography 98, Table 8")
- At MTJ (Colorado), off-airport visitor spending generated 70% of total jobs (2,002 of 2,850) and 64% of total business revenues ($210.9M of $327.3M). The 2025 CEIS updated to 4,323 total jobs and $713.1M revenues. Other Colorado airports at ~500K: DRO 1,993 jobs / $342.1M; GUC 958 jobs / $154.9M — all tourism-dominated. For non-tourism 500K airports, the FAA 1992 AP/POP test suggests visitor expenditures may be negligible. [CEIS 2020 MTJ](http://www.coloradoaviationsystem.com/wp-content/uploads/2024/09/Montrose-Regional-MTJ.pdf "MTJ impacts") and [2025 CEIS](http://www.coloradoaviationsystem.com/wp-content/uploads/2025/02/CEIS-Executive-Summary_FINAL_021925.pdf "individual airport table")
- ACRP Report 218 (Ballard et al. 2020) found each departing seat at a nonhub airport is associated with 0.0114 regional jobs — over twice the rate at small-hub airports (0.005). A daily 100-seat departure (36,500 annual seats) at a nonhub would support ~416 regional jobs. Bilotkach (2015) found that the number of nonstop destinations matters more than capacity to existing destinations — each new nonstop created 223 jobs and 15 new establishments. [ACRP Web Resource 12](https://crp.trb.org/acrpwebresource12/understanding-air-service-and-regional-economic-activity/the-role-of-aviation-in-supporting-local-economic-activity/ "citing ACRP 218 and Bilotkach 2015")
- Brueckner (2003): 10% increase in enplanements → 0.9% increase in MSA employment; Blonigen & Cristea (2015): 50% increase in air traffic growth → 5.5% increase in annual employment growth and 7.4% of GDP in cumulative income over 20 years (using 1978 deregulation as quasi-experiment); Sheard (2014): 10% air traffic increase → ~1,650 additional service jobs in a 1M-population MSA, but no effect on manufacturing. McGraw (2020): airports contributed 3.9% employment growth and 3.4% population growth per decade in mid-size cities over 1950–2010. [Blonigen & Cristea 2015](https://pages.uoregon.edu/cristea/Research_files/airurban.pdf "J. Urban Economics 86") and [ACRP Web Resource 12](https://crp.trb.org/acrpwebresource12/understanding-air-service-and-regional-economic-activity/the-role-of-aviation-in-supporting-local-economic-activity/ "citing Brueckner 2003, Sheard 2014, McGraw 2020")
- Tveter (2017) found no significant employment effect from the construction of nine regional airports in Norway (1970–72) in a difference-in-differences study. Breidenbach (2020) found no effect in Germany. Evidence from Australia and New Zealand (Baker et al. 2015; Fu et al. 2021) is more positive. This geographic heterogeneity suggests that small-airport impacts depend on transportation alternatives (rail/road), airport-network density, and local economic context. [Pot & Koster 2022](https://www.researchgate.net/publication/357405362_Small_airports_Runways_to_regional_economic_growth "citing Tveter 2017, Breidenbach 2020, Baker et al. 2015")
- Most 500K-pax airports handle minimal dedicated cargo; regional jets have limited belly capacity. Yellowknife is a niche exception (diamond mining resupply, Det'on Cho Logistics). RAA reports 570 U.S. small community airports collectively generate $134B in annual economic activity and 1M jobs. [RAA 2024](https://raa.org/valuable-service-air-service-to-small-communities-generates-significant-economic-activity/ "November 2024") and [YZF 2024](https://www.inf.gov.nt.ca/sites/inf/files/resources/facilitating_economic_and_social_connectivity_yzf_final_13sep2024.pdf "cargo case study")

### 可用图片
- None identified

### 仍需补充
- No airport-size-tier-specific multiplier tables in FAA or ACI-NA national reports; gap between system-wide multipliers (1.96) and likely small-airport multipliers (0.5–0.6 FAA shortcut) is not directly quantified by tier
- Tourism vs. non-tourism airport distinction is critical but underspecified in most studies; MTJ's 70% visitor-share is not generalizable
- Cargo tonnage data for individual 500K airports is sparse; Yellowknife is an outlier, not representative
- Causal-inference studies (Brueckner, Sheard, Blonigen & Cristea) cover all airport sizes, not specifically the 500K band; ACRP 218's nonhub finding is associational, not causally identified
- European evidence (Pot & Koster, Tveter) is more pessimistic than North American evidence — geographic heterogeneity needs explicit acknowledgment

---

## Chapter 5：Broader Socioeconomic and Connectivity Effects

### 研究目标
- Measure connectivity: route networks, frequency, hub connectivity, accessibility indices typical of 500K airports
- Assess real estate and land-use effects near small regional airports (accessibility premium vs. noise discount)
- Examine population dynamics: evidence on whether air service helps retain population in rural/peripheral regions
- Evaluate healthcare access (medical evacuation, patient transfer) and educational/labor mobility roles
- Address social equity and spatial justice arguments

### 关键发现
- Cherry Capital Airport (TVC, ~787K pax in 2024) offers 7 airlines and ~20 nonstop destinations (Chicago, Dallas, Denver, Atlanta, Minneapolis, JFK/LGA, Newark), illustrating a successful connectivity profile near the 500K threshold. The GAO (2024) found that the 218 smallest U.S. communities' mean connectivity index declined 8% from 2018–2023 (5.1→4.7), remaining ~1% of large-community connectivity. [TVC airlines page](https://tvcairport.com/airlines-serving-cherry-capital-airport/ "accessed June 2025") and [GAO-24-106681](https://files.gao.gov/reports/GAO-24-106681/index.html "September 2024")
- From 2000–2018, departures from nonhub airports fell 47% vs. 7% at large hubs (GAO). The CAC/InterVISTAS (2025) report found Canadian regional airport frequencies at 64% of 2014 levels, with IATA Connectivity Index showing 10.1% domestic decline from 2019 to 2024. A single regional flight in Canada generates 126–210 total jobs and $11.4–$19.5M in GDP annually. [GAO-24-106681](https://files.gao.gov/reports/GAO-24-106681/index.html "departure trends") and [CAC/InterVISTAS 2025](https://airportscouncil.org/wp-content/uploads/2025/05/2025CACConnectivityReport-Full.pdf "Keeping Canada Connected, May 2025")
- Nelson (2004) meta-analysis of 33 hedonic studies across 23 airports: Noise Depreciation Index of 0.58% per dB (0.8–0.9% in U.S., 0.5–0.6% in Canada). At 500K airports with modest traffic (10–30 daily departures of regional jets), the 65-dB noise contour is dramatically smaller than at major hubs, shifting the balance toward an accessibility premium rather than a noise discount. [Nelson 2004 via SJSU thesis](https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=4616&context=etd_theses "meta-analysis of 33 studies") and [Applied Economics 2025](https://www.tandfonline.com/doi/full/10.1080/00036846.2025.2547105 "heterogeneous dual effect")
- McGraw (2020): airport presence contributed 3.9% employment growth and 3.4% population growth per decade in mid-size cities over 1950–2010. But Tveter (2017) found no statistically significant population/employment effect from nine Norwegian regional airports (1970–72), and Pot & Koster (2022) found causality mostly runs from economy to airport for small airports. [ACRP Web Resource 12](https://crp.trb.org/acrpwebresource12/understanding-air-service-and-regional-economic-activity/the-role-of-aviation-in-supporting-local-economic-activity/ "McGraw 2020") and [Pot & Koster 2022](https://www.researchgate.net/publication/357405362_Small_airports_Runways_to_regional_economic_growth "Table 8")
- Air ambulances serve 550,000+ patients/year in the U.S.; 80+ rural hospitals have closed since 2010, with 700 more at risk by 2028. Only one-third of U.S. geographic area is within 15–20 min helicopter response, though 86% of population is covered. At Yellowknife, Advanced Medical Solutions (350 employees) uses YZF as its air ambulance hub. In Canada, BC issued 98,000 medical travel approvals and Ontario 200,000 in 2023–24. [Ahmed et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9285155/ "AMIA 2022") and [CAC/InterVISTAS 2025](https://airportscouncil.org/wp-content/uploads/2025/05/2025CACConnectivityReport-Full.pdf "medical access section") and [YZF 2024](https://www.inf.gov.nt.ca/sites/inf/files/resources/facilitating_economic_and_social_connectivity_yzf_final_13sep2024.pdf "AMS case study")
- Yellowknife Airport was critical during 2023 NWT wildfires: 195 aircraft deployed for evacuation. Det'on Cho Logistics (100% Indigenous-owned, primary FBO at YZF) coordinated the operation and has since signed a standing emergency agreement. During COVID-19, Det'on Cho redeployed staff to transport medical supplies and vaccines to remote communities. [YZF 2024 Study](https://www.inf.gov.nt.ca/sites/inf/files/resources/facilitating_economic_and_social_connectivity_yzf_final_13sep2024.pdf "Det'on Cho case study")
- The GAO (2024) found EAS communities experienced smaller connectivity declines (4% vs. 10%) than non-EAS communities. However, community members value EAS service at only $16M/year vs. program costs of $290M+ — and many EAS residents drive to larger airports instead (willingness to travel up to 80 miles). As of March 2024, 107 contiguous U.S. communities received EAS subsidies averaging $4.3M each. [GAO-24-106681](https://files.gao.gov/reports/GAO-24-106681/index.html "EAS valuation and usage data")
- Service Canada outreach teams conducted 1,280 visits to 646 Indigenous communities in 2019–20 relying on regional airports. CAC frames regional airports as instruments of spatial equity enabling economic development, social connectivity, emergency response, government service delivery, and medical/educational access. [CAC/InterVISTAS 2025](https://airportscouncil.org/wp-content/uploads/2025/05/2025CACConnectivityReport-Full.pdf "government services and equity sections")

### 可用图片
- None identified

### 仍需补充
- Hedonic pricing studies specific to small (~500K) airports are sparse; noise-footprint argument is inferred from operations data, not directly measured at this scale
- No data on income distribution of travelers at 500K airports to evaluate equity claims
- No study directly links health outcomes (mortality, morbidity) to presence/absence of a specific small regional airport
- European spatial justice literature for airports at the 500K threshold not located
- Causal chain from airport presence to individual migration decisions is under-documented in peer-reviewed literature at this scale

---

## Chapter 6：Case Studies — Documented Impacts at or Near the 500K Threshold

### 研究目标
- Present 4–6 case studies of airports in the 300K–700K passenger range with published economic impact assessments
- Cover at least 3 geographic regions: US, Europe, Australia/Asia-Pacific, developing/island economies
- Extract quantified metrics: jobs, GDP contribution, multiplier, visitor spending per case
- Build a cross-case comparison table identifying patterns and outliers

### 关键发现
- **Rapid City Regional (RAP), South Dakota, USA** (~677K pax, 2022): 456 direct on-airport jobs; 2,877 total jobs; $456M output; $251M GDP (5.5% of county GDP); $2.2M annual tax revenue. Visitor spending: $198M direct. IMPLAN-based study with 7,537-response intercept survey. Peer comparison: similar airports (Trenton-Mercer, Baton Rouge, South Bend, Fort Wayne at 338K–428K enplanements) ranged from $167M–$580M output and 1,115–4,738 jobs, showing wide variation driven by tourism vs. business context. [RAP Economic Impact Study](https://rapairport.com/wp-content/uploads/2024/01/RAP-Economic-Impact-Study-Final-2024.pdf "GVSU Seidman Center, November 2023")
- **Inverness Airport (INV), Scottish Highlands, UK** (875K pax, 2017): 554 direct FTEs; 2,522 total FTEs (748 on-site + 1,774 visitor-related); £93.3M total GVA (£33.3M on-site + £60M visitor); £43M time-savings value. Average direct wage £34,200/FTE, above Scottish average. More passengers are inbound than outbound (tourism gateway to Scottish Highlands). On-site employment multiplier ~1.35x; visitor channel dominates. HIAL (operator of 11 airports) received £50.7M public subsidy in FY2023/24. [Inverness Airport EIS](https://www.hie.co.uk/media/3003/economicplusandplussocialplusimpactplusofplusinvernessplusairportplus-plusexecutiveplussummary.pdf "ekosgen for HIE/HIAL, September 2018")
- **Queenstown Airport (ZQN), New Zealand** (653K pax, 2007): 377 on-airport employees; 2,717 total FTEs; NZ$368M output; NZ$162M GDP (2.5% of Otago Region GDP). International visitors: $150.5M NZD spending, average $810/visit (7.9 nights); domestic visitors: $54.3M, average $445/visit (3.1 nights). Effective employment multiplier ~7.2x including facilitated visitor activity. 97% of regional GDP contribution from visitor spending. Data vintage note: Queenstown now handles 2.7M pax. [Queenstown Airport EIA](https://www.qldc.govt.nz/media/obkpvzhu/appendix_4.pdf "Market Economics Ltd, December 2008")
- **Fiji/Nadi (illustrative island-economy case)**: Aviation supports 51,400 jobs and $1.2B GDP (21.8% of national GDP). Tourism facilitated by air accounts for $1.0B GDP and 39,600 jobs. 4,100 direct aviation jobs generate $63.3M output. Nadi handles ~2.35M total pax (exceeds 500K, but included because Fiji's 13 outer-island airports individually serve small volumes, and IATA/Oxford data is the best-documented SIDS case). [IATA Value of Air Transport to Fiji](https://www.iata.org/en/iata-repository/publications/economic-reports/the-value-of-air-transport-to-fiji/ "IATA/Oxford Economics, 2023") and [Fiji Airports AR 2022](https://parliament.gov.fj/wp-content/uploads/2025/04/Fiji-Airports-Annual-Report-2022.pdf "Fiji Airports Ltd")
- **Ballina Byron Gateway (BNK), Australia** (~620K pax): No standalone published EIA available. Airport operating revenue ~AUD $8.2M. Serves Byron Bay tourism hinterland (~45K pop Ballina Shire). Completed $20.68M terminal upgrade. Deloitte/AAA national benchmarks: Queensland airports facilitated $6.5B value-added and 49K FTEs from domestic tourism alone. Included as contextual evidence only. [Deloitte "Taking Flight" 2023](https://airports.asn.au/wp-content/uploads/2023/11/Deloitte-Taking-flight_The-economic-and-social-importance-of-Australias-Airports.pdf "Deloitte for AAA, November 2023")
- **Cross-case synthesis**: Airports at 300K–700K passengers consistently generate 250–600 direct on-airport jobs and 2,000–3,000 total jobs. Total-jobs-per-1,000-pax ratio: 2.9–5.1 (tourism airports at high end). On-airport multiplier: 1.3–1.9x; including visitor-facilitated employment: 6–7x. Visitor spending accounts for 50–80% of total impact at tourism gateways. GDP share: 2.5–5.5% of local/regional economy in developed countries, up to 21.8% for island developing states. Context matters enormously: peripheral/isolated communities amplify impacts due to lack of transport alternatives; tourism gateways are visitor-spending-dominated and seasonal; island economies show existential aviation dependence.

### 可用图片
- None identified

### 仍需补充
- Ballina Byron Gateway lacks a formal published EIA with quantified employment/GDP/multiplier data
- No individual Scandinavian airport-level EIA near 500K was found; Avinor reports are system-wide only; SPARA 2020 project produced methodology guidance but not individual airport assessments
- Fiji/Nadi exceeds the 500K threshold; included as illustrative island-economy case, not strict comparator
- Queenstown data is from 2007 (airport now at 2.7M pax); valid for illustrating ~650K-pax dynamics but vintage noted
- Currency/temporal comparability across cases is imprecise (2007–2023, USD/NZD/GBP/FJD); employment and proportionality metrics are more reliably comparable

---

## Chapter 7：Counterarguments, Limitations, and Conditions for Impact

### 研究目标
- Examine financial viability and subsidization issues (EAS, PSO, per-passenger subsidy levels)
- Present methodological critiques of airport economic impact studies (double-counting, inflated multipliers, attribution errors)
- Assess environmental externalities (carbon, noise, air quality) and whether they offset economic benefits
- Evaluate opportunity-cost arguments: alternative uses of public investment
- Document airports near 500K that underperformed expectations
- Synthesize moderating conditions that determine whether a 500K airport generates significant impact

### 关键发现
- EAS program cost ~$598M in FY2025 for 108 communities; average subsidy per community rose from $3.2M to $4.3M (2018–2023 in real dollars). Drukker (2023) found communities collectively value EAS at only $16M/year vs. program costs >$290M — a cost-benefit ratio of ~18:1 against. 57% of EAS users are nonresidents; nonresidents have higher median incomes ($62,800 vs. $53,400), raising distributional concerns. Most EAS residents drive to larger airports (in Decatur, IL, only 7% used the local EAS airport). [GAO-26-107751](https://www.gao.gov/assets/gao-26-107751.pdf "GAO, December 2025") and [Drukker 2023](https://rosap.ntl.bts.gov/view/dot/68535/dot_68535_DS1.pdf "University of Arizona, May 2023")
- European PSO routes: ERA (2024) documented 150+ PSO routes across 14 airlines in 11 countries, with wide variation in compensation methods and fare caps. Spain offers 75% resident discounts on Canary Islands flights; Italian Sicilian PSOs require 20,000 free seats/year for medical transport. EU State Aid Guidelines permit operating aid for airports <3M pax through April 2027; Oxera/ACI Europe (2024) confirms airports <1M pax cannot achieve consistent profitability. [ERA PSO Study 2024](https://eraa.org/wp-content/uploads/2025/04/era_pso_report_june_2024_final_5_june.pdf "ERA, June 2024") and [Oxera 2024](https://www.oxera.com/insights/reports/economic-analysis-of-the-profitability-of-regional-airports/ "for ACI Europe")
- Forsyth & Niemeier (2016): "EIA should not be used to assess decisions on investment, night curfews and subsidies for regional airports" — direct+indirect effects are proportional to cost, induced effects are investment-agnostic, substitution/price effects are neglected. Catalytic impact estimates range 25%–177% of direct jobs. 27% of U.S. commercial airports lack observed (vs. modeled) impact data. NEF (UK, 2025): government "is unable to produce evidence that growing airports will grow the economy"; business air travel demand is declining and tourism outflows may exceed inflows. [Forsyth & Niemeier 2016](http://www.verkehrskonferenz.de/fileadmin/archiv/konferenz_2016/Papers/forsyth_et_al-wider_economic_benefits_or_catalytic_effects_of_air_transport.pdf "Wider Economic Benefits") and [NEF 2025](https://neweconomics.org/2025/10/government-failed-to-produce-evidence-for-airport-expansion-growth-claims "October 2025")
- Pot & Koster (2022): for small airports (<1M pax), GDP elasticity is only 0.022; causality mostly runs economy→airport. "A purely economic cost-benefit analysis will, in most cases, wind up with a negative result" for small regional airports. Discussion should center on societal interests (accessibility, regional identity, air ambulance) rather than economic ones. Tveter (2017): no significant employment effect from 9 Norwegian regional airports. [Pot & Koster 2022](https://www.rug.nl/news/2022/01/regional-airports-often-not-a-booster-of-economic-growth?lang=en "University of Groningen, January 2022")
- ICCT (2020): regional aircraft emit ~162g CO₂/RPK (~80% above global average). Estimated annual carbon footprint for a 500K-pax airport: ~65,000 tonnes CO₂ (~$3.25M social cost at $50/tonne). Turboprops are ~15% less carbon-intensive than regional jets. Noise impacts at 500K airports are substantially smaller than at major hubs due to 10–30 daily departures vs. hundreds — Nelson (2004) NDI of 0.58%/dB applies to a much smaller geographic footprint. [ICCT 2020](https://theicct.org/wp-content/uploads/2021/06/CO2-commercial-aviation-oct2020.pdf "October 2020")
- GAO (December 2025): nonhub daily departures per route declined 19% from 2018–2024; non-EAS nonhubs fell 21%. Airlines now demand $1.5–$2M revenue guarantees per route (doubled since pandemic). SCASDP grants ($12M for 14 communities in FY2023) are oversubscribed 3:1. EAS creates market distortion: airlines may shift resources from marginal non-EAS airports to guaranteed-revenue EAS markets. [GAO-26-107751](https://www.gao.gov/assets/gao-26-107751.pdf "December 2025")
- Documented underperformance cases: Dubuque (DBQ) lost 94% of departures per route (2018–2024), funded $1.9M revenue guarantee exhausted by May 2025; Springfield (SPI) lost 90% of catchment travelers to other airports, Breeze A220 service scaled back after insufficient demand; Wenatchee (EAT) dropped from 7 daily flights to much less after smaller aircraft retired. Nordica abandoned Groningen–Munich/Copenhagen routes due to low load factors and hub competition. [GAO-26-107751](https://www.gao.gov/assets/gao-26-107751.pdf "case studies") and [ERA 2024](https://eraa.org/wp-content/uploads/2025/04/era_pso_report_june_2024_final_5_june.pdf "Nordica case")
- Opportunity cost: 330 nonhub airports received $1.437B in grants (FY2022), exceeding their ~$1.377B operating revenue. Average grant per nonhub (~$4.4M) exceeds average operating revenue (~$4.2M). The question of whether equivalent investment in roads, broadband, or healthcare would yield greater returns for the same communities is raised but not definitively answered in the literature. [FAA NPIAS 2025–2029](https://www.faa.gov/sites/faa.gov/files/airports/planning_capacity/npias/current/ARP-NPIAS-2025-2029-Narrative.pdf "Table 3")
- **Moderating conditions synthesis**: (1) Geographic isolation is the strongest moderator — only in lagging but densely populated regions do small airports show growth stimulus. (2) Tourism dependence dramatically amplifies impact (RAP $456M vs. Springfield near-zero). (3) Hub connectivity quality matters more than frequency; route diversity (nonstop destinations) drives economic effects. (4) Catchment leakage: airports within 2–3 hours of a large hub lose 60–90% of travelers. (5) Surface transport alternatives reduce the marginal value of air service. (6) State-level support structures (WY capacity purchase, MI Air Service Program, local lodging taxes) can be decisive. [GAO-26-107751](https://www.gao.gov/assets/gao-26-107751.pdf "moderating factors") and [Pot & Koster 2022](https://www.researchgate.net/publication/357405362_Small_airports_Runways_to_regional_economic_growth "conditions for growth")

### 可用图片
- None identified

### 仍需补充
- No comprehensive cross-national PSO cost-per-passenger database; ERA study documents institutional arrangements but not aggregate EU-wide expenditure
- No direct airport-vs-alternative-infrastructure investment return comparison at the 500K scale in peer-reviewed literature
- Social cost of carbon estimate ($3.25M/year) is rough approximation; airport-specific carbon data at this scale is rare
- Noise cost monetization specific to small airports is poorly studied; the minimal-impact inference rests on smaller noise contours, not direct measurement
- No single unified study examines all moderating conditions together; the synthesis draws on multiple geographies and methodologies

---

# Section 2：给 Write 阶段的执行建议

## Language and Terminology
- All prose, headings, chart titles, axis labels, figure captions, and table headers in English.
- Primary metric term: **"annual passenger throughput"**. On first use, clarify relationship to "enplanements" (FAA, ~half of throughput), "passenger movements" (arrivals + departures = throughput), and "passengers per annum" (UK/AU usage). After the definitional paragraph, use "passenger throughput" or "passengers" consistently.
- Formal prose: **"500,000 passengers"**, not "500K pax" or "0.5 million." Abbreviation "500K" acceptable in chart labels and tables only.
- Standard term: **"airport economic impact study/studies"** (not "assessment" or "benefit analysis").

## Source Credibility and Verification
- All multiplier values, employment ratios, GDP figures, and per-passenger economic output estimates must come from T1/T2 sources (FAA/ACI/ATAG publications, peer-reviewed papers, GAO/audit reports, official airport economic impact studies).
- Tourism spending estimates require explicit methodological disclosure (passenger surveys, visitor expenditure models, or national tourism statistics).
- Claims about the number of airports globally/nationally in the 500K range must cite the specific database year (e.g., ACI World Traffic Database 2024, FAA NPIAS 2025).
- Case study data must cite the specific published study with publication year and commissioning body; airport marketing materials or press releases are insufficient as sole sources.

## Cross-Chapter Coherence
- The "four-tier impact taxonomy" (direct / indirect / induced / catalytic) introduced in Chapter 2 must be the organizing framework for Chapters 3, 4, and 5. No ad hoc impact categories.
- If Chapter 2 defines "direct employment" in a specific way, Chapters 3 and 6 must use that same definition. Flag any definitional discrepancies between FAA and European standards.
- Multiplier values used illustratively in Chapter 2 must be consistent with those in Chapter 4 and applied in Chapter 6. Note discrepancies if different studies use different methodologies.
- Chapter 7 methodological critiques must reference the specific methods described in Chapter 2.

## Analytical Tone
- Evidence review, not advocacy. Present supportive and critical evidence with equal rigor.
- Avoid promotional language ("vital economic engines," "indispensable lifelines") unless directly quoting and attributing.
- Avoid empty hedging ("may or may not be significant"). State what evidence shows and note its limitations.
- Quantitative claims must include all five elements: subject, time period, unit, value, source citation.

## Time Scope
- Current date: 2026-04-09. Research covers the most recent available evidence and historical studies that remain relevant. No fixed time-range constraint, but preference for post-2015 data with pre-2015 seminal works included where foundational.
