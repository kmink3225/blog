---
name: "Survival Analysis: Techniques for Censored and Truncated Data (2nd Ed.)"
type: book-summary
sources:
  - file: "Klein-SurvivalAnalysisTechniques_azure_full.md"
    tool: Document Intelligence
authors: "John P. Klein, Melvin L. Moeschberger"
year: 2003
total_pages: 536
language: en
keywords: [survival analysis, censoring, truncation, Kaplan-Meier, Nelson-Aalen, hypothesis testing, proportional hazards, additive hazards, parametric models, frailty, competing risks, regression diagnostics]
---

# Survival Analysis: Techniques for Censored and Truncated Data (2nd Ed.) — Summary

> Klein & Moeschberger (2003), ~536 pages, 13 chapters + 3 appendices
> 중도절단 및 절단 데이터를 위한 이론적 기초와 실용적 기법을 균형 있게 다루는 생존분석 교재이다.

## Contents

- Chapter 1: Examples of Survival Data (pp. 1-20)
- Chapter 2: Basic Quantities and Models (pp. 21-62)
- Chapter 3: Censoring and Truncation (pp. 63-90)
- Chapter 4: Nonparametric Estimation of Basic Quantities for Right-Censored and Left-Truncated Data (pp. 91-138)
- Chapter 5: Estimation of Basic Quantities for Other Sampling Schemes (pp. 139-164)
- Chapter 6: Topics in Univariate Estimation (pp. 165-200)
- Chapter 7: Hypothesis Testing (pp. 201-242)
- Chapter 8: Semiparametric Proportional Hazards Regression with Fixed Covariates (pp. 243-294)
- Chapter 9: Refinements of the Semiparametric Proportional Hazards Model (pp. 295-328)
- Chapter 10: Additive Hazards Regression Models (pp. 329-352)
- Chapter 11: Regression Diagnostics (pp. 353-392)
- Chapter 12: Inference for Parametric Regression Models (pp. 393-424)
- Chapter 13: Multivariate Survival Analysis (pp. 425-442)
- Appendix A: Numerical Techniques for Maximization (p. 443)
- Appendix B: Large-Sample Tests Based on Likelihood Theory (p. 449)
- Appendix C: Statistical Tables (p. 455)

---

## Chapter Summaries

### Ch 1: Examples of Survival Data (pp. 1-20)

**핵심**: 의학, 생물학, 역학 등 다양한 분야에서의 시간-사건 데이터 예제를 제시한다. 급성 백혈병 관해 기간, 골수이식, 신장 투석 감염 시간, 유방암 사망시간, 화상환자 감염시간 등 19가지 실제 데이터셋을 소개하며, 중도절단과 절단의 개념을 예고한다.

**키워드**: `time-to-event data`, `leukemia`, `bone marrow transplant`, `clinical examples`, `censoring`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 1 (line 1065)

의학, 생물학, 역학 등 다양한 분야에서의 시간-사건 데이터 예제 19가지를 소개하며 생존분석의 기본 개념을 예고한다. 급성 백혈병 환자의 관해(remission) 유지 기간 데이터는 두 치료군 비교의 전형적 예제로 제시된다. 골수이식(bone marrow transplant) 데이터에서는 이식편대숙주질환, 재발, 사망 등 다양한 사건 유형이 경쟁위험 구조를 형성한다. 유방암 사망시간, 신장 투석 감염시간, 화상환자 감염시간 등 각 데이터셋의 연구 목적과 구조를 설명한다. 중도절단(censoring)의 개념을 예제를 통해 직관적으로 소개하며, 추적 종료나 탈락으로 인한 불완전 관측을 설명한다. 절단(truncation)의 개념도 예고하며, 좌절단(left truncation)이 발생하는 지연 진입(delayed entry) 상황을 소개한다. 각 데이터셋은 이후 장에서 비모수 추정, 가설검정, 회귀모형 적합 등의 예제로 반복 활용된다. 전통 의학 분야뿐 아니라 동물실험, 역학 연구, 임상시험 등 폭넓은 응용 맥락을 보여준다. 데이터 구조에서 생존시간, 중도절단 지시변수, 공변량의 기본 형식을 소개한다. 연속형과 이산형 생존시간의 차이, 동점(ties)의 발생 가능성도 언급한다. 이 장은 이론적 내용 없이 순수하게 예제 기반으로 생존분석의 필요성과 적용 범위를 동기부여한다.

---

### Ch 2: Basic Quantities and Models (pp. 21-62)

**핵심**: 생존 데이터 모형화의 기본 모수를 정의한다. 생존함수, 위험함수(hazard function), 평균잔여수명(mean residual life), 확률밀도함수의 상호관계를 설명한다. 지수, Weibull, log-logistic 등 일반적 모수적 모형과 회귀모형, 경쟁위험 모형을 소개한다.

**키워드**: `survival function`, `hazard function`, `mean residual life`, `parametric models`, `competing risks`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 2 (line 2714)

생존 데이터 모형화의 기본 모수인 생존함수, 위험함수, 평균잔여수명 등을 정의하고 상호관계를 유도한다. 생존함수 S(t) = P(T > t), 위험함수 h(t) = f(t)/S(t), 누적위험함수 H(t) = −log S(t)의 수학적 관계를 엄밀히 전개한다. 평균잔여수명(mean residual life) mrl(t) = E(T−t|T>t)은 시간 t까지 생존한 조건하에서의 잔여 기대수명이다. 지수분포는 h(t) = λ로 상수 위험을 가지며 무기억성(memoryless property)을 갖는 유일한 연속분포이다. Weibull 분포는 형상 모수에 따라 위험이 단조 증가 또는 감소하며, 지수분포를 특수 경우로 포함한다. log-logistic 분포는 위험이 단봉이 될 수 있어 비단조적 위험 패턴을 모형화할 수 있다. 로그정규(lognormal) 분포, 감마(gamma) 분포 등 기타 모수적 분포의 위험함수와 생존함수도 제시한다. 비례위험 모형 h(t|Z) = h_0(t)c(β'Z)과 가속실패시간 모형 S(t|Z) = S_0(te^{β'Z})의 일반적 형태를 소개한다. 경쟁위험(competing risks) 모형에서 원인별 위험함수와 전체 생존함수의 관계를 정의한다. 모수적 모형의 모수 추정 방법으로 모멘트법, 최대우도법, 최소제곱법을 간략히 언급한다. 각 분포의 특성과 적용 상황을 비교 정리하여 이후 장에서의 모형 선택에 대한 기반을 제공한다.

---

### Ch 3: Censoring and Truncation (pp. 63-90)

**핵심**: 중도절단과 절단의 유형을 엄밀히 정의한다. 우측중도절단(Type I, II, progressive, random), 좌측/구간 중도절단, 좌절단(left truncation)과 우절단(right truncation)을 구분하고, 각 유형에 맞는 우도함수 구성법을 설명한다. 계수과정(counting process) 기초도 포함한다.

**키워드**: `right censoring`, `left censoring`, `interval censoring`, `truncation`, `likelihood`, `counting process`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 3 (line 5405)

중도절단과 절단의 유형을 엄밀히 정의하고 각 유형에 맞는 우도함수 구성법을 체계적으로 설명한다. 우측중도절단의 유형으로 Type I(고정 시점), Type II(고정 사건 수), 점진적(progressive), 무작위(random) 중도절단을 구분한다. 좌측중도절단은 사건이 관찰 시작 전에 발생한 경우로, 구간중도절단은 사건이 특정 구간 내에서 발생한 경우이다. 좌절단(left truncation)은 연구 진입 시점 이전에 사건이 발생한 개인이 표본에 포함되지 않는 편향 표본추출이다. 우절단(right truncation)은 관찰 시점까지 사건이 발생하지 않은 개인이 표본에서 제외되는 경우이다. 각 중도절단·절단 유형에 대한 우도함수를 정확우도(exact likelihood), 이산화 우도, 조건부 우도로 구성하는 방법을 유도한다. 독립 중도절단 가정하에서 우도함수의 기여분은 비중도절단 관측치에서 밀도함수, 우측중도절단에서 생존함수, 좌측중도절단에서 누적분포함수이다. 구간중도절단 관측치의 우도 기여분은 S(L) − S(U)로 구간 내 확률을 반영한다. 계수과정(counting process)의 기초 개념으로 위험집합 과정 Y(t)와 사건 계수과정 N(t)를 도입한다. 강도함수(intensity function)와 마팅게일의 정의를 통해 이후 장의 비모수 추정과 가설검정의 이론적 기반을 마련한다. 각 유형의 데이터 구조를 구체적 예제를 통해 시각화하고 우도함수 구성을 시연한다.

---

### Ch 4: Nonparametric Estimation of Basic Quantities for Right-Censored and Left-Truncated Data (pp. 91-138)

**핵심**: 우측중도절단 데이터에서 생존함수와 누적위험함수의 비모수적 추정을 다룬다. Kaplan-Meier 추정량과 Nelson-Aalen 추정량을 유도하고, 생존함수의 점별 신뢰구간 및 신뢰대(confidence band), 평균/중앙 생존시간 추정, 좌절단 데이터와 경쟁위험에서의 요약 곡선을 설명한다.

**키워드**: `Kaplan-Meier`, `Nelson-Aalen`, `confidence band`, `left truncation`, `competing risks`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 4 (line 7022)

우측중도절단 및 좌절단 데이터에서 생존함수와 누적위험함수의 비모수적 추정 방법을 상세히 다룬다. Kaplan-Meier 추정량을 곱극한(product-limit) 추정으로 유도하며, 각 사건 시점에서의 조건부 확률 곱으로 생존함수를 추정한다. Nelson-Aalen 추정량은 누적위험함수를 직접 추정하며, Ĥ(t) = Σ d_j/n_j 형태로 각 사건 시점에서의 위험 기여분을 합산한다. 두 추정량의 관계에서 S_NA(t) = exp{−Ĥ(t)}와 KM 추정의 차이를 비교하고, 소표본에서의 상대적 성능을 논의한다. 생존함수의 점별(pointwise) 신뢰구간은 Greenwood 공식 기반이며, 로그 변환이나 보완 로그-로그 변환을 통해 개선된다. 신뢰대(confidence band)는 EP(equal precision)와 Hall-Wellner 두 유형이 있으며, 전체 시간 구간에 걸친 동시 신뢰영역을 제공한다. 평균 생존시간의 추정은 KM 곡선 아래 면적으로 구하되, 가장 긴 관측이 중도절단일 때 특정 시점까지의 제한 평균으로 산출한다. 중앙 생존시간과 기타 백분위수의 점추정과 신뢰구간을 KM 곡선으로부터 유도하는 방법을 설명한다. 좌절단(left truncation) 데이터에서는 절단 시점 이후에만 위험집합에 진입하도록 수정된 KM 추정을 사용한다. 경쟁위험 상황에서의 요약 곡선으로 누적발생함수(cumulative incidence function)의 비모수적 추정을 소개한다. 골수이식, 백혈병 관해 데이터 등을 통해 각 추정 방법의 적용과 해석을 시연한다.

---

### Ch 5: Estimation of Basic Quantities for Other Sampling Schemes (pp. 139-164)

**핵심**: 우측중도절단 이외의 표본추출 방식에서의 생존함수 추정을 다룬다. 좌중도절단, 이중중도절단(double censoring), 구간중도절단, 우절단(right truncation) 데이터와 그룹화 데이터(cohort life table)에서의 추정 기법을 설명한다.

**키워드**: `left censoring`, `double censoring`, `interval censoring`, `right truncation`, `life table`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 5 (line 11219)

우측중도절단 이외의 표본추출 방식에서의 생존함수 추정 기법을 다룬다. 좌중도절단 데이터에서는 역전된(reverse) KM 추정 또는 EM 알고리즘을 이용한 비모수적 최대우도 추정을 사용한다. 이중중도절단(double censoring)은 좌측과 우측 중도절단이 동시에 존재하는 경우로, 반복 알고리즘을 통해 생존함수를 추정한다. 구간중도절단 데이터에서의 비모수적 최대우도 추정(NPMLE)은 Turnbull 알고리즘(자기일관(self-consistency) 알고리즘)을 사용한다. 우절단(right truncation) 데이터에서의 생존함수 추정은 역시간(reverse time) KM 추정을 적용한다. 그룹화 데이터(cohort life table)에서의 보험수리적(actuarial) 추정은 각 구간 내에서 중도절단이 균일하게 발생한다는 가정을 사용한다. 각 표본추출 방식에서의 우도함수 구성과 최대우도 추정의 수학적 유도를 제시한다. NPMLE의 존재성과 유일성 조건, 수렴 속성에 대한 이론적 결과를 소개한다. 생존함수 추정치의 점근적(asymptotic) 분포와 분산 추정 방법도 다룬다. 각 방법의 실제 적용에서 소프트웨어 구현 시 고려할 사항을 논의한다. 수혈 관련 AIDS 데이터, 유방종양학 데이터 등을 통해 각 추정 방법을 시연한다.

---

### Ch 6: Topics in Univariate Estimation (pp. 165-200)

**핵심**: 위험함수의 추정에 관한 심화 주제를 다룬다. 커널 평활(kernel smoothing)을 이용한 위험함수의 평활 추정, 초과 사망률(excess mortality) 추정(역사적 대조군과의 비교), 베이지안 비모수적 방법을 설명한다.

**키워드**: `kernel smoothing`, `hazard estimation`, `excess mortality`, `Bayesian nonparametric`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 6 (line 14615)

위험함수의 추정에 관한 심화 주제를 다루며, 평활 추정, 초과 사망률, 베이지안 방법을 설명한다. 커널 평활(kernel smoothing) 위험함수 추정에서 대역폭(bandwidth)의 선택이 추정의 매끄러움과 편향-분산 균형에 핵심적이다. 고정 대역폭과 변동 대역폭(nearest-neighbor) 방법을 비교하며, 최적 대역폭 선택을 위한 교차검증(cross-validation)을 설명한다. 경계 효과(boundary effects)는 관찰 기간의 시작과 끝에서 발생하며, 경계 커널이나 반사(reflection) 방법으로 보정한다. 초과 사망률(excess mortality) 추정은 관찰된 사망률에서 일반 인구의 기대 사망률을 빼서 질병 관련 초과 위험을 산출한다. 상대생존(relative survival) S_r(t) = S(t)/S*(t)는 질병이 없었다면 기대되는 생존과 비교한 상대적 생존확률이다. 초과 사망률 추정에는 일반 인구 생명표(population life table)가 필요하며, 연령·성별·연도별 보정이 중요하다. 베이지안 비모수적 방법에서 디리클레 과정(Dirichlet process) 사전분포를 사용한 생존함수 추정을 소개한다. 디리클레 과정 사전분포의 모수 α는 사전정보의 강도를, 기저 분포 F_0는 사전 추측을 반영한다. 사전정보가 약할 때(α → 0) 사후 추정은 KM 추정으로 수렴하며, 강할 때 사전 분포 F_0에 가까워진다. 커널 평활 추정의 점근적 성질, 편향, 평균제곱오차 등 이론적 결과를 제시한다. 골수이식 후 급성 이식편대숙주질환 데이터와 당뇨병 사망률 데이터 등을 통해 각 방법을 시연한다.

---

### Ch 7: Hypothesis Testing (pp. 201-242)

**핵심**: Nelson-Aalen 추정량의 관측값과 기대값의 가중 차이에 기반한 가설검정을 다룬다. 일표본 검정, 이표본 이상의 비교, 추세 검정, 층화 검정, Renyi 유형 검정, 고정 시점에서의 결과 차이 검정 등 다양한 검정법을 설명한다.

**키워드**: `log-rank test`, `Wilcoxon test`, `stratified test`, `trend test`, `Renyi test`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 7 (line 17984)

Nelson-Aalen 추정량의 관측값과 기대값의 가중 차이에 기반한 다양한 가설검정을 체계적으로 다룬다. 일표본 검정에서는 특정 모수적 분포(예: 지수분포)에 대한 적합도를 검정하며, 관측-기대 차이의 통계적 유의성을 평가한다. 이표본 비교의 일반적 형태는 U = Σ W_j(d_{1j} − e_{1j})로, 가중치 W_j의 선택에 따라 다양한 검정이 도출된다. log-rank 검정(W_j = 1)은 비례위험 대안에 최적이며, Wilcoxon(Gehan) 검정(W_j = n_j)은 초기 차이에 민감하다. Peto-Peto 검정은 생존함수 기반 가중치를 사용하여 후기 중도절단에 대해 log-rank보다 안정적이다. Tarone-Ware 검정(W_j = √n_j)은 log-rank과 Wilcoxon의 절충적 성격을 갖는다. 세 그룹 이상의 비교에서는 자유도 K−1의 카이제곱 검정으로 확장되며, 추세 검정(trend test)은 순서형 그룹 변수에 적용된다. 층화 검정(stratified test)은 교란변수의 층 내에서 검정통계량을 합산하여 보정된 비교를 수행한다. Renyi 유형 검정은 sup|U(t)| 형태의 통계량으로, 비비례위험 대안에서 더 강력할 수 있다. 고정 시점에서의 생존확률 차이 검정과 제한 평균 생존시간(RMST) 비교 방법도 소개한다. 각 검정의 점근적 분포, 검정력 비교, 적용 시 주의사항을 이론과 예제를 통해 설명한다.

---

### Ch 8: Semiparametric Proportional Hazards Regression with Fixed Covariates (pp. 243-294)

**핵심**: 고정 공변량을 갖는 준모수적 비례위험 회귀모형(Cox 모형)을 상세히 다룬다. 공변량 코딩 방법, 구별 사건시간의 편우도(partial likelihood), 동점 처리, 국소 검정, 연속 공변량의 이산화, 모형 구축, 생존함수 추정을 설명한다.

**키워드**: `Cox model`, `partial likelihood`, `covariate coding`, `model building`, `survival function estimation`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 8 (line 20974)

고정 공변량을 갖는 준모수적 비례위험 회귀모형(Cox 모형)을 상세히 다룬다. 공변량 코딩 방법으로 이분 변수의 0-1 코딩, 다범주 변수의 더미 변수 코딩, 연속 변수의 원값 사용을 설명한다. 편우도(partial likelihood) 구성에서 구별 사건시간에서의 기여분을 유도하며, 기저 위험함수가 소거되는 원리를 보인다. 동점(tied) 사건시간의 처리에서 Breslow 근사와 Efron 근사를 비교하며, 정확(exact) 편우도 방법도 제시한다. 최대편우도 추정치의 점근적 정규성과 분산 추정을 관측 정보행렬의 역행렬로 구하는 과정을 설명한다. 국소 검정(local tests)으로 우도비 검정, Wald 검정, 스코어 검정의 세 가지를 비교하고 각각의 장단점을 논의한다. 연속 공변량의 이산화(discretization) 방법과 이에 따른 정보 손실·해석 편의의 트레이드오프를 설명한다. 모형 구축(model building)에서 전진·후진·단계적 선택법과 AIC 기반 비교를 다룬다. 기저 생존함수의 추정에서 Breslow 추정량과 그 분산, 공변량 보정 생존함수의 산출을 설명한다. 각 사건시간에서의 위험비 해석과 신뢰구간 구성을 상세히 다룬다. 백혈병 관해, 후두암, 골수이식 데이터 등을 통해 Cox 모형의 적합과 해석을 시연한다.

---

### Ch 9: Refinements of the Semiparametric Proportional Hazards Model (pp. 295-328)

**핵심**: Cox 모형의 정교화를 다룬다. 시간의존 공변량(time-dependent covariates), 층화 비례위험 모형, 좌절단(left truncation) 처리, 시간 변동 효과의 종합(다상태 모형, multistate modeling)을 설명한다.

**키워드**: `time-dependent covariates`, `stratified model`, `left truncation`, `multistate model`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 9 (line 24445)

Cox 모형의 정교화로서 시간의존 공변량, 층화 모형, 좌절단, 다상태 모형을 다룬다. 시간의존 공변량은 내부(internal)와 외부(external) 유형으로 구분되며, 편우도에서 위험집합 계산 시 각 시점의 공변량 값을 사용한다. 시간의존 공변량이 포함되면 위험비가 시간에 따라 변하므로 모형은 더 이상 비례위험이 아니다. 데이터 구조는 계수과정 형식의 (시작, 끝] 시간 구간으로 분할하며, 각 구간에서 공변량이 상수이다. 층화 비례위험 모형은 층별로 별도의 기저 위험함수를 허용하면서 공변량 효과는 층 간에 공통으로 추정한다. 층화 편우도는 각 층의 편우도의 곱으로 구성되며, 위험집합은 층 내에서만 형성된다. 좌절단(left truncation)은 개인이 특정 시점 이후에만 관찰에 진입하는 경우로, 위험집합을 적절히 수정하여 편우도에 반영한다. 시간 변동 효과(time-varying effects)의 모형화에서 PH 가정 위반 시 시간-공변량 교호작용을 포함하는 방법을 설명한다. 다상태 모형(multistate model)은 개인이 여러 상태를 거치는 과정을 전이 강도(transition intensity)로 모형화하며, 경쟁위험은 특수 경우이다. 각 정교화의 편우도 구성, 추정, 해석 방법을 수학적으로 전개한다. 골수이식, 당뇨망막병증 등 예제를 통해 시간의존 공변량과 층화 모형의 적합을 시연한다.

---

### Ch 10: Additive Hazards Regression Models (pp. 329-352)

**핵심**: 비례위험 모형의 대안으로 가법적 위험 모형(additive hazards model)을 다룬다. 위험함수를 공변량의 선형 결합으로 모형화하며, Aalen의 비모수적 가법 위험 모형과 Lin-Ying의 반모수적 가법 위험 모형을 설명한다.

**키워드**: `additive hazards`, `Aalen model`, `Lin-Ying model`, `nonparametric regression`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 10 (line 26983)

비례위험 모형의 대안으로 가법적 위험 모형(additive hazards model)을 다루며, 두 가지 주요 접근을 설명한다. Aalen의 비모수적 가법 위험 모형은 h(t|Z) = β_0(t) + β_1(t)Z_1 + ... + β_p(t)Z_p로, 계수가 시간의 함수이다. 누적 회귀함수 B_j(t) = ∫β_j(s)ds를 Nelson-Aalen 유사 추정량으로 추정하며, 그 도표가 핵심 진단 도구이다. B_j(t) 도표가 직선이면 해당 공변량의 효과가 시간에 걸쳐 일정함을 의미하며, 곡률은 시간에 따른 효과 변화를 나타낸다. Lin-Ying의 반모수적 가법 위험 모형은 h(t|Z) = h_0(t) + β'Z로 계수가 시간에 의존하지 않는 간결한 형태이다. Lin-Ying 모형에서 β의 추정은 계수과정 이론에 기반한 추정방정식을 풀어 구하며, 점근적 정규성을 갖는다. 가법 모형의 장점은 효과를 위험의 절대적 변화(absolute change)로 해석할 수 있어 공중보건 관점에서 유용하다는 것이다. 반면 가법 모형은 추정된 위험이 음수가 될 수 있다는 한계가 있어, 실무에서 주의가 필요하다. 비례위험 모형과 가법 모형을 결합한 모형이나, Aalen 모형을 비례위험 가정 검토 도구로 활용하는 방법도 논의한다. 가법 모형의 적합도 검정과 모형 진단 방법을 설명한다. 백혈병 관해, 골수이식, 신장투석 데이터를 통해 두 가법 모형의 적합과 해석을 시연한다.

---

### Ch 11: Regression Diagnostics (pp. 353-392)

**핵심**: Cox 모형의 회귀진단을 다룬다. Cox-Snell 잔차를 이용한 모형 적합 평가, 마팅게일 잔차를 이용한 공변량의 함수 형태 결정, PH 가정의 그래프적 검토, 편차 잔차(deviance residuals), 개별 관측치의 영향력 평가를 설명한다.

**키워드**: `Cox-Snell residuals`, `martingale residuals`, `deviance residuals`, `influence diagnostics`, `PH assumption`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 11 (line 28245)

Cox 모형의 회귀진단을 체계적으로 다루며, 다양한 잔차를 이용한 모형 평가 방법을 설명한다. Cox-Snell 잔차는 추정된 누적위험함수 값으로, 올바른 모형이면 단위 지수분포를 따르며 전반적 적합도 평가에 사용된다. Cox-Snell 잔차에 대한 Nelson-Aalen 추정의 누적위험을 45도 직선과 비교하여 모형 적합도를 그래프적으로 평가한다. 마팅게일 잔차는 관측 사건 수와 기대 사건 수의 차이로, 공변량의 함수 형태 결정에 핵심적이다. 공변량의 함수 형태는 null 모형의 마팅게일 잔차를 해당 공변량에 대해 산점도로 그리고 평활곡선을 적합하여 결정한다. PH 가정의 그래프적 검토에서 로그-로그 생존곡선의 평행성, 관측 vs. 기대 도표, Schoenfeld 잔차의 시간 도표를 사용한다. 편차 잔차(deviance residuals)는 마팅게일 잔차를 대칭적으로 변환한 것으로, 이상 관측치 식별에 적합하다. 개별 관측치의 영향력 평가에서 dfbeta 잔차는 각 관측치 제거 시 계수 변화를 근사적으로 측정한다. 지렛대(leverage) 잔차는 공변량 공간에서 극단적 위치에 있는 관측치를 식별한다. 모형 검토의 종합적 절차로서 적합도, PH 가정, 함수 형태, 영향력 분석을 순차적으로 수행할 것을 권고한다. 후두암, 백혈병, 골수이식 데이터를 통해 각 진단 방법의 적용과 해석을 시연한다.

---

### Ch 12: Inference for Parametric Regression Models (pp. 393-424)

**핵심**: 모수적 모형을 이용한 생존 회귀분석을 다룬다. 가속실패시간(AFT) 모형의 로그 선형 표현을 기본으로 하여 Weibull, log-logistic 분포 및 기타 모수적 모형의 추정, 진단 방법을 설명한다. 모수적 모형이 적합할 때 비모수 방법보다 정밀한 추정이 가능함을 보인다.

**키워드**: `AFT model`, `Weibull regression`, `log-logistic regression`, `parametric diagnostics`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 12 (line 31548)

모수적 모형을 이용한 생존 회귀분석을 다루며, AFT 모형의 로그 선형 표현을 기본으로 한다. AFT 모형은 log T = μ + α'Z + σε 형태로, 오차항 ε의 분포에 따라 Weibull, log-logistic, 로그정규 등의 모형이 결정된다. Weibull 회귀모형에서 오차항은 극소값(extreme minimum value) 분포를 따르며, PH 모형과 AFT 모형 모두로 해석 가능하다. log-logistic 회귀모형에서 오차항은 로지스틱 분포를 따르며, 비례오즈(proportional odds) 구조를 갖는다. 각 모수적 모형의 최대우도 추정에서 중도절단을 반영한 우도함수를 구성하고, 뉴턴-랩슨법으로 최대화한다. AFT 모형의 가속인자(acceleration factor) exp(α)는 공변량이 생존시간의 스케일에 미치는 승법적 효과를 나타낸다. 모수적 모형이 적합할 때 비모수 방법보다 정밀한 추정(더 작은 표준오차)이 가능함을 보인다. 분포 선택을 위해 표준화 잔차의 확률도표, AIC 비교, Cox-Snell 잔차의 지수분포 적합도를 사용한다. 진단 방법으로 표준화 잔차 도표, Cox-Snell 잔차 도표, 영향력 분석을 설명한다. 일반화 감마 분포는 Weibull, 로그정규, 감마를 특수 경우로 포함하는 유연한 분포 계열이다. 후두암, 화상환자 데이터를 통해 각 모수적 모형의 적합, 비교, 진단을 시연한다.

---

### Ch 13: Multivariate Survival Analysis (pp. 425-442)

**핵심**: 독립성 가정이 적절하지 않은 다변량 생존 데이터(형제, 부부, 동일 개인 내 반복 사건 등)의 분석을 다룬다. 프레일티(frailty) 모형을 통한 하위그룹 내 연관성 모형화, 감마 프레일티의 추정, 주변 모형(marginal model)을 설명한다.

**키워드**: `multivariate survival`, `frailty model`, `gamma frailty`, `marginal model`, `correlated survival`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 13 (line 33839)

독립성 가정이 적절하지 않은 다변량 생존 데이터의 분석을 다루며, 프레일티 모형과 주변 모형을 설명한다. 다변량 생존 데이터는 형제, 부부, 동일 개인 내 반복 사건, 쌍체 기관(눈, 귀, 신장) 등에서 발생한다. 프레일티(frailty) 모형은 하위그룹 내 개인들이 공유하는 미관측 랜덤효과를 통해 그룹 내 연관성을 모형화한다. 감마 프레일티 모형에서 공유 프레일티 z는 평균 1, 분산 θ의 감마분포를 따르며, θ가 0이면 독립 모형으로 환원된다. 감마 프레일티의 추정은 EM 알고리즘을 사용하며, E-단계에서 프레일티의 조건부 기대값을 계산하고 M-단계에서 모수를 갱신한다. 벌칙 편우도(penalized partial likelihood) 방법은 편우도에 프레일티의 벌칙항을 추가하여 동시에 β와 프레일티를 추정한다. 프레일티 분산 θ의 유의성 검정은 경계 문제(boundary problem)로 인해 표준 카이제곱이 아닌 혼합분포를 사용한다. 주변 모형(marginal model)은 Wei-Lin-Weissfeld(WLW) 접근으로, 각 사건에 대해 별도의 주변 비례위험 모형을 적합하고 로버스트 분산을 사용한다. 주변 모형은 프레일티의 분포 가정 없이 공변량의 주변적(marginal) 효과를 추정하며, 해석이 인구 수준에 적합하다. 프레일티 모형(조건부 효과)과 주변 모형(주변 효과)의 해석 차이를 비교한다. 골수이식, 신장이식, 당뇨망막병증 데이터를 통해 두 접근법의 적합과 해석을 시연한다.
