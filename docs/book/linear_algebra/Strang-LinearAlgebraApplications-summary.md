---
name: "Linear Algebra and Its Applications, Fourth Edition"
type: book-summary
sources:
  - file: "Strang-LinearAlgebraApplications_azure_full.md"
    tool: Document Intelligence
authors: "Gilbert Strang"
year: 2006
total_pages: 486
language: en
keywords: [linear algebra, Gaussian elimination, vector spaces, orthogonality, determinants, eigenvalues, positive definite, SVD, linear programming, game theory]
---

# Linear Algebra and Its Applications, Fourth Edition — Summary

> Gilbert Strang (2006), 486 pages, 8 chapters + 부록
> 선형대수의 이론과 응용을 균형 있게 다루며, 양정치행렬, 선형계획법, 게임이론까지 포괄하는 응용 중심 교재이다.

## Contents

1. Matrices and Gaussian Elimination (pp. 1-76)
   - 1.1 Introduction
   - 1.2 The Geometry of Linear Equations
   - 1.3 An Example of Gaussian Elimination
   - 1.4 Matrix Notation and Matrix Multiplication
   - 1.5 Triangular Factors and Row Exchanges
   - 1.6 Inverses and Transposes
   - 1.7 Special Matrices and Applications
2. Vector Spaces (pp. 77-158)
   - 2.1 Vector Spaces and Subspaces
   - 2.2 Solving Ax = 0 and Ax = b
   - 2.3 Linear Independence, Basis, and Dimension
   - 2.4 The Four Fundamental Subspaces
   - 2.5 Graphs and Networks
   - 2.6 Linear Transformations
3. Orthogonality (pp. 159-224)
   - 3.1 Orthogonal Vectors and Subspaces
   - 3.2 Cosines and Projections onto Lines
   - 3.3 Projections and Least Squares
   - 3.4 Orthogonal Bases and Gram-Schmidt
   - 3.5 The Fast Fourier Transform
4. Determinants (pp. 225-259)
   - 4.1 Introduction
   - 4.2 Properties of the Determinant
   - 4.3 Formulas for the Determinant
   - 4.4 Applications of Determinants
5. Eigenvalues and Eigenvectors (pp. 260-344)
   - 5.1 Introduction
   - 5.2 Diagonalization of a Matrix
   - 5.3 Difference Equations and Powers A^k
   - 5.4 Differential Equations and e^{At}
   - 5.5 Complex Matrices
   - 5.6 Similarity Transformations
6. Positive Definite Matrices (pp. 345-389)
   - 6.1 Minima, Maxima, and Saddle Points
   - 6.2 Tests for Positive Definiteness
   - 6.3 Singular Value Decomposition
   - 6.4 Minimum Principles
   - 6.5 The Finite Element Method
7. Computations with Matrices (pp. 390-416)
   - 7.1 Introduction
   - 7.2 Matrix Norm and Condition Number
   - 7.3 Computation of Eigenvalues
   - 7.4 Iterative Methods for Ax = b
8. Linear Programming and Game Theory (pp. 417-458)
   - 8.1 Linear Inequalities
   - 8.2 The Simplex Method
   - 8.3 The Dual Problem
   - 8.4 Network Models
   - 8.5 Game Theory
- Appendix A: Intersection, Sum, and Product of Spaces (pp. 459-465)
- Appendix B: The Jordan Form (pp. 466-472)
- Appendix C: Matrix Factorizations (pp. 473-474)
- Appendix D: Glossary (pp. 475-483)
- Appendix E: MATLAB Teaching Codes (pp. 484-485)
- Appendix F: Linear Algebra in a Nutshell (pp. 486)

---

## Chapter Summaries

### Ch 1: Matrices and Gaussian Elimination (pp. 1-76)

**핵심**: 연립방정식 풀이라는 선형대수의 중심 문제를 소거법과 행렬식 두 가지 방법으로 접근한다. 소거법을 행렬 표기로 발전시키고, 삼각인수분해(LU), 행 교환, 역행렬과 전치행렬을 다룬다. 연립방정식의 기하학적 해석(행 관점과 열 관점)을 통해 직관을 형성하며, 대칭/밴드/양정치 등 특수행렬을 소개한다.

**키워드**: `가우스 소거법`, `LU분해`, `역행렬`, `전치행렬`, `특수행렬`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 1 (line 644)

연립방정식의 기하학적 해석을 행 관점(초평면의 교차)과 열 관점(열벡터의 선형결합)으로 제시한다. 가우스 소거법을 2x2에서 nxn으로 확장하고, 피벗이 0이 되는 경우의 행 교환을 다룬다. 소거법을 행렬 표기로 발전시켜 EA=U를 유도하고, 소거행렬 E_{ij}의 구조를 분석한다. 삼각인수분해 A=LU를 유도하고, L이 소거 승수를 원소로 가지는 하삼각행렬임을 보인다. 행 교환이 필요한 경우 PA=LU를 제시하고, 치환행렬 P의 성질(P^{-1}=P^T)을 증명한다. 역행렬의 존재 조건을 소거법의 피벗과 연결하고, (AB)^{-1}=B^{-1}A^{-1}을 증명한다. 전치행렬의 성질과 대칭행렬 A=A^T를 도입하며, 대칭/밴드/양정치 등 특수행렬의 구조적 이점을 소개한다. LDL^T 분해에 의한 대칭행렬의 효율적 처리를 설명하고, 양정치행렬에서는 L=촐레스키 인수가 됨을 언급한다.

### Ch 2: Vector Spaces (pp. 77-158)

**핵심**: 소거법 너머의 깊은 이해를 위해 벡터 공간과 부분공간 개념을 도입한다. Ax = 0과 Ax = b의 해를 체계적으로 분석하고, 선형독립/기저/차원을 정의한다. 네 가지 기본 부분공간(열공간, 영공간, 행공간, 좌영공간)을 통해 행렬의 본질을 파악한다. 그래프/네트워크와 선형변환을 응용으로 다룬다.

**키워드**: `벡터공간`, `부분공간`, `기저`, `차원`, `네 가지 기본 부분공간`, `선형변환`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 2 (line 5315)

벡터 공간과 부분공간의 공리적 정의를 제시하고, 행렬의 열공간 C(A)과 영공간 N(A)을 핵심 예로 소개한다. Ax=0의 해를 소거법으로 구하고, 자유변수에 의한 특수해 구성법을 설명한다. Ax=b의 해가 존재하려면 b∈C(A)이어야 함을 보이고, 완전해를 특수해+영공간의 벡터로 표현한다. 선형독립, 기저, 차원의 개념을 정의하고, 랭크=피벗 수=dim C(A)=dim C(A^T)임을 증명한다. 네 가지 기본 부분공간(C(A), N(A), C(A^T), N(A^T))의 차원 관계를 r+(n-r)=n, r+(m-r)=m으로 정리한다. 그래프와 네트워크를 접속행렬(incidence matrix)로 표현하고, 영공간이 전위(potential), 좌영공간이 루프를 나타냄을 보인다. 키르히호프의 전류법칙(KCL)과 전압법칙(KVL)을 선형대수로 재해석한다. 선형변환의 정의와 핵(kernel)/치역(range)의 개념을 소개하고, 기저 선택에 의한 행렬 표현을 다룬다.

### Ch 3: Orthogonality (pp. 159-224)

**핵심**: 직교 기저(orthogonal basis)가 선형대수 계산을 단순화하는 핵심임을 강조한다. 벡터의 길이, 직교성 판정(x^T y = 0), Gram-Schmidt 과정을 통한 직교벡터 생성을 다룬다. 기본 부분공간이 쌍으로 직교함을 보이고, 사영과 최소제곱법을 정리한다. FFT(고속 푸리에 변환)를 직교성의 응용으로 소개한다.

**키워드**: `직교`, `사영`, `최소제곱법`, `Gram-Schmidt`, `FFT`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 3 (line 10275)

직교 기저가 계산을 단순화하는 핵심임을 강조하고, 직교벡터의 내적이 0임을 정의한다. 네 가지 기본 부분공간이 쌍으로 직교함을 증명하고, R^n = C(A^T) ⊕ N(A)임을 보인다. 직선 위의 사영 공식 p = (a^T b/a^T a)a에서 출발하여, 열공간 위의 사영행렬 P = A(A^T A)^{-1}A^T를 유도한다. P가 대칭이고 P²=P(멱등)임을 증명한다. 최소제곱법의 정규방정식 A^T Ax̂ = A^T b를 사영의 관점에서 유도하고, 직선/포물선 피팅에 응용한다. Gram-Schmidt 과정을 설명하여 독립 벡터로부터 직교정규 기저를 구성하는 방법을 시연한다. QR 분해 A=QR을 유도하고, 최소제곱에서 A^T A = R^T R로 단순화됨을 보인다. 고속 푸리에 변환(FFT)을 직교성의 응용으로 소개하고, 푸리에 행렬의 재귀적 구조에 의해 연산량이 O(n log n)으로 줄어드는 원리를 설명한다.

### Ch 4: Determinants (pp. 225-259)

**핵심**: 행렬식이 선형대수의 중심에서 벗어났지만 여전히 유용한 도구임을 인정하며 다룬다. A^{-1}과 A^{-1}b에 대한 명시적 공식을 제공하고, 가역성 판별, n차원 부피 계산, 고유값 계산(det(A - λI) = 0)에 활용한다. 행렬식의 성질, 여인수 전개, 크래머 공칙을 설명한다.

**키워드**: `행렬식`, `여인수`, `크래머 공칙`, `가역성`, `부피`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 4 (line 14288)

행렬식이 선형대수의 중심에서 벗어났지만 여전히 유용한 도구임을 인정하며 다룬다. 행렬식의 세 가지 핵심 성질(det I=1, 행 교환시 부호 변경, 행에 대한 선형성)에서 출발하여, 특이행렬 det=0, 삼각행렬 det=피벗의 곱 등 모든 성질을 유도한다. det(AB)=det(A)det(B)를 증명한다. 행렬식의 공식을 순열(permutation)과 여인수(cofactor)를 통해 두 가지 방식으로 전개한다. 여인수 전개를 임의의 행(열)을 따라 수행하는 방법을 제시한다. 행렬식의 응용으로 크래머 공칙(Cramer's rule) x_i = det(B_i)/det(A)를 유도하고, 역행렬 공식 A^{-1} = C^T/det(A)를 제시한다. 행렬식과 부피의 관계를 다루어, n개 벡터가 만드는 평행육면체의 부피가 |det A|임을 보인다. 행렬식을 고유값 계산의 도구(det(A-λI)=0)로도 활용한다.

### Ch 5: Eigenvalues and Eigenvectors (pp. 260-344)

**핵심**: 선형대수의 "후반부"를 여는 장으로, Ax = λx 문제를 본격적으로 다룬다. 고유값을 미분방정식(du/dt = Au)과 차분방정식(u_{k+1} = Au_k)에 적용하여 동적 시스템의 성장/감쇠/진동을 분석한다. 대각화, 행렬 거듭제곱, 복소행렬, 유사변환(similarity transformation)을 포괄한다.

**키워드**: `고유값`, `고유벡터`, `대각화`, `미분방정식`, `차분방정식`, `유사변환`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 5 (line 16248)

Ax=λx 문제를 도입하고, 특성방정식 det(A-λI)=0으로 고유값을 구하는 방법을 제시한다. 대각화 S^{-1}AS=Λ의 조건(n개의 독립 고유벡터)을 설명하고, 대각화 불가능한 결핍행렬(defective matrix)의 예를 든다. 차분방정식 u_{k+1}=Au_k의 해를 u_k=SΛ^k S^{-1}u_0으로 구하고, 피보나치 수열을 행렬 거듭제곱으로 분석한다. 미분방정식 du/dt=Au의 해 u(t)=e^{At}u_0를 고유값 분해로 구하고, 안정성/불안정성을 Re(λ)의 부호로 판별한다. 행렬 지수함수 e^{At}=Se^{Λt}S^{-1}을 유도한다. 복소행렬과 복소 고유값을 다루며, 에르미트 행렬의 실수 고유값과 유니터리 행렬의 성질을 증명한다. 유사변환(similarity transformation) B=M^{-1}AM에서 A와 B의 고유값이 같음을 보이고, Jordan 형을 소개한다. 슈어 정리(모든 행렬은 유니터리 유사변환으로 상삼각화 가능)를 제시한다.

### Ch 6: Positive Definite Matrices (pp. 345-389)

**핵심**: 고유값의 부호가 중요한 양정치행렬을 독립된 장으로 심도 있게 다룬다. 극소/극대/안장점 판별에서 출발하여, 피벗/행렬식/고유값을 통한 양정치성 판별법을 제시한다. 특이값 분해(SVD), 최소원리(minimum principles), 유한요소법(FEM)을 양정치행렬의 응용으로 다룬다.

**키워드**: `양정치행렬`, `SVD`, `최소원리`, `유한요소법`, `이차형식`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 6 (line 21438)

이차형식 f(x)=x^T Ax의 극소/극대/안장점 판별에서 양정치행렬의 중요성을 동기화한다. 양정치행렬의 5가지 판별법(양의 고유값, 양의 피벗, 양의 선행 소행렬식, x^T Ax>0, A=R^T R)을 제시하고 동치성을 증명한다. 타원(x^T Ax=1)의 축이 고유벡터, 축 길이가 1/√λ_i임을 보인다. 특이값 분해 A=UΣV^T를 임의의 m×n 행렬에 대해 유도하고, 특이값이 √(A^T A의 고유값)임을 보인다. SVD의 기하학적 해석(직교변환-스케일링-직교변환)을 제시한다. 최소원리(minimum principles)를 다루어, λ_max = max(x^T Ax/x^T x)와 min-max 원리를 증명한다. 레일리 몫의 안장점 성질을 다룬다. 유한요소법(FEM)을 선형대수의 관점에서 소개하고, 요소 강성행렬의 조립(assembly)과 전체 강성행렬 K=A^T CA의 구조를 설명한다. K가 양반정치(고정 경계조건 시 양정치)임을 물리적 에너지 관점에서 해석한다.

### Ch 7: Computations with Matrices (pp. 390-416)

**핵심**: 수치 계산의 실제 문제를 다루며, 이론과 실용의 간극을 메운다. 행렬 노름과 조건수(condition number)를 통해 수치적 안정성을 정량화하고, 고유값 계산 알고리즘과 Ax = b에 대한 반복법(iterative methods)을 설명한다. 희소행렬 처리의 효율성을 강조한다.

**키워드**: `행렬 노름`, `조건수`, `고유값 계산`, `반복법`, `수치 안정성`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 7 (line 23945)

수치 선형대수에서 속도와 정확성의 균형 문제를 제기한다. 행렬 노름을 정의하고, 유도 노름(induced norm) ||A|| = max(||Ax||/||x||)와 프로베니우스 노름의 관계를 설명한다. 조건수 c(A) = ||A|| ||A^{-1}||을 정의하고, ||δx||/||x|| ≤ c(A) ||δb||/||b||로 해의 민감도를 정량화한다. 조건수가 클수록 행렬이 거의 특이함을 수치 예로 시연한다. 고유값 계산 알고리즘으로 QR 반복법(QR iteration)을 소개하고, A_k → QR → RQ = A_{k+1} 과정이 대각행렬로 수렴함을 설명한다. 시프트(shift)를 이용한 수렴 가속을 다룬다. Ax=b에 대한 반복법으로 야코비법(Jacobi), 가우스-자이델법(Gauss-Seidel), SOR(successive over-relaxation)을 소개하고, 수렴 조건을 반복행렬의 스펙트럼 반경 ρ(M)<1로 제시한다. 전처리기(preconditioner)의 역할과 불완전 분해를 다룬다. 대규모 희소 시스템에서 반복법이 직접법보다 효율적일 수 있음을 강조한다.

### Ch 8: Linear Programming and Game Theory (pp. 417-458)

**핵심**: 선형 부등식과 최적화를 선형대수의 관점에서 다룬다. 심플렉스법(simplex method)과 내부점법(interior point method)의 경쟁을 소개하고, 쌍대문제(dual problem)의 중요성을 강조한다. 네트워크 모형과 게임이론(행렬 게임)을 추가 응용으로 제시한다.

**키워드**: `선형계획`, `심플렉스법`, `쌍대문제`, `네트워크`, `게임이론`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 8 (line 25388)

선형 부등식 Ax ≤ b로 정의되는 가능해 영역(feasible region)이 볼록 다면체(convex polyhedron)임을 보인다. 선형계획 문제 min c^T x (Ax≤b, x≥0)에서 최적해가 코너점(extreme point)에서 달성됨을 증명한다. 심플렉스법(simplex method)의 원리를 코너점 간의 이동으로 설명하고, 피벗 연산을 통한 구현을 다룬다. 내부점법(interior point method)과의 경쟁을 언급한다. 쌍대문제(dual problem) max b^T y (A^T y≥c, y≥0)를 도입하고, 약쌍대정리(약한 쌍대 부등식 b^T y ≤ c^T x)와 강쌍대정리(최적값 일치)를 제시한다. 상보 여유조건(complementary slackness)을 설명한다. 네트워크 모형에서 최소비용 흐름 문제를 선형계획으로 정식화한다. 게임이론(행렬 게임)을 도입하고, 최소극대(minimax) 정리를 폰 노이만의 결과로 제시한다. 혼합전략(mixed strategy)의 최적해를 선형계획의 쌍대 구조와 연결하여, 게임의 값이 원문제와 쌍대문제의 공통 최적값임을 보인다.
