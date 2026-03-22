# The Matrix Cookbook [ http: //matrixcookbook. com

Kaare Brandt Petersen
Michael Syskind Pedersen
VERSION: NOVEMBER 15, 2012

<!-- PageNumber="1" -->
<!-- PageBreak -->


## Introduction

What is this? These pages are a collection of facts (identities, approxima-
tions, inequalities, relations, ... ) about matrices and matters relating to them.
It is collected in this form for the convenience of anyone who wants a quick
desktop reference .

Disclaimer: The identities, approximations and relations presented here were
obviously not invented but collected, borrowed and copied from a large amount
of sources. These sources include similar but shorter notes found on the internet
and appendices in books - see the references for a full list.

Errors: Very likely there are errors, typos, and mistakes for which we apolo-
gize and would be grateful to receive corrections at cookbook@2302.dk.

Its ongoing: The project of keeping a large repository of relations involving
matrices is naturally ongoing and the version will be apparent from the date in
the header.

Suggestions: Your suggestion for additional content or elaboration of some
topics is most welcome acookbook@2302.dk.

Keywords: Matrix algebra, matrix relations, matrix identities, derivative of
determinant, derivative of inverse matrix, differentiate a matrix.

Acknowledgements: We would like to thank the following for contributions
and suggestions: Bill Baxter, Brian Templeton, Christian Rishøj, Christian
Schröppel, Dan Boley, Douglas L. Theobald, Esben Hoegh-Rasmussen, Evripidis
Karseras, Georg Martius, Glynne Casteel, Jan Larsen, Jun Bin Gao, Jürgen
Struckmeier, Kamil Dedecius, Karim T. Abou-Moustafa, Korbinian Strimmer,
Lars Christiansen, Lars Kai Hansen, Leland Wilkinson, Liguo He, Loic Thibaut,
Markus Froeb, Michael Hubatka, Miguel Barão, Ole Winther, Pavel Sakov,
Stephan Hattinger, Troels Pedersen, Vasile Sima, Vincent Rabaud, Zhaoshui
He. We would also like thank The Oticon Foundation for funding our PhD
studies.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 2" -->
<!-- PageBreak -->

<!-- PageHeader="CONTENTS" -->
<!-- PageHeader="CONTENTS" -->


## Contents


### 1 Basics 6

1.1 Trace
6

1.2
Determinant
6

1.3
The Special Case 2x2
7

2
Derivatives
8

2.1
1 Derivatives of a Determinant
8

2.2
Derivatives of an Inverse
9

2.3
Derivatives of Eigenvalues
10

2.4
4 Derivatives of Matrices, Vectors and Scalar Forms
10

2.5
Derivatives of Traces
12

2.6
Derivatives of vector norms
14

2.7
Derivatives of matrix norms
14

2.8
Derivatives of Structured Matrices
14


#### 3 Inverses 17

3.1 Basic
17

3.2
Exact Relations
18

3.3
3 Implication on Inverses
20

3.4
Approximations
20

3.5
Generalized Inverse
21

3.6
Pseudo Inverse
21

4
Complex Matrices
24

4.1
Complex Derivatives
24

4.2
Higher order and non-linear derivatives
26

4.3
Inverse of complex sum
27

5
Solutions and Decompositions
28

5.1
Solutions to linear equations
28

5.2
Eigenvalues and Eigenvectors
30

5.3
Singular Value Decomposition
31

5.4
Triangular Decomposition
32

5.5
LU decomposition
32

5.6
LDM decomposition
33

5.7
LDL decompositions
33

6
Statistics and Probability
34

6.1
Definition of Moments
34

6.2
Expectation of Linear Combinations
35

6.3
Weighted Scalar Variable
36

7
Multivariate Distributions
37

7.1
Cauchy
37

7.2
Dirichlet
37

7.3
Normal
37

7.4
Normal-Inverse Gamma
37

7.5
Gaussian
37

7.6
Multinomial
37

PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 3

<!-- PageBreak -->


<table>
<tr>
<th>CONTENTS</th>
<th>CONTENTS</th>
</tr>
<tr>
<td>7.7 Student's t</td>
<td>37</td>
</tr>
<tr>
<td>7.8 Wishart</td>
<td>38</td>
</tr>
<tr>
<td>7.9 Wishart, Inverse</td>
<td>39</td>
</tr>
<tr>
<td>8 Gaussians</td>
<td>40</td>
</tr>
<tr>
<td>8.1 Basics</td>
<td>40</td>
</tr>
<tr>
<td>8.2 Moments</td>
<td>42</td>
</tr>
<tr>
<td>8.3 Miscellaneous</td>
<td>44</td>
</tr>
<tr>
<td>8.4 Mixture of Gaussians</td>
<td>44</td>
</tr>
<tr>
<td>9 Special Matrices</td>
<td>46</td>
</tr>
<tr>
<td>9.1 Block matrices</td>
<td>46</td>
</tr>
<tr>
<td>9.2 Discrete Fourier Transform Matrix, The</td>
<td>47</td>
</tr>
<tr>
<td>9.3 Hermitian Matrices and skew-Hermitian</td>
<td>48</td>
</tr>
<tr>
<td>9.4 Idempotent Matrices</td>
<td>49</td>
</tr>
<tr>
<td>9.5 Orthogonal matrices</td>
<td>49</td>
</tr>
<tr>
<td>9.6 Positive Definite and Semi-definite Matrices</td>
<td>50</td>
</tr>
<tr>
<td>9.7 Singleentry Matrix, The</td>
<td>52</td>
</tr>
<tr>
<td>9.8 Symmetric, Skew-symmetric/ Antisymmetric</td>
<td>54</td>
</tr>
<tr>
<td>9.9 Toeplitz Matrices</td>
<td>54</td>
</tr>
<tr>
<td>9.10 Transition matrices</td>
<td>55</td>
</tr>
<tr>
<td>9.11 Units, Permutation and Shift</td>
<td>56</td>
</tr>
<tr>
<td>9.12 Vandermonde Matrices</td>
<td>57</td>
</tr>
<tr>
<td>10 Functions and Operators</td>
<td>58</td>
</tr>
<tr>
<td>10.1 Functions and Series</td>
<td>58</td>
</tr>
<tr>
<td>10.2 Kronecker and Vec Operator</td>
<td>59</td>
</tr>
<tr>
<td>10.3 Vector Norms</td>
<td>61</td>
</tr>
<tr>
<td>10.4 Matrix Norms</td>
<td>61</td>
</tr>
<tr>
<td>10.5 Rank</td>
<td>62</td>
</tr>
<tr>
<td>10.6 Integral Involving Dirac Delta Functions</td>
<td>62</td>
</tr>
<tr>
<td>10.7 Miscellaneous</td>
<td>63</td>
</tr>
<tr>
<td>A One-dimensional Results</td>
<td>64</td>
</tr>
<tr>
<td>A.1 Gaussian .</td>
<td>64</td>
</tr>
<tr>
<td>A.2 One Dimensional Mixture of Gaussians</td>
<td>65</td>
</tr>
<tr>
<td>B Proofs and Details</td>
<td>66</td>
</tr>
<tr>
<td>B.1 Misc Proofs</td>
<td>66</td>
</tr>
</table>


<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 4" -->
<!-- PageBreak -->

<!-- PageHeader="CONTENTS" -->
<!-- PageHeader="CONTENTS" -->


## Notation and Nomenclature

$\mathrm { A }$
Matrix

$\mathrm { A } _ { i j }$
Matrix indexed for some purpose

$\mathrm { A } _ { i }$
Matrix indexed for some purpose

$\mathrm { A } ^ { i j }$
Matrix indexed for some purpose

$\mathrm { A } ^ { n }$
Matrix indexed for some purpose or

The n.th power of a square matrix

$A ^ { - 1 }$
The inverse matrix of the matrix A

$\mathrm { A }$
The pseudo inverse matrix of the matrix $\mathrm { A }$ (see Sec. 3.6)

$\mathrm { A } ^ { 1 / 2 }$
The square root of a matrix (if unique), not elementwise

$\left( \mathrm { A } \right) _ { i j }$
The $\left( i , \right.$ j).th entry of the matrix A

$A _ { i j }$
The $\left( i , \right.$ j).th entry of the matrix A

$\left. \mathrm { A } \right] _ { i j }$
$\mathrm { T h e } i j \mathrm { - s u b m a t r i } ,$ i.e. A with i.th row and j.th column deleted
a
Vector (column-vector)

$a i$
Vector indexed for some purpose

$a _ { i }$
The i.th element of the vector a

a
Scalar

$\mathfrak{R} z$
Real part of a scalar

$\mathfrak{R} \mathrm { z }$
Real part of a vector

AZ
Real part of a matrix

Sz
Imaginary part of a scalar

$\mathfrak{I} \mathrm { z }$
Imaginary part of a vector

SZ
Imaginary part of a matrix

$\det \left( \mathrm { A } \right)$
$\mathrm { D e t e r m i n a n t <space> o f } \mathrm { A }$

$\mathrm { T r } \left( \mathrm { A } \right)$
Trace of the matrix $\mathrm { A }$

$\mathrm { d i a g } \left( \mathrm { A } \right)$
Diagonal matrix of the matrix $\mathrm { A } ,$ i.e. $\left( \mathrm { d i a g } \left( \mathrm { A } \right) \right) _ { i j } = \delta _ { i j } A _ { i j }$

$\mathrm { e i g } \left( \mathrm { A } \right)$
Eigenvalues of the matrix A

$\mathrm { v e c } \left( \mathrm { A } \right)$
The vector-version of the matrix $\mathrm { A }$ (see Sec. 10.2.2)

sup
Supremum of a set

$| | \mathrm { A } |$
Matrix norm (subscript if any denotes what norm)

$\mathrm { A } ^ { T }$
Transposed matrix

$A ^ { - T }$
The inverse of the transposed and vice versa, $\mathrm { A } ^ { - T } = \left( \mathrm { A } ^ { - 1 } \right) ^ { T } = \left( \mathrm { A } ^ { T } \right) ^ { - 1 } .$

$\mathrm { A } ^ { * }$
Complex conjugated matrix

$\mathrm { A } ^ { H }$
Transposed and complex conjugated matrix (Hermitian)

$\mathrm { A } \circ \mathrm { B }$
Hadamard (elementwise) product

$\mathrm { A } \otimes \mathrm { B }$
☒
Kronecker product

0
The null matrix. Zero in all entries.

I
The identity matrix

$\mathrm { J } ^ { i j }$
The single-entry matrix, 1 at $\left( i , j \right)$ and zero elsewhere

$\Sigma$
A positive definite matrix

$\Lambda$
A diagonal matrix

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 5" -->
<!-- PageBreak -->

<!-- PageHeader="1 BASICS" -->


## 1 Basics

(AB)-1 = $\mathrm { B } ^ { - 1 } \mathrm { A } ^ { \cdot }$
(1)

$$\left( \mathrm { A B C } \ldots \right) ^ { - 1 } = \ldots \mathrm { C } ^ { - 1 } \mathrm { B } ^ { - 1 } \mathrm { A } ^ { - 1 }$$
$$\left( A ^ { T } \right) ^ { - 1 } = \left( A ^ { - 1 } \right) ^ { T }$$
$$\left( A + B \right) ^ { T } = A ^ { T } + B ^ { T }$$
$$\left( A B \right) ^ { T } = B ^ { T } A ^ { T }$$
$$\left( \mathrm { A B C } _ { \cdots } \right) ^ { T } = \ldots \mathrm { C } ^ { T } \mathrm { B } ^ { T } \mathrm { A } ^ { T }$$
$$\left( A ^ { H } \right) ^ { - 1 } = \left( A ^ { - 1 } \right) ^ { H }$$
$$\left( \mathrm { A } + \mathrm { B } \right) ^ { H } = \mathrm { A } ^ { H } + \mathrm { B } ^ { H }$$
$$\left( \mathrm { A B } \right) ^ { H } = \mathrm { B } ^ { H } \mathrm { A } ^ { H }$$
$$\left( \mathrm { A B C } \ldots \right) ^ { H } = \ldots \mathrm { C } ^ { H } \mathrm { B } ^ { H } \mathrm { A } ^ { H }$$

(2)
(3)
(4)

(5)
(6)

(7)

(8)

(9)

(10)


### 1.1 Trace

$$\mathrm { T r } \left( \mathrm { A } \right) = \sum _ { i } A _ { i i }$$
$$\mathrm { T r } \left( \mathrm { A } \right) = \sum _ { i } \lambda _ { i } , \quad \lambda _ { i } = \mathrm { e i g } \left( \mathrm { A } \right) ,$$
(11)
(12)

$$\mathrm { T r } \left( \mathrm { A } \right) = \mathrm { T r } \left( \mathrm { A } ^ { T } \right)$$
$$\mathrm { T r } \left( \mathrm { A B } \right) = \mathrm { T r } \left( \mathrm { B A } \right)$$
$$\mathrm { T r } \left( \mathrm { A } + \mathrm { B } \right) = \mathrm { T r } \left( \mathrm { A } \right) + \mathrm { T r } \left( \mathrm { B } \right)$$
$$\mathrm { T r } \left( \mathrm { A B C } \right) = \mathrm { T r } \left( \mathrm { B C A } \right) = \mathrm { T r } \left( \mathrm { C A B } \right)$$
$$\mathrm { a } ^ { T } \mathrm { a } = \mathrm { T r } \left( \mathrm { a a } ^ { T } \right)$$
(13)
(14)
(15)
(16)
(17)


### 1.2 Determinant

Let $\mathrm { A }$ be an $n \times n$ matrix.

$$\det \left( \mathrm { A } \right) = \prod _ { i } \lambda _ { i } \quad \lambda _ { i } = \mathrm { e i g } \left( \mathrm { A } \right)$$
$$\det \left( c \mathrm { A } \right) = c ^ { n } \det \left( \mathrm { A } \right) , \quad \mathrm { i f } \mathrm { A } \in \mathbb{R} ^ { n \times n } ,$$
(18)
(19)

$$\det \left( \mathrm { A } ^ { T } \right) = \det \left( \mathrm { A } \right)$$
$$\det \left( \mathrm { A B } \right) = \det \left( \mathrm { A } \right) \det \left( \mathrm { B } \right)$$
$$\det \left( \mathrm { A } ^ { - 1 } \right) = 1 / \det \left( \mathrm { A } \right)$$
$$\det \left( \mathrm { A } ^ { n } \right) = \det \left( \mathrm { A } \right) ^ { n }$$
$$\det \left( \mathrm { I } + \mathrm { u v } ^ { T } \right) = 1 + \mathrm { u } ^ { T } \mathrm { v }$$
(20)
(21)
(22)
(23)
(24)

For $n = 2 :$

$$\det \left( \mathrm { I } + \mathrm { A } \right) = 1 + \det \left( \mathrm { A } \right) + \mathrm { T r } \left( \mathrm { A } \right)$$
(25)

For $n = 3 :$

$$\det \left( \mathrm { I } + \mathrm { A } \right) = 1 + \det \left( \mathrm { A } \right) + \mathrm { T r } \left( \mathrm { A } \right) + \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { A } \right) ^ { 2 } - \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { A } ^ { 2 } \right)$$
(26)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 6" -->


<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="1 BASICS" -->
<!-- PageHeader="1.3 The Special Case 2x2" -->

For $n = 4 :$

$$\det \left( \mathrm { I } + \mathrm { A } \right) = 1 + \det \left( \mathrm { A } \right) + \mathrm { T r } \left( \mathrm { A } \right) + \frac { 1 } { 2 }$$
$$+ \mathrm { T r } \left( A \right) ^ { 2 } - \frac { 1 } { 2 } \mathrm { T r } \left( A ^ { 2 } \right)$$
$$+ \frac { 1 } { 6 } \mathrm { T r } \left( \mathrm { A } \right) ^ { 3 } - \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { A } \right) \mathrm { T r } \left( \mathrm { A } ^ { 2 } \right) + \frac { 1 } { 3 } \mathrm { T r } \left( \mathrm { A } ^ { 3 } \right)$$

(27)

For small &, the following approximation holds

$$\det \left( \mathrm { I } + \varepsilon \mathrm { A } \right) \cong 1 + \det \left( \mathrm { A } \right) + \varepsilon \mathrm { T r } \left( \mathrm { A } \right) + \frac { 1 } { 2 } \varepsilon ^ { 2 } \mathrm { T r } \left( \mathrm { A } \right) ^ { 2 } - \frac { 1 } { 2 } \varepsilon ^ { 2 } \mathrm { T r } \left( \mathrm { A } ^ { 2 } \right)$$
(28)


### 1.3 The Special Case $2 \times 2$

Consider the matrix A

$$A = \left[ \begin{array}{} { A _ { 1 1 } } & { A _ { 1 2 } } \\ { A _ { 2 1 } } & { A _ { 2 2 } } \end{array} \right]$$

Determinant and trace

$$\det \left( \mathrm { A } \right) = A _ { 1 1 } A _ { 2 2 } - A _ { 1 2 } A _ { 2 1 }$$
(29)

$$\mathrm { T r } \left( \mathrm { A } \right) = A _ { 1 1 } + A _ { 2 2 }$$
(30)

Eigenvalues

$$\lambda ^ { 2 } - \lambda \cdot \mathrm { T r } \left( \mathrm { A } \right) + \det \left( \mathrm { A } \right) = 0$$

$$\lambda _ { 1 } = \frac { \mathrm { T r } \left( \mathrm { A } \right) + \sqrt { \mathrm { T r } \left( \mathrm { A } \right) ^ { 2 } - 4 \det \left( \mathrm { A } \right) } } { 2 } \quad \lambda _ { 2 } = \frac { \mathrm { T r } \left( \mathrm { A } \right) - \sqrt { \mathrm { T r } \left( \mathrm { A } \right) ^ { 2 } - 4 \det \left( \mathrm { A } \right) } } { 2 }$$
$$\lambda _ { 1 } + \lambda _ { 2 } = \mathrm { T r } \left( \mathrm { A } \right) \quad \lambda _ { 1 } \lambda _ { 2 } = \det \left( \mathrm { A } \right)$$

Eigenvectors

$$\mathrm { v } _ { 1 } \propto \left[ \begin{array}{} A _ { 1 2 } \\ \lambda _ { 1 } - A _ { 1 1 } \end{array} \right] \quad \mathrm { v } _ { 2 } \propto \left[ \begin{array}{} A _ { 1 2 } \\ \lambda _ { 2 } - A _ { 1 1 } \end{array} \right]$$

Inverse

$$\mathrm { A } ^ { - 1 } = \frac { 1 } { \det \left( \mathrm { A } \right) } \left[ \begin{array}{} A _ { 2 2 } & - A _ { 1 2 } \\ - A _ { 2 1 } & A _ { 1 1 } \end{array} \right]$$
(31)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 7" -->
<!-- PageBreak -->

<!-- PageHeader="2 DERIVATIVES" -->


## 2 Derivatives

This section is covering differentiation of a number of expressions with respect to
a matrix X. Note that it is always assumed that $\mathrm { X }$ has no special structure, i.e.
☒ ☒

that the elements of $\mathrm { X }$ are independent (e.g. not symmetric, Toeplitz, positive
☒
definite). See section 2.8 for differentiation of structured matrices. The basic
assumptions can be written in a formula as

$$\frac { \partial X _ { k l } } { \partial X _ { i j } } = \delta _ { i k } \delta _ { l j }$$
(32)
☒

that is for e.g. vector forms,

$$\left[ \frac { \partial \mathrm { x } } { \partial y } \right] _ { i } = \frac { \partial x _ { i } } { \partial y } \quad \left[ \frac { \partial x } { \partial \mathrm { y } } \right] _ { i } = \frac { \partial x } { \partial y _ { i } } \quad \left[ \frac { \partial \mathrm { x } } { \partial \mathrm { y } } \right] _ { i j } = \frac { \partial x _ { i } } { \partial y _ { j } }$$

The following rules are general and very useful when deriving the differential of
an expression ([19]):

$$\partial \mathrm { A } = 0$$

$\left( A \quad i s \quad a \quad c o n s t a n t \right)$
(33)
$$\partial \left( \alpha \mathrm { X } \right) = \alpha \partial \mathrm { X }$$
$$\partial \left( \mathrm { X } + \mathrm { Y } \right) = \partial \mathrm { X } + \partial \mathrm { Y }$$
$$\partial \left( \mathrm { T r } \left( \mathrm { X } \right) \right) = \mathrm { T r } \left( \partial \mathrm { X } \right)$$
$$\partial \left( \mathrm { X Y } \right) = \left( \partial \mathrm { X } \right) \mathrm { Y } + \mathrm { X } \left( \partial \mathrm { Y } \right)$$
$$\partial \left( \mathrm { X } \circ \mathrm { Y } \right) = \left( \partial \mathrm { X } \right) \circ \mathrm { Y } + \mathrm { X } \circ \left( \partial \mathrm { Y } \right)$$
$$\partial \left( \mathrm { X } \otimes \mathrm { Y } \right) = \left( \partial \mathrm { X } \right) \otimes \mathrm { Y } + \mathrm { X } \otimes \left( \partial \mathrm { Y } \right)$$
$$\partial \left( X ^ { - 1 } \right) = - X ^ { - 1 } \left( \partial X \right) X ^ { - 1 }$$
$\alpha \partial X$
☒ ☒
(34)
☒ ☒ ☒ ☒
(35)
☒ ☒
(36)
☒ ☒ ☒ ☒
(37)
☒ ☒ ☒ ☒ ☒
(38)
☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒
(39)
☒ ☒ ☒ ☒
(40)
(det(X)) = $\mathrm { T r } \left( \mathrm { a d j } \left( \mathrm { X } \right) \partial \mathrm { X } \right.$
☒

☒ ☒

(41)

(42)

$$\partial \left( \det \left( \mathrm { X } \right) \right) = \det \left( \mathrm { X } \right) \mathrm { T r } \left( \mathrm { X } ^ { - 1 } \partial \mathrm { X } \right)$$
$$\partial \left( \ln \left( \det \left( \mathrm { X } \right) \right) \right) _ { \perp } = \mathrm { T r } \left( \mathrm { X } ^ { - 1 } \partial \mathrm { X } \right)$$
$$\partial X ^ { T } = \left( \partial X \right) ^ { T }$$
$$\partial \mathrm { X } ^ { H } = \left( \partial \mathrm { X } \right) ^ { H }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

(43)

(44)

(45)


### 2.1 Derivatives of a Determinant


#### 2.1.1 General form

$$\frac { \partial \det \left( \mathrm { Y } \right) } { \partial x } = \det \left( \mathrm { Y } \right) \mathrm { T r } \left[ \mathrm { Y } ^ { - 1 } \frac { \partial \mathrm { Y } } { \partial x } \right]$$
$$\sum _ { k } \frac { \partial \det \left( \mathrm { X } \right) } { \partial X _ { i k } } X _ { j k } = \delta _ { i j } \det \left( \mathrm { X } \right)$$
$$\frac { \partial ^ { 2 } \det \left( \mathrm { Y } \right) } { \partial x ^ { 2 } } = \det \left( \mathrm { Y } \right) \left[ \mathrm { T r } \left[ \mathrm { Y } ^ { - 1 } \frac { \partial \frac { \partial \mathrm { Y } } { \partial x } } { \partial x } \right] \right.$$
$$+ \mathrm { T r } \left[ \mathrm { Y } ^ { - 1 } \frac { \partial \mathrm { Y } } { \partial x } \right] \mathrm { T r } \left[ \mathrm { Y } ^ { - 1 } \frac { \partial \mathrm { Y } } { \partial x } \right]$$
$$\left. - \mathrm { T r } \left[ \left( \mathrm { Y } ^ { - 1 } \frac { \partial \mathrm { Y } } { \partial x } \right) \left( \mathrm { Y } ^ { - 1 } \frac { \partial \mathrm { Y } } { \partial x } \right) \right] \right]$$ ☒ ☒
(46)
☒ ☒
(47)
☒ ☒ ☒ ☒ ☒
(48)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 8" -->
<!-- PageBreak -->

<!-- PageHeader="2.2 Derivatives of an Inverse" -->
<!-- PageHeader="2 DERIVATIVES" -->


#### 2.1.2 Linear forms

$$\frac { \partial \det \left( \mathrm { X } \right) } { \partial \mathrm { X } } = \det \left( \mathrm { X } \right) \left( \mathrm { X } ^ { - 1 } \right) ^ { T }$$ ☒ ☒ ☒
(49)
☒

$$\sum _ { k } \frac { \partial \det \left( \mathrm { X } \right) } { \partial X _ { i k } } X _ { j k } = \delta _ { i j } \det \left( \mathrm { X } \right)$$ ☒
(50)
☒ ☒ ☒

$$\frac { \partial \det \left( \mathrm { A X B } \right) } { \partial \mathrm { X } } = \det \left( \mathrm { A X B } \right) \left( \mathrm { X } ^ { - 1 } \right) ^ { T } = \det \left( \mathrm { A X B } \right) \left( \mathrm { X } ^ { T } \right) ^ { - 1 }$$ ☒ ☒ ☒
(51)
☒ ☒


#### 2.1.3 Square forms

If $\mathrm { X }$ is square and invertible, then
☒

$$\frac { \partial \det \left( \mathrm { X } ^ { T } \mathrm { A X } \right) } { \partial \mathrm { X } } = 2 \det \left( \mathrm { X } ^ { T } \mathrm { A X } \right) \mathrm { X } ^ { - T }$$ ☒ ☒ ☒ ☒ ☒
(52)
☒

If $\mathrm { x }$ is not square but A is symmetric, then
☒

$$\frac { \partial \det \left( \mathrm { X } ^ { T } \mathrm { A X } \right) } { \partial \mathrm { X } } = 2 \det \left( \mathrm { X } ^ { T } \mathrm { A X } \right) \mathrm { A X } \left( \mathrm { X } ^ { T } \mathrm { A X } \right) ^ { - 1 }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒
(53)
☒

If $\mathrm { X }$ is not square and $\mathrm { A }$ is not symmetric, then
☒

$$\frac { \partial \det \left( \mathrm { X } ^ { T } \mathrm { A X } \right) } { \partial \mathrm { X } } = \det \left( \mathrm { X } ^ { T } \mathrm { A X } \right) \left( \mathrm { A X } \left( \mathrm { X } ^ { T } \mathrm { A X } \right) ^ { - 1 } + \mathrm { A } ^ { T } \mathrm { X } \left( \mathrm { X } ^ { T } \mathrm { A } ^ { T } \mathrm { X } \right) ^ { - 1 } \right)$$ ☒ ☒
(54)
☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒


#### 2.1.4 Other nonlinear forms

Some special cases are (See [9, 7])

$$\frac { \partial \ln \det \left( X ^ { T } X \right) | } { \partial X } = 2 \left( X ^ { + } \right) ^ { T }$$ ☒ ☒ ☒
(55)
☒

$$\frac { \partial \ln \det \left( \mathrm { X } ^ { T } \mathrm { X } \right) } { \partial \mathrm { X } ^ { + } } = - 2 \mathrm { X } ^ { T }$$
$$\frac { \partial \ln | \det \left( \mathrm { X } \right) | } { \partial \mathrm { X } } = \left( \mathrm { X } ^ { - 1 } \right) ^ { T } = \left( \mathrm { X } ^ { T } \right) ^ { - 1 }$$
$$\frac { \partial \det \left( \mathrm { X } ^ { k } \right) } { \partial \mathrm { X } } = k \mathrm { d e t } \left( \mathrm { X } ^ { k } \right) \mathrm { X } ^ { - T }$$ ☒ ☒ ☒
(56)
☒ ☒ ☒ ☒
(57)
☒ ☒ ☒ ☒
(58)
☒


### 2.2 Derivatives of an Inverse

From [27] we have the basic identity

$$\frac { \partial \mathrm { Y } ^ { - 1 } } { \partial x } = - \mathrm { Y } ^ { - 1 } \frac { \partial \mathrm { Y } } { \partial x } \mathrm { Y } ^ { - 1 }$$ ☒ ☒
(59)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 9" -->
<!-- PageBreak -->

<!-- PageHeader="2 DERIVATIVES" -->
<!-- PageHeader="2.3 Derivatives of Eigenvalues" -->

from which it follows

$$\frac { \partial \left( \mathrm { X } ^ { - 1 } \right) _ { k l } } { \partial X _ { i j } } = - \left( \mathrm { X } ^ { - 1 } \right) _ { k i } \left( \mathrm { X } ^ { - 1 } \right) _ { j l }$$
$$\frac { \partial a ^ { T } X ^ { - 1 } b } { \partial X } = - X ^ { - T } a b ^ { T } X ^ { - T }$$
$$\frac { \partial \det \left( \mathrm { X } ^ { - 1 } \right) } { \partial \mathrm { X } } = - \det \left( \mathrm { X } ^ { - 1 } \right) \left( \mathrm { X } ^ { - 1 } \right) ^ { T }$$ ☒ ☒ ☒
(60)
☒ ☒ ☒
(61)
☒ ☒ ☒ ☒
(62)
☒

$$\frac { \partial \mathrm { T r } \left( \mathrm { A X } ^ { - 1 } \mathrm { B } \right) } { \partial \mathrm { X } } = - \left( \mathrm { X } ^ { - 1 } \mathrm { B A X } ^ { - 1 } \right) ^ { T }$$
$$\frac { \partial \mathrm { T r } \left( \left( \mathrm { X } + \mathrm { A } \right) ^ { - 1 } \right) } { \partial \mathrm { X } } = - \left( \left( \mathrm { X } + \mathrm { A } \right) ^ { - 1 } \left( \mathrm { X } + \mathrm { A } \right) ^ { - 1 } \right) ^ { T }$$ ☒ ☒
(63)
☒ ☒
(64)
☒ ☒ ☒ ☒

From [32] we have the following result: Let $\mathrm { A }$ be an $n \times n$ invertible square
matrix, W be the inverse of $\mathrm { A } ,$ and $J \left( \mathrm { A } \right)$ is an $n \times n$ -variate and differentiable
function with respect to $\mathrm { A } ,$ then the partial differentials of $J$ with respect to $\mathrm { A }$
and W satisfy

$$\frac { \partial J } { \partial \mathrm { A } } = - \mathrm { A } ^ { - T } \frac { \partial J } { \partial \mathrm { W } } \mathrm { A } ^ { - T }$$


### 2.3 Derivatives of Eigenvalues

$$\frac { \partial } { \partial \mathrm { X } } \sum \mathrm { e i g } \left( \mathrm { X } \right) = \frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X } \right) = \mathrm { I }$$
$$\frac { \partial } { \partial \mathrm { X } } \prod \mathrm { e i g } \left( \mathrm { X } \right) = \frac { \partial } { \partial \mathrm { X } } \mathrm { d e t } \left( \mathrm { X } \right) = \det \left( \mathrm { X } \right) \mathrm { X } ^ { - T }$$ ☒
(65)
☒ ☒ ☒ ☒
(66)
☒ ☒ ☒ ☒ ☒

If A is real and symmetric, $\lambda _ { i }$ and $V i$ are distinct eigenvalues and eigenvectors
of $\mathrm { A }$ (see (276)) with $\mathrm { v } _ { i } ^ { T } \mathrm { v } _ { i } = 1 ,$ then [33]

$$\partial \lambda _ { i } = \mathrm { v } _ { i } ^ { T } \partial \left( \mathrm { A } \right) \mathrm { v } _ { i }$$
$$\partial \mathrm { v } _ { i } = \left( \lambda _ { i } \mathrm { I } - \mathrm { A } \right) ^ { + } \partial \left( \mathrm { A } \right) \mathrm { v } _ { i }$$
(67)
(68)


### 2.4 Derivatives of Matrices, Vectors and Scalar Forms


#### 2.4.1 First Order

$$\frac { \partial x ^ { T } a } { \partial x } = \frac { \partial a ^ { T } x } { \partial x } = a$$
$$\frac { \partial a ^ { T } X b } { \partial X } = a b ^ { T }$$
$$\frac { \partial a ^ { T } X ^ { T } b } { \partial X } = b a ^ { T }$$
$$\frac { \partial a ^ { T } X a } { \partial X } = \frac { \partial a ^ { T } X ^ { T } a } { \partial X } = a a ^ { T }$$
$$\frac { \partial X } { \partial X _ { i j } } = J ^ { i j }$$
$$\frac { \partial \left( \mathrm { X A } \right) _ { i j } } { \partial X _ { m n } } = \delta _ { i m } \left( \mathrm { A } \right) _ { n j } = \left( \mathrm { J } ^ { m n } \mathrm { A } \right) _ { i j }$$
$$\frac { \partial \left( \mathrm { X } ^ { T } \mathrm { A } \right) _ { i j } } { \partial X _ { m n } } = \delta _ { i n } \left( \mathrm { A } \right) _ { m j } = \left( \mathrm { J } ^ { n m } \mathrm { A } \right) _ { i j }$$
(69)
(70)
☒ ☒
(71)
☒
(72)
☒ ☒ ☒
(73)
☒
(74)
☒
(75)

PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 10

<!-- PageBreak -->

<!-- PageHeader="2.4 Derivatives of Matrices, Vectors and Scalar Forms 2 DERIVATIVES" -->


#### 2.4.2 Second Order

$$\frac { \partial } { \partial X _ { i j } } \sum _ { k l m n } X _ { k l } X _ { m n } = 2 \sum _ { k l } X _ { k l }$$
$$\frac { \partial \mathrm { b } ^ { T } \mathrm { X } ^ { T } \mathrm { X c } } { \partial \mathrm { X } } = \mathrm { X } \left( \mathrm { b c } ^ { T } + \mathrm { c b } ^ { T } \right)$$
$$\frac { \partial \left( \mathrm { B x } + \mathrm { b } \right) ^ { T } \mathrm { C } \left( \mathrm { D x } + \mathrm { d } \right) } { \partial \mathrm { x } } = \mathrm { B } ^ { T } \mathrm { C } \left( \mathrm { D x } + \mathrm { d } \right) + \mathrm { D } ^ { T } \mathrm { C } ^ { T } \left( \mathrm { B x } + \mathrm { b } \right)$$
(76)
☒
(77)
(78)

$$\frac { \partial \left( \mathrm { X } ^ { T } \mathrm { B X } \right) _ { k l } } { \partial X _ { i j } } = \delta _ { l j } \left( \mathrm { X } ^ { T } \mathrm { B } \right) _ { k i } + \delta _ { k j } \left( \mathrm { B X } \right) _ { i l }$$
$$\frac { \partial \left( \mathrm { X } ^ { T } \mathrm { B X } \right) } { \partial X _ { i j } } = \mathrm { X } ^ { T } \mathrm { B J } ^ { i j } + \mathrm { J } ^ { j i } \mathrm { B X } \quad \left( \mathrm { J } ^ { i j } \right) _ { k l } = \delta _ { i k } \delta _ { j l }$$ ☒ ☒ ☒
(79)
☒
(80)
☒

See Sec 9.7 for useful properties of the Single-entry matrix $\mathrm { J } ^ { i j }$

$$\frac { \partial x ^ { T } B x } { \partial x } = \left( B + B ^ { T } \right) x$$
$$\frac { \partial \mathrm { b } ^ { T } \mathrm { X } ^ { T } \mathrm { D X c } } { \partial \mathrm { X } } = \mathrm { D } ^ { T } \mathrm { X b c } ^ { T } + \mathrm { D X c b } ^ { T }$$
$$\frac { \partial } { \partial \mathrm { X } } \left( \mathrm { X b } + \mathrm { c } \right) ^ { T } \mathrm { D } \left( \mathrm { X b } + \mathrm { c } \right) = \left( \mathrm { D } + \mathrm { D } ^ { T } \right) \left( \mathrm { X b } + \mathrm { c } \right) \mathrm { b } ^ { T }$$
(81)
☒
(82)
☒ ☒
(83)
☒ ☒

Assume $\mathrm { W }$ is symmetric, then

$$\frac { \partial } { \partial \mathrm { s } } \left( \mathrm { x } - \mathrm { A s } \right) ^ { T } \mathrm { W } \left( \mathrm { x } - \mathrm { A s } \right) = - 2 \mathrm { A } ^ { T } \mathrm { W } \left( \mathrm { x } - \mathrm { A s } \right)$$ ☒ ☒
(84)

$$\frac { \partial } { \partial x } \left( x - s \right) ^ { T } W \left( x - s \right) = 2 W \left( x - s \right)$$
$$\frac { \partial } { \partial s } \left( x - s \right) ^ { T } W \left( x - s \right) = - 2 W \left( x - s \right)$$ ☒ ☒ ☒
(85)
☒ ☒
(86)

$$\frac { \partial } { \partial x } \left( x - A s \right) ^ { T } W \left( x - A s \right) = 2 W \left( x - A s \right)$$ ☒ ☒ ☒
(87)

$$\frac { \partial } { \partial A } \left( x - A s \right) ^ { T } W \left( x - A s \right) = - 2 W \left( x - A s \right) s ^ { T }$$ ☒ ☒ ☒
(88)

As a case with complex values the following holds

$$\frac { \partial \left( a - x ^ { H } b \right) ^ { 2 } } { \partial x } = - 2 b \left( a - x ^ { H } b \right) ^ { * }$$
(89)

This formula is also known from the LMS algorithm [14]


#### 2.4.3 Higher-order and non-linear

$$\frac { \partial \left( \mathrm { X } ^ { n } \right) _ { k l } } { \partial X _ { i j } } = \sum _ { r = 0 } ^ { n - 1 } \left( \mathrm { X } ^ { r } \mathrm { J } ^ { i j } \mathrm { X } ^ { n - 1 - r } \right) _ { k l }$$ ☒
(90)

For proof of the above, see B.1.3.

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { a } ^ { T } \mathrm { X } ^ { n } \mathrm { b } = \sum _ { r = 0 } ^ { n - 1 } \left( \mathrm { X } ^ { r } \right) ^ { T } \mathrm { a b } ^ { T } \left( \mathrm { X } ^ { n - 1 - r } \right) ^ { T }$$ ☒
(91)

PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 11

<!-- PageBreak -->

<!-- PageHeader="2.5 Derivatives of Traces" -->
<!-- PageHeader="2 DERIVATIVES" -->

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { a } ^ { T } \left( \mathrm { X } ^ { n } \right) ^ { T } \mathrm { X } ^ { n } \mathrm { b } = \sum _ { r = 0 } ^ { n - 1 } \left[ \mathrm { X } ^ { n - 1 - r } \mathrm { a b } ^ { T } \left( \mathrm { X } ^ { n } \right) ^ { T } \mathrm { X } ^ { r } \right.$$
$$\left. + \left( \mathrm { X } ^ { r } \right) ^ { T } \mathrm { X } ^ { n } \mathrm { a b } ^ { T } \left( \mathrm { X } ^ { n - 1 - r } \right) ^ { T } \right]$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

See B.1.3 for a proof.
Assume $\mathrm { S }$ and $\mathrm { r }$ are functions of x, i.e. $\mathrm { s } = \mathrm { s } \left( \mathrm { x } \right) ,$ $r = r \left( x \right) ,$ and that $\mathrm { A }$ is a
☒ ☒
(92)
☒

constant, then

$$\frac { \partial } { \partial x } s ^ { T } A r = \left[ \frac { \partial s } { \partial x } \right] ^ { T } A r + \left[ \frac { \partial r } { \partial x } \right] ^ { T } A ^ { T } s$$
$$\frac { \partial } { \partial \mathrm { x } } \frac { \left( \mathrm { A x } \right) ^ { T } \left( \mathrm { A x } \right) } { \left( \mathrm { B x } \right) ^ { T } \left( \mathrm { B x } \right) } = \frac { \partial \mathrm { x } ^ { T } \mathrm { A } ^ { T } \mathrm { A x } } { \partial \mathrm { x } \mathrm { x } ^ { T } \mathrm { B } ^ { T } \mathrm { B x } }$$
(93)
☒
(94)
☒ ☒ ☒

$$= 2 \frac { \mathrm { A } ^ { T } \mathrm { A x } } { \mathrm { x } ^ { T } \mathrm { B B x } } - 2 \frac { \mathrm { x } ^ { T } \mathrm { A } ^ { T } \mathrm { A x B } ^ { T } \mathrm { B x } } { \left( \mathrm { x } ^ { T } \mathrm { B } ^ { T } \mathrm { B x } \right) ^ { 2 } }$$ ☒
(95)


#### 2.4.4 Gradient and Hessian

Using the above we have for the gradient and the Hessian

$$f = x ^ { T } A x + b ^ { T } x$$ ☒
(96)

$$\nabla _ { \mathrm { x } } f = \frac { \partial f } { \partial \mathrm { x } } = \left( \mathrm { A } + \mathrm { A } ^ { T } \right) \mathrm { x } + \mathrm { b }$$
$$\frac { \partial ^ { 2 } f } { \partial x \partial x ^ { T } } = A + A ^ { T }$$ ☒
(97)
(98)


### 2.5 Derivatives of Traces

Assume $F \left( \mathrm { X } \right)$ to be a differentiable function of each of the elements of $X .$ It
☒

☒
then holds that

$$\frac { \partial \mathrm { T r } \left( F \left( \mathrm { X } \right) \right) } { \partial \mathrm { x } \tau } = f \left( \mathrm { X } \right) ^ { T }$$ ☒
0x
☒ ☒

where $f \left( \cdot \right)$ is the scalar derivative of $F \left( \cdot \right) .$
☒ ☒


#### 2.5.1 First Order

$$\frac { \partial } { \partial X } \mathrm { T r } \left( X \right) = I$$
$$\frac { \partial } { \partial X } T r \left( X A \right) = A ^ { T }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { A X B } \right) = \mathrm { A } ^ { T } \mathrm { B } ^ { T }$$
$$\frac { \partial } { \partial X } \mathrm { T r } \left( A X ^ { T } B \right) = B A$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X } ^ { T } \mathrm { A } \right) = \mathrm { A }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { A X } ^ { T } \right) = \mathrm { A }$$
$$\frac { \partial } { \partial X } \mathrm { T r } \left( A \otimes X \right) = \mathrm { T r } \left( A \right) I$$ ☒ ☒
(99)
☒
(100)
☒
(101)
☒ ☒
(102)
☒ ☒
(103)
☒ ☒
(104)
☒
(105)
☒ ☒

PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 12

<!-- PageBreak -->

<!-- PageHeader="2.5 Derivatives of Traces" -->
<!-- PageHeader="2 DERIVATIVES" -->


#### 2.5.2 Second Order

$$\frac { \partial } { \partial X } T r \left( X ^ { 2 } \right) = 2 X ^ { T }$$
(106)
☒ ☒ ☒

$$\frac { \partial } { \partial X } \mathrm { T r } \left( X ^ { 2 } B \right) = \left( X B + B X \right) ^ { T }$$
$$\frac { \partial } { \partial X } \mathrm { T r } \left( X ^ { T } B X \right) = B X + B ^ { T } X$$ ☒ ☒ ☒ ☒
(107)
☒ ☒ ☒ ☒
(108)

$$\frac { \partial } { \partial X } \mathrm { T r } \left( B X X ^ { T } \right) = B X + B ^ { T } X$$ ☒ ☒ ☒ ☒ ☒
(109)

$$\frac { \partial } { \partial X } \mathrm { T r } \left( X X ^ { T } B \right) = B X + B ^ { T } X$$ ☒ ☒ ☒ ☒
(110)
☒

$$\frac { \partial } { \partial X } \mathrm { T r } \left( X B X ^ { T } \right) = X B ^ { T } + X B$$ ☒ ☒
(111)
☒

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { B X } ^ { T } \mathrm { X } \right) = \mathrm { X B } ^ { T } + \mathrm { X B }$$ ☒ ☒
(112)
☒

$$\frac { \partial } { \partial X } \mathrm { T r } \left( X ^ { T } X B \right) = X B ^ { T } + X B$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { A X B X } \right) = \mathrm { A } ^ { T } \mathrm { X } ^ { T } \mathrm { B } ^ { T } + \mathrm { B } ^ { T } \mathrm { X } ^ { T } \mathrm { A } ^ { T }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X } ^ { T } \mathrm { X } \right) = \frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X X } ^ { T } \right) = 2 \mathrm { X }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { B } ^ { T } \mathrm { X } ^ { T } \mathrm { C X B } \right) = \mathrm { C } ^ { T } \mathrm { X B B } ^ { T } + \mathrm { C X B B } ^ { T }$$
$$\frac { \partial } { \partial X } \mathrm { T r } \left[ X ^ { T } B X C \right] = B X C + B ^ { T } X C ^ { T }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { A X B X } ^ { T } \mathrm { C } \right) = \mathrm { A } ^ { T } \mathrm { C } ^ { T } \mathrm { X B } ^ { T } + \mathrm { C A X B }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left[ \left( \mathrm { A X B } + \mathrm { C } \right) \left( \mathrm { A X B } + \mathrm { C } \right) ^ { T } \right] = 2 \mathrm { A } ^ { T } \left( \mathrm { A X B } + \mathrm { C } \right) \mathrm { B } ^ { T }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X } \otimes \mathrm { X } \right) = \frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X } \right) \mathrm { T r } \left( \mathrm { X } \right) = 2 \mathrm { T r } \left( \mathrm { X } \right) \mathrm { I } \left( 1 2 0 \right)$$ ☒ ☒ ☒
(113)
☒ ☒ ☒
(114)
☒
(115)
☒ ☒ ☒ ☒ ☒ ☒ ☒
(116)
☒ ☒
(117)
☒
(118)
☒ ☒ ☒ ☒ ☒ ☒
(119)
☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

See [7].


#### 2.5.3 Higher Order

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X } ^ { k } \right) = k \left( \mathrm { X } ^ { k - 1 } \right) ^ { T }$$ ☒ ☒
(121)
☒

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { A X } ^ { k } \right) = \sum _ { r = 0 } ^ { k - 1 } \left( \mathrm { X } ^ { r } \mathrm { A X } ^ { k - r - 1 } \right) ^ { T }$$
$$\frac { \partial } { \partial \mathrm { x } } \mathrm { T r } \left[ \mathrm { B } ^ { T } \mathrm { X } ^ { T } \mathrm { C X X } ^ { T } \mathrm { C X B } \right] = \mathrm { C X X X } ^ { T } \mathrm { C X B B } ^ { T }$$
$$+ \mathrm { C } ^ { T } \mathrm { X B B } ^ { T } \mathrm { X } ^ { T } \mathrm { C } ^ { T } \mathrm { X }$$
$$+ \mathrm { C X B B } ^ { T } \mathrm { X } ^ { T } \mathrm { C X }$$ ☒ ☒
(122)
☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

$$+ \mathrm { C } ^ { T } \mathrm { X X } ^ { T } \mathrm { C } ^ { T } \mathrm { X B B } ^ { T }$$ ☒ ☒
(123)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 13" -->
<!-- PageBreak -->

<!-- PageHeader="2 DERIVATIVES" -->
<!-- PageHeader="2.6 Derivatives of vector norms" -->


#### 2.5.4 Other

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { A X } ^ { - 1 } \mathrm { B } \right) = - \left( \mathrm { X } ^ { - 1 } \mathrm { B A X } ^ { - 1 } \right) ^ { T } = - \mathrm { X } ^ { - T } \mathrm { A } ^ { T } \mathrm { B } ^ { T } \mathrm { X } ^ { - T }$$ ☒ ☒ ☒
(124)
☒ ☒ ☒

Assume $\mathrm { B }$ and $\mathrm { C }$ to be symmetric, then

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left[ \left( \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 } \mathrm { A } \right] = - \left( \mathrm { C X } \left( \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 } \right) \left( \mathrm { A } + \mathrm { A } ^ { T } \right) \left( \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 } \left( 1 2 5 \right)$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left[ \left( \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 } \left( \mathrm { X } ^ { T } \mathrm { B X } \right) \right] = - 2 \mathrm { C } \mathrm { X } \left( \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 } \mathrm { X } ^ { T } \mathrm { B X } \left( \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 }$$
$$\frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left[ \left( \mathrm { A } + \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 } \left( \mathrm { X } ^ { T } \mathrm { B X } \right) \right] = - 2 \mathrm { C } \mathrm { X } \left( \mathrm { A } + \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 } \mathrm { X } ^ { T } \mathrm { B X } \left( \mathrm { A } + \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 }$$
$$+ 2 \mathrm { B } \mathrm { X } \left( \mathrm { A } + \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒
$+ 2 \mathrm { B } \mathrm { X } \left( \mathrm { X } ^ { T } \mathrm { C X } \right) ^ { - 1 }$
☒ ☒ ☒
(126)
☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒
(127)

$$\frac { \partial \mathrm { T r } \left( \sin \left( \mathrm { X } \right) \right) } { \partial \mathrm { X } } = \cos \left( \mathrm { X } \right) ^ { T }$$
$$S e e \left[ 7 \right] .$$ ☒ ☒
(128)
☒


### 2.6 Derivatives of vector norms


#### 2.6.1 Two-norm

$$\frac { \partial } { \partial x } | | x - a | | _ { 2 } = \frac { x - a } { | | x - a | | _ { 2 } }$$
$$\frac { \partial } { \partial x } \frac { x - a } { | | x - a | | _ { 2 } } = \frac { I } { | | x - a | | _ { 2 } } - \frac { \left( x - a \right) \left( x - a \right) ^ { T } } { | | x - a | | _ { 2 } ^ { 3 } }$$
$$\frac { \partial | | x | | _ { 2 } ^ { 2 } } { \partial x } = \frac { \partial | | x ^ { T } x | | _ { 2 } } { \partial x } = 2 x$$
(129)
(130)
(131)


### 2.7 Derivatives of matrix norms

For more on matrix norms, see Sec. 10.4.


#### 2.7.1 Frobenius norm

$$\frac { \partial } { \partial \mathrm { X } } | | \mathrm { X } | | _ { \mathrm { F } } ^ { 2 } = \frac { \partial } { \partial \mathrm { X } } \mathrm { T r } \left( \mathrm { X X } ^ { H } \right) = 2 \mathrm { X }$$ ☒ ☒
(132)
☒ ☒

See (248). Note that this is also a special case of the result in equation 119.


### 2.8 Derivatives of Structured Matrices

Assume that the matrix A has some structure, i.e. symmetric, toeplitz, etc.
In that case the derivatives of the previous section does not apply in general.
Instead, consider the following general rule for differentiating a scalar function
$f \left( \mathrm { A } \right)$

$$\frac { d f } { d A _ { i j } } = \sum _ { k l } \frac { \partial f } { \partial A _ { k l } } \frac { \partial A _ { k l } } { \partial A _ { i j } } = \mathrm { T r } \left[ \left[ \frac { \partial f } { \partial \mathrm { A } } \right] ^ { T } \frac { \partial \mathrm { A } } { \partial A _ { i j } } \right]$$
(133)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 14" -->
<!-- PageBreak -->

<!-- PageHeader="2 DERIVATIVES" -->
<!-- PageHeader="2.8 Derivatives of Structured Matrices" -->

The matrix differentiated with respect to itself is in this document referred to
as the structure matrix of $\mathrm { A }$ and is defined simply by

$$\frac { \partial A } { \partial A _ { i j } } = S ^ { i j }$$
(134)

If A has no special structure we have simply $\mathrm { S } ^ { i j } = \mathrm { J } ^ { i j } ,$ that is, the structure
matrix is simply the single-entry matrix. Many structures have a representation
in singleentry matrices, see Sec. 9.7.6 for more examples of structure matrices.


#### 2.8.1 The Chain Rule

Sometimes the objective is to find the derivative of a matrix which is a function
of another matrix. Let $\mathrm { U } = f \left( \mathrm { X } \right) ,$ the goal is to find the derivative of the
☒
function $\mathrm { g } \left( \mathrm { U } \right)$ with respect to $\mathrm { X } :$
☒ ☒

$$\frac { \partial g \left( \mathrm { U } \right) } { \partial \mathrm { X } } = \frac { \partial g \left( f \left( \mathrm { X } \right) \right) } { \partial \mathrm { X } }$$ ☒
(135)
☒ ☒

Then the Chain Rule can then be written the following way:

$$\frac { \partial g \left( \mathrm { U } \right) } { \partial \mathrm { X } } = \frac { \partial g \left( \mathrm { U } \right) } { \partial x _ { i j } } = \sum _ { k = 1 } ^ { M } \sum _ { l = 1 } ^ { N } \frac { \partial g \left( \mathrm { U } \right) } { \partial u _ { k l } } \frac { \partial u _ { k l } } { \partial x _ { i j } }$$
(136)
☒

Using matrix notation, this can be written as:

$$\frac { \partial g \left( \mathrm { U } \right) } { \partial X _ { i j } } = \mathrm { T r } \left[ \left( \frac { \partial g \left( \mathrm { U } \right) } { \partial \mathrm { U } } \right) ^ { T } \frac { \partial \mathrm { U } } { \partial X _ { i j } } \right] .$$
(137)


#### 2.8.2 Symmetric

If $\mathrm { A }$ is symmetric, then $\mathrm { S } ^ { i j } = \mathrm { J } ^ { i j } + \mathrm { J } ^ { j i } - \mathrm { J } ^ { i j } \mathrm { J } ^ { i j }$ and therefore

$$\frac { d f } { d A } = \left[ \frac { \partial f } { \partial A } \right] + \left[ \frac { \partial f } { \partial A } \right] ^ { T } - \mathrm { d i a g } \left[ \frac { \partial f } { \partial A } \right]$$
(138)

That is, e.g., ([5]):

$$\frac { \partial \mathrm { T r } \left( \mathrm { A X } \right) } { \partial \mathrm { X } } = \mathrm { A } + \mathrm { A } ^ { T } - \left( \mathrm { A } \circ \mathrm { I } \right) , \sec \left( 1 4 2 \right)$$
$$\frac { \partial \det \left( X \right) } { \partial X } = \det \left( X \right) \left( 2 X ^ { - 1 } - \left( X ^ { - 1 } \circ I \right) \right)$$
$$\frac { \partial \ln \det \left( \mathrm { X } \right) } { \partial \mathrm { X } } = 2 \mathrm { X } ^ { - 1 } - \left( \mathrm { X } ^ { - 1 } \circ \mathrm { I } \right)$$ ☒
(139)
☒ ☒ ☒ ☒ ☒
(140)
☒ ☒ ☒ ☒
(141)
☒


#### 2.8.3 Diagonal

If $\mathrm { X }$ is diagonal, then ([19]):
☒

$$\frac { \partial \mathrm { T r } \left( \mathrm { A X } \right) } { \partial \mathrm { X } } = \mathrm { A } \circ \mathrm { I }$$ ☒
(142)
☒

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 15" -->
<!-- PageBreak -->

<!-- PageHeader="2.8 Derivatives of Structured Matrices" -->
<!-- PageHeader="2 DERIVATIVES" -->


#### 2.8.4 Toeplitz

Like symmetric matrices and diagonal matrices also Toeplitz matrices has a
special structure which should be taken into account when the derivative with
respect to a matrix with Toeplitz structure.

$$\frac { \partial \mathrm { T r } \left( \mathrm { A T } \right) } { \partial \mathrm { T } }$$
$$= \frac { \partial \mathrm { T r } \left( \mathrm { T A } \right) } { \partial \mathrm { T } }$$
(143)

Tr(A)
Tr([AT]n1)
Tr(A)

Tr([AT ]1n))

=

Tr([AT]1n]2,n-1)

Tr([AT]1n]n-1,2)

.

.

.

.

.

.

.

.

A1n

·

·

·

Tr([AT]1n12,2-1)

Tr([AT]in))

$\mathrm { T r } \left( \left[ \mathrm { A } ^ { T } \right] _ { n 1 } \right.$
$\mathrm { T r } \left( \mathrm { A } \right)$
$A _ { n 1 }$
.
.

= $\alpha \left( \mathrm { A } \right)$

As it can be seen, the derivative $\alpha \left( \mathrm { A } \right)$ also has a Toeplitz structure. Each value
in the diagonal is the sum of all the diagonal valued in $\mathrm { A } ,$ the values in the
diagonals next to the main diagonal equal the sum of the diagonal next to the
main diagonal in $\mathrm { A } ^ { T } .$ This result is only valid for the unconstrained Toeplitz
matrix. If the Toeplitz matrix also is symmetric, the same derivative yields

$$\frac { \partial \mathrm { T r } \left( \mathrm { A T } \right) } { \partial \mathrm { T } } = \frac { \partial \mathrm { T r } \left( \mathrm { T A } \right) } { \partial \mathrm { T } } = \alpha \left( \mathrm { A } \right) + \alpha \left( \mathrm { A } \right) ^ { T } - \alpha \left( \mathrm { A } \right) \circ \mathrm { I }$$
(144)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 16" -->

Tr[AT]1nln-1,2)

·

·

·

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

<!-- PageBreak -->

<!-- PageHeader="3 INVERSES" -->


## 3 Inverses


### 3.1 Basic


#### 3.1.1 Definition

The inverse $\mathrm { A } ^ { - 1 }$ of a matrix $\mathrm { A } \in \mathbb{C} ^ { n \times n }$ is defined such that

$$\mathrm { A A } ^ { - 1 } = \mathrm { A } ^ { - 1 } \mathrm { A } = \mathrm { I } . ,$$
(145)

where I is the $n \times n$ identity matrix. If $\mathrm { A } ^ { - 1 }$ exists, $\mathrm { A }$ is said to be nonsingular.
Otherwise, A is said to be singular (see e.g. [12]).


#### 3.1.2 Cofactors and Adjoint

The submatrix of a matrix $\mathrm { A } ,$ denoted by $\left[ \mathrm { A } \right] _ { i j }$ is a $\left( n - 1 \right) \times \left( n - 1 \right)$ matrix
obtained by deleting the ith row and the jth column of $\mathrm { A } .$ The $\left( i , j \right)$ cofactor
of a matrix is defined as

$$\mathrm { c o f } \left( \mathrm { A } , i , j \right) = \left( - 1 \right) ^ { i + j } \det \left( \left[ \mathrm { A } \right] _ { i j } \right) ,$$
(146)

The matrix of cofactors can be created from the cofactors

cof(A) =
cof(A,1,1)
.
cof(A, n, 1)

. . .
cof(A,i,j)
cof(A, 1,n)
cof(A, n, n)
...

.
(147)

The adjoint matrix is the transpose of the cofactor matrix

$$\mathrm { a d j } \left( \mathrm { A } \right) = \left( \mathrm { c o f } \left( \mathrm { A } \right) \right) ^ { T } ,$$
(148)


#### 3.1.3 Determinant

The determinant of a matrix $\mathrm { A } \in \mathbb{C} ^ { n \times n }$ is defined as (see [12])

$$\det \left( \mathrm { A } \right) = \sum _ { j = 1 } ^ { n } \left( - 1 \right) ^ { j + 1 } A _ { 1 j } \det \left( \left[ \mathrm { A } \right] _ { 1 j } \right)$$
(149)

$$= \sum _ { j = 1 } ^ { n } A _ { 1 j } \mathrm { c o f } \left( \mathrm { A } , 1 , j \right) .$$
(150)


#### 3.1.4 Construction

The inverse matrix can be $c o n s t r u c t e d ,$ using the adjoint matrix, by

$$A ^ { - 1 } = \frac { 1 } { \det \left( A \right) } \cdot \mathrm { a d j } \left( A \right)$$
(151)

For the case of $2 \times 2$ matrices, see section 1.3.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 17" -->
<!-- PageBreak -->

<!-- PageHeader="3 INVERSES" -->
<!-- PageHeader="3.2 Exact Relations" -->


#### 3.1.5 Condition number

The condition number of a matrix $c \left( \mathrm { A } \right)$ is the ratio between the largest and the
smallest singular value of a matrix (see Section 5.3 on singular values),

$$c \left( \mathrm { A } \right) = \frac { d _ { + } } { d _ { - } }$$
(152)

The condition number can be used to measure how singular a matrix is. If the
condition number is large, it indicates that the matrix is nearly singular. The
condition number can also be estimated from the matrix norms. Here

$$c \left( \mathrm { A } \right) = \| \mathrm { A } \| \cdot \| \mathrm { A } ^ { - 1 } \| ,$$
(153)

where $\| \cdot \|$ is a norm such as e.g the 1-norm, the 2-norm, the oo-norm or $t h e$
Frobenius norm (see Sec 10.4 for more on matrix norms).

The 2-norm of $\mathrm { A }$ equals $\sqrt { \left( \max \left( \mathrm { e i g } \left( \mathrm { A } ^ { H } \mathrm { A } \right) \right) \right) }$ [12, p.57]. For a symmetric
☒
matrix, this reduces to $| | \mathrm { A } | | _ { 2 } = \max \left( | \mathrm { e i g } \left( \mathrm { A } \right) | \right)$ [12, p.394]. If the matrix is
symmetric and positive definite, $| | \mathrm { A } | | _ { 2 } = \max \left( \mathrm { e i g } \left( \mathrm { A } \right) \right) .$ The condition number
based on the 2-norm thus reduces to

$$\| \mathrm { A } \| _ { 2 } \| \mathrm { A } ^ { - 1 } \| _ { 2 } = \max \left( \mathrm { e i g } \left( \mathrm { A } \right) \right) \max \left( \mathrm { e i g } \left( \mathrm { A } ^ { - 1 } \right) \right) = \frac { \max \left( \mathrm { e i g } \left( \mathrm { A } \right) \right) } { \min \left( \mathrm { e i g } \left( \mathrm { A } \right) \right) } .$$
(154)


### 3.2 Exact Relations


#### 3.2.1 Basic

$$\left( \mathrm { A B } \right) ^ { - 1 } = \mathrm { B } ^ { - 1 } \mathrm { A } ^ { - 1 }$$
(155)


#### 3.2.2 The Woodbury identity

The Woodbury identity comes in many variants. The latter of the two can be
found in [12]

$$\left( \mathrm { A } + \mathrm { C B C } ^ { T } \right) ^ { - 1 } = \mathrm { A } ^ { - 1 } - \mathrm { A } ^ { - 1 } \mathrm { C } \left( \mathrm { B } ^ { - 1 } + \mathrm { C } ^ { T } \mathrm { A } ^ { - 1 } \mathrm { C } \right) ^ { - 1 } \mathrm { C } ^ { T } \mathrm { A } ^ { - 1 }$$
$$\left( \mathrm { A } + \mathrm { U B V } \right) ^ { - 1 } = \mathrm { A } ^ { - 1 } - \mathrm { A } ^ { - 1 } \mathrm { U } \left( \mathrm { B } ^ { - 1 } + \mathrm { V A } ^ { - 1 } \mathrm { U } \right) ^ { - 1 } \mathrm { V A } ^ { - 1 }$$
(156)
(157)

If $P ,$ $\mathrm { R }$ are positive definite, then (see [30])

$$\left( \mathrm { P } ^ { - 1 } + \mathrm { B } ^ { T } \mathrm { R } ^ { - 1 } \mathrm { B } \right) ^ { - 1 } \mathrm { B } ^ { T } \mathrm { R } ^ { - 1 } = \mathrm { P B } ^ { T } \left( \mathrm { B P B } ^ { T } + \mathrm { R } \right) ^ { - 1 }$$
(158)


#### 3.2.3 The Kailath Variant

$$\left( \mathrm { A } + \mathrm { B C } \right) ^ { - 1 } = \mathrm { A } ^ { - 1 } - \mathrm { A } ^ { - 1 } \mathrm { B } \left( \mathrm { I } + \mathrm { C A } ^ { - 1 } \mathrm { B } \right) ^ { - 1 } \mathrm { C A } ^ { - 1 }$$
(159)

See [4, page 153].


#### 3.2.4 Sherman-Morrison

$$\left( \mathrm { A } + \mathrm { b c } ^ { T } \right) ^ { - 1 } = \mathrm { A } ^ { - 1 } - \frac { \mathrm { A } ^ { - 1 } \mathrm { b c } ^ { T } \mathrm { A } ^ { - 1 } } { 1 + \mathrm { c } ^ { T } \mathrm { A } ^ { - 1 } \mathrm { b } }$$
(160)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 18" -->
<!-- PageBreak -->

<!-- PageHeader="3 INVERSES" -->
<!-- PageHeader="3.2 Exact Relations" -->


#### 3.2.5 The Searle Set of Identities

The following set of identities, can be found in [25, page 151],

$$\left( \mathrm { I } + \mathrm { A } ^ { - 1 } \right) ^ { - 1 } = \mathrm { A } \left( \mathrm { A } + \mathrm { I } \right) ^ { - 1 }$$
$$\left( \mathrm { A } + \mathrm { B B } ^ { T } \right) ^ { - 1 } \mathrm { B } = \mathrm { A } ^ { - 1 } \mathrm { B } \left( \mathrm { I } + \mathrm { B } ^ { T } \mathrm { A } ^ { - 1 } \mathrm { B } \right) ^ { - 1 }$$
$$\left( A ^ { - 1 } + B ^ { - 1 } \right) ^ { - 1 } = A \left( A + B \right) ^ { - 1 } B = B \left( A + B \right) ^ { - 1 } A$$
$$\mathrm { A } - \mathrm { A } \left( \mathrm { A } + \mathrm { B } \right) ^ { - 1 } \mathrm { A } \quad = \quad \mathrm { B } - \mathrm { B } \left( \mathrm { A } + \mathrm { B } \right) ^ { - 1 } \mathrm { B }$$
(161)
(162)
(163)
$\left( 1 6 4 \right)$

$$\mathrm { A } ^ { - 1 } + \mathrm { B } ^ { - 1 } = \mathrm { A } ^ { - 1 } \left( \mathrm { A } + \mathrm { B } \right) \mathrm { B } ^ { - 1 }$$
(165)

$$\left( I + A B \right) ^ { - 1 } = I - A \left( I + B A \right) ^ { - 1 } B$$
$$\left( I + A B \right) ^ { - 1 } A = A \left( I + B A \right) ^ { - 1 }$$
(166)
(167)


#### 3.2.6 Rank-1 update of inverse of inner product

Denote $A = \left( X ^ { T } X \right) ^ { - 1 }$ and that $\mathrm { X }$ is extended to include a new column vector
in the end $\widetilde { \mathrm { X } } = \left[ \mathrm { X } \quad \mathrm { v } \right] .$ Then [34]
☒ ☒ ☒ ☒ ☒

☒
(XTX)-1
☒

=
A +

[

AXT VVTXAT
VTV-VTXAXTV

VTV-VTXAXTv
-AXTv

1

-vTXAT
VTV-VTXAXTV

VTV-VTXAXTV


#### 3.2.7 Rank-1 update of Moore-Penrose Inverse

The following is a rank-1 update for the Moore-Penrose pseudo-inverse of real
valued matrices and proof can be found in [18]. The matrix G is defined below:

$$\left( \mathrm { A } + \mathrm { c d } ^ { T } \right) ^ { + } = \mathrm { A } ^ { + } + \mathrm { G }$$
(168)

Using the the notation

$$\beta = 1 + d ^ { T } A ^ { + } c$$
$$\mathrm { v } = \mathrm { A } ^ { + } \mathrm { c }$$
(169)
(170)

$$\mathrm { n } = \left( \mathrm { A } ^ { + } \right) ^ { T } \mathrm { d }$$
$$\mathrm { w } = \left( \mathrm { I } - \mathrm { A A } ^ { + } \right) \mathrm { c }$$
$$\mathrm { m } = \left( \mathrm { I } - \mathrm { A } ^ { + } \mathrm { A } \right) ^ { T } \mathrm { d }$$
(171)
(172)
(173)

the solution is given as six different cases, depending on the entities $| | \mathrm { w } | | ,$
$| | \mathrm { m } | | ,$ and $\beta .$ Please note, that for any (column) vector $\mathrm { v }$ it holds that $\mathrm { v } ^ { + } =$
$\mathrm { v } ^ { T } \left( \mathrm { v } ^ { T } \mathrm { v } \right) ^ { - 1 } = \frac { \mathrm { v } ^ { T } } { | | \mathrm { v } | | ^ { 2 } } .$ The solution is:

Case 1 of 6: $\mathrm { I f } | | \mathrm { w } | | \neq 0$ and $| | \mathrm { m } | | \neq 0 .$ Then

$$\mathrm { G } = - \mathrm { v w } ^ { + } - \left( \mathrm { m } ^ { + } \right) ^ { T } \mathrm { n } ^ { T } + \beta \left( \mathrm { m } ^ { + } \right) ^ { T } \mathrm { w } ^ { + }$$
$$= - \frac { 1 } { | | \mathrm { w } | | ^ { 2 } } \mathrm { v w } ^ { T } - \frac { 1 } { | | \mathrm { m } | | ^ { 2 } } \mathrm { m n } ^ { T } + \frac { \beta } { | | \mathrm { m } | | ^ { 2 } | | \mathrm { w } | | ^ { 2 } } \mathrm { m w } ^ { T }$$
(174)
(175)

Case 2 of 6: If $| | \mathrm { w } | | = 0$ and $| | \mathrm { m } | | \neq 0$ and $\beta = 0 .$ Then

$$\mathrm { G } = - \mathrm { v v } ^ { + } \mathrm { A } ^ { + } - \left( \mathrm { m } ^ { + } \right) ^ { T } \mathrm { n } ^ { T }$$
$$= - \frac { 1 } { | | \mathrm { v } | | ^ { 2 } } \mathrm { v v } ^ { T } \mathrm { A } ^ { + } - \frac { 1 } { | | \mathrm { m } | | ^ { 2 } } \mathrm { m n } ^ { T }$$
(176)
(177)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 19" -->
<!-- PageBreak -->

<!-- PageHeader="3 INVERSES" -->
<!-- PageHeader="3.3 Implication on Inverses" -->

Case 3 of 6: If $| | \mathrm { w } | | = 0 \mathrm { a n d } \beta \neq 0 .$ Then

$$\mathrm { G } = \frac { 1 } { \beta } \mathrm { m v } ^ { T } \mathrm { A } ^ { + } - \frac { \beta } { | | \mathrm { v } | | ^ { 2 } | | \mathrm { m } | | ^ { 2 } + | \beta | ^ { 2 } } \left( \frac { | | \mathrm { v } | | ^ { 2 } } { \beta } \mathrm { m } + \mathrm { v } \right) \left( \frac { | | \mathrm { m } | | ^ { 2 } } { \beta } \left( \mathrm { A } ^ { + } \right) ^ { T } \mathrm { v } + \mathrm { n } \right) ^ { T }$$
(178)

Case 4 of 6: If $| | \mathrm { w } | | \neq 0$ and $| | \mathrm { m } | | = 0$ and $\beta = 0 .$ Then

$$\mathrm { G } = - \mathrm { A } ^ { + } \mathrm { n n } ^ { + } - \mathrm { v w } ^ { + }$$
$$= - \frac { 1 } { | | \mathrm { n } | | ^ { 2 } } \mathrm { A } ^ { + } \mathrm { n n } ^ { T } - \frac { 1 } { | | \mathrm { w } | | ^ { 2 } } \mathrm { v w } ^ { T }$$
(179)
(180)

$5 \text { of } 6 : \text { If } | | m | | = 0 \text { and } \beta \neq 0 .$ Then

$$\mathrm { G } = \frac { 1 } { \beta } \mathrm { A } ^ { + } \mathrm { n w } ^ { T } - \frac { \beta } { | | \mathrm { n } | | ^ { 2 } | | \mathrm { w } | | ^ { 2 } + | \beta | ^ { 2 } } \left( \frac { | | \mathrm { w } | | ^ { 2 } } { \beta } \mathrm { A } ^ { + } \mathrm { n } + \mathrm { v } \right) \left( \frac { | | \mathrm { n } | | ^ { 2 } } { \beta } \mathrm { w } + \mathrm { n } \right) ^ { T }$$
(181)

$6 \text { of } 6 : \text { If } | | w | | = 0 \text { and } | | m | | = 0 \text { and } \beta = 0 .$

$$\mathrm { G } = - \mathrm { v v } ^ { + } \mathrm { A } ^ { + } - \mathrm { A } ^ { + } \mathrm { n n } ^ { + } + \mathrm { v } ^ { + } \mathrm { A } ^ { + } \mathrm { n v n } ^ { + }$$
(182)

$$= - \frac { 1 } { | | \mathrm { v } | | ^ { 2 } } \mathrm { v v } ^ { T } \mathrm { A } ^ { + } - \frac { 1 } { | | \mathrm { n } | | ^ { 2 } } \mathrm { A } ^ { + } \mathrm { n n } ^ { T } + \frac { \mathrm { v } ^ { T } \mathrm { A } ^ { + } \mathrm { n } } { | | \mathrm { v } | | ^ { 2 } | | \mathrm { n } | | ^ { 2 } } \mathrm { v n } ^ { T }$$
(183)


### 3.3 Implication on Inverses

If
$\left( \mathrm { A } + \mathrm { B } \right) ^ { - 1 } = \mathrm { A } ^ { - 1 } + \mathrm { B } ^ { - 1 }$
then
AB-1A = BA-1B
(184)

See [25].


#### 3.3.1 A PosDef identity

Assume P, $R$ to be positive definite and invertible, then

$$\left( \mathrm { P } ^ { - 1 } + \mathrm { B } ^ { T } \mathrm { R } ^ { - 1 } \mathrm { B } \right) ^ { - 1 } \mathrm { B } ^ { T } \mathrm { R } ^ { - 1 } = \mathrm { P B } ^ { T } \left( \mathrm { B P B } ^ { T } + \mathrm { R } \right) ^ { - 1 }$$
(185)

See [30].


### 3.4 Approximations

The following identity is known as the Neuman series of a matrix, which holds
when $| \lambda _ { i } | < 1$ for all eigenvalues $\lambda _ { i }$

$$\left( \mathrm { I } - \mathrm { A } \right) ^ { - 1 } = \sum _ { n = 0 } ^ { \infty } \mathrm { A } ^ { n }$$
(186)

which is equivalent to

$$\left( \mathrm { I } + \mathrm { A } \right) ^ { - 1 } = \sum _ { n = 0 } ^ { \infty } \left( - 1 \right) ^ { n } \mathrm { A } ^ { n }$$
(187)

When $| \lambda _ { i } | < 1$ for all eigenvalues $\lambda _ { i } ,$ it holds that $\mathrm { A } \rightarrow 0$ for $n \rightarrow \infty ,$ and the
following approximations holds

$$\left( \mathrm { I } - \mathrm { A } \right) ^ { - 1 } \cong \mathrm { I } + \mathrm { A } + \mathrm { A } ^ { 2 }$$
(188)

$$\left( \mathrm { I } + \mathrm { A } \right) ^ { - 1 } \cong \mathrm { I } - \mathrm { A } + \mathrm { A } ^ { 2 }$$
(189)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 20" -->
<!-- PageBreak -->

<!-- PageHeader="3 INVERSES" -->
<!-- PageHeader="3.5 Generalized Inverse" -->

The following approximation is from [22] and holds when $\mathrm { A }$ large and symmetric

$$\mathrm { A } - \mathrm { A } \left( \mathrm { I } + \mathrm { A } \right) ^ { - 1 } \mathrm { A } \cong \mathrm { I } - \mathrm { A } ^ { - 1 }$$
(190)

If $\sigma ^ { 2 }$ is small compared to $\mathrm { Q }$ and $M$ then

$$\left( \mathrm { Q } + \sigma ^ { 2 } \mathrm { M } \right) ^ { - 1 } \cong \mathrm { Q } ^ { - 1 } - \sigma ^ { 2 } \mathrm { Q } ^ { - 1 } \mathrm { M Q } ^ { - }$$
(191)

Proof:

$$\left( \mathrm { Q } + \sigma ^ { 2 } \mathrm { M } \right) ^ { - 1 } =$$
$$\left( \mathrm { Q Q } ^ { - 1 } \mathrm { Q } + \sigma ^ { 2 } \mathrm { M Q } ^ { - 1 } \mathrm { Q } \right) ^ { - 1 } =$$
(192)
(193)

$$\left( \left( I + \sigma ^ { 2 } M Q ^ { - 1 } \right) Q \right) ^ { - 1 } =$$
$$\mathrm { Q } ^ { - 1 } \left( \mathrm { I } + \sigma ^ { 2 } \mathrm { M Q } ^ { - 1 } \right) ^ { - 1 }$$
(194)
(195)

This can be rewritten using the Taylor expansion:

$$Q ^ { - 1 } \left( I + \sigma ^ { 2 } M Q ^ { - 1 } \right) ^ { - 1 } =$$
$$\mathrm { Q } ^ { - 1 } \left( \mathrm { I } - \sigma ^ { 2 } \mathrm { M Q } ^ { - 1 } + \left( \sigma ^ { 2 } \mathrm { M Q } ^ { - 1 } \right) ^ { 2 } - \ldots \right) \cong \mathrm { Q } ^ { - 1 } - \sigma ^ { 2 } \mathrm { Q } ^ { - 1 } \mathrm { M Q } ^ { - 1 }$$
(196)
(197)


### 3.5 Generalized Inverse


#### 3.5.1 Definition

A generalized inverse matrix of the matrix $\mathrm { A }$ is any matrix $\mathrm { A } ^ { - }$ such that (see
[26])

$$\mathrm { A A } ^ { - } \mathrm { A } = \mathrm { A }$$
(198)

The matrix A - is not unique.


### 3.6 Pseudo Inverse


#### 3.6.1 Definition

The pseudo inverse (or Moore-Penrose inverse) of a matrix $\mathrm { A }$ is the matrix $A +$
that fulfils

I
$\mathrm { A A } ^ { + } \mathrm { A } = \mathrm { A }$
II
$\mathrm { A } ^ { + } \mathrm { A A } ^ { + } = \mathrm { A } ^ { + }$

III
AA+ symmetric

IV
$\mathrm { A } ^ { + } \mathrm { A }$ symmetric

The matrix $\mathrm { A } ^ { + }$ is unique and does always exist. Note that in case of com-
plex matrices, the symmetric condition is substituted by a condition of being
Hermitian.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 21" -->
<!-- PageBreak -->

<!-- PageHeader="3 INVERSES" -->
<!-- PageHeader="3.6 Pseudo Inverse" -->


#### 3.6.2 Properties

Assume $\mathrm { A } ^ { + }$ to be the pseudo-inverse of $\mathrm { A } ,$ then $\left( \mathrm { S e e } \left[ 3 \right] \right.$ for some of them)

$$\left( \mathrm { A } ^ { + } \right) ^ { + } = \mathrm { A }$$
$$\left( \mathrm { A } ^ { T } \right) ^ { + } = \left( \mathrm { A } ^ { + } \right) ^ { T }$$
$$\left( \mathrm { A } ^ { H } \right) ^ { + } = \left( \mathrm { A } ^ { + } \right) ^ { H }$$
$$\left( \mathrm { A } ^ { * } \right) ^ { + } = \left( A ^ { + } \right) ^ { * }$$
$$\left( A ^ { + } A \right) A ^ { H } = A ^ { H }$$
$$\left( A ^ { + } A \right) A ^ { T } \neq A ^ { T }$$
$$\left( c A \right) ^ { + } = \left( 1 / c \right) A ^ { + }$$
$$\mathrm { A } ^ { + } = \left( \mathrm { A } ^ { T } \mathrm { A } \right) ^ { + } \mathrm { A } ^ { T }$$
$$\mathrm { A } ^ { + } = \mathrm { A } ^ { T } \left( \mathrm { A A } ^ { T } \right) ^ { + }$$
$$\left( \mathrm { A } ^ { T } \mathrm { A } \right) ^ { + } = \mathrm { A } ^ { + } \left( \mathrm { A } ^ { T } \right) ^ { + }$$
$$\left( \mathrm { A A } ^ { T } \right) ^ { + } = \left( \mathrm { A } ^ { T } \right) ^ { + } \mathrm { A } ^ { + }$$
$$\mathrm { A } ^ { + } = \left( \mathrm { A } ^ { H } \mathrm { A } \right) ^ { + } \mathrm { A } ^ { H }$$
$$\mathrm { A } ^ { + } = \mathrm { A } ^ { H } \left( \mathrm { A A } ^ { H } \right) ^ { + }$$
$$\left( \mathrm { A } ^ { H } \mathrm { A } \right) ^ { + } = \mathrm { A } ^ { + } \left( \mathrm { A } ^ { H } \right) ^ { + }$$
$$\left( \mathrm { A A } ^ { H } \right) ^ { + } = \left( \mathrm { A } ^ { H } \right) ^ { + } \mathrm { A } ^ { + }$$
$$\left( \mathrm { A B } \right) ^ { + } = \left( \mathrm { A } ^ { + } \mathrm { A B } \right) ^ { + } \left( \mathrm { A B B } ^ { + } \right) ^ { + }$$
(199)
(200)
(201)
(202)
(203)
(204)
(205)
(206)
(207)
(208)
(209)
(210)
(211)
(212)
(213)
(214)

$$f \left( \mathrm { A } ^ { H } \mathrm { A } \right) - f \left( 0 \right) \mathrm { I } = \mathrm { A } ^ { + } \left[ f \left( \mathrm { A A } ^ { H } \right) - f \left( 0 \right) \mathrm { I } \right] \mathrm { A }$$
$$\mathrm { T r } \left( \mathrm { A } ^ { + } \mathrm { A } \right) = \mathrm { r a n k } \left( \mathrm { A } ^ { + } \mathrm { A } \right)$$
$$f \left( \mathrm { A A } ^ { H } \right) - f \left( 0 \right) \mathrm { I } = \mathrm { A } \left[ f \left( \mathrm { A } ^ { H } \mathrm { A } \right) - f \left( 0 \right) \mathrm { I } \right] \mathrm { A } ^ { + }$$
(216)

$$\left( \mathrm { A A } ^ { + } \right) \left( \mathrm { A A } ^ { + } \right) = \mathrm { A A } ^ { + }$$
$$\left( \mathrm { A } ^ { + } \mathrm { A } \right) \left( \mathrm { A } ^ { + } \mathrm { A } \right) = \mathrm { A } ^ { + } \mathrm { A }$$
(217)
(218)

$$\mathrm { T r } \left( \mathrm { A A } ^ { + } \right) = \mathrm { r a n k } \left( \mathrm { A A } ^ { + } \right)$$
(See [26])
(219)

(215)
where $\mathrm { A } \in \mathbb{C} ^ { n \times m } .$
Assume $\mathrm { A }$ to have full rank, then
(See [26])
(220)

For two matrices it hold that

$$\left( \mathrm { A B } \right) ^ { + } = \left( \mathrm { A } ^ { + } \mathrm { A B } \right) ^ { + } \left( \mathrm { A B B } ^ { + } \right) ^ { + }$$
(221)

$$\left( \mathrm { A } \otimes \mathrm { B } \right) ^ { + } = \mathrm { A } ^ { + } \otimes \mathrm { B } ^ { + }$$
(222)


#### 3.6.3 Construction

Assume that A has full rank, then

$$\begin{array}{} \mathrm { A } \mathrm { n } \times m \mathrm { B r o a d } \mathrm { r a n k } \left( \mathrm { A } \right) = n \Rightarrow \mathrm { A } ^ { + } = \mathrm { A } ^ { T } \left( \mathrm { A A } ^ { T } \right) ^ { - 1 } \\ \mathrm { A } n \times m \mathrm { T a l l } \mathrm { r a n k } \left( \mathrm { A } \right) = m \stackrel { \mathrm { A } ^ { + } = \mathrm { A } ^ { \mathrm { T } } \left( \mathrm { A } \mathrm { A } ^ { T } \right) ^ { - 1 } } { \mathrm { A } ^ { \mathrm { T } } \mathrm { A } ^ { \mathrm { T } } \mathrm { A } ^ { \mathrm { T } } }$$

The so-called "broad version" is also known as right inverse and the "tall ver-
sion" as the left inverse.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 22" -->
<!-- PageBreak -->

<!-- PageHeader="3.6 Pseudo Inverse" -->
<!-- PageHeader="3 INVERSES" -->

Assume A does not have full rank, i.e. A is $n \times m$ and $\mathrm { r a n k } \left( \mathrm { A } \right) = r <$
$\min \left( n , m \right) .$ The pseudo inverse $\mathrm { A } ^ { + }$ can be constructed from the singular value
decomposition $\mathrm { A } = \mathrm { U D V } ^ { T } ,$ by

$$\mathrm { A } ^ { + } = \mathrm { V } _ { r } \mathrm { D } _ { r } ^ { - 1 } \mathrm { U } _ { r } ^ { T }$$
(223)

where $\mathrm { U } _ { 1 } ,$ $\mathrm { D } _ { r } ,$ and $\mathrm { V } _ { \mathrm { r } }$ are the matrices with the degenerated rows and columns
deleted. A different way is this: There do always exist two matrices $\mathrm { C } n \times r$
and Dr $r \times m$ of rank r, such that $\mathrm { A } = \mathrm { C D } .$ Using these matrices it holds that

$$\mathrm { A } ^ { + } = \mathrm { D } ^ { T } \left( \mathrm { D D } ^ { T } \right) ^ { - 1 } \left( \mathrm { C } ^ { T } \mathrm { C } \right) ^ { - 1 } \mathrm { C } ^ { T }$$
(224)

See [3].

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 23" -->
<!-- PageBreak -->

<!-- PageHeader="4 COMPLEX MATRICES" -->


## 4 Complex Matrices

The complex scalar product $r = p q$ can be written as

$$\left[ \begin{array}{} { 9 x } \\ { 3 r } \end{array} \right] = \left[ \begin{array}{} { 9 x p } & { - 3 p } \\ { 5 p } & { 9 p } \end{array} \right] \left[ \begin{array}{} { 9 q } \\ { 3 q } \end{array} \right]$$
(225)


### 4.1 Complex Derivatives

In order to differentiate an expression $f \left( z \right)$ with respect to a complex z, the
Cauchy-Riemann equations have to be satisfied ([7]):

$$\frac { d f \left( z \right) } { d z } = \frac { \partial \mathfrak{R} \left( f \left( z \right) \right) } { \partial \mathfrak{R} z } + i \frac { \partial \mathfrak{I} \left( f \left( z \right) \right) } { \partial \mathfrak{R} z }$$
(226)

and

$$\frac { d f \left( z \right) } { d z } = - i \frac { \partial \mathfrak{R} \left( f \left( z \right) \right) } { \partial \mathfrak{I} z } + \frac { \partial \mathfrak{I} \left( f \left( z \right) \right) } { \partial \mathfrak{I} z }$$
(227)

or in a more compact form:

$$\frac { \partial f \left( z \right) } { \partial \mathrm { S } z } = i \frac { \partial f \left( z \right) } { \partial \mathrm { f } \mathrm { R } z } .$$
(228)

A complex function that satisfies the Cauchy-Riemann equations for points in $\mathrm { a }$
region $\mathrm { R }$ is said $\mathrm { y o }$ be analytic in this region R. In general, expressions involving
complex conjugate or conjugate transpose do not satisfy the Cauchy-Riemann
equations. In order to avoid this problem, a more generalized definition of
complex derivative is used ([24], [6]):

· Generalized Complex Derivative:

$$\frac { d f \left( z \right) } { d z } = \frac { 1 } { 2 } \left( \frac { \partial f \left( z \right) } { \partial \mathfrak{R} z } - i \frac { \partial f \left( z \right) } { \partial \mathfrak{I} z } \right) .$$
(229)

· Conjugate Complex Derivative

$$\frac { d f \left( z \right) } { d z ^ { * } } = \frac { 1 } { 2 } \left( \frac { \partial f \left( z \right) } { \partial \mathfrak{R} z } + i \frac { \partial f \left( z \right) } { \partial \mathfrak{I} z } \right) .$$
(230)

The Generalized Complex Derivative equals the normal derivative, when $f \quad i s \quad a n$
analytic function. For a non-analytic function such $\mathrm { a s } f \left( z \right) = z ^ { * } ,$ the derivative
equals zero. The Conjugate Complex Derivative equals zero, when $f \quad i s \quad a n$
analytic function. The Conjugate Complex Derivative has e.g been used by [21]
when deriving a complex gradient.

Notice:

$$\frac { d f \left( z \right) } { d z } \neq \frac { \partial f \left( z \right) } { \partial \mathfrak{R} z } + i \frac { \partial f \left( z \right) } { \partial \mathfrak{I} z } .$$
(231)

· Complex Gradient Vector: If $f$ is a real function of a complex vector z,
then the complex gradient vector is given by ([14, p. 798])

$$\nabla f \left( \mathrm { z } \right) = 2 \frac { d f \left( \mathrm { z } \right) } { d \mathrm { z } ^ { * } }$$
$$= \frac { \partial f \left( \mathrm { z } \right) } { \partial \mathfrak{R} \mathrm { z } } + i \frac { \partial f \left( \mathrm { z } \right) } { \partial \mathfrak{I} \mathrm { z } } .$$
(232)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 24" -->
<!-- PageBreak -->

<!-- PageHeader="4 COMPLEX MATRICES" -->
<!-- PageHeader="4.1 Complex Derivatives" -->

. Complex Gradient Matrix: If $f$ is a real function of a complex matrix $Z ,$
then the complex gradient matrix is given by ([2])

$$\nabla f \left( \mathrm { Z } \right) = 2 \frac { d f \left( \mathrm { Z } \right) } { d \mathrm { Z } ^ { * } }$$
$$= \frac { \partial f \left( Z \right) } { \partial \mathfrak{R} Z } + i \frac { \partial f \left( Z \right) } { \partial \mathfrak{I} Z } .$$
(233)

These expressions can be used for gradient descent algorithms.


#### 4.1.1 The Chain Rule for complex numbers

The chain rule is a little more complicated when the function of a complex
$u = f \left( x \right)$ is non-analytic. For a non-analytic function, the following chain rule
can be applied ([7])

$$\frac { \partial g \left( u \right) } { \partial x } = \frac { \partial g } { \partial u } \frac { \partial u } { \partial x } + \frac { \partial g } { \partial u ^ { * } } \frac { \partial u ^ { * } } { \partial x }$$
$$= \frac { \partial g } { \partial u } \frac { \partial u } { \partial x } + \left( \frac { \partial g ^ { * } } { \partial u } \right) ^ { * } \frac { \partial u ^ { * } } { \partial x }$$
(234)

Notice, if the function is analytic, the second term reduces to zero, and the func-
tion is reduced to the normal well-known chain rule. For the matrix derivative
of a scalar function $g \left( \mathrm { U } \right) ,$ the chain rule can be written the following way:

$$\frac { \partial g \left( \mathrm { U } \right) } { \partial \mathrm { X } } = \frac { \mathrm { T r } \left( \left( \frac { \partial g \left( \mathrm { U } \right) } { \partial \mathrm { U } } \right) ^ { T } \partial \mathrm { U } \right) } { \partial \mathrm { X } } + \frac { \mathrm { T r } \left( \left( \frac { \partial g \left( \mathrm { U } \right) } { \partial \mathrm { U } ^ { * } } \right) ^ { T } \partial \mathrm { U } ^ { * } \right) } { \partial \mathrm { X } } .$$
(235)


#### 4.1.2 Complex Derivatives of Traces

If the derivatives involve complex numbers, the conjugate transpose is often in-
volved. The most useful way to show complex derivative is to show the derivative
with respect to the real and the imaginary part separately. An easy example is:

$$\frac { \partial \mathrm { T r } \left( X ^ { * } \right) } { \partial \mathrm { f i X } } = \frac { \partial \mathrm { T r } \left( \mathrm { X } ^ { H } \right) } { \partial \mathrm { f } \mathrm { X } } = \mathrm { I }$$
$$i \frac { \partial \mathrm { T r } \left( \mathrm { X } ^ { * } \right) } { \partial \mathrm { S X } } = i \frac { \partial \mathrm { T r } \left( \mathrm { X } ^ { H } \right) } { \partial \mathrm { S X } } = \mathrm { I }$$ ☒ ☒
(236)
☒
(237)

Since the two results have the same sign, the conjugate complex derivative (230)
should be used.

$$\frac { \partial \mathrm { T r } \left( X \right) } { \partial R X } = \frac { \partial \mathrm { T r } \left( X ^ { T } \right) } { \partial \sec } = 1$$ ☒ ☒
(238)

$$i \frac { \partial \mathrm { T r } \left( X \right) } { \partial \mathrm { S X } } = i \frac { \partial \mathrm { T r } \left( X ^ { T } \right) } { \partial \mathrm { S X } } = - I$$ ☒ ☒
(239)

Here, the two results have different signs, and the generalized complex derivative
(229) should be used. Hereby, it can be seen that (100) holds even $i f \quad X \quad i s \quad a$
complex number.

$$\frac { \partial \mathrm { T r } \left( \mathrm { A X } ^ { H } \right) } { \partial \mathrm { R X } } = \mathrm { A }$$
(240)

$$i \frac { \partial \mathrm { T r } \left( \mathrm { A X } ^ { H } \right) } { \partial \mathrm { S X } } = \mathrm { A }$$
(241)

PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 25

<!-- PageBreak -->

<!-- PageHeader="4.2 Higher order and non-linear derivatives" -->
<!-- PageHeader="4 COMPLEX MATRICES" -->

$$\frac { \partial \mathrm { T r } \left( A X ^ { * } \right) } { \partial \mathfrak{R} X } = A ^ { T }$$
(242)

$$i \frac { \partial \mathrm { T r } \left( \mathrm { A X } ^ { * } \right) } { \partial \mathrm { S X } } = \mathrm { A } ^ { T }$$
$$\frac { \partial \mathrm { T r } \left( \mathrm { X X } ^ { H } \right) } { \partial \mathrm { f } \mathrm { X } } = \frac { \partial \mathrm { T r } \left( \mathrm { X } ^ { H } \mathrm { X } \right) } { \partial \mathrm { f } \mathrm { X } } = 2 \mathrm { R } \mathrm { X }$$
(243)
☒ ☒ ☒
(244)

$$i \frac { \partial \mathrm { T r } \left( \mathrm { X X } ^ { H } \right) } { \partial \mathrm { S X } } = i \frac { \partial \mathrm { T r } \left( \mathrm { X } ^ { H } \mathrm { X } \right) } { \partial \mathrm { S X } } = i 2 \mathrm { S X }$$ ☒ ☒ ☒
(245)

By inserting (244) and (245) in (229) and (230), it can be seen that

$$\frac { \partial \mathrm { T r } \left( \mathrm { X X } ^ { H } \right) } { \partial \mathrm { X } } = \mathrm { X } ^ { * }$$ ☒ ☒ ☒
(246)

$$\frac { \partial \mathrm { T r } \left( \mathrm { X X } ^ { H } \right) } { \partial \mathrm { X } ^ { * } } = \mathrm { X }$$ ☒ ☒
(247)
☒

Since the function $\mathrm { T r } \left( \mathrm { X X } ^ { H } \right)$ is a real function of the complex matrix X, the
☒
complex gradient matrix (233) is given by
☒ ☒

$$\nabla \mathrm { T r } \left( \mathrm { X X } ^ { H } \right) = 2 \frac { \partial \mathrm { T r } \left( \mathrm { X X } ^ { H } \right) } { \partial \mathrm { X } ^ { * } } = 2 \mathrm { X }$$ ☒ ☒ ☒
(248)
☒


#### 4.1.3 Complex Derivative Involving Determinants

Here, a calculation example is provided. The objective is to find the derivative of
$\det \left( \mathrm { X } ^ { H } \mathrm { A X } \right)$ with respect to $\mathrm { X } \in \mathbb{C} ^ { m \times n } .$ The derivative is found with respect to
☒ ☒ ☒
the real part and the imaginary part $\mathrm { o f } \mathrm { X } ,$ by use of (42) and (37), $\det \left( \mathrm { X } ^ { H } \mathrm { A X } \right)$
☒ ☒ ☒
can be calculated as (see App. B.1.4 for details)

$$\frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathrm { X } } = \frac { 1 } { 2 } \left( \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{R} \mathrm { X } } - i \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{I} \mathrm { X } } \right)$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \mathrm { A } \right) ^ { T }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

(249)

and the complex conjugate derivative yields

$$\frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathrm { X } ^ { * } } = \frac { 1 } { 2 } \left( \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{R} \mathrm { X } } + i \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{I} \mathrm { X } } \right)$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \mathrm { A X } \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

(250)


### 4.2 Higher order and non-linear derivatives

$$\frac { \partial } { \partial \mathrm { x } } \frac { \left( \mathrm { A x } \right) ^ { H } \left( \mathrm { A x } \right) } { \left( \mathrm { B x } \right) ^ { H } \left( \mathrm { B x } \right) } = \frac { \partial \mathrm { x } ^ { H } \mathrm { A } ^ { H } \mathrm { A x } } { \partial \mathrm { x } \mathrm { x } ^ { H } \mathrm { B } ^ { H } \mathrm { B x } }$$ ☒
(251)
☒

$$= 2 \frac { \mathrm { A } ^ { H } \mathrm { A x } } { \mathrm { x } ^ { H } \mathrm { B B x } } - 2 \frac { \mathrm { x } ^ { H } \mathrm { A } ^ { H } \mathrm { A x B } ^ { H } \mathrm { B x } } { \left( \mathrm { x } ^ { H } \mathrm { B } ^ { H } \mathrm { B x } \right) ^ { 2 } }$$
(252)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 26" -->
<!-- PageBreak -->

<!-- PageHeader="4 COMPLEX MATRICES" -->
<!-- PageHeader="4.3 Inverse of complex sum" -->


### 4.3 Inverse of complex sum

Given real matrices A, B find the inverse of the complex sum $\mathrm { A } + i \mathrm { B } .$ Form
the auxiliary matrices

$$\mathrm { E } = \mathrm { A } + t \mathrm { B }$$
(253)

$$\mathrm { F } = \mathrm { B } - t \mathrm { A } . ,$$
(254)

and find a value of $t$ such that $\mathrm { E } ^ { - 1 }$ exists. Then

$$\left( \mathrm { A } + i \mathrm { B } \right) ^ { - 1 } = \left( 1 - i t \right) \left( \mathrm { E } + i \mathrm { F } \right) ^ { - 1 }$$
$$= \left( 1 - i t \right) \left( \left( \mathrm { E } + \mathrm { F E } ^ { - 1 } \mathrm { F } \right) ^ { - 1 } - i \left( \mathrm { E } + \mathrm { F E } ^ { - 1 } \mathrm { F } \right) ^ { - 1 } \mathrm { F E } ^ { - 1 } \right) \left( 2 5 6 \right)$$
(255)

$$= \left( 1 - i t \right) \left( E + F E ^ { - 1 } F \right) ^ { - 1 } \left( I - i F E ^ { - 1 } \right)$$
(257)

$$= \left( E + F E ^ { - 1 } F \right) ^ { - 1 } \left( \left( I - t F E ^ { - 1 } \right) - i \left( t I + F E ^ { - 1 } \right) \right)$$
$$= \left( E + F E ^ { - 1 } F \right) ^ { - 1 } \left( I - t F E ^ { - 1 } \right)$$
$$- i \left( E + F E ^ { - 1 } F \right) ^ { - 1 } \left( t I + F E ^ { - 1 } \right)$$
(258)
(259)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 27" -->
<!-- PageBreak -->

<!-- PageHeader="5 SOLUTIONS AND DECOMPOSITIONS" -->


## 5 Solutions and Decompositions


### 5.1 Solutions to linear equations


#### 5.1.1 Simple Linear Regression

Assume we have data $\left( x _ { n } , y _ { n } \right)$ for $n = 1 , \ldots , N$ and are seeking the parameters
$a ,$ $b \in \mathbb{R} \mathrm { s u c h }$ that $y _ { i } \cong a x _ { i } + b .$ With a least squares error function, the optimal
values for $a ,$ $b$ can be expressed using the notation

$$\mathrm { x } = \left( x _ { 1 } , \ldots , x _ { N } \right) ^ { T } \quad \mathrm { y } = \left( y _ { 1 } , \ldots , y _ { N } \right) ^ { T } \quad 1 = \left( 1 , \ldots , 1 \right) ^ { T } \in \mathbb{R} ^ { N \times 1 }$$

and

$$R _ { x x } = x ^ { T } x \quad R _ { x 1 } = x ^ { T } 1 \quad R _ { 1 1 } = 1 ^ { T } 1$$
$$R _ { y x } = y ^ { T } x \quad R _ { y 1 } = y ^ { T } 1$$

as

$$\left[ \begin{array}{} { a } \\ { b } \end{array} \right] = \left[ \begin{array}{} { R _ { x x } } & { R _ { x 1 } } \\ { R _ { x 1 } } & { R _ { 1 1 } } \end{array} \right] ^ { - 1 } \left[ \begin{array}{} { R _ { x , y } } \\ { R _ { y 1 } } \end{array} \right]$$
(260)


#### 5.1.2 Existence in Linear Systems

Assume $\mathrm { A }$ is $n \times m$ and consider the linear system

$$\mathrm { A x } = \mathrm { b }$$
(261)

Construct the augmented matrix $\mathrm { B } = \left[ \mathrm { A } \mathrm { b } \right.$ then

Condition
Solution

$$\mathrm { r a n k } \left( \mathrm { A } \right) = \mathrm { r a n k } \left( \mathrm { B } \right) = m \quad \text { Unique solution } \mathrm { x }$$
$$\mathrm { r a n k } \left( \mathrm { A } \right) = \mathrm { r a n k } \left( \mathrm { B } \right) < m \quad \text { Many solutions x }$$
$$\mathrm { r a n k } \left( \mathrm { A } \right) < \mathrm { r a n k } \left( \mathrm { B } \right) \quad \text { No solutions x }$$


#### 5.1.3 Standard Square

Assume $\mathrm { A }$ is square and invertible, then

$$A x = b \quad \Rightarrow \quad x = A ^ { - 1 } b$$
(262)


#### 5.1.4 Degenerated Square

Assume $\mathrm { A }$ is $n \times n$ but of rank $r < n .$ In that case, the system $\mathrm { A x } = \mathrm { b }$ is solved
by

$$\mathrm { x } = \mathrm { A } ^ { + } \mathrm { b }$$

where $\mathrm { A } ^ { + }$ is the pseudo-inverse of the rank-deficient matrix, constructed as
described in section 3.6.3.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 28" -->
<!-- PageBreak -->


##### 5.1 Solutions to linear equations5 SOLUTIONS AND DECOMPOSITIONS


#### 5.1.5 Cramer's rule

The equation

$$\mathrm { A x } = \mathrm { b } ,$$
(263)

where $\mathrm { A }$ is square has exactly one solution $\mathrm { x }$ if the $i \mathrm { t h }$ element in x can be
found as

$$x _ { i } = \frac { \det \mathrm { B } } { \det \mathrm { A } } ,$$
(264)

where $\mathrm { B }$ equals $\mathrm { A } ,$ but the ith column in A has been substituted by $\mathrm { b } .$


#### 5.1.6 Over-determined Rectangular

Assume A to be $n \times m ,$ $n > m \left( \mathrm { t a l l } \right)$ and $\mathrm { r a n k } \left( \mathrm { A } \right) = m ,$ then

$$\mathrm { A x } = \mathrm { b } \quad \Rightarrow \quad \mathrm { x } = \left( \mathrm { A } ^ { T } \mathrm { A } \right) ^ { - 1 } \mathrm { A } ^ { T } \mathrm { b } = \mathrm { A } ^ { + } \mathrm { b }$$
(265)

that is if there exists a solution $\mathrm { x }$ at all! If there is no solution the following
can be useful:

$$\mathrm { A x } = \mathrm { b } \quad \Rightarrow \quad \mathrm { x } _ { m i n } = \mathrm { A } ^ { + } \mathrm { b }$$
(266)

Now $\mathrm { x } _ { m i n }$ is the vector $\mathrm { x }$ which minimizes $| | \mathrm { A x } - \mathrm { b } | | ^ { 2 } ,$ i.e. the vector which is
"least wrong". The matrix $\mathrm { A } ^ { + }$ is the pseudo-inverse of $\mathrm { A } .$ See [3].


#### 5.1.7 Under-determined Rectangular

Assume $\mathrm { A }$ is $n \times m$ and n < m ("broad") and rank(A) = n.
☒

$$\mathrm { A x } = \mathrm { b } \quad \Rightarrow \quad \mathrm { x } _ { m i n } = \mathrm { A } ^ { T } \left( \mathrm { A A } ^ { T } \right) ^ { - 1 } \mathrm { b }$$
(267)

The equation have many solutions x. But $\mathrm { x } _ { m i n }$ is the solution which minimizes
$| | A x - b | | ^ { 2 }$ and also the solution with the smallest norm | $| | x | | ^ { 2 } .$ The same holds
☒
for a matrix version: Assume $\mathrm { A }$ is $n \times m ,$ $X$ is $m \times n$ and Bis $n \times n ,$ then
☒

$$\mathrm { A X } = \mathrm { B } \quad \Rightarrow \quad \mathrm { X } _ { m i n } = \mathrm { A } ^ { + } \mathrm { B }$$ ☒
(268)

The equation have many solutions $\mathrm { X } .$ $\mathrm { B u t } \mathrm { X } _ { m i n }$ is the solution which minimizes
☒ ☒

$| | \mathrm { A X } - \mathrm { B } | | ^ { 2 }$ and also the solution with the smallest norm $| | \mathrm { X } | | ^ { 2 } .$ See [3].
☒

Similar but different: Assume $\mathrm { A }$ is square $n \times n$ and the matrices $\mathrm { B } _ { 0 } ,$ $\mathrm { B } _ { 1 }$
are $n \times N ,$ where $N > n ,$ then if $\mathrm { B } _ { 0 }$ has maximal rank

$$\mathrm { A B } _ { 0 } = \mathrm { B } _ { 1 } \quad \Rightarrow \quad \mathrm { A } _ { m i n } = \mathrm { B } _ { 1 } \mathrm { B } _ { 0 } ^ { T } \left( \mathrm { B } _ { 0 } \mathrm { B } _ { 0 } ^ { T } \right) ^ { - 1 }$$
(269)

where $\mathrm { A } _ { m i n }$ denotes the matrix which is optimal in a least square sense. An
interpretation is that $\mathrm { A }$ is the linear approximation which maps the columns
vectors of $\mathrm { B } _ { 0 }$ into the columns vectors of $\mathrm { B } _ { 1 } .$


#### 5.1.8 Linear form and zeros

$$\mathrm { A x } = 0 , \quad \forall \mathrm { x } \quad \Rightarrow \quad \mathrm { A } = 0$$
(270)


#### 5.1.9 Square form and zeros

If $\mathrm { A }$ is symmetric, then

$$\mathrm { x } ^ { T } \mathrm { A x } = 0 , \quad \forall \mathrm { x } \quad \Rightarrow \quad \mathrm { A } = 0$$ ☒
(271)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 29" -->
<!-- PageBreak -->

<!-- PageHeader="5.2 Eigenvalues and Eigenvectors SOLUTIONS AND DECOMPOSITIONS" -->


#### 5.1.10 The Lyapunov Equation

$$\mathrm { A X } + \mathrm { X B } = \mathrm { C }$$
$$\mathrm { v e c } \left( \mathrm { X } \right) = \left( \mathrm { I } \otimes \mathrm { A } + \mathrm { B } ^ { T } \otimes \mathrm { I } \right) ^ { - 1 } \mathrm { v e c } \left( \mathrm { C } \right)$$ ☒
(272)
☒
(273)

Sec 10.2.1 and 10.2.2 for details on the Kronecker product and the vec op-
erator.


#### 5.1.11 Encapsulating Sum

$$\sum _ { n } A _ { n } X B _ { n } = C$$
$$\mathrm { v e c } \left( \mathrm { X } \right) = \left( \sum _ { n } \mathrm { B } _ { n } ^ { T } \otimes \mathrm { A } _ { n } \right) ^ { - 1 } \mathrm { v e c } \left( \mathrm { C } \right)$$ ☒
(274)
☒
(275)

See Sec 10.2.1 and 10.2.2 for details on the Kronecker product and the vec
operator.


### 5.2 Eigenvalues and Eigenvectors


#### 5.2.1 Definition

The eigenvectors $\mathrm { v } _ { i }$ and eigenvalues $\lambda _ { i }$ are the ones satisfying

$$\mathrm { A v } _ { i } = \lambda _ { i } \mathrm { v } _ { i }$$
(276)


#### 5.2.2 Decompositions

For matrices $\mathrm { A }$ with as many distinct eigenvalues as dimensions, the following
holds, where the columns of $\mathrm { v }$ are the eigenvectors and $\left( \mathrm { D } \right) _ { i j } = \delta _ { i j } \lambda _ { i } ,$

$$\mathrm { A V } = \mathrm { V D }$$
(277)

For defective matrices $\mathrm { A } ,$ which is matrices which has fewer distinct eigenvalues
than dimensions, the following decomposition called Jordan canonical form,
holds

$$\mathrm { A V } = \mathrm { V J }$$
(278)

where $J$ is a block diagonal matrix with the blocks $\mathrm { J } _ { i } = \lambda _ { i } \mathrm { I } + \mathrm { N } .$ The matrices
$\mathrm { J } _ { i }$ have dimensionality as the number of identical eigenvalues equal to $\lambda _ { i } ,$ and N
is square matrix of same size with 1 on the super diagonal and zero elsewhere.

It also holds that for all matrices $\mathrm { A }$ there exists matrices $\mathrm { v }$ and R such that

$$\mathrm { A V } = \mathrm { V R }$$
(279)

where $\mathrm { R }$ is upper triangular with the eigenvalues $\lambda _ { i }$ on its $\mathrm { d i a g o n a l } .$


#### 5.2.3 General Properties

Assume that $\mathrm { A } \in \mathbb{R} ^ { n \times m }$ and $\mathrm { B } \in \mathbb{R} ^ { m \times n }$

$$\mathrm { e i g } \left( \mathrm { A B } \right) \quad = \quad \mathrm { e i g } \left( \mathrm { B A } \right)$$

(280)
$$\mathrm { r a n k } \left( \mathrm { A } \right) = r \quad \Rightarrow \quad \mathrm { A t } \mathrm { m o s t } r \mathrm { n o n - z e r o } \lambda _ { i }$$
(281)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 30" -->
<!-- PageBreak -->

<!-- PageHeader="5.3 Singular Value Decomposition SOLUTIONS AND DECOMPOSITIONS" -->


#### 5.2.4 Symmetric

Assume $\mathrm { A }$ is symmetric, then

$$\mathrm { V V } ^ { T } = \mathrm { I } \quad \text { \left(i.e. V is orthogonal\right) }$$
$$\lambda _ { i } \in \mathbb{R} \quad \text { \left(i.e. \lambda_{i } \text { is real\right) } }$$
(282)
(283)

$$\mathrm { T r } \left( \mathrm { A } ^ { p } \right) = \sum _ { i } \lambda _ { i } ^ { p }$$
$$\mathrm { e i g } \left( \mathrm { I } + c \mathrm { A } \right) = 1 + c \lambda _ { i }$$
(284)
(285)

$$\mathrm { e i g } \left( \mathrm { A } - c \mathrm { I } \right) = \lambda _ { i } - c$$
$$\mathrm { e i g } \left( \mathrm { A } ^ { - 1 } \right) = \lambda _ { i } ^ { - 1 }$$
(286)
(287)

For a symmetric, positive matrix $\mathrm { A } ,$

$$\mathrm { e i g } \left( \mathrm { A } ^ { T } \mathrm { A } \right) = \mathrm { e i g } \left( \mathrm { A A } ^ { T } \right) = \mathrm { e i g } \left( \mathrm { A } \right) \circ \mathrm { e i g } \left( \mathrm { A } \right)$$
(288)


#### 5.2.5 Characteristic polynomial

The characteristic polynomial for the matrix $\mathrm { A }$ is

$$0 = \det \left( \mathrm { A } - \lambda \mathrm { I } \right)$$
$$= \lambda ^ { n } - g _ { 1 } \lambda ^ { n - 1 } + g _ { 2 } \lambda ^ { n - 2 } - \ldots + \left( - 1 \right) ^ { n } g _ { n }$$
(289)
(290)

Note that the coefficients $g _ { 1 }$ for $j = 1 , \ldots , n$ are the $n$ invariants under rotation
of $\mathrm { A } .$ Thus, $g _ { \jmath }$ is the sum of the determinants of all the sub-matrices of $\mathrm { A }$ taken
$j$ rows and columns at a time. That is, $g _ { 1 }$ is the trace of $\mathrm { A } ,$ and $g _ { 2 }$ is the sum
of the determinants of the $n \left( n \quad - \quad 1 \right) / 2$ sub-matrices that can be formed from $\mathrm { A }$
by deleting all but two rows and columns, and so on - see [17].


### 5.3 Singular Value Decomposition

Any n x m matrix A can be written as

$$\mathrm { A } = \mathrm { U D V } ^ { T } ,$$
(291)
,

where

$$\begin{array}{} \mathrm { U } & = & \text { eigenvectors of } \mathrm { A A } ^ { T } & n \times n \\ \mathrm { D } & = & \sqrt { \mathrm { d i a g } \left( \mathrm { e i g } \left( \mathrm { A A T } \right) \right) } & n \times m \end{array}$$
$$\mathrm { V } = \text { eigenvectors of } \mathrm { A } ^ { T } \mathrm { A } \quad m \times m$$ ☒
(292)


#### 5.3.1 Symmetric Square decomposed into squares

Assume $\mathrm { A }$ to be $n \times$ n and symmetric. Then

$$\left\lceil \mathrm { A } \right\rceil = \left\lceil \mathrm { V } \right\rceil \left\lceil \mathrm { D } \right\rceil \left[ \mathrm { V } ^ { T } \right] ,$$
(293)

where $\mathrm { D }$ is $d i a g o n a l$ with the eigenvalues of $\mathrm { A } ,$ and $\mathrm { v }$ is orthogonal and the
eigenvectors of $\mathrm { A } .$


#### 5.3.2 Square decomposed into squares

Assume $\mathrm { A } \in \mathbb{R} ^ { n \times n } .$ Then

$$\left\lceil \mathrm { A } \right\rceil = \left\lceil \mathrm { V } \right\rceil \left\lceil \mathrm { D } \right\rceil \left[ \mathrm { U } ^ { T } \right] ,$$
(294)

where $\mathrm { D }$ is diagonal with the square root of the eigenvalues of $\mathrm { A A } ^ { T } ,$ $\mathrm { V }$ is the
eigenvectors of $\mathrm { A A } ^ { T }$ and $\mathrm { U } ^ { T }$ is the eigenvectors of $\mathrm { A } ^ { T } \mathrm { A } .$

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 31" -->
<!-- PageBreak -->

<!-- PageHeader="5.4 Triangular Decomposition 5 SOLUTIONS AND DECOMPOSITIONS" -->


#### 5.3.3 Square decomposed into rectangular

Assume $\mathrm { V } _ { * } \mathrm { D } _ { * } \mathrm { U } _ { * } ^ { T } = 0$ then we can expand the SVD of $\mathrm { A }$ into

$$\left[ \begin{array}{} \mathrm { A } \end{array} \right] = \left[ \begin{array}{} \mathrm { V } & \mathrm { V } _ { * } \end{array} \right] \left[ \begin{array}{} \mathrm { D } & \mathrm { D } & \mathrm { U } \\ 0 & \mathrm { D } _ { * } & \mathrm { D } _ { * } \end{array} \right] \left[ \begin{array}{} \mathrm { U } ^ { T } \\ \bar { \mathrm { U } _ { * } ^ { T } } \end{array} \right] ,$$
(295)

where the SVD of $\mathrm { A }$ is $\mathrm { A } = \mathrm { V D U } ^ { T } .$


#### 5.3.4 Rectangular decomposition I

Assume $\mathrm { A }$ is $n \times m ,$ $\mathrm { v }$ is $n \times n ,$ $\mathrm { D }$ is $n \times n ,$ $\mathrm { U } ^ { T }$ is $n \times m$

$$\left[ \begin{array}{} & \mathrm { A } & \end{array} \right] = \left[ \begin{array}{} \mathrm { V } \end{array} \right] \left[ \begin{array}{} \mathrm { D } \end{array} \right] \left[ \begin{array}{} \mathrm { U } ^ { T } \end{array} \right] ,$$
(296)

where $\mathrm { D }$ is diagonal with the square root of the eigenvalues of $\mathrm { A A } ^ { T } ,$ $\mathrm { V }$ is the
eigenvectors of $\mathrm { A A } ^ { T }$ and $\mathrm { U } ^ { T }$ is the eigenvectors of $\mathrm { A } ^ { T } \mathrm { A } .$


#### 5.3.5 Rectangular decomposition II

Assume $\mathrm { A }$ is $n \times m ,$ $\mathrm { v }$ is $n \times m ,$ $m \text { is } m \times m ,$ $\mathrm { U } ^ { T }$ is m $\times$ m

$$\left[ \begin{array}{} { A } & { 1 = \left[ \begin{array}{} { V } & { 1 } \end{array} \right] \left[ \begin{array}{} { I } \\ { D } \end{array} \right] \left[ \begin{array}{} { U ^ { T } } \end{array} \right] } \end{array} \right.$$
(297)


#### 5.3.6 Rectangular decomposition III

Assume $\mathrm { A }$ is $n \times m ,$ $\mathrm { V }$ is $n \times n ,$ D is $n \times m$ m, $\mathrm { U } ^ { T }$ is $m \times m$

$$\left[ \begin{array}{} \mathrm { A } & \mathrm { \left. \right] } = \left[ \begin{array}{} \mathrm { V } \end{array} \right] \left[ \begin{array}{} \mathrm { D } & & \end{array} \right] \end{array} \left[ \begin{array}{} \mathrm { U } ^ { T } \end{array} \right] , \right. ,$$
(298)

where $\mathrm { D }$ is diagonal with the square root of the eigenvalues of $\mathrm { A A } ^ { T } ,$ $\mathrm { V } \mathrm { i s } \mathrm { t h e }$
eigenvectors of $\mathrm { A A } ^ { T }$ and $\mathrm { U } ^ { T }$ is the eigenvectors of $\mathrm { A } ^ { T } \mathrm { A } .$


### 5.4 Triangular Decomposition


### 5.5 LU decomposition

Assume $\mathrm { A }$ is a square matrix with non-zero leading principal minors, then

$$\mathrm { A } = \mathrm { L U }$$
(299)

where L is a unique unit lower triangular matrix and $\mathrm { U }$ is a unique upper
triangular matrix.


#### 5.5.1 Cholesky-decomposition

Assume $\mathrm { A }$ is a symmetric positive definite square matrix, then

$$\mathrm { A } = \mathrm { U } ^ { T } \mathrm { U } = \mathrm { L L } ^ { T } ,$$
(300)
,

where U is a unique upper triangular matrix and L is a lower triangular matrix.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 32" -->
<!-- PageBreak -->

<!-- PageHeader="5.6 LDM decomposition" -->
<!-- PageHeader="5 SOLUTIONS AND DECOMPOSITIONS" -->


### 5.6 LDM decomposition

Assume $\mathrm { A }$ is a square matrix with non-zero leading principal minors1, then

$$\mathrm { A } = \mathrm { L D M } ^ { T }$$
(301)

where L, $M$ are unique unit lower triangular matrices and $\mathrm { D }$ is a unique diagonal
matrix.


### 5.7 LDL decompositions

The LDL decomposition are special cases of the LDM decomposition. Assume
$\mathrm { A }$ is a non-singular symmetric definite square matrix, then

$$\mathrm { A } = \mathrm { L D L } ^ { T } = \mathrm { L } ^ { T } \mathrm { D L }$$
(302)

where L is a unit lower triangular matrix and D is a diagonal matrix. If $\mathrm { A }$ is
also positive definite, then $\mathrm { D }$ has strictly positive diagonal entries.

1 If the matrix that corresponds to a principal minor is a quadratic upper-left part of the
larger matrix (i.e., it consists of matrix elements in rows and columns from 1 to k), then the
principal minor is called a leading principal minor. For an n times n square matrix, there are
n leading principal minors. [31]

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 33" -->
<!-- PageBreak -->

<!-- PageHeader="6 STATISTICS AND PROBABILITY" -->


## 6 Statistics and Probability


### 6.1 Definition of Moments

Assume $\mathrm { x } \in \mathbb{R} ^ { n \times 1 }$ is a random variable


#### 6.1.1 Mean

The vector of means, m, is defined by

$$\left( \mathrm { m } \right) _ { i } = \langle x _ { i } \rangle$$
(303)


#### 6.1.2 Covariance

The matrix of covariance $\mathrm { M }$ is defined by

$$\left( \mathrm { M } \right) _ { i j } = \langle \left( x _ { i } - \langle x _ { i } \rangle \right) \left( x _ { j } - \langle x _ { j } \rangle \right) \rangle$$
(304)

or alternatively as

$$M = \langle \left( x - m \right) \left( x - m \right) ^ { T } \rangle$$
(305)


#### 6.1.3 Third moments

The matrix of third centralized moments - in some contexts referred to as
coskewness - is defined using the notation

$$m _ { i j k } ^ { \left( 3 \right) } = \langle \left( x _ { i } - \langle x _ { i } \rangle \right) \left( x _ { j } - \langle x _ { j } \rangle \right) \left( x _ { k } - \langle x _ { k } \rangle \right) \rangle$$
(306)

as

$$\mathrm { M } _ { 3 } = \left\lceil m _ { : : 1 } ^ { \left( 3 \right) } m _ { : : 2 } ^ { \left( 3 \right) } \ldots m _ { : : n } ^ { \left( 3 \right) } \right\rceil$$
(307)

where ':' denotes all elements within the given index. $\mathrm { M } _ { 3 }$ can alternatively be
expressed as

$$\mathrm { M } _ { 3 } = \langle \left( \mathrm { x } - \mathrm { m } \right) \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \otimes \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \rangle$$
(308)


#### 6.1.4 Fourth moments

The matrix of fourth centralized moments - in some contexts referred to as
cokurtosis - is defined using the notation

$$m _ { i j k l } ^ { \left( 4 \right) } = \langle \left( x _ { i } - \langle x _ { i } \rangle \right) \left( x _ { j } - \langle x _ { j } \rangle \right) \left( x _ { k } - \langle x _ { k } \rangle \right) \left( x _ { l } - \langle x _ { l } \rangle \right) \rangle$$
(309)

as

$$\mathrm { M } _ { 4 } = \left\lceil m _ { : : 1 1 } ^ { \left( 4 \right) } m _ { : : 2 1 } ^ { \left( 4 \right) } \ldots m _ { : : n 1 } ^ { \left( 4 \right) } | m _ { : : 1 2 } ^ { \left( 4 \right) } m _ { : : 2 2 } ^ { \left( 4 \right) } \ldots m _ { : : n 2 } ^ { \left( 4 \right) } \ldots | m _ { : : 1 n } ^ { \left( 4 \right) } m _ { : : 2 n } ^ { \left( 4 \right) } \ldots m _ { : : n n } ^ { \left( 4 \right) } | \right.$$
(310)

or alternatively as

$$\mathrm { M } _ { 4 } = \langle \left( \mathrm { x } - \mathrm { m } \right) \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \otimes \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \otimes \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \rangle$$
(311)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 34" -->
<!-- PageBreak -->

<!-- PageHeader="6.2 Expectation of Linear Combinations STATISTICS AND PROBABILITY" -->


### 6.2 Expectation of Linear Combinations


#### 6.2.1 Linear Forms

Assume $\mathrm { X }$ and $x$ to be a matrix and a vector of random variables. Then (see
See [26])

$$E \left[ \mathrm { A X B } + \mathrm { C } \right] = \mathrm { A } E \left[ \mathrm { X } \right] \mathrm { B } + \mathrm { C }$$ ☒
(312)

$$\mathrm { V a r } \left[ \mathrm { A x } \right] = \mathrm { A V a r } \left[ \mathrm { x } \right] \mathrm { A } ^ { T }$$
$$\mathrm { C o v } \left[ \mathrm { A x } , \mathrm { B y } \right] = \mathrm { A C o v } \left[ \mathrm { x } , \mathrm { y } \right] \mathrm { B } ^ { T }$$
(313)
(314)

Assume $x$ to be a stochastic vector with mean $\mathrm { m } ,$ then (see [7])

$$E \left[ \mathrm { A x } + \mathrm { b } \right] = \mathrm { A m } + \mathrm { b }$$
$$E \left[ \mathrm { A x } \right] = \mathrm { A m }$$
$$E \left[ x + b \right] = m + b$$
(315)
(316)
(317)


#### 6.2.2 Quadratic Forms

Assume $\mathrm { A }$ is symmetric, $\mathrm { c } = E \left[ \mathrm { x } \right]$ and $\Sigma = \mathrm { V a r } \left[ \mathrm { x } \right] .$ Assume also that all
coordinates $x _ { i }$ are independent, have the same central moments $\mu _ { 1 } , \mu _ { 2 } ,$ $\mu _ { 3 } ,$ $\mu _ { 4 }$
and denote $\mathrm { a } = \mathrm { d i a g } \left( \mathrm { A } \right) .$ Then (See [26])

$$E \left[ \mathrm { x } ^ { T } \mathrm { A x } \right] = \mathrm { T r } \left( \mathrm { A } \Sigma \right) + \mathrm { c } ^ { T } \mathrm { A c }$$
$$\mathrm { V a r } \left[ \mathrm { x } ^ { T } \mathrm { A x } \right] = 2 \mu _ { 2 } ^ { 2 } \mathrm { T r } \left( \mathrm { A } ^ { 2 } \right) + 4 \mu _ { 2 } \mathrm { c } ^ { T } \mathrm { A } ^ { 2 } \mathrm { c } + 4 \mu _ { 3 } \mathrm { c } ^ { T } \mathrm { A } \mathrm { a } + \left( \mu _ { 4 } - 3 \mu _ { 2 } ^ { 2 } \right) \mathrm { a } ^ { T } \mathrm { a } \left( 3 1 9 \right)$$
(318)

Also, assume $x$ to be a stochastic vector with mean $\mathrm { m } ,$ and covariance $M .$ Then
(see [7])

$$E \left[ \left( \mathrm { A x } + \mathrm { a } \right) \left( \mathrm { B x } + \mathrm { b } \right) ^ { T } \right] = \mathrm { A M B } ^ { T } + \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { B m } + \mathrm { b } \right) ^ { T }$$
$$E \left[ \mathrm { x x } ^ { T } \right] = \mathrm { M } + \mathrm { m m } ^ { T }$$
$$E \left[ \mathrm { x a } ^ { T } \mathrm { x } \right] = \left( \mathrm { M } + \mathrm { m m } ^ { T } \right) \mathrm { a }$$
$$E \left[ \mathrm { x } ^ { T } \mathrm { a x } ^ { T } \right] = \mathrm { a } ^ { T } \left( \mathrm { M } + \mathrm { m m } ^ { T } \right)$$
(320)
(321)
(322)
(323)

$$E \left[ \left( \mathrm { A x } \right) \left( \mathrm { A x } \right) ^ { T } \right] = \mathrm { A } \left( \mathrm { M } + \mathrm { m m } ^ { T } \right) \mathrm { A } ^ { T }$$
$$E \left[ \left( x + a \right) \left( x + a \right) ^ { T } \right] = M + \left( m + a \right) \left( m + a \right) ^ { T }$$
$$E \left[ \left( \mathrm { A x } + \mathrm { a } \right) ^ { T } \left( \mathrm { B x } + \mathrm { b } \right) \right] = \mathrm { T r } \left( \mathrm { A M B } ^ { T } \right) + \left( \mathrm { A m } + \mathrm { a } \right) ^ { T } \left( \mathrm { B m } + \mathrm { b } \right)$$
$$E \left[ x ^ { T } x \right] = T r \left( M \right) + m ^ { T } m$$
$$E \left[ \mathrm { x } ^ { T } \mathrm { A x } \right] = \mathrm { T r } \left( \mathrm { A M } \right) + \mathrm { m } ^ { T } \mathrm { A m }$$
(324)
(325)
(326)
(327)
(328)

$$E \left[ \left( \mathrm { A x } \right) ^ { T } \left( \mathrm { A x } \right) \right] = \mathrm { T r } \left( \mathrm { A M A } ^ { T } \right) + \left( \mathrm { A m } \right) ^ { T } \left( \mathrm { A m } \right)$$
$$E \left[ \left( x + a \right) ^ { T } \left( x + a \right) \right] = T r \left( M \right) + \left( m + a \right) ^ { T } \left( m + a \right)$$
(329)
(330)

$S e e \left[ 7 \right] .$

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 35" -->
<!-- PageBreak -->

<!-- PageHeader="6.3 Weighted Scalar Variable" -->
<!-- PageHeader="6 STATISTICS AND PROBABILITY" -->


#### 6.2.3 Cubic Forms

Assume x to be a stochastic vector with independent coordinates, mean m,
covariance M and central moments $\mathrm { v } _ { 3 } = E \left[ \left( \mathrm { x } - \mathrm { m } \right) ^ { 3 } \right] .$ Then (see [7])

$$E \left[ \left( \mathrm { A x } + \mathrm { a } \right) \left( \mathrm { B x } + \mathrm { b } \right) ^ { T } \left( \mathrm { C x } + \mathrm { c } \right) \right] = \mathrm { A d i a g } \left( \mathrm { B } ^ { T } \mathrm { C } \right) \mathrm { v } _ { 3 }$$
$$+ \mathrm { T r } \left( \mathrm { B M C } ^ { T } \right) \left( \mathrm { A m } + \mathrm { a } \right)$$
$$+ \mathrm { A M C } ^ { T } \left( \mathrm { B m } + \mathrm { b } \right)$$
$$+ \left( \mathrm { A M B } ^ { T } + \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { B m } + \mathrm { b } \right) ^ { T } \right) \left( \mathrm { C m } + \mathrm { c } \right)$$
$$E \left[ \left( A x + a \right) \left( A x + a \right) ^ { T } \left( A x + a \right) \right] = A d i a g \left( A ^ { T } A \right) v _ { 3 }$$
$$+ \left[ 2 A M A ^ { T } + \left( A x + a \right) \left( A x + a \right) ^ { T } \right] \left( A m + a \right)$$
$$+ \mathrm { T r } \left( \mathrm { A M A } ^ { T } \right) \left( \mathrm { A m } + \mathrm { a } \right)$$
$$E \left[ \left( \mathrm { A x } + \mathrm { a } \right) \mathrm { b } ^ { T } \left( \mathrm { C x } + \mathrm { c } \right) \left( \mathrm { D x } + \mathrm { d } \right) ^ { T } \right] = \left( \mathrm { A x } + \mathrm { a } \right) \mathrm { b } ^ { T } \left( \mathrm { C M D } ^ { T } + \left( \mathrm { C m } + \mathrm { c } \right) \left( \mathrm { D m } + \mathrm { d } \right) ^ { T } \right)$$
$$+ \left( \mathrm { A M C } ^ { T } + \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { C m } + \mathrm { c } \right) ^ { T } \right) \mathrm { b } \left( \mathrm { D m } + \mathrm { d } \right) ^ { T }$$
$$+ \mathrm { b } ^ { T } \left( \mathrm { C m } + \mathrm { c } \right) \left( \mathrm { A M D } ^ { T } - \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { D m } + \mathrm { d } \right) ^ { T } \right)$$
E[xx x] = V3+ 2Mm + (Tr(M) + m™m)m


### 6.3 Weighted Scalar Variable

Assume $\mathrm { x } \in \mathbb{R} ^ { n \times 1 }$ is a random variable, $\mathrm { w } \in \mathbb{R} ^ { n \times 1 }$ is a vector of constants and
$y$ is the linear combination $y = w ^ { T } x .$ Assume further that $\mathrm { m } ,$ $\mathrm { M } _ { 2 } ,$ $\mathrm { M } _ { 3 } ,$ $\mathrm { M } _ { 4 }$
denotes the mean, covariance, and central third and fourth moment matrix of
the variable $x .$ Then it holds that

$$\langle y \rangle = \mathrm { w } ^ { T } \mathrm { m }$$
$$\langle \left( y - \langle y \rangle \right) ^ { 2 } \rangle = \mathrm { w } ^ { T } \mathrm { M } _ { 2 } \mathrm { w }$$
$$\langle \left( y - \langle y \rangle \right) ^ { 3 } \rangle = \mathrm { w } ^ { T } \mathrm { M } _ { 3 } \mathrm { w } \otimes \mathrm { w }$$
$$\langle \left( y - \langle y \rangle \right) ^ { 4 } \rangle = \mathrm { w } ^ { T } \mathrm { M } _ { 4 } \mathrm { w } \otimes \mathrm { w } \otimes \mathrm { w }$$
(331)
(332)
(333)
(334)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 36" -->
<!-- PageBreak -->

<!-- PageHeader="7 MULTIVARIATE DISTRIBUTIONS" -->


## 7 Multivariate Distributions


### 7.1 Cauchy

The density function for a Cauchy distributed vector $\mathrm { t } \in \mathbb{R} ^ { P \times 1 } ,$ is given by

$$p \left( \mathrm { t } | \mu , \Sigma \right) = \pi ^ { - P / 2 } \frac { \Gamma \left( \frac { 1 + P } { 2 } \right) } { \Gamma \left( 1 / 2 \right) } \frac { \det \left( \Sigma \right) ^ { - 1 / 2 } } { \left[ 1 + \left( \mathrm { t } - \mu \right) ^ { \mathrm { T } } \Sigma ^ { - 1 } \left( \mathrm { t } - \mu \right) \right] ^ { \left( 1 + P \right) / 2 } }$$
(335)

where $\mu$ is the location, $\Sigma$ is positive definite, and $\Gamma$ denotes the gamma func-
tion. The Cauchy distribution is a special case of the Student-t distribution.


### 7.2 Dirichlet

The Dirichlet distribution is a kind of "inverse" distribution compared to the
multinomial distribution on the bounded continuous variate $\mathrm { x } = \left[ x _ { 1 } , \ldots , x _ { P } \right]$
[16, p. 44]

$$p \left( \mathrm { x } | \alpha \right) = \frac { \Gamma \left( \sum _ { p } ^ { P } \alpha _ { p } \right) } { \prod _ { p } ^ { P } \Gamma \left( \alpha _ { p } \right) } \prod _ { p } ^ { P } x _ { p } ^ { \alpha _ { p } - 1 }$$


### 7.3 Normal

The normal distribution is also known as a Gaussian distribution. See sec. 8.


### 7.4 Normal-Inverse Gamma


### 7.5 Gaussian

See sec. 8.


### 7.6 Multinomial

If the vector n contains counts, i.e. $\left( \mathrm { n } \right) _ { i } \in 0 , 1 , 2 , \ldots .$ , then the discrete multino-
mial disitrbution for n is given by

$$P \left( \mathrm { n } | \mathrm { a } , n \right) = \frac { n ! } { n _ { 1 } ! \ldots n _ { d } ! } \prod _ { i } ^ { d } a _ { i } ^ { n _ { i } } , \quad \sum _ { i } ^ { d } n _ { i } = n$$
(336)

where $a _ { i }$ are probabilities, i.e. $0 \leq a _ { i } \leq 1 \text { and } \sum _ { i } a _ { i } = 1 .$


### 7.7 Student's $\mathrm { t }$

The density of a Student-t distributed vector $\mathrm { t } \in \mathbb{R} ^ { P \times 1 } ,$ is given by

$$p \left( \mathrm { t } | \mu , \Sigma , \nu \right) = \left( \pi \nu \right) ^ { - P / 2 } \frac { \Gamma \left( \frac { \nu + P } { 2 } \right) } { \Gamma \left( \nu / 2 \right) } \frac { \det \left( \Sigma \right) ^ { - 1 / 2 } } { \left[ 1 + \nu ^ { - 1 } \left( \mathrm { t } - \mu \right) ^ { \mathrm { T } } \Sigma ^ { - 1 } \left( \mathrm { t } - \mu \right) \right] ^ { \left( \nu + P \right) / 2 } }$$
(337)

where $\mu$ is the location, the scale matrix $\Sigma$ is symmetric, positive definite, $\nu$
is the degrees of freedom, and $\Gamma$ denotes the gamma function. For $\nu = 1$ 1, the
Student-t distribution becomes the Cauchy distribution (see sec 7.1).

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 37" -->
<!-- PageBreak -->

<!-- PageHeader="7 MULTIVARIATE DISTRIBUTIONS" -->
<!-- PageHeader="7.8 Wishart" -->


#### 7.7.1 Mean

$$\mathrm { E } \left( \mathrm { t } \right) = \mu , \quad \nu > 1$$
(338)


### 7.7.2 Variance

$$\mathrm { c o v } \left( \mathrm { t } \right) = \frac { \nu } { \nu - 2 } \Sigma , \quad \nu > 2$$
(339)


### 7.7.3 Mode

The notion mode meaning the position of the most probable value

$$\mathrm { m o d e } \left( \mathrm { t } \right) = \mu$$
(340)


### 7.7.4 Full Matrix Version

$\text { If instead of a vector t } \in \mathbb{R} ^ { P \times }$ one has a matrix $\mathrm { T } \in \mathbb{R} ^ { P \times N } ,$ then the Student-t
distribution for $\mathrm { T }$ is

$$p \left( \mathrm { T } | \mathrm { M } , \Omega , \Sigma , \nu \right) = \pi ^ { - N P / 2 } \prod _ { p = 1 } ^ { P } \frac { \Gamma \left[ \left( \nu + P - p + 1 \right) / 2 \right] } { \Gamma \left[ \left( \nu - p + 1 \right) / 2 \right] } \times$$
$$\nu \det \left( \Omega \right) ^ { - \nu / 2 } \det \left( \Sigma \right) ^ { - N / 2 } \times$$
$$\det \left[ \Omega ^ { - 1 } + \left( \mathrm { T } - \mathrm { M } \right) \Sigma ^ { - 1 } \left( \mathrm { T } - \mathrm { M } \right) ^ { \mathrm { T } } \right] ^ { - \left( \nu + P \right) / 2 } \left( 3 4 1 \right)$$ ☒ ☒

where M is the location, $\Omega$ is the rescaling matrix, $\Sigma \text { is positive definite, } \nu \mathrm { i s }$
the degrees of freedom, and $\Gamma$ denotes the gamma function.


### 7.8 Wishart

The central Wishart distribution for $\mathrm { M } \in \mathbb{R} ^ { P \times P } ,$ $\mathrm { M }$ is positive definite, where
m can be regarded as a degree of freedom parameter [16, equation 3.8.1] [8,
section 2.5],[11]

$$p \left( \mathrm { M } | \Sigma , m \right) = \frac { 1 } { 2 ^ { m P / 2 } \pi ^ { P \left( P - 1 \right) / 4 } \prod _ { p } ^ { P } \Gamma \left[ \frac { 1 } { 2 } \left( m + 1 - p \right) \right] } \times$$
$$\det \left( \Sigma \right) ^ { - m / 2 } \det \left( \mathrm { M } \right) ^ { \left( m - P - 1 \right) / 2 } \times$$
$$\exp \left[ - \frac { 1 } { 2 } \mathrm { T r } \left( \Sigma ^ { - 1 } \mathrm { M } \right) \right]$$ ☒ ☒

(342)


#### 7.8.1 Mean

$$E \left( \mathrm { M } \right) = \mathrm { m } \Sigma$$
(343)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 38" -->
<!-- PageBreak -->

<!-- PageHeader="7 MULTIVARIATE DISTRIBUTIONS" -->
<!-- PageHeader="7.9 Wishart, Inverse" -->


### 7.9 Wishart, Inverse

The (normal) Inverse Wishart distribution for $\mathrm { M } \in \mathbb{R} ^ { P \times P } ,$ M is positive defi-
nite, where $m$ can be regarded as a degree of freedom parameter [11]

$$p \left( \mathrm { M } | \Sigma , m \right) = \frac { 1 } { 2 ^ { m P / 2 } \pi ^ { P \left( P - 1 \right) / 4 } \prod _ { p } ^ { P } \Gamma \left[ \frac { 1 } { 2 } \left( m + 1 - p \right) \right] } \times$$
$$\det \left( \Sigma \right) ^ { m / 2 } \det \left( \mathrm { M } \right) ^ { - \left( m - P - 1 \right) / 2 } \times$$
$$\exp \left[ - \frac { 1 } { 2 } \mathrm { T r } \left( \Sigma \mathrm { M } ^ { - 1 } \right) \right]$$ ☒ ☒ ☒

(344)


#### 7.9.1 Mean

$$E \left( \mathrm { M } \right) = \Sigma \frac { 1 } { m - P - 1 }$$
(345)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 39" -->
<!-- PageBreak -->

<!-- PageHeader="8 GAUSSIANS" -->


## 8 Gaussians


### 8.1 Basics


#### 8.1.1 .1 Density and normalization

The density of $\mathrm { x } \sim \mathcal{N} \left( \mathrm { m } , \Sigma \right)$ is

$$p \left( \mathrm { x } \right) = \frac { 1 } { \sqrt { \det \left( 2 \pi \Sigma \right) } } \exp \left[ - \frac { 1 } { 2 } \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \Sigma ^ { - 1 } \left( \mathrm { x } - \mathrm { m } \right) \right]$$ ☒ ☒ ☒
(346)

Note that $i f \quad x \quad i s \quad d - d i m e n s i o n a l ,$ then $\det \left( 2 \pi \Sigma \right) = \left( 2 \pi \right) ^ { d } \det \left( \Sigma \right) .$
Integration and normalization

$$\int \exp \left[ - \frac { 1 } { 2 } \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \Sigma ^ { - 1 } \left( \mathrm { x } - \mathrm { m } \right) \right] d \mathrm { x } = \sqrt { \det \left( 2 \pi \Sigma \right) }$$
$$\int \exp \left[ - \frac { 1 } { 2 } \mathrm { x } ^ { T } \Sigma ^ { - 1 } \mathrm { x } + \mathrm { m } ^ { T } \Sigma ^ { - 1 } \mathrm { x } \right] d \mathrm { x } = \sqrt { \det \left( 2 \pi \Sigma \right) } \exp \left[ \frac { 1 } { 2 } \mathrm { m } ^ { T } \Sigma ^ { - 1 } \mathrm { m } \right]$$
$$\int \exp \left[ - \frac { 1 } { 2 } \mathrm { x } ^ { T } \mathrm { A x } + \mathrm { c } ^ { T } \mathrm { x } \right] d \mathrm { x } = \sqrt { \det \left( 2 \pi \mathrm { A } ^ { - 1 } \right) } \exp \left[ \frac { 1 } { 2 } \mathrm { c } ^ { T } \mathrm { A } ^ { - T } \mathrm { c } \right]$$ ☒ ☒ ☒ ☒ ☒ ☒

If $\mathrm { X } = \left[ \mathrm { x } _ { 1 } \mathrm { x } _ { 2 } \ldots \mathrm { x } _ { n } \right]$ and $\mathrm { C } = \left[ \mathrm { c } _ { 1 } \mathrm { c } _ { 2 } \ldots \mathrm { c } _ { n } \right] ,$ then
☒ ☒

$$\int \exp \left[ - \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { X } ^ { T } \mathrm { A X } \right) + \mathrm { T r } \left( \mathrm { C } ^ { T } \mathrm { X } \right) \right] d \mathrm { X } = \sqrt { \det \left( 2 \pi \mathrm { A } ^ { - 1 } \right) } ^ { n } \exp \left[ \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { C } ^ { T } \mathrm { A } ^ { - 1 } \mathrm { C } \right) \right]$$ ☒ ☒ ☒

The derivatives of the density are

$$\frac { \partial p \left( x \right) } { \partial x } = - p \left( x \right) \Sigma ^ { - 1 } \left( x - m \right)$$
$$\frac { \partial ^ { 2 } p } { \partial \mathrm { x } \partial \mathrm { x } ^ { T } } = p \left( \mathrm { x } \right) \left( \Sigma ^ { - 1 } \left( \mathrm { x } - \mathrm { m } \right) \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \Sigma ^ { - 1 } - \Sigma ^ { - 1 } \right)$$
(347)
(348)


#### 8.1.2 Marginal Distribution

Assume $\mathrm { x } \sim \mathcal{N} _ { \mathrm { x } } \left( \mu , \Sigma \right)$ where

$$\mathrm { x } = \left[ \begin{array}{} \mathrm { x } _ { a } \\ \mathrm { x } _ { b } \end{array} \right] \quad \mu = \left[ \begin{array}{} \mu _ { a } \\ \mu _ { b } \end{array} \right] \quad \Sigma = \left[ \begin{array}{} \Sigma _ { a } & \Sigma _ { c } \\ \Sigma _ { c } ^ { T } & \Sigma _ { b } \end{array} \right]$$
(349)

then

$$p \left( \mathrm { x } _ { a } \right) = \mathcal{N} _ { \mathrm { x } _ { a } } \left( \mu _ { a } , \Sigma _ { a } \right)$$
$$p \left( \mathrm { x } _ { b } \right) = \mathcal{N} _ { \mathrm { x } _ { b } } \left( \mu _ { b } , \Sigma _ { b } \right)$$ ☒
(350)
(351)


#### 8.1.3 Conditional Distribution

Assume $\mathrm { x } \sim \mathcal{N} _ { \mathrm { x } } \left( \mu , \Sigma \right)$ where

$$\mathrm { x } = \left[ \begin{array}{} \mathrm { x } _ { a } \\ \mathrm { x } _ { b } \end{array} \right] \quad \mu = \left[ \begin{array}{} \mu _ { a } \\ \mu _ { b } \end{array} \right] \quad \Sigma = \left[ \begin{array}{} \Sigma _ { a } & \Sigma _ { c } \\ \Sigma _ { c } ^ { T } & \Sigma _ { b } \end{array} \right]$$
(352)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 40" -->
<!-- PageBreak -->

<!-- PageHeader="8 GAUSSIANS" -->
<!-- PageHeader="8.1 Basics" -->

then

$$p \left( \mathrm { x } _ { a } | \mathrm { x } _ { b } \right) = \mathcal{N} _ { \mathrm { x } _ { a } } \left( \widehat { \mu } _ { a } , \widehat { \Sigma } _ { a } \right) \left\{ \begin{array}{} \widehat { \mu } _ { a } = \mu _ { a } + \Sigma _ { c } \Sigma _ { b } ^ { - 1 } \left( \mathrm { x } _ { b } - \mu _ { b } \right) \\ \widehat { \Sigma } _ { a } = \Sigma _ { a } - \Sigma _ { c } \Sigma _ { b } ^ { - 1 } \Sigma _ { c } ^ { T } \end{array} \right.$$
$$p \left( \mathrm { x } _ { b } | \mathrm { x } _ { a } \right) = \mathcal{N} _ { \mathrm { x } _ { b } } \left( \widehat { \mu } _ { b } , \widehat { \Sigma } _ { b } \right) \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad$$
(353)
(354)


<table>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>


Note, that the covariance matrices are the Schur complement of the block ma-
trix, see 9.1.5 for details.


#### 8.1.4 Linear combination

Assume $\mathrm { x } \sim \mathcal{N} \left( \mathrm { m } _ { x } , \Sigma _ { x } \right)$ and $\mathrm { y } \sim \mathcal{N} \left( \mathrm { m } _ { y } , \Sigma _ { y } \right)$ then

$$\mathrm { A x } + \mathrm { B y } + \mathrm { c } \sim \mathcal{N} \left( \mathrm { A m } _ { x } + \mathrm { B m } _ { y } + \mathrm { c } , \mathrm { A } \Sigma _ { x } \mathrm { A } ^ { T } + \mathrm { B } \Sigma _ { y } \mathrm { B } ^ { T } \right)$$
(355)


#### 8.1.5 Rearranging Means

$$\mathcal{N} _ { \mathrm { A x } } \left[ \mathrm { m } , \Sigma \right] = \frac { \sqrt { \det \left( 2 \pi \left( \mathrm { A } ^ { T } \Sigma ^ { - 1 } \mathrm { A } \right) ^ { - 1 } \right) } } { \sqrt { \det \left( 2 \pi \Sigma \right) } } \mathcal{N} _ { \mathrm { x } } \left[ \mathrm { A } ^ { - 1 } \mathrm { m } , \left( \mathrm { A } ^ { T } \Sigma ^ { - 1 } \mathrm { A } \right) ^ { - 1 } \right]$$ ☒ ☒
(356)

If $\mathrm { A }$ is square and invertible, it simplifies to

$$\mathcal{N} _ { \mathrm { A x } } \left[ \mathrm { m } , \Sigma \right] = \frac { 1 } { | \det \left( \mathrm { A } \right) | } \mathcal{N} _ { \mathrm { x } } \left[ \mathrm { A } ^ { - 1 } \mathrm { m } , \left( \mathrm { A } ^ { T } \Sigma ^ { - 1 } \mathrm { A } \right) ^ { - 1 } \right]$$
(357)


#### 8.1.6 Rearranging into squared form

If $\mathrm { A }$ is symmetric, then

$$- \frac { 1 } { 2 } \mathrm { x } ^ { T } \mathrm { A x } + \mathrm { b } ^ { T } \mathrm { x } = - \frac { 1 } { 2 } \left( \mathrm { x } - \mathrm { A } ^ { - 1 } \mathrm { b } \right) ^ { T } \mathrm { A } \left( \mathrm { x } - \mathrm { A } ^ { - 1 } \mathrm { b } \right) + \frac { 1 } { 2 } \mathrm { b } ^ { T } \mathrm { A } ^ { - 1 } \mathrm { b }$$
$$- \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { X } ^ { T } \mathrm { A X } \right) + \mathrm { T r } \left( \mathrm { B } ^ { T } \mathrm { X } \right) = - \frac { 1 } { 2 } \mathrm { T r } \left[ \left( \mathrm { X } - \mathrm { A } ^ { - 1 } \mathrm { B } \right) ^ { T } \mathrm { A } \left( \mathrm { X } - \mathrm { A } ^ { - 1 } \mathrm { B } \right) \right] + \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { B } ^ { T } \mathrm { A } ^ { - 1 } \mathrm { B } \right)$$


#### 8.1.7 Sum of two squared forms

In vector formulation (assuming $\Sigma _ { 1 } ,$ $\Sigma _ { 2 }$ are symmetric)

$$- \frac { 1 } { 2 } \left( x - m _ { 1 } \right) ^ { T } \Sigma _ { 1 } ^ { - 1 } \left( x - m _ { 1 } \right)$$
$$- \frac { 1 } { 2 } \left( x - m _ { 2 } \right) ^ { T } \Sigma _ { 2 } ^ { - 1 } \left( x - m _ { 2 } \right)$$
$$= - \frac { 1 } { 2 } \left( \mathrm { x } - \mathrm { m } _ { c } \right) ^ { T } \Sigma _ { c } ^ { - 1 } \left( \mathrm { x } - \mathrm { m } _ { c } \right) + C$$
$$\Sigma _ { c } ^ { - 1 } = \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 }$$
$$\mathrm { m } _ { c } = \left( \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 } \right) ^ { - 1 } \left( \Sigma _ { 1 } ^ { - 1 } \mathrm { m } _ { 1 } + \Sigma _ { 2 } ^ { - 1 } \mathrm { m } _ { 2 } \right)$$
$$C = \frac { 1 } { 2 } \left( \mathrm { m } _ { 1 } ^ { T } \Sigma _ { 1 } ^ { - 1 } + \mathrm { m } _ { 2 } ^ { T } \Sigma _ { 2 } ^ { - 1 } \right) \left( \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 } \right) ^ { - 1 } \left( \Sigma _ { 1 } ^ { - 1 } \mathrm { m } _ { 1 } + \Sigma _ { 2 } ^ { - 1 } \mathrm { m } _ { 2 } \right) \left( 3 6 3 \right)$$
(358)
(359)
(360)
(361)
(362)

$$- \frac { 1 } { 2 } \left( \mathrm { m } _ { 1 } ^ { T } \Sigma _ { 1 } ^ { - 1 } \mathrm { m } _ { 1 } + \mathrm { m } _ { 2 } ^ { T } \Sigma _ { 2 } ^ { - 1 } \mathrm { m } _ { 2 } \right)$$
(364)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 41" -->
<!-- PageBreak -->

<!-- PageHeader="8 GAUSSIANS" -->
<!-- PageHeader="8.2 Moments" -->

In a trace formulation (assuming $\Sigma _ { 1 } ,$ $\Sigma _ { 2 }$ are symmetric)

$$- \frac { 1 } { 2 } \mathrm { T r } \left( \left( \mathrm { X } - \mathrm { M } _ { 1 } \right) ^ { T } \Sigma _ { 1 } ^ { - 1 } \left( \mathrm { X } - \mathrm { M } _ { 1 } \right) \right)$$
$$- \frac { 1 } { 2 } \mathrm { T r } \left( \left( \mathrm { X } - \mathrm { M } _ { 2 } \right) ^ { T } \Sigma _ { 2 } ^ { - 1 } \left( \mathrm { X } - \mathrm { M } _ { 2 } \right) \right)$$
$$= - \frac { 1 } { 2 } \mathrm { T r } \left[ \left( \mathrm { X } - \mathrm { M } _ { c } \right) ^ { T } \Sigma _ { c } ^ { - 1 } \left( \mathrm { X } - \mathrm { M } _ { c } \right) \right] + C$$
$$\Sigma _ { c } ^ { - 1 } = \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 }$$
$$\mathrm { M } _ { c } = \left( \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 } \right) ^ { - 1 } \left( \Sigma _ { 1 } ^ { - 1 } \mathrm { M } _ { 1 } + \Sigma _ { 2 } ^ { - 1 } \mathrm { M } _ { 2 } \right)$$
$$C = \frac { 1 } { 2 } \mathrm { T r } \left[ \left( \Sigma _ { 1 } ^ { - 1 } \mathrm { M } _ { 1 } + \Sigma _ { 2 } ^ { - 1 } \mathrm { M } _ { 2 } \right) ^ { T } \left( \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 } \right) ^ { - 1 } \left( \Sigma _ { 1 } ^ { - 1 } \mathrm { M } _ { 1 } + \Sigma _ { 2 } ^ { - 1 } \mathrm { M } _ { 2 } \right) \right]$$
$$- \frac { 1 } { 2 } \mathrm { T r } \left( \mathrm { M } _ { 1 } ^ { T } \Sigma _ { 1 } ^ { - 1 } \mathrm { M } _ { 1 } + \mathrm { M } _ { 2 } ^ { T } \Sigma _ { 2 } ^ { - 1 } \mathrm { M } _ { 2 } \right)$$ ☒ ☒
(365)
☒ ☒
(366)
☒
(367)
(368)
(369)
(370)


#### 8.1.8 Product of gaussian densities

Let $\mathcal{N} _ { \mathrm { x } } \left( \mathrm { m } , \Sigma \right)$ denote a density of $x ,$ then
☒

$$\mathcal{N} _ { \mathrm { x } } \left( \mathrm { m } _ { 1 } , \Sigma _ { 1 } \right) \cdot \mathcal{N} _ { \mathrm { x } } \left( \mathrm { m } _ { 2 } , \Sigma _ { 2 } \right) = c _ { c } \mathcal{N} _ { \mathrm { x } } \left( \mathrm { m } _ { c } , \Sigma _ { c } \right)$$
$$c _ { c } = \mathcal{N} _ { \mathrm { m } _ { 1 } } \left( \mathrm { m } _ { 2 } , \left( \Sigma _ { 1 } + \Sigma _ { 2 } \right) \right)$$
$$= \frac { 1 } { \sqrt { \det \left( 2 \pi \left( \Sigma _ { 1 } + \Sigma _ { 2 } \right) \right) } } \exp \left[ - \frac { 1 } { 2 } \left( \mathrm { m } _ { 1 } - \mathrm { m } _ { 2 } \right) ^ { T } \left( \Sigma _ { 1 } + \Sigma _ { 2 } \right) ^ { - 1 } \left( \mathrm { m } _ { 1 } - \mathrm { m } _ { 2 } \right) \right]$$
$$\mathrm { m } _ { c } = \left( \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 } \right) ^ { - 1 } \left( \Sigma _ { 1 } ^ { - 1 } \mathrm { m } _ { 1 } + \Sigma _ { 2 } ^ { - 1 } \mathrm { m } _ { 2 } \right)$$
$$\Sigma _ { c } = \left( \Sigma _ { 1 } ^ { - 1 } + \Sigma _ { 2 } ^ { - 1 } \right) ^ { - 1 }$$
(371)

but note that the product is not normalized as $a$ density of $x .$


### 8.2 Moments


#### 8.2.1 Mean and covariance of linear forms

First and second moments. Assume $\mathrm { x } \sim \mathcal{N} \left( \mathrm { m } , \Sigma \right)$

$$E \left( x \right) = m$$
$$\mathrm { C o v } \left( \mathrm { x } , \mathrm { x } \right) = \mathrm { V a r } \left( \mathrm { x } \right) = \Sigma = E \left( \mathrm { x x } ^ { T } \right) - E \left( \mathrm { x } \right) E \left( \mathrm { x } ^ { T } \right) = E \left( \mathrm { x x } ^ { T } \right) - \mathrm { m m } ^ { T }$$ ☒
(372)
(373)
☒ ☒

As for any other distribution is holds for gaussians that

$$E \left[ \mathrm { A x } \right] = \mathrm { A } E \left[ \mathrm { x } \right]$$
$$\mathrm { V a r } \left[ \mathrm { A x } \right] = \mathrm { A V a r } \left[ \mathrm { x } \right] \mathrm { A } ^ { T }$$
(374)
☒
(375)

$$\mathrm { C o v } \left[ \mathrm { A x } , \mathrm { B y } \right] = \mathrm { A C o v } \left[ \mathrm { x } , \mathrm { y } \right] \mathrm { B } ^ { T }$$
(376)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 42" -->
<!-- PageBreak -->

<!-- PageHeader="8 GAUSSIANS" -->
<!-- PageHeader="8.2 Moments" -->


#### 8.2.2 Mean and variance of square forms

Mean and variance of square forms: Assume $\mathrm { x } \sim \mathcal{N} \left( \mathrm { m } , \Sigma \right)$

$$E \left( \mathrm { x x } ^ { T } \right) = \Sigma + \mathrm { m m } ^ { T }$$

(377)
$$E \left[ \mathrm { x } ^ { T } \mathrm { A x } \right] = \mathrm { T r } \left( \mathrm { A } \Sigma \right) + \mathrm { m } ^ { T } \mathrm { A m }$$
$$\mathrm { V a r } \left( \mathrm { x } ^ { T } \mathrm { A x } \right) = \mathrm { T r } \left[ \mathrm { A } \Sigma \left( \mathrm { A } + \mathrm { A } ^ { T } \right) \Sigma \right] + \ldots .$$
(378)

$$+ \mathrm { m } ^ { T } \left( \mathrm { A } + \mathrm { A } ^ { T } \right) \Sigma \left( \mathrm { A } + \mathrm { A } ^ { T } \right) \mathrm { m }$$
$$E \left[ \left( \mathrm { x } - \mathrm { m } ^ { \prime } \right) ^ { T } \mathrm { A } \left( \mathrm { x } - \mathrm { m } ^ { \prime } \right) \right] = \left( \mathrm { m } - \mathrm { m } ^ { \prime } \right) ^ { T } \mathrm { A } \left( \mathrm { m } - \mathrm { m } ^ { \prime } \right) + \mathrm { T r } \left( \mathrm { A } \Sigma \right)$$
(379)
(380)

If $\Sigma = \sigma ^ { 2 } \mathrm { I }$ and $\mathrm { A }$ is symmetric, then

$$\mathrm { V a r } \left( \mathrm { x } ^ { T } \mathrm { A x } \right) = 2 \sigma ^ { 4 } \mathrm { T r } \left( \mathrm { A } ^ { 2 } \right) + 4 \sigma ^ { 2 } \mathrm { m } ^ { T } \mathrm { A } ^ { 2 } \mathrm { m }$$
(381)

Assume $\mathrm { x } \sim \mathcal{N} \left( 0 , \sigma ^ { 2 } \mathrm { I } \right)$ and $\mathrm { A }$ and $\mathrm { B }$ to be symmetric, then

$$\mathrm { C o v } \left( \mathrm { x } ^ { T } \mathrm { A x } , \mathrm { x } ^ { T } \mathrm { B x } \right) = 2 \sigma ^ { 4 } \mathrm { T r } \left( \mathrm { A B } \right)$$
(382)


#### 8.2.3 Cubic forms

Assume $x$ to be a stochastic vector with independent coordinates, mean m and
covariance $M$

$$E \left[ \mathrm { x b } ^ { T } \mathrm { x x } ^ { T } \right] = \mathrm { m b } ^ { T } \left( \mathrm { M } + \mathrm { m m } ^ { T } \right) + \left( \mathrm { M } + \mathrm { m m } ^ { T } \right) \mathrm { b m } ^ { T }$$
$$+ \mathrm { b } ^ { T } \mathrm { m } \left( \mathrm { M } - \mathrm { m m } ^ { T } \right)$$
(383)


#### 8.2.4 Mean of Quartic Forms

$$E \left[ \mathrm { x x } ^ { T } \mathrm { x x } ^ { T } \right] = 2 \left( \Sigma + \mathrm { m m } ^ { T } \right) ^ { 2 } + \mathrm { m } ^ { T } \mathrm { m } \left( \Sigma - \mathrm { m m } ^ { T } \right)$$
$$+ \mathrm { T r } \left( \Sigma \right) \left( \Sigma + \mathrm { m m } ^ { T } \right)$$
$$E \left[ \mathrm { x x } ^ { T } \mathrm { A x x } ^ { T } \right] = \left( \Sigma + \mathrm { m m } ^ { T } \right) \left( \mathrm { A } + \mathrm { A } ^ { T } \right) \left( \Sigma + \mathrm { m m } ^ { T } \right)$$
$$+ \mathrm { m } ^ { T } \mathrm { A m } \left( \Sigma - \mathrm { m m } ^ { T } \right) + \mathrm { T r } \left[ \mathrm { A } \Sigma \right] \left( \Sigma + \mathrm { m m } ^ { T } \right)$$
$$E \left[ \mathrm { x } ^ { T } \mathrm { x x } ^ { T } \mathrm { x } \right] = 2 \mathrm { T } \mathrm { r } \left( \Sigma ^ { 2 } \right) + 4 \mathrm { m } ^ { T } \Sigma \mathrm { m } + \left( \mathrm { T r } \left( \Sigma \right) + \mathrm { m } ^ { T } \mathrm { m } \right) ^ { 2 }$$

Ε[x] Axx7Bx] = $\mathrm { T r } \left[ \mathrm { A } \Sigma \left( \mathrm { B } + \mathrm { B } ^ { T } \right) \Sigma \right] + \mathrm { m } ^ { T } \left( \mathrm { A } + \mathrm { A } ^ { T } \right) \Sigma \left( \mathrm { B } + \mathrm { B } ^ { T } \right) \mathrm { n }$

$$+ \left( \mathrm { T r } \left( \mathrm { A } \Sigma \right) + \mathrm { m } ^ { T } \mathrm { A m } \right) \left( \mathrm { T r } \left( \mathrm { B } \Sigma \right) + \mathrm { m } ^ { T } \mathrm { B m } \right)$$

$$E \left[ a ^ { T } x b ^ { T } x c ^ { T } x d ^ { T } x \right]$$
$$= \quad \left( \mathrm { a } ^ { T } \left( \Sigma + \mathrm { m m } ^ { T } \right) \mathrm { b } \right) \left( \mathrm { c } ^ { T } \left( \Sigma + \mathrm { m m } ^ { T } \right) \mathrm { d } \right)$$
$$+ \left( a ^ { T } \left( \Sigma + m m ^ { T } \right) c \right) \left( b ^ { T } \left( \Sigma + m m ^ { T } \right) d \right)$$
$$+ \left( \mathrm { a } ^ { T } \left( \Sigma + \mathrm { m m } ^ { T } \right) \mathrm { d } \right) \left( \mathrm { b } ^ { T } \left( \Sigma + \mathrm { m m } ^ { T } \right) \mathrm { c } \right) - 2 \mathrm { a } ^ { T } \mathrm { m b } ^ { T } \mathrm { m c } ^ { T } \mathrm { m d } ^ { T } \mathrm { m }$$

$$E \left[ \left( A x + a \right) \left( B x + b \right) ^ { T } \left( C x + c \right) \left( D x + d \right) ^ { T } \right]$$
$$= \left[ \mathrm { A } \Sigma \mathrm { B } ^ { T } + \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { B m } + \mathrm { b } \right) ^ { T } \right] \left[ \mathrm { C } \Sigma \mathrm { D } ^ { T } + \left( \mathrm { C m } + \mathrm { c } \right) \left( \mathrm { D m } + \mathrm { d } \right) ^ { T } \right]$$
$$+ \left[ \mathrm { A } \Sigma \mathrm { C } ^ { T } + \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { C m } + \mathrm { c } \right) ^ { T } \right] \left[ \mathrm { B } \Sigma \mathrm { D } ^ { T } + \left( \mathrm { B m } + \mathrm { b } \right) \left( \mathrm { D m } + \mathrm { d } \right) ^ { T } \right]$$
$$+ \left( \mathrm { B m } + \mathrm { b } \right) ^ { T } \left( \mathrm { C m } + \mathrm { c } \right) \left[ \mathrm { A } \Sigma \mathrm { D } ^ { T } - \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { D m } + \mathrm { d } \right) ^ { T } \right]$$
$$+ \mathrm { T r } \left( \mathrm { B } \Sigma \mathrm { C } ^ { T } \right) \left[ \mathrm { A } \Sigma \mathrm { D } ^ { T } + \left( \mathrm { A m } + \mathrm { a } \right) \left( \mathrm { D m } + \mathrm { d } \right) ^ { T } \right]$$

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 43" -->
<!-- PageBreak -->

<!-- PageHeader="8 GAUSSIANS" -->
<!-- PageHeader="8.3 Miscellaneous" -->

$$E \left[ \left( A x + a \right) ^ { T } \left( B x + b \right) \left( C x + c \right) ^ { T } \left( D x + d \right) \right]$$

$$+ \left[ \left( \mathrm { A m } + \mathrm { a } \right) ^ { T } \mathrm { B } + \left( \mathrm { B m } + \mathrm { b } \right) ^ { T } \mathrm { A } \right] \Sigma \left[ \mathrm { C } ^ { T } \left( \mathrm { D m } + \mathrm { d } \right) + \mathrm { D } ^ { T } \left( \mathrm { C m } + \mathrm { c } \right) \right]$$

= $\mathrm { T r } \left[ \mathrm { A } \Sigma \left( \mathrm { C } ^ { T } \mathrm { D } + \mathrm { D } ^ { T } \mathrm { C } \right) \Sigma \mathrm { B } ^ { T } \right]$
$+ \left[ \mathrm { T r } \left( \mathrm { A } \Sigma \mathrm { B } ^ { T } \right) + \left( \mathrm { A m } + \mathrm { a } \right) ^ { T } \left( \mathrm { B m } + \mathrm { b } \right) \right] \left[ \mathrm { T r } \left( \mathrm { C } \Sigma \mathrm { D } ^ { T } \right) + \left( \mathrm { C m } + \mathrm { c } \right) ^ { T } \left( \mathrm { D m } + \mathrm { d } \right) \right]$
See [7].


#### 8.2.5 Moments

$$E \left[ x \right] = \sum _ { k } \rho _ { k } m _ { k }$$
$$\mathrm { C o v } \left( \mathrm { x } \right) = \sum _ { k } \sum _ { k ^ { \prime } } \rho _ { k } \rho _ { k ^ { \prime } } \left( \Sigma _ { k } + \mathrm { m } _ { k } \mathrm { m } _ { k } ^ { T } - \mathrm { m } _ { k } \mathrm { m } _ { k ^ { \prime } } ^ { T } \right)$$
(384)
☒
(385)


### 8.3 Miscellaneous


#### 8.3.1 Whitening

Assume $\mathrm { x } \sim \mathcal{N} \left( \mathrm { m } , \Sigma \right)$ then

$$\mathrm { z } = \Sigma ^ { - 1 / 2 } \left( \mathrm { x } - \mathrm { m } \right) \sim \mathcal{N} \left( 0 , \mathrm { I } \right)$$
(386)

Conversely having $\mathrm { z } \sim \mathcal{N} \left( 0 , \mathrm { I } \right)$ one can generate data $\mathrm { x } \sim \mathcal{N} \left( \mathrm { m } , \Sigma \right)$ by setting

$$\mathrm { x } = \Sigma ^ { 1 / 2 } \mathrm { z } + \mathrm { m } \sim \mathcal{N} \left( \mathrm { m } , \Sigma \right)$$
(387)

Note that $\Sigma ^ { 1 / 2 }$ means the matrix which fulfils $\Sigma ^ { 1 / 2 } \Sigma ^ { 1 / 2 } = \Sigma ,$ and that it exists
and is unique since $\Sigma$ is positive definite.


#### 8.3.2 The Chi-Square connection

Assume $\mathrm { x } \sim \mathcal{N} \left( \mathrm { m } , \Sigma \right)$ and $\mathrm { x }$ to be $n$ dimensional, then

$$z = \left( \mathrm { x } - \mathrm { m } \right) ^ { T } \Sigma ^ { - 1 } \left( \mathrm { x } - \mathrm { m } \right) \sim \chi _ { n } ^ { 2 }$$
(388)

where $\chi _ { n } ^ { 2 }$ denotes the Chi square distribution with n degrees of freedom.


#### 8.3.3 Entropy

Entropy of a D-dimensional gaussian

$$H \left( \mathrm { x } \right) = - \int \mathcal{N} \left( \mathrm { m } , \Sigma \right) \ln \mathcal{N} \left( \mathrm { m } , \Sigma \right) d \mathrm { x } = \ln \sqrt { \det \left( 2 \pi \Sigma \right) } + \frac { D } { 2 }$$ ☒
(389)


### 8.4 Mixture of Gaussians


#### 8.4.1 Density

The variable $\mathrm { x }$ is distributed as a mixture of gaussians if it has the density

$$p \left( \mathrm { x } \right) = \sum _ { k = 1 } ^ { K } \rho _ { k } \frac { 1 } { \sqrt { \det \left( 2 \pi \Sigma _ { k } \right) } } \exp \left[ - \frac { 1 } { 2 } \left( \mathrm { x } - \mathrm { m } _ { k } \right) ^ { T } \Sigma _ { k } ^ { - 1 } \left( \mathrm { x } - \mathrm { m } _ { k } \right) \right]$$ ☒
(390)

where pk sum to 1 and $\mathrm { t h e } \Sigma$ $\Sigma _ { k }$ all are positive definite.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 44" -->
<!-- PageBreak -->

<!-- PageHeader="8.4 Mixture of Gaussians" -->
<!-- PageHeader="8 GAUSSIANS" -->


#### 8.4.2 Derivatives

Defining $p \left( \mathrm { s } \right) = \sum _ { k } \rho _ { k } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { k } , \Sigma _ { k } \right)$ one get

$$\frac { \partial \ln p \left( \mathrm { s } \right) } { \partial \rho _ { j } } = \frac { \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { k } , \Sigma _ { k } \right) } \frac { \partial } { \partial \rho _ { j } } \ln \left[ \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) \right]$$
(391)

$$= \frac { \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { k } , \Sigma _ { k } \right) } \frac { 1 } { \rho _ { j } }$$
$$\frac { \partial \ln p \left( \mathrm { s } \right) } { \partial \mu _ { j } } = \frac { \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { k } , \Sigma _ { k } \right) } \frac { \partial } { \partial \mu _ { j } } \ln \left[ \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) \right]$$
$$= \frac { \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { k } , \Sigma _ { k } \right) } \left[ \Sigma _ { j } ^ { - 1 } \left( \mathrm { s } - \mu _ { j } \right) \right]$$
$$\frac { \partial \ln p \left( \mathrm { s } \right) } { \partial \Sigma _ { j } } = \frac { \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { k } , \Sigma _ { k } \right) } \frac { \partial } { \partial \Sigma _ { j } } \ln \left[ \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) \right]$$
$$= \frac { \rho _ { j } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { j } , \Sigma _ { j } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { \mathrm { s } } \left( \mu _ { k } , \Sigma _ { k } \right) } \frac { 1 } { 2 } \left[ - \Sigma _ { j } ^ { - 1 } + \Sigma _ { j } ^ { - 1 } \left( \mathrm { s } - \mu _ { j } \right) \left( \mathrm { s } - \mu _ { j } \right) ^ { T } \Sigma _ { j } ^ { - } \right\} _ { j } ^ { - } \left( 3 6 \right)$$
(392)
(393)
(394)
(395)

But $\rho _ { k }$ and $\Sigma _ { k }$ needs to be constrained.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 45" -->
<!-- PageBreak -->

<!-- PageHeader="9 SPECIAL MATRICES" -->


## 9 Special Matrices


### 9.1 Block matrices

Let $\mathrm { A } _ { i j }$ denote the ijth block of $\mathrm { A } .$


#### 9.1.1 Multiplication

Assuming the dimensions of the blocks matches we have

$$\left[ \begin{array}{} \mathrm { A } _ { 1 1 } & \mathrm { A } _ { 1 2 } \\ \mathrm { A } _ { 2 1 } & \mathrm { A } _ { 2 2 } \end{array} \right] \left[ \begin{array}{} \mathrm { B } _ { 1 1 } & \mathrm { B } _ { 1 2 } \\ \mathrm { B } _ { 2 1 } & \mathrm { B } _ { 2 2 } \end{array} \right] = \left[ \begin{array}{} \mathrm { A } _ { 1 1 } \mathrm { B } _ { 1 1 } + \mathrm { A } _ { 1 2 } \mathrm { B } _ { 2 1 } & \mathrm { A } _ { 1 1 } \mathrm { B } _ { 1 2 } + \mathrm { A } _ { 1 2 } \mathrm { B } _ { 2 2 } \\ \mathrm { A } _ { 2 1 } \mathrm { B } _ { 1 1 } + \mathrm { A } _ { 2 2 } \mathrm { B } _ { 2 1 } & \mathrm { A } _ { 2 1 } \mathrm { B } _ { 1 2 } + \mathrm { A } _ { 2 2 } \mathrm { B } _ { 2 2 } \end{array} \right]$$


#### 9.1.2 The Determinant

The determinant can be expressed as by the use of

$$\mathrm { C } _ { 1 } = \mathrm { A } _ { 1 1 } - \mathrm { A } _ { 1 2 } \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 }$$
$$\mathrm { C } _ { 2 } = \mathrm { A } _ { 2 2 } - \mathrm { A } _ { 2 1 } \mathrm { A } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 2 }$$
(397)
(398)

as

$$\det \left( \left[ \frac { \mathrm { A } _ { 1 1 } } { \mathrm { A } _ { 2 1 } } | \frac { \mathrm { A } _ { 1 2 } } { \mathrm { A } _ { 2 2 } } \right] \right) = \det \left( \mathrm { A } _ { 2 2 } \right) \cdot \det \left( \mathrm { C } _ { 1 } \right) = \det \left( \mathrm { A } _ { 1 1 } \right) \cdot \det \left( \mathrm { C } _ { 2 } \right)$$


#### 9.1.3 The Inverse

The inverse can be expressed as by the use of

$$\mathrm { C } _ { 1 } = \mathrm { A } _ { 1 1 } - \mathrm { A } _ { 1 2 } \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 }$$
$$\mathrm { C } _ { 2 } = \mathrm { A } _ { 2 2 } - \mathrm { A } _ { 2 1 } \mathrm { A } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 2 }$$
(399)
(400)

as

$$\left[ \frac { \mathrm { A } _ { 1 1 } | \mathrm { A } _ { 1 2 } } { \mathrm { A } _ { 2 1 } | \mathrm { A } _ { 2 2 } } \right] ^ { - 1 } = \left[ \frac { \mathrm { C } _ { 1 } ^ { - 1 } } { - \mathrm { C } _ { 2 } ^ { - 1 } \mathrm { A } _ { 2 1 } \mathrm { A } _ { 1 1 } ^ { - 1 } } | \frac { - \mathrm { A } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 2 } \mathrm { C } _ { 2 } ^ { - 1 } } { \mathrm { C } _ { 2 } ^ { - 1 } } \right]$$
$$= \left[ \frac { \mathrm { A } _ { 1 1 } ^ { - 1 } + \mathrm { A } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 2 } \mathrm { C } _ { 2 } ^ { - 1 } \mathrm { A } _ { 2 1 } \mathrm { A } _ { 1 1 } ^ { - 1 } } { - \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 } \mathrm { C } _ { 1 } ^ { - 1 } } | _ { \mathrm { A } _ { 2 2 } ^ { - 1 } + \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 } \mathrm { C } _ { 1 } ^ { - 1 } \mathrm { A } _ { 1 2 } \mathrm { A } _ { 2 2 } ^ { - 1 } } \right]$$
]


#### 9.1.4 Block diagonal

For block diagonal matrices we have

$$\left[ \begin{array}{} { c | c } { A _ { 1 1 } } & { 0 } \\ 0 & { A _ { 2 2 } } \end{array} \right] ^ { - 1 } = \left[ \frac { \left( A _ { 1 1 } \right) ^ { - 1 } } { 0 } | \frac { 0 } { \left( A _ { 2 2 } \right) ^ { - 1 } } \right]$$
$$\det \left( \left[ \begin{array}{} \frac { \mathrm { A } _ { 1 1 } } { 0 } & \frac { 0 } { \mathrm { A } _ { 2 2 } } \end{array} \right] \right) = \det \left( \mathrm { A } _ { 1 1 } \right) \cdot \det \left( \mathrm { A } _ { 2 2 } \right)$$
(401)
(402)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 46" -->
<!-- PageBreak -->

<!-- PageHeader="9 SPECIAL MATRICES" -->
<!-- PageHeader="9.2 Discrete Fourier Transform Matrix, The" -->


#### 9.1.5 Schur complement

Regard the matrix

$$\begin{array}{} { | c | c | c | } A _ { 1 1 } & { A _ { 1 2 } } \\ A _ { 2 1 } & { A _ { 2 2 } } \end{array}$$

1

The Schur complement of block $A _ { 1 1 }$ of the matrix above is the matrix (denoted
$\mathrm { C } _ { 2 }$ in the text above)

$$\mathrm { A } _ { 2 2 } - \mathrm { A } _ { 2 1 } \mathrm { A } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 2 }$$

The Schur complement of block $\mathrm { A } _ { 2 2 }$ of the matrix above is the matrix (denoted
$\mathrm { C } _ { 1 }$ in the text above)

$$\mathrm { A } _ { 1 1 } - \mathrm { A } _ { 1 2 } \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 }$$

Using the Schur complement, one can rewrite the inverse of a block matrix

$A _ { 1 1 }$

$\mathrm { A } _ { 1 2 }$

-1
$\mathrm { A } _ { 2 2 }$
1

$A _ { 2 }$

$$\left. = \left[ \frac { \mathrm { I } } { - \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 } } \right] \frac { 0 } { \mathrm { I } } \right] \left[ \frac { \left( \mathrm { A } _ { 1 1 } - \mathrm { A } _ { 1 2 } \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 } \right) ^ { - 1 } } { 0 } | \frac { \mathrm { 0 } } { \mathrm { A } _ { 2 2 } ^ { - 1 } } \right] \left[ \frac { \mathrm { I } } { 0 } | \frac { \mathrm { I } } { 0 } \frac { \mathrm { A } _ { 2 2 } ^ { - 1 } } { \mathrm { I } } \right]$$

The Schur complement is useful when solving linear systems of the form

$$\left[ \frac { \mathrm { A } _ { 1 1 } } { \mathrm { A } _ { 2 1 } } | \frac { \mathrm { A } _ { 1 2 } } { \mathrm { A } _ { 2 2 } } \right] \left[ \frac { \mathrm { x } _ { 1 } } { \mathrm { x } _ { 2 } } \right] = \left[ \frac { \mathrm { b } _ { 1 } } { \mathrm { b } _ { 2 } } \right.$$

which has the following equation for $\mathrm { x } _ { 1 }$

$$\left( \mathrm { A } _ { 1 1 } - \mathrm { A } _ { 1 2 } \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 1 } \right) \mathrm { x } _ { 1 } = \mathrm { b } _ { 1 } - \mathrm { A } _ { 1 2 } \mathrm { A } _ { 2 2 } ^ { - 1 } \mathrm { b } _ { 2 }$$

When the appropriate inverses exists, this can be solved for $\mathrm { x } _ { 1 }$ which can then
be inserted in the equation for $\mathrm { x } _ { 2 }$ to solve for $\mathrm { x } _ { 2 } .$


### 9.2 Discrete Fourier Transform Matrix, The

The DFT matrix is an $N \times N$ symmetric matrix $\mathrm { W } _ { N } ,$ where the $k ,$ $n$ nth element
is given by

$$W _ { N } ^ { k n } = e ^ { \frac { - j 2 \pi k n } { N } }$$
(403)

Thus the discrete Fourier transform (DFT) can be expressed as

$$X \left( k \right) = \sum _ { n = 0 } ^ { N - 1 } x \left( n \right) W _ { N } ^ { k n } .$$
(404)

Likewise the inverse discrete Fourier transform (IDFT) can be expressed as

$$x \left( n \right) = \frac { 1 } { N } \sum _ { k = 0 } ^ { N - 1 } X \left( k \right) W _ { N } ^ { - k n } .$$
(405)

The DFT of the vector $\mathrm { x } = \left[ x \left( 0 \right) , x \left( 1 \right) , \cdots , x \left( N - 1 \right) \right] ^ { T }$ can be written in matrix
form as

$$\mathrm { X } = \mathrm { W } _ { N } \mathrm { x } ,$$
(406)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 47" -->
<!-- PageBreak -->

<!-- PageHeader="9.3 Hermitian Matrices and skew-Hermitian" -->
<!-- PageHeader="9 SPECIAL MATRICES" -->

where $\mathrm { X } = \left[ X \left( 0 \right) , X \left( 1 \right) , \cdots , x \left( N - 1 \right) \right] ^ { T } .$ The IDFT is similarly given as

$$\mathrm { x } = \mathrm { W } _ { N } ^ { - 1 } \mathrm { X } .$$
(407)

Some properties of $\mathrm { W } _ { N }$ exist:

$$\mathrm { W } _ { N } ^ { - 1 } = \frac { 1 } { N } \mathrm { W } _ { N } ^ { * }$$
$$\mathrm { W } _ { N } \mathrm { W } _ { N } ^ { * } = N \mathrm { I }$$
$$\mathrm { W } _ { N } ^ { * } = \mathrm { W } _ { N } ^ { H }$$
(408)
(409)
(410)

If $W _ { N } = e ^ { \frac { - j 2 \pi } { N } } ,$ then [23]

$$W _ { N } ^ { m + N / 2 } = - W _ { N } ^ { m }$$
(411)

Notice, the DFT matrix is a Vandermonde Matrix.

The following important relation between the circulant matrix and the dis-
crete Fourier transform (DFT) exists

$$\mathrm { T } _ { C } = \mathrm { W } _ { N } ^ { - 1 } \left( \mathrm { I } \circ \left( \mathrm { W } _ { N } \mathrm { t } \right) \right) \mathrm { W } _ { N } ,$$
(412)

where $\mathrm { t } = \left[ t _ { 0 } , t _ { 1 } , \cdots , t _ { n - 1 } \right] ^ { T }$ is the first row of $\mathrm { T } _ { C } .$


### 9.3 Hermitian Matrices and skew-Hermitian

A matrix $\mathrm { A } \in \mathbb{C} ^ { m \times n }$ is called Hermitian if

$$\mathrm { A } ^ { H } = \mathrm { A }$$
For real valued matrices, Hermitian and symmetric matrices are equivalent.
(413)

A is Hermitian > x Ax ER, $\forall \mathrm { x } \in \mathbb{C} ^ { n \times 1 }$
A is Hermitian > eig(A) ER

(414)
$$\mathrm { A } = \mathrm { B } + i \mathrm { C }$$

Note that

where B, $\mathrm { C }$ are hermitian, then

$$\mathrm { B } = \frac { \mathrm { A } + \mathrm { A } ^ { H } } { 2 } , \quad \mathrm { C } = \frac { \mathrm { A } - \mathrm { A } ^ { H } } { 2 i }$$


#### 9.3.1 Skew-Hermitian

A matrix $\mathrm { A }$ is called skew-hermitian if

$$\mathrm { A } = - \mathrm { A } ^ { H }$$
For real valued matrices, skew-Hermitian and skew-symmetric matrices are
(416)
(417)

equivalent.


<table>
<tr>
<td>A Hermitian &gt;</td>
<td>iA is skew-hermitian</td>
<td>(415)</td>
</tr>
<tr>
<td>A skew-Hermitian &gt;</td>
<td>x"Ay = - x"AHy, Vx, y</td>
<td></td>
</tr>
<tr>
<td colspan="2">A skew-Hermitian &gt; eig(A) = il, $\lambda \in \mathbb{R}$</td>
<td></td>
</tr>
</table>


<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 48" -->
<!-- PageBreak -->

<!-- PageHeader="9 SPECIAL MATRICES" -->
<!-- PageHeader="9.4 Idempotent Matrices" -->


### 9.4 Idempotent Matrices

A matrix A is idempotent if

$A A = A$

Idempotent matrices $\mathrm { A }$ and $\mathrm { B } ,$ have the following properties

$\mathrm { f o r } n = 1 , 2 , 3 , . ,$ ...
(418)

$A$ = A,
$\mathrm { I } - \mathrm { A }$
is idempotent
(419)

$A ^ { H }$
is idempotent
(420)

$\mathrm { I } - \mathrm { A } ^ { H }$
is idempotent
(421)
$I f \quad A B = B A$ => AB is idempotent
(422)

$$\mathrm { r a n k } \left( \mathrm { A } \right) \quad = \quad \mathrm { T r } \left( \mathrm { A } \right)$$
(423)
(424)

$$\mathrm { A } \left( \mathrm { I } - \mathrm { A } \right) = 0$$
$$\left( \mathrm { I } - \mathrm { A } \right) \mathrm { A } \quad = \quad 0$$
$$f \left( s \mathrm { I } + t \mathrm { A } \right) = \left( \mathrm { I } - \mathrm { A } \right) f \left( s \right) + \mathrm { A } f \left( s + t \right)$$
(425)

$\mathrm { A } ^ { + } = \mathrm { A }$
(426)
(427)

Note that A - I is not necessarily idempotent.


#### 9.4.1 Nilpotent

A matrix A is nilpotent if

$$\mathrm { A } ^ { 2 } = 0$$

A nilpotent matrix has the following property:

$$f \left( s \mathrm { I } + t \mathrm { A } \right) = \mathrm { I } f \left( s \right) + t \mathrm { A } f ^ { \prime } \left( s \right)$$
(428)


#### 9.4.2 Unipotent

A matrix A is unipotent if

$$\mathrm { A A } = \mathrm { I }$$

A unipotent matrix has the following property:

$$f \left( s \mathrm { I } + t \mathrm { A } \right) = \left[ \left( \mathrm { I } + \mathrm { A } \right) f \left( s + t \right) + \left( \mathrm { I } - \mathrm { A } \right) f \left( s - t \right) \right] / 2$$
(429)


### 9.5 Orthogonal matrices

If a square matrix $\mathrm { Q }$ is orthogonal, if and only if,

$$\mathrm { Q } ^ { T } \mathrm { Q } = \mathrm { Q Q } ^ { T } = \mathrm { I }$$

and then $\mathrm { Q }$ has the following properties

· Its eigenvalues are placed on the unit circle.

· Its eigenvectors are unitary, i.e. have length one.

. The inverse of an orthogonal matrix is orthogonal too.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 49" -->
<!-- PageBreak -->

<!-- PageHeader="9.6 Positive Definite and Semi-definite Matrices" -->
<!-- PageHeader="9 SPECIAL MATRICES" -->

Basic properties for the orthogonal matrix $\mathrm { Q }$

$$\mathrm { Q } ^ { - 1 } = \mathrm { Q } ^ { T }$$
$$Q ^ { - T } = Q$$
$$\mathrm { Q Q } ^ { T } = \mathrm { I }$$
$$\mathrm { Q } ^ { T } \mathrm { Q } = \mathrm { I }$$
$$\det \left( \mathrm { Q } \right) = \pm 1$$


#### 9.5.1 Ortho-Sym

A matrix $\mathrm { Q } _ { + }$ which simultaneously is orthogonal and symmetric is called an
ortho-sym matrix [20]. Hereby

$$\mathrm { Q } _ { + } ^ { T } \mathrm { Q } _ { + } = \mathrm { I }$$
$$\mathrm { Q } _ { + } = \mathrm { Q } _ { + } ^ { T }$$
(430)
(431)

The powers of an ortho-sym matrix are given by the following rule

$$\mathrm { Q } _ { + } ^ { k } = \frac { 1 + \left( - 1 \right) ^ { k } } { 2 } \mathrm { I } + \frac { 1 + \left( - 1 \right) ^ { k + 1 } } { 2 } \mathrm { Q } _ { + }$$
$$= \frac { 1 + \cos \left( k \pi \right) } { 2 } \mathrm { I } + \frac { 1 - \cos \left( k \pi \right) } { 2 } \mathrm { Q } _ { + }$$
(432)
(433)


#### 9.5.2 Ortho-Skew

A matrix which simultaneously is orthogonal and antisymmetric is called an
ortho-skew matrix [20]. Hereby

$$\mathrm { Q } _ { - } ^ { H } \mathrm { Q } _ { - } = \mathrm { I }$$
(434)

$$\mathrm { Q } _ { - } = - \mathrm { Q } _ { - } ^ { H }$$
(435)

The powers of an ortho-skew matrix are given by the following rule

$$\mathrm { Q } _ { - } ^ { k } = \frac { i ^ { k } + \left( - i \right) ^ { k } } { 2 } \mathrm { I } - i \frac { i ^ { k } - \left( - i \right) ^ { k } } { 2 } \mathrm { Q }$$
(436)

$$= \cos \left( k \frac { \pi } { 2 } \right) I + \sin \left( k \frac { \pi } { 2 } \right) Q _ { - }$$
(437)


#### 9.5.3 Decomposition

A square matrix A can always be written as a sum of a symmetric A+ and an
antisymmetric matrix A_

$$\mathrm { A } = \mathrm { A } _ { + } + \mathrm { A }$$
(438)


### 9.6 Positive Definite and Semi-definite Matrices


#### 9.6.1 Definitions

A matrix A is positive definite if and only if

$$\mathrm { x } ^ { T } \mathrm { A x } > 0 , \quad \forall \mathrm { x } \neq 0$$ ☒
(439)

A matrix A is positive semi-definite if and only if

$$\mathrm { x } ^ { T } \mathrm { A x } > 0 , \quad \forall \mathrm { x }$$
(440)

Note that if $\mathrm { A }$ is positive definite, then $\mathrm { A }$ is also positive semi-definite.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 50" -->
<!-- PageBreak -->

<!-- PageHeader="9.6 Positive Definite and Semi-definite Matrices" -->
<!-- PageHeader="9 SPECIAL MATRICES" -->


#### 9.6.2 Eigenvalues

The following holds with respect to the eigenvalues:

$$\Leftrightarrow \quad \mathrm { e i g } \left( \frac { \mathrm { A } + \mathrm { A } ^ { H } } { 2 } \right) > 0$$
$$\begin{array}{} \text { A pos. def. } \quad \Leftrightarrow \quad \mathrm { e i g } \left( \frac { \mathrm { A } + \mathrm { A } ^ { H } } { 2 } \right) > 0 \\ \text { A pos. semi-def. } \quad \Leftrightarrow \quad \mathrm { e i g } \left( \frac { \mathrm { A } + \mathrm { A } ^ { H } } { 2 } \right) \geq 0 \end{array}$$

(441)


#### 9.6.3 Trace

The following holds with respect to the trace:

$$\text { A pos. semi-def. } \quad \Rightarrow \quad \mathrm { T r } \left( \mathrm { A } \right) \geq 0$$
(442)


#### 9.6.4 Inverse

If A is positive definite, then A is invertible and $\mathrm { A } ^ { - 1 }$ is also positive definite.


#### 9.6.5 Diagonal

If $\mathrm { A }$ is positive definite, then $A _ { i i } > 0 ,$ $\forall i$


#### 9.6.6 Decomposition I

The matrix $\mathrm { A }$ is positive semi-definite of rank $r \Leftrightarrow$ there exists a matrix $\mathrm { B }$ of
rank r such that $\mathrm { A } = \mathrm { B B } ^ { T }$

The matrix $\mathrm { A }$ is positive definite $\Leftrightarrow$ there exists an invertible matrix $\mathrm { B }$ such
that $\mathrm { A } = \mathrm { B B } ^ { T }$


### 9.6.7 Decomposition $\mathrm { I I }$

Assume $\mathrm { A }$ is an $n \times n$ positive semi-definite, then there exists an $n \times r$ matrix
$\mathrm { B }$ of rank $\mathrm { r }$ such that $\mathrm { B } ^ { T } \mathrm { A B } = \mathrm { I } .$


### 9.6.8 Equation with zeros

Assume $\mathrm { A }$ is positive semi-definite, then $\mathrm { X } ^ { T } \mathrm { A X } = 0 \quad \Rightarrow \quad \mathrm { A X } = 0$
☒


### 9.6.9 Rank of product

Assume $\mathrm { A }$ is positive definite, then $\mathrm { r a n k } \left( \mathrm { B A B } ^ { T } \right) = \mathrm { r a n k } \left( \mathrm { B } \right)$


### 9.6.10 Positive definite property

If $\mathrm { A }$ is $n \times n$ positive definite and $\mathrm { B }$ is $r \times n$ of rank r, then $\mathrm { B A B } ^ { T }$ is positive
definite.


#### 9.6.11 Outer Product

If $\mathrm { X }$ is $n \times r ,$ where $n \leq r$ and $\mathrm { r a n k } \left( \mathrm { X } \right) = n ,$ then $\mathrm { X X } ^ { T }$ is positive definite.
☒ ☒

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 51" -->
<!-- PageBreak -->

<!-- PageHeader="9 SPECIAL MATRICES" -->
<!-- PageHeader="9.7 Singleentry Matrix, The" -->


#### 9.6.12 Small pertubations

If $\mathrm { A }$ is positive definite and B is symmetric, then $\mathrm { A } - t \mathrm { B }$ is positive definite for
sufficiently small t.


#### 9.6.13 Hadamard inequality

If $\mathrm { A }$ is a positive definite or semi-definite matrix, then

$$\det \left( \mathrm { A } \right) \leq \prod _ { i } A _ { i i }$$

See [15, pp.477]


#### 9.6.14 Hadamard product relation

Assume that $\mathrm { P } = \mathrm { A A } ^ { T }$ and $\mathrm { Q } = \mathrm { B B } ^ { T }$ are semi positive definite matrices, it
then holds that

$$\mathrm { P } \circ \mathrm { Q } = \mathrm { R R } ^ { T }$$

where the columns of $\mathrm { R }$ are constructed as follows: $\mathrm { r } _ { i + \left( j - 1 \right) N _ { A } } = \mathrm { a } _ { i } \circ \mathrm { b } _ { j } ,$ for
$i = 1 , 2 , \ldots , N _ { A }$ and $j = 1 , 2 , \ldots , N _ { B } .$ The result is unpublished, but reported by
Pavel Sakov and Craig Bishop.


### 9.7 Singleentry Matrix, The


#### 9.7.1 Definition

The single-entry matrix $\mathrm { J } ^ { i j } \in \mathbb{R} ^ { n \times n }$ is defined as the matrix which is zero
everywhere except in the entry $\left( , j \right)$ in which it is 1. In a $4 \times 4$ example one
might have

$$J ^ { 2 3 } = \left[ \begin{array}{} { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right]$$
(443)

The single-entry matrix is very useful when working with derivatives of expres-
sions involving matrices.


#### 9.7.2 Swap and Zeros

Assume $\mathrm { A }$ to be $n \times m$ and $\mathrm { J } ^ { i j }$ to be $m \times p$

$$\mathrm { A J } ^ { i j } = \left[ \begin{array}{} 0 & 0 & \ldots & \mathrm { A } _ { i } & \ldots & 0 \end{array} \right.$$
(444)

i.e. an $n \times p$ matrix of zeros with the i.th column of $\mathrm { A }$ in place of the j.th
column. Assume $\mathrm { A }$ to be $n \times m$ and $\mathrm { J } ^ { i j }$ to be $p \times n$

$$\mathrm { J } ^ { i j } \mathrm { A } = \left[ \begin{array}{} 0 \\ \vdots \\ 0 \\ \mathrm { A } _ { j } \\ 0 \end{array} \right]$$
(445)

.

0

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 52" -->
<!-- PageBreak -->

<!-- PageHeader="9 SPECIAL MATRICES" -->
<!-- PageHeader="9.7 Singleentry Matrix, The" -->

i.e. an $p \times m$ matrix of zeros with the j.th row of $\mathrm { A }$ in the placed of the i.th
row.


#### 9.7.3 Rewriting product of elements

$$A _ { k i } B _ { j l } = \left( \mathrm { A e } _ { i } \mathrm { e } _ { j } ^ { T } \mathrm { B } \right) _ { k l } = \left( \mathrm { A J } ^ { i j } \mathrm { B } \right) _ { k l }$$
(446)

$$A _ { i k } B _ { l j } = \left( \mathrm { A } ^ { T } \mathrm { e } _ { i } \mathrm { e } _ { i } ^ { T } \mathrm { B } ^ { T } \right) _ { k l } = \left( \mathrm { A } ^ { T } \mathrm { J } ^ { i j } \mathrm { B } ^ { T } \right) _ { k l }$$
$$A _ { i k } B _ { j l } = \left( \mathrm { A } ^ { T } \mathrm { e } _ { i } \mathrm { e } _ { j } ^ { T } \mathrm { B } \right) _ { k l } = \left( \mathrm { A } ^ { T } \mathrm { J } ^ { i j } \mathrm { B } \right) _ { k l }$$
$$A _ { k i } B _ { l j } = \left( \mathrm { A e } _ { i } \mathrm { e } _ { i } ^ { T } \mathrm { B } ^ { T } \right) _ { k l } = \left( \mathrm { A J } ^ { i j } \mathrm { B } ^ { T } \right) _ { k l }$$
(447)
(448)
(449)


#### 9.7.4 Properties of the Singleentry Matrix

If $i = j$

$$\mathrm { J } ^ { i j } \mathrm { J } ^ { i j } = \mathrm { J } ^ { i j } \quad \left( \mathrm { J } ^ { i j } \right) ^ { T } \left( \mathrm { J } ^ { i j } \right) ^ { T } = \mathrm { J } ^ { i j }$$
$$\mathrm { J } ^ { i j } \left( \mathrm { J } ^ { i j } \right) ^ { T } = \mathrm { J } ^ { i j } \quad \left( \mathrm { J } ^ { i j } \right) ^ { T } \mathrm { J } ^ { i j } = \mathrm { J } ^ { i j }$$

If $i \neq j$

$$\mathrm { J } ^ { i j } \mathrm { J } ^ { i j } = 0 \quad \left( \mathrm { J } ^ { i j } \right) ^ { T } \left( \mathrm { J } ^ { i j } \right) ^ { T } = 0$$
$$\mathrm { J } ^ { i j } \left( \mathrm { J } ^ { i j } \right) ^ { T } = \mathrm { J } ^ { i i } \quad \left( \mathrm { J } ^ { i j } \right) ^ { T } \mathrm { J } ^ { i j } = \mathrm { J } ^ { j j }$$


#### 9.7.5 The Singleentry Matrix in Scalar Expressions

Assume $A$ is $n \times m$ and $\mathrm { J }$ is $m \times n ,$ then

$$\mathrm { T r } \left( \mathrm { A J } ^ { i j } \right) = \mathrm { T r } \left( \mathrm { J } ^ { i j } \mathrm { A } \right) = \left( \mathrm { A } ^ { T } \right) _ { i j }$$
(450)

Assume $\mathrm { A }$ is $n \times n ,$ J is $n \times m$ and $\mathrm { B }$ is $m \times n ,$ then

$$\mathrm { T r } \left( \mathrm { A J } ^ { i j } \mathrm { B } \right) = \left( \mathrm { A } ^ { T } \mathrm { B } ^ { T } \right) _ { i j }$$
$$\mathrm { T r } \left( \mathrm { A J } ^ { j i } \mathrm { B } \right) = \left( \mathrm { B A } \right) _ { i j }$$
$$\mathrm { T r } \left( \mathrm { A J } ^ { i j } \mathrm { J } ^ { i j } \mathrm { B } \right) = \mathrm { d i a g } \left( \mathrm { A } ^ { T } \mathrm { B } ^ { T } \right) _ { i j }$$
(451)
(452)
(453)

Assume $\mathrm { A }$ is $n \times n$ n, $\mathrm { J } ^ { i j }$ is $n \times m \mathrm { B }$ Bis $m \times n ,$ then

$$\mathrm { x } ^ { T } \mathrm { A J } ^ { i j } \mathrm { B x } = \left( \mathrm { A } ^ { T } \mathrm { x x } ^ { T } \mathrm { B } ^ { T } \right) _ { i j }$$
(454)

$$\mathrm { x } ^ { T } \mathrm { A J } ^ { i j } \mathrm { J } ^ { i j } \mathrm { B x } = \mathrm { d i a g } \left( \mathrm { A } ^ { T } \mathrm { x x } ^ { T } \mathrm { B } ^ { T } \right) _ { i j }$$
(455)


#### 9.7.6 Structure Matrices

The structure $m a t r i x \quad i s \quad d e f i n e d \quad b y$

$$\frac { \partial A } { \partial A _ { i j } } = S ^ { i j }$$
(456)

If A has no special structure then

$$\mathrm { S } ^ { i j } = \mathrm { J } ^ { i j }$$
(457)

If $\mathrm { A }$ is symmetric then

$$\mathrm { S } ^ { i j } = \mathrm { J } ^ { i j } + \mathrm { J } ^ { j i } - \mathrm { J } ^ { i j } \mathrm { J } ^ { i j }$$
(458)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 53" -->
<!-- PageBreak -->

<!-- PageHeader="9.8 Symmetric, Skew-symmetric/Antisymmetric 9 SPECIAL MATRICES" -->


### 9.8 Symmetric, Skew-symmetric/ Antisymmetric


#### 9.8.1 Symmetric

The matrix A is said to be symmetric if

$$A = A ^ { T }$$
(459)

Symmetric matrices have many important properties, e.g. that their eigenvalues
are real and eigenvectors orthogonal.


#### 9.8.2 Skew-symmetric/Antisymmetric

The antisymmetric matrix is also known as the skew symmetric matrix. It $h a s$
the following property from which it is defined

$$\mathrm { A } = - \mathrm { A } ^ { T }$$
(460)

Hereby, it can be seen that the antisymmetric matrices always have a zero
diagonal. The $n \times n$ antisymmetric matrices also have the following properties.

$$\det \left( \mathrm { A } ^ { T } \right) = \det \left( - \mathrm { A } \right) = \left( - 1 \right) ^ { n } \det \left( \mathrm { A } \right)$$
$$- \det \left( \mathrm { A } \right) = \det \left( - \mathrm { A } \right) = 0 , \quad \mathrm { i f } n \text { is odd }$$
(461)
(462)

The eigenvalues of an antisymmetric matrix are placed on the imaginary axis
and the eigenvectors are unitary.


#### 9.8.3 Decomposition

A square matrix A can always be written as a sum of a symmetric $\mathrm { A } _ { \perp }$ and an
antisymmetric matrix A_

$$\mathrm { A } = \mathrm { A } _ { + } + \mathrm { A }$$
(463)

Such a decomposition could e.g. be

$$A = \frac { A + A ^ { T } } { 2 } + \frac { A - A ^ { T } } { 2 } = A _ { + } + A _ { - } .$$
(464)


### 9.9 Toeplitz Matrices

A Toeplitz matrix $\mathrm { T }$ is a matrix where the elements of each diagonal is the
same. In the $n \times n$ square case, it has the following structure:

$$\mathrm { T } = \left[ \begin{array}{} t _ { 1 1 } & t _ { 1 2 } & \cdots & t _ { 1 n } \\ t _ { 1 2 } & \cdots & t _ { 1 n } \\ & \ddots & \ddots & \vdots \\ t _ { n 1 } & \cdots & t _ { 2 1 } & t _ { 1 2 } \\ & & & t _ { 1 1 } \end{array} \right] = \left[ \begin{array}{} & t _ { 1 } & \cdots & t _ { n - 1 } \\ & \ddots & \ddots & \vdots \\ & & \ddots & \vdots \\ t _ { 1 1 } & t _ { 1 1 } & & t _ { - 1 } & t _ { - 1 } & t _ { - 1 } \end{array} \right]$$
(465)

A Toeplitz matrix is persymmetric. If a matrix is persymmetric (or orthosym-
metric), it means that the matrix is symmetric about its northeast-southwest
diagonal (anti-diagonal) [12]. Persymmetric matrices is a larger class of matri-
ces, since a persymmetric matrix not necessarily has a Toeplitz structure. There

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 54" -->
<!-- PageBreak -->

<!-- PageHeader="9 SPECIAL MATRICES" -->
<!-- PageHeader="9.10 Transition matrices" -->

are some special cases of Toeplitz matrices. The symmetric Toeplitz matrix is
given by:

$$\mathrm { T } = \left[ \begin{array}{} t _ { 0 } & t _ { 1 } & \cdots & t _ { n - 1 } \\ t _ { 1 } & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & t _ { 1 } \\ t _ { n - 1 } & \cdots & t _ { 1 } & t _ { 0 } \end{array} \right]$$
(466)

The circular Toeplitz matrix:

$$\mathrm { T } _ { C } = \left[ \begin{array}{} t _ { 0 } & t _ { 1 } & \cdots & t _ { n - 1 } \\ t _ { n - 1 } & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & t _ { 1 } \\ t _ { 1 } & \cdots & t _ { n - 1 } & t _ { 0 } \end{array} \right]$$
(467)

The upper triangular Toeplitz matrix:

$$\mathrm { T } _ { U } = \left[ \begin{array}{} t _ { 0 } & t _ { 1 } & \cdots & t _ { n - 1 } \\ 0 & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & t _ { 1 } \\ 0 & \cdots & 0 & t _ { 0 } \end{array} \right] ,$$
(468)

and the lower triangular Toeplitz matrix:

$$\mathrm { T } _ { L } = \left[ \begin{array}{} t _ { 0 } & 0 & \cdots & 0 \\ t _ { - 1 } & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & 0 \\ t _ { - \left( n - 1 \right) } & \cdots & t _ { - 1 } & t _ { 0 } \end{array} \right]$$
(469)


#### 9.9.1 Properties of Toeplitz Matrices

The Toeplitz matrix has some computational advantages. The addition of two
Toeplitz matrices can be done with $\mathcal{O} \left( n \right)$ flops, multiplication of two Toeplitz
matrices can be done in $\mathcal{O} \left( n \ln n \right.$ flops. Toeplitz equation systems can be solved
in $\mathcal{O} \left( n ^ { 2 } \right)$ flops. The inverse of a positive definite Toeplitz matrix can be found
in $\mathcal{O} \left( n ^ { 2 } \right)$ flops too. The inverse of a Toeplitz matrix is persymmetric. The
product of two lower triangular Toeplitz matrices is a Toeplitz matrix. More
information on Toeplitz matrices and circulant matrices can be found in [13, 7].


### 9.10 Transition matrices

A square matrix $\mathrm { P }$ is a transition matrix, also known as stochastic matrix or
probability matrix, if

$$0 \leq \left( \mathrm { P } \right) _ { i j } \leq 1 , \quad \sum _ { j } \left( \mathrm { P } \right) _ { i j } = 1 ,$$

The transition matrix usually describes the probability of moving from state $\dot { \imath }$
to $j$ in one step and is closely related to markov processes. Transition matrices

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 55" -->
<!-- PageBreak -->

<!-- PageHeader="9 SPECIAL MATRICES" -->
<!-- PageHeader="9.11 Units, Permutation and Shift" -->

have the following properties

$$\mathrm { P r o b } \left[ i \rightarrow j \mathrm { i n } 1 \mathrm { s t e p } \right] = \left( \mathrm { P } \right) _ { i j }$$
$$\mathrm { P r o b } \left[ i \rightarrow j \mathrm { i n } 2 \mathrm { s t e p s } \right] = \left( \mathrm { P } ^ { 2 } \right) _ { i j }$$
(470)
(471)

$$\mathrm { P r o b } \left[ i \rightarrow j \text { in } k \text { steps } \right] = \left( P ^ { k } \right) _ { i j }$$
$$\text { If all rows are identical } \Rightarrow \mathrm { P } ^ { n } = \mathrm { P }$$
(472)
(473)

aP = a, & is called invariant
(474)

where $\alpha$ is a so-called stationary probability vector, i.e., $0 \leq \alpha _ { i } \leq 1 \mathrm { a n d } \sum _ { i } \alpha _ { i } =$
1.


### 9.11 Units, Permutation and Shift


#### 9.11.1 Unit vector

Let $\mathrm { e } _ { i } \in \mathbb{R} ^ { n \times 1 }$ be the ith unit vector, i.e. the vector which is zero in all entries
except the ith at which it is 1.


#### 9.11.2 Rows and Columns

$$i . t h \text { row of } \mathrm { A } = \mathrm { e } _ { i } ^ { T } \mathrm { A }$$
(475)
(476)

j.th column of A = Aej


#### 9.11.3 Permutations

Let $P$ be some permutation matrix, e.g.

P = 1 0 0 = [e2 e1 e3 ] = et

010
001

e
er
3
(477)

For permutation matrices it holds that

$$\mathrm { P P } ^ { T } = \mathrm { I }$$
(478)

and that

$$\mathrm { A P } = \left[ \begin{array}{} \mathrm { A e } _ { 2 } & \mathrm { A e } _ { 1 } & \mathrm { A e } _ { 3 } ^ { \mathrm { T } } \mathrm { A } \\ \mathrm { A e } _ { 2 } & \mathrm { A e } _ { 3 } & \mathrm { A } \mathrm { e } _ { 3 } \end{array} \right] \quad \mathrm { P A } = \left[ \begin{array}{} \mathrm { e } _ { 2 } ^ { T } \mathrm { A } \\ \mathrm { e } _ { 1 } ^ { T } \mathrm { A } \\ \mathrm { e } _ { 3 } ^ { T } \mathrm { A } \end{array} \right]$$
(479)

That is, the first is a matrix which has columns of $\mathrm { A }$ but in permuted sequence
and the second is a matrix which has the rows of $\mathrm { A }$ but in the permuted se-
quence.


##### 9.11.4 Translation, Shift or Lag Operators

Let L denote the lag (or 'translation' or 'shift') operator defined on a $4 \times 4$
example by

$$L = \left[ \begin{array}{} { 0 } & { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} \right]$$
(480)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 56" -->
<!-- PageBreak -->

<!-- PageHeader="9.12 Vandermonde Matrices" -->
<!-- PageHeader="9 SPECIAL MATRICES" -->

i.e. a matrix of zeros with one on the sub-diagonal, $\left( \mathrm { L } \right) _ { i j } = \delta _ { i , j + 1 } .$ With some
signal $x _ { t }$ for $t = 1 , \ldots , N ,$ the n.th power of the lag operator shifts the indices,
i.e.

$$\left( \mathrm { L } ^ { n } \mathrm { x } \right) _ { t } = \left\{ \begin{array}{} 0 & \mathrm { f o r } \quad t = 1 , \ldots , n \\ x _ { t - n } & \mathrm { f o r } \quad t = n + 1 , \ldots , N \end{array} \right.$$ ☒
(481)

A related but slightly different matrix is the 'recurrent shifted' operator defined
on a 4x4 example by

$$\widehat { \mathrm { L } } = \left[ \begin{array}{} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right]$$
(482)

i.e. a matrix defined by $\left( \widehat { \mathrm { L } } \right) _ { i j } = \delta _ { i , j + 1 } + \delta _ { i , 1 } \delta _ { j , d i m \left( \mathrm { L } \right) } .$ On a signal x it has the
effect

$$\left( \widehat { \mathrm { L } } ^ { n } \mathrm { x } \right) _ { t } = x _ { t ^ { \prime } } , \quad t ^ { \prime } = \left[ \left( t - n \right) m o d N \right] + 1$$ ☒
(483)

That is, L is like the shift operator L except that it 'wraps' the signal as if it
was periodic and shifted (substituting the zeros with the rear end of the signal).
Note that $\widehat { \mathrm { L } }$ is invertible and orthogonal, i.e.

$$\widehat { \mathrm { L } } ^ { - 1 } = \widehat { \mathrm { L } } ^ { T }$$
(484)


### 9.12 Vandermonde Matrices

A Vandermonde matrix has the form [15]

$$\mathrm { V } = \left[ \begin{array}{} 1 & v _ { 1 } & v _ { 1 } ^ { 2 } & \cdots & v _ { 1 } ^ { n - 1 } \\ 1 & v _ { 2 } & v _ { 2 } ^ { 2 } & \cdots & v _ { 2 } ^ { n - 1 } \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & v _ { n } & v _ { n } ^ { 2 } & \cdots & v _ { n } ^ { n - 1 } \end{array} \right] .$$
(485)

The transpose of $\mathrm { V }$ is also said to a Vandermonde matrix. The determinant is
given by [29]

$$\det \mathrm { V } = \prod _ { i > j } \left( v _ { i } - v _ { j } \right)$$
(486)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 57" -->
<!-- PageBreak -->

<!-- PageHeader="10 FUNCTIONS AND OPERATORS" -->


## 10 Functions and Operators


### 10.1 Functions and Series


#### 10.1.1 Finite Series

$$\left( \mathrm { X } ^ { n } - \mathrm { I } \right) \left( \mathrm { X } - \mathrm { I } \right) ^ { - 1 } = \mathrm { I } + \mathrm { X } + \mathrm { X } ^ { 2 } + \ldots + \mathrm { X } ^ { n - 1 }$$ ☒ ☒ ☒ ☒ ☒
(487)


#### 10.1.2 Taylor Expansion of Scalar Function

Consider some scalar function $f \left( \mathrm { x } \right)$ which takes the vector $x$ as an argument.
☒
This we can Taylor expand around $\mathrm { x } _ { 0 }$

$$f \left( \mathrm { x } \right) \cong f \left( \mathrm { x } _ { 0 } \right) + \mathrm { g } \left( \mathrm { x } _ { 0 } \right) ^ { T } \left( \mathrm { x } - \mathrm { x } _ { 0 } \right) + \frac { 1 } { 2 } \left( \mathrm { x } - \mathrm { x } _ { 0 } \right) ^ { T } \mathrm { H } \left( \mathrm { x } _ { 0 } \right) \left( \mathrm { x } - \mathrm { x } _ { 0 } \right)$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒
(488)

where

$$g \left( x _ { 0 } \right) = \frac { \partial f \left( x \right) } { \partial x } | _ { x _ { 0 } } \quad H \left( x _ { 0 } \right) = \frac { \partial ^ { 2 } f \left( x \right) } { \partial x \partial x ^ { T } } | _ { x _ { 0 } }$$ ☒ ☒


#### 10.1.3 Matrix Functions by Infinite Series

As for analytical functions in one dimension, one can $d e f i n e$ a matrix function
for square matrices $\mathrm { X }$ by an infinite series
☒

$$\mathrm { f } \left( \mathrm { X } \right) = \sum _ { n = 0 } ^ { \infty } c _ { n } \mathrm { X } ^ { n }$$ ☒ ☒
(489)

assuming the limit exists and is finite. If the coefficients $c _ { n }$ fulfils $\sum _ { n } c _ { n } x ^ { n } < \infty ,$
then one can prove that the above series exists and is finite, see [1]. Thus for
any $a n a l y t i c a l$ function $f \left( x \right)$ there exists a corresponding matrix function $\mathrm { f } \left( \mathrm { x } \right)$
☒
constructed by the Taylor expansion. Using this one can prove the following
results:

1\) $A$ matrix $\mathrm { A }$ is a zero of its own characteristic polynomium [1]:

$$p \left( \lambda \right) = \det \left( \mathrm { I } \lambda - \mathrm { A } \right) = \sum _ { n } c _ { n } \lambda ^ { n } \quad \Rightarrow \quad p \left( \mathrm { A } \right) = 0$$ ☒
(490)

2\) If $\mathrm { A }$ is square it holds that [1]

$$\mathrm { A } = \mathrm { U B U } ^ { - 1 } \quad \Rightarrow \quad \mathrm { f } \left( \mathrm { A } \right) = \mathrm { U f } \left( \mathrm { B } \right) \mathrm { U } ^ { - 1 }$$ ☒
(491)

3\) $\mathrm { A }$ useful fact when using power series is that

$$\mathrm { A } ^ { n } \rightarrow 0 \mathrm { f o r } n \rightarrow \infty \quad \mathrm { i f } \quad | \mathrm { A } | < 1$$
(492)


#### 10.1.4 Identity and commutations

It holds for an analytical matrix function $\mathrm { f } \left( \mathrm { X } \right)$ that
☒

$$\mathrm { f } \left( \mathrm { A B } \right) \mathrm { A } = \mathrm { A f } \left( \mathrm { B A } \right)$$
(493)

see B.1.2 for a proof.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 58" -->
<!-- PageBreak -->

<!-- PageHeader="10.2 Kronecker and Vec Operator" -->
<!-- PageHeader="10 FUNCTIONS AND OPERATORS" -->


#### 10.1.5 Exponential Matrix Function

In analogy to the ordinary scalar exponential function, one can define exponen-
tial and logarithmic matrix functions:

$$e ^ { \mathrm { A } } \equiv \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \mathrm { A } ^ { n } = \mathrm { I } + \mathrm { A } + \frac { 1 } { 2 } \mathrm { A } ^ { 2 } + \ldots .$$
$$e ^ { - \mathrm { A } } \equiv \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \left( - 1 \right) ^ { n } \mathrm { A } ^ { n } = \mathrm { I } - \mathrm { A } + \frac { 1 } { 2 } \mathrm { A } ^ { 2 } - \ldots .$$
(494)
(495)

$$e ^ { t \mathrm { A } } \equiv \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \left( t \mathrm { A } \right) ^ { n } = \mathrm { I } + t \mathrm { A } + \frac { 1 } { 2 } t ^ { 2 } \mathrm { A } ^ { 2 } + \ldots .$$
$$\ln \left( \mathrm { I } + \mathrm { A } \right) \equiv \sum _ { n = 1 } ^ { \infty } \frac { \left( - 1 \right) ^ { n - 1 } } { n } \mathrm { A } ^ { n } = \mathrm { A } - \frac { 1 } { 2 } \mathrm { A } ^ { 2 } + \frac { 1 } { 3 } \mathrm { A } ^ { 3 } - \ldots .$$
(496)
(497)

Some of the properties of the exponential function are [1]

$$\begin{array}{} e ^ { \mathrm { A } } e ^ { \mathrm { B } } = e ^ { \mathrm { A } + \mathrm { B } } \mathrm { i f } \mathrm { A B } = \mathrm { B A } \\ \left( e ^ { \mathrm { A } } \right) ^ { - 1 } = e ^ { - \mathrm { A } } \end{array}$$
$$\frac { d } { d t } e ^ { t \mathrm { A } } = \mathrm { A } e ^ { t \mathrm { A } } = e ^ { t \mathrm { A } } \mathrm { A } , \quad t \in \mathbb{R} ,$$
$$\frac { d } { d t } \mathrm { T r } \left( e ^ { t \mathrm { A } } \right) = \mathrm { T r } \left( \mathrm { A } e ^ { t \mathrm { A } } \right)$$
(498)
(499)
(500)
(501)

$$\det \left( e ^ { \mathrm { A } } \right) = e ^ { \mathrm { T r } \left( \mathrm { A } \right) }$$
(502)


#### 10.1.6 Trigonometric Functions

$$\sin \left( \mathrm { A } \right) \equiv \sum _ { n = 0 } ^ { \infty } \frac { \left( - 1 \right) ^ { n } \mathrm { A } ^ { 2 n + 1 } } { \left( 2 n + 1 \right) ! } = \mathrm { A } - \frac { 1 } { 3 ! } \mathrm { A } ^ { 3 } + \frac { 1 } { 5 ! } \mathrm { A } ^ { 5 } - \ldots$$
$$\cos \left( \mathrm { A } \right) \equiv \sum _ { n = 0 } ^ { \infty } \frac { \left( - 1 \right) ^ { n } \mathrm { A } ^ { 2 n } } { \left( 2 n \right) ! } = \mathrm { I } - \frac { 1 } { 2 ! } \mathrm { A } ^ { 2 } + \frac { 1 } { 4 ! } \mathrm { A } ^ { 4 } - \ldots .$$
(503)
(504)


### 10.2 Kronecker and Vec Operator


#### 10.2.1 The Kronecker Product

The Kronecker product of an $m \times n$ matrix A and an $r \times q$ matrix B, is an
$m r \times n q$ matrix, $\mathrm { A } \otimes \mathrm { B }$ defined as

$$A \otimes B = \left[ \begin{array}{} A _ { 1 1 } B & A _ { 1 2 } B & \ldots & A _ { 1 n } B \\ A _ { 2 1 } B & A _ { 2 2 } B & \ldots & A _ { 2 n } B \\ A _ { 2 1 } B & A _ { 2 2 } B & \ldots & A _ { m n } B \\ A _ { m 1 } B & A _ { m 2 } B & \ldots & A _ { m n } B \end{array} \right]$$
(505)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 59" -->
<!-- PageBreak -->

<!-- PageHeader="10.2 Kronecker and Vec Operator" -->
<!-- PageHeader="10 FUNCTIONS AND OPERATORS" -->

The Kronecker product has the following properties (see [19])

$$A \otimes \left( B + C \right) = A \otimes B + A \otimes C$$
$$\mathrm { A } \otimes \mathrm { B } \neq \mathrm { B } \otimes \mathrm { A }$$
$$A \otimes \left( B \otimes C \right) = \left( A \otimes B \right) \otimes C$$
$$\left( \alpha _ { A } \mathrm { A } \otimes \alpha _ { B } \mathrm { B } \right) = \alpha _ { A } \alpha _ { B } \left( \mathrm { A } \otimes \mathrm { B } \right)$$
$$\left( A \otimes B \right) ^ { T } = A ^ { T } \otimes B ^ { T }$$
$$\left( \mathrm { A } \otimes \mathrm { B } \right) \left( \mathrm { C } \otimes \mathrm { D } \right) = \mathrm { A C } \otimes \mathrm { B D }$$
$$\left( \mathrm { A } \otimes \mathrm { B } \right) ^ { - 1 } = \mathrm { A } ^ { - 1 } \otimes \mathrm { B } ^ { - 1 }$$
$$\left( A \otimes B \right) ^ { + } = A ^ { + } \otimes B ^ { + }$$
(506)
in general
☒ ☒
(507)
☒ ☒
(508)
☒
(509)
☒
(510)
☒
(511)
☒ ☒
(512)
☒
(513)


<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td> ☒</td>
<td>=</td>
<td></td>
<td>(514)</td>
</tr>
<tr>
<td>☒</td>
<td></td>
<td>☒</td>
<td>(515)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$$\mathrm { T r } \left( \mathrm { A } \otimes \mathrm { B } \right) = \mathrm { T r } \left( \mathrm { A } \right) \mathrm { T r } \left( \mathrm { B } \right) = \mathrm { T r } \left( \Lambda _ { A } \otimes \Lambda _ { B } \right)$$ $$\det \left( \mathrm { A } \otimes \mathrm { B } \right) = \det \left( \mathrm { A } \right) ^ { \mathrm { r a n k } \left( \mathrm { B } \right) } \det \left( \mathrm { B } \right) ^ { \mathrm { r a n k } \left( \mathrm { A } \right) }$$</td>
<td>(516)</td>
</tr>
<tr>
<td></td>
<td>=</td>
<td>{eig(B&amp; A)} if A, are square</td>
<td>(517)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$$\left\{ \mathrm { e i g } \left( \mathrm { A } \otimes \mathrm { B } \right) \right\} = \left\{ \mathrm { e i g } \left( \mathrm { A } \right) \mathrm { e i g } \left( \mathrm { B } \right) ^ { T } \right\}$$ $$\mathrm { e i g } \left( \mathrm { A } \otimes \mathrm { B } \right) = \mathrm { e i g } \left( \mathrm { A } \right) \otimes \mathrm { e i g } \left( \mathrm { B } \right)$$ if $\mathrm { A } ,$ B are symmetric and square</td>
<td>(518)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>☒</td>
<td>(519)</td>
</tr>
</table>


Where $\left\{ \lambda _ { i } \right\}$ denotes the set of values $\lambda _ { i } ,$ that is, the values in no particular
order or structure, and $\Lambda _ { A }$ denotes the diagonal matrix with the eigenvalues of
$\mathrm { A } .$


#### 10.2.2 The Vec Operator

The vec-operator applied on a matrix $\mathrm { A }$ stacks the columns into a vector, i.e.
for a $2 \times 2$ matrix

$$\mathrm { A } = \left[ \begin{array}{} A _ { 1 1 } & A _ { 1 2 } \\ A _ { 2 1 } & A _ { 2 2 } \end{array} \right] \quad \mathrm { v e c } \left( \mathrm { A } \right) = \left[ \begin{array}{} A _ { 1 1 } \\ A _ { 2 1 } \\ A _ { 1 2 } \\ A _ { 2 2 } \end{array} \right]$$

Properties of the vec-operator include (see [19])

$$\mathrm { v e c } \left( \mathrm { A X B } \right) = \left( \mathrm { B } ^ { T } \otimes \mathrm { A } \right) \mathrm { v e c } \left( \mathrm { X } \right)$$
$$\mathrm { T r } \left( \mathrm { A } ^ { T } \mathrm { B } \right) = \mathrm { v e c } \left( \mathrm { A } \right) ^ { T } \mathrm { v e c } \left( \mathrm { B } \right)$$ ☒ ☒
(520)
☒
(521)

$$\mathrm { v e c } \left( \mathrm { A } + \mathrm { B } \right) = \mathrm { v e c } \left( \mathrm { A } \right) + \mathrm { v e c } \left( \mathrm { B } \right)$$
$$\mathrm { v e c } \left( \alpha \mathrm { A } \right) = \alpha \cdot \mathrm { v e c } \left( \mathrm { A } \right)$$
$$\mathrm { a } ^ { T } \mathrm { X B X } ^ { T } \mathrm { c } = \mathrm { v e c } \left( \mathrm { X } \right) ^ { T } \left( \mathrm { B } \otimes \mathrm { c a } ^ { T } \right) \mathrm { v e c } \left( \mathrm { X } \right)$$ ☒
(522)
(523)
☒ ☒
(524)

See B.1.1 for a proof for Eq. 524.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 60" -->
<!-- PageBreak -->

<!-- PageHeader="10 FUNCTIONS AND OPERATORS" -->
<!-- PageHeader="10.3 Vector Norms" -->


### 10.3 Vector Norms


#### 10.3.1 Examples

$$| | \mathrm { x } | | _ { 1 } = \sum _ { i } | x _ { i } |$$
$$| | \mathrm { x } | | _ { 2 } ^ { 2 } = \mathrm { x } ^ { H } \mathrm { x }$$
$$| | \mathrm { x } | | _ { p } = \left[ \sum _ { i } | x _ { i } | ^ { p } \right] ^ { 1 / p }$$
$$| | \mathrm { x } | | _ { \infty } = \max _ { i } | x _ { i } |$$ ☒
(525)
☒ ☒ ☒
(526)
(527)
☒
(528)

Further reading in e.g. [12, $p .$ 52]


### 10.4 Matrix Norms


#### 10.4.1 Definitions

A matrix norm is a mapping which fulfils

$$| \mathrm { A } | | \geq 0$$
$$| | \mathrm { A } | | \quad = \quad 0 \Leftrightarrow \mathrm { A } = 0$$
$$| | c \mathrm { A } | | = | c | | | \mathrm { A } | | , \quad c \in \mathbb{R}$$
$$| | \mathrm { A } + \mathrm { B } | | \leq | | \mathrm { A } | | + | | \mathrm { B } | |$$
(529)
(530)
(531)
(532)


#### 10.4.2 Induced Norm or Operator Norm

An induced norm is a matrix norm induced by a vector norm by the following

$$| | \mathrm { A } | | = \sup \left\{ | | \mathrm { A x } | | \quad | | \mathrm { x } | | = 1 \right\}$$ ☒
(533)

where $| \cdot |$ on the left side is the induced matrix norm, while $| | \cdot | |$ on the right
side denotes the vector norm. For induced norms it holds that

$$\begin{array}{} | | \mathrm { I } | | & = & 1 \\ | | \mathrm { A x } | | & \leq & | | \mathrm { A } | | \cdot | | \mathrm { x } | | , & \text { for all } \mathrm { A } , \mathrm { x } \\ | | \mathrm { A x } | | & \leq & | | \mathrm { A } | | _ { 1 } & | \mathrm { i } _ { \mathrm { R } | | } & \mathrm { f o r } \mathrm { a l l } \mathrm { A } , \mathrm { B } \end{array} ,$$
(534)
(535)
AB| |
(536)


### 10.4.3 Examples

$$| | \mathrm { A } | | _ { 1 } \quad = \quad \max _ { j } \sum _ { j } | A _ { i j } |$$
$$\begin{array}{} | | \mathrm { A } | | _ { 2 } = \sqrt { \max \mathrm { e i g } \left( \mathrm { A } ^ { H } \mathrm { A } \right) } \\ | | \mathrm { A } | | _ { p } = \left( \max | | \mathrm { A x } | | _ { p } \right) ^ { 1 / p } \end{array}$$
$$| | \mathrm { A } | | _ { \infty } = \max _ { i } \sum | A _ { i j } |$$
(537)
(538)
$\left( \max _ { | | x | | } | | A x | | _ { p } \right) ^ { 1 / p }$
(539)
☒
(540)
j

$| | A | | _ { F }$

=
\>
ij

1

|Aij|2 = Tr(AAH)
(Frobenius)
(541)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 61" -->
<!-- PageBreak -->

<!-- PageHeader="10 FUNCTIONS AND OPERATORS" -->
<!-- PageHeader="10.5 Rank" -->

$$| | \mathrm { A } | | _ { \max } = \max _ { i j } | A _ { i j } |$$
(542)


<table>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$$| | \mathrm { A } | | _ { \mathrm { K F } } = | | \mathrm { s i n g } \left( \mathrm { A } \right) | | _ { 1 } \quad \mathrm { \left( K y <space> F a n \right) }$$</td>
<td>(543)</td>
</tr>
</table>


$\mathrm { w h e r e } \mathrm { s i n g } \left( \mathrm { A } \right)$ is the vector of singular values of the matrix $\mathrm { A } .$


### 10.4.4 Inequalities

E. H. Rasmussen has in yet unpublished material derived and collected the
following inequalities. They are collected in a table as below, assuming $\mathrm { A }$ is an
$m \times n ,$ and $d = \mathrm { r a n k } \left( \mathrm { A } \right)$


<table>
<tr>
<th></th>
<th></th>
<th>|A|1</th>
<th></th>
<th></th>
<th></th>
<th>| A|KF</th>
</tr>
<tr>
<td>$\bar { | | \mathrm { A } | | _ { \max } }$</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>$| | \mathrm { A } | | _ { 1 }$</td>
<td>$m$</td>
<td></td>
<td>$m$</td>
<td>☒ $\sqrt { m }$</td>
<td>☒ $\sqrt { m }$</td>
<td>☒ $\sqrt { m }$</td>
</tr>
<tr>
<td>$| | \mathrm { A } | | _ { \infty }$</td>
<td>$n$</td>
<td>$n$</td>
<td></td>
<td>☒ $\sqrt { n }$</td>
<td>☒ $\sqrt { n }$</td>
<td>☒ $\sqrt { n }$</td>
</tr>
<tr>
<td>$| | \mathrm { A } | | _ { 2 }$</td>
<td>☒ $\sqrt { m n }$</td>
<td>☒ $\sqrt { n }$</td>
<td>☒ $\sqrt { m }$</td>
<td></td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>$| | \mathrm { A } | | _ { \mathrm { F } }$</td>
<td>☒ $\sqrt { m n }$</td>
<td>☒ $\sqrt { n }$</td>
<td>☒ $\sqrt { m }$</td>
<td>$\sqrt { d }$ ☒</td>
<td></td>
<td>1</td>
</tr>
<tr>
<td>$| | \mathrm { A } | | _ { \mathrm { K F } }$</td>
<td>☒ $\sqrt { m n d }$</td>
<td>☒ $\sqrt { n d }$</td>
<td>☒ $\sqrt { m d }$</td>
<td>$d$</td>
<td>$\sqrt { d }$ ☒</td>
<td></td>
</tr>
</table>


which are to be read as, e.g.

$$| | \mathrm { A } | | _ { 2 } \leq \sqrt { m } \cdot | | \mathrm { A } | | _ { \infty }$$ ☒ ☒
(544)


### 10.4.5 Condition Number

The 2-norm of A equals $\sqrt { \left( \max \left( \mathrm { e i g } \left( \mathrm { A } ^ { T } \mathrm { A } \right) \right) \right) }$ [12, p.57]. For a symmetric, pos-
☒
itive definite matrix, this reduces to $\max \left( \mathrm { e i g } \left( \mathrm { A } \right) \right.$ The condition number based
on the 2-norm thus reduces to

$$\| \mathrm { A } \| _ { 2 } \| \mathrm { A } ^ { - 1 } \| _ { 2 } = \max \left( \mathrm { e i g } \left( \mathrm { A } \right) \right) \max \left( \mathrm { e i g } \left( \mathrm { A } ^ { - 1 } \right) \right) = \frac { \max \left( \mathrm { e i g } \left( \mathrm { A } \right) \right) } { \min \left( \mathrm { e i g } \left( \mathrm { A } \right) \right) } .$$
(545)


### 10.5 $\mathrm { R a n k }$


#### 10.5.1 Sylvester's Inequality

$\mathrm { A } \text { is } m \times n \text { and } B \text { is } n \times r ,$ then

$$\mathrm { r a n k } \left( \mathrm { A } \right) + \mathrm { r a n k } \left( \mathrm { B } \right) - n \leq \mathrm { r a n k } \left( \mathrm { A B } \right) \leq \min \left\{ \mathrm { r a n k } \left( \mathrm { A } \right) , \mathrm { r a n k } \left( \mathrm { B } \right) \right\}$$
(546)


### 10.6 Integral Involving Dirac Delta Functions

Assuming A to be square, then

$$\int p \left( \mathrm { s } \right) \delta \left( \mathrm { x } - \mathrm { A s } \right) d \mathrm { s } = \frac { 1 } { \det \left( \mathrm { A } \right) } p \left( \mathrm { A } ^ { - 1 } \mathrm { x } \right)$$
(547)

Assuming A to be "underdetermined", i.e. "tall", then

$$\int p \left( \mathrm { s } \right) \delta \left( \mathrm { x } - \mathrm { A s } \right) d \mathrm { s } = \left\{ \begin{array}{} \frac { 1 } { \sqrt { \det \left( \mathrm { A } ^ { T } \mathrm { A } \right) } } p \left( \mathrm { A } ^ { + } \mathrm { x } \right) & \mathrm { i f } \mathrm { x } = \mathrm { A A } ^ { + } \mathrm { x } \\ 0 & \mathrm { e l s e w h e r e } \end{array} \right\}$$ ☒
(548)

$S e e \left[ 9 \right] .$

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 62" -->
<!-- PageBreak -->

<!-- PageHeader="10.7 Miscellaneous" -->
<!-- PageHeader="10 FUNCTIONS AND OPERATORS" -->


## 10.7 Miscellaneous

For any A it holds that

$$\mathrm { r a n k } \left( \mathrm { A } \right) = \mathrm { r a n k } \left( \mathrm { A } ^ { T } \right) = \mathrm { r a n k } \left( \mathrm { A A } ^ { T } \right) = \mathrm { r a n k } \left( \mathrm { A } ^ { T } \mathrm { A } \right)$$
(549)

It holds that

$$\text { positive definite } \Leftrightarrow \quad \exists \text { B invertible, such that } \mathrm { A } = \mathrm { B B } ^ { T }$$
A is
(550)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 63" -->
<!-- PageBreak -->

<!-- PageHeader="A ONE-DIMENSIONAL RESULTS" -->


## A One-dimensional Results


### A.1 Gaussian


#### A.1.1 Density

$$p \left( x \right) = \frac { 1 } { \sqrt { 2 \pi \sigma ^ { 2 } } } \exp \left( - \frac { \left( x - \mu \right) ^ { 2 } } { 2 \sigma ^ { 2 } } \right)$$ ☒
(551)


#### A.1.2 Normalization

$$\int e ^ { - \frac { \left( s - \mu \right) ^ { 2 } } { 2 \sigma ^ { 2 } } } d s = \sqrt { 2 \pi \sigma ^ { 2 } }$$ ☒ ☒

(552)

$$\int e ^ { - \left( a x ^ { 2 } + b x + c \right) } d x = \sqrt { \frac { \pi } { a } } \exp \left[ \frac { b ^ { 2 } - 4 a c } { 4 a } \right]$$
$$\int e ^ { c _ { 2 } x ^ { 2 } + c _ { 1 } x + c _ { 0 } } d x = \sqrt { \frac { \pi } { - c _ { 2 } } } \exp \left[ \frac { c _ { 1 } ^ { 2 } - 4 c _ { 2 } c _ { 0 } } { - 4 c _ { 2 } } \right]$$ ☒
(553)
☒
(554)


#### A.1.3 Derivatives

$$\frac { \partial p \left( x \right) } { \partial \mu } = p \left( x \right) \frac { \left( x - \mu \right) } { \sigma ^ { 2 } }$$
(555)

$$\frac { \partial \ln p \left( x \right) } { \partial \mu } = \frac { \left( x - \mu \right) } { \sigma ^ { 2 } }$$
(556)

$$\frac { \partial p \left( x \right) } { \partial \sigma } = p \left( x \right) \frac { 1 } { \sigma } \left[ \frac { \left( x - \mu \right) ^ { 2 } } { \sigma ^ { 2 } } - 1 \right]$$
$$\frac { \partial \ln p \left( x \right) } { \partial \sigma } = \frac { 1 } { \sigma } \left[ \frac { \left( x - \mu \right) ^ { 2 } } { \sigma ^ { 2 } } - 1 \right]$$
(557)
(558)


##### A.1.4 Completing the Squares

$$c _ { 2 } x ^ { 2 } + c _ { 1 } x + c _ { 0 } = - a \left( x - b \right) ^ { 2 } + w$$
$$- a = c _ { 2 } \quad b = \frac { 1 } { 2 } \frac { c _ { 1 } } { c _ { 2 } } \quad w = \frac { 1 } { 4 } \frac { c _ { 1 } ^ { 2 } } { c _ { 2 } } + c _ { 0 }$$

or

$$c _ { 2 } x ^ { 2 } + c _ { 1 } x + c _ { 0 } = - \frac { 1 } { 2 \sigma ^ { 2 } } \left( x - \mu \right) ^ { 2 } + d$$
$$\mu = \frac { - c _ { 1 } } { 2 c _ { 2 } } \quad \sigma ^ { 2 } = \frac { - 1 } { 2 c _ { 2 } } \quad d = c _ { 0 } - \frac { c _ { 1 } ^ { 2 } } { 4 c _ { 2 } }$$


#### A.1.5 Moments

If the density is expressed by

$$p \left( x \right) = \frac { 1 } { \sqrt { 2 \pi \sigma ^ { 2 } } } \exp \left[ - \frac { \left( s - \mu \right) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] \quad \mathrm { o r } \quad p \left( x \right) = C \exp \left( c _ { 2 } x ^ { 2 } + c _ { 1 } x \right)$$ ☒
(559)

then the first few basic moments are

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 64" -->
<!-- PageBreak -->

<!-- PageHeader="A.2 One Dimensional Mixture of Gaussians ONE-DIMENSIONAL RESULTS" -->

$\langle x \rangle \quad = \quad \mu$
\=
$\langle x ^ { 2 } \rangle = \sigma ^ { 2 } + \mu ^ { 2 }$
\=
$\langle x ^ { 3 } \rangle = 3 \sigma ^ { 2 } \mu + \mu ^ { 3 }$
\=

$\frac { - c _ { 1 } } { 2 c _ { 2 } }$

2

\+
2

2
$\frac { - 1 } { 2 c _ { 2 } } + \left( \frac { - c _ { 1 } } { 2 c _ { 2 } } \right) ^ { 2 }$
$\frac { c _ { 1 } } { \left( 2 c _ { 2 } \right) ^ { 2 } } \left[ 3 - \frac { c _ { 1 } ^ { 2 } } { 2 c _ { 2 } } \right.$
c
1

$$\langle x ^ { 4 } \rangle \quad = \quad \mu ^ { 4 } + 6 \mu ^ { 2 } \sigma ^ { 2 } + 3 \sigma ^ { 4 } \quad = \quad \left( \frac { c _ { 1 } } { 2 c _ { 2 } } \right) ^ { 4 } + 6 \left( \frac { c _ { 1 } } { 2 c _ { 2 } } \right) ^ { 2 } \left( \frac { - 1 } { 2 c _ { 2 } } \right) + 3 \left( \frac { 1 } { 2 c _ { 2 } } \right) ^ { 2 }$$

and the central moments are

$\langle \left( x - \mu \right)$ = 0
\=
0

$$\begin{array}{} \langle \left( x - \mu \right) ^ { 2 } \rangle = \sigma ^ { 2 } = \left[ \frac { - 1 } { 2 c _ { 2 } } \right] \\ \langle \left( x - \mu \right) ^ { 3 } \rangle = 0 = 0 \end{array}$$
$$\langle \left( x - \mu \right) ^ { 4 } \rangle = 3 \sigma ^ { 4 } = 3 \left[ \frac { 1 } { 2 c _ { 2 } } \right] ^ { 2 }$$

A kind of pseudo-moments (un-normalized integrals) can easily be derived as

$$\int \exp \left( c _ { 2 } x ^ { 2 } + c _ { 1 } x \right) x ^ { n } d x = Z \langle x ^ { n } \rangle = \sqrt { \frac { \pi } { - c _ { 2 } } } \exp \left[ \frac { c _ { 1 } ^ { 2 } } { - 4 c _ { 2 } } \right] \langle x ^ { n } \rangle$$
(560)

¿From the un-centralized moments one can derive other entities like

$$\begin{array}{} \langle x ^ { 2 } \rangle - \langle x \rangle ^ { 2 } = \sigma ^ { 2 } = \frac { - 1 } { 2 c _ { 2 } } \\ \langle x ^ { 3 } \rangle - \langle x ^ { 2 } \rangle \langle x \rangle = 2 \sigma ^ { 2 } \mu = \frac { 2 c _ { 1 } } { \left( 2 c _ { 2 } \right) ^ { 2 } } \end{array}$$
$$\langle x ^ { 4 } \rangle - \langle x ^ { 2 } \rangle ^ { 2 } \quad = \quad 2 \sigma ^ { 4 } + 4 \mu ^ { 2 } \sigma ^ { 2 } \quad = \quad \frac { 2 } { \left( 2 c _ { 2 } \right) ^ { 2 } } \left[ 1 - 4 \frac { c _ { 1 } ^ { 2 } } { 2 c _ { 2 } } \right]$$


### A.2 One Dimensional Mixture of Gaussians


#### A.2.1 Density and Normalization

$$p \left( s \right) = \sum _ { k } ^ { K } \frac { \rho _ { k } } { \sqrt { 2 \pi \sigma _ { k } ^ { 2 } } } \exp \left[ - \frac { 1 } { 2 } \frac { \left( s - \mu _ { k } \right) ^ { 2 } } { \sigma _ { k } ^ { 2 } } \right]$$
(561)


#### A.2.2 Moments

A useful fact of MoG, is that

$$\langle x ^ { n } \rangle = \sum _ { k } \rho _ { k } \langle x ^ { n } \rangle _ { k }$$
(562)

where $\langle \cdot \rangle _ { k }$ denotes average with respect to the k.th component. We can calculate
the first four moments from the densities

$$p \left( x \right) = \sum _ { k } \rho _ { k } \frac { 1 } { \sqrt { 2 \pi \sigma _ { k } ^ { 2 } } } \exp \left[ - \frac { 1 } { 2 } \frac { \left( x - \mu _ { k } \right) ^ { 2 } } { \sigma _ { k } ^ { 2 } } \right]$$
$$p \left( x \right) = \sum _ { k } \rho _ { k } C _ { k } \exp \left[ c _ { k 2 } x ^ { 2 } + c _ { k 1 } x \right]$$
(563)
(564)

as

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 65" -->
<!-- PageBreak -->

<!-- PageHeader="$B$ PROOFS AND DETAILS" -->

$\langle x \rangle = \sum _ { k } \rho _ { k } \mu _ { k }$
$\langle x ^ { 2 } \rangle \quad = \quad \sum _ { k } \rho _ { k } \left( \sigma _ { k } ^ { 2 } + \mu _ { k } ^ { 2 } \right)$
$\langle x ^ { 3 } \rangle \quad = \quad \sum _ { k } \rho _ { k } \left( 3 \sigma _ { k } ^ { 2 } \mu _ { k } + \mu _ { k } ^ { 3 } \right)$
$= \sum _ { k } \rho _ { k }$
Ck1
2ck2

$= \sum _ { k } \rho _ { k } | \frac { - c _ { k 1 } } { 2 c _ { k 2 } } |$
= $\sum _ { k } \rho _ { k } | \frac { - 1 } { 2 c _ { k 2 } } + \left( \frac { - c _ { k 1 } } { 2 c _ { k 2 } } \right) ^ { 2 }$

2

\+
2

3 -

2
Ck1
2ck2

]

$$\langle x ^ { 4 } \rangle \quad = \quad \sum _ { k } \rho _ { k } \left( \mu _ { k } ^ { 4 } + 6 \mu _ { k } ^ { 2 } \sigma _ { k } ^ { 2 } + 3 \sigma _ { k } ^ { 4 } \right) \quad = \quad \sum _ { k } \rho _ { k } \left[ \left( \frac { 1 } { 2 c _ { k 2 } } \right) ^ { 2 } \right] \left( \frac { c _ { k 1 } } { 2 c _ { k 2 } } \right) ^ { 2 } - 6 \frac { c _ { k 1 } ^ { 2 } } { 2 c _ { k 2 } } + i$$

]
(x)
\=
0

If all the gaussians are centered, i.e. $\mu _ { k } = 0$ for all $k ,$ then

=
0

$$\begin{array}{} \langle x ^ { 2 } \rangle = \sum _ { k } \rho _ { k } \sigma _ { k } ^ { 2 } = \sum _ { k } \rho _ { k } \left[ \frac { - 1 } { 2 c _ { k 2 } } \right] \\ \langle x ^ { 3 } \rangle = 0 \end{array}$$
$$\langle x ^ { 4 } \rangle = \sum _ { k } \rho _ { k } 3 \sigma _ { k } ^ { 4 } = \sum _ { k } \rho _ { k } 3 \left[ \frac { - 1 } { 2 c _ { k 2 } } \right] ^ { 2 }$$

¿From the un-centralized moments one can derive other entities like

$\dot { \mu } _ { k } ^ { 2 } + \sigma _ { k } ^ { 2 } - \mu _ { k } \mu _ { k ^ { \prime } }$
$$\begin{array}{} \langle x ^ { 2 } \rangle - \langle x \rangle ^ { 2 } = \sum _ { k , k ^ { \prime } } \rho _ { k } \rho _ { k ^ { \prime } } \left[ \mu _ { k } ^ { 2 } + \sigma _ { k } ^ { 2 } - \mu _ { k } \mu _ { k ^ { \prime } } \right] \\ \langle x ^ { 3 } \rangle - \langle x ^ { 2 } \rangle \langle x \rangle = \sum _ { k , k ^ { \prime } } \rho _ { k } \rho _ { k ^ { \prime } } \left[ 3 \sigma _ { k } ^ { 2 } \mu _ { k } + \mu _ { k } ^ { 3 } - \left( \sigma _ { k } ^ { 2 } + \mu _ { k } ^ { 2 } \right) \mu _ { k ^ { \prime } } \right] _ { 2 \times \ldots 2 , \lambda } , \end{array}$$
$$\dot { \langle x ^ { 4 } \rangle } - \dot { \langle x ^ { 2 } \rangle ^ { 2 } } = \bar { \sum _ { k , k ^ { \prime } } \rho _ { k } \rho _ { k ^ { \prime } } \left[ \mu _ { k } ^ { 4 } + 6 \mu _ { k } ^ { 2 } \sigma _ { k } ^ { 2 } + 3 \sigma _ { k } ^ { 4 } - \left( \sigma _ { k } ^ { 2 } + \mu _ { k } ^ { 2 } \right) \left( \sigma _ { k ^ { \prime } } ^ { 2 } + \mu _ { k ^ { \prime } } ^ { 2 } \right) \right] }$$


#### A.2.3 Derivatives

Defining $p \left( s \right) = \sum _ { k } \rho _ { k } \mathcal{N} _ { s } \left( \mu _ { k } , \sigma _ { k } ^ { 2 } \right)$ we get for a parameter $\theta _ { j }$ of the j.th compo-
nent

$$\frac { \partial \ln p \left( s \right) } { \partial \theta _ { j } } = \frac { \rho _ { j } \mathcal{N} _ { s } \left( \mu _ { j } , \sigma _ { j } ^ { 2 } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { s } \left( \mu _ { k } , \sigma _ { k } ^ { 2 } \right) } \frac { \partial \ln \left( \rho _ { j } \mathcal{N} _ { s } \left( \mu _ { j } , \sigma _ { j } ^ { 2 } \right) \right) } { \partial \theta _ { j } }$$
(565)

that is,

$$\frac { \partial \ln p \left( s \right) } { \partial \rho _ { j } } = \frac { \rho _ { j } \mathcal{N} _ { s } \left( \mu _ { j } , \sigma _ { j } ^ { 2 } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { s } \left( \mu _ { k } , \sigma _ { k } ^ { 2 } \right) } \frac { 1 } { \rho _ { j } }$$
$$\frac { \partial \ln p \left( s \right) } { \partial \mu _ { j } } = \frac { \rho _ { j } \mathcal{N} _ { s } \left( \mu _ { j } , \sigma _ { j } ^ { 2 } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { s } \left( \mu _ { k } , \sigma _ { k } ^ { 2 } \right) } \frac { \left( s - \mu _ { j } \right) } { \sigma _ { j } ^ { 2 } }$$
$$\frac { \partial \ln p \left( s \right) } { \partial \sigma _ { j } } = \frac { \rho _ { j } \mathcal{N} _ { s } \left( \mu _ { j } , \sigma _ { j } ^ { 2 } \right) } { \sum _ { k } \rho _ { k } \mathcal{N} _ { s } \left( \mu _ { k } , \sigma _ { k } ^ { 2 } \right) } \frac { 1 } { \sigma _ { j } } \left[ \frac { \left( s - \mu _ { j } \right) ^ { 2 } } { \sigma _ { j } ^ { 2 } } - 1 \right]$$
(566)
(567)
(568)

Note that $\rho _ { k }$ must be constrained to be proper ratios. Defining the ratios by
$\rho _ { j } = e ^ { r _ { j } } / \sum _ { k } e ^ { r _ { k } } ,$ we obtain

$$\frac { \partial \ln p \left( s \right) } { \partial r _ { j } } = \sum _ { l } \frac { \partial \ln p \left( s \right) } { \partial \rho _ { l } } \frac { \partial \rho _ { l } } { \partial r _ { j } }$$

where

$$\frac { \partial \rho _ { l } } { \partial r _ { j } } = \rho _ { l } \left( \delta _ { l j } - \rho _ { j } \right)$$
(569)


## B Proofs and Details


### B.1 Misc Proofs


#### B.1.1 Proof of Equation 524

The following proof is work of Florian Roemer. Note the the vectors and ma-
trices below can be complex and the notation $X ^ { H } \text { is used fo }$ transpose and
☒
conjugated, while XT is only transpose of the complex matrix.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 66" -->
<!-- PageBreak -->

<!-- PageHeader="$B$ PROOFS AND DETAILS" -->
<!-- PageHeader="B.1 Misc Proofs" -->

Define the row vector $\mathrm { y } = \mathrm { a } ^ { H } \mathrm { X B }$ and the column vector $\mathrm { z } = \mathrm { X } ^ { H } \mathrm { c } .$ Then
☒ ☒

$$\mathrm { a } ^ { T } \mathrm { X B X } ^ { T } \mathrm { c } = \mathrm { y z } = \mathrm { z } ^ { T } \mathrm { y } ^ { T }$$ ☒

Note that $\mathrm { y }$ can be rewritten as $\mathrm { v e c } \left( \mathrm { y } \right) ^ { T }$ which is the same as
☒

$$\mathrm { v e c } \left( \mathrm { c o n j } \left( \mathrm { y } \right) \right) ^ { H } = \mathrm { v e c } \left( \mathrm { a } ^ { T } \mathrm { c o n j } \left( \mathrm { X } \right) \mathrm { c o n j } \left( \mathrm { B } \right) \right) ^ { H }$$ ☒ ☒

where "conj" means complex conjugated. Applying the vec rule for linear forms
Eq 520, we get

$$\mathrm { y } = \left( \mathrm { B } ^ { H } \otimes \mathrm { a } ^ { T } \mathrm { v e c } \left( \mathrm { c o n j } \left( \mathrm { X } \right) \right) ^ { H } = \mathrm { v e c } \left( \mathrm { X } \right) ^ { T } \left( \mathrm { B } \otimes \mathrm { c o n j } \left( \mathrm { a } \right) \right) \right.$$ ☒ ☒ ☒ ☒

where we have also used the rule for transpose of Kronecker products. For $\mathrm { y }$
☒
this yields $\left( \mathrm { B } ^ { T } \otimes \mathrm { a } ^ { H } \right) \mathrm { v e c } \left( \mathrm { X } \right) .$ Similarly we can rewrite z which is the same as
☒ ☒
$\mathrm { v e c } \left( \mathrm { z } ^ { T } \right) = \mathrm { v e c } \left( \mathrm { c } ^ { T } \mathrm { c o n j } \left( \mathrm { X } \right) \right) .$ Applying again Eq 520, we get
☒ ☒

$$\mathrm { z } = \left( \mathrm { I } \otimes \mathrm { c } ^ { T } \right) \mathrm { v e c } \left( \mathrm { c o n j } \left( \mathrm { X } \right) \right)$$ ☒

where I is the identity matrix. For $\mathrm { z } ^ { T }$ we obtain $\mathrm { v e c } \left( \mathrm { X } \right) \left( \mathrm { I } \otimes \mathrm { c } \right) .$ Finally, the
☒

original expression is $\mathrm { z } ^ { T } \mathrm { y } ^ { T }$ which now takes the form
☒

$$\mathrm { v e c } \left( \mathrm { X } \right) ^ { H } \left( \mathrm { I } \otimes \mathrm { c } \right) \left( \mathrm { B } ^ { T } \otimes \mathrm { a } ^ { H } \right) \mathrm { v e c } \left( \mathrm { X } \right)$$ ☒ ☒

the final step is to apply the rule for products of Kronecker products and by
that combine the Kronecker products. This gives

$$\mathrm { v e c } \left( \mathrm { X } \right) ^ { H } \left( \mathrm { B } ^ { T } \otimes \mathrm { c a } ^ { H } \right) \mathrm { v e c } \left( \mathrm { X } \right)$$ ☒ ☒ ☒

which is the desired result.


#### B.1.2 Proof of Equation 493

For any analytical function $\mathrm { f } \left( \mathrm { X } \right)$ of a matrix argument $\mathrm { X } ,$ it holds that
☒ ☒

$$\mathrm { f } \left( \mathrm { A B } \right) \mathrm { A } = \left( \sum _ { n = 0 } ^ { \infty } c _ { n } \left( \mathrm { A B } \right) ^ { n } \right) \mathrm { A }$$
$$= \sum _ { n = 0 } ^ { \infty } c _ { n } \left( A B \right) ^ { n } A$$
$$= \sum _ { n = 0 } ^ { \infty } c _ { n } A \left( B A \right) ^ { n }$$
$$= A \sum _ { n = 0 } ^ { \infty } c _ { n } \left( B A \right) ^ { n }$$
$$= \mathrm { A f } \left( \mathrm { B A } \right)$$


#### B.1.3 Proof of Equation 91

Essentially we need to calculate

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 67" -->
<!-- PageBreak -->

<!-- PageHeader="B PROOFS AND DETAILS" -->
<!-- PageHeader="B.1 Misc Proofs" -->

$$\frac { \partial \left( \mathrm { X } ^ { n } \right) _ { k l } } { \partial X _ { i j } } = \frac { \partial } { \partial X _ { i j } } \sum _ { u _ { 1 } , \ldots , u _ { n - 1 } } X _ { k , u _ { 1 } } X _ { u _ { 1 } , u _ { 2 } } \ldots X _ { u _ { n - 1 } , l }$$
$$= \delta _ { k , i } \delta _ { u _ { 1 } , j } X _ { u _ { 1 } , u _ { 2 } } \ldots X _ { u _ { n - 1 } , l }$$
$$+ X _ { k , u _ { 1 } } \delta _ { u _ { 1 } , i } \delta _ { u _ { 2 } , j } \ldots X _ { u _ { n - 1 } , l }$$
$$+ X _ { k , u _ { 1 } } X _ { u _ { 1 } , u _ { 2 } } \ldots \delta _ { u _ { n - 1 } , i } \delta _ { l , j }$$
$$= \sum _ { r = 0 } ^ { n - 1 } \left( X ^ { r } \right) _ { k i } \left( X ^ { n - 1 - r } \right) _ { j l }$$
$$= \sum _ { r = 0 } ^ { n - 1 } \left( X ^ { r } J ^ { i j } X ^ { n - 1 - r } \right) _ { k l }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒
.
☒ ☒ ☒ ☒ ☒ ☒

Using the properties of the single entry matrix found in Sec. 9.7.4, the result
follows easily.


#### B.1.4 Details on $E q .$ 571

$$\partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) = \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \mathrm { T r } \left[ \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \partial \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \right]$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \mathrm { T r } \left[ \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \left( \partial \left( \mathrm { X } ^ { H } \right) \mathrm { A X } + \mathrm { X } ^ { H } \partial \left( \mathrm { A } \right) \right. \right.$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \mathrm { T r } \left[ \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \partial \left( \mathrm { X } ^ { H } \right) \mathrm { A X } \right] \right.$$
$$\left. + \mathrm { T r } \left[ \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \partial \left( \mathrm { A X } \right) \right] \right)$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \mathrm { T r } \left[ \mathrm { A X } \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \partial \left( \mathrm { X } ^ { H } \right) \right] \right.$$
$$\left. + \mathrm { T r } \left[ \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \mathrm { A } \partial \left( \mathrm { X } \right) \right] \right)$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

First, the derivative is found with respect to the real part of $\mathrm { X }$
☒

$$\frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{R} \mathrm { X } } = \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \frac { \mathrm { T r } \left[ \mathrm { A X } \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \partial \left( \mathrm { X } ^ { H } \right) \right] } { \partial \mathfrak{R} \mathrm { X } } \right.$$
$$\left. + \frac { \mathrm { T r } \left[ \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \mathrm { A } \partial \left( \mathrm { X } \right) \right] } { \partial \mathfrak{R} \mathrm { X } } \right)$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \mathrm { A X } \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } + \left( \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \mathrm { A } \right) ^ { T } \right)$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

Through the calculations, (100) and (240) were used. In addition, by use of
(241), the derivative is found with respect to the imaginary part of X

$$i \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{I} \mathrm { X } } = i \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \frac { \mathrm { T r } \left[ \mathrm { A X } \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \partial \left( \mathrm { X } ^ { H } \right) \right] } { \partial \mathfrak{I} \mathrm { X } } \right.$$
$$\left. + \frac { \mathrm { T r } \left[ \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \mathrm { A } \partial \left( \mathrm { X } \right) \right] } { \partial \mathrm { S X } } \right)$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \mathrm { A X } \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } - \left( \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \mathrm { A } \right) ^ { T } \right)$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

Hence, derivative yields

$$\frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathrm { X } } = \frac { 1 } { 2 } \left( \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{R} \mathrm { X } } - i \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{I} \mathrm { X } } \right)$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \left( \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 } \mathrm { X } ^ { H } \mathrm { A } \right) ^ { T }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 68" -->
<!-- PageBreak -->

<!-- PageHeader="B PROOFS AND DETAILS" -->
<!-- PageHeader="B.1 Misc Proofs" -->

and the complex conjugate derivative yields

$$\frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathrm { X } ^ { * } } = \frac { 1 } { 2 } \left( \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathfrak{R} \mathrm { X } } + i \frac { \partial \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) } { \partial \mathrm { S X } } \right)$$
$$= \det \left( \mathrm { X } ^ { H } \mathrm { A X } \right) \mathrm { A X } \left( \mathrm { X } ^ { H } \mathrm { A X } \right) ^ { - 1 }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

Notice, for real $\mathrm { X } ,$ $\mathrm { A } ,$ the sum of (249) and (250) is reduced to (54).
☒
Similar calculations yield

$$\frac { \partial \det \left( \mathrm { X A X } ^ { H } \right) } { \partial \mathrm { X } } = \frac { 1 } { 2 } \left( \frac { \partial \det \left( \mathrm { X A X } ^ { H } \right) } { \partial \mathfrak{R} \mathrm { X } } - i \frac { \partial \det \left( \mathrm { X A X } ^ { H } \right) } { \partial \mathfrak{I} \mathrm { X } } \right)$$
$$= \det \left( \mathrm { X A X } ^ { H } \right) \left( \mathrm { A X } ^ { H } \left( \mathrm { X A X } ^ { H } \right) ^ { - 1 } \right) ^ { T }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒ ☒

(570)

and

$$\frac { \partial \det \left( \mathrm { X A X } ^ { H } \right) } { \partial \mathrm { X } ^ { * } } = \frac { 1 } { 2 } \left( \frac { \partial \det \left( \mathrm { X A X } ^ { H } \right) } { \partial \mathfrak{R} \mathrm { X } } + i \frac { \partial \det \left( \mathrm { X A X } ^ { H } \right) } { \partial \mathrm { S X } } \right)$$
$$= \det \left( \mathrm { X A X } ^ { H } \right) \left( \mathrm { X A X } ^ { H } \right) ^ { - 1 } \mathrm { X A }$$ ☒ ☒ ☒ ☒ ☒ ☒ ☒

(571)

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 69" -->
<!-- PageBreak -->

<!-- PageHeader="REFERENCES" -->
<!-- PageHeader="REFERENCES" -->


## References

[1] Karl Gustav Andersson and Lars-Christer Boiers. Ordinaera differentialek-
vationer. Studenterlitteratur, 1992.

[2] Jörn Anemüller, Terrence J. Sejnowski, and Scott Makeig. Complex inde-
pendent component analysis of frequency-domain electroencephalographic
data. Neural Networks, 16(9):1311-1323, November 2003.

[3] S. Barnet. Matrices. Methods and Applications. Oxford Applied Mathe-
matics and Computin Science Series. Clarendon Press, 1990.

[4] Christopher Bishop. Neural Networks for Pattern Recognition. Oxford
University Press, 1995.

[5] Robert J. Boik. Lecture notes: Statistics 550. Online, April 22 2002. Notes.

[6] D. H. Brandwood. A complex gradient operator and its application in
adaptive array theory. IEE Proceedings, 130(1):11-16, February 1983. PTS.
F and H.

[7] M. Brookes. Matrix Reference Manual, 2004. Website May 20, 2004.

[8] Contradsen K., $E n$ introduktion til statistik, IMM lecture notes, 1984.

[9] Mads Dyrholm. Some matrix results, 2004. Website August 23, 2004.

[10] Nielsen F. A., Formula, Neuro Research Unit and Technical university of
Denmark, 2002.

[11] Gelman A. B., J. S. Carlin, H. S. Stern, D. B. Rubin, Bayesian Data
Analysis, Chapman and Hall / CRC, 1995.

[12] Gene H. Golub and Charles F. van Loan. Matrix Computations. The Johns
Hopkins University Press, Baltimore, 3rd edition, 1996.

[13] Robert M. Gray. Toeplitz and circulant matrices: A review. Technical
report, Information Systems Laboratory, Department of Electrical Engi-
neering,Stanford University, Stanford, California 94305, August 2002.

[14] Simon Haykin. Adaptive Filter Theory. Prentice Hall, Upper Saddle River,
NJ, 4th edition, 2002.

[15] Roger A. Horn and Charles R. Johnson. Matrix Analysis. Cambridge
University Press, 1985.

[16] Mardia K. V., J.T. Kent and J.M. Bibby, Multivariate Analysis, Academic
Press Ltd., 1979.

[17] Mathpages on "Eigenvalue Problems and Matrix Invariants",

http://www.mathpages.com/home/kmath128.htm

[18] Carl D. Meyer. Generalized inversion of modified matrices. SIAM Journal
of Applied Mathematics, 24(3):315-323, May 1973.

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 70" -->
<!-- PageBreak -->

<!-- PageHeader="REFERENCES" -->


## REFERENCES

[19] Thomas P. Minka. Old and new matrix algebra useful for statistics, De-
cember 2000. Notes.

[20] Daniele Mortari Ortho-Skew and Ortho Sym Matrix Trigonometry John
Lee Junkins Astrodynamics Symposium, AAS 03-265, May 2003. Texas
A&M University, College Station, TX

[21] L. Parra and C. Spence. Convolutive blind separation of non-stationary
sources. In IEEE Transactions Speech and Audio Processing, pages 320-
327, May 2000.

[22] Kaare Brandt Petersen, Jiucang Hao, and Te-Won Lee. Generative and
filtering approaches for overcomplete representations. Neural Information
Processing - Letters and Reviews, vol. 8(1), 2005.

[23] John G. Proakis and Dimitris G. Manolakis. Digital Signal Processing.
Prentice-Hall, 1996.

[24] Laurent Schwartz. Cours d'Analyse, volume II. Hermann, Paris, 1967. As
referenced in [14].

[25] Shayle R. Searle. Matrix Algebra Useful for Statistics. John Wiley and
Sons, 1982.

[26] G. Seber and A. Lee. Linear Regression Analysis. John Wiley and Sons,
2002.

[27] S. M. Selby. Standard Mathematical Tables. CRC Press, 1974.

[28] Inna Stainvas. Matrix algebra in differential calculus. Neural Computing
Research Group, Information Engeneering, Aston University, UK, August
2002. Notes.

[29] P. P. Vaidyanathan. Multirate Systems and Filter Banks. Prentice Hall,
1993.

[30] Max Welling. The Kalman Filter. Lecture Note.

[31] Wikipedia on minors: "Minor (linear algebra)",

http://en.wikipedia.org/wiki/Minor_(linear_algebra)

[32] Zhaoshui He, Shengli Xie, et al, "Convolutive blind source separation in
frequency domain based on sparse representation", IEEE Transactions on
Audio, Speech and Language Processing, vol.15(5):1551-1563, July 2007.

[33] Karim T. Abou-Moustafa On Derivatives of Eigenvalues and Eigenvectors
of the Generalized Eigenvalue Problem. McGill Technical Report, October
2010.

[34] Mohammad Emtiyaz Khan Updating Inverse of a Matrix When a Column
is Added/Removed. Emt CS,UBC February 27, 2008

<!-- PageFooter="PETERSEN & PEDERSEN, THE MATRIX COOKBOOK, VERSION: NOVEMBER 15, 2012, Page 71" -->
<!-- PageBreak -->


### Index


<table>
<tr>
<th>Anti-symmetric, 54</th>
<th>Normal-Inverse Gamma distribution, 37 Normal-Inverse Wishart distribution, 39</th>
</tr>
<tr>
<td>Block matrix, 46</td>
<td></td>
</tr>
<tr>
<td>Chain rule, 15</td>
<td>Orthogonal, 49</td>
</tr>
<tr>
<td>Cholesky-decomposition, 32</td>
<td>Power series of matrices, 58</td>
</tr>
<tr>
<td>Co-kurtosis, 34</td>
<td>Probability matrix, 55</td>
</tr>
<tr>
<td>Co-skewness, 34</td>
<td>Pseudo-inverse, 21</td>
</tr>
<tr>
<td>$C o n d i t i o n \quad n u m b e r ,$ 62</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Schur complement, 41, 47 Single entry matrix, 52</td>
</tr>
<tr>
<td>Derivative of a complex matrix, 24</td>
<td>Singular Valued Decomposition (SVD),</td>
</tr>
<tr>
<td>Derivative of a determinant, 8</td>
<td>31</td>
</tr>
<tr>
<td>Derivative of a trace, 12</td>
<td>Skew-Hermitian, 48</td>
</tr>
<tr>
<td>Derivative of an inverse, 9</td>
<td>Skew-symmetric, 54</td>
</tr>
<tr>
<td>Derivative of symmetric matrix, 15</td>
<td>Stochastic matrix, 55</td>
</tr>
<tr>
<td>Derivatives of Toeplitz matrix, 16</td>
<td>Student-t, 37</td>
</tr>
<tr>
<td>Dirichlet distribution, 37</td>
<td>Sylvester's Inequality, 62 Symmetric, 54</td>
</tr>
<tr>
<td>Eigenvalues, 30</td>
<td></td>
</tr>
<tr>
<td>Eigenvectors, 30</td>
<td>Taylor expansion, 58</td>
</tr>
<tr>
<td>Exponential Matrix Function, 59</td>
<td>Toeplitz matrix, 54 Transition matrix, 55</td>
</tr>
<tr>
<td>Gaussian, conditional, 40</td>
<td>Trigonometric functions, 59</td>
</tr>
<tr>
<td>Gaussian, entropy, 44</td>
<td></td>
</tr>
<tr>
<td>Gaussian, linear combination, 41</td>
<td>Unipotent, 49</td>
</tr>
<tr>
<td>Gaussian, marginal,</td>
<td></td>
</tr>
<tr>
<td>Gaussian, product of $d e n s i t i e s , 4 2$</td>
<td>Vandermonde matrix, 57</td>
</tr>
<tr>
<td>Generalized inverse, 21</td>
<td>Vec operator, 59, 60</td>
</tr>
<tr>
<td>Hadamard inequality, 52</td>
<td>Wishart distribution, 38</td>
</tr>
<tr>
<td>Hermitian, 48</td>
<td>Woodbury identity, 18</td>
</tr>
</table>


Idempotent, 49
Kronecker product, 59
LDL decomposition, 33
LDM-decomposition, 33
Linear regression, 28
LU decomposition, 32
Lyapunov Equation, 30

Moore-Penrose inverse, 21
Multinomial distribution, 37

Nilpotent, 49
Norm of a matrix, 61
Norm of a vector, 61

<!-- PageNumber="72" -->
