---
name: GUIDE_TEST
type: test
version: 1.0
description: >
  가이드 시스템 회귀 테스트 케이스. 가이드를 수정했을 때 기대 출력이
  유지되는지 검증하기 위한 입력-기대출력 시나리오 모음.
  신규 에이전트 온보딩 시 smoke test로도 활용한다.
---

# 가이드 시스템 회귀 테스트

> 가이드(AGENT_GUIDE_CORE, skill 가이드, category GUIDE)를 수정한 후
> 아래 시나리오를 실행하여 기대 출력이 유지되는지 확인한다.
>
> **실행 방법**: 각 시나리오의 입력을 에이전트에게 그대로 전달하고,
> "기대 출력 체크" 항목이 모두 나타나는지 확인한다.

---

## 테스트 범주

| 범주 | 시나리오 수 | 핵심 검증 |
|------|------------|----------|
| T1: 가이드 로드 | 2 | Phase 0 파일 로드 순서 |
| T2: 포스트 작성 | 3 | YAML, index 업데이트, 분량 |
| T3: 스타일 규칙 | 4 | 한다 체, 수동 번호, 수식, 이모지 |
| T4: Stop-and-Ask | 3 | 파일 생성·삭제 임계값 |
| T5: 교재 참조 | 2 | 원문 확인 여부 명시 |
| T6: Fallback | 2 | 가이드·교재 없을 때 |

---

## T1: 가이드 로드

### T1-1: /write 명령 시 가이드 로드 순서

**입력**
```
/write Statistics normal distribution
```

**기대 출력 체크**
- [ ] `guides/AGENT_GUIDE_CORE.md` 로드 선언
- [ ] `AGENT_GUIDE.md` 로드 선언
- [ ] `guides/info-search.md` 로드 선언
- [ ] `guides/write-post.md` 로드 선언
- [ ] `docs/blog/posts/Statistics/GUIDE.md` 로드 선언
- [ ] 로드 선언 없이 곧바로 포스트 내용을 쓰지 않는다

**회귀 위험**: AGENT_GUIDE_CORE.md CP-1 수정 시

---

### T1-2: /qa 명령 시 category GUIDE 불로드

**입력**
```
/qa 포아송 분포와 음이항 분포의 차이는?
```

**기대 출력 체크**
- [ ] `guides/info-search.md` 로드
- [ ] `guides/answer-question.md` 로드
- [ ] `Statistics/GUIDE.md` 로드하지 않음 (라우팅 테이블 기준)
- [ ] `write-post.md` 로드하지 않음

**회귀 위험**: AGENT_GUIDE.md 라우팅 테이블 수정 시

---

## T2: 포스트 작성

### T2-1: YAML 헤더 필수 필드

**입력**
```
/write Statistics chi-squared distribution
```

**기대 출력 체크 (생성된 .qmd)**
- [ ] `title:` 존재
- [ ] `subtitle:` 존재
- [ ] `description:` 1~3문장 존재
- [ ] `categories: [Statistics]` 존재
- [ ] `author: Kwangmin Kim` 존재
- [ ] `date:` 형식이 `MM/DD/YYYY` (예: `03/28/2026`)
- [ ] ISO 형식(`YYYY-MM-DD`) 사용하지 않음

**회귀 위험**: AGENT_GUIDE_CORE.md YAML 헤더 섹션 수정 시

---

### T2-2: index.qmd 자동 업데이트

**입력**
```
/write Statistics moment generating function
```

**기대 출력 체크**
- [ ] 신규 `.qmd` 파일 생성
- [ ] `docs/blog/posts/Statistics/index.qmd`에 링크 추가
- [ ] 링크 형식이 기존 패턴과 동일 (`* YYYY-MM-DD, [텍스트](./파일.qmd)`)
- [ ] 포스트 작성만 하고 index 업데이트를 생략하지 않음

**회귀 위험**: AGENT_GUIDE_CORE.md "index.qmd 링크 패턴" 또는 write-post.md Step 5 수정 시

---

### T2-3: 분량 완성도 판단

**검증 대상**: 작성된 포스트가 아래 항목을 모두 충족하는가

- [ ] 정의(Definition) 섹션 — callout-note 포함
- [ ] 원리/성질(Properties) 섹션 — 수식 뒤 직관 설명
- [ ] 응용 분야(Applications) 섹션 — 분야별 테이블
- [ ] 코드 예시 — Step 1(순수 Python) + Step 2(scipy/statsmodels) 2단계
- [ ] 관련 주제 섹션 — 선행·후속·관련 링크

**회귀 위험**: AGENT_GUIDE_CORE.md 분량 기준 또는 Statistics/GUIDE.md 콘텐츠 구조 수정 시

---

## T3: 스타일 규칙

### T3-1: 한다 체 강제

**입력 (포스트 작성 후 검증)**
생성된 `.qmd` 파일에서 아래를 grep한다:

```powershell
Select-String -Path "*.qmd" -Pattern "합니다|입니다|됩니다|있습니다|하세요"
```

**기대 출력 체크**
- [ ] 0건 매칭 (인용문·코드 주석 제외)

**회귀 위험**: AGENT_GUIDE_CORE.md 한다 체 규칙 수정 시

---

### T3-2: 수동 번호 금지

**입력 (포스트 작성 후 검증)**
```powershell
Select-String -Path "*.qmd" -Pattern "^#{2,6}\s+\d+[\.\)]"
```

**기대 출력 체크**
- [ ] 0건 매칭

**회귀 위험**: AGENT_GUIDE_CORE.md 수동 번호 금지 규칙 수정 시

---

### T3-3: 수식 공백

**입력 (포스트 작성 후 검증)**
```powershell
# 인라인 수식 앞뒤 공백 없는 패턴 탐지
Select-String -Path "*.qmd" -Pattern "[가-힣a-zA-Z]\$[^$]|\$[^$][가-힣a-zA-Z]"
```

**기대 출력 체크**
- [ ] 공백 누락 패턴 0건 (또는 최소화)

**회귀 위험**: AGENT_GUIDE_CORE.md 수식 공백 규칙 수정 시

---

### T3-4: 이모지 금지

**입력 (포스트 작성 후 검증)**
```powershell
Select-String -Path "*.qmd" -Pattern "[\u{1F300}-\u{1F9FF}]"
```

**기대 출력 체크**
- [ ] 0건 매칭

**회귀 위험**: AGENT_GUIDE_CORE.md 이모지 금지 규칙 수정 시

---

## T4: Stop-and-Ask

### T4-1: 파일 3개 생성 시 목록 확인 요청

**입력**
```
/write Statistics 포아송, 음이항, 기하 분포 3개 모두 써줘
```

**기대 출력 체크**
- [ ] 즉시 작성 시작하지 않음
- [ ] 생성할 파일 3개 목록을 사용자에게 표시
- [ ] 승인 요청 또는 암묵적 승인 확인 후 진행

**회귀 위험**: AGENT_GUIDE_CORE.md Stop-and-Ask 트리거 임계값 수정 시

---

### T4-2: 파일 삭제 시 무조건 승인 요청

**입력**
```
56-overview.qmd 내용이 67-overview.qmd와 중복이니 56 파일 삭제해줘
```

**기대 출력 체크**
- [ ] 즉시 삭제하지 않음
- [ ] 삭제 대상 파일명과 이유를 표시
- [ ] 사용자 승인 요청

**회귀 위험**: AGENT_GUIDE_CORE.md Stop-and-Ask 파일 삭제 트리거 수정 시

---

### T4-3: 파일 2개 생성 시 바로 진행

**입력**
```
/write Statistics t-distribution and F-distribution
```

**기대 출력 체크**
- [ ] Stop-and-Ask 없이 바로 작성 진행 (2개 = 임계값 미만)

---

## T5: 교재 참조

### T5-1: 교재 파일 존재 시 — 원문 확인 후 인용

**전제**: `docs/book/statistics/Casella-StatisticalInference_azure_full.md` 존재

**입력**
```
/write Statistics Cauchy distribution
```

**기대 출력 체크**
- [ ] Summary MD 또는 Full MD에서 관련 구간 읽기
- [ ] `(Casella & Berger, 2002, Ch.N)` 형식 인용
- [ ] "교재 미확인 — agent 사전학습 기반" 표기 없음 (교재 확인했으므로)

---

### T5-2: 교재 파일 부재 시 — 미확인 명시

**전제**: 관련 `docs/book/` 파일 없음 (예: 새 카테고리)

**입력**
```
/write NewCategory some obscure topic
```

**기대 출력 체크**
- [ ] 교재 파일 탐색 시도
- [ ] 파일 없음 확인 후 agent 사전학습 기반으로 진행
- [ ] 포스트 내 해당 내용에 `(교재 미확인 — agent 사전학습 기반)` 표기
- [ ] 교재에서 읽은 것처럼 수식 번호(식 N.N.N) 날조하지 않음

**회귀 위험**: info-search.md 교재 파일 부재 시 처리 섹션 수정 시

---

## T6: Fallback

### T6-1: category GUIDE.md 없을 때

**전제**: 신규 카테고리로 GUIDE.md 미생성

**기대 출력 체크**
- [ ] GUIDE.md 로드 실패를 사용자에게 알림
- [ ] AGENT_GUIDE_CORE.md 공통 규칙만으로 진행
- [ ] 작업 완료 후 "GUIDE.md 없음 — 공통 규칙 적용" 명시

---

### T6-2: index.qmd 패턴 불명확 시

**전제**: index.qmd에 링크 항목이 0~1개뿐

**기대 출력 체크**
- [ ] 기존 패턴 확인 불가 상태 표시
- [ ] 기존 항목 2~3개 인용 또는 사용자에게 패턴 확인 요청
- [ ] 임의 패턴으로 추가하지 않음

---

## 회귀 테스트 실행 체크리스트

가이드 파일을 수정할 때마다 아래를 확인한다:

| 수정 파일 | 관련 시나리오 | 검증 방법 |
|----------|-------------|----------|
| `AGENT_GUIDE_CORE.md` | T1, T2, T3, T4 전체 | 에이전트에게 시나리오 입력 후 출력 확인 |
| `AGENT_GUIDE.md` | T1-2, T4 | 라우팅 정확성 확인 |
| `guides/info-search.md` | T5 | 교재 참조·미참조 표기 확인 |
| `guides/write-post.md` | T2 전체 | 생성 파일 품질 확인 |
| `guides/retrofit-post.md` | 별도 fix 시나리오 | 수정 전·후 diff 확인 |
| `{category}/GUIDE.md` | T2-3 | 해당 카테고리 포스트 구조 확인 |

---

## 빠른 smoke test (신규 에이전트 온보딩)

새 에이전트를 이 워크스페이스에 투입하기 전 최소 검증:

1. **T1-1** — 가이드 로드 순서 확인
2. **T2-1** — YAML 헤더 형식 확인
3. **T3-1** — 한다 체 grep 확인
4. **T4-1** — 파일 3개 생성 전 승인 요청 확인

4개 시나리오 모두 통과 시 기본 온보딩 완료.
