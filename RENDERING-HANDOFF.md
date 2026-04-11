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

