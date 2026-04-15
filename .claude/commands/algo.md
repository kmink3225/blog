---
description: Python 알고리즘 튜터 — AIE/DS 트랙 Level 1~5 문제를 대화식으로 풀이 → 세션을 .qmd 포스트로 저장
---

CLAUDE.md 의 실행 프로토콜(Phase 0~4)을 순서대로 따른다.

## 로드할 가이드 (Phase 0)

1. `guides/AGENT_GUIDE_CORE.md`
2. `AGENT_GUIDE.md`
3. `guides/algo-tutor.md`
4. Mode B (출제) 인 경우 추가: `guides/algo-flow-b-rules.md`
5. `docs/blog/posts/Code_Test/GUIDE.md`

## 실행

위 가이드를 Read 한 뒤, algo-tutor Step 순서로 수행한다.

### 단축 문법

- `random` — 그룹·토픽 모두 random
- `go` / `!` — 확인 단계 건너뛰고 Step 1부터 시작
- 유형명 (`문자열`, `Hash`, `DFS` 등) — 그룹 고정, 토픽 random
- `Programmers {문제명}` / URL — Mode A 실전
- `concept` / `concept:{주제}` — Mode C 개념

인자: $ARGUMENTS

예시:
- `DS Lv1 문자열 random go` (Mode B)
- `AIE Lv3 DFS go` (Mode B 유형 지정)
- `AIE Lv2 Programmers 완주하지못한선수` (Mode A)
- `공통 Hash concept` (Mode C)
