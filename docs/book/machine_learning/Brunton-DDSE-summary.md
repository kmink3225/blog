---
name: Brunton-DDSE
type: book-summary
authors: ["Steven L. Brunton", "J. Nathan Kutz"]
year: 2022
description: "데이터 기반 과학·공학의 핵심 방법론을 다룬다. SVD·DMD·SINDy 등 수학적 기초부터 강화학습·물리 기반 ML까지 포괄한다."
categories: ["machine_learning", "Engineering", "control_systems"]
sources:
  - file: "Brunton-DDSE_marker_full.md"
    tool: Marker
---

# Data-Driven Science and Engineering — Brunton & Kutz (2022)

## 개요

데이터 기반 과학과 공학의 핵심 방법론을 체계적으로 다룬 교재다. SVD·Fourier 변환·압축 센싱 등 수학적 기초에서 출발하여, 동역학 시스템 식별(SINDy, DMD), 선형 제어 이론, 강화학습, 축소차수 모델(ROM), 물리 기반 머신러닝까지 광범위한 주제를 포괄한다. 각 방법론은 MATLAB·Python·R 코드 예제와 함께 제시되어 실용성을 강조한다. 이 책 전반에서 반복되는 핵심 원리는 복잡한 고차원 데이터가 실제로는 저차원 구조를 가진다는 관찰이며, 이를 활용해 효율적인 표현·예측·제어를 달성하는 것이 전체 서사를 관통한다.

## 챕터별 요약

### Ch 1. Singular Value Decomposition (SVD)
**핵심**: SVD는 임의의 행렬에 대해 반드시 존재하는 유일한 분해이며, 고차원 데이터의 최적 저차원 근사를 계층적으로 제공한다.
**키워드**: SVD, PCA, dimensionality reduction, matrix approximation, Eckart-Young theorem, pseudo-inverse
**상세**: → `Brunton-DDSE_marker_full.md` Ch 1 (L:652)

SVD는 계산 시대의 가장 중요한 행렬 분해 중 하나로, 이 책 전체 방법론의 수학적 기초를 이룬다. 임의의 복소 행렬 X를 X = UΣV* 형태로 분해하며, U와 V는 유니터리 행렬이고 Σ는 특이값을 내림차순으로 배열한 대각 행렬이다. 복잡한 시스템에서 수집한 데이터는 일반적으로 저차원 구조를 가지며, SVD는 이 지배적인 패턴을 데이터로부터 순수하게 추출하는 데이터 기반 방법이다. Eckart-Young 정리에 따르면, 상위 r개의 특이값과 벡터만 남긴 절단 SVD는 주어진 계수 r에서 ℓ₂ 의미의 최적 저차원 근사를 제공한다. 이미지·유체 시뮬레이션·신경 신호 등 다양한 응용에서 단 소수의 모드만으로 데이터를 효과적으로 표현할 수 있다. Economy SVD는 계산 효율을 높이며, n >> m인 tall-skinny 행렬에서 자주 사용된다. PCA는 SVD 알고리즘으로 구현되며, Karhunen-Loeve 변환·경험적 직교 함수(EOF)·고유직교분해(POD) 등과 수학적으로 동등하다. SVD는 비정방 행렬의 의사역행렬 계산에도 활용되어 과결정·미결정 선형 시스템의 해를 제공한다. 랜덤화 수치 알고리즘을 활용한 대규모 SVD 계산법도 별도 절에서 다룬다. 계수 r의 선택 기준으로는 특이값의 급격한 감쇠 지점(elbow method), 정보량 기반 기준(AIC/BIC), 에너지 비율 등이 논의된다. SVD는 이후 챕터의 DMD, POD, 균형 모델 축소 등 모든 방법론의 핵심 계산 도구로 반복 등장한다.

---

### Ch 2. Fourier and Wavelet Transforms
**핵심**: 푸리에 변환은 함수를 주파수 공간의 직교 기저로 변환하며, 신호 압축·미분방정식 수치 해석·필터링의 핵심 도구다. 웨이블릿은 시간-주파수 국소화가 필요한 경우에 보완적으로 사용된다.
**키워드**: Fourier series, FFT, DFT, wavelet, inner product, Hilbert space, spectral methods
**상세**: → `Brunton-DDSE_marker_full.md` Ch 2 (L:2147)

푸리에의 연구는 힐베르트 공간 이론과 근대 계산 수학의 기초를 제공했으며, 고속 푸리에 변환(FFT)은 지난 세기 가장 영향력 있는 알고리즘으로 꼽힌다. 이 챕터는 함수 내적의 개념에서 출발하여 L²([a,b]) 공간에서의 함수 표현 이론을 전개한다. 푸리에 급수는 주기 함수를 증가하는 주파수의 사인·코사인 함수의 직교 기저로 전개하는 것으로, 벡터 내적의 무한 차원 유사체로 이해할 수 있다. 연속 푸리에 변환은 비주기 함수로 확장되며, 주파수 도메인에서의 미분·적분은 단순한 대수 연산으로 바뀌어 PDE의 수치 해석을 크게 단순화한다. 이산 푸리에 변환(DFT)과 FFT는 데이터 벡터에 대한 계산으로 구현되며, O(n log n) 복잡도로 신호 처리·이미지 압축·수치 해석의 핵심 도구가 된다. 함수의 평활도와 푸리에 계수의 감쇠 속도 사이의 관계는 압축 효율과 직결된다. 웨이블릿은 시간-주파수 국소화가 가능한 기저 함수로, 에지(edge)가 풍부한 이미지나 순간적인 이벤트가 있는 신호에서 순수 푸리에 기저보다 더 희소한 표현을 제공한다. 이 챕터의 방법들은 3챕터 압축 센싱에서 희소 기저로, 12챕터 ROM에서 공간 기저로 계속 활용된다.

---

### Ch 3. Sparsity and Compressed Sensing
**핵심**: 자연 신호는 적절한 기저에서 희소 표현을 가지며, 압축 센싱은 이 희소성을 이용해 전통적 샘플링 이론의 한계를 넘어 소수의 랜덤 측정만으로 전체 신호를 복원한다.
**키워드**: sparsity, compressed sensing, ℓ₁ minimization, RIP, basis pursuit, LASSO, incoherence
**상세**: → `Brunton-DDSE_marker_full.md` Ch 3 (L:3566)

자연 신호의 압축 가능성(compressibility)은 신호가 푸리에·웨이블릿 등의 기저에서 희소 표현을 가진다는 사실에 기반한다. JPEG 이미지 압축과 MP3 오디오 압축이 이 원리의 대표적 응용이다. 압축 센싱은 이 패러다임을 뒤집어, 고차원 신호를 먼저 수집한 뒤 압축하는 대신 처음부터 소수의 압축된 측정만을 수집하여 희소 신호를 복원한다. 신호 x가 K-희소하다면, ℓ₀ 최소화는 조합론적으로 NP-hard 문제이지만, 측정 행렬 C가 제한 등장성 조건(RIP)을 만족하면 ℓ₁ 볼록 최소화로 동일한 희소 해를 높은 확률로 복원할 수 있다. 필요한 측정 수는 O(K log(n/K))로 신호 차원 n에 비해 훨씬 적다. 측정 행렬 C가 희소화 기저 Ψ에 대해 비일관성(incoherence)을 가져야 한다는 조건은 가우스·베르누이 랜덤 행렬이 잘 만족한다. ℓ₁ 최소화가 ℓ₂ 최소화와 달리 희소 해를 선택하는 기하학적 직관도 제시된다. 희소 최적화는 이상치 데이터에 강건하며 해석 가능한 간결한 모델을 선호하는 Occam의 면도날 원리와도 연결된다. 이 챕터에서 다룬 희소 회귀는 4챕터 LASSO, 7챕터 SINDy 동역학 식별의 핵심 도구로 이어진다.

---

### Ch 4. Regression and Model Selection
**핵심**: 머신러닝의 핵심은 최적화이며, 정칙화(regularization)의 선택이 모델의 복잡도와 해석 가능성을 결정한다. 교차검증은 과적합·과소적합을 평가하는 필수 도구다.
**키워드**: regression, least squares, LASSO, ridge regression, cross-validation, regularization, AIC, BIC, model selection
**상세**: → `Brunton-DDSE_marker_full.md` Ch 4 (L:4425)

회귀와 모델 선택은 데이터로부터 간결하고 해석 가능한 모델을 구축하는 머신러닝의 핵심이다. 고전적 최소제곱 적합은 Ax = b의 해로 정식화되며, 과결정·미결정 시스템에서는 정칙화가 필요하다. ℓ₂ 정칙화(릿지 회귀)는 작은 계수를 균일하게 축소하는 반면, ℓ₁ 정칙화(LASSO)는 계수를 정확히 0으로 만들어 자동 변수 선택 기능을 제공한다. ℓ∞ 오차, ℓ₁ 오차, ℓ₂ 오차의 비교에서 ℓ∞는 이상치에 민감하고 ℓ₁은 이상치에 강건함을 보인다. 손실 함수 f(·)와 정칙화 g(·)의 선택은 계산 가능성과 해의 특성을 동시에 결정하며, 이 이분법적 구조는 딥러닝 목적 함수와도 동일하다. 모델의 복잡도가 증가할수록 훈련 오차는 감소하지만 검증 오차는 U자형 곡선을 그리는 전형적 과적합 현상이 설명된다. 교차검증은 데이터를 훈련·검증·보류 세트로 나누어 모델의 일반화 성능을 평가한다. AIC·BIC 등 정보 기준은 모델 복잡도와 적합도를 동시에 고려하는 모델 선택 지표로 활용된다. 이 챕터의 스파스 회귀 프레임워크는 7챕터 SINDy, 9챕터 시스템 식별, 14챕터 물리 기반 ML에서 반복 적용된다.

---

### Ch 5. Clustering and Classification
**핵심**: 머신러닝의 목표는 데이터의 내재적 저차원 특징 공간을 구축·활용하는 것이며, 감독 학습(SVM, 결정 트리)과 비감독 학습(k-means, GMM)이 상호 보완적으로 사용된다.
**키워드**: supervised learning, unsupervised learning, SVM, k-means, GMM, LDA, feature engineering, PCA, eigenfaces
**상세**: → `Brunton-DDSE_marker_full.md` Ch 5 (L:5259)

머신러닝은 최적화 기반의 데이터 분석 방법론으로, 진단·예측·제어에 활용 가능한 데이터의 지배적 특징을 추출하는 것이 핵심이다. 감독 학습은 레이블된 데이터를 이용해 입출력 관계를 학습하고, 비감독 학습은 레이블 없이 데이터의 패턴을 발견한다. SVD/PCA를 이용한 고유얼굴(eigenfaces) 분해는 고차원 얼굴 이미지를 소수의 특징 벡터로 표현하는 대표적 특징 공학 사례다. 개·고양이 이미지 분류 예제에서 SVD 모드의 로딩 분포를 통해 어떤 특징이 분류에 유용한지 시각화한다. 웨이블릿 변환 이미지는 원시 픽셀 이미지보다 클래스 분리도가 높아 분류 성능을 향상시킨다. 선형 판별 분석(LDA)은 클래스 내 분산을 최소화하고 클래스 간 분산을 최대화하는 투영을 찾아 Fisher 아이리스 데이터 같은 예제에서 뛰어난 분리도를 보인다. SVM은 마진 최대화 원리로 분류 경계를 결정하며, 커널 트릭을 통해 비선형 분류를 선형 문제로 변환한다. k-means 클러스터링은 데이터를 k개의 군집으로 비감독 분류하며 군집 중심을 반복 갱신한다. 가우스 혼합 모델(GMM)은 확률적 클러스터링 프레임워크로 소프트 클러스터 배정이 가능하다.

---

### Ch 6. Neural Networks and Deep Learning
**핵심**: 신경망은 비선형 활성화 함수를 가진 다층 합성 함수로, 범용 함수 근사기(universal approximator)이며 역전파와 확률적 경사하강법으로 훈련된다.
**키워드**: neural networks, deep learning, backpropagation, CNN, autoencoder, activation function, dropout, transfer learning
**상세**: → `Brunton-DDSE_marker_full.md` Ch 6 (L:6230)

신경망은 Hubel과 Wiesel의 일차 시각 피질 연구에서 영감을 얻었으며, 2012년 ImageNet 데이터셋에서의 성과를 계기로 딥러닝 혁명이 시작됐다. 단층 신경망은 Ax = b 형태의 선형 시스템으로, 의사역행렬이나 LASSO로 최적 가중치를 구할 수 있다. 비선형 활성화 함수(로지스틱, tanh, ReLU)를 도입한 다층 구조는 훨씬 풍부한 함수 공간을 표현하며, 다층 피드포워드 망은 충분한 폭과 깊이에서 범용 함수 근사기임이 증명되었다. 일반화된 딥러닝 최적화 문제는 argmin f_θ(x) 형태로 표현되며, 계층 가중치 θ를 역전파와 확률적 경사하강으로 최적화한다. 과적합 방지를 위해 드롭아웃·배치 정규화·데이터 증강·사전훈련 등의 기법이 도입된다. 합성곱 신경망(CNN)은 이미지 처리에, 순환 신경망(RNN/LSTM)은 시계열에 특화된 구조다. 오토인코더는 입력을 저차원 잠재 공간으로 압축하고 재구성하며, 비선형 차원 축소·이상 탐지·물리 좌표 발견에 사용된다. 교차검증을 반드시 적용해야 한다는 원칙이 강조된다. 이 챕터의 신경망 아키텍처는 6·14챕터에서 SINDy 오토인코더와 Koopman 예측 등 물리 기반 응용으로 이어진다.

---

### Ch 7. Data-Driven Dynamical Systems
**핵심**: 데이터 기반 동역학 시스템은 동적 모드 분해(DMD)로 선형 스펙트럼 구조를 추출하고, SINDy로 비선형 지배 방정식을 희소 회귀를 통해 식별한다. Koopman 연산자는 비선형 시스템을 선형 프레임워크로 표현하는 이론적 기반을 제공한다.
**키워드**: DMD, SINDy, Koopman operator, Lorenz system, chaotic dynamics, sparse regression, nonlinear dynamics, flow map
**상세**: → `Brunton-DDSE_marker_full.md` Ch 7 (L:7148)

동역학 시스템은 미분방정식이나 반복 사상으로 기술되는 시간 진화 시스템으로, 유체·기후·신경과학·경제 등 광범위한 분야에 적용된다. 선형 시스템은 행렬 A의 스펙트럼 분해(고유값·고유벡터)로 완전히 특성화되며 닫힌 형태의 해가 존재한다. 로렌즈 시스템은 카오스의 대표적 예로, 초기 조건에 민감하게 의존하는 궤적이 복잡한 어트랙터를 형성한다. 동적 모드 분해(DMD)는 시간 스냅샷 데이터로부터 선형 시스템 행렬의 최적 근사를 SVD 기반 회귀로 구하며, 주요 시공간 모드와 그 주파수·성장률을 추출한다. SINDy(Sparse Identification of Nonlinear Dynamics)는 후보 함수 라이브러리에 대한 희소 회귀를 통해 비선형 지배 방정식을 명시적으로 식별한다. Koopman 연산자는 비선형 시스템의 비선형 관측 함수를 선형적으로 진화시키는 무한차원 선형 연산자로, 데이터 기반 Koopman 근사는 비선형 시스템을 선형 프레임워크로 분석할 가능성을 제공한다. 연속 시간과 이산 시간 시스템 모두 통일된 프레임워크 내에서 다루어진다. 이 챕터의 DMD와 SINDy는 9·10챕터의 제어 지향 시스템 식별, 14챕터의 물리 기반 ML에서 핵심 도구로 재활용된다.

---

### Ch 8. Linear Control Theory
**핵심**: 선형 시스템에 대한 피드백 제어는 가관측성과 가제어성에 기반하며, LQR 최적 제어와 Kalman 필터를 결합한 LQG 구조가 노이즈가 있는 실제 시스템의 표준 제어 아키텍처다.
**키워드**: feedback control, LTI system, LQR, Kalman filter, PID, controllability, observability, transfer function, stability
**상세**: → `Brunton-DDSE_marker_full.md` Ch 8 (L:8627)

제어 이론은 동역학 시스템의 거동을 능동적으로 조작하는 응용 수학의 핵심 분야로, 크루즈 컨트롤·자동조종장치·산업 자동화 등 현대 기술 전반에 적용된다. 수동 제어·개루프 제어·피드포워드 제어·폐루프 피드백 제어의 유형이 비교되며, 불안정 시스템 안정화·외란 보상·모델 불확실성 극복 등 피드백의 핵심 이점이 강조된다. 선형 시불변(LTI) 시스템 x' = Ax + Bu, y = Cx + Du는 제어 이론의 표준 표현이며, 비선형 시스템의 고정점 주변 선형화로 얻어진다. 가제어성과 가관측성은 시스템의 상태를 원하는 대로 구동하거나 측정으로 추정할 수 있는지를 판별한다. LQR(선형 이차 조절기)은 상태 오차와 제어 비용을 동시에 최소화하는 최적 상태 피드백 제어기로, 리카티 방정식의 해로 구한다. Kalman 필터는 측정과 모델을 결합해 상태를 최적으로 추정하는 동적 옵저버로, 프로세스 노이즈와 측정 노이즈 모두를 고려한다. LQR과 Kalman 필터를 결합한 LQG 제어기는 분리 원리에 의해 독립적으로 설계 가능하다. 전달 함수와 주파수 응답(H₂, H∞ 노름) 분석이 강건성 평가에 사용된다.

---

### Ch 9. Balanced Models for Control
**핵심**: 균형 모델 축소는 가제어성과 가관측성을 동시에 고려하는 좌표 변환으로 입출력 에너지 관점에서 최적의 저차원 모델을 제공하며, ERA/OKID 알고리즘으로 데이터에서 직접 도출할 수 있다.
**키워드**: balanced truncation, balanced POD, ERA, OKID, Gramian, model reduction, system identification, Hankel matrix
**상세**: → `Brunton-DDSE_marker_full.md` Ch 9 (L:10030)

고차원 시스템(예: 유체 시뮬레이션)의 실시간 피드백 제어를 위해서는 입출력 특성을 충실히 보존하는 저차 모델이 필수적이다. POD 기반 ROM이 에너지 기준으로 모드를 정렬하는 반면, 균형 모델 축소는 가제어성과 가관측성 Gramian을 동등하게 대각화하는 좌표 변환을 통해 입출력 에너지 관점의 계층적 모드 분해를 제공한다. 가제어성 Gramian W_c는 입력에서 상태로의 에너지 전달을, 가관측성 Gramian W_o는 상태에서 출력으로의 에너지 전달을 정량화한다. 균형 변환 행렬 T는 SVD를 통해 W_c와 W_o의 곱에서 도출되며, 결과적으로 두 Gramian이 동일한 대각 행렬(균형 특이값)로 표현된다. 균형 특이값이 작은 상태는 가제어성과 가관측성이 모두 낮아 입출력에 거의 기여하지 않으므로 안전하게 절단된다. 실제 고차원 시스템에서는 스냅샷 기반 균형 POD(BPOD)가 효율적인 계산 수단을 제공한다. ERA(고유시스템 실현 알고리즘)와 OKID(옵저버 Kalman 필터 식별)는 임펄스 응답 데이터 혹은 입출력 데이터로부터 균형 모델을 직접 식별하는 시스템 식별 기법이다. H∞ 노름으로 원본 시스템과 축소 모델 사이의 근사 오차를 정량화한다.

---

### Ch 10. Data-Driven Control
**핵심**: 모델이 없거나 강한 비선형성을 가진 시스템에는 모델 예측 제어(MPC)·유전 알고리즘·SINDy/DMD 기반 비선형 시스템 식별 등의 데이터 기반 제어 전략이 사용된다.
**키워드**: MPC, model predictive control, DMDc, SINDy with control, genetic programming, Koopman control, system identification, extremum seeking
**상세**: → `Brunton-DDSE_marker_full.md` Ch 10 (L:10869)

데이터 기반 제어는 원리적 모델이 없는 복잡한 비선형 시스템(신경과학·난류·전염병·금융)의 제어를 위해 머신러닝을 활용한다. 모델 예측 제어(MPC)는 후퇴 수평선에서 서로게이트 모델을 이용해 예측·최적화를 반복 수행하며, 비선형 시스템의 제약과 불확실성을 명시적으로 처리한다. DMD with Control(DMDc)은 제어 입력과 상태 데이터를 동시에 활용해 내부 동역학과 외부 제어 효과를 분리하는 선형 모델을 식별한다. SINDy with Control은 비선형 지배 방정식에 제어 입력 항을 포함시켜 완전 비선형 시스템의 MPC 적용을 가능하게 한다. Koopman 제어는 비선형 시스템을 선형적으로 진화하는 측정 함수 공간으로 변환해 표준 선형 제어 이론을 적용한다. 유전 알고리즘은 제어 법칙을 기호 표현식으로 직접 탐색·최적화하는 구배 불필요 방법이다. 극값 추종 제어는 시스템의 섭동 응답을 분석하여 비용 함수의 최적점을 향해 제어 신호를 적응적으로 조정한다. 딥 MPC, 튜브 MPC, 미분 가능 예측 제어 등 최신 확장도 간략히 소개된다.

---

### Ch 11. Reinforcement Learning
**핵심**: 강화학습은 에이전트가 환경과의 시행착오 상호작용을 통해 누적 보상을 최대화하는 정책을 학습하며, 마르코프 결정 과정(MDP)과 벨만 방정식이 수학적 기초를 이룬다.
**키워드**: reinforcement learning, MDP, Q-learning, policy gradient, value function, Bellman equation, deep RL, exploration-exploitation
**상세**: → `Brunton-DDSE_marker_full.md` Ch 11 (L:11481)

강화학습은 제어 이론과 머신러닝의 교차점에 위치하며, 범용 인공지능과 자율성의 가장 유망한 연구 분야로 평가된다. RL 에이전트는 상태 s에서 행동 a를 선택하는 정책 π를 학습하여 할인 누적 보상 V(s) = E(Σγᵏrₖ)를 최대화한다. 마르코프 결정 과정(MDP)은 현재 상태만이 미래 상태를 결정한다는 마르코프 성질을 가지는 확률적 프레임워크로, 체스·바둑 등 게임과 연속 제어 시스템 모두를 포괄한다. 벨만 방정식 V(s) = max_π E(r₀ + γV(s'))는 가치 함수의 재귀적 구조를 표현하며 현대 RL 알고리즘의 핵심 결과다. 정책 반복과 가치 반복은 알려진 MDP 모델이 있을 때의 동적 프로그래밍 기반 해법이며, Q-학습은 환경 모델 없이 행동-가치 함수를 직접 추정한다. 탐색(exploration)과 활용(exploitation)의 균형, 신용 배정 문제, 희소하고 지연된 보상의 어려움이 RL의 핵심 도전으로 논의된다. 심층 강화학습은 신경망으로 정책·가치 함수·Q 함수를 근사하여 고차원 연속 상태·행동 공간으로 확장한다. RL은 보드 게임 마스터링에서 자율 주행·유체 제어까지 광범위한 응용을 갖는다.

---

### Ch 12. Reduced-Order Models (ROMs)
**핵심**: 고유직교분해(POD)는 SVD를 PDE에 적용한 데이터 기반 차원 축소로, Galerkin 투영과 결합하여 수백만 자유도의 PDE를 소수 모드의 저차원 ODE로 대체한다.
**키워드**: POD, Galerkin projection, ROM, eigenfunction expansion, Fourier modes, PDE, snapshot method, energy truncation
**상세**: → `Brunton-DDSE_marker_full.md` Ch 12 (L:12197)

편미분방정식(PDE)은 유체역학·구조역학·대기과학·신경과학 등 다양한 물리 시스템의 지배 방정식이지만, 수치 해석을 위한 공간 이산화로 수백만~수십억 자유도의 고차원 시스템이 생성된다. 이 인공적인 고차원성을 제거하기 위해 POD는 수치 시뮬레이션이나 실험 데이터의 스냅샷 행렬에 SVD를 적용해 에너지를 기준으로 정렬된 최적 기저 모드를 추출한다. Galerkin 투영은 PDE를 이 POD 모드로 투영하여 저차원 ODE 시스템(축소차수 모델, ROM)을 생성한다. 푸리에 모드 확장은 O(n log n)의 FFT 덕분에 광범위하게 사용되지만, 국소화된 함수 표현에 많은 모드가 필요하다. Sturm-Liouville 특수 함수(베셀·라게르·에르미트·르장드르)는 특정 물리 문제에 최적화된 기저로, Gauss-Hermite 함수는 양자 조화 진동자의 고유함수로 대표적 예다. POD 모드의 절단 수 r 선택은 특이값의 상대적 에너지 비율로 결정되며, 비선형 모드 혼합이 Galerkin 투영 ODE에서 핵심 과제다. ROM은 Monte Carlo 시뮬레이션·매개변수 최적화·실시간 제어처럼 PDE를 수천 번 반복 평가해야 하는 응용에서 계산 가능성을 제공한다.

---

### Ch 13. Interpolation for Parametric Reduced-Order Models
**핵심**: 비선형 ROMs에서 계산 복잡도의 병목은 비선형 항의 평가이며, Gappy POD와 DEIM은 희소 샘플링을 통해 비선형 항을 효율적으로 근사하는 보간 기법이다.
**키워드**: gappy POD, DEIM, sparse sensing, interpolation, condition number, sensor placement, nonlinear ROM, EIM
**상세**: → `Brunton-DDSE_marker_full.md` Ch 13 (L:13099)

POD-Galerkin ROM의 근본적 계산 병목은 비선형 항의 내적 계산으로, 매 시간 단계마다 고차원 전체 상태에서 평가가 필요해 ROM의 계산 이점을 무력화한다. Gappy POD는 Everson과 Sirovich가 제안한 방법으로, 전체 상태의 소수 위치(r << n)에서만 측정을 수행해 비선형 항을 근사하는 최소제곱 문제를 해결한다. 측정 행렬 P는 r개의 공간 측정 위치를 지정하며, 재구성 행렬 M의 조건수 κ(M)가 측정 배치의 품질을 평가하는 핵심 지표다. 조건수가 작을수록 재구성 정확도가 높으며, 조건수는 재구성할 함수를 몰라도 계산 가능해 범용 품질 지표로 사용된다. 랜덤 샘플링에서 동일한 측정 수라도 배치에 따라 조건수가 수 오더(order)나 차이날 수 있음이 통계 실험으로 확인된다. 그리디 알고리즘 기반 DEIM(이산 경험 보간법)은 비선형 ROMs에서 가장 널리 사용되는 방법으로, POD 모드에서 최적 보간 인덱스를 단계적으로 선택해 거의 최적의 ℓ₂ 근사를 달성한다. 최적 센서 배치 문제는 3챕터 압축 센싱의 측정 행렬 설계와 수학적으로 동일한 프레임워크 내에 있다. 이 챕터의 희소 샘플링 기법은 14챕터 물리 기반 ML의 센서 배치 전략으로 직접 연결된다.

---

### Ch 14. Physics-Informed Machine Learning
**핵심**: 물리 지식을 머신러닝 파이프라인의 문제 정식화·데이터·아키텍처·손실 함수·최적화 각 단계에 내재화함으로써 해석 가능하고 일반화 가능한 데이터 기반 모델을 구축한다.
**키워드**: physics-informed ML, SINDy autoencoder, Koopman forecasting, PINN, digital twin, sparse regression, coordinate discovery, parsimony
**상세**: → `Brunton-DDSE_marker_full.md` Ch 14 (L:13838)

물리 기반 머신러닝은 이 책 전반의 방법론을 통합하는 최종 장으로, 데이터 기반 모델의 해석 가능성·일반화·외삽 능력을 향상시키기 위해 사전 물리 지식을 모델에 내재화하는 다양한 전략을 제시한다. 간결성(parsimony)은 아리스토텔레스부터 아인슈타인까지 물리 모델링의 지도 원리였으며, 현대 ML에서도 과적합 방지와 일반화를 위해 핵심 원칙으로 작동한다. SINDy 오토인코더는 오토인코더로 발견한 내재 좌표 z에서 SINDy가 간결한 동역학을 식별하도록 동시 최적화하며, 진자 비디오에서 각도·각속도를 자동 발견하는 예제로 시연된다. Koopman 예측 프레임워크는 신경망으로 시계열 데이터를 가능한 한 정현파에 가깝게 변환하는 시간 왜핑(time warping)을 학습하여 FFT의 한계를 극복하는 장기 예측 도구를 제공한다. 물리 정보 신경망(PINN)은 손실 함수에 지배 방정식의 잔차를 포함시켜 PDE 제약을 만족하는 해를 학습한다. 디지털 트윈은 물리 모델과 Kalman 필터링을 결합해 온라인 데이터로 지속 갱신되는 가상 모델을 구현한다. 다중 스케일·부분 관측·잡음이 있는 데이터 환경에서의 모델 식별은 여전히 미해결 수학적 과제로 제시된다.

---

## Marker 세부 목차

> `L:숫자`는 `Brunton-DDSE_marker_full.md`의 라인 번호.

- Ch 1 Singular Value Decomposition `L:652`
- Ch 2 Fourier and Wavelet Transforms `L:2147`
- Ch 3 Sparsity and Compressed Sensing `L:3566`
- Ch 4 Regression and Model Selection `L:4425`
- Ch 5 Clustering and Classification `L:5259`
- Ch 6 Neural Networks and Deep Learning `L:6230`
- Ch 7 Data-Driven Dynamical Systems `L:7148`
- Ch 8 Linear Control Theory `L:8627`
- Ch 9 Balanced Models for Control `L:10030`
- Ch 10 Data-Driven Control `L:10869`
- Ch 11 Reinforcement Learning `L:11481`
- Ch 12 Reduced-Order Models (ROMs) `L:12197`
- Ch 13 Interpolation for Parametric ROMs `L:13099`
- Ch 14 Physics-Informed Machine Learning `L:13838`
