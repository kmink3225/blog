---
name: Writing_GUIDE
type: category
version: 1.0
description: "LOAD when writing or saving posts in the Writing category. Covers logical writing practice sessions, rubric-based feedback records, organized by level and language."
scope: docs/blog/posts/Writing/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Writing/index.qmd
---

# Writing 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Writing 전용 가이드**이다.

---

## 카테고리 특성

- **레벨별 글쓰기 훈련 기록**: Lv.1(중학생) ~ Lv.7(학술 논문)
- **언어**: 한국어 / 영어 통합 (파일명으로 구분)
- **저장 단위**: 레벨 × 언어 단위로 하나의 파일에 누적 append

---

## 파일명 패턴

`level{N}_{언어}_problems.qmd`

| 예시 | 설명 |
|------|------|
| `level1_ko_problems.qmd` | Lv.1 한국어 |
| `level3_ko_problems.qmd` | Lv.3 한국어 (수능 논술) |
| `level5_en_problems.qmd` | Lv.5 영어 (GRE AW) |

---

## YAML 헤더

```yaml
---
title: "논리적 글쓰기: Lv.3 한국어 문제 모음"
subtitle: "수능 논술 수준 — 한국어"
description: |
  Lv.3 수능 논술 수준 글쓰기 훈련 기록.
  채점 루브릭(R1~R7) 기반 피드백 및 개선 과정 포함.
categories:
  - Writing
author: Kwangmin Kim
date: MM/DD/YYYY
---
```

---

## 포스트 구조 (문제별 반복)

```markdown
## 문제 N: [주제 한 줄 요약]

### 문제 정보

| 항목 | 내용 |
|---|---|
| 레벨 | Lv.N |
| 언어 | 한국어 / 영어 |
| 주제 | 주제 문장 |
| 날짜 | YYYY-MM-DD |

### 제출 글

(학습자가 작성한 원문)

### 채점 결과

[R1 Gate: Pass]
총점: N/30

| 기준 | 점수 |
|------|------|
| R2 Focus | N/5 |
| R3 Syntax | N/5 |
| R4 Cohesion | N/5 |
| R5 Structure | N/5 |
| R6 Depth | N/5 |
| R7 Flow | N/5 |

### 피드백

1. [R? - N점] ...
2. [R? - N점] ...
3. [R? - N점] ...

### 개선 글 (재제출 시)

(재작성된 글)

### 최종 채점

총점: N/30 — [합격 / 미달]
```

---

## 관련 가이드

- `guides/writing-tutor.md` — 튜터 운영 모드, 대화 흐름
- `guides/writing-rubric.md` — R1~R7 채점 기준 상세
- `guides/writing-weakness.md` — 취약점 트래커
