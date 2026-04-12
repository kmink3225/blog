---
name: sql-topics
type: data
description: >
  SQL 튜터 Mode B 주제 목록. 레벨(1~5) × 그룹별 세부 토픽.
  tutoring_topic_picker.py --tutor sql 이 이 파일을 파싱한다.
  헤더 형식: ### 레벨 N - 그룹 M: 그룹명
  토픽 형식: | 토픽 설명 |
---

# SQL 튜터 토픽 목록

---

## 레벨 1 — SELECT · WHERE · 기본 집계

### 레벨 1 - 그룹 1: SELECT·WHERE

| topic |
|-------|
| BETWEEN 범위 조건 (날짜·숫자 범위 필터) |
| LIKE 패턴 검색 (전방/후방/포함 매칭) |
| IN · NOT IN 다중 값 필터 |
| 복합 AND·OR 조건 (3개 이상 조건 조합) |
| 부정 조건 (NOT · != · <>) |

### 레벨 1 - 그룹 2: ORDER BY·LIMIT

| topic |
|-------|
| 단일 컬럼 정렬 (ASC · DESC) |
| 다중 컬럼 정렬 (1차·2차 기준) |
| LIMIT으로 상위 N개 추출 |
| OFFSET 기반 페이지네이션 |
| DESC + LIMIT 조합 (최근 N개·최고 N개) |

### 레벨 1 - 그룹 3: DISTINCT·NULL처리

| topic |
|-------|
| SELECT DISTINCT 중복 제거 |
| IS NULL · IS NOT NULL 조건 필터 |
| COALESCE · IFNULL 기초 대체값 |
| COUNT(*) vs COUNT(col) NULL 차이 |
| NULL 포함 정렬 동작 (NULL은 최솟값 또는 최댓값) |

### 레벨 1 - 그룹 4: 기본 집계

| topic |
|-------|
| COUNT + WHERE 조건 집계 |
| SUM · AVG 집계 + ROUND 반올림 |
| MAX · MIN 단순 조회 |
| 여러 집계 함수 혼합 (COUNT + SUM + AVG) |
| GROUP BY 없이 전체 집계 |

### 레벨 1 - 그룹 5: 혼합 (Lv.1 복합)

| topic |
|-------|
| WHERE + ORDER BY + LIMIT 3단 조합 |
| DISTINCT + 집계 혼합 |
| 조건 필터 + 정렬 + NULL처리 통합 |
| 다중 조건 + 집계 + 정렬 |
| 날짜 조건 + 집계 + ORDER BY |

---

## 레벨 2 — JOIN · GROUP BY · CASE WHEN

### 레벨 2 - 그룹 1: INNER JOIN

| topic |
|-------|
| 2테이블 INNER JOIN 기본 |
| JOIN + WHERE 조건 필터 |
| JOIN + 집계 (COUNT · SUM) |
| JOIN + ORDER BY 정렬 |
| 자기 조인 (Self Join) |

### 레벨 2 - 그룹 2: LEFT·RIGHT JOIN

| topic |
|-------|
| LEFT JOIN + NULL 체크 (매칭 없는 행 탐지) |
| RIGHT JOIN 활용 |
| LEFT JOIN + WHERE IS NULL (차집합 패턴) |
| 외부 조인 + 집계 (매칭 없는 행 포함 COUNT) |
| 다중 LEFT JOIN 연결 (3테이블) |

### 레벨 2 - 그룹 3: GROUP BY·HAVING

| topic |
|-------|
| GROUP BY + COUNT 단순 집계 |
| GROUP BY + HAVING 집계 후 필터 |
| 다중 컬럼 GROUP BY (조합별 집계) |
| HAVING vs WHERE 판별 (집계 전/후 필터링) |
| GROUP BY + 집계 + ORDER BY 조합 |

### 레벨 2 - 그룹 4: CASE WHEN

| topic |
|-------|
| 단순 CASE WHEN THEN END 값 분기 |
| 조건부 집계 SUM(CASE WHEN ... END) |
| CASE WHEN + GROUP BY 조합 |
| 다중 분기 CASE WHEN (3개 이상 조건) |
| CASE WHEN으로 NULL 대체 처리 |

### 레벨 2 - 그룹 5: 기본 서브쿼리

| topic |
|-------|
| IN + 서브쿼리 (하위 집합 필터) |
| WHERE + 스칼라 서브쿼리 (MAX · MIN 참조) |
| FROM + 인라인 뷰 (서브쿼리를 테이블로) |
| NOT IN + 서브쿼리 (제외 패턴) |
| SELECT 절 스칼라 서브쿼리 |

---

## 레벨 3 — 다중 JOIN · 날짜 함수 · UNION

### 레벨 3 - 그룹 1: 다중 JOIN

| topic |
|-------|
| 3테이블 연속 JOIN |
| JOIN + 서브쿼리 혼합 |
| 자기 참조 조인 (계층 1단계) |
| 다중 JOIN + GROUP BY 집계 |
| JOIN + CASE WHEN + GROUP BY 복합 |

### 레벨 3 - 그룹 2: 상관 서브쿼리·EXISTS

| topic |
|-------|
| EXISTS 존재 여부 검사 |
| NOT EXISTS 비존재 패턴 |
| 상관 서브쿼리 + 집계 비교 (행별 최대값) |
| IN vs EXISTS 동치 변환 |
| 상관 서브쿼리 + GROUP BY 조합 |

### 레벨 3 - 그룹 3: 날짜 함수

| topic |
|-------|
| DATE_FORMAT 날짜 포맷 변환 |
| DATEDIFF · TIMESTAMPDIFF 기간 계산 |
| DATE_ADD · DATE_SUB 날짜 연산 |
| YEAR · MONTH · DAY 단위 추출 |
| 날짜 범위 + 함수 조합 (월별·연도별 집계) |

### 레벨 3 - 그룹 4: UNION·UNION ALL

| topic |
|-------|
| UNION 중복 제거 결합 |
| UNION ALL 전체 결합 (중복 포함) |
| UNION + ORDER BY 최종 정렬 |
| 두 쿼리 결과 비교 (UNION 구조로 합집합) |
| UNION + GROUP BY 재집계 |

### 레벨 3 - 그룹 5: COALESCE·NULL심화

| topic |
|-------|
| COALESCE 다단계 대체값 |
| NULL + 집계 함정 (SUM(NULL) = NULL vs COUNT 0) |
| NULLIF 활용 (0 나누기 방지) |
| NULL + CASE WHEN 조합 |
| NULL + JOIN 혼합 패턴 (LEFT JOIN + NULL 처리) |

---

## 레벨 4 — Window Function · CTE

### 레벨 4 - 그룹 1: ROW_NUMBER·RANK·DENSE_RANK

| topic |
|-------|
| ROW_NUMBER 고유 순번 부여 |
| RANK vs DENSE_RANK 동점 처리 비교 |
| PARTITION BY + RANK (그룹별 순위) |
| 순위 기반 필터링 (CTE + WHERE rank = 1 패턴) |
| 복합 ORDER BY + 순위 (다중 기준 정렬 + RANK) |

### 레벨 4 - 그룹 2: LAG·LEAD

| topic |
|-------|
| LAG 이전 행 값 참조 |
| LEAD 다음 행 값 참조 |
| LAG + 차이 계산 (증가율·변화량) |
| LEAD + 조건 비교 (다음 이벤트 판별) |
| LAG · LEAD + PARTITION BY 그룹 내 비교 |

### 레벨 4 - 그룹 3: CTE

| topic |
|-------|
| 단순 CTE (가독성 개선) |
| 다단계 CTE (중간 결과 참조) |
| CTE + JOIN 조합 |
| CTE + 집계 후 필터 (HAVING 대체) |
| CTE vs 서브쿼리 동치 변환 비교 |

### 레벨 4 - 그룹 4: PARTITION BY + 집계

| topic |
|-------|
| 파티션별 누적합 SUM OVER (PARTITION BY) |
| 파티션별 이동평균 AVG OVER |
| 파티션별 최대·최소 MAX · MIN OVER |
| 윈도우 집계 vs GROUP BY 결과 비교 |
| COUNT OVER로 그룹 크기 참조 |

---

## 레벨 5 — 재귀 CTE · Island & Gaps · PIVOT

### 레벨 5 - 그룹 1: 재귀 CTE

| topic |
|-------|
| 계층 구조 탐색 (조직도·카테고리 트리) |
| 경로 추적 (루트→리프 전체 경로 문자열 구성) |
| 깊이 제한 재귀 (최대 레벨 N까지) |
| 재귀 + 집계 (레벨별 누적합) |
| 재귀 종료 조건 설계 (사이클 방지) |

### 레벨 5 - 그룹 2: ROWS·RANGE BETWEEN

| topic |
|-------|
| 이동평균 (ROWS BETWEEN N PRECEDING AND CURRENT ROW) |
| 누적합 (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) |
| RANGE vs ROWS 차이 (동점 행 포함 범위) |
| 슬라이딩 윈도우 최대·최소 |
| 복합 프레임 + PARTITION BY 조합 |

### 레벨 5 - 그룹 3: Island & Gaps

| topic |
|-------|
| 연속 날짜 구간 감지 (날짜 - ROW_NUMBER 패턴) |
| 갭(단절) 구간 찾기 |
| 연속 이벤트 카운팅 (연속 로그인 일수 등) |
| 섬(island) 시작·끝 날짜 추출 |
| 연속 행 그룹화 패턴 (같은 값 연속 묶기) |

### 레벨 5 - 그룹 4: 누적 집계

| topic |
|-------|
| Running Total (행별 누적합) |
| 누적 최대·최솟값 |
| PERCENT_RANK · CUME_DIST 백분위 |
| 이동합 vs 누적합 비교 |
| 기간 리셋 누적 집계 (월별 리셋) |

### 레벨 5 - 그룹 5: PIVOT·UNPIVOT

| topic |
|-------|
| 조건부 집계 PIVOT (SUM(CASE WHEN col = '값' THEN ...)) |
| 동적 PIVOT 개념 (컬럼 수가 데이터 의존적) |
| UNPIVOT 행열 역전환 |
| PIVOT + JOIN 조합 |
| 다중 집계 PIVOT (SUM + COUNT 동시) |
