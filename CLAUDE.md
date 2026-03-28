# CLAUDE.md — Claude Code 실행 규칙

> 이 파일은 Claude Code가 **매 세션 시작 시 자동으로 읽는 진입점**이다.
> 아래 규칙은 리다이렉트가 아니라 **직접 따라야 하는 행동 지시**이다.

---

## 실행 프로토콜 (반드시 순서대로)

Claude Code는 규칙을 자체 요약·압축하거나, 단계를 건너뛰는 경향이 있다.
이를 방지하기 위해 아래 프로토콜을 **순서대로, 건너뛰지 않고** 실행한다.

### Phase 0: 가이드 로드 (작업 시작 전)

**파일을 읽지 않으면 작업을 시작하지 않는다.** 아래 파일을 순서대로 Read 도구로 읽는다.

1. `guides/AGENT_GUIDE_CORE.md` — 항상-온 규칙 (필수)
2. `AGENT_GUIDE.md` — 슬래시 커맨드 라우팅 테이블
3. 태스크에 해당하는 skill 가이드 (아래 라우팅 테이블 참조)
4. 해당 카테고리 `docs/blog/posts/{category}/GUIDE.md`

**"이미 알고 있다", "이전에 읽었다"는 이유로 스킵하지 않는다.**
같은 세션 내에서 동일 파일을 이미 Read한 경우에만 재읽기를 생략할 수 있다.

### Phase 1: 탐색 (info-search)

포스트 작성·수정·전환 태스크인 경우, `guides/info-search.md`의 3-Layer 병렬 탐색을 실행한다.
탐색 결과를 사용자에게 1~2줄로 보고한 후 다음 단계로 넘어간다.

### Phase 2: 실행

skill 가이드(write-post.md, retrofit-post.md 등)의 Step을 **순서대로** 실행한다.
각 Step 시작 시 어떤 단계를 수행하는지 **사용자에게 보이는 텍스트로 명시**한다.

```
예시:
"Step 1: 카테고리 확인 — Statistics 폴더, 다음 번호 54"
"Step 3: 중복 판단 — Grep으로 'Leibniz' 검색, 기존 포스트 없음"
```

Step을 암묵적으로 건너뛰거나, 여러 Step을 한 문장으로 뭉개지 않는다.

### Phase 3: 검증 (Self-Check)

작업 완료 보고 **전에** `guides/AGENT_GUIDE_CORE.md`의 Self-Check 항목을 **출력**한다.
체크리스트를 내부적으로만 점검하고 생략하지 않는다.

```
예시:
"Self-Check:
- [x] 한다 체 준수
- [x] 수동 번호 없음
- [x] index.qmd 업데이트 완료
- [x] 수식 공백 확인
- [x] 분량 480줄"
```

### Phase 4: 자동 배포 (기본 동작)

Self-Check 통과 후 **별도 지시 없이 `guides/publish.md`를 로드하고 git add → commit → push를 실행**한다.

예외 (실행하지 않는 경우):
- `/qa`, `/log` 태스크 (파일 변경 없음)
- 사용자가 "push 하지 마" 등 명시적으로 제외 지시한 경우

---

## 절대 규칙 5개 (인라인 — 리다이렉트 아님)

1. **한다 체** — `~한다/~이다/~된다` (X: `~합니다/~입니다`)
2. **수동 번호 금지** — `number-sections: true`가 자동 부여 (X: `## 1. 개요`)
3. **Category GUIDE 필수 로드** — 해당 카테고리 GUIDE.md를 Read 도구로 읽은 후에만 포스트 작성
4. **index.qmd 업데이트** — 새 포스트 작성 후 반드시 링크 추가
5. **이모지 사용 금지** — `.qmd` 콘텐츠에 이모지 넣지 않음

---

## 슬래시 커맨드 라우팅

| 명령어 | 추가 로드 가이드 |
|--------|-----------------|
| `/write [category] [topic]` | `guides/info-search.md` + `guides/write-post.md` + category GUIDE |
| `/fix [file-path]` | `guides/retrofit-post.md` + category GUIDE |
| `/qa [question]` | `guides/info-search.md` + `guides/answer-question.md` |
| `/convert [category]` | `guides/info-search.md` + `guides/convert-tbd.md` + category GUIDE |
| `/series [category]` | `guides/info-search.md` + `guides/organize-series.md` + category GUIDE |
| `/audit [file-path]` | `guides/audit.md` + category GUIDE |
| `/log` | `guides/changelog-summary.md` |
| `/reindex [category]` | `guides/reorganize-index.md` + category GUIDE |
| `/publish` | `guides/publish.md` |

슬래시 커맨드가 없으면 자연어로 태스크를 추론하여 위 표에서 가장 적합한 행을 선택한다.

---

## 카테고리 목록

`Statistics` / `Math` / `Machine_Learning` / `Deep_Learning` / `Experimentation` /
`Engineering` / `Agent` / `Data_Science` / `Governance` / `Strategy_Frameworks` /
`Code_Test` / `Surveilance`

---

## 규칙 우선순위

```
카테고리 GUIDE.md  >  guides/AGENT_GUIDE_CORE.md  >  에이전트 자체 판단
```

---

## Project Info

- **Site**: https://kk3225.netlify.app
- **Author**: Kwangmin Kim
- **Stack**: Quarto → Netlify
- **Commands**: `quarto preview` / `quarto render`
- **Key Files**: `_quarto.yml`, `docs/blog/posts/_metadata.yml`
