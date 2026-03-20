---
name: "Extending the Linear Model with R"
type: book-summary
source_file: "Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md"
authors: "Julian J. Faraway"
year: 2006
total_pages: 331
language: en
keywords: [GLM, R, binomial, Poisson, multinomial, random effects, mixed effects, longitudinal data, nonparametric regression, additive models, trees, neural networks]
---

# Extending the Linear Model with R — Summary

> Julian J. Faraway (2006), 331 pages, 14 chapters + 2 appendices
> R을 활용하여 일반화선형모형, 혼합효과모형, 비모수회귀 등 선형모형의 세 가지 확장을 실습 중심으로 다루는 교과서이다.

## Contents

- Preface (ix)
- 1 Introduction (1)
- 2 Binomial Data (28)
- 3 Count Regression (61)
- 4 Contingency Tables (76)
- 5 Multinomial Data (106)
- 6 Generalized Linear Models (126)
- 7 Other GLMs (149)
- 8 Random Effects (169)
- 9 Repeated Measures and Longitudinal Data (203)
- 10 Mixed Effect Models for Nonnormal Responses (221)
- 11 Nonparametric Regression (232)
- 12 Additive Models (254)
- 13 Trees (278)
- 14 Neural Networks (296)
- A Likelihood Theory (307)
- B R Information (316)
- Bibliography (318)
- Index (324)

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-27)

**핵심**: 선형모형과 R의 기본 사항을 복습한다. 2000년 미국 대선 조지아주 투표 데이터를 사용하여 R에서의 데이터 탐색, 회귀 분석, 모형 진단의 전체 워크플로우를 시연한다. 이 책의 세 가지 확장 방향(GLM: 반응변수의 일반화, 혼합효과: 오차구조의 일반화, 비모수회귀: 예측변수의 일반화)을 소개한다.

**키워드**: `linear model`, `R`, `regression review`, `model diagnostics`, `Georgia voting data`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 1 (line 539)

### Ch 2: Binomial Data (pp. 28-60)

**핵심**: 이항 반응 데이터의 모형화를 다룬다. 챌린저 우주왕복선 O-링 사고 데이터를 시작으로 로지스틱 회귀, 모형 해석(오즈비), 모형 적합도 검정, 과산포 처리, 프로빗·보완로그-로그 모형 등을 R 코드와 함께 설명한다. 그룹 데이터와 개별 데이터의 처리 방식 차이도 다룬다.

**키워드**: `logistic regression`, `odds ratio`, `Challenger disaster`, `probit`, `complementary log-log`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 2 (line 3704)

### Ch 3: Count Regression (pp. 61-75)

**핵심**: 카운트 반응변수를 위한 회귀 모형을 다룬다. 포아송 회귀의 정의와 적합, 포아송 분포의 발생 맥락(드문 사건의 이항 근사, 사건 발생률, 분할표), 비율 모형, 과산포 처리, 음이항 회귀를 설명한다.

**키워드**: `Poisson regression`, `rate model`, `over-dispersion`, `negative binomial`, `count data`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 3 (line 6779)

### Ch 4: Contingency Tables (pp. 76-105)

**핵심**: 교차분류 범주형 데이터의 분석을 다룬다. 2x2 표에서의 독립성 검정, 오즈비, 쌍 대응 데이터부터 시작하여 다원 분할표의 로그선형 모형, Simpson의 역설, 순서형 자료 처리, 큰 분할표에서의 모형 선택까지 포괄한다.

**키워드**: `contingency table`, `log-linear model`, `independence`, `odds ratio`, `Simpson's paradox`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 4 (line 8304)

### Ch 5: Multinomial Data (pp. 106-125)

**핵심**: 다항 반응 데이터의 모형화를 다룬다. 명목형 반응을 위한 다항 로짓 모형과 순서형 반응을 위한 비례 오즈 모형을 구분하여 설명한다. 다항분포의 정의에서 출발하여 모형 적합, 해석, R 코드를 사용한 실습을 포함한다.

**키워드**: `multinomial logit`, `proportional odds`, `ordinal data`, `nominal data`, `categorical response`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 5 (line 10990)

### Ch 6: Generalized Linear Models (pp. 126-148)

**핵심**: 이전 장들에서 다룬 개별 모형들을 GLM이라는 통합 틀로 묶어 이론적으로 정리한다. 지수족 분포의 일반적 형태, 연결함수의 정의, 모형 적합을 위한 IRLS 알고리즘, 이탈도와 잔차, 대가설 검정을 다루며, Nelder와 Wedderburn(1972)의 원래 논문을 참조한다.

**키워드**: `exponential family`, `canonical parameter`, `IRLS`, `deviance`, `link function`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 6 (line 12922)

### Ch 7: Other GLMs (pp. 149-168)

**핵심**: 이항·정규·포아송 이외의 GLM을 다룬다. 감마 GLM(연속 양의 비대칭 반응), 역가우시안 GLM, 이중 GLM(평균과 분산의 동시 모형화), 준-GLM(분포 미지정, 연결함수와 분산함수만 지정)을 소개한다.

**키워드**: `gamma GLM`, `inverse Gaussian`, `dual GLM`, `quasi-GLM`, `dispersion modeling`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 7 (line 14722)

### Ch 8: Random Effects (pp. 169-202)

**핵심**: 그룹화된 데이터를 위한 랜덤효과 모형을 도입한다. 고정효과와 랜덤효과의 개념적 구분, 단일 그룹 요인의 랜덤효과 모형, 중첩(nested) 설계, 교차(crossed) 설계, 다수준 모형의 적합과 추론을 R의 lme4 패키지를 통해 시연한다.

**키워드**: `random effects`, `fixed effects`, `nested design`, `crossed design`, `multilevel model`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 8 (line 16839)

### Ch 9: Repeated Measures and Longitudinal Data (pp. 203-220)

**핵심**: 반복측정 및 종단 데이터를 위한 혼합효과 모형을 다룬다. 개체 내 상관을 고려한 모형 구조(고정효과 + 랜덤효과 + 오차)를 정의하고, 오차의 공분산 구조 모형화, 시계열적 상관 구조 등을 포함한다.

**키워드**: `repeated measures`, `longitudinal data`, `mixed effects model`, `covariance structure`, `panel study`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 9 (line 20308)

### Ch 10: Mixed Effect Models for Nonnormal Responses (pp. 221-231)

**핵심**: GLM과 랜덤효과를 결합한 일반화선형혼합모형(GLMM)을 다룬다. 지수족 반응에 랜덤효과를 추가하는 모형 구조, 우도함수의 적분 문제, 근사 추정 방법(PQL, Laplace, 구적법)을 설명하고 R에서의 실습을 포함한다.

**키워드**: `GLMM`, `generalized linear mixed model`, `PQL`, `Laplace approximation`, `random effects`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 10 (line 22109)

### Ch 11: Nonparametric Regression (pp. 232-253)

**핵심**: 단변량 비모수 회귀 방법을 다룬다. 커널 평활법, 스플라인(평활 스플라인, 회귀 스플라인), 국소 다항식 회귀(loess), 파동함수(wavelet) 방법을 비교하고, 평활 모수 선택(교차검증, GCV 등)과 신뢰 구간 문제를 설명한다.

**키워드**: `kernel smoothing`, `spline`, `loess`, `bandwidth selection`, `cross-validation`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 11 (line 23611)

### Ch 12: Additive Models (pp. 254-277)

**핵심**: 다변량 비모수 회귀를 위한 가법모형을 다룬다. 선형모형과 완전 비모수 모형의 절충으로서 가법모형을 정의하고, 역적합(backfitting) 알고리즘, 일반화가법모형(GAM), 다변량 적응 회귀 스플라인(MARS) 등을 R에서 실습한다.

**키워드**: `additive model`, `GAM`, `backfitting`, `MARS`, `multivariate smoothing`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 12 (line 25085)

### Ch 13: Trees (pp. 278-295)

**핵심**: 의사결정나무 방법론을 다룬다. 회귀나무와 분류나무의 구성 원리, 가지치기(pruning), 배깅(bagging), 랜덤 포레스트, 부스팅 등 앙상블 방법을 소개한다. 통계학과 기계학습 양쪽의 나무 방법론 발전을 개관한다.

**키워드**: `regression tree`, `classification tree`, `pruning`, `random forest`, `boosting`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 13 (line 27857)

### Ch 14: Neural Networks (pp. 296-306)

**핵심**: 인공신경망의 통계학적 관점에서의 소개를 다룬다. 뉴런 모형에서 출발하여 단층·다층 퍼셉트론, 역전파 알고리즘, 과적합 방지, 통계 모형과의 관계를 설명한다. 실용적 성능은 과장에 비해 제한적이지만 유용한 도구임을 강조한다.

**키워드**: `neural network`, `perceptron`, `backpropagation`, `overfitting`, `universal approximation`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 14 (line 29449)
