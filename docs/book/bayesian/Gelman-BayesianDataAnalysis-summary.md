---
name: "Bayesian Data Analysis (3rd Edition)"
type: book-summary
source_file: "Gelman et al. - Bayesian Data Analysis (3rd Ed.).md"
authors: "Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari, Donald B. Rubin"
year: 2013
total_pages: 661
language: en
keywords: [bayesian-inference, hierarchical-models, MCMC, regression, model-checking, decision-analysis, nonparametric, Hamiltonian-Monte-Carlo, Stan, Gaussian-process]
---

# Bayesian Data Analysis (3rd Edition) — Summary

> Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari, Donald B. Rubin (2013), 661 pages, 23 chapters + 3 appendices
> 베이즈 추론의 기초부터 고급 계산법, 회귀 모델, 비모수 모델까지 포괄하는 대학원 수준의 베이즈 통계학 교과서이다.

## Contents

**Part I: Fundamentals of Bayesian Inference (pp. 1-137)**
- Ch 1. Probability and inference (pp. 3-27)
- Ch 2. Single-parameter models (pp. 29-57)
- Ch 3. Introduction to multiparameter models (pp. 63-79)
- Ch 4. Asymptotics and connections to non-Bayesian approaches (pp. 83-98)
- Ch 5. Hierarchical models (pp. 101-134)

**Part II: Fundamentals of Bayesian Data Analysis (pp. 139-257)**
- Ch 6. Model checking (pp. 141-163)
- Ch 7. Evaluating, comparing, and expanding models (pp. 165-194)
- Ch 8. Modeling accounting for data collection (pp. 197-230)
- Ch 9. Decision analysis (pp. 237-257)

**Part III: Advanced Computation (pp. 259-349)**
- Ch 10. Introduction to Bayesian computation (pp. 261-272)
- Ch 11. Basics of Markov chain simulation (pp. 275-291)
- Ch 12. Computationally efficient Markov chain simulation (pp. 293-309)
- Ch 13. Modal and distributional approximations (pp. 311-349)

**Part IV: Regression Models (pp. 351-467)**
- Ch 14. Introduction to regression models (pp. 353-378)
- Ch 15. Hierarchical linear models (pp. 381-402)
- Ch 16. Generalized linear models (pp. 405-432)
- Ch 17. Models for robust inference (pp. 435-446)
- Ch 18. Models for missing data (pp. 449-467)

**Part V: Nonlinear and Nonparametric Models (pp. 469-573)**
- Ch 19. Parametric nonlinear models (pp. 471-486)
- Ch 20. Basis function models (pp. 487-498)
- Ch 21. Gaussian process models (pp. 501-516)
- Ch 22. Finite mixture models (pp. 519-543)
- Ch 23. Dirichlet process models (pp. 545-573)

**Appendixes (pp. 575-608)**
- A. Standard probability distributions (pp. 577-586)
- B. Outline of proofs of limit theorems (pp. 587-590)
- C. Computation in R and Stan (pp. 591-608)

---

## Chapter Summaries

### Ch 1: Probability and inference (pp. 3-27)

**핵심**: 베이즈 데이터 분석의 세 단계(확률 모델 설정, 사후분포 계산, 모델 적합도 평가)를 정의한다. 확률 표기법, 베이즈 추론의 기본 구조, 유전학·맞춤법 검사·미식축구 포인트 스프레드·레코드 링키지 등의 이산 예제를 통해 불확실성의 확률적 표현을 설명한다.

**키워드**: `bayesian-data-analysis`, `posterior-distribution`, `conditional-probability`, `prior`, `likelihood`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 1 (line 1256)

### Ch 2: Single-parameter models (pp. 29-57)

**핵심**: 이항·정규·포아송·지수 분포의 단일 파라미터 모델을 다룬다. 사전분포와 데이터 간의 타협으로서의 사후분포, 켤레 사전분포, 정보적/비정보적/약정보적 사전분포를 소개하고, 암 발생률 추정 예제를 제시한다.

**키워드**: `single-parameter`, `conjugate-prior`, `binomial`, `noninformative-prior`, `weakly-informative-prior`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 2 (line 3149)

### Ch 3: Introduction to multiparameter models (pp. 63-79)

**핵심**: 다중 파라미터 문제에서 귀찮은 파라미터(nuisance parameter)를 주변화하여 관심 파라미터의 사후분포를 얻는 방법을 설명한다. 정규 분포(미지 평균·분산), 다항 분포, 다변량 정규 분포 모델을 다루고, 생물학적 검정 실험의 비켤레 로지스틱 회귀를 격자 계산으로 분석한다.

**키워드**: `multiparameter`, `nuisance-parameter`, `marginalization`, `multinomial`, `bioassay`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 3 (line 5609)

### Ch 4: Asymptotics and connections to non-Bayesian approaches (pp. 83-98)

**핵심**: 사후분포의 정규 근사와 대표본 이론을 다루어 베이즈 방법과 빈도주의 방법 간의 연결을 설명한다. 대표본 정리의 반례들을 제시하고, 베이즈 추론의 빈도주의적 평가와 다른 통계적 방법에 대한 베이즈적 해석을 논의한다.

**키워드**: `asymptotic-theory`, `normal-approximation`, `frequentist-connection`, `large-sample`, `consistency`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 4 (line 7011)

### Ch 5: Hierarchical models (pp. 101-134)

**핵심**: 교환 가능성(exchangeability)에 기반한 계층적 모델링을 소개한다. 그룹 파라미터가 공통 모집단 분포에서 추출된 것으로 보는 구조를 설정하고, 8개 학교(eight schools) 실험과 메타분석 예제를 통해 수축(shrinkage) 추정의 원리와 분산 파라미터에 대한 약정보적 사전분포를 다룬다.

**키워드**: `hierarchical-model`, `exchangeability`, `eight-schools`, `shrinkage`, `hyperparameter`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 5 (line 8226)

### Ch 6: Model checking (pp. 141-163)

**핵심**: 적용된 베이즈 분석에서 모델 점검의 중요성을 강조한다. 사후 예측 점검(posterior predictive check)의 개념과 시각적 방법, 검정 통계량을 이용한 모형 적합도 평가를 설명하고, 교육 테스트 예제로 실제 적용을 보여준다.

**키워드**: `model-checking`, `posterior-predictive-check`, `sensitivity-analysis`, `p-value`, `discrepancy`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 6 (line 11389)

### Ch 7: Evaluating, comparing, and expanding models (pp. 165-194)

**핵심**: 예측 정확도 측정, 정보 기준(AIC, DIC, WAIC), 교차 검증을 통한 모델 비교를 다룬다. 베이즈 팩터에 의한 모델 선택, 연속적 모델 확장, 대통령 선거 예측 회귀를 예시로 사용하며, 과적합 보정 방법을 설명한다.

**키워드**: `model-comparison`, `cross-validation`, `information-criteria`, `WAIC`, `bayes-factor`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 7 (line 13331)

### Ch 8: Modeling accounting for data collection (pp. 197-230)

**핵심**: 표본 조사, 설계 실험, 관찰 연구에서 데이터 수집 과정을 확률 모델에 반영하는 방법을 다룬다. 무시가능성(ignorability) 조건, 층화·군집 표본, 무작위 배치, 절단·결측 데이터의 처리를 베이즈적 관점에서 설명한다.

**키워드**: `data-collection`, `ignorability`, `survey-sampling`, `stratification`, `censoring`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 8 (line 15580)

### Ch 9: Decision analysis (pp. 237-257)

**핵심**: 불확실성 하에서의 의사결정 이론을 소개한다. 설문 인센티브의 계층적 회귀 분석, 암 진단 의료 검진의 다단계 의사결정, 가정용 라돈 측정의 계층적 결정 분석을 예제로 사용하며, 개인적 vs 제도적 결정 분석을 구분한다.

**키워드**: `decision-analysis`, `utility`, `survey-incentive`, `medical-screening`, `radon`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 9 (line 18874)

### Ch 10: Introduction to Bayesian computation (pp. 261-272)

**핵심**: 사후분포와 사후 예측 분포의 계산을 위한 기본 방법들을 소개한다. 수치 적분, 분포 근사, 직접 시뮬레이션과 기각 표본추출, 중요도 표본추출을 다루고, 필요한 시뮬레이션 횟수 및 디버깅 전략을 설명한다.

**키워드**: `numerical-integration`, `rejection-sampling`, `importance-sampling`, `simulation`, `computing-environment`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 10 (line 20671)

### Ch 11: Basics of Markov chain simulation (pp. 275-291)

**핵심**: 마르코프 체인 몬테 카를로(MCMC)의 기본 알고리즘인 깁스 표본추출기(Gibbs sampler)와 메트로폴리스-헤이스팅스 알고리즘을 소개한다. 수렴 진단, 유효 표본 크기 계산, 다중 체인을 이용한 추론 방법을 설명하고, 계층적 정규 모델 예제를 제시한다.

**키워드**: `MCMC`, `Gibbs-sampler`, `Metropolis-Hastings`, `convergence`, `effective-sample-size`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 11 (line 21552)

### Ch 12: Computationally efficient Markov chain simulation (pp. 293-309)

**핵심**: 깁스와 메트로폴리스의 효율성을 높이는 재매개변수화, 튜닝 전략을 다룬다. 해밀턴 몬테 카를로(HMC)를 도입하여 고차원에서의 빠른 탐색을 가능하게 하고, 계층적 모델에의 적용과 Stan 프로그래밍 환경을 소개한다.

**키워드**: `HMC`, `Hamiltonian-Monte-Carlo`, `Stan`, `reparameterization`, `efficient-sampling`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 12 (line 23023)

### Ch 13: Modal and distributional approximations (pp. 311-349)

**핵심**: 사후 최빈값 탐색, 정규 및 혼합 정규 근사, EM 알고리즘을 통한 주변 사후 최빈값 탐색을 다룬다. 변분 추론(variational inference)과 기대치 전파(expectation propagation) 등 분포 근사 기법을 소개하여 대규모 문제에서의 빠른 추론 방법을 제시한다.

**키워드**: `modal-approximation`, `EM-algorithm`, `variational-inference`, `expectation-propagation`, `normal-approximation`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 13 (line 24169)

### Ch 14: Introduction to regression models (pp. 353-378)

**핵심**: 정규 선형 회귀의 베이즈 분석을 소개한다. 균등 사전분포 하에서의 기본 결과를 유도하고, 미국 선거의 현직 효과 추정을 확장 예제로 사용하며, 정규화·차원 축소·불등 분산·수치적 사전정보 포함 등 실용적 주제를 다룬다.

**키워드**: `linear-regression`, `bayesian-regression`, `incumbency`, `regularization`, `conditional-modeling`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 14 (line 27184)

### Ch 15: Hierarchical linear models (pp. 381-402)

**핵심**: 다수준 예측변수가 있는 계층적 회귀 모델을 다룬다. 미국 대통령 선거 예측을 예시로, 변동 절편과 기울기 모델, 분산 분석과의 관계, 분산 성분에 대한 계층적 모델을 설명한다.

**키워드**: `hierarchical-regression`, `varying-intercept`, `varying-slope`, `ANOVA`, `multilevel`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 15 (line 29197)

### Ch 16: Generalized linear models (pp. 405-432)

**핵심**: 일반화 선형 모델을 베이즈적 관점에서 검토한다. 로지스틱 회귀의 약정보적 사전분포, 경찰 검문의 과분산 포아송 회귀, 국가 수준 여론 추정, 다변량 범주형 데이터의 로그선형 모델을 다룬다.

**키워드**: `GLM`, `logistic-regression`, `Poisson-regression`, `overdispersion`, `loglinear`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 16 (line 31535)

### Ch 17: Models for robust inference (pp. 435-446)

**핵심**: 이상치에 대한 정규 모델의 비강건성을 다루고, 표준 모델의 과분산 확장을 통한 로버스트 추론을 소개한다. 8개 학교 예제에 t-분포를 적용하고, t-분포 오차를 사용한 로버스트 회귀를 설명한다.

**키워드**: `robustness`, `outliers`, `t-distribution`, `overdispersion`, `eight-schools`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 17 (line 34471)

### Ch 18: Models for missing data (pp. 449-467)

**핵심**: 결측 데이터 문제를 베이즈 프레임워크에서 다중 대체(multiple imputation)로 처리하는 방법을 설명한다. 다변량 정규 및 t-모델에서의 결측값 처리, 여론조사 시계열 대체, 슬로베니아 여론조사의 계수 데이터 결측값 문제를 예시로 사용한다.

**키워드**: `missing-data`, `multiple-imputation`, `ignorability`, `MAR`, `multivariate-normal`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 18 (line 35484)

### Ch 19: Parametric nonlinear models (pp. 471-486)

**핵심**: 예측변수와 파라미터가 선형으로 결합하지 않는 비선형 모델을 다룬다. 연속 희석 검정(serial dilution assay)과 모집단 독성동태학(population toxicokinetics)을 예시로, 모델 구축·계산·검정의 세 단계를 비선형 맥락에서 적용한다.

**키워드**: `nonlinear-model`, `serial-dilution`, `toxicokinetics`, `pharmacokinetics`, `parametric`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 19 (line 36896)

### Ch 20: Basis function models (pp. 487-498)

**핵심**: 스플라인과 기저 함수 가중합을 사용한 비선형 회귀를 소개한다. 기저 함수 선택 및 계수 축소(shrinkage), 비정규 모델과 회귀 표면으로의 확장을 다루어 유연한 비모수적 적합을 가능하게 한다.

**키워드**: `basis-function`, `spline`, `shrinkage`, `knot-selection`, `nonparametric-regression`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 20 (line 38654)

### Ch 21: Gaussian process models (pp. 501-516)

**핵심**: 가우시안 과정을 회귀 함수에 대한 사전분포로 사용하는 방법을 소개한다. 생일·출생일 데이터 분석, 잠재 가우시안 과정 모델, 함수적 데이터 분석, 밀도 추정 및 회귀로의 확장을 다룬다.

**키워드**: `Gaussian-process`, `GP-regression`, `covariance-function`, `functional-data`, `density-estimation`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 21 (line 39566)

### Ch 22: Finite mixture models (pp. 519-543)

**핵심**: 혼합 분포 모델의 설정과 해석을 다룬다. 조현병 환자의 반응시간 데이터로 혼합 모델을 적합하고, 라벨 스위칭 문제, 미지의 성분 수, 분류 및 회귀를 위한 혼합 모델을 설명한다.

**키워드**: `mixture-model`, `label-switching`, `latent-variable`, `classification`, `reaction-time`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 22 (line 41036)

### Ch 23: Dirichlet process models (pp. 545-573)

**핵심**: 디리클레 과정을 무한 차원 사전분포로 사용하여 미지의 분포에 대한 베이즈 추론을 수행한다. 베이즈 히스토그램에서 출발하여 디리클레 과정 혼합 모델, 밀도 추정을 넘어선 확장, 계층적 의존성, 밀도 회귀를 다룬다.

**키워드**: `Dirichlet-process`, `nonparametric-Bayes`, `infinite-mixture`, `density-estimation`, `stick-breaking`

**상세**: → `Gelman et al. - Bayesian Data Analysis (3rd Ed.).md` Ch 23 (line 43098)
