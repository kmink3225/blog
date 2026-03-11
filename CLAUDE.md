# CLAUDE.md — Blog Repository Instructions

## Project Overview

Quarto 기반 기술 블로그. `.qmd` 파일로 콘텐츠 작성, `quarto render`로 정적 HTML 생성, Netlify 배포.

- **Site**: https://kk3225.netlify.app
- **Author**: Kwangmin Kim
- **Language**: 한국어 (한다 체)

## Directory Structure

```
blog/
├── _quarto.yml              # 마스터 설정 (navbar, sidebar, 빌드)
├── docs/blog/posts/         # 모든 블로그 콘텐츠
│   ├── _metadata.yml        # 공통 메타데이터 (댓글, TOC, 배너)
│   ├── Math/                # 선형대수, 미적분, 최적화
│   ├── Statistics/          # 분포, 검정, 베이지안
│   ├── Data_Science/        # CRISP-DM, EDA, Feature Engineering
│   ├── Machine_Learning/    # 분류, 회귀, 앙상블
│   ├── Deep_Learning/       # CNN, RNN, Transformer, GAN
│   ├── Engineering/         # DevOps, Python, 인프라, 자료구조
│   │   └── DevOps/          # Git, Poetry, Docker, K8s 등
│   ├── Experimentation/     # A/B Test, 인과추론
│   ├── RAG/                 # 검색 증강 생성
│   ├── Governance/          # 데이터 품질, 메타데이터
│   └── Surveilance/         # 모니터링, 로깅
├── _site/                   # 빌드 출력 (gitignore)
└── CLAUDE.md                # 이 파일
```

## .qmd 파일 작성 규칙

### YAML 헤더 (필수)

```yaml
---
title: "제목"
subtitle: "부제목"
description: |
  1-3문장 설명. 이 글에서 다루는 핵심 내용을 요약한다.
categories:
  - Category1
  - Category2
author: Kwangmin Kim
date: MM/DD/YYYY
---
```

- `title`, `description`, `categories`, `author`, `date`는 필수
- `format`, `toc`, `code-fold` 등은 `_metadata.yml`과 `_quarto.yml`에서 상속되므로 개별 파일에 넣지 않아도 됨
- `date`는 `MM/DD/YYYY` 형식 사용

### 시리즈 블로그 파일명 규칙

```
01.topic-name.qmd
02.topic-name.qmd
...
11_topic-name-detail.qmd   # 언더스코어도 허용 (기존 패턴)
```

- 번호 prefix로 순서 표시
- 하이픈(`-`) 또는 언더스코어(`_`)로 단어 구분
- 같은 시리즈 내에서는 일관된 구분자 사용

### 콘텐츠 스타일

- **한다 체 사용** (설명체): `~한다`, `~이다`, `~된다`
- **경어체 금지**: `~합니다`, `~입니다`, `~하세요` 사용하지 않음
  - O: `Git은 분산형 버전 관리 시스템이다.`
  - X: `Git은 분산형 버전 관리 시스템입니다.`
- **이모지 사용 금지**
- Quarto callout 블록 활용: `{.callout-tip}`, `{.callout-warning}`, `{.callout-important}`, `{.callout-note}`

### 코드 블록

````markdown
```bash
# shell 명령
poetry install
```

```python
# Python 코드
import pandas as pd
```

```toml
# 설정 파일
[tool.poetry]
name = "my-project"
```
````

실행 가능한 코드 블록이 필요한 경우:

````markdown
```{python}
#| eval: true
import pandas as pd
```
````

## 시리즈 블로그 정리 패턴

블로그 시리즈를 체계적으로 정리할 때 따르는 패턴:

1. **기존 파일 전체 읽기** — 현재 상태 파악
2. **문제 진단** — 중복, 잘못된 내용, 누락된 주제, 비체계적 구성 식별
3. **구조 설계** — 기초 → 핵심 → 심화 → 실전 순서로 배치
4. **파일 처리**:
   - 잘 된 파일: 유지
   - 내용이 잘못된 파일: 같은 번호로 새 파일 작성, 기존 파일 삭제
   - 누락된 주제: 새 파일 추가
5. **요약 테이블 제공** — 작업 결과를 사용자에게 보고

### 시리즈 구성 원칙

```
기초: 개요, 설치, 기본 개념
핵심: 주요 기능, 일상적 사용법
심화: 고급 기능, 비교 분석, CI/CD 통합
실전: 트러블슈팅, 실무 사례
```

## 완료된 정리 작업

### Git 시리즈 (`Engineering/DevOps/Git/`)
- 00: 비개발자용 Git (별도 대상)
- 01: 설치 및 설정
- 02: 기본 워크플로 (status, add, commit, push, pull)
- 03: 브랜치
- 04: 브랜치 전략 (Git Flow)
- 05: Pull Request
- 06: Git 그래프 시각화
- 07: 원격 저장소 관리
- 08: Merge vs Rebase
- 09: 되돌리기 (restore, reset, revert, reflog)
- 10: Stash
- 11: 태그와 SemVer
- 12: .gitignore
- 13: Cherry-pick
- 14: 고급 (bisect, submodule, worktree, hooks, alias)

### Poetry 시리즈 (`Engineering/DevOps/Poetry/`)
- 01: Poetry 소개
- 02: 설치
- 03: 의존성 관리 (add, remove, update, lock)
- 04: 가상환경 (install, run, shell, env)
- 05: pyproject.toml 상세
- 06: 빌드와 배포 (build, publish)
- 07: 설정과 고급 명령어 (config, source, cache, plugin)
- 08: 도구 비교 (pip, Conda, Pipenv, PDM)
- 09: CI/CD와 Docker 통합
- 10: 트러블슈팅
- 11-17: 외부 Git 패키지 통합 실전 사례

## Commands

```bash
# 로컬 미리보기
quarto preview

# 빌드
quarto render

# Git 커밋 시 Co-Authored-By 포함
```

## Key Files

- `_quarto.yml` — 프로젝트 설정, navbar, sidebar
- `docs/blog/posts/_metadata.yml` — 포스트 공통 설정 (댓글, TOC, 배너, 날짜형식)
- `styles.css` — 커스텀 CSS
- `theme.scss` / `theme-dark.scss` — 테마 정의
- `blog_requirements.txt` — Python 의존성
