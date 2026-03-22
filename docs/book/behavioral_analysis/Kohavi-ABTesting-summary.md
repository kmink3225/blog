---
name: "Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing"
type: book-summary
source_file: "Kohavi-ABTesting_azure_full.md"
authors: "Ron Kohavi, Diane Tang, Ya Xu"
year: 2020
total_pages: 250
language: en
keywords: [AB-testing, online-experiments, OEC, metrics, statistical-significance, SRM, triggering, experimentation-platform, causal-inference]
sources:
  - file: "Kohavi-ABTesting_azure_full.md"
    tool: Document Intelligence
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
이 장은 온라인 통제 실험(A/B 테스트)의 기본 구조를 소개하며, Bing 광고 제목 변경 실험에서 연 1억 달러 이상의 수익 증가를 달성한 사례를 통해 실험의 가치를 보여준다. 통제 실험의 핵심 용어로 OEC(Overall Evaluation Criterion), 파라미터(요인), 변이(variant), 무작위 배정 단위(randomization unit)를 정의한다. 실험이 상관관계가 아닌 인과관계를 입증할 수 있는 유일한 방법임을 강조하며, 반사실적(counterfactual) 프레임워크를 설명한다. 아이디어의 가치를 사전에 평가하기 어려우며, 대부분의 실험에서 기대한 효과가 나타나지 않는다는 겸손의 원칙을 제시한다. 실험 실행의 end-to-end 과정(가설 수립, 설계, 실행, 분석, 의사결정)을 예시를 통해 설명한다. 세그먼트 차이와 Simpson's Paradox가 집계 수준의 결과를 왜곡할 수 있는 위험을 경고하며, 건전한 회의주의와 Twyman's Law의 중요성을 강조한다. 실험 성숙도 모델을 크롤(crawl), 워크(walk), 런(run), 플라이(fly)의 네 단계로 구분하고, 각 단계에서 필요한 인프라와 문화적 요구사항을 개관한다. 데이터 주도 문화를 구축하기 위해 HiPPO(Highest Paid Person's Opinion) 의존을 줄이고 실험 결과에 기반한 의사결정을 하는 조직 전환의 필요성을 논의한다. 실험 플랫폼의 기본 아키텍처와 확장 요구사항을 소개한다.

### Part II: Speed, Metrics, Ethics (pp. 79-123)
**핵심**: 웹사이트 성능이 사용자 참여에 미치는 영향을 end-to-end 사례로 분석한다. 조직 지표 분류(goal, driver, guardrail), 실험용 지표 공식화 원칙, OEC 구성 방법(Bing 검색, Amazon 이메일 사례)을 다룬다. Goodhart's Law와 Campbell's Law의 실무적 함의, 실험 윤리(데이터 수집, 사용자 식별, 문화)를 설명한다.
**키워드**: `latency`, `metrics-taxonomy`, `guardrail-metrics`, `Goodharts-law`, `ethics`
**상세**: → source file Part II (line 463)
이 장은 웹사이트 속도가 사용자 참여와 수익에 미치는 영향을 end-to-end 사례로 분석하며, 의도적 지연(slowdown) 실험 설계와 국소 선형 근사(local linear approximation) 가정을 설명한다. 페이지 요소별로 성능 영향이 다르며, 극단적 결과(extreme results)에 대한 주의가 필요함을 보여준다. 조직 지표를 목표(goal), 동인(driver), 가드레일(guardrail) 지표로 분류하는 체계를 제시하고, 지표 공식화의 원칙(측정 가능성, 방향성, 민감도, 적시성)을 설명한다. 실험용 지표와 비즈니스 지표의 차이를 논의하며, OEC를 구성하는 방법을 Bing 검색(세션당 성공률, 사용자당 세션 수)과 Amazon 이메일(구매 전환율, 구독 해지율) 사례로 설명한다. Goodhart's Law("측정 지표가 목표가 되면 좋은 측정 지표가 아니게 된다")와 Campbell's Law의 실무적 함의를 경고한다. 제도적 기억(institutional memory)의 개념을 소개하며, 과거 실험 결과의 체계적 기록과 메타분석이 조직 학습을 가속화한다고 주장한다. 실험 윤리에서 데이터 수집의 범위, 사용자 식별자(user identifier)의 유형과 프라이버시 함의, 사전 동의의 실무적 한계를 논의한다. 실험 문화와 프로세스 측면에서 윤리 검토 위원회, 위험 최소화 원칙, 사용자 피해 방지 가드레일의 구축 방법을 설명한다.

### Part III: Complementary Techniques (pp. 125-147)
**핵심**: 로그 분석, 인간 평가, UX 리서치, 포커스 그룹, 설문, 외부 데이터 등 통제 실험을 보완하는 기법을 비교한다. 관찰적 인과 연구(observational causal studies)의 설계와 함정, 반박된 관찰 연구 사례를 분석한다.
**키워드**: `complementary-techniques`, `observational-study`, `UER`, `logs-analysis`
**상세**: → source file Part III (line 544)
이 장은 통제 실험을 보완하는 기법들의 공간을 개관하며, 각 기법의 강점과 한계를 비교한다. 로그 기반 분석(logs-based analysis)이 사용자 행동의 대규모 패턴을 파악하는 데 유용하지만 인과관계를 입증하지 못한다는 점을 설명한다. 인간 평가(human evaluation)가 검색 관련성과 콘텐츠 품질 판단에 사용되며, 평가자 간 일치도와 비용이 주요 고려사항임을 논의한다. 사용자 경험 연구(UER)가 소규모 참가자를 대상으로 깊이 있는 정성적 통찰을 제공하지만 일반화에 제한이 있음을 지적한다. 포커스 그룹과 설문 조사의 활용 조건과 편향 위험을 설명하며, 외부 데이터 소스의 보완적 역할을 소개한다. 관찰적 인과 연구(observational causal studies)가 통제 실험이 불가능한 상황에서 사용되며, 자연 실험, 도구 변수(instrumental variables), 이중 차분법(difference-in-differences), 회귀 불연속 설계(regression discontinuity) 등의 방법을 설명한다. 관찰 연구의 핵심 함정으로 선택 편향(selection bias), 측정되지 않은 교란 변수(unmeasured confounders), 역인과(reverse causality)를 경고한다. 반박된 관찰적 인과 연구 사례(호르몬 대체 요법과 심장병 위험, 비타민 E와 암 등)를 분석하여 관찰 연구 결과의 신뢰성에 대한 건전한 회의주의를 촉구한다. 보완 기법들을 통제 실험과 결합하여 사용하는 것이 가장 효과적인 접근임을 결론짓는다.

### Part IV: Experimentation Platform (pp. 151-180)
**핵심**: 클라이언트 사이드 vs 서버 사이드 실험의 차이, 계측(instrumentation)의 원칙, 무작위 배정 단위(randomization unit) 선택, 실험 노출 확대(ramping)의 SQR 프레임워크, 대규모 분석 확장의 데이터 처리·계산·시각화를 다룬다.
**키워드**: `client-side`, `server-side`, `randomization-unit`, `ramping`, `SQR`
**상세**: → source file Part IV (line 565)
이 장은 클라이언트 사이드와 서버 사이드 실험의 차이를 설명하며, 클라이언트 사이드 실험에서 깜빡임(flickering) 문제, 캐싱 이슈, 지연된 배정의 영향을 다룬다. 계측(instrumentation)의 원칙으로 클라이언트 사이드와 서버 사이드 로깅의 장단점을 비교하고, 여러 소스의 로그를 처리하는 방법과 계측 문화 구축의 중요성을 강조한다. 무작위 배정 단위(randomization unit) 선택에서 사용자 단위, 페이지 단위, 세션 단위, 사용자-일 단위의 트레이드오프를 분석하며, 사용자 단위 무작위 배정을 권장한다. 실험 노출 확대(ramping)의 SQR 프레임워크를 소개하며, 속도(Speed), 품질(Quality), 위험(Risk)의 세 가지 축 사이의 균형을 설명한다. 실험 노출 확대의 네 단계(설계 검증, 내부 테스트, 소규모 노출, 전체 노출)와 각 단계의 의사결정 기준을 기술한다. 대규모 분석 확장을 위한 데이터 처리 파이프라인 설계, 데이터 계산의 효율화 방법, 결과 요약 및 시각화 도구의 구축 원칙을 설명한다. 실험 플랫폼이 실험의 한계 비용(marginal cost)을 0에 가깝게 낮추는 것이 목표임을 강조하며, 이를 통해 조직 전체의 실험 문화를 확산시킬 수 있다고 주장한다. 서버 사이드와 클라이언트 사이드 실험의 결합, 하이브리드 접근의 실무적 고려사항을 논의한다.

### Part V: Advanced Analysis (pp. 183-240)
**핵심**: 이표본 t-검정, p-value, 신뢰구간, 검정력, Type I/II 오류, 다중 검정 보정을 설명한다. 분산 추정의 함정과 민감도 향상 기법, A/A 테스트의 목적과 실행, 트리거링을 통한 민감도 최적화, SRM(Sample Ratio Mismatch) 디버깅, 변이 간 누출·간섭 문제, 장기적 처리 효과 측정 방법을 다룬다.
**키워드**: `t-test`, `power-analysis`, `SRM`, `triggering`, `long-term-effects`, `interference`
**상세**: → source file Part V (line 649)
이 장은 온라인 통제 실험의 통계적 기초로 이표본 t-검정의 원리를 설명하고, p-value와 신뢰구간의 올바른 해석을 제시한다. 중심극한정리에 의한 정규성 가정의 근거와 한계, Type I 오류(위양성)와 Type II 오류(위음성)의 관계, 검정력(power) 분석을 통한 표본 크기 결정 방법을 다룬다. 다중 검정(multiple testing) 문제에 대해 Bonferroni 보정, False Discovery Rate 제어 등의 방법을 소개하고, Fisher의 메타분석을 통한 결과 종합 방법을 설명한다. 분산 추정의 일반적 함정(사용자당 지표의 분산 과소추정, 무작위 배정 단위와 분석 단위 불일치)과 민감도 향상 기법(CUPED, 분산 감소 기법, 사전 실험 공변량 활용)을 기술한다. A/A 테스트의 목적(실험 시스템 검증, 분산 추정 교정, Type I 오류율 확인)과 실행 방법, 실패 시 원인 진단 절차를 설명한다. 트리거링(triggering)을 통해 실험에 실제로 영향을 받는 사용자만 분석 대상에 포함시켜 민감도를 최적화하는 방법과 신뢰할 수 있는 트리거링의 조건을 제시한다. SRM(Sample Ratio Mismatch)의 정의, 탐지 방법(카이제곱 검정), 주요 원인(로봇 필터링, 리디렉트, 잔류 효과)과 디버깅 절차를 상세히 다룬다. 변이 간 누출(leakage)과 간섭(interference)의 문제를 소셜 네트워크, 공유 자원, 양면 시장(two-sided market) 사례로 설명하고, 클러스터 무작위 배정 등 실무적 해결책을 논의한다. 장기적 처리 효과 측정을 위한 장기 실험 운영, 사용자 학습 효과, 참신성 효과(novelty effect), 대안적 방법(코호트 분석, 장기 홀드아웃)을 다룬다.
