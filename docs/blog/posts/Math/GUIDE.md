---
name: Math_GUIDE
type: category
version: 1.0
description: Math 카테고리 포스트 작성 규칙 — 응용 수학, 기하학적 직관, 시각화 중시
scope: docs/blog/posts/Math/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Math/index.qmd
book_sources:
  - docs/book/linear_algebra/
  - docs/book/statistics/
cross_references:
  - docs/blog/posts/Statistics/GUIDE.md
  - docs/blog/posts/Deep_Learning/GUIDE.md
  - docs/blog/posts/Machine_Learning/GUIDE.md
---

# Math 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Math 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **응용 수학 관점**: 순수 수학이 아닌 ML/DL/통계의 기초로서 수학을 다룬다
- **시각적 직관 중시**: 수식만으로 끝내지 않고 그래프, 기하학적 해석을 반드시 포함한다
- **한국어/영어 병기**: 핵심 용어는 `한국어(English)` 형태로 처음 등장 시 병기한다
- **교재 기반**: `docs/book/linear_algebra/` (Strang, Magnus), `docs/book/statistics/` (미적분 관련) 참조

---

## 포스트 콘텐츠 구조

Math 카테고리의 포스트는 다음 구조를 따른다. 주제에 따라 일부 섹션을 생략하거나 순서를 조정할 수 있으나, 가능한 한 이 흐름을 유지한다.

### 1. 정의 (Definition)

- 수학적 정의를 callout 블록으로 제시한다
- 기호(notation)를 정의 직후에 명시한다

```markdown
::: {.callout-note}
## 정의: 내적 (Inner Product)

벡터 공간 $V$ 위의 내적은 함수 $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$로,
다음 성질을 만족한다:

1. **대칭성**: $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$
2. **선형성**: $\langle a\mathbf{u} + b\mathbf{w}, \mathbf{v} \rangle = a\langle \mathbf{u}, \mathbf{v} \rangle + b\langle \mathbf{w}, \mathbf{v} \rangle$
3. **양정치성**: $\langle \mathbf{u}, \mathbf{u} \rangle \geq 0$, 등호는 $\mathbf{u} = \mathbf{0}$일 때만 성립
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 정의에서 파생되는 정리, 성질, 관계를 전개한다
- 증명은 핵심 아이디어를 중심으로 포함한다 (모든 세부 단계를 나열하지 않아도 됨)
- 다른 개념과의 연결을 명시한다 (예: "내적 → 직교성 → 정사영 → 최소제곱법")

### 3. 직관적 설명 (Intuitive Explanation)

- 기하학적 해석을 우선적으로 제시한다
- 2D/3D 시각화를 활용한다 (matplotlib, 다이어그램)
- "이것이 의미하는 바는..."으로 시작하는 단락을 포함한다

```markdown
> **기하학적 직관**: 내적 $\langle \mathbf{u}, \mathbf{v} \rangle = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$는
> 두 벡터가 얼마나 같은 방향을 가리키는지를 측정한다.
> 내적이 0이면 직교(수직)이고, 양수이면 비슷한 방향, 음수이면 반대 방향이다.
```

### 4. 왜 필요한가 (Why It Matters)

- 이 수학적 개념이 ML/DL/통계에서 어떤 역할을 하는지 설명한다
- "이 개념 없이는 ~을 이해할 수 없다" 형태로 동기를 부여한다
- 실무 문제와의 연결 고리를 제시한다

### 5. 응용 분야 (Applications)

- ML/DL/통계/공학에서의 구체적 활용을 테이블로 정리한다

```markdown
| 분야 | 활용 | 구체적 예시 |
|---|---|---|
| 머신러닝 | 유사도 측정 | 코사인 유사도 = 정규화된 내적 |
| 딥러닝 | Attention 메커니즘 | Query-Key 내적으로 관련도 계산 |
| 통계학 | 최소제곱법 | 잔차 벡터와 열공간의 직교성 |
| 신호처리 | 주파수 분석 | 푸리에 계수 = 신호와 기저함수의 내적 |
```

### 6. 예시 (Examples)

- 손계산 가능한 저차원(2D, 3D) 예시를 제시한다
- 단계별 풀이 과정을 보여준다
- 가능하면 기하학적 의미를 함께 설명한다

### 7. 코드 예시 (Code Examples)

- **2단계 구성**: (1) 순수 Python/최소 의존성으로 원리를 구현 → (2) NumPy/프레임워크로 실무 코드 제시
- 패키지: `numpy`, `sympy`, `matplotlib`, `torch` (필요 시)
- 시각화를 포함한다 (그래프, 벡터 플롯, 행렬 히트맵 등)

```markdown
#### Step 1: Low-level 구현 (원리 이해)

```python
# 순수 Python으로 내적 구현 — 원리를 직접 확인
def dot_product(u, v):
    """내적 = 대응하는 성분끼리 곱한 후 합산"""
    assert len(u) == len(v), "벡터 차원이 같아야 한다"
    return sum(u_i * v_i for u_i, v_i in zip(u, v))

def norm(v):
    """L2 노름 = 각 성분 제곱합의 제곱근"""
    return sum(x**2 for x in v) ** 0.5

import math

u = [3, 1]
v = [1, 2]
dp = dot_product(u, v)                          # 3*1 + 1*2 = 5
cos_theta = dp / (norm(u) * norm(v))             # 5 / (√10 * √5)
theta = math.degrees(math.acos(cos_theta))

print(f"내적: {dp}, 사잇각: {theta:.1f}도")
```

#### Step 2: NumPy 구현 (실무 활용)

```python
import numpy as np

u = np.array([3, 1])
v = np.array([1, 2])

dot_product = np.dot(u, v)
cos_theta = dot_product / (np.linalg.norm(u) * np.linalg.norm(v))
theta = np.degrees(np.arccos(cos_theta))

print(f"내적: {dot_product}, 사잇각: {theta:.1f}도")
```
```

### 8. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**선행 지식**

- [벡터의 기본](./linear_algebra/01.basic_vector.qmd)
- [노름과 내적](./linear_algebra/02.norm_dot-product.qmd)

**후속 주제**

- [직교성과 정사영](./linear_algebra/orthogonality.qmd)
- [고유값 분해](./linear_algebra/eigenvalue.qmd)

**다른 카테고리 연결**

- [최소제곱 회귀](../Statistics/regression.qmd) — 내적의 통계적 응용
- [Attention 메커니즘](../Deep_Learning/NLP/attention.qmd) — 내적의 딥러닝 응용
```

---

## 하위 카테고리별 추가 지침

### 함수 (function/)

- 스칼라 함수 → 벡터 함수 → 합성함수 순서로 복잡도를 높인다
- 각 함수 유형의 정의역/공역/치역을 명확히 표기한다
- 그래프(2D 곡선, 3D 곡면, 등고선)를 반드시 포함한다

### 선형대수 (linear_algebra/)

- MIT 18.06 시리즈(`mit-*.qmd`)와 개념 포스트(`01.*.qmd`)가 공존한다
- 새 포스트는 개념 포스트 시리즈에 추가한다 (MIT 시리즈는 강의 노트)
- 행, 열, 행렬 관점(row picture, column picture, matrix picture)을 병행 설명한다
- 파일명 패턴: `번호.토픽명.qmd` (예: `15.eigenvalue.qmd`)

### 최적화 (Optimization — 계획됨)

- 현재 index.qmd에 placeholder로만 존재한다
- 경사하강법, 볼록 최적화, 라그랑주 승수법 등을 다룰 예정이다
- 통계(MLE)와 딥러닝(역전파)과의 연결을 강조한다

---

## 수식 작성 규칙

- 벡터는 굵은 소문자($\mathbf{v}$), 행렬은 굵은 대문자($\mathbf{A}$)로 표기한다
- 스칼라는 일반 소문자($a, b, c$) 또는 그리스 문자($\alpha, \lambda$)를 사용한다
- 집합은 blackboard bold($\mathbb{R}^n$, $\mathbb{C}$)를 사용한다
- 전치는 $\top$ 기호를 사용한다: $\mathbf{A}^\top$ (T 위첨자가 아닌 $\top$)
- 기하학적 의미가 있는 수식에는 반드시 시각화를 동반한다

---

## 교재 참조 매핑

| 주제 영역 | 교재 소스 경로 | 주요 교재 |
|---|---|---|
| 선형대수 | `docs/book/linear_algebra/` | Strang (Introduction to Linear Algebra) |
| 행렬 미분 | `docs/book/linear_algebra/` | Magnus (Matrix Differential Calculus), Matrix Cookbook |
| 미적분/해석 | `docs/book/statistics/` | Casella & Berger (수리통계 내 부록) |

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재의 Summary를 먼저 참조한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Strang — Introduction to Linear Algebra (4th Ed.) | `docs/book/linear_algebra/Strang-IntroLinearAlgebra-summary.md` | 벡터, 행렬, 고유값, SVD |
| Strang — Linear Algebra and Its Applications | `docs/book/linear_algebra/Strang-LinearAlgebraApplications-summary.md` | 응용 선형대수 |
| Magnus & Neudecker — Matrix Differential Calculus (3rd Ed.) | `docs/book/linear_algebra/Magnus-MatrixDifferentialCalculus-summary.md` | 행렬 미분, 벡터화, 크로네커 곱 |
| Matrix Cookbook | `docs/book/linear_algebra/Petersen-MatrixCookbook-summary.md` | 행렬 공식 레퍼런스 |

**참조 절차**: Summary 읽기 → 키워드로 관련 챕터 특정 → Full MD에서 수식/정의 확인 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용
