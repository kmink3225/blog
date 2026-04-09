---
name: LDA_HANDOFF
type: handoff
last_updated: 2026-04-10
author: Claude Sonnet 4.6
description: >
  LDA 폴더 현황 및 인계 문서.
  다른 agent가 이 폴더에서 작업을 이어받을 때 참조한다.
---

# LDA 폴더 인계 문서 (Handoff)

## 1. 배경 및 목표

이 폴더는 **Hedeker & Gibbons (2006) 교재**를 기준으로 종단 데이터 분석(LDA) 시리즈를 체계화하는 작업이 진행 중이다.

- **정본 시리즈**: `20-`번대 이후 파일. Hedeker 교재 챕터 순서를 따른다.
- **통합 예정**: `01~19`, `basic-*`, `139-rmle.qmd`, `survival_lda.qmd`는 별도 기간에 계획 없이 작성된 파일이다. Hedeker 시리즈가 해당 주제를 커버하면 내용을 통합한다.
- **삭제 금지**: 통합 전까지 파일은 보존한다. 고유 콘텐츠를 신규 포스트에 먼저 반영한 뒤 index에서만 정리한다.

---

## 2. 파일 현황

### 그룹 A: Hedeker 시리즈 (정본 — 진행 중)

| 파일 | 제목 | Hedeker 챕터 | 상태 |
|------|------|-------------|------|
| `20-longitudinal-studies-overview.qmd` | 종단 연구 개요 | Ch.1 | 완료 |
| `21-anova-longitudinal-overview.qmd` | 반복측정 ANOVA 개요 | Ch.2 | 완료 |
| `22-rm-anova-single-sample-decomposition.qmd` | 단일 표본 RM-ANOVA | Ch.2 심화 | 완료 |
| `23-rm-anova-multiple-sample-decomposition.qmd` | 다중 표본 RM-ANOVA | Ch.2 심화 | 완료 |
| `24-manova-longitudinal.qmd` | MANOVA 종단 접근 | Ch.3 | 완료 |
| `25-anova-manova-data-layout.qmd` | ANOVA vs MANOVA 데이터 구조 | Ch.3 보조 | 완료 |
| `26-manova-repeated-measurements.qmd` | MANOVA 일표본 | Ch.3 | 완료 |
| `27-manova-repeated-s-sample.qmd` | MANOVA 다표본 | Ch.3 | 완료 |
| `28-manova-illustration.qmd` | MANOVA 수치 예시 (Bock) | Ch.3 | 완료 |
| `29-anova-longitudinal-illustration.qmd` | ANOVA 수치 예시 (Bock) | Ch.2 | 완료 |
| `30-mixed-effects-continuous-overview.qmd` | 혼합효과 연속 반응 개요 | Ch.4 | 완료 |

**다음 작업**: Ch.4 이후 (혼합효과 모형 상세) → `31-` 번호부터 작성

---

### 그룹 B: Mixed Model 심화 시리즈 (01~19 — 통합 예정)

2026-03-07 일괄 작성됨. Hedeker 기준이 아닌 LMM/GLMM 중심 구성.
Hedeker 시리즈가 해당 챕터를 완성하면 점진적으로 통합한다.

| 파일 | 제목 | 통합 대상 Hedeker 챕터 |
|------|------|----------------------|
| `01-mixed-model-intro.qmd` | 왜 Mixed Model인가 | Ch.4 (개요) |
| `02-mixed-model-structure.qmd` | 모델 구조 | Ch.4 |
| `03-mixed-model-estimation.qmd` | 추정과 모델 선택 (ML/REML) | Ch.4, Ch.5 |
| `04-mixed-model-practice.qmd` | 실무 예시 | Ch.4 응용 |
| `05-mixed-model-glmm-intro.qmd` | GLMM 개요 | Ch.9 (Hedeker GLMM) |
| `06-mixed-model-glmm-binary.qmd` | GLMM 이진 결과 | Ch.9 |
| `07-mixed-model-glmm-count.qmd` | GLMM 카운트 | Ch.9 |
| `08-mixed-model-gee-intro.qmd` | GEE | Ch.10 (GEE) |
| `09-mixed-model-gam-intro.qmd` | GAM/GAMM | 추가 섹션 |
| `10-mixed-model-functional-intro.qmd` | FDA 개요 | 추가 섹션 (FDA 폴더와 cross-link) |
| `11-mixed-model-comparison.qmd` | 기법 비교 | 추가 섹션 |
| `15-mixed-model-diagnostics.qmd` | 회귀 진단 | 추가 섹션 |
| `16-mixed-model-stratified.qmd` | 층화 분석 | 추가 섹션 |
| `17-mixed-model-eda.qmd` | 종단 EDA | 추가 섹션 |
| `18-mixed-model-panel-intro.qmd` | 패널 데이터 (1) | 추가 섹션 |
| `19-mixed-model-panel-did.qmd` | 패널 데이터 (2) DID | 추가 섹션 |

---

### 그룹 C: 초기 노트 (basic-* — 통합 예정)

2023년 작성. 내용이 초안 수준이며 draft: true 상태.

| 파일 | 제목 | 비고 |
|------|------|------|
| `basic-00-intro.qmd` | LDA (1) - Introduction | 한국어/영어 탭 구조. 일반 LDA 개요. |
| `basic-01-covariance_model.qmd` | LDA (2) - Concepts & Covariance Models | 공분산 구조 모형 설명 |
| `basic-03-wls.qmd` | LDA (3) - WLS & REML | WLS, REML 개념 |
| `basic-04-CD4-plus.qmd` | LDA - CD4+ Cell Depletion | HIV CD4 데이터 응용 예시 |
| `basic-05-eda.qmd` | LDA - EDA | 탐색적 분석 |

---

### 그룹 D: 단독 파일 (통합 예정)

| 파일 | 제목 | 내용 요약 | 통합 대상 |
|------|------|----------|----------|
| `139-rmle.qmd` | MLE | MLE vs REML 비교, Mixed Effects 맥락 | `03-mixed-model-estimation.qmd` 또는 Hedeker Ch.4 추정 포스트 |
| `survival_lda.qmd` | LDA - Survival / Cox Model | Cox 비례위험모형, Shared Frailty, Stratified Cox를 종단 데이터에 적용 | 추가 섹션 (생존 분석 × LDA) |

> **주의**: `survival_lda.qmd`는 `basic-00-intro.qmd`와 제목이 같지만 **내용이 완전히 다르다**. Cox Model 관점의 종단 분석이다.

---

## 3. 인덱스 구조

`index.qmd`는 아래 4개 섹션으로 구성된다:

```
# Hedeker 시리즈 (진행 중)
  ## LDA 기초 (ANOVA/MANOVA)  ← 20~29
  ## 혼합효과 모형              ← 30~

# Mixed Model 심화 시리즈       ← 01~19
  (LMM, GLMM, GEE, GAM, 진단, 패널 등)

# ML / DL / RL for Longitudinal Data  ← cross-link (ML/DL 폴더)

# 초기 노트 (통합 예정)         ← basic-*, 139-rmle, survival_lda
```

`Statistics/index.qmd`에서는 이 `LDA/index.qmd`로 단일 링크만 유지한다.

---

## 4. 작업 규칙

### 신규 포스트 번호 규칙

- Hedeker 시리즈: `31-`, `32-`, ... 순서로 이어간다
- `32-mixed-model-roadmap.qmd`는 **Statistics 루트**에 있다 (LDA 폴더 아님)
- 기존 파일 번호 변경 금지 (크로스 링크 파손)

### 통합 시 필수 절차

1. 구 포스트 전체 읽기
2. 신규 포스트에 없는 고유 콘텐츠 (수식 유도, 코드 예시, 응용 사례) 식별
3. 신규 포스트에 한다체로 재작성하여 보강
4. 보강 완료 후 `index.qmd` 초기 노트 섹션에서 링크 제거 (파일은 보존)

### cross-link 주의

- `10-mixed-model-functional-intro.qmd`는 `Statistics/index.qmd`의 **FDA 섹션**에도 링크됨 — 제거 시 양쪽 확인 필요
- ML/DL/RL 포스트들은 실제로 `Machine_Learning/`, `Deep_Learning/` 폴더에 있음 (상대경로 `../Machine_Learning/`, `../Deep_Learning/`)

---

## 5. 교재 정보

- **주 교재**: Hedeker, D. & Gibbons, R. D. (2006). *Longitudinal Data Analysis*. Wiley.
- **교재 소스**: `docs/book/statistics/longidutindal_data_analysis/`
- **읽기 전략**: Niche 교재이므로 챕터 전체 읽기 (`info-search.md` 기준)

---

## 6. 미완료 항목

- [ ] Hedeker Ch.5 이후 포스트 (`31-`~) 미작성
- [ ] 01~19 → Hedeker 시리즈 통합 (Ch.4 완성 후 순차 진행)
- [ ] `basic-03-wls.qmd`의 WLS/REML 내용 → `139-rmle.qmd`와 함께 추정 포스트에 통합
- [ ] `survival_lda.qmd` → 생존 분석 × LDA 추가 섹션 포스트로 발전
- [ ] 연구 설계 섹션 placeholder 5개 미작성
