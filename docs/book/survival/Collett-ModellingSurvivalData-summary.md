---
name: "Modelling Survival Data in Medical Research (4th Ed.)"
type: book-summary
source_file: "Collett-ModellingSurvivalData_full.md"
authors: "David Collett"
year: 2023
total_pages: 480
language: en
keywords: [survival analysis, Cox regression, parametric models, flexible parametric models, frailty, competing risks, Bayesian survival analysis, interval censoring, non-proportional hazards, R]
---

# Modelling Survival Data in Medical Research (4th Ed.) — Summary

> Collett (2023), ~480 pages, 17 chapters
> 의학 연구에서의 생존 데이터 모형화를 포괄적으로 다루는 중급 수준의 실용 교재이며, 4판에서는 베이지안 생존분석 장이 신설되었다.

## Contents

- Chapter 1: Survival analysis (pp. 1-14)
- Chapter 2: Some non-parametric procedures (pp. 15-48)
- Chapter 3: The Cox regression model (pp. 49-114)
- Chapter 4: Model checking in the Cox regression model (pp. 115-146)
- Chapter 5: Parametric regression models (pp. 147-216)
- Chapter 6: Flexible parametric models (pp. 217-234)
- Chapter 7: Model checking in parametric models (pp. 235-250)
- Chapter 8: Time-dependent variables (pp. 251-284)
- Chapter 9: Interval-censored survival data (pp. 285-300)
- Chapter 10: Frailty models (pp. 301-330)
- Chapter 11: Non-proportional hazards and institutional comparisons (pp. 331-352)
- Chapter 12: Competing risks (pp. 353-372)
- Chapter 13: Multiple events and event history modelling (pp. 373-394)
- Chapter 14: Dependent censoring (pp. 395-406)
- Chapter 15: Sample size requirements for a survival study (pp. 407-418)
- Chapter 16: Bayesian survival analysis (pp. 419-446)
- Chapter 17: Survival analysis with R (pp. 447+)

---

## Chapter Summaries

### Ch 1: Survival analysis (pp. 1-14)

**핵심**: 생존분석의 기본 개념을 소개한다. 시간 원점(time origin)에서 사건(end point) 발생까지의 시간 데이터에 관한 것으로, 중도절단(censoring)과 독립 중도절단 가정을 설명한다. 생존함수(survivor function), 위험함수(hazard function), 누적위험함수(cumulative hazard function)를 정의하고, 다양한 의학 연구 예제를 제시한다.

**키워드**: `time origin`, `end point`, `censoring`, `survivor function`, `hazard function`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 1 (line 313)

---

### Ch 2: Some non-parametric procedures (pp. 15-48)

**핵심**: 생존 데이터의 비모수적 요약 방법을 다룬다. 생명표(life-table) 추정, Kaplan-Meier 추정, Nelson-Aalen 추정으로 생존함수를 추정하며, 중앙 생존시간과 사분위수를 구한다. 두 표본 이상의 생존곡선 비교를 위한 log-rank 검정 등의 방법을 설명한다.

**키워드**: `life-table`, `Kaplan-Meier`, `Nelson-Aalen`, `log-rank test`, `median survival`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 2 (line 1361)

---

### Ch 3: The Cox regression model (pp. 49-114)

**핵심**: Cox 비례위험 회귀모형의 형태, 편우도(partial likelihood) 추정, 위험비(hazard ratio) 해석을 설명한다. 인구통계학적 변수, 생리학적 변수 등 설명변수를 포함한 모형 적합과 해석을 다양한 예제를 통해 설명한다.

**키워드**: `Cox regression`, `partial likelihood`, `hazard ratio`, `explanatory variables`, `baseline hazard`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 3 (line 3966)

---

### Ch 4: Model checking in the Cox regression model (pp. 115-146)

**핵심**: Cox 회귀모형의 적합 후 모형 적절성을 평가하는 진단 절차를 설명한다. 잔차 분석(martingale, deviance, Schoenfeld residuals)을 통한 모형 가정 위반 탐지, 영향력 관측치 식별, PH 가정 검토 방법을 다룬다. 중도절단이 있는 상황에서의 시각적 검토 한계도 논의한다.

**키워드**: `residuals`, `martingale`, `deviance`, `Schoenfeld`, `model diagnostics`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 4 (line 9189)

---

### Ch 5: Parametric regression models (pp. 147-216)

**핵심**: 생존시간에 특정 확률분포를 가정하는 모수적 모형을 다룬다. Weibull, log-logistic, lognormal 분포를 중심으로 모수적 모형이 Cox 모형보다 정밀한 추정을 제공할 수 있는 경우를 설명한다. 가속실패시간(AFT) 모형과 비례위험(PH) 모형의 관계를 비교한다.

**키워드**: `Weibull`, `log-logistic`, `lognormal`, `AFT model`, `parametric estimation`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 5 (line 11575)

---

### Ch 6: Flexible parametric models (pp. 217-234)

**핵심**: 모수적 모형의 제한된 유연성과 Cox 모형의 비연속적 기저 위험함수의 한계를 극복하는 유연한 모수적 모형(spline 기반)을 소개한다. 기저 위험함수와 누적위험함수를 스플라인으로 모형화하여 연속적이고 매끄러운 추정을 가능하게 한다.

**키워드**: `flexible parametric model`, `splines`, `baseline hazard`, `cumulative hazard`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 6 (line 16912)

---

### Ch 7: Model checking in parametric models (pp. 235-250)

**핵심**: 모수적 모형에서의 모형 적합성 진단을 다룬다. Cox 모형에서 개발된 잔차 기반 방법을 모수적 모형에 적용하고, Weibull, log-logistic, lognormal 분포의 적합성을 그래프적으로 평가하는 방법을 설명한다. 영향력 관측치 탐지와 PH 가정 검토도 포함한다.

**키워드**: `residuals`, `parametric diagnostics`, `graphical assessment`, `influential observations`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 7 (line 18263)

---

### Ch 8: Time-dependent variables (pp. 251-284)

**핵심**: 연구 기간 중 값이 변하는 시간의존 설명변수(time-dependent variables)를 모형에 포함하는 방법을 설명한다. 기저 시점에서 기록된 고정 변수와 달리, 추적 기간 동안 모니터링되는 변수의 처리 방법을 다룬다.

**키워드**: `time-dependent variables`, `internal covariates`, `external covariates`, `Cox model extension`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 8 (line 19363)

---

### Ch 9: Interval-censored survival data (pp. 285-300)

**핵심**: 사건 발생 시점이 정확히 관측되지 않고 특정 구간 내에서 발생한 것으로만 알려진 구간중도절단(interval-censored) 데이터의 요약 및 모형화 방법을 설명한다. 4판에서 현대적 방법으로 대폭 개정되었다.

**키워드**: `interval censoring`, `grouped data`, `non-lethal end point`, `NPMLE`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 9 (line 21843)

---

### Ch 10: Frailty models (pp. 301-330)

**핵심**: 관측되지 않은 이질성(unobserved heterogeneity)을 설명하는 프레일티(frailty) 효과를 다룬다. 동일 그룹 내 개인들의 생존시간이 독립이 아닌 경우, 공유 프레일티(shared frailty) 모형을 통해 그룹 내 상관성을 모형화하는 방법을 설명한다.

**키워드**: `frailty`, `shared frailty`, `unobserved heterogeneity`, `random effects`, `gamma frailty`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 10 (line 23066)

---

### Ch 11: Non-proportional hazards and institutional comparisons (pp. 331-352)

**핵심**: 비례위험 가정이 적절하지 않은 상황에서의 모형화 방법을 다룬다. 설명변수의 효과가 시간에 따라 변하는 경우의 대응 방법과, 의료기관 간 생존률 비교에서의 비비례위험 모형 적용을 설명한다.

**키워드**: `non-proportional hazards`, `institutional comparison`, `time-varying effects`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 11 (line 25268)

---

### Ch 12: Competing risks (pp. 353-372)

**핵심**: 환자가 여러 원인 중 하나로 사망할 수 있는 경쟁위험(competing risks) 상황의 데이터 요약 및 모형화 방법을 설명한다. 원인별 위험함수(cause-specific hazard)와 누적발생함수(cumulative incidence function) 접근법을 다룬다.

**키워드**: `competing risks`, `cause-specific hazard`, `cumulative incidence`, `Fine-Gray model`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 12 (line 26932)

---

### Ch 13: Multiple events and event history modelling (pp. 373-394)

**핵심**: 동일 개인에서 반복 발생하는 사건(recurrent events)이나 여러 유형의 사건이 발생하는 다중 사건 데이터를 다룬다. 사건 이력 모형(event history modelling)과 다상태 모형(multistate models)을 설명한다.

**키워드**: `recurrent events`, `multiple events`, `event history`, `multistate model`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 13 (line 28460)

---

### Ch 14: Dependent censoring (pp. 395-406)

**핵심**: 독립 중도절단 가정이 위반되는 종속 중도절단(dependent censoring) 문제를 다룬다. 부작용으로 인한 이탈, 구제 약물(rescue medication) 투여 등으로 중도절단이 생존시간과 관련되는 경우의 분석 방법을 설명한다.

**키워드**: `dependent censoring`, `informative censoring`, `inverse probability weighting`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 14 (line 30055)

---

### Ch 15: Sample size requirements for a survival study (pp. 407-418)

**핵심**: 생존 연구 설계 시 표본 크기를 결정하는 방법을 다룬다. 포함/제외 기준, 추적관찰 기간, 순차적 설계(sequential design), 중간 분석(interim analysis), 적응적 설계(adaptive design) 등 다양한 설계 요소를 고려한 표본 크기 산출을 설명한다.

**키워드**: `sample size`, `power`, `sequential design`, `interim analysis`, `adaptive design`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 15 (line 30862)

---

### Ch 16: Bayesian survival analysis (pp. 419-446)

**핵심**: 4판에서 새로 추가된 장으로, 미지의 모형 모수를 확률변수로 간주하는 베이지안 추론 방법을 생존분석에 적용한다. 사전분포(prior), 사후분포(posterior), 우도함수의 결합을 통한 모수 추정과 구간 추정을 설명한다.

**키워드**: `Bayesian inference`, `prior distribution`, `posterior distribution`, `MCMC`, `credible interval`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 16 (line 31826)

---

### Ch 17: Survival analysis with R (pp. 447+)

**핵심**: R 소프트웨어를 사용하여 본서에서 다룬 생존분석 기법을 구현하는 방법을 설명한다. R 패키지의 풍부함, 새로운 통계 방법의 빠른 구현, 무료 이용 가능성 등 R의 장점과 함께 실습 코드를 제공한다.

**키워드**: `R`, `survival package`, `software`, `implementation`, `code examples`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 17 (line 34006)
