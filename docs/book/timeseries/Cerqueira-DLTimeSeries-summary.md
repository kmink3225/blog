---
name: "Deep Learning for Time Series Data Cookbook"
type: book-summary
authors: "Vitor Cerqueira, Luís Roque"
year: 2024
publisher: Packt
total_pages: 310
language: en
keywords: [deep-learning, time-series, PyTorch, Python, forecasting, classification, anomaly-detection, LSTM, Transformer, TCN]
sources:
  - file: "Cerqueira-DLTimeSeries_full.md"
    tool: "marker (PDF → MD)"
  - file: "Cerqueira-DLTimeSeries-images.md"
    tool: "marker (48 figures)"
---

# Deep Learning for Time Series Data Cookbook — Summary

> Vitor Cerqueira, Luís Roque (2024), Packt, ~310 pages, 9 chapters
> 레시피 기반(cookbook) 형식으로 시계열 딥러닝을 체계적으로 다룬다. PyTorch/PyTorch Lightning을 주요 프레임워크로 사용하며 단변량 예측부터 분류, 이상 탐지까지 실전 레시피를 제공한다.

## Contents

- Ch 1: Getting Started with Time Series (L:453)
- Ch 2: Getting Started with PyTorch (L:1140)
- Ch 3: Univariate Time Series Forecasting (L:1676)
- Ch 4: Forecasting with PyTorch Lightning (L:3079)
- Ch 5: Global Forecasting Models (L:4012)
- Ch 6: Advanced Deep Learning Architectures for Time Series Forecasting (L:4871)
- Ch 7: Probabilistic Time Series Forecasting (L:5792)
- Ch 8: Deep Learning for Time Series Classification (L:6716)
- Ch 9: Deep Learning for Time Series Anomaly Detection (L:7409)

---

## Chapter Summaries

### Ch 1: Getting Started with Time Series (L:453)

**핵심**: pandas를 활용한 시계열 로딩/시각화/리샘플링, 결측값 처리, 분해, 자기상관 계산, 정상성 검정, 이분산성 처리, 다변량 시계열 탐색의 기초 레시피를 다룬다.

**키워드**: `pandas`, `time series loading`, `visualization`, `resampling`, `missing values`, `decomposition`, `ACF`, `stationarity`, `heteroskedasticity`, `multivariate`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 1 (L:453)
cookbook 형식의 첫 챕터로 시계열 기초 조작을 pandas 레시피로 제공한다. 시계열 로딩, 시각화, 리샘플링(업/다운샘플링), 결측값 처리(보간, 전진 채우기), 분해(가산/승산 모델), ACF 계산, ADF·KPSS를 활용한 정상성 검정, ARCH 효과 검정을 통한 이분산성 탐지를 다룬다. 다변량 시계열의 로딩, 시각화, 리샘플링, 변수 간 상관 분석도 포함한다.

### Ch 2: Getting Started with PyTorch (L:1140)

**핵심**: PyTorch 설치, 텐서 기초 연산, 고급 연산(자동 미분), 간단한 신경망 구축, 피드포워드 신경망 훈련, RNN 훈련, LSTM 훈련, CNN 훈련의 레시피를 다룬다.

**키워드**: `PyTorch`, `tensor`, `autograd`, `feedforward`, `RNN`, `LSTM`, `CNN`, `training loop`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 2 (L:1140)
시계열 딥러닝에 사용할 PyTorch 기초를 다진다. 텐서 생성과 연산, 자동 미분(autograd) 메커니즘, 신경망 모듈(`nn.Module`) 구조를 설명한다. 피드포워드, RNN, LSTM, CNN 각각의 간단한 네트워크를 구축하고 훈련 루프(loss 계산, 역전파, 옵티마이저 업데이트)를 완전히 구현하는 방법을 레시피로 제공한다.

### Ch 3: Univariate Time Series Forecasting (L:1676)

**핵심**: 단변량 예측 기준선 모델, ARIMA, 지도 학습 준비(supervised learning 변환), 피드포워드 신경망, LSTM, 계절성 처리(seasonal dummies, Fourier series) 레시피를 다룬다.

**키워드**: `univariate forecasting`, `ARIMA`, `supervised learning conversion`, `feedforward`, `LSTM`, `Fourier series`, `seasonal dummies`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 3 (L:1676)
단변량 시계열 예측의 전체 방법론을 단계적 레시피로 제공한다. 단순 기준선 모델부터 시작하여 ARIMA 적합, 시계열을 지도 학습 행렬로 변환하는 방법, 피드포워드 신경망과 LSTM 예측 모델 구현을 다룬다. 계절성 처리를 위한 계절 더미 변수와 Fourier 급수 특성 공학도 포함한다.

### Ch 4: Forecasting with PyTorch Lightning (L:3079)

**핵심**: PyTorch Lightning을 활용한 구조화된 딥러닝 워크플로, TCN(Temporal Convolutional Network), Transformer 기반 예측 모델 구현 레시피를 다룬다.

**키워드**: `PyTorch Lightning`, `TCN`, `Temporal Convolutional Network`, `Transformer`, `training framework`, `callbacks`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 4 (L:3079)
PyTorch Lightning으로 훈련 코드의 구조화와 재사용성을 높이는 방법을 설명한다. LightningModule과 LightningDataModule을 구현하여 시계열 예측 파이프라인을 표준화한다. TCN(확장 인과적 합성곱으로 장기 의존성 포착)과 Transformer 아키텍처(self-attention 기반)를 시계열 예측에 적용하는 레시피를 제공한다.

### Ch 5: Global Forecasting Models (L:4012)

**핵심**: 여러 시계열을 하나의 모델로 학습하는 글로벌 예측 모델, 다중 시계열 LSTM, GluonTS 시작, N-BEATS 모델 레시피를 다룬다.

**키워드**: `global forecasting`, `multiple time series`, `LSTM global`, `GluonTS`, `N-BEATS`, `cross-learning`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 5 (L:4012)
글로벌 예측 모델은 여러 시계열을 동시에 학습하여 cross-series 패턴을 포착한다. 다중 시계열 LSTM 구현 방법을 설명하고, GluonTS 라이브러리를 활용한 딥러닝 예측 생태계를 소개한다. 순수 딥러닝 기반 N-BEATS 모델의 아키텍처와 구현도 다룬다.

### Ch 6: Advanced Deep Learning Architectures for Time Series Forecasting (L:4871)

**핵심**: Temporal Fusion Transformer(TFT), DeepAR(확률적 예측), GluonTS 기반 고급 모델 구현 레시피를 다룬다.

**키워드**: `TFT`, `Temporal Fusion Transformer`, `DeepAR`, `probabilistic`, `GluonTS`, `attention mechanism`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 6 (L:4871)
시계열 예측의 최신 아키텍처를 다룬다. TFT는 다변량 시계열의 정적/동적 공변량을 attention 메커니즘으로 통합하는 강력한 모델이다. DeepAR은 LSTM 기반 확률적 예측으로 예측 분포를 직접 출력한다. GluonTS를 활용한 구현 레시피를 제공한다.

### Ch 7: Probabilistic Time Series Forecasting (L:5792)

**핵심**: 확률적 예측의 개념(점 예측 vs. 구간/분포 예측), 예측 구간 생성, conformal prediction, DeepAR 확률 예측 구현 레시피를 다룬다.

**키워드**: `probabilistic forecasting`, `prediction intervals`, `conformal prediction`, `quantile regression`, `DeepAR`, `uncertainty quantification`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 7 (L:5792)
점 예측의 한계와 불확실성 정량화의 중요성을 설명한다. 예측 구간 생성 방법(분위수 회귀, 베이지안 접근, conformal prediction)을 비교하고 각각의 PyTorch 구현을 제공한다. DeepAR을 활용한 완전한 확률적 예측 워크플로를 레시피로 다룬다.

### Ch 8: Deep Learning for Time Series Classification (L:6716)

**핵심**: 시계열 분류 문제 설정, LSTM/CNN/Inception 기반 분류 모델, 클래스 불균형 처리, 모델 평가 레시피를 다룬다.

**키워드**: `time series classification`, `LSTM classifier`, `CNN classifier`, `InceptionTime`, `class imbalance`, `F1-score`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 8 (L:6716)
시계열 분류는 예측과 다른 설정(레이블 할당 문제)으로 PyTorch 분류 아키텍처가 필요하다. LSTM, CNN, InceptionTime 아키텍처를 분류에 적용하는 레시피를 제공한다. 클래스 불균형 처리(가중 손실, 오버샘플링), 정밀도·재현율·F1 기반 평가 방법을 다룬다.

### Ch 9: Deep Learning for Time Series Anomaly Detection (L:7409)

**핵심**: 시계열 이상 탐지 방법(재구성 기반, 예측 기반), Autoencoder, LSTM-AE, 임계값 설정 레시피를 다룬다.

**키워드**: `anomaly detection`, `autoencoder`, `LSTM autoencoder`, `reconstruction error`, `threshold`, `unsupervised`

**상세**: → `Cerqueira-DLTimeSeries_full.md` Ch 9 (L:7409)
시계열 이상 탐지는 레이블 없이(비지도) 비정상 패턴을 찾는 문제다. 재구성 기반 방법(Autoencoder, LSTM Autoencoder)은 정상 패턴을 학습한 후 재구성 오차가 큰 구간을 이상으로 탐지한다. 임계값 설정 전략(통계적 방법, 백분위수 기반)과 이상 탐지 평가 방법(precision@k, ROC-AUC)을 다룬다.
