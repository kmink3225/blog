---
name: publish
type: skill
description: >
  블로그 변경사항을 git add → commit → push까지 완료하는 절차.
  충돌 발생 시 해결 후 재push까지 포함한다.
  Quarto 블로그(kk3225.netlify.app)를 Netlify에 배포하는 최종 단계.
prerequisite:
  - AGENT_GUIDE.md (공통 코어)
---

# 블로그 배포 (git add → commit → push)

## 렌더링 구조

이 블로그는 Netlify가 build step 없이 커밋된 HTML 파일을 직접 서빙한다.
따라서 `.qmd` 파일을 수정·생성한 후 **반드시 HTML로 렌더링하고 함께 커밋**해야 사이트에 반영된다.

```
.qmd 수정/생성
    ↓
렌더링 (HTML 생성 — _site/ 에 생성됨)
    ↓
git add (.qmd + _site/ + _freeze/)
    ↓
commit → push → Netlify 반영
```

### _freeze 캐시 구조

- `_freeze/`는 코드 실행 결과를 캐시한다 — git에 추적됨 (`.gitignore`에서 제외됨)
- `_quarto.yml`에 `freeze: auto` 설정 → 소스가 변경되지 않은 파일은 코드 재실행 스킵
- 따라서 전체 렌더(`quarto render`)도 코드 실행 없이 파싱만 하므로 3~5분 수준으로 빠름

### 렌더링 명령어

#### 변경된 파일만 렌더링 (권장 — 빠름)

`render-changed.ps1`을 실행하면 마지막 커밋 이후 변경된 `.qmd`만 골라서 렌더링 후 자동 push한다.

```powershell
# 프로젝트 루트에서 실행
cd C:\Users\Administrator\Desktop\projects\blog
.\render-changed.ps1
```

- git diff(수정) + staged(staged) + untracked(신규) 파일을 모두 감지한다
- `conda blog` 환경으로 렌더링한다
- 렌더 후 `blog/index.qmd`를 재렌더하여 목록을 업데이트한다
- git add → commit → push 까지 자동 처리한다

#### 전체 렌더링 (뭔가 꼬였을 때)

```powershell
cd C:\Users\Administrator\Desktop\projects\blog
conda run -n blog quarto render
git add -A
git commit -m "chore: 전체 렌더링"
git push origin
```

#### 특정 파일만 렌더링

```powershell
conda run -n blog quarto render docs/blog/posts/Statistics/22-mle.qmd
```

개별 파일 렌더링 시 HTML이 `_site/` 하위에 생성된다.
단, `blog/index.qmd`가 업데이트되지 않으므로 새 포스트라면 index도 함께 렌더해야 한다.

```powershell
conda run -n blog quarto render docs/blog/posts/Statistics/22-mle.qmd
conda run -n blog quarto render docs/blog/index.qmd
```

::: {.callout-warning}
## 렌더링 없이 push 금지

`.qmd`만 커밋하고 HTML을 커밋하지 않으면 사이트에서 404가 발생한다.
커밋 전에 반드시 렌더링을 먼저 실행한다.

`draft: true`인 파일은 렌더링해도 사이트에 표시되지 않으나, HTML 파일은 생성된다.
:::

::: {.callout-important}
## 반드시 conda blog 환경 사용

Python/R 코드가 포함된 파일은 반드시 `conda run -n blog` 로 렌더해야 한다.
시스템 Python으로 렌더하면 패키지 의존성 오류가 발생한다.
:::

## 전환 절차

### Step 1: 변경 파일 확인

`git status`와 `git diff --stat`으로 변경된 파일 목록과 규모를 파악한다.

```bash
git --no-pager status
git --no-pager diff --stat
```

결과를 사용자에게 1~2줄로 요약 보고한다.

```
예: "변경 파일 4개 — 신규 포스트 2개(24-Agent-Architecture/), index.qmd 수정, TBD.qmd 초기화"
```

### Step 2: git add

변경 파일을 스테이징한다. 원칙은 **주제 단위로 묶어서 add**한다.

- 포스트 신규/수정 + 해당 index.qmd: 함께 add
- 가이드 파일 수정: 별도 커밋 권장
- `_site/`, `_freeze/` 등 빌드 산출물: 포함 여부를 `.gitignore` 기준으로 판단

```bash
# 전체 add (단일 커밋으로 묶을 때)
git add .

# 선택적 add (주제별 커밋 분리 시)
git add docs/blog/posts/Agent/24-Agent-Architecture/ docs/blog/posts/Agent/index.qmd
```

::: {.callout-warning}
## add 전 확인 사항

- 민감 정보(API 키, 비밀번호)가 포함된 파일이 없는지 확인
- `draft: true`인 파일이 의도치 않게 포함되지 않는지 확인
- 빌드 캐시(`_freeze/`)는 필요 시에만 포함
:::

### Step 3: 커밋 메시지 작성

커밋 메시지는 아래 형식을 따른다.

```
<type>: <한국어 요약> [선택: 파일 범위]

<선택: 본문 — 무엇을, 왜>
```

**type 목록**

| type | 사용 상황 |
|------|----------|
| `feat` | 신규 포스트 추가 |
| `fix` | 기존 포스트 수정·교정 |
| `refactor` | 구조 변경 (index 재구성, 파일 이동) |
| `docs` | 가이드·README 수정 |
| `chore` | 설정 파일, 빌드 관련 |

**예시**

```
feat: Agent 포스트 2개 추가 — LLM 지시 준수 메커니즘, 동적 주입 아키텍처

- 24-llm-instruction-compliance-mechanisms.qmd
- 25-system-prompt-dynamic-injection-architecture.qmd
- Agent/index.qmd 업데이트, TBD.qmd 초기화
```

커밋 메시지는 **에이전트가 직접 생성**한다. Step 1에서 파악한 변경 파일 목록을 기반으로 의미 있는 요약을 작성한다.

### Step 4: git commit

```bash
git commit -m "<생성한 커밋 메시지>"
```

멀티라인 메시지가 필요하면:

```bash
git commit -m "feat: Agent 포스트 2개 추가" -m "- 24-llm-instruction-compliance-mechanisms.qmd 신규\n- 25-system-prompt-dynamic-injection-architecture.qmd 신규\n- index.qmd 업데이트, TBD.qmd 초기화"
```

### Step 5: git push

```bash
git push
```

push가 성공하면 Netlify가 자동으로 빌드·배포를 시작한다. 완료까지 보통 1~3분 소요된다.

### Step 6: 충돌 발생 시 해결

push 시 아래와 같은 에러가 발생하면 원격 변경사항을 먼저 받아야 한다.

```
error: failed to push some refs
hint: Updates were rejected because the remote contains work that you do not have locally.
```

**해결 절차**

```bash
# 1. 원격 변경사항 가져오기
git pull --rebase origin main

# 2. 충돌 파일 확인
git --no-pager status
# "both modified:" 항목이 충돌 파일

# 3. 충돌 파일 열어 마커 확인
# <<<<<<< HEAD
# (로컬 변경)
# =======
# (원격 변경)
# >>>>>>> origin/main

# 4. 충돌 해결 후 스테이징
git add <해결한 파일>

# 5. rebase 계속 진행
git rebase --continue

# 6. 재push
git push
```

::: {.callout-important}
## 충돌 해결 원칙

- 블로그 포스트 파일(`.qmd`)은 **로컬 버전 우선**이 일반적이다 (내가 방금 작성한 내용이 최신)
- `index.qmd`는 양쪽 변경을 **모두 보존**해야 한다 (양쪽에서 추가된 링크가 각각 유효)
- 가이드 파일(`.md`)은 충돌 내용을 읽고 **더 최신 규칙을 채택**한다
- 판단이 어려우면 사용자에게 보여주고 결정을 요청한다 (Stop-and-Ask)
:::

### Step 7: 완료 보고

```
### 배포 결과
- **커밋**: <커밋 해시 앞 7자리> — <커밋 메시지>
- **push 상태**: 성공 / 충돌 해결 후 성공
- **Netlify**: 자동 빌드 시작 (https://kk3225.netlify.app)
- **변경 파일**: N개
```

## 주의 사항

- `_quarto.yml`, `_metadata.yml`, `styles.css` 등 프로젝트 설정 파일은 수정하지 않는다 (AGENT_GUIDE_CORE.md 권한 제한)
- push 전 `git --no-pager log --oneline -3`으로 최근 커밋 이력을 확인하면 실수를 방지할 수 있다
- 충돌이 복잡하거나 판단이 불가능한 경우 즉시 중단하고 사용자에게 보고한다
