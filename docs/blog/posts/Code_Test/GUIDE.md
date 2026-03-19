---
name: Code_Test_GUIDE
type: category
version: 1.0
description: Code Test 카테고리 포스트 작성 규칙 — 문제-풀이 쌍, 알고리즘/SQL 유형별 분류
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

### 4. 풀이 접근법 (직관적 설명)

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

```
Hash           — dict/set 활용, 중복 검사, 카운팅
Stack/Queue    — 괄호 매칭, BFS, 우선순위 큐
Sorting        — 정렬 기반 문제, 그리디
DFS/BFS        — 그래프 탐색, 연결 요소
Dynamic Programming — 최적 부분 구조, 메모이제이션
Greedy         — 탐욕 알고리즘
Binary Search  — 이진 탐색, 매개변수 탐색
Graph          — 최단 경로, 위상 정렬
```

---

## SQL 문제 (sql/ — 계획 중)

- SELECT, JOIN, GROUP BY, 윈도우 함수 등 유형별로 구성할 예정이다
- 실행 결과 테이블을 포함한다
