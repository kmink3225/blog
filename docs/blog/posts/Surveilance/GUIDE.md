---
name: Surveilance_GUIDE
type: category
version: 1.0
description: Surveilance 카테고리 포스트 작성 규칙 — FDA/EMA 규제, 인허가, BibTeX 참고문헌
scope: docs/blog/posts/Surveilance/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Surveilance/index.qmd
book_sources: []
cross_references:
  - docs/blog/posts/Statistics/GUIDE.md
  - docs/blog/posts/Deep_Learning/GUIDE.md
  - docs/blog/posts/Data_Science/GUIDE.md
  - docs/blog/posts/Governance/GUIDE.md
---

# Surveilance 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Surveilance 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **규제/인허가 중심**: FDA, EMA, MFDS 등 의료기기 규제 체계를 다룬다
- **사례 기반**: 실제 승인 사례와 규제 문서를 분석한다
- **참고문헌(BibTeX) 사용**: `references.bib`로 학술 문헌을 관리한다
- **기관별 구성**: SGS, FDA, DHF 등 규제 기관/프레임워크 단위로 포스트를 분류한다
- **파일명 패턴**: `번호-regulation-토픽.qmd` (예: `0-regulation-basic.qmd`)

---

## 포스트 콘텐츠 구조

### 1. 정의 (Definition)

- 규제 용어의 공식 정의를 callout 블록으로 제시한다
- 규제 문서 원문을 인용한다

```markdown
::: {.callout-note}
## 정의: SaMD (Software as a Medical Device)

의료기기의 일부가 아닌, 그 자체로 하나 이상의 의료 목적을 수행하도록 의도된 소프트웨어이다.

> "Software intended to be used for one or more medical purposes that perform
> these purposes without being part of a hardware medical device."
> — IMDRF SaMD Working Group, 2013

- FDA 분류: Class I / II / III (위험도 기반)
- 국내: MFDS 의료기기 소프트웨어 허가 심사 가이드라인
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 규제 프레임워크의 구조와 논리를 설명한다
- 위험 분류 체계, 심사 경로, 필수 요건을 정리한다
- 규제 기관별 차이점을 비교한다

### 3. 직관적 설명 (Intuitive Explanation)

- 규제의 목적(환자 안전)을 중심으로 설명한다
- 규제 없는 상황의 위험성을 예시로 제시한다

```markdown
> **직관**: 의료 AI 규제는 "제품이 안전하고 효과적인지 증명하라"는 요구이다.
> 자동차가 출시 전 충돌 테스트를 거치는 것처럼,
> 의료 AI도 임상적 성능(민감도, 특이도)과 안전성(편향, 실패 모드)을 입증해야 한다.
```

### 4. 왜 필요한가 (Why It Matters)

- 규제 미준수 시 법적/비즈니스 리스크를 제시한다
- 승인 전략 수립의 중요성을 강조한다
- AI/ML 기반 의료기기의 특수한 규제 도전을 설명한다

### 5. 응용 분야 (Applications)

```markdown
| 제품 유형 | 규제 경로 | 구체적 예시 |
|---|---|---|
| 영상 진단 AI | FDA 510(k) / De Novo | 흉부 X-ray 폐렴 탐지 |
| 병리 AI | FDA De Novo | 디지털 병리 슬라이드 분석 |
| 임상 의사결정 지원 | CDS 면제 여부 판단 | 약물 상호작용 알림 |
| IVD 소프트웨어 | FDA 510(k) | RT-PCR 결과 해석 |
| 웰니스 앱 | 의료기기 비해당 | 운동 추적, 수면 모니터링 |
```

### 6. 예시 (Examples)

- 실제 FDA/EMA 승인 사례를 분석한다
- 승인 전략(predicate device 선정, 임상 데이터 구성)을 단계별로 보여준다
- 승인 실패 사례에서의 교훈을 포함한다

### 7. 코드 예시 (Code Examples — Optional)

- 성능 검증(민감도, 특이도, ROC 곡선) 코드를 포함한다
- 시그모이드 피팅, PCR 곡선 분석 등 도메인 특화 분석 코드를 포함한다

```markdown
```python
from sklearn.metrics import roc_curve, auc, confusion_matrix
import matplotlib.pyplot as plt

# 모델 성능 평가 (규제 제출용)
fpr, tpr, thresholds = roc_curve(y_true, y_score)
roc_auc = auc(fpr, tpr)

# 민감도/특이도 계산
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
sensitivity = tp / (tp + fn)  # 민감도 (recall)
specificity = tn / (tn + fp)  # 특이도

print(f"AUC: {roc_auc:.3f}")
print(f"Sensitivity: {sensitivity:.3f}, Specificity: {specificity:.3f}")
```
```

### 8. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**카테고리 내 연결**

- [의료 AI 규제의 본질](./0-regulation-basic.qmd)
- [승인 전략](./1-regulation-approval-spectrum.qmd)
- [FDA SW Validation](./2022-12-10_FDA_sw_general_guidance/index.qmd)

**다른 카테고리 연결**

- [모델 성능 지표](../Data_Science/performance-index.qmd) — 규제 제출용 성능 평가
- [데이터 거버넌스](../Governance/1.basis.qmd) — 데이터 품질 관리 (규제 요건)
- [통계적 가설 검정](../Statistics/2023-04-10_hypothesis.qmd) — 임상 성능 검증의 통계적 기반
```

---

## YAML 헤더 특이사항

Surveilance 카테고리는 참고문헌 관리를 위해 `bibliography` 필드를 사용한다:

```yaml
---
title: "제목"
subtitle: "부제목"
description: |
  설명
categories:
  - AI
  - Surveilance
  - Regulation
author: Kwangmin Kim
date: MM/DD/YYYY
execute:
  eval: false
bibliography: references.bib
---
```

- `references.bib`는 카테고리 루트(`docs/blog/posts/Surveilance/`)에 위치한다
- 본문에서 `[@author2023]` 형태로 인용한다
- Quarto가 자동으로 참고문헌 목록을 생성한다

---

## 규제 기관 약어

| 약어 | 정식 명칭 | 관할 |
|---|---|---|
| FDA | Food and Drug Administration | 미국 |
| EMA | European Medicines Agency | 유럽 |
| MFDS | 식품의약품안전처 | 한국 |
| IMDRF | International Medical Device Regulators Forum | 국제 |
| SGS | Societe Generale de Surveillance | 인증 기관 |
| DHF | Design History File | 문서 체계 |

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재의 Summary를 먼저 참조한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Ramsay & Silverman — Functional Data Analysis (1997) | `docs/book/functional_data_analysis/Ramsay-FunctionalDataAnalysis-summary.md` | 함수형 데이터 분석 이론, 스플라인 |
| Ramsay & Silverman — Applied FDA (2002) | `docs/book/functional_data_analysis/Ramsay-AppliedFDA-summary.md` | FDA 사례 연구, 실무 적용 |
| Kokoszka & Reimherr — Introduction to FDA (2017) | `docs/book/functional_data_analysis/Kokoszka-IntroFDA-summary.md` | FDA 입문, 현대적 접근 |

**참조 절차**: Summary 읽기 → 키워드로 관련 챕터 특정 → Full MD에서 수식/정의 확인 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용
