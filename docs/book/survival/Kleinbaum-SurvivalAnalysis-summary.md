---
name: "Survival Analysis: A Self-Learning Text (3rd Ed.)"
type: book-summary
source_file: "Kleinbaum-SurvivalAnalysis_full.md"
authors: "David G. Kleinbaum, Mitchel Klein"
year: 2012
total_pages: 700
language: en
keywords: [survival analysis, Cox proportional hazards, Kaplan-Meier, log-rank test, time-dependent variables, stratified Cox, parametric models, recurrent events, competing risks, sample size]
---

# Survival Analysis: A Self-Learning Text (3rd Ed.) — Summary

> Kleinbaum & Klein (2012), ~700 pages, 10 chapters + Computer Appendix
> 생존분석의 핵심 개념을 자기학습 형식(lecture-book format)으로 체계적으로 설명하는 입문-중급 교재이다.

## Contents

- Chapter 1: Introduction to Survival Analysis (pp. 1-54)
- Chapter 2: Kaplan-Meier Survival Curves and the Log-Rank Test (pp. 55-96)
- Chapter 3: The Cox Proportional Hazards Model and Its Characteristics (pp. 97-160)
- Chapter 4: Evaluating the Proportional Hazards Assumption (pp. 161-200)
- Chapter 5: The Stratified Cox Procedure (pp. 201-240)
- Chapter 6: Extension of the Cox Proportional Hazards Model for Time-Dependent Variables (pp. 241-288)
- Chapter 7: Parametric Survival Models (pp. 289-362)
- Chapter 8: Recurrent Event Survival Analysis (pp. 363-424)
- Chapter 9: Competing Risks Survival Analysis (pp. 425-496)
- Chapter 10: Design Issues for Randomized Trials (pp. 497-524)
- Computer Appendix: Survival Analysis on the Computer (pp. 525-689)

---

## Chapter Summaries

### Ch 1: Introduction to Survival Analysis (pp. 1-54)

**핵심**: 생존분석이 다루는 문제(시간-사건 데이터)와 주요 목표를 소개한다. 생존함수, 위험함수(hazard function) 등 핵심 개념과 표기법을 정의하고, 중도절단(censoring)의 유형(random, independent, noninformative)을 구분한다. Counting Process 데이터 레이아웃도 소개하여 이후 장에서 활용할 기반을 마련한다.

**키워드**: `survival function`, `hazard function`, `censoring`, `counting process`, `time-to-event`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 1 (line 673)

---

### Ch 2: Kaplan-Meier Survival Curves and the Log-Rank Test (pp. 55-96)

**핵심**: Kaplan-Meier(KM) 생존곡선의 작성 및 해석 방법을 설명한다. 두 개 이상의 KM 곡선이 동일한지 검정하는 log-rank 검정과 대안적 검정법을 다루며, KM 곡선과 중앙 생존시간에 대한 95% 신뢰구간 산출 방법을 제시한다.

**키워드**: `Kaplan-Meier`, `log-rank test`, `confidence interval`, `median survival`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 2 (line 8350)

---

### Ch 3: The Cox Proportional Hazards Model and Its Characteristics (pp. 97-160)

**핵심**: Cox PH 모형의 수식적 형태와 그 인기의 이유를 설명한다. 최대우도(ML) 추정, 위험비(hazard ratio) 공식, 보정 생존곡선(adjusted survival curves) 도출 방법, 그리고 비례위험(PH) 가정의 의미를 다룬다. 연령을 시간 척도로 사용하는 방법도 추가되었다.

**키워드**: `Cox model`, `proportional hazards`, `partial likelihood`, `hazard ratio`, `baseline hazard`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 3 (line 14914)

---

### Ch 4: Evaluating the Proportional Hazards Assumption (pp. 161-200)

**핵심**: PH 가정을 평가하는 세 가지 접근법을 설명한다. 그래프적 방법(log-log 생존곡선, 관측 vs. 기대 플롯), 적합도 검정(GOF testing), 그리고 시간의존 변수를 이용한 검정이다.

**키워드**: `PH assumption`, `log-log plot`, `goodness-of-fit`, `time-dependent covariate`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 4 (line 21778)

---

### Ch 5: The Stratified Cox Procedure (pp. 201-240)

**핵심**: PH 가정을 만족하지 않는 예측변수를 층화변수로 처리하는 Stratified Cox 모형을 설명한다. 층화의 수행 방법, 컴퓨터 결과 해석, 위험비 산출, 단일 예측변수 vs. 다중 예측변수 상황에서의 적용을 다룬다.

**키워드**: `stratified Cox`, `stratification`, `non-proportional hazards`, `hazard ratio`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 5 (line 25565)

---

### Ch 6: Extension of the Cox PH Model for Time-Dependent Variables (pp. 241-288)

**핵심**: Cox PH 모형을 시간의존 변수(time-dependent variables)로 확장하는 방법을 설명한다. 모형의 형태와 특성, 위험비 해석, PH 가정 확인 방법, 그리고 컴퓨터 적용 예제를 포함한다.

**키워드**: `time-dependent covariates`, `extended Cox model`, `counting process`, `hazard ratio`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 6 (line 29984)

---

### Ch 7: Parametric Survival Models (pp. 289-362)

**핵심**: 모수적 모형(parametric models)을 개관하며, 지수(exponential), Weibull, log-logistic 모형을 예제와 함께 설명한다. 가속실패시간(AFT) 모형과 PH 모형의 관계를 비교하고, 구간중도절단(interval-censoring), 프레일티(frailty) 모형도 간략히 소개한다.

**키워드**: `exponential`, `Weibull`, `log-logistic`, `AFT model`, `parametric likelihood`, `frailty`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 7 (line 35166)

---

### Ch 8: Recurrent Event Survival Analysis (pp. 363-424)

**핵심**: 동일 대상에서 반복 발생하는 사건(recurrent events)의 분석 방법을 다룬다. Counting Process(CP) 접근법을 중심으로 Cox PH 모형 활용, Stratified Cox PH 모형, 프레일티 모형 등 대안적 접근법을 설명한다.

**키워드**: `recurrent events`, `counting process`, `stratified Cox`, `frailty model`, `gap time`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 8 (line 41822)

---

### Ch 9: Competing Risks Survival Analysis (pp. 425-496)

**핵심**: 서로 다른 유형의 사건이 경쟁적으로 발생할 수 있는 경쟁위험(competing risks) 상황을 다룬다. Cox PH 모형을 이용한 분석과 그 한계점, 그리고 이를 보완하는 접근법들을 설명한다.

**키워드**: `competing risks`, `cause-specific hazard`, `cumulative incidence`, `Cox model`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 9 (line 51449)

---

### Ch 10: Design Issues for Randomized Trials (pp. 497-524)

**핵심**: 3판에서 새로 추가된 장으로, 시간-사건 데이터를 포함하는 무작위 임상시험의 설계 문제를 다룬다. 표본 크기(sample size) 산정, 모집 기간(accrual period), 추적관찰 기간, 치료 전환(therapy switching) 시 대처 방법 등 통계적 의사결정 사항을 설명한다.

**키워드**: `sample size`, `power`, `accrual period`, `randomized trial`, `study design`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 10 (line 59803)
