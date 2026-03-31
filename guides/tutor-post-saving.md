---
name: tutor-post-saving
type: sub-skill
parent: algo-tutor, sql-tutor
description: >
  코딩 테스트 튜터 공통 포스트 저장 규칙. 저장 트리거, 판단 기준, 묶음 기준,
  append 규칙, 저장 절차를 정의한다. algo-tutor와 sql-tutor 공유.
---

# 코딩 테스트 포스트 저장 규칙

> `algo-tutor.md`와 `sql-tutor.md`에서 공유하는 하위 가이드이다.
> Step 7 (포스트 저장) 실행 시 이 가이드를 따른다.

---

## 저장 트리거

- 사용자가 `/save` 또는 "저장해줘"라고 하면 즉시 저장한다
- 사용자가 별도 지시 없이 문제를 계속 풀면, 대화가 끝날 때 일괄 저장 여부를 묻는다

## 저장 판단 기준

| 상황 | 저장 여부 | 비고 |
|------|----------|------|
| 문제 풀이 완료 (정답) | O | 풀이 과정 + 모범 답안 |
| 문제 풀이 실패 (오답/포기) | O | 오답 과정 + 어디서 막혔는지 + 모범 답안. 오답 과정 자체가 학습 기록이다 |
| Mode B 연습 문제 | O | 실전 문제와 동일하게 저장 |
| 개념 질문만 (Flow C) | X | 문제 풀이가 없으면 포스트화하지 않는다 |

## 묶음 기준: 같은 유형 단위

- **같은 유형**의 문제를 하나의 포스트로 묶는다
- 유형이 다르면 별도 포스트로 분리한다

| 튜터 | 묶음 예시 | 파일명 예시 |
|------|----------|-----------|
| 알고리즘 | Hash 문제 3개 | `hash_level1-2_problems.qmd` |
| SQL | JOIN 문제 3개 | `join_level2-3_problems.qmd` |

## 기존 포스트가 있는 경우: append

- 같은 유형의 포스트가 이미 존재하면 **새 파일을 만들지 않고 기존 포스트에 추가(append)**한다
- 기존 포스트를 Read로 읽고, 마지막 문제 뒤에 새 문제를 이어붙인다
- YAML 헤더의 `date`는 최신 날짜로 업데이트한다
- `description`에 추가된 문제 제목을 반영한다

## 저장 절차

| 단계 | 알고리즘 | SQL |
|------|---------|-----|
| 1. 기존 포스트 확인 | `docs/blog/posts/Code_Test/algorithm/` | `docs/blog/posts/Code_Test/sql/` |
| 2. 있으면 | 기존 파일에 append (새 `##` 섹션) | 동일 |
| 3. 없으면 | 새 파일 생성 | 동일 |
| 4. 파일명 | `유형_난이도범위_problems.qmd` | 동일 |
| 5. GUIDE 준수 | Code_Test GUIDE.md 포스트 구조 | 동일 |
| 6. index 업데이트 | `Code_Test/index.qmd`에 링크 추가 (신규 시) | 동일 |

---

## 포스트 구조

### 알고리즘 YAML 헤더

```yaml
---
title: "알고리즘: Hash 문제 모음"
subtitle: "Hash — Level 1~2 (DS)"
description: |
  Hash 유형 알고리즘 문제 풀이 모음. 포켓몬, 완주하지 못한 선수 등.
categories:
  - Code Test
  - Algorithm Test
author: Kwangmin Kim
date: MM/DD/YYYY
---
```

### SQL YAML 헤더

```yaml
---
title: "SQL 코딩 테스트: JOIN 문제 모음"
subtitle: "JOIN — Level 2~3"
description: |
  JOIN 유형 SQL 문제 풀이 모음. 부서별 급여, 고객 주문 매칭 등.
categories:
  - Code Test
  - SQL
author: Kwangmin Kim
date: MM/DD/YYYY
---
```

### 본문 — 문제별 반복 구조

각 문제는 `##` 수준 헤더로 구분한다:

#### 알고리즘 문제 템플릿

```markdown
## 문제 1: 문제 제목

### 문제 정보

| 항목 | 내용 |
|---|---|
| 출처 | Programmers / LeetCode / 튜터 생성 |
| 난이도 | Level N |
| 트랙 | AIE / DS / 공통 |
| 유형 | Hash |

### 문제 설명
(요약 + 입출력 예시 + 제한사항)

### 풀이 과정
(사용자의 시도 과정 — 오답 포함, 브루트포스 → 최적화)

### 최종 풀이
(정답 코드 + 주석 + 복잡도 분석)

### 배운 점
(핵심 패턴, 함정, Python 팁)

### 면접 방어 포인트
- **복잡도 정밀 분석**: worst/average/best case 구분, 상수 계수 논의
- **대안 비교**: 왜 이 접근법을 택했는가 (trade-off 근거)
- **공학적 확장**: 프로덕션 제약 시 어떻게 변형하는가
```

#### SQL 문제 템플릿

```markdown
## 문제 1: 문제 제목

### 문제 정보

| 항목 | 내용 |
|---|---|
| 출처 | Programmers / 튜터 생성 |
| 난이도 | Level N |
| SQL 유형 | JOIN |

### 문제 설명
(테이블 스키마 + 기대 결과)

### 풀이 과정
(사용자의 시도 과정 — 오답 포함)

### 최종 풀이
(정답 쿼리 + 각 절 설명)

### 배운 점
(핵심 개념, 함정, 팁)

### 면접 방어 포인트
- **실행 계획 분석**: 이 쿼리의 실행 비용과 인덱스 활용 여부
- **대안 비교**: 서브쿼리/JOIN/CTE 중 왜 이 접근을 택했는가 (trade-off 근거)
- **공학적 확장**: 대용량 테이블, 방언 호환, 동시성 고려사항
```

### 말미 공통 섹션

```markdown
## 관련 문제
- 같은 유형 문제 링크
```
