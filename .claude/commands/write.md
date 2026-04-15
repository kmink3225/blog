---
description: 새 포스트 작성 — 3-Layer 탐색 → 중복 판단 → .qmd 신규 작성 → index.qmd 링크 추가 → 렌더링 → 배포
---

CLAUDE.md 의 실행 프로토콜(Phase 0~4)을 순서대로 따른다.

## 로드할 가이드 (Phase 0)

1. `guides/AGENT_GUIDE_CORE.md`
2. `AGENT_GUIDE.md`
3. `guides/info-search.md`
4. `guides/write-post.md`
5. `docs/blog/posts/{category}/GUIDE.md` (인자에서 category 파싱)

## 실행

위 가이드를 모두 Read 한 뒤, info-search 3-Layer 탐색 → write-post Step 순서대로 수행한다.

인자: $ARGUMENTS

형식: `[category] [topic]` (예: `Statistics continuous distributions`)
