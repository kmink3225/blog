---
name: "Statistical Inference, 2nd Edition"
type: book-summary
sources:
  - file: "Casella-StatisticalInference_azure_full.md"
    tool: Document Intelligence
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

집합론의 기초(합집합, 교집합, 여집합, 드모르간 법칙)에서 출발하여 표본공간(sample space)과 사건(event)의 개념을 정의한다. 확률의 세 가지 공리(비음수성, 정규화, 가산 가법성)를 제시하고, 이로부터 포함-배제 원리와 본페로니 부등식을 유도한다. 조건부 확률 P(A|B) = P(A∩B)/P(B)를 정의하고, 베이즈 정리와 전체확률 법칙을 증명한다. 독립성을 P(A∩B) = P(A)P(B)로 정의하고, 쌍별 독립과 상호 독립의 차이를 구분한다. 확률변수를 표본공간에서 실수로의 함수로 정의하고, 이산/연속 구분 없이 누적분포함수(CDF) F(x) = P(X≤x)를 통일적으로 다룬다. 밀도함수(PDF)와 확률질량함수(PMF)를 정의하고, CDF와의 관계를 정리한다. 이 장은 이후 모든 추론 이론의 확률론적 기초를 놓으며, 엄밀한 측도론적 기초보다는 직관적인 공리적 접근을 택한다.

---

### Ch 2: Transformations and Expectations (pp. 47-84)

**핵심**: 확률변수의 함수(변환)에 대한 분포를 구하는 기법과 기댓값의 성질을 다룬다. 변수 변환 정리, 기댓값, 적률(moment), 적률생성함수(MGF)를 정의하고, 적분 기호 아래서의 미분(Leibniz rule)을 다룬다.

**키워드**: `transformation`, `expected value`, `moments`, `MGF`, `Leibniz rule`, `variance`

**상세**: → `source_file` Ch 2 (line 6227)

확률변수의 함수(변환)에 대한 분포를 구하는 CDF 기법과 변수변환 정리(Jacobian을 이용한 밀도 변환)를 체계적으로 다룬다. 기댓값 E[g(X)] = ∫g(x)f(x)dx를 정의하고, 선형성을 증명한다. 적률(moment)을 정의하여 μ'_k = E[X^k]와 중심적률 μ_k = E[(X-μ)^k]를 구분한다. 분산 Var(X) = E[(X-μ)²] = E[X²] - (E[X])²를 유도하고 성질을 정리한다. 적률생성함수(MGF) M_X(t) = E[e^{tX}]를 정의하고, MGF가 존재하면 분포를 유일하게 결정함을 증명한다. MGF로부터 적률을 M^{(k)}(0) = E[X^k]로 구하는 방법을 시연한다. 적분 기호 아래서의 미분(Leibniz rule)을 엄밀하게 다루어, 모수에 대한 기댓값의 미분이 가능한 조건을 제시한다. 이 장은 이후 분포론과 추정론에 필수적인 변환과 기댓값 도구를 제공한다.

---

### Ch 3: Common Families of Distributions (pp. 85-138)

**핵심**: 통계에서 자주 사용되는 분포 가족을 체계적으로 정리한다. 이산분포(균등, 이항, 포아송, 음이항, 초기하), 연속분포(정규, 감마, 베타, 코시, 로그노멀), 지수족(exponential family), 위치-척도족, 확률 부등식(체비셰프, 젠센 등)을 다룬다.

**키워드**: `discrete uniform`, `binomial`, `Poisson`, `normal`, `gamma`, `beta`, `exponential family`, `location-scale family`, `Chebyshev inequality`, `Jensen inequality`

**상세**: → `source_file` Ch 3 (line 8539)

이산분포로 이산균등, 초기하, 이항, 포아송, 음이항, 기하분포를 다루고 각각의 PMF, 평균, 분산, MGF를 정리한다. 연속분포로 균등, 정규, 감마(지수, 카이제곱 포함), 베타, 코시, 로그노멀, 이중지수(라플라스) 분포를 다룬다. 지수족(exponential family)을 f(x|θ) = h(x)c(θ)exp(Ση_i(θ)T_i(x)) 형태로 정의하고, 대부분의 표준 분포가 지수족에 속함을 보인다. 곡선 지수족(curved exponential family)의 개념을 소개한다. 위치-척도족(location-scale family)을 f(x|μ,σ) = (1/σ)f₀((x-μ)/σ)로 정의하고, 정규/코시/이중지수가 위치-척도족임을 보인다. 확률 부등식으로 체비셰프 부등식 P(|X-μ|≥kσ) ≤ 1/k²과 젠센 부등식 E[g(X)] ≥ g(E[X])(볼록 g에 대해)를 증명한다. 이 장은 이후 추론에서 반복적으로 사용되는 분포 도구상자를 제공한다.

---

### Ch 4: Multiple Random Variables (pp. 139-206)

**핵심**: 다변량 확률 모형을 다룬다. 결합분포와 주변분포, 조건부분포와 독립성, 이변량 변환, 계층 모형과 혼합분포, 공분산과 상관, 다변량 분포(다변량 정규 포함), 수치적/함수적 부등식(코시-슈바르츠, 횔더 등)을 전개한다.

**키워드**: `joint distribution`, `marginal distribution`, `conditional distribution`, `independence`, `bivariate transformation`, `hierarchical model`, `mixture distribution`, `covariance`, `correlation`, `multivariate normal`, `Cauchy-Schwarz inequality`

**상세**: → `source_file` Ch 4 (line 11644)

결합분포를 결합CDF와 결합밀도/질량함수로 정의하고, 주변분포를 적분(합산)으로 구하는 방법을 제시한다. 조건부분포 f(y|x) = f(x,y)/f_X(x)를 정의하고, 독립성을 f(x,y)=f_X(x)f_Y(y)로 특성화한다. 이변량 변환의 야코비안 기법을 다루어, (X,Y)→(U,V) 변환에서 f_{U,V} = f_{X,Y}|J^{-1}|을 유도한다. 계층 모형(hierarchical model) X|Y~f(x|y), Y~f(y)을 소개하고, 이로부터 혼합분포(mixture distribution) f(x) = ∫f(x|y)f(y)dy를 유도한다. 공분산 Cov(X,Y)와 상관계수 ρ를 정의하고, 독립이면 비상관이지만 역은 성립하지 않음을 보인다. 조건부기댓값의 성질(전체기댓값 법칙 E[X]=E[E[X|Y]], 조건부분산 공식)을 증명한다. 다변량 정규분포를 정의하고 그 조건부/주변분포의 정규성을 증명한다. 수치적/함수적 부등식으로 코시-슈바르츠, 횔더, 민코프스키 부등식을 제시하고, 젠센 부등식의 확률론적 버전을 증명한다.

---

### Ch 5: Properties of a Random Sample (pp. 207-270)

**핵심**: 랜덤 표본의 성질을 다룬다. iid 정의, 표본 평균과 분산의 분포, 정규모집단에서의 표본분포(카이제곱, t, F), 순서통계량, 수렴 개념(확률수렴, 거의 확실한 수렴, 분포수렴), 델타 방법, 난수 생성(역변환법, 기각법)을 다룬다.

**키워드**: `random sample`, `iid`, `sample mean`, `sample variance`, `chi-squared`, `Student's t`, `Snedecor's F`, `order statistics`, `convergence in probability`, `convergence in distribution`, `delta method`, `CLT`, `accept/reject algorithm`

**상세**: → `source_file` Ch 5 (line 15834)

iid(독립 동일 분포) 랜덤 표본을 정의하고, 표본평균 X̄과 표본분산 S²의 분포를 유도한다. 정규모집단에서 X̄~N(μ,σ²/n), (n-1)S²/σ²~χ²(n-1), X̄과 S²의 독립성을 증명한다. 카이제곱, 스튜던트 t, 스네데커 F 분포를 정의하고 각각의 밀도함수와 적률을 유도한다. 순서통계량(order statistics) X_{(1)}≤...≤X_{(n)}의 결합밀도를 유도하고, 최소값/최대값/중간값의 분포를 구한다. 확률수렴(convergence in probability), 거의 확실한 수렴(a.s. convergence), 분포수렴(convergence in distribution)의 세 가지 수렴 개념을 정의하고 관계를 정리한다. 약대수법칙(WLLN)과 중심극한정리(CLT)를 증명하고, 델타 방법(delta method)으로 g(X̄)의 점근 분포를 N(g(μ), (g'(μ))²σ²/n)으로 근사한다. 난수 생성(random number generation)의 기초로 역변환법(inverse transform method)과 기각법(accept-reject algorithm)을 소개한다.

---

### Ch 6: Principles of Data Reduction (pp. 271-310)

**핵심**: 데이터 축소의 원리를 다룬다. 충분통계량(sufficiency), 인수분해 정리(factorization theorem), 최소충분통계량, 보조통계량(ancillary), 완비통계량(completeness), 우도원리(likelihood principle), 형식적 우도(formal likelihood)를 다룬다.

**키워드**: `sufficient statistic`, `factorization theorem`, `minimal sufficiency`, `ancillary statistic`, `completeness`, `Basu's theorem`, `likelihood principle`, `likelihood function`

**상세**: → `source_file` Ch 6 (line 19601)

충분통계량(sufficient statistic)을 조건부분포 f(x|T,θ)가 θ에 의존하지 않는 통계량 T(X)로 정의한다. 인수분해 정리(factorization theorem)를 증명하여, T가 충분통계량일 필요충분조건이 f(x|θ)=g(T(x)|θ)h(x)로 인수분해되는 것임을 보인다. 지수족에서 자연 충분통계량이 자동으로 충분함을 보인다. 최소충분통계량(minimal sufficient statistic)을 정의하고, 우도비 판별법 f(x|θ)/f(y|θ)가 θ에 무관한 조건으로 최소충분을 판정하는 방법을 제시한다. 보조통계량(ancillary statistic)을 분포가 θ에 의존하지 않는 통계량으로 정의한다. 완비통계량(complete statistic)을 E_θ[g(T)]=0 ∀θ이면 P(g(T)=0)=1인 통계량으로 정의하고, 바수 정리(Basu's theorem)로 완비 충분통계량과 보조통계량의 독립성을 증명한다. 우도원리(likelihood principle)를 정의하고, 충분성 원리와 조건화 원리로부터 우도원리가 도출됨을 논증한다.

---

### Ch 7: Point Estimation (pp. 311-372)

**핵심**: 점추정의 방법과 평가를 다룬다. 추정량 탐색 방법(적률법, MLE, 베이즈 추정)과 평가 기준(MSE, 비편향성, UMVUE, 크래머-라오 하한, 충분성과 비편향성의 결합인 라오-블랙웰 정리, EM 알고리즘)을 전개한다.

**키워드**: `method of moments`, `MLE`, `maximum likelihood`, `Bayes estimator`, `MSE`, `unbiased`, `UMVUE`, `Cramer-Rao lower bound`, `Rao-Blackwell theorem`, `Lehmann-Scheffe theorem`, `EM algorithm`

**상세**: → `source_file` Ch 7 (line 22117)

점추정의 방법으로 적률법(method of moments)과 최대우도추정법(MLE)을 소개한다. MLE의 불변성 원리(invariance principle)를 증명하여 τ(θ)의 MLE가 τ(θ̂)임을 보인다. 베이즈 추정을 사후분포의 기댓값(또는 최빈값, 중위수)로 정의하고, 사전분포의 역할을 논의한다. EM 알고리즘을 불완전 자료에서의 MLE 계산 방법으로 소개하고, E-step과 M-step을 정의한다. 평균제곱오차(MSE) = 분산 + 편향²로 추정량을 평가하고, 비편향성(unbiasedness)의 장단점을 논의한다. 라오-블랙웰 정리(Rao-Blackwell theorem)를 증명하여, 비편향 추정량을 충분통계량에 조건화하면 MSE가 개선됨을 보인다. 크래머-라오 하한(CRLR) Var(T) ≥ (τ'(θ))²/I(θ)를 유도하고, 정보부등식에서 등호 조건을 제시한다. 레만-쉐페 정리(Lehmann-Scheffe theorem)로 완비 충분통계량의 함수인 비편향 추정량이 UMVUE(균일 최소분산 비편향 추정량)임을 증명한다.

---

### Ch 8: Hypothesis Testing (pp. 373-416)

**핵심**: 가설검정의 방법과 평가를 다룬다. 우도비 검정(LRT), 네이만-피어슨 보조정리(가장 강력한 검정), 단조 우도비를 이용한 UMP 검정, p-value의 정의와 해석, 검정력 함수, 두 종류의 오류(Type I/II)와 그 관계를 다룬다.

**키워드**: `likelihood ratio test`, `Neyman-Pearson lemma`, `UMP test`, `power function`, `p-value`, `Type I error`, `Type II error`, `significance level`, `size`, `monotone likelihood ratio`

**상세**: → `source_file` Ch 8 (line 25933)

가설검정의 기본 구조를 귀무가설 H₀과 대립가설 H₁, 기각역(rejection region), 검정통계량으로 정의한다. 제1종 오류(α, 크기)와 제2종 오류(β)를 정의하고, 검정력 함수 β(θ) = P_θ(X∈R)를 도입한다. 우도비 검정(LRT) λ(x) = sup_{θ∈Θ₀}L(θ)/sup_{θ∈Θ}L(θ)을 정의하고, 기각역 {λ(x)≤c}를 설정한다. 네이만-피어슨 보조정리(Neyman-Pearson lemma)를 증명하여, 단순가설 대 단순가설 검정에서 우도비 검정이 주어진 크기에서 가장 강력한(most powerful) 검정임을 보인다. 단조 우도비(monotone likelihood ratio) 성질을 이용하여 일방향 대립가설에 대한 UMP(균일 최강력) 검정을 구성하는 방법을 제시한다. 양방향 검정에서 UMP 검정이 일반적으로 존재하지 않음을 보이고, 비편향 검정(unbiased test)의 개념을 도입한다. p-value를 P_θ₀(T(X)≥T(x_obs))로 정의하고, p-value가 H₀ 하에서 U(0,1) 분포를 따름을 증명한다. 정규분포에서의 t-검정, F-검정을 체계적으로 유도한다.

---

### Ch 9: Interval Estimation (pp. 417-460)

**핵심**: 구간추정의 방법과 평가를 다룬다. 피벗(pivot) 방법, 우도비 기반 구간, 베이즈 구간, 신뢰구간의 최적성(최단 길이, 비편향 구간), 피벗팅에 의한 구간 구성, 신뢰 영역의 구성과 평가를 전개한다.

**키워드**: `confidence interval`, `pivot`, `coverage probability`, `confidence coefficient`, `inverting a test`, `Bayesian interval`, `credible set`, `shortest length`, `unbiased interval`

**상세**: → `source_file` Ch 9 (line 28697)

신뢰구간(confidence interval)의 정의를 피복확률(coverage probability) P_θ(θ∈C(X)) ≥ 1-α로 제시한다. 피벗(pivot) Q(X,θ)의 분포가 θ에 무관한 경우, Q를 이용한 구간 구성법을 설명한다. 정규분포에서 μ의 t-구간, σ²의 카이제곱 구간을 유도한다. 검정의 역전(inverting a test)에 의한 신뢰구간 구성법을 제시하고, UMP 검정의 역전이 최적 구간을 줌을 보인다. 우도비 기반 구간을 {θ: λ(θ)>c}로 정의한다. 베이즈 구간(credible set)을 사후분포의 구간으로 정의하고, HPD(highest posterior density) 영역을 소개한다. 구간의 최적성 평가로 최단 기대 길이(expected length)와 비편향 구간(unbiased interval)의 개념을 다룬다. 피벗팅(pivoting)에 의한 구간 구성의 일반적 절차를 정리한다. 신뢰 영역(confidence region)을 다변량 모수로 확장하고, F-분포 기반 타원형 영역을 유도한다. 대표본 근사 구간으로 MLE ± z_{α/2}·SE를 제시한다.

---

### Ch 10: Asymptotic Evaluations (pp. 461-524)

**핵심**: 점근(대표본) 이론을 다룬다. 일치성(consistency), MLE의 점근 정규성과 점근 효율, 점근 가설검정(왈드, 스코어, LRT의 점근 동치성), 부트스트랩, M-추정(로버스트 추정), 점근 구간추정을 전개한다. 이 챕터는 2판에서 크게 확장된 부분이다.

**키워드**: `consistency`, `asymptotic normality`, `asymptotic efficiency`, `Wald test`, `score test`, `asymptotic LRT`, `bootstrap`, `M-estimation`, `robust estimation`, `asymptotic confidence interval`

**상세**: → `source_file` Ch 10 (line 31797)

일치성(consistency)을 P_θ(|T_n-θ|>ε)→0으로 정의하고, MLE의 일치성을 정규 조건 하에서 증명한다. MLE의 점근 정규성 √n(θ̂-θ₀) →_d N(0, 1/I(θ₀))을 증명하고, 이것이 점근 크래머-라오 하한을 달성함을 보인다. MLE의 점근 효율(asymptotic efficiency)을 정의하고, MLE가 점근적으로 최소분산임을 논의한다. 점근 가설검정 방법으로 왈드 검정(Wald test) W=(θ̂-θ₀)²I(θ̂), 스코어 검정(score test, Rao test) S=s(θ₀)²/I(θ₀), 점근 우도비 검정(LRT) -2logλ를 소개하고, 세 검정의 점근 동치성(모두 χ² 분포로 수렴)을 증명한다. 부트스트랩(bootstrap)을 비모수적 분산 추정과 신뢰구간 구성 방법으로 소개한다. M-추정(M-estimation)을 Σρ(x_i,θ) 최소화로 정의하고, 로버스트 추정(robust estimation)의 기초로서 영향함수(influence function)를 다룬다. 점근 구간추정으로 MLE 기반 구간과 부트스트랩 구간을 제시한다. 이 장은 2판에서 크게 확장된 부분으로, 현대 통계학의 대표본 이론 핵심을 담고 있다.

---

### Ch 11: Analysis of Variance and Regression (pp. 525-566)

**핵심**: 일원 분산분석(one-way ANOVA)과 단순 선형회귀를 다룬다. 선형 모형의 기본 가정, 변동의 분해(SST = SSB + SSW), F-검정, 회귀에서의 최소제곱 추정, 적합도 검정, 잔차 분석을 전개한다.

**키워드**: `ANOVA`, `one-way ANOVA`, `F-test`, `linear model`, `sum of squares`, `simple linear regression`, `least squares`, `coefficient of determination`, `residual analysis`

**상세**: → `source_file` Ch 11 (line 35327)

일원 분산분석(one-way ANOVA)의 선형모형 X_{ij} = μ + α_i + ε_{ij}을 정의하고, 전체평균과 처리효과의 개념을 도입한다. 총변동을 처리간 변동(SSB)과 처리내 변동(SSW)으로 분해하여 SST = SSB + SSW를 유도한다. H₀: α₁=...=α_k=0 검정을 위한 F-통계량 F = (SSB/(k-1))/(SSW/(n-k))를 구성하고, H₀ 하에서 F~F(k-1,n-k)임을 증명한다. 단순 선형회귀 모형 Y_i = β₀ + β₁x_i + ε_i에서 최소제곱 추정량 β̂₁ = Σ(x_i-x̄)(Y_i-Ȳ)/Σ(x_i-x̄)²와 β̂₀ = Ȳ - β̂₁x̄를 유도한다. 결정계수(coefficient of determination) R² = SSR/SST의 의미를 설명한다. 적합도 검정(goodness-of-fit test)을 잔차 분석으로 다루고, 잔차의 정규성/등분산성/독립성 가정을 점검하는 방법을 설명한다. 분산분석과 회귀분석의 통합적 관점을 행렬 표현 Y = Xβ + ε로 제시하고, 사영행렬 H = X(X^T X)^{-1}X^T의 역할을 설명한다.

---

### Ch 12: Regression Models (pp. 567-620)

**핵심**: 11장의 선형 모형을 확장한다. 측정오차가 있는 회귀(errors in variables), 로지스틱 회귀(일반화 선형 모형의 일종), 로버스트 회귀(M-추정 기반)를 다룬다. 로지스틱 회귀에서 로짓 변환, 최대우도 추정, 반복가중최소제곱(IRLS)을 전개한다.

**키워드**: `errors in variables`, `logistic regression`, `logit transformation`, `generalized linear model`, `robust regression`, `M-estimation`, `IRLS`, `influence function`

**상세**: → `source_file` Ch 12 (line 38942)

측정오차가 있는 회귀(errors in variables) 모형을 다루어, 독립변수에도 오차가 있을 때 통상 최소제곱 추정량의 편향(attenuation bias)을 보인다. 구조적 모형과 기능적 모형을 구분하고, 도구변수(instrumental variables) 등의 대안 추정법을 논의한다. 로지스틱 회귀를 일반화 선형 모형(GLM)의 대표적 예로 소개하고, 로짓 변환 log(p/(1-p)) = x^T β를 정의한다. 로지스틱 회귀의 MLE를 뉴턴-랩슨법으로 구하는 과정을 유도하고, 반복가중최소제곱(IRLS) 알고리즘을 제시한다. 로지스틱 회귀에서의 왈드 검정과 우도비 검정을 다룬다. 로버스트 회귀(robust regression)를 M-추정 기반으로 소개하고, 잔차에 대한 손실함수 ρ를 최소화하는 추정량을 정의한다. 후버(Huber) 함수와 이중제곱(bisquare) 함수를 대표적 ρ 함수로 제시한다. 영향함수(influence function)를 추정량의 로버스트성 지표로 도입하고, 최소제곱 추정량의 무계한 영향함수가 이상치에 취약함을 보인다. 이 장은 11장의 선형모형을 비표준적 상황으로 확장하여 실전적 회귀분석의 폭을 넓힌다.
