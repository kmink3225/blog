---
name: "Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing"
type: book-summary
source_file: "Kohavi-ABTesting_full.md"
authors: "Ron Kohavi, Diane Tang, Ya Xu"
year: 2020
total_pages: 250
language: en
keywords: [AB-testing, online-experiments, OEC, metrics, statistical-significance, SRM, triggering, experimentation-platform, causal-inference]
---

# Trustworthy Online Controlled Experiments — Summary

> Ron Kohavi, Diane Tang, Ya Xu (2020), ~250pp, 23 chapters in 5 parts
> A/B 테스팅의 설계·실행·분석·확장을 위한 실무 가이드이다

## Contents

- Part I: Introductory Topics for Everyone
  - Experimentation fundamentals, segment differences, Simpson's Paradox, platform & culture
- Part II: Selected Topics for Everyone
  - Ch 5-9: Speed matters, Organizational metrics, Metrics for experimentation & OEC, Institutional memory, Ethics
- Part III: Complementary and Alternative Techniques
  - Ch 10: Complementary Techniques (logs, human evaluation, UER, surveys)
  - Ch 11: Observational Causal Studies
- Part IV: Advanced Topics — Building an Experimentation Platform
  - Ch 12: Client-Side Experiments
  - Ch 13: Instrumentation
  - Ch 14: Choosing a Randomization Unit
  - Ch 15: Ramping Experiment Exposure
  - Ch 16: Scaling Experiment Analyses
  - Ch 17: Data Processing, Computation, Visualization
- Part V: Advanced Topics — Analyzing Experiments
  - Ch 18: The Statistics behind Online Controlled Experiments
  - Ch 19: Variance Estimation and Improved Sensitivity
  - Ch 20: The A/A Test
  - Ch 21: Triggering for Improved Sensitivity
  - Ch 22: Sample Ratio Mismatch and Trust-Related Guardrail Metrics
  - Ch 23: Leakage and Interference between Variants
  - Ch 24: Measuring Long-Term Treatment Effects

---

## Chapter Summaries

### Part I: Introductory Topics (pp. 1-70)
**핵심**: 과학적 방법을 통한 가설 검증, 통제 실험의 기본 구조(treatment/control), 핵심 지표 정의와 Overall Evaluation Criterion(OEC)의 개념을 소개한다. 세그먼트 차이와 Simpson's Paradox의 위험, 건전한 회의주의의 중요성을 강조한다. 실험 성숙도 모델과 인프라 요구사항을 개관한다.
**키워드**: `controlled-experiment`, `OEC`, `Simpsons-paradox`, `maturity-model`
**상세**: → source file Part I (line 797)

### Part II: Speed, Metrics, Ethics (pp. 79-123)
**핵심**: 웹사이트 성능이 사용자 참여에 미치는 영향을 end-to-end 사례로 분석한다. 조직 지표 분류(goal, driver, guardrail), 실험용 지표 공식화 원칙, OEC 구성 방법(Bing 검색, Amazon 이메일 사례)을 다룬다. Goodhart's Law와 Campbell's Law의 실무적 함의, 실험 윤리(데이터 수집, 사용자 식별, 문화)를 설명한다.
**키워드**: `latency`, `metrics-taxonomy`, `guardrail-metrics`, `Goodharts-law`, `ethics`
**상세**: → source file Part II (line 463)

### Part III: Complementary Techniques (pp. 125-147)
**핵심**: 로그 분석, 인간 평가, UX 리서치, 포커스 그룹, 설문, 외부 데이터 등 통제 실험을 보완하는 기법을 비교한다. 관찰적 인과 연구(observational causal studies)의 설계와 함정, 반박된 관찰 연구 사례를 분석한다.
**키워드**: `complementary-techniques`, `observational-study`, `UER`, `logs-analysis`
**상세**: → source file Part III (line 544)

### Part IV: Experimentation Platform (pp. 151-180)
**핵심**: 클라이언트 사이드 vs 서버 사이드 실험의 차이, 계측(instrumentation)의 원칙, 무작위 배정 단위(randomization unit) 선택, 실험 노출 확대(ramping)의 SQR 프레임워크, 대규모 분석 확장의 데이터 처리·계산·시각화를 다룬다.
**키워드**: `client-side`, `server-side`, `randomization-unit`, `ramping`, `SQR`
**상세**: → source file Part IV (line 565)

### Part V: Advanced Analysis (pp. 183-240)
**핵심**: 이표본 t-검정, p-value, 신뢰구간, 검정력, Type I/II 오류, 다중 검정 보정을 설명한다. 분산 추정의 함정과 민감도 향상 기법, A/A 테스트의 목적과 실행, 트리거링을 통한 민감도 최적화, SRM(Sample Ratio Mismatch) 디버깅, 변이 간 누출·간섭 문제, 장기적 처리 효과 측정 방법을 다룬다.
**키워드**: `t-test`, `power-analysis`, `SRM`, `triggering`, `long-term-effects`, `interference`
**상세**: → source file Part V (line 649)
