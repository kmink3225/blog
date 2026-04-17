# MINERVA 도메인 분류기 시리즈 — 퇴고 Handoff

**작성일**: 2026-04-17 (금)
**다음 세션**: 2026-04-20 (월) 예정
**상태**: 1편·2편 주요 개념 교정 반영 완료. 3~7편 본문 전면 점검 미진행.
**파일명 `_` 접두사**: Quarto 렌더 대상 제외.

---

## 이번 세션(4-17) 교정 요약 — 리콜용

### 개념적 오류 → 수정된 내용

1. **하이브리드 엔진 순서** (1편)
   - (잘못) Rule → ML → RAG
   - (맞음) **ML(분류) → RAG(영문 번역) → Rule(약어 축약) → RAG(최종 검토)**

2. **"완전한 결정론은 아니다"** (1편)
   - → **"데이터 기반(data-driven), 확률 분포 출력, argmax 결정은 deterministic"**
   - Rule vs ML 대조축은 "결정론 여부"가 아니라 "명시 규칙 vs 통계 학습"

3. **"실데이터 26.4%"** (1편·2편)
   - → **전체 7,698건 모두 합성**. 실데이터 없음.
   - LLM 37.3% + 규칙 36.4% + **RAG grounded 생성 26.4%**
   - RAG는 표준화 원칙 문서에 grounded된 엄밀한 합성 경로 (edge case 포함)

4. **"다중공선성은 정확한 근거가 아니다"** (2편)
   - → **사용자 직관이 정확**. 다중공선성 확장하여 **dominant signal + redundancy + noise** 프레임으로.
   - 도메인명이 dominant, 메타데이터는 중복(redundant) + 노이즈
   - "메타데이터 granularity가 도메인명보다 거침" (`DATE`는 `일자/분/초` 구분 불가)

5. **"Label Leakage"** (2편, 1편·6편 연동) — **완전 제거**
   - 진짜 이유는 **서비스 스키마 불일치** (추론 시 메타데이터 비가용)
   - X-y 상관은 설명력(explanatory power)이지 leakage가 아님
   - 2편 line 158에 "설명력 ≠ leakage" 명시 문장 유지 (선제 반박용)

### 기타 수정
- `일반 → 일반단어` 라벨 정규화 설명 과도하게 장황 → 사용자가 직접 축약
- README "149~635" 수치 언급 → 사용자 삭제 (README 이미 463~634로 갱신됨)
- 1편 코드 블록 이모지 안 씀, 씨젠 회사명 일괄 제거 완료

### 반복된 실수 패턴 (재발 방지용)
- Task 자체 구조 분석을 건너뛰고 ML 문헌의 **유명 용어 association**으로 그럴싸한 프레임 선점
- 유사 컬럼명·맥락만 보고 Label Leakage 같은 강한 개념을 끼워맞춤
- **원칙**: 정제된 입력·엄밀한 용어. 유명 용어는 정의에 정확히 해당할 때만 사용. 모르면 1차 원리(signal-to-noise, 설명력, 추론 가용성)로 돌아가 task 구조부터 분해.

---

## 월욜 이어서 할 작업 — 점검 대상

### 각 편 미점검 상태
- **3편** 모델 후보 선정 — 본문 전체 미점검
- **4편** 실험 설계 — 본문 전체 미점검
- **5편** 결과 분석·통계 검증 — 본문 전체 미점검
- **6편** Task 재정의 — Label Leakage 언급 1곳만 교체, 본문 전체 재검토 필요
- **7편** 배포 의사결정 — 본문 전체 미점검

### 점검 시 의심해야 할 패턴

| 의심 패턴 | 체크 방법 |
|---|---|
| 일반화·추상화된 ML 용어 오용 | "leakage", "overfitting", "bias/variance", "scaling", "ensemble" 같은 단어가 **정확히** 해당하는지 |
| 하이브리드 엔진 순서 옛 프레임 | 각 편에서 Rule Layer를 엔진 초입이나 ML 뒤에 두는 서술 남아 있나 |
| "합성 vs 실데이터" 옛 프레임 | "RAG 실데이터", "합성 73.6% 의존의 대가" 같은 표현 |
| EXP-1~6 실측과 서술 불일치 | HANDOFF(data_standardization) ⭐⭐ 섹션 수치와 대조 |
| 유사 컬럼명에 강한 프레임 끼워맞춤 | "왜 이 용어를 썼는지" 1차 원리로 재검토 |

### 2편 내 추가 개선 후보 (이번 세션 스코프 밖이었음)
- **"합성 73.6% 의존의 대가 — 06편 복선"** 섹션 전체 프레임 — 이제 "실데이터 대비 합성"이 아니라 "경로별 grounded 수준 차이"라 복선 재구성 필요
- "설명 컬럼 예외" 섹션의 "RAG 실데이터 2,030건에서 설명 결측률" → "RAG 경로"로 용어 조정
- grep으로 "실데이터", "합성 73.6%" 잔존 확인

### 6편은 특히 주의
- 클라이맥스 편이라 "실데이터 강건성", "합성 과적합 기각" 서사가 전체 관통
- RAG가 합성임을 전제로 재작성해야 논리 일관

---

## 참조 경로

| 대상 | 경로 |
|---|---|
| 시리즈 파일 | `docs/blog/posts/Data_Science/minerva-domain-classifier/minerva-0[1-7]-*.qmd` |
| 시리즈 index | `docs/blog/posts/Data_Science/index.qmd` |
| 실험 HANDOFF (실측 결과) | `C:\Users\kmkim\Desktop\projects\data_standardization\notebooks\domain_classification\HANDOFF.md` (⭐⭐ 섹션) |
| 블로그 메모리 (규칙) | `~/.claude/projects/C--Users-kmkim-Desktop-projects-blog/memory/` |
| MINERVA 아키텍처 | `C:\Users\kmkim\Desktop\SG_Projects\minerva\data\docs\architecture\project-overview.md` |

## 최근 커밋 히스토리 (최신 순)

- `3ae3fd89` — 2편 핵심 재구성 (Label Leakage 삭제 + 서비스 스키마 승격 + redundancy+noise 확장 + 4축 정리)
- `b5a08b58` — 7편 최초 배포
- `c7857184` — 6편 최초 배포
- `aadcc2a4` — 5편 최초 배포
- `9ac21459` — 4편 최초 배포
- `c49299db` — 3편 최초 배포
- `d8582582` — 2편 최초 배포
- `793c70f5` — 1편 최초 배포

## 세션 시작 시 프롬프트 예시

> "minerva-domain-classifier 시리즈 퇴고 이어서 한다. `_revision-notes.md` 먼저 읽고, 3편부터 본문 읽어보며 의심 지점 잡으면 알려달라."
