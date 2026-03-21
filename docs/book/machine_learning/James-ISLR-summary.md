---
name: "An Introduction to Statistical Learning with Applications in R, 2nd Ed"
type: book-summary
source_file: "James-ISLR_full.md"
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

### Ch 1: Introduction (pp. 1-14)

**핵심**: 통계적 학습의 개요를 소개한다. 임금 데이터, 주식시장 데이터, 유전자 발현 데이터 등 세 가지 실제 데이터를 통해 지도학습과 비지도학습의 응용 사례를 보여준다. 이 책의 구조와 ESL과의 관계를 설명한다.

**키워드**: `statistical learning`, `supervised learning`, `unsupervised learning`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 1 (line 403)

### Ch 2: Statistical Learning (pp. 15-57)

**핵심**: 통계적 학습의 기본 개념을 다룬다. f를 추정하는 이유(예측 vs 추론), f 추정 방법(모수적/비모수적), 예측 정확도와 모형 해석가능성의 트레이드오프, 지도학습 대 비지도학습, 모형 정확도 평가(적합도 측정, 편향-분산 트레이드오프, 분류 설정)를 설명한다. R 입문 실습을 포함한다.

**키워드**: `bias-variance tradeoff`, `MSE`, `flexibility`, `parametric`, `nonparametric`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 2 (line 405)

### Ch 3: Linear Regression (pp. 59-128)

**핵심**: 선형 회귀를 다룬다. 단순 선형 회귀(계수 추정, 정확도 평가), 다중 선형 회귀(회귀 계수 추정, 중요 질문들), 질적 예측변수, 선형 모형의 확장(상호작용, 비선형), 잠재적 문제점(비선형성, 상관 오차, 이분산성, 이상값, 다중공선성), KNN과의 비교를 설명한다.

**키워드**: `simple regression`, `multiple regression`, `qualitative predictors`, `collinearity`, `KNN`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 3 (line 115)

### Ch 4: Classification (pp. 129-196)

**핵심**: 분류 방법을 다룬다. 로지스틱 회귀(로지스틱 모형, 다항 로지스틱), 분류를 위한 생성 모형(LDA, QDA, 나이브 베이즈), 분류 방법 비교, 일반화 선형 모형(포아송 회귀 포함)을 설명한다. 주식시장 데이터를 이용한 R 실습을 포함한다.

**키워드**: `logistic regression`, `LDA`, `QDA`, `naive Bayes`, `Poisson regression`, `GLM`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 4 (line 145)

### Ch 5: Resampling Methods (pp. 197-224)

**핵심**: 재표본 방법을 다룬다. 교차검증(검증 세트 접근법, LOOCV, k-겹 교차검증, 편향-분산 트레이드오프, 분류 문제에서의 교차검증)과 부트스트랩을 설명한다. R 실습을 포함한다.

**키워드**: `cross-validation`, `LOOCV`, `k-fold`, `bootstrap`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 5 (line 178)

### Ch 6: Linear Model Selection and Regularization (pp. 225-288)

**핵심**: 선형 모형 선택과 정규화를 다룬다. 부분집합 선택(최적 부분집합, 단계적 선택), 축소 방법(릿지 회귀, 라소, 튜닝 파라미터 선택), 차원 축소 방법(주성분 회귀, 부분 최소제곱), 고차원에서의 고려사항을 설명한다.

**키워드**: `subset selection`, `ridge regression`, `lasso`, `PCR`, `PLS`, `high-dimensional`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 6 (line 197)

### Ch 7: Moving Beyond Linearity (pp. 289-326)

**핵심**: 비선형 방법을 다룬다. 다항 회귀, 단계 함수, 기저 함수, 회귀 스플라인(구간별 다항식, 매듭 선택), 평활 스플라인, 국소 회귀, 일반화 가법 모형(GAM, 회귀/분류)을 설명한다.

**키워드**: `polynomial regression`, `splines`, `smoothing splines`, `local regression`, `GAM`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 7 (line 223)

### Ch 8: Tree-Based Methods (pp. 327-366)

**핵심**: 트리 기반 방법을 다룬다. 결정 트리의 기초(회귀 트리, 분류 트리, 트리 대 선형 모형), 배깅, 랜덤 포레스트, 부스팅, 베이지안 가법 회귀 트리(BART), 트리 앙상블 방법 요약을 설명한다.

**키워드**: `decision trees`, `bagging`, `random forests`, `boosting`, `BART`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 8 (line 249)

### Ch 9: Support Vector Machines (pp. 367-402)

**핵심**: 서포트 벡터 머신을 다룬다. 최대 마진 분류기(초평면, 분리 불가능 경우), 서포트 벡터 분류기, 서포트 벡터 머신(비선형 결정 경계, 커널), 다중 클래스 SVM(일대일, 일대나머지), 로지스틱 회귀와의 관계를 설명한다.

**키워드**: `maximal margin classifier`, `support vector classifier`, `SVM`, `kernel`, `ROC`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 9 (line 269)

### Ch 10: Deep Learning (pp. 403-460)

**핵심**: 딥러닝을 다룬다. 단층/다층 신경망, 합성곱 신경망(CNN, 합성곱 층, 풀링 층, 데이터 증강, 사전학습 분류기), 문서 분류, 순환 신경망(RNN, 시계열 예측), 딥러닝 사용 시점, 신경망 적합(역전파, 정규화, SGD, 드롭아웃), 보간과 이중 하강을 설명한다.

**키워드**: `neural networks`, `CNN`, `RNN`, `backpropagation`, `dropout`, `double descent`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 10 (line 297)

### Ch 11: Survival Analysis and Censored Data (pp. 461-496)

**핵심**: 생존분석과 중도절단 데이터를 다룬다. 생존 시간과 중도절단 시간, 카플란-마이어 생존 곡선, 로그순위 검정, 위험함수와 비례위험 모형(콕스 모형), 콕스 모형의 축소, AUC, 시간의존 공변량, 생존 트리를 설명한다.

**키워드**: `survival analysis`, `censoring`, `Kaplan-Meier`, `Cox model`, `hazard function`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 11 (line 328)

### Ch 12: Unsupervised Learning (pp. 497-552)

**핵심**: 비지도학습을 다룬다. 주성분 분석(PCA, 분산 설명 비율), 결측값과 행렬 완성, 군집 방법(K-평균 군집화, 계층적 군집화, 군집화의 실제적 이슈)을 설명한다. NCI60 데이터 예제를 포함한 R 실습을 제공한다.

**키워드**: `PCA`, `K-means`, `hierarchical clustering`, `matrix completion`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 12 (line 350)

### Ch 13: Multiple Testing (pp. 553-596)

**핵심**: 다중 검정을 다룬다. 가설 검정 복습(제1종/제2종 오류), 다중 검정의 도전, 족내 오류율(FWER, 본페로니 보정, 홀름 절차), 거짓 발견율(FDR, 벤자미니-호크버그 절차), p-값과 FDR의 재표본 접근법을 설명한다.

**키워드**: `hypothesis testing`, `FWER`, `FDR`, `Bonferroni`, `Benjamini-Hochberg`, `resampling`

**상세**: → `An Introduction to Statistical Learning (ISLR), 2nd Ed_full.md` Ch 13 (line 372)
