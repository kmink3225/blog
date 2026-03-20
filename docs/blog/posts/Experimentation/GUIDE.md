---
name: Experimentation_GUIDE
type: category
version: 1.0
description: Experimentation 카테고리 포스트 작성 규칙 — 역학 원류, 인과추론 프레임워크, A/B 테스트
scope: docs/blog/posts/Experimentation/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Experimentation/index.qmd
book_sources:
  - docs/book/epidemiology/
cross_references:
  - docs/blog/posts/Statistics/GUIDE.md
  - docs/blog/posts/Data_Science/GUIDE.md
  - docs/blog/posts/Engineering/GUIDE.md
  - docs/blog/posts/Machine_Learning/GUIDE.md
---

# Experimentation 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Experimentation 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **역학(Epidemiology)이 원류**: A/B 테스트를 RCT의 IT 버전으로 이해하는 관점을 유지한다
- **인과추론 프레임워크 기반**: Rubin Causal Model(잠재적 결과), DAG(Pearl) 표기를 일관되게 사용한다
- **이론 → 실무 연결**: 통계적 원리를 먼저 설명하고 IT/비즈니스 맥락의 실무 적용으로 이어간다
- **계층적 학습 경로**: Epidemiology → A/B Test → Sequential/Bayesian → MAB → Advanced 순서를 따른다
- **교재 기반**: `docs/book/epidemiology/` (Hernan, Woodward, Schulz 등) 참조

---

## 포스트 콘텐츠 구조

Experimentation 카테고리의 포스트는 다음 구조를 따른다. 주제에 따라 일부 섹션을 생략하거나 순서를 조정할 수 있으나, 가능한 한 이 흐름을 유지한다.

### 1. 정의 (Definition)

- 공식적 정의를 callout 블록으로 제시한다
- 역학 용어와 IT 용어를 병기한다

```markdown
::: {.callout-note}
## 정의: 무작위 대조 시험 (Randomized Controlled Trial, RCT)

연구 대상을 **무작위(random)**로 처치군(treatment group)과 대조군(control group)에 배정하여
처치의 인과적 효과를 추정하는 실험 설계이다.

- 역학: Randomized Controlled Trial (RCT)
- IT: A/B Test, Online Controlled Experiment
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 인과추론의 수학적 프레임워크를 사용한다
- 잠재적 결과(Potential Outcomes) 표기법을 일관되게 적용한다: $Y_i(1)$, $Y_i(0)$, $\tau_i = Y_i(1) - Y_i(0)$
- 가정(SUTVA, ignorability, positivity 등)을 명시한다
- 편향(bias)의 방향과 크기를 논의한다

### 3. 직관적 설명 (Intuitive Explanation)

- 비유와 일상 예시를 활용한다
- "만약 무작위 배정을 하지 않으면 어떤 일이 벌어지는가?"와 같은 반사실적 사고를 유도한다
- 역사적 맥락을 활용한다 (Fisher, Neyman-Pearson, 1948 Streptomycin Trial 등)

```markdown
> **직관**: A/B 테스트에서 무작위 배정이 중요한 이유는 "비교 가능한 집단"을 만들기 위해서이다.
> 약 효과를 알고 싶은데 건강한 사람만 약을 먹고 아픈 사람은 안 먹었다면,
> 약 때문에 나아진 건지 원래 건강해서 나아진 건지 구분할 수 없다.
> 무작위 배정은 이런 교란(confounding)을 제거한다.
```

### 4. 왜 필요한가 (Why It Matters)

- 비즈니스 의사결정에서의 중요성을 설명한다
- 이 개념 없이 실험하면 발생하는 구체적 실패 사례를 제시한다
- 비용/리스크 관점에서 동기를 부여한다

```markdown
**왜 필요한가**: 전후 비교(before-after)만으로 시책 효과를 판단하면 계절성, 자연 회복,
외부 이벤트 등 교란 변수의 영향을 처치 효과로 오인할 수 있다. A/B 테스트는 동시에
두 집단을 비교하여 이러한 시간 교란을 통제한다.
```

### 5. 응용 분야 (Applications)

- 역학/의학과 IT/비즈니스 양쪽의 활용을 병행 제시한다
- IT 맥락에서는 구체적인 메트릭과 시나리오를 포함한다

```markdown
| 분야 | 활용 | 구체적 예시 |
|---|---|---|
| 임상시험 | 신약 효능 평가 | Phase III RCT에서 생존율 비교 |
| 테크 기업 | UI/UX 최적화 | 버튼 색상 변경의 CTR 영향 측정 |
| 마케팅 | 캠페인 효과 측정 | 이메일 제목줄 A/B 테스트 |
| 정책 | 프로그램 평가 | 교육 바우처의 학업 성취도 효과 (RCT) |
| 게임 | 밸런싱 | 보상 구조 변경의 리텐션 영향 |
```

### 6. 예시 (Examples)

- 가상의 실험 시나리오를 구체적 숫자와 함께 제시한다
- 효과 크기(effect size), 검정력(power), 표본 크기(sample size) 계산을 포함한다
- 역학 지표(RR, OR, RD, NNT)와 IT 지표(Lift, Uplift, Conversion Rate) 매핑을 활용한다

```markdown
| 역학 지표 | IT 지표 | 수식 |
|---|---|---|
| Relative Risk (RR) | Lift | $RR = p_T / p_C$ |
| Risk Difference (RD) | Uplift | $RD = p_T - p_C$ |
| Number Needed to Treat (NNT) | Number to Convert | $NNT = 1 / RD$ |
```

### 7. 코드 예시 (Code Examples)

- Python 코드로 구현한다
- 패키지: `scipy.stats`, `statsmodels`, `numpy`, `pandas`
- 표본 크기 계산, 검정, 신뢰구간, 시뮬레이션을 포함한다

```markdown
```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportions_ztest

# 표본 크기 계산
power_analysis = NormalIndPower()
n = power_analysis.solve_power(
    effect_size=0.05,  # Cohen's h
    alpha=0.05,
    power=0.80,
    alternative='two-sided'
)
print(f"그룹당 필요 표본 크기: {int(np.ceil(n))}")
```
```

### 8. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- 역학 ↔ IT 크로스 레퍼런스를 포함한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**선행 지식**

- [가설 검정 기초](../Statistics/2023-04-10_hypothesis.qmd)
- [역학 연구 설계](./Epidemiology/study_design.qmd)

**후속 주제**

- [Sequential Testing](./AB_test/advanced/sequential.qmd)
- [CUPED 분산 감소](./Advanced/cuped.qmd)

**다른 카테고리 연결**

- [GLM과 로지스틱 회귀](../Statistics/2026-03-07_glm.qmd) — 이진 지표 분석의 통계적 기반
- [MAB와 강화학습](../Agent/16-Agent/bandit.qmd) — 탐색-활용 트레이드오프
```

---

## 하위 카테고리별 추가 지침

### 역학 (Epidemiology/)

- 역학 고유 개념(교란, 효과 수정, 편향 유형)에 대해 IT 맥락 번역을 함께 제공한다
- 자체 `index.qmd`가 있으므로 새 포스트 추가 시 이 index도 업데이트한다
- 교재: `docs/book/epidemiology/` (Hernan, Woodward)

### A/B 테스트 (AB_test/)

- 기본 A/B 테스트와 고급 방법론(Sequential, Bayesian, A/A)을 구분한다
- 실무 체크리스트 형태의 포스트를 권장한다
- 메트릭 선정 → 표본 크기 → 실행 → 분석 → 의사결정 흐름을 따른다

### 인과추론 (Causal_inference/)

- Potential Outcomes 프레임워크를 기본으로 사용한다
- 관찰 데이터 방법론(PSM, DiD, IV, RDD, SCM)은 RCT와의 비교를 통해 설명한다
- HTE(이질적 처치효과) 하위 폴더는 CATE 추정 방법론을 다룬다

### MAB (MAB/)

- Classical(Epsilon-Greedy, UCB, Thompson Sampling)과 Advanced(Contextual, Non-stationary)를 구분한다
- A/B 테스트와의 비교(탐색 vs 활용 트레이드오프)를 항상 포함한다
- 시뮬레이션 코드로 알고리즘 성능을 비교한다
- Regret 분석을 수학적으로 제시한다

### 고급 주제 (Advanced/)

- 분산 감소(CUPED, CUPAC, Regression Adjustment)
- 실무 도전(Novelty Effect, Network Effect, SRM)
- 최신 연구 동향

### 플랫폼 (Platform/)

- 실험 플랫폼 아키텍처 설계
- 시스템 관점의 포스트이므로 Engineering 카테고리와의 크로스 레퍼런스를 활용한다

---

## 용어 매핑 테이블

포스트에서 역학 용어를 사용할 때는 IT 대응 용어를 함께 제시한다:

| 역학 (Epidemiology) | IT/비즈니스 | 비고 |
|---|---|---|
| Treatment/Exposure | Variant/Treatment | 처치 |
| Control | Control/Baseline | 대조군 |
| Outcome | Metric/KPI | 결과 변수 |
| Randomization | Random Assignment | 무작위 배정 |
| Blinding | - | IT에서는 해당 없음 (사용자는 배정을 모름) |
| Intention-to-Treat (ITT) | Intent-to-Treat | 배정 기준 분석 |
| Per-Protocol | As-Treated | 실제 노출 기준 분석 |
| Confounding | Confounding/Bias | 교란 |
| Effect Modification | Heterogeneous Treatment Effect (HTE) | 효과 수정/이질적 처치효과 |
| External Validity | Generalizability | 외적 타당성 |

---

## 교재 참조 매핑

| 주제 영역 | 교재 소스 경로 | 주요 교재 |
|---|---|---|
| 인과추론 | `docs/book/epidemiology/` | Hernan & Robins (Causal Inference: What If) |
| 역학 방법론 | `docs/book/epidemiology/` | Woodward (Epidemiology: Study Design and Data Analysis) |
| 실험 설계 | `docs/book/epidemiology/` | Schulz (CONSORT), Maxwell (실험 설계) |
| A/B 테스트 | `docs/book/epidemiology/` | Buisson (A/B Testing) |

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재의 Summary를 먼저 참조한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Hernan & Robins — Causal Inference: What If (2020) | `docs/book/epidemiology/Hernan-Causal-Inference-summary.md` | 인과추론, 반사실, DAG, IP 가중 |
| Buisson — Behavioral Data Analysis (2021) | `docs/book/epidemiology/Buisson-Behavioral-Data-Analysis-summary.md` | 행동 데이터 인과추론, A/B 테스트 |
| Schulz & Grimes — Essential Concepts in Clinical Research (2018) | `docs/book/epidemiology/Schulz-Clinical-Research-summary.md` | RCT 설계, 관찰역학 |
| Maxwell & Delaney — Designing Experiments (2004) | `docs/book/epidemiology/Maxwell-Designing-Experiments-summary.md` | 실험 설계, 모형 비교, ANOVA |
| Woodward — Epidemiology: Study Design and Data Analysis (2014) | `docs/book/epidemiology/Woodward-Epidemiology-summary.md` | 역학 연구 설계, 데이터 분석 |

**참조 절차**: Summary 읽기 → 키워드로 관련 챕터 특정 → Full MD에서 수식/정의 확인 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용
