---
name: "Introduction to Functional Data Analysis"
type: book-summary
sources:
  - file: "Kokoszka-IntroFDA_azure_full.md"
    tool: Document Intelligence
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

함수 데이터 분석(FDA)은 데이터셋에서 변수나 관심 단위가 매끄러운 곡선 또는 함수로 자연스럽게 간주될 수 있을 때 발생한다. FDA에서 가장 단순한 데이터는 공통 구간에서 관측된 N개의 곡선 표본이며, 관측점이 곡선마다 다를 수 있다. 기저 전개(basis expansion)는 이산 데이터를 함수 객체로 변환하는 핵심 기법으로, B-spline, Fourier, wavelet 등의 기저 함수를 선형 결합하여 곡선을 근사한다. 표본 평균 함수와 표본 공분산 함수는 함수 데이터의 가장 기본적인 요약 통계량이며, 공분산 함수는 두 시점 간 곡선 값의 공변을 나타내는 이변량 함수이다. 추정 함수 주성분(EFPC)은 평균으로부터의 편차를 최소 개수의 직교 함수로 근사하는 최적 기저를 제공하며, 각 주성분이 설명하는 변동 비율을 통해 차원 축소가 가능하다. BOA 주식의 분 단위 누적 로그수익률 데이터에 FDA를 적용하여 일중 수익률의 평균 함수, 신뢰 구간, 주성분을 분석하였으며, 결과가 브라운 운동과 유사한 패턴을 보였다. 확산 텐서 영상(DTI) 데이터에서는 뇌량(corpus callosum)의 부분 비등방성 트랙 프로파일 376개를 함수 객체로 변환하여 분석하였다. R의 fda 패키지와 refund 패키지가 기저 생성, 평활화, 함수 객체 조작에 사용되며, smooth.basis 함수로 원시 데이터를 함수 데이터 객체로 변환한다. 희소 데이터(sparse data)와 밀집 데이터(dense data)의 구분이 FDA에서 중요하며, 관측점 수에 따라 적합한 방법론이 달라진다. 함수 데이터의 형태(shape)가 개별 관측값보다 중요한 분석 대상이며, 이 장은 이후 장에서 다루는 고급 방법론의 기초를 제공한다.

### Ch 2: Further topics in exploratory FDA (pp. 21-36)

**핵심**: 미분, 벌점 스무딩(penalized smoothing), 곡선 정렬(curve alignment)을 다룬다. 스무딩 모수 선택, 곡선 등록의 기본 방법을 포함한다.

**키워드**: `derivatives`, `penalized smoothing`, `curve alignment`, `registration`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 2 (line 2437)

미분(derivative) 정보의 활용은 전통적 다변량 분석과 구별되는 FDA의 고유한 특징이다. 기저 전개로 표현된 함수의 k차 도함수는 기저 함수의 k차 도함수를 이용하여 근사할 수 있으며, Fourier 기저는 무한 미분 가능하나 B-spline은 차수에 의해 미분 가능 횟수가 제한된다. Matérn 과정을 시뮬레이션하여 B-spline 기반 도함수와 수치 도함수가 매우 유사함을 보였다. 벌점 스무딩(penalized smoothing)은 과적합과 과평활 사이의 균형을 위해 벌점화 제곱합(PSS)을 최소화하며, 선형 미분 연산자 L을 통한 벌점 항을 포함한다. 스무딩 모수 λ가 0이면 데이터를 정확히 통과하는 거친 곡선이 되고, λ가 크면 벌점 연산자에 의해 결정되는 매끄러운 곡선이 된다. 일반화 교차 검증(GCV)이 최적 λ 선택에 사용되며, 스무딩 수준에 따른 적합도와 복잡도의 트레이드오프를 정량화한다. 곡선 정렬(curve alignment) 또는 등록(registration)은 곡선 간의 위상 변동을 제거하여 진폭 변동만 남기는 기법이다. 성장 곡선 데이터에서 사춘기 성장 급증의 시기 차이를 보정하기 위해 곡선 등록이 적용되며, warping 함수를 통해 시간 축을 비선형 변환한다. 이 장에서 소개하는 미분, 벌점 스무딩, 곡선 정렬은 직접적인 스칼라 유사체가 없는 FDA 고유의 탐색적 분석 도구이다. fda 패키지의 deriv.fd 함수를 통해 함수 객체의 도함수를 계산할 수 있다.

### Ch 3: Mathematical framework for functional data (pp. 37-44)

**핵심**: 함수 데이터의 수학적 프레임워크를 제시한다. 제곱적분 가능 함수(L2 공간), 확률 함수(random function), 선형 변환의 기본 개념을 다룬다.

**키워드**: `L2 space`, `random function`, `linear transformation`, `square integrable`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 3 (line 3337)

FDA에서 추론을 수행하려면 관측된 함수를 적절한 공간의 원소로 취급해야 하며, 가장 편리한 설정은 제곱적분 가능 함수의 공간 L²이다. L² 공간에서 두 함수의 내적은 ⟨f,g⟩ = ∫f(t)g(t)dt로 정의되며, 이로부터 직교성, 노름, 거리 개념이 도출된다. 코시-슈바르츠 부등식 |⟨f,g⟩| ≤ ‖f‖·‖g‖는 L²에서의 핵심 관계식이다. 정규직교 기저에서는 Parseval 등식 ‖f‖² = Σ⟨f,eⱼ⟩²이 성립하며, 삼각함수는 정규직교 기저를, B-spline은 비직교 기저를 구성한다. 확률 함수 X는 확률 공간에서 L²로의 사상이며, E‖X‖² < ∞일 때 제곱적분 가능하다고 한다. 모평균 함수 μ(t) = EX(t)와 모공분산 함수 c(t,s) = E[(X(t)−μ(t))(X(s)−μ(s))]가 FDA의 핵심 모수이다. Karhunen-Loève 전개 X(t) = μ(t) + Σξⱼvⱼ(t)는 공분산 함수의 고유함수 vⱼ와 점수 ξⱼ로 확률 함수를 최적 표현하며, 고유값 λⱼ는 각 주방향의 분산을 나타낸다. 브라운 운동의 예에서 공분산 함수 c(t,s) = min(t,s), 고유함수 vⱼ(t) = √2 sin((j−1/2)πt), 고유값 λⱼ = 1/((j−1/2)²π²)의 닫힌 형태가 유도된다. 적분 연산자는 함수를 스칼라로 변환하는 L₁과 함수를 함수로 변환하는 L₂로 구분되며, 핵(kernel)이 ∬ψ²(t,s)dtds < ∞를 만족하면 힐베르트-슈미트 연산자라 한다. 공분산 연산자 C는 스펙트럼 분해 C(x) = Σλⱼ⟨x,vⱼ⟩vⱼ를 통해 대각적으로 표현된다.

### Ch 4: Scalar-on-function regression (pp. 45-66)

**핵심**: 스칼라 반응에 대한 함수 회귀를 다룬다. 기저 전개를 통한 추정, roughness penalty, 함수 PCA 기반 추정, refund 패키지 구현, 비선형 함수 회귀를 포함한다.

**키워드**: `scalar-on-function regression`, `roughness penalty`, `refund package`, `functional PCA regression`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 4 (line 3698)

함수 회귀 모형은 반응과 예측변수의 종류에 따라 스칼라-on-함수, 함수-on-스칼라, 함수-on-함수의 세 범주로 분류된다. 스칼라-on-함수 회귀에서 반응 Yᵢ는 스칼라이고 예측변수 Xᵢ(s)는 곡선이며, 모형은 Yᵢ = ∫β(s)Xᵢ(s)ds + εᵢ로 정의된다. 함수 모수 β는 무한 차원이므로 유한 표본에서 제약 없이 추정하면 완벽 적합이 가능하여 불안정한 추정이 된다. 기저 전개를 통한 추정에서는 β(s) ≈ ΣbₖBₖ(s)로 근사하고 최소제곱법으로 계수를 추정한다. roughness penalty 방법은 벌점화 제곱합을 최소화하여 추정 함수의 매끄러움을 보장하며, 스무딩 모수 λ는 GCV로 선택한다. 함수 PCA 기반 추정은 예측변수의 주성분 점수를 회귀변수로 사용하여 차원을 축소한다. 가솔린 옥탄가 예측, 고기 지방 함량 예측, DTI 데이터의 인지 점수 예측이 실제 응용 사례로 제시된다. refund 패키지의 pfr 함수가 스칼라-on-함수 회귀의 R 구현을 제공하며, 다양한 기저와 벌점 옵션을 지원한다. 비선형 함수 회귀로의 확장도 논의되며, 함수 예측변수의 비선형 변환을 포함하는 모형이 소개된다. 이산 인덱스 k를 연속 인덱스 s로 대체하는 것이 전통적 선형 모형과 함수 선형 모형의 핵심 차이이다.

### Ch 5: Functional response models (pp. 67-100)

**핵심**: 함수 반응 모형의 최소제곱 및 벌점 최소제곱 추정을 다룬다. 함수 회귀변수, refund 패키지 구현, 효과 없음 검정, 함수 선형 모형의 타당성 검증을 포함한다.

**키워드**: `functional response`, `penalized least squares`, `test of no effect`, `model validation`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 5 (line 4880)

함수-on-스칼라 회귀 모형은 Yᵢ(t) = Σxᵢₖβₖ(t) + εᵢ(t)로 정의되며, 반응이 함수이고 예측변수가 스칼라이다. 최소제곱 추정량은 각 시점 t에서 독립적으로 β̂(t) = (X'X)⁻¹X'Y(t)로 계산되며, 반응 함수가 매끈하면 점별 추정이 적절하다. 자동차 대시보드 설계를 위한 각도 운동 데이터에 함수-on-스칼라 회귀를 적용하여 목표 좌표(x,y,z)로부터 팔 각도 곡선을 예측하였다. 잔차 곡선의 EFPC 분석에서 운동 중간부의 변동성이 시작과 끝보다 크다는 것을 확인하였다. 벌점 최소제곱 추정은 반응이 잡음이 많을 때 기저 전개 β_ℓ(tⱼ) = Σbₗₖφₖ(tⱼ)와 벌점 항을 포함하여 매끈한 추정을 보장한다. 함수-on-함수 회귀는 Yᵢ(t) = α(t) + ∫ψ(t,s)Xᵢ(s)ds + εᵢ(t)로, 회귀 계수가 이변량 함수이다. 벡터화된 행렬과 크로네커 곱을 이용하여 벌점 추정량의 닫힌 형태 해가 유도된다. refund 패키지에서 함수 반응 모형의 적합을 지원하며, 효과 없음 검정(test of no effect)을 통해 예측변수의 유의성을 평가한다. 함수 선형 모형의 타당성 검증을 위해 잔차 곡선의 EFPC 분석과 진단 도표가 사용된다. 벌점 스무딩 모수 λ_ℓ은 각 회귀 함수별로 독립적으로 선택될 수 있다.

### Ch 6: Functional generalized linear models (pp. 101-116)

**핵심**: 함수 일반화 선형 모형(functional GLM)의 배경, 스칼라-on-함수 GLM, 함수 반응 GLM, refund 패키지 구현, DTI 데이터 적용을 다룬다.

**키워드**: `functional GLM`, `logistic regression`, `Poisson regression`, `DTI application`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 6 (line 7228)

일반화 선형 모형(GLM)은 비정규 반응(이진, 카운트, 양수 등)에 대해 평균과 예측변수 간의 비선형 관계를 링크 함수를 통해 선형화한다. 지수족 밀도는 f(y|θ,φ) = exp{(θy−b(θ))/a(φ) + c(y,φ)}로 표현되며, 평균은 E[Y] = b'(θ), 분산은 a(φ)b''(θ)이다. 로지스틱 회귀에서 정준 링크 함수는 logit(p) = log(p/(1−p))이며, 최대우도 추정은 Newton-Raphson을 통해 추정 방정식을 풀어 수행된다. 스칼라-on-함수 GLM에서는 ηₙ = g(μₙ) = α + ∫Xₙ(t)β(t)dt로, 함수 예측변수를 기저 전개하고 벌점을 부과하여 β(t)를 추정한다. 함수 반응 GLM에서는 각 시점 t에서 Yₙ(t)가 GLM을 따른다고 가정하고, ηₙ(t) = α(t) + xₙβ(t)로 시간에 따라 변하는 모수를 허용한다. 함수-on-함수 GLM에서는 ηₙ(t) = α(t) + ∫Xₙ(s)β(t,s)ds로 이변량 회귀 계수를 추정한다. refund 패키지의 pffr 함수가 함수 GLM의 적합을 지원하며, 정규 및 비정규 설계 모두를 처리한다. 시뮬레이션에서 Matérn 가우스 과정을 잠재 변수로 사용하여 함수 probit 모형의 데이터를 생성하였다. DTI 데이터에 함수 로지스틱 회귀를 적용하여 부분 비등방성 프로파일로부터 다발성 경화증 여부를 예측하였다. 무한 차원에서의 밀도 정의 문제로 인해 함수 GLM은 적률 추정과 추정 방정식에 기반하는 접근법을 사용한다.

### Ch 7: Sparse FDA (pp. 117-140)

**핵심**: 희소 함수 데이터(sparse FDA)의 분석을 다룬다. 평균 함수와 공분산 함수의 추정, 희소 함수 PCA, 희소 함수 회귀를 포함한다.

**키워드**: `sparse FDA`, `mean estimation`, `covariance estimation`, `PACE`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 7 (line 8078)

희소 함수 데이터는 종단 연구에서 각 피험자가 소수의 불규칙 시점에서만 관측되는 경우 발생하며, 개별 곡선 수준의 스무딩이 아닌 피험자 간 정보 풀링(pooling)에 기반한 방법론이 필요하다. 관측 모형은 Yₙₘ = μ(tₙₘ) + εₙ(tₙₘ) + δₙₘ으로, 피험자 특이적 오차 εₙ과 측정 잡음 δₙₘ을 구분한다. 커널 스무딩에서 편향과 분산의 트레이드오프를 분석하면, 피험자당 관측 수 M이 N^(1/4)보다 빠르게 증가할 때 모수적 수렴 속도 N⁻¹에 도달한다. M이 고정이면 비모수적 수렴 속도 N^(-4/5)를 얻으며, 이 경계가 희소 방법론의 적절성을 판단하는 경험 규칙이 된다. 평균 함수 추정에는 국소 다항 회귀, 기저 전개, 재생 핵 힐베르트 공간(RKHS) 방법이 사용된다. Nadaraya-Watson 추정량은 커널 함수 K를 이용하여 각 시점 t에서 국소 상수를 적합하며, 국소 선형 추정은 경계 편향이 적다. 공분산 함수 추정은 교차곱 Yₙₘ₁Yₙₘ₂를 이변량 국소 다항으로 스무딩하되, 대각선(m₁=m₂) 항은 측정 오차를 포함하므로 제외한다. 희소 함수 PCA(PACE)는 추정된 공분산 함수의 고유분석과 조건부 기대를 통해 개별 곡선의 주성분 점수를 예측한다. 황반 변성 임상시험(CATT) 데이터에서 시각 민감도 점수를 희소 함수 데이터로 분석하여 치료 효과를 평가하였다. 희소 함수 회귀는 예측된 주성분 점수를 사용하여 스칼라 또는 함수 반응 모형을 적합한다.

### Ch 8: Functional time series (pp. 141-178)

**핵심**: 함수 시계열의 기본 개념과 분석 방법을 다룬다. 함수 자기회귀(FAR) 과정, Hyndman-Ullah 예측법, 다변량 예측, 장기 공분산 함수, 정상성 검정, FAR(1) 모형의 존재 조건을 포함한다.

**키워드**: `functional time series`, `FAR`, `forecasting`, `stationarity test`, `long-run covariance`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 8 (line 9532)

함수 시계열은 시간 순서로 관측된 곡선들로, 독립 동일 분포 가정이 성립하지 않는다. 정상성(stationarity)은 기대값과 자기공분산이 시간 인덱스 n에 의존하지 않을 때 성립하며, 자기공분산 함수 γₕ = Cov(Xₙ, Xₙ₊ₕ)는 정상 모형에서만 정의된다. 함수 자기회귀 과정 FAR(1)은 Xₙ(t) = ∫φ(t,s)Xₙ₋₁(s)ds + εₙ(t)로 정의되며, ∬φ²(t,s)dtds < ∞이면 정상 해가 존재한다. FAR(1)의 자기회귀 연산자 Φ는 Φ = C₁C⁻¹ 관계식을 통해 추정되며, 공분산 연산자의 유사역행렬(pseudo-inverse)을 사용하여 불안정성을 제어한다. Hyndman-Ullah 예측법은 Karhunen-Loève 전개의 절단된 점수에 대해 단변량 시계열 예측을 적용하여 미래 곡선을 예측한다. 미국 사망률 곡선 데이터에 이 방법을 적용하여 연도별 로그 사망률 곡선의 미래 패턴을 예측하였다. 장기 공분산 함수(long-run covariance)는 종속 함수 시계열에서의 추론에 사용되며, 핵 추정량과 대역폭 선택이 필요하다. 함수 정상성 검정은 확률적 추세의 존재 여부를 KPSS 유형 통계량으로 평가한다. FAR(1) 모형은 R의 fda 패키지에서 시뮬레이션과 추정이 가능하며, 커널 추정량의 계산은 pca.fd 함수의 출력을 직접 활용한다. FAR(p) 과정으로의 확장도 가능하나, 실제 함수 시계열 분석에서 FAR(1)이 지배적으로 사용된다.

### Ch 9: Spatial functional data and models (pp. 179-210)

**핵심**: 공간 통계의 기본 개념, 함수 공간장(functional spatial field), 함수 크리깅(functional kriging), 평균 함수 추정, R geofd 패키지 구현을 다룬다.

**키워드**: `spatial statistics`, `functional kriging`, `geofd package`, `spatial field`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 9 (line 11977)

공간 함수 데이터는 공간 위치 sₖ에서 관측된 곡선 X(sₖ)의 집합으로, 기상 관측소의 기온 곡선 등이 대표적 예이다. 기존 공간 통계에서는 스칼라 관측값을 다루지만, 함수 공간장은 각 위치에서 L² 원소인 확률 함수를 관측한다. 2차 정상성과 등방성 가정 하에서 공간 공분산 함수 C(h;t,u) = Cov(X(s;t), X(s+h;u))가 정의된다. 스칼라 공간 데이터에서 크리깅은 관측된 값들의 가중 선형 결합으로 미관측 위치의 값을 예측하며, 가중치는 예측 오차의 분산을 최소화하도록 결정된다. 함수 크리깅에서는 예측 기준이 E‖X̂(s)−X(s)‖²로 확장되며, 함수 공간 공분산 C(s,s') = E[⟨X(s)−μ, X(s')−μ⟩]를 이용한다. 크리깅 가중치를 구하는 선형 방정식 체계는 스칼라 경우와 형식적으로 동일하나, 공분산이 함수 내적에 기반한다. 반변동도(semivariogram) 추정을 통해 공간 공분산 함수를 모수화하며, 지수형과 Matérn 상관 함수가 사용된다. 평균 함수의 공간 추정에서는 가중 평균을 사용하되, 가까운 위치의 관측에 작은 가중치를 부여하여 정보의 중복을 보정한다. R의 geofd 패키지가 함수 공간 데이터의 크리깅과 평균 추정을 지원한다. 격자 데이터, 지역 데이터, 점 과정 데이터 등 다양한 공간 데이터 구조도 함수적 확장이 가능하다.

### Ch 10: Elements of Hilbert space theory (pp. 211-232)

**핵심**: 힐베르트 공간의 기본 이론을 다룬다. 힐베르트 공간의 정의, 사영과 정규직교 집합, 선형 연산자, 스펙트럼 이론의 기초, 텐서 곱을 포함한다.

**키워드**: `Hilbert space`, `projection`, `spectral theory`, `linear operator`, `tensor`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 10 (line 13768)

벡터 공간은 덧셈과 스칼라 곱의 공리를 만족하는 집합이며, 내적 공간은 대칭성, 양정치성, 쌍선형성을 만족하는 내적이 정의된 벡터 공간이다. 내적으로부터 ‖x‖ = √⟨x,x⟩로 노름이 유도되며, 코시-슈바르츠 부등식과 삼각 부등식이 성립한다. 완비 내적 공간을 힐베르트 공간이라 하며, 모든 코시 수열이 극한을 가진다. ℓ² 공간은 제곱합 가능 수열의 힐베르트 공간이고, L²[0,1]은 제곱적분 가능 실함수의 힐베르트 공간이다. 소볼레프 공간 H^K(T)는 K차 도함수까지 제곱적분 가능한 함수의 공간으로, 도함수를 내적에 포함한다. 닫힌 부분공간 G에 대한 사영 정리는 임의의 x ∈ H를 P(x) ∈ G와 Q(x) ∈ G⊥로 유일하게 분해할 수 있음을 보장한다. Riesz 표현 정리는 힐베르트 공간의 모든 연속 선형 범함수 L(x)를 내적 ⟨x,y⟩ 형태로 표현할 수 있음을 증명한다. 유계 선형 연산자의 연산자 노름 ‖L‖ = sup{‖L(x)‖ : ‖x‖ ≤ 1}이 정의되며, 수반 연산자 L*은 ⟨L(x),y⟩ = ⟨x,L*(y)⟩를 만족한다. 콤팩트 연산자의 스펙트럼 정리는 고유값과 고유함수로의 분해를 보장하며, 공분산 연산자의 FPCA 이론적 기초가 된다. 텐서 곱 x⊗y와 힐베르트-슈미트 공간은 공분산 연산자의 통계적 추론에서 핵심 도구이다.

### Ch 11: Random functions (pp. 233-248)

**핵심**: 거리 공간에서의 확률 원소, 힐베르트 공간에서의 기댓값과 공분산, 가우스 함수와 극한 정리, 함수 주성분의 이론적 기초를 다룬다.

**키워드**: `random element`, `expectation`, `covariance operator`, `Gaussian process`, `limit theorem`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 11 (line 14923)

거리 공간에서의 확률 원소는 보렐 σ-대수에 대한 가측 사상으로 정의되며, 함수 공간에서의 확률 원소를 확률 함수라 한다. 약수렴(weak convergence)은 모든 유계 연속 함수에 대한 적분의 수렴으로 정의되며, 확률 수렴과 분포 수렴의 관계가 성립한다. 연속 사상 정리(continuous mapping theorem)에 의해 Xₙ →d X이면 h(Xₙ) →d h(X)이다. 슬루츠키 정리(Slutsky's theorem)는 Xₙ →d X이고 Yₙ →P a이면 (Xₙ,Yₙ) →d (X,a)임을 보장한다. 힐베르트 공간에서 확률 함수 X의 기대값 EX는 E[⟨X,y⟩] = ⟨EX,y⟩를 만족하는 유일한 원소로 정의된다. 공분산 연산자 C(y) = E[⟨X−EX,y⟩(X−EX)]는 대칭, 비음정치, 핵(nuclear) 연산자이며, 고유값의 합이 유한하다. 가우스 확률 함수는 특성 범함수가 φ_X(y) = exp{i⟨μ,y⟩ − ⟨C(y),y⟩/2}인 함수이며, 모든 선형 사영 ⟨y,X⟩가 정규분포를 따르는 것과 동치이다. 힐베르트 공간의 중심극한정리는 iid 제곱적분 가능 확률 함수에 대해 N⁻¹/²Σ(Xᵢ−μ) →d Z를 보장하며, Z는 공분산 연산자 C를 가진 가우스 원소이다. Karhunen-Loève 전개에서 X(t) = μ(t) + Σξⱼvⱼ(t)의 점수 ξⱼ는 비상관이고 Eξⱼ² = λⱼ이며, X가 가우스이면 점수도 독립 정규이다. 브라운 운동(위너 과정)은 가우스 확률 함수의 대표적 예로, 독립 증분과 연속 경로를 가진다.

### Ch 12: Inference from a random sample (pp. 249-288)

**핵심**: 확률 표본으로부터의 추론을 다룬다. 표본 평균과 공분산의 일치성, 추정된 주성분의 수렴, 점근 정규성, 평균에 대한 가설 검정, 신뢰 대역(confidence band), BOA 누적 수익률 적용을 포함한다.

**키워드**: `consistency`, `asymptotic normality`, `hypothesis testing`, `confidence band`

**상세**: → `Introduction to functional data analysis-Chapman & Hall _ CRC (2017) - (Chapman & Hall_CRC texts in statistical science series) Kokoszka, Piotr_ Reimherr, Matthew.md` Ch 12 (line 15730)

iid 확률 표본 X₁,...,Xₙ ∈ L²에서 표본 평균 μ̂는 비편향이며 E‖μ̂−μ‖² = O(N⁻¹)의 L²-일치 추정량이다. E‖X‖⁴ < ∞ 조건 하에서 표본 공분산 연산자 Ĉ는 힐베르트-슈미트 노름에서 E‖Ĉ−C‖²_S ≤ N⁻¹E‖X‖⁴로 일치성이 보장된다. 추정 함수 주성분(EFPC) v̂ⱼ와 추정 고유값 λ̂ⱼ는 각각 N⁻¹/² 속도로 참값에 수렴하며, 이는 완전 관측 가능한 함수의 모수적 수렴 속도이다. 고유값의 단순성 가정 λ₁ > λ₂ > ··· > λₚ > λₚ₊₁은 EFPC의 일치성과 고유 방향 결정에 필수적이다. EFPC는 v̂ⱼ의 부호가 결정되지 않으므로, 부호 ĉⱼ = sign(⟨v̂ⱼ,vⱼ⟩)를 보정한 후 수렴이 논의된다. 점근 정규성에 기반하여 평균 함수에 대한 가설 검정과 동시 신뢰 대역(confidence band) 구축이 가능하다. 누적 분산 비율(CPV) 방법은 CPV(p) = Σₖ₌₁ᵖλ̂ₖ/ΣₖΣ̂ₖ가 85%를 초과하는 p를 선택하며, 스크리 도표는 고유값의 급감 지점으로 p를 결정한다. BOA 누적 일중 수익률 데이터에 평균 검정과 신뢰 대역을 적용하여 장기 평균 수익률 패턴을 추론하였다. 텐서 곱 표현 X⊗X를 사용한 공분산 추정의 대안적 증명도 제시되며, 텐서 공간과 힐베르트-슈미트 공간의 노름 동치가 활용된다. 정상 함수 시계열로의 확장도 가능하며, 종속성이 충분히 빨리 감소하면 동일한 수렴 결과가 성립한다.
