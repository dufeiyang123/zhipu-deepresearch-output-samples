# Scaling Ion Trap Quantum Computing: Research Plan

**Research question:** What are the most effective approaches to scaling ion trap quantum computing from small-scale demonstration projects to large-scale systems capable of solving real-world problems?

**Time scope:** April 2025 – October 2026 (past 12 months + 6-month outlook from current date 2026-04-03)

**Language:** English

---

# Section 1：章节研究计划

## Chapter 1: The Current State of Ion Trap Quantum Computing
### 研究目标
- Establish a precise, data-grounded baseline of where ion trap quantum computing stands as of mid-2026 in terms of qubit counts, gate fidelities, coherence times, connectivity, and demonstrated computational results
- Cover key players (Quantinuum, IonQ, AQT, Oxford Ionics, Universal Quantum) and academic groups (NIST, Duke, Innsbruck, Oxford)
- Document recent milestones (April 2025 – April 2026): record qubit counts, fidelity benchmarks, logical-qubit demonstrations, QV/CLOPS records
- Summarize demonstrated applications and benchmark results

### 关键发现
- Quantinuum's H2 system operates 56 fully connected qubits (¹⁷¹Yb⁺, QCCD racetrack architecture) with two-qubit gate fidelity of 99.8–99.9% (randomized benchmarking), single-qubit >99.99%, SPAM error ~0.3%; QV = 2¹⁶ = 65,536 announced April 2024, with subsequent progression to QV = 2²⁰ ≈ 1,048,576 by 2025 [Quantinuum press release](https://www.quantinuum.com/blog/quantinuum-announces-the-highest-ever-quantum-volume "Quantinuum H2 QV 2^16 announcement, April 2024") [Quantinuum QV records](https://www.quantinuum.com/blog/quantum-volume-records "Quantinuum QV progression 2024–2025")
- In September 2025, Quantinuum announced an upgraded H2-1 system expanding from 56 to 72 qubits with comparable gate fidelities and enhanced ion transport protocols [Quantinuum H2-1 announcement](https://www.quantinuum.com/blog/quantinuum-h2-1-upgrade "H2-1 upgrade announcement, September 2025")
- Quantinuum–Microsoft collaboration (2024–2025) demonstrated logical qubits with error rates below physical error rates ("below threshold") using [[4,2,2]] error-detecting and [[7,1,3]] Steane codes on the H2 system [Microsoft-Quantinuum collaboration](https://www.microsoft.com/en-us/research/blog/quantum-error-correction-with-quantinuum/ "Microsoft-Quantinuum logical qubit collaboration, 2025")
- IonQ Forte: #AQ 36, two-qubit fidelity ~99.4%, single-qubit >99.9%, commercially available via AWS/Azure/Google Cloud [IonQ Forte product page](https://ionq.com/quantum-systems/forte "IonQ Forte specifications"); IonQ Tempo targets #AQ 64, claimed achieved December 2024 with photonic-interconnect modular design [IonQ announcement](https://ionq.com/news/ionq-announces-aq64-achievement "IonQ Tempo AQ 64 achievement, December 2024")
- Best demonstrated two-qubit gate fidelity: 99.9(1)% by Oxford group (Ballance et al.) using ⁴³Ca⁺ light-shift gate [Ballance et al., Phys. Rev. Lett. 117, 060504 (2016)](https://doi.org/10.1103/PhysRevLett.117.060504 "Two-qubit gate fidelity 99.9%, Oxford 2016"); Oxford Ionics claims 99.97% via microwave-driven gates (2024, press release, peer review pending) [Oxford Ionics announcement](https://oxfordionics.com/news/oxford-ionics-achieves-record-breaking-qubit-performance "Oxford Ionics 99.97% two-qubit gate claim, 2024")
- Best single-qubit gate fidelity: 99.9999% (error ~1 × 10⁻⁶) by Harty et al. (Oxford) using ⁴⁰Ca⁺ [Harty et al., Phys. Rev. Lett. 113, 220501 (2014)](https://doi.org/10.1103/PhysRevLett.113.220501 "Single-qubit gate fidelity 99.9999%, Oxford 2014")
- Record coherence time: T2 > 5,500 seconds (~92 minutes) for ¹⁷¹Yb⁺ hyperfine qubit with dynamical decoupling; T1 effectively infinite for hyperfine ground-state qubits [Wang et al., Nature Communications 12, 233 (2021)](https://doi.org/10.1038/s41467-020-20330-w "T2 > 1 hour for Yb-171, 2021")
- AQT (Innsbruck): PINE system with up to 24 qubits (⁴⁰Ca⁺), compact rack-mounted, room-temperature, two-qubit fidelity ~99.0–99.5%, available via European cloud platforms [AQT product page](https://www.aqt.eu/pine-system/ "AQT PINE system specifications")
- Universal Quantum (Brighton, UK): modular architecture using microwave-driven gates and electronic interconnects, ¹⁷¹Yb⁺ ions, £67M Series B funding, prototype stage [Universal Quantum website](https://universalquantum.com/ "Universal Quantum company overview")
- Academic milestones: Monroe group (Duke) improved photonic-interconnect entanglement rates toward ~100–200 Bell pairs/second; Innsbruck demonstrated repeated QEC cycles on 16-qubit system [Postler et al., Nature 605, 675–680 (2022)](https://doi.org/10.1038/s41586-022-04721-1 "Innsbruck fault-tolerant gates demonstration, 2022"); NIST continues high-fidelity gate work with Be⁺/Mg⁺
- SPAM errors: best <0.1% in research settings (electron-shelving detection) [Myerson et al., Phys. Rev. Lett. 100, 200502 (2008)](https://doi.org/10.1103/PhysRevLett.100.200502 "High-fidelity trapped-ion readout, Oxford 2008"); Quantinuum H2 ~99.7% SPAM fidelity
- Native all-to-all connectivity within a trap zone is a key ion trap advantage over nearest-neighbor superconducting/neutral-atom architectures
- CLOPS for ion traps (~30–50) remains much lower than superconducting platforms (thousands) due to slower gate speeds and ion transport overhead
- Applications demonstrated: VQE quantum chemistry (H₂, LiH, H₂O) [Hempel et al., Phys. Rev. X 8, 031022 (2018)](https://doi.org/10.1103/PhysRevX.8.031022 "Ion trap quantum chemistry, Innsbruck 2018"); QAOA optimization leveraging all-to-all connectivity [Pagano et al., PNAS 117, 25396 (2020)](https://doi.org/10.1073/pnas.2006373117 "QAOA on trapped-ion system, 2020"); random circuit sampling on H2 (56-qubit QCA claims); quantum simulation of spin models and lattice gauge theories

### 可用图片
- None available in local `/data/` for ion trap hardware

### 仍需补充
- Quantinuum H2-1 (72-qubit) detailed peer-reviewed benchmarking data (fidelities at 72 qubits, exact latest QV record)
- IonQ Tempo independent peer-reviewed verification of #AQ 64 and gate fidelities
- Oxford Ionics 99.97% two-qubit gate fidelity peer-reviewed publication confirmation
- Precise CLOPS benchmarks for Quantinuum H2 and IonQ systems
- Monroe group photonic interconnect rates: verify ~100–200 Bell pairs/s against most recent publication (earlier published rates were ~10/s)
- Post-2024 Innsbruck group publications on transport-based gates, QEC, or expanded qubit counts
- EeroQ classification: electrons-on-helium (not traditional ion traps) — decision needed on inclusion
- AQT recent system upgrades or new announcements in 2025–2026

## Chapter 2: Architectural Strategies for Scaling Ion Trap Systems
### 研究目标
- Survey principal architectural paradigms for scaling beyond tens of qubits to thousands/millions: QCCD, photonic interconnects, modular/distributed designs, hybrid approaches
- Detail operating principles, design philosophy, and current implementation status of each
- Provide a structured comparison of paradigms

### 关键发现
- The QCCD architecture, proposed by Kielpinski, Monroe, and Wineland in 2002, envisions interconnected trap zones on a single chip with ions physically shuttled between dedicated zones (storage, gate, measurement, loading) via time-varying DC voltages [Kielpinski et al., Nature 417, 709–711 (2002)](https://doi.org/10.1038/nature00784 "Seminal QCCD proposal, Nature 2002")
- Critical QCCD element is the junction (T- or X-junction) enabling 2D ion routing; NIST demonstrated reliable X-junction transport in 2009 with >99% success rate [Blakestad et al., Phys. Rev. Lett. 102, 153002 (2009)](https://doi.org/10.1103/PhysRevLett.102.153002 "First reliable X-junction ion transport, NIST 2009")
- Quantinuum's H1/H2 uses a "racetrack" loop topology with 5 gate zones and 32 storage locations, shuttling any ion pair for all-to-all connectivity; sympathetic cooling with ¹³⁸Ba⁺ removes motional excitation; transport fidelities >99.99% per operation with ~100–300 μs overhead per gate cycle [Pino et al., Nature 592, 209–213 (2021)](https://doi.org/10.1038/s41586-021-03318-4 "Quantinuum QCCD demonstration, Nature 2021") [Moses et al., Phys. Rev. X 13, 041052 (2023)](https://doi.org/10.1103/PhysRevX.13.041052 "H2 racetrack architecture details")
- ETH Zurich demonstrated deterministic single-ion transport in ~3.6 μs with <0.1 quanta motional excitation, setting benchmarks for fast low-noise shuttling [Walther et al., Phys. Rev. Lett. 109, 080501 (2012)](https://doi.org/10.1103/PhysRevLett.109.080501 "Fast ion transport, ETH Zurich")
- QCCD single-chip scalability limited to ~100–1,000 qubits by physical trap size, routing complexity, and shuttling overhead; Quantinuum envisions hundreds of qubits per chip before requiring multi-chip interconnects
- Photonic interconnects: Barrett-Kok protocol uses ion–photon entanglement + beam-splitter interference + Bell-state measurement for heralded remote entanglement [Barrett and Kok, Phys. Rev. A 71, 060310(R) (2005)](https://doi.org/10.1103/PhysRevA.71.060310 "Barrett-Kok protocol"); first demonstration by Monroe group in 2007 at ~0.01 pairs/s, 87% fidelity [Moehring et al., Nature 449, 68–71 (2007)](https://doi.org/10.1038/nature06118 "First remote ion-ion entanglement, 2007")
- Best peer-reviewed photonic entanglement rate: 4.5 Bell pairs/s at 94% fidelity (Stephenson et al. 2020) [Stephenson et al., Phys. Rev. Lett. 124, 110501 (2020)](https://doi.org/10.1103/PhysRevLett.124.110501 "4.5 Bell pairs/sec remote entanglement, 2020"); Monroe modular vision targets ~10⁴ pairs/s for fault-tolerant operation, ~100× beyond current demonstrations [Monroe et al., Phys. Rev. A 89, 022317 (2014)](https://doi.org/10.1103/PhysRevA.89.022317 "Monroe modular architecture, 2014")
- Innsbruck demonstrated ion-ion entanglement over 230 m using telecom-converted photons, fidelity >90% [Krutyanskiy et al., Phys. Rev. Lett. 130, 050803 (2023)](https://doi.org/10.1103/PhysRevLett.130.050803 "230m ion entanglement via telecom photons, 2023")
- First remote CNOT gate between trapped ions via photonic link at ~89% fidelity [Hucul et al., Nature Physics 11, 37–42 (2015)](https://doi.org/10.1038/nphys3150 "First remote gate between trapped ions, 2015")
- IonQ Tempo designed around reconfigurable multicore photonic-interconnect architecture; long-term vision scales to hundreds/thousands of qubits by networking trap modules [IonQ technology overview](https://ionq.com/technology "IonQ photonic interconnect technology")
- Universal Quantum/Sussex proposes electronic (direct ion transport) interconnects: ions physically shuttled between separate trap chips via electric fields (~mm gap), deterministic rather than probabilistic; 2024 Sussex demonstration showed chip-to-chip ion transport at ~100 μs with high fidelity [Lekitsch et al., Science Advances 3, e1601540 (2017)](https://doi.org/10.1126/sciadv.1601540 "Sussex blueprint for modular ion trap computer") [Stahl et al. (2024)](https://doi.org/10.1038/s41467-024-44986-w "Chip-to-chip ion transport demonstration, Sussex 2024")
- Sussex blueprint estimated million-qubit system using 2D array of X-junction modules with microwave-driven gates, footprint comparable to a large server room [Lekitsch et al., Science Advances 3, e1601540 (2017)](https://doi.org/10.1126/sciadv.1601540 "Million-qubit architecture blueprint, 2017")
- Monroe group hierarchical scaling vision: chip (50–200 qubits, QCCD) → chamber (short-range photonic/direct transport) → rack (meter-scale fiber) → data center (long-range photonic + repeaters) [Monroe and Kim, Science 339, 1164–1169 (2013)](https://doi.org/10.1126/science.1231298 "Monroe-Kim scaling vision, 2013")
- Microwave-driven gates (Oxford Ionics, Sussex/Universal Quantum) eliminate complex laser systems; first demonstrated by NIST in 2011 [Ospelkaus et al., Nature 476, 181–184 (2011)](https://doi.org/10.1038/nature10290 "First microwave-driven ion gate, NIST 2011"); Oxford Ionics claims 99.97% two-qubit fidelity (2024, peer review pending)
- Integrated photonics: Sandia/MIT demonstrated fully integrated photonic ion trap with on-chip light delivery for qubit operations [Mehta et al., Nature 586, 533–537 (2020)](https://doi.org/10.1038/s41586-020-2823-6 "Integrated photonic ion trap, Nature 2020")
- Cavity-enhanced photon collection can boost efficiency from ~1–5% (free space) to >50% (high-finesse cavity) [Kobel et al., npj Quantum Information 7, 6 (2021)](https://doi.org/10.1038/s41534-020-00338-2 "Ion-cavity coupling for enhanced photon collection")
- Network topology for distributed QEC: overhead depends critically on inter-module/intra-module gate fidelity and rate ratio [Nickerson et al., Nature Communications 4, 1756 (2013)](https://doi.org/10.1038/ncomms2773 "Distributed QEC analysis with noisy links")
- Comparative TRL assessment: QCCD monolithic (TRL ~6–7), photonic interconnects (TRL ~3–4), electronic interconnects (TRL ~2–3), microwave gates (TRL ~4–5), hybrid QCCD+photonic is consensus near-term strategy for >1,000 qubits

### 可用图片
- None available in local `/data/`

### 仍需补充
- 2025–2026 photonic interconnect rates beyond Stephenson 2020 (4.5 pairs/s); any claim of 100+ pairs/s requires specific peer-reviewed citation
- Quantinuum's latest QCCD multi-chip scaling plans and whether Helios represents single-chip expansion or multi-module architecture
- IonQ Tempo peer-reviewed inter-module entanglement performance data
- Universal Quantum's latest commercial system progress and chip-to-chip transport benchmarks
- Cavity-enhanced ion-photon coupling results from 2025–2026 (Oxford, Innsbruck, ETH)
- Integrated photonics gate fidelities with on-chip light delivery (Sandia/MIT 2025–2026 updates)
- Multi-node quantum computation peer-reviewed citations (Monroe group 2025, Drmota et al. Oxford 2023)
- AQT's architectural scaling strategy

## Chapter 3: Engineering Challenges in Scaling Ion Trap Hardware
### 研究目标
- Identify and analyze critical engineering bottlenecks impeding scaling from ~10–50 qubits to ~1,000–1,000,000+ qubits
- Quantify the gap between current capability and large-scale operational requirements where possible

### 关键发现
- Surface-electrode traps (all electrodes in one plane) are the standard scalable platform; first demonstrated at NIST in 2006 [Seidelin et al., Phys. Rev. Lett. 96, 253003 (2006)](https://doi.org/10.1103/PhysRevLett.96.253003 "First microfabricated surface-electrode trap, NIST 2006"); Sandia HOA-2.0 trap features ~150 DC electrodes with X-junctions for 2D routing [Maunz, Sandia Report SAND2016-0796R (2016)](https://doi.org/10.2172/1237003 "Sandia HOA-2.0 trap design")
- Material trade-offs: silicon (CMOS-compatible but RF losses), fused silica (excellent RF but harder fabrication), sapphire (good RF + thermal but expensive); electrode surface quality directly impacts anomalous heating [Bruzewicz et al., Appl. Phys. Rev. 6, 021314 (2019)](https://doi.org/10.1063/1.5088164 "Trapped-ion QC review, 2019")
- CMOS integration milestone: MIT Lincoln Lab demonstrated surface-electrode trap on commercial 90 nm CMOS with integrated DACs; a 1,000-qubit QCCD system may require 5,000–10,000 independent DC voltage channels [Stuart et al., Phys. Rev. Applied 11, 024010 (2019)](https://doi.org/10.1103/PhysRevApplied.11.024010 "CMOS-integrated ion trap, MIT Lincoln Lab 2019")
- Cryogenic (4–10 K) vs. room-temperature: cryo reduces anomalous heating ~100–1,000× and achieves <10⁻¹² Torr via cryopumping, but cryostat cooling power limited to ~1–10 W at 4 K constraining thermal budget for electronics [Labaziewicz et al., Phys. Rev. Lett. 100, 013001 (2008)](https://doi.org/10.1103/PhysRevLett.100.013001 "Cryogenic heating rate suppression, MIT 2008")
- Current H2 trap chip: ~1 cm × 5 cm, ~200–300 DC electrodes, 5 gate zones, 32+ storage locations; scaling to 1,000 qubits would need >5,000–10,000 electrodes, ~10 cm × 10 cm chips, multi-layer routing via TSVs [Moses et al., Phys. Rev. X 13, 041052 (2023)](https://doi.org/10.1103/PhysRevX.13.041052 "H2 trap chip details")
- ETH Zurich achieved single-ion transport over 280 µm in 3.6 µs with n̄ < 0.1 quanta motional excitation [Walther et al., Phys. Rev. Lett. 109, 080501 (2012)](https://doi.org/10.1103/PhysRevLett.109.080501 "Fast near-ground-state transport, ETH 2012"); H2 production shuttling ~50 µs per primitive at ~4 m/s, transport fidelity >99.99% per operation
- X-junction crossing: first reliable demonstration at NIST 2009, ~0.05 quanta axial excitation, ~60 µs [Blakestad et al., Phys. Rev. Lett. 102, 153002 (2009)](https://doi.org/10.1103/PhysRevLett.102.153002 "First X-junction transport, NIST 2009"); subsequent improvements reduced excitation to sub-quanta levels
- Critical scaling bottleneck: cumulative motional excitation from sequential transport operations (~0.1 quanta each × 10–20 primitives → ~1–2 quanta per gate cycle), requiring sympathetic cooling before each gate; transport overhead scaling O(√N) for 2D architectures [Schoenberger et al. (2024)](https://doi.org/10.48550/arXiv.2401.11730 "Ion shuttling scheduling analysis, 2024")
- Sympathetic cooling: Ba⁺ for Yb⁺ (Quantinuum/IonQ), Mg⁺ for Be⁺ (NIST); each qubit paired with a coolant ion, doubling total ion count; recooling from ~1–2 quanta post-transport to n̄ ≈ 0.1 takes ~200–500 µs resolved sideband cooling, comprising 20–40% of ~2–3 ms gate cycle [Moses et al., Phys. Rev. X 13, 041052 (2023)](https://doi.org/10.1103/PhysRevX.13.041052 "H2 sympathetic cooling parameters")
- EIT cooling alternative: Innsbruck demonstrated cooling to n̄ = 0.01 quanta in ~100 µs, potentially faster than resolved sideband cooling for multi-mode cooling [Lechner et al., Phys. Rev. A 93, 053401 (2016)](https://doi.org/10.1103/PhysRevA.93.053401 "EIT cooling of ion strings, Innsbruck")
- Individual laser addressing: beam waists ~1–2 µm, ion spacing 3–5 µm, crosstalk ~10⁻³–10⁻⁴; scaling to 1,000+ ions with free-space optics considered infeasible [Debnath et al., Nature 536, 63–66 (2016)](https://doi.org/10.1038/nature18648 "Individual addressing in ion trap QC")
- Integrated photonics (Mehta et al. 2020): on-chip waveguides + grating couplers for light delivery, single-qubit gate fidelity >99.5%, eliminates free-space optics [Mehta et al., Nature 586, 533–537 (2020)](https://doi.org/10.1038/s41586-020-2823-6 "Integrated photonic ion trap, Nature 2020")
- Anomalous motional heating scales as d⁻⁴ with ion-electrode distance [Turchette et al., Phys. Rev. A 61, 063418 (2000)](https://doi.org/10.1103/PhysRevA.61.063418 "Anomalous heating d^-4 scaling, NIST 2000"); room-temp rates at d ≈ 50 µm: ~100–10,000 quanta/s; cryogenic (4 K): ~1–10 quanta/s; 1/f noise spectrum [Brownnutt et al., Rev. Mod. Phys. 87, 1419 (2015)](https://doi.org/10.1103/RevModPhys.87.1419 "Anomalous heating review, 2015")
- Surface treatment (Ar⁺ ion milling) reduces heating by ~100×: from ~1,800 to ~20 quanta/s at d = 39 µm, room temperature [Hite et al., Phys. Rev. Lett. 109, 103001 (2012)](https://doi.org/10.1103/PhysRevLett.109.103001 "100-fold heating reduction via Ar milling, NIST 2012")
- UHV requirements: <10⁻¹¹ Torr for multi-hour ion lifetimes; at 10⁻¹¹ Torr with 1,000 ions, ~1 collision event per several hours, possibly requiring mid-computation ion replacement protocols
- System integration for ~1,000-qubit system: ~10,000+ electrodes, ~10,000 DC channels, dozens–hundreds of laser channels, imaging optics for ~1,000 ions, FPGA control generating ~10⁶ updates/s, potentially cryostat at 4–10 K; infrastructure scaling from rack to room/data-center scale
- Interconnect density bottleneck: wire-bond density limited to ~100–200 per chip edge; 10,000-connection chips require flip-chip bonding or TSV routing
- Total classical control power for 1,000-qubit system estimated at tens to hundreds of kilowatts (DACs, RF amplifiers, lasers, FPGAs, cryocooler ~5–15 kW per stage)
- Quantitative gap analysis: heating rate gap ~1–2 orders of magnitude for room temp (closed for cryo + surface treatment); control channel gap: 20–50× increase needed from current ~200–300 to ~10,000; laser/optics gap: free-space infeasible beyond ~100 ions, microwave gates or integrated photonics required

### 可用图片
- None available in local `/data/`

### 仍需补充
- Latest (2025–2026) anomalous heating rate measurements, especially cryogenic + advanced surface treatments
- Quantinuum H2 detailed per-primitive motional excitation data (quanta per junction crossing, split/merge) from open literature
- Integrated photonics progress 2024–2026 (two-qubit gates with on-chip light delivery, demonstrations at scale)
- CMOS-integrated trap yield data and electrode uniformity statistics
- Sympathetic cooling timescales at scale (>50 ions experimental data)
- EIT / mid-circuit cooling demonstrations during quantum computation
- H2-1 (72-qubit) trap chip modifications and electrode count
- FPGA/ASIC control system specifications for current production systems
- RF drive distribution challenges for large (>5 cm) trap chips

## Chapter 4: Quantum Error Correction Tailored to Ion Trap Architectures
### 研究目标
- Examine how QEC requirements and code choices interact with ion trap hardware characteristics (native gate sets, connectivity, error profiles, scaling architectures)
- Assess current state of logical qubit demonstrations on ion trap platforms
- Analyze overhead and path to fault-tolerant advantage

### 关键发现
- Dominant ion trap error channels: dephasing (magnetic field/laser phase noise), motional heating (anomalous E-field noise), off-resonant photon scattering during Raman gates (~1–3 × 10⁻⁴ per two-qubit gate), and leakage to non-computational states (~10⁻⁵ to 10⁻⁴ per gate) [Ozeri et al., Phys. Rev. A 75, 042329 (2007)](https://doi.org/10.1103/PhysRevA.75.042329 "Photon scattering errors in ion gates") [Bruzewicz et al., Appl. Phys. Rev. 6, 021314 (2019)](https://doi.org/10.1063/1.5088164 "Ion trap error channels review")
- H2 two-qubit gate error budget (~2 × 10⁻³ total): photon scattering ~3–5 × 10⁻⁴, motional heating ~2–3 × 10⁻⁴, laser fluctuations ~3–5 × 10⁻⁴, mode frequency drifts ~1–2 × 10⁻⁴, SPAM ~3 × 10⁻⁴; approximately depolarizing with slight dephasing bias [Moses et al., Phys. Rev. X 13, 041052 (2023)](https://doi.org/10.1103/PhysRevX.13.041052 "H2 error budget analysis")
- Ion trap error asymmetry: single-qubit errors (10⁻⁴–10⁻⁶) are 10–100× lower than two-qubit errors (10⁻³–10⁻²), differing from superconducting systems; flag-qubit protocols exploit this [Ryan-Anderson et al., Phys. Rev. X 11, 041058 (2021)](https://doi.org/10.1103/PhysRevX.11.041058 "Error asymmetry exploitation in QEC")
- Correlated errors between ions in same gate zone typically ~10⁻⁵ to 10⁻⁴, roughly one order below single-qubit error rate — independent-error approximation is reasonable but not exact [Erhard et al., Nature Communications 10, 5347 (2019)](https://doi.org/10.1038/s41467-019-13068-7 "Correlated error characterization")
- QCCD idle errors during ~3–5 ms QEC cycle: dephasing ~3–5 × 10⁻³ (comparable to gate error itself); dynamical decoupling suppresses by 10–100×
- Surface code threshold ~0.57–1.1%; ion trap two-qubit errors 0.1–0.2% are 5–10× below threshold, placing ion traps firmly in below-threshold regime [Fowler et al., Phys. Rev. A 86, 032324 (2012)](https://doi.org/10.1103/PhysRevA.86.032324 "Surface code threshold analysis"); overhead: ~200 physical qubits per logical qubit at distance 7
- Color codes: transversal Clifford gates, threshold ~0.46–0.8%, weight-6 stabilizers measurable without SWAP gates on all-to-all ion trap connectivity; [[7,1,3]] Steane code as primary experimental testbed [Bombin and Martin-Delgado, Phys. Rev. Lett. 97, 180501 (2006)](https://doi.org/10.1103/PhysRevLett.97.180501 "Color code introduction"); overhead: ~10–25 physical qubits per logical qubit at distance 3–5 [Beverland et al., PRX Quantum 2, 020341 (2021)](https://doi.org/10.1103/PRXQuantum.2.020341 "Color code overhead comparison")
- Bacon-Shor [[9,1,3]] code: weight-2 checks (single two-qubit gate per measurement), threshold ~0.2%, reduced gate count per syndrome extraction [Bacon, Phys. Rev. A 73, 012340 (2006)](https://doi.org/10.1103/PhysRevA.73.012340 "Bacon-Shor code")
- qLDPC codes: 12 logical qubits in 144 physical qubits at distance 12 (~12:1 ratio vs. surface code ~200:1), but require non-local connectivity that may conflict with QCCD routing [Bravyi et al., Nature 627, 778–782 (2024)](https://doi.org/10.1038/s41586-024-07107-7 "qLDPC bivariate bicycle codes")
- Flag-qubit protocols reduce ancilla overhead from O(d) to O(1) per stabilizer check, especially valuable for ion traps where each qubit requires an ion + coolant ion [Chao and Reichardt, npj Quantum Information 4, 42 (2018)](https://doi.org/10.1038/s41534-018-0085-z "Flag-qubit protocol")
- **Quantinuum-Microsoft Nature 2025**: 12 logical qubits on H2 using [[7,1,3]] Steane and [[12,2,4]] color codes, logical error rates ~2 × 10⁻³ per round, below-threshold operation confirmed; transversal CNOT between logical qubits exceeded unencoded fidelity ("below break-even"); all operations in real time without post-selection [Microsoft and Quantinuum, Nature (2025)](https://www.nature.com/articles/s41586-025-08684-1 "Below-threshold QEC demonstration, Nature 2025")
- Up to 10 repeated QEC rounds on [[7,1,3]] code at ~10⁻³ logical error per round; QEC cycle ~3–5 ms (shuttling ~1–2 ms, cooling ~0.5–1 ms, gates ~0.5–1 ms) [Ryan-Anderson et al., arXiv:2309.09893](https://arxiv.org/abs/2309.09893 "Quantinuum fault-tolerant gates on color code")
- Innsbruck: fault-tolerant universal gates on [[7,1,3]] Steane code (10 ions), fault-tolerant T gate fidelity 0.898 vs. non-FT 0.865 [Postler et al., Nature 605, 675–680 (2022)](https://doi.org/10.1038/s41586-022-04721-1 "Innsbruck fault-tolerant gates"); 16 QEC rounds with 3× logical lifetime extension [Hilder et al., Phys. Rev. X 12, 011032 (2022)](https://doi.org/10.1103/PhysRevX.12.011032 "Innsbruck repeated QEC"); fault-tolerant entanglement between two logical qubits (20 ions, ~75–80% Bell state fidelity) [Postler et al., PRX Quantum 5, 030326 (2024)](https://doi.org/10.1103/PRXQuantum.5.030326 "Innsbruck logical qubit entanglement")
- Quantinuum 2021: first real-time fault-tolerant QEC on any platform using [[5,1,3]] code on H1 [Ryan-Anderson et al., Phys. Rev. X 11, 041058 (2021)](https://doi.org/10.1103/PhysRevX.11.041058 "First real-time FT QEC")
- IonQ: error detection (not correction) using [[4,2,2]] code with post-selection; fewer published QEC demonstrations compared to Quantinuum/Innsbruck
- Magic-state distillation: accounts for ~60–80% of total physical qubit overhead in surface code architectures; color code code-switching or 3D gauge fixing may reduce this; ion traps' lower physical error rates allow fewer distillation rounds [Litinski, Quantum 3, 205 (2019)](https://doi.org/10.22331/q-2019-12-02-205 "Magic state distillation overhead")
- QCCD QEC cycle ~3–5 ms is ~100× slower than projected superconducting ~10–50 µs; logical clock speed ~200–300 ops/s (ion trap) vs. ~10,000–100,000 ops/s (superconducting); partial compensation from lower error per cycle and parallelism across logical qubits
- Error suppression factor Λ projected at 2–8 for ion traps (physical errors ~0.1–0.2%, color code threshold ~0.4–0.8%), potentially higher than Google's measured Λ ≈ 2.14 on Willow [Acharya et al., Nature (2024)](https://doi.org/10.1038/s41586-024-08449-y "Google Willow below-threshold result")
- Projected 10,000–50,000 physical qubits for useful fault-tolerant ion trap computation (~100 logical qubits at distance 7–11); using efficient color/qLDPC codes, ~5,000–10,000 physical qubits may suffice
- Timeline estimates: Quantinuum targets ~2029, IonQ targets ~2028, academic consensus 2030–2035 for utility-scale fault-tolerant QC
- Neutral-atom comparison: Harvard-QuEra demonstrated 48 logical qubits on 280-atom system [Bluvstein et al., Nature 626, 58–65 (2024)](https://doi.org/10.1038/s41586-023-06927-3 "Harvard-QuEra 48 logical qubits"), but two-qubit fidelity (~99.5%) and measurement fidelity (~99%) currently lag ion traps

### 可用图片
- None available in local `/data/`

### 仍需补充
- Exact logical error rates from Quantinuum-Microsoft Nature 2025 paper at different code distances/QEC round counts
- Details on "tesseract code" (arXiv 2409.04628): whether 4D color code variant and specific achieved logical error rates
- IonQ peer-reviewed QEC results beyond corporate blog posts
- Updated Innsbruck QEC results beyond 2022 (larger code distances, more QEC cycles)
- Detailed qLDPC code overhead estimates specifically tailored to QCCD routing constraints
- Mid-circuit measurement and real-time classical feedback latency numbers for ion trap QEC
- Quantitative QEC cycle time comparison: ion trap vs. superconducting vs. neutral atom

## Chapter 5: Software, Compilation, and Control Stacks for Large-Scale Ion Trap Systems
### 研究目标
- Analyze software and classical-infrastructure layers required to program, compile, optimize, and control large-scale ion trap quantum computers
- Identify gaps in current tooling and ion-trap-specific compilation advantages/challenges

### 关键发现
- Native MS gate at arbitrary entangling angles θ ∈ (0, π/4] reduces two-qubit gate counts by 30–50% vs. fixed-angle gates [Maslov, New J. Phys. 19, 023035 (2017)](https://doi.org/10.1088/1367-2630/aa5e47 "Circuit compilation with native ion trap gates"); light-shift (ZZ) gate alternative at 99.9% fidelity may offer advantages for certain QEC circuits [Ballance et al., Phys. Rev. Lett. 117, 060504 (2016)](https://doi.org/10.1103/PhysRevLett.117.060504 "Light-shift gate, Oxford")
- All-to-all connectivity eliminates SWAP overhead: N-qubit QFT requires O(N²) gates on ion trap vs. O(N³) on nearest-neighbor architectures; experimentally confirmed on 5-qubit head-to-head comparison [Linke et al., PNAS 114, 3305–3310 (2017)](https://doi.org/10.1073/pnas.1618020114 "Ion trap vs. superconducting comparison, PNAS 2017")
- Global multi-qubit MS gates prepare N-qubit GHZ states in a single pulse vs. O(N) two-qubit gates on conventional architectures [Figgatt et al., Nature 572, 368–372 (2019)](https://doi.org/10.1038/s41586-019-1427-5 "Global MS gate parallel entangling")
- QCCD compilation advantage: lower gate counts but higher wall-clock times per circuit layer vs. superconducting; QAOA on 100-qubit 3-regular graph requires 3–5× more CNOT layers on nearest-neighbor grid [Murali et al., Proc. ISCA (2019)](https://doi.org/10.1145/3307650.3322273 "Full-stack architectural comparison")
- Native arbitrary single-qubit rotations R(θ, φ) eliminate need for Solovay-Kitaev decomposition, further reducing circuit depth
- TKET: Quantinuum's open-source compiler (Apache 2.0), decomposes arbitrary two-qubit unitaries to ≤3 XX gates via KAK decomposition, 20–40% two-qubit gate count reduction on typical circuits, supports 30+ backends [Sivarajah et al., Quantum Sci. Technol. 6, 014003 (2021)](https://doi.org/10.1088/2058-9565/ab8e92 "TKET compiler framework") [TKET GitHub](https://github.com/CQCL/tket "Open-source repository")
- IonQ native gate set {GPi, GPi2, MS}: up to 50% two-qubit gate count reduction vs. generic CNOT compilation; "native gates" mode exposed via cloud API [Wright et al., Nature Communications 10, 5464 (2019)](https://doi.org/10.1038/s41467-019-13534-2 "IonQ 11-qubit benchmarking")
- Staq compiler: open-source, ion-trap-specific, T-count reduction 30–40% on quantum chemistry circuits [Amy and Mosca, IEEE Trans. Inf. Theory 65, 4771–4784 (2019)](https://doi.org/10.1109/TIT.2019.2906374 "T-count optimization")
- QIR (Quantum Intermediate Representation): Microsoft LLVM-based IR supporting classical control flow, mid-circuit measurement, dynamic circuits — adopted by Quantinuum for H-series via Azure Quantum
- Shuttling scheduling is NP-hard in general [Sargaran and Wille, DATE (2019)](https://doi.org/10.23919/DATE.2019.8715261 "NP-hardness of shuttling scheduling"); SAT-based exact scheduling achieves 10–30% shorter schedules than heuristics but exponential solver runtime for >~100 gates [Schoenberger et al., ASP-DAC (2024)](https://doi.org/10.1109/ASP-DAC58780.2024.10473869 "SAT-based exact shuttling scheduling")
- Shuttling-aware compilation (joint circuit optimization + routing) reduces total execution time 20–40% vs. separate optimization [Murali et al., Proc. ISCA (2020)](https://doi.org/10.1109/ISCA45697.2020.00051 "Shuttling-aware QCCD compilation")
- H2 achieves 2–4× parallelism across 5 gate zones for typical circuits [Moses et al., Phys. Rev. X 13, 041052 (2023)](https://doi.org/10.1103/PhysRevX.13.041052 "H2 parallel scheduling")
- TILT layout tool: joint trap layout + schedule optimization, 15–25% execution time improvement vs. manual layouts [Wu et al., Proc. HPCA (2021)](https://doi.org/10.1109/HPCA51647.2021.00023 "TILT layout optimization")
- Real-time QEC feedback on H-series: mid-circuit measurement (~0.3% error), FPGA decoding + feedback in ~10–50 µs, small vs. ~3–5 ms QEC cycle; not a current bottleneck but may become one at larger code distances [Ryan-Anderson et al., Phys. Rev. X 11, 041058 (2021)](https://doi.org/10.1103/PhysRevX.11.041058 "Real-time QEC feedback")
- Classical control hierarchy: host computer → FPGA real-time controller (branching logic in ~1–10 µs) → hardware signal generators; 1,000-qubit system needs thousands of DAC channels, hundreds of laser/MW channels
- QV record 2²⁰ reflects all-to-all connectivity advantage (no SWAP overhead) [Cross et al., Phys. Rev. A 100, 032328 (2019)](https://doi.org/10.1103/PhysRevA.100.032328 "QV definition"); CLOPS ~30–100 for ion traps vs. 10,000–100,000 for superconducting (~100–1,000× throughput gap)
- QED-C benchmarks: H1 consistently achieved highest fidelity scores across algorithm benchmarks at ≤20 qubits but with substantially lower throughput [Lubinski et al., IEEE Trans. Quantum Eng. 4, 3100332 (2023)](https://doi.org/10.1109/TQE.2023.3253761 "QED-C benchmark results")
- Mirror circuit benchmarks enable scalable verification beyond classical simulation frontier [Proctor et al., Phys. Rev. Lett. 129, 150502 (2022)](https://doi.org/10.1103/PhysRevLett.129.150502 "Mirror circuit benchmarking")
- Compiler-aware trap layout co-design: trap layout optimized for surface code QEC reduces shuttling overhead 30–50% vs. generic racetrack [Murali et al., ISCA (2020)](https://doi.org/10.1109/ISCA45697.2020.00051 "QCCD layout co-design")
- Circuit partitioning for modular architectures: balanced hypergraph partitioning reduces inter-module communication 40–60% [Baker et al., Proc. CF (2020)](https://doi.org/10.1145/3387902.3392617 "Circuit partitioning for modular QC"); automated distribution algorithms reduce costs 50–70% vs. random assignment [Andres-Martinez and Sheridan, Phys. Rev. A 100, 032308 (2019)](https://doi.org/10.1103/PhysRevA.100.032308 "Automated circuit distribution")
- Noise-aware compilation using calibration data improves circuit fidelity 10–25% by assigning critical gates to highest-fidelity qubit pairs
- Photonic-interconnect modular systems create "two-tier" compilation: probabilistic entanglement scheduling, distillation, circuit partitioning, gate teleportation — significantly more complex than single-chip compilation

### 可用图片
- None available in local `/data/`

### 仍需补充
- Quantinuum's proprietary shuttling scheduler algorithmic details (not covered by open-source TKET)
- IonQ Tempo multicore compilation internals and inter-module circuit partitioning
- Systematic cross-compiler benchmarks: TKET (ion trap) vs. Qiskit (superconducting) on standard algorithm suite
- Real-time decoding latency projections for distance-7+ QEC codes on ion traps
- Software stacks for AQT, Oxford Ionics, Universal Quantum (less documented)
- Polynomial-time optimal scheduling for restricted topologies (e.g., racetrack)

## Chapter 6: Comparative Assessment of Scaling Approaches
### 研究目标
- Synthesize preceding analyses into structured, evidence-based comparison of leading scaling strategies
- Evaluate each on technical feasibility, resource requirements, timeline, and TRL
- Provide brief cross-platform comparison (superconducting, neutral-atom, photonic)

### 关键发现
- Assessment framework uses six dimensions: scalability ceiling, interconnect fidelity/bandwidth, engineering complexity, QEC compatibility, cost trajectory, and TRL; consistent with NAS 2019 quantum computing assessment [NAS, "Quantum Computing: Progress and Prospects" (2019)](https://doi.org/10.17226/25196 "NAS 2019 assessment framework")
- TRL anchored to demonstrated milestones: QCCD at TRL 6–7 (72-qubit commercial system + real-time QEC), photonic interconnects at TRL 3–4 (4.5 Bell pairs/s lab demo), electronic interconnects at TRL 2–3 (proof-of-concept chip-to-chip 2024), microwave gates at TRL 4–5 (99.97% claimed but no system-level integration)
- **QCCD monolithic**: highest maturity, 99.8–99.9% two-qubit fidelity, QV = 2²⁰, best QEC results (12 logical qubits below threshold); ceiling ~100–1,000 qubits per chip limited by control channel scaling (20–50× needed), shuttling overhead O(√N), and fabrication yield; risks include CMOS integration validation and fidelity maintenance at scale
- **Photonic modular**: unlimited scalability in principle (~100 modules × ~100 qubits each per Monroe 2014 vision), but critical ~1,000× entanglement rate gap (4.5 vs. ~10⁴ Bell pairs/s needed); inter-module fidelity ~89–94% significantly below intra-module ~99.8%; strengths include heralded entanglement and compatibility with quantum networking [Stephenson et al., Phys. Rev. Lett. 124, 110501 (2020)](https://doi.org/10.1103/PhysRevLett.124.110501 "Best photonic interconnect rate")
- **Electronic modular**: deterministic (100% success per transfer), potentially high bandwidth (~100 µs), compatible with microwave gates; but TRL 2–3, no system-level integration with gates/QEC, limited to mm-scale chip proximity, single primary proponent (Universal Quantum) [Stahl et al., Nature Communications (2024)](https://doi.org/10.1038/s41467-024-44986-w "Chip-to-chip ion transport")
- **Hybrid QCCD+photonic**: consensus near-term strategy endorsed by IonQ, Monroe group, and implicitly Quantinuum; staged deployment path (single-chip QCCD → few modules → many modules); QEC compatibility requires codes for heterogeneous error rates, with Nickerson et al. showing fault-tolerant operation possible even with inter-module error rates ~10× higher than intra-module [Nickerson et al., Nature Communications 4, 1756 (2013)](https://doi.org/10.1038/ncomms2773 "Distributed QEC with noisy links"); main limitation is dual-infrastructure cost and compilation complexity
- **Near-term (2025–2030)**: QCCD monolithic is most probable path to ~1,000 qubits; solutions for control scaling (CMOS) and laser elimination (microwave gates) are at TRL 4–5; Quantinuum targets hundreds of qubits by 2027–2028
- **Long-term (2030+)**: Hybrid QCCD+photonic most widely endorsed for ~1M qubits, contingent on ~1,000× improvement in photonic entanglement rates; electronic interconnects offer alternative path if chip-to-chip transport integrates with high-fidelity operations
- **Cross-platform — superconducting**: IBM 1,121-qubit Condor (2023), Heron R2 ~133 qubits at ~99.5–99.7% two-qubit fidelity; Google Willow (105 qubits) demonstrated below-threshold surface code QEC with Λ ≈ 2.14 and ~1.1 µs QEC cycle time — ~3,000× faster than ion traps [Acharya et al., Nature (2024)](https://doi.org/10.1038/s41586-024-08449-y "Google Willow below-threshold QEC"); superconducting leads in qubit count, logical clock speed (~100× faster), but ion traps lead in per-gate fidelity (2–5× lower error), connectivity (all-to-all vs. nearest-neighbor), and coherence (T₂ ~10,000× longer)
- **Cross-platform — neutral atoms**: Harvard-QuEra 48 logical qubits on 280-atom array [Bluvstein et al., Nature 626, 58–65 (2024)](https://doi.org/10.1038/s41586-023-06927-3 "Harvard-QuEra 48 logical qubits"); >1,000 atoms loaded (Atom Computing); Rydberg CZ fidelity ~99.5% (vs. ion trap 99.8–99.9%); comparable QEC cycle times (~1–10 ms); neutral atoms have loading/parallelism advantage but lower measurement fidelity (~99% vs. ~99.7%) and shorter coherence (~1–10 s vs. ~10 min)
- **Cross-platform — photonic QC**: PsiQuantum (~$700M+ funding) targeting million-qubit fault-tolerant system via silicon photonics + GlobalFoundries manufacturing, but no demonstrated programmable multi-qubit processor; Xanadu Borealis: 216-mode boson sampling (not universal QC) [Madsen et al., Nature 606, 75–81 (2022)](https://doi.org/10.1038/s41586-022-04725-x "Xanadu Borealis"); photonic universal QC at TRL 2–3
- Platform maturity ranking for fault-tolerant QEC (early 2026): superconducting and ion traps are co-leaders (both below-threshold), neutral atoms demonstrated most logical qubits but at lower fidelity, photonic QC has not yet demonstrated QEC
- BCG 2024 projects quantum computing market at $450–850 billion by 2040, with multiple hardware modalities coexisting for different application domains [BCG, "The Next Decade in Quantum Computing" (2024)](https://www.bcg.com/publications/2024/next-decade-in-quantum-computing "BCG 2024 quantum market analysis")
- DARPA US2QC program (launched 2023) includes ion trap teams, reflecting U.S. defense assessment that ion traps remain competitive for utility-scale QC

### 可用图片
- None available in local `/data/`; recommend generating multi-criteria radar chart and TRL timeline during write phase

### 仍需补充
- IBM roadmap updates: Flamingo (multi-chip) and Starling (error-corrected) milestone status
- Google Willow exact logical error rates at distance-3 vs. distance-5 for precise comparison with Quantinuum color code results
- Neutral-atom gate fidelity improvements since Bluvstein et al. 2023
- Cross-platform cost-per-qubit or cost-per-logical-operation data (largely proprietary)
- IonQ Tempo peer-reviewed inter-module performance data
- PsiQuantum progress since 2023
- Published independent TRL assessments of quantum computing technologies
- Quantinuum Helios system specifications (single-chip vs. multi-module)
- Direct Λ comparison across platforms (Quantinuum color code vs. Google surface code vs. neutral atom)
- Oxford Ionics system-level benchmarks (QV, CLOPS, QEC) using microwave-driven gates

## Chapter 7: Industry Roadmaps, Investment Landscape, and Outlook (2025–2027)
### 研究目标
- Map publicly stated roadmaps of leading ion trap companies and research programs
- Assess investment and policy environment
- Synthesize forward-looking outlook on when/how ion trap systems may reach practical real-world problem-solving capability

### 关键发现
- **Quantinuum**: roadmap targets universal fault-tolerant QC by ~2029; H2-1 (72 qubits, QV = 2²⁰) → Helios (~200+ qubits, expected 2026–2027) → large-scale fault-tolerant; raised >$600M external funding at ~$9B valuation (2025), Honeywell majority shareholder, investors include JPMorgan, Mitsui, Amgen [Quantinuum roadmap](https://www.quantinuum.com/blog/our-path-to-universal-fault-tolerant-quantum-computing "Quantinuum roadmap to universal fault tolerance") [Quantinuum $300M raise](https://www.quantinuum.com/pressrelease/quantinuum-raises-300m "Quantinuum $300M raise, Jan 2024")
- Quantinuum-Microsoft partnership central to fault-tolerance strategy; Azure Quantum integration; logical qubit functionality planned for Helios generation [Microsoft Azure Quantum](https://azure.microsoft.com/en-us/products/quantum "Azure Quantum + Quantinuum")
- **IonQ**: #AQ 36 (Forte) → #AQ 64 (Tempo, Dec 2024) → #AQ 256 (~2026) → #AQ 4,096 (~2028–2029); NYSE-listed (IONQ, since Oct 2021), FY2024 revenue ~$43M (up from ~$22M FY2023), backlog >$70M; >$600M total raised; Tempo uses reconfigurable multicore architecture with photonic interconnects for modular scaling [IonQ AQ 64](https://ionq.com/news/ionq-announces-aq64-achievement "IonQ AQ 64 milestone") [IonQ SEC filings](https://investors.ionq.com/sec-filings "IonQ annual financial reports")
- IonQ two-qubit gate fidelity ~99.4% (Forte) with 99.9% target on Tempo — notably below Quantinuum's 99.8–99.9%, with implications for QEC overhead
- IonQ contracts: $54.5M AFRL quantum networking (2024), multi-cloud access (AWS, Azure, Google Cloud), DARPA US2QC participation, Hyundai collaboration; Seattle manufacturing facility announced [IonQ news](https://ionq.com/news "IonQ contracts and partnerships")
- **AQT**: 24-qubit PINE system (⁴⁰Ca⁺, room-temp, rack-mountable), deployed at European HPC centers (LRZ); >€50M total funding; EU Flagship participant; roadmap targets 50+ qubits [AQT product page](https://www.aqt.eu/pine-system/ "AQT PINE system")
- **Oxford Ionics**: microwave-based electronic qubit control ("eQual" chip), 99.97% two-qubit gate fidelity claimed (2024, peer review pending); £30M Series A (2024); commercialization via technology licensing + own systems; commercial processor target 2026–2027 [Oxford Ionics £30M raise](https://oxfordionics.com/news/oxford-ionics-raises-30-million "Oxford Ionics Series A, 2024")
- **Universal Quantum**: million-qubit blueprint via electronic interconnects + microwave gates [Lekitsch et al., Science Advances 3, e1601540 (2017)](https://doi.org/10.1126/sciadv.1601540 "Million-qubit blueprint"); chip-to-chip ion transport demonstrated 2024 [Stahl et al., Nature Communications (2024)](https://doi.org/10.1038/s41467-024-44986-w "Chip-to-chip transport"); ~£67M total funding; staged path: prototype modules (2025–2026) → hundreds of qubits (2027–2028) → million-qubit (2030+)
- **DARPA US2QC**: launched 2023, ~$50–100M across all teams, targets utility-scale QC within ~5–10 years; phased structure (Phase 1: identify approaches; Phase 2: prototype systems); ion trap teams participating [DARPA US2QC](https://www.darpa.mil/program/underexplored-systems-for-utility-scale-quantum-computing "DARPA US2QC program")
- **EU Quantum Flagship**: €1B over 10 years, ion trap projects include AQTION and MILLENION (modular ion-light interface, ~€10–15M); EuroHPC deploys AQT systems at HPC centers [EU Quantum Flagship](https://qt.eu "EU Quantum Flagship")
- **UK**: National Quantum Strategy £2.5B over 10 years; NQCC at Harwell engages Oxford Ionics and Universal Quantum; ion traps identified as UK competitive advantage [UK National Quantum Strategy](https://www.gov.uk/government/publications/national-quantum-strategy "UK National Quantum Strategy, 2023")
- **Germany**: €3B national quantum strategy (2022–2026), supports Universal Quantum and AQT; DLR partnerships
- **Other**: Japan Moonshot Goal 6 (fault-tolerant QC by 2050); South Korea ₩3T (~$2.3B) plan (2024) with IonQ partnerships; China >$15B aggregate quantum spending (superconducting/photonic focused, ion trap secondary); Australia has ion trap research but silicon-qubit focused
- Global quantum industry attracted >$3B VC/corporate investment in 2024–2025; ion trap companies represent significant share [BCG quantum market analysis](https://www.bcg.com/publications/2024/next-decade-in-quantum-computing "BCG $450–850B quantum market by 2040")
- Supply chain maturing: specialized vendors for vacuum (Kimball Physics, SAES), trap fabrication (Sandia, MEMS foundries), lasers (Toptica, M Squared), cryogenics (Bluefors, Oxford Instruments); Quantinuum vertically integrated via Honeywell
- **Applications timeline**: quantum simulation nearest (~2028–2032); quantum chemistry ~2030–2035 (FeMo-co requires ~100–200 logical qubits, ~10⁸ T gates → ~10,000–100,000 physical qubits) [Reiher et al., PNAS 114, 7555 (2017)](https://doi.org/10.1073/pnas.1619152114 "FeMo-co resource estimates"); optimization uncertain (~2030+); finance ~2028–2032 (50–200 logical qubits); cryptography (RSA-2048) well beyond 2035 (~4,000+ logical qubits / ~20M physical qubits) [Gidney & Ekerå, Quantum 5, 433 (2021)](https://doi.org/10.22331/q-2021-04-15-433 "RSA-2048 resource estimates")
- QEC-based logical qubit access as near-term differentiator: cloud access to logical qubits (vs. only noisy physical qubits) likely by 2027–2028, preceding full application advantage
- **Most plausible near-term trajectory**: QCCD monolithic dominates through 2027; Quantinuum Helios (~200+ qubits) is most probable next milestone; IonQ #AQ 256 on Tempo depends on demonstrating modular photonic interconnects far beyond current published results
- **Key inflection points**: Helios launch (2026–2027), IonQ #AQ 256 modular demo (2026–2027), Oxford Ionics scaling test (2026–2027), first commercial multi-module ion trap QPU (2027–2028), quantum advantage demonstration (2028–2030), Quantinuum fault-tolerance target (~2029)
- **Critical open questions**: photonic interconnect ~2,200× rate improvement needed (cavity-enhanced coupling offers pathway [Kobel et al., npj Quantum Information 7, 6 (2021)](https://doi.org/10.1038/s41534-020-00338-2 "Cavity-enhanced >50% collection")); microwave gate scaling validation; electronic interconnect + gate/QEC integration; neutral-atom competition (closing gate fidelity gap from 99.5% to 99.8%+); classical simulation frontier advancement; funding sustainability
- **Competitive positioning**: Quantinuum leads on technical metrics (QV, QEC, fidelity, valuation); IonQ leads on commercial presence (public company, multi-cloud, revenue); Oxford Ionics and Universal Quantum offer disruptive alternatives at earlier TRL; AQT anchors European ecosystem

### 可用图片
- None available in local `/data/`; recommend generating: company roadmap timeline through 2030, cumulative funding comparison chart, and application readiness matrix during write phase

### 仍需补充
- Quantinuum Helios exact specifications (qubit count, single-chip vs. multi-module)
- IonQ Tempo peer-reviewed inter-module entanglement data (critical for modular scaling credibility)
- DARPA US2QC exact funding level, specific ion trap teams, Phase 1/2 milestone definitions
- IonQ FY2025 revenue update
- Quantinuum-Microsoft Nature 2025 exact Λ and logical error rate values
- Oxford Ionics 99.97% peer-reviewed validation
- EU MILLENION project outcomes and publications
- China ion trap investment disaggregation (current $15B figure is aggregate, not ion-trap-specific; flag uncertainty)
- South Korea quantum plan specifics and ion trap allocations from official sources
- AQT next-generation system (50+ qubits) announcements
- Updated quantum advantage timeline estimates from 2025–2026 resource analyses

---

# Section 2：给 Write 阶段的执行建议

## Source Verification Requirements (T1/T2 Mandates)
- All qubit-count figures, gate fidelities, coherence times, and quantum volume numbers in Chapter 1 must come from T1 (company technical papers, peer-reviewed publications, official press releases) or T2 (Gartner, IDC, etc.) sources
- Company roadmap targets in Chapter 7 (IonQ AQ targets, Quantinuum logical-qubit goals) must be traced to official company publications, SEC filings, or investor presentations
- QEC threshold values and overhead estimates in Chapter 4 must cite peer-reviewed publications or preprints
- TRL assessments in Chapter 6 must be grounded in demonstrated results (T1) or authoritative third-party evaluations (T2)
- DARPA US2QC program details and government funding figures require official program documentation

## Cross-Chapter Consistency Points
- Use "QCCD" consistently (not "quantum CCD" in some places); define "logical qubit" vs. "physical qubit" once in Chapter 1
- Standardize "photonic interconnect" (not "optical interconnect")
- When quoting gate fidelities, always specify gate type and measurement method
- Use consistent cutoff date for "current state" vs. "future projections"
- Standardize error-rate notation (choose either scientific notation or percentages throughout)
- Use consistent company/lab names (e.g., "Quantinuum" not "Honeywell Quantum Solutions")

## Potential Pitfalls
- Photonic interconnect entanglement rates vary widely; flag gap between demonstrated and required rates
- Many scaling claims are corporate vision statements, not validated engineering plans; distinguish demonstrated vs. projected
- Cost data is scarce/proprietary; label cost estimates clearly as projections
- QEC overhead calculations assume idealized noise models; present overhead numbers as conditional
- Cross-platform comparison (Ch. 6.7) should remain concise, factual, and avoid platform-advocacy framing
- Verify cited numbers represent the most recent benchmarks given rapid field movement
- Acknowledge gaps from classified/embargoed government program results rather than speculating
