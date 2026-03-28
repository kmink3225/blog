---
name: "Functional Data Analysis"
type: book-summary
sources:
  - file: "Ramsay-FunctionalDataAnalysis_azure_full.md"
    tool: Document Intelligence
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

함수 데이터는 매끈한 함수의 이산 관측값으로, 스위스 남아 성장 데이터(29개 시점의 키)가 대표적 예이다. 가속도 곡선(2차 도함수)에서 사춘기 성장 급증과 약 6세의 중간 급증(mid-spurt)이 관찰되며, 도함수 분석은 FDA의 핵심 도구이다. 캐나다 기상 데이터에서 월평균 기온과 강수량의 매끈한 함수 표현을 통해 지역 간 기후 패턴을 비교한다. 보행 분석에서 무릎 각도와 고관절 각도의 주기적 곡선이 함수 데이터로 다루어지며, 시간 변환(registration)이 필요하다. FDA의 주요 목표는 데이터 표현(스무딩, 보간), 등록(registration), 요약 통계(평균, 공분산, 상관 함수), 함수 PCA, 함수 선형 모형 등이다. 관측 시점의 불등 간격과 곡선별 상이한 관측 시점이 다변량 분석과의 핵심 차이이며, 함수적 관점이 이를 자연스럽게 처리한다. 함수 PCA는 곡선 간 변동의 주요 모드를 추출하되, 시기 변동과 강도 변동의 분리가 필요하다. 미분의 활용은 FDA를 전통적 다변량 분석과 구별하는 가장 중요한 특징이며, 위상 평면 그림과 미분 방정식 모형이 이를 실현한다. 정칙화(regularization)는 함수 모수 추정에서 반복적으로 등장하는 주제이다. 이 장은 FDA의 전반적 목표, 방법론적 방향, 주요 응용 분야를 조망한다.

### Ch 2: Notation and techniques (pp. 23-36)

**핵심**: FDA에 사용되는 수학적 표기법과 기본 기법을 소개한다. 내적(inner product), 사영(projection), 다변량 선형 모형, 정칙화(regularization)의 개념을 함수 공간으로 확장한다.

**키워드**: `inner product`, `projection`, `regularization`, `linear model`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 2 (line 3157)

FDA에 사용되는 표기법에서 스칼라, 벡터, 함수를 구분하지 않는 통합 표기를 채택하며, 전치는 x'으로, m차 도함수는 D^m x로 표기한다. 내적 ⟨x,y⟩는 벡터의 x'y = Σxᵢyᵢ, 함수의 ∫x(t)y(t)dt, 가중 내적 ∫x(t)y(t)w(t)dt 등을 통합하는 핵심 장치이다. 내적은 대칭성(⟨x,y⟩ = ⟨y,x⟩), 양정치성(⟨x,x⟩ ≥ 0), 쌍선형성의 세 성질을 만족한다. 사영(projection) 개념이 함수 공간으로 확장되며, 부분공간 V 위로의 사영 Pₓ는 ‖x−Pₓ‖을 최소화한다. 다변량 선형 모형 Y = Xβ + E에서 최소제곱 추정량 β̂ = (X'X)⁻¹X'Y가 함수 설정으로의 확장을 위한 참조점이 된다. 정칙화(regularization)는 X'X가 비특이(non-singular)가 아닐 때 벌점 항을 추가하여 안정적 추정을 가능하게 한다. 함수 설정에서는 적합도와 매끈함의 균형이 벌점 매개변수 λ를 통해 조절된다. 크로네커 곱과 vec 연산이 다변량-함수 모형의 행렬 표현에 사용된다. 가중 내적 ⟨x,y⟩_w = ∫x(t)y(t)w(t)dt는 특정 구간에서의 적합도에 차등 가중을 부여한다. 이 장의 표기법과 기법은 이후 모든 장에서 반복적으로 활용된다.

### Ch 3: Representing functional data as smooth functions (pp. 37-56)

**핵심**: 관측된 이산 데이터를 평활 함수로 표현하는 방법을 다룬다. 기저 함수 방법(Fourier, 다항식, B-spline, wavelet), 커널 스무딩, 국소 가중치 방법, 대역폭 선택을 포함한다.

**키워드**: `basis function`, `B-spline`, `Fourier`, `kernel smoothing`, `bandwidth`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 3 (line 3898)

관측된 이산 데이터 yⱼ = x(tⱼ) + εⱼ를 평활 함수 x로 변환하는 방법을 다루며, 함수 데이터의 기본 철학은 관측값 집합이 아닌 단일 함수 실체로 사고하는 것이다. 기저 함수 방법에서 x(t) ≈ Σcₖφₖ(t)로 표현하며, Fourier 기저(주기적 데이터), B-spline(비주기적 데이터), wavelet(국소 변동), 다항식 기저 등이 사용된다. Fourier 기저는 주기적 데이터에 최적이며 직교성으로 계산이 효율적이나, 비주기적 데이터에는 부적절하다. B-spline은 국소 지지(local support)를 가져 계산이 효율적이고, 매듭(knot) 위치와 차수로 유연성을 조절한다. 커널 스무딩은 Nadaraya-Watson 추정량을 사용하며, 대역폭 h가 편향-분산 트레이드오프를 조절한다. 국소 다항 적합은 각 점 t₀에서 가중 다항 회귀를 수행하며, 국소 선형 적합은 경계 편향이 적다. 관측 시점 간격과 곡률의 상대적 밀도가 함수 복원의 품질을 결정하며, 잡음 수준과 결합하여 분석 가능성을 제한한다. 도함수 추정은 원 함수보다 더 높은 관측 밀도를 요구하며, 인접 관측값의 차분을 직접 사용하면 잡음이 증폭된다. 필기 데이터(600Hz)에서도 높은 곡률 때문에 충분한 해상도가 필요하다. 기저 계수의 추정은 최소제곱법 min Σ(yⱼ − Σcₖφₖ(tⱼ))²을 통해 수행된다.

### Ch 4: The roughness penalty approach (pp. 57-66)

**핵심**: 스플라인 스무딩과 roughness penalty 접근법을 다룬다. 적합도와 평활도 간의 균형, 미분의 스무딩, 정칙화된 기저 접근법과 그 성질을 설명한다.

**키워드**: `roughness penalty`, `spline smoothing`, `regularized basis`, `smoothing parameter`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 4 (line 4993)

roughness penalty 접근법은 적합도와 매끈함의 명시적 트레이드오프를 통해 기저 전개와 커널 스무딩의 한계를 극복한다. 벌점화 잔차 제곱합 PENSSE_λ(x|y) = Σ(yⱼ−x(tⱼ))² + λ·PEN₂(x)에서 PEN₂(x) = ∫(D²x(s))²ds는 곡선의 총 곡률을 측정한다. 스무딩 모수 λ가 크면 직선에 가까운 추정이, λ→0이면 데이터를 보간하는 가장 매끈한 곡선이 얻어진다. 최적 λ는 일반화 교차 검증(GCV) 기준 GCV(λ) = (n·SSE)/(n−df(λ))²으로 선택하며, df(λ)는 스무딩 행렬의 대각합(trace)이다. 스플라인 스무딩의 해는 관측점을 매듭으로 하는 자연 큐빅 스플라인이며, O(n) 알고리즘으로 효율적 계산이 가능하다. 미분의 스무딩에서는 D^m x의 추정을 위해 m차 도함수의 roughness에 벌점을 부과한다. 정칙화된 기저 접근법은 대규모 기저 집합에 벌점을 부과하여 적합도를 유지하면서 매끈함을 보장한다. 벌점 행렬 R = ∫(Dφₖ)(Dφₗ)dt는 기저 함수의 도함수 간 내적으로 구성된다. 이 접근법은 곡선 추정뿐 아니라 함수 PCA, 함수 회귀 등 다양한 FDA 문제로 자연스럽게 확장된다. Green과 Silverman(1994)이 논의한 일반화 선형 모형으로의 확장도 가능하다.

### Ch 5: Registration and display of functional data (pp. 67-84)

**핵심**: 곡선 등록(registration) 문제를 다룬다. 이동 등록(shift registration), 특징점 등록(landmark registration), 비선형 시간 변환(time warping), Newton-Raphson 알고리즘을 이용한 추정을 포함한다.

**키워드**: `registration`, `landmark alignment`, `time warping`, `curve alignment`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 5 (line 5463)

등록(registration)은 곡선 간의 위상 변동을 제거하여 특징의 시기를 정렬하는 과정이며, 이동 등록(shift registration)이 가장 단순한 형태이다. 이동 등록에서 각 곡선 xᵢ(t+δᵢ)의 이동량 δᵢ는 등록된 곡선의 변동을 최소화하도록 결정한다. 특징점 등록(landmark registration)은 곡선의 특정 특징(극대, 극소, 영점 교차 등)을 미리 식별하여 해당 시점을 일치시키는 방법이다. 비선형 시간 변환(time warping)에서 warping 함수 hᵢ(t)는 순단조 증가여야 하며, hᵢ(0) = 0, hᵢ(T₀) = Tᵢ의 경계 조건을 만족한다. Newton-Raphson 알고리즘을 이용한 연속 등록은 warping 함수를 반복적으로 갱신하여 최적 정렬을 달성한다. 등록 기준으로 곡선 간 제곱 거리의 최소화 또는 곡선 면적의 최대화가 사용된다. 등록 과정에서 목표 함수 x₀는 표본 평균에서 시작하여 등록된 곡선의 평균으로 갱신된다. 성장 데이터에서 사춘기 성장 급증의 시기 변동을 등록을 통해 제거하면, 평균 속도 곡선이 더 선명한 단일 피크를 보인다. warping 함수 자체의 분석은 위상 변동의 체계적 패턴을 드러낸다. 등록의 표시 방법으로는 원 곡선과 등록된 곡선의 병렬 표시, warping 함수 그래프, 등록 전후 평균 곡선 비교가 사용된다.

### Ch 6: Principal components analysis for functional data (pp. 85-110)

**핵심**: 함수 PCA의 정의, 다변량 PCA와의 관계, 고유분석(eigenanalysis), 결과 시각화(평균 변동, 주성분 점수), 이변량/다변량 함수 PCA, 계산 방법(이산화, 기저 전개)을 다룬다.

**키워드**: `functional PCA`, `eigenfunction`, `variance explained`, `principal component scores`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 6 (line 6418)

함수 PCA는 곡선 집합의 변동을 직교 고유함수(principal component function)로 분해하며, 다변량 PCA의 함수적 확장이다. 공분산 함수 v(s,t)의 고유분석에서 ∫v(s,t)ξⱼ(s)ds = ρⱼξⱼ(t)를 만족하는 고유함수 ξⱼ와 고유값 ρⱼ를 구한다. 각 곡선 xᵢ의 j번째 주성분 점수는 fᵢⱼ = ⟨xᵢ−μ, ξⱼ⟩ = ∫(xᵢ(t)−μ(t))ξⱼ(t)dt로 계산된다. 결과 시각화에서 평균 함수 ± c·√ρⱼ·ξⱼ(t)를 그려 각 주성분의 효과를 직관적으로 파악한다. 주성분이 설명하는 변동 비율은 ρⱼ/Σρₖ로 측정되며, 소수의 주성분으로 전체 변동의 대부분을 설명할 수 있다. 이변량/다변량 함수 PCA에서는 여러 함수 변수(예: 무릎 각도와 고관절 각도)를 결합하여 동시 분석한다. 계산적으로 이산화(discretization) 방법과 기저 전개 방법이 있으며, 기저 전개에서는 B = Φ'CΦ 행렬의 고유분석으로 환원된다. 주성분 점수의 산점도와 상자 그림을 통해 군집이나 이상치를 탐색한다. 캐나다 기온 데이터에서 제1주성분은 기온의 전반적 수준 차이를, 제2주성분은 여름 대 겨울의 대비를 나타낸다. 기저 전개 계수의 공분산 행렬에 대한 고유분석으로 함수 PCA를 효율적으로 수행할 수 있다.

### Ch 7: Regularized principal components analysis (pp. 111-124)

**핵심**: roughness penalty를 이용한 정칙화 PCA를 다룬다. 교차 검증을 통한 스무딩 모수 선택, pinch force 데이터 예제, 데이터 vs PCA 스무딩의 비교를 포함한다.

**키워드**: `regularized PCA`, `cross-validation`, `smoothing`, `roughness penalty`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 7 (line 8222)

roughness penalty를 이용한 정칙화 PCA는 고유함수의 과적합을 방지하여 더 해석 가능하고 안정적인 주성분을 산출한다. 벌점화 고유분석에서 ∫v(s,t)ξ(s)ds − λ∫(D²ξ(s))²ds를 최대화하여 정칙화된 고유함수를 구한다. 교차 검증을 통해 스무딩 모수 λ를 선택하며, leave-one-curve-out 방식이 사용된다. 데이터 스무딩(개별 곡선의 평활화)과 PCA 스무딩(고유함수의 평활화)은 구별되며, 두 접근의 효과가 비교된다. pinch force 데이터 예제에서 잡음이 심한 원시 곡선에 대해 정칙화 PCA가 더 매끈한 고유함수를 산출한다. 정칙화 PCA에서 고유함수의 직교성은 ⟨ξⱼ,ξₖ⟩ = δⱼₖ로 유지되나, roughness penalty에 의한 가중 직교성도 고려된다. 잡음이 적은 데이터에서는 정칙화의 효과가 미미하나, 잡음이 큰 경우 추정 안정성이 크게 향상된다. 정칙화 수준에 따라 설명되는 변동 비율이 달라지며, 과도한 정칙화는 정보 손실을, 불충분한 정칙화는 잡음 포함을 초래한다. 기저 전개와 정칙화의 결합에서 벌점 행렬 R이 기저 함수의 roughness를 반영한다. 이 장은 FDA에서 정칙화가 단순한 곡선 스무딩을 넘어 통계적 분석 도구에도 적용됨을 보여준다.

### Ch 8: PCA of mixed data (pp. 125-138)

**핵심**: 함수 데이터와 벡터 데이터가 혼합된 경우의 PCA를 다룬다. 함수와 벡터 공간의 결합, 등록과 PCA의 동시 수행, 기온 데이터와 시간 이동 효과의 균형을 포함한다.

**키워드**: `mixed data PCA`, `hybrid data`, `registration with PCA`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 8 (line 9061)

혼합 데이터 PCA는 함수 변수와 스칼라/벡터 변수가 공존하는 경우의 주성분 분석을 다룬다. 함수 공간 L²와 유한 차원 공간 ℝᵈ의 결합에서 내적을 정의하여 통합 PCA를 수행한다. 등록(registration)과 PCA를 동시에 수행하는 방법이 제시되며, 위상 변동이 진폭 변동과 혼합된 경우에 유용하다. 캐나다 기온 데이터에서 시간 이동(time shift) 변수와 기온 함수를 결합한 혼합 PCA를 적용한다. 등록 전후의 PCA 결과 비교에서 등록이 진폭 변동의 해석을 명확하게 한다. 혼합 데이터에서 함수 변수와 스칼라 변수의 상대적 스케일링이 결과에 영향을 미치며, 적절한 가중치 선택이 필요하다. 위상 변동을 별도의 스칼라 변수로 추출하면, 등록된 곡선의 PCA가 순수한 진폭 변동을 포착한다. 기저 전개 표현에서 함수 계수와 스칼라 변수를 하나의 확장 벡터로 결합하여 공분산 행렬을 구성한다. 다변량 함수 데이터(여러 함수 변수의 동시 분석)로의 확장에서 각 변수의 스케일 차이를 고려한 가중 내적이 사용된다. 이 장은 함수 데이터와 전통적 데이터를 통합 분석하는 프레임워크를 제공한다.

### Ch 9: Functional linear models (pp. 139-156)

**핵심**: 함수 선형 모형과 함수 ANOVA를 다룬다. 모형 적합, 적합도 평가, 걷는 말의 힘판(force plate) 데이터 분석, 계산적 이슈(기저 전개, 정칙화)를 포함한다.

**키워드**: `functional ANOVA`, `functional linear model`, `pointwise test`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 9 (line 9973)

함수 선형 모형과 함수 분산분석(ANOVA)은 다변량 선형 모형의 함수적 확장으로, 반응과/또는 예측변수가 함수이다. 함수 ANOVA에서 Yᵢⱼ(t) = μ(t) + αⱼ(t) + εᵢⱼ(t) 모형은 그룹별 효과 함수 αⱼ(t)를 추정한다. 점별(pointwise) 적합은 각 시점 t에서 독립적인 선형 모형을 적용하여 모수 함수를 추정한다. 걷는 말의 힘판(force plate) 데이터에 함수 ANOVA를 적용하여 다리 위치별 지면 반력 패턴의 차이를 분석한다. 적합도 평가에서 점별 F-검정과 전역 검정을 결합하며, 다중 비교 보정이 필요할 수 있다. 기저 전개를 이용한 계산에서 반응과 모수 함수를 동일 기저로 전개하면 행렬 연산으로 환원된다. 정칙화된 함수 선형 모형에서는 모수 함수에 roughness penalty를 부과하여 매끈한 추정을 보장한다. 잔차 곡선의 분석을 통해 모형의 적합성을 진단하며, 잔차의 자기상관 패턴이 모형 부적합을 시사할 수 있다. 교호작용 효과의 함수적 표현과 해석도 논의된다. 이 장은 실험 설계와 관측 연구에서의 함수 데이터 분석 프레임워크를 확립한다.

### Ch 10: Functional linear models for scalar responses (pp. 157-178)

**핵심**: 함수를 예측변수로, 스칼라를 반응변수로 하는 회귀 모형을 다룬다. 정칙화 방법(이산화, 기저 함수, roughness penalty), 교차 검증, 적분 방정식과의 관계를 포함한다.

**키워드**: `scalar-on-function regression`, `regularization`, `cross-validation`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 10 (line 11059)

스칼라 반응에 대한 함수 예측변수 회귀 모형 Yᵢ = α + ∫β(s)Xᵢ(s)ds + εᵢ에서 회귀 함수 β(s)는 무한 차원 모수이다. 이산화 방법에서 β(sⱼ)를 유한 격자점에서 추정하면 p > n 문제가 발생하여 정칙화가 필수적이다. 기저 함수 방법에서 β(s) ≈ ΣbₖBₖ(s)로 전개하고 최소제곱 추정량 b̂ = (Z'Z)⁻¹Z'Y를 구하며, Zᵢₖ = ∫Xᵢ(s)Bₖ(s)ds이다. roughness penalty 방법에서 PENSSE(β) = Σ(Yᵢ−α−⟨Xᵢ,β⟩)² + λ∫(D²β(s))²ds를 최소화한다. 교차 검증(leave-one-out)으로 스무딩 모수 λ와 기저 차원 K를 동시에 선택한다. 캐나다 기온 데이터에서 연간 강수량을 반응, 일일 기온 곡선을 예측변수로 하는 함수 회귀를 적합한다. 추정된 β(s) 함수의 해석에서 양의 β(s) 구간은 해당 시기의 높은 기온이 많은 강수와 연관됨을 의미한다. 적분 방정식 관점에서 정상 방정식 ∫v(s,t)β(t)dt = cov(X(s),Y)는 Fredholm 제1종 적분 방정식이며, 역문제(ill-posed problem)의 특성을 가진다. 함수 PCA 기반 회귀에서 주성분 점수를 예측변수로 사용하면 자동적으로 차원 축소와 정칙화가 이루어진다. 이 장은 함수 예측변수 회귀의 이론적 기초와 실제 적용을 체계적으로 다룬다.

### Ch 11: Functional linear models for functional responses (pp. 179-198)

**핵심**: 함수 예측변수와 함수 반응변수를 모두 포함하는 모형을 다룬다. 기저 표현을 이용한 추정, 정칙화, 적합도 평가, 이변량 roughness penalty를 포함한다.

**키워드**: `function-on-function regression`, `bivariate roughness penalty`, `basis expansion`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 11 (line 12242)

함수 반응 모형 Yᵢ(t) = α(t) + ∫β(t,s)Xᵢ(s)ds + εᵢ(t)에서 회귀 계수 β(t,s)는 이변량 함수이다. 기저 표현에서 β(t,s) ≈ ΣΣbₖₗφₖ(t)ψₗ(s)로 전개하면 계수 행렬 B의 추정 문제로 환원된다. 정칙화는 β의 t 방향과 s 방향 모두에 roughness penalty를 부과하는 이변량 벌점을 사용한다. 적합도 평가에서 점별 잔차와 전역 잔차 지표를 결합하여 모형의 적합성을 진단한다. 기저 함수의 선택에서 반응과 예측변수의 특성(주기성, 매끈함)에 맞는 적절한 기저 체계가 필요하다. 캐나다 기상 데이터에서 일일 기온 곡선으로부터 일일 강수 곡선을 예측하는 함수-on-함수 회귀를 적합한다. 추정된 β(t,s) 표면의 등고선도는 기온과 강수 간의 시간적 연관 구조를 드러낸다. 과거 이력(concurrent/historical) 모형에서 β(t,s) = 0 for s > t를 부과하면 인과적 해석이 가능하다. 정칙화 수준에 따라 β 표면의 매끈함이 달라지며, 교차 검증으로 최적 수준을 선택한다. 이 장은 함수-on-함수 회귀의 추정, 정칙화, 해석 방법을 체계적으로 제시한다.

### Ch 12: Canonical correlation and discriminant analysis (pp. 199-216)

**핵심**: 함수 정준상관분석(functional CCA)과 판별분석을 다룬다. 정칙화의 필요성, 보행 데이터와 lupus nephritis 데이터 적용, 최적 스코어링과 판별 문제를 포함한다.

**키워드**: `canonical correlation`, `discriminant analysis`, `regularization`, `optimal scoring`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 12 (line 1249)

함수 정준상관분석(CCA)은 두 함수 변수 집합 간의 최대 상관을 찾는 방법으로, 가중 함수 ξ(s)와 η(t)에 의한 점수 간 상관을 최대화한다. 정칙화 없이는 표본 CCA가 항상 상관 1을 산출하므로, roughness penalty에 의한 정칙화가 필수적이다. 보행 데이터에서 고관절 각도와 무릎 각도 간의 함수 CCA를 적용하여 두 관절 운동의 연관 패턴을 분석한다. 함수 판별분석은 그룹 간 차이를 최대화하는 가중 함수를 찾으며, CCA의 특수한 경우로 해석될 수 있다. 최적 스코어링(optimal scoring) 방법은 범주형 반응을 연속형 스코어로 변환하여 판별 문제를 회귀 문제로 환원한다. 루푸스 신염(lupus nephritis) 데이터에서 정칙화된 LDA를 적용하여 질병 진행 패턴에 따른 환자 분류를 수행한다. 정칙화 수준의 선택에서 교차 검증 오분류율이 사용되며, 과도한 정칙화는 판별 능력을 저하시킨다. 다중 그룹 판별에서는 여러 정준 판별 함수를 순차적으로 추출한다. CCA와 판별분석의 연결에서 그룹 지시 행렬과 함수 변수 간의 CCA가 판별분석과 동치임을 보인다. 이 장은 다변량 CCA와 LDA를 함수 설정으로 확장하되 정칙화의 필수성을 강조한다.

### Ch 13: Differential operators in FDA (pp. 217-238)

**핵심**: 선형 미분 연산자(LDO)의 FDA에서의 역할을 다룬다. 새로운 함수 관측 생성, 모형 정칙화, 변동 분할, Green 함수, 재생 핵(reproducing kernel)을 포함한다.

**키워드**: `differential operator`, `Green function`, `reproducing kernel`, `LDO`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 13 (line 14502)

선형 미분 연산자(LDO) Lx = α₀(t)x + α₁(t)Dx + ··· + αₘ(t)D^m x는 FDA에서 세 가지 역할을 수행한다. 첫째, LDO는 관측된 함수로부터 새로운 함수 관측을 생성하며, 예를 들어 성장 가속도 D²Height는 LDO의 산출물이다. 둘째, LDO는 roughness penalty에서 ∫(Lx(t))²dt 형태로 사용되어 모형에 적합한 정칙화를 제공한다. 셋째, LDO는 함수 데이터의 변동을 분할(partition)하는 데 사용되며, 주미분분석(PDA)의 기초가 된다. Green 함수 G(t,s)는 Lx = f의 해를 x(t) = ∫G(t,s)f(s)ds로 표현하며, LDO의 역연산자 역할을 한다. 재생 핵(reproducing kernel) K(s,t)는 Green 함수와 관련되며, K(s,t) = ∫G(u,s)G(u,t)du로 정의된다. 정상 계수 LDO에서 Lx = w₀x + w₁Dx + ··· + D^m x의 해는 보조 방정식의 근에 의해 결정된다. 조화 연산자 Lx = D²x + ω²x는 주기적 변동의 정칙화에 적합하며, Fourier 기저와 자연스럽게 연결된다. 비정상 계수 LDO에서는 계수 함수 αⱼ(t)가 시간에 따라 변하여 더 유연한 모형을 허용한다. LDO의 수반(adjoint) 연산자 L*는 부분 적분을 통해 유도되며, 자기수반(self-adjoint) 연산자는 대칭적 커널을 가진다. 이 장은 미분 연산자가 FDA에서 데이터 생성, 정칙화, 변동 분석의 통합 프레임워크를 제공함을 보여준다.

### Ch 14: Principal differential analysis (pp. 239-252)

**핵심**: 주미분분석(PDA)의 기본 원리와 필요성을 소개한다. PCA와의 관계, 미분 방정식을 이용한 함수 변동의 특성화를 다룬다.

**키워드**: `principal differential analysis`, `PDA`, `differential equation`, `functional variation`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 14 (line 15688)

주미분분석(PDA)은 함수 데이터의 변동을 선형 미분 방정식의 관점에서 특성화하는 방법이다. PCA가 공분산 구조를 고유함수로 분해하는 것처럼, PDA는 미분 방정식의 계수를 추정하여 곡선의 동적 구조를 요약한다. Lx = f에서 잔차 f의 크기를 최소화하는 LDO의 계수를 데이터로부터 추정하며, 이는 다변량의 인자 분석과 유사한 역할을 한다. PDA의 적용에서 LDO의 차수 m과 계수 함수의 매끈함이 핵심 선택 사항이다. 필기 데이터에 PDA를 적용하여 x'''(t) = β₁(t)x'(t) + β₂(t)x''(t) + f(t) 형태의 미분 방정식을 추정한다. 추정된 계수 함수 β₁(t), β₂(t)는 필기 동작의 제어 메커니즘을 반영하며, 시간에 따라 변하는 동적 특성을 포착한다. PDA에서 잔차 f(t)의 분석은 미분 방정식 모형의 적합도를 평가하고, 누락된 동적 요인을 시사한다. PCA와 PDA의 관계에서 PDA가 시간적 동태를 더 직접적으로 모형화하는 반면, PCA는 단면적(cross-sectional) 변동 구조를 포착한다. 가변 계수 미분 방정식의 추정에서 기저 전개와 roughness penalty가 결합된다. 이 장은 미분 방정식을 탐색적 분석 도구로 활용하는 PDA의 원리와 적용을 소개한다.

### Ch 15: More general roughness penalties (pp. 253-270)

**핵심**: 보다 일반적인 roughness penalty의 구성과 적용을 다룬다. LDO를 이용한 일반화된 penalty, 가변 계수 모형을 포함한다.

**키워드**: `generalized roughness penalty`, `variable coefficient`, `LDO penalty`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 15 (line 16797)

일반화된 roughness penalty는 2차 도함수 대신 LDO L을 사용하여 PENSSE_λ(x|y) = Σ(yⱼ−x(tⱼ))² + λ∫(Lx(s))²ds를 최소화한다. LDO 기반 벌점에서 Lx = 0의 해 공간이 벌점이 0인 함수 집합을 정의하며, 이는 문제의 사전 지식을 반영한다. 조화 가속 연산자 L = D³ + ω²D를 사용하면 Lx = 0의 해가 주기 함수와 상수이므로, 주기적 데이터의 스무딩에 적합하다. 가변 계수 LDO에서 계수가 시간에 따라 변하면 더 유연한 정칙화가 가능하나, 계수 추정이 추가로 필요하다. 캐나다 기온 데이터에 조화 가속 연산자를 적용하여 Fourier 벌점 스무딩보다 우수한 결과를 얻는다. 일반화된 벌점의 계산에서 LDO의 Green 함수를 이용한 효율적 알고리즘이 제시된다. 벌점 매개변수 λ의 선택에서 GCV가 사용되며, 일반화된 벌점의 유효 자유도(df(λ))가 정의된다. 다변량 반응에 대한 일반화된 벌점 확장에서 각 반응별 상이한 LDO와 λ를 허용한다. 정칙화된 기저 접근법에서 일반화된 벌점 행렬 R_L = ∫(Lφₖ)(Lφₗ)dt로 대체된다. 이 장은 표준 roughness penalty를 물리적/구조적 사전 지식을 반영하는 일반화된 형태로 확장한다.

### Ch 16: Some perspectives on FDA (pp. 271-310)

**핵심**: FDA의 역사적 맥락과 향후 발전 방향에 대한 저자들의 관점을 제시한다.

**키워드**: `FDA history`, `future directions`, `perspectives`

**상세**: → `Functional Data Analysis-Springer New York (1997) - (Springer Series in Statistics) J. O. Ramsay, B. W. Silverman (auth.).md` Ch 16 (line 17962)

FDA의 역사적 맥락에서 다변량 분석, 시계열 분석, 비모수 회귀가 FDA의 선구적 분야이며, Grenander(1950)의 추상적 추론 이론이 초기 기여이다. 스플라인 이론과 커널 스무딩의 발전이 함수 추정의 수학적 기초를 제공하였으며, Wahba(1990)의 재생 핵 힐베르트 공간 접근이 핵심적이다. FDA의 고유한 기여는 미분의 체계적 활용, 등록(registration), 함수 모수의 정칙화된 추정이다. 향후 발전 방향으로 비정상(nonstationary) 함수 데이터, 공간-시간 함수 데이터, 고차원 함수 데이터의 분석이 제시된다. 함수 데이터의 가설 검정과 신뢰 영역 구축에서 무한 차원의 특수성으로 인한 이론적 도전이 논의된다. 베이지안 접근에서 함수 모수에 대한 사전 분포로 가우스 과정이 자연스러우며, roughness penalty와의 연결이 있다. 함수 데이터의 분류와 군집 분석에서 함수적 거리 측도와 함수 밀도 추정이 필요하다. 다변량 함수 데이터(multivariate functional data)와 텐서 함수 데이터의 분석이 새로운 영역으로 부상하고 있다. 소프트웨어 개발(R의 fda 패키지 등)이 FDA의 실제 적용을 촉진하고 있다. 저자들은 함수적 관점이 통계학의 다양한 분야에 새로운 통찰을 제공할 잠재력을 강조한다.
