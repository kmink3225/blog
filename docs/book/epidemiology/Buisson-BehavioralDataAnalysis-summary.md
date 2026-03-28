---
name: "Behavioral Data Analysis with R and Python"
type: book-summary
sources:
  - file: "Buisson-BehavioralDataAnalysis_azure_full.md"
    tool: Document Intelligence
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
이 장은 인과-행동 프레임워크(causal-behavioral framework)를 소개하며, 행동·인과 다이어그램·데이터의 삼각 구조를 제시한다. 분석의 세 유형인 기술적·예측적·인과적 분석을 구분하고, 인간 행동이 다원적 원인·맥락 의존성·비결정성·혁신성·전략성을 지녀 예측 분석만으로는 부족함을 설명한다. 차원의 저주와 Lucas 비판을 통해 외삽의 위험성을 수학적으로 논증한다. C-Mart 아이스크림 판매 사례로, 여름 방학이라는 교란 변수가 온도-판매 관계를 왜곡하는 현상을 시연한다. 변수를 무분별하게 추가하면 다중공선성이 발생하여 회귀 계수가 불안정해짐을 아이스드커피 변수 추가 사례로 보여준다. 또한 충돌 변수(collider)에 대한 조건부 분석이 실제로 존재하지 않는 상관을 만들어내는 바닐라-초콜릿 선호도 사례를 제시한다. 예측 분석과 인과 분석의 회귀 사용 목적 차이를 명확히 하고, 인과 분석에서는 계수의 정확성이 핵심임을 강조한다. 이를 통해 행동 데이터 분석에서 인과적 접근이 필수적인 이유를 종합적으로 제시한다.

### Ch 2: Understanding Behavioral Data (pp. 19-35)

**핵심**: 인간 행동의 기본 모형(개인 특성, 인지/감정, 의도, 행동)을 제시하고, 행동 데이터와의 연결 방법을 다룬다. 행동적 무결성(behavioral integrity) 마인드셋과 데이터 검증 방법을 소개한다.

**키워드**: `behavioral model`, `personal characteristics`, `cognition`, `behavioral integrity`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 2 (line 2452)
이 장은 인간 행동의 기본 모형을 개인 특성, 인지/감정, 의도, 행동, 비즈니스 행동의 다섯 가지 구성요소로 제시한다. 개인 특성은 인구통계 변수 외에 성격 특질과 생활 습관까지 포함하며, 이들이 인과 모형에서 1차 원인으로 기능하는 방식을 설명한다. 인지와 감정은 고객 만족도(CSAT)나 고객 경험(CX) 같은 비즈니스 개념을 포함하며, UX 연구와 행동과학의 관점 차이를 논의한다. 의도-행동 간극(intention-action gap)의 중요성을 강조하고, 행동 변수가 관찰 가능·개별적·원자적이어야 한다는 기준을 제시한다. 비즈니스 행동은 커뮤니케이션, 규칙, 개별 결정 등을 포함하며, 데이터 수집의 어려움과 고객 행동 해석에 미치는 영향을 다룬다. AirCnC 사례를 통해 행동적 무결성(behavioral integrity) 마인드셋을 소개하고, 변수를 의심하고 검증하는 접근을 권장한다. 변수의 행동 범주를 식별하고 행동 변수를 정제하는 구체적 방법을 제시하며, 빈도·지속시간·인접성 같은 시간적 정보의 활용을 다룬다. 고객 참여(engagement)의 이중 의미를 분석하여, 행동적 참여와 감정적 참여의 혼동이 초래하는 문제를 지적한다.

### Ch 3: Introduction to Causal Diagrams (pp. 39-61)

**핵심**: 인과 다이어그램의 기본 구조(chain, fork, collider)를 소개한다. 변수의 분할/집계, 순환(cycle), 경로(path) 개념을 다루며, 인과 다이어그램이 행동과 데이터를 동시에 표현하는 방법을 설명한다.

**키워드**: `causal diagram`, `chain`, `fork`, `collider`, `path`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 3 (line 3363)
이 장은 인과 다이어그램(CD)이 행동과 데이터를 동시에 표현하는 도구임을 설명하며, 인과-행동 프레임워크의 세 꼭짓점 중 하나로 위치시킨다. CD의 기본 요소인 사각형(관찰 변수)과 화살표(인과 관계), 그리고 음영 사각형(미관찰 변수)의 표기법을 소개한다. CD가 행동에 대한 직관과 믿음을 표현하며, 주관성이 약점이 아니라 불확실성을 명시화하는 장점임을 논증한다. 선형 회귀와 CD의 수학적 대응 관계를 설명하고, 로지스틱 회귀 같은 일반화 선형 모형에도 CD 논리가 적용됨을 보인다. 체인(chain) 구조를 소개하며, 부모-자식·조상-후손 관계와 매개 변수(mediator)의 개념을 정의한다. 체인의 축소(collapsing)와 확장(expanding)을 통해 CD를 단순화하거나 상세화하는 방법을 시연한다. 포크(fork) 구조에서 공통 원인이 만드는 비인과적 상관을 설명하고, 미지의 공통 원인을 양방향 화살표로 표현하는 관례를 제시한다. 충돌 변수(collider)는 두 원인의 공통 결과로서, 포크와 대칭적 문제를 일으킴을 설명한다. 세 변수가 체인·포크·충돌 변수를 동시에 포함할 수 있음을 C-Mart 사례로 보여주며, CD의 분할·집계·순환·경로 개념까지 다룬다.

### Ch 4: Building Causal Diagrams from Scratch (pp. 63-90)

**핵심**: 비즈니스 문제에서 출발하여 인과 다이어그램을 단계적으로 구축하는 방법을 다룬다. 관심 관계 파악, 후보 변수 식별, 데이터 기반 검증, 반복적 확장 및 단순화 과정을 실습한다.

**키워드**: `diagram construction`, `variable selection`, `iterative refinement`, `proxy variable`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 4 (line 4672)
이 장은 비즈니스 문제로부터 인과 다이어그램을 단계적으로 구축하는 실용적 방법론을 제시한다. 호텔 예약 데이터셋을 활용하여 "환불 불가 보증금(NRDeposit)이 취소율에 미치는 인과적 영향"이라는 질문을 CD로 표현한다. 관심 관계를 먼저 설정한 뒤, 행동·의도·인지와 감정·개인 특성·비즈니스 행동·시간 추세의 범주별로 후보 변수를 체계적으로 식별한다. 과거 행동(PreviousCancellation, IsRepeatedGuest)을 프록시 변수로 활용하는 방법과, 여행 목적·취소 사유 같은 미관찰 의도 변수의 중요성을 강조한다. 고객의 보증금 이해 여부, 매몰비용 편향 같은 인지적 요인과 성실성·신경증 같은 성격 특질을 CD에 통합하는 과정을 보여준다. 인구통계 변수는 행동적 특성의 프록시로서 가치가 있으며, 재정 특성과 연결되는 방식을 설명한다. 비즈니스 규칙이 CD에 명시적 또는 매개 변수 형태로 반영되어야 함을 논의한다. 데이터 기반 검증 방법으로 Cramer's V 등 상관 분석과 VIF 진단을 활용하며, CD를 반복적으로 확장·단순화하는 과정을 실습한다. 최종적으로 CD가 비즈니스 목표에 부합하는지를 유일한 평가 기준으로 삼아야 함을 강조한다.

### Ch 5: Using Causal Diagrams to Deconfound Data Analyses (pp. 91-103)

**핵심**: 분리적 원인 기준(disjunctive cause criterion)과 백도어 기준(backdoor criterion)을 이용한 교란 제거 방법을 설명한다. 아이스크림과 생수 판매 사례를 통해 두 기준의 적용을 시연한다.

**키워드**: `deconfounding`, `disjunctive cause criterion`, `backdoor criterion`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 5 (line 6437)
이 장은 인과 다이어그램에서 교란을 제거하기 위한 두 가지 결정 규칙을 제시한다. C-Mart의 아이스크림-생수 판매 관계를 분석하는 비즈니스 사례를 설정하고, CD를 개념적 블록으로 분해하여 분석하는 방법을 보여준다. 분리적 원인 기준(DCC)은 관심 변수의 직접 원인(매개 변수 제외)을 모두 회귀에 포함하면 교란이 제거됨을 보장하는 충분 조건이다. DCC의 장점은 적용이 단순하고 CD에 오류가 있어도 작동한다는 점이며, 단점은 불필요한 변수를 포함하여 데이터 요구량이 증가한다는 것이다. 백도어 기준(BC)은 경로(path), 인과 경로, 비인과 경로, 차단/비차단 경로의 개념을 정의하고, 비인과적 비차단 경로를 모두 차단하면 교란이 제거됨을 보인다. BC는 정확한 CD를 전제하지만 필요충분 조건으로서 최소한의 통제 변수만 요구한다. M-패턴(두 포크 사이의 충돌 변수)에서 충돌 변수를 회귀에 포함하면 오히려 교란이 생성됨을 보여준다. 담배 소송 사례를 인용하여 안전벨트 착용을 통제했을 때 흡연-폐암 관계가 편향된 실제 사례를 제시한다. 두 기준의 장단점을 비교하며, 상황에 따라 적절한 규칙을 선택할 것을 권고한다.

### Ch 6: Handling Missing Data (pp. 107-146)

**핵심**: 결측 데이터의 시각화, 진단(MCAR/MAR/MNAR), 그리고 다중 대체(multiple imputation) 기법을 다룬다. PMM, 정규분포 대체, 보조 변수 추가, 대체 데이터셋 수 결정 등 실무적 방법을 R과 Python으로 구현한다.

**키워드**: `missing data`, `MCAR`, `MAR`, `MNAR`, `multiple imputation`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 6 (line 7171)
이 장은 결측 데이터의 유형 분류와 처리 방법을 체계적으로 다룬다. AirCnC 설문 시뮬레이션 데이터를 사용하여, 결측 패턴을 시각화하는 방법(R의 mice 패키지 md.pattern 함수)을 소개한다. 결측의 양이 분석 결과에 실질적 영향을 미치는지를 판단하는 실용적 기준(최솟값/최댓값 대체 후 회귀 비교)을 제시한다. 결측 상관(correlation of missingness)을 통해 변수 간 결측 패턴의 관계를 파악하는 이변량 시각화를 수행한다. Donald Rubin의 결측 분류 체계인 MCAR(완전 무작위 결측), MAR(조건부 무작위 결측), MNAR(비무작위 결측)을 정의하고 진단 방법을 설명한다. MCAR은 완전 사례 분석이 가능하고, MAR은 다중 대체(multiple imputation)로 처리할 수 있으며, MNAR은 보조 변수 추가를 통해 MAR로 전환할 수 있음을 보인다. 다중 대체의 핵심 기법인 PMM(예측 평균 매칭)과 정규분포 대체를 R과 Python 코드로 구현한다. 대체 데이터셋 수 결정 방법과 보조 변수(auxiliary variable) 추가의 효과를 실습하며, 결측 처리가 회귀 계수의 편향에 미치는 영향을 비교 분석한다.

### Ch 7: Measuring Uncertainty with the Bootstrap (pp. 147-169)

**핵심**: 부트스트랩의 원리와 신뢰구간 구성 방법을 소개한다. 표본 평균, 임의 통계량, 회귀분석에 대한 부트스트랩 적용과 전통적 방법 대비 부트스트랩의 장단점을 다룬다.

**키워드**: `bootstrap`, `confidence interval`, `resampling`, `uncertainty`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 7 (line 11065)
이 장은 부트스트랩의 원리와 적용을 소개하며, 소표본이나 비정규 데이터에서 전통적 방법이 실패하는 경우의 대안을 제시한다. C-Mart 케이크 제조 시간 데이터(10개 관측값, 이상치 포함)로, 전통적 95% 신뢰구간이 음수 구간을 포함하는 비현실적 결과를 만드는 문제를 보여준다. 부트스트랩은 원본 표본에서 복원 추출을 반복하여 다수의 가상 데이터셋을 생성하고, 각 데이터셋의 통계량 분포에서 경험적 신뢰구간을 구성한다. 부트스트랩 표본 수에 대한 가이드라인(중심 추정치 100~200개, 90%-CI 1,000~2,000개, 99%-CI 5,000개)을 제시한다. 임의 통계량(180분 초과 비율)에 대한 부트스트랩 CI 구성법을 보여주며, 이는 전통적 방법으로 불가능한 분석이다. 회귀 분석에 부트스트랩을 적용하여 경험-제조시간 관계의 계수와 부트스트랩 p-값을 산출하고, 전통적 p-값(0.16) 대비 부트스트랩 p-값(0.04)이 더 정확함을 보인다. 부트스트랩 CI의 비대칭 형태가 이상치의 존재와 부재를 데이터 기반 시나리오 분석으로 반영함을 설명한다. 부트스트랩 사용 시기에 대한 결정 트리를 제공하며, 전통적 방법이 적절한 경우와 부트스트랩이 필수적인 경우를 구분한다.

### Ch 8: Experimental Design: The Basics (pp. 173-202)

**핵심**: 변화 이론(theory of change)에 기반한 실험 계획, 무작위 배정, 표본 크기/검정력 분석, 실험 결과 분석 및 해석의 전 과정을 다룬다.

**키워드**: `experimental design`, `randomization`, `power analysis`, `sample size`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 8 (line 12475)
이 장은 변화 이론(Theory of Change)에 기반한 실험 계획, 무작위 배정, 표본 크기 분석, 결과 해석의 전 과정을 다룬다. AirCnC의 1-클릭 예약 버튼 실험을 사례로, 비즈니스 목표(매출 증대), 목표 지표(예약 확률), 개입(1-클릭 버튼), 행동 논리(예약 과정 단축)를 CD로 연결한다. 목표 지표 선택 시 재무 지표와 선행 지표 간의 트레이드오프, 다중 지표 사용의 위양성 위험, OEC(Overall Evaluation Criterion)의 한계를 논의한다. 개입 정의의 구체성 중요성을 강조하며, 작은 개입 테스트를 먼저 수행할 것을 권장한다. 무작위 배정의 시점(배정 타이밍)과 수준(방문·예약·계정 수준)을 결정하는 실무적 고려사항을 다룬다. 표본 크기와 검정력 분석의 기본 통계 이론(진양성·위양성·위음성·진음성)을 비즈니스 의사결정 맥락에서 설명한다. 최소 탐지 효과(MDE)와 통계적 유의성의 전통적 기준(5%, 80%)을 소개하고, 비즈니스 의사결정에 맞게 조정하는 방법을 논의한다. 부트스트랩 시뮬레이션을 이용한 검정력 분석 대안을 제시하며, 실험 결과 분석에서 부트스트랩 CI와 p-값을 활용하는 방법을 설명한다.

### Ch 9: Stratified Randomization (pp. 203-232)

**핵심**: 층화 무작위 배정의 원리와 구현, 부트스트랩 시뮬레이션을 이용한 검정력 분석을 다룬다. ITT(intention-to-treat)와 CACE(complier average causal estimate) 추정을 설명한다.

**키워드**: `stratified randomization`, `intention-to-treat`, `CACE`, `power simulation`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 9 (line 14256)
이 장은 층화 무작위 배정의 원리와 구현, 부트스트랩 시뮬레이션을 이용한 검정력 분석을 다룬다. AirCnC의 두 가지 소유주 정책(무료 청소 서비스 vs. 최소 예약 기간) 실험을 사례로 사용하며, 경쟁하는 비즈니스 제안 간 실험적 비교의 실무적 어려움을 논의한다. OEC(Overall Evaluation Criterion)의 한계를 네 가지 관점(전략적 주관성, 선형성 가정, 고정된 개입, 미측정 교환비율)에서 비판하고, 단일 목표 지표와 가드레일 지표의 조합을 권장한다. 표준 무작위 배정이 소표본에서 그룹 간 불균형을 초래하는 문제를 설명하고, 층화(stratification)를 통해 유사한 개체 쌍을 만들어 균형을 보장하는 방법을 제시한다. 거리(distance) 개념을 활용하여 수치 변수의 재척도화와 범주 변수의 원-핫 인코딩을 수행하고, R의 blockTools와 Python의 유사 함수로 매칭을 구현한다. 부트스트랩 시뮬레이션으로 검정력 분석을 수행하며, 층화 배정이 검정력을 크게 향상시킴을 보인다. ITT(intention-to-treat) 분석과 CACE(complier average causal estimate) 추정의 차이를 설명하고, 순응하지 않는 대상에 대한 처리 방법을 논의한다.

### Ch 10: Cluster Randomization and Hierarchical Modeling (pp. 233-252)

**핵심**: 군집 무작위 배정 실험 설계와 계층적 모형(hierarchical model)을 소개한다. R과 Python을 이용한 계층 모형 구현, 무작위 배정, 검정력 분석, 실험 분석 방법을 다룬다.

**키워드**: `cluster randomization`, `hierarchical model`, `mixed effects`, `ICC`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 10 (line 16121)
이 장은 군집 무작위 배정 실험과 계층적 모형(hierarchical model)을 소개한다. AirCnC 콜센터의 SOP(표준 운영 절차) 변경 실험을 사례로, 개인 수준이 아닌 콜센터 수준에서 무작위 배정이 필요한 이유를 설명한다. 순응(compliance) 문제와 그룹 간 누출(leakage) 위험을 다루며, 이를 완화하기 위한 파일럿 연구와 순응 측정의 중요성을 강조한다. 중첩된 범주형 변수(콜센터-상담원)가 있을 때 표준 선형 회귀의 다중공선성 문제를 설명하고, 계층적 모형이 이를 해결하는 방식을 소개한다. R의 lmer() 함수와 Python의 mixedlm() 함수를 사용한 계층적 모형 구현을 시연하며, 랜덤 효과(random effects)와 고정 효과(fixed effects)의 해석 방법을 다룬다. 범주형 변수와 계층적 모형의 해석적 차이(고유한 그룹 차이 vs. 무한 분포에서의 무작위 추출)를 설명한다. 층화 무작위 배정을 콜센터 수준에서 적용하는 방법과, 10개 콜센터만으로 검정력을 확보하기 위한 시뮬레이션 기반 검정력 분석을 수행한다. ICC(급내상관계수)의 개념과 군집 실험에서의 검정력 저하 문제를 다룬다.

### Ch 11: Introduction to Moderation (pp. 257-295)

**핵심**: 조절 효과(moderation)의 행동적 유형(세분화, 상호작용, 비선형성)을 설명한다. 조절 효과의 적용 시점과 방법, 다중 조절 변수, 부트스트랩을 이용한 검증을 다룬다.

**키워드**: `moderation`, `segmentation`, `interaction`, `nonlinearity`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 11 (line 17840)
이 장은 조절 효과(moderation)의 세 가지 행동적 유형인 세분화(segmentation), 상호작용(interaction), 비선형성(nonlinearity)을 설명한다. C-Mart 놀이 공간-방문 시간 사례로, 자녀 유무가 놀이 공간의 효과를 조절하는 세분화 분석을 시연한다. 회귀에서 상호작용 항(PlayArea * Children)의 계수 해석과 시각적 표현(비평행 선)을 다룬다. 실험 데이터에서의 리프트(uplift) 분석 개념을 소개하며, 높은 성향(propensity)과 높은 효과(uplift)의 차이를 구분한다. 대칭적 상호작용(놀이 공간 × 라운지 공간)의 CD 표현과 해석을 다루고, 비선형성을 자기 조절(self-moderation)로 재해석하는 방법을 제시한다. 이차항을 이용한 비선형 관계의 회귀 표현과 R/Python 코드(I() 함수)를 시연한다. 조절 효과 탐색 시 위양성 위험을 강조하며, 실험 설계 단계와 데이터 분석 단계에서의 조절 효과 분석 전략을 구분하여 제시한다. 조절 효과 측정을 위한 실험은 주효과 실험 대비 10~20배 이상의 표본이 필요하므로, 먼저 주효과를 확인한 뒤 별도 실험을 설계할 것을 권장한다. 다중 조절 변수와 부트스트랩을 이용한 CI 검증 방법을 포함한다.

### Ch 12: Mediation and Instrumental Variables (pp. 297-315)

**핵심**: 매개 효과(mediation)를 통한 인과 메커니즘 이해와 측정 방법을 다룬다. 도구변수(instrumental variable)의 개념, 적용, FAQ를 비즈니스 맥락에서 설명한다.

**키워드**: `mediation`, `causal mechanism`, `instrumental variable`, `2SLS`

**상세**: → `Florent Buisson - Behavioral Data Analysis with R and Python_ Customer-Driven Data for Real Business Results-O'Reilly Media (2021).md` Ch 12 (line 20016)
이 장은 매개 효과(mediation)를 통한 인과 메커니즘 이해와 도구변수(instrumental variable)를 다룬다. C-Mart 놀이 공간이 식료품 구매에 미치는 효과를 방문 시간이 매개하는 사례로, 매개 분석의 두 가지 이점(메커니즘 이해와 편향 방지)을 설명한다. 총효과(total effect), 매개 효과(indirect effect), 직접 효과(direct effect)를 분리하는 세 단계 회귀 절차를 시연한다. 매개 효과의 비율(약 99.5%)을 산출하고, 완전 매개와 부분 매개를 구분하는 방법을 제시한다. 매개 변수가 이항 변수인 경우 로지스틱 회귀를 사용한 매개 효과 산출의 복잡성과 해결책을 논의한다. 매개 분석이 조절 효과 분석과 결합되어 행동적 통찰(폐점 시간 근처의 약화 효과)을 생성하는 방법을 보여준다. 도구변수는 완전 매개 관계에서 교란된 관계의 비편향 추정치를 얻는 도구로, AirCnC의 CSAT→M6Spend 관계에서 실험 배정(Group)을 도구변수로 활용한다. 2SLS(2단계 최소자승법)의 원리와 R(ivreg)·Python(IV2SLS) 구현을 다루며, 도구변수의 세 가지 조건과 FAQ를 비즈니스 맥락에서 설명한다.
