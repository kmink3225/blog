---
name: "Time Series Forecasting in Python"
type: book-summary
authors: "Marco Peixeiro"
year: 2022
publisher: Manning
total_pages: 435
language: en
keywords: [time-series, forecasting, Python, ARIMA, AR, MA, SARIMA, VAR, deep-learning, LSTM, N-BEATS, Prophet, statsmodels]
sources:
  - file: "Peixeiro-TSForecasting_full.md"
    tool: "marker (PDF → MD)"
  - file: "Peixeiro-TSForecasting-images.md"
    tool: "marker (225 figures)"
---

# Time Series Forecasting in Python — Summary

> Marco Peixeiro (2022), Manning, ~435 pages, 21 chapters
> 시계열 예측의 기초부터 딥러닝, 자동화 예측까지 체계적으로 다루는 Manning 실습 교과서. 각 챕터는 구체적인 예측 문제(구글 주가, 약품 처방 건수, 전력 소비 등)를 중심으로 이론과 Python 구현을 함께 제시한다.

## Contents

### Part 1: Time Waits for No One (Ch 1-3)
- Ch 1: Understanding time series forecasting (L:427)
- Ch 2: A naive prediction of the future (L:622)
- Ch 3: Going on a random walk (L:989)

### Part 2: Forecasting with Statistical Models (Ch 4-11)
- Ch 4: Modeling a moving average process (L:1635)
- Ch 5: Modeling an autoregressive process (L:2168)
- Ch 6: Modeling complex time series (L:2700)
- Ch 7: Forecasting non-stationary time series (L:3703)
- Ch 8: Accounting for seasonality (L:4094)
- Ch 9: Adding external variables to our model (L:4662)
- Ch 10: Forecasting multiple time series (L:5116)
- Ch 11: Capstone: Forecasting antidiabetic drug prescriptions in Australia (L:5620)

### Part 3: Large-Scale Forecasting with Deep Learning (Ch 12-18)
- Ch 12: Introducing deep learning for time series forecasting (L:6023)
- Ch 13: Data windowing and creating baselines for deep learning (L:6346)
- Ch 14: Baby steps with deep learning (L:7100)
- Ch 15: Remembering the past with LSTM (L:7530)
- Ch 16: Filtering a time series with CNN (L:7876)
- Ch 17: Using predictions to make more predictions (L:8231)
- Ch 18: Capstone: Forecasting electric power consumption (L:8478)

### Part 4: Automating Forecasting at Scale (Ch 19-21)
- Ch 19: Automating time series forecasting with Prophet (L:9432)
- Ch 20: Capstone: Forecasting steak prices in Canada (L:10060)
- Ch 21: Going above and beyond (L:10560)

---

## Chapter Summaries

### Ch 1: Understanding time series forecasting (L:427)

**핵심**: 시계열의 정의, 트렌드·계절성·잔차 분해, 예측 프로세스(목표 설정 → 데이터 수집 → 모델 개발 → 배포 → 모니터링), 일반 회귀와의 차이를 다룬다.

**키워드**: `time series`, `trend`, `seasonality`, `components`, `forecasting process`, `temporal order`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 1 (L:427)
시계열은 시간 순서로 관측된 데이터로, 트렌드·계절성·주기·잔차 성분으로 분해된다. 예측 프로세스는 목표 설정, 데이터 수집, 모델 개발, 배포, 모니터링, 새 데이터 수집의 순환 구조로 진행된다. 시계열 예측이 일반 회귀와 다른 이유(시간 순서, feature 부재 가능성)를 설명하고 책의 전체 로드맵을 제시한다.

### Ch 2: A naive prediction of the future (L:622)

**핵심**: 기준선(baseline) 모델의 중요성, 역사적 평균, 전년도 평균, 마지막 알려진 값, 순진한 계절 예측(naive seasonal forecast)을 Python으로 구현한다.

**키워드**: `baseline`, `historical mean`, `naive forecast`, `last known value`, `seasonal naive`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 2 (L:622)
복잡한 모델 개발 전에 단순 기준선 모델을 구축하는 것이 필수적이다. 역사적 평균, 전년도 평균, 마지막 값 반복, 계절 순진 예측 네 가지 기준선을 구현하고 비교한다. statsmodels를 이용한 실습 환경 설정과 예측 시각화 방법을 함께 다룬다.

### Ch 3: Going on a random walk (L:989)

**핵심**: 랜덤 워크 과정의 정의와 시뮬레이션, 정상성 개념, ADF 검정, ACF를 통한 랜덤 워크 식별, 단기/장기 랜덤 워크 예측을 다룬다.

**키워드**: `random walk`, `stationarity`, `ADF test`, `ACF`, `GOOGL stock`, `drift`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 3 (L:989)
랜덤 워크는 현재 값이 이전 값에 백색잡음이 더해진 과정으로, 비정상 시계열의 대표 예시이다. Google 주가 데이터가 랜덤 워크인지 ADF 검정과 ACF로 판단하는 방법을 실습한다. 랜덤 워크의 단기(마지막 값 사용)와 장기(평균 수준) 예측 전략의 차이를 설명하고 예측 불확실성의 시간적 증가를 보인다.

### Ch 4: Modeling a moving average process (L:1635)

**핵심**: MA(q) 과정의 정의, ACF 패턴으로 차수 결정, statsmodels ARMA를 활용한 적합, 예측 방법을 다룬다.

**키워드**: `MA`, `moving average`, `ACF`, `order selection`, `invertibility`, `ARMA`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 4 (L:1635)
MA(q) 과정은 과거 q개의 백색잡음 오차의 선형 결합이다. ACF가 차수 q 이후 급격히 0이 되는 절단(cutoff) 패턴으로 q를 식별한다. 시뮬레이션 데이터로 MA 과정을 생성하고 statsmodels로 적합한 후 예측을 수행하는 전체 워크플로를 다룬다.

### Ch 5: Modeling an autoregressive process (L:2168)

**핵심**: AR(p) 과정의 정의, PACF로 차수 결정, 소매점 유동인구 예측 사례, 정상 AR 과정의 차수 식별 방법을 다룬다.

**키워드**: `AR`, `autoregressive`, `PACF`, `order selection`, `retail foot traffic`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 5 (L:2168)
AR(p) 과정은 과거 p개의 관측값의 선형 결합이다. PACF가 차수 p 이후 절단되는 패턴으로 p를 식별한다. 소매점 주간 유동인구 예측 문제를 통해 AR 모델 적합, 진단, 예측 전체 과정을 실습하고 AR과 MA의 ACF/PACF 패턴 차이를 비교한다.

### Ch 6: Modeling complex time series (L:2700)

**핵심**: ARMA(p,q) 모델, AIC 기반 일반 모델링 절차(탐색 → 모델 적합 → 잔차 분석), 대역폭 예측 사례를 다룬다.

**키워드**: `ARMA`, `AIC`, `model selection`, `residual analysis`, `Ljung-Box`, `bandwidth forecasting`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 6 (L:2700)
복잡한 시계열은 AR 또는 MA만으로 포착되지 않아 ARMA가 필요하다. AIC를 기준으로 (p,q) 조합을 탐색하는 일반 모델링 절차를 제시하고, 잔차 분석(Ljung-Box 검정, Q-Q plot)으로 모델 적합성을 진단하는 방법을 설명한다. 데이터 센터 대역폭 예측에 ARMA를 적용하는 전체 과정을 다룬다.

### Ch 7: Forecasting non-stationary time series (L:3703)

**핵심**: ARIMA(p,d,q) 모델, 차분(d)을 통한 비정상 시계열 처리, 일반 모델링 절차 수정, 비정상 시계열 예측을 다룬다.

**키워드**: `ARIMA`, `non-stationary`, `differencing`, `integration`, `ADF test`, `order of integration`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 7 (L:3703)
ARIMA는 비정상 시계열을 d번 차분하여 정상화한 후 ARMA를 적용한다. ADF 검정으로 차분 횟수 d를 결정하는 절차를 포함한 수정된 일반 모델링 절차를 제시한다. Ch 4, 5, 6에서 사용한 데이터셋에 ARIMA를 적용하여 이전 모델과 성능을 비교한다.

### Ch 8: Accounting for seasonality (L:4094)

**핵심**: SARIMA(p,d,q)(P,D,Q)m 모델, 계절 패턴 식별, 월별 항공 승객 데이터 예측, ARIMA vs. SARIMA 성능 비교를 다룬다.

**키워드**: `SARIMA`, `seasonality`, `seasonal ARIMA`, `airline passengers`, `seasonal differencing`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 8 (L:4094)
SARIMA는 ARIMA에 계절성 컴포넌트 (P,D,Q)m을 추가하여 계절 패턴을 명시적으로 모델링한다. 월별 항공 승객 수 데이터(고전적 시계열 벤치마크)에 ARIMA와 SARIMA를 각각 적용하고 성능 차이를 시각적으로 비교한다. 계절 차분 필요성 판단 방법을 설명한다.

### Ch 9: Adding external variables to our model (L:4662)

**핵심**: SARIMAX 모델, 외생 변수의 역할과 주의사항(미래 값 필요), 미국 거시경제 데이터를 활용한 실질 GDP 예측을 다룬다.

**키워드**: `SARIMAX`, `exogenous variables`, `real GDP`, `macroeconomics`, `lagged regressors`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 9 (L:4662)
SARIMAX는 SARIMA에 외생 변수를 추가한 모델로, 예측 시 외생 변수의 미래 값도 필요하다는 중요한 주의사항이 있다. 미국 거시경제 데이터셋을 탐색하고, 실질 GDP 예측에 외생 변수로 금리, 인플레이션 등을 포함한 SARIMAX를 적용한다.

### Ch 10: Forecasting multiple time series (L:5116)

**핵심**: VAR(p) 모델, Granger 인과성 검정, VAR 모델링 절차, 실질 가처분 소득과 실질 소비 예측을 다룬다.

**키워드**: `VAR`, `Granger causality`, `vector autoregression`, `real disposable income`, `consumption`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 10 (L:5116)
VAR(p)는 여러 시계열의 상호 의존성을 동시에 모델링하는 다변량 접근이다. Granger 인과성 검정으로 변수 간 인과 관계를 탐색하는 방법을 포함한 VAR 모델링 절차를 제시한다. 미국 경제 데이터에서 실질 가처분 소득과 소비를 동시에 예측하는 실습을 수행한다.

### Ch 11: Capstone: Forecasting antidiabetic drug prescriptions in Australia (L:5620)

**핵심**: 호주 항당뇨약 월별 처방 건수 예측 캡스톤 프로젝트. Ch 1-10에서 학습한 통계 모델을 종합 적용한다.

**키워드**: `capstone`, `SARIMA`, `pharmaceutical`, `Australia`, `statsmodels`, `AIC`, `model selection`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 11 (L:5620)
실제 의약품 처방 데이터를 분석하고 강한 계절성을 포착하는 SARIMA 모델을 선택한다. 데이터 탐색, 정상성 검정, 모델 선택(AIC), 잔차 진단, 예측 생성 및 평가의 전체 파이프라인을 수행한다. 통계적 예측 방법의 한계와 딥러닝 접근의 필요성으로 Part 3를 예고한다.

### Ch 12: Introducing deep learning for time series forecasting (L:6023)

**핵심**: 시계열 예측에 딥러닝을 사용할 때와 안 할 때, TensorFlow/Keras 환경 설정, 신경망 기초, 훈련 절차를 다룬다.

**키워드**: `deep learning`, `TensorFlow`, `Keras`, `neural network basics`, `when to use DL`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 12 (L:6023)
딥러닝은 대규모 데이터, 복잡한 비선형 패턴, 다변량 시나리오에서 강점을 가지지만 소규모 데이터나 해석 가능성이 중요한 경우 통계 모델이 더 적합하다. TensorFlow 2.x와 Keras API를 활용한 시계열 딥러닝 환경을 설정하고 신경망의 기초 학습 원리를 설명한다.

### Ch 13: Data windowing and creating baselines for deep learning (L:6346)

**핵심**: 딥러닝을 위한 데이터 윈도잉(시퀀스 구성), 기준선 모델(단순 회귀, 마지막 값) 구축, 다단계 예측 설정을 다룬다.

**키워드**: `data windowing`, `sequence construction`, `baseline`, `multi-step forecasting`, `DataWindow class`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 13 (L:6346)
딥러닝 모델을 위해 시계열을 (입력 윈도우, 예측 윈도우) 쌍으로 변환하는 데이터 윈도잉 과정을 구현한다. 재사용 가능한 DataWindow 클래스를 구축하고 단일 및 다단계 기준선 모델을 만들어 이후 복잡한 모델의 비교 기준을 확립한다.

### Ch 14: Baby steps with deep learning (L:7100)

**핵심**: 시계열 예측을 위한 선형 모델, 완전 연결 신경망(DNN) 구현, 배치 정규화, dropout을 다룬다.

**키워드**: `linear model`, `DNN`, `batch normalization`, `dropout`, `regularization`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 14 (L:7100)
딥러닝 시계열 예측의 첫 단계로 Keras 선형 모델과 완전 연결 신경망을 구현한다. 배치 정규화와 dropout으로 일반화 성능을 개선하는 방법을 설명하고 통계 기준선과 성능을 비교한다.

### Ch 15: Remembering the past with LSTM (L:7530)

**핵심**: RNN과 LSTM 아키텍처, LSTM 단일/다단계 예측 구현, 양방향 LSTM을 다룬다.

**키워드**: `LSTM`, `RNN`, `long-term dependencies`, `multi-step LSTM`, `bidirectional`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 15 (L:7530)
LSTM의 셀 상태와 게이트 메커니즘이 장기 의존성 학습을 가능하게 하는 원리를 설명한다. 단일 단계와 다단계 LSTM 예측을 각각 구현하고 성능을 비교한다. 양방향 LSTM의 개념과 구현도 포함한다.

### Ch 16: Filtering a time series with CNN (L:7876)

**핵심**: 1D 합성곱 신경망(CNN)의 시계열 적용, 합성곱 필터의 역할, CNN 단일/다단계 예측 구현을 다룬다.

**키워드**: `CNN`, `1D convolution`, `causal convolution`, `temporal patterns`, `filter`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 16 (L:7876)
CNN은 합성곱 필터로 시계열의 지역적 패턴을 감지한다. 1D 합성곱 레이어를 사용한 시계열 예측 모델을 구현하고 LSTM과 성능을 비교한다. 인과적(causal) 합성곱의 개념과 시계열 예측에서의 중요성을 설명한다.

### Ch 17: Using predictions to make more predictions (L:8231)

**핵심**: 자기회귀 LSTM(ARLSTM), 재귀적 다단계 예측(단일 단계 모델을 반복 적용), 구현과 성능 분석을 다룬다.

**키워드**: `autoregressive LSTM`, `ARLSTM`, `recursive multi-step`, `prediction as input`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 17 (L:8231)
재귀적 다단계 예측은 단일 단계 모델의 출력을 다음 입력으로 사용하는 전략이다. ARLSTM 아키텍처를 구현하고 직접 다단계 예측(direct multi-step)과 비교하여 각 접근의 오차 누적 특성을 분석한다.

### Ch 18: Capstone: Forecasting electric power consumption (L:8478)

**핵심**: 가정용 전력 소비 예측 캡스톤 프로젝트. 딥러닝 전체 파이프라인(데이터 전처리, 특성 엔지니어링, 모델링, 평가)을 수행한다.

**키워드**: `capstone`, `power consumption`, `feature engineering`, `LSTM`, `CNN`, `deep learning pipeline`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 18 (L:8478)
대규모 전력 소비 데이터셋에 Ch 12-17에서 학습한 딥러닝 방법을 종합 적용한다. 시계열 데이터 전처리, 특성 엔지니어링, 여러 딥러닝 아키텍처(선형, DNN, LSTM, CNN, ARLSTM)를 비교 평가하는 완전한 실무 파이프라인을 구현한다.

### Ch 19: Automating time series forecasting with Prophet (L:9432)

**핵심**: Facebook Prophet의 자동화 예측, 트렌드/계절성/휴일 컴포넌트, 고급 기능(추가 회귀변수, 교차검증), 강건한 예측 프로세스 구축을 다룬다.

**키워드**: `Prophet`, `automated forecasting`, `trend changepoints`, `seasonality`, `holiday`, `cross-validation`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 19 (L:9432)
Prophet은 분해 기반 자동화 예측 라이브러리로 비전문가도 사용하기 쉽다. 트렌드 변화점(changepoint), 푸리에 급수 기반 계절성, 휴일 효과를 포함한 모델을 구축하고, Prophet의 내장 교차검증 도구로 예측 성능을 평가한다. 추가 회귀변수 통합과 하이퍼파라미터 튜닝도 다룬다.

### Ch 20: Capstone: Forecasting steak prices in Canada (L:10060)

**핵심**: 캐나다 스테이크 월별 평균 소매 가격 예측 캡스톤. Prophet을 활용한 자동화 예측 파이프라인을 구축한다.

**키워드**: `capstone`, `steak prices`, `Prophet`, `Canada`, `retail price`, `automated pipeline`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 20 (L:10060)
Part 4의 자동화 예측 방법을 실제 소매 가격 데이터에 적용한다. 데이터 탐색, Prophet 모델 구축, 교차검증 기반 평가, 예측 생성 전체 과정을 수행하며 자동화 예측 파이프라인의 실무 구현 방법을 보인다.

### Ch 21: Going above and beyond (L:10560)

**핵심**: 책에서 다루지 않은 고급 주제(N-BEATS, Temporal Fusion Transformer, 확률적 예측, 글로벌 모델)와 추가 학습 자료를 안내한다.

**키워드**: `N-BEATS`, `TFT`, `Temporal Fusion Transformer`, `probabilistic forecasting`, `global models`, `next steps`

**상세**: → `Peixeiro-TSForecasting_full.md` Ch 21 (L:10560)
책의 결론부로, 더 발전된 방향을 소개한다. N-BEATS(순수 딥러닝 예측), Temporal Fusion Transformer(주의 메커니즘 기반), 확률적 예측(베이지안 접근), 글로벌 모델(다중 시계열 동시 학습) 등 최신 방법론의 개념과 참고 자료를 제시한다.
