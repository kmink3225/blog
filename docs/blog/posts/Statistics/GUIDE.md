# Statistics 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Statistics 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **수학적 엄밀성이 핵심**: 정의 → 정리 → 증명 → 예시 흐름을 따른다
- **이론과 실무의 연결**: 순수 수학이 아닌 응용 통계학 관점으로 작성한다
- **교재 기반 작성**: `docs/book/statistics/` (Casella & Berger), `docs/book/mixed_model/` (Hedeker & Gibbons), `docs/book/fda/` (Ramsay) 등을 참조한다
- **한국어/영어 병기**: 핵심 용어는 `한국어(English)` 형태로 처음 등장 시 병기한다

---

## 포스트 콘텐츠 구조

Statistics 카테고리의 포스트는 다음 구조를 따른다. 주제에 따라 일부 섹션을 생략하거나 순서를 조정할 수 있으나, 가능한 한 이 흐름을 유지한다.

### 1. 정의 (Definition)

- 공식적인 수학적 정의를 callout 블록으로 제시한다
- 표기법(notation)을 명확히 한다

```markdown
::: {.callout-note}
## 정의: 최대우도추정량 (Maximum Likelihood Estimator, MLE)

모수 $\theta$에 대한 최대우도추정량 $\hat{\theta}_{MLE}$는 다음과 같이 정의된다:

$$
\hat{\theta}_{MLE} = \arg\max_{\theta} L(\theta | \mathbf{x}) = \arg\max_{\theta} \prod_{i=1}^n f(x_i | \theta)
$$
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 정의가 왜 그렇게 구성되는지 수학적 근거를 설명한다
- 관련 정리(theorem)와 성질(properties)을 제시한다
- 가정(assumptions)과 조건(conditions)을 명시한다
- 증명이 필요한 경우 핵심 단계를 포함한다

### 3. 직관적 설명 (Intuitive Explanation)

- 수식 없이 핵심 아이디어를 전달한다
- 비유, 시각적 묘사, 일상 예시를 활용한다
- "한 줄 요약"을 제공한다

```markdown
> **직관**: MLE는 "관측된 데이터가 나올 확률이 가장 높은 모수 값을 찾는 것"이다.
> 동전을 10번 던져 7번 앞면이 나왔다면, 앞면 확률 $p=0.7$이 가장 그럴듯하다고 판단하는 것과 같다.
```

### 4. 왜 필요한가 (Why It Matters)

- 이 개념이 없으면 어떤 문제가 해결되지 않는지 설명한다
- 통계적 의사결정에서의 역할을 명시한다
- 선행 개념과의 관계를 밝힌다 (예: "점추정의 한계를 보완하기 위해 구간추정이 필요하다")

### 5. 응용 분야 (Applications)

- 어느 분야에서, 어떤 목적으로 사용되는지 구체적으로 기술한다
- 분야별 활용 예시를 테이블로 정리한다

```markdown
| 분야 | 활용 | 구체적 예시 |
|---|---|---|
| 임상시험 | 처치 효과 추정 | 신약의 혈압 강하 효과를 MLE로 추정 |
| 자연어처리 | 언어 모델 학습 | n-gram 확률의 MLE 추정 |
| 품질관리 | 공정 파라미터 추정 | 제조 공정의 불량률 추정 |
| 보험수리 | 손해 분포 모수 추정 | 보험금 청구액의 파레토 분포 적합 |
```

### 6. 예시 (Examples)

- 손으로 풀 수 있는 간단한 수학적 예시를 제시한다
- 단계별 풀이 과정을 보여준다
- 결과의 해석을 포함한다

### 7. 코드 예시 (Code Examples)

- **2단계 구성**: (1) 순수 Python으로 통계 공식을 직접 구현 → (2) scipy/statsmodels 등 프레임워크로 실무 코드 제시
- 패키지: `numpy` (low-level), `statsmodels`, `scipy.stats`, `pandas` (Python) / `lme4`, `survival`, `fda` (R)
- 시뮬레이션 또는 실제 데이터 분석 예시를 포함한다
- 결과 해석을 코드 아래에 추가한다

```markdown
#### Step 1: 순수 Python 구현 (원리 이해)

```python
import math

# 순수 Python으로 정규 분포 MLE 구현 — 공식을 직접 확인
data = [2.3, 1.8, 3.1, 2.7, 2.5]

# MLE for mu: 우도를 최대화하는 mu = 표본 평균
mu_mle = sum(data) / len(data)

# MLE for sigma: n으로 나눔 (비편향이 아닌 MLE)
sigma_mle = math.sqrt(sum((x - mu_mle) ** 2 for x in data) / len(data))

# 로그 우도 계산
log_likelihood = sum(
    -0.5 * math.log(2 * math.pi) - math.log(sigma_mle)
    - 0.5 * ((x - mu_mle) / sigma_mle) ** 2
    for x in data
)

print(f"mu_hat = {mu_mle:.3f}, sigma_hat = {sigma_mle:.3f}")
print(f"log-likelihood = {log_likelihood:.3f}")
```

#### Step 2: scipy 구현 (실무 활용)

```python
import numpy as np
from scipy.stats import norm

data = np.array([2.3, 1.8, 3.1, 2.7, 2.5])

# scipy의 MLE 피팅
mu_mle, sigma_mle = norm.fit(data)
log_lik = np.sum(norm.logpdf(data, loc=mu_mle, scale=sigma_mle))

print(f"mu_hat = {mu_mle:.3f}, sigma_hat = {sigma_mle:.3f}")
print(f"log-likelihood = {log_lik:.3f}")
```
```

### 8. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**선행 지식**

- [확률론 기초](../2023-02-05_probability.qmd)
- [확률 분포](../2023-02-06_distribution.qmd)

**후속 주제**

- [충분통계량과 피셔 정보](../2023-03-26_sufficiency.qmd)
- [구간 추정](../2023-04-01_interval_estimation.qmd)

**관련 개념**

- [베이지안 추정](../bayesian_estimation.qmd) — MLE와 MAP의 비교
- [EM 알고리즘](../../Machine_Learning/em_algorithm.qmd) — 불완전 데이터에서의 MLE
```

---

## 하위 카테고리별 추가 지침

### 종단 데이터 분석 (LDA/)

- Mixed Model 포스트는 GLM과의 관계를 항상 명시한다
- 수식에서 고정효과($\beta$)와 랜덤효과($b_i$)를 명확히 구분한다
- R(`lme4`)과 Python(`statsmodels`) 코드를 병행 제시한다
- 파일명 패턴: `01-mixed-model-*.qmd` (번호 prefix)

### 함수형 데이터 분석 (FDA/)

- 교재: `docs/book/fda/` (Ramsay & Silverman, Kokoszka & Reimherr)
- 함수 공간, 기저함수, FPCA 등 고유 개념에 대해 유한차원 통계학과의 대비를 통해 설명한다
- 실무 응용(RT-PCR, 센서 데이터 등)과의 연결을 포함한다

### 시계열 (time_series/)

- 정상성, ACF/PACF, 모형 식별 → 추정 → 진단 → 예측 순서를 따른다
- R(`tseries`, `forecast`)과 Python(`statsmodels.tsa`) 코드를 포함한다

---

## 수식 작성 규칙

- 확률변수는 대문자($X$), 관측값은 소문자($x$)로 표기한다
- 모수는 그리스 문자($\theta, \mu, \sigma$), 추정량은 hat($\hat{\theta}$)을 사용한다
- 행렬은 굵은 대문자($\mathbf{X}$), 벡터는 굵은 소문자($\mathbf{x}$)로 표기한다
- 블록 수식에는 번호를 매기지 않는다 (Quarto 기본 설정 사용)
- 긴 유도 과정은 `aligned` 환경을 사용한다:

```latex
$$
\begin{aligned}
\ell(\theta) &= \sum_{i=1}^n \log f(x_i|\theta) \\
&= \sum_{i=1}^n \left[ \log h(x_i) + \eta(\theta)^\top T(x_i) - A(\theta) \right]
\end{aligned}
$$
```

---

## 교재 참조 매핑

| 주제 영역 | 교재 소스 경로 | 주요 교재 |
|---|---|---|
| 수리통계 | `docs/book/statistics/` | Casella & Berger |
| GLM/회귀 | `docs/book/glm/` | McCullagh & Nelder, Faraway |
| 종단 데이터 | `docs/book/mixed_model/` | Hedeker & Gibbons |
| 생존 분석 | `docs/book/survival/` | Kleinbaum, Hosmer |
| FDA | `docs/book/fda/` | Ramsay & Silverman, Kokoszka |
| 베이지안 | `docs/book/bayesian/` | Gelman, Downey |
