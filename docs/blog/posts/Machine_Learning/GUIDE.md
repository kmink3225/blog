---
name: Machine_Learning_GUIDE
type: category
version: 1.0
description: LOAD when writing posts about classification, regression, ensemble methods, unsupervised learning, or model evaluation. Covers algorithm theory with mathematical foundations and scikit-learn implementations.
scope: docs/blog/posts/Machine_Learning/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Machine_Learning/index.qmd
book_sources:
  - docs/book/machine_learning/
cross_references:
  - docs/blog/posts/Statistics/GUIDE.md
  - docs/blog/posts/Deep_Learning/GUIDE.md
  - docs/blog/posts/Data_Science/GUIDE.md
  - docs/blog/posts/Experimentation/GUIDE.md
---

# Machine Learning 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Machine Learning 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **수학 + 코드 하이브리드**: 알고리즘의 수학적 원리와 scikit-learn/XGBoost 구현을 병행한다
- **커리큘럼 기반**: index.qmd가 4단계 학습 경로(기초 → 핵심 → 심화 → 엔지니어링)를 제시한다
- **알고리즘 비교 중시**: 유사한 알고리즘 간 차이점을 테이블로 정리한다
- **해석 가능성 강조**: SHAP, LIME 등 모델 해석 도구를 적극 활용한다
- **종단 데이터 연계**: Statistics/Deep_Learning 카테고리와 크로스 레퍼런스가 많다

---

## 포스트 콘텐츠 구조

### 1. 정의 (Definition)

- 알고리즘의 수학적 정의를 callout 블록으로 제시한다
- 학습 목표(목적 함수)를 명시한다

```markdown
::: {.callout-note}
## 정의: Random Forest

Random Forest는 $B$개의 독립적인 결정 트리의 예측을 집계(aggregation)하는 앙상블 기법이다.

$$
\hat{f}_{RF}(\mathbf{x}) = \frac{1}{B}\sum_{b=1}^B T_b(\mathbf{x})
$$

- $T_b$: $b$번째 부트스트랩 표본 + 랜덤 피처 부분집합으로 학습한 결정 트리
- 핵심 아이디어: Bagging + Feature Randomness → 분산(variance) 감소
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 알고리즘의 학습 과정을 단계별로 분해한다
- 목적 함수(loss function)와 최적화 방법을 명시한다
- Bias-Variance Trade-off 관점에서 알고리즘을 분석한다
- 하이퍼파라미터의 역할과 영향을 설명한다
- 추상적이거나 이해하기 어려운 개념에는 비유, 결정 경계 시각화 등 직관적 설명을 적재적소에 포함한다 (필요시 별도 섹션으로 분리 가능)
- 각 개념 또는 원리에 데이터 사이언스 실무에 어떻게 적용될 수 있는지 설명한다

### 3. 왜 필요한가 (Why It Matters)

- 단순 모델의 한계와 이를 보완하는 방식을 설명한다
- 실무에서 이 알고리즘이 선호되는 이유를 제시한다
- 대안 알고리즘과의 비교를 포함한다

### 4. 응용 분야 (Applications)

```markdown
| 분야 | 활용 | 구체적 예시 |
|---|---|---|
| 금융 | 신용 평가 | 대출 부도 예측 (분류) |
| 의료 | 진단 보조 | 환자 위험도 분류 |
| 마케팅 | 고객 세분화 | 이탈 예측, 타겟팅 |
| 제조 | 품질 관리 | 불량품 탐지 (이상 탐지) |
| 추천 | 개인화 | 협업 필터링 |
```

### 5. 예시 (Examples)

- 소규모 데이터셋으로 알고리즘 동작을 단계별로 보여준다
- 결정 경계, 학습 곡선 등 시각화를 포함한다
- 하이퍼파라미터 변화에 따른 결과 차이를 보여준다

### 6. 코드 예시 (Code Examples)

- **2단계 구성**: (1) 순수 Python/NumPy로 알고리즘 원리를 구현 → (2) scikit-learn 등 프레임워크로 실무 코드 제시
- 패키지: `numpy` (low-level), `scikit-learn`, `xgboost`, `lightgbm`, `pandas`, `matplotlib`, `shap`
- 전처리 → 학습 → 평가 → 해석 파이프라인을 따른다

```markdown
#### Step 1: NumPy 구현 (원리 이해)

```python
import numpy as np
from collections import Counter

class SimpleDecisionStump:
    """단일 분할 결정 트리 — Random Forest의 기본 빌딩 블록"""
    def __init__(self):
        self.feature_idx = None
        self.threshold = None
        self.left_label = None
        self.right_label = None

    def fit(self, X, y):
        best_gini = float('inf')
        for feat in range(X.shape[1]):
            thresholds = np.unique(X[:, feat])
            for t in thresholds:
                left_mask = X[:, feat] <= t
                right_mask = ~left_mask
                gini = self._weighted_gini(y[left_mask], y[right_mask], len(y))
                if gini < best_gini:
                    best_gini = gini
                    self.feature_idx = feat
                    self.threshold = t
                    self.left_label = Counter(y[left_mask]).most_common(1)[0][0]
                    self.right_label = Counter(y[right_mask]).most_common(1)[0][0]

    def _weighted_gini(self, left_y, right_y, n):
        def gini(y):
            if len(y) == 0: return 0
            counts = np.bincount(y)
            probs = counts / len(y)
            return 1 - np.sum(probs ** 2)
        return (len(left_y) * gini(left_y) + len(right_y) * gini(right_y)) / n

    def predict(self, X):
        return np.where(X[:, self.feature_idx] <= self.threshold,
                        self.left_label, self.right_label)
```

#### Step 2: scikit-learn 구현 (실무 활용)

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_classification
import shap

# 데이터 생성
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# 모델 학습
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
scores = cross_val_score(rf, X, y, cv=5, scoring='f1')
print(f"F1 Score: {scores.mean():.3f} ± {scores.std():.3f}")

# SHAP 해석
rf.fit(X, y)
explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X[:100])
shap.summary_plot(shap_values[1], X[:100])
```
```

### 7. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**선행 지식**

- [확률과 베이즈 정리](../Statistics/06-probability.qmd)
- [선형대수 기초](../Math/linear_algebra/mit-01-1-gilbert-strang-vectors-overview.qmd)

**후속 주제**

- [XGBoost + 시간 피처 공학](./22-mixed-model-ml-xgboost.qmd)
- [모델 해석 (SHAP, LIME)](./interpretability.qmd)

**다른 카테고리 연결**

- [신경망과 딥러닝](../Deep_Learning/NLP/1.nlp_overview.qmd) — ML → DL 확장
- [A/B 테스트와 모델 평가](../Experimentation/01-ab-test-mechanism.qmd) — 모델 배포 후 실험
```

---

## 자주 발생하는 품질 문제

<fix-algorithm-without-tradeoff>
WRONG: 알고리즘 설명만 나열하고 끝냄
CORRECT: bias-variance tradeoff, 시간/공간 복잡도, 적합한 데이터 유형까지 포함
</fix-algorithm-without-tradeoff>

<fix-evaluation-without-context>
WRONG: "accuracy 95%"라고만 보고
CORRECT: 불균형 데이터 여부, 적절한 메트릭 선택 근거, baseline 비교를 함께 제시
</fix-evaluation-without-context>

---

## 알고리즘 분류 체계

포스트 작성 시 알고리즘의 위치를 다음 체계 내에서 명시한다:

```
Supervised Learning
├── Regression: Linear, Polynomial, Ridge, Lasso, Elastic Net
├── Classification: Logistic, Naive Bayes, KNN, SVM, Decision Tree
└── Ensemble: Bagging (RF), Boosting (AdaBoost, GB, XGBoost, LightGBM, CatBoost), Stacking

Unsupervised Learning
├── Clustering: K-Means, Hierarchical, DBSCAN, GMM
├── Dimensionality Reduction: PCA, t-SNE, UMAP
└── Anomaly Detection: Isolation Forest, One-Class SVM, LOF

Semi-Supervised / Self-Supervised / Transfer Learning
```

---

## 알고리즘 비교 테이블 템플릿

새 알고리즘 포스트에는 유사 알고리즘과의 비교 테이블을 포함한다:

```markdown
| 기준 | Random Forest | XGBoost | LightGBM |
|---|---|---|---|
| 앙상블 방식 | Bagging | Boosting | Boosting |
| 트리 성장 | Level-wise | Level-wise | Leaf-wise |
| 과적합 제어 | max_depth, min_samples | reg_alpha, reg_lambda | num_leaves |
| 학습 속도 | 보통 | 느림 | 빠름 |
| 결측치 처리 | 불가 | 자동 | 자동 |
| 해석 가능성 | Feature Importance | SHAP | SHAP |
```

---

## 하위 주제별 추가 지침

### 종단 데이터 ML (12, 21~24번 파일)

- Statistics/LDA 시리즈, Deep_Learning 종단 데이터 파일과 크로스 레퍼런스된다
- RSF, XGBoost + 시간 피처, HMM, Lasso/Elastic Net을 다룬다
- 통계 모델(Mixed Model)과의 선택 기준을 항상 포함한다
- 파일명 패턴: `번호-mixed-model-ml-토픽.qmd`

### 프레임워크 튜토리얼 (PyTorch, TensorFlow)

- 텐서 연산, GPU 활용, 자동 미분 등 기본 조작을 다룬다
- Deep_Learning 카테고리의 모델 구현을 위한 선행 지식으로 위치한다

### 모델 평가 및 해석

- 메트릭(F1, AUC-ROC, RMSE 등)의 수학적 정의와 선택 기준을 제시한다
- SHAP, LIME, PDP 등 해석 도구의 원리와 코드를 포함한다
- Data_Science/performance-index.qmd와 연계한다

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재를 **논리적 뼈대**로 활용한다. 교재의 체계를 참고하되, agent의 최신 사전지식으로 outdated된 내용은 수정하고 부족한 부분은 보완한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Hastie et al. — Elements of Statistical Learning (2009) | `docs/book/machine_learning/Hastie-ESL-summary.md` | 지도/비지도학습 이론, 정규화, 앙상블, SVM |
| Bishop — Pattern Recognition and Machine Learning (2006) | `docs/book/machine_learning/Bishop-PRML-summary.md` | 베이지안 ML, 확률적 모델링, EM, 커널 |
| James et al. — Introduction to Statistical Learning (2021) | `docs/book/machine_learning/James-ISLR-summary.md` | ML 입문, R 실습, 트리, SVM, 딥러닝 기초 |
| Murphy — Probabilistic ML: Introduction (2022) | `docs/book/machine_learning/Murphy-PMLIntro-summary.md` | 확률론적 ML 기초, 딥러닝, 비지도학습 |
| Murphy — Probabilistic ML: Advanced (2023) | `docs/book/machine_learning/Murphy-PMLAdvanced-summary.md` | 추론, 생성모델, 인과추론, 강화학습 |

**활용 절차**: Summary 읽기 → 논리 구조 파악 → Full MD에서 수식/정의 확인 → 교재 내용 중 유효한 부분은 유지, outdated된 부분은 agent 지식으로 수정·보완 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용

---

## 경계 정의

<boundaries>
CAN:
- 교재 기반 알고리즘 유도 (목적함수 → 최적화 → 해)
- 알고리즘 간 비교표 (복잡도, 가정, 적합 상황)
- scikit-learn + low-level NumPy 구현 병행
- 실무 적용 맥락 (데이터 특성에 따른 알고리즘 선택 근거)

CANNOT:
- 알고리즘을 단순 API 호출로만 소개 (수학적 원리 없이 sklearn 코드만 나열)
- 수학적 근거 없이 "이 알고리즘이 좋다" 주장 (벤치마크·이론적 분석 없는 추천 금지)
</boundaries>
