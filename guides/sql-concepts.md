---
name: sql-concepts
type: sub-skill
parent: sql-tutor
description: >
  SQL 코딩 테스트 난이도별 개념 레퍼런스. Level 1~5 핵심 개념과 패턴 정리.
  sql-tutor가 설명·출제 시 참조한다.
---

# SQL 개념 레퍼런스 (난이도별)

> `sql-tutor.md`에서 분리된 하위 가이드이다.
> 튜터가 설명·출제 시 참조하는 핵심 개념 체계이다.

---

## Level 1: 기본 조회

| 개념 | 핵심 | 자주 나오는 패턴 |
|------|------|-----------------|
| SELECT / FROM | 컬럼 선택, 테이블 지정 | 전체 조회, 특정 컬럼 조회 |
| WHERE | 행 필터링 | 비교 연산, IN, BETWEEN, LIKE, IS NULL |
| ORDER BY | 정렬 | ASC/DESC, 다중 컬럼 정렬 |
| LIMIT / TOP | 결과 제한 | 상위 N건 조회 |
| DISTINCT | 중복 제거 | 고유값 조회 |
| 기본 집계 | COUNT, SUM, AVG, MAX, MIN | 단일 테이블 집계 |

## Level 2: 결합과 그룹화

| 개념 | 핵심 | 자주 나오는 패턴 |
|------|------|-----------------|
| INNER JOIN | 교집합 결합 | 두 테이블 매칭 |
| LEFT/RIGHT JOIN | 한쪽 전체 유지 | NULL 포함 결과 |
| GROUP BY | 그룹별 집계 | 카테고리별 합계/평균 |
| HAVING | 그룹 필터 | 집계 결과 조건 |
| CASE WHEN | 조건 분기 | 값 변환, 조건별 컬럼 생성 |
| 기본 서브쿼리 | WHERE 절 서브쿼리 | IN (SELECT ...) |

## Level 3: 복합 쿼리

| 개념 | 핵심 | 자주 나오는 패턴 |
|------|------|-----------------|
| 다중 JOIN | 3개 이상 테이블 결합 | 연쇄 JOIN |
| 상관 서브쿼리 | 외부 쿼리 참조, 행별 실행 | EXISTS, NOT EXISTS, 행별 비교 |
| 날짜 함수 | DATE_FORMAT, DATEDIFF | 기간 계산, 날짜 추출 |
| UNION / UNION ALL | 결과 결합 | 여러 쿼리 합치기 |
| COALESCE / IFNULL | NULL 처리 | 기본값 대체 |
| 복합 CASE | 집계 함수 내 CASE | 조건부 집계, 피벗 유사 |

## Level 4: 윈도우 함수와 CTE

| 개념 | 핵심 | 자주 나오는 패턴 |
|------|------|-----------------|
| ROW_NUMBER | 행 번호 부여 | 그룹 내 순위, Top-N |
| RANK / DENSE_RANK | 순위 (동점 처리) | 랭킹 문제 |
| LAG / LEAD | 이전/다음 행 참조 | 연속 비교, 변화율 |
| SUM() OVER | 누적합 / 이동합 | 런닝 토탈, 구간 합계 |
| CTE (WITH) | 공통 테이블 표현식 | 복잡 쿼리 분해 |
| PARTITION BY | 윈도우 분할 | 그룹별 윈도우 연산 |

## Level 5: 고급 패턴

| 개념 | 핵심 | 자주 나오는 패턴 |
|------|------|-----------------|
| 재귀 CTE | WITH RECURSIVE | 계층 구조, 경로 탐색, 연속 날짜 생성 |
| Island & Gaps | 연속 구간 탐지 | 연속 방문일, 연속 매출 구간, 결측 탐지 |
| 누적 집계 | SUM/COUNT() OVER + ORDER BY | 런닝 토탈, 누적 비율, 구간별 누적합 |
| 이동 평균 | ROWS/RANGE BETWEEN | N일 이동 평균, 슬라이딩 윈도우 분석 |
| PIVOT / UNPIVOT | 행-열 변환 | 크로스탭 보고서, 동적 컬럼 |
| 순위 기반 필터링 | 복합 윈도우 + CTE 결합 | 그룹 내 Top-N, 조건부 순위 |
