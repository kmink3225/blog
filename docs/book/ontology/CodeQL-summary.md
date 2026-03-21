# CodeQL — 코드를 데이터로 다루는 쿼리 엔진 Summary

> Source: https://codeql.github.com/docs/
> 핵심: 소스 코드를 관계형 데이터베이스로 변환하여 쿼리하는 정적 분석 도구
> 프로젝트 맥락: 코드 온톨로지 구축의 실무 레퍼런스. AST→관계형 데이터 변환, 코드 쿼리 패턴

---

## 핵심 개념: 코드를 데이터베이스로

CodeQL의 핵심 아이디어는 **소스 코드를 관계형 데이터베이스로 변환**하여, SQL과 유사한 쿼리 언어(QL)로 코드를 분석하는 것이다.

```
소스 코드 → [Extractor] → CodeQL Database → [QL Query] → 분석 결과
```

### 코드 온톨로지 프로젝트와의 관계

| CodeQL | 코드베이스 분석 프로젝트 |
|---|---|
| 코드 → 관계형 DB | 코드 → 지식 그래프 (Neo4j) |
| SQL-like 쿼리 (QL) | 그래프 쿼리 (Cypher) |
| 테이블 + 조인 | 노드 + 관계 |
| 보안 취약점 탐지에 최적화 | 의존성/영향도 분석에 최적화 |

CodeQL의 데이터 모델과 추출 방식은 코드 온톨로지의 **AST→그래프 파이프라인 설계에 직접 참고**할 수 있다.

---

## 분석 파이프라인

### Step 1: Database Creation (데이터베이스 생성)

**컴파일 언어 (Java, C/C++, C#, Go):**

- 빌드 프로세스를 모니터링하여 구문/의미 데이터 추출
- AST, 타입 정보, 심볼 해석 결과를 관계형 테이블로 변환

**인터프리터 언어 (Python, JavaScript, Ruby):**

- 빌드 없이 소스 코드에 직접 extractor 실행
- AST + 타입 추론 결과를 추출

**추출 결과물:**

- 관계형 데이터 (테이블)
- 소스 파일 참조 (위치 정보)
- 데이터베이스 스키마

### Step 2: Query Execution (쿼리 실행)

QL 언어로 작성된 쿼리를 데이터베이스에 실행한다.

### Step 3: Result Interpretation (결과 해석)

쿼리 결과를 소스 코드 위치에 매핑하여 의미 있는 분석 결과로 변환한다. 데이터 흐름/제어 흐름 경로를 포함하여 표시한다.

---

## 데이터 모델

### 데이터베이스 구조

CodeQL 데이터베이스는 코드를 관계형 테이블로 표현한다. 각 언어마다 고유한 스키마가 있다.

**Java 예시:**

| 테이블 | 설명 | 코드 온톨로지 대응 |
|---|---|---|
| `expressions` | 모든 식 (expression) | → Cypher의 Expression 노드 |
| `statements` | 모든 문 (statement) | → Cypher의 Statement 노드 |
| `methods` | 메서드 선언 | → Function 노드 |
| `classes` | 클래스 선언 | → Class 노드 |
| `imports` | import 문 | → IMPORTS 관계 |
| `calls` | 메서드 호출 | → CALLS 관계 |

### 추상화 계층

테이블 위에 객체지향 라이브러리가 추상화 계층을 제공한다:

```
관계형 테이블 (저수준)
    ↓
QL 클래스 (고수준 추상화)
    - Expr: 식
    - Stmt: 문
    - Method: 메서드
    - Class: 클래스
    - Call: 호출
```

---

## QL 쿼리 언어

### 기본 구조

```codeql
from <variable declarations>
where <conditions>
select <expressions>
```

### 핵심 문법 요소

#### Predicate (술어)

QL의 핵심 구성 요소. 논리적 관계를 정의한다.

**결과 없는 술어 (boolean 조건):**

```codeql
predicate isPublicMethod(Method m) {
  m.isPublic() and
  not m.isAbstract()
}
```

**결과 있는 술어 (값 반환):**

```codeql
Method getCallee(Method caller) {
  result = caller.getACallee()
}
```

**재귀 술어 (전이적 관계):**

```codeql
// 전이적 호출 관계: A가 B를 직접 또는 간접 호출하는가?
predicate transitivelyCallsMethod(Method source, Method target) {
  source.getACallee() = target
  or
  exists(Method mid |
    source.getACallee() = mid and
    transitivelyCallsMethod(mid, target)
  )
}
```

이것이 **코드 온톨로지의 전이적 의존성 추적**과 정확히 같은 패턴이다.

#### Type (타입)

| 타입 | 설명 |
|---|---|
| Primitive | `boolean`, `int`, `float`, `string`, `date` |
| Database | `@method`, `@class`, `@variable` (DB 스키마 의존) |
| User-defined | QL 클래스로 정의 |

#### Class (클래스)

```codeql
class PublicMethod extends Method {
  // 특성 술어: 이 클래스에 속하는 조건
  PublicMethod() {
    this.isPublic() and
    not this.isStatic()
  }

  // 멤버 술어
  int getParameterCount() {
    result = count(this.getAParameter())
  }
}
```

---

## 코드 분석 쿼리 패턴

### 의존성 분석

```codeql
// 모듈 간 import 관계 추출
from Import imp, CompilationUnit source, CompilationUnit target
where imp.getEnclosingCompilationUnit() = source and
      imp.getImportedType().getCompilationUnit() = target
select source.getName() as "source_module",
       target.getName() as "target_module"
```

### 호출 그래프

```codeql
// 함수 호출 관계
from MethodAccess call, Method caller, Method callee
where call.getEnclosingCallable() = caller and
      call.getMethod() = callee
select caller.getQualifiedName() as "caller",
       callee.getQualifiedName() as "callee",
       call.getLocation().getStartLine() as "line"
```

### 상속 관계

```codeql
// 클래스 상속 트리
from Class child, Class parent
where child.getASupertype() = parent
select child.getQualifiedName() as "child_class",
       parent.getQualifiedName() as "parent_class"
```

### 전이적 의존성 (N홉 추적)

```codeql
// A를 변경하면 영향받는 모든 메서드
from Method changed, Method affected
where transitivelyCallsMethod(affected, changed)
select affected.getQualifiedName() as "affected_method",
       affected.getFile().getRelativePath() as "file"
```

### 미사용 코드 탐지

```codeql
// 아무도 호출하지 않는 public 메서드
from Method m
where m.isPublic() and
      not exists(MethodAccess call | call.getMethod() = m) and
      not m.hasAnnotation("Override") and
      not m.getName() = "main"
select m.getQualifiedName() as "unused_method",
       m.getFile().getRelativePath() as "file"
```

---

## CodeQL vs 코드 온톨로지 (Neo4j) 비교

| 항목 | CodeQL | 코드 온톨로지 (Neo4j) |
|---|---|---|
| 데이터 모델 | 관계형 (테이블) | 그래프 (노드 + 관계) |
| 쿼리 언어 | QL (논리 프로그래밍) | Cypher (패턴 매칭) |
| 강점 | 데이터/제어 흐름 분석, 보안 | 의존성 경로 탐색, 영향도 |
| 멀티 리포 | 리포별 개별 DB | 전체를 하나의 그래프로 통합 |
| 전이적 탐색 | 재귀 술어 (복잡) | `*` 연산자 (간단) |
| 증분 업데이트 | DB 전체 재생성 필요 | 노드/관계 단위 증분 갱신 |
| 시각화 | 제한적 (SARIF) | 풍부 (Neo4j Browser, Bloom) |

### 하이브리드 활용

- **CodeQL**: AST/CFG/PDG 수준의 정밀 분석 (보안 취약점, 데이터 흐름)
- **Neo4j**: 리포 간 의존성, 영향도, 아키텍처 수준 분석
- **파이프라인**: CodeQL extractor로 추출 → 변환 → Neo4j에 적재

---

## 실무 도입 포인트

### CodeQL에서 배울 것 (코드 온톨로지 구축 시)

1. **Extractor 패턴**: 언어별 전용 파서로 AST + 타입 정보 + 심볼 해석을 추출
2. **스키마 설계**: 언어 공통 스키마 + 언어별 확장 스키마
3. **쿼리 라이브러리**: 자주 쓰는 분석 패턴을 재사용 가능한 라이브러리로
4. **SARIF 출력**: 분석 결과를 표준 형식으로 교환

### CodeQL의 한계 (코드 온톨로지가 보완하는 부분)

1. **리포 단위 분석**: 40개 리포를 하나로 통합 분석 불가 → Neo4j 필요
2. **증분 업데이트 불가**: 코드 변경 시 전체 DB 재생성 → Neo4j의 증분 갱신이 우위
3. **의존성 경로 탐색**: 재귀 술어가 Cypher `*`보다 복잡
4. **실시간 쿼리**: 대화형 분석보다 배치 분석에 최적화
