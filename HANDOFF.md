# HANDOFF — Netlify 빌드 방식 전환

작성일: 2026-04-08

---

## 목표

현재 블로그 배포 방식을 **git에 `_site/` HTML 포함 → push** 방식에서
**Netlify가 `quarto render` 빌드** 방식으로 전환한다.

### 전환 이유

- 현재 방식은 `_site/` HTML 수천 개를 git에 포함 → 저장소 비대
- 이번 세션에서 git 조작 실수로 HTML 868개가 원격에서 삭제되는 사고 발생
- quarto 공식 레포(quarto-dev/quarto-web)도 Netlify 빌드 방식 사용

---

## 현재 상태 (2026-04-08 기준)

- `.gitignore`: `_site/`에 대한 ignore 규칙 없음 → git이 `_site/` 정상 추적 중
- Netlify: 빌드 커맨드 없음, git의 `_site/` 폴더를 직접 서빙
- `_freeze/`: `.gitignore`에서 주석 처리(`# /_freeze/`) → git 미추적 상태

---

## 전환 단계 (순서대로 실행)

### Step 1 — `_freeze/` git 추적 시작

```bash
# _freeze/ 가 git에 없으면 quarto render 시 모든 코드 재실행 → 빌드 시간 폭증
# freeze를 먼저 git에 올려야 Netlify 빌드가 빠르게 동작

git add _freeze/
git commit -m "feat(freeze): quarto freeze 결과 추적 시작 — Netlify 빌드 캐시용"
git push
```

### Step 2 — Netlify 사이트 설정 변경

Netlify 대시보드 → Site configuration → Build & deploy → Build settings:

| 항목 | 값 |
|---|---|
| Build command | `quarto render` |
| Publish directory | `_site` |

저장 후 **Deploy** 탭에서 수동 트리거로 테스트 빌드 실행.

### Step 3 — 빌드 성공 확인

빌드 로그에서 오류 없이 완료되는지 확인.
실패 시 Python 의존성 문제일 가능성 높음 → Step 4로.

### Step 4 — Netlify 의존성 파일 추가 (필요 시)

Netlify는 `requirements.txt`를 자동 감지해서 pip install 실행.

```bash
# 현재 conda 환경(blog)에서 의존성 추출
conda activate blog
pip freeze > requirements.txt
# 불필요한 패키지 정리 후 커밋
```

또는 `runtime.txt`로 Python 버전 지정:
```
3.11
```

### Step 5 — `_site/` gitignore 추가 및 git 추적 제거

빌드가 정상 확인된 후에만 실행 (되돌리기 어려움):

```bash
# .gitignore에 추가
echo "/_site/" >> .gitignore

# git 인덱스에서 제거 (파일은 로컬에 유지)
git rm -r --cached _site/

git add .gitignore
git commit -m "fix(gitignore): _site/ git 추적 제거 — Netlify 빌드 방식 전환"
git push
```

---

## 주의사항

- **Step 5는 Step 2~4 완료 후에만 실행** — `_site/` 제거 전에 Netlify 빌드가 정상임을 반드시 확인
- Netlify 무료 플랜 빌드 시간: 월 300분 → `_freeze/` 추적으로 재실행 최소화 필수
- `_freeze/`가 없으면 Python/R 코드 있는 포스트마다 재실행 → 빌드 시간 급증

---

## 관련 커밋

| 커밋 | 내용 |
|---|---|
| `abb330e7` | `.gitignore` 수정 — `/_site/` 주석 처리 (현재) |
| `123419ef` | `_site/` HTML 1127개 복구 |
| `ff72de55` | (사고) SQL 커밋 시 `_site/` HTML 868개 삭제 |
