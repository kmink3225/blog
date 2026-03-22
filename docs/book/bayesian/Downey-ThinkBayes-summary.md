---
name: "Think Bayes: Bayesian Statistics in Python (2nd Edition)"
type: book-summary
source_file: "Downey-ThinkBayes_azure_full.md"
authors: "Allen B. Downey"
year: 2021
total_pages: 305
language: en
keywords: [bayesian-statistics, python, bayes-theorem, probability, MCMC, conjugate-prior, decision-analysis, classification, regression, ABC]
---

# Think Bayes: Bayesian Statistics in Python — Summary

> Allen B. Downey (2021), 305 pages, 20 chapters
> 프로그래밍 능력을 활용하여 수학 공식 대신 Python 코드와 이산 근사로 베이즈 통계를 학습하는 실용 입문서이다.

## Contents

- Preface
- Ch 1. Probability (pp. 1-14)
- Ch 2. Bayes's Theorem (pp. 17-26)
- Ch 3. Distributions (pp. 29-41)
- Ch 4. Estimating Proportions (pp. 43-54)
- Ch 5. Estimating Counts (pp. 57-66)
- Ch 6. Odds and Addends (pp. 69-81)
- Ch 7. Minimum, Maximum, and Mixture (pp. 83-97)
- Ch 8. Poisson Processes (pp. 99-110)
- Ch 9. Decision Analysis (pp. 113-127)
- Ch 10. Testing (pp. 129-142)
- Ch 11. Comparison (pp. 145-158)
- Ch 12. Classification (pp. 161-173)
- Ch 13. Inference (pp. 175-189)
- Ch 14. Survival Analysis (pp. 191-204)
- Ch 15. Mark and Recapture (pp. 207-221)
- Ch 16. Logistic Regression (pp. 223-238)
- Ch 17. Regression (pp. 241-255)
- Ch 18. Conjugate Priors (pp. 257-267)
- Ch 19. MCMC (pp. 269-283)
- Ch 20. Approximate Bayesian Computation (pp. 287-303)
- Index (p. 305)

---

## Chapter Summaries

### Ch 1: Probability (pp. 1-14)

**핵심**: 베이즈 통계의 기초인 조건부 확률을 Linda the Banker 문제로 도입한다. General Social Survey 데이터셋을 사용하여 결합 확률, 조건부 확률, 전체 확률의 법칙을 Python으로 계산하며, 확률의 세 가지 정리와 베이즈 정리를 유도한다.

**키워드**: `conditional-probability`, `conjunction`, `bayes-theorem`, `total-probability`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 1 (line 1408)

### Ch 2: Bayes's Theorem (pp. 17-26)

**핵심**: 베이즈 정리를 쿠키 문제(Cookie Problem)에 적용하여 사전-사후 확률 갱신 과정을 설명한다. Diachronic Bayes와 Bayes Table 방식을 도입하고, 주사위 문제와 몬티 홀 문제를 통해 반복적 갱신을 시연한다.

**키워드**: `bayes-theorem`, `cookie-problem`, `diachronic-bayes`, `monty-hall`, `bayes-table`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 2 (line 2312)

### Ch 3: Distributions (pp. 29-41)

**핵심**: 확률 질량 함수(PMF)와 empiricaldist 라이브러리의 Pmf 클래스를 소개한다. 쿠키 문제를 Pmf 객체로 재구현하고, 101개 그릇 문제로 확장하여 베이즈 갱신을 분포 수준에서 수행하는 방법을 다룬다.

**키워드**: `PMF`, `empiricaldist`, `distributions`, `bayesian-update`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 3 (line 3002)

### Ch 4: Estimating Proportions (pp. 43-54)

**핵심**: 유로 동전 문제를 통해 비율 추정으로 전환한다. 이항 분포를 도입하고, 균등 사전분포 및 삼각 사전분포를 사용한 베이즈 추정을 수행하며, 사전분포 선택과 미지 값을 확률로 표현하는 베이즈 통계의 핵심 요소를 설명한다.

**키워드**: `binomial-distribution`, `proportion-estimation`, `prior-distribution`, `euro-problem`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 4 (line 3901)

### Ch 5: Estimating Counts (pp. 57-66)

**핵심**: 기차 문제(Train Problem)와 독일 전차 문제(German Tank Problem)를 통해 모집단 크기 추정을 다룬다. 사전분포에 대한 민감도 분석, 거듭제곱 법칙 사전분포, 신뢰 구간(credible interval) 개념을 도입한다.

**키워드**: `count-estimation`, `german-tank-problem`, `power-law-prior`, `credible-interval`, `sensitivity`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 5 (line 4639)

### Ch 6: Odds and Addends (pp. 69-81)

**핵심**: 확률을 승산(odds)으로 표현하는 방법과 베이즈 규칙(Bayes's rule)을 소개한다. Oliver's Blood 문제로 증거의 강도를 정량화하고, 확률변수의 합·차에 대한 분포 연산(addends)과 글루텐 민감도 문제를 통해 순방향/역방향 문제를 구분한다.

**키워드**: `odds`, `bayes-rule`, `likelihood-ratio`, `addends`, `forward-inverse-problem`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 6 (line 5323)

### Ch 7: Minimum, Maximum, and Mixture (pp. 83-97)

**핵심**: 누적 분포 함수(CDF)를 도입하고 최솟값·최댓값 분포의 계산법을 설명한다. D&D의 "4개 중 최고 3개" 문제를 예시로 사용하며, 혼합 분포(mixture distribution)를 통해 예측 문제를 해결하는 방법을 다룬다.

**키워드**: `CDF`, `minimum`, `maximum`, `mixture-distribution`, `prediction`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 7 (line 6232)

### Ch 8: Poisson Processes (pp. 99-110)

**핵심**: 포아송 과정을 소개하고 2018 FIFA 월드컵 결승전 데이터를 활용하여 축구 경기의 골 득점을 모델링한다. 감마 분포를 사전분포로, 포아송 분포를 가능도로 사용하며, 우월 확률(probability of superiority)과 재경기 예측을 수행한다.

**키워드**: `poisson-process`, `gamma-distribution`, `world-cup-problem`, `probability-of-superiority`, `exponential-distribution`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 8 (line 7396)

### Ch 9: Decision Analysis (pp. 113-127)

**핵심**: TV 쇼 "The Price Is Right"를 활용한 베이즈 의사결정 분석을 다룬다. 커널 밀도 추정(KDE)으로 사전분포를 구성하고, 정규 분포로 가능도를 계산한 뒤, 사후분포를 이용하여 기대 이익을 최대화하는 최적 입찰 전략을 도출한다.

**키워드**: `decision-analysis`, `KDE`, `expected-gain`, `optimal-bidding`, `price-is-right`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 9 (line 8325)

### Ch 10: Testing (pp. 129-142)

**핵심**: 유로 동전 문제를 재방문하여 베이즈 가설 검정을 수행한다. 편향된 동전 vs 공정한 동전의 증거를 베이즈 팩터로 평가하고, 다중 밴딧(Bayesian Bandits) 문제를 통해 탐험-활용(explore-exploit) 전략을 소개한다.

**키워드**: `hypothesis-testing`, `bayes-factor`, `evidence`, `bayesian-bandits`, `explore-exploit`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 10 (line 9295)

### Ch 11: Comparison (pp. 145-158)

**핵심**: 결합 분포(joint distribution)를 도입하고 외적(outer product) 연산으로 구현한다. 두 사람의 키 비교 문제와 체스 선수 평가 문제를 통해 결합 분포의 갱신, 주변 분포, 조건부 사후분포를 다루며, 변수 간 독립과 종속의 개념을 설명한다.

**키워드**: `joint-distribution`, `outer-product`, `marginal-distribution`, `conditional-posterior`, `mesh-grid`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 11 (line 10353)

### Ch 12: Classification (pp. 161-173)

**핵심**: Palmer Station 펭귄 데이터를 사용하여 베이즈 분류를 시연한다. 나이브 베이즈 분류기를 구축하고, 다변량 정규 분포를 도입하여 변수 간 상관관계를 고려하는 개선된 분류기를 만든다.

**키워드**: `naive-bayes`, `classification`, `penguin-data`, `multivariate-normal`, `joint-distribution`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 12 (line 11354)

### Ch 13: Inference (pp. 175-189)

**핵심**: 교육 처치 효과 비교를 통해 베이즈 추론과 빈도주의 t-검정을 대비한다. 두 집단 간 차이의 사후분포를 계산하고, 요약 통계량을 활용한 갱신, 우월 확률, 신뢰 구간 등 p-값의 베이즈 대안을 제시한다.

**키워드**: `bayesian-inference`, `t-test-alternative`, `posterior-difference`, `summary-statistics`, `probability-of-superiority`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 13 (line 12281)

### Ch 14: Survival Analysis (pp. 191-204)

**핵심**: 생존 분석을 소개하며 와이블 분포를 사용하여 전구 수명과 보호소 개의 입양 시간을 모델링한다. 불완전 데이터(절단 데이터)를 베이즈 방법으로 다루는 기법과 사후 예측 분포를 설명한다.

**키워드**: `survival-analysis`, `weibull-distribution`, `censored-data`, `posterior-predictive`, `incomplete-data`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 14 (line 13276)

### Ch 15: Mark and Recapture (pp. 207-221)

**핵심**: 표지-재포획 실험을 통한 모집단 크기 추정을 다룬다. 그리즐리 곰 DNA 포획 데이터를 사용하여 2-파라미터 및 3-파라미터 모델을 구축하고, Lincoln Index 문제와 소프트웨어 버그 수 추정으로 확장한다.

**키워드**: `mark-recapture`, `population-estimation`, `lincoln-index`, `hypergeometric`, `three-parameter-model`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 15 (line 14317)

### Ch 16: Logistic Regression (pp. 223-238)

**핵심**: 로그 승산(log odds)과 로지스틱 회귀를 소개한다. 베이즈 규칙의 로그 스케일 해석으로 증거 축적 과정을 설명하고, 우주왕복선 챌린저호의 O-링 데이터로 온도와 손상 확률 간의 관계를 모델링한다.

**키워드**: `logistic-regression`, `log-odds`, `space-shuttle`, `o-ring`, `empirical-bayes`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 16 (line 15390)

### Ch 17: Regression (pp. 241-255)

**핵심**: 단순 선형 회귀의 베이즈적 접근을 다룬다. Norfolk County 적설량 변화와 마라톤 세계 기록 데이터를 사용하여 세 개 파라미터(절편, 기울기, 분산)의 사후분포를 추정하고 미래 값을 예측한다.

**키워드**: `linear-regression`, `bayesian-regression`, `snowfall`, `marathon`, `prediction`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 17 (line 16594)

### Ch 18: Conjugate Priors (pp. 257-267)

**핵심**: 격자 방법의 한계를 넘기 위해 켤레 사전분포를 도입한다. 월드컵 문제를 감마-포아송 켤레쌍으로 재풀이하고, 이항-베타 및 다항-디리클레 켤레쌍을 소개하여 분석적 갱신의 효율성을 보여준다.

**키워드**: `conjugate-prior`, `gamma-poisson`, `beta-binomial`, `dirichlet-multinomial`, `analytical-update`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 18 (line 17795)

### Ch 19: MCMC (pp. 269-283)

**핵심**: 마르코프 체인 몬테 카를로(MCMC) 방법과 PyMC3 라이브러리를 소개한다. 월드컵 문제를 MCMC로 재풀이하고, 사전 예측 분포 점검, 행복도 데이터의 단순/다중 회귀를 PyMC3으로 구현하여 격자 방법 이후의 확장 경로를 제시한다.

**키워드**: `MCMC`, `PyMC3`, `prior-predictive`, `posterior-predictive`, `regression`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 19 (line 18503)

### Ch 20: Approximate Bayesian Computation (pp. 287-303)

**핵심**: 가장 복잡한 문제를 위한 최후의 수단으로 근사 베이즈 계산(ABC)을 소개한다. 신장 종양 성장 모델링으로 종양의 나이를 추정하고, 세포 계수 문제에 ABC를 적용하여 시뮬레이션 기반 추론을 시연한다.

**키워드**: `ABC`, `approximate-bayesian-computation`, `kidney-tumor`, `cell-counting`, `simulation-based-inference`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 20 (line 19580)
