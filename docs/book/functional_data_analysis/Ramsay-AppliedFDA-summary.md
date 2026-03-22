---
name: "Applied Functional Data Analysis: Methods and Case Studies"
type: book-summary
source_file: "Ramsay-AppliedFDA_azure_full.md"
authors: "J. O. Ramsay, B. W. Silverman"
year: 2002
total_pages: 190
language: en
keywords: [functional data analysis, case study, criminology, growth curve, handwriting, bone shape, PCA, registration, differential equation, juggling]
---

# Applied Functional Data Analysis: Methods and Case Studies — Summary

> J. O. Ramsay, B. W. Silverman (2002), 190 pages, 12 chapters
> 다양한 분야의 사례 연구를 통해 함수 데이터 분석의 아이디어와 방법을 실제 적용 관점에서 소개하는 보완서

## Contents

1. Introduction (p.1)
2. Life Course Data in Criminology (p.17)
3. The Nondurable Goods Index (p.41)
4. Bone Shapes from a Paleopathology Study (p.57)
5. Modeling Reaction-Time Distributions (p.69)
6. Zooming in on Human Growth (p.83)
7. Time Warping Handwriting and Weather Records (p.101)
8. How Do Bone Shapes Indicate Arthritis? (p.115)
9. Functional Models for Test Items (p.131)
10. Predicting Lip Acceleration from Electromyography (p.145)
11. The Dynamics of Handwriting Printed Characters (p.157)
12. A Differential Equation for Juggling (p.171)

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-16)

**핵심**: 함수 데이터를 왜 고려해야 하는지 설명하고, 12개 사례 연구를 개괄적으로 소개한다. 범죄학, 경제학, 고고학, 류마티스학, 성장 분석, 생체역학, 교육학 등 다양한 분야에서의 FDA 적용 가능성을 제시한다.

**키워드**: `functional data`, `case studies`, `overview`, `interdisciplinary`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 1 (line 1010)

함수 데이터는 관측값이 곡선이나 함수의 형태를 취하는 데이터로, 종단 데이터, 밀도 함수, 공간 곡선, 형태(shape) 등 다양한 형태로 나타난다. 12개 사례 연구를 통해 범죄학, 경제학, 고고학, 심리학, 성장 분석, 생체역학, 교육학, 기상학 등에서의 FDA 적용 가능성을 개괄한다. 범죄학 사례에서는 413명의 25년간 범죄 기록을 함수로 변환하고, 비내구재 지수 사례에서는 위상 평면 그림(phase-plane plot)으로 경기 순환을 분석한다. 뼈 형태 사례에서는 고고학적 대퇴골의 윤곽 곡선을 PCA로 분석하고, 반응 시간 사례에서는 밀도 함수를 함수 데이터로 취급한다. 성장 데이터 사례에서는 키, 속도, 가속도의 세 스케일에서 성장 패턴을 분석하며, 필기 사례에서는 시간 변환(time warping)을 통한 등록을 다룬다. 미분 방정식 기반 모형이 필기 동역학과 저글링 분석에 적용되며, 이는 FDA의 고유한 도구이다. 입술 가속도와 근전도 사례에서는 과거 이력(historical) 모형을 통한 함수 회귀를 소개한다. 검사 문항 분석에서는 능력 공간 곡선과 문항 반응 함수의 함수적 모형화를 제시한다. 이 책의 목표는 독자가 함수적 사고방식(functional thinking)을 습득하도록 돕는 것이다. 웹 사이트를 통해 데이터와 분석 코드를 제공하며, MATLAB과 S-PLUS에서의 구현을 지원한다.

### Ch 2: Life Course Data in Criminology (pp. 17-40)

**핵심**: 범죄학 생애과정(life course) 데이터를 함수적 접근으로 분석한다. 이산 값을 함수 데이터로 변환, 평균 추정, 평활화된 함수 PCA, 주성분 점수의 상세 분석, 기저 전개와 교차 검증을 다룬다.

**키워드**: `criminology`, `life course`, `functional PCA`, `basis expansion`, `cross-validation`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 2 (line 2059)

500명의 비행소년에 대한 Glueck 종단 연구 데이터를 기반으로 413명의 11세에서 35세까지 25년간 범죄 기록을 분석한다. 연간 체포 수의 제곱근을 선형 보간하여 각 개인의 범죄 활동 수준을 나타내는 함수 데이터로 변환한다. 제곱근 변환은 포아송 카운트에 대한 표준 분산 안정화 변환이며 분포의 비대칭성을 감소시킨다. 표본 평균 함수의 잡음을 제거하기 위해 roughness penalty 방법을 적용하며, 스무딩 모수 λ는 교차 검증으로 초기 선택 후 주관적으로 조정한다. 함수 PCA에서 주성분 가중 함수 ξ(t)에 대해 점수 zᵢ = ∫ξ(t)Yᵢ(t)dt를 계산하여 개인 간 변동의 주요 패턴을 추출한다. 평활화된 함수 PCA는 가중 함수 자체에 roughness penalty를 부과하여 더 해석 가능한 주성분을 산출한다. 주성분 점수의 히스토그램과 산점도를 통해 범죄 유형의 연속체적 특성과 잠재적 군집을 탐색한다. 특이한 점수를 가진 개인의 범죄 곡선을 상세 분석하여 소년 범죄자의 성인기 범죄 중단(desistance) 패턴을 식별한다. 기저 전개에서 기저 함수 수 M과 기저 유형의 선택이 분석 결과에 미치는 영향을 논의한다. 이 사례는 이산 값을 함수 데이터로 변환하고 함수 PCA를 적용하는 FDA의 전형적 워크플로우를 제시한다.

### Ch 3: The Nondurable Goods Index (pp. 41-56)

**핵심**: 비내구재 지수의 경기 순환을 위상 평면 그림(phase-plane plot)으로 분석한다. 데이터 변환과 스무딩, 4차 미분 roughness penalty, 스무딩 모수 선택을 다룬다.

**키워드**: `phase-plane plot`, `nondurable goods`, `business cycle`, `derivative smoothing`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 3 (line 3542)

미국 비내구재 제조업 지수는 1919년부터 2000년까지의 월별 경제 지표로, 식품, 의류, 연료 등 2년 내 소모되는 재화의 생산을 반영한다. 지수의 지수적 증가 경향과 변동성 비대칭을 해결하기 위해 로그 변환을 적용하며, 로그 지수의 연간 증가율은 약 1.6%이다. 로그 지수를 다항 스무딩 스플라인으로 평활화하여 연 내 3회 진동하는 계절 패턴을 식별하였다. 위상 평면 그림(phase-plane plot)은 속도(1차 도함수)와 가속도(2차 도함수)의 관계를 시각화하여 에너지 교환 패턴을 보여준다. 단순 조화 운동에서 위상 평면은 타원이며, 잠재 에너지와 운동 에너지의 교환이 순환적으로 나타난다. 경제적 맥락에서 잠재 에너지는 가용 자본과 자원에, 운동 에너지는 활발한 제조 활동에 대응한다. 4차 미분의 roughness penalty를 사용하여 2차 도함수 추정의 품질을 보장하며, 이는 가속도 분석에 필수적이다. 1929년 대공황과 제2차 세계대전 전후의 위상 평면 구조가 크게 변하며, 경제 체제 전환을 반영한다. 스무딩 모수 선택에서 GCV와 사후 변동 분석을 결합하여 미분 추정의 신뢰성을 평가한다. 이 장은 FDA에서 도함수의 활용이 원시 데이터에서 보이지 않는 동적 구조를 드러낼 수 있음을 보여준다.

### Ch 4: Bone Shapes from a Paleopathology Study (pp. 57-68)

**핵심**: 고병리학 연구에서 뼈 형태의 함수적 분석을 다룬다. 형태의 매개변수화, Procrustes 회전과 PCA, Varimax 회전, 관절염과의 임상적 관계를 탐색한다.

**키워드**: `bone shape`, `Procrustes rotation`, `shape PCA`, `paleopathology`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 4 (line 4476)

영국 Barton-upon-Humber의 St. Peter 교회에서 발굴된 약 2000구의 중세(1000-1500 CE) 골격 중 대퇴골의 무릎 관절 형태를 분석한다. 뼈의 2차원 영상에서 12개 랜드마크를 정의하여 형태를 매개변수화하며, 6개는 수동으로 4개는 수직 이등분선의 극점으로, 2개는 추가 세분으로 결정한다. Procrustes 변환으로 크기와 회전 변동을 제거한 후, 24개 랜드마크 좌표(x,y 각 12개)에 대해 표준 PCA를 수행한다. 제1주성분(21%)은 과간 홈(intercondylar notch)의 깊이와 상부 돌출 정도의 변동을, 제2주성분(18%)은 과(condyle)의 좁아짐과 홈의 확대를 나타낸다. 관절염 골과 대조 골의 주성분 점수 비교에서 제2주성분만이 유의한 차이(t=−3.01, p=0.0037)를 보였다. Varimax 회전을 적용하면 형태의 특정 부분에 집중된 더 해석 가능한 변동 모드가 산출되며, 회전 후 제2(과 두께)와 제3(슬개 홈 대칭) 성분에서 유의한 차이가 나타났다. 관절염 골은 평균적으로 두꺼운 과와 평평하고 대칭적인 슬개 홈을 가지는 경향이 있다. 형태와 골관절염 사이의 인과적 연결은 생체역학적 피드백 메커니즘(관절 안정화를 위한 뼈 리모델링)으로 설명될 수 있다. 순환 곡선으로서의 뼈 윤곽은 주기적 스플라인 보간을 통해 랜드마크로부터 복원된다. 이 사례는 2차원 형태 데이터가 함수 데이터의 한 형태임을 보여준다.

### Ch 5: Modeling Reaction-Time Distributions (pp. 69-82)

**핵심**: 반응 시간 분포의 비모수적 밀도 함수 모형화를 다룬다. 개인차 추정, 밀도 함수의 PCA를 통한 피험자 간 변동 탐색을 포함한다.

**키워드**: `reaction time`, `density estimation`, `nonparametric modeling`, `individual differences`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 5 (line 4938)

주의력 결핍 과잉행동 장애(ADHD) 아동의 반응 시간 분포를 비모수적 밀도 함수로 모형화한다. 17명의 ADHD 아동과 16명의 대조 아동 각각에 대해 약 70개의 반응 시간을 수집하여 개인별 밀도 함수를 추정한다. 반응 시간 분포는 120ms 이상의 사각 시간(dead time), 강한 양의 비대칭, 극단적 이상치 경향 등 표준 교과서 분포로 포착할 수 없는 특성을 보인다. 밀도 함수의 양수성과 적분 1 제약을 피하기 위해 p(t) = C·exp(W(t)) 변환을 사용하여, 제약 없는 함수 W(t)에 대해 분석을 수행한다. B-spline 기저와 roughness penalty를 결합한 최대 벌점 우도법으로 밀도를 추정하며, 매듭(knot) 배치는 데이터 분포에 맞게 조정한다. ADHD 집단과 대조 집단의 전체 밀도를 비교하면 ADHD 아동은 1초 이상의 반응 시간 비율이 현저히 높다. 로그 밀도 함수 W(t)에 대해 함수 PCA를 적용하여 집단 내 개인차의 주요 변동 모드를 추출한다. 제1주성분은 분포의 전반적 위치(빠른 반응 vs 느린 반응)를, 제2주성분은 분포의 퍼짐 정도를 나타낸다. 개인차 탐색에서 일부 ADHD 아동의 밀도가 대조군과 유사하고 일부 대조 아동이 ADHD 패턴을 보여 진단의 복잡성을 시사한다. 이 사례는 관측값으로부터 밀도 함수를 구성하여 함수 데이터로 분석하는 FDA의 확장된 적용을 보여준다.

### Ch 6: Zooming in on Human Growth (pp. 83-100)

**핵심**: 인간 성장 데이터를 세 가지 스케일(키, 속도, 가속도)에서 분석한다. 성장 방정식, 시간적(phase) 변동, 진폭과 위상 변동의 분리를 다룬다.

**키워드**: `growth curve`, `velocity`, `acceleration`, `phase variation`, `amplitude variation`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 6 (line 5830)

인간 성장 데이터를 키(height), 속도(velocity), 가속도(acceleration)의 세 스케일에서 분석한다. Berkeley Growth Study의 10명 여아의 1-18세 키 곡선에서 사춘기 성장 급증(PGS)이 9-15세에 관찰되며, 시기와 강도가 개인마다 다르다. 한 학년 동안 83일간 측정한 10세 남아 데이터에서 주 단위의 성장 변동이 감지되며, 단조 스무딩(monotone smoothing)으로 키의 감소를 방지한다. 신생아 경골(tibia) 데이터는 0.1mm 정밀도로 측정되어 며칠 단위의 성장 패턴을 드러낸다. 가속도 곡선에서 사춘기 급증은 강한 양의 가속 이후 급격한 감속으로 나타나며, 약 6세의 중간 급증(mid-spurt)도 감지된다. 진폭 변동(amplitude variation)은 성장의 강도 차이이고, 위상 변동(phase variation)은 성장 이벤트의 시기 차이이다. 성장 모형에서 위상 변동과 진폭 변동의 분리가 정확한 평균 곡선 추정과 개인차 분석에 필수적이다. 단조 스무딩은 W(t) = β₀ + β₁∫₀ᵗexp(W(u))du 형태의 변환을 사용하여 단조성을 보장한다. 단기 성장 데이터에서 saltation(도약)과 stasis(정체)의 교대 패턴이 관찰되며, 이는 성장이 연속적이지 않을 수 있음을 시사한다. 이 장은 FDA에서 도함수 분석과 곡선 등록의 중요성을 성장 데이터를 통해 실증한다.

### Ch 7: Time Warping Handwriting and Weather Records (pp. 101-114)

**핵심**: 등록(registration) 문제를 필기체와 기상 기록 데이터에 적용한다. 연속 등록의 공식화, warping 함수 추정, 필기 데이터와 기상 데이터의 등록 실습을 포함한다.

**키워드**: `time warping`, `registration`, `handwriting`, `weather data`, `warping function`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 7 (line 7086)

곡선의 변동은 수직적 진폭(amplitude) 변동과 수평적 위상(phase) 변동으로 구분되며, 등록(registration)은 위상 변동을 제거하여 진폭 변동만 남기는 과정이다. 시간 변환 함수(warping function) hᵢ(t)는 표준 시간 구간을 개별 곡선의 시간 구간으로 단사(strictly increasing) 매핑한다. 등록 모형 xᵢ[hᵢ(t)] = x₀(t) + εᵢ(t)에서 잔차 εᵢ가 작다면 곡선 간 차이가 주로 위상 변동에 기인함을 의미한다. 필기체 "fda" 데이터에서 20개 반복 샘플의 접선 가속도(tangential acceleration) 곡선을 등록하여 정점의 시기를 정렬한다. 등록 후 곡선들은 훨씬 일관된 패턴을 보이며, 평균 곡선이 더 선명한 특징을 나타낸다. 기상 데이터에서 34년간(1961-1994)의 일일 기온 기록을 연도별로 등록하여 계절 변동의 시기 차이를 보정한다. 목표 함수 x₀는 초기에 선형 스케일링 후의 표본 평균으로 설정하고, 등록된 곡선의 평균으로 갱신하는 반복 과정을 거친다. 연속 등록에서 warping 함수의 추정은 단조 스무딩과 Newton-Raphson 알고리즘을 결합하여 수행된다. 도함수에 대한 등록이 원 함수보다 더 뚜렷한 특징을 정렬할 수 있어 효과적인 경우가 많다. warping 함수 자체의 분석은 위상 변동의 패턴(예: 겨울의 조기/지연 도래)을 드러낸다.

### Ch 8: How Do Bone Shapes Indicate Arthritis? (pp. 115-130)

**핵심**: 뼈 형태가 관절염을 어떻게 나타내는지를 랜드마크 없는 형태 분석으로 다룬다. 평균 비교, PCA, 정칙화된 선형 판별분석(LDA), 교차 검증을 포함한다.

**키워드**: `bone shape`, `arthritis`, `linear discriminant analysis`, `regularized LDA`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 8 (line 7941)

4장의 뼈 형태 데이터로 돌아와 과간 홈(intercondylar notch)의 상세 형태를 랜드마크 없이 분석한다. 96개의 과간 홈 윤곽(21개 관절염, 75개 대조)을 대상으로 하며, 4장에서 제외된 부분 손상 뼈도 홈이 온전하면 포함한다. 윤곽의 너비를 열(row)별로 측정하여 두 개의 함수(측면 가장자리 X_L, 내측 가장자리 X_M)로 표현한다. 공통 정의역으로 정규화한 후 평균 형태를 추정하고, 관절염 골과 대조 골의 평균 차이를 시각화한다. 함수 PCA로 형태 변동의 주요 모드를 추출하여 과간 홈의 너비, 깊이, 비대칭성의 변동 패턴을 식별한다. 정칙화된 선형 판별분석(regularized LDA)을 적용하여 관절염 여부에 따른 형태 차이를 최대화하는 방향을 찾는다. 정칙화는 소표본에서 공분산 행렬의 역행렬 계산 불안정성을 해결하며, 벌점 모수는 교차 검증으로 선택한다. 분류 성능을 leave-one-out 교차 검증으로 평가하며, 연령을 공변량으로 포함하면 분류 정확도가 향상된다. 관절염 골은 대조 골에 비해 더 넓고 얕은 과간 홈을 보이는 경향이 있다. 이 사례는 형태 데이터를 함수로 표현하여 분류 문제에 FDA를 적용하는 방법을 제시한다.

### Ch 9: Functional Models for Test Items (pp. 131-144)

**핵심**: 검사 문항에 대한 함수 모형을 다룬다. 능력 공간 곡선(ability space curve), 문항 반응 함수 추정, 로그 오즈비 함수의 PCA, 성별 차이 분석을 포함한다.

**키워드**: `item response function`, `ability space`, `test item`, `DIF`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 9 (line 9030)

ACT 수학 시험의 5000명 응시자와 60개 문항 데이터를 사용하여 검사 문항의 함수 모형을 구축한다. 능력 공간 곡선(ability space curve)은 60차원 공간에서 각 좌표가 해당 문항의 정답 확률인 매끄러운 곡선이며, 단일 차원의 능력에 의해 매개변수화된다. 문항 반응 함수(item response function)는 능력 수준 θ에 따른 정답 확률 Pᵢ(θ)로, 비모수적으로 추정한다. 로그 오즈비(log odds ratio) 함수에 대해 함수 PCA를 적용하여 문항 간 변동의 주요 패턴을 추출한다. 제1주성분은 문항의 전반적 난이도 수준 변동을, 제2주성분은 문항의 변별도(discrimination) 차이를 반영한다. 성별에 따른 차별적 문항 기능(DIF) 분석에서 남녀의 문항 반응 함수 차이를 시각화하여 공정성을 평가한다. 총점 기반의 비모수적 능력 추정은 유사한 점수의 응시자 집단을 풀링하여 확률을 추정한다. 검사 설계에서 쉬운 문항은 대부분의 응시자가 맞추고, 어려운 문항은 소수만 맞추며, 이 패턴이 능력 공간 곡선의 매끈한 단차원 구조를 지지한다. 문항 반응 함수의 비모수적 추정은 모수적 IRT 모형(예: 2-모수 로지스틱)보다 유연하여 모형 부적합을 진단할 수 있다. 이 사례는 이산 0/1 데이터로부터 함수 데이터를 구성하여 FDA를 적용하는 독창적 접근을 제시한다.

### Ch 10: Predicting Lip Acceleration from EMG (pp. 145-156)

**핵심**: 발화 시 근전도(EMG) 신호로부터 입술 가속도를 예측하는 함수 회귀 모형을 다룬다. 과거 이력(historical) 모형의 적합과 시간 범위 선택을 포함한다.

**키워드**: `EMG`, `lip acceleration`, `historical linear model`, `functional regression`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 10 (line 882)

발화 시 입술 가속도를 근전도(EMG) 신호로부터 예측하는 함수 회귀 모형을 다룬다. 음절 "bob" 반복 발화 실험에서 하순의 수직 위치, 속도, 가속도와 하순과 관련된 EMG 활동을 동시에 기록한다. 과거 이력(historical) 선형 모형은 현재 시점의 입술 가속도를 이전 시간 구간의 EMG 함수의 가중 적분으로 예측한다. 모형은 Lip''(t) = α(t) + ∫₀ᵗ β(t,s)EMG(s)ds + ε(t)로, 회귀 계수 β(t,s)는 시점 t에서 과거 시점 s의 EMG가 미치는 영향을 나타낸다. 시간 범위 선택 문제가 중요하며, EMG 신호가 입술 운동에 영향을 미치는 지연 시간(약 50-100ms)을 반영해야 한다. β(t,s) 표면의 추정에서 이변량 기저 전개와 roughness penalty를 사용하여 매끈한 회귀 표면을 얻는다. 신경 전달과 중앙 처리의 시간 지연으로 인해 과거 시점의 EMG만이 현재 입술 운동에 영향을 미치는 인과적 모형이 성립한다. 적합 결과에서 EMG 활동이 입술 가속도의 상당 부분을 설명하며, 특히 수축 시기와 이완 시기의 비대칭적 영향이 관찰된다. 잔차 분석을 통해 모형의 적합도를 평가하고, 추가 EMG 채널의 포함 가능성을 논의한다. 이 사례는 함수 회귀에서 인과적 시간 제약을 자연스럽게 반영하는 과거 이력 모형의 유용성을 보여준다.

### Ch 11: The Dynamics of Handwriting Printed Characters (pp. 157-170)

**핵심**: 실시간 필기 데이터의 동역학적 모형을 다룬다. 미분 방정식 기반 필기 모형, 적합도 평가, 미분 방정식의 계수를 이용한 필기자 분류를 포함한다.

**키워드**: `handwriting dynamics`, `differential equation`, `writer classification`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 11 (line 924)

실시간 필기 데이터의 X, Y, Z 좌표를 200Hz로 기록하여 "fda" 인쇄체의 동역학을 분석한다. 선형 미분 방정식 x'''(t) = β₁(t)x'(t) + β₂(t)x''(t) + f(t)를 필기 모형으로 제시하며, 속도와 가속도로부터 jerk(3차 도함수)를 예측한다. 뉴턴의 제2법칙에 의해 근육 수축이 가속도에 직접 작용하므로, 가속도 수준에서의 모형이 운동 제어 시스템을 가장 잘 반영한다. 각 좌표(X, Y, Z)에 대해 독립적인 미분 방정식을 적합하며, 시간 가변 계수 β₁(t), β₂(t)는 기저 전개로 추정한다. 모형 적합도 평가에서 잔차 함수 f(t)의 크기를 원래 jerk 함수와 비교하여 설명 비율을 산출한다. X축(필기 방향)의 적합이 Y축(수직)이나 Z축(들어 올림)보다 우수하며, 이는 필기의 자연 좌표계와 일치한다. 미분 방정식의 시간 가변 계수를 이용하여 필기자 분류(writer classification)를 수행하며, 계수 함수의 유사성으로 동일인의 반복 필기를 식별한다. 분류에서는 시간 가변 계수의 함수적 거리를 기반으로 최근접 이웃 방법이나 판별분석을 적용한다. 5차 도함수에 대한 roughness penalty로 jerk 함수의 안정적 추정을 보장한다. 이 사례는 미분 방정식이 함수 데이터의 동적 구조를 모형화하는 강력한 도구임을 입증한다.

### Ch 12: A Differential Equation for Juggling (pp. 171-181)

**핵심**: 저글링 동작의 데이터를 분석하여 평균 사이클의 특징을 파악하고, 선형 미분 방정식 모형을 적합하여 저글링의 동역학을 설명한다.

**키워드**: `juggling`, `differential equation`, `periodic motion`, `biomechanics`

**상세**: → `Applied Functional Data Analysis_ Methods and Case Studies (2002) - Ramsay J. O., Silverman B. W.md` Ch 12 (line 11755)

전문 저글러의 검지 끝 궤적을 OPTOTRAK 시스템으로 200Hz로 기록하여 3차원 공간에서 123개 사이클의 저글링 동작을 분석한다. 사이클 정의에는 접선 속도의 최소값(손가락 궤적의 최저점, 공 발사 시작)을 랜드마크로 사용하며, 평균 사이클 지속 시간은 719ms이다. 연속 등록(continuous registration)을 접선 속도 함수에 적용하여 사이클 간 위상 변동을 보정한 후 평균 사이클을 산출한다. 평균 사이클에서 공 던지기(throw)와 공 잡기(catch)의 시점이 식별되며, 궤적에 상당한 비틀림이 존재하여 3차원 분석이 필수적이다. 선형 미분 방정식 x'''(t) = β₁(t)x'(t) + β₂(t)x''(t) + f(t)를 각 좌표에 적합하되, 필기와 달리 좌표계 선택이 덜 자명하다. 좌표계에 대한 모형의 불변성이 중요하며, 유클리드 좌표 대신 내재적(intrinsic) 좌표가 더 적절할 수 있다. 공이 손을 떠난 후에는 물리 법칙이 지배하므로, 뇌가 공의 도착 위치를 예측하여 운동을 조정해야 한다. 빠르고 자동화된 동작에서 시각적 피드백보다 신체 변형(strain) 정보에 의한 근육 제어가 지배적이다. 모형 적합 결과에서 잔차 함수 f(t)의 크기로 미분 방정식 모형의 설명력을 평가한다. 이 사례는 필기보다 도전적인 3차원 주기 운동에 미분 방정식 모형을 확장한 것이다.
