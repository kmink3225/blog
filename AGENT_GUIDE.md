---
name: AGENT_GUIDE
type: router
version: 7.0
last_updated: 2026-03-28
changelog: "v7.0 (2026-03-28): 슬래시 커맨드 라우팅 도입. 공통 규칙을 guides/AGENT_GUIDE_CORE.md로 분리. AGENT_GUIDE.md는 순수 라우터로 전환."
description: >
  슬래시 커맨드 라우터. 사용자가 명령어를 입력하면 해당 태스크에 필요한 가이드만 로드한다.
  공통 규칙은 guides/AGENT_GUIDE_CORE.md에 있다 — 모든 태스크에서 반드시 먼저 로드한다.
scope: global
---

# AGENT_GUIDE.md — Copilot CLI 진입점

> **Copilot CLI 전용 래퍼.** 모든 공통 규칙은 `guides/AGENT_GUIDE_CORE.md`에 있다.
> 작업 시작 전 반드시 `guides/AGENT_GUIDE_CORE.md`를 먼저 읽어라.
>
> Claude Code 사용자는 `CLAUDE.md`를 참조한다.

---

## 로드 원칙


모든 태스크에서 **반드시 `conda activate blog` & `guides/AGENT_GUIDE_CORE.md` 를 가장 먼저 로드**한다.  
그 후 아래 슬래시 커맨드에 매핑된 가이드만 추가로 로드한다.

```
사용자 입력
    ↓
conda activate blog
    ↓    
guides/AGENT_GUIDE_CORE.md 로드 (항상)
    ↓
슬래시 커맨드 파싱 → 매핑 테이블 조회
    ↓
해당 skill 가이드 + category GUIDE만 로드
    ↓
실행
```

**슬래시 커맨드가 없으면**: 자연어로 태스크 유형을 추론하여 아래 표의 가장 적합한 행을 선택한다.

---

## 슬래시 커맨드 정의

| 명령어 | 태스크 | 로드할 가이드 (CORE 제외) |
|--------|--------|--------------------------|
| `/write [category] [topic]` | **새 포스트 작성** — 3-Layer 탐색 → 중복 판단 → .qmd 신규 작성 → index.qmd 링크 추가 → 렌더링 → 배포 | `guides/info-search.md` + `guides/write-post.md` + `docs/blog/posts/{category}/GUIDE.md` |
| `/fix [file-path]` | **기존 포스트 교정** — 지정 파일의 YAML·한다체·수식·구조를 현행 규칙에 맞게 직접 수정 (내용 삭제 금지) | `guides/retrofit-post.md` + `docs/blog/posts/{category}/GUIDE.md` |
| `/qa [question]` | **질문 답변** — 블로그→교재→사전지식 3-Layer 탐색 후 통합 답변 (파일 변경 없음) | `guides/info-search.md` + `guides/answer-question.md` |
| `/convert [category]` | **TBD 메모→정식 포스트 전환** — TBD.qmd의 임시 메모를 정식 .qmd로 분리·재작성 → index 업데이트 | `guides/info-search.md` + `guides/convert-tbd.md` + `docs/blog/posts/{category}/GUIDE.md` |
| `/series [category]` | **시리즈 재구성** — 카테고리 내 기존 .qmd 파일들의 중복·누락·순서 진단 → 파일 병합/분할/번호 재배치 → index.qmd 반영 | `guides/info-search.md` + `guides/organize-series.md` + `docs/blog/posts/{category}/GUIDE.md` |
| `/audit [file-path]` | **품질 감사 (읽기 전용)** — 지정 파일의 추상적 서술·누락 섹션·규칙 위반을 진단·보고만 함 (파일 수정 안 함) | `guides/audit.md` + `docs/blog/posts/{category}/GUIDE.md` |
| `/log` | **변경 이력 요약** — git 히스토리에서 .qmd 생성/수정/삭제 이력을 기간별로 조회·보고 (파일 변경 없음) | `guides/changelog-summary.md` |
| `/reindex [category]` | **index.qmd 재편성** — 카테고리 내 모든 .qmd 메타데이터를 읽고 논리적 그룹핑·순서로 index.qmd를 재작성 | `guides/reorganize-index.md` + `docs/blog/posts/{category}/GUIDE.md` |
| `/algo [track] [problem]` | **Python 알고리즘 튜터** — AIE/DS 트랙 Level 1~5 문제를 대화식으로 풀이 → 세션을 .qmd 포스트로 저장 | `guides/algo-tutor.md` + `docs/blog/posts/Code_Test/GUIDE.md` |
| `/sql [problem]` | **SQL 코딩 테스트 튜터** — Programmers Level 1~5 문제를 평가·교정·해설 → 세션을 .qmd 포스트로 저장 | `guides/sql-tutor.md` + `docs/blog/posts/Code_Test/GUIDE.md` |
| `/publish` | **배포** — 변경된 .qmd를 HTML 렌더링 → git add (.qmd + _site/ + _freeze/) → commit → push → 충돌 해결 | `guides/publish.md` |

### 커맨드별 사용 예시

| 명령어 | 예시 |
|--------|------|
| `/write` | `/write Statistics continuous distributions` |
| `/fix` | `/fix Statistics/22-mle.qmd` |
| `/qa` | `/qa 포아송과 음이항의 차이는?` |
| `/convert` | `/convert Statistics` |
| `/series` | `/series Statistics` |
| `/audit` | `/audit Statistics/56-common-families-discrete.qmd` |
| `/log` | `/log` |
| `/reindex` | `/reindex Statistics` |
| `/algo` | `/algo AIE Level 3 DFS 문제 풀자` |
| `/algo` | `/algo DS Level 2 정렬 연습` |
| `/sql` | `/sql Programmers SELECT Level 1 문제 풀자` |
| `/publish` | `/publish` |

### `/fix` vs `/audit` 차이

| | `/fix` | `/audit` |
|---|---|---|
| 동작 | 형식·구조·내용을 **직접 수정** | 문제점을 **진단·보고만** |
| 파일 변경 | O | X (사용자가 결정) |
| 언제 쓰나 | 수정이 필요한 게 확실할 때 | 먼저 뭐가 문제인지 파악하고 싶을 때 |

### 커맨드별 로드 비교

```
/write Statistics discrete distributions
  → CORE + info-search + write-post + Statistics/GUIDE.md
  → 로드 안 함: retrofit, audit, changelog, organize-series, ...

/qa 포아송 분포란?
  → CORE + info-search + answer-question
  → 로드 안 함: write-post, retrofit, audit, category GUIDE, ...

/fix Statistics/22-mle.qmd
  → CORE + retrofit-post + Statistics/GUIDE.md
  → 로드 안 함: info-search(전체), write-post, changelog, ...

/log
  → CORE + changelog-summary
  → 로드 안 함: 모든 skill/category 가이드

/algo AIE Level 3 DFS
  → CORE + algo-tutor + Code_Test/GUIDE.md
  → 로드 안 함: write-post, info-search, sql-tutor, ...

/sql Programmers JOIN Level 2
  → CORE + sql-tutor + Code_Test/GUIDE.md
  → 로드 안 함: write-post, info-search, algo-tutor, ...

/publish
  → CORE + publish.md
  → 로드 안 함: 모든 content/category 가이드
```

**슬래시 커맨드가 없으면**: 자연어로 태스크 유형을 추론하여 위 표의 가장 적합한 행을 선택한다. 다만 커맨드 명시가 더 빠르고 정확하다.

---

## 카테고리 목록

`{category}` 자리에 아래 폴더명을 사용한다.

| 폴더명 | 주제 |
|--------|------|
| `Statistics` | 분포, 검정, 회귀, 종단분석, FDA |
| `Math` | 선형대수, 미적분, 최적화 |
| `Machine_Learning` | 분류, 회귀, 앙상블, 비지도학습 |
| `Deep_Learning` | CNN, RNN, Transformer, NLP |
| `Experimentation` | A/B Test, 인과추론, MAB |
| `Engineering` | DevOps, Python, Infra |
| `Agent` | RAG, LangChain, LangGraph |
| `Data_Science` | CRISP-DM, EDA, Feature Engineering |
| `Governance` | 데이터 거버넌스, 품질 |
| `Strategy_Frameworks` | 비즈니스 분석, 전략 |
| `Code_Test` | 알고리즘, SQL |
| `Surveilance` | 의료기기 규제, FDA/EMA |

---

## 규칙 우선순위

```
카테고리 GUIDE.md  >  guides/AGENT_GUIDE_CORE.md  >  에이전트 자체 판단
```

---

## Project Info

- **Site**: https://kk3225.netlify.app
- **Author**: Kwangmin Kim
- **Stack**: Quarto → Netlify
- **Commands**: `quarto preview` / `quarto render`
- **Key Files**: `_quarto.yml`, `docs/blog/posts/_metadata.yml`
