---
name: Statistics_GUIDE
type: category
version: 1.0
description: >
  LOAD when writing posts about 수리통계, 회귀분석, GLM, 혼합모형, 생존분석, FDA, 베이지안,
  시계열, 또는 Statistics 카테고리 전반. Covers 수학적 엄밀성 기준, 교재 기반 작성법,
  이론-실무 2단계 코드 구성, 수식 표기 규칙.
scope: docs/blog/posts/Statistics/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Statistics/index.qmd
book_sources:
  - docs/book/statistics/
  - docs/book/statistics/generalized_linear_model/
  - docs/book/statistics/longidutindal_data_analysis/
  - docs/book/statistics/survival/
  - docs/book/statistics/functional_data_analysis/
  - docs/book/statistics/bayesian/
  - docs/book/statistics/timeseries/
cross_references:
  - docs/blog/posts/Math/GUIDE.md
  - docs/blog/posts/Experimentation/GUIDE.md
  - docs/blog/posts/Machine_Learning/GUIDE.md
  - docs/blog/posts/Deep_Learning/GUIDE.md
---

# Statistics 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Statistics 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **수학적 엄밀성이 핵심**: 정의 → 정리 → 증명 → 예시 흐름을 따른다
- **이론과 실무의 연결**: 순수 수학이 아닌 응용 통계학 관점으로 작성한다
- **교재 기반 작성**: `docs/book/statistics/` (Casella & Berger), `docs/book/statistics/longidutindal_data_analysis/` (Hedeker & Gibbons), `docs/book/statistics/functional_data_analysis/` (Ramsay) 등을 논리적 뼈대로 활용하되, agent의 최신 지식으로 보완한다
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
- 추상적이거나 이해하기 어려운 개념에는 비유, 시각적 묘사, 일상 예시 등 직관적 설명을 적재적소에 포함한다 (필요시 별도 섹션으로 분리 가능)
- 각 개념 또는 원리에 데이터 사이언스 실무에 어떻게 적용될 수 있는지 설명한다

### 3. 왜 필요한가 (Why It Matters)

- 이 개념이 없으면 어떤 문제가 해결되지 않는지 설명한다
- 통계적 의사결정에서의 역할을 명시한다
- 선행 개념과의 관계를 밝힌다 (예: "점추정의 한계를 보완하기 위해 구간추정이 필요하다")

### 4. 응용 분야 (Applications)

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

### 5. 예시 (Examples)

- 손으로 풀 수 있는 간단한 수학적 예시를 제시한다
- 단계별 풀이 과정을 보여준다
- 결과의 해석을 포함한다

### 6. 코드 예시 (Code Examples)

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

### 7. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**선행 지식**

- [확률론 기초](../37-set-theory.qmd)
- [확률 분포](../2023-02-06_distribution.qmd)

**후속 주제**

- [충분통계량과 피셔 정보](../2023-03-26_sufficiency.qmd)
- [구간 추정](../2023-04-01_interval_estimation.qmd)

**관련 개념**

- [베이지안 추정](../bayesian_estimation.qmd) — MLE와 MAP의 비교
- [EM 알고리즘](../../Machine_Learning/em_algorithm.qmd) — 불완전 데이터에서의 MLE
```

---

## 흔한 실수 교정 (Fix Blocks)

<fix-formula-without-intuition>
**WRONG**: 수식만 나열하고 바로 다음 주제로 넘어감

```markdown
## MLE
$$\hat{\theta} = \arg\max_\theta L(\theta|\mathbf{x})$$
다음으로 충분통계량을 살펴보자.
```

**CORRECT**: 수식 전에 직관적 설명, 수식 후에 해석

```markdown
## MLE
관측된 데이터를 가장 잘 설명하는 모수를 찾는 것이 핵심이다.
"이 데이터가 나올 확률을 최대로 만드는 θ는 무엇인가?"라는 질문에 답한다.

$$\hat{\theta} = \arg\max_\theta L(\theta|\mathbf{x})$$

즉, 우도함수 $L$을 θ에 대해 최대화한다. 직관적으로는
"모든 후보 θ 중에서, 관측된 표본을 생성했을 가능성이 가장 높은 θ를 선택"하는 것이다.
```
</fix-formula-without-intuition>

<fix-code-framework-only>
**WRONG**: 프레임워크 코드만 제시하여 내부 원리를 알 수 없음

```python
# BAD: statsmodels 한 줄로 끝
import statsmodels.api as sm
result = sm.OLS(y, X).fit()
print(result.summary())
```

**CORRECT**: low-level 구현(numpy)으로 원리 이해 → 프레임워크(statsmodels)로 실무 활용, 2단계 제시

```python
# Step 1: numpy로 OLS 직접 구현 — 정규방정식 확인
import numpy as np
beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y  # (X'X)^{-1}X'y
residuals = y - X @ beta_hat
sigma2_hat = residuals @ residuals / (len(y) - X.shape[1])

# Step 2: statsmodels로 실무 코드
import statsmodels.api as sm
result = sm.OLS(y, X).fit()
print(result.summary())
```
</fix-code-framework-only>

---

## 하위 카테고리별 추가 지침

### 종단 데이터 분석 (LDA/)

- Mixed Model 포스트는 GLM과의 관계를 항상 명시한다
- 수식에서 고정효과($\beta$)와 랜덤효과($b_i$)를 명확히 구분한다
- R(`lme4`)과 Python(`statsmodels`) 코드를 병행 제시한다
- 파일명 패턴: `01-mixed-model-*.qmd` (번호 prefix)

### 함수형 데이터 분석 (FDA/)

- 교재: `docs/book/statistics/functional_data_analysis/` (Ramsay & Silverman, Kokoszka & Reimherr)
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

## 교재 활용 매핑

| 주제 영역 | 교재 소스 경로 | 주요 교재 |
|---|---|---|
| 수리통계 | `docs/book/statistics/` | Casella & Berger |
| GLM/회귀 | `docs/book/statistics/generalized_linear_model/` | McCullagh & Nelder, Faraway |
| 종단 데이터 | `docs/book/statistics/longidutindal_data_analysis/` | Hedeker & Gibbons |
| 생존 분석 | `docs/book/statistics/survival/` | Kleinbaum, Hosmer |
| FDA | `docs/book/statistics/functional_data_analysis/` | Ramsay & Silverman, Kokoszka |
| 베이지안 | `docs/book/statistics/bayesian/` | Gelman, Downey |

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재를 **논리적 뼈대**로 활용한다. 교재의 체계를 참고하되, agent의 최신 사전지식으로 outdated된 내용은 수정하고 부족한 부분은 보완한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Casella & Berger — Statistical Inference (2002) | `docs/book/statistics/Casella-StatisticalInference-summary.md` | 확률론, 추정, 검정, 신뢰구간, 점근이론 |
| Gelman et al. — Bayesian Data Analysis (2013) | `docs/book/statistics/bayesian/Gelman-BayesianDataAnalysis-summary.md` | 베이지안 추론, 사후분포, MCMC, 계층모형 |
| Downey — Think Bayes (2021) | `docs/book/statistics/bayesian/Downey-ThinkBayes-summary.md` | 베이지안 기초, Python 구현 |

**활용 절차**: Summary 읽기 → 논리 구조 파악 → Full MD에서 수식/정의 확인 → 교재 내용 중 유효한 부분은 유지, outdated된 부분은 agent 지식으로 수정·보완 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용

---

<boundaries>
**CAN (허용)**:

- 수학적으로 엄밀한 정의/정리 기반 설명 — 정의 → 정리 → 증명 → 예시 흐름
- 교재 기반 증명/유도 포함 (Casella & Berger, Gelman, Ramsay 등)
- Python + R 코드 병행 제시 (low-level 구현 + 프레임워크 2단계)
- 다른 카테고리와 크로스 링크 (Math, Experimentation, Machine_Learning, Deep_Learning 등)

**CANNOT (금지)**:

- 교재에 없는 방법론을 교재 기반인 것처럼 서술 — 출처가 교재가 아니면 "agent 지식 기반"으로 명시하거나, 적절한 레퍼런스를 별도로 밝힌다
- 증명 없이 "자명하다(trivial)" 처리 — 자명하더라도 최소한 핵심 논증 단계를 1~2줄로 제시한다
- 실무 예시 없이 이론만 나열 — 반드시 응용 분야 또는 코드 예시를 포함하여 이론-실무 연결을 보여준다
</boundaries>
