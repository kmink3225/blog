---
name: "Pattern Recognition and Machine Learning"
type: book-summary
source_file: "Bishop-PRML_full.md"
authors: "Christopher M. Bishop"
year: 2006
total_pages: 738
language: en
keywords: [pattern recognition, machine learning, Bayesian methods, graphical models, neural networks, kernel methods, SVM, EM algorithm, variational inference, MCMC, sequential data, PCA]
---

# Pattern Recognition and Machine Learning — Summary

> Christopher M. Bishop (2006), 738 pages, 14 chapters
> 베이지안 관점에서 패턴인식과 머신러닝의 핵심 이론을 체계적으로 다루는 대학원 수준 교과서이다.

## Contents

1. Introduction
2. Probability Distributions
3. Linear Models for Regression
4. Linear Models for Classification
5. Neural Networks
6. Kernel Methods
7. Sparse Kernel Machines
8. Graphical Models
9. Mixture Models and EM
10. Approximate Inference
11. Sampling Methods
12. Continuous Latent Variables
13. Sequential Data
14. Combining Models
Appendix A: Data Sets
Appendix B: Probability Distributions
Appendix C: Properties of Matrices
Appendix D: Calculus of Variations
Appendix E: Lagrange Multipliers

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-66)

**핵심**: 다항식 곡선 적합 예제를 통해 머신러닝의 기본 개념을 도입한다. 확률론(베이즈 정리, 가우시안 분포), 모델 선택, 차원의 저주, 결정이론(오분류율 최소화, 기대 손실 최소화, 거부 옵션), 정보이론(엔트로피, KL 발산, 상호정보량)을 설명한다.

**키워드**: `polynomial curve fitting`, `Bayesian probability`, `decision theory`, `information theory`, `curse of dimensionality`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 1 (line 513)

### Ch 2: Probability Distributions (pp. 67-135)

**핵심**: 주요 확률분포를 다룬다. 이항 변수(베타 분포), 다항 변수(디리클레 분포), 가우시안 분포(조건부/주변 분포, 베이즈 정리, MLE, 순차 추정, 베이지안 추론, t-분포), 지수족, 비모수 방법(커널 밀도 추정, 최근접이웃)을 설명한다.

**키워드**: `Gaussian`, `beta distribution`, `Dirichlet`, `exponential family`, `conjugate priors`, `nonparametric`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 2 (line 237)

### Ch 3: Linear Models for Regression (pp. 137-177)

**핵심**: 선형 기저함수 모형을 다룬다. 최대우도와 최소제곱, 정규화 최소제곱, 편향-분산 분해, 베이지안 선형 회귀(매개변수 분포, 예측 분포, 등가 커널), 베이지안 모형 비교, 증거 근사를 설명한다.

**키워드**: `Bayesian linear regression`, `evidence approximation`, `bias-variance`, `predictive distribution`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 3 (line 260)

### Ch 4: Linear Models for Classification (pp. 179-224)

**핵심**: 선형 분류 모형을 다룬다. 판별함수(피셔 선형 판별, 퍼셉트론), 확률적 생성 모형(가우시안 클래스 조건부, 이산 특징, 지수족), 확률적 판별 모형(로지스틱 회귀, IRLS, 프로빗 회귀), 라플라스 근사, 베이지안 로지스틱 회귀를 설명한다.

**키워드**: `Fisher discriminant`, `logistic regression`, `Laplace approximation`, `Bayesian classification`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 4 (line 281)

### Ch 5: Neural Networks (pp. 225-284)

**핵심**: 피드포워드 신경망을 다룬다. 네트워크 함수와 가중치 공간 대칭성, 오차 역전파(오류함수 미분 평가, 야코비안 행렬), 헤시안 행렬(대각 근사, 외적 근사, 정확한 평가), 정규화(조기 종료, 불변성, 접선 전파, 합성곱 네트워크, 소프트 가중치 공유), 혼합 밀도 네트워크, 베이지안 신경망을 설명한다.

**키워드**: `backpropagation`, `Hessian`, `regularization`, `convolutional networks`, `mixture density networks`, `Bayesian neural networks`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 5 (line 308)

### Ch 6: Kernel Methods (pp. 291-324)

**핵심**: 커널 방법을 다룬다. 쌍대 표현, 커널 구성법, 방사 기저함수 네트워크(나다라야-왓슨 모형), 가우시안 과정(회귀, 분류, 하이퍼파라미터 학습, 자동 관련성 결정, 신경망과의 연결)을 설명한다.

**키워드**: `dual representation`, `kernel construction`, `Gaussian processes`, `ARD`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 6 (line 344)

### Ch 7: Sparse Kernel Machines (pp. 325-357)

**핵심**: 희소 커널 기계를 다룬다. 최대 마진 분류기(겹치는 클래스, 로지스틱 회귀와의 관계, 다중 클래스, 회귀, 계산학습이론), 관련 벡터 머신(RVM, 회귀/분류, 희소성 분석)을 설명한다.

**키워드**: `SVM`, `maximum margin`, `RVM`, `sparsity`, `computational learning theory`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 7 (line 358)

### Ch 8: Graphical Models (pp. 359-422)

**핵심**: 그래프 모형을 다룬다. 베이지안 네트워크(다항 회귀, 생성 모형, 이산/연속 변수), 조건부 독립(D-분리), 마르코프 랜덤 필드(조건부 독립 성질, 인수분해, 이미지 잡음제거), 그래프 모형에서의 추론(체인, 트리, 인수 그래프, 합-곱 알고리즘, 최대-합 알고리즘, 루피 신뢰 전파)을 설명한다.

**키워드**: `Bayesian networks`, `D-separation`, `MRF`, `factor graphs`, `sum-product`, `max-sum`, `belief propagation`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 8 (line 372)

### Ch 9: Mixture Models and EM (pp. 423-458)

**핵심**: 혼합 모형과 EM 알고리즘을 다룬다. K-평균 군집화, 가우시안 혼합의 최대우도와 EM, EM의 대안적 관점(가우시안 혼합 재방문, K-평균과의 관계, 베르누이 혼합, 베이지안 선형 회귀를 위한 EM), 일반적 EM 알고리즘을 설명한다.

**키워드**: `K-means`, `Gaussian mixture`, `EM algorithm`, `maximum likelihood`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 9 (line 396)

### Ch 10: Approximate Inference (pp. 461-522)

**핵심**: 근사 추론 방법을 다룬다. 변분 추론(인수분해 분포, 일변량 가우시안 예제, 모형 비교), 변분 가우시안 혼합, 변분 선형 회귀, 지수족 분포, 국소 변분 방법, 변분 로지스틱 회귀, 기대 전파(EP)를 설명한다.

**키워드**: `variational inference`, `factorized distribution`, `variational mixture`, `expectation propagation`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 10 (line 409)

### Ch 11: Sampling Methods (pp. 523-558)

**핵심**: 샘플링 방법을 다룬다. 기본 샘플링 알고리즘(거부 샘플링, 적응적 거부 샘플링, 중요도 샘플링, SIR), 마르코프 연쇄 몬테카를로(MCMC, 메트로폴리스-헤이스팅스), 깁스 샘플링, 슬라이스 샘플링, 하이브리드 몬테카를로(HMC, 동역학 시스템), 분할함수 추정을 설명한다.

**키워드**: `rejection sampling`, `importance sampling`, `MCMC`, `Metropolis-Hastings`, `Gibbs sampling`, `HMC`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 11 (line 438)

### Ch 12: Continuous Latent Variables (pp. 559-604)

**핵심**: 연속 잠재 변수 모형을 다룬다. 주성분 분석(PCA, 최대 분산/최소 오차 공식화, 고차원 데이터), 확률적 PCA(MLE, EM, 베이지안 PCA, 인자 분석), 커널 PCA, 비선형 잠재변수 모형(ICA, 자기연관 신경망, 비선형 다양체 모델링)을 설명한다.

**키워드**: `PCA`, `probabilistic PCA`, `factor analysis`, `kernel PCA`, `ICA`, `autoencoders`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 12 (line 456)

### Ch 13: Sequential Data (pp. 605-652)

**핵심**: 순차 데이터 모형을 다룬다. 마르코프 모형, 은닉 마르코프 모형(HMM, 최대우도, 전방-후방 알고리즘, 비터비 알고리즘), 선형 동적 시스템(LDS, 칼만 필터, 추론과 학습, 입자 필터)을 설명한다.

**키워드**: `HMM`, `forward-backward`, `Viterbi`, `Kalman filter`, `particle filters`, `LDS`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 13 (line 475)

### Ch 14: Combining Models (pp. 653-676)

**핵심**: 모형 결합 방법을 다룬다. 베이지안 모형 평균화, 위원회(커미티), 부스팅(지수 오류 최소화, 부스팅 오류 함수), 트리 기반 모형, 조건부 혼합 모형(선형 회귀 혼합, 로지스틱 모형 혼합, 전문가 혼합)을 설명한다.

**키워드**: `model averaging`, `boosting`, `committees`, `mixture of experts`, `decision trees`

**상세**: → `Bishop-Pattern-Recognition-and-Machine-Learning-2006_full.md` Ch 14 (line 490)
