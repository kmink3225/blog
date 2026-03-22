---
name: "Introduction to Linear Algebra, Fourth Edition"
type: book-summary
source_file: "Strang-IntroLinearAlgebra_azure_full.md"
authors: "Gilbert Strang"
year: 2009
total_pages: 575
language: en
keywords: [linear algebra, vectors, matrices, eigenvalues, orthogonality, SVD, elimination, subspaces, determinants, linear transformations]
---

# Introduction to Linear Algebra, Fourth Edition — Summary

> Gilbert Strang (2009), 575 pages, 10 chapters
> 선형대수의 핵심 개념을 벡터, 행렬, 부분공간, 고유값 중심으로 체계적으로 다루는 MIT 교재이다.

## Contents

1. Introduction to Vectors (pp. 1-30)
   - 1.1 Vectors and Linear Combinations
   - 1.2 Lengths and Dot Products
   - 1.3 Matrices
2. Solving Linear Equations (pp. 31-120)
   - 2.1 Vectors and Linear Equations
   - 2.2 The Idea of Elimination
   - 2.3 Elimination Using Matrices
   - 2.4 Rules for Matrix Operations
   - 2.5 Inverse Matrices
   - 2.6 Elimination = Factorization: A = LU
   - 2.7 Transposes and Permutations
3. Vector Spaces and Subspaces (pp. 121-195)
   - 3.1 Spaces of Vectors
   - 3.2 The Nullspace of A: Solving Ax = 0
   - 3.3 The Rank and the Row Reduced Form
   - 3.4 The Complete Solution to Ax = b
   - 3.5 Independence, Basis and Dimension
   - 3.6 Dimensions of the Four Subspaces
4. Orthogonality (pp. 196-244)
   - 4.1 Orthogonality of the Four Subspaces
   - 4.2 Projections
   - 4.3 Least Squares Approximations
   - 4.4 Orthogonal Bases and Gram-Schmidt
5. Determinants (pp. 245-283)
   - 5.1 The Properties of Determinants
   - 5.2 Permutations and Cofactors
   - 5.3 Cramer's Rule, Inverses, and Volumes
6. Eigenvalues and Eigenvectors (pp. 284-375)
   - 6.1 Introduction to Eigenvalues
   - 6.2 Diagonalizing a Matrix
   - 6.3 Applications to Differential Equations
   - 6.4 Symmetric Matrices
   - 6.5 Positive Definite Matrices
   - 6.6 Similar Matrices
   - 6.7 Singular Value Decomposition (SVD)
7. Linear Transformations (pp. 376-409)
   - 7.1 The Idea of a Linear Transformation
   - 7.2 The Matrix of a Linear Transformation
   - 7.3 Diagonalization and the Pseudoinverse
8. Applications (pp. 410-465)
   - 8.1 Matrices in Engineering
   - 8.2 Graphs and Networks
   - 8.3 Markov Matrices, Population, and Economics
   - 8.4 Linear Programming
   - 8.5 Fourier Series: Linear Algebra for Functions
   - 8.6 Linear Algebra for Statistics and Probability
   - 8.7 Computer Graphics
9. Numerical Linear Algebra (pp. 466-493)
   - 9.1 Gaussian Elimination in Practice
   - 9.2 Norms and Condition Numbers
   - 9.3 Iterative Methods and Preconditioners
10. Complex Vectors and Matrices (pp. 494-516)
    - 10.1 Complex Numbers
    - 10.2 Hermitian and Unitary Matrices
    - 10.3 The Fast Fourier Transform

---

## Chapter Summaries

### Ch 1: Introduction to Vectors (pp. 1-30)

**핵심**: 선형대수의 두 가지 핵심 연산인 벡터 덧셈과 스칼라 곱을 소개한다. 선형결합 cv + dw의 개념을 도입하고, 벡터의 길이와 내적(dot product)을 정의한다. 2차원과 3차원에서 시작하여 n차원 공간으로의 확장이 자연스럽게 이루어짐을 보여주며, 행렬의 기본 개념을 미리 제시한다.

**키워드**: `벡터`, `선형결합`, `내적`, `길이`, `행렬`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 1 (line 772)

벡터의 덧셈과 스칼라 곱이라는 두 가지 기본 연산을 도입하고, 선형결합 cv+dw가 만드는 기하학적 구조를 2차원과 3차원에서 시각화한다. 내적(dot product) v·w = v₁w₁+...+vₙwₙ를 정의하고, 벡터의 길이 ||v|| = √(v·v)와 코사인 공식 cosθ = v·w/(||v|| ||w||)를 유도한다. 슈바르츠 부등식 |v·w| ≤ ||v|| ||w||과 삼각 부등식 ||v+w|| ≤ ||v||+||w||을 증명한다. 단위벡터와 직교 개념을 도입한다. 행렬을 열벡터의 모음으로 소개하고, Ax를 열벡터의 선형결합으로 해석하는 관점을 강조한다. 선형방정식과 행렬을 미리 제시하여, 이후 장들에서 다룰 소거법과 부분공간의 동기를 부여한다.

### Ch 2: Solving Linear Equations (pp. 31-120)

**핵심**: 연립선형방정식 Ax = b의 풀이를 행(row)과 열(column) 관점 모두에서 다룬다. 소거법(elimination)을 행렬 형태로 표현하고, 행렬 연산 규칙, 역행렬, LU 분해(A = LU), 전치행렬과 치환행렬을 체계적으로 설명한다. 행 관점(직선/평면의 교차)과 열 관점(열벡터의 선형결합)을 비교하여 직관을 제공한다.

**키워드**: `소거법`, `역행렬`, `LU분해`, `전치`, `치환행렬`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 2 (line 2812)

연립선형방정식 Ax=b를 행 관점(직선/평면의 교차)과 열 관점(열벡터의 선형결합)으로 해석한다. 소거법(elimination)의 아이디어를 도입하고, 피벗(pivot)의 역할과 실패 조건을 설명한다. 소거법을 소거행렬 E를 이용한 행렬 곱으로 표현하고, EA=U(상삼각행렬)를 유도한다. 행렬 곱셈의 네 가지 관점(내적, 열, 행, 외적)을 비교한다. 역행렬의 정의와 존재 조건을 다루고, 가우스-조르단 방법 [A|I]→[I|A^{-1}]을 소개한다. LU 분해 A=LU를 소거법의 행렬 표현으로 유도하고, 연산량이 n³/3임을 보인다. 전치행렬의 성질(AB)^T = B^T A^T를 증명하고, 대칭행렬의 LDL^T 분해를 유도한다. 치환행렬(permutation matrix)을 도입하여 행 교환이 필요한 경우의 PA=LU 분해를 설명한다.

### Ch 3: Vector Spaces and Subspaces (pp. 121-195)

**핵심**: 개별 벡터에서 벡터 공간(vector space)과 부분공간(subspace)으로 사고를 확장한다. R^n 공간을 정의하고, 영공간(nullspace), 열공간(column space), 행공간(row space), 좌영공간(left nullspace)의 네 가지 기본 부분공간을 소개한다. 독립, 기저, 차원의 개념을 정립하고, 선형대수의 기본정리(Fundamental Theorem)를 제시한다.

**키워드**: `벡터공간`, `부분공간`, `기저`, `차원`, `랭크`, `네 가지 기본 부분공간`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 3 (line 8583)

벡터 공간의 정의(벡터 덧셈과 스칼라 곱에 대해 닫힘)를 R^n에서 시작하여 함수 공간, 행렬 공간 등으로 확장한다. 부분공간(subspace)을 정의하고, 열공간 C(A)과 영공간 N(A)을 Ax=b와 Ax=0의 해집합으로 소개한다. 소거법으로 Ax=0의 특수해를 구하고, 자유변수의 개념을 도입한다. 행 사다리꼴(rref)을 소개하고, 피벗 열/자유 열의 구분을 명확히 한다. Ax=b의 완전해를 특수해+영공간으로 표현하고, 해의 존재 조건을 열공간 소속으로 설명한다. 선형독립, 생성(span), 기저(basis), 차원(dimension)의 개념을 정의하고 관계를 정립한다. 랭크를 피벗 수=열공간의 차원=행공간의 차원으로 정의한다. 네 가지 기본 부분공간(열공간, 영공간, 행공간, 좌영공간)의 차원 관계를 랭크-넘무차원 정리(rank-nullity theorem)로 정리하고, 이것이 선형대수의 기본정리(Fundamental Theorem)의 첫 번째 부분임을 제시한다.

### Ch 4: Orthogonality (pp. 196-244)

**핵심**: 직교성(orthogonality) 개념을 벡터에서 부분공간으로 확장한다. 네 가지 기본 부분공간이 쌍으로 직교함을 보이고(선형대수 기본정리 Part 2), 사영(projection)과 최소제곱법(least squares)을 다룬다. Gram-Schmidt 과정을 통해 직교 기저를 구성하는 방법을 제시한다.

**키워드**: `직교`, `사영`, `최소제곱법`, `Gram-Schmidt`, `직교기저`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 4 (line 13242)

네 가지 기본 부분공간이 쌍으로 직교함을 증명한다. 행공간과 영공간은 R^n의 직교보(orthogonal complement)이며, 열공간과 좌영공간은 R^m의 직교보이다. 이것이 선형대수 기본정리의 두 번째 부분이다. 사영(projection) 개념을 도입하여, 직선 위의 사영 p = (a^T b/a^T a)a와 부분공간 위의 사영 p = A(A^T A)^{-1}A^T b를 유도한다. 사영행렬 P = A(A^T A)^{-1}A^T가 대칭이고 멱등(P²=P)임을 증명한다. 최소제곱법(least squares)을 Ax=b에 해가 없을 때 오차 ||Ax-b||²를 최소화하는 문제로 정식화하고, 정규방정식 A^T Ax̂ = A^T b를 유도한다. 데이터 피팅(직선, 포물선)에의 응용을 보인다. Gram-Schmidt 과정을 설명하여 독립 벡터 집합으로부터 직교정규 기저를 구성하는 방법을 시연하고, QR 분해 A=QR을 유도한다.

### Ch 5: Determinants (pp. 245-283)

**핵심**: 행렬식(determinant)의 세 가지 핵심 성질로부터 출발하여 모든 공식을 유도한다. 행렬의 가역성 판별, 크래머 공칙(Cramer's rule), 역행렬 공식, 그리고 행렬식과 부피의 관계를 다룬다. 피벗의 곱이 행렬식과 같음을 보이며, 순열(permutation)과 여인수(cofactor)를 통한 공식을 제시한다.

**키워드**: `행렬식`, `여인수`, `크래머 공칙`, `순열`, `부피`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 5 (line 16363)

행렬식의 세 가지 핵심 성질(det I=1, 행 교환시 부호 변경, 각 행에 대한 선형성)에서 출발하여 나머지 모든 성질을 유도한다. 특이행렬의 행렬식이 0임을 보이고, det(AB) = det(A)det(B)를 증명한다. 피벗의 곱이 행렬식과 같음(det A = ±d₁d₂...dₙ)을 LU 분해로 증명한다. 순열(permutation)을 이용한 행렬식의 "빅 공식" det A = Σ(±)a_{1α}a_{2β}...a_{nω}를 유도한다. 여인수(cofactor) 전개로 행렬식을 계산하는 방법을 제시한다. 크래머 공칙(Cramer's rule) x_i = det(B_i)/det(A)를 유도하고, 역행렬 공식 A^{-1} = C^T/det(A)를 제시한다. 행렬식과 n차원 부피의 관계를 설명하고, 평행육면체의 부피가 |det A|임을 보인다. 외적(cross product)을 행렬식으로 정의한다.

### Ch 6: Eigenvalues and Eigenvectors (pp. 284-375)

**핵심**: 동적 문제(미분방정식, 행렬 거듭제곱)에서 핵심적인 고유값과 고유벡터를 도입한다. 대각화(diagonalization)를 통해 A^100 같은 행렬 거듭제곱을 효율적으로 계산하는 방법을 보여준다. 대칭행렬의 실수 고유값, 양정치행렬(positive definite), 유사행렬(similar matrices), 특이값 분해(SVD)까지 확장한다.

**키워드**: `고유값`, `고유벡터`, `대각화`, `대칭행렬`, `양정치행렬`, `SVD`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 6 (line 18869)

Ax=λx 문제를 도입하고, 고유값이 det(A-λI)=0의 근이며 고유벡터가 (A-λI)x=0의 비자명해임을 보인다. 고유값의 합이 trace, 곱이 행렬식과 같음을 증명한다. 대각화 A=SΛS^{-1}의 조건(n개의 독립 고유벡터)을 제시하고, 대각화를 이용한 A^k = SΛ^k S^{-1} 계산을 시연한다. 차분방정식 u_{k+1}=Au_k과 미분방정식 du/dt=Au에의 응용을 다룬다. 행렬 지수함수 e^{At}를 고유값으로 분석하여 안정성(모든 Re(λ)<0) 조건을 유도한다. 대칭행렬의 스펙트럼 정리(실수 고유값, 직교 고유벡터)를 증명하고 A=QΛQ^T를 유도한다. 양정치행렬의 5가지 동치 조건(양의 고유값, 양의 피벗, 양의 소행렬식, 양의 에너지 x^T Ax>0, A=R^T R)을 제시한다. 유사행렬(similar matrices)의 동일한 고유값과 Jordan 형을 다룬다. 특이값 분해 A=UΣV^T를 유도하고, 네 기본 부분공간의 직교기저를 SVD로 구성하는 방법을 보인다.

### Ch 7: Linear Transformations (pp. 376-409)

**핵심**: 행렬 곱 Av를 선형변환 T(v)로 재해석한다. 선형변환의 정의(T(cv+dw) = cT(v)+dT(w))를 제시하고, 기저를 선택하면 모든 선형변환이 행렬로 표현됨을 보인다. 대각화와 의사역행렬(pseudoinverse)을 선형변환 관점에서 다룬다.

**키워드**: `선형변환`, `행렬 표현`, `의사역행렬`, `기저 변환`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 7 (line 24678)

선형변환 T의 정의(T(cv+dw) = cT(v)+dT(w))를 제시하고, 회전, 사영, 미분, 적분 등이 선형변환의 예임을 보인다. 기저를 선택하면 모든 선형변환이 행렬로 표현됨을 증명하고, 입력 기저와 출력 기저가 다를 수 있음을 설명한다. 기저 변환(change of basis) 공식 B = M^{-1}AM을 유도하고, 이것이 유사변환(similarity transformation)과 같음을 보인다. 좋은 기저의 선택이 행렬을 대각행렬이나 Jordan 형으로 단순화함을 강조한다. 대각화를 선형변환 관점에서 재해석하여, 고유벡터 기저에서 변환이 단순한 스칼라 곱이 됨을 보인다. 의사역행렬(pseudoinverse) A^+를 SVD로 정의하고(σ_i를 1/σ_i로, 0은 0으로), A^+가 Ax=b의 최소제곱 최소노름해를 줌을 보인다. 의사역행렬의 기하학적 해석을 네 기본 부분공간과 연결한다.

### Ch 8: Applications (pp. 410-465)

**핵심**: 선형대수의 다양한 응용을 다룬다. 공학에서의 강성행렬(K = A^T C A), 그래프/네트워크의 접속행렬, 마르코프 행렬과 정상분포, 선형계획법, 푸리에 급수, 통계/확률에서의 선형대수, 컴퓨터 그래픽스를 포괄한다. 대칭 양정치행렬이 에너지를 표현하는 물리적 의미를 강조한다.

**키워드**: `공학 응용`, `그래프`, `마르코프`, `선형계획`, `푸리에`, `컴퓨터 그래픽`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 8 (line 26779)

공학에서의 강성행렬(stiffness matrix) K = A^T CA를 스프링 시스템으로 설명하고, A가 접속행렬(incidence matrix), C가 물질 상수행렬임을 보인다. K가 대칭 양반정치임을 A^T CA 구조에서 유도한다. 그래프와 네트워크를 접속행렬로 표현하고, 키르히호프 법칙과의 관계를 다룬다. 마르코프 행렬(모든 원소 ≥ 0, 열합 1)의 정상분포(steady state)를 고유값 1의 고유벡터로 구하고, |λ|≤1인 고유값 성질을 증명한다. 인구 이동과 경제 모형에 응용한다. 선형계획법(linear programming)의 기초를 가능해 영역(feasible region)과 코너점 최적성으로 설명한다. 푸리에 급수를 선형대수의 관점에서 재해석하여, 함수 공간의 직교기저로서의 sin/cos 함수를 다룬다. 통계/확률에서의 선형대수(평균, 분산, 공분산의 행렬 표현)를 다룬다. 컴퓨터 그래픽스에서의 아핀변환과 동차좌표(homogeneous coordinates)를 소개한다.

### Ch 9: Numerical Linear Algebra (pp. 466-493)

**핵심**: 수치 선형대수의 핵심 문제인 속도와 정확성의 균형을 다룬다. 부분 피벗팅(partial pivoting)을 통한 안정성 확보, 희소행렬의 효율적 처리, 조건수(condition number)를 통한 불안정성 측정, 반복법(iterative methods)과 전처리기(preconditioners)를 통한 대규모 시스템 풀이를 설명한다.

**키워드**: `부분 피벗팅`, `조건수`, `반복법`, `희소행렬`, `켤레구배법`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 9 (line 30402)

실제 계산에서 가우스 소거법의 안정성 문제를 다루며, 부분 피벗팅(partial pivoting)으로 성장인자(growth factor)를 제어하는 방법을 설명한다. 희소행렬(sparse matrix)의 효율적 저장과 대역행렬(banded matrix)의 LU 분해에서 대역폭이 보존됨을 보인다. 재정렬(reordering)로 채움(fill-in)을 줄이는 전략을 소개한다. 행렬 노름(||A||)을 정의하고, 유도 노름(induced norm)으로서의 2-노름 ||A||₂ = σ_max를 제시한다. 조건수 c(A) = σ_max/σ_min = ||A|| ||A^{-1}||을 정의하고, 조건수가 큰 행렬에서 해의 작은 변동이 큰 오차를 야기함을 수치 예로 시연한다. 반복법(iterative methods)으로 야코비법과 가우스-자이델법을 소개하고 수렴 조건(스펙트럼 반경 < 1)을 제시한다. 전처리기(preconditioner) P를 이용한 P^{-1}Ax = P^{-1}b의 아이디어를 설명한다. 켤레구배법(conjugate gradient method)을 양정치 시스템에 대한 효율적 반복법으로 소개하고, 크릴로프 부분공간에서의 최적성을 설명한다.

### Ch 10: Complex Vectors and Matrices (pp. 494-516)

**핵심**: 실수 행렬에서도 복소수 고유값/고유벡터가 나타나므로 복소수 확장이 필수적임을 보인다. 에르미트 행렬(Hermitian), 유니터리 행렬(Unitary)을 대칭/직교행렬의 복소수 일반화로 소개한다. 고속 푸리에 변환(FFT)의 원리와 푸리에 행렬의 구조를 다룬다.

**키워드**: `복소수`, `에르미트 행렬`, `유니터리 행렬`, `FFT`, `푸리에 행렬`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 10 (line 32111)

복소수의 기본 연산(덧셈, 곱셈, 켤레, 절대값)을 복습하고, 오일러 공식 e^{iθ} = cosθ + i sinθ를 소개한다. 실수 행렬에서도 복소 고유값이 나타나는 예(90도 회전행렬의 고유값 i, -i)를 들어 복소수 확장의 필요성을 동기화한다. 에르미트 행렬(A^H = A)이 대칭행렬의 복소수 일반화이며, 고유값이 항상 실수이고 고유벡터가 직교함을 증명한다. 유니터리 행렬(U^H U = I)이 직교행렬의 복소수 일반화이며, 고유값의 절대값이 1임을 보인다. 모든 정방행렬에 대한 Schur 정리(유니터리 유사변환으로 상삼각화)를 증명한다. 정규행렬(A^H A = AA^H)의 대각화 가능성을 다룬다. 고속 푸리에 변환(FFT)의 원리를 푸리에 행렬 F_n의 재귀적 인수분해로 설명하고, 연산량이 n²에서 (n/2)log₂n으로 줄어드는 것을 보인다. 푸리에 행렬의 열이 직교함(F^H F = nI)을 증명한다.
