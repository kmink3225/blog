# Knowledge Graphs: Fundamentals, Techniques, and Applications — Summary

> 저자: Kejriwal, Knoblock, Szekely (2021)
> 핵심: 지식 그래프의 설계, 구축, 추론, 응용을 체계적으로 정리한 교과서
> 프로젝트 맥락: 코드베이스 온톨로지 설계, GraphRAG retriever, 의존성 그래프 구축에 직결

---

## Part 1: 지식 그래프 기초

### 지식 그래프란 무엇인가

지식 그래프는 엔터티(entity)와 관계(relation)를 그래프 구조로 표현한 지식 베이스이다.

```
(엔터티) --[관계]--> (엔터티)
(Module_A) --[imports]--> (Module_B)
(Function_X) --[calls]--> (Function_Y)
(Class_C) --[inherits]--> (Class_D)
```

### 트리플 (Triple)

지식 그래프의 기본 단위:

```
(Subject, Predicate, Object)
(auth_service, depends_on, database_module)
(login_function, has_parameter, username:string)
(UserController, inherits_from, BaseController)
```

### 코드베이스 온톨로지에의 적용

코드베이스를 지식 그래프로 표현할 때의 트리플 구조:

| Subject | Predicate | Object |
|---|---|---|
| Module | imports | Module |
| Function | calls | Function |
| Function | has_parameter | Parameter |
| Function | returns | Type |
| Class | inherits_from | Class |
| Class | has_method | Function |
| Module | belongs_to | Repository |
| Config | affects | Module |
| Function | reads | Config_Value |
| Function | writes | Database_Table |

---

## Part 2: 온톨로지 설계

### 온톨로지의 구성 요소

| 요소 | 설명 | 코드 온톨로지 예시 |
|---|---|---|
| **Class (클래스)** | 엔터티의 범주 | Module, Function, Class, Config, Repository |
| **Property (속성)** | 엔터티의 특성 | name, file_path, line_number, visibility |
| **Relation (관계)** | 엔터티 간 연결 | imports, calls, inherits, depends_on |
| **Instance (인스턴스)** | 구체적 엔터티 | auth_service.py, login(), UserModel |
| **Axiom (공리)** | 제약 조건 | "모든 Function은 정확히 하나의 Module에 속한다" |

### 온톨로지 설계 원칙

**1. 명확한 범위 정의 (Scope)**

- 온톨로지가 답해야 할 질문을 먼저 정의한다
- 코드베이스 분석 맥락:
  - "모듈 A를 변경하면 어디에 영향이 있는가?"
  - "이 함수를 호출하는 모든 경로는?"
  - "리포 간 순환 의존성이 있는가?"

**2. 재사용 (Reuse)**

- 기존 온톨로지를 활용한다
- 코드 온톨로지: CodeOntology, Software Ontology (SWO), Schema.org/SoftwareSourceCode

**3. 열거 vs 정의 (Enumeration vs Definition)**

| 접근 | 설명 | 코드 온톨로지 적용 |
|---|---|---|
| 열거적 | 인스턴스를 나열 | 모든 함수, 클래스를 개별 노드로 등록 |
| 정의적 | 클래스의 특성으로 멤버십 결정 | "public 메서드이면서 외부 모듈에서 호출 가능한 것" |

**4. 클래스 계층 설계**

```
CodeEntity
├── Module
│   ├── PythonModule
│   ├── JavaScriptModule
│   └── ConfigModule
├── Function
│   ├── Method (클래스 내 함수)
│   ├── StaticFunction
│   └── Lambda
├── Class
│   ├── AbstractClass
│   ├── Interface
│   └── DataClass
├── Variable
│   ├── GlobalVariable
│   ├── ConfigValue
│   └── EnvironmentVariable
└── Repository
    ├── Library
    └── Service
```

### 관계(Relation) 설계

**구조적 관계 (정적 분석으로 추출):**

| 관계 | 설명 | AST 추출 가능 |
|---|---|---|
| `imports` | 모듈 간 import 관계 | O |
| `calls` | 함수/메서드 호출 | O |
| `inherits_from` | 클래스 상속 | O |
| `implements` | 인터페이스 구현 | O |
| `has_method` | 클래스→메서드 소속 | O |
| `has_parameter` | 함수→파라미터 | O |
| `returns` | 함수→반환 타입 | O |
| `reads_config` | 함수→설정값 읽기 | O (패턴 매칭) |
| `writes_to` | 함수→DB/파일 쓰기 | △ (패턴 매칭) |

**의미적 관계 (추론 또는 수동 정의):**

| 관계 | 설명 | 추출 방법 |
|---|---|---|
| `depends_on` | 모듈 간 의존성 (imports의 전이적 폐쇄) | 그래프 순회 |
| `affects` | 변경 시 영향받는 엔터티 | 역방향 의존성 추적 |
| `co_changes_with` | 함께 변경되는 경향 | git log 분석 |
| `semantically_similar` | 의미적으로 유사한 코드 | 임베딩 유사도 |

---

## Part 3: 지식 그래프 구축

### 구축 파이프라인

```
소스 코드 (40개 리포)
    ↓
[1] AST 파싱 → 구조적 엔터티/관계 추출
    ↓
[2] 정적 분석 → 호출 그래프, 의존성 그래프
    ↓
[3] Git 분석 → 공동 변경 패턴 (co_changes_with)
    ↓
[4] 온톨로지 매핑 → 트리플 생성
    ↓
[5] 그래프 DB 적재 (Neo4j)
    ↓
[6] 추론 & 보강 → 전이적 관계 계산, 유사도 추가
```

### 엔터티 추출 (Entity Extraction)

AST 기반 추출이 코드 온톨로지의 핵심이다:

**Python AST 예시:**

```python
# 추출 대상
import module_b          # → (current_module, imports, module_b)
from module_c import X   # → (current_module, imports, module_c)

class MyClass(Base):     # → (MyClass, inherits_from, Base)
    def method(self, x): # → (MyClass, has_method, method)
        module_b.func()  # → (method, calls, module_b.func)
```

**추출 결과 트리플:**

```
(my_module, imports, module_b)
(my_module, imports, module_c)
(MyClass, inherits_from, Base)
(MyClass, has_method, method)
(MyClass.method, calls, module_b.func)
(MyClass.method, has_parameter, x)
```

### 관계 추출 (Relation Extraction)

| 추출 방법 | 적용 | 정확도 |
|---|---|---|
| AST 패턴 매칭 | import, call, inheritance | 매우 높음 |
| 타입 추론 | 동적 타입 언어의 호출 관계 | 중간 |
| 정규식 | config 읽기, DB 접근 패턴 | 중간 |
| Git co-change 분석 | 의미적 연관성 | 낮음~중간 |
| 임베딩 유사도 | 의미적 유사성 | 중간 |

### 엔터티 해소 (Entity Resolution)

40개 리포에서 같은 엔터티를 식별하는 문제:

| 문제 | 예시 | 해결 |
|---|---|---|
| 동일 모듈의 다른 이름 | `utils` vs `common.utils` | 정규화된 경로(FQN) 사용 |
| 리포 간 같은 이름 | 리포 A의 `User` vs 리포 B의 `User` | `repo:module:class` 네임스페이스 |
| 버전별 차이 | v1의 `login()` vs v2의 `login()` | 버전 태그 추가 |

**코드 온톨로지의 URI 설계:**

```
code:{repo}/{module_path}/{entity_type}/{entity_name}
code:auth-service/src/controllers/class/UserController
code:auth-service/src/controllers/method/UserController.login
code:shared-lib/src/utils/function/validate_email
```

---

## Part 4: 지식 그래프 추론

### 전이적 폐쇄 (Transitive Closure)

"모듈 3→모듈 97 영향도" 질문의 핵심 메커니즘:

```
imports 관계의 전이적 폐쇄:
A imports B, B imports C → A (transitively) depends_on C

calls 관계의 전이적 폐쇄:
f() calls g(), g() calls h() → f() (transitively) reaches h()
```

그래프 쿼리로 구현:

```cypher
// Neo4j Cypher: 모듈 A에서 모듈 Z까지의 모든 경로
MATCH path = (a:Module {name: 'module_3'})-[:IMPORTS|CALLS*]->(z:Module {name: 'module_97'})
RETURN path
```

### 경로 기반 추론 (Path-Based Reasoning)

| 추론 유형 | 질문 | 그래프 연산 |
|---|---|---|
| 도달 가능성 | "A에서 Z에 도달할 수 있는가?" | BFS/DFS |
| 최단 경로 | "가장 직접적인 의존 경로는?" | Dijkstra, BFS |
| 모든 경로 | "모든 의존 경로를 열거하라" | 전체 경로 탐색 |
| 영향 범위 | "A를 변경하면 영향받는 모든 노드" | 역방향 BFS |
| 순환 탐지 | "순환 의존성이 있는가?" | SCC (Strongly Connected Components) |
| 중요도 | "가장 많이 의존되는 모듈은?" | PageRank, 중심성(Centrality) |

### 규칙 기반 추론

```
# 규칙 1: 전이적 의존성
IF (A, imports, B) AND (B, imports, C) THEN (A, depends_on, C)

# 규칙 2: 영향 전파
IF (A, depends_on, B) AND (B, changed) THEN (A, potentially_affected)

# 규칙 3: 순환 의존성 경고
IF (A, depends_on, B) AND (B, depends_on, A) THEN (A, circular_dependency, B)

# 규칙 4: 설정 영향
IF (F, reads_config, C) AND (C, changed) THEN (F, behavior_may_change)
```

### 그래프 임베딩 (Graph Embedding)

노드를 벡터 공간에 매핑하여 유사도 계산:

| 기법 | 설명 | 코드 온톨로지 활용 |
|---|---|---|
| TransE | 관계를 벡터 변환으로 모델링 | 단순 의존성 예측 |
| Node2Vec | 랜덤 워크 기반 노드 임베딩 | 구조적으로 유사한 모듈 탐지 |
| GNN (Graph Neural Network) | 이웃 정보를 집계하여 노드 표현 학습 | 변경 영향 예측, 버그 전파 예측 |

---

## Part 5: 지식 그래프 쿼리

### Cypher (Neo4j) 핵심 패턴

**기본 조회:**

```cypher
// 특정 모듈이 import하는 모든 모듈
MATCH (m:Module {name: 'auth_service'})-[:IMPORTS]->(dep)
RETURN dep.name

// 특정 함수를 호출하는 모든 함수
MATCH (caller)-[:CALLS]->(f:Function {name: 'validate_token'})
RETURN caller.module, caller.name
```

**영향도 분석:**

```cypher
// 모듈 변경 시 영향받는 모든 모듈 (N홉)
MATCH (changed:Module {name: 'module_3'})<-[:IMPORTS*]-(affected)
RETURN DISTINCT affected.name, affected.repository

// 설정 변경 시 영향받는 모든 함수
MATCH (c:Config {key: 'MAX_RETRIES'})<-[:READS_CONFIG]-(f:Function)
RETURN f.module, f.name
```

**순환 의존성 탐지:**

```cypher
// 순환 의존성이 있는 모듈 쌍
MATCH (a:Module)-[:IMPORTS*]->(b:Module)-[:IMPORTS*]->(a)
WHERE a <> b
RETURN DISTINCT a.name, b.name
```

**중심성 분석:**

```cypher
// 가장 많이 의존되는 모듈 (in-degree)
MATCH (dep:Module)<-[:IMPORTS]-(user)
RETURN dep.name, dep.repository, count(user) AS dependents
ORDER BY dependents DESC
LIMIT 10
```

### SPARQL (RDF 기반) 핵심 패턴

```sparql
# 리포 간 교차 의존성
SELECT ?repo_a ?module_a ?repo_b ?module_b
WHERE {
  ?module_a code:belongs_to ?repo_a .
  ?module_b code:belongs_to ?repo_b .
  ?module_a code:imports ?module_b .
  FILTER (?repo_a != ?repo_b)
}
```

---

## Part 6: 지식 그래프 유지보수

### 증분 업데이트 (Incremental Update)

코드 변경 시 전체 그래프를 재빌드하지 않고 변경분만 갱신:

```
Git diff 분석
    ↓
변경된 파일 목록 추출
    ↓
해당 파일의 기존 트리플 삭제
    ↓
변경된 파일 재파싱 → 새 트리플 생성
    ↓
그래프 DB에 새 트리플 삽입
    ↓
전이적 관계 재계산 (영향받는 부분만)
```

### CI/CD 통합

```
코드 Push → CI 파이프라인 트리거
    ↓
AST 재파싱 (변경 파일만)
    ↓
트리플 diff 생성 (추가/삭제/수정)
    ↓
그래프 DB 업데이트
    ↓
영향도 보고서 자동 생성 (선택)
```

### 품질 보장

| 품질 차원 | 검증 방법 |
|---|---|
| 완전성 | AST 추출 커버리지 측정 (전체 함수/클래스 중 그래프에 있는 비율) |
| 정확성 | 샘플링하여 트리플의 실제 코드 대응 확인 |
| 최신성 | 그래프 최종 업데이트 시점 vs 코드 최종 커밋 시점 비교 |
| 일관성 | 고아 노드(참조되지 않는 엔터티), 깨진 관계 탐지 |

---

## Part 7: 응용 — 코드베이스 분석 에이전트

### 질문 유형별 그래프 쿼리 매핑

| 사용자 질문 | 그래프 연산 | 쿼리 패턴 |
|---|---|---|
| "이 함수 뭐 해?" | 노드 속성 조회 + 1홉 이웃 | 단일 노드 + 관계 |
| "이 설정 바꾸면?" | reads_config 역추적 | 1~2홉 역방향 |
| "모듈 3→97 영향?" | 경로 탐색 | 다중홉 경로 |
| "순환 의존성?" | SCC 알고리즘 | 전체 그래프 |
| "가장 위험한 모듈?" | 중심성 분석 | PageRank/Betweenness |
| "이 인터페이스 변경 시?" | implements 역추적 + 전이적 영향 | 다중홉 역방향 |
| "사용되지 않는 코드?" | in-degree 0 노드 탐지 | 전체 그래프 스캔 |

### LLM과의 통합 (GraphRAG)

```
사용자 질문
    ↓
LLM이 질문을 분석하여 그래프 쿼리 의도 파악
    ↓
Skill Prompt가 쿼리 유형 분류
    ↓
그래프 쿼리 생성 (Cypher/SPARQL)
    ↓
그래프 DB에서 결과 반환 (deterministic)
    ↓
LLM이 결과를 자연어로 설명
    ↓
필요시 관련 코드 파일을 추가 retrieve하여 상세 설명 보강
```

**핵심**: 의존성 추적은 그래프가 하고, LLM은 결과를 설명만 한다. 이것이 환각을 구조적으로 방지하는 메커니즘이다.
