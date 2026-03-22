# Book Summary 보강 작업 — Agent 핸드오프 문서

> 최종 갱신: 2026-03-22

## 개요

`docs/book/` 하위의 교재 참조 시스템을 완성하는 작업이다. 크게 **두 가지 작업**이 있다:

1. **상세 필드 채우기** — `*-summary.md`에서 `(삭제됨)`으로 표시된 상세 필드를 본문 기반 요약으로 교체
2. **guide.md → summary.md 통합** — 각 카테고리의 `guide.md`는 잘못된 지시로 생성된 별도 버전의 summary 역할 파일이므로, guide.md의 고유 정보를 summary.md에 통합한 뒤 guide.md는 삭제

---

## 작업 1: 상세 필드 채우기

### 목표

`*-summary.md` 파일의 각 챕터에 있는 `**상세**: → (삭제됨) Ch N (line XXXX)` 를,
해당 책의 `*_marker_full.md` 본문을 읽고 **10~15문장 한국어 요약**으로 교체한다.

### 핵심 규칙

1. **사전 지식 사용 금지** — 반드시 `_marker_full.md` 본문을 `Read(file, offset, limit)`로 읽고, 그 내용만으로 요약 작성
2. **포맷** — 아래 완료 예시를 정확히 따를 것
3. **분량** — 챕터당 10~15문장
4. **언어** — 한국어
5. **rate limit** — 90% 도달 시 즉시 중단, 이 문서의 진행 현황 테이블을 갱신

### 완료 예시 (Sutton-RL Ch 1)

교체 전:
```markdown
**상세**: → (삭제됨) Ch 1 (line 1285)
```

교체 후:
```markdown
**상세**: → `Sutton-RL_marker_full.md` Ch 1 (L:150)
이 장은 강화학습의 기본 틀을 소개하며, 환경과 상호작용하면서 목표를 달성하기 위해
학습하는 에이전트라는 핵심 개념을 제시한다. (... 10~15문장 ...)
```

**주의**: `(삭제됨)` 줄의 `(line XXXX)` 번호는 이전 작업의 잘못된 매핑이므로 **무시**한다.
아래 챕터 시작 라인 표의 `L:` 값을 사용할 것.

### 작업 절차 (챕터 1개당)

```
1. _marker_full.md에서 해당 챕터 시작 라인(L:)부터 60~100줄 Read
2. 내용이 부족하면 추가로 50~100줄 더 Read
3. 읽은 본문을 바탕으로 10~15문장 한국어 요약 작성
4. summary.md에서 해당 챕터의 `(삭제됨)` 줄을 Edit으로 교체
5. 교체 포맷:
   **상세**: → `{marker파일명}` Ch {N} (L:{시작라인})
   (줄바꿈 후 요약 본문)
```

효율 팁: 한 번에 5개 챕터를 병렬 Read → 순차 Edit

### 진행 현황

| # | 책 (key) | 카테고리 | (삭제됨) 수 | 상태 | 비고 |
|---|---------|---------|-----------|------|------|
| 1 | Sutton-RL | deep_learning | 15 | **완료** | 15/15 챕터 교체 완료 |
| 2 | Hastie-ESL | machine_learning | 18 | **읽기완료, 편집 미착수** | marker 본문 Ch1~18 모두 Read 완료, Edit 0건 |
| 3 | James-ISLR | machine_learning | 13 | 미착수 | |
| 4 | Murphy-PMLAdvancedSupp | machine_learning | 5 | 미착수 | Part 단위 구조, 챕터 매핑 확인 필요 |
| 5 | DAMA-DMBOK | governance | 17 | 미착수 | Knowledge Area 단위 |
| 6 | Huang-Pragmatics | linguistics | 9 | 미착수 | |
| 7 | McEnery-CorpusLinguistics | linguistics | 9 | 미착수 | marker가 ## 수준 헤더 |
| 8 | Sidnell-ConversationAnalysis | linguistics | 12 | 미착수 | 편집 논문집 |
| 9 | Robinson-GraphDatabases | ontology | 7 | 미착수 | |
| 10 | Cialdini-Persuasion | psychology | 9 | 미착수 | |
| 11 | Eysenck-CognitivePsychology | psychology | 7 | 미착수 | marker 헤더 비표준, 재검색 필요 |
| 12 | Morling-ResearchMethods | psychology | 11 | 미착수 | 로마 숫자 챕터, 본문 L: 재검색 필요 |

**전체**: 15/132 챕터 완료 (약 11%)

### 다음 작업 순서 (권장)

1. **Hastie-ESL** (18ch) — 이미 marker 본문 읽기 완료, 바로 Edit 시작 가능
2. **James-ISLR** (13ch) — guide.md에 상세 챕터 L: 이미 존재
3. **DAMA-DMBOK** (17ch) — 분량 큼
4. 나머지 소규모 책들

---

## 책별 챕터 시작 라인

### Hastie-ESL (확정)
- 파일: `machine_learning/Hastie-ESL-summary.md`
- Marker: `machine_learning/Hastie-ESL_marker_full.md` (~14,534 라인)

| Ch | 제목 | marker L: |
|----|------|-----------|
| 1 | Introduction | 551 |
| 2 | Overview of Supervised Learning | 678 |
| 3 | Linear Methods for Regression | 1304 |
| 4 | Linear Methods for Classification | 2461 |
| 5 | Basis Expansions and Regularization | 3182 |
| 6 | Kernel Smoothing Methods | 4149 |
| 7 | Model Assessment and Selection | 4642 |
| 8 | Model Inference and Averaging | 5426 |
| 9 | Additive Models, Trees, and Related Methods | 6131 |
| 10 | Boosting and Additive Trees | 6912 |
| 11 | Neural Networks | 7831 |
| 12 | Support Vector Machines and Flexible Discriminants | 8341 |
| 13 | Prototype Methods and Nearest-Neighbors | 9194 |
| 14 | Unsupervised Learning | 9576 |
| 15 | Random Forests | 11468 |
| 16 | Ensemble Learning | 11757 |
| 17 | Undirected Graphical Models | 12103 |
| 18 | High-Dimensional Problems: p >> N | 12617 |

### James-ISLR (guide.md에서 추출, 검증 필요)
- 파일: `machine_learning/James-ISLR-summary.md`
- Marker: `machine_learning/James-ISLR_marker_full.md` (~15,230 라인)
- guide.md에 158개 세부 섹션 L: 이 있으므로 챕터 시작 라인 특정 가능

| Ch | marker L: (추정) | 비고 |
|----|-----------------|------|
| 1 | ~344 | "An Overview of Statistical Learning" |
| 2 | 557 | "2.1 What Is Statistical Learning?" |
| 3 | 1601 | "3.1 Simple Linear Regression" |
| 4 | 3209 | "4.1 An Overview of Classification" |
| 5 | 4961 | "5.1.1 The Validation Set Approach" |
| 6 | ? | guide.md에서 grep 필요 |
| 7 | 7045 | |
| 8 | ? | grep 필요 |
| 9 | ? | grep 필요 |
| 10 | 9973 | |
| 11 | 11540 | |
| 12 | 12480 | |
| 13 | 13784 | |

### Murphy-PMLAdvancedSupp
- 파일: `machine_learning/Murphy-PMLAdvancedSupp-summary.md`
- Marker: `machine_learning/Murphy-PMLAdvancedSupp_marker_full.md` (~7,821 라인)
- Part 단위 구조 — summary.md 챕터 구조와 매핑 확인 필요

| Part | marker L: (추정) |
|------|-----------------|
| I (Fundamentals) | 262 |
| II (Inference) | 1178 |
| III (Prediction) | 4423 |
| IV (Generation) | 5231 |
| V (Discovery) | 5289 |
| VI (Decision making) | 7350 |

### DAMA-DMBOK
- 파일: `governance/DAMA-DMBOK-summary.md`
- Marker: `governance/DAMA-DMBOK_marker_full.md` (~14,347 라인)

| Knowledge Area | marker L: (추정) |
|----------------|-----------------|
| Data Management Introduction | 728 |
| Data Governance | 1803 |
| Data Architecture | 2614 |
| Data Modeling and Design | 3068 |
| Data Storage and Operations | 4068 |
| Data Security | 5130 |
| Data Integration and Interoperability | 6250 |
| Document and Content Management | 6921 |
| Reference and Master Data | 7841 |
| Data Warehousing and BI | 8610 |
| Metadata Management | 9394 |
| Data Quality Management | 10161 |
| Big Data and Data Science | 11237 |
| Data Management Maturity Assessment | 11952 |
| Data Management Organization | 12451 |
| Organizational Change Management | 12931 |

### Huang-Pragmatics
- 파일: `linguistics/Huang-Pragmatics-summary.md`
- Marker: `linguistics/Huang-Pragmatics_marker_full.md` (~9,510 라인)
- Ch 1, 4, 7, 8, 9는 marker에서 직접 grep 필요

| Ch | marker L: (추정) |
|----|-----------------|
| 2 (Implicature) | 952 |
| 3 (Presupposition) | 2349 |
| 5 (Deixis) | 3894 |
| 6 (Reference) | 4866 |

### McEnery-CorpusLinguistics
- 파일: `linguistics/McEnery-CorpusLinguistics-summary.md`
- Marker: `linguistics/McEnery-CorpusLinguistics_marker_full.md` (~3,771 라인)
- marker가 `##` 수준 헤더 사용 — 챕터 시작 라인 전체 grep 필요

### Sidnell-ConversationAnalysis
- 파일: `linguistics/Sidnell-ConversationAnalysis-summary.md`
- Marker: `linguistics/Sidnell-ConversationAnalysis_marker_full.md` (~6,587 라인)
- 편집 논문집, TOC L:93~100 부근, 실제 본문은 뒤에 있을 수 있음

### Robinson-GraphDatabases
- 파일: `ontology/Robinson-GraphDatabases-summary.md`
- Marker: `ontology/Robinson-GraphDatabases_marker_full.md` (~4,647 라인)

| 섹션 | marker L: (추정) |
|------|-----------------|
| Introduction | 301 |
| Options for Storing Connected Data | 431 |
| Data Modeling with Graphs | 634 |
| Building a Graph Database Application | 1510 |
| Graphs in the Real World | 2522 |
| Graph Database Internals | 3375 |
| Predictive Analysis with Graph Theory | 3716 |

### Cialdini-Persuasion
- 파일: `psychology/Cialdini-Persuasion-summary.md`
- Marker: `psychology/Cialdini-Persuasion_marker_full.md` (~3,222 라인)
- Ch 3 (Commitment & Consistency)는 직접 검색 필요

| Ch | marker L: (추정) |
|----|-----------------|
| 1 (Weapons of Influence) | 78 |
| 2 (Reciprocation) | 180 |
| 4 (Social Proof) | 848 |
| 5 (Liking) | 1236 |
| 6 (Authority) | 1554 |
| 7 (Scarcity) | 1744 |

### Eysenck-CognitivePsychology
- 파일: `psychology/Eysenck-CognitivePsychology-summary.md`
- Marker: `psychology/Eysenck-CognitivePsychology_marker_full.md` (~20,111 라인)
- marker 헤더 구조가 비표준적 — 챕터 시작 라인 전체 재검색 필요

### Morling-ResearchMethods
- 파일: `psychology/Morling-ResearchMethods-summary.md`
- Marker: `psychology/Morling-ResearchMethods_marker_full.md` (~6,482 라인)
- 로마 숫자(I~XIII) 챕터 구조, TOC L:23~97은 목차 영역이므로 실제 본문 시작 라인 별도 검색 필요

---

## 작업 2: guide.md → summary.md 통합

### 배경

각 카테고리 폴더에 `guide.md`가 8개 존재한다. 이것은 잘못된 지시로 생성된 **다른 버전의 summary** 역할 파일이다.
guide.md의 고유 정보를 summary.md에 통합한 뒤, guide.md는 삭제해야 한다.

### 대상 파일

| 카테고리 | guide.md 크기 |
|---------|-------------|
| behavioral_analysis | 161 lines |
| data_science | 127 lines |
| deep_learning | 401 lines |
| governance | 174 lines |
| linguistics | 261 lines |
| machine_learning | 403 lines |
| ontology | 71 lines |
| psychology | 200 lines |

### guide.md의 구조

각 guide.md는 두 섹션으로 구성:

1. **소스 파일 목록** — 각 책의 파일 목록과 변환 도구(Marker, Document Intelligence 등) 표시
   ```markdown
   ### Hastie-ESL
   | 파일 | 변환 도구 |
   |---|---|
   | Hastie-ESL-summary.md | 요약 |
   | Hastie-ESL_marker_full.md | Marker |
   ```

2. **챕터 목차 (Marker 기준)** — `L:숫자`로 marker_full.md의 세부 섹션 참조
   ```markdown
   ### Hastie-ESL
   - **파일**: `Hastie-ESL_marker_full.md`
   - **총 라인 수**: ~14,535
   - **주요 섹션** (16개):
   - 2.3 Two Simple Approaches... `L:710`
   ```

### 통합 방법

1. **소스 파일 목록**: summary.md의 YAML frontmatter 또는 상단에 통합
   - 또는 카테고리 폴더에 별도 index/README로 유지할 수도 있음 (사용자 확인 필요)

2. **챕터 목차 (Marker 세부 목차)**: 이미 일부 summary.md에 `**Marker 세부 목차**` 블록으로 들어가 있음
   - guide.md의 세부 섹션 L: 참조가 summary.md보다 더 상세한 경우 → summary.md에 병합
   - 중복인 경우 → 무시

3. guide.md 삭제

### 통합 절차

```
1. guide.md 읽기
2. 해당 카테고리의 각 summary.md와 비교
3. guide.md에만 있는 정보 식별:
   - 소스 파일 목록 (변환 도구 정보)
   - 더 상세한 Marker 세부 목차
4. summary.md에 해당 정보 통합
5. guide.md 삭제
```

> **주의**: 통합 전 사용자에게 소스 파일 목록을 어디에 넣을지 확인하는 것이 좋음.
> summary.md frontmatter에 `sources:` 필드를 추가하는 방식이 깔끔할 수 있음.

### 통합 진행 현황

| 카테고리 | 상태 |
|---------|------|
| behavioral_analysis | 미착수 |
| data_science | 미착수 |
| deep_learning | 미착수 |
| governance | 미착수 |
| linguistics | 미착수 |
| machine_learning | 미착수 |
| ontology | 미착수 |
| psychology | 미착수 |

---

## 주의사항

- `(삭제됨)` 옆의 `(line XXXX)` 번호는 **이전 작업의 잘못된 참조**이므로 무시
- 위 표의 `marker L:` 값 중 "(추정)"은 탐색 에이전트가 추출한 값 — 작업 시 `Grep`으로 재확인 권장
- 일부 책(McEnery, Eysenck, Morling, Sidnell)은 marker 헤더 구조가 비표준적이므로 챕터 경계를 본문에서 직접 확인
- `_marker_full.md`는 Marker(GPU PDF→MD 변환기) 출력물이므로 OCR 노이즈가 있을 수 있음
- 작업 2(guide.md 통합)는 작업 1(상세 채우기)과 독립적이므로 병렬 진행 가능
- rate limit 90% 도달 시 즉시 중단하고 이 문서의 진행 현황을 갱신할 것
