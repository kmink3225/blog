---
name: "Probabilistic Machine Learning: Advanced Topics"
type: book-summary
authors: "Kevin P. Murphy"
year: 2023
total_pages: 1211
language: en
keywords: [probabilistic ML, Bayesian inference, variational inference, MCMC, generative models, VAE, normalizing flows, diffusion models, GAN, Gaussian processes, reinforcement learning, causality, graphical models, state-space models, representation learning]
sources:
  - file: "Murphy-PMLAdvanced_marker_full.md"
    tool: Marker
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

이 책은 확률적 머신러닝의 고급 주제를 기초(Part I), 추론(Part II), 예측(Part III), 생성(Part IV), 발견(Part V), 행동(Part VI)의 여섯 파트로 나누어 체계적으로 다룬다. 현재 머신러닝의 상당 부분이 입력을 출력으로 매핑하는 함수 근사에 치중되어 있으나, 이 책은 데이터의 잠재 구조를 이해하는 모형 기반 접근법을 채택한다. 예측 모형은 조건부 분포 p(y|x)를 학습하여 분류와 회귀 문제를 다루며, 생성 모형은 p(x) 또는 p(x|c) 형태로 이미지·텍스트 등 고차원 출력을 생성한다. 잠재변수 모형은 p(z,x)=p(z)p(x|z) 형태로 관측 데이터 이면의 의미 있는 구조를 발견하는 데 사용된다. 마지막으로 불확실성 하의 의사결정과 인과추론까지 포괄하여 머신러닝의 범위를 넓힌다. 저자는 베이지안 추론을 핵심 프레임워크로 삼아, 확률 모형을 통해 데이터 생성 과정의 간결한 표현을 학습하는 것을 목표로 한다. 강건하고 데이터 효율적인 시스템 구축을 위해 분포 변화, 인과 추론, 순차적 의사결정 등 현실적 문제들을 다룬다. 이 책의 전작인 [Mur22]가 기본적인 ML 기법을 다루었다면, 본서는 보다 심화된 연구 전선까지 깊이 들어간다. 대부분의 그림에 대해 JAX 기반 Python 코드를 제공하여 재현성을 보장한다. 전체적으로 예측·생성·발견·행동이라는 네 가지 과제 축을 중심으로 확률적 ML의 통합적 관점을 제시한다.

### Ch 2: Probability (pp. 5-62)

**핵심**: 고급 확률 이론을 다룬다. 측도론적 확률, 다변량 가우시안의 고급 성질, 확률적 그래프 모형의 수학적 기초, 확률 부등식, 마르코프 연쇄의 수렴 이론을 설명한다.

**키워드**: `measure theory`, `multivariate Gaussian`, `Markov chains`, `probability inequalities`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 2 (line 1826)

확률 공간을 표본공간 Ω, 사건공간 F, 확률측도 P의 삼중쌍으로 정의하며, 이산 및 연속 확률변수의 측도론적 기초를 엄밀하게 다룬다. 콜모고로프 공리(비음수성, 정규화, 가산 가법성)로부터 조건부 확률과 베이즈 규칙을 도출한다. 이산 분포(범주형, 다항)와 연속 분포(가우시안, 감마, 베타 등)를 포괄적으로 정리하며, 다변량 가우시안의 조건부·주변부 분포 및 선형 가우시안 시스템의 고급 성질을 설명한다. 지수족 분포의 정의, 충분통계량, 로그 분배함수의 적률 생성 성질, 자연 매개변수와 평균 매개변수 간의 관계를 체계적으로 다룬다. 확률변수의 변환으로서 전사함수 변환, 몬테카를로 근사, 확률 적분 변환을 설명한다. 마르코프 연쇄의 매개변수화, 전이 행렬, 정상 분포의 수렴 이론을 다루며 언어 모형에의 응용을 보여 준다. f-발산(KL, 역KL 포함), 적분 확률 메트릭(IPM), 최대 평균 불일치(MMD), 총 변동 거리 등 확률 분포 간의 다양한 발산 측도를 비교한다. 밀도비 추정을 이진 분류기로 수행하는 방법까지 포함하여 생성 모형과 추론에 필요한 수학적 도구를 완비한다. 전체적으로 이 장은 이후 모든 장의 수학적 기반을 놓는 역할을 한다.

### Ch 3: Statistics (pp. 63-142)

**핵심**: 고급 통계적 추론을 다룬다. 빈도론적 추정이론(충분통계량, 래오-블랙웰, 피셔 정보), 베이지안 통계(계층적 모형, 경험적 베이즈), 점근 이론, 인과 추론의 기초를 설명한다.

**키워드**: `Fisher information`, `hierarchical Bayes`, `empirical Bayes`, `asymptotic theory`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 3 (line 5800)

베이지안 통계의 기초로서 동전 던지기 예제를 통해 사전분포, 우도, 사후분포의 관계를 설명하며, 계층적 모형과 경험적 베이즈(EB) 방법을 다룬다. 빈도론적 통계에서는 표본 분포, 부트스트랩 근사, MLE의 점근적 정규성, 피셔 정보 행렬의 성질과 크래머-라오 하한을 설명한다. 켤레 사전분포를 이항·다항·일변량/다변량 가우시안·지수족 모형에 체계적으로 적용하며, 정규-역위샤트(NIW) 분포를 통한 완전 켤레 사후분포를 유도한다. 비정보적 사전분포로 최대 엔트로피 사전분포, 제프리스 사전분포, 불변 사전분포, 참조 사전분포를 비교한다. 계층적 사전분포를 이항 및 가우시안 모형에 적용하며, 경험적 베이즈로 n-그램 스무딩과 비켤레 모형을 포함한 실용적 추정 방법을 제시한다. 모형 선택에서 베이지안 모형 선택, 주변 우도 추정, 교차검증과의 관계, 정보 기준(AIC, BIC, WAIC)을 비교 분석한다. 모형 검사를 위한 사후 예측 검사와 베이지안 p-값을 설명한다. 가설 검정에서 빈도론적 접근과 베이지안 접근(베이즈 인자)을 비교하며, 일반적 통계 검정이 선형 모형에서의 추론에 대응됨을 보인다. 결측 데이터 처리 메커니즘(MCAR, MAR, MNAR)과 그에 따른 추론 전략도 다룬다. 전반적으로 빈도론과 베이지안 관점을 균형 있게 제시하며 고급 통계 추론의 기반을 마련한다.

### Ch 4: Graphical models (pp. 143-218)

**핵심**: 그래프 모형의 고급 이론을 다룬다. 유향 그래프 모형(DGM), 비유향 그래프 모형(UGM), 조건부 랜덤 필드(CRF), 인수 그래프, 그래프 구조 학습을 설명한다.

**키워드**: `DGM`, `UGM`, `CRF`, `factor graphs`, `structure learning`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 4 (line 12540)

유향 그래프 모형(DGM, 베이즈 네트)은 결합 분포를 부모 노드에 대한 조건부 분포의 곱으로 분해하여 효율적으로 표현한다. 가우시안 베이즈 네트, 조건부 독립 성질(d-분리), 판 표기법(plate notation)을 포함한 DGM의 구조와 추론·학습 방법을 설명한다. 비유향 그래프 모형(UGM, 마르코프 랜덤 필드)은 결합 분포를 포텐셜 함수의 곱과 분배함수로 표현하며, 이징·포츠·홉필드 모형 등의 완전 가시 MRF와 볼츠만 머신 등 잠재변수 MRF를 다룬다. 최대 엔트로피 모형과 가우시안 MRF의 성질, UGM의 조건부 독립 성질(전역/지역/쌍별 마르코프 성질)을 설명한다. 조건부 랜덤 필드(CRF)를 1차원(체인 구조)과 2차원(격자 구조)에 대해 다루며, 매개변수 추정과 구조적 예측 방법을 설명한다. DGM과 UGM의 조건부 독립 성질을 비교하고, 두 표현 간의 변환(도덕화, 삼각화)과 레이블 편향 문제를 논의한다. 인수 그래프, 확률 회로, 유향/비유향 관계형 PGM, 개방 세계 확률 모형, 확률적 프로그래밍 등의 확장된 PGM을 다룬다. 구조적 인과 모형(SCM)의 기초로서 구조 방정식, do-연산자, 증강 DAG, 반사실을 소개하여 인과 추론과 그래프 모형의 연결을 제시한다. 전반적으로 확률적 그래프 모형의 표현력, 추론, 학습의 이론적 기반을 포괄적으로 정립한다.

### Ch 5: Information theory (pp. 219-260)

**핵심**: 정보이론의 고급 주제를 다룬다. 최대 엔트로피 원리, 정보 기하학, 최적 수송, 레이트-왜곡 이론을 설명한다.

**키워드**: `maximum entropy`, `information geometry`, `optimal transport`, `rate-distortion`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 5 (line 52)

KL 발산의 공리적 도출에서 출발하여, 유일하게 원하는 성질을 만족하는 발산 측도임을 증명하며, 전방 KL과 역방 KL의 서로 다른 최소화 특성(모드 커버링 대 모드 추구)을 비교한다. KL 발산과 MLE, 베이지안 추론, 지수족 분포, 피셔 정보 행렬, 브레그만 발산의 관계를 체계적으로 밝힌다. 엔트로피의 정의, 미분 엔트로피, 전형 집합(typical set), 교차 엔트로피와 혼란도(perplexity)를 다루며 정보론의 핵심 개념을 정립한다. 상호정보량(MI)의 정의, 해석, 데이터 처리 부등식, 충분통계량과의 관계를 설명하고, 다변량 MI(총 상관, 이중 총 상관, 상호작용 정보)까지 확장한다. MI에 대한 변분 하한(InfoNCE 등)과 상한을 소개하며 표현 학습에서의 활용 가능성을 제시한다. 데이터 압축(소스 코딩)에서 무손실 압축의 섀넌 부호화 정리와 손실 압축의 레이트-왜곡 절충, bits-back 코딩을 설명한다. 오류 정정 부호(채널 코딩)와 정보 병목(IB) 방법을 다루며, 변분 IB와 조건부 엔트로피 병목 등의 확장을 소개한다. 알고리즘 정보 이론에서 콜모고로프 복잡도와 솔로모노프 귀납을 통해 압축과 일반 지능의 관계를 논의한다. 관련 네트워크(relevance network)를 MI 기반으로 구성하는 방법과 그래프 모형과의 비교를 포함한다. 전체적으로 정보이론이 확률적 ML의 목적함수 설계, 모형 평가, 표현 학습에 어떻게 기여하는지를 통합적으로 보여 준다.

### Ch 6: Optimization (pp. 261-342)

**핵심**: 고급 최적화 방법을 다룬다. 자연 그래디언트, 미러 디센트, 프록시멀 방법, 분산 최적화, 이중 목적 방법, 조합 최적화를 설명한다.

**키워드**: `natural gradient`, `mirror descent`, `proximal methods`, `distributed optimization`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 6 (line 19644)

자동 미분(AD)을 함수적 형태의 미분, 연쇄·회로·프로그램의 미분으로 나누어 설명하며, 전방 모드와 역방 모드 AD의 계산 복잡도를 비교한다. 확률적 최적화에서 SGD, 유한합 목적함수 최적화, 분포 매개변수 최적화, 스코어 함수 추정기(REINFORCE), 재매개변수화 트릭, 검벨-소프트맥스 트릭을 다룬다. 자연 그래디언트 강하(NGD)를 피셔 정보 행렬 기반의 2차 방법으로 정의하고, 해석, 이점, 근사 방법(K-FAC 등), 지수족에서의 자연 그래디언트를 설명한다. 경계 최적화(MM) 알고리즘의 일반 원리를 제시하고, EM 알고리즘을 특수 경우로 유도하며 결측 데이터가 있는 가우시안과 강건 선형 회귀 예제를 포함한다. 베이지안 최적화(BO)에서 순차적 모형 기반 최적화, 대리 함수(가우시안 과정), 획득 함수(EI, UCB, Thompson 샘플링)를 설명한다. 미분 불가능 최적화(DFO)로 지역 탐색, 시뮬레이티드 어닐링, 진화 알고리즘, EDA, 교차 엔트로피 방법, 진화 전략, LLM 기반 DFO를 다룬다. 최적 수송(OT)에서 칸토로비치·몽주 정식화, 엔트로피 정규화, 싱크혼 알고리즘을 설명한다. 부분모듈러 최적화의 정의, 예제, 탐욕 알고리즘의 근사 보장, ML/AI에서의 응용(데이터 선택, 클러스터링, 능동학습 등)을 포괄적으로 다룬다. 전체적으로 ML에서 사용되는 1차·2차·조합론적 최적화 방법을 통합적으로 제시한다.

### Ch 7: Inference algorithms: an overview (pp. 345-358)

**핵심**: 추론 알고리즘의 개요를 제공한다. 정확한 추론과 근사 추론의 분류, 결정론적 근사(변분법, 라플라스) 대 확률적 근사(MCMC, SMC)의 장단점을 비교한다.

**키워드**: `exact inference`, `approximate inference`, `deterministic`, `stochastic`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 7 (line 55)

베이지안 추론의 핵심이 사후분포 및 기대값 계산에 있음을 명시하며, 사후 평균·MAP·주변 우도·사후 예측 분포 등 다양한 추론 목표를 통합적으로 기대값 형태로 표현한다. 추론 패턴을 전역 잠재변수(모형 매개변수), 지역 잠재변수(데이터별 잠재상태), 전역+지역 잠재변수의 세 가지로 분류한다. 정확한 추론이 가능한 경우(켤레 모형, 이산 잠재변수의 소진 등)와 불가능한 경우를 구별한다. 근사 추론 방법으로 MAP 근사와 그 한계(불확실성 과소평가), 격자 근사, 라플라스(2차) 근사를 설명한다. 변분 추론(VI)은 ELBO 최대화를 통해 다루기 쉬운 분포로 사후분포를 근사하며, MCMC는 마르코프 연쇄를 통해 사후분포에서 정확한 샘플을 생성한다. 순차적 몬테카를로(SMC)는 상태 공간 모형에서 온라인 추론을 수행한다. 다봉분포, 강한 상관, 고차원 등 사후분포가 도전적인 경우의 문제점을 논의한다. 근사 추론 알고리즘의 평가 방법으로 KL 발산, 유효 표본 크기 등의 진단 도구를 제시한다. 모형과 추론 엔진의 분리를 강조하며, 이를 "베이지안 크랭크 돌리기"라 표현한다. 이 장은 이후 추론 관련 장(Ch 8-13)의 로드맵 역할을 한다.

### Ch 8: Gaussian filtering and smoothing (pp. 359-400)

**핵심**: 가우시안 필터링과 스무딩을 다룬다. 칼만 필터, 확장 칼만 필터(EKF), 무향 칼만 필터(UKF), 라우흐-퉁-스트리벨(RTS) 스무더, 가우시안 합 필터를 설명한다.

**키워드**: `Kalman filter`, `EKF`, `UKF`, `RTS smoother`, `Gaussian sum filter`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 8 (line 56)

상태 공간 모형(SSM)에서의 추론 목표를 필터링(현재 상태 추정), 스무딩(과거 상태 수정), 예측의 세 가지로 구분한다. 베이지안 필터링 방정식(예측 단계와 갱신 단계)과 스무딩 방정식을 유도하며, 가우시안 가정(Gaussian ansatz)을 통해 닫힌 형태의 해를 얻는다. 선형 가우시안 SSM에서 칼만 필터의 예측·갱신 재귀식을 유도하고, 라우흐-퉁-스트리벨(RTS) 스무더의 역방향 패스를 설명한다. 정보 형태(information form)의 필터링과 스무딩을 다루어 희소 정밀도 행렬의 경우 계산 이점을 보인다. 비선형 SSM에 대해 테일러 전개 기반의 확장 칼만 필터(EKF)와 무향 변환 기반의 무향 칼만 필터(UKF)를 설명하며 각각의 장단점을 비교한다. 일반화된 가우시안 필터링, 조건부 적률 가우시안 필터링, 반복 필터/스무더, 앙상블 칼만 필터, 강건 칼만 필터 등 다양한 변형을 다룬다. 가정 밀도 필터링(ADF)을 소개하며, 전환 SSM(가우시안 합 필터), 온라인 로지스틱 회귀, 온라인 DNN에의 응용을 설명한다. 격자 기반 근사, 기대 전파(EP), 변분 추론, MCMC, 입자 필터 등 SSM을 위한 다른 추론 방법도 개관한다. 정규화 흐름 칼만 필터(NF-KF) 등 최신 확장도 포함한다. 전반적으로 가우시안 가정 하에서의 시계열 추론 방법을 체계적으로 정리한다.

### Ch 9: Message passing algorithms (pp. 401-438)

**핵심**: 메시지 전달 알고리즘을 다룬다. 신뢰 전파(BP), 접합 트리 알고리즘, 변분 메시지 전달, 기대 전파(EP)를 설명한다.

**키워드**: `belief propagation`, `junction tree`, `variational message passing`, `expectation propagation`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 9 (line 57)

체인 구조의 신뢰 전파(BP)를 은닉 마르코프 모형(HMM)에서 유도하며, 전방 알고리즘, 전방-역방 알고리즘, 비터비 알고리즘의 시간·공간 복잡도를 분석한다. 트리 구조로 BP를 확장하여 합-곱(sum-product) 알고리즘과 최대-곱(max-product) 알고리즘을 설명한다. 루피 신뢰 전파(loopy BP)를 쌍별 비유향 그래프와 인수 그래프에 적용하며, 가우시안 BP, 수렴성, 정확도, 일반화된 BP, 볼록 BP를 논의한다. 루피 BP의 응용으로 오류 정정 부호(LDPC)와 친화도 전파(affinity propagation) 클러스터링을 다루며, 그래프 신경망으로 BP를 모사하는 방법도 소개한다. 변수 소거(VE) 알고리즘의 유도, 계산 복잡도, 좋은 소거 순서 선택 전략을 설명하고, 정확한 추론의 NP-난해성을 언급한다. 접합 트리 알고리즘(JTA)은 VE를 일반화하여 모든 변수의 주변분포를 효율적으로 계산한다. 추론을 최적화 문제로 재해석하며, 역전파를 통한 추론과 교란-후-MAP(perturb-and-MAP) 방법을 설명한다. 전방-역방 샘플링(FFBS)을 통해 HMM에서의 정확한 사후 샘플링 방법을 제시한다. 전체적으로 정확한 추론이 가능한 트리 구조에서 근사가 필요한 일반 그래프까지의 메시지 전달 알고리즘을 체계적으로 다룬다.

### Ch 10: Variational inference (pp. 439-482)

**핵심**: 변분 추론을 다룬다. 평균장 근사, 좌표 상승 변분 추론(CAVI), 확률적 변분 추론(SVI), 재매개변수화 트릭, 변분 오토인코더(VAE)와의 연결을 설명한다.

**키워드**: `mean field`, `CAVI`, `SVI`, `reparameterization trick`, `ELBO`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 10 (line 58)

변분 목적함수(ELBO)를 로그 주변 우도의 하한으로 유도하며, 변분 사후분포의 형태 선택(평균장, 구조적, 정규화 흐름 등)에 따른 근사 정확도를 논의한다. 변분 EM을 통해 매개변수 추정과 잠재변수 추론을 교대로 수행하는 방법을 설명한다. 그래디언트 기반 VI로서 재매개변수화 VI(구체적 분포의 경우), 자동 미분 VI(ADVI), 블랙박스 변분 추론(BBVI)을 다룬다. 좌표 상승 변분 추론(CAVI)의 유도와 이징 모형·일변량 가우시안·가우시안 혼합 모형(GMM)에의 적용을 설명한다. 변분 메시지 전달(VMP)과 Autoconj를 통한 자동화된 CAVI를 소개한다. 더 정확한 변분 사후분포를 위해 구조적 평균장, 계층적(보조변수) 사후분포, 정규화 흐름 사후분포, 암묵적 사후분포, VI와 MCMC의 결합을 제시한다. 더 긴밀한 경계로 다중 샘플 ELBO(IWAE 경계), 열역학 변분 목적함수(TVO), 증거 상한(EUBO) 최소화를 다룬다. 웨이크-슬립 알고리즘의 웨이크/슬립/데이드림 단계를 설명하며, 기대 전파(EP)의 알고리즘·예제·일반화된 ADF와의 관계·파워 EP와 α-발산을 포함한다. 확률적 변분 추론(SVI)과 상각 추론(amortized inference)을 통해 대규모 데이터에의 확장성을 확보하는 방법을 설명한다. 전반적으로 결정론적 근사 추론의 가장 중요한 프레임워크를 포괄적으로 제시한다.

### Ch 11: Monte Carlo methods (pp. 483-498)

**핵심**: 몬테카를로 방법을 다룬다. 몬테카를로 적분, 중요도 샘플링, 거부 샘플링, 순열 검정, 부트스트랩을 설명한다.

**키워드**: `Monte Carlo integration`, `importance sampling`, `rejection sampling`, `bootstrap`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 11 (line 59)

몬테카를로 적분의 기본 원리를 소개하며, π 추정 예제를 통해 직관적으로 설명하고, 추정의 정확도가 1/√N 속도로 개선됨을 보인다. 단순 분포에서의 난수 생성 방법으로 역 누적분포함수(inverse cdf) 방법과 박스-뮬러(Box-Muller) 방법을 설명한다. 거부 샘플링(rejection sampling)의 기본 아이디어, 적응적 거부 샘플링, 고차원에서의 비효율성을 다룬다. 중요도 샘플링(importance sampling)으로 직접 중요도 샘플링, 자기정규화 중요도 샘플링, 제안 분포 선택, 어닐드 중요도 샘플링(AIS)을 설명한다. AIS는 중간 분포의 시퀀스를 통해 고차원에서도 효과적인 중요도 샘플링을 가능하게 한다. 몬테카를로 분산 제어 기법으로 공통 난수, 라오-블랙웰화, 제어 변량, 대칭(antithetic) 샘플링, 준-몬테카를로(QMC)를 다룬다. 라오-블랙웰화는 일부 변수를 해석적으로 적분하여 분산을 줄이며, 제어 변량은 기대값이 알려진 함수를 빼서 분산을 감소시킨다. QMC는 저불일치(low-discrepancy) 수열을 사용하여 균일 난수보다 빠른 수렴을 달성한다. 전반적으로 MCMC 이전 단계의 기본적 샘플링 방법과 분산 감소 기법을 체계적으로 정리한다. 이 장의 기법들은 이후 MCMC(Ch 12)와 SMC(Ch 13) 장의 구성 요소로 활용된다.

### Ch 12: Markov chain Monte Carlo (pp. 499-542)

**핵심**: MCMC 방법을 다룬다. 메트로폴리스-헤이스팅스, 깁스 샘플링, 해밀턴 몬테카를로(HMC), NUTS, 수렴 진단, 템퍼링을 설명한다.

**키워드**: `Metropolis-Hastings`, `Gibbs`, `HMC`, `NUTS`, `convergence diagnostics`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 12 (line 60)

메트로폴리스-헤이스팅스(MH) 알고리즘의 기본 아이디어와 상세 균형 조건을 통한 정당성을 증명하며, 랜덤 워크·독립·랑주뱅 제안 분포를 비교한다. 깁스 샘플링을 MH의 특수 경우로 도출하고, 이징·포츠·가우시안 혼합 모형에 적용하며, 메트로폴리스 내 깁스, 블록 깁스, 붕괴 깁스 샘플링을 설명한다. 보조변수 MCMC로 슬라이스 샘플링과 스웬드센-왕(Swendsen-Wang) 알고리즘을 다루어 다봉분포에서의 혼합 개선을 보인다. 해밀턴 몬테카를로(HMC)를 해밀턴 역학으로부터 유도하며, 도약 적분기(leapfrog integrator), HMC 튜닝, 리만 다양체 HMC, 랑주뱅 몬테카를로(MALA)를 설명한다. SGD와 랑주뱅 샘플링의 연결, 제약 조건이 있는 매개변수에 HMC를 적용하는 방법, HMC 가속화 기법을 다룬다. MCMC 수렴 진단으로 마르코프 연쇄의 혼합률, 실용적 진단(R-hat, 추적 그래프), 유효 표본 크기(ESS), 비중심 매개변수화(닐의 깔때기)를 설명한다. 확률적 그래디언트 MCMC(SG-MCMC)로 SGLD, 전조건화, 그래디언트 분산 감소, SG-HMC, 과소감쇠 랑주뱅을 다루어 대규모 데이터에의 확장을 논의한다. 가역 점프(초차원) MCMC를 통해 모형 차수가 다른 경우의 사후분포 탐색을 설명한다. 어닐링 방법으로 시뮬레이티드 어닐링과 병렬 템퍼링(replica exchange)을 다룬다. 전반적으로 MCMC의 이론·알고리즘·실용적 진단을 포괄적으로 정리한다.

### Ch 13: Sequential Monte Carlo (pp. 543-572)

**핵심**: 순차적 몬테카를로(SMC) 방법을 다룬다. 입자 필터, 보조 입자 필터, 라오-블랙웰화 입자 필터, SMC 샘플러를 설명한다.

**키워드**: `particle filter`, `auxiliary particle filter`, `Rao-Blackwellization`, `SMC sampler`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 13 (line 61)

순차적 몬테카를로(SMC)의 문제 정의를 상태 공간 모형에서의 온라인 추론과 정적 매개변수 추정의 두 가지로 구분한다. 입자 필터의 핵심 요소로 중요도 샘플링, 순차적 중요도 샘플링(SIS), 재표본추출 기반 SIS(SIR)를 단계적으로 유도한다. 재표본추출 방법(다항, 층화, 잔차, 체계적)을 비교하고, 유효 표본 크기(ESS) 기반의 적응적 재표본추출을 설명한다. 제안 분포로 부트스트랩 제안, 국소 최적 제안, EKF/UKF 기반 제안, 라플라스 근사 기반 제안, 중첩 SMC를 다룬다. 라오-블랙웰화 입자 필터(RBPF)를 소개하며, 칼만 필터 혼합, 기동하는 물체 추적, FastSLAM에의 응용을 설명한다. 보조 입자 필터(APF)를 포함한 입자 필터의 확장을 논의한다. SMC 샘플러를 정적 매개변수 추정 문제에 적용하며, 우도 템퍼링(기하 경로), 데이터 템퍼링, 희귀 사건 샘플링을 다룬다. 우도 없는 추론을 위한 SMC-ABC와 SMC² 알고리즘을 소개한다. 변분 필터링 SMC와 변분 스무딩 SMC를 통해 심층 생성 모형과의 결합 가능성을 제시한다. 전체적으로 온라인 베이지안 추론과 정적 추론에서의 입자 기반 방법을 체계적으로 정리한다.

### Ch 14: Predictive models: an overview (pp. 575-590)

**핵심**: 예측 모형의 개요를 제공한다. 판별 모형 대 생성 모형, 모형 선택과 정규화, 앙상블 방법의 관점에서 예측 모형을 분류한다.

**키워드**: `discriminative models`, `generative models`, `model selection`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 14 (line 63)

예측 모형 p(y|x)를 모수 모형과 비모수 모형으로 대별하며, 비모수 모형(가우시안 과정, K-최근접 이웃)은 훈련 집합 크기에 따라 매개변수 수가 증가한다. 모수 모형은 GLM(선형), DNN(비선형 미분가능 함수) 등의 형태를 가지며, 모형 적합에 MLE, MAP, ERM을 사용한다. 베이지안 적합 방법으로 완전 베이지안, 변분 추론, 일반화 베이지안(tempered posterior)을 설명하며, 각 방법의 장단점을 비교한다. 예측 모형 평가를 위한 적절 스코어링 규칙(proper scoring rules)로 로그 확률, 브라이어 스코어 등을 소개한다. 교정(calibration)의 개념을 정의하고, 신뢰도 다이어그램, 기대 교정 오차(ECE), 온도 스케일링에 의한 사후 교정을 설명한다. 주변 확률 평가를 넘어서는 방법으로 적절한 다변량 스코어링 규칙과 결정론적 첨예도(sharpness)를 논의한다. 순응 예측(conformal prediction)을 분포 무관 불확실성 정량화 방법으로 소개하며, 분류·회귀·베이지안 모형에의 적용을 다룬다. 교정 집합이 없는 경우의 분할 전략과 일반적 순응 예측/결정 문제까지 확장한다. 전반적으로 예측 모형의 유형, 적합, 평가, 불확실성 정량화에 대한 통합적 틀을 제공한다. 이 장은 이후 구체적 예측 모형(Ch 15-19)의 공통 기반을 마련한다.

### Ch 15: Generalized linear models (pp. 591-630)

**핵심**: 일반화 선형 모형의 고급 주제를 다룬다. 베이지안 GLM, 프로빗/로빗 회귀, 다항 로지스틱 회귀, 서수 회귀, 다중과제 학습을 설명한다.

**키워드**: `Bayesian GLM`, `probit`, `ordinal regression`, `multi-task learning`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 15 (line 64)

GLM의 정의로 정준 연결함수와 비정준 연결함수를 구분하며, 선형 회귀·로지스틱 회귀·포아송 회귀 등 대표적 GLM을 소개한다. 베이지안 선형 회귀에서 켤레 사전분포(정규-역감마), 비정보적 사전분포, 정보적 사전분포, 스파이크-앤-슬랩, 라플라스(베이지안 라쏘), 호스슈(horseshoe), 자동 관련성 결정(ARD) 등 다양한 사전분포를 비교한다. 다변량 선형 회귀로 다중 출력을 동시에 모형화하는 방법을 설명한다. 이항 로지스틱 회귀의 베이지안 추론에서 라플라스 근사, 사후 예측 분포 근사(프로빗 근사, 몬테카를로), MCMC 추론을 다루며, 버클리 입학 편향 사례 연구를 포함한다. 다항 로지스틱 회귀, 클래스 불균형과 긴 꼬리 처리, 매개변수 사전분포 선택을 논의한다. 프로빗 회귀를 잠재변수 해석으로 유도하고, 서수(ordinal) 프로빗 회귀와 다항 프로빗 모형을 설명한다. 다수준(계층적) GLM으로 일반화 선형 혼합 모형(GLMM)을 소개하며, 라돈 회귀 예제를 통해 부분 풀링(partial pooling)의 이점을 보인다. 전반적으로 GLM의 베이지안 처리, 다양한 사전분포에 의한 정규화, 계층적 확장을 체계적으로 제시한다. 이 장의 방법들은 베이지안 신경망(Ch 17)의 기반이 된다.

### Ch 16: Deep neural networks (pp. 631-646)

**핵심**: 심층 신경망의 고급 주제를 다룬다. 정규화 기법, 신경 아키텍처 탐색(NAS), 트랜스포머 아키텍처의 변형, 그래프 신경망(GNN)을 설명한다.

**키워드**: `NAS`, `transformer variants`, `GNN`, `regularization`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 16 (line 65)

미분 가능 회로의 구성 요소로 선형 층, 비선형 활성화 함수, 합성곱 층, 잔차(스킵) 연결, 정규화 층(배치/레이어/그룹/인스턴스), 드롭아웃 층을 설명한다. 어텐션 층을 자기 어텐션과 교차 어텐션으로 나누어 다루며, 스케일드 닷-프로덕트 어텐션과 다중 헤드 어텐션의 구조를 설명한다. 순환 층(LSTM, GRU 포함), 곱셈 층(게이트, 하이퍼네트워크), 암묵적 층(신경 ODE, 심층 평형 모형)을 소개한다. 대표적 신경망 아키텍처로 다층 퍼셉트론(MLP), 합성곱 신경망(CNN), 오토인코더, 순환 신경망(RNN), 트랜스포머를 정리한다. 트랜스포머의 인코더-디코더 구조, 위치 인코딩, 인과적 마스킹을 설명한다. 그래프 신경망(GNN)을 메시지 전달 신경망(MPNN)의 관점에서 소개하며, 그래프 합성곱, 그래프 어텐션, 읽기/풀링 함수를 다룬다. 전반적으로 각 구성 요소의 역할과 결합 방식을 명확히 하여 후속 장(BNN, GP, 생성 모형 등)에서 활용할 기반을 제공한다. 신경 아키텍처 탐색(NAS), 지식 증류 등 고급 주제도 간략히 언급한다. DNN의 범용 근사 성질과 깊이의 이점에 대한 이론적 논의를 포함한다. 이 장은 이전 책 [Mur22]의 DNN 내용을 고급 관점에서 보완하는 역할을 한다.

### Ch 17: Bayesian neural networks (pp. 647-680)

**핵심**: 베이지안 신경망을 다룬다. 사후분포 근사(라플라스, 변분 추론, MCMC, 드롭아웃), 불확실성 정량화, 신경 네트워크 가우시안 과정(NNGP), 심층 커널 학습을 설명한다.

**키워드**: `Bayesian neural networks`, `uncertainty quantification`, `NNGP`, `deep kernel learning`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 17 (line 66)

BNN의 사전분포로 가우시안 사전분포, 희소성 촉진 사전분포, 학습 가능한 사전분포, 함수 공간 사전분포, 아키텍처 사전분포를 비교한다. 사후분포 근사 방법으로 몬테카를로 드롭아웃, 라플라스 근사(전체/최종층/크로네커 분해), 변분 추론(평균장 가우시안, 매트릭스 가우시안), 기대 전파를 설명한다. 최종 층 방법으로 선형 프로브와 SNGP(스펙트럼 정규화 가우시안 과정)를 소개하며, MCMC 방법(HMC, SGLD)과 SGD 궤적 기반 방법(SWAG, cSGLD)을 다룬다. 심층 앙상블(deep ensemble)의 효과와 한계를 논의하며, 하이퍼심층 앙상블과 배치 앙상블 등의 변형을 소개한다. 사후 예측 분포의 근사 방법으로 베이즈 모형 평균(BMA)과 베이즈 모형 결합(BMC)을 구분한다. 템퍼드 사후분포(cold posterior)의 경험적 성공과 이론적 해석을 논의한다. 일반화 이론으로 날카로운 대 평탄한 극솟값, 모드 연결성과 손실 지형, 유효 차원, DNN의 가설 공간, PAC-베이즈 경계를 다룬다. OOD 일반화와 BNN의 모형 선택(주변 우도 추정)을 설명한다. 온라인 추론으로 순차적 라플라스, 확장 칼만 필터, ADF, 온라인 변분 추론의 DNN 적용을 다룬다. 계층적 BNN을 통한 메타학습 관점의 사전분포 학습을 설명한다. 전반적으로 DNN에 베이지안 원리를 적용하여 불확실성을 정량화하는 방법을 포괄적으로 제시한다.

### Ch 18: Gaussian processes (pp. 681-734)

**핵심**: 가우시안 과정의 고급 주제를 다룬다. 희소 GP(유도점 방법), 심층 GP, 비가우시안 우도, 다중출력 GP, 베이지안 최적화를 설명한다.

**키워드**: `sparse GP`, `inducing points`, `deep GP`, `Bayesian optimization`, `multi-output GP`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 18 (line 47308)

가우시안 과정(GP)을 함수에 대한 분포로 정의하며, 머서 커널의 종류를 정상(SE, 마테른, 주기적)과 비정상(선형, 신경망) 커널, 비벡터 입력용 커널(문자열, 그래프)로 분류한다. 머서 정리와 랜덤 특징(Random Fourier Features)을 통한 커널 근사를 설명한다. 가우시안 우도에서의 GP 예측(노이즈 유무), 가중치 공간 대 함수 공간 관점, 주변 우도, 커널 릿지 회귀와의 관계를 다룬다. 비가우시안 우도(이진/다중 분류, 포아송 회귀, 콕스 과정)에 대한 GP 추론 방법을 라플라스 근사와 변분 추론을 중심으로 설명한다. 대규모 데이터에의 확장을 위해 데이터 부분집합, 뉘스트룀 근사, 유도점 방법(FITC, VFE), 희소 변분 방법(SVGP), 병렬화 및 구조 활용(KISS-GP), GP를 SSM으로 변환하는 방법을 다룬다. 커널 학습으로 경험적 베이즈, 베이지안 추론, 다중 커널 학습, 자동 합성 커널 탐색, 스펙트럼 혼합 커널, 심층 커널 학습을 설명한다. GP와 DNN의 관계로 무한 너비 DNN에서 유도되는 NN-GP, 신경 접선 커널(NTK), 심층 GP를 다룬다. 시계열 예측을 위한 GP의 응용(Mauna Loa CO₂ 예제)을 포함한다. 전반적으로 GP의 이론, 확장성, DNN과의 연결을 포괄적으로 제시한다.

### Ch 19: Beyond the iid assumption (pp. 735-770)

**핵심**: iid 가정을 넘어서는 방법을 다룬다. 분포 이동(공변량 이동, 개념 이동), 도메인 적응, 분포 외(OOD) 탐지, 데이터 증강, 공정성과 편향을 설명한다.

**키워드**: `distribution shift`, `domain adaptation`, `OOD detection`, `fairness`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 19 (line 68)

분포 이동(distribution shift)의 인과적 관점을 제시하며, 공변량 이동, 레이블 이동, 개념 이동, 데이터셋 이동의 네 가지 주요 유형을 분류한다. 분포 이동 탐지를 위한 이표본 검정과 단일 분포 외(OOD) 입력 탐지(소프트맥스 기반, 에너지 기반, 마할라노비스 거리 등)를 설명한다. 선택적 예측과 개방 집합/개방 세계 인식을 통한 신뢰할 수 없는 예측의 거부 전략을 다룬다. 분포 이동에 대한 강건성을 위해 데이터 증강과 분포적으로 강건한 최적화(DRO)를 설명한다. 분포 이동 적응으로 전이 학습(특징 추출, 미세 조정), 공변량 이동를 위한 가중 ERM, 비지도 도메인 적응(DANN 등), 레이블 이동를 위한 비지도 기법, 테스트 시점 적응을 다룬다. 다중 분포로부터의 학습으로 다중 과제 학습, 도메인 일반화, 불변 위험 최소화(IRM), 메타학습(MAML 등)을 설명한다. 연속 학습에서 도메인 표류, 개념 표류, 클래스 증분 학습, 파국적 망각과 그 완화 전략(정규화, 리플레이, 매개변수 격리)을 다룬다. 적대적 예제에 대해 화이트박스(FGSM, PGD)와 블랙박스 공격, 현실 세계 적대적 공격, 강건 최적화 기반 방어, 적대적 예제의 근본 원인을 논의한다. 온라인 학습의 기초(후회 최소화)도 포함한다. 전반적으로 iid 가정이 위반될 때의 진단·강건성·적응 전략을 체계적으로 제시한다.

### Ch 20: Generative models: an overview (pp. 773-790)

**핵심**: 생성 모형의 개요를 제공한다. 밀도 추정, 잠재변수 모형, 암묵적 생성 모형, 에너지 기반 모형, 스코어 기반 모형의 분류와 비교를 설명한다.

**키워드**: `density estimation`, `latent variable models`, `implicit generative models`, `score-based`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 20 (line 74)

생성 모형을 VAE, 자기회귀 모형(ARM), 정규화 흐름, 에너지 기반 모형(EBM), 확산 모형, GAN으로 분류하며, 학습 방법·잠재변수 사용 여부·아키텍처 제약 등의 기준으로 비교한다. 생성 모형의 목표로 데이터 생성(생성 AI), 밀도 추정, 결측값 대치(imputation), 구조 발견, 잠재 공간 보간 및 산술을 설명한다. 조건부 생성 모형 p(x|c)의 다양한 응용(텍스트→이미지, 이미지→텍스트, 이미지→이미지, 음성→텍스트, 기계 번역)을 제시한다. 생성적 설계, 모형 기반 강화학습, 표현 학습, 데이터 압축에의 활용을 논의한다. 생성 모형의 평가 방법으로 우도 기반 평가, 특징 공간에서의 거리와 발산(FID, IS), 정밀도와 재현율 메트릭, 통계적 검정을 다룬다. 사전 학습된 분류기 사용의 문제점, 모형 샘플을 이용한 분류기 학습에 의한 평가, 과적합 평가, 인간 평가를 포함한다. 각 생성 모형의 학습 목적함수(MLE, ELBO, 적대적 학습, 스코어 매칭 등)를 개관한다. 잠재변수가 있는 모형과 없는 모형의 장단점을 비교하며, 아키텍처 제약(가역성, 야코비안 계산 등)에 따른 유연성 차이를 논의한다. 전반적으로 생성 모형의 종류·목표·평가·학습 방법에 대한 통합적 분류 체계를 제공한다. 이 장은 이후 구체적 생성 모형(Ch 21-26)의 로드맵 역할을 한다.

### Ch 21: Variational autoencoders (pp. 791-820)

**핵심**: 변분 오토인코더(VAE)를 다룬다. ELBO, 재매개변수화 트릭, 조건부 VAE, beta-VAE, VQ-VAE, 계층적 VAE를 설명한다.

**키워드**: `VAE`, `ELBO`, `reparameterization`, `beta-VAE`, `VQ-VAE`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 21 (line 75)

VAE의 기본 구조를 인코더 q(z|x)와 디코더 p(x|z)의 결합으로 정의하며, ELBO의 유도와 재매개변수화 트릭을 통한 경사 기반 학습을 설명한다. VAE와 일반 오토인코더의 차이(확률적 잠재 공간, 정규화 효과)를 비교하고, 증강 공간에서의 최적화 관점을 제시한다. β-VAE를 통한 분리된 표현 학습과 InfoVAE(MMD 기반 정규화)를 포함한 VAE 일반화를 다룬다. 다중 모달 VAE(MVAE, MMVAE), 반지도 VAE, 순차적 인코더/디코더를 가진 VAE를 설명한다. 사후 붕괴(posterior collapse) 문제에 대해 KL 어닐링, 하한 제약, 자유 비트, 스킵 연결, 개선된 변분 추론, 대안적 목적함수 등의 해결 전략을 제시한다. 계층적 VAE에서 상향식 대 하향식 추론, 매우 깊은 VAE(NVAE 등), 자기회귀 모형과의 연결, 변분 가지치기를 설명한다. 벡터 양자화 VAE(VQ-VAE)를 이진 부호 오토인코더에서 출발하여 유도하며, 사전분포 학습(PixelCNN), 계층적 확장(VQ-VAE-2), 이산 VAE, VQ-GAN을 다룬다. 전반적으로 VAE의 이론·변형·실용적 문제 해결을 체계적으로 정리한다. VAE는 잠재 공간의 구조를 학습하면서 생성 품질을 향상시키는 핵심 프레임워크이다.

### Ch 22: Autoregressive models (pp. 821-828)

**핵심**: 자기회귀 모형을 다룬다. 자기회귀 밀도 추정, MADE, PixelCNN, WaveNet, 자기회귀 흐름을 설명한다.

**키워드**: `autoregressive`, `MADE`, `PixelCNN`, `WaveNet`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 22 (line 76)

자기회귀 모형(ARM)은 결합 분포를 조건부 분포의 곱 p(x)=∏p(xd|x1:d-1)으로 분해하여 정확한 우도 계산과 순차적 샘플링을 가능하게 한다. 신경 자기회귀 밀도 추정기(NADE)는 각 조건부 분포를 공유 가중치를 가진 신경망으로 매개변수화한다. 인과적 CNN으로 1차원 합성곱 마르코프 모형(dilated causal CNN, WaveNet)과 2차원 인과적 CNN(PixelCNN, PixelCNN++)을 설명하며, 마스크된 합성곱을 통한 자기회귀 구조를 유지하는 방법을 다룬다. 트랜스포머 기반 자기회귀 모형으로 GPT 계열의 텍스트 생성과 DALL-E 등의 이미지 생성을 소개한다. DALL-E는 이미지를 이산 토큰으로 변환(VQ-VAE)한 후 자기회귀적으로 생성하며, Parti는 ViT 기반 인코더-디코더 트랜스포머를 사용한다. 대규모 언어 모형(LLM)을 자기회귀 모형의 핵심 응용으로 간략히 언급한다. ARM의 장점은 정확한 우도 계산과 유연한 아키텍처이며, 단점은 순차적 샘플링의 느린 속도이다. 자기회귀 흐름은 ARM과 정규화 흐름을 결합하여 유연한 밀도 추정을 가능하게 한다. 전반적으로 ARM의 원리, 아키텍처, 응용을 간결하게 정리한다. 이 장은 다른 생성 모형(흐름, 확산 등)과의 비교 맥락을 제공한다.

### Ch 23: Normalizing flows (pp. 829-848)

**핵심**: 정규화 흐름을 다룬다. 변수 변환, 평면/방사 흐름, RealNVP, GLOW, 연속 정규화 흐름(신경 ODE), 잔차 흐름을 설명한다.

**키워드**: `normalizing flows`, `RealNVP`, `GLOW`, `neural ODE`, `continuous flows`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 23 (line 77)

정규화 흐름은 단순한 기저 분포(표준 가우시안)를 가역적 변환의 합성을 통해 복잡한 분포로 변환하며, 변수 변환 공식과 야코비안 행렬식을 이용해 정확한 우도를 계산한다. 흐름 모형의 학습은 변환된 분포의 로그 우도를 최대화하여 수행한다. 아핀 흐름, 요소별 흐름(스플라인 흐름 포함)을 기본 구성 요소로 설명한다. 커플링 흐름(RealNVP, GLOW)은 입력을 두 부분으로 나누어 한 부분이 다른 부분의 변환을 매개변수화하는 구조로, 야코비안이 삼각 행렬이 되어 효율적인 계산을 가능하게 한다. 자기회귀 흐름(IAF, MAF)은 자기회귀 구조를 이용하여 유연한 변환을 구성하며, 밀도 추정(MAF)과 빠른 샘플링(IAF)의 절충 관계를 설명한다. 잔차 흐름은 가역 잔차 네트워크를 사용하여 자유도 높은 변환을 가능하게 한다. 연속 시간 흐름은 신경 ODE를 기반으로 하며, 순시 변화율(instantaneous change of variables) 공식을 사용하여 야코비안의 추적만으로 우도를 계산한다. FFJORD는 허친슨 추적 추정기를 사용하여 연속 정규화 흐름의 확장성을 높인다. 응용으로 밀도 추정, 생성 모형, 변분 추론에서의 유연한 사후분포 구성을 다룬다. 전반적으로 정규화 흐름의 이론·구성·학습·응용을 체계적으로 제시한다.

### Ch 24: Energy-based models (pp. 849-866)

**핵심**: 에너지 기반 모형을 다룬다. 볼츠만 분포, 제한 볼츠만 머신(RBM), 대비 발산(CD), 스코어 매칭, 잡음 대비 추정(NCE)을 설명한다.

**키워드**: `EBM`, `RBM`, `contrastive divergence`, `score matching`, `NCE`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 24 (line 78)

에너지 기반 모형(EBM)은 비정규화 확률 p(x)∝exp(-E(x))로 정의되며, 분배함수의 비다루기성이 핵심 계산적 어려움이다. 전문가 곱(Product of Experts, PoE)을 EBM의 대표적 예시로 소개한다. 최대 우도 학습에서 로그 우도의 그래디언트가 데이터 기대값과 모형 기대값의 차이로 표현되며, 모형 기대값 계산에 MCMC가 필요함을 보인다. 그래디언트 기반 MCMC 방법과 대비 발산(contrastive divergence, CD)을 설명하며, CD-k와 지속 CD(PCD)의 장단점을 비교한다. 스코어 매칭(SM)은 분배함수 계산 없이 에너지 함수의 그래디언트(스코어)를 직접 학습하는 방법으로, 기본 SM, 잡음제거 스코어 매칭(DSM), 슬라이스 스코어 매칭(SSM)을 다룬다. SM과 CD의 이론적 연결을 밝히며, 스코어 기반 생성 모형(확산 모형의 전신)의 기초를 제시한다. 잡음 대비 추정(NCE)은 진짜 데이터와 잡음 데이터를 구별하는 이진 분류 문제로 에너지 함수를 학습한다. 기타 방법으로 KL 발산 차이 최소화, 스타인 불일치 최소화, 적대적 학습을 소개한다. 제한 볼츠만 머신(RBM)을 EBM의 중요한 특수 경우로 다루며 CD 학습을 설명한다. 전반적으로 EBM의 정의·학습·스코어 매칭의 이론적 기반을 제시하여 확산 모형(Ch 25)으로의 연결을 준비한다.

### Ch 25: Diffusion models (pp. 867-892)

**핵심**: 확산 모형을 다룬다. 잡음제거 확산 확률 모형(DDPM), 스코어 기반 생성 모형, 확률 미분 방정식(SDE) 관점, 조건부 생성, 가이던스 방법을 설명한다.

**키워드**: `DDPM`, `score-based`, `SDE`, `conditional generation`, `guidance`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 25 (line 58993)

잡음제거 확산 확률 모형(DDPM)은 전방 확산(인코더)에서 데이터에 점진적으로 가우시안 잡음을 추가하고, 역방 확산(디코더)에서 학습된 신경망으로 잡음을 순차적으로 제거하여 데이터를 생성한다. ELBO를 유도하여 각 시간 단계의 KL 발산 합으로 분해하며, 단순화된 잡음 예측 목적함수를 제시한다. 잡음 스케줄의 학습 방법과 이미지 생성 예제를 포함한다. 스코어 기반 생성 모형(SGM)은 다중 스케일 잡음에서의 스코어 함수를 학습하며, DDPM과의 동등성을 보인다. 연속 시간 모형으로 전방/역방 확산 확률 미분 방정식(SDE)과 확률 흐름 상미분 방정식(ODE)을 유도하며, SDE와 ODE 접근의 장단점을 비교한다. 흐름 매칭(flow matching)을 포함한 최신 학습 방법을 소개한다. 확산 모형의 가속화를 위한 DDIM 샘플러, 비가우시안 디코더, 증류(distillation), 잠재 공간 확산(latent diffusion, Stable Diffusion)을 설명한다. 조건부 생성에서 조건부 확산 모형, 분류기 가이던스, 분류기 없는 가이던스, 고해상도 이미지 생성(Imagen, Stable Diffusion)을 다룬다. 이산 상태 공간을 위한 확산 모형(D3PM)과 마르코프 전이 행렬 선택, 역방향 과정 매개변수화를 설명한다. 전반적으로 확산 모형의 이론·학습·가속·조건부 생성을 포괄적으로 제시하며, 현재 가장 강력한 생성 모형 중 하나로서의 위치를 보여 준다.

### Ch 26: Generative adversarial networks (pp. 893-924)

**핵심**: 생성적 적대 신경망(GAN)을 다룬다. GAN 학습, 와서스타인 GAN, 조건부 GAN, StyleGAN, 모드 붕괴, 안정적 학습 기법을 설명한다.

**키워드**: `GAN`, `Wasserstein GAN`, `StyleGAN`, `mode collapse`, `conditional GAN`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 26 (line 80)

GAN은 생성자(generator)와 판별자(discriminator)의 적대적 학습을 통해 암묵적 생성 모형을 학습하며, 비교를 통한 학습(learning by comparison) 원리에 기반한다. 밀도비 추정을 이진 분류기로 수행하는 방법에서 출발하여, f-발산 경계, 적분 확률 메트릭(IPM, 와서스타인 거리 포함), 적률 매칭의 이론적 기반을 제시한다. 학습 원리로부터 구체적 손실 함수(원본 GAN, 와서스타인 GAN, 힌지 손실 등)를 유도하며, 미니맥스 최적화의 경사 하강법과 교대 학습을 설명한다. GAN 학습의 어려움으로 모드 붕괴, 학습 불안정성, 그래디언트 소실을 분석하고, 스펙트럼 정규화, 그래디언트 페널티, 학습률 조정 등의 개선 기법을 다룬다. GAN 학습의 수렴 이론과 평형점 분석을 포함한다. 조건부 GAN(cGAN, pix2pix), GAN을 이용한 추론(인코더 결합), 신경 아키텍처(판별자의 중요성, 아키텍처 유도 편향, 어텐션, 점진적 생성)를 설명한다. StyleGAN의 스타일 기반 생성자와 점진적 학습을 포함한 대규모 GAN 모형(BigGAN, StyleGAN-XL)을 다룬다. 응용으로 이미지 생성, 비디오 생성, 오디오 생성, 텍스트 생성, 모방 학습, 도메인 적응, 창작을 포괄적으로 소개한다. 전반적으로 GAN의 이론·학습·아키텍처·응용을 체계적으로 정리하며, 확산 모형과의 상대적 장단점도 논의한다.

### Ch 27: Discovery methods: an overview (pp. 927-928)

**핵심**: 데이터에서 구조와 패턴을 발견하는 방법의 개요를 제공한다. 잠재 인자 모형, 상태 공간 모형, 그래프 학습 등 발견 방법의 분류를 설명한다.

**키워드**: `discovery`, `structure learning`, `latent factors`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 27 (line 82)

Part V(발견)의 개요를 제공하며, 관측 데이터 이면의 구조와 패턴을 발견하는 것을 "역 그래픽스"(vision as inverse graphics) 비유로 설명한다. 잠재변수 모형을 통해 관측 데이터 x로부터 잠재 상태 z를 추론하는 것이 발견의 핵심 과제임을 밝힌다. Chapter 28에서 고정 차원 벡터에 대한 단순 잠재변수 모형(혼합 모형, 인자 분석, ICA, 토픽 모형)을 다룸을 예고한다. Chapter 29에서 시퀀스 데이터에 대한 상태 공간 모형(HMM, LDS, 전환 SSM, 딥 SSM)으로 확장함을 설명한다. Chapter 30에서 일반 그래프에 대한 구조 학습으로 확장하며, Chapter 31에서 비모수 베이지안 모형을 통해 모형 복잡도를 데이터에 적응시키는 방법을 소개한다. Chapter 32에서 신경망 기반 표현 학습(자기지도학습 포함)을, Chapter 33에서 예측 모형의 해석가능성을 다룸을 예고한다. 발견 과제에서 유연성과 해석가능성의 균형이 중요함을 강조한다. 비선형("심층") 확장의 가능성을 각 모형에 대해 언급한다. 전체적으로 이 장은 Part V의 7개 장에 대한 로드맵을 제공한다. 시공간 확장과 확률적 프로그래밍으로의 연결 가능성도 간략히 언급한다.

### Ch 28: Latent factor models (pp. 929-978)

**핵심**: 잠재 인자 모형을 다룬다. 인자 분석, 확률적 PCA, 독립 성분 분석(ICA), 토픽 모형(LDA), 비음수 행렬 분해(NMF), 행렬/텐서 분해를 설명한다.

**키워드**: `factor analysis`, `ICA`, `LDA`, `NMF`, `matrix factorization`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 28 (line 83)

잠재변수 모형(LVM)을 z~p(z), x|z~Expfam(x|f(z))의 일반적 형태로 정의하며, 사전분포와 우도의 선택에 따라 다양한 고전적 모형이 도출됨을 표로 정리한다. 혼합 모형(GMM, 베르누이 혼합, 가우시안 스케일 혼합)을 다루며, GMM의 EM 학습, 역 영상 문제에의 응용, 비식별가능성 문제를 설명한다. 인자 분석(FA)의 기본 구조, 확률적 PCA(PPCA), 인자 분석기 혼합(MFA)을 다루며, 쌍 데이터를 위한 인자 분석, 지수족 우도, DNN 우도(VAE), GP 우도(GP-LVM)의 확장을 포함한다. 비가우시안 사전분포를 가진 LFM으로 비음수 행렬 분해(NMF)와 다항 PCA를 설명한다. 토픽 모형으로 잠재 디리클레 할당(LDA)의 구조, 변분 추론, 상관 토픽 모형, 동적 토픽 모형, LDA-HMM을 다룬다. 독립 성분 분석(ICA)에서 비가우시안 사전분포의 필요성, MLE 및 대안적 추정법, 희소 코딩, 비선형 ICA까지 포괄한다. 각 모형에 대해 EM, 변분 추론, MCMC 등의 추론 방법을 구체적으로 제시한다. 전반적으로 잠재 인자 모형의 통합적 분류 체계를 제공하며, 고전적 방법과 심층 확장의 연결을 명확히 한다. 이 장의 모형들은 발견(구조 추출)이라는 관점에서 사후 추론에 초점을 맞춘다.

### Ch 29: State-space models (pp. 979-1042)

**핵심**: 상태 공간 모형을 다룬다. 선형 가우시안 SSM, 비선형/비가우시안 SSM, 전환 SSM, 딥 상태 공간 모형(S4 등), 연속 시간 SSM(ODE)을 설명한다.

**키워드**: `SSM`, `linear Gaussian`, `switching SSM`, `deep SSM`, `S4`, `ODE`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 29 (line 84)

은닉 마르코프 모형(HMM)의 조건부 독립 성질, 상태 전이 모형(왼쪽→오른쪽, 에르고딕), 이산/가우시안/자기회귀/신경망 우도를 포함한 다양한 관측 모형을 설명한다. HMM의 응용으로 시계열 분할, 단백질 서열 정렬(프로파일 HMM), 철자 교정을 다루며, 바움-웰치(EM), SGD, 스펙트럼 방법, 베이지안 HMM에 의한 매개변수 학습을 설명한다. HMM의 일반화로 은닉 반마르코프 모형(HSMM), 계층적 HMM, 인수 HMM, 결합 HMM, 동적 베이즈 네트(DBN), 변화점 탐지를 다룬다. 선형 동적 시스템(LDS)의 매개변수화, 응용(물체 추적, 온라인 선형 회귀, 적응 필터링, 시계열 예측), EM/부분공간 식별/베이지안/온라인 매개변수 학습을 설명한다. 전환 선형 동적 시스템(SLDS)의 매개변수화, 사후 추론, 다중 표적 추적 응용을 다룬다. 비선형 SSM과 비가우시안 SSM(스파이크 트레인, 확률적 변동성 모형)의 모형 구조와 추론을 설명한다. 구조적 시계열 모형(STS)의 구성 요소(추세, 계절성, 회귀), Prophet, 인과 영향 분석, 신경 예측 방법을 다룬다. 심층 SSM으로 심층 마르코프 모형, 순환 SSM, 변분 RNN, S4 등 최신 아키텍처를 소개한다. 전반적으로 시퀀스 데이터에 대한 확률적 모형의 포괄적 분류 체계를 제공한다.

### Ch 30: Graph learning (pp. 1043-1046)

**핵심**: 그래프 구조 학습을 다룬다. DAG 구조 학습, 비방향 그래프 구조 학습, 인과 DAG 학습 방법을 설명한다.

**키워드**: `DAG learning`, `structure learning`, `causal discovery`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 30 (line 85)

그래프 구조 학습의 개요를 제공하며, 잠재변수를 가진 그래프 모형과 관측 데이터로부터 그래프 구조를 추론하는 문제를 다룬다. 그래프의 잠재변수 모형으로 노드 임베딩, 확률적 블록 모형, 그래프 생성 모형 등을 간략히 소개한다. 그래프 모형 구조 학습의 방법으로 점수 기반 방법(BIC, 베이지안 점수), 제약 기반 방법(조건부 독립 검정), 하이브리드 방법을 분류한다. DAG 구조 학습에서 조합적 탐색 공간의 초지수적 크기로 인한 계산적 어려움과, 이를 극복하기 위한 탐욕 탐색, 순서 탐색, 연속 완화(NOTEARS) 등의 방법을 설명한다. 비유향 그래프 구조 학습에서 그래피컬 라쏘(graphical lasso)를 통한 희소 정밀도 행렬 추정을 다룬다. 인과 DAG 학습을 위한 관측 데이터 기반 발견 알고리즘(PC, GES 등)의 한계와 개입 데이터의 필요성을 논의한다. 구조 학습의 응용으로 유전자 네트워크 추론, 뇌 연결성 분석 등 생물학적·신경과학적 응용을 언급한다. 구조 학습과 인과 발견의 관계를 명확히 하여 Ch 36(인과성)과의 연결을 제시한다. 전반적으로 이 장은 데이터로부터 그래프 구조를 발견하는 방법의 간결한 개요를 제공한다. 상세한 이론은 Ch 4(그래프 모형)와 Ch 36(인과성)에서 보완된다.

### Ch 31: Nonparametric Bayesian models (pp. 1047-1048)

**핵심**: 비모수 베이지안 모형을 다룬다. 디리클레 과정(DP), DP 혼합 모형, 인도 뷔페 과정, 가우시안 과정의 비모수적 관점을 설명한다.

**키워드**: `Dirichlet process`, `DP mixture`, `Indian buffet process`, `nonparametric Bayes`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 31 (line 86)

비모수 베이지안 모형은 모형의 복잡도(은닉 상태 수, 클러스터 수, 특징 수 등)를 데이터에 적응적으로 결정할 수 있게 하는 프레임워크이다. 디리클레 과정(DP)을 중국 음식점 과정(CRP)과 스틱-브레이킹(stick-breaking) 구성으로 정의하며, 집중 매개변수 α의 역할을 설명한다. DP 혼합 모형(DPMM)은 클러스터 수가 무한히 커질 수 있는 유연한 혼합 모형으로, 깁스 샘플링과 변분 추론에 의한 사후 추론을 다룬다. 계층적 디리클레 과정(HDP)을 통해 그룹 간 클러스터를 공유하는 방법을 설명한다. 인도 뷔페 과정(IBP)은 이진 특징 행렬에 대한 비모수 사전분포로, 각 객체가 가변 개수의 잠재 특징을 가질 수 있게 한다. IBP를 베타 과정의 관점에서 유도하며, 비모수 인자 분석에의 응용을 설명한다. 가우시안 과정의 비모수적 관점을 통해 함수에 대한 사전분포를 정의하는 방법을 재조명한다. 비모수 HMM(무한 HMM)과 비모수 LDS를 포함한 시계열 모형의 확장을 간략히 언급한다. 전반적으로 모형 복잡도에 대한 베이지안 불확실성을 표현하는 유연한 프레임워크를 제시한다. 데이터의 양과 질에 따라 모형이 자동으로 성장하거나 축소되는 적응성이 핵심 이점이다.

### Ch 32: Representation learning (pp. 1049-1072)

**핵심**: 표현 학습을 다룬다. 자기지도학습(대비 학습, SimCLR, BYOL), 분리된 표현 학습, 전이 학습, 다중모달 표현을 설명한다.

**키워드**: `self-supervised learning`, `contrastive learning`, `SimCLR`, `disentangled representations`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 32 (line 87)

표현 학습의 목표를 입력 데이터에서 하류 과제에 유용한 특징을 자동으로 추출하는 것으로 정의하며, 학습된 표현의 평가 방법을 체계적으로 분류한다. 하류 성능 평가로 선형 평가(고정 특징 위의 선형 분류기), 미세 조정(전체 네트워크 갱신), 분리도(disentanglement) 메트릭을 설명한다. 표현 유사성 측정으로 중심 커널 정렬(CKA), 표현 유사성 분석(RSA), 정준 상관 분석(CCA), 프로크루스테스 분석을 비교한다. 표현 학습 접근법을 지도 표현 학습·전이, 생성적 표현 학습, 자기지도 표현 학습, 다중 관점 표현 학습으로 분류한다. 자기지도학습에서 대비 학습(SimCLR, MoCo), 비대비 방법(BYOL, Barlow Twins, VICReg)의 원리와 붕괴 방지 메커니즘을 설명한다. 마스크된 자기인코딩(MAE, BEiT) 기반 자기지도학습을 소개한다. 다중 관점 표현 학습으로 정준 상관 분석의 심층 확장(Deep CCA), CLIP 등의 대비적 다중 모달 학습을 다룬다. 표현 학습의 이론으로 식별가능성 조건과 정보 최대화 원리를 설명한다. 전반적으로 표현 학습의 평가·방법·이론을 통합적으로 제시하며, 자기지도학습의 급속한 발전을 반영한다.

### Ch 33: Interpretability (pp. 1073-1102)

**핵심**: 해석가능성을 다룬다. 특징 귀속 방법(SHAP, LIME, 기울기 기반), 개념 기반 설명, 반사실적 설명, 내재적 해석가능 모형을 설명한다.

**키워드**: `SHAP`, `LIME`, `feature attribution`, `counterfactual explanations`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 33 (line 88)

해석가능성의 필요성을 미지수(unknown unknowns)와 과소 명세(under-specification) 문제로 설명하며, 과학적 발견·의료 의사결정·공정성 감사 등의 맥락을 제시한다. 해석가능 ML의 핵심 요소로 맥락(context), 최종 과제(end-task), 방법(method), 메트릭(metrics), 속성(properties)을 정의하고 상호 관계를 설명한다. 방법을 내재적 해석가능 모형(결정 트리, 규칙 목록, GAM), 반내재적 모형(예시 기반: 프로토타입, 반사실적 설명), 사후적 설명(특징 귀속, 개념 기반 설명)으로 분류한다. 특징 귀속 방법으로 LIME(지역 해석 가능한 모형 독립적 설명), SHAP(섀플리 값 기반), 기울기 기반 방법(통합 기울기, SmoothGrad), 클래스 활성화 매핑(CAM, Grad-CAM)을 설명한다. 개념 기반 설명(TCAV)과 투명성·시각화 기법을 다룬다. 설명의 속성으로 충실도(faithfulness), 안정성(stability), 이해가능성(comprehensibility), 인과성, 반사실적 유효성 등을 정의한다. 인지과학 관점의 설명 속성(대비, 선택성, 사회적 맥락)도 포함한다. 계산적 평가(속성 검증)와 사용자 연구 기반 평가(하류 과제 수행 지원)를 구분하여 설명한다. 해석가능 ML에 대한 사고 방식으로 맥락과 목적에 따른 방법 선택의 중요성을 강조한다. 전반적으로 해석가능 ML의 방법·속성·평가를 사회기술적 시스템의 관점에서 통합적으로 제시한다.

### Ch 34: Decision making under uncertainty (pp. 1105-1144)

**핵심**: 불확실성 하의 결정을 다룬다. 베이지안 결정이론, 밴디트 문제(탐색-활용), 베이지안 최적화, 실험 설계, 능동학습을 설명한다.

**키워드**: `Bayesian decision theory`, `bandit`, `Bayesian optimization`, `experimental design`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 34 (line 90)

통계적 결정이론을 빈도론적(최소최대, 허용 가능성) 및 베이지안(기대 손실 최소화) 관점에서 설명하며, 베이지안 접근의 빈도론적 최적성을 보인다. 일발 결정 문제의 예시로 분류, 회귀, 가설 검정 등을 다룬다. 결정(영향력) 다이어그램을 이용한 순차적 결정 문제 표현을 설명하며, 석유 시추 예제를 통해 최적 정책과 정보의 가치(VPI)를 유도한다. A/B 검정을 베이지안 관점에서 다루며, 사후 기대 손실과 Thompson 샘플링에 의한 적응적 실험을 설명한다. 맥락적 밴디트(contextual bandit) 문제에서 탐색-활용 절충, 최적 해(Gittins 지수), 상한 신뢰 구간(UCB), Thompson 샘플링, 후회(regret) 분석을 다룬다. 마르코프 결정 과정(MDP)의 정의, 부분 관측 MDP(POMDP), 에피소드와 반환, 가치 함수(상태 가치, 행동 가치), 최적 가치 함수와 정책(벨만 최적 방정식)을 설명한다. MDP에서의 계획으로 가치 반복, 정책 반복, 선형 계획법을 다룬다. 능동학습(active learning)의 시나리오(풀, 스트림, 멤버십 질의), 획득 전략(불확실성 샘플링, QBC, BALD, BatchBALD), 배치 능동학습을 설명한다. 베이지안 최적화를 순차적 결정 문제의 관점에서 재조명한다. 전반적으로 불확실성 하의 결정을 단발성에서 순차적 문제까지 체계적으로 다루며, 강화학습(Ch 35)의 기반을 마련한다.

### Ch 35: Reinforcement learning (pp. 1145-1184)

**핵심**: 강화학습을 다룬다. 마르코프 결정 과정(MDP), 가치 기반 방법(Q-러닝), 정책 그래디언트, 액터-크리틱, 모델 기반 RL, 역강화학습, 오프라인 RL을 설명한다.

**키워드**: `MDP`, `Q-learning`, `policy gradient`, `actor-critic`, `model-based RL`, `offline RL`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 35 (line 91)

강화학습(RL)을 에이전트가 미지의 환경과 순차적으로 상호작용하여 할인 누적 보상을 최대화하는 패러다임으로 정의하며, 모형 없는(model-free) RL과 모형 기반(model-based) RL을 대별한다. 가치 기반 RL로 몬테카를로 RL, 시간차(TD) 학습(TD(0), TD(λ), 적격 추적), SARSA(온정책), Q-러닝(이탈정책)을 설명한다. 심층 Q-네트워크(DQN)의 경험 리플레이, 표적 네트워크, 이중 DQN, 우선순위 경험 리플레이 등의 안정화 기법을 다룬다. 정책 기반 RL로 정책 그래디언트 정리, REINFORCE, 액터-크리틱 방법(A2C, A3C, GAE), 경계 최적화(TRPO, PPO), 결정론적 정책 그래디언트(DDPG, TD3, SAC)를 설명한다. 그래디언트 없는 방법(CMA-ES, ARS)도 간략히 소개한다. 모형 기반 RL로 모형 예측 제어(MPC), 모형 기반과 모형 없는 결합(Dyna, MBPO), GP 기반 MBRL(PILCO), DNN 기반 MBRL, 잠재변수 모형 기반 MBRL(World Models, Dreamer)을 다룬다. 이탈정책 학습의 기초 기법(중요도 샘플링), 수평선의 저주, 치명적 삼중주(deadly triad), 대표적 이탈정책 방법을 설명한다. 제어를 추론으로 보는 관점에서 최대 엔트로피 RL(Soft Actor-Critic)과 모방 학습(행동 복제, 역강화학습, GAIL)을 다룬다. 전반적으로 RL의 핵심 알고리즘과 이론을 가치·정책·모형 기반 관점에서 통합적으로 제시한다.

### Ch 36: Causality (pp. 1185-1211)

**핵심**: 인과성을 다룬다. 구조적 인과 모형(SCM), do-연산, 반사실, 도구변수, 이중차분법, 인과 발견 알고리즘을 설명한다.

**키워드**: `SCM`, `do-calculus`, `counterfactuals`, `instrumental variables`, `causal discovery`

**상세**: → `Probabilistic Machine Learning Advanced_azure_full.md` Ch 36 (line 78249)

인과추론의 핵심 과제를 개입(intervention) 하에서의 세계 변화를 데이터로부터 추정하는 것으로 정의하며, 인과 추정량(causal estimand), 식별(identification), 추정(estimation)의 세 단계 접근법을 제시한다. 구조적 인과 모형(SCM)을 확률 모형과 구별하여, 변수 간 기계적 관계와 개입의 의미를 형식화한다. 인과 DAG를 통해 교란 변수, 매개 변수, 충돌 변수(collider)의 역할을 설명하며, 뒷문 기준(backdoor criterion)에 의한 식별 조건을 유도한다. 반사실(counterfactual)과 인과 위계(관측-개입-반사실)를 설명한다. 무작위 대조 시험(RCT)을 인과 효과 추정의 금본위(gold standard)로 제시하며, 관측 데이터에서의 교란 변수 보정 방법을 다룬다. 평균 처리 효과(ATE) 추정을 위한 결과 회귀, 역확률 가중치(IPW), 이중 강건(doubly robust) 추정, AIPW 추정기를 설명한다. 매칭 방법과 실용적 절차(양 겹침 확인, 균형 검정)를 포함한다. 도구변수(IV) 전략으로 비관측 교란에 대처하며, 도구 단조성과 국소 평균 처리 효과(LATE), 2단계 최소제곱(2SLS)을 다룬다. 이중차분법(difference-in-differences)에 의한 인과 효과 추정과 평행 추세 가정을 설명한다. 신뢰성 검사로 위약 검사와 비관측 교란에 대한 민감도 분석(Rosenbaum 경계, E-값)을 다룬다. do-연산법의 세 규칙과 뒷문/앞문 보정의 유도를 포함한다. 전반적으로 인과추론의 형식적 프레임워크, 식별 전략, 현대적 추정 방법을 포괄적으로 제시한다.
