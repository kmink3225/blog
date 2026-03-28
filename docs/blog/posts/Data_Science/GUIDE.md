---
name: Data_Science_GUIDE
type: category
version: 1.0
description: >
  LOAD when writing posts about (1) CRISP-DM workflow, EDA, feature engineering, model deployment,
  MLOps, or AI engineering — end-to-end pipeline methodology; OR (2) domain application projects
  that integrate Statistics, ML, DL, Engineering tools to solve real business/domain problems
  (e.g., PCR signal analysis, clinical diagnostics, demand forecasting).
scope: docs/blog/posts/Data_Science/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Data_Science/index.qmd
book_sources:
  - docs/book/data_science/
cross_references:
  - docs/blog/posts/Statistics/GUIDE.md
  - docs/blog/posts/Machine_Learning/GUIDE.md
  - docs/blog/posts/Deep_Learning/GUIDE.md
  - docs/blog/posts/Engineering/GUIDE.md
  - docs/blog/posts/Experimentation/GUIDE.md
  - docs/blog/posts/Governance/GUIDE.md
  - docs/blog/posts/Surveilance/GUIDE.md
---

# Data Science 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Data Science 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **통합자(integrator) 관점**: Statistics, ML, DL, Engineering을 아우르는 메타 카테고리이다
- **방법론 + 프로세스 중심**: 개별 알고리즘보다 문제 정의 → 데이터 수집 → 분석 → 배포의 전체 흐름을 다룬다
- **비즈니스 문제 연결**: 기술적 방법론을 비즈니스 가치와 연결하여 설명한다
- **CRISP-DM 프레임워크**: 데이터 과학 프로젝트의 표준 프로세스를 따른다
- **다른 카테고리로의 허브**: 세부 기술은 Statistics, ML, DL, Engineering 카테고리를 참조한다

---

## 포스트 콘텐츠 구조

### 1. 정의 (Definition)

- 개념/방법론의 정의를 callout 블록으로 제시한다
- 유사 개념과의 구분을 명확히 한다 (예: Analysis vs Analytics, AI vs ML vs DL)

```markdown
::: {.callout-note}
## 정의: EDA (Exploratory Data Analysis)

탐색적 데이터 분석(EDA)은 데이터의 구조, 패턴, 이상치, 변수 간 관계를 시각화와 요약 통계를
통해 파악하는 분석 과정이다.

- 목적: 가설 생성, 데이터 품질 확인, 모델링 전략 수립
- 구분: EDA(탐색) ≠ CDA(확증적 데이터 분석, 가설 검정)
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 방법론의 이론적 배경과 단계별 프로세스를 설명한다
- 데이터 과학의 전체 파이프라인 내에서의 위치를 명시한다
- Statistics/ML/DL/Engineering 간 역할 분담을 설명한다
- 추상적이거나 이해하기 어려운 개념에는 비유, 실패/성공 사례 등 직관적 설명을 적재적소에 포함한다 (필요시 별도 섹션으로 분리 가능)
- 각 개념 또는 원리에 데이터 사이언스 실무에 어떻게 적용될 수 있는지 설명한다

### 3. 왜 필요한가 (Why It Matters)

- 이 단계를 건너뛰면 발생하는 구체적 문제를 제시한다
- 비즈니스 의사결정에서의 역할을 설명한다
- ROI, 효율성 관점에서 동기를 부여한다

### 4. 응용 분야 (Applications)

```markdown
| 분야 | 활용 | 구체적 예시 |
|---|---|---|
| 마케팅 | 고객 분석 | RFM 세분화, 퍼널 분석 |
| 제조 | 공정 최적화 | 센서 데이터 기반 불량 예측 |
| 금융 | 리스크 관리 | 이상 거래 탐지 |
| 의료 | 임상 연구 | 환자 코호트 분석, 생존 분석 |
| 물류 | 수요 예측 | 재고 최적화 |
```

### 5. 예시 (Examples)

- end-to-end 프로젝트 시나리오를 제시한다
- 문제 정의 → 데이터 → 분석 → 결론 흐름을 따른다
- 의사결정 포인트를 강조한다

### 6. 코드 예시 (Code Examples)

- **2단계 구성**: (1) 순수 Python으로 원리를 구현 → (2) pandas/seaborn 등 프레임워크로 실무 코드 제시
- 패키지: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- 데이터 로드 → EDA → 전처리 → 시각화 파이프라인을 따른다

```markdown
#### Step 1: 순수 Python 구현 (원리 이해)

```python
# 순수 Python으로 상관계수 구현 — 공식을 직접 확인
def mean(xs):
    return sum(xs) / len(xs)

def pearson_correlation(x, y):
    """피어슨 상관계수: r = Σ(xi - x̄)(yi - ȳ) / √(Σ(xi - x̄)² · Σ(yi - ȳ)²)"""
    assert len(x) == len(y)
    x_mean, y_mean = mean(x), mean(y)
    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denom_x = sum((xi - x_mean) ** 2 for xi in x) ** 0.5
    denom_y = sum((yi - y_mean) ** 2 for yi in y) ** 0.5
    return numerator / (denom_x * denom_y)

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
print(f"Pearson r = {pearson_correlation(x, y):.4f}")
```

#### Step 2: pandas/seaborn 구현 (실무 활용)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드 및 기본 탐색
df = pd.read_csv("data.csv")
print(df.info())
print(df.describe())

# 결측치 시각화
sns.heatmap(df.isnull(), cbar=True, yticklabels=False)
plt.title("Missing Value Pattern")
plt.show()

# 변수 간 상관관계
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Matrix")
plt.show()
```
```

### 7. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**세부 기술 (다른 카테고리 참조)**

- [가설 검정](../Statistics/2023-04-10_hypothesis.qmd) — CDA의 통계적 기반
- [분류 알고리즘](../Machine_Learning/classification.qmd) — 예측 모델링
- [데이터 파이프라인](../Engineering/Data_Engineering/airflow/) — 데이터 엔지니어링

**관련 개념**

- [A/B 테스트](../Experimentation/01-ab-test-mechanism.qmd) — 데이터 기반 의사결정
- [데이터 거버넌스](../Governance/1.basis.qmd) — 데이터 품질 관리
```

---

## 포스트 유형별 가이드

### 방법론/프로세스 포스트

- CRISP-DM 6단계(Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment)를 기준으로 설명한다
- 각 단계의 산출물(deliverable)을 명시한다

### 개념 비교 포스트

- Statistics vs ML vs DL vs AI 등 분야 간 관계를 설명한다
- 비교 테이블과 벤 다이어그램을 활용한다
- 각 분야의 독립적 정체성과 실무에서의 통합을 균형 있게 다룬다

### 성능 지표 포스트

- 수학적 정의 → 직관적 해석 → 선택 기준 순서를 따른다
- 분류/회귀/클러스터링/랭킹별 메트릭을 구분한다
- 지표 간 trade-off를 설명한다 (예: Precision vs Recall)

### 도메인 응용 프로젝트 포스트

- 특정 도메인 문제를 해결하기 위해 여러 tool(Statistics, ML, Engineering 등)을 통합하여 사용하는 사례를 다룬다
- **구조**: 도메인 배경 → 문제 정의 → 데이터 탐색 → 방법론 선택 및 적용 → 결과 해석 → 비즈니스 인사이트
- 기술 선택의 근거(왜 이 방법을 이 도메인에 적용했는가)를 반드시 설명한다
- 도메인 지식(예: PCR 증폭 원리, 임상 QC 기준)과 데이터 과학 기법을 연결하여 서술한다
- 크로스 링크: 관련 도메인 카테고리(Surveilance, Governance 등)와 기법 카테고리(Statistics, ML 등)를 모두 참조한다

---

## 다른 카테고리와의 관계

Data Science는 허브 카테고리로서, 세부 기술은 다른 카테고리에서 깊이 있게 다룬다:

```
Data Science (프로세스, 방법론, 통합, 도메인 응용)
  ├── Statistics (이론적 기반, 추론)
  ├── Machine Learning (예측 모델)
  ├── Deep Learning (신경망 모델)
  ├── Engineering (데이터 파이프라인, 배포)
  ├── Experimentation (실험 설계, A/B 테스트)
  ├── Governance (데이터 품질, 표준화)
  └── Surveilance (규제/도메인 지식 — PCR, 의료기기 등 응용 시 참조)
```

포스트에서 특정 기술을 깊이 다룰 때는 해당 카테고리로의 크로스 링크를 제공하고, Data Science 포스트 자체는 통합적 관점과 프로세스에 집중한다.

---

## 흔한 실수 교정 (Fix Blocks)

<fix-tool-without-methodology>

**WRONG**: pandas/sklearn 코드만 나열

```python
# BAD — 코드만 있고 왜 이 방법을 택했는지 설명이 없다
df = df.dropna()
df['price_log'] = np.log1p(df['price'])
model = RandomForestRegressor()
model.fit(X_train, y_train)
```

**CORRECT**: 방법론적 근거(왜 이 전처리/피처를 선택했는가) → 코드

```markdown
## 결측치 처리 전략

price 변수의 결측은 전체의 2.3%이며, MCAR 패턴을 보인다 (Little's test p=0.42).
비율이 낮고 무작위 결측이므로 완전 제거(listwise deletion)를 선택한다.
만약 MAR이었다면 다중 대체(MICE)를 사용해야 한다 (Huyen, 2022, Ch.4).

price의 오른쪽 꼬리가 길어(skewness=3.2) log 변환을 적용한다.
이를 통해 트리 모델의 분할 효율이 개선되고, 선형 모델에서도 잔차 정규성에 가까워진다.
```

```python
# 결측 비율 확인 후 완전 제거
print(f"price 결측 비율: {df['price'].isna().mean():.3f}")
df = df.dropna(subset=['price'])

# skewness 기반 log 변환
print(f"변환 전 skewness: {df['price'].skew():.2f}")
df['price_log'] = np.log1p(df['price'])
print(f"변환 후 skewness: {df['price_log'].skew():.2f}")
```

</fix-tool-without-methodology>

<fix-isolated-step>

**WRONG**: EDA만 독립적으로 설명

```markdown
## EDA
히스토그램을 그리고, 상관행렬을 확인하고, 이상치를 박스플롯으로 본다.
```

**CORRECT**: CRISP-DM 워크플로 내에서 EDA의 위치와 전후 단계 연결

```markdown
## EDA — CRISP-DM Phase 2: Data Understanding

### 이전 단계와의 연결
Business Understanding에서 정의한 핵심 질문:
"어떤 숙소 특성이 가격 프리미엄을 만드는가?"
이 질문에 답하기 위해 EDA에서 확인할 사항을 정리한다.

### EDA 수행
1. **타겟 분포**: price의 분포 → 변환 필요성 판단 (→ Data Preparation으로 연결)
2. **피처-타겟 관계**: room_type별 가격 차이 → 모델링 전략에 반영 (→ Modeling으로 연결)
3. **데이터 품질**: 결측 패턴, 이상치 → 전처리 전략 수립 (→ Data Preparation으로 연결)

### 다음 단계로의 인사이트
EDA 결과, neighbourhood_group과 room_type이 가격의 주요 설명 변수임을 확인했다.
Data Preparation 단계에서 이 변수들의 인코딩 전략을 결정한다.
```

</fix-isolated-step>

---

## 범위 정의 (Boundaries)

<boundaries>

### CAN (이 카테고리에서 다루는 것)

- 교재 기반 방법론 설명 (CRISP-DM, ML 시스템 설계, 비즈니스 프레이밍)
- 실무 파이프라인: 데이터 수집 → 전처리 → 모델링 → 배포 → 모니터링 전체 흐름
- 비즈니스 맥락 연결: 기술적 선택이 비즈니스 가치에 미치는 영향
- 도구 비교: pandas vs polars, sklearn vs XGBoost, MLflow vs W&B 등 방법론적 관점의 도구 선택 가이드
- **도메인 응용 프로젝트**: 특정 도메인 문제를 Statistics/ML/DL/Engineering 도구를 통합해 해결하는 실전 분석 사례 (예: RT-PCR 신호 분석, 진단 알고리즘 개발)

### CANNOT (이 카테고리에서 하지 않는 것)

- 방법론적 근거 없이 코드만 나열 (→ `<fix-tool-without-methodology>` 참조)
- 비즈니스 목적 없는 기술적 EDA만 수행 (→ `<fix-isolated-step>` 참조)

</boundaries>

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재를 **논리적 뼈대**로 활용한다. 교재의 체계를 참고하되, agent의 최신 사전지식으로 outdated된 내용은 수정하고 부족한 부분은 보완한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Chip Huyen — AI Engineering (2025) | `docs/book/data_science/Huyen-AIEngineering-summary.md` | LLM 시스템, RAG, Agent, 평가, 배포 |
| Chip Huyen — Designing ML Systems (2022) | `docs/book/data_science/Huyen-DesigningMLSystems-summary.md` | ML 시스템 설계, 데이터, 배포, 모니터링 |
| Provost & Fawcett — Data Science for Business (2013) | `docs/book/data_science/Provost-DataScienceBusiness-summary.md` | 비즈니스 관점 DS, 모델 평가, Expected Value |

**활용 절차**: Summary 읽기 → 논리 구조 파악 → Full MD에서 수식/정의 확인 → 교재 내용 중 유효한 부분은 유지, outdated된 부분은 agent 지식으로 수정·보완 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용
