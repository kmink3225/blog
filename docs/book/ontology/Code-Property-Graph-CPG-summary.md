# Code Property Graph (CPG) Specification — Summary

> Source: Joern 프로젝트 (https://joern.io), CPG Spec v1.1
> 원본 논문: Yamaguchi et al., "Modeling and Discovering Vulnerabilities with Code Property Graphs" (IEEE S&P 2014)
> 핵심: AST + CFG + PDG를 하나의 그래프로 통합한 코드 표현 모델
> 프로젝트 맥락: 코드 온톨로지의 노드/관계 설계 레퍼런스. 언어 무관 코드 그래프의 사실상 표준

---

## CPG란 무엇인가

Code Property Graph는 세 가지 코드 표현을 **하나의 방향성 다중 그래프**로 통합한 것이다:

```
AST (Abstract Syntax Tree)     — 코드의 구문 구조
  +
CFG (Control Flow Graph)       — 실행 흐름
  +
PDG (Program Dependence Graph) — 데이터/제어 의존성
  =
CPG (Code Property Graph)      — 통합 그래프
```

### 왜 통합하는가

| 개별 표현 | 답할 수 있는 질문 | 못 답하는 질문 |
|---|---|---|
| AST만 | "이 함수의 파라미터 타입은?" | "이 변수가 어떤 경로로 반환되는가?" |
| CFG만 | "이 분기에서 어디로 가는가?" | "이 변수의 값이 어디서 오는가?" |
| PDG만 | "이 변수가 어디에 의존하는가?" | "코드의 구문 구조는?" |
| **CPG** | **위 질문 모두** | |

---

## CPG 레이어 구조

CPG는 계층적 레이어로 구성된다. 각 레이어는 노드 유형, 엣지 유형, 속성을 정의한다.

### Layer 1: MetaData

그래프 생성 정보를 담는 메타데이터.

```
META_DATA 노드:
  - LANGUAGE: "python" | "java" | "javascript" | ...
  - VERSION: CPG 스펙 버전
  - ROOT: 소스 루트 경로
  - OVERLAYS: 적용된 오버레이 목록
```

코드 온톨로지 적용: 40개 리포를 하나의 그래프로 통합할 때, 각 리포의 메타데이터를 이 레이어로 관리한다.

### Layer 2: FileSystem

소스 파일 구조와 위치 정보.

```
FILE 노드:
  - NAME: 파일 경로
  - HASH: 파일 해시

모든 노드의 위치 속성:
  - FILENAME: 상대 경로
  - LINE_NUMBER / LINE_NUMBER_END
  - COLUMN_NUMBER / COLUMN_NUMBER_END
```

코드 온톨로지 적용: 분석 결과를 실제 코드 위치에 매핑할 때 필수. "이 의존성은 어느 파일 몇 번째 줄에서 발생하는가?"

### Layer 3: Namespace

네임스페이스 구조.

```
NAMESPACE 노드: 네임스페이스 정의
NAMESPACE_BLOCK 노드: 네임스페이스 참조 블록
  - FULL_NAME: "com.example.auth" (점 구분)
```

코드 온톨로지 적용: 40개 리포 간 엔터티 충돌 방지를 위한 네임스페이스 설계에 참조.

### Layer 4: Method

함수/메서드 선언.

```
METHOD 노드:
  - NAME: 메서드 이름
  - FULL_NAME: 정규화된 전체 이름
  - SIGNATURE: 파라미터 타입 인코딩
  - IS_EXTERNAL: 외부(분석 범위 밖) 여부
  - AST_PARENT_TYPE: 소속 (METHOD | TYPE_DECL | NAMESPACE_BLOCK)
  - AST_PARENT_FULL_NAME: 소속 엔터티 전체 이름

METHOD_PARAMETER_IN 노드:
  - NAME: 파라미터 이름
  - TYPE_FULL_NAME: 타입
  - INDEX: 위치 (0부터)
  - IS_VARIADIC: 가변 인자 여부
  - EVALUATION_STRATEGY: BY_VALUE | BY_REFERENCE | BY_SHARING

METHOD_RETURN 노드:
  - TYPE_FULL_NAME: 반환 타입
```

코드 온톨로지 적용: **Function 노드의 속성 설계에 직접 참조**. 특히 FULL_NAME, SIGNATURE, IS_EXTERNAL 속성은 리포 간 함수 식별에 핵심.

### Layer 5: Type

타입 선언과 관계.

```
TYPE 노드:
  - FULL_NAME: 인스턴스화된 타입 전체 이름
  - TYPE_DECL_FULL_NAME: 선언 참조

TYPE_DECL 노드:
  - FULL_NAME: 타입 선언 전체 이름
  - IS_EXTERNAL: 외부 타입 여부
  - INHERITS_FROM_TYPE_FULL_NAME: 상속 목록
  - ALIAS_TYPE_FULL_NAME: 별칭 (typedef)

MEMBER 노드:
  - NAME: 멤버(필드) 이름
  - TYPE_FULL_NAME: 멤버 타입

엣지:
  - INHERITS_FROM: 상속 관계
  - ALIAS_OF: 타입 별칭 관계
  - BINDS_TO: 제네릭 타입 인자 바인딩
```

코드 온톨로지 적용: **Class 노드와 INHERITS_FROM 관계 설계에 직접 참조**. INHERITS_FROM_TYPE_FULL_NAME 리스트로 다중 상속/구현을 표현.

### Layer 6: AST (Abstract Syntax Tree)

코드의 구문 구조.

**표현식(Expression) 노드:**

| 노드 유형 | 설명 | 핵심 속성 |
|---|---|---|
| `CALL` | 함수/메서드 호출 | METHOD_FULL_NAME, DISPATCH_TYPE |
| `IDENTIFIER` | 변수 참조 | NAME, TYPE_FULL_NAME |
| `LITERAL` | 리터럴 값 | TYPE_FULL_NAME |
| `FIELD_IDENTIFIER` | 필드 접근 | CANONICAL_NAME |
| `METHOD_REF` | 메서드 참조 | METHOD_FULL_NAME |

**문(Statement) 노드:**

| 노드 유형 | 설명 | 하위 유형 |
|---|---|---|
| `BLOCK` | 블록 | |
| `CONTROL_STRUCTURE` | 제어 구조 | IF, ELSE, FOR, WHILE, DO, SWITCH, TRY, THROW |
| `RETURN` | 반환문 | |
| `LOCAL` | 지역 변수 선언 | |

**CALL 노드의 DISPATCH_TYPE:**

| 타입 | 설명 | 코드 온톨로지 영향 |
|---|---|---|
| `STATIC_DISPATCH` | 컴파일 타임에 호출 대상 결정 | 정확한 호출 관계 추출 가능 |
| `DYNAMIC_DISPATCH` | 런타임에 호출 대상 결정 | 호출 관계가 불확실할 수 있음 |

코드 온톨로지 적용: CALL 노드의 METHOD_FULL_NAME이 **CALLS 관계의 target을 결정**한다. DYNAMIC_DISPATCH인 경우 여러 후보가 있을 수 있어 그래프에서 다중 관계로 표현해야 한다.

### Layer 7: Call Graph

메서드 간 호출 관계.

```
엣지:
  - CALL: 호출 사이트 → 호출 대상 메서드
  - ARGUMENT: 호출 → 인자, 반환 → 식
  - RECEIVER: 호출 → 수신 객체
```

코드 온톨로지 적용: **CALLS 관계의 직접적 레퍼런스**. CPG의 Call Graph 레이어가 코드 온톨로지의 호출 관계 모델 그 자체다.

### Layer 8: CFG (Control Flow Graph)

실행 흐름.

```
CFG_NODE: 제어 흐름의 노드 (AST_NODE 확장)
CFG 엣지: 소스 → 목적지 (실행 순서)
```

코드 온톨로지 적용: 의존성/영향도 분석에서는 CFG를 직접 사용하기보다, **조건부 호출 여부**를 CALLS 관계의 속성(`is_conditional`)으로 반영한다.

### Layer 9: PDG (Program Dependence Graph)

데이터/제어 의존성.

```
REACHING_DEF 엣지: 변수 데이터 의존성 (VARIABLE 속성 포함)
CDG 엣지: 제어 의존성
```

코드 온톨로지 적용: 데이터 흐름 수준의 영향도 분석이 필요할 때 참조. "설정값이 어떤 변수를 거쳐 어떤 출력에 영향을 미치는가?"

### Layer 10: Configuration

설정 파일 표현.

```
CONFIG_FILE 노드:
  - NAME: 설정 파일 경로
  - CONTENT: 파일 내용 (verbatim)
```

코드 온톨로지 적용: **Config 노드와 READS_CONFIG 관계**의 직접적 레퍼런스. 설정 변경 영향도 분석의 기반.

---

## CPG 노드/엣지 전체 요약

### 핵심 노드 유형

| 노드 | 레이어 | 코드 온톨로지 대응 | 우선순위 |
|---|---|---|---|
| METHOD | Method | Function 노드 | **필수** |
| METHOD_PARAMETER_IN | Method | Parameter 속성 | **필수** |
| TYPE_DECL | Type | Class 노드 | **필수** |
| MEMBER | Type | Field 속성 | 선택 |
| CALL | AST | CALLS 관계의 근거 | **필수** |
| IDENTIFIER | AST | 변수 참조 추적 | 선택 |
| FILE | FileSystem | Module 노드의 file_path | **필수** |
| CONFIG_FILE | Configuration | Config 노드 | 중요 |
| NAMESPACE_BLOCK | Namespace | 네임스페이스 속성 | 중요 |
| LOCAL | AST | 지역 변수 | 선택 |

### 핵심 엣지 유형

| 엣지 | 레이어 | 코드 온톨로지 대응 | 우선순위 |
|---|---|---|---|
| AST | AST | HAS_METHOD, DEFINES | **필수** |
| CALL | CallGraph | CALLS | **필수** |
| INHERITS_FROM | Type | INHERITS_FROM | **필수** |
| CFG | CFG | (조건부 호출 속성으로 반영) | 선택 |
| REACHING_DEF | PDG | (데이터 흐름 분석 시) | 선택 |
| CDG | PDG | (제어 의존성 분석 시) | 선택 |
| SOURCE_FILE | FileSystem | BELONGS_TO | **필수** |
| CONTAINS | Shortcuts | CONTAINS | **필수** |
| REF | Base | 변수→선언 참조 | 중요 |

---

## CPG → 코드 온톨로지 변환 매핑

### 최소 온톨로지 (Phase 1)

CPG에서 의존성/영향도 분석에 필요한 최소 요소만 추출:

```
CPG                          코드 온톨로지 (Neo4j)
───────────────────          ───────────────────────
FILE                    →    (:Module {name, file_path, loc})
METHOD                  →    (:Function {name, full_name, signature})
TYPE_DECL               →    (:Class {name, full_name, is_external})
CONFIG_FILE             →    (:Config {name, content})
NAMESPACE_BLOCK         →    (:Repository {name, language})

AST (METHOD→TYPE_DECL)  →    -[:DEFINES]->
CALL                    →    -[:CALLS {line, dispatch_type}]->
INHERITS_FROM           →    -[:INHERITS_FROM]->
SOURCE_FILE             →    -[:BELONGS_TO]->
import 구문 (AST 패턴)  →    -[:IMPORTS]->
config 참조 (AST 패턴)  →    -[:READS_CONFIG]->
```

### 확장 온톨로지 (Phase 2)

데이터 흐름/제어 흐름까지 포함:

```
REACHING_DEF            →    -[:DATA_DEPENDS_ON {variable}]->
CDG                     →    -[:CONTROL_DEPENDS_ON]->
MEMBER                  →    (:Field {name, type})
LOCAL                   →    (:Variable {name, type, scope})
```

---

## 다중 언어 처리

CPG는 **언어 무관(language-agnostic)** 설계이다. 각 언어의 프론트엔드가 언어별 구문을 공통 CPG 노드로 변환한다.

| 언어 구문 | CPG 표현 |
|---|---|
| Python `def func():` | METHOD 노드 |
| Java `void func() {}` | METHOD 노드 |
| JS `function func()` | METHOD 노드 |
| Python `class Foo(Bar):` | TYPE_DECL + INHERITS_FROM |
| Java `class Foo extends Bar` | TYPE_DECL + INHERITS_FROM |
| Python `import module` | AST 패턴으로 IMPORTS 추출 |
| Java `import com.pkg.Class` | AST 패턴으로 IMPORTS 추출 |

코드 온톨로지 적용: 40개 리포가 여러 언어로 되어 있어도 **하나의 통합 그래프**로 표현할 수 있다. CPG의 언어 무관 설계를 그대로 차용한다.

---

## 도구 생태계

| 도구 | 역할 | 코드 온톨로지 활용 |
|---|---|---|
| **Joern** | CPG 생성 + 쿼리 (Scala) | AST→CPG 변환 파이프라인으로 사용 가능 |
| **CodeQL** | 관계형 코드 DB + QL 쿼리 | 정밀 보안 분석에 보완적 사용 |
| **tree-sitter** | 범용 AST 파서 (다중 언어) | 경량 AST 추출에 사용 가능 |
| **jedi (Python)** | Python 정적 분석/타입 추론 | Python 리포의 호출 관계 보강 |
| **ts-morph (TypeScript)** | TS AST + 타입 시스템 접근 | TS/JS 리포의 정밀 분석 |

### 실무 파이프라인 선택지

```
Option A: Joern 직접 사용
  소스 코드 → Joern → CPG → 변환 스크립트 → Neo4j

Option B: tree-sitter 기반 직접 구축
  소스 코드 → tree-sitter (AST) → 자체 분석기 (호출/의존성) → Neo4j

Option C: 언어별 전용 도구
  Python → jedi/pyan
  TypeScript → ts-morph
  Java → CodeQL extractor
  → 변환 → Neo4j
```

40개 리포가 다중 언어면 **Option A(Joern)** 또는 **Option B(tree-sitter)**가 언어 통합 관점에서 유리하다. 단일 언어가 지배적이면 Option C가 정밀도에서 유리하다.
