---
name: "Reinforcement Learning: An Introduction"
type: book-summary
source_file: "Sutton-RL_full.md"
authors: "Richard S. Sutton, Andrew G. Barto"
year: 2015
total_pages: 338
language: en
keywords: [reinforcement learning, MDP, temporal-difference learning, Q-learning, policy gradient, Monte Carlo methods, dynamic programming, eligibility traces, function approximation, actor-critic]
---

# Reinforcement Learning: An Introduction — Summary

> Richard S. Sutton, Andrew G. Barto (2nd ed., 2015), 338 pages, 15 chapters
> 강화학습의 핵심 아이디어와 알고리즘을 표 기반 방법부터 함수 근사까지 체계적으로 설명하는 표준 교과서이다

## Contents

### Part I: Tabular Solution Methods
- Ch 1: The Reinforcement Learning Problem
- Ch 2: Multi-arm Bandits
- Ch 3: Finite Markov Decision Processes
- Ch 4: Dynamic Programming
- Ch 5: Monte Carlo Methods
- Ch 6: Temporal-Difference Learning
- Ch 7: Eligibility Traces
- Ch 8: Planning and Learning with Tabular Methods

### Part II: Approximate Solution Methods
- Ch 9: On-policy Approximation of Action Values
- Ch 10: Off-policy Approximation of Action Values
- Ch 11: Policy Approximation

### Part III: Frontiers
- Ch 12: Psychology
- Ch 13: Neuroscience
- Ch 14: Applications and Case Studies
- Ch 15: Prospects

---

## Chapter Summaries

### Ch 1: The Reinforcement Learning Problem (pp. 1-25)
**핵심**: 환경과의 상호작용을 통해 학습하는 에이전트라는 기본 틀을 제시한다. RL의 핵심 요소(정책, 보상 신호, 가치 함수, 환경 모델)를 정의하고, 지도 학습과의 차이를 명확히 한다. 틱택토 예제를 통해 가치 함수 기반 학습의 직관을 제공한다. RL의 역사(시행착오 학습, 최적 제어, TD 학습)를 요약한다.
**키워드**: `agent-environment`, `policy`, `reward signal`, `value function`, `exploration-exploitation`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 1 (line 836)

### Ch 2: Multi-arm Bandits (pp. 27-52)
**핵심**: 가장 단순한 RL 설정인 n-armed 밴딧 문제를 소개한다. 행동 가치 추정(sample average), 탐욕적/ε-탐욕적 전략, 증분적 갱신 규칙을 설명한다. 비정상 문제에 대한 지수 가중 평균, 낙관적 초기값, UCB(Upper-Confidence-Bound), 기울기 밴딧(gradient bandit) 알고리즘을 다룬다.
**키워드**: `epsilon-greedy`, `UCB`, `gradient bandit`, `incremental update`, `exploration`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 2 (line 2167)

### Ch 3: Finite Markov Decision Processes (pp. 53-79)
**핵심**: 에이전트-환경 인터페이스를 MDP로 형식화한다. 보상 가설, 수익(return), 할인(discount)의 개념을 정의한다. 마르코프 성질을 설명하고, 상태 가치 함수 vπ와 행동 가치 함수 qπ에 대한 벨만 방정식을 유도한다. 최적 가치 함수와 최적 정책의 존재를 증명한다.
**키워드**: `MDP`, `Bellman equation`, `value function`, `optimal policy`, `discount factor`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 3 (line 3743)

### Ch 4: Dynamic Programming (pp. 89-107)
**핵심**: 완전한 환경 모델이 주어졌을 때의 정책 평가(반복 정책 평가)와 정책 개선 정리를 설명한다. 정책 반복(policy iteration)과 가치 반복(value iteration)을 유도하고, 비동기 DP와 일반화된 정책 반복(GPI) 프레임워크를 제시한다.
**키워드**: `policy evaluation`, `policy iteration`, `value iteration`, `GPI`, `dynamic programming`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 4 (line 155)

### Ch 5: Monte Carlo Methods (pp. 113-138)
**핵심**: 모델 없이 에피소드 경험에서 직접 학습하는 몬테카를로 방법을 소개한다. 첫 방문/모든 방문 MC 예측, 탐색적 출발(exploring starts)을 이용한 MC 제어를 설명한다. 중요도 샘플링을 통한 오프폴리시 예측과 제어, 절단된 수익에 대한 중요도 샘플링을 다룬다.
**키워드**: `Monte Carlo prediction`, `exploring starts`, `importance sampling`, `off-policy`, `episode`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 5 (line 219)

### Ch 6: Temporal-Difference Learning (pp. 143-161)
**핵심**: TD 예측의 핵심 아이디어(부트스트래핑)를 소개하고, MC/DP와의 차이를 분석한다. TD(0)의 최적성(배치 학습에서 최대우도 해)을 보여준다. Sarsa(온폴리시)와 Q-learning(오프폴리시) TD 제어를 도입하고, 절벽 걷기 예제로 비교한다.
**키워드**: `TD(0)`, `Sarsa`, `Q-learning`, `bootstrapping`, `on-policy vs off-policy`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 6 (line 10382)

### Ch 7: Eligibility Traces (pp. 167-190)
**핵심**: n-step TD를 통해 MC와 TD의 스펙트럼을 연결한다. TD(λ)의 전방 관점(λ-수익)과 후방 관점(적격 흔적)을 설명하고, 두 관점의 동등성을 증명한다. Sarsa(λ), Watkins의 Q(λ), 오프폴리시 적격 흔적(중요도 샘플링)을 다룬다.
**키워드**: `eligibility traces`, `TD(λ)`, `n-step TD`, `forward view`, `backward view`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 7 (line 309)

### Ch 8: Planning and Learning with Tabular Methods (pp. 195-220)
**핵심**: 모델 기반 계획(planning)과 모델 프리 학습을 통합하는 Dyna 아키텍처를 소개한다. 모델이 부정확할 때의 문제(Dyna-Q+)와 우선 순위 스위핑(prioritized sweeping)을 다룬다. 전체/샘플 백업의 비교, 궤적 샘플링, 휴리스틱 탐색, 몬테카를로 트리 탐색(MCTS)을 설명한다.
**키워드**: `Dyna`, `planning`, `model-based`, `prioritized sweeping`, `MCTS`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 8 (line 13439)

### Ch 9: On-policy Approximation of Action Values (pp. 225-249)
**핵심**: 상태 공간이 클 때 함수 근사(function approximation)를 도입한다. 경사 하강 기반 가치 예측(SGD)과 선형 방법(특징 구성: 다항식, 푸리에, 타일 코딩, RBF)을 설명한다. 함수 근사를 이용한 온폴리시 제어와 부트스트래핑 여부의 비교를 다룬다.
**키워드**: `function approximation`, `tile coding`, `linear methods`, `SGD`, `feature construction`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 9 (line 14718)

### Ch 10: Off-policy Approximation of Action Values (p. 255)
**핵심**: 오프폴리시 환경에서의 함수 근사 문제를 다루는 장이다. 행동 정책과 타깃 정책이 다를 때 발생하는 학습의 불안정성 문제를 논의한다.
**키워드**: `off-policy`, `function approximation`, `stability`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 10 (line 435)

### Ch 11: Policy Approximation (pp. 257-263)
**핵심**: 가치 함수가 아닌 정책을 직접 매개변수화하는 접근법을 소개한다. 액터-크리틱(actor-critic) 방법과 적격 흔적의 결합을 설명한다. R-learning과 평균 보상 설정을 다룬다.
**키워드**: `actor-critic`, `policy gradient`, `R-learning`, `average reward`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 11 (line 437)

### Ch 12: Psychology (p. 269)
**핵심**: 강화학습과 동물 학습 심리학(고전적/조작적 조건화)의 연결을 논의한다. 보상 예측 오차와 행동주의 학습 이론의 관계를 다룬다.
**키워드**: `conditioning`, `reward prediction error`, `animal learning`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 12 (line 457)

### Ch 13: Neuroscience (p. 271)
**핵심**: 도파민 뉴런의 발화 패턴과 TD 오차의 유사성을 중심으로 RL과 신경과학의 관계를 설명한다.
**키워드**: `dopamine`, `TD error`, `basal ganglia`, `neuroscience`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 13 (line 459)

### Ch 14: Applications and Case Studies (pp. 273-301)
**핵심**: TD-Gammon(백개먼), Samuel의 체커 프로그램, Acrobot, 엘리베이터 배차, 동적 채널 할당, 작업 공정 스케줄링 등 RL의 주요 응용 사례를 상세히 분석한다.
**키워드**: `TD-Gammon`, `game playing`, `scheduling`, `elevator dispatching`, `channel allocation`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 14 (line 461)

### Ch 15: Prospects (pp. 303-306)
**핵심**: RL의 통합적 관점(GPI의 보편성)을 제시하고, 상태 추정, 시간적 추상화(옵션), 예측적 표현 등 미래 연구 방향을 전망한다.
**키워드**: `GPI`, `temporal abstraction`, `options`, `predictive representations`, `future directions`
**상세**: → `Reinforcement Learning An Introduction_full.md` Ch 15 (line 499)
