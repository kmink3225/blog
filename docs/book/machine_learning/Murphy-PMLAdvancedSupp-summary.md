---
name: "Probabilistic Machine Learning: Advanced Topics — Supplementary Material"
type: book-summary
source_file: "Murphy-PMLAdvancedSupp_full.md"
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

**상세**: → `Probabilistic Machine Learning Advanced Supplementary_full.md` Ch 2 (line 258)

### Ch 3 보충: Bayesian Statistics (line 20)

**핵심**: 베이지안 개념 학습(숫자 게임, 건강 수치 게임)의 상세 예제, 도메인 특화 사전분포(가우시안, 멱급수, Erlang), Tweedie 공식(경험적 베이즈에서 사전분포 추정 없이 사용)을 다룬다.

**키워드**: `concept learning`, `informative priors`, `Tweedie formula`, `empirical Bayes`

**상세**: → `Probabilistic Machine Learning Advanced Supplementary_full.md` Ch 3 (line 20)

### Ch 7 보충: Optimization (line 50)

**핵심**: 프록시멀 연산자와 프록시멀 방법(미러 디센트, 프록시멀 그래디언트, ADMM), 동적 프로그래밍, 켤레 쌍대성(시그모이드 함수 바운드), 베이지안 학습 규칙(BLR)에서 추론/최적화 알고리즘 유도를 다룬다.

**키워드**: `proximal operator`, `ADMM`, `conjugate duality`, `Bayesian learning rule`

**상세**: → `Probabilistic Machine Learning Advanced Supplementary_full.md` Ch 7 (line 50)

### Ch 30 보충: Graph Learning (line 182)

**핵심**: 확률적 블록 모형(SBM, MMSB, 무한 관계 모형), 트리 구조 학습(Chow-Liu, MAP forest), DAG 구조 학습(베이지안 모형 선택, 제약 기반, 희소 최적화), 비방향 그래프 학습(의존 네트워크, 그래프 라소), 인과 DAG 학습(원인-결과 쌍, 개입 데이터)을 상세히 다룬다.

**키워드**: `SBM`, `Chow-Liu`, `DAG structure learning`, `graphical lasso`, `causal DAG`

**상세**: → `Probabilistic Machine Learning Advanced Supplementary_full.md` Ch 30 (line 182)

### Ch 31 보충: Nonparametric Bayesian Models (line 212)

**핵심**: 디리클레 과정(정의, 스틱 브레이킹, 중국 식당 과정), DP 혼합 모형(깁스 샘플링, 변분 베이즈), 피트먼-요르 과정, 인도 뷔페 과정, 소분산 점근, 완전 랜덤 측도, 레비 과정, 반발과 강화를 가진 점 과정(포아송, 재생, 호크스, 깁스, DPP)을 상세히 다룬다.

**키워드**: `Dirichlet process`, `stick breaking`, `CRP`, `Pitman-Yor`, `IBP`, `DPP`

**상세**: → `Probabilistic Machine Learning Advanced Supplementary_full.md` Ch 31 (line 212)
