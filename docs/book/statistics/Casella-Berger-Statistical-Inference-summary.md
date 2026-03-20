---
name: "Statistical Inference, 2nd Edition"
type: book-summary
source_file: "George Casella&Roger L.Berger--Statistical Inference_2nd_Edition (1).md"
authors: "George Casella, Roger L. Berger"
year: 2002
total_pages: 660
language: en
keywords: [probability, inference, estimation, hypothesis-testing, confidence-interval, sufficiency, likelihood, asymptotic, ANOVA, regression, MLE, exponential-family]
---

# Statistical Inference (2nd Edition) — Summary

> George Casella & Roger L. Berger (2002), 660 pages, 12 chapters
> 수리통계학의 바이블. 확률론 기초부터 추정, 검정, 점근이론, 회귀까지 체계적으로 다룬다.

## Contents

### Part I: Probability and Distributions (Ch 1-4)
- Ch 1: Probability Theory (p.1)
- Ch 2: Transformations and Expectations (p.47)
- Ch 3: Common Families of Distributions (p.85)
- Ch 4: Multiple Random Variables (p.139)

### Part II: Sampling and Data Reduction (Ch 5-6)
- Ch 5: Properties of a Random Sample (p.207)
- Ch 6: Principles of Data Reduction (p.271)

### Part III: Inference (Ch 7-9)
- Ch 7: Point Estimation (p.311)
- Ch 8: Hypothesis Testing (p.373)
- Ch 9: Interval Estimation (p.417)

### Part IV: Advanced Topics (Ch 10-12)
- Ch 10: Asymptotic Evaluations (p.461)
- Ch 11: Analysis of Variance and Regression (p.525)
- Ch 12: Regression Models (p.567)

---

## Chapter Summaries

### Ch 1: Probability Theory (pp. 1-46)

**핵심**: 통계학의 토대인 확률론의 기초를 다룬다. 집합론에서 출발하여 표본공간, 사건, 확률의 공리적 기초를 정의하고, 조건부 확률, 독립성, 확률변수, 분포함수, 밀도/질량 함수를 체계적으로 전개한다.

**키워드**: `sample space`, `event`, `axioms of probability`, `conditional probability`, `independence`, `random variable`, `CDF`, `PDF`, `PMF`

**상세**: → `source_file` Ch 1 (line 3311)

---

### Ch 2: Transformations and Expectations (pp. 47-84)

**핵심**: 확률변수의 함수(변환)에 대한 분포를 구하는 기법과 기댓값의 성질을 다룬다. 변수 변환 정리, 기댓값, 적률(moment), 적률생성함수(MGF)를 정의하고, 적분 기호 아래서의 미분(Leibniz rule)을 다룬다.

**키워드**: `transformation`, `expected value`, `moments`, `MGF`, `Leibniz rule`, `variance`

**상세**: → `source_file` Ch 2 (line 6227)

---

### Ch 3: Common Families of Distributions (pp. 85-138)

**핵심**: 통계에서 자주 사용되는 분포 가족을 체계적으로 정리한다. 이산분포(균등, 이항, 포아송, 음이항, 초기하), 연속분포(정규, 감마, 베타, 코시, 로그노멀), 지수족(exponential family), 위치-척도족, 확률 부등식(체비셰프, 젠센 등)을 다룬다.

**키워드**: `discrete uniform`, `binomial`, `Poisson`, `normal`, `gamma`, `beta`, `exponential family`, `location-scale family`, `Chebyshev inequality`, `Jensen inequality`

**상세**: → `source_file` Ch 3 (line 8539)

---

### Ch 4: Multiple Random Variables (pp. 139-206)

**핵심**: 다변량 확률 모형을 다룬다. 결합분포와 주변분포, 조건부분포와 독립성, 이변량 변환, 계층 모형과 혼합분포, 공분산과 상관, 다변량 분포(다변량 정규 포함), 수치적/함수적 부등식(코시-슈바르츠, 횔더 등)을 전개한다.

**키워드**: `joint distribution`, `marginal distribution`, `conditional distribution`, `independence`, `bivariate transformation`, `hierarchical model`, `mixture distribution`, `covariance`, `correlation`, `multivariate normal`, `Cauchy-Schwarz inequality`

**상세**: → `source_file` Ch 4 (line 11644)

---

### Ch 5: Properties of a Random Sample (pp. 207-270)

**핵심**: 랜덤 표본의 성질을 다룬다. iid 정의, 표본 평균과 분산의 분포, 정규모집단에서의 표본분포(카이제곱, t, F), 순서통계량, 수렴 개념(확률수렴, 거의 확실한 수렴, 분포수렴), 델타 방법, 난수 생성(역변환법, 기각법)을 다룬다.

**키워드**: `random sample`, `iid`, `sample mean`, `sample variance`, `chi-squared`, `Student's t`, `Snedecor's F`, `order statistics`, `convergence in probability`, `convergence in distribution`, `delta method`, `CLT`, `accept/reject algorithm`

**상세**: → `source_file` Ch 5 (line 15834)

---

### Ch 6: Principles of Data Reduction (pp. 271-310)

**핵심**: 데이터 축소의 원리를 다룬다. 충분통계량(sufficiency), 인수분해 정리(factorization theorem), 최소충분통계량, 보조통계량(ancillary), 완비통계량(completeness), 우도원리(likelihood principle), 형식적 우도(formal likelihood)를 다룬다.

**키워드**: `sufficient statistic`, `factorization theorem`, `minimal sufficiency`, `ancillary statistic`, `completeness`, `Basu's theorem`, `likelihood principle`, `likelihood function`

**상세**: → `source_file` Ch 6 (line 19601)

---

### Ch 7: Point Estimation (pp. 311-372)

**핵심**: 점추정의 방법과 평가를 다룬다. 추정량 탐색 방법(적률법, MLE, 베이즈 추정)과 평가 기준(MSE, 비편향성, UMVUE, 크래머-라오 하한, 충분성과 비편향성의 결합인 라오-블랙웰 정리, EM 알고리즘)을 전개한다.

**키워드**: `method of moments`, `MLE`, `maximum likelihood`, `Bayes estimator`, `MSE`, `unbiased`, `UMVUE`, `Cramer-Rao lower bound`, `Rao-Blackwell theorem`, `Lehmann-Scheffe theorem`, `EM algorithm`

**상세**: → `source_file` Ch 7 (line 22117)

---

### Ch 8: Hypothesis Testing (pp. 373-416)

**핵심**: 가설검정의 방법과 평가를 다룬다. 우도비 검정(LRT), 네이만-피어슨 보조정리(가장 강력한 검정), 단조 우도비를 이용한 UMP 검정, p-value의 정의와 해석, 검정력 함수, 두 종류의 오류(Type I/II)와 그 관계를 다룬다.

**키워드**: `likelihood ratio test`, `Neyman-Pearson lemma`, `UMP test`, `power function`, `p-value`, `Type I error`, `Type II error`, `significance level`, `size`, `monotone likelihood ratio`

**상세**: → `source_file` Ch 8 (line 25933)

---

### Ch 9: Interval Estimation (pp. 417-460)

**핵심**: 구간추정의 방법과 평가를 다룬다. 피벗(pivot) 방법, 우도비 기반 구간, 베이즈 구간, 신뢰구간의 최적성(최단 길이, 비편향 구간), 피벗팅에 의한 구간 구성, 신뢰 영역의 구성과 평가를 전개한다.

**키워드**: `confidence interval`, `pivot`, `coverage probability`, `confidence coefficient`, `inverting a test`, `Bayesian interval`, `credible set`, `shortest length`, `unbiased interval`

**상세**: → `source_file` Ch 9 (line 28697)

---

### Ch 10: Asymptotic Evaluations (pp. 461-524)

**핵심**: 점근(대표본) 이론을 다룬다. 일치성(consistency), MLE의 점근 정규성과 점근 효율, 점근 가설검정(왈드, 스코어, LRT의 점근 동치성), 부트스트랩, M-추정(로버스트 추정), 점근 구간추정을 전개한다. 이 챕터는 2판에서 크게 확장된 부분이다.

**키워드**: `consistency`, `asymptotic normality`, `asymptotic efficiency`, `Wald test`, `score test`, `asymptotic LRT`, `bootstrap`, `M-estimation`, `robust estimation`, `asymptotic confidence interval`

**상세**: → `source_file` Ch 10 (line 31797)

---

### Ch 11: Analysis of Variance and Regression (pp. 525-566)

**핵심**: 일원 분산분석(one-way ANOVA)과 단순 선형회귀를 다룬다. 선형 모형의 기본 가정, 변동의 분해(SST = SSB + SSW), F-검정, 회귀에서의 최소제곱 추정, 적합도 검정, 잔차 분석을 전개한다.

**키워드**: `ANOVA`, `one-way ANOVA`, `F-test`, `linear model`, `sum of squares`, `simple linear regression`, `least squares`, `coefficient of determination`, `residual analysis`

**상세**: → `source_file` Ch 11 (line 35327)

---

### Ch 12: Regression Models (pp. 567-620)

**핵심**: 11장의 선형 모형을 확장한다. 측정오차가 있는 회귀(errors in variables), 로지스틱 회귀(일반화 선형 모형의 일종), 로버스트 회귀(M-추정 기반)를 다룬다. 로지스틱 회귀에서 로짓 변환, 최대우도 추정, 반복가중최소제곱(IRLS)을 전개한다.

**키워드**: `errors in variables`, `logistic regression`, `logit transformation`, `generalized linear model`, `robust regression`, `M-estimation`, `IRLS`, `influence function`

**상세**: → `source_file` Ch 12 (line 38942)
