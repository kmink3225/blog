---
name: Agent_GUIDE
type: category
version: 1.0
description: LOAD when writing posts about LangChain, LangGraph, RAG, Agent architecture, prompt engineering, or GraphRAG. Covers code-centric tutorials with progressive complexity from basics to advanced agent patterns.
scope: docs/blog/posts/Agent/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Agent/index.qmd
book_sources:
  - docs/book/ontology/
cross_references:
  - docs/blog/posts/Engineering/GUIDE.md
  - docs/blog/posts/Math/GUIDE.md
  - docs/blog/posts/Deep_Learning/GUIDE.md
---

# Agent 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Agent 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **코드 중심 튜토리얼**: 개념 설명 후 반드시 실행 가능한 코드를 포함한다
- **LangChain/LangGraph 생태계 기반**: 프레임워크 버전 변화에 주의하여 작성한다
- **순차적 학습 경로**: 00-Intro → 12-RAG → 18-LangGraph → 24-Architecture 순으로 복잡도가 증가한다
- **실무 구현 지향**: "왜?"보다 "어떻게?"에 무게를 두되, 원리 이해도 함께 제공한다
- **파일명 패턴**: `번호-TopicName.qmd` (예: `01-PromptTemplate.qmd`)

---

## 포스트 콘텐츠 구조

Agent 카테고리의 포스트는 다음 구조를 따른다. 주제에 따라 일부 섹션을 생략하거나 순서를 조정할 수 있으나, 가능한 한 이 흐름을 유지한다.

### 1. 정의 (Definition)

- 기술 개념의 정의를 callout 블록으로 제시한다
- 공식 문서의 정의를 인용하고 한국어로 풀어 설명한다

```markdown
::: {.callout-note}
## 정의: RAG (Retrieval-Augmented Generation)

검색 증강 생성(RAG)은 LLM이 응답을 생성하기 전에 외부 지식 소스에서 관련 정보를
검색(retrieve)하여 컨텍스트로 제공하는 기법이다.

- 핵심 구성: Retriever(검색기) + Generator(생성기)
- 목적: LLM의 지식 한계(hallucination, 최신 정보 부재)를 보완
:::
```

### 2. 개념 및 원리 (Concept & Principles)

- 기술의 작동 원리를 아키텍처 수준에서 설명한다
- 데이터 흐름(pipeline)을 단계별로 분해한다
- 핵심 컴포넌트 간 관계를 명시한다
- 추상적이거나 이해하기 어려운 개념에는 비유, 기존 방식과의 비교 등 직관적 설명을 적재적소에 포함한다 (필요시 별도 섹션으로 분리 가능)

```markdown
## RAG 파이프라인

```
문서 → 청킹 → 임베딩 → 벡터 저장소
                                ↓
사용자 질의 → 임베딩 → 유사도 검색 → 상위 k개 문서 → LLM → 응답
```
```

### 3. 왜 필요한가 (Why It Matters)

- LLM의 한계와 이를 보완하는 방법을 설명한다
- 실무에서 마주하는 구체적 문제를 제시한다
- 대안 기술과의 비교를 통해 포지셔닝한다 (예: RAG vs Fine-tuning)

```markdown
| 접근법 | 장점 | 단점 | 적합한 경우 |
|---|---|---|---|
| Prompt Engineering | 구현 간단, 비용 낮음 | 컨텍스트 길이 제한 | 단순 질의 |
| RAG | 최신 정보, 출처 추적 가능 | 검색 품질에 의존 | 지식 기반 QA |
| Fine-tuning | 도메인 특화 성능 | 비용 높음, 데이터 필요 | 스타일/형식 학습 |
```

### 4. 응용 분야 (Applications)

- 산업/도메인별 활용 사례를 구체적으로 기술한다

```markdown
| 분야 | 활용 | 구체적 예시 |
|---|---|---|
| 기업 내부 | 사내 문서 QA | 사규/매뉴얼 검색 챗봇 |
| 법률 | 판례 검색 | 유사 판례 기반 법률 자문 |
| 의료 | 임상 가이드라인 검색 | 약물 상호작용 확인 시스템 |
| 고객 서비스 | FAQ 자동화 | 제품 매뉴얼 기반 고객 응대 |
| 교육 | 교재 기반 튜터링 | 학습 자료 기반 질의응답 |
```

### 5. 예시 (Examples)

- 입출력 예시를 구체적으로 보여준다
- 기대 동작과 실제 동작을 비교한다
- 실패 케이스와 성공 케이스를 대비한다

### 6. 코드 예시 (Code Examples)

- Python 코드로 구현한다 (이 카테고리의 핵심)
- 패키지: `langchain`, `langchain-openai`, `langchain-community`, `langgraph`, `chromadb`, `faiss` 등
- 코드는 복붙하여 실행 가능한 수준으로 작성한다
- 환경 설정(API 키, 패키지 설치)을 코드 상단에 명시한다
- 코드 블록 사이에 설명을 넣어 단계별로 이해할 수 있도록 한다

```markdown
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. 모델 초기화
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 2. 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 유능한 AI 어시스턴트입니다."),
    ("human", "{question}")
])

# 3. 체인 구성 (LCEL)
chain = prompt | llm

# 4. 실행
response = chain.invoke({"question": "RAG란 무엇인가?"})
print(response.content)
```
```

### 7. 관련 주제 (Related Topics)

- 포스트 끝에 관련 개념과 블로그 내 링크를 목록으로 제시한다
- 선행 지식(prerequisite)과 후속 주제(next)를 구분한다
- 같은 카테고리 내 + 다른 카테고리 링크를 모두 포함한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

```markdown
## 관련 주제

**선행 지식**

- [LangChain 기초](../01-Basic/01-langchain-intro.qmd)
- [임베딩 모델](../08-Embeddings/01-embeddings.qmd)

**후속 주제**

- [Advanced RAG 기법](../12-RAG/advanced-rag.qmd)
- [LangGraph로 Agent 구축](../18-LangGraph/01-langgraph-intro.qmd)

**다른 카테고리 연결**

- [벡터 공간과 유사도](../../Math/linear_algebra/02.norm_dot-product.qmd) — 임베딩의 수학적 기반
- [텍스트 전처리](../../Engineering/Python/text-processing.qmd) — 문서 파이프라인 구축
```

---

## 하위 카테고리별 추가 지침

### 기초 (00-Intro ~ 05-Memory)

- 각 컴포넌트를 독립적으로 설명한다
- LangChain의 클래스 구조와 인터페이스를 명시한다
- 간단한 예제로 시작하여 점진적으로 복잡도를 높인다

### 프롬프트 (02-Prompt/)

- 42개 파일로 구성된 대규모 시리즈이다
- 각 프롬프트 기법을 독립적으로 설명한다
- 입력-출력 예시를 반드시 포함한다
- 기법 간 비교를 제공한다 (어떤 상황에서 어떤 기법이 적합한가)

### 전처리 (06-DocumentLoader ~ 09-VectorStore)

- 문서 포맷별(PDF, CSV, HWP, Web 등) 로더를 다룬다
- 청킹 전략(recursive, semantic, token-based)의 trade-off를 설명한다
- 벡터 저장소(Chroma, FAISS, Pinecone) 비교를 포함한다

### RAG (12-RAG, 13-Cloud-RAG)

- Basic RAG → Advanced RAG(reranking, hybrid search, query transformation) 순서를 따른다
- Cloud-RAG는 Azure 서비스(AI Search, Document Intelligence) 기반이다
- 평가 메트릭(faithfulness, relevancy, context recall)을 포함한다

### LangGraph (18-LangGraph/)

- 3개 하위 섹션으로 구성: Core Features, Structures, Use Cases
- StateGraph, 노드, 엣지, 조건부 분기의 개념을 먼저 설명한다
- 시각적 그래프 다이어그램을 포함한다
- 상태 관리와 체크포인팅을 강조한다

### GraphRAG (21-GraphRAG/)

- Neo4j 기반 지식 그래프 구축을 다룬다
- 벡터 검색 vs 그래프 검색 vs 하이브리드 비교를 포함한다
- 엔티티-관계 추출 파이프라인을 설명한다

### Agent Architecture (24-Agent-Architecture/)

- 최신 Agent 설계 패턴(skill-based, progressive disclosure 등)을 다룬다
- 시스템 아키텍처 다이어그램을 포함한다
- 멀티 에이전트 시스템의 통신 패턴을 설명한다

---

## 자주 발생하는 오류 패턴

<fix-deprecated-api>
WRONG:
```python
from langchain.chat_models import ChatOpenAI
```
CORRECT:
```python
from langchain_openai import ChatOpenAI  # v0.3+
```
LangChain v0.3부터 `langchain.chat_models`, `langchain.llms` 등 monolithic import는 deprecated이다. 분리된 패키지(`langchain-openai`, `langchain-community` 등)에서 import한다.
</fix-deprecated-api>

<fix-hardcoded-api-key>
WRONG:
```python
llm = ChatOpenAI(openai_api_key="sk-...")  # API 키 직접 입력
```
CORRECT:
```python
from dotenv import load_dotenv
load_dotenv()  # .env 파일에서 OPENAI_API_KEY 자동 로드

llm = ChatOpenAI()  # 환경변수에서 자동 참조
```
API 키를 코드에 직접 포함하면 보안 사고로 이어진다. 반드시 환경변수(`.env` + `python-dotenv`)를 사용한다.
</fix-hardcoded-api-key>

---

## 코드 작성 규칙

- LangChain v0.3+ 문법을 사용한다 (deprecated API 사용 금지)
- `langchain-openai`, `langchain-community` 등 분리된 패키지명을 사용한다
- 환경 변수는 `dotenv`로 관리한다: `from dotenv import load_dotenv; load_dotenv()`
- 코드 블록에 언어 태그를 반드시 지정한다 (`python`, `bash`, `yaml` 등)
- 긴 코드는 기능 단위로 분할하고 사이에 설명을 넣는다
- API 키나 민감 정보를 코드에 직접 포함하지 않는다

---

## 버전 및 패키지 참고

포스트에서 사용하는 주요 패키지와 버전 정보를 명시한다:

```python
# 주요 패키지 (2026년 기준)
langchain >= 0.3
langchain-openai >= 0.2
langchain-community >= 0.3
langgraph >= 0.2
chromadb >= 0.5
faiss-cpu >= 1.8
```

버전에 민감한 API 변경이 있을 경우 callout으로 안내한다:

```markdown
::: {.callout-warning}
LangChain v0.3부터 `from langchain.chat_models import ChatOpenAI`는 deprecated이다.
`from langchain_openai import ChatOpenAI`를 사용한다.
:::
```

---

## 참고 소스

이 카테고리는 주로 **공식 문서와 GitHub 레포지토리**가 primary source이다. 기술 변화가 빠르므로 agent의 최신 사전지식으로 보완한다.

### 공통 (LangChain/LangGraph/LLM API)

| 소스 | 역할 |
|------|------|
| LangChain 공식 문서 (python.langchain.com) | 체인, 메모리, 도구, 출력 파서 등 핵심 API |
| LangGraph 공식 문서 (langchain-ai.github.io/langgraph) | 상태 그래프, 멀티 에이전트, 체크포인트 |
| LangChain GitHub (langchain-ai/langchain) | 최신 코드, 예제, 변경 이력 |
| LangGraph GitHub (langchain-ai/langgraph) | 그래프 기반 에이전트 구현 패턴 |
| OpenAI API 문서 (platform.openai.com/docs) | Chat Completions, Function Calling, Embeddings |
| Anthropic API 문서 (docs.anthropic.com) | Claude API, Tool Use |

### GraphRAG 하위 주제 — 교재 레퍼런스

GraphRAG(21-GraphRAG/) 관련 포스트 작성 시 다음 교재를 **논리적 뼈대**로 활용한다.

| 교재 | Summary 경로 | 활용 영역 |
|---|---|---|
| Kejriwal et al. — Knowledge Graphs (2021) | `docs/book/ontology/Knowledge-Graphs-Kejriwal-summary.md` | 지식 그래프 설계, 구축, 추론 |
| Robinson et al. — Graph Databases (2015) | `docs/book/ontology/Robinson-GraphDatabases-summary.md` | Neo4j, Cypher, 그래프 모델링 |
| CodeQL Documentation | `docs/book/ontology/CodeQL-summary.md` | 코드→관계형 DB, QL 쿼리 |
| CPG Specification | `docs/book/ontology/Code-Property-Graph-CPG-summary.md` | AST+CFG+PDG 통합 코드 그래프 |

**활용 절차**: 공식 문서에서 최신 API/패턴 확인 → agent 사전지식과 통합 → 블로그 스타일로 재작성. 버전 변경이 잦으므로 포스트에 사용한 패키지 버전을 명시한다. GraphRAG 주제는 교재 Summary → Full MD 참조도 병행한다.

---

## Boundaries

<boundaries>
### CAN (허용)
- 실행 가능한 코드 예시 제공 (복붙 즉시 실행 가능 수준)
- LangChain v0.3+ 문법 사용
- 사용한 패키지 버전 명시
- 공식 문서(LangChain, LangGraph, OpenAI, Anthropic) 기반 서술

### CANNOT (금지)
- deprecated API 사용 (`from langchain.chat_models import ...` 등 monolithic import)
- API 키를 코드에 직접 포함 (`openai_api_key="sk-..."`)
- 공식 문서에 없는 비공식 패턴 권장 (커뮤니티 해킹, undocumented internal API 등)
</boundaries>
