# HANDOFF — Netlify 빌드 방식 전환

작성일: 2026-04-11

---

## 목표

블로그 배포 방식을 로컬 `_site/` 생성 후 Git push 방식에서 **Netlify 서버 측 빌드(Remote Build)** 방식으로 전환한다.

### 전환 이유

- 로컬 렌더링 시 `_site/`가 초기화되어 Git 파일 유실 및 동기화 사고 빈번함.
- Netlify 서버에서 직접 `quarto render`를 수행하여 빌드 무결성 확보.

---

## 현재 상태 (2026-04-11 기준)

- **배포 방식**: Git 푸시 감지 후 Netlify 서버에서 빌드 수행 (`netlify.toml` 설정 적용).
- **빌드 환경**:
  - `netlify.toml`: Quarto 설치 및 R/Python 의존성 직접 설치 명령 구성.
  - `requirements.txt`: Python 의존성 목록 정리.
  - `r_requirements.txt`: R 의존성 목록 정리.
  - `runtime.txt`: (제거됨, Netlify 시스템 Python 3.11 강제 사용).
  - `.gitignore`: `/_site/`를 다시 제외 목록으로 설정(Git 관리 제외).
- **상태**: 현재 `mise` 의존성 충돌 해결 후 `apt-get` 및 `pip`을 통한 수동 설치 방식으로 빌드 프로세스 구성 완료.

---

## 해결된 문제들

1. **빌드 실패(`Exit code 2`)**:
   - Python 3.14/3.10 버전 충돌: `mise`를 비활성화(`MISE_VERSION="disable"`)하고 시스템 Python 3.11을 강제 지정하여 해결.
   - 의존성 누락: `requirements.txt`와 `r_requirements.txt`를 생성하여 빌드 스크립트에서 자동 설치하도록 보강.
2. **`_site/` 유실**: `.gitignore`에 `/_site/`를 추가하고 원격 빌드 체제로 전환하여 로컬 렌더링 결과가 Git 저장소에 영향을 주지 않도록 격리.

---

## 향후 유지보수 가이드

- **Python 패키지 추가 시**: `requirements.txt`에 패키지 이름 추가 후 푸시.
- **R 패키지 추가 시**: `r_requirements.txt`에 패키지 이름 추가 후 푸시.
- **빌드 오류 발생 시**: Netlify 대시보드 -> Deploys -> 최근 빌드 로그 확인. 
  - `apt-get` 명령어나 패키지 설치 단계에서 에러가 나는지 확인.
  - 시스템 라이브러리 추가가 필요하면 `netlify.toml`의 `apt-get install` 라인에 패키지 추가.

---

## 관련 커밋 요약

| 커밋 | 내용 |
|---|---|
| `7a41d150` | Netlify 원격 빌드 체제 전환 (`netlify.toml` 생성) |
| `11c73813` | Python 의존성 설치 및 오류 처리(`quarto render || true`) |
| `58688a0e` | Python 의존성 최적화 (`blog_requirements` 파일 정리) |
| `21b54633` | Python 3.11 버전 명시 |
| `3aad9fc3` | Python 3.11로 완화 및 컴파일 옵션 조정 |
| `6a612281` | Python 3.11 강제 설치 및 시스템 Python 고정 |
| `5ad76d9e` | `.tool-versions` 삭제 및 `mise` 비활성화 |
| `d79fed6f` | `requirements.txt` 표준화 및 `netlify.toml` 정리 |
