# HANDOFF — Netlify 배포 파이프라인

최초 작성일: 2026-04-11  
최종 업데이트: 2026-04-11

---

## 현재 배포 방식 (최종)

**로컬 렌더 → `_site/` git 커밋 → git push → Netlify 정적 서빙**

```
[로컬 PC]
.qmd 수정/추가
    ↓
quarto render <파일>   ← 변경된 파일만, 수초~수분
    ↓
_site/ 업데이트됨
    ↓
git add -A             ← .qmd + _site/ 동시 포함
git commit && git push
    ↓
[Netlify] 빌드 없이 _site/ 그대로 서빙 → kk3225.netlify.app 즉시 반영
```

### 핵심 설정

| 파일 | 내용 |
|------|------|
| `netlify.toml` | `publish = "_site"`, 빌드 커맨드 없음 |
| `.gitignore` | `/_site/` **제외** — git 추적 허용 |
| `_quarto.yml` | `freeze: auto`, `eval: false`, `cache: false` |
| `_publish.yml` | Site ID 등록 (quarto publish 쓸 경우 참고용) |

---

## 왜 `_site/`를 git에 넣는가?

Quarto 공식 레포(`quarto-dev/quarto-web`)는 `_site/`를 `.gitignore`에 넣는다.
이유: **GitHub Actions로 서버 렌더링 후 Netlify API 직접 배포**하기 때문에 git에 넣을 필요가 없다.

이 블로그는 다르다:

| | 공식 Quarto 레포 | 이 블로그 |
|--|--|--|
| CI/CD | GitHub Actions | 없음 |
| 렌더링 위치 | GitHub 서버 | 로컬 PC |
| `_site/` in git | ❌ 불필요 | ✅ 필요 (백업 + 배포) |
| `_site/` 날아가면? | 서버가 다시 렌더 | 로컬에서 20분 재렌더 |

`_site/`를 git에 넣으면:
- **절대 날아가지 않는다** — git clone 하면 복원됨
- **git push = 배포** — Netlify가 빌드 없이 서빙
- `git add -A` 하나로 소스와 빌드 결과 동시 커밋

Quarto 공식 문서도 이 방식을 유효한 방법으로 명시한다:
> "If you have your _site directory checked into version control then everything is now configured and your site will be deployed to Netlify automatically whenever you commit to your repository."

---

## "GitHub Actions / GitHub Pages로 가면 이 고민 안 해도 되나?" — NO

자주 헷갈리는 질문이므로 명확히 정리한다.

**서버 빌드 방식 (GitHub Actions, Netlify 자동빌드)** 은 항상 처음부터 전체 재렌더한다.  
`freeze: auto`를 써도 캐시 레이어가 있을 뿐, 근본적으로 936개 파일을 서버에서 렌더한다.

| | 현재 방식 (로컬 렌더 + `_site/` in git) | 서버 빌드 (GitHub Actions 등) |
|--|--|--|
| 렌더 범위 | **변경된 파일만** (수 초) | 전체 936개 (~7분/커밋) |
| 렌더 위치 | 로컬 PC | GitHub/Netlify 서버 |
| `_site/` git 필요 여부 | ✅ 필요 (이게 배포물) | ❌ 서버가 만들어줌 |
| `_site/` 날아갈 위험 | 없음 (git에 있음) | 없음 (서버가 다시 만듦) |
| 추가 repo 필요? | ❌ 불필요 | ❌ 불필요 (같은 repo에 workflow 추가) |

**결론**: GitHub Pages로 옮겨도 "매 push마다 전체 재렌더" 문제는 그대로다.  
현재 방식이 **이 블로그에는 가장 빠르고 단순**하다.  
공식 Quarto 레포가 `_site/` gitignore하는 이유는 GitHub Actions을 쓰기 때문이지, 이 방식이 틀려서가 아니다.

---

## 공식 방식 vs 현재 방식 — 효율성·안전성 비교

| 항목 | 공식 방식 (서버 빌드) | 현재 방식 (로컬 렌더) |
|------|----------------------|----------------------|
| **배포 속도** | push 후 ~7분 대기 | push 즉시 반영 |
| **렌더 범위** | 전체 재렌더 | 변경분만 |
| **실수 위험** | 낮음 — 서버가 관리 | `.qmd` 수정 후 렌더 안 하면 사이트 미반영 |
| **로컬 환경 의존** | 없음 | Quarto 설치 필수 |
| **R/Python 코드 실행** | ✅ 서버에서 실행 가능 | ⚠️ 로컬에서만 실행 |
| **repo 용량** | 가벼움 | HTML 1119개 포함 (무거움) |
| **장애 복구** | CI 깨지면 배포 중단 | git에 HTML 있어 과거 버전 즉시 복원 |

### 이 블로그 기준으로는?

**현재 방식이 더 효율적** — 코드 실행 청크 0개이므로 서버 환경 불필요, 변경분만 렌더해 속도가 압도적으로 빠름.

**공식 방식이 유리한 경우:**
- R/Python 코드가 실제로 실행돼야 할 때 (그래프 생성, 데이터 분석 등)
- 여러 명이 협업하는 프로젝트 (로컬 환경 통일 어려울 때)
- repo 용량을 작게 유지하고 싶을 때

---

## R/Python 청크를 정적으로 변환한 이유와 재고 지점

현재 이 블로그의 모든 `{r}`, `{python}` 청크는 ` ```r `, ` ```python ` 형식으로 변환돼 있다 (총 189개).  
변환 이유: Netlify 서버에서 R/Python 환경 설치 실패 → 렌더 불가 → 정적 변환으로 우회.

**그런데 꼭 정적이어야 하는 건 아니다:**
- 로컬 렌더 방식에서는 로컬 PC의 R/Python이 실행됨 → 코드 실행 자체는 가능
- 단, 실행 시간이 길어지고, 환경(패키지 버전 등) 관리가 필요해짐
- `freeze: auto`를 쓰면 한 번 실행 후 결과를 캐시하므로 반복 렌더 시 재실행 안 함

**정적 변환이 맞는 경우:**
- 코드 출력(그래프, 표)을 이미 스크린샷/이미지로 대체했거나
- 교육 목적으로 코드만 보여주면 충분한 포스트

**다시 실행 코드로 되돌릴 수 있는 경우:**
- 로컬에 R/Python 환경이 갖춰져 있고
- 그래프나 계산 결과를 항상 최신으로 유지하고 싶다면
- ` ```r ` → ` ```{r} `로 되돌리면 됨 (단, 전체 렌더 시 실행 시간 증가)

---

## 주의사항

- **렌더 없이 push하면 사이트에 반영 안 됨** — `.qmd`는 최신이지만 `_site/` HTML은 구버전
- **반드시 순서**: `quarto render` → `git add -A` → `git push`
- `git add -A`는 완전히 OK — `_site/` 변경분이 자동으로 포함됨
- 전체 재렌더가 필요한 경우: `quarto render` (936개, ~20분)

---

## 실행 가능 청크 현황

- `{python}` 0개, `{r}` 0개 — 완전 정적 블로그
- 총 189개 청크 정적 변환 (166 python + 21 r + 2 LLFS)
- 새 포스트 작성 시: ` ```python `, ` ```r ` 형식 사용 (중괄호 없음)

---

## 해결된 문제 이력

1. **Python 버전 설치 실패** — mise `python-3.10` 형식 오류 → Python 엔진 완전 제거
2. **`skfda`/`torch` 설치 실패** — `requirements.txt` 제거
3. **`apt-get` 권한 오류** — Netlify noble 컨테이너 root 없음 → R 설치 제거
4. **R 엔진 오류** — 21개 `{r}` 청크 정적 변환
5. **무한 리다이렉트 루프** — SPA용 `[[redirects]]` 규칙 제거
6. **루트가 backfitting으로 리다이렉트** — 깨진 `_site/` git rm --cached
7. **Netlify 서버 재렌더 (~7분/커밋)** — `@quarto/netlify-plugin-quarto` → 로컬 렌더 방식 전환
8. **`docs/projects/LLFS/` 렌더 실패** — 2개 `{r}` 청크 정적 변환

---

## 관련 커밋

| 커밋 | 내용 |
|---|---|
| `6e3f6c1e` | 166개 `{python}` 정적 변환, Python 파이프라인 제거 |
| `19495f38` | 21개 `{r}` 정적 변환, R 엔진 제거 |
| `19872d8c` | `[[redirects]]` 무한 루프 제거 |
| `7030e382` | `@quarto/netlify-plugin-quarto` 플러그인 전환 |
| `6a82b564` | `quarto publish netlify` 방식, `_publish.yml` 추가 |
| `5cd9bf95` | `docs/projects/LLFS/` 2개 `{r}` 정적 변환 |
| `3fc7a0ec` | `_site/` git 커밋, `.gitignore` 수정, Netlify 자동빌드 재활성화 |


---

## 관련 커밋 요약

| 커밋 | 내용 |
|---|---|
| `7a41d150` | Netlify 원격 빌드 체제 전환 (`netlify.toml` 생성) |
| `6e3f6c1e` | 166개 파일 `{python}` → `python` 정적 변환, `torch`/`transformers` 제거 |
| `94b35886` | `requirements.txt`, `runtime.txt` 삭제, Python 파이프라인 완전 제거 |
| `19872d8c` | `[[redirects]]` 무한 루프 규칙 제거 |
| `19495f38` | 21개 파일 `{r}` → `r` 정적 변환, R 엔진 의존성 완전 제거 |
| `7030e382` | 공식 `@quarto/netlify-plugin-quarto` 플러그인으로 전환, `package.json` 추가 |
| `95c89bb6` | `render-changed.ps1` conda 의존성 제거 |
| `6a82b564` | `quarto publish netlify` 로컬 배포 방식 전환, `_publish.yml` 추가, `package.json` 삭제 |
| `5cd9bf95` | `docs/projects/LLFS/` 2개 파일 `{r}` → `r` 정적 변환 |

