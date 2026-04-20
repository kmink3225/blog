# MINERVA 도메인 분류기 시리즈 — 퇴고 Handoff

**작성일**: 2026-04-17 (금), 2026-04-20 (월) 갱신
**다음 세션**: 2026-04-21 (화) 이후 예정
**상태**: 1~3편 주요 개념·표현 교정 완료. 시리즈 일괄 용어 치환 완료. 4~7편 본문 전면 점검 미진행 (일부만 부분 교정).
**파일명 `_` 접두사**: Quarto 렌더 대상 제외.

---

## 2026-04-20 (월) 세션 — 수행 요약

### A. 2편 개념 프레임 전면 재정립 (이어서 완료)

1. **RAG 설계 의도 재정의** — 기존 "RAG 실데이터 추출" 프레임은 완전 오류. 정정:
   - RAG는 표준화 원칙 문서를 split·Vector DB 인덱싱 후 매 쿼리마다 연관 split 문서 retrieval → **엄밀한 원칙 준수 합성**
   - 규칙의 gray zone edge case 생성도 이 경로에서 담당
   - 전체 7,698건 모두 합성 (실데이터 없음)
2. **3경로 상보성 프레임** — "규칙 합성 / LLM 멀티턴 / RAG grounded"의 실패 모드 3각 구조:
   - 규칙: 기계적 고정 → 실사용 어휘 밖 섞임
   - LLM 멀티턴: lost-in-the-middle·attention 희석으로 원칙 준수 느슨 → 현실 사용자 입력 변이를 닮음 (의도적 포함)
   - RAG grounded: 원칙 준수 쏠림 → 사용자 불완전 숙지 케이스 재현 못 함
3. **"합성 73.6% 의존의 대가" 섹션 재구성** — "실데이터 vs 합성" 이분법 폐기. "경로별 grounded 차이 + 느슨 경로 템플릿 암기 리스크"로 재프레임. 실험 1을 "경로 간 일반화 갭 정량화"로 재해석.
4. 수정 위치 (2편): line 6(YAML), 48(표), 55(실패 모드), 63~65(로직 요약), 73(라벨), 204, 248~294(복선 섹션)

### B. 3편 신규 점검

1. **BiLSTM "왜 후보에 포함했는가"의 3가지 이유 상세 보강**:
   - Absolute floor baseline (Transformer·SP 토크나이저·한국어 corpus 사전학습 3축 분리)
   - **CPU 배포 실용성 프레임 정정** — "CPU 가능/불가능 이분법"은 과한 프레임. 실제는 latency·throughput·memory footprint 규모 차이
   - char-level OOV 회피 (영문+숫자+한글 혼재, 오타·표기 변이 robustness)
2. **사후 실험 일람 신설** — 03편 `## 사후 통합` 섹션 바로 아래 `### 사후 실험 일람` 표 (6개 실험 × 질문 × 결과).
3. 수정 위치 (3편): BiLSTM 섹션 (line 93~97), 사후 실험 일람 (line 241 직후)

### C. 5편 부분 교정

1. **Macro F1 ≈ Weighted F1의 수리적 유도 추가** — line 34~38에 수식 + $n_k/N \approx 1/K$ 균형 조건에서 수렴하는 수학적 필연 명시.

### D. 7편 부분 교정

1. **사후 실험 일람 추가** — `## 이 편의 위치` 바로 아래 `## 사후 실험 일람` (03편과 동일 표).

### E. 01편 간단 등재

1. **사후 실험 6종 한눈에** — line 209 직전에 bullet 6줄로 각 실험 역할 요약.

### F. 시리즈 일괄 작업

1. **용어 치환**: `EXP-1`~`EXP-8` → `실험 1`~`실험 8` (7개 편 sed 일괄). 이어 공백 정리(`실험1` → `실험 1`).
2. **"면접/상사" 상황 수사 제거** — 13곳:
   - 02편 line 246, 320
   - 03편 YAML, line 29, 61, 90, 138, 154
   - 05편 line 231
   - 07편 line 129, 153, 175, 207
   - 중립 표현으로 치환: "~라는 의문이 들 때", "~라는 의구심이 제기될 때", "엄밀한 근거 평가를 통과하는", "선택·탈락 근거 요약" 등
   - 메모리 저장: `feedback_rhetorical_framing.md`
3. **실험 번호 체계 확정**: 실험 1=RAG holdout, 2=접미사, 3=per-source 오류, 4=일반단어 noise floor, 5=K-Fold, 6=Latency (노트북 21~25, 20 대응)
4. **실험 3 누락 발견** — `23_per_source_error_analysis.ipynb`에 정의되어 있으나 블로그 본문에 언급 0건이었음. 01·03·07편 일람에 모두 등재 완료. **단, 06편 본문에는 실험 3 섹션 신규 작성 미진행** (아직 일람에만 등록됨).

### G. 기타 메모리 갱신

- `feedback_rhetorical_framing.md` 신규 저장 (상황 수사 금지)
- MEMORY.md index 갱신

---

## 반복된 실수 패턴 (재발 방지용)

- ML 유명 용어의 반사적 association ("Label Leakage", "GPU 전제", "실데이터 vs 합성")으로 그럴싸한 프레임 먼저 선점 → 사용자가 task 실제 구조로 교정
- 성능 주장에서 **이분법적 프레임** (CPU 가능/불가능) 대신 **스펙트럼·규모** (latency·throughput·memory)로 가야 함
- **원칙**: 정제된 입력·엄밀한 용어. 유명 용어는 정의에 정확히 해당할 때만 사용. 1차 원리(signal-to-noise, 설명력, 추론 가용성, 규모 스펙트럼)로 돌아가 task 구조부터 분해.

---

## 남은 작업 — 2026-04-21 이후

### 높은 우선순위

- **06편 본문에 실험 3 섹션 신규 작성** — `23_per_source_error_analysis.ipynb` 내용 기반. 실험 1과 실험 4 사이에 배치. 핵심 결론:
  - 약한 그룹(KLUE+ALBERT): 합성 오답률 3.24%, RAG 오답률 5.14% → 합성 특화 성향
  - 강한 그룹(나머지 6개): 합성 6.65%, RAG 4.52% → RAG 친화
  - KLUE+ALBERT 동시 오답 ∧ 다른 모델 정답 = 9건(RAG 428건 중), 그중 18.2%가 `일반단어`
  - 실험 4(일반단어 제외)와 자연스럽게 연결
- **06편 실험 1 섹션의 미묘한 보정** — 현재 "완전 기각"으로 단순 결론. 실험 3과 함께 읽으면 "과적합은 없으나 KLUE/ALBERT는 약간 합성 친화"라는 세밀한 그림이 필요. 실험 1 결론부에 실험 3으로의 연결 한 줄 추가 권장.

### 중간 우선순위 — 본문 전면 점검 미진행

- **4편** 실험 설계 — 본문 전체 미점검
- **5편** 통계 검증 — 수식 추가 외 미점검
- **6편** Task 재정의 — 실험 1~4 언급만 부분 교정, 본문 전체 재검토 필요
- **7편** 배포 의사결정 — 사후 실험 일람 외 미점검

### 점검 시 의심할 패턴 (2026-04-17 한 목록 유지)

| 의심 패턴 | 체크 방법 |
|---|---|
| 일반화·추상화된 ML 용어 오용 | "leakage", "overfitting", "bias/variance", "scaling", "ensemble"이 정확히 해당하는지 |
| 실험 간 결론의 단순화 ↔ 세밀화 갭 | 실험 1·3 같이 서로 보정하는 쌍이 동시에 서술되는지 |
| 이분법적 프레임 잔존 | "CPU 가능/불가능", "합성 vs 실데이터", "결정론 vs 확률적" 같은 단순 대비가 규모 스펙트럼으로 바뀌어 있나 |
| 인물·상황 수사 재등장 | "면접", "상사", "감사 자리에서" 같은 표현 grep |
| EXP 번호 표기 잔존 | `grep "EXP"` 0건 유지 |

### 2편 관련 잔여 (이전 notes 유지)

- grep으로 "RAG 실데이터", "합성 73.6%", "EXP-" 잔존 모두 0 확인 완료 (2026-04-20)

---

## 참조 경로

| 대상 | 경로 |
|---|---|
| 시리즈 파일 | `docs/blog/posts/Data_Science/minerva-domain-classifier/minerva-0[1-7]-*.qmd` |
| 시리즈 index | `docs/blog/posts/Data_Science/index.qmd` |
| 실험 HANDOFF (실측 결과) | `C:\Users\kmkim\Desktop\projects\data_standardization\notebooks\domain_classification\HANDOFF.md` (⭐⭐ 섹션) |
| **실험 노트북 (번호 매핑)** | `C:\Users\kmkim\Desktop\projects\data_standardization\notebooks\domain_classification\` |
| ↳ 실험 1 RAG holdout | `21_rag_holdout_eval.ipynb` |
| ↳ 실험 2 접미사 ablation | `22_suffix_ablation.ipynb` |
| ↳ 실험 3 per-source 오류 | `23_per_source_error_analysis.ipynb` |
| ↳ 실험 4 일반단어 noise floor | `24_general_word_noise_floor.ipynb` |
| ↳ 실험 5 K-Fold CV | `25_kfold_cv.ipynb` |
| ↳ 실험 6 Latency (+ 전체 비교) | `20_model_comparison.ipynb` |
| 블로그 메모리 (규칙) | `~/.claude/projects/C--Users-kmkim-Desktop-projects-blog/memory/` |
| MINERVA 아키텍처 | `C:\Users\kmkim\Desktop\SG_Projects\minerva\data\docs\architecture\project-overview.md` |

---

## 최근 커밋 히스토리 (최신 순 — 2026-04-17 기준, 2026-04-20 신규 커밋 없음)

- `3ae3fd89` — 2편 핵심 재구성 (Label Leakage 삭제 + 서비스 스키마 승격 + redundancy+noise 확장 + 4축 정리)
- `b5a08b58` — 7편 최초 배포
- `c7857184` — 6편 최초 배포
- `aadcc2a4` — 5편 최초 배포
- `9ac21459` — 4편 최초 배포
- `c49299db` — 3편 최초 배포
- `d8582582` — 2편 최초 배포
- `793c70f5` — 1편 최초 배포

2026-04-20 세션 산출물은 아직 커밋 전. 1·2·3·5·7편 + 01편·01편·MEMORY.md에 변경사항 존재. 다음 세션 시작 시 `git status`로 확인.

---

## 세션 시작 시 프롬프트 예시

> "minerva-domain-classifier 시리즈 퇴고 이어서 한다. `_revision-notes.md` 먼저 읽고, 우선 06편 실험 3 섹션 신규 작성부터. 이어 4·5·6·7편 본문 전면 점검 들어간다."
