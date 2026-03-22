---
name: "Design and Analysis of Experiments"
type: book-summary
authors: "M. N. Das, N. C. Giri"
year: 1979
total_pages: 296
language: en
keywords: [DOE, ANOVA, factorial-design, randomized-block, latin-square, incomplete-block, confounding, split-plot, bio-assay, weighing-design]
sources:
  - file: "Montgomery-DOE_marker_full.md"
    tool: Marker
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
이 장은 실험 설계와 데이터 수집의 기본 개념을 소개한다. 실험은 문제에 대한 답을 데이터로부터 추론하기 위해 통제된 조건을 만들어 수행하는 것이다. 통계적 원리를 무시하고 수집된 데이터는 유효한 추론에 활용할 수 없다. 실험 설계의 세 가지 기본 원리로 무작위화(randomization), 반복(replication), 오차 통제(error control)를 정의한다. 무작위화는 처리를 실험 단위에 무작위로 배분하여 주관적 편향을 방지하고 관측값의 독립성을 보장한다. 반복은 처리 효과 추정의 정밀도를 높이며, 오차 분산의 추정치를 제공한다. 오차 통제는 실험 단위를 동질적 블록으로 묶어 오차 분산을 줄이는 기법이다. 대비(contrast)의 개념을 도입하여 처리 효과 간 비교를 수학적으로 정의하며, 직교 대비의 최대 수가 n-1임을 증명한다. 분산분석(ANOVA)의 일원·이원 분류 모형과 직교·비직교 데이터 분석 방법을 상세히 다룬다. t-검정과 F-검정을 이용한 가설 검정 절차를 설명하고, 반복 수 결정 및 오차 분산 추정 방법을 제시한다. ANOVA의 기본 가정으로 정규성, 독립성, 등분산성을 논의한다.

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
이 장은 비교적 단순하고 널리 사용되는 세 가지 완전 블록 설계를 다룬다. 완전 무작위 설계(CRD)는 단일 동질 그룹의 실험 단위에 처리를 무작위로 배분하는 가장 간단한 설계이다. 무작위 배분은 난수표, 제비뽑기, 동전 던지기 등의 방법으로 수행한다. CRD의 분석은 일원 분류 모형에 기반하며, F-검정으로 처리 효과의 동질성을 검정한다. 무작위화 블록 설계(RBD)는 실험 단위를 동질적 블록으로 묶어 블록 간 변동을 제거함으로써 CRD보다 정밀도를 높인다. 각 블록에 모든 처리를 한 번씩 배분하므로 직교 설계가 된다. RBD의 분석에서는 블록, 처리, 오차의 제곱합을 분리하여 F-검정을 적용한다. 라틴 방격 설계(Latin Square)는 행과 열 두 방향의 변동을 동시에 제거할 수 있는 설계로, k개 처리를 k×k 방격에 배치한다. Graeco Latin 방격 설계와 직교 라틴 방격의 확장도 소개한다. 결측 관측치가 발생하면 데이터가 비직교가 되며, Yates의 결측값 추정법 또는 비직교 데이터 분석법으로 처리할 수 있다. 라틴 방격에서의 결측 행·열 처리 방법도 설명한다.

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
이 장은 요인 실험의 특성과 설계·분석 방법을 체계적으로 다룬다. 실험은 품종 시험, 요인 실험, 생물 검정의 세 가지 유형으로 분류된다. 요인 실험에서는 둘 이상의 요인의 수준 조합이 처리를 구성하며, 주효과와 교호작용을 동시에 추정할 수 있다. 2수준 요인 설계(2^n)에서 주효과와 교호작용 대비를 기호(+, -)로 정의하고, 그 제곱합을 계산하는 방법을 설명한다. 유한체(Galois field)의 원소를 이용하여 요인 조합의 수준 코드를 정의하고 선형 방정식의 해로 교호작용 그룹을 구성하는 방법을 제시한다. 교락(confounding)은 블록 크기를 줄이기 위해 고차 교호작용을 블록 효과와 혼합하는 기법이다. 완전 교락에서는 모든 반복에서 같은 교호작용을 교락하고, 부분 교락에서는 다른 반복에서 다른 교호작용을 교락하여 정보를 복구한다. 키 블록(key block)의 내용은 동차 방정식의 독립 해의 선형 조합으로 생성한다. 둘 이상의 블록으로 분할할 때 일반화 교호작용(generalized interaction)이 추가로 교락된다. 3수준 요인 설계(3^n)에 대해서도 유사한 교락 구성과 분석 방법을 제공한다. 부분실시법(fractional factorial)은 전체 요인 조합의 일부만 실시하여 자원을 절약하며, 앨리어스(alias) 구조를 통해 추정 가능한 효과를 결정한다.

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
이 장은 비대칭 요인 설계와 분할구 설계를 다룬다. 비대칭 요인 실험에서는 모든 요인이 동일한 수준 수를 갖지 않으며, 대칭 요인 설계보다 실험자의 요구에 유연하게 대응할 수 있다. 비대칭 요인의 교락 설계 구성은 대칭 요인보다 복잡하며, Das(1960)와 Kishen-Srivastava(1959)의 체계적 구성 방법이 소개된다. Das의 방법은 비대칭 요인을 대응하는 대칭 요인의 부분실시(fraction)로 변환하여 설계를 구성한다. 비대칭 요인의 수준은 의사 요인(pseudo factor)의 조합으로 표현되며, 불필요한 조합은 제거한다. 교락 시 의사 요인만 포함된 교호작용이 교락되면 비대칭 요인의 주효과가 손실되므로 이를 피해야 한다. 균형 교락 비대칭 요인 설계를 얻기 위해 여러 반복에 걸쳐 동일한 비대칭 요인 교호작용을 모든 가능한 방식으로 교락한다. 정의 대비(defining contrast)와 앨리어스 그룹을 이용하여 균형을 달성하는 반복 선택 절차를 체계화한다. 2×2×3, 3×2², 6×2² 등 다양한 비대칭 요인 설계의 구체적 구성 예를 제시한다. 분할구 설계(split-plot)는 한 요인의 수준 변경이 어려울 때 전체구(whole plot)와 세부구(sub-plot)로 나누어 배치하는 설계이다. 분할구 설계의 분석에서는 전체구 오차와 세부구 오차를 별도로 추정한다.

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
이 장은 불완전 블록 설계의 정의, 구성, 분석을 다룬다. 품종 시험에서 처리 수가 많으면 무작위화 블록 설계의 블록 크기가 커져 정밀도가 떨어지므로, 블록 크기를 줄인 불완전 블록 설계가 필요하다. 균형 불완전 블록(BIB) 설계에서는 모든 처리 쌍이 동일한 횟수(λ)만큼 함께 나타나며, 매개변수 v, b, k, r, λ 사이의 기본 관계식을 도출한다. Fisher의 부등식 b≥v를 증명하며, b=v인 경우를 대칭 BIB 설계로 정의한다. BIB 설계의 구성 방법으로 유한 기하학, 초기 블록 전개(developing initial blocks), 그리고 요인 설계와의 연결을 활용하는 방법을 소개한다. 격자 설계(lattice design)는 처리 수가 완전 제곱수일 때 적용 가능하며, 적은 반복 수로 설계할 수 있다. 부분 균형 불완전 블록(PBIB) 설계에서는 처리 쌍의 반복 횟수가 m가지 유형(λ₁, λ₂, ...)으로 나뉘며, 연관 클래스 개념을 정의한다. 설계의 연결성(connectedness) 조건을 확인하여 모든 처리 대비가 추정 가능한지 판별한다. 블록 간 정보 복구(recovery of inter-block information) 기법을 통해 블록 내 추정치와 블록 간 추정치를 가중 결합하여 정밀도를 높인다. 설계의 최적성 기준으로 해소 가능(resolvable) 설계와 아핀 해소 가능(affine resolvable) 설계의 개념을 소개한다.

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
이 장은 직교 라틴 방격(orthogonal Latin squares)의 최대 수와 구성 방법을 다룬다. 차수 r의 라틴 방격은 r개의 기호를 r×r 방격에 배치하여 각 행과 열에 모든 기호가 정확히 한 번씩 나타나도록 한 배열이다. 두 라틴 방격이 직교한다는 것은 하나를 다른 하나 위에 겹쳤을 때 모든 기호 쌍이 정확히 한 번씩 나타남을 의미한다. 차수 r의 직교 라틴 방격의 최대 수는 r-1임을 증명한다. r이 소수 또는 소수의 거듭제곱일 때 r-1개의 직교 라틴 방격을 모두 구성할 수 있다. 구성 방법은 Galois field의 원소를 기호로 사용하여 합산표(summation table)를 만들고, 주열(principal column)에 서로 다른 승수(multiplier)를 곱하여 새로운 직교 방격을 생성하는 것이다. r이 서로 다른 소수의 곱일 때는 각 소인수 체의 원소 조합을 기호로 사용하며, 최소 소인수 s에 대해 s-1개의 직교 방격을 구성한다. 차수 4와 12의 직교 라틴 방격 구성 예를 구체적으로 제시한다. 쌍별 균형 설계(pairwise balanced design)와 직교 배열(orthogonal array)을 활용하여 직교 라틴 방격을 구성하는 Bose-Shrikhande-Parker의 방법을 소개한다. 이 방법으로 차수 6을 제외한 모든 차수에서 최소 두 개의 직교 라틴 방격이 존재함을 보여 오일러의 추측이 거짓임을 증명한다. 차수 3m+1(m은 홀수), 14, 26에 대한 직교 라틴 방격의 구체적 구성법도 제시한다.

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
이 장은 생물 검정(bio-assay)과 반응표면 설계를 다룬다. 생물 검정은 두 가지 이상의 약물 제제의 효능을 생체 반응을 통해 비교하는 실험이다. 표준 제제와 시험 제제의 상대적 역가(relative potency)는 동일 반응을 유도하는 두 용량의 비율로 정의한다. 직접 검정(direct assay)에서는 사전에 지정된 반응(예: 사망)이 나타나는 내성 용량을 직접 측정하며, Fieller의 정리로 역가 추정의 정밀도를 평가한다. 간접 검정(indirect assay)에서는 용량-반응 관계를 먼저 파악한 후 해당 관계로부터 등효 용량을 추정한다. 용량의 로그 변환이 선형화 변환이면 두 제제의 회귀선이 평행하므로 평행선 검정(parallel line assay)이 되고, 거듭제곱 변환이면 기울기비 검정(slope ratio assay)이 된다. 대칭 평행선 검정에서는 각 제제의 용량을 등비 수열로 배치하여 분석을 단순화한다. 타당성 검정으로 선형성과 평행성(또는 절편 공유)을 확인한 후 상대 역가를 추정한다. 불완전 블록 설계를 생물 검정에 적용하는 방법도 설명한다. 반응표면 설계(response surface design)는 반응 변수를 요인 수준의 함수로 모형화하여 최적 조건을 탐색하는 설계이다. 2차 반응표면 설계와 중심합성설계(central composite design)의 구성 원리와 추정 반응의 분산을 분석한다.

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
이 장은 공분산 분석(ANCOVA)과 데이터 변환을 다룬다. 공분산 분석은 연구 변량(y)과 상관된 보조 변량(x)의 관측값을 이용하여 오차 분산을 줄이는 기법이다. 기본 원리는 블록과 처리 효과를 제거한 후 x와 y의 선형 관계를 추정하고, 그 관계로부터 기대되는 y값을 분석하여 조정된 오차 분산을 얻는 것이다. 보조 변량이 실험 처리에 영향을 받지 않아야 한다는 조건이 필수적이다. 무작위화 블록 설계에서의 ANCOVA 모형은 일반 평균, 처리 효과, 블록 효과, 회귀 계수, 오차를 포함하며, 최소제곱법으로 추정한다. 조정된 오차 제곱합의 자유도는 (r-1)(k-1)-1로, 회귀 계수 추정을 위해 1만큼 감소한다. 처리 효과의 동질성 검정은 처리 효과가 0이라는 가설 하에서의 오차 제곱합과 비교하여 F-검정으로 수행한다. 처리 대비의 분산에는 x 변량의 처리 평균 차이에 따른 추가 항이 포함된다. 완전 무작위 설계와 라틴 방격 설계에 대해서도 동일한 절차가 적용된다. 비직교 데이터의 공분산 분석에서는 조정된 처리 곱합(sum of products)을 별도로 계산한다. 보조 변량이 두 개인 경우로 확장하여 편회귀 계수를 연립 방정식으로 추정하는 방법을 제시한다. 불완전 블록 설계의 공분산 분석도 유사한 절차를 따른다. 데이터 변환(transformation)은 ANOVA의 가정이 충족되지 않을 때 적용하는 보완 기법이다.

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
이 장은 계량 설계(weighing design)의 정의, 추정 방법, 구성을 다룬다. 계량 설계는 p개의 물체를 N번의 계량으로 그룹화하여 개별 무게를 최소제곱법으로 추정하는 기법이다. Yates(1935)는 물체를 개별이 아닌 그룹으로 계량하면 추정 정밀도가 크게 향상됨을 보였다. Hotelling(1944)은 화학 저울의 양쪽 접시에 물체를 분배하면 정밀도가 추가로 증가함을 입증하였다. 1접시 계량 설계에서는 물체를 한쪽 접시에만 올리며, 설계 행렬 A로부터 최소제곱 추정량 W=(A'A)⁻¹(A'Y)를 구한다. 균형 불완전 블록(BIB) 설계의 블록 내용을 계량 그룹으로 활용하여 1접시 계량 설계를 구성한다. BIB 기반 추정량은 대비(contrast) 형태가 아니므로 영점 편향에 취약하며, 모든 물체를 포함하는 추가 계량을 도입하여 대비 형태의 추정량을 유도할 수 있다. 보강 불완전 블록 설계(reinforced IB design)는 각 블록에 추가 물체를 포함하여 계량 설계로 활용한다. 2접시 계량 설계에서는 블록 내 물체를 왼쪽 접시에, 나머지를 오른쪽 접시에 배치하여 v=2k인 경우를 제외하고 추정이 가능하다. 2접시 보강 BIB 설계에서 추가 물체의 분산이 다른 물체보다 클 수 있음을 보인다. PBIB 설계를 1접시 계량 설계로 활용하는 방법과 절단 BIB 설계(truncated BIB)로부터의 구성법도 소개한다. 계량 설계의 효율성은 관습적 개별 계량 대비 분산 비율로 평가한다.

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

---

## Marker 세부 목차

> `L:숫자`는 `Montgomery-DOE_marker_full.md`의 라인 번호. `Read(file, offset=L, limit=N)`으로 해당 구간을 직접 읽을 수 있다.

- Design and Analysis of Experiments `L:22`
- Concepts of Experiments: Design and Analysis `L:60`
- CHAPTER 4 Asymmetrical Factorial and Split-Plot Designs `L:99`
- Designsfor Bio-assays and Response Surfaces `L:137`
- CHAPTER 8 Analysis of Covariance and Transformation `L:150`
- CHAPTER 9 Weighing Designs `L:160`
- 1.1 Design of Experiments and Collection of Data `L:175`
- 1.2 Experiments and their Designs `L:187`
- 1.4 Three Principles of Designs of Experiments `L:263`
- DETERMINATION OF NUMBER OF REPLICATIONS `L:287`
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
- Asymmetrical Factorial and Split-Plot Designs `L:3650`
- 4.2 Confounded Asymmetrical Factorials `L:3664`
- 4.3 Construction of Balanced Confounded Asymmetrical Factorials `L:3718`
- Choice of Replications for Balance and Interactions Confounded `L:3768`
- 4.4 Construction of Confounded Asymmetrical Factorial $v \times 2^2$ in 2v Plot Blocks `L:3959`
- 4.5.3 CRITERIA OF BALANCE AND MUTUAL INDEPENDENCE OF CONFOUNDED INTERACTIONS `L:4346`
- 4.6 Split-Plot Designs `L:4360`
- 4.7 Analysis `L:4370`
- 5.1 Varietal Trials `L:4604`
- 5.2 Incomplete Block Designs `L:4616`
- 5.4 Construction of B.I.B. Designs `L:4742`
- 5.4.3 AN ALTERNATIVE APPROACH FOR CONSTRUCTION OF B.I.B. DESIGNS `L:4862`
- 5.4.4 CONSTRUCTION OF B.I.B. DESIGNS BY DEVELOPING INITIAL BLOCKS `L:4874`
- Case of p Initial Blocks `L:4946`
- 5.8 Lattice Designs `L:5196`
- 5.9 Partially Balanced Incomplete Block Designs `L:5310`
- 5.9.4 CLASSIFICATIONS OF P.B.I.B. DESIGNS WITH TWO ASSOCIATE CLASSES `L:5454`
- 5.11 Analysis with Recovery of Inter-Block Information `L:5679`
- 5.11.1 Estimation of the Weights W and W' `L:5787`
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
- 7.1 Bio-assays `L:6612`
- 7.2 Direct Assays `L:6630`
- 7.3 Indirect Bio-assays `L:6688`
- Example 1: 6-Point Symmetrical Parallel Line Assay `L:6992`
- 7.5 Incomplete Block Designs for Bio-assays `L:7031`
- 7.7.3 SECOND ORDER RESPONSE SURFACE DESIGNS `L:7579`
- 7.7.4 VARIANCE OF ESTIMATED RESPONSE `L:7668`
- Method II: Central Composite Designs `L:7858`
- Analysis of Covariance and Transformation `L:8157`
- 8.1 Analysis of Covariance `L:8159`
- 8.2 Analysis of Covariance for Randomized Block Designs `L:8173`
- 8.3 Analysis of Covariance of Completely Randomized and Latin Square Designs `L:8283`
- 8.4 Analysis of Covariance of Non-Orthogonal Data in Two-Way Classification `L:8294`
- 8.4.1 Analysis of Covariance of Non-Orthogonal Designs `L:8348`
- 8.6 Covariance and Analysis of Experiments with Missing Observations `L:8479`
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
