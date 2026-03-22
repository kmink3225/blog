---
name: "Reinforcement Learning: An Introduction"
type: book-summary
authors: "Richard S. Sutton, Andrew G. Barto"
year: 2015
total_pages: 338
language: en
keywords: [reinforcement learning, MDP, temporal-difference learning, Q-learning, policy gradient, Monte Carlo methods, dynamic programming, eligibility traces, function approximation, actor-critic]
sources:
  - file: "Sutton-RL_marker_full.md"
    tool: Marker
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

> Marker 원본: `Sutton-RL_marker_full.md` | 총 ~4,412 라인 | `L:숫자`로 직접 접근 가능


### Ch 1: The Reinforcement Learning Problem (pp. 1-25)
**핵심**: 환경과의 상호작용을 통해 학습하는 에이전트라는 기본 틀을 제시한다. RL의 핵심 요소(정책, 보상 신호, 가치 함수, 환경 모델)를 정의하고, 지도 학습과의 차이를 명확히 한다. 틱택토 예제를 통해 가치 함수 기반 학습의 직관을 제공한다. RL의 역사(시행착오 학습, 최적 제어, TD 학습)를 요약한다.
**키워드**: `agent-environment`, `policy`, `reward signal`, `value function`, `exploration-exploitation`
**상세**: → `Sutton-RL_marker_full.md` Ch 1 (L:150)
이 장은 강화학습의 기본 틀을 소개하며, 환경과 상호작용하면서 목표를 달성하기 위해 학습하는 에이전트라는 핵심 개념을 제시한다. 강화학습은 지도 학습과 달리 올바른 행동을 알려주는 교사가 없고, 행동의 결과로 받는 평가적 피드백(evaluative feedback)을 통해 학습한다. RL의 네 가지 핵심 요소로 정책(policy), 보상 신호(reward signal), 가치 함수(value function), 환경 모델(model)을 정의한다. 탐색(exploration)과 활용(exploitation) 사이의 균형이 RL만의 고유한 도전 과제임을 강조한다. 틱택토 예제를 통해 가치 함수 기반 학습의 직관을 제공하며, 상태의 가치를 추정하고 시간차 학습으로 갱신하는 방식을 보여준다. RL의 역사를 세 갈래로 정리한다: Thorndike의 시행착오 학습에서 비롯된 심리학적 전통, Bellman의 최적 제어와 동적 프로그래밍 전통, 그리고 시간차(TD) 학습의 독자적 발전이다. 이 세 흐름이 1980년대 후반 하나로 합류하여 현대 RL이 형성되었음을 설명한다. 교과서 전체의 구조(표 기반 방법 → 함수 근사 → 프론티어)를 개괄하며, RL이 인공지능의 일반적 학습 패러다임으로서 갖는 잠재력을 제시한다.

### Ch 2: Multi-arm Bandits (pp. 27-52)
**핵심**: 가장 단순한 RL 설정인 n-armed 밴딧 문제를 소개한다. 행동 가치 추정(sample average), 탐욕적/ε-탐욕적 전략, 증분적 갱신 규칙을 설명한다. 비정상 문제에 대한 지수 가중 평균, 낙관적 초기값, UCB(Upper-Confidence-Bound), 기울기 밴딧(gradient bandit) 알고리즘을 다룬다.
**키워드**: `epsilon-greedy`, `UCB`, `gradient bandit`, `incremental update`, `exploration`
**상세**: → `Sutton-RL_marker_full.md` Ch 2 (L:477)
이 장은 RL의 가장 단순한 형태인 n-armed 밴딧 문제를 통해 탐색과 활용의 균형 문제를 다룬다. 행동 가치를 추정하는 가장 자연스러운 방법인 표본 평균(sample-average)법을 소개하고, 탐욕적(greedy) 행동 선택과 ε-탐욕적(ε-greedy) 행동 선택을 비교한다. 10-armed 테스트베드 실험에서 ε-greedy가 순수 greedy보다 장기적으로 우수함을 보여준다. 증분적 갱신 규칙 Qk+1 = Qk + (1/k)[Rk - Qk]을 유도하여 메모리 효율적인 구현을 제시한다. 비정상(nonstationary) 문제에 대응하기 위해 고정 스텝 크기 α를 사용하는 지수 가중 이동 평균(exponential recency-weighted average)을 도입한다. 수렴 조건으로 확률적 근사 이론의 표준 조건(Σαk = ∞, Σαk² < ∞)을 제시한다. 낙관적 초기값(optimistic initial values)을 통한 탐색 장려와 UCB(Upper-Confidence-Bound) 행동 선택 방법을 설명한다. 기울기 밴딧(gradient bandit) 알고리즘은 행동 선호도(preference)를 소프트맥스로 변환하여 확률적으로 행동을 선택하며, 기준선(baseline) 사용의 중요성을 보여준다. 마지막으로 연관 탐색(associative search, contextual bandits)을 소개하여 밴딧 문제에서 완전한 RL 문제로의 확장 방향을 제시한다.

### Ch 3: Finite Markov Decision Processes (pp. 53-79)
**핵심**: 에이전트-환경 인터페이스를 MDP로 형식화한다. 보상 가설, 수익(return), 할인(discount)의 개념을 정의한다. 마르코프 성질을 설명하고, 상태 가치 함수 vπ와 행동 가치 함수 qπ에 대한 벨만 방정식을 유도한다. 최적 가치 함수와 최적 정책의 존재를 증명한다.
**키워드**: `MDP`, `Bellman equation`, `value function`, `optimal policy`, `discount factor`
**상세**: → `Sutton-RL_marker_full.md` Ch 3 (L:836)
이 장은 유한 마르코프 결정 과정(finite MDP)의 수학적 틀을 체계적으로 정립한다. 에이전트-환경 인터페이스를 상태, 행동, 보상의 순차적 상호작용으로 형식화하고, 전이 확률 p(s',r|s,a)로 환경의 역학을 완전히 기술한다. 수익(return)을 에피소드적 과제에서는 보상의 단순 합, 연속적 과제에서는 할인된 보상의 합 Gt = Σγ^k R_{t+k+1}로 정의한다. 흡수 상태(absorbing state)를 도입하여 에피소드적 과제와 연속적 과제를 통합하는 표기법을 제시한다. 마르코프 성질을 형식적으로 정의하며, 미래 상태와 보상이 현재 상태와 행동에만 의존하는 조건임을 설명한다. 상태 가치 함수 vπ(s)와 행동 가치 함수 qπ(s,a)를 정의하고, 벨만 방정식 vπ(s) = Σπ(a|s) Σp(s',r|s,a)[r + γvπ(s')]을 유도한다. 최적 가치 함수 v*와 q*에 대한 벨만 최적 방정식을 도출하고, 최적 정책의 존재를 증명한다. 그리드월드 예제와 재활용 로봇 예제를 통해 MDP의 개념을 구체적으로 설명한다. 장대 균형(pole-balancing) 과제와 드로 포커를 예로 들어 마르코프 상태 표현의 실용적 측면을 논의한다. 최적성과 근사(optimality and approximation)의 관계를 언급하며, 상태 공간이 거대할 때 완전한 최적 정책을 찾는 것이 비현실적임을 인정한다.

**Marker 세부 목차** (`Sutton-RL_marker_full.md`):
- 3.4 Unified Notation for Episodic and Continuing Tasks `L:866`


### Ch 4: Dynamic Programming (pp. 89-107)
**핵심**: 완전한 환경 모델이 주어졌을 때의 정책 평가(반복 정책 평가)와 정책 개선 정리를 설명한다. 정책 반복(policy iteration)과 가치 반복(value iteration)을 유도하고, 비동기 DP와 일반화된 정책 반복(GPI) 프레임워크를 제시한다.
**키워드**: `policy evaluation`, `policy iteration`, `value iteration`, `GPI`, `dynamic programming`
**상세**: → `Sutton-RL_marker_full.md` Ch 4 (L:1380)
이 장은 환경의 완전한 모델이 주어졌을 때 최적 정책을 계산하는 동적 프로그래밍(DP) 방법을 다룬다. 반복 정책 평가(iterative policy evaluation)는 벨만 방정식을 갱신 규칙으로 변환하여 vπ를 계산하며, 수렴이 보장된다. 정책 개선 정리(policy improvement theorem)를 증명하여, 현재 가치 함수에 대해 탐욕적인 새 정책이 원래 정책보다 반드시 같거나 나음을 보인다. 정책 반복(policy iteration)은 정책 평가와 정책 개선을 교대로 수행하여 유한 횟수 안에 최적 정책에 수렴한다. Jack의 자동차 렌탈 예제에서 정책 반복의 과정을 구체적으로 보여준다. 가치 반복(value iteration)은 정책 평가를 한 번의 스윕으로 축소한 특수한 경우로, vk+1(s) = max_a Σp(s',r|s,a)[r+γvk(s')]로 정의된다. 도박꾼 문제(Gambler's Problem)에서 가치 반복의 수렴 과정을 시각적으로 제시한다. 비동기 DP(asynchronous DP)는 상태를 체계적으로 스윕하지 않고 임의 순서로 갱신하여, 대규모 문제에서의 계산 부담을 줄인다. 일반화된 정책 반복(GPI) 프레임워크를 제시하여, 정책 평가와 정책 개선이 서로를 향해 수렴하는 일반적 구조를 설명한다. DP의 계산 효율성을 논하며, 상태 수에 대해 다항 시간이 소요되어 직접 탐색보다 지수적으로 빠름을 지적한다.

### Ch 5: Monte Carlo Methods (pp. 113-138)
**핵심**: 모델 없이 에피소드 경험에서 직접 학습하는 몬테카를로 방법을 소개한다. 첫 방문/모든 방문 MC 예측, 탐색적 출발(exploring starts)을 이용한 MC 제어를 설명한다. 중요도 샘플링을 통한 오프폴리시 예측과 제어, 절단된 수익에 대한 중요도 샘플링을 다룬다.
**키워드**: `Monte Carlo prediction`, `exploring starts`, `importance sampling`, `off-policy`, `episode`
**상세**: → `Sutton-RL_marker_full.md` Ch 5 (L:1770)
이 장은 환경 모델 없이 실제 경험 에피소드에서 직접 가치 함수를 학습하는 몬테카를로(MC) 방법을 소개한다. 첫 방문 MC(first-visit MC)와 모든 방문 MC(every-visit MC) 예측 방법을 구분하며, 에피소드 종료 후 관측된 수익의 평균으로 가치를 추정한다. MC 제어를 위해 상태 가치 대신 행동 가치 qπ(s,a)를 학습해야 하는 이유를 설명한다. 탐색적 출발(exploring starts) 가정 하에서 MC 제어가 최적 정책에 수렴함을 보인다. ε-soft 정책을 사용하여 탐색적 출발 가정을 제거한 온폴리시 MC 제어를 제시한다. 오프폴리시 학습을 위한 중요도 샘플링(importance sampling)을 도입하며, 중요도 샘플링 비율 ρ = Π(π(Ak|Sk)/μ(Ak|Sk))이 환경의 전이 확률에 독립적임을 보인다. 일반(ordinary) 중요도 샘플링은 불편추정량이나 분산이 무한할 수 있고, 가중(weighted) 중요도 샘플링은 편향되지만 분산이 극적으로 낮아 실용적으로 선호됨을 블랙잭 예제로 입증한다. 무한 분산 예제(단일 상태 MDP)로 일반 중요도 샘플링의 문제를 극명하게 보여준다. 증분적 구현(incremental implementation)을 통해 가중 중요도 샘플링을 온라인으로 효율적으로 수행하는 방법을 제시한다. 절단된 수익에 대한 중요도 샘플링으로 분산을 더욱 줄이는 고급 기법도 다룬다.

### Ch 6: Temporal-Difference Learning (pp. 143-161)
**핵심**: TD 예측의 핵심 아이디어(부트스트래핑)를 소개하고, MC/DP와의 차이를 분석한다. TD(0)의 최적성(배치 학습에서 최대우도 해)을 보여준다. Sarsa(온폴리시)와 Q-learning(오프폴리시) TD 제어를 도입하고, 절벽 걷기 예제로 비교한다.
**키워드**: `TD(0)`, `Sarsa`, `Q-learning`, `bootstrapping`, `on-policy vs off-policy`
**상세**: → `Sutton-RL_marker_full.md` Ch 6 (L:2200)
이 장은 시간차(TD) 학습이라는 RL의 핵심 방법을 소개하며, MC와 DP 양쪽의 장점을 결합한다. TD(0) 예측은 V(St) ← V(St) + α[Rt+1 + γV(St+1) - V(St)]로, 에피소드 종료를 기다리지 않고 매 스텝 갱신한다(부트스트래핑). MC처럼 모델 없이 경험에서 학습하면서도, DP처럼 다른 추정값을 사용하여 현재 추정값을 갱신하는 것이 TD의 핵심이다. 배치 학습에서 TD(0)는 최대우도 마르코프 모델의 확실성 등가 추정(certainty-equivalence estimate)으로 수렴하여, 제한된 데이터에서 MC보다 빠르게 수렴함을 랜덤 워크 예제로 입증한다. Sarsa 알고리즘은 온폴리시 TD 제어로, Q(St,At) ← Q(St,At) + α[Rt+1 + γQ(St+1,At+1) - Q(St,At)]이며 (S,A,R,S',A') 다섯 원소에서 이름이 유래했다. Q-learning은 오프폴리시 TD 제어로, Q(St,At) ← Q(St,At) + α[Rt+1 + γ max_a Q(St+1,a) - Q(St,At)]이며, 따르는 정책과 독립적으로 최적 행동 가치 함수 q*에 직접 수렴한다. 절벽 걷기(cliff walking) 예제에서 Sarsa는 안전한 우회 경로를, Q-learning은 절벽 가장자리의 최적 경로를 학습하지만 ε-greedy 탐색으로 인해 온라인 성능이 낮음을 비교한다. 바둑판 이후 상태(afterstates) 개념을 도입하여, 행동의 즉각적 효과가 알려진 경우 더 효율적인 학습이 가능함을 틱택토 예제로 설명한다. TD 방법이 RL에서 가장 널리 쓰이는 이유로 단순성, 온라인 학습 가능성, 최소 계산량을 들며, 1-step, 표 기반, 모델 프리 TD 방법의 위치를 정립한다.

### Ch 7: Eligibility Traces (pp. 167-190)
**핵심**: n-step TD를 통해 MC와 TD의 스펙트럼을 연결한다. TD(λ)의 전방 관점(λ-수익)과 후방 관점(적격 흔적)을 설명하고, 두 관점의 동등성을 증명한다. Sarsa(λ), Watkins의 Q(λ), 오프폴리시 적격 흔적(중요도 샘플링)을 다룬다.
**키워드**: `eligibility traces`, `TD(λ)`, `n-step TD`, `forward view`, `backward view`
**상세**: → `Sutton-RL_marker_full.md` Ch 7 (L:2560)
이 장은 적격 흔적(eligibility traces)을 통해 MC와 TD 방법을 하나의 스펙트럼으로 연결한다. n-step TD 예측은 n 스텝 후의 수익 Gt:t+n을 부트스트랩 타깃으로 사용하여, n=1이면 TD(0), n=∞이면 MC가 되는 연속체를 형성한다. TD(λ)의 전방 관점(forward view)은 λ-수익 Gt^λ = (1-λ)Σλ^(n-1) Gt:t+n을 타깃으로 사용하며, λ가 각 n-step 수익의 가중치를 결정한다. 후방 관점(backward view)은 적격 흔적 Et(s) = γλEt-1(s) + I(s=St)를 유지하여, 과거 방문한 상태들에 TD 오차를 역방향으로 전파한다. λ=0이면 TD(0), λ=1이면 MC와 동등하며, 오프라인 갱신 시 전방/후방 관점이 수학적으로 동등함을 증명한다. 누적(accumulating), 대체(replacing), 네덜란드(dutch) 세 가지 흔적 유형을 비교하며, 대체 흔적은 상태 재방문 시 1로 리셋하고 네덜란드 흔적은 Et(St)=(1-α)γλEt-1(St)+1로 중간적 특성을 보인다. 진정한 온라인 TD(λ)(true online TD(λ))는 네덜란드 흔적과 수정된 갱신 규칙으로 온라인 λ-수익 알고리즘과 정확히 동등한 최초의 효율적 후방 관점 알고리즘이다. Sarsa(λ)는 TD(λ)를 상태-행동 쌍으로 확장한 온폴리시 제어 방법이며, 그리드월드 예제에서 적격 흔적이 학습 효율을 크게 향상시킴을 보여준다. Watkins의 Q(λ)는 Q-learning과 적격 흔적을 결합한 오프폴리시 제어로, 탐욕적이지 않은 행동 시 흔적을 0으로 리셋한다. 오프폴리시 적격 흔적에서 중요도 샘플링을 사용하는 방법도 간략히 다룬다.

**Marker 세부 목차** (`Sutton-RL_marker_full.md`):
- 7.7 Off-policy Eligibility Traces using Importance Sampling `L:2766`


### Ch 8: Planning and Learning with Tabular Methods (pp. 195-220)
**핵심**: 모델 기반 계획(planning)과 모델 프리 학습을 통합하는 Dyna 아키텍처를 소개한다. 모델이 부정확할 때의 문제(Dyna-Q+)와 우선 순위 스위핑(prioritized sweeping)을 다룬다. 전체/샘플 백업의 비교, 궤적 샘플링, 휴리스틱 탐색, 몬테카를로 트리 탐색(MCTS)을 설명한다.
**키워드**: `Dyna`, `planning`, `model-based`, `prioritized sweeping`, `MCTS`
**상세**: → `Sutton-RL_marker_full.md` Ch 8 (L:2836)
이 장은 모델 기반 계획(planning)과 모델 프리 학습(learning)을 통합하는 관점을 제시한다. 모델을 분포 모델(distribution model)과 샘플 모델(sample model)로 구분하고, 계획을 모델을 입력으로 받아 정책을 생성하는 계산 과정으로 정의한다. 모든 상태 공간 계획 방법의 공통 구조는 가치 함수의 백업 연산이며, 학습과 계획은 경험의 출처(실제 vs 시뮬레이션)만 다를 뿐 동일한 알고리즘을 사용할 수 있다. Dyna 아키텍처는 직접 RL, 모델 학습, 계획을 하나의 에이전트에 통합하며, Dyna-Q는 Q-learning을 실제 경험과 시뮬레이션 경험 모두에 적용한다. 미로 예제에서 계획 스텝 수(n)가 많을수록 학습이 극적으로 빨라짐을 보여준다. 모델이 틀렸을 때의 문제를 차단 미로(blocking maze)와 지름길 미로(shortcut maze) 예제로 설명하며, Dyna-Q+는 탐색 보너스(exploration bonus)로 오래 방문하지 않은 상태-행동 쌍의 재탐색을 장려한다. 우선 순위 스위핑(prioritized sweeping)은 가치 변화가 큰 상태부터 우선적으로 백업하여 계획 효율을 높인다. 전체 백업과 샘플 백업을 비교하며, 분기 계수가 크면 샘플 백업이 유리함을 분석한다. 궤적 샘플링(trajectory sampling)은 온폴리시 분포에 따라 상태를 방문하여, 관련 없는 상태의 불필요한 백업을 피한다. 휴리스틱 탐색과 몬테카를로 트리 탐색(MCTS)을 RL 관점에서 재해석하며, 이들이 동일한 가치 함수 백업 프레임워크의 변형임을 보인다.

### Ch 9: On-policy Approximation of Action Values (pp. 225-249)
**핵심**: 상태 공간이 클 때 함수 근사(function approximation)를 도입한다. 경사 하강 기반 가치 예측(SGD)과 선형 방법(특징 구성: 다항식, 푸리에, 타일 코딩, RBF)을 설명한다. 함수 근사를 이용한 온폴리시 제어와 부트스트래핑 여부의 비교를 다룬다.
**키워드**: `function approximation`, `tile coding`, `linear methods`, `SGD`, `feature construction`
**상세**: → `Sutton-RL_marker_full.md` Ch 9 (L:3141)
이 장은 상태 공간이 거대할 때 표 기반 방법의 한계를 극복하기 위해 함수 근사(function approximation)를 도입한다. 근사 가치 함수 v̂(s,w)를 매개변수 벡터 w로 표현하며, 하나의 상태 갱신이 다른 상태들로 일반화(generalization)되는 것이 핵심이다. 백업을 s→v 형태의 훈련 예제로 해석하여, 기존 지도 학습 방법을 RL에 적용하는 프레임워크를 제시한다. 성능 측정으로 온폴리시 분포 d(s)에 대한 RMSE를 정의하고, 온폴리시 분포가 이론적 수렴 보장과 훈련 데이터 생성 모두에 자연스러움을 설명한다. 경사 하강법(gradient descent)의 일반 갱신 규칙 wt+1 = wt + α[Vt - v̂(St,wt)]∇v̂(St,wt)를 유도하며, MC 타깃(Gt)은 불편추정이므로 지역 최적해 수렴이 보장되나 부트스트래핑 타깃(TD, DP)은 불편추정이 아님을 지적한다. 경사 하강 TD(λ)의 전방/후방 관점을 함수 근사로 확장하며, 적격 흔적 벡터 et의 갱신 규칙을 제시한다. 선형 방법에서 v̂(s,w) = w⊤x(s)로 특징 벡터와 가중치의 내적으로 가치를 근사하며, 다항식, 푸리에 기저, 타일 코딩(tile coding), 방사 기저 함수(RBF) 등 다양한 특징 구성법을 설명한다. 타일 코딩은 연속 상태 공간을 격자로 분할하여 이진 특징을 생성하는 효율적 방법이다. 함수 근사를 사용한 온폴리시 제어에서 부트스트래핑 여부에 따른 성능 차이를 산악 자동차 과제로 비교하며, 부트스트래핑(Sarsa(λ))이 MC보다 우수한 경우가 많음을 보여준다.

**Marker 세부 목차** (`Sutton-RL_marker_full.md`):
- 9.1 Value Prediction with Function Approximation `L:3151`


### Ch 10: Off-policy Approximation of Action Values (p. 255)
**핵심**: 오프폴리시 환경에서의 함수 근사 문제를 다루는 장이다. 행동 정책과 타깃 정책이 다를 때 발생하는 학습의 불안정성 문제를 논의한다.
**키워드**: `off-policy`, `function approximation`, `stability`
**상세**: → `Sutton-RL_marker_full.md` Ch 10 (L:3573)
이 장은 오프폴리시 환경에서 함수 근사를 사용할 때 발생하는 학습의 불안정성 문제를 다루는 짧은 장이다. 행동 정책(behavior policy)과 타깃 정책(target policy)이 다를 때, 부트스트래핑과 함수 근사의 결합이 발산(divergence) 문제를 일으킬 수 있음을 지적한다. 이 문제는 2판에서 확장 논의될 예정인 중요한 연구 주제로 남겨진다.

### Ch 11: Policy Approximation (pp. 257-263)
**핵심**: 가치 함수가 아닌 정책을 직접 매개변수화하는 접근법을 소개한다. 액터-크리틱(actor-critic) 방법과 적격 흔적의 결합을 설명한다. R-learning과 평균 보상 설정을 다룬다.
**키워드**: `actor-critic`, `policy gradient`, `R-learning`, `average reward`
**상세**: → `Sutton-RL_marker_full.md` Ch 11 (L:3577)
이 장은 가치 함수를 간접적으로 사용하는 대신 정책을 직접 매개변수화하여 학습하는 접근법을 소개한다. 액터-크리틱(actor-critic) 방법은 정책(액터)과 가치 함수(크리틱)를 별도의 메모리 구조로 유지하며, TD 오차 δt = Rt+1 + γV(St+1) - V(St)가 유일한 학습 신호이다. 액터는 Gibbs 소프트맥스로 행동을 선택하고, TD 오차가 양이면 해당 행동의 선호도를 높이고 음이면 낮춘다. 액터-크리틱의 두 가지 장점으로 연속 행동 공간에서의 효율적 행동 선택과 명시적 확률적 정책 학습 능력을 든다. 적격 흔적을 액터-크리틱에 결합하는 방법을 설명하며, 크리틱은 상태별 흔적, 액터는 상태-행동 쌍별 흔적을 각각 유지한다. R-learning은 할인하지 않는 연속 과제를 위한 오프폴리시 제어 방법으로, 평균 보상 설정(average-reward setting)을 도입한다. 평균 보상 r̄(π)에 대한 상대 가치(relative values)를 정의하여, 보상에서 평균 보상을 뺀 차이의 누적합으로 상태 가치를 정의한다. R-learning의 갱신 규칙은 Q-learning과 유사하나 할인 대신 추정된 평균 보상 R̄를 사용하며, 탐욕적 행동이 선택된 경우에만 R̄를 갱신한다. 접근 제어 큐잉 과제(access-control queuing task) 예제에서 R-learning이 우선순위에 따른 최적 접근 제어 정책을 학습하는 과정을 보여준다.

**Marker 세부 목차** (`Sutton-RL_marker_full.md`):
- 11.3 R-Learning and the Average-Reward Setting `L:3644`


### Ch 12: Psychology (p. 269)
**핵심**: 강화학습과 동물 학습 심리학(고전적/조작적 조건화)의 연결을 논의한다. 보상 예측 오차와 행동주의 학습 이론의 관계를 다룬다.
**키워드**: `conditioning`, `reward prediction error`, `animal learning`
**상세**: → `Sutton-RL_marker_full.md` Ch 12 (L:3688)
이 장은 강화학습과 동물 학습 심리학의 연결을 논의하는 장이나, 이 판본에서는 제목만 제시되어 있다. 2판에서 고전적 조건화(classical conditioning)와 조작적 조건화(operant conditioning)에서의 보상 예측 오차, 행동주의 학습 이론과 TD 학습의 관계를 확장할 예정이다. 1판에서는 동물 학습 실험에서 관찰된 현상(차단, 억제 등)이 TD 모델로 설명 가능함을 보였다.

### Ch 13: Neuroscience (p. 271)
**핵심**: 도파민 뉴런의 발화 패턴과 TD 오차의 유사성을 중심으로 RL과 신경과학의 관계를 설명한다.
**키워드**: `dopamine`, `TD error`, `basal ganglia`, `neuroscience`
**상세**: → `Sutton-RL_marker_full.md` Ch 13 (L:3690)
이 장은 강화학습과 신경과학의 관계를 다루는 장이나, 이 판본에서는 제목만 제시되어 있다. 2판에서 도파민 뉴런의 발화 패턴과 TD 오차 신호의 유사성, 기저핵(basal ganglia)의 보상 처리 회로, 피질-기저핵 루프의 액터-크리틱 구조 등을 확장할 예정이다. Schultz 등의 실험에서 도파민 뉴런이 예상치 못한 보상에 반응하고 예상된 보상에는 반응하지 않는 패턴이 TD 오차와 일치함이 밝혀진 것은 RL과 신경과학의 가장 중요한 교차점이다.

### Ch 14: Applications and Case Studies (pp. 273-301)
**핵심**: TD-Gammon(백개먼), Samuel의 체커 프로그램, Acrobot, 엘리베이터 배차, 동적 채널 할당, 작업 공정 스케줄링 등 RL의 주요 응용 사례를 상세히 분석한다.
**키워드**: `TD-Gammon`, `game playing`, `scheduling`, `elevator dispatching`, `channel allocation`
**상세**: → `Sutton-RL_marker_full.md` Ch 14 (L:3692)
이 장은 RL의 주요 응용 사례를 상세히 분석한다. TD-Gammon은 TD(λ)와 다층 신경망을 결합하여 백개먼을 거의 세계 최고 수준으로 학습했으며, 최소한의 도메인 지식으로 자기 대국(self-play)을 통해 30만 게임 만에 기존 프로그램과 동등해졌다. 입력 표현(198 유닛)과 시그모이드 은닉층의 설계를 상세히 기술한다. Samuel의 체커 프로그램은 역사적으로 RL의 선구적 사례이다. Acrobot은 2관절 로봇으로, Sarsa(λ)와 선형 함수 근사(타일 코딩, 48개 타일링)를 사용하여 스윙업 과제를 학습한다. 엘리베이터 배차는 10^22 이상의 상태를 가진 실용적 문제로, 준마르코프 결정 과정(semi-MDP)으로 형식화하고 신경망 기반 Q-learning으로 해결하며, 기존 산업용 디스패처와 동등하거나 우수한 성능을 달성했다. 동적 채널 할당은 셀룰러 전화 시스템에서 채널 재사용 제약 하에 통화 차단을 최소화하는 문제로, 선형 TD(0)와 가용성/패킹 특징으로 고정 할당 및 BDCL보다 낮은 차단률을 달성했다. 작업 공정 스케줄링(NASA 우주 왕복선 화물)은 스케줄을 상태로, 수리 연산을 행동으로 하는 계획 공간(plan-space) RL의 최초 성공 사례로, TD(λ)와 TDNN으로 반복 수리 알고리즘보다 적은 수리 횟수로 동등한 품질의 스케줄을 찾았다.

### Ch 15: Prospects (pp. 303-306)
**핵심**: RL의 통합적 관점(GPI의 보편성)을 제시하고, 상태 추정, 시간적 추상화(옵션), 예측적 표현 등 미래 연구 방향을 전망한다.
**키워드**: `GPI`, `temporal abstraction`, `options`, `predictive representations`, `future directions`
**상세**: → `Sutton-RL_marker_full.md` Ch 15 (L:3962)
이 장은 RL의 통합적 관점을 제시하고 미래 연구 방향을 전망한다. 모든 RL 방법의 세 가지 공통 아이디어로 가치 함수 추정, 백업 연산, 일반화된 정책 반복(GPI)을 제시한다. 방법 공간의 핵심 차원으로 백업의 깊이(1-step TD ~ 완전 수익 MC)와 폭(샘플 백업 ~ 전체 백업)을 도식화하여 DP, TD, MC를 하나의 프레임워크에 배치한다. 함수 근사, 온폴리시/오프폴리시, 에피소드/연속 과제, 동기/비동기, 대체/누적 흔적, 실제/시뮬레이션 경험 등 추가적인 방법 차원을 열거한다. 비마르코프 환경에 대한 확장으로 부분 관측 MDP(POMDP)와 베이지안 접근을 논의하며, 관측에서 마르코프 상태 신호를 구축하는 문제가 미해결임을 지적한다. 모듈성과 계층적 RL(시간적 추상화, 옵션 프레임워크)의 필요성을 강조하며, 원시 행동뿐 아니라 신발 끈 묶기나 전화하기 같은 복합 행동을 계획과 학습에 사용할 수 있어야 함을 설명한다. 과제 구조 활용(변수 독립성, 문제 분해), 다중 에이전트 RL, 그리고 조언이나 시범을 통한 학습 가속화(셰이핑)의 가능성을 전망한다. RL이 특수 목적 교사나 도메인 지식 없이도 작동하면서, 이러한 것들이 가용할 때 활용할 수 있는 충분히 일반적인 학습 접근법임을 결론짓는다.


### 기타 섹션 (Marker)

- Part I Tabular Solution Methods `L:467`
- \*5.8 Importance Sampling on Truncated Returns `L:1947`
- Planning and Learning with Tabular Methods `L:2836`
- Part II Approximate Solution Methods `L:3141`
- On-policy Approximation of Action Values `L:3143`
- Off-policy Approximation of Action Values `L:3573`

---

## Marker 세부 목차

> `L:숫자`는 `Sutton-RL_marker_full.md`의 라인 번호.

- Part I Tabular Solution Methods `L:467`
- 3.4 Unified Notation for Episodic and Continuing Tasks `L:866`
- \*5.8 Importance Sampling on Truncated Returns `L:1947`
- 7.7 Off-policy Eligibility Traces using Importance Sampling `L:2766`
- Planning and Learning with Tabular Methods `L:2836`
- Part II Approximate Solution Methods `L:3141`
- On-policy Approximation of Action Values `L:3143`
- 9.1 Value Prediction with Function Approximation `L:3151`
- Off-policy Approximation of Action Values `L:3573`
- 11.3 R-Learning and the Average-Reward Setting `L:3644`
