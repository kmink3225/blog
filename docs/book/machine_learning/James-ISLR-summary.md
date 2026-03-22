---
name: "An Introduction to Statistical Learning with Applications in R, 2nd Ed"
type: book-summary
authors: "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani"
year: 2021
total_pages: 607
language: en
keywords: [statistical learning, R, regression, classification, resampling, regularization, SVM, deep learning, survival analysis, unsupervised learning, multiple testing, decision trees, boosting]
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

**상세**: → (삭제됨) Ch 1 (line 403)

### Ch 2: Statistical Learning (pp. 15-57)

**핵심**: 통계적 학습의 기본 개념을 다룬다. f를 추정하는 이유(예측 vs 추론), f 추정 방법(모수적/비모수적), 예측 정확도와 모형 해석가능성의 트레이드오프, 지도학습 대 비지도학습, 모형 정확도 평가(적합도 측정, 편향-분산 트레이드오프, 분류 설정)를 설명한다. R 입문 실습을 포함한다.

**키워드**: `bias-variance tradeoff`, `MSE`, `flexibility`, `parametric`, `nonparametric`

**상세**: → (삭제됨) Ch 2 (line 405)

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

**상세**: → (삭제됨) Ch 3 (line 115)

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

**상세**: → (삭제됨) Ch 4 (line 145)

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

**상세**: → (삭제됨) Ch 5 (line 178)

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

**상세**: → (삭제됨) Ch 6 (line 197)

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

**상세**: → (삭제됨) Ch 7 (line 223)

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

**상세**: → (삭제됨) Ch 8 (line 249)

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

**상세**: → (삭제됨) Ch 9 (line 269)

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

**상세**: → (삭제됨) Ch 10 (line 297)

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

**상세**: → (삭제됨) Ch 11 (line 328)

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

**상세**: → (삭제됨) Ch 12 (line 350)

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

**상세**: → (삭제됨) Ch 13 (line 372)

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
