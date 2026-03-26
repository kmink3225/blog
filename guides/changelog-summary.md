---
name: changelog-summary
type: skill
description: >
  git 히스토리 기반으로 블로그 포스트의 생성/수정/삭제 이력을 요약한다.
  기간별(오늘, 이번주, 최근 N일) 조회를 지원한다.
prerequisite:
  - AGENT_GUIDE.md (공통 코어)
---

# 변경 이력 요약

사용자가 "오늘 뭐 만들었지", "이번주 포스트 요약", "최근 3일 변경사항" 등을 요청하면 이 스킬을 실행한다.

> **info-search 불필요**: 이 스킬은 콘텐츠 탐색이 아닌 git 조회 태스크이므로 info-search를 생략한다.

## 트리거 패턴

아래와 같은 요청이 들어오면 이 스킬을 로드한다.

- "오늘 변경된 포스트 요약해줘"
- "이번주 포스트 정리해줘"
- "최근 N일간 뭐 만들었지"
- "어떤 포스트가 생성/수정되었는지 보고싶어"

## 조회 절차

### Step 1: 미커밋 변경 확인 (오늘 작업)

커밋되지 않은 변경과 신규 파일을 먼저 확인한다.

```bash
# 수정된 .qmd 파일
git diff --name-status HEAD -- "docs/blog/posts/**/*.qmd"

# 새로 생성되었지만 아직 추적되지 않는 .qmd 파일
git ls-files --others --exclude-standard -- "docs/blog/posts/**/*.qmd"
```

### Step 2: 커밋 이력 조회 (기간별)

사용자가 요청한 기간에 맞춰 `--since` 옵션을 조정한다.

```bash
# 오늘
git log --since="YYYY-MM-DD" --name-status --pretty=format:"%h %ad %s" --date=short -- "docs/blog/posts/**/*.qmd"

# 이번주 (월요일 기준)
git log --since="이번주 월요일 날짜" --name-status --pretty=format:"%h %ad %s" --date=short -- "docs/blog/posts/**/*.qmd"

# 최근 N일
git log --since="N days ago" --name-status --pretty=format:"%h %ad %s" --date=short -- "docs/blog/posts/**/*.qmd"
```

### Step 3: 결과 분류

git 출력의 상태 코드를 기준으로 분류한다.

| 코드 | 의미 | 표시 |
|------|------|------|
| A | 신규 생성 | **신규** |
| M | 수정 | **수정** |
| D | 삭제 | **삭제** |
| R | 이름 변경/이동 | **리네이밍** |

### Step 4: 요약 보고

아래 형식으로 출력한다.

```
## 포스트 변경 요약 (기간)

### 미커밋 (오늘 작업중)
| 구분 | 파일 | 내용 |
|------|------|------|
| 신규 | `경로/파일.qmd` | 제목 또는 변경 요약 |
| 수정 | `경로/파일.qmd` | 변경 요약 |

### MM/DD — 커밋 메시지
| 구분 | 카테고리 | 파일 | 제목 |
|------|---------|------|------|
| 신규 | Agent | `파일.qmd` | 제목 |
...

### 통계
- 신규: N편
- 수정: N편
- 삭제: N편
```

## 보고 규칙

- 파일 경로에서 카테고리를 추출한다 (`docs/blog/posts/Agent/...` → Agent)
- 신규 파일은 YAML `title`을 읽어 제목을 표시한다. 파일 수가 많으면(10개 초과) 카테고리별 편수로 요약한다
- 수정 파일은 `git diff`로 변경 범위를 간략히 파악한다 (전체 diff를 출력하지 않는다)
- index.qmd 변경은 별도로 나열하지 않고 "index 업데이트 포함"으로 축약한다
