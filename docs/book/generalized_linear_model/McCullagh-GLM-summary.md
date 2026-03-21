---
name: "Generalized Linear Models (2nd Edition)"
type: book-summary
source_file: "McCullagh-GLM_full.md"
authors: "P. McCullagh, J.A. Nelder"
year: 1989
total_pages: 511
language: en
keywords: [GLM, exponential family, deviance, link function, quasi-likelihood, binary data, log-linear models, polytomous data, survival analysis, dispersion, model checking]
---

# Generalized Linear Models (2nd Edition) — Summary

> P. McCullagh, J.A. Nelder (1989), 511 pages, 15 chapters
> 일반화선형모형(GLM)의 이론적 기초와 응용을 체계적으로 다루는 고전적 교과서이다.

## Contents

- Preface to the first edition (xvi)
- Preface (xviii)
- 1 Introduction (1)
- 2 An outline of generalized linear models (21)
- 3 Models for continuous data with constant variance (48)
- 4 Binary data (98)
- 5 Models for polytomous data (149)
- 6 Log-linear models (193)
- 7 Conditional likelihoods (245)
- 8 Models with constant coefficient of variation (285)
- 9 Quasi-likelihood functions (323)
- 10 Joint modelling of mean and dispersion (357)
- 11 Models with additional non-linear parameters (372)
- 12 Model checking (391)
- 13 Models for survival data (419)
- 14 Components of dispersion (432)
- 15 Further topics (455)
- Appendices (469)
- References (479)
- Index (506)

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-20)

**핵심**: GLM의 역사적 배경과 동기를 설명한다. 고전적 선형모형에서 출발하여 probit 분석, logit 모형, 로그선형 모형 등으로의 확장 과정을 개관한다. 데이터 관찰, 이론으로서의 패턴, 모형 적합, 좋은 모형의 조건 등 통계적 모형화의 철학적 기초를 다룬다.

**키워드**: `linear model`, `probit analysis`, `logit model`, `log-linear model`, `model fitting`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 1 (line 1812)

### Ch 2: An outline of generalized linear models (pp. 21-47)

**핵심**: GLM의 세 가지 구성요소(확률분포, 선형예측자, 연결함수)를 정의한다. 모형 선택, 추정, 예측의 세 과정을 기술하고, 지수족 분포와 우도함수, 충분통계량과 정준연결함수의 관계를 설명한다. 적합도 측정을 위한 이탈도(deviance) 분석과 잔차 유형(Pearson, Anscombe, deviance)을 소개하며, IRLS 알고리즘을 제시한다.

**키워드**: `exponential family`, `link function`, `deviance`, `IRLS`, `sufficient statistic`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 2 (line 2818)

### Ch 3: Models for continuous data with constant variance (pp. 48-97)

**핵심**: 고전적 선형모형을 GLM의 특수 사례로 재해석한다. 정규분포 오차구조, 연속형/범주형 공변량, 모형 공식(model formulae)의 연산자(dot, +, *, /) 체계를 설명한다. 에일리어싱(aliasing), 최대우도 추정의 기하학적 해석, 최소제곱 알고리즘(정보행렬 기반, 직접분해법)을 다룬다.

**키워드**: `normal distribution`, `linear predictor`, `model formula`, `aliasing`, `least squares`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 3 (line 4309)

### Ch 4: Binary data (pp. 98-148)

**핵심**: 이항 반응 데이터의 모형화를 다룬다. 이항분포의 성질(모멘트, 정규극한, 포아송극한)을 기술하고, logit/probit/complementary log-log 등 연결함수를 비교한다. 우도함수, 이탈도, 과산포(over-dispersion) 문제를 논의하며, 도마뱀 서식지 선호도 예제를 통해 실제 적용을 보여준다.

**키워드**: `binomial distribution`, `logit`, `probit`, `over-dispersion`, `deviance`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 4 (line 7133)

### Ch 5: Models for polytomous data (pp. 149-192)

**핵심**: 다범주 반응 데이터를 위한 모형을 다룬다. 순서형, 구간형, 명목형, 계층형 등 측정 척도별로 적절한 연결함수를 제시한다. 다항분포의 이론(모멘트, 일반화역행렬, 이차형식, 주변·조건부 분포)과 우도함수 기반 추정을 설명하며, 치즈 맛 실험과 탄광부 진폐증 예제를 포함한다.

**키워드**: `multinomial distribution`, `ordinal scale`, `nominal scale`, `proportional odds`, `measurement scale`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 5 (line 11131)

### Ch 6: Log-linear models (pp. 193-244)

**핵심**: 비율이 아닌 카운트 데이터를 위한 로그선형 모형을 다룬다. 포아송 분포의 성질과 로그우도함수, 과산포 처리를 설명한다. 로그선형 모형과 다항 반응 모형의 관계, 독립성·조건부 독립성, 정준상관모형, 다변량 회귀모형 등 다중 반응의 분석을 포괄적으로 기술한다.

**키워드**: `Poisson distribution`, `log-linear model`, `contingency table`, `independence`, `multiple responses`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 6 (line 13894)

### Ch 7: Conditional likelihoods (pp. 245-284)

**핵심**: 장해 모수(nuisance parameter)가 존재할 때의 추론을 다룬다. 주변 우도, 조건부 우도, 프로파일 우도의 개념을 설명하고, 중심·비중심 초기하분포를 도출한다. 2x2 표에서의 이항확률 비교, 정보 결합, 대응 쌍 분석(명목·순서 반응) 등의 응용을 포함한다.

**키워드**: `conditional likelihood`, `marginal likelihood`, `hypergeometric distribution`, `nuisance parameter`, `matched pairs`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 7 (line 18288)

### Ch 8: Models with constant coefficient of variation (pp. 285-322)

**핵심**: 분산이 평균의 제곱에 비례하는 데이터(변동계수 일정)를 위한 모형을 다룬다. 감마 분포의 성질, 분산함수, 이탈도, 정준연결(역수), 로그연결(곱셈 모형), 항등연결(선형 모형) 등을 설명한다. 자동차 보험 청구, 혈액 응고 시간, 강수량 모형화, 초파리 발달률 등의 예제를 포함한다.

**키워드**: `gamma distribution`, `coefficient of variation`, `variance function`, `multiplicative model`, `inverse link`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 8 (line 20551)

### Ch 9: Quasi-likelihood functions (pp. 323-356)

**핵심**: 완전한 확률 모형을 가정하지 않고 평균-분산 관계만으로 추론하는 준우도(quasi-likelihood) 방법을 다룬다. 독립 관측과 종속 관측 각각에 대한 준우도 추정방정식을 유도하고, 최적 추정함수, 최적성 기준, 확장 준우도(extended quasi-likelihood)를 논의한다.

**키워드**: `quasi-likelihood`, `estimating equation`, `variance function`, `optimal estimating function`, `extended quasi-likelihood`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 9 (line 26005)

### Ch 10: Joint modelling of mean and dispersion (pp. 357-371)

**핵심**: 평균과 산포를 동시에 모형화하는 방법을 다룬다. 산포 모수가 공변량에 따라 체계적으로 변할 때의 모형 명세, 평균-산포 효과의 교호작용, 확장 준우도 기준, 첨도와 자유도에 대한 추정방정식 조정을 설명한다. 트럭용 판스프링 생산 예제를 통해 실제 적용을 보여준다.

**키워드**: `dispersion model`, `mean-dispersion interaction`, `extended quasi-likelihood`, `joint estimation`, `Taguchi methods`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 10 (line 28323)

### Ch 11: Models with additional non-linear parameters (pp. 372-390)

**핵심**: 분산함수, 연결함수, 또는 공변량에 미지의 비선형 모수가 포함된 모형을 다룬다. Box-Cox 변환의 일반화로서 연결함수 내 모수 추정, 데이터 변환과 적합값 변환의 비교, 비선형 공변량 항의 처리를 논의한다. 비료 효과, 살충제·상승제 분석, 약물 혼합 등의 예제를 포함한다.

**키워드**: `non-linear parameter`, `Box-Cox transformation`, `link parameter`, `variance function parameter`, `non-linear covariates`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 11 (line 29407)

### Ch 12: Model checking (pp. 391-418)

**핵심**: 모형 진단의 체계적 전략을 제시한다. 스코어 검정, 평활화, 잔차를 이용한 비공식적 검사를 소개하고, 분산함수·연결함수·공변량 척도에 대한 체계적 이탈 검사와 레버리지·일관성·영향력 측도를 이용한 개별 이상점 검사를 구분한다. 당근 피해, Minitab 나무, 보험 청구 예제를 포함한다.

**키워드**: `residual`, `leverage`, `influence`, `score test`, `model diagnostics`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 12 (line 30747)

### Ch 13: Models for survival data (pp. 419-431)

**핵심**: 생존 시간 데이터의 분석을 다룬다. 생존함수와 위험함수의 정의, 비례위험 모형, 지수·와이블·극치값 분포를 가정한 모수적 추정, Cox의 비례위험 모형과 부분 우도(partial likelihood), 동률 처리 방법을 설명한다. 백혈병 관해 시간 예제를 포함한다.

**키워드**: `survival function`, `hazard function`, `proportional hazards`, `Cox model`, `partial likelihood`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 13 (line 32661)

### Ch 14: Components of dispersion (pp. 432-454)

**핵심**: 관측값이 독립이 아닌 계층적 구조(예: 학교-교실-학생)를 가질 때의 분산 성분 모형을 다룬다. 선형모형과 비선형모형에서의 분산 성분 추정을 설명하고, 도롱뇽 교배 실험 예제를 통해 랜덤 효과가 포함된 로지스틱 모형의 산포 모수 추정을 보여준다.

**키워드**: `variance components`, `random effects`, `hierarchical data`, `intraclass correlation`, `salamander mating`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 14 (line 33374)

### Ch 15: Further topics (pp. 455-468)

**핵심**: 추가적인 고급 주제를 간략히 다룬다. 최대우도 추정량의 편향 교정(정준 연결과 비정준 모형), Bartlett 조정의 계산, 일반화가법모형(GAM)의 적합 알고리즘과 평활 방법을 소개한다.

**키워드**: `bias correction`, `Bartlett adjustment`, `generalized additive model`, `smoothing`, `exponential regression`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 15 (line 35555)
