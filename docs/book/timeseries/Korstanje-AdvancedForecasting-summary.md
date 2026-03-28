---
name: "Advanced Forecasting with Python"
type: book-summary
authors: "Joos Korstanje"
year: 2021
publisher: Apress
total_pages: 296
language: en
keywords: [time-series, forecasting, ARIMA, prophet, DeepAR, LSTM, machine-learning, Python, AR, MA, SARIMA, VAR, ARCH, GARCH, XGBoost, LightGBM, deep-learning]
sources:
  - file: "Korstanje-AdvancedForecasting_full.md"
    tool: "marker (PDF → MD)"
  - file: "Korstanje-AdvancedForecasting-images.md"
    tool: "marker (101 figures)"
---

# Advanced Forecasting with Python — Summary

> Joos Korstanje (2021), Apress, ~296 pages, 21 chapters
> 시계열 예측의 전반적인 모델 생태계를 탐색하는 실무 교과서. 고전 통계 모델(AR, MA, ARIMA, SARIMA, VAR)부터 지도 학습(XGBoost, LightGBM), 딥러닝(LSTM, RNN, GRU), Facebook Prophet, Amazon DeepAR까지 Python 코드와 함께 단계적으로 다룬다.

## Contents

### Part I: Machine Learning for Forecasting (Ch 1-2)
- Ch 1: Models for Forecasting (L:296)
- Ch 2: Model Evaluation for Forecasting (L:670)

### Part II: Univariate Time Series Models (Ch 3-7)
- Ch 3: The AR Model (L:1170)
- Ch 4: The MA Model (L:1724)
- Ch 5: The ARMA Model (L:2087)
- Ch 6: The ARIMA Model (L:2453)
- Ch 7: The SARIMA Model (L:2647)

### Part III: Multivariate Time Series Models (Ch 8-10)
- Ch 8: The SARIMAX Model (L:2823)
- Ch 9: The VAR Model (L:2980)
- Ch 10: The VARMAX Model (L:3120)

### Part IV: Supervised Machine Learning Models (Ch 11-15)
- Ch 11: The Linear Regression (L:3225)
- Ch 12: The Decision Tree Model (L:3432)
- Ch 13: The kNN Model (L:3661)
- Ch 14: The Random Forest (L:3846)
- Ch 15: Gradient Boosting with XGBoost and LightGBM (L:4165)

### Part V: Advanced Machine and Deep Learning Models (Ch 16-21)
- Ch 16: Neural Networks (L:4425)
- Ch 17: RNNs Using SimpleRNN and GRU (L:4827)
- Ch 18: LSTM RNNs (L:5189)
- Ch 19: The Prophet Model (L:5404)
- Ch 20: The DeepAR Model (L:5809)
- Ch 21: Model Selection (L:6117)

---

## Chapter Summaries

### Ch 1: Models for Forecasting (L:296)

**핵심**: 머신러닝 예측 모델의 전체 지형을 소개한다. 단변량 시계열 모델과 지도 학습 모델의 차이, 회귀 대 분류, 단변량 대 다변량 구분을 설명하며 책의 로드맵을 제시한다.

**키워드**: `univariate`, `supervised learning`, `regression`, `classification`, `machine learning landscape`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 1 (L:296)
예측 모델은 크게 시계열 접근과 지도 학습 접근으로 나뉜다. 시계열 접근은 과거 값의 자기상관을 모델링하며, 지도 학습은 특성 행렬과 타깃 벡터를 구성해 범용 ML 알고리즘을 적용한다. 상관 계수, 단변량/다변량 구분, 지도/비지도 구분 등 기초 개념을 Python 예시와 함께 설명한다. 이 책은 두 접근을 모두 다루며 각 챕터에서 실제 데이터셋에 적용하는 방식으로 진행된다.

### Ch 2: Model Evaluation for Forecasting (L:670)

**핵심**: MSE, RMSE, MAE, MAPE, R² 등 예측 품질 지표와 학습-검증 전략(train-test split, 교차검증, 시계열 교차검증, 백테스팅)을 다룬다.

**키워드**: `MSE`, `RMSE`, `MAE`, `MAPE`, `R²`, `train-test split`, `cross-validation`, `backtesting`, `walk-forward`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 2 (L:670)
예측 모델 평가는 일반 ML과 다르다. 시계열은 순서가 있으므로 k-fold 교차검증 대신 시계열 교차검증(walk-forward validation)이나 백테스팅이 적합하다. 각 지표의 특성과 적합한 사용 상황을 설명하고 Python 코드로 구현한다. 과적합의 위험과 out-of-sample 오차의 중요성을 강조한다.

### Ch 3: The AR Model (L:1170)

**핵심**: 자기회귀(AR) 모델의 개념, ACF/PACF, 정상성과 ADF 검정, Yule-Walker 방정식을 통한 계수 추정, 하이퍼파라미터 튜닝을 다룬다.

**키워드**: `AR`, `autocorrelation`, `PACF`, `stationarity`, `ADF test`, `differencing`, `Yule-Walker`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 3 (L:1170)
AR 모델은 과거 값들의 선형 결합으로 현재 값을 예측한다. 정상성 검정(ADF)과 차분을 통한 정상화 방법을 지진 데이터로 실습한다. PACF로 AR 차수를 결정하고, Yule-Walker 방정식으로 계수를 추정한다. 시계열 교차검증으로 최적 차수 p를 선택하는 방법을 보인다.

### Ch 4: The MA Model (L:1724)

**핵심**: 이동평균(MA) 모델의 정의, ACF 패턴으로 차수 결정, AR과 MA의 구분, statsmodels ARMA를 활용한 적합, 다단계 예측과 그리드 서치를 다룬다.

**키워드**: `MA`, `moving average`, `ACF`, `invertibility`, `multistep forecasting`, `grid search`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 4 (L:1724)
MA 모델은 과거 오차 항들의 선형 결합으로 현재 값을 예측한다. ACF가 차수 q 이후 급격히 0에 가까워지는 패턴으로 식별한다. 실제 시계열 데이터에 MA 모델을 적합하고 다단계 예측(model retraining 방식)과 그리드 서치를 통한 최적 차수 선택을 Python으로 구현한다.

### Ch 5: The ARMA Model (L:2087)

**핵심**: ARMA 모델의 수학적 정의, AIC/BIC 기반 자동 하이퍼파라미터 튜닝, 태양흑점 데이터 예측 예시를 다룬다.

**키워드**: `ARMA`, `AIC`, `BIC`, `sunspots`, `automated hyperparameter tuning`, `grid search`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 5 (L:2087)
ARMA(p,q)는 AR과 MA를 결합한 모델로, 정상 시계열의 복잡한 자기상관 구조를 포착한다. 태양흑점 데이터를 활용해 ARMA(1,1) 적합 과정을 보이고, AIC 기반 그리드 서치로 최적 (p,q) 조합을 자동으로 탐색하는 방법을 설명한다. MSE, AIC, BIC 등 다양한 평가 지표를 비교한다.

### Ch 6: The ARIMA Model (L:2453)

**핵심**: ARIMA(p,d,q) 모델 정의, 차분(d) 파라미터의 역할, CO2 농도 데이터 적용 예시를 다룬다.

**키워드**: `ARIMA`, `integration`, `differencing`, `non-stationary`, `CO2`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 6 (L:2453)
ARIMA는 비정상 시계열을 d번 차분하여 정상화한 후 ARMA를 적용한다. CO2 농도 시계열에 ARIMA를 적용하여 비정상성 처리와 예측을 보인다. 차분 횟수 d의 선택 방법과 ADF 검정을 통한 정상성 확인 절차를 설명한다.

### Ch 7: The SARIMA Model (L:2647)

**핵심**: 계절성을 가진 시계열을 위한 SARIMA(p,d,q)(P,D,Q)m 모델, Walmart 매출 데이터 적용 예시를 다룬다.

**키워드**: `SARIMA`, `seasonality`, `seasonal differencing`, `Walmart sales`, `seasonal patterns`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 7 (L:2647)
SARIMA는 ARIMA에 계절성 컴포넌트 (P,D,Q)m을 추가한 모델이다. Walmart 매출 데이터에 적용하여 계절 패턴 포착 방법을 보인다. 단변량 시계열 모델 분류 체계(AR→MA→ARMA→ARIMA→SARIMA)를 정리하고 각 모델의 적용 범위를 비교한다.

### Ch 8: The SARIMAX Model (L:2823)

**핵심**: 외생 변수를 포함하는 SARIMAX 모델, 지도 학습 모델과의 비교, Walmart 데이터셋 적용을 다룬다.

**키워드**: `SARIMAX`, `exogenous variables`, `external regressors`, `multivariate`, `supervised vs SARIMAX`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 8 (L:2823)
SARIMAX는 SARIMA에 외생 변수(exogenous variables)를 추가한 모델로, 외부 요인의 영향을 명시적으로 모델링한다. 지도 학습 모델과의 차이점을 비교하고 Walmart 데이터셋에 적용하여 외생 변수 포함 효과를 분석한다.

### Ch 9: The VAR Model (L:2980)

**핵심**: 다변량 시계열을 위한 VAR(p) 모델, 계수 추정, 단변량 다중 모델 대비 장점, Walmart 매출 예측 예시를 다룬다.

**키워드**: `VAR`, `multivariate`, `vector autoregression`, `Granger causality`, `Walmart`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 9 (L:2980)
VAR(p) 모델은 여러 시계열 간의 상호 의존성을 동시에 모델링한다. 하이퍼파라미터는 시차 p 하나뿐이며, 정상성이 필요하다. Walmart 복수 제품 매출 데이터에 VAR을 적용하여 단일 시계열 모델 여러 개를 사용하는 경우와 성능을 비교한다.

### Ch 10: The VARMAX Model (L:3120)

**핵심**: VAR의 확장인 VARMAX 모델(외생 변수 포함 다변량 모델), 모델 정의와 Python 구현을 다룬다.

**키워드**: `VARMAX`, `multivariate`, `exogenous`, `multiple time series`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 10 (L:3120)
VARMAX는 VAR에 이동평균과 외생 변수를 추가한 완전한 다변량 시계열 모델이다. 여러 시계열과 외부 변수가 동시에 존재하는 시나리오에 적용하며, statsmodels VARMAX 구현을 통해 모델링 절차를 설명한다.

### Ch 11: The Linear Regression (L:3225)

**핵심**: 시계열 예측에 선형 회귀를 적용하는 지도 학습 접근 방식, 특성 엔지니어링(lag features), CO2 예측 예시를 다룬다.

**키워드**: `linear regression`, `lag features`, `supervised learning`, `feature engineering`, `CO2`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 11 (L:3225)
지도 학습 접근에서는 시계열을 lag feature를 사용한 지도 학습 문제로 변환한다. 선형 회귀 모델의 수학적 정의와 sklearn 구현을 CO2 수준 예측에 적용한다. 지도 학습 접근의 장단점(feature engineering 필요, 일반 ML 도구 사용 가능)을 논의한다.

### Ch 12: The Decision Tree Model (L:3432)

**핵심**: 의사결정 트리의 수학적 원리(분기, 가지치기), 시계열 예측 적용, 과적합 제어를 다룬다.

**키워드**: `decision tree`, `splitting`, `pruning`, `overfitting`, `non-linear`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 12 (L:3432)
의사결정 트리는 비선형 패턴을 포착할 수 있는 지도 학습 모델이다. 분기 기준(gini, entropy)과 가지치기(복잡도 제어)를 설명하고 시계열 예측에 적용한다. 과적합 문제와 max_depth 등 하이퍼파라미터 튜닝 방법을 다룬다.

### Ch 13: The kNN Model (L:3661)

**핵심**: k-최근접이웃 모델의 직관적 설명, 거리 척도, k 값 결정, 그리드 서치와 랜덤 서치, 교통량 예측 예시를 다룬다.

**키워드**: `kNN`, `nearest neighbors`, `distance metric`, `grid search`, `random search`, `traffic`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 13 (L:3661)
kNN은 유사한 과거 패턴으로부터 예측값을 추론하는 비모수적 방법이다. 교통량 예측 문제에 적용하여 이웃 수 k 선택의 중요성을 보인다. 그리드 서치 외에 분포 기반 랜덤 서치를 대안으로 소개한다.

### Ch 14: The Random Forest (L:3846)

**핵심**: 앙상블 학습(배깅), 변수 서브셋 선택, 특성 중요도, 태양흑점 예측, 랜덤 서치 교차검증을 다룬다.

**키워드**: `random forest`, `ensemble`, `bagging`, `bootstrap`, `feature importance`, `RandomizedSearchCV`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 14 (L:3846)
랜덤 포레스트는 여러 의사결정 트리를 부트스트랩 샘플과 랜덤 변수 서브셋으로 학습하는 앙상블 모델이다. max_features와 n_estimators 두 가지 핵심 하이퍼파라미터의 분포 기반 랜덤 서치를 설명하고 특성 중요도(feature importance)를 통한 모델 해석 방법을 보인다.

### Ch 15: Gradient Boosting with XGBoost and LightGBM (L:4165)

**핵심**: 그래디언트 부스팅의 이론, XGBoost와 LightGBM의 차이, 베이지안 최적화(scikit-optimize)를 활용한 하이퍼파라미터 튜닝, 교통량 예측을 다룬다.

**키워드**: `XGBoost`, `LightGBM`, `gradient boosting`, `Bayesian optimization`, `scikit-optimize`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 15 (L:4165)
그래디언트 부스팅은 잔차를 순차적으로 피팅하는 앙상블 방법이다. XGBoost와 LightGBM의 구조적 차이(레벨 vs. 리프 기반 성장)를 비교하고 교통량 데이터에 각각 적용한다. scikit-optimize를 활용한 베이지안 최적화로 효율적 하이퍼파라미터 탐색을 구현한다.

### Ch 16: Neural Networks (L:4425)

**핵심**: 완전 연결 신경망의 구조, 활성화 함수, 역전파, 옵티마이저, 학습률, PCA, Keras 구현을 다룬다.

**키워드**: `neural network`, `backpropagation`, `activation function`, `optimizer`, `learning rate`, `PCA`, `Keras`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 16 (L:4425)
완전 연결 신경망의 기초 구조와 학습 원리를 설명하고 Keras로 구현한다. 시계열 예측을 위한 데이터 전처리(스케일링, PCA)를 다루고, 주요 하이퍼파라미터(레이어 수, 유닛 수, 학습률, 배치 크기)의 역할을 설명한다.

### Ch 17: RNNs Using SimpleRNN and GRU (L:4827)

**핵심**: 순환 신경망(RNN)의 구조, SimpleRNN 내부 메커니즘, GRU의 개선점, 시퀀스 예측, Keras 구현을 다룬다.

**키워드**: `RNN`, `SimpleRNN`, `GRU`, `gated recurrent unit`, `sequence prediction`, `Keras`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 17 (L:4827)
RNN은 은닉 상태를 통해 시퀀스의 시간적 의존성을 학습한다. SimpleRNN의 내부 구조를 설명한 후 그래디언트 소실 문제를 완화하는 GRU를 소개한다. 단일 값 예측과 시퀀스 예측 두 가지 출력 방식을 Keras로 구현하고 비교한다.

### Ch 18: LSTM RNNs (L:5189)

**핵심**: LSTM 셀의 구조(forget gate, input gate, output gate), 장기 의존성 학습, 다층 LSTM 구현과 성능 비교를 다룬다.

**키워드**: `LSTM`, `long short-term memory`, `forget gate`, `cell state`, `deep LSTM`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 18 (L:5189)
LSTM은 셀 상태(cell state)와 세 가지 게이트(forget, input, output)로 장기 의존성을 효과적으로 학습한다. 단순 LSTM(1층 8유닛)과 깊은 LSTM(3층 64유닛)을 비교하여 모델 복잡도가 성능에 미치는 영향을 분석한다.

### Ch 19: The Prophet Model (L:5404)

**핵심**: Facebook Prophet의 분해 모델(추세 + 계절성 + 휴일), 월간/연간 계절성 추가, 휴일 데이터, 추가 회귀변수, 그리드 서치를 다룬다.

**키워드**: `Prophet`, `trend`, `seasonality`, `holiday effects`, `additive model`, `Fourier series`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 19 (L:5404)
Prophet은 추세, 계절성, 휴일 효과를 가산 분해하는 모델로 비통계학자도 직관적으로 사용할 수 있다. 소매 매출 데이터에 기본 모델부터 월간 계절성, 휴일, 추가 회귀변수를 단계적으로 추가하며 예측 성능 개선을 확인한다. 그리드 서치로 Prophet의 주요 하이퍼파라미터를 최적화한다.

### Ch 20: The DeepAR Model (L:5809)

**핵심**: Amazon DeepAR의 확률적 예측, GluonTS를 활용한 훈련과 예측, 확률 구간, 추가 회귀변수, 하이퍼파라미터를 다룬다.

**키워드**: `DeepAR`, `probabilistic forecasting`, `GluonTS`, `quantile`, `LSTM-based`, `Amazon`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 20 (L:5809)
DeepAR은 LSTM 기반 확률적 예측 모델로 점 예측 외에 예측 분포를 제공한다. GluonTS 라이브러리를 활용한 훈련과 추론 코드를 단계적으로 구현한다. 확률 예측의 활용(분위수 예측, 리스크 관리), 추가 회귀변수 통합, 주요 하이퍼파라미터 설명을 포함한다.

### Ch 21: Model Selection (L:6117)

**핵심**: 여러 예측 모델 중 최적 모델을 선택하기 위한 기준(지표, 구조, 입력, 복잡도, 해석 가능성, 안정성)을 다룬다.

**키워드**: `model selection`, `bias-variance tradeoff`, `interpretability`, `model stability`, `forecasting horizon`

**상세**: → `Korstanje-AdvancedForecasting_full.md` Ch 21 (L:6117)
실무에서 모델 선택은 단순히 검증 오차만으로 결정되지 않는다. 모델 구조와 입력 방식(단변량 vs. 다변량), 단기 vs. 장기 예측 성능, 모델 복잡도와 성능 이득의 트레이드오프, 해석 가능성 요구사항, 예측 안정성을 종합적으로 고려해야 한다. 이 챕터는 책 전체의 모델들을 비교하는 결론부 역할을 한다.
