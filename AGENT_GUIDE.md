---
name: AGENT_GUIDE
type: master
version: 6.2
last_updated: 2026-03-25
changelog: "v6.3 (2026-03-25): E2E 예시·Common Mistakes를 별도 파일로 분리, changelog 압축"
description: >
  LOAD at the START of any blog-related task. 공통 규칙(스타일, YAML, index 패턴 등)을
  담은 코어 가이드. 태스크별 상세 절차는 guides/ 폴더의 스킬 파일을 로드한다.
scope: global
category_guides:
  - path: docs/blog/posts/Statistics/GUIDE.md
    category: Statistics
  - path: docs/blog/posts/Math/GUIDE.md
    category: Math
  - path: docs/blog/posts/Experimentation/GUIDE.md
    category: Experimentation
  - path: docs/blog/posts/Agent/GUIDE.md
    category: Agent
  - path: docs/blog/posts/Deep_Learning/GUIDE.md
    category: Deep Learning
  - path: docs/blog/posts/Machine_Learning/GUIDE.md
    category: Machine Learning
  - path: docs/blog/posts/Data_Science/GUIDE.md
    category: Data Science
  - path: docs/blog/posts/Engineering/GUIDE.md
    category: Engineering
  - path: docs/blog/posts/Governance/GUIDE.md
    category: Governance
  - path: docs/blog/posts/Code_Test/GUIDE.md
    category: Code Test
  - path: docs/blog/posts/Strategy_Frameworks/GUIDE.md
    category: Strategy Frameworks
  - path: docs/blog/posts/Surveilance/GUIDE.md
    category: Surveilance
reference_guides: []
skill_guides:
  - path: guides/info-search.md
    skill: 통합 정보 탐색
  - path: guides/write-post.md
    skill: 블로그 포스트 작성
  - path: guides/convert-tbd.md
    skill: TBD 메모 전환
  - path: guides/organize-series.md
    skill: 시리즈 정리
  - path: guides/answer-question.md
    skill: 질문 응답
  - path: guides/retrofit-post.md
    skill: 기존 포스트 교정
  - path: guides/audit.md
    skill: 콘텐츠 품질 감사
  - path: guides/common-mistakes.md
    skill: 오류 패턴 참조
  - path: guides/examples.md
    skill: E2E 실행 흐름 예시
  - path: guides/changelog-summary.md
    skill: 변경 이력 요약
---

# AGENT_GUIDE.md — Blog Repository Instructions (공통 코어)

---

<always-on-rules>

## 절대 규칙 (Always-On Rules)

> 가이드 전체를 읽지 못하더라도 아래 5개는 반드시 지킨다.

1. **한다 체** — 모든 콘텐츠는 `~한다/~이다/~된다`로 작성. 경어체(`~합니다`) 금지.
2. **수동 번호 금지** — 섹션 헤더에 `## 1. 개요` 식 번호를 절대 붙이지 않는다 (`number-sections: true`로 자동 부여).
3. **Category GUIDE 필수 로드** — 해당 카테고리 포스트를 작성·수정하기 전에 반드시 그 카테고리의 `GUIDE.md`를 읽는다.
4. **index.qmd 업데이트** — 새 포스트 작성 후 반드시 해당 카테고리 `index.qmd`에 링크를 추가한다.
5. **이모지 사용 금지** — `.qmd` 콘텐츠에 이모지를 넣지 않는다.

</always-on-rules>

---

<rule-precedence>

## 규칙 우선순위 (Rule Precedence)

규칙이 충돌할 경우 아래 순서를 따른다 (위가 우선).

```
카테고리 GUIDE.md  >  AGENT_GUIDE.md (이 파일)  >  에이전트 자체 판단
```

- 카테고리 GUIDE가 AGENT_GUIDE와 다른 패턴을 명시하면 카테고리 GUIDE를 따른다.
- 어느 가이드에도 언급이 없는 사항은 에이전트가 판단하되, 불확실하면 사용자에게 확인한다.

</rule-precedence>

---

## Project Overview

Quarto 기반 기술 블로그. `.qmd` 파일로 콘텐츠 작성, `quarto render`로 정적 HTML 생성, Netlify 배포.

- **Site**: https://kk3225.netlify.app
- **Author**: Kwangmin Kim
- **Language**: 한국어 (한다 체)
- **Commands**: `quarto preview` (로컬 미리보기), `quarto render` (빌드)

### Key Files

| 파일 | 역할 |
|------|------|
| `_quarto.yml` | 프로젝트 설정, navbar, sidebar, `number-sections: true` |
| `docs/blog/posts/_metadata.yml` | 포스트 공통 설정 (댓글, TOC, 배너, 날짜형식) |

### 메타데이터 상속 구조

```
_quarto.yml → docs/blog/posts/_metadata.yml → 각 .qmd YAML 헤더 (우선순위 최고)
```

따라서 개별 `.qmd` 파일에는 `title`, `subtitle`, `description`, `categories`, `author`, `date`만 넣으면 된다.

---

## 카테고리 구조

`docs/blog/posts/` 아래에 다음 카테고리 폴더가 존재한다. 각 폴더에는 `index.qmd`(목차)와 `GUIDE.md`(작성 규칙)가 있다.

| 카테고리 폴더 | 주제 |
|---|---|
| `Agent/` | RAG, LangChain, LangGraph, Agent 개발 |
| `Code_Test/` | 알고리즘, SQL 문제 풀이 |
| `Data_Science/` | CRISP-DM, EDA, Feature Engineering |
| `Deep_Learning/` | CNN, RNN, Transformer, NLP, GAN |
| `Engineering/` | DevOps, Python, Infra, Data Engineering |
| `Experimentation/` | A/B Test, 인과추론, MAB |
| `Governance/` | 데이터 거버넌스, 품질, 표준화 |
| `Machine_Learning/` | 분류, 회귀, 앙상블, 비지도학습 |
| `Math/` | 선형대수, 미적분, 최적화 |
| `Statistics/` | 분포, 검정, 회귀, 종단분석, FDA |
| `Strategy_Frameworks/` | 비즈니스 분석, 전략 프레임워크 |
| `Surveilance/` | 의료기기 규제, FDA/EMA 가이드라인 |

> **하위 폴더 구조와 파일 배치는 각 카테고리의 `index.qmd`와 실제 폴더를 직접 확인한다.**

---

## 작성 규칙

### YAML 헤더 (필수)

```yaml
---
title: "제목"
subtitle: "부제목"
description: |
  1-3문장 설명.
categories:
  - Category1
  - Category2
author: Kwangmin Kim
date: MM/DD/YYYY
---
```

- `title`, `description`, `categories`, `author`, `date`는 필수
- `date`는 `MM/DD/YYYY` 형식 (예: `03/18/2026`). 미작성 글은 `1111-11-11`
- `format`, `toc`, `code-fold` 등은 `_metadata.yml`에서 상속되므로 생략

### 파일명 규칙

같은 폴더 내 기존 패턴을 따른다. 각 카테고리 GUIDE.md에 상세 패턴이 정의되어 있다.

### 콘텐츠 스타일

- **한다 체 사용**: `~한다`, `~이다`, `~된다` (O: `Git은 분산형 버전 관리 시스템이다` / X: `~입니다`)
- **경어체 금지**: `~합니다`, `~입니다`, `~하세요` 사용하지 않음
- **이모지 사용 금지**
- **섹션 헤더에 수동 번호 절대 금지**: `number-sections: true` 전역 설정으로 자동 부여됨. 수동 번호 시 이중 번호 발생 (O: `## 개요` / X: `## 1. 개요`)

### 자주 발생하는 오류 패턴

> 상세 Bad → Corrected 예시는 `guides/common-mistakes.md` 참조. 대표 4가지: 경어체 혼입, 수동 번호 붙이기, 수식 공백 누락, 콘텐츠 축소.

### 콘텐츠 분량 기본값

| 항목 | 기본값 | 비고 |
|------|--------|------|
| 포스트 전체 길이 | **500줄 내외** (400~600줄) | 카테고리 GUIDE에 별도 지침이 있으면 그것을 따른다 |
| 섹션 수 | 4~8개 (`##` 수준) | 주제 복잡도에 따라 조정 |
| 코드 블록 포함 시 | 코드 + 설명 합쳐 500줄 | 코드가 길면 기능 단위로 분할하고 사이에 설명 |
| description (YAML) | 1~3문장 | 50~150자 |

너무 짧으면(200줄 미만) 깊이가 부족하고, 너무 길면(800줄 이상) 독자가 이탈한다. 500줄은 "하나의 주제를 충분히 설명하되 집중력이 유지되는" 분량이다.

### 줄 개행 규칙

문단 내 줄바꿈이 필요한 곳에 **줄 끝 공백 2칸**을 붙인다. 빈 줄(`\n\n`) 문단 구분, 코드 블록, YAML, callout 내부, bullet list에서는 불필요하다.

### 콘텐츠 품질 원칙

모든 서술은 **주장 → 근거 → 해석** 구조를 따른다.

| 점검 항목 | 질문 | 미충족 시 조치 |
|-----------|------|---------------|
| 주장 → 왜 | "왜 그게 문제인가?"에 답하는가 | 시나리오 또는 반사실적 비교를 추가 |
| 숫자 → 해석 | 숫자 뒤에 "so what"이 있는가 | 실무적 임팩트로 번역 |
| 사례 → 연결 | 이 사례가 왜 여기 있는지 독자가 아는가 | 일반론을 증명하는 구조로 재배치 |
| 나열 → 흐름 | 목록이 단순 나열인가, 논리 흐름인가 | 항목 간 인과·순서 관계를 명시 |
| 추상 → 직관 | 수식·가정·알고리즘 뒤에 비유가 있는가 | 일상어 비유 또는 반사실 시나리오 추가 |

### 수식 (LaTeX)

- 인라인: `$수식$` — **`$` 양쪽에 반드시 공백** (O: `모수 $\theta$ 를` / X: `모수$\theta$를`)
- 블록: `$$수식$$`
- 교재 인용 시 `(저자, 연도, Ch.N)` 형식

---

## index.qmd 업데이트 규칙

**새 포스트 작성 후 반드시 해당 카테고리의 `index.qmd`에 링크를 추가한다.**

### 링크 패턴

index.qmd마다 형식이 다르다. **기존 패턴을 반드시 따른다.** 대상 index.qmd를 읽고 기존 항목의 형식을 확인한 후 동일하게 작성한다.

| 패턴 | 사용처 | 형식 요약 |
|------|--------|----------|
| A: 번호 목록 | Agent | `1.  [텍스트](./서브폴더/파일.qmd)` |
| B: 날짜 + bullet | Engineering, Statistics, Governance | `* YYYY-MM-DD, [텍스트](./서브폴더/파일.qmd)` |
| C: 순수 목록 | Math, Deep_Learning | 링크 있는 항목과 없는 항목 혼재 |
| D: 구조화된 학습 경로 | Experimentation, Machine_Learning | 설명 문단 + 중첩 bullet + `1111-11-11` 미작성 항목 |

- 상대경로: 같은 폴더 `./파일.qmd`, 서브폴더 `./서브폴더/파일.qmd`, 다른 카테고리 `../Other/파일.qmd`
- index.qmd 날짜는 `YYYY-MM-DD` (YAML 헤더의 `MM/DD/YYYY`와 다름에 주의)

### Placeholder 링크

파일이 아직 없어도 논리적으로 필요한 주제는 placeholder 링크로 포함한다. 파일 생성 시 자동 연결된다.

### 크로스 카테고리 링크

하나의 `.qmd`가 여러 `index.qmd`에 링크될 수 있다. 물리적 위치는 주 카테고리에 두되, 관련 카테고리의 index.qmd에도 `../OtherCategory/파일.qmd`로 크로스 링크를 건다. YAML `categories`에 관련 카테고리를 모두 나열한다.

### Multi-disciplinary 주제

여러 분야가 융합되는 주제를 작성할 때는 **관련된 모든 카테고리의 GUIDE.md를 함께 참조**한다. 주 카테고리 GUIDE에서 콘텐츠 구조를 따르고, 관련 카테고리 GUIDE에서 용어·표기법·교재를 확인한다.

---

<task-routing>

## 태스크 라우팅

### 스킬 간 의존성

```
info-search.md (공통 전처리)
    │
    ├──→ write-post.md ──→ audit.md (후처리)
    │
    ├──→ convert-tbd.md ──→ audit.md
    │
    ├──→ answer-question.md (독립 — audit 불필요)
    │
    ├──→ organize-series.md ──→ audit.md
    │
    └──→ retrofit-post.md ──→ audit.md (내장)
                │
                └── retrofit-post는 내부 Step 마지막에 audit 항목을 자체 포함

[호출 관계 요약]
- info-search.md: 모든 태스크의 전처리 (1:N)
- audit.md: write-post, convert-tbd, organize-series의 후처리 (N:1)
- retrofit-post.md: audit 항목을 내부에 포함 (자체 완결)
- answer-question.md: info-search만 선행, 후처리 없음 (독립)
- changelog-summary.md: 선행/후처리 없음 (git 조회 독립 태스크)
```

### 공통 선행: 통합 정보 탐색 (모든 태스크)

**태스크 유형에 관계없이**, 사용자 요청을 받으면 `guides/info-search.md`의 병렬 탐색 프로토콜을 먼저 실행한다.

> **예외**: GUIDE.md 자체 수정처럼 콘텐츠 탐색이 불필요한 태스크는 info-search를 생략할 수 있다.

### 태스크별 로드 파일

| 태스크 유형 | 로드할 파일 | 핵심 절차 |
|---|---|---|
| 새 블로그 포스트 작성 | `guides/write-post.md` + 해당 Category GUIDE | info-search → Step 1~6 체크리스트 |
| 기존 포스트 보강/수정 | `guides/write-post.md` + 해당 Category GUIDE | info-search → 대상 파일 읽기 → 수정 → index.qmd 확인 |
| 주제에 대한 질문 답변 | `guides/answer-question.md` | info-search → 3개 레이어 통합 답변 |
| 시리즈 정리/재구성 | `guides/organize-series.md` + Category GUIDE | info-search → 전체 읽기 → 진단 → 설계 → 파일 처리 |
| TBD.qmd 전환 | `guides/convert-tbd.md` + 대상 Category GUIDE | info-search → 분류 → 재작성 → index 업데이트 → 초기화 |
| 기존 포스트 교정 | `guides/retrofit-post.md` + 해당 Category GUIDE | 형식 → 구조 → 콘텐츠 보강 → audit 실행 |
| 콘텐츠 품질 감사 | `guides/audit.md` + 해당 Category GUIDE | 태스크 완료 직후 → 스캔 → 보강 → 재검증 |
| 변경 이력 요약 | `guides/changelog-summary.md` | git log/diff 조회 → 기간별 분류 → 요약 보고 (info-search 생략) |
| GUIDE.md 자체 수정 | AGENT_GUIDE.md (이 파일) | 기존 규칙 보존, 추가/구조화만 (info-search 생략 가능) |

</task-routing>

---

<stop-and-ask>

## 중단 및 확인 트리거 (Stop-and-Ask)

아래 상황에서는 **즉시 작업을 멈추고 사용자에게 확인**을 받는다.

| 트리거 | 임계값 / 조건 |
|--------|---------------|
| 파일 생성 | 한 태스크에서 **3개 이상** 파일을 새로 생성해야 할 때 → 생성 예정 파일 목록을 먼저 보여주고 승인 후 진행 |
| 파일 삭제/이동 | **1개라도** 삭제·이동이 필요할 때 → 대상 목록과 사유를 보여주고 승인 후 진행 |
| index.qmd 패턴 판별 불가 | 기존 항목이 없거나 패턴(A/B/C/D)을 특정할 수 없을 때 → 판단 근거와 함께 사용자에게 질문 |
| 카테고리 분류 모호 | 포스트가 2개 이상 카테고리에 동등하게 해당할 때 → 후보 카테고리를 나열하고 사용자에게 선택 요청 |
| 가이드 파일 부재 | 로드해야 할 Category GUIDE.md 또는 skill guide가 존재하지 않을 때 → 로드 생략 후 사용자에게 알림 |

</stop-and-ask>

---

<fallback>

## 에러 및 예외 처리 (Fallback)

| 상황 | 대응 |
|------|------|
| 참조해야 할 파일(GUIDE.md, index.qmd 등)이 존재하지 않음 | 해당 로드를 생략하고, 생략 사실과 영향 범위를 사용자에게 알린다 |
| index.qmd의 링크 패턴을 자동 판별할 수 없음 | 기존 항목 2~3개를 인용하며 사용자에게 패턴 확인을 요청한다 |
| 교재 파일(`docs/book/`)이 경로에 없음 | 교재 참조 없이 진행하되, 교재 미참조임을 포스트 상단 주석 또는 사용자 메시지로 명시한다 |
| 카테고리 GUIDE.md에 파일명 규칙이 정의되지 않음 | 같은 폴더 내 기존 파일명에서 패턴을 추론하되, 추론 결과를 사용자에게 확인받는다 |
| 판단 불가 (위 어디에도 해당하지 않는 예외) | 작업을 중단하고 상황을 설명한 뒤 사용자에게 지시를 요청한다 |

</fallback>

---

## Boundaries

<boundaries>

### 할 수 있는 것

- 블로그 포스트 작성, 수정, 보강
- index.qmd에 링크 추가
- 교재 소스(`docs/book/`) 참조 및 블로그 스타일로 재작성
- 질문에 대해 블로그 → 교재 → 사전지식 순서로 답변
- 콘텐츠 gap 식별 및 작성 제안
- placeholder 링크로 미래 콘텐츠 경로 사전 설계
- 크로스 카테고리 링크 추가

### 행동 규칙 (하면 안 되는 것)

- 기존 포스트의 내용을 삭제하거나 축소
- 교재 원문을 그대로 복붙 (반드시 한다 체로 재작성)
- 블로그에 없는 내용을 블로그에서 읽은 것처럼 인용
- Category GUIDE.md를 읽지 않고 해당 카테고리 포스트 작성
- Summary MD만 읽고 블로그 작성 (Full MD 확인 필수)
- 읽지 않은 교재 구간의 내용을 원문에서 확인한 것처럼 서술
- 마크다운 헤더에 수동 번호 붙이기

### 권한 제한 (접근/수정이 금지된 것)

- `_quarto.yml`, `_metadata.yml`, `styles.css` 등 프로젝트 설정 파일 수정
- 사용자 확인 없이 대량 파일 생성 (3개 이상 → Stop-and-Ask)

</boundaries>

---

<output-format>

## 작업 완료 보고 형식 (Output Format)

모든 태스크 완료 시, 아래 형식으로 사용자에게 결과를 보고한다.

```
### 작업 결과

- **태스크**: (수행한 태스크 유형)
- **생성/수정 파일**:
  - `경로/파일명.qmd` — (변경 요약)
  - `경로/index.qmd` — (링크 추가 등)
- **주요 판단**: (에이전트가 자체 판단한 사항이 있으면 기술)
- **미완료/후속 작업**: (남은 작업이 있으면 기술, 없으면 "없음")
```

- 파일을 변경하지 않은 태스크(질문 답변 등)는 파일 목록 대신 답변 요약을 넣는다.
- 보고는 간결하게. 불필요한 반복 설명을 하지 않는다.

</output-format>

---

<self-check>

## 셀프 체크리스트 (Self-Check)

**모든 태스크 완료 직후**, 아래 항목을 에이전트 스스로 점검한다. 위반 항목이 있으면 보고 전에 수정한다.

- [ ] **절대 규칙(Always-On Rules) 5개 전체 준수** — 한다 체, 수동 번호 금지, Category GUIDE 로드, index.qmd 업데이트, 이모지 금지
- [ ] YAML 헤더 필수 필드(`title`, `description`, `categories`, `author`, `date`)가 모두 있는가?
- [ ] `date` 형식이 `MM/DD/YYYY`인가?
- [ ] index.qmd 링크 패턴이 기존 항목과 동일한가?
- [ ] 수식 `$...$` 양쪽에 공백이 있는가?
- [ ] 포스트 분량이 기본값(500줄 내외) 범위 안인가?

> `guides/audit.md`의 심층 감사는 별도 태스크로 실행한다. 위 체크리스트는 모든 태스크에 내장된 최소 검증이다.

</self-check>

---

## End-to-End 예시

> Happy Path 및 Stop-and-Ask 발동 예시는 `guides/examples.md` 참조.
