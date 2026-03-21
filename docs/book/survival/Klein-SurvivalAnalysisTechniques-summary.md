---
name: "Survival Analysis: Techniques for Censored and Truncated Data (2nd Ed.)"
type: book-summary
source_file: "Klein-SurvivalAnalysisTechniques_full.md"
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

---

### Ch 2: Basic Quantities and Models (pp. 21-62)

**핵심**: 생존 데이터 모형화의 기본 모수를 정의한다. 생존함수, 위험함수(hazard function), 평균잔여수명(mean residual life), 확률밀도함수의 상호관계를 설명한다. 지수, Weibull, log-logistic 등 일반적 모수적 모형과 회귀모형, 경쟁위험 모형을 소개한다.

**키워드**: `survival function`, `hazard function`, `mean residual life`, `parametric models`, `competing risks`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 2 (line 2714)

---

### Ch 3: Censoring and Truncation (pp. 63-90)

**핵심**: 중도절단과 절단의 유형을 엄밀히 정의한다. 우측중도절단(Type I, II, progressive, random), 좌측/구간 중도절단, 좌절단(left truncation)과 우절단(right truncation)을 구분하고, 각 유형에 맞는 우도함수 구성법을 설명한다. 계수과정(counting process) 기초도 포함한다.

**키워드**: `right censoring`, `left censoring`, `interval censoring`, `truncation`, `likelihood`, `counting process`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 3 (line 5405)

---

### Ch 4: Nonparametric Estimation of Basic Quantities for Right-Censored and Left-Truncated Data (pp. 91-138)

**핵심**: 우측중도절단 데이터에서 생존함수와 누적위험함수의 비모수적 추정을 다룬다. Kaplan-Meier 추정량과 Nelson-Aalen 추정량을 유도하고, 생존함수의 점별 신뢰구간 및 신뢰대(confidence band), 평균/중앙 생존시간 추정, 좌절단 데이터와 경쟁위험에서의 요약 곡선을 설명한다.

**키워드**: `Kaplan-Meier`, `Nelson-Aalen`, `confidence band`, `left truncation`, `competing risks`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 4 (line 7022)

---

### Ch 5: Estimation of Basic Quantities for Other Sampling Schemes (pp. 139-164)

**핵심**: 우측중도절단 이외의 표본추출 방식에서의 생존함수 추정을 다룬다. 좌중도절단, 이중중도절단(double censoring), 구간중도절단, 우절단(right truncation) 데이터와 그룹화 데이터(cohort life table)에서의 추정 기법을 설명한다.

**키워드**: `left censoring`, `double censoring`, `interval censoring`, `right truncation`, `life table`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 5 (line 11219)

---

### Ch 6: Topics in Univariate Estimation (pp. 165-200)

**핵심**: 위험함수의 추정에 관한 심화 주제를 다룬다. 커널 평활(kernel smoothing)을 이용한 위험함수의 평활 추정, 초과 사망률(excess mortality) 추정(역사적 대조군과의 비교), 베이지안 비모수적 방법을 설명한다.

**키워드**: `kernel smoothing`, `hazard estimation`, `excess mortality`, `Bayesian nonparametric`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 6 (line 14615)

---

### Ch 7: Hypothesis Testing (pp. 201-242)

**핵심**: Nelson-Aalen 추정량의 관측값과 기대값의 가중 차이에 기반한 가설검정을 다룬다. 일표본 검정, 이표본 이상의 비교, 추세 검정, 층화 검정, Renyi 유형 검정, 고정 시점에서의 결과 차이 검정 등 다양한 검정법을 설명한다.

**키워드**: `log-rank test`, `Wilcoxon test`, `stratified test`, `trend test`, `Renyi test`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 7 (line 17984)

---

### Ch 8: Semiparametric Proportional Hazards Regression with Fixed Covariates (pp. 243-294)

**핵심**: 고정 공변량을 갖는 준모수적 비례위험 회귀모형(Cox 모형)을 상세히 다룬다. 공변량 코딩 방법, 구별 사건시간의 편우도(partial likelihood), 동점 처리, 국소 검정, 연속 공변량의 이산화, 모형 구축, 생존함수 추정을 설명한다.

**키워드**: `Cox model`, `partial likelihood`, `covariate coding`, `model building`, `survival function estimation`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 8 (line 20974)

---

### Ch 9: Refinements of the Semiparametric Proportional Hazards Model (pp. 295-328)

**핵심**: Cox 모형의 정교화를 다룬다. 시간의존 공변량(time-dependent covariates), 층화 비례위험 모형, 좌절단(left truncation) 처리, 시간 변동 효과의 종합(다상태 모형, multistate modeling)을 설명한다.

**키워드**: `time-dependent covariates`, `stratified model`, `left truncation`, `multistate model`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 9 (line 24445)

---

### Ch 10: Additive Hazards Regression Models (pp. 329-352)

**핵심**: 비례위험 모형의 대안으로 가법적 위험 모형(additive hazards model)을 다룬다. 위험함수를 공변량의 선형 결합으로 모형화하며, Aalen의 비모수적 가법 위험 모형과 Lin-Ying의 반모수적 가법 위험 모형을 설명한다.

**키워드**: `additive hazards`, `Aalen model`, `Lin-Ying model`, `nonparametric regression`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 10 (line 26983)

---

### Ch 11: Regression Diagnostics (pp. 353-392)

**핵심**: Cox 모형의 회귀진단을 다룬다. Cox-Snell 잔차를 이용한 모형 적합 평가, 마팅게일 잔차를 이용한 공변량의 함수 형태 결정, PH 가정의 그래프적 검토, 편차 잔차(deviance residuals), 개별 관측치의 영향력 평가를 설명한다.

**키워드**: `Cox-Snell residuals`, `martingale residuals`, `deviance residuals`, `influence diagnostics`, `PH assumption`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 11 (line 28245)

---

### Ch 12: Inference for Parametric Regression Models (pp. 393-424)

**핵심**: 모수적 모형을 이용한 생존 회귀분석을 다룬다. 가속실패시간(AFT) 모형의 로그 선형 표현을 기본으로 하여 Weibull, log-logistic 분포 및 기타 모수적 모형의 추정, 진단 방법을 설명한다. 모수적 모형이 적합할 때 비모수 방법보다 정밀한 추정이 가능함을 보인다.

**키워드**: `AFT model`, `Weibull regression`, `log-logistic regression`, `parametric diagnostics`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 12 (line 31548)

---

### Ch 13: Multivariate Survival Analysis (pp. 425-442)

**핵심**: 독립성 가정이 적절하지 않은 다변량 생존 데이터(형제, 부부, 동일 개인 내 반복 사건 등)의 분석을 다룬다. 프레일티(frailty) 모형을 통한 하위그룹 내 연관성 모형화, 감마 프레일티의 추정, 주변 모형(marginal model)을 설명한다.

**키워드**: `multivariate survival`, `frailty model`, `gamma frailty`, `marginal model`, `correlated survival`

**상세**: → `Survial Analysis – Techniques for Censored  and Truncated Data.md` Ch 13 (line 33839)
