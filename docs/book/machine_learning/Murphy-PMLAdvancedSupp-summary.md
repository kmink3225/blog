---
name: "Probabilistic Machine Learning: Advanced Topics — Supplementary Material"
type: book-summary
authors: "Kevin P. Murphy"
year: 2025
total_pages: 310
language: en
keywords: [supplementary material, probabilistic ML, Bayesian inference, Dirichlet process, graph learning, proximal methods, particle filtering, variational inference, state-space models, diffusion models]
---

# Probabilistic Machine Learning: Advanced Topics (Supplementary Material) — Summary

> Kevin P. Murphy (2025), ~310 pages, 36 chapters (supplementary sections)
> "Probabilistic Machine Learning: Advanced Topics" 본문의 보충 자료로, 추가 예제, 증명, 심화 내용을 제공한다.

## Contents

이 파일은 본서("Probabilistic Machine Learning: Advanced Topics")의 각 장에 대한 보충 자료이다. 모든 장에 보충 내용이 있는 것은 아니며, 주로 추가 예제, 수학적 유도, 고급 알고리즘의 상세 설명을 포함한다.

**Part I: Fundamentals**
- Ch 2: Probability — MVN 추론, PageRank 알고리즘
- Ch 3: Bayesian statistics — 베이지안 개념 학습, 정보적 사전분포, Tweedie 공식
- Ch 4: Graphical models — DGM/UGM 추가 예제, RBM 상세
- Ch 5: Information theory — 가우시안 간 KL 최소화

**Part II: Inference**
- Ch 7: Optimization — 프록시멀 방법, 동적 프로그래밍, 켤레 쌍대성, 베이지안 학습 규칙
- Ch 8: Inference for state-space models — 칼만 필터 추가, EKF 유도, 지수족 EKF
- Ch 9: Inference for graphical models — BP on polytrees, 접합 트리 알고리즘, MAP 추정
- Ch 10: Variational inference — 가우시안 VI, 온라인 VI, 그래프 모형 VI
- Ch 11-13: Monte Carlo / MCMC / SMC — 추가 예제와 입자 MCMC

**Part III: Prediction**
- Ch 15: Generalized linear models — 변분 추론 로지스틱 회귀, 포아송 회귀
- Ch 16: Deep neural networks — 트랜스포머, GNN 추가
- Ch 17: Bayesian neural networks — EKF 기반 학습 상세
- Ch 18: Gaussian processes — 심층 GP, GP와 SSM

**Part IV: Generation**
- Ch 21: VAE — 결측 데이터 VAE
- Ch 22-26: 자기회귀 모형, 정규화 흐름, EBM, 확산 모형, GAN — 간략 보충

**Part V: Discovery**
- Ch 28: Latent factor models — 토픽 모형 추론 (LDA 깁스/변분)
- Ch 29: State-space models — 연속 시간 SSM, ODE, S4
- Ch 30: Graph learning — 확률적 블록 모형, 트리 구조 학습, DAG 구조 학습, 비방향 그래프 학습, 인과 DAG 학습
- Ch 31: Nonparametric Bayesian models — 디리클레 과정, DP 혼합, 피트먼-요르, 인도 뷔페, 포인트 과정

**Part VI: Decision making**
- Ch 34-36: 다단계 결정, 강화학습, 인과성 — 간략 보충

---

## 주요 보충 내용 요약

### Ch 2 보충: Probability (line 258)

**핵심**: 다변량 가우시안에서 결측 데이터가 있을 때의 추론, 측정 잡음이 알려지지 않은 센서 융합 문제를 다룬다. 구글 PageRank 알고리즘의 수학적 유도와 효율적 계산, 웹 스팸, 개인화 PageRank를 설명한다.

**키워드**: `MVN`, `missing data`, `sensor fusion`, `PageRank`

**상세**: → (삭제됨) Ch 2 (line 258)

### Ch 3 보충: Bayesian Statistics (line 20)

**핵심**: 베이지안 개념 학습(숫자 게임, 건강 수치 게임)의 상세 예제, 도메인 특화 사전분포(가우시안, 멱급수, Erlang), Tweedie 공식(경험적 베이즈에서 사전분포 추정 없이 사용)을 다룬다.

**키워드**: `concept learning`, `informative priors`, `Tweedie formula`, `empirical Bayes`

**상세**: → (삭제됨) Ch 3 (line 20)

### Ch 7 보충: Optimization (line 50)

**핵심**: 프록시멀 연산자와 프록시멀 방법(미러 디센트, 프록시멀 그래디언트, ADMM), 동적 프로그래밍, 켤레 쌍대성(시그모이드 함수 바운드), 베이지안 학습 규칙(BLR)에서 추론/최적화 알고리즘 유도를 다룬다.

**키워드**: `proximal operator`, `ADMM`, `conjugate duality`, `Bayesian learning rule`

**상세**: → (삭제됨) Ch 7 (line 50)

### Ch 30 보충: Graph Learning (line 182)

**핵심**: 확률적 블록 모형(SBM, MMSB, 무한 관계 모형), 트리 구조 학습(Chow-Liu, MAP forest), DAG 구조 학습(베이지안 모형 선택, 제약 기반, 희소 최적화), 비방향 그래프 학습(의존 네트워크, 그래프 라소), 인과 DAG 학습(원인-결과 쌍, 개입 데이터)을 상세히 다룬다.

**키워드**: `SBM`, `Chow-Liu`, `DAG structure learning`, `graphical lasso`, `causal DAG`

**상세**: → (삭제됨) Ch 30 (line 182)

### Ch 31 보충: Nonparametric Bayesian Models (line 212)

**핵심**: 디리클레 과정(정의, 스틱 브레이킹, 중국 식당 과정), DP 혼합 모형(깁스 샘플링, 변분 베이즈), 피트먼-요르 과정, 인도 뷔페 과정, 소분산 점근, 완전 랜덤 측도, 레비 과정, 반발과 강화를 가진 점 과정(포아송, 재생, 호크스, 깁스, DPP)을 상세히 다룬다.

**키워드**: `Dirichlet process`, `stick breaking`, `CRP`, `Pitman-Yor`, `IBP`, `DPP`

**상세**: → (삭제됨) Ch 31 (line 212)


---

## 원본 목차 (Marker 기준)

> 원본 파일: `Murphy-PMLAdvancedSupp_marker_full.md` | 총 ~7,822 라인
> `L:숫자`로 `Read(file, offset=L, limit=N)` 직접 접근 가능

- 1 Introduction (p.10) `L:258`
- 2 Probability (p.14) `L:266`
- 2.2 Google's PageRank algorithm (p.17) `L:385`
- 2.2.1 Retrieving relevant pages using inverted indices (p.17) `L:389`
- 2.2.2 The PageRank score (p.18) `L:418`
- 2.2.3 Efficiently computing the PageRank vector (p.19) `L:451`
- 2.2.4 Web spam (p.20) `L:485`
- 2.2.5 Personalized PageRank (p.21) `L:489`
- 3 Bayesian statistics (p.22) `L:493`
- 3.1 Bayesian concept learning (p.22) `L:495`
- 3.1.1 Learning a discrete concept: the number game (p.22) `L:503`
- 3.1.2 Learning a continuous concept: the healthy levels game (p.28) `L:624`
- 3.2 Informative priors (p.31) `L:698`
- 3.2.1 Domain specific priors (p.32) `L:729`
- 3.2.2 Gaussian prior (p.33) `L:741`
- 3.2.4 Erlang prior (p.34) `L:777`
- 3.3 Tweedie's formula (Empirical Bayes without estimating the prior) (p.35) `L:802`
- 4 Graphical models (p.38) `L:870`
- 4.1 More examples of DGMs (p.38) `L:872`
- 4.1.1 Water sprinkler (p.38) `L:874`
- 4.1.2 Asia network (p.39) `L:906`
- 4.1.3 The QMR network (p.40) `L:924`
- 4.1.4 Genetic linkage analysis (p.42) `L:975`
- 4.2 More examples of UGMs (p.45) `L:1033`
- 4.3 Restricted Boltzmann machines (RBMs) in more detail (p.45) `L:1035`
- 4.3.1 Binary RBMs (p.45) `L:1039`
- 4.3.2 Categorical RBMs (p.46) `L:1080`
- 4.3.3 Gaussian RBMs (p.46) `L:1095`
- 5 Information theory (p.48) `L:1123`
- 5.1 Minimizing KL between two Gaussians (p.48) `L:1125`
- 5.1.1 Moment projection (p.48) `L:1127`
- 5.1.2 Information projection (p.48) `L:1135`
- 7 Optimization (p.54) `L:1184`
- 7.1 Proximal methods (p.54) `L:1186`
- 7.1.1 Proximal operators (p.54) `L:1194`
- 7.1.2 Computing proximal operators (p.57) `L:1324`
- 7.1.3 Proximal point methods (PPM) (p.60) `L:1443`
- 7.1.3.2 Beyond linear approximations (truncated ADAGRAD) (p.60) `L:1470`
- 7.1.5.1 Example: Iterative soft-thresholding algorithm (ISTA) for sparse linear regression (p.66) `L:1680`
- 7.1.6 Alternating direction method of multipliers (ADMM) (p.66) `L:1694`
- 7.2 Dynamic programming (p.69) `L:1796`
- 7.2.1 Example: computing Fibonnaci numbers (p.69) `L:1800`
- 7.2.2 ML examples (p.69) `L:1824`
- 7.3 Conjugate duality (p.70) `L:1850`
- 7.3.2 Example: exponential function (p.71) `L:1882`
- 7.4 The Bayesian learning rule (p.75) `L:2032`
- 7.4.2 Deriving optimization algorithms from BLR (p.78) `L:2151`
- 7.4.3 Variational optimization (p.81) `L:2326`
- 8 Inference for state-space models (p.84) `L:2341`
- 8.1 More Kalman filtering (p.84) `L:2343`
- 8.1.3 Handling unknown observation noise (p.86) `L:2410`
- 8.2 More extended Kalman filtering (p.88) `L:2538`
- 8.2.2 Example: Tracking a pendulum (p.89) `L:2581`
- 8.3 Exponential-family EKF (p.90) `L:2615`
- 8.3.1 Modeling assumptions (p.90) `L:2619`
- 8.3.3 EEKF for training logistic regression (p.91) `L:2670`
- 8.3.4 EEKF performs online natural gradient descent (p.92) `L:2691`
- 9 Inference for graphical models (p.98) `L:2896`
- 9.1 Belief propagation on trees (p.98) `L:2898`
- 9.2 The junction tree algorithm (JTA) (p.101) `L:3022`
- 9.2.1 Tree decompositions (p.101) `L:3026`
- 9.2.3 The generalized distributive law (p.108) `L:3178`
- 9.2.4 JTA applied to a chain (p.109) `L:3220`
- 9.2.5 JTA for general temporal graphical models (p.110) `L:3256`
- 9.3.2 The marginal polytope (p.113) `L:3338`
- 9.3.3 Linear programming relaxation (p.114) `L:3373`
- 10 Variational inference (p.122) `L:3519`
- 10.1.2 Example: Full-rank vs rank-1 GVI for logistic regression (p.124) `L:3573`
- 10.1.3 Structured (sparse) Gaussian VI (p.125) `L:3577`
- 10.3 Beyond mean field (p.129) `L:3776`
- 10.3.1 Exploiting partial conjugacy (p.129) `L:3780`
- 10.3.2 Structured mean for factorial HMMs (p.133) `L:3933`
- 10.4 VI for graphical model inference (p.135) `L:3992`
- 10.4.5 Tree-reweighted belief propagation (p.141) `L:4227`
- 12 Markov Chain Monte Carlo (MCMC) inference (p.146) `L:4283`
- 13 Sequential Monte Carlo (SMC) inference (p.148) `L:4285`
- 13.1 More applications of particle filtering (p.148) `L:4287`
- 13.1.1 1d pendulum model with outliers (p.148) `L:4291`
- 13.1.2 Visual object tracking (p.148) `L:4295`
- 13.1.3 Online parameter estimation (p.150) `L:4313`
- 13.1.4 Monte Carlo robot localization (p.150) `L:4319`
- 13.2.2 Particle Independent Metropolis Hastings (p.152) `L:4368`
- 15 Generalized linear models (p.160) `L:4429`
- 15.1 Variational inference for logistic regression (p.160) `L:4431`
- 15.1.1 Binary logistic regression (p.160) `L:4435`
- 15.2 Converting multinomial logistic regression to Poisson regression (p.166) `L:4681`
- 15.2.1 Beta-binomial logistic regression (p.166) `L:4710`
- 15.2.2 Poisson regression (p.167) `L:4763`
- 15.2.3 GLMM (hierarchical Bayes) regression (p.168) `L:4796`
- 16 Deep neural networks (p.172) `L:4867`
- 16.1 More canonical examples of neural networks (p.172) `L:4869`
- 16.1.2 Graph neural networks (GNNs) (p.174) `L:4911`
- 17 Bayesian neural networks (p.180) `L:4995`
- 17.1 More details on EKF for training MLPs (p.180) `L:4997`
- 17.1.1 Global EKF (p.180) `L:5001`
- 17.1.2 Decoupled EKF (p.180) `L:5027`
- 18 Gaussian processes (p.182) `L:5062`
- 18.1 Deep GPs (p.182) `L:5064`
- 21 Variational autoencoders (p.194) `L:5237`
- 21.0.1 VAEs with missing data (p.194) `L:5239`
- 28 Latent factor models (p.212) `L:5295`
- 28.1 Inference in topic models (p.212) `L:5297`
- 29 State-space models (p.218) `L:5496`
- 29.1 Continuous time SSMs (p.218) `L:5498`
- 29.1.2 Example: Noiseless 1d spring-mass system (p.219) `L:5529`
- 29.1.3 Example: tracking a moving object in continuous time (p.220) `L:5579`
- 29.1.4 Example: tracking a particle in 2d (p.223) `L:5660`
- 29.2 Structured State Space Sequence model (S4) (p.223) `L:5672`
- 30 Graph learning (p.226) `L:5729`
- 30.1 Latent variable models for graphs (p.226) `L:5731`
- 30.1.1 Stochastic block model (p.226) `L:5735`
- 30.1.2 Mixed membership stochastic block model (p.228) `L:5779`
- 30.2 Learning tree structures (p.232) `L:5854`
- 30.2.1 Chow-Liu algorithm (p.232) `L:5858`
- 30.2.2 Finding the MAP forest (p.233) `L:5897`
- 30.3 Learning DAG structures (p.235) `L:5934`
- 30.3.1 Faithfulness (p.235) `L:5938`
- 30.3.4 Bayesian model selection: algorithms (p.240) `L:6077`
- 30.3.4.1 The K2 algorithm for known node orderings (p.240) `L:6081`
- 30.3.5 Constraint-based approach (p.242) `L:6130`
- 30.3.6 Methods based on sparse optimization (p.245) `L:6164`
- 30.3.7 Consistent estimators (p.245) `L:6187`
- 30.3.8 Handling latent variables (p.246) `L:6195`
- 30.4 Learning undirected graph structures (p.254) `L:6368`
- 30.5 Learning causal DAGs (p.260) `L:6499`
- 30.5.1 Learning cause-effect pairs (p.260) `L:6511`
- 30.5.2 Learning causal DAGs from interventional data (p.264) `L:6597`
- 30.5.3 Learning from low-level inputs (p.264) `L:6609`
- 31 Non-parametric Bayesian models (p.266) `L:6615`
- 31.1 Dirichlet processes (p.266) `L:6619`
- 31.1.2 Stick breaking construction of the DP (p.268) `L:6681`
- 31.1.3 The Chinese restaurant process (CRP) (p.270) `L:6718`
- 31.2 Dirichlet process mixture models (p.271) `L:6749`
- 31.2.2 Fitting using collapsed Gibbs sampling (p.273) `L:6787`
- 31.2.4 Other fitting algorithms (p.277) `L:6942`
- 31.2.5 Choosing the hyper-parameters (p.278) `L:6952`
- 31.3 Generalizations of the Dirichlet process (p.278) `L:6956`
- 31.3.1 Pitman-Yor process (p.278) `L:6960`
- 31.4 The Indian buffet process and the beta process (p.282) `L:7053`
- 31.5 Small-variance asymptotics (p.285) `L:7097`
- 31.6 Completely random measures (p.288) `L:7174`
- 31.7 Lévy processes (p.289) `L:7192`
- 31.8 Point processes with repulsion and reinforcement (p.291) `L:7214`
- 31.8.2 Renewal process (p.292) `L:7241`
- 31.8.4 Gibbs point process (p.295) `L:7277`
- Supplementary Material for "Probabilistic Machine Learning: Advanced Topics" `L:1`
- Part I (p.12) `L:262`
- Part II (p.50) `L:1178`
- Part III (p.156) `L:4423`
- Part IV (p.190) `L:5231`
- Part V (p.208) `L:5289`
- Part VI (p.304) `L:7350`
