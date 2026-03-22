---
name: "Data Science for Business"
type: book-summary
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

> Marker 원본: `Provost-DataScienceBusiness_marker_full.md` | 총 ~6,602 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Introduction: Data-Analytic Thinking (pp. 1-16)
**핵심**: 데이터 기회의 편재성을 허리케인 프랜시스 사례와 고객 이탈 예측으로 설명한다. 데이터 과학, 엔지니어링, 데이터 기반 의사결정의 관계를 정의하고, 빅데이터 1.0에서 2.0으로의 전환을 다룬다. 데이터와 데이터 과학 역량을 전략적 자산으로 보는 분석적 사고(data-analytic thinking)의 중요성을 강조한다.
**키워드**: `data-analytic-thinking`, `strategic-asset`, `big-data`, `customer-churn`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 1 (L:519)
허리케인 프랜시스 사례에서 Walmart가 과거 허리케인 데이터를 분석하여 딸기 팝타르트와 맥주의 비정상적 수요 급증 패턴을 발견한 데이터 기반 예측의 가치를 보여준다. MegaTelCo의 고객 이탈(churn) 문제를 책 전체를 관통하는 사례로 소개하며, 20%의 이탈률을 줄이기 위한 데이터 과학적 접근을 설계한다. Target의 임신 고객 예측 사례(식단, 비타민, 의류 구매 패턴 분석)로 예측 모델의 경쟁 우위 확보 효과를 설명한다. 데이터 기반 의사결정(DDD)의 효과를 MIT/Wharton 연구로 실증하며, DDD 수준이 높은 기업이 생산성 4-6% 향상, ROA/ROE 개선을 보인다. DDD를 두 유형으로 구분한다: (1) 데이터 내 "발견"이 필요한 의사결정(Walmart 사례), (2) 대규모로 반복되어 작은 정확도 향상도 큰 이익을 주는 의사결정(이탈 예측). 데이터 과학은 데이터에서 자동화된 분석을 통해 지식을 추출하는 원리·프로세스·기법의 집합으로 정의하며, 데이터 마이닝은 이를 구현하는 기술이다. 빅데이터 1.0(대규모 데이터 저장·접근)에서 2.0(데이터 기반 제품·서비스 혁신)으로의 전환을 다루며, Google, Amazon, LinkedIn의 사례를 제시한다. 데이터와 데이터 과학 역량을 전략적 자산으로 보는 분석적 사고(data-analytic thinking)가 데이터 과학자뿐 아니라 경영자에게도 필수적임을 강조한다.

### Ch 2: Business Problems and Data Science Solutions (pp. 19-41)
**핵심**: 비즈니스 문제를 데이터 마이닝 과제(분류, 회귀, 유사도 매칭, 클러스터링, 연관 규칙 등)로 변환하는 방법을 설명한다. 지도학습과 비지도학습을 구분하고, CRISP-DM 프로세스(비즈니스 이해 → 데이터 이해 → 데이터 준비 → 모델링 → 평가 → 배포)를 제시한다. 통계, 데이터베이스 쿼리, 회귀 분석, 머신러닝 등 관련 기법과의 관계를 정리한다.
**키워드**: `CRISP-DM`, `supervised-unsupervised`, `data-mining-tasks`, `business-understanding`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 2 (L:685)
비즈니스 문제를 데이터 마이닝 과제로 변환하는 체계적 접근을 제시한다. 핵심 데이터 마이닝 과제 유형으로 분류(classification: 이산 클래스 예측), 회귀(regression: 연속값 예측), 유사도 매칭(similarity matching), 클러스터링(clustering: 자연적 그룹 발견), 공출현 그룹화(co-occurrence: 장바구니 분석), 프로파일링(profiling: 일반적 행동 패턴 기술), 링크 예측(link prediction: 연결 관계 예측), 데이터 축소(data reduction), 인과 모델링(causal modeling)을 분류한다. 지도학습(labeled data로 학습)과 비지도학습(레이블 없이 패턴 발견)을 구분하며, 반지도학습과 능동학습도 소개한다. CRISP-DM(Cross-Industry Standard Process for Data Mining)의 6단계 프로세스를 상세히 설명한다: 비즈니스 이해 → 데이터 이해 → 데이터 준비 → 모델링 → 평가 → 배포. 데이터 마이닝 프로세스가 소프트웨어 개발 주기와 유사해 보이지만, 본질적으로 탐색적이고 연구에 가까우며, 결과의 불확실성이 높다는 점에서 다름을 강조한다. 통계(가설 검정, 신뢰 구간), 데이터베이스 쿼리(SQL 기반 선택적 검색), 데이터 웨어하우징(OLAP 큐브), 회귀 분석, 머신러닝, 텍스트 마이닝 등 관련 분석 기법과 데이터 마이닝의 관계를 정리한다.

### Ch 3: Introduction to Predictive Modeling (pp. 43-78)
**핵심**: 정보 이득(information gain)을 활용한 속성 선택과 트리 구조 모델을 통한 지도 세분화(supervised segmentation)를 설명한다. 엔트로피 기반 속성 선택 예제를 상세히 다루고, 결정 트리의 시각화와 규칙 집합으로의 변환을 보여준다. 고객 이탈 문제에 트리 유도를 적용하는 사례를 제시한다.
**키워드**: `information-gain`, `decision-tree`, `supervised-segmentation`, `entropy`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 3 (L:977)
상관관계에서 지도 세분화(supervised segmentation)로의 전환을 설명하며, 예측 모델링의 기초를 제시한다. 엔트로피(entropy)를 불확실성의 수학적 측정으로 도입하며, H = -Σ p(i) log₂ p(i) 공식으로 클래스 분포의 순수도를 측정한다. 정보 이득(information gain = 부모 엔트로피 - 가중 평균 자식 엔트로피)을 기준으로 데이터를 가장 효과적으로 분할하는 속성을 선택한다. 결정 트리 구축 과정을 상세히 설명하며, 재귀적 분할(recursive partitioning)로 각 노드에서 최적 속성을 선택하고 리프 노드에 도달할 때까지 반복한다. MegaTelCo 고객 이탈 사례에 트리 유도를 적용하여, 계약 기간, 통화량 변화, 데이터 사용량 등이 이탈 예측의 핵심 변수임을 발견한다. 결정 트리는 if-then 규칙 집합으로 변환 가능하며, 모델의 해석 가능성(interpretability)이 비즈니스 의사결정에서 핵심적 장점이다. 수치형 속성의 경우 최적 분할점(threshold)을 찾기 위해 모든 가능한 분할을 평가하며, 이진 분할과 다중 분할의 트레이드오프를 논의한다. 과적합(overfitting) 문제를 예고하며, 이를 다음 장에서 상세히 다룰 것임을 언급한다.

### Ch 4: Fitting a Model to Data (pp. 81-108)
**핵심**: 목적 함수·손실 함수의 개념과 데이터 기반 최적 모델 파라미터 탐색 과정을 설명한다. 선형 판별 함수, 로지스틱 회귀, 서포트 벡터 머신(SVM)을 예시 기법으로 다룬다. 비선형 함수, SVM 커널, 신경망으로의 확장을 소개하고, 로지스틱 회귀와 트리 유도의 비교 사례를 제시한다.
**키워드**: `objective-function`, `logistic-regression`, `SVM`, `linear-discriminant`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 4 (L:1366)
Ch 3의 트리 유도와 달리, 데이터에 수학적 함수를 적합(fitting)시키는 접근을 설명한다. 목적 함수(objective function)와 손실 함수(loss function)의 개념을 도입하며, 모델 학습이 목적 함수를 최적화하는 파라미터 탐색 과정임을 설명한다. 선형 판별 함수(linear discriminant)는 특성 공간에서 클래스를 분리하는 초평면을 찾으며, 가중합 f(x) = w₀ + w₁x₁ + w₂x₂로 표현된다. 로지스틱 회귀는 선형 판별의 출력을 시그모이드 함수로 변환하여 0-1 사이의 확률을 출력하며, 클래스 소속 확률(class-membership probability)을 제공한다. 서포트 벡터 머신(SVM)은 최대 마진(maximum margin) 초평면을 찾으며, 서포트 벡터(결정 경계에 가장 가까운 데이터 포인트)만이 경계를 결정한다. 비선형 문제를 위해 커널 트릭(kernel trick)으로 데이터를 고차원 공간으로 매핑하여 선형 분리가 가능하게 한다. 신경망의 기본 개념(퍼셉트론, 다층 네트워크, 역전파)을 간략히 소개하며, 비선형 함수 근사 능력을 설명한다. 로지스틱 회귀와 트리 유도의 비교를 MegaTelCo 이탈 사례로 수행하며, 각 기법의 장단점(해석 가능성 vs. 성능, 선형 vs. 비선형)을 분석한다.

### Ch 5: Overfitting and Its Avoidance (pp. 111-140)
**핵심**: 일반화(generalization) 개념과 과적합의 메커니즘을 트리 유도·수학적 함수 모두에서 분석한다. 홀드아웃 데이터와 적합 그래프를 통한 과적합 시각화, 교차 검증(cross-validation)으로의 발전을 설명한다. 학습 곡선(learning curve), 트리 가지치기, 정규화(regularization) 등 복잡도 제어 기법을 다룬다.
**키워드**: `overfitting`, `cross-validation`, `regularization`, `learning-curve`, `complexity-control`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 5 (L:1774)
과적합(overfitting)을 데이터 과학의 가장 중요한 개념 중 하나로 소개하며, 학습 데이터에서는 성능이 좋지만 새로운 데이터에서는 성능이 저하되는 현상을 설명한다. 일반화(generalization)란 학습에 사용하지 않은 데이터에 대해서도 정확한 예측을 할 수 있는 능력으로 정의한다. 트리 유도에서의 과적합을 예시하며, 완전히 성장한 트리가 학습 데이터의 노이즈까지 학습하여 일반화 성능이 떨어짐을 보여준다. 홀드아웃 데이터(holdout data)를 사용하여 모델의 일반화 성능을 추정하며, 학습/검증/테스트 세트의 역할과 분할 비율을 설명한다. 적합 그래프(fitting graph)는 x축에 모델 복잡도, y축에 학습/검증 성능을 그려 최적 복잡도를 시각적으로 식별하는 도구이다. 교차 검증(cross-validation, k-fold)은 데이터를 k개로 분할하여 k번 반복 학습/검증함으로써 홀드아웃 방법보다 안정적인 성능 추정을 제공한다. 학습 곡선(learning curve)은 학습 데이터 양에 따른 성능 변화를 보여주며, 더 많은 데이터가 과적합을 줄일 수 있는지 판단하는 데 사용한다. 복잡도 제어 기법으로 트리 가지치기(pruning: 일반화를 해치는 가지 제거), 정규화(regularization: L1/L2 패널티로 모델 복잡도 제어), 중간 정지(early stopping)를 다룬다. 중첩 교차 검증(nested cross-validation)으로 하이퍼파라미터 튜닝과 모델 평가를 동시에 수행하는 방법을 설명한다.

### Ch 6: Similarity, Neighbors, and Clusters (pp. 141-184)
**핵심**: 유사도·거리 개념을 정의하고 최근접 이웃(nearest-neighbor) 방법의 예측 모델링 적용을 설명한다. 위스키 분석 사례로 유사도 기반 추론을 보여주고, 이질적 속성·거리 함수 선택의 기술적 세부사항을 다룬다. 계층적 클러스터링과 중심점(centroid) 기반 클러스터링(k-means), 비즈니스 뉴스 클러스터링 사례를 포함한다.
**키워드**: `nearest-neighbor`, `clustering`, `k-means`, `similarity`, `distance-metrics`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 6 (L:2226)
유사도(similarity)와 거리(distance)의 개념을 정의하며, 유사한 개체는 유사한 특성을 가진다는 기본 원리를 설명한다. 위스키 분석 사례로 유사도 기반 추론을 보여주며, 단맛, 스모키함 등의 속성으로 위스키 간 유사도를 계산한다. 최근접 이웃(nearest-neighbor) 분류는 새로운 데이터 포인트의 레이블을 가장 가까운 k개 이웃의 다수결로 결정하며, k 값에 따라 결정 경계가 변한다. 거리 함수로 유클리드 거리, 맨해튼 거리, 코사인 유사도를 비교하며, 이질적 속성(수치+범주)의 거리 계산 문제를 다룬다. 속성 정규화(normalization)의 중요성을 설명하며, 스케일이 다른 속성이 거리 계산을 지배하는 문제를 방지한다. 클러스터링(clustering)은 비지도학습으로 데이터를 자연적 그룹으로 분할하며, 계층적 클러스터링(단일/완전/평균 연결)과 k-means의 두 가지 주요 접근을 설명한다. k-means는 초기 중심점 선택 → 할당 → 중심점 갱신을 수렴까지 반복하며, k 값 선택과 초기화 민감성이 과제이다. 비즈니스 뉴스 클러스터링 사례로 텍스트 데이터에 대한 클러스터링 적용을 보여주며, TF-IDF 벡터를 사용한 문서 유사도 계산을 설명한다.

### Ch 7: Decision Analytic Thinking I: What Is a Good Model? (pp. 187-207)
**핵심**: 데이터 과학 결과물에 대한 신중한 평가의 필요성을 강조하고, 기대값(expected value)을 핵심 평가 프레임워크로 제시한다. 혼동 행렬(confusion matrix), 불균형 클래스·불균등 비용/편익 문제를 분석한다. 기대 이익 계산, 베이스라인 성능 비교, 데이터 투자에 대한 시사점을 다룬다.
**키워드**: `expected-value`, `confusion-matrix`, `baseline`, `cost-benefit-analysis`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 7 (L:2810)
데이터 과학 결과물의 가치를 비즈니스 관점에서 평가하는 "의사결정 분석적 사고"(decision analytic thinking)를 도입한다. 혼동 행렬(confusion matrix)을 통해 TP, FP, TN, FN의 4가지 결과를 정의하고, 정확도(accuracy), 정밀도(precision), 재현율(recall), F1 점수를 도출한다. 불균형 클래스에서 전체 정확도가 오도적일 수 있음을 보여주며(99% 정상인 경우 "모두 정상" 예측이 99% 정확도), 비용/편익 분석의 필요성을 강조한다. 기대값(expected value) 프레임워크를 핵심 평가 도구로 제시하며, E[V] = Σ p(outcome_i) × V(outcome_i)로 모델 배포의 기대 이익을 계산한다. 비즈니스 비용/편익 행렬을 정의하여 각 예측 결과(TP/FP/TN/FN)의 비즈니스 가치를 명시적으로 할당한다. MegaTelCo 이탈 사례에서 고객 유지 제안의 비용(인센티브 비용)과 편익(고객 생애 가치)을 기대값으로 분석한다. 베이스라인(baseline) 모델과의 비교 중요성을 강조하며, "모두 긍정", "모두 부정", 랜덤 예측 등의 기본 베이스라인을 정의한다. 모델의 가치가 비용 구조에 따라 크게 달라지므로, 기술적 성능(정확도)과 비즈니스 가치(기대 이익)를 분리하여 평가해야 한다.

### Ch 8: Visualizing Model Performance (pp. 209-231)
**핵심**: 분류 대신 랭킹 관점에서 모델 성능을 시각화하는 기법을 다룬다. 이익 곡선(profit curve), ROC 그래프/곡선과 AUC, 누적 응답 곡선(cumulative response curve), 리프트 곡선(lift curve)을 설명한다. 고객 이탈 모델링의 성능 분석 사례를 통해 시각화 기법의 실무 적용을 보여준다.
**키워드**: `ROC-curve`, `AUC`, `profit-curve`, `lift-curve`, `cumulative-response`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 8 (L:3168)
모델 성능을 시각화하는 4가지 핵심 도구를 제시하며, 분류 결정 대신 랭킹(ranking) 관점에서 모델을 평가한다. 이익 곡선(profit curve)은 x축에 인구 비율(가장 높은 확률 순), y축에 누적 이익을 그려 최적 타겟팅 비율을 결정한다. ROC(Receiver Operating Characteristic) 그래프는 x축에 위양성률(FPR), y축에 진양성률(TPR)을 그리며, 왼쪽 상단에 가까울수록 좋은 모델이다. AUC(Area Under the ROC Curve)는 ROC 곡선 아래 면적으로, 0.5(랜덤 모델)에서 1.0(완벽한 모델) 사이의 값을 가지며, 임계값에 독립적인 모델 비교 지표이다. 누적 응답 곡선(cumulative response curve)은 상위 x%의 고객을 타겟팅했을 때 전체 양성 사례 중 몇 %를 포착하는지를 보여준다. 리프트 곡선(lift curve)은 랜덤 선택 대비 모델의 성능 향상 배수를 보여주며, 리프트 = (모델의 응답률) / (전체 응답률)로 계산한다. MegaTelCo 고객 이탈 모델에 이 4가지 시각화를 적용하여, 상위 20% 고객 타겟팅 시 약 45%의 이탈 고객을 포착할 수 있음을 보여준다. 여러 모델의 ROC 곡선을 중첩하여 비교하며, 비용 구조에 따라 최적 모델이 달라질 수 있음을 설명한다.

### Ch 9: Evidence and Probabilities (pp. 233-247)
**핵심**: 베이즈 정리(Bayes' Rule)를 활용한 명시적 증거 결합과 조건부 독립 가정 하의 확률적 추론을 설명한다. 나이브 베이즈 분류의 원리·장단점을 다루고, 증거 리프트(evidence lift) 모델을 소개한다. Facebook 좋아요 데이터의 증거 리프트, 온라인 광고 타겟팅 사례를 제시한다.
**키워드**: `Bayes-rule`, `naive-Bayes`, `evidence-lift`, `conditional-independence`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 9 (L:3588)
베이즈 정리(Bayes' Rule)를 활용한 명시적 증거 결합의 원리를 설명하며, P(A|B) = P(B|A) × P(A) / P(B) 공식의 비즈니스 적용을 다룬다. 사전 확률(prior probability), 우도(likelihood), 사후 확률(posterior probability)의 관계를 고객 이탈 예측 사례로 설명한다. 조건부 독립(conditional independence) 가정을 도입하며, 이 가정이 복잡한 확률 계산을 단순화하는 핵심 역할을 한다. 나이브 베이즈(Naive Bayes) 분류기는 모든 속성이 클래스에 대해 조건부 독립이라는 "순진한" 가정 하에 작동하며, 이 가정이 현실에서 위반되더라도 실무에서 놀라울 정도로 잘 작동한다. 나이브 베이즈의 장점(빠른 학습, 해석 가능성, 적은 데이터로도 작동)과 단점(독립 가정 위반 시 확률 추정의 부정확성)을 비교한다. 증거 리프트(evidence lift) 모델은 특정 증거가 사건의 확률을 얼마나 높이는지를 리프트 = P(A|B) / P(A)로 측정한다. Facebook 좋아요 데이터에서 특정 페이지 좋아요가 사용자 특성(성별, 정치 성향 등)을 예측하는 증거 리프트를 계산하는 사례를 제시한다. 온라인 광고 타겟팅에서 베이즈 추론과 증거 리프트를 활용하여 광고 클릭 확률을 높이는 실무 적용을 설명한다.

### Ch 10: Representing and Mining Text (pp. 249-275)
**핵심**: 텍스트의 중요성과 어려움을 설명하고, Bag of Words 표현, TF-IDF 계산, N-gram, 스테밍, 개체명 추출, 토픽 모델 등 텍스트 표현 기법을 다룬다. 재즈 뮤지션 사례로 TF-IDF를 실습하고, 뉴스 기사 마이닝을 통한 주가 예측 사례로 텍스트 마이닝의 실전 적용을 보여준다.
**키워드**: `TF-IDF`, `bag-of-words`, `topic-models`, `text-mining`, `N-gram`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 10 (L:4044)
비구조화 텍스트 데이터를 구조화된 표현으로 변환하는 과정을 설명하며, 웹의 80% 이상이 비구조화 텍스트임을 강조한다. Bag of Words(BoW) 표현은 텍스트를 단어 빈도 벡터로 변환하며, 단어 순서를 무시하지만 분류/클러스터링에 효과적이다. TF-IDF(Term Frequency-Inverse Document Frequency)는 TF(단어 빈도) × IDF(log(N/df), 희귀 단어에 높은 가중치)로 단어의 중요도를 측정한다. 재즈 뮤지션 사례에서 Miles Davis, John Coltrane 등의 Wikipedia 문서에 TF-IDF를 적용하여 각 뮤지션을 특징짓는 핵심 용어를 추출한다. N-gram은 연속된 N개 단어의 조합으로, 단어 순서 정보를 부분적으로 보존하며, bigram("New York"), trigram("New York City") 등이 유용하다. 스테밍(stemming)과 표제어 추출(lemmatization)은 단어의 변형을 기본형으로 통일하여 어휘 크기를 줄인다. 개체명 인식(NER: Named Entity Recognition)은 텍스트에서 인물, 장소, 조직 등을 자동 식별한다. 토픽 모델(LDA: Latent Dirichlet Allocation 등)은 문서 집합에서 잠재적 주제를 자동 발견하며, 각 문서를 주제의 혼합으로 표현한다. 뉴스 기사 텍스트 마이닝을 통한 주가 예측 사례로, 뉴스 감성과 주가 변동의 상관관계를 분석하는 실전 적용을 보여준다.

### Ch 11: Decision Analytic Thinking II: Toward Analytical Engineering (pp. 277-287)
**핵심**: 기대값 프레임워크를 활용한 데이터 과학 솔루션의 분석적 설계(analytical engineering)를 다룬다. 자선 우편물 타겟팅, 고객 이탈 문제의 인센티브 영향 평가 등 복잡한 비즈니스 문제를 기대값 분해로 구조화하고 데이터 과학 솔루션으로 전환하는 방법을 보여준다.
**키워드**: `analytical-engineering`, `expected-value-decomposition`, `selection-bias`, `incentive`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 11 (L:4637)
Ch 7의 기대값 프레임워크를 확장하여 복잡한 비즈니스 문제를 분석적으로 설계(analytical engineering)하는 방법을 제시한다. 기대값 분해(expected value decomposition)는 복잡한 의사결정을 구성 요소로 분해하여, 데이터 과학으로 추정할 수 있는 부분과 비즈니스 판단이 필요한 부분을 식별한다. 자선 우편물 타겟팅 사례에서 기부 확률 × 기대 기부금 - 우편 비용의 기대값을 계산하여 최적 타겟팅 전략을 도출한다. MegaTelCo 이탈 문제에서 인센티브의 인과적 효과를 분석하며, 인센티브가 이탈 확률에 미치는 영향(처치 효과)과 인센티브 없이도 남았을 고객에게 드는 불필요한 비용을 분리한다. 선택 편향(selection bias) 문제를 다루며, 관찰 데이터에서 인과적 결론을 도출할 때의 함정을 설명한다. 무작위 배정 실험(A/B 테스트)이 인과 관계 파악의 골드 스탠다드이지만, 비용과 윤리적 제약이 있을 때 준실험적(quasi-experimental) 방법을 대안으로 제시한다. 분석적 설계의 핵심은 비즈니스 문제 → 의사결정 구조 → 필요한 추정치 → 데이터 과학 태스크로의 체계적 변환이다.

### Ch 12: Other Data Science Tasks and Techniques (pp. 289-310)
**핵심**: 공출현·연관 규칙(리프트, 레버리지), 행동 프로파일링, 링크 예측, 데이터 축소, 잠재 정보 마이닝(영화 추천), 편향-분산 분해, 앙상블 방법, 데이터 기반 인과 추론 등 추가 기법을 소개한다. 맥주와 복권, Facebook 좋아요 연관 등 사례를 활용한다.
**키워드**: `association-rules`, `profiling`, `ensemble`, `bias-variance`, `causal-reasoning`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 12 (L:4940)
연관 규칙 마이닝(association rule mining)에서 지지도(support: 동시 출현 빈도), 신뢰도(confidence: 조건부 확률), 리프트(lift: 독립 가정 대비 초과 비율)의 3가지 측정 지표를 설명한다. "맥주와 기저귀" 전설과 실제 장바구니 분석 사례로 공출현 패턴의 비즈니스 가치를 보여준다. 행동 프로파일링(profiling)은 정상 행동의 패턴을 학습하여 이상치(anomaly)를 탐지하며, 사기 탐지에 핵심적이다. 링크 예측(link prediction)은 소셜 네트워크에서 미래 연결을 예측하며, 공통 이웃 수, Jaccard 계수, 선호적 연결(preferential attachment) 등의 지표를 사용한다. 잠재 정보 마이닝으로 행렬 분해(matrix factorization) 기반의 협업 필터링 추천 시스템을 설명하며, Netflix Prize를 사례로 든다. 편향-분산 분해(bias-variance decomposition)를 통해 모델 오류를 편향(체계적 오류)과 분산(불안정성)으로 분해하고, 이 두 요소의 트레이드오프를 설명한다. 앙상블 방법으로 배깅(bagging: 분산 감소, Random Forest), 부스팅(boosting: 편향 감소, AdaBoost/Gradient Boosting)을 다루며, 개별 모델보다 앙상블이 일반적으로 우수한 이유를 편향-분산 관점에서 분석한다. 데이터 기반 인과 추론에서 상관관계와 인과관계의 차이, Simpson의 역설, 교란 변수(confounding variable)의 위험을 설명한다.

### Ch 13: Data Science and Business Strategy (pp. 313-327)
**핵심**: 데이터 과학을 통한 경쟁 우위 확보와 지속 전략을 다룬다. 역사적 데이터 자산, 고유 지적 재산, 무형 부수 자산, 우수 데이터 과학자, 탁월한 관리 등 지속 가능한 차별화 요인을 분석한다. 데이터 과학 프로젝트 제안서 평가 방법과 기업의 데이터 과학 성숙도 모델을 제시한다.
**키워드**: `competitive-advantage`, `data-science-maturity`, `strategic-asset`, `talent-management`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 13 (L:5351)
데이터 과학이 기업 전략에서 경쟁 우위를 제공하는 메커니즘을 분석하며, 단순히 기술을 도입하는 것이 아니라 전략적으로 활용하는 것이 핵심이다. 지속 가능한 경쟁 우위의 5가지 원천을 제시한다: (1) 역사적 데이터 자산(경쟁사가 복제 불가), (2) 고유한 지적 재산(특허, 알고리즘), (3) 무형 부수 자산(브랜드, 네트워크 효과), (4) 우수한 데이터 과학자(인재 확보), (5) 탁월한 관리 능력. 데이터의 네트워크 효과를 설명하며, 더 많은 사용자 → 더 많은 데이터 → 더 좋은 모델 → 더 많은 사용자의 선순환 구조가 강력한 진입 장벽을 형성한다. 데이터 과학 프로젝트 제안서를 평가하는 체계적 방법을 제시하며, 비즈니스 가치, 기술적 타당성, 데이터 가용성, ROI 추정을 기준으로 평가한다. 데이터 과학 성숙도 모델을 5단계로 제시하며, 조직이 데이터 기반 의사결정 역량을 점진적으로 발전시키는 경로를 설명한다. 데이터 과학 팀 구성과 조직 내 위치(중앙 집중 vs. 분산), 비즈니스 리더와의 협업 모델을 다룬다.

### Ch 14: Conclusion (pp. 331-344)
**핵심**: 전체 기본 개념을 정리하고 모바일 디바이스 데이터 마이닝이라는 새로운 문제에 적용한다. 비즈니스 문제 해결에 대한 사고 방식의 전환, 인간 참여(human-in-the-loop)의 한계, 프라이버시·윤리 문제, 크라우드소싱에서 클라우드소싱으로의 전환을 다룬다.
**키워드**: `mobile-data`, `human-in-the-loop`, `privacy`, `ethics`, `crowd-sourcing`
**상세**: → `Provost-DataScienceBusiness_marker_full.md` Ch 14 (L:5738)
전체 책의 핵심 원리를 모바일 디바이스 데이터 마이닝이라는 새로운 문제에 적용하여 종합적으로 복습한다. 모바일 데이터의 특성(위치 정보, 앱 사용 패턴, 센서 데이터)이 새로운 비즈니스 기회를 창출함을 설명한다. 데이터 과학의 기본 원리를 12가지로 요약하며, 각 원리가 이 책의 어느 장에서 다뤄졌는지 매핑한다. 인간 참여(human-in-the-loop) 시스템의 장점(복잡한 판단, 예외 처리)과 한계(확장성, 일관성, 비용)를 분석한다. 프라이버시 문제를 심층적으로 다루며, 데이터 수집의 투명성, 익명화의 한계(재식별 위험), 차등 프라이버시(differential privacy)의 개념을 소개한다. 윤리적 고려사항으로 알고리즘 편향(protected class에 대한 차별), 공정성(fairness)의 다양한 정의, 모델의 사회적 영향을 다룬다. 크라우드소싱(crowdsourcing: 인간의 분산 작업)에서 클라우드소싱(cloudsourcing: 클라우드 기반 ML 서비스)으로의 전환을 설명하며, ML-as-a-Service의 등장과 의미를 논의한다.


### 기타 섹션 (Marker)

- What You Need to Know About Data Mining and Data-Analytic Thinking `L:11`
- The Ubiquity of Data Opportunities `L:519`
- Data Processing and "Big Data" `L:603`
- Data and Data Science Capability as a Strategic Asset `L:627`
- Data Mining and Data Science, Revisited `L:683`
- Business Problems and Data Science Solutions (p.42) `L:723`
- Data Mining and Its Results `L:805`
- Implications for Managing the Data Science Team `L:917`
- Other Analytics Techniques and Technologies `L:933`
- Introduction to Predictive Modeling: From Correlation to Supervised Segmentation (p.66) `L:1030`
- Trees as Sets of Rules (p.94) `L:1412`
- Fitting a Model to Data `L:1520`
- Example: Logistic Regression versus Tree Induction `L:1824`
- \* Example: Why Is Overfitting Bad? (p.147) `L:2077`
- Overfitting Avoidance and Complexity Control (p.156) `L:2176`
- Decision Analytic Thinking I: What Is a Good Model? (p.210) `L:3034`
- The Area Under the ROC Curve (AUC) `L:3524`
- Cumulative Response and Lift Curves `L:3532`
- Example: Performance Analytics for Churn Modeling (p.246) `L:3562`
- Applying Bayes' Rule to Data Science `L:3804`
- Example: Evidence Lifts from Facebook "Likes" `L:3921`
- \* The Relationship of IDF to Entropy (p.284) `L:4209`
- Decision Analytic Thinking II: Toward Analytical Engineering (p.300) `L:4448`
- Targeting the Best Prospects for a Charity Mailing `L:4460`
- Other Data Science Tasks and Techniques (p.312) `L:4628`
- Link Prediction and Social Recommendation `L:4835`
- Bias, Variance, and Ensemble Methods `L:4888`
- Data Science and Business Strategy (p.336) `L:4954`
- Achieving Competitive Advantage with Data Science `L:4976`
- Sustaining Competitive Advantage with Data Science `L:4988`
- Attracting and Nurturing Data Scientists and Their Teams `L:5047`
- Examine Data Science Case Studies `L:5073`
- Be Ready to Accept Creative Ideas from Any Source `L:5087`
- Be Ready to Evaluate Proposals for Data Science Projects `L:5091`
- The Fundamental Concepts of Data Science `L:5192`
- What Data Can't Do: Humans in the Loop, Revisited `L:5270`
- Privacy, Ethics, and Mining Data About Individuals `L:5304`
- Is There More to Data Science? `L:5322`
- Final Example: From Crowd-Sourcing to Cloud-Sourcing `L:5330`
