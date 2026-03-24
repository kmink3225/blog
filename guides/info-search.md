---
name: info-search
type: skill
description: >
  통합 정보 탐색 (Universal Information Gathering).
  블로그 포스트 작성, 질문 응답, TBD 전환, 시리즈 정리 등
  모든 콘텐츠 태스크의 공통 선행 단계.
prerequisite: AGENT_GUIDE.md (공통 코어)
---

# 통합 정보 탐색 (Universal Information Gathering)

**모든 태스크(Q&A, 포스트 작성, 시리즈 정리 등)의 공통 선행 단계.** 태스크 유형을 판별하기 전에, 또는 판별과 동시에 아래 3개 레이어를 **병렬로** 탐색한다. 어느 한 레이어에서 결과가 나왔다고 나머지를 건너뛰지 않는다.

## 병렬 탐색 프로토콜

```
사용자 요청 수신
    ↓
주제 키워드 추출 (복수 가능)
    ↓
┌─────────────────────────────────────────────────────────┐
│  동시 탐색 — 3개 레이어를 모두 실행한다                    │
│                                                         │
│  Layer 1: 블로그 포스트                                   │
│    - 주제 관련 전 카테고리의 index.qmd 스캔               │
│    - Grep으로 docs/blog/posts/ 전체 키워드 검색           │
│    - 크로스 카테고리 후보 파일 경량 스캔 (YAML + 헤더)     │
│                                                         │
│  Layer 2: 교재 소스 (docs/book/)                          │
│    - 카테고리에 국한하지 않고 전체 Summary MD 스캔         │
│    - 키워드 매칭으로 관련 챕터 특정                        │
│    - 필요 시 Full MD 선택적/확장 읽기                     │
│                                                         │
│  Layer 3: agent 사전지식                                  │
│    - 항상 준비 상태 (별도 탐색 불필요)                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
    ↓
탐색 결과 통합 → 태스크 유형에 맞게 출력
```

## 통합 원칙

| 원칙 | 설명 |
|------|------|
| **전수 탐색** | 3개 레이어를 모두 탐색한다. Layer 1에서 답이 나와도 Layer 2·3을 생략하지 않는다 |
| **충돌 시 신뢰도** | 블로그 포스트 > 교재 소스 > agent 사전지식 순으로 신뢰한다. 이 순서는 "탐색 중단 순서"가 아니라 **내용 충돌 시 우선 채택 순서**다 |
| **출처 명시** | 최종 답변/포스트에서 어느 레이어의 정보를 사용했는지 구분 가능해야 한다 (블로그 → 파일 경로, 교재 → 인용, 사전지식 → "블로그에 아직 없다" 명시) |
| **교차 조합** | 하나의 주제에 여러 교재·여러 카테고리의 정보가 관련되면 **모두 조합**하여 최적의 답변을 구성한다. 예: "발화데이터 분석" → `linguistics/`(대화분석) + `behavioral_analysis/`(행동분석) + `psychology/`(인지심리) + `Agent/`(블로그) |

## Book Source 상세

`docs/book/` 폴더에 교과서 md 파일이 있다.

### 왜 교재를 넣었는가

agent의 사전지식은 너무 방대하여, 제약 없이 쓰면 불필요한 지식이 섞여 포커스가 흐려진다. **교재는 agent 지식의 범위를 좁히고 구체성을 높이는 경계(boundary) 역할**을 한다. 교재가 다루는 영역 안에서 깊고 정확하게 서술하되, 교재가 커버하지 못하는 최신/부족한 부분만 agent 사전지식으로 채운다.

### 활용 철학

1. **범위 제한**: 교재가 정의하는 범위 안에서 논리를 전개한다. 교재에 없는 방향으로 지식을 확장할 때는 명확한 이유가 있어야 한다.
2. **교차 검색·조합**: 하나의 주제를 다룰 때 **카테고리에 국한하지 않고 전체 book 소스를 교차 검색**한다. 예를 들어 "인과추론 기반 A/B 테스트"라면 `epidemiology/`(Hernan), `behavioral_analysis/`(Kohavi), `statistics/`(Casella), `strategy_frameworks/`(Kahneman)를 함께 참조할 수 있다.
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
| `timeseries/` | Hyndman & Athanasopoulos(FPP3) | 시계열 예측, ARIMA, ETS, 동적 회귀 |

### 2-Layer 교재 참조 체계

각 교재 폴더에는 두 종류의 파일이 있다:

| 파일 유형 | 명명 규칙 | 역할 |
|---|---|---|
| **Summary MD** | `*-summary.md` | 목차 + 챕터별 요약 + 키워드 + **상세 요약(10~15문장)** + Marker 세부 목차. **항상 먼저 읽는다** (지도 역할) |
| **Full MD** | `*_full.md` | PDF→MD 변환 원본. 챕터 단위로 상세 내용 참조 시 사용 |

### Summary MD 구조

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

#### 새 교재 추가 시

새 PDF 변환 파일(`_full.md`)이 `docs/book/`에 추가되면:
1. 해당 책의 `*-summary.md`를 생성한다 (YAML frontmatter + 챕터별 핵심/키워드/상세)
2. `sources:` 필드에 변환 파일 정보를 추가한다
3. Marker 변환본이 있으면 `## Marker 세부 목차` 섹션을 추가한다
4. 이 파일(AGENT_GUIDE.md)의 그룹 구조 테이블을 업데이트한다
5. 해당 카테고리의 `GUIDE.md`에 교재 레퍼런스를 추가한다

#### 기존 교재의 변환 품질 개선 시

더 좋은 변환 도구로 재변환한 경우(예: Azure → Marker):
1. 새 `_full.md` 파일을 추가하고, summary의 `sources:`에 추가한다
2. 상세 요약의 라인 참조(`L:숫자`)를 새 파일 기준으로 업데이트한다
3. Marker 세부 목차를 추가/갱신한다

#### 정기 점검

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
