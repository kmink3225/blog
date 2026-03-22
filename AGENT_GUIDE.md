---
name: AGENT_GUIDE
type: master
version: 3.0
description: >
  LOAD at the START of any blog-related task. Covers post writing, question
  answering, category management, and book source referencing. This is the
  master guide — all category GUIDEs inherit these common rules.
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
---

# AGENT_GUIDE.md — Blog Repository Instructions

---

## 1. Project Overview

Quarto 기반 기술 블로그. `.qmd` 파일로 콘텐츠 작성, `quarto render`로 정적 HTML 생성, Netlify 배포.

- **Site**: https://kk3225.netlify.app
- **Author**: Kwangmin Kim
- **Language**: 한국어 (한다 체)

### Commands

```bash
quarto preview    # 로컬 미리보기
quarto render     # 빌드
```

### Key Files

| 파일 | 역할 |
|------|------|
| `_quarto.yml` | 프로젝트 설정, navbar, sidebar |
| `docs/blog/posts/_metadata.yml` | 포스트 공통 설정 (댓글, TOC, 배너, 날짜형식) |
| `styles.css` | 커스텀 CSS |
| `theme.scss` / `theme-dark.scss` | 테마 정의 |

### 메타데이터 상속 구조

```
_quarto.yml          ← 전체 프로젝트 설정 (navbar, sidebar, toc: true 등)
  └── docs/blog/posts/_metadata.yml  ← 포스트 공통 설정
        - 댓글: giscus (repo: kmink3225/blog)
        - 배너: #EDF3F9 배경, 검정 글씨
        - TOC: 우측, 3단계 깊이
        - 날짜 형식: "YYYY년 MM월 DD일"
        - 언어: ko
        - freeze: auto
      └── 각 .qmd 파일의 YAML 헤더  ← 파일별 설정 (우선순위 가장 높음)
```

따라서 개별 `.qmd` 파일에는 `title`, `subtitle`, `description`, `categories`, `author`, `date`만 넣으면 된다.

---

## 2. 카테고리 구조

`docs/blog/posts/` 아래에 다음 카테고리 폴더가 존재한다. 각 폴더에는 `index.qmd`(목차)와 `GUIDE.md`(작성 규칙)가 있다.

| 카테고리 폴더 | 주제 | GUIDE |
|---|---|---|
| `Agent/` | RAG, LangChain, LangGraph, Agent 개발 | O |
| `Code_Test/` | 알고리즘, SQL 문제 풀이 | O |
| `Data_Science/` | CRISP-DM, EDA, Feature Engineering | O |
| `Deep_Learning/` | CNN, RNN, Transformer, NLP, GAN | O |
| `Engineering/` | DevOps, Python, Infra, Data Engineering | O |
| `Experimentation/` | A/B Test, 인과추론, MAB | O |
| `Governance/` | 데이터 거버넌스, 품질, 표준화 | O |
| `Machine_Learning/` | 분류, 회귀, 앙상블, 비지도학습 | O |
| `Math/` | 선형대수, 미적분, 최적화 | O |
| `Statistics/` | 분포, 검정, 회귀, 종단분석, FDA | O |
| `Strategy_Frameworks/` | 비즈니스 분석, 전략 프레임워크 | O |
| `Surveilance/` | 의료기기 규제, FDA/EMA 가이드라인 | O |

> **하위 폴더 구조와 파일 배치는 각 카테고리의 `index.qmd`와 실제 폴더를 직접 확인한다.** AGENT_GUIDE에 폴더 트리를 중복 관리하지 않는다.

---

## 3. 블로그 포스트 작성 절차

새 블로그 포스트를 작성할 때 다음 순서를 따른다.

### Step 1: 카테고리 확인

- 주제에 맞는 카테고리 폴더를 결정한다
- 해당 폴더의 기존 파일을 확인하여 파일명 패턴을 파악한다

### Step 2: 카테고리 GUIDE.md 전체 읽기 (필수)

해당 카테고리 폴더의 `GUIDE.md`를 **전체** 읽는다. GUIDE.md에는 카테고리별 콘텐츠 구조, 용어 규칙, 참조 교재, 관련 주제 링크 패턴 등이 정의되어 있다. 이 파일을 읽지 않고 포스트를 작성하면 카테고리의 기존 관습과 어긋나는 결과물이 나온다.

- **읽기 범위**: 전체를 읽는다. 대부분 200줄 이내이므로 토큰 비용이 작다.
- **GUIDE.md가 없는 카테고리**: 이 단계를 건너뛴다. 단, frontmatter의 `category_guides` 목록에서 해당 카테고리에 GUIDE가 등록되어 있는지 먼저 확인한다.
- **Multi-disciplinary 주제**: 주 카테고리의 GUIDE.md를 읽은 후, 관련 카테고리의 GUIDE.md도 함께 읽는다 (아래 "Multi-disciplinary 주제 작성 원칙" 참조).

### Step 3: 기존 콘텐츠 중복 판단 (필수)

새 파일을 만들기 전에 **반드시** 기존 포스트와의 내용 중복을 확인한다.

**확인 방법**:

1. 해당 카테고리 폴더의 파일 목록을 확인한다
2. 관련 카테고리의 `index.qmd`에서 비슷한 주제의 링크가 있는지 확인한다
3. 핵심 키워드로 `Grep`을 사용해 기존 파일을 검색한다
4. **경량 스캔**: 후보 파일의 **YAML 헤더(title, description) + 마크다운 헤더(`##`, `###` 등)**만 읽어 범위를 파악한다. 본문 전체를 읽지 않는다
5. 경량 스캔 결과 겹침이 의심되는 파일만 **선택적으로 본문을 읽어** 깊이와 완성도를 판단한다

> **토큰 절약 원칙**: 유사 포스트 탐색 단계에서 모든 후보 파일의 전체 내용을 읽으면 컨텍스트가 낭비된다. 파일명 → YAML 헤더 → 마크다운 헤더 → (필요시) 본문 순서로 점진적으로 깊이를 늘린다.

**판단 기준**:

| 상황 | 조치 |
|---|---|
| 동일 주제의 파일이 이미 존재하고 내용이 상당 부분 겹침 | 새 파일 생성 금지 — 기존 파일을 보강한다 |
| 동일 주제의 포스트가 존재하지만 얕거나 불완전 | 기존 포스트를 보강 (내용 추가, 구조 개선, 코드/수식 보충) |
| 기존 파일이 있지만 다루는 관점·깊이·범위가 다름 | 기존 파일에 섹션을 추가하거나, 별도 파일로 분리하고 상호 링크한다 |
| 유사한 주제이지만 독립적으로 완결되는 내용 | 새 파일을 만들되, 기존 파일에서 크로스 링크를 건다 |
| 해당 주제의 포스트가 전혀 없다 | 새 파일을 만든다 |
| 기존 포스트가 잘못된 내용을 포함 | 기존 포스트를 수정한다 |

판단이 애매할 때는 사용자에게 "기존 포스트를 보강할지 새로 작성할지" 확인을 구한다.

**보강 시 주의사항**:

- 기존 파일의 전체 내용을 먼저 읽고 구조를 파악한다
- 중복 설명 없이 빠진 내용·깊이·예시만 추가한다
- 기존 내용을 삭제하거나 축소하지 않는다

### Step 4: 포스트 작성

- YAML 헤더 필수 필드를 모두 포함한다 (아래 "작성 규칙" 참조)
- 교재 기반 주제라면 `docs/book/`에서 관련 소스를 **카테고리에 국한하지 않고 교차 검색**하여 논리적 뼈대를 잡는다. 교재 범위 안에서 깊고 구체적으로 서술하되, 교재가 커버하지 못하는 최신/부족한 부분만 agent 사전지식으로 보완한다 (아래 "Book Source" 참조)

### Step 5: index.qmd 업데이트

- 해당 카테고리의 `index.qmd`를 읽는다
- 기존 링크 패턴(날짜 형식, 번호 형식, 들여쓰기 등)을 확인한다
- 적절한 섹션에 새 포스트 링크를 추가한다
- 섹션이 없으면 기존 구조에 맞게 새 섹션을 추가한다

### Step 6: 검증

- 상대경로가 올바른지 확인한다
- YAML 헤더의 필수 필드가 빠지지 않았는지 확인한다
- 링크 형식이 해당 index.qmd의 기존 패턴과 일치하는지 확인한다

### 수정 작업 원칙

- **실제 파일을 먼저 확인한 후 수정한다.** 규칙을 기계적으로 일괄 적용하지 않는다. 대상 파일을 읽어 해당 문제가 실제로 존재하는지 확인한 뒤에만 수정한다.
- **"혹시 모르니까" 식의 포괄적 수정 지시를 내리지 않는다.**
- **Sub-agent에게 작업을 위임할 때도 동일한 원칙을 적용한다.**

---

## 4. 작성 규칙

### YAML 헤더 (필수)

```yaml
---
title: "제목"
subtitle: "부제목"
description: |
  1-3문장 설명. 이 글에서 다루는 핵심 내용을 요약한다.
categories:
  - Category1
  - Category2
author: Kwangmin Kim
date: MM/DD/YYYY
---
```

- `title`, `description`, `categories`, `author`, `date`는 필수
- `format`, `toc`, `code-fold` 등은 `_metadata.yml`과 `_quarto.yml`에서 상속되므로 개별 파일에 넣지 않아도 됨
- `date`는 `MM/DD/YYYY` 형식 사용 (예: `03/18/2026`)
- 아직 작성하지 않은 예정 글의 date는 `1111-11-11` placeholder 사용

### 파일명 규칙

카테고리별로 파일명 패턴이 다르다. **같은 폴더 내에서는 기존 패턴을 따른다.**

| 패턴 | 예시 | 사용처 |
|------|------|--------|
| `번호-토픽명.qmd` | `01-TopicName.qmd` | Agent, Engineering/DevOps, Statistics |
| `번호.토픽명.qmd` | `01.topic-name.qmd` | Engineering/Data_Engineering |
| `날짜_토픽명.qmd` | `2023-01-17_topic.qmd` | 일부 카테고리 |
| `유형_난이도_문제명.qmd` | `hash_level1_pocketmon.qmd` | Code_Test |

**패턴 결정 방법**: 새 포스트를 넣을 폴더의 기존 파일명을 확인하고 동일한 패턴을 사용한다. 각 카테고리 GUIDE.md에 상세 패턴이 정의되어 있다.

### 콘텐츠 스타일

- **한다 체 사용** (설명체): `~한다`, `~이다`, `~된다`
- **경어체 금지**: `~합니다`, `~입니다`, `~하세요` 사용하지 않음
- **이모지 사용 금지**
- **섹션 헤더에 수동 번호 절대 금지**: `_quarto.yml`에서 `number-sections: true`가 전역 설정되어 있으므로, 수동 번호를 붙이면 이중 번호가 생긴다. **`##`, `###`, `####` 등 모든 수준의 마크다운 헤더에 숫자+마침표(`1.`, `2.` 등)를 접두사로 붙이지 않는다.** 이 규칙은 예외 없이 적용된다.

<fix-honorific-style>

```
# WRONG: 경어체
Git은 분산형 버전 관리 시스템입니다.

# CORRECT: 한다 체
Git은 분산형 버전 관리 시스템이다.
```

</fix-honorific-style>

<fix-manual-section-number>

```
# WRONG: 모든 수준에서 수동 번호 금지
## 1. 개요                    ← 렌더링 시 "1. 1. 개요"로 이중 표시
### 2. 평가의 주관성           ← 렌더링 시 "1.2. 2. 평가의 주관성"
#### 3. 세부 항목              ← 동일 문제

# CORRECT: 번호 없이 제목만 작성
## 개요
### 평가의 주관성
#### 세부 항목
```

</fix-manual-section-number>

### 줄 개행 규칙

Quarto(Markdown)에서 단순 줄바꿈은 렌더링 시 무시된다. **줄 끝에 공백 2칸(`  `)을 반드시 추가**하여 `<br>` 개행을 보장한다.

<fix-line-break>

```
# WRONG: 줄 끝에 공백 없음 → 렌더링 시 한 줄로 합쳐짐
첫 번째 줄
두 번째 줄

# CORRECT: 줄 끝에 공백 2칸 추가
첫 번째 줄
두 번째 줄
```

</fix-line-break>

- 본문의 모든 줄(문단 내 줄바꿈이 필요한 곳)에 trailing 공백 2칸을 붙인다
- 빈 줄(`\n\n`)로 구분되는 문단 사이에는 불필요하다
- 코드 블록, YAML 헤더, callout 내부에서는 적용하지 않는다
- bullet list(`- `, `* `) 항목은 자체 블록이므로 trailing 공백이 불필요하다

### 주장-근거-해석 원칙

모든 서술은 **주장(claim) → 근거(evidence) → 해석(interpretation)** 구조를 따른다. 어느 하나라도 빠지면 독자의 신뢰를 잃는다.

**규칙 1: 주장에는 반드시 "왜"가 한 문장 이상 붙어야 한다**

<fix-claim-without-why>

```
# WRONG: 주장만 있고 왜가 없다
동일한 질의에 동일한 설정을 적용해도 LLM 출력이 달라진다.
따라서 복수 회 반복이 필요하다.

# CORRECT: 왜 문제인지 구체적 시나리오로 보여준다
동일한 질의에 동일한 설정을 적용해도 LLM 출력이 달라진다.
BM25 가중치 0.3 vs 0.5를 비교하는 실험에서, 각 설정을 1회만 실행하면
0.3이 우연히 좋은 응답을 뽑고 0.5가 나쁜 응답을 뽑는 경우를
처치 효과로 오인할 수 있다. 반복 없이 내린 결론은 동전 한 번 던져서
정책을 결정하는 것과 구조적으로 같다.
```

</fix-claim-without-why>

**규칙 2: 숫자는 반드시 해석과 붙어야 한다. 숫자 단독은 정보가 아니라 소음이다**

<fix-number-without-interpretation>

```
# WRONG: 숫자만 나열
| 기업 내부 Agent | 수백 건 | 수개월 이상 |

# CORRECT: 숫자 → 해석 → 시사점 (so what)
| 기업 내부 Agent | 수백 건 | 수개월 이상 |

하루 50건의 질의를 받는 Agent에서 MDE=10% 실험을 설계하면,
그룹당 약 1,500건이 필요하고 이는 편도 30일이 걸린다.
이 기간 동안 프롬프트나 문서가 업데이트되면 실험 자체가 오염되므로,
Sequential Testing이나 오프라인 선스크리닝이 선택이 아닌 필수가 된다.
```

</fix-number-without-interpretation>

**규칙 3: 구체적 사례(프로젝트, 도메인)는 일반론을 증명하는 구조로 배치한다. 일반론 옆에 병렬로 나열하지 않는다**

<fix-example-without-connection>

```
# WRONG: 일반론과 사례가 병렬 나열 — 왜 여기 있는지 불명확
Agent는 모델 × 프롬프트 × top-k × 청킹 등 다층 파라미터가 상호작용한다.

| Agent | 도메인 | 태스크 |
| QnA Chatbot | 표준화 | Q&A |
| Data Std Helper | 메타데이터 | 추천 |

# CORRECT: 일반론 → 사례가 일반론을 구체화 → 시사점
Agent는 모델 × 프롬프트 × top-k × 청킹 등 다층 파라미터가 상호작용한다.
3 × 4 × 3 × 2 = 72개 조합을 모두 실험하려면, 그룹당 200건 기준으로
72 × 200 = 14,400건이 필요하다. 하루 50건이면 288일, 거의 1년이다.
이것이 Fractional factorial이나 Thompson Sampling이 선택이 아닌 필수인 이유다.

| Agent | 도메인 | 태스크 | 실험 설계 차이 |
| QnA Chatbot | 표준화 | Q&A | 정답이 명확 → Hit Rate로 실험 가능 |
| Insilico | 코드 | 분석·설명 | 주관 판단 → 자동 지표만으로 불충분 |

같은 A/B 프레임이어도 Agent마다 실험 설계가 달라지는 이유가 여기 있다.
```

</fix-example-without-connection>

**규칙 4: 추상적 개념에는 반드시 직관적 설명(비유, 반사실, 일상 대응)을 붙인다**

수식이나 정의만으로는 "왜 이것이 의미 있는가"를 전달할 수 없다. 도메인 지식이 없는 독자도 핵심 아이디어를 파악할 수 있도록, 추상적 개념이 등장하는 **바로 그 위치에** 직관적 설명을 삽입한다.

직관적 설명이 **필수**인 경우:

| 상황 | 직관적 설명 유형 | 배치 위치 |
|------|-----------------|-----------|
| 수식이 처음 등장할 때 | 수식이 **뜻하는 바**를 일상어로 1~2문장 | 수식 직후 |
| 통계적 가정 (SUTVA, positivity 등) | "이 가정이 깨지면 무슨 일이 생기는가" 반사실 시나리오 | 가정 정의 직후 |
| 알고리즘의 핵심 메커니즘 | 일상적 비유 (예: 식당 선택, 동전 던지기 등) | 알고리즘 설명 시작부 |
| 보정 방법 (Bonferroni, Alpha Spending 등) | "보정하지 않으면 어떻게 되는가" 반사실 + "보정이 하는 일"을 비유로 | 보정 소개 직후 |
| 지표/점수 (κ, ICC, Cohen's d 등) | 해당 값이 실무에서 **체감되는 차이**로 번역 | 점수 정의 직후 |

<fix-abstract-without-intuition>

```
# WRONG: 수식/정의만 있고 직관 없음
Alpha spending function α*(t)는 정보 분율 t에서 누적으로 소비된 α의 양을 정의한다.
α*(t): [0,1] → [0,α]

# CORRECT: 수식 + 직관을 바로 붙인다
Alpha spending function α*(t)는 정보 분율 t에서 누적으로 소비된 α의 양을 정의한다.
α*(t): [0,1] → [0,α]

직관적으로, α는 실험 전체에서 쓸 수 있는 "오판 허용 예산"이다.
한정된 예산(α=0.05)을 중간 분석마다 조금씩 꺼내 쓰는 구조이므로,
일찍 많이 쓰면 나중에 남는 예산이 줄어든다. O'Brien-Fleming은
초반에 거의 쓰지 않고 마지막에 몰아 쓰는 "절약형" 전략이다.
```

</fix-abstract-without-intuition>

**자기 점검**: 수식, 가정, 알고리즘, 보정 방법, 지표가 등장할 때마다 "도메인 비전문 독자가 이 단락만 읽고 핵심 아이디어를 말할 수 있는가?"를 확인한다. 말할 수 없으면 비유 또는 반사실 시나리오를 추가한다.

**요약: 모든 서술 블록에 대한 자기 점검**

| 점검 항목 | 질문 | 미충족 시 조치 |
|-----------|------|---------------|
| 주장 → 왜 | "왜 그게 문제인가?"에 답하는가 | 시나리오 또는 반사실적 비교를 추가한다 |
| 숫자 → 해석 | 숫자 뒤에 "so what"이 있는가 | 실무적 임팩트(기간, 비용, 위험)로 번역한다 |
| 사례 → 연결 | 이 사례가 왜 여기 있는지 독자가 알 수 있는가 | 사례가 일반론을 증명하는 구조로 재배치한다 |
| 나열 → 흐름 | 목록이 단순 나열인가, 논리 흐름인가 | 항목 간 인과·순서 관계를 명시한다 |
| 추상 → 직관 | 수식·가정·알고리즘 뒤에 비유 또는 반사실이 있는가 | 일상어 비유 또는 "이것이 없으면?" 시나리오를 추가한다 |

### 수식 (LaTeX)

<fix-latex-spacing>

```
# WRONG: $ 양쪽에 공백 없음 → Quarto가 LaTeX로 인식 못 함
모수$\theta$를 추정한다

# CORRECT: $ 양쪽에 공백
모수 $\theta$ 를 추정한다

# 예외: 구두점은 공백 없이 붙어도 됨
($\theta$), $\theta$,
```

</fix-latex-spacing>

- 인라인 수식: `$수식$` — **`$` 양쪽에 반드시 공백을 둔다**
- 블록 수식: `$$수식$$`
- 교재 소스에서 가져온 수식 중 깨진 것이 있을 수 있다. 의미가 불명확한 수식은 교과서 맥락에서 재구성한다
- 교재 인용 시 `(저자, 연도, Ch.N)` 형식을 사용한다 (예: `(Casella & Berger, 2002, Ch.5)`)

### 코드 블록

````markdown
```bash
# shell 명령
poetry install
```

```python
# Python 코드
import pandas as pd
```

```toml
# 설정 파일
[tool.poetry]
name = "my-project"
```
````

실행 가능한 코드 블록이 필요한 경우:

````markdown
```{python}
#| eval: true
import pandas as pd
```
````

### Quarto Callout 블록

```markdown
::: {.callout-tip}
팁 내용
:::

::: {.callout-warning}
경고 내용
:::

::: {.callout-important}
중요 내용
:::

::: {.callout-note}
참고 내용
:::
```

---

## 5. index.qmd 업데이트 규칙

**새 포스트를 작성한 후 반드시 해당 카테고리의 `index.qmd`에 링크를 추가해야 한다.**

### 링크 추가 패턴

index.qmd마다 링크 형식이 다르다. **기존 패턴을 반드시 따른다.**

#### 패턴 A: 번호 목록 + 상대경로 (Agent)

```markdown
### 섹션 제목

1.  [링크텍스트](./서브폴더/파일명.qmd)
2.  [링크텍스트](./서브폴더/파일명.qmd)
```

- 번호는 `1.  ` (숫자+마침표+공백2칸)
- 상대경로는 `./`로 시작
- 계층 구조: `##` → `###` → `####` 순서로 섹션 분류

#### 패턴 B: 날짜 + bullet list (Engineering, Statistics, Governance)

```markdown
## 섹션 제목

* YYYY-MM-DD, [링크텍스트](./서브폴더/파일명.qmd)
* YYYY-MM-DD, [링크텍스트](./서브폴더/파일명.qmd)
```

- `* ` (별표+공백)으로 시작
- 날짜는 `YYYY-MM-DD` 형식 (YAML 헤더의 `MM/DD/YYYY`와 다름에 주의)
- 하위 항목은 `  * ` (공백2칸+별표+공백)으로 들여쓰기

#### 패턴 C: 순수 목록 (Math, Deep_Learning)

```markdown
## 섹션 제목

* YYYY-MM-DD, [링크텍스트](./서브폴더/파일명.qmd)
1.  링크 없는 텍스트 항목
```

- 링크가 있는 항목과 없는 항목(미작성)이 혼재

#### 패턴 D: 구조화된 학습 경로 (Experimentation, Machine_Learning)

```markdown
## 섹션 제목

설명 텍스트

* [링크텍스트](./서브폴더/파일명.qmd)
  * YYYY-MM-DD, [하위 링크](./서브폴더/파일명.qmd)
  * 1111-11-11, [미작성 항목](./서브폴더/파일명.qmd)
```

- 설명 문단 포함
- 중첩 bullet 사용
- 미작성 항목은 `1111-11-11` 날짜 사용

### 상대경로 규칙

| 포스트 위치 | index.qmd 위치 | 상대경로 |
|---|---|---|
| 같은 폴더 | `Category/index.qmd` | `./파일명.qmd` |
| 서브폴더 | `Category/index.qmd` | `./서브폴더/파일명.qmd` |
| 다른 카테고리 | `Category/index.qmd` | `../OtherCategory/파일명.qmd` |

<fix-index-link-pattern>

```
# WRONG: 기존 패턴이 * 인데 - 로 작성
- 2026-03-21, [제목](./파일명.qmd)

# CORRECT: 기존 패턴을 그대로 따름
* 2026-03-21, [제목](./파일명.qmd)

# WRONG: index.qmd에 날짜가 YAML 형식(MM/DD/YYYY)
* 03/21/2026, [제목](./파일명.qmd)

# CORRECT: index.qmd 날짜는 YYYY-MM-DD 형식
* 2026-03-21, [제목](./파일명.qmd)
```

</fix-index-link-pattern>

### Placeholder 링크 원칙

**파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 포스트의 "관련 주제" 섹션에서도 선행/후속 지식으로 필요하지만 아직 작성되지 않은 포스트의 경로를 미리 지정해 둔다. 파일이 생성되면 링크가 자연스럽게 연결된다.

### 크로스 카테고리 링크

**하나의 .qmd 파일이 여러 index.qmd에 중복으로 링크될 수 있다.** 파일은 물리적으로 한 폴더에만 존재하지만, 논리적으로 관련된 모든 카테고리의 index.qmd에서 참조한다. 크로스 카테고리 링크 시 `../OtherCategory/파일명.qmd` 형식을 사용한다.

### Multi-disciplinary 주제 작성 원칙

여러 분야가 융합되는 주제를 작성할 때는 해당 주제와 관련된 **모든 카테고리의 GUIDE.md를 함께 참조**한다.

| 주제 | 주 카테고리 | 함께 참조할 GUIDE |
|---|---|---|
| A/B 테스트 | Experimentation | Statistics, Engineering, Data_Science |
| 생존 분석 | Statistics | Experimentation, Machine_Learning, Deep_Learning |
| 종단 데이터 | Statistics | Machine_Learning, Deep_Learning, Experimentation |
| RAG 시스템 | Agent | Engineering, Math |
| 모델 배포 | Engineering | Machine_Learning, Data_Science, Experimentation |
| 데이터 품질 | Governance | Statistics, Engineering |
| 의료 AI 규제 | Surveilance | Statistics, Deep_Learning |

포스트 작성 시:

1. 주 카테고리의 GUIDE에서 콘텐츠 구조를 따른다
2. 관련 카테고리의 GUIDE에서 해당 분야의 용어, 표기법, 참조 교재를 확인한다
3. "관련 주제" 섹션에서 모든 관련 카테고리의 포스트를 크로스 링크한다

---

## 6. Book Source (교재 활용)

`docs/book/` 폴더에 교과서 md 파일이 있다.

### 왜 교재를 넣었는가

agent의 사전지식은 너무 방대하여, 제약 없이 쓰면 불필요한 지식이 섞여 포커스가 흐려진다. **교재는 agent 지식의 범위를 좁히고 구체성을 높이는 경계(boundary) 역할**을 한다. 교재가 다루는 영역 안에서 깊고 정확하게 서술하되, 교재가 커버하지 못하는 최신/부족한 부분만 agent 사전지식으로 채운다.

### 활용 철학

1. **범위 제한**: 블로그 작성 시 교재가 정의하는 범위 안에서 논리를 전개한다. 교재에 없는 방향으로 지식을 확장할 때는 명확한 이유가 있어야 한다.
2. **교차 검색·조합**: 하나의 주제를 다룰 때 **카테고리에 국한하지 않고 전체 book 소스를 교차 검색**한다. 예를 들어 "인과추론 기반 A/B 테스트" 포스트라면 `epidemiology/`(Hernan), `behavioral_analysis/`(Kohavi), `statistics/`(Casella), `strategy_frameworks/`(Kahneman)를 함께 참조할 수 있다.
3. **사전지식 보완**: 교재 내용이 outdated되었거나 누락된 최신 발전이 있을 때만 agent 지식으로 수정·보완한다. 변경이 큰 경우 본문에 간략히 언급한다.

| 판단 | 행동 |
|------|------|
| 교재 내용이 여전히 유효하다 | 교재의 논리 체계를 유지하고 블로그 스타일로 재작성 |
| 교재 내용이 outdated되었다 | agent의 최신 지식으로 수정하고, 변경이 큰 경우 본문에 간략히 언급 |
| 교재에 누락된 최신 발전이 있다 | agent가 보완하여 추가 (새로운 방법론, 도구, best practice 등) |
| 교재의 표기·용어가 현재 관행과 다르다 | 현재 통용되는 표기·용어로 업데이트 |
| 주제가 여러 교재에 걸쳐 있다 | 관련 교재를 모두 교차 참조하여 통합적으로 서술 |

### 운영 규칙

- 렌더링 대상 아님 (`_quarto.yml`에서 제외)
- 블로그 스타일(한다 체)로 재작성한다
- 인용 시 `(저자, 연도, Ch.N)` 형식 사용
- 교재 내용이 outdated되었거나 현재 best practice와 다른 경우, agent의 최신 사전지식으로 수정·보완한다

### 그룹 구조

| 폴더 | 교재 | 분야 |
|------|------|------|
| `statistics/` | Casella & Berger | 수리통계 |
| `linear_algebra/` | Strang, Magnus, Matrix Cookbook | 선형대수, 행렬 미분 |
| `generalized_linear_model/` | McCullagh & Nelder, Faraway | GLM, 회귀 |
| `mixed_model/` | Hedeker & Gibbons | 종단 데이터, 반복측정 |
| `survival/` | Kleinbaum, Klein, Hosmer, Collett | 생존 분석 |
| `epidemiology/` | Hernan, Woodward, Schulz, Maxwell, Buisson | 인과추론, 역학, 실험설계, AB test |
| `bayesian/` | Gelman, Downey | 베이지안 |
| `functional_data_analysis/` | Ramsay×2, Kokoszka | 함수형 데이터 분석 |
| `machine_learning/` | Hastie(ESL), James(ISLR), Bishop(PRML), Murphy(PMLIntro/Advanced/Supp) | 기계학습 |
| `deep_learning/` | Goodfellow, Zhang(D2L), Raschka, Sutton(RL), Jurafsky(SLP) | 딥러닝, NLP, RL |
| `data_science/` | Huyen(AIEng/DesigningML), Provost | 데이터 사이언스, ML 시스템, AI 엔지니어링 |
| `strategy_frameworks/` | Porter, Rumelt, Kahneman, Hurley, Lipton, Parrish×3, Dixit, Lafley | 전략, 논리, 멘탈 모델, 게임이론 |
| `behavioral_analysis/` | Cooper(ABA), Kohavi(ABTest), Montgomery(DOE), Thaler(Nudge) | 행동분석, A/B 테스트, 실험설계 |
| `psychology/` | Eysenck, Cialdini, Morling, PAIR, HAX | 인지심리, 설득, 연구방법, AI UX |
| `linguistics/` | Sidnell, Huang, McEnery | 대화분석, 화용론, 코퍼스 언어학 |
| `governance/` | DAMA DMBOK | 데이터 거버넌스 |
| `ontology/` | Robinson(GraphDB), Kejriwal(KG), Keet(Ontology), CodeQL, CPG, KR | 지식 그래프, 온톨로지, 코드 분석 |

### 2-Layer 교재 참조 체계

각 교재 폴더에는 두 종류의 파일이 있다:

| 파일 유형 | 명명 규칙 | 역할 |
|---|---|---|
| **Summary MD** | `*-summary.md` | 목차 + 챕터별 요약 + 키워드 + **상세 요약(10~15문장)** + Marker 세부 목차. **항상 먼저 읽는다** (지도 역할) |
| **Full MD** | `*_full.md` | PDF→MD 변환 원본. 챕터 단위로 상세 내용 참조 시 사용 |

#### Summary MD 구조

각 Summary MD는 다음 구조를 따른다:

```yaml
---
name: "책 제목"
type: book-summary
authors: "저자"
year: 2024
sources:                                    # 변환 소스 정보
  - file: "Author-Book_marker_full.md"
    tool: Marker
  - file: "Author-Book_azure_full.md"
    tool: Document Intelligence
---
```

각 챕터 항목:
- **핵심**: 2~3문장 핵심 요약
- **키워드**: 검색용 태그
- **상세**: → `Full MD 파일명` Ch N (L:라인번호) + 10~15문장 한국어 요약 (Full MD 본문 기반)

파일 끝에 `## Marker 세부 목차` 섹션이 있는 경우, `L:숫자`로 Full MD의 세부 섹션 라인을 직접 참조할 수 있다.

### 교재 참조 절차

```
포스트 주제 결정
    ↓
Summary MD 읽기 (목차 + 키워드 스캔)
    ↓
관련 챕터/섹션 특정 (키워드 매칭)
    ↓
읽기 깊이 판단 (아래 기준표 참조)
    ↓
Full MD 읽기 (선택적 구간 or 챕터 전체)
    ↓
블로그 스타일로 재작성 + 인용
```

### 읽기 깊이 판단 기준

| 교재 유형 | 주제 유형 | 읽기 전략 | 이유 |
|---|---|---|---|
| 표준 교재 (Casella, Strang 등) | 잘 알려진 개념 (MLE, CLT, SVD) | **선택적 읽기** — 정의/정리/예시 구간만 (100~200줄) | 사전학습 커버리지가 높음 |
| 표준 교재 | 덜 알려진 세부 주제 | **확장 읽기** — 관련 섹션 전체 (300~500줄) | 세부 전개는 부정확할 수 있음 |
| Niche 교재 (Hedeker, Kokoszka 등) | 모든 주제 | **챕터 전체 읽기** | 사전학습 커버리지가 얇음 |
| 한국어/미공개 자료 | 모든 주제 | **챕터 전체 읽기** | 사전학습에 거의 없음 |

**판단이 애매할 때는 더 많이 읽는 쪽을 선택한다.** 토큰 절약보다 정확성이 우선이다.

### 선택적 읽기 시 구간 결정 방법

선택적 읽기를 할 때는 다음 순서로 읽을 구간을 결정한다:

1. Summary의 line 번호로 챕터 시작점을 확인한다
2. 챕터 시작점에서 **200줄만 먼저 읽어** 목차 구조(섹션 헤딩)를 파악한다
3. 필요한 섹션의 시작/끝 line을 특정한다
4. 해당 구간만 읽는다
5. 부족하면 추가 구간을 읽는다

**주의사항:**

- Summary만으로 답하지 않는다 — 요약은 탐색 도구이지 답변 근거가 아니다
- Summary의 Contents 목차에 없는 챕터를 날조하지 않는다
- 여러 교재를 교차 참조할 때는 각 교재의 Summary를 먼저 비교하여 가장 적합한 소스를 선택한다
- 선택적 읽기 후 블로그를 작성할 때, **읽지 않은 구간의 내용을 사전학습 지식으로 채우면서 원문에서 읽은 것처럼 서술하지 않는다.** 원문에서 확인하지 않은 세부사항은 생략하거나, 필요하면 추가로 읽는다

### Book Source 유지보수

교재 소스는 정적 자산이 아니라 지속적으로 관리해야 한다. 다음 상황에서 유지보수가 필요하다:

#### 1. 새 교재 추가 시

새 PDF 변환 파일(`_full.md`)이 `docs/book/`에 추가되면:
1. 해당 책의 `*-summary.md`를 생성한다 (YAML frontmatter + 챕터별 핵심/키워드/상세)
2. `sources:` 필드에 변환 파일 정보를 추가한다
3. Marker 변환본이 있으면 `## Marker 세부 목차` 섹션을 추가한다
4. 이 파일(AGENT_GUIDE.md)의 그룹 구조 테이블을 업데이트한다
5. 해당 카테고리의 `GUIDE.md`에 교재 레퍼런스를 추가한다

#### 2. 기존 교재의 변환 품질 개선 시

더 좋은 변환 도구로 재변환한 경우(예: Azure → Marker):
1. 새 `_full.md` 파일을 추가하고, summary의 `sources:`에 추가한다
2. 상세 요약의 라인 참조(`L:숫자`)를 새 파일 기준으로 업데이트한다
3. Marker 세부 목차를 추가/갱신한다

#### 3. 정기 점검

새 세션 시작 시 사용자가 요청하면, 다음을 확인한다:
- `_full.md`가 있지만 대응하는 `*-summary.md`가 없는 파일 (누락된 summary)
- `*-summary.md`의 `**상세**` 필드에 요약 텍스트가 없는 챕터 (미보강)
- `sources:` 필드가 누락된 summary

<fix-book-source-misuse>

```
# WRONG: 교재 원문을 그대로 복붙
"The maximum likelihood estimator is obtained by maximizing
the log-likelihood function..." (원문 영어 그대로)

# CORRECT: 블로그 스타일(한다 체)로 재작성 + 인용
최대가능도 추정량은 로그가능도 함수를 최대화하여 구한다
(Casella & Berger, 2002, Ch.7).

# WRONG: Summary만 읽고 답변 (요약은 탐색 도구이지 근거가 아님)
Summary에 따르면 Ch.5에서 MLE를 다룬다 → MLE는 ...이다

# CORRECT: Full MD에서 해당 구간을 읽은 뒤 재작성
Full MD Ch.5의 정의/정리를 읽고 → 한다 체로 재구성
```

</fix-book-source-misuse>

---

## 7. 질문 응답 가이드

사용자가 특정 주제에 대해 질문하면, **블로그에 이미 작성된 콘텐츠를 먼저 검색**하여 답변의 근거로 활용한다. 이 블로그는 사용자의 학습 자산이므로, 일반적인 지식보다 블로그에 정리된 내용을 우선 참조한다.

### 검색 순서

1. **카테고리 추정**: 질문 주제가 어느 카테고리에 해당하는지 판단한다
2. **index.qmd 스캔**: 해당 카테고리의 `index.qmd`에서 관련 항목을 찾는다
3. **키워드 검색**: `Grep`으로 `docs/blog/posts/` 전체에서 핵심 키워드를 검색한다
4. **크로스 카테고리 확인**: Multi-disciplinary 주제는 여러 카테고리를 교차 검색한다

### 지식 우선순위

| 소스 | 우선순위 | 사용 방식 |
|------|----------|-----------|
| 블로그 포스트 | 1순위 | 내용을 기반으로 답변 + 파일 경로 제시 |
| 교재 소스 (`docs/book/`) | 2순위 | 블로그에 없지만 교재에 있는 내용은 교재를 참조하여 답변. 카테고리에 국한하지 않고 전체 book 소스를 교차 검색·조합 |
| agent 사전지식 | 3순위 | 블로그·교재 모두 없는 부분만 보완. "블로그에 아직 없다" 명시 |

### 콘텐츠 gap 발견 시

| 상황 | 행동 |
|---|---|
| 관련 포스트가 존재하고 답변에 충분 | 포스트 내용 기반 답변 + 링크 제시 |
| 관련 포스트가 존재하지만 일부만 다룸 | 포스트 기반 답변 + 부족한 부분 보충 + "이 부분은 블로그에 아직 없다" 명시 |
| 관련 포스트가 전혀 없음 | 일반 지식으로 답변 + "이 주제는 블로그에 아직 정리되지 않았다. 작성할까?" 제안 |
| `index.qmd`에 placeholder(1111-11-11)로만 존재 | "이 주제는 계획되어 있지만 아직 작성되지 않았다" + 일반 지식으로 답변 + 작성 제안 |

### 주의사항

- **블로그 내용과 일반 지식을 혼동하지 않는다.** 블로그에 작성된 내용을 인용할 때는 파일 경로를 명시한다.
- **블로그의 용어와 표기법을 따른다.** 블로그에서 "한다 체"를 사용하더라도 답변은 대화체로 한다. 다만 블로그 내용을 인용할 때는 원문 그대로 제시한다.

---

## 8. 작업 패턴

### 임시 메모 → 블로그 전환

사용자가 AI agent와의 대화에서 유용한 정보를 `docs/blog/posts/TBD.qmd`에 저장해 둘 수 있다. Agent는 이를 주제별 정식 블로그 포스트로 전환한다.

**전환 절차**:

1. **임시 파일 읽기** — 내용을 파악하고 주제별로 분리
2. **중복 확인** — 이미 정식 포스트로 작성된 내용이 있는지 대조
3. **분류** — 적절한 카테고리 폴더에 매핑
4. **재작성 및 보강**:
   - 대화 요소 제거 ("당신", "네", 독자에게 던지는 질문 등)
   - 한다 체로 통일, YAML 헤더 포함
   - 단순 스타일 변환이 아니라 배경 설명, 수식, 코드, 다이어그램 등을 보강
   - 독자가 메모의 맥락을 모르더라도 포스트만으로 완결되도록 작성
5. **index.qmd 업데이트**
6. **TBD.qmd 초기화** — 전환 완료 후 빈 템플릿 상태로 되돌린다 (파일 삭제 금지)

**임시 파일 규칙**:

- 경로: `docs/blog/posts/TBD.qmd` (고정)
- 하나의 파일에 여러 주제를 누적하며, 주제 간 구분은 `---` 또는 `## 제목`
- YAML 헤더에 `draft: true`를 포함하여 빌드에서 제외
- 전환 후에도 파일은 삭제하지 않고 빈 상태로 유지

### 시리즈 블로그 정리

블로그 시리즈를 체계적으로 정리할 때 따르는 패턴:

1. **기존 파일 전체 읽기** — 현재 상태 파악
2. **문제 진단** — 중복, 잘못된 내용, 누락된 주제, 비체계적 구성 식별
3. **구조 설계** — 기초 → 핵심 → 심화 → 실전 순서로 배치
4. **파일 처리**: 잘 된 파일은 유지, 잘못된 파일은 재작성, 누락된 주제는 추가
5. **요약 테이블 제공** — 작업 결과를 사용자에게 보고

---

## 9. 태스크 라우팅

사용자 요청의 유형에 따라 참조할 가이드와 절차가 다르다.

| 태스크 유형 | 로드할 가이드 | 핵심 절차 |
|---|---|---|
| 새 블로그 포스트 작성 | AGENT_GUIDE + 해당 Category GUIDE | Step 1~6 체크리스트 |
| 기존 포스트 보강/수정 | AGENT_GUIDE + 해당 Category GUIDE | 대상 파일 읽기 → 수정 → index.qmd 확인 |
| 주제에 대한 질문 답변 | AGENT_GUIDE §7 (질문 응답 가이드) | 블로그 검색 → 교재 검색 → 사전지식 순 |
| 시리즈 정리/재구성 | AGENT_GUIDE §8 (시리즈 정리) + Category GUIDE | 전체 읽기 → 진단 → 설계 → 파일 처리 |
| TBD.qmd 전환 | AGENT_GUIDE §8 (임시 메모 전환) + 대상 Category GUIDE | 분류 → 재작성 → index 업데이트 → 초기화 |
| GUIDE.md 자체 수정 | AGENT_GUIDE (이 파일) | 기존 규칙 보존, 추가/구조화만 |

---

## 10. Boundaries

<boundaries>

### 할 수 있는 것

- 블로그 포스트 작성, 수정, 보강
- index.qmd에 링크 추가
- 교재 소스(`docs/book/`) 참조 및 블로그 스타일로 재작성
- 질문에 대해 블로그 → 교재 → 사전지식 순서로 답변
- 콘텐츠 gap 식별 및 작성 제안
- placeholder 링크로 미래 콘텐츠 경로 사전 설계
- 크로스 카테고리 링크 추가

### 할 수 없는 것

- 기존 포스트의 내용을 삭제하거나 축소
- 교재 원문을 그대로 복붙 (반드시 한다 체로 재작성)
- 블로그에 없는 내용을 블로그에서 읽은 것처럼 인용
- 사용자 확인 없이 대량 파일 생성
- `_quarto.yml`, `_metadata.yml`, `styles.css` 등 프로젝트 설정 파일 수정
- Category GUIDE.md를 읽지 않고 해당 카테고리 포스트 작성
- Summary MD만 읽고 블로그 작성 (Full MD 확인 필수)
- 읽지 않은 교재 구간의 내용을 원문에서 확인한 것처럼 서술
- 마크다운 헤더(`##`, `###`, `####`)에 수동 번호 붙이기 (`## 1. 제목`, `### 2. 제목` 등 — `number-sections: true` 전역 설정과 충돌)

</boundaries>
