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

- **배포 방식**: Git 푸시 감지 후 Netlify 서버에서 빌드 수행 (`netlify.toml` 설정 적용).
- **빌드 환경**:
  - `netlify.toml`: Quarto 설치 후 `quarto render`만 실행. R/Python 설치 단계 없음.
  - `r_requirements.txt`: 로컬 참고용으로만 유지 (빌드에서 사용 안 함).
  - `requirements.txt`, `runtime.txt`: **삭제됨** — Python 엔진 불필요.
  - `_site/`: **git 추적 제외** (`git rm --cached` 처리 완료). Netlify 빌드가 매번 새로 생성.
  - `_freeze/`: git 추적 유지. `freeze: auto` 설정으로 R 청크 실행 결과 캐시.
- **상태**: `quarto render`만으로 빌드 성공. 900여 개 포스트 렌더링 정상 동작 확인.

### 현재 `netlify.toml`

```toml
[build]
  publish = "_site"
  command = """
    curl -L -o quarto.tar.gz https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.550/quarto-1.4.550-linux-amd64.tar.gz && \
    tar -xzf quarto.tar.gz && \
    export PATH=$PATH:$(pwd)/quarto-1.4.550/bin && \
    quarto render || true
  """

[build.environment]
  QUARTO_VERSION = "1.4.550"
```

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

5. **무한 리다이렉트 루프**:
   - `netlify.toml`의 `[[redirects]] from="/*" to="/index.html" status=200` 규칙이 SPA용 설정.
   - Quarto 정적 사이트에서 `index.html`의 상대경로 meta-refresh와 결합 → URL 무한 누적.
   - **해결**: `[[redirects]]` 규칙 완전 제거.

6. **루트 페이지가 `docs/projects/backfitting/`으로 리다이렉트**:
   - 과거 로컬 빌드로 생성된 깨진 `_site/index.html`이 git에 추적된 채 배포됨.
   - **해결**: `git rm -r --cached _site/` 로 `_site/` 전체를 git 추적에서 제거. Netlify 빌드가 매번 신선한 `_site/` 생성.

---

## 향후 유지보수 가이드

- **새 포스트 추가**: `.qmd` 파일 작성 후 push → Netlify 자동 빌드.
- **`{python}` 청크 주의**: 새 포스트에서 실행 가능한 ` ```{python} ` 청크를 사용하지 않는다. 반드시 ` ```python ` 정적 형식으로 작성.
- **`{r}` 청크 주의**: 마찬가지로 ` ```{r} ` 대신 ` ```r ` 정적 형식으로 작성.
- **출력이 필요한 코드**: 로컬에서 렌더링 후 `_freeze/`를 커밋하면 Netlify에서 캐시 사용.
- **빌드 오류 발생 시**: Netlify 대시보드 → Deploys → 최근 빌드 로그 확인.
  - `quarto render` 이후 출력에서 실패 파일 확인.
  - `|| true`로 인해 빌드 "성공"으로 표시돼도 특정 파일 렌더링이 누락될 수 있음.
- **`_site/`를 절대 git add 하지 않는다**: `.gitignore`에 `/_site/` 등록됨. `git add -A` 해도 무시됨.

---

## 관련 커밋 요약

| 커밋 | 내용 |
|---|---|
| `7a41d150` | Netlify 원격 빌드 체제 전환 (`netlify.toml` 생성) |
| `11c73813` | Python 의존성 설치 및 오류 처리 (`quarto render \|\| true`) |
| `58688a0e` | Python 의존성 최적화 (`blog_requirements` 파일 정리) |
| `21b54633` | Python 3.11 버전 명시 |
| `3aad9fc3` | Python 3.11로 완화 및 컴파일 옵션 조정 |
| `6a612281` | Python 3.11 강제 설치 및 시스템 Python 고정 |
| `5ad76d9e` | `.tool-versions` 삭제 및 `mise` 비활성화 |
| `d79fed6f` | `requirements.txt` 표준화 및 `netlify.toml` 정리 |
| `0a4f4e6f` | `PYTHON_VERSION=3.11` 환경변수 추가 |
| `60df5ec9` | `runtime.txt` → `python-3.11` |
| `b7ba34f2` | 정확한 패치 버전 `3.11.11` 지정 |
| `dae572dc` | `skfda` 제거 (Python 3.12+ 전용) |
| `6e3f6c1e` | 166개 파일 `{python}` → `python` 정적 변환, `torch`/`transformers` 제거 |
| `94b35886` | `requirements.txt`, `runtime.txt` 삭제, Python 파이프라인 완전 제거 |
| `19872d8c` | `[[redirects]]` 무한 루프 규칙 제거 |
| `19495f38` | 21개 파일 `{r}` → `r` 정적 변환, R 엔진 의존성 완전 제거 |
