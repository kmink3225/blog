---
name: "Matrix Differential Calculus with Applications in Statistics and Econometrics, Third Edition"
type: book-summary
sources:
  - file: "Magnus-MatrixDifferentialCalculus_azure_full.md"
    tool: Document Intelligence
authors: "Jan R. Magnus, Heinz Neudecker"
year: 2007
total_pages: 470
language: en
keywords: [matrix calculus, differentials, Jacobian, Hessian, Kronecker product, vec operator, eigenvalues, inequalities, linear regression, maximum likelihood, econometrics]
---

# Matrix Differential Calculus with Applications in Statistics and Econometrics — Summary

> Jan R. Magnus, Heinz Neudecker (2007, 3rd ed.), 470 pages, 17 chapters (6 Parts)
> 행렬 미분법의 이론적 기초부터 통계학/계량경제학 응용까지 자기완결적으로 다루는 전문 교재이다.

## Contents

### Part One — Matrices
1. Basic properties of vectors and matrices (pp. 3-29)
2. Kronecker products, the vec operator and the Moore-Penrose inverse (pp. 31-45)
3. Miscellaneous matrix results (pp. 47-71)

### Part Two — Differentials: the theory
4. Mathematical preliminaries (pp. 75-88)
5. Differentials and differentiability (pp. 89-111)
6. The second differential (pp. 113-131)
7. Static optimization (pp. 133-163)

### Part Three — Differentials: the practice
8. Some important differentials (pp. 167-192)
9. First-order differentials and Jacobian matrices (pp. 193-211)
10. Second-order differentials and Hessian matrices (pp. 213-221)

### Part Four — Inequalities
11. Inequalities (pp. 225-270)

### Part Five — The linear model
12. Statistical preliminaries (pp. 275-286)
13. The linear regression model (pp. 287-322)
14. Further topics in the linear model (pp. 323-348)

### Part Six — Applications to maximum likelihood estimation
15. Maximum likelihood estimation (pp. 351-370)
16. Simultaneous equations (pp. 371-393)
17. Topics in psychometrics (pp. 395-423)

---

## Chapter Summaries

### Ch 1: Basic properties of vectors and matrices (pp. 3-29)

**핵심**: 행렬대수의 기본 정의와 정리를 요약한다. 집합론적 기초에서 출발하여 행렬의 덧셈/곱셈, 전치, 정방행렬, 일차형식/이차형식, 랭크, 역행렬, 행렬식, 대각합(trace), 분할행렬, 복소행렬, 고유값/고유벡터, Schur 분해, Jordan 분해, 특이값 분해, 양정치행렬까지 폭넓게 다룬다.

**키워드**: `행렬 기본`, `고유값`, `특이값 분해`, `양정치행렬`, `Jordan 분해`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 1 (line 1922)

이 장은 집합론적 기초(합집합, 교집합, 데카르트 곱, 유클리드 공간 R^n)에서 출발하여 행렬의 덧셈과 곱셈, 전치행렬, 정방행렬의 정의를 체계적으로 전개한다. 삼각행렬, 대칭/반대칭 행렬, 대각행렬, 항등행렬, 직교행렬 등 특수 정방행렬의 성질을 정리한다. 일차형식 a'x와 이차형식 x'Ax를 정의하고 양정치/양반정치 행렬과의 관계를 밝힌다. 행렬의 랭크를 정의하고 랭크와 가역성의 관계를 증명하며, 역행렬의 존재 조건과 성질을 다룬다. 행렬식을 여인수 전개로 정의하고 행렬식의 기본 성질(곱의 행렬식, 전치의 행렬식 등)을 증명한다. 대각합(trace)의 순환성과 선형성을 정리하고, 분할행렬(partitioned matrix)에 대한 역행렬 공식을 유도한다. 복소행렬로 확장하여 에르미트 전치와 유니터리 행렬을 소개한다. 고유값과 고유벡터를 정의하고, Schur 분해 정리를 증명하여 모든 정방행렬이 유니터리 유사변환으로 상삼각행렬이 됨을 보인다. Jordan 분해와 특이값 분해(SVD)를 제시하고, 양정치행렬의 여러 동치 조건을 정리한다.

### Ch 2: Kronecker products, the vec operator and the Moore-Penrose inverse (pp. 31-45)

**핵심**: 이후 행렬 미분법에 필수적인 도구를 개발한다. 크로네커 곱(Kronecker product)의 정의와 성질, 크로네커 곱의 고유값, vec 연산자(행렬을 열 벡터로 변환), 무어-펜로즈(Moore-Penrose) 역행렬의 존재성/유일성/성질, 그리고 선형방정식계의 풀이에 대한 응용을 다룬다.

**키워드**: `크로네커 곱`, `vec 연산자`, `무어-펜로즈 역행렬`, `일반화 역행렬`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 2 (line 3644)

크로네커 곱 A⊗B를 정의하고 결합법칙, 분배법칙, 혼합곱 성질 (A⊗B)(C⊗D) = AC⊗BD를 증명한다. 크로네커 곱의 전치, 대각합, 역행렬이 각각 개별 행렬의 전치, 대각합의 곱, 역행렬의 크로네커 곱으로 표현됨을 보인다. Schur 분해를 이용하여 A⊗B의 고유값이 A와 B의 고유값의 곱 λ_i μ_j임을 증명하고, 이로부터 양정치성의 보존, 행렬식 공식 |A⊗B| = |A|^p |B|^m, 랭크 공식 r(A⊗B) = r(A)r(B)를 유도한다. vec 연산자를 정의하여 행렬을 열 벡터로 변환하고, vec ABC = (C'⊗A) vec B라는 핵심 정리를 증명한다. vec과 trace의 관계 (vec A)' vec B = tr A'B를 증명하고 이를 4개 행렬의 곱으로 일반화한다. 무어-펜로즈(Moore-Penrose) 역행렬을 4가지 조건(AXA=A, XAX=X, (AX)'=AX, (XA)'=XA)으로 정의하고 존재성과 유일성을 증명한다. MP 역행렬을 이용한 선형방정식계의 해의 존재 조건과 일반해의 구조를 제시한다.

### Ch 3: Miscellaneous matrix results (pp. 47-71)

**핵심**: Part One의 마지막 장으로 더 전문적인 행렬 결과를 다룬다. 수반행렬(adjoint matrix), 줄친 행렬식(bordered determinants), 아다마르 곱(Hadamard product), 교환행렬(commutation matrix) K_mn, 중복행렬(duplication matrix) D_n, 경계가 있는 그라미안 행렬(bordered Gramian matrix)과 특정 행렬방정식의 풀이를 포함한다.

**키워드**: `수반행렬`, `아다마르 곱`, `교환행렬`, `중복행렬`, `그라미안 행렬`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 3 (line 4517)

수반행렬(adjoint matrix) A#=C'의 성질을 랭크별로 분석한다. r(A)=n이면 A#=|A|A^{-1}, r(A)=n-1이면 A#은 랭크 1 행렬, r(A)≤n-2이면 A#=0임을 Jordan 분해로 증명한다. 줄친 행렬식(bordered determinant) 공식을 수반행렬로 유도하고, 대칭행렬의 단순 영고유값 경우에 적용한다. 행렬방정식 AX=0의 일반해를 랭크 n-1 행렬에 대해 구하고, 특수 경우로 Ax=0의 벡터해를 제시한다. 아다마르 곱(Hadamard product, 원소별 곱)의 정의와 양정치성 보존 성질을 다루며, Schur의 정리를 증명한다. 교환행렬(commutation matrix) K_mn을 정의하여 K_mn vec A = vec A'임을 보이고, 크로네커 곱의 순서 교환 공식 K(A⊗B)K=B⊗A를 유도한다. 중복행렬(duplication matrix) D_n을 정의하여 대칭행렬의 vec과 vech를 연결하고, D_n의 무어-펜로즈 역행렬을 명시적으로 구한다. 경계가 있는 그라미안 행렬과 특정 행렬방정식의 풀이에 이 도구들을 적용한다.

### Ch 4: Mathematical preliminaries (pp. 75-88)

**핵심**: 미분론의 이론적 기초에 필요한 해석학적 예비지식을 제공한다. 내점(interior points), 집적점(accumulation points), 개집합/폐집합, 볼차노-바이어슈트라스 정리, 함수의 극한, 연속함수와 컴팩트성, 볼록집합(convex sets), 볼록/오목함수(convex/concave functions)를 다룬다.

**키워드**: `위상적 기초`, `연속성`, `볼록집합`, `볼록함수`, `컴팩트성`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 4 (line 6161)

R^n에서의 n-ball(근방)을 정의하고 내점, 집적점, 고립점, 경계점의 개념을 구분한다. 집적점의 근방에는 무한히 많은 점이 포함됨을 증명하고, 개집합과 폐집합을 정의한다. 모든 n-ball이 개집합임을 증명하고, 폐집합이 개집합의 여집합과 동치임을 보인다. 개집합의 임의 합집합과 유한 교집합이 개집합이며, 폐집합의 유한 합집합과 임의 교집합이 폐집합임을 증명한다. 유계 무한 집합에 대한 볼차노-바이어슈트라스 정리를 증명한다. 함수의 극한을 epsilon-delta 방식으로 정의하고, 연속함수의 성질을 정리한다. 컴팩트 집합(유계이고 폐인 집합)에서 연속함수의 유계성을 증명한다. 볼록집합과 볼록/오목함수를 정의하고, 볼록함수의 여러 동치 조건(에피그래프의 볼록성, 옌센 부등식 등)을 제시한다. 미분가능 볼록함수의 접선 부등식과 헤시안의 양반정치성을 증명한다. 이 장은 Part Two(미분론)의 해석학적 기초를 제공한다.

### Ch 5: Differentials and differentiability (pp. 89-111)

**핵심**: 미분(differential)의 엄밀한 정의와 이론을 전개한다. 미분가능성과 선형근사의 관계, 벡터 함수의 미분, 미분의 유일성, 편미분, 제1동치정리(first identification theorem), 미분의 존재 조건, 연쇄법칙(chain rule), 코시 불변성(Cauchy invariance), 평균값 정리를 증명한다. 행렬 함수로의 확장도 다룬다.

**키워드**: `미분`, `미분가능성`, `제1동치정리`, `연쇄법칙`, `편미분`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 5 (line 7000)

1차원에서의 미분가능성과 선형근사의 동치성에서 출발하여, 벡터 함수 f: R^n → R^m의 미분을 df(c;u) = A(c)u로 엄밀하게 정의한다. 미분가능성이 아핀 함수에 의한 1차 근사의 존재와 동치임을 보이고, 나머지 항 r_c(u)/||u||→0 조건을 제시한다. 미분(도함수 행렬) A(c)의 유일성을 증명하고, 편미분의 존재가 미분가능성을 보장하지 않음을 반례로 보인다. 제1동치정리를 증명하여 df = a'dx 형태에서 도함수 벡터 a'를 식별하는 방법을 제시한다. 편미분의 연속성이 미분가능성의 충분조건임을 증명한다. 합성함수의 연쇄법칙(chain rule)을 증명하고, 코시 불변성(Cauchy invariance)을 도출한다. 평균값 정리를 R^n에서 R^m으로의 함수에 대해 일반화하여 증명한다. 행렬 함수 F: R^{n×q} → R^{m×p}로의 확장을 다루며, vec 연산자를 통해 행렬 미분을 벡터 미분으로 환원하는 방법을 제시한다. 이 장은 미분의 올바른 정의를 강조하며, 무한소 개념이 아닌 선형근사로서의 미분을 일관되게 사용한다.

### Ch 6: The second differential (pp. 113-131)

**핵심**: 이차 편미분, 이차 미분가능성, 이차 미분(second differential)을 체계적으로 다룬다. 헤시안 행렬(Hessian matrix)을 정의하고 그 (열) 대칭성을 증명한다. 제2동치정리, 이차근사와 이차 미분가능성의 관계, 헤시안 행렬의 연쇄법칙, 테일러 정리, 고차 미분을 포함한다.

**키워드**: `이차 미분`, `헤시안 행렬`, `제2동치정리`, `테일러 정리`, `이차근사`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 6 (line 8369)

이차 편미분 D^2_{kj} f_i를 정의하고, D_{12}φ ≠ D_{21}φ인 반례를 제시하여 이차 편미분의 교환 가능성이 자동적이지 않음을 보인다. 실수함수와 벡터함수의 헤시안 행렬을 정의하고, ij-번째 원소가 D^2_{ji}φ(전치된 순서)임을 강조한다. 이차 미분가능성을 모든 편미분이 미분가능한 것으로 정의하고, 이것이 이차 테일러 공식의 존재보다 강한 조건임을 반례로 보인다. 이차 미분 d²f를 미분의 미분으로 정의하고, 제2동치정리를 증명하여 d²φ = (dx)'B dx에서 헤시안 행렬 Hφ = (1/2)(B+B')를 식별하는 방법을 제시한다. 이차 미분가능성이 이차 테일러 공식을 함의함을 증명한다. 헤시안 행렬의 (열) 대칭성이 이차 편미분의 연속성에 의해 보장됨을 증명한다. 헤시안 행렬에 대한 연쇄법칙을 유도하고, 테일러 정리를 라그랑주 나머지항과 함께 증명한다. 행렬 함수로의 확장에서 vec 연산자를 활용한 일반화를 제시한다. 고차 미분의 정의를 간략히 다루고, 고차 테일러 전개의 기초를 놓는다.

### Ch 7: Static optimization (pp. 133-163)

**핵심**: 정적 최적화 이론을 제약 없는 경우와 제약 있는 경우로 나누어 다룬다. 절대 극값의 존재, 극소의 필요조건/충분조건(1차/2차 미분 검정), 미분가능 볼록함수의 특성화, 단조변환, 라그랑주 승수법과 그 경제학적 해석을 포함한다. 부록으로 음함수 정리를 제시한다.

**키워드**: `최적화`, `라그랑주 승수`, `볼록함수`, `필요조건`, `충분조건`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 7 (line 9464)

정적 최적화를 제약 없는 경우와 제약 있는 경우로 나누어 다룬다. 국소 극소, 엄밀 국소 극소, 절대 극소를 정의하고 임계점(정류점)과 안장점의 개념을 구분한다. 바이어슈트라스 정리를 증명하여 컴팩트 집합 위의 연속함수가 절대 극값을 가짐을 보인다. 국소 극소의 필요조건으로 dφ=0(1차 조건)과 d²φ≥0(2차 조건)을 증명한다. 충분조건으로 dφ=0이고 d²φ>0(양정치)이면 엄밀 국소 극소임을 증명한다. 미분가능 볼록함수의 특성화 정리를 증명하여, 볼록함수의 임계점이 절대 극소점과 동치임을 보인다. 목적함수의 단조변환에 의한 극값의 보존을 다룬다. 등식 제약조건 g(x)=0 하의 최적화에서 라그랑주 승수법을 엄밀하게 전개한다. 라그랑주 함수 ψ = φ - λ'g의 1차/2차 조건을 유도하고, 라그랑주 승수의 경제학적 해석(그림자 가격)을 제시한다. 부록에서 음함수 정리를 증명하고 이를 제약 최적화의 기초 도구로 활용한다.

### Ch 8: Some important differentials (pp. 167-192)

**핵심**: 실전적으로 중요한 함수들의 미분을 구한다. 미분법의 기본 규칙을 정리하고, 행렬식(determinant), 역행렬, 무어-펜로즈 역행렬, 수반행렬(adjoint), 고유값과 고유벡터(대칭/복소 경우 모두)의 미분을 도출한다. 고유값 함수의 이차 미분과 중복 고유값 문제도 다룬다.

**키워드**: `행렬식 미분`, `역행렬 미분`, `고유값 미분`, `고유벡터 미분`, `MP역행렬 미분`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 8 (line 11431)

미분법의 기본 규칙(상수, 스칼라 곱, 합, 차, 곱, 몫, 거듭제곱, 로그, 지수)을 스칼라와 행렬 함수 모두에 대해 정리한다. 크로네커 곱과 아다마르 곱의 미분 규칙 d(U⊗V) = (dU)⊗V + U⊗(dV)를 증명한다. 행렬식의 미분 d|F| = tr F# dF를 수반행렬을 통해 유도하고, 비특이 경우 d|F| = |F| tr F^{-1} dF로 단순화한다. 랭크 m-1인 경우와 랭크 m-2 이하인 경우의 행렬식 미분을 별도로 다룬다. log|F|의 미분 d log|F| = tr F^{-1} dF를 도출한다. 역행렬의 미분 dF^{-1} = -F^{-1}(dF)F^{-1}을 증명한다. 무어-펜로즈 역행렬의 미분을 일반적인 경우와 풀 랭크인 경우로 나누어 유도한다. 수반행렬의 미분을 도출한다. 실수 대칭행렬의 단순 고유값과 고유벡터의 미분을 dλ = u'(dA)u와 du = -(A-λI)^+(dA)u로 구한다. 복소행렬의 고유값/고유벡터 미분도 다루며, 고유값 함수의 이차 미분과 중복 고유값 문제를 포함한다. 이 장은 이후 장들의 실전적 응용을 위한 핵심 도구를 제공한다.

### Ch 9: First-order differentials and Jacobian matrices (pp. 193-211)

**핵심**: 1차 미분으로부터 야코비 행렬(Jacobian matrix)을 식별하는 체계적 방법을 제시한다. 표기법의 좋고 나쁜 관행을 비교하고, 제1동치정리를 활용한 동치표(identification table)를 구성한다. 스칼라/벡터/행렬 함수에 대해 trace, determinant, eigenvalue의 편미분을 계산하며, 크로네커 곱과의 관계를 다룬다.

**키워드**: `야코비 행렬`, `동치표`, `편미분`, `표기법`, `크로네커 곱`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 9 (line 13011)

편미분의 배열 방식에 대해 두 가지 부적절한 표기법(∂F/∂X와 ∂F//∂X)의 문제점을 구체적으로 지적한다. 항등함수 F(X)=X에 대해 ∂F/∂X가 랭크 1 행렬이 되어 야코비 행렬의 본질을 반영하지 못함을 보인다. 올바른 표기법으로 DF(X) = ∂vec F / ∂(vec X)'를 정의하고, 이것이 야코비 행렬의 자연스러운 일반화임을 주장한다. 제1동치정리를 핵심 도구로 활용하여 d vec F = A(X) d vec X에서 DF(X) = A(X)를 식별하는 3단계 절차를 제시한다. 스칼라 함수의 편미분을 trace와 vec을 이용하여 체계적으로 계산하는 방법을 다수의 예제로 시연한다. tr AX, tr X'AX, |X|, log|X| 등의 야코비 행렬을 구한다. 벡터 함수 f(X)=Xa, 고유벡터 함수의 야코비 행렬을 구한다. 행렬 함수 F(X)=AXB, X², X^{-1}, X^+ 등의 야코비 행렬을 크로네커 곱으로 표현한다. 동치표(identification table)를 구성하여 스칼라/벡터/행렬 변수와 스칼라/벡터/행렬 함수의 9가지 조합을 체계적으로 정리한다. 이 장은 표기법의 중요성을 강조하며 실전적인 계산 방법을 체계화한다.

### Ch 10: Second-order differentials and Hessian matrices (pp. 213-221)

**핵심**: 제2동치정리를 핵심 도구로 사용하여, 이차 미분으로부터 헤시안 행렬을 식별하는 실전적 방법을 시연한다. 행렬 함수의 헤시안 행렬, 동치표(second identification table), 명시적 헤시안 공식을 제시하고, 스칼라/벡터/행렬 함수에 대해 적용한다.

**키워드**: `헤시안 행렬`, `제2동치정리`, `이차 미분`, `행렬 함수`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 10 (line 14365)

제2동치정리를 핵심 도구로 활용하여 이차 미분에서 헤시안 행렬을 식별하는 실전적 방법을 시연한다. 스칼라 함수 φ(x)에 대해 d²φ = (dx)'B dx이면 Hφ = (1/2)(B+B')임을 적용하고, 벡터/행렬 함수로 확장한다. 행렬 함수 F(X)의 헤시안 행렬을 HF(X) = D(DF(X))'로 정의하고, 이것이 mpnq × nq 행렬임을 명시한다. 이차 동치표(second identification table)를 구성하여 9가지 함수-변수 조합에 대한 헤시안 식별 공식을 일목요연하게 정리한다. 편미분을 통한 명시적 헤시안 공식을 제시하고, 동치표 사용이 어려운 경우의 대안으로 활용한다. 스칼라 함수 φ(X) = |X|의 헤시안을 비특이점에서 계산하고 n≥2일 때 비특이임을 보인다. φ(x) = a'x와 φ(x) = x'Ax의 헤시안을 각각 0과 (1/2)(A+A')로 구한다. 벡터 함수와 행렬 함수의 헤시안 계산에서 (B')_v 연산(각 블록의 전치를 쌓는 연산)의 역할을 설명한다. 이 장은 9장의 1차 미분 기법을 2차로 확장하여 최적화의 충분조건 검증에 필수적인 도구를 제공한다.

### Ch 11: Inequalities (pp. 225-270)

**핵심**: 행렬 부등식을 포괄적으로 다룬다. 코시-슈바르츠 부등식, 산술-기하 평균 정리, 레일리 몫(Rayleigh quotient), 고유값의 변분적 기술, 피셔의 min-max 정리, 푸앵카레 분리정리, 아다마르 부등식, 카라마타 부등식, 횔더/민코프스키 부등식, 최소제곱법과 일반화 최소제곱법의 부등식을 증명한다.

**키워드**: `코시-슈바르츠`, `레일리 몫`, `min-max 정리`, `아다마르 부등식`, `민코프스키`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 11 (line 14970)

코시-슈바르츠 부등식 (a'b)² ≤ (a'a)(b'b)를 두 가지 방법(trace 방법, 멱등행렬 방법)으로 증명하고 등호 조건을 밝힌다. 행렬 유사체로 (tr A'B)², tr(A'B)², |A'B|²에 대한 부등식을 증명한다. 산술-기하 평균 부등식의 가중 버전을 미분법으로 증명하고, |A|^{1/n} ≤ (1/n)tr A를 양반정치행렬에 대해 유도한다. 레일리 몫(Rayleigh quotient) x'Ax/x'x의 상한과 하한이 각각 최대/최소 고유값임을 증명한다. 피셔의 min-max 정리를 증명하여 대칭행렬의 고유값을 변분적으로 기술한다. 푸앵카레 분리정리를 유도하여 주 부분행렬의 고유값이 원래 행렬의 고유값 사이에 끼임을 보인다. 아다마르 부등식 |A| ≤ Π a_{ii}를 양정치행렬에 대해 증명한다. 카라마타 부등식을 활용하여 (tr A^p)^{1/p}의 표현 정리를 증명하고, 이로부터 횔더 부등식과 민코프스키 부등식의 행렬 유사체를 유도한다. 민코프스키 행렬식 정리 |A+B|^{1/n} ≥ |A|^{1/n}+|B|^{1/n}을 증명한다. 최소제곱법과 일반화 최소제곱법에 관련된 부등식을 다루며, 에이트킨 추정량의 최적성을 부등식 관점에서 증명한다.

### Ch 12: Statistical preliminaries (pp. 275-286)

**핵심**: 이후 장에서 사용할 통계학적 개념을 간결하게 복습한다. 누적분포함수, 결합밀도함수, 기댓값, 분산/공분산, 독립성, 표본추출, 일변량/다변량 정규분포, 추정(estimation)의 기초를 다룬다.

**키워드**: `정규분포`, `기댓값`, `분산`, `공분산`, `추정`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 12 (line 17780)

누적분포함수(CDF)를 일변량과 다변량 경우에 대해 정의하고, 연속확률변수의 밀도함수(PDF)를 CDF의 도함수로 도출한다. 기댓값을 적분으로 정의하고, 행렬 함수의 기댓값을 원소별 기댓값으로 확장한다. 기댓값의 선형성과 상수행렬과의 교환 성질 E(AGB) = A(EG)B를 제시한다. 분산과 공분산을 일변량과 다변량 경우 모두에 대해 정의하고, 분산행렬 V(x)가 대칭 양반정치임을 증명한다. 아핀변환 y = Ax+b에 대해 V(y) = AV(x)A'를 증명한다. 이차형식의 기댓값 공식 E(x'Ax) = tr AΩ + μ'Aμ를 유도한다. 두 확률변수의 독립성을 결합밀도의 인수분해로 정의하고, 독립성이 비상관보다 강한 조건임을 보인다. 표본추출과 표본통계량의 기초를 다룬다. 일변량/다변량 정규분포의 밀도함수와 적률생성함수를 제시하고, 정규분포의 이차형식에 대한 분산 공식 V(x'Ax) = 2σ⁴ tr A²을 증명한다. 이 장은 이후 선형모형과 최대우도 추정에 필요한 통계적 기초를 간결하게 제공한다.

### Ch 13: The linear regression model (pp. 287-322)

**핵심**: 일반 선형회귀모형 y = Xβ + ε을 다양한 조건하에서 분석한다. 아핀 최소분산 비편향 추정, 가우스-마르코프 정리, 최소제곱법, 에이트킨 정리(Aitken's theorem), 다중공선성, 추정가능 함수, 선형 제약조건(여러 경우), 특이 분산행렬, 일반화 최소제곱법을 포함한다.

**키워드**: `선형회귀`, `가우스-마르코프`, `최소제곱법`, `에이트킨 정리`, `다중공선성`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 13 (line 18483)

일반 선형회귀모형 y = Xβ + ε (E(ε)=0, E(εε')=σ²V)을 정의하고, 모수공간 B가 R^k 전체인 경우와 아핀 부분공간 {β: Rβ=r}인 경우를 구분한다. 아핀 최소분산 비편향 추정(affine minimum-trace unbiased estimation)을 행렬 미분법으로 구성하는 방법론을 제시한다. 라그랑주 함수 ψ(A) = (1/2)tr AA' - tr L'(AX-I)를 미분하여 β̂ = (X'X)^{-1}X'y를 유도하고, 가우스-마르코프 정리를 증명한다. 에이트킨 정리를 V가 양정치일 때 β̂ = (X'V^{-1}X)^{-1}X'V^{-1}y로 확장한다. 추정가능 함수(estimable function)의 완전한 특성화를 제시하고, Wβ가 추정가능할 필요충분조건을 유도한다. 다중공선성(X의 랭크가 k보다 작은 경우)에서의 추정 문제를 다루며, MP 역행렬을 이용한 해법을 제시한다. 선형 제약조건 Rβ=r 하의 제약 추정량을 라그랑주 승수법으로 유도한다. 특이 분산행렬 V의 경우를 포함한 일반화 최소제곱법을 다루고, 비정칙 V에서도 BLUE가 존재하는 조건을 제시한다. 이 장은 행렬 미분법의 통계학적 응용을 체계적으로 시연한다.

### Ch 14: Further topics in the linear model (pp. 323-348)

**핵심**: 선형모형의 추가 주제를 다룬다. σ²의 최적 이차 비편향 추정(best quadratic unbiased estimation), 이차 불변 추정, 다변량 정규 경우의 이차 추정, 최소제곱 추정량의 편향 한계, 교란 예측(prediction of disturbances), 최적 선형 비편향 예측량(BLUP), 사후 평균의 국소 민감도 분석을 포함한다.

**키워드**: `이차 추정`, `BLUP`, `편향 한계`, `민감도 분석`, `분산 추정`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 14 (line 20795)

σ²의 최적 이차 비편향 추정 문제를 정의하고, 정규 선형모형에서 최적 이차 양 비편향 추정량 σ̂² = y'(I-XX⁺)y/(n-r)을 라그랑주 승수법과 행렬 미분법으로 유도한다. C'C = (1/(n-r))(I-XX⁺)를 만족하는 멱등행렬의 최적 랭크가 n-r임을 보인다. 양 제약 없이도 동일한 추정량이 최적임을 증명하여, 양 제약이 구속력이 없음을 보인다. 이차 불변 추정(quadratic invariant estimation)을 정의하고 그 성질을 다룬다. 다변량 정규 경우의 이차 추정으로 확장한다. V(y) ≠ σ²I인 경우 최소제곱 추정량 σ̂²의 편향 한계를 행렬 부등식을 이용하여 유도하고, X에 의존하지 않는 보편적 한계를 제시한다. 교란(disturbance) 예측 문제를 다루며, 스칼라 분산행렬을 가지는 BLUS(best linear unbiased with scalar variance) 예측량과 고정 분산행렬을 가지는 BLUF 예측량을 유도한다. 사후 평균의 국소 민감도 분석(local sensitivity analysis)에 행렬 미분법을 적용하여, 사전분포의 초모수 변화에 대한 사후 모멘트의 변동을 분석한다.

### Ch 15: Maximum likelihood estimation (pp. 351-370)

**핵심**: 최대우도추정법(ML)의 이론과 행렬 미분법의 응용을 결합한다. 다변량 정규분포의 ML 추정, 대칭성의 명시적/암묵적 처리, 양정치성 처리, 정보행렬(information matrix), 다변량 선형회귀모형, 오차변수모형(errors-in-variables), 비선형 회귀모형을 다룬다.

**키워드**: `최대우도`, `정보행렬`, `다변량 정규`, `오차변수모형`, `비선형 회귀`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 15 (line 22462)

최대우도추정(ML)의 기본 틀을 정의하고, 우도함수, 대수우도함수, 스코어 벡터, 헤시안 행렬, 정보행렬의 관계를 정리한다. 점근 크래머-라오 부등식에 의해 정보행렬의 역이 ML 추정량의 점근 분산행렬이 됨을 설명한다. 다변량 정규분포 N_m(μ,Ω)의 ML 추정량 μ̂=ȳ, Ω̂=(1/n)Σ(y_i-ȳ)(y_i-ȳ)'를 네 가지 방법으로 증명한다. 첫 번째 증명은 Ω의 대칭성을 무시하고, 두 번째는 중복행렬(duplication matrix)을 이용한 암묵적 처리, 세 번째는 라그랑주 승수를 이용한 명시적 처리, 네 번째는 Ω=X'X로 양정치성을 부과하는 방법이다. 정보행렬을 대칭성을 고려하여 정확히 계산하고, 이를 위해 중복행렬 D_m과 그 MP 역행렬이 핵심적으로 사용됨을 보인다. 다변량 선형회귀모형에서의 ML 추정을 다루고, 오차변수모형(errors-in-variables model)에서 행렬 미분법의 위력을 시연한다. 비선형 회귀모형의 ML 추정에서 가우스-뉴턴 반복법의 유도를 다룬다.

### Ch 16: Simultaneous equations (pp. 371-393)

**핵심**: 연립방정식 모형에서의 식별(identification) 문제와 최대우도 추정을 다룬다. 선형/비선형 제약조건하의 식별, FIML(완전정보최대우도)의 정보행렬과 점근 분산행렬, LIML(제한정보최대우도)의 1차 조건, 정보행렬, 점근 분산행렬을 도출한다.

**키워드**: `연립방정식`, `식별`, `FIML`, `LIML`, `점근 분산`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 16 (line 23607)

연립방정식 모형 y_t'Γ₀ + x_t'B₀ = u_t'을 도입하고, 정규성 가정 하에서 Γ₀의 비특이성을 증명한다. 유도형(reduced form) Y = XΠ₀ + V₀를 도출하고, 구조형의 대수우도함수에 야코비안 항 (1/2)log|Γ'Γ|이 포함됨을 보인다. 식별(identification) 문제를 체계적으로 정의하고, 관측 동치(observationally equivalent)인 구조의 개념을 형식화한다. 유도형 모수 (Π₀,Ω₀)의 전역 식별을 X의 풀 랭크 조건 하에서 증명한다. B와 Γ에 대한 선형 제약조건 R₁vec B + R₂vec Γ = r 하의 전역 식별 조건을 유도하여, 특정 행렬이 풀 랭크 m²임을 조건으로 제시한다. B, Γ, Σ에 대한 비선형 제약조건 하의 국소 식별을 야코비 행렬의 랭크 조건으로 처리한다. FIML(완전정보 최대우도)의 스코어 벡터와 정보행렬을 행렬 미분법으로 유도하고, 점근 분산행렬을 구한다. LIML(제한정보 최대우도)의 1차 조건을 단일 방정식에 대해 유도하고, 정보행렬과 점근 분산행렬을 도출한다. FIML과 LIML의 점근 효율 비교에 행렬 부등식을 활용한다.

### Ch 17: Topics in psychometrics (pp. 395-423)

**핵심**: 심리측정학에서 발생하는 최적화 문제를 행렬 미분법으로 해결한다. 모집단/표본 주성분분석, 주성분의 최적성, 1모드/2모드/다모드 성분분석, 인자분석(factor analysis), 지그재그/뉴턴-랩슨 루틴, 카이저 배리맥스 회전(varimax), 정준상관(canonical correlations)을 다룬다.

**키워드**: `주성분분석`, `인자분석`, `배리맥스`, `정준상관`, `성분분석`

**상세**: → `Magnus J., Neudecker H. Matrix differential calculus...md` Ch 17 (line 24997)

모집단 주성분분석에서 분산행렬 Ω의 고유벡터 T에 의한 변환 v = T'x가 비상관 성분을 생성하고, 각 성분의 분산이 고유값 λ_i와 같음을 증명한다. 제i주성분 v_i가 v_1,...,v_{i-1}과 비상관인 정규화 선형결합 중 분산이 최대인 것임을 레일리 몫과 부등식 이론으로 증명한다. Ω의 최적 저랭크 근사 문제를 tr(Ω-V)²의 최소화로 정식화하고, 최적 V가 상위 r개 고유값/고유벡터로 구성됨을 행렬 미분법으로 증명한다. 표본 주성분분석에서 표본 분산행렬 S의 고유분해를 다룬다. 1모드 성분분석에서 자료행렬 X를 ZA'로 근사하는 문제를 A의 반직교성 제약 하에서 풀고, SVD와의 관계를 밝힌다. 2모드 및 다모드 성분분석으로 확장한다. 인자분석 모형 x = Ay + μ + ε의 ML 추정을 다루고, 지그재그 루틴과 뉴턴-랩슨 루틴을 행렬 미분으로 유도한다. 카이저 배리맥스 회전을 max Σ(1/p)Σa_{ij}⁴ - (1/p²)(Σa_{ij}²)²로 정식화하고 해법을 제시한다. 정준상관(canonical correlations)을 고유값 문제로 정식화하고, 분산행렬의 고유구조를 이용한 해를 구한다.
