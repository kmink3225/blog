---
name: Strategy_Frameworks_GUIDE
type: category
version: 1.0
description: "LOAD when writing posts about business strategy, mental models, logical reasoning, decision-making, or behavioral economics. Covers multi-disciplinary frameworks from Porter to Kahneman."
scope: docs/blog/posts/Strategy_Frameworks/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Strategy_Frameworks/index.qmd
book_sources:
  - docs/book/strategy_frameworks/
cross_references:
  - docs/blog/posts/Experimentation/GUIDE.md
  - docs/blog/posts/Agent/GUIDE.md
  - docs/blog/posts/Statistics/GUIDE.md
---

# Strategy Frameworks 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Strategy Frameworks 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **이론/프레임워크 중심**: 게임 이론, 의사결정 이론, 추론 방법론 등 사고 체계를 다룬다
- **학술적 엄밀성**: 스탠포드 철학 백과사전 등 권위 있는 출처를 인용한다
- **AI/데이터 과학 연계**: 이론적 프레임워크를 AI 에이전트 설계, 프롬프트 엔지니어링, 데이터 분석에 적용한다
- **소규모 카테고리**: 현재 2개 포스트. 점진적으로 확장 예정이다

---

## 포스트 콘텐츠 구조

### 1. 정의 (Definition)

- 프레임워크/이론의 학술적 정의를 callout 블록으로 제시한다
- 출처를 명시한다

```markdown
::: {.callout-note}
## 정의: 가추적 추론 (Abductive Reasoning)

관찰된 현상을 가장 잘 설명하는 가설을 추론하는 방법이다.
연역(전제 → 결론)이나 귀납(사례 → 일반화)과 달리,
가추는 결과에서 원인을 역으로 추론한다.

> "놀라운 사실 C가 관찰된다. 만약 A가 참이라면 C는 당연하다. 따라서 A가 참이라고 추측할 이유가 있다."
> — C.S. Peirce

출처: Stanford Encyclopedia of Philosophy, "Abduction"
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 이론의 구성 요소, 가정, 한계를 체계적으로 설명한다
- 다른 이론과의 관계(보완, 대립, 확장)를 명시한다
- 수학적 형식화가 가능한 경우 수식을 포함한다 (게임 이론의 내쉬 균형 등)
- 추상적이거나 이해하기 어려운 개념에는 일상적 예시, 역사적 맥락 등 직관적 설명을 적재적소에 포함한다 (필요시 별도 섹션으로 분리 가능)
- 각 개념 또는 원리에 데이터 사이언스 실무에 어떻게 적용될 수 있는지 설명한다

### 3. 왜 필요한가 (Why It Matters)

- 데이터 과학자/AI 엔지니어에게 이 프레임워크가 왜 유용한지 설명한다
- 의사결정, 시스템 설계, 전략 수립에서의 역할을 제시한다

### 4. 응용 분야 (Applications)

```markdown
| 분야 | 프레임워크 활용 | 구체적 예시 |
|---|---|---|
| AI 에이전트 | 게임 이론 | 멀티 에이전트 협력/경쟁 전략 |
| 프롬프트 엔지니어링 | 추론 방법론 | Chain-of-Thought = 연역적 추론 |
| 비즈니스 전략 | 의사결정 이론 | 불확실성 하의 투자 결정 |
| 데이터 분석 | 인과추론 | 가추적 추론으로 가설 생성 |
```

### 5. 예시 (Examples)

- 이론을 적용한 분석 사례를 단계별로 보여준다
- AI/데이터 과학 맥락의 예시를 우선한다

### 6. 코드 예시 (Code Examples — Optional)

- 시뮬레이션, 게임 이론 계산 등 코드로 표현 가능한 경우 포함한다
- 순수 이론 포스트의 경우 생략 가능하다

### 7. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**카테고리 내 연결**

- [추론 방법론](./reasoning.qmd)
- [전략 분석 이론](./analysis_theory.qmd)

**다른 카테고리 연결**

- [프롬프트 엔지니어링](../Agent/02-Prompt/) — 추론 방법론의 AI 적용
- [A/B 테스트](../Experimentation/01-ab-test-mechanism.qmd) — 의사결정 이론의 실험적 적용
- [베이즈 정리](../Statistics/06-probability.qmd) — 가추적 추론의 수학적 기반
```

---

## 자주 발생하는 실수 패턴

<fix-framework-without-application>

```
# WRONG: 프레임워크 정의만 나열
Porter의 Five Forces는 산업의 경쟁 강도를 분석하는 프레임워크이다.
1. 기존 경쟁자 간 경쟁
2. 신규 진입자 위협
3. 대체재 위협
4. 공급자 교섭력
5. 구매자 교섭력

# CORRECT: 정의 → 적용 시나리오 → 한계점 → 다른 프레임워크와 비교
Porter의 Five Forces는 산업의 경쟁 강도를 분석하는 프레임워크이다 (Porter, 1980, Ch.1).

**적용 시나리오: AI SaaS 시장 분석**
| Force | 분석 | 강도 |
|---|---|---|
| 기존 경쟁자 간 경쟁 | OpenAI, Google, Anthropic 등 빅테크 경쟁 | 높음 |
| 신규 진입자 위협 | 오픈소스 LLM으로 진입 장벽 하락 | 높음 |
| 대체재 위협 | 내부 개발 vs SaaS 구독 | 중간 |

**한계점**: 정적 분석 → 빠르게 변화하는 AI 시장에서는 동태적 경쟁 분석(D'Aveni, Hypercompetition)으로 보완해야 한다.

**비교**: Porter(산업 구조) vs Rumelt(전략의 핵심) vs Lafley(전략적 선택 계단)
```

</fix-framework-without-application>

---

## 인용 규칙

- 학술 출처를 반드시 명시한다
- 형식: `(저자, 연도)` 또는 `출처: 문서명`
- 주요 참조 소스: Stanford Encyclopedia of Philosophy, 경영학/경제학 교과서

---

## 교재 레퍼런스

이 카테고리의 포스트 작성 시 다음 교재를 **논리적 뼈대**로 활용한다. 교재의 체계를 참고하되, agent의 최신 사전지식으로 outdated된 내용은 수정하고 부족한 부분은 보완한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Hurley — A Concise Introduction to Logic | `docs/book/strategy_frameworks/Hurley-Logic-summary.md` | 연역/귀납/귀추 추론 |
| Lipton — Inference to the Best Explanation (2004) | `docs/book/strategy_frameworks/Lipton-InferenceBestExplanation-summary.md` | 귀추법, 과학적 추론 |
| Porter — Competitive Strategy (1980) | `docs/book/strategy_frameworks/Porter-CompetitiveStrategy-summary.md` | 5 Forces, Value Chain |
| Rumelt — Good Strategy Bad Strategy (2011) | `docs/book/strategy_frameworks/Rumelt-GoodStrategy-summary.md` | 전략의 본질, Kernel |
| Kahneman — Thinking, Fast and Slow (2011) | `docs/book/strategy_frameworks/Kahneman-ThinkingFastSlow-summary.md` | 인지 편향, 시스템 1/2 |
| Lafley & Martin — Playing to Win (2013) | `docs/book/strategy_frameworks/Lafley-PlayingToWin-summary.md` | Strategy Choice Cascade |
| Dixit & Nalebuff — The Art of Strategy (2008) | `docs/book/strategy_frameworks/Dixit-ArtOfStrategy-summary.md` | 게임이론 기반 전략 |
| Parrish — The Great Mental Models (Vol 1-3) | `docs/book/strategy_frameworks/Parrish-GreatMentalModelsV1-summary.md` | 멘탈 모델 |

**활용 절차**: Summary 읽기 → 논리 구조 파악 → Full MD에서 수식/정의 확인 → 교재 내용 중 유효한 부분은 유지, outdated된 부분은 agent 지식으로 수정·보완 → 블로그 스타일로 재작성 + `(저자, 연도, Ch.N)` 인용

---

<boundaries>

### 할 수 있는 것

- 교재 기반 프레임워크/이론 설명 (출처 명시)
- 다학제 연결 (전략 ↔ AI ↔ 데이터 과학 ↔ 심리학)
- 프레임워크의 적용 시나리오와 한계점 분석
- 수학적 형식화 (게임 이론, 의사결정 이론)
- AI/데이터 과학 맥락의 응용 예시

### 할 수 없는 것

- 프레임워크를 교과서 정의만 나열하고 적용 없이 끝내기
- 비판적 분석 없이 단순 소개
- 출처 없는 이론적 주장
- 특정 기업/조직에 대한 전략 자문 형태의 서술

</boundaries>
