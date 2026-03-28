---
name: "Survival Analysis: A Self-Learning Text (3rd Ed.)"
type: book-summary
sources:
  - file: "Kleinbaum-SurvivalAnalysis_azure_full.md"
    tool: Document Intelligence
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

생존분석이 다루는 문제(시간-사건 데이터)와 주요 목표를 자기학습 형식으로 소개한다. 생존시간(failure time)의 정의에서 시작점, 종료사건, 시간 측정 단위의 세 가지 요소를 명확히 해야 한다. 중도절단(censoring)의 세 유형으로 우측(right), 좌측(left), 구간(interval) 중도절단을 구분하며, 우측이 가장 흔하다. 중도절단 발생 이유로 연구 종료, 추적 실패(loss to follow-up), 경쟁적 사건에 의한 탈락을 설명한다. 무작위 중도절단(random censoring), 독립 중도절단(independent censoring), 비정보적 중도절단(noninformative censoring)의 개념적 차이를 설명한다. 비정보적 중도절단은 중도절단이 생존 전망과 무관함을 의미하며, 대부분의 생존분석 방법이 이 가정에 의존한다. 생존함수 S(t) = P(T > t)와 위험함수 h(t) = lim[P(t ≤ T < t+Δt | T ≥ t)/Δt]의 정의와 해석을 다룬다. 위험함수는 순간 잠재 사망률(instantaneous potential per unit time)로 해석되며, 확률이 아닌 비율(rate)이다. S(t)와 h(t)의 관계식 S(t) = exp{−∫h(u)du}를 유도하고, 한 함수로부터 다른 함수를 구할 수 있음을 보인다. Counting Process(CP) 데이터 레이아웃을 소개하며, (시작, 끝] 구간과 사건지시 변수로 데이터를 구성하는 방법을 설명한다. CP 레이아웃이 시간의존 변수, 반복 사건, 층화 분석 등에서 유연하게 활용되는 기반임을 예고한다.

---

### Ch 2: Kaplan-Meier Survival Curves and the Log-Rank Test (pp. 55-96)

**핵심**: Kaplan-Meier(KM) 생존곡선의 작성 및 해석 방법을 설명한다. 두 개 이상의 KM 곡선이 동일한지 검정하는 log-rank 검정과 대안적 검정법을 다루며, KM 곡선과 중앙 생존시간에 대한 95% 신뢰구간 산출 방법을 제시한다.

**키워드**: `Kaplan-Meier`, `log-rank test`, `confidence interval`, `median survival`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 2 (line 8350)

Kaplan-Meier(KM) 생존곡선의 작성과 해석, log-rank 검정을 자기학습 형식으로 설명한다. KM 추정의 핵심 공식 Ŝ(t) = Π[(n_j − d_j)/n_j]를 단계별로 유도하며, 중도절단 관측치가 위험집합에만 기여함을 설명한다. KM 곡선은 단조 감소하는 계단함수이며, 중도절단 시점에서는 곡선이 떨어지지 않고 관측치만 위험집합에서 제거된다. 중앙 생존시간은 KM 곡선이 0.5를 처음 교차하는 시점이며, 평균 생존시간보다 선호되는 요약 측도이다. KM 곡선에 대한 95% 신뢰구간은 Greenwood 공식 기반의 표준오차를 사용하여 구축한다. 로그 변환 또는 보완 로그-로그 변환을 적용하면 신뢰구간이 [0,1] 범위 안에 들어오도록 보정된다. log-rank 검정은 두 개 이상의 KM 곡선이 동일한지 검정하며, 각 사건 시점에서 관측-기대 차이를 합산한 통계량을 사용한다. log-rank 검정의 대안으로 Wilcoxon(Breslow), Tarone-Ware, Peto-Peto, 일반화 Flemington-Harrington 검정을 소개한다. 각 검정은 가중치의 차이로 초기 vs. 후기 사건에 대한 민감도가 다르며, log-rank은 비례위험 대안에 최적이다. 세 그룹 이상의 비교에서는 전체 검정(omnibus test)과 쌍별 비교(pairwise comparison)를 구분하며, 다중비교 보정을 논의한다. 연습문제와 풀이를 통해 KM 추정, log-rank 검정의 계산 과정을 반복 학습할 수 있다.

---

### Ch 3: The Cox Proportional Hazards Model and Its Characteristics (pp. 97-160)

**핵심**: Cox PH 모형의 수식적 형태와 그 인기의 이유를 설명한다. 최대우도(ML) 추정, 위험비(hazard ratio) 공식, 보정 생존곡선(adjusted survival curves) 도출 방법, 그리고 비례위험(PH) 가정의 의미를 다룬다. 연령을 시간 척도로 사용하는 방법도 추가되었다.

**키워드**: `Cox model`, `proportional hazards`, `partial likelihood`, `hazard ratio`, `baseline hazard`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 3 (line 14914)

Cox PH 모형의 수식적 형태, 인기의 이유, 최대우도 추정, 위험비 해석을 자기학습 형식으로 설명한다. Cox 모형 h(t,X) = h_0(t)exp(Σβ_iX_i)에서 기저 위험함수 h_0(t)는 미지정이므로 준모수적(semiparametric) 모형이다. 모형의 인기는 h_0(t)를 추정하지 않고도 위험비를 구할 수 있고, 다양한 공변량을 유연하게 포함할 수 있기 때문이다. 위험비 HR = exp(Σβ_i(X*_i − X_i))는 기저 위험이 소거되어 시간에 의존하지 않으며, 이것이 "비례위험" 가정의 의미이다. 최대편우도(maximum partial likelihood) 추정에서 편우도 함수의 구성과 뉴턴-랩슨 반복법에 의한 최대화를 설명한다. 우도비 검정, Wald 검정, 스코어 검정의 세 가지 통계적 검정 방법을 비교하고, 대표본에서의 동등성을 논의한다. 보정 생존곡선(adjusted survival curves)은 특정 공변량 조합에서의 생존함수를 S(t,X) = [Ŝ_0(t)]^{exp(β̂'X)}로 산출한다. 연령을 연속 시간 척도(time scale)로 사용하는 방법이 3판에서 추가되었으며, 연령-기간-코호트 효과를 분리하는 데 유용하다. 다양한 공변량 유형(이분, 다범주, 연속, 교호작용)에 대한 위험비의 구체적 산출과 해석을 예제로 설명한다. no-interaction 모형과 interaction 모형에서의 위험비 차이를 비교하고, 교호작용의 임상적 의미를 논의한다. 연습문제를 통해 Cox 모형의 적합, 위험비 산출, 신뢰구간 해석을 반복 학습한다.

---

### Ch 4: Evaluating the Proportional Hazards Assumption (pp. 161-200)

**핵심**: PH 가정을 평가하는 세 가지 접근법을 설명한다. 그래프적 방법(log-log 생존곡선, 관측 vs. 기대 플롯), 적합도 검정(GOF testing), 그리고 시간의존 변수를 이용한 검정이다.

**키워드**: `PH assumption`, `log-log plot`, `goodness-of-fit`, `time-dependent covariate`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 4 (line 21778)

PH 가정을 평가하는 세 가지 접근법을 자기학습 형식으로 설명한다. 그래프적 방법으로 로그-로그(log-log) 생존곡선 −log(−log Ŝ(t)) vs. log t의 평행성을 검토하며, 평행하면 PH 가정이 지지된다. 관측 vs. 기대(observed vs. expected) 도표는 Cox 모형의 기대 생존곡선과 KM 관측 생존곡선을 비교하여 PH 가정의 적합성을 시각적으로 평가한다. 적합도 검정(GOF testing) 접근에서는 Schoenfeld 잔차를 시간 변환 함수에 대해 회귀하여 기울기의 유의성으로 PH 가정을 검정한다. 시간의존 변수를 이용한 검정에서는 모형에 공변량×시간(또는 시간 함수) 교호작용 항을 추가하여 그 계수의 유의성을 검정한다. PH 가정 위반 시 대처 방안으로 층화 Cox 모형(Ch 5), 시간의존 변수 확장(Ch 6), 모수적 AFT 모형(Ch 7) 등을 예고한다. 각 접근법의 장단점을 비교하며, 그래프적 방법은 주관적이지만 직관적이고, GOF 검정은 객관적이지만 표본 크기에 민감하다. 다변량 모형에서 여러 공변량의 PH 가정을 동시에 평가하는 전체 검정(global test)도 설명한다. PH 가정 위반의 정도와 방향(초기 vs. 후기 효과 차이)에 따른 해석 지침을 제공한다. 구체적 예제로 약물 투여군 vs. 위약군, 연령, 성별 등 다양한 공변량에 대한 PH 가정 평가를 시연한다. 연습문제를 통해 세 가지 접근법의 적용과 결과 해석을 반복 학습한다.

---

### Ch 5: The Stratified Cox Procedure (pp. 201-240)

**핵심**: PH 가정을 만족하지 않는 예측변수를 층화변수로 처리하는 Stratified Cox 모형을 설명한다. 층화의 수행 방법, 컴퓨터 결과 해석, 위험비 산출, 단일 예측변수 vs. 다중 예측변수 상황에서의 적용을 다룬다.

**키워드**: `stratified Cox`, `stratification`, `non-proportional hazards`, `hazard ratio`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 5 (line 25565)

PH 가정을 만족하지 않는 예측변수를 층화변수로 처리하는 Stratified Cox 모형을 자기학습 형식으로 설명한다. 층화 Cox 모형에서 각 층은 별도의 기저 위험함수 h_{0k}(t)를 가지지만, 공변량의 β 계수는 층 간에 동일하다. 층화의 수행은 PH 가정을 위반하는 변수를 층화변수로 지정하고, 나머지 공변량은 모형에 포함하는 방식이다. 층화 편우도는 각 층의 편우도의 곱으로 구성되며, 위험집합은 층 내에서만 형성된다. 층화 변수가 PH 가정을 만족하지 않더라도 다른 공변량에 대한 위험비를 타당하게 추정할 수 있다. no-interaction 층화 모형과 interaction 층화 모형을 구분하며, 후자는 층에 따라 공변량 효과가 다를 수 있음을 모형화한다. interaction 모형에서 각 층별 위험비는 주효과와 교호작용 계수를 결합하여 산출한다. 층화 변수가 여러 개일 때 결합 층(combined strata)을 형성하며, 층의 수가 과도하면 각 층의 표본이 부족해질 수 있다. 층화 Cox 모형의 한계로 층화 변수의 효과를 직접 추정할 수 없다는 점을 지적한다. 보정 생존곡선은 각 층별로 별도의 기저 생존함수를 사용하여 산출한다. 연습문제를 통해 층화 Cox 모형의 적합, 위험비 산출, 모형 비교를 반복 학습한다.

---

### Ch 6: Extension of the Cox PH Model for Time-Dependent Variables (pp. 241-288)

**핵심**: Cox PH 모형을 시간의존 변수(time-dependent variables)로 확장하는 방법을 설명한다. 모형의 형태와 특성, 위험비 해석, PH 가정 확인 방법, 그리고 컴퓨터 적용 예제를 포함한다.

**키워드**: `time-dependent covariates`, `extended Cox model`, `counting process`, `hazard ratio`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 6 (line 29984)

Cox PH 모형을 시간의존 변수(time-dependent variables)로 확장하는 방법을 자기학습 형식으로 설명한다. 확장된 Cox 모형 h(t,X(t)) = h_0(t)exp(Σβ_iX_i(t))에서 공변량 X_i(t)가 시간에 따라 변할 수 있다. 시간의존 변수가 포함되면 위험비가 시간에 따라 변하므로 모형은 비비례위험 모형이 된다. 시간의존 변수의 유형으로 정의된(defined) 변수(X×g(t) 형태)와 내부(internal) 변수(반복 측정값)를 구분한다. 정의된 시간의존 변수는 PH 가정 검정에 사용되며, X×t, X×log(t) 등의 형태가 일반적이다. 내부 시간의존 변수는 혈압, 약물 투여 상태 변화 등 개인별로 시간에 따라 측정되는 변수이다. 확장된 Cox 모형에서의 위험비 해석은 특정 시점 t에서 두 패턴 X*(t)와 X(t)를 비교하는 것이다. 시간의존 변수가 포함된 모형에서는 보정 생존곡선을 직접 산출할 수 없어 해석이 제한적이다. 데이터 구조는 Counting Process(CP) 형식의 (시작, 끝, 사건) 삼중 항으로 구성하며, 각 구간에서 공변량이 상수이다. PH 가정 평가를 위한 시간의존 변수 활용과 진정한 시간의존 공변량의 모형화를 구분하여 설명한다. 연습문제를 통해 확장된 Cox 모형의 적합, 위험비 해석, CP 데이터 구성을 반복 학습한다.

---

### Ch 7: Parametric Survival Models (pp. 289-362)

**핵심**: 모수적 모형(parametric models)을 개관하며, 지수(exponential), Weibull, log-logistic 모형을 예제와 함께 설명한다. 가속실패시간(AFT) 모형과 PH 모형의 관계를 비교하고, 구간중도절단(interval-censoring), 프레일티(frailty) 모형도 간략히 소개한다.

**키워드**: `exponential`, `Weibull`, `log-logistic`, `AFT model`, `parametric likelihood`, `frailty`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 7 (line 35166)

모수적 생존 모형의 개관과 주요 분포(지수, Weibull, log-logistic)를 자기학습 형식으로 설명한다. 모수적 모형은 기저 위험함수의 형태를 특정 확률분포로 가정하며, 가정이 타당하면 Cox 모형보다 효율적인 추정이 가능하다. 지수 모형은 h(t) = λ로 상수 위험을 가정하며, 비례위험(PH)과 가속실패시간(AFT) 모형 모두에 해당한다. Weibull 모형은 h(t) = λpt^{p-1}로 단조적 위험을 허용하며, PH와 AFT 모형 모두로 표현 가능한 유일한 분포이다. Weibull PH 모형에서 위험비 exp(β)와 AFT 모형의 가속인자 exp(−β/p)는 부호와 크기가 다르므로 해석에 주의가 필요하다. log-logistic 모형은 위험함수가 단봉일 수 있어 비단조적 패턴을 모형화하며, 비례오즈(proportional odds) 구조를 갖는다. log-logistic 모형은 PH 모형이 아니므로 위험비가 시간에 따라 변하며, 오즈비(odds ratio)로 효과를 해석한다. 구간중도절단(interval-censoring) 데이터에 대한 모수적 모형의 적용 방법을 간략히 소개한다. 프레일티(frailty) 모형은 모수적 기저 위험에 랜덤효과를 추가하여 미관측 이질성을 모형화한다. 모형 선택 기준으로 AIC, 그래프적 적합도(Cox-Snell 잔차 도표), 내포 모형에 대한 우도비 검정을 설명한다. 연습문제를 통해 각 모수적 모형의 적합, 가속인자·위험비의 산출과 해석을 반복 학습한다.

---

### Ch 8: Recurrent Event Survival Analysis (pp. 363-424)

**핵심**: 동일 대상에서 반복 발생하는 사건(recurrent events)의 분석 방법을 다룬다. Counting Process(CP) 접근법을 중심으로 Cox PH 모형 활용, Stratified Cox PH 모형, 프레일티 모형 등 대안적 접근법을 설명한다.

**키워드**: `recurrent events`, `counting process`, `stratified Cox`, `frailty model`, `gap time`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 8 (line 41822)

동일 대상에서 반복 발생하는 사건(recurrent events)의 분석 방법을 자기학습 형식으로 다룬다. 반복 사건 데이터의 핵심 문제는 동일 개인 내 사건들의 비독립성(within-subject correlation)이다. Counting Process(CP) 접근법은 추적 기간을 사건 기준으로 분할하고, 각 구간을 (시작, 끝, 사건) 형태로 구성한다. CP 데이터 배열에서 총 시간(total time)과 갭 시간(gap time) 스케일의 차이를 설명하며, 각각의 해석적 의미를 비교한다. Andersen-Gill(AG) 모형은 총 시간 스케일에서 모든 사건을 동일하게 취급하며, 편우도는 표준 Cox 모형과 동일한 형태이다. AG 모형에서 개인 내 상관을 보정하기 위해 로버스트(robust/sandwich) 분산 추정을 사용한다. 층화 Cox PH 모형은 사건 순서(k번째 사건)별로 별도의 기저 위험을 허용하여 사건 순서 효과를 모형화한다. 조건부 모형(WLW, PWP)에서 WLW는 주변 모형으로 각 사건을 별도 과정으로, PWP는 조건부 모형으로 이전 사건 발생 후의 위험을 모형화한다. 프레일티 모형은 개인별 랜덤효과를 추가하여 개인 내 사건의 비독립성을 직접 모형화한다. 각 접근법의 데이터 배열, 위험집합 구성, 위험비 해석의 차이를 표와 예제를 통해 비교한다. 연습문제를 통해 CP 데이터 구성, AG·층화·프레일티 모형의 적합과 해석을 반복 학습한다.

---

### Ch 9: Competing Risks Survival Analysis (pp. 425-496)

**핵심**: 서로 다른 유형의 사건이 경쟁적으로 발생할 수 있는 경쟁위험(competing risks) 상황을 다룬다. Cox PH 모형을 이용한 분석과 그 한계점, 그리고 이를 보완하는 접근법들을 설명한다.

**키워드**: `competing risks`, `cause-specific hazard`, `cumulative incidence`, `Cox model`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 9 (line 51449)

서로 다른 유형의 사건이 경쟁적으로 발생할 수 있는 경쟁위험(competing risks) 상황을 자기학습 형식으로 다룬다. 경쟁위험은 관심 사건의 관찰을 방해하는 다른 사건이 존재하는 상황으로, 사망 원인이 여러 가지인 경우가 전형적이다. Cox PH 모형을 이용한 원인별 위험 분석에서 관심 원인 외 사건은 중도절단으로 처리하여 원인별 위험비를 추정한다. 원인별 위험 분석의 한계는 다른 원인의 사건이 독립적 중도절단이 아닐 수 있다는 가정의 위반 가능성이다. Kaplan-Meier 1 − Ŝ(t)는 경쟁위험 상황에서 원인별 사건 발생 확률을 과대추정하므로 부적절하다. 누적발생함수(Cumulative Incidence Function, CIF)는 경쟁위험을 고려한 올바른 사건 발생 확률 측도이다. CIF의 비모수적 추정은 원인별 위험과 전체 생존함수를 결합하여 산출하며, 모든 원인의 CIF 합이 1을 초과하지 않는다. Fine-Gray 모형은 부분분포위험(subdistribution hazard)에 대한 비례위험 구조를 모형화하며, CIF에 대한 직접적 추론을 가능하게 한다. Fine-Gray 모형의 위험집합에서는 경쟁 사건이 발생한 개인이 이후에도 위험집합에 (가중) 잔류하는 특이한 구조를 갖는다. 원인별 위험 모형과 Fine-Gray 모형의 계수 해석 차이를 비교하며, 전자는 병인론적(etiological), 후자는 예측적(prognostic) 관점에 적합하다. 연습문제를 통해 경쟁위험 분석의 데이터 구성, CIF 추정, 두 모형의 적합과 해석을 반복 학습한다.

---

### Ch 10: Design Issues for Randomized Trials (pp. 497-524)

**핵심**: 3판에서 새로 추가된 장으로, 시간-사건 데이터를 포함하는 무작위 임상시험의 설계 문제를 다룬다. 표본 크기(sample size) 산정, 모집 기간(accrual period), 추적관찰 기간, 치료 전환(therapy switching) 시 대처 방법 등 통계적 의사결정 사항을 설명한다.

**키워드**: `sample size`, `power`, `accrual period`, `randomized trial`, `study design`

**상세**: → `Kleinbaum & Klein - Survival Analysis_ A Self-Learning Text (3rd Ed.).md` Ch 10 (line 59803)

3판에서 새로 추가된 장으로, 시간-사건 결과를 포함하는 무작위 임상시험의 설계 문제를 다룬다. 표본 크기 산정의 기본 공식 d = 4(z_{α/2} + z_β)²/θ²에서 d는 필요 사건 수, θ는 탐지하려는 로그 위험비이다. 필요 사건 수를 필요 환자 수로 변환하려면 모집 기간(accrual period)과 추적관찰 기간 동안의 예상 사건 발생 비율을 고려해야 한다. 모집 기간과 추적 기간의 결합에서 환자의 등록 시점이 균일분포를 따르는 가정이 일반적이다. 기대 사건 비율은 지수분포 또는 Weibull 분포 가정하에서 산출하며, 중도절단 비율을 반영하여 보정한다. 치료 전환(therapy switching) 문제는 대조군 환자가 실험 치료를 받게 되는 경우로, 의향치료(intention-to-treat, ITT) 분석과 실제치료(as-treated) 분석의 차이를 설명한다. ITT 분석은 편향을 방지하지만 치료 효과를 희석시킬 수 있으며, 이를 보정하는 방법으로 역확률가중(IPCW) 등을 소개한다. 비열등성(non-inferiority) 시험에서의 표본 크기 산정은 비열등성 마진의 설정이 핵심이며, 우월성 시험과 다른 가설 구조를 갖는다. 중간 분석(interim analysis)에서 조기 중단 규칙(stopping rules)으로 O'Brien-Fleming, Pocock 경계, 알파 소비 함수(alpha spending function)를 소개한다. 적응적 설계(adaptive design)는 축적된 데이터에 따라 표본 크기나 배정 비율을 사전 계획에 따라 수정할 수 있는 설계이다. 연습문제를 통해 다양한 가정하에서의 표본 크기 산출과 설계 요소 결정을 반복 학습한다.
