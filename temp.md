# Curvature (곡률) — 수식과 직관

## 0. $\kappa$ 공식의 유도 — 무엇을 미분했는가

### 출발점: curvature의 정의

곡선 위를 따라 이동할 때, 접선이 $x$축과 이루는 각도를 $\theta$라 하면:

$$\kappa = \left|\frac{d\theta}{ds}\right|$$

- $\theta$: 접선 각도 (방향)
- $s$: 호의 길이 (곡선을 따라 실제로 이동한 거리)
- 즉, **"곡선을 한 걸음 걸을 때 방향이 얼마나 바뀌는가"**

### Step 1: $\theta$를 $f'(x)$로 표현

접선의 기울기는 $\tan\theta = f'(x)$이므로:

$$\theta = \arctan(f'(x))$$

양변을 $x$로 미분하면 ($\arctan(u)$의 미분 $= \frac{u'}{1+u^2}$):

$$\frac{d\theta}{dx} = \frac{f''(x)}{1 + (f'(x))^2}$$

### Step 2: 호의 길이 $ds$를 $dx$로 표현

곡선의 미소 호 길이는:

$$ds = \sqrt{1 + (f'(x))^2} \, dx$$

따라서:

$$\frac{ds}{dx} = \sqrt{1 + (f'(x))^2}$$

### Step 3: Chain rule로 결합

$$\kappa = \left|\frac{d\theta}{ds}\right| = \left|\frac{d\theta/dx}{ds/dx}\right| = \frac{\left|\frac{f''(x)}{1+(f'(x))^2}\right|}{\sqrt{1+(f'(x))^2}}$$

정리하면:

$$\boxed{\kappa = \frac{|f''(x)|}{(1 + (f'(x))^2)^{3/2}}}$$

### 분모 $3/2$승의 기원

| 공식의 항 | 유래 |
|---|---|
| 분자 $f''(x)$ | $\frac{d\theta}{dx}$에서 옴. $\arctan(f')$를 미분하면 $f''$이 분자에 등장 |
| 분모의 $1 + (f')^2$ | 두 곳에서 옴: (1) $\arctan$ 미분 시 $\frac{1}{1+u^2}$에서 한 번, (2) 호 길이 $ds/dx = \sqrt{1+(f')^2}$에서 한 번 |
| 분모의 지수 $3/2$ | $(1+(f')^2)^1$ (arctan 미분) $\times$ $(1+(f')^2)^{1/2}$ (호 길이) $= (1+(f')^2)^{3/2}$ |

결국 $\kappa$는 **"$\arctan(f'(x))$를 호의 길이 $s$에 대해 미분한 것"**이다.

---

## 1. 평면 곡선의 Curvature

함수 $y = f(x)$로 표현된 곡선의 curvature:

$$\kappa = \frac{|f''(x)|}{(1 + (f'(x))^2)^{3/2}}$$

**각 항의 의미:**

| 항 | 의미 |
|---|---|
| $f'(x)$ | 1차 도함수. 곡선의 **기울기(방향)**. 지금 어디를 향하고 있는지 |
| $f''(x)$ | 2차 도함수. 기울기가 **얼마나 빠르게 변하는지**. 이것이 curvature의 핵심 |
| $\|f''(x)\|$ | 절대값을 씌우는 이유: 위로 휘든 아래로 휘든 **휘어진 정도** 자체만 측정 |
| $(1 + (f'(x))^2)^{3/2}$ | **정규화(normalization) 항**. 기울기가 가파른 곳에서 $f''$이 과대평가되는 것을 보정 |

**직관:** 분자는 "방향이 얼마나 빠르게 변하는가", 분모는 "곡선을 따라 실제로 이동하는 속도로 보정"이다. 즉, curvature는 **단위 호(arc) 길이당 방향 변화량**이다.

**특수한 경우:**

- $f'(x) = 0$ (수평인 점)이면 → $\kappa = |f''(x)|$. 2차 도함수가 곧 curvature
- $f''(x) = 0$이면 → $\kappa = 0$. 직선처럼 안 휘어진 구간

---

## 2. 원과의 관계 — 가장 직관적인 해석

곡선 위의 점에서 curvature $\kappa$는 그 점을 가장 잘 근사하는 원(**접촉원, osculating circle**)의 반지름 $R$과:

$$\kappa = \frac{1}{R}$$

- 반지름이 **작은** 원 → curvature **큼** → 급하게 꺾임
- 반지름이 **큰** 원 → curvature **작음** → 완만하게 휘어짐
- 직선 → $R = \infty$ → $\kappa = 0$

이것이 curvature의 **가장 직관적인 해석**이다. "이 점에서 곡선이 반지름 $R$짜리 원처럼 휘고 있다."

---

## 3. 다변수 함수에서의 Curvature — ML/최적화 맥락

임계점 $\mathbf{x}^*$에서 gradient = 0일 때의 2차 Taylor 근사:

$$f(\mathbf{x}) \approx f(\mathbf{x}^*) + \frac{1}{2}(\mathbf{x} - \mathbf{x}^*)^T \mathbf{H} (\mathbf{x} - \mathbf{x}^*)$$

| 항 | 의미 |
|---|---|
| $\mathbf{H}$ | **Hessian 행렬**. 2차 편미분의 행렬. 각 방향으로의 curvature 정보를 담고 있음 |
| $\mathbf{H}$의 고유값 $\lambda_i$ | **각 고유벡터 방향의 curvature**. $\lambda_i$가 크면 그 방향으로 급격히 휘어짐 |
| $\lambda_i > 0$ (모두) | 모든 방향으로 위로 볼록 → **극소점** |
| $\lambda_i < 0$ (모두) | 모든 방향으로 아래로 볼록 → **극대점** |
| 양수/음수 혼재 | 방향에 따라 볼록/오목 → **안장점 (saddle point)** |

**직관:** 1변수에서 $f''(x)$가 curvature였던 것이, 다변수에서는 **Hessian의 고유값**으로 일반화된다. 고유값 하나하나가 해당 방향의 curvature이다.

**최적화에서의 의미:**

- curvature가 큰 방향 → 학습률을 작게 (overshooting 방지)
- curvature가 작은 방향 → 학습률을 크게 (수렴 가속)
- 이것이 **Newton's method**, **Adam** 같은 2차 정보 활용 최적화의 핵심 아이디어

---

## 요약 — 한 줄 흐름

$$\text{1변수: } f''(x) \xrightarrow{\text{보정}} \kappa = \frac{|f''|}{(1+f'^2)^{3/2}} = \frac{1}{R} \xrightarrow{\text{다변수 일반화}} \lambda_i(\mathbf{H})$$

**Curvature의 본질은 하나다: "2차 도함수 = 방향이 얼마나 빠르게 변하는가"**

---

## 응용: 시계열 신호에서 스파이크/증폭 시점 탐지

### 핵심 아이디어

시계열 신호 $y = f(t)$에서 "갑자기 튀는 구간"은 **curvature가 급격히 커지는 지점**이다.

- 정상 구간: 신호가 완만 → $f'' \approx 0$ → $\kappa \approx 0$
- 증폭/스파이크 구간: 신호가 급변 → $f''$이 큼 → $\kappa$가 급등

따라서:

$$\kappa(t) = \frac{|f''(t)|}{(1 + (f'(t))^2)^{3/2}}$$

를 시간축 전체에 대해 계산하고, **$\kappa(t)$가 threshold를 넘는 $t$ 값을 찾으면** 그것이 신호가 튀는 시점이다.

### 왜 $f''(t)$만 쓰지 않고 $\kappa$를 쓰는가

| 상황 | $f''(t)$ | $\kappa(t)$ |
|---|---|---|
| 기울기가 이미 가파른 구간에서 $f''$이 큼 | 크게 나옴 (false positive) | 분모가 보정 → 적절히 억제 |
| 평탄한 구간에서 갑자기 방향 전환 | 작게 나올 수 있음 | 분모가 작아 → 민감하게 포착 |

$f''$만 보면 **이미 가파르게 상승 중인 구간**도 "급변"으로 잡힌다. $\kappa$는 분모의 $(1+(f')^2)^{3/2}$이 이를 보정해서, **진짜 방향이 꺾이는 지점**만 잡아낸다.

### 적용 흐름

```
1. 신호 f(t) 수집
2. 수치 미분으로 f'(t), f''(t) 계산 (or Savitzky-Golay 필터로 노이즈 제거 후 미분)
3. κ(t) 계산
4. threshold τ 설정 (e.g., mean + 3σ)
5. κ(t) > τ 인 t 값들 → 증폭/스파이크 시점
```

### 실용적 주의점

| 문제 | 대응 |
|---|---|
| 노이즈가 많으면 $f''$이 폭발 | 스무딩 먼저 적용 (이동평균, Savitzky-Golay 등) |
| 이산 데이터라 미분이 정확하지 않음 | 중심차분 $f''(t_i) \approx \frac{f(t_{i+1}) - 2f(t_i) + f(t_{i-1})}{(\Delta t)^2}$ 사용 |
| threshold 설정이 애매 | adaptive threshold (rolling window 기반) 또는 curvature의 curvature (3차 변화) 활용 |
