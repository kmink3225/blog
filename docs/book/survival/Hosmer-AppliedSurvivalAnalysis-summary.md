---
name: "Applied Survival Analysis: Regression Modeling of Time-to-Event Data (2nd Ed.)"
type: book-summary
source_file: "Hosmer-AppliedSurvivalAnalysis_azure_full.md"
authors: "David W. Hosmer, Stanley Lemeshow, Susanne May"
year: 2008
total_pages: 392
language: en
keywords: [survival analysis, regression modeling, proportional hazards, Kaplan-Meier, model development, model adequacy, parametric models, recurrent events, frailty, competing risks]
---

# Applied Survival Analysis: Regression Modeling of Time-to-Event Data (2nd Ed.) — Summary

> Hosmer, Lemeshow & May (2008), ~392 pages, 9 chapters + 3 appendices
> 시간-사건 데이터의 회귀모형에 초점을 맞춘 실용적 교재로, 데이터 기반 모형 구축 패러다임을 생존분석에 적용한다.

## Contents

- Chapter 1: Introduction to Regression Modeling of Survival Data (pp. 1-15)
- Chapter 2: Descriptive Methods for Survival Data (pp. 16-66)
- Chapter 3: Regression Models for Survival Data (pp. 67-91)
- Chapter 4: Interpretation of a Fitted Proportional Hazards Regression Model (pp. 92-131)
- Chapter 5: Model Development (pp. 132-168)
- Chapter 6: Assessment of Model Adequacy (pp. 169-206)
- Chapter 7: Extensions of the Proportional Hazards Model (pp. 207-243)
- Chapter 8: Parametric Regression Models (pp. 244-285)
- Chapter 9: Other Models and Topics (pp. 286-354)
- Appendix 1: The Delta Method (p. 355)
- Appendix 2: An Introduction to the Counting Process Approach to Survival Analysis (p. 359)
- Appendix 3: Percentiles for Computation of the Hall and Wellner Confidence Band (p. 364)

---

## Chapter Summaries

### Ch 1: Introduction to Regression Modeling of Survival Data (pp. 1-15)

**핵심**: 회귀모형의 일반적 패러다임(체계적 성분과 오차 성분의 선택)을 생존 데이터에 적용하는 방법을 소개한다. 선형회귀, 로지스틱회귀와의 유사성을 비교하며, 우측중도절단(right censoring) 메커니즘의 유형(Type I, Type II, random)을 설명한다. WHAS100 등 예제 데이터셋을 소개한다.

**키워드**: `regression paradigm`, `censoring mechanisms`, `time-to-event`, `WHAS100`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 1 (line 488)

회귀모형의 일반적 패러다임(체계적 성분과 오차 성분의 선택)을 생존 데이터에 적용하는 접근법을 소개한다. 선형회귀에서의 정규 오차, 로지스틱회귀에서의 이항 오차와 유사하게, 생존분석에서는 시간-사건 데이터에 맞는 체계적·오차 성분을 선택해야 한다. 생존시간의 관찰에는 시작점(clock starts)과 종료점(clock stops)의 명확한 정의가 필수적이다. WHAS100 데이터셋(Worcester Heart Attack Study)을 통해 심근경색 환자의 입원 후 생존시간 분석 문제를 예시한다. 중도절단(censoring)은 생존시간의 불완전 관측으로, 우측중도절단이 가장 흔한 유형이다. Type I 중도절단은 모든 대상자가 동일 시점까지 추적되는 경우, Type II 중도절단은 특정 수의 사건이 관측될 때까지 추적하는 경우이다. 무작위 중도절단(random censoring)은 대상자마다 다른 시점에 추적이 끝나는 실제 연구에서 가장 일반적인 유형이다. 좌측 중도절단과 구간 중도절단의 개념도 소개하며, 좌절단(left truncation)과의 구분을 설명한다. 본서에서 사용될 다양한 예제 데이터셋(WHAS100, WHAS500, ACTG320, UIS 등)을 소개한다. 각 데이터셋의 연구 목적, 변수 구성, 중도절단 특성을 설명하여 이후 장에서의 분석 기반을 마련한다.

---

### Ch 2: Descriptive Methods for Survival Data (pp. 16-66)

**핵심**: 중도절단 데이터에서 누적분포함수와 생존함수를 추정하는 방법을 설명한다. Kaplan-Meier 추정량, 생존함수의 활용(중앙값, 사분위수 추정), 생존함수 비교를 위한 log-rank 등 검정법, 위험함수(hazard function) 및 관련 추정량을 다룬다.

**키워드**: `Kaplan-Meier`, `survival function`, `log-rank test`, `hazard function`, `kernel smoothing`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 2 (line 2613)

중도절단 데이터에서 누적분포함수와 생존함수를 추정하는 기술적 방법을 설명한다. Kaplan-Meier 추정량은 각 사건 시점에서의 조건부 생존확률의 곱으로 생존함수를 추정하며, 중도절단 관측치도 위험집합에 기여한다. KM 추정의 핵심은 각 시점에서 (n−d)/n으로 조건부 생존확률을 계산하고 이를 누적 곱으로 구하는 것이다. 동점(ties) 생존시간의 처리에서는 중도절단이 사건 직후에 발생한 것으로 간주하며, 다수의 동시 사건은 동일한 조건부 확률로 처리한다. 생존함수의 신뢰구간은 Greenwood 공식 기반의 점별(pointwise) 구간과 Hall-Wellner, EP 신뢰대(confidence band)를 포함한다. 중앙 생존시간과 사분위수는 KM 곡선에서 해당 확률 수준을 교차하는 시점으로 추정하며, 95% 신뢰구간을 제공한다. 두 그룹 이상의 생존경험 비교를 위해 log-rank 검정, Wilcoxon(Gehan) 검정, Tarone-Ware 검정, Peto-Peto 검정 등을 소개한다. 각 검정은 가중 방식의 차이로 조기 vs. 후기 사건에 대한 민감도가 다르며, 연구 목적에 따라 선택한다. 위험함수의 추정에서는 Nelson-Aalen 누적위험추정량과 커널 평활(kernel smoothing)을 이용한 매끄러운 위험함수 추정을 설명한다. 커널 평활 위험함수는 대역폭(bandwidth) 선택에 민감하며, 위험의 시간적 패턴을 시각적으로 파악하는 데 유용하다. WHAS100 데이터에 대한 상세한 적용 예제를 통해 각 방법의 계산 과정과 결과 해석을 시연한다.

---

### Ch 3: Regression Models for Survival Data (pp. 67-91)

**핵심**: 위험함수에 회귀 구조를 도입하는 방법을 다루며, 준모수적(semiparametric) 비례위험모형의 수리적 기초를 설명한다. 편우도(partial likelihood)를 이용한 모형 적합, 동점(tied) 생존시간의 처리, 그리고 비례위험 회귀모형의 생존함수 추정 방법을 제시한다.

**키워드**: `semiparametric model`, `proportional hazards`, `partial likelihood`, `tied survival times`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 3 (line 5889)

위험함수에 회귀 구조를 도입하는 방법을 다루며, 준모수적 비례위험모형의 수리적 기초를 설명한다. 위험함수가 시간 변화를 반영하는 가장 적절한 함수이므로, 회귀모형의 체계적 성분으로 위험함수를 모형화한다. Cox(1972)가 제안한 비례위험 모형 h(t,x,β) = h_0(t)exp(xβ)에서 기저 위험함수 h_0(t)는 미지정(unspecified)으로 남긴다. 위험비(hazard ratio)는 h_0(t)가 소거되어 시간에 의존하지 않으며, HR = exp{β(x_1 − x_0)} 형태로 해석이 직관적이다. 생존함수는 S(t,x,β) = [S_0(t)]^{exp(xβ)}로 표현되며, 기저 생존함수의 거듭제곱 형태를 갖는다. 편우도(partial likelihood)는 기저 위험함수를 포함하지 않으면서 β 추정을 가능하게 하는 핵심 도구이다. 편우도의 구성에서 각 사건 시점의 기여분은 해당 위험집합(risk set) 내에서 사건 발생 개인의 상대 위험 비율이다. 동점(tied) 생존시간의 처리에는 Breslow 근사, Efron 근사, 정확 방법이 있으며, 동점이 많을수록 Efron이 Breslow보다 정확하다. β의 최대편우도 추정치는 뉴턴-랩슨(Newton-Raphson) 반복법으로 구하며, 분산 추정은 관측 정보행렬의 역행렬로 얻는다. 기저 위험함수와 생존함수의 추정에는 Breslow-Nelson-Aalen 방법을 사용하며, 이는 적합 후 단계에서 수행된다. 가법 모형(additive model) h(t,x,β) = h_0(t)(1 + xβ) 등 대안적 모형 구조도 간략히 언급한다.

---

### Ch 4: Interpretation of a Fitted Proportional Hazards Regression Model (pp. 92-131)

**핵심**: 적합된 PH 모형의 계수를 실질적으로 해석하는 방법을 설명한다. 명목형(nominal), 연속형(continuous) 공변량에 대한 해석, 다중 공변량 모형에서의 통계적 보정과 교호작용(interaction) 해석, 공변량 보정 생존함수의 해석과 활용을 다룬다.

**키워드**: `hazard ratio`, `nominal covariate`, `continuous covariate`, `interaction`, `adjusted survival function`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 4 (line 7153)

적합된 비례위험 모형의 계수를 실질적으로 해석하는 방법을 설명한다. 연결함수(link function)는 로그 변환으로, 로그위험의 차이가 공변량에 대해 선형이며 시간에 의존하지 않는다. 이분 공변량의 경우 exp(β)가 위험비이며, 이는 전 추적 기간에 걸쳐 한 그룹의 순간 사망률이 다른 그룹의 몇 배인지를 나타낸다. 위험비는 특정 시점의 사건 발생 확률 비교인 오즈비와 구별되며, 시간 전체에 걸친 비율(rate) 비교이다. 연속형 공변량의 위험비는 HR = exp{β(a−b)}로 비교 단위(a−b)의 선택이 해석에 중요하다. 다범주 명목형 공변량은 더미 변수(design variables)로 코딩하며, 기준 범주 대비 각 범주의 위험비를 산출한다. 다변량 모형에서 각 계수는 다른 공변량을 통제(adjusted)한 효과를 나타내며, 교란(confounding)의 영향을 평가한다. 교호작용(interaction)이 포함된 모형에서 위험비는 주효과와 교호작용 계수를 결합하여 산출하며, 해석이 복잡해진다. 공변량 보정 생존함수(covariate-adjusted survival function)는 특정 공변량 값에서의 생존곡선을 추정하며, 치료 비교에 유용하다. 보정 생존함수는 S(t,x) = [S_0(t)]^{exp(xβ̂)} 형태로 기저 생존함수의 거듭제곱으로 산출된다. WHAS100 데이터의 성별, 연령, BMI에 대한 위험비 추정과 보정 생존곡선을 예제로 제시한다.

---

### Ch 5: Model Development (pp. 132-168)

**핵심**: PH 회귀분석에서 공변량 선택의 실무적 방법을 다룬다. 목적적 선택(purposeful selection), 연속형 공변량의 로그위험에서의 스케일 검토, 단계적 선택(stepwise), 최적부분집합(best-subsets), 다변량 분수다항식(multivariable fractional polynomial) 방법을 비교 설명한다. 수치적 문제도 논의한다.

**키워드**: `purposeful selection`, `stepwise`, `best subsets`, `fractional polynomials`, `model building`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 5 (line 10073)

비례위험 회귀분석에서 공변량 선택의 실무적 방법을 7단계 절차로 체계적으로 다룬다. 목적적 선택(purposeful selection)은 단변량 분석에서 유의한 변수(20-25% 수준)와 임상적으로 중요한 변수로 시작한다. 변수 제거 시 잔류 변수의 계수가 20% 이상 변하면 해당 변수는 교란변수(confounder)로 모형에 유지해야 한다. 단계적 선택(stepwise selection)은 전진, 후진 또는 양방향 방식으로 통계적 기준에 의해 자동으로 변수를 선택한다. 최적부분집합(best-subsets) 방법은 가능한 모든 변수 조합 중 최적 모형을 AIC나 편우도 등으로 평가한다. 연속형 공변량의 로그위험에서의 함수 형태를 확인하기 위해 사분위 설계변수 방법과 분수다항식(fractional polynomials)을 사용한다. 분수다항식은 p ∈ {−2, −1, −0.5, 0, 0.5, 1, 2, 3} 집합에서 최적 거듭제곱을 탐색하여 비선형 효과를 포착한다. 다변량 분수다항식(MFP)은 변수 선택과 변환을 반복적으로 동시 수행하는 방법이다. 교호작용의 포함 여부는 주효과 모형 완성 후 각 가능한 교호작용을 편우도비 검정으로 평가하여 결정한다. 사건 수 대비 공변량 수의 비율로서 10 사건당 1 공변량의 경험적 지침을 제시하며, 과적합 방지를 강조한다. WHAS500 데이터에 대한 목적적 선택, 단계적 선택, 최적부분집합, MFP 방법의 적용을 비교 시연한다.

---

### Ch 6: Assessment of Model Adequacy (pp. 169-206)

**핵심**: 적합된 모형의 타당성을 평가하는 방법을 다룬다. 잔차(residuals) 분석, PH 가정의 평가, 영향력 있는 관측치 및 적합이 나쁜 대상의 식별, 전반적 적합도(goodness-of-fit) 평가, 최종 모형의 해석 및 결과 제시 방법을 설명한다.

**키워드**: `residuals`, `proportional hazards assumption`, `influential observations`, `goodness-of-fit`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 6 (line 13247)

적합된 비례위험 모형의 타당성을 평가하는 방법을 체계적으로 다룬다. 생존 데이터에서는 중도절단과 편우도 사용으로 인해 표준적 '관측-예측' 잔차가 존재하지 않아 여러 유형의 잔차가 개발되었다. Schoenfeld 잔차는 각 사건 시점에서 공변량 값과 위험집합 가중 평균의 차이로 정의되며, PH 가정 검토에 핵심적이다. 척도 조정된 Schoenfeld 잔차(scaled Schoenfeld residuals)에 β̂를 더하고 시간에 대해 평활하면 시간에 따른 계수 변화를 시각화할 수 있다. PH 가정의 통계적 검정은 척도 조정된 Schoenfeld 잔차를 시간 변환 함수에 대해 회귀하여 기울기의 유의성으로 평가한다. 마팅게일 잔차는 관측 사건 수와 모형 기대 사건 수의 차이이며, 공변량의 함수 형태와 전반적 적합도를 평가하는 데 사용된다. 편차 잔차(deviance residuals)는 마팅게일 잔차를 대칭적으로 변환한 것으로, 적합이 나쁜 관측치 식별에 유용하다. 영향력 분석에서 dfbeta 잔차는 각 관측치가 계수 추정에 미치는 영향을 측정하며, 지렛대(leverage) 통계량은 극단적 공변량 값을 가진 관측치를 식별한다. 전반적 적합도(goodness-of-fit) 평가에는 May-Hosmer 검정(위험 그룹별 관측-기대 비교)을 사용한다. 최종 모형의 해석에서는 위험비, 신뢰구간, 보정 생존곡선을 표와 그래프로 제시하는 방법을 설명한다. WHAS500 데이터에 대한 모형 진단의 전체 과정을 단계별로 시연한다.

---

### Ch 7: Extensions of the Proportional Hazards Model (pp. 207-243)

**핵심**: 기본 PH 모형의 확장을 다룬다. 층화 PH 모형(stratified PH model), 시간의존 공변량(time-varying covariates), 절단(truncated) 데이터, 좌측 중도절단 및 구간 중도절단(interval censored) 데이터의 처리 방법을 설명한다.

**키워드**: `stratified model`, `time-varying covariates`, `truncation`, `left censoring`, `interval censoring`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 7 (line 16174)

기본 비례위험 모형의 주요 확장을 다루며, 다양한 데이터 구조에 대응하는 방법을 설명한다. 층화 PH 모형(stratified PH model)은 각 층에 별도의 기저 위험함수를 허용하면서 공변량 효과는 층 간에 동일하게 추정한다. 층화는 PH 가정을 위반하는 공변량이나 연구 설계상 중요하지만 효과 추정이 불필요한 변수에 대해 적용한다. 층화 편우도는 각 층의 편우도를 곱한 것으로 구성되며, 위험집합은 층 내에서만 형성된다. 시간의존 공변량(time-varying covariates)은 추적 기간 중 값이 변하는 변수로, 환자의 생리적 상태 변화 등을 반영한다. 시간의존 공변량의 모형화에서 데이터는 계수과정 형식의 시간 구간으로 분할하며, 각 구간에서 공변량 값이 상수이다. PH 가정 위반 시 시간-공변량 교호작용 항을 모형에 포함하여 시간에 따른 효과 변화를 모형화할 수 있다. 절단(truncation) 데이터에서 좌절단(left truncation)은 일정 시점 이후에만 관찰이 시작되는 경우로, 지연 진입(delayed entry)이라고도 한다. 구간 중도절단(interval censoring) 데이터는 이산시간 모형이나 보완 로그-로그 모형으로 분석할 수 있다. 좌측 중도절단 데이터의 처리 방법과 이중 중도절단(doubly censored) 데이터의 분석도 간략히 다룬다. ACTG320 데이터에 대한 CD4 사분위 층화 모형 적합을 예제로 제시한다.

---

### Ch 8: Parametric Regression Models (pp. 244-285)

**핵심**: 완전 모수적 모형의 장점(ML 추정, 예측값 산출, 잔차 계산)을 설명하며, 가속실패시간(AFT) 모형 계열을 다룬다. 지수(exponential), Weibull, log-logistic 회귀모형을 상세히 설명하고, 기타 모수적 모형에 대해서도 간략히 언급한다.

**키워드**: `AFT model`, `exponential`, `Weibull`, `log-logistic`, `maximum likelihood`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 8 (line 18802)

완전 모수적 모형의 장점과 가속실패시간(AFT) 모형 계열을 체계적으로 다룬다. 모수적 모형은 완전 최대우도 추정, 예측값 산출, 관측-예측 잔차 계산이 가능하여 선형회귀와 유사한 분석 경험을 제공한다. AFT 모형은 T = exp(β_0 + β_1 x) × ε 형태로, 로그 변환하면 ln(T) = β_0 + β_1 x + σε*로 선형화된다. 지수(exponential) 회귀모형은 위험함수가 상수인 가장 단순한 AFT 모형으로, 시간비(time ratio) exp(β_1)로 공변량 효과를 해석한다. Weibull 회귀모형은 형상 모수 σ를 추가하여 단조적 위험함수를 허용하며, AFT 모형과 PH 모형 모두로 해석 가능한 유일한 분포이다. Weibull 모형에서 가속인자(acceleration factor) exp(β)와 위험비 exp(−β/σ)는 부호가 반대이므로 해석 시 주의가 필요하다. log-logistic 회귀모형은 위험함수가 단봉(unimodal)일 수 있어 비단조적 위험을 모형화하며, PH 모형이 아닌 순수 AFT 모형이다. 각 모수적 모형의 최대우도 추정, Cox-Snell 잔차를 이용한 적합도 평가, 표준화 잔차 분석을 설명한다. 모형 적합도는 Cox-Snell 잔차의 누적위험함수가 45도 직선에 가까운지로 평가하며, 표준화 잔차의 분포도 확인한다. SAS, Stata 등 소프트웨어에 따라 AFT 형태와 PH 형태의 계수 부호가 반대일 수 있어 출력 해석에 주의를 강조한다. WHAS500 데이터에 대한 지수, Weibull, log-logistic 모형의 적합과 비교를 예제로 시연한다.

---

### Ch 9: Other Models and Topics (pp. 286-354)

**핵심**: 반복 사건 모형(recurrent event models), 프레일티 모형(frailty models), 환자-대조군 연구(nested case-control), 가법 모형(additive models), 경쟁위험 모형(competing risk models), 표본 크기와 검정력, 결측 데이터 처리 등 다양한 고급 주제를 다룬다.

**키워드**: `recurrent events`, `frailty`, `nested case-control`, `additive model`, `competing risks`, `sample size`, `missing data`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 9 (line 21555)

반복 사건 모형, 프레일티 모형, 환자-대조군 연구, 가법 모형, 경쟁위험, 표본 크기, 결측 데이터 등 다양한 고급 주제를 다룬다. 반복 사건(recurrent events) 분석에서 Andersen-Gill(AG), 조건부 모형(WLW, PWP), 주변 모형 등 네 가지 접근법을 비교 설명한다. AG 모형은 모든 사건을 동일하게 취급하고 계수과정 형식으로 데이터를 구성하며, 클러스터 로버스트 분산으로 상관을 보정한다. 프레일티 모형(frailty models)은 미관측 이질성을 랜덤효과로 모형화하며, 감마 프레일티와 로그정규 프레일티를 설명한다. 내포된 환자-대조군(nested case-control) 설계는 대규모 코호트에서 비용 효율적으로 공변량 효과를 추정하는 방법이다. Aalen 가법 모형(additive hazards model)은 위험함수를 공변량의 선형 결합으로 모형화하며, 계수가 시간에 따라 변할 수 있다. 가법 모형의 누적 회귀함수 도표는 비례위험 모형의 PH 가정 위반 여부를 진단하는 데도 활용 가능하다. 경쟁위험(competing risks) 분석에서 원인별 위험 모형과 누적발생함수(CIF)를 소개하고, Fine-Gray 모형의 해석을 설명한다. 표본 크기 산출에서 log-rank 검정 기반 공식과 시뮬레이션 방법을 제시하며, 사건 수 대비 공변량 수의 지침을 논의한다. 결측 데이터 처리에서 완전사례 분석, 단일 대치, 다중 대치(multiple imputation) 방법을 비교하며, MICE 등의 실무적 접근을 설명한다.
