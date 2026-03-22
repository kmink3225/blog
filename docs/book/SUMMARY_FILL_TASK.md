# Book Summary 보강 작업 — Agent 핸드오프 문서

> 최종 갱신: 2026-03-22 (세션 3 완료)

## 개요

`docs/book/` 하위의 교재 참조 시스템을 완성하는 작업이다. **세 가지 작업**이 있다:

1. **guide.md → summary.md 통합** — ✅ **완료** (세션 3)
2. **상세 필드 채우기** — ✅ **완료** (세션 3) — 132/132 챕터 + 추가 559 챕터 보강
3. **MinerU 변환 완료** — 데스크탑에서 나머지 6개 PDF를 MinerU로 변환 후 품질 검사 → docs/book/ 복사

---

## 전체 시스템 구조 (최종 목표)

```
AGENT_GUIDE.md (최상위 규칙)
    ↓
카테고리 GUIDE.md (docs/blog/posts/*/GUIDE.md)
    ↓ "이 주제는 이 교재를 참조하라"
Book Summary (docs/book/*/-summary.md) ← 지도
    ↓ "이 챕터의 이 라인을 읽어라"
Book Full MD (docs/book/*/_full.md) ← 본문
```

**목적:**
- Agent가 수만 줄의 본문을 전부 읽지 않고, summary(지도)를 통해 필요한 부분만 정확히 찾아 읽는다
- 토큰 비용 최적화 + 환각 방지 + 풍성한 근거 기반 블로그/답변

---

## 작업 1: guide.md → summary.md 통합

### 상태: **완료** (8개 전부)

| 카테고리 | guide.md 크기 | 상태 |
|---------|-------------|------|
| machine_learning | 403 lines | **완료** |
| deep_learning | 401 lines | **완료** |
| data_science | 127 lines | **완료** |
| governance | 174 lines | **완료** |
| behavioral_analysis | 161 lines | **완료** |
| linguistics | 261 lines | **완료** |
| ontology | 71 lines | **완료** |
| psychology | 200 lines | **완료** |

### guide.md 구조

각 guide.md는 두 섹션:

1. **소스 파일 목록** — 각 책의 파일 목록과 변환 도구(Marker, Document Intelligence 등)
2. **챕터 목차 (Marker 기준)** — `L:숫자`로 marker_full.md의 세부 섹션 라인 참조

### 통합 방법

1. summary.md YAML frontmatter에 `sources:` 필드 추가 (변환 도구 정보)
2. summary.md 끝에 `## Marker 세부 목차` 섹션 추가 (L: 라인 참조)
3. guide.md 삭제

### 통합 예시

YAML frontmatter에 추가:
```yaml
sources:
  - file: "Hastie-ESL_marker_full.md"
    tool: Marker
  - file: "Hastie-ESL_azure_full.md"
    tool: Document Intelligence
```

파일 끝에 추가:
```markdown
---

## Marker 세부 목차

> `L:숫자`는 `Hastie-ESL_marker_full.md`의 라인 번호.

- 2.3 Two Simple Approaches to Prediction `L:710`
- 2.6 Statistical Models `L:1020`
(...)
```

---

## 작업 2: 상세 필드 채우기

### 목표

`*-summary.md`의 각 챕터에 있는 `**상세**: → (삭제됨)` 를, 해당 책의 `*_marker_full.md` 본문을 읽고 **10~15문장 한국어 요약**으로 교체.

### 핵심 규칙

1. **사전 지식 사용 금지** — 반드시 `_marker_full.md` 본문을 `Read(file, offset, limit)`로 읽고 내용만으로 요약
2. **포맷**: `**상세**: → {marker파일명} Ch N (L:시작라인)` + 줄바꿈 후 10~15문장 요약
3. **언어**: 한국어 (한다 체)

### 완료 예시

```markdown
**상세**: → `Sutton-RL_marker_full.md` Ch 1 (L:150)
이 장은 강화학습의 기본 틀을 소개하며, 환경과 상호작용하면서 목표를 달성하기 위해
학습하는 에이전트라는 핵심 개념을 제시한다. (... 10~15문장 ...)
```

### 진행 현황

| # | 책 (key) | 카테고리 | (삭제됨) 수 | 상태 |
|---|---------|---------|-----------|------|
| 1 | Sutton-RL | deep_learning | 15 | **완료** |
| 2 | Hastie-ESL | machine_learning | 18 | **완료** |
| 3 | James-ISLR | machine_learning | 13 | **완료** |
| 4 | Murphy-PMLAdvancedSupp | machine_learning | 5 | **완료** |
| 5 | DAMA-DMBOK | governance | 17 | **완료** |
| 6 | Huang-Pragmatics | linguistics | 9 | **완료** |
| 7 | McEnery-CorpusLinguistics | linguistics | 9 | **완료** |
| 8 | Sidnell-ConversationAnalysis | linguistics | 12 | **완료** |
| 9 | Robinson-GraphDatabases | ontology | 7 | **완료** |
| 10 | Cialdini-Persuasion | psychology | 9 | **완료** |
| 11 | Eysenck-CognitivePsychology | psychology | 7 | **완료** |
| 12 | Morling-ResearchMethods | psychology | 11 | **완료** |

**전체**: 132/132 챕터 완료 (100%)

### 책별 챕터 시작 라인

(아래 표의 L: 값은 _marker_full.md 기준)

#### Hastie-ESL
- Marker: `machine_learning/Hastie-ESL_marker_full.md` (~14,534 라인)

| Ch | 제목 | L: |
|----|------|-----|
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

#### James-ISLR
- Marker: `machine_learning/James-ISLR_marker_full.md` (~15,230 라인)

| Ch | L: (추정) |
|----|-----------|
| 1 | ~344 |
| 2 | 557 |
| 3 | 1601 |
| 4 | 3209 |
| 5 | 4961 |
| 6 | 5530 |
| 7 | 7045 |
| 8 | guide.md에서 확인 필요 |
| 9 | guide.md에서 확인 필요 |
| 10 | 9973 |
| 11 | 11540 |
| 12 | 12480 |
| 13 | 13784 |

#### Murphy-PMLAdvancedSupp
- Marker: `machine_learning/Murphy-PMLAdvancedSupp_marker_full.md` (~7,821 라인)

| Part | L: |
|------|-----|
| I (Fundamentals) | 262 |
| II (Inference) | 1178 |
| III (Prediction) | 4423 |
| IV (Generation) | 5231 |
| V (Discovery) | 5289 |
| VI (Decision making) | 7350 |

#### DAMA-DMBOK
- Marker: `governance/DAMA-DMBOK_marker_full.md` (~14,347 라인)

| Knowledge Area | L: |
|----------------|-----|
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

#### 나머지 (Huang, McEnery, Sidnell, Robinson, Cialdini, Eysenck, Morling)
- 챕터 시작 라인은 각 guide.md에 일부 있고, 나머지는 grep으로 검색 필요
- 상세는 이전 핸드오프 문서 내용 참조

---

## 작업 3: MinerU PDF 변환 (데스크탑에서 수행)

### 완료된 변환

**Nougat 성공 (4개):**
- Sutton RL, Huyen AI Engineering, Huyen Designing ML Systems, Hastie ESL
- 출력: `새 폴더/nougat_output/`

**MinerU 성공 (5개):**
- Kohavi AB Testing, Bishop PRML, James ISLR, Raschka Build LLM, Murphy PML Adv Supp, Provost DS Business
- 출력: `새 폴더/mineru_output/{name}/auto/{name}.md`

### 데스크탑에서 할 나머지 (6개)

| 순서 | 파일 | 페이지 |
|------|------|--------|
| 1 | Jurafsky SLP | 611 |
| 2 | Montgomery DOE | 700 |
| 3 | Goodfellow Deep Learning | 777 |
| 4 | Murphy PML Intro | 850 |
| 5 | Zhang D2L | 1089 |
| 6 | Murphy PML Advanced | 1100 |

**변환 스크립트**: `새 폴더/convert_mineru.py` (15분 쿨다운, 2시간 타임아웃, GPU 온도 모니터링 포함)

**변환 후 절차**: 품질 검사 → 승인 → docs/book/에 복사 (바로 복사하지 않는다)

### 변환 도구 설정 (blog conda env)

- MinerU: `magic-pdf -p input.pdf -o output_dir -m auto`
- 설정: `C:\Users\kmkim\magic-pdf.json` (models-dir: `C:/Users/kmkim/mineru_models/models`)
- transformers==4.46.3 (최신 버전은 Nougat/MinerU와 충돌)
- 긴 파일명은 Windows 260자 제한에 걸리므로 짧은 이름으로 복사 후 변환

---

## docs/book/ 폴더 구조

```
docs/book/
├── BOOK_SOURCE_GUIDE.md
├── SUMMARY_FILL_TASK.md (이 파일)
├── bayesian/              ← summary 완료, guide.md 없음 (기존)
├── behavioral_analysis/   ← guide.md 통합 필요
├── data_science/          ← guide.md 통합 필요
├── deep_learning/         ← guide.md 통합 필요
├── epidemiology/          ← summary 완료, guide.md 없음 (기존)
├── functional_data_analysis/ ← summary 완료, guide.md 없음 (기존)
├── generalized_linear_model/ ← summary 완료, guide.md 없음 (기존)
├── governance/            ← guide.md 통합 필요
├── linear_algebra/        ← summary 완료, guide.md 없음 (기존)
├── linguistics/           ← guide.md 통합 필요
├── machine_learning/      ← guide.md 통합 필요
├── mixed_model/           ← summary 완료, guide.md 없음 (기존)
├── ontology/              ← guide.md 통합 필요
├── psychology/            ← guide.md 통합 필요
├── statistics/            ← summary 완료, guide.md 없음 (기존)
├── strategy_frameworks/   ← summary 완료, guide.md 없음
└── survival/              ← summary 완료, guide.md 없음 (기존)
```

파일 명명 규칙:
- `{Author}-{ShortTitle}-summary.md` — 지도 (챕터별 요약 + 키워드 + 라인 참조)
- `{Author}-{ShortTitle}_full.md` — markitdown 변환 원본
- `{Author}-{ShortTitle}_marker_full.md` — Marker 변환 원본
- `{Author}-{ShortTitle}_azure_full.md` — Document Intelligence 변환 원본

---

## 관련 파일 참조

- `AGENT_GUIDE.md` — 2-Layer 교재 참조 체계 (Book Source 섹션)
- `docs/book/BOOK_SOURCE_GUIDE.md` — 교재 소스 가이드
- 카테고리 GUIDE.md (`docs/blog/posts/*/GUIDE.md`) — 10개 카테고리에 교재 레퍼런스 섹션 추가 완료
- CLAUDE.md — AGENT_GUIDE.md 참조 포인터

## 메모리 참조

- `~/.claude/projects/.../memory/feedback_conversion.md` — 변환 워크플로 (품질 검사 후 복사)
- `~/.claude/projects/.../memory/feedback_network.md` — 사내 방화벽 주의
- `~/.claude/projects/.../memory/feedback_tool_install.md` — 도구 설치 시 공식 문서 먼저
- `~/.claude/projects/.../memory/project_blog_env.md` — conda 환경 (nblog vs blog)
- `~/.claude/projects/.../memory/project_minerva.md` — MINERVA 프로젝트 맥락
