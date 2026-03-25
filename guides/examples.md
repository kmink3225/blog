---
name: examples
description: >
  AGENT_GUIDE.md의 End-to-End 실행 흐름 예시.
  정상 흐름(Happy Path)과 예외 흐름(Stop-and-Ask 발동) 2가지를 포함.
type: skill-reference
---

# End-to-End 예시

## 정상 흐름 (Happy Path)

> 사용자가 "Bayesian Optimization에 대한 블로그 포스트 작성해줘"라고 요청했을 때의 실행 흐름 예시.

```
1. [info-search] guides/info-search.md 로드 → 병렬 탐색 실행
   - 블로그 검색: docs/blog/posts/ 에서 "Bayesian Optimization" 관련 기존 포스트 확인
   - 교재 검색: docs/book/ 에서 관련 챕터 확인
   - 결과: 기존 포스트 없음, 교재 Ch.12에 관련 내용 존재

2. [카테고리 결정] Machine_Learning 카테고리로 판단
   → docs/blog/posts/Machine_Learning/GUIDE.md 로드

3. [write-post] guides/write-post.md 로드 → Step 1~6 실행
   - Step 1: YAML 헤더 작성 (date: 03/25/2026)
   - Step 2: 교재 Ch.12 읽기 → 한다 체로 재작성
   - Step 3: 콘텐츠 작성 (주장→근거→해석 구조)
   - Step 4: 수식 표기 점검 ($\theta$ 공백 확인)
   - Step 5: index.qmd에 링크 추가 (패턴 D 확인 후 동일 형식)
   - Step 6: 셀프 체크리스트 실행 → 위반 없음

4. [보고] 작업 완료 보고 형식에 맞춰 결과 전달
```

## 예외 흐름 예시 (Stop-and-Ask 발동)

> 사용자가 "A/B 테스트의 검정력 분석 포스트 써줘"라고 요청했을 때, Stop-and-Ask가 발동하는 흐름.

```
1. [info-search] guides/info-search.md 로드 → 병렬 탐색 실행
   - 블로그 검색: "검정력 분석" 관련 기존 포스트 확인
   - 결과: Statistics/에 "검정력(Power)" 포스트 존재, Experimentation/에 "A/B Test 설계" 포스트 존재

2. [카테고리 결정] ⚠️ Stop-and-Ask 발동 — 카테고리 분류 모호
   → "검정력 분석"은 Statistics(통계 이론)와 Experimentation(A/B Test 실무) 양쪽에 해당
   → 에이전트가 사용자에게 확인:
     "이 포스트는 두 카테고리에 동등하게 해당합니다.
      (1) Statistics/ — 검정력의 수학적 정의와 계산 중심
      (2) Experimentation/ — A/B 테스트 설계 시 검정력 활용 중심
      어느 카테고리에 배치할까요? (다른 쪽에 크로스 링크를 추가합니다)"

3. [사용자 응답] "Experimentation으로 해줘"

4. [재개] Experimentation/GUIDE.md 로드
   → guides/write-post.md 로드 → Step 1~6 실행

5. [write-post 진행 중] Step 5: index.qmd 업데이트
   → Experimentation/index.qmd 읽기 → 패턴 D (구조화된 학습 경로)
   → ⚠️ 기존 항목 중 "검정력 분석"이 placeholder로 이미 존재 (date: 1111-11-11)
   → placeholder를 실제 링크로 교체하고 날짜를 업데이트
   → Statistics/index.qmd에도 크로스 링크 추가

6. [보고] 작업 완료 보고 형식에 맞춰 결과 전달
   - 주요 판단: "카테고리를 사용자 확인 후 Experimentation으로 결정.
     Statistics/index.qmd에 크로스 링크 추가함"
```
