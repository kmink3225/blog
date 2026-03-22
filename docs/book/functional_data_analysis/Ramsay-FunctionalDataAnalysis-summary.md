---
name: "Functional Data Analysis"
type: book-summary
source_file: "Ramsay-FunctionalDataAnalysis_azure_full.md"
authors: "J. O. Ramsay, B. W. Silverman"
year: 1997
total_pages: 310
language: en
keywords: [functional data analysis, FDA, smoothing, registration, functional PCA, functional linear model, canonical correlation, differential operator, principal differential analysis, roughness penalty]
---

# Functional Data Analysis — Summary

> J. O. Ramsay, B. W. Silverman (1997), 310 pages, 16 chapters
> 함수 데이터 분석(FDA)의 개념과 방법론을 최초로 체계화한 기념비적 교과서

## Contents

1. Introduction (p.1)
2. Notation and techniques (p.23)
3. Representing functional data as smooth functions (p.37)
4. The roughness penalty approach (p.57)
5. The registration and display of functional data (p.67)
6. Principal components analysis for functional data (p.85)
7. Regularized principal components analysis (p.111)
8. Principal components analysis of mixed data (p.125)
9. Functional linear models (p.139)
10. Functional linear models for scalar responses (p.157)
11. Functional linear models for functional responses (p.179)
12. Canonical correlation and discriminant analysis (p.199)
13. Differential operators in functional data analysis (p.217)
14. Principal differential analysis (p.239)
15. More general roughness penalties (p.253)
16. Some perspectives on FDA (p.271)

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-22)

**핵심**: 함수 데이터(functional data)의 정의와 다양한 분석 사례를 소개한다. 데이터 표현(스무딩, 보간), 등록(registration), 요약 통계(평균, 공분산, 상관 함수), 함수 PCA, 함수 선형 모형, 미분 활용 등 FDA의 전반적 목표와 방향을 제시한다.

**키워드**: `functional data`, `smoothing`, `registration`, `functional PCA`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 1 (line 1746)

### Ch 2: Notation and techniques (pp. 23-36)

**핵심**: FDA에 사용되는 수학적 표기법과 기본 기법을 소개한다. 내적(inner product), 사영(projection), 다변량 선형 모형, 정칙화(regularization)의 개념을 함수 공간으로 확장한다.

**키워드**: `inner product`, `projection`, `regularization`, `linear model`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 2 (line 3157)

### Ch 3: Representing functional data as smooth functions (pp. 37-56)

**핵심**: 관측된 이산 데이터를 평활 함수로 표현하는 방법을 다룬다. 기저 함수 방법(Fourier, 다항식, B-spline, wavelet), 커널 스무딩, 국소 가중치 방법, 대역폭 선택을 포함한다.

**키워드**: `basis function`, `B-spline`, `Fourier`, `kernel smoothing`, `bandwidth`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 3 (line 3898)

### Ch 4: The roughness penalty approach (pp. 57-66)

**핵심**: 스플라인 스무딩과 roughness penalty 접근법을 다룬다. 적합도와 평활도 간의 균형, 미분의 스무딩, 정칙화된 기저 접근법과 그 성질을 설명한다.

**키워드**: `roughness penalty`, `spline smoothing`, `regularized basis`, `smoothing parameter`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 4 (line 4993)

### Ch 5: Registration and display of functional data (pp. 67-84)

**핵심**: 곡선 등록(registration) 문제를 다룬다. 이동 등록(shift registration), 특징점 등록(landmark registration), 비선형 시간 변환(time warping), Newton-Raphson 알고리즘을 이용한 추정을 포함한다.

**키워드**: `registration`, `landmark alignment`, `time warping`, `curve alignment`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 5 (line 5463)

### Ch 6: Principal components analysis for functional data (pp. 85-110)

**핵심**: 함수 PCA의 정의, 다변량 PCA와의 관계, 고유분석(eigenanalysis), 결과 시각화(평균 변동, 주성분 점수), 이변량/다변량 함수 PCA, 계산 방법(이산화, 기저 전개)을 다룬다.

**키워드**: `functional PCA`, `eigenfunction`, `variance explained`, `principal component scores`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 6 (line 6418)

### Ch 7: Regularized principal components analysis (pp. 111-124)

**핵심**: roughness penalty를 이용한 정칙화 PCA를 다룬다. 교차 검증을 통한 스무딩 모수 선택, pinch force 데이터 예제, 데이터 vs PCA 스무딩의 비교를 포함한다.

**키워드**: `regularized PCA`, `cross-validation`, `smoothing`, `roughness penalty`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 7 (line 8222)

### Ch 8: PCA of mixed data (pp. 125-138)

**핵심**: 함수 데이터와 벡터 데이터가 혼합된 경우의 PCA를 다룬다. 함수와 벡터 공간의 결합, 등록과 PCA의 동시 수행, 기온 데이터와 시간 이동 효과의 균형을 포함한다.

**키워드**: `mixed data PCA`, `hybrid data`, `registration with PCA`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 8 (line 9061)

### Ch 9: Functional linear models (pp. 139-156)

**핵심**: 함수 선형 모형과 함수 ANOVA를 다룬다. 모형 적합, 적합도 평가, 걷는 말의 힘판(force plate) 데이터 분석, 계산적 이슈(기저 전개, 정칙화)를 포함한다.

**키워드**: `functional ANOVA`, `functional linear model`, `pointwise test`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 9 (line 9973)

### Ch 10: Functional linear models for scalar responses (pp. 157-178)

**핵심**: 함수를 예측변수로, 스칼라를 반응변수로 하는 회귀 모형을 다룬다. 정칙화 방법(이산화, 기저 함수, roughness penalty), 교차 검증, 적분 방정식과의 관계를 포함한다.

**키워드**: `scalar-on-function regression`, `regularization`, `cross-validation`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 10 (line 11059)

### Ch 11: Functional linear models for functional responses (pp. 179-198)

**핵심**: 함수 예측변수와 함수 반응변수를 모두 포함하는 모형을 다룬다. 기저 표현을 이용한 추정, 정칙화, 적합도 평가, 이변량 roughness penalty를 포함한다.

**키워드**: `function-on-function regression`, `bivariate roughness penalty`, `basis expansion`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 11 (line 12242)

### Ch 12: Canonical correlation and discriminant analysis (pp. 199-216)

**핵심**: 함수 정준상관분석(functional CCA)과 판별분석을 다룬다. 정칙화의 필요성, 보행 데이터와 lupus nephritis 데이터 적용, 최적 스코어링과 판별 문제를 포함한다.

**키워드**: `canonical correlation`, `discriminant analysis`, `regularization`, `optimal scoring`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 12 (line 1249)

### Ch 13: Differential operators in FDA (pp. 217-238)

**핵심**: 선형 미분 연산자(LDO)의 FDA에서의 역할을 다룬다. 새로운 함수 관측 생성, 모형 정칙화, 변동 분할, Green 함수, 재생 핵(reproducing kernel)을 포함한다.

**키워드**: `differential operator`, `Green function`, `reproducing kernel`, `LDO`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 13 (line 14502)

### Ch 14: Principal differential analysis (pp. 239-252)

**핵심**: 주미분분석(PDA)의 기본 원리와 필요성을 소개한다. PCA와의 관계, 미분 방정식을 이용한 함수 변동의 특성화를 다룬다.

**키워드**: `principal differential analysis`, `PDA`, `differential equation`, `functional variation`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 14 (line 15688)

### Ch 15: More general roughness penalties (pp. 253-270)

**핵심**: 보다 일반적인 roughness penalty의 구성과 적용을 다룬다. LDO를 이용한 일반화된 penalty, 가변 계수 모형을 포함한다.

**키워드**: `generalized roughness penalty`, `variable coefficient`, `LDO penalty`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 15 (line 16797)

### Ch 16: Some perspectives on FDA (pp. 271-310)

**핵심**: FDA의 역사적 맥락과 향후 발전 방향에 대한 저자들의 관점을 제시한다.

**키워드**: `FDA history`, `future directions`, `perspectives`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 16 (line 17962)
