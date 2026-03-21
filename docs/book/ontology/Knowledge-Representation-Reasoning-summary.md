# Knowledge Representation and Reasoning — Summary

> 저자: Brachman, Levesque (2004, 개정 2022)
> 핵심: 지식 표현의 이론적 기초. 논리, 프레임, 의미망, 기술 논리
> 프로젝트 맥락: 코드 온톨로지의 표현력과 추론 능력의 이론적 기반

---

## Part 1: 지식 표현이란 무엇인가

### 표현의 다섯 가지 역할

1. **대리자 (Surrogate)**: 실세계 대상을 대신하는 기호
2. **존재론적 약속 (Ontological Commitment)**: 세계를 어떤 범주로 나눌 것인가
3. **단편적 이론 (Fragmentary Theory)**: 세계의 일부를 불완전하게 표현
4. **효율적 계산의 매체 (Medium of Computation)**: 추론이 가능한 형태
5. **인간 표현의 매체 (Medium of Expression)**: 사람이 이해하고 소통할 수 있는 형태

### 코드 온톨로지에의 시사점

코드베이스를 표현할 때, 위 다섯 역할을 모두 만족해야 한다:

| 역할 | 코드 온톨로지 적용 |
|---|---|
| 대리자 | 함수/클래스/모듈 노드가 실제 코드를 대신 |
| 존재론적 약속 | Module, Function, Class, Config 등으로 세계를 분류 |
| 단편적 이론 | 모든 코드 의미를 포착하지 않음 (호출 관계, 의존성 등 선택적) |
| 효율적 계산 | 그래프 쿼리로 추론 가능한 형태 |
| 인간 표현 | 개발자가 결과를 이해할 수 있는 형태로 표현 |

---

## Part 2: 명제 논리 (Propositional Logic)

### 기본 구성

- 명제 변수: p, q, r (참/거짓)
- 논리 연결자: ∧(AND), ∨(OR), ¬(NOT), →(IF-THEN), ↔(IFF)

### 코드 온톨로지 적용

```
p: "module_A가 module_B를 import한다"
q: "module_B가 변경되었다"
r: "module_A가 영향받는다"

규칙: (p ∧ q) → r
"A가 B를 import하고, B가 변경되었으면, A가 영향받는다"
```

### 한계

- 내부 구조를 표현할 수 없다 (개체, 관계, 양화 불가)
- "모든 모듈", "어떤 함수" 같은 표현 불가
- → 술어 논리로 확장 필요

---

## Part 3: 술어 논리 (First-Order Logic)

### 기본 구성

- 상수: `auth_service`, `login_function`
- 변수: x, y
- 술어: `imports(x, y)`, `calls(x, y)`, `belongs_to(x, y)`
- 양화사: ∀(모든), ∃(존재하는)
- 함수: `module_of(x)`, `return_type(x)`

### 코드 온톨로지 규칙의 형식화

```
# 전이적 의존성
∀x,y,z: imports(x,y) ∧ imports(y,z) → depends_on(x,z)

# 변경 영향 전파
∀x,y: depends_on(x,y) ∧ changed(y) → potentially_affected(x)

# 순환 의존성 경고
∀x,y: depends_on(x,y) ∧ depends_on(y,x) → circular_dependency(x,y)

# 미사용 함수 탐지
∀f: function(f) ∧ ¬∃g: calls(g,f) → unused(f)

# 인터페이스 변경 영향
∀c,i: implements(c,i) ∧ interface_changed(i) → must_update(c)
```

### 개방 세계 가정 vs 폐쇄 세계 가정

| 가정 | 설명 | 코드 온톨로지 적용 |
|---|---|---|
| **개방 세계 (OWA)** | 알려지지 않은 것은 참일 수도 거짓일 수도 | 동적 호출, 리플렉션 → 정적 분석으로 포착 못한 관계가 존재할 수 있음 |
| **폐쇄 세계 (CWA)** | 알려지지 않은 것은 거짓 | AST에서 추출되지 않은 관계는 없는 것으로 간주 |

코드 온톨로지는 기본적으로 **CWA**를 따르되, 동적 언어(Python, JavaScript)에서는 런타임 호출이 누락될 수 있음을 인지해야 한다.

---

## Part 4: 의미망 (Semantic Networks)

### 개념

엔터티를 노드로, 관계를 엣지로 표현하는 그래프:

```
[Module_A] --imports--> [Module_B]
[Module_B] --imports--> [Module_C]
[Function_X] --calls--> [Function_Y]
[Class_P] --is_a--> [AbstractBase]
```

### 관계 유형

| 관계 | 설명 | 특성 |
|---|---|---|
| **is-a** | 클래스 계층 (상속) | 전이적, 속성 상속 |
| **part-of** | 구성 관계 (메서드→클래스) | 전이적 |
| **has-a** | 소유 관계 (클래스→속성) | 비전이적 |
| **uses** | 사용 관계 (함수→라이브러리) | 비전이적 |

### 상속과 속성 전파

```
[Animal] --is_a--> [LivingThing]
  속성: has_life = true

[Dog] --is_a--> [Animal]
  → Dog는 has_life = true를 상속

코드 온톨로지 적용:
[UserController] --inherits_from--> [BaseController]
  → UserController는 BaseController의 모든 메서드를 상속
  → BaseController의 메서드 시그니처가 변경되면 UserController도 영향
```

### 다중 상속 문제

- 다이아몬드 문제: 두 부모 클래스에서 같은 메서드를 상속
- 코드 온톨로지에서 다중 상속/믹스인을 정확히 표현해야 한다
- MRO(Method Resolution Order) 정보도 그래프에 포함하는 것이 이상적

---

## Part 5: 프레임 (Frames)

### 개념

구조화된 지식 표현 단위. 슬롯(slot)에 값을 채우는 형태:

```
Frame: Function
  Slots:
    - name: "validate_token"
    - module: "auth_service"
    - parameters: [(token, str), (secret, str)]
    - return_type: bool
    - calls: [decode_jwt, check_expiry]
    - called_by: [login, refresh_token]
    - complexity: 12
    - last_modified: "2026-03-15"
    - repository: "auth-service"
```

### 코드 온톨로지에의 적용

프레임은 **노드의 풍부한 속성**을 표현하는 데 적합하다:

```
Frame: Module
  Slots:
    - name: "auth_service.controllers.user"
    - file_path: "src/controllers/user.py"
    - repository: "auth-service"
    - language: "python"
    - loc: 450
    - imports: [Module_A, Module_B, Module_C]
    - exports: [UserController, AdminController]
    - functions: [login, logout, register]
    - classes: [UserController]
    - config_dependencies: [JWT_SECRET, TOKEN_EXPIRY]
    - test_coverage: 0.85
    - last_commit: "abc1234"
    - authors: ["kim", "lee"]
```

### 디폴트 값과 예외

프레임은 디폴트 값을 지원한다:

```
Frame: PythonFunction (기본값)
  - visibility: "public"   (기본)
  - is_async: false         (기본)
  - has_docstring: true     (기본)

Frame: _internal_helper (예외)
  - visibility: "private"   (디폴트 오버라이드)
  - has_docstring: false     (디폴트 오버라이드)
```

---

## Part 6: 기술 논리 (Description Logic)

### OWL의 이론적 기반

기술 논리는 OWL(Web Ontology Language)의 수학적 기반이다. 온톨로지의 표현력과 추론 복잡도 사이의 트레이드오프를 다룬다.

### 핵심 구성자 (Constructor)

| 구성자 | 의미 | 코드 온톨로지 예시 |
|---|---|---|
| ⊓ (intersection) | AND | PublicFunction ⊓ AsyncFunction (공개이면서 비동기인 함수) |
| ⊔ (union) | OR | PythonModule ⊔ JavaScriptModule (Python 또는 JS 모듈) |
| ¬ (negation) | NOT | ¬Deprecated (비권장이 아닌) |
| ∃R.C (existential) | R 관계로 C에 연결된 것이 존재 | ∃calls.ExternalAPI (외부 API를 호출하는 함수) |
| ∀R.C (universal) | R 관계의 모든 대상이 C | ∀imports.InternalModule (내부 모듈만 import하는 모듈) |
| ≤n R (cardinality) | R 관계가 최대 n개 | ≤3 has_parameter (파라미터 3개 이하 함수) |

### 표현력 vs 계산 복잡도

| DL 언어 | 표현력 | 추론 복잡도 | 대응 OWL |
|---|---|---|---|
| ALC | 기본 (⊓, ⊔, ¬, ∃, ∀) | EXPTIME | OWL DL |
| SHIQ | 전이적 역할, 역관계, 한정 수량사 | EXPTIME | OWL DL |
| SROIQ | 위 + 역할 합성, 자기 참조 | 2NEXPTIME | OWL 2 DL |
| EL++ | ⊓, ∃만 (¬, ∀ 없음) | PTIME | OWL 2 EL |

**코드 온톨로지 권장:** EL++ 수준이면 충분하다. 코드의 구조적 관계는 대부분 교차(⊓)와 존재 양화(∃)로 표현 가능하며, 부정(¬)이나 전칭 양화(∀)가 필수적인 경우는 드물다. 추론 복잡도를 PTIME으로 유지할 수 있다.

---

## Part 7: 추론 방법

### 전방 추론 (Forward Chaining)

알려진 사실에서 출발하여 규칙을 적용, 새로운 사실을 도출:

```
사실: imports(A, B), imports(B, C)
규칙: imports(x,y) ∧ imports(y,z) → depends_on(x,z)
추론: depends_on(A, C)  ← 새로 도출
```

**코드 온톨로지 적용:** CI/CD에서 그래프 갱신 시 전방 추론으로 전이적 관계를 자동 계산한다.

### 후방 추론 (Backward Chaining)

목표에서 출발하여 필요한 사실을 역추적:

```
목표: "module_97이 module_3에 의존하는가?"
역추적: depends_on(97, 3)?
  ← imports(97, X) ∧ depends_on(X, 3)?
    ← imports(97, 50) ∧ depends_on(50, 3)?
      ← imports(50, 3) → 참!
경로: 97 → 50 → 3
```

**코드 온톨로지 적용:** 사용자 질문 시 후방 추론으로 경로를 탐색한다.

### 비단조 추론 (Non-Monotonic Reasoning)

새로운 정보가 추가되면 이전 결론이 철회될 수 있다:

```
기본 가정: "test_로 시작하는 함수는 프로덕션에서 호출되지 않는다"
예외 발견: "하지만 test_helper()는 프로덕션 코드에서 호출된다"
→ 기존 결론 철회
```

코드 온톨로지에서는 동적 분석 결과가 정적 분석 결과를 뒤집을 수 있다.

---

## 실무 설계 결정 가이드

### 코드 온톨로지 설계 시 결정 사항

| 결정 | 선택지 | 코드베이스 분석 권장 |
|---|---|---|
| 개방/폐쇄 세계 | OWA vs CWA | **CWA** (정적 분석 기반, 누락 인지) |
| 표현력 수준 | EL++ ~ SROIQ | **EL++** (충분하면서 빠름) |
| 추론 방향 | 전방 vs 후방 | **전방** (CI/CD에서 사전 계산) + **후방** (질문 시 동적 탐색) |
| 스키마 유연성 | 고정 vs 유연 | **반유연** (핵심 스키마 고정, 속성은 유연) |
| 저장 형태 | RDF(트리플) vs Property Graph | **Property Graph** (Neo4j, 노드/엣지 속성 풍부) |
