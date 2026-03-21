---
name: "Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications"
type: book-summary
source_file: "Huyen-DesigningMLSystems_full.md"
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

### Ch 1: Machine Learning Systems in Production (line 81)
**핵심**: ML 알고리즘은 ML 시스템의 일부에 불과하며 데이터 스택, 하드웨어 백엔드, 인터페이스, 배포·모니터링 인프라를 포함한 전체 시스템 관점이 필요하다. ML 적용의 적합 조건(학습 가능성, 복잡한 패턴, 기존 데이터, 예측 필요성)을 정의한다. 신뢰성·확장성·유지보수성·적응성의 4대 설계 원칙과 프로젝트 스코핑부터 배포까지의 반복적 개발 프로세스를 제시한다. 연구와 프로덕션 ML의 차이(속도 vs. 공정성, 최신 기술 vs. 검증된 기술)를 비교한다.
**키워드**: `ML-system-design`, `production-vs-research`, `iterative-process`, `scalability`
**상세**: → `Designing Machine Learning Systems_full.md` Ch 1 (line 81)

### Ch 2: Data Engineering Fundamentals (line 1654)
**핵심**: 데이터 형식(CSV, Parquet, Avro, Protobuf)의 특성과 row-major vs. column-major, 텍스트 vs. 바이너리 포맷의 장단점을 비교한다. 관계형·NoSQL·그래프 데이터 모델과 ETL vs. ELT 패턴을 설명한다. 트랜잭셔널 처리(OLTP)와 분석적 처리(OLAP)의 차이를 다루고, 배치 처리와 스트림 처리의 개념 및 상호 관계를 정리한다.
**키워드**: `data-formats`, `ETL`, `OLTP-OLAP`, `batch-vs-stream`, `data-models`
**상세**: → `Designing Machine Learning Systems_full.md` Ch 2 (line 1654)

### Ch 3: Training Data (line 3185)
**핵심**: 수동 레이블링, 자연 레이블(로그 기반), 약한 지도학습, 반지도학습, 전이학습, 액티브 러닝 등 다양한 레이블링 방법을 비교한다. 클래스 불균형 문제에 대해 데이터 수준(오버/언더샘플링, SMOTE), 알고리즘 수준(비용 민감 학습, focal loss)의 대응 전략을 제시한다. 데이터 증강(텍스트 역번역, 이미지 변환 등) 기법과 데이터의 비정상성 문제를 다룬다.
**키워드**: `labeling`, `class-imbalance`, `data-augmentation`, `weak-supervision`, `active-learning`
**상세**: → `Designing Machine Learning Systems_full.md` Ch 3 (line 3185)

### Ch 4: Feature Engineering (line 5128)
**핵심**: 수치형(정규화, 로그 변환, 버킷화), 범주형(원핫 인코딩, 임베딩, 해싱), 텍스트(TF-IDF, 임베딩) 등 피처 유형별 엔지니어링 기법을 다룬다. 피처 교차(feature crossing), 위치 임베딩 등 고급 기법을 설명한다. 피처 중요도 측정, 불필요한 피처 제거, 피처 스토어를 통한 학습-서빙 간 일관성 보장, 데이터 누수(data leakage) 방지를 강조한다.
**키워드**: `feature-crossing`, `feature-store`, `data-leakage`, `encoding`, `feature-importance`
**상세**: → `Designing Machine Learning Systems_full.md` Ch 4 (line 5128)

### Ch 5: Model Development (line 6321)
**핵심**: 가장 단순한 베이스라인(로지스틱 회귀, 규칙 기반)에서 시작하여 점진적으로 복잡도를 높이는 모델 선택 전략을 제시한다. 앙상블 방법(배깅, 부스팅, 스태킹)과 실험 추적(하이퍼파라미터, 메트릭, 아티팩트 기록)의 중요성을 설명한다. 모델 평가 시 오프라인 메트릭과 온라인 메트릭의 괴리를 인지하고 교차 검증, 섭동 테스트 등 견고한 평가 방법론을 다룬다.
**키워드**: `baseline`, `ensemble`, `experiment-tracking`, `model-evaluation`, `hyperparameter-tuning`
**상세**: → `Designing Machine Learning Systems_full.md` Ch 5 (line 6321)

### Ch 6: Model Deployment (line 9040)
**핵심**: 배치 예측(주기적 생성·저장)과 온라인 예측(실시간 서빙)의 패턴을 비교한다. 엣지 디바이스 배포, 모델 압축(양자화, 가지치기, 지식 증류)을 다룬다. 섀도우 배포, 카나리 릴리스, A/B 테스트, 블루-그린 배포 등 배포 전략을 설명한다. 학습 파이프라인과 서빙 파이프라인의 불일치(training-serving skew) 문제를 분석한다.
**키워드**: `batch-prediction`, `online-prediction`, `edge-deployment`, `canary-release`, `training-serving-skew`
**상세**: → `Designing Machine Learning Systems_full.md` Ch 6 (line 9040)

### Ch 7: Why Machine Learning Systems Fail in Production (line 10346)
**핵심**: 소프트웨어 시스템 장애와 ML 고유 장애를 구분하고, 데이터 분포 변화(공변량 변화, 레이블 변화, 개념 드리프트)를 상세히 분석한다. 퇴화 피드백 루프(추천 시스템 편향 강화)와 엣지 케이스(자율주행 등)의 위험을 설명한다. KS 검정, PSI 등 드리프트 탐지 통계 기법과 모니터링 전략을 제시하고, 지속적 학습(Continual Learning)의 필요성을 강조한다.
**키워드**: `data-distribution-shift`, `concept-drift`, `degenerate-feedback-loop`, `edge-cases`, `drift-detection`
**상세**: → `Designing Machine Learning Systems_full.md` Ch 7 (line 10346)
