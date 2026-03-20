---
name: "Behavioral Data Analysis with R and Python"
type: book-summary
source_file: "Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md"
authors: "Florent Buisson"
year: 2021
total_pages: 321
language: en
keywords: [behavioral data analysis, causal diagram, A/B testing, experimental design, confounding, missing data, bootstrap, moderation, mediation, instrumental variable]
---

# Behavioral Data Analysis with R and Python — Summary

> Florent Buisson (2021), 321 pages, 12 chapters
> 행동 데이터 분석을 위한 인과 다이어그램과 실험 설계를 비즈니스 실무 관점에서 R과 Python 코드와 함께 소개하는 실용서

## Contents

**Part I. Understanding Behaviors**
1. The Causal-Behavioral Framework for Data Analysis (p.3)
2. Understanding Behavioral Data (p.19)

**Part II. Causal Diagrams and Deconfounding**
3. Introduction to Causal Diagrams (p.39)
4. Building Causal Diagrams from Scratch (p.63)
5. Using Causal Diagrams to Deconfound Data Analyses (p.91)

**Part III. Robust Data Analysis**
6. Handling Missing Data (p.107)
7. Measuring Uncertainty with the Bootstrap (p.147)

**Part IV. Designing and Analyzing Experiments**
8. Experimental Design: The Basics (p.173)
9. Stratified Randomization (p.203)
10. Cluster Randomization and Hierarchical Modeling (p.233)

**Part V. Advanced Tools in Behavioral Data Analysis**
11. Introduction to Moderation (p.257)
12. Mediation and Instrumental Variables (p.297)

---

## Chapter Summaries

### Ch 1: The Causal-Behavioral Framework for Data Analysis (pp. 3-18)

**핵심**: 인과 분석(causal analytics)이 인간 행동 설명에 왜 필요한지를 설명한다. 상관이 인과가 아닌 이유를 교란 변수(confounder)의 실제 사례로 보여주며, 변수를 무분별하게 추가하면 오히려 편향이 증가할 수 있음을 시연한다.

**키워드**: `causal analytics`, `confounder`, `behavioral framework`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 1 (line 1545)

### Ch 2: Understanding Behavioral Data (pp. 19-35)

**핵심**: 인간 행동의 기본 모형(개인 특성, 인지/감정, 의도, 행동)을 제시하고, 행동 데이터와의 연결 방법을 다룬다. 행동적 무결성(behavioral integrity) 마인드셋과 데이터 검증 방법을 소개한다.

**키워드**: `behavioral model`, `personal characteristics`, `cognition`, `behavioral integrity`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 2 (line 2452)

### Ch 3: Introduction to Causal Diagrams (pp. 39-61)

**핵심**: 인과 다이어그램의 기본 구조(chain, fork, collider)를 소개한다. 변수의 분할/집계, 순환(cycle), 경로(path) 개념을 다루며, 인과 다이어그램이 행동과 데이터를 동시에 표현하는 방법을 설명한다.

**키워드**: `causal diagram`, `chain`, `fork`, `collider`, `path`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 3 (line 3363)

### Ch 4: Building Causal Diagrams from Scratch (pp. 63-90)

**핵심**: 비즈니스 문제에서 출발하여 인과 다이어그램을 단계적으로 구축하는 방법을 다룬다. 관심 관계 파악, 후보 변수 식별, 데이터 기반 검증, 반복적 확장 및 단순화 과정을 실습한다.

**키워드**: `diagram construction`, `variable selection`, `iterative refinement`, `proxy variable`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 4 (line 4672)

### Ch 5: Using Causal Diagrams to Deconfound Data Analyses (pp. 91-103)

**핵심**: 분리적 원인 기준(disjunctive cause criterion)과 백도어 기준(backdoor criterion)을 이용한 교란 제거 방법을 설명한다. 아이스크림과 생수 판매 사례를 통해 두 기준의 적용을 시연한다.

**키워드**: `deconfounding`, `disjunctive cause criterion`, `backdoor criterion`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 5 (line 6437)

### Ch 6: Handling Missing Data (pp. 107-146)

**핵심**: 결측 데이터의 시각화, 진단(MCAR/MAR/MNAR), 그리고 다중 대체(multiple imputation) 기법을 다룬다. PMM, 정규분포 대체, 보조 변수 추가, 대체 데이터셋 수 결정 등 실무적 방법을 R과 Python으로 구현한다.

**키워드**: `missing data`, `MCAR`, `MAR`, `MNAR`, `multiple imputation`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 6 (line 7171)

### Ch 7: Measuring Uncertainty with the Bootstrap (pp. 147-169)

**핵심**: 부트스트랩의 원리와 신뢰구간 구성 방법을 소개한다. 표본 평균, 임의 통계량, 회귀분석에 대한 부트스트랩 적용과 전통적 방법 대비 부트스트랩의 장단점을 다룬다.

**키워드**: `bootstrap`, `confidence interval`, `resampling`, `uncertainty`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 7 (line 11065)

### Ch 8: Experimental Design: The Basics (pp. 173-202)

**핵심**: 변화 이론(theory of change)에 기반한 실험 계획, 무작위 배정, 표본 크기/검정력 분석, 실험 결과 분석 및 해석의 전 과정을 다룬다.

**키워드**: `experimental design`, `randomization`, `power analysis`, `sample size`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 8 (line 12475)

### Ch 9: Stratified Randomization (pp. 203-232)

**핵심**: 층화 무작위 배정의 원리와 구현, 부트스트랩 시뮬레이션을 이용한 검정력 분석을 다룬다. ITT(intention-to-treat)와 CACE(complier average causal estimate) 추정을 설명한다.

**키워드**: `stratified randomization`, `intention-to-treat`, `CACE`, `power simulation`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 9 (line 14256)

### Ch 10: Cluster Randomization and Hierarchical Modeling (pp. 233-252)

**핵심**: 군집 무작위 배정 실험 설계와 계층적 모형(hierarchical model)을 소개한다. R과 Python을 이용한 계층 모형 구현, 무작위 배정, 검정력 분석, 실험 분석 방법을 다룬다.

**키워드**: `cluster randomization`, `hierarchical model`, `mixed effects`, `ICC`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 10 (line 16121)

### Ch 11: Introduction to Moderation (pp. 257-295)

**핵심**: 조절 효과(moderation)의 행동적 유형(세분화, 상호작용, 비선형성)을 설명한다. 조절 효과의 적용 시점과 방법, 다중 조절 변수, 부트스트랩을 이용한 검증을 다룬다.

**키워드**: `moderation`, `segmentation`, `interaction`, `nonlinearity`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 11 (line 17840)

### Ch 12: Mediation and Instrumental Variables (pp. 297-315)

**핵심**: 매개 효과(mediation)를 통한 인과 메커니즘 이해와 측정 방법을 다룬다. 도구변수(instrumental variable)의 개념, 적용, FAQ를 비즈니스 맥락에서 설명한다.

**키워드**: `mediation`, `causal mechanism`, `instrumental variable`, `2SLS`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 12 (line 20016)
