---
name: "Think Bayes: Bayesian Statistics in Python (2nd Edition)"
type: book-summary
sources:
  - file: "Downey-ThinkBayes_azure_full.md"
    tool: Document Intelligence
authors: "Allen B. Downey"
year: 2021
total_pages: 305
language: en
keywords: [bayesian-statistics, python, bayes-theorem, probability, MCMC, conjugate-prior, decision-analysis, classification, regression, ABC]
---

# Think Bayes: Bayesian Statistics in Python — Summary

> Allen B. Downey (2021), 305 pages, 20 chapters
> 프로그래밍 능력을 활용하여 수학 공식 대신 Python 코드와 이산 근사로 베이즈 통계를 학습하는 실용 입문서이다.

## Contents

- Preface
- Ch 1. Probability (pp. 1-14)
- Ch 2. Bayes's Theorem (pp. 17-26)
- Ch 3. Distributions (pp. 29-41)
- Ch 4. Estimating Proportions (pp. 43-54)
- Ch 5. Estimating Counts (pp. 57-66)
- Ch 6. Odds and Addends (pp. 69-81)
- Ch 7. Minimum, Maximum, and Mixture (pp. 83-97)
- Ch 8. Poisson Processes (pp. 99-110)
- Ch 9. Decision Analysis (pp. 113-127)
- Ch 10. Testing (pp. 129-142)
- Ch 11. Comparison (pp. 145-158)
- Ch 12. Classification (pp. 161-173)
- Ch 13. Inference (pp. 175-189)
- Ch 14. Survival Analysis (pp. 191-204)
- Ch 15. Mark and Recapture (pp. 207-221)
- Ch 16. Logistic Regression (pp. 223-238)
- Ch 17. Regression (pp. 241-255)
- Ch 18. Conjugate Priors (pp. 257-267)
- Ch 19. MCMC (pp. 269-283)
- Ch 20. Approximate Bayesian Computation (pp. 287-303)
- Index (p. 305)

---

## Chapter Summaries

### Ch 1: Probability (pp. 1-14)

**핵심**: 베이즈 통계의 기초인 조건부 확률을 Linda the Banker 문제로 도입한다. General Social Survey 데이터셋을 사용하여 결합 확률, 조건부 확률, 전체 확률의 법칙을 Python으로 계산하며, 확률의 세 가지 정리와 베이즈 정리를 유도한다.

**키워드**: `conditional-probability`, `conjunction`, `bayes-theorem`, `total-probability`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 1 (line 1408)
이 장은 베이즈 통계의 기초인 조건부 확률을 Linda the Banker 문제로 도입하며, 결합 오류(conjunction fallacy)를 통해 확률적 사고의 중요성을 강조한다. General Social Survey(GSS) 데이터셋을 사용하여 은행원, 여성, 진보주의자 등의 확률을 Python으로 직접 계산한다. 확률 함수 prob()과 조건부 확률 함수 conditional()을 정의하고, 결합(conjunction)과 조건부 확률이 교환법칙을 만족하지 않음을 보인다. 결합 확률과 조건부 확률의 관계를 세 가지 정리로 정리하는데, 정리 1은 결합 확률로부터 조건부 확률을 계산하고, 정리 2는 조건부 확률로부터 결합 확률을 계산하며, 정리 3이 곧 베이즈 정리이다. 베이즈 정리 P(A|B) = P(A)P(B|A)/P(B)를 GSS 데이터로 검증하여 직접 계산한 결과와 일치함을 확인한다. 전체 확률의 법칙(Law of Total Probability)을 도입하여 상호 배타적이고 전체를 포괄하는 조건들의 합으로 확률을 분해하는 방법을 설명한다. 정치적 견해(polviews) 7개 범주를 사용하여 전체 확률의 법칙을 일반화된 합산 형태로 검증한다. 이 장은 모든 데이터가 있을 때는 직접 계산이 가능하지만, 데이터가 불완전할 때 베이즈 정리가 유용해진다는 점을 예고한다. 연습문제에서는 Linda 문제의 변형, conditional 함수의 인자 순서, 나이와 정치적 성향의 관계를 다룬다.

### Ch 2: Bayes's Theorem (pp. 17-26)

**핵심**: 베이즈 정리를 쿠키 문제(Cookie Problem)에 적용하여 사전-사후 확률 갱신 과정을 설명한다. Diachronic Bayes와 Bayes Table 방식을 도입하고, 주사위 문제와 몬티 홀 문제를 통해 반복적 갱신을 시연한다.

**키워드**: `bayes-theorem`, `cookie-problem`, `diachronic-bayes`, `monty-hall`, `bayes-table`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 2 (line 2312)
이 장은 베이즈 정리를 쿠키 문제(Cookie Problem)에 적용하여 사전 확률에서 사후 확률로의 갱신 과정을 단계별로 설명한다. 두 그릇에서 바닐라 쿠키를 꺼냈을 때, 그릇 1에서 나왔을 확률을 베이즈 정리로 계산하여 3/5임을 보인다. Diachronic Bayes 해석을 도입하여 가설 H와 데이터 D의 관계에서 사전(prior), 사후(posterior), 가능도(likelihood), 데이터의 전체 확률이라는 용어를 정의한다. Bayes Table을 pandas DataFrame으로 구현하여 사전 확률과 가능도의 곱을 비정규화 사후 확률로, 이를 정규화하여 사후 확률을 구하는 체계적 절차를 제시한다. 주사위 문제에서는 6면체, 8면체, 12면체 주사위를 대상으로 세 개 이상의 가설이 있는 경우에도 Bayes Table을 적용하며, Fraction 클래스로 정확한 분수 계산을 수행한다. 몬티 홀 문제에서는 3개 문 뒤의 자동차 위치에 대한 가설을 세우고, 호스트가 문 3을 여는 데이터의 가능도를 각 가설별로 계산하여 문 2의 사후 확률이 2/3임을 도출한다. 이 결과는 호스트의 행동이 추가적 정보를 제공한다는 점에서 직관과 다른 결론을 보여준다. 연습문제에서는 트릭 동전, 두 자녀 문제, 몬티 홀 변형, M&M's 색상 문제를 다룬다.

### Ch 3: Distributions (pp. 29-41)

**핵심**: 확률 질량 함수(PMF)와 empiricaldist 라이브러리의 Pmf 클래스를 소개한다. 쿠키 문제를 Pmf 객체로 재구현하고, 101개 그릇 문제로 확장하여 베이즈 갱신을 분포 수준에서 수행하는 방법을 다룬다.

**키워드**: `PMF`, `empiricaldist`, `distributions`, `bayesian-update`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 3 (line 3002)
이 장은 확률 질량 함수(PMF)와 empiricaldist 라이브러리의 Pmf 클래스를 소개하며, 분포 수준에서 베이즈 갱신을 수행하는 방법을 다룬다. Pmf 클래스는 pandas Series를 상속하며, 괄호 연산자로 존재하지 않는 값을 조회하면 0을 반환하는 편의 기능을 제공한다. 쿠키 문제를 Pmf 객체로 재구현하여 사전분포에 가능도를 곱하고 normalize()로 정규화하는 간결한 갱신 절차를 보인다. 연속적인 데이터(바닐라-바닐라-초콜릿)로 순차 갱신을 수행하며, 각 갱신 후 사후 확률이 어떻게 변화하는지 시각적으로 보여준다. 101개 그릇 문제로 확장하여 균등 사전분포에서 바닐라 쿠키 데이터로 갱신하면 사후분포가 선형 형태가 됨을 보이고, 추가 데이터에 따라 분포가 변화하는 과정을 시각화한다. MAP(Maximum A Posteriori) 개념을 도입하여 사후 확률이 가장 높은 값을 idxmax() 또는 max_prob()으로 구하며, 2/3 바닐라 데이터의 MAP이 67임을 확인한다. 주사위 문제를 Pmf로 재풀이하여 불가능한 결과의 가능도를 0으로 설정하는 update_dice 함수를 구현한다. 이 장은 비율 추정의 기초를 마련하며, 다음 장의 유로 동전 문제와 이항 분포로의 전환을 예고한다.

### Ch 4: Estimating Proportions (pp. 43-54)

**핵심**: 유로 동전 문제를 통해 비율 추정으로 전환한다. 이항 분포를 도입하고, 균등 사전분포 및 삼각 사전분포를 사용한 베이즈 추정을 수행하며, 사전분포 선택과 미지 값을 확률로 표현하는 베이즈 통계의 핵심 요소를 설명한다.

**키워드**: `binomial-distribution`, `proportion-estimation`, `prior-distribution`, `euro-problem`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 4 (line 3901)
이 장은 유로 동전 문제를 통해 비율 추정(proportion estimation)으로 전환하며, 베이즈 통계의 핵심 요소를 소개한다. 벨기에 1유로 동전을 250번 회전시켜 140번 앞면이 나온 데이터를 사용하여 동전의 앞면 확률 x를 추정한다. 이항 분포를 도입하여 공정한 동전(p=0.5)에서 140회 이상 앞면이 나올 확률이 약 3.3%이며, 양쪽 꼬리를 합하면 약 6.6%임을 계산한다. 0에서 1까지 101개 값의 균등 사전분포를 사용하여 각 회전 결과마다 순차적으로 가능도를 곱하는 갱신 함수 update_euro를 구현한다. 사후분포의 MAP은 0.56으로 데이터의 앞면 비율 140/250과 일치한다. 삼각 사전분포(triangle prior)를 도입하여 0.5 근처에 더 높은 확률을 부여하고, 충분한 데이터가 있으면 서로 다른 사전분포에서 출발해도 사후분포가 수렴하는 "사전분포 압도(swamping the priors)" 현상을 시연한다. 이항 가능도 함수를 사용하여 전체 데이터셋의 가능도를 한 번에 계산하는 효율적 방법을 제시한다. 베이즈 통계의 두 가지 핵심 특징으로 사전분포 선택의 주관성과 미지의 물리적 속성을 확률로 표현하는 해석을 설명한다. 연습문제에서는 타율 추정, 무작위 응답 기법을 통한 탈세 비율 추정, 측정 오차가 있는 동전 문제, 외계인 미사일 문제를 다룬다.

### Ch 5: Estimating Counts (pp. 57-66)

**핵심**: 기차 문제(Train Problem)와 독일 전차 문제(German Tank Problem)를 통해 모집단 크기 추정을 다룬다. 사전분포에 대한 민감도 분석, 거듭제곱 법칙 사전분포, 신뢰 구간(credible interval) 개념을 도입한다.

**키워드**: `count-estimation`, `german-tank-problem`, `power-law-prior`, `credible-interval`, `sensitivity`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 5 (line 4639)
이 장은 기차 문제(Train Problem)를 통해 모집단 크기 추정을 다루며, 주사위 문제와 동일한 가능도 함수(1/N)를 사용한다. 기관차 번호 60을 관측한 경우 균등 사전분포(1~1000)에서 MAP은 60이지만, 사후 평균은 333으로 훨씬 높다. 사전분포의 상한을 500, 1000, 2000으로 변화시키면 사후 평균이 207, 333, 552로 크게 달라지며, 이는 데이터가 적을 때 사전분포에 대한 민감도가 높음을 보여준다. 거듭제곱 법칙(power law) 사전분포를 도입하여 기업 규모 분포에 대한 배경 지식을 반영하면, 사후 평균의 상한 의존성이 크게 줄어든다. 신뢰 구간(credible interval) 개념을 도입하여 백분위수와 분위수의 차이를 설명하고, Pmf의 quantile과 credible_interval 메서드를 사용하여 90% 신뢰 구간을 계산한다. 독일 전차 문제를 역사적 사례로 소개하며, 2차 세계대전 중 연합군이 일련번호 분석으로 독일의 탱크 생산량을 정확하게 추정한 사례를 설명한다. 정보적 사전분포(informative prior)와 비정보적 사전분포(uninformative prior) 사이의 논쟁을 정리하며, 데이터가 많으면 사전분포 선택이 중요하지 않고, 데이터가 적으면 배경 정보 활용이 중요하다는 실용적 관점을 제시한다. 연습문제에서는 강의실 인원 추정, 토끼 개체수 추정, 수감자 표본 편향 문제, 종말론적 논증을 다룬다.

### Ch 6: Odds and Addends (pp. 69-81)

**핵심**: 확률을 승산(odds)으로 표현하는 방법과 베이즈 규칙(Bayes's rule)을 소개한다. Oliver's Blood 문제로 증거의 강도를 정량화하고, 확률변수의 합·차에 대한 분포 연산(addends)과 글루텐 민감도 문제를 통해 순방향/역방향 문제를 구분한다.

**키워드**: `odds`, `bayes-rule`, `likelihood-ratio`, `addends`, `forward-inverse-problem`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 6 (line 5323)
이 장은 확률의 대안적 표현인 승산(odds)과 베이즈 규칙(Bayes's rule)을 소개하며, 확률변수의 합에 대한 분포 연산을 다룬다. 승산은 사건이 일어날 확률과 일어나지 않을 확률의 비율이며, 확률과 승산 사이의 변환 함수를 정의한다. 베이즈 규칙은 사후 승산 = 사전 승산 × 가능도 비율의 형태로, 쿠키 문제를 암산으로 풀 수 있게 한다. Oliver's Blood 문제에서 증거의 강도를 가능도 비율(베이즈 팩터)로 정량화하며, 데이터가 가설과 일치하더라도 반드시 가설을 지지하는 것은 아님을 보인다. add_dist 함수를 구현하여 두 확률변수의 합의 분포를 계산하며, 6면체 주사위 합의 분포가 삼각형, 세 개 합의 분포가 종 모양임을 보인다. 글루텐 민감도 문제에서 순방향 문제(Forward Problem)와 역방향 문제(Inverse Problem)를 구분하며, 35명 중 12명이 글루텐 밀가루를 올바르게 식별한 데이터로 실제 민감한 피험자 수의 사후분포를 계산한다. 순방향 문제에서는 민감한 피험자 수가 주어졌을 때 정답 수의 분포를 이항 분포의 합으로 구하고, 역방향 문제에서는 관측된 정답 수의 가능도를 이용하여 사후분포를 갱신한다. 12명 정답의 경우 민감한 피험자가 0명일 가능성이 가장 높다는 결과를 도출한다. 연습문제에서는 미국 의회 정직성, D&D 전투, 주사위 곱 문제 등을 다룬다.

### Ch 7: Minimum, Maximum, and Mixture (pp. 83-97)

**핵심**: 누적 분포 함수(CDF)를 도입하고 최솟값·최댓값 분포의 계산법을 설명한다. D&D의 "4개 중 최고 3개" 문제를 예시로 사용하며, 혼합 분포(mixture distribution)를 통해 예측 문제를 해결하는 방법을 다룬다.

**키워드**: `CDF`, `minimum`, `maximum`, `mixture-distribution`, `prediction`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 7 (line 6232)
이 장은 누적 분포 함수(CDF)를 도입하고, 최솟값·최댓값 분포의 계산법과 혼합 분포(mixture distribution)를 설명한다. Cdf 클래스는 Pmf에서 cumsum()으로 생성하거나 make_cdf()를 사용하며, 분위수 조회와 신뢰 구간 계산에 효율적이다. D&D 캐릭터 속성 생성 문제에서 6면체 주사위 4개를 굴려 최고 3개의 합을 구하는 분포를 시뮬레이션으로 추정한다. 최댓값 분포는 CDF를 n제곱하여 계산하며, 6개 속성 중 최댓값의 CDF를 cdf_best3**6으로 구한다. 최솟값 분포는 여보수 CDF(1-CDF)를 n제곱한 후 다시 여보수를 취하여 계산한다. 혼합 분포는 여러 분포의 가중 평균으로, D&D의 단검(4면체)과 단검(6면체)을 무작위로 선택하여 공격하는 상황에서 피해량의 분포를 계산한다. make_mixture 함수를 구현하여 pandas DataFrame을 활용한 효율적인 가중 합산을 수행하며, 임의 개수의 분포를 혼합할 수 있다. 혼합 분포와 합의 분포(add_dist)의 차이를 명확히 구분하며, 혼합은 확률의 가중 평균이고 합은 확률변수의 합에 대한 분포이다. 이 장에서 도입한 make_mixture는 이후 장들에서 예측 문제를 해결하는 핵심 도구로 활용된다. 연습문제에서는 D&D 표준 배열 비교, 몬스터 공격 추론, 푸앵카레의 빵 무게 문제를 다룬다.

### Ch 8: Poisson Processes (pp. 99-110)

**핵심**: 포아송 과정을 소개하고 2018 FIFA 월드컵 결승전 데이터를 활용하여 축구 경기의 골 득점을 모델링한다. 감마 분포를 사전분포로, 포아송 분포를 가능도로 사용하며, 우월 확률(probability of superiority)과 재경기 예측을 수행한다.

**키워드**: `poisson-process`, `gamma-distribution`, `world-cup-problem`, `probability-of-superiority`, `exponential-distribution`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 8 (line 7396)
이 장은 포아송 과정을 소개하고 2018 FIFA 월드컵 결승전(프랑스 4:2 크로아티아)을 모델링한다. 포아송 분포는 골 득점률 λ가 주어졌을 때 k골을 넣을 확률을 계산하며, λ=1.4일 때 4골의 확률은 약 4%이다. 감마 분포를 사전분포로 선택하는데, 이는 연속적이고 음이 아닌 값에 적합하고 파라미터 α가 곧 평균이 되는 편리함이 있다. 프랑스의 4골 데이터로 갱신하면 사후분포가 오른쪽으로 이동하여 사후 평균이 2.7이 되고, 크로아티아는 2골로 갱신하여 사후 평균이 1.7이 된다. 우월 확률(probability of superiority)을 계산하여 프랑스가 더 강한 팀일 확률이 약 75%임을 보인다. 재경기 예측을 위해 사후 예측 분포(posterior predictive distribution)를 혼합 분포로 계산하며, 프랑스의 재경기 승리 확률은 약 65%로 우월 확률보다 낮다. 이는 더 나은 팀이라도 단일 경기에서는 불확실성이 더 크기 때문이다. 지수 분포를 도입하여 골 사이의 시간 간격을 모델링하는 방법을 설명하며, 포아송 과정의 또 다른 활용 가능성을 보인다. 감마 분포를 사전분포로 선택한 네 번째 이유는 18장에서 밝혀질 켤레 사전분포 관계임을 예고한다. 연습문제에서는 2014 월드컵 독일-브라질 반결승과 NHL 챔피언십 시리즈를 다룬다.

### Ch 9: Decision Analysis (pp. 113-127)

**핵심**: TV 쇼 "The Price Is Right"를 활용한 베이즈 의사결정 분석을 다룬다. 커널 밀도 추정(KDE)으로 사전분포를 구성하고, 정규 분포로 가능도를 계산한 뒤, 사후분포를 이용하여 기대 이익을 최대화하는 최적 입찰 전략을 도출한다.

**키워드**: `decision-analysis`, `KDE`, `expected-gain`, `optimal-bidding`, `price-is-right`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 9 (line 8325)
이 장은 TV 쇼 "The Price Is Right"의 Showcase 게임을 활용하여 베이즈 의사결정 분석을 수행한다. 2011-2012 시즌의 과거 데이터를 사용하여 커널 밀도 추정(KDE)으로 쇼케이스 가격의 사전분포를 구성한다. 참가자의 추정 오차를 정규 분포로 모델링하며, 과거 입찰 데이터의 표준편차를 사용하되 평균은 0으로 가정하여 전략적 저입찰을 보정한다. 참가자의 추측값 $23,000을 데이터로 사용하여 사후분포를 갱신하면, 사전 평균 $30,000에서 사후 평균 $26,000으로 이동한다. 상대 참가자의 과거 성과를 기반으로 차액별 승리 확률을 계산하며, 과입찰하면 무조건 패배하는 규칙을 반영한다. 전체 확률의 법칙을 적용하여 각 입찰 금액에 대한 총 승리 확률을 계산하고, 승리 확률을 최대화하는 최적 입찰가 $21,000을 도출한다. 기대 이익 최대화 분석에서는 $250 이내로 맞추면 양쪽 쇼케이스를 모두 획득하는 규칙을 고려하여 최적 입찰가가 $22,000으로 달라진다. 이 예시는 "최적"이라는 용어가 최적화 대상에 따라 다른 결과를 낳을 수 있음을 보여준다. 빈도주의 방법과 대비하여 사후분포 전체를 활용하는 베이즈 방법의 의사결정 분석에서의 우위를 강조한다. 연습문제에서는 지하철 대기 시간 분석과 도서 판매 예측 문제를 다룬다.

### Ch 10: Testing (pp. 129-142)

**핵심**: 유로 동전 문제를 재방문하여 베이즈 가설 검정을 수행한다. 편향된 동전 vs 공정한 동전의 증거를 베이즈 팩터로 평가하고, 다중 밴딧(Bayesian Bandits) 문제를 통해 탐험-활용(explore-exploit) 전략을 소개한다.

**키워드**: `hypothesis-testing`, `bayes-factor`, `evidence`, `bayesian-bandits`, `explore-exploit`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 10 (line 9295)
이 장은 유로 동전 문제를 재방문하여 베이즈 가설 검정을 수행하고 베이즈 팩터로 증거의 강도를 정량화한다. "편향"의 정의에 따라 결과가 달라지는데, 특정 값(x=0.56)으로 정의하면 베이즈 팩터가 약 6으로 편향 지지, 균등 분포로 정의하면 약 2.1로 공정 지지, 삼각 분포로 정의하면 그 중간이 된다. 베이즈 가설 검정은 p-값과 달리 증거의 강도를 연속적 척도로 측정하지만, 가설의 정의에 의존한다는 한계가 있다. 저자는 가설 검정보다 예측과 의사결정이 더 유용한 질문이라고 주장한다. 베이즈 밴딧(Bayesian Bandits) 문제를 도입하여 네 대의 슬롯 머신에서 탐험(exploration)과 활용(exploitation)을 균형 잡는 전략을 설명한다. 균등 사전분포에서 시작하여 각 플레이 결과로 승리 확률의 사후분포를 갱신하며, 톰슨 샘플링(Thompson sampling)으로 각 분포에서 하나의 값을 추출하여 가장 높은 값의 머신을 선택한다. 100회 플레이 후 높은 확률의 머신이 더 많이 선택되는 결과를 보이며, 정밀한 추정 자체보다 최선의 행동을 취하는 것이 목표임을 강조한다. 이 장은 베이즈 의사결정 이론이 사후분포를 행동으로 전환하는 가장 큰 장점이라고 결론짓는다. 연습문제에서는 적응형 표준화 시험 문제를 다룬다.

### Ch 11: Comparison (pp. 145-158)

**핵심**: 결합 분포(joint distribution)를 도입하고 외적(outer product) 연산으로 구현한다. 두 사람의 키 비교 문제와 체스 선수 평가 문제를 통해 결합 분포의 갱신, 주변 분포, 조건부 사후분포를 다루며, 변수 간 독립과 종속의 개념을 설명한다.

**키워드**: `joint-distribution`, `outer-product`, `marginal-distribution`, `conditional-posterior`, `mesh-grid`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 11 (line 10353)
이 장은 결합 분포(joint distribution)를 도입하고, 외적(outer product) 연산으로 두 변수의 결합 분포를 구성하는 방법을 설명한다. NumPy의 meshgrid를 사용하여 외적, 외합, 외비교 연산을 수행하며, 이를 DataFrame으로 시각화한다. 미국 성인 남성의 키를 정규 분포(평균 178cm, 표준편차 7.7cm)로 모델링하고, A와 B 두 사람의 키에 대한 결합 사전분포를 독립 가정하에 외적으로 구성한다. A가 B보다 크다는 데이터의 가능도를 np.where로 이진 배열로 만들어 사후분포를 갱신하며, A보다 키가 작은 B의 쌍은 모두 제거된다. 주변 분포(marginal distribution)를 행 또는 열의 합으로 추출하여 A의 사후 평균이 182.4cm, B의 사후 평균이 173.6cm임을 보인다. 사후분포의 표준편차가 사전분포보다 줄어들어 비교 정보가 불확실성을 감소시킴을 확인한다. 조건부 사후분포를 통해 A가 170cm일 때 B의 분포가 170cm 이하로 절단됨을 보이며, 사후분포에서 A와 B가 종속적임을 설명한다. 독립과 종속의 개념을 명확히 하여, 사전분포에서는 독립이었던 두 변수가 데이터 갱신 후 종속이 됨을 강조한다. 연습문제에서는 Elo 레이팅 시스템을 사용한 체스 선수 평가 문제를 다루며, 로지스틱 함수를 통해 승리 확률을 계산한다.

### Ch 12: Classification (pp. 161-173)

**핵심**: Palmer Station 펭귄 데이터를 사용하여 베이즈 분류를 시연한다. 나이브 베이즈 분류기를 구축하고, 다변량 정규 분포를 도입하여 변수 간 상관관계를 고려하는 개선된 분류기를 만든다.

**키워드**: `naive-bayes`, `classification`, `penguin-data`, `multivariate-normal`, `joint-distribution`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 12 (line 11354)
이 장은 Palmer Station 펭귄 데이터셋(344마리, 3종)을 사용하여 베이즈 분류를 시연한다. Adelie, Chinstrap, Gentoo 세 종의 부리 길이(culmen length)와 날개 길이(flipper length) 등의 측정값 분포를 CDF로 비교하여 각 특성의 종 구별력을 평가한다. 각 종별로 정규 분포 객체를 생성하고, 관측값의 확률 밀도를 가능도로 사용하여 사전분포를 갱신하는 update_penguin 함수를 구현한다. 나이브 베이즈 분류기를 구축하여 특성 간 독립을 가정하고 순차적으로 갱신하며, 두 특성만으로 약 95%의 분류 정확도를 달성한다. 산점도에서 종별 데이터가 대각선 방향의 타원 형태를 보이는 것은 특성 간 상관관계가 있음을 나타낸다. 다변량 정규 분포(multivariate normal)를 도입하여 특성 간 공분산을 포함한 결합 분포를 모델링하고, 등고선이 데이터에 더 잘 맞는 타원을 형성함을 보인다. 다변량 정규 분포를 사용한 개선된 분류기는 95.3%의 정확도를 달성하여 나이브 분류기(94.7%)보다 약간 향상된다. 나이브 베이즈가 실용적으로 충분히 잘 작동하는 경우가 많다는 점을 강조한다. 분류의 과학적 활용으로 성적 이형성(sexual dimorphism) 연구를 소개하며, 분류 정확도가 이형성의 정도를 정량화하는 지표가 될 수 있음을 설명한다.

### Ch 13: Inference (pp. 175-189)

**핵심**: 교육 처치 효과 비교를 통해 베이즈 추론과 빈도주의 t-검정을 대비한다. 두 집단 간 차이의 사후분포를 계산하고, 요약 통계량을 활용한 갱신, 우월 확률, 신뢰 구간 등 p-값의 베이즈 대안을 제시한다.

**키워드**: `bayesian-inference`, `t-test-alternative`, `posterior-difference`, `summary-statistics`, `probability-of-superiority`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 13 (line 12281)
이 장은 교육 처치 효과를 비교하는 문제를 통해 베이즈 추론과 빈도주의 t-검정을 대비한다. 21명의 처치 집단과 23명의 통제 집단이 8주간 읽기 활동을 수행한 후 DRP 점수를 비교하며, 데이터는 정규 분포로 적절히 모델링된다. 모집단의 평균(μ)과 표준편차(σ)를 미지 파라미터로 설정하고, 균등 사전분포의 결합 분포를 외적으로 구성한다. 3차원 메시그리드를 사용하여 각 데이터 점의 확률 밀도를 모든 파라미터 쌍에 대해 계산하고, 곱으로 가능도를 구한다. 주변 분포를 추출하여 처치 집단의 평균이 더 높을 확률(우월 확률)이 약 98%임을 보인다. sub_dist로 평균 차이의 분포를 계산하여 평균 차이가 약 10점이며 90% 신뢰 구간이 [2.4, 17.4]임을 도출한다. 요약 통계량(표본 평균, 표본 표준편차)만으로 갱신하는 대안적 방법을 제시하며, 정규 분포의 표본 평균 분포와 카이제곱 분포를 활용한다. Basu의 정리에 의해 표본 평균과 표본 표준편차가 독립이므로 결합 가능도를 곱으로 구할 수 있다. 요약 통계량 기반 갱신은 계산 효율적이나 정규성 가정으로 인해 정보 손실이 발생하여 사후분포가 약간 더 넓어진다. 연습문제에서는 Cohen의 효과 크기, 시험 점수 분포 추정, 변동성 가설(남녀 키 차이)을 다룬다.

### Ch 14: Survival Analysis (pp. 191-204)

**핵심**: 생존 분석을 소개하며 와이블 분포를 사용하여 전구 수명과 보호소 개의 입양 시간을 모델링한다. 불완전 데이터(절단 데이터)를 베이즈 방법으로 다루는 기법과 사후 예측 분포를 설명한다.

**키워드**: `survival-analysis`, `weibull-distribution`, `censored-data`, `posterior-predictive`, `incomplete-data`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 14 (line 13276)
이 장은 생존 분석을 소개하며 와이블 분포를 사용하여 사건까지의 시간을 모델링한다. 와이블 분포는 λ(위치)와 k(형태) 두 파라미터를 가지며, SciPy의 weibull_min으로 구현한다. 시뮬레이션 데이터 10개를 생성하여 와이블 분포의 파라미터를 추정하며, 3차원 메시그리드로 모든 파라미터 쌍과 데이터 점에 대한 가능도를 계산한다. 보호소 개의 입양 시간 문제에서 불완전 데이터(절단 데이터, censored data)를 다루는 방법을 설명한다. 관측 기간을 넘어 체류하는 개들의 데이터는 생존 함수(survival function, sf)로 가능도를 계산하며, 이는 체류 시간이 관측값보다 클 확률을 나타낸다. 완전 데이터와 불완전 데이터를 결합하여 순차적으로 갱신하며, 불완전 데이터가 있을 때 사후분포가 더 넓어짐을 보인다. 전구 수명 실험 데이터(50개 전구, 32개 고유 수명)를 사용하여 실제 와이블 파라미터를 추정하며, 사후 평균 수명이 약 1,413시간임을 계산한다. 사후 예측 분포를 혼합 분포로 계산하여 100개 전구 설치 후 1,000시간 뒤 사망 전구 수의 분포를 구하며, 파라미터 불확실성으로 인해 알려진 파라미터의 이항 분포보다 넓은 분포를 얻는다. 베이즈 방법이 불완전 데이터를 자연스럽게 처리할 수 있음을 강조한다. 연습문제에서는 전구 실험 갱신과 시애틀 강수량의 감마 분포 추정을 다룬다.

### Ch 15: Mark and Recapture (pp. 207-221)

**핵심**: 표지-재포획 실험을 통한 모집단 크기 추정을 다룬다. 그리즐리 곰 DNA 포획 데이터를 사용하여 2-파라미터 및 3-파라미터 모델을 구축하고, Lincoln Index 문제와 소프트웨어 버그 수 추정으로 확장한다.

**키워드**: `mark-recapture`, `population-estimation`, `lincoln-index`, `hypergeometric`, `three-parameter-model`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 15 (line 14317)
이 장은 표지-재포획 실험을 통한 모집단 크기 추정을 다루며, 그리즐리 곰 DNA 데이터를 사용한다. 1996-1997년 연구에서 1차 세션에 23마리, 2차 세션에 19마리를 포획했으며 그 중 4마리가 중복이었다. 초기모형분포 분포를 사용하여 N=100일 때 k=4의 확률이 가장 높음을 보이고, 균등 사전분포(50~500)를 갱신하여 MAP이 109, 사후 평균이 174임을 계산한다. 2-파라미터 모델에서는 N과 관측 확률 p를 동시에 추정하며, 다항 분포를 가능도 함수로 사용한다. 데이터를 k00(미관측), k01(2차만), k10(1차만), k11(양쪽)의 네 범주로 분류하고, 각 범주의 확률을 p와 q=1-p로 표현한다. MultiIndex를 활용한 Pmf로 2차원 결합 분포를 표현하고, stack/unstack으로 변환하여 등고선 플롯을 그린다. Lincoln Index 문제로 확장하여 소프트웨어 버그 수를 두 독립 테스터의 결과로 추정하며, 3-파라미터 모델(N, p0, p1)을 구축한다. 3-파라미터 모델은 약 17만 개의 조합을 열거하며, 격자 방법의 실용적 한계에 근접함을 보인다. 사후 평균 버그 수가 약 106개이며, 두 테스터의 발견 확률이 각각 약 23%, 18%로 추정된다. 연습문제에서는 대만 A형 간염 역학 연구의 표지-재포획 분석을 다룬다.

### Ch 16: Logistic Regression (pp. 223-238)

**핵심**: 로그 승산(log odds)과 로지스틱 회귀를 소개한다. 베이즈 규칙의 로그 스케일 해석으로 증거 축적 과정을 설명하고, 우주왕복선 챌린저호의 O-링 데이터로 온도와 손상 확률 간의 관계를 모델링한다.

**키워드**: `logistic-regression`, `log-odds`, `space-shuttle`, `o-ring`, `empirical-bayes`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 16 (line 15390)
이 장은 로그 승산(log odds)과 로지스틱 회귀를 소개하며, 베이즈 규칙의 로그 스케일 해석을 통해 증거 축적 과정을 설명한다. 대학원 수업 일화를 통해 사전 승산 10:1에서 여학생 3명을 관측할 때마다 가능도 비율 1/3을 곱하여 사후 승산이 10/27로 감소하는 과정을 보인다. 로그 승산 스케일에서 베이즈 갱신은 덧셈이 되어, log O(H|F^x) = log O(H) + x·log(가능도 비율)이라는 선형 관계가 성립한다. 이 선형 관계가 로지스틱 회귀의 기초이며, log O(H|x) = β₀ + β₁x로 표현된다. 우주왕복선 챌린저호의 O-링 데이터를 사용하여 온도와 손상 확률 간의 관계를 모델링한다. statsmodels로 비베이즈 로지스틱 회귀를 수행하여 점추정값을 구하고, 이를 기반으로 균등 사전분포의 범위를 설정하는 Empirical Bayes 접근을 사용한다. 온도를 평균 중심화하여 파라미터 간 상관을 최소화하고, 이항 분포로 각 온도별 손상 건수의 가능도를 계산한다. 사후분포에서 절편을 expit으로 변환하면 70°F에서 손상 확률의 분포를, 기울기를 exp로 변환하면 1°F당 가능도 비율(약 0.75)의 분포를 얻는다. 예측 분포를 계산하여 31°F(챌린저호 발사 온도)에서 손상 확률이 97% 이상임을 보이며, 모든 데이터를 고려했다면 재난을 예측할 수 있었음을 시사한다. 연습문제에서는 정치 전문가 평가와 ADHD 진단율-출생월 관계를 다룬다.

### Ch 17: Regression (pp. 241-255)

**핵심**: 단순 선형 회귀의 베이즈적 접근을 다룬다. Norfolk County 적설량 변화와 마라톤 세계 기록 데이터를 사용하여 세 개 파라미터(절편, 기울기, 분산)의 사후분포를 추정하고 미래 값을 예측한다.

**키워드**: `linear-regression`, `bayesian-regression`, `snowfall`, `marathon`, `prediction`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 17 (line 16594)
이 장은 단순 선형 회귀의 베이즈적 접근을 다루며, y = ax + b + ε 모델에서 기울기, 절편, 표준편차의 세 파라미터를 추정한다. Norfolk County의 Blue Hill 기상관측소 데이터(1967~2020)로 연간 적설량의 변화 추세를 분석한다. 적설량의 분포가 정규 분포에 잘 맞음을 CDF 비교로 확인하고, statsmodels의 최소제곱법으로 점추정값(기울기 약 0.51 인치/년, 절편 약 64 인치)을 구한다. 세 파라미터의 균등 사전분포를 make_joint3로 결합하여 약 65,000개 조합의 3차원 결합 분포를 구성한다. 각 파라미터 조합에 대해 잔차의 정규 분포 밀도를 곱하여 가능도를 계산하며, 격자 방법의 한계에 근접하는 계산량이 소요된다. 기울기의 사후 평균은 약 0.51 인치/년이며, 음의 기울기일 확률은 약 2%로, 저자의 직관과 달리 적설량이 증가하고 있음을 보인다. 마라톤 세계 기록 데이터(1970~)를 두 번째 사례로 사용하여 속도의 증가 추세를 모델링하고, 사후 예측 분포를 생성한다. 예측을 위해 사후분포에서 파라미터를 샘플링하고, 정규 잡음을 추가하여 미래 값의 분포를 생성한다. 보간법으로 2시간 마라톤(13.1 mph) 달성 시점을 추정하여 중앙값 2036년, 90% 신뢰 구간 [2032, 2043]을 도출한다. 격자 방법의 한계로 3개 이상 파라미터의 모델에는 MCMC 등 대안이 필요함을 예고한다.

### Ch 18: Conjugate Priors (pp. 257-267)

**핵심**: 격자 방법의 한계를 넘기 위해 켤레 사전분포를 도입한다. 월드컵 문제를 감마-포아송 켤레쌍으로 재풀이하고, 이항-베타 및 다항-디리클레 켤레쌍을 소개하여 분석적 갱신의 효율성을 보여준다.

**키워드**: `conjugate-prior`, `gamma-poisson`, `beta-binomial`, `dirichlet-multinomial`, `analytical-update`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 18 (line 17795)
이 장은 격자 방법의 한계를 넘기 위해 켤레 사전분포를 도입하며, 세 가지 켤레쌍을 소개한다. 월드컵 문제를 감마-포아송 켤레쌍으로 재풀이하여, 사후 감마 분포의 파라미터가 α+k와 β+t로 단순 덧셈만으로 계산됨을 보인다. 감마 분포의 PDF와 포아송 분포의 PMF를 곱하면 동일한 함수 형태(λ의 거듭제곱 × 지수함수)가 유지되어 사후분포도 감마 분포임을 수학적으로 유도한다. α는 관측된 사건 수를, β는 경과 시간을 반영한다는 파라미터의 의미를 해석한다. 유로 동전 문제를 이항-베타 켤레쌍으로 재풀이하며, 균등 분포가 alpha=1, beta=1인 베타 분포와 같음을 보인다. 이항 가능도와 베타 사전분포의 곱이 α+k와 β+n-k를 파라미터로 하는 베타 분포가 됨을 유도한다. 사자-호랑이-곰 문제를 통해 다항-디리클레 켤레쌍을 소개하며, 디리클레 분포에서 각 변수의 주변 분포가 베타 분포임을 보인다. 디리클레 사전분포의 파라미터 벡터에 관측 데이터 벡터를 더하면 사후분포가 되는 간결한 갱신 규칙을 제시한다. 켤레 사전분포는 산술 연산만으로 갱신이 가능하지만, 실용적으로 사용 가능한 경우가 제한적임을 인정한다. 연습문제에서는 지수 분포의 켤레 사전분포, 삼각 사전분포의 베타 근사, 온라인 판매자 평가, 디리클레 분포를 활용한 동물 출현 예측을 다룬다.

### Ch 19: MCMC (pp. 269-283)

**핵심**: 마르코프 체인 몬테 카를로(MCMC) 방법과 PyMC3 라이브러리를 소개한다. 월드컵 문제를 MCMC로 재풀이하고, 사전 예측 분포 점검, 행복도 데이터의 단순/다중 회귀를 PyMC3으로 구현하여 격자 방법 이후의 확장 경로를 제시한다.

**키워드**: `MCMC`, `PyMC3`, `prior-predictive`, `posterior-predictive`, `regression`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 19 (line 18503)
이 장은 마르코프 체인 몬테 카를로(MCMC) 방법과 PyMC3 라이브러리를 소개하며, 격자 방법의 한계를 넘는 확장 경로를 제시한다. MCMC는 사후분포를 직접 계산하지 않고 샘플을 생성하며, 월드컵 문제를 PyMC3로 재풀이하여 격자 방법과 동일한 결과를 확인한다. PyMC3의 모델 명세에서는 with 문 안에서 Gamma 사전분포와 Poisson 가능도를 정의하고, observed 인자로 데이터를 지정하면 사후분포를 샘플링한다. 사전 예측 분포(prior predictive distribution)를 도입하여 모델이 데이터와 일관적인지 사전 점검하는 방법을 설명한다. NUTS(No U-Turn Sampler) 알고리즘, 튜닝 단계, 다중 체인 등 PyMC3의 샘플링 과정을 개략적으로 소개한다. 단순 회귀 모델로 세계 행복 보고서의 GDP-행복도 관계를 분석하여 기울기 약 0.72를 추정하고, linregress 결과와 일치함을 확인한다. 다중 회귀 모델로 6개 예측 변수(GDP, 사회적 지원, 건강 기대수명, 자유, 관대함, 부패 인식)와 행복도의 관계를 추정하며, 8개 파라미터의 모델은 격자 방법으로는 불가능하지만 PyMC3로 쉽게 처리된다. GDP, 사회적 지원, 건강 기대수명, 자유가 행복에 가장 강한 연관을 보이며, 관대함의 신뢰 구간은 0을 포함한다. MCMC는 강력하지만 튜닝과 진단에 전문성이 필요하므로, 격자 방법으로 시작하여 필요할 때 MCMC로 전환하는 점진적 개발을 권장한다.

### Ch 20: Approximate Bayesian Computation (pp. 287-303)

**핵심**: 가장 복잡한 문제를 위한 최후의 수단으로 근사 베이즈 계산(ABC)을 소개한다. 신장 종양 성장 모델링으로 종양의 나이를 추정하고, 세포 계수 문제에 ABC를 적용하여 시뮬레이션 기반 추론을 시연한다.

**키워드**: `ABC`, `approximate-bayesian-computation`, `kidney-tumor`, `cell-counting`, `simulation-based-inference`

**상세**: → `Allen B. Downey - Think Bayes_ Bayesian Statistics in Python-O'Reilly Media (2021).md` Ch 20 (line 19580)
이 장은 가장 복잡한 문제를 위한 최후의 수단으로 근사 베이즈 계산(ABC)을 소개하며, 시뮬레이션 기반 추론을 시연한다. 신장 종양 환자의 질문에서 출발하여, 종양의 크기로부터 나이를 추정하는 문제를 다룬다. Zhang 등의 논문에서 체적 배가 시간(volumetric doubling time)과 역배가 시간(RDT) 데이터를 가져와 성장률 분포를 KDE로 추정한다. 단순 성장 모델에서 종양을 구형으로 가정하고, 8개월 간격으로 RDT 분포에서 성장률을 샘플링하여 0.3cm에서 20cm까지의 성장을 시뮬레이션한다. 101회 시뮬레이션을 수행하여 각 크기에 도달하는 나이의 분포를 보간법으로 추정하며, 15cm 종양의 중앙 나이는 약 22년, 9년 이내일 확률은 1% 미만이다. 이 접근은 사전분포나 베이즈 갱신 없이, 시뮬레이션에서 조건부 분포를 직접 추출하는 방식이다. 세포 계수 문제에서는 효모 현탁액의 3단계 희석과 혈구계산기를 사용한 세포 수 측정 과정을 PyMC3으로 모델링한다. 피펫 오차, 희석 변동, 포아송 샘플링, 이항 격자 선택 등 다단계 오차원을 포함하며, MCMC로 농도의 사후분포(평균 약 23억/mL)를 추정한다. ABC 버전에서는 사전분포에서 대량 샘플을 생성하고 시뮬레이션을 수행한 뒤, 관측 데이터(49개)와 정확히 일치하는 경우만 선택하여 사후분포를 근사한다. ABC의 핵심은 사전분포 샘플링, 시뮬레이션, 근사적 데이터 매칭의 세 요소이며, 정확한 매칭 대신 근사적 기준을 사용할 수 있다. 연습문제에서는 세탁기 양말 짝 맞추기 문제를 다룬다.
