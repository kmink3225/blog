---
name: "Probabilistic Machine Learning: Advanced Topics"
type: book-summary
source_file: "Murphy-PMLAdvanced_azure_full.md"
authors: "Kevin P. Murphy"
year: 2023
total_pages: 1211
language: en
keywords: [probabilistic ML, Bayesian inference, variational inference, MCMC, generative models, VAE, normalizing flows, diffusion models, GAN, Gaussian processes, reinforcement learning, causality, graphical models, state-space models, representation learning]
---

# Probabilistic Machine Learning: Advanced Topics — Summary

> Kevin P. Murphy (2023), 1211 pages, 36 chapters (6 Parts)
> 확률적 머신러닝의 고급 주제를 추론, 예측, 생성, 발견, 행동의 관점에서 체계적으로 다루는 심화 교과서이다.

## Contents

**Part I: Fundamentals**
1. Introduction
2. Probability
3. Statistics
4. Graphical models
5. Information theory
6. Optimization

**Part II: Inference**
7. Inference algorithms: an overview
8. Gaussian filtering and smoothing
9. Message passing algorithms
10. Variational inference
11. Monte Carlo methods
12. Markov chain Monte Carlo
13. Sequential Monte Carlo

**Part III: Prediction**
14. Predictive models: an overview
15. Generalized linear models
16. Deep neural networks
17. Bayesian neural networks
18. Gaussian processes
19. Beyond the iid assumption

**Part IV: Generation**
20. Generative models: an overview
21. Variational autoencoders
22. Autoregressive models
23. Normalizing flows
24. Energy-based models
25. Diffusion models
26. Generative adversarial networks

**Part V: Discovery**
27. Discovery methods: an overview
28. Latent factor models
29. State-space models
30. Graph learning
31. Nonparametric Bayesian models
32. Representation learning
33. Interpretability

**Part VI: Action**
34. Decision making under uncertainty
35. Reinforcement learning
36. Causality

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-2)

**핵심**: 이 책의 구조와 범위를 개괄한다. 기초, 추론, 예측, 생성, 발견, 행동의 여섯 파트로 구성되며, 확률적 머신러닝의 고급 주제를 통합적으로 다룬다.

**키워드**: `probabilistic ML`, `advanced topics`, `book overview`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 1 (line 97)

### Ch 2: Probability (pp. 5-62)

**핵심**: 고급 확률 이론을 다룬다. 측도론적 확률, 다변량 가우시안의 고급 성질, 확률적 그래프 모형의 수학적 기초, 확률 부등식, 마르코프 연쇄의 수렴 이론을 설명한다.

**키워드**: `measure theory`, `multivariate Gaussian`, `Markov chains`, `probability inequalities`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 2 (line 1826)

### Ch 3: Statistics (pp. 63-142)

**핵심**: 고급 통계적 추론을 다룬다. 빈도론적 추정이론(충분통계량, 래오-블랙웰, 피셔 정보), 베이지안 통계(계층적 모형, 경험적 베이즈), 점근 이론, 인과 추론의 기초를 설명한다.

**키워드**: `Fisher information`, `hierarchical Bayes`, `empirical Bayes`, `asymptotic theory`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 3 (line 5800)

### Ch 4: Graphical models (pp. 143-218)

**핵심**: 그래프 모형의 고급 이론을 다룬다. 유향 그래프 모형(DGM), 비유향 그래프 모형(UGM), 조건부 랜덤 필드(CRF), 인수 그래프, 그래프 구조 학습을 설명한다.

**키워드**: `DGM`, `UGM`, `CRF`, `factor graphs`, `structure learning`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 4 (line 12540)

### Ch 5: Information theory (pp. 219-260)

**핵심**: 정보이론의 고급 주제를 다룬다. 최대 엔트로피 원리, 정보 기하학, 최적 수송, 레이트-왜곡 이론을 설명한다.

**키워드**: `maximum entropy`, `information geometry`, `optimal transport`, `rate-distortion`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 5 (line 52)

### Ch 6: Optimization (pp. 261-342)

**핵심**: 고급 최적화 방법을 다룬다. 자연 그래디언트, 미러 디센트, 프록시멀 방법, 분산 최적화, 이중 목적 방법, 조합 최적화를 설명한다.

**키워드**: `natural gradient`, `mirror descent`, `proximal methods`, `distributed optimization`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 6 (line 19644)

### Ch 7: Inference algorithms: an overview (pp. 345-358)

**핵심**: 추론 알고리즘의 개요를 제공한다. 정확한 추론과 근사 추론의 분류, 결정론적 근사(변분법, 라플라스) 대 확률적 근사(MCMC, SMC)의 장단점을 비교한다.

**키워드**: `exact inference`, `approximate inference`, `deterministic`, `stochastic`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 7 (line 55)

### Ch 8: Gaussian filtering and smoothing (pp. 359-400)

**핵심**: 가우시안 필터링과 스무딩을 다룬다. 칼만 필터, 확장 칼만 필터(EKF), 무향 칼만 필터(UKF), 라우흐-퉁-스트리벨(RTS) 스무더, 가우시안 합 필터를 설명한다.

**키워드**: `Kalman filter`, `EKF`, `UKF`, `RTS smoother`, `Gaussian sum filter`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 8 (line 56)

### Ch 9: Message passing algorithms (pp. 401-438)

**핵심**: 메시지 전달 알고리즘을 다룬다. 신뢰 전파(BP), 접합 트리 알고리즘, 변분 메시지 전달, 기대 전파(EP)를 설명한다.

**키워드**: `belief propagation`, `junction tree`, `variational message passing`, `expectation propagation`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 9 (line 57)

### Ch 10: Variational inference (pp. 439-482)

**핵심**: 변분 추론을 다룬다. 평균장 근사, 좌표 상승 변분 추론(CAVI), 확률적 변분 추론(SVI), 재매개변수화 트릭, 변분 오토인코더(VAE)와의 연결을 설명한다.

**키워드**: `mean field`, `CAVI`, `SVI`, `reparameterization trick`, `ELBO`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 10 (line 58)

### Ch 11: Monte Carlo methods (pp. 483-498)

**핵심**: 몬테카를로 방법을 다룬다. 몬테카를로 적분, 중요도 샘플링, 거부 샘플링, 순열 검정, 부트스트랩을 설명한다.

**키워드**: `Monte Carlo integration`, `importance sampling`, `rejection sampling`, `bootstrap`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 11 (line 59)

### Ch 12: Markov chain Monte Carlo (pp. 499-542)

**핵심**: MCMC 방법을 다룬다. 메트로폴리스-헤이스팅스, 깁스 샘플링, 해밀턴 몬테카를로(HMC), NUTS, 수렴 진단, 템퍼링을 설명한다.

**키워드**: `Metropolis-Hastings`, `Gibbs`, `HMC`, `NUTS`, `convergence diagnostics`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 12 (line 60)

### Ch 13: Sequential Monte Carlo (pp. 543-572)

**핵심**: 순차적 몬테카를로(SMC) 방법을 다룬다. 입자 필터, 보조 입자 필터, 라오-블랙웰화 입자 필터, SMC 샘플러를 설명한다.

**키워드**: `particle filter`, `auxiliary particle filter`, `Rao-Blackwellization`, `SMC sampler`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 13 (line 61)

### Ch 14: Predictive models: an overview (pp. 575-590)

**핵심**: 예측 모형의 개요를 제공한다. 판별 모형 대 생성 모형, 모형 선택과 정규화, 앙상블 방법의 관점에서 예측 모형을 분류한다.

**키워드**: `discriminative models`, `generative models`, `model selection`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 14 (line 63)

### Ch 15: Generalized linear models (pp. 591-630)

**핵심**: 일반화 선형 모형의 고급 주제를 다룬다. 베이지안 GLM, 프로빗/로빗 회귀, 다항 로지스틱 회귀, 서수 회귀, 다중과제 학습을 설명한다.

**키워드**: `Bayesian GLM`, `probit`, `ordinal regression`, `multi-task learning`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 15 (line 64)

### Ch 16: Deep neural networks (pp. 631-646)

**핵심**: 심층 신경망의 고급 주제를 다룬다. 정규화 기법, 신경 아키텍처 탐색(NAS), 트랜스포머 아키텍처의 변형, 그래프 신경망(GNN)을 설명한다.

**키워드**: `NAS`, `transformer variants`, `GNN`, `regularization`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 16 (line 65)

### Ch 17: Bayesian neural networks (pp. 647-680)

**핵심**: 베이지안 신경망을 다룬다. 사후분포 근사(라플라스, 변분 추론, MCMC, 드롭아웃), 불확실성 정량화, 신경 네트워크 가우시안 과정(NNGP), 심층 커널 학습을 설명한다.

**키워드**: `Bayesian neural networks`, `uncertainty quantification`, `NNGP`, `deep kernel learning`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 17 (line 66)

### Ch 18: Gaussian processes (pp. 681-734)

**핵심**: 가우시안 과정의 고급 주제를 다룬다. 희소 GP(유도점 방법), 심층 GP, 비가우시안 우도, 다중출력 GP, 베이지안 최적화를 설명한다.

**키워드**: `sparse GP`, `inducing points`, `deep GP`, `Bayesian optimization`, `multi-output GP`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 18 (line 47308)

### Ch 19: Beyond the iid assumption (pp. 735-770)

**핵심**: iid 가정을 넘어서는 방법을 다룬다. 분포 이동(공변량 이동, 개념 이동), 도메인 적응, 분포 외(OOD) 탐지, 데이터 증강, 공정성과 편향을 설명한다.

**키워드**: `distribution shift`, `domain adaptation`, `OOD detection`, `fairness`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 19 (line 68)

### Ch 20: Generative models: an overview (pp. 773-790)

**핵심**: 생성 모형의 개요를 제공한다. 밀도 추정, 잠재변수 모형, 암묵적 생성 모형, 에너지 기반 모형, 스코어 기반 모형의 분류와 비교를 설명한다.

**키워드**: `density estimation`, `latent variable models`, `implicit generative models`, `score-based`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 20 (line 74)

### Ch 21: Variational autoencoders (pp. 791-820)

**핵심**: 변분 오토인코더(VAE)를 다룬다. ELBO, 재매개변수화 트릭, 조건부 VAE, beta-VAE, VQ-VAE, 계층적 VAE를 설명한다.

**키워드**: `VAE`, `ELBO`, `reparameterization`, `beta-VAE`, `VQ-VAE`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 21 (line 75)

### Ch 22: Autoregressive models (pp. 821-828)

**핵심**: 자기회귀 모형을 다룬다. 자기회귀 밀도 추정, MADE, PixelCNN, WaveNet, 자기회귀 흐름을 설명한다.

**키워드**: `autoregressive`, `MADE`, `PixelCNN`, `WaveNet`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 22 (line 76)

### Ch 23: Normalizing flows (pp. 829-848)

**핵심**: 정규화 흐름을 다룬다. 변수 변환, 평면/방사 흐름, RealNVP, GLOW, 연속 정규화 흐름(신경 ODE), 잔차 흐름을 설명한다.

**키워드**: `normalizing flows`, `RealNVP`, `GLOW`, `neural ODE`, `continuous flows`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 23 (line 77)

### Ch 24: Energy-based models (pp. 849-866)

**핵심**: 에너지 기반 모형을 다룬다. 볼츠만 분포, 제한 볼츠만 머신(RBM), 대비 발산(CD), 스코어 매칭, 잡음 대비 추정(NCE)을 설명한다.

**키워드**: `EBM`, `RBM`, `contrastive divergence`, `score matching`, `NCE`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 24 (line 78)

### Ch 25: Diffusion models (pp. 867-892)

**핵심**: 확산 모형을 다룬다. 잡음제거 확산 확률 모형(DDPM), 스코어 기반 생성 모형, 확률 미분 방정식(SDE) 관점, 조건부 생성, 가이던스 방법을 설명한다.

**키워드**: `DDPM`, `score-based`, `SDE`, `conditional generation`, `guidance`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 25 (line 58993)

### Ch 26: Generative adversarial networks (pp. 893-924)

**핵심**: 생성적 적대 신경망(GAN)을 다룬다. GAN 학습, 와서스타인 GAN, 조건부 GAN, StyleGAN, 모드 붕괴, 안정적 학습 기법을 설명한다.

**키워드**: `GAN`, `Wasserstein GAN`, `StyleGAN`, `mode collapse`, `conditional GAN`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 26 (line 80)

### Ch 27: Discovery methods: an overview (pp. 927-928)

**핵심**: 데이터에서 구조와 패턴을 발견하는 방법의 개요를 제공한다. 잠재 인자 모형, 상태 공간 모형, 그래프 학습 등 발견 방법의 분류를 설명한다.

**키워드**: `discovery`, `structure learning`, `latent factors`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 27 (line 82)

### Ch 28: Latent factor models (pp. 929-978)

**핵심**: 잠재 인자 모형을 다룬다. 인자 분석, 확률적 PCA, 독립 성분 분석(ICA), 토픽 모형(LDA), 비음수 행렬 분해(NMF), 행렬/텐서 분해를 설명한다.

**키워드**: `factor analysis`, `ICA`, `LDA`, `NMF`, `matrix factorization`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 28 (line 83)

### Ch 29: State-space models (pp. 979-1042)

**핵심**: 상태 공간 모형을 다룬다. 선형 가우시안 SSM, 비선형/비가우시안 SSM, 전환 SSM, 딥 상태 공간 모형(S4 등), 연속 시간 SSM(ODE)을 설명한다.

**키워드**: `SSM`, `linear Gaussian`, `switching SSM`, `deep SSM`, `S4`, `ODE`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 29 (line 84)

### Ch 30: Graph learning (pp. 1043-1046)

**핵심**: 그래프 구조 학습을 다룬다. DAG 구조 학습, 비방향 그래프 구조 학습, 인과 DAG 학습 방법을 설명한다.

**키워드**: `DAG learning`, `structure learning`, `causal discovery`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 30 (line 85)

### Ch 31: Nonparametric Bayesian models (pp. 1047-1048)

**핵심**: 비모수 베이지안 모형을 다룬다. 디리클레 과정(DP), DP 혼합 모형, 인도 뷔페 과정, 가우시안 과정의 비모수적 관점을 설명한다.

**키워드**: `Dirichlet process`, `DP mixture`, `Indian buffet process`, `nonparametric Bayes`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 31 (line 86)

### Ch 32: Representation learning (pp. 1049-1072)

**핵심**: 표현 학습을 다룬다. 자기지도학습(대비 학습, SimCLR, BYOL), 분리된 표현 학습, 전이 학습, 다중모달 표현을 설명한다.

**키워드**: `self-supervised learning`, `contrastive learning`, `SimCLR`, `disentangled representations`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 32 (line 87)

### Ch 33: Interpretability (pp. 1073-1102)

**핵심**: 해석가능성을 다룬다. 특징 귀속 방법(SHAP, LIME, 기울기 기반), 개념 기반 설명, 반사실적 설명, 내재적 해석가능 모형을 설명한다.

**키워드**: `SHAP`, `LIME`, `feature attribution`, `counterfactual explanations`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 33 (line 88)

### Ch 34: Decision making under uncertainty (pp. 1105-1144)

**핵심**: 불확실성 하의 결정을 다룬다. 베이지안 결정이론, 밴디트 문제(탐색-활용), 베이지안 최적화, 실험 설계, 능동학습을 설명한다.

**키워드**: `Bayesian decision theory`, `bandit`, `Bayesian optimization`, `experimental design`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 34 (line 90)

### Ch 35: Reinforcement learning (pp. 1145-1184)

**핵심**: 강화학습을 다룬다. 마르코프 결정 과정(MDP), 가치 기반 방법(Q-러닝), 정책 그래디언트, 액터-크리틱, 모델 기반 RL, 역강화학습, 오프라인 RL을 설명한다.

**키워드**: `MDP`, `Q-learning`, `policy gradient`, `actor-critic`, `model-based RL`, `offline RL`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 35 (line 91)

### Ch 36: Causality (pp. 1185-1211)

**핵심**: 인과성을 다룬다. 구조적 인과 모형(SCM), do-연산, 반사실, 도구변수, 이중차분법, 인과 발견 알고리즘을 설명한다.

**키워드**: `SCM`, `do-calculus`, `counterfactuals`, `instrumental variables`, `causal discovery`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 36 (line 78249)
