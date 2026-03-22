---
name: "Linear Algebra and Its Applications, Fourth Edition"
type: book-summary
source_file: "Strang-LinearAlgebraApplications_azure_full.md"
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

### Ch 2: Vector Spaces (pp. 77-158)

**핵심**: 소거법 너머의 깊은 이해를 위해 벡터 공간과 부분공간 개념을 도입한다. Ax = 0과 Ax = b의 해를 체계적으로 분석하고, 선형독립/기저/차원을 정의한다. 네 가지 기본 부분공간(열공간, 영공간, 행공간, 좌영공간)을 통해 행렬의 본질을 파악한다. 그래프/네트워크와 선형변환을 응용으로 다룬다.

**키워드**: `벡터공간`, `부분공간`, `기저`, `차원`, `네 가지 기본 부분공간`, `선형변환`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 2 (line 5315)

### Ch 3: Orthogonality (pp. 159-224)

**핵심**: 직교 기저(orthogonal basis)가 선형대수 계산을 단순화하는 핵심임을 강조한다. 벡터의 길이, 직교성 판정(x^T y = 0), Gram-Schmidt 과정을 통한 직교벡터 생성을 다룬다. 기본 부분공간이 쌍으로 직교함을 보이고, 사영과 최소제곱법을 정리한다. FFT(고속 푸리에 변환)를 직교성의 응용으로 소개한다.

**키워드**: `직교`, `사영`, `최소제곱법`, `Gram-Schmidt`, `FFT`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 3 (line 10275)

### Ch 4: Determinants (pp. 225-259)

**핵심**: 행렬식이 선형대수의 중심에서 벗어났지만 여전히 유용한 도구임을 인정하며 다룬다. A^{-1}과 A^{-1}b에 대한 명시적 공식을 제공하고, 가역성 판별, n차원 부피 계산, 고유값 계산(det(A - λI) = 0)에 활용한다. 행렬식의 성질, 여인수 전개, 크래머 공칙을 설명한다.

**키워드**: `행렬식`, `여인수`, `크래머 공칙`, `가역성`, `부피`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 4 (line 14288)

### Ch 5: Eigenvalues and Eigenvectors (pp. 260-344)

**핵심**: 선형대수의 "후반부"를 여는 장으로, Ax = λx 문제를 본격적으로 다룬다. 고유값을 미분방정식(du/dt = Au)과 차분방정식(u_{k+1} = Au_k)에 적용하여 동적 시스템의 성장/감쇠/진동을 분석한다. 대각화, 행렬 거듭제곱, 복소행렬, 유사변환(similarity transformation)을 포괄한다.

**키워드**: `고유값`, `고유벡터`, `대각화`, `미분방정식`, `차분방정식`, `유사변환`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 5 (line 16248)

### Ch 6: Positive Definite Matrices (pp. 345-389)

**핵심**: 고유값의 부호가 중요한 양정치행렬을 독립된 장으로 심도 있게 다룬다. 극소/극대/안장점 판별에서 출발하여, 피벗/행렬식/고유값을 통한 양정치성 판별법을 제시한다. 특이값 분해(SVD), 최소원리(minimum principles), 유한요소법(FEM)을 양정치행렬의 응용으로 다룬다.

**키워드**: `양정치행렬`, `SVD`, `최소원리`, `유한요소법`, `이차형식`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 6 (line 21438)

### Ch 7: Computations with Matrices (pp. 390-416)

**핵심**: 수치 계산의 실제 문제를 다루며, 이론과 실용의 간극을 메운다. 행렬 노름과 조건수(condition number)를 통해 수치적 안정성을 정량화하고, 고유값 계산 알고리즘과 Ax = b에 대한 반복법(iterative methods)을 설명한다. 희소행렬 처리의 효율성을 강조한다.

**키워드**: `행렬 노름`, `조건수`, `고유값 계산`, `반복법`, `수치 안정성`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 7 (line 23945)

### Ch 8: Linear Programming and Game Theory (pp. 417-458)

**핵심**: 선형 부등식과 최적화를 선형대수의 관점에서 다룬다. 심플렉스법(simplex method)과 내부점법(interior point method)의 경쟁을 소개하고, 쌍대문제(dual problem)의 중요성을 강조한다. 네트워크 모형과 게임이론(행렬 게임)을 추가 응용으로 제시한다.

**키워드**: `선형계획`, `심플렉스법`, `쌍대문제`, `네트워크`, `게임이론`

**상세**: → `Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.md` Ch 8 (line 25388)
