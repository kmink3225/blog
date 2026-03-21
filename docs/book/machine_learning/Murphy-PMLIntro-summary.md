---
name: "Probabilistic Machine Learning: An Introduction"
type: book-summary
source_file: "Murphy-PMLIntro_full.md"
authors: "Kevin P. Murphy"
year: 2022
total_pages: 826
language: en
keywords: [probabilistic ML, Bayesian inference, statistics, decision theory, information theory, linear models, neural networks, CNN, RNN, kernel methods, trees, boosting, clustering, dimensionality reduction, recommender systems]
---

# Probabilistic Machine Learning: An Introduction — Summary

> Kevin P. Murphy (2022), 826 pages, 23 chapters (5 Parts + Appendix)
> 확률적 관점에서 머신러닝의 기초부터 딥러닝, 비지도학습까지 포괄적으로 다루는 현대적 교과서이다.

## Contents

**Part I: Foundations**
1. Introduction
2. Probability: Univariate Models
3. Probability: Multivariate Models
4. Statistics
5. Decision Theory
6. Information Theory
7. Linear Algebra
8. Optimization

**Part II: Linear Models**
9. Linear Discriminant Analysis
10. Logistic Regression
11. Linear Regression
12. Generalized Linear Models *

**Part III: Deep Neural Networks**
13. Neural Networks for Tabular Data
14. Neural Networks for Images
15. Neural Networks for Sequences

**Part IV: Nonparametric Models**
16. Exemplar-based Methods
17. Kernel Methods *
18. Trees, Forests, Bagging, and Boosting

**Part V: Beyond Supervised Learning**
19. Learning with Fewer Labeled Examples
20. Dimensionality Reduction
21. Clustering
22. Recommender Systems
23. Graph Embeddings *

Appendix A: Notation

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-30)

**핵심**: 머신러닝이 무엇인지 정의하고 주요 유형을 소개한다. 지도학습(분류, 회귀, 과적합과 일반화, 무공짜 점심 정리), 비지도학습(군집화, 잠재 인자 발견, 자기지도학습), 강화학습을 설명한다. 일반적인 이미지/텍스트 데이터셋과 데이터 전처리 방법도 다룬다.

**키워드**: `classification`, `regression`, `overfitting`, `no free lunch`, `self-supervised learning`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 1 (line 115)

### Ch 2: Probability: Univariate Models (pp. 33-76)

**핵심**: 일변량 확률 모형을 다룬다. 확률의 정의와 불확실성 유형, 확률변수(이산/연속, 적률), 베이즈 정리(COVID-19 검사 예제, 몬티 홀 문제), 베르누이/이항 분포, 범주형/다항 분포(소프트맥스 함수), 가우시안 분포, 기타 분포(t-분포, 라플라스, 베타, 감마)를 설명한다.

**키워드**: `Bayes rule`, `Bernoulli`, `categorical`, `Gaussian`, `softmax`, `Student-t`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 2 (line 139)

### Ch 3: Probability: Multivariate Models (pp. 77-106)

**핵심**: 다변량 확률 모형을 다룬다. 결합 분포, 주변 분포, 조건부 분포, 다변량 가우시안, 혼합 모형, 확률적 그래프 모형(DAG, 조건부 독립)을 설명한다.

**키워드**: `joint distribution`, `multivariate Gaussian`, `mixture models`, `graphical models`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 3 (line 192)

### Ch 4: Statistics (pp. 107-166)

**핵심**: 통계적 추론의 기초를 다룬다. 최대우도추정(MLE), 경험적 위험 최소화(ERM), 모형의 과적합/부적합, 정규화, 베이지안 통계(사전분포, 사후분포, 사후예측, 신뢰구간), 빈도론적 통계(편향-분산 트레이드오프, 신뢰구간, 가설검정)를 설명한다.

**키워드**: `MLE`, `ERM`, `Bayesian statistics`, `frequentist statistics`, `regularization`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 4 (line 224)

### Ch 5: Decision Theory (pp. 167-206)

**핵심**: 결정이론을 다룬다. 베이지안 결정이론, 분류기 평가(ROC, PR 곡선), 회귀 손실, 확률적 예측(적절 채점 규칙), 불확실성 하의 결정(효용이론, 다기준 결정 분석)을 설명한다.

**키워드**: `Bayesian decision theory`, `ROC`, `loss functions`, `proper scoring rules`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 5 (line 83)

### Ch 6: Information Theory (pp. 207-228)

**핵심**: 정보이론을 다룬다. 엔트로피, 교차 엔트로피, KL 발산, 상호정보량, 데이터 처리 부등식, 충분통계량을 설명한다.

**키워드**: `entropy`, `cross-entropy`, `KL divergence`, `mutual information`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 6 (line 84)

### Ch 7: Linear Algebra (pp. 229-274)

**핵심**: 머신러닝에 필요한 선형대수를 다룬다. 벡터 공간, 행렬 분해(고유값, SVD, QR, 촐레스키), 행렬의 미적분(그래디언트, 헤시안), 행렬 근사(저랭크), 텐서를 설명한다.

**키워드**: `eigendecomposition`, `SVD`, `matrix calculus`, `low-rank approximation`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 7 (line 340)

### Ch 8: Optimization (pp. 275-320)

**핵심**: 최적화 방법을 다룬다. 1차 방법(경사하강법, 모멘텀, SGD, Adam), 2차 방법(뉴턴법, BFGS), 제약 최적화(라그랑주 승수법, KKT 조건), 볼록 최적화, 확률적 최적화를 설명한다.

**키워드**: `gradient descent`, `SGD`, `Adam`, `Newton method`, `convex optimization`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 8 (line 395)

### Ch 9: Linear Discriminant Analysis (pp. 323-338)

**핵심**: 선형 판별분석을 다룬다. 가우시안 판별분석(GDA), 이차 판별분석(QDA), 정규화 판별분석, 최근접 축소 중심(NSC), 피셔 선형 판별을 설명한다.

**키워드**: `GDA`, `QDA`, `Fisher discriminant`, `nearest shrunken centroids`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 9 (line 439)

### Ch 10: Logistic Regression (pp. 339-370)

**핵심**: 로지스틱 회귀를 다룬다. 이진/다항 로지스틱 회귀, MLE 추정(SGD, 뉴턴법), 정규화(L2, L1), 베이지안 로지스틱 회귀(라플라스 근사, 변분추론)를 설명한다.

**키워드**: `logistic regression`, `multinomial`, `regularization`, `Bayesian logistic regression`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 10 (line 458)

### Ch 11: Linear Regression (pp. 371-414)

**핵심**: 선형 회귀를 다룬다. 최소제곱, 릿지 회귀, 라소, 탄력적 그물, 로버스트 회귀, 베이지안 선형 회귀, 변수 선택, 혼합효과 모형을 설명한다.

**키워드**: `least squares`, `ridge`, `lasso`, `elastic net`, `Bayesian linear regression`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 11 (line 488)

### Ch 12: Generalized Linear Models (pp. 415-424)

**핵심**: 일반화 선형 모형을 다룬다. GLM 프레임워크(링크 함수, 지수족), 포아송 회귀, 프로빗 회귀를 설명한다.

**키워드**: `GLM`, `link function`, `exponential family`, `Poisson regression`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 12 (line 533)

### Ch 13: Neural Networks for Tabular Data (pp. 425-466)

**핵심**: 테이블 데이터를 위한 신경망을 다룬다. 다층 퍼셉트론(MLP), 활성화 함수, 역전파, 배치 정규화, 드롭아웃, 잔차 연결, 신경망 해석가능성을 설명한다.

**키워드**: `MLP`, `backpropagation`, `batch normalization`, `dropout`, `residual connections`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 13 (line 543)

### Ch 14: Neural Networks for Images (pp. 467-502)

**핵심**: 이미지를 위한 신경망을 다룬다. 합성곱 신경망(CNN), 합성곱 연산, 풀링, 주요 CNN 아키텍처(LeNet, AlexNet, ResNet 등), 객체 탐지, 의미론적 분할, 이미지 생성을 설명한다.

**키워드**: `CNN`, `convolution`, `pooling`, `ResNet`, `object detection`, `semantic segmentation`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 14 (line 580)

### Ch 15: Neural Networks for Sequences (pp. 503-544)

**핵심**: 순차 데이터를 위한 신경망을 다룬다. 순환 신경망(RNN, LSTM, GRU), 1차원 CNN, 어텐션 메커니즘, 트랜스포머, 자기지도학습(BERT, GPT)을 설명한다.

**키워드**: `RNN`, `LSTM`, `GRU`, `attention`, `transformer`, `BERT`, `GPT`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 15 (line 95)

### Ch 16: Exemplar-based Methods (pp. 547-566)

**핵심**: 예시 기반 방법을 다룬다. K-최근접이웃(KNN), 거리 측도 학습, 커널 밀도 추정을 설명한다.

**키워드**: `KNN`, `distance metric learning`, `kernel density estimation`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 16 (line 97)

### Ch 17: Kernel Methods (pp. 567-602)

**핵심**: 커널 방법을 다룬다. 메르서 커널, 가우시안 과정(GP), 서포트 벡터 머신(SVM), 커널화 방법의 비교를 설명한다.

**키워드**: `Mercer kernels`, `Gaussian processes`, `SVM`, `kernel trick`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 17 (line 98)

### Ch 18: Trees, Forests, Bagging, and Boosting (pp. 603-624)

**핵심**: 트리 기반 앙상블 방법을 다룬다. 결정 트리(CART), 배깅, 랜덤 포레스트, 그래디언트 부스팅(XGBoost, LightGBM), 해석가능성 도구를 설명한다.

**키워드**: `CART`, `random forests`, `gradient boosting`, `XGBoost`, `LightGBM`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 18 (line 99)

### Ch 19: Learning with Fewer Labeled Examples (pp. 627-656)

**핵심**: 적은 레이블 데이터로 학습하는 방법을 다룬다. 데이터 증강, 전이 학습, 준지도학습, 능동학습, 메타학습(few-shot learning)을 설명한다.

**키워드**: `data augmentation`, `transfer learning`, `semi-supervised`, `active learning`, `meta-learning`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 19 (line 105)

### Ch 20: Dimensionality Reduction (pp. 657-714)

**핵심**: 차원축소 방법을 다룬다. PCA, 인자 분석, 오토인코더, 다양체 학습(t-SNE, UMAP, Isomap)을 설명한다.

**키워드**: `PCA`, `factor analysis`, `autoencoders`, `t-SNE`, `UMAP`, `manifold learning`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 20 (line 106)

### Ch 21: Clustering (pp. 715-740)

**핵심**: 군집화 방법을 다룬다. K-평균, 가우시안 혼합 모형(GMM)과 EM 알고리즘, 계층적 군집화, 스펙트럼 군집화, 군집 유효성 평가를 설명한다.

**키워드**: `K-means`, `GMM`, `EM algorithm`, `hierarchical clustering`, `spectral clustering`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 21 (line 107)

### Ch 22: Recommender Systems (pp. 741-752)

**핵심**: 추천 시스템을 다룬다. 협업 필터링(행렬 분해, 신경 협업 필터링), 콘텐츠 기반 필터링, 하이브리드 방법을 설명한다.

**키워드**: `collaborative filtering`, `matrix factorization`, `content-based filtering`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 22 (line 108)

### Ch 23: Graph Embeddings (pp. 753-772)

**핵심**: 그래프 임베딩 방법을 다룬다. 그래프 신경망(GNN), 노드/그래프 수준 임베딩, 지식 그래프 임베딩을 설명한다.

**키워드**: `GNN`, `graph embeddings`, `knowledge graphs`, `node embeddings`

**상세**: → `Probabilistic Machine Learning An Introduction_full.md` Ch 23 (line 109)
