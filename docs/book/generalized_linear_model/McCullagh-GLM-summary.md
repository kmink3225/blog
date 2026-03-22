---
name: "Generalized Linear Models (2nd Edition)"
type: book-summary
source_file: "McCullagh-GLM_azure_full.md"
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

이 장은 GLM의 역사적 배경과 통계적 모형화의 철학적 기초를 설명한다. Gauss와 Legendre의 최소제곱법에서 출발하여 정규 오차 모형의 발전 과정을 개관하고, 이산 사건을 위한 포아송·이항 분포의 역사를 기술한다. 데이터 관찰의 문제를 체계적 효과와 무작위 효과의 분리로 정의하고, 이론을 모수의 함수로 생성되는 패턴으로 해석한다. 모형 적합을 불일치 측도(L₁, L₂, L∞ 노름)의 최소화로 정의하며, 최소제곱 기준이 정규 분포 가정 하의 최대우도 추정과 동치임을 보인다. 우도함수의 이중 해석—밀도함수(y의 함수)와 가능도함수(μ의 함수)—을 구분하며, Fisher 정보와 추정 정밀도의 관계를 설명한다. 좋은 모형의 조건으로 절약성(parsimony), 범위(scope), 모수 불변성(parameter invariance)을 제시한다. probit 분석(Bliss, 1935), 로짓 모형(Berkson, 1944; Cox, 1958), 로그선형 모형의 역사적 발전을 추적한다. Nelder와 Wedderburn(1972)의 원래 논문이 이 개별 모형들을 GLM이라는 단일 클래스로 통합한 업적을 기술한다. 분산이 평균에 의존하는 비정규 연속 반응(감마, 역가우시안)에 대한 모형의 필요성을 설명한다. 모형 적합과 모형 비판의 이중 과정(Box, 1980)과 "모든 모형은 틀리지만, 일부는 유용하다"는 원칙을 강조한다.

### Ch 2: An outline of generalized linear models (pp. 21-47)

**핵심**: GLM의 세 가지 구성요소(확률분포, 선형예측자, 연결함수)를 정의한다. 모형 선택, 추정, 예측의 세 과정을 기술하고, 지수족 분포와 우도함수, 충분통계량과 정준연결함수의 관계를 설명한다. 적합도 측정을 위한 이탈도(deviance) 분석과 잔차 유형(Pearson, Anscombe, deviance)을 소개하며, IRLS 알고리즘을 제시한다.

**키워드**: `exponential family`, `link function`, `deviance`, `IRLS`, `sufficient statistic`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 2 (line 2818)

이 장은 GLM의 형식적 정의와 추론 방법을 체계적으로 제시한다. 모형 적합의 세 과정—모형 선택, 모수 추정, 예측—을 Box-Jenkins 시계열 분석의 틀에서 기술한다. GLM의 세 가지 구성요소를 확률 성분(지수족 분포), 체계적 성분(선형예측자 η = Σxⱼβⱼ), 연결 성분(연결함수 g(μ) = η)으로 정의한다. 지수족 분포의 일반적 형태 f(y;θ,φ) = exp{(yθ−b(θ))/a(φ)+c(y,φ)}를 정의하고, 정규·포아송·이항·감마 분포가 이 형태의 특수 사례임을 보인다. 평균 μ = b′(θ)와 분산 var(Y) = b″(θ)a(φ)를 유도하며, 충분통계량과 정준 모수의 관계를 설명한다. 축척 이탈도(scaled deviance) D* = 2{l(y;y) − l(μ̂;y)}를 적합도 측도로 정의하고, 정규 모형에서 잔차제곱합과 동치임을 보인다. IRLS(반복 재가중 최소제곱) 알고리즘의 유도와 수렴 성질을 설명한다. 잔차의 세 가지 유형—Pearson 잔차, Anscombe 잔차, 이탈도 잔차—을 정의하고 각각의 분포적 성질을 비교한다. 정준 연결함수의 수학적·계산적 편리성과 비정준 연결의 사용 동기를 논의한다. 모형 선택에서 척도 선택의 문제를 다루며, GLM이 정규성과 등분산 가정을 완화함으로써 척도 선택 문제를 크게 줄여줌을 강조한다.

### Ch 3: Models for continuous data with constant variance (pp. 48-97)

**핵심**: 고전적 선형모형을 GLM의 특수 사례로 재해석한다. 정규분포 오차구조, 연속형/범주형 공변량, 모형 공식(model formulae)의 연산자(dot, +, *, /) 체계를 설명한다. 에일리어싱(aliasing), 최대우도 추정의 기하학적 해석, 최소제곱 알고리즘(정보행렬 기반, 직접분해법)을 다룬다.

**키워드**: `normal distribution`, `linear predictor`, `model formula`, `aliasing`, `least squares`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 3 (line 4309)

이 장은 고전적 선형모형을 GLM의 특수 사례로 재해석한다. 정규분포 오차 가정 하에서 항등 연결함수를 사용하는 GLM이 통상적 선형회귀와 동치임을 보인다. 모형 공식(model formulae)의 연산자 체계—dot(.), +, *, /, ^—를 정의하고, 주효과, 교호작용, 중첩의 표현 방법을 설명한다. 연속형 공변량과 범주형 요인의 처리, 에일리어싱(aliasing: 추정 불가능한 모수 조합) 문제를 논의한다. 최대우도 추정의 기하학적 해석을 제시하며, 적합값이 관측 벡터를 모형 부분공간에 직교 사영한 결과임을 보인다. 최소제곱 알고리즘을 정보행렬(X^TWX) 기반 방법과 직접분해법(QR 분해)으로 구분하여 설명한다. 분산분석 표의 구성, 제곱합의 분해, 순차적 대 조정된 제곱합의 구별을 다룬다. 모형 비교를 위한 F-검정과 이탈도 차이 검정의 관계를 설명한다. 잔차 분석, 레버리지, Cook 거리 등 진단 도구를 소개한다. 비선형 회귀와 가중최소제곱을 GLM 틀 안에서 해석한다. 여러 실제 데이터 예제(농업 실험, 공업 실험)를 통해 모형 구성과 해석 과정을 시연한다.

### Ch 4: Binary data (pp. 98-148)

**핵심**: 이항 반응 데이터의 모형화를 다룬다. 이항분포의 성질(모멘트, 정규극한, 포아송극한)을 기술하고, logit/probit/complementary log-log 등 연결함수를 비교한다. 우도함수, 이탈도, 과산포(over-dispersion) 문제를 논의하며, 도마뱀 서식지 선호도 예제를 통해 실제 적용을 보여준다.

**키워드**: `binomial distribution`, `logit`, `probit`, `over-dispersion`, `deviance`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 4 (line 7133)

이 장은 이항 반응 데이터의 모형화를 체계적으로 다룬다. 이항분포의 성질(모멘트, 정규극한, 포아송극한)을 기술하고, logit·probit·complementary log-log 연결함수를 비교한다. 로짓 연결의 정준성(canonicity)과 오즈비를 통한 해석의 편리성을 강조한다. 우도함수 구성, 스코어 방정식의 유도, Fisher 정보행렬의 계산을 상세히 전개한다. 이탈도를 포화 모형과 관심 모형의 로그우도 차이로 정의하고, 대표본에서의 χ² 근사를 설명한다. 과산포(over-dispersion) 문제를 집단 내 이질성과 상관의 관점에서 논의하며, 산포 모수의 추정과 윌리엄스 방법을 제시한다. 도마뱀 서식지 선호도 데이터를 통해 로지스틱 회귀의 적합, 해석, 진단의 전 과정을 시연한다. 유효용량(ED50)의 추정과 Fieller 방법에 의한 신뢰구간 구성을 다룬다. 이항 지수 자료(binary exponential data)에서의 적합 문제와 잔차 분석의 한계를 논의한다. 관측 정보행렬과 기대 정보행렬의 차이, Hauck-Donner 효과에 의한 Wald 검정의 비보수성을 설명한다. 다수의 예제(살충제 실험, 역학 연구)를 통해 실제 적용을 보여준다.

### Ch 5: Models for polytomous data (pp. 149-192)

**핵심**: 다범주 반응 데이터를 위한 모형을 다룬다. 순서형, 구간형, 명목형, 계층형 등 측정 척도별로 적절한 연결함수를 제시한다. 다항분포의 이론(모멘트, 일반화역행렬, 이차형식, 주변·조건부 분포)과 우도함수 기반 추정을 설명하며, 치즈 맛 실험과 탄광부 진폐증 예제를 포함한다.

**키워드**: `multinomial distribution`, `ordinal scale`, `nominal scale`, `proportional odds`, `measurement scale`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 5 (line 11131)

이 장은 다범주 반응 데이터를 위한 모형을 측정 척도별로 체계화한다. 순서형, 구간형, 명목형, 계층형 척도를 구분하고, 각 척도에 적합한 연결함수를 제시한다. 다항분포의 이론적 성질—모멘트, 일반화역행렬, 이차형식, 주변·조건부 분포—을 상세히 전개한다. 순서형 반응을 위한 누적 로짓 모형(비례 오즈 모형)과 인접 범주 로짓 모형을 정의하고, 비례 오즈 가정의 의미와 검정을 설명한다. 명목형 반응을 위한 기준 범주 로짓(baseline-category logit) 모형을 도입한다. 우도함수 기반 추정에서 반복 재가중 최소제곱 알고리즘의 적용과 수렴 성질을 논의한다. 치즈 맛 실험 데이터를 통해 순서형 반응의 적합과 해석을 시연하고, 탄광부 진폐증(pneumoconiosis) 데이터를 통해 누적 모형의 적용을 보여준다. 연속 비율 모형(continuation-ratio model)과 로그-감마 모형 등 대안적 연결함수를 소개한다. 다항 반응의 잔차 정의와 적합도 평가 방법을 논의하며, 이탈도와 Pearson χ²의 적합도 비교를 수행한다. 측정 척도의 선택이 모형의 효율성과 해석에 미치는 영향을 강조한다.

### Ch 6: Log-linear models (pp. 193-244)

**핵심**: 비율이 아닌 카운트 데이터를 위한 로그선형 모형을 다룬다. 포아송 분포의 성질과 로그우도함수, 과산포 처리를 설명한다. 로그선형 모형과 다항 반응 모형의 관계, 독립성·조건부 독립성, 정준상관모형, 다변량 회귀모형 등 다중 반응의 분석을 포괄적으로 기술한다.

**키워드**: `Poisson distribution`, `log-linear model`, `contingency table`, `independence`, `multiple responses`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 6 (line 13894)

이 장은 카운트 데이터를 위한 로그선형 모형을 포괄적으로 다룬다. 포아송 분포의 성질(모멘트, 로그우도, 충분통계량)을 기술하고, 정준 연결함수 η = log μ의 사용을 설명한다. 과산포 문제를 분산함수 V(μ) = μ(1+αμ)로 모형화하는 음이항 접근법을 제시한다. 로그선형 모형과 다항 반응 모형의 동치 관계—독립 포아송의 조건부 분포가 다항—를 증명한다. 이원 분할표에서의 독립성, 삼원 이상 분할표에서의 조건부 독립성, 균질적 연관(homogeneous association) 모형을 구분한다. 정준상관모형(canonical correlation model)을 행과 열 점수의 곱으로 정의하고, 연관 구조의 절약적 표현을 제시한다. 다변량 회귀모형으로의 확장을 통해 여러 반응변수의 동시 분석을 다룬다. 반복 비례 적합(iterative proportional fitting)과 IRLS의 관계를 설명한다. 이탈도와 Pearson χ² 통계량의 적합도 비교, 모형 선택에서 AIC의 역할을 논의한다. 다양한 예제(직업 이동 표, 건강 조사 데이터, 사회 이동 데이터)를 통해 로그선형 모형의 적합과 해석을 시연한다.

### Ch 7: Conditional likelihoods (pp. 245-284)

**핵심**: 장해 모수(nuisance parameter)가 존재할 때의 추론을 다룬다. 주변 우도, 조건부 우도, 프로파일 우도의 개념을 설명하고, 중심·비중심 초기하분포를 도출한다. 2x2 표에서의 이항확률 비교, 정보 결합, 대응 쌍 분석(명목·순서 반응) 등의 응용을 포함한다.

**키워드**: `conditional likelihood`, `marginal likelihood`, `hypergeometric distribution`, `nuisance parameter`, `matched pairs`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 7 (line 18288)

이 장은 장해 모수(nuisance parameter)가 존재할 때의 추론 전략을 다룬다. 주변 우도(marginal likelihood)를 장해 모수를 적분하여 제거하는 방법으로 정의하고, 조건부 우도(conditional likelihood)를 충분통계량에 조건을 부여하여 장해 모수를 소거하는 방법으로 구분한다. 프로파일 우도(profile likelihood)의 개념과 한계를 논의한다. 2×2 표에서 두 이항 확률의 비교를 위해 중심·비중심 초기하분포를 유도하고, Fisher의 정확 검정과의 관계를 설명한다. 조건부 우도를 사용한 오즈비 추정과 정확 신뢰구간 구성을 시연한다. 독립된 2×2 표들에서의 정보 결합 문제를 Mantel-Haenszel 추정량과 조건부 우도 방법으로 다룬다. 대응 쌍(matched pairs) 분석을 명목 반응과 순서 반응 각각에 대해 전개하며, McNemar 검정의 일반화를 제시한다. 층화(stratification)와 교란(confounding)의 처리에서 조건부 추론의 역할을 강조한다. Cox의 비례위험 모형에서 부분 우도(partial likelihood)의 개념을 조건부 우도의 특수 사례로 소개한다. 조건부 추론에서 앵커리(ancillarity)의 역할과 조건부 추정의 효율성 문제를 논의한다.

### Ch 8: Models with constant coefficient of variation (pp. 285-322)

**핵심**: 분산이 평균의 제곱에 비례하는 데이터(변동계수 일정)를 위한 모형을 다룬다. 감마 분포의 성질, 분산함수, 이탈도, 정준연결(역수), 로그연결(곱셈 모형), 항등연결(선형 모형) 등을 설명한다. 자동차 보험 청구, 혈액 응고 시간, 강수량 모형화, 초파리 발달률 등의 예제를 포함한다.

**키워드**: `gamma distribution`, `coefficient of variation`, `variance function`, `multiplicative model`, `inverse link`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 8 (line 20551)

이 장은 분산이 평균의 제곱에 비례하는(변동계수 일정) 데이터를 위한 감마 분포 모형을 다룬다. 감마 분포를 EY = μ, var Y = μ²/ν로 재모수화하고, 정준 연결(역수 η = 1/μ), 로그 연결(곱셈 모형 η = log μ), 항등 연결(선형 모형 η = μ)의 세 가지 연결함수를 설명한다. 분산함수 V(μ) = μ²와 이탈도 D = 2Σ{−log(yᵢ/μ̂ᵢ) + (yᵢ−μ̂ᵢ)/μ̂ᵢ}의 유도를 제시한다. 자동차 보험 청구 데이터를 로그 연결 감마 모형으로 분석하여 요인 효과의 곱셈적 해석을 시연한다. 혈액 응고 시간 데이터를 역수 연결로 적합하여 Michaelis-Menten형 포화 관계를 모형화한다. 강수량 데이터를 감마 모형(영과잉 포함)으로 분석하며, 정확한 영(zero)의 처리 문제를 논의한다. 초파리 발달률 데이터에 역수 연결을 적용하여 온도와 발달 시간의 역비례 관계를 모형화한다. 산포 모수의 추정에서 Pearson X²/(n−p) 추정량이 이탈도 기반 추정량보다 강건함을 강조한다. 감마 분포의 대수 정규 분포와의 유사성과 차이를 비교한다. 역가우시안 분포를 분산함수 V(μ) = μ³인 대안으로 간략히 소개한다.

### Ch 9: Quasi-likelihood functions (pp. 323-356)

**핵심**: 완전한 확률 모형을 가정하지 않고 평균-분산 관계만으로 추론하는 준우도(quasi-likelihood) 방법을 다룬다. 독립 관측과 종속 관측 각각에 대한 준우도 추정방정식을 유도하고, 최적 추정함수, 최적성 기준, 확장 준우도(extended quasi-likelihood)를 논의한다.

**키워드**: `quasi-likelihood`, `estimating equation`, `variance function`, `optimal estimating function`, `extended quasi-likelihood`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 9 (line 26005)

이 장은 완전한 확률분포를 가정하지 않고 평균-분산 관계만으로 추론하는 준우도(quasi-likelihood) 방법을 전개한다. 독립 관측에 대해 함수 U = (Y−μ)/{σ²V(μ)}가 로그우도 미분의 세 가지 핵심 성질—E(U)=0, var(U)=−E(∂U/∂μ)—을 공유함을 보인다. 준우도 Q(μ;y) = ∫(y−t)/{σ²V(t)}dt를 적분으로 정의하고, 다양한 분산함수에 대응하는 준우도를 표로 정리한다(정규, 포아송, 감마, 역가우시안, 이항, 음이항 등). 준-스코어 함수와 준-정보행렬의 구성, Newton-Raphson 반복 추정 절차를 설명하며, σ²에 대한 독립성을 보인다. 준우도 추정량의 점근적 비편향성과 정규성을 1단계 추정량의 선형 표현으로부터 증명한다. σ²의 추정을 일반화 Pearson 통계량 X²/(n−p)로 수행하며, 이는 이탈도 기반이 아님을 강조한다. 보리 잎 반점 데이터를 V(μ) = μ(1−μ)인 준이항 모형으로 분석하여 실제 적용을 시연한다. 최적 추정함수(optimal estimating function)의 개념을 소개하고, 준우도가 특정 조건 하에서 최적임을 보인다. 종속 관측을 위한 준우도 확장에서 상관 구조의 명세와 일반화추정방정식(GEE)의 연결을 논의한다. 확장 준우도(extended quasi-likelihood)를 σ²의 동시 추정을 위해 도입한다.

### Ch 10: Joint modelling of mean and dispersion (pp. 357-371)

**핵심**: 평균과 산포를 동시에 모형화하는 방법을 다룬다. 산포 모수가 공변량에 따라 체계적으로 변할 때의 모형 명세, 평균-산포 효과의 교호작용, 확장 준우도 기준, 첨도와 자유도에 대한 추정방정식 조정을 설명한다. 트럭용 판스프링 생산 예제를 통해 실제 적용을 보여준다.

**키워드**: `dispersion model`, `mean-dispersion interaction`, `extended quasi-likelihood`, `joint estimation`, `Taguchi methods`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 10 (line 28323)

이 장은 평균과 산포를 동시에 모형화하는 방법을 개발한다. 산포 모수 φ가 공변량에 따라 체계적으로 변할 때의 모형 명세 log φᵢ = Σfₖgₖᵢ를 정의한다. 평균 모형과 산포 모형의 교호작용, 즉 산포가 평균에 영향을 미치고 그 역도 성립하는 상황을 논의한다. 확장 준우도(extended quasi-likelihood) Q⁺ = −½{D(y;μ)/φ + log(2πφV(y))}를 산포 모수 추정의 기준으로 사용한다. 감마 GLM을 산포 모형에 적용하여 이탈도 성분 dᵢ를 감마 분포의 반응으로 취급하는 절차를 설명한다. 첨도(kurtosis)에 의한 자유도 조정—특히 정규 분포(κ₄=3)와 비정규 분포에서의 차이—을 논의한다. 트럭용 판스프링 생산 데이터를 사용하여 평균과 산포의 동시 모형화를 시연하며, Taguchi의 품질 공학 방법론과의 연결을 설명한다. 반복 적합 절차—평균 모형 적합 후 잔차의 산포 모형 적합을 반복—의 알고리즘을 기술한다. 감마 이탈도 성분의 분포적 성질과 χ² 근사의 정확도를 논의한다. 산포 모형에서의 모형 선택과 검정 절차를 이탈도 차이와 F-검정으로 수행한다. 이 접근법이 Nelder와 Lee의 이후 연구(결합 GLM)로 발전한 배경을 언급한다.

### Ch 11: Models with additional non-linear parameters (pp. 372-390)

**핵심**: 분산함수, 연결함수, 또는 공변량에 미지의 비선형 모수가 포함된 모형을 다룬다. Box-Cox 변환의 일반화로서 연결함수 내 모수 추정, 데이터 변환과 적합값 변환의 비교, 비선형 공변량 항의 처리를 논의한다. 비료 효과, 살충제·상승제 분석, 약물 혼합 등의 예제를 포함한다.

**키워드**: `non-linear parameter`, `Box-Cox transformation`, `link parameter`, `variance function parameter`, `non-linear covariates`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 11 (line 29407)

이 장은 분산함수, 연결함수, 또는 공변량에 미지의 비선형 모수가 포함된 모형을 다룬다. Box-Cox 변환 y^(λ) = (y^λ − 1)/λ를 연결함수 내 모수 추정의 일반적 틀로 확장하며, 데이터 변환과 적합값 변환의 중요한 차이를 설명한다. 연결함수에 미지 모수가 포함된 경우의 프로파일 우도 구성과 최적 연결의 탐색 방법을 제시한다. 분산함수 V(μ) = μ^ζ에서 멱지수 ζ의 추정 문제를 다루며, 트위디(Tweedie) 분포족과의 관계를 논의한다. 비선형 공변량 항의 처리—예: 용량-반응 관계에서의 비선형 모수—를 위한 수정된 IRLS 절차를 설명한다. 비료 효과 데이터에서 Mitscherlich 성장 곡선의 비선형 모수 추정을 시연한다. 살충제·상승제(synergist) 분석에서 두 약물의 결합 효과 모형화를 다루며, 상호작용의 비선형 표현을 제시한다. 약물 혼합(drug mixture) 설계에서의 등효과선(isobole) 분석을 포함한다. 추정 절차에서 프로파일 우도의 비이차성(non-quadraticity)과 이로 인한 표준오차 근사의 한계를 논의한다. 비선형 모수의 존재가 정규 방정식의 구조를 변화시키며 수렴 속도를 저하시킬 수 있음을 지적한다.

### Ch 12: Model checking (pp. 391-418)

**핵심**: 모형 진단의 체계적 전략을 제시한다. 스코어 검정, 평활화, 잔차를 이용한 비공식적 검사를 소개하고, 분산함수·연결함수·공변량 척도에 대한 체계적 이탈 검사와 레버리지·일관성·영향력 측도를 이용한 개별 이상점 검사를 구분한다. 당근 피해, Minitab 나무, 보험 청구 예제를 포함한다.

**키워드**: `residual`, `leverage`, `influence`, `score test`, `model diagnostics`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 12 (line 30747)

이 장은 모형 진단의 체계적 전략을 세 범주로 구분하여 제시한다. 비공식적 검사로서 스코어 검정(score test), 부분잔차 평활, 잔차 그림 등을 소개한다. 체계적 이탈(systematic departure) 검사를 분산함수·연결함수·공변량 척도의 세 차원에서 수행하며, 분산함수 검사를 위한 비정수 멱(non-constant power) 검정을 제시한다. 개별 이상점(individual aberrance) 검사를 레버리지(hat 행렬의 대각 원소 hᵢ), 일관성(consistency: 삭제 잔차), 영향력(influence: Cook 거리)의 세 가지 측도로 구분한다. 잔차의 여러 유형—응답(response), Pearson, 이탈도, Anscombe, 표준화—의 정의와 상대적 장점을 비교한다. 추가 변수 그림(added-variable plot)과 부분잔차 그림(partial-residual plot)을 모형 명세의 개선 도구로 제시한다. 당근 피해(carrot damage) 데이터를 사용하여 포아송 모형의 진단 과정을 시연하고, 과산포 발견 시의 대응을 설명한다. Minitab 나무 데이터를 통해 연결함수 선택의 진단을 보여준다. 보험 청구(motor insurance claims) 데이터를 감마 모형으로 분석하며, 이상점 탐지와 영향력 분석을 수행한다. 시뮬레이션 기반 잔차 검정의 가능성을 논의한다. 모형 진단이 모형 적합과 함께 반복적으로 수행되어야 하는 순환적 과정임을 강조한다.

### Ch 13: Models for survival data (pp. 419-431)

**핵심**: 생존 시간 데이터의 분석을 다룬다. 생존함수와 위험함수의 정의, 비례위험 모형, 지수·와이블·극치값 분포를 가정한 모수적 추정, Cox의 비례위험 모형과 부분 우도(partial likelihood), 동률 처리 방법을 설명한다. 백혈병 관해 시간 예제를 포함한다.

**키워드**: `survival function`, `hazard function`, `proportional hazards`, `Cox model`, `partial likelihood`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 13 (line 32661)

이 장은 생존 시간 데이터의 분석을 GLM의 틀 안에서 다룬다. 생존함수 S(t) = P(T > t)와 위험함수(hazard function) h(t) = f(t)/S(t)의 정의와 상호 관계를 설명한다. 비례위험 모형 h(t|x) = h₀(t)exp(xᵀβ)를 도입하고, 지수·와이블·극치값 분포를 가정한 모수적 추정을 전개한다. 와이블 분포가 로그 변환 하에서 극치값 분포가 되며, 이를 GLM으로 적합할 수 있음을 보인다. Cox의 비례위험 모형에서 기저 위험함수 h₀(t)를 비모수적으로 처리하고, 부분 우도(partial likelihood)를 사용한 β의 추정을 설명한다. 동률(tied observations) 처리를 위한 Breslow와 Cox의 근사 방법을 제시한다. 중도절단(censoring)의 유형(1형, 2형, 무작위)과 각 경우의 우도 구성을 다룬다. 백혈병 관해 시간(remission time) 데이터를 사용하여 모수적·비모수적 모형의 적합과 비교를 시연한다. 구간 중도절단 데이터를 이항 GLM으로 변환하여 분석하는 방법을 설명한다. 비례위험 가정의 검정과 잔차 진단을 논의한다. 가속 고장 시간(accelerated failure time) 모형과 비례위험 모형의 관계를 설명한다.

### Ch 14: Components of dispersion (pp. 432-454)

**핵심**: 관측값이 독립이 아닌 계층적 구조(예: 학교-교실-학생)를 가질 때의 분산 성분 모형을 다룬다. 선형모형과 비선형모형에서의 분산 성분 추정을 설명하고, 도롱뇽 교배 실험 예제를 통해 랜덤 효과가 포함된 로지스틱 모형의 산포 모수 추정을 보여준다.

**키워드**: `variance components`, `random effects`, `hierarchical data`, `intraclass correlation`, `salamander mating`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 14 (line 33374)

이 장은 관측값이 독립이 아닌 계층적 구조(예: 학교-교실-학생)를 가질 때의 분산 성분 모형을 다룬다. 선형모형에서의 분산 성분 추정을 ANOVA 방법(기대 평균제곱의 등치)과 REML(제한최대우도)의 두 접근법으로 설명한다. 균형 설계에서 ANOVA 추정량의 명시적 형태를 유도하고, 불균형 설계에서의 모호성 문제를 논의한다. 급내상관계수(intraclass correlation) ρ = σ²ₐ/(σ²ₐ+σ²ₑ)의 해석과 추정을 설명한다. 비선형모형(GLM)에서의 분산 성분 추정 문제를 소개하며, 정규 분포 가정이 성립하지 않는 경우 적분이 필요한 어려움을 지적한다. 도롱뇽 교배(salamander mating) 실험 데이터를 이항 GLMM의 주요 예제로 사용하여, 교차 랜덤효과(crossed random effects) 구조에서의 산포 모수 추정을 시연한다. 벌점 준우도(penalized quasi-likelihood, PQL) 접근법을 GLMM의 근사적 추정 방법으로 제시한다. 분산 성분의 가설 검정에서 경계 모수(boundary parameter) 문제—σ² = 0이 모수 공간의 경계—에 의한 χ² 검정의 비표준적 분포를 설명한다. 중첩(nested)과 교차(crossed) 랜덤효과 구조의 구분과 각각의 모형 명세를 다룬다. 분산 성분 모형과 반복측정 설계의 관계를 논의한다.

### Ch 15: Further topics (pp. 455-468)

**핵심**: 추가적인 고급 주제를 간략히 다룬다. 최대우도 추정량의 편향 교정(정준 연결과 비정준 모형), Bartlett 조정의 계산, 일반화가법모형(GAM)의 적합 알고리즘과 평활 방법을 소개한다.

**키워드**: `bias correction`, `Bartlett adjustment`, `generalized additive model`, `smoothing`, `exponential regression`

**상세**: → `McCullagh & Nelder - Generalized Linear Models (2nd Ed.).md` Ch 15 (line 35555)

이 장은 세 가지 고급 주제를 다룬다. 첫째, 최대우도 추정량의 편향 교정을 정준 연결 모형과 비정준 모형으로 나누어 설명한다. 정준 연결에서 편향 벡터 b = −½κʳˢκᵗᵘκₛ,ₜ,ᵤ를 텐서 표기로 유도하고, 이를 보조 회귀(supplementary regression)로 간단히 계산할 수 있음을 보인다. 비정준 모형에서는 역연결함수의 이차 미분 μ″/μ′을 사용하여 수정된 형식 응답 벡터 ξᵢ를 구성한다. 도마뱀 데이터로 편향 교정의 실제 크기(표준오차의 약 10%)를 시연한다. 둘째, Bartlett 조정을 우도비 통계량의 기대값 보정으로 정의하고, 조정된 통계량 Λ′ = Λ/(1+b)가 χ² 분포에 O(n⁻²)까지 일치함을 보인다. 복합 귀무가설에 대한 Bartlett 조정 인수 bₚq = (pb_p − qb_q)/(p−q)의 계산과 GLM에서의 구체적 공식을 제시한다. 셋째, 일반화가법모형(GAM)을 선형예측자의 평활 함수 확장 η = Σsⱼ(xⱼ)로 정의하고, 국소 스코어링(local scoring) 알고리즘에 의한 적합 절차를 설명한다. 평활 방법의 선택(커널, 스플라인, loess)과 평활도의 제어를 논의한다. 지수 회귀(exponential regression)에서의 추가적 고려 사항을 포함하며, 표본 크기가 작을 때의 이론과 실제의 괴리를 경고한다.
