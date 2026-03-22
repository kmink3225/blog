---
name: "Forecasting: Principles and Practice, 3rd Edition"
type: book-summary
authors: "Rob J Hyndman, George Athanasopoulos"
year: 2021
total_pages: 380
language: en
keywords: [time-series, forecasting, ARIMA, exponential-smoothing, ETS, decomposition, regression, seasonality, autocorrelation, cross-validation, hierarchical-forecasting, dynamic-regression, prophet, neural-network, fable, tsibble, R]
sources:
  - file: "Hyndman-FPP3_full.md"
    tool: "wget + html2text (otexts.com/fpp3/)"
  - file: "Hyndman-FPP3-images.md"
    tool: "wget (217 figures)"
---

# Forecasting: Principles and Practice (3rd ed.) — Summary

> Rob J Hyndman & George Athanasopoulos (2021), 380 pages, 13 chapters
> 시계열 예측의 실무 교과서. R fable/tsibble 생태계 기반으로 ETS, ARIMA, 동적 회귀, 계층 예측까지 체계적으로 다룬다.

## 실무 Python 라이브러리 (코드 레퍼런스)

FPP3는 R/fable 기반이다. Python으로 동일한 작업을 할 때는 아래 라이브러리를 참조한다.

| 라이브러리 | GitHub | 역할 | FPP3 대응 챕터 |
|-----------|--------|------|---------------|
| **statsforecast** | https://github.com/Nixtla/statsforecast | 전통 모델 (ETS, ARIMA, Theta) 대규모 서빙 | Ch 5, 8, 9 |
| **neuralforecast** | https://github.com/Nixtla/neuralforecast | DL 모델 (NBEATS, PatchTST, TFT) | Ch 12 확장 |
| **mlforecast** | https://github.com/Nixtla/mlforecast | ML 모델 (LightGBM, XGBoost) 시계열 적용 | Ch 7 확장 |
| **hierarchicalforecast** | https://github.com/Nixtla/hierarchicalforecast | 계층 예측 조정 (MinT, ERM) | Ch 11 |
| **GluonTS** | https://github.com/awslabs/gluonts | 확률적 예측 (DeepAR, Chronos) | Ch 12 확장 |
| **Darts** | https://github.com/unit8co/darts | 통합 API (전통+DL), 빠른 프로토타이핑 | 전체 |

> **활용 방식**: 블로그 포스트에서 FPP3 이론을 설명한 후 Python 코드 예시를 붙일 때 위 라이브러리의 docs/examples를 참조한다. 레포를 로컬에 클론하지 않고 온라인 docs + GitHub 코드를 직접 참조한다.

---

## Contents

### Part I: Foundations (Ch 1-4)
- Ch 1: Getting Started (L:99)
- Ch 2: Time Series Graphics (L:375)
- Ch 3: Time Series Decomposition (L:1181)
- Ch 4: Time Series Features (L:1778)

### Part II: Forecasting Toolbox (Ch 5-6)
- Ch 5: The Forecaster's Toolbox (L:2133)
- Ch 6: Judgmental Forecasts (L:3370)

### Part III: Core Methods (Ch 7-9)
- Ch 7: Time Series Regression Models (L:3756)
- Ch 8: Exponential Smoothing (L:4775)
- Ch 9: ARIMA Models (L:5544)

### Part IV: Advanced Topics (Ch 10-13)
- Ch 10: Dynamic Regression Models (L:6809)
- Ch 11: Forecasting Hierarchical and Grouped Time Series (L:7373)
- Ch 12: Advanced Forecasting Methods (L:8063)
- Ch 13: Some Practical Forecasting Issues (L:8673)

---

## Chapter Summaries

### Ch 1: Getting Started (L:99)

**핵심**: 예측의 정의, 계획과의 관계, 예측 가능성의 조건, 통계적 예측의 관점을 소개한다. 예측 과업의 기본 단계(문제 정의 → 데이터 수집 → 탐색 → 모델링 → 평가)를 개괄한다.

**키워드**: `forecasting`, `planning`, `predictability`, `statistical perspective`, `forecasting steps`

**상세**: → `Hyndman-FPP3_full.md` Ch 1 (L:99)
예측은 미래에 대한 불확실성을 정량화하는 작업이다. 예측 가능성은 (1) 시스템에 대한 이해도, (2) 사용 가능한 데이터의 양, (3) 예측이 예측 대상 자체에 미치는 영향 정도에 의존한다. 통계적 예측에서는 관측된 시계열이 확률과정의 실현값이라고 본다. 정량적 예측은 과거 수치 데이터가 있고 과거 패턴이 미래에도 지속된다는 가정 하에 적용한다. 예측의 기본 단계는 문제 정의, 정보 수집, 탐색적 분석, 모델 선택과 적합, 예측 생성과 평가 순서로 진행된다.

### Ch 2: Time Series Graphics (L:375)

**핵심**: tsibble 객체 구조, 시계열 시각화(time plot, seasonal plot, subseries, scatterplot, lag plot, ACF), 백색잡음 검정을 다룬다.

**키워드**: `tsibble`, `time plot`, `seasonal plot`, `ACF`, `autocorrelation`, `white noise`, `lag plot`, `Ljung-Box test`

**상세**: → `Hyndman-FPP3_full.md` Ch 2 (L:375)
R의 tsibble 패키지로 시계열 데이터를 정돈된(tidy) 형태로 관리한다. 시계열의 3가지 기본 패턴은 추세(trend), 계절성(seasonality), 순환(cycle)이다. 계절성 그래프(gg_season)는 주기 내 패턴을, 서브시리즈 그래프(gg_subseries)는 주기 간 변화를 드러낸다. 자기상관함수(ACF)는 시계열의 시차 간 상관을 요약하며, 추세가 있으면 ACF가 느리게 감소하고, 계절성이 있으면 계절 주기에서 봉우리가 나타난다. 백색잡음은 모든 자기상관이 0인 시계열이며, Ljung-Box 검정으로 통계적으로 확인한다.

### Ch 3: Time Series Decomposition (L:1181)

**핵심**: 시계열을 추세-순환, 계절, 잔차 성분으로 분해하는 방법을 다룬다. 수학적 변환(Box-Cox), 이동평균, 고전적 분해, X-11/SEATS, STL 분해를 비교한다.

**키워드**: `decomposition`, `trend-cycle`, `seasonality`, `remainder`, `Box-Cox`, `moving average`, `classical decomposition`, `X-11`, `SEATS`, `STL`

**상세**: → `Hyndman-FPP3_full.md` Ch 3 (L:1181)
가법 분해는 $y_t = T_t + S_t + R_t$, 승법 분해는 $y_t = T_t \times S_t \times R_t$로 표현한다. Box-Cox 변환($\lambda$ 파라미터)으로 분산을 안정화한다. 이동평균은 추세-순환 추정의 기본이며, m-MA로 단기 변동을 제거한다. 고전적 분해의 한계(끝점 추정 불가, 계절 패턴 고정)를 X-11과 STL이 보완한다. STL은 LOESS 기반으로 계절 패턴의 변화를 허용하며, 이상치에 강건하고, 모든 주기의 계절성을 처리할 수 있다.

### Ch 4: Time Series Features (L:1778)

**핵심**: 시계열의 정량적 특징(feature)을 추출하여 대규모 시계열 집합을 요약·분류하는 방법을 다룬다.

**키워드**: `features`, `STL features`, `ACF features`, `trend strength`, `seasonal strength`, `feature extraction`, `dimensionality reduction`

**상세**: → `Hyndman-FPP3_full.md` Ch 4 (L:1778)
대규모 시계열 컬렉션에서 개별 시계열을 일일이 시각화하는 것은 불가능하다. 대신 각 시계열에서 정량적 특징을 추출하여 비교한다. 기본 통계(평균, 분산, 최소/최대)부터 ACF 기반 특징(첫 번째 자기상관, 차분 후 자기상관), STL 기반 특징(추세 강도, 계절 강도)까지 다양하다. 추세 강도는 $1 - \text{Var}(R_t)/\text{Var}(T_t + R_t)$로 계산하며, 1에 가까울수록 강한 추세를 의미한다. 추출된 특징들을 주성분 분석(PCA)으로 2차원에 투영하면 유사한 시계열끼리 군집을 형성한다.

### Ch 5: The Forecaster's Toolbox (L:2133)

**핵심**: 예측 워크플로우(모델 정의 → 적합 → 예측 → 평가), 기본 예측 방법(평균, 나이브, 계절나이브, 드리프트), 잔차 진단, 예측 구간, 교차 검증을 다룬다.

**키워드**: `forecasting workflow`, `naive`, `seasonal naive`, `drift`, `residuals`, `Ljung-Box`, `prediction interval`, `accuracy`, `MAE`, `RMSE`, `MAPE`, `MASE`, `cross-validation`, `CRPS`

**상세**: → `Hyndman-FPP3_full.md` Ch 5 (L:2133)
fable 패키지의 워크플로우는 model() → forecast() → accuracy()로 이어진다. 기본 벤치마크 방법으로 평균(MEAN), 나이브(NAIVE), 계절 나이브(SNAIVE), 드리프트(RW with drift)를 사용한다. 잔차 진단에서는 (1) 평균 0, (2) 비상관, (3) 등분산, (4) 정규성을 확인한다. 점 예측 정확도는 MAE, RMSE, MAPE, MASE로 평가하며, 분포 예측 정확도는 CRPS와 Winkler score로 평가한다. 시계열 교차검증(TSCV)은 rolling origin 방식으로 훈련 셋을 점진적으로 확장하며 h-step ahead 예측을 반복 평가한다.

### Ch 6: Judgmental Forecasts (L:3370)

**핵심**: 판단적 예측의 원칙, 한계(인지 편향), Delphi 방법, 유추에 의한 예측, 시나리오 예측, 신제품 예측, 판단적 조정을 다룬다.

**키워드**: `judgmental forecasting`, `cognitive bias`, `anchoring`, `Delphi method`, `analogy`, `scenario forecasting`, `new product forecasting`

**상세**: → `Hyndman-FPP3_full.md` Ch 6 (L:3370)
데이터가 없거나 극히 부족할 때 전문가 판단에 의존한다. 주요 인지 편향으로 가용성 편향, 정박 효과, 과신이 있다. Delphi 방법은 익명성, 반복, 통제된 피드백으로 편향을 줄인다. 유추에 의한 예측은 유사 제품/사건의 과거 데이터를 참조한다. 통계적 예측에 판단적 조정을 더할 때는 구조화된 프로세스를 따라야 하며, 무분별한 조정은 정확도를 오히려 악화시킨다.

### Ch 7: Time Series Regression Models (L:3756)

**핵심**: 시계열 맥락에서의 회귀 모형(추세, 계절, 공변량), 최소제곱 추정, 모형 평가(잔차 진단, 정보 기준), 예측자 선택, 비선형 회귀를 다룬다.

**키워드**: `regression`, `least squares`, `trend`, `dummy variables`, `Fourier terms`, `AIC`, `AICc`, `BIC`, `CV`, `stepwise`, `ex-ante`, `ex-post`, `scenario forecasting`, `piecewise regression`, `spline`

**상세**: → `Hyndman-FPP3_full.md` Ch 7 (L:3756)
시계열 회귀에서 추세는 시간 변수($t$)로, 계절성은 더미 변수 또는 푸리에 항으로 모형화한다. 푸리에 항은 $\sin(2\pi kt/m)$, $\cos(2\pi kt/m)$로 $K$개 항을 포함하며, 더미 변수보다 적은 모수로 복잡한 계절 패턴을 표현할 수 있다. 모형 선택은 수정 $R^2$, AICc, BIC, CV로 하며, AICc가 실무에서 가장 많이 사용된다. Ex-ante 예측은 예측 시점에 예측자 값도 예측해야 하며, 시나리오 예측이 대안이 된다. 구간선형, 스플라인 등 비선형 추세 모형도 다룬다.

### Ch 8: Exponential Smoothing (L:4775)

**핵심**: 단순 지수평활(SES), Holt의 추세법, Holt-Winters 계절법, ETS 상태공간 모형의 분류 체계(오차×추세×계절), 추정과 예측을 다룬다.

**키워드**: `exponential smoothing`, `SES`, `Holt`, `Holt-Winters`, `damped trend`, `ETS`, `state space`, `additive`, `multiplicative`, `AICc`, `forecast interval`

**상세**: → `Hyndman-FPP3_full.md` Ch 8 (L:4775)
SES는 가장 최근 관측에 가장 큰 가중치를 두는 가중 평균이다. 평활 모수 $\alpha$가 1에 가까울수록 최근 데이터에 민감하다. Holt의 방법은 수준과 추세 두 개의 평활 방정식을 사용하며, 감쇠 추세(damped trend)는 장기 예측에서 추세를 점진적으로 0에 수렴시킨다. Holt-Winters는 계절 성분(가법/승법)을 추가한다. ETS는 Error-Trend-Seasonal의 약자로 30가지 모형의 분류 체계를 제공하며, 각 모형을 상태공간으로 표현한다. AICc로 최적 모형을 자동 선택하고, 상태공간 구조에서 예측 구간을 해석적으로 도출한다.

### Ch 9: ARIMA Models (L:5544)

**핵심**: 정상성, 차분, 후방이동 연산자, AR/MA/ARMA/ARIMA 모형, 계절 ARIMA, 자동 모형 선택, ARIMA vs ETS 비교를 다룬다.

**키워드**: `stationarity`, `differencing`, `backshift operator`, `AR`, `MA`, `ARIMA`, `seasonal ARIMA`, `KPSS test`, `unit root`, `ACF`, `PACF`, `auto ARIMA`

**상세**: → `Hyndman-FPP3_full.md` Ch 9 (L:5544)
정상성은 시계열의 통계적 성질이 시간에 불변인 조건이다. 비정상 시계열은 차분으로 정상화한다. KPSS 검정으로 차분 횟수를 결정한다. AR(p) 모형은 과거 $p$개 값의 선형 결합이고, MA(q)는 과거 $q$개 오차의 선형 결합이다. ARIMA(p,d,q)는 $d$차 차분 후 ARMA(p,q)를 적합한 것이다. 계절 ARIMA는 ARIMA$(p,d,q)(P,D,Q)_m$으로 표기하며, 비계절+계절 요소를 곱셈적으로 결합한다. ACF/PACF 패턴으로 모형 차수를 식별하거나, AICc 기반 자동 선택(stepwise)을 사용한다. ARIMA는 ETS와 보완적이며, 두 방법 모두 시도하여 교차검증으로 비교하는 것이 권장된다.

### Ch 10: Dynamic Regression Models (L:6809)

**핵심**: 회귀 오차에 ARIMA 구조를 부여하는 동적 회귀, 추세/계절성/공변량의 동시 모형화, 확률적/결정적 추세의 차이, 시차 예측자를 다룬다.

**키워드**: `dynamic regression`, `regression with ARIMA errors`, `stochastic trend`, `deterministic trend`, `Fourier terms`, `lagged predictors`, `harmonic regression`

**상세**: → `Hyndman-FPP3_full.md` Ch 10 (L:6809)
표준 회귀는 오차가 iid라 가정하지만, 시계열 데이터에서는 오차에 자기상관이 남는다. 동적 회귀는 $y_t = \beta_0 + \beta_1 x_{1,t} + \cdots + \eta_t$에서 $\eta_t$를 ARIMA 과정으로 모형화한다. 추세를 결정적(시간 변수 포함)으로 넣을지, 확률적(차분)으로 처리할지 선택해야 한다. 확률적 추세는 추세 변화에 유연하고, 결정적 추세는 추세가 안정적일 때 적합하다. 푸리에 항을 이용한 조화 회귀는 복잡한 계절 패턴이나 비정수 주기를 처리할 수 있다.

### Ch 11: Forecasting Hierarchical and Grouped Time Series (L:7373)

**핵심**: 계층적/그룹화된 시계열의 구조, 상향/하향/조합 예측, 최소 추적(MinT) 조정, 호주 관광 및 교도소 데이터 사례를 다룬다.

**키워드**: `hierarchical time series`, `grouped time series`, `bottom-up`, `top-down`, `reconciliation`, `MinT`, `coherent forecasts`

**상세**: → `Hyndman-FPP3_full.md` Ch 11 (L:7373)
계층적 시계열은 상위 수준의 합이 하위 수준의 합과 일치해야 한다(정합성). 상향식(bottom-up)은 최하위에서 예측 후 합산하고, 하향식(top-down)은 최상위 예측을 비율로 분배한다. 두 방법 모두 정보 손실이 있다. 최적 조정(reconciliation)은 모든 수준에서 독립적으로 예측한 후, 정합성 제약을 만족하도록 최소분산 기준으로 조정한다(MinT). 이 방법이 상향/하향보다 일관되게 더 정확하다. 교차 시간 축(temporal hierarchy)에도 동일 원리가 적용된다.

### Ch 12: Advanced Forecasting Methods (L:8063)

**핵심**: 복잡한 계절성(다중 계절), Prophet, VAR, 신경망 자기회귀(NNAR), 부트스트랩 예측 구간을 다룬다.

**키워드**: `complex seasonality`, `TBATS`, `STL+ARIMA`, `Prophet`, `VAR`, `neural network`, `NNAR`, `bootstrap prediction interval`

**상세**: → `Hyndman-FPP3_full.md` Ch 12 (L:8063)
일별/시간별 데이터는 주간+연간 등 다중 계절성을 가진다. STL 분해 후 계절 조정된 시리즈에 비계절 모형을 적합하는 방법, 또는 푸리에 항을 사용하는 동적 조화 회귀가 대안이다. Prophet은 가법 분해(추세+계절+공휴일)를 기반으로 비선형 추세, 다중 계절, 불규칙 공휴일을 처리한다. VAR(p)는 다변량 시계열의 상호 의존을 모형화하며, Granger 인과 분석에 사용된다. NNAR(p,P,k)는 AR 구조의 입력을 갖는 피드포워드 신경망이며, 비선형 패턴을 포착하지만 예측 구간은 부트스트랩으로 구해야 한다.

### Ch 13: Some Practical Forecasting Issues (L:8673)

**핵심**: 주간 데이터, 이산 데이터, 예측 한계, 결합 예측, 시계열 집계, 역예측(backcasting), 길이가 다른 시계열, 결측치와 이상치 처리를 다룬다.

**키워드**: `weekly data`, `count data`, `forecast limits`, `forecast combination`, `aggregation`, `backcasting`, `missing values`, `outliers`, `croston method`

**상세**: → `Hyndman-FPP3_full.md` Ch 13 (L:8673)
주간 데이터는 연간 주기가 약 52.18주로 비정수이므로 STL 분해 + 동적 조화 회귀가 적합하다. 이산 카운트 데이터는 Croston 방법이나 정수 ARIMA를 고려한다. 예측의 물리적 한계(음수 불가 등)는 변환이나 절단으로 처리한다. 예측 결합(forecast combination)은 개별 모형보다 일관되게 좋은 성능을 내며, 단순 평균이 복잡한 가중 방식보다 실무에서 잘 작동한다. 결측치는 보간으로 처리하고, 이상치는 결측 후 보간하여 모형 적합에 미치는 영향을 줄인다.
