---
name: "Applied Survival Analysis: Regression Modeling of Time-to-Event Data (2nd Ed.)"
type: book-summary
source_file: "Hosmer-AppliedSurvivalAnalysis_full.md"
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

---

### Ch 2: Descriptive Methods for Survival Data (pp. 16-66)

**핵심**: 중도절단 데이터에서 누적분포함수와 생존함수를 추정하는 방법을 설명한다. Kaplan-Meier 추정량, 생존함수의 활용(중앙값, 사분위수 추정), 생존함수 비교를 위한 log-rank 등 검정법, 위험함수(hazard function) 및 관련 추정량을 다룬다.

**키워드**: `Kaplan-Meier`, `survival function`, `log-rank test`, `hazard function`, `kernel smoothing`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 2 (line 2613)

---

### Ch 3: Regression Models for Survival Data (pp. 67-91)

**핵심**: 위험함수에 회귀 구조를 도입하는 방법을 다루며, 준모수적(semiparametric) 비례위험모형의 수리적 기초를 설명한다. 편우도(partial likelihood)를 이용한 모형 적합, 동점(tied) 생존시간의 처리, 그리고 비례위험 회귀모형의 생존함수 추정 방법을 제시한다.

**키워드**: `semiparametric model`, `proportional hazards`, `partial likelihood`, `tied survival times`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 3 (line 5889)

---

### Ch 4: Interpretation of a Fitted Proportional Hazards Regression Model (pp. 92-131)

**핵심**: 적합된 PH 모형의 계수를 실질적으로 해석하는 방법을 설명한다. 명목형(nominal), 연속형(continuous) 공변량에 대한 해석, 다중 공변량 모형에서의 통계적 보정과 교호작용(interaction) 해석, 공변량 보정 생존함수의 해석과 활용을 다룬다.

**키워드**: `hazard ratio`, `nominal covariate`, `continuous covariate`, `interaction`, `adjusted survival function`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 4 (line 7153)

---

### Ch 5: Model Development (pp. 132-168)

**핵심**: PH 회귀분석에서 공변량 선택의 실무적 방법을 다룬다. 목적적 선택(purposeful selection), 연속형 공변량의 로그위험에서의 스케일 검토, 단계적 선택(stepwise), 최적부분집합(best-subsets), 다변량 분수다항식(multivariable fractional polynomial) 방법을 비교 설명한다. 수치적 문제도 논의한다.

**키워드**: `purposeful selection`, `stepwise`, `best subsets`, `fractional polynomials`, `model building`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 5 (line 10073)

---

### Ch 6: Assessment of Model Adequacy (pp. 169-206)

**핵심**: 적합된 모형의 타당성을 평가하는 방법을 다룬다. 잔차(residuals) 분석, PH 가정의 평가, 영향력 있는 관측치 및 적합이 나쁜 대상의 식별, 전반적 적합도(goodness-of-fit) 평가, 최종 모형의 해석 및 결과 제시 방법을 설명한다.

**키워드**: `residuals`, `proportional hazards assumption`, `influential observations`, `goodness-of-fit`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 6 (line 13247)

---

### Ch 7: Extensions of the Proportional Hazards Model (pp. 207-243)

**핵심**: 기본 PH 모형의 확장을 다룬다. 층화 PH 모형(stratified PH model), 시간의존 공변량(time-varying covariates), 절단(truncated) 데이터, 좌측 중도절단 및 구간 중도절단(interval censored) 데이터의 처리 방법을 설명한다.

**키워드**: `stratified model`, `time-varying covariates`, `truncation`, `left censoring`, `interval censoring`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 7 (line 16174)

---

### Ch 8: Parametric Regression Models (pp. 244-285)

**핵심**: 완전 모수적 모형의 장점(ML 추정, 예측값 산출, 잔차 계산)을 설명하며, 가속실패시간(AFT) 모형 계열을 다룬다. 지수(exponential), Weibull, log-logistic 회귀모형을 상세히 설명하고, 기타 모수적 모형에 대해서도 간략히 언급한다.

**키워드**: `AFT model`, `exponential`, `Weibull`, `log-logistic`, `maximum likelihood`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 8 (line 18802)

---

### Ch 9: Other Models and Topics (pp. 286-354)

**핵심**: 반복 사건 모형(recurrent event models), 프레일티 모형(frailty models), 환자-대조군 연구(nested case-control), 가법 모형(additive models), 경쟁위험 모형(competing risk models), 표본 크기와 검정력, 결측 데이터 처리 등 다양한 고급 주제를 다룬다.

**키워드**: `recurrent events`, `frailty`, `nested case-control`, `additive model`, `competing risks`, `sample size`, `missing data`

**상세**: → `Applied-Survival-Analysis-Regression-Modeling-of-Time-to-Event-Data-Second-Edition.md` Ch 9 (line 21555)
