---
name: "Modelling Survival Data in Medical Research (4th Ed.)"
type: book-summary
sources:
  - file: "Collett-ModellingSurvivalData_azure_full.md"
    tool: Document Intelligence
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

생존분석은 잘 정의된 시간 원점(time origin)에서 특정 사건(end point)이 발생하기까지의 시간 데이터를 분석하는 방법이다. 의학 연구에서 시간 원점은 보통 임상시험 등록 시점이며, 사건은 사망이나 증상 재발 등이 될 수 있다. 생존 데이터의 특수한 점은 양의 방향으로 치우친(positively skewed) 분포를 보이며, 정규분포 가정이 적절하지 않다는 것이다. 가장 핵심적인 특징은 중도절단(censoring)인데, 이는 관심 사건이 관찰 기간 내에 발생하지 않거나 추적이 불가능해진 경우에 발생한다. 우측 중도절단(right censoring)이 가장 흔하며, 좌측 중도절단과 구간 중도절단도 존재한다. 독립 중도절단(independent censoring) 가정은 실제 생존시간이 중도절단 메커니즘에 의존하지 않음을 의미하며, 대부분의 생존분석 방법의 타당성 전제 조건이다. 생존함수 S(t)는 시간 t 이후에도 생존할 확률, 위험함수 h(t)는 시간 t까지 생존한 조건하에서 순간 사망률, 누적위험함수 H(t)는 위험함수의 적분으로 정의된다. 이 세 함수는 상호 유도 가능하며 S(t) = exp{−H(t)} 관계를 갖는다. 본서는 범죄학, 공학, 금융, 마케팅, 정치학, 심리학 등 다양한 분야에서의 생존분석 응용 사례를 제시하며, 의학 연구에 초점을 맞춘다. 연구 시간(study time)과 환자 시간(patient time)의 구분을 통해 실제 연구에서 관측되는 데이터 구조를 설명한다. 다양한 예제 데이터셋(IUD 사용 중단, 유방암 예후, 다발골수종 생존 등)을 소개하여 이후 장에서의 분석 기반을 마련한다.

---

### Ch 2: Some non-parametric procedures (pp. 15-48)

**핵심**: 생존 데이터의 비모수적 요약 방법을 다룬다. 생명표(life-table) 추정, Kaplan-Meier 추정, Nelson-Aalen 추정으로 생존함수를 추정하며, 중앙 생존시간과 사분위수를 구한다. 두 표본 이상의 생존곡선 비교를 위한 log-rank 검정 등의 방법을 설명한다.

**키워드**: `life-table`, `Kaplan-Meier`, `Nelson-Aalen`, `log-rank test`, `median survival`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 2 (line 1361)

생존 데이터의 초기 분석 단계로서 비모수적 방법을 통해 생존함수와 위험함수를 추정하는 절차를 다룬다. 생명표(life-table) 추정은 관찰 기간을 일정 구간으로 나누고 보험수리적 가정(actuarial assumption)을 적용하여 생존확률을 산출하며, 구간중도절단 데이터에 특히 적합하다. Kaplan-Meier(KM) 추정은 각 사망 시점에서 조건부 생존확률의 곱으로 생존함수를 추정하며, 생명표 추정의 구간 수가 무한대로 갈 때의 극한값이므로 곱극한(product-limit) 추정이라고도 한다. 중도절단이 없을 경우 KM 추정은 경험적 생존함수(empirical survivor function)와 동일하다. Nelson-Aalen 추정은 누적위험함수를 직접 추정하며, KM 추정의 대안으로 사용된다. 생존함수의 표준오차는 Greenwood 공식을 통해 구하고, 이를 바탕으로 신뢰구간을 산출한다. 중앙 생존시간과 사분위수는 추정된 생존함수로부터 구할 수 있으며, 이에 대한 신뢰구간도 제공된다. 두 그룹 이상의 생존곡선 비교를 위해 log-rank 검정, Wilcoxon 검정, Peto-Peto 검정 등 비모수 검정법을 소개한다. log-rank 검정은 전 추적 기간에 걸쳐 동일한 가중치를 부여하고, Wilcoxon 검정은 초기 시점에 더 큰 가중치를 부여하는 차이가 있다. 세 그룹 이상의 비교, 층화 검정(stratified test), 추세 검정(trend test)으로의 확장도 설명한다. 다양한 의학 연구 예제(IUD, 유방암, 다발골수종 등)를 통해 각 방법의 적용을 구체적으로 보여준다.

---

### Ch 3: The Cox regression model (pp. 49-114)

**핵심**: Cox 비례위험 회귀모형의 형태, 편우도(partial likelihood) 추정, 위험비(hazard ratio) 해석을 설명한다. 인구통계학적 변수, 생리학적 변수 등 설명변수를 포함한 모형 적합과 해석을 다양한 예제를 통해 설명한다.

**키워드**: `Cox regression`, `partial likelihood`, `hazard ratio`, `explanatory variables`, `baseline hazard`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 3 (line 3966)

Cox 회귀모형은 설명변수가 위험함수에 미치는 영향을 탐색하기 위한 준모수적(semi-parametric) 비례위험 모형이다. 모형의 핵심 형태는 h_i(t) = exp(β'x_i)h_0(t)이며, 기저 위험함수 h_0(t)에 대해 어떤 분포도 가정하지 않는다. 편우도(partial likelihood)를 통해 β 계수를 추정하며, 이 방법은 기저 위험함수를 추정하지 않고도 회귀계수의 추론이 가능하다는 장점이 있다. 설명변수의 선형 성분(linear component)에는 변량(variate), 요인(factor), 교호작용(interaction) 항을 포함할 수 있으며, 요인은 더미 변수로 코딩한다. 모형 비교는 편우도비 검정(partial likelihood ratio test), Wald 검정, 스코어 검정을 사용하며, AIC 통계량을 통한 비중첩 모형 비교도 가능하다. 모형 선택 전략으로 전진/후진/단계적 선택법과 LASSO 변수 선택을 설명한다. β 계수의 해석에서 exp(β)는 위험비(hazard ratio)로, 해당 변수가 1단위 증가할 때 위험의 배수적 변화를 나타낸다. 연속형 변수의 비선형 효과를 포착하기 위한 분수다항식(fractional polynomials) 방법도 다룬다. 기저 위험함수와 생존함수의 추정은 Breslow 방법을 사용하며, 위험 보정 생존함수(risk-adjusted survivor function)도 산출할 수 있다. 일치도(concordance), 예측 능력, 설명 변이량 측도, 시간의존 ROC 곡선 등 모형의 예측 성능 평가 방법을 제시한다. 비례위험 모형과 log-rank 검정의 관계도 설명하며, 두 그룹 비교 시 log-rank 검정이 Cox 모형의 스코어 검정과 동등함을 보인다.

---

### Ch 4: Model checking in the Cox regression model (pp. 115-146)

**핵심**: Cox 회귀모형의 적합 후 모형 적절성을 평가하는 진단 절차를 설명한다. 잔차 분석(martingale, deviance, Schoenfeld residuals)을 통한 모형 가정 위반 탐지, 영향력 관측치 식별, PH 가정 검토 방법을 다룬다. 중도절단이 있는 상황에서의 시각적 검토 한계도 논의한다.

**키워드**: `residuals`, `martingale`, `deviance`, `Schoenfeld`, `model diagnostics`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 4 (line 9189)

Cox 회귀모형 적합 후 모형의 적절성을 평가하는 진단 절차를 체계적으로 설명한다. Cox-Snell 잔차는 적합 모형이 올바를 때 단위 지수분포를 따르며, 모형 전반적 적합성 평가에 사용된다. 수정된 Cox-Snell 잔차는 중도절단 관측치에 대해 지수분포의 무기억성(lack of memory property)을 이용하여 보정한 것이다. 마팅게일 잔차(martingale residuals)는 관측된 사망 수와 모형 기반 기대 사망 수의 차이로 정의되며, 합이 0이지만 비대칭 분포를 갖는다. 편차 잔차(deviance residuals)는 마팅게일 잔차를 대칭적으로 변환한 것으로, 해석이 더 용이하다. Schoenfeld 잔차는 각 사망 시점에서 공변량 값과 위험집합 가중 평균의 차이로 정의되며, 비례위험 가정 검토에 핵심적이다. 스코어 잔차(score residuals)와 dfbeta 잔차를 이용하여 개별 관측치가 모형 계수에 미치는 영향력을 평가한다. 비례위험(PH) 가정의 검토 방법으로 로그-로그 생존곡선 그래프, Schoenfeld 잔차의 시간에 대한 회귀, 시간의존 변수를 이용한 검정을 제시한다. 공변량의 함수 형태를 확인하기 위해 마팅게일 잔차를 공변량에 대해 산점도로 그리는 방법을 설명한다. 영향력 관측치(influential observations)의 식별은 각 관측치를 제외했을 때의 계수 변화를 측정하는 방식으로 수행한다. 모형 진단의 권장 절차로서 잔차 분석, PH 가정 검토, 영향력 분석을 종합적으로 수행할 것을 권고한다.

---

### Ch 5: Parametric regression models (pp. 147-216)

**핵심**: 생존시간에 특정 확률분포를 가정하는 모수적 모형을 다룬다. Weibull, log-logistic, lognormal 분포를 중심으로 모수적 모형이 Cox 모형보다 정밀한 추정을 제공할 수 있는 경우를 설명한다. 가속실패시간(AFT) 모형과 비례위험(PH) 모형의 관계를 비교한다.

**키워드**: `Weibull`, `log-logistic`, `lognormal`, `AFT model`, `parametric estimation`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 5 (line 11575)

생존시간에 특정 확률분포를 가정하는 모수적 모형을 다루며, 분포 가정이 타당할 경우 Cox 모형보다 정밀한 추정을 제공한다. 지수분포는 위험함수가 상수(h(t) = λ)인 가장 단순한 모형으로, 실무에서는 거의 비현실적이지만 기본 구성요소로 중요하다. Weibull 분포는 형상 모수(γ)에 따라 위험함수가 단조 증가(γ > 1) 또는 단조 감소(γ < 1)하며, 모수적 생존분석의 핵심 분포이다. log-logistic 분포는 위험함수가 단봉(unimodal)일 수 있어 Weibull의 단조적 한계를 극복하며, 가속실패시간 모형에서 사용된다. 로그정규(lognormal) 분포는 로그 생존시간이 정규분포를 따른다고 가정하며, 역시 단봉 위험함수를 산출할 수 있다. 분포의 적합성은 그래프적 방법(로그-로그 도표 등)으로 사전 평가할 수 있다. 비례위험(PH) 모형과 가속실패시간(AFT) 모형의 두 가지 모형화 접근법을 비교하며, Weibull 분포만이 두 모형 모두에 해당한다. AFT 모형에서는 공변량 효과가 시간 스케일에 승법적으로 작용하여 생존시간을 "가속" 또는 "감속"시킨다. Gompertz 분포, 비례오즈(proportional odds) 모형, 치유율(cure rate) 모형 등 추가적인 모수적 모형도 소개한다. 모수적 모형의 설명 변이량(explained variation), 공변량 보정 효과(effect of covariate adjustment), 최대우도 추정 방법을 상세히 설명한다. 다양한 예제를 통해 Weibull, log-logistic, lognormal 모형의 적합과 해석, 모형 간 비교 방법을 시연한다.

---

### Ch 6: Flexible parametric models (pp. 217-234)

**핵심**: 모수적 모형의 제한된 유연성과 Cox 모형의 비연속적 기저 위험함수의 한계를 극복하는 유연한 모수적 모형(spline 기반)을 소개한다. 기저 위험함수와 누적위험함수를 스플라인으로 모형화하여 연속적이고 매끄러운 추정을 가능하게 한다.

**키워드**: `flexible parametric model`, `splines`, `baseline hazard`, `cumulative hazard`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 6 (line 16912)

표준 모수적 모형의 제한된 유연성과 Cox 모형의 불연속적 기저 위험함수의 한계를 극복하는 유연한 모수적 모형을 소개한다. 구간별 지수 모형(piecewise exponential model)은 사건 시점 사이에서 기저 위험을 상수로 가정하며, 절점(knot)의 수와 위치 선택이 중요하다. 스플라인(spline) 함수는 시간 축을 여러 구간으로 나누고 각 구간에 다항식을 적합하되 경계에서 매끄럽게 연결하는 방법이다. B-스플라인은 m+k+1개의 기저함수로 구성되며, 재귀 관계식(recurrence relationship)을 통해 기저함수를 산출한다. 제한 3차 스플라인(restricted cubic spline)은 경계 절점 바깥에서 선형으로 제한하여 극단값에서의 불안정성을 방지한다. Royston-Parmar 모형은 로그 누적위험함수에 제한 3차 스플라인을 적용하여 비례위험, 비례오즈, AFT 구조를 유연하게 모형화한다. 절점의 수와 위치 결정은 AIC나 BIC 기준을 사용하며, 보통 5개 이하의 내부 절점으로 충분하다. 구간별 지수 모형은 완전 우도(full likelihood) 기반으로 추정하므로 Cox 모형의 편우도 기반 AIC와 직접 비교할 수 없다. 유연한 모수적 모형은 연속적이고 매끄러운 위험함수와 생존함수의 추정을 가능하게 하여 임상적 해석을 용이하게 한다. 하이퍼네프로마 치료 데이터 등 실제 예제를 통해 구간별 지수 모형, 스플라인 기반 모형의 적합 및 비교를 시연한다. 유연 비례오즈 모형(flexible proportional odds model)으로의 확장도 다룬다.

---

### Ch 7: Model checking in parametric models (pp. 235-250)

**핵심**: 모수적 모형에서의 모형 적합성 진단을 다룬다. Cox 모형에서 개발된 잔차 기반 방법을 모수적 모형에 적용하고, Weibull, log-logistic, lognormal 분포의 적합성을 그래프적으로 평가하는 방법을 설명한다. 영향력 관측치 탐지와 PH 가정 검토도 포함한다.

**키워드**: `residuals`, `parametric diagnostics`, `graphical assessment`, `influential observations`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 7 (line 18263)

모수적 모형에서의 모형 적합성 진단을 다루며, Cox 모형에서 개발된 잔차 기반 방법을 모수적 모형에 적용한다. 표준화 잔차(standardised residuals)는 AFT 모형에서 '관측값 − 적합값' 형태로 정의되며, 올바른 모형일 때 오차항의 분포를 따른다. Cox-Snell 잔차는 모수적 모형에서도 추정된 누적위험함수 값으로 정의되며, 적합 모형이 올바를 때 단위 지수분포를 따른다. 마팅게일 잔차와 편차 잔차는 Cox 모형에서의 정의와 유사하게 모수적 모형에 적용되며, 적합이 나쁜 관측치를 식별하는 데 사용된다. 스코어 잔차는 로그우도 함수의 모수에 대한 편미분의 개별 성분으로 정의되며, 합이 0이 된다. Weibull 모형에서 표준화 잔차는 Gumbel 분포를 따르며, Cox-Snell 잔차는 이의 지수변환으로 얻어진다. log-logistic 모형과 로그정규 모형에서의 잔차 형태와 잔여 생존함수 표현도 구체적으로 제시한다. 모수적 분포의 적합성을 그래프적으로 평가하기 위해 관측 생존함수와 적합 생존함수를 비교하는 방법을 설명한다. 영향력 관측치의 탐지는 스코어 잔차 기반의 dfbeta 유사 통계량을 사용하여 수행한다. Weibull 모형에서 비례위험 가정의 검정은 스코어 잔차의 시간에 대한 회귀를 통해 실시한다. 다양한 예제를 통해 각 모수적 모형별 잔차 분석과 진단 절차를 시연한다.

---

### Ch 8: Time-dependent variables (pp. 251-284)

**핵심**: 연구 기간 중 값이 변하는 시간의존 설명변수(time-dependent variables)를 모형에 포함하는 방법을 설명한다. 기저 시점에서 기록된 고정 변수와 달리, 추적 기간 동안 모니터링되는 변수의 처리 방법을 다룬다.

**키워드**: `time-dependent variables`, `internal covariates`, `external covariates`, `Cox model extension`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 8 (line 19363)

연구 기간 중 값이 변하는 시간의존 설명변수(time-dependent variables)를 Cox 모형에 포함하는 방법을 설명한다. 내부 변수(internal variables)는 특정 개인에 관련되어 생존 중에만 측정 가능한 것(예: 혈압, 백혈구 수)이며, 외부 변수(external variables)는 개인의 생존과 독립적으로 존재하는 것(예: 대기오염 수준)이다. 시간의존 계수(time-varying coefficients)는 고정 공변량의 효과가 시간에 따라 변하는 경우로, 이때 모형은 비비례위험 모형이 된다. 확장된 Cox 모형에서 편우도 함수는 각 사망 시점에서 위험집합 내 모든 개인의 시간의존 변수 값을 필요로 한다. 시간의존 변수의 값은 항상 마지막으로 관측된 값을 사용해야 하며, 미래 값을 사용하거나 보간하면 편향이 발생한다. 데이터 코딩은 계수과정(counting process) 형식으로 각 관측 구간을 (시작, 끝] 형태로 분할하여 구성한다. PH 가정 검정에서의 시간-공변량 교호작용, 이식 후 이식편대숙주질환(GVHD) 발생 같은 상태 변화 변수의 처리 등 구체적 응용을 다룬다. 종단 데이터와 생존 데이터를 동시에 모형화하는 결합 모형(joint modelling)도 소개한다. 결합 모형은 종단 하위모형(longitudinal submodel)과 생존 하위모형(survival submodel)을 공유 랜덤효과나 현재값 연결을 통해 결합한다. 결합 모형의 확장으로서 다중 종단 결과, 경쟁위험, 비선형 궤적 등의 가능성을 논의한다. 전립선암 임상시험, 심장이식 연구 등 다양한 예제를 통해 시간의존 변수의 모형화를 시연한다.

---

### Ch 9: Interval-censored survival data (pp. 285-300)

**핵심**: 사건 발생 시점이 정확히 관측되지 않고 특정 구간 내에서 발생한 것으로만 알려진 구간중도절단(interval-censored) 데이터의 요약 및 모형화 방법을 설명한다. 4판에서 현대적 방법으로 대폭 개정되었다.

**키워드**: `interval censoring`, `grouped data`, `non-lethal end point`, `NPMLE`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 9 (line 21843)

사건 발생 시점이 정확히 관측되지 않고 특정 구간 내에서 발생한 것으로만 알려진 구간중도절단(interval-censored) 데이터의 분석 방법을 설명한다. 구간중도절단은 우측·좌측 중도절단의 일반화로, (L, U] 형태의 구간으로 표현되며 우측중도절단은 U = ∞, 좌측중도절단은 L = 0인 특수 경우이다. 현재 상태 데이터(current status data)는 한 시점에서의 관찰만 있어 모든 관측치가 좌측 또는 우측 중도절단인 경우이다. Turnbull 구간은 구간중도절단 데이터에서 생존함수가 정의되는 구간으로, 하한(L)과 상한(U) 경계값의 순서 배열을 통해 결정된다. 생존함수의 비모수적 최대우도 추정(NPMLE)은 EM 알고리즘을 통해 Turnbull 구간에서의 생존확률 감소분을 반복적으로 추정한다. 준모수적 비례위험 모형은 구간중도절단 데이터에 적용 가능하며, 기저 위험의 구간별 상수 가정하에 최대우도 추정을 수행한다. 모수적 모형(Weibull, log-logistic 등)도 구간중도절단 우도함수를 구성하여 적합할 수 있으며, 구간 폭이 작을 때 표준 분석으로의 근사도 논의한다. 4판에서는 현대적 방법인 icenReg, survival 패키지 등을 활용한 방법으로 대폭 개정되었다. 궤양 재발 임상시험 데이터를 통해 구간중도절단 데이터의 변환, 생존함수 추정, 회귀모형 적합을 구체적으로 시연한다. 구간중도절단을 무시하고 상한 또는 하한만 사용하는 단순화가 편향을 초래할 수 있음을 경고한다. 중간값 대치(midpoint imputation)나 다중 대치 방법보다 구간중도절단 전용 분석법이 권장된다.

---

### Ch 10: Frailty models (pp. 301-330)

**핵심**: 관측되지 않은 이질성(unobserved heterogeneity)을 설명하는 프레일티(frailty) 효과를 다룬다. 동일 그룹 내 개인들의 생존시간이 독립이 아닌 경우, 공유 프레일티(shared frailty) 모형을 통해 그룹 내 상관성을 모형화하는 방법을 설명한다.

**키워드**: `frailty`, `shared frailty`, `unobserved heterogeneity`, `random effects`, `gamma frailty`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 10 (line 23066)

관측되지 않은 이질성(unobserved heterogeneity)을 설명하는 프레일티(frailty) 모형을 다룬다. 동일한 설명변수 값을 가진 개인들 사이에서도 생존시간이 다른 이유를 프레일티 효과로 설명하며, 프레일티가 큰 개인이 더 빨리 사망하는 경향이 있다. 프레일티 z_i는 위험함수에 승법적으로 작용하여 h_i(t) = z_i exp(β'x_i) h_0(t) 형태의 모형을 구성한다. z_i = exp(u_i)로 변환하면 u_i는 비례위험 모형의 선형 성분에 추가되는 랜덤효과(random effect)가 된다. 프레일티 분포로는 로그정규(lognormal) 분포와 감마(gamma) 분포가 주로 사용되며, 감마 프레일티는 해석적 편의성이 있다. 프레일티가 존재하면 선택 효과(selection effect)로 인해 관측된 위험함수가 실제보다 감소하는 것처럼 보일 수 있다. 공유 프레일티(shared frailty) 모형은 동일 그룹 내 개인들이 같은 프레일티를 공유하여 그룹 내 생존시간의 상관성을 모형화한다. 다기관 임상시험의 센터 효과, 동일 개인 내 반복 사건, 쌍체 기관(paired organs) 연구 등에서 공유 프레일티가 적용된다. 모수적 프레일티 모형의 추정은 EM 알고리즘이나 벌칙 편우도(penalised partial likelihood)를 사용한다. 준모수적 프레일티 모형에서는 편우도에 프레일티의 벌칙항을 추가하여 추정하며, 프레일티 분산의 유의성은 우도비 검정으로 평가한다. 유방암 예후, 사지 이식 데이터 등 예제를 통해 개인 프레일티와 공유 프레일티 모형의 적합 및 해석을 시연한다.

---

### Ch 11: Non-proportional hazards and institutional comparisons (pp. 331-352)

**핵심**: 비례위험 가정이 적절하지 않은 상황에서의 모형화 방법을 다룬다. 설명변수의 효과가 시간에 따라 변하는 경우의 대응 방법과, 의료기관 간 생존률 비교에서의 비비례위험 모형 적용을 설명한다.

**키워드**: `non-proportional hazards`, `institutional comparison`, `time-varying effects`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 11 (line 25268)

비례위험 가정이 적절하지 않은 상황에서의 모형화 방법과 의료기관 간 비교에서의 비비례위험 처리를 다룬다. 수술과 항암요법 비교처럼 단기적으로는 한 치료가 불리하지만 장기적으로 유리한 경우가 비비례위험의 전형적 예시이다. 특정 시점까지의 사건 발생 확률을 모형화하는 보완 로그-로그(complementary log-log) 모형을 이항 반응에 적용하는 방법을 설명한다. 층화 비례위험 모형(stratified PH model)은 각 층(stratum)에 별도의 기저 위험함수를 허용하면서 공변량 효과는 동일하게 추정한다. 제한 평균 생존시간(restricted mean survival time, RMST)은 비비례위험 상황에서 치료 효과를 요약하는 대안적 측도이다. RMST는 특정 시점 τ까지의 생존곡선 아래 면적으로 정의되며, 두 그룹 간 RMST 차이를 통해 치료 비교가 가능하다. 의료기관 비교(institutional comparison)에서는 기관 간 환자 구성(case-mix)의 차이를 보정해야 하며, 위험 보정(risk adjustment)이 필수적이다. 기관 효과를 랜덤효과로 모형화하는 프레일티 접근과 고정효과로 모형화하는 더미 변수 접근을 비교한다. 깔때기 도표(funnel plot)는 각 기관의 위험 보정 결과를 기관 크기 대비 시각화하여 이상치 기관을 식별하는 방법이다. 비비례위험 하에서의 가중 log-rank 검정(weighted log-rank test), 맥스콤비(MaxCombo) 검정 등 대안적 검정법도 논의한다. 궤양 재발, 간이식 데이터 등을 통해 비비례위험 상황에서의 분석 전략을 구체적으로 시연한다.

---

### Ch 12: Competing risks (pp. 353-372)

**핵심**: 환자가 여러 원인 중 하나로 사망할 수 있는 경쟁위험(competing risks) 상황의 데이터 요약 및 모형화 방법을 설명한다. 원인별 위험함수(cause-specific hazard)와 누적발생함수(cumulative incidence function) 접근법을 다룬다.

**키워드**: `competing risks`, `cause-specific hazard`, `cumulative incidence`, `Fine-Gray model`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 12 (line 26932)

여러 원인 중 하나로 사건이 발생할 수 있는 경쟁위험(competing risks) 상황의 데이터 요약 및 모형화 방법을 설명한다. 경쟁위험 데이터에서 Kaplan-Meier 추정은 다른 원인을 중도절단으로 처리하므로 원인별 사건 발생률을 과대추정하는 문제가 있다. 원인별 위험함수(cause-specific hazard)는 다른 모든 위험이 존재하는 상태에서 특정 원인의 순간 사망률을 나타낸다. 전체 위험함수는 원인별 위험함수의 합이며, 전체 생존함수는 S(t) = exp{−ΣH_j(t)}로 표현된다. 누적발생함수(cumulative incidence function, CIF)는 특정 원인에 의한 사건이 시간 t까지 발생할 확률을 나타내며, 모든 원인의 CIF 합이 1을 초과하지 않는다. CIF의 비모수적 추정은 원인별 위험함수 추정치와 전체 생존함수 추정치를 결합하여 산출한다. 원인별 위험 모형화는 Cox 회귀를 사용하여 각 원인별로 별도의 비례위험 모형을 적합하며, 다른 원인의 사건은 중도절단으로 처리한다. Fine-Gray 모형은 CIF에 직접 회귀 구조를 부여하여 부분분포위험(subdistribution hazard)을 모형화하며, 원인별 위험 모형과 다른 해석을 제공한다. 모형 검토에서는 원인별 모형과 Fine-Gray 모형 각각에 대한 잔차 분석과 PH 가정 검토가 필요하다. 간이식 환자의 이식편 실패(거부반응, 혈전, 재발, 기타) 데이터를 통해 경쟁위험 분석의 전 과정을 시연한다. 원인별 위험 모형과 Fine-Gray 모형의 계수 해석 차이와 각 접근법의 적절한 사용 상황을 비교 설명한다.

---

### Ch 13: Multiple events and event history modelling (pp. 373-394)

**핵심**: 동일 개인에서 반복 발생하는 사건(recurrent events)이나 여러 유형의 사건이 발생하는 다중 사건 데이터를 다룬다. 사건 이력 모형(event history modelling)과 다상태 모형(multistate models)을 설명한다.

**키워드**: `recurrent events`, `multiple events`, `event history`, `multistate model`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 13 (line 28460)

동일 개인에서 반복 사건(recurrent events)이나 여러 유형의 사건이 발생하는 다중 사건 데이터의 분석을 다룬다. 계수과정(counting process) N_i(t)는 시간 (0, t] 동안 발생한 사건 수를 세는 확률과정이며, 강도함수(intensity function)는 사건 발생률을 나타낸다. 계수과정의 강도함수를 비례위험 구조로 모형화하면 λ_i(t) = Y_i(t) exp(β'x_i(t)) λ_0(t) 형태가 된다. 표준 생존 데이터는 N_i(t)가 0에서 1로 한 번만 올라가는 특수 계수과정으로 해석할 수 있다. 반복 사건 모형화에는 Andersen-Gill(AG) 모형, 조건부(conditional) 모형, 주변(marginal) 모형의 세 가지 접근법이 있다. AG 모형은 모든 사건을 동일하게 취급하고 계수과정 형식으로 데이터를 구성하며, 클러스터 로버스트 분산을 사용한다. 조건부 모형은 사건 순서를 고려하여 각 사건 번째별로 별도의 기저 위험을 허용한다. 다상태 모형(multistate model)은 개인이 여러 상태를 거치는 질병 과정을 전이 강도(transition intensity)로 모형화한다. 사건 이력 분석(event history analysis)에서는 전이 확률 행렬과 Aalen-Johansen 추정치를 통해 각 상태의 점유 확률을 산출한다. 만성 신장질환의 투석-이식-거부-실패 과정이나 재발 감염 데이터 등의 예제를 통해 다중 사건 모형의 적합을 시연한다. 마팅게일 이론은 M_i(t) = N_i(t) − Λ_i(t)로 정의되며, 이는 4장의 마팅게일 잔차의 이론적 기반이 된다.

---

### Ch 14: Dependent censoring (pp. 395-406)

**핵심**: 독립 중도절단 가정이 위반되는 종속 중도절단(dependent censoring) 문제를 다룬다. 부작용으로 인한 이탈, 구제 약물(rescue medication) 투여 등으로 중도절단이 생존시간과 관련되는 경우의 분석 방법을 설명한다.

**키워드**: `dependent censoring`, `informative censoring`, `inverse probability weighting`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 14 (line 30055)

독립 중도절단 가정이 위반되는 종속 중도절단(dependent censoring) 문제를 다루며, 중도절단 시간과 생존시간 사이에 연관이 있는 경우의 분석 방법을 설명한다. 종속 중도절단은 치료 부작용으로 인한 이탈, 구제 약물(rescue medication) 투여, 환자 요청에 의한 중단 등에서 발생한다. 종속 중도절단의 존재는 관측 데이터만으로는 확인이 불가능하며, 연구 맥락에서 가능성을 판단해야 한다. 중도절단 확률이 설명변수에 의존하는지를 로지스틱 모형으로 검토하여 종속 중도절단의 가능성을 평가할 수 있다. 민감도 분석은 중도절단 관측치를 즉시 사건으로 처리하거나 가장 긴 사건시간 이후로 이동시키는 두 가지 극단적 분석을 비교한다. Weibull 비례위험 모형 기반의 정량적 민감도 분석에서는 위험 점수(risk score)와 중도절단 점수(censoring score)의 관계를 살펴본다. 민감도 지표 B(x)는 종속 중도절단의 강도 φ에 대한 위험 점수의 변화를 근사적으로 측정하며, 중도절단 위험이 클수록 민감도가 크다. 역확률 가중(inverse probability of censoring weighting, IPCW) 방법은 중도절단이 관측 공변량에만 의존할 때 종속 중도절단을 보정한다. IPCW는 각 개인의 중도절단 확률의 역수를 가중치로 사용하여 편우도를 수정한다. 간이식 대기 환자의 사망률 연구 데이터를 통해 민감도 분석과 IPCW 방법의 적용을 시연한다. 양의 종속성은 생존함수의 과대추정을, 음의 종속성은 과소추정을 초래할 수 있음을 보인다.

---

### Ch 15: Sample size requirements for a survival study (pp. 407-418)

**핵심**: 생존 연구 설계 시 표본 크기를 결정하는 방법을 다룬다. 포함/제외 기준, 추적관찰 기간, 순차적 설계(sequential design), 중간 분석(interim analysis), 적응적 설계(adaptive design) 등 다양한 설계 요소를 고려한 표본 크기 산출을 설명한다.

**키워드**: `sample size`, `power`, `sequential design`, `interim analysis`, `adaptive design`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 15 (line 30862)

생존 연구 설계 시 필요한 표본 크기를 결정하는 방법을 다루며, log-rank 검정에 기반한 공식을 제시한다. 필요 사망 수 d = 4c(α,β)/θ_R² 공식에서 θ_R은 탐지하고자 하는 참 로그위험비이고, c(α,β) = (z_{α/2} + z_β)²이다. 유의수준 α = 0.05, 검정력 1−β = 0.90일 때 c(α,β) = 10.51이며, 탐지하려는 위험비에 따라 필요 사망 수가 결정된다. 두 치료군에 동일 인원을 배정하지 않으면 필요 사망 수가 증가하며, 비율 π에 따른 보정 공식을 제시한다. 필요 사망 수를 필요 환자 수로 변환하려면 모집 기간(accrual period), 추적관찰 기간, 기대 사망 비율을 고려해야 한다. 지수분포 가정하에서 환자 모집률, 추적 기간, 예상 탈락률을 반영한 필요 환자 수 산출 공식을 유도한다. 위험비 대신 중앙 생존시간의 차이나 특정 시점 생존확률의 차이로부터 θ_R을 산출하는 방법도 설명한다. 순차적 설계(sequential design)는 데이터가 축적됨에 따라 중간 분석(interim analysis)을 수행하여 조기 종료 여부를 결정한다. 적응적 설계(adaptive design)는 축적된 데이터에 따라 표본 크기나 배정 비율을 사전 계획에 따라 수정할 수 있다. 다중 비교 보정(Bonferroni 등)이 중간 분석에서 필요하며, O'Brien-Fleming 경계가 자주 사용된다. 전립선암 임상시험 설계 예제를 통해 다양한 가정하에서의 표본 크기 산출을 구체적으로 시연한다.

---

### Ch 16: Bayesian survival analysis (pp. 419-446)

**핵심**: 4판에서 새로 추가된 장으로, 미지의 모형 모수를 확률변수로 간주하는 베이지안 추론 방법을 생존분석에 적용한다. 사전분포(prior), 사후분포(posterior), 우도함수의 결합을 통한 모수 추정과 구간 추정을 설명한다.

**키워드**: `Bayesian inference`, `prior distribution`, `posterior distribution`, `MCMC`, `credible interval`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 16 (line 31826)

4판에서 새로 추가된 장으로, 베이지안 추론 방법을 생존분석에 적용하는 방법을 체계적으로 설명한다. 베이즈 정리는 사전분포 π(θ)와 우도함수 L(t|θ)의 곱에 비례하는 사후분포 π(θ|t)를 산출하는 기본 원리이다. 생존 데이터의 우도함수는 모수적 모형에서 완전 우도를, Cox 모형에서 편우도를 사용할 수 있다. 구간별 지수 모형(piecewise exponential)은 기저 위험함수에 대한 사전정보를 반영할 수 있어 베이지안 준모수 모형의 기반이 된다. 사전분포의 선택에서 무정보 사전분포(non-informative prior)는 π(λ) ∝ λ^{-1} 등의 형태를 사용하며, 정보적 사전분포는 과거 연구 결과를 반영한다. 지수 모형의 단순한 경우 사후분포가 감마분포로 해석적으로 구해지지만, 복잡한 모형에서는 수치적 방법이 필요하다. 사후분포의 평가에는 MCMC(Markov chain Monte Carlo) 방법, 특히 Gibbs 샘플링과 Metropolis-Hastings 알고리즘이 사용된다. 사후 요약으로 점추정(사후 평균, 중앙값, 최빈값), 신용구간(credible interval), 최고사후밀도(HPD) 구간을 산출한다. 예측분포(predictive distribution)는 새로운 개인의 생존시간에 대한 확률적 예측을 제공하며, 사후분포로부터 유도된다. 베이지안 모형 비교에는 편차정보기준(DIC), WAIC, 베이즈 인자(Bayes factor) 등이 사용된다. IUD 사용 중단, 유방암 예후 데이터 등에 대한 베이지안 분석 예제를 JAGS/Stan 소프트웨어를 통해 시연한다.

---

### Ch 17: Survival analysis with R (pp. 447+)

**핵심**: R 소프트웨어를 사용하여 본서에서 다룬 생존분석 기법을 구현하는 방법을 설명한다. R 패키지의 풍부함, 새로운 통계 방법의 빠른 구현, 무료 이용 가능성 등 R의 장점과 함께 실습 코드를 제공한다.

**키워드**: `R`, `survival package`, `software`, `implementation`, `code examples`

**상세**: → `modelling_survival_data_in_medical_research.md` Ch 17 (line 34006)

R 소프트웨어를 사용하여 본서에서 다룬 생존분석 기법을 구현하는 방법을 설명한다. R은 풍부한 패키지 생태계, 새로운 통계 방법의 빠른 구현, 무료 이용 가능성이 장점이며, survival 패키지가 생존분석의 핵심 도구이다. 데이터 입력과 편집에서 data.frame 구성, 변수 변환, 요인(factor) 생성 등 기본 데이터 처리 방법을 소개한다. 비모수적 절차에서 survfit 함수를 이용한 Kaplan-Meier 추정과 survdiff 함수를 이용한 log-rank, Peto-Peto 검정의 코드를 제시한다. Cox 회귀모형 적합은 coxph 함수를 사용하며, 모형 공식(model formula), 동점 처리(ties), 층화(strata) 지정 방법을 설명한다. 모형 진단에서 잔차 추출(residuals 함수), cox.zph 함수를 이용한 PH 가정 검정, 영향력 분석 코드를 제공한다. 모수적 모형은 survreg 함수(AFT 모형)와 flexsurvreg 함수(유연 모수적 모형)를 사용하여 적합한다. 시간의존 변수 처리는 tmerge 함수를 이용한 계수과정 데이터 구성과 시간분할(time-splitting) 방법을 설명한다. 구간중도절단 데이터는 icenReg 패키지, 프레일티 모형은 coxph의 frailty 옵션이나 coxme 패키지로 적합한다. 경쟁위험 분석에는 cmprsk, tidycmprsk 패키지를, 다중 사건 및 다상태 모형에는 mstate 패키지를 사용한다. 베이지안 생존분석은 rstanarm, brms 패키지 또는 JAGS를 R에서 호출하여 수행하며, 사전분포 지정과 MCMC 진단 방법을 설명한다.
