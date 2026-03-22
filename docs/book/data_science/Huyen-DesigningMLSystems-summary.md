---
name: "Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications"
type: book-summary
authors: "Chip Huyen"
year: 2022
total_pages: 388
language: en
keywords: [ML-systems, production-ML, data-engineering, feature-engineering, model-deployment, monitoring, continual-learning, data-distribution-shift, training-data, MLOps]
---

# Designing Machine Learning Systems — Summary

> Chip Huyen (2022), 388 pages, 7 chapters (Early Release)
> ML 시스템의 설계·배포·운영 전 과정을 반복적 프로세스로 체계화한 실무 가이드이다.

## Contents

- Ch 1: Machine Learning Systems in Production
- Ch 2: Data Engineering Fundamentals
- Ch 3: Training Data
- Ch 4: Feature Engineering
- Ch 5: Model Development
- Ch 6: Model Deployment
- Ch 7: Why Machine Learning Systems Fail in Production
- About the Author

---

## Chapter Summaries

> Marker 원본: `Huyen-DesigningMLSystems_marker_full.md` | 총 ~5,313 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Machine Learning Systems in Production (line 81)
**핵심**: ML 알고리즘은 ML 시스템의 일부에 불과하며 데이터 스택, 하드웨어 백엔드, 인터페이스, 배포·모니터링 인프라를 포함한 전체 시스템 관점이 필요하다. ML 적용의 적합 조건(학습 가능성, 복잡한 패턴, 기존 데이터, 예측 필요성)을 정의한다. 신뢰성·확장성·유지보수성·적응성의 4대 설계 원칙과 프로젝트 스코핑부터 배포까지의 반복적 개발 프로세스를 제시한다. 연구와 프로덕션 ML의 차이(속도 vs. 공정성, 최신 기술 vs. 검증된 기술)를 비교한다.
**키워드**: `ML-system-design`, `production-vs-research`, `iterative-process`, `scalability`
**상세**: → `Huyen-DesigningMLSystems_marker_full.md` Ch 1 (L:67)
ML 시스템은 ML 알고리즘 외에도 인터페이스, 데이터 스택, 하드웨어 백엔드, 배포·모니터링 인프라를 포함하는 복합 시스템이다. ML 적용의 6가지 조건을 정의한다: (1) 학습 가능성, (2) 복잡한 패턴, (3) 패턴의 존재, (4) 기존 데이터 확보, (5) 예측 문제로 프레이밍 가능, (6) 미래 데이터가 학습 데이터와 유사한 분포. ML이 특히 빛나는 추가 조건으로 반복적 태스크, 잘못된 예측 비용이 낮은 경우, 대규모 처리가 필요한 경우를 제시한다. 연구 ML과 프로덕션 ML의 핵심 차이를 비교한다: 연구는 SOTA 달성과 빠른 학습이 목표인 반면, 프로덕션은 공정성, 해석 가능성, 지연시간 등 다양한 이해관계자의 요구사항을 충족해야 한다. ML 시스템 설계의 4대 원칙으로 신뢰성(reliability), 확장성(scalability), 유지보수성(maintainability), 적응성(adaptability)을 제시한다. 전통적 소프트웨어와 ML 시스템의 차이를 설명하며, ML 코드는 전체 시스템의 작은 부분에 불과하고 데이터 의존성이 핵심 복잡성을 만든다. 반복적 ML 개발 프로세스는 프로젝트 스코핑 → 데이터 엔지니어링 → ML 모델 개발 → 배포 → 모니터링 및 지속적 학습의 단계로 구성된다. Google Translate의 신경망 번역 도입(2016)을 사례로 ML의 프로덕션 적용 성공 사례를 소개하며, 그 이후 ML이 정보 접근, 커뮤니케이션, 업무 방식 등 삶의 거의 모든 측면에 영향을 미치게 되었음을 설명한다.

**Marker 세부 목차** (`Huyen-DesigningMLSystems_marker_full.md`):
- Chapter 1. Machine Learning Systems in Production `L:67`
- 1. Learn: the system has the capacity to learn `L:119`
- 1. It's repetitive `L:169`
- 1. Avoid the state-of-the-art trap `L:2691`


### Ch 2: Data Engineering Fundamentals (line 1654)
**핵심**: 데이터 형식(CSV, Parquet, Avro, Protobuf)의 특성과 row-major vs. column-major, 텍스트 vs. 바이너리 포맷의 장단점을 비교한다. 관계형·NoSQL·그래프 데이터 모델과 ETL vs. ELT 패턴을 설명한다. 트랜잭셔널 처리(OLTP)와 분석적 처리(OLAP)의 차이를 다루고, 배치 처리와 스트림 처리의 개념 및 상호 관계를 정리한다.
**키워드**: `data-formats`, `ETL`, `OLTP-OLAP`, `batch-vs-stream`, `data-models`
**상세**: → `Huyen-DesigningMLSystems_marker_full.md` Ch 2 (L:726)
ML 시스템의 데이터 엔지니어링 기초를 다루며, 데이터 소스부터 처리 패턴까지 전반을 설명한다. 데이터 소스를 4가지로 분류한다: 사용자 입력 데이터(형식 오류 가능성 높음, 빠른 처리 필요), 시스템 생성 데이터(로그, 모델 예측값), 내부 데이터베이스(자산 관리), 서드파티 데이터(개인정보 우려). 데이터 직렬화 형식으로 JSON, CSV(텍스트 기반, 사람 읽기 가능), Parquet, Avro, Protobuf, Pickle(바이너리 기반, 효율적)을 비교하며, row-major(접근 빈번) vs. column-major(분석 최적화) 저장 방식의 차이를 설명한다. 데이터 모델로 관계형(정규화, ACID), NoSQL(문서형-MongoDB, 그래프형-Neo4j), 구조화 vs. 비구조화 데이터를 비교한다. 데이터 저장 엔진을 OLTP(트랜잭션 처리, 낮은 지연시간)와 OLAP(분석 처리, 대규모 집계)로 구분하며, 각각의 최적화 방향이 다름을 설명한다. ETL(Extract-Transform-Load)과 ELT(Extract-Load-Transform)의 차이를 다루며, ELT가 클라우드 스토리지 비용 감소로 인기를 얻고 있음을 설명한다. 데이터 전달 방식으로 DB를 통한 전달, 서비스 간 REST/RPC, 실시간 전송(Apache Kafka, Amazon Kinesis)을 비교한다. 배치 처리(MapReduce, Spark)와 스트림 처리(Apache Flink, KSQL)의 차이를 설명하며, 스트림 처리가 더 유연하고 배치 처리를 포함할 수 있지만 구현 복잡도가 높다고 분석한다.

**Marker 세부 목차** (`Huyen-DesigningMLSystems_marker_full.md`):
- 2. The cost of wrong predictions is cheap `L:173`
- Chapter 2. Data Engineering Fundamentals `L:726`
- 2. Start with the simplest models `L:2701`
- 2. Overfit a single batch `L:3084`
- 2. Simple heuristic `L:3507`


### Ch 3: Training Data (line 3185)
**핵심**: 수동 레이블링, 자연 레이블(로그 기반), 약한 지도학습, 반지도학습, 전이학습, 액티브 러닝 등 다양한 레이블링 방법을 비교한다. 클래스 불균형 문제에 대해 데이터 수준(오버/언더샘플링, SMOTE), 알고리즘 수준(비용 민감 학습, focal loss)의 대응 전략을 제시한다. 데이터 증강(텍스트 역번역, 이미지 변환 등) 기법과 데이터의 비정상성 문제를 다룬다.
**키워드**: `labeling`, `class-imbalance`, `data-augmentation`, `weak-supervision`, `active-learning`
**상세**: → `Huyen-DesigningMLSystems_marker_full.md` Ch 3 (L:1339)
학습 데이터의 생성과 관리에 대한 실무적 접근을 다루며, 데이터가 ML 시스템의 Kraken과 같다고 비유한다. 샘플링 방법을 비확률적(편의, 눈덩이, 판단, 할당) 방법과 확률적(단순 랜덤, 층화, 가중치, 저수지) 방법으로 분류하며, 각각의 편향과 적합한 사용 사례를 분석한다. 레이블링 전략으로 수동 레이블링(비용↑, 데이터 프라이버시 문제), 자연 레이블(사용자 피드백으로 자동 생성, 추천 시스템에 적합), 약한 지도학습(labeling function 기반, Snorkel), 반지도학습(self-training, 의사 레이블), 전이학습, 액티브 러닝(불확실한 샘플 우선 레이블링)을 비교한다. 클래스 불균형 문제에 대해 데이터 수준 접근(오버샘플링-SMOTE, 언더샘플링-Tomek links, 2단계 학습)과 알고리즘 수준 접근(비용 민감 학습-클래스별 가중치 조절, focal loss-어려운 샘플에 집중)을 제시한다. 데이터 증강 기법으로 컴퓨터 비전(랜덤 자르기, 뒤집기, 색상 변환, CutMix, MixUp), NLP(역번역, 토큰 교체, 템플릿 기반 생성)를 다루며, perturbation invariance(변형에도 레이블 유지)와 PERT(가능한 모든 변형에 대한 일관된 예측)의 원칙을 설명한다. 데이터의 비정상성(non-stationarity) 문제를 소개하며, 시간에 따라 데이터 분포가 변화할 수 있음을 경고한다.

**Marker 세부 목차** (`Huyen-DesigningMLSystems_marker_full.md`):
- 3. Patterns: there are patterns to learn `L:135`
- 3. It's at scale `L:179`
- Chapter 3. Training Data `L:1339`
- 3. Avoid human biases in selecting models `L:2709`


### Ch 4: Feature Engineering (line 5128)
**핵심**: 수치형(정규화, 로그 변환, 버킷화), 범주형(원핫 인코딩, 임베딩, 해싱), 텍스트(TF-IDF, 임베딩) 등 피처 유형별 엔지니어링 기법을 다룬다. 피처 교차(feature crossing), 위치 임베딩 등 고급 기법을 설명한다. 피처 중요도 측정, 불필요한 피처 제거, 피처 스토어를 통한 학습-서빙 간 일관성 보장, 데이터 누수(data leakage) 방지를 강조한다.
**키워드**: `feature-crossing`, `feature-store`, `data-leakage`, `encoding`, `feature-importance`
**상세**: → `Huyen-DesigningMLSystems_marker_full.md` Ch 4 (L:2021)
Facebook의 2014년 논문을 인용하며, 올바른 피처가 알고리즘 기법보다 ML 모델 성능에 더 큰 영향을 미친다고 강조한다. 딥러닝이 피처 학습을 자동화했지만, 텍스트/이미지 외 구조화된 데이터에서는 여전히 수작업 피처 엔지니어링이 필요하다. 수치형 피처 처리로 정규화(min-max, z-score), 로그 변환(왜곡 분포 처리), 이산화/버킷화(연속값을 구간으로 분할)를 설명한다. 범주형 피처는 원핫 인코딩(희소, 고차원), 임베딩(학습 기반, 저차원 밀집 표현), 해싱 트릭(고정 크기 벡터, 충돌 가능성 있지만 메모리 효율적)으로 처리한다. 피처 교차(feature crossing)는 두 개 이상의 피처를 결합하여 비선형 관계를 모델이 학습 가능한 선형 특성으로 변환하며, 추천 시스템에서 사용자 × 아이템 상호작용 모델링에 핵심적이다. 데이터 누수(data leakage)를 상세히 다루며, 학습 시에는 사용 가능하지만 서빙 시에는 존재하지 않는 정보가 피처로 포함되는 문제를 설명한다. 누수의 원인으로 시간순 미분할(미래 정보 유출), 과도한 전처리(검증 데이터에 학습 데이터 통계 적용), 피처 복제(타겟 변수와 상관 높은 파생 변수), 그룹 간 유출을 분류한다. 피처 중요도 측정 방법으로 모델 내장(XGBoost feature importance), 순열 중요도(피처 값 섞어서 성능 변화 측정), SHAP 값을 소개한다. 피처 일반화를 위해 학습-서빙 간 일관성을 보장하는 피처 스토어(Feast, Tecton)의 역할과 아키텍처를 설명한다. 불필요한 피처 제거 기준으로 커버리지(결측률), 상관성(타겟과의 관련성), 모델 성능 기여도를 제시한다.

**Marker 세부 목차** (`Huyen-DesigningMLSystems_marker_full.md`):
- Chapter 4. Feature Engineering `L:2021`


### Ch 5: Model Development (line 6321)
**핵심**: 가장 단순한 베이스라인(로지스틱 회귀, 규칙 기반)에서 시작하여 점진적으로 복잡도를 높이는 모델 선택 전략을 제시한다. 앙상블 방법(배깅, 부스팅, 스태킹)과 실험 추적(하이퍼파라미터, 메트릭, 아티팩트 기록)의 중요성을 설명한다. 모델 평가 시 오프라인 메트릭과 온라인 메트릭의 괴리를 인지하고 교차 검증, 섭동 테스트 등 견고한 평가 방법론을 다룬다.
**키워드**: `baseline`, `ensemble`, `experiment-tracking`, `model-evaluation`, `hyperparameter-tuning`
**상세**: → `Huyen-DesigningMLSystems_marker_full.md` Ch 5 (L:2497)
ML 문제를 프레이밍하는 것부터 시작하며, 비즈니스 문제(예: 고객 서비스 속도 향상)를 ML 문제(요청 분류)로 변환하는 과정을 설명한다. ML 태스크 유형을 분류(이진, 다중 클래스, 다중 레이블)와 회귀로 구분하며, 높은 카디널리티(수천 클래스)의 경우 계층적 분류를 제안한다. 동일 문제를 여러 방식으로 프레이밍할 수 있으며(분류 vs. 회귀, 다중 레이블 vs. 다중 이진 분류), 프레이밍에 따라 난이도가 크게 달라진다. 목적 함수(objective function)를 분리하여 ML 목적함수(최적화 가능)와 비즈니스 목적함수(실제 목표) 간의 괴리를 인지하고 조율해야 한다. 모델 선택 시 가장 단순한 베이스라인(로지스틱 회귀, 규칙 기반)에서 시작하여 점진적으로 복잡도를 높이며, "state-of-the-art trap"(최신 모델에 대한 과도한 집착)을 경계한다. 앙상블 방법으로 배깅(분산 감소), 부스팅(편향 감소), 스태킹(메타 학습기)을 다루며, 프로덕션에서 앙상블이 유용하지만 레이턴시와 유지보수 비용 증가를 주의해야 한다. 실험 추적(MLflow, Weights & Biases)과 버저닝(데이터, 모델, 코드)의 중요성을 강조하며, 재현 가능성이 ML 디버깅의 핵심이다. 분산 학습(데이터 병렬, 모델 병렬)과 AutoML(하이퍼파라미터 튜닝-random search/Bayesian opt, 아키텍처 탐색-NAS)을 소개한다. 오프라인 평가에서 교차 검증, 섭동 테스트, 슬라이스 분석(특정 하위 그룹별 성능 확인)의 중요성을 다루며, 오프라인 메트릭과 온라인 메트릭 간 괴리가 흔함을 경고한다.

**Marker 세부 목차** (`Huyen-DesigningMLSystems_marker_full.md`):
- Chapter 5. Model Development `L:2497`
- 5. Existing solutions `L:3521`


### Ch 6: Model Deployment (line 9040)
**핵심**: 배치 예측(주기적 생성·저장)과 온라인 예측(실시간 서빙)의 패턴을 비교한다. 엣지 디바이스 배포, 모델 압축(양자화, 가지치기, 지식 증류)을 다룬다. 섀도우 배포, 카나리 릴리스, A/B 테스트, 블루-그린 배포 등 배포 전략을 설명한다. 학습 파이프라인과 서빙 파이프라인의 불일치(training-serving skew) 문제를 분석한다.
**키워드**: `batch-prediction`, `online-prediction`, `edge-deployment`, `canary-release`, `training-serving-skew`
**상세**: → `Huyen-DesigningMLSystems_marker_full.md` Ch 6 (L:4155)
ML 모델 배포의 일반적인 미신 4가지를 먼저 반박한다: (1) 한두 개 모델만 배포(실제로 Uber는 수천 개), (2) 방치해도 성능 유지(실제로 concept drift로 퇴화), (3) 자주 업데이트 불필요(실제로 빈번한 재학습 필요), (4) 복잡한 인프라 불필요. 배치 예측은 주기적으로 예측을 생성하여 저장해두고 서빙하는 방식으로, 레이턴시 요구가 낮은 추천 시스템 등에 적합하며 구현이 단순하지만 새로운 입력에 대한 적응이 느리다. 온라인 예측(실시간 추론)은 요청 즉시 예측을 생성하며, 요청-응답 방식과 이벤트 기반 스트리밍 방식이 있고, 레이턴시가 중요한 사기 탐지 등에 필수적이다. 엣지 디바이스 배포는 모바일·IoT 기기에서 직접 추론하여 네트워크 지연 제거와 프라이버시 보호를 제공하지만, 제한된 연산 자원과 메모리가 과제이다. 모델 압축 기법으로 양자화(32비트→8비트/4비트 축소, 최대 4배 메모리 감소), 가지치기(불필요한 파라미터 제거), 지식 증류(큰 teacher 모델의 지식을 작은 student 모델로 전달)를 설명한다. 모델 최적화로 TensorRT, TVM 등 추론 엔진이 연산 그래프 최적화(연산 융합, 불필요 연산 제거)를 수행하는 과정을 다룬다. 배포 전략으로 섀도우 배포(신모델을 병렬 실행하되 결과 비교만), 카나리 릴리스(소수 트래픽으로 점진적 전환), A/B 테스트(통계적 유의성 기반 비교), 블루-그린 배포(즉시 전환 가능한 두 환경 유지)를 비교한다. 학습-서빙 불일치(training-serving skew)를 상세히 분석하며, 피처 전처리 차이, 배치 추론과 실시간 추론의 차이가 주요 원인이다. 모델 내보내기 형식으로 TensorFlow SavedModel, ONNX, TorchScript 등을 소개한다.

**Marker 세부 목차** (`Huyen-DesigningMLSystems_marker_full.md`):
- 6. Unseen data: Unseen data shares patterns with the training data `L:161`
- 6. Understand your model's assumptions `L:2745`
- Chapter 6. Model Deployment `L:4155`


### Ch 7: Why Machine Learning Systems Fail in Production (line 10346)
**핵심**: 소프트웨어 시스템 장애와 ML 고유 장애를 구분하고, 데이터 분포 변화(공변량 변화, 레이블 변화, 개념 드리프트)를 상세히 분석한다. 퇴화 피드백 루프(추천 시스템 편향 강화)와 엣지 케이스(자율주행 등)의 위험을 설명한다. KS 검정, PSI 등 드리프트 탐지 통계 기법과 모니터링 전략을 제시하고, 지속적 학습(Continual Learning)의 필요성을 강조한다.
**키워드**: `data-distribution-shift`, `concept-drift`, `degenerate-feedback-loop`, `edge-cases`, `drift-detection`
**상세**: → `Huyen-DesigningMLSystems_marker_full.md` Ch 7 (L:4854)
식료품 수요 예측 모델의 실패 사례로 시작하며, 배포 후 모델 성능이 시간이 지남에 따라 퇴화하는 현실을 보여준다. ML 시스템 장애를 운영 기대(레이턴시, 처처량)와 ML 성능 기대(정확도)로 구분하며, ML 성능 장애는 조용히 발생하여 탐지가 어렵다. Google의 96건 ML 파이프라인 장애 분석 결과, 60건(62.5%)이 ML과 직접 관련 없는 소프트웨어 엔지니어링 문제(의존성 장애, 배포 오류, 하드웨어 고장 등)였다. 자연 레이블(natural labels)은 시스템이 자동으로 수집 가능한 피드백으로, 추천 시스템의 클릭/비클릭이 대표적이며, 피드백 루프 길이(수 분~수 개월)가 모니터링 전략을 좌우한다. 데이터 분포 변화(data distribution shift)를 P(X), P(Y|X), P(X|Y), P(Y)의 변화로 수학적으로 정의하고, 공변량 변화(covariate shift: P(X) 변화), 레이블 변화(label shift: P(Y) 변화), 개념 드리프트(concept drift: P(Y|X) 변화)를 구분한다. 개념 드리프트가 가장 위험한 유형으로, 같은 입력에 대한 정답 자체가 변하는 경우(예: 코로나 이전 vs. 이후의 소비 패턴)를 설명한다. 퇴화 피드백 루프(degenerate feedback loop)는 모델의 예측이 미래 학습 데이터에 영향을 미쳐 편향이 강화되는 현상으로, 추천 시스템에서 인기 편향(popularity bias)이 대표적이다. 엣지 케이스는 모델이 극단적으로 잘못된 예측을 하는 드문 경우로, 자율주행의 안전 관련 실패가 대표 사례이며, outlier(데이터 관점)와 edge case(성능 관점)를 구분한다. 드리프트 탐지를 위해 KS 검정(Kolmogorov-Smirnov test), PSI(Population Stability Index) 등 통계적 방법과 시간 윈도우 기반 비교를 사용하며, 차원이 높은 데이터에서는 차원 축소 후 적용한다. 지속적 학습(continual learning)의 필요성을 강조하며, 정적 모델은 프로덕션에서 점진적으로 성능이 저하될 수밖에 없음을 결론짓는다.

**Marker 세부 목차** (`Huyen-DesigningMLSystems_marker_full.md`):
- Chapter 7. Why Machine Learning Systems Fail in Production `L:4854`



### 기타 섹션 (Marker)

- When to Use Machine Learning `L:107`
- THE DATA SCIENCE HIERARCHY OF NEEDS `L:273`
- Machine learning in research vs. in production `L:313`
- Machine learning systems vs. traditional software `L:533`
- Designing ML Systems in Production (p.41) `L:561`
- Step 3. ML model development `L:652`
- Step 5. Monitoring and continual learning `L:660`
- Data Storage Engines and Processing `L:1118`
- Batch Processing vs. Stream Processing `L:1272`
- Learned Features vs. Engineered Features `L:2037`
- Multiple Ways to Frame a Problem `L:2563`
- Six tips for model selection `L:2687`
- Hard AutoML: Architecture search and learned optimizer `L:3184`
- FOUR PHASES OF ML MODEL DEVELOPMENT `L:3210`
- Phase 3. Optimizing simple models `L:3234`
- Unifying Batch Pipeline And Streaming Pipeline `L:4455`
- ML on the Cloud and on the Edge `L:4551`
- Compiling and Optimizing Models for Edge Devices `L:4612`
- Using ML to optimize ML models `L:4759`
- Natural Labels and Feedback Loop `L:4874`
