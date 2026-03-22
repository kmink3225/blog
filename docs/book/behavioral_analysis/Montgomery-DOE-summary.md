---
name: "Design and Analysis of Experiments"
type: book-summary
authors: "M. N. Das, N. C. Giri"
year: 1979
total_pages: 296
language: en
keywords: [DOE, ANOVA, factorial-design, randomized-block, latin-square, incomplete-block, confounding, split-plot, bio-assay, weighing-design]
---

# Design and Analysis of Experiments — Summary

> M. N. Das, N. C. Giri (1979), ~296pp, 9 chapters
> 실험 설계의 통계적 원리와 분석 방법을 이론·실습 중심으로 다룬다

## Contents

- Ch 1: Concepts of Experiments: Design and Analysis (pp. 1-46)
- Ch 2: Complete Block Designs (pp. 47-77)
- Ch 3: Factorial Experiments (pp. 78-119)
- Ch 4: Asymmetrical Factorial and Split-Plot Designs (pp. 120-151)
- Ch 5: Incomplete Block Designs (pp. 152-204)
- Ch 6: Orthogonal Latin Squares (pp. 205-216)
- Ch 7: Designs for Bio-assays and Response Surfaces (pp. 217-262)
- Ch 8: Analysis of Covariance and Transformation (pp. 263-279)
- Ch 9: Weighing Designs (pp. 280-291)

---

## Chapter Summaries

> Marker 원본: `Montgomery-DOE_marker_full.md` | 총 ~9,150 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: Concepts of Experiments: Design and Analysis (pp. 1-46)
**핵심**: 실험 설계의 기본 개념과 데이터 수집 방법론을 소개한다. 실험 설계의 3대 원리(반복, 무작위화, 지역 통제)를 정의한다. 대비(contrasts)와 분산분석(ANOVA)의 기본 모델, 이원 분류 데이터 분석, ANOVA의 가정을 다룬다.
**키워드**: `replication`, `randomization`, `local-control`, `ANOVA`, `contrasts`
**상세**: → source file Ch 1 (line 134)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- 1.1 Design of Experiments and Collection of Data `L:175`
- 1.2 Experiments and their Designs `L:187`
- 1.4 Three Principles of Designs of Experiments `L:263`
- 1.6 Contrasts and Analysis of Variance `L:328`
- 1.7 Models and Analysis of Variance `L:491`
- 1.7.3 An Illustration of the Analysis of One-Way Classified Data `L:663`
- 1.8 Two-Way Classified Data `L:740`
- 1.8.1 Analysis of Two-Way Orthogonal Data `L:799`
- 1.8.3 Analysis of Three-Way Classified Orthogonal Data `L:1050`
- 1.8.4 Analysis of Non-Orthogonal Two-Way Data `L:1096`
- 1.8.5 ESTIMATE OF TREATMENT CONTRAST AND ITS VARIANCE `L:1224`
- 1.8.6 AN ILLUSTRATION OF THE ANALYSIS OF NON-ORTHOGONAL DATA `L:1255`
- 1.8.7 Some Types of Non-Orthogonal Data `L:1356`
- 1.9 Assumptions of Analysis of Variance `L:1426`


### Ch 2: Complete Block Designs (pp. 47-77)
**핵심**: 완전 무작위 설계(CRD), 무작위화 블록 설계(RBD), 라틴 방격 설계(Latin Square)의 구조·분석·적용을 다룬다. RBD에서의 결측 관측치 처리 방법을 설명한다.
**키워드**: `CRD`, `RBD`, `Latin-square`, `missing-observations`
**상세**: → source file Ch 2 (line 148)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- 2.1.2 ALTERNATIVE METHODS OF RANDOM ALLOCATION `L:1582`
- 2.2 Randomized Block Designs `L:1663`
- 2.2.1 RANDOMIZATION `L:1681`
- 2.2.2 Local Control `L:1687`
- 2.2.4 Missing Observations `L:1766`
- 2.3 Latin Square Designs `L:1772`
- 2.3.1 Randomization `L:1801`
- 2.3.4 Graeco Latin Square Designs `L:1938`
- 2.3.5 Orthogonal Latin Squares `L:1962`
- 2.4 Missing Observation in Randomized Block Designs `L:1993`
- 2.4.1 Analysis by Estimating the Missing Observations `L:1997`
- 2.4.2 Analysis by Taking the Data as Non-Orthogonal `L:2034`
- 2 4.4 Missing Observations in Latin Square Designs `L:2126`
- 2.4.5 LATIN SQUARES WITH A MISSING ROW OR COLUMN `L:2144`


### Ch 3: Factorial Experiments (pp. 78-119)
**핵심**: 요인 실험의 특성, 2수준·3수준 요인 설계, 유한체를 이용한 설계, 교호작용 대비의 그룹화, 교락(confounding), 부분실시법(fractional factorial)을 체계적으로 다룬다.
**키워드**: `factorial`, `confounding`, `fractional-factorial`, `interaction`
**상세**: → source file Ch 3 (line 158)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- 3.1 Characterization of Experiments `L:2464`
- 3.3 Factorial Experiments with Factors at Two Levels / `L:2490`
- 3.3.1 Designs for 2n Factorials, Main Effects and Interactions `L:2512`
- 3.4 Finite Fields and Designs of Experiments `L:2593`
- 3.5 Grouping for Interaction Contrasts `L:2654`
- 3.6 Confounding `L:2703`
- 3.8 Experiments with Factors at Three Levels Each `L:2817`
- 3.8.1 Factorials with Threb Factors each at Three Levels `L:2927`
- 3.8.2 Factorials with Four Factors each at Three Levels `L:2991`
- 3.9 A General Method of Construction of Confounded Factorials `L:3022`
- 3.9.1 A PROCEDURE TO AVOID BLOCK REPETITION WHILE GENERATING BLOCKS FROM THE KEY BLOCK `L:3141`
- 3.10 Maximum Number of Factors to Save Interactions up to a Given Order for a Given Block Size `L:3165`
- 3.10.1 MAXIMUM NUMBER OF FACTORS SAVING THREE FACTOR INTERACTIONS `L:3179`
- 3.11 Analysis of Factorial Experiments `L:3195`
- 3.12.1 Analysis of Fractional Factorials `L:3452`


### Ch 4: Asymmetrical Factorial and Split-Plot Designs (pp. 120-151)
**핵심**: 비대칭 요인 설계의 구성과 균형 교락 비대칭 요인의 분석, 분할구 설계(split-plot)의 구조와 분석 방법을 다룬다.
**키워드**: `asymmetrical-factorial`, `split-plot`, `balanced-confounding`
**상세**: → source file Ch 4 (line 182)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- CHAPTER 4 Asymmetrical Factorial and Split-Plot Designs `L:99`
- 4.2 Confounded Asymmetrical Factorials `L:3664`
- 4.3 Construction of Balanced Confounded Asymmetrical Factorials `L:3718`
- 4.4 Construction of Confounded Asymmetrical Factorial $v \times 2^2$ in 2v Plot Blocks `L:3959`
- 4.5.3 CRITERIA OF BALANCE AND MUTUAL INDEPENDENCE OF CONFOUNDED INTERACTIONS `L:4346`
- 4.6 Split-Plot Designs `L:4360`
- 4.7 Analysis `L:4370`


### Ch 5: Incomplete Block Designs (pp. 152-204)
**핵심**: 불완전 블록 설계(BIB, PBIB), Youden 방격, 격자 설계(lattice)의 구성·분석·블록 간 정보 복구(recovery of inter-block information)를 다룬다. 설계의 최적성(optimality) 기준을 소개한다.
**키워드**: `BIB`, `PBIB`, `Youden-square`, `lattice`, `optimality`
**상세**: → source file Ch 5 (line 199)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- 5.1 Varietal Trials `L:4604`
- 5.2 Incomplete Block Designs `L:4616`
- 5.4 Construction of B.I.B. Designs `L:4742`
- 5.4.3 AN ALTERNATIVE APPROACH FOR CONSTRUCTION OF B.I.B. DESIGNS `L:4862`
- 5.4.4 CONSTRUCTION OF B.I.B. DESIGNS BY DEVELOPING INITIAL BLOCKS `L:4874`
- 5.8 Lattice Designs `L:5196`
- 5.9 Partially Balanced Incomplete Block Designs `L:5310`
- 5.9.4 CLASSIFICATIONS OF P.B.I.B. DESIGNS WITH TWO ASSOCIATE CLASSES `L:5454`
- 5.11 Analysis with Recovery of Inter-Block Information `L:5679`
- 5.11.1 Estimation of the Weights W and W' `L:5787`


### Ch 6: Orthogonal Latin Squares (pp. 205-216)
**핵심**: 직교 라틴 방격의 최대 수, 구성 방법(유한체, 쌍별 균형 설계 활용)을 다룬다.
**키워드**: `orthogonal-Latin-squares`, `construction`, `finite-field`
**상세**: → source file Ch 6 (line 215)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- 6.1.1 DEFINITION: LATIN SQUARES `L:6286`
- 6.2 Maximum Number of Orthogonal Latin Squares `L:6296`
- 6.3 Construction of Orthogonal Latin Squares `L:6319`
- 6.3.1 CONSTRUCTION OF ORTHOGONAL LATIN SQUARES OF ORDER 4 `L:6341`
- 6.3.2 Construction of Two Orthogonal Latin Squares of Order 12 `L:6367`
- 6.4. Construction of Orthogonal Latin Squares by Using Pairwise Balanced Designs `L:6434`
- 6.4.1 ORTHOGONAL ARRAYS ASSOCIATED WITH LATIN SQUARES `L:6438`
- 6.4.2 A Modified Method: Falsity of Euler's Conjecture `L:6470`
- 6.4.3 Method of Construction of Two Orthogonal Latin Squares of Order 3m+l where m is Odd `L:6480`
- 6.4.4 Two Orthogonal Latin Squares of Order 14 `L:6540`
- 6.4.5 Two Orthogonal Latin Squares of Order 26 `L:6562`


### Ch 7: Designs for Bio-assays and Response Surfaces (pp. 217-262)
**핵심**: 생물 검정(bio-assay)용 설계: 직접 검정, 간접 검정, 평행선 검정, 기울기비 검정을 다룬다. 반응표면 설계(response surface design)의 원리와 구성을 설명한다.
**키워드**: `bio-assay`, `parallel-line`, `slope-ratio`, `response-surface`
**상세**: → source file Ch 7 (line 225)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- 7.1 Bio-assays `L:6612`
- 7.2 Direct Assays `L:6630`
- 7.3 Indirect Bio-assays `L:6688`
- 7.5 Incomplete Block Designs for Bio-assays `L:7031`
- 7.7.3 SECOND ORDER RESPONSE SURFACE DESIGNS `L:7579`
- 7.7.4 VARIANCE OF ESTIMATED RESPONSE `L:7668`


### Ch 8: Analysis of Covariance and Transformation (pp. 263-279)
**핵심**: 공분산 분석(ANCOVA)을 RBD, CRD, 라틴 방격, 비직교 데이터에 적용하는 방법을 다룬다. 결측 관측치 처리와 데이터 변환(transformation)을 설명한다.
**키워드**: `ANCOVA`, `covariate`, `transformation`, `non-orthogonal`
**상세**: → source file Ch 8 (line 242)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- CHAPTER 8 Analysis of Covariance and Transformation `L:150`
- 8.1 Analysis of Covariance `L:8159`
- 8.2 Analysis of Covariance for Randomized Block Designs `L:8173`
- 8.3 Analysis of Covariance of Completely Randomized and Latin Square Designs `L:8283`
- 8.4 Analysis of Covariance of Non-Orthogonal Data in Two-Way Classification `L:8294`
- 8.4.1 Analysis of Covariance of Non-Orthogonal Designs `L:8348`
- 8.6 Covariance and Analysis of Experiments with Missing Observations `L:8479`


### Ch 9: Weighing Designs (pp. 280-291)
**핵심**: 계량 설계(weighing design)의 정의, 추정 방법, 불완전 블록 설계를 계량 설계로 활용하는 방법, 1접시·2접시 계량 설계, 효율성 평가를 다룬다.
**키워드**: `weighing-design`, `BIB-application`, `efficiency`
**상세**: → source file Ch 9 (line 262)

**Marker 세부 목차** (`Montgomery-DOE_marker_full.md`):
- CHAPTER 9 Weighing Designs `L:160`
- 9.1 Introduction `L:8650`
- 9.2 Definition `L:8658`
- 9.3 Method of Estimation `L:8668`
- 9.4 Incomplete Block Designs as Weighing Designs `L:8698`
- 9.4.1 One Pan Weighing Design from B.I.B. Designs `L:8702`
- 9.4.3 ESTIMATE OF WEIGHT AS CONTRAST OF OBSERVATIONS `L:8783`
- 9.4.4 Reinforced Incomplete Block Designs as Weighing Designs `L:8817`
- 9.5 Two Pan Weighing Designs from B.I.B. Designs `L:8859`
- 9.5.1 REINFORCED B.I.B. DESIGNS FOR TWO PAN WEIGHING DESIGNS `L:8910`
- 9.5.2 REINFORCED B.I.B. DESIGNS WITH PARAMETERS `L:8952`
- 9.6 Two Associate P.B.I.B. Designs as One Pan Weighing Designs `L:8977`
- 9.7 Weighing Designs from Truncated Incomplete B.I.B. Designs `L:9026`
- 9.8 Efficiency `L:9042`



### 기타 섹션 (Marker)

- Design and Analysis of Experiments `L:22`
- Concepts of Experiments: Design and Analysis `L:60`
- Designsfor Bio-assays and Response Surfaces `L:137`
- DETERMINATION OF NUMBER OF REPLICATIONS `L:287`
- Asymmetrical Factorial and Split-Plot Designs `L:3650`
- Choice of Replications for Balance and Interactions Confounded `L:3768`
- Case of p Initial Blocks `L:4946`
- Example 1: 6-Point Symmetrical Parallel Line Assay `L:6992`
- Method II: Central Composite Designs `L:7858`
- Analysis of Covariance and Transformation `L:8157`
