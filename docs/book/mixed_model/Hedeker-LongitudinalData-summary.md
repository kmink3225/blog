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

### Ch 2: ANOVA Approaches to Longitudinal Data (pp. 13-29)

**핵심**: 단일 표본 및 다중 표본 반복측정 ANOVA를 다룬다. 시간 효과의 분해(직교 다항 대비, 기준셀 대비, 프로파일 대비, Helmert 대비), 그룹×시간 교호작용 검정, 복합대칭성(compound symmetry)과 구형성(sphericity) 가정을 설명한다.

**키워드**: `repeated measures ANOVA`, `compound symmetry`, `sphericity`, `orthogonal contrast`, `time effect`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 2 (line 2393)

### Ch 3: MANOVA Approaches to Longitudinal Data (pp. 31-45)

**핵심**: 다변량 반복측정 분석(MANOVA)을 다룬다. ANOVA와 MANOVA의 데이터 배치 차이, 성장곡선 분석의 다항식 표현, 다변량 시간효과 검정을 설명한다. MANOVA의 장점(일반적 공분산 구조 허용)과 단점(완전 데이터 필요, 시변 공변량 불가)을 비교한다.

**키워드**: `MANOVA`, `growth curve analysis`, `multivariate test`, `complete data`, `polynomial representation`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 3 (line 3592)

### Ch 4: Mixed-Effects Regression Models for Continuous Outcomes (pp. 47-79)

**핵심**: 연속 반응을 위한 혼합효과 회귀모형(MRM)의 핵심 장을 다룬다. 랜덤 절편 모형에서 출발하여 랜덤 절편+기울기 모형으로 확장하고, 복합대칭성과 급내상관계수의 관계를 설명한다. 행렬 표현, 분산-공분산 구조의 적합, 시변 공변량 처리(피험자 내·피험자 간 효과 분리), ML/REML 추정을 정신과 데이터 예제로 시연한다.

**키워드**: `mixed-effects regression`, `random intercept`, `random slope`, `intraclass correlation`, `REML`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 4 (line 4702)

### Ch 5: Mixed-Effects Polynomial Regression Models (pp. 81-99)

**핵심**: 비선형 시간 추세를 모형화하기 위한 다항식 혼합효과 모형을 다룬다. 이차 추세(곡선형) 모형의 정의와 적합, 직교 다항식의 사용과 모수 변환, 고차 다항식 모형(3차 이상)의 적용을 설명한다. 천장효과와 바닥효과가 있는 평정 척도 데이터에 특히 유용하다.

**키워드**: `polynomial regression`, `curvilinear trend`, `orthogonal polynomial`, `quadratic model`, `cubic trend`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 5 (line 7680)

### Ch 6: Covariance Pattern Models (pp. 101-111)

**핵심**: 공분산 패턴 모형(CPM)을 MANOVA의 확장으로 소개한다. 복합대칭, 1차 자기회귀(AR1), Toeplitz(띠), 비구조적(unstructured), 랜덤효과 구조 등 다양한 공분산 형태를 정의하고, AIC/BIC 기반 모형 선택을 설명한다. MRM과 달리 피험자 간·피험자 내 분산을 구분하지 않는 특성을 강조한다.

**키워드**: `covariance pattern model`, `compound symmetry`, `AR(1)`, `Toeplitz`, `model selection`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 6 (line 9838)

### Ch 7: Mixed Regression Models with Autocorrelated Errors (pp. 113-129)

**핵심**: 랜덤효과와 자기상관 오차를 동시에 포함하는 모형을 다룬다. 조건부 독립 가정을 완화하여 AR(1), MA(1), ARMA(1,1), Toeplitz, 비정상 AR(1) 오차 구조를 추가한다. MRM과 CPM의 결합으로서 종단 데이터의 분산-공분산 모형화를 더욱 유연하게 만든다.

**키워드**: `autocorrelated errors`, `AR(1)`, `MA(1)`, `ARMA`, `conditional independence`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 7 (line 10772)

### Ch 8: Generalized Estimating Equations (GEE) Models (pp. 131-146)

**핵심**: GEE 모형을 일반화선형모형(GLM)의 상관 데이터 확장으로 소개한다. 준우도 추정에 기반하며 완전 우도를 명시하지 않는 주변(marginal) 모형의 특성을 설명한다. 작동 상관 구조(independence, exchangeable, AR1, unstructured), GEE 추정 절차, 일반화 Wald 검정을 다루고, MCAR 가정의 한계를 논의한다.

**키워드**: `GEE`, `marginal model`, `quasi-likelihood`, `working correlation`, `robust standard error`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 8 (line 12822)

### Ch 9: Mixed-Effects Regression Models for Binary Outcomes (pp. 149-186)

**핵심**: 이항 반응을 위한 혼합효과 로지스틱/프로빗 회귀모형을 다룬다. 역치(threshold) 개념을 통해 연속 잠재변수와 이항 반응의 관계를 설명한다. 랜덤 절편 모형, 다중 랜덤효과 모형, 이분산 항, 다수준 표현을 기술하고, 주변 최대우도 추정(가우스-에르미트 구적법)과 랜덤효과·확률의 추정을 정신과 데이터 예제로 시연한다.

**키워드**: `logistic regression`, `probit`, `threshold concept`, `random intercept`, `Gauss-Hermite quadrature`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 9 (line 14134)

### Ch 10: Mixed-Effects Regression Models for Ordinal Outcomes (pp. 187-216)

**핵심**: 순서형 반응을 위한 혼합효과 비례 오즈 모형을 다룬다. 부분 비례 오즈, 척도항을 포함한 모형, 생존분석 모형과의 관계를 설명한다. 급내상관계수 계산, 피험자 간·피험자 내 분산의 분리를 논의하고, 정신과 및 보건서비스 연구 예제를 포함한다.

**키워드**: `proportional odds`, `ordinal regression`, `partial proportional odds`, `scaling term`, `cumulative logit`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 10 (line 16977)

### Ch 11: Mixed-Effects Regression Models for Nominal Data (pp. 219-238)

**핵심**: 명목형 반응을 위한 혼합효과 다항 회귀모형을 다룬다. 순서형 모형과의 차이(범주별 별도 계수 추정, 범주별 별도 랜덤효과 분산)를 설명한다. 보건서비스 이용 예제와 경쟁위험 생존모형(장기이식 대기) 예제를 포함한다.

**키워드**: `multinomial regression`, `nominal response`, `competing risks`, `category-specific effects`, `random-effect variance`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 11 (line 19788)

### Ch 12: Mixed-Effects Regression Models for Counts (pp. 239-256)

**핵심**: 카운트 데이터를 위한 혼합효과 모형을 다룬다. 포아송 회귀모형, 수정 포아송 모형(음이항 등), 영과잉 포아송(ZIP) 모형을 소개하고, 각각의 혼합효과 확장(랜덤효과 포아송, 혼합효과 ZIP)을 기술한다. 랜덤효과 추정과 이항·순서형 접근법과의 비교를 포함한다.

**키워드**: `Poisson regression`, `zero-inflated Poisson`, `negative binomial`, `mixed-effects count model`, `rate model`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 12 (line 21705)

### Ch 13: Mixed-Effects Regression Models for Three-Level Data (pp. 257-278)

**핵심**: 3수준 데이터(예: 반복측정이 피험자 내에, 피험자가 센터 내에 중첩)를 위한 혼합효과 모형을 다룬다. 3수준 선형 모형과 3수준 비선형 모형(프로빗, 로지스틱)을 정의하고, 급내상관계수의 계산, 순서형·명목형·카운트 반응으로의 확장을 논의한다.

**키워드**: `three-level model`, `nested data`, `multi-center study`, `intraclass correlation`, `hierarchical structure`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 13 (line 22996)

### Ch 14: Missing Data in Longitudinal Studies (pp. 279-312)

**핵심**: 종단 연구에서의 결측 데이터 문제를 체계적으로 다룬다. 결측 메커니즘(MCAR, MAR, MNAR)의 정의와 차이, 각 모형의 결측 메커니즘 가정, MCAR 검정, 비무시적 결측(MNAR)을 위한 선택 모형(selection model)과 패턴 혼합 모형(pattern-mixture model)을 시뮬레이션과 예제를 통해 설명한다.

**키워드**: `missing data`, `MCAR`, `MAR`, `MNAR`, `selection model`, `pattern-mixture model`

**상세**: → `Applied Longitudinal Data Analysis -Wiley-Interscience (2005) - (Wiley Series in Probability and Statistics) - Donald Hedeker, Robert D. Gibbons.md` Ch 14 (line 24872)
