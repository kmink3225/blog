# Data Science — Book Guide

이 디렉토리의 교재 소스를 빠르게 탐색하기 위한 가이드.

## 소스 파일 목록

### Huyen-AIEngineering
| 파일 | 변환 도구 |
|---|---|
| Huyen-AIEngineering-summary.md | 요약 |
| Huyen-AIEngineering_marker_full.md | Marker |

### Huyen-DesigningMLSystems
| 파일 | 변환 도구 |
|---|---|
| Huyen-DesigningMLSystems-summary.md | 요약 |
| Huyen-DesigningMLSystems_marker_full.md | Marker |

### Provost-DataScienceBusiness
| 파일 | 변환 도구 |
|---|---|
| Provost-DataScienceBusiness-summary.md | 요약 |
| Provost-DataScienceBusiness_marker_full.md | Marker |

## 챕터 목차 (Marker 기준)

> `L:숫자`는 원본 md 파일의 라인 번호. `Read(file, offset=L, limit=N)`으로 해당 구간을 직접 읽을 수 있음.

### Huyen-AIEngineering
- **파일**: `Huyen-AIEngineering_marker_full.md`
- **총 라인 수**: ~9,884
- **주요 섹션** (3개):
  - Introduction to Building AI Applications with Foundation Models (p.24) `L:520`
  - Challenges of Evaluating Foundation Models `L:2389`
  - AI Engineering Architecture and User Feedback (p.472) `L:8517`

### Huyen-DesigningMLSystems
- **파일**: `Huyen-DesigningMLSystems_marker_full.md`
- **총 라인 수**: ~5,313
- **주요 섹션** (40개):
- Chapter 1. Machine Learning Systems in Production `L:67`
  - When to Use Machine Learning `L:107`
  - 1. Learn: the system has the capacity to learn `L:119`
  - 3. Patterns: there are patterns to learn `L:135`
  - 6. Unseen data: Unseen data shares patterns with the training data `L:161`
  - 1. It's repetitive `L:169`
  - 2. The cost of wrong predictions is cheap `L:173`
  - 3. It's at scale `L:179`
- THE DATA SCIENCE HIERARCHY OF NEEDS `L:273`
  - Machine learning in research vs. in production `L:313`
  - Machine learning systems vs. traditional software `L:533`
  - Designing ML Systems in Production (p.41) `L:561`
  - Step 3. ML model development `L:652`
  - Step 5. Monitoring and continual learning `L:660`
- Chapter 2. Data Engineering Fundamentals `L:726`
  - Data Storage Engines and Processing `L:1118`
  - Batch Processing vs. Stream Processing `L:1272`
  - Chapter 3. Training Data `L:1339`
  - Chapter 4. Feature Engineering `L:2021`
  - Learned Features vs. Engineered Features `L:2037`
- Chapter 5. Model Development `L:2497`
  - Multiple Ways to Frame a Problem `L:2563`
  - Six tips for model selection `L:2687`
  - 1. Avoid the state-of-the-art trap `L:2691`
  - 2. Start with the simplest models `L:2701`
  - 3. Avoid human biases in selecting models `L:2709`
  - 6. Understand your model's assumptions `L:2745`
  - 2. Overfit a single batch `L:3084`
  - Hard AutoML: Architecture search and learned optimizer `L:3184`
  - FOUR PHASES OF ML MODEL DEVELOPMENT `L:3210`
  - Phase 3. Optimizing simple models `L:3234`
  - 2. Simple heuristic `L:3507`
  - 5. Existing solutions `L:3521`
- Chapter 6. Model Deployment `L:4155`
  - Unifying Batch Pipeline And Streaming Pipeline `L:4455`
  - ML on the Cloud and on the Edge `L:4551`
  - Compiling and Optimizing Models for Edge Devices `L:4612`
  - Using ML to optimize ML models `L:4759`
- Chapter 7. Why Machine Learning Systems Fail in Production `L:4854`
  - Natural Labels and Feedback Loop `L:4874`

### Provost-DataScienceBusiness
- **파일**: `Provost-DataScienceBusiness_marker_full.md`
- **총 라인 수**: ~6,602
- **주요 섹션** (42개):
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
- A Key Analytical Framework: Expected Value `L:3142`
- The Area Under the ROC Curve (AUC) `L:3524`
- Cumulative Response and Lift Curves `L:3532`
- Example: Performance Analytics for Churn Modeling (p.246) `L:3562`
- Applying Bayes' Rule to Data Science `L:3804`
- A Model of Evidence "Lift" (p.267) `L:3895`
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
- A Firm's Data Science Maturity `L:5150`
- The Fundamental Concepts of Data Science `L:5192`
- What Data Can't Do: Humans in the Loop, Revisited `L:5270`
- Privacy, Ethics, and Mining Data About Individuals `L:5304`
- Is There More to Data Science? `L:5322`
- Final Example: From Crowd-Sourcing to Cloud-Sourcing `L:5330`
