---
name: "Causal Inference: What If"
type: book-summary
sources:
  - file: "Hernan-CausalInference_azure_full.md"
    tool: Document Intelligence
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
이 장은 개인 인과효과를 반사실적(counterfactual) 결과 Y^a를 이용하여 정의한다. 심장이식 사례(Zeus, Hera)를 통해 치료 시와 미치료 시의 잠재적 결과를 비교하여 인과효과를 판단하는 직관을 수학적으로 공식화한다. 일관성(consistency) 개념을 Y = Y^A로 정의하고, 관찰된 결과와 반사실적 결과의 관계를 명확히 한다. 개인 인과효과는 결측 데이터 문제로 인해 일반적으로 식별 불가능함을 설명한다. 평균 인과효과를 Pr[Y^{a=1}=1] ≠ Pr[Y^{a=0}=1]로 정의하며, 귀무가설과 예리한 인과 귀무가설(sharp causal null)을 구분한다. 인과효과 측정 지표로 인과 위험차(causal risk difference), 위험비(risk ratio), 교차비(odds ratio)를 정의하고 각각의 용도를 설명한다. 간섭(interference) 가정과 치료의 다중 버전(multiple versions of treatment) 문제를 Fine Point에서 논의한다. 20명 가족 데이터 표를 활용하여 평균 인과효과가 영인 경우에도 개별 인과효과가 존재할 수 있음을 보여준다. NNT(number needed to treat) 개념을 소개하고 인과 위험차와의 관계를 설명한다. 이산 및 연속 결과에 대한 인과효과의 일반화를 기대값 E[Y^a]로 표현한다.

### Ch 2: Randomized experiments (pp. 13-26)

**핵심**: 무작위 배정(randomization)이 교환가능성(exchangeability)을 보장하여 인과 추론을 가능하게 하는 원리를 설명한다. 조건부 무작위 배정, 표준화(standardization), 역확률 가중치(IPW)를 통한 인과효과 추정 방법을 소개한다.

**키워드**: `randomization`, `exchangeability`, `standardization`, `inverse probability weighting`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 2 (line 1797)
이 장은 무작위 배정이 교환가능성(exchangeability)을 보장하여 인과 추론을 가능하게 하는 원리를 설명한다. 보행자 실험 사례로 무작위 실험의 기본 구조를 소개하고, 동전 던지기에 의한 치료 배정이 그룹 교환을 가능하게 함을 보인다. 교환가능성을 Y^a ⊥⊥ A로 공식화하고, 이것이 무작위 실험에서 연관(association)이 곧 인과(causation)임을 의미함을 증명한다. 조건부 무작위 배정에서는 공변량 L에 따라 배정 확률이 달라지며, 조건부 교환가능성 Y^a ⊥⊥ A|L이 성립함을 설명한다. 표준화(standardization)를 통해 조건부 무작위 실험에서 주변 인과효과를 계산하는 방법을 제시하고, 층별 위험을 가중 평균하는 공식을 도출한다. 역확률 가중치(IPW)를 대안적 방법으로 소개하며, 가상 모집단(pseudo-population) 개념을 통해 L과 A의 독립성을 복원하는 원리를 설명한다. 교차 실험(crossover experiment)에서 개인 인과효과 식별 조건(이월효과 없음, 시간 불변 효과)을 논의한다. 완전 교환가능성(full exchangeability)과 평균 교환가능성(mean exchangeability)의 차이를 기술적으로 구분한다. Y^a ⊥⊥ A와 Y ⊥⊥ A의 차이를 명확히 하여 인과 독립과 관찰적 독립의 혼동을 방지한다.

### Ch 3: Observational studies (pp. 27-42)

**핵심**: 관찰 연구에서 인과효과를 식별하기 위한 세 가지 식별 조건(exchangeability, positivity, consistency)을 정의한다. 각 조건의 의미와 위반 시의 문제점, 그리고 target trial 개념을 소개한다.

**키워드**: `identifiability`, `exchangeability`, `positivity`, `consistency`, `target trial`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 3 (line 3102)
이 장은 관찰 연구에서 인과효과를 식별하기 위한 세 가지 조건을 정의한다. 관찰 연구를 조건부 무작위 실험(conditionally randomized experiment)으로 개념화할 수 있는 조건을 제시하며, 이것이 식별가능성(identifiability)의 핵심임을 설명한다. 일관성(consistency)은 관찰된 치료값에 대한 반사실적 결과가 실제 결과와 일치함을 요구하며, 잘 정의된 개입(well-defined intervention)과 치료 버전의 관련성을 논의한다. 교환가능성(exchangeability)은 측정된 공변량 L에 조건부로 Y^a ⊥⊥ A|L이 성립해야 함을 의미하며, 미측정 교란 변수의 존재가 이를 위반할 수 있음을 설명한다. 양성(positivity)은 L의 모든 수준에서 모든 치료값을 받을 확률이 양수여야 함을 요구하며, 구조적 위반과 확률적 위반을 구분한다. 흡연 여부에 의한 교환가능성 위반 사례를 통해, 미측정 변수 U가 조건부 교환가능성을 깨뜨리는 구조를 보여준다. 식별가능성의 형식적 정의를 제시하고, 관찰 데이터가 복수의 인과효과 값과 양립 가능한 경우의 비식별성을 논의한다. 전문 지식이 조건부 교환가능성 가정의 타당성을 뒷받침해야 하지만, 경험적으로 검증 불가능함을 강조한다. 목표 시험(target trial) 개념을 간략히 소개하며 도구변수 접근법을 대안으로 언급한다.

### Ch 4: Effect modification (pp. 43-56)

**핵심**: 치료 효과의 이질성(heterogeneity)을 다루며, 층화(stratification)와 매칭(matching)을 통한 효과 수정 식별 방법을 설명한다. 효과 수정과 보정 방법 간의 관계를 논의한다.

**키워드**: `effect modification`, `heterogeneity`, `stratification`, `matching`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 4 (line 4372)
이 장은 치료 효과의 이질성(heterogeneity)을 다루며, 효과 수정(effect modification)의 정의와 식별 방법을 제시한다. Zeus 가족 데이터에서 성별 V에 따라 심장이식의 인과효과가 여성에서는 해로운 방향(위험비 1.5), 남성에서는 보호적 방향(위험비 2/3)으로 상반됨을 보여준다. 가산적(additive) 효과 수정과 승산적(multiplicative) 효과 수정을 구분하고, 질적(qualitative) 효과 수정과 양적(quantitative) 효과 수정의 차이를 설명한다. 주변적 무작위 실험에서는 단순 층화 분석으로 효과 수정을 식별할 수 있음을 보인다. 조건부 무작위 실험에서는 층별로 표준화 또는 IPW를 적용하여 V의 각 수준에서 인과효과를 계산해야 함을 설명한다. 40명 인구(그리스인 20명, 로마인 20명)의 데이터로 국적 V에 의한 효과 수정을 분석하는 구체적 예제를 제시한다. 치료군에서의 효과(effect in the treated)를 별도로 정의하고 SMR(표준화 이환비)과의 관계를 논의한다. 효과 수정 변수 V가 대리(surrogate) 효과 수정인지 직접적 인과적 상호작용의 결과인지를 구별하는 중요성을 강조한다. 매칭(matching)을 통한 효과 수정 식별의 장단점과 외적 타당성(transportability) 문제를 다룬다.

### Ch 5: Interaction (pp. 57-70)

**핵심**: 상호작용(interaction)은 공동 개입(joint intervention)을 요구하며, 반사실적 반응 유형과 충분원인(sufficient cause) 모형을 통해 상호작용을 정의하고 식별하는 방법을 다룬다.

**키워드**: `interaction`, `joint intervention`, `sufficient cause`, `counterfactual response type`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 5 (line 5861)
이 장은 상호작용(interaction)을 공동 개입(joint intervention)의 맥락에서 정의하며, 효과 수정과의 차이를 명확히 한다. 심장이식 A와 비타민 E의 공동 개입으로 4가지 반사실적 결과 Y^{a,e}를 정의하고, 가산적·승산적 상호작용의 공식을 제시한다. 상호작용의 정의에서 두 치료 A와 E가 대등한 지위를 가짐을 수학적으로 증명한다. 효과 수정은 한 변수의 인과효과만을 고려하는 비대칭적 개념인 반면, 상호작용은 두 변수 모두에 대한 식별 가정(교환가능성, 양성, 일관성)을 요구함을 설명한다. E가 무작위 배정된 경우 상호작용과 효과 수정이 일치함을 보이고, E가 관찰된 경우 결합 치료 AE로 재정의하여 식별하는 방법을 제시한다. 반사실적 반응 유형(response type)을 4가지(doomed, helped, hurt, immune)로 분류하고, 두 이분 치료의 경우 16가지 반응 유형을 도출한다. 가산적 상호작용이 존재하려면 반응 유형 8, 12, 14, 15 또는 7, 10에 속하는 개인이 있어야 함을 보인다. 충분원인(sufficient cause) 모형을 소개하고, 충분원인 상호작용이 가산적 상호작용의 존재를 시사함을 논증한다. 초가산적(superadditive) 상호작용과 초승산적(supermultiplicative) 상호작용의 관계를 논의한다.

### Ch 6: Graphical representation of causal effects (pp. 71-84)

**핵심**: 인과 다이어그램(DAG)을 통한 인과관계의 그래프적 표현을 소개한다. 주변 독립과 조건부 독립을 DAG로 표현하고, 편향의 구조적 분류(confounding, selection bias)를 제시한다.

**키워드**: `causal diagram`, `DAG`, `d-separation`, `structural bias`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 6 (line 6977)
이 장은 인과 다이어그램(DAG)을 통한 인과관계의 그래프적 표현을 소개하며, 주변 독립과 조건부 독립의 판단 규칙을 제시한다. DAG의 기본 요소(노드, 방향 간선)와 "방향적 비순환 그래프"의 의미를 정의하고, 인과 DAG의 세 가지 조건(직접 인과효과의 부재 표현, 공통 원인 포함, 후손 관계)을 설명한다. 아스피린-심장병(인과 경로), 라이터-폐암(공통 원인 포크), 유전형-흡연(충돌 변수 콜라이더)의 세 가지 사례로 주변 연관성의 유무를 판단하는 규칙을 시연한다. 충돌 변수(collider)가 경로상의 연관 흐름을 차단하지만, 충돌 변수에 대한 조건부 분석이 차단된 경로를 열어 허위 연관을 생성함을 설명한다. 매개 변수 B에 대한 조건부 분석이 A→B→Y 경로의 연관을 차단하여 조건부 독립을 만드는 과정을 보여준다. d-분리(d-separation) 이론을 직관적으로 소개하고, 경로 차단과 개방의 규칙을 일반화한다. 인과 DAG와 반사실 모형의 관계를 비모수 구조방정식 모형(NPSEM)과 FFRCISTG를 통해 기술적으로 연결한다. 단일 세계 개입 그래프(SWIG)의 개념을 간략히 예고하며, 교란·선택 편향의 구조적 분류를 위한 기초를 제공한다. 양성(positivity)과 일관성(consistency)의 DAG 표현을 논의한다.

### Ch 7: Confounding (pp. 85-102)

**핵심**: 교란의 구조를 DAG를 통해 분석하고, 교환가능성 및 backdoor criterion과의 관계를 설명한다. 교란 변수(confounder)의 정의 문제와 교란 보정 방법을 다룬다.

**키워드**: `confounding`, `backdoor criterion`, `exchangeability`, `confounder`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 7 (line 8103)
이 장은 교란(confounding)의 구조를 DAG를 통해 분석하고, 교환가능성 및 백도어 기준(backdoor criterion)과의 관계를 설명한다. 교란을 치료와 결과의 공통 원인이 만드는 열린 백도어 경로의 존재로 정의하며, 직업적 요인·임상 결정·생활 습관·유전 요인·사회 요인·환경 노출 등 다양한 교란 사례를 제시한다. 교란과 교환가능성의 관계를 공식화하여, 교란이 없으면 주변 교환가능성 Y^a ⊥⊥ A이 성립하고, 잔여 교란이 없으면 조건부 교환가능성 Y^a ⊥⊥ A|L이 성립함을 보인다. 백도어 기준을 정의하고, L이 치료의 후손이 아니면서 모든 백도어 경로를 차단하면 충분한 교란 보정 집합임을 설명한다. 다양한 DAG 구조(Figure 7.1~7.8)에 백도어 기준을 적용하여 교란 존재 여부와 보정 필요 변수를 판단하는 예제를 시연한다. 충돌 변수에 대한 보정이 오히려 편향을 도입하는 사례와, 매개 변수에 대한 부적절한 보정이 총효과를 왜곡하는 사례를 다룬다. SWIG(Single World Intervention Graph)를 활용한 교환가능성 판단 방법을 대안적 접근으로 소개한다. 교란 변수(confounder)의 정의 문제를 논의하며, 전통적 정의의 한계와 DAG 기반 정의의 장점을 비교한다. 교란의 방향과 크기가 DAG만으로는 판단 불가능함을 강조한다.

### Ch 8: Selection bias (pp. 103-118)

**핵심**: 선택 편향의 구조를 collider 조건부로 설명하고, 중도절단(censoring)과의 관계를 다룬다. 역확률 가중치를 이용한 선택 편향 보정 방법과 편향 없는 선택의 조건을 제시한다.

**키워드**: `selection bias`, `collider`, `censoring`, `IP weighting`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 8 (line 9435)
이 장은 선택 편향의 구조를 충돌 변수(collider) 조건부로 설명하고, 다양한 형태의 선택 편향을 통합적으로 분류한다. 엽산 보충제-심장기형 연구 사례(Figure 8.1)로, 치료 A와 결과 Y의 공통 효과 C(사산)에 대한 조건부 분석이 허위 연관을 생성하는 기본 구조를 보여준다. 충돌 변수의 후손(부모의 슬픔 S)에 대한 조건부 분석도 동일한 편향을 유발함을 설명한다. HIV 치료 연구의 차별적 추적 손실(Figure 8.3~8.6) 사례로, 미측정 변수 U를 포함하는 다양한 선택 편향 구조를 분석한다. 건강 근로자 편향, 자기 선택 편향, 연구 진입 전 치료에 의한 선택 편향 등 구체적 사례를 제시한다. 선택 편향과 교란의 구조적 차이(공통 효과 vs. 공통 원인)를 명확히 구분하면서도, 실무에서 양자가 동시에 존재하는 사례를 논의한다. 역확률 가중치(IP censoring weights)를 이용한 선택 편향 보정 방법을 소개하며, 중도절단 변수 C에 대한 가중치 W^C의 구성과 적용을 설명한다. 선택 편향이 귀무가설 하에서도 발생할 수 있음(bias under the null)을 강조하고, M-편향 구조를 포함한 추가적 선택 편향 형태를 다룬다. 환자-대조군 연구에서의 선택 편향 구조를 Fine Point에서 별도로 논의한다.

### Ch 9: Measurement bias and "Noncausal" diagrams (pp. 119-130)

**핵심**: 측정 오차가 인과 추론에 미치는 영향을 분석한다. 측정 오차가 있는 교란 변수와 충돌 변수의 문제, 그리고 비인과적 화살표를 포함하는 다이어그램의 한계를 논의한다.

**키워드**: `measurement error`, `mismeasured confounder`, `noncausal diagram`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 9 (line 10826)
이 장은 측정 오차가 인과 추론에 미치는 영향을 분석하며, 측정 편향(measurement bias)의 구조적 분류를 제시한다. 치료 A와 결과 Y의 측정된 버전 A*와 Y*를 구분하고, 측정 오차의 원인 U_A와 U_Y를 DAG에 명시적으로 포함하는 표현법을 소개한다. 측정 오차의 네 가지 유형을 독립성과 비차등성(nondifferentiality)의 조합으로 분류한다: 독립·비차등(Figure 9.2), 종속·비차등(Figure 9.3), 독립·차등(Figure 9.4, 9.5), 종속·차등(Figure 9.6, 9.7). 회상 편향(recall bias)과 역인과 편향(reverse causation bias)을 차등 측정 오차의 구체적 사례로 설명한다. 독립·비차등 측정 오차에서도 비이분 치료의 경우 편향의 방향이 역전될 수 있음을 지적한다. 교란 변수 L의 측정 오차가 존재할 때, L*에 대한 보정이 백도어 경로를 완전히 차단하지 못하여 잔여 교란이 발생하는 구조를 분석한다. 비인과적 다이어그램(noncausal diagram)의 개념을 소개하며, 전통적 역학 다이어그램에서 화살표가 반드시 인과관계를 의미하지 않는 경우를 논의한다. 충돌 변수의 측정 오차가 DAG의 d-분리 성질에 미치는 영향을 분석하여, 오측정된 충돌 변수에 대한 보정이 예상과 다른 편향을 유발할 수 있음을 보인다. 측정 오차 보정 방법의 일반적 원리(타당화 표본, 모형 가정)를 개관한다.

### Ch 10: Random variability (pp. 131-144)

**핵심**: 식별(identification)과 추정(estimation)의 차이를 구분하고, 초모집단(super-population) 개념의 문제점, 조건부 원칙(conditionality principle), 차원의 저주(curse of dimensionality)를 다룬다.

**키워드**: `identification`, `estimation`, `super-population`, `curse of dimensionality`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 10 (line 11843)
이 장은 식별(identification)과 추정(estimation)의 차이를 구분하고, 무작위 변동성이 인과 추론에 미치는 영향을 다룬다. 앞선 장들이 사실상 무한한 연구 모집단을 가정한 식별 문제에 집중했음을 명시하고, 이제 유한 표본에서의 추정 문제로 전환한다. 추정량(estimand), 추정자(estimator), 추정치(estimate)의 개념을 정의하고, 일치 추정자(consistent estimator)의 형식적 정의를 제시한다. Wald 95% 신뢰구간의 구성 방법(점추정치 ± 1.96 × 표준오차)을 설명하고, 신뢰구간의 빈도주의적 해석(95%의 표본에서 모수를 포함)을 강조한다. 초모집단(super-population) 개념의 두 가지 정당화(전체 무작위 배정 vs. 표본 후 무작위 배정)와 그 동치성을 설명한다. 초모집단의 존재에 대한 회의를 표명하며, 결정론적 반사실과 비결정론적 반사실 하에서의 이항 표집 분포의 성립 조건을 분석한다. 조건부 원칙(conditionality principle)과 비조건부 추론의 차이를 논의하고, 제한적 추론의 실무적 의미를 다룬다. 차원의 저주(curse of dimensionality)가 비모수적 추정에 미치는 영향을 설명하며, 이것이 Part II에서 모형 사용의 동기가 됨을 예고한다. 체계적 편향과 무작위 변동성의 질적 차이를 강조하며, 신뢰구간이 체계적 편향을 반영하지 못하는 한계를 논의한다.

### Ch 11: Why model? (pp. 147-156)

**핵심**: 모형이 필요한 이유를 설명하고, 모수적/비모수적 조건부 평균 추정량, 평활화(smoothing), 편향-분산 트레이드오프를 다룬다.

**키워드**: `parametric model`, `nonparametric`, `smoothing`, `bias-variance tradeoff`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 11 (line 12810)
이 장은 모형이 필요한 이유를 설명하고, 모수적/비모수적 조건부 평균 추정의 차이를 다룬다. HIV 감염자 16명의 치료-CD4 데이터를 사용하여, 이분 치료에서는 표본 평균이 비모수적으로 조건부 평균을 추정할 수 있지만, 연속 치료(0~100mg)에서는 관찰되지 않은 치료 수준의 평균을 추정할 수 없는 문제를 보여준다. 모수적 조건부 평균 모형 E[Y|A] = θ₀ + θ₁A를 도입하고, 최소자승법(OLS)으로 모수를 추정하는 과정을 설명한다. 모형을 "데이터의 결합 분포에 대한 사전 제약"으로 정의하며, 모형 오명세(misspecification)의 위험을 강조한다. 포화 모형(saturated model)의 개념을 소개하고, 이분 치료에서 선형 모형이 포화 모형이 되어 사실상 모형이 아님을 보인다. 비모수적 추정자와 모수적 추정자의 관계를 명확히 하며, 모수적 추정이 필요한 근본적 이유가 차원의 저주임을 재확인한다. 평활(smoothing) 기법(이동 평균, 커널 평활)을 비모수적 대안으로 소개하고, 모수적 모형과의 유사성을 논의한다. 편향-분산 트레이드오프를 설명하며, 모형의 유연성과 분산 간의 균형이 좋은 추정의 핵심임을 강조한다. Part II의 나머지 장들에서 모형 기반 인과 추론을 다룰 것임을 예고한다.

### Ch 12: IP weighting and marginal structural models (pp. 157-168)

**핵심**: 모형을 이용한 역확률 가중치 추정, 안정화 가중치(stabilized IP weights), 주변 구조 모형(marginal structural model)의 구성과 해석을 다룬다.

**키워드**: `IP weighting`, `stabilized weights`, `marginal structural model`, `censoring`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 12 (line 13565)
이 장은 모형을 이용한 역확률 가중치(IP weighting) 추정과 주변 구조 모형(marginal structural model)을 다룬다. NHEFS 데이터에서 금연(A)이 체중 증가(Y)에 미치는 인과효과를 추정하는 인과 질문을 설정하고, 9개 교란 변수(성별, 나이, 인종, 교육, 체중, 흡연 강도·기간, 운동, 활동량)를 식별한다. 고차원 공변량에서 비모수적 IP 가중치 추정이 불가능한 이유(차원의 저주)를 설명하고, 로지스틱 회귀 모형으로 Pr[A=1|L]을 추정하는 방법을 제시한다. 가상 모집단(pseudo-population)에서 포화 모형 E[Y|A] = θ₀ + θ₁A를 가중 최소자승법으로 적합하여 인과효과 추정치 3.4kg을 산출한다. 안정화 가중치(stabilized IP weights) SW^A = f(A)/f(A|L)를 도입하여, 비안정화 가중치 대비 분산 감소와 양성 위반에 대한 강건성 향상을 보인다. 비포화 주변 구조 모형(nonsaturated MSM)을 소개하여, 연속 치료나 다수준 치료에서 인과효과를 추정하는 방법을 설명한다. 효과 수정을 포함하는 MSM과 중도절단에 대한 IP 가중치 보정(IP censoring weights)을 다루며, 치료와 중도절단 모두에 대한 결합 가중치 W^{A,C}의 구성을 설명한다. Horvitz-Thompson 추정자와 Hajek 추정자의 차이를 기술적으로 논의한다. 가중치의 극단값 진단과 모형 적합도 평가 방법을 제시한다.

### Ch 13: Standardization and the parametric g-formula (pp. 169-180)

**핵심**: IP 가중치의 대안으로서 표준화와 모수적 g-공식을 소개한다. 결과 모형을 통한 교란 보정과 두 방법의 비교, 추정값의 신뢰도 평가를 다룬다.

**키워드**: `standardization`, `g-formula`, `outcome model`, `parametric estimation`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 13 (line 14626)
이 장은 IP 가중치의 대안으로서 표준화(standardization)와 모수적 g-공식(parametric g-formula)을 소개한다. 결과 모형 E[Y|A,L]을 적합하고 치료값 a에 대해 L의 주변 분포로 평균하여 반사실적 평균 E[Y^a]를 추정하는 과정을 설명한다. NHEFS 금연-체중 데이터에서 표준화 추정치 3.5kg과 IP 가중치 추정치 3.4kg을 비교하며, 두 방법이 동일한 식별 가정 하에서 동일한 인과효과를 추정함을 확인한다. 결과 모형과 치료 모형의 올바른 명세가 각각 표준화와 IP 가중치의 일치성 조건임을 대비한다. 표준화가 비포화 결과 모형을 사용할 때 모형 외삽(extrapolation)의 위험이 있음을 설명하고, IP 가중치가 치료 모형의 오명세에 민감함을 논의한다. 부트스트랩을 이용한 신뢰구간 구성 방법을 제시하며, IP 가중치 방법과의 분산 비교를 다룬다. 효과 수정을 포함하는 표준화 분석과 비포화 결과 모형의 사용법을 설명한다. 중도절단(censoring)이 있는 경우의 표준화 적용을 다루며, 중도절단 변수를 결과 모형에 포함하는 방법을 제시한다. 두 방법의 장단점을 종합적으로 비교하고, 실무적 선택 기준을 논의한다.

### Ch 14: G-estimation of structural nested models (pp. 181-192)

**핵심**: 구조적 중첩 평균 모형(structural nested mean model)과 g-추정(g-estimation) 방법을 소개한다. 순위 보존(rank preservation) 가정과 다중 모수 모형을 다룬다.

**키워드**: `g-estimation`, `structural nested model`, `rank preservation`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 14 (line 15659)
이 장은 구조적 중첩 평균 모형(structural nested mean model, SNMM)과 g-추정(g-estimation) 방법을 소개한다. SNMM은 반사실적 결과 Y^{a=0}을 이용하여 치료 효과를 E[Y^a - Y^{a=0}|A=a, L]로 모형화하며, 조건부 인과효과를 직접 추정한다. 순위 보존(rank preservation) 가정 하에서 개인 수준의 반사실적 결과 Y^{a=0} = Y - ψ₁A를 도출하고, 이를 치료 A와의 독립성(교환가능성)을 이용하여 ψ₁을 추정하는 g-추정 절차를 설명한다. 격자 탐색(grid search)과 모수적 모형을 이용한 g-추정의 두 가지 구현 방법을 제시한다. 순위 보존 가정 없이도 평균 인과효과를 추정할 수 있는 조건을 논의하고, 다중 모수 SNMM의 확장을 다룬다. NHEFS 데이터에서 금연의 체중 증가 효과를 g-추정으로 3.5kg으로 추정하며, IP 가중치 및 표준화 결과와의 일치를 확인한다. g-추정이 치료 모형에 의존하지만 결과 모형의 오명세에 상대적으로 강건한 특성을 설명한다. 효과 수정을 포함하는 SNMM의 구성과 해석을 다루며, 비이분 치료로의 확장을 논의한다. SNMM과 MSM의 관계 및 차이점을 비교 분석한다.

### Ch 15: Outcome regression and propensity scores (pp. 193-202)

**핵심**: 결과 회귀와 성향점수(propensity score) 방법을 비교한다. 성향점수 층화, 표준화, 매칭 방법을 설명하고, 성향 모형과 구조 모형의 관계를 논의한다.

**키워드**: `outcome regression`, `propensity score`, `matching`, `stratification`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 15 (line 16500)
이 장은 결과 회귀(outcome regression)와 성향점수(propensity score) 방법을 비교하며, 양자의 관계와 한계를 논의한다. 결과 모형 E[Y|A,L]에 L을 포함하여 조건부 인과효과를 추정하는 접근과, IP 가중치로 주변 인과효과를 추정하는 접근의 차이를 설명한다. 성향점수 Pr[A=1|L]의 정의와 성질을 소개하고, 성향점수에 조건부로 교환가능성이 성립함(Y^a ⊥⊥ A|e(L))을 증명한다. 성향점수 층화(stratification), 매칭(matching), 가중치 부여의 세 가지 성향점수 활용법을 설명하며, 각각의 장단점을 비교한다. 성향점수 모형과 결과 모형의 관계를 논의하고, 두 모형을 동시에 사용하는 이중 강건(doubly robust) 추정의 개념을 예고한다. 결과 회귀에서 L을 포함한 조건부 효과 추정치를 주변 효과로 전환하는 표준화 과정의 필요성을 설명한다. 매칭 방법에서 1:1 매칭, 다대다 매칭, 캘리퍼 매칭 등 다양한 매칭 전략의 실무적 고려사항을 다룬다. 성향점수의 균형 진단(balance check)과 모형 적합도 평가 방법을 제시한다. 처치군에 대한 효과(ATT)와 전체 모집단에 대한 효과(ATE) 추정의 차이를 논의한다.

### Ch 16: Instrumental variable estimation (pp. 203-220)

**핵심**: 도구변수의 세 가지 조건을 정의하고, 동질성(homogeneity)과 단조성(monotonicity) 가정 하의 식별 전략을 설명한다. 다른 인과 추론 방법과의 비교를 다룬다.

**키워드**: `instrumental variable`, `homogeneity`, `monotonicity`, `LATE`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 16 (line 17317)
이 장은 도구변수(instrumental variable)의 세 가지 조건을 정의하고, 동질성(homogeneity)과 단조성(monotonicity) 가정 하의 식별 전략을 설명한다. 도구변수 Z는 (1) 치료 A와 연관되고, (2) 미측정 교란 변수 U와 독립이며, (3) 결과 Y에 Z를 통한 직접 효과가 없어야 한다는 세 조건을 DAG로 표현한다. 동질성 가정(치료 효과가 모든 개인에서 동일) 하에서 도구변수 추정량이 인과효과의 비율(Wald estimator)로 산출됨을 보인다. 단조성 가정(Z가 A에 미치는 효과가 모든 개인에서 같은 방향) 하에서 LATE(local average treatment effect, 순응자 평균 인과효과)를 식별하는 방법을 설명한다. 네 가지 순응 유형(always-takers, never-takers, compliers, defiers)을 정의하고, 단조성이 defiers의 부재를 의미함을 보인다. 무작위 시험에서의 비순응 문제를 도구변수 분석으로 해결하는 방법과, 멘델리안 무작위화(Mendelian randomization)를 역학 연구에서의 도구변수 응용으로 소개한다. 2단계 최소자승법(2SLS)의 원리와 구현을 설명하고, 약한 도구변수(weak instrument)의 문제를 논의한다. 도구변수 조건의 검증 불가능성과 위반 시의 편향 방향을 분석한다. 다른 인과 추론 방법(IP 가중치, 표준화, g-추정)과의 식별 가정 차이를 비교한다.

### Ch 17: Causal survival analysis (pp. 221-234)

**핵심**: 위험률(hazard)과 위험(risk)의 관계, 중도절단의 중요성, 생존 분석에서의 IP 가중치와 g-공식 적용을 다룬다.

**키워드**: `hazard`, `survival analysis`, `censoring`, `marginal structural model`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 17 (line 18712)
이 장은 생존 분석(survival analysis)에서의 인과 추론을 다루며, 위험률(hazard)과 위험(risk)의 관계를 명확히 한다. 사건 발생 시간(time-to-event) 결과에서 반사실적 결과 T^a를 정의하고, 이산 시간(discrete time)과 연속 시간(continuous time)에서의 생존 함수와 위험 함수를 공식화한다. 위험비(hazard ratio)가 조건부 효과 측정치임을 설명하고, 비충돌성(non-collapsibility)으로 인해 조건부 위험비와 주변 위험비가 일반적으로 다름을 보인다. 인과 위험비(causal hazard ratio)와 연관 위험비(associational hazard ratio)의 차이를 논의하며, 교환가능성 하에서도 양자가 일치하지 않을 수 있음을 보인다. 중도절단(censoring)의 중요성을 강조하고, 정보적 중도절단(informative censoring)이 선택 편향을 도입하는 구조를 DAG로 표현한다. IP 가중치를 이용한 생존 분석에서의 교란 보정과 중도절단 보정을 다루며, 가중 Cox 모형과 가중 로지스틱 모형의 적용을 설명한다. 모수적 g-공식의 생존 분석 확장을 제시하고, 이산 시간 위험 모형을 통한 반사실적 생존 곡선 추정 방법을 설명한다. 생존 분석에서 양성(positivity) 조건의 특수한 형태와 위반 시의 문제를 논의한다.

### Ch 18: Variable selection and high-dimensional data (pp. 235-246)

**핵심**: 변수 선택의 다양한 목표를 구분하고, 편향을 유발하거나 증폭하는 변수의 문제를 다룬다. 인과 추론에서의 머신러닝 활용과 이중 강건(doubly robust) 추정량을 소개한다.

**키워드**: `variable selection`, `bias amplification`, `machine learning`, `doubly robust`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 18 (line 19927)
이 장은 변수 선택의 다양한 목표를 구분하고, 편향을 유발하거나 증폭하는 변수의 문제를 다룬다. 인과 추론에서의 변수 선택이 예측 모형에서의 변수 선택과 근본적으로 다름을 강조하며, 교란 보정을 위한 변수 선택의 원칙을 제시한다. 도구변수를 교란 보정에 포함하면 편향을 증폭(bias amplification)시킬 수 있음을 DAG와 수치 예제로 보인다. Z-편향(Z-bias) 구조에서 도구변수의 포함이 오히려 추정치를 악화시키는 메커니즘을 분석한다. 충돌 변수의 후손을 보정 변수에 포함하면 선택 편향을 도입할 수 있는 구조를 설명하고, M-편향의 가능성을 논의한다. 인과 추론에서의 머신러닝 활용을 소개하며, 예측 모형과 인과 모형의 목적 차이에 따른 변수 선택 전략의 차이를 설명한다. 이중 강건(doubly robust) 추정량을 소개하고, 치료 모형과 결과 모형 중 하나만 올바르게 명세되어도 일치 추정을 보장하는 성질을 설명한다. TMLE(targeted maximum likelihood estimation)와 AIPW(augmented IPW)의 개념을 간략히 소개한다. 고차원 데이터에서의 변수 선택 방법(LASSO, 정규화)과 인과 추론에서의 적용 주의사항을 논의한다. 데이터 적응적(data-adaptive) 방법과 교차 적합(cross-fitting)의 필요성을 다룬다.

### Ch 19: Time-varying treatments (pp. 249-260)

**핵심**: 시간 변동 치료의 인과효과를 정의하고, 치료 전략(treatment strategy)과 순차적 무작위 배정 실험을 다룬다. 순차적 교환가능성(sequential exchangeability) 조건을 소개한다.

**키워드**: `time-varying treatment`, `treatment strategy`, `sequential exchangeability`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 19 (line 20791)
이 장은 시간 변동 치료(time-varying treatment)의 인과효과를 정의하고, 치료 전략(treatment strategy)과 순차적 무작위 배정 실험의 개념을 다룬다. 시간 변동 치료 이력 ā = (a₀, a₁, ..., aₖ)에 대한 반사실적 결과 Y^ā를 정의하며, 정적 전략(static strategy)과 동적 전략(dynamic strategy)을 구분한다. 순차적 교환가능성(sequential exchangeability) Y^ā ⊥⊥ Aₖ | Āₖ₋₁, L̄ₖ 조건을 소개하고, 이것이 각 시점에서의 조건부 무작위 배정에 해당함을 설명한다. 순차적 양성(sequential positivity)과 순차적 일관성(sequential consistency) 조건을 정의하며, 시간 변동 설정에서의 식별 조건을 완성한다. NHEFS 데이터를 이산 시간으로 재구성하여 시간 변동 치료 분석의 기초를 마련하는 과정을 보여준다. 시간 변동 치료에서의 ITT(intention-to-treat) 효과와 per-protocol 효과의 구분을 도입한다. 단순한 2시점 사례로 시간 변동 교란의 개념을 직관적으로 설명하고, 전통적 회귀 분석의 한계를 예고한다. 치료 전략의 비교가 단일 시점 치료의 비교와 질적으로 다른 이유를 설명하며, Part III의 핵심 주제인 g-방법의 필요성을 동기부여한다.

### Ch 20: Treatment-confounder feedback (pp. 261-270)

**핵심**: 치료-교란 피드백의 구조를 설명하고, 전통적 방법(회귀 등)이 실패하는 이유와 이를 교정할 수 없는 근본적 원인을 분석한다.

**키워드**: `treatment-confounder feedback`, `time-varying confounding`, `traditional methods failure`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 20 (line 21861)
이 장은 치료-교란 피드백(treatment-confounder feedback)의 구조를 설명하고, 전통적 방법이 실패하는 이유를 분석한다. 시간 변동 교란 변수 Lₖ가 이전 치료 Aₖ₋₁의 영향을 받으면서 동시에 미래 치료 Aₖ와 결과 Y의 공통 원인인 구조를 DAG로 표현한다. 이 피드백 구조에서 전통적 회귀 보정이 실패하는 두 가지 이유를 설명한다: (1) Lₖ를 보정하면 이전 치료 Aₖ₋₁의 매개 효과를 차단하여 총효과를 과소추정하고, (2) Lₖ를 보정하지 않으면 교란이 남아 편향이 발생한다. 이 딜레마가 시간 변동 치료의 인과 추론에서 전통적 회귀 분석으로는 근본적으로 해결 불가능함을 보인다. 단순한 2시점 사례(항레트로바이러스 치료-CD4 수-사망)를 통해 치료-교란 피드백의 구조를 직관적으로 설명한다. 층화 분석, 결과 회귀, 성향점수 매칭 등 전통적 교란 보정 방법이 모두 이 구조에서 편향을 산출함을 수치적으로 시연한다. 이 장의 결론으로, 치료-교란 피드백이 존재할 때 일관된 인과효과 추정을 위해서는 g-방법(g-formula, IP 가중치, g-추정)이 필요함을 동기부여한다. 교란 변수가 치료의 영향을 받지 않는 단순한 경우와의 대비를 통해 피드백 구조의 독특한 난점을 부각한다.

### Ch 21: G-methods for time-varying treatments (pp. 271-298)

**핵심**: 시간 변동 치료를 위한 g-공식, IP 가중치, 이중 강건 추정량, g-추정의 구체적 적용을 다룬다. 중도절단을 시간 변동 치료로 취급하는 방법과 big g-formula를 소개한다.

**키워드**: `g-formula`, `IP weighting`, `doubly robust`, `g-estimation`, `big g-formula`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 21 (line 22734)
이 장은 시간 변동 치료를 위한 g-공식, IP 가중치, 이중 강건 추정량, g-추정의 구체적 적용을 다룬다. 시간 변동 IP 가중치(time-varying IP weights)를 구성하여 각 시점의 치료 배정 확률의 곱으로 안정화 가중치 SW를 계산하는 방법을 설명한다. 주변 구조 모형(MSM)을 시간 변동 치료 설정으로 확장하고, 가중 풀링 로지스틱 회귀(weighted pooled logistic regression)로 적합하는 과정을 시연한다. 중도절단을 시간 변동 치료의 한 형태로 취급하여, 치료 가중치와 중도절단 가중치를 결합하는 방법을 설명한다. 모수적 g-공식(big g-formula)을 시간 변동 설정으로 확장하며, 시점별 결과 모형과 공변량 모형을 순차적으로 시뮬레이션하여 반사실적 결과를 생성하는 절차를 설명한다. g-추정을 시간 변동 치료의 구조적 중첩 모형(SNMM)에 적용하는 방법을 다루며, 순차적 교환가능성을 활용한 추정 절차를 제시한다. 이중 강건(doubly robust) 추정량의 시간 변동 확장을 소개하고, 치료 모형과 결과 모형의 동시 사용이 제공하는 강건성 이점을 설명한다. 각 g-방법의 장단점(모형 명세 요구사항, 계산 복잡성, 동적 전략 적용 가능성)을 비교하며, 실무적 선택 지침을 제공한다. 세 가지 g-방법이 동일한 식별 가정(순차적 교환가능성, 양성, 일관성) 하에서 동일한 인과효과를 추정함을 강조한다.

### Ch 22: Target trial emulation (pp. 299-316)

**핵심**: 목표 시험 에뮬레이션(target trial emulation)의 개념을 정의한다. ITT 효과와 per-protocol 효과, 지속 치료 전략의 에뮬레이션, 시간 제로(time zero) 문제를 다루고, "What If" 질문에 대한 통합적 접근을 제시한다.

**키워드**: `target trial emulation`, `intention-to-treat`, `per-protocol`, `time zero`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 22 (line 24974)
이 장은 목표 시험 에뮬레이션(target trial emulation)의 개념을 정의하고, 관찰 데이터로 무작위 시험을 모방하는 방법론을 체계적으로 제시한다. 목표 시험의 프로토콜 요소(적격 기준, 치료 전략, 배정 절차, 추적 기간, 결과, 인과 대비, 분석 계획)를 정의하고, 각 요소를 관찰 데이터에서 어떻게 에뮬레이션하는지 설명한다. ITT(intention-to-treat) 효과와 per-protocol 효과의 차이를 설명하고, 관찰 연구에서 per-protocol 효과 추정이 IP 가중치 보정을 필요로 하는 이유를 논의한다. 지속 치료 전략(sustained treatment strategy)의 에뮬레이션에서 시간 제로(time zero)의 올바른 설정이 중요함을 강조하며, 시간 제로의 잘못된 설정이 불멸 시간 편향(immortal time bias)을 초래하는 구조를 분석한다. 클로닝(cloning) 기법을 이용하여 각 개인이 복수의 치료 전략에 할당된 것처럼 데이터를 구성하는 방법을 설명한다. 관찰 데이터에서의 적격성 조건 설정과 기저 공변량 측정의 실무적 고려사항을 다룬다. 복수 시험의 순차적 에뮬레이션(sequential trial emulation)과 풀링(pooling) 방법을 소개한다. "What If" 질문에 대한 통합적 접근으로서 목표 시험 에뮬레이션의 의의를 강조하며, 이것이 관찰 역학의 핵심 방법론임을 논증한다. 에뮬레이션의 타당성이 식별 가정(교환가능성, 양성, 일관성)에 의존함을 재확인한다.

### Ch 23: Causal mediation (pp. 317-325)

**핵심**: 매개 분석에 대한 비판과 옹호를 다루고, 경험적으로 검증 가능한 매개 효과와 개입주의적(interventionist) 매개 이론을 소개한다.

**키워드**: `mediation`, `direct effect`, `indirect effect`, `interventionist`

**상세**: → `causal inference what if - Miguel A. Hernan and James M. Robins.md` Ch 23 (line 26177)
이 장은 매개 분석(causal mediation)에 대한 비판과 옹호를 다루고, 현대적 매개 이론의 핵심 개념을 소개한다. 직접 효과(direct effect)와 간접 효과(indirect effect)의 반사실적 정의를 제시하며, 통제 직접 효과(controlled direct effect)와 자연 직접 효과(natural direct effect)를 구분한다. 통제 직접 효과 E[Y^{a=1,m} - Y^{a=0,m}]는 매개 변수 M을 특정 값 m으로 고정했을 때의 치료 효과로서, g-방법으로 식별 가능함을 설명한다. 자연 직접 효과 E[Y^{a=1,M^{a=0}} - Y^{a=0,M^{a=0}}]는 교차 세계(cross-world) 반사실을 포함하여 더 강한 가정(교차 세계 독립)을 요구함을 논의한다. 총효과를 자연 직접 효과와 자연 간접 효과로 분해하는 과정을 설명하고, 이 분해가 치료-매개 상호작용이 있을 때 4가지 성분으로 확장됨을 보인다. 매개 분석에 대한 전통적 비판(Baron-Kenny 접근의 한계, 교차 세계 가정의 비검증성, 매개 변수에 대한 보정이 충돌 변수 편향을 유발할 가능성)을 체계적으로 검토한다. 개입주의적(interventionist) 매개 이론을 소개하며, 매개 변수에 대한 확률적 개입(stochastic intervention)으로 교차 세계 가정을 회피하는 접근을 제시한다. 경험적으로 검증 가능한 매개 효과와 그렇지 않은 매개 효과를 구분하는 기준을 논의한다. 매개 분석이 인과 메커니즘 이해와 개입 설계에 기여하는 실무적 가치를 강조한다.
