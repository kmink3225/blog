# SSH 기반 Private Git 패키지 설치 - 작업 컨텍스트

블로그 리포에서 `4-ssh-private-package.qmd` 파일을 편집할 때 참고할 작업 기록.

## 프로젝트 정보

- 프로젝트 경로 (로컬): `C:\Users\kmkim\Desktop\SG_Projects\agent`
- 프로젝트 경로 (VM): `~/projects/kmkim/agent`
- VM 접속: `ssh ai_agent_dev_vm` (azureuser@20.196.144.16)
- 패키지 관리: Poetry (poetry-core 빌드 시스템)
- Python: 3.11 (.venv 기반)

## 설치 대상 패키지

- 이름: `sg-data-standardization`
- 버전: 1.0.0
- 설명: 데이터베이스 테이블/컬럼 명명 규칙 검증 및 물리명 자동 생성 패키지
- 의존성: openpyxl, pandas, tqdm
- 소스: `git+ssh://git@seegene_org/SeegeneDevelopmentPlatform/data_standardization.git@main`

## pyproject.toml 의존성 선언

```toml
sg-data-standardization @ git+ssh://git@seegene_org/SeegeneDevelopmentPlatform/data_standardization.git@main
```

## 작업 과정 (시간순)

### 1. 문제 확인
- `pyproject.toml`에 패키지가 선언되어 있었지만 실제 설치 안 됨
- `pip show sg-data-standardization` → Package(s) not found

### 2. 로컬 SSH 설정 시도 (Windows)
- 로컬 `~/.ssh/config`에 `seegene_org` 호스트가 없었음
- `github.com` 호스트는 있었음 (키: `id_ed25519_github`)
- `seegene_org` 호스트 추가함:
  ```
  Host seegene_org
      HostName github.com
      User git
      IdentityFile C:/Users/kmkim/.ssh/id_ed25519_github
  ```
- SSH 키에 passphrase가 걸려 있어 비대화식 환경에서 인증 실패
  - 에러: `read_passphrase: can't open /dev/tty`
- PowerShell에서 `eval $(ssh-agent -s)` 실행 시 에러
  - PowerShell은 `Start-Service ssh-agent` 사용해야 함

### 3. VM으로 전환
- VM에는 이미 SSH 설정이 완비되어 있었음:
  ```
  ~/.ssh/
  ├── seegene_org        # 조직용 개인키
  ├── seegene_org.pub    # 조직용 공개키
  ├── agent_repo         # agent 리포용 개인키
  ├── agent_repo.pub
  ├── config             # 호스트 별칭 설정 완료
  └── ...
  ```
- VM SSH config:
  ```
  Host agent_repo
      HostName github.com
      User git
      IdentityFile ~/.ssh/agent_repo

  Host seegene_org
      HostName github.com
      User git
      IdentityFile ~/.ssh/seegene_org
  ```

### 4. 실수: pip으로 먼저 설치함
- `pip install -e .`로 설치해버림 (poetry 프로젝트인데)
- 이후 `pip uninstall sg-data-standardization -y`로 제거

### 5. Poetry 환경 문제
- `poetry install` 실행 시 에러:
  ```
  'C:\Users\kmkim\AppData\Local\miniconda3\envs\nblog' could not be resolved
  ```
- 원인: Poetry가 로컬 Windows Python 경로를 참조하고 있었음
- 해결: `poetry env use /home/azureuser/projects/kmkim/agent/.venv/bin/python3`

### 6. 최종 설치 성공
```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/seegene_org
poetry install
poetry show sg-data-standardization  # 확인 완료
```

## 작성한 블로그 파일

- 파일: `4-ssh-private-package.qmd`
- 기존 시리즈: 0-ssh.qmd → 1-ssh-remote.qmd → 2-ssh-vm.qmd → 3-ssh-keygen.qmd → **4-ssh-private-package.qmd**
- 스타일: 기존 `3-ssh-keygen.qmd`의 형식(YAML frontmatter, 단계별 구성, 표, 코드블록)을 따름

## 패키지 업데이트 방법 (나중에 필요 시)

```bash
poetry update sg-data-standardization
```
