---
name: "The Matrix Cookbook"
type: book-summary
source_file: "Petersen-MatrixCookbook_full.md"
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

### Ch 2: Derivatives (pp. 8-16)

**핵심**: 행렬 X에 대한 다양한 표현식의 미분을 집대성한다. 행렬식, 역행렬, 고유값의 미분, 행렬/벡터/스칼라 형식의 미분, trace의 미분(가장 방대한 공식 모음), 벡터/행렬 노름의 미분을 포함한다. X의 원소가 독립(비구조적)임을 기본 가정으로 하며, 구조화된 행렬(대칭 등)의 미분은 별도 절에서 다룬다.

**키워드**: `행렬 미분`, `행렬식 미분`, `역행렬 미분`, `trace 미분`, `구조화 행렬`

**상세**: → `matrixcookbook.md` Ch 2 (line 691)

### Ch 3: Inverses (pp. 17-23)

**핵심**: 역행렬에 관한 다양한 결과를 정리한다. 역행렬의 정의, 여인수/수반행렬을 통한 역행렬, 정확한 관계식(Woodbury 항등식, Sherman-Morrison 공식 등), 역행렬에 대한 함의, 역행렬의 근사(Neumann 급수), 일반화 역행렬, 의사역행렬(pseudo inverse)을 포함한다.

**키워드**: `역행렬`, `Woodbury`, `Sherman-Morrison`, `의사역행렬`, `Neumann 급수`

**상세**: → `matrixcookbook.md` Ch 3 (line 1418)

### Ch 4: Complex Matrices (pp. 24-27)

**핵심**: 복소 행렬에 대한 미분을 다룬다. 코시-리만 방정식을 만족하는 해석함수의 미분, 복소 켤레를 포함하는 경우의 일반화된 미분 정의, 고차/비선형 미분, 복소합의 역행렬을 정리한다.

**키워드**: `복소 미분`, `코시-리만`, `해석함수`, `복소 역행렬`

**상세**: → `matrixcookbook.md` Ch 4 (line 1915)

### Ch 5: Solutions and Decompositions (pp. 28-33)

**핵심**: 연립선형방정식의 풀이와 행렬 분해법을 정리한다. 단순선형회귀의 최소제곱 해, 선형시스템의 존재/유일성 조건, 고유값/고유벡터의 성질, 특이값 분해(SVD), 삼각분해, LU/LDM/LDL 분해를 포함한다.

**키워드**: `선형방정식`, `고유값`, `SVD`, `LU분해`, `최소제곱`

**상세**: → `matrixcookbook.md` Ch 5 (line 2148)

### Ch 6: Statistics and Probability (pp. 34-36)

**핵심**: 확률과 통계의 행렬 표현을 요약한다. 평균, 공분산 행렬, 3차/4차 적률의 정의, 선형결합의 기댓값(평균/공분산/교차공분산 변환 규칙), 가중 스칼라 변수의 기댓값을 정리한다.

**키워드**: `평균`, `공분산`, `적률`, `선형결합 기댓값`

**상세**: → `matrixcookbook.md` Ch 6 (line 2566)

### Ch 7: Multivariate Distributions (pp. 37-39)

**핵심**: 주요 다변량 분포의 밀도함수를 행렬 표기로 나열한다. 코시, 디리클레, 정규, 정규-역감마, 가우시안, 다항, 스튜던트 t, 위샤트, 역위샤트 분포의 밀도/모수를 정리한다.

**키워드**: `다변량 분포`, `위샤트`, `디리클레`, `스튜던트 t`, `정규`

**상세**: → `matrixcookbook.md` Ch 7 (line 2752)

### Ch 8: Gaussians (pp. 40-45)

**핵심**: 가우시안(정규) 분포에 관한 심층적 공식을 모은다. 밀도함수와 정규화, 조건부/주변부 분포, 적률(평균, 공분산, 4차 적률), 엔트로피, KL 발산, 가우시안 혼합 모형의 기본 공식을 포함한다.

**키워드**: `가우시안`, `조건부 분포`, `KL 발산`, `엔트로피`, `혼합 모형`

**상세**: → `matrixcookbook.md` Ch 8 (line 2898)

### Ch 9: Special Matrices (pp. 46-57)

**핵심**: 특수한 구조를 가진 행렬들의 성질을 정리한다. 블록행렬(곱, 행렬식, 역행렬, Schur 보원), DFT 행렬, 에르미트/반에르미트 행렬, 멱등행렬, 직교행렬, 양정치/반양정치 행렬, 단일원소행렬, 대칭/반대칭 행렬, 토플리츠 행렬, 전이행렬, 치환행렬, 반데르몬드 행렬을 포함한다.

**키워드**: `블록행렬`, `양정치`, `에르미트`, `토플리츠`, `직교행렬`

**상세**: → `matrixcookbook.md` Ch 9 (line 3267)

### Ch 10: Functions and Operators (pp. 58-63)

**핵심**: 행렬 함수와 연산자를 정리한다. 유한/무한 급수(행렬 지수함수, 로그 등), 스칼라 함수의 테일러 전개, 크로네커 곱과 vec 연산자의 성질, 벡터/행렬 노름, 랭크의 성질, 디랙 델타 함수를 포함하는 적분, 기타 유용한 항등식을 모은다.

**키워드**: `행렬 함수`, `크로네커 곱`, `vec 연산자`, `노름`, `테일러 전개`

**상세**: → `matrixcookbook.md` Ch 10 (line 4114)
