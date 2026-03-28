---
name: "Designing Experiments and Analyzing Data: A Model Comparison Perspective"
type: book-summary
sources:
  - file: "Maxwell-DesigningExperiments_azure_full.md"
    tool: Document Intelligence
authors: "Scott E. Maxwell, Harold D. Delaney"
year: 2004
total_pages: 868
language: en
keywords: [experimental design, ANOVA, model comparison, factorial design, repeated measures, multilevel model, contrast, multiple comparison, ANCOVA, nested design]
---

# Designing Experiments and Analyzing Data — Summary

> Scott E. Maxwell, Harold D. Delaney (2004, 2nd ed.), 868 pages, 16 chapters
> 모형 비교(model comparison) 관점에서 실험 설계와 데이터 분석을 포괄적으로 다루는 대학원 수준 교과서

## Contents

**Part I. Conceptual Bases of Experimental Design and Analysis**
1. The Logic of Experimental Design (p.3)
2. Introduction to the Fisher Tradition (p.34)

**Part II. Model Comparisons for Between-Subjects Designs**
3. Introduction to Model Comparisons: One-Way Between-Subjects Designs (p.67)
4. Individual Comparisons of Means (p.149)
5. Testing Several Contrasts: The Multiple-Comparison Problem (p.193)
6. Trend Analysis (p.243)
7. Two-Way Between-Subjects Factorial Designs (p.275)
8. Higher Order Between-Subjects Factorial Designs (p.354)
9. Designs With Covariates: ANCOVA and Blocking (p.399)
10. Designs with Random or Nested Factors (p.469)

**Part III. Model Comparisons for Designs Involving Within-Subjects Factors**
11. One-Way Within-Subjects Designs: Univariate Approach (p.525)
12. Higher-Order Designs with Within-Subjects Factors: Univariate Approach (p.573)
13. One-Way Within-Subjects Designs: Multivariate Approach (p.624)
14. Higher Order Designs With Within-Subjects Factors: Multivariate Approach (p.682)

**Part IV. Alternative Analysis Strategies**
15. An Introduction to Multilevel Models for Within-Subjects Designs (p.763)
16. An Introduction to Multilevel Hierarchical Mixed Models: Nested Designs (p.828)

---

## Chapter Summaries

### Ch 1: The Logic of Experimental Design (pp. 3-33)

**핵심**: 과학 철학적 관점에서 실험 설계의 논리를 다룬다. 전통적 과학관과 현대 과학 철학을 비교하고, 타당도(내적, 외적, 구성, 통계적 결론 타당도)에 대한 위협과 그 통제 방법을 체계적으로 제시한다.

**키워드**: `validity`, `internal validity`, `external validity`, `threats to validity`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 1 (line 2360)
이 장은 실험 설계와 데이터 분석의 근간이 되는 과학 철학적 논리를 다룬다. Bacon의 귀납적 방법론에서 출발한 전통적 과학관이 순수한 객관성과 합리성을 전제했으나, 데이터 수집·분석·해석의 모든 단계에서 연구자의 사전 판단이 개입한다는 한계를 지적한다. 자연의 법칙성, 유한 인과, 인과성 원리 등 과학의 기본 가정을 논의하며, 행동과학에서 개인차로 인한 균일성 가정의 문제를 강조한다. Hume의 상관-인과 구분, Cook과 Campbell의 인과 철학 논의를 통해 현대 과학에서 인과관계가 확률적이고 맥락 의존적임을 설명한다. 실재론적 관점에서 이론적 주장은 객관적으로 옳거나 틀릴 수 있다고 본다. 내적 타당도, 외적 타당도, 구성 타당도, 통계적 결론 타당도의 네 가지 타당도 유형을 체계적으로 구분하고, 각 타당도에 대한 위협 요인을 열거한다. 무작위 배정, 실험 통제, 맹검 등 타당도 위협을 통제하는 방법을 소개하며, 실험 설계가 과학적 추론의 질을 결정짓는 핵심 도구임을 강조한다. 연구자의 철학적 입장이 설계와 분석 전략에 영향을 미치므로, 방법론적 선택에 대한 반성적 인식이 필요하다고 결론짓는다.

### Ch 2: Introduction to the Fisher Tradition (pp. 34-66)

**핵심**: Fisher 전통의 통계적 추론을 소개한다. 이산 확률 예제, 무작위 배정 검정, 가설과 p-값에 대한 Fisher vs Neyman-Pearson 관점을 비교하고, 분포 가정에 기반한 검정으로의 전환을 다룬다.

**키워드**: `Fisher tradition`, `randomization test`, `p-value`, `Neyman-Pearson`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 2 (line 4290)
이 장은 Fisher 전통의 통계적 추론을 소개하며, 통계를 단순한 계산이 아닌 조직화된 논증으로 바라보는 관점을 강조한다. Fisher가 Rothamsted 농업시험장에서 실험 설계와 분산분석(ANOVA)의 기초를 확립한 역사적 맥락을 설명한다. 유명한 "차 맛보기 실험"(lady tasting tea)을 통해 무작위 배정과 이산 확률 분포를 이용한 가설검정의 원리를 상세히 도출한다. 조합론(combinations)을 활용하여 관찰 결과의 확률을 직접 계산하는 방법을 보여준다. 무작위 배정이 통제 불가능한 요인들의 영향을 균형 잡아 통계 검정의 타당성을 보장하는 핵심 원리임을 설명한다. Fisher의 p-값 해석과 Neyman-Pearson의 가설검정 프레임워크(제1종 오류, 제2종 오류, 검정력)를 비교·대조하며, 현재 널리 사용되는 절차가 두 접근의 혼합임을 논의한다. 이산 확률 분석에서 연속 분포 가정에 기반한 검정(z, t, F 검정)으로의 전환 과정을 다루며, 정규성 가정과 중심극한정리의 역할을 설명한다. 효과 크기와 신뢰구간의 중요성도 언급하며, 통계적 방법론이 역동적으로 진화하는 분야임을 강조한다.

### Ch 3: One-Way Between-Subjects Designs (pp. 67-148)

**핵심**: 일반선형모형(GLM) 프레임워크에서 일원 분산분석을 모형 비교로 재구성한다. 최소제곱 추정, F 검정의 도출, 효과 크기 측정, 통계적 가정(정규성, 등분산)의 검토, 검정력 분석을 포괄적으로 다룬다. 강건 방법(비모수적 접근 포함)도 다룬다.

**키워드**: `one-way ANOVA`, `model comparison`, `F-test`, `effect size`, `robust methods`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 3 (line 6977)
이 장은 일반선형모형(GLM) 프레임워크 내에서 일원 피험자 간 설계의 분산분석을 모형 비교 관점으로 재구성한다. 종속변수를 허용된 요인의 효과와 잔차의 합으로 표현하는 data = fit + residual 구조를 소개하며, Tukey의 간결한 표현을 인용한다. 단일 집단 상황에서 μ 추정과 최소제곱 원리를 설명한 후, 두 집단, 세 집단 이상으로 점진적으로 확장한다. 전체 모형(full model)과 제한 모형(restricted model)의 오차제곱합 차이에 기반한 F 검정의 도출 과정을 상세히 다룬다. 효과 크기 측정 지표로 η², ω², Cohen의 d를 소개하고, 신뢰구간과 검정력 분석의 중요성을 강조한다. 정규성, 등분산성, 독립성 등 통계적 가정의 의미와 위반 시 영향을 논의하며, Levene 검정 등 진단 방법을 제시한다. 가정 위반에 강건한 대안으로 Welch의 F 검정, Brown-Forsythe 검정, 비모수적 Kruskal-Wallis 검정을 소개한다. 데이터 시각화를 통한 사전 탐색의 중요성을 APA 통계추론 태스크포스의 권고와 함께 강조한다. 모형 비교 접근이 이후 장에서 다루는 다요인 설계, 회귀, 공분산분석으로 자연스럽게 확장될 수 있음을 예고한다.

### Ch 4: Individual Comparisons of Means (pp. 149-192)

**핵심**: 개별 대비(contrast)의 모형 비교적 접근, 복합 대비, t 검정 공식, 직교성과 비직교성, 효과 크기 측정을 다룬다.

**키워드**: `contrast`, `pairwise comparison`, `orthogonality`, `effect size`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 4 (line 12861)
이 장은 옴니버스 F 검정 이후 어떤 집단 평균이 차이 나는지를 파악하기 위한 개별 비교(individual comparison) 방법을 다룬다. 고혈압 치료 연구 예제를 통해 약물 치료, 바이오피드백, 식이 조절, 복합 치료 간 다양한 비교 질문을 동기부여한다. 모형 비교 접근에서 전체 모형은 동일하게 유지하면서 제한 모형만 변경하여 특정 쌍의 평균 동일성을 검정하는 방법을 도출한다. 두 집단 평균 비교를 위한 F 통계량 공식을 최소제곱 추정으로부터 유도하며, t 검정과의 관계(F = t²)를 설명한다. 대비(contrast) 개념을 일반화하여 대비 계수(c_j)의 합이 0이 되는 선형 조합으로 정의하고, 복합 대비의 검정 방법을 제시한다. 직교 대비(orthogonal contrasts)와 비직교 대비의 구분, 직교 대비의 제곱합 가산성(additivity)을 증명한다. 효과 크기 측정으로 대비에 대한 d 지표를 소개하고, 신뢰구간 구성 방법을 다룬다. 계획된 비교(planned comparisons)와 사후 비교(post hoc comparisons)의 구분을 예고하며, 다중 비교 문제를 Ch 5에서 본격적으로 다룰 것임을 안내한다.

### Ch 5: The Multiple-Comparison Problem (pp. 193-242)

**핵심**: 다중 비교 문제를 체계적으로 다룬다. 실험별 오류율(experimentwise error rate), Bonferroni, Tukey HSD, Scheffe, Dunnett, FDR 등 다양한 보정 방법을 비교하고 적절한 절차 선택 지침을 제시한다.

**키워드**: `multiple comparison`, `Bonferroni`, `Tukey HSD`, `Scheffe`, `FDR`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 5 (line 16130)
이 장은 동일 데이터에서 여러 대비를 검정할 때 발생하는 다중 비교 문제를 체계적으로 다룬다. 비교별 오류율(αPC), 실험별 오류율(αEW), 실험당 기대 오류 수(ENEPE)의 세 가지 오류율 유형을 정의하고, 이항 공식을 통해 직교 대비 집합의 αEW를 계산한다. αEW를 .05로 통제하는 것이 바람직한 이유를 출판 편향 및 문헌 내 제1종 오류 축적 관점에서 논증한다. 동시 신뢰구간(simultaneous confidence intervals)의 개념과 가설검정과의 대응 관계를 설명한다. Hsu의 다섯 수준 추론 강도(비교별, 동질성 검정, 확신된 부등식, 확신된 방향, 신뢰구간)를 소개하며 가장 강한 수준의 추론을 권장한다. Bonferroni, Tukey HSD, Scheffe, Dunnett 등 주요 다중 비교 절차의 원리, 장단점, 적용 조건을 비교한다. 등분산 가정이 위반될 때의 대안적 절차와 비균등 표본 크기 상황에서의 조정 방법을 다룬다. 계획된 비교와 사후 비교 상황에 따른 적절한 절차 선택 지침을 제시하며, FDR(false discovery rate) 방법도 소개한다. 검정력과 제1종 오류 간 상충 관계를 강조하며, 연구 목적에 맞는 균형 잡힌 선택의 중요성을 결론짓는다.

### Ch 6: Trend Analysis (pp. 243-274)

**핵심**: 양적 요인에 대한 추세 분석을 다룬다. 선형/비선형 추세의 검정, 고차 추세 분석, 추세 대비 계수 산출, 비균등 표본 크기 상황을 포함한다.

**키워드**: `trend analysis`, `linear trend`, `polynomial contrast`, `quantitative factor`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 6 (line 20558)
이 장은 양적 요인(quantitative factor)에 대한 추세 분석을 대비 검정의 특수한 경우로 다룬다. 질적 요인과 양적 요인의 구분을 설명하고, 양적 요인의 수준 간 관계를 활용한 분석의 이점을 논의한다. 기억 과제에서 학습 시간이 회상 점수에 미치는 효과를 예제로, 산점도를 통한 시각적 탐색에서 출발하여 회귀 모형을 동기부여한다. 선형 추세 대비 계수를 직교 다항식(orthogonal polynomials)으로 도출하는 방법을 상세히 설명한다. 선형, 이차, 삼차 등 고차 추세의 검정 방법과 각 추세의 제곱합 계산을 다룬다. 직교 다항식 대비 계수의 산출 원리와 표 사용법을 제시하며, 비균등 간격 수준에서의 계수 조정 방법도 다룬다. 추세 분석과 회귀 분석의 관계를 논의하며, 요인의 수준 수가 적고 각 수준에 여러 관측치가 있을 때 추세 분석이 유리함을 설명한다. 비균등 표본 크기 상황에서의 추세 분석 조정 방법을 포함하며, 연속형 변수를 범주화하여 추세 분석을 수행하는 것은 권장하지 않는다고 강조한다. 피험자 내 설계에서의 추세 분석은 Ch 11 이후에서 확장됨을 예고한다.

### Ch 7: Two-Way Factorial Designs (pp. 275-353)

**핵심**: 이원 요인 설계에서 상호작용의 개념, 모형 비교를 통한 주효과와 상호작용 검정, 단순효과(simple effects)와 상호작용 대비(interaction contrast), 비직교 설계에서의 제곱합 유형(Type I/II/III)을 다룬다.

**키워드**: `factorial design`, `interaction`, `simple effects`, `Type III SS`, `nonorthogonal`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 7 (line 23251)
이 장은 이원 요인 설계(two-way factorial design)에서 주효과와 상호작용의 개념을 모형 비교 관점으로 다룬다. 바이오피드백과 약물 치료의 2×2 고혈압 연구 예제를 통해 4개 집단의 데이터를 분석한다. 옴니버스 검정 대신 직교 대비로 바이오피드백 효과, 약물 효과, 상호작용을 분리하여 검정하는 방법을 보여준다. 주효과(main effect)는 한 요인의 평균 효과로서 다른 요인의 수준에 걸쳐 평균한 주변 평균의 비교임을 설명한다. 상호작용은 한 요인의 효과가 다른 요인의 수준에 따라 달라지는 것으로, 교차 그래프(interaction plot)를 통한 시각적 해석 방법을 제시한다. 단순효과(simple effects) 분석과 상호작용 대비(interaction contrast)의 의미와 검정 방법을 다룬다. 비직교 설계(unequal cell sizes)에서 제곱합 유형(Type I, II, III)의 차이와 각 유형의 장단점을 논의한다. 가중 평균과 비가중 평균의 구분, 효과 크기 측정, 검정력 분석을 이원 설계 맥락에서 다룬다. 유의한 상호작용이 존재할 때 주효과 해석의 주의점과 후속 분석 전략의 일반 지침을 제시한다. 이 장의 원리가 삼원 이상의 고차 요인 설계(Ch 8)로 확장됨을 예고한다.

### Ch 8: Higher Order Factorial Designs (pp. 354-398)

**핵심**: 삼원 이상의 요인 설계에서 주효과, 이원 상호작용, 삼원 상호작용의 의미와 해석을 다룬다. 효과 분석의 일반 지침과 비직교 설계를 포함한다.

**키워드**: `three-way interaction`, `higher-order factorial`, `simple interaction`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 8 (line 30027)
이 장은 삼원 이상의 요인 설계로 확장하며, 2×2×2 설계를 중심으로 삼원 상호작용의 개념을 설명한다. 고혈압 연구에 식이 요인을 추가한 바이오피드백×약물×식이 설계를 예제로 사용한다. 삼원 설계에서 7개의 효과(3개 주효과, 3개 이원 상호작용, 1개 삼원 상호작용)를 식별하는 방법을 체계적으로 제시한다. 주효과는 나머지 모든 요인에 걸쳐 평균한 주변 평균을 비교하며, 이원 상호작용은 관련 없는 요인에 걸쳐 평균한 후 이원 설계와 동일한 논리로 평가한다. 삼원 상호작용은 이원 상호작용이 세 번째 요인의 수준에 따라 달라지는 것으로 정의하며, 인구 평균 표를 이용한 수치적 예시로 해석 방법을 보여준다. 일반적인 a×b×c 설계로의 확장에서 F 검정의 도출, 자유도 계산, ANOVA 표 구성 방법을 다룬다. 효과 분석의 일반 지침으로 유의한 최고차 상호작용부터 해석하는 하향식(top-down) 전략을 권장한다. 단순 상호작용 효과(simple interaction effects)와 단순 단순효과(simple simple effects)의 검정 방법을 설명한다. 비직교 설계(비균등 셀 크기)에서의 추가적 고려사항과 제곱합 유형 선택 문제를 다룬다. 4요인 이상의 설계에서 효과 수가 급증하는 문제와 실질적 해석의 어려움을 논의한다.

### Ch 9: ANCOVA and Blocking (pp. 399-468)

**핵심**: 공변량 분석(ANCOVA)의 논리, 선형 모형, 통계적 가정(회귀 동질성), 보정 평균의 비교를 다룬다. 블로킹(blocking), 잔차 ANOVA, 이득 점수(gain score) 등 대안적 분석도 포함한다.

**키워드**: `ANCOVA`, `covariate`, `blocking`, `homogeneity of regression`, `adjusted means`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 9 (line 34696)
이 장은 공변량 분석(ANCOVA)과 블로킹(blocking)을 통해 피험자 간 개인차 정보를 모형에 포함시키는 방법을 다룬다. 공변량(covariate)은 종속변수와 공변하는 사전 측정 변수로, 집단 내 변동성을 줄여 검정력을 높이는 주요 효과를 갖는다. ANCOVA의 선형 모형은 집단 효과와 연속형 공변량을 동시에 포함하며, 전체 모형과 제한 모형의 비교로 처리 효과를 검정한다. 회귀 동질성(homogeneity of regression) 가정의 의미와 위반 시 영향, 보정 평균(adjusted means)의 해석을 상세히 다룬다. 무작위 배정 연구에서 ANCOVA가 검정력을 높이는 정당한 방법이지만, 비무작위 연구에서는 체계적 매칭이 다른 차원의 체계적 불일치를 초래할 수 있음을 Lord의 경고와 함께 논의한다. 변화 점수(change score) 분석과 잔차 ANOVA 등 대안적 분석 방법을 ANCOVA와 비교한다. 블로킹 설계에서 연속 공변량을 범주화하여 추가 요인으로 사용하는 방법과 그 장단점을 다룬다. 사후 블로킹(post hoc blocking)의 문제점과 ANCOVA 대비 블로킹의 효율성 비교를 제시한다. 공변량이 여러 개인 경우의 다중 공변량 ANCOVA로의 확장 가능성을 언급하며, 공변량 선택의 실질적 고려사항을 논의한다.

### Ch 10: Random and Nested Factors (pp. 469-524)

**핵심**: 무선 요인(random factor)과 중첩 요인(nested factor)의 개념, 모형, 검정을 다룬다. 고정 vs 무선 효과의 구별, 기대 평균 제곱, 검정력 결정을 포함한다.

**키워드**: `random factor`, `nested design`, `expected mean squares`, `variance component`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 10 (line 40553)
이 장은 무선 요인(random factor)과 중첩 요인(nested factor)을 포함하는 설계의 분석을 다룬다. 고정 효과는 특정 수준에 대한 추론인 반면, 무선 효과는 표집된 수준을 통해 수준 모집단으로 일반화하는 것이 목적임을 구분한다. 일요인 무선효과 모형에서 μ_j가 정규분포를 따르는 확률변수가 되며, 귀무가설이 σ²_α = 0으로 표현됨을 설명한다. 기대 평균 제곱(expected mean squares)의 유도를 통해 무선 효과 존재 시 F 검정의 분모항이 달라져야 함을 보여준다. 이요인 혼합 모형(mixed model)에서 고정 요인 검정 시 적절한 오차항 선택 규칙을 기대 평균 제곱으로부터 도출한다. 무선 요인을 고정으로 잘못 처리할 경우 양의 편향이 발생하여 위양성 결론에 이를 수 있음을 경고한다. 중첩 설계(nested design)의 구조를 설명하며, 중첩 요인과 교차 요인의 차이를 구분한다. 중첩 설계의 ANOVA 모형, 제곱합 분해, F 검정 구성 방법을 다루며, 분산 성분 추정 방법을 소개한다. 언어·기억 연구에서 자극 또는 재료를 무선 요인으로 처리하는 Clark(1973)의 관행을 언급한다. 편의 표본(convenience sample)으로 수준을 선정한 경우 무선 요인 처리의 적절성에 대한 논쟁을 다룬다.

### Ch 11: One-Way Within-Subjects Designs: Univariate (pp. 525-572)

**핵심**: 반복 측정 설계의 일변량 접근(혼합 모형)을 다룬다. 상관 오차 문제, 구형성(sphericity) 가정, 조정된 검정(Greenhouse-Geisser, Huynh-Feldt), 순서효과, 라틴 스퀘어 설계를 포함한다.

**키워드**: `repeated measures`, `sphericity`, `Greenhouse-Geisser`, `Latin square`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 11 (line 44857)
이 장은 반복 측정(within-subjects) 설계의 일변량 분석을 소개하며, 실험 설계의 두 번째 주요 구성 요소를 다룬다. 각 피험자가 여러 조건에서 측정되는 세 가지 상황(다중 처치 조건, 다중 검사, 시간에 따른 반복 측정)을 구분한다. 피험자 내 설계의 장점으로 개인차 제거를 통한 오차 분산 감소와 적은 피험자 수로 높은 검정력 달성을 설명한다. 두 수준 설계에서 상관된 오차(correlated errors) 문제를 제기하며, 차이 점수(difference scores) 접근이 이를 해결함을 보여준다. 피험자 요인을 추가 요인으로 다루는 혼합 모형(mixed model) ANOVA의 구조와 오차항 선택 원리를 설명한다. 세 수준 이상 설계에서 구형성(sphericity) 가정의 필요성과 Mauchly 검정을 통한 진단 방법을 다룬다. 구형성 위반 시 Greenhouse-Geisser와 Huynh-Feldt ε 조정 방법의 원리와 장단점을 비교한다. 순서효과(order effects)와 이월효과(carryover effects)의 위험, 이를 통제하기 위한 역균형화(counterbalancing)와 라틴 스퀘어 설계를 소개한다. 피험자 내 설계와 피험자 간 설계의 검정력 비교 공식을 제시하며, 설계 선택의 실질적 고려사항을 논의한다. 다변량 접근(Ch 13)이 구형성 가정을 요구하지 않는 대안임을 예고한다.

### Ch 12: Higher-Order Within-Subjects: Univariate (pp. 573-623)

**핵심**: 이원 이상의 피험자 내 설계와 분할 구획 설계(split-plot design)의 일변량 분석을 다룬다. 단순효과, 상호작용 대비, 가정 검토, 조정 검정을 포함한다.

**키워드**: `split-plot design`, `within-subjects factorial`, `mixed design`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 12 (line 49421)
이 장은 Ch 11의 혼합모형 방법론을 이원 이상의 요인을 포함하는 피험자 내 및 혼합 설계로 확장한다. 지각 심리학 실험(소음×각도) 데이터를 예제로 2×3 피험자 내 설계의 분석을 동기부여한다. 피험자 요인을 세 번째 요인으로 포함하여 삼원 설계와 동일한 모형 구조를 갖추며, 7개 효과의 제곱합과 자유도를 도출한다. 각 효과에 대한 적절한 오차항 선택이 기대 평균 제곱에 의해 결정되며, 주효과 A는 A×S, 주효과 B는 B×S, 상호작용 AB는 AB×S를 오차항으로 사용함을 설명한다. 분할 구획 설계(split-plot design)에서 피험자 간 요인과 피험자 내 요인이 혼합된 경우의 오차항 선택 규칙을 다룬다. 구형성 가정의 확장과 각 효과별 ε 조정 적용 방법을 설명한다. 단순효과, 상호작용 대비 등 후속 분석의 실행 방법과 적절한 오차항 선택을 다룬다. 혼합 설계에서 피험자 간 요인 검정에는 구형성 가정이 불필요하나, 피험자 내 요인 관련 효과에는 필요함을 구분한다. 다변량 접근(Ch 14)이 이러한 제한적 가정을 요구하지 않는 대안임을 예고한다. Ch 7, 8의 해석 논리가 요인 유형에 관계없이 동일하게 적용됨을 강조한다.

### Ch 13: One-Way Within-Subjects: Multivariate (pp. 624-681)

**핵심**: 반복 측정의 다변량 접근을 다룬다. D 변수 형성, 다변량 검정 통계량, 대비 검정, 일변량과 다변량 접근의 비교(가정, 제1종 오류율, 검정력)를 포함한다.

**키워드**: `multivariate approach`, `D variables`, `Wilks lambda`, `power comparison`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 13 (line 54426)
이 장은 반복 측정 설계의 다변량(multivariate) 접근을 소개하며, 구형성 가정을 요구하지 않는 대안을 제시한다. 두 수준 설계에서 차이 점수(D 변수)를 형성하여 단일 표본 t 검정(또는 동등한 F 검정)을 수행하는 방법을 복습한다. 세 수준 설계에서는 a-1개의 D 변수가 필요하며, 인접 시점 간 차이(D₁ = Y₂ - Y₁, D₂ = Y₃ - Y₂)를 형성하는 방법을 설명한다. 옴니버스 검정은 모든 D 변수의 모집단 평균이 동시에 0인지를 다변량으로 검정하며, Hotelling의 T² 통계량을 사용한다. Wilks의 λ, Pillai의 trace, Roy의 최대근 등 다변량 검정 통계량의 의미와 관계를 다룬다. D 변수의 선택이 검정 결과에 영향을 미치지 않음을 증명하며, 직교 대비에 기반한 D 변수도 동일한 결과를 산출함을 보여준다. 개별 대비 검정에서는 단일 D 변수에 대한 t 검정을 사용하며, 다중 비교 보정의 적용을 논의한다. 일변량 접근과 다변량 접근의 비교에서 가정의 차이, 제1종 오류율, 검정력의 상대적 장단점을 분석한다. 구형성이 심하게 위반될 때 다변량 접근이 유리하고, 표본 크기가 작거나 구형성이 충족될 때 일변량 접근이 더 높은 검정력을 가질 수 있음을 논의한다. ε 조정 접근보다 다변량 접근을 일반적으로 선호하는 이유를 제시한다.

### Ch 14: Higher-Order Within-Subjects: Multivariate (pp. 682-762)

**핵심**: 복잡한 피험자 내/간 요인 설계의 다변량 분석을 다룬다. 주효과와 상호작용에 대한 D 변수 형성, 분할 구획 설계의 다변량 처리를 포함한다.

**키워드**: `multivariate factorial`, `split-plot multivariate`, `D variables formation`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 14 (line 60952)
이 장은 Ch 13의 다변량 방법론을 복잡한 요인 설계(이원 이상 피험자 내 및 혼합 설계)로 확장한다. 2×2 피험자 내 설계(소음×각도)를 예제로, 주효과와 상호작용 각각에 대응하는 D 변수를 형성하는 방법을 상세히 설명한다. 주효과 D 변수는 해당 요인의 수준별 평균 차이를 각 피험자에 대해 계산하며, 상호작용 D 변수는 한 요인의 효과가 다른 요인의 수준에 따라 달라지는 정도를 반영한다. 각 D 변수에 대한 단일 표본 t 검정(또는 F 검정)으로 개별 효과를 검정하며, 이는 Ch 7의 해석 논리와 일관된다. 일반적인 a×b 설계로의 확장에서 주효과에는 a-1 또는 b-1개, 상호작용에는 (a-1)(b-1)개의 D 변수가 필요함을 설명한다. 분할 구획 설계(split-plot design)에서 피험자 간 요인은 D 변수에 대한 독립 표본 비교로, 피험자 내 요인과 상호작용은 D 변수에 대한 다변량 검정으로 처리한다. 혼합모형 접근과 다변량 접근의 비교에서 가정, 검정력, 결측치 처리의 차이를 논의한다. 세 요인 이상의 복잡한 설계에서 D 변수 형성의 체계적 원리를 제시한다. 다변량 접근이 구형성 가정에 의존하지 않는 장점을 재강조하며, 결측치가 있는 경우 Ch 15의 다층모형이 대안이 됨을 예고한다.

### Ch 15: Multilevel Models for Within-Subjects (pp. 763-827)

**핵심**: 종단 데이터를 위한 다층 모형(multilevel model)을 소개한다. 무선효과 모형, 최대우도 추정, ANOVA 혼합모형과의 비교, 성장 곡선 모형, 공분산 행렬 구조를 다룬다.

**키워드**: `multilevel model`, `random effects`, `maximum likelihood`, `growth curve`, `longitudinal`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 15 (line 67660)
이 장은 종단 데이터 분석을 위한 다층 모형(multilevel model)을 소개하며, ANOVA 혼합모형에서 최대우도 접근으로의 전환을 다룬다. 다층 모형의 세 가지 주요 장점으로 상관 모형화의 유연성, 결측치 처리 능력, 범주형 및 연속형 예측 변수의 동시 수용을 제시한다. McCarthy 인지 발달 데이터(12명 아동, 4개 연령)를 예제로 ANOVA 혼합모형을 복습하고, 이를 다층 모형으로 재구성한다. 고정 효과와 무선 효과를 구분하는 일반 선형 혼합 모형(Y = Xβ + Zu + ε)의 구조를 설명한다. ANOVA 접근은 모든 모수를 추정한 후 마지막에 고정·무선을 구분하지만, 최대우도 접근은 처음부터 무선 효과의 분산을 직접 추정한다. 제한 최대우도(REML) 추정의 원리와 ANOVA 추정과의 균등 셀 크기에서의 동치 관계를 보여준다. 성장 곡선 모형(growth curve model)에서 무선 절편과 무선 기울기의 의미와 추정을 다룬다. 공분산 행렬 구조(복합 대칭, 비구조적, 1차 자기회귀 등)의 선택과 모형 비교(우도비 검정, AIC, BIC)를 논의한다. 불균등 시점 간격, 시변 공변량(time-varying covariate), 시불변 공변량(time-invariant covariate)의 포함 방법을 설명한다. 결측치가 MAR(missing at random) 조건에서 다층 모형이 유효한 추론을 제공함을 강조한다.

### Ch 16: Multilevel Hierarchical Mixed Models: Nested (pp. 828-867)

**핵심**: 중첩 설계를 위한 다층 계층적 혼합 모형을 다룬다. ANOVA 접근과 최대우도 접근의 비교, 불균형 설계, 2수준 변수 추가, 1수준 변수 추가를 포함한다.

**키워드**: `hierarchical model`, `nested design`, `level-1 predictor`, `level-2 predictor`

**상세**: → `Scott E. Maxwell, Harold D. Delaney - Designing Experiments and Analyzing Data_ A Model Comparison Perspective-Routledge Academic (2004).md` Ch 16 (line 73370)
이 장은 중첩 설계를 위한 다층 계층적 혼합 모형을 소개하며, Ch 10의 ANOVA 접근과 최대우도 접근을 비교한다. 임상 수련생의 내담자 심각도 평정 데이터(남녀 수련생 각 3명, 내담자 각 4명)를 예제로 사용한다. ANOVA 접근에서 성별 효과 검정 시 MS_{B/A}를 오차항으로 사용하는 원리를 복습하며, 균등 셀 크기에서 두 접근이 동일한 결과를 산출함을 확인한다. 최대우도 접근은 고정 효과(성별)와 무선 효과(수련생)를 모형 구성 초기부터 구분하며, 무선 효과의 분산을 직접 추정한다. 불균형 설계(불균등 셀 크기)에서 ANOVA 접근의 기대 평균 제곱 표현이 비유일적이 되는 문제를 최대우도 접근이 해결함을 설명한다. 2수준 변수(학생 수준 예측 변수) 추가 시 교실 간 변동을 설명하는 방법을 다루며, 이는 ANCOVA의 다층적 확장에 해당한다. 1수준 변수(개인 수준 공변량) 추가와 무선 기울기 모형으로의 확장 가능성을 논의한다. 정규성 가정의 구현에서 ANOVA와 최대우도 접근의 차이점을 설명한다. 모형 비교를 위한 우도비 검정, AIC, BIC의 사용법을 다루며, 중첩 구조가 분석에 반영되지 않을 경우 발생하는 편향을 경고한다. 이 장이 개념적 기초를 제공하며, 심화 학습을 위한 참고문헌을 안내한다.
