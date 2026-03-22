---
name: "An Introduction to Statistical Learning with Applications in R, 2nd Ed"
type: book-summary
authors: "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani"
year: 2021
total_pages: 607
language: en
keywords: [statistical learning, R, regression, classification, resampling, regularization, SVM, deep learning, survival analysis, unsupervised learning, multiple testing, decision trees, boosting]
sources:
  - file: "James-ISLR_marker_full.md"
    tool: Marker
---

# An Introduction to Statistical Learning — Summary

> Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (2021), 607 pages, 13 chapters
> 통계적 학습의 핵심 방법론을 R 실습과 함께 접근 가능하게 소개하는 학부/대학원 입문 교과서이다.

## Contents

1. Introduction
2. Statistical Learning
3. Linear Regression
4. Classification
5. Resampling Methods
6. Linear Model Selection and Regularization
7. Moving Beyond Linearity
8. Tree-Based Methods
9. Support Vector Machines
10. Deep Learning
11. Survival Analysis and Censored Data
12. Unsupervised Learning
13. Multiple Testing

---

## Chapter Summaries

> Marker 원본: `James-ISLR_marker_full.md` | 총 ~15,231 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Introduction (pp. 1-14)

**핵심**: 통계적 학습의 개요를 소개한다. 임금 데이터, 주식시장 데이터, 유전자 발현 데이터 등 세 가지 실제 데이터를 통해 지도학습과 비지도학습의 응용 사례를 보여준다. 이 책의 구조와 ESL과의 관계를 설명한다.

**키워드**: `statistical learning`, `supervised learning`, `unsupervised learning`

**상세**: → `James-ISLR_marker_full.md` Ch 1 (L:344)
통계적 학습(statistical learning)은 데이터를 이해하기 위한 광범위한 도구 집합으로, 지도학습과 비지도학습으로 분류된다. 지도학습은 입력 변수에 기반하여 출력을 예측하거나 추정하는 통계 모형을 구축하며, 비지도학습은 출력 변수 없이 데이터의 관계와 구조를 학습한다. 책에서는 임금 데이터(Wage), 주식 시장 데이터(Smarket), 유전자 발현 데이터(NCI60) 등 세 가지 실제 데이터셋을 통해 회귀, 분류, 클러스터링 문제를 예시한다. 통계적 학습의 역사는 19세기 초 최소제곱법에서 시작하여 선형 판별 분석, 로지스틱 회귀, 일반화 선형 모형, 분류 및 회귀 트리, 일반화 가법 모형, 신경망, 서포트 벡터 머신으로 발전해왔다. 이 책은 ESL(The Elements of Statistical Learning)의 접근성 높은 입문서로서 다양한 분야의 대학원생과 실무자를 대상으로 한다. 수학 표기법에서는 n을 관측치 수, p를 예측 변수 수로 사용하며, 데이터 행렬 X는 n×p 행렬로 표현한다. 각 장 끝에는 R 실습이 포함되어 있으며, ISLR2 패키지에 포함된 다양한 데이터셋을 사용한다. 이 책의 네 가지 전제는 통계적 학습 방법의 광범위한 적용 가능성, 블랙박스 거부, 수학적 깊이보다는 직관 중시, 실제 문제 적용 강조이다. 책의 구성은 기초 개념(2장)부터 선형 회귀(3장), 분류(4장), 리샘플링(5장), 선형 모형 선택 및 정규화(6장), 비선형 방법(7장), 트리 기반 방법(8장), SVM(9장), 딥러닝(10장), 생존 분석(11장), 비지도학습(12장), 다중 검정(13장)까지 다룬다.

### Ch 2: Statistical Learning (pp. 15-57)

**핵심**: 통계적 학습의 기본 개념을 다룬다. f를 추정하는 이유(예측 vs 추론), f 추정 방법(모수적/비모수적), 예측 정확도와 모형 해석가능성의 트레이드오프, 지도학습 대 비지도학습, 모형 정확도 평가(적합도 측정, 편향-분산 트레이드오프, 분류 설정)를 설명한다. R 입문 실습을 포함한다.

**키워드**: `bias-variance tradeoff`, `MSE`, `flexibility`, `parametric`, `nonparametric`

**상세**: → `James-ISLR_marker_full.md` Ch 2 (L:557)
통계적 학습은 입력 변수 X와 출력 변수 Y 사이의 관계 Y = f(X) + ε에서 미지 함수 f를 추정하는 문제를 다룬다. f를 추정하는 이유는 예측(prediction)과 추론(inference) 두 가지이며, 추정 방법은 모수적(parametric) 접근과 비모수적(non-parametric) 접근으로 나뉜다. 모수적 방법은 f의 형태를 가정한 후 파라미터를 추정하는 2단계 절차를 따르며, 비모수적 방법은 f의 함수 형태를 미리 가정하지 않는다. 모형의 유연성이 증가하면 편향은 감소하지만 분산이 증가하는 편향-분산 트레이드오프(bias-variance trade-off)가 존재한다. 회귀 문제에서 모형의 정확도는 평균제곱오차(MSE)로 측정하며, 테스트 MSE = Var(f̂(x₀)) + [Bias(f̂(x₀))]² + Var(ε)로 분해된다. 분류 문제에서는 오분류율로 정확도를 평가하며, 베이즈 분류기는 가능한 가장 낮은 테스트 오류율을 달성한다. K-최근접 이웃(KNN) 분류기는 베이즈 분류기의 실용적 대안으로, K값에 따라 편향과 분산의 균형이 달라진다. K가 작으면 유연하지만 분산이 높고, K가 크면 덜 유연하지만 편향이 높다. R 실습에서는 기본 명령어, 그래픽 생성, 데이터 인덱싱, 데이터 로딩, 수치 및 그래픽 요약 방법을 다룬다. 올바른 유연성 수준을 선택하는 것이 통계적 학습 방법의 성공에 핵심적이며, 이를 위한 방법은 5장에서 교차 검증을 통해 다룬다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 2.1 What Is Statistical Learning? `L:557`
- 2.1.1 Why Estimate f? `L:587`
- 2.1.3 The Trade-O*ff *Between Prediction Accuracy and Model Interpretability `L:712`
- 2.2 Assessing Model Accuracy `L:774`
- 2.2.1 Measuring the Quality of Fit `L:780`
- 2.2.2 The Bias-Variance Trade-O*ff `L:837`
- 2.3 Lab: Introduction to R `L:968`
- 2.3.1 Basic Commands `L:980`
- 2.3.2 Graphics `L:1120`
- 2.3.3 Indexing Data `L:1194`
- 2.3.4 Loading Data `L:1267`
- 2.4 Exercises `L:1444`


### Ch 3: Linear Regression (pp. 59-128)

**핵심**: 선형 회귀를 다룬다. 단순 선형 회귀(계수 추정, 정확도 평가), 다중 선형 회귀(회귀 계수 추정, 중요 질문들), 질적 예측변수, 선형 모형의 확장(상호작용, 비선형), 잠재적 문제점(비선형성, 상관 오차, 이분산성, 이상값, 다중공선성), KNN과의 비교를 설명한다.

**키워드**: `simple regression`, `multiple regression`, `qualitative predictors`, `collinearity`, `KNN`

**상세**: → `James-ISLR_marker_full.md` Ch 3 (L:1601)
선형 회귀(linear regression)는 양적 반응변수를 예측하기 위한 기본적이면서 널리 사용되는 지도학습 방법이다. 단순 선형 회귀에서는 Y ≈ β₀ + β₁X로 모형화하고, 계수는 잔차제곱합(RSS)을 최소화하는 최소제곱법으로 추정한다. 계수 추정치의 정확도는 표준오차로 평가하며, 이를 통해 신뢰구간과 가설검정(t-통계량, p-값)을 수행한다. 모형 적합도는 잔차표준오차(RSE)와 R² 통계량으로 평가하며, R²는 반응변수 분산 중 예측 변수로 설명되는 비율을 나타낸다. 다중 선형 회귀에서는 Y = β₀ + β₁X₁ + ··· + βₚXₚ + ε 형태로 확장하고, F-통계량을 통해 예측 변수들과 반응변수 간의 전반적 관계를 검정한다. 변수 선택(전진 선택, 후진 선택, 혼합 선택)을 통해 유용한 예측 변수의 부분집합을 식별한다. 질적 예측 변수는 더미 변수(dummy variable)를 사용하여 회귀 모형에 포함시킨다. 상호작용 항(interaction term)은 가법 가정을 완화하여 예측 변수 간의 시너지 효과를 모형화한다. 다항 회귀(polynomial regression)를 통해 비선형 관계를 선형 모형 프레임워크 내에서 수용한다. 잠재적 문제로는 비선형성, 오차항의 상관, 이분산성, 이상치, 높은 레버리지, 다중공선성이 있으며, VIF(분산팽창인자)로 다중공선성을 진단한다. KNN 회귀와의 비교에서는 차원의 저주로 인해 고차원에서 모수적 방법이 비모수적 방법보다 우수할 수 있음을 보인다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 3.1 Simple Linear Regression `L:1601`
- 3.1.2 Assessing the Accuracy of the Coe*ffi*cient Estimates `L:1670`
- 3.1.3 Assessing the Accuracy of the Model `L:1782`
- 3.2 Multiple Linear Regression `L:1846`
- 3.2.1 Estimating the Regression Coe*ffi*cients `L:1882`
- 3.3.2 Extensions of the Linear Model `L:2163`
- 3.4 The Marketing Plan `L:2427`
- 3.5 Comparison of Linear Regression with *K*-Nearest Neighbors `L:2454`
- 3.6 Lab: Linear Regression `L:2502`
- 3.6.4 Interaction Terms `L:2814`
- 3.6.5 Non-linear Transformations of the Predictors `L:2838`
- 3.6.6 Qualitative Predictors `L:2925`
- 3.6.7 Writing Functions `L:3000`
- 3.7 Exercises `L:3039`


### Ch 4: Classification (pp. 129-196)

**핵심**: 분류 방법을 다룬다. 로지스틱 회귀(로지스틱 모형, 다항 로지스틱), 분류를 위한 생성 모형(LDA, QDA, 나이브 베이즈), 분류 방법 비교, 일반화 선형 모형(포아송 회귀 포함)을 설명한다. 주식시장 데이터를 이용한 R 실습을 포함한다.

**키워드**: `logistic regression`, `LDA`, `QDA`, `naive Bayes`, `Poisson regression`, `GLM`

**상세**: → `James-ISLR_marker_full.md` Ch 4 (L:3209)
분류(classification)는 질적 반응변수를 예측하는 문제로, 회귀 문제보다 빈번하게 발생한다. 선형 회귀를 분류에 적용하면 확률이 [0,1] 범위를 벗어나거나 3개 이상의 범주에 대해 의미 있는 확률 추정을 제공하지 못하는 문제가 있다. 로지스틱 회귀(logistic regression)는 로지스틱 함수 p(X) = eᵝ⁰⁺ᵝ¹ˣ/(1+eᵝ⁰⁺ᵝ¹ˣ)를 사용하여 0과 1 사이의 확률을 모형화하며, 최대우도법(maximum likelihood)으로 계수를 추정한다. 다중 로지스틱 회귀에서는 단일 예측 변수와 다중 예측 변수 모형의 계수가 다를 수 있는데, 이는 교란(confounding) 때문이다. 선형 판별 분석(LDA)은 각 클래스 내 예측 변수가 공통 공분산 행렬을 가진 다변량 정규분포를 따른다고 가정하고, 베이즈 정리를 적용하여 사후 확률을 계산한다. 이차 판별 분석(QDA)은 각 클래스별 고유한 공분산 행렬을 가정하여 비선형 결정 경계를 생성하며, 편향-분산 트레이드오프에 따라 LDA 또는 QDA를 선택한다. 나이브 베이즈(Naive Bayes) 분류기는 각 클래스 내에서 예측 변수들이 독립이라는 가정 하에 밀도 함수를 곱으로 분해하여 계산량을 줄인다. 분류 성능은 혼동 행렬(confusion matrix), 민감도, 특이도, ROC 곡선 및 AUC로 평가하며, 결정 임계값 조정을 통해 오류 유형 간 트레이드오프를 조절한다. 일반화 선형 모형의 일종인 포아송 회귀는 카운트 데이터에 적합하며, Bikeshare 데이터 실습에서 시연된다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 4.1 An Overview of Classification `L:3209`
- 4.2 Why Not Linear Regression? `L:3227`
- 4.3 Logistic Regression `L:3259`
- 4.3.3 Making Predictions `L:3328`
- 4.3.4 Multiple Logistic Regression `L:3349`
- 4.4.1 Linear Discriminant Analysis for p = 1 `L:3471`
- 4.4.2 Linear Discriminant Analysis for p > 1 `L:3538`
- 4.4.4 Naive Bayes `L:3694`
- 4.5 A Comparison of Classification Methods `L:3778`
- 4.5.2 An Empirical Comparison `L:3850`
- 4.6 Generalized Linear Models `L:3882`
- 4.6.1 Linear Regression on the Bikeshare Data `L:3890`
- 4.7 Lab: Classification Methods `L:4036`
- 4.7.1 The Stock Market Data `L:4038`
- 4.7.2 Logistic Regression `L:4122`
- 4.7.3 Linear Discriminant Analysis `L:4302`
- 4.7.4 Quadratic Discriminant Analysis `L:4383`
- 4.7.6 K-Nearest Neighbors `L:4484`
- 4.7.7 Poisson Regression `L:4653`


### Ch 5: Resampling Methods (pp. 197-224)

**핵심**: 재표본 방법을 다룬다. 교차검증(검증 세트 접근법, LOOCV, k-겹 교차검증, 편향-분산 트레이드오프, 분류 문제에서의 교차검증)과 부트스트랩을 설명한다. R 실습을 포함한다.

**키워드**: `cross-validation`, `LOOCV`, `k-fold`, `bootstrap`

**상세**: → `James-ISLR_marker_full.md` Ch 5 (L:4961)
리샘플링(resampling) 방법은 적합된 모형에서 반복적으로 표본을 추출하여 모형의 테스트 오류를 추정하거나 통계적 추정량의 불확실성을 정량화하는 데 사용된다. 검증 세트 접근법(validation set approach)은 데이터를 훈련 세트와 검증 세트로 무작위 분할하지만, 추정치의 변동성이 크고 훈련 데이터가 줄어드는 단점이 있다. Leave-One-Out 교차 검증(LOOCV)은 한 개의 관측치만 검증에 사용하고 나머지로 모형을 적합하는 과정을 n번 반복하여 편향이 낮지만 분산이 높을 수 있다. 최소제곱 선형 회귀에서는 LOOCV를 단일 모형 적합 비용으로 계산할 수 있는 축약 공식 CV(n) = (1/n)Σ[(yᵢ - ŷᵢ)/(1-hᵢ)]²이 존재한다. k-겹 교차 검증(k-fold CV)은 데이터를 k개 그룹으로 나누어 각 그룹을 검증 세트로 사용하며, 통상 k=5 또는 k=10을 사용한다. k-겹 CV는 LOOCV에 비해 계산 효율적이고, 편향은 약간 높지만 분산이 낮아 전체적으로 더 정확한 테스트 오류 추정치를 제공한다. 분류 문제에서는 MSE 대신 오분류율을 사용하여 교차 검증을 수행한다. 부트스트랩(bootstrap)은 원본 데이터에서 복원추출로 새로운 데이터셋을 반복 생성하여 추정량의 표준오차를 계산하는 강력한 방법이다. 부트스트랩은 선형 회귀의 계수 표준오차 추정부터 복잡한 통계적 학습 방법의 정확도 평가까지 광범위하게 적용된다. 이러한 리샘플링 방법은 모형 선택과 최적 유연성 수준 결정에 핵심적인 역할을 한다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 5.1.1 The Validation Set Approach `L:4961`
- 5.1.3 k-Fold Cross-Validation `L:5037`
- 5.1.4 Bias-Variance Trade-O*ff *for k-Fold Cross-Validation `L:5061`
- 5.2 The Bootstrap `L:5102`
- 5.3 Lab: Cross-Validation and the Bootstrap `L:5162`
- 5.3.1 The Validation Set Approach `L:5166`
- 5.3.2 Leave-One-Out Cross-Validation `L:5229`
- 5.3.4 The Bootstrap `L:5301`
- 5.4 Exercises `L:5428`


### Ch 6: Linear Model Selection and Regularization (pp. 225-288)

**핵심**: 선형 모형 선택과 정규화를 다룬다. 부분집합 선택(최적 부분집합, 단계적 선택), 축소 방법(릿지 회귀, 라소, 튜닝 파라미터 선택), 차원 축소 방법(주성분 회귀, 부분 최소제곱), 고차원에서의 고려사항을 설명한다.

**키워드**: `subset selection`, `ridge regression`, `lasso`, `PCR`, `PLS`, `high-dimensional`

**상세**: → `James-ISLR_marker_full.md` Ch 6 (L:5530)
선형 모형 선택 및 정규화(regularization)는 최소제곱법의 대안으로 예측 정확도와 모형 해석가능성을 향상시킨다. 부분집합 선택(subset selection)에는 최적 부분집합 선택, 전진 단계적 선택, 후진 단계적 선택이 있으며, 2ᵖ개의 모형 중 최적 모형을 탐색한다. 최적 모형 선택을 위해 Cp, AIC, BIC, 조정 R² 등 훈련 오류 조정 지표 또는 교차 검증을 사용하며, BIC는 Cp보다 더 적은 변수를 가진 모형을 선호한다. 1-표준오차 규칙(one-standard-error rule)은 추정 테스트 오류가 최소점의 1 표준오차 이내인 가장 단순한 모형을 선택하는 실용적 기준이다. 릿지 회귀(ridge regression)는 RSS에 ℓ₂ 벌칙항 λΣβⱼ²을 추가하여 계수를 0 방향으로 축소하며, 편향-분산 트레이드오프를 통해 최소제곱법보다 낮은 테스트 MSE를 달성한다. 라쏘(lasso)는 ℓ₁ 벌칙항 λΣ|βⱼ|을 사용하여 일부 계수를 정확히 0으로 만들어 변수 선택을 수행하며, 희소 모형(sparse model)을 생성한다. 릿지와 라쏘의 제약 영역 형태(원형 vs 다이아몬드형) 차이로 인해 라쏘만이 축 위에서 해를 찾아 변수 선택 특성을 갖는다. 베이지안 관점에서 릿지 회귀는 가우시안 사전분포, 라쏘는 이중지수(라플라스) 사전분포에 대응한다. 차원 축소 방법으로 주성분 회귀(PCR)와 부분 최소제곱(PLS)이 있으며, p개의 예측 변수를 M(<p)개의 선형 결합으로 변환하여 회귀를 수행한다. 조율 모수 λ(또는 제약 s)의 선택은 교차 검증을 통해 이루어진다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 6.2 Shrinkage Methods `L:5737`
- 6.3.1 Principal Components Regression `L:6021`
- 6.3.2 Partial Least Squares `L:6116`
- 6.4 Considerations in High Dimensions `L:6144`
- 6.4.3 Regression in High Dimensions `L:6190`
- 6.4.4 Interpreting Results in High Dimensions `L:6208`
- 6.5 Lab: Linear Models and Regularization Methods `L:6216`
- 6.6 Exercises `L:6915`


### Ch 7: Moving Beyond Linearity (pp. 289-326)

**핵심**: 비선형 방법을 다룬다. 다항 회귀, 단계 함수, 기저 함수, 회귀 스플라인(구간별 다항식, 매듭 선택), 평활 스플라인, 국소 회귀, 일반화 가법 모형(GAM, 회귀/분류)을 설명한다.

**키워드**: `polynomial regression`, `splines`, `smoothing splines`, `local regression`, `GAM`

**상세**: → `James-ISLR_marker_full.md` Ch 7 (L:7045)
선형성 가정을 넘어서는 비선형 모형을 다루며, 해석가능성을 유지하면서 예측력을 향상시키는 방법들을 소개한다. 다항 회귀(polynomial regression)는 예측 변수의 거듭제곱(X², X³ 등)을 추가 예측 변수로 사용하며, 일반적으로 차수 d는 3 또는 4를 초과하지 않는다. 계단 함수(step functions)는 연속 변수의 범위를 K개 구간으로 나누어 구간별 상수를 적합하는 구간별 상수 함수를 생성한다. 기저 함수(basis functions) 접근은 다항 회귀와 구간별 상수 함수를 일반화하여 b₁(X), b₂(X), ..., bK(X) 형태의 변환을 사용한다. 회귀 스플라인(regression splines)은 X의 범위를 매듭(knot)으로 나누어 각 영역에서 다항식을 적합하되, 매듭에서 연속성과 미분 연속성 제약을 부과하여 매끄러운 곡선을 만든다. 3차 스플라인(cubic spline)은 K개 매듭에서 K+4 자유도를 사용하며, 자연 3차 스플라인(natural cubic spline)은 경계 영역에서 선형 제약을 추가하여 더 안정적인 추정을 제공한다. 평활 스플라인(smoothing splines)은 RSS + λ∫g″(t)²dt를 최소화하는 함수를 찾으며, 조율 모수 λ가 편향-분산 트레이드오프를 제어한다. 평활 스플라인은 모든 고유한 xᵢ에 매듭을 두는 자연 3차 스플라인의 축소 버전이며, 유효 자유도(effective degrees of freedom)는 λ가 0에서 ∞로 증가할 때 n에서 2로 감소한다. 국소 회귀(local regression)는 목표점 x₀ 근처의 관측치에만 가중치를 부여하여 가중 최소제곱 회귀를 적합하며, 범위(span) s가 유연성을 제어한다. 일반화 가법 모형(GAMs)은 각 예측 변수에 비선형 함수 fⱼ를 적합하여 합산하는 방식으로, 다중 선형 회귀를 비선형으로 확장하면서 가법 구조를 유지한다. GAMs는 자연 스플라인, 평활 스플라인, 국소 회귀 등을 구성 요소로 사용할 수 있으며, 역적합(backfitting) 알고리즘으로 적합하고, 분류 문제에도 확장 가능하다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 7.1 Polynomial Regression `L:7062`
- 7.4 Regression Splines `L:7168`
- 7.4.3 The Spline Basis Representation `L:7214`
- 7.4.5 Comparison to Polynomial Regression `L:7269`
- 7.5 Smoothing Splines `L:7277`
- 7.5.1 An Overview of Smoothing Splines `L:7281`
- 7.5.2 Choosing the Smoothing Parameter $\lambda$ `L:7304`
- 7.7 Generalized Additive Models `L:7368`
- 7.7.1 GAMs for Regression Problems `L:7384`
- 7.7.2 GAMs for Classification Problems `L:7442`
- 7.8 Lab: Non-linear Modeling `L:7469`
- 7.8.2 Splines `L:7735`


### Ch 8: Tree-Based Methods (pp. 327-366)

**핵심**: 트리 기반 방법을 다룬다. 결정 트리의 기초(회귀 트리, 분류 트리, 트리 대 선형 모형), 배깅, 랜덤 포레스트, 부스팅, 베이지안 가법 회귀 트리(BART), 트리 앙상블 방법 요약을 설명한다.

**키워드**: `decision trees`, `bagging`, `random forests`, `boosting`, `BART`

**상세**: → `James-ISLR_marker_full.md` Ch 8 (L:8128)
결정 트리는 예측변수 공간을 재귀적 이진 분할(recursive binary splitting)을 통해 비중복 영역으로 나누고, 각 영역의 훈련 응답 평균으로 예측한다. 회귀 트리는 RSS를 최소화하는 분할을 탐욕적으로 선택하며, 비용 복잡도 가지치기(cost complexity pruning)로 과적합을 방지한다. 분류 트리는 지니 지수나 엔트로피 같은 노드 순도 측정을 분할 기준으로 사용한다. 트리는 해석이 용이하나 예측 정확도가 낮고 데이터 변화에 민감하다는 단점이 있다. 배깅(bagging)은 부트스트랩 표본으로 다수의 깊은 트리를 성장시켜 평균함으로써 분산을 줄이며, OOB(out-of-bag) 오차로 테스트 오류를 추정한다. 랜덤 포레스트는 각 분할에서 무작위로 m개(보통 sqrt(p))의 예측변수만 후보로 고려하여 트리 간 상관을 제거(decorrelate)한다. 부스팅은 잔차에 작은 트리를 순차적으로 적합시키며, 축소 파라미터 lambda, 트리 수 B, 상호작용 깊이 d의 세 가지 튜닝 파라미터를 갖는다. BART는 각 트리를 이전 반복의 트리에서 무작위 섭동(perturbation)하여 생성하고, 번인(burn-in) 이후 예측을 평균하는 베이지안 앙상블 방법이다. 네 가지 앙상블 방법(배깅, 랜덤 포레스트, 부스팅, BART) 각각은 트리를 약학습기로 사용하되, 독립 성장, 비상관화, 순차 학습, 섭동 기반 탐색이라는 서로 다른 전략을 취한다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 8.1 The Basics of Decision Trees `L:8128`
- 8.1.4 Advantages and Disadvantages of Trees `L:8310`
- 8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees `L:8324`
- 8.2.1 Bagging `L:8330`
- 8.2.3 Boosting `L:8392`
- 8.2.4 Bayesian Additive Regression Trees `L:8446`
- 8.2.5 Summary of Tree Ensemble Methods `L:8512`
- 8.3 Lab: Decision Trees `L:8526`
- 8.3.1 Fitting Classification Trees `L:8528`
- 8.3.2 Fitting Regression Trees `L:8693`
- 8.3.3 Bagging and Random Forests `L:8752`
- 8.4 Exercises `L:8950`


### Ch 9: Support Vector Machines (pp. 367-402)

**핵심**: 서포트 벡터 머신을 다룬다. 최대 마진 분류기(초평면, 분리 불가능 경우), 서포트 벡터 분류기, 서포트 벡터 머신(비선형 결정 경계, 커널), 다중 클래스 SVM(일대일, 일대나머지), 로지스틱 회귀와의 관계를 설명한다.

**키워드**: `maximal margin classifier`, `support vector classifier`, `SVM`, `kernel`, `ROC`

**상세**: → `James-ISLR_marker_full.md` Ch 9 (L:9036)
최대 마진 분류기는 p차원 공간에서 두 클래스를 완벽히 분리하는 초평면 중 마진이 가장 큰 것을 선택하며, 마진 위에 놓인 관측치인 서포트 벡터에만 의존한다. 분리 불가능한 경우, 서포트 벡터 분류기(소프트 마진 분류기)는 슬랙 변수 epsilon_i를 도입하여 일부 관측치가 마진이나 초평면의 잘못된 쪽에 위치하는 것을 허용한다. 튜닝 파라미터 C는 마진 위반의 총합을 제한하여 편향-분산 트레이드오프를 제어한다. 서포트 벡터 머신(SVM)은 커널 함수 K(x_i, x_i')를 사용하여 특성 공간을 확장함으로써 비선형 결정 경계를 생성한다. 다항 커널 K=(1+sum x_ij x_i'j)^d와 방사 커널 K=exp(-gamma sum (x_ij - x_i'j)^2)가 널리 사용된다. 방사 커널은 매우 국소적으로 동작하여 가까운 훈련 관측치만 테스트 관측치의 분류에 영향을 미친다. 커널의 핵심 이점은 확장된 특성 공간에서 명시적으로 계산하지 않아도 되어 계산 효율이 높다는 것이다. 다중 클래스 분류는 일대일(one-versus-one) 또는 일대나머지(one-versus-all) 접근법으로 확장한다. SVM의 최적화 문제를 "손실+벌점" 형태로 재구성하면 힌지 손실(hinge loss)과 릿지 벌점의 결합이 되며, 이는 로지스틱 회귀의 손실 함수와 밀접하게 관련된다. 클래스가 잘 분리된 경우 SVM이, 클래스가 많이 겹치는 경우 로지스틱 회귀가 더 좋은 성능을 보이는 경향이 있다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 9.1 Maximal Margin Classifier `L:9036`
- 9.1.4 Construction of the Maximal Margin Classifier `L:9130`
- 9.2 Support Vector Classifiers `L:9159`
- 9.2.1 Overview of the Support Vector Classifier `L:9161`
- 9.2.2 Details of the Support Vector Classifier `L:9190`
- 9.3 Support Vector Machines `L:9237`
- 9.3.1 Classification with Non-Linear Decision Boundaries `L:9241`
- 9.3.3 An Application to the Heart Disease Data `L:9330`
- 9.5 Relationship to Logistic Regression `L:9362`
- 9.6 Lab: Support Vector Machines `L:9411`
- 9.6.1 Support Vector Classifier `L:9415`
- 9.6.4 SVM with Multiple Classes `L:9758`
- 9.6.5 Application to Gene Expression Data `L:9782`


### Ch 10: Deep Learning (pp. 403-460)

**핵심**: 딥러닝을 다룬다. 단층/다층 신경망, 합성곱 신경망(CNN, 합성곱 층, 풀링 층, 데이터 증강, 사전학습 분류기), 문서 분류, 순환 신경망(RNN, 시계열 예측), 딥러닝 사용 시점, 신경망 적합(역전파, 정규화, SGD, 드롭아웃), 보간과 이중 하강을 설명한다.

**키워드**: `neural networks`, `CNN`, `RNN`, `backpropagation`, `dropout`, `double descent`

**상세**: → `James-ISLR_marker_full.md` Ch 10 (L:9973)
단층 신경망은 입력의 선형 결합에 비선형 활성화 함수(시그모이드 또는 ReLU)를 적용한 은닉 유닛을 만들고, 이를 출력층에서 선형 결합하여 예측한다. 다층 신경망은 여러 은닉층을 쌓아 복잡한 변환을 구축하며, MNIST 숫자 분류에서 드롭아웃 정규화로 1.8% 테스트 오류를 달성한다. 합성곱 신경망(CNN)은 합성곱 필터로 이미지의 국소 특징(가장자리, 형태 등)을 감지하고, 풀링 층으로 공간 크기를 축소하며, 이 과정을 반복하여 저수준에서 고수준 특징의 계층을 구축한다. 데이터 증강은 훈련 이미지를 회전, 이동, 뒤집기 등으로 변형하여 정규화 효과를 얻으며, 사전학습된 분류기(예: ResNet50)의 필터를 새로운 문제에 전이(weight freezing)할 수 있다. 문서 분류에서는 단어 가방(bag-of-words) 모델이나 워드 임베딩을 사용하며, 순환 신경망(RNN)은 순차적 데이터를 처리하여 문서 감성이나 시계열을 예측한다. LSTM RNN은 장기 의존성을 포착하여 단순 RNN보다 성능이 우수하다. 신경망 적합은 역전파(backpropagation)로 그래디언트를 계산하고, 확률적 경사 하강법(SGD)으로 미니배치 단위 학습을 수행한다. 드롭아웃은 훈련 시 은닉 유닛을 무작위로 제거하여 과적합을 방지하는 정규화 기법이다. 딥러닝은 대규모 데이터에서 강력하지만, 소규모 표 형식 데이터에서는 라소 같은 단순 선형 모형이 유사하거나 더 나은 성능을 보일 수 있으므로 오컴의 면도날 원칙을 따르는 것이 바람직하다. 이중 하강(double descent) 현상은 보간 임계점 이후에도 최소 노름 해를 통해 테스트 오류가 다시 감소할 수 있음을 보여준다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 10.1 Single Layer Neural Networks `L:9985`
- 10.2 Multilayer Neural Networks `L:10071`
- 10.3 Convolutional Neural Networks `L:10165`
- 10.3.1 Convolution Layers `L:10189`
- 10.3.3 Architecture of a Convolutional Neural Network `L:10251`
- 10.5.1 Sequential Models for Document Classification `L:10424`
- 10.6 When to Use Deep Learning `L:10562`
- 10.7 Fitting a Neural Network `L:10604`
- 10.7.4 Network Tuning `L:10717`
- 10.8 Interpolation and Double Descent `L:10728`
- 10.9 Lab: Deep Learning `L:10774`
- 10.9.2 A Multilayer Network on the MNIST Digit Data `L:10896`
- 10.10 Exercises `L:11498`


### Ch 11: Survival Analysis and Censored Data (pp. 461-496)

**핵심**: 생존분석과 중도절단 데이터를 다룬다. 생존 시간과 중도절단 시간, 카플란-마이어 생존 곡선, 로그순위 검정, 위험함수와 비례위험 모형(콕스 모형), 콕스 모형의 축소, AUC, 시간의존 공변량, 생존 트리를 설명한다.

**키워드**: `survival analysis`, `censoring`, `Kaplan-Meier`, `Cox model`, `hazard function`

**상세**: → `James-ISLR_marker_full.md` Ch 11 (L:11540)
생존분석은 사건 발생까지의 시간을 분석하며, 관측 시간 Y=min(T,C)와 상태 지시자 delta로 표현되는 중도절단 데이터를 다룬다. 독립 중도절단 가정은 특성에 조건부로 사건 시간 T와 중도절단 시간 C가 독립임을 요구한다. 카플란-마이어 추정량은 각 사망 시점에서 위험 집합(risk set) 내 생존 확률을 순차적으로 곱하여 생존 곡선 S(t)를 추정한다. 로그순위 검정은 두 그룹의 생존 곡선이 동일한지를 각 사망 시점의 2x2 분할표를 이용하여 검정하며, 검정 통계량 W는 대표본에서 표준정규분포를 따른다. 위험함수 h(t)는 시간 t까지 생존한 조건 하에서의 순간 사망률로, 생존함수 S(t) 및 확률밀도함수 f(t)와 h(t)=f(t)/S(t)의 관계를 갖는다. 콕스 비례위험 모형은 h(t|x_i)=h_0(t)exp(sum x_ij beta_j)로 공변량 효과를 모형화하며, 기저 위험함수 h_0(t)의 형태를 지정하지 않는 반모수적 접근이다. 부분 우도(partial likelihood)에서 h_0(t)가 소거되어 beta를 추정할 수 있으며, 이진 공변량의 경우 콕스 모형의 스코어 검정은 로그순위 검정과 동일하다. BrainCancer 데이터 분석에서 카르노프스키 지수의 단위 증가는 위험의 0.95배 감소(p<0.01)를 보인다. Publication 데이터에서는 다른 공변량을 조정하면 양성 결과의 출판 위험비가 1.74로 유의하게 나타나, 단변량 로그순위 검정(p=0.36)과 대조적인 결과를 보여준다. 콕스 모형에 릿지 또는 라소 벌점을 적용하여 고차원 생존 데이터에서 축소 추정이 가능하다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 11.2 A Closer Look at Censoring `L:11578`
- 11.3 The Kaplan-Meier Survival Curve `L:11590`
- 11.4 The Log-Rank Test `L:11648`
- 11.5 Regression Models With a Survival Response `L:11713`
- 11.5.1 The Hazard Function `L:11719`
- 11.6 Shrinkage for the Cox Model `L:11932`
- 11.7 Additional Topics `L:11966`
- 11.7.1 Area Under the Curve for Survival Analysis `L:11968`
- 11.7.2 Choice of Time Scale `L:11986`
- 11.8 Lab: Survival Analysis `L:12012`
- 11.8.1 Brain Cancer Data `L:12016`
- 11.8.2 Publication Data `L:12171`


### Ch 12: Unsupervised Learning (pp. 497-552)

**핵심**: 비지도학습을 다룬다. 주성분 분석(PCA, 분산 설명 비율), 결측값과 행렬 완성, 군집 방법(K-평균 군집화, 계층적 군집화, 군집화의 실제적 이슈)을 설명한다. NCI60 데이터 예제를 포함한 R 실습을 제공한다.

**키워드**: `PCA`, `K-means`, `hierarchical clustering`, `matrix completion`

**상세**: → `James-ISLR_marker_full.md` Ch 12 (L:12488)
비지도학습은 응답 변수 없이 데이터의 구조를 탐색하며, 교차검증 등으로 결과를 객관적으로 평가하기 어렵다는 점에서 지도학습보다 주관적이다. 주성분 분석(PCA)은 데이터의 분산이 최대인 방향을 순차적으로 찾아 저차원 표현을 제공하며, 각 주성분은 원래 변수의 정규화된 선형 결합이다. 주성분은 관측치에 가장 가까운 저차원 부분공간으로도 해석되며, 분산 설명 비율(PVE)로 각 주성분의 중요도를 평가한다. 변수의 척도가 다를 경우 PCA 전에 표준화가 필수적이며, 스크리 플롯의 엘보 지점으로 적절한 주성분 수를 선택한다. 결측값과 행렬 완성에서는 관측된 원소만으로 최적화 문제를 풀어 결측값을 대체하며, 반복 알고리즘(Algorithm 12.1)으로 주성분 계산과 결측값 추정을 동시에 수행한다. 이 방법은 넷플릭스 같은 추천 시스템에서 고객-영화 평점 행렬의 결측 원소를 예측하는 데 활용된다. K-평균 군집화는 총 군집 내 변동(within-cluster variation)을 최소화하도록 관측치를 K개 군집으로 분할하며, 지역 최적에 수렴하므로 다양한 초기값으로 반복 실행한다. 계층적 군집화는 덴드로그램을 생성하여 어떤 수의 군집이든 한 번에 확인할 수 있으며, 연결 방법(완전, 평균, 단일, 중심)에 따라 결과가 달라진다. 비유사도 측정(유클리드 vs 상관 기반 거리) 및 변수 표준화 여부가 군집 결과에 큰 영향을 미치므로, 도메인 지식에 기반한 신중한 선택이 필요하다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 12.1 The Challenge of Unsupervised Learning `L:12488`
- 12.2 Principal Components Analysis `L:12498`
- 12.3 Missing Values and Matrix Completion `L:12696`
- 12.4 Clustering Methods `L:12813`
- 12.4.2 Hierarchical Clustering `L:12892`
- 12.4.3 Practical Issues in Clustering `L:12992`
- 12.5 Lab: Unsupervised Learning `L:13025`
- 12.5.1 Principal Components Analysis `L:13027`
- 12.5.4 NCI60 Data Example `L:13489`


### Ch 13: Multiple Testing (pp. 553-596)

**핵심**: 다중 검정을 다룬다. 가설 검정 복습(제1종/제2종 오류), 다중 검정의 도전, 족내 오류율(FWER, 본페로니 보정, 홀름 절차), 거짓 발견율(FDR, 벤자미니-호크버그 절차), p-값과 FDR의 재표본 접근법을 설명한다.

**키워드**: `hypothesis testing`, `FWER`, `FDR`, `Bonferroni`, `Benjamini-Hochberg`, `resampling`

**상세**: → `James-ISLR_marker_full.md` Ch 13 (L:13784)
가설 검정은 귀무가설 H_0과 대립가설 H_a를 설정하고, 검정 통계량 T를 구성하며, p-값을 계산하여 H_0 기각 여부를 결정하는 네 단계로 진행한다. p-값은 H_0이 참일 때 관측된 것만큼 극단적인 검정 통계량을 볼 확률이며, H_0이 참일 확률이 아니다. 제1종 오류(위양성)는 참인 H_0을 기각하는 것이고, 제2종 오류(위음성)는 거짓인 H_0을 기각하지 못하는 것이다. 다중 검정에서 m개의 참인 귀무가설을 각각 alpha 수준으로 검정하면, 약 alpha x m개의 위양성이 기대되어 족내 오류율(FWER)이 급증한다. FWER = 1-(1-alpha)^m으로, m이 커지면 적어도 하나의 제1종 오류를 범할 확률이 거의 1에 근접한다. 본페로니 보정은 각 검정의 기각 임계값을 alpha/m으로 설정하여 FWER을 제어하나 보수적이며, 홀름의 단계적 하강법은 본페로니보다 항상 더 많은 귀무가설을 기각하여 검정력이 높다. 터키 방법은 G개 평균의 쌍별 비교에, 셰페 방법은 평균의 임의 선형 대비에 특화된 FWER 제어를 제공한다. m이 클 때 FWER 제어는 검정력이 지나치게 낮아지므로, 거짓 발견율(FDR) = E(V/R)을 제어하는 것이 실용적이다. 벤자미니-호크버그 절차는 정렬된 p-값과 qj/m의 비교를 통해 FDR을 q 이하로 제어하며, 독립이거나 약한 의존 관계의 p-값에 대해 유효하다. 재표본 접근법은 관측치를 순열하여 검정 통계량의 귀무 분포를 근사하고, 이론적 귀무 분포가 불확실하거나 가정이 위반될 때 특히 유용하다.

**Marker 세부 목차** (`James-ISLR_marker_full.md`):
- 13.1 A Quick Review of Hypothesis Testing `L:13804`
- 13.2 The Challenge of Multiple Testing `L:13929`
- 13.3 The Family-Wise Error Rate `L:13947`
- 13.3.3 Trade-O*ff *Between the FWER and Power `L:14101`
- 13.4 The False Discovery Rate `L:14111`
- 13.5 A Re-Sampling Approach to *p*-Values and False Discovery Rates `L:14179`
- 13.5.2 A Re-Sampling Approach to the False Discovery Rate `L:14237`
- 13.5.3 When Are Re-Sampling Approaches Useful? `L:14289`
- 13.6 Lab: Multiple Testing `L:14300`
- 13.6.1 Review of Hypothesis Tests `L:14302`
- 13.6.2 The Family-Wise Error Rate `L:14369`
- 13.6.3 The False Discovery Rate `L:14499`
- 13.6.4 A Re-Sampling Approach `L:14566`
- 13.7 Exercises `L:14704`



### 기타 섹션 (Marker)

- An Introduction to Statistical Learning `L:3`
- An Overview of Statistical Learning `L:344`
- Who Should Read This Book? `L:421`
- Data Sets Used in Labs and Exercises `L:509`
- Linear Model Selection and Regularization `L:5530`
- Cp*, AIC, BIC, and Adjusted *R*2 `L:5669`
- What Goes Wrong in High Dimensions? `L:6166`
- Results Using a Pretrained Classifier `L:10295`
- Regularization and Stochastic Gradient Descent `L:10686`
- Survival Analysis and Censored Data `L:11542`

---

## Marker 세부 목차

> `L:숫자`는 `James-ISLR_marker_full.md`의 라인 번호. `Read(file, offset=L, limit=N)`으로 해당 구간을 직접 읽을 수 있다.

- An Introduction to Statistical Learning `L:3`
- An Overview of Statistical Learning `L:344`
- A Brief History of Statistical Learning `L:392`
- Who Should Read This Book? `L:421`
- Data Sets Used in Labs and Exercises `L:509`
- 2.1 What Is Statistical Learning? `L:557`
  - 2.1.1 Why Estimate f? `L:587`
- 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability `L:712`
  - 2.2 Assessing Model Accuracy `L:774`
  - 2.2.1 Measuring the Quality of Fit `L:780`
- 2.2.2 The Bias-Variance Trade-Off `L:837`
- 2.3 Lab: Introduction to R `L:968`
- 2.3.1 Basic Commands `L:980`
  - 2.3.2 Graphics `L:1120`
  - 2.3.3 Indexing Data `L:1194`
- 2.3.4 Loading Data `L:1267`
- 2.4 Exercises `L:1444`
- 3.1 Simple Linear Regression `L:1601`
- 3.1.2 Assessing the Accuracy of the Coefficient Estimates `L:1670`
  - 3.1.3 Assessing the Accuracy of the Model `L:1782`
- 3.2 Multiple Linear Regression `L:1846`
- 3.2.1 Estimating the Regression Coefficients `L:1882`
  - 3.3.2 Extensions of the Linear Model `L:2163`
- 3.4 The Marketing Plan `L:2427`
- 3.5 Comparison of Linear Regression with K-Nearest Neighbors `L:2454`
- 3.6 Lab: Linear Regression `L:2502`
  - 3.6.4 Interaction Terms `L:2814`
- 3.6.5 Non-linear Transformations of the Predictors `L:2838`
- 3.6.6 Qualitative Predictors `L:2925`
- 3.6.7 Writing Functions `L:3000`
- 3.7 Exercises `L:3039`
- 4.1 An Overview of Classification `L:3209`
- 4.2 Why Not Linear Regression? `L:3227`
- 4.3 Logistic Regression `L:3259`
  - 4.3.3 Making Predictions `L:3328`
- 4.3.4 Multiple Logistic Regression `L:3349`
- 4.4.1 Linear Discriminant Analysis for p = 1 `L:3471`
  - 4.4.2 Linear Discriminant Analysis for p > 1 `L:3538`
  - 4.4.4 Naive Bayes `L:3694`
- 4.5 A Comparison of Classification Methods `L:3778`
- 4.5.2 An Empirical Comparison `L:3850`
- 4.6 Generalized Linear Models `L:3882`
- 4.6.1 Linear Regression on the Bikeshare Data `L:3890`
- 4.7 Lab: Classification Methods `L:4036`
  - 4.7.1 The Stock Market Data `L:4038`
  - 4.7.2 Logistic Regression `L:4122`
- 4.7.3 Linear Discriminant Analysis `L:4302`
- 4.7.4 Quadratic Discriminant Analysis `L:4383`
  - 4.7.6 K-Nearest Neighbors `L:4484`
- 4.7.7 Poisson Regression `L:4653`
- 5.1.1 The Validation Set Approach `L:4961`
- 5.1.3 k-Fold Cross-Validation `L:5037`
- 5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation `L:5061`
- 5.2 The Bootstrap `L:5102`
- 5.3 Lab: Cross-Validation and the Bootstrap `L:5162`
- 5.3.1 The Validation Set Approach `L:5166`
- 5.3.2 Leave-One-Out Cross-Validation `L:5229`
- 5.3.4 The Bootstrap `L:5301`
- 5.4 Exercises `L:5428`
- Linear Model Selection and Regularization `L:5530`
  - Cp, AIC, BIC, and Adjusted R2 `L:5669`
- 6.2 Shrinkage Methods `L:5737`
- 6.3.1 Principal Components Regression `L:6021`
- 6.3.2 Partial Least Squares `L:6116`
- 6.4 Considerations in High Dimensions `L:6144`
  - What Goes Wrong in High Dimensions? `L:6166`
- 6.4.3 Regression in High Dimensions `L:6190`
  - 6.4.4 Interpreting Results in High Dimensions `L:6208`
- 6.5 Lab: Linear Models and Regularization Methods `L:6216`
- 6.6 Exercises `L:6915`
- 7.1 Polynomial Regression `L:7062`
- 7.4 Regression Splines `L:7168`
  - 7.4.3 The Spline Basis Representation `L:7214`
- 7.4.5 Comparison to Polynomial Regression `L:7269`
- 7.5 Smoothing Splines `L:7277`
- 7.5.1 An Overview of Smoothing Splines `L:7281`
  - 7.5.2 Choosing the Smoothing Parameter λ `L:7304`
- 7.7 Generalized Additive Models `L:7368`
- 7.7.1 GAMs for Regression Problems `L:7384`
- 7.7.2 GAMs for Classification Problems `L:7442`
- 7.8 Lab: Non-linear Modeling `L:7469`
- 7.8.2 Splines `L:7735`
- 8.1 The Basics of Decision Trees `L:8128`
- 8.1.4 Advantages and Disadvantages of Trees `L:8310`
- 8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees `L:8324`
- 8.2.1 Bagging `L:8330`
  - 8.2.3 Boosting `L:8392`
  - 8.2.4 Bayesian Additive Regression Trees `L:8446`
  - 8.2.5 Summary of Tree Ensemble Methods `L:8512`
- 8.3 Lab: Decision Trees `L:8526`
- 8.3.1 Fitting Classification Trees `L:8528`
- 8.3.2 Fitting Regression Trees `L:8693`
- 8.3.3 Bagging and Random Forests `L:8752`
- 8.4 Exercises `L:8950`
- 9.1 Maximal Margin Classifier `L:9036`
  - 9.1.4 Construction of the Maximal Margin Classifier `L:9130`
- 9.2 Support Vector Classifiers `L:9159`
  - 9.2.1 Overview of the Support Vector Classifier `L:9161`
- 9.2.2 Details of the Support Vector Classifier `L:9190`
- 9.3 Support Vector Machines `L:9237`
  - 9.3.1 Classification with Non-Linear Decision Boundaries `L:9241`
  - 9.3.3 An Application to the Heart Disease Data `L:9330`
- 9.5 Relationship to Logistic Regression `L:9362`
- 9.6 Lab: Support Vector Machines `L:9411`
- 9.6.1 Support Vector Classifier `L:9415`
- 9.6.4 SVM with Multiple Classes `L:9758`
- 9.6.5 Application to Gene Expression Data `L:9782`
  - 10.1 Single Layer Neural Networks `L:9985`
- 10.2 Multilayer Neural Networks `L:10071`
- 10.3 Convolutional Neural Networks `L:10165`
  - 10.3.1 Convolution Layers `L:10189`
  - 10.3.3 Architecture of a Convolutional Neural Network `L:10251`
- Results Using a Pretrained Classifier `L:10295`
  - 10.5.1 Sequential Models for Document Classification `L:10424`
- 10.6 When to Use Deep Learning `L:10562`
- 10.7 Fitting a Neural Network `L:10604`
  - Regularization and Stochastic Gradient Descent `L:10686`
- 10.7.4 Network Tuning `L:10717`
- 10.8 Interpolation and Double Descent `L:10728`
- 10.9 Lab: Deep Learning `L:10774`
  - 10.9.2 A Multilayer Network on the MNIST Digit Data `L:10896`
- 10.10 Exercises `L:11498`
- Survival Analysis and Censored Data `L:11542`
- 11.2 A Closer Look at Censoring `L:11578`
- 11.3 The Kaplan-Meier Survival Curve `L:11590`
- 11.4 The Log-Rank Test `L:11648`
- 11.5 Regression Models With a Survival Response `L:11713`
- 11.5.1 The Hazard Function `L:11719`
  - 11.6 Shrinkage for the Cox Model `L:11932`
- 11.7 Additional Topics `L:11966`
  - 11.7.1 Area Under the Curve for Survival Analysis `L:11968`
  - 11.7.2 Choice of Time Scale `L:11986`
- 11.8 Lab: Survival Analysis `L:12012`
  - 11.8.1 Brain Cancer Data `L:12016`
- 11.8.2 Publication Data `L:12171`
- 12.1 The Challenge of Unsupervised Learning `L:12488`
- 12.2 Principal Components Analysis `L:12498`
- 12.3 Missing Values and Matrix Completion `L:12696`
- 12.4 Clustering Methods `L:12813`
- 12.4.2 Hierarchical Clustering `L:12892`
  - 12.4.3 Practical Issues in Clustering `L:12992`
- 12.5 Lab: Unsupervised Learning `L:13025`
- 12.5.1 Principal Components Analysis `L:13027`
- 12.5.4 NCI60 Data Example `L:13489`
- 13.1 A Quick Review of Hypothesis Testing `L:13804`
- 13.2 The Challenge of Multiple Testing `L:13929`
  - 13.3 The Family-Wise Error Rate `L:13947`
- 13.3.3 Trade-Off Between the FWER and Power `L:14101`
- 13.4 The False Discovery Rate `L:14111`
- 13.5 A Re-Sampling Approach to p-Values and False Discovery Rates `L:14179`
- 13.5.2 A Re-Sampling Approach to the False Discovery Rate `L:14237`
- 13.5.3 When Are Re-Sampling Approaches Useful? `L:14289`
- 13.6 Lab: Multiple Testing `L:14300`
- 13.6.1 Review of Hypothesis Tests `L:14302`
- 13.6.2 The Family-Wise Error Rate `L:14369`
- 13.6.3 The False Discovery Rate `L:14499`
- 13.6.4 A Re-Sampling Approach `L:14566`
- 13.7 Exercises `L:14704`
