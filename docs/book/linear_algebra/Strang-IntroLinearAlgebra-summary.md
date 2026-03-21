---
name: "Introduction to Linear Algebra, Fourth Edition"
type: book-summary
source_file: "Strang-IntroLinearAlgebra_full.md"
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

### Ch 2: Solving Linear Equations (pp. 31-120)

**핵심**: 연립선형방정식 Ax = b의 풀이를 행(row)과 열(column) 관점 모두에서 다룬다. 소거법(elimination)을 행렬 형태로 표현하고, 행렬 연산 규칙, 역행렬, LU 분해(A = LU), 전치행렬과 치환행렬을 체계적으로 설명한다. 행 관점(직선/평면의 교차)과 열 관점(열벡터의 선형결합)을 비교하여 직관을 제공한다.

**키워드**: `소거법`, `역행렬`, `LU분해`, `전치`, `치환행렬`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 2 (line 2812)

### Ch 3: Vector Spaces and Subspaces (pp. 121-195)

**핵심**: 개별 벡터에서 벡터 공간(vector space)과 부분공간(subspace)으로 사고를 확장한다. R^n 공간을 정의하고, 영공간(nullspace), 열공간(column space), 행공간(row space), 좌영공간(left nullspace)의 네 가지 기본 부분공간을 소개한다. 독립, 기저, 차원의 개념을 정립하고, 선형대수의 기본정리(Fundamental Theorem)를 제시한다.

**키워드**: `벡터공간`, `부분공간`, `기저`, `차원`, `랭크`, `네 가지 기본 부분공간`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 3 (line 8583)

### Ch 4: Orthogonality (pp. 196-244)

**핵심**: 직교성(orthogonality) 개념을 벡터에서 부분공간으로 확장한다. 네 가지 기본 부분공간이 쌍으로 직교함을 보이고(선형대수 기본정리 Part 2), 사영(projection)과 최소제곱법(least squares)을 다룬다. Gram-Schmidt 과정을 통해 직교 기저를 구성하는 방법을 제시한다.

**키워드**: `직교`, `사영`, `최소제곱법`, `Gram-Schmidt`, `직교기저`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 4 (line 13242)

### Ch 5: Determinants (pp. 245-283)

**핵심**: 행렬식(determinant)의 세 가지 핵심 성질로부터 출발하여 모든 공식을 유도한다. 행렬의 가역성 판별, 크래머 공칙(Cramer's rule), 역행렬 공식, 그리고 행렬식과 부피의 관계를 다룬다. 피벗의 곱이 행렬식과 같음을 보이며, 순열(permutation)과 여인수(cofactor)를 통한 공식을 제시한다.

**키워드**: `행렬식`, `여인수`, `크래머 공칙`, `순열`, `부피`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 5 (line 16363)

### Ch 6: Eigenvalues and Eigenvectors (pp. 284-375)

**핵심**: 동적 문제(미분방정식, 행렬 거듭제곱)에서 핵심적인 고유값과 고유벡터를 도입한다. 대각화(diagonalization)를 통해 A^100 같은 행렬 거듭제곱을 효율적으로 계산하는 방법을 보여준다. 대칭행렬의 실수 고유값, 양정치행렬(positive definite), 유사행렬(similar matrices), 특이값 분해(SVD)까지 확장한다.

**키워드**: `고유값`, `고유벡터`, `대각화`, `대칭행렬`, `양정치행렬`, `SVD`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 6 (line 18869)

### Ch 7: Linear Transformations (pp. 376-409)

**핵심**: 행렬 곱 Av를 선형변환 T(v)로 재해석한다. 선형변환의 정의(T(cv+dw) = cT(v)+dT(w))를 제시하고, 기저를 선택하면 모든 선형변환이 행렬로 표현됨을 보인다. 대각화와 의사역행렬(pseudoinverse)을 선형변환 관점에서 다룬다.

**키워드**: `선형변환`, `행렬 표현`, `의사역행렬`, `기저 변환`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 7 (line 24678)

### Ch 8: Applications (pp. 410-465)

**핵심**: 선형대수의 다양한 응용을 다룬다. 공학에서의 강성행렬(K = A^T C A), 그래프/네트워크의 접속행렬, 마르코프 행렬과 정상분포, 선형계획법, 푸리에 급수, 통계/확률에서의 선형대수, 컴퓨터 그래픽스를 포괄한다. 대칭 양정치행렬이 에너지를 표현하는 물리적 의미를 강조한다.

**키워드**: `공학 응용`, `그래프`, `마르코프`, `선형계획`, `푸리에`, `컴퓨터 그래픽`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 8 (line 26779)

### Ch 9: Numerical Linear Algebra (pp. 466-493)

**핵심**: 수치 선형대수의 핵심 문제인 속도와 정확성의 균형을 다룬다. 부분 피벗팅(partial pivoting)을 통한 안정성 확보, 희소행렬의 효율적 처리, 조건수(condition number)를 통한 불안정성 측정, 반복법(iterative methods)과 전처리기(preconditioners)를 통한 대규모 시스템 풀이를 설명한다.

**키워드**: `부분 피벗팅`, `조건수`, `반복법`, `희소행렬`, `켤레구배법`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 9 (line 30402)

### Ch 10: Complex Vectors and Matrices (pp. 494-516)

**핵심**: 실수 행렬에서도 복소수 고유값/고유벡터가 나타나므로 복소수 확장이 필수적임을 보인다. 에르미트 행렬(Hermitian), 유니터리 행렬(Unitary)을 대칭/직교행렬의 복소수 일반화로 소개한다. 고속 푸리에 변환(FFT)의 원리와 푸리에 행렬의 구조를 다룬다.

**키워드**: `복소수`, `에르미트 행렬`, `유니터리 행렬`, `FFT`, `푸리에 행렬`

**상세**: → `Gilbert Strang_Introduction_to_Linear_Algebra-_Fourth_Edition.md` Ch 10 (line 32111)
