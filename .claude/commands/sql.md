---
description: SQL 코딩 테스트 튜터 — Programmers Level 1~5 문제를 평가·교정·해설 → 세션을 .qmd 포스트로 저장
---

CLAUDE.md 의 실행 프로토콜(Phase 0~4)을 순서대로 따른다.

## 로드할 가이드 (Phase 0)

1. `guides/AGENT_GUIDE_CORE.md`
2. `AGENT_GUIDE.md`
3. `guides/sql-tutor.md`
4. Mode B (출제) 인 경우 추가: `guides/sql-flow-b-rules.md`
5. `docs/blog/posts/Code_Test/GUIDE.md`

## 실행

위 가이드를 Read 한 뒤, sql-tutor Step 순서로 수행한다.

### 단축 문법

- `random` — 그룹·토픽 모두 random (track 생략 시 DS)
- `go` / `!` — 확인 단계 건너뛰고 Step 1부터
- 유형명 (`JOIN`, `NULL처리`, `WindowFunction` 등) — 그룹 고정
- `Programmers {문제명}` / URL — Mode A 실전
- `concept` / `concept:{주제}` — Mode C 개념

### SQL 출제 용어 구분

- "Active 취약점 연계" → `guides/sql-weakness.md` 기반
- "Trick Point" → 유형 일반 함정 (weakness 아님)

인자: $ARGUMENTS

예시:
- `DS Lv1 random go`
- `Lv2 JOIN go`
- `Programmers 조건에맞는회원수구하기`
- `WindowFunction concept`
