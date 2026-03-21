---
name: "Causal Inference: What If"
type: book-summary
source_file: "Hernan-CausalInference_full.md"
authors: "Miguel A. Hernan, James M. Robins"
year: 2020
total_pages: 352
language: en
keywords: [causal inference, counterfactual, DAG, confounding, IP weighting, g-formula, marginal structural model, target trial, time-varying treatment, mediation]
---

# Causal Inference: What If — Summary

> Miguel A. Hernan, James M. Robins (2020), 352 pages, 23 chapters
> 반사실적(counterfactual) 프레임워크를 기반으로 인과 추론의 개념과 방법론을 체계적으로 다루는 교과서

## Contents

**Part I. Causal inference without models**
1. A definition of causal effect (p.3)
2. Randomized experiments (p.13)
3. Observational studies (p.27)
4. Effect modification (p.43)
5. Interaction (p.57)
6. Graphical representation of causal effects (p.71)
7. Confounding (p.85)
8. Selection bias (p.103)
9. Measurement bias and "Noncausal" diagrams (p.119)
10. Random variability (p.131)

**Part II. Causal inference with models**
11. Why model? (p.147)
12. IP weighting and marginal structural models (p.157)
13. Standardization and the parametric g-formula (p.169)
14. G-estimation of structural nested models (p.181)
15. Outcome regression and propensity scores (p.193)
16. Instrumental variable estimation (p.203)
17. Causal survival analysis (p.221)
18. Variable selection and high-dimensional data (p.235)

**Part III. Causal inference for time-varying treatments**
19. Time-varying treatments (p.249)
20. Treatment-confounder feedback (p.261)
21. G-methods for time-varying treatments (p.271)
22. Target trial emulation (p.299)
23. Causal mediation (p.317)

---

## Chapter Summaries

### Ch 1: A definition of causal effect (pp. 3-12)

**핵심**: 개인 인과효과와 평균 인과효과의 정의를 반사실적(counterfactual) 표기법으로 공식화한다. 잠재적 결과(potential outcome) Y^a를 도입하고, 인과효과와 연관(association)의 차이를 수학적으로 구분한다. 인과효과 측정 지표(causal risk difference, risk ratio, odds ratio)를 정의한다.

**키워드**: `counterfactual`, `potential outcome`, `causal effect`, `association`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 1 (line 878)

### Ch 2: Randomized experiments (pp. 13-26)

**핵심**: 무작위 배정(randomization)이 교환가능성(exchangeability)을 보장하여 인과 추론을 가능하게 하는 원리를 설명한다. 조건부 무작위 배정, 표준화(standardization), 역확률 가중치(IPW)를 통한 인과효과 추정 방법을 소개한다.

**키워드**: `randomization`, `exchangeability`, `standardization`, `inverse probability weighting`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 2 (line 1797)

### Ch 3: Observational studies (pp. 27-42)

**핵심**: 관찰 연구에서 인과효과를 식별하기 위한 세 가지 식별 조건(exchangeability, positivity, consistency)을 정의한다. 각 조건의 의미와 위반 시의 문제점, 그리고 target trial 개념을 소개한다.

**키워드**: `identifiability`, `exchangeability`, `positivity`, `consistency`, `target trial`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 3 (line 3102)

### Ch 4: Effect modification (pp. 43-56)

**핵심**: 치료 효과의 이질성(heterogeneity)을 다루며, 층화(stratification)와 매칭(matching)을 통한 효과 수정 식별 방법을 설명한다. 효과 수정과 보정 방법 간의 관계를 논의한다.

**키워드**: `effect modification`, `heterogeneity`, `stratification`, `matching`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 4 (line 4372)

### Ch 5: Interaction (pp. 57-70)

**핵심**: 상호작용(interaction)은 공동 개입(joint intervention)을 요구하며, 반사실적 반응 유형과 충분원인(sufficient cause) 모형을 통해 상호작용을 정의하고 식별하는 방법을 다룬다.

**키워드**: `interaction`, `joint intervention`, `sufficient cause`, `counterfactual response type`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 5 (line 5861)

### Ch 6: Graphical representation of causal effects (pp. 71-84)

**핵심**: 인과 다이어그램(DAG)을 통한 인과관계의 그래프적 표현을 소개한다. 주변 독립과 조건부 독립을 DAG로 표현하고, 편향의 구조적 분류(confounding, selection bias)를 제시한다.

**키워드**: `causal diagram`, `DAG`, `d-separation`, `structural bias`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 6 (line 6977)

### Ch 7: Confounding (pp. 85-102)

**핵심**: 교란의 구조를 DAG를 통해 분석하고, 교환가능성 및 backdoor criterion과의 관계를 설명한다. 교란 변수(confounder)의 정의 문제와 교란 보정 방법을 다룬다.

**키워드**: `confounding`, `backdoor criterion`, `exchangeability`, `confounder`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 7 (line 8103)

### Ch 8: Selection bias (pp. 103-118)

**핵심**: 선택 편향의 구조를 collider 조건부로 설명하고, 중도절단(censoring)과의 관계를 다룬다. 역확률 가중치를 이용한 선택 편향 보정 방법과 편향 없는 선택의 조건을 제시한다.

**키워드**: `selection bias`, `collider`, `censoring`, `IP weighting`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 8 (line 9435)

### Ch 9: Measurement bias and "Noncausal" diagrams (pp. 119-130)

**핵심**: 측정 오차가 인과 추론에 미치는 영향을 분석한다. 측정 오차가 있는 교란 변수와 충돌 변수의 문제, 그리고 비인과적 화살표를 포함하는 다이어그램의 한계를 논의한다.

**키워드**: `measurement error`, `mismeasured confounder`, `noncausal diagram`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 9 (line 10826)

### Ch 10: Random variability (pp. 131-144)

**핵심**: 식별(identification)과 추정(estimation)의 차이를 구분하고, 초모집단(super-population) 개념의 문제점, 조건부 원칙(conditionality principle), 차원의 저주(curse of dimensionality)를 다룬다.

**키워드**: `identification`, `estimation`, `super-population`, `curse of dimensionality`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 10 (line 11843)

### Ch 11: Why model? (pp. 147-156)

**핵심**: 모형이 필요한 이유를 설명하고, 모수적/비모수적 조건부 평균 추정량, 평활화(smoothing), 편향-분산 트레이드오프를 다룬다.

**키워드**: `parametric model`, `nonparametric`, `smoothing`, `bias-variance tradeoff`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 11 (line 12810)

### Ch 12: IP weighting and marginal structural models (pp. 157-168)

**핵심**: 모형을 이용한 역확률 가중치 추정, 안정화 가중치(stabilized IP weights), 주변 구조 모형(marginal structural model)의 구성과 해석을 다룬다.

**키워드**: `IP weighting`, `stabilized weights`, `marginal structural model`, `censoring`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 12 (line 13565)

### Ch 13: Standardization and the parametric g-formula (pp. 169-180)

**핵심**: IP 가중치의 대안으로서 표준화와 모수적 g-공식을 소개한다. 결과 모형을 통한 교란 보정과 두 방법의 비교, 추정값의 신뢰도 평가를 다룬다.

**키워드**: `standardization`, `g-formula`, `outcome model`, `parametric estimation`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 13 (line 14626)

### Ch 14: G-estimation of structural nested models (pp. 181-192)

**핵심**: 구조적 중첩 평균 모형(structural nested mean model)과 g-추정(g-estimation) 방법을 소개한다. 순위 보존(rank preservation) 가정과 다중 모수 모형을 다룬다.

**키워드**: `g-estimation`, `structural nested model`, `rank preservation`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 14 (line 15659)

### Ch 15: Outcome regression and propensity scores (pp. 193-202)

**핵심**: 결과 회귀와 성향점수(propensity score) 방법을 비교한다. 성향점수 층화, 표준화, 매칭 방법을 설명하고, 성향 모형과 구조 모형의 관계를 논의한다.

**키워드**: `outcome regression`, `propensity score`, `matching`, `stratification`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 15 (line 16500)

### Ch 16: Instrumental variable estimation (pp. 203-220)

**핵심**: 도구변수의 세 가지 조건을 정의하고, 동질성(homogeneity)과 단조성(monotonicity) 가정 하의 식별 전략을 설명한다. 다른 인과 추론 방법과의 비교를 다룬다.

**키워드**: `instrumental variable`, `homogeneity`, `monotonicity`, `LATE`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 16 (line 17317)

### Ch 17: Causal survival analysis (pp. 221-234)

**핵심**: 위험률(hazard)과 위험(risk)의 관계, 중도절단의 중요성, 생존 분석에서의 IP 가중치와 g-공식 적용을 다룬다.

**키워드**: `hazard`, `survival analysis`, `censoring`, `marginal structural model`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 17 (line 18712)

### Ch 18: Variable selection and high-dimensional data (pp. 235-246)

**핵심**: 변수 선택의 다양한 목표를 구분하고, 편향을 유발하거나 증폭하는 변수의 문제를 다룬다. 인과 추론에서의 머신러닝 활용과 이중 강건(doubly robust) 추정량을 소개한다.

**키워드**: `variable selection`, `bias amplification`, `machine learning`, `doubly robust`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 18 (line 19927)

### Ch 19: Time-varying treatments (pp. 249-260)

**핵심**: 시간 변동 치료의 인과효과를 정의하고, 치료 전략(treatment strategy)과 순차적 무작위 배정 실험을 다룬다. 순차적 교환가능성(sequential exchangeability) 조건을 소개한다.

**키워드**: `time-varying treatment`, `treatment strategy`, `sequential exchangeability`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 19 (line 20791)

### Ch 20: Treatment-confounder feedback (pp. 261-270)

**핵심**: 치료-교란 피드백의 구조를 설명하고, 전통적 방법(회귀 등)이 실패하는 이유와 이를 교정할 수 없는 근본적 원인을 분석한다.

**키워드**: `treatment-confounder feedback`, `time-varying confounding`, `traditional methods failure`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 20 (line 21861)

### Ch 21: G-methods for time-varying treatments (pp. 271-298)

**핵심**: 시간 변동 치료를 위한 g-공식, IP 가중치, 이중 강건 추정량, g-추정의 구체적 적용을 다룬다. 중도절단을 시간 변동 치료로 취급하는 방법과 big g-formula를 소개한다.

**키워드**: `g-formula`, `IP weighting`, `doubly robust`, `g-estimation`, `big g-formula`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 21 (line 22734)

### Ch 22: Target trial emulation (pp. 299-316)

**핵심**: 목표 시험 에뮬레이션(target trial emulation)의 개념을 정의한다. ITT 효과와 per-protocol 효과, 지속 치료 전략의 에뮬레이션, 시간 제로(time zero) 문제를 다루고, "What If" 질문에 대한 통합적 접근을 제시한다.

**키워드**: `target trial emulation`, `intention-to-treat`, `per-protocol`, `time zero`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 22 (line 24974)

### Ch 23: Causal mediation (pp. 317-325)

**핵심**: 매개 분석에 대한 비판과 옹호를 다루고, 경험적으로 검증 가능한 매개 효과와 개입주의적(interventionist) 매개 이론을 소개한다.

**키워드**: `mediation`, `direct effect`, `indirect effect`, `interventionist`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 23 (line 26177)
