---
name: AGENT_GUIDE
type: master
version: 4.0
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
---

# AGENT_GUIDE.md — Blog Repository Instructions (공통 코어)

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

## 3. 작성 규칙

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

## 4. index.qmd 업데이트 규칙

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

### 복수 카테고리 태깅

**하나의 포스트는 여러 카테고리에 동시에 속할 수 있다.** 포스트의 내용이 여러 분야에 걸쳐 있으면 YAML 헤더의 `categories` 필드에 관련 카테고리를 모두 나열한다. 포스트는 반드시 하나의 카테고리 폴더에만 물리적으로 존재해야 한다는 제약은 없다 — 물리적 위치는 **주 카테고리** 폴더에 두되, 논리적으로 관련된 모든 카테고리를 태깅하고 각 카테고리의 index.qmd에 크로스 링크를 건다.

```yaml
# 예시: Math 폴더에 물리적으로 존재하지만, ML/DS/Statistics에도 관련
categories:
  - Mathematics          # 주 카테고리 (물리적 위치)
  - Machine Learning     # 관련 카테고리
  - Data Science         # 관련 카테고리
  - Statistics           # 관련 카테고리
```

| 항목 | 규칙 |
|------|------|
| 물리적 위치 | 주 카테고리 폴더에 둔다 |
| YAML `categories` | 관련된 모든 카테고리를 나열한다 |
| index.qmd 링크 | 주 카테고리 + 관련 카테고리의 index.qmd **모두**에 크로스 링크를 건다 |
| 주 카테고리 판단 기준 | 포스트의 **출발점이 되는 개념**이 속한 분야. 응용이 아닌 핵심 원리 기준 |

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
| 함수 구조와 추정 | Math | Machine_Learning, Data_Science, Statistics |

포스트 작성 시:

1. 주 카테고리의 GUIDE에서 콘텐츠 구조를 따른다
2. 관련 카테고리의 GUIDE에서 해당 분야의 용어, 표기법, 참조 교재를 확인한다
3. YAML `categories`에 관련 카테고리를 모두 나열한다
4. "관련 주제" 섹션에서 모든 관련 카테고리의 포스트를 크로스 링크한다
5. 관련 카테고리의 index.qmd에도 크로스 링크를 추가한다

---

## 5. 태스크 라우팅

### 공통 선행: 통합 정보 탐색 (모든 태스크)

**태스크 유형에 관계없이**, 사용자 요청을 받으면 `guides/info-search.md`의 병렬 탐색 프로토콜을 먼저 실행한다. 탐색 결과를 확보한 상태에서 아래 태스크별 절차를 진행한다.

```
사용자 요청
    ↓
guides/info-search.md 실행 (블로그 + 교재 + 사전지식, 병렬)
    ↓
태스크 유형 판별 + 해당 스킬 가이드 로드
```

> **예외**: GUIDE.md 자체 수정처럼 콘텐츠 탐색이 불필요한 태스크는 info-search를 생략할 수 있다.

### 태스크별 로드 파일

| 태스크 유형 | 로드할 파일 | 핵심 절차 |
|---|---|---|
| 새 블로그 포스트 작성 | `guides/write-post.md` + 해당 Category GUIDE | info-search → Step 1~6 체크리스트 |
| 기존 포스트 보강/수정 | `guides/write-post.md` + 해당 Category GUIDE | info-search → 대상 파일 읽기 → 수정 → index.qmd 확인 |
| 주제에 대한 질문 답변 | `guides/answer-question.md` | info-search → 3개 레이어 통합 답변 |
| 시리즈 정리/재구성 | `guides/organize-series.md` + Category GUIDE | info-search → 전체 읽기 → 진단 → 설계 → 파일 처리 |
| TBD.qmd 전환 | `guides/convert-tbd.md` + 대상 Category GUIDE | info-search → 분류 → 재작성 → index 업데이트 → 초기화 |
| GUIDE.md 자체 수정 | AGENT_GUIDE.md (이 파일) | 기존 규칙 보존, 추가/구조화만 (info-search 생략 가능) |

---

## 6. Boundaries

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
