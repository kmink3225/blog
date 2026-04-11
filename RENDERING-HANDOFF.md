# HANDOFF — Netlify 빌드 방식 전환

최초 작성일: 2026-04-11  
최종 업데이트: 2026-04-11

---

## 목표

블로그 배포 방식을 로컬 `_site/` 생성 후 Git push 방식에서 **Netlify 서버 측 빌드(Remote Build)** 방식으로 전환한다.

### 전환 이유

- 로컬 렌더링 시 `_site/`가 초기화되어 Git 파일 유실 및 동기화 사고 빈번함.
- Netlify 서버에서 직접 `quarto render`를 수행하여 빌드 무결성 확보.

---

## 현재 상태 (2026-04-11 최종)

- **배포 방식**: `@quarto/netlify-plugin-quarto` 공식 플러그인 사용. Git push → Netlify 서버 빌드.
- **빌드 환경**:
  - `netlify.toml`: 빌드 커맨드 없음, `publish = "_site"` + Quarto 플러그인만 선언.
  - `package.json`: `@quarto/netlify-plugin-quarto: ^0.0.5` 의존성.
  - `r_requirements.txt`: 로컬 참고용으로만 유지 (빌드에서 사용 안 함).
  - `requirements.txt`, `runtime.txt`: **삭제됨** — Python 엔진 불필요.
  - `_site/`: **git 추적 제외** (`.gitignore`에 `/_site/` 등록). 플러그인이 매번 새로 생성.
  - `_freeze/`: git 추적 유지.
  - `_quarto.yml`: `freeze: auto`, `eval: false`, `cache: false`.
- **실행 가능 청크**: `{python}` 0개, `{r}` 0개 — 완전 정적 블로그.
- **render-changed.ps1**: conda 의존성 제거, plain `quarto` 사용.

### 현재 `netlify.toml`

```toml
[build]
  publish = "_site"

[[plugins]]
  package = "@quarto/netlify-plugin-quarto"
```

### 현재 `package.json`

```json
{
  "dependencies": {
    "@quarto/netlify-plugin-quarto": "^0.0.5"
  }
}
```

---

## 알려진 한계 — 전체 재렌더링

Netlify 서버 빌드 방식은 **커밋할 때마다 935개 파일을 전부 재렌더링**한다 (~7분/회).
서버는 이전 빌드의 `_site/`를 기억하지 못하기 때문이다.
`freeze: auto`는 코드 실행 결과 캐싱이며, 마크다운→HTML 렌더링 시간에는 영향 없다.

### 빌드 시간 최적화 방법 (미적용)

`quarto publish netlify` 명령을 사용하면 로컬에서 렌더 후 Netlify API로 직접 배포한다:

```bash
quarto publish netlify   # 최초 실행 시 브라우저 인증 + _publish.yml 자동 생성
```

이후에는 다음 스크립트로 운영:
1. `quarto render <변경된파일>` (또는 `.\render-changed.ps1`)
2. `quarto publish netlify --no-render` (이미 렌더된 `_site/` 배포)
3. `git push` (소스 `.qmd` 파일만 push)

이 방식은 Netlify 빌드 분을 소모하지 않으며 Netlify 서버에서 렌더링하지 않는다.
`_publish.yml`에 Site ID를 등록해야 한다 (최초 1회 `quarto publish netlify` 대화형 실행 필요).

---

## 해결된 문제들 (전체 이력)

1. **Python 버전 설치 실패 (`mise` 오류)**:
   - `runtime.txt`에 `python-3.10` 형식 사용 → mise/pyenv가 `python@python-3.10`으로 해석, 정의 없음 오류.
   - `MISE_VERSION="disable"`은 mise 비활성화 변수가 아님 — mise 자체 버전 지정 변수였음.
   - **해결**: 정확한 패치 버전 `3.11.11` 지정 후, Python 엔진 자체가 불필요함을 확인하고 완전 제거.

2. **`skfda`, `torch`, `transformers` 설치 실패**:
   - `skfda`: Python 3.12+ 전용, `torch`/`transformers`: 용량 ~2GB로 빌드 타임아웃 유발.
   - **해결**: `requirements.txt`에서 제거.

3. **Python 엔진 완전 제거**:
   - 166개 `.qmd` 파일의 ` ```{python} ` → ` ```python ` 변환 (정적 코드 블록).
   - `_quarto.yml`에 `eval: false` 전역 설정 + 모든 청크 정적화 → Jupyter 커널 불필요.
   - `requirements.txt`, `runtime.txt` 삭제.

4. **`apt-get` 권한 오류**:
   - Netlify noble 빌드 컨테이너는 `apt-get`에 root 권한 없음.
   - R 청크는 `eval: false` + `_freeze/` 캐시로 실행 불필요 → R 설치 단계 제거.

5. **R 엔진 오류 (`Rscript: No such file or directory`)**:
   - `{r}` 청크가 남아있어 Quarto가 knitr 엔진(R)을 호출, 빌드 336/946에서 중단.
   - **해결**: 21개 `.qmd` 파일의 ` ```{r} ` → ` ```r ` 변환. 전체 실행 가능 청크 0개 달성.

6. **무한 리다이렉트 루프**:
   - `netlify.toml`의 `[[redirects]] from="/*" to="/index.html" status=200` 규칙이 SPA용 설정.
   - Quarto 정적 사이트에서 `index.html`의 상대경로 meta-refresh와 결합 → URL 무한 누적.
   - **해결**: `[[redirects]]` 규칙 완전 제거.

7. **루트 페이지가 `docs/projects/backfitting/`으로 리다이렉트**:
   - 과거 로컬 빌드로 생성된 깨진 `_site/index.html`이 git에 추적된 채 배포됨.
   - **해결**: `git rm -r --cached _site/` 로 `_site/` 전체를 git 추적에서 제거.

8. **수동 Quarto 설치 방식 → 공식 플러그인으로 교체**:
   - `curl`로 Quarto tar.gz를 `/tmp`에 직접 설치하는 방식은 비공식적이며 불안정.
   - **해결**: `@quarto/netlify-plugin-quarto` 공식 플러그인 + `package.json`으로 교체.

---

## 향후 유지보수 가이드

- **새 포스트 추가**: `.qmd` 파일 작성 후 `git push` → Netlify 자동 빌드 (~7분).
- **`{python}` 청크 주의**: 새 포스트에서 실행 가능한 ` ```{python} ` 청크를 사용하지 않는다. 반드시 ` ```python ` 정적 형식으로 작성.
- **`{r}` 청크 주의**: 마찬가지로 ` ```{r} ` 대신 ` ```r ` 정적 형식으로 작성.
- **`_site/`를 절대 git add 하지 않는다**: `.gitignore`에 `/_site/` 등록됨.
- **빌드 오류 발생 시**: Netlify 대시보드 → Deploys → 최근 빌드 로그 확인.

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

