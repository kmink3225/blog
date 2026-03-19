# AGENT_GUIDE.md — Blog Repository Instructions

> **참조 문서**: 교재 기반 블로그 작성 시 [docs/book/BOOK_SOURCE_GUIDE.md](docs/book/BOOK_SOURCE_GUIDE.md) 를 반드시 참조한다.
>
> **카테고리별 가이드**: 아래 카테고리의 포스트를 작성할 때는 해당 GUIDE.md를 함께 참조한다.
>
> | 카테고리 | 가이드 경로 |
> |---|---|
> | Statistics | [docs/blog/posts/Statistics/GUIDE.md](docs/blog/posts/Statistics/GUIDE.md) |
> | Math | [docs/blog/posts/Math/GUIDE.md](docs/blog/posts/Math/GUIDE.md) |
> | Experimentation | [docs/blog/posts/Experimentation/GUIDE.md](docs/blog/posts/Experimentation/GUIDE.md) |
> | Agent | [docs/blog/posts/Agent/GUIDE.md](docs/blog/posts/Agent/GUIDE.md) |
> | Deep Learning | [docs/blog/posts/Deep_Learning/GUIDE.md](docs/blog/posts/Deep_Learning/GUIDE.md) |
> | Machine Learning | [docs/blog/posts/Machine_Learning/GUIDE.md](docs/blog/posts/Machine_Learning/GUIDE.md) |
> | Data Science | [docs/blog/posts/Data_Science/GUIDE.md](docs/blog/posts/Data_Science/GUIDE.md) |
> | Engineering | [docs/blog/posts/Engineering/GUIDE.md](docs/blog/posts/Engineering/GUIDE.md) |
> | Governance | [docs/blog/posts/Governance/GUIDE.md](docs/blog/posts/Governance/GUIDE.md) |
> | Code Test | [docs/blog/posts/Code_Test/GUIDE.md](docs/blog/posts/Code_Test/GUIDE.md) |
> | Strategy Frameworks | [docs/blog/posts/Strategy_Frameworks/GUIDE.md](docs/blog/posts/Strategy_Frameworks/GUIDE.md) |
> | Surveilance | [docs/blog/posts/Surveilance/GUIDE.md](docs/blog/posts/Surveilance/GUIDE.md) |

## Project Overview

Quarto 기반 기술 블로그. `.qmd` 파일로 콘텐츠 작성, `quarto render`로 정적 HTML 생성, Netlify 배포.

- **Site**: https://kk3225.netlify.app
- **Author**: Kwangmin Kim
- **Language**: 한국어 (한다 체)

## Commands

```bash
quarto preview    # 로컬 미리보기
quarto render     # 빌드
```

## Key Files

- `_quarto.yml` — 프로젝트 설정, navbar, sidebar
- `docs/blog/posts/_metadata.yml` — 포스트 공통 설정 (댓글, TOC, 배너, 날짜형식)
- `styles.css` — 커스텀 CSS
- `theme.scss` / `theme-dark.scss` — 테마 정의
- `blog_requirements.txt` — Python 의존성

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

## 카테고리 구조

`docs/blog/posts/` 아래에 다음 카테고리 폴더가 존재한다. 각 폴더에는 `index.qmd`(목차 파일)가 있다.

| 카테고리 폴더 | 주제 | index.qmd |
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
| `Surveilance/` | 모니터링, FDA 가이드라인 | O |

### 하위 카테고리 (서브폴더 구조)

- **Agent/**: 번호 prefix 폴더 (`00-Intro/`, `01-Basic/`, ..., `21-GraphRAG/`, `22-Personalization/` 등 24개)
- **Engineering/**: `Data_Engineering/`, `Data_Structure/`, `DevOps/`, `Infra/`, `Python/`, `System/`, `web/`
  - `DevOps/` 하위: `Git/`, `Poetry/`, `Docker/`, `Conda/`, `VScode/`
- **Deep_Learning/**: `NLP/`, `Time_Series/`, `cnn/`, `data/`
- **Statistics/**: `FDA/`, `LDA/`, `time_series/`
- **Experimentation/**: `Epidemiology/`, `AB_test/`, `Causal_inference/`, `MAB/`, `Advanced/`, `Platform/`

### 서브 index.qmd 파일

일부 서브폴더에도 자체 `index.qmd`가 있다:
- `Statistics/FDA/index.qmd`
- `Experimentation/Epidemiology/index.qmd`

### 카테고리별 상세 구조

#### Agent (`docs/blog/posts/Agent/`)

서브폴더 24개, 번호 prefix로 정렬:

```
00-Intro/          # RAG 소개, 환경설정
01-Basic/          # OpenAI API, LCEL, Runnable
02-Prompt/         # PromptTemplate, 프롬프트 엔지니어링
03-OutputParser/   # 출력 파서
04-Model/          # Chat Models, 다양한 LLM
05-Memory/         # 대화 메모리
06-DocumentLoader/ # 문서 로더 (PDF, CSV, HWP 등)
07-TextSplitter/   # 텍스트 분할
08-Embeddings/     # 임베딩 모델
09-VectorStore/    # 벡터 저장소 (Chroma, FAISS, Pinecone)
10-Retriever/      # 검색기
11-Reranker/       # 리랭커
12-RAG/            # RAG 구현
13-Cloud-RAG/      # Azure 기반 클라우드 RAG
14-LangChain-Expression-Language/  # LCEL 심화
15-Chains/         # Chain 패턴
16-Agent/          # Agent 구현
17-Evaluations/    # RAG/Agent 평가
18-LangGraph/      # LangGraph (Core, Structures, Use Cases)
19-FineTuning/     # 파인튜닝
20-Streamlit/      # Streamlit 앱
21-GraphRAG/       # GraphRAG (+ neo4j 서브폴더)
22-Personalization/            # 개인화
22-Segmentation-Personalization/ # 세분화 & 개인화
24-Agent-Architecture/         # Agent 아키텍처
```

#### Engineering (`docs/blog/posts/Engineering/`)

```
Data_Engineering/  # Airflow, Spark, Kafka
  airflow/         # 01~18번 시리즈
Data_Structure/    # 배열, 연결리스트, 트리, 그래프
DevOps/            # VM, 개발환경
  Git/             # 00~14번 시리즈
  Poetry/          # 01~17번 시리즈
  Docker/          # Docker 시리즈
  Conda/           # Conda 시리즈
  VScode/          # VS Code 설정
Infra/
  Cloud/Azure/     # Azure DBA, AI Search, Document Intelligence
  Cloud/AWS/       # AWS 기초
  Cloud/Azure_DevOps/  # Azure DevOps
  OS/Linux/        # Linux 명령어
  OS/Shell/        # Shell 개념
  OS/WSL/          # WSL2
  Security/        # SSH
  On_Presmise/     # GPU
Python/            # Python 기본~고급
System/            # 아키텍처 설계, 데이터 모델링
web/               # HTTP, 방문자 추적
```

#### Statistics (`docs/blog/posts/Statistics/`)

```
(루트)             # 기본, 확률론, 검정, 회귀, 종단분석, Mixed Model 시리즈
FDA/               # 함수형 데이터 분석 (자체 index.qmd 보유)
LDA/               # 종단 데이터 분석
time_series/       # 시계열
```

#### Experimentation (`docs/blog/posts/Experimentation/`)

```
Epidemiology/      # 역학 기초 (자체 index.qmd 보유)
AB_test/           # A/B 테스트
  advanced/        # Sequential, Bayesian, A/A Testing
Fundamentals/      # 통계적 기초
Causal_inference/  # 인과추론
  hte/             # 이질적 처치효과
MAB/               # Multi-Armed Bandit
  classical/       # Epsilon-Greedy, UCB, Thompson Sampling
  advanced/        # Contextual, Non-stationary
Advanced/          # 분산감소, 실무 도전, 연구 최전선
Platform/          # 실험 플랫폼 아키텍처
```

---

## .qmd 파일 작성 규칙

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

카테고리별로 두 가지 파일명 패턴이 혼재한다. **같은 폴더 내에서는 기존 패턴을 따른다.**

**패턴 A: 번호 prefix (Agent, Engineering/DevOps 하위 시리즈)**
```
01-TopicName.qmd
02-TopicName-Detail.qmd
01.topic-name.qmd         # 마침표 구분도 허용
11_topic-name-detail.qmd  # 언더스코어도 허용 (기존 패턴)
```

**패턴 B: 날짜 prefix (Statistics, Engineering 일부)**
```
2023-01-17_topic_name.qmd
2026-03-07_glm.qmd
```

**패턴 결정 방법**: 새 포스트를 넣을 폴더의 기존 파일명을 확인하고 동일한 패턴을 사용한다.

### 콘텐츠 스타일

- **한다 체 사용** (설명체): `~한다`, `~이다`, `~된다`
- **경어체 금지**: `~합니다`, `~입니다`, `~하세요` 사용하지 않음
  - O: `Git은 분산형 버전 관리 시스템이다.`
  - X: `Git은 분산형 버전 관리 시스템입니다.`
- **이모지 사용 금지**
- Quarto callout 블록 활용: `{.callout-tip}`, `{.callout-warning}`, `{.callout-important}`, `{.callout-note}`

### 줄 개행 규칙

Quarto(Markdown)에서 단순 줄바꿈은 렌더링 시 무시된다. **줄 끝에 공백 2칸(`  `)을 반드시 추가**하여 `<br>` 개행을 보장한다.

```markdown
첫 번째 줄  ← 줄 끝에 공백 2칸
두 번째 줄  ← 줄 끝에 공백 2칸
세 번째 줄
```

- 본문의 모든 줄(문단 내 줄바꿈이 필요한 곳)에 trailing 공백 2칸을 붙인다
- 빈 줄(`\n\n`)로 구분되는 문단 사이에는 불필요하다
- 코드 블록, YAML 헤더, callout 내부에서는 적용하지 않는다
- bullet list(`- `, `* `) 항목은 자체 블록이므로 trailing 공백이 불필요하다

### 수식 (LaTeX)

Quarto는 LaTeX 수식을 네이티브로 지원한다.

- 인라인 수식: `$수식$` (예: `$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$`)
- **인라인 수식의 `$` 양쪽에 반드시 공백을 둔다.** `$` 바로 옆에 한글/영문 글자가 붙으면 Quarto가 LaTeX로 인식하지 못한다.
  - O: `모수 $\theta$ 를 추정한다` → 렌더링 정상
  - X: `모수$\theta$를 추정한다` → 렌더링 실패
  - 예외: 괄호, 쉼표, 마침표 등 구두점은 공백 없이 붙어도 된다 (예: `($\theta$)`, `$\theta$,`)
- 블록 수식: `$$수식$$`

```markdown
$$
\hat{\beta} = (X^\top X)^{-1} X^\top y
$$
```

- 교재 소스(`docs/book/`)에서 가져온 수식 중 깨진 것이 있을 수 있다. 의미가 불명확한 수식은 교과서 맥락에서 재구성한다.
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

## index.qmd 업데이트 규칙

**새 포스트를 작성한 후 반드시 해당 카테고리의 `index.qmd`에 링크를 추가해야 한다.**

### index.qmd 위치 찾기

```
포스트 위치: docs/blog/posts/{Category}/{SubFolder}/{filename}.qmd
index 위치:  docs/blog/posts/{Category}/index.qmd
```

1. 포스트가 위치한 카테고리 폴더 확인
2. 해당 폴더의 `index.qmd` 파일을 읽음
3. 적절한 섹션에 링크를 추가

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

index.qmd에서 포스트로의 경로는 **index.qmd 기준 상대경로**를 사용한다:

| 포스트 위치 | index.qmd 위치 | 상대경로 |
|---|---|---|
| 같은 폴더 | `Category/index.qmd` | `./파일명.qmd` |
| 서브폴더 | `Category/index.qmd` | `./서브폴더/파일명.qmd` |
| 상위 폴더 참조 | `Category/Sub/index.qmd` | `../파일명.qmd` |
| 다른 카테고리 | `Category/index.qmd` | `../OtherCategory/파일명.qmd` |

### Placeholder 링크 원칙

**파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이는 index.qmd의 `1111-11-11` 날짜 항목과 동일한 원칙이다. 포스트의 "관련 주제" 섹션에서도 선행/후속 지식으로 필요하지만 아직 작성되지 않은 포스트의 경로를 미리 지정해 둔다. 이를 통해:

- 향후 채워야 할 콘텐츠 gap을 체계적으로 파악할 수 있다
- 파일이 생성되면 링크가 자연스럽게 연결된다
- 블로그의 논리적 구조를 사전에 설계할 수 있다

### 크로스 카테고리 링크 원칙

index.qmd는 **물리적으로 해당 폴더에 있는 파일만 링크하는 것이 아니다.** 논리적으로 연관된 콘텐츠라면 다른 카테고리에 위치한 파일도 링크할 수 있다.

예시:
- `Statistics/index.qmd`의 종단 데이터 섹션에서 `Deep_Learning/`에 있는 DL for Longitudinal Data 파일을 참조 링크로 포함
- `Experimentation/index.qmd`에서 `Statistics/`의 가설검정 관련 포스트를 참조

크로스 카테고리 링크 시 상대경로로 `../OtherCategory/파일명.qmd` 형식을 사용한다.

**하나의 .qmd 파일이 여러 index.qmd에 중복으로 링크될 수 있다.** 파일은 물리적으로 한 폴더에만 존재하지만, 논리적으로 관련된 모든 카테고리의 index.qmd에서 참조한다. 예를 들어 `Deep_Learning/25-mixed-model-dl-lstm.qmd`는 Deep_Learning/index.qmd에 링크되면서 동시에 Statistics/index.qmd의 종단 데이터 섹션에서도 크로스 링크될 수 있다.

### Multi-disciplinary 주제 작성 원칙

A/B 테스트, 생존 분석, 종단 데이터 분석 등 **여러 분야가 융합되는 주제**를 작성할 때는 해당 주제와 관련된 **모든 카테고리의 GUIDE.md를 함께 참조**한다. 단일 카테고리의 GUIDE만으로는 필요한 관점이 누락될 수 있다.

| 주제 | 주 카테고리 | 함께 참조할 GUIDE |
|---|---|---|
| A/B 테스트 | Experimentation | Statistics (가설검정, 검정력), Engineering (플랫폼), Data_Science (메트릭) |
| 생존 분석 | Statistics | Experimentation (임상시험 설계), Machine_Learning (RSF), Deep_Learning (DeepSurv) |
| 종단 데이터 | Statistics | Machine_Learning (시간 피처), Deep_Learning (LSTM, TCN), Experimentation (패널 DiD) |
| RAG 시스템 | Agent | Engineering (인프라, 클라우드), Math (임베딩, 벡터 공간) |
| 모델 배포 | Engineering | Machine_Learning (모델 평가), Data_Science (MLOps), Experimentation (A/B 테스트) |
| 데이터 품질 | Governance | Statistics (이상치 탐지), Engineering (파이프라인) |
| 의료 AI 규제 | Surveilance | Statistics (성능 검증), Deep_Learning (모델 아키텍처) |

포스트 작성 시:

1. 주 카테고리의 GUIDE에서 콘텐츠 구조를 따른다
2. 관련 카테고리의 GUIDE에서 해당 분야의 용어, 표기법, 참조 교재를 확인한다
3. "관련 주제" 섹션에서 모든 관련 카테고리의 포스트를 크로스 링크한다

---

## 블로그 포스트 작성 체크리스트

새 블로그 포스트를 작성할 때 다음 순서를 따른다:

### Step 1: 카테고리 확인
- 주제에 맞는 카테고리 폴더를 결정한다
- 해당 폴더의 기존 파일을 확인하여 파일명 패턴을 파악한다

### Step 1.5: 기존 콘텐츠 중복 판단

새 포스트를 작성하기 전에, **해당 주제를 이미 다루는 기존 포스트가 있는지 반드시 확인**한다. 같은 카테고리뿐 아니라 관련 카테고리도 검색한다.

**판단 기준:**

| 상황 | 조치 |
|---|---|
| 동일 주제의 포스트가 이미 존재하고 내용이 충분 | 새 포스트 작성 불필요. 필요 시 기존 포스트에 섹션/내용 보충 |
| 동일 주제의 포스트가 존재하지만 얕거나 불완전 | 기존 포스트를 보강(내용 추가, 구조 개선, 코드/수식 보충). 새 파일을 만들지 않는다 |
| 주제가 유사하지만 관점/깊이가 다르다 | 새 포스트를 작성하되, 기존 포스트와의 차이점을 명시하고 상호 링크한다 |
| 해당 주제의 포스트가 전혀 없다 | 새 포스트를 작성한다 |
| 기존 포스트가 잘못된 내용을 포함 | 기존 포스트를 수정한다. 잘못된 내용 위에 새 파일을 덮어쓰지 않는다 |

**확인 방법:**

1. 해당 카테고리의 `index.qmd`에서 유사 주제를 검색한다
2. 기존 파일의 YAML 헤더(title, description)를 읽어 범위를 파악한다
3. 필요 시 본문을 읽어 깊이와 완성도를 판단한다
4. 사용자에게 "기존 포스트를 보강할지 새로 작성할지" 확인을 구한다

### Step 2: 포스트 작성
- YAML 헤더 필수 필드를 모두 포함한다
- `date`는 `MM/DD/YYYY` 형식을 사용한다
- 한다 체로 작성한다
- 이모지를 사용하지 않는다
- 문단 내 줄바꿈이 필요한 곳에 줄 끝 공백 2칸을 붙인다
- 교재 기반 주제라면 `docs/book/`의 소스 파일을 먼저 읽고 개념을 정리한 뒤 블로그 스타일로 재작성한다

### Step 3: index.qmd 업데이트
- 해당 카테고리의 `index.qmd`를 읽는다
- 기존 링크 패턴(날짜 형식, 번호 형식, 들여쓰기 등)을 확인한다
- 적절한 섹션에 새 포스트 링크를 추가한다
- 섹션이 없으면 기존 구조에 맞게 새 섹션을 추가한다

### Step 4: 검증
- 상대경로가 올바른지 확인한다
- YAML 헤더의 필수 필드가 빠지지 않았는지 확인한다
- 링크 형식이 해당 index.qmd의 기존 패턴과 일치하는지 확인한다

### 수정 작업 원칙

- **실제 파일을 먼저 확인한 후 수정한다.** 규칙(경어체 금지, 이모지 금지 등)을 기계적으로 일괄 적용하지 않는다. 대상 파일을 읽거나 샘플링하여 해당 문제가 실제로 존재하는지 확인한 뒤에만 수정 작업을 수행한다.
- **"혹시 모르니까" 식의 포괄적 수정 지시를 내리지 않는다.** 검증 없이 수정하면 불필요한 변경이 발생하고, 의도하지 않은 내용 훼손으로 이어질 수 있다.
- **Sub-agent에게 작업을 위임할 때도 동일한 원칙을 적용한다.** 수정 대상 파일의 실제 상태를 확인한 후, 실제 존재하는 문제에 대해서만 수정을 지시한다.

---

## 임시 메모 → 블로그 전환 패턴

사용자가 AI agent와의 대화에서 유용한 정보를 임시 파일(`docs/blog/posts/` 루트)에 저장해 둘 수 있다. Agent는 이 임시 파일을 주제별 정식 블로그 포스트로 전환한다.

### 전환 절차

1. **임시 파일 읽기** — 내용을 파악하고 주제별로 분리한다
2. **중복 확인** — 이미 정식 포스트로 작성된 내용이 있는지 기존 블로그 파일과 대조한다
3. **분류** — 미정식화된 내용을 적절한 카테고리 폴더에 매핑한다
4. **재작성 및 보강** — 대화 메모를 독립적인 블로그 포스트로 완성한다
   - 대화 요소 제거 ("당신", "네", 독자에게 던지는 질문, "묻겠다" 등)
   - 한다 체로 통일하고 YAML 헤더 필수 필드를 포함한다
   - **단순 스타일 변환이 아니라 내용을 보강한다:**
     - 메모에 없는 배경 설명, 정의, 동기(왜 중요한가)를 추가한다
     - 핵심 개념에 대한 수식, 코드 예시, 다이어그램을 보충한다
     - 논리적 흐름이 끊기는 곳에 연결 설명을 넣는다
     - 비교 테이블, 장단점 정리 등 구조화된 요약을 추가한다
     - 독자가 메모의 맥락을 모르더라도 포스트만으로 완결되도록 작성한다
   - 각 포스트의 구조: 도입(왜 필요한가) → 핵심 개념 → 비교/분석 → 실무 적용 → 정리
5. **index.qmd 업데이트** — 새 포스트 링크를 해당 카테고리 index에 추가한다
6. **TBD.qmd 초기화** — 정식 포스트로 전환 완료 후 TBD.qmd의 내용을 비우고 빈 템플릿 상태로 되돌린다 (파일 자체는 삭제하지 않는다)

### 임시 파일 규칙

- **경로**: `docs/blog/posts/TBD.qmd` (고정)
- 하나의 파일에 여러 주제를 누적하며, 주제 간 구분은 `---` 또는 `## 제목`으로 한다
- YAML 헤더에 `draft: true`를 포함하여 빌드에서 제외한다
- 전환 작업 후에도 파일은 삭제하지 않고 빈 상태로 유지한다 (다음 메모를 위해)

---

## 시리즈 블로그 정리 패턴

블로그 시리즈를 체계적으로 정리할 때 따르는 패턴:

1. **기존 파일 전체 읽기** — 현재 상태 파악
2. **문제 진단** — 중복, 잘못된 내용, 누락된 주제, 비체계적 구성 식별
3. **구조 설계** — 기초 → 핵심 → 심화 → 실전 순서로 배치
4. **파일 처리**:
   - 잘 된 파일: 유지
   - 내용이 잘못된 파일: 같은 번호로 새 파일 작성, 기존 파일 삭제
   - 누락된 주제: 새 파일 추가
5. **요약 테이블 제공** — 작업 결과를 사용자에게 보고

### 시리즈 구성 원칙

```
기초: 개요, 설치, 기본 개념
핵심: 주요 기능, 일상적 사용법
심화: 고급 기능, 비교 분석, CI/CD 통합
실전: 트러블슈팅, 실무 사례
```

---

## 완료된 정리 작업

### Git 시리즈 (`Engineering/DevOps/Git/`)
- 00: 비개발자용 Git (별도 대상)
- 01: 설치 및 설정
- 02: 기본 워크플로 (status, add, commit, push, pull)
- 03: 브랜치
- 04: 브랜치 전략 (Git Flow)
- 05: Pull Request
- 06: Git 그래프 시각화
- 07: 원격 저장소 관리
- 08: Merge vs Rebase
- 09: 되돌리기 (restore, reset, revert, reflog)
- 10: Stash
- 11: 태그와 SemVer
- 12: .gitignore
- 13: Cherry-pick
- 14: 고급 (bisect, submodule, worktree, hooks, alias)

### Poetry 시리즈 (`Engineering/DevOps/Poetry/`)
- 01: Poetry 소개
- 02: 설치
- 03: 의존성 관리 (add, remove, update, lock)
- 04: 가상환경 (install, run, shell, env)
- 05: pyproject.toml 상세
- 06: 빌드와 배포 (build, publish)
- 07: 설정과 고급 명령어 (config, source, cache, plugin)
- 08: 도구 비교 (pip, Conda, Pipenv, PDM)
- 09: CI/CD와 Docker 통합
- 10: 트러블슈팅
- 11-17: 외부 Git 패키지 통합 실전 사례

---

## Book Source (교재 레퍼런스)

`docs/book/` 폴더에 교과서 md 파일이 있다. 블로그 포스트 작성 시 교과서 기반 근거로 참조한다.
- 렌더링 대상 아님 (`_quarto.yml`에서 제외)
- 상세 가이드: `docs/book/BOOK_SOURCE_GUIDE.md`
- 소스 내용을 그대로 복붙하지 않고 블로그 스타일(한다 체)로 재작성한다
- 인용 시 `(저자, 연도, Ch.N)` 형식 사용

### 그룹 구조
- `statistics/` — Casella & Berger (수리통계)
- `linear_algebra/` — Strang, Magnus, Matrix Cookbook (선형대수, 행렬 미분)
- `glm/` — McCullagh & Nelder, Faraway (GLM, 회귀)
- `mixed_model/` — Hedeker & Gibbons (종단 데이터, 반복측정)
- `survival/` — Kleinbaum, Klein, Hosmer, Collett (생존 분석)
- `epidemiology/` — Hernan, Woodward, Schulz, Maxwell, Buisson (인과추론, 역학, 실험설계, AB test)
- `bayesian/` — Gelman, Downey (베이지안)
- `fda/` — Ramsay×2, Kokoszka (함수형 데이터 분석)
