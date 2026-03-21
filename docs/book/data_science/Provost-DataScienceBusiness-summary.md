---
name: "Data Science for Business"
type: book-summary
source_file: "Provost-DataScienceBusiness_full.md"
authors: "Foster Provost, Tom Fawcett"
year: 2013
total_pages: 414
language: en
keywords: [data-science, data-mining, predictive-modeling, classification, overfitting, clustering, evaluation, ROC, text-mining, business-strategy]
---

# Data Science for Business — Summary

> Foster Provost, Tom Fawcett (2013), 414 pages, 14 chapters + Appendices
> 데이터 과학의 기본 원리를 비즈니스 문제 해결 관점에서 체계적으로 설명하는 교과서이다.

## Contents

- Preface
- Ch 1: Introduction: Data-Analytic Thinking
- Ch 2: Business Problems and Data Science Solutions
- Ch 3: Introduction to Predictive Modeling: From Correlation to Supervised Segmentation
- Ch 4: Fitting a Model to Data
- Ch 5: Overfitting and Its Avoidance
- Ch 6: Similarity, Neighbors, and Clusters
- Ch 7: Decision Analytic Thinking I: What Is a Good Model?
- Ch 8: Visualizing Model Performance
- Ch 9: Evidence and Probabilities
- Ch 10: Representing and Mining Text
- Ch 11: Decision Analytic Thinking II: Toward Analytical Engineering
- Ch 12: Other Data Science Tasks and Techniques
- Ch 13: Data Science and Business Strategy
- Ch 14: Conclusion
- Appendix A: Proposal Review Guide
- Appendix B: Another Sample Proposal
- Glossary / Bibliography / Index

---

## Chapter Summaries

### Ch 1: Introduction: Data-Analytic Thinking (pp. 1-16)
**핵심**: 데이터 기회의 편재성을 허리케인 프랜시스 사례와 고객 이탈 예측으로 설명한다. 데이터 과학, 엔지니어링, 데이터 기반 의사결정의 관계를 정의하고, 빅데이터 1.0에서 2.0으로의 전환을 다룬다. 데이터와 데이터 과학 역량을 전략적 자산으로 보는 분석적 사고(data-analytic thinking)의 중요성을 강조한다.
**키워드**: `data-analytic-thinking`, `strategic-asset`, `big-data`, `customer-churn`
**상세**: → `data science for business_full.md` Ch 1 (line 148)

### Ch 2: Business Problems and Data Science Solutions (pp. 19-41)
**핵심**: 비즈니스 문제를 데이터 마이닝 과제(분류, 회귀, 유사도 매칭, 클러스터링, 연관 규칙 등)로 변환하는 방법을 설명한다. 지도학습과 비지도학습을 구분하고, CRISP-DM 프로세스(비즈니스 이해 → 데이터 이해 → 데이터 준비 → 모델링 → 평가 → 배포)를 제시한다. 통계, 데이터베이스 쿼리, 회귀 분석, 머신러닝 등 관련 기법과의 관계를 정리한다.
**키워드**: `CRISP-DM`, `supervised-unsupervised`, `data-mining-tasks`, `business-understanding`
**상세**: → `data science for business_full.md` Ch 2 (line 164)

### Ch 3: Introduction to Predictive Modeling (pp. 43-78)
**핵심**: 정보 이득(information gain)을 활용한 속성 선택과 트리 구조 모델을 통한 지도 세분화(supervised segmentation)를 설명한다. 엔트로피 기반 속성 선택 예제를 상세히 다루고, 결정 트리의 시각화와 규칙 집합으로의 변환을 보여준다. 고객 이탈 문제에 트리 유도를 적용하는 사례를 제시한다.
**키워드**: `information-gain`, `decision-tree`, `supervised-segmentation`, `entropy`
**상세**: → `data science for business_full.md` Ch 3 (line 194)

### Ch 4: Fitting a Model to Data (pp. 81-108)
**핵심**: 목적 함수·손실 함수의 개념과 데이터 기반 최적 모델 파라미터 탐색 과정을 설명한다. 선형 판별 함수, 로지스틱 회귀, 서포트 벡터 머신(SVM)을 예시 기법으로 다룬다. 비선형 함수, SVM 커널, 신경망으로의 확장을 소개하고, 로지스틱 회귀와 트리 유도의 비교 사례를 제시한다.
**키워드**: `objective-function`, `logistic-regression`, `SVM`, `linear-discriminant`
**상세**: → `data science for business_full.md` Ch 4 (line 210)

### Ch 5: Overfitting and Its Avoidance (pp. 111-140)
**핵심**: 일반화(generalization) 개념과 과적합의 메커니즘을 트리 유도·수학적 함수 모두에서 분석한다. 홀드아웃 데이터와 적합 그래프를 통한 과적합 시각화, 교차 검증(cross-validation)으로의 발전을 설명한다. 학습 곡선(learning curve), 트리 가지치기, 정규화(regularization) 등 복잡도 제어 기법을 다룬다.
**키워드**: `overfitting`, `cross-validation`, `regularization`, `learning-curve`, `complexity-control`
**상세**: → `data science for business_full.md` Ch 5 (line 234)

### Ch 6: Similarity, Neighbors, and Clusters (pp. 141-184)
**핵심**: 유사도·거리 개념을 정의하고 최근접 이웃(nearest-neighbor) 방법의 예측 모델링 적용을 설명한다. 위스키 분석 사례로 유사도 기반 추론을 보여주고, 이질적 속성·거리 함수 선택의 기술적 세부사항을 다룬다. 계층적 클러스터링과 중심점(centroid) 기반 클러스터링(k-means), 비즈니스 뉴스 클러스터링 사례를 포함한다.
**키워드**: `nearest-neighbor`, `clustering`, `k-means`, `similarity`, `distance-metrics`
**상세**: → `data science for business_full.md` Ch 6 (line 255)

### Ch 7: Decision Analytic Thinking I: What Is a Good Model? (pp. 187-207)
**핵심**: 데이터 과학 결과물에 대한 신중한 평가의 필요성을 강조하고, 기대값(expected value)을 핵심 평가 프레임워크로 제시한다. 혼동 행렬(confusion matrix), 불균형 클래스·불균등 비용/편익 문제를 분석한다. 기대 이익 계산, 베이스라인 성능 비교, 데이터 투자에 대한 시사점을 다룬다.
**키워드**: `expected-value`, `confusion-matrix`, `baseline`, `cost-benefit-analysis`
**상세**: → `data science for business_full.md` Ch 7 (line 289)

### Ch 8: Visualizing Model Performance (pp. 209-231)
**핵심**: 분류 대신 랭킹 관점에서 모델 성능을 시각화하는 기법을 다룬다. 이익 곡선(profit curve), ROC 그래프/곡선과 AUC, 누적 응답 곡선(cumulative response curve), 리프트 곡선(lift curve)을 설명한다. 고객 이탈 모델링의 성능 분석 사례를 통해 시각화 기법의 실무 적용을 보여준다.
**키워드**: `ROC-curve`, `AUC`, `profit-curve`, `lift-curve`, `cumulative-response`
**상세**: → `data science for business_full.md` Ch 8 (line 307)

### Ch 9: Evidence and Probabilities (pp. 233-247)
**핵심**: 베이즈 정리(Bayes' Rule)를 활용한 명시적 증거 결합과 조건부 독립 가정 하의 확률적 추론을 설명한다. 나이브 베이즈 분류의 원리·장단점을 다루고, 증거 리프트(evidence lift) 모델을 소개한다. Facebook 좋아요 데이터의 증거 리프트, 온라인 광고 타겟팅 사례를 제시한다.
**키워드**: `Bayes-rule`, `naive-Bayes`, `evidence-lift`, `conditional-independence`
**상세**: → `data science for business_full.md` Ch 9 (line 320)

### Ch 10: Representing and Mining Text (pp. 249-275)
**핵심**: 텍스트의 중요성과 어려움을 설명하고, Bag of Words 표현, TF-IDF 계산, N-gram, 스테밍, 개체명 추출, 토픽 모델 등 텍스트 표현 기법을 다룬다. 재즈 뮤지션 사례로 TF-IDF를 실습하고, 뉴스 기사 마이닝을 통한 주가 예측 사례로 텍스트 마이닝의 실전 적용을 보여준다.
**키워드**: `TF-IDF`, `bag-of-words`, `topic-models`, `text-mining`, `N-gram`
**상세**: → `data science for business_full.md` Ch 10 (line 343)

### Ch 11: Decision Analytic Thinking II: Toward Analytical Engineering (pp. 277-287)
**핵심**: 기대값 프레임워크를 활용한 데이터 과학 솔루션의 분석적 설계(analytical engineering)를 다룬다. 자선 우편물 타겟팅, 고객 이탈 문제의 인센티브 영향 평가 등 복잡한 비즈니스 문제를 기대값 분해로 구조화하고 데이터 과학 솔루션으로 전환하는 방법을 보여준다.
**키워드**: `analytical-engineering`, `expected-value-decomposition`, `selection-bias`, `incentive`
**상세**: → `data science for business_full.md` Ch 11 (line 369)

### Ch 12: Other Data Science Tasks and Techniques (pp. 289-310)
**핵심**: 공출현·연관 규칙(리프트, 레버리지), 행동 프로파일링, 링크 예측, 데이터 축소, 잠재 정보 마이닝(영화 추천), 편향-분산 분해, 앙상블 방법, 데이터 기반 인과 추론 등 추가 기법을 소개한다. 맥주와 복권, Facebook 좋아요 연관 등 사례를 활용한다.
**키워드**: `association-rules`, `profiling`, `ensemble`, `bias-variance`, `causal-reasoning`
**상세**: → `data science for business_full.md` Ch 12 (line 398)

### Ch 13: Data Science and Business Strategy (pp. 313-327)
**핵심**: 데이터 과학을 통한 경쟁 우위 확보와 지속 전략을 다룬다. 역사적 데이터 자산, 고유 지적 재산, 무형 부수 자산, 우수 데이터 과학자, 탁월한 관리 등 지속 가능한 차별화 요인을 분석한다. 데이터 과학 프로젝트 제안서 평가 방법과 기업의 데이터 과학 성숙도 모델을 제시한다.
**키워드**: `competitive-advantage`, `data-science-maturity`, `strategic-asset`, `talent-management`
**상세**: → `data science for business_full.md` Ch 13 (line 416)

### Ch 14: Conclusion (pp. 331-344)
**핵심**: 전체 기본 개념을 정리하고 모바일 디바이스 데이터 마이닝이라는 새로운 문제에 적용한다. 비즈니스 문제 해결에 대한 사고 방식의 전환, 인간 참여(human-in-the-loop)의 한계, 프라이버시·윤리 문제, 크라우드소싱에서 클라우드소싱으로의 전환을 다룬다.
**키워드**: `mobile-data`, `human-in-the-loop`, `privacy`, `ethics`, `crowd-sourcing`
**상세**: → `data science for business_full.md` Ch 14 (line 444)
