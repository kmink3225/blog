---
name: Ljung-SystemID
type: book-summary
authors: ["Lennart Ljung"]
year: 1999
description: "시스템 식별의 이론과 실용적 응용을 다룬 고전 교재. 모델 구조 선택부터 파라미터 추정·검증까지 체계적으로 설명한다."
categories: ["timeseries", "Engineering", "Statistics"]
sources:
  - file: "Ljung-SystemID_marker_full.md"
    tool: Marker
---

# System Identification: Theory for the User — Ljung (1999, 2nd ed.)

## 개요

시스템 식별(System Identification) 분야의 표준 교재다. 관측 데이터로부터 동적 시스템의 수학적 모델을 구성하는 방법론 전반을 다룬다. 선형 시불변 시스템의 이론적 기초부터 비선형·시변 모델, 파라미터 추정의 수렴·일관성·점근 분포 분석, 수치 계산, 재귀 추정, 실험 설계, 데이터 전처리, 모델 선택·검증에 이르기까지 17개 챕터에 걸쳐 체계적으로 서술한다. 이론 결과를 실제 적용으로 연결하는 실용적 관점이 특징이며, MATLAB System Identification Toolbox와의 연계도 다룬다.

## 챕터별 요약

### Ch 1. Introduction
**핵심**: 시스템 식별의 동기와 범위를 소개하고, ARX 모델과 최소제곱법을 원형 문제로 제시한다.
**키워드**: system identification, dynamic systems, ARX, least squares, model types
**상세**: → `Ljung-SystemID_marker_full.md` Ch 1 (L:562)

동적 시스템은 현재 출력이 과거 입출력에 의존하는 시스템이며, 시스템 식별은 관측 데이터로부터 이러한 시스템의 수학적 모델을 구성하는 분야다. 시스템의 입력(manipulable signal), 출력(observable signal), 교란(disturbance)을 구분하고, 각각이 모델링에서 어떤 역할을 하는지 태양열 난방 주택, 군용 항공기, 음성 신호 등 다양한 예시로 설명한다. 모델의 종류를 정신적 모델, 그래픽 모델, 수학적 모델, 소프트웨어 모델로 분류하고, 물리 기반 모델링과 데이터 기반 시스템 식별의 차이를 명확히 한다. "진실한 시스템"이라는 개념은 수학적 픽션임을 명시하며, 실용성이 진리보다 중요하다는 관점을 제시한다. ARX 모델을 원형 문제로 소개하는데, 선형 차분방정식 $y(t) + a_1 y(t-1) + \dots = b_1 u(t-1) + \dots$로 입출력 관계를 기술한다. 파라미터 벡터 $\theta$와 회귀 벡터 $\varphi(t)$를 도입하여 $\hat{y}(t|\theta) = \varphi^T(t)\theta$로 표현하고, 최소제곱 기준 $V_N(\theta, Z^N) = \frac{1}{N}\sum_{t=1}^N (y(t) - \varphi^T(t)\theta)^2$를 최소화하여 추정치 $\hat{\theta}_N$을 구하는 과정을 보인다. 이 닫힌 형태 해가 존재하는 것은 예측 오차가 파라미터에 대해 선형이기 때문이다. 책 전체의 구성과 다루는 핵심 주제들을 미리 조망한다.

---

### Ch 2. Time-Invariant Linear Systems
**핵심**: 선형 시불변 시스템의 임펄스 응답, 전달함수, 스펙트럼 이론을 정립한다.
**키워드**: impulse response, transfer function, covariance function, spectrum, white noise, quasi-stationary
**상세**: → `Ljung-SystemID_marker_full.md` Ch 2 (L:914)

선형 시불변(LTI) 시스템은 실제 공학 시스템의 가장 중요한 근사 모델이다. 시스템이 선형, 시불변, 인과적일 때 임펄스 응답 $\{g(\tau)\}$로 완전히 기술되며, 출력은 $y(t) = \sum_{k=1}^\infty g(k)u(t-k)$로 표현된다. 연속 시간 시스템을 이산 시간으로 샘플링하는 과정에서 샘플링 간격 $T$에 따른 이산 임펄스 응답 $g_T(\ell)$을 도출하고, 홀드(ZOH) 근사의 타당성을 논의한다. 교란(disturbance)은 가산 항 $v(t)$로 모델링되며, 측정 노이즈, 비제어 입력, 모델링 오차 등 다양한 원인이 있다. 교란은 백색 잡음 $e(t)$를 필터 $H(q)$에 통과시켜 $v(t) = H(q)e(t) = \sum_{k=0}^\infty h(k)e(t-k)$로 표현하고, 이때 공분산 함수 $R_v(\tau) = \lambda \sum_{k=0}^\infty h(k)h(k-\tau)$가 정의된다. 전달함수 $G(z) = \sum_{k=1}^\infty g(k)z^{-k}$와 주파수 응답, 전력 스펙트럼을 도입한다. 준정상(quasi-stationary) 신호 개념을 정의하고, 입출력 스펙트럼 관계 $\Phi_y(\omega) = |G(e^{i\omega})|^2 \Phi_u(\omega) + \Phi_v(\omega)$를 유도한다. 다변수 시스템으로의 확장도 마지막 절에서 다룬다.

---

### Ch 3. Simulation and Prediction
**핵심**: 시스템 모델의 시뮬레이션 활용과 미래 출력 예측 방법을 체계화한다.
**키워드**: simulation, one-step-ahead prediction, invertibility, predictor, prediction error
**상세**: → `Ljung-SystemID_marker_full.md` Ch 3 (L:2395)

시스템 모델 $y(t) = G(q)u(t) + H(q)e(t)$는 시뮬레이션과 예측이라는 두 가지 핵심 용도로 활용된다. 시뮬레이션은 원하는 입력 시퀀스를 모델에 적용하여 교란이 없는 출력 $y^*(t) = G(q)u^*(t)$와 교란 성분 $v^*(t) = H(q)e^*(t)$를 모두 계산하는 과정이다. 예측은 과거 관측치를 이용하여 미래 출력을 추정하는 문제로, 노이즈 모델 $H(q)$의 역필터 가능성(invertibility)이 핵심 조건이다. 역필터가 존재하려면 $1/H(z)$가 $|z|>1$ 영역에서 해석적이어야 하며, 이는 $H(q)$의 영점이 단위원 내부에 있어야 함을 의미한다. 한 스텝 앞 예측치 $\hat{v}(t|t-1) = \sum_{k=1}^\infty h(k)e(t-k)$는 알려진 과거 출력으로부터 $e(s)$를 역필터로 복원하여 계산한다. 최적 예측치는 조건부 기댓값으로, Gaussian 잡음 가정 하에 이는 최대 사후 확률(MAP) 예측과 동일하다. 일반 시스템 $y(t) = G(q)u(t) + H(q)e(t)$에 대한 한 스텝 예측기는 $\hat{y}(t|t-1) = H^{-1}(q)G(q)u(t) + [1-H^{-1}(q)]y(t)$로 유도되며, 이것이 파라미터 추정의 핵심 도구가 된다. 이 장의 결과는 Ch 7의 예측 오차 추정 방법의 수학적 기반을 제공한다.

---

### Ch 4. Models of Linear Time-Invariant Systems
**핵심**: 선형 시불변 시스템의 다양한 파라미터 모델 구조(ARX, ARMAX, OE, BJ, 상태공간)를 체계화한다.
**키워드**: ARX, ARMAX, OE, BJ, state-space, model structure, identifiability, linear regression
**상세**: → `Ljung-SystemID_marker_full.md` Ch 4 (L:2952)

완전한 선형 시불변 모델은 $y(t) = G(q,\theta)u(t) + H(q,\theta)e(t)$로 기술되며, 유한 차원 파라미터 벡터 $\theta$로 표현하는 것이 실용적이다. 가장 단순한 방정식 오차 모델(ARX)은 $A(q)y(t) = B(q)u(t) + e(t)$로, 예측기가 $\hat{y}(t|\theta) = \varphi^T(t)\theta$로 선형 회귀 형태가 된다는 결정적 장점이 있다. ARMAX 모델은 $A(q)y(t) = B(q)u(t) + C(q)e(t)$로 노이즈 모델에 유연성을 추가하며, 예측기는 의사 선형 회귀(pseudolinear regression) 형태가 된다. Output Error(OE) 모델은 $y(t) = \frac{B(q)}{F(q)}u(t) + e(t)$로 시스템 다이나믹스와 노이즈를 독립적으로 모델링한다. Box-Jenkins(BJ) 모델은 $y(t) = \frac{B(q)}{F(q)}u(t) + \frac{C(q)}{D(q)}e(t)$로 가장 일반적인 형태다. 상태공간 모델은 $x(t+1) = Ax(t)+Bu(t)+Ke(t)$, $y(t) = Cx(t)+e(t)$로 다변수 시스템에 적합하다. 모델 구조의 동일 식별 가능성(identifiability)을 정의하고, 서로 다른 파라미터가 동일한 입출력 거동을 낼 수 있는 문제를 논의한다. 블랙박스 파라미터화와 물리적 파라미터화의 장단점을 비교한다.

---

### Ch 5. Models for Time-varying and Nonlinear Systems
**핵심**: 시변·비선형 시스템의 모델 구조를 다루고, 인공신경망·퍼지·웨이블릿 등 블랙박스 비선형 모델을 소개한다.
**키워드**: time-varying, nonlinear, Hammerstein, Wiener, neural network, fuzzy model, NARX, semi-physical modeling
**상세**: → `Ljung-SystemID_marker_full.md` Ch 5 (L:5070)

선형 시불변 모델이 부적합한 경우를 위해 시변·비선형 모델 구조를 체계적으로 소개한다. 선형 시변 모델은 시불변 상태공간 모델의 행렬을 시간 함수로 교체한 $A_t(\theta), B_t(\theta), C_t(\theta)$로 기술하며, 비균등 샘플링과 비선형 시스템의 궤적 주변 선형화에 응용된다. 비선형 정적 특성이 있는 시스템에서는 Hammerstein 모델(입력 측 비선형성 후 선형 다이나믹스)과 Wiener 모델(선형 다이나믹스 후 출력 측 비선형성)이 유용하며, 예측기 형태가 상대적으로 단순하다. 반물리적(semi-physical) 모델링은 도메인 지식으로부터 핵심 비선형 변환을 도출하여 선형 회귀 모델에 통합하는 접근으로, 예를 들어 전력 = 전압 × 전류와 같은 물리적 관계를 특성으로 사용한다. 일반 비선형 블랙박스 모델에서는 과거 데이터를 비선형 함수에 적용하는 NARX, NARMAX 등의 구조를 다룬다. 인공신경망, 방사 기저 함수(RBF), 웨이블릿, 퍼지 모델 등 다양한 비선형 함수 근사 방법을 소개하고, 각각의 파라미터화와 예측기 구조를 비교한다. 비선형 모델은 표현 유연성이 크지만 유한 데이터에서 일반화가 어렵고 파라미터 수가 급격히 증가하는 문제가 있다.

---

### Ch 6. Nonparametric Time- and Frequency-Domain Methods
**핵심**: 파라미터 모델 없이 임펄스 응답과 전달함수를 직접 추정하는 비파라미터 방법을 소개한다.
**키워드**: correlation analysis, spectral analysis, periodogram, frequency response, transient response, nonparametric
**상세**: → `Ljung-SystemID_marker_full.md` Ch 6 (L:5924)

비파라미터 방법은 유한 차원 파라미터 벡터 없이 임펄스 응답이나 전달함수를 직접 추정한다. 임펄스 응답 분석은 펄스 입력을 가하여 출력에서 임펄스 응답을 직접 읽는 가장 단순한 방법이지만, 충분한 펄스 진폭이 요구되어 실용성에 한계가 있다. 계단 응답 분석은 지연, 정적 이득, 주요 시상수 등 기본 제어 파라미터를 읽기에 유용하며, Ziegler-Nichols 등 고전 조정 규칙의 기초가 된다. 상관 분석(correlation analysis)은 입력을 백색 잡음으로 선택할 때 $\hat{g}(\tau) = R_{yu}(\tau)/\alpha$로 임펄스 응답을 추정하며, 일반 입력에서는 Wiener-Hopf 방정식을 풀어야 한다. 주파수 응답 분석(sine-wave testing)은 각 주파수의 정현파 입력에 대한 출력 진폭·위상 비로 전달함수를 추정하며, 상관 방법으로 노이즈에 강건하게 구현할 수 있다. 주기도(periodogram)와 스펙트럼 밀도 추정은 DFT 기반으로 계산하며, Welch의 중첩 평균과 같은 스무딩 기법으로 분산을 줄인다. 모든 비파라미터 방법은 개방 루프(open loop) 가정 하에서만 편향 없이 동작하며, 폐쇄 루프에서는 문제가 발생할 수 있다.

---

### Ch 7. Parameter Estimation Methods
**핵심**: 파라미터 추정의 원리를 정형화하고, 예측 오차 방법(PEM), 최소제곱, 최대우도, 상관·도구변수 방법을 체계화한다.
**키워드**: prediction error method (PEM), least squares, maximum likelihood, instrumental variable (IV), subspace method, criterion function
**상세**: → `Ljung-SystemID_marker_full.md` Ch 7 (L:6843)

파라미터 추정은 데이터 집합 $Z^N$을 파라미터 공간으로 매핑하는 절차이며, 핵심 원리는 예측 오차 $\varepsilon(t,\theta) = y(t) - \hat{y}(t|\theta)$를 가능한 한 작게 만드는 것이다. 예측 오차 방법(PEM)은 $\hat{\theta}_N = \arg\min_\theta V_N(\theta, Z^N)$으로 정의되며, 여기서 $V_N(\theta, Z^N) = \frac{1}{N}\sum_{t=1}^N \ell(\varepsilon_F(t,\theta))$이다. 선형 필터 $L(q)$를 통한 사전 필터링은 주파수 대역 강조에 해당하며, 손실 함수 $\ell(\cdot)$의 선택은 통계적 효율성과 로버스트성에 영향을 준다. 이차 손실 $\ell(\varepsilon) = \frac{1}{2}\varepsilon^2$는 Gaussian 잡음 가정 하에서 최대우도 추정과 일치한다. ARX 모델에서 예측기가 파라미터에 선형이면 최소제곱의 닫힌 형태 해 $\hat{\theta}_N = R^{-1}(N)f(N)$이 존재한다. ARMAX, OE 등 비선형 회귀 구조에서는 반복 최적화가 필요하다. 도구변수(IV) 방법은 $\frac{1}{N}\sum \zeta(t)\varepsilon(t,\hat{\theta}) = 0$을 풀어 교란과 상관된 회귀 벡터 문제를 해결한다. 부분공간(subspace) 방법은 한크(Hankel) 행렬로부터 관측 가능성 부분공간을 추출하여 상태공간 모델을 직접 추정한다.

---

### Ch 8. Convergence and Consistency
**핵심**: 데이터 수가 무한히 증가할 때 파라미터 추정치의 수렴 성질과 일관성을 분석한다.
**키워드**: consistency, convergence, informative data, true system, limit model, frequency-domain characterization
**상세**: → `Ljung-SystemID_marker_full.md` Ch 8 (L:8570)

추정치의 점근적 수렴 분석은 대규모 샘플 이론의 핵심이며, 현실에서 무한 데이터를 다루지 않더라도 추정치에 대한 신뢰도를 평가하는 사고 실험으로 가치가 있다. 데이터 생성 과정에 대한 기술 조건 D1은 입출력이 균일하게 안정적인 필터를 통과한 결정론적 성분과 4+δ차 모멘트를 가지는 독립 확률 변수의 합으로 표현됨을 가정한다. 참 시스템 $S: y(t) = G_0(q)u(t) + H_0(q)e_0(t)$를 설정하고, 모델 구조 $\mathcal{M}$이 참 시스템을 포함하는지($S \in \mathcal{M}$) 여부에 따라 일관성 분석이 달라진다. 데이터가 서로 다른 모델을 구별할 수 있을 때 "충분히 정보적(informative enough)"이라 하며, 이는 스펙트럼 행렬이 거의 모든 주파수에서 양정치일 때 성립한다. 예측 오차 방법의 한계치는 평균 기준 $\bar{V}(\theta) = \bar{E}\ell(\varepsilon(t,\theta))$를 최소화하는 $\theta^*$로 수렴하며, 이는 대수의 법칙으로 증명한다. $S \in \mathcal{M}$이고 데이터가 충분히 정보적이면 $\hat{\theta}_N \to \theta_0$으로 일관성이 성립한다. $S \notin \mathcal{M}$인 경우의 한계 모델을 주파수 영역에서 특성화하고, 이것이 입력 스펙트럼과 노이즈 모델에 어떻게 의존하는지 설명한다.

---

### Ch 9. Asymptotic Distribution of Parameter Estimates
**핵심**: 파라미터 추정치의 점근 정규 분포와 공분산 행렬을 유도하고, 크래머-라오 하한과의 관계를 분석한다.
**키워드**: asymptotic normality, covariance matrix, Cramér-Rao bound, Fisher information, variance expression
**상세**: → `Ljung-SystemID_marker_full.md` Ch 9 (L:9756)

수렴 성질에 더하여 추정치의 수렴 속도와 분포를 분석하는 것이 실용적으로 중요하다. $\sqrt{N}(\hat{\theta}_N - \theta^*)$의 점근 분포가 중심 극한 정리 유형의 논증으로 정규 분포에 수렴함을 증명한다. 테일러 전개로부터 $(\hat{\theta}_N - \theta^*) \approx -[\bar{V}''(\theta^*)]^{-1}V_N'(\theta^*, Z^N)$이 유도되고, $V_N'$가 독립 확률 변수들의 합의 형태이므로 점근 정규성이 성립한다. 점근 공분산 행렬은 $P_\theta = [\bar{V}''(\theta^*)]^{-1}Q[\bar{V}''(\theta^*)]^{-1}$로 표현된다. $S \in \mathcal{M}$이고 이차 기준을 사용할 때는 $P_\theta = \lambda_0[\bar{E}\psi(t,\theta_0)\psi^T(t,\theta_0)]^{-1}$로 단순화된다. 이 공분산은 피셔 정보 행렬의 역행렬과 일치하여 이차 기준 PEM이 점근적으로 크래머-라오 하한을 달성함을 보인다. 주파수 영역 표현을 통해 전달함수 추정의 분산이 각 주파수에서 신호대잡음비의 역수에 비례함을 보인다. 이 결과는 실험 설계 최적화와 모델 차수 선택의 이론적 근거가 된다.

---

### Ch 10. Computing the Estimate
**핵심**: 예측 오차 최소화, 상관 방정식, 부분공간 방법을 수치적으로 효율적으로 계산하는 알고리즘을 설명한다.
**키워드**: QR factorization, Levinson algorithm, gradient descent, Newton method, subspace identification, numerical computation
**상세**: → `Ljung-SystemID_marker_full.md` Ch 10 (L:11099)

파라미터 추정 계산 문제는 비선형 계획법의 표준 문제이지만, 시스템 식별의 구조가 알고리즘 설계에 도움을 준다. 선형 회귀(ARX)에서 최소제곱 추정은 정규 방정식 $R(N)\hat{\theta}_N = f(N)$을 풀어야 하며, 수치 안정성을 위해 QR 분해를 사용한다. QR 분해 접근은 조건수를 $R(N)$의 제곱근 수준으로 낮추고, 상삼각 행렬이 되어 역추적이 용이하며, 더 작은 차수 모델의 해도 자동으로 얻는다. Levinson 알고리즘은 Toeplitz 구조를 활용하여 AR 모델 계산을 $O(n^2)$ 복잡도로 수행하며, 반사 계수(reflection coefficients)를 재귀적으로 계산한다. 비선형 모델 구조(ARMAX, OE 등)에서는 반복 Gauss-Newton 방법이 표준이며, 수렴을 위한 초기치 선택과 다중 극소 문제가 실용적 도전이다. 부분공간 방법은 데이터로부터 관측 가능성 행렬을 추출하고 SVD로 계수를 결정하는 직접 방법으로, 반복 탐색 없이 상태공간 모델을 추정한다.

---

### Ch 11. Recursive Estimation Methods
**핵심**: 데이터가 순차적으로 도착할 때 실시간으로 파라미터를 갱신하는 재귀 추정 알고리즘을 유도하고 분석한다.
**키워드**: recursive least squares (RLS), forgetting factor, Kalman filter, adaptive control, online identification
**상세**: → `Ljung-SystemID_marker_full.md` Ch 11 (L:12574)

적응 제어, 적응 필터링, 장애 감지 등 실시간 응용에서는 새로운 데이터가 도착할 때마다 모델을 갱신해야 한다. 재귀 알고리즘은 $\hat{\theta}_t = \hat{\theta}_{t-1} + \gamma_t Q_\theta(X(t), y(t), u(t))$ 형태의 고정 계산량 갱신으로 구현된다. 재귀 최소제곱(RLS) 알고리즘은 망각 인수(forgetting factor) $\lambda(t)$를 사용하는 가중 최소제곱으로부터 유도되며, 행렬 역산 보조 정리를 이용하여 이득 벡터 $L(t)$와 공분산 행렬 $P(t)$를 효율적으로 갱신한다. 망각 인수 $\lambda < 1$은 오래된 데이터의 영향을 지수적으로 감소시켜 시변 시스템 추적을 가능하게 한다. RLS의 이득 갱신은 칼만 필터와 동형적이어서 상태 추정과 파라미터 추정이 통합 프레임워크를 공유한다. 일반 예측 오차 방법의 재귀 버전은 준 뉴턴(quasi-Newton) 형태로 구현되며, 이론적 성질은 대응하는 오프라인 추정치로의 수렴으로 분석한다. 실용적 이슈로 공분산 행렬의 조건 저하, 지나친 추적(wind-up), 분산 추정의 모니터링 등을 다룬다.

---

### Ch 12. Options and Objectives
**핵심**: 식별 과정에서 사용자가 선택할 수 있는 설계 변수를 정의하고, 모델 품질을 주파수 가중 이차 기준으로 형식화한다.
**키워드**: design variables, model quality, bias-variance, frequency weighting, design criterion, model application
**상세**: → `Ljung-SystemID_marker_full.md` Ch 12 (L:13842)

시스템 식별의 목표는 적절한 작업량으로 좋고 신뢰할 수 있는 모델을 얻는 것이며, 이를 위해 설계 변수 $\mathcal{D}$의 집합을 정의한다. 설계 변수에는 실험 조건, 모델 구조, 식별 알고리즘, 검증 절차가 포함된다. 모델 품질은 참 시스템과 추정 모델 간의 차이를 주파수 가중 기준 $\bar{J}(\mathcal{D}) = \int_{-\pi}^{\pi} \text{tr}[\Pi(\omega,\mathcal{D})C(\omega)]d\omega$로 측정한다. 가중 행렬 $C(\omega)$는 모델의 응용 목적에 따라 결정되며, 시뮬레이션에서는 입력 스펙트럼으로, 예측에서는 잡음 스펙트럼으로 표현된다. 모델 오차는 편향(bias) 기여와 분산(variance) 기여로 분해되며, 이 두 성분은 모델 복잡도에 대해 반대 방향으로 움직인다. 최적 설계 문제는 $\min_{\mathcal{D}} \bar{J}(\mathcal{D})$로 공식화되며, 제약 조건 $\Delta$는 실험 비용, 신호 전력, 계산 복잡도 등을 포함한다. 이 형식화가 이후 챕터들(실험 설계, 데이터 전처리, 모델 선택)의 통합 프레임워크가 된다.

---

### Ch 13. Experiment Design
**핵심**: 정보가 충분한 데이터를 수집하기 위한 실험 설계 원칙, 지속 자극 조건, 폐쇄 루프 식별 방법을 다룬다.
**키워드**: persistently exciting, informative experiment, input design, closed-loop identification, sampling interval, open-loop
**상세**: → `Ljung-SystemID_marker_full.md` Ch 13 (L:14125)

좋은 실험 설계는 사후에 수정할 수 없어서 사전에 신중하게 수행해야 하는 가장 중요한 결정 중 하나다. 기본 설계 원칙으로 편향 최소화, 분산 최소화, 검증력 확보가 있으며 이들은 서로 상충할 수 있다. 데이터 집합이 충분히 정보적이려면 스펙트럼 행렬이 거의 모든 주파수에서 양정치여야 한다. 지속 자극(persistently exciting) 조건은 $n$개 주파수 성분이 있는 신호가 $n$차 이동 평균 필터로 완전히 제거될 수 없음을 의미하며, $n \times n$ 공분산 행렬 $\bar{R}_n$의 비특이성과 동치다. 입력 신호의 선택으로는 다중 정현파, 의사 랜덤 이진 신호(PRBS), 필터 백색 잡음이 대표적이며, 각각의 스펙트럼 분포와 구현 편의성이 다르다. 폐쇄 루프 식별에서는 입력과 잡음이 상관되어 개방 루프 방법이 편향을 낳으므로, 직접 방법, 간접 방법, 연속 폐쇄 루프 방법 중 적절한 접근을 선택해야 한다. 최적 입력 설계는 분산 행렬 $P_\theta(X)$의 스칼라 척도를 최소화하는 문제로, 이차 계획법으로 스펙트럼 분포를 최적화한다. 샘플링 간격과 반샘플링 필터의 선택도 다룬다.

---

### Ch 14. Preprocessing Data
**핵심**: 식별 알고리즘 적용 전에 데이터의 오프셋, 이상치, 누락 데이터, 주파수 범위 등을 전처리하는 방법을 다룬다.
**키워드**: detrending, outliers, missing data, prefiltering, differencing, data segmentation
**상세**: → `Ljung-SystemID_marker_full.md` Ch 14 (L:15543)

수집된 데이터를 즉시 식별 알고리즘에 적용하기보다는 여러 전처리 단계가 필요하다. 오프셋과 추세(drift)는 물리적 평형점에서의 편차로 정의하거나 표본 평균을 빼는 방식으로 제거하며, 차분(differencing)이나 고역 통과 필터링도 대안이 된다. 차분은 ARIMA 모델과 동치이지만 기준 함수를 고주파 영역으로 치우치게 하는 단점이 있어 주의가 필요하다. 이상치(outlier)는 잔차 그래프로 감지하며, 강건 노름(예: Huber 함수)이나 이상치 구간 제거·병합으로 처리한다. 누락 입력 데이터는 미지 파라미터로 처리하여 모델과 함께 추정하고, 누락 출력 데이터는 시변 칼만 필터로 올바른 예측기를 유도하거나 EM 알고리즘으로 처리한다. 여러 데이터 세그먼트는 초기 상태를 파라미터로 추가하거나 각 세그먼트의 예측 오차를 합산하여 병합할 수 있다. 사전 필터링(prefiltering)은 관심 주파수 대역을 강조하거나 고주파 노이즈를 억제하는 데 사용되며, 노이즈 모델 $H(q)$를 수정하는 것과 동치임을 보인다.

---

### Ch 15. Choice of Identification Criterion
**핵심**: 예측 오차 방법, 상관 방법, 부분공간 방법 간의 선택 기준과 노름 선택의 로버스트성을 분석한다.
**키워드**: norm selection, robustness, maximum likelihood, Huber norm, instrumental variable, bias-variance tradeoff
**상세**: → `Ljung-SystemID_marker_full.md` Ch 15 (L:16053)

세 가지 기본 식별 방법(PEM, 상관 방법, 부분공간 방법) 각각의 적용 가능성, 편향, 분산, 계산 편의성을 종합적으로 비교한다. PEM은 선형·비선형, 개방·폐쇄 루프 모두 적용 가능하며 편향 분포를 명확히 제어할 수 있어 가장 범용적이다. 노름 $\ell(\cdot)$ 선택의 최적 기준은 분산 스케일 $\kappa(\ell, f_e) = \int[\ell'(x)]^2 f_e(x)dx / [\int\ell''(x)f_e(x)dx]^2$를 최소화하는 것이며, 최적 선택은 최대우도 $\ell_\text{opt}(\varepsilon) = -\log f_e(\varepsilon)$이다. Gaussian 잡음에서는 이차 노름이 최적이다. 그러나 이상치가 소수 존재할 때 이차 노름의 $\kappa$가 급격히 증가(예시: 0.1% 이상치에서 11배 증가)하여 강건 노름이 필요하다. Huber 노름은 $|\varepsilon| \leq c$이면 이차, $|\varepsilon| > c$이면 선형으로 작동하며 이상치에 강건하다. 도구변수(IV) 방법의 최적 도구 선택은 점근 분산 최소화로 유도되며, 이는 특정 예측 오차 방법과 동등한 정확도를 달성한다. 실용적 권고 사항으로 일반적인 경우 PEM을 우선 시도하고, 계산 효율과 폐쇄 루프 고려시 부분공간 방법을 활용한다.

---

### Ch 16. Model Structure Selection and Model Validation
**핵심**: 적절한 모델 구조를 선택하는 방법과 식별된 모델의 타당성을 검증하는 절차를 체계화한다.
**키워드**: order selection, model validation, residual analysis, AIC, cross-validation, bias-variance tradeoff
**상세**: → `Ljung-SystemID_marker_full.md` Ch 16 (L:16500)

모델 구조 선택은 모델 타입(선형/비선형, 블랙박스/물리 기반), 모델 크기(차수), 파라미터화 방식의 세 단계 결정을 포함한다. 품질 기준은 편향과 분산의 합 $J(\mathcal{D}) = J_B(\mathcal{D}) + J_P(\mathcal{D})$로, 더 복잡한 구조는 편향을 줄이지만 분산을 키우는 상충 관계가 있다. 물리 기반 모델은 파라미터 효율이 높고, 블랙박스 모델은 알고리즘 단순성과 범용성이 장점이다. 사전 데이터 분석으로 스펙트럼 분석 추정치, 공분산 행렬의 계수, 변수 상관 분석을 활용하여 적절한 모델 차수를 가늠할 수 있다. 정보 기준(AIC, BIC, MDL)을 포함한 다양한 차수 선택 방법을 비교하고, 교차 검증으로 데이터를 추정·검증 집합으로 분리하여 모델 일반화 성능을 평가한다. 잔차 분석은 가장 중요한 검증 도구로, 잔차의 백색성(화이트니스) 검정과 잔차-입력 교차 상관으로 미설명 구조를 탐지한다. 극영점 도표(pole-zero plot)의 상쇄 패턴은 과도적합이나 부적절한 구조를 시사한다.

---

### Ch 17. System Identification in Practice
**핵심**: 실제 시스템 식별의 실용적 절차를 5단계 워크플로우로 정리하고, 실제 데이터에 적용한 사례 연구를 제시한다.
**키워드**: interactive software, MATLAB SITB, practical procedure, hairdryer application, JAS-Gripen, step-by-step
**상세**: → `Ljung-SystemID_marker_full.md` Ch 17 (L:17275)

실제 시스템 식별은 이론 이외에 경험, 직관, 통찰이 중요하며 반복적인 탐색 과정이다. MATLAB의 System Identification Toolbox(SITB)를 비롯한 대화형 소프트웨어가 핵심 도구이며, 데이터 처리, 비파라미터 추정, 파라미터 추정, 모델 표현, 검증 루틴을 제공한다. 실용적 식별 절차는 5단계로 정리된다: Step 1(데이터 시각화 및 전처리), Step 2(초기 모델 신속 추정으로 문제 난이도 파악), Step 3(불일치 원인 진단), Step 4(차수 및 노이즈 구조 세밀 조정), Step 5(최종 모델 채택). 헤어드라이어 실험(PT326 Process Trainer)은 실험실 규모 응용으로, PRBS 입력, 데이터 분리(추정/검증), 상관 분석, ARX 및 상태공간 초기 모델, 1000개 ARX 모델 병렬 계산으로 최적 차수를 탐색하는 전 과정을 보여준다. 최종적으로 ARX(9,6,2)와 ARMAX(3,3,2,2)가 잔차 검정을 통과하며, 간결한 ARMAX 모델이 실용적 최종 선택이 된다. JAS-Gripen 전투기의 피치 채널 식별 사례도 제시하여 폐쇄 루프 데이터 처리 및 다입력 모델링의 실제 도전을 다룬다.

---

## Marker 세부 목차

> `L:숫자`는 `Ljung-SystemID_marker_full.md`의 라인 번호.

- Ch 1 Introduction `L:562`
- Ch 2 Time-Invariant Linear Systems `L:914`
- Ch 3 Simulation and Prediction `L:2395`
- Ch 4 Models of Linear Time-Invariant Systems `L:2952`
- Ch 5 Models for Time-varying and Nonlinear Systems `L:5070`
- Ch 6 Nonparametric Time- and Frequency-Domain Methods `L:5924`
- Ch 7 Parameter Estimation Methods `L:6843`
- Ch 8 Convergence and Consistency `L:8570`
- Ch 9 Asymptotic Distribution of Parameter Estimates `L:9756`
- Ch 10 Computing the Estimate `L:11099`
- Ch 11 Recursive Estimation Methods `L:12574`
- Ch 12 Options and Objectives `L:13842`
- Ch 13 Experiment Design `L:14125`
- Ch 14 Preprocessing Data `L:15543`
- Ch 15 Choice of Identification Criterion `L:16053`
- Ch 16 Model Structure Selection and Model Validation `L:16500`
- Ch 17 System Identification in Practice `L:17275`
