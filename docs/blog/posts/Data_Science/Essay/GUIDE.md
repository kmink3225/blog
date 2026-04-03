---
name: Essay_GUIDE
type: category
version: 2.0
description: >
  LOAD when writing or converting Essay posts under Data_Science/Essay/.
  Essay는 면접·임원 미팅·이직 대비용 ideation 문서다.
  Input은 JD/회사 홈페이지 기술 내용이거나, 직접 시리즈로 빌드업하는 ideation이다.
  "내가 당신 조직의 문제를 이렇게 해결할 수 있다"는 구체적 제안서 수준까지 발전시킨다.
scope: docs/blog/posts/Data_Science/Essay/
parent: AGENT_GUIDE.md
---

# Essay 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE_CORE.md`의 공통 규칙을 보충하는 **Essay 전용 가이드**다.
> Essay는 **기술 블로그 포스트가 아니다.** 면접·임원 PT·이직 ideation 문서다.

---

## Essay의 목적과 독자

### 핵심 목적

> "나는 당신 조직이 갖고 있는 이 문제를 이렇게 해결할 수 있다."

Essay는 이 한 문장을 **데이터 과학 언어로 구체적으로 증명**하는 문서다.

### 상정 독자

| 독자 | 맥락 | Essay가 전달해야 할 것 |
|---|---|---|
| 면접관 (DS/ML 리드) | 기술 역량 검증 | "이 사람은 우리 문제를 이미 분석했고 방법론을 갖고 있다" |
| 임원 (CPO/CDO/CTO) | 비즈니스 임팩트 검증 | "이 사람이 합류하면 우리 X 문제가 풀린다" |
| 현 조직 내부 발표 | 신규 프로젝트 제안 | "이 방법으로 지금 우리 팀이 이 문제를 해결할 수 있다" |

---

## Essay 입력 유형 (Input Type)

Essay를 작성하는 출발점은 두 가지다.

### Type A: JD / 회사 홈페이지 기반

채용 공고(JD) 또는 회사 기술 블로그·홈페이지 내용을 분석해 Essay를 작성한다.

**작성 절차:**

```
1. JD 또는 홈페이지 기술 내용을 붙여넣는다
2. JD에서 "핵심 문제" 추출 (Requirements, Responsibilities 섹션 집중)
3. 그 문제를 5단 전개 구조로 전환
4. 보유 역량(아래 역량 목록) 중 가장 직접적으로 연결되는 것을 선택
5. 연결 고리 한 문장 작성 → 방법론 상세화 → KPI 추정 → 로드맵
```

**JD 분석 체크리스트:**

```
- [ ] JD에서 반복 등장하는 기술 키워드 3개 이상 추출됐는가?
- [ ] "팀의 미션"과 "내가 해결할 문제"가 분리됐는가?
- [ ] 회사 규모·산업·데이터 인프라 수준이 파악됐는가?
      (스타트업 vs 대기업, on-prem vs cloud, 데이터 성숙도)
- [ ] 경쟁사 대비 이 회사가 갖는 특수한 고민이 명시됐는가?
```

### Type B: 자체 시리즈 빌드업 (PCR 방식)

특정 도메인 문제를 직접 설정하고, 포스트 시리즈 형태로 ideation을 누적한다.

```
예: PCR 시리즈
  pcr-sigmoid-curve-fitting.qmd    → 모델 기초
  pcr-grayzone-uncertainty.qmd     → 불확실성 문제 정의
  pcr-hierarchical-bayesian.qmd    → 해결 방법론
  pcr-joint-bayesian-estimation.qmd → 통합 추정
  pcr-portfolio-career-strategy.qmd → 역량 전이 + 비즈니스 적용 (Essay)
```

**시리즈 마지막 Essay는 반드시 포함해야 할 것:**
- 시리즈 전체를 한 문단으로 요약
- 이 역량이 타 도메인에서 어떤 JD에 맞는지 명시
- KPI 임팩트 추정

---

## Essay 구조 — 5단 전개

모든 Essay는 아래 5단 구조를 따른다.

### 1단: 조직의 고민 (Problem Framing)

면접관·임원이 **매일 고민하는 문제**를 구체적으로 서술한다.
- 추상적 고민("수요 예측이 어렵다") → 수치화된 고민으로 전환
- 예: "전국 1300개 매장 × 3만 SKU에서 재고 과잉·품절로 연간 매출 손실 추정 X억원"

```
작성 체크:
- [ ] 조직명 또는 산업군이 명시됐는가?
- [ ] 고민이 KPI/비용/리스크 중 하나로 수치화됐는가?
- [ ] 현재 조직이 이 문제를 어떻게 다루고 있는지(as-is) 서술됐는가?
```

### 2단: 왜 기존 방법이 부족한가 (As-Is 한계)

현재 일반적으로 쓰는 방법의 구조적 한계를 **기술적으로** 설명한다.
- 규칙 기반, 단순 ML, 엑셀 분석 등의 한계
- 한계는 수학/통계적으로 설명할 수 있어야 한다

```
작성 체크:
- [ ] 기존 방법이 구체적으로 명시됐는가?
- [ ] 한계가 "왜 수학적으로 부족한지" 설명됐는가?
- [ ] 한계가 비즈니스 손실로 연결됐는가?
```

### 3단: 내 방법론 (To-Be 설계)

보유한 기술 역량을 이 문제에 **직접 적용**하는 방식을 제안한다.
- 수식, 코드 스니펫, 파이프라인 다이어그램 중 하나 이상 포함
- "PCR에서 X를 했는데, 여기서는 Y에 동일한 구조를 적용한다"는 연결 고리 명시

```
작성 체크:
- [ ] 제안 방법론의 핵심 수식 또는 알고리즘이 있는가?
- [ ] 기존 역량과의 연결 고리가 1문장 이상 명시됐는가?
- [ ] 구현 난이도·기간이 현실적으로 서술됐는가?
```

### 4단: 기대 효과 (Impact)

방법론 적용 시 **KPI 개선 수치**를 추정한다.
- 정확한 수치가 없으면 범위 추정(예: "RMSE 15~30% 개선 예상")
- 비즈니스 언어(매출, 비용, 리드타임)로 번역 필수

```
작성 체크:
- [ ] KPI 개선 수치가 있는가?
- [ ] 수치가 비즈니스 단위(원, %, cycle)로 표현됐는가?
- [ ] 불확실성(best/worst case)이 언급됐는가?
```

### 5단: 실행 로드맵 (Roadmap)

"언제, 무엇을, 어떻게" 3개월/6개월/1년 단위로 기술한다.
- Phase 1 (0~3개월): 데이터 확인 + PoC
- Phase 2 (3~6개월): 파이프라인 구축 + A/B 테스트
- Phase 3 (6~12개월): 프로덕션 배포 + 모니터링

```
작성 체크:
- [ ] Phase가 3개 이상 있는가?
- [ ] 각 Phase에 산출물(deliverable)이 명시됐는가?
- [ ] 필요한 데이터/인프라 전제조건이 명시됐는가?
```

---

## 도메인별 고민 목록 (면접 준비용)

### 물류·리테일 (올리브영, 쿠팡, 무신사, SSG 등)

| 고민 | 현재 방법의 한계 | 적용 가능 역량 |
|---|---|---|
| SKU × 매장 수요 예측 정확도 | 독립 시계열, cold-start 취약 | 계층적 Bayesian (PCR 배치 공유 구조) |
| 재고 발주 타이밍 (회색지대) | 고정 임계값, 불확실성 무시 | Bayesian posterior 기반 발주 확률 (PCR 그레이존 구조) |
| 프로모션 ROI 측정 | before/after 비교, 교란 변수 무시 | DID, synthetic control |
| 프로모션 반응 모델 | 선형 가정, SKU별 반응 차이 무시 | 4PL sigmoid — 임계 할인율 자동 추정 (PCR 피팅 직접 전이) |
| 배송 리드타임 이상 탐지 | 수동 임계값 알람 | ARIMA 잔차 + Ljung-Box (PCR RFU 탐지 구조) |
| 고객 이탈 예측 불확실성 | 점 추정만 보고, CI 없음 | Bayesian LTV/이탈 모델, 불확실성 전파 |
| 상품 카탈로그 자동 분류 | 수동 태깅, 규칙 기반 | RAG + LLM 분류 파이프라인 (Agent Platform 경험) |
| 상담 CS 자동화 한계 | 단순 FAQ 봇, context 유지 안 됨 | Agentic RAG — multi-turn + memory (LangGraph 경험) |
| 상품 검색 품질 개선 | 키워드 매칭, 의미 검색 없음 | Modular RAG — embedding + reranker 파이프라인 |

### PCR·바이오테크·의료기기 (씨젠, 바이오메리유, 로슈, 애보트 등)

| 고민 | 현재 방법의 한계 | 적용 가능 역량 |
|---|---|---|
| 그레이존 Ct 판정 불일치 | 단일 임계값, 재검 기준 불명확 | Bayesian posterior, 30/40/30 프로토콜 |
| 배치 간 증폭 효율 편차 | 배치별 독립 보정, 정보 손실 | 계층적 Bayesian, partial pooling |
| 피팅 품질 자동 평가 | R²만 확인, 잔차 구조 미검토 | ACF/Ljung-Box, AIC/BIC 자동화 |
| FDA 규제 문서 자동화 | 수동 작성, 버전 관리 어려움 | RAG 기반 규제 문서 Q&A + 초안 생성 (Agent Platform) |
| 임상 데이터 이상치 탐지 | 도메인 전문가 수동 검토 | Mechanistic 모델 잔차 기반 이상 탐지 |
| 다중 검사 패널 해석 | 각 검사 독립 판정, 상관 무시 | Joint Bayesian Estimation (PCR joint 모델 직접 전이) |

### e-커머스·플랫폼 (네이버, 카카오, 쿠팡, 토스 등)

| 고민 | 현재 방법의 한계 | 적용 가능 역량 |
|---|---|---|
| A/B 테스트 해석 오류 | p-value 오용, 다중 비교 미보정 | Bayesian A/B, ROPE 기반 의사결정 |
| 추천 cold-start | 인기도 fallback, 개인화 없음 | 계층적 Bayesian 협업 필터링 |
| LTV 추정 불확실성 | 점 추정, CI 없음 | Bayesian LTV, 불확실성 전파 |
| 검색·추천 품질 측정 자동화 | 수동 평가, 느린 피드백 루프 | LLM-as-Judge + RAG 자동 평가 파이프라인 |
| 사내 지식 검색 (Knowledge Base) | 키워드 검색, 문서 파편화 | Advanced RAG (hybrid search + reranking) |
| LLM 기반 서비스 hallucination | 단순 프롬프트 엔지니어링 한계 | Modular RAG + retrieval grounding + fact-check layer |

### 금융·핀테크 (토스, 카카오페이, 신한, KB 등)

| 고민 | 현재 방법의 한계 | 적용 가능 역량 |
|---|---|---|
| 이상 거래 탐지 (FDS) | 규칙 기반, 신규 패턴 대응 늦음 | 시계열 이상 탐지 (ARIMA 잔차 구조) |
| 신용 리스크 모델 불확실성 | 점 추정, 규제 해석 어려움 | Bayesian 신용 모델, 불확실성 정량화 |
| 규제 문서·약관 Q&A | 수동 법무 검토, 느린 응답 | RAG 기반 규제 문서 Agent (LangGraph 경험) |
| 투자 리포트 자동 생성 | 템플릿 기반, 수동 데이터 입력 | Agentic RAG — 데이터 조회 + 문서 생성 orchestration |

### AI 플랫폼·LLM 서비스 (네이버 클로바, 카카오 AI, 업스테이지 등)

| 고민 | 현재 방법의 한계 | 적용 가능 역량 |
|---|---|---|
| RAG 검색 품질 개선 | 단순 벡터 유사도, context window 낭비 | Modular RAG — query routing + reranking + compression |
| 멀티턴 대화 context 관리 | 매 턴 독립 처리, 메모리 없음 | LangGraph stateful agent + memory layer 설계 |
| Agent 오케스트레이션 복잡도 | 단일 LLM 호출, tool 조합 어려움 | LangGraph orchestration layer — 조건부 라우팅 + 병렬 실행 |
| LLM 응답 신뢰도 측정 | 주관적 평가, 자동화 없음 | LLM-as-Judge + Bayesian 신뢰도 스코어링 |
| 도메인 특화 LLM 성능 한계 | General LLM, 도메인 지식 부족 | Advanced RAG + few-shot + domain-specific retrieval |
| AI 서비스 latency 최적화 | 순차 호출, 병목 미파악 | Modular RAG 비동기 파이프라인 + streaming |

---

## 보유 역량 목록 (Essay 연결 고리 작성용)

### 역량 A: AI Agent Platform

**핵심 경험:** LangChain/LangGraph를 통한 RAG 시스템 구현 및 orchestration layer 설계

| 세부 역량 | 설명 |
|---|---|
| Advanced RAG | Query transformation, hybrid search (dense+sparse), reranking, contextual compression |
| Modular RAG | Retrieve → Rerank → Generate 각 모듈 독립 교체 가능한 파이프라인 설계 |
| Agentic RAG | Tool-calling, 자기 수정(self-reflection), multi-step reasoning LangGraph 구현 |
| Orchestration Layer | 조건부 라우팅, 병렬 실행, state machine 설계 (LangGraph StateGraph) |
| Memory & State | Short-term (대화 이력) + Long-term (Vector DB 기반) 메모리 아키텍처 |

**Essay 연결 고리 템플릿:**

| 새 문제 | 연결 고리 한 문장 |
|---|---|
| 사내 지식 검색 | "Advanced RAG의 hybrid search + reranking 파이프라인을 사내 문서 검색에 그대로 적용한다" |
| CS 자동화 | "LangGraph stateful agent로 멀티턴 고객 상담 context를 유지하는 구조를 설계한 경험이 있다" |
| 규제 문서 Q&A | "Modular RAG의 retrieval grounding으로 hallucination을 억제하는 구조를 구현했다" |
| 복합 데이터 파이프라인 | "LangGraph orchestration layer로 병렬 도구 호출과 조건부 분기를 설계한 경험이 있다" |

---

### 역량 B: 고급 통계 / Mechanistic 모델링 (PCR 시리즈)

**핵심 경험:** 4PL sigmoid 피팅 + 계층적 Bayesian + 시계열 분석으로 PCR 진단 파이프라인 설계

| 세부 역량 | 설명 |
|---|---|
| 4PL Sigmoid 피팅 | 비선형 회귀, 수렴 안정성 (bounds, Ridge 정규화), AIC/BIC 모델 선택 |
| 계층적 Bayesian | PyMC MCMC, partial pooling, shrinkage, CRB/Fisher 정보 분석 |
| Bayesian 불확실성 정량화 | Posterior CI, 그레이존 처리, 재검 프로토콜 설계 |
| 시계열 이상 탐지 | ARIMA, wavelet 변환, Ljung-Box 잔차 검정, 전환점 탐지 |
| Joint Bayesian Estimation | 다중 파라미터 동시 추정, prior 설계, MCMC 수렴 진단 |
| FDA 규제 맥락 ML 설계 | Closed system, OOD 탐지, 규제 적합 모델 구조 |

**Essay 연결 고리 템플릿:**

| 새 문제 | 연결 고리 한 문장 |
|---|---|
| 수요 예측 | "PCR 배치 간 Hill slope 공유 구조가 매장 간 계절성 partial pooling과 수학적으로 동일하다" |
| 재고 회색지대 | "Ct 35~40 그레이존 처리의 Bayesian posterior 구조를 재주문점 불확실성 처리에 그대로 전용한다" |
| 프로모션 반응 | "PCR 증폭 곡선의 S자(4PL) 구조가 할인율-전환율 반응 모델과 수학적으로 동일하다" |
| 이상 탐지 | "RFU 시계열의 ARIMA 잔차 + Ljung-Box 파이프라인을 리드타임/거래 시계열에 그대로 적용한다" |
| A/B 테스트 | "PCR 그레이존의 Bayesian posterior 의사결정 구조가 A/B 테스트의 ROPE 기반 판정과 동일하다" |

---

### 역량 C: 딥러닝 / 머신러닝

| 세부 역량 | 설명 |
|---|---|
| 분류/회귀 파이프라인 | 피처 엔지니어링, 앙상블, 하이퍼파라미터 최적화 |
| 시계열 DL | LSTM, Transformer 기반 예측 |
| 도메인 특화 DL | PCR 신호 처리 딥러닝 (FDA 규제 closed system 내 설계) |
| 모델 해석 | SHAP, LIME, Bayesian 불확실성 연동 |

---

## 작성 스타일 규칙

- **한다 체** (`~한다/~이다/~된다`) 유지
- **이모지 금지** (`.qmd` 내)
- **수동 번호 금지** (`number-sections: true` 자동 적용)
- 수식 있으면 직관 설명 必 (수식만 넣으면 안 됨)
- **비즈니스 임팩트 수치**가 없는 Essay는 미완성으로 간주

---

## Self-Check (작성 완료 전 확인)

```
- [ ] Input 유형이 명시됐는가? (Type A: JD 기반 / Type B: 자체 시리즈)
- [ ] 조직의 고민이 수치화됐는가?
- [ ] As-Is 한계가 기술적으로 설명됐는가?
- [ ] 내 방법론의 핵심 수식/코드/파이프라인이 있는가?
- [ ] 역량 A(Agent)/B(통계·모델링)/C(DL/ML) 중 연결 고리가 명시됐는가?
- [ ] KPI 개선 수치(범위라도)가 있는가?
- [ ] 3단계 이상의 실행 로드맵이 있는가?
- [ ] 한다 체, 이모지 없음, 수동 번호 없음
```


# Essay 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE_CORE.md`의 공통 규칙을 보충하는 **Essay 전용 가이드**다.
> Essay는 **기술 블로그 포스트가 아니다.** 면접·임원 PT·이직 ideation 문서다.

---

## Essay의 목적과 독자

### 핵심 목적

> "나는 당신 조직이 갖고 있는 이 문제를 이렇게 해결할 수 있다."

Essay는 이 한 문장을 **데이터 과학 언어로 구체적으로 증명**하는 문서다.

### 상정 독자

| 독자 | 맥락 | Essay가 전달해야 할 것 |
|---|---|---|
| 면접관 (DS/ML 리드) | 기술 역량 검증 | "이 사람은 우리 문제를 이미 분석했고 방법론을 갖고 있다" |
| 임원 (CPO/CDO/CTO) | 비즈니스 임팩트 검증 | "이 사람이 합류하면 우리 X 문제가 풀린다" |
| 현 조직 내부 발표 | 신규 프로젝트 제안 | "이 방법으로 지금 우리 팀이 이 문제를 해결할 수 있다" |

---

## Essay 구조 — 5단 전개

모든 Essay는 아래 5단 구조를 따른다.

### 1단: 조직의 고민 (Problem Framing)

면접관·임원이 **매일 고민하는 문제**를 구체적으로 서술한다.
- 추상적 고민("수요 예측이 어렵다") → 수치화된 고민으로 전환
- 예: "전국 1300개 매장 × 3만 SKU에서 재고 과잉·품절로 연간 매출 손실 추정 X억원"

```
작성 체크:
- [ ] 조직명 또는 산업군이 명시됐는가?
- [ ] 고민이 KPI/비용/리스크 중 하나로 수치화됐는가?
- [ ] 현재 조직이 이 문제를 어떻게 다루고 있는지(as-is) 서술됐는가?
```

### 2단: 왜 기존 방법이 부족한가 (As-Is 한계)

현재 일반적으로 쓰는 방법의 구조적 한계를 **기술적으로** 설명한다.
- 규칙 기반, 단순 ML, 엑셀 분석 등의 한계
- 한계는 수학/통계적으로 설명할 수 있어야 한다

```
작성 체크:
- [ ] 기존 방법이 구체적으로 명시됐는가?
- [ ] 한계가 "왜 수학적으로 부족한지" 설명됐는가?
- [ ] 한계가 비즈니스 손실로 연결됐는가?
```

### 3단: 내 방법론 (To-Be 설계)

보유한 기술 역량을 이 문제에 **직접 적용**하는 방식을 제안한다.
- 수식, 코드 스니펫, 파이프라인 다이어그램 중 하나 이상 포함
- "PCR에서 X를 했는데, 여기서는 Y에 동일한 구조를 적용한다"는 연결 고리 명시

```
작성 체크:
- [ ] 제안 방법론의 핵심 수식 또는 알고리즘이 있는가?
- [ ] 기존 역량(PCR 등)과의 연결 고리가 1문장 이상 명시됐는가?
- [ ] 구현 난이도·기간이 현실적으로 서술됐는가?
```

### 4단: 기대 효과 (Impact)

방법론 적용 시 **KPI 개선 수치**를 추정한다.
- 정확한 수치가 없으면 범위 추정(예: "RMSE 15~30% 개선 예상")
- 비즈니스 언어(매출, 비용, 리드타임)로 번역 필수

```
작성 체크:
- [ ] KPI 개선 수치가 있는가?
- [ ] 수치가 비즈니스 단위(원, %, cycle)로 표현됐는가?
- [ ] 불확실성(best/worst case)이 언급됐는가?
```

### 5단: 실행 로드맵 (Roadmap)

"언제, 무엇을, 어떻게" 3개월/6개월/1년 단위로 기술한다.
- Phase 1 (0~3개월): 데이터 확인 + PoC
- Phase 2 (3~6개월): 파이프라인 구축 + A/B 테스트
- Phase 3 (6~12개월): 프로덕션 배포 + 모니터링

```
작성 체크:
- [ ] Phase가 3개 이상 있는가?
- [ ] 각 Phase에 산출물(deliverable)이 명시됐는가?
- [ ] 필요한 데이터/인프라 전제조건이 명시됐는가?
```

---

## 도메인별 고민 목록 (면접 준비용)

### 물류·리테일 (올리브영, 쿠팡, 무신사 등)

| 고민 | 현재 방법의 한계 | 적용 가능 방법론 |
|---|---|---|
| SKU × 매장 수요 예측 정확도 | 독립 시계열 모델, cold-start 취약 | 계층적 Bayesian, shrinkage |
| 재고 발주 타이밍 (그레이존) | 고정 임계값, 불확실성 무시 | Bayesian posterior 기반 발주 확률 |
| 프로모션 ROI 측정 | 단순 비교(before/after), 교란 변수 무시 | 이중차분법(DID), synthetic control |
| 프로모션 반응 모델 | 선형 가정, SKU별 반응 차이 무시 | 4PL sigmoid (임계 할인율 추정) |
| 배송 리드타임 이상 탐지 | 알람 임계값 수동 설정 | ARIMA 잔차 + Ljung-Box 자동 탐지 |

### PCR·바이오테크 (씨젠, 바이오메리유, 로슈 등)

| 고민 | 현재 방법의 한계 | 적용 가능 방법론 |
|---|---|---|
| 그레이존 Ct 판정 불일치 | 단일 임계값, 재검 기준 불명확 | Bayesian posterior, 30/40/30 프로토콜 |
| 배치 간 증폭 효율 편차 | 배치별 독립 보정, 정보 손실 | 계층적 Bayesian, partial pooling |
| 피팅 품질 자동 평가 | R²만 확인, 잔차 구조 미검토 | ACF/Ljung-Box, AIC/BIC 자동화 |

### e-커머스 (네이버, 카카오, 쿠팡 등)

| 고민 | 현재 방법의 한계 | 적용 가능 방법론 |
|---|---|---|
| A/B 테스트 해석 오류 | Frequentist p-value, 다중 비교 미보정 | Bayesian A/B, ROPE 기반 의사결정 |
| 추천 cold-start | 인기도 기반 fallback, 개인화 없음 | 계층적 Bayesian 협업 필터링 |
| LTV 추정 불확실성 | 점 추정만 보고, CI 없음 | Bayesian LTV 모델, 불확실성 전파 |

---

## 역량 전이 매핑 (연결 고리 작성용)

Essay를 쓸 때 "기존 역량 → 새 문제" 연결 고리를 반드시 포함한다.

| 보유 역량 (PCR에서 한 것) | 새 도메인 동치 문제 | 연결 고리 한 문장 예시 |
|---|---|---|
| 4PL sigmoid 피팅 | 프로모션 반응 모델 | "PCR 증폭 곡선의 S자 구조가 할인율-전환율 반응 모델과 수학적으로 동일하다" |
| 계층적 Bayesian | 매장별 수요 예측 | "배치 간 Hill slope 공유 구조를 매장 간 계절성 공유로 그대로 전용한다" |
| 그레이존 처리 | 재고 발주 임계 | "Ct 35~40의 불확실 판정 처리 로직이 재주문점 회색지대 처리와 동일한 Bayesian 구조다" |
| ARIMA 잔차 탐지 | 배송 이상 탐지 | "RFU 시계열의 비정상 증폭 탐지 파이프라인을 리드타임 시계열에 그대로 적용한다" |
| AIC/BIC 모델 선택 | 추천 모델 complexity 관리 | "4PL vs 5PL 선택 기준이 추천 모델의 feature 추가 결정과 동일한 정보이론 원칙이다" |

---

## 작성 스타일 규칙

- **한다 체** (`~한다/~이다/~된다`) 유지
- **이모지 금지** (`.qmd` 내)
- **수동 번호 금지** (`number-sections: true` 자동 적용)
- 수식 있으면 직관 설명 必 (수식만 넣으면 안 됨)
- **비즈니스 임팩트 수치**가 없는 Essay는 미완성으로 간주

---

## Self-Check (작성 완료 전 확인)

```
- [ ] 조직의 고민이 수치화됐는가?
- [ ] As-Is 한계가 기술적으로 설명됐는가?
- [ ] 내 방법론의 핵심 수식/코드가 있는가?
- [ ] 기존 역량(PCR 등)과의 연결 고리가 명시됐는가?
- [ ] KPI 개선 수치(범위라도)가 있는가?
- [ ] 3단계 이상의 실행 로드맵이 있는가?
- [ ] 한다 체, 이모지 없음, 수동 번호 없음
```
