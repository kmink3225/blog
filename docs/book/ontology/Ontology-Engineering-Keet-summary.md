# Ontology Engineering — Summary

> 저자: C. Maria Keet (2020)
> 핵심: 온톨로지 설계 방법론, OWL, 설계 패턴, 평가, 유지보수
> 프로젝트 맥락: 코드 온톨로지의 체계적 설계 방법론과 품질 보장

---

## Part 1: 온톨로지 공학의 기초

### 온톨로지의 정의와 수준

| 수준 | 설명 | 코드 온톨로지 예시 |
|---|---|---|
| **상위 온톨로지 (Upper)** | 도메인 독립적 최상위 범주 | Entity, Process, Relation |
| **도메인 온톨로지 (Domain)** | 특정 분야의 개념 체계 | SoftwareEntity, CodeStructure |
| **태스크 온톨로지 (Task)** | 특정 작업을 위한 개념 | ImpactAnalysis, DependencyTrace |
| **응용 온톨로지 (Application)** | 특정 시스템용 | CodebaseAnalyzerOntology |

### 온톨로지 vs 데이터 모델

| 항목 | 데이터 모델 (DB 스키마) | 온톨로지 |
|---|---|---|
| 목적 | 데이터 저장 효율 | 지식 표현 & 추론 |
| 의미 | 암묵적 (개발자 머릿속) | 명시적 (기계 해석 가능) |
| 폐쇄/개방 | 폐쇄 세계 | 개방 세계 (기본) |
| 추론 | 없음 | 내장 (분류, 일관성 검증) |
| 진화 | 마이그레이션 필요 | 유연한 확장 |

---

## Part 2: 온톨로지 개발 방법론

### METHONTOLOGY (7단계)

| 단계 | 활동 | 코드 온톨로지 적용 |
|---|---|---|
| 1. 명세 | 목적, 범위, 사용자 정의 | "모듈 간 영향도 분석" |
| 2. 지식 획득 | 도메인 지식 수집 | AST 파서, 코드 구조 분석 |
| 3. 개념화 | 핵심 개념/관계 식별 | Module, Function, Class, imports, calls |
| 4. 통합 | 기존 온톨로지 재사용 | SWO, CodeOntology 참조 |
| 5. 구현 | 형식 언어로 인코딩 | OWL 또는 Property Graph Schema |
| 6. 평가 | 품질 검증 | 역량 질문 기반 검증 |
| 7. 문서화 | 온톨로지 문서 작성 | 스키마 문서, 사용 가이드 |

### 역량 질문 (Competency Questions)

온톨로지가 답할 수 있어야 하는 질문을 먼저 정의:

**코드베이스 분석 역량 질문:**

```
CQ1: 모듈 X를 변경하면 영향받는 모든 모듈은?
CQ2: 함수 f를 호출하는 모든 함수의 호출 체인은?
CQ3: 리포 A와 리포 B 사이의 모든 의존성 경로는?
CQ4: 순환 의존성이 있는 모듈 그룹은?
CQ5: 설정값 C를 읽는 모든 함수는?
CQ6: 클래스 K의 메서드 시그니처 변경 시 영향받는 하위 클래스는?
CQ7: 가장 많이 의존되는(critical) 모듈 Top 10은?
CQ8: 테스트 커버리지가 없는 public 함수 목록은?
CQ9: 특정 라이브러리를 사용하는 모든 리포는?
CQ10: 최근 30일간 가장 많이 변경된 모듈과 그 의존 모듈은?
```

각 역량 질문이 온톨로지의 클래스/관계로 표현 가능한지 검증한다.

---

## Part 3: 온톨로지 설계 패턴 (ODP)

### 콘텐츠 패턴 (Content ODP)

재사용 가능한 온톨로지 설계의 모듈식 조각:

**1. Part-Whole 패턴 (부분-전체)**

```
Repository --hasPart--> Module --hasPart--> Class --hasPart--> Method
```

- 코드의 계층 구조를 표현
- 전이성: Repository가 Method를 간접적으로 포함

**2. Classification 패턴 (분류)**

```
CodeEntity
├── ExecutableEntity (실행 가능)
│   ├── Function
│   ├── Method
│   └── Lambda
├── DeclarativeEntity (선언적)
│   ├── Class
│   ├── Interface
│   └── TypeAlias
└── ConfigEntity (설정)
    ├── EnvironmentVariable
    ├── ConfigFile
    └── Secret
```

**3. Participation 패턴 (참여)**

```
Function --participatesIn--> Process
(validate_token) --participatesIn--> (Authentication)
(encrypt_data) --participatesIn--> (DataProtection)
```

- 함수가 어떤 비즈니스 프로세스에 참여하는지 표현
- 순수 구조적 관계를 넘어 의미적 맥락 추가

**4. N-ary Relation 패턴 (N항 관계)**

이항 관계로 표현하기 어려운 복합 관계:

```
# "함수 A가 조건 C 하에서 함수 B를 호출한다"를 표현
CallEvent
  - caller: Function_A
  - callee: Function_B
  - condition: "if config.DEBUG"
  - frequency: "always" | "conditional"
  - line_number: 42
```

**5. Time-Indexed 패턴 (시간 인덱스)**

```
# "모듈 A가 시점 T에 모듈 B에 의존했다"
DependencyAtTime
  - source: Module_A
  - target: Module_B
  - valid_from: "2026-01-01"
  - valid_to: "2026-03-15"   # B에 대한 의존이 제거된 시점
```

- 코드 진화를 추적할 때 유용
- Git 이력과 연동하여 시간별 의존성 변화 분석

### 구조적 패턴 (Structural ODP)

**1. Modularity 패턴**

- 큰 온톨로지를 모듈로 분리
- 코드 온톨로지: 리포별 서브 온톨로지 + 리포 간 연결 온톨로지

```
code-ontology/
├── core.owl           # 공통 클래스/관계 정의
├── repo-auth.owl      # auth-service 리포 온톨로지
├── repo-payment.owl   # payment-service 리포 온톨로지
├── ...
└── cross-repo.owl     # 리포 간 의존성 온톨로지
```

**2. Normalization 패턴**

- 동일 개념의 중복 정의 방지
- 공유 어휘(shared vocabulary)를 core 모듈에 정의
- 각 리포 온톨로지는 core를 import

---

## Part 4: 온톨로지 언어 — OWL

### OWL 프로파일

| 프로파일 | 특징 | 추론 복잡도 | 코드 온톨로지 적합성 |
|---|---|---|---|
| **OWL 2 EL** | 교차, 존재 양화만 | PTIME | **가장 적합** — 빠른 추론, 충분한 표현력 |
| **OWL 2 QL** | DB 쿼리 최적화 | AC0 (데이터) | 대규모 인스턴스 쿼리 시 |
| **OWL 2 RL** | 규칙 기반 추론 | PTIME | 규칙 추론이 많을 때 |
| **OWL 2 DL** | 전체 표현력 | 2NEXPTIME | 과잉 — 코드 온톨로지에 불필요 |

### OWL로 코드 온톨로지 정의 (예시)

```xml
<!-- 클래스 정의 -->
<owl:Class rdf:about="#Module"/>
<owl:Class rdf:about="#Function"/>
<owl:Class rdf:about="#PythonModule">
  <rdfs:subClassOf rdf:resource="#Module"/>
</owl:Class>

<!-- 관계 정의 -->
<owl:ObjectProperty rdf:about="#imports">
  <rdfs:domain rdf:resource="#Module"/>
  <rdfs:range rdf:resource="#Module"/>
</owl:ObjectProperty>

<owl:ObjectProperty rdf:about="#calls">
  <rdfs:domain rdf:resource="#Function"/>
  <rdfs:range rdf:resource="#Function"/>
</owl:ObjectProperty>

<!-- 전이적 관계 -->
<owl:ObjectProperty rdf:about="#depends_on">
  <rdf:type rdf:resource="&owl;TransitiveProperty"/>
  <rdfs:domain rdf:resource="#Module"/>
  <rdfs:range rdf:resource="#Module"/>
</owl:ObjectProperty>

<!-- 제약 조건 -->
<owl:Class rdf:about="#Function">
  <rdfs:subClassOf>
    <owl:Restriction>
      <owl:onProperty rdf:resource="#belongs_to"/>
      <owl:qualifiedCardinality rdf:datatype="&xsd;nonNegativeInteger">1</owl:qualifiedCardinality>
      <owl:onClass rdf:resource="#Module"/>
    </owl:Restriction>
  </rdfs:subClassOf>
</owl:Class>
<!-- 모든 Function은 정확히 하나의 Module에 속한다 -->
```

### Property Graph vs OWL/RDF

| 항목 | OWL/RDF (트리플 스토어) | Property Graph (Neo4j) |
|---|---|---|
| 표현력 | 풍부 (추론, 제약) | 실용적 (속성 풍부) |
| 추론 | 내장 (분류, 일관성) | 없음 (쿼리로 구현) |
| 쿼리 | SPARQL | Cypher |
| 성능 | 추론 시 느림 | 쿼리 빠름 |
| 유연성 | 스키마 유연 | 스키마 유연 |
| 도구 생태계 | Protégé, Jena, RDFLib | Neo4j, Memgraph |

**코드 온톨로지 권장**: 설계 단계에서 OWL로 스키마를 정의하고 검증한 후, 운영은 **Property Graph(Neo4j)**로 한다. OWL의 추론 능력은 스키마 검증에만 사용하고, 실시간 쿼리는 Cypher로 수행한다.

---

## Part 5: 온톨로지 평가

### 평가 차원

| 차원 | 기준 | 검증 방법 |
|---|---|---|
| **정확성** | 개념/관계가 실세계를 올바르게 반영 | 도메인 전문가 리뷰 |
| **완전성** | 역량 질문에 모두 답할 수 있음 | CQ 기반 테스트 |
| **일관성** | 논리적 모순 없음 | 추론기(Reasoner)로 자동 검증 |
| **간결성** | 불필요한 중복 없음 | 중복 클래스/관계 탐지 |
| **확장성** | 새 개념 추가가 기존 구조를 깨지 않음 | 확장 시나리오 테스트 |
| **적응성** | 도메인 변화에 대응 가능 | 버전 관리, 모듈성 검토 |

### 코드 온톨로지 평가 체크리스트

```
[ ] 모든 역량 질문(CQ1~CQ10)에 답할 수 있는가?
[ ] 추론기로 일관성 검증을 통과하는가?
[ ] 40개 리포의 모든 엔터티가 온톨로지에 매핑되는가?
[ ] 리포 추가 시 스키마 변경 없이 확장 가능한가?
[ ] 언어(Python, JS, Java) 추가 시 스키마가 깨지지 않는가?
[ ] 쿼리 응답 시간이 실용적 범위 내인가?
[ ] CI/CD 파이프라인에서 자동 갱신이 정상 동작하는가?
```

---

## Part 6: 온톨로지 유지보수 & 진화

### 변경 유형

| 변경 | 설명 | 코드 온톨로지 상황 |
|---|---|---|
| **인스턴스 변경** | 개별 엔터티 추가/삭제/수정 | 함수 추가, 모듈 삭제 → AST 재파싱으로 자동 |
| **스키마 변경** | 클래스/관계 추가/수정 | 새 언어 지원, 새 관계 유형 추가 → 수동 설계 |
| **의미 변경** | 기존 개념의 의미 재정의 | "dependency"의 범위 변경 → 주의 필요 |

### 버전 관리 전략

```
v1.0: Module, Function, Class, imports, calls
v1.1: + ConfigValue, reads_config (설정 의존성 추가)
v1.2: + Repository, belongs_to (리포 단위 추적 추가)
v2.0: Function을 SyncFunction/AsyncFunction으로 분화 (breaking change)
```

- Minor 변경: 하위 호환 유지 (클래스/관계 추가)
- Major 변경: 하위 호환 깨짐 (기존 클래스 분화/병합)
- 마이그레이션 스크립트 자동화 권장

### 온톨로지 드리프트 방지

- 정기적 CQ 검증 (온톨로지가 여전히 역량 질문에 답하는지)
- 코드베이스 변화와 온톨로지 스키마의 정합성 모니터링
- 사용되지 않는 클래스/관계 정리 (온톨로지 부채)
