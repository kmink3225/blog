---
name: sql-weakness
type: sub-skill
parent: sql-tutor
description: >
  사용자의 SQL 실수 패턴 추적 파일. 세션 시작 시 필수 로드.
  Active = 현재 약점, Resolved = 극복 완료. 세션 종료 후 agent가 업데이트한다.
last_updated: 2026-04-15 (6차)
---

# SQL 취약점 트래커

> 이 파일은 **모든 SQL 튜터링 세션 시작 시 필수 로드**한다.
> 세션 종료 후 아래 업데이트 프로토콜에 따라 agent가 직접 수정한다.

---

## Active 취약점

현재 반복 발생 중인 실수 패턴이다.

| 패턴 | 최근 발생 | 누적 횟수 | 비고 |
|------|---------|---------|------|
| 경계값 혼동 (`>` vs `>=`) | 2026-04-13 | 3 | "이후/이상" = `>=` 임을 매번 확인 필요. 2026-04-13 (Lv.2 SELECT 스칼라 서브쿼리): "평균 가격 이상"을 `>`로 작성, 힌트 후 수정 → 연속 카운트 리셋, 누적 3 |
| 문자열 따옴표 (큰따옴표 사용) | 2026-04-07 | 1 | MySQL은 허용하나 표준 SQL은 작은따옴표. 2026-04-07: IFNULL 문제 1차 통과 (연속 +1) |
| BETWEEN 문법 혼동 | 2026-04-07 | 2 | 컬럼명 누락(`BETWEEN 20000`), 비교연산자 혼용. 2026-04-07: 힌트 후 수정 → 연속 카운트 리셋 |
| LIKE 문법 혼동 | 2026-04-07 | 1 | 포함 검색에 `=` 또는 `IN` 먼저 시도 → `LIKE '%값%'` 필요. 2026-04-07: 1차 통과 (연속 +1) |
| GROUP BY 다중 컬럼 누락 | 2026-04-07 | 1 | `GROUP BY user_id`만 쓰고 `product_id` 누락 → 조합별 집계 시 모든 그룹 기준 컬럼 포함 필요. 힌트 후 수정 |
| JOIN 구조 오류 | 2026-04-15 | 3 | WHERE를 FROM/JOIN보다 앞에 위치, 컬럼 테이블 귀속 혼동, JOIN 대상 테이블 누락. 2026-04-15 (Lv.2 CASE+GROUP BY): `FROM product p WHERE ... INNER JOIN category c ON ...` — WHERE를 JOIN 앞에 삽입. 3차 힌트 후 수정, 누적 3. SQL 절 순서 `FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY` 반복 숙지 필요 |
| CASE WHEN END 누락 | 2026-04-07 | 1 | `END` 키워드 누락, grade를 독립 컬럼으로 나열 → `CASE WHEN ... END AS grade` 구조 필요. 힌트 후 수정 |
| COUNT 인자 예약어/컬럼명 오류 | 2026-04-08 | 1 | `COUNT(order)` — order는 SQL 예약어, 실제 컬럼명은 order_id. 힌트 후 수정 |
| SQL 키워드/식별자 오타 | 2026-04-15 | 7 | 2026-04-08~13 누적 4건. 2026-04-15 (Lv.2 CASE+GROUP BY 1문제 내 3건 연속): `categoy` → `category` (테이블명, 3차 힌트까지 잔존), `c.category` → `c.category_name` (컬럼명, 2차 힌트 지적에도 잔존), `FEILD` → `FIELD` (함수명). 1차 힌트에서 지적했는데도 다음 제출에서 그대로 남는 경향 — 힌트 읽은 후 **해당 오타 문자열을 직접 찾아 수정하는 점검 루틴** 필요. 제출 전 Ctrl+F로 지적된 오타 검색 권장. 누적 7 |
| SELECT 절 별칭 외부 참조 시도 | 2026-04-13 | 2 | SELECT 절에서 정의한 별칭(`AS avg_price`)을 같은 SELECT의 다른 컬럼·WHERE·HAVING에서 참조 시도. 별칭 스코프는 평가 순서상 ORDER BY에서만 안전. 외부 참조가 필요하면 인라인 뷰의 컬럼(`ca.cat_avg`)으로 만들 것. 2026-04-13 (Lv.2 인라인 뷰 문제 2번 시도 연속 발생). 누적 2 |
| WHERE vs HAVING 혼동 | 2026-04-13 | 1 | 행 단위 비교를 HAVING에 작성 → WHERE가 맞음. HAVING은 GROUP BY 후 집계 결과 필터 전용. 2026-04-13 (Lv.2 인라인 뷰 1차): `HAVING p.price > avg_price` 사용, 힌트 후 수정 |
| 행 단위 출력에 GROUP BY 부적절 사용 | 2026-04-13 | 1 | 각 행마다 한 줄을 출력해야 할 문제에 `GROUP BY category_name` 시도 → 그룹당 1행으로 축소되어 비집계 컬럼 결정 불능. 그룹 집계가 필요한 경우와 행 단위 부착(인라인 뷰/JOIN)이 필요한 경우를 구분할 것. 2026-04-13 (Lv.2 인라인 뷰 1차) |
| DBMS 방언 혼동 (Oracle vs MySQL) | 2026-04-13 | 1 | 2026-04-13 (Lv.2 NOT IN 1차): `SELECT UNIQUE(book_id)` 사용 — `UNIQUE`는 Oracle의 DISTINCT 동의어이나 MySQL은 인덱스 제약 키워드로만 인식 → syntax error. MySQL 기본 방언 학습 중이므로 Oracle/PostgreSQL 키워드 혼입 주의 (NVL, ROWNUM, MINUS 등도 동일 패턴 가능). 누적 1 |
| 패턴 과일반화 (NOT IN 방어 IN에 과적용) | 2026-04-13 | 1 | 2026-04-13 (Lv.2 IN 1차): NOT IN의 NULL 함정 방어 패턴(`IS NOT NULL`, `DISTINCT`)을 IN 문제에 그대로 적용. IN은 NULL-safe라 방어 불필요. 한 패턴을 학습했다고 무조건 다른 곳에 옮기지 말 것 — 각 연산자의 의미론을 정확히 이해하고 필요한 곳에만 적용. 누적 1 |
| CASE WHEN `THEN` 누락 | 2026-04-15 | 1 | 2026-04-15 (Lv.2 CASE+GROUP BY): `WHEN p.price >= 10000 and p.price < 50000 'MID'` — 조건과 값 사이 `THEN` 키워드 누락. SELECT와 GROUP BY에 같은 CASE를 반복할 때 양쪽 모두 동일 오류. 1차 힌트에서 지적했으나 다음 제출에서도 재발. CASE 문법은 `WHEN 조건 THEN 값` 고정 — `THEN` 없이는 파서가 다음 토큰을 조건으로 오해. 누적 1 |
| GROUP BY 에 `AS 별칭` 부여 시도 | 2026-04-15 | 1 | 2026-04-15 (Lv.2 CASE+GROUP BY): `GROUP BY c.category_name, CASE ... END AS price_range,` — GROUP BY는 "그룹화할 식"만 받으며 **별칭 부여 위치가 아니다**. `END`까지만 쓰고 잘라야 함. SELECT 별칭 규칙과 GROUP BY 규칙 구분 필요. 표준 SQL에서 GROUP BY는 SELECT 별칭 참조도 불가 (MySQL만 예외). 누적 1 |
| 절 사이 trailing comma | 2026-04-15 | 1 | 2026-04-15 (Lv.2): `GROUP BY ..., END, ORDER BY ...` — GROUP BY 마지막에 쉼표 남김. 다음 절로 넘어가기 전 마지막 항목 뒤 쉼표 제거 필수. 누적 1 |

---

## Resolved 취약점

3회 연속 미발생으로 극복 판정된 패턴이다. 이력 보존용으로 삭제하지 않는다.

| 패턴 | 해결 날짜 | 총 발생 횟수 | 비고 |
|------|---------|------------|------|
| WHERE 조건 누락 (필터 빠뜨리기) | 2026-04-06 | 3 | 5연속 미발생으로 극복. restaurant/category 등 범위 조건 누락 패턴 |
| ORDER BY 다중 정렬 문법 | 2026-04-13 | 2 | 2026-04-13 (Lv.2 서브쿼리 3문제 연속): 모든 시도에서 쉼표 구분 정확 사용 → 3연속 1차 통과로 극복 판정. `AND` 오용 패턴 재발 없음 |

---

## 업데이트 프로토콜

### 언제 업데이트하는가

- `/save` 트리거 또는 세션 종료 시
- 문제가 3개 이상 풀린 세션에서만 업데이트한다 (1~2문제 세션은 노이즈)

### 어떻게 업데이트하는가

**실수가 발생한 경우 (Active 업데이트):**

1. 해당 패턴이 이미 Active 테이블에 있으면 — `최근 발생` 날짜 갱신, `누적 횟수` +1
2. 없는 새 패턴이면 — Active 테이블에 행 추가
3. `last_updated` 날짜 갱신

**실수가 없었던 경우 (Resolved 이동 조건):**

- Active 패턴이 **3회 연속 1차 통과(힌트 없이 정답)**되면 Resolved로 이동
- Resolved 이동 시: Active에서 행 삭제 → Resolved 테이블에 추가 (`해결 날짜`, `총 발생 횟수` 기록)

### 판단 기준

| 상황 | 처리 |
|------|------|
| 힌트 없이 1차 정답 | 해당 패턴 연속 성공 카운트 +1 |
| 힌트 후 정답 또는 오답 | 연속 성공 카운트 리셋 |
| 새로운 실수 패턴 발견 | Active에 추가 |
| 3회 연속 1차 성공 | Resolved로 이동 |

---

## 출제 활용 가이드

Mode B 문제 생성 시 이 파일을 참고하여:

1. **Active 패턴을 문제의 함정(trap)으로 의도적으로 포함한다** — 사용자가 약점을 다시 마주쳐 교정 기회를 얻도록
2. **출제 주제 선정 시 Active 패턴과 관련된 유형을 우선 배치한다**
3. **힌트 제공 시 Active 패턴에 해당하면 더 구체적인 힌트를 제공한다**
