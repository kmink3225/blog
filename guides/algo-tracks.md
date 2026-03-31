---
name: algo-tracks
type: sub-skill
parent: algo-tutor
description: >
  알고리즘 튜터의 트랙 정의·전략·난이도 체계.
  AIE/DS 트랙별 학습 전략, Level 1~5 상세, 트랙 간 매핑을 포함한다.
---

# 알고리즘 트랙 및 난이도 체계

> `algo-tutor.md`에서 분리된 하위 가이드이다.
> 트랙 선택, 학습 전략, 난이도 정의를 담당한다.

---

## 트랙 선택

사용자 입력에서 트랙을 판별한다. 명시하지 않으면 질문한다.

| 트리거 | 트랙 |
|--------|------|
| "AI Engineer", "AIE", "엔지니어", "백엔드", "시스템" | AI Engineer 트랙 |
| "Data Scientist", "DS", "데이터 사이언티스트", "분석", "통계" | Data Scientist 트랙 |
| "둘 다", "공통" | 공통 문제 (양쪽에 해당하는 유형) |
| 미지정 | "AI Engineer와 Data Scientist 중 어느 트랙으로 진행할까?" 질문 |

---

## 전략 개요: DS vs AIE 코딩 테스트 현실

두 트랙은 코딩 테스트의 무게 중심이 근본적으로 다르다.

| 항목 | Data Scientist (DS) | AI Engineer (AIE) |
|------|---------------------|-------------------|
| 핵심 변별력 | **SQL** (Lv.4~5) | **알고리즘** (Lv.3~4) |
| 알고리즘 난이도 | Lv.2~3 (중급) | Lv.3~4 (상급) |
| SQL 중요도 | 매우 높음 | 보통 (Lv.3 수준) |
| 주요 평가 항목 | 통계적 논리, 데이터 가공 | 시스템 최적화, 구현 정교함 |
| 수학/이론 | 통계 검정, 확률론 | 선형대수, 미분, 최적화 |
| 전략 | SQL Lv.4~5 필수 정복 + 알고리즘 Lv.2 완벽 마스터 → Lv.3 빈출 유형 확장 | 알고리즘 Lv.3 완벽 마스터 → Lv.4 주요 유형 확장 |

### DS 학습 전략

```
[필수] SQL Lv.4~5 정복 (윈도우 함수, CTE, 누적 집계)
        ↓
[핵심] 알고리즘 Lv.2 완벽 마스터 (정렬, Hash, GroupBy)
        ↓
[확장] 알고리즘 Lv.3 빈출 유형 (DFS/BFS, 시뮬레이션, 확률)
        ↓
[Big Tech 대비] Lv.4~5 (DP, 대규모 데이터 패턴)
```

- DS 실무의 70% 이상이 데이터 추출·가공이므로 SQL이 최우선이다
- 알고리즘은 O(N log N) 이내 최적화 능력이면 충분하다
- 통계 공식을 코드로 번역하는 능력이 순수 알고리즘 기교보다 중요하다

### AIE 학습 전략

```
[핵심] 알고리즘 Lv.3 완벽 마스터 (DFS/BFS, Binary Search, Greedy)
        ↓
[변별력] 알고리즘 Lv.4 주요 유형 (DP, Tree, Heap)
        ↓
[FAANG 대비] Lv.5 (고급 Graph, Trie, Union-Find)
        ↓
[선택] 시스템 설계, 병렬 처리, NumPy 기반 low-level 구현
```

- 코드 효율성이 합불을 가른다 — O(N^2)는 정답이어도 리팩토링 대상
- Graph/Tree 구조 활용이 빈출 (신경망 연산 그래프 = 위상 정렬)
- 소프트웨어 공학적 완성도 (예외 처리, 테스트) 평가 비중이 DS보다 높다

---

## 난이도 체계

### AI Engineer 트랙 (AIE)

> ML/AI 시스템을 설계·구축하는 엔지니어 면접에 출제되는 알고리즘.
> 자료구조 구현력, 그래프/트리 활용, 시스템 설계 기반 문제 해결이 핵심이다.

| Level | 면접 우선순위 | 핵심 개념 | 자주 나오는 패턴 | 대표 자료구조 |
|-------|-------------|-----------|-----------------|--------------|
| 1 | 기초 체력 | Array, String, Hash 기초 | 중복 검사, 빈도 카운팅, 문자열 파싱 | list, dict, set |
| 2 | 기본기 | Stack/Queue, Two Pointer, Sliding Window | 괄호 매칭, 부분 배열, 구간 합 | deque, stack |
| 3 | **핵심 (필수)** | DFS/BFS, Binary Search, Greedy | 그래프 탐색, 정렬 배열 탐색, 최적 선택 | graph(dict), heap |
| 4 | **변별력** | Dynamic Programming, Tree, Heap | 최적 부분 구조, 트리 순회, Top-K | DP table, heapq, TreeNode |
| 5 | FAANG 대비 | 고급 Graph, Trie, Union-Find, 위상 정렬 | 최단 경로, 접두사 탐색, 사이클 검출, DAG 처리 | Trie, DisjointSet, PriorityQueue |

#### AIE Level 상세

**Level 1: 기초 자료구조 활용**
- Hash(dict/set)를 이용한 O(1) 조회
- 문자열 순회, 슬라이싱, 변환
- 리스트 기본 조작 (정렬, 필터, 변환)
- Counter, defaultdict 활용
- 핵심: "자료구조 선택이 곧 복잡도를 결정한다"

**Level 2: 선형 자료구조 응용**
- Stack: 괄호 검증, 모노톤 스택, 히스토그램 최대 직사각형
- Queue/Deque: BFS 기초, 슬라이딩 윈도우 최대값
- Two Pointer: 정렬 배열 합, 물 채우기(Container With Most Water)
- Sliding Window: 고정/가변 크기 윈도우, 최소 부분 배열
- 핵심: "포인터/윈도우 이동 조건을 정확히 설계한다"

**Level 3: 탐색과 최적화**
- DFS: 연결 요소, 백트래킹, 순열/조합 생성
- BFS: 최단 거리, 레벨 순회, 다차원 격자 탐색
- Binary Search: 정렬 배열 탐색, 매개변수 탐색(Parametric Search)
- Greedy: 활동 선택, 구간 스케줄링, 허프만 코딩
- 핵심: "탐색 공간을 줄이는 전략이 효율성을 결정한다"

**Level 4: 최적화와 트리**
- DP: 메모이제이션 vs 타뷸레이션, 배낭 문제, LCS, LIS
- Tree: 이진 트리 순회, BST 연산, LCA(최소 공통 조상)
- Heap: Top-K 문제, 중앙값 유지(두 개 힙), 작업 스케줄링
- 핵심: "상태 정의와 전이 관계를 정확히 설계한다"

**Level 5: 고급 알고리즘**
- Graph: Dijkstra, Bellman-Ford, Floyd-Warshall, 위상 정렬
- Trie: 자동완성, 문자열 집합 관리, XOR 최대화
- Union-Find: 연결 요소 관리, 사이클 검출, Kruskal MST
- 비트 마스킹: 부분집합 열거, 상태 압축 DP
- 핵심: "복합 자료구조를 조합하여 문제를 분해한다"

---

### Data Scientist 트랙 (DS)

> 데이터 분석·모델링을 수행하는 데이터 사이언티스트 면접에 출제되는 알고리즘.
> 데이터 조작 능력, 통계적 사고의 코드 구현, 효율적 데이터 처리가 핵심이다.

| Level | 면접 우선순위 | 핵심 개념 | 자주 나오는 패턴 | 대표 라이브러리 |
|-------|-------------|-----------|-----------------|----------------|
| 1 | 기초 체력 | List/Dict 조작, Counter, 기초 통계 | 빈도 분석, 평균/중앙값/최빈값, 데이터 정제 | collections, statistics |
| 2 | **핵심 (필수)** | Sorting, Ranking, GroupBy 구현, Hash | 커스텀 정렬, 순위 부여, 그룹별 집계, 중복 검사 | sorted, itertools.groupby |
| 3 | **변별력** | DFS/BFS, Simulation, 확률 계산 | 그래프 탐색, 몬테카를로, 조건부 확률, 통계 검정 구현 | itertools, random |
| 4 | Big Tech 대비 | Matrix 연산, DP(최적화), Sliding Window 통계 | 행렬 조작, 이동 평균, 편집 거리, 구간 최적화 | numpy-style 사고 |
| 5 | 차별화 | 근사 알고리즘, 샘플링, 대규모 데이터 패턴 | Reservoir Sampling, Bloom Filter, MapReduce 사고 | heapq, bisect |

#### DS Level 상세

**Level 1: 데이터 기초 조작**
- 리스트/딕셔너리로 데이터 정제 (결측치, 이상치 처리)
- Counter를 이용한 빈도 분석
- 기초 통계량 직접 구현 (평균, 분산, 중앙값, 사분위수)
- 문자열 파싱으로 로그/CSV 데이터 추출
- 핵심: "pandas 없이도 데이터를 다룰 수 있는 기초 체력"

**Level 2: 정렬, 그룹화, Hash** ★ DS 면접 핵심
- 커스텀 정렬: key 함수 설계, 다중 조건 정렬, 안정 정렬 활용
- Hash 활용: dict/set으로 빈도 카운팅, 중복 검사, Two Sum 패턴
- 순위 부여: 동점 처리(min/max/average rank), 백분위 계산
- 그룹별 집계: itertools.groupby, defaultdict로 GROUP BY 구현
- 데이터 변환: 피벗, 언피벗, 원-핫 인코딩 직접 구현
- 벡터 연산 사고: 반복문 대신 리스트 컴프리헨션, map/filter 활용
- 핵심: "Lv.2를 완벽히 마스터하는 것이 DS 코딩테스트의 80%이다"

**Level 3: 탐색, 시뮬레이션, 통계 구현** ★ DS 변별력
- DFS/BFS: 연결 요소 탐색, 그래프 기반 데이터 관계 분석
- 확률 계산: 조건부 확률, 베이즈 정리의 코드 구현
- 몬테카를로 시뮬레이션: 원주율 추정, A/B 테스트 시뮬레이션
- 통계 검정 직접 구현: t-test, chi-square, 부트스트랩 신뢰구간
- 손실 함수 구현: MSE, Cross-Entropy, 경사하강법 기초
- 핵심: "통계 공식을 코드로 번역하는 능력 — DS의 진짜 무기"

**Level 4: 행렬과 최적화**
- 행렬 연산: 전치, 회전, 나선형 순회, 희소 행렬 처리
- DP 기반 최적화: 편집 거리(문자열 유사도), 최적 구간 분할
- Sliding Window 통계: 이동 평균, 이동 표준편차, 변화 탐지
- 그래프 기반 데이터 분석: 네트워크 중심성, 커뮤니티 탐지 기초
- 핵심: "수학적 구조를 알고리즘으로 변환한다"

**Level 5: 대규모 데이터 알고리즘**
- Reservoir Sampling: 스트림 데이터에서 균일 샘플링
- Bloom Filter: 대용량 집합의 근사 멤버십 테스트
- Count-Min Sketch: 스트림 빈도 근사 추정
- 외부 정렬 / Merge-K: 메모리 초과 데이터 정렬
- Top-K 스트리밍: heapq로 실시간 Top-K 유지
- MapReduce 사고: 분할-처리-병합 패턴
- 핵심: "메모리 제약 하에서 근사적으로 정확한 답을 구한다"

---

## 트랙 간 공통 개념 매핑

일부 알고리즘은 양쪽 트랙에서 다르게 출제된다:

| 알고리즘 | AIE 관점 | DS 관점 |
|----------|----------|---------|
| Hash | 캐시 설계, 중복 제거 | 빈도 분석, Counter 활용 |
| Sorting | 병합 정렬 구현, 안정 정렬 | 커스텀 정렬, 순위 부여 |
| DFS/BFS | 그래프 연결 요소, 최단 경로 | 네트워크 분석, 커뮤니티 탐지 |
| DP | 배낭 문제, LCS/LIS | 편집 거리(문자열 유사도), 구간 최적화 |
| Sliding Window | 최대/최소 구간, 부분 배열 합 | 이동 평균, 변화 탐지 |
| Heap | 작업 스케줄러, 중앙값 유지 | Top-K, 스트리밍 집계 |
| Binary Search | 정렬 배열 탐색, 매개변수 탐색 | 백분위 계산, 이분 탐색 기반 통계 |

### 같은 Level, 다른 출제 의도

| Level | AIE 출제 의도 | DS 출제 의도 |
|-------|--------------|-------------|
| 2 | 자료구조 구현력 (Stack/Queue 직접 활용) | 데이터 조작 능력 (정렬/그룹화/Hash) |
| 3 | 탐색 최적화 (공간 축소, 가지치기) | 통계 로직의 코드화 (검정, 시뮬레이션) |
| 4 | 복잡한 상태 전이 설계 (DP, Tree) | 수학적 구조의 알고리즘 변환 (행렬, 최적화) |

### DS 면접에서 잘 안 나오는 유형

아래 유형은 AIE/SWE 전용으로, DS 트랙에서는 학습 우선순위가 낮다:

- Segment Tree / BIT (구간 쿼리)
- Trie (접두사 트리)
- Union-Find (분리 집합)
- 비트 마스킹
- 위상 정렬
- KMP / Rabin-Karp (문자열 매칭)
