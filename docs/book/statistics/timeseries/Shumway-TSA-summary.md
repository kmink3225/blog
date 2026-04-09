---
name: "Time Series Analysis and Its Applications: With R Examples (4th ed)"
type: book-summary
authors: "Robert H. Shumway, David S. Stoffer"
year: 2017
publisher: "Springer (Springer Texts in Statistics)"
total_pages: 562
language: en
keywords: [time-series, ARIMA, spectral-analysis, state-space, R, statistics, ACF, PACF, regression, multivariate, GARCH, Bayesian]
sources:
  - file: "Shumway-TSA_full.md"
    tool: "marker (PDF → MD)"
  - file: "Shumway-TSA-images.md"
    tool: "marker (151 figures)"
---

# Time Series Analysis and Its Applications (4th ed.) — Summary

> Robert H. Shumway, David S. Stoffer (2017), Springer, ~562 pages, 7 chapters + appendices
> 시계열 분석의 이론적 깊이와 R 실습을 결합한 표준 대학원 교재. 고전 통계 이론(ARIMA, 스펙트럼 분석)부터 상태 공간 모델, 주파수 영역 통계까지 수학적 엄밀성을 유지하면서 astsa R 패키지로 실습한다.

## Contents

- Ch 1: Characteristics of Time Series (L:173)
- Ch 2: Time Series Regression and Exploratory Data Analysis (L:1393)
- Ch 3: ARIMA Models (L:2233)
- Ch 4: Spectral Analysis and Filtering (L:5278)
- Ch 5: Additional Time Domain Topics (L:7644)
- Ch 6: State Space Models (L:9213)
- Ch 7: Statistical Methods in the Frequency Domain (L:12740)
- Appendix A: Large Sample Theory (L:15800)
- Appendix B: Time Domain Theory (L:16300)
- Appendix C: Spectral Domain Theory (L:16600)
- Appendix R: R Supplement (L:17502)

---

## Chapter Summaries

### Ch 1: Characteristics of Time Series (L:173)

**핵심**: 시계열 데이터의 특성과 통계적 모델 개요(이동평균, 자기회귀, 랜덤 워크), 의존성 측도(평균함수, 자기공분산, ACF, CCF), 정상성, 표본 ACF, 다차원 시계열을 다룬다.

**키워드**: `autocorrelation`, `stationarity`, `ACF`, `CCF`, `white noise`, `moving average`, `random walk`, `vector-valued series`

**상세**: → `Shumway-TSA_full.md` Ch 1 (L:173)
Johnson & Johnson 주당순이익, 지구 온난화, 음성 데이터, DJIA, 엘니뇨-어류 개체수 등 다양한 실제 예시로 시계열의 특성을 보인다. 평균 함수, 자기공분산·자기상관 함수(ACF), 교차상관 함수(CCF)를 정의하고 그 성질을 이론적으로 확립한다. 정상성의 엄밀한 정의(강/약 정상성), 선형 공정의 표본 ACF 분포, 예비백화(prewhitening)를 통한 교차상관 분석을 다룬다.

### Ch 2: Time Series Regression and Exploratory Data Analysis (L:1393)

**핵심**: 시계열 맥락에서의 고전 회귀, 탐색적 데이터 분석(추세 추정, 백차 연산자, 차분), 시계열 맥락의 평활화(이동평균, 커널, 국소 다항 평활, 스플라인)를 다룬다.

**키워드**: `regression`, `backshift operator`, `differencing`, `EDA`, `smoothing`, `moving average smoother`, `kernel smoother`, `spline`

**상세**: → `Shumway-TSA_full.md` Ch 2 (L:1393)
시계열 데이터에서 고전 선형 회귀의 적용과 자기상관 오차의 문제를 다룬다. 백차 연산자(B)와 차분 연산자를 정의하고 이를 활용한 추세 제거 방법을 설명한다. 이동평균 평활, 커널 평활, 국소 다항 회귀, 스플라인 평활 등 비모수 평활 기법을 비교하며 R astsa 패키지로 실습한다.

### Ch 3: ARIMA Models (L:2233)

**핵심**: ARMA 모델(자기회귀, 이동평균), 차분 방정식, ACF/PACF, 예측(Durbin-Levinson, 혁신 알고리즘), 추정(조건부/비조건부 최소자승, MLE), ARIMA, 계절 SARIMA 모델을 다룬다.

**키워드**: `ARMA`, `ARIMA`, `SARIMA`, `Durbin-Levinson`, `innovation algorithm`, `MLE`, `seasonal models`, `causality`, `invertibility`

**상세**: → `Shumway-TSA_full.md` Ch 3 (L:2233)
ARMA(p,q) 모델의 인과성·가역성 조건을 이론적으로 확립하고, 편자기상관함수(PACF) 계산을 위한 Durbin-Levinson 알고리즘, 최우수 선형 예측을 위한 혁신(innovation) 알고리즘을 유도한다. 최대우도 추정(MLE)과 조건부/비조건부 최소자승 추정의 대표본 성질을 다룬다. ARIMA의 적분 모델, 계절 SARIMA, 자기상관 오차를 포함한 회귀 모델도 포함한다.

### Ch 4: Spectral Analysis and Filtering (L:5278)

**핵심**: 주기성과 스펙트럼 밀도, 주기도와 이산 푸리에 변환(DFT), 비모수/모수 스펙트럼 추정, 다중 시계열과 교차 스펙트럼, 선형 필터, 지연 회귀, 신호 추출, 다차원 스펙트럼 분석을 다룬다.

**키워드**: `spectral density`, `periodogram`, `DFT`, `nonparametric spectral estimation`, `coherence`, `linear filter`, `signal extraction`, `multitaper`

**상세**: → `Shumway-TSA_full.md` Ch 4 (L:5278)
주파수 영역 분석의 이론적 기초를 확립한다. 스펙트럼 밀도 함수의 정의와 추정(주기도, 커널 평활, 다중테이퍼), 이산 푸리에 변환의 통계적 성질을 다룬다. 다중 시계열의 교차 스펙트럼과 코히런스, 위상을 활용한 주파수별 관계 분석, 선형 필터(저역/고역/대역 통과)의 스펙트럼 해석을 포함한다.

### Ch 5: Additional Time Domain Topics (L:7644)

**핵심**: 장기 기억 ARMA와 분수 차분, 단위근 검정, GARCH 모델(변동성 클러스터링), 임계 모델(TAR), 지연 회귀와 전달 함수, 다변량 ARMAX를 다룬다.

**키워드**: `long memory`, `fractional differencing`, `unit root`, `GARCH`, `TAR`, `threshold model`, `transfer function`, `VARMAX`

**상세**: → `Shumway-TSA_full.md` Ch 5 (L:7644)
고전 ARIMA를 넘어서는 고급 시간 영역 주제를 다룬다. 분수 차분 ARFIMA(d)로 장기 기억 특성을 모델링하고, ADF·PP·KPSS 단위근 검정 이론을 설명한다. ARCH(1)과 GARCH(p,q)로 변동성 클러스터링을 포착하고, 임계 자기회귀 모델(TAR)의 비선형성을 다룬다. 다변량 ARMAX와 전달 함수 모델도 포함한다.

### Ch 6: State Space Models (L:9213)

**핵심**: 선형 가우스 상태 공간 모델, 칼만 필터/스무더/예측, 최대우도 추정, 결측값 처리, 구조적 모델, 부트스트랩, 은닉 마르코프 모델, 전환 자기회귀, 확률적 변동성, 베이지안 분석을 다룬다.

**키워드**: `Kalman filter`, `Kalman smoother`, `state space`, `EM algorithm`, `hidden Markov model`, `switching autoregression`, `stochastic volatility`, `Bayesian`

**상세**: → `Shumway-TSA_full.md` Ch 6 (L:9213)
상태 공간 모델의 통합 프레임워크를 다루는 가장 광범위한 챕터이다. 칼만 재귀 방정식(필터·스무더·예측)과 EM 알고리즘 기반 최대우도 추정을 유도한다. 결측값, 이상값, 구조적 모델(추세+계절+잔차)에 상태 공간을 적용하고, 은닉 마르코프 모델(HMM), 체제 전환 자기회귀, 스플라인 평활과 칼만 스무더의 동치성을 증명한다. 확률적 변동성 모델의 베이지안 추론도 다룬다.

### Ch 7: Statistical Methods in the Frequency Domain (L:12740)

**핵심**: 주파수 영역의 통계 방법론 — 스펙트럼 행렬과 우도 함수, 결합 정상 시계열 회귀, 결정론적 입력 회귀, 랜덤 계수 회귀, 실험 설계 분석, 판별·군집 분석, 주성분 분석, 스펙트럼 포락선을 다룬다.

**키워드**: `spectral matrix`, `frequency domain regression`, `discriminant analysis`, `cluster analysis`, `PCA in frequency domain`, `spectral envelope`

**상세**: → `Shumway-TSA_full.md` Ch 7 (L:12740)
주파수 영역 통계의 고급 주제를 다루는 이론 중심 챕터이다. 스펙트럼 행렬과 다변량 가우스 과정의 우도 함수를 정의하고, 결합 정상 시계열에서의 회귀 추론을 주파수 영역으로 전환한다. 시계열 분류를 위한 주파수 영역 판별 분석, 시계열 군집화, 스펙트럼 주성분 분석, DNA 서열 카테고리화를 위한 스펙트럼 포락선을 포함한다.
