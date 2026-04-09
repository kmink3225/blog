---
name: "Applied Time Series Analysis and Forecasting with Python"
type: book-summary
authors: "Changquan Huang, Alla Petukhina"
year: 2022
publisher: Springer
total_pages: 365
language: en
keywords: [time-series, forecasting, ARIMA, Python, statistics, econometrics, spectral-analysis, state-space, cointegration, machine-learning]
sources:
  - file: "Huang-AppliedTS_full.md"
    tool: "marker (PDF → MD)"
  - file: "Huang-AppliedTS-images.md"
    tool: "marker (272 figures)"
---

# Applied Time Series Analysis and Forecasting with Python — Summary

> Changquan Huang, Alla Petukhina (2022), Springer, ~365 pages, 10 chapters
> 이론과 Python 실습을 균형 있게 결합한 Springer 시계열 교재. 수학적 기초(정상성, ACF, 분해)부터 ARIMA, 금융 시계열 모델(GARCH), 다변량 분석, 상태 공간 모델, 공적분, 최신 머신러닝 방법까지 Python과 함께 체계적으로 다룬다.

## Contents

- Ch 1: Time Series Concepts and Python (L:232)
- Ch 2: Exploratory Time Series Data Analysis (L:1119)
- Ch 3: Stationary Time Series Models (L:1831)
- Ch 4: ARMA and ARIMA Modeling and Forecasting (L:2828)
- Ch 5: Nonstationary Time Series Models (L:3855)
- Ch 6: Financial Time Series and Related Models (L:4800)
- Ch 7: Multivariate Time Series Analysis (L:5791)
- Ch 8: State Space Models and Markov Switching Models (L:6933)
- Ch 9: Nonstationarity and Cointegrations (L:7735)
- Ch 10: Modern Machine Learning Methods for Time Series Analysis (L:9088)

---

## Chapter Summaries

### Ch 1: Time Series Concepts and Python (L:232)

**핵심**: 시계열의 개념과 역사, Python 기초(설치, 데모, NumPy/pandas/matplotlib/statsmodels 등 패키지), 시계열 모멘트 함수와 정상성(ACF, PACF, 백색 잡음, 랜덤 워크), 데이터 시각화를 다룬다.

**키워드**: `time series concepts`, `Python basics`, `stationarity`, `ACF`, `PACF`, `white noise`, `random walk`, `pandas`, `statsmodels`

**상세**: → `Huang-AppliedTS_full.md` Ch 1 (L:232)
시계열 분석의 역사(Yule의 AR 모델, Slutsky의 MA 모델, Box-Jenkins 방법론 등)를 개관하고 분석 목적(기술, 모델링, 예측, 제어)을 설명한다. Python 프로그래밍 기초를 소개하며, NumPy 배열 연산, pandas DataFrame, statsmodels의 시계열 함수를 실습한다. 모멘트 함수(평균, 자기공분산, ACF, PACF)의 수학적 정의와 Python 계산 방법을 함께 다룬다.

### Ch 2: Exploratory Time Series Data Analysis (L:1119)

**핵심**: PACF의 정의와 계산, 백색 잡음 검정(Box-Pierce, Ljung-Box), 단순 시계열 분해(가산/승산), 분해와 평활 방법(이동평균, Holt-Winters, STL)을 다룬다.

**키워드**: `PACF`, `Ljung-Box test`, `decomposition`, `additive model`, `multiplicative model`, `Holt-Winters`, `STL`, `exponential smoothing`

**상세**: → `Huang-AppliedTS_full.md` Ch 2 (L:1119)
탐색적 시계열 분석의 핵심 도구를 Python으로 실습한다. PACF의 계산(Yule-Walker 연립방정식)과 statsmodels 구현을 설명하고, 백색 잡음 검정을 통해 시계열의 자기상관 유무를 통계적으로 검정한다. 시계열을 추세·계절·잔차로 분해하는 가산/승산 모델을 Python으로 구현하고, Holt-Winters 지수 평활과 STL(Seasonal-Trend decomposition using LOESS)을 활용한 평활 방법을 다룬다.

### Ch 3: Stationary Time Series Models (L:1831)

**핵심**: 단위근 검정(ADF, KPSS, PP), AR 모델(정상성 조건, Yule-Walker), MA 모델(가역성), ARMA 모델, 인과성/가역성 조건을 다룬다.

**키워드**: `unit root`, `ADF test`, `KPSS test`, `AR model`, `MA model`, `ARMA`, `Yule-Walker`, `causality`, `invertibility`

**상세**: → `Huang-AppliedTS_full.md` Ch 3 (L:1831)
정상 시계열 모델의 이론과 Python 구현을 다룬다. ADF(Augmented Dickey-Fuller), KPSS, PP(Phillips-Perron) 단위근 검정을 비교하고 statsmodels로 실행하는 방법을 설명한다. AR(p) 모델의 정상성 조건(특성근이 단위원 밖), MA(q)의 가역성 조건, ARMA(p,q)의 인과성과 가역성을 이론적으로 확립하고 PythonTsa 패키지를 활용한 실습을 포함한다.

### Ch 4: ARMA and ARIMA Modeling and Forecasting (L:2828)

**핵심**: ARMA/ARIMA 모델링 절차(명세 → 추정 → 진단 → 예측), 정보 기준(AIC, BIC, AICC), MLE, 잔차 분석, ARIMA 예측과 예측 한계를 다룬다.

**키워드**: `ARIMA modeling`, `AIC`, `BIC`, `AICC`, `MLE`, `residual diagnostics`, `Box-Jenkins`, `forecasting`, `prediction intervals`

**상세**: → `Huang-AppliedTS_full.md` Ch 4 (L:2828)
Box-Jenkins ARIMA 모델링의 완전한 절차를 Python으로 구현한다. ACF/PACF로 초기 (p,q) 후보를 식별하고, AIC/BIC/AICC로 최적 모델을 선택한 후, 잔차의 자기상관·정규성·등분산성을 점검하는 진단 과정을 수행한다. 적합된 ARIMA 모델로 점 예측과 예측 구간을 생성하고 시각화하는 방법을 실제 경제·금융 데이터에 적용한다.

### Ch 5: Nonstationary Time Series Models (L:3855)

**핵심**: 단위근 과정, ARIMA 모델, 결정론적 vs. 확률론적 추세, 분수 차분(ARFIMA), Box-Cox 변환을 다룬다.

**키워드**: `ARIMA`, `unit root process`, `deterministic trend`, `stochastic trend`, `fractional differencing`, `ARFIMA`, `Box-Cox`

**상세**: → `Huang-AppliedTS_full.md` Ch 5 (L:3855)
비정상 시계열의 두 가지 유형(결정론적 추세와 확률적 추세/단위근)의 차이를 명확히 한다. ARIMA(p,d,q)에서 차분 횟수 d의 결정과 과도 차분의 위험성을 설명한다. 분수 차분을 통한 장기 기억 ARFIMA 모델과 Box-Cox 분산 안정화 변환을 Python으로 구현하는 방법을 다룬다.

### Ch 6: Financial Time Series and Related Models (L:4800)

**핵심**: 금융 시계열의 특성(정형화 사실), ARCH 효과 검정, ARCH(1), GARCH(p,q), EGARCH, GJR-GARCH, 변동성 예측, Python 구현을 다룬다.

**키워드**: `financial time series`, `stylized facts`, `ARCH`, `GARCH`, `EGARCH`, `GJR-GARCH`, `volatility forecasting`, `arch library`

**상세**: → `Huang-AppliedTS_full.md` Ch 6 (L:4800)
주식 수익률, 환율 등 금융 시계열의 정형화 사실(heavy tails, 변동성 클러스터링, 레버리지 효과)을 분석한다. Lagrange multiplier 검정으로 ARCH 효과를 검정하고, ARCH(1), GARCH(1,1), 비대칭 GARCH(EGARCH, GJR-GARCH)를 Python arch 패키지로 추정하는 방법을 설명한다. 변동성 예측과 리스크 측도(VaR) 계산 방법도 포함한다.

### Ch 7: Multivariate Time Series Analysis (L:5791)

**핵심**: VAR 모델(인과성, 안정성, 차수 선택, 예측), Granger 인과성, 충격 반응 함수(IRF), 예측 오차 분산 분해(FEVD), VARMA, VARX를 다룬다.

**키워드**: `VAR`, `Granger causality`, `impulse response function`, `FEVD`, `VARMA`, `VARX`, `vector autoregression`, `multivariate`

**상세**: → `Huang-AppliedTS_full.md` Ch 7 (L:5791)
다변량 시계열 분석의 핵심 방법론을 Python으로 구현한다. VAR(p) 모델의 인과성(안정성) 조건, AIC/BIC를 통한 차수 p 선택, MLE 추정을 설명하고 statsmodels VAR으로 실습한다. Granger 인과성 검정으로 변수 간 인과 방향을 탐색하고, 충격 반응 함수(IRF)와 예측 오차 분산 분해(FEVD)로 모델을 해석한다.

### Ch 8: State Space Models and Markov Switching Models (L:6933)

**핵심**: 선형 상태 공간 모델, 칼만 필터와 스무더, EM 알고리즘, 국소 선형 추세 모델, 체제 전환(Markov switching) AR/ARMA 모델을 다룬다.

**키워드**: `state space`, `Kalman filter`, `Kalman smoother`, `EM algorithm`, `local linear trend`, `Markov switching`, `regime switching`

**상세**: → `Huang-AppliedTS_full.md` Ch 8 (L:6933)
상태 공간 프레임워크를 Python statsmodels로 구현한다. 선형 가우스 상태 공간 모델의 칼만 필터(일단계 예측 갱신)와 스무더(역방향 통과) 알고리즘을 설명하고, EM 알고리즘을 통한 파라미터 추정을 다룬다. 국소 선형 추세 모델을 상태 공간으로 표현하고 실제 거시경제 데이터에 적용한다. 해밀턴 Markov 전환 모델로 경기 사이클의 체제 변화를 모델링하는 방법도 포함한다.

### Ch 9: Nonstationarity and Cointegrations (L:7735)

**핵심**: 단위근 검정 복습, 공적분(Engle-Granger, Johansen), 오차 수정 모델(ECM/VECM), 장기 균형 관계, Python 구현을 다룬다.

**키워드**: `cointegration`, `Engle-Granger`, `Johansen test`, `ECM`, `VECM`, `long-run equilibrium`, `error correction`

**상세**: → `Huang-AppliedTS_full.md` Ch 9 (L:7735)
여러 비정상 시계열 간의 장기 균형 관계인 공적분을 분석한다. Engle-Granger 2단계 방법과 Johansen 최대우도 검정으로 공적분 관계를 탐색하고 공적분 벡터를 추정한다. 단기 동학을 포착하는 오차 수정 모델(ECM)과 다변량 VECM을 statsmodels로 구현하며, 매크로경제 변수(소비-소득, 주가 등)의 장기 균형 분석 예시를 다룬다.

### Ch 10: Modern Machine Learning Methods for Time Series Analysis (L:9088)

**핵심**: 머신러닝 기반 시계열 예측(랜덤 포레스트, XGBoost, LSTM), 특성 공학, 앙상블 방법, 하이퍼파라미터 최적화, 딥러닝 예측 모델을 다룬다.

**키워드**: `machine learning`, `random forest`, `XGBoost`, `LSTM`, `feature engineering`, `ensemble`, `hyperparameter tuning`, `deep learning`

**상세**: → `Huang-AppliedTS_full.md` Ch 10 (L:9088)
전통적 통계 모델을 넘어서는 현대 머신러닝 방법을 시계열 예측에 적용한다. 시계열을 지도 학습 문제로 변환하는 특성 공학(lag features, rolling statistics, calendar features)을 설명하고, 랜덤 포레스트, XGBoost, LightGBM을 Python sklearn/xgboost로 구현한다. LSTM 기반 딥러닝 예측 모델을 Keras로 구현하고 전통적 ARIMA 모델과 성능을 비교한다. 교차검증 기반 하이퍼파라미터 최적화 방법도 포함한다.
