# Research Plan: Analysis and Study of Singles Badminton Player Actions Using Sports Videos

**Research Time Window**: April 2025 – October 2026 (anchored at current date 2026-04-07)

---

# Section 1: Chapter Research Plan

## Chapter 1: Object Detection and Tracking in Badminton Videos

### 研究目标
- What are the unique visual challenges of badminton video analysis (fast shuttlecock motion, occlusion, broadcast camera angles, motion blur) and how do state-of-the-art detection and tracking methods address them?
- What is the current accuracy–speed trade-off frontier for each detection target (player, shuttlecock, court, racket), and where do remaining gaps lie?
- Scope includes: player/shuttlecock/court/racket detection and tracking in monocular footage; homography-based court mapping; TrackNet family and YOLO-based detectors; public datasets (ShuttleSet, VideoBadminton, TrackNet benchmarks).
- Scope excludes: multi-camera/motion-capture setups; wearable sensors; doubles-specific formations; detailed pose estimation (Chapter 2); downstream classification/prediction.

### 关键发现
- 发现 1: TrackNet (2019) pioneered heatmap-based deep learning for high-speed tiny object tracking in sports video. Using VGG-16 encoder with deconvolution decoder on 640×360 input, 3-frame temporal stacking achieved F1 98.5% on a single match but dropped to F1 84.3% under 10-fold cross-validation across 10 videos, revealing significant generalization challenges [TrackNet](https://arxiv.org/abs/1907.03698 "Huang et al., IEEE AVSS 2019").
- 发现 2: TrackNetV2 (2020) shifted to a U-Net encoder-decoder processing 3 frames simultaneously (9-channel input, 3 heatmap outputs), achieving accuracy 96.3%, precision 97.0%, recall 98.7% on 78,200 labeled frames from 26 broadcast videos, with ~3× faster throughput than TrackNet [TrackNetV2](https://scholar.nycu.edu.tw/en/publications/tracknetv2-efficient-shuttlecock-tracking-network "Sun et al., ICPAI 2020").
- 发现 3: TrackNetV3 (2024) introduced trajectory prediction and trajectory rectification modules (background-based augmentation + inpainting for occluded segments), raising shuttlecock tracking accuracy from 87.72% to 97.51% on the standard benchmark (~10 pp improvement) [TrackNetV3](https://dl.acm.org/doi/10.1145/3595916.3626370 "Chen & Wang, ACM MMAsia 2023/2024").
- 发现 4: YO-CSA (2025) adapted YOLOv8s with Contextual Transformer (CoT2f) blocks and Spatial Group-wise Enhance (SGE) modules, achieving 99.43% mAP@0.5, 90.43% mAP@0.75, 74.00% mAP@0.5:0.95 on 32,539 images from 10 venues, outperforming YOLOv8s (71.50% mAP@0.5:0.95) and YOLO11s (71.56%). The complete YO-CSA-T 3D tracking system maintained >130 fps [YO-CSA-T](https://arxiv.org/pdf/2501.06472 "Lai et al., arXiv:2501.06472, Jan 2025").
- 发现 5: Standard YOLO comparison shows near-perfect mAP@0.5 for shuttlecock detection (YOLOv5s 98.49%, YOLOv8s 99.38%, YOLO11s 99.37%), but stricter IoU thresholds (mAP@0.75) range 76–90%, indicating remaining challenges in precise bounding box localization [YO-CSA-T](https://arxiv.org/pdf/2501.06472 "Lai et al., 2025, Table I").
- 发现 6: Shuttlecock detection faces five unique challenges: (a) ~5px apparent size in 1280×720 broadcast footage; (b) velocities up to 493 km/h causing severe motion blur; (c) conical feathered shape varies with viewing angle; (d) visual confusion with court lines and reflections; (e) frequent occlusion behind players/net [Shuttlecock challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC9655598/ "Sensors 2022").
- 发现 7: Heatmap regression is the dominant paradigm for shuttlecock tracking (adopted by TrackNet/V2/V3), outperforming bounding-box methods for sub-pixel-scale objects by avoiding anchor/box regression and naturally handling partial visibility [TrackNet](https://arxiv.org/abs/1907.03698 "Huang et al., 2019").
- 发现 8: MonoTrack (CVPR Workshop 2022) presented the first end-to-end monocular 3D shuttle trajectory reconstruction system, integrating court recognition, 2D trajectory estimation, GRU-based hit detection, and physics-informed 3D reconstruction [MonoTrack](https://arxiv.org/abs/2204.01899 "Liu & Wang, CVSports 2022").
- 发现 9: Deep semantic segmentation for court registration (ResNet-50 + DeepLabV3Plus + RANSAC) achieved mean IoU 0.781 for homography registration and 99.08% mIoU for court zone segmentation on 564 broadcast images with diverse court colors [Court Registration](https://openreview.net/pdf/01b2e7445170ebd4328ed615e1196d4ce6b880ef.pdf "Jouini et al., 2024").
- 发现 10: CourtKeyNet (2026) introduced octave-based architecture with Polar Transform Attention and Quadrilateral Constraint Module for badminton court keypoint detection, reportedly outperforming general-purpose keypoint methods [CourtKeyNet](https://github.com/adithyanraj03/Paper_09_Data-Set_CourtKeyNet "Raj & Prethija, ML with Applications, 2026").
- 发现 11: TrackNet/V2 benchmark dataset comprises 26 broadcast videos (78,200 labeled frames) with per-frame shuttlecock coordinates, covering 2018–2021 tournaments with elite players [TrackNet Dataset](https://hackmd.io/@TUIK/rJkRW54cU "Official CoachAI dataset page").
- 发现 12: ShuttleSet (KDD 2023) is the largest badminton singles dataset with 36,492 human-annotated strokes across 3,685 rallies in 44 matches, featuring 18 shot type classes and player positions [ShuttleSet](https://arxiv.org/abs/2306.04948 "Wang et al., KDD 2023").
- 发现 13: ShuttleSet22 (IJCAI 2024) provides 30,172 training strokes in 2,888 rallies from 2022 high-ranking matches, designed for stroke forecasting benchmarking [ShuttleSet22](https://arxiv.org/abs/2306.15664 "Wang et al., IJCAI 2024 Demo").
- 发现 14: VideoBadminton (IEEE BigData 2024) contains 7,822 video clips (145 min) from 19 players covering 18 BWF-standard stroke classes at 1280×960/60fps; SlowFast achieved 82.80% Top-1 accuracy [VideoBadminton](https://arxiv.org/html/2403.12385v1 "Li et al., IEEE BigData 2024").
- 发现 15: FineBadminton (ACM MM 2025) introduces 3,215 rally clips with multi-level semantic annotation (Foundational Actions, Tactical Semantics, Decision Evaluation) for evaluating MLLMs on fine-grained sports video understanding [FineBadminton](https://arxiv.org/abs/2508.07554 "He et al., ACM MM 2025").
- 发现 16: Speed comparison — TrackNet: 12–15 fps; TrackNetV2: ~30+ fps; YOLO variants: 230–290 fps; YO-CSA-T complete 3D system: >130 fps. Real-time broadcast analysis (30–60 fps) is achievable with YOLO-based but not heatmap-based approaches [YO-CSA-T](https://arxiv.org/pdf/2501.06472 "Lai et al., 2025, Table IV").
- 发现 17: Racket detection remains largely unexplored — no dedicated method exists; current approaches infer racket position indirectly through wrist/hand keypoints from pose estimation.
- 发现 18: Unified multi-task badminton detection benchmarks do not exist — different studies use different datasets, splits, and metrics, making cross-method comparison difficult. The TrackNet benchmark covers only shuttlecock detection.

### 可用图片
（无本地相关图片）

### 仍需补充
- TrackNetV2 exact F1 score on the held-out test set (3 test matches) — the original paper reports accuracy/precision/recall on training distribution but exact test-set F1 is unclear.
- Player detection mAP in badminton-specific contexts — no badminton-specific study benchmarks player detection independently; quantitative badminton-broadcast player detection benchmarks are absent.
- CourtKeyNet (2026) exact quantitative IoU and keypoint accuracy numbers — full paper in Machine Learning with Applications not yet fully accessible.
- WASB-SBDT and HRNet-based shuttlecock detector performance numbers — referenced in YO-CSA-T but specific badminton metrics not retrieved.
- FineBadminton detailed frame counts and detection-specific annotation statistics beyond the 3,215 rally clips.
- Latest 2026 publications (YOLOv12+, updated TrackNet models, novel transformer-based shuttlecock detectors) may not be captured.

---

## Chapter 2: Recognition of Technical Actions (Stroke-Type Classification)

### 研究目标
- Which feature representations and model architectures currently achieve the highest classification accuracy for badminton stroke types?
- How do skeleton-based approaches (GCN, Transformer-based models like BST) compare with RGB-appearance-based and hybrid methods?
- What role do complementary signals—shuttlecock trajectory, player court position, temporal context within rallies—play in improving recognition?
- Scope includes: frame/clip-level stroke classification; skeleton/pose-based action recognition; appearance-based and Transformer-based temporal models; TrackNet-derived ball trajectory as auxiliary input; annotation taxonomies; stroke quality assessment.
- Scope excludes: general action recognition benchmarks unrelated to racket sports; real-time coaching hardware/deployment; tactical interpretation (Chapter 3).

### 关键发现
- 发现 1: BST (Badminton Stroke-type Transformer, 2025) is the current SOTA for badminton stroke classification. On ShuttleSet (25 merged classes, 33,481 strokes), BST-CG-AP achieves 83.22% accuracy and 80.97% Macro-F1, outperforming TemPose-TF (82.35%, 80.28%). Key innovation: Cross Transformer Layer performs cross-attention where K/V derive from shuttlecock trajectory latent and Q from player pose/position [BST](https://arxiv.org/html/2502.21085v4 "Chang, arXiv:2502.21085, Feb 2025").
- 发现 2: On fine-grained ShuttleSet (35 classes), BST-CG-AP achieves 77.80% accuracy and 71.16% Macro-F1 vs. TemPose-TF at 76.42%/69.53%. Confusion matrices reveal kinematically similar strokes ("smash" vs. "wrist smash," "return net" vs. "defensive return drive") are the primary error source [BST](https://arxiv.org/html/2502.21085v4 "Chang, Appendix B").
- 发现 3: TemPose (CVPR Workshop 2023) is a factorized skeleton-based Transformer with separate temporal and interaction layers. On Badminton Olympics dataset (13 classes, 15,300 samples), TemPose-TF achieves 90.7% Top-1 accuracy with 1.7M parameters, outperforming ST-GCN (82.0%), MS-G3D (83.2%), and AcT (83.7%) [TemPose](https://openaccess.thecvf.com/content/CVPR2023W/CVSports/papers/Ibh_TemPose_A_New_Skeleton-Based_Transformer_Model_Designed_for_Fine-Grained_Motion_CVPRW_2023_paper.pdf "Ibh et al., CVPRW 2023").
- 发现 4: Standard GCN models without auxiliary inputs yield limited accuracy on ShuttleSet (25 classes): ST-GCN 77.58%, BlockGCN (CVPR 2024) 76.52%, SkateFormer (ECCV 2024) 77.10%, ProtoGCN (CVPR 2025) 77.46% — all using joint-only input without shuttlecock/position data [BST](https://arxiv.org/html/2502.21085v4 "Chang, Table 1").
- 发现 5: 2D skeleton joints outperform 3D joints for badminton stroke recognition — BST with 2D: 76.95% vs. 3D: 75.25% on ShuttleSet (35 classes). 3D pose estimation models trained on general-purpose datasets introduce bias toward generic poses [BST](https://arxiv.org/html/2502.21085v4 "Chang, Appendix B.2").
- 发现 6: On VideoBadminton (18 BWF-aligned classes, 7,822 clips), SlowFast achieves best RGB-based Top-1 accuracy 82.80% (MCA 73.80%), followed by Video Swin Transformer 81.99%, R(2+1)D 79.53%. Among skeleton methods, PoseC3D achieves 80.76%, ST-GCN 74.41% [VideoBadminton](https://arxiv.org/html/2403.12385v1 "Li et al., IEEE BigData 2024, Table 3").
- 发现 7: In low-data regimes, skeleton-based methods significantly outperform RGB: with 10 samples/class, ST-GCN achieves 28.05% vs. SlowFast 12.79%; with 50 samples/class, ST-GCN 60.70% vs. SlowFast 12.28%. Skeleton representations are invariant to appearance variations [VideoBadminton](https://arxiv.org/html/2403.12385v1 "Li et al., Table 2").
- 发现 8: Shuttlecock trajectory is more discriminative than player court position for stroke classification: adding shuttlecock position to TemPose-V yields +3.44 pp improvement (77.56% → 81.00%), while adding player position yields only +1.86 pp (→ 79.42%). Trajectory "always reflects the actual stroke-type and contains no misleading information" [BST](https://arxiv.org/html/2502.21085v4 "Chang, Table 1, modality analysis").
- 发现 9: TCN (Temporal Convolutional Networks) serve as temporal backbone in both TemPose and BST, chosen over LSTM/GRU for parallelizable computation and better handling of variable-length sequences [TemPose](https://openaccess.thecvf.com/content/CVPR2023W/CVSports/papers/Ibh_TemPose_A_New_Skeleton-Based_Transformer_Model_Designed_for_Fine-Grained_Motion_CVPRW_2023_paper.pdf "Ibh et al., CVPRW 2023") [BST](https://arxiv.org/html/2502.21085v4 "Chang, Section 3.3.1").
- 发现 10: Temporal window size matters: BST's adaptive clipping strategy (100 frames including context from adjacent strokes) outperforms fixed-width clipping (30 frames), improving from 82.54% to 83.22% accuracy. Including opponent's previous/next stroke provides discriminative context [BST](https://arxiv.org/html/2502.21085v4 "Chang, Appendix D").
- 发现 11: Transformer depth requires careful tuning: TemPose-TF peaks at depth L_T=2, L_N=2 (90.7%) on Bad OL; increasing to L_T=8, L_N=8 degrades to 85.2%, indicating overfitting on small badminton datasets [TemPose](https://openaccess.thecvf.com/content/CVPR2023W/CVSports/papers/Ibh_TemPose_A_New_Skeleton-Based_Transformer_Model_Designed_for_Fine-Grained_Motion_CVPRW_2023_paper.pdf "Ibh et al., CVPRW 2023, Table 4").
- 发现 12: ShuttleSet defines 18 original stroke categories, expanding to 35 when differentiating top/bottom player. Class distribution is highly imbalanced (>24:1 ratio between most/least common). BST merges similar categories to yield 25 practical classes [BST](https://arxiv.org/html/2502.21085v4 "Chang, Appendix E, Tables F/G").
- 发现 13: BadmintonDB (ACM MMSports 2022) uses 9 stroke categories per player (18 total), 7,658 strokes across 8 matches. BST-AP achieves 99.23% accuracy and 99.22% Macro-F1, suggesting this dataset is relatively less challenging due to fewer players and matches [BST](https://arxiv.org/html/2502.21085v4 "Chang, Table 4").
- 发现 14: Li et al. (2025) present the first integrated pipeline for badminton action recognition + quality assessment, using HRNet pose estimation (83.2% mAP) and Siamese network with SlowFast backbone for quality scoring against reference actions. Stroke classification achieves 83.08% Top-1 accuracy [Li et al. 2025](https://journals.sagepub.com/doi/10.1177/1088467X251353444 "Li et al., Intelligent Data Analysis, 2025").
- 发现 15: Deceptive strokes are a fundamental challenge — players deliberately perform misleading body movements, causing skeleton-only models to be misled. Shuttlecock trajectory is more reliable since it "always reflects the actual stroke-type" regardless of deceptive movements [BST](https://arxiv.org/html/2502.21085v4 "Chang, Section 1").
- 发现 16: Asriani et al. (2026) proposed a hybrid RGB-skeleton framework with handcrafted features (HOG, HOF, MBH, ROMI, DTW) and weighted soft-voting ensemble achieving 98.21% accuracy, though on a custom smaller-scale dataset rather than standardized benchmarks [Asriani et al. 2026](https://www.etasr.com/index.php/ETASR/article/view/15586 "Asriani et al., ETASR vol. 16, Feb 2026").

### 可用图片
（无本地相关图片）

### 仍需补充
- FineBadminton (ACM MM 2025) multi-level annotation scheme details and MLLM benchmark results for stroke-type recognition beyond what is available from the abstract.
- CTR-GCN (ICCV 2021) performance on badminton datasets — not evaluated in any reviewed paper.
- I3D and C3D performance on badminton datasets — absent from main benchmarks.
- Cross-dataset generalization study (e.g., ShuttleSet → BadmintonDB) — no systematic evaluation exists.
- Temporal action detection (automatic stroke boundary localization) benchmarking accuracy — most works assume pre-segmented clips.
- Stroke quality assessment beyond Li et al. (2025) — Siamese-network quality metrics and validation against human judges need verification from the full paper.
- Latest 2026 publications building on BST or introducing novel architectures.

---

## Chapter 3: Recognition of Tactical Intent Behind Singles Players' Actions

### 研究目标
- How can tactical intent categories (offensive pressure, defensive recovery, transitional maneuvering, deception) be formally defined and operationalized for computational modeling?
- What contextual features—player positions, rally history, score state, shuttlecock placement zones—are most informative for inferring tactical intent?
- How do current methods for tactical pattern mining and classification perform, and what are the principal challenges in bridging low-level action recognition with high-level strategic understanding?
- Scope includes: tactical intent classification from video-derived features; rally/point-level tactical pattern analysis; contextual modeling using court zones, movement trajectories, rally sequences; visual analytics tools for coaches; deception detection.
- Scope excludes: doubles-specific formations; game-theoretic equilibrium analysis without empirical grounding; match-outcome prediction without per-action intent labels (partly Chapter 4); coaching pedagogy beyond computational modeling.

### 关键发现
- 发现 1: TIVEE (IEEE TVCG 2022) establishes a three-category tactical taxonomy: offensive techniques (smash, net shot, cut smash), control techniques (clear, drop, chop, push, hook shot, drive), and defensive techniques (lob, block). A "tactic" is formally defined as "a combination of consecutive strokes (containing at least two of a player's strokes)" [TIVEE](https://ssxiexiao.github.io/papers/TIVEE.pdf "Chu et al., IEEE TVCG 2022, Section 3.2").
- 发现 2: FineBadminton (ACM MM 2025) introduces the most detailed computational tactical taxonomy: 3 categories of player actions (offensive/defensive/passive-transitional), 9 strategic classifications, 6 types of shot characteristics, including "deception" as an explicit intent label. It contains 3,215 rally clips (33,325 strokes) from 120 singles matches [FineBadminton](https://arxiv.org/html/2508.07554v1 "He et al., ACM MM 2025, Section 3.1/3.3").
- 发现 3: BFMD (arXiv 2026) maps fine-grained shot types into attack/control/defense categories for temporal tactical evolution analysis using sliding-window pattern matching, revealing dynamic strategic transitions across full matches [BFMD](https://arxiv.org/html/2603.25533v1 "Ding et al., arXiv:2603.25533, Section 3.5").
- 发现 4: Court zone division schemes vary across studies: TIVEE uses 3×3×3=27-field 3D division (distance, lateral, height); BadmintonVis uses 6-zone scheme; FineBadminton uses 9-zone aligned with BWF coaching conventions; CoachAI+ uses 10-area division [TIVEE](https://ssxiexiao.github.io/papers/TIVEE.pdf "Chu et al., 2022") [BadmintonVis](https://people.cs.nycu.edu.tw/~yushuen/data/BadmintonVis23.pdf "Chen et al., CGF 2023") [FineBadminton](https://arxiv.org/html/2508.07554v1 "He et al., 2025").
- 发现 5: TIVEE employs tactic aggregation where tactics with the same stroke technique sequence are grouped and ranked by "tactic score" (usage rate × scoring rate). Three-stroke tactical units (player's two strokes + opponent's intervening stroke) are the standard analysis convention across racket sports [TIVEE](https://ssxiexiao.github.io/papers/TIVEE.pdf "Chu et al., IEEE TVCG 2022, Sections 4.1–4.3").
- 发现 6: Shot2Tactic-Caption (ACM MMSports 2025) introduces a Tactic Unit Detector identifying valid tactic units, types, and states (Interrupt/Resume) from shot sequences. The dataset contains 5,494 shot captions and 544 tactic captions [Shot2Tactic-Caption](https://arxiv.org/abs/2510.14617 "Ding et al., ACM MMSports 2025").
- 发现 7: The offline RL approach (EAAI 2026) formulates tactical decisions as a hybrid-action MDP (state = player/opponent positions + last action; actions = shot type [discrete] + landing/movement position [continuous]). CQL achieves average reward 0.8703 ± 0.0786 on 94 international matches (59,472 strokes), outperforming Behavior Cloning (0.8482) and Decision Transformer (0.8027). The learned policy increases "Active Shot Type Rate" (0.3526 vs. 0.3015) and "Average Distance of Opponent Landing Position" (0.3898 vs. 0.2185) [Offline RL Badminton](https://wenminggong.github.io/papers/Offline_RL_for_Badminton_EAAI_paper.pdf "Liu et al., EAAI 2026, Tables 5/8").
- 发现 8: The preference-based reward model achieves 96.92% rally-preference accuracy and 92.27% action-preference accuracy in-distribution, but non-terminal rally-preference accuracy is only ~59%, indicating that distinguishing mid-rally tactical quality from outcome data remains largely unsolved [Offline RL Badminton](https://wenminggong.github.io/papers/Offline_RL_for_Badminton_EAAI_paper.pdf "Liu et al., EAAI 2026, Table 4").
- 发现 9: Deception detection — Park et al. (2019) found that kinematic information (global body motion) is more reliable than non-kinematic information for detecting deceptive movements in badminton through human perception studies (n=24). BST (2025) confirms that shuttlecock trajectory "always reflects the actual stroke-type" regardless of deceptive body movements [Park et al. 2019](https://e-space.mmu.ac.uk/627947/ "Park et al., Perception 48(4), 2019") [BST](https://arxiv.org/html/2502.21085v4 "Chang, 2025").
- 发现 10: FineBadminton is the first dataset with explicit "deception" intent labels for computational training, and FBBench reveals current MLLMs struggle with tactical comprehension — best model (Gemini 2.5 Pro) achieves only 38.62% accuracy on tactical multiple-choice questions [FineBadminton](https://arxiv.org/html/2508.07554v1 "He et al., ACM MM 2025, Table 1").
- 发现 11: Visual analytics tools for coaching — ShuttleSpace (IEEE TVCG 2021, 116 citations) clusters trajectories for VR first-person analysis; TIVEE (IEEE TVCG 2022, 86 citations) adds tactical sequence analysis in multi-court VR; VIRD (IEEE TVCG 2024, 47 citations) supports end-to-end immersive match analysis with Olympic athletes [ShuttleSpace](https://www.computer.org/csdl/journal/tg/2021/02/09222313/1nTr29xEpkk "Ye et al., TVCG 2021") [TIVEE](https://ssxiexiao.github.io/papers/TIVEE.pdf "Chu et al., TVCG 2022") [VIRD](https://arxiv.org/abs/2307.12539 "Lin et al., TVCG 2024").
- 发现 12: "Court to Conversation" (Knowledge-Based Systems, 2026) presents a novel end-to-end system converting CV outputs into structured tactical representations, then using RAG-enhanced LLMs to generate conversational tactical analysis for coaching [Court to Conversation](https://www.sciencedirect.com/science/article/abs/pii/S0950705125020659 "Bharadwaj & Srinivasa, KBS 333:115027, 2026").
- 发现 13: The gap between computational and human-expert tactical understanding remains substantial — FBBench shows GPT-4.1 achieves only ~30% on tactical reasoning; the RL reward model scores only ~59% on non-terminal tactical quality; current models learn primarily from win/lose outcomes rather than expert-annotated intent [FineBadminton](https://arxiv.org/html/2508.07554v1 "He et al., 2025") [Offline RL Badminton](https://wenminggong.github.io/papers/Offline_RL_for_Badminton_EAAI_paper.pdf "Liu et al., 2026").
- 发现 14: Offline RL limitations include: myopic one-step policy evaluation only; flawed "winner is superior" assumption; 0.80% irrational shot type rate; 3.17% out-of-bounds action rate; no real-world coaching validation [Offline RL Badminton](https://wenminggong.github.io/papers/Offline_RL_for_Badminton_EAAI_paper.pdf "Liu et al., EAAI 2026, Section 7").

### 可用图片
（无本地相关图片）

### 仍需补充
- "Court to Conversation" (KBS 2026) full paper details — paywall blocks access to the CV→structured representation pipeline, RAG architecture, and quantitative evaluation metrics. T2 source (KBS IF ~8.0) critical for knowledge engineering pipeline discussion.
- Quantitative tactical intent classification accuracy — no paper reports F1/accuracy specifically for offensive/defensive/transitional classification as a standalone task; existing approaches either map stroke types heuristically or generate NL descriptions.
- Score state and match momentum integration — no paper quantitatively demonstrates how incorporating score state improves tactical intent prediction; the offline RL paper explicitly excludes score state.
- Computational deception detection models — no explicit model exists despite available components (skeleton data, trajectory data, deception labels from FineBadminton).
- ViSTec (AAAI 2024) full details — primarily demonstrated on table tennis; specific tactical classification accuracy numbers not retrieved.
- Gaming tree-based tactical analysis (Cheng et al., Applied Sciences 2023) — analyzes Lin Dan vs. Lee Chong Wei matches but not read in full.

---

## Chapter 4: Prediction of Singles Players' Subsequent Actions

### 研究目标
- How is the next-action prediction problem formally defined—what are the prediction targets (stroke type, landing location, timing), input representations (rally history, player state, score), and prediction horizons?
- Which sequence modeling and RL architectures achieve the best predictive performance, and how do they handle the inherent uncertainty and multi-modality of human decision-making?
- What is the current gap between prediction accuracy in research settings and practical utility for real-time coaching or opponent scouting?
- Scope includes: next-shot type and landing-location prediction; rally-outcome forecasting; ShuttleNet, RallyTemPose and analogous architectures; offline/online RL for badminton (ShuttleEnv, CQL-based agents); game-tree search + deep learning; multi-task prediction; evaluation against human expert baselines.
- Scope excludes: match-winner prediction from aggregate statistics; injury/fatigue modeling; embedded system deployment; player ranking systems.

### 关键发现
- 发现 1: ShuttleNet (AAAI 2022) established the canonical formulation — given τ observed strokes with type-area pairs, predict future strokes. Architecture: Transformer-Based Rally Extractor (TRE) with type-area-attention, Transformer-Based Player Extractor (TPE) separating player subsequences, and Position-Aware Gated Fusion Network (PGFN). On 75 matches (43,191 strokes), with τ=8: CE=1.9802, MSE=1.5856, MAE=1.3802, outperforming Seq2Seq LSTM (CE=2.5219) and Transformer (CE=2.3843) by 12.0% in shot type CE [ShuttleNet](https://ojs.aaai.org/index.php/AAAI/article/view/20341/20100 "Wang et al., AAAI 2022").
- 发现 2: CoachAI Badminton Challenge 2023 (IJCAI 2023, Track 2) standardized the benchmark on ShuttleSet22 (30,172 training strokes, 2,040 test strokes). The winning team achieved total score 2.5776 (CE=1.7892, MAE=0.7884) vs. ShuttleNet baseline 2.8774. 11 of 16 teams outperformed ShuttleNet; improvements were primarily in shot type CE while area MAE barely improved [ShuttleSet22](https://ar5iv.labs.arxiv.org/html/2306.15664 "Du & Peng, IJCAI 2024").
- 发现 3: RallyTemPose (CVPR Workshop 2024) is the first model incorporating skeleton pose data for prediction. Achieved 54.3% top-1 accuracy, 77.3% top-2, 92.5% top-3 on ShuttleSet, outperforming Seq2Seq LSTM (47.9%) and Transformer (49.8%). Player ground position was the most critical input (+2.6% from its inclusion). Prediction accuracy varies by >20% across players, indicating potential for player "readability" measurement [RallyTemPose](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf "Ibh et al., CVPRW 2024").
- 发现 4: ShuttleFlow (Machine Learning, 2025) reframes prediction as distribution modeling using conditional normalizing flows, arguing the bivariate Gaussian assumption (ShuttleNet, DyMF) is invalid for multi-modal landing distributions. Achieved ~3× lower shuttle position RMSE (≈0.17 vs. ShuttleNet ≈0.53) and ~25% lower shot type CE (≈1.6 vs. ≈2.0) on 78 games (3,553 rallies). Inference: ~0.5s for 96 samples on RTX 4090 [ShuttleFlow](https://link.springer.com/article/10.1007/s10994-024-06682-0 "Lien et al., Machine Learning 114(2), 2025").
- 发现 5: DyMF (AAAI 2023) extends prediction to player movement forecasting using Player-Movement graphs with dynamic hierarchical fusion, predicting shot type + landing position + player movement positions [DyMF](https://arxiv.org/abs/2211.12217 "Chang et al., AAAI 2023").
- 发现 6: SPAIT (Journal of Big Data, 2026) proposes Area Position Feature-Encoder, Guidance Mask mechanism, and hierarchical Infer-Decoder that eliminates inconsistencies between predicted shot types and player positions (e.g., net shot while positioned in backcourt). Reports SOTA on movement forecasting on ShuttleSet22 [SPAIT](https://link.springer.com/article/10.1186/s40537-026-01407-7 "Jhang et al., J Big Data, 2026").
- 发现 7: CoachAI Badminton Environment (AAAI 2024) is the first RL environment bridging simulated and real-world badminton, providing data-driven opponent AIs for interactive rally-level simulation [CoachAI Environment](https://ojs.aaai.org/index.php/AAAI/article/view/30584 "Wang et al., AAAI 2024").
- 发现 8: ShuttleEnv (arXiv 2026) presents an interactive RL environment grounded in elite match data (Lin Dan vs. Lee Chong Wei). PPO agents achieved 98.3% ± 2.5% win rate over 1,000 simulated matches vs. fixed BC opponent (BC: 33.2%, A2C: 65.8%, SAC: 90.5%), demonstrating RL can discover strategies substantially superior to imitation [ShuttleEnv](https://arxiv.org/html/2603.17324v1 "Gong et al., arXiv:2603.17324, 2026").
- 发现 9: CQL with hybrid action space (EAAI 2026) achieves average reward 0.8703 ± 0.0786 on 94 matches (59,472 strokes), outperforming BC (0.8482) and Decision Transformer (0.8027). The learned policy increases opponent mobilization (Active Shot Type Rate 0.3526 vs. 0.3015) [Offline RL Badminton](https://wenminggong.github.io/papers/Offline_RL_for_Badminton_EAAI_paper.pdf "Liu et al., EAAI 2026").
- 发现 10: RallyNet (arXiv 2024) proposes hierarchical offline imitation learning via Contextual MDPs with Latent Geometric Brownian Motion for stochastic player modeling. Surpasses all baselines by ≥16% in MRNS; maximum win rate difference from ground truth only 3.79% (vs. BC 13.21%). Provides tactical interpretability through decoded context intents [RallyNet](https://arxiv.org/html/2403.12406v2 "Wang et al., arXiv:2403.12406, 2024").
- 发现 11: Minooka et al. (ICAART 2026) combine SARSA + LSTM action values with expanded game-tree search for optimal shot prediction. On ShuttleSet (2,220 rallies, 18 classes): 34.6% top-1, 66.9% top-3, 81.5% top-5, outperforming ShuttleNet (31.5%/54.8%/78.0%) and conventional game trees (31.8%/65.6%/80.9%) [Minooka et al.](https://www.scitepress.org/publishedPapers/2026/143176/pdf/index.html "Minooka et al., ICAART 2026").
- 发现 12: Three paradigms for handling prediction uncertainty: (a) parametric bivariate Gaussian (ShuttleNet, DyMF) — simple but fails on multi-modal distributions; (b) normalizing flows (ShuttleFlow) — captures full distribution, ~3× lower RMSE; (c) Geometric Brownian Motion (RallyNet) — models stochastic player interactions in latent space [ShuttleFlow](https://link.springer.com/article/10.1007/s10994-024-06682-0 "Lien et al., ML 2025").
- 发现 13: Transformer-based models consistently outperform RNN-based: ShuttleNet (CE=1.98) vs. Seq2Seq LSTM (CE=2.52); RallyTemPose (54.3% top-1) vs. Seq2Seq LSTM (47.9%). Key advantages: long-range dependency capture, type-area disentangled attention, turn-based player separation [ShuttleNet](https://ojs.aaai.org/index.php/AAAI/article/view/20341/20100 "Wang et al., 2022") [RallyTemPose](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf "Ibh et al., 2024").
- 发现 14: Evaluation metrics — CE for shot type distributions; MAE/MSE/RMSE for area coordinates; top-k accuracy for classification; DTW for sequence similarity; JSD for rally length distributions; EMD for spatial distributions. Standard stochastic protocol: generate K=6 or 10 samples, take closest to ground truth [ShuttleNet](https://ojs.aaai.org/index.php/AAAI/article/view/20341/20100 "Wang et al., 2022") [ShuttleSet22](https://ar5iv.labs.arxiv.org/html/2306.15664 "Du & Peng, 2024").
- 发现 15: Research-practice gap — best top-1 accuracy is ~54% (insufficient for real-time advice); no deployed real-time prediction system exists; ShuttleFlow inference ~0.5s exceeds ~0.3s reaction window; models omit score state, fatigue, and psychological context. The "what will happen" vs. "what should happen" distinction is largely unresolved [RallyTemPose](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf "Ibh et al., 2024") [ShuttleFlow](https://link.springer.com/article/10.1007/s10994-024-06682-0 "Lien et al., 2025").
- 发现 16: Most promising near-term application is opponent scouting via distribution visualization (ShuttleFlow) and player tendency analysis (ShuttleNet case studies showing player-specific response patterns) rather than real-time prediction [ShuttleNet](https://ojs.aaai.org/index.php/AAAI/article/view/20341/20100 "Wang et al., 2022") [RallyNet](https://arxiv.org/html/2403.12406v2 "Wang et al., 2024").

### 可用图片
（无本地相关图片）

### 仍需补充
- DyMF (AAAI 2023) exact quantitative results (CE, MSE, MAE) for movement forecasting on ShuttleSet — referenced extensively but specific metrics not fully extracted.
- SPAIT (J Big Data, 2026) specific numerical performance metrics (exact CE, MAE, DTW) and ablation results — full text not fully accessible.
- Diffusion-based models for badminton prediction — no published diffusion model found; ShuttleFlow explicitly chose normalizing flows over diffusion for sampling efficiency.
- Human expert baselines — no paper directly compares model predictions against human coach predictions; significant evaluation gap.
- CoachAI Badminton Environment (AAAI 2024) full opponent AI architecture details and benchmark results.
- KNN-HMM real-time model (Song & Zhang, J Big Data, 2026) — sensor-based stroke prediction, potentially the closest to deployed real-time systems; not fully read.

---

# Section 2: Writing Recommendations for the Write Stage

1. **Unified terminology**: Use "shuttlecock" consistently (not "shuttle"/"birdie"/"ball"); use "stroke type" for classification tasks; use "player" rather than "athlete." Define "rally," "stroke," "shot," "point," and "game" precisely in Chapter 1 and use uniformly thereafter.

2. **Model naming conventions**: Use canonical names with version numbers on first mention (e.g., "YOLOv8," "TrackNetV3," "ShuttleNet") and maintain exact form throughout. Do not alternate stylizations.

3. **Court coordinate system**: Adopt a single, clearly defined normalized court coordinate system (origin at center of court) and reference consistently across Chapters 1–4.

4. **Pipeline dependency acknowledgment**: Each chapter introduction should briefly state where it sits in the perception-to-cognition pipeline (detection → recognition → intent → prediction), what it receives from prior chapters, and what it passes downstream.

5. **Error propagation**: Each chapter should acknowledge how upstream errors cascade (detection errors → stroke misclassification → tactical analysis corruption → degraded predictions) without redundantly analyzing upstream methods.

6. **Shared architectures**: Transformers, GCNs, LSTMs appear across multiple chapters. Each chapter describes how the architecture is adapted to its specific task rather than repeating architectural tutorials.

7. **Running example**: Consider using a single representative rally clip that recurs across chapters to illustrate how the same video data is processed at each pipeline stage.

8. **Narrative arc**: The four chapters follow a perception-to-cognition pipeline from low-level to high-level. Each successive chapter addresses a harder, more ambiguous problem—detection is mature, stroke classification is advancing, tactical intent is nascent, action prediction remains an open frontier.

9. **End-to-end counterpoint**: In Chapters 3–4, discuss end-to-end approaches as alternatives to the modular pipeline paradigm.

10. **Time scope**: Research covers April 2025 – October 2026. Verify that cited methods and benchmarks reflect the most current state within this window.
