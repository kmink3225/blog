---
name: "Introduction to Functional Data Analysis"
type: book-summary
source_file: "Kokoszka-IntroFDA_azure_full.md"
authors: "Piotr Kokoszka, Matthew Reimherr"
year: 2017
total_pages: 290
language: en
keywords: [functional data analysis, FDA, scalar-on-function regression, functional PCA, functional time series, spatial FDA, Hilbert space, sparse FDA, functional GLM, refund]
---

# Introduction to Functional Data Analysis — Summary

> Piotr Kokoszka, Matthew Reimherr (2017), 290 pages, 12 chapters
> 함수 데이터 분석의 이론과 방법을 대학원 교과서 형태로 체계적으로 소개하며 R 코드와 문제를 포함하는 입문서

## Contents

1. First steps in the analysis of functional data (p.1)
2. Further topics in exploratory FDA (p.21)
3. Mathematical framework for functional data (p.37)
4. Scalar-on-function regression (p.45)
5. Functional response models (p.67)
6. Functional generalized linear models (p.101)
7. Sparse FDA (p.117)
8. Functional time series (p.141)
9. Spatial functional data and models (p.179)
10. Elements of Hilbert space theory (p.211)
11. Random functions (p.233)
12. Inference from a random sample (p.249)

---

## Chapter Summaries

### Ch 1: First steps in the analysis of functional data (pp. 1-20)

**핵심**: 기저 전개(basis expansion)를 이용한 함수 데이터 표현, 표본 평균과 공분산의 추정, 주성분 함수(principal component function), BOA 주식 수익률 분석, 확산 텐서 영상(DTI) 데이터 분석을 다룬다.

**키워드**: `basis expansion`, `sample covariance`, `principal component`, `BOA returns`, `DTI`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 1 (line 1308)

### Ch 2: Further topics in exploratory FDA (pp. 21-36)

**핵심**: 미분, 벌점 스무딩(penalized smoothing), 곡선 정렬(curve alignment)을 다룬다. 스무딩 모수 선택, 곡선 등록의 기본 방법을 포함한다.

**키워드**: `derivatives`, `penalized smoothing`, `curve alignment`, `registration`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 2 (line 2437)

### Ch 3: Mathematical framework for functional data (pp. 37-44)

**핵심**: 함수 데이터의 수학적 프레임워크를 제시한다. 제곱적분 가능 함수(L2 공간), 확률 함수(random function), 선형 변환의 기본 개념을 다룬다.

**키워드**: `L2 space`, `random function`, `linear transformation`, `square integrable`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 3 (line 3337)

### Ch 4: Scalar-on-function regression (pp. 45-66)

**핵심**: 스칼라 반응에 대한 함수 회귀를 다룬다. 기저 전개를 통한 추정, roughness penalty, 함수 PCA 기반 추정, refund 패키지 구현, 비선형 함수 회귀를 포함한다.

**키워드**: `scalar-on-function regression`, `roughness penalty`, `refund package`, `functional PCA regression`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 4 (line 3698)

### Ch 5: Functional response models (pp. 67-100)

**핵심**: 함수 반응 모형의 최소제곱 및 벌점 최소제곱 추정을 다룬다. 함수 회귀변수, refund 패키지 구현, 효과 없음 검정, 함수 선형 모형의 타당성 검증을 포함한다.

**키워드**: `functional response`, `penalized least squares`, `test of no effect`, `model validation`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 5 (line 4880)

### Ch 6: Functional generalized linear models (pp. 101-116)

**핵심**: 함수 일반화 선형 모형(functional GLM)의 배경, 스칼라-on-함수 GLM, 함수 반응 GLM, refund 패키지 구현, DTI 데이터 적용을 다룬다.

**키워드**: `functional GLM`, `logistic regression`, `Poisson regression`, `DTI application`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 6 (line 7228)

### Ch 7: Sparse FDA (pp. 117-140)

**핵심**: 희소 함수 데이터(sparse FDA)의 분석을 다룬다. 평균 함수와 공분산 함수의 추정, 희소 함수 PCA, 희소 함수 회귀를 포함한다.

**키워드**: `sparse FDA`, `mean estimation`, `covariance estimation`, `PACE`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 7 (line 8078)

### Ch 8: Functional time series (pp. 141-178)

**핵심**: 함수 시계열의 기본 개념과 분석 방법을 다룬다. 함수 자기회귀(FAR) 과정, Hyndman-Ullah 예측법, 다변량 예측, 장기 공분산 함수, 정상성 검정, FAR(1) 모형의 존재 조건을 포함한다.

**키워드**: `functional time series`, `FAR`, `forecasting`, `stationarity test`, `long-run covariance`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 8 (line 9532)

### Ch 9: Spatial functional data and models (pp. 179-210)

**핵심**: 공간 통계의 기본 개념, 함수 공간장(functional spatial field), 함수 크리깅(functional kriging), 평균 함수 추정, R geofd 패키지 구현을 다룬다.

**키워드**: `spatial statistics`, `functional kriging`, `geofd package`, `spatial field`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 9 (line 11977)

### Ch 10: Elements of Hilbert space theory (pp. 211-232)

**핵심**: 힐베르트 공간의 기본 이론을 다룬다. 힐베르트 공간의 정의, 사영과 정규직교 집합, 선형 연산자, 스펙트럼 이론의 기초, 텐서 곱을 포함한다.

**키워드**: `Hilbert space`, `projection`, `spectral theory`, `linear operator`, `tensor`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 10 (line 13768)

### Ch 11: Random functions (pp. 233-248)

**핵심**: 거리 공간에서의 확률 원소, 힐베르트 공간에서의 기댓값과 공분산, 가우스 함수와 극한 정리, 함수 주성분의 이론적 기초를 다룬다.

**키워드**: `random element`, `expectation`, `covariance operator`, `Gaussian process`, `limit theorem`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 11 (line 14923)

### Ch 12: Inference from a random sample (pp. 249-288)

**핵심**: 확률 표본으로부터의 추론을 다룬다. 표본 평균과 공분산의 일치성, 추정된 주성분의 수렴, 점근 정규성, 평균에 대한 가설 검정, 신뢰 대역(confidence band), BOA 누적 수익률 적용을 포함한다.

**키워드**: `consistency`, `asymptotic normality`, `hypothesis testing`, `confidence band`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 12 (line 15730)
