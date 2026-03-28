---
name: "Epidemiology: Study Design and Data Analysis"
type: book-summary
sources:
  - file: "Woodward-Epidemiology_azure_full.md"
    tool: Document Intelligence
authors: "Mark Woodward"
year: 2014
total_pages: 849
language: en
keywords: [epidemiology, study design, cohort study, case-control, clinical trial, logistic regression, survival analysis, meta-analysis, confounding, sample size]
---

# Epidemiology: Study Design and Data Analysis — Summary

> Mark Woodward (2014, 3rd ed.), 849 pages, 14 chapters
> 역학 연구 설계와 데이터 분석을 통계학적 관점에서 체계적으로 다루는 교과서

## Contents

1. Fundamental issues (p.1)
2. Basic analytical procedures (p.23)
3. Assessing risk factors (p.89)
4. Confounding and interaction (p.125)
5. Cohort studies (p.165)
6. Case-control studies (p.211)
7. Intervention studies (p.257)
8. Sample size determination (p.297)
9. Modelling quantitative outcome variables (p.323)
10. Modelling binary outcome data (p.371)
11. Modelling follow-up data (p.431)
12. Meta-analysis (p.513)
13. Risk scores and clinical decision rules (p.557)
14. Computer-intensive methods (p.601)

---

## Chapter Summaries

### Ch 1: Fundamental issues (pp. 1-22)

**핵심**: 역학의 정의, Doll과 Hill의 사례 연구(흡연과 폐암)를 통한 역학의 기본 원리를 소개한다. 모집단과 표본, 발생률과 유병률, 인과성의 원칙, 일상 데이터를 이용한 연구, 연구 설계의 분류(개입/관찰 연구)를 다룬다.

**키워드**: `epidemiology`, `incidence`, `prevalence`, `causality`, `study design`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 1 (line 3525)
역학(epidemiology)은 인간 집단에서 질병의 분포와 결정 요인을 연구하는 학문이다. 질병의 지리적·인구통계학적 분포를 기술하는 기술역학과 질병의 원인을 탐구하는 분석역학으로 나뉜다. Doll과 Hill의 흡연-폐암 연구를 사례로 소개하며, 환자-대조군 연구(1948-1949)와 영국 의사 코호트 연구(1951-)를 통해 역학 연구의 핵심 원리를 설명한다. 환자-대조군 연구에서 폐암 환자가 대조군보다 흡연량이 많았고, 코호트 연구에서 하루 25개비 이상 흡연자는 비흡연자 대비 폐암 사망률이 30배 이상 높았다. 모집단(target population)과 연구 집단(study population), 표본(sample)의 관계를 설명하며, 일반화 가능성의 문제를 논의한다. 발생률(incidence)은 새로운 질병 발생의 빈도를, 유병률(prevalence)은 특정 시점의 질병 보유 비율을 측정한다. 인과성 판단을 위한 Bradford Hill 기준(연관성의 강도, 일관성, 특이성, 시간적 선행성, 용량-반응 관계 등)을 제시한다. 일상 데이터(사망 등록, 질병 등록 등)의 활용과 한계를 다루며, 연구 설계를 개입 연구와 관찰 연구(코호트, 환자-대조군, 횡단면)로 분류한다. 관찰 연구는 연구자가 노출 요인을 통제하지 않고 자연 상태에서 관찰하는 반면, 개입 연구는 치료 배정을 계획적으로 수행한다. 역학 연구의 궁극적 목표는 공중보건 전문가와 일반 대중에게 정보를 제공하여 전반적인 건강 상태를 개선하는 것이다.

### Ch 2: Basic analytical procedures (pp. 23-88)

**핵심**: 역학 데이터 분석의 기본 절차를 다룬다. 변수 유형, 표와 그래프, 범주형 변수의 추론(분할표, 비율 비교), 양적 변수의 기술 통계(5-number summary, 분위수), 평균 비교, 비정규 데이터 처리, 일치도 측정, 진단 검사 평가를 포함한다.

**키워드**: `contingency table`, `chi-square test`, `nonparametric test`, `kappa`, `sensitivity`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 2 (line 5101)
역학 데이터의 기본 분석 절차를 기술 통계와 추론 통계로 나누어 설명한다. 추론 분석의 두 축인 가설 검정(귀무가설의 기각 여부 판단)과 추정(신뢰구간을 통한 모수 추정)을 소개하며, 일반적으로 추정이 가설 검정보다 유용하다고 강조한다. 스코틀랜드 심장 건강 연구(SHHS)를 사례 연구로 도입하여 이후 장에서 반복 활용한다. 변수 유형을 질적 변수(범주형, 순서형, 이항)와 양적 변수(이산형, 연속형)로 분류하고, 이들 간의 위계 구조를 설명한다. 범주형 변수의 기술 통계로 도수분포표, 막대 그래프, 원형 그래프를 제시하며, 보고서에서 표 작성 시 자기 완결성, 시각적 매력, 자연스러운 순서, 수직 배치를 권장한다. 분할표를 활용한 범주형 변수 간 관계 분석과 카이제곱 검정의 원리를 설명한다. 양적 변수에 대해 5-number summary, 히스토그램, 상자 그림 등 기술 통계와 평균 비교를 위한 t 검정을 다룬다. 비정규 데이터 처리를 위한 변환(로그, 제곱근 등)과 비모수 검정(Wilcoxon, Mann-Whitney)을 소개한다. 관찰자 간 일치도 측정을 위한 카파(kappa) 통계량과 진단 검사 평가를 위한 민감도(sensitivity), 특이도(specificity), 양성 예측도를 설명한다. 상관계수와 산점도를 통한 두 양적 변수 간 관계 분석 방법도 제시한다.

### Ch 3: Assessing risk factors (pp. 89-124)

**핵심**: 위험(risk)과 상대 위험(relative risk), 오즈비(odds ratio), 유병률 연구, 연관성 검정, 다수준 위험 요인, 기여 위험(attributable risk), 율(rate)과 상대율을 다룬다.

**키워드**: `relative risk`, `odds ratio`, `attributable risk`, `rate`, `trend test`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 3 (line 11273)
위험(risk)은 특정 속성을 가진 개인이 질병에 걸릴 확률이며, 상대 위험(relative risk)은 위험 요인 보유 집단과 비보유 집단 간 위험의 비율이다. 2x2 분할표에서 위험과 상대 위험의 계산 공식을 도출하고, 태국 EGAT 연구 데이터를 활용하여 흡연자의 심혈관 사망 상대 위험이 2.77임을 보인다. 오즈(odds)는 질병 발생 수 대 비발생 수의 비율이며, 오즈비(odds ratio)는 두 집단 간 오즈의 비율로 ad/bc 공식으로 계산한다. 질병이 드물 때 오즈비는 상대 위험의 좋은 근사값이 되며, 미노출 집단의 위험과 상대 위험이 모두 낮을 때 근사가 가장 정확하다. 유병률 연구에서는 위험 대신 유병률 위험, 유병률 오즈비 등의 접두어를 사용하여 발생률 기반 측도와 구분한다. 다수준 위험 요인에 대한 추세 검정을 설명하며, 순서형 노출 수준에서 용량-반응 관계를 평가하는 방법을 제시한다. 기여 위험(attributable risk)은 위험 요인에 기인하는 질병 사례의 비율을 나타내며, 모집단 수준의 공중보건적 영향을 평가하는 데 활용된다. 율(rate)은 인-시간(person-time)을 분모로 사용하는 측도로, 위험과 달리 추적 기간의 변동을 반영한다. 상대율(rate ratio)과 그 신뢰구간 계산 방법을 설명하고, 가설 검정의 한계(p 값의 표본 크기 의존성)를 논의하며 신뢰구간 사용을 권장한다. 상대 위험과 오즈비의 로그 변환을 통한 정규 근사와 신뢰구간 산출 공식을 상세히 유도한다.

### Ch 4: Confounding and interaction (pp. 125-164)

**핵심**: 교란의 개념, 식별 전략, 평가 방법, 표준화(직접/간접), Mantel-Haenszel 방법, 상호작용의 개념과 검정(상대위험/오즈비/위험차 기반)을 다룬다.

**키워드**: `confounding`, `standardisation`, `Mantel-Haenszel`, `interaction`, `effect modification`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 4 (line 14184)
교란(confounding)은 제3의 변수가 위험 요인과 질병 간의 겉보기 관계를 전체 또는 부분적으로 설명하는 현상이다. 가상 예제를 통해 교란이 없는 관계를 있는 것처럼 보이게 하거나(양의 교란), 실제 존재하는 관계를 숨기는(음의 교란) 경우를 모두 설명한다. 교란 변수의 필요 조건은 질병과 관련되어야 하고(질병의 결과가 아닌), 위험 요인과도 관련되어야 한다(위험 요인의 결과가 아닌)는 것이다. 경로 다이어그램을 사용하여 교란이 성립하는 세 가지 상황과 성립하지 않는 네 가지 상황을 구분한다. 교란 평가 방법으로 전체 추정치와 층별 추정치의 비교, 변화율(10% 기준) 계산을 제시한다. 직접 표준화(direct standardisation)는 공통 표준 인구에 각 집단의 층별 율을 적용하여 비교 가능한 요약률을 산출하는 방법이다. 간접 표준화(indirect standardisation)는 표준 인구의 층별 율을 연구 집단에 적용하여 표준화 사망비(SMR)를 계산한다. Mantel-Haenszel 방법은 층화된 2x2 표에서 교란을 통제한 상태의 공통 오즈비를 추정하며, 가중 평균 방식으로 각 층의 정보를 결합한다. 상호작용(interaction)은 제3의 변수가 위험 요인과 질병 간 관계의 크기를 변경하는 현상으로, 교란과는 본질적으로 다르다. 상호작용 검정은 상대 위험, 오즈비, 위험차 등 사용하는 척도에 따라 결과가 달라질 수 있으며, 상대 위험 기반 검정이 가장 흔히 사용된다. SHHS 데이터를 사용하여 주거 형태와 관상동맥 심장병 관계에서 흡연의 교란 효과를 실증적으로 분석한다.

### Ch 5: Cohort studies (pp. 165-210)

**핵심**: 코호트 연구의 설계(장단점, 동시 추적, 이탈), 코호트 생명표, Kaplan-Meier 추정, 생존 함수 비교(로그순위 검정), 경쟁 위험, 인-년 방법, 기간-코호트 분석을 다룬다.

**키워드**: `cohort study`, `Kaplan-Meier`, `log-rank test`, `person-years`, `competing risk`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 5 (line 17721)
코호트(전향적) 연구는 개인을 시간에 걸쳐 추적하여 건강 결과를 모니터링하는 설계이다. 기본 설계는 위험 요인 보유 집단과 비보유 집단을 기저선(baseline)에서 선정한 후 질병 발생을 비교하며, 인과 관계 입증에 유리하다는 장점이 있다. 단점으로는 높은 비용, 긴 잠복기 질병에 부적합, 희귀 질병 연구의 비효율성, 연구 효과에 의한 행동 변화, 추적 중 노출 변화, 탈락 등이 있다. 비요인 집단 생략, 외부 비교 집단 사용, 사망만 기록, 일상 통계를 통한 사건 알림, 후향적 코호트 등 비용 절감을 위한 대안 설계를 제시한다. 단일 기저선 표본 설계는 여러 위험 요인을 동시에 연구할 수 있으며, 건강한 근로자 효과(healthy worker effect) 등의 편향 가능성을 논의한다. 코호트 생명표(life table)를 통해 구간별 위험, 생존 확률, 누적 생존 확률을 계산하는 방법을 설명한다. Kaplan-Meier 추정법은 정확한 사건 시점을 이용하여 계단 함수 형태의 생존 함수를 추정하며, 중도절단 데이터를 자연스럽게 처리한다. 로그순위 검정(log-rank test)은 두 개 이상의 생존 곡선을 비교하는 비모수적 가설 검정법으로, 기대 사건 수와 관측 사건 수의 차이를 기반으로 한다. 경쟁 위험(competing risk)은 관심 사건 외 다른 사건이 관찰을 종료시키는 상황으로, 이를 중도절단으로 처리하면 편향이 발생할 수 있다. 인-년(person-years) 방법은 추적 기간이 불균등한 코호트에서 율(rate)을 계산하는 표준적 접근법이며, 표준화 사망비(SMR)와 연결된다. 기간-코호트 분석은 연령 효과, 기간 효과, 코호트 효과를 분리하여 시간적 추세를 이해하고자 하는 방법이다.

### Ch 6: Case-control studies (pp. 211-256)

**핵심**: 환자-대조군 연구의 기본 설계, 분석 방법, 환자와 대조군 선택, 매칭(1:1, 1:c, variable matching), 중첩 환자-대조군, 환자-코호트, 환자-교차 연구를 다룬다.

**키워드**: `case-control study`, `matching`, `nested case-control`, `case-crossover`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 6 (line 22402)
환자-대조군(case-control) 연구는 질병이 있는 사람(환자)과 없는 사람(대조군)을 선정한 후 과거의 위험 요인 노출을 비교하는 후향적 설계이다. 장점으로는 코호트 연구보다 빠르고 저렴하며, 희귀 질병과 긴 잠복기 질병에 적합하고, 작은 표본으로도 수행 가능하다는 점이 있다. 단점으로는 시간 순서를 입증할 수 없어 인과성 증명이 어렵고, 하나의 질병만 연구 가능하며, 위험과 상대 위험을 직접 추정할 수 없다는 점이 있다. 환자-대조군 연구에서 표본 추출 분율이 환자와 대조군에서 다르기 때문에 위험과 상대 위험은 추정 불가능하지만, 오즈비는 추출 분율이 상쇄되어 유효한 추정이 가능하다. 편향 오차(회상 편향, 선택 편향 등)가 발생하기 쉬우므로 눈가림, 신중한 환자-대조군 선택 등으로 최소화해야 한다. 매칭(matching)은 환자와 대조군을 나이, 성별 등 잠재적 교란 변수에 대해 짝짓는 방법으로, 1:1 매칭과 1:c 매칭이 있다. 매칭된 데이터의 분석에는 McNemar 검정(1:1)이나 조건부 방법이 사용되며, 비매칭 분석을 적용하면 편향이 발생한다. 중첩 환자-대조군(nested case-control) 연구는 기존 코호트 내에서 환자-대조군을 선정하여 코호트 연구의 장점을 유지하면서 비용을 절감한다. 환자-코호트(case-cohort) 설계는 코호트에서 무작위 하위 코호트를 선정하고 모든 환자를 포함하여 분석한다. 환자-교차(case-crossover) 설계는 각 환자가 자신의 대조군 역할을 하여 일시적 노출의 급성 효과를 연구하는 데 적합하다. 벨기에·프랑스·독일의 흑색종 연구에서 어린 시절 자외선 차단 여부에 따른 오즈비가 0.72로 추정되어 자외선 차단의 보호 효과를 보인 예를 제시한다.

### Ch 7: Intervention studies (pp. 257-296)

**핵심**: 개입 연구(임상 시험)의 설계를 다룬다. 윤리적 고려, 편향 회피(대조군, 눈가림, 무작위 배정), 병행 설계, 교차 설계, 순차 설계, 치료군 배정 방법(전역/층화/적응 무작위 배정)을 포함한다.

**키워드**: `clinical trial`, `blinding`, `randomisation`, `crossover design`, `sequential design`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 7 (line 26379)
개입 연구(임상 시험)는 기존 환자에게 치료 효과를 평가하거나 건강한 대상에게 예방 전략을 평가하기 위한 실험적 설계이다. 핵심 특징은 연구자가 대상자에 대한 치료 배정을 계획적으로 결정한다는 점에서 관찰 연구와 구분된다. 장점으로는 원인이 결과에 선행함을 보장하고, 교란 요인을 통제할 수 있으며, 치료 집단 간 효율적 비교가 가능하다. 단점으로는 전향적 데이터 수집에 따른 코호트 연구와 유사한 문제점, 윤리적 제약, 연구 대상의 일반화 가능성 제한 등이 있다. 헬싱키 선언에 기반한 윤리적 고려를 논의하며, 모든 임상 시험은 윤리위원회(IRB)의 승인과 참가자의 사전 동의(informed consent)가 필요하다. 편향 회피를 위해 대조군 사용(위약 또는 기존 치료), 눈가림(단일·이중·삼중), 무작위 배정을 핵심 원칙으로 제시한다. 병행 설계(parallel design)는 가장 기본적인 형태로 대상자를 무작위로 치료군에 배정하여 결과를 비교한다. 교차 설계(crossover design)는 각 대상자가 모든 치료를 순서대로 받아 개인 내 비교를 가능하게 하며, 이월 효과(carryover effect)가 문제가 될 수 있다. 순차 설계(sequential design)는 데이터가 축적됨에 따라 중간 분석을 수행하여 조기 종료 여부를 결정한다. 치료군 배정 방법으로 전역 무작위 배정(simple randomisation), 층화 무작위 배정(stratified randomisation), 최소화법(minimisation) 등 적응적 무작위 배정 방법을 설명한다. IQ 점수에 대한 비타민·미네랄 보충제의 효과를 위약과 비교한 던디 연구에서 유의한 차이가 발견되지 않은 사례를 제시한다.

### Ch 8: Sample size determination (pp. 297-322)

**핵심**: 표본 크기 결정의 원리와 공식을 다룬다. 두 비율 비교, 두 평균 비교, 코호트/환자-대조군/매칭 연구, 임상 시험(교차/순차 설계 포함)에 대한 표본 크기 계산을 포함한다.

**키워드**: `sample size`, `power`, `type I error`, `type II error`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 8 (line 29686)
역학 연구 계획 시 표본 크기(sample size) 결정은 필수적이며, 너무 큰 표본은 자원 낭비를, 너무 작은 표본은 결과의 정밀도 부족을 초래한다. 검정력(power)은 귀무가설이 거짓일 때 이를 기각할 확률로, 제2종 오류(β)의 보수(1-β)이다. 표본 크기 공식은 유의 수준(α), 검정력(1-β), 효과 크기, 표준편차에 의해 결정되며, 단측 검정과 양측 검정에 따라 공식이 달라진다. 단일 평균 검정에 대한 표본 크기 공식 n = (z_α + z_β)²σ² / (μ₁ - μ₀)²를 유도하며, 개발도상국 콜레스테롤 연구를 예로 설명한다. 두 비율 비교(χ² 검정 기반)에 대한 표본 크기 공식은 Fleiss 보정을 포함하여 연속성 보정이 가능하다. 두 평균 비교를 위한 표본 크기는 pooled t 검정에 기반하며, 두 집단의 크기가 동일할 때 가장 효율적이다. 코호트 연구의 표본 크기는 상대 위험의 크기, 비노출군의 질병 발생률, 위험 요인 유병률에 따라 결정된다. 환자-대조군 연구에서는 오즈비의 크기와 환자 대 대조군의 비율(1:c)을 고려하며, c가 증가할수록 검정력이 향상되나 c=4 이상에서는 한계 효용이 크게 감소한다. 매칭된 환자-대조군 연구의 표본 크기 계산은 불일치 쌍(discordant pairs)의 비율에 의존한다. 임상 시험(교차 설계, 순차 설계 포함)의 표본 크기 결정 방법과, 검정력 곡선을 통한 시각적 해석 방법을 제시한다. 표본 크기 계산에 필요한 모수 값의 사전 추정이 불확실하므로, 계산 결과는 근사적 지침으로 활용해야 한다고 강조한다.

### Ch 9: Modelling quantitative outcome variables (pp. 323-370)

**핵심**: 양적 결과 변수에 대한 회귀 모형을 다룬다. 단순/다중 선형 회귀, 모형 진단, 변수 선택, 분산분석과의 관계, 일반화 선형 모형 소개를 포함한다.

**키워드**: `linear regression`, `multiple regression`, `model diagnostics`, `variable selection`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 9 (line 31773)
통계 모형은 결과 변수(y)와 하나 이상의 설명 변수(x) 간의 관계를 수학적으로 표현하며, 체계적 성분과 무작위 오차로 구성된다. 일원 분산분석(one-way ANOVA)은 범주형 설명 변수의 여러 수준에 걸쳐 평균의 동일성을 F 검정으로 판단하며, 총변동을 집단 간 변동과 오차 변동으로 분해한다. 가상 식이 연구에서 잡식·채식·완전 채식 집단의 콜레스테롤 평균 비교를 통해 ANOVA 표 구성과 F 비 계산을 시연한다. 집단 평균의 쌍별 비교에는 Bonferroni 보정 등 다중 비교 방법이 필요하며, 사전 계획된 비교만 수행해야 한다. 단순 선형 회귀는 하나의 양적 설명 변수와 양적 결과 변수 간의 직선 관계를 최소제곱법으로 추정한다. 회귀 계수(기울기)는 x가 1단위 증가할 때 y의 평균 변화량이며, 결정 계수(R²)는 설명된 변동의 비율을 나타낸다. 다중 회귀는 여러 설명 변수를 동시에 포함하여 교란 조정과 독립적 효과 평가를 가능하게 하며, 변수 선택 방법(전진, 후진, 단계적)을 논의한다. 모형 진단(잔차 분석, 정규성 검정, 등분산 검정, 영향 관측치 탐지)을 통해 모형의 적절성을 사후 검증하는 절차를 설명한다. 더미 변수를 사용하여 범주형 변수를 회귀 모형에 통합하는 일반 선형 모형(general linear model)을 소개하며, ANOVA와 회귀의 통합을 보인다. 공분산분석(ANCOVA)은 범주형과 양적 설명 변수를 함께 포함하여 교란 조정 후 집단 간 비교를 수행한다. 일반화 추정 방정식(GEE)과 같은 반복 측정 데이터 분석 방법도 간략히 소개한다.

### Ch 10: Modelling binary outcome data (pp. 371-430)

**핵심**: 이항 결과 데이터에 대한 로지스틱 회귀를 다룬다. 오즈비 추정, 교란과 상호작용의 모형화, 모형 적합도 평가, 조건부 로지스틱 회귀(매칭 데이터), 순서형/다항 로지스틱 회귀를 포함한다.

**키워드**: `logistic regression`, `odds ratio`, `conditional logistic`, `goodness of fit`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 10 (line 40570)
이항(binary) 결과 변수를 모형화할 때 표준 선형 회귀는 부적절한데, 위험-설명 변수 관계가 비선형이고, 예측값이 0-1 범위를 벗어날 수 있으며, 오차 분포가 정규가 아닌 이항 분포를 따르기 때문이다. 로지스틱 회귀는 질병의 로그 오즈(logit)를 설명 변수의 선형 함수로 모형화하여 이 세 문제를 동시에 해결한다. 로지스틱 함수는 S자 곡선 형태로 0과 1 사이의 점근선을 가지며, 최대가능도 추정(maximum likelihood estimation)으로 계수를 추정한다. 기울기 계수 b₁의 지수(exp(b₁))는 x가 1단위 증가할 때의 오즈비를 직접 나타내어 역학적 해석이 매우 편리하다. 이항, 양적, 범주형, 순서형 위험 요인 각각에 대한 로지스틱 회귀 계수의 해석 방법을 구체적 사례와 함께 설명한다. 다중 로지스틱 회귀를 통해 여러 위험 요인의 동시 효과를 평가하고, 교란 조정과 상호작용 검정을 수행할 수 있다. 모형 적합도 평가를 위해 우도비 검정(deviance), Hosmer-Lemeshow 검정, 잔차 분석 방법을 제시한다. 조건부 로지스틱 회귀는 매칭된 환자-대조군 데이터에 적합하며, 매칭 변수가 자동으로 통제된다. 순서형 로지스틱 회귀(proportional odds model)는 결과 변수가 세 수준 이상의 순서형일 때 적용하며, 비례 오즈 가정의 검정이 필요하다. 다항 로지스틱 회귀는 순서가 없는 다범주 결과 변수를 다루며, 기저 범주 대비 각 범주의 오즈비를 추정한다. EGAT 연구에서 흡연의 심혈관 사망 오즈비가 로지스틱 회귀로 2.808으로 추정되어 분할표 결과(2.81)와 일치함을 보인다.

### Ch 11: Modelling follow-up data (pp. 431-512)

**핵심**: 추적 데이터의 모형화를 다룬다. Cox 비례위험 모형, 시간 변동 공변량, 모형 진단, Poisson 회귀, 프레일티 모형(frailty model), 반복 사건, 다수준 생존 분석을 포함한다.

**키워드**: `Cox proportional hazards`, `Poisson regression`, `frailty model`, `time-varying covariate`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 11 (line 51093)
추적 데이터의 모형화는 중도절단(censoring)이 있거나 사건 발생까지의 시간 자체가 관심 결과 변수일 때 필요하다. 생존 함수 S(t)는 시간 t까지 사건 없이 생존할 확률이며, 위험 함수(hazard function) h(t)는 시간 t까지 생존한 조건에서 다음 순간 사건이 발생할 순간 확률이다. Kaplan-Meier 추정, 인-시간(person-time) 추정, 보험수리적(actuarial) 추정의 세 가지 방법으로 위험 함수를 추정할 수 있다. 지수(exponential) 분포는 일정한 위험률을 가정하며, Weibull 분포는 시간에 따라 위험률이 단조적으로 증가하거나 감소하는 것을 허용하는 모수적 모형이다. Cox 비례위험 모형은 위험 함수의 특정 분포를 가정하지 않는 준모수적(semiparametric) 접근으로, h(t) = h₀(t)·exp(βx)의 형태를 취한다. 비례위험 가정은 위험비(hazard ratio)가 시간에 걸쳐 일정하다는 것을 의미하며, 로그-로그 생존 곡선의 평행성 등으로 검정한다. 시간 변동 공변량(time-varying covariate)은 추적 중 변화하는 위험 요인(예: 흡연 상태 변화)을 모형에 통합할 수 있게 한다. Poisson 회귀는 인-시간 데이터에 적용되며, 사건 수가 Poisson 분포를 따른다고 가정하여 율비(rate ratio)를 추정한다. 프레일티 모형(frailty model)은 관측되지 않은 이질성을 무작위 효과로 포착하여 군집(cluster) 데이터나 반복 사건을 다룬다. 모형 진단(잔차 분석, Schoenfeld 잔차를 통한 비례위험 가정 검정)과 다수준 생존 분석의 개요를 제시한다. 교아세포종(glioblastoma) 환자의 생존 데이터를 사례로 위험 함수와 생존 함수 추정을 시연한다.

### Ch 12: Meta-analysis (pp. 513-556)

**핵심**: 메타분석의 원리와 방법을 다룬다. 효과 크기 결합, 고정/변량 효과 모형, 이질성 평가, 출판 편향, 메타회귀, 개인 수준 데이터 메타분석을 포함한다.

**키워드**: `meta-analysis`, `fixed effect`, `random effect`, `heterogeneity`, `publication bias`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 12 (line 56753)
메타분석은 여러 연구의 결과를 종합하여 노출-질병 관계의 일관성을 평가하고, 적절한 경우 개별 추정치를 하나의 요약 추정치로 결합하는 방법이다. 체계적 문헌 고찰(systematic review)은 전자 데이터베이스 검색, 회색 문헌(grey literature) 탐색, 사전 정의된 포함·배제 기준 적용을 통해 관련 연구를 객관적으로 수집한다. 연구 질(quality) 평가에서 내적 타당성(편향, 교란 통제)과 외적 타당성(일반화 가능성)을 구분하며, Cochrane Collaboration의 역할을 소개한다. 효과 크기 결합에는 역분산(inverse variance) 가중 평균을 사용하며, 이를 통해 최소 분산의 종합 추정치를 얻는다. 고정 효과(fixed effect) 모형은 모든 연구가 동일한 참값을 추정한다고 가정하는 반면, 변량 효과(random effects) 모형은 연구 간 이질성을 추가 분산 성분(τ²)으로 허용한다. 이질성(heterogeneity) 평가를 위해 Cochran의 Q 통계량과 I² 지표를 사용하며, I²는 총 변동 중 연구 간 변동의 비율을 나타낸다. 포레스트 플롯(forest plot)은 각 연구의 효과 추정치와 신뢰구간을 시각적으로 표현하며, 종합 추정치를 다이아몬드로 표시한다. 출판 편향(publication bias)은 유의한 결과를 가진 연구가 출판될 가능성이 높아 발생하며, 깔때기 도표(funnel plot)와 Egger 검정으로 탐지한다. 메타회귀(meta-regression)는 연구 수준의 공변량으로 이질성의 원인을 탐색하는 확장된 변량 효과 모형이다. 개인 수준 데이터(individual participant data) 메타분석은 원시 데이터를 통합하여 교란 조정과 하위 집단 분석의 정확성을 높인다. 손으로 말은 담배와 공장 제조 담배의 폐암 위험을 비교한 15개 연구의 메타분석 사례를 제시한다.

### Ch 13: Risk scores and clinical decision rules (pp. 557-600)

**핵심**: 통계 모형의 결과를 임상적으로 유용한 위험 점수와 의사결정 규칙으로 변환하는 방법을 다룬다. 판별 분석, ROC 곡선, 위험 예측 모형, 모형 검증을 포함한다.

**키워드**: `risk score`, `clinical decision rule`, `ROC curve`, `calibration`, `discrimination`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 13 (line 60058)
역학 데이터로부터 임상적으로 유용한 위험 점수(risk score)와 의사결정 규칙(clinical decision rule)을 개발하는 방법을 다룬다. 개인 수준 개입(약물 처방 등)과 인구 수준 개입(소금 저감 정책 등)의 차이를 설명하며, 대부분의 의료적 치료는 고위험군을 식별하여 개인 수준으로 적용해야 한다. 위험 요인과 질병 간의 통계적 연관성이 강하더라도 판별력(discrimination)이 반드시 우수한 것은 아님을 강조한다. 판별력은 질병 양성군과 음성군의 위험 요인 분포가 얼마나 잘 분리되는지를 나타내며, SHHEC 연구의 피브리노겐과 심혈관 질환 사례에서 이를 시연한다. 민감도(sensitivity)와 특이도(specificity)의 상충 관계를 다양한 임계값에서 평가하며, ROC 곡선(receiver operating characteristic curve)이 이를 시각적으로 요약한다. ROC 곡선 아래 면적(AUC, c-통계량)은 무작위로 선택한 환자와 비환자를 올바르게 순서 매길 확률로 해석되며, 0.5가 무작위, 1.0이 완벽한 판별이다. 다변량 위험 예측 모형은 Cox 회귀 또는 로지스틱 회귀에서 유도되며, Framingham 위험 점수 등이 대표적 사례이다. 모형 보정(calibration)은 예측된 위험과 관측된 위험의 일치도를 평가하며, Hosmer-Lemeshow 검정이나 보정 도표(calibration plot)를 사용한다. 내적 검증(교차 검증, 부트스트랩)과 외적 검증(독립 데이터셋)을 통해 모형의 과적합 여부를 확인해야 한다. 순 재분류 지수(NRI)와 통합 판별 개선(IDI)은 새로운 위험 요인 추가가 기존 모형의 예측력을 실질적으로 향상시키는지 평가하는 지표이다. 피브리노겐이 심혈관 질환의 유의한 예측 인자임에도 불구하고 기존 고전적 위험 요인에 추가했을 때 판별력 향상이 미미한 사례를 통해 연관성과 예측력의 구분을 명확히 한다.

### Ch 14: Computer-intensive methods (pp. 601-649)

**핵심**: 컴퓨터 집약적 방법을 다룬다. 부트스트랩, 순열 검정, 몬테카를로 시뮬레이션, EM 알고리즘, 다중 대체(multiple imputation), 베이즈 방법의 역학적 적용을 포함한다.

**키워드**: `bootstrap`, `permutation test`, `Monte Carlo`, `EM algorithm`, `Bayesian methods`

**상세**: → `Woodward, Mark - Epidemiology _ study design and data analysis-Chapman & Hall_CRC (2014).md` Ch 14 (line 66441)
컴퓨터 집약적 방법은 고전 통계의 수학적 제약을 극복하기 위해 현대 컴퓨터의 연산 능력을 활용하는 접근법이다. 부트스트랩(bootstrap)은 관측 데이터에서 복원 추출로 재표본을 수천 번 생성하여 추정량의 변동성과 신뢰구간을 구하는 방법이다. 부트스트랩 신뢰구간 구성에는 백분위수 방법, 편향 보정 가속(BCa) 방법 등이 있으며, 정규 분포 가정이 불필요하다는 장점이 있다. 중앙값, 두 평균의 비율, 심하게 편향된 변수의 평균 차이 등 폐쇄형 분산 공식이 없는 추정량에 특히 유용하다. 순열 검정(permutation test)은 귀무가설 하에서 데이터의 모든 가능한 재배열(또는 무작위 부분집합)을 생성하여 검정 통계량의 분포를 구성하는 비모수적 가설 검정법이다. 순열 검정은 분포 가정이 필요 없으며, 표본이 작거나 분포가 비정규일 때 정확한 p 값을 제공한다. 결측치(missing data) 문제를 완전 무작위 결측(MCAR), 무작위 결측(MAR), 비무작위 결측(MNAR)의 세 유형으로 분류한다. 단순 대체법(평균 대체, 회귀 대체)은 불확실성을 과소평가하는 반면, 다중 대체(multiple imputation)는 결측치를 여러 번 대체하여 대체의 불확실성을 반영한다. 다중 대체는 결측 데이터에 대한 m개의 완성된 데이터셋을 생성하고, 각각을 분석한 후 Rubin의 규칙으로 결과를 결합한다. EM 알고리즘은 불완전 데이터의 가능도를 최대화하기 위해 E 단계(기대)와 M 단계(최대화)를 반복하는 방법이다. 베이즈 방법은 사전 분포와 관측 데이터의 가능도를 결합하여 사후 분포를 구하며, MCMC(마르코프 연쇄 몬테카를로) 시뮬레이션을 통해 계산한다.
