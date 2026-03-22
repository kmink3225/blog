---
name: "Longitudinal Data Analysis"
type: book-summary
source_file: "Hedeker-LongitudinalData_azure_full.md"
authors: "Donald Hedeker, Robert D. Gibbons"
year: 2006
total_pages: 360
language: en
keywords: [longitudinal data, mixed-effects model, repeated measures, ANOVA, MANOVA, GEE, binary outcomes, ordinal outcomes, nominal outcomes, count data, missing data, three-level model, autocorrelated errors]
---

# Longitudinal Data Analysis — Summary

> Donald Hedeker, Robert D. Gibbons (2006), 360 pages, 14 chapters
> 종단 데이터 분석을 위한 혼합효과 회귀모형을 연속형·이항·순서형·명목형·카운트 반응에 대해 체계적으로 다루는 응용 교과서이다.

## Contents

- Preface (xiii)
- Acknowledgments (xvii)
- Acronyms (xix)
- 1 Introduction (1)
- 2 ANOVA Approaches to Longitudinal Data (13)
- 3 MANOVA Approaches to Longitudinal Data (31)
- 4 Mixed-Effects Regression Models for Continuous Outcomes (47)
- 5 Mixed-Effects Polynomial Regression Models (81)
- 6 Covariance Pattern Models (101)
- 7 Mixed Regression Models with Autocorrelated Errors (113)
- 8 Generalized Estimating Equations (GEE) Models (131)
- 9 Mixed-Effects Regression Models for Binary Outcomes (149)
- 10 Mixed-Effects Regression Models for Ordinal Outcomes (187)
- 11 Mixed-Effects Regression Models for Nominal Data (219)
- 12 Mixed-Effects Regression Models for Counts (239)
- 13 Mixed-Effects Regression Models for Three-Level Data (257)
- 14 Missing Data in Longitudinal Studies (279)
- Bibliography (313)
- Topic Index (335)

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-12)

**핵심**: 종단 연구의 장점(검정력 향상, 피험자 자기 통제, 연령효과와 코호트효과 분리)과 종단 데이터 분석의 도전(상관된 관측값, 불균형 시점, 결측치)을 설명한다. 기본 표기법과 데이터 배치(long format)를 정의하고, 가장 단순한 종단 분석(변화점수, ANCOVA)을 예제와 함께 소개한다.

**키워드**: `longitudinal study`, `change score`, `ANCOVA`, `data layout`, `within-subject variability`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 1 (line 1476)

이 장은 종단 연구의 기본 개념과 장단점을 설명한다. 종단 설계의 세 가지 주요 이점—검정력 향상(피험자 내 비교를 통한 오차 분산 감소), 피험자 자기 통제(각 개인이 자신의 대조군 역할), 연령효과와 코호트효과의 분리—를 기술한다. 종단 데이터 분석의 도전 과제로 상관된 관측값(같은 피험자의 반복 측정 간 상관), 불균형 시점(피험자마다 다른 관측 시점과 횟수), 결측치(탈락과 비응답)를 제시한다. 기본 표기법을 정의하며, 피험자 i의 j번째 관측을 Yᵢⱼ로 표기하고 데이터의 long format 배치를 설명한다. 가장 단순한 종단 분석 방법인 변화점수(change score: 사후-사전)와 ANCOVA(공변량으로서의 사전 점수)를 소개하고, 각각의 장단점을 비교한다. 변화점수 분석에서 Lord의 역설(사전 점수와의 상관에 따른 결론 차이)을 논의한다. 정신과 임상시험 데이터(HAMD 우울증 척도)를 본서 전체에서 사용할 주요 예제로 소개한다. 반복측정 데이터의 상관 구조가 독립 가정에 기반한 통상적 분석을 무효화할 수 있음을 경고한다. 이 책에서 다룰 모형들의 전체 로드맵을 제시한다.

### Ch 2: ANOVA Approaches to Longitudinal Data (pp. 13-29)

**핵심**: 단일 표본 및 다중 표본 반복측정 ANOVA를 다룬다. 시간 효과의 분해(직교 다항 대비, 기준셀 대비, 프로파일 대비, Helmert 대비), 그룹×시간 교호작용 검정, 복합대칭성(compound symmetry)과 구형성(sphericity) 가정을 설명한다.

**키워드**: `repeated measures ANOVA`, `compound symmetry`, `sphericity`, `orthogonal contrast`, `time effect`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 2 (line 2393)

이 장은 반복측정 ANOVA를 단일 표본 및 다중 표본 설계로 나누어 다룬다. 단일 표본 반복측정에서 시간 효과를 직교 다항 대비(선형, 이차, 삼차 등), 기준셀 대비(한 시점 대 나머지), 프로파일 대비(인접 시점 간 차이), Helmert 대비(각 시점 대 이후 평균)로 분해하는 방법을 설명한다. 다중 표본 반복측정에서 그룹×시간 교호작용 검정을 F-통계량으로 수행하고, 주효과와 교호작용의 분리를 기술한다. 복합대칭성(compound symmetry) 가정—모든 관측 간 동일한 상관과 동일한 분산—의 정의와 의미를 설명한다. 구형성(sphericity) 가정을 차이 변수들의 분산 동질성 조건으로 정의하고, Mauchly의 구형성 검정을 소개한다. 구형성 가정 위반 시의 보정 방법으로 Greenhouse-Geisser와 Huynh-Feldt ε-교정을 제시한다. 정신과 임상시험 데이터로 반복측정 ANOVA의 적용을 시연하며, 약물 그룹과 위약 그룹의 시간에 따른 HAMD 점수 변화를 분석한다. 반복측정 ANOVA의 제한점—완전 데이터 필요, 시변 공변량 불가, 연속 시간 처리 불가—을 정리한다. 결측치가 있는 피험자가 분석에서 완전히 제외되는 문제를 강조한다.

### Ch 3: MANOVA Approaches to Longitudinal Data (pp. 31-45)

**핵심**: 다변량 반복측정 분석(MANOVA)을 다룬다. ANOVA와 MANOVA의 데이터 배치 차이, 성장곡선 분석의 다항식 표현, 다변량 시간효과 검정을 설명한다. MANOVA의 장점(일반적 공분산 구조 허용)과 단점(완전 데이터 필요, 시변 공변량 불가)을 비교한다.

**키워드**: `MANOVA`, `growth curve analysis`, `multivariate test`, `complete data`, `polynomial representation`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 3 (line 3592)

이 장은 다변량 반복측정 분석(MANOVA)을 종단 데이터 분석에 적용한다. ANOVA와 MANOVA의 데이터 배치 차이를 설명하며, ANOVA는 long format, MANOVA는 wide format(한 행에 한 피험자의 모든 시점)을 사용함을 기술한다. 성장곡선 분석(growth curve analysis)을 다항식 시간 추세의 추정으로 정의하고, 시간을 직교 다항식으로 변환하여 각 차수의 유의성을 검정하는 절차를 설명한다. 다변량 시간효과 검정에서 Wilks' Λ, Pillai's trace, Hotelling-Lawley trace, Roy's 최대근 등 네 가지 검정 통계량을 소개한다. MANOVA의 장점—구형성 가정 불필요, 비구조적(unstructured) 공분산 행렬 허용—을 설명한다. MANOVA의 단점—완전 데이터만 사용 가능(결측 피험자 완전 제외), 시변 공변량 처리 불가, 시점이 많으면 추정할 공분산 모수가 급증—을 정리한다. 정신과 데이터에 MANOVA를 적용하여 그룹×시간 교호작용을 검정하고, ANOVA 결과와 비교한다. 완전 데이터 분석과 불완전 데이터 분석 간 표본 크기 차이에 따른 결론의 변화 가능성을 논의한다. 이후 장에서 다룰 혼합효과 모형이 이 한계점들을 해결함을 예고한다.

### Ch 4: Mixed-Effects Regression Models for Continuous Outcomes (pp. 47-79)

**핵심**: 연속 반응을 위한 혼합효과 회귀모형(MRM)의 핵심 장을 다룬다. 랜덤 절편 모형에서 출발하여 랜덤 절편+기울기 모형으로 확장하고, 복합대칭성과 급내상관계수의 관계를 설명한다. 행렬 표현, 분산-공분산 구조의 적합, 시변 공변량 처리(피험자 내·피험자 간 효과 분리), ML/REML 추정을 정신과 데이터 예제로 시연한다.

**키워드**: `mixed-effects regression`, `random intercept`, `random slope`, `intraclass correlation`, `REML`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 4 (line 4702)

이 장은 연속 반응을 위한 혼합효과 회귀모형(MRM)의 핵심 이론과 적용을 다룬다. 랜덤 절편 모형에서 출발하여 Yᵢⱼ = (Xᵢⱼβ + υ₀ᵢ) + εᵢⱼ의 구조를 정의하고, 복합대칭성 공분산과 급내상관계수 ρ = σ²ᵥ/(σ²ᵥ+σ²ₑ)의 관계를 유도한다. 랜덤 절편+기울기 모형으로 확장하여 개인별 시간 추세의 이질성을 모형화하고, 랜덤효과 분산-공분산 행렬 D의 구조를 설명한다. 행렬 표현 Yᵢ = Xᵢβ + Zᵢυᵢ + εᵢ를 통해 주변(marginal) 공분산 구조 Σᵢ = ZᵢDZᵢᵀ + σ²I를 유도한다. ML과 REML 추정의 차이를 설명하며, REML이 분산 성분의 편향을 교정함을 강조한다. 시변 공변량의 처리에서 피험자 내(within-subject) 효과와 피험자 간(between-subject) 효과의 분리 방법을 기술한다. 정신과 임상시험 데이터로 랜덤 절편 모형, 랜덤 절편+기울기 모형을 순차적으로 적합하고, 우도비 검정으로 모형 비교를 수행한다. 약물×시간 교호작용의 해석과 예측값 계산을 시연한다. 잔차 진단과 랜덤효과의 정규성 검사를 포함한다. 불균형 데이터(피험자마다 다른 관측 횟수와 시점)의 자연스러운 처리가 MRM의 핵심 장점임을 강조한다.

### Ch 5: Mixed-Effects Polynomial Regression Models (pp. 81-99)

**핵심**: 비선형 시간 추세를 모형화하기 위한 다항식 혼합효과 모형을 다룬다. 이차 추세(곡선형) 모형의 정의와 적합, 직교 다항식의 사용과 모수 변환, 고차 다항식 모형(3차 이상)의 적용을 설명한다. 천장효과와 바닥효과가 있는 평정 척도 데이터에 특히 유용하다.

**키워드**: `polynomial regression`, `curvilinear trend`, `orthogonal polynomial`, `quadratic model`, `cubic trend`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 5 (line 7680)

이 장은 비선형 시간 추세를 모형화하기 위한 다항식 혼합효과 모형을 다룬다. 이차(곡선형) 추세 모형 Yᵢⱼ = β₀ + β₁tᵢⱼ + β₂t²ᵢⱼ + υ₀ᵢ + υ₁ᵢtᵢⱼ + εᵢⱼ를 정의하고, 이차항의 랜덤효과 포함 여부에 따른 모형 비교를 수행한다. 직교 다항식의 사용 동기—다공선성 감소와 모수 해석의 용이성—를 설명하고, 직교 변환 후 계수의 해석 방법을 기술한다. 원래 다항식 계수로의 역변환 공식을 제시하며, 직교 다항식 모형과 원래 다항식 모형의 동치성을 확인한다. 고차 다항식(3차 이상) 모형의 적용 사례를 제시하고, 차수 선택을 위한 우도비 검정과 AIC/BIC 기준의 사용을 설명한다. 정신과 임상시험 데이터에 이차 모형을 적합하여, 약물 그룹의 빠른 초기 호전과 이후 안정화 패턴(곡선형 추세)을 포착한다. 천장효과(ceiling effect)와 바닥효과(floor effect)가 있는 평정 척도 데이터에서 다항식 모형이 특히 유용함을 논의한다. 랜덤효과 공분산 행렬의 양정치(positive definite) 제약과 수렴 문제를 다룬다. 시간의 중심화(centering)가 수치적 안정성과 해석에 미치는 영향을 설명한다. 다항식 모형의 외삽(extrapolation) 위험을 경고한다.

### Ch 6: Covariance Pattern Models (pp. 101-111)

**핵심**: 공분산 패턴 모형(CPM)을 MANOVA의 확장으로 소개한다. 복합대칭, 1차 자기회귀(AR1), Toeplitz(띠), 비구조적(unstructured), 랜덤효과 구조 등 다양한 공분산 형태를 정의하고, AIC/BIC 기반 모형 선택을 설명한다. MRM과 달리 피험자 간·피험자 내 분산을 구분하지 않는 특성을 강조한다.

**키워드**: `covariance pattern model`, `compound symmetry`, `AR(1)`, `Toeplitz`, `model selection`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 6 (line 9838)

이 장은 공분산 패턴 모형(CPM)을 MANOVA의 확장이자 MRM의 대안으로 소개한다. CPM이 반응의 주변(marginal) 분포를 직접 모형화하며, 피험자 간·피험자 내 분산의 구분 없이 총 공분산 구조를 명세한다는 점에서 MRM과 차이가 있음을 설명한다. 다양한 공분산 구조를 정의한다: 복합대칭(CS: 동일한 상관과 분산), 1차 자기회귀(AR1: 시간 간격에 따라 지수적으로 감소하는 상관), Toeplitz(띠 구조: 같은 시차에 같은 상관), 비구조적(UN: 모든 원소가 자유 모수), 랜덤효과 구조(RE: MRM의 ZDZᵀ+σ²I와 동치). 각 구조의 자유 모수 수를 비교하고, 시점 수가 많아질 때 비구조적 모형의 모수 폭발 문제를 지적한다. AIC와 BIC 기반 모형 선택을 설명하며, BIC가 더 절약적 모형을 선호하는 경향을 논의한다. 정신과 데이터에 CS, AR1, Toeplitz, UN 구조를 적합하고 적합도를 비교한다. CPM에서 고정효과 추정이 공분산 구조 선택에 영향받을 수 있음을 지적한다. GEE(일반화추정방정식)와 CPM의 관계를 언급하며, 두 접근법 모두 주변 모형에 속함을 설명한다. CPM이 MRM보다 단순하지만, 랜덤효과의 예측이나 피험자별 추론이 불가능한 한계를 정리한다.

### Ch 7: Mixed Regression Models with Autocorrelated Errors (pp. 113-129)

**핵심**: 랜덤효과와 자기상관 오차를 동시에 포함하는 모형을 다룬다. 조건부 독립 가정을 완화하여 AR(1), MA(1), ARMA(1,1), Toeplitz, 비정상 AR(1) 오차 구조를 추가한다. MRM과 CPM의 결합으로서 종단 데이터의 분산-공분산 모형화를 더욱 유연하게 만든다.

**키워드**: `autocorrelated errors`, `AR(1)`, `MA(1)`, `ARMA`, `conditional independence`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 7 (line 10772)

이 장은 랜덤효과와 자기상관 오차를 동시에 포함하는 모형을 다룬다. 표준 MRM의 조건부 독립 가정(랜덤효과를 조건부로 하면 오차가 독립)을 완화하여 εᵢ ~ N(0, σ²Rᵢ)에서 Rᵢ ≠ I를 허용한다. AR(1) 오차 구조에서 corr(εᵢⱼ, εᵢⱼ') = ρ^|tⱼ−tⱼ'|의 정의와 해석을 설명하고, MA(1) 오차(1시차까지만 상관)와 ARMA(1,1) 오차(AR과 MA의 결합)를 소개한다. Toeplitz 오차 구조와 비정상(nonstationary) AR(1) 구조를 추가적 대안으로 제시한다. MRM+자기상관 모형의 총 공분산이 Σᵢ = ZᵢDZᵢᵀ + σ²Rᵢ로 랜덤효과 성분과 오차 성분의 합임을 설명한다. 이 모형이 MRM(피험자 간 이질성)과 CPM(시간적 상관)의 결합으로서 가장 유연한 분산-공분산 모형화를 제공함을 강조한다. 정신과 데이터에 랜덤 절편+기울기 모형에 AR(1) 오차를 추가하여 적합하고, 자기상관 포함 여부에 따른 고정효과 추정의 변화를 비교한다. 자기상관 모수의 유의성을 우도비 검정으로 평가한다. 관측 시점이 불균등할 때 연속 시간 AR(1)의 정의와 이산 시간 AR(1)과의 차이를 논의한다. 모형 복잡도와 해석 가능성 사이의 균형을 강조한다.

### Ch 8: Generalized Estimating Equations (GEE) Models (pp. 131-146)

**핵심**: GEE 모형을 일반화선형모형(GLM)의 상관 데이터 확장으로 소개한다. 준우도 추정에 기반하며 완전 우도를 명시하지 않는 주변(marginal) 모형의 특성을 설명한다. 작동 상관 구조(independence, exchangeable, AR1, unstructured), GEE 추정 절차, 일반화 Wald 검정을 다루고, MCAR 가정의 한계를 논의한다.

**키워드**: `GEE`, `marginal model`, `quasi-likelihood`, `working correlation`, `robust standard error`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 8 (line 12822)

이 장은 GEE 모형을 일반화선형모형(GLM)의 상관 데이터 확장으로 소개한다. GLM의 세 구성요소(분포, 연결함수, 선형예측자)를 복습하고, GEE가 완전 우도를 명시하지 않고 준우도(quasi-likelihood) 추정에 기반하는 주변(marginal) 모형임을 설명한다. 작동 상관 구조(working correlation structure)의 네 가지 유형—independence, exchangeable, AR(1), unstructured—을 정의하고, 각각의 장단점을 비교한다. 샌드위치(sandwich) 추정량에 의한 강건 표준오차의 구성을 설명하며, 작동 상관 구조가 잘못 지정되어도 일치 추정을 보장하는 GEE의 핵심 특성을 기술한다. 일반화 Wald 검정과 일반화 스코어 검정을 모수의 유의성 검정에 사용한다. GEE와 혼합효과 모형의 근본적 차이—GEE는 모집단 평균(population-averaged) 효과를, 혼합효과 모형은 피험자 특이적(subject-specific) 효과를 추정—를 비정규 반응에서의 비축소성(non-collapsibility)을 통해 설명한다. 정신과 데이터에 GEE를 적용하여 이항 반응의 주변 분석을 시연한다. GEE의 주요 한계로 MCAR(완전 무작위 결측) 가정의 필요성을 지적하며, MAR 하에서의 편향 가능성을 논의한다. 피험자 수가 적을 때 샌드위치 추정량의 하향 편향 문제를 언급한다.

### Ch 9: Mixed-Effects Regression Models for Binary Outcomes (pp. 149-186)

**핵심**: 이항 반응을 위한 혼합효과 로지스틱/프로빗 회귀모형을 다룬다. 역치(threshold) 개념을 통해 연속 잠재변수와 이항 반응의 관계를 설명한다. 랜덤 절편 모형, 다중 랜덤효과 모형, 이분산 항, 다수준 표현을 기술하고, 주변 최대우도 추정(가우스-에르미트 구적법)과 랜덤효과·확률의 추정을 정신과 데이터 예제로 시연한다.

**키워드**: `logistic regression`, `probit`, `threshold concept`, `random intercept`, `Gauss-Hermite quadrature`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 9 (line 14134)

이 장은 이항 반응을 위한 혼합효과 로지스틱/프로빗 회귀모형을 체계적으로 다룬다. 역치(threshold) 개념을 도입하여 연속 잠재변수 Y*와 이항 관측 반응 Y = I(Y* > 0)의 관계를 설명하며, 잠재변수의 분포가 로지스틱이면 로짓 모형, 정규이면 프로빗 모형이 됨을 보인다. 랜덤 절편 모형 logit P(Yᵢⱼ=1) = xᵢⱼᵀβ + υ₀ᵢ를 정의하고, 랜덤효과가 잠재변수의 피험자별 역치 이동으로 해석됨을 설명한다. 다중 랜덤효과 모형과 이분산(heteroscedastic) 항의 포함을 다수준 표현으로 기술한다. 주변 최대우도 추정에서 랜덤효과에 대한 적분 문제를 가우스-에르미트 구적법(Gauss-Hermite quadrature)으로 해결하는 방법을 설명한다. 구적점(quadrature points)의 수가 추정 정확도에 미치는 영향과 적응적 구적법의 이점을 논의한다. 정신과 데이터에서 이항화된 반응(HAMD ≤ 7 여부)에 대해 랜덤 절편 로지스틱 모형을 적합하고, 약물×시간 교호작용의 오즈비 해석을 시연한다. 조건부(subject-specific) 효과와 주변(population-averaged) 효과의 관계를 근사식 βₘₐᵣₘ ≈ β/(1+c²σ²ᵥ)^½으로 설명한다. 경험적 베이즈(empirical Bayes)에 의한 랜덤효과 예측과 개인별 확률 추정을 포함한다. 분산 성분의 급내상관계수를 잠재변수 척도에서 σ²ᵥ/(σ²ᵥ+π²/3)으로 계산한다.

### Ch 10: Mixed-Effects Regression Models for Ordinal Outcomes (pp. 187-216)

**핵심**: 순서형 반응을 위한 혼합효과 비례 오즈 모형을 다룬다. 부분 비례 오즈, 척도항을 포함한 모형, 생존분석 모형과의 관계를 설명한다. 급내상관계수 계산, 피험자 간·피험자 내 분산의 분리를 논의하고, 정신과 및 보건서비스 연구 예제를 포함한다.

**키워드**: `proportional odds`, `ordinal regression`, `partial proportional odds`, `scaling term`, `cumulative logit`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 10 (line 16977)

이 장은 순서형 반응을 위한 혼합효과 비례 오즈 모형을 다룬다. 누적 로짓 모형 logit P(Yᵢⱼ ≤ c) = γc − xᵢⱼᵀβ를 정의하고, 역치 모수 γc의 의미와 비례 오즈 가정(공변량 효과가 모든 절단점에서 동일)의 의미를 설명한다. 랜덤 절편 υ₀ᵢ를 추가하여 피험자 간 이질성을 모형화하고, 역치가 피험자별로 이동하는 것으로 해석한다. 부분 비례 오즈(partial proportional odds) 모형을 일부 공변량에 대해 비례 오즈 가정을 완화하는 확장으로 소개한다. 척도항(scaling term)을 포함한 위치-척도 모형에서 공변량이 잠재변수의 분산에도 영향을 미치는 경우를 모형화한다. 생존분석 모형과의 관계—이산 비례 위험 모형이 보완 로그-로그 연결의 순서형 모형과 동치—를 설명한다. 급내상관계수 계산에서 잠재변수 분산(로짓: π²/3, 프로빗: 1)을 사용한 공식을 제시한다. 피험자 간·피험자 내 분산의 분리를 통해 시변 공변량의 두 가지 효과를 구분한다. 정신과 데이터의 원래 4점 순서형 반응(CTSIB)에 비례 오즈 모형을 적합하고, 보건서비스 연구 데이터에서의 추가 예제를 포함한다. 적합도 평가와 비례 오즈 가정의 검정 방법을 논의한다.

### Ch 11: Mixed-Effects Regression Models for Nominal Data (pp. 219-238)

**핵심**: 명목형 반응을 위한 혼합효과 다항 회귀모형을 다룬다. 순서형 모형과의 차이(범주별 별도 계수 추정, 범주별 별도 랜덤효과 분산)를 설명한다. 보건서비스 이용 예제와 경쟁위험 생존모형(장기이식 대기) 예제를 포함한다.

**키워드**: `multinomial regression`, `nominal response`, `competing risks`, `category-specific effects`, `random-effect variance`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 11 (line 19788)

이 장은 명목형 반응을 위한 혼합효과 다항 회귀모형을 다룬다. 순서형 모형과의 근본적 차이—범주별 별도 회귀계수 추정, 범주별 별도 랜덤효과 분산—를 설명한다. 기준 범주 로짓(baseline-category logit) 구조에서 log P(Yᵢⱼ=c)/P(Yᵢⱼ=C) = xᵢⱼᵀβc + υcᵢ의 형태를 정의하고, C−1개의 로짓 함수에 대해 각각 랜덤효과를 설정한다. 주변 우도의 적분 차원이 범주 수에 비례하여 증가하므로 구적법의 계산 부담이 급증하는 문제를 지적한다. 보건서비스 이용(mental health service utilization) 데이터—외래, 입원, 무치료의 3범주—에 명목형 혼합효과 모형을 적합하고, 범주별 치료 효과와 시간 효과를 해석한다. 경쟁위험 생존모형(competing risks survival model)과 명목형 혼합효과 모형의 등가성을 장기이식 대기(organ transplant waiting) 데이터로 시연한다. 경쟁위험 설정에서 사망, 이식, 계속 대기의 세 결과를 이산 시간 모형으로 분석한다. 범주별 랜덤효과 공분산 행렬의 구조(비구조적, 독립적, 동일한 분산)와 모형 선택을 논의한다. 명목형 모형에서 피험자 간 급내상관의 범주별 차이를 계산하고 해석한다. 계산 효율을 위한 가우스-에르미트 구적법의 적응적 버전 사용을 권장한다.

### Ch 12: Mixed-Effects Regression Models for Counts (pp. 239-256)

**핵심**: 카운트 데이터를 위한 혼합효과 모형을 다룬다. 포아송 회귀모형, 수정 포아송 모형(음이항 등), 영과잉 포아송(ZIP) 모형을 소개하고, 각각의 혼합효과 확장(랜덤효과 포아송, 혼합효과 ZIP)을 기술한다. 랜덤효과 추정과 이항·순서형 접근법과의 비교를 포함한다.

**키워드**: `Poisson regression`, `zero-inflated Poisson`, `negative binomial`, `mixed-effects count model`, `rate model`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 12 (line 21705)

이 장은 카운트 데이터를 위한 혼합효과 모형을 다룬다. 포아송 회귀모형 log μᵢⱼ = xᵢⱼᵀβ를 정의하고, 포아송 분포의 평균-분산 동등 가정(E(Y) = var(Y) = μ)을 설명한다. 과산포에 대응하는 수정 포아송 모형으로 음이항 분포(var(Y) = μ + μ²/k)를 소개한다. 영과잉 포아송(ZIP: zero-inflated Poisson) 모형을 영의 과다 발생을 별도의 구조적 영(structural zero) 성분으로 모형화하는 혼합 분포로 정의한다. 각 모형의 혼합효과 확장을 다룬다: 랜덤효과 포아송(log μᵢⱼ = xᵢⱼᵀβ + υ₀ᵢ)에서 exp(υ₀ᵢ)의 해석(개인별 비율 승수)을 설명하고, 랜덤효과 ZIP 모형에서 영 성분과 카운트 성분에 대한 별도의 랜덤효과를 정의한다. 노출 시간(exposure time)의 오프셋 항 log(tᵢⱼ)으로의 포함을 기술한다. 랜덤효과 추정과 경험적 베이즈 예측을 통한 피험자별 비율 추정을 시연한다. 이항·순서형 접근법과의 비교에서 카운트 모형이 범위 제한 없는 반응에 적합함을 논의한다. 의료 이용 횟수 데이터를 사용하여 랜덤효과 포아송과 ZIP 모형을 적합하고, 영과잉의 존재를 우도비 검정으로 확인한다. 과산포 진단과 모형 선택 전략을 정리한다.

### Ch 13: Mixed-Effects Regression Models for Three-Level Data (pp. 257-278)

**핵심**: 3수준 데이터(예: 반복측정이 피험자 내에, 피험자가 센터 내에 중첩)를 위한 혼합효과 모형을 다룬다. 3수준 선형 모형과 3수준 비선형 모형(프로빗, 로지스틱)을 정의하고, 급내상관계수의 계산, 순서형·명목형·카운트 반응으로의 확장을 논의한다.

**키워드**: `three-level model`, `nested data`, `multi-center study`, `intraclass correlation`, `hierarchical structure`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 13 (line 22996)

이 장은 3수준 데이터를 위한 혼합효과 모형을 다룬다. 반복측정이 피험자 내에 중첩되고 피험자가 센터(또는 학교, 병원) 내에 중첩되는 3수준 구조를 정의한다. 3수준 선형 모형 Yᵢⱼₖ = xᵢⱼₖᵀβ + w₀ₖ + υ₀ⱼₖ + εᵢⱼₖ에서 센터 수준 랜덤효과 w₀ₖ와 피험자 수준 랜덤효과 υ₀ⱼₖ의 역할을 설명한다. 급내상관계수를 두 수준—센터 수준 ρ₃ = σ²w/(σ²w+σ²υ+σ²ε)와 피험자 수준 ρ₂ = (σ²w+σ²υ)/(σ²w+σ²υ+σ²ε)—에서 계산한다. 3수준 비선형 모형(프로빗, 로지스틱)으로의 확장에서 적분 차원이 증가하는 문제와 구적법의 계산 부담을 논의한다. 다기관 임상시험(multi-center clinical trial) 데이터를 사용하여 3수준 모형의 적합을 시연하며, 센터 간 치료 효과의 이질성을 랜덤 기울기로 모형화한다. 3수준 순서형·명목형·카운트 반응 모형으로의 확장 가능성을 간략히 기술한다. 교차(crossed) 랜덤효과 구조가 순수한 중첩 구조와 다름을 설명하고, 교차 구조의 처리 방법을 논의한다. 모형 선택에서 우도비 검정과 AIC/BIC의 사용, 센터 수준 분산 성분의 유의성 평가 방법을 제시한다. 센터 효과가 고정인지 랜덤인지의 판단 기준과 실제적 의미를 논의한다.

### Ch 14: Missing Data in Longitudinal Studies (pp. 279-312)

**핵심**: 종단 연구에서의 결측 데이터 문제를 체계적으로 다룬다. 결측 메커니즘(MCAR, MAR, MNAR)의 정의와 차이, 각 모형의 결측 메커니즘 가정, MCAR 검정, 비무시적 결측(MNAR)을 위한 선택 모형(selection model)과 패턴 혼합 모형(pattern-mixture model)을 시뮬레이션과 예제를 통해 설명한다.

**키워드**: `missing data`, `MCAR`, `MAR`, `MNAR`, `selection model`, `pattern-mixture model`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 14 (line 24872)

이 장은 종단 연구에서의 결측 데이터 문제를 체계적으로 다룬다. 결측 메커니즘의 세 가지 유형—MCAR(완전 무작위 결측: 결측이 관측·미관측 반응 모두와 무관), MAR(무작위 결측: 결측이 관측 데이터에만 의존), MNAR(비무작위 결측: 결측이 미관측 반응에 의존)—을 정의하고, 각각의 실제적 의미를 예시로 설명한다. MRM(혼합효과 모형)이 MAR 가정 하에서 유효한 추론을 제공하며, GEE는 MCAR만 처리 가능하다는 핵심적 차이를 강조한다. MCAR 검정을 위한 Little의 χ² 검정을 소개하고, 정신과 데이터에 적용한다. MNAR을 위한 선택 모형(selection model)을 반응 모형과 결측 모형의 결합으로 정의하며, 탈락(dropout) 모형에서 logit P(Dᵢ=j) = f(관측 반응, 미관측 반응)의 구조를 설명한다. 패턴 혼합 모형(pattern-mixture model)을 결측 패턴별로 별도의 분포를 가정하는 대안적 접근법으로 제시하고, 식별 불가능(non-identifiability) 문제와 이에 대한 민감도 분석 전략을 논의한다. 시뮬레이션을 통해 MCAR, MAR, MNAR 하에서 각 분석 방법(완전 사례, GEE, MRM, 선택 모형)의 편향과 효율성을 비교한다. 다중 대입(multiple imputation)을 결측 처리의 추가적 전략으로 간략히 소개한다. 결측 메커니즘 가정의 검증 불가능성과 민감도 분석의 중요성을 강조한다.
