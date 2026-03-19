# Engineering 카테고리 작성 가이드

> 이 문서는 `AGENT_GUIDE.md`의 공통 규칙을 보충하는 **Engineering 전용 가이드**이다.
> 공통 규칙(YAML 헤더, 한다 체, index.qmd 패턴 등)은 `AGENT_GUIDE.md`를 따른다.

---

## 카테고리 특성

- **실무/도구 중심**: 개념보다 "어떻게 설정하고 사용하는가"에 초점을 둔다
- **시리즈 구성**: Git(15편), Poetry(17편), Airflow(18편), SSH(7편) 등 시리즈 단위로 구성된다
- **커맨드 기반**: CLI 명령어, 설정 파일, 코드 스니펫이 핵심 콘텐츠이다
- **하위 카테고리가 다양**: Data Engineering, DevOps, Infra, Python, System, web 등 광범위하다
- **파일명 패턴**: 하위 영역마다 다르므로 기존 패턴을 반드시 확인한다

---

## 포스트 콘텐츠 구조

Engineering 카테고리는 다른 카테고리와 달리 **도구/기술 튜토리얼**이 주력이다. 콘텐츠 구조를 주제 성격에 따라 두 가지로 구분한다.

### 유형 A: 도구/기술 튜토리얼 (Git, Docker, Airflow 등)

#### 1. 정의 (Definition)

- 도구/기술이 무엇인지 한 문장으로 정의한다
- 핵심 특징 3~5개를 bullet으로 나열한다

```markdown
::: {.callout-note}
## 정의: Docker

Docker는 애플리케이션과 그 의존성을 **컨테이너(container)**라는 격리된 환경에 패키징하여
어디서든 동일하게 실행할 수 있게 하는 플랫폼이다.

- 핵심: OS 수준 가상화 (VM보다 가볍다)
- 구성: Image(빌드 단위) + Container(실행 단위)
- 관리: Dockerfile(빌드 스크립트) + docker-compose(다중 컨테이너 오케스트레이션)
:::
```

#### 2. 개념 및 원리 (Concept & Principles)

- 도구의 아키텍처/동작 원리를 설명한다
- 핵심 컴포넌트 간 관계를 다이어그램으로 표현한다

#### 3. 직관적 설명 (Intuitive Explanation)

- 이 도구가 없었을 때의 불편함 → 도구가 해결하는 문제로 설명한다

#### 4. 왜 필요한가 (Why It Matters)

- 실무에서 이 도구를 사용하지 않으면 발생하는 문제를 제시한다
- 대안 도구와의 비교를 포함한다

#### 5. 응용 분야 (Applications)

- 어떤 워크플로에서 이 도구가 사용되는지 설명한다

#### 6. 예시 (Examples)

- 실제 사용 시나리오를 단계별로 보여준다
- 초보자가 따라할 수 있는 수준의 예시를 제공한다

#### 7. 코드/명령어 예시 (Code/Command Examples)

- CLI 명령어와 설정 파일이 핵심이다
- 명령어 → 출력 → 설명 순서로 작성한다
- 설정 파일(YAML, TOML, INI)은 주석으로 각 항목을 설명한다

```markdown
```bash
# 가상환경 생성 및 의존성 설치
poetry init                    # pyproject.toml 생성
poetry add pandas numpy        # 의존성 추가
poetry install                 # 가상환경에 설치
poetry run python main.py      # 가상환경에서 실행
```

```toml
# pyproject.toml 예시
[tool.poetry]
name = "my-project"
version = "0.1.0"
python = "^3.11"

[tool.poetry.dependencies]
pandas = "^2.0"        # 데이터 처리
numpy = "^1.24"        # 수치 연산
```
```

#### 8. 관련 주제 (Related Topics)

- 같은 시리즈의 이전/다음 포스트를 링크한다
- 대안/보완 도구를 연결한다
- **파일이 아직 존재하지 않더라도 논리적으로 필요한 주제는 placeholder 링크로 포함한다.** 이를 통해 향후 채워야 할 콘텐츠를 체계적으로 파악할 수 있다. Placeholder 링크는 경로를 미리 지정하되, 해당 파일이 생성되면 자연스럽게 연결된다.

### 유형 B: 시스템/아키텍처 포스트 (System/, Cloud_Archi/)

- 이 유형은 Statistics/ML 카테고리의 구조(정의 → 원리 → 직관 → 응용)를 따른다
- 다이어그램(Mermaid, ASCII)을 적극 활용한다
- 설계 결정(design decision)의 근거를 명시한다

---

## 하위 카테고리별 추가 지침

### Data Engineering (Data_Engineering/)

- **Airflow**: 18편 시리즈. DAG 정의, Operator, Scheduler, Executor 등을 다룬다
- **Spark, Kafka**: 계획 중. 빅데이터 처리 파이프라인을 다룰 예정이다
- 파일명 패턴: `번호.토픽명.qmd` (예: `01.intro.qmd`)

### 자료구조 (Data_Structure/)

- 배열, 연결리스트, 스택, 큐, 트리, 그래프 등 기본 자료구조를 다룬다
- 시간/공간 복잡도(Big-O)를 반드시 포함한다
- 파일명 패턴: `날짜_토픽명.qmd` (예: `2023-01-17_data_structure_overview.qmd`)

### DevOps (DevOps/)

- **Git**: 15편 완결 시리즈. 기초 → 브랜치 → 협업 → 고급 순서
- **Poetry**: 17편 완결 시리즈. 설치 → 의존성 → 배포 → 트러블슈팅 순서
- **Docker**: 확장 중. 컨테이너 기초부터 CI/CD 통합까지
- **Conda**: 4편. Poetry와의 비교를 포함한다
- 파일명 패턴: `번호.토픽명.qmd` 또는 `번호-토픽명.qmd`

### 인프라 (Infra/)

- **Cloud**: Azure(19편, 가장 활발), AWS(4편), Azure DevOps(3편)
- **OS**: Linux 명령어, Shell 개념, WSL2 설정
- **Security**: SSH 7편 시리즈 (개요 → 키 생성 → Agent Forwarding → 터널링)
- 파일명 패턴: `번호-토픽명.qmd` 또는 `날짜_토픽명.qmd`

### Python (Python/)

- 입문부터 고급까지: 변수, 함수, OOP, 비동기, 데코레이터, 로깅 등
- 23편으로 구성. 파일명 패턴: `번호-토픽명.qmd`

### 시스템 (System/)

- 데이터 모델링(개념적/논리적/물리적), 플랫폼 설계, 클라우드 아키텍처
- Agent 카테고리와 크로스 레퍼런스가 많다

### 웹 (web/)

- HTTP, 방문자 추적, 수익화 등 기본 웹 개념
- 3편으로 구성. 소규모 카테고리이다

---

## 도구 비교 테이블 템플릿

도구 소개 포스트에는 대안 도구와의 비교를 포함한다:

```markdown
| 기준 | Poetry | pip + venv | Conda | Pipenv |
|---|---|---|---|---|
| 의존성 해석 | 정밀 (SAT solver) | 단순 | 정밀 | 정밀 |
| Lock 파일 | poetry.lock | 없음 | 없음 | Pipfile.lock |
| 빌드/배포 | 통합 | 별도 (setuptools) | 별도 | 없음 |
| 가상환경 | 자동 관리 | 수동 | 자동 | 자동 |
| Python 외 패키지 | 불가 | 불가 | 가능 | 불가 |
```

---

## 코드/명령어 작성 규칙

- 코드 블록에 언어 태그를 반드시 지정한다: `bash`, `python`, `toml`, `yaml`, `dockerfile`, `sql`
- CLI 명령어에는 주석으로 각 명령의 목적을 설명한다
- 위험한 명령어(rm -rf, force push 등)에는 callout 경고를 추가한다
- 설정 파일은 최소 동작 예시(minimal working example)를 먼저 보여주고, 이후 상세 옵션을 설명한다
