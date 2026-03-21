---
name: Code_Test_GUIDE
type: category
version: 1.0
description: "LOAD when writing posts about algorithm problem solving or SQL challenges. Covers problem-solution pairs with complexity analysis, organized by algorithm type and difficulty."
scope: docs/blog/posts/Code_Test/
parent: AGENT_GUIDE.md
index: docs/blog/posts/Code_Test/index.qmd
book_sources: []
cross_references:
  - docs/blog/posts/Engineering/GUIDE.md
---

# Code Test 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Code Test 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **문제-풀이 쌍(Problem-Solution Pair)**: 코딩 테스트 문제 풀이가 핵심이다
- **알고리즘 유형별 분류**: Hash, Stack/Queue, Sorting, Graph 등 유형별로 구성한다
- **실행 가능한 코드**: 코드가 즉시 실행 가능해야 한다
- **하위 폴더**: `algorithm/` (알고리즘 문제), `sql/` (SQL 문제, 계획 중)
- **파일명 패턴**: `유형_난이도_문제명.qmd` (예: `hash_level1_pocketmon.qmd`)

---

## 포스트 콘텐츠 구조

Code Test 카테고리는 다른 카테고리와 다른 고유 구조를 따른다.

### 1. 문제 정보

포스트 상단에 문제 메타정보를 테이블로 제시한다:

```markdown
| 항목 | 내용 |
|---|---|
| 출처 | Programmers / LeetCode / 백준 |
| 제목 | 문제 제목 |
| 난이도 | Level 1 / Level 2 / Level 3 |
| 유형 | Hash / Stack / DFS/BFS / DP 등 |
| 풀이 시간 | 실제 소요 시간 |
| 링크 | [문제 링크](URL) |
```

### 2. 문제 설명

- 문제 내용을 요약한다 (저작권 문제로 전문 복사 대신 요약)
- 입출력 예시를 테이블로 정리한다
- 제한사항을 명시한다

### 3. 핵심 알고리즘/자료구조 (정의 + 원리)

- 이 문제를 풀기 위해 필요한 알고리즘/자료구조를 설명한다
- 시간/공간 복잡도를 분석한다

```markdown
::: {.callout-tip}
## 핵심: Hash Table

Hash Table은 key-value 쌍을 저장하며, 평균 $O(1)$ 시간에 조회/삽입/삭제가 가능하다.
Python의 `dict`와 `set`이 Hash Table 기반이다.

- 조회: $O(1)$ 평균, $O(n)$ 최악
- 삽입: $O(1)$ 평균
- 이 문제에서의 역할: 중복 검사를 $O(n)$에 수행
:::
```

### 4. 풀이 접근법 (Approach)

- 문제를 어떻게 분석했는지 사고 과정을 서술한다
- 브루트포스 → 최적화 순서로 접근을 발전시킨다
- 왜 이 자료구조/알고리즘을 선택했는지 설명한다

### 5. 코드 풀이

- Python 코드로 구현한다
- 핵심 로직에 주석을 단다
- 복잡도 분석을 코드 아래에 명시한다

```markdown
```python
def solution(nums):
    """
    포켓몬 종류의 최대 수를 반환한다.
    N/2마리를 선택할 때 가능한 최대 종류 수 = min(고유 종류 수, N/2)
    """
    unique_count = len(set(nums))      # O(n): 고유 종류 수
    max_pick = len(nums) // 2          # 선택 가능한 수
    return min(unique_count, max_pick)  # 둘 중 작은 값
```

- **시간 복잡도**: $O(n)$ — set 생성
- **공간 복잡도**: $O(n)$ — set 저장
```

### 6. 다른 풀이 / 개선 (Optional)

- 대안 풀이가 있으면 비교한다
- 시간/공간 복잡도 trade-off를 분석한다

### 7. 관련 문제 (Related Problems)

- 같은 유형의 다른 문제를 링크한다
- 난이도를 명시한다
- **파일이 아직 존재하지 않더라도 논리적으로 관련된 문제 유형은 placeholder 링크로 포함한다.** 이를 통해 향후 풀어야 할 문제 유형을 체계적으로 파악할 수 있다.

```markdown
## 관련 문제

- [완주하지 못한 선수 (Hash Level 1)](./hash_level1_runner.qmd)
- [전화번호 목록 (Hash Level 2)](./hash_level2_phone_number.qmd)
```

---

## 알고리즘 유형 분류

| 유형 | 핵심 개념 | 대표 패턴 |
|------|-----------|-----------|
| Hash | dict/set 활용 | 중복 검사, 카운팅, Two Sum |
| Stack/Queue | LIFO/FIFO, 우선순위 큐 | 괄호 매칭, 모노톤 스택, BFS 큐 |
| Sorting | 정렬 기반 풀이 | 병합 정렬 응용, 커스텀 정렬 |
| DFS/BFS | 그래프/트리 탐색 | 연결 요소, 최단 거리, 레벨 순회 |
| Dynamic Programming | 최적 부분 구조, 중복 부분 문제 | 메모이제이션, 바텀업 테이블 |
| Greedy | 지역 최적 → 전역 최적 | 활동 선택, 구간 스케줄링 |
| Binary Search | 정렬된 탐색 공간 | 이진 탐색, 매개변수 탐색 (parametric search) |
| Graph | 그래프 알고리즘 | 최단 경로(Dijkstra, Floyd), 위상 정렬, MST |
| Backtracking | 탐색 + 가지치기 | N-Queen, 순열/조합 생성, 스도쿠 |
| String | 문자열 처리 | KMP, Rabin-Karp, 팰린드롬, 정규식 |
| Trie | 접두사 트리 | 자동완성, 사전 검색, 문자열 집합 |
| Bit Manipulation | 비트 연산 | XOR 활용, 비트 마스킹, 부분집합 |
| Union-Find | 분리 집합 (Disjoint Set) | 연결 요소 판별, 사이클 검출, 크루스칼 MST |
| Sliding Window | 구간 이동 | 부분 배열 합, 최대/최소 윈도우 |
| Two Pointer | 양 끝/동방향 포인터 | 정렬 배열 합, 부분 수열 |
| Heap | 힙 기반 우선순위 처리 | Top-K, 중앙값 유지, 작업 스케줄링 |
| Segment Tree / BIT | 구간 쿼리 | 구간 합, 구간 최솟값, 업데이트 |

---

## SQL 문제 (sql/)

### 유형 분류

| 유형 | 핵심 개념 | 대표 패턴 |
|------|-----------|-----------|
| SELECT/WHERE | 필터링, 조건 검색 | 조건 조합, LIKE, IN, BETWEEN |
| JOIN | 테이블 결합 | INNER/LEFT/RIGHT/CROSS JOIN, 자기 결합 |
| GROUP BY / HAVING | 집계, 그룹 필터 | COUNT, SUM, AVG + HAVING 조건 |
| Window Function | 윈도우 함수 | ROW_NUMBER, RANK, LAG/LEAD, 누적합 |
| Subquery / CTE | 서브쿼리, 공통 테이블 표현식 | 상관 서브쿼리, WITH 절, 재귀 CTE |
| String / Date | 문자열·날짜 처리 | CONCAT, SUBSTRING, DATE_DIFF, FORMAT |

### SQL 포스트 구조

SQL 문제는 알고리즘과 다른 구조를 따른다:

1. **문제 정보** — 출처, 난이도, SQL 유형
2. **문제 설명** — 테이블 스키마 + 기대 결과 테이블
3. **핵심 SQL 개념** — 사용하는 SQL 기능 설명
4. **풀이 접근법** — 쿼리 설계 사고 과정
5. **SQL 풀이** — 실행 가능한 쿼리 + 결과 테이블
6. **다른 풀이** — 대안 쿼리, 성능 비교
7. **관련 문제** — 같은 SQL 유형 문제 링크

### SQL 파일명 패턴

`유형_난이도_문제명.qmd` (예: `join_level2_department_salary.qmd`)

---

## 참고 소스

이 카테고리는 교재(book)가 아닌 **코딩 플랫폼과 알고리즘 레퍼런스**가 primary source이다.

| 소스 | 역할 |
|------|------|
| Programmers (programmers.co.kr) | 한국어 코딩 테스트 문제 |
| LeetCode (leetcode.com) | 글로벌 알고리즘 문제, 난이도 체계 |
| 백준 (acmicpc.net) | 알고리즘 문제, 경시대회 스타일 |
| HackerRank (hackerrank.com) | SQL 문제 포함 |

**활용 원칙**: 문제 출처를 명시하고, 저작권 문제로 문제 전문을 복사하지 않고 요약한다. agent의 사전지식으로 알고리즘 원리와 복잡도 분석을 보충한다.

---

## 자주 발생하는 실수 패턴

<fix-solution-without-approach>

```
# WRONG: 정답 코드만 제시
def solution(nums):
    return min(len(set(nums)), len(nums) // 2)

# CORRECT: 브루트포스 → 최적화 사고 과정 → 최종 코드
# 접근 1 (브루트포스): 모든 조합을 시도 → O(2^n) → 비효율
# 접근 2 (관찰): 고유 종류 수와 N/2 중 작은 값이 답 → O(n)
def solution(nums):
    unique_count = len(set(nums))      # O(n): 고유 종류 수
    max_pick = len(nums) // 2          # 선택 가능한 수
    return min(unique_count, max_pick)  # 둘 중 작은 값
```

</fix-solution-without-approach>

<fix-missing-complexity>

```
# WRONG: 코드만 제시하고 복잡도 분석 없음

# CORRECT: 코드 아래에 반드시 복잡도 명시
# - 시간 복잡도: O(n) — set 생성
# - 공간 복잡도: O(n) — set 저장
```

</fix-missing-complexity>

---

<boundaries>

### 할 수 있는 것

- 문제 요약 (저작권 준수, 전문 복사 금지)
- 알고리즘/자료구조 원리 설명
- Python 코드 풀이 + 주석
- 시간/공간 복잡도 분석
- 브루트포스 → 최적화 사고 과정

### 할 수 없는 것

- 문제 전문 복사 (저작권 위반)
- 복잡도 분석 없는 풀이 제시
- 사고 과정 없이 정답 코드만 나열
- 테스트 없는 코드

</boundaries>
