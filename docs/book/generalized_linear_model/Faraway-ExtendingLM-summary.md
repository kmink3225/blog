---
name: "Extending the Linear Model with R"
type: book-summary
source_file: "Faraway-ExtendingLM_azure_full.md"
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

이 장은 선형모형의 기본 개념과 R 사용법을 복습하며, 2000년 미국 대선 조지아주 투표 데이터를 분석 예제로 활용한다. 반응변수(미투표율)와 예측변수(투표 장비, 경제 수준, 아프리카계 미국인 비율, 도시/농촌 구분) 사이의 관계를 탐색한다. R의 lm 함수를 사용하여 최소제곱 추정, 회귀계수 해석, 결정계수(R²), F-검정, t-검정, 신뢰구간 계산을 시연한다. 질적 예측변수를 위한 더미변수 코딩(처리 대비)과 교호작용 항의 해석 방법을 설명한다. 잔차 대 적합값 그림, QQ 그림, Cook 통계량, 레버리지 등 진단 방법을 소개한다. 강건 회귀(Huber 방법)와 가중최소제곱을 대안적 적합 방법으로 제시한다. 반응변수 변환(Box-Cox 방법)과 예측변수 변환(직교 다항식, B-스플라인)을 다루며, 변환의 해석적 어려움을 논의한다. AIC 기반 단계적 변수 선택과 F-검정 기반 변수 선택을 비교하며, 위계 원칙의 중요성을 강조한다. 최종 모형에서 경제 수준이 미투표율의 가장 명확한 예측인자이며, 투표 장비와 인종 구성의 효과는 교호작용에 의존한다는 결론을 도출한다. 이 책의 세 가지 확장 방향—GLM(반응변수의 일반화), 혼합효과(오차구조의 일반화), 비모수회귀(예측변수의 일반화)—을 개관한다.

### Ch 2: Binomial Data (pp. 28-60)

**핵심**: 이항 반응 데이터의 모형화를 다룬다. 챌린저 우주왕복선 O-링 사고 데이터를 시작으로 로지스틱 회귀, 모형 해석(오즈비), 모형 적합도 검정, 과산포 처리, 프로빗·보완로그-로그 모형 등을 R 코드와 함께 설명한다. 그룹 데이터와 개별 데이터의 처리 방식 차이도 다룬다.

**키워드**: `logistic regression`, `odds ratio`, `Challenger disaster`, `probit`, `complementary log-log`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 2 (line 3704)

이 장은 1986년 챌린저 우주왕복선 O-링 사고 데이터를 시작으로 이항 반응 데이터의 모형화를 다룬다. 이항분포 B(n,p)에서 출발하여 선형예측자와 연결함수의 개념을 도입하고, 로짓·프로빗·보완로그-로그의 세 가지 연결함수를 비교한다. 최대우도 추정과 이탈도(deviance) 기반 검정을 개발하며, 이탈도의 χ² 근사의 한계(특히 이진 반응에서)를 논의한다. 관용분포(tolerance distribution) 개념을 통해 프로빗 연결의 이론적 동기를 설명한다. 오즈비의 해석, 상대위험도와의 비교, 전향적·후향적 표본추출에서 로짓 모형의 동일한 결과를 보인다. 과산포(overdispersion) 문제를 군집화와 이질성의 관점에서 설명하고, 산포 모수 σ²의 추정과 F-검정 사용을 제시한다. 유효용량(ED50, LD50)의 추정과 델타 방법을 이용한 표준오차 계산을 시연한다. 완전 분리(linear separability) 상황에서의 추정 문제와 Firth의 편향 축소 방법을 소개한다. 적합도 측정으로 Pearson X² 통계량과 Nagelkerke R²를 제시한다. 대응 환자-대조군 연구를 위한 조건부 로지스틱 회귀를 생존분석 소프트웨어를 이용하여 적합하는 방법을 시연한다. 영아 호흡기 질환 데이터와 소아 백혈병 방사선 노출 데이터를 예제로 사용한다.

### Ch 3: Count Regression (pp. 61-75)

**핵심**: 카운트 반응변수를 위한 회귀 모형을 다룬다. 포아송 회귀의 정의와 적합, 포아송 분포의 발생 맥락(드문 사건의 이항 근사, 사건 발생률, 분할표), 비율 모형, 과산포 처리, 음이항 회귀를 설명한다.

**키워드**: `Poisson regression`, `rate model`, `over-dispersion`, `negative binomial`, `count data`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 3 (line 6779)

이 장은 카운트 반응변수를 위한 포아송 회귀 모형을 개발한다. 포아송 분포가 자연적으로 발생하는 세 가지 맥락—이항의 드문 사건 근사, 독립적 사건 발생률, 지수분포 대기시간—을 설명한다. 로그 연결함수를 사용하여 μ > 0을 보장하며, 최대우도 추정의 정규방정식이 이항 회귀와 동일한 형태(X^T y = X^T μ̂)임을 보인다. 갈라파고스 군도 거북 종 수 데이터를 사용하여 선형모형(제곱근 변환)과 포아송 GLM을 비교한다. 이탈도와 Pearson X² 통계량을 적합도 검정에 사용하며, 반정규(half-normal) 잔차 그림으로 이상점을 검사한다. 포아송 분포의 평균-분산 동등 가정이 위반될 때 발생하는 과산포를 진단하고, 산포 모수 φ̂ = X²/(n-p)를 추정하여 표준오차를 조정하는 방법을 제시한다. 비율 모형(rate model)에서 오프셋 항(log t)의 사용과 해석을 설명한다. 음이항 회귀를 과산포의 대안적 모형으로 소개하며, 감마 혼합 포아송으로부터의 유도를 보인다. R의 glm 함수와 MASS 패키지의 glm.nb 함수를 사용한 실습을 포함한다. 영과잉(zero-inflated) 데이터에 대한 간략한 논의도 포함한다.

### Ch 4: Contingency Tables (pp. 76-105)

**핵심**: 교차분류 범주형 데이터의 분석을 다룬다. 2x2 표에서의 독립성 검정, 오즈비, 쌍 대응 데이터부터 시작하여 다원 분할표의 로그선형 모형, Simpson의 역설, 순서형 자료 처리, 큰 분할표에서의 모형 선택까지 포괄한다.

**키워드**: `contingency table`, `log-linear model`, `independence`, `odds ratio`, `Simpson's paradox`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 4 (line 8304)

이 장은 교차분류 범주형 데이터의 분석을 위한 분할표 방법론을 다룬다. 2×2 표에서의 네 가지 표본추출 방식—포아송, 다항, 이항, 초기하—이 모두 동일한 독립성 검정 결과를 산출함을 보인다. 포아송 모형에서 가법 모형(교호작용 없음)이 독립성 가정과 동치이며, 적합값이 주변합의 함수임을 설명한다. Pearson X² 통계량, 이탈도 기반 검정, Fisher의 정확 검정을 비교하고, Yates의 연속성 교정을 소개한다. 오즈비를 연관성의 측도로 정의하고 정확 신뢰구간을 계산한다. 다원 분할표로 확장하여 로그선형 모형 log μ = γ + αᵢ + βⱼ + (αβ)ᵢⱼ의 체계를 설명한다. Simpson의 역설을 UC 버클리 대학원 입학 데이터로 시연하며, 교란변수를 포함한 모형의 중요성을 강조한다. 순서형 자료에 대해 선형 대비와 비선형 성분의 분해를 다루고, 큰 분할표에서의 모형 선택(AIC, 단계적 방법)을 설명한다. 쌍 대응(matched pairs) 데이터를 위한 McNemar 검정과 대칭 모형을 소개한다. R의 xtabs, glm, fisher.test 함수와 mosaic plot, dotchart 등의 시각화를 활용한다.

### Ch 5: Multinomial Data (pp. 106-125)

**핵심**: 다항 반응 데이터의 모형화를 다룬다. 명목형 반응을 위한 다항 로짓 모형과 순서형 반응을 위한 비례 오즈 모형을 구분하여 설명한다. 다항분포의 정의에서 출발하여 모형 적합, 해석, R 코드를 사용한 실습을 포함한다.

**키워드**: `multinomial logit`, `proportional odds`, `ordinal data`, `nominal data`, `categorical response`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 5 (line 10990)

이 장은 다항분포의 정의에서 출발하여 명목형과 순서형 다범주 반응 데이터의 모형화를 다룬다. 다항 로짓 모형에서 기준 범주(baseline category)를 설정하고 log(pᵢⱼ/pᵢ₁) = xᵢᵀβⱼ의 형태로 확률을 선형예측자에 연결한다. 1996년 미국 선거 조사(NES) 데이터를 사용하여 정당 지지(민주·독립·공화)를 소득, 교육, 나이로 예측하는 모형을 적합한다. nnet 패키지의 multinom 함수로 최대우도 추정을 수행하고, AIC 기반 단계적 모형 선택으로 소득만 남는 모형을 도출한다. 우도비 검정으로 교육의 유의성을 평가하며, 계수의 로그-오즈 해석과 예측 확률 계산을 시연한다. 다항 로짓 모형을 포아송 GLM으로 변환하여 적합할 수 있음을 보이며, 독립 포아송의 조건부 분포가 다항분포임을 이용한다. 순서형 반응을 위한 비례 오즈 모형(proportional odds model) cumulative logit P(Y ≤ j) = αⱼ + xᵀβ를 정의하고, MASS 패키지의 polr 함수로 적합한다. 비례 오즈 가정의 검정과 해석을 설명하며, 순서형 자료에서 명목형 모형 대비 비례 오즈 모형의 절약성(parsimony) 이점을 논의한다. 예측 확률의 시각화와 신뢰구간 구성을 포함한다.

### Ch 6: Generalized Linear Models (pp. 126-148)

**핵심**: 이전 장들에서 다룬 개별 모형들을 GLM이라는 통합 틀로 묶어 이론적으로 정리한다. 지수족 분포의 일반적 형태, 연결함수의 정의, 모형 적합을 위한 IRLS 알고리즘, 이탈도와 잔차, 대가설 검정을 다루며, Nelder와 Wedderburn(1972)의 원래 논문을 참조한다.

**키워드**: `exponential family`, `canonical parameter`, `IRLS`, `deviance`, `link function`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 6 (line 12922)

이 장은 이전 장들의 개별 모형을 GLM이라는 통합적 틀로 정리한다. 지수족 분포의 일반적 형태 f(y|θ,φ) = exp[(yθ−b(θ))/a(φ)+c(y,φ)]를 정의하고, 정규·포아송·이항 분포가 이 형태의 특수 사례임을 보인다. 정준 모수 θ와 산포 모수 φ의 역할을 설명하며, 평균 μ = b′(θ)와 분산 var Y = b″(θ)a(φ)의 관계를 유도한다. 연결함수 g(μ) = η의 개념을 정의하고, 정준 연결(정규: 항등, 포아송: 로그, 이항: 로짓, 감마: 역수, 역가우시안: μ⁻²)을 표로 정리한다. IRLS(반복 재가중 최소제곱) 알고리즘을 직관적으로 유도하며, 조정 종속변수 z와 가중치 w의 계산 과정을 Bliss 데이터로 명시적으로 구현하여 시연한다. 이탈도를 포화 모형과 관심 모형의 우도비 통계량으로 정의하고, 정규·포아송·이항·감마·역가우시안의 이탈도 공식을 제시한다. 적합도 검정(이탈도의 χ² 근사)과 중첩 모형 비교(이탈도 차이)의 두 가지 가설 검정 유형을 구분한다. 산포 모수를 추정해야 하는 경우 F-통계량 사용의 필요성을 설명한다. 잔차 진단(이탈도 잔차, Pearson 잔차, 작업 잔차)과 레버리지, 영향력 측도를 포함한다.

### Ch 7: Other GLMs (pp. 149-168)

**핵심**: 이항·정규·포아송 이외의 GLM을 다룬다. 감마 GLM(연속 양의 비대칭 반응), 역가우시안 GLM, 이중 GLM(평균과 분산의 동시 모형화), 준-GLM(분포 미지정, 연결함수와 분산함수만 지정)을 소개한다.

**키워드**: `gamma GLM`, `inverse Gaussian`, `dual GLM`, `quasi-GLM`, `dispersion modeling`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 7 (line 14722)

이 장은 이항·정규·포아송 외의 GLM을 다룬다. 감마 분포의 재모수화 EY = μ, var Y = μ²/ν를 통해 변동계수가 일정한 데이터에 적합한 GLM을 구성한다. 정준 연결(역수), 로그 연결(곱셈적 효과), 항등 연결(분산 성분)의 세 가지 연결함수를 비교한다. 반도체 저항 데이터를 사용하여 로그 변환 정규 모형과 감마 GLM(로그 연결)의 적합 결과가 거의 동일함을 보인다. 역가우시안 GLM을 var Y ∝ μ³인 데이터를 위해 소개하며, 정준 연결 η = μ⁻²와 분산함수를 설명한다. 이중 GLM(dual GLM)을 평균과 분산의 동시 모형화를 위해 도입하고, 감마 GLM으로 이탈도 잔차의 제곱을 분산 모형에 적합하는 절차를 기술한다. Taguchi 방법론과의 연결을 논의하며, 판스프링 데이터로 평균-분산 최적화 문제를 시연한다. 준-GLM(quasi-GLM)을 완전한 확률분포를 가정하지 않고 연결함수와 분산함수만으로 추론하는 방법으로 소개한다. 준-GLM에서도 IRLS 알고리즘이 동일하게 적용됨을 보이며, 과산포 이항 및 포아송 모형에서의 실용성을 강조한다. R의 family=Gamma, family=inverse.gaussian, family=quasi 옵션을 사용한 실습을 포함한다. 트위디(Tweedie) 분포족에 대한 간략한 언급도 포함한다.

### Ch 8: Random Effects (pp. 169-202)

**핵심**: 그룹화된 데이터를 위한 랜덤효과 모형을 도입한다. 고정효과와 랜덤효과의 개념적 구분, 단일 그룹 요인의 랜덤효과 모형, 중첩(nested) 설계, 교차(crossed) 설계, 다수준 모형의 적합과 추론을 R의 lme4 패키지를 통해 시연한다.

**키워드**: `random effects`, `fixed effects`, `nested design`, `crossed design`, `multilevel model`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 8 (line 16839)

이 장은 그룹화된 데이터를 위한 랜덤효과 모형을 도입한다. 고정효과(추정 대상인 미지 상수)와 랜덤효과(추정 대상이 아닌 확률변수)의 개념적 구분을 설명하고, 혼합효과 모형 y = Xβ + Zγ + ε의 행렬 표현을 제시한다. 급내상관계수(ICC) ρ = σ²ₐ/(σ²ₐ+σ²ₑ)가 랜덤효과에 의한 관측값 간 상관을 유도함을 보인다. ANOVA 추정량의 단점(음수 분산 추정, 불균형 설계에서의 모호성)을 지적하고, 최대우도(ML)와 제한최대우도(REML) 추정의 우월성을 설명한다. 제지 공장 밝기 데이터로 aov(고정효과)와 lme4 패키지의 lmer(랜덤효과)를 비교하며, 균형 설계에서 REML과 ANOVA 추정이 일치함을 확인한다. 중첩(nested) 설계를 학교-교실 다수준 구조로, 교차(crossed) 설계를 라틴 방격과 실험 블록으로 설명한다. 분산 성분의 유의성 검정에서 χ² 근사, 정확 검정, 부트스트랩의 세 가지 접근법을 비교한다. 랜덤효과의 예측값(BLUP: 최적선형비편향예측)의 계산과 해석을 설명한다. lme4 패키지의 모형 명세 문법—(1|group)은 랜덤 절편, (x|group)은 랜덤 기울기—을 상세히 설명한다. 음료 배달 시간, 반도체 생산, 수면 연구 등 다양한 실험 설계의 예제를 포함한다.

### Ch 9: Repeated Measures and Longitudinal Data (pp. 203-220)

**핵심**: 반복측정 및 종단 데이터를 위한 혼합효과 모형을 다룬다. 개체 내 상관을 고려한 모형 구조(고정효과 + 랜덤효과 + 오차)를 정의하고, 오차의 공분산 구조 모형화, 시계열적 상관 구조 등을 포함한다.

**키워드**: `repeated measures`, `longitudinal data`, `mixed effects model`, `covariance structure`, `panel study`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 9 (line 20308)

이 장은 반복측정 및 종단 데이터를 위한 혼합효과 모형을 다룬다. 개체 내 반응벡터를 yᵢ|γᵢ ~ N(Xᵢβ+Zᵢγᵢ, σ²Λᵢ)로 모형화하며, 오차 공분산 Λᵢ의 일반화를 허용한다. PSID(소득역학 패널 조사) 데이터를 사용하여 85명의 1968-1990년 소득 변화를 분석한다. 반응특성분석(response feature analysis)으로 개인별 절편과 기울기를 추출하여 성별 비교를 수행하는 간단한 접근법을 시연한다. 랜덤 절편과 랜덤 기울기를 포함한 혼합효과 모형을 lmer로 적합하고, 성별·나이·교육과 시간의 교호작용을 검정한다. 오차의 공분산 구조 모형화를 위해 nlme 패키지의 lme 함수를 사용하여 AR(1), 복합대칭 등의 상관 구조를 비교한다. 시트 데이터(치과 성장 곡선)를 사용하여 시간에 따른 성장 패턴의 성별 차이를 분석한다. 고정효과의 검정에서 근사적 F-검정과 자유도 계산(Kenward-Roger, Satterthwaite)의 어려움을 논의한다. 모형 선택에서 AIC/BIC의 사용과 REML 대 ML의 적절한 사용 시점을 설명한다. 분산 성분의 신뢰구간을 프로파일 우도와 부트스트랩으로 구성하는 방법을 시연한다. 종단 데이터에서 시변 공변량(time-varying covariates)의 처리를 포함한다.

### Ch 10: Mixed Effect Models for Nonnormal Responses (pp. 221-231)

**핵심**: GLM과 랜덤효과를 결합한 일반화선형혼합모형(GLMM)을 다룬다. 지수족 반응에 랜덤효과를 추가하는 모형 구조, 우도함수의 적분 문제, 근사 추정 방법(PQL, Laplace, 구적법)을 설명하고 R에서의 실습을 포함한다.

**키워드**: `GLMM`, `generalized linear mixed model`, `PQL`, `Laplace approximation`, `random effects`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 10 (line 22109)

이 장은 GLM과 랜덤효과를 결합한 일반화선형혼합모형(GLMM)을 다룬다. 지수족 반응에 랜덤효과를 추가하면 우도함수에 적분이 포함되어 해석적 계산이 불가능해지는 문제를 설명한다. 균형 실험(표면·시각 조건에서의 자세 안정성) 데이터를 사용하여 이진 반응에 대한 피험자 랜덤효과의 필요성을 이탈도 검정으로 확인한다. 고정 피험자 효과 모형에서 완전 분리와 식별 불가능 문제가 발생함을 보이고, 편향 축소 로지스틱 회귀(brlr)를 대안으로 제시한다. GLMM의 세 가지 근사 추정법—벌점 준우도(PQL), 라플라스 근사, 가우스-에르미트 구적법—을 비교하며, PQL은 편향이 크고 구적법은 정확하지만 계산 비용이 높음을 설명한다. lme4 패키지의 glmer 함수로 이항 GLMM을 적합하고 결과를 해석한다. 피험자별 랜덤효과의 예측값을 추출하여 개인 차이를 시각화한다. GEE(일반화추정방정식)를 주변(marginal) 모형의 대안으로 간략히 소개하고, GLMM(조건부 모형)과의 차이를 논의한다. 포아송 반응에 대한 GLMM 적용을 간암 발생률 데이터로 시연한다. 순서형 반응에 대한 혼합효과 모형으로의 확장 가능성을 언급한다.

### Ch 11: Nonparametric Regression (pp. 232-253)

**핵심**: 단변량 비모수 회귀 방법을 다룬다. 커널 평활법, 스플라인(평활 스플라인, 회귀 스플라인), 국소 다항식 회귀(loess), 파동함수(wavelet) 방법을 비교하고, 평활 모수 선택(교차검증, GCV 등)과 신뢰 구간 문제를 설명한다.

**키워드**: `kernel smoothing`, `spline`, `loess`, `bandwidth selection`, `cross-validation`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 11 (line 23611)

이 장은 단변량 비모수 회귀 방법을 체계적으로 다룬다. 모수적 접근(유한 개의 모수로 f를 지정)과 비모수적 접근(매끄러운 함수 클래스에서 f를 선택)의 장단점을 비교한다. 핵 추정량(kernel estimator)으로서 Nadaraya-Watson 추정량을 정의하고, Epanechnikov 핵의 최적성과 대역폭(bandwidth) 선택의 중요성을 설명한다. 비모수 추정의 최적 MSE가 O(n⁻⁴/⁵)로 모수적 O(n⁻¹)보다 느리지만, 모형 오지정 시 모수적 MSE가 O(1)에 머무름을 지적한다. 평활 스플라인을 조도 벌점(roughness penalty) ∫f″(x)²dx의 최소화로 정의하고, 평활 모수 λ의 역할을 설명한다. 회귀 스플라인(B-스플라인, 자연 스플라인)에서 매듭(knot)의 수와 위치 선택 문제를 다룬다. 국소 다항식 회귀(loess)를 국소 가중 최소제곱의 관점에서 설명하고, span 모수에 의한 평활도 조절을 시연한다. 교차검증(leave-one-out CV)과 일반화교차검증(GCV)을 대역폭·평활 모수 선택의 자동화 방법으로 제시한다. 파동함수(wavelet) 방법을 불연속점이나 급격한 변화가 있는 함수에 적합한 대안으로 간략히 소개한다. Old Faithful 간헐천 데이터와 시뮬레이션 데이터(exa, exb)를 사용하여 각 방법의 성능을 비교한다. 신뢰 구간의 구성과 점별(pointwise) 대 동시(simultaneous) 구간의 구분을 논의한다.

### Ch 12: Additive Models (pp. 254-277)

**핵심**: 다변량 비모수 회귀를 위한 가법모형을 다룬다. 선형모형과 완전 비모수 모형의 절충으로서 가법모형을 정의하고, 역적합(backfitting) 알고리즘, 일반화가법모형(GAM), 다변량 적응 회귀 스플라인(MARS) 등을 R에서 실습한다.

**키워드**: `additive model`, `GAM`, `backfitting`, `MARS`, `multivariate smoothing`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 12 (line 25085)

이 장은 다변량 비모수 회귀를 위한 가법모형 y = β₀ + Σfⱼ(xⱼ) + ε를 다룬다. 선형모형과 완전 비모수 모형 사이의 절충으로서 가법모형의 위치를 설명하며, 차원의 저주를 우회하면서도 각 예측변수의 주변적 관계를 해석할 수 있는 장점을 강조한다. 역적합(backfitting) 알고리즘을 부분잔차에 대한 반복적 평활로 정의하고, 수렴 조건을 설명한다. R의 gam 패키지(Hastie-Tibshirani 방식, loess 평활 사용)와 mgcv 패키지(Wood 방식, 벌점 스플라인 사용, 자동 평활 모수 선택)의 두 가지 적합 방법을 비교한다. LA 오존 농도 데이터를 사용하여 선형모형(R² = 0.65)과 가법모형(R² ≈ 0.72)의 적합도를 비교하고, 변환함수의 형태를 부분잔차 그림으로 시각화한다. 일반화가법모형(GAM)을 지수족 반응에 대한 가법모형의 확장으로 소개하며, 이항 GAM과 포아송 GAM의 적합을 시연한다. 다변량 적응 회귀 스플라인(MARS)을 구간선형 기저함수의 곱으로 정의하고, earth 패키지로 적합하는 방법을 설명한다. MARS의 교호작용 차수 제한 기능과 변수 중요도 평가를 논의한다. 모형 선택에서 GCV와 AIC의 사용을 설명하고, 가법 구조의 가정이 강한 교호작용 존재 시 적절하지 않음을 지적한다. 범주형 예측변수와 연속형 예측변수의 혼합 처리를 포함한다.

### Ch 13: Trees (pp. 278-295)

**핵심**: 의사결정나무 방법론을 다룬다. 회귀나무와 분류나무의 구성 원리, 가지치기(pruning), 배깅(bagging), 랜덤 포레스트, 부스팅 등 앙상블 방법을 소개한다. 통계학과 기계학습 양쪽의 나무 방법론 발전을 개관한다.

**키워드**: `regression tree`, `classification tree`, `pruning`, `random forest`, `boosting`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 13 (line 27857)

이 장은 의사결정나무 방법론을 통계학과 기계학습 양쪽의 관점에서 다룬다. 재귀 분할(recursive partitioning) 알고리즘—예측변수 축에 평행한 분할로 RSS를 최소화—의 절차를 단계별로 설명한다. LA 오존 농도 데이터에 rpart 패키지를 적용하여 나무를 구성하고, 온도가 첫 번째 분할 변수로 선택되어 RSS를 21,000에서 9,600으로 감소시킴을 보인다. 나무 그림의 두 가지 표현(오차 감소에 비례한 깊이, 균일 깊이)을 비교한다. 범주형 예측변수의 분할(순서형: L−1개, 비순서형: 2^(L−1)−1개)과 결측값 처리(대리 분할) 방법을 설명한다. 과적합 방지를 위한 가지치기(pruning)를 비용-복잡도 기준 Cα(T) = RSS(T) + α|T|로 정의하고, 교차검증으로 최적 α를 선택한다. 분류나무에서의 불순도 측도(지니 지수, 교차 엔트로피)와 잘못 분류율을 비교한다. 배깅(bagging)을 부트스트랩 앙상블로 소개하고, 예측 분산의 감소 효과를 설명한다. 랜덤 포레스트를 각 분할에서 예측변수의 무작위 부분집합만 고려하는 방법으로 정의하고, randomForest 패키지로 적합한다. 부스팅(boosting)을 잔차에 대한 순차적 나무 적합으로 설명하며, gbm 패키지의 사용을 시연한다. 나무 방법이 교호작용 탐지에 강하지만 주효과 모형에서는 비효율적일 수 있음을 논의한다.

### Ch 14: Neural Networks (pp. 296-306)

**핵심**: 인공신경망의 통계학적 관점에서의 소개를 다룬다. 뉴런 모형에서 출발하여 단층·다층 퍼셉트론, 역전파 알고리즘, 과적합 방지, 통계 모형과의 관계를 설명한다. 실용적 성능은 과장에 비해 제한적이지만 유용한 도구임을 강조한다.

**키워드**: `neural network`, `perceptron`, `backpropagation`, `overfitting`, `universal approximation`

**상세**: → `Extending the linear model with R  generalized linear, mixed effects and nonparametric regression models by Faraway, Julian James (z-lib.org).md` Ch 14 (line 29449)

이 장은 인공신경망을 통계학적 관점에서 소개한다. 퍼셉트론을 가중합에 활성화 함수를 적용한 뉴런 모형 x₀ = f₀(Σwᵢxᵢ)으로 정의하고, 활성화 함수(항등, 로지스틱, 지시)에 따라 다중선형회귀·로지스틱 회귀·선형판별분석과 등가임을 보인다. 하나의 은닉층을 가진 전방향(feed-forward) 신경망의 구조를 정의하며, 은닉 뉴런에는 로지스틱 활성화, 출력에는 항등(연속 반응) 또는 로지스틱(이항 반응) 활성화를 사용한다. 범용 근사 정리(universal approximation theorem)의 이론적 의미와 유한 표본에서의 한계를 논의한다. 가중치(weights) 추정을 RSS 최소화로 정의하고, 복수의 국소 최솟값 문제를 강조한다. nnet 패키지로 LA 오존 데이터에 신경망을 적합하며, 입력 변수의 척도 표준화(scale)가 필수적임을 보인다. 100회 반복으로 최적 적합을 탐색하는 절차를 시연하고, R² ≈ 0.73으로 가법모형과 유사한 성능을 얻는다. 각 예측변수의 주변적 효과를 시각화하여 모형 해석의 어려움을 보완한다. 과적합 방지를 위한 가중치 감쇠(weight decay) 정규화와 은닉 유닛 수 선택 문제를 다룬다. 신경망의 단점—해석 불가능한 모수, 확률모형 부재, 표준오차 없음—을 지적하며, 실용적 성능이 과장에 비해 제한적이지만 유용한 도구임을 결론짓는다.
