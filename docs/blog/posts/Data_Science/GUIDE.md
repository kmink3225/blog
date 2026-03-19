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

### 3. 직관적 설명 (Intuitive Explanation)

- 비즈니스 관점에서 왜 이 과정이 필요한지 설명한다
- 실패 사례/성공 사례를 통해 중요성을 전달한다

```markdown
> **직관**: EDA는 "데이터와의 첫 대화"이다.
> 환자를 진단하기 전에 문진하는 것처럼, 모델을 만들기 전에 데이터의 상태를 파악해야 한다.
> EDA 없이 모델링하면 잘못된 가정 위에 집을 짓는 것과 같다.
```

### 4. 왜 필요한가 (Why It Matters)

- 이 단계를 건너뛰면 발생하는 구체적 문제를 제시한다
- 비즈니스 의사결정에서의 역할을 설명한다
- ROI, 효율성 관점에서 동기를 부여한다

### 5. 응용 분야 (Applications)

```markdown
| 분야 | 활용 | 구체적 예시 |
|---|---|---|
| 마케팅 | 고객 분석 | RFM 세분화, 퍼널 분석 |
| 제조 | 공정 최적화 | 센서 데이터 기반 불량 예측 |
| 금융 | 리스크 관리 | 이상 거래 탐지 |
| 의료 | 임상 연구 | 환자 코호트 분석, 생존 분석 |
| 물류 | 수요 예측 | 재고 최적화 |
```

### 6. 예시 (Examples)

- end-to-end 프로젝트 시나리오를 제시한다
- 문제 정의 → 데이터 → 분석 → 결론 흐름을 따른다
- 의사결정 포인트를 강조한다

### 7. 코드 예시 (Code Examples)

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

### 8. 관련 주제 (Related Topics)

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

---

## 다른 카테고리와의 관계

Data Science는 허브 카테고리로서, 세부 기술은 다른 카테고리에서 깊이 있게 다룬다:

```
Data Science (프로세스, 방법론, 통합)
  ├── Statistics (이론적 기반, 추론)
  ├── Machine Learning (예측 모델)
  ├── Deep Learning (신경망 모델)
  ├── Engineering (데이터 파이프라인, 배포)
  ├── Experimentation (실험 설계, A/B 테스트)
  └── Governance (데이터 품질, 표준화)
```

포스트에서 특정 기술을 깊이 다룰 때는 해당 카테고리로의 크로스 링크를 제공하고, Data Science 포스트 자체는 통합적 관점과 프로세스에 집중한다.
