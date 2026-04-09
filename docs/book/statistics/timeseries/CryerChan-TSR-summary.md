---
name: "Time Series Analysis: With Applications in R (2nd ed)"
type: book-summary
authors: "Jonathan D. Cryer, Kung-Sik Chan"
year: 2008
publisher: Springer
total_pages: 491
language: en
keywords: [time-series, R, ARIMA, ACF, PACF, regression, forecasting, statistics, seasonal, intervention, GARCH, spectral]
sources:
  - file: "CryerChan-TSR_full.md"
    tool: "marker (PDF → MD)"
  - file: "CryerChan-TSR-images.md"
    tool: "marker (272 figures)"
---

# Time Series Analysis: With Applications in R (2nd ed.) — Summary

> Jonathan D. Cryer, Kung-Sik Chan (2008), Springer, ~491 pages, 15 chapters
> R을 활용한 시계열 분석의 표준 입문 교재. 수학적 이론과 R 코드(TSA 패키지)를 병행하여 ARIMA 모델링의 전체 워크플로(탐색 → 명세 → 추정 → 진단 → 예측)를 단계적으로 설명한다.

## Contents

- Ch 1: Introduction (L:226)
- Ch 2: Fundamental Concepts (L:407)
- Ch 3: Trends (L:927)
- Ch 4: Models for Stationary Time Series (L:1599)
- Ch 5: Models for Nonstationary Time Series (L:2441)
- Ch 6: Model Specification (L:3050)
- Ch 7: Parameter Estimation (L:3856)
- Ch 8: Model Diagnostics (L:4662)
- Ch 9: Forecasting (L:5057)
- Ch 10: Seasonal Models (L:6365)
- Ch 11: Time Series Regression Models (L:7018)
- Ch 12: Time Series Models of Heteroscedasticity (L:7637)
- Ch 13: Introduction to Spectral Analysis (L:8492)
- Ch 14: Estimating the Spectrum (L:9297)
- Ch 15: Threshold Models (L:9979)
- Appendix: Introduction to R (L:10888)

---

## Chapter Summaries

### Ch 1: Introduction (L:226)

**핵심**: 다양한 시계열 예시(LA 강수량, 산업 화학 공정, 하레 개체수, 월평균 온도, 오일 필터 판매), 모델 구축 전략, 시계열 도표의 역사, 책의 개요를 다룬다.

**키워드**: `time series examples`, `model building`, `data exploration`, `descriptive analysis`

**상세**: → `CryerChan-TSR_full.md` Ch 1 (L:226)
연속형과 이산형 시계열의 다양한 실제 예시를 통해 시계열 분석의 필요성을 동기화한다. 시계열 모델 구축의 반복적 전략(명세 → 적합 → 진단 → 수정)을 소개하고, 역사적 관점에서 시계열 도표 방법론의 발전을 개관한다. 이 책 전체의 분석 흐름과 각 챕터 간 연결을 설명한다.

### Ch 2: Fundamental Concepts (L:407)

**핵심**: 시계열과 확률 과정의 정의, 평균·분산·공분산 함수, 정상성, 백색 잡음, 이동평균 과정, 랜덤 코사인파를 다룬다.

**키워드**: `stochastic process`, `autocovariance`, `stationarity`, `white noise`, `moving average`, `random cosine wave`

**상세**: → `CryerChan-TSR_full.md` Ch 2 (L:407)
확률 과정으로서의 시계열을 엄밀히 정의한다. 평균 함수, 분산 함수, 자기공분산·자기상관 함수의 특성(대칭성, 양반정값)을 유도한다. 랜덤 워크와 이동평균의 자기공분산을 계산하는 예시를 상세히 다루고, 약 정상성(weak stationarity)의 실용적 의미를 설명한다. 기댓값, 분산, 공분산, 상관의 성질을 정리한 부록을 포함한다.

### Ch 3: Trends (L:927)

**핵심**: 결정론적 vs. 확률적 추세, 상수 평균 추정, 선형/이차 추세와 계절 추세를 포함한 회귀 방법, 회귀 추정의 신뢰성과 효율성, 회귀 출력 해석, 잔차 분석과 표본 ACF를 다룬다.

**키워드**: `deterministic trend`, `stochastic trend`, `regression`, `seasonal trend`, `cosine trend`, `residual analysis`, `GLS`

**상세**: → `CryerChan-TSR_full.md` Ch 3 (L:927)
시계열의 추세를 제거하는 두 가지 접근(결정론적 회귀 vs. 차분)의 차이와 각각의 적합한 상황을 논의한다. 선형, 이차, 주기(코사인 포함), 계절 회귀 모델을 R로 적합하는 방법을 설명한다. 자기상관 오차 존재 시 OLS 추정의 문제점과 GLS의 필요성, 잔차 ACF로 모델 적합성을 진단하는 방법을 다룬다.

### Ch 4: Models for Stationary Time Series (L:1599)

**핵심**: 일반 선형 과정, MA 과정(1차, 2차), AR 과정(1차, 2차, 고차), 혼합 ARMA 모델, 가역성을 다룬다.

**키워드**: `MA`, `AR`, `ARMA`, `invertibility`, `causality`, `Yule-Walker`, `partial autocorrelation`

**상세**: → `CryerChan-TSR_full.md` Ch 4 (L:1599)
정상 시계열 모델의 이론적 기초를 확립한다. 일반 선형 과정의 자기공분산을 MA 표현으로 계산하고, MA(1), MA(2), AR(1), AR(2), AR(p)의 ACF/PACF 패턴을 유도한다. Yule-Walker 방정식으로 AR 계수와 자기상관 간 관계를 수립하고, ARMA(p,q)의 인과성과 가역성 조건을 설명한다. AR(2) 정상성 영역과 ARMA ACF 공식을 부록으로 제공한다.

### Ch 5: Models for Nonstationary Time Series (L:2441)

**핵심**: 차분을 통한 정상화, ARIMA(p,d,q) 모델, ARIMA에서의 상수항, 기타 변환(로그, Box-Cox), 백차 연산자를 다룬다.

**키워드**: `ARIMA`, `differencing`, `nonstationarity`, `Box-Cox`, `logarithm`, `backshift operator`

**상세**: → `CryerChan-TSR_full.md` Ch 5 (L:2441)
비정상 시계열을 차분으로 정상화하는 방법을 체계적으로 설명한다. ARIMA(p,d,q) 모델에서 적분 차수 d의 의미와 결정 방법을 다룬다. ARIMA 모델의 상수항(drift vs. 평균) 해석의 차이를 명확히 하고, 로그 변환과 Box-Cox 변환으로 분산 안정화를 처리하는 방법을 설명한다. 백차 연산자 부록을 포함한다.

### Ch 6: Model Specification (L:3050)

**핵심**: 표본 ACF의 통계적 성질, 편자기상관함수(PACF)와 확장 ACF(EACF), 시뮬레이션 시계열 명세, 비정상성 처리, 기타 명세 방법(AIC, BIC), 실제 시계열 명세를 다룬다.

**키워드**: `PACF`, `EACF`, `model specification`, `ACF patterns`, `AIC`, `BIC`, `unit root`, `ARIMA identification`

**상세**: → `CryerChan-TSR_full.md` Ch 6 (L:3050)
ARIMA 모델 명세(p, d, q 결정)의 전체 과정을 다룬다. 표본 ACF의 대표본 분포를 이용한 신뢰 구간, PACF와 EACF의 이론과 계산을 설명한다. 다양한 시뮬레이션 시계열과 실제 데이터(월별 의약품 판매 등)에 ACF/PACF 패턴을 적용하여 모델 명세 실습을 수행한다.

### Ch 7: Parameter Estimation (L:3856)

**핵심**: 모멘트 방법, 최소자승 추정(조건부/비조건부), 최대우도 추정(MLE), 추정량의 통계적 성질, 추정 예시, ARIMA 모델의 부트스트랩을 다룬다.

**키워드**: `method of moments`, `least squares`, `MLE`, `asymptotic distribution`, `bootstrap`, `parameter estimation`

**상세**: → `CryerChan-TSR_full.md` Ch 7 (L:3856)
ARMA/ARIMA 모델 계수 추정의 세 가지 방법을 비교한다. 모멘트 방법(Yule-Walker 확장)은 계산이 간단하지만 효율적이지 않다. 조건부 최소자승(관측값 조건부)과 비조건부 최소자승, MLE의 수치적 최적화 방법을 설명한다. 대표본에서 추정량의 점근 분포와 신뢰 구간 구성, 부트스트랩을 활용한 비모수 추론도 다룬다.

### Ch 8: Model Diagnostics (L:4662)

**핵심**: 잔차 분석(ACF, Ljung-Box 검정, 정규성 검정, Q-Q plot), 과적합과 파라미터 중복성 감지를 다룬다.

**키워드**: `residual analysis`, `Ljung-Box test`, `normality test`, `overfitting`, `parameter redundancy`, `diagnostic plots`

**상세**: → `CryerChan-TSR_full.md` Ch 8 (L:4662)
모델 진단은 ARIMA 모델링 과정의 핵심 단계이다. 표준화 잔차의 ACF로 자기상관 잔존 여부를 검정하고, Ljung-Box 포트만토 검정으로 잔차 백색잡음 여부를 공식 검정한다. 잔차의 정규성 검정(Shapiro-Wilk, Q-Q plot)과 과적합(특성근이 소거되는 경우)을 R TSA 패키지로 탐지하는 방법을 설명한다.

### Ch 9: Forecasting (L:5057)

**핵심**: 최소평균제곱오차(MMSE) 예측, 결정론적 추세 예측, ARIMA 예측, 예측 한계, 예측 갱신, 예측 가중치와 지수 가중 이동평균(EWMA), 변환된 시계열 예측을 다룬다.

**키워드**: `MMSE forecasting`, `prediction intervals`, `ARIMA forecasting`, `EWMA`, `updating forecasts`, `Durbin-Levinson`, `forecast weights`

**상세**: → `CryerChan-TSR_full.md` Ch 9 (L:5057)
ARIMA 모델을 사용한 예측의 이론적 기초를 확립한다. MMSE 선형 예측의 재귀 공식(Durbin-Levinson)과 최우수 예측으로서의 조건부 기댓값을 유도한다. ARIMA 예측의 점근 예측 한계 구성, 새 관측값이 들어올 때 예측을 효율적으로 갱신하는 방법, 예측 가중치가 EWMA와 연결되는 특수 사례를 설명한다.

### Ch 10: Seasonal Models (L:6365)

**핵심**: 계절 ARIMA 모델, 승산 계절 ARMA, 비정상 계절 ARIMA, 모델 명세/적합/점검, 계절 모델 예측을 다룬다.

**키워드**: `seasonal ARIMA`, `SARIMA`, `multiplicative seasonal`, `seasonal differencing`, `airline model`

**상세**: → `CryerChan-TSR_full.md` Ch 10 (L:6365)
계절 주기 s를 갖는 시계열을 위한 계절 ARIMA 모델을 체계적으로 설명한다. Box-Jenkins의 승산 계절 ARMA 구조 SARIMA(p,d,q)(P,D,Q)s의 이론과 ACF/PACF 패턴을 다룬다. 유명한 항공 승객 데이터(airline model)에 대한 명세, 추정, 진단, 예측 전체 과정을 R로 실습한다.

### Ch 11: Time Series Regression Models (L:7018)

**핵심**: 개입 분석(interruption, outlier), 이상값 처리, 허구적 상관, 예비백화와 확률 회귀를 다룬다.

**키워드**: `intervention analysis`, `outliers`, `spurious correlation`, `prewhitening`, `stochastic regression`, `transfer function`

**상세**: → `CryerChan-TSR_full.md` Ch 11 (L:7018)
시계열에서 외부 사건(개입)의 효과를 모델링하는 개입 분석을 설명한다. 이상값(가산 이상값, 일시적 변화, 수준 이동)을 감지하고 처리하는 방법을 다룬다. 시계열 간 허구적 상관의 위험성과 예비백화(prewhitening)를 통한 교차상관 분석, 확률론적 회귀 모델을 설명한다.

### Ch 12: Time Series Models of Heteroscedasticity (L:7637)

**핵심**: 금융 시계열의 공통 특성(변동성 클러스터링, 두꺼운 꼬리), ARCH(1) 모델, GARCH 모델, MLE, 모델 진단, 비음수 조건, GARCH 확장 모델을 다룬다.

**키워드**: `ARCH`, `GARCH`, `volatility clustering`, `heavy tails`, `MLE`, `financial time series`, `conditional variance`

**상세**: → `CryerChan-TSR_full.md` Ch 12 (L:7637)
금융 시계열의 비선형 특성인 변동성 클러스터링을 포착하는 ARCH/GARCH 모델을 다룬다. ARCH(1)의 정의와 정상성 조건을 수립하고, GARCH(p,q)로 확장하는 이론을 설명한다. 미국 주가 지수와 USD/HKD 환율 데이터에 GARCH를 적용하는 실제 예시를 포함한다. 일반화 포트만토 검정 공식을 부록으로 제공한다.

### Ch 13: Introduction to Spectral Analysis (L:8492)

**핵심**: 스펙트럼 분석 소개, 주기도, 스펙트럼 표현과 분포, 스펙트럼 밀도, ARMA 과정의 스펙트럼 밀도, 표본 스펙트럼 밀도의 표본 성질을 다룬다.

**키워드**: `spectral analysis`, `periodogram`, `spectral density`, `Fourier`, `frequency domain`, `ARMA spectrum`

**상세**: → `CryerChan-TSR_full.md` Ch 13 (L:8492)
주파수 영역 분석의 기초를 소개한다. 주기도의 정의와 계산, 스펙트럼 분포 함수와 밀도 함수의 관계를 확립한다. ARMA 모델의 스펙트럼 밀도 공식을 유도하고, 이를 통해 AR/MA/ARMA 모델의 주파수별 에너지 분포를 해석하는 방법을 설명한다. 코사인/사인 수열의 직교성 부록을 포함한다.

### Ch 14: Estimating the Spectrum (L:9297)

**핵심**: 스펙트럼 밀도 평활, 편향과 분산, 대역폭, 스펙트럼 신뢰 구간, 누설과 테이퍼링, 자기회귀 스펙트럼 추정, 시뮬레이션/실제 데이터 예시를 다룬다.

**키워드**: `spectral smoothing`, `bandwidth`, `confidence intervals`, `leakage`, `tapering`, `AR spectrum`, `Dirichlet kernel`

**상세**: → `CryerChan-TSR_full.md` Ch 14 (L:9297)
비모수 스펙트럼 추정의 통계적 이론을 다룬다. 주기도의 편향-분산 트레이드오프와 대역폭 선택의 중요성을 설명한다. 스펙트럼 신뢰 구간 구성, 주파수 누설 문제와 테이퍼링을 통한 완화, 자기회귀 모수적 스펙트럼 추정을 비교한다. 테이퍼링과 Dirichlet 커널의 관계를 부록으로 유도한다.

### Ch 15: Threshold Models (L:9979)

**핵심**: 비선형성 그래픽 탐색, 비선형성 검정, 임계 자기회귀(TAR) 모델, 임계 모델 추정과 진단, 예측을 다룬다.

**키워드**: `threshold model`, `TAR`, `nonlinearity`, `regime switching`, `SETAR`, `limit cycles`, `nonlinear forecasting`

**상세**: → `CryerChan-TSR_full.md` Ch 15 (L:9979)
선형 ARIMA로 포착할 수 없는 비선형 시계열을 위한 임계 자기회귀(TAR) 모델을 다룬다. RESET 검정, Keenan 검정, Tsay 검정 등 비선형성 검정 방법을 설명한다. TAR 모델의 추정, 검정(임계 비선형성), 진단, 예측 방법을 Canadian lynx(스라소니 개체수) 데이터와 다른 예시로 실습한다. 일반화 포트만토 검정 공식을 부록으로 포함한다.
