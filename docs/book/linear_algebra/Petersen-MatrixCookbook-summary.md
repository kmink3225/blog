---
name: "The Matrix Cookbook"
type: book-summary
source_file: "Petersen-MatrixCookbook_azure_full.md"
authors: "Kaare Brandt Petersen, Michael Syskind Pedersen"
year: 2012
total_pages: 72
language: en
keywords: [matrix identities, matrix derivatives, matrix inverses, Gaussian, decompositions, special matrices, Kronecker product, statistics, probability]
---

# The Matrix Cookbook — Summary

> Kaare Brandt Petersen, Michael Syskind Pedersen (2012), 72 pages, 10 chapters + 부록
> 행렬 대수의 항등식, 미분, 역행렬, 분해 등을 빠르게 참조할 수 있도록 정리한 레퍼런스 모음집이다.

## Contents

1. Basics (pp. 6-7)
   - 1.1 Trace
   - 1.2 Determinant
   - 1.3 The Special Case 2x2
2. Derivatives (pp. 8-16)
   - 2.1 Derivatives of a Determinant
   - 2.2 Derivatives of an Inverse
   - 2.3 Derivatives of Eigenvalues
   - 2.4 Derivatives of Matrices, Vectors and Scalar Forms
   - 2.5 Derivatives of Traces
   - 2.6 Derivatives of vector norms
   - 2.7 Derivatives of matrix norms
   - 2.8 Derivatives of Structured Matrices
3. Inverses (pp. 17-23)
   - 3.1 Basic
   - 3.2 Exact Relations
   - 3.3 Implication on Inverses
   - 3.4 Approximations
   - 3.5 Generalized Inverse
   - 3.6 Pseudo Inverse
4. Complex Matrices (pp. 24-27)
   - 4.1 Complex Derivatives
   - 4.2 Higher order and non-linear derivatives
   - 4.3 Inverse of complex sum
5. Solutions and Decompositions (pp. 28-33)
   - 5.1 Solutions to linear equations
   - 5.2 Eigenvalues and Eigenvectors
   - 5.3 Singular Value Decomposition
   - 5.4 Triangular Decomposition
   - 5.5 LU decomposition
   - 5.6 LDM decomposition
   - 5.7 LDL decompositions
6. Statistics and Probability (pp. 34-36)
   - 6.1 Definition of Moments
   - 6.2 Expectation of Linear Combinations
   - 6.3 Weighted Scalar Variable
7. Multivariate Distributions (pp. 37-39)
   - 7.1 Cauchy
   - 7.2 Dirichlet
   - 7.3 Normal
   - 7.4 Normal-Inverse Gamma
   - 7.5 Gaussian
   - 7.6 Multinomial
   - 7.7 Student's t
   - 7.8 Wishart
   - 7.9 Wishart, Inverse
8. Gaussians (pp. 40-45)
   - 8.1 Basics
   - 8.2 Moments
   - 8.3 Miscellaneous
   - 8.4 Mixture of Gaussians
9. Special Matrices (pp. 46-57)
   - 9.1 Block matrices
   - 9.2 Discrete Fourier Transform Matrix
   - 9.3 Hermitian Matrices and skew-Hermitian
   - 9.4 Idempotent Matrices
   - 9.5 Orthogonal matrices
   - 9.6 Positive Definite and Semi-definite Matrices
   - 9.7 Singleentry Matrix
   - 9.8 Symmetric, Skew-symmetric/Antisymmetric
   - 9.9 Toeplitz Matrices
   - 9.10 Transition matrices
   - 9.11 Units, Permutation and Shift
   - 9.12 Vandermonde Matrices
10. Functions and Operators (pp. 58-63)
    - 10.1 Functions and Series
    - 10.2 Kronecker and Vec Operator
    - 10.3 Vector Norms
    - 10.4 Matrix Norms
    - 10.5 Rank
    - 10.6 Integral Involving Dirac Delta Functions
    - 10.7 Miscellaneous
- Appendix A: One-dimensional Results (pp. 64-65)
- Appendix B: Proofs and Details (pp. 66-72)

---

## Chapter Summaries

### Ch 1: Basics (pp. 6-7)

**핵심**: 행렬 대수의 가장 기본적인 항등식을 나열한다. 역행렬의 곱 (AB)^{-1} = B^{-1}A^{-1}, 전치/에르미트 전치의 성질, 대각합(trace)의 성질(순환성, 선형성), 행렬식(determinant)의 기본 성질, 2x2 행렬의 특수 경우(역행렬, 행렬식, 고유값)를 정리한다.

**키워드**: `기본 항등식`, `trace`, `행렬식`, `2x2 행렬`

**상세**: → `matrixcookbook.md` Ch 1 (line 507)

역행렬의 곱 (AB)^{-1} = B^{-1}A^{-1}과 다중곱의 역행렬, 전치의 역행렬 (A^T)^{-1} = (A^{-1})^T를 나열한다. 에르미트 전치(conjugate transpose)에 대한 유사한 성질을 정리한다. 대각합(trace)의 핵심 성질로 tr(A) = Σλ_i, tr(AB) = tr(BA) 순환성, tr(A+B) = tr(A)+tr(B) 선형성, a^T a = tr(aa^T)를 제시한다. 행렬식의 기본 성질로 det(A) = Πλ_i, det(cA) = c^n det(A), det(A^T) = det(A), det(AB) = det(A)det(B), det(A^{-1}) = 1/det(A), det(I+uv^T) = 1+u^T v를 나열한다. n=2,3,4에 대한 det(I+A) 공식과 소규모 ε에 대한 det(I+εA) 근사를 제시한다. 2x2 행렬의 특수 경우로 행렬식, 대각합, 고유값(λ² - λ·tr(A) + det(A) = 0), 고유벡터, 역행렬의 명시적 공식을 정리한다.

### Ch 2: Derivatives (pp. 8-16)

**핵심**: 행렬 X에 대한 다양한 표현식의 미분을 집대성한다. 행렬식, 역행렬, 고유값의 미분, 행렬/벡터/스칼라 형식의 미분, trace의 미분(가장 방대한 공식 모음), 벡터/행렬 노름의 미분을 포함한다. X의 원소가 독립(비구조적)임을 기본 가정으로 하며, 구조화된 행렬(대칭 등)의 미분은 별도 절에서 다룬다.

**키워드**: `행렬 미분`, `행렬식 미분`, `역행렬 미분`, `trace 미분`, `구조화 행렬`

**상세**: → `matrixcookbook.md` Ch 2 (line 691)

X의 원소가 독립(비구조적)임을 기본 가정으로 하여 ∂X_{kl}/∂X_{ij} = δ_{ik}δ_{lj}를 출발점으로 삼는다. 미분의 일반 규칙(상수, 스칼라 곱, 합, 곱, 아다마르 곱, 크로네커 곱, 역행렬, 행렬식, 전치)을 나열한다. 행렬식의 미분을 일반형, 선형형, 제곱형, 비선형형으로 세분하여 공식을 집대성한다. 역행렬의 미분 ∂Y^{-1}/∂x = -Y^{-1}(∂Y/∂x)Y^{-1}과 이를 이용한 다수의 파생 공식을 정리한다. 고유값 합과 곱의 미분을 trace와 det으로 환원한다. 행렬/벡터/스칼라 형식의 미분에서 ∂(Ax+b)/∂x = A, ∂(x^T Ax)/∂x = (A+A^T)x 등 핵심 공식을 나열한다. trace의 미분 공식이 가장 방대하며, ∂tr(AX)/∂X = A^T부터 ∂tr(X^n)/∂X = n(X^{n-1})^T까지 수십 개의 공식을 포괄한다. 벡터 노름(||x||_p)과 행렬 노름(||X||_F 등)의 미분을 다룬다. 대칭/토플리츠 등 구조화된 행렬에서의 미분은 변환 규칙을 별도로 제시한다.

### Ch 3: Inverses (pp. 17-23)

**핵심**: 역행렬에 관한 다양한 결과를 정리한다. 역행렬의 정의, 여인수/수반행렬을 통한 역행렬, 정확한 관계식(Woodbury 항등식, Sherman-Morrison 공식 등), 역행렬에 대한 함의, 역행렬의 근사(Neumann 급수), 일반화 역행렬, 의사역행렬(pseudo inverse)을 포함한다.

**키워드**: `역행렬`, `Woodbury`, `Sherman-Morrison`, `의사역행렬`, `Neumann 급수`

**상세**: → `matrixcookbook.md` Ch 3 (line 1418)

역행렬의 정의 AA^{-1} = A^{-1}A = I에서 출발하여, 여인수(cofactor)와 수반행렬(adjoint)을 통한 역행렬 구성 A^{-1} = adj(A)/det(A)를 제시한다. 조건수(condition number)를 최대/최소 특이값의 비로 정의하고, 행렬이 거의 특이일 때 조건수가 큰 값을 가짐을 설명한다. Woodbury 항등식 (A+CBC^T)^{-1} = A^{-1} - A^{-1}C(B^{-1}+C^T A^{-1}C)^{-1}C^T A^{-1}을 제시하고, Kailath 변형, Sherman-Morrison 공식 (A+bc^T)^{-1}, Searle 항등식 집합 등 다양한 변형을 나열한다. 랭크-1 갱신에 의한 역행렬 갱신 공식을 제시한다. 역행렬에 대한 함의(implication)로 (I+AB)^{-1} = I - A(I+BA)^{-1}B 등의 관계식을 정리한다. Neumann 급수 (I-A)^{-1} = Σ A^k에 의한 역행렬의 급수 근사와 1차/2차 근사를 제시한다. 일반화 역행렬(generalized inverse)의 정의 AXA=A를 제시하고, 의사역행렬(pseudo inverse, Moore-Penrose)의 4가지 조건과 풀 랭크 경우의 명시적 공식 A^+ = (A^T A)^{-1}A^T를 정리한다.

### Ch 4: Complex Matrices (pp. 24-27)

**핵심**: 복소 행렬에 대한 미분을 다룬다. 코시-리만 방정식을 만족하는 해석함수의 미분, 복소 켤레를 포함하는 경우의 일반화된 미분 정의, 고차/비선형 미분, 복소합의 역행렬을 정리한다.

**키워드**: `복소 미분`, `코시-리만`, `해석함수`, `복소 역행렬`

**상세**: → `matrixcookbook.md` Ch 4 (line 1915)

복소 스칼라 곱을 실부와 허부로 분리하여 행렬 형태로 표현한다. 코시-리만 방정식을 만족하는 해석함수의 미분을 정의하고, 복소 켤레를 포함하는 비해석함수에 대해 일반화된 복소 미분(generalized complex derivative)과 켤레 복소 미분(conjugate complex derivative)을 정의한다. 해석함수에서는 일반화 복소 미분이 통상 미분과 일치하고 켤레 복소 미분은 0이 됨을 보인다. 복소 그래디언트 벡터와 행렬을 2·df/dZ*로 정의하여 경사하강법에 활용할 수 있도록 한다. 비해석함수에 대한 연쇄법칙의 확장을 제시하고, trace와 행렬식의 복소 미분을 실부/허부 분리 방법으로 계산하는 예를 보인다. det(X^H AX)의 일반화 복소 미분과 켤레 복소 미분을 각각 구한다. 고차/비선형 미분으로 (Ax)^H(Ax)/((Bx)^H(Bx))의 미분을 다룬다. 복소합의 역행렬에 대한 결과를 정리한다.

### Ch 5: Solutions and Decompositions (pp. 28-33)

**핵심**: 연립선형방정식의 풀이와 행렬 분해법을 정리한다. 단순선형회귀의 최소제곱 해, 선형시스템의 존재/유일성 조건, 고유값/고유벡터의 성질, 특이값 분해(SVD), 삼각분해, LU/LDM/LDL 분해를 포함한다.

**키워드**: `선형방정식`, `고유값`, `SVD`, `LU분해`, `최소제곱`

**상세**: → `matrixcookbook.md` Ch 5 (line 2148)

단순선형회귀의 최소제곱 해를 정규방정식의 행렬 형태로 제시한다. 선형시스템 Ax=b의 해의 존재/유일성을 증대행렬(augmented matrix)의 랭크 조건으로 분류한다. 정방가역, 정방랭크결핍, 과결정(tall), 미결정(broad) 시스템 각각에 대해 해 또는 최소제곱 해 x = A^+b를 제시한다. 크래머 공칙(Cramer's rule)을 정리한다. 리아푸노프 방정식 AX+XB=C의 해를 크로네커 곱과 vec으로 vec(X) = (I⊗A + B^T⊗I)^{-1}vec(C)로 표현한다. 고유값/고유벡터의 정의 Av_i = λ_i v_i와 고유분해 AV=VD를 제시하고, 결핍행렬의 조단 정준형(Jordan canonical form)을 다룬다. 특이값 분해 A=UDV^T의 정의와 성질을 정리한다. 삼각분해, LU/LDM/LDL 분해의 구성법과 성질을 나열한다. 촐레스키 분해는 양정치행렬에 대한 LDL 분해의 특수 경우로 언급한다.

### Ch 6: Statistics and Probability (pp. 34-36)

**핵심**: 확률과 통계의 행렬 표현을 요약한다. 평균, 공분산 행렬, 3차/4차 적률의 정의, 선형결합의 기댓값(평균/공분산/교차공분산 변환 규칙), 가중 스칼라 변수의 기댓값을 정리한다.

**키워드**: `평균`, `공분산`, `적률`, `선형결합 기댓값`

**상세**: → `matrixcookbook.md` Ch 6 (line 2566)

확률벡터 x의 평균 벡터 m, 공분산 행렬 M = E[(x-m)(x-m)^T]를 정의한다. 3차 중심적률(공왜도 행렬) M_3과 4차 중심적률(공첨도 행렬) M_4를 크로네커 곱을 이용하여 행렬 형태로 표현한다. 선형결합의 기댓값 규칙 E[AXB+C] = AE[X]B+C, Var[Ax] = AVar[x]A^T, Cov[Ax,By] = ACov[x,y]B^T를 정리한다. 이차형식의 기댓값 E[x^T Ax] = tr(AΣ) + c^T Ac와 분산 공식을 독립 좌표 가정 하에서 제시한다. 확률벡터 x의 선형/이차/3차 형식에 대한 기댓값 공식을 체계적으로 나열하며, E[xx^T] = M+mm^T, E[xa^T x] = (M+mm^T)a 등의 결과를 포함한다. 가중 스칼라 변수 y = w^T x의 1차~4차 중심적률을 크로네커 곱으로 표현하여 <(y-<y>)^k> = w^T M_k (w⊗...⊗w)임을 보인다.

### Ch 7: Multivariate Distributions (pp. 37-39)

**핵심**: 주요 다변량 분포의 밀도함수를 행렬 표기로 나열한다. 코시, 디리클레, 정규, 정규-역감마, 가우시안, 다항, 스튜던트 t, 위샤트, 역위샤트 분포의 밀도/모수를 정리한다.

**키워드**: `다변량 분포`, `위샤트`, `디리클레`, `스튜던트 t`, `정규`

**상세**: → `matrixcookbook.md` Ch 7 (line 2752)

코시 분포의 밀도함수를 위치 μ와 양정치 척도행렬 Σ로 매개변수화하여 p(t|μ,Σ) ∝ det(Σ)^{-1/2}[1+(t-μ)^T Σ^{-1}(t-μ)]^{-(1+P)/2}로 제시하고, 이것이 자유도 1인 스튜던트 t 분포의 특수 경우임을 언급한다. 디리클레 분포의 밀도를 감마함수를 이용하여 표현한다. 정규분포는 8장(가우시안)으로 참조를 안내한다. 다항분포의 질량함수를 다항계수와 확률 벡터로 정리한다. 스튜던트 t 분포를 벡터와 행렬 형태 모두로 제시하고, 평균 E(t)=μ(ν>1), 분산 cov(t)=(ν/(ν-2))Σ(ν>2), 최빈값 mode(t)=μ를 정리한다. 행렬 버전의 스튜던트 t 분포 p(T|M,Ω,Σ,ν)를 도출한다. 위샤트 분포 p(M|Σ,m)의 밀도와 평균 E(M)=mΣ를 제시하고, 역위샤트 분포의 밀도와 평균 E(M)=Σ/(m-P-1)을 정리한다.

### Ch 8: Gaussians (pp. 40-45)

**핵심**: 가우시안(정규) 분포에 관한 심층적 공식을 모은다. 밀도함수와 정규화, 조건부/주변부 분포, 적률(평균, 공분산, 4차 적률), 엔트로피, KL 발산, 가우시안 혼합 모형의 기본 공식을 포함한다.

**키워드**: `가우시안`, `조건부 분포`, `KL 발산`, `엔트로피`, `혼합 모형`

**상세**: → `matrixcookbook.md` Ch 8 (line 2898)

가우시안(정규)분포의 밀도함수 p(x) = (det(2πΣ))^{-1/2} exp[-(1/2)(x-m)^T Σ^{-1}(x-m)]와 정규화 적분 공식을 여러 변형으로 제시한다. 주변분포와 조건부분포를 블록 분할된 공분산행렬의 Schur 보원으로 표현하고, 조건부 평균 μ̂_a = μ_a + Σ_c Σ_b^{-1}(x_b - μ_b)와 조건부 분산 Σ̂_a = Σ_a - Σ_c Σ_b^{-1} Σ_c^T를 유도한다. 선형결합 Ax+By+c의 정규성을 보인다. 1차/2차 적률과 이차형식의 기댓값을 가우시안 특수 공식으로 정리한다. 4차 적률 E[x_i x_j x_k x_l]을 공분산의 조합으로 표현한다. 엔트로피 H = (1/2)ln det(2πeΣ)와 KL 발산 KL(p₁||p₂) = (1/2)[tr(Σ₂^{-1}Σ₁) + (μ₂-μ₁)^T Σ₂^{-1}(μ₂-μ₁) - ln(det Σ₁/det Σ₂) - d]를 제시한다. 두 가우시안의 곱을 다시 가우시안으로 정리하고 정규화 상수를 명시한다. 가우시안 혼합 모형(mixture of Gaussians)의 기본 공식과 EM 알고리즘에 활용되는 사후확률 공식을 포함한다.

### Ch 9: Special Matrices (pp. 46-57)

**핵심**: 특수한 구조를 가진 행렬들의 성질을 정리한다. 블록행렬(곱, 행렬식, 역행렬, Schur 보원), DFT 행렬, 에르미트/반에르미트 행렬, 멱등행렬, 직교행렬, 양정치/반양정치 행렬, 단일원소행렬, 대칭/반대칭 행렬, 토플리츠 행렬, 전이행렬, 치환행렬, 반데르몬드 행렬을 포함한다.

**키워드**: `블록행렬`, `양정치`, `에르미트`, `토플리츠`, `직교행렬`

**상세**: → `matrixcookbook.md` Ch 9 (line 3267)

블록행렬의 곱, 행렬식, 역행렬을 Schur 보원(Schur complement)을 중심으로 체계적으로 정리한다. 이산 푸리에 변환(DFT) 행렬의 정의와 성질(유니터리, 고유값, 역변환)을 나열한다. 에르미트 행렬(A = A^H)과 반에르미트 행렬(A = -A^H)의 성질(실수 고유값, 유니터리 대각화)을 정리한다. 멱등행렬(A² = A)의 고유값(0 또는 1), rank = trace 관계, 사영 성질을 다룬다. 직교행렬(A^T A = I)의 고유값(절대값 1), 행렬식(±1) 등을 정리한다. 양정치/양반정치 행렬의 여러 동치 조건(고유값 양수, 촐레스키 분해 존재, x^T Ax > 0 등)을 나열하고, 양정치행렬의 합/곱/역행렬의 양정치성 보존을 다룬다. 단일원소행렬(single-entry matrix), 대칭/반대칭 행렬, 토플리츠 행렬(대각선상 동일 원소), 전이행렬(stochastic matrix), 치환/시프트 행렬, 반데르몬드 행렬의 성질과 행렬식 공식을 포함한다.

### Ch 10: Functions and Operators (pp. 58-63)

**핵심**: 행렬 함수와 연산자를 정리한다. 유한/무한 급수(행렬 지수함수, 로그 등), 스칼라 함수의 테일러 전개, 크로네커 곱과 vec 연산자의 성질, 벡터/행렬 노름, 랭크의 성질, 디랙 델타 함수를 포함하는 적분, 기타 유용한 항등식을 모은다.

**키워드**: `행렬 함수`, `크로네커 곱`, `vec 연산자`, `노름`, `테일러 전개`

**상세**: → `matrixcookbook.md` Ch 10 (line 4114)

행렬 함수를 유한 급수(다항식, 네만 급수)와 무한 급수(행렬 지수함수 e^A = Σ A^k/k!, 행렬 로그, 삼각함수)로 정의하고 수렴 조건을 제시한다. 스칼라 함수의 테일러 전개를 행렬 변수로 확장하고, f(A+εB)의 1차/2차 근사를 유도한다. 크로네커 곱의 핵심 성질((A⊗B)(C⊗D) = AC⊗BD, (A⊗B)^{-1} = A^{-1}⊗B^{-1}, eigenvalues λ_i μ_j)을 집대성한다. vec 연산자와 크로네커 곱의 관계 vec(ABC) = (C^T⊗A)vec(B)를 제시하고, 리아푸노프/실베스터 방정식 풀이에 활용한다. 벡터 노름(1-노름, 2-노름, p-노름, ∞-노름)과 행렬 노름(프로베니우스 노름, 유도 노름, 핵 노름)의 정의와 성질을 정리한다. 랭크의 기본 성질(r(AB) ≤ min(r(A),r(B)), r(A+B) ≤ r(A)+r(B) 등)을 나열한다. 디랙 델타 함수를 포함하는 적분과 그 행렬 유사체를 다루고, 기타 유용한 항등식을 모은다.
