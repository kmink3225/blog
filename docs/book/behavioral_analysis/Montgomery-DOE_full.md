Ik-

THE

STATISTICS LIBRARY

UNIVERSITY OF GLASGOW

'

r

/

. . / \

■

r

\

f

f

y

I

J

Design and Analysis
of Experiments

M. N. DAS
Central Water Commission, New Delhi

N. C. GIRI
University of Montreal, Quebec, Canada

WILEY EASTERN LIMITED
New Delhi Bangalore Bombay Calcutta

Copyright © 1979, Wiley Eastern Limited

This book or any part thereof may not be reproduced
in any form without the written permission of the publisher

This book is not to be sold outside the country to which
it is consigned by Wiley Eastern Limited

10 98765432

ISBN 0 85226 158 6

F
Published by Mohinder Singh Sejwal for W/iley Eastern Limited
4835/24 Ansari Road, Daryaganj, New Delhi 110002, and
printed by Mohan Makhijani at ReJchaPrinters Private Limited

A 102/1 Okhla Industrial Estate, Phase A New Delhi 110020.
Printed in India. fh .

Preface

The material presented in the book is the product of the experience gained
by the authors while offering courses on design and analysis of experiments
to graduate and post-graduate students and applied workers in the
Institute of Agricultural ResearchStatistics,New Delhi and Department of
Mathematics, University of Montreal, Canada. The book has been written to
suit the academic persons including teachers and students and the applied
workers who have to apply statistical principles for the collection and
interpretation of experimental data. Almost all the commonly adopted
designs have been included in the book. Most of the advanced techniques
and methodology available for designing and analysis of experiments are
included here together with discussion of elementary concepts and pre¬
liminary treatments of different topics. A number of new concepts and
alternative methods of treatment of several topics have been presented.
Simple andj convenient methods of construction of confounded symmetri¬
cal and asymmetrical factorial designs, alternative methods of analysis of
missing observations, orthogonal latin squares, designs for bio-assays and
weighing designs are some of the examples. The book contains in all nine
chapters including a chapter on basic statistical methods and concepts. A
chapter on designs for bio-assays required for pharmaceutical investigations
and response surface designs has also been added.

Complicated mathematical treatment has been avoided while presenting
the results in the different chapters. No emphasis has been given on
combinatorics while presenting the methods of construction of various
designs. More emphasis has been laid on common sense, experience and
intuition while introducing the topics, providing proofs of main results
and discussing extension and application of the results.

The book can serve as a textbook for both the graduate and post¬
graduate students in addition to being a reference book for applied
workers and research workers and students in statistics.

The authors acknowledge gratefully the facilities provided by the

University of Montreal for writing the book.

May 1979

M. N. Das
N. C. Giri

, , /

. \

'

•

■

'

♦

■

.

■

'

V

Contents

CHAPTER 1

Concepts of Experiments: Design and Analysis .

1.1 Design of Experiments and Collection of Data 1
1.2 Experiments and their Designs 2
1.3 Methodology for Making Inferences 3
1.4 Three Principles of Designs of Experiments 7
1.5 Experimental Error and Interpretation of Data 8
1.6 Contrasts and Analysis of Variance 10
1.7 Models and Analysis of Variance 16
1.8 Two-Way Classified Data 26
1.9 Assumptions of Analysis of Variance 43

CHAPTER 2

Complete Block Designs

2.1 Completely Randomized Designs 48
2.2 Randomized Block Designs 52
2.3 Latin Square Designs 56
2.4 Missing Observations in Randomized Block Designs 64
2.5 An Illustration 74

CHAPTER 3
Factorial Experiments

3.1 Characterization of Experiments 78
3.2 Factorial Experiments 79
3.3 Factorial Experiments with Factors at Two Levels 80
3.4 Finite Fields and Designs of Experiments 83
3.5 Grouping for Interaction Contracts 85
3.5 Confounding 86
3.7 Confounding in more than Two Blocks 89
3.8 Experiments with Factors at Three Levels Each 91
3.9 A General Method of Construction of Confounded

Factorials 97

3.10 Maximum Number of Factors to Save Interactions upto a

Given Order for a Given Block Size 103

3.11 Analysis of Factorial Experiments 105
3.12 Fractional Factorials 107

VI

CHAPTER 4
Asymmetrical Factorial and Split-Plot Designs

4.1 Asymmetrical Factorial Designs 120
4.2 Confounded Asymmetrical Factorials 120
4.3 Construction of Balanced Confounded Asymmetrical

Factorials 122

4.4 Construction of Confounded Asymmetrical Factorial

vx22 in 2v plot Blocks 131

4.5 Analysis of Balanced Confounded Asymmetrical Factorials 133
4.6 Split-Plot Designs 143
4.7 Analysis 144

CHAPTER 5
Incomplete Block Designs

5.1 Varietal Trials 152
5.2 Incomplete Block Designs 153
5.3 Balanced Incomplete Block Designs 156
5.4 Construction of B.I.B. Designs 158
5.5 Analysis 166
5.6 Analysis with Recovery of Inter-Block Information 168
5.7 Youden Squares 172
5.8 Lattice Designs 172
5.9 Partially Balanced Incomplete Block Designs 176
5.10 Analysis of P.B.I.B. Designs 183
5.11 Analysis with Recovery of Inter-Block Information 186
5.12 Optimality of Designs 198

CHAPTER 6
Orthogonal Latin Squares

6.1 Orthogonal Latin Squares 205
6.2 Maximum Number of Orthogonal Latin Squares 205
6.3 Construction of Orthogonal Latin Squares 206
6.4 Construction of Orthogonal Latin Squares by Using

Pairwise Balanced Designs 209

CHAPTER 7

Designs for Bio-assays and Response Surfaces

7.1 Bio-assays 277
7.2 Direct Assays 218
7.3 Indirect Bio-assays 220
7.4 Parallel Line Assays 224

CONTENTS

vii

7.5 Incomplete Block Designs for Bio-assays 229
7.6 Slope Ratio Assays 236
7.7 Response Surface Designs 244

CHAPTER 8

Analysis of Covariance and Transformation

8.1 Analysis af Covariance 263
8.2 Analysis of Covariance for Randomized Block Designs 263
8.3 Analysis of Covariance of Completely Randomized and

Latin Square Designs 267

8.4 Analysis of Covariance of Non-Orthogonal Data and Designs

in Two-Way Classification 267

8.5 Analysis of Covariance with Two Ancillary Variates 272
8.6 Covariance and Analysis of Experiments with Missing

Observations 274
8.7 Transformations 275

CHAPTER 9
Weighing Designs

9.1 Introduction 280
9.2 Definition 280
9.3 Method of Estimation 281
9.4 Incomplete Block Designs as Weighing Designs 282
9.5 Two Pan Weighing Designs from B.I.B. Designs 296
9.6 Two Associate P.B.I.B. Designs as One Pan Weighing

Designs 289

9.7 Weighing Designs from Truncated Incomplete B.I.B.

Designs 290

9.8 Efficiency 290

v; 1 , -&C '■c-5

■

\ ;■ i’■■■■"' ' " -.fr . ■■■/?■ . ■ :

• ' ■ LI l&i ,

. ■'r“ . ' ■ ' :

I

.

'

r ;i:

• »

. .. , • ’ "i . - '•>. ' • s4- ■' ' •' • *

CHAPTER 1

Concepts of Experiments:
Design and Analysis

1.1 Design of Experiments and Collection of Data

Experimentation and making inferences are twin essential features of
general scientific methodology. Statistics as a scientific discipline is
mainly designed to achieve these objectives. It is generally concerned
with problems of inductive inferences in relation to stochastic models
describing random phenomena. When faced with the problem of studying
a random phenomenon, the scientist, in general, may not have complete
knowledge of the true variant of the phenomenon under study. A
statistical problem arises when he is interested in the specific behaviour
of the unknown variant of the phenomenon.

After a statistical problem has been set-up, the next step is to perform
experiments for collecting information on the basis of which inferences
can be made in the best possible manner.

The methodology for making inferences has three main aspects. First,
it derives methods for drawing inference from observations when these are
not exact but subject to variation. As such, the inferences are not exact
but probabilistic in nature. Second, it specifies methods for collection
of data appropriately so that the assumptions for the application of
appropriate statistical methods to them are satisfied. Lastly, techniques
for proper ^interpretation of results are devised. There has been a great
advance in the derivation of statistical methods applicable to various
problems under different assumptions. A good coverage of these methods
is available in Fisher (1953), Giri (1976) and Scheffe( 1959). A good deal
of work has also been done in the field of data collection and interpreta¬
tion techniques. The topic of the present book, viz., design and analysis
of experiments falls in the sphere of data collection and interpretation
techniques. The other main topic in this regard is the theory of sample
surveys. Though the theories of sample surveys and design of experi¬
ments are both concerned with data collection techniques, they serve
different purposes. The theory of sample surveys has the objective of
deriving methods for collection of samples of observations from a popu¬
lation which exists in its own way such that the sample can adequately
represent and accurately interpret the population. In the case of experi¬
mental data no such population exists in its own way. What exists is a
problem and the data have, so to say, to be manufactured by proper

2

DESIGN AND ANALYSIS OF EXPERIMENTS

experimentation so that an answer to the problem can be inferred from
the data. Creation of controlled conditions is the main characteristic
feature of experimentation. It is the design of an experiment which specifies
the nature of control over the operations in the experiments. Proper
designing is necessary also to ensure that the assumptions required for
appropriate interpretation of the data are satisfied. Designing is necessary,
moreover, to increase accuracy and sensitivity of the results.

Data obtained without regard to the statistical principles cannot lead
to valid inferences. They can, no doubt, be analyzed, but the results
obtained from them need not hold true subsequently in situations other
than those in which they were collected. For example, if two varieties of
a crop are to be compared with regard to their yield performance by
conducting an experiment, and a particular variety which the experimenter
for some personal reasons, say, wants to favour, is allotted to the better
plots, then the statistical principles are violated in the experiment and the
data collected from the experiment cannot be validly interpreted. Their
interpretation may show the favoured variety more promising. But the
same result may not be obtained in future when the variety does not
receive a favoured treatment. It is, therefore, necessary that the data are
collected by adopting proper designs so that they can be validly inter¬
preted. For further reading on this topic Fisher (1953), Kempthorne(1952),
and Federer (1955) maybe consulted.

1.2 Experiments and their Designs

As already stated an experiment starts with a problem, an answer to which
is obtained from interpretation of a set of observations collected suitably.
For this purpose a set of experimental units and adequate experimental
material are required. Equal sized plots of land, a single or a group of
plants, etc. are used as experimental units for agricultural experiments.
For animal husbandary experiments animals, animal organs, etc. form the
experimental units. Again, for industrial experiments machines, ovens and
other similar objects form the experimental units.

The problems are usually in the form of comparisons among a set of
treatments in respect of some of their effects which are produced when
they are applied to the experimental units. A general name ‘treatment'
will be given throughout the book to denote experimental material among
which comparison is desired by utilizing the effects which are produced
when the experimental material is applied to the experimental units.

For example, in agricultural experiments different varieties of a crop,
different fertilizer doses, different levels of irrigation, different combinations
of levels of two or more of the above factors, viz. variety, irrigation,
nitrogen fertilizer, date of sowing, etc. may constitute the treatments.

Given a set of treatments which can provide information regarding the
objective of an experiment, a design for the experiment defines the size

CONCEPTS OF experiments: design and analysis

3

and number of the experimental units, the manner in which the treatments
are allotted to the units and also the appropriate type and grouping of the
experimental units. These requirements of a design ensure validity,
interpretability and accuracy of the results obtainable from an analysis of
the observations. These purposes are served by the principles of
(i) randomization which defines the manner of allocation of the treatments
to the experimental units, (ii) replication which specifies the number of
units to be provided for each of the treatments and (iii) error control
which increases the precision by choosing appropriate type of experimental
units and also their grouping.

1.3 Methodology for Making Inference

The basis for making statistical inference is one or more samples of
observations from one or more variables. These observations are required
to satisfy certain assumptions. Some of the assumptions are that the
observations should belong to p. population having some specified
probability distribution, and that they should be independent. The,
distribution which is usually assumed is the normal distribution because
most of the variables encountered in nature are found to have this distri¬
bution. Such distributions involve certain unknown quantities called
parameters which differ from variable to variable. The main purpose of
statistical inference is, (i) to estimate such parameters by using the obser¬
vations, and (ii) to compare these parameters among themselves again by
using the observations and their estimates. The methodology dealing
with the first part of the inference has developed into what is known as
theory of estimation and that for the second part into methods of testing
of hypothesis. The maximum likelihood method of estimation and the
least squares method of estimation are the two more important methods of
estimation. The least squares method of estimation gives the same estimate
as that of the maximum likelihood method of estimation under normality
assumption. This method has been discussed in Section 1.7. The details
about these methods are available in publications on statistical methodology
cited in Section 1.1.

For testing of hypothesis, first certain hypothesis involving the
parameters is made. The hypotheses are of comparative nature and
depend on the type of inference problems. For example, let there be two
varieties of a crop denoted by vx and v2, there being n1 observations of
yield on vx from plots each of a given size and w2 observations on v2 from
similar plots. Further, let the observations of the ith variety (i = l, 2)
have the normal distribution

at \/2tt

where y denotes the variable of yield of the crop, pi is the mean yield and
ffi2 is the variance of the ith variable.

4

DESIGN AND ANALYSIS OF EXPERIMENTS

By using the two samples of observations, and af can be estimated
by adopting an appropriate method of estimation. In regard to testing
of hypothesis we have two problems of comparison—one being the
comparison between o1 and c2 and other between and (x2. For the
purpose of comparison an hypothesis of the type al=c2 or y-1=ii2 is made.
This type of hypothesis which specifies that the difference between any
pair of a number of similar parameters is zero, is known as the null
hypothesis.

Next, a statistic, that is, a function of the observations, is defined so
as to suit the objective of the problem. This is called the test statistic as
it is used to test the tenability or otherwise of the hypothesis.

Let us imagine a very large number of independent samples of obser¬
vations from a population under investigation. From each such sample
a value of a statistic can be obtained. Thus, there will be as many values
of the statistic as the number of samples. We can now think of a
probability distribution of these values of the statistic. Such a distribution
is called the sampling distribution of the statistic.

For testing of hypothesis first the sampling distribution of a test
statistic is theoretically derived assuming that the hypothesis regarding
the parameters of the original population of the observations is
correct From the sampling distribution it is possible to evaluate
the probability of occurrence of the value of the test statistic lying in
given ranges of values. For example, one can evaluate the probability
of assuming by a test statistic, T all values which are greater than a given
value, say, T0 or less than a value T0' or which lie between T0 and T0\
Usually, for specific test statistic tables are prepared showing different
values of T0 and the corresponding probability or vice versa. Such tables
are available in Fisher and Yates (1942). Evidently, the larger T0 deviates
from its central or most expected value, the less is the probability of
getting samples which provide T greater than T0. For testing of hypothesis,
usually two values of T0 are important, one of these corresponds to 5 per
cent probability of having samples giving T greater than T0 when the
hypothesis is correct and the other corresponds to 1 per cent probability of
having samples giving T greater than T0. We may call these two values
of T0 as r.95 and T.go respectively or in general T,_a corresponding to a
per cent probability. These are called respectively the 5 per cent, 1 per
cent and a per cent values of significance. We have said earlier that for
testing of hypothesis the value of a suitable test statistic is calculated
from the observations. If this value of the statistic is greater than its
tabulated value at 5 per cent level of significance, the probability of getting
such samples as has given the value is less than 5 per cent if the hypothesis
is correct. This, in other words, means that the correctness of the hypothesis
is greatly doubtful. When the sampling distribution of a statistic is
symmetrical, a similar conclusion is also possible if T is less than r.05, as
the sample value of T is too small in such cases. Hence, in such a situation

CONCEPTS OF experiments: design and analysis

5

the hypothesis is rejected at 5 per cent level of significance. This shows that
we are likely to reject a correct hypothesis in 5 per cent of the samples.
If, again, the calculated value of the test statistic is greater than its tabulated
value at 1 per cent level of significance, the probability of getting such
samples as has given the value is less than 1 per cent if the hypothesis is
correct. In this case the hypothesis is rejected at 1 per cent level of
significance. Evidently, rejection at 1 per cent level of significance carries
more definite information than rejection at 5 per cent level of significance,
because when we reject an hypothesis at 1 per cent level we are likely
to reject a correct hypothesis for 1 per cent samples while in the case of
5 per cent level rejection we are likely to reject a correct hypothesis in
5 per cent cases. Thus, in the 1 per cent case we are likely to be in less
error by rejecting an hypothesis.

Though we have discussed the test procedure with reference to 5 per
cent and 1 per cent levels of significance, it is not necessary that testing
should be restricted to only these two levels. Tables are available for
testing at other levels of significance if so required. For example, in a
situation where more definite information is required, a test at 0.1 per cent
level of significance can be applied.

In relation to design and analysis of experiments, two test statistics,
viz. (i) /-test for testing the significance of the difference between two linear
estimates, and (ii) F-test or variance ratio test for testing equality of two
variances, are usually applied. Some of the hypotheses tested by, these
tests are discussed below:

Case I: One sample from a normal population with mean g.. When the
problem is to know if p. differs from a given or conjectured value the
hypothesis (x=^0 is made. The test statistic to be applied in this case is
called one sample /-test and is taken as

y-Fo
VsZln

where y is the sample mean based on n observations from a normal
population and s2 is the error mean square given by (l(y—y)2/(n—l) and
has («—1) degrees of freedom (d.f.). The concept of degrees of freedom
has been discussed in a later section.

Here, / is said to have the degrees of freedom of s2, that is, n— 1. The
5 per cent or 1 per cent values of / depend on the d.f. of / and are tabulated
for different values of d.f. Usually, /-table is prepared by showing the
5 per cent level of significance as /.975. This is done in consideration of
the fact that / has a symmetrical distribution and can be both positive and
negative as the mean of the /-distribution is zero. Actually, /.025 is negative
and the probability of / being less than /.025 is .025. Thus, the 5 per cent
significance value of / is a value, say, /„' such that the probability of having
samples to give values of / exceeding /„' is 2.5 per cent and that of having

6

DESIGN AND ANALYSIS OF EXPERIMENTS

samples to give values of t less than —/„' is 2.5 percent so that the
probability of t being greater than t0 or less than —10 is 5 per cent. This
type of test which takes into account the probability of occurrence of
extreme values of a test statistic on either direction of its mean value is
known as two-tailed test. In such cases the alternatives to the hypothesis,
viz. do not specify the nature of difference, that is, whether the
difference should be only positive or only negative. The hypothesis
which specify the direction like the alternative being \x > {*„, leads
to one-tailed test. In such tests the 5 per cent level of significance corres¬
ponds to t.05. Though we have discussed the test with reference to 5 per
cent level of significance, the same considerations and procedures apply to
tests at other levels of significance.

Case 2: Two samples from two normal populations having means Ui and
{a2 and a common variance. Setting the problem to test if the estimates
of mean from the two samples are homogeneous, the hypothesis
is made. The test statistic / is defined as

y*—y

where yx and y2 are the means of the two samples of sizes ftj and n2
respectively,

v2-.^ Q’lf "ki)2+

«l + «2 —2

yu and y2i denoting observations from the two samples.

Here, the d.f. of t is nx-\-n2—2. The table of t is the same for both one
sample and two sample tests. There are other situations where /-test is
applied. Full discussion on the topic has been given in Snedecor (1946),
Goulden (1952) and other books on statistical methods.

Case 3: Variance ratio or F-test. Let mean squares, sx2 and s22 be two
estimates of variance a2 given by

-?>* and (*;-*>*
— 1

n2-1

obtained from two samples yx, y2,.. •, ynx and xx, x2,,... xna from two
normal populations having variances, ax2 and a22 respectively. In order to
test if the mean squares sx2 and s22 can be considered to be of equal order,
the hypothesis ct12=ct22 is made. It is tested by defining the test-statistic, F
given by

F~S-~ with — 1 and n2~ 1 d.f.

s22

F-table has been so prepared that Fis always greater than 1. Thus, Fhas

CONCEPTS OF experiments: design and analysis

7

to be taken as either sf/s^ or 522/jx2, whichever is greater than one. If,
however, it is intended to test if one, say, sx2 is greater than 522, then the
ratio should be s^/s^ and no test is required if sx2 < s22. We shall
encounter this type of situation mostly in this study.

It is not always necessary that sx2 and s22 should be calculated from
two independent samples. What is necessary is that ^x2 and s22 should be
two independent mean squares.

For details of this topic the reader may consult Lehmann (1959).

1.4 Three Principles of Designs of Experiments

We have seen that randomization, replication and error control are the
three main principles of designs of experiments. The roles they play in
data collection and interpretation are discussed below.

Randomization

After the treatments and the experimental units are decided the treatments
are allotted to the experimental units at random to avoid any type of
personal or subjective bias whiqh may be conscious or unconscious. This
ensures validity of the results. It helps to have an objective comparison
among the treatments. It also ensures independence of the observations
which is necessary for drawing valid inference from the observations by
applying appropriate statistical techniques.

We shall see subsequently that depending on the nature of the experi¬
ment and the experimental units, there are various experimental designs.
Each design has its own way of randomization. We shall, therefore,
discuss the procedure of random allocation separately while describing
each specific design. However, for a thorough discussion on the subject
the reader may see Fisher (1942), Kempthorne (1952) and Ogawa (1974).

Replication

If a treatment is allotted to r experimental units in an experiment, it is
said to be replicated r times. If in a design each of the treatments is
replicated r times, the design is said to have r replications. Replication
is necessary to increase the accuracy of estimates of the treatment effects.
It also provides an estimate of the error variance which is a function of
the differences among observations from experimental units under identical
treatments. Though, the more the number of replications the better it is,
so far as precision of estimates is concerned, it cannot be increased
indefinitely as it increases cost of experimentation. Moreover, due to
limited availability of experimental resources too many replications

cannot be taken. ,

The number of replications is, therefore, decided keeping in view the

8

DESIGN AND ANALYSIS OF EXPERIMENTS

permissible expenditure and the required degree of precision. Sensitivity
of statistical methods for drawing inference also depends on the number
of replications. Sometimes this criterion is used to decide the number of
replications in specific experiments. A more detailed discussion of this
topic is deferred till a discussion of experimental error is made. The
principle of error control will also follow the same discussion.

1.5 Experimental Error and Interpretation of Data

After the observations are collected they are statistically analysed so
as to obtain relevant information regarding the objective of the experiment.
As we know, the objective is usually to make comparisons among the
effects of several treatments when the observations are subject to variation.
Such comparisons are made by the technique of analysis of variance. It
will be seen subsequently that inference is drawn through this technique
by comparing two measures of variation, one of which arises due to
uncontrolled sources of variation, called the error variation and the other
includes variation due to a controlled set of treatments together with the
variation due to all the uncontrolled causes of variation contributing to
the error variation.

For example, let there be six plots of land denoted by Pl5 P2, P3, p4,
P5 and P6. The first three plots receive one treatment, say, and the
last three, another treatment, tz. Suppose, further, that plots P, and P4
receive one level of irrigation, P2, P5, another level and P3, P6, a third
level. Let ylf y2, y3, y4, y5 andjs denote the observations on a character
recorded from the above six plots in that order. Then the comparison
Pi~y-i which denotes the variation in the observations from the first two
plots, does not contain any component of variation due to the treatments
as both of them receive the same treatment. But the comparison is not
free from the effect of the other controlled factor viz. irrigation as Pt
received one level of irrigation while P2 received another level. Hence,
this comparison by itself does not contribute to error variation, But the
comparison (yt— y2)~is> evidently, free from the variability caused
by both the controlled factors, viz. treatment and irrigation. Hence, such
comparisons which contain contributions due to uncontrolled factors like
soil fertility and management variation which were not specified in the
plots, build up error variance. The actual measure of error variance is a
function of the squares of all such comparisons. The procedure of
obtaining it has been discussed in the next section. There are, again, some
other concepts of experimental error which we shall discuss at appropriate
places.

Determination of Number of Replications

Error variance provides a measure of precision of an experiment, the less the

CONCEPTS OF experiments: design and analysis

9

error variance the more is the precision. Once a measure of error variance
is available for a set of experimental units, the number of replications
needed for a desired level of sensitivity can be obtained as below.

Given a set of treatments an experimenter may not be interested to
know if two treatments differ in their effects by less than a certain
quantity, say, d. In other words, he wants an experiment which should be
able to differentiate two treatments when they differ by d or more.

As discussed in the previous section the significance of the difference

between two treatments is tested by /-test where

t _ yt—yj
V 2 s2/r

Here, yt, and yj are the arithmatic means of two treatment effects each

based on r replications, s2 is a measure of the error variation.

Given a difference d, between two treatment effects such that any
difference greater than d should be brought out as significant by using a
design with r replications, the following equation provides a solution of r:

r=-L£L X
0 V2s2/r ’

where /0 is the critical value of the /-distribution at the desired level of
significance, that is, the value of / at 5 or 1 per cent level of significance
read from the table. If s2 is known or is based on a very large number
of observations, made available from some pilot pre-experiment investi¬
gation, then / is taken as the normal variate. If .s2 is estimated with
n degrees of freedom (d.f.) then /„ corresponds to n d.f.

When the number of replications is r or more as obtained above, then
all differences greater than d are expected to be brought out as significant
by an experiment when it is conducted on a set of experimental units
which has variability of the order of s2.

For example, in an experiment on wheat crop conducted in a seed
farm in Bhopal, India to study the effect of application of nitrogen and
phosphorus on yield, a randomized block design with three replications
was adopted. There were 11 treatments two of which were (i) 10 lb/acre
of nitrogen (ii) 20 lb per acre of nitrogen. The average yield figures for
these two applications of the fertiliser were 1438 and 1592 Ibs/acre
respectively and it is required that differences of the order of 150 lb/acre
should be brought out significant. The error mean squares 02) was
12134.88. Assuming that the experimental error will be of the same
order in future experiments and t0 is of the order of 2.00, which is likely
as the error d.f. is likely to be more than 30 as there are 11 treatments,
we have all the information to obtain the numbers of replications r from

the relation:

/ - |J|-

#“V2Wr

10

T hat is

DESIGN AND ANALYSIS OF EXPERIMENTS

2f0V 2x22x 12134.88

1502
d2 1502

=»=4 (approx.)

Thus, an experiment with 4 replications is likely to bring out differences
of this order as significant.

Another criterion for determining r is to take a number of replications
which ensures at least 10 d.f. for the estimate of error variance in the
analysis of variance of the design concerned since the sensitivity of the
experiment will be very much low as the F test which is used to draw
inference in such experiments, is very much unstable below 10 d.f.

The above considerations for determining the number of replications

holds only for specific designs.

Error Control

The considerations in regard to the choice of number of replications
ensure reduction of standard error of the estimates of the treatment
effects because the standard error of the estimate of a treatment
effect is Vs2jr. But they cannot reduce the error variance itself, though a
large number of replications can ensure a more stable estimate of the error
variance. It is, however, possible to devise methods for reducing the error
variance. Such measures are called error control or local control. One
such measure is to make the experimental units homogeneous. Another
method is to form the units into several homogeneous groups, usually
called blocks, allowing variation between the groups.

A considerable amount of research work has been done to divide the
treatments into suitable groups for allotment to groups of experimental
units so that the treatment effects can be estimated more precisely. Extensive
use of combinatorial mathematics has been made for formation of such
groups of treatments. These have been discussed in a later chapter.
Adequate coverage of the combinatorial aspects of this topic is available in
Bose (1939) and Raghavarao (1971).

1.6 Contrasts and Analysis of Variance

The main technique adopted for the analysis and interpretation of the data
collected from an experiment is the analysis of variance technique which
essentially consists of partitioning the total variation in an experiment into
components ascribable to different sources of variation due to the controlled
factors and error.

The following discussion attempts to relate the technique of
analysis of variance to comparisons among treatment effects which in terms
of symbols can be called contrasts.

CONCEPTS OF experiments: design and analysis

11

Contrast

Let ylt y2,... ,y„ denote n observations or any other quantities. The linear

n »

function C=X 1 tfi where l/’s are given numbers such that Y 1<=0, is

i-i i

n

called a contrast of j/’s. The restriction X 1*=0» makes C a comparison

among the y values.

i

If ylf y2,... ,yn are independent random variables with a common mean
(x and variance a2, the expected value of the ramdon variable, C is zero and

the variance is c2 Y l*2. In what follows we shall not distinguish between

n

a contrast and its corresponding random variable.

i-i

Sum of squares (s. s) of contrasts. The square due to the contrast C is
defined as C2/2 l,2. It is known that this square has a a2X2 chi-square
distribution with 1 degree of freedom (d.f.) when the yi s are normally
distributed. Thus, the sum of squares due to two or more contrasts has
also a a2X2 distribution if the contrasts are independent.

Multiplication of any contrast by a constant does not materially change
the contrast. The square due to a contrast as defined above is not
evidently changed by such multiplication.

Orthogonal contrasts. Two contrasts, Cx=X anc^ X miyi, are

I i

said to be orthogonal if ^ 1< mj=0.

i

This condition ensures that the convariance between Cx and C2 is zero

when the observations are independent, because

n

cov (Cl5 C2)=o2 Y. 1* mi

i

When there are more than two contrasts, they are said to be mutually

orthogonal, if they are orthogonal pairwise.

For example, when there are four observations yx, y2, y2 and yi} we can

write the following three mutually orthogonal contrasts:

(t) Jl+^2-.V*

(u) yi-y2-ya+y*

(iii) yi—yi+yz—y*

The sum of squares due to a set of mutually orthogonal contrasts has a
a2*2 distribution with as many degrees of freedom as the number of

contrasts in the set.

12

DESIGN AND ANALYSIS OF EXPERIMENTS

Maximum number of orthogonal contrasts. Given a set of n values
,Vi> - the maximum number of mutually orthogonal contrasts among
them is n— 1.

Proof: Suppose we have the following m mutually orthogonal contrasts:

Ci=Z lj iyi
1

n

c2=Z iztyi
i

C*=Z lml }>i
1

Let us now take one more contrast C— Z liyi where l/’s are unknown but

71

i

satisfy £ 1,-0. Now, C can be orthogonal to each of the above m

contrasts if the following simultaneous equations in /,’* have at least one
non-zero solution:

Z l/=0
i

Z lull-0
t

z hi 1*=0

Z 1 mi l/=0
i

But this set of homogeneous linear equations in n unknowns can have
a non-zero solution, only if the total number of equations does not exceed
n-l. Thus, m can be at the most n-2 and the total number of such
contrasts cannot exceed n— 1. This proves that the maximum number of
mutually orthogonal contrasts among n quantities is n— 1 and that the
contrasts can be written in more than one way as there is an infinite
number of solutions of the homogeneous equations Q. E. D.

One way of writing such contrasts is to progressively introduce the

values as below:

(i) yi-yz
(“) Ti+Tg—2ys

(iii) Ti+T2+T3-3v4

and so on.

CONCEPTS OF experiments: design and analysis

13

Another set of orthogonal contrasts for various values of n is available
in the tables for Statisticians and Biometricians prepared by Fisher and
Yates (1942) under the name of Orthogonal polynomials.

Measures of Variation

The square of a contrast gives a measure of variation due to the contrast.
The sum of squares due to the (n— 1) mutually orthogonal contrasts of n
observations, gives the s.s. due to the n observations. This s.s. divided by
the number of independent contrasts on which it is based viz. (n—1) gives
a measure of variation of the observations and is called mean squares (m.s.)
The number of independent contrasts on which a s.s. is based is called the
degrees of freedom (d.f.) of the sum of squares.

We have seen in Section 1.4 that certain contrasts represented
variation due to uncontrolled causes of variation while certain others did
not. The s.s. due to contrasts which represent variation due to only
uncontrolled causes of variation builds up error variance. Again, the s.s.
due to some other contrasts which are orthogonal to the above error
contrasts and represents comparisons among effects of, say, a set of
treatments, build up the treatment s.s.

For illustration let us take the case discussed in Secton 1.4 as
reproduced in Table 1.1. The figures shown in bracket are the obser¬
vations on wheat yield collected from an actual experiment conducted in an
experimental station in Betul, India with three irrigation treatments viz.

Ix: no irrigation,
h: one irrigation at tillering

and /3: two irrigations, one at tillering and one at flowering stage

with two manurial treatments,

tl: 15 lbs/acW-f-15 Ibs/ac(/\05)
i2: 80 lbs/acAH-80 lbs/ac (P205)

These figures have been extracted from the publication entitled National
Index of field experiments, M.P. (1954-59) published by IARS, New Delhi.

TABLE 1.1
Yield Data from the Irrigation Experiment (lb/acre)

Treatments

h

h

h

3*u
(837)

3*21
(914)

Irrigation levels

h

3*12
(804)

3*22
(758)

h

3*13
(843)

3*23
(849)

Marginal total

3*11+3*12+3*13
(2484)
3*21 + 3*22 + 3*23
(2521)

Totals

3*11+3*21
(1751)

3*12 4"3*22
(1562)

3*13 + 3*23
(1692)

2 3*//
(5005)

14

DESIGN AND ANALYSIS OF EXPERIMENTS

Here, yu (/= 1,2, y=l, 2, 3) denotes the observation from the ith treatment

and yth level of irrigation.

It will be seen that the following two orthogonal contrasts are free
from the effects of the two controlled factors viz. treatments and irrigation:

(i) 0'u->,2i)-0'i2-J’22)
00 O'ls-Jaaj

Each of these contrasts is actually a contrast of contrasts. In a contrast
of two observations in the same column, the effect of irrigation is removed.
Again, by taking contrast of such contrasts the effect of treatment is
eliminated. Evidently, it is not possible to obtain any more error contrast
which is orthogonal to each of the above two error contrasts. Hence, the
s.s. due to error variation, in short, error s.s. can be obtained by adding
the squares of these two contrasts. This s.s. has two d.f.

Again, let us take the contrast

O'l+J'a+J's) ~ O^+Ts+ya)

It is easily seen that this contrast gives a comparison between the effects
of the two treatments. This contrast is not affected by the effects of the
irrigation levels as they are evenly distributed in the positive and negative
parts of the contrast. There is no other contrast orthogonal to the above
which also represents purely treatment comparison. This contrast is also
orthogonal to each of the two error contrasts presented earlier.. We get the
treatment s.s. by obtaining the square of the above contrast and dividing
it by the appropriate factor as indicated earlier. It has evidently 1 d.f.
On the hypothesis that there is no variation among the treatment effects,
the treatment s.s. is distributed as c2/2 withl d.f. Thus, on the above
hypothesis both the error m.s. and treatment m.s. have the same expected
value, a2. They are independent as they are obtained from orthogonal
contrasts. Their ratio, F, can, therefore, be used to provide a test of the
hypothesis of equality of the treatment effects.

To complete the analysis of variance, we have yet to account for two
more orthogonal contrasts each of which is orthogonal to the three
contrasts already discussed. We can write these two contrasts as below
from the irrigation marginal totals:

0) (>;U+^2l)-(>’x* + ^22)

(ii) (>;iX+3;2x) + (>,ia+>’22)-2 Oia+J^)

They represent comparison of irrigation effects and their s.s. gives a
measure of variation due to irrigation effects.

Table 1.2 shows in a compact form the details of the analysis of

variance obtainable from the contrast approach.

As the figures in bracket in Table 1.1 are averages based on 4 observations
each, the actual divisors for getting the s.s. is 1/16 times each of the
divisors shown in col (3) of table 1.2 for the different s.s. The s.s. obtained

CONCEPTS OF experiments: DESIGN AND ANALYSIS

15

e
l
b
a
T

e
c
n
a
i
r
a
V

f
o

s
i
s
y
l
a
n
A

~
?
i
y
X

l
a
t
o
T

16

DESIGN AND ANALYSIS OF EXPERIMENTS

from the revised divisors can be considered to be based on the original
observations rather than on the averages shown in the table.

Though the above analysis helps to have a clear understanding of the
technique and its rationale, it need not be adopted to analyze larger
numbers of observations, as there are simpler methods for obtaining such
sums of squares. The present method has, however, the advantage that
special components of variation in which an experimenter may be interested
can be easily obtained and tested through this technique.

1.7 Models and Analysis of Variance

The method of analysis described in the previous section was more a
deduction from intuitive arguments. It did not clearly specify the nature
of the treatment or error effects, that is, if they are fixed or random. In
order to provide a more rigorous basis and a sound statistical treatment
another representation of analysis of variance based on postulated models
has been given below briefly. Both these methods, however, lead to the
same ultimate results so far as our present objective is concerned.

A statistical model is actually a linear relation of the effects of the
different levels of a number of factors involved in an experiment along with
one or more terms representing error effects. The effects of any factor can
be either fixed or random. For example, the effects of two well defined
levels of irrigation are fixed as each irrigation level can be reasonably taken
to have a fixed effect. Again, if the variety of a crop is taken as a factor
with a number of varieties of the crop as its levels, then the effects of the
varieties will be random if these varieties are selected at random from a large
number. The random effects can again belong to a finite or an infinite
population. The error effects are always random and may belong either
to a finite or infinite population.

A model in which each of the factors has fixed effects and only the error
effect is random is called a fixed model. Models in which some factors
have fixed effects and some random effects are called mixed models. Again,
models where all the factors have random effects are called random models.
Depending on the finiteness or otherwise of the random effect populations,
mixed and random effect models can be of many different types. A
detailed discussion of this topic is, however, not the objective of this
section. Readers are referred to Wilk and Kempthorne (1955) for details
on the topic.

In fixed effect models, the main objectives are to estimate the effects,
find a measure of variability among the effects of each of the factors and
finally find the variability among the error effects. In random effect models
the main emphasis is on estimating the variability among the effects of the
different factors. The methodology for obtaining expressions of variability
is, however, mostly the same in the different models, though the methods
appropriate for their testing are different.

CONCEPTS OF experiments: design and analysis

17

We shall restrict ourselves in this publication to mainly fixed effect

models. A fixed effect model for, say, two factors is written as below:

y»k—[a+ at+bj+euk

where yuu is an observation coming from a unit defined by the levels i,j, k
of the factors involved, at is the effect of the i-th level of one factor, say,
A and bj is the effect of another factor, say, B and etJk is an error effect
which is assumed to be normally and independently distributed with zero
mean and a constant variance a2. These assumptions regarding behaviour
of etjk are necessary for drawing inference by adopting known statistical
methodology. The methodology that is adopted is the analysis of variance
technique by which inference is drawn by applying F test. For the F test
it is necessary that the observations, that is, the error components should
be normally and independently distributed with a common variance. Thus,
while collecting observations by adopting various designs to be discussed
subsequently it has to be ensured that these assumptions are satisfied by
the observations, otherwise no valid inference can be drawn from their.
analysis.

A further assumption that has been made in the model is that the effects
are additive. Though often this assumption is satisfied, it is desirable to
get it tested preferably in relatively less known situations. A test due to
Tukey (1949) is available for this purpose.

Though we have presented above a model involving two factors, there
can be other types of models depending on the nature of data, that is, the
number of controllable factors involved in the data classification. For
example, if the data are from the different levels of a single factor, then we
call the data as one-way classified data and it has its own model. In
general, if the data belong to the level combinations of m different factors,
we call them m-way classified data. Further discussions about classification
of data and their models have been made in subsequent sections.

After a model has been fixed, the general method of analysis takes the

following steps.

Let the model be denoted in general by

ah bj, c*) + <?

where y donotes the observations, e, the error effects and /((a, at, bj, Ck), a
linear function of the fixed effects of different factors. Since

e=y-f([i, at, bj, ck)

is normally and independently distributed, the estimates of the constant
effects [x, di, bj etc. can be obtained by the maximum likelihood method of
estimation which in the present case gives the same estimate as the least
squares method of estimation. That is, let

where the summation is over the observations. Then by solving the normal

{y-f(\h “I> bj, Ck)}2 (1.1)

18

DESIGN AND ANALYSIS OF EXPERIMENTS

equations obtained by partially differentiating E with respect to fx, ah bj
etc., and equating them to zero, we shall get as many normal equations as
the number of constants, or effects, that is,

f£-0, (i=l, 2, ...p, say), ^=0(./=l, 2,...?.say) etc.
d[L cdi ooj

are the normal equations by solving which estimates of the effects can be
obtained. It can be shown that all these normal equations are not
independent. As such unique solutions for the effects are not available.
Solutions are, however, available only when the sum of the effects of each
factor is assumed to be zero. The implication of such assumptions has
been discussed subsequently.

Once the estimates are available as above, we can get the value of E
when the estimates of the effects are substituted in (1.1). The value of E
thus obtained is called the error s.s. It is said to have degrees of freedom
equal to N—k where N is the total number of observations and k is the
total number of independent normal equations. Clarification of the
concept of degrees of freedom has been given at the end of the section
1.7.2.

The next problem is to obtain the variability due to the effects of a
factor and compare it with the error variability. An hypothesis about the
effects of this factor is then made. The hypothesis is usually that the
effects of the different levels of the factor are equal, that is, each effect is
zero by virtue of the fact that their sum is zero. On this hypothesis we
get another model in which the effects of the factor under test is absent.
On this model also we can get another error s. s., say, Ex. Actually, Ex
contains the variability due to the effects of the factors under test and also
the error variability. Thus, Ex—E gives a measure of the variability due
to effects of the factor under test and is called the s. s. due to the factor.
Its d.f. is one less than the number of levels of the factor. Next, the mean
squares (m. s.) for each of error s. s. and the s. s. due to the factor are
obtained by dividing the s. s. by their respective d. f. These two m. s’s are
independent and hence their ratio is tested by the variance ratio test. The
hypothesis here is that both these mean squares have the same expected
values which is possible only when all the effects under test are equal.
After this general discussion of analysis of variance we have discussed
below specific types of data and the details regarding their analysis.

1.7.1 Types of Data

As the method of analysis based on model depends on the type of data,
we have defined below several types of data.

One-way classified data: When a set of observations is distributed
over the different levels of a factor, they form one-way classified data. Let
us take a factor, say, at k levels. Let there be m observations denoted by

CONCEPTS OF experiments: design and analysis

19

yu |’ 2’ ' ,Tjfj against the zth level. Then the observations yu classified

in k groups according to the k levels of the factor are said to form one¬
way classified data.

Two-way classified data: Similarly, if we take two factors simultane¬
ously, say, A and B at numbers of levels k and r respectively, then there are
kr cells each of which is defined by one level of A and one level of B. For
example, the data presented in Section 1.6 are arranged according to the
levels of two factors, treatments and irrigation at levels 2 and 3 respectively.
There are 6 cells each having one observation.

Let there be njj observations in the (/, y')th cell defined by the zth level
of A and jth level of B. Let yuk denote the ftth observation in the (z, y)th
cell. Then the data

(*=1,2, .. .,nu \

j 1, 2,... ,r I
i— 1, 2,... ,k J

arranged in the rk groups are called two-way classified data.

Similarly, in-general, m-way classified data are defined using levels of

m factors simultaneously.

1.7.2 Analysis of One-Way Classified Data

Let yu denote the jth observation in the zth level of a factor, say, A and
Y{j denote the corresponding random variate. We make the assumption
that Yij=y.+tl+elj where [x represents the general mean which is fixed and
stands for general condition of the experimental units and treatments, U
denotes the effect of the zth level of the factor (z=l, 2,... ,k). It can be
both random and fixed depending on how it has been chosen. For example,
if U denotes the effect of a crop variety which has been chosen at random
at the zth draw from a large number of varieties, its effect is a random
variable. If, again, U denotes the effect of one treatment in a given
complete set of varieties, it is a fixed effect. When ti s are fixed the model
is called fixed eflect model and the variation due to the treatments,
tt (/= 1, 2,.. .,k) is said to be controlled. We shall discuss here the fixed
effect model.

The last component in the model, eu is a random variable and is called
the error component. It makes Yi} a random variable. The variation in
it is due to all the uncontrolled causes which can influence the observation.
It has a hypothetical distribution, because there are a large number of
uncontrolled factors which contribute to the realization of a particular yu.
Actually, an indefinite number of possibilities of any particular ei} arises
from an infinite number of possible combinations of the many levels of an
unspecified number of uncontrolled factors which influence y{J. The one
that is realized is the outcome of the particular combination of these

20

DESIGN AND ANALYSIS OF EXPERIMENTS

uncontrolled factors which happen to occur on the experimental unit

of yij.

For example, if yu denotes the yield of the z'th variety of a crop in an
agricultural experiment grown on an experimental plot, then variety is the
controlled factor and factors like presence of moisture in the plot, its
fertility status in respect of contents of soil nitrogen, phosphorus, etc.,
quality of seeds sown on the plot, level of management, etc. are some of
the uncontrolled factors. What particular combination of the possible
levels of these uncontrolled factors was actually present on the plot of yu
was determined by chance. Hence, etj is chance determined and is consi¬
dered to be a random variable with an infinite distribution. Normally, it
is assumed to be a random variable with zero mean and a constant
variance, a2.

Taking eu as a random variable with zero mean and y. and U as

constants, we have E(Yij)=[i.+ti.

Hence, ja and t{ (z'=l, 2,... ,k) can be estimated by the least squares

method, that is, by minimizing the sum of squares

£=z (yu-it-uy

U

with respect to the k-\-1 constants.

Taking that there are zz< observations in the z'th level of the factor of
classification (z=1, 2,... ,k), we get the following normal equations obtained
by partially differentiating E with respect to each of [a and ti and then
equating such differentials to zero:

ni U=G where ]T m—n• and (?= £ yu (1.2)

i i ij

ni £+»* ~ti=Ti where 7i=£ yu (i=l, 2 ,...,k) (1.3)

j

There are k+1 equations with k+1 unknowns. But since the sum of the
k equations in (1.3) is equal to the equation in (1.2) only £—1 of the
equations in (1.3) are independent. _ By making the assumption that
2 ni ti= 0, we get unique solutions of ^ and all if s. That is, yi=G/n and
ii=Ttlnt—Gjn-{i— 1, 2,.. .,k). The implication of the assumption 2i/ = 0,
is that the treatment effects are estimated only as deviates from their
weighted means. This also shows that contrasts alone among the treatment
effects are estimable, since only contrasts are linear functions of such
deviates.

Once the least squares estimates are _available we obtain E, the error
sum of squares from £ eu2— ]T (yu—ti)2 after substituting the estimated

a u

ja and tf s in it.

Thus,

£=X (yij—^—uY

v

CONCEPTS OF experiments: design and analysis

21

= £ yu (yu- (a- t,)-ii x (yu -v.—td—'E Uj (ytj-p-u)

il

IJ

= Eyiji — [J-G— E UTi, the other terms

u i

vanish by normal
equations

»•/ V , m n )

(1.4)

G2
The first part of (1.4), viz. -is called corrected total sum of

squares.

u n'

For obtaining a measure of variation due to the treatments, we make
the hypothesis that all the treatments have equal effects. The model on
this hypothesis becomes

Yij — {a -f etj

Proceeding as before we get the error s.s., Ex on the hypothesis of equal

treatment effects as EX = E. yu2-• It actually contains the variation

G2

due to both treatments and errors. Hence, we get a measure of treatment
variation from

a n-

Ti2 G2
Ei — E= Y — -
, ^ n-

(1.5)

The expression at (1.5) is usually called corrected treatment sum of squares

2?

while E — is called uncorrected treatment sum of squares and G2/n • is

called correction term.

Degree of Freedom (d.f). We have earlier introduced the concept of
degrees of freedom of a sum of squares as the number of orthogonal
contrasts on which it is based. But it can be viewed differently as the
number of independent error components in a sum of squares. It will be
remembered that we got the error s.s., E subject to k independent
restrictions on the yij>s imposed by the k independent normal equations.
Hence, E can be considered to be based on n—k free observations, the other
k observations being fixed so as to satisfy the normal equations, when the
n—k observations have occurred in any way. E is, therefore, said to have
(n—k) degrees of freedom. It is distributed as a2x2 when each individual eu
is normally and independently distributed with zero mean and variance, a2.
Similarly, it follows that is, has got (n—1) d.f. Hence, the treatment s.s.
has got the d.f. of E-^—E, that is,(n—1)—(n—k)=k — 1. On the hypothesis
of equal treatment effects, the treatment m.s., that is, treatment s.s. divided
by its d.f. estimates the same variance as the error m.s. does. The hypo¬
thesis of equal treatment effects can now be tested by F-test where F is the
ratio of the treatment m.s. to the error m.s. If the hypothesis is tenable,
the value of F as calculated should compare well with the corresponding

22

DESIGN AND ANALYSIS OF EXPERIMENTS

(that is with the same d.f. as the two m.s.) table value of F. If the
calculated value of F is larger than the tabulated value, the hypothesis is
not tenable and is rejected. The table values of F are available at 1, 5 and
10 per cent levels of significance.

If the F-test rejects the hypothesis, it is necessary to find an index for
comparing the effects two by two to have a better picture about their
distribution. That is, given two effects, the problem is to know if they
differ significantly. It is also necessary to have a measure of the precision
of their estimates. For a measure of precision first the variance of the
estimates of individual effects is obtained from

where a2 is the error variance and is estimated by s2, the error m.s., that is,

V(u)=s2lni

The square root of this variance is called standard error of /, denoted by
S.E. (ti) and it has the same unit as that of the estimate. Thus,

S.E. (/7)=V^M-

The larger the S.E. the less is the precision of the estimate. While
presenting the results it is desirable that the estimates of the effects are
presented along with their standard errors. It has been seen that the
estimate of /<’s are obtained by solving the normal equations under the
restriction that £/i=0. However, to give physical meaning to such

estimates, it is desirable to add to each such estimate the estimated value

i

Of [i.

In order to know if the difference between the estimates of two effects

is significant we calculate

and can apply the /-test to test the significance of the difference. The
d.f. of / is the same as that of s2. If the table value of / at a given level
of significance is /„, then CD (ij)—t0\/s2 {l/nt + l/rij) gives an index such
that if a difference between two effects // and tj estimated with m and nj
observations, using the above method, is greater than CD (ij) then the
treatments differ significantly, otherwise not. If all the effects are estimated
with the same number of observations, say, n, then CD{ij)=y/2s2jn and is
independent of the pair of effects chosen. In this case the index is called
critical difference and is denoted by CD. If the difference between any
two effects is greater then CD then the effects differ significantly. Using
CD a bar diagram can be drawn which shows all effects which do not
differ among them significantly under one bar.

CONCEPTS OF experiments: design and analysis

23

When F-test reveals that the hypothesis can not be rejected, no bar
diagram is necessary. Other types of procedures for such testing the signifi¬
cance of the difference between pairs of effects are, among others, Student
Newman-Keuls range test, multiple range test by Duncan(1955), and S' and
T method by Scheffe (1953). We shall discuss here only the first two of the
above procedures. For a detailed discussion on these procedures and
their relative merits and demerits the reader is referred to Federer (1955).
Though we shall discuss these procedures for comparing means in two-
way classified data, they can be applied in other similar situations without
any complexity.

Let the observed estimates yx, y2,..., yk which are the means in the
present case be arranged from the highest to the smallest as Xk, Xk-i.. .xx,
where xk denotes the highest among yx, y2,..., yk and xt is the ith largest
among yx, y2.. .yk, i=( 1, 2.. .k). The quantity Xk—xx is called the range
of the set of means and

__(xk—Xi)\/n

4k p ~

where nx—n2.. ,np=n (by assumption) and p is the d.f. of error m.s. (s2)
is called the Studentized range of the observed means yx, y2.. .yk- Let
qa,k,p denote the upper a per cent point of the Studentized range. The
values of q<x,k,P for different values of a, k and p are available in statistical
table in Federer (1955).

Student-Newman-Keuls test: We compute the upper a per cent point

of Studentized Critical Range Wk given by

Next, we compare the observed range Xk—xx with Wk- If it is less than
Wk, the process of comparison stops and we conclude that the means are
all of the same order. If Xk—xx is greater than Wk, we devide Xk,. .., xx
into two subgroups, one containing Xk,..., x2 and the other from Xk-i to
xx. Next, each of the ranges in the two subgroups viz Xk—X2 and
Xk-1—JCj, is compared with Wk-j. If either range does not exceed, Wk-i,
then the means in each of the groups are equal. If either or both ranges
exceeds Wk-u then the k^-\ means in the group concerned are divided
into two groups of k—2 means each and the ranges for these subgroups
are compared with Wk-2- This procedure is continued until a group of
i means is found whose range does not exceed W/. In other words, by
this method the difference between any two means is significant when the
range of the observed means of each and every sub-group containing the
two means under test is significant according to Studentized Critical

Range.

Duncan’s multiple range test: This test procedure is essentially the same
as the previous procedure except the observed ranges are compared here

24

DESIGN AND ANALYSIS OF EXPERIMENTS

with Duncan’s a per cent critical range Dk ~qakp J$n  where q^kp denotes

the upper a per cent point of the Studentized range based on Duncan’s
range table.

The results obtained from the analysis of one-way classified data are
presented in form of an analysis of variance table as shown below. This
method has also been illustrated by analysis of a set of actual data. The
estimates, SE's and CD’s and other calculations have also been presented
there.

TABLE 1.3

Analysis of Variance Table for One-Way Classification

Sources of
variation

d.f.

s.s.

s.s.
m-s-=dT

F

Between levels of
the factors

Within levels of the
factors (Error)

k-1

v r<2 g2
tii~ n

St2

St2 is2

n—k

By subtraction

.S2

Total

n-1

X- 2 G2
2- yu2-~

1.7.3 An Illustration of the Analysis of One-Way

Classified Data

The method of analysis of one-way classified data has been illustrated
below by analysing data collected from an economic poultry feeding study
conducted in a poultry farm in U.P. in India for investigating the effect
of feeding cockerels with locally available food stuff's on their growth.
The feeds tried were: (i) usual feed (control); (ii) rice bran; (iii) kodon;

Data on Increased Body Weight of each Set (oz) Classified According to Feeds

TABLE 1.4

Feeds

Control

Rice bran

Kodon

Sawan

Meat meal

28.0

24.7
22.7

30.5,
28.7,

30.7,
22.5,

28.7,
26.7,

24.8

30.7
34.7

24.8,
33.5,

24.7,
22.8,

30.8,
25.0,

27.8

30.5

24.8

22.5

28.7

26.7

34.8

28.7

30.8

28.7

30.7,
24.0

24.8,
21.7,

22.7,
31.0,

22.7,

37.7,

28.5,

28.7

30.7,
28.7,

27.8,
25.0

20.7,
38.7

23.8,

30.8,

30.5,

18.7,

24.7,

CONCEPTS OF experiments: design and analysis

25

(iv) sawan; and (v) meat meal. The cockerels under study were allotted
to the feeds at random and the increase in their body weight over a period
of 10 weeks was recorded. The data of increase in body weight in oz of
individual birds are shown in Table 1.4 separately for the different
treatments.

Denoting the totals of the observations of the different feed treatments

by T0, Tj, T2, T3 and T4 in the same order as above, we have

7’0=199.7(7)

7\=249.9 (9)

J3=287.8(10)

r8=327.3(12)

7>=284.9(11)

The figures in bracket indicate the numbers of observations («,) in the

different totals so that

Uncorrected total s.s.=]T j</=38056.8800

n=X 49

Correction term — = 37171.8400

n

Corrected total s.s. = Xi yu2~^-=885.0400

Uncorrected s.s. due to feeds: V —=37224.9472

ni

Correction term — = 37171.8400

n

Corrected s.s. due to feeds V ———=53.1072

^ ru n

Within feed s.s. (Error s.s.)=Total s.s.—Bet. feed s.s.=831.9328

TABLE 1.5

Analysis of Variance Table of One-Way Classified Data

Sources

d.f.

s.s.

m.s.

F

Feeds

Within feeds (Error)

Total

4

44

48

53.1072

831.9328

885.0400

13.28

18.91

Z.1

26

DESIGN AND ANALYSIS OF EXPERIMENTS

As the variance ratio is less than unity, the variability among the feed
effects is not even as much as can be expected due to chance causes,
that is, the error variance. This fact is expressed by saying that the feed
effects are not significantly different.

The mean effects of the feeds along with their standard errors

are presented below:

Feeds Control Rice bran Kodon Sawan Meat meal

Means (oz) ’28.53 27.77 28.78 27.27 25.90

Standard Error (S.E.) 1.64 1.45 1.36 1.25 1.31

Though F is not significant, we have calculated CD (ij) for the sake of

illustration.

CD (3, 4)=1.96 X J18.9075 (L+L \=6. 45

Since n3 and n4 are the two largest numbers of observation, hence CD
(3, 4) is the least. The maximum difference between the means is 2.88.
Hence, no pair shows significant difference and thus all the means can be
considered to be under one bar.

Since the nfs are not equal, the Multiple Range test procedures could

not be applied here.

1.8 Two-Way Classified Data

We have already defined two-way classified data. The analysis of such
data has been described below in a general way.

Let the two factors of classification be denoted by A and B at p and q
levels respectively. Let denote the number of observations in the
0",y)th cell. Denoting the ftth observation in the (i,j)th cell by ytjk
(&—1, 2,..., riij) we make the following substitutions:

(/ 1> 2,..., q)
(i=l, 2,..., p)

(i) X yt]k=Tij, the cell total

k

00 X Tu=Ai, marginal total corresponding to the ith level of A.

J

(iii) X Tij=Bj, marginal total of B.

i

(iv) X ^/=X Bj=G, grand total

1 j

(v) X nij=nt., XI nij — n.j and X »/• = X n.j=n..

J i j

Orthogonal data: The concept of orthogonality of data is associated
with two or higher way classified data. It is defined as below:

CONCEPTS OF experiments: design and analysis

27

Let

and

(i'=l» 2,..p)

nt.

h-ffr U=l,2.q)

denote the marginal means of the factors A and B respectively in a two-
way classified table of data. If any contrast Y 1/7) of the marginal means

i

of A is orthogonal to any contrast Y mjbj of the other marginal means,
j
then the data are called orthogonal; otherwise, they are non-orthogonal.

The definition extends immediately to higher order classification, if we
treat the marginal means of every pairs of factors of classification as above. .
If each cell has a constant number of observations, say, n, then the

data are orthogonal as shown below.

We have Y hU——-=—U (Ti/+772+.. .-\-Ttr)

i rn rn t

Similarly Y mjbj=^Y mJ (TiJ+T2j+... + Tkj).

j J

The sum of products of the coefficients of identical observations in the two
contrasts is

1
krn2

Y l mjn-
tj

l
krn  YU Y mJ=°
i J

So, the data are orthogonal.

When the cell frequencies are proportional, that is,

ni}: nt/ =cj: c/ (j, j' = 1, 2.r)

0'=1, 2,...,p)

then also the data are orthogonal.

These results are true for any higher order classification as well if the

number of observations in the ultimate cell is constant.

Analysis of variance of such two-way orthogonal data has been

discussed below.

1.8.1 Analysis of Two-Way Orthogonal Data

The model appropriate for this type of data is

ytjk=[L+at+bj+cu+eijk
where (i) yuk is the kth of the n observations in the (/', j)th cell of the data
classified according to p levels of one factor A and q levels of the other

factor B,

(ii) at is the fixed effect of the ith level of A (/=1, 2,...,/>)
(iii) bj is the fixed effect of the ;th level of B (7=1, 2,..., q)
(iv) c,j is the interaction effect of the two factors which may arise due

28

DESIGN AND ANALYSIS OF EXPERIMENTS

to the simultaneous occurrence of the z'th level of A and y'th level
B and is in addition to the effects at and bj

(v) eijk s are the error effects which are assumed to be normally and
independently distributed with zero mean and a common variance,
9
a-.

Here, E=2 e,jk2=2 (yt ik—fx— at—bj—c,-,)2
ijk Ijk

and the normal equations

bE
tt =—2 H (,yijk-y.-ai-bJ-cij)=0

dE
8ai

ilk

-2 Z (yijk P- ai bj Q;)=0 (i = l, 2

ik

8E
jrr — 2 Z (yiJk—[k—at—bj—cn)=0 (j— 1, 2,...,q)
CD) ik

dE

2£ (y.«-(x-«/-*,-c„)=0 f

ddj k

k \ J A> • • • ? H )

When simplified they reduce to

npqy.+nq Z Oi+np Z bj + n Z «j=G

i J U

nqyL+nqcti+n Z *;+ Z CU—Ai (* = 1, 2-- p)

J J

np^+npbj+n Z «» + Z cn=Bj {j=\, 2,...,q)

i I

nyL+nai+nbj+ncu=Tij (2’"',P)

(1.6)

(1.7)

(1.8)

(1.9)

Here, G, Ai, Bj, Ttj are as defined earlier. These equations are not all
independent. The p equations at (1.7) when added give equation (1.6).
Similarly, the q equations at (1.8) when added also give (1.6). The
equations at 1.9 give the equation at 1.7 when added over j and those
at (1.8) when added over i. In order to get unique solutions of the effects,
we impose the restrictions that

2 fl/=0, 2bj=0,2 cij=2cij=0
i i i I

The implications of the first two of these restrictions are that effects are
estimated as deviates from their means; ct/s for a given i are estimated
as deviates from the effect of the ith level of A and so on. Under these
restrictions we get

[i,—G/npq

at=(Ai/nq)—G/npq

f>J—{B)lnp)—Gjnpq
Tij * £ y\

CONCEPTS OF experiments: design and analysis

29

Now, we have E=2 (yi]k—y-—ai—bj—ctj)2

= Z at-bj—aj) (ytj-n-at-bj-Cij)

tjk

—Y yu2—^ Y yvk-Y yuk -ai—Yyukbj—X! yukcu

Ijk ijk ijk ijk ijk
-t-terms which are zero by virtue of the normal equations.

Substituting the estimates in E we get

E= Y yijk2- — -Y aJi-Y bjBj- \ cijTij

G2

ijk i j ij

= Z yuk2-—- £ Si^,- Z M;

i J
i--2 A. A \

Z Z bjBj — ^G )
i J '

-(z^
vfr »

(1.10)

npq

npq—pq d.f.

with
It is seen that the error s.s. £ has come out as within cell s.s, so that
variations due to the other causes are contained in the between-cell sum
of squares. In order to estimate these variations, we shall treat the cell
totals Ti/s as the observations and the model becomes

Tn=nii-\-nai-\-nbi-\-nci)-}-Z euk

k

That is, —=v.+at+bj+Cij+Eij where Eij=~Y eW

T • 1

n n kj

In the model ctj and E,j get mixed up and the error s.s. in this model
includes the interaction s.s. In this model the error s.s., say, E' comes
out as

=z Tn2 G2

npq

n

Y a‘Ai — Z bjBj

This s.s. is the interaction s.s. with (p—1) (q— 1) d.f. Making the
hypothesis that Cj=0, (i=l,2,...,/>) we get

B,'=Z

= V

Tu2
n

[iG— Y bjBj where p. is

npq

We now get the s.s. due to A from the difference

with

(p-l) d.f.

°a
nq npq

30

DBSIGN AND ANALYSIS OF EXPERIMENTS

Similarly, the s.s. due to B can be obtained as

The analysis of variance table can now be written as below:

^pn npq

TABLE 1.6

Analysis or Variance Table of Two-Way Classified Data
with n Observations per Cell

Source

d.f.

s.s.

m.s.

F

Due to A

P-1

Due to B

q-1

2 A(* G2
nq npq

2 Bf2 G2

pq npq

V

Sa2ISab2

So8

sb2isab2

Int. AB

(P—1) (?-l)

/S7V,2 E AS S G2 ^
\ n nq pq Vnpqj

Sab2

sabw

Error

pq (n—1)

V

Total

npq— 1

s ywc%

For such data first the interaction m. s. is tested against the error m. s.
If the test shows that interaction variation is not significant, the error s. s.
and the interaction s. s. are added and then divided by their total d. f. to
get the pooled m, s. which is then used to test the significance of the
variation due to A and B. If interaction s.s. comes out significant, then
the interaction m. s. alone is used to test the significance of the variations
of A and B.

The rest of the details regarding presentation of the results is the same
as discussed in the case of one-way classified data. When there is only
one observation per cell, the within cell s. s. is not available and in such
cases the interaction s. s. is used as error. If it is known in advance that
there is no interaction, the results can be derived on similar lines. Actually,
in such cases the error s. s. becomes the sum of the interaction s. s. and
the error s. s. as obtained from the model with interaction. In other
words, the error s. s. under this model is given by

Error s. s. = Total s. s. — s. s. due to A — s. s. due to B
where the total s. s. and the s. s. due to A and B are the same as obtained
earlier.

The method of analysis has been illustrated in the next section by

analyzing an actual set of data.

CONCEPTS OF experiments: design and analysis

31

1.8.2. Example

The data presented below are the wool yield in (oz) of individual clips of
24 ewes belonging to three crops (generation) of progenies of farm bred
stock maintained in a sheep breeding research station in Rajasthan,
India. For each ewe clip yield was recorded for 6 clips at intervals
of 6 months. There were 8 animals in each crop.

Clip Nos.

First crop

progeny

Second crop

progeny

Third crop

progeny

TABLE 1.7

Data of Clip Yield (in oz per Clip)

1

16

15

16

19

16

17

18

14

2

12

18
12
12
26

18

24

16

3

12
32

23
20
16
22
20
22

4

38

24

30

32
22
25

30
26

5

24

23

24

30

32

28
20
20

6

18

18

19

15
20
18

24

17

131

138

167

227

201

149

22
20
16

15

19

17

16

19

28

26
20

24

30
20
23
20

26

24

24
20
28

24

30

28

38

30

36

26

38

36

30

30

30

32

29

40
22
22
20
24

22
20
24
22
20
26

18
22

144

191

204

264

219

174

15

14

16

17

18
20
15

16

16

16

26

30
20
18

15

27

22
27

25

19
20
21
45

38

25

27

35

35

39

40

39

28

24

19

24
21
18

26

27

24

30

24

26

16

18
20
16

28

131

168

217

268

183

178

32

DESIGN AND ANALYSIS OF EXPERIMENTS

Table of Cell Totals (Each Total Based on 8 Observations)

TABLE 1.8

Clip Nos.

Total

Crops

1

1

2

3

131

144

131

2

138

191

168

3

4

167

204

217

227

264

268

5

201

219

183

6

149

174

178

1013(48)  21.10

1196

1145

24.91

23.85

Total

406

497

588

759

603

501

3354

(144)

16.91

20.70

24.50 31.62

25.12

20.81

s. s. due to cells  = 81807.75-78120.25 i = 3687.50
s. s. due to clips = 81178.33-78120.25  = 3058.08
s. s. due to generation = = 78491.8750- 78120.25=371.6250
Interaction S. S.  = 3687.50-3058.08- 371.6250=257.80
Total S. S. = 84782.00 -78120.25=6661.75

TABLE 1.9

Analysis of Variance Table

Sources

d. f.

s. s.

m. s.

F

Clips

Generations

Interaction

Error

5

2

10

126

3058.08

371.62

257.80

2974.25

Total

143

6661.75

611.62

185.81

25.78

23-61

Pooled=

24.43

24

7

**

**

Clips

Means  : 16.91

20.70

24.50

31.62

25.12

20.81

)
Z
<

M

I
I

A
—

t

A
©
—

t

Generation

Means

21.10

24.91

23.85

S. E. = = 0.07

♦•indicates significant at 1 per cent level of significance.

CONCEPTS OF experiments: design and analysis

33

Application of multiple range test: The Student—Newman—Keuls test
is applied below to test the significance of the differences between the clip
averages obtained in the above example.

The following are the six clip averages written in ascending order of

magnitudes:

16.91, 20.70, 20.81, 24.50, 25.12, 31.62

Here, k= 6; p= 10; s2=25.78 and n=24.
The values of qa,k,P for a=5, p—10 and the values of k from 2 to 6 as
taken from the Studentized Range table are shown below together with
the values of Wk-

k

2

3

4

5

6

q<xkP

Wk=qakp

3.15

3.88

4.33

4.65

4.91

3.26

4.02

4.48

4.82

5.09

As the range Xk—Xj for k=6 is 14.71 and the value of Wk for k=6 is
5.09, the 6 averages are different. Accordingly, they are broken into the
following two groups:

16.91, 20.70, 20.81, 24.50, 25.12

20.70, 20.81, 24.50, 25.12, 31.61

As W5=4.S2 is less than the ranges in the above two groups viz.
8.21 and 10.91, the averages in each of the groups are different. These
are subdivided again into the following three distinct groups each of

size 4:

16.91 20.70 20.81 24.50

20.70 20.81 24.50 25.12

20.81 24.50 25.12 31.61

As Wt is 4.48 while the ranges in the above groups are 7.59, 4.42 and
10.80 respectively, the range for the second group only is less than Wt.
The averages in this group, thus, do not differ among themselves.

The averages in the other two groups are therefore divided into the

following two distinct groups each of three:

16.31 20.70 20.81

24.50 25.12 31.61

34

DESIGN AND ANALYSIS OF EXPERIMENTS

As Wa=4.02 and the ranges for the above two groups are 3 90 and
7.11 the range for the first group is less than 4.02 and so the average in
this group are of the same order while those in the other are different.
Proceeding similarly it is seen that the last two averages viz. 25.12 and
31.62 are significantly different. The final position is summed up below
by putting the averages which do not differ under the same bar

16.91, 20.70, 20.81 24.50, 25.12, 31.62

The average 16.91 is significantly lower than each of 24.50, 25.12 and 31.63,

is significantly higher than each of all the other averages.

1.8.3 Analysis of Three-Way Classified Orthogonal Data

The analysis of three-way classified orthogonal data follows immediately
from the analysis of two-way classified orthogonal data. Let A, B and C
be three factors according to the levels of which the data are classified.
The classification takes the form shown below when three levels of A and B
each and two levels for C are taken.

Form of Three-way Classified Data (The figures in the cells indicate the number

of observations in the cells.)

TABLE 1.10

Levels of A

<*i

a2

Cl
(1)

n

n

n

c2
(2)

n

n

n

Levels of C

Cl c2
(3) (4)

n

n

n

n

n

n

ci
(5)

n

n

n

c2
(6)

n

n

it

Levels of B

bi

b*

ba

From the three-way ABC table, we can form 3 two-way tables, that is,
AB table, AC table and BC table. The AB table is formed by putting
together all the observations under c1 and c2 occurring with each combi¬
nation (aftj). The BC table is obtained similarly by putting together all
the observations under the three levels of A occurring with each combi¬
nation (bicj), that is, by putting together the observations in columns 1, 3
and 5 and writing them in the same row on which they occur, we get the
observations in the cells bxcv bic1 and b3cx. Similarly, by putting together
the observations in the columns 2, 4 and 6, we get the observations in the
remaining cells of the BC table, that is, bxc2, b2c2 and bzc2. Similarly, by

CONCEPTS OF experiments: design and analysis

35

putting together the observations under the levels of B we get the AC
table. This table will actually come out as shown in Table 1.11.

Two-Way AC Table Formed from the ABC Table Showing the Cell Frequencies

TABLE 1.11

a2

a3

Cl

3 n

c2

3 n

Cl

3 n

c2

3 n

Cl

3 n

c2

3 n

To get the usual form of the table, it can be written after rearranging the
cells as shown in Table 1.12.

TABLE 1.12

-

Levels of A

Levels of C

Cl

c2

«i

3 n

‘in

o2

3 n

in

«s

in

in

Next, each of these tables can be analyzed as discussed for two-way data.
From these analyses we get the s.s. due to A, B, AB, C, AC, and BC. For
three-way data there is one more component called three-factor interaction
denoted by ABC. To get the s.s. due to ABC, first the s.s. due to the
cell totals of the three-way table is obtained from

Z Ti jk2/n — G2I npqr

where Ttjk is the total of the cell defined by the ith level of A, jib. level of
B and fcth level of C and p, q and r are the number of levels of A, B and
C respectively. Next, by subtracting from the between cell s.s. all the s.s.
due to A, B etc., we get the s.s. due to ABC with

(p-l) (q-1) (r-1) d.f.

This technique can be extended in a straight forward manner to m-way

classified data.

1.8.4 Analysis of Non-Orthogonal Two-Way Data

We take the following model:

yak=i>-+ai+bj-\-eijk

36

DESIGN AND ANALYSIS OF EXPERIMENTS

\

where yak is the random variable corresponding to the observation Yak;
fji, at, bj (i—1, 2,...,k, j—l, 2,..., r) are fixed effects and have similar
meaning as discussed while analyzing one-way classified data; eak is the
error component and arises in experimental data as indicated earlier. eakS
are normally and independently distributed with zero mean and constant
variance, a2. We assume that the levels of A represents the different
columns in the two-way table and those of B, the different rows. The
normal equations for obtaining the least-squares estimates of the effects are

n.y.+ Y.ni-ai+'2-.n-j*>j = G

i j

ni .y.A-ni .diJr'2lnijbj=Ai (i=l, 2.k)

j

n.]V-+n.jbj+'£.nijd,=Bj (j= 1, 2,.. .r)

i

(1.11)

(1.12)

(1.13)

Obtaining bj from 1.13 and putting it in 1.12 we get

ni. (x+nt. di+X niA ~ — n — —- £ nmjdm }=At

j \” • j m J

(1.14)

This reduces to

(a,-

Substituting

j n’J J V j n-j J mj*i \ j n-J /

(1.15)

Qi for ( At

v r n'j J

C„ forn,.-Z—!
j nJ

and

Cim evidently Cim=Cmt,

n.j

the normal equations (1.15) are written as

Ciidi~\- ^ Clmdm — Qi (/—1,2,... k)

m^i

(1.16)

These equations are called reduced normal equations. Qt is called the
adjusted total of the ith level of A. The k equations at (1.16) are not
independent, because when these equations are -added both the left hand
and right hand sides vanish. That is, Qi=0 and ]TC,m=0. These can

be proved easily by writing down their actual expressions and adding.

As C)m=Cmi, it also follows that the sum of the coefficients of afs in
each equation at 1.16 is zero. Obviously then, if, dt (/=1,2,.. .k) is a set
of solutions of 1.16, then u,-+0 (/—1,2,...k) where 6 is a constant, is also
a set of solutions.

The equations at (1.16) have thus no unique solutions. To get unique
solutions we impose the restriction 2a,=0. This implies that afs are

CONCEPTS of experiments: design and analysis

37

estimated as deviates from their means. As a matter of fact the restriction
need not be 2d/ = 0 always. It can be any linear function of a/’s other
than their contrasts. Such restrictions change 0 only.

When a set of solutions of (1.16) is obtained, we can get the solutions

of b/s from (1.13) if so required. The error s.s.,

ijk

ijk i j

— yyuk2—ij.G— y Hi At y Bj( —Tj,-L ^nmjdm\
ijk I j \n-J n.jm )

ijk I n'J I

Instead of eliminating bj to get the reduced normal equations in a/’s, we
could have eliminated a/’s and got the reduced normal equations in fc/S
and finally the error s.s. as function of b/s. In this situation

uk i n‘- j

0-1&)

where Rj is the adjusted total of the y'th level of B and is given by

R,=v,-Y.n~ ,
i Hi- *

As 1.17 and 1.18 are both the same error s.s., we have

, j n J r

E—’-Z—*jrj 0-19)

Next, for getting the s.s. of A we make the hypothesis ax=a2=... =a*=0

and get the reduced model yuk=y-{-bj+etjk.

The error s.s. on this model is

-L-.
ijk J

So, the s.s. of A—E1—E=Y. <*iQi-

i

It is called the adjusted s.s. of A while "EAZ/ni.—G2lrt.. is called its unad¬
justed s.s. It will be seen that, once the adjusted 5.5. of A is got, the s.s. due
to B can be obtained from 1.19.

We, now, get following Table 1.13 of analysis of variance.

38

DESIGN AND ANALYSIS OF EXPERIMENTS

TABLE 1.13

Analysis of Variance of Non-Orthogonal Data

Sources of variation

d.f.

s.s.
ss’ =dZ

Variance Ratio
(.E)

A (adj)

k-1

B (unadj)

r—1

2 aiQ{
i

2 QI
J n.j

Error

Total

n. ,—k—r+1

by subtraction

n..— 1

^ yak1
ijk

When interaction is present, the model is

yijk—t1+#/+b) -f hi)+eijk

The normal equations for hi/s are

Now, the error s.s.,

Tij—nij (/i-\-di-\-bjJrhjj)

/i 1,2,..., k\
\J—1» 2,..., r)

^2=11 {yuk (yijk —fi—di—bj—Hij)

Ijk

T-. 2
= £ yjk2-^ ^
ijk ij n‘J

On the hypothesis that hi/s are zero, we have already got the error s.s.,

Hence, the interaction s.s.

k J nJ i

=e-e2=z ~—~y. ———x: diQ,.

T• 2 B -2

n ntJ j n.j ,

Its d.f. is (r— \)(k— 1), if there is at least one observation in each cell;
otherwise, it is reduced by the number of cells having no observation.

1.8.5 Estimate of Treatment Contrast and its Variance

Let 2 hat be a treatment contrast. We know that the estimate of a< is a

linear function of Qi s. Hence 2 is estimated by another linear function

of Qi. Let 2 hat = 2 qiQj.

i i

If J/’s are available as linear functions of Q/s, q/s can be obtained

easily. However, q/s can be obtained as below also.

CONCEPTS OF EXPERIMENTS: DESIGN AND ANALYSIS

39

Substituting for Qi in X QiQi from (1*16)

i

we get V //dj=X qi(Cna1+Ci2ai+..\-Cik5k)

Equating coefficients of at in this identity we get

i i

li=Y.qmCmi(i^l,2,...,k) (1.20)

m

These equations are the same as the normal equations at (1.16) excepting
that Qi s are substituted by /,’s and the unknowns a?s have been written
as qi s.

Hence, qCs can be obtained from the solution of the same normal

equations.

Now, var (Qi)=V ^Ai — X =

cov (Qi, <2m)=cov |

— C/m cr2

So, var (X qiQd=<j2 (X <7*2 C»+X qtqmCim)

=ct2 (X qi X qmCim)
t m

=a2 X

/ « '

In particular, v(a,-Jm)=a2 (qt-qm) where 9/ and qm are the coefficients
of and Qm respectively in the expression giving the estimate of <5/—dm.

We have seen that the s.s. of a contrast is the square of the contrast
divided by the coefficient of a2 in its variance. Hence, the s.s. of the

estimate of X hai (X q* Qd“l X hqt-

i i ‘

1.8.6 An Illustration of the Analysis of Non-Orthogonal Data

With a view to upgrading the Indian stock in production level, an experi¬
ment was conducted at Military Dairy Farm, Meerut. In all 117 records of
first lactation milk yield (kg) from cows of different grades of exotic blood
over a period of 18 years frpm 1938 to 1955 were collected. These
records were classified to form different grades, viz., pure Sahiwal, 3/4,
7/8 and 112 exotic blood proportions. The data for each grade were divided
i«o” ur periods, viz. 1938-«, 1943-46. 1947-50 and 1950-55 The data
have been presented in the Table 1.14. Only the cell totals have been

presented together with the numbers of observations in each cell shown in
bracket. The crude total sum of squares of all the 117 observations was
obtained as 26639224. The salient steps in the analysis of the data have

been given in Table 1.14.

40

DESIGN AND ANALYSIS OF EXPERIMENTS

TABLE 1.14

Percentage of Foreign Blood

Periods

Sahiwal

3
4

7
8

1
2

Total (jB,-)

Average Bj/n.

1942 and
earlier

1943-46

1947-50

1950 and
afterwards

Totals (Ti)

Adjusted
totals (Qi)

1428
(4)

2670

(7)
10029
(26)

5621
(16)

820
(1)
3213
(5)
6000
(ID
3346
(16)

528

(1)
2523
(4)
1499

(2)
3345

(8)

1400

(2)
3769
(7)
1230

(1)
2257

(6)

4176(8)

522.00

12175(23)

529.35

18757(40)

18758.95

14569(46)

316.72

19748
(53)

13379
(33)

7895
(15)

8656
(16)

49678(117)

-3305.61

-15.67  1783.97  1537.31

Cu =53-

/ 42 , 72
V 8 +23

262
+ —+
40

-^=26.404
46 )

— Ci2 =G+ 35 , 286

23 40

256 )
46 j

|=14.737

— C13=5.802; —Cl4=5.867; -C23=4.237

— C24=4.134; — C34=2.561; C22=23.198;

C33=12.688; C44=12.562

The normal equations are

26.404 tj—14.737 fa-5.802 f3—5.867 /4= —3305.61

-14.737 /j+23.198 f2-4.327 f3-4.134 t4=-15.67

-5.802 4.327 fa+12.188 /3—2.561 f4=1783.97

—5.867 fj—4.134 F2—2.561 F3+12.562 f4=1537.31

Solutions of the equations with the restrictions 2 /,-=0 are

74= —114.84; f2=—44.51; J3=87.43; ?4=71.91

Adjusted s.s. =2 tQ=646830.76

Unadjusted treatment s.s. =527454.04

Unadjusted period s.s. =942301.66

Between cell s.s. =2651401.49

The unadjusted s.s. are all corrected.

CONCEPTS OF experiments: design and analysis

41

Interaction s.s. =2651401.49-646830.76-942301.66

= 1062259.07

Total s.s. =5546030.12

Error s.s. =5546030.12-2651401.49=894628.63.

TABLE 1.15

Analysis of Variance Table

Sources

d.f.

s.s.

m.s.

F

Periods (unadj.)

f Treatments
t(P.C. of F blood) (adj.)

Interaction

Error

Total

3

3

9

101

116

942301.66

646830.76

215610.25

1.8

1062259.07

118028.78

13**

894628.63

8857.71

5546030.12

Since interaction variation is significant, it has been used to test the
significance of treatment variation. The treatment variation does not come
out significant. This indicates that the yield does not depend on the extent
of foreign blood percentage. Comparison of the four estimates of the
treatment effects, however, shows that the last two treatments had better
yield performance.

Suppose the experimenter is interested to know how the performance of
the pure Sahiwal breed differs from the average of the crossbred animals.
We have, then, to estimate the contrast /2+f3+/4—2>tx, find its variance
and then test by the t-test.

The estimate = —44.5+87.4+71.9+114.8x3

=457.2

To obtain variance, we have to replace the left hand side of the normal
equations by —3, 1, 1, 1 in that order. The solutions for qi s come as

<7i=— .0928, <jr2= .0009, #3= .0459 and ?4=.0460.

Variance of the estimate <r2(-3(- ,0928a)+.0009+ .0459+ .0460) =.3612a2

Replacing a2 by interaction m. s.

, +45ZJL=~2.18 with 9 d.f.

V.3612X 1180.28

This value of t just falls short of significance. Therefore, there is no
evidence that the cross-breds differ significantly from the pure bred.

42

DESIGN AND ANALYSIS OF EXPERIMENTS

1.8.7 Some Types of Non-Orthogonal Data

It has been seen that the main difficulty in the analysis of non-orthogonal
data is the solution of the reduced normal equations. There are, however,
certain types of data as discussed below for which the solution problem

does not exist.

Proportionate Cell FrequenciesOne such type of data is obtained when
the cell frequencies are the same in a column (row), though it may vary
from column to column. Suppose the frequencies in each row of the ith

column be n/. Then

Cti=rnr

rnp
'~N

where JV=2 m and r is the number of rows.,

Qj

rnm„
N

The reduced normal equations become

r <5<~~N ^

. «,• „ Qi
That is, —2 nmam=-j

Taking the restriction that £ nmam=0

we get the solution as 5/= Ql
m

In,this case the adjusted s. s. due to A can be obtained from

and that of B from

y il_G?
mi rN

^ N rN

Var (di - a„) ■

a2/l_ }_\
' n \ni+nmJ

Balanced Data. For certain types of data, it is possible to have C« a
constant, say, equal to R and Ctm also another constant, say, A • In this
situation, the reduced normal equations turn out to be

with the solution

Rai+ A £ am=Qi

mj£i

ar-

Qi
R-A

The same simplicity of solution is available even if Cu is not constant but
Cim is constant. It is unlikely that in naturally occurring data the cell
frequencies will be such as renders Cim or Cu constant. But we can delibe¬
rately choose the number of observations to be obtained in different
cells defined according to the levels of two factors. Actually, one of the

CONCEPTS OF experiments: design and analysis

43

main purposes of design of experiments is to decide such cell frequencies
and their distribution in the different cells. One of the main series of
designs called incomplete block designs which will be discussed in a later
chapter has the cell frequencies 0 and 1. These are so distributed in the
different cells that C„ is constant and Cim can take one or two values. The
main purpose of such choice is again to get an easy solution of the normal
equations and constant precision of comparisons. An example of such a
distribution in which both Cu and C\j are constants is given below taking
7 different groups of size 3 as the levels of one factor B and 7 different
treatments as the levels of another factor A. Only the cell frequencies and
the corresponding normal equations have been shown.

Frequency Distribution of Observations in a Two-Way Classified Balanced Data

TABLE 1.16

Groups

1

2

3

4

5

6

7

l

l

0

0

0

1

0

1

2

1

1

0

0

0

1

0

Treatments
3 4

0

1

1

0

0

0

1

1

0

1

1

0

0

0

Hence

Til . ==3y  n.j—3,  C„=2,

Reduced normal equations are

6

0

0

1

0

1

1

0

7

0

0

0

1

0

1

1

5

0

1

0

1

1

0

0

1

r
-
4
f
i

O

u

I
I

 E

2oi~— 51 am=Qi
mj&i

z' 3 Qt
Solutions are: ai=-y-

These types of designs known as balanced incomplete block designs, lattice
designs, partially B.I.B. designs were introduced by Fisher (1953), Yates
(1936) and many other workers. Subsequently they were developed by
Bose (1939). Tocker (1952) defined another type of design where the cell
frequencies can take any number of values, but they are so distributed that
Cu and Cim are constants. He called these designs n-ary designs.

1.9 Assumptions of Analysis of Variance

We have seen that the data should satisfy certain assumptions before these
methods can be applied. One of the assumptions is that the variance of

44

DESIGN AND ANALYSIS OF EXPERIMENTS

the observations should be constant. There are certain types of data for
which this assumption does not hold. For example, if the observations
are the number of plants (r) affected by a disease among a given number
of plants 1(aj) in a plot,then the fraction (r/n) which is taken for analysis is
binomially distributed and therefore does not have a constant variance.
In such a case the observations are suitably transformed such that the
variance of the transformed observation is constant. The methodology
for obtaining appropriate transformation indifferent situations is discussed
in a subsequent chapter.

We have seen that classification of data is a way of reducing the error
variance because the variation due to a factor according to which the data
have been classified can be taken out of the error variance by the technique
of analysis of variance. There are other methods of reducing the error
variance; one such method is called analysis of covariance for which
observations on another variate called concomitant variate from each of
the experimental units are used. It is, however, necessary that there is a
linear relation connecting the variate under study (>>) and the concomitant
variate (x). By this method the portion of variability in y which is due to
the variation in x, is eliminated from the error variance. The method will
also be discussed in another chapter together with the technique of
transformation of data.

1. What comparisons do the following contrasts represent?

EXERCISES

(0 7i+72-2y3

(ii) 71+4^2-2^3-3^4

2. Write down the complete set of mutually orthogonal contrasts among

7i> y2,- ■ ,78 using only +1 and —1 as coefficients.

3. Show that the sum total of the s.s due to all the (n—1) mutually orthogonal
contrasts among n observations is equal to the s.s obtained by summing the
squares of their deviations from the mean.
Solution: Write the contrasts as

C1=2Lk7<

C2='E,Ltiyi

C„-i — 2Z.(„-i)<7<

where

2Lmi =0

CONCEPTS OF experiments: design and analysis

45

s.s, of the contrasts=Q2+ C22+.. . + C„-i2

m , r L- ^ X1+J2+. • •yn
Take one more function C0=-7=-

Vn

Then the following matrix is an orthogonal matrix:

““ L11 Ln ... Lln

L 21 ■^'22 • • •

^-(n-l)l» i(«—1)2 • • • L(n-i)n

j_ jl _i

— y/n \/n Vn

So, A'A = 1 giving

SLm/2=l and lLmiLmi'=0 (i=l, 2,...«)
m m

Omitting the last row of A we, therefore, get

71 — 1 1 71 — 1 1

m***± m*=*L

In C12+Ca2+-. • + C„-12, the coefficient of Ji2= S L2„<=1-- and that of

71-1 1

71-1 1

771-1

Therefore, C12+C22+.. . + C»-i2=^l —

SXi

/<|i

=»Ey<2-

a
(gy<)
n

4. Show that two-way classified data where the cell frequencies are proportional,

that is, mj: nij'^Cj.C., (/,/=!, 2,...r) are orthogonal.

5. In a set of two-way data classified according to k levels of factor A and r
levels of B, there is one observation in each cell. Show that the total
number of error contrasts is (r-1) (A:—1). Describe a convenient method of

writing them.

6. If one observation is absent in one cell of the data in problem 5, obtain the
reduced normal equations for the effects of A and get their algebraic
solutions. Find the variance of the contrast estimate t-tm where the cell

with no observation belongs to /,.

7 Show that the /-value for testing the significance of any contrast estimated
from non-orthogonal data is unaffected when the contrast is multiplied by a

constant.

8 in a two-way classified data, the cell frequencies are shown below. Analyze
the data completely taking the general observations as y,j. Show that the
variance of the estimates of all treatment contrasts of the type t(—tm is

constant.

46

DESIGN AND ANALYSIS OF EXPERIMENTS

Blocks

Treatments

1

2

1

0

0

0

1

0

1

1

1

0

0

0

1

0

3

0

1

1

0

0

0

1

4

5

6

7

1

0

1

1

0

0

0

0

1

0

1

1

0

0

0

0

1

0

1

1

0

0

0

0

1

0

1

1

1

2

3

4

5

6

7

9. If a set of solutions ti of the reduced normal equations is available with the
restriction 2rf=0, find the set of solutions with the restriction £/>/,■= 0 where

0.

10. If the observations in an agricultural experiment are precentages of seeds that
germinated, how can you justify that the technique of analysis of variance
developed in this chapter, cannot be applied to these data as such?

REFERENCES

1. Bose, R.C. (1939). “On construction of balanced incomplete block designs/'

Ann Eug. Lond. pp. 353.

2. Bose, R.C. and Nair, K.R. (1939). “Partially balanced incomplete block

designs.” Sankhya, 4, pp. 337.

3. Duncan, B.P. (1952). “On the properties of multiple comparison tests.”

Virginia F. Sci. N.5.3, pp. 49.

4. Duncan, B.P. (1955). “Multiple range and multiple F-tests.” Biometrics, 11,

pp. 1.

5. Federer, W.T. (1955). Experimental Design, Theory and Application—

Macmillian and Co.

6. Fisher, R.A. (1944). Statistical Methods for Research Workers, 9th Ed. Oliver

and Boyd, Edinburg.

7. Fisher, R.A. (1953). Design of Experiments. Oliver and Boyd, Edinburg.
8. Fisher, R.A. and Yates, F. (1942). Statistical Tables for use in Biological,

Agricultural and Medical Research, 2nd Ed. Oliver and Boyd, Edinburg.

9. Gnu, N. (1976). Introduction to Probability and Statistics. Part II, Marcel Dekker.

10/ Keuls, M. (1952). “The use of Studentised range in connection with an

analysis of variance.” Euphytica, I, pp. 112.

11. Kempthorne, O. (1952). The Design and Analysis of Experiments. Wiley,

New York.

12. Kendall, M.G, and Stuart, A. (1966). The Advanced Theory of Statistics,

Charles Griffin and Company, London.

13. Lehmann, E.L. Testing of Hypothesis, Wiley, New York.
14'. Newman, D. (1939). “The distribution of range in samples from a normal
population expressed in terms of an independent estimate of standard
deviation." Biometrica, 31, pp. 20.

CONCEPTS OF experiments: design and analysis

47

15. Ogawa, J. (1974). Statistical Theory of the Analysis of Experimental Designs.

Marcel Dekker.

16. Raghavarao, D. (1971). Construction and Combinatorial Problems in Design

of Experiments. Wiley, New York.

17. Scheffe, H. (1953). “Method for judging all contrasts in analysis of variance.”

Biometrica. 40, pp. 87.

18. Scheffe, H. (1959j. The Analysis of Variance. Wiley, New York.
19. Student (1908). “On the probable error of mean.” Biometrica, 6, pp. 1.
20. Tocher, K.D. (1952). “The design and analysis of block experiments”

J. Royal Stat. Soc. B, 14, pp. 45.

21. Tukey, J.W. (1949). “One degree of freedom for non-additivity”,Biometrica,

5, pp. 232.

22. Wilk, M.S. and Kempthorne, 0.(1955). “Fixed, mixed and random models.”

J. Amer. Stat. Asso. 52, pp. 218.

23. Yates, F. (1936). “Incomplete randomised blocks.” Ann. Eugen. 7, pp 721.
24. Yates, F. (1937). “The design and analysis of factorial experiments.” Imp.

Bur. Soil. Sci. Tech. Comm. No. 35.

25. “National Index of Field Experiments” (1954-59) M.P. Pub. by I.A.R.S.

New Delhi 12.

CHAPTER 2

Complete Block Designs

We have discussed in Chapter 1 the underlying principles of experimental
designs. There is a large number of designs possessing one or more of
these properties. We shall discuss in this chapter the relatively simple and
more commonly used designs. These are: (i) completely randomized
designs, (ii) randomized block designs and (iii) latin square designs. These
designs are described below one by one.

2.1 Completely Randomized Designs

Designs are usually characterized by the nature of grouping of experimental
units and the procedure of random allocation of treatments to the experi¬
mental units. In a completely randomized design the units are taken in a
single group. As far as possible the units forming the group should be
homogeneous. We shall sometimes use the word “plot” for unit.

Let there be k treatments in an experiment. Let the zth treatment be
replicated times (i= 1, 2, ..., k). The total number of experimental units

k

required for the design is thus 2 rt. The treatments are allotted at random

to these units as described in section 2.1.1.

/-i

Normally, the number of replications for different treatments should be
equal as it ensures equal precision of estimates of the treatment effects.
The actual number of replications is, however, determined by availability
of experimental resources and the requirement of precision and sensitivity
of comparisons. If the experimental material for some treatments is
available in limited quantities, the numbers of their replication are reduced.
If the estimates of certain treatment effects are required with more precision,
the numbers of their replication are increased. We shall see subsequently
that this type of flexibility in the choice of number of replications is present
only in this design.

2.1.1 Randomization

There are several methods for random allocation of treatments to the
experimental units. Some of them are discussed below.

The k treatments are first numbered in any order, from 1 to k.

COMPLETE BLOCK DESIGNS

49

k

The 2 ri=R (say) experimental units are also numbered suitably.

i-i
One of the methods uses the random number table as discussed below.
Any page of a random number table is taken. If k is a one-digit number,
then the table is consulted digit by digit. If k is a two-digit number then
two-digited random numbers are consulted. All numbers which are greater
than k along with zero are ignored.

Let the first number chosen be nlt then the treatment numbered is
allotted to the first unit. If the second number is «2, which may or may
not be equal to«j, then the treatment numbered n2 is allotted to the second
unit. This procedure is continued. When the ith treatment number has
occurred rt times, (/= 1,2,..., k) this treatment is ignored subsequently.
This process terminates when all the units are exhausted.

One drawback of the above procedure is that sometimes a very large
number of random numbers may have to be ignored because they are
greater than k. It may even happen that the random number table is
exhausted before the allocation is complete. To avoid this difficulty the
following procedure is adopted. We have described the procedure by
taking A: to be a two-digit number.

Let P be the highest two-digit number divisible by k. Then all numbers
greater than P and zero are ignored.,If a selected random number is less than
Jfc,then it is used as such. If it is greater than or equal to k, then it is divided
by k and the remainder is taken to be the random number. When a
number is completely divisible by k, then the random number is k. If k is
a n-digit number, then P is taken to be the highest /i-digit number divisible
by k. The rest of the procedure is the same as above.

2.1.2 Alternative Methods of Random Allocation

If random number tables are not available, treatments can be allotted by
drawing “lots” as below. Let the number of the /th treatment be written

k

on rt pieces of papers (/= 1, 2, ...,k). The 2 n pieces of papers are then

folded individually so that the numbers written on them are not visible.
These papers are then drawn' one by one at random. The treatment which
is drawn in the /th draw is allotted to the /th plot (/= 1, 2, ..., R).

Random allocation is also possible by using a fair coin. We illustrate

this procedure by the following example.

Let there be five treatments each to be replicated four times.
There are, therefore, 20 plots. Let these plots be numbered from 1 to
20 conveniently.

When a coin is tossed, there are two events, that is, either the head
comes up, or the tail. We denote the “head” by H and the “tail” by T.
When the coin is tossed twice, there are four events, that is, both times
head HH\ first head next tail HT\ first tail next head TH and both times

50

DESIGN AND ANALYSIS OF EXPERIMENTS

tail TT. Similarly, when the coin is thrown three times, there are the
following eight possible events:

HHH, HHT, HTH, HTT, THH, THT, TTH, TTT.

Similar events can be written easily for four or more numbers of throws
of the coin.

The five treatments are now labelled not by serial numbers as earlier
but by any five of the above eight events obtainable by tossing three coins.
Let us use the first five events and omit THT, TTH and TTT.

A coin is now thrown three times and the event noted. If the event is
any of the first five, the treatment labelled by it is allotted to the first plot.
If the event is any of the last three, it is ignored. The coin is tossed again
three times and this event is used to select a treatment for the second plot.
If the same event occurs more than once, we are not to reject it till the
number of times it has occurred equals the number of replications of the
treatment it represents. This process is continued till all the plots are
exhausted.

2.1.3 Local Control

No local control measure as such is provided in this design excepting that
the error variance can be reduced by choosing a homogeneous set of
experimental units. When the number of treatments is large, it may not
always be possible to get a large homogeneous set of units required for
the experiment. It is, therefore, not desirable to adopt completely ran¬
domized designs when the number of treatments is large or when the
experimental units are very heterogeneous.

2.1.4 Analysis

This design provides a one-way classified data according to levels of a single
factor, treatment . For its analysis the following model is taken:

., k
• ,rt  )

where Yi} is the random variable corresponding to the observation yi}
obtained from theyth replicate of the ith treatment, ^ is the general mean,
U is the fixed effect of the z'th treatment and etJ is the error compo¬
nent as described in Chapter 1. The error components are assumed
to be independently and normally distributed with 0 mean and constant
variance a2.

Let j y,j=Ti be the observation total of the ith treatment. Following

the method of analysis suggested for the one-way classified data in Chapter 1
the following sums of squares are computed first.

COMPLETE BLOCK DESIGNS

51

K T,2 G*
1. Treatment sum of squares =2]-—
<=1 ri R
k k

where G=X Tt, R=Y. ri-

1 (-1

G2
2. Total sum of squares=]T ytJ2——.

u R

The analysis of variance is given in Table 2.1.

TABLE 2.1

Analysis of Variance of Completely Randomized Design

Sources of
variation

Degrees of
freedom (d.f.)

Sum of
squares (s. s.)

Mean s.s.
square-d.f.

F

Treatments

k-1

y Ti 2 G2
,-1 "

St2

St2/S2

Error
(within treatments)

R-k

By subtraction

s2

Total

R-1

V 0 G2
2- y*>2—jr
u R

* '

The hypothesis that treatments have equal effects is tested by the F-test.
If F is not significant at the desired level of significance, the treatments
can be considered to have equal effects. If F is significant, the treatment
effects are not equal. In such cases it becomes necessary to estimate and
test individual treatment contrasts in which the experimenter may be
interested.

k

Estimate of any treatment contrast ]T hti where tt denotes the effect

of the ith treatment is obtained from

i = 1

£ liU= £ hyi
1 1

- T,
where ~ •

v Cl Uyi)=°2 X~
, f n

where a2 is the error variance which is estimated by the error mean squares,

s2 in Table 2.1.

52

DESIGN AND ANALYSIS OF EXPERIMENTS

The significance of the contrast can be tested by f-test where

I £ lm I

with (R—k) degrees of freedom.

Contrasts of the type (ti—tm) in which experimenters are often interes¬
ted are obtainable from X hU by putting U—\, lm= — l and zero for the

other /’s.

I

Presentation of Results

In addition to the analysis of variance table, the treatment means
yi (i=l, 2,..., k) are presented in a row in descending order of magnitudes.
The standard errors s2/n of these means are also presented side by side. If
the treatments have equal numbers of replications r, then only the common
standard error s2/r need be shown. In such cases the treatments can
also be compared by obtaining critical difference as discussed in Chapter 1.
Missing observations do not make the analysis of this design compli¬
cated. If an observation from a treatment is missing in one or more
replications, the actual number of replications where the treatment is not
affected is to be taken into account for the computation.

2.2 Randomized Block Designs

We have seen that in a completely randomized design no local control
measure was adopted excepting that the experimental units should be
homogeneous. Usually, when experiments require a large number of experi¬
mental units, completely randomized designs cannot ensure precision of
the estimates of treatment effects.

An improvement of the completely randomized designs can be obtained
by providing error control measures as described below. The resulting
design is called randomized block design.

Let there be k treatments. Each of the treatments is replicated the
same number of times in this design. Let r denote the number of repli¬
cations of each treatment. The total number of experimental units is,
therefore, k r. These units are arranged into r groups, each of size k.
The error control measure in this design consists of making the units in
each of these groups homogeneous. These groups are commonly known as
blocks and the experimental units in the the blocks are known as plots.

In agricultural experiments such groups are formed by neighbouring
plots of land of desired size, a set of similar trees, etc. In clinical or
similar trials where animals like rats, guinea pigs, etc. are the experimental
units, animals coming from the same litter may form such groups. In

COMPLETE BLOCK DESIGNS

53

general, such groups are formed with units having common characteristics
which are known to have influence on the variate under study.

The number of blocks in the design is the same as the number of
replications. The k treatments are allotted at random to the k plots in
each block.

This type of homogeneous grouping of the experimental units and the
random allocation of the treatments separately in each block are the two
main characteristic features of randomized block designs.

Actual number of replications in the design is determined by the
availability of resources and considerations of cost and precision. A
method of finding the number of replications from considerations of
sensitivity of comparison of the treatments has been given in Chapter 1.

2.2.1 R AN DOMIZ ATION

The treatments are first numbered from 1 to k in any order. The units in
each block are also numbered, conveniently from 1 to k. The A: treatments
are then allotted at random to the k units in each block. Random allocation
can be made either by consulting a random number table or by drawing of
lots or by coin tossing as described for completely randomized designs. If
k is not very large, not more than two digited numbers need be consulted.
A column is first chosen. If the first number in the column is k or less,
the treatment corresponding to this number is allotted to the first plot in
the first block. If it is zero or greater than ky it is omitted. Similarly, if
the next number is not greater than k and has not been chosen earlier,
the treatment corresponding to it is allotted to the second plot. All
numbers greater than k are ignored. When all the units in the first block
are allotted treatments, by following the above procedure, units in the second
and subsequent blocks are allotted treatments exactly similarly.

When all numbers greater than k are rejected, there may be too many
rejections. This difficulty can be avoided by consulting all two-digited
numbers except 00 and numbers greater than P where P is the highest
two-digit number exactly divisible by k. When a number is greater than
k but less than P, it is divided by k and the remainder gives the number
to be chosen. If the number is non-zero and exactly divisible by k, the
number chosen is k.

2.2.2 Loca l Control

The principle of local control is adopted in this design by first forming
homogeneous groups of the units and then allotting at random each
treatment once in each group. This results in an increase in precision of
estimates of the treatment contrasts, due to the fact that error variance
which is a function of comparisons within blocks, is smaller because of
homogeneous blocks. This type of allocation makes it possible to elirni-

54

DESIGN AND ANALYSIS OF EXPERIMENTS

nate from error variance a portion of variation attributable to block
differences. If, however, variation between the blocks is not significantly
large, this type of grouping of the units does not lead to any advantage;
rather some degrees of freedom of the error variance is lost without any
consequent decrease in the error variance. In such situations it is not
desirable to adopt randomized block designs in preference to completely
randomized designs.

When the number of treatments is large, say, greater than 10,
randomized block designs are not usually suitable because it is often
difficult to get homogeneous groups of units of size larger than 10. If,
however, homogeneous groups can be formed with larger number of units
in certain situations, randomized block design can still be adopted with
larger number of treatments. Plots of very small area as units in
agricultural experiments is an example on this point.

2.2.3 Analysis

The data collected from experiments with randomized block designs form
a two-way classification, that is, classified according to the levels of two
factors, viz., blocks and treatments. There are kr cells in the two-way
table with one observation in each cell. The data are orthogonal and
therefore the design is called an orthogonal design.

We take the model

where To denotes the random variable corresponding to the observation
yu from ith treatment in yth block, bj are respectively the general
mean, effect of the ith treatment and effect of the /th block as explained
in Chapter 1. These effects are fixed and e{j is the error component which
is a random variable. These are assumed to be normally and independently
distributed with zero mean and a constant variance a2. We discussed in
detail in Chapter 1 how the error component arises as a random variable.

Following the method of analysis of variance for finding sums of
squares due to blocks, treatments and error as described in Chapter 1 for
the two-way classification, the different sums of squares are obtained as
follows:

Let

and

Z yij—Ti (i=l, 2,.k)
j

— observation total of ith treatment

Z yiJ=Bj(j=l, 2,.r)
i

=observation total of yth block.

These are the marginal totals of the two-way data table.

55

COMPLETE BLOCK DESIGNS

Let further

Z Ti=E B)—G.
i s

We shall call G2/rk as correction factor denoted by C.F.
T,2

Sum of squares due to treatment = Z-C.F.

Sum of squares due to blocks

Total sum of squares

i r

= V —C.F

^ k

=Z yu—C.F.

u

TABLE 2.2

Analysis of Variance of a Randomized Block Design

Sources of
variation

Degrees of
freedom (d.f.)

Sum of
squares (s.s.)

Mean s.s.
squares (m.s.) = d.f.

F

Blocks

r—1

Treatments

k-1

z f-C.F.
i k

?—-CF-

Error

Total

(r—1) (At—1)

by subtraction

rk—1

2 W2_C.F.

St2

j2

r*

The hypothesis that the treatments have equal effects is tested by F-test
where Fis the ratio st2/sz with (fc—T) and (r — 1) (&—1) d.f. If F is not
significant the data do not suggest that the treatment effects are different.
When F is significant, we conclude that the treatment effects are different.
We may then be interested to either compare the treatments in pairs or
evaluate special contrasts depending on the objectives of the experiments.
This can be done as follows.

Let 2 Utt denote a general contrast among the treatment effects.

i

Estimate of 2 hti is given by

I

where yt=Ti/r,

Z liu— Z hyt
i t

nz hu)=7 z 42
i I

where a2 is estimated by the error mean squares s2 (in Table 2.2).

The critical difference for testing the significance of estimate of the

differences like — tm is obtained from

C.D. — fl—a/2, (r—lHk-1) J

i2s2

56

DESIGN AND ANALYSIS OF EXPERIMENTS

where (r-i) (k-d is the value of t at the level of significance a with
degrees of freedom (r—1) (A:-1). If any difference'is greater than C.D.
the corresponding two treatments effects are significantly different. Such
differences can also be tested by the multiple range test of Duncan

(Chapter 1).

These results are presented by writing the treatment means y<’s in
descending order below the analysis of variance table. The standard error
s2/r and C.D. value are also put alongside. All treatments which are not

significantly different are put under one line.

2.2.4 Missing Observations

It may happen that due to some unforeseen causes, observations from
some of the plots are missing. This happens in agricultural experiments
when crop of some experimental plots is damaged by animals, pests, etc.
In animal experiments, again, some animals may die in course of the
experiment. Sometimes, observations from one or two units are extremely
large or small in comparison with the rest of the observations. The
accuracy of such observations is often in doubt. These observations
inflate the error variance too much and thereby distort the results. They
are, therefore, better omitted and the remaining data are then analyzed

treating the omitted data as missing.

When observations from one or more units are missing, the data
become non-orthogonal. The usual analysis of variance for the randomized
block designs is no longer applicable. The data have to be analyzed either
as non-orthogonal data or by adopting the missing plot technique due to
Yates (1937). Some more techniques are also available for their analysis.
These techniques have been discussed in detail in Section 2.4 subsequently.

2.3 Latin Square Designs

It was pointed out earlier that the randomized block designs are
improvements over completely randomized designs in the sense that they
provide error control measures for the elimination of block variation.
This principle can be extended further to improve randomized block
designs by eliminating more sources of variation. Latin square design is
one such improved design with provision for the elimination of two
sources of variation. This design is discussed below.

Let there be k treatments each replicated k times so that the total

number of experimental units required is k2.

Let P and Q denote two factors whose variabilities are to be eliminated
from the experimental error by having a suitable design. Evidently, both
these factors should be related to the variate under study so that their
variability may influence the variability of the variate under study. These
two are actually the controlled factors. Each of the factors P and Q is

COMPLETE BLOCK DESIGNS

57

taken at k levels. The total number of level combinations of the two
factors is A:3. The k2 experimental units are now so chosen that each unit
possesses a different level combination of the two factors.

For example, in an animal experiment with the object of comparing the
effects of four feeds, let young calves be the experimental units with their
growth rate during a certain period as the variate under study. Let it be
intended to eliminate the variation due to breeds and ages of the calves.
So breed and age are the two factors P and Q. The calves are, therefore,
to come from four breeds and four age groups. The 16 calves required
for the experiment should each belong to a different breed-age combination.
It is, therefore, necessary that there should be four calves belonging to each
breed and each of these four calves should come from a different age
group. In agricultural field plot experiment with k treatments, the plots
are arranged in form of a k x k square so that there are k rows and k
columns of the plots. Here rows and columns are the two factors, P and
Q. Each plot belongs to different row-column combination.

Originally, latin square designs were defined for eliminating the
variation of two factors which are generally called row and column.
Though it is not necessary that the two factors should always be called
row and column, it has become customary to define latin squares by

calling the factors as row and column.

After the experimental units are obtained as specified above, the
treatments are allotted to these units in the following way. The k treatments
are allotted to the k2 units in such a manner that each treatment Occurs
only once in each level of the factor P and once in each level of the factor
Q. This requires that each treatment should be replicated k times.

If a two-way table is formed with the levels of the factors P and Q
spch that the levels of P denote the rows and the levels of Q denote the
columns, then the latin square design requires that the treatments should
be so allotted to the k2 cells of this table that each treatment occurs once
in each row and once in each column. Such an arrangement is called a

latin square of order k.

For example, suppose there are five treatments denoted by A,B,C,D, E.
Then the following arrangement of treatments in a 5 x 5 square is a latin

square design:

Levels of Q Levels of P

Pi

A

D

B

E

C

P 2

B

E

C

A

D

Pz

C

A

D

B

E

Pi

D

B

E

C

A

P 5

E

C

A

D

B

<h

?2

#3

<li

(7 5

58

DESIGN AND ANALYSIS OF EXPERIMENTS

It has been pointed out earlier that this design is effective if the two-
factors P and Q can cause variability in the variate under study. If one
of the factors does not have substantial influence on the variate under
study, elimination of its variance may not reduce the error variance. In
such a situation a latin square design is no improvement over the rando¬
mized block designs. So, unless it is known that both the factors cause
sufficient variation in the variate under study, it is better to adopt a
randomized block design. In agricultural experiments if there is soil
fertility in two mutually perpendicular directions, then the adoption of a
latin square design with rows and columns along the directions of fertility
gradients, proves useful.

2.3.1 Randomization

According to the definition of a latin square design, treatments can bo
allocated to the k2 units in a number of ways. There is, therefore, a
number of latin squares of a given order. The purpose of randomization
is to select one of these squares at random. The following is one of the
methods of random selection of latin squares.

Let a kxk latin square arrangement be first written by denoting
treatments by latin letters A, B, C, etc. or by numbers 1, 2, 3, etc. Such
arrangements are readily available in the Tables for Statisticians and
Biometricians (Fisher and Yates, 1948). One of these squares of any
order can be written systematically as shown below for a 5x5 square.

TABLE 2.3

A 5 X 5 Latin Square Written Systematically

A

B

C

D

E

B

C

D

E

A

C

D

E

A

B

D

E

A

B

C

E

A

B

C

D

For the purpose of randomization rows and columns of the square are
rearranged at random. Both the rows and columns are, therefore,
numbered separately. Keeping the first row as such the remaining
rows are rearranged and numbered. If the latin square is of order r, then
random numbers less than or equal to r—1 are selected by consulting-a
random number table or otherwise as indicated earlier. If the first number
chosen is nlr then the «xth row of the initial square is written as the second
row. If n2 is the second number and not equal to nv then the n2th row is
written as the third row. This procedure is continued till all the rows of
the initial square are placed at random to form another square. After
row randomization is over, the columns of the row randomized squares

COMPLETE BLOCK DESIGNS

59

are rearranged by following exactly a similar procedure as for row
randomization.

For example, the following is a row randomized square of the above

5x5 la tin square;

A

B

E

D

C

B

C

A

E

D

C

D

B

A

E

D

E

C

B

A

E

A

D

C

B

Next, the columns of the above row randomized square have been
rearranged randomly to give the following random square:

E B C A D

A C D B E

D A B E C

C E A D B

B D E C A

As a result of row and column randomization, but not the randomization

of the individual units, the whole arrangement remains alatin square.

2.3.2 Analysis of Latin Square Designs

In latin square designs there are three factors. These are the factors P, Q
and treatments. The data collected from this design are, therefore,
analyzed as a three-way classified data. Actually, there should have been
k3 observations as there are three factors each at k levels. But because of
the particular allocation of treatments to the cells, there is only one
observation per cell instead of k in the usual three-way classified orthogonal
data. As a result we can obtain only the sums of squares due to each of
the three factors and error sum of squares. None of the interaction sums
of squares of the factors can be obtained. Accordingly, we take the

model

where Ytjs denotes the random variable corresponding to the observation
yijs in ith row, jth column and under .sth treatment; [x, n, cj, ts
(iij,s=l,2,...,k) are fixed effects denoting in order the general mean,
the row, the column and the treatment effects. The etjs is the error
component, assumed to be independently and normally distributed with
zero mean and a constant variance a2.

The analysis is conducted by following a similar procedure as described
for the analysis of two-way classified data. The different sums of squares

are obtained as below:

60

DESIGN AND ANALYSIS OF EXPERIMENTS

Let the data be arranged first in a row X column table such that

denotes the observation of (z, y)th cell of the table.

Let Ri = Y. yu=ith row total (z=l, 2,..k),

j

C,=£ yij—jth column total (j= 1, 2,..k),

,/

F, = sum of those observations which come from 5th treatment

=5th treatment observation total (5=1, 2,.... k),

(7= X! grand total.

G2
Correction factor, C.F.=-^.

Treatment sum of squares= £ ~j^—C.F.

r2

Row sum of squares= ]T —C.F.

Rt2

/

Column sum of squares = X —C.F.

C/2

TABLE 2.4

Analysis of Variance of kxk Latin Squares Design

Sources of variation

d.f.

Rows

Columns

Treatment

Error

Total

s.s.

Ri2

Cj 2

jT-C-F.

T. 2

k—1

k—\

k-\

r

1

—
1

1

By subtraction

£2-1

2 y;,2—C.F.
ij

m.s.

F.

St2

52

The hypothesis of equal treatment effects is tested by F-test where F is the
ratio of treatment mean squares to error mean squares. If Fis not
significant, treatment effects do not differ significantly among themselves.
If F is significant, further studies to test the significance of any treatment
contrast can be made in exactly the same way as discussed for randomized
block designs.

COMPLETE BLOCK DESIGNS

61

2.3.3 Repeated Latin Squares

A latin square design is not normally used when the number of treatments
is eight or more, because a design of higher order requires too many
replications and it may not also be possible to get the required type of
experimental units.

Again, if the number of treatments is very small, then also there are
difficulties for adopting a latin square design. When there are two treat¬
ments a latin square design cannot be adopted, because from a 2x2 latin
square design error variance is not estimable. For a 3x3 latin square
design the degrees of freedom for error sum of squares is 2 and for a 4 x 4
latin square it is 6. In both these cases the degrees of freedom for error
sum of squares are two small. To make the design more effective in such
cases, the latin square design may be repeated, that is, instead of taking
one latin square, a number of, say, P latin squares each of the same order,
is taken for the experiment. The treatments are the same in each square
but each has a separate set of units and a separate randomization. The
data obtained from such repeated latin squares are analyzed as below.

Each of the P latin squares is first analyzed separately by following the
method described above. The corresponding sums of squares obtained
from the different squares are then added. This gives the pooled row,
column, treatment and error sums of squares. The pooled row sum of
squares is also called ‘between rows within square sum of squares’ and
similarly for the other pooled sums of squares.

From each of the p squares, the k treatment totals are obtained. With

these totals apxk table of squares X treatment is prepared.

Let Pi denote the total of all observations in zth square,

(/= 1, 2,..., p)

Ts denote the total of observations of 5th treatment from all

the latin squares, (5=1, 2,..., k)

and Tis denote the total of all observations of 5th treatment in z'th square.
The square X treatment table is formed with these Tia totals. The totals
Pi and Ts are the marginal totals of the Square X Treatment Table.

Next, the following sums of squares are obtained:

Correction factor=(£ F<)2/p^2

/

Pi2

Sum of squares due to squares = £ £2 ~ C.F.

i

2

Sum of squares due to treatment= X C.F.

Treatment x square interaction=(Pooled treatment s.s.)

-<£&7CF->

rT' 2

Total sum of squares = X Jo*/- C.F.,

62

DESIGN AND ANALYSIS OF EXPERIMENTS

where yijst denotes the observation from tth square in its ith row, jth
column and under 5th treatment. The following partitioning of the
degrees of freedom of analysis of variance then follows:

TABLE 2.5

Partitioning of Degrees of Freedom in the Analysis of Variance of
Repeated Latin Squares

Sources of variation

Squares

Between rows within squares (pooled)

Between columns within squares (pooled)

Treatments

Treatment x squares interaction

Error (pooled)

Total

d.f.

P—1

Pik-1)

p(k—1)

k—1

(p-l)(fc--l)

p(k-\)(k-2)

pk*-l

The testing and other procedures are the same as in ordinary latin square

designs.

2.3.4 Graeco Latin Square Designs

We have seen that by using latin square designs treatment effects can be
estimated by eliminating two sources of variation. This technique can
be extended further to eliminate more sources of variation. A Graeco
latin square is one such design where three sources of variation can be
eliminated. This design can be defined formally as below.

An orthogonal design by which three sources of variation can be
eliminated by using only k1 units where k is the number of treatments is
called a k X k Graeco latin square design.

A design is said to be orthogonal when the data obtained from it are
orthogonal. When all the levels of a controlled factor occur with each level
of any other controlled factor in a design, the data obtained from such a
design are always orthogonal.

In order to make the data from aGraeco latin square orthogonal, we
have to take another controlled factor R at k levels in addition to the two
controlled factors P and Q introduced for the latin square design, such
that each level of R occurs with each level of P and also of Q only once.
If treatments in an ordinary latin square design are taken to be levels of
the factor R, then such an arrangement is provided by the latin square
design. In that case we have to allocate treatments to the units such that
each treatment occurs once with each level of the controlled factors P, Q

COMPLETE BLOCK DESIGNS

63

and R in the k2 units. For example, let us replace the five treatments
symbols A, B, C, D and E in the example of the latin square design written
systematically by the five Greek letters a, (3, y, § and 0 respectively. These
letters represent the five levels of the factor R. We then get the following
arrangement of five levels of each of three factors in 52 units:

Levels of P

a (3 y S 0

(3 y 8 0 a

Levels of Q

Y 8 9 a (3

8 0 a (3 y

0 a ,3 y 8

Now, five treatments denoted by A, B, C, D and E are to be allotted to
the above 25 units such that each treatment occurs once in each row, each
column and with each of the Greek letters.

It is not easy to allot the treatments to the units so as to satisfy the
above requirements of a Graeco latin square design. The problem can,
however, be solved easily by exploiting the properties of orthogonal latin
squares described below.

2.3.5 Orthogonal Latin Squares

Two latin squares each of the same order, say, r are said to be orthogonal
if when one is superimposed on the other each symbol of one falls on each
symbol of the other once and only once.

For example, the following two latin squares are orthogonal.

Square I

A

B

C

B C

C A

A B

Square II

a

Y

P

P Y

a (3

Y «

We shall discuss the methods of construction of orthogonal latin squares
in Chapter 6. Orthogonal latin squares are also available in the Tables
for Statisticians and Biometricians by Fisher and Yates (1948).

For construction of a Graeco latin square design we have to take two
orthogonal latin squares each of order k. One of these squares is written
by using Latin letters and the other by using greek letters. By super¬
imposing one square over another and by treating the Greek letters as the
levels of the third controlled factor R, we get the Graeco latin square design.
The rows and columns of the square denote levels of the other two
controlled factors.

64

DESIGN AND ANALYSIS OF EXPERIMENTS

For example, the following is a graeco latin square with five treatments.

a A

Y D

8C

6 B

Y A

8 E

6Z)

a C

ye

8 B

6 A

a E

Si)

0C

v.B

'M

Y E

9 E

a D

pc

Y B

SA

The randomization procedure of this design is the same as that of the
latin square design. The analysis is also the same excepting that an extra
component of the sum of squares due to the factor R is to be obtained in
addition to the usual sums of squares for the latin square design.

These designs are supposed to be very efficient but it is very difficult to
get situations and the required types of experimental units for adopting
such designs. This procedure can be extended further to get hyper-graeco
latin square designs which can be used to eliminate four or more sources of
variation. These designs can be constructed by superimposing three or
more mutually orthogonal latin squares. Utility of such designs is,

however, limited.

2.4 Missing Observation in Randomized Block Designs

It has been pointed out earlier that sometimes observations from experiments
get lost due to unavoidable circumstances. Consequently, the data become
non-orthogonal and they cannot be analyzed according to the method of
analysis suggested for the design. Starting with Yates (1937) several
attempts have been made to simplify the method of analysis of experiments
with missing observations avoiding the complication of analysis of non-
orthogonal data. Some of these methods are discussed below.

2.4.1 Analysis by Estimating the Missing Observations

The method of analysis of experiments with missing observations by
estimating the missing observations is due to Yates (1937). It consists of
estimating the missing observations by the values which make the error
sum of squares minimum. In order to get such estimates first unknown
values are substituted for the missing observations. The error sum of

COMPLETE BLOCK DESIGNS

65

squares for the design is then expressed as a function of these unknowns.
Next, by differentiating the error sum of squares with respect to the
unknowns and equating the differentials to zero, as many linear equations
in the unknowns as the number of the missing observations are obtained.
Solutions of these equations provide the estimated values of the missing
observations.

The data are then completed with these estimated values and analyzed
by the usual technique appropriate for the design. From this analysis the
correct error sum of squares is obtained but not the treatment sum of
squares. In the case of randomized block design the correct treatment sum
of squares is obtained by subtracting the correct error sum of squares
from ‘within block sum of squares’ obtained from the incomplete data.
The degrees of freedom of the error sum of squares is reduced by the
number of missing observations.

For example, suppose in a randomized block design with k treatments
and r replications, two observations are missing. Let these missing obser¬
vations belong to different blocks and affect different treatments and be
substituted by the unknowns xx and x2. We assume that xt belongs to
jth block and ith treatment and x2 belongs to j'th block and mth treatment.
Let Bj denote the observation total of jth block taking zero for the
missing observations. Similarly, Bj denotes the total of the j'th block.
Tt and Tm are similar totals for ith and mth treatments respectively.
Further, let G denote the grand total of the observations obtained by taking
zero for the missing observations.

The error sum of squares expressed as a function of xx and x2 is as

given below:

Error s.s. = C+*i2+xa2

(Bj +*i)2
k '

CBj> 4-X2)2 (Tz-t-Xx)8
k ~ r

(Tm±x 2)2 (Cr-f-X, -Lx,)2
r ^ kr

where the constant term C does not contain xx and x2. Differentiating
partially this error sum of squares with respect to x1 and x2 and equating
the differentials to zero the following equations are obtained:

x Bj-\-x Tt + xx G+x1+x2_q

1 k r ' rk

„ Bjf-\-x% Tm+x2 t G!+xI-Fx:j_rk
*• k ~ r *" rk U>

Incidentally, if only one observation is missing, its estimate can be obtained
from the first of the above two equations by putting x2=C and gettihg
xx as

kTi+rBj—G
\r- !)(*-!)*

The solutions of xx and xt from the above two equations are

66

and

DESIGN AND ANALYSIS OF EXPERIMENTS

(r— 1) (k— 1) (kTi+rB ;—G)—(kTm+rB)i G)
(r—1)2(£—1)2-—1

(r— \)(k—\){kTm+rBj'—G)—(kTi+rBi — G)
{r-if{k - 1)2-1

"the data are now completed by substituting x1 and x2 for the missing
values and analyzed by the usual method. The error sum of squares
obtained from this analysis is the correct error sum of squares. Next,
‘within block sum of squares’ is obtained ignoring and x2. This is actually
the error sum of squares on the hypothesis of equal treatment effects. By
subtracting the correct error sum of squares from within block sum of
squares the exact treatment sum of squares is obtained.

Though the treatment and error sums of squares could be obtained by
this method without much difficulty, it is very much complicated to obtain
the variance of the estimates of treatment contrasts when this method is
followed. Such variances can, however, be obtained easily when the data
are analyzed as non-orthogonal data as discussed below.

2.4.2 Analysis by Taking the Data as Non-Orthogonal

When the data become non-orthogonal due to missing observations in a
randomized block design, they can be analyzed as such without much
difficulty when the number of missing observations is not large. As an
example we take the same data as discussed in Section 2.4.1.

Let ti and tm denote the effects of treatments which have missing obser¬
vations and /,(/>= 1,2, .. .,k but not i and m) denote the effects of the
remaining treatments.

Let

(p=ly 2, .. .,k butp^i,p=£m)

where the totals Tu Tm, Bj, By and G have the same definitions as in
Section 2.4.1 Tp is the observation total of pth treatment. By following
the method of analysis of non-orthogonal data as discussed in Chapter 1,
the reduced normal equations for estimating treatment effects are as follows
(^denotes the estimate of 1/ for all i):

r—2 2

( r k k-l

COMPLETE BLOCK DESIGNS

67

H-rraM- k ' k ^r)?r'-r-

- r-2- ^
~jr~ tm—Qi

With the restriction 2 f*=0, these equations reduce to

4 = 1

k ~^k  \)^tp

rJr+li±^=Qr

(r-l)(k—l)ti+tm=(k—l) Qt

(r— 1){k— \)Tm+7t=(k—1) Qm.

The solutions of these equations are

7>=T-r>-0^-"l)+l} (P=2.k’P*U

k—\ J

Ql~hQm

Qi Qm

2 1 Xr-l)(fc-l)+l !  (r—\)(k— 1)—

k-1 1 f Qi^rQm
' 2 | [(r-l)(/c-l)+l  (r-1)^-1)-

Qi-Qm

The adjusted treatment sum of squares is obtained from

pj*i, m
The unadjusted block sum of squares is obtained from

2 t pQp-\-imQm-\-tiQi

y B? B?+B,,2

and the total sum of squares, from

2 yrf.
ij

The analysis of variance can now be written as in Table 2.6.

Analysis of Variance of Non-Orthogonal Data Due to Missing Observations

TABLE 2.6

Source of

variation

Blocks

(unadjusted)

Treatments

(adjusted)

d.f.

r— 1

k—\

s.s.

m.s.

F

Bi2 Bj2+B)>*

£ b d ‘b_i
K K 1

2 tpQp + tiQf¥tmQm

p^l, m

s,*

s2

St*ls*

Error

(r—1) (k—1)—2

by subtraction

Total

rk—3

s yua
U

68

DESIGN AND ANALYSIS OF EXPERIMENTS

The estimate of tt—tm is given by

r 7 £ (Qi~Qm)
‘ \)(k-1)—1

We know that if £ Af) = XI #<£?/» then

i i

F(X hu)=°2 X Uqi-

i i

— — . 2fc<r2

Hence,

Similarly,

T„- -x ,fl , r(fc-l)+2 Ar—1 1
6)-ci [_7+2r{(r-l)(A:-l)+l}+2{(r-l)(Ar-l)-l>J

There are two other possible ways of two missing observations in a design,
that is, (i) when they are both in the same block and (ii) when they are
the two replicates of the same treatment. The analyses of all these
cases together with the variance of estimates of treatment contrasts
following this method have been given by Das (1954).

2.4.3 Analysis by the Technique of Analysis of Covariance

The analysis of covariance technique has been discussed in detail in
Chapter 8. For further reading on this topic the readers are referred to
that chapter.

For applying this technique suitable ancillary variates are first defined

as below.

Let the missing observations be numbered first in some order and let
Xt (i=l, 2,..., n) denote the ancillary variate for the ith missing observation.
Then takes the value 1 for the unit in which it is missing and zero in all
other units. There will, therefore, be n ancillary variate values in each
unit. Next, the data are analyzed by the technique of analysis of
covariance as appropriate for randomized block design in presence of rt
ancillary variates. For this analysis values of the missing observations
are taken as zero. This technique gives the correct error and treatment
sums of squares. It has been discussed in detail in Chapter 8.

2 4.4 Missing Observations in Latin Square Designs

Analysis of latin square design with missing observations can be carried
out by the three methods described earlier in case of randomized block
design. The method of analysis treating the data as non-orthogonal is
similar to that for randomized block designs. This method has been
discussed by Das (1955).

The ancillary variates required for applying the covariance technique
are defined in exactly the same way as in randomized block designs. The

COMPLETE BLOCK DESIGNS

69

analysis of covariance appropriate for latin square designs is then worked
out.

The method of analysis by estimating the missing observations needs
some modification as described below. First, the unknowns are substituted
for the missing values and error sum of squares is expressed as a function
of these unknowns. Next, the equations are obtained in exactly the same
way as in randomized block designs. The solutions of these equations
give the estimates of the missing observations. The completed data are
then analyzed by the method appropriate for latin square designs. This
analysis gives the correct error sum of squares but not the correct
treatment sum of squares.

To get the correct treatment sum of squares, the treatment classification
is first ignored so that only the row and column classification remains.
Now, unknowns are again substituted for the missing observations.
These are estimated by following the method for randomized block designs.
Then the error sum of squares is obtained from the completed data. Let
this error sum of squares be denoted by E1 and the error sum of squares
obtained previously for the latin square design be denoted by E. Then,
Ex—E gives the correct treatment sum of squares. The degrees of freedom
of the error sum of squares is reduced by the number of observations
missing. Das (1955) has given a convenient method of analysis when x
observations are missing each in a separate row and column and each
affecting a different treatment. If // and U' denote two affected treatments
in such cases and there are n missing observations, then he has obtained
the following variances of the estimates of different treatment contrasts of
interest.

where tb denotes the effect of an unaffected treatment.

2.4.5 Latin Squares with a Missing Row or Column

The method of analysis of a latin square with a missing row or column is
the same. We have discussed the case of missing row. The results
appropriate for missing column can be obtained easily from this analysis.

Let one row of an rxr latin square be missing. The design, now,
does not remain latin square but becomes what is known as Youden Square.
It is an incomplete block design, by which two sources of variation can
be eliminated. In each of the remaining rows of the design all the treat¬
ments are present. All the columns are also equally represented in each
row. But all the treatments are not present in each column. So the

70

DESIGN AND ANALYSIS OF EXPERIMENTS

treatment and column are non-orthogonal while the row X treatment and
row X column classifications are orthogonal. The treatment sum o
squares has, therefore, to be adjusted for the columns by following the
method of analysis of non-orthogonal data. The reduced normal equations
for this purpose are as follows. Let n denote the effect of ith treatment
(i = l, 2,..., r) and Qi denote the adjusted total of ith treatment and is
given by Qi = Ti-Si where S( is the sum of the averages of those columns
in which ith treatment is not missing and Tt is the total of ith treatment.

(r-£ r„=fi, (1=1,2,. ...r)
V ' r—lj r-1

r (r-l)Qi
U~r(r-2) ‘

The analysis of variance results are then obtained as below. Let i?„ Cj,
etc. denote respectively the row and column totals and C.F. = G2/r(r 1)

where G is the grand total.

TABLE 2.7

Analysis of Variance of Latin Square Design with a Missing Row

Source of variance

d.f.

s.s.

m.s.

F

Rows

Columns

Treatments

Error

Total

r—2

r-1

r-1

*<2

S —-C.F.
i r

Cj2

S ——C.F.
J r

(r-D ^ ^ „
r (r—2) * Qs

(r-1) (r—3)

By subtraction

r2—r—1

2 yijk2—C.F.

st2ls2

**2

s2

The variance of the estimate of the difference between any two treatments is

obtained as below:

V(ti-Tm)= r(r_2) °2-

If a column is missing instead, the results do not change excepting
that the adjusted totals Q{s are now row adjusted instead of being column
adjusted as presented here. The reader is referred to Giri (1963) for the
combined analysis of Youden squares and latin squares designs with

some common treatments.

COMPLETE BLOCK DESIGNS

71

2.4.6 An Alternative Method of Analysis of

Experiments with Missing Observations

In a randomized block design with k treatments and r replications let n
observations be missing such that each belongs to a different block and
a different treatment. Let the missing observations be denoted by the
unknowns x„ x2,..., xn, written in some convenient order.

Let 7f (7=1, 2,..., n) denote the total of the treatment to which ith
missing observation belongs and be obtained by taking zero for the
missing observations. Similarly, let Bt (/=1, 2,..., ft) denote the total of
the block to which z'th missing observation belongs. This is also obtained
by taking zero for the missing observations. Again, G denotes the grand
total of all the observations taking zero for the missjng ones.

The error sum of squares as a function of the unknowns can now be

written as below:

„ , ” „ ^+*02 (G+2*)2
Error s.s. = Cj+ 2 xr—2 -— -2 —r-h -—-r—-
;=1 i r i K rK

where C1 does not contain any of the x<’s. That is.

Error s.s. =C,+i?2 x,2-22 x,Mi+2 2 ^
i i i >j r/c

(2.1)

where C2 is different from Cx but does not contain the x,-’s

and

R==i-1— 1+ L
r k rk

M TiS- Bt G
M,-7+k'7k

The missing values are estimated by minimizing this error s.s. with respect
to the xi’s. The equations, obtained by partial differentiation of the error
sum of squares with respect to xt, are

rkRxt+ 2 Xj—rkMi (i=l, 2(2.2)

From (2.1) it is seen that C2 is the error sum of squares obtained by
putting zero for each of the missing observations. Again,

R2x?+2 2

i i>j rlc

say, is the error sum of squares obtained by putting the existing
observations as zero and the missing observations as xt (i= 1, 2
Eliminating Mi from (2.1) with the help of (2.2), we get

Error s.s. (E)=C„—i?2 x*2—2 2 (2 -3)
i i» rk

=C.-CX.

Though the result (2.3) is obtained for the particular case described in

72

DESIGN AND ANALYSIS OF EXPERIMENTS

the beginning of this section, it is true in general for all designs including
the incomplete block and latin square designs even when the observations
are missing in a general fashion.

Adding the n equations of (2.2) we get

that is,

(rkR—1)2 X/+/J 2 Xi—rk'Z Mi

/ i i

rk'ZMi

^]Xl~{rkR—\+n)‘

From (2.2) we have

{rkR-\)xi+'Zxi=rkM, (2.4)

Substituting for 2 xi in (2.4) we get

, f 2 Mi i

Xi=(rkR - i) lMi“ rkR-1+nj ^2‘5^

A general solution of the equations is thus obtained from (2.5) in the
particular case under consideration. The treatment sum of squares is
obtained by subtracting the true error sum of squares as obtainable
from (2.3) from another error sum of squares, say, Ex obtained on the
hypothesis that the treatments are all zero and, therefore, ignoring the
treatment classification.
On this hypothesis,

ir1=C3+i?12x/'2-2 2 (2.6)

where i?!=(A:—l)/k and Xj' (*=1, 2,...,«) denote the unknowns substi¬
tuted for the missing values. Obviously, these are different from the xt s
(because of ignoring the treatment classification).

C3 is free from xx (i=l, 2,..., ri) and is actually (Treatment s.s.+

Error s.s.) obtained by putting zero for the missing values. We put
C3=(T.s.s.)0+(E.s.s.)0 where (T.s.s.)0 denotes the treatment s.s. obtained
by putting zero for the missing values. Similarly, (E. s. s.)0 is defined.
The equations for obtaining xt (i=l, 2,... ,n) are

or,

RlXl -k
R y'—Bi

2»-- •’ n)-

Substituting it in (2.6) we get

COMPLETE BLOCK DESIGNS

73

From (2.3)

E~C%—CX

The correct treatment s. s.=EX—E

=(E.s.s.)0— Cx, since C,=(E.s.s.)0.

X W

=(T.s.s.)0- *k (A:_1)+C*

The variances of the estimates of different types of treatment contrasts for
this general case of missing observations have been given by Das (1954).

Alternative Method for latin square design. Let n observations be missing
in a latin square design such that each observation is missing in a different
row and column and affecting each time a different treatment. Let these
observations be denoted by the unknowns*!. x2,..., x„ in some order.

Further, let denote the total of the row to which the z'th missing
observation belongs. Similarly, C,- and 7) are the totals of the column and
treatment respectively to which the z'th missing treatment belongs. These
totals are obtained by taking zero for the missing values. G denotes the
grand total obtained by putting zero for the missing values.

The error s.s. as function of */’s is as below:

Error s.s. (E)=C2'+R 2 x,*+*2 2 x,xj-2 2 x,Mi (2.7)

where C2' is a constant not containing xfs

n (r-l)(r-2) „ r(T,+R,+Q)-G
zv— -g > -"2 •

Though the same symbols R and Mi have been used for both randomized
block designs and latin square designs, there is no chance of confusion.
The equations for estimating Xi (z= 1, 2,. .., n) are as below:

Rxt+-„ 2 xj=Mi (z=l, 2,.. .,n)

r j*i

(2.8)

These equations can be solved exactly as in randomized block designs in
the Section 2.4.6. The solutions are

f 22Mi |

X,=F^3{ Mr~r3-3r + 2/z J (,==1, 2>'' *’ ")

(2.9)

Now,

E=C\— Cx where CX=R 2 xi2+-„ 2 xiXj

i r i> J

Expressing (2.7) as a function of Mi by using (2.8), error sum of squares
can also be obtained by

74

DESIGN AND ANALYSIS OF EXPERIMENTS

£=C2'—2 XtMi

( 2 (2 M,Y \

= Ca'-^3UW'a-7C3^iJ

By following a procedure similar to that for the randomized block designs
the correct treatment s.s. can be obtained as below:

Correct treatment s.s

/ (2 Nif \

2 a Mi? \

—3{^^-3r+2n

' )

where

N, =r — (* = 1, 2,.. .,ri).

The formulae for the variances of estimates of different types of treatment
contrasts have been given in Section 2.4.4 for this general case.

2.5 An Illustration

The method of analysis of a randomized block design with two missing
observations has been illustrated below by analyzing a set of experimental

Yield Data of 10 Varieties of Fodder Crop Collected Through a Randomized

Block Design with 3 Replications

TABLE 2.6

Variety
nos

Block I
yield dev.

Block II
yield dev.

Block III
yield dev.

Variety total (adjusted)
(dev. total)

1

2

3

4

5

6

7

8

9

10

27

21

12

6

X(0)  —11

20

9

X(0)  —15

13

22

23

-2

7

8

11  —4

1  —10

8  —3

5  —6

18

23

7

12

30

14

16

0

3  —11

7  —7

6  —8

20

18

6

4

3  —12

4  —7

5  —9

11  —4

19

4

Total

150

Average

15

9

0

20

11

110

11

4

5

18

19

140

14

17

15

—36

—12

—7

21

12

—28

9

9

COMPLETE BLOCK DESIGNS

75

data collected from a variety trial on 10 varieties of fodder crop in Bihar.
A randomized block in three replications was adopted. The plot size was
36' X 29'. The data in kg. per plot are presented below along with the
deviates of the observations from their block averages. Two observations
were missing and they are indicated by X. These data have been analyzed
by the alternative method discussed in Section 2.4.6. The first part of
analysis consists of analyzing the data taking zero for the missing obser¬
vations. This part illustrates the method for randomized block designs.

(r,.s.s.)=| (172+152+ • • • +92)=1178

Total s.s. of the deviations—2048

(within block s.s.)

(E.s.s.)0=2048 —1178=870

Block s.s. =5804.44

Total s.s. =7468.00

Calling the missing observation in block 1 as the first missing obser¬

vation and that in block 2 as the second missing observation, we have

110 ,57 400 _50
M<1~ 10 3 30 3

Mi M2
rkR—\ +m

=3.47

30/50 59 \

JCa—17 V 3 3x19/

=27.59

=0.6 (3.472+27.592M

2x3.47x27.59

30

=470.16

Correct error s.s. =(E.s.s.)0—C*=870—-470.16

=399.84

76

DESIGN AND ANALYSIS OF EXPERIMENTS

Corrected T,.s.s. =(Tr.s.$.\-1 * +CX

B *4-B *

= 1178-384.44+470.16

= 1263.72

TABLE 2.7

Analysis of Variance of the Data in Table 2.6

Sources of variation

d.f.

s.s.

m.s.

F.

Blocks (unadj. uncorrected) 2

Treatment (corrected)

Error (corrected)

Total (uncorrected)

9

16

27

5804.44

1263.72

399.84

7468.00

140.41

24.99

5.6**

Since F is significant at 5 per cent level of significance, the varieties
differ significantly among themselves. The variety effects estimated by
substituting the estimated values of the missing observations are shown in
the descending order for comparing them two by two.

Variety no. 1* 6 2 7 9 10 5 4 8 3*

Averages 28.2 20-3 18.3 17.3 16.3 16.3 11.0 9.3 4.0 2.5

*indicate treatments having missing observations.

v (h—*3)= i)2(fc — i)_f = 20x 24.99__29.41 (both affected)

- - 2a2

v (t2—tu) = — = 16.67 (non affected)

v

■ r(A:-l)+2 ,
+2r{(r-l)^-l)+i}+2

k-1 "I
{(r—1) f/c—1)—1>J

=24.99

\3^6x 19^2x17/

=21.30 (one affected)

EXERCISES

1. When there are n missing observations in a randomized block design such that
each observation is missing in a different block affecting each time a different
treatment, find the variances of the estimates of the missing observations obtained
by minimizing the error variance. Find also the covariance between any two
estimates.

COMPLETE BLOCK DESIGNS

77

2. An experiment was conducted in two different places adopting the same latin
square design in each place. Give a method of combined analysis of the data
collected from the two places, assuming that the error variances are the same in
both the places.

3. Derive the method of analysis of a latin square design in which a row and a

column are missing.

4. In a randomized block design with k treatments and r replications r>k, a
replication of ith treatment is missing in ith block (i=l, 2, ..., k). Derive the
expressions for estimates of the missing observations and hence give the
computational procedure for the analysis of the data.

5. An experiment was conduted at Indian Agricultural Research Institute, New Delhi
during rabi 1970-71 under irrigated condition to determine the optimum dose of
ammonium sulphate for Kalyan Sona variety of wheat. Details of the experiment
are given below:

(i) Design—Latin square design
(ii) Treatment—A— 0 kg N per hectare
B— 40
C— 80
D—120
E—160
F—200

99

99

99

99

99

(iii) Plot size—8 m x 0.60 m

Layout plan and wheat yield in kg. per plot
F 2.19
E 2.27
B 2.04
A 0.77
D 2.50
C 1.52

E 2.50
C 1.41
A 0.91
B 2.04
F 2.31
D 1.86
(a) Analyze the data.
(b) If the yield corresponding to treatment A in the second row is missing
analyze the data. Give the standard error of the difference between estimates
of the effects of treatments A and D.

B 1.82
A 0.91
B 1.95
F 2.13
D 2.50
C 2.07
C 1.82  D 2.50
E 2.27
A 0.91
F 1.98
E 2.30

D 2.27
A 0.91
F 2.25
E 2.40
C 2.09
B 1.91

C 1.62
D 1.91
E 2.29
F 1.99
B 2.04
A 0.77

(c) Supposing the yield corresponding to treatment B in row four is also missing
analyze the data. Give the standard errors of the difference between estimates
of treatments (i) A and B, (ii) A and D, and (iii) C and D.

REFERENCES

1. Das, M.N. (1954). “Missing plots and randomized block designs with balanced

incompleteness”. Jour. Ind. Soc. Agri. Stat. 6, 58-76.

2. Das, M.N. (1955). “Latin squares with several missing observations”. Jour. Ind.

Soc. Agri. Stat. 7, 46-56.

3. Duncan, D.B. (1953). “Multiple range and multiple F-tests”. Mimeo. Tech,

Report no. 6, Va. Polytechnic Inst.

4. Fisher, R.A. and Yates, F. (1948). Statistical Tables for Statisticians and

Biometricians. Hafner Publishing Co. New York.

5. Giri, N.C. (1963). “A note on the combined analysis of Youden squares and

latin square designs with some common treatments”. Biometrics 19.

6. Yates, F. (1933). “Analysis of replicated experiments when the field results are

incomplete”. Emp. J. Exp. Agri 1, 235-44.

7. Yates, F. (1936). “Incomplete latin squares”. Jour. Agri. Sci. 26,301-15.

CHAPTER 3

Factorial Experiments

3.1 Characterization of Experiments

There are several types of experiments which require statistical investigation.
These are characterized by the nature of treatments under investigation
and also the nature of comparison required among them so as to meet the
objectives of the experiment. There are three main types of experiments:
(i) varietal trials, (ii) factorial experiments and (iii) bio-assays. In varietal
trials treatments like (a) different varieties of a crop, (b) several feeds for
animals, (c) different doses of a drug, etc. are under investigation. In fact,
different levels of only one factor usually form the treatment in varietal
trials. The main purpose of such experiments is to compare the treatments

in all possible pairs.

In factorial experiments combinations of two or more levels of more
than one factor are the treatments. For example, with two factors
(i) nitrogen fertilizer at three levels, denoted by n0, nl and n2 and (ii) irriga¬
tion at two levels, 70 and Ix in an agricultural experiment we can form the
following six combinations taking one level from each factor I0n0,I0nx,
I0n2, Ixna, Ixnx and Ixn2. Such combinations form treatments in factorial
experiments.

The comparisons required in this type of experiments are not the pair
comparisons as in varietal trials but a special type of comparison called
main effects and interactions. The contrast obtained from the difference
of the totals of the first three and the last three of the above six combina¬
tions gives the main effect contrast for irrigation. This is so, because the
total of the first three treatment combinations represents the effect of
irrigation at its 70 level, while the sum of the last three represents its
effect at Ix level, of course, in each case in presence of different levels
of nitrogen. Hence, their difference gives a comparison between the
responses from the two levels of irrigation. This comparison, therefore,
represents the main effect of irrigation.

Similarly, two independent comparisons among the totals, 70/i0-F71flo>

70n1+71n1 and 70nJ-f-71/i2 represent the main effect of nitrogen.

Again, we can get an effect of irrigation in presence of, say, n0 from

70n0—Two more such effects can be obtained from the other two
levels of nitrogen, viz. I0nl—Ilnl and I0n2—Ixn2. Comparison among these
three contrasts indicates the equality or otherwise of the effects of irrigation

FACTORIAL EXPERIMENTS

79

at the different levels of nitrogen. This sort of comparison, therefore,
indicates if the factors act independently or they interact to influence the
yield of the experimental unit on which they appear simultaneously.
Contrasts representing such comparisons, that is, (I0n0—Ixn^)—{hn\—Fi«i)
are called interaction effects. In the present example there are in all two
interaction contrasts.

There is, again, a third type of experiment called bio-assays, as stated
earlier. In one category of these experiments usually two preparations
of drugs are taken, each at several doses. These doses form the treatments.
The main comparisons required for the assay are (i) a comparison giving
the difference between the two preparations and (ii) comparisons
representing the slopes of the effects of the doses of each preparation on

the doses.

Each type of experiment has got its optimum management which
includes its design as well. We shall discuss in detail the factorial
experiments in this chapter leaving the other topics for the present.

3.2 Factorial Experiments

As stated earlier a factorial experiment involves simultaneously more than
one factor each at two or more levels. If the number of levels of each
factor in an experiment is the same, the experiment is called symmetrical
factorial, otherwise, it is called asymmetrical factorial or sometimes mixed
factorial. Only symmetrical factorials will be discussed in this chapter.

These experiments provide an opportunity to study not only the
individual effects of each factor but also their interactions. When
experiments are conducted factor by factor changing the level of one factor
at a time and keeping the other factors at constant levels, the effect of
interaction cannot be investigated. In many biological and clinical trials
factors are likely to have interaction. Therefore, factorial types of
experiments are more informative in such investigations.

They have the further advantage of economizing on experimental
resources. When experiments are conducted factor by factor, much more
resources are required for the same precision than when they are tried in
factorial experiments. For example, to conduct the experiment described
in Section 3.1 by adopting a randomized block design so as to have at
least 10 d.f. for error variance, we require six replications for the experi¬
ment on nitrogen alone and 11 replications for the second experiment on
irrigation. Therefore, a total of 40 experimental units are required. But
for conducting a factorial experiment with six combinations of the two
factors as treatments, we require only 18 plots (units) for similar precision.

80

DESIGN AND ANALYSIS OF EXPERIMENTS

3.3 Factorial Experiments with Factors at Two Levels /

Sometimes experiments are conducted with factors each at two levels.
The levels of a factor may be its presence and absence or a high and a
low dose or even two modes of application of a technique. For example,
an experiment was conducted with several factors each at two levels. One
of the levels was the Indian method and the other was the Japanese method
of agriculture with respect to factors like seed rate, method of cultivation,
irrigation, etc.

We shall denote the factors in a general way by the letters A, B, C etc.
unless otherwise specified. Several types of notations of the levels of the
factors are in use. These notations are always in codes. One type is
a0 and ax for the factor A and similarly for the other factors. They
represent both qualitative and quantitative levels.

One more type of level codes used are 0 and 1 for each factor. As we
shall see afterwards, these codes are subjected to mathematical treatments
as well.

The simplest of the factorials consists of two factors each at two levels.
This factorial is called 22 as there are four combinations in the experiment.
Denoting the factors by A and B, the combinations can be written either as

aQbQ, Giby and ^\b y

or 00, 01, 10 and 11.,

Sometimes, the combinations are also written as

I, a, b and ab.

The symbol I denotes that both factors are at the lower levels in this
combination. It is also called the control treatment.

When there are three factors each at two levels, the factorial is denoted

by 23 as there are eight treatment combinations. These are written as

a0Vo, 4>Vi, ajbiCq, u^b\Cy, a^b^c^, ttyb^c^ ayb yCq and a-Jb^C\.

The general factorial with n factors each at two levels is denoted by 2".

3.3.1 Designs for 2n Factorials, Main Effects and Interactions

For 28 or 23 factorials any of the three designs, viz. completely randomized,
randomized block and latin square, can be used. But their analysis involve
some more partitioning of the treatment s.s. to obtain the main effect and
interaction variations of the factors.

The analysis of the randomized block design for the 2a factorial in r
replications is given in Table 3.1 (Tu denotes the observation total of the
treatment cambination a,-6y, i«=0,1; j=0,1):

It will be seen that the 3 d.f. for treatment variation have been divided
into three components A, B and AB each having 1 d.f. The first two
components are the main effects of the factors A and B respectively and
the third component is their interaction and is denoted by their product.

FACTORIAL EXPERIMENTS

81

TABLE 3.1

Analysis of Variance for 22 Factorials

Sources

Replications

Treatments

A

B

AB

Error

Total

d.f.

r—1

3

1

1

1

3 (r—1)

4/-1

s.s.

(— Too— ^oi+ ^io + ^n)2/^

(— Fo0+ r01—T10-f- ru)2/4r

(Tn0-T01-Tl0+Tn)ZAr

The contrasts representing A, B and AB are shown below with -f and

— signs against the treatment combinations.

Combinations

a0b0

a0b i

a,b0

aA

Contrasts

A B AB

- - +

- + -

+ - -

+ + +

The estimate of the main effect of A is the contrast among the treatment
totals: -T00-2’01+ri0+T11 where To0, etc. denote the observation totals
of the treatments. This contrast is evidently a comparison between two
group totals. In one of these groups, the factor A occurs at level a0 and
in the other at level ax. The two levels of B are evenly distributed in each
of these groups. The main effect of B is also a similar contrast. The AB
interaction is the difference between two contrasts. The first of these
contrasts is the difference between the first two combinations in the above
table and gives the effect of B at a0 level. The second contrast between
the last two combinations, gives the effect of B at ax level. So, the interac¬
tion component indicates if the effect of B is the same or different at the
two levels of A. If the effects of B are different at the two levels of ,4

the two factors are said to have interaction.

The s.s. due to each of A, B and AB is obtained by first obtaining the
contrast from the treatment totals and then dividing its square by the
total number of observations in the experiment. As the three contrasts
are mutually orthogonal, we can get the treatment s.s. from the total of

their sums of squares.

82

DESIGN AND ANALYSIS OF EXPERIMENTS

3.3.2 Analysis of 23 Factorial

We can get the seven mutually orthogonal contrasts representing the main
effects and interactions in 23 factorial from Table 3.2.

TABLE 3.2

Main Effect and Interaction Contrasts in 2s Factorials

Combinations

OoboCo
aab0cx

<*oVo
&obxcx

axbQc0

axb0cx

axbxc0

axbxcx

A

—

—

—

—

+

+

+

+

B

—

—

+

4*

—

—

+

+

Main Effects and Interactions

C AB AC BC

ABC

—

+
—

+
—

+
—

+

+

+

—

—

—

—

+

+

+

—

+

—

—

+
—

+

+

—

—

+

+
—

—

+

—

+

-f
—

+
—

—

+

The main effects A, B, C and interactions AB, AC and BC have been
obtained exactly as in 22 factorial. That is, the (—) minus sign has been
put against the combinations with a0 level of A and (+) sign against the
rest for getting the contrast of A. Similarly, for B and C. The AB
interaction has been obtained as the difference between two con¬
trasts, one representing the effect of B at a0 level and the other represen¬
ting the same contrast but at ax level. Levels of C have been ignored
while getting AB contrast.

In Table 3.2 there is one more interaction denoted by ABC. This is
called the three factor interaction or interaction of second order. It is
represented by a contrast which is the difference between two contrasts.
One of them is interaction AB at c0 level and the other is the same
interaction but at cx level. Similarly, a four factor interaction ABCD is
defined as a contrast formed of the difference between two contrasts one of
which is ABC at d0 level and the other, also ABC, but at dx level. The
higher order interactions can also be defined similarly. Though second and
higher order intractions can be understood in an inductive way, it is not
possible to comprehend their physical meaning. Normally, they are
found to be of the order of error. They are, therefore, considered to be
less important treatment contrasts.

Coming back to Table 3.2, the s.s. due to any effect is obtained by
first getting its contrast value from the treatment totals and then dividing
its square by the total number of observations. As the contrasts are
mutually orthogonal, the sum total of their s.s. gives the treatment s.s.
with 7 d.f.

FACTORIAL EXPERIMENTS

83

The contrasts in Table 3.2 can also be written mechanically as follows.
First, the contrasts for A, B and C are obtained as described earlier.
Then, the column for AB is obtained by multiplying corresponding entries
in a row under A and B and putting the product under AB in the same
row. Similarly, the other columns can also be obtained.

Again, the contrasts for A, B, AB, ABC, etc. can be obtained from the

following products:

A: (ax—o0)(^i+^o) (Ci + co)

B: (o1A~o0){b1 b0)(c^A-c0)

AB'. (fli—a0) (by b0) (cj+Cq)

ABC: (fli—a0) (b± b$) Cq)

The actual effects of A, B, etc. can be obtained from the difference of their
level means, or by dividing its contrast by half the total number of

observations.

It has been seen that with the help of each contrast of a main effect
or interaction the treatment combinations can be divided into two groups.
Qjjg group is formed of those which occur with negative sign in the contrast
and the other, of what occur with positive sign. *The interaction or main
effect is the difference between these two group means.

There is one more convenient method for getting such groups. This
method has been discussed in Section 3.5. In Section 3.4 below we have
discussed some mathematical methods which we shall use often.

3.4 Finite Fields and Designs of Experiments

Construction and analysis of several types of designs become very con¬
venient by using the properties of finite fields. We have discussed below
some of these properties which we shall require.

1.

2.

A rule is made that any positive integral number N is equal to the
remainder R when N is divided by an integer p. R is written as
R*=N mod. p. R is also called an element of module p.
If p is a prime number, then all the four operations of addition,
subtraction, multiplication and division are possible. That is, if any
two elements are operated upon by any of the operations, the result
is also another element of the same module.

For example, taking p = 7, the elements of mod. p are 0, 1, 2, 3, 4, 5

and 6.

Here,

3+4=0
3—4=3+7—4=6

3x4=5
3+4=(3+3x7)+4=6,

84

DESIGN AND ANALYSIS OF EXPERIMENTS

3. When any element of a prime module is multiplied in turn by all its
non-zero elements, each time a different product is obtained. This
ensures all possible divisions. This property does not hold when p is
non-prime. All divisions are also not possible in this case. When
division is possible, the elements are said to form a finite field (Galois

field).

4. There is at least one element in every field, different powers of which
give the different non-zero elements of the field. Such an element is
called the primitive root of the field. For example, when p —7, the
primitive root is 3, because

30=1, 3r=3, 32=2, 33=6, 34=4, 35=5.

We find that 3® is again 1. Actually, xp~l = \ where at is any element

of the field.

Through the above device an infinite set of numbers could be reduced
to only p elements. They can be manipulated just like the infinite set of
numbers. This is, however, not true when p is not a prime. But when p
is a power of a prime, such treatments are, again, possible by defining the
elements in the following modified ways.

1. Let the number of elements be s—pn where p is a prime and n any
integer. Let us now define s elements consisting of 0 and a—1 poly¬
nomials up to (n— 1) degree written by using any symbol, say, a. The
coefficients in the polynomials are the elements of mod. p. With these
elements as coefficients the total number of such polynomials is s— 1.

For example, 32 polynomials up to degree one are written below

using the elements of mod. 3 as coefficients:

0, 1, 2, a, a+ 1, a-)-2, 2a, 2a+ 1, 2a-f 2.

2. These elements can be added and subtracted mod. p, but they cannot
be multiplied or divided unless a device for reducing the polynomials
is obtained. Such a device consists of choosing an irreducible poly¬
nomial of degree n and then any polynomial of degree n or more is
equated to the remainder when it is divided by the irreducible
polynomial. Such reducing polynomials are called minimum functions.
It is not always very easy to obtain them. But some, which are
required often are given below.

Field

22

2s

32

Min. functions

a2+a+l

a3+af 1

a2+a-f-2

There may be more than one minimum function in a field. A full
discussion of the topic is available in Carmichael (1937).

FACTORIAL EXPERIMENTS

85

3. The non-zero elements can be obtained from different powers of a up

to ap"-2. For example, in the 32 field

a° = l, a 1=a, a2=2a+l, a3=2a+2,

a.4—2, a5=2a, a6=a+2 and a7=a+l

ap”-i is always 1. In this example, a8—1.

If the minimum function is wrongly chosen, the different powers of

a cannot be reduced by using it to get all the elements.

4. Multiplication and division become very easy and evident by using

such powers as elements. To continue with the example,

(a+2) (2a+2)=a6-a3=a9=a8-a=a.

(2a+2) (a + 2) = a3-^ a® = (a3 • a8) a6=a5= 2a.

In the present chapter we shall use such elements to have linear
equations and their solutions. The number of solutions of these
equations is finite.

3.5 Grouping for Interaction Contrasts

The elements of mod. 2, that is, 0 and 1 are taken as the level codes of
each factor at two levels. The different treatment combinations are then
formed by taking one level from each factor. When there are n factors,
the total number of treatment combinations is 2". We shall introduce the
various procedures for obtaining the interaction groups and their contrasts
with reference to the 23 factorial.

The treatment combinations of the 23 factorial are written as 000, 001,
010, 011, 100, 101, 110, 111. Let us now define a variate *i(i=1, 2, 3)
such that it takes as its values the level codes of the z'th factor in the
different factorial combinations. Though this variate is defined with
reference to 28 factorial, it gets generalized immediately.

We write the following pairs of linear equations using the elements,

0 and 1 as coefficients:

1 *x,+0-x2+0-a:8=0|

O-^+l'Xa+O-Xa^Oj

O'Xa+Oxj+l-Xa^Oj

l-xx + l'x2+0-x3=0|

1 -Xj+O-^-fl 'x3=0|

86

DESIGN AND ANALYSIS OF EXPERIMENTS

O-Xi+l-Xj + l-Xg^Oj

1 *x1+1 *x2-!-l •*3=01
= 1J

Solutions of each of two bracketed equations are mutually exclusive. These
are the possible linear equations that can be written with 3 variates using

coefficients, 0 and 1.

Using any of these seven sets of bracketed equations, we can divide
the eight treatment combinations into two groups of four each. One of
these groups is formed of the solutions of one equation and the other,
of the solutions of the second equation in the set. Comparison between
these two group totals gives either a main effect or an interaction contrast,
depending on the equation set from which they are obtained. In the
general case, there are 2” — 1 such sets of equations giving as many contrasts.

We now take the first set of equations. It is seen that the solutions of
the first equation in the set are those four combinations, in each of which
the factor A occurs at 0 level and in each of the solutions of the second
equation A occurs at 1 level. This set of equations, thus, gives two
groups of solutions and the contrast between these two group totals gives
the main effect A. Similarly, the next two sets of equations give groups
for the main effects of B and C respectively.

In the fourth set of equations, both, jqand x2 occur with coefficient 1.
The first equation in the set' is satisfied by combinations in which both
A and B occur at the same level. The other combinations satisfy the
second equation in the set. By examining the contrast of AB interaction
in Table 3.2, we see that the above two groups are exactly the two groups
compared. Thus, the AB interaction groups are obtained from the
equation set in which the variates corresponding to A and B occur with
coefficient 1 and the coefficients of the other variates are zero. Similar
considerations hold for higher order interactions as well. In general, the
solutions of the equation set

2 Pm^m-i 0=0, 1)

n

m-1

provide the groups for the interaction, A^A^*... Anp« where Av Az, etc.,
denote the factors and pm takes the value 0 or 1. Factors with power 1
only remain in the interaction.

Accordingly, the seven sets of equations provide the groups for the
following main effects and interactions: A, B, C, AB, AC, BC and ABC.

3.6 Confounding

>

We recommended that the 22 and 23 factorial experiments should be conduct¬
ed by using completely randomized, randomized block or latin square design.
We have also seen how these experiments are analyzed by breaking the
treatment components into main effect and interaction components.

FACTORIAL EXPERIMENTS

87

The next factorial, 24, has 16 treatment combinations and it is not
advisable to adopt a randomized block design for it, because blocks of
16 plots are too big to ensure homogeneity within them. A new device
is, therefore, necessary for designing experiments with a large number of
treatments. One such device is to take blocks of size less than the number
of treatments and have more than one block per replication. The treat¬
ments are then divided into as many groups as the number of blocks per
replication. The different groups of treatments are allotted to the blocks.

Example: We can take for 24 factorial two blocks each of eight units
and divide the 16 treatment combinations into two groups of eight each
for allotment to the two blocks.

In general, the block size for 2n factorials is of the form 2r. There are
many ways of grouping the treatments into as many groups as the number
of blocks per replication. We have already seen that for obtaining an
interaction contrast the treatment combinations are divided into two
groups. Two such groups representing a suitable interaction, say, P, can
be taken to form the contents of two blocks, each containing half the total
number of treatments.

In such cases the contrast of the interaction Pand the contrast between
the two block totals are given by the same function. They are, therefore,
mixed up with block effects and cannot be separated. In other words, the
interaction P, has been confounded with the blocks. Evidently, P has
been lost but the other interactions and main effects can now be estimated
with better precision because of reduced block size. This device of
reducing the block size by making one or more interaction contrasts
identical with block contrasts, is known as confounding. Though we have
introduced the concept of confounding by having only two blocks, the
number of blocks can be any power of 2 as we shall see subsequently.

Preferably, only higher order interactions, that is, interactions with
three or more factors are confounded, because their loss is immaterial.
As an experimenter is more interested in main effects and two factor
interactions, these should not be confounded as far as possible.

The designs for such confounded factorials can be called incomplete
randomized block designs. The treatment groups are first allotted at random
to the different blocks. The treatments allotted to a block are then
distributed at random to its different units.

Complete and Partial Confounding. When there are two or more
replications, a question arises whether the same interactions are confounded
in each replication or different sets of interactions are confounded in
different replications. Both the procedures are practised. If the same
set of interactions is confounded in all the replications, confounding is
called complete. If, again, different sets of interactions are confounded
in different replications, confounding is called partial. In complete

88

DESIGN AND ANALYSIS OF EXPERIMENTS

confounding all the confounded interactions are lost. But in partial
confounding, the confounded interactions can be recovered from those
replications in which they are not confounded.

Example: We can get the two groups of eight treatments each for 24
factorial from the solutions of the equations:

*1+*2+x3+xi=0"]

= 1J

Block  1

0  0  0  0

0  0  1  1

0  1  0  1

0  1  1  0

1  0  0  1

1  0  1  0

1  1  0  0

1  1

1

1

Block  2

0  0  0  1

0  0  1  0

0  1  0  0

0  1  1  1

1  0  0  0

1  0  1  1

1  1  0  1

1  1  1  0

The interaction ABCD is accordingly confounded here. If partial
confounding is desired wre can confound another interaction, say, ABC in
the second replication. The blocks are then obtained from the solutions
of the equations:

,a:o}

Block  1
0 0  0  0

0 1  1

1

1 1  0  0

1 0  1  0

1 6  1  1

1 1  0  1
1  0
0 1
0 0  0  1

Block  2
0  0  1  0

0  1  0  1

1  1  1  0
1  0  0  0

1  0  0  1

1

1  1

1

0  1  0  0

0  0  1

1

We notice that one of the two equations for getting the two block
contents is homogeneous. So, all linear conbinations of the solution vectors
of the homogeneous equation are also its solutions. By obtaining three
independent solutions, all the other solutions can be obtained from their

FACTORIAL EXPERIMENTS

89

linear combinations. In general, if the size of the block correspon¬
ding to a homogeneous equation is 2', its contents can be generated from
all possible linear combinations of r independent solutions of the equation.
Such a block is called the principal or key block.

Again, if (s,, s2,..., sm...sH) is a solution of the equation 2 ptXt=0,

n

i-i

then (j„ s2,..., 1,..., sn) is a solution of the equation

n

2 />,*, = 1

if Pm^O.

This property is exploited to get the second block from the contents
of the key block. That is, by increasing the mth element by 1 in all the
treatments in the key block, we get the other block.

This property has been used to get the second block when ABC is
confounded by increasing the third element in each combination in the
key block. The element in the fourth position could not be increased to get
the block as the coefficient of xt in its equation is zero.

3.7 Confounding in More than Two Blocks

Though for 24 factorial, two blocks per replication are reasonable, in
experiment with a larger number of factors, more blocks per replication
are required. The two groups obtained by confounding one interaction
are not enough here. More than one interaction are confounded in such
cases. The key block contents are obtained from the solutions of more
than one homogeneous equation simultaneously.

Example: We get the key block of size 23in 25 factorial from the solutions
of the equations:

Xj+Xj+Xg^O

*l+*4+*5 = 0

These equations indicate that ABC and ADE interactions are confounded
simultaneously in the same replication.

Now, any solution of the above two homogeneous equations is also a
solution of the equation which is obtained from a linear combination of
the equations. This shows that some more interaction is also confounded.
Adding the above equations we get

*2 + *3 + *4+*5 = 0

No other equation is possible from their linear combination. Hence, in
addition to interactions ABC and ADE, the interaction BCDE is also
confounded. This last interaction is called the generalized interaction of
the previous two independent interactions. The generalized interaction
BCDE can also be obtained from the product of the independent interactions

90

DESIGN AND ANALYSIS OF EXPERIMENTS

ABC and ADE by omitting all letters with even powers.

The key block has been obtained as shown below by first obtaining
three independent solutions of the homogeneous equations and then taking
all their linear combinations.

Key block

0 0 0 0 0

0 1111

10 10 1

10 110

110 10

110 0 1

0 0 0 1 1

0 110 0

There are three more blocks. These are obtained from the solutions of
the following three sets of equations. These equations have the same left
hand side, but the right hand side changes from equation to equation.
This ensures that the solutions of the three pairs of equations are non¬
overlapping. '

Sets of Equations

1

1

0

2

0

1

3

1

1

-^l+^2 + X3 —

Xl + X4+X5=

Let (jx, s2,..., ,s5) be any solution of the equations

*J+*2+*3=l

*l + *4 + *5 = 0

Then, by adding (su s2,..., j5) in turn to all the treatments in the key
block, we get the block corresponding to the above equations.

Similarly, the two blocks for the other two equations are obtained.
All the four blocks forming the full replication have been obtained as
above and are presented in Table 3.3.

FACTORIAL EXPERIMENTS

91

One Replicate of 2» Factorial, Confounding ABC, ADE and BCDE

TABLE 3.3

Key block Block 2 Block 3 Block A

0  0  0  0  0

0  1  I  1  1

1  0  1  0  I

1  0  1  1  0

1  1  0  1  0

1  1  0  0  1

0  0  0  1  1

0  1

1  0  0

0  0  1  0  0

0  1  0  1  1

1  0  0  0  1

1  0  0  1  0

1  1  1  1  0

1  1  1  0  1

0  0  1  1  1

0  1  0  0  0

0  0  0  0  J

0  1  1  1  0

1  0  1  0  0

J  0  1  1  1

1  1  0  1

1

1  1  0  0  0

0  0  0  1  0

0  1  1  0  1

1  0  0  0  0

1  1  1  1  1

0  0  1  0  1

0  0  1  1  0

0  1  0  1  0

0  1  0  0  1

1  0  0  1  1

1

1  1  0  0

We have seen that when there are four blocks in a replication, three
interactions are confounded, two of the which are independent and one
generalized. When there are 2k blocks in a replication, 2*-l interactions
are confounded of which k are independent and the remaining 2k—k— 1
are generalized. We can have enough control over the choice of indepen¬
dent interactions in so far as their order is concerned, but we can have very
little control on the generalized interactions which are consequential. This
fact creates difficulty in the construction of confounded factorials so as to
save all lower order interactions including main effects. Lots of trial and
error in the choice of independent interactions become necessary to get the
desired type of confounding.

For example, in 27 confounded factorial using blocks of size 23, there
are 2* blocks. So, 15 interactions are confounded of which four are
independent and 11 generalized. If we are to confound only three factor
and higher order interactions, it is very difficult to get a set of four
independent interactions each of two or more order such that all their
generalized interactions'are of the desired order. Das (1964) gave a method
of construction of confounded factorials. This method mostly eliminates
the trial and error procedure. We have presented this method in a general
way covering factors with different numbers of levels after discussing
experiments with factors at three levels each in Section 3.8.

3.8 Experiments with Factors at Three Levels Each

When factors are taken at three levels instead of two, the scope of the
experiment increases. It becomes more informative. Further, when the
levels of a factor are quantitative, the pattern of change of response with

92

DESIGN AND ANALYSIS OF EXPERIMENTS

the increase of the level values of the factor can be studied in a better way.
A study to investigate if the change is linear or quadratic is possible when
the factors are at three levels, though from this point of view the more
the number of levels the better. However, the number of levels of the
factors cannot be increased too much as the size of the experiment increases
too rapidly with them.

Let us begin with two factors A and B each at three levels. We shall
use 0, 1 and 2 as the level codes and treat them as the three elements of
mod. 3. In future, all mathematical treatments on these elements will be
in the finite field.

Taking one level from each factor we get the following treatment

combinations or simply treatments:

00, 01, 02, 10, 11, 12, 20, 21, 2±
A randomized block design can be adopted for the experiment. If there
are r replications, the analysis of variance partitioning for the design is as
given in Table 3.4.

TABLE 3.4

Analysis of Variance for 32 Factorial

Sources

Replication

Treatments

A

B

AB

Error

Total

d.f.

r—1

8

2

2

4

8 (r—1)

9 r—1

Since it is a factorial experiment, the treatment component has been
partitioned to have information on the main effect and interaction of the
two factors. These have been shown against A, B and AB having d.f. 2,2
and 4 respectively. The s. s. due to A is obtained by first grouping the
nine treatments into three groups. The first group contains all those
treatments in which A occurs at 0 level. The second and third groups
contain treatments having the level of A as 1 and 2 respectively. Evidently,
a comparison among these three group totals, gives comparison denoting
the main effect of A. As there are two independent contrasts among the
three group totals, the d. f. of the main effect of A is 2. The s. s. can be
obtained either from the total of the s. s. due to the two contrasts or from
the three group totals by the usual method of deviation squares. Let A0,
A1 and A2 denote the totals of the three groups of treatments obtained as

FACTORIAL EXPERIMENTS

93

described above. Then, the contrast

A2 A0

gives the linear contrast among the three levels of A if they are equispaced.
It indicates a linear relation between the response and level values of A.

The other contrast orthogonal to the above is

A2—2A1-}-A0

This contrast indicates a quadratic relation between the levels and their
responses. The main effect of B can also be treated similarly.

The interaction s. s. can be obtained by subtracting the s. s. due to A
and B from the treatment s. s. The meaning of two factor interaction when
factors are at three levels each is the same as in 2" factorial. That is,
when the effect of B is different at different levels of A, the factors are said
to have interaction.

The interaction can also be split into components of interactions between
the linear and quadratic effects of the two factors. Denoting the linear
and quadratic effects of A by AL and Aq respectively and similarly for B,
the four interaction components each with 1 d.f. can be written as

AlBl, AlBq, AqBl and AqBq.

They can be obtained from the following contrasts among the levels of the
two factors:

ALBL=(a2—a0) (b2—b0)

A lBq=(a2- a0) (b2- 26,+b0)

AqBl=(ci2—2a1+«o) (b2-b0)
AqBq=(a 2<3j-J-q0) (b2 26j-f-6o)

The letters a and b have been written with level codes to denote the
contrasts more clearly. The AlBl contrast is actually the contrast obtained
by multiplying algebraically (a2—a0) by (b2—b0), that is, a2b2—a2b0—a0b2+
a0b0. Similarly, the other contrasts are obtained. The estimate of the
contrast is obtained from the corresponding treatment totals.

Though this way of subdivision of the interaction effect is more
informative, such components cannot be used for the construction of 3"
factorials. For this purpose alternative types of components having some
sort of geometrical meaning, have been used. This procedure is described
below. Its development is due to Fisher, Yates and Bose.

Let us define, as earlier, one variate for each factor in a factorial such
that the ith variate xi denotes the levels of the z'th factor in the different
combinations of the factors. In the 3a factorial we have two variates xx
and x2 corresponding to A and B respectively.
Using the solutions of the equations:

94

DESIGN AND ANALYSIS OF EXPERIMENTS

we can divide the nine treatments into three non-overlapping groups of
three each. These three groups are the same as were obtained earlier for

finding the main effect of A.

Similarly, from the three groups of non-overlapping solutions of the

equations

x2=0

=2 J

we get the main effect of B.
We can write two more such sets of equations as below:

*1 + *2==0

=1 ■

=2 .

*2+2*2=0 '

= 1 •
=2 .
Each of these sets gives three groups of solutions—one coming from each
equation in a set. Comparison among these three groups represents a two
factor interaction component. Thus, there are two 2-factor interaction
components each having 2 d.f. These two interaction contrasts are
orthogonal between them and also to those of the two main effects.

The interaction component obtained from the equations

is denoted by AB.

The component corresponding to the equations

*2 + *2 I (/=0, 1, 2)

*2+2*2=/ (i—0, 1, 2)

is denoted by AB2, that is, the coefficient of *2 is the power of B. Evidently,
AB and A2B2 are the same. So also AB2 and A2B. Normally, these
components are written with the first letter having 1 as the power.

We can now write the 8 d.f. due to the treatments as below:

A 2

B 2

AB 2

AB2 2

Treatments 8

Components like AB, AB2 have great advantages for construction and

FACTORIAL EXPERIMENTS

95

analysis of these and other factorials, but they do not have any physical
meaning.

3.8.1 Factorials with Threb Factors each at Three Levels

\

When there are three factors we get on the same analogy the following
main effects and interaction components each having 2 d. f. The equations
from which they are obtainable are also shown beside them.

TABLE 3.5

Main Effect and Interaction Components of 33 Factorial

Effects

Corresponding equations

A

B

C

AB

AB2

AC

AC2

BC

BC2

ABC

ABC2

AB2C

AB2C2

*1=*' 0=0, 1, 2)

*2=»

*3=*'

*l+*2 = *

•*1 + 2*2=/

*l + *3 = *

*1 + 2*3=/

*2+*3=*

*2 + 2*3=/

*l + *2 + -*3 = I

*1+ *2 + 2*3 = /

*l + 2*2+ *3 = /

*1 + 2*2+ 2*3 = /

The 26 d.f. due to 27 treatments are divided into the above 13 components
each having 2 d.f. A group contrast for any of the components is ortho¬
gonal to the group contrasts of any other component. The equations
having t non-zero coefficients of the variates give the groups of an inter¬
action component of the corresponding t factors in the general case.

Evidently, a randomized block design is not suitable for a 33 factorial

We have, therefore, to resort to confounding. The number of blocks per
replication in 3" factorials is a power of 3. In the present case we have three
blocks. The contents of these blocks can be obtained from the three treat¬
ment groups obtained from any of the last four equations which represent
three factor interactions. Here also, confounding can be complete or partial.
If we take four replications, each time confounding a different three factor

95 DESIGN AND ANALYSIS OF EXPERIMENTS

interaction component, then confounding is called balanced. In the balanc¬
ed case, confounding is restricted to interactions of one or more orders,
such that each component of each order is confounded a constant number
of times and this constant number may differ from order to order of
interactions. The blocks corresponding to the confounding of ABC are

shown in Table 3.6.

TABLE 3.6

Blocks of the 33 Factorial

Key block

Block 2

Block 3

0 0 0

0 1 2

1 0 2

1 1 1

1 2 0

0 2 1

2 0 1

2 2 2

2 1 0

0 0 1

0 1 0

1 0 0

1 1 2

1 2 1

0 2 2

2 0 2

2 2 0

2 1 1

0 0 2

0 1 1

1 0 1

1 1 0

1 2 2

0 2 0

2 0 0

2 2 1

2 1 2

The second block has been obtained by adding a solution of x1+x2+x3=l
to each treatment in the key block. Similarly, the third block has been

•obtained.

3.8.2 Factorials with Four Factors each at Three Levels

When there are fpur factors we have to get nine blocks of nine plots each.
The 34 combinations have to be made into 32 groups. We have to use two
homogeneous equations simultaneously to get contents of the key block.

For example, we take the following two equations:

x1+x2-]-x8=0

+x4—0

This amounts to confounding ABC and AB2D. The solutions of these
equations give the key block contents. As these are homogeneous equa¬
tions any solution is also a solution of an equation obtained from their
linear combinations. Hence, two more interactions corresponding to the
following two resulting equations are also confounded:

FACTORIAL EXPERIMENTS

97

*1+2*3+2*4=0

*2 + 2*3+*4 = 0

Therefore, the interactions AC2D2 and BC2D are also confounded. These
two interactions are the generalized interactions. They can also be
obtained—one by multiplying ABC with ABZD and taking out the cubed
letters and another by multiplying ABC with (AB2D)a.

The other blocks are obtained from the solutions of the following eight

equations:

2

3

4

5

6

7

8

9

*l+*2 + *3=:  0

*1 + 2*j + *4 =

1

0

2

1

0

l

1

1

2

2

0

2

1

2

2

They can also be obtained from the key block by an exactly similar
procedure as described in 2" factorials. This method has, however, been
discussed in detail subsequently.

Here, again, by obtaining only two independent solutions of the
homogeneous equations, we can get the others from their linear
combinations.

In general, if in 3" factorial block size is 3r, the key block can be
obtained from the linear combinations of r independent solutions of n—r
homogeneous equations corresponding to confounded interactions. Again,
out of the (3n-r—1)/2 confounded interactions, (n—r) are independent
and $(3"-r—1)—(«—r) are generalized.

Following the above procedures the nine blocks obtained by confounding
the independent interactions, ABC and AB2D are shown in Table 3.7.
Here, also, a considerable amount of trial and error is required to obtain
a desired type of confounding. We have presented below, as stated earlier
also, a general technique of construction of confounded factorials which
eliminates considerably trial and error in the search of a desired type of
confounding.

3.9 A General Method of Construction of Confounded Factorials

Let there be n factors each at s levels where s=pm and p is a prime. The
total number of treatments in the factorial is sn. There are (i*— 1) d.f.
due to the treatments. These are divided into (sn—l)/(s— 1) main effect
and interaction components each of (s— 1) d.f. There are (s — l)*-1
components belonging to interaction among a given set of k factors.

The components can be represented by equations of the following

form:

98

DESIGN AND ANALYSIS OF EXPERIMENTS

o\
u
o
o
«

00

o o
s

h-

u
o
5

VO

o o
3

«/■>

o
O
3

Tf

rU
o
o
©

m Q
JD
3

CN

o
w
_o
S

o
5
>> 0)

fN

O

T-,

—H

_
o

pH

pH

CN

cn

ph

pH

CN

P*H

pH

o
CN

CN

T-H

cn

CN

CN

pH

o

tH

fS

pH

CN

pH

CN

T-H

o
o
H

T-H

CN

CN

cn

CN
o
o

pH

cn

O
o

cn

©
o

PH

T-H
o
o

o
CN
o
o

o  o
<N

pH

o
o

cn
o
o
o

pH
o

©
o

©

o

©

©

PH

CN

pH

pH

pH

pH

—
T-H

o

T-H

tH

T-H

T-H

CN

PH

O
©

CN

CN

O

CN

T-H

pH
o

CN

tH

o
o
o

CN

cn
o
o
CN

o
CN

O

CN

CN

cn

O

CN

t-H

O
o
CN

.

cn
o
cn

o
T-H
o
CN

cn

T-H
o

CN

P*

O

CN

T-H
o
CN
o

©
o

fS

©

pH

cn

CN

O

o

cn

cn
o

CN

O

cn

O

CN

cn

cn
o

T-H

T-H

CN

O

O

T-H

cn
o

CN

^H

CN

-©

CN

pH

CN

CN

-1

cn

CN

CN
o
cn

cn

T“H
o
CN

CN

O

t-H

CN

CN

o
o

cn

CN

CN

CN

CN

<N

T-H

CN

CN

CN

o

CN

CN

CN

cn

tH

cn

o
cn

pH

CnJ

T-H

tH

t-H

CN

O

T-H

T-H

cn

cn

cn

t-H

CN

CN

T-H

T-H

CN

O

T-H
fS

O

O

T-H

CN

CN

O

T-H

CN

T-H

©

t-H

o
tH

©

pH

T-H
o
o
T-H

o
o
o

CN

T-H
o
T-H

CN
o
o
T-H

T-H

CN
o
T-H

o

CN
o

t^H

CN

CN

O

pH

o

T-H
o

CN

*“

pH

O

o
o
T-H

©

©

©

tH

tH

T-H

©

©

tH

O

o
CN

tH

O

CN

CN

pH
©

TH

CN

T-H

O

FACTORIAL EXPERIMENTS

99

PiX1-\-ptx2+ ... +pnXn=i 0=0, 1, cc2, a3.. .<*,_,)

where plt p2,.. and a2, a3,..., ctj-j are the elements of the Galois
field, pm and xlt x2,..., x„ are the variates corresponding to the factors as
defined earlier.

Each choice of the pi s (not all zero) gives the equation of a component,
Once a set of p*’s has been selected, all its multiples are omitted as they do
not lead to any new grouping. A set of k non-zero pi s in the equation
lead to an interaction component of those k factors, the variates of which
occur with non-zero coefficients in the equation. If in an equation the
variate x{ has the non-zero coefficient pu then in the interaction corres¬
ponding to it, the corresponding factor At has the power pi. It can be
shown that the group contrasts for any interaction component is orthogonal
to the group contrasts of any other interaction.

In the confounded factorial sn let the block size be sr. There are sn~r
blocks. So (s',-r— 1) interaction components are confounded. In
the key block only r treatments are independent. The others can be
obtained from their linear combinations. Among the (sn~r— 1 )/(•*— 1)
confounded interactions (n—r)are independent and the rest are generalized.
The contents of the different blocks can be obtained from the solution of a set
of (/i—r) equations following from the independent confounded interactions.
The left hand side of these sets of equations is the same. Their right hand
sides are all possible combinations of n-r factors each at 5 levels—one
combination for each set. This method is due to Bose (1947).

To ensure a desired type of confounding is not very easy with the
above method. An alternative method due to Das (1964) simplifies the
problem and has been presented below. This method incorporates all the
basic principles of the above method but differs in procedure. In the
method of Bose the interactions for confounding are chosen first and the
block contents follow. In the method of Das the block contents are
choosen first and the interactions confounded follow therefrom.

When the block size is sr, we begin with the following r independent
treatment combinations of r factors each at 5 levels, written in the form of

an rxr identity matrix.

A} A2 A3. • •Ar

1 0 0...0

0 1 0...0

0 0 1...0

0 0 0...1

All the treatment combinations of the r factors can be generated from
the Unear combinations of these r treatments. Next, to accommodate
more factors we go on annexing further columns, one by one, to the nghfi

100

DESIGN AND ANALYSIS OF EXPERIMENTS

of the above matrix. Each such column corresponds to a subsequently
taken factor. They are denoted by Ar+1, Ar+2.. -A„. Let us now decide
the column below Ar+1. The columns evidently consist of the elements of
the field pm. As soon as a column below Ar+1 is written, the r combina¬
tions each of r-f 1 factors, become the r independent combinations of the
key block. Now, if the column consists of zeros only, all the elements
under the factor Ar+\ will be zero when the r independent combinations
are linearly combined to get the complete key block. Hence, in this case
the main effect of Ar+i is confounded. So to save main effects a column
consisting of zeros only should not be taken.

Next, let us take a column which is a multiple of one of the columns
already present. Here, multiplication is in the sense of multiplying a vector
by a scalar. Let xr+1, which denotes the variate for the factor Ar+\, be
times an already existing zth column which corresponds to the factor A/
and variate xt. Then Xr+i—piXi, that is,

Xr+i+(p— \)piXi=0.

This shows that a two factor interaction component involving the factors
Ar+1 and Ai is confounded. Hence, to save two factor interaction com¬
ponents no column should be taken any of whose multiples is already exist¬
ing. This is true not only for selecting the column below Ar+1, but any
subsequent column as well.

Similarly, to save three factor interactions no column should be taken
which is a linear combination of any two existing columns. This concept
extends for saving interaction of any order.

After a column below Ar+i has been chosen, another column below
Ar+2 >s chosen similarly. This procedure continues till the last column
required is chosen.

For each subsequent factor taken, an independent interaction is
confounded. Let the column taken below Ar+i be the vector (ax, a2,..., ar)'.
Denote the column vectors below the first r factors by xlf xa,..., xr.
These are unit vectors. Hence, ... +a,ocr=xr+1. That is,

. ..+ aLrxr + (p— 1) x,+i=0.

This equation gives the interaction confounded as a result of choosing
the column (al5 a2,.. .,ar), below A,+x. In symbol the interaction is
written as

A1*'A2«'...Ar«'Ar+l<p-»

When the power of a factor is zero, it goes out of the interaction. The
interaction confounded due to the choice of a column is independent of the
interaction corresponding to any previously chosen column, as everytime a
new column is taken, a fresh factor enters its interaction.

In this way by choosing (n—r) columns according to requirement, we
get the key block for the confounded factorial together with the independent

FACTORIAL EXPERIMENTS

101

interactions confounded. It is seen that it is very easy to choose columns
for saving upto two factor interactions which is mostly required.

The generalized interactions can be obtained from the possible linear
combinations of the chosen columns below Ar+i to A„ and then using the
resulting columns just like the chosen columns for writing the generalized
interactions. The heading of a thus derived column is not a single letter
but the product of those factors with appropriate powers whose columns
have been combined. If a particular column variate occurs with a coefficient
Pt in one of these column combinations, the factor for this column has the
power pt in the generalized interaction.

All these procedures have been illustrated by constructing 4* factorial
in 42 plot block saving all main effects and two factor interaction compo¬
nents.

Example: As the factors are each at four levels, we use as level codes the
four elements of the field 22:

0, 1, a, a8.

As the block size is 42 we start with the 2 x2 unit matrix shown in the
first two columns in Table 3.8. The last three columns are taken sub¬
sequently.

TABLE 3.8

Key Block of the 46 Factorial in 42 Plot Blocks

A\

a3

X\

*2

1

0

0

1

Az  Ai  ab
ft
Xi  xB

x3

1

1

<£

a2

1

1

Some derived columns for generalized interactions

*3 + X4

x3+ax4

*3 + *2X*

0

1

a2

a2

a

0

The last two rows of Table 3.8 give the two independent treatments
of the five factors in the key block. The interaction confounded due to

the column below A3 is

A1A2aA3

Similarly, the interactions confounded for the other two columns under

At and AB are . . .

A1AiaAl and A1A2A5.

The generalized interactions for the three derived columns shown in the

table are

A2A3A4, A*A*A3Ap

and Af-A3Af respectively.

The next 15 generalized interactions can be obtained from the other linear
combinations of the last three columns.

102

DESIGN AND ANALYSIS OF EXPERIMENTS

The entire block of 16 treatments is generated from the linear combi¬

nations of the two independent treatments in Table 3.8 as shown below.

A\  A2
0
0

1

0

1

1

1

0

1

1

a

a2

A9  A,

ab

0

1

a

a2

a

0

0

1

a2

a

0

a2

0

1

1

0

a2

a

The last three combinations are obtained from the first two, say, ax and a2
from ax -f pa2 by taking for p the values 1, a and a2 in turn. Another set of
five combinations is obtained by multiplying each of the last five treatments
by a and a third set of five, by a2. These give all the 16 treatments in the
key block.

The other blocks can be obtained by taking a treatment which has not
occurred in the key block and adding this treatment vector to each of the
treatments in the key block. To get the other blocks a similar operation
is done, each time taking a new treatment which has not occurred earlier
in any block. Sometimes it happens that a treatment which has already
occurred in some blocks is taken to get a block. This results in the
repetition of a block which is not always apparent as the treatments are
arranged in different order in the two blocks. This risk can be avoided
by following the method described below:

3.9.1 A Procedure to Avoid Block Repetition While
Generating Blocks from the Key Block

The independent confounded interactions are written in a column of a
two-way table. From each of these interactions we form a vector with the
powers of the factors ACs as elements. If any factor does not occur in an
interaction the corresponding element in its vector is zero. Such vectors
will be called confounding vectors. Let us denote these vectors as rows by
Cl, Ct, C8, etc.

We now take a treatment vector f which is to be added to each treat¬
ment in the key block to get another block. We shall call such vectors,
increment vectors. The other increment vectors will be denoted by /2,
/„ etc.

Next, each of Cx, C2, C3, etc. is multiplied by as vectors. The
products are entered in a column below f. We shall call such columns
derived columns. If this column consists of zeroes only, then the addition of
h to the key block treatments will generate the key block again. If the

FACTORIAL EXPERIMENTS

103

vector is something else, a new block is obtained. Again, another increment
vector /2 is taken and a derived column is obtained. If it does not contain
all zeroes or is not the same as the one obtained from Ix then its addition
will give another block. So, everytime to get a new block, the increment
vector has to be so chosen that a new derived column is obtained each
time. For getting sn~r— 1 blocks excluding the key block, we have to
obtain (n-r) independent derived columns from (n—r) increment vectors.
The rest of the increment vectors are their linear combinations. This
procedure has been illustrated in Table 3.9 obtaining some more blocks
of the 46 factorial in 42 plot blocks discussed earlier.

TABLE 3.9

Choice of Increment Vectors

Independent
confounded Confounding vectors Independent increment vectors
interactions

0 0 00 a  a 1 000  0 0 10 0  a 1 0 0»

AtA2*A3 1 a 1 0 0 (Ci) 0

Ax A2*' Ai 1 a2 0 1 0 (C2) 0

Ax A2 As 110 0 1 (C3) a

h

h

0

0

a2

h

0

1

0

h

0

1

1

The first three increment vectors are independent as their derived
columns are independent. The fourth vector is the sum of the first two.
All the 60 other increment vectors are obtained from the linear combinations
of the first three vectors:

0000 a, a 1 0 0 0, 00100

3.10 Maximum Number of Factors to Save Interactions
up to a Given Order for a Given Block Size

When block size is given it is of interest to ascertain—the maximum number
of factors that can be accommodated in the given block size so as to save
all interactions up to a given order. The known results in this regard can
be obtained in a straight forward way by applying the procedures of

Section 3.9.1.

Let the block size be sr. To obtain confounded interaction and the key
block we take an rxr unit matrix and annex a further column to it. In
order to save all main effects and two factor interactions we cannot take
any multiple of a column already taken, nor the null column. There are
in all sn—1 possible columns including the r columns in the unit matrix but

104

DESIGN AND ANALYSIS OF EXPERIMENTS

excluding the null column. If we take one of these columns, we are to
exclude all its (j—2) multiples to save two factor interactions. Thus, in a
group of s—1 columns which are multiples, only one column can be taken.
Hence, the maximum number of columns that can be taken including the
ones in the unit matrix is (sn— 1)/(j—1). Therefore, the maximum number
of factors each at s levels that can be accommodated in a block of size sr
without confounding any main effect and two factor interactions is
($"—l)/(.y— 1). This result was first obtained by Bose (1947) by following
a different method.

Example: When the block size is 23, we can accommodate seven factors
to save all main effects and two factor interactions. The independent
treatments in the key block are shown below:

A B C D E F G

10 0 110 1

0 10 10 11

0 0 10 111

This has been obtained by annexing four possible non-null columns to the
3x3 unit matrix under ABC.

In the example of 45 factorial in 42 plot blocks, discussed earlier, five is
the maximum number of factors for 42 plot blocks to save all main effects
and two factor interactions. Therefore, it is not possible to annex any
further column to the key block presented in Table 3.8.

3.10.1 Maximum Number of Factors Saving Three

Factor Interactions

When the factors are at two levels each and the block size is 2r, let us
choose columns containing only odd numbers of unity in all possible ways.
All these columns are distinct and the sum of any two cannot be another
of these columns, because the sum of two columns each containing an odd
number of unity, necessarily contains an even number of unity. So this
type of choice of columns saves three factor interactions also. The
maximum number of such columns is

rc1+rca+,'c#+ • • •

That is, the maximum number of factors each at two levels that can be
accommodated in a block of size 2r saving up to three factor interactions
is 2'-1.

Recently, Biyani (1973) in his unpublished thesis has shown that as
many as 5 • 2r-3 factors each at three levels can be accommodated in a block

FACTORIAL EXPERIMENTS

105

of size 3r when r > 3 without confounding any interactions up to three
factors. His method of choosing the columns consists of first taking for
block size 34a 4 x 4 unit matrix. Six columns are annexed to this matrix
by trial and error so as to save up to three factor interactions. Thus, we
get 10 columns corresponding to 10 factors which can be accommodated
m a block of size 34 saving up to three factor interactions. Such a block
has been given by Bose (1947) also.

Let us denote this 4x 10 matrix by A. We now write a 4x20 matrix
by putting A once again beside A. To get a fifth row we put the element
0 below each of the first 10 columns and 1 below each of the last ten
columns. The 5 x 20 matrix thus obtained, gives the 20 columns corres¬
ponding to 20 factors accommodated in a block of size 3® saving up to
three factor interactions. This process is repeated to get the columns for
38 from the column of 3s and so on.

3.11 Analysis of Factorial Experiments

The procedure of getting the sum of squares due to the main effects and
interaction components is straight-forward though laborious. For each
interaction the treatment groups are obtained from the solutions of its
equations. Then, from the treatment totals of the observations, these group
totals are obtained. The s.s. due to these totals is then obtained by the
deviation square method.

In case of complete confounding the s.s. of the completely confounded
interactions are not obtained. In case of partial confounding, the s.s. of
a partially confounded interaction is obtained by using the observation
totals from replications in which it is not confounded.

For 2" factorial there is a very convenient and compact method of
analysis due to Yates (1937). It consists of first writing the treatment
combinations in a column beginning with the control treatment (0 0.. .0)
and then introducing the factors one by one as shown in Table 3.10
in the case of 24 factorial. A factor is introduced by a row which
contains the element 1 in one position only and 0 in all other positions.
This row is then added to the previous rows to get new treatments. When
all the previous rows have been added another factor is introduced. The
observation totals of the treatments are entered in the second column.
These totals are then added two by two and entered in the third column.
This way half the third column is filled up. The difference between the
same two totals which have been added (second minus the first) is now
obtained and entered in order to fill the rest of the third column.
Thereafter, the fourth column is obtained from the third column in exactly
the same way as the third column is obtained from the second. As many
columns are obtained in this way as the number of factors. In the present
case four such columns are obtained. The entries in the last column give
the main effect and interaction contrasts. The first entry in this column is

106 DESIGN AND ANALYSIS OF EXPERIMENTS

the grand total of the observations. If the treatment in z'th position of the
first column is (a/i, a/2... a/4), then zth contrast belongs to the interaction,
Jan ga-ii C<XI» D*lt.

The s.s. due to an individual contrast is obtained by squaring a contrast
and dividing it by the total number of observations in the experiment. If
an interaction is confounded, its s.s. is ignored. If an interaction is
partially confounded, its contrast is also obtained from those replications
in which it is confounded and then this contrast is subtracted from its
corresponding contrast in the table. This adjusted contrast is then squared
and divided by the number of observations in the replications in which it

is not confounded.

TABLE 3.10

Analysis of Variance of 24 Factorial by Yates’ Algorithm

Treatments Totals

Col. 1 Col. 2 Col. 3 Col. 4 Col. 5 Col. 6

0 0 0 0

10 0 0

0 10 0

110 0

0 0 10

10 10

0 110

1110

0 0 0 1

10 0 1

0 10 1

110 1

0 0 1 J

10 11

0 111

1111

This technique can be applied in 3" series as well. Here also, the
treatments are written by introducing the factors one by one as shown for
32 factorial:

FACTORIAL EXPERIMENTS

107

A B

0 0

1 0

2 0

0 1

1 1

2 1

0 2

1 2

2 2

In the next column the treatment totals are written. The operations on
the total column are as follows:

(i) The totals are added three by three and one third of the next

column is filled up with these sums.

(ii) The first total in each of the above triplets is subtracted from the
third and another one third of the next column is filled up with
such differences.

(iii) In each of the above triplets twice the second total is subtracted
from the sum of the first and third totals. These differences fill up
the remaining one third of the next column.
This procedure is continued as many times as the number of
factors. The last column gives the contrasts of their interactions of
the linear and quadratic components of the factors. If the treatment
in /th position is, say, (an a/2 a/3) the contrast in zth position gives
the interaction component, AXil BxlJ Caf8. When any at is zero, the
corresponding factor goes out of the interaction. The value 1 or 2
of a/ indicates respectively the linear or quadratic component of A.
The same rule holds for B and C as well. The s.s. due to a
contrast is obtained by dividing the square of the contrast by a
suitable divisor. If ,in the treatment in column 1 against a contrast
there are p unity and a two, the division for the contrast is
(2p+6a) r where r is the number of observations in each total
entered in column 2.

3.12 Fractional Factorials

When there is a large number of factors even at two levels each, the total
number of treatment combinations becomes so large that it is very difficult
to organize an experiment involving these treatments. The demand on the
resources is so great that it may not, always, be possible for the experi-

108

DESIGN AND ANALYSIS OF EXPERIMENTS

menter to ‘provide them. In addition, non-experimental types of errors
may crop up while planning and conducting such a big experiment. For
example, the treatment labelling may be interchanged, the plot numbers
may be wrongly noted and similar other things may happen. Therefore,
it was proposed by Finney to resort to fractional replication in large
factorial experiments. If the experiment is not very large but it is difficult
to replicate it, we can take only one replication. In this case higher order
interactions are used as errors. The same advantage is exploited in
fractionally replicated experiments. The salient features of designs for
fractionally replicated experiments are given below:

1. The fraction of Sn is of the order 1 /sk. It is written as 1 jsk (sn).
2. The fraction consists of the key block of the confounded factorial s" in
blocks of size sn~k obtained by confounding (sk—l)/(s— 1) interactions.
3. These (Vc— l)/(s— 1) interactions are called defining contrasts. They are
written in a row beginning with the identity 7, and separated by the
equality sign.

4. As only one block obtained from the defining contrasts is taken,

these contrasts are not estimable.

5. Any main effect or interaction is said to be in alias with all its
generalised interactions with the defining contrasts. The interaction
in question together with all its aliases are written in a row separated
by equality sign.

The solutions of the following k homogeneous equations corresponding

to k independent interactions in the defining contrasts, give the fraction.

Pnxi+Pizx2+ ■. • +Pi„*n=0

P2lXl'^~Pi2X2~^~ • • • fiPlnXn= 0

To obtain any interaction which has the equation

PkiX1-\~Pk2X2Jr . ■ . -rPknXn—0

PmiX1-rPm2X2+.. .-\-pmnx„=i(i— 0, 1, a2, a3,. .

we get the s groups from the solutions of the following s sets of equations.

P\\XlJrP\2X2JC • • • +7’lnXn = 0

Pkix1+pk2X2+... +pknX„=0

Pm\X^ -\-pm2X2~\- • • .-f•PmnXn — i (/— 0, 1, a2, a3, . .

Any contrast between these groups is not only a contrast for the inter-
action/>mlx1-Fpff,2^2+... •3rpmnXn—i but also for all interactions corres¬
ponding to equations which are obtained from its linear combinations
with the rest of the equations in the above set and their combinations. All
these interactions form the aliases of 2 pmjXj=i. This shows that all the

FACTORIAL EXPERIMENTS

109

interactions in an alias group are confounded among themselves. So, to
get information on main effects and two factor interactions, their alias
should contain interactions with three or more factors. In such a case the
variation due to the alias group can be considered to be due to the main
effector two factor interaction as the other interactions in the group are
of the order of error being of higher orders. This type of alias groups is
possible only if the defining contrasts do not include any interaction with
less than five factors. This serves as a criterion for selecting appropriate
defining contrasts. All those alias groups which contain interactions with
three or more factors only are used to provide error variance.

In these experiments also, confounding is necessary to reduce block
size. Preferably, alias groups containing higher order interactions alone
are confounded. The procedure of blocking is similar to that in the case
of fully replicated designs but taking care of the fact that all blocks con¬
taining treatments not in the fraction are omitted. We have explained the
blocking and other procedures with two examples: £ (27) and 1/3 (36).

Example 1: \ (27) in blocks of 23 units.

Denoting the seven factors by A, B, C, D, E, Fand G we take the

defining contrast: 1—ABCDEFG.

Any other non-symmetrical defining contrast makes the searching of

interactions in the alias groups difficult.

The fraction is obtained from the solutions of the equation

*i+*2+*3++x5+x6+x7=0
The main effect of A is obtained from the difference between two group
totals, the groups being obtained from the solutions of the following two
sets of simultaneous equations:

*1 + *2 + X» + *4 + X 5 + *8 "I" *7 = 01
*1 = 0 J
*i+Xt4-.x3+.x4+.X 5+.x8+x7=01
*i=l)

It is seen that any solution of the first set of equations is also a solution

of their linear combination which gives

Similarly, any solution of the second set of equations is a solution of

x% "P *3+*4+x6 -f-x6+x7=0

*2 + *,-f*4 + *5 + X, + X7 = l

Hence, the interaction B CDEFG is in alias with A. Similarly, the
interaction CD EFG is in alias with AB. Any three factor interaction is
in alias with interactions with four factors. So, these can be used for
obtaining error variance.

We get the blocks in the following manner by using the same general

method described earlier.

110

DESIGN AND ANALYSIS OF EXPERIMENTS

As the block size is 23, we begin with the 3x3 unit matrix.

A B C D E F G

10 0 1 1 0 1

0 10 10 11

0 0 10 1 11

We have chosen threfe columns under D, E and F so as not to confound
any main effect and two factor interactions. The column under the last
factor G is so chosen that the block remains within the fraction. This is
ensured by having in each row an even number of unity against the factors
which appear in the defining contrast. If there be more than one
independent interaction among the defining contrasts, the above requirement
should hold for each of the independent interactions.

We see that there is no freedom for the choice of the column under G.
As a result it may happen to be the same as one of the columns already
taken. In such cases some trial and error is necessary while choosing the
columns for confounding.

The interactions confounded are obtained exactly in the same way
described earlier by using the columns under D, E and F. They are A BD,
ACE and B C F together with their generalized interactions and aliases.

The other blocks can be obtained by using the same procedure as
discussed in 3.9.1 earlier—excepting that (I) more confounding vectors
corresponding to the independent interactions in the defining contrasts
are taken together with the confounding vectors and (II) the product of
every increment vector with each of these additional confounding vectors
should be zero.

A choice of three independent increment vectors in the present example

is shown in Table 3.11.

Choice of Increment Vectors in £ (27) with 23 Units per Block

TABLE 3.11

Confounded
interactions
with the
defining contrast

Confounding
vectors

Increment vectors

0000011  0000101

0 0 0  10 0 1

ABD

ACE

BCF

1101000

1010100

0110010

ABCDEFG

1111111

0

0

1

0

0

1

0

0

1

0

0

0

FACTORIAL EXPERIMENTS

111

The rest of the increment vectors are obtained from the linear combinations

of the above vectors.

The full partitioning of the degrees of freedom for the analysis of the

design is shown below.

TABLE 3.12

Partitioning of d.f. for \ (2?) Factorial

Sources

Main effects

(Aliases: 6factor interactions)

Two factor interactions

(Aliases: 5 factor interactions)

Three factor interactions

(Aliases: 4 factor interactions)

d.f.

7

21

35

63

Seven of the above 35 interactions are confounded.

Example 2: 1/3 38 in 33 plot blocks.
We take the defining contrast

I=A BCDEF

It helps greatly to take a defining contrast which is symmetrical with
respect to the powers of the letters in it. A defining contrast of the form
ABCDE*Fcomplicates the whole problem. The fraction is obtained
from the solutions of 2 x,=0. The alias groups of some of the typical

main effects and interactions are shown below:

A=A* BCDEF=BCDEF

A B=A% B2 CD EF—C D EF

A B*=A* CD EF=B2 CDEF

ABC=A%B2 C2 DE F=D E F

A B C*=A2 B2 D EF= C2 D EF

ABC2 D*=A*BiEF=C2DtEF

These have been called typical because all types of interactions have

atmeared in the above set. In two factor interactions there are two types,
\iz^AB and AB2. In AB no letter is squared while in AB one letter is

^rthree factor interactions, there are two types: ABC and A B C*.

112

DESIGN AND ANALYSIS OF EXPERIMENTS

The type with two squared letters does not arise because it is the square
of the second type above.

Similarly, for four and five letter interactions there are three types
each. For six factors there are four types. It is seen that the aliases of
four factor interactions with two squared letters are interactions of the
same type. Hence, confounding should be limited to them as far as possible-
The key block is obtained below by beginning with a 3 x3 unit matrix:

ABC

1 0 0

0 1 0

0 0 1

D E F

1 1 0

1 2 2

2 1 2

The columns under D and E have been used for confounding and that
under F for keeping the block within the fraction. The element 2 has to
be taken once in each of the columns under D and E to get four factor
interactions with two squared letters.

The interactions confounded are shown below:

ABC2 D2—A2B2 EF—C2D2EF

A B2 C E2=A2 C2 D F=B2 D E2 F

B2 C D2 E=A C2 E2 F—A B2 D2 F

A D E=A2 BCD2 E2F=B CF

The other blocks can be obtained from the key block by increasing the
key block treatments with the following increment vectors.

Confounded
interactions and
defining contrasts

Confounding
vectors

Independent
increment vectors

ABC2 D2

AB2C E2

ABCDEF

1 1 2 2 0 0

121020

111111

0

2

0

000012

000102
2

0

0

The break up of the total d.f. of the interactions is shown below:

Main Effects

(Aliases: *6! and 50)

Two factor, AB type

(Aliases: 62 and 40)

Two factor, AB2 type

d.f.

12

30

30

• 6i means one letter in a six factor interaction is squared and similarly for others.

FACTORIAL EXPERIMENTS

113

(Aliases: 5X and 5J

Three factor, ABC type

(Aliases: 6, and 30)

Three factor, ABC2 type

(Aliases: 52 and 4j)

Four factor, A B C2 D2 type

(Aliases: 42 and 4S)

20

120

30

242

There are 40 d.f. due to all the interactions of type ABC, as there are
20 such combinations of three letters out of six. But since in the same alias
group there are two interactions of the same type, we get only ten such
alias groups. So, the total d.f. of the type is 20. Two of these d.f. are
confounded.

Given a set of four letters, say, ABCD, there are three components

each having two square letters. These are:

ABC2 D2

A B2 CD2

ABAC2 D

Hence, for q. given set of letters, there are six d.f. due to the interactions
of 42 type, that is, the type of four factor interactions with two squared
letters. As the total number of such combinations is 15, the total d.f. of
this type of interactions is 90. But since each of their aliases contains
interactions of the same typet the total d.f. of the type becomes 30. Six
of them are confounded.

3.12.1 Analysis of Fractional Factorials

The analysis of fractional factorial is similar to the analysis of full factorials.
The treatment groups for each main effect or interaction are found by
solving appropriate sets of equations and then the s.s. is obtained from
the observation totals of these treatment groups by the usual method.

For 2" factorials, the fractionally replicated designs can also be
analyzed by applying Yates’ algorithm. The only difference is that while
writing the treatments, levels of k factors have to be ignored in the case
of 1/2* fraction. These k factors are so chosen that as a result of their
suppression no treatment combination of the remaining n-k factors
should have zeroes only, excepting, of course, the control treatment. The
other n—k factors are introduced one by one while writing the treatments,
as in full replication. Here, n-k columns will be generated by following
the same method as described in full factorial. An interaction corresponding
to a contrast is also found similarly by considering only the (n — k) factors.

114

DESIGN AND ANALYSIS OF EXPERIMENTS

The rest of the interaction which will contain the ignored factors also will
form aliases of the above interactions.

The fractions of 3" factorial can also be analyzed on the same analogy.
Here, also, while writing the treatments, factors are suppressed first and
then they are written by introducing the factors one by one as described
in full factorial. The operations and the correspondence of contrasts and
interactions are also similar when the non-suppressed factors alone are
considered. It is, however, not possible to write the aliases of such
interaction components, But this does not create any serious problem.
The linear and quadratic contrasts for a suppressed factor, L, come from
contrasts involving those factors with which L is in alias.

EXERCISES

1. Show that the total number of solutions of the following k equations is s”-fc

for every choice of (ax, a2- • •**):

TllXl +Pl$-2T ■ • ■ +/7l»Xn = al

/72lXl+/?22Xg+ • • • +/>2nXn = «2

PklX-1 +-Pfc2Xj+ ■ • • +PknXn = <*k

where the coefficients ptfs, a,- (1, 2,..., k) and the solutions are in the field S,
where S=pm and p, a prime.
Hints: Fix {n—k) of the x<’s by giving them any set of values. Then solve
for the other k > x»’s. This gives one solution. As the {n—k) x,-’s can be fixed
in sn~k ways, there are as many solutions.

2. Show that in the Sn factorial the treatment groups corresponding to any
interaction contain an equal number of treatments from each of the groups
of any other interaction and hence show that the contrasts for the two
interactions are orthogonal.

3. Find the confounded interactions separately for five replications of the factorial
25 in 23 plot blocks such that confounding is balanced for the second and
third order interactions.
Hints: Take a 3 x 3 unit matrix. Annex two columns to it by choosing two
consecutive columns from the following four in all possible ways:

110 1

10 11

0 111

The choices being Cx and C2 for the first replicate, C2 and C3 for the second,
C3 and C4 for the third and C4 and Cx for the fourth, the fifth replicate is
obtained from the three remaining interactions.

4. Given that the following three independent interactions ABCD, BEFK and
ABGK are confounded in 2® factorial having blocks of 26 plots, find the
independent treatments in the key block by applying the general method
discussed in the text.
Hints: Find three letters each occurring in a different confounded interaction
but no two or more of which occur together in any interaction. These can be

FACTORIAL EXPERIMENTS

115

C, F and G. Write all the letters in a row and then write five columns of the
5x5 unit matrix below the five letters other than C, Fand G. Put below C a
column which confounds A BCD. Similarly, put below F a column which
confounds BEFK and so on.

5. Given the following key block of 28 plot factorial in 28 blocks find the inter¬

actions confounded:

A

B C D E F G

K

1

1

0

1

0

0

0

1

1

1

110 110

1 0 0 0 0 1

11110 0

0 0 10 10

0

10 10 11

1

0 10 111

0

0

0 1110 1

0 0 0 0 0 0

Hint: Choose three rows from the above eight rows such that three columns
of these rows give three different columns of the 3x3 unit matrix. Then, with
the help of the remaining columns find the interactions confounded.

6. Find the confounded interactions separately for four replications of 34 factorial
in 32 plot blocks so that confounding is balanced for three factor interactions.
Hints: Take a 3x3 unit matrix. Annex two columns taken consecutively from
the following four columns:

The last pair of columns is

112 2

12 2 1

2 1

1 1

7 Write the independent treatments in the key block of size 33 of 313 factorial
such that no main effect and two factor interactions are confounded. Obtain
the independent interactions confounded.

8. Describe the method of analysis of 4» factorials by applying Yates’ algorithm.
9 . If the fraction 1/23 (2») is obtained from the confounding as shown in problem 4
and if the key block in problem 5 is the key block of the fraction, obtain the
three alias groups of interactions for the three confounded interactions.

10 Show that it is not possible to construct the half fraction of 2® factorial using

blocks of 23 plots and saving all main effects and two factor interactions.

11 The following table gives data relating to yields of dry herbage (cwt/acre) from
an experiment on grazed grass. Three fertilizers nitrogen at three levels,
phosphorus at two levels and potassium at two levels were used. Yields are

given for three years 1958-1960.

116

DESIGN AND ANALYSIS OF EXPERIMENTS

Years

N

P K

0

0

0

0

1

1

1

1

2

2

2

2

0

0

1

1

0

0

1

1

0

0

1

1

0

1

0

1

0

1

0

1

0

1

0

1

a

1958

1959

1960

54.2

75.9

65.2

68.4

81.8

110.4

98.7

107.9

81.5

102.9

105.7

125.9

48.9

74.8

63.1

65.6

83.8

108.7

94.9

105.3

79.8

110.4

115.2

123.9

60.3

80.4

65.2

70.1

89.4

112.7

97.8

102.9

89.2

108.4

112.7

119.6

Analyze the data, assuming all factors to be fixed and give your comments.
12 The table below gives the yields and the layout of a 25 factorial experiment on
beans conducted in Rothamsted in 1935. A single replication in four blocks of
eight plots each was used. The five factors and their levels were as follows:
(s) spacing of rows at 18 inch or 24 inch
(d) dung at none or 10 tons per acre
(n) nitrochalk at none or 0.4 cwt N per acre
(p) super phosphate none or 0.6 cwt P205 per acre
(k) muriate of potash at none or 1.0 cwt KgO per acre
As usual, absence of a symbol denotes the lower level of the corresponding,
factor and (1) denotes the treatment with all the factors at the lower level.
Analyze the data, using higher-order interactions as error.

Yields and layout of a 25 experiment in blocks of eight plots

Block I

' s

snk

np

dn

36.2
60.5
36.3
67.3

sdp

dk

sdnpk

pk

49.8
51.3
61.3
49.6

Block III

nk

snp

dp

71.2
45.7
76.7

(1)
sdrt

spk

66.5
70.5
74.3

sdk

73.3

dnpk

77.0

n

sdnk

sp
sd

Block II

68.0
92.5
29.9
54.7

k

dpk

dnp

snpk

Block IV

p
sdnp

d

dnk

56.7
64.6
74.8

73.7

npk

sn

sk

sdpk

63.6
63.6
60.8
47.9

48.0
23.3
39.3
56.3

Source: Rothamsted Experimental Station, Imperial Bureau of Soil Science,
1935.

FACTORIAL EXPERIMENTS

117

13. Th© following table gives the plan and the yields of a 23 experiment involving

three factors N, P, K, in block size of four plots each.
Analyze the data and give your comments.

Plan and yields of a 23 experiment in blocks of four plots.

Replication

Treatment

Yield

Blocks

Treatment

Yield

1

2

3

I

pk

pk

np

1

k

npk

np

P

npk

I

nk

1

2

3

4

5

6

54

90

188

136

122

65

145

88

68

73

70

103

k

P

n

npk

P

nk

pk

n

n

k

pk

np

98

182

65

201

156

210

143

187

109

93

142

154

14. A 33 experiment was conducted to study the effects of the three factors (each at
three levels 0,1, 2): sowing date (d), spacing of rows (s) and sulphate of ammonia (n)
on sugar beets. Two replications each consisting of three blocks of nine plots each
were used. The table below shows the plan and the percentage of sugar. Analyze
the data and write a report!

Plan and percent sugar of a 33 experiment of blocks of nine plots.

Replication! Treatment % sugar Replication 2 Treatment % sugar

d

s  n

0

1  2

2  0  2

0  0

1

2

i  0

0  2  0

1  2  2

1

1

1

1  0  0

2  2

1

14.07

15.06

16.00

15.07

16.05

17.96

17.50

18.65

16.63

Block I

d  s  n

1  2

1

1  0  0

1

1

2

0  0  2

2

0

1  0

1

1

0  2  0

1

2

2  0

2

1

19.67

18.68

16.93

18.16

18.86

15.63

16.12

19.36

16.39

Block I

118

DESIGN AND ANALYSIS OF EXPERIMENTS

2  0

1

0  0  0

15.63

17.69

0

1

1

17. 50

Block II

0  2  2

1  0  2

2  2  0

2

1

2

1

1

1  0

2

1

2  2  2

2  0  0

Block III

2

0

1

1  0

1

1

1

1  0

1  2

1  2  0

0  0  2

0  2

,1

Block II

Block III

19.58

17.69

15.66

15.69

16.26

14.64

16.59

15.96

16.74

19.66

16.39

16.38

15.66

18.56

17.06

2

1

1

2  0  2

1  2  2

0

1

2

2  2  0

0  2

1

0  0  0

1  0

1

1

1  0

1  0  2

2

1

2

2  0  0

1

1

0  2

1

2

0

1  0

1  2  0

2  2

0  0

1

1

14 63

16.24

16.39

16 54

17.80

16.63

16.74

16.69

14.64

14.66

16 24

16.72

16.40

16.65

16.63

17.30

16.86

16.72

15. Obtain the layout of a design for a 25 factorial in a 4x8 rectangle, confounding

ABD, ACE, BCDE with rows and AD, CE, ABD with columns.

16. Obtain the partially .confounded design for a 33 factorial with four replicates, each
in three blocks of nine plots each. Confound ABC with blocks in the first repli¬
cate, ABC2 in the second, AB2C in the third, and AB?C2 in the fourth.

REFERENCES

1. Biyani, S.H. (1973). “Maximum number of factors saving up three factor inter¬

action”. Unpublished thesis submitted to I.A.R.S., New Delhi.

2. Bose, R.C. (1947). “Mathematical theory of symmetrical factorial design.”

Sankhya, 8.

3. Carmichael, R.D. (1937). Introduction to Theory of Groups of Finite Order.

Ginn, Boston.

4. Cochran, W.G. and Cox, G.M. (1957). Experimental Designs, Wiley, New York.
5. Das, M.N. (1964). “A somewhat alternative approach for construction of
symmetrical designs and obtaining maximum number of factors.” Cal. Stat. Assoc.
Bull. 13.

6. Finney D.J. (1945). “The fractional replication of factorial arrangements.”

Ann. Eugen. 12.

7. Fisher, R.A. (1947). The Design of Experiments. 4th Ed., Oliver and Boyd.

8.

Edinburgh.
Kshirsagar, A.M. (1966). “Balanced factorial designs”. J.R.S.S. (B), 28,
ppi 559-67.

FACTORIAL EXPERIMENTS

119

9. Kurkjian, B. and Zelen, M. (1962). “A calculus of factorial arrangements.”

Ann. Math. Stat. 33, pp. 600-19.

10. Raghavarao, D. (1971). Constructions and Combinatorial Problems in Design of

Experiments, Wiley, New York.

11. Shah, B.V. (1960). “Balanced factorial experiments.” Ann. Math. Stat. 31,

pp. 502-14.

12. Shah, B.y. (1958). “On balancing in factorial experiments.” Ann. Math. Stat.

29. pp. 766-79.

13. Yates, F. (1937). “The design and analysis of factorial experiment.” Imp. Bui.

Soil, Sci.

CHAPTER 4

Asymmetrical Factorial and
Split-Plot Designs

4.1 Asymmetrical Factorial Designs

It has been mentioned earlier that factorial experiments are of two types,
symmetrical and asymmetrical. In symmetrical factorial experiments the
factors occur at the same number of levels. The designs for these
experiments have been discussed in Chapter 3. In asymmetrical factorial
experiments all the factors are not at the same number of levels. The designs
for such experiments are discussed in this chapter. The designs for asym¬
metrical factorial experiments will also be called asymmetrical factorials.

Symmetrical factorial experiments are somewhat inflexible because all
the factors have to be at the same number of levels. This may be in
conflict with the requirements of the experimenter. It may even be
unrealistic in some situations to take all the factors under investigation at
the same number of levels.

The above drawbacks can be removed by adopting asymmetrical factorials
as they accommodate factors with different numbers of levels. These designs
are, therefore, more flexible to meet the requirements of the experimenters.
Construction of confounded asymmetrical factorials and their analysis
are, however, somewhat complicated. As a matter of fact very little was
known about their construction through any systematic method till Kishen
and Srivastava (1959) and Das (1960) gave two convenient methods of their
construction. The previous works on asymmetrical factorials were due to
Yates (1937) and Li (1944) who gave several confounded designs which
were obtained individually rather than devising general methods for such
constructions.

Of the two methods given by Kishen and Srivastava (1959) and Das
(1960) it appears that the method of Das is more general, in the sense that
by using this method many more designs are obtainable than by the method
of Kishen and Srivastava. This is so because for the construction of designs
of the form in siXsk plot blocks, the method of Kishen and
Srivastava requires that ^ < 5, while the method of Das is not subjected
to any such restriction.

4.2 Confounded Asymmetrical Factorials

The simplest of the asymmetrical factorial experiments is the one with two

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

121

factors, say, A and B where A is at two Tevels and B is at three levels. This
is denoted by 2 x 3 factorial. Denoting the levels of A by a0 and ax and
those of B by b0, b1 and b2, the six treatments combinations of the factorial
are

^0^2’ ^1^1* ^1^2”

As the number of treatment combinations is not large, the randomized
block design can be adopted for this experiment. The data can be analyzed
as appropriate for the randomized block design with the partitioning of
treatment sum of squares into components which give the sums of squares
due to the main effects and the interaction of the factors.

Let there be r replications in the design. Accordingly, we get the

following partitioning of the total degrees of freedom.

Partitioning of the Total d.f. in the Analysis of Variance of 2x3 Factorial

TABLE 4.1

Source

Block

Treatments

A

B

AB

Error

d.f.

r— 1

5

1

2

2

5 (r—1)

The sums of squares due to blocks, treatments and error can be obtained
exactly in the same way as in the analysis of randomized block designs.
The sums of squares due to the main effects A and B and their interaction
AB can be obtained by forming the following table with six treatment
totals, Tij, i=0, 1,7=0, 1, 2.

TABLE 4.2

Table of Treatment Totals of the 2 x 3 Factorial

Levels of B

Levels of A

oo

*i

Total

bo

bi

b2

Too

Tor

T02

Tio

Tii

T12

Bo

B1

b2

Total

Ag

A\

G

122

DESIGN AND ANALYSIS OF EXPERIMENTS

Sum of squares due to A =

A*'+A*_G*
3 r 6 r

Sum of squares due to B=-

Sum of squares due to the cells=

2 r 6 r
r2 00+ n,+n,+r210+ r2n+r2lt_ g*
6r'

r

Sum of squares due to

AB—{s.s. due to cells)—(s.s. due to /4)—(s.s. due to 5)

When there are three factors at the lowest possible numbers of levels,
viz., 3, 2 and 2, they generate 12 treatment combinations. In such
situations a randomized block design or a latin square design may not
always be suitable. It is, therefore, necessary to adopt confounding for
reducing the block size.

Normally, the block size in confounded asymmetrical factorials is a
factor of the total number of treatment combinations in the experiment.
This makes the design resolvable. A design is said to be resolvable when
it is possible to divide all its blocks into several groups such that each
group represents a full replication of all the treatments. Resolvability,
however, does not seem to serve any useful purpose in our case.

Confounding of effects in asymmetrical factorials is somewhat different
from what we have seen in symmetrical factorials. When an interaction is
confounded in a replication in these designs, it is not necessary that it is
completely confounded with the blocks in the sense that the block contrasts
and the interaction contrasts become identical. Though these two sets of
contrasts are not identical, they are dependent so that the usual contrasts
for obtaining a confounded interaction from the treatment totals is not
free from block effects. It is, therefore, necessary to take more than one
replication in confounded asymmetrical factorials so as to make the design
balanced, in the sense that, (i) any contrast of a confounded interaction is
estimable independently of any other contrast belonging to any other
confounded interaction and (ii) the loss of information of each degree of
freedom of any confounded interaction is the same. The difficulty of
construction of confounded asymmetrical factorials is mainly due to
achieving such a balance. We have discussed below a method of cons¬
truction of balanced confounded designs by linking them with the fractions
of suitable symmetrical factorials. This method is due to Das (1960).

4.3 Construction of Balanced Confounded Asymmetrical Factorials

Let P=p1pi.. ,pt be the total number of treatment combinations in an
asymmetrical factorial involving t factors such that the ith factor Ft is at
pt levels (i=l, 2,...,/) and allpfs are not equal. Let JR be the block size.
For the present method of construction it is required that PjR—N, say, is

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

123

either a prime or a prime power. Let N—sk where s is a prime number
and k any integer.

Each of the above factors whose number of levels is .y, is called a real
factor and each of the other factors is called a factor of asymmetry. Our
technique of construction consists of converting the asymmetrical factorial
to a suitable fraction of a corresponding symmetrical factorial by denoting
the levels of each factor of asymmetry by the combinations of a requisite
number of factors each at 5 levels. These latter factors are called pseudo
factors corresponding to the factors of asymmetry. The levels of each real
and pseudo factors are denoted by the elements of Galois field j. The
number of pseudo factors corresponding to a factor of asymmetry is
determined as below.

Ifp/, the number of levels ith factors, Ft, is less than s, then any pi of
the s elements of Galois field of s are used to denote the levels of Ft. If
s 1 ^ Pi ^ *s",» then any set of pt combinations of the sn‘ factorial is used
to denote the levels of Ft and the remaining s"1—pt combinations are
omitted. The factors each at s levels are called the pseudo factors corres¬
ponding to Ft. This type of level designation is made for each asymmetry
factor.

When all the treatment combinations are written using such level

designations, the design becomes a fraction of sM where

M= t0-)-2 tit

i

/0=number of real factors

and 2 m=number of pseudo factors corresponding to all the factors

of asymmetry.

The size of the fraction is evidently P/sM. This need not be a regular

fraction of the type 1 /sk which we have discussed in Chapter 3.

Example 1: In the asymmetrical factorial 2x2x3 with block size 4, we
have s=3. So each of the factors at two levels which we shall denote by
X and Y are the factors of asymmetry. The factor at three levels is the
real factor which we denote by A. In future all real factors will be denoted
by A, B, C, etc. and all factors of asymmetry by X, Y, etc. The pseudo
factors corresponding to X will be denoted by Xlt X2, etc., and those
corresponding to Y by Yx, Y2, etc.

The corresponding symmetrical factorial is therefore, 33 involving the
factors Xlt Yx and A. The fraction is obtained by omitting the level 2 of
each of Xx and Yx and then writing all the 12 possible combinations.

Example 2: If in the same factorial 2x2x3, the block size is 6, then
s=2. So, the two factors each at two levels are the two real factors and
are denoted by A and B. The other factor at three levels is the factor of
asymmetry, denoted by X. Since 3 lies between 2 and 22, we have to

124

DESIGN AND ANALYSIS OF EXPERIMENTS

take two pseudo factors X1 and X2 corresponding to X. Any three of the
four combinations of the pseudo factors Xy and X2 are used for designating
the levels of X. The corresponding symmetrical factorial is then 2*. The
fraction is obtained by writing all the 12 combinations of the four factors
such that the combination, say, 11, of X, and X2 does not occur.

We know that the number of blocks per replication in the asymmetrical
factorial is sk. The corresponding symmetrical factorial is, therefore, to be
split into sk blocks by confounding a suitable set of interactions. While
writing the block contents, the treatment combinations, which contain those
combinations of the pseudo factors which are not used for designation of
levels of factors of asymmetry, are not to be written. In choosing
interactions for confounding, care should be taken so that interactions
involving only pseudo factors are not confounded as this will lead to
confounding of main effects of the corresponding factors of asymmetry.
Similarly, if an interaction involving only real factors is confounded, it
will be confounded completely as in symmetrical factorials. After one
replication is obtained as above, the other'replications are chosen suitably
so as to achieve the balance. A method of choosing such replications

has been discussed below.

Correspondence and Interactions

When an interaction, say, 7* of the corresponding symmetrical factorial
$m obtained earlier is confounded it leads to the confounding of some
interaction, say, I a of the asymmetrical factorial and we say that the
interaction I a corresponds to the interaction Is. When Is does not contain
any pseudo factors, Is and Ia are evidently identical. When Is, contains
one or more pseudo factors corresponding to one factor of asymmetry,
say X, then the corresponding interaction IA is obtained from I, by
replacing the set of pseudo factors in it by X. The real factors in Is
remain as they are. If Is contains pseudo factors corresponding to two
factors of asymmetry, say, X and Y, then I a is obtained from Is by
replacing the set of pseudo factors corresponding to X by X and the other
set by Y. A similar procedure is followed to obtain I a from 7, when there
are pseudo factors in I, corresponding to more than two factors of
asymmetry.

It is easily seen that more than one interaction Is of the symmetrical

factorial can correspond to the same interaction I a.

Example 3: In Example 2 above each of the interactions XxAB, X2AB
and XxX2AB corresponds to the interaction XAB.

Balancing the Design

When an interaction of the symmetrical factorial is confounded, it leads

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

125

to the confounding of its corresponding interactions in the asymmetrical
factorial. Thus, an interaction of the asymmetrical factorial can be
confounded in several ways by confounding its different corresponding
interactions in the symmetrical factorial in different replications. This is
evidently not the case when the interaction contains only real factors.

We have seen earlier how the first replication of the symmetrical
factorial is obtained. The set of interaction of the asymmetrical factorial
which are confounded while obtaining this replication is, therefore, known.
While obtaining further replications for the balance, the interactions for
confounding in the symmetrical factorial have to be so chosen that in
each replication the same set of interactions of the asymmetrical factorial,
as in the first replication, is confounded. Different replications are so
chosen that this set of interactions of the asymmetrical factorial is
confounded in all possible ways, that is, corresponding to all possible
choices of confounded interactions of the symmetrical factorial, which
always lead to the same confounding in the asymmetrical factorial.

The procedure of choosing the replications for balance can be
systematised by utilizing the defining contrasts for the factorial replication.
We shall introduce this concept with the help of Example 1 discussed
earlier.

Choice of Replications for Balance and Interactions

Confounded

In Example 1 we discussed the 2x2x3 factorial using blocks of four
units. The corresponding symmetrical factorial is 3® involving the factors
Xx, Yx and A. Level 2 of each of the factors Xt and Yx is omitted to get
the fraction. Considering first the factor Xv we can say that with the
help of the defining contrast

l—Xx

the 3s combinations are divided into three groups and the group contain¬
ing the level 2 of Xx is omitted. The concepts of defining contrasts, and
alias groups of interaction have been explained in Chapter 3. Thus, the
defining contrast of the fraction obtained by omitting the level 2 of Xx is

I=Xx.

Similarly, the defining contrast for omitting the level 2 of Yx is

I=YX.

Hence, the defining contrast for omitting the level 2 of each of Xx and
Yx is

I=Xx=Yx=XxYx=Xx*Yx.

Actually with the help of these defining contrasts the 3® combinations are
divided into nine groups of three each. In four of these groups none of
Xx and Yx occur at level 2. These four groups form the required fraction
along with the levels of A.

126

DESIGN AND ANALYSIS OF EXPERIMENTS

Let the interaction XxYxA be confounded to get the first replication.
Then all interactions in the alias group of interactions of Xx YXA are a so
confounded. The alias group of interactions of XxYXA is shown below.

Xl Y1A=X12 YXA Y2 A=Xx2 Y2 A=Xx* A = YXA =XxA=A = Yxa A.

The corresponding confounded interactions in the asymmetrical factorial

-are respectively.

XYA, XYA, XYA, XYA, XA, YA, XA, A, YA.

That is, the confounded interactions are XYA, XA, YA and A. The
interaction XxYxA which was originally confounded to get the first
replication, corresponds to XYA. Now confounding all interactions in the
alias of XxYxA which correspond to XYA a balanced design is obtained.
Thus by confounding the interaction XxYxA,Xx2 YxA,XxYx2AandXx2 Yx2 A,
one in each replication, we get a balanced design in four replications. I
more than one interaction of the symmetrical factorial is confounded to
get the first replication, then the above considerations should hold for
each of the confounded interactions.

The interactions XYA is confounded due to blocking while the other
interactions XA, YA and A are confounded due to fractionation. The loss
of information of these three interactions is considerably less than the loss

on XYA.

Example 4: In Example 2 we discussed the design 3x2x2 in six plot
blocks. The corresponding symmetrical factorial is 24 with factors Xx, X2,
A and B. The fraction was obtained by omitting the combination 11 of
the pseudo factors Xx and X2 and using the other three combinations as
the level codes of the factor of symmetry X.

Let us obtain the first replication of the corresponding symmetrical

factorial by confounding XiX2AB.
By taking the defining contrasts

I=Xx=X*=XxX2

the 24 combination can be divided into four groups. One of these groups
contain the combination 11 of the factors Xx and X2. This group is
omitted for getting the fraction. So the defining contrasts for the fraction

are

I=Xx=Xt=XxX2.

The aliases of XxX2AB are as below

XxX2AB=X%AB=XxAB=AB.

The interaction confounded in the asymmetrical factorial are therefore

XAB, XAB, XAB, AB.

So there are three interactions viz. XxAB, X2AB and XxX2AB each of which
corresponds to XAB which was originally confounded. A balanced design
is, therefore, obtained by confounding the above three interactions in
three replications separately.

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

127

In addition to XAB which is confounded due to blocking, the interaction
AB is also confounded due to fractionation. The contents of the blocks
of the balanced design are shown in Table 4.3.

Block Contents of the Confounded Asymmetrical Factorial 3x2x2 in Six Plot Block.
(The Factors in the Treatment Combinations Appear in the Order Xly X2, A and B)

TABLE 4.3

Replication I

Replication II

Confounded Y . _
interaction axab

XaAB

Replication III

XjXaAB

Block 1

Block 2

Block 1

Block 2

Block 1

Block 2

0000

0 0 0 1

0000

000 1

0000

000 1

00 11

00 10

0 0 11

00 10

0 0 11

00 1 0

0 100

0 10 1

0 10 1

0 100

0 110

0 111

0 111

0 110

0 110

0 111

0 10 1

0100

10 10

10 11

1000

100 1

10 10

10 11

10 0 1

1000

10 11

10 10

100 1

1000

By recoding the levels of X, denoting 00 by 0, 01 by 1 and 10 by 2, the
design is converted to one where the levels of X are 0, 1,2. This design
is shown below.

Replication I Replication II Replication III

Block 1

Block 2

Block 1

Block 2

Block 1

Block 2

poo

0 1 1

1 00

1 1 1

21 0

20 1

00 1

0 1 0

1 0 1

1 1 0

2 1 1

200

000

0 1 1

1 0 1

1 1 0

200

2 1 1

00 1

0 1 0

1 00

1 1 1

201

2 10

000

0 1 1

1 0 1

1 1 0

2 0 1

2 1 0

00 1

0 1 0

1 00

1 1 1

200

2 1 1

Example 5: 6x22 design in 12 plot blocks. Here s=2. There is,
therefore, one factor of asymmetry X at six levels and two real factors
A and B each at two levels. The pseudo factors corresponding to X are
X X3 and X3, each at two levels. The six levels of X are designated by six
combinations of Xv X2,X3 omitting the two combinations of, say, 110 and
111. The level designations of the three factors are shown below.

128

DESIGN AND ANALYSIS OF EXPERIMENTS

Factors

A

0

1

B

0

1

Levels

X

0 0 0

0 0 1

0 1 0

0 1 1

1 0 0

1 0 1

The 24 combinations are obtained by forming combinations of these levels.
This is a fraction of the corresponding symmetrical factorial 25.

Using the defining contrasts I=X1=X2—XlX2, the 25 combinations
can be divided into four groups. In one of these groups the omitted com¬
binations 110 and 111 of the factors Xx, X2, X3 which were omitted, occur.
Thus, the defining contrasts for the fraction are

I— X1=X2=X1X2

The defining contrasts are actually those interactions which are confounded
in the omitted combinations of the pseudo factors.

In designs where the number of omitted combinations of the pseudo
factors corresponding to a factor of asymmetry has a common multiple
with the total number of combinations of the pseudo factors, different
choices of the initial replication may lead to different designs. One such
design is as follows:

Choice 1: Let the first replication be obtained by confounding X\XtXsAB.
Its aliases are

XxX2XaAB=X2X3AB=XxXsAB=XaAB.

Correspoding interactions are XAB, XAB, XAB, XAB. Hence, a balanced
design in four replications is obtained by confounding separately
XxX2X3AB, X2X3AB, XxX3AB and XaAB. The interaction XAB alone is
confounded is this design.

Choice 2: Let us now choose XxX2AB for confounding to obtain the
first replicate. This choice has the peculiarity that the pseudo factor
portion in it, viz., XxX2 is present in the defining contrasts as an
interaction.

Its aliases are

XlXiAB=XiAB=XxAB=AB

The corresponding interactions are

XAB, XAB, XAB, AB.

Hence, a balanced design is obtained in three replications by confounding

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

129

separately XxX%AB, X2AB and XxAB. The interactions which are con¬
founded here are XAB and. AB. We, thus, see that the two different choices
of interactions for confounding to obtain the initial replication have given
two different designs. One design requires four replications confounding
only XAB while the other requires three replications but confounding
XAB and AB. The block contents for the three replications corresponding
to the second choice are shown in Table 4.4.

Block Contents of the Design 6x22 in 12 Plot Blocks in Three Replications. The
Factors in the Different Combinations Appear in the Order Xx, X2, A and B.

TABLE 4.4

Replication I

Replication II

Replication III

Confounded
interaction

XxXz AB

XxAB

X2AB

Block 1

Block 2

Block 1

Block 2

00 000  00 00 1

00000  0000 1

00 0 1 1  0 0 0 1 0

000 1 1  0 0 0 1 0

0 0 111  0 0 110

0 0 10 0  0 0 10 1

0 10 10  0 10 11

0 10 0 1  0 1000

0 1110  0 1111

0 110 1  0 110 0

10010  10011

1 000 1

1 0 0 0 0

10 110  10 111

10 10 1  10 100

0 0 10 0  0 0 10 1

00111  0 0 110

0 1000  0 10 0 1

0 10 11  0 10 10

0 1100  0 110 1

0 1111  0 1110

1 000 1

1 0000

10 0 10  10 0 11

10 10 1  10 10 0

10 110  10 111

Block 1

Block 2

00 000  0 0 0 0 1

000 1 1  000 1 0

00 100  00101

00111  0011 0

0 1001  0 1000

0 10 10  0 10 11

0 110 1  0 1100

0 1110  0 1111

1 000 0

1 00 0 1

10011  10 0 10

10 10 0  10 10 1

10 111  10 110

Example 6: To construct the design 2x3x3 in six plot blocks. Here
s==2 There are two real factors A and B each at three levels and one
factor of asymmetry X at two levels. The corresponding symmetrical
factorial is 33 with the factors Xlt A and B where Xx corresponds to X.
The fraction is obtained by omitting the level 2 of Xx. The level Resigna¬
tions of X are 0 and 1. The defining contrast is I=Xx as one of the three
groups obtained by confounding Xx is omitted to get the fraction. Let
the first replicate be obtained by contending XxAB. aliases^are
y A Ft_Y * AB=AB Corresponding interactions are XAB, XAB ana A .

' thf two replications ob.ataed by confounding X,AB and X^AB

130

DESIGN AND ANALYSIS OF EXPERIMENTS

give the balanced design. The interactions confounded are XAB and AB
each with two degrees of freedom.

One more design is possible by choosing XxAB2 for confounding in the
first replication. This design is also balanced in two replications obtained
by confounding XxAB2 and Xx2 AB2. The interactions confounded are
XAB2 and AB2.

Combining these two designs a third design can be obtained in four
replications. In this design the interactions XAB, XAB2, AB and AB2 are
confounded. This design is balanced for the interaction of the factors
A and B.

Example 7: To construct the design 3 x 23 in six plot blocks. Here s—2,
since the number of blocks per replicate is 22. There are three real factors,
A, B and C, each at two levels and one factor of asymmetry X is at three
levels. Corresponding to X there are two pseudo factors Xx and X2. The
corresponding symmetrical factorial is 25. The three combinations of Xx
and X2 other than 11 are used to designate the levels of X. The defining
contrasts are

because by confounding Xx, Xt and XxX2 the 2s combination can be divided
into four groups one of which contains the combination 11 of Xx and X2.
This group is omitted to get the fraction.

As the number of blocks per replication is four in this design, three
interactions are to be confounded to get the first replication. Let us
confound

XxAB, X2AC and X,X2BC.

The aliases of these interactions are shown below together with the
corresponding interactions in the asymmetrical factorial:

(i) XxAB=AB=XxX2AB=X2AB

XAB AB XAB XAB

(ii) X2AC=XxX2AC=AC=X1AC

XAC XAC AC XAC

(iii) X1X2BC=X2BC=X1BC=>BC

XBC XBC XBC BC.

So we have to take other replications such that the interactions

XxX2AB, x2ab

XxX2AC, XxAC

XxBC, x2bc

occur equally frequently in the confounded interactions. Such a set of
confounded interactions is shown below:

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

131

(1) XxX2AB, XxAC, x2bc

(2) x2ab, x,x2ac, XxBC.

So the design in three replications obtained by confounding these two sets
of interaction and the one confounded earlier, is balanced. The interactions
confounded in the design are XAB, AB, XAC, AC, XBC and BC.

4.4 Construction of Confounded Asymmetrical

Factorial vx22 in 2v Plot Blocks

This series of designs can be obtained by using balanced incomplete block
(B.I.B.) designs which will be discussed in Chapter 5. The method
is described below.

Let the three factors be denoted by X at v levfels and A and B each at
two levels. Let us define by a the vector of the two combinations (??) of
the factors A and B, and by p the vector of the remaining two combinations
(JJ). Let us obtain a B.I.B. design with v treatments and block size k
in b blocks such that each treatment is replicated r times and each pair of
treatments is replicated X time. Let us further write the incidence (design)
matrix M of this design by using the symbols 0 and 1.

Next, the symbol 1 in M is replaced by a and the other symbol 0 is
replaced by (3. Denoting the levels of X by 1, 2,..., v, the mth element in
each row of M is associated with m, the mth level of X(m=l, 2,..., v).
If m is associated with a, this association creates the combinations mOO
and mil; if with p, it creates (mOl and mlO).

When all the elements of M are associated with the levels of X, we get
from the rows of this matrix, b blocks each of size 2v. Another set of b
blocks is obtained by replacing a by £ and (3 by a in the previous set of b
blocks. The design in these 2b blocks is balanced. The interactions XAB
and AB are confounded.

Example 8: To construct 7x22 design in 14 plot blocks. The B.I.B.
design with the following parameters is used

The incidence matrix of the design is

v=b=7, r=k=3, A= 1.

110 10 0 0

0 110 10 0

0 0 110 10

M=

0001101

1000110

0100011

1 0 1 0 0 0 1 |

132

DESIGN AND ANALYSIS OF EXPERIMENTS

Replacing 1 by a and 0 by p and then associating the mth element in each
row by m (m=l, 2,.. .,7) we get the following:

la, 2a, 3p, 4a, 5p, 6p, 7p

ip, 2a, 3a, 4p. 5a, 6p, 7p

ip, 2p, 3a, 4a, 5p, 6a, 7p

lp, 26, 3p, 4a, 5a, 6p, 7a

la, 2p, 3P, 4p, 5a, 6a, 7p

ip, 2a, 3p, 4p, 5p, 6a, 7a

la, 2p, 3a, 4p, 5p, 6p, 7x

Replacing the association la by 100 and 111 and so on for the other
associations and writing the transpose of the resultant matrix we get the
following seven blocks of the design:

Block

1

1  0  0

1  1  1

2

1  0  1

1  1  0

2  0  0

2  0  0

2  1  1

2  1  1

3

1  0  1

1  1  0

2  0  1

2  1  0

4

5

6

7

1  0  1

1  1  0

2  0  1

t  0  0

1  1

1

1  0  1

1  0  0

1  1  0

1  1

1

2  0  1

2  0  0

2  0  1

2  1  0

2  1  0

2  1

1

2  1  0

3  0  1

3  0  0

3  0 0

3  0  1

3  0  1

3  0  1

3  0  0

3  1  0

4  0  0

4  1  1

5  0  1

5  1  0

6  0  1

6  1  0

7  0  1

3  1  1

4  0  1

3  1  1

4  0  0

3  1  0

4  0  0

3  1  0

3  1  0

3  1

1

4  0  1

4  0  1

4  0  1

4  1  0

4  1  1

4  1  1

4  1  0

4

1  0

4  1  0

5  0  0

5  1  1

6  0  1

6  1  0

7  0  1

5  0  1

5  0  0

5  0  0

5  0  1

5  0  1

5  1  0

5  1  1

5  1  1

5  1  0

6  0  0

6  0  1

6  0  0

6  0  0

6  1  1

7  0  1

6  1  0

6  1  1

6  1

1

7  0  0

7  0  1

7  0  0

7  1  1

5  1  0

6  0  1

6  1  0

7  0  0

7  1  1

7  1  0

7  1  0

7  1  0

7  1  1

7  1  0

The other seven i blocks can  be obtained  from  the  above  seven  blocks by
replacing 00 combination of AB by 01; 11 by 10; 01 by 00 and 10 by 11.

Other incomplete block designs can also be utilized likewise to get
partially balanced asymmetrical factorials in the sense that though the
interactions AB and XAB can be estimated independently, the loss of

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

133

information of the different degrees of freedom of XAB need not be the
same. This method was mentioned by Das (1960).

4.5 Analysis of Balanced Confounded Asymmetrical Factorials

The analysis of balanced confounded asymmetrical factorials is not straight
forward, because the data are non-orthogonal and it is required to adjust
unequal representation of the block effects in the different contrasts of the
confounded interactions.

One very simple and straight forward method is to adjust each obser¬
vation for the block effects by subtracting from each observation the average
of the block in which it occurs. Suppose ytjki is an observation in Ith
block of a confounded asymmetrical factorial involving three factors. The
levels of the three factors are denoted by i,j and k in the observation yijki-
Let Bi be the total of the block containing yijki and r be the block size.

Then Xijki=yuki—Bilr is the adjusted yijki observation. Next, these
adjusted observations are subjected to the usual analysis of variance as
appropriate for the classification of the data. That is, if there are three
factors, then the analysis of variance is the same as that of the three-way
classified orthogonal data with as many observations in each cell as the
number of replications of the design. This analysis gives as such the
correct sums of squares of all main effects and interactions which are not
confounded. These sums of squares can also be obtained by analyzing
the original unadjusted observations by the usual method.

The sum of squares due to a confounded interaction when obtained
from the analysis of adjusted observations has to be adjusted by dividing it
by the fraction of information recovered for the interaction. In all
standard designs the fraction of information recovered is known. It can
also be obtained as below.

Let L denote a contrast among the treatment combinations for a con¬
founded interaction. Let each treatment combination in L be replaced by
the total of the observations under that treatment combination and call
this function of the observations Ly. Let each treatment combination in L
be again replaced by the total of the adjusted observations under that
treatment combination and call this function of the adjusted obser¬
vations, Lx. Then the ratio var L*/var Ly gives the fraction of the
information recovered of the interaction. The rest of the analysis consists
of finding the unadjusted block s.s. and the total s.s. The error s.s. is
obtained by subtraction. This method of analysis has been illustrated
after describing an alternative method of analysis which provides directly
the fraction of information recovered of each confounded interaction.

4.5.1 An Alternative Method of Analysis

We have discussed below another convenient method of finding the sum of

134

DESIGN AND ANALYSIS OF EXPERIMENTS

squares of confounded interactions. This method has the advantage that
the fractions of information recovered of the confounded interactions can
be obtained from it easily. By this method we can ascertain whether the
confounded interactions are estimable mutually independently or not.

For each confounded interaction, first, suitable linear functions of the
treatment combinations are defined such that their contrasts represent the
interaction contrasts. We assume that these linear functions are defined
by using +1,-1 and 0 as the coefficients of treatment combinations. Such
functions will be called reparameterized treatments for the interaction or
simply R-treatments. In the expected value of any observation variable,
y, any particular R-treatment, say, pi occurs with the coefficient 0, +1 or
— 1 accordingly as the treatment combination of the observation occurs in
pi with coefficient 0, +1, or — 1.

Example 9: In the design 3 x22 in six plot blocks presented in Example 4,
the interaction XAB is confounded. For finding the sum of squares of
XAB we can take the following three reparameterized treatments:

Pq—Xq (a06o+aA Oib0 tfo&i)

Px—xi (aobo+axb^aibo—aob^

p2—x2 (u0^0+ai^i aibo <*A)

where x0a0b0 denotes the treatment combination 000 and so on for the
other products.

Evidently, the contrasts among p0, px and p2 are the contrasts for

XAB.

In any observation variable, say, y010, the R-treatment p0 occurs with — l
as coefficient and the other two R-treatments occur with coefficient 0,
because the coefficient of the treatment combination 010 of the observation
is —1 in p0 and 0 in each of px and p2.

After the R-treatments are defined a two-way table of the R-treatments
and blocks is made. The contents of the different cells of this table are
the frequencies of occurrences of the R-treatments in the different blocks.
For finding the frequency of occurrence of any particular R-treatment, say.
Pi in a block, each observation in the block is examined for co-efficient
values of p0>Ri and p2. In these values pi occurs with coefficients 0, +1, or
— 1. The algebraic sum of these coefficients gives the frequency of />,• in
the block. Likewise, the frequencies of all the R-treatments in all the
blocks are obtained for completing the frequency table.

Example 10: The six blocks of the balanced 3x22 design in six plot
blocks are as shown:

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

135

Replication I Replication II Replication III

Block 1  Block 2

Block 1  Block 2

Block 1  Block 2

0 0 0

0 0 1

0 0 0

0 0 1

0 0 0

0 0 1

0 1 1

0 1 0

0 1 1

0 1 0

0 1 1

0 1 0

1 0 0

1 0 1

1 0 1

1 0 0

1 1 1

1 1 0

1 1 0

1 1 1

2 0 1

2 0 0

2 0 0

2 0 1

1 0 1

1 1 0

2 0 1

1 0 0

1 1 1

2 0 0

2 1 0

2 1 1

2 1 1

2 1 0

2 1 0

2 1 1

The frequencies of p0, px and p2 defined above for the XAB interaction
in the different blocks of the above design are obtained below.

The R-treatments of the six observations variables in the first block
are in the order of the treatment combinations in that block p0, pQ, px, pu
—p2, —p2. Hence the frequencies of the R-treatments in this block are
as shown in Table 4.5. The frequencies of these treatments in the other
blocks have also been shown in Table 4.5.

TABLE 4.5

Frequencies of /^-Treatments for XAB in the 3 x 22 Design

/{-treatments

Po

Pi

P2

2

2  —2

Blocks
/

1

2

-2

-2

. 3

2

-2

4

5

6

-2

2

2

-2

-2

2

2

2

-2

-2

2

For finding the sum of squares of the confounded interactions in addition
to the cell frequencies obtained above, the observation total in each cell is
also required. These totals are obtained as below.

Letj>;* denote kth. observation in y'th block and auk be the coefficient
of the R-treatment pt in the expected value of V}k. Then the total of the
cell defined by ;'th block and ith R-treatment is given by 2aiJk y}k. Further

2 aijk gives the frequency of pi in ;'th block.
k

Accordingly, the cell total of the cell defined by p0 and block 1 in the
above example is the sum of those observations in the first block each of

136

DESIGN AND ANALYSIS OF EXPERIMENTS

which has the value p0, that is, the sum of the first two observations in the
block. Similarly, the total in the cell defined by block 1 and p2 is the sum
of the last two observations in the block multiplied by 1, as the co-efficient
of p2 value of each of these two observations is —1.

Both the cell frequencies and cell totals of the block X R-treatment
table are now obtained. These data in the table are now analyzed just
like the analysis of non-orthogonal data discussed in Chapter 2. The total
frequency of zth i?-treatment is taken as w/=2 | atjk |. This frequency is

also equal to P/k where P is the total number of observations in the design
being analyzed and k is the number of i?-treatments in the interaction
under consideration. The block size, n.j is the same as in the design. It
is not to be obtained by adding the frequencies in the block.

For finding the sums of squares of balanced interactions the problem
of solution of the reduced normal equations of the i?-treatments is very
much simplified as we shall see in the following examples.

Example 11: We shall analyze the 3 X 22 design in six plot blocks presented
above by the method described here. In this design the interactions XAB
and AB are confounded. The ^-treatments for XAB have been defined as

pt^iOQ+i Il-z01-il0(*=0, 1, 2)

The ^-treatments for AB are

and ,^=001 + 010+101 + 110+201+210.

m0=000+011 + 100+111 +200+211

The frequency tables for these two interactions are shown in Table 4.6.

Frequency Tables of the jR-treatments of XAB and AB Interactions

TABLE 4.6

Interaction XAB

/t-treatments: p0

Pi

P%

Interaction AB
mo mj

Block size

n.f

Blocks 1

2

3

4

5

6

2

-2

2

-2

2

-2

2

-2

-2

2

-2

2

-2

2

2

-2

-2

2

4

2

4

2

2

4

2

4

2

4

4

2

6

6

6

6

6

6

Total n<.

12

12

12

18

18

36

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

137

The reduced normal equations for XAB are

(l2 —y) Po-\\{Pl+P*) = Q*

(l2~) Pi+!(Po+/>t)-e*

Those for are

The adjusted totals QPoetc. are found exactly as described in the analysis of
non-orthogonal data excepting that the marginal totals of the reconstrained
table are not taken as the block totals. The totals of the observations in
the blocks are taken as the block totals. The marginal jR-treatment totals
are, however, used as such for obtaining their adjusted total. These totals
are actually the algebraic sum of the requisite cell totals.

Here, QP(i=TP*-2f6 (B1-B.i-\-B3-BA+B5-B6) where Tp,is the margi¬
nal total of the p0 treatment obtained from the table and B1 etc. are the
block totals and not the marginal totals of the table. The other adjusted
totals for pr and p2 are ob+ained similarly.

The adjusted total Qm0—Tma —1/6 (4B1A-2B%+^B3-\-2Bi+2B6-\-4B6)
and 0Ml=Tmi-l/6(251+4J524-258+454+456+256) where Tm and Tm
are the marginal 7?-treatment totals.
The reduced normal equations for XAB can be written as

20 , 2 y _
X Po+t
20 , 8 v

y Pi "h g y Pi ~ Qpi

y 7^2+^ J Pi—Qpt

Taking 2 pi =0, we get the solutions as

^ 3 _
Po~~20

-_3 n
Pi 20

3 n

P-2 9Q Up*

xs /v. 2a2
Variance of (pn—pi)=20"*
T

138

DESIGN AND ANALYSIS OF EXPERIMENTS

If XAB is not confounded, var (p0— pj)

12 •

Hence, the fraction of information recovered is

20 5
3xl2~9’

The solution of the normal equations for AB gives us

Qmo
°~ 16

m =Q”X
1 16

The variance of When AB is not confounded

var (w0—wx)=

2a2
18

,16 8
Hence, information recovered=jg=^-

The sums of squares due to XAB and AB are obtained as below

, f VQpiY

,s Qpi2~±~ir~

s.s. (AB)=±2Qm,\

Since 2 Qmi=0, the correction factor has not been subtracted while

I

finding the sum of squares of AB.

When all the frequencies in a table for an interaction are positive, the
sum of the adjusted totals is zero. In other cases this sum need not be
zero. Hence, in such cases the correction factor has to be subtracted
from the crude sum of squares of the adjusted totals.

This method of analysis along with the other method of analysis
described earlier has been illustrated below by analyzing a set of
experimental data.

4 5.2 An Illustration

An experiment was conducted in Jhansi, India, to study the effect of
nitrogen and clipping in the spring and fall seasons on the yields of hay
from alfalfa. Nitrogen was taken at three levels, viz., No nitrogen (0),
30 lbs of nitrogen per acre (1) and 60 lbs of nitrogen per acre (2),
Clipping in each season was tried at two levels, viz., No clipping (0) and
clipping (1). The design adopted for the experiment was the 3x2x2
confounded asymmetrical factorial in three replications using blocks of
six plots. The treatment combinations have been written by using the
level codes of nitrogen by 0, 1 and 2 and those for each of the other

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

139

>
&

.2 *>>

cn

8
«

>
•8

2

8
cq

>
'O

.2 E

cn

o
JO
P2

>
T3
T3
.2 2
pq

> <t>
T3

2
2
E
CN

O
2
PP
> o>

.2 c
o

a
pd

c
o
ccJ O
E

C2
.2 aj
.2 E
pd

t
n
e
m

i
r
e
p
x
E

*
2
x
3

e
h
t

f
o

s
d
l
e
i
Y

t
o
l
P

d
n
a

s
n
o
i
t
a
n
i
b
m
o
C

t
n
e
m
t
a
e
r
T

e
h
T

I

o
CN

1

•n
CN

i

r-

CN

1

•n

CN

00
cn

cn
cn

in
r-

VO
in

cn
vo

cn
oc

OO 00
rf
cn

©
o

CN
CN

1

00
CN

o

©
V—

cn
CN

o
o
CN

«—i
cn

VO

CN

VO

cn
r-

VC
vr>

CN
*n

O O © **">
CN

i—i
o

8

O
CN

©
i-H
CN

8

O
CN

1

O
cn

5

VO

»T)

O

7  7

©V

ON

cn

. %o VO
cn

cn

VO
Tt

T_M

—

in
Tt

o
cn

©V
cn

O
i—«
cn

8

CO

cn

cn

VOi

VO
in

O
TT

o

o
*—<

Tt

o
O
CN

cn
TT

_

—■1
CN

<n|<
<N

cn

os

o

r-<

•

o
Tt

o
o

cn r-
cn cn
cn

vO
Vn

t"-
CO

i—

,“l

o
o
CN

00
Cn

L t
*—<
<N

CN

O

in

OO

VO
CN

,

O
o

o
CN

o
>»—«
o

iT)

cn

7  7

cn
cn

o
o
o

OO

1

tn
CN

,
*—«
O

in

7

OS
CN

CN
CN

o
o

On

1

©
o

VO
i—<

1

rt
CN

CO

CN
in

o
Tt

*n
Tt

00
Tt

I

T^- Tt

O O
<N 0
bO

r— <3

(Tt

140

DESIGN AND ANALYSIS OF EXPERIMENTS

factors by 0 and 1. These codes have also been indicated above while
describing the levels of the factors. The design together with the yield of
hay in kg (1000 gram) per plot are presented in Table 4.7. The deviation
of each observation from its block average has also been presented in

this table.

These data are analyzed first by the method described in 4.5.1. The first
step in this method is to get the deviation of each observation from its
block average. These deviations have been presented along with the
observations. Next, a three-way table corresponding to the three factors
has been prepared. In each cell the totals of the deviations corresponding
to the different treatment combinations have been entered. There are
three observations in each cell. Hence each cell total is based on three

deviate values. The table is presented below:

Three Way Table of the Experiment with the Deviate Totals in the Cells

TABLE 4.8

Levels of Nitrogen (N)

0

1

2

Levels of spring (S)

0

1

0

1

0

1

Levels of fall (F)

1

0

,

-51
(3)

-38
(3)

-56
(3)

-44
(3)

19
(3)

47
(3)

0
(3)

5,
(3)

8
(3)

20
(3)

13
(3)

31
(3)

Conducting the usual analysis as appropriate for three way orthogonal
-data we get the following sum of squares:

s.s. (N) = 4549.50

s.s. (S) = 2.78

s.s. (F) = 498.78

s.s. (NS) = 47.39

s.s. (NF) = 148.39

s.s. (SF) = 21.78

s.s .(NSF)= 25.38

Total s.s. = 8437.00 based on original observations

Block s.s.=2357.00.

As NSF and SF are confounded their sum of squares have to be adjusted
by dividing them by the respective fraction of information recovered.

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

141

In 4.5.2 above we have seen that the fraction of information recovered
for NSF and SF are respectively 5/9 and 8/9. The adjusted sum of
squares of NSF and SF are therefore,

s.s. (iVSF)=25.38-^=45.70

s.s. (SF)=21.78^|=24.50

TABLE 4.9

Analysis of Variance of the Experiment Obtained through Observation Deviate

Source of
variations

Blocks

N

S

F

NS

NF

SF

NSF

Error
(by subtraction)
Total

d.f.

s.s.

m.s.

5

2

1

1

2

2

1

2

19

35

2357.00

4549.50

2.78

498.78

47.39

148.39

24.50

45.70

762.96

8437.00

2274.75**

2.78

498.78**

23.69

74.20

24.50

22.85

40.16

The variations due to nitrogen and fall clipping effects are significant at
1 per cent level. The average values of the effects of the three levels of
nitrogen and two levels of fall clipping are given below.

N0 Nt Nt S.E. F0 S.E.

27.4 52.9 49.2 1.8 39.4 46.9 1.5

These averages show that application of nitrogen enhanced the yield very
much. The increase in yield due to the increase of dose of nitrogen
from 30 to 60 is not significant. Similarly, fall clipping has better effect

on the yield.

These data have now been analyzed to get the sums of squares due to
NSF and SF which are confounded by the alternative method discussed

in 4.5.2.

The i?-treatments for SNF are shown below

142

DESIGN AND ANALYSIS OF EXPIRIMENTS

^=000+011-010-001

^=100+111-110-101

^=200+211-210-201

The /^-treatments for SF are

mQ=000+011 + 100+111+200+211

/m1=001+010+101 + 110+201+210.

The tables showing the frequencies and totals of the different
^-treatments of the two interactions in the different blocks are shown in

Table 4.10.

Frequencies and Cell Totals of the.^-Treatments of NSF and SF

TABLE 4.10

Blocks

Po

NSF
Pi

P2

m0

SF

Block
totals

Block
average  n j

1

55(2)

- 92(—2)  - 93(—2)

55(2)

185(4)

240

40

2  — 51(—2)

96(2)

75(2)

171(4)

3

48(2)

- 96(—2)

84(2)

132(4)

4  —46(—2)

86(2)

1

0
0

>

—

1

/

C
4

/

—
V

86(2)

5

58(2)

134(2)  —108(—2)  192(4)

51(2)

96(2)

130(4)

108(2)

6  —7I(—2)  —131 (—2)

146(2)

146(2)

202(4)

Totals Tp{ —7

nt 12

-3

12

20

12

782

18

772

18

37

38

36

50

58

222

228

216

300

348

1554

6

6

6

6

6

6

Qpt =—7—2 (40—37+38—36+50—58)= —1

Qpv =—3—2 (—40+37—38+36+50—58)=23

QPt =20—2 (—40+37+38—36—50+58)=6

Q«,=782-^ (2x240+4x222+4x228+2x216+4x300+2x348)

= 14

(/«1=772—^(4x240+2x222+2x228+4x216+2 x 300+4x348)

= -14

s.s. (tfSF)=^l2+23*+62-^=45.70

s.s. (SF=)~ ^148+14*^=24.50.

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

143

These two sums of squares are exactly the same as obtained earlier. The
sums of squares of other interactions which are not confounded are
obtained by the usual method. The unadjusted block sum of squares and
total sum of squares are obtained as earlier. The error sum of squares is
obtained by subtraction.

4.5.3 Criteria of Balance and Mutual Independence of

Confounded Interactions

When more than one interaction is confounded in an asymmetrical
factorial design, it is necessary that these interaction effects are estimable
mutually independently. Otherwise, the error sum of squares can not be
obtained by subtraction. Moreover, adjustment of one confounded inter¬
action for the other confounded interaction is also complicated in such
cases. Therefore, it is to be ascertained first if the interactions are
estimable mutually independently. A procedure for this purpose is
described below.

Let fjk denote the frequency of ,/th ^-treatment of zth confounded

interaction in kth. block. Then, if

2 fjkfj'k
k

is constant for different choices of ^-treatments j and j' of the same zth
interaction, then the design is balanced in the sense that the loss of inform¬
ation of each degree of freedom of the interaction is the same. This
criterion, however, does not ensure that different confounded interactions
are estimable independently. For this purpose the following criterion
should be satisfied. Let

Uiip —'ZfijkZ'j'k •

k

If Uu, is constant for different choices of y'th and /th /^-treatments in the
zth and z'th confounded interactions respectively, then the zth and z'th
interactions are estimable independently.

4.6 Split-Plot Designs

In factorial experiments it may sometimes happen that certain factors
require bigger plots than others for convenience of the organization of
the experiment. For example, in an agricultural experiment involving
two factors, say, irrigation and nitrogen fertilizer, it is organizationaly very
inconvenient to apply different levels of irrigation to small neighbouring
plots. But there is no such difficulty for the application of different levels
of nitrogen. To meet such situations it is desirable to evolve designs
which can have different sizes of the experimental units in the same
experiment.

144

DESIGN AND ANALYSIS OF EXPERIMENTS

For this purpose first a design with bigger plots is taken to accom¬
modate the factors which require bigger plots. Next, each of the bigger
plots is split into as many parts as the number of treatments coming
from the other factor. The bigger plots are called main plots and the
treatments allotted to them are called main plot treatments or simply main
treatments. The constituent parts of the main plots are called subplots
and the treatments allotted to them are called subplot treatments. The
different types of treatments are allotted at random to their respective

plots. Such designs are called split-plot designs.

For example, let there be three levels of irrigation prescribing three
different amounts of water per plot and four doses of nitrogen fertilizer.
First a randomized block design with a suitable plot size is taken with the
three levels of irrigation as treatments. Let there be, say, five replications
in this design. The irrigation treatments are then allotted at random to
each of the five blocks of three bigger plots each. Next, each of these
main plots is split into four parts or subplots to accommodate the four
levels of nitrogen. The 15 main plots actually serve as 15 replications
of the subplot treatments. The subplot treatments are allotted at random

to the subplots in each of the main plots.

The split-plot designs are thus a combination of two or more
randomized block designs (depending on the number of factors) such that
the plots of one design form the block of another design. It is not
necessary that a split-plot design has always two sizes of plots. The
above analogy can be extended to have three or more plot sizes to
accommodate different types of treatments. Though in the above
example, the main plot treatments are the levels of only one factor, such
treatments can also be the combinations of the levels of different factors
each of which require similar plot size. Similarly, the subplot treatments
can also be the combinations of the levels of different factors. Accordingly,
the device of confounding can be applied to reduce the block sizes of
each of the constituent randomized block designs.

4.7 Analysis

We shall discuss the analysis of simple split-plot designs with two sizes
of plots. It is further assumed that both the main plot and subplot
treatments are the levels of single factors. Further the design adopted
for the main plots is a randomized block design.

Let the number of main plot treatments be a and that of the subplot
be (3. Let further the number replications in the randomized block design

for the main treatments be r.

First the observations in the p subplots in each main plot are added.
This will give ar totals distributed in r blocks of a units each. These
totals are then analyzed by the method of analysis of variance appropriate
for the randomized block design excepting that each sum of squares has

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

145

to be divided by (3 as the main plot observations are the totals of (3
observations. The partitioning of the total sum of squares is shown

below.

Let ytjk denote the observation from the A:th subplot treatment in the

jth main plot treatment in the /th replication.

Let further

2 yi}k=Rh 2 yuk—Tij,
Jk k

2 yuk=Aj, 2 yijk = Ijk, 2 yuk=Bk,
ik i u

and

2 Rt—G.
i

Then the different sums of squares for the main plot analysis are shown

in Table 4.11.

TABLE 4.11

Anaiyis of Variance of Main Plot Totals

Sources of variation

d.f.

S.S.

Replications

Main plot treatments

r—1

a— 1

Rl_&

7 ra£ . .

A,*__ G*
J Pr rap

Error

Total

(r_l)(a_l)

-TV* R* yAl+&
f, P t 3r rap

ra —1

rw« C2

5 e

For the analysis of subplot observations we treat the r« main plots as the

replications of the subplot treatments.

A two-way main plot treatment X subplot treatment is first made
entering the appropriate observation totals in each cell. There are a,3 cells
in this table and each cell contains the total of r observations coming
from the r replications of each combination of the two factors. An
analysis of variance of these totals gives the sum of squares due to subplot
treatments and interaction between subplot and main plot treatments in
addition to the sum of squares due to main plot treatments which has been
obtained in the previous analysis as well. The error sum of squares in the
subplot analysis is obtained by subtraction as all the sums of squares

146 design and analysis of experiments

including those in the main plot analysis add to the total sum of squares.

All these sums of squares are shown in Table 4.12.

TABLE 4.12

Analysis of Variance of Subplot Observations (Only s.s.)

Sources of variation

Replication (main plot totals)

Subplot treatments

Interaction

Error (subplot)

d.f.

ra—1

P-1

s.s.

Tu 2 G2

5 P

5fc2_ G2

\ ret rap

(a—1) (P-1)

% r 1 « ; ^ ^

(r—1)(P—D

By subtraction

Total

rap—1

G2

It is seen that in the analysis of split-plot designs there are as many error
variances as the number of plot sizes—one coming from each plot size and
its associated randomization. In the present case the error for testing the
interaction sum of squares is the subplot error because the interaction

contrasts are functions of subplot contrasts.

The above method of analysis has been derived from the following

model;

Yijk—y.-\-ri-\-a.jJr$k+IjkJr etjk

where Yi]k is the observation variable corresponding to the observation
yiJk coming from the fcth subplot treatment of theyth main plot treatment
in the ith replication; p. is the general mean, r/, a/ and [3& are the fixed
effects of the ith replication, yth main treatment and kth subplot treatment
respectively: Ijk is interaction effect and etJk are the error components
which are assumed to be independently and normally distributed with zero
mean and constant variance a2. As the subplots in a main plot are close
together, being located in the same main plot, two error components
corresponding to two subplots in the same plot are taken to be correlated
with pas the correlation coefficient. This type of association of observations
in the same main plots do not affect the usual analysis presented above.

Assuming that E(eJkjz)=c" and E{eijk eijk.)^9o* the expected values of

the two error sum of squares can be obtained as below:

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

147

Let Ea denote the main plot error mean squares and Eb, the subplot

error mean squares.

Then the expected value of isa=<T2{l-f ([}—l)p}and expected value of

Eb=o2 (1 - p).

From these the estimates of p and a2 come out as

)Eb

P

— _ Ea—Eb
9~Ea+$-l)£b

Expectedly p is positive. Hence Ea is expected to be greater than Eb.

4.7.1 Variance of the Estimates of Treatment Contrasts

Case 1 The estimate of the effect of any main plot treatment is the
average of all the observations coming from the treatment. Hence, the
variance of the estimator of the difference between two main plot treatments
say a0—at is given by

V(a0-0!)=—

. 2 Ea

Case 2 Similarly, the variance of the estimator of the difference between two

subplot treatments, say, bl}—b1 is given by V (b0—b})=—-.

O 17

rJ.Y

Case 3 If a0, av etc., denote the main plot treatments and b0, bu etc.,
denote the subplot treatments, then the variance of the estimator of the
difference between two combinations like aibj and ajhji is given by

Here, the error Eb is taken because this is a subplot comparison.

V&bj-^bj,)-2-- •

Case 4 The variance of the estimator of the difference between two
combinations of the type aibj and a^by, that is, two combinations belong¬
ing to different main treatments, is given by

V(aibj—att bji)=~- •

This is because the two averages which estimate the above two combination
effects are independent being based on observations coming from different
main plots. Substituting the estimate of c2 we get

V (aibj—aj> bj>)-

2{Ea+{$-\)Eb)

When there are more than two sizes of the plots the same technique of

148

DESIGN AND ANALYSIS OF EXPERIMENTS

analysis can be extended in a straight forward way. We may assume that only
observations coming from the smallest plots in the next bigger plots are
correlated. This assumption seems to be more reasonable than assuming
an association between observations coming from two different plot sizes.

If the subplot or main plot treatments are combinations of the levels of
several factors, then the above technique of analysis can be extended in the
usual manner, excepting that the ((3— 1) degrees of freedom for the
subplot treatments have to be partitioned according to the factors whose level
combinations build up the p combinations. The same considerations hold

for the main treatments as well.

EXERCISES

1. Construct the confounded design 6x23 in 12 plot blocks and indicate the

confounded interactions. Outline the method of analysis of the design.

2. Construct the 3x22 design in three plot blocks. Indicate the interaction that are
confounded. Find the loss of information on the different confounded
interactions.

3. Examine if the following 5 x 22 design in 10 plot blocks and five replications fa

balanced.

la

Ip

IP

IP

la

IP

la

la

IP

la

2a

2a

2P

2P

2p

2a

2p

2a

2a

2p

3P

3a

3a

3P

3p

3P

3a

3p

3a

3a

43

4P

4a

4a

4P

4a

43

4a

4P

4a

5p

53

53

4a

5a

5a

5a

53

5a

53

Here, the combination /a means iOO and ill and ip means id and *10 (*=1, 2y
3, 4, 5).

4. Discuss why asymmetrical factorials in one replication are not considered suitable

designs:

5. Obtain first a balanced confounded factorial 5 x 3 in three plot blocks. Next,
associate each combination of the above design with the two levels 0 and 1 of a
third factor so that out of one combination of 5 x 3 factorial, we get two combi'
nations of the 5x3x2 factorial and the block size becomes six. Show that the
resultant 5x3x2 design in blocks of six plot and four replications, is balanced.
Derive the method of its analysis.

6. In an asymmetrical factorial with the factors X, A and B at levels 3, 2 and 2
respectively, the three levels of X are coded by the four combinations of two
factors Xi and X% each at two levels as below. The combination 00 is used to
code the first level of X, the combination 01, the second level and each of 10 and
11 is used to code the third level. This way the asymmetrical factorial is.

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS 149

x

converted to a symmetrical factorial. Obtain the confounded factorial 3x2x2
in four plot blocks in one replication and outline the method of analysis of the
design. Indicate what interactions are confounded.

7. In a factorial with two factors each factor requires bigger plots. It is required
to study their interaction more accurately. Suggest a suitable design for the
experiment and indicate its method of analysis, (strip- plot designs)

8. To study the effect of application of different doses of nitrogen, phosphorus and
potash with different doses of farm-yard manure on cabbage an experiment was
conducted at the Indian Agricultural Research Institute, New Delhi during
1961-62. The design adopted was split-plot-cum-confounding. The details
of the experiment are given below:

I. Treatment

Main plot: All combinations of

Nitrogen

Phosphorus

$

 o

1

Pi-40

P2-80

N~i—50 lb/acre

N2-100

Na—150

Subplot treatments:

Fi=2.5 tons/acre

F2—5 tons/acre

Ib/acre

99

99

Potash

*o=0
F1=40

^
5

I
I

0
0

O

lb/acre

99

99

2. Numbers of replications—Two
3. Plot size: Gross: 17'xl5'
Net: 17'x 10'

The layout plan and yield of cabbage in (Oz) per plot are given below:
The lower figures indicate the yield and the upper ones the treatment combinations.

Analyze the data appropriately. The yields are below the treatments.

REPLICATION I

Block I Block II Block III

1001

378

2102

1024

1212

867

1121

841

3022

1177

2221

999

3111

908

2012

1105

3202

1340

1002

535

2101

1122

1211

510

1122

460

3021

721

2222

1154

3112

1472

2011

747

3201

1159

3121

4428

2111

622

1221

418

3211

627

2022

581

3001

173

1101

607

2202

768

1011

404

3122

803

2112

744

1222

599

3212

1077

2021

508

3002

91

1102

489

2201

618

1012

434

2002

855

1202

626

2212

658

1111

551

1022

291

3222

623

3012

523

2121

591

3102

975

2001

315

1201

368

2211

354

1112

312

1021

203

3221

250

3011

229

2122

444

3101

193

150

DESIGN AND ANALYSIS OF EXPERIMENTS

Block I Block II Block III

REPLICATION II

2022

2021

337

3201

591

2101

951

3121

894

mi

470

2211

572

3012

464

1001

386

1221

509

506

3202

598

2102

425

3122

393

1112

516

2212

482

3011

253

1002

160

1222'

365

1011

338

2221

867

2001

442

2111

368

3102

300

1122

379

1201

381

3021

58

1012

195

2222

396

2002

426

2112

638

3101

127

1121

68

1202

306

3022

191

3212

3211

375

389

3222

346

3112

235

2012

171

3001

192

1212

263

1102

479

1021

369

2202

850

2121

276

3221

293

3111

294

2011

97

3002

258

1211

343

1101

521

1022

453

2201

707

2122

372

9. In a varietal cum manurial experiment on soybeen, four levels of nitrogen (0,0.1,
0.3 and 0.5 cwt per acre, designated as rt0, nv n2, n3 respectively) were applied
to each of three varieties v1( v2, v3. The different levels of the manure for each
variety were applied by splitting the plot into four subplots. The plan and the
yields (in lbs) are given in the following table. Analyze the data and give your
comments.
Plan and yields of a split-plot experiment

Replication I Replication II Replication III Replication IV

vi

v2

v3

«o
104

n2
112

«o
112

«2
125

«o
116

'*2
121

«1
105

«3
146

«i
109

«3
161

«i
119

«3
159

*1

v2

V3

«0
117

«2
153

«o
111

« 2
134

«o
119

*2
143

«i
129

«3
139

«i
123

«3
141

«i
132

n3
149

Vl

v3

V3

H
12 3

«2
151

n0
117

«2
159

no
102

"2
167

«i
123

«3
164

«i
109

n3
157

«i
116

n3
161

n

V2

v3

no
105

«2
129

no
124

«2
133

no
135

«i
142

n i
137

nz
143

«i
129

«3
139

143

nz
158

ASYMMETRICAL FACTORIAL AND SPLIT-PLOT DESIGNS

151

REFERENCES

1. Banerjee, A.K. and Das, M.N. (1969). “On. a method of construction of con¬
founded asymmetrical factorial designs.” Cal. Stat. Asso. Bull. 18, pp. 163-77.
2. Chakrabarti, M.C. (1962). Mathematics of Design and Analysis of Experiments,

Asia Publishing House.

3. DAS, M.N. (1960). Fractional replicates as asymmetrical factorial designs. J.Ind.

Soc. Agri. Stat. 12.

4. Kishen, K. and Srivastava, J.N. (1959). “Mathematical theory of confounding
in asymmetrical and symmetrical factorial designs.” J. Ind. Soc. Agri. Stat. 11,
pp. 73-110.

5. Kishen, K. and Tyagi, B.N. (1964). “On the construction and analysis of some
balanced asymmetrical factorial designs.” Calcutta Statistical Association Bull.,

6. Kshirsagar, A.M. (1966). “Balanced factorial designs.” Jour. Royal Stat.

13, pp. 123-49.

Soc. B, 28, pp. 559-67.

7. Li, J.C.R. (1944). “Design and analysis of some confounded factorial experi¬

ments,” Res. Bull. 333, Iowa State College of Agriculture.

8. Muller, E.R. (1966). “Balanced confounding of factorial experiments.” Bio-

metrika, 53, pp. 507-24.

9. Nair, K.R. and Rao, C.R. (1948). “Confounding in asymmetrical factorial

experiments.” J. Roy. Stat. Soc. B. 10,109-31.

10. Raghavarao, D. (1971). Construction and Combinatorial Problems in Design of

Experiments, Wiley, N.Y.

11. Sardana, M.G. and Das, M.N. (1965). “On the construction and analysis of
some confounded asymmetrical factorial designs.” Biometrics 21, 948-56.
12. Shah, B.V. (1960). “On a 5x2^ factorial design.” Biometrics 16, 115-18.
13. Yates, F. (1935). “Complex experiments.” Sup pi. J. Roy. Stat. Soc. 2,

181-247.

14. Yates, F. (1937). “The design and analysis of factorial experiments.” Imperial

Bureau of Soil Science Tech. Comm. 35.

CHAPTER 5

Incomplete Block Designs

5.1 Varietal Trials

We pointed out in Chapter 2 that mainly three types of experiments
require statistical designing. These are factorial experiments, varietal trials
and bio-assays. The designs for factorial experiments have already been
discussed in Chapter 4. In the present chapter we shall discuss appropriate

designs for varietal and other similar trials.

Varietal trials are primarily agricultural experiments. The object of
these trials is to select through experimentation over a number of varieties
of a crop, a few varieties which are better than the rest in respect of
some economic character. An appropriate experiment for the purpose
consists of growing the varieties on field plots according to a suitable
design and then recording the character under consideration. If the
number of varieties is small, say, below ten, ordinary randomized block
designs or sometimes latin square designs can be used for the trials. But,
often, the number of varieties in such trials is large. Therefore, adoption
of randomized block designs may result in an increase of error variance
due to larger block size. The randomized block or latin square designs
are not, therefore, suitable for varietal trials when the number of varieties

is large.

We have seen that in factorial experiments when the number of treat¬
ment combinations is large, the device of confounding is adopted to
reduce the block size. This device ensures more precise estimation of
lower order interactions at the cost of some of the less important higher
order interactions which are confounded with blocks. A similar device of
reducing the block size is required in varietal trials as well. But because
the contrasts of interest are different in the two types of experiments, the
devices for reducing the block size cannot be the same for both. In varietal
trials comparisons of all possible pairs of varieties are required desirably
with the same precision. Therefore, no contrast can be completely
confounded with the blocks as in factorial experiments. The development
of designs with reduced block size to suit varietal trials, has been discussed
in Section 5.2.

Just like varietal trials there are also other types of experiments in
which the objective is to compare pairs of treatments with equal or nearly
equal precisions. The design requirements for all such experiments are

-INCOMPLETE BLOCK DESIGNS

153

the same. We shall, therefore, discuss the designs for all such experiments
in a general way. The term “treatment” will accordingly be used in
place of “variety”.

5.2 Incomplete Block Designs

We have seen that the precision of the estimate of a treatment effect
depends on the number of replications of the treatment. That is, the
larger is the number of replications, the more is the precision. A similar
thing holds for the precision of the estimate of the difference between two
treatment effects. If two treatments occur together in a block, then we
can say that these are replicated once in that block. Similarly, if there
are, say, p blocks in a design in each of which tl\e two treatments occur
together, then the pair of treatments is said to be replicated p times
in the design. It can be seen that the precision of the estimate of the
difference between two treatments depends on the number of replications
of the two treatments. This consideration has been exploited to construct
designs for varietal or similar trials with larger numbers of treatments so as
to reduce the block size.

If in a block the number of units or plots is smaller than the number
of treatments, then the block is said to be incomplete and a design
constituted of such blocks is called an incomplete blocks design. Let v
denote the number of treatments in an experiment and k, which is less
than v, denote the number of plots in each of the blocks of the design
for the experiment; k is also called the block size of the design. In order
to ensure equal or nearly equal precision of the comparisons of different
pairs of treatments, the treatments are so allotted to the different blocks
such that each pair of treatments has the same or nearly the same num¬

ber of replications and each treatment has an equal number of repli¬
cations, say, r.

Different patterns of values of the numbers of replications of different
pairs of treatments in a design, have given rise to different types of
incomplete block designs. When the number of replications of all pairs
of treatments in a design is the same, then an important series of designs
known as balanced incomplete block (B.I.B.) design is obtained. This series
of designs ensures equal precisions of the estimates of all pairs of treatment
effects. It was first devised by Yates (1936) for agricultural experiments.
These designs have evidently some constructional problems because the
allotment of k of the v treatments in different blocks so that each pair of
treatments is replicated a constant number of times is not straight-forward.
The constructional problems were solved by the joint efforts of Fisher and
Yates and Bose (1939) among others. While Fisher and Yates being in
touch with the experimental scientists were, restrained in their efforts to
obtain new designs and new analytical techniques by the requirements of
the experimenters, Bose concentrated more on the methods of construction

154

DESIGN AND ANALYSIS OF EXPERIMENTS

of the balanced and other incomplete block designs and was not necessarily

constrained by the considerations of practical utility.

The various constructional and analytical methods of the incomp e e-

block designs have been discussed separately in the subsequent sections.

It was found that the balanced incomplete block designs were not
always suitable for varietal trials because these designs require large
numbers of replications and further, suitable designs are not available tor
all numbers of treatments. To overcome such difficulties Yates (193 )
evolved a series of incomplete block designs which he called lattice designs.
Subsequently, Bose and Nair (1939) evolved another type of incomplete
block designs which they called partially balanced incomplete block

(P.B.I.B.) designs. . . ,
One type of lattice designs is available for numbers of varieties which
are perfect squares. These are, therefore, called square lattice designs.
These can accommodate a flexible number of replications beginning with
two. The number of replications of pair of treatments is one for certain
pairs and zero for others. These designs are actually a type of confounded
symmetrical factorial designs involving two factors as we shall see after¬
wards. Likewise, there are lattice designs corresponding to confounded
symmetrical factorial designs involving three factors. These are called
cubic lattice. As these designs fellow from factorial designs these are

also called quasi factorial designs. .

The partially balanced incomplete block designs are available with
smaller numbers of replications for many more numbers of treatments. The
number of replications of pairs of treatments in these designs is not
constant. These were defined in general for m types of replications of the
different pairs of treatments where m is any integer. That is, in these
designs some pairs of treatments can be replicated, say, \ times, some
others A2 times and so on up to m such type s of pairs. From considera¬
tions of analysis of these designs, they have to possess some more
properties as well. These are taken care of by defining some more

parameters which we shall discuss subsequently.

In order to make incomplete block designs available for all number of
treatments with smaller numbers of replications two more series of
incomplete block designs were defined. These are re-inforced incomplete
block designs (Das, 1958 and Giri, 1958) and circular designs (Das, 1958).
The re-inforced incomplete block designs are actually augmented in¬
complete block designs and are obtained by including in each block of
any usual incomplete block design a certain number of additional treat¬
ments, say, a so that the block size becomes k+a and the number of
treatments v+a. By suitably choosing v and a any numbers of treatments

can be accommodated in such designs.

Circular designs are a particular type of P.B.I.B. designs which are avail¬
able for any number of treatments. They have no constructional problems.
When the block size is 2 or 3, their analysis is also not complicated. For v

INCOMPLETE BLOCK DESIGNS

155

treatments and block size ti, these are obtained by developing the initial
block 1,2,3, n mod v.

Even before Yates used the B.I.B designs for agricultural experiments,
some of them were known in combinatorial mathematics in the form of
groups possessing special properties. Bose exploited the group properties
for the construction of these designs. Since then considerable amount
of work has been done in the name of incomplete block designs.
But, it seems, much of these activities has very little to do with designs
required for actual experiments. They are more curiosity guided than
problem oriented. The present activities have penetrated much into
combinatorial mathematics and are, therefore, more concerned with group
properties rather than problems of precision or availability of designs
to suit particular experiments.

We have so far tried to view the incomplete block designs from the
angle of precision as related to the replication of pairs of treatments. But
actually, analytical considerations have played a greater role in the
development of various incomplete block designs. From incomplete
block designs we get two-way data classified according to blocks and
treatments. If there are b blocks in a design with v treatments and k as
block size, then there are b xv cells in the two-way table with frequencies
0 or 1. Since k of the v treatments occur in a block, the frequencies in
the k corresponding cells in the row for the block, are unity and those in
the remaining cells of the row are zero. The data obtained from such
designs are, therefore, non-orthogonal. The b X v cell frequency table is
called the incidence matrix of the corresponding design, As the cells can
take two values 0 or 1 these designs are called binary designs.

While obtaining the method of analysis of non-orthogonal data in
Chapter 1, we have seen that the analysis involves the solution of as many
reduced normal equations as the number of treatments. In balanced
incomplete block designs, these equations take the form

V

cjf,-+c2 2 tm=Q> (z= l,2,...,v)

1

So, taking the restriction 2 tm=0, the solution of these equations becomes

very easy.

m

While evolving new designs similar simplicity of the solutions of the
normal equations has also been kept in view along with the other
considerations discussed previously. A further consideration that is kept
in view is that all the treatment effects should be estimable as deviates
from their means. This in turn implies that the reduced normal equations
should be solvable taking one additional restriction among the treatment
effects. Usually, this criterion is called “connectedness” of the design.
If a design is not connected, all the (v— 1) mutually orthogonal contrasts
of the v treatments effects cannot be estimated. Hence, it is necessary to
know if a design is connected before it is recommended. Efforts have,.

156

DESIGN AND ANALYSIS OF EXPERIMENTS

therefore, been made to ascertain if a design is connected by examining
its blocks. Bose (1943) in his unpublished class notes gave the following

method.

If for every pair of treatments a and b, it is possible to get other
treatments alt a2,...,an such that every pair of consecutive treatments

in the series a, ax, a2,..., a„, b occurs in some block or the other of a

design, then the design is connected.

The criterion of connectedness can be viewed from the following
convenient angle also. If all the blocks in an incomplete block design
can be divided into two groups of blocks such that none of the treatments
present in one group, is present in the other group, then the design is
disconnected. The concept of connectedness is thus analogous to

complete confounding in factorial designs.

We shall restrict ourselves to a discussion of the more important
incomplete block designs in respect of their definition, analysis and usual
methods of construction and omit a discussion regarding various
combinatorial properties which have no immediate relevance with

experimentation.

5.3 Balanced Incomplete Block Designs

An incomplete block design with v treatments distributed over b blocks,
each of size k, where k is less than v such that each treatment occurs in
r blocks, no treatment occurs more than once in a block and each pair of
treatments occurs together in A blocks, is called a balanced incomplete
block design (B.I.B.). The symbols v, b, k, r and A are called the
parameters of the design.

Example 1: A balanced incomplete block design with parameters

v=9, 6=12, k=3, r= 4 and A=1

The treatments are numbered from 1 to 9. The contents of the blocks

are shown below.

Blocks

Contents

Blocks

Contents

1

2

3

4

5

6

1 2 3

4 5 6

7 8 9

1 4 7

2 5 8

3 6 9

7

8

9

10

11

12

1 6 8

2 4 9

3 5 7

1 5 9

2 6 7

3 4 8

Evidently, the parameters satisfy the following relations.

INCOMPLETE BLOCK DESIGNS

157

vr=6fc=total number of plots in the design (5 i)

Mv_ l)=r(&—l)=total number of replications of all possible

pairs of treatments in each of which a

particular treatment is always present. (5.2)

It was observed by Fisher (1940) that even though parameters satisfying
the above relations are available, a corresponding design may not be
available. In search of a criterion for the availability of B.I.B. designs,
he proved that no design with parameters 6 < v is possible. He proved
this result as below.

Suppose a B.I.B. design with the parameters v, b, r, k, A. is available.
Let one of its block be singled out. Let this block contents be denoted
by B0. Let xt be the number of treatments common between B0 and the
/th block when the blocks are arranged in some order (/=!, 2,..., 6—1).

Evidently,  2 Xi~k (r—1)
/=i

(5.3)

because each of the k treatments in B0 occurs (r— 1) times in the
remaining (6—1) blocks.

Again, 2 j)_ k{k — 1)(A— 1)

/ 2 2

(5.4)

=the total number of replications of

pairs of treatments formed of the k treatments in Bv in the remaining
(6—1) blocks.

From (5.3) and (5.4) we get

2x,a=A:(r— \)+k(k—1) (A— I) (5.5)

The corrected sum of squares of the x,’s is given by

s.s. (x)=2x,2—{2x,}2/(6— 1)

/ i

=&(r—1)+&(k—1)(A—1)—&2(r—1)2/(6—1)

(5.6)

~(r—k) (r-A)(v-k)/(6—1)

after simplification subject to (5.1) and (5.2).

Being sum of squares of deviates, (5.6) is evidently zero or positive.
But since (r—A) and (v—k) are necessarily positive, (r—k) must be zero
or positive.

Since 6/v=r/A:, we get 6 > v.

When (5.6) is zero, all the x/s are equal. This also makes r=k or 6 = v.
A much simpler and more elegant proof of the result 6 ^ v which makes
use of the incidence matrix N of the design is as follows. It is easy to
observe that for a B.I.B. design N'N=(r—A)/,+A£W so that |N'N\—
(r+A(v—1)} (r—A)?-1=rAr(r—A)*-1 # 0. This means that N’N is non-

158

design and analysis of experiments

singular and hence of rank v. But rank (NW)=rank (JV)< b. This
proves that b > v. Even a sharper inequality b^v+r-k is true. This

follows from the fact that (£_l) (r-*)>0 which implies ~-v > r-k

i q, b ^ v-\~k k.

The class of designs in which b = v is called symmetrical B.I.B. designs.
In these designs, therefore, the number of treatments common between

any two blocks is constant.

Since, 2xi=k(r— 1) the value of this constant is

7 ' *(r-l) r{k-1)_,
b~\- b-1 “ b-1

because in these designs r=k and b=v. It is found that many designs
where b is greater than v are impossible. For example, the design with
the parameters v =36, b = 42. r=l, k = 6 and A=1 is impossible. Many
more designs where b ^ v have since been proved impossible. A sufficient
condition for the availability of B.I.B. designs is yet to be found. The
designs which are impossible or unsolved have been pointed out in the
tables for such designs as indicated in the next paragraph.

5.4 Construction of B.I.B. Designs

There is no single general method for the construction of all balanced
incomplete block designs. There are specific methods for specific series
of designs. Solutions of many designs are not yet known. The
solutions of all known designs indicating impossible designs have been
tabulated by Fisher and Yates (1948), Rao (1961) and Sprott<1962). We
have given below the methods of construction of some of the more
common series of B.I.B. designs.

5.4.1 B.I.B. Designs with Parameters v,b=—~a—,k—2, r=v—1, A=1

The block size in this series of designs is 2. All non-repeated designs with
Jc=2, belong to this series. They are constructed easily when all possible
combinations of v treatments taken two at a time are used as blocks.

By repeating p times the b blocks of a B.I.B. design with parameters
v, b, r, k and A, another B.I.B. design with parameters v, pb, k, pr, p\ is
obtained. Such designs are called repeated designs.

The above series of designs with k=2, is suitable when vis not very
large because it requires v—1 replications which for large v may be
prohibitive. When twin calves or litter mates are used as blocks for
testing a smaller number of treatments, these designs are more suitable.

This method of construction can be extended to construct designs

with parameters

INCOMPLETE BLOCK DESIGNS

159

v, k, b=vCk, r—v-1Ck-1, A=v-2c*_2

It is obtained by taking all possible combinations of v treatments
taken k at a time as the possible blocks. This series has the same drawback
that even for small v it requires a large number of replications.

5.4.2 Construction of B.I.B. Designs with Parameters

v=52, b=s2+s,k^s, r-5-{-l, A=1 (5.7)

When s is either a prime or a prime power, the above series of designs
can be obtained by first forming a finite 2-dimensional Euclidean geometry
by using the elements of G.F. (s) and then treating the points as treatments,
all possible lines as blocks, and the points on a line as the contents of
the block corresponding to the line. This method is illustrated below by
taking 5=4.

Example 2: Construction of B.I.B. design with parameters corresponding
to 5=4, that is,

v=16, b—20, k== 4, r—5, A=l.

The elements in the Galois fields with four elements are 0, 1, a, a2 with
a2+a+l as the minimum function. There are 16 points in the 2-dimen¬
sional Euclidean geometry which can be written using these elements. The
following 16 possible pairs (x, j) formed of these elements (*, >’=0, 1, a, a2)
give the 16 points:

Point no. 1

Points 00

Point no. 9

Points a0

2

01

10

al

3

0a

11

aa

4

Oa2

5

10

6

11

7

la

8

la2

12

aa2

13

a20

14

a2l

15

a2a

16

a2 a2

The equations of the possible lines are
(1) x=i (i=0, 1, a, a2). That is,

x=0

x=l

X=a.

x=cc2

(2) y=i
(3) x+y~i
(4) x + aty=i
(5) x+«*y=i

160

DESIGN AND ANALYSIS OF EXPERIMENTS

Thus there are five sets of lines with four paraUel lines in each set.

There is no common point in any two lines belonging to a set.

In general, there are (5+1) such sets of lines each set containing

s parallel lines. So the total number of lines is 5(5+1).

The number of points in a line, say,

x+py=i (5.8)

is 5, where p and / are two elements in the Galois field. That is because
for each value of x in the field, one value of y is obtainable from (5.8+
These two values of x and y give a point on the line (5.8). As x can
be any of the 5 elements in the field, there are in all 5 such points on
the line.

Given a point there is one line in each set which passes through the
point. As there are (5+1) sets, (5+1) lines passes through a point. Hence
the replication of each variety is 5 + 1. As only one line can pass through
two points, a pair of treatments occurs in one block only. That is, A=l.

The points on the 20 lines of Example 2 obtained as indicated above
are shown below. Only the point numbers have been shown (not the
coordinates of the points).

Block  no. Contents

Block no.  Contents

Block  no.  Contents

1

2

3

4

5

6

7

8

1

2

3  4

9 1  6

11

5  6  7

8

10 2  5  12

9  10  11  12

11 3

8

9

13  14  15  16

12 4  7

10

16

15

14

13

17

18

19

20

1

8 10 15

2  7 9 16

3  6 12 13

4  5 11 14

1

5

9  13

13 1

2  6  10  14

14 3

7

5

12  14

10  16

3  7  11  15

15 4  6

9

4

8  12  16

16 2

8

11

15

13

When  5=6, no Galois field exists. Hence, the design  for 5 =6, v=36,
b=42, r=7, k—6, A=1 is not obtainable by this method. Actually, it
has been shown that this design is impossible.

By taking 5+1 more treatments and by putting the ith of these
treatments (when arranged in some order) in each of the 5 blocks in the
rth set of blocks, (1= 1,2,. ., 5+1) we get 52+5+1 treatments distributed
over 52+5 blocks each of size 5+1. These blocks together with another
block formed of the new (5 1) treatments give a series of symmetrical
B.I.B. designs with parameters

v=Z>=52+5+1, r=fc=5+l, A = 1 (5.9)

Evidently, each of the new treatments occurs in(5+l) blocks and each
of them occurs with each of the previous treatments in a block only once.

INCOMPLETE BLOCK DESIGNS

161

because each of the previous treatments is present once only in the s
blocks, in each of which a new treatment is put.

By the reverse process, viz. by taking out a block from any symmetrical
B.I.B. design with parameters v=b, r=k, A and then omitting all treat¬
ments in that block from all other blocks of the original B.I.B. design,
another B.I.B. design with the following parameters is obtained:

v'—v—k, b'=b—1, r'—r, k'=k—A, A'=A

As any two blocks of a symmetrical B.I.B. design have A treatments in
common, so from each of the b—1 blocks only A treatments are omitted
and hence the block size in the resultant design is k—A.

If, again, blocks are formed each with A treatments which are omitted
from each block as indicated above, then another series of B.I.B. designs
with the following parameters is obtained:

v"=k, b"=b-1, r"=r—1, k"=A, A"=A-1.

Resolvable Designs
It has been seen that the blocks of the designs

v=s2, b—s2-\-s, r—s-\-1, k—s, A—1

can be divided into (j+ 1) groups of s blocks each, such that in each group
each of the treatments is replicated once. Designs for which this type of
grouping of the blocks is possible are called resolvable designs. If, again,
the number of treatments common between any two blocks belonging to
two different groups of a resolvable design is constant, then such designs
are called affine resolvable designs.

It can be shown that for resolvable designs no solution exists if

b < v—r+1.

The proof follows exactly the same line as adopted for showing b > v.

5.4.3 An Alternative Approach for Construction of

B.I.B. Designs

The procedure of construction of the two series of designs at (5.7) and
(5.9) and their generalization can also be viewed from a different angle.
If the s2 treatments are taken as the s2 treatment combinations of two
factors each at s levels, then all the blocks each of size s obtained in
different replications by confounding each of the main effects and inter¬
actions once, give the series of balanced incomplete block design at (5.7).
In general taking sn treatment combinations of n factors each at 5 levels
as the treatments, all possible blocks each of size j' obtained by confounding
in different replications each of the main effects and interactions an equal
number of times, form a series of balanced incomplete block design. This
series corresponds to that obtained by Bose (1939) from the n-dimensional

Euclidean geometry.

162

DESIGN AND ANALYSIS OF EXPERIMENTS

In the above factorial set up if all the interaction components, which
can be written by always taking the first letter with power unity, are used
to denote the treatments and the interaction components which are con¬
founded to get a replication for any given block size, are taken as the
contents of a block, then all the blocks corresponding to all possible
replications having the same block size, form a series of balanced incomplete
block designs. This series is the generalization of the series at (5.9). Bose
(1939) got this series by using projective geometry.

In particular, when n=3, there are (a-3— 1)/(a-— 1)=5-2-|-a--4- 1 interactions
of the type indicated above. If these interactions are confounded taking
two independent interactions at a time, there are in all

/a3 — 1 \ Is3—l

ls2—l\ /s* — 1

=(j'2+j-f-i)

possible ways of choosing two interactions such that each choice generates
a separate replication. Hence, the number of blocks is The
block size is evidently (a2-1)/(j-1)=(a+1). The number of replications
of the factorial in which a particular interaction is always confounded is

(s2— 1)A>— 1)=CH-1), because given one interaction, a second interaction
can be chosen in (s2- 1)/(a— 1) ways. Similarly, A==(a — 1)/(a—1)=1. This
method was given by Kempthorne (1952).

5.4.4 Construction of B.I.B, Designs by Developing Initial

Blocks

Let the v treatments in a B.I.B. design be denoted by the elements of
mod v. Let Xj, a2,...,Xk be the contents of an initial block where
*i. ... ,Xn are the elements of the module. By taking all possible
differences, two by two, of the k elements in the initial block we get
k(k 1) such differences. Let among these differences each of the non¬
zero elements bf mod v occur a constant time, say^ A. Then by developing
the initial block mod v, a symmetrical balanced incomplete block design
with parameters

is obtained.

v=b, k=r, A

By developing an initial block mod v, we mean getting other blocks
from it. The first block is obtained by adding unity to each element of the
initial block mod v and taking these sums as the contents of the block.
Next, from this block another block is obtained in exactly the same way
by which the first block was obtained from the initial block. This process
is repeated till v blocks including the initial blocks are obtained.

Example 3: Taking the elements of mod 13

as the treatments let

INCOMPLETE BLOCK DESIGNS

163

0, 1, 3, 9 form an initial block. The differences, mod of these elements
two by two are shown below.

0

1

1

12

3

3

10

2

11

9

9

4

8

5

6

7

It is seen that among the above 12 differences each of the non-zero
elements of mod 13 occurs once. Hence, by developing this block mod 13
asymmetrical B. I. B. design with parameters v=6 = 13, r=k=4, A=1 is
obtained. The actual design is shown below:

Blocks

Contents

1

2

3

4

5

6

7

8

9

10

11

12

13

0

1

2

3

4

5

6

7

8

9

10

. 11

12

1

2

3

4

5

6

7

8

9

10

11

12

0

3

4

5

6

7

8

9

10

11

12

0

1

2

9

10

11

12
0

1

2

3

4

5

6

7

8

The Rationale Behind the Method
If the difference between two elements in the initial block is, say, d,
then when the block is developed to get other blocks, all possible pairs of
elements which differ by d occur together in the different blocks. If
there are A pairs of elements each giving a difference d, then all possible
pairs of numbers differing by d occur together in the different blocks A
times. Now, the initial block is so chosen that d takes each of the values
from 1 to v—1 equally often. Hence, all pairs of numbers occur together
equally often in the different blocks of the design. This ensures constancy
of the number of replications of pairs of treatments.

164

DESIGN AND ANALYSIS OF EXPERIMENTS

Construction of B.I.B. Designs of the Series

v=6=4A+3, r=k=2k-\-\, A (5.10)

If 4A+3 is a prime or a prime power, then the initial block formed
of the even powers of the primitive root * of G.F. (4A+3) gives the above
series of B.I.B. designs. The odd powers of the primitive roots also form
another initial block which gives the same design. It can be verified that
among 2A(2A+1) differences between the even powers of x, each of the
non-zero elements of G.F. (4A+3) occurs A times.

When 4A+3 is a prime power, the initial block is developed by adding
in turn each of the different non-zero elements of the field to the elements
of the initial block.

Example 4: The design v—b= 11, r=k=5, A=2 is obtained by develop¬
ing the initial block formed of the even powers of 2 which is the primitive
root of G.F. (11). The initial block is then

The actual design is shown below.

1,4, 5, 9, 3

Blocks

Contents

1

2

3

4

5

6

7

8

9

10

0

4

5

6

7

8

9

10

0

1

2

3

5

6

7

8

9

10

0

1

2

3

4

9

10

0

1

2

3

4

5

6

7

8

4

5

6

7

8

9

10

0

1

2

Case of p Initial Blocks

Instead of taking one initial block a number of, say, p initial blocks can
also be taken. From each of these blocks A: (£-1) differences are obtained.
If among lhspk(k-\) differences obtained from all the p blocks, each of
the non-zero elements of the concerned field occurs say, A times, then by
developing these p blocks a B.I.B. design with the following parameters is
obtained:

v, b=pv, k, r—pk, A.

INCOMPLETE BLOCK DESIGNS

165

Case of p Initial Blocks with Elements from Different Fields
of the Same Size
Let xv x2, ..., xY denote v elements of a field. Let these elements of the
field be repeated n times such that x'2, .. .,xv‘ (/— 1, 2, .. ,,ri) denote

the elements of the ith field, G.F. (v).

The differences of the type x'm—x1,^ are called pure differences and can
take as value any of the non-zero elements of G.F. (v), that is, x2, x3,..xv,

assuming that xx=0.

The differences of the type xlm—Xm(if^i') are called mixed differences

and can take all the values of the field including 0.

Let there be p initial blocks framed of the elements of all the n fields.
From these blocks pk(k—1) differences are obtained. Some of these
differences are pure and the rest mixed. If among the pure differences
each of the non-zero elements x2, x3,..., xv occurs an equal number of
times, say, A and among the mixed differences each of the elements
Xj, xz, . ..,xv also occurs A times, then by developing these initial blocks
a B.I.B. design with the following parameters is obtained.

v'=nv, b=pv, k, r=— , A.

pic
n

Here, all the elements from the n fields are taken to denote the nv

treatments.

Some Derived Designs
Let pv pa, ..., p6 denote the contents of b blocks of a balanced incomplete
block design with parameters, v, b, k, r and A. From the block
pi (j=l, 2, ..., b) another block p/ can be obtained by including in it all
those (v—k) treatments which do not occur in (3/. The design formed
with Pi, P2', .,Pa' as blocks is a B.I.B. design with the following

parameters:

—v, b'=b, k'—v—k, r'—b—r, \'—b—2r-}-A

This design is called the complimentary design to the one with

parameters v, b, r, k, A.

In the complimentary design the numbers of treatments and blocks
evidently remain unchanged. As any treatment occurs in r block of the
original design, so must it occur in the remaining b-r blocks of the

complimentary design.

Given two treatments 6 and <£, (i) both of them occur together in A
blocks of the original design (ii) 0 occurs alone in r—A blocks (iii) <f> occurs
alone in r-A blocks and (iv) both of them do not occur in A' blocks.

Since all these four cases exhaust all the blocks,

A+(r—A)+(r A)-j-A =b.

That is, A'=6—2r-j-A.

The complimentary designs of the series

v=&=4A+3, r=A:=2A-f 1, A

166

DESIGN AND ANALYSIS OF EXPERIMENTS

have the following parameters

v'=b’=4X+3, r'=k'=2A+2, A'=A+1.

Dual Designs
Let 0l5 02, .. .,0„ denote the treatments in a B.I.B. design with b blocks.
Let the blocks be numbered by 1,2, ..., b. Any treatment 0/ (i= 1, 2,..., v)
occurs in r blocks. Let a block (3/ be formed with these r block numbers.
Then the design with the blocks (3j, (i2, ..., (3„ is called the dual design of the
original B.I.B. design. The parameters of the design are v'= b, b'—v, r'=k,
k'—r. The resultant design is not, however, a B.I.B. design always. If
the original design is a symmetrical B.I.B. design, then the dual design is
also a B.I.B. design with the same parameters.

5.5 Analysis

It has been pointed out earlier that the data obtainable from incomplete
block designs are non-orthogonal. They are, therefore, analyzed by
following the method of analysis of non-orthogonal data described in
Chapter 1. The method as appropriate for B.I.B. designs is discussed
below briefly.

The incidence matrix of a B.I.B. design is of the following type.

TABLE 5.1

Incidence Matrix of B.I.B. Designs

Treatments
1 2 3 .

. V

Total block size
n.j

Block Total

Block

1

2

3

1

0

1

0

0

1

1 .  .. 0

1 .  .. l

1 .  .. 0

b

0

1

0 .  .. I

k

k

k

k

Bx

b2

b3

Bb

Total

no. of rep. (n4.) r r r ... r

Observation total Tx Tt T3 ... Tv

Adjusted total

01 0S 03 •• • Qv

INCOMPLETE BLOCK DESIGNS

167

Qi=Ti-\ 2 n,jBj (1=1, 2,..v)

AC J

where nu denotes the entry in the above table in the cell defined by the ith

treatment and j'th block.

The reduced normal equations obtainable from the model

are as follows

\ k) k m7it

2 (5.11)

Taking the restriction 2 tm—0, the solutions of the treatment effects are as

follows:

m

f,=gwherc£=^1(i=1.2,....v).

The adjusted sum of squares of the treatment is

s uq,=~e 2 e<*.

Next, the following analysis of variance table is prepared.

TABLE 5.2

Analysis of Variance of B.I.B. Designs

Sources of
variation

Block
(unadjusted)

Treatments
(adjusted)

Error

Total

d.f.

s.s.

m.s.

t

V

b-1

v—1

f k

4rS Qi*
rE "

vr—b—v+1

By subtraction

St2

s2

vr-I

2T«2

The variance of the estimate of the contrast 2 i,t, is given by

where c2 is estimated by the error mean square, j*. This design is called
balanced because the variances of the estimates of all elementary treatment

contrasts like (ti—tm) ure all equal.

168

DESIGN AND ANALYSIS OF EXPERIMENTS

The efficiency of the design as compared to randomized block design is

2<tv2

rE

where cr„2 is the error variance from a randomized block design with v as
block size and a- the error variance from B.I.B. designs with k as block
size.

The ratio 0„2)/a2 is expected to be greater than unity while E is less
than unity as shown below. If the product Ex(<jf)/a2 is greater than
unity, then the B.I.B. design is more efficient than the corresponding
randomized block design. E does not indicate the real efficiency of a B.I.B
design but is only a factor in the efficiency. It is, therefore, called the
efficiency factor of the design.

We have

v’A v(k—1)
rk k (v—fj

because-=

r

k— 1
"v-1

k— 1
k
'El
V

< 1 since k < v.

An Alternative Method of Analysis of B.I.B. Designs
The B.I.B. design can also be analyzed by first obtaining the deviations of
each observation from its block mean. Treating these deviates as if they
are from a completely randomized design, the treatment sum of squares
and the total sum of squares are obtained from them by following the
usual method. Denoting this treatment sum of squares by (Tr.S.S.)^ and
the total sum of squares by (T.S.S.)^, the adjusted treatment and error
sums of squares are obtained as below.

Adjusted treatment s.s.=——S-S-)n

E

Error s.s.=(T.S.S.)0-(Adj. Treat. S.S.)

5.6 Analysis with Recovery of Inter-Block Information

In all incomplete block designs there are two types of blocks. One type
of blocks consists of sets of k treatment numbers. Another type of
blocks are the actual blocks, each consisting of a set of k experimental
units. We shall call the two types of blocks as treatment blocks and unit

The randomization procedure in incomplete block designs consists of
first allotting the treatment blocks to the unit blocks at random. Then

INCOMPLETE BLOCK DESIGNS

169

the treatments thus allotted to a unit block are distributed at random to
the different units in the unit block.

Thus, if a poor set of treatments happen to be allotted to a unit
block, the effect of the block will appear to be small. If, again, a good
set of treatments happens to be allotted to the same block, its effect will
appear better. Hence, as the treatment sets are allotted to the blocks at
random, the block effects can be considered to be random variables. But
in the previous analysis, called intra-block analysis, the block effects were
taken to be fixed. Soothe same data can be analyzed taking the block
effects as random. The corresponding method of analysis is called analysis
with recovery of inter-block information. This method is due to Yates
(1940). We shall discuss this method in general for incomplete block
designs in Section 5.11.

Example 5: The method of analysis of a B.I.B. design has been illustrated
below with actual data.

A varietal trial involving 13 varieties of wheat crop was conducted in
an agricultural college in U.P. India. A balanced incomplete block design
with the following parameters was used for the trial

v=b —13, r—k=4, A= 1

The layout-plan, showing the contents of the different blocks and the
plot yields in kg. per plot of size l/20th of an acre are shown in Table 5.3.
The deviate of each observation from its block mean is also shown along
with the observations.

Layout and Yield from the B.I.B. Design v=b~13, r=k=4, X=1

TABLE 5.3

Block numbers

1
(2)

2

3

4

5

(3)

(1)

(2)

(3)

(1)

(2)

(3)

(1)

(2)

(3)

(1)

(2)

(3)

50

1

39 - -10

58

49

9

0

3

4

8

45  —3

10

31 - -15

38  —10

65

17

37 - -9

17

2

5

8

54

54

1

1

70

17

7

8

9

12

44  —4

7

11

34  —19

10

47 - -11

60

61

64

2

3

6

(1)

3

6

9

11

Total
Mean

196
49

192
48

212
53

232
58

(1) Content

(2) Yield

(3) Deviation

11

12

13

63

53

184
46

170

DESIGN AND ANALYSIS OF EXPERIMENTS

Block numbers

6

(2)

(1)

(3)  CD

7

(2)

(3;

(1)

8

(2)

(3)

(1)

9
(2) (3)  0)

10

(2) (3)

4

5

6

60  —1

65

4

54  —7

1

5

9

69

'62

8

1

52  —9

3

5

7

68

0

65  —3

66  —2

1

2

3

77 7

65 —5

75 5

2

4

9

57 —3

60 0

53 —7

10

65

4

12

61

0

13

73

5

10

63 —7

13

70 10

Total
Mean

244
61

244
61

272
68

280
70

240
60

Block numbers

(3) (1)

12
(2)

(3)

(1)

9 1

—1 6

—1 8

—7 13

63  —4

67

0

54  —13

84

17

2

6

7

12

li
(2)

72

62

62

56

a)

i

4

7

11

Total
Mean

252
63

268
67

(3)

—3

—1

15

—11

13
(2)

61

63

79

53

256
64

The treatment totals as obtained from the deviates are  shown below.

Treatments

Total

1

20

2 3 4

5

6 7

8 9

10

11 12  13

-10 3 -12  3 - 18 1

23 -4

-12

-35 2  39

Incidentally, the above totals are also the adjusted totals of the treatments.
Taking each total to be based on four observations the treatment sum

of squares=1106.5

The efficiency factor

Hence, the adj. treat.

=11
16

s.s. =-

1106.5x16
13

= 1361.85

INCOMPLETE BLOCK DESIGNS

171

Total sum of squares of the deviates=3596
So the error sum of squares=3596 —1361.85=2234.15
Uncorrected block s.s. (unadj.)= 184466.

The final results are presented in the following analysis of variance

table.

Analysis of Variance of the B.I.B. design v=6=13, r=&=4, A=1

Table 5.4

Sources of variation

d.f.

s.s.

m.s.

F.

Blocks unadjusted

Treatments (adj.)

Error

12

12

29

184456.00

1361.85

2234.15

113.49

77.04

1.4*

Total . 53 188052.00

*not significant

The total sum of squares has been obtained by addition. The variance of
the estimate of the difference between two treatment effects is

2x77.04 4x2x77.04

rE

13

=47.41

The grand mean of all observations—^  -59.1

3072

The estimates of the treatment effects obtainable from

are as below

Treatments

1

2

3

4

5

6

7

Estimates

6.2

-3.1

0.9

-3.7

0.9

-5.5

0.3

Estimates+grand mean  65.3

56.0  60.0

55.4  60.0

53.6

59.4

Treatments

8

9

10

11

12

13

Estimates

7.1

-1.2

-3.7  -10.8

0.7

12.0

Estimates+grand mean  66.2  57.9  55.4

48.3

59.8

71.1

172

DESIGN AND ANALYSIS OF EXPERIMENTS

The relative performances of the varieties can be assessed better from the
■estimates increased by the grand mean as presented in the last row.

5.7 Youden Squares

Like a latin square design a Youden square is an incomplete block design by
means of which two sources of variation can be eliminated. These are
basically symmetrically balanced incomplete block designs by which the
block to block variation can be eliminated. The k units in each block can
be thought of occupying k different positions. With the help of Youden
square design the effects of such positions can also be eliminated.

The k units in each block of a symmetrical B.I.B. design can always be
so arranged that each treatment occupies each position once in some block
or the other. When a symmetrical B.I.B. design is obtained by developing
an initial block such an arrangement is evident.

The position effects are evidently orthogonal to the treatments as eacn
treatment occurs once in each position. The position effects are similarly
orthogonal to the blocks as well. Hence, the analysis of Youden squares
is the same as that of B.I.B. designs excepting that a component of the sum
of squares obtained from the position totals of the observations is
subtracted from the error sum of squares of the B.I.B. design.

These designs were used for the first time by Youden (1940) for green

house studies.

The possibility of obtaining Youden squares from symmetrical B.I.B.
designs was proved by Smith and Hartley (1948). The Youden squares
can also be looked upon as an incomplete vxv latin squares with k suitably
chosen columns. If a column or a row is omitted from a latin square,
the resultant design is always a Youden square.

5.8 Lattice Designs

One drawback of balanced incomplete block designs is that suitable
designs are not available for all numbers of treatments. The number of
replications required in these designs is usually large and does not always
suit the convenience of the experimenters. Efforts were therefore made
to evolve designs with smaller number of replications. With this end in
view Yates (1936), evolved a series of designs which are available for all
numbers of treatments which are perfect squares. The numbers of
replications of the treatments are flexible in these designs. These designs
are obtained as below.

Let there be k2 treatments numbered by 1,2,3,...,k*. Let these
treatment numbers be arranged in the form of a kxk square. The
contents of each of the k rows of this square are taken to form a block.
Thus, k blocks are obtained from k rows. Similarly, taking the contents
of the columns to form blocks, another k blocks are obtained.

INCOMPLETE BLOCK DESIGNS

17$

A latin square of order k (arrangement with latin letters) is now taken
and is superimposed on the kY~k square written with the treatment
numbers. The treatment numbers which fall on a symbol of the latin
square are taken to form a block. Thus, from k symbols of the latin
square k blocks are obtained. Next, another latin square orthogonal to
the previous one is taken and is superimposed on the square. From this
latin square also, another set of k blocks can be obtained likewise.
Similarly, by using (m—2) mutually orthogonal latin squares of order
k,(m—2) k blocks are obtained where m^k—1. These blocks along
with the 2k blocks formed by the rows and columns of the arrangement
of the treatment numbers, give a lattice design with /c2 treatment, mk
blocks each of size k and m replications. This is called an m-ple square
lattice design. A square lattice design with two replications is called a
simple lattice and one with three replications, a triple lattice.

When k is a prime or a power of a prime by using all the (k— 1) mutually
orthogonal latin squares for obtaining the blocks as indicated above, a
lattice design in (&+1) replications is obtained. This is called a balanced
lattice. Balanced lattices are also balanced incomplete block designs
belonging to the series v=s2, 6=sa+.y, k—s+l, k=s, A=l. By taking
any two sets of blocks of the design in Example 2 in section 5.4.2a simple
lattice design for 16 treatments is obtained.

If the k2 treatments are coded by the combinations of the k2 factorial,
that is, the combinations of two factors each at k levels, then a con¬
founded design in blocks of size k obtained by confounding m main effects
and interactions in m different replications, gives an m-ple lattice design.
These designs are, therefore, also called quasifactorial designs. Extending
this analogy to factorials with three factors each at k levels, (k3 factorials)
two types of designs corresponding to block sizes k and k2 can be
obtained by adopting suitable confounding. These designs are called
cubic lattices.

5 8.1 Analysis

The data obtained from an m-ple square lattice design is non-orthogonal
and are, therefore, analyzed by the method of analysis of non-orthogonal
data described in Chapter 1. The incidence matrix of the design is shown
below along with the other parameters required for analysis.

174

DESIGN AND ANALYSIS OF EXPERIMENTS

TABLE 5.5

Incidence Matrix of m-ple Lattice Designs

Treatments
2 3..

. £2

Total block size
(n.j)

Block
totals

Block

1

2

3

mk

Total (Rep. «<.)

Treatment totals

1

1

0

1

1

0

1

0

1

0

•

.

. 1

. 1

. 0

0
m

n

0
1
m  m

T2

Tz

. . 1
m
Tk*

Qk*

Adjusted totals

Q\  Q,  Qz

Here, £7/=7) —^ 2 n,j B,

k

k

k

k

b3

Bmjc

where

Further,

ro, if the ith treatment does not occur in the /'th block,
(.1, if the /th treatment occurs in the 7th block.

2 nijnmJ=\1’ if the Ith and wth treatments occur together in a block,
j 11 mJ [0, if these two treatments do not occur together in a block.

The reduced normal equations come out as below.

km t>-SR (tt)-Sc (t,)-St (/,)-... -Sm (t,)=kQi

(1 —1,2,..., k2) (5.12)

where (i) SR (t,) is the sum of those treatment effects including /, which
occur in the row blocks of ith treatment, that is, the block
obtained from a row in the arrangement of the treatments in
which the /th treatment is present.

(ii) Sc (//) is similarly the sum of those treatment effects which

occur in the column block of tt.

(iii) sp (U) denotes the sum of those treatment effects which occur
in the block with the ith treatment obtained from the pth
orthogonal latin square (p = l, 2,...,m—2).

Writing an equation like (5.12) for each of the treatments in SR(t) and
adding these k equations we get

km SR {ti) -k Sr (t,) = k Sr (Q,)

INCOMPLETE BLOCK DESIGNS j75

where SR(Q,) has similar meaning as SR(ii). The other terms vanish due
to 2,ti—0.

That is, SR(n)=

m— 1

Similarly, Sc (ti)=S£^Ql)

m— 1

and ^('0=|®r (P=

Hence, from (5.12) the solution of ti is obtained as

7:=gf+^(^)+‘s'c(g/)+^, (Qi)+...+Sm^(o,)

m mk(m-1) - (5-13)

The adjusted sum of squares due to the treatments can now be obtained
from 2 ti Qi.
i

TABLE 5.6

Analysis of Variance of m-pie Lattice Design

Sources of variation

d.f.

s.s.

m.s.

F

Blocks (unadjusted)

Treatments (adjusted)

mk—1

k*— 1

b,‘

21< Qi
i

«

St2/S*

Error

Total

'

w

'

1

1

s
,

i

7

by subtraction

5^

mk2—l

£ ya2
ij

The estimate of the difference between the effects of the /th and the i'th

treatments is given by

7,-7i,= Q'-Qi' , s*(Qi)-S*(Qi')+Sc(Qi)-Sc(Q„)+ ■..

m km(m—\)

If the /th and the /'th treatments occur together in a block, say, a row
block, then SR(Qt) and SR(Qi>) are identical.

In this case

V (ti—tt')=o2

2 j 2(m-1) \
m km(m— 1)/

(5.14)

176

DESIGN AND ANALYSIS OF EXPERIMENTS

If the ith and the i'th treatments do not occur together in any block, then

(5.15)

We have, therefore, two variances of the estimates of different pairs of
treatment effects. To obtain the efficiency of these designs, an average
variance is obtained as below and then this average is compared with the
corresponding variance in the randomized block designs as was done in

B.I.B. designs. , . . ^
Let V, denote the variance of the estimate of tt-U> when these two
treatments occur together in the same block and V2 denote its variance

when they do not occur together in the same block.

Let rn — m (k— 1) = the number of treatments each of which occurs with.

say, ti in some block or other

number of treatments which do not occur

with U in any block.

Then, the average variance of the estimates of the difference between pairs

of treatment effect is given by

nxV1+n2Vt

5.9 Partially Balanced Incomplete Block Designs

Lattice designs have the drawback that they are available only for numbers
of treatments which are perfect squares or cubes. This limitation was
‘removed considerably by Bose and Nair (1939) by evolving partially
balanced incomplete block (P.B.I.B.) designs. They defined an m-associate

design as follows.

A set of v treatments distributed in b blocks each containing k distinct
treatments {k < v), is said to form a P.B.I.B. design with m-associate

classes when

(1) every treatment occurs in r blocks
(2) two treatments occur together in Aa, X8, ...» or Am blocks
(3) given a treatment 0 each of nt treatments occur with 0 in A,
blocks (i=l,2,..., w) so that 2 n,=v-1 and 2 n,A,=r (k-1).

1 i

Relative to 0 the remaining treatments are, thus, grouped into m groups
such that the ith group contains n/ treatments each of which occurs with 0
in A, blocks. These nt treatments are said to be the ith associate treatments

or simply ith associates of 0.

Given two treatments 0 and <f> which are ith associates, let the number
of treatments common between the jth associates of 0 and /cth associates
of<t> be denoted by p‘k•

INCOMPLETE BLOCK DESIGNS

177

Then, the P.B.I.B. designs require further that p\k is constant for any

choice of 0 and 6 so long as they are z'th associates.

In the above definition the association between two treatments has been
defined in relation to the number of replications of these two treatments
together. Later on, Bose and Shimamoto (1952) defined association
between two treatments purely from group considerations without relating
it to the number of replications of the pair of treatments. According to
this definition, two treatments or symbols are either first associate or second
associate, etc. or mth associate, and any treatment has m z'th associates
(z'= 1,2,..., m). Given any two treatments 0 and <f» which are z'th associates,
the number of treatments which are y'th associate to 0 and kth associate to
<f> is pjk where p)k is independent of the choice of 0 and <f> so long as they
are z'th associates.

A display of the associates of each of v treatments satisfying the above
requirements forms an association scheme. The parameters of the scheme
are nlt «2.nm, Pjk(i,j, k—1,2,,. .,m). If with v treatments such a
scheme is available then the P.B.I.B. designs are so defined that the require¬
ments in (1) and (2) of the previous definition are satisfied together with
the fact that two treatments which are z'th associates should occur in A<
blocks (z'= 1,2, ..., m).

Example 6. The following blocks give a P.B.I.B. design with parameters
v=b=9, r=k=4, zz1=«2=4, ^=2, A2=l. The pjk parameters which are
called secondary parameters are also shown. The treatments have been
numbered from 1 to 9.

(1358), (2347), (3678), (1269), (1567), (3459), (2468), (1489) and (2579).
The first and second associates of treatments, 1, 2 and 5 are shown below

Ai~2

5, 6, 8, 9 (first associates)

VTl

2, 3, 7, 4 (second associates)

Ai=2

4, 7, 6, 9

1, 3, 5, 8

A, =2

1,3, 7,9

Aa=»l

2, 4, 6, 8

Taking the treatments 1 and 2 which are second associates we find p*x=2,
because 6 and 9 are common between the first associates of 1 and 2.
Similarly,

P\3. ^ P»V P\2 ^ *

178

DESIGN AND ANALYSIS OF EXPERIMENTS

Taking treatments 1 and 5 which are first associates we find similarly

P\x = 1 > Pn =P\\=P\i—2-

It can be verified that these values of p‘jk (},j» k—\, 2) remain unchanged
for any choice of two first or second associate treatments. These secondary
parameters are usually written in the form of the following matrices

*-(! a

5.9.1 Some Facts About P.B.I.B. Designs

Many incomplete block designs including the B.I.B. and lattice designs are
particular cases of P.B.I.B. designs. When all the Vs are equal, it
becomes a B.I.B. design. The square lattice designs are two associates
P.B.I.B. designs. If there are m replications in a square lattice design with
k2 treatments, then the parameters of the corresponding P.B.I.B. design
are as given below:

v—A:2, b=mk, r—m, k—k, nx=m (k— l),n2=(fc—l)(fc+l— m), A1=l,Aa=0

srnd n1 - ((k-2)+(m-\) (m—2) (m-1) (fc+l-m)\
P,J \(m—1) (A: + I—m) {k + \—m){k—m)J

2=(m(m— 1) m(k—m) \
pi> \m(k—m) k2—2— m (2k—m—1)/

In order to make the cubic lattice and higher order lattices as particular
cases of P.B.I.B. designs Nair and Rao (1942) generalized the definition of
P.B.I.B. designs by providing that some of the A/’s can be equal.

’The requirement of constant p')k simplifies the solution of the v reduced
normal equations enabling us to obtain from this set of v equations a set
m independent equations from which a solution of the treatment effects
can be obtained.

5.9.2 Parametric Relations

(1) The relation jPjk—i^k) always holds because of symmetry, that is, from

the fact that if 0 is an /th associate <f>, then<£ is an fth associate of 0.

(2) kf/jk=nJ if *W. (5.16)

=nj—1 if i—j.

(3) n,pjk =njPjk (5.17)

Taking 0 and ^ as two /th associate treatments, the /^treatments which
are yth associates of 0 are distributed in the different associate classes of
^ excepting that when i=j, <f> is one of the /th associate treatments of 0
and is not present in any of the associate classes of <j>. The relation at
(5.16) follows immediately from this consideration.

INCOMPLETE BLOCK DESIGNS

179

Let the group of ith associates of 0 be denoted by Si and the group
of rij jth associates of 0 be denoted by Sj. We now want to find out the
number of pairs of treatments which are kth associates when each such
pair is formed by taking one treatment from S, and the other from Sj.

Any of the n{ treatments in St has pjk of its kth associate treatments
in Sj. So, this treatment forms pjk fcth associate pairs with the treatments
in Sj. Hence, the total number of &th associate pairs of the above type

is rnpljk.

Again, any of the tij treatments in Sj has pjk kth associate treatments

in St. Hence, the total number of such kth associate pairs is also nj pjk.

Hence, n, pjk—nj p'Jk.
This proves (5.17).
In two associate P.B.I.B. designs, there is only one independent
secondary parameter. The remaining parameters can be obtained from
the above relations.

5.9.3 Concept of Association Matrices for a P.B.I.B. Design

Given an association scheme of a P.B.I.B. design with m associate classes,
we can define certain matrices, called association matrices for the P.B.I.B.
design, which possess some algebraic properties and can be applied to
establish the various parametric relations proved in Section 5.9.2. These
matrices are defined as follows.

For every i'=l, 2,..., m, the vxv matrix At=(ay with aj^lifa
and p are zth associates of each other and 0, otherwise,, is a symmetric
matrix with row and column total each equal to nt, the number of zth
associates of any a. Adopting the convention that any a is the oth associate
of itself and of no other p, we can define another vxv symmetric matrix
A0=Iy which corresponds to z=0.

The (m+1) matrices A0, Av..., Am are said to be the association

matrices of the association scheme of the P.B.I.B. design.

Since for any two symbols a and p (may be equal to a), one and only
one of the elements a\p.o™ is unity and the rest are all zeros,
it follows that

(1) 2 Ai=EVfV=the vxv matrix all of whose elements are unity. From

z-o
the same consideration, it follows that

Iff A

(2) 2 aiAi=0,,y implies and is implied by a0=a1«=... =am=0.

' Z-0

From the definitions of the association matrices and the elements

it follows that

(3) AjAjf = 2 pjjt At,(j, j =0,1,..., in)

180

DESIGN AND ANALYSIS OF EXPERIMENTS

(2) and (3) mean that the set of linear functions of A0, Alf..., Am
forms a vector-space of dimension (m+1) with basis A0, Alt..Am
and is closed under multiplication. Multiplication of the A-matrices
is commutative also. This is because

(4) AjAj'=A/A' =(Aj'Aj)'=( 2 pj>jA,y= 2 p\>jA{= 2 pj,jA,=Aj, Aj.

i-0 / =0 1=0

As a consequence of this fact, from (2) follows the relation /?'.,=pi,..
j,j'=0, 1,..., m which is but (1) of Section 5.9.2.

Again, since matrix multiplication is associative, from (3) it follows

that

(5) Aj(Aj,Ajn)=Aj( 2 pj,r,A,)= 2 ppj"{A,A,)= 2 2 pjtJ„ p1' A,>

l — o 1=0 iso i'=0

/w fYi tn

(AjAji ) Aj>> 2 pjjt (AiAjn')— 2 2 pjjr p\^> Aj,
i=0 1-0 <' =0

m m

and hence, in view of (2),

in . . m

(6) 2 Pjj, p'jn = 2 Pj/Jf, Pj, .

is 0

i=0

Defining therefore, the p,-ma trices for i=0, 1,..., m by

_1 m
Pol • • • Poi

P/rtf ' ' • Pmi mi

(7) />/=(/>£) =

Pol

Pm,

(6) is equivalent to

(8) pj> pjn= 2 pjtjn pi

i-0

which shows that the ^/-matrices multiply in the same manner as the
^-matrices. Also, these matrices are linearly independent.

It has been proved by Connor and Clatworthy (1954) and also by
Bose and Mesner (1959) that the distinct characteristic roots of the

m m

matrices 2 a/^i and 2 aipt are the same. Since the incidence matrix

/=o is o

N of a P.B.I.B. design satisfies

(9) N’N^A^X.A^... -\-\mAm,

it follows that the distinct characteristic roots of NN' are simply those
°f rPo+\P\+... +Ampm. For m~2, Connor and Clatworthy
determined the roots of NN' and their multiplicities. The reader is
referred to the papers by these authors for details.

5.9.4 Classifications of P.B.I.B. Designs with Two

Associate Classes

The P.B.I.B. designs with two associate classes are the simplest for analysis.

INCOMPLETE BLOCK DESIGNS

181

because a general solution of treatment effects can be obtained in this
case by solving two equations. Further, these designs are the nearest
to B.I.B. designs because through these designs the different treatment
pairs can be compared with two precisions. Bose, Clatworthy and
Shrikhande (1954), tabulated the solutions of all known two associate
designs. These designs are not, however, exhaustive. For example, Saha
and Das (1971) gave some designs which are not tabulated there.

For such tabulation they first divided the two associate designs in the
following five categories according to the association schemes of the
designs:

(1) group divisible (G.D.)
(2) simple
(3) triangular
(4) Latin Square type
(5) cyclic

These are defined as below.

(1) Group Divisible
In this category the v=mn treatments are divided into m groups of n each
such that any two treatments of the same group are first associates and
two treatments from different groups are second associates. The
association scheme can be displayed by arranging the treatment numbers
in a rectangular arrangement of m rows and n columns where each row of
n treatments gives a group. Evidently,

nx=n— 1, n2=n (m—1)

The secondary parameters are

0 n— 1
n — 1 n(m—2)

(2) Simple P.B.I.B. Designs
A P.B.I.B. design with two associate classes is said to be simple if either
(i) a^O, A2=0 or (ii) A^O, A2^0. It may happen that a design of the
simple category may belong to some other category as well.

(3) Triangular P.B.I.B. Designs .
A P B I B design with two associate classes is said to be triangular if the
number of treatments v=n(n-1)/2 and the association scheme is an

array of n rows and n columns such that

182

DESIGN AND ANALYSIS OF EXPERIMENTS

(i) the positions in the principal diagonal of the scheme (upper left

to lower right) are left blank,

(ii) the n(n—l)/2 positions above the principal diagonal are filled by

the treatment numbers 1, 2.n(n—1)/2,

(iii) the n (n—1)/2 positions below the diagonal are so filled that the

array is symmetrical about the principal diagonal and

(iv) for any treatment i the first associates are exactly those treatments

which lie in the same row as i.

Here, nx=2n—4, n2=(n—2)(n—3)/2

1 _ 1 f n—2
Pi i | \ n—3

( 4

Pi]— I (2n-8

n—3
{n—3) (n— -4)/2

2/1—8
(71— 4) (77 — -5)/2

(4) Latin Square Type of P.B.I.B. Designs
Let a square array of n rows and n columns be formed with n2 treatment
numbers from 1 to ti2, so that two treatments are first associates if they
occur in the same row or the same column of the array and second
associates otherwise. A design with the above array as association scheme
is said to belong to the sub-type L2. A design belonging to sub-type Lz
is also defined. In this design it is possible to form a square array of ti2
treatment numbers from 1 to n2 and to impose a latin square with n letters
on this array, so that any two treatments are first associates if they occur
in the same ro\y or column of the array or correspond to the same letter
of the latin square and are second associates otherwise.

In these designs,

ny=L{n — 1), n2=(n— 1) (n-L-r 1)

/L2-3L+n (L—1) (n-L + \)\

\(L—1) (n-L+1) (n-L)in-L+ 1)/

L(L-l) L(n—L)

L(n—L) {n-L)2+(L-2)

where L - 2 for sub-type L2

and L=3 for sub-type L3.

The above parameters are exactly the same as those in simple and
triple lattices with rC- treatments. These two types of designs are, however,
different.

(5) Cyclic P.B.I.B. Designs
A non-group divisible P.B.I.B. design is called cyclic if the set of first

INCOMPLETE BLOCK DESIGNS

183

associates of the treatment numbered i is obtained by adding i—1 to the
numbers in the set of first associates of the treatment numbered 1 and
subtracting v whenever the sum exceed v (the number of treatments).

The analysis of each category of designs has been illustrated by them.
There are large numbers of methods for the construction of these designs.
We shall restrict ourselves to a discussion of the analysis of P.B.I.B. designs
leaving constructional details, many of which are available in Bose and
Nair (1939).

5.10 Analysis of P.B.I.B. Designs

We have discussed below the method of analysis suitable for m-associate
P.B.I.B. designs. The model and the method followed are the same as
those described in the analysis of non-orthogonal data in Chapter 1. The
incidence matrix or the frequency table of P.B.I.B. designs is of the
following type:

TABLE 5.7

Incidence Matrix of P.B.I.B. Designs

Treatments

2 3 .

. V

Block size
n.j

Block
totals

1

1

0

1

1

2

3

0

1

1

o . .

. 1

l . .

. 0

o . .

. 1

b

1

1

l . .

. 0

r

r

r
Tx  t2  t3 . .
Qx  Q2  Qz

. r

. T,

Qv

Blocks

Total (Rep. n<.)

Treatment totals

Adjusted totals

k

k

k

k

Bx

b2

Bz

Bb

where Qt—Tt—^nuBj

JO, if the ith treatment does not occur in theyth block,

and n,',==(l, if the ith treatment occurs in the y'th block.

The adjusted total Qfs can also be obtained by first taking the deviation
of each observation from its block mean and then the treatment totals
obtained by treating these deviations as if they come from a completely
randomized design, give the adjusted totals.

m

DESIGN AND ANALYSIS OF EXPERIMENTS

In this design «,.=r, n.j=k and 2 mj ni>j—'kp when the ith and the i'th

treatments are pth associates (p — \, 2,..., m).

j

Let ti (i= 1, 2,..., v) denote the effect of the ith treatment. Let further
Sp (ti) denote the sum of the np treatment effects which are pth associates
to U(p—1,2,..m).

Similarly, Sp(Qi) denotes the sum of the adjusted totals of these np
treatments. Let further 0', ©/,..., 0j,p denote the effects of the np
treatments which are pth. associates to the ith treatment.

The reduced normal equation for ti is

r (*-1) ii-\Sx (i,)-\S9 (1,)-...—XmSm (t,)=kQ,

(z=l,2,..., v) (5.18)

Let us again write the following np equations for 0^, 02',..., B'„p:

r(k-\) (V)S,(0a0-. • .-^(O^fcgtV)

. (5.19)

r (k-1)0',-A^ (%)-S2 (0'p- ... -Sm (0',)=*fi (0>p)

Adding all the np equations at (5.19) we get an equation of the following
form:

'(*-1) Sp(ti)-\CX-\C2- .. .-AmCm=kSp(Qi) (5.20)

where Cx, C2,... ,Cm are m linear functions of the treatment effects. As
a matter of fact, the ra-associate P. B. I. B. designs are so defined as to
make the C/’s linear functions of th S^U), S2(t,),.. .,Sm(tt).

One test to ascertain if a design is P.B.I.B. with w-associate classes is
provided by the behaviour of C/’s. That is, if any of the C/’s does not
come out as a linear function of U, Sx (t,),.. .,Sm(t,), then the design is not
a P.B.I.B with w-associate classes. Further, the different associate groups
of treatments of any treatment in the design where some of the A/’s are
equal, can be ascertained easily from an inspection of the C/’s.

$v ^2” • -’Kj denote the effects of nj treatments which are, say/th

associates to the ith treatment.

In Cj any /th associate treatment />/, say, occurs as many times as the
number of treatments among 0,| 0«,... ,0'p which have <f>[, as the first
associate, which in other words means the number of treatments among 0f,
of the 0g,... ,6‘„p which are first associates to c£*. This number is, by
definition of the design, p[y So, the coefficient of 4>[ in Cx is p\. This is
so for every ^

Hence, adding over / C,=2 pJpl S, (t,).

Jal

In general, it can be argued similarly that

m

and

Cl=2 pjpL Sj (ti)

j

Cp=np iz+Sppp Sj (t/)

INCOMPLETE BLOCK DESIGNS

185

Substituting these values of C;’s in (5.20) we get after rearranging

r (k-1) S, (td-S, (t,) 2 \l p\l-S, (/,) 2 \,p\L-...

L L

—Sm 2 ALppL—Xp np ti—kSp (Qi) (p=\, 2,..m). (5.21)

For m distinct values of p we get m such equations. Each of these
equations contains (m+1) unknowns Sj (ti),... ,Sm (ti). The equation
at (5.18) also contains the same unknowns. These equations are not,
however, all independent. A unique solution for tt can be obtained from
them by taking the restriction 2 //=0, that is

J/+S'1 (?/)-{-.Sg (tj)+... + >Sm (ri)=0.

5.10.1 Analysis of P.B.I.B. Designs with Two Associate Classes

Although the set of reduced normal equations could be reduced to m
equations involving (m+1) unknowns as indicated above, no neat solution
of the treatment effects is easily available for m-associate designs. We
have, therefore, given below the complete technique of analysis of two
associate P.B.I.B. designs.

When m=2, the equations at (5.18) and (5.21) become

r (k— 1) 'ti—\ (~ti)—\si(ti)=kQi

r (k— 1) St (ti)—Sl (ti) (A1 p’1+A2 p\2)—nx \ t~i—S2 (t{)

X(A1pf14A2jp?2)=^1(e<)

r (k-1) S2 (iti)-Sx (ti) (Aj pJ2+A2 p\2)-S2 &)

The last of the above three equations is actually not required. Eliminating
S2 (ti) from the first two equations by using the restriction:

X (Ax P*2+A2 pl2) n2 A2 ti—kS2 (Qi)

and simplifying, we get

4/+<Si (ii)+St (ti)—0

{r (k- 1)+Aa> F,-(A1-A8) Sj (i,)==kQ,

(A.-Ai)p% ii+Sx (f,) (r (k— l)+A2-f (A2—Aj) (p^-p^kS, (Qi)

The solution of ti from the above is given by

- k {B2 Qi A2Sa (Qi)} 0 \
U~ A~B2—A2 By (l~l> A- • -,v)

(5.22)

where

A1=r (k- 1)+A2

A j=A2 Aj

’^l) P] 2

B2=r (*-!)+A2+(A2-Aj) (Pl-Pl)

186

DESIGN AND ANALYSIS OF EXPERIMENTS

The estimate of the difference between two treatment effects is given by

7 _r (fit ~ Q,')-A»{Sl m-Sr (6,0}
' U' Ax B2-A2

Hence,

i \ 2k(B2+At)J

var(t,-t,)= A<B_AiB-

when ti and tt> are first associates,

(say)

2kB2a2
Ax B2 A2 Bx

when the two treatments are second associates

=v2 (say).

In the case of lattice designs we saw that there are two variances for the
comparisons of the estimates of such difference. The efficiency of these
designs is therefore obtained from the average variance which is obtained
as an average variance of vx and v2 given above using nx and n2 respectively
as the weights. The average variance is given by

v_nx Vi+n2v8

«l + «2

The efficiency factor of the design relative to randomized block designs is,
therefore, equal to

(»— 1) (A}B2—A9Bx)
rk {(v — 1) B2+nxA2)

5.11 Analysis with Recovery of Inter-Block Information

In Section 5.6 it was pointed out that block effects can be considered to
be random variables in incomplete block designs. Accordingly, using
block effects as another source of error, there can be one more estimate of
the treatment effects (based on block totals). Such estimates are called
inter-block estimates./ Yates (1940) obtained inter-block estimates of
treatment effects for balanced incomplete block designs as functions of
block totals. Then by suitably combining the inter-block estimates and the
usual intra-block estimates the combined estimates of the treatment effects
were obtained. In P.B.I.B. designs it is not always possible to get
separate inter-block estimates as functions of the block totals because in
these designs the number of blocks can be less than the number of treat¬
ments. However, Rao (1947) gave a method of obtaining combined
estimates of treatment effects for incomplete block designs in general. This
method has been described below.

In the model

Yu—(x -j- ti+bj+Cij

INCOMPLETE BLOCK DESIGNS

187

£//s alone are considered to be random variables with a constant variance
for intra-block analysis. For inter-block analysis b/s are also considered
as random variables and hence the random variables Ytj have the variance

^ where ab2 is the block variance.

The inter-block estimates are obtained by treating the block totals as

observations, and are obtained by minimizing

(5.23)

with respect to p. and U.

The normal equations are

j t

G=bkiL+r2t, (5.24)

i

and Vi=kr^i-rti+ 2 (2/i/j/V;)7,* (i=l,2, ..., v) (5.25)

/V/ J

where F/ is the sum of the totals of those blocks in which the ith treatment
occurs and G is the grand total.

From (5.24) and (5.25), we get

rt,+ 2 F,-^G=Pi,(/=1,2, ...,v) (5.26)

where hi> = 2ntjnt>j, Pi = Vt—r^G.

The reduced normal equations for intra-block estimates which are obtained
by minimizing

2 (y>j—[>■—U—bj)2 (5.27)
u

are r(k — 1) ti— 2 —kQi(i= 1,2, ..., v) (5.28)

Let W=~ and -=*-(kab2+o2)-\

iV(
1 W' 1

Then linearly combining the two equations (5.26) and (5.28) with W'Jk
and W respectively as weights we get the following equation from which
the combined estimates can be obtained:

' {W(k-X)±W) 'tx=WQ,+^ P, (5.29)

The equations (5.29) can also be obtained by first combining the two
least-squares set-ups (5.23) and (5.27) with W'\k and W respectively as
weights and then minimizing with respect to the parameters.

The equations (5.29) are the general reduced normal equations for all
incomplete block designs. For P.B.I.B. designs with m-associate classes,
these equations take the same form as in (5.18) obtained for intra-block
analysis of P.B.I.B. designs. Subsequent procedures for obtaining the
combined estimates are, therefore, the same as in the case of intra-block

analysis.

188

DESIGN AND ANALYSIS OF EXPERIMENTS

We have discussed below the case of two associate P.B.I.B. designs

from which the results for B.I.B. and lattice designs also are obtainable.

In the case of P.B.I.B. designs with two associate classes the reduced

normal equations (5.29) become

r{W{k-\)+W'} W') (XiSi (ti) 4- \Sa (?<)}=WkQi+W'Pi (5.30)

Taking h+S'i (h)+S2 (ti)=0

and eliminating Ss(t,) from (5.30) we get

lr{W(k-l)+W'}+(W-W')K] t,]

+(W- W’) (A2-\) Si (/,)=WkQt+ W'Pi (5.31)

Adding such equations for each of the treatments in S1 (u) and eliminating
S2 (U) we get

(W—W) (A2—A,)p*2 i,+S1 (/,) [r {W (k—1)+ W'j

+(^-W"){A2+(Aa-^i) (Pn'-Pn2)}]^! W

(/=1,2, ..., v) (5.32)

where R,=WkQ,+W'Ph i=l,2,...,v.

By solving the equations (5.31) and (5.32) we get

- k(B2'Ri — A2'S^ (Rj) r5 33^
' A^B^—AoB^ K ' }

where A^ =r {W (k-\)+W'}+(W-W') A2

Aa'=(\-\)(W-W')

B1'=(W— W’) (A,—A2) p*2

Bt’ —r { W(k- 1)+W'}+(W-W’) {A2+(A2-A1)(z^-^)}.

varCtt—t+)=^2 % when the treatments are first associates

A1B2~A2B1

• 2 kB2 , , . .

—-mu—m*> when the treatments are second associates

AxB2—A.ifBi

It is seen that by putting Ai=A2 in equation (5.30) we get the combined
-estimate of the treatment effect for B.I.B. designs as

WkQi+W'Pi
r{W(k-\) + W } + (W-W')X

Q,+ P,

where p=

rE+ p (^)

VW
W

(5.34)

var{ti—tm)-

2 Wk

r{W(k-\)+W') + (W-W')A~r£[ p(«-A)

INCOMPLETE BLOCK DESIGNS

189

The variance and the efficiency formula remain of the same form as in
the corresponding incomplete block designs. No exact F-test is valid for
testing the equality of the treatment effects based on the combined estimates
particularly because W and W' are unknown. Approximate F and f-test
are, however, possible when the treatment effects are estimated from (5.34),
after substituting for estimates of W and W'.

5.11.1 Estimation of the Weights W and W'

W is estimated from the intra-block mean squares for the design. If s2
denotes the intra-block mean squares, then

W' is estimated by using the adjusted block mean squares. The adjusted
block sum of squares can be obtained from the relation (1.19) which was
derived in Section 1.8.4 of analysis of variance of non-orthogonal data in
Chapter 1.
Adjusted block r.r^fadj. Tr. j’.5,.)-|-(unadj. block s.s.)—(unadj. Tr. s.s.)

Let S&* denote the adjusted block mean squares for any incomplete block
design. Then

(5.35)

Taking the intra-block error mean square, s2 as an estimate of a2, we

get an estimate of ob2 from

Hence, the estimate of ~=kcb2-\-o2 is given by

k(b-\)sb2-(?-k) s2
v(r—1)

(5.36)

These estimates remain the same for both B.I.B. and Youden Square
designs.

For resolvable incomplete block designs in which the blocks can be
made into r groups such that each group contains a complete replication
of the treatments, the within group adjusted block mean squares can be
used to estimate W more precisely. The within group adjusted
block sum of squares can be obtained by subtracting the between group

190

DESIGN AND ANALYSIS OF EXPERIMENTS

sum of squares from the adjusted block sum of squares. It has (b—r)
degrees of freedom. Let the within group adjusted block mean squares
be denoted by Sb'2.

Then

E(sb’*> -oa-

(r-  -l)(v—Ac) 2
i---- Go

Hence, a*,8 is estimated by

(Sb’2 k(r-l)

and 7777 is estimated by

W

rSb'2 -s'

(5.37)

Another method of estimation of weights under the so-called normal
set-up has been developed by Roy and Shah (1962) while examining the
problem of recovery of inter-block information for a general incomplete
block design. This method can be discussed as follows. We have already
mentioned in Section 5.6 that the randomization procedure in all in¬
complete block designs consists of first allotting the treatment blocks
to the field blocks at random and then distributing the treatments thus
allotted to a field block at random to the different units in the block.
Denoting by Ti« the yield of wth plot in ith block and putting mjiu=l or 0
according as the jth treatment occurs in the wth cell of the ith block or
not, the linear model under the usual assumption of additive treatment
and (random) block effects can be written as

E{Yiu)=\i+ 2 tj rrijiu

j=i

if i—i’, u=u

if i—i', u^u'

-i(„=+W),

if izj/Li’

Cov(Y,„, YVu, )=- I 1

1
l

Writing p=(oa+A:CT62)/a2= JL/IF', the combined normal equations (5.29)
for estimating the treatment effects, obtained by combining the inter¬
block and intra-block equations (5.26) and (5.28) respectively, can be
rewritten as

r | (k— l)?i+^4j -(l~=kQi+l~Pi> *=•» 2.v (5.38)

The method of estimation of p adopted by Roy and Shah is the maximum
likelihood method under the assumption of normality of the distribution
of Tin’s through a canonical reduction of the problem. However no
compact form of the estimate suitable for computation is available and
an iterative formula which is to be used in practice for actual computation
is given by

INCOMPLETE BLOCK DESIGNS

n * - g* i

6(fc-l)

191

(5.39)

(6-1)  2 ylu*-2 2 tjO Tj+r2(tjW)*-l
L i,u j J *

2 B,a(f<»))l
'/=■! J

where B/(if)=i?,—2 mjiutj and 7<") is the «th approximation for t, obtained

J,u _ _

by solving the equations (5.38) taking r=f<"-1). As a first approximation
for T, we may take its intra-block estimate.

Individual maximum likelihood estimates of a2 and o*2 have also been
provided by Roy and Shah under the normality assumption. But since
these are somewhat difficult to compute, they also derived estimates of a2
and (a2+kcb2) by restricting to the class of quadratic estimators. In case
when the ratio p=WfW' is large, the optimum unbiased estimates of o2
and (kab2+o2) obtained by minimizing the term involving p2 in the
expression for the respective variances of the estimates have been provided
by them and are given by

± S **(»)-£] (5.40)

where Bi(i)=Bi— 2 mjlu ~tj and tj is the intra-block estimate ofT/ obtained

from (5.28) and ci=(rk—<f>i)/<f>i with <£,’s as the q positive latent roots of
NN\ which are smaller than rk. This estimate (5.40) was also suggested
by Shah (1962) from intuitive considerations. Starting with these
estimators, we get as an unbiased estimator of p the following:

2 \(a2+W) 2(y-l) (\
bk-b-v+l) (bk-b-v+l)(b-l)\E )

(5.41)

where E is the efficiency factor of the design (Kempthorne, 1956; Roy,
1958) given by

_(v—1)/(v—1—g | | 1 1
rk rk i=\rk—<f>i)

(5.42)

It may be mentioned that the usual estimate p of p given by

^ k(b—1)^*—(v—k)s2
9 ~~ v(r—1)

is not an unbiased estimate of p, but a simple correction gives an unbiased
estimate in the form

2 V_2 (v—k)_
bk—b — v+l)9 v(r—l)(bk—b—v+l)

(5.43)

192

DESIGN AND ANALYSIS OF EXPERIMENTS

For details of the derivations of the above results, the reader is referred
to the relevant paper by Roy and Shah (1962) cited at the end of this
chapter.

Another kind of results in this direction has been obtained by
Zyskind and Martin (1966) while developing conditions for combinations
of information from uncorrelated linear models by simple weighting. It
is clear from the work of these authors and also from the work of Roy
and Shah (1962) that the reduced intra-block and inter-block normal
equations (5.28) and (5.26) respectively for estimating the same set of
treatment effects can be regarded as originating from two uncorrelated
sources of data. This fact often makes it possible, under certain conditions,
to obtain the best linear unbiased estimate of an estimable linear function
of treatment effects (e.g., estimable treatment contrasts) just from one or the
other set of normal equations alone or by simple weighting of the solutions
from both the equations. Zyskind and Martin (1966) have derived
various such conditions in terms of the form of the matrix NN' where N
is the incidence matrix of the incomplete block design in question. For
example, for incomplete block designs in general, if we are interested in
estimating a treatment contrast V t, then it is best estimated from intra-
block information alone, if, and only if, NN'I=0 and from inter-block
information alone, if NN'l=rkl so that in either case combination is no
longer necessary. Moreover, in general, a treatment contrast I't, estimable
from both the intra-block and inter-block information, is best combined
by simple weighting (b.c.s.w.) in the sense that its b.l.u.e. is obtained by
simple weighting of its intra-block and inter-block estimates if, and only
if, / is an eigenvector of NN’. In particular, in an incomplete block
design all treatment contrasts are b.c.s.w. if, and only if, the design has
the structure of a balanced incomplete block design. For the derivation
of these and other very similar interesting results the reader is referred
to the relevant paper of Zyskind and Martin (1966) cited at the end of
this chapter.

Example 1: Both the intra-block analysis and the combined estimates
of the treatment effects have been illustrated below by analyzing a body
of data collected from a varietal trial on wheat crop in India adopting a
two associate P.B.I.B. design. The parameters of the design are

v=6=9, r—k—3, A1=l, Aa=0, nx=6, «2=2

The data along with the block contents and the deviate of each observation
from its block average are shown in Table 5.8.

INCOMPLETE BLOCK DESIGNS

193

Layout Plan and the Observation (K.G. per plot) from the above P.B.I.B. Design

TABLE 5.8

Blocks

1

2

3

Contents
(1)

Observations
(2)

Deviation
(3)

3

8

4

Total
Mean

(1)

7

8

9

Total
Mean

(D

1

8

6

59

56

53

168
56

4

(2)

46

56

51

153
51

7

(2)

54

58

62

3

0

-3

(3)

—5

5

0

(3)

-4

0

4

(1)

(2)

(3)

(1)

(2)

(3)

-1

-3

4

1

7

5

2

7

4

35

33

40

108
36

4

-2

-2

48

42

42

132
44

Blocks

5

6

(1)

(2)

(3)

(1)

(2)

(3)

4

5

6

61

61

55

177
59

2

2

-4

3

9

5

52

53

1

2

48  —3

153
51

Blocks

8

9

(1)

(2)

(3)

(1)

(2)

(3)

• 2

45  —1

9

6

46

47

0

1

1

2

3

31

27

35

0

-4

4

Total
Mean

174 138 93
58 46 31

194 DESIGN AND ANALYSIS OF EXPERIMENTS

The sum of the deviates in the above table against the treatment

number / gives Qt(i—1, 2,..9).

Thus gi=4—4+0=0.

Similarly, 02=—6

03=8

04=3

05=-3

06=1

07= 10

08 = 5

09=2.

The association scheme of the design is as shown below.

V=1 <-- 2, 3, 5, 6, 7, 8 (first associates)

- 4, 9 (second associates)
At=0

1. 3, 4, 6, 7, 9

5, 8

1,2,4, 5, 8,9

6,7

2, 3, 5, 6, 7, 8

1,9

1, 3, 4, 6, 7, 9
2, 8
1, 2, 4, 5, 8, 9

3,7

1, 2, 4, 5, 8, 9

3, 6

1, 3, 4, 6, 7, 9

2,5

2, 3, 5, 6, 7, 8

1, 9

INCOMPLETE BLOCK DESIGNS

195

The design is resolvable. Block numbers 1, 3, and 8 form one group;

2, 6, 7 form another group and 4,5,9 form the last group.
The solution of the treatment effects are given below:

r kjBtQt-A^Q,)}
1 AxB2-AtBx

where Ax=r(k—1)+Aa=6

Aa=(\~ A»)=—1

B2—r (k- 1)+A2+(*2-*i) (P\~P\J=9

Substituting these values in the expression for ?/, we get
Qt, s,m

~ 2 t 18

As Sx{Qt) is the sum of six Qfs and S2(Qt) is the sum of two 0/’sitis
better to express tt here as a function of S2(Qi) with the help of the

relation

Accordingly,

Qt+S^Qd+S^Q,)^

- = 4g,_Ss(g^ (/=1,2.9). (5.3*)

Substituting for 0, and S2(Qt) in (5.35) we get

18?,= —5, 18?2=—50, 18?s=73, 18?*=22, 18?6=-23,

18?6=10, 18?7=—89, 18?8=49, 18?#=13.

- 365
The adj. tr. s.s.=2 tiQi=-~-
i ^

Total s.s. of the deviates=within block s.s.=222

365 301
Hence, the error s.s.=222—— —— .

The different results are now shown in Table 5.9.

Analysis of Variance of the Data Presented in Table 5.8

TABLE 5.9

Source
of

variation

d.f.

s.s.

m.s.

F

For combined
analysis
s.s.

1295.00

Blocks
(adj.)

Blocks
(un. cor)
(unadj.)
Treatments
(adjusted)

Error
Total

8

8

10
26

64476.00

121.67

15.21

1.5 n.s.

63302.67  Treatments

(unadj.)

100.33
64698.00

10.03

100,33
64698.00

Error
Total

196

DESIGN AND ANALYSIS OF EXPERIMENTS

The results do not indicate any significant difference among the

treatment effects.

vfc _ 7,)=V*' A * ° when U and tt> are first associates

„i=!
- 54 9

__?kB2o b- when tt and tt> are second associates

AyB^—A^B^

Since

6x9 2
34" °

=c

«x=6 and h2=2,

(|x«42)

Av. var.

11 .
=12 °

Hence, efficiency factor=—.

Combined Estimates

The weight, W is estimated by 1 Is2 where 52 is the intra-block error

m.s. in Table 5.9.

That is, W=0.1.
To estimate W’, we require within group adj. block s.s.
This s.s.=(Adj. block 5.5.)—(Bet. group s.s.)

= 1495—14=1481

Hence, 56'2=^ = 185.125.

Hence W'=■■-■■& 1 -2
rst,2—52

2

"3x185.125-10.033

=0.004

To obtain the combined estimates we require further

A^riWik-V+W^+iJV-W) Aa=0.612

A2'=(\-\){W-W')

= -0.096

■®i =(^a ^i) Pu*

=0

INCOMPLETE BLOCK DESIGNS

197

Bt’=r{W{k-\)+W')+(W-W) (p\-*np)}

=0.900

Again, Ri=Wk Qt + W'Pi (/= 1,2.9)

and P/=F,~G.

b

In the subsequent calculation Pi has been taken to be equal to
Pi(*=l» 2,.. .,9) and the term rjb G has been ignored. This will result
in a shift of the origin of the estimate tt of the treatments. Since 2 f/=0

without the above manipulation, we can easily get the actual solution
from the following:

i

2//

T *' l

where U' is the estimate of tt obtained after ignoring rjb G while calculating

Accordingly,

Pi(i— 1, 2,..., v).

PX=VX= 132+174+93 =399=Sum of totals of blocks with tx.

Pa=339

Ps=414

P4=453

P6=462

Pe=4 89

P7=393

P8=495

P„=444

Hence P,= WkQt+ W'Pi (/= 1, 2,....9)

= .3<2,+ .004P,

Using (5.34) we now get the combined estimates, ti as follows:

?!=—1.39 f4=4.08 f7= —15.22

?a=—9.88 ?6=—3.16 /„=9.25

?s=l 1.65 i«=2.34 7„=2.43

The variance of the estimate of the difference between two treatment
effects is given by

— — 2k (B ' -\-A ')

v (tt —ti>)— , „ ,* W". when the treatments are first associates

At xj2 —At dx

6(.9—.096)

~ .9x .612

=8.76

198

DESIGN AND ANALYSIS OF EXPERIMENTS

_ _. N 2kB2' when the treatments are second

v(^—U> )=Al'Bi— A2'Bi associates

6x .9
.9 X .612

=9.80.

5.12 Optimality of Designs

Having described in detail various complete and incomplete block designs,
designs with variable replications, factorial designs and others, we shall
introduce here the concept of optimality of designs and mention some
important results. In the early stages of agricultural experimentation, only
a few experimental designs were at one’s disposal. But, now-a-days, an
experimenter with modern statistical equipments at his disposal, can use a
variety of experimental designs as mentioned above. Hence, whenever the
conditions of an experiment allow the possibility of simultaneous existence
of a number of experimental designs, the question of selection of an appro¬
priate design, a design which is easy to analyze and which has some
optimum properties, naturally arises. A systematic study of the specification
of optimum experimental designs was undertaken by Kiefer (1958, 1959)
in a series of papers, where he introduced various optimality criteria
(A, D, E, L, M), discussed interrelations amongst these and established
the optimality property of some well-known designs in some particular
problems.

We assume here the usual linear set-up for the analysis of an experi¬
mental design. To explain the various optimality criteria let us suppose
that D is the class of all available designs in a given context and we are
interested in the vector of treatment effects

n—Lt

where Lisa matrix of dimension / X v of known coefficients and t=>(tx, ..., tv)'
is the v-dimensional vector of unknown treatment effects. Proper choice
of L would lead to the vector of all elementary treatment contrasts
{(ti—tj) i^fij) and to the vector of orthogonal treatment contrasts. Fora
given d £ D we write cov (n)d for the covariance matrix of the estimator n
of n using the design d.

Definition 5.12.1 (A-optimum): For / (number of rows of the matrix L)
unrestricted and finite with rank (L) < min (/, v—1), a design d* £ D is
said to be zl-optimum in D if

tr (cov (n)d.} ^ tr {cov (n)d)

7 < / “

for any other design d£D.

Definition 5.12.2 (D-optimum): Let rank (£,)=/< v—1. A design J*g;D

INCOMPLETE BLOCK DESIGNS

199

is said to be Z)-optimum in E if det (cov ^ det (cov («)<*) for any other
d^D.

Definition 5.12.3 (E-optimum): Let rank (L)=/ < v—1. A design d* is
said to be E-optimum in D if the maximum characteristic root of cov(ri)d*
is less than or equal to the maximum characteristic root of cov (ri)d for any
other d£L D.

For the definitions of L-and Af-optimality criteria the reader is referred

to Kiefer (1958).

The late professor Abraham Wald (1943) was the first to mention the
.E-optimality criteria for designs in testing hypotheses in the setting of two-
way soil heterogeneity where Latin square designs are commonly used and
established that the Latin square design is E-optimum for estimating a full
set of orthonormal treatment contrasts. Later Ehrenfeld(1953) proved the
property of E-optimality of the latin square designs for the same problem.
Restricting attention to non-randomized designs where we would like to
use one and only one of the available designs, the fundamental results
obtained by Kiefer (1958) in the setting of one-way heterogeneity (i.e. two
way classified data) are that for estimating a full set of orthonormal treat¬
ment contrasts, the balanced incomplete block design, whenever it exists,
is A—D—E—L optimum. As a matter of fact, Kiefer proved the optimum
properties for a more general class of designs, called by him balanced
block designs, which include as particular cases the randomized block
designs and the balanced incomplete block designs. For the three-way
classified data he defined generalized Youden square designs including as
particular cases the Youden square and the Latin square designs.

Writing t—(tx, ..., tv)' for the column vector of treatment effects and

n=Pt where

is an orthogonal matrix, Kiefer proved the optimality of balanced block
designs (in a two-way classified data) and of generalized Youden square
designs (in a three-way classified data) in general in the class of all connected
proper designs for estimating n with respect to the ,4-E-E-E-optimality
criteria. For binary designs, however, Mote (1958) proved the E-optimality
of balanced incomplete block designs and Kshirsagar (1958) proved the
A-and E-optimality of this design for estimating orthogonal contrasts and
also of the Youden square designs. Roy (1958) established the necessary
and the sufficient condition for a binary design to be most efficient with
respect to the ,4-optimality criterion for estimating all elementary treatment
contrasts and proved that in the case of proper binary incomplete block
designs a most efficient design, if it exists, is necessarily a balanced
incomplete block design. In all such cases it has been demonstrated that

200

DESIGN AND ANALYSIS OF EXPERIMENTS

the C-matrix of the design plays a very important role. In fact, all the
optimum properties are derived from some special forms of the C-matrix
as defined in Chapter 1. For further study and proofs of the results stated
here the reader is referred to the references given in this chapter.

EXERCISES

Prove that for a symmetrical B.I.B.D. with v even, (r—A) must be a perfect
square. Also, show that for a symmetrical B.I.B. design,

(IV,)_i=(Ar—“ *..)/ (r—X)

and hence that NN'^N'N. Interpret the last result in terms of the number of
treatments common between any two blocks.

2. Prove that for a resolvable B.I.B.D. rank N < b—(r—1).
3. Prove that the C-matrix of a B.I.B.D. is given by

vk A
C=~j~ Iv Evv

and hence show that using a B.I.B.D. all elementary treatment contrasts are
estimated with the same precision.
Show that for an affine resolvable B.I.B.D. the parameters can be expressed in
terms of two integers n and t (n > 2, t > 0) as

4.

v=nk=ri2‘[(n—\) f+1], 6 = «/-<=« (rfi + nt+l), A=/tf+l.

5.

In the case of a P.B.I.B.D. with two-associate classes determine the values
and multiplicities of the eigen values of N'N in terms of the parameters of the

6.

7.

design.
Show that the design obtained by taking blocks for treatments and treatments for
blocks in the B.I.B.D. with parameters &=(v(v—1))/2, k=2, r=v—1, A=1 isa
P. B. I. B. D. Obtain the parameters of the design.
In a B. I. B. design n observations are missing in n blocks such that there is no
common treatments between any two of the blocks having missing observations.
For the sake of convenience let the z'th missing observation (when arranged in
some order) be missing in the j (/) th block and belong to the z'th treatment.
Show that the estimate of the z'th missing observation obtained by minimizing the
error sum of squares, is given by

/ 1 1 1 \ _ Qi1
[l-k+7+7r) Xi=~T"

2 Qi’

JO)

vA

0=1, 2,.. .,«)

where Qi' is the adjusted total of the z'th treatment obtained by taking zero for
the missing values and 2 Qi is the sum of adjusted total of those treatments

which are present in the block in which the z'th treatment is missing. Show
further that the true error sum of squares is equal to

an

where (E.S.S.)o is the error sum of squares obtained by taking zero for the
missing observations.
rfi numbers from I to are arranged in the form of an rtxn square. The n
elements occurring in the left to right diagonal of the square are. omitted. Next,

8

INCOMPLETE BLOCK DESIGNS

i201

from each row of the square a block of size («—1) is formed. Similarly, from
each column of it a block is formed. The design in these 2n blocks each of (n-/l)
units is called a simple rectangular lattice design. Show that this design is a four
associate P.B.I.B design.

9. If in each block of a P.B.I.B. design with two associate classes a new treatment

is included, derive a method of analysis of the resultant design.

10. Let one of the b blocks of k units each of a B.I.B. design with v treatments be
drawn at random with equal probability. If these k units are taken to provide
a sample of k units from a population of v units, show that it provides the same
unbiased estimate of the population mean and its variance, as is provided by the
technique of simple random sampling without replacement. Show further that
the usual simple random sampling without replacement corresponds to drawing of
one of the blocks, of the following B. I. B. design at random.

v, k, b=vCk, r-v-lCfc-1, A=v-2Cjfc_2

11. An incomplete block design in v treatments is obtained by developing the initial
block (1,2) mod v. Show that the design is a P.B.I.B. design with v/2 or (v—1)/2
associate classes according as r is even or odd. Obtain an expression for the
estimate of the treatment effects appropriate for this design.

12. The following data pertain to a paddy varietal trial with 16 varieties conducted
at Nagina Research Station in Uttar Pradesh. The plan and yields are given

below.

Plan and yields of 4x4 balanced lattice.

Yield in lb per plot of size 1/40 acre. Experiment with paddy
varieties of Nagina (U. P.)

Replication 1

Replication II

Block  I

Hi

Vl«

v6

33

25

36

32

Block  3

v2

v16

^12

V6

36

13

31

15

Block S

v8

v13

V8

Vl2

18

41

23

39

Block 7

v6

H

vn

Vll

13

40

25

26

Block 2

Vl3

H

V7

Vio

22

29

24

22

Block 4

v#

V8

vu

Vs

41

29

3&

25

Block 6

VlO

v.

Vl

Vl2

18

21

1+

44

Block 8

v#

v7

V2

Vl«

27

21.

30

31

202

DESIGN AND ANALYSIS OF EXPERIMENTS

Replication III

Block 9

Block 10

vi

v#

Vl6

v%

19

33

20

21

Vl

v12

>h4

19

36

30

17

Block 11

Block 12

>'16

vs

>ho

36

19

13

19

v2

V\3

Vs

Vll

29

28

31

40

Replication IV

Block 13

Block J4

Vl5
V?

v3

I’ll

50
32

23

38

Vl2

Vi

Vs

v16

55
22

23

39

Block 15

Block 16

vi

V»

vi2

V5

15

27

19

39

V10

v6

V14

>’2

34

20

28

24

Replication V

Block 17

Block 18

>'14

vl3

‘'is

vie

33

41

31

27

Block 19

Vg

v12

''ll

>’10

14

38

9

25

V3

vi

>’2

Vi

35

17

21

18

Block 20

V7

vs

Vs

V6

32

11

37

16

Analyze the data and interpret the results.

REFERENCES

1.

2.

3.

4.

Atiqullah, M. (1961).
215-18.

“On a property of balanced designs.” Biometrika, 48,

Bose, R.C. (1939). “On the construction of balanced incomplete block designs.”
Ann. Eugen. 9, 353-99.

Bose, R.C. and Nair, K.R. (1939). “Partially balanced incomplete block designs ”
Sankhya. 4, 337-72.

Bose, R.C. and Shimamoto, T. (1952). “Classification and analysis of partially
balanced incomplete block designs with two associate classes.” Journ Amer
Stat. Assn. 47, 151-90.

;

INCOMPLETE BLOCK DESIGNS

203

5.

Bose, R.C., Clatworthy, W.H. and Shrikhande, S.S. (1954), “Tables of parti¬
ally balanced designs with two associate classes.” North Carolina Agricultural
Experiment Station. Tech. Bull, no 107.
Bose, R.C. and Mesner, D.M. (1959). “On linear associative algebras corres¬
ponding to association schemes of partially balanced designs.” Ann. Math. Stat.

7.

8.

9.

10.

11.
12.

13.

14.

15.

16.

17.

18.

19.

20.
21.

22.

23.

24.

25.

26.

27.

28.

29.

30.

31.

30, 21-38.
Chakrabarti, M C. (1963). “On the C-matrix in design of experiments.” Jour.

Indian Stat. Assoc. 1, 8-23.
Connor, W.S., Jr. (1952). “On the structure of balanced incomplete block

designs.” Am. Math. Stat. 23, 57-71.
Connor, W.S. and Clatworthy, W.H. (1954). “Some theorems for partially
balanced designs.” Am. Math. Stat. 25, 100-112.
Das, M.N. (1958). “Reinforced incomplete block designs.” Journ. Ind. Soc. Agri.

Stat. 10, 73-77.
Das, M.N. (1958). “Circular designs.” Journ. Ind. Soc. Agri. Stat. 12, 45-56.
Ehrenfeld, S. (1953). “On the efficiency of experimental designs.” Ann. Math,

Stat. 26, 247-55.
Fisher, R.A. and Yates, F. (1948). Statistical Tables. Hafner Publishing Co.

New York. _
Fisher, R.A. (1940). “An examination of possible different solutions of a
problem in incomplete blocks. Ann. Eugen.” 9,353-400.
Giri, N.C. (1958). “On reinforced P.B.I.B. designs.” Journ. Ind. Soc. Agri.

Stat. 12, 41-51.
Giri, N.C. (1957). “On row balance in P.B.I.B. designs.” Journ. Ind. Soc.

Agri. Stat. 11, 168-78.
Giri, N.C. (1965). “On the F-test in the intra-block analysis of a class ot two
associate P.B.I.B. designs.” Journ. Amer. Stat. Assn. 60, 309.
Harshbarger, B.(1947). “Rectangular lattices.” Virginia Agricultural Experi¬

mental Station, Memoire, 1. „
John, P.W.M. (1964). “Balanced designs with unequal number of replications.

Ann. Math. Stat. 35, 897-99. v ,
Kempthorne, O. (1952). The Design and Analysis of Experiments. Wiley, New York.
Kempthorne, O. (1956). “The efficiency factor of an incomplete block design.

Ann. Math. Stat. 27, 846-49. ... , , . .
Kiefer, J. (1958). “On the nonrandomized optimality and randomized no
optimality of symmetrical designs.” Ann. Math. Stat. 29, 675-99.
Kiefer, J. (1959). “Optimum experimental designs. ’ Jour. Royal Stat. Soc. (»;,

21 272-319.
Kshirsagar, A.M. (1958). “A note on incomplete block designs.” Ann. Math.

KulshLhthI0 A.c. and Das M.N. (1968). “On derivation of initial Nocks of
BIB designs with more than one initial block.” Aust. J. Stat. 10, 75-8Z.
Martin, F.B. and Zyskind, G. (1966). “On combinability of information from
uncorrelated linear models by simple weighting. Ann. Math. Stat. 37, 1321 ■■ •
Mote, V.L. (1958). “On a minimax property of a balanced incomplete b

design. “Ann. Math. Stat. 29, 910-14. / ,i i
Nair, K.R. and Rao, C.R. (1942). “A note on partially balanced incomplete block

designs.” Science and Culture, 7, 568-69. . „ . «
Nandi, H.K. (1950). “On the efficiency of experimental designs. Cal. Stat.

Rao, C.R. (1947). “General methods of analysis of incomplete block designs.

Journ. Amer. Stat. Assn. 42, 541-61. cnnkhvh
Rao, C.R. (1961). “Study of B.I.B. designs with replications 11 to 15. Sankliya,

23,117-27.

204

DESIGN AND ANALYSIS OF EXPERIMENTS

32. Rao, M.B. (1966). “A note on equireplicate balanced designs with 6=v.”

Calcutta Stat. Assoc. Bull. 15, 43-44.

33. Rao, V.R. (1958). “A note on balanced designs.” Ann. Math. Stat. 29,290-

294.

34. Raghavarao, D. (1971). Constructions and Combinatorial Problems in Design of

Experiments. Wiley, New York.

35. Roy, J. (1958). ‘On the efficiency factor of block designs.” Sankhyd. 19,181-

188.

36. Roy, J. and Shah K.R. (1962). “Recovery of interblock information.” Sankhya

(A), 24, 269-280.

37. Saha, G.M. and Das, M.N. (1971). “Construction of P.B.I.B. designs through

2" factorials and some new designs.” Journ. Comb. Theory, 11, 282-95.

38. Shah, K.R. (1962). “An estimate of inter-group variance in one and two-way

designs,” Sankhyd (A), 24, 281-86.

39. Sinha, B.K. and Sinha, B.K. (1970). “Comparison of relative efficiency of some

classes of designs.” Cal. Stat. Assoc. Bull. 19, 97-122.

40. Sinha, B.K. (1971). “Contribution to comparison of experiments: Optimum
experiments for linear inference.” Unpublished Ph. D. thesis, Calcutta
University.

41. Smith, C.A.B. and Hartley H.O. (1948). “The construction of Youden squares.”

Journ. Roy. Stat. Soc. B, 10, 262-63.

42. Sprott, D.A. (1962). “Listing of B.I.B. designs from r=16 to 20.” Sankhyd 24,

203-04.

43. Vartak, M.N. (1963). “Disconnected balanced designs.” Jour. Indian Stat.

Assoc., 1, 104-07.

44. Wald, A. (1943). “On the efficient design of statistical investigations.” Ann

Math. Stat. 14, 134-40.

45. Yates, F. (1936). “Incomplete randomised blocks.” Ann. Eugen. 7,121-40.
46. Yates, F. (1936). “A new method of arranging variety trials involving a large

number of varieties.” Ann. Eugen. 7. 319-22.

47. Yates, F. (1940). “The recovering of inter-block information in balanced incom¬

plete block designs. Ann. Eugen. 10, 317-25.

48. Youden, W.J. (1940). “Experimental designs to increase accuracy of greenhouse

studies.” Cont. Boyce Thompson Inst., 11, 219-28.

CHAPTER 6

Orthogonal Latin Squares

6.1 Orthogonal Latin Squares

In Chapter 2 we used orthogonal latin squares for construction of Graeco-
Latin squares. They are also used for construction of balanced incomplete
block designs and square lattice designs. These are of much combinatorial
interest from the days of Euler who used such squares for arrangement of
soldiers according to their age, nationality, etc. He could not construct
such squares in some cases and made the conjecture that orthogonal latin
squares of order 4/i+2 do not exist. This conjecture has since been
proved false by Bose and Shrikhande (1959).

6.1.1 Definition : Latin Squares

A Latin square of order r is an arrangement of r symbols in r2 units arranged
in an rxr square such that every symbol occurs once in each row and
once in each column of the square.

Two latin squares of the same order are said to be orthogonal, if when
one is superimposed on the other each symbol of one falls on every
symbol of the other once and only once. ^

A set of latin squares is said to be orthogonal if every pair of these

squares is orthogonal.

6.2 Maximum Number of Orthogonal Latin Squares

A

The number of orthogonal latin squares of order r can be at the most

r—1.

This can be proved as below.
A latin square is said to be in a substandard form if the symbols occur
in its first row in the natural order. If the symbols used are the alphabets
A, b, C, etc., then in the first row they occur in the alphabetic order to
make a latin square substandard. It is always possible to write orthogonal
latin squares in substandard form by having a suitable permutation
over the symbols. For example, the following latin square can be
written in the substandard form by permuting D to A, A to B, C to C and

B to D.

206

DESIGN AND ANALYSIS OF EXPERIMENTS

Original square

Substandard square

D A C B

A C B D

B D A C

C B D A

A B C D

B C D A

D A B C

C D A B

We assume that all the orthogonal latin squares are in the substandard
form.

In an orthogonal latin square of order r any of r— 1 symbols can be
written in the second position of the first column, the remaining symbol
occurs in the first position of this column. As in each square a different
symbol is to occur in this position, the number of such squares can be at
the most r— 1.

When r is either a prime or a prime power all the (r— 1) orthogonal
latin squares can be constructed. When r is the product of different
primes or prime powers, MacNaish (1922) and Mann (1942) gave methods
of construction of (5— 1) orthogonal squares of order r where sis the
minimum prime or prime power factor of r.

We have given below a unified method of construction of orthogonal
latin squares of order r, by which (t— 1) orthogonal squares can be obtained
where, (i) t=s if r is the product of different primes and 5 is the minimum
of the prime or prime power factors of r and (ii) t=r if r is a prime or a
prime power.

6.3 Construction of Orthogonal Latin Squares

Let(r=sr Sg- • • ^p)where each factor, S[ is either a prime or a prime power.
We shall use the s, elements of the GF(s,) (i=l, 2,..., p) for forming
combinations of elements of the p different fields as below.

Let us combine the elements from the p different fields taking one
from each field in all possible ways. There are evidently r such combina¬
tions. If r is a prime or prime power, then p=1 and each such combination
is just an element of its field. We shall use such combinations of the/>
field elements as symbols for writing the latin squares.

Let the r combinations be written in a row and again in a column so
as to obtain the summation table of all possible sums, two by two, of
these combinations. This column will be called the principal column and
the row, the principal row.

By addition or multiplication of two combinations means addition or
multiplication of each pair of corresponding elements, (that is, occurring in
the same position) in the two combinations in the respective fields.

It can be easily seen that this summation table gives a latin square.
Next, each combination in the principal column is multiplied by a combi¬
nation, say, (0^2,a p) where at=£ 0 or 1 (1 = 1, 2,..., p). The resultant

ORTHOGONAL LATIN SQUARBS

207

column is the second principal column. Again, another summation table
is formed by using this second principal column and the first principal row.
This table gives a second latin square which is orthogonal to the one
obtained earlier.

Again, a third principal column is obtained by multiplying the different
elements in the first principal column by another multiplier, say,
(bv b2,..., bp) where or 1 or 0 (/=1, 2,...,/?) that is, the multipliers
are so chosen that no element in any field is repeated in the different
multipliers. A third latin square is obtained by adding the third principal
column and the first principal row. This square is orthogonal to the
previous two. This process is continued till suitable multipliers are
available.

As each time we have to introduce a new element 'in each field in the
multiplier combinations, we cannot get more than s— 1 multipliers where
s is the minimum factor of r. Each of these multipliers contains a
different non-zero element of the field of s and so not more than 5— 1 can
be taken without repeating an element in this field.

If r is a prime or a prime power, each multiplier combination consists
of only one element. We can, therefore, get (r—1) multipliers which are
the different non-zero elements in its field.

We have constructed below all the orthogonal latin squares of order

4 and 12 which are possible according to this method.

6.3.1 Construction of Orthogonal Latin Squares of Order 4

The elements in Galois field G.F. (2*) are 0, 1, a, a2 with a2-f a-4-1 as the
minimum function.

Table of smnination of the elements of G.F. (22)

First
principal
column

0
1
a

a2

Principal row
1 a

0

0
1
a

1
0
.2 a

7.2
0
1

cl*

a
1
0

Second principal
column obtained
by multiplying by a

Third principal
column obtained
by multiplying by a2

0
a

0

a1

1
(X2
a
0

a
0
1

1
0
a

0
a2
1
a

0
a2
1
a

1
x.
0
a2

a
1
a2
0

CL*
0
a
1

The three summation tables give three orthogonal latin squares.

208

DESIGN AND ANALYSIS OF EXPERIMENTS

6.3.2 Construction of Two Orthogonal Latin Squares of

Order 12

The two factors of 12 are 3 and 4. The elements in the two corresponding
fields are 0, 1, 2 and 0, 1, a, a2.

The 12 combinations which will be used as symbols for constructing

the latin squares are

Let us now obtain the summation table.

00, 01, 0a, Oa2, 10, 11, la, la2, 20, 21, 2a, 2a2.

First
principal Principal row
column

0a  Oa2

00

01

10

la

11

la2  20

00

01

0a

Oa2

10

11

la

la2

20

21

2a

2a2

21

2a

2a2

21

20

2a

2a*

2a2  2a

2a2  20

21

00

01

01

0a  Oa2

00  Oa*  Oa

0a  Oa2  00

0a2  0a

10

11

la

11

10

la2

la2

la

la2  20

21

2a

la

11

10

la

la*

10

11

2a

01

00

la

11

10

la2  20

21

2a

01

la

la2

10

11

2a

11

10

la2

la

21

20

10

11

la

la2

20

21

2a

2a2  2a

21 '  20

21

20

2a2  00

2a*  2a

01

01

00

Oa  Oa2

Oa2  Oa

2a2  20

21

Oa  Oa2  00

2a2  2a

21

20  Oa2  Oa

01

00

la2

la

11

10

01

la

la2

10

11

10

11

la

11

10

la2

la2

la

2a2  00

01  Oa  Oa2

2a*  2a

01

00  Oa*  Oa

2a*  20

2a2  2a

21

21  Oa  Oa2  00
20  Oa2  Oa

01

01

00

Second Summation table

Second
principal
column
obtained
by multi- Principal row
plying by

ORTHOGONAL LATIN SQUARES

209

We can take that the multiplier in the first square is 11 and that in the
second square is 2a. Hence, no further multiplier is possible as in the
first position 1 and 2 have appeared in the two multipliers and there is no
other multiplier left in the first field of 3.

It is easily seen that such summation tables always give latin squares.
As each row or column is obtained by adding a particular combination to
all the combinations, so no combination can be repeated in a row or
column.

Let a/ be the combination in the z'th position of the principal row and
be the combination in the yth position of the first principal column.
Let further c, and c2 denote two multiplier combinations for obtaining
two latin squares denoted by Lx and L2. The combinations in the (/, y)th
cell of the two latin squares are

a i+c$j and a/-fc2Py

«

These two symbol combinations can be equal only when (3, is the null
combination. In all other cases the symbols in the (/, y)th cell in the two
latin squares are different. But if cx and c2 have a common element in a
field with elements 0,1, U, t2, etc., then the combinations like (00- 010- -00),
(00- -0^00- -00), (00- -OLjOO- -00) etc. will occupy identical positions in the
two squares. Hence, the multipliers should contain each time a different
element in each field.

Again let

and

Then if

then

For,

Now, if

Then

*i+c1pJ=k

as+c] $t=k.

a.i + c$}=m

<*s +

«.i — cx.s = c1($l — $])

a / + c$j = a,+c2(3,—m

Ci 0/—(Sy)=c2 (p,—P7). That is, cl=c2

But this is not possible. This shows that any two cells having identical
symbols in one square, cannot have identical symbols in another square.

6.4. Construction of Orthogonal Latin Squares by Using

Pairwise Balanced Designs

An incomplete block design in v treatments with block sizes klt k2,..., km
where k^kj < v (/,y = l, 2,.. .,m) such that each pair of treatments
occurs together only in one block, is called a pairwise balanced design of
index unity. These designs were defined by Bose and Shrikhande (1959)
and were used to obtain orthogonal latin squares by associating them with
orthogonal latin squares and orthogonal arrays.

210

DESIGN AND ANALYSIS OF EXPERIMENTS-

6.4.1 Orthogonal Arrays Associated with Latin Squarbs

Given a latin square of order r, a row vector with r2 elements can be
obtained from it by writing the entry in the (z, j)th cell of the square
(i,j*= 1, 2,..r) in the {r (/— l)+7‘}tli position of the row vector. If there
are q latin squares we can get from them q such row vectors. With these
<7 vectors a qxr2 matrix can be written. We shall call the matrix an
orthogonal array of q constraints (rows) and r2 size. This array is of
strength two, if in any two rows of the array each possible pair of symbols-
of the latin squares occurs once only in the different columns.

If the q latin squares are orthogonal, the orthogonal array obtained,

from them is always of strength two.

Let us write r rows each containing the same r symbols in a given order
as in the above latin squares, so as to get an rxr square. We can form
another row vector of size r2 with this square. Taking this vector along
with the q vectors obtained from q orthogonal latin squares each written in
substandard form we get an orthogonal array of <7+1 rows, size r2 and of
strength two. Such arrays will be called R arrays.

Again let us write r columns each having the r symbols in a given order
once so as to get anrxr square. We form another vector with this square
as described earlier. Let us take this vector also with the R arrays to get
another orthogonal array with q+2 rows and of strength two. Such arrays-
will be called Q arrays. From an R array let us omit the first r columns.
The resultant array is of size r(r—1) with q+1 rows. Such arrays will be
called P arrays.

A matrix with v columns and t rows such that its zth column contains

the same symbol //(z=l, 2, .. .,v) will be denoted by Tvt.

Let there be b blocks in a pairwise balanced design of index unity.
With the symbols in its zth block let us form an orthogonal array of type P.
Let it be denoted by Pi with qi rows and size ki (lq— 1) where kt is the size
of the block and assuming that <7,-_1 orthogonal latin squares of order kt
are available.

For each block an array of the P type is obtained. Next, the following

array is formed by putting.the different P arrays one after another:

(PiPz- • Pb)•
The sizes of the different columns of the above array are unequal as the
number of rows in the different P arrays are different. Let qm be the
maximum number of rows present in each of the P arrays. Now, another
array is formed from (p^.. ./?<,)i by retaining only the first qm rows. Let
the array be denoted by

Then the following array

(PiPi-'-Pb)

Pi • • Pb)

is an orthogonal array of strength two with qm rows and size va, since

v + 2ki(ki — 1) = v2.

ORTHOGONAL LATIN SQUARES

!

211

Let the two symbols in the different columns of the first two rows be used
to denote the cell positions in a v x v square. Then by putting the symbol
which is present in a column in the third row, in the cell defined by the
preceding two symbols in the same column and repeating this process for
all the columns we get a latin square. Similarly, one latin square can be
obtained for each row of the array beginning with the third. These latin
squares are orthogonal.

6.4.2 A Modified Method: Falsity of Euler’s Conjecture

If all the blocks of a particular size are distinct so that no two blocks of
this size have any common treatment then such a set of blocks in a pairwise
balanced design of index unity is called a clear set.

When in a pairwise balanced design there is a clear set, the previous
method can be modified as below. For each block of a clear set, the Q
array may be taken instead of the P array. For all the other blocks P-type
arrays are used. The rest of the procedure is the same excepting that Tvqm
is replaced by T(v-s) qm where s is the number of treatments in the clear set
of blocks.

Similarly, if there be more than one clear set, 0-type of array is taken
for each block in the different clear sets. For the other blocks P-type
arrays are taken. The rest of the procedure is the same excepting that
Tyqm is to be replaced by -^(v—2 Si) qm where 2 si is the number of treatments
in all the clear sets.

This method is due to Bose, Shrikhande and Parker (1960). They showed
by these methods that it is possible to get at least two orthogonal latin
squares of any order other than 6. They used several other types of arrays
also to get the desired orthogonal latin squares. One of these methods is
through symmetrical differences and is described below.

6.4.3 Method of Construction of Two Orthogonal Latin Squares

of Order 3m+l where m is Odd

The (2m+ 1) residue classes mod(2m+l) along with xlt x2, ..., xm form
the 3m+l symbols of the. latin squares.

First, the following 4 vectors are taken:

=(0,0,0,,.. .0)

P2=(l,2,3,.. .m)

P3—(2m, 2m—1, ..., m+l)

^4==(^'l, * • • j Xm).

Next, the following latin square is written with the above vectors:

212

DESIGN AND ANALYSIS OF EXPERIMENTS

7?J -/Jg -^3 ^4

7?2

J?3 i?4 /Jj iv2

_/?4 /?3 .Z?2 ^1

The »th element of mod(2m+l) is added to each element in 0 keeping i?4
the same always. Let the resultant matrix obtained by this way of adding
the ith element be denoted by 0,-. Then the following matrix

(Oo»Oi> • • •> 02jk)

is an orthogonal array of size 4m(2m+l).

It is always possible to get two orthogonal latin squares of order m as
m is odd. Let us form two orthogonal latin squares with the symbols
Xj, x2, ..., xm. A Q-type array is then formed with the help of these two
orthogonal latin squares. This array has four rows and is of size m2.

Lastly, we form the array r(2m+1) 4. Then the array

(00 0j. . . 02m QT(2m+l) 4)

is an orthogonal array of strength two with four rows and (3m+1)2
columns.

Two orthogonal latin squares of order 3m +1 can be obtained from the
last two rows of the array when the first two rows are used for coordination
as described earlier. Taking m=3, we get two orthogonal latin squares of
order 10.

These same type of orthogonal squares of order 3m+l where m is odd
can however be obtained by a direct method developed by Menon (1961)
who provided an elegant demonstration of the existence of these squares.
This method is described below.

Denote by A the circulant matrix of order 2m+l

0 1 2 ... 2m

2m 0 1 ... 2m— 1

1 2 3 ... 0

and by B the matrix of order (2m +1) whose first (m+1) diagonals (counted
from the principal diagonal onwards from left to right) are respectively the
first (m+1) rows of + and the remaining m diagonals have the constant
elements 2m+l, 2m+ 2, ...,3m respectively, i.e..

ORTHOGONAL LATIN SQUARES

213

0 2m 2m—1 ... m-f-2 m+1 2m+l 2m+2 .

. 3m—1 3m

3m 1 0 ... m+4 m+3 m+2 2m+l ..

. 3m—2 3m—1

3m—1 3m 2 ... m+6 m+5 m+4 m+3

. 3m—3 3m—2

Be

2m—5 2m—6 2m—7 ... 2m+2 2m+3 2m +4 2m+5 ... 2m—3 2m—4

2m—3 2m—4 2m—5 ... 2m+1 2m+2 2m+3 2m+4 ... 2m—1 2m—2

2m—1 2m—2 2m—3 ... m 2m+1 2m+2 2m+3 ... 3m 2m

Let Cbe the (2m+l)xm-matrix whose columns are the last m rows of
.4 reckoned from the bottom upwards:

1 2 ... m ;

2 3 ... m+1

3 4 ... m+2

2m 0 ... m—2

0 1 ... m—1

Let D be the mx(2m+l) matrix formed by the rows of + beginning with
2, 4, 6, ...,2m respectively

2 3 4 ... 2m 0 1

4 5 6 ... 1 2 3

• •••••• • *

2m 0 1 ... 2m—3 2m—2 2m—1

Finally, let Li, Z,a be two mutually orthogonal latin squares of order m
formed by 2m+1, 2m+2, ...,3m. This is always possible as mis odd.

Then it can be verified that the matrices

form two mutually orthogonal latin squares of order 3m+l.

6.4.4 Two Orthogonal Latin Squares of Order 14

Eleven symbols are obtained from the residue classes mod 11 and xu x2
and x3 are three more symbols. The two 14 x 14 orthogonal latin squares
are obtained by using these 14 symbols.

214

DESIGN AND ANALYSIS OF EXPERIMENTS

Let as define four vectors as follows

$!=(), xv x2, xa

S2= 1,0, 0,0

53=4, 4, 6, 9
Si=6, 1,2, 8
The matrix 0 is formed with these four vectors as below:

S2 S3

$2 S3 S*
S3 iS4 5, S2

S1 S2 sa

By adding ith residue class mod 11 to each of the residue classes in 0 and
keeping xltx2 and x3 the same always, we get the matrices

0i(/=0, 1, 2,.10).

Then the matrix (00,0i,02,... ,010T(11)4 Q) where Q is the orthogonal arrays of
strength two with four rows and nine columns formed with the two
orthogonal latin squares with the symbols xlt x2, xa, is an orthogonal array
of strength two with four rows and 196 columns. From this orthogonal
array two orthogonal latin squares of order 14 can be obtained as described
earlier.

6.4.5 Two Orthogonal Latin Squares of Order 26

The symbols for these latin squares are the 23 residue classes mod 23
along with xlt x2 and xa.

Let us define four vectors as below:

5'1=0, 0, 0, 0, jcj, x2, x3

S2—3, 6, 2, 1, 0, 0, 0

S3=8, 20, 12,16, 20, 17, 8

S4=12, 16, 7, 2, 19, 6, 21

The matrix 0 is then formed with these vectors as in the case of 14x 14
latin squares as below.

Si S2 Sa S4

St S3 Si

s3 Si Si s2

Si Si S2 S3

■ORTHOGONAL LATIN SQUARES

215

By adding *th residue class mod 23 to each residue class in 0 and keeping
^i, *2, x8 the same, another matrix is obtained. Let it be denoted by
Of (1=0, 1,2,..., 22). Then, the matrix

(0o»0j,0S, ...,022, QT(2i)4)

is an orthogonal array of strength two with four rows and 262 columns.
Here Q is the same as used while obtaining the 14x14 latin squares.

From this array two orthogonal latin squares of order 26 can be

obtained as described in the case of 14x 14 latin squares.

EXERCISES
1. If r—2 mutually orthogonal latin squares of order r are available, show that the

complete set of (r— 1) orthogonal latin squares can be obtained.

2. It is known that in a sm factorial where s is a prime or a prime power, if the
block size is s2, a maximum of (s2—l)/(s—1) factors can be accommodated in the
blocks so as to save all main effects and two factors interaction. Treating such a
principal block as an orthogonal array of s+1 constraint and size s2, show that
(5—1) orthogonal latin squares can be obtained from it.

3. Show that using any three orthogonal latin squares of order 5 as three
symbols for the 3x3 latin squares, we can get two orthogonal latin squares of
order 15 from the two orthogonal latin squares of order 3 when each symbol of
5x5 latin squares is prefixed by the symbol of the 3x3 latin squares 0, 1, 2 to
which the 5x5 latin square is made to correspond.

4. Show that the procedure of obtaining orthogonal latin squares as described in
problem 2 can be extended to get all the (sm—1) orthogonal latin squares of
order r where r=slt s2 ..sp and sm is the minimum of the prime or prime
power factors of r.

5. Four persons bought 16 cows at the rate of four per person from four markets
such that each person bought one cow from each market. The cows belonged
to 4 breeds equally, such that each person bought a cow of each breed and the
four cows sold in each market belonged to different breeds. The cows belonged
to four different age groups equally such that each person purchased cows of
different ages, the cows sold in a market belonged to different age groups and
the four cows of every breed were of different age groups. Lastly, the cows
were marked by using four different colours such that four cows were marked
by each of the four colours, each cow belonging to a person was marked by
different colours, the cows purchased from each market were marked by different
colours and the cows belonging to each breed and age group were also marked
differently.

Describe the 16 cows in respect of the owner, market of purchase,breed,

age group and colour marking of each individual cow.

6. Show that it is impossible to get a set of nine or 36 cows of similar groupings,
that is, changing the group size to three or six but keeping the owner, market,
etc. classification the same.

REFERENCES

1. Bose, R.C. and Shrikhande, S.S. (1959). “On the falsity of Euler’s conjecture
on the non-existence of two orthogonal latin squares of order 4«+2.” Proc.
Natl. Acad. Sci. U.S., 45, 734.

216

DESIGN AND ANALYSIS OF EXPERIMENTS

2. Bose, R.C., Shrikhande, S.S., and Parker, E.T. (1960). ‘Further results on
the construction of mutually orthogonal latin squares arid falsity of Euler’s
conjectur:.” Can. J. Math. 12, 189.

3. Mac Nafsh, H.F. (1922). “Euler’s squares.” Ann. Math., 23, 221.
4. Mann, H.B. (1942). “Construction of orthogonal latin squares.” Ann. Math.

Stat. 13, 418.

5. Menon, P.K. (1961). “Method of constructing two mutually orthogonal latin

squares of order 3n+l.” Sankhya (A), 23, 281-82.

C. Raohavarao, D. (1971). Constructions and Combinatorial Problems in Design of

Experiments, Wiley, New York.

CHAPTER 7

Designs for Bio-assays and
Response Surfaces

7.1 Bio-assays

In certain investigations it is necessary to compare the efficacy of two or
more substances in respect of some of their common effects. Such
comparisons are not possible by comparing the effects of individual doses
of the substances. The techniques used in bio-assays are designed for
such comparisons. Bio-assays are thus a type of experiments with the
object of comparing the efficacy of two or more substances, or prepara¬
tions, like drugs, by using responses produced by them on suitable living
organisms. This technique is used more in pharmacological investigations
for comparing the potency of two or more preparations of individual
drugs.

Normally, two preparations having a common effect are taken for
assaying. One of the preparations is of known strength and is called the
standard preparation and the other is of unknown strength and is called
test preparation. The objective of the assay is to estimate the potency
of the test preparation relative to that of the standard preparation. The
potency of the test preparation is defined to be the ratio of two doses, one
from the standard preparation and the other from the test preparation
such that each of them produces the same response. This response is in
the form of some of their common effects when these are applied to suitable
living animals or other organisms.

Let zs and zt denote the doses of the standard and the test preparations
respectively such that each of them produces a pre-assigned response in
some living organism. Then the ratio

z.

is called the relative potency of the test preparation. If p is greater than
unity, it shows that a smaller dose of the test preparation produces as
much response as a relatively larger dose of the standard preparation and
hence the potency of the test preparation is greater than that of the
standard preparation. Similarly when p is less than 1 the potency of the
test preparation is smaller than that of the standard preparation.

An assay with two preparations containing the same effective ingredient
which is responsible for the response, is called analytical dillusion assay.

218

DESIGN AND ANALYSIS OF EXPERIMENTS

An assay with two preparations which have a common effect but do not
contain the same effective ingredient, is called a comparative dillusion
assay. The results obtained from analytical dillusion assays hold in general
and are not necessarily limited only to experimental conditions, while the
results obtained from comparative dillusion assays are limited by the
experimental conditions. For example, two preparations which do not
contain the same effective ingredient may produce a common effect on a
certain organism, say A, while they may not produce the same effect on a
certain other organism say, B. Then the potency estimated from such an
assay holds only for A organism and not for B. This is, however, not the
case with analytical dillusion assays. We shall discuss here only analytical
dillusion assays.

The purpose of bio-assays is ultimately to conduct an experiment for
estimating the doses of the standard and test preparations, such that each
of them produces the same response. Depending on the nature of the
preparations, the experimental subjects, that is, the type of living being or
organism being used as experimental units and the type of response, such
two doses can be estimated by various methods. One of these methods
attempts to estimate such doses directly and is called direct bio-assay. In
many situations this technique is not applicable and indirect methods are
adopted for the estimation of such doses. A detailed discussion of the
application of statistical methods to bio-assays is available in the works of
Finney (1964). We have discussed here only some of the topics which
are necessary for statistical designs for bio-assays.

7.2 Direct Assays

Ip direct assays the response is pre-assigned as the death of experimental
subjects as a result of application of each preparation. Other types of
responses like the appearance of a symptom which can be recognized as
soon as it happens, can also be used as preassigned response. It is further
■assumed that when the dose of a preparation of a drug or a poison under
assay, is administered to a subject, it produces the effect immediately
without any time lag, and the dose corresponding to the 'preassigned
response can be measured as soon as the response has occurred.

If a subject can tolerate up to a dose “d” of a preparation, such that
any dose greater than d will always kill it and any dose less than d will not
kill it, then d is called the tolerance of (he subject relative to the prepara¬
tion. The direct assay technique requires that the tolerance dose of each
subject should be measurable as soon as death occurs.

From a population of subjects as experimental units, we can think of
a population of tolerance doses relative to a preparation. It will be
assumed that for a given type of subject and preparation the distribution
of such tolerance is normal. In some situations the logarithm of tolerance
is also assumed to be normally distributed.

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

219

Design for the Assay
The assay technique consists of taking a number of subjects and dividing
them into two groups at random. One of the groups is allotted to the
standard preparation and the other to the test preparation. To each
animal the corresponding drug is administered by a suitable device such
that the administration can be stopped as soon as the preassigned response
has occurred. This dose is recorded as an observation. Likewise, for
each preparation, observations on all the subjects allotted to it are
obtained.

The averages of these observations for the preparations are taken as
the estimates of their equipotent doses. Denoting these two average doses
by y, and y, we get an estimate of the relative potency (R) as below:

A measure of precision of R cannot be obtained in any straight-forward
way. It is obtained by using a theorem due to Fieller (see Finney, 1964).
The theorem is reproduced below.

Fieller's Theorem
Let a and b be two random variables distributed normally such that

E(a)=a

E(b)=£

a

v(a) = vus2

Hb)=v22s2

cov (a, b) = v12s2

The fiducial limits of [x are obtained from the following

mi, mu--

m~~ (vn-2mv12+m2 v22+^ g-v12gVl2
U V22
1 —g

k22

where g=t2s2':2Jb2 and s2 is the error variance.

The precision of R depends on the precisions of y* and yt. One way
of increasing the precisions ofy* and y, is to allot a larger number of
subjects to each preparation so that v(ys) and v(y,) are smaller. But this
technique increases the cost of the experiment and sometimes a large
number of suitable subjects may not be available.

The other method is to take a homogeneous group of subjects, such
that they are similar in respect of those characters which influence the

220

DESIGN AND ANALYSIS OF EXPERIMENTS

response under consideration. These animals are then divided into two
random groups for allocation to the two preparations. It is, however,
risky to choose two homogeneous groups of subjects without regards to
the between group variation and then allot them to the two preparations.
This procedure may increase the precision of the estimates and }’t but
it introduces bias in the estimation of relative potency when the animals
in the two groups differ materially.

Fieller’s theorem gives a measure of precision of R by obtaining
fiducial limits of R. This method makes the assumption that tolerance is
normally distributed. The expression for the fiducial limits of R are some¬
what complicated. If, however, the logarithm of tolerance is normally
distributed, estimation of precision of R gets simplified as shown below.

When the logarithm of tolerance is normally distributed, the individual
tolerance values collected from the assay are transformed to the logarithmic
scale. If xs and Xt denote the averages of the logarithm of the tolerance
values for the standard and test preparations respectively, then

log R=Xs—xt.

The variance of xs—Xt can be obtained easily and provides a measure of
precision of log R. The estimate of R is obtained by taking the antilog
of xs—xt.

In many situations there may be a time lag between the administration
of the dose and the appearance of response. Alternative assay techniques
are necessary in such situations. Some of these techniques along with
their appropriate designs are described in Section 7.3..

7.3 Indirect Bio-assays

In indirect bio-assays the relationship between the dose and response of
each preparation is first ascertained. Then the dose corresponding to a
given response is obtained from the relation for each preparation
separately.

In order to obtain such a relation two or more doses of the standard
preparation are taken. Then their responses are obtained through an
appropriate experiment.

Let there be k doses of the standard preparation and each dose be
administered to n subjects. Some suitable effect of the doses on the subjects
is then observed from each of the subjects. Here the response is not
preassigned but takes its own value according to the strength of the dose
and nature of the subject. With the help of these responses which are
assumed to be normally and independently distributed with a constant
variance, the dose response relationship can be investigated as given
below. First the following table is made with the response observations.

DtSIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

221

TABLE 7.1

Responses from k Doses of the Standard Preparation

Response

Doses
d<L d$ . ..  dk

>21

>’31 • • .

>*1

>22

>32 • •

>*2

dx

>n

yi2

yin

>2»

>3» • • •

>fcn

Total

Si

S,,

S3 •••

Let 2 Si = G.

First, it is tested if the dose response relationship is linear. For this

purpose the following table is made.

Analysis of Variance for Testing the Linearity of Dose Response Relation

TABLE 7.2

Sources of variation

df.

s.s.

s.s.

m-S

F

Between doses

k-1

Regression of response on dose

1

Deviation from regression

k—2

5,2

<72
Tn=D

(Ydi)G
k

=>/v

T A. C.
if UjUt
/

D-R

Within doses (Error)

k(n-1)

T-D

Sd2

S2

Sd2/52

Total

kn—1

s yrf-
u

G2
-kn=T

The linearity of regression is tested by applying F-test on the ratio of
the mean squares due to deviation from regression and the within dose mean
squares. If the deviation mean squares is not significant, the relationship is
linear and further investigation is made accordingly. If this mean squares
is significant, then the doses are transformed to get another variate, say, x.
Usually, the following transformations are used

222

DESIGN AND ANALYSIS OF EXPERIMENTS

(i) x=log (dose)

(ii) x=(dose)x

where A is a suitable constant.

Using any of these transformations we get a value of x for each dose
as recorded in Table 7.1. These x values are called the dose metameters.
Now replacing the dose values by the dose metameters in the above analysis
of variance, we can form a separate analysis of variance table for each
metameter and then test the linearity of relation of the response on the
dose metameter. It will be seen that due to such transformation only the
regression s.s.and the deviation from regression s.s. change. If for a certain,
dose metameter the mean squares due to the deviation from regression is
not significant, then the relationship between response -and the metameter is
taken to be linear. Normally, simple values like 1, 2, etc. are chosen
'for A- Experience shows that suitable dose metameters are available in
usual situations, though it is not necessary that in all situations such
transformations are available.

Sometimes, the response variable is also transformed for linearizing the
relationship between the dose and response metameters. But in the present
case we shall restrict the investigation only to find out suitable transformation
of the dose variable.

The design and analytical techniques of the assay depends on such
linearizing transformation on the dose metameters. Depending on these
metameters, the indirect assays are divided into two broad categories,
called parallel lines assays and slope ratio* assays. These have been
discussed below.

Case 1 When x=log (dose) is the linearizing transformation.

Let y=as-rbx, (7.2)

denote the relation between the response y and x, where x,=log z, and z*
denote the dose of the standard preparation.

Denoting by z,a dose equipotent to z„ we have p=z,/zt that is,

log p=log zf—log zt=x,—xt.

That is, x,=log p+x,.

Substiuting for xs in the relation of the standard preparation,

y=as+bxt we get the relation for the test preparation as

that is

where

y=a*+ b (log p+x,)

y=at+bxt

a,=at-{-b log p.

(7.3)

Hence, the relationship for the test preparation is also linear like that of
the standard preparation for the same transformation.

An examination of the two equations for the two preparations shows

that the lines have the same slope and are, therefore, parallel.

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

223

As

we gei

at=as+b log p

log p

Of Qs

~Y~

where a, and at are the intercepts of the lines on the y axis and b is the
common slope.

If in an assay k doses are taken for each of the two preparations and
xs and xt denote the averages of the dose metameters and ys and yt are the
average responses for the preparations, then it is known that

and at—yt—bxt.
Substituting these values in

as=y,—bxs

we get an estimate R of p from

log R=xt-(7 '4)

From equations (7.2) and (7.3) it is seen that the two lines for the two
preparations should be parallel when the dose metameter is log (dose).
The assays corresponding to this transformation are, therefore, called
parallel line assays. Before going to estimate the relative potency, it is
desirable to test with the help of the data collected from the assay if the
two lines are parallel. Such a test is called validity test. It is also desirable
to test if the relation between response and dose metameter is linear. This
gives rise to another validity test. While planning the assay it is necessary
that suitable data are available for conducting these validity tests before
relative potency is estimated.

Case 2 If the linearizing transformation is

where z denotes the dose, then it is seen by following a similar procedure
as in parallel line assays that the equations of the two lines for the two
preparations are

y—a-\-btXs

y=a+b,xt

(1)

(2)

where bt=b,px.

Hence,

(7.5)

Since the relative potency is estimated from the ratio of the slopes of the
two preparations, the assays corresponding to the transformation zx is

called slope ratio assays.

An examination of the equations of the two lines shows that they

224

DESIGN AND ANALYSIS OF EXPERIMENTS

intersect on the response axis. A test of this fact gives rise to one validity
test. The other validity test is to see if the relation between the response
and dose metameter is linear. It is seen that the first validity test for slope
ratio assays is different from the first validity test for the parallel line assays,
though the second test is the same for both the types. So the plans for
the two types of assays have to be different. The plans for parallel line
assays have been discussed in Section 7.4.

7.4 Parallel Line Assays

A parallel line assay in which each of the preparations has an equal number
of doses and an equal number of subjects is allotted to each of the doses,
is called a symmetrical parallel line assay. We shall discuss here only
symmetrical parallel line assays.

Let the number of doses of each of the preparations be k. As there
are in all 2k doses in this assay, it is called a 2&-point symmetrical parallel
line assay or simply 2A>point assay.

Let n subjects be allotted to each of the doses and a suitable response
be measured from each subject. Suppose further that jj, s2,..., s* denote
the doses of the standard preparation and tx, t2,..., tk the same for the
test preparation. Denoting the response of the rth subject allotted to the
pth dose of the standard preparation by ytpT and the rth response from the
<?th subject of the test preparation by jtqr, the response data are first
arranged as in Table 7.3.

TABLE 7.3

Response Data from 2A>Point Assay

Response

Standard Preparation
Doses

Test Preparation
Doses

$2 • - • sk

h h ••• h

y>n

y, 21 •  • • y tki

ym

yt2i ■ • • >'tk]

jr«i2

y»22 ■ ■ • y$k2

yt 12

yt22 ■ • • ytk2

J'rtn

y>2n

• ■ y>kn

ytm

yt2n • • • • y kn.

Total

Si

sa ..  . s*

Tv

t2 ,.  ■ Tk

>

The analysis of the assay for conducting validity tests and for estimating

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

225

relative potency becomes very much simplified when the doses of each of
the preparations are taken in geometric progression as shown below:

s, cs, c2s,..c*-1 s and t, ct, c*t,...,c*-11

where s and t are suitable starting doses of the standard and test preparation
respectively and c is a constant which is the same for both the preparations.
A further precaution necessary while choosing the doses is that the doses
should be evenly distributed in the range of response in which the dose
response relationship was investigated for obtaining the linearing trans¬
formation.

Let xs, — log c'.y=log s-f-i log c (/=0, 1, 2,..k— 1)

and xtt = log c‘t=\og t+i log c (i=0, 1, 2,..k— 1).

Denoting by xs and x, the averages of the doses of the two preparations,
we get

and

So,

and

i . 1 i
x,=logs-l-Y log c

- . . .k—\.
X(= log t-)—— log c.

X,t — 3c,= ^/ — ^y-1) log c

xlf —x,= (ilog c.

(7.6)

(7.7)

Case 1 When k is odd we choose the base of the logarithm as c so that
log c is 1. The log dose as deviates from their mean can now be written
as below:

Standard preparation

k— 1
2 ’

k-3
2 ’

, -1,0, 1,.

k-1 k—3
2 ’ 2 *

Test preparation
1,0, 1,.

k-1
2 ’

k-1
’ 2 '

By choosing the base of the logarithm as above, these deviate values could
be made integers.

Case 2 When k is even, the base of the logarithm is taken as Vc s0 that
log c becomes 2 and hence all the dose deviate (/—(k—1)/2) log c become
odd integers as shown below.

Standard preparation
—(A:— 1), — (£-3),..1, 1, 3,..., {k— 1).

Test preparation
—(k— 1), -(*-3),...,-l, 1,3,..., (&—1).

226

DESIGN AND ANALYSIS OF EXPERIMENTS

The regression contrast for each preparation can now be obtained by
multiplying these deviate values by the corresponding dose totals and
adding them.

Analysis
As stated earlier the purpose of analysis of indirect bio-assays is two fold.
First, it is tested through the analysis of variance technique if, (i) the dose
metameter and response relationship is linear and (ii) the two lines for the
two preparations are parallel. If the tests reveal that the relationship is
linear and the lines are parallel, then the relative potency of the test
preparation is estimated from the relation

log R=xs—xt—^---Jt.

We have already obtained xs and X( at (7.6) and (7.l\ys~yt is given by

y»-yt=-

2 St-2 Tt

i
kn

The combined regression coefficient of the two preparations as obtained
at (7.8) below gives the value of b.

For the first part of the analysis the following contrasts among the

dose totals are obtained:

Preparation contrast (Lp)=—2 Si+2 7)

i i

(7.8)

Combined regression contrast

(LJ-  ~ to+ro--y-3 (S2+T2)~,

k-1

(Sk+Tk)

when k is odd,

Combined regression contrast

(L1)=-(/c-1) OVH^Mfc-3) (S2+r2)-... +(*-1) (Sk+Tk)

when k is even.

The difference between the two regression contrasts of the two

preparations is the parallelism contrast.

Parallelism contrast

when k is odd,

= -(fc-l) (S1-T1)-(k-3) (Sa-T,)-...-^-!) (,sk-Tk)

when k is even.

-'LY (Sk-T£i

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

227

Again, when k is odd

when k is even

4i(V)+(V)+---+i!}

6L,

kn(k2—])

b=_hi_
4{(fc—l)2+(fc—3)*+... + p}

3L,
~2kn (k2—1)'

The following analysis of variance table is then written for the validity
tests and estimation of error variance.

TABLE 7.4

Analysis of Variance in 2&-Point Assays for Validity Tests

Sources of variations

d.f.

s.s.

m.s.  F.

Preparation (Lv)

Regression (combined) (Z^)

Parallelism (Z,[)

1

1

1

L\\2kn

L\iD

I?!D

Deviation from regression

2fc—4

By subtraction

4/y*

4

s*d

Doses

2k-1

L S<2+s Ti2 ,
i i {sos«+r,)>>
n 2k n

Within doses (error)

2k («—1)

By subtraction

j2

Total

2kn— 1

„ {S(5f+r<)}2
S J^spr + 2 y2tqr ?»
pr qr n

The value of D, the divisor for the regression and the parallelism sums;of
squares in the above table is (J<n (k2—1))/6 when k is odd and (2fcn(A:8—1))/3
when k is even.

For testing the linearity of regression, the mean squares for the deviation
from regression is tested by the F-test using the within mean squares as
error. For testing parallelism, the “parallelism” component is tested.

If both these tests are not significant, then the relative potency can be

estimated as below.

log R=xs—xt—

— log y—log t+

Lp
kn

kn(k2—l)
6 L,

228

when k is odd.

or

where d=logi0 c.
When k is even

That is.

DESIGN AND ANALYSIS OF EXPERIMENTS

=log:

(£2-i) y

v 6 ’ L,

R=S-
t

antilog x'}

log R—log —

s Lp 2kn(k2—\)

kn

3L1

„ * , •, \d(k
R-- antilog <-j

2_  1)

Lp)
lS'

Precision of R can

be estimated through Fieller’s theorem.

Some Particular Cases
It is seen that in 4-point assay a test of linearity of regression is not
available, as the deviation from regression component does not exist in the
analysis of variance. In 6-point assay there are 2 degrees of freedom for
the deviation from regression. The following two contrasts of the dose
totals are the two deviation contrasts.

Quadratic (Z2) combined=(S1—2S2+S3)+(TX—2T2+T3)
Difference between quadratics (L2')^=(S1 — 2S2 + S^)—(T1--2Ti+T3).
When k is 4, there are 4 degrees of freedom for deviation from regression.
In general, the contrast L„ is represented by the nth degree orthogonal
polynomial (see Fisher and Yates table, 1963). The difference between two-
such polynomials is denoted by Z/.

Example 1: 6-Point Symmetrical Parallel Line Assay
Let s and t denote two initial doses of the standard and the test preparations
respectively. The other doses are shown in Table 7.5.

Contrasts of Validity Tests, Regression and Preparation in 6-Point Assay

TABLE 7.5

Dose (z)

X.i-Xs

Dose total
Preparation contrast
Regression
Parallelism
Quadratic
Difference between
quadratics

Standard preparation
c2s
cs

s

Test preparation
ct
c2t
t

—1

0

1

-1

0

1

-1
-1
—1
1

-1
0
0
-2

S3
-1
1
1
1

Ti
+ 1
-1
1
1

t2
+ 1
0
0
-2

T3
+ 1
1
-1
1

Divisors
6n
4 n
4 n
12/t

1

-2

1

-1

2

-1

12 n

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

229

TABLE 7.6

Analysis of Variance

Sources of variation

d.f. s.s.

m.s.

F.

Preparation

Regression

Parallelism

Quadratic

Difference between
quadratics

1 (—Si—S2—S3-+- Tx+ 7^-f- T3)2/6n

. 1 (-s1+s3-r1+r3)2/4«

1 (—SiH- S3+ 7\—Ts)2/4n
1 (s1-2s2+S3+r1-2r2+r3)2/i2«  %

Sl

S*/S2

S2qIS2

1 (S1-2S2+S3-7’i+272-r3)2/12/i

SDQ  sys*
S2

Within dose (error)

6(n—1) By subtraction

Total

•

. ayf,)

• 6" 1 f/h 6 n

Designs for Symmetrical Parallel Line Assays
The precision of the estimate of relative potency depends on the precision
of Lp and Lx and the error variance. In the previous planning of the
assays we assumed completely randomized designs. But taking all the doses
as treatments, randomized block designs can also be adopted, if the experi¬
mental animals can be made available in homogeneous groups. This
design is, however, not applicable when k is (say) greater than 3 or 4.
Usually small animals like rats, cats, guinea pigs, etc. are used as experi¬
mental units in bio-assays. These can be formed into homogeneous groups
of required size by equalizing them in respect of age, breed, housing and
other management, etc., to form blocks. Animals belonging to the same
litter are expected to be very much homogeneons and hence whenever
available, litters can be used as blocks. For a 2&-point assay each block
consists of 2k units to which the 2k doses are allotted at random when a
randomized block design is adopted. The analysis of the data is the same
as indicated earlier excepting that a component due to a block is also
obtained. If the number of doses is small a latin square design can also
be adopted to increase further the precision of the estimate of the relative
potency. Availability of suitable animals, however, stands in the way of
adopting latin square designs.

7.5 Incomplete Block Designs for Bio-assays

When the number of doses is large it may not always be possible to get

230

DESIGN AND ANALYSIS OF EXPERIMENTS

suitable homogeneous groups of experimental units for adopting rando¬
mized block designs. If litters are used as blocks a sufficient number of
litters of required size may not be available, even if the number of doses
is not very large. If, again, twin calves are used as blocks, it is not possible
to use a randomized block design when the total number of doses is more
than two. All these point to the necessity of incomplete block designs for
bio-assays. We have discussed below some incomplete block designs
which are suitable for parallel line assays. This work is mainly due to
Das and Kulkarni (1966).

The use of incomplete block designs for bio-assays is limited mainly
due to the inflexibility of the existing incomplete block designs. The
main purpose of these designs is the estimation of the difference between
all pairs of treatment effects with equal or nearly equal variances. In
bio-assays all contrasts are not of equal importance. The preparation
and the combined regression contrasts in parallel line assays are more
important because these two are used to estimate the relative potency.
The other contrasts are used for testing the validity of the underlying
assumptions which are normally likely to be satisfied. They are, therefore,
not as important as the preparation and regression contrasts.

When an incomplete block design is used for an assay the block effects
are not orthogonal, to the dose effects. The dose effects are, therefore,
estimated first by the method appropriate for the incomplete block design
and these effects are then used in place of the unadjusted dose totals in the
various contrasts indicated earlier. The sums of squares of these contrasts
are then obtained by squaring each contrast value and then dividing it
by a suitable divisor. The method of finding the divisors has been discussed
subsequently. These designs are not, however, optimum for parallel line
assays, as no special effort is made here to minimize the loss of information
on the preparation and regression contrasts.

By designing properly it is possible to estimate the preparation and regres¬
sion contrasts free from block effects. In such designs these two contrasts
can be estimated by the unadjusted dose totals as in randomized block
designs. A method for obtaining such designs has been discussed below.

Let sv s2,.. .,Sk denotek doses on the logarithmic scale of the standard
preparation. These are arranged in the ascending order of magnitude.
Similarly, tlt t2,..., tk denote the k doses of the test preparation in
logarithmic scale but are arranged in the descending order of magnitude.
The constant difference between two consecutive doses is the same in
magnitude in both the preparations. The doses of the two preparations
have been arranged in opposite directions for notational convenience as
we shall see below.

Let Si and Tj (i=l, 2,..., k, j=l, 2,.. ,,k) denote respectively the
observation totals of the ith dose of the standard preparation and the jth
dose of the test preparation.

First, an incomplete block design with the k doses of the standard

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

231

preparation as treatments is taken. Let k! < k be the block size of this
design. This can be any incomplete block design. The final assay design
is, then, obtained from it by including k' doses of the test preparation in
each block of the previous design. These k‘ doses are selected by using
the rule that if the dose si is included in a block of the original design,
then the dose /,• should also be included in the same block (i=l, 2,..., k).
As a result of arranging the doses of the two preparations in opposite
directions, the correspondence of si and U in the same block is possible.

This is an incomplete block design in 2k' plot blocks. By using this
design both the preparation and regression contrasts can be obtained from
the unadjusted dose totals as these two contrasts are free from block,
effects. The preparation contrast is free from block effects because an
equal number of doses from each preparation occurs in each block.
Again, an examination of the orthogonal polynomial contrasts shows that
in the regression contrast with n doses, the ith entry from the beginning as
also from the end backward are equal but with opposite signs
(i=l, 2,...— njl or (n—1)/2). This fact along with the fact that the doses
of the two preparations are numbered in opposite directions,ensures that
the coefficients of the totals S( and 2,.. .,k) in the combined
regression contrast are equal but with opposite signs. Since Si and T,
occur in the same block, the contrasts {Si— Ti) (i = l, 2,..., k) are free
from block effects. As the regression contrast of the dose totals is a
function of (S’,-—Ti), it is, therefore, free from block effects

Example 2: An 8-Point Parallel Line Assay
We take the following balanced incomplete block design with k—4 and
k'=2 written by using the doses slt s2, s3 and 54 as treatments.

Blocks

1 ^1^2
2 $1^3
3 *^1*^4
4 s.zs3
5 s3sA
6 s3st

The final design in four plot blocks along with the doses of the test
preparation is then the following design.

Blocks

1
2
3
4
5
6

232 DESIGN AND ANALYSIS OF EXPERIMENTS

The coefficients of the dose total in the different contrasts of the 8-point
assay are shown in Table 7.7. These, excepting Lp are taken from the
orthogonal polynomial tables of Fisher and Yates (1963).

Coefficients of the Dose Total in the Different Contrasts of an 8-Point Assay

TABLE 7.7

Standard preparation

Test preparation

Doses

Sl

•*2

■*3

Si

'1

h

h

U

Dose total

Si

Si.

S3

Si

Ti

Ti

t3

Ti

Contrasts L„

-1

—1  —1  —1

-3  —1

—3  —1

1

1

1  —1  —1

1

—1  —1

3

3

1

1

1  —3

3  —1

1

3

1

1

1

1  —1

-3

—3  —1

1

1  —1

—1

—1

—r

1

1

3  —3

3

1

-1

1

1

-3

3  —1

1  —3

3

-1

Lx

L\

L*

l'2

l3

K

The estimate of the regression contrast from the dose total is

3(S,—TJ-(52-r2)+(53-r3)+3(54-r4).

Since S) and Tt (i=l, 2, 3, 4) occur in the same block, Si — Tt is free from
block effects. Hence L± which is a function of (S'/—Tt) is also free from
block effects. It is seen that for the same reason L2' and Lz are also free
from block effects. As a matter of fact through such designs all contrasts
Li„ and L2n-i for different values of n are estimable free from block
effects.

The contrasts Lx', L„ and L3' are not free from block effects. To
estimate them the individual dose effects are first estimated. These are the
same as the estimated treatment effects obtained by following the method
appropriate for the design. These designs are actually regular group
divisible incomplete block designs. Hence, their analysis is easily
obtainable.

These estimated dose effects are then substituted for the unadjusted
dose total in the affected contrasts. Their sum of squares is found by
squaring each of them and then dividing by the coefficient of o2 in the
variance of the contrast of the dose effects.

If the initial design is a balanced incomplete block design, the estimate
of the affected contrasts obtained as indicated above, are mutually

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

233

orthogonal. By adding the sums of squares due to all these contrasts,
including the unaffected ones, the adjusted dose sum of squares is obtained.
The error sum of squares can now be obtained by subtraction.

In case of other incomplete block designs, the estimates of the affected
contrasts may not be orthogonal. In these cases the error sum of squares
has to be obtained from a complete analysis of the final incomplete block

designs adopted for the assay.

Example 3: For illustrating the method of analysis of a 6-point assay
Bliss (1952) presented a body of data collected on a vitamin D assay by
Coward and Kassner (1941). A randomized block design with 12 litters of
6 rats each was used for the assay. .

The same data have been used for the present illustration with suitable
modification as indicated below. To ensure comparability all the obser¬
vations collected by them are used but only after they are fitted into the

following incomplete block design.

The initial design is a balanced incomplete block design with k=3 and

k'=2. The final design in four plot blocks is shown below:

Blocks
1

2 JjJtMs

3

This design is repeated six times to accommodate all the 72 observations.
The block size in the present design is 4, while it was 6 in the design o
Bliss So two observations from each of the 12 blocks were kept aside as
shown by blanks in the first 12 blocks presented below. With these
24 observations, which are taken out of the original blocks, 6 blocks
were formed ignoring their litter differences but maintaining the dose
observation relation. The six blocks are actually the same as the three
blocks of the above incomplete block design repeated twice.

Thus, we have finally the incomplete block design of six doses distri¬
buted in 18 blocks of four units each. The data along with the design

are shown in Table 7.8.

234

DESIGN AND ANALYSIS OF EXPERIMENTS

The Design and the Data of a 6-Point Parallel Line Assay (Doses in \ig)

TABLE 7.8

Standard preparation
Doses Si s% s3
2.5 5 10

Test preparation

t3 t2 tx Block total
2.5 5 10

Blocks

1

2

2

6

3 —

4

5

9

10

6 —

7

8

4

11

9 —

10

11

4

12

12 —

13

14

4

7

15 —

16

17

2

4

18 —

8

—

6

11

—

7

10

—

9

7

—

8

4

—

15

4

—

10

—

9

12

—

17

5

—

9

14

—

9

IT

—

8

10

—

13

13

Dose
total

75

sx

99

S2

Adjusted total

-25.75

130

*3

1.25

22*

9

—

6

14

—

9

11

—

8

10

—

8

5

—

8

6

—

18

112

—

3

4

—

8

6

—

3

5

—

15

7

—

3

6

—

5

4

69

r.

22.50 ■

<2/

-38.50
QzT

26

26

28

47

45

27

38

38

36

31

51

34

22

27

39

18

34

45

61.2

7

8

—

13

10

—

13

15

—

10

15

—

9

9

—■

6

12

—

127

Tx

14.25
Q%T

26.25

Gir

Unadjusted s.s. due to blocks=358.00.
The different contrast values along with their divisors are shown in Table

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

235

Contrasts, Divisors and Sum of Squares for Data of Table 7.8

TABLE 7.9

Unaffected contrasts

Value of contrast

divisor for s.s.

sum of squares

Lp

Lx

w

Affected contrast

w

L*

4

113

-35

-3.00

-46.50

6x12

4x12

12x12

4X9

12X9

0.22

266.02

8.51

0.25

20.02

The divisors are the coefficients of o2 in the variance of the contrats
estimator. If h denotes the coefficient in a contrast C of ith dose, then
the divisor for C is r2 /,-2 when C is not affected. When C is affected r is
replaced by rE in the present case, where E is the efficiency factor of the
original balanced incomplete block design. As r—12 and £=9/12,
rE=9. In the last two contrasts above, 9 has been used as multiplier of
21? instead of 12 which has been used for the unaffected contrast. The
error and other sums of squares are shown in Table 7. KM

TABLE 7.10

Analysis of Variance of Data in Table 7.8

Source of variation

d.f.

s.s.

m.s.

F.

Between blocks (unadjusted)

17

358.00

Preparations

Regressions

Parallelism

Quadratics

Difference between quadratics

All contrasts (doses)

Error by subtraction

Total

1

1

l

1

1

5

49

71

0.22

0.22

266.02

266.02

0.25

20.02

8.51

295.02

342.98

996.00

0.25

<1

20.02

2.86 n.s.

8.51

1.22 n.s.

7.00

236

DESIGN AND ANALYSIS OF EXPERIMENTS

All the validity tests are satisfied as in the original data. It is also
seen that the error variance has not increased due to regrouping of the
observations.

The estimate of relative potence is

R=W antilog jy yj where <f=log?0

=anti!og {3~|.

7.6 Slope Ratio Assays

We have seen in Section 7.3 that the linearizing transformation

x=zK

leads to slope ratio assays. The equations for the lines of the two
preparations are

y=a+b,bx,

y=a+b,x,

where bt=p'b, and A is a known constant determined by the trans¬
formation. Before going on to estimate the relative potency it is necessary
to ascertain by an appropriate test if the two lines intersect on the response
axis. As the dose takes the value zero on the response axis, it is necessary
to include a blank dose in the assay for the purpose of a validity test.
Thus, if there are k doses of each of the two preparations in a slope ratio
assay, the total number of doses is 2k+\. If against each of these doses
an equal number of subjects, say, n is allotted, then the assay is 2k+\
symmetrical slope ratio assays. We shall now discuss only the symmetrical
assays.

The regression coefficients bs and bt of the two lines can be estimated
subject to the fact that the two lines intersect on the response axis by
fitting the relation

y=a-\-bsxs-\-btXt (7.9)

by using the data described below.

Let Sy st,..., sk denote k equispaced dose metameters of the standard
preparation and tx, t2,...,tk denote the same for the test preparation
By changing the origin and scale of the doses of each preparation thev
can be written as ’

k— 1 k-2 2 1
’ k ’ k k ’ k

for each preparation.

Let there be n subjects allotted to each of the doses and the total of
the observations from the zth dose of the standard preparation, when the
doses are arranged in the ascending order, be denoted by St and that of

DESIGN FOR BIO-ASSAYS AND RESPONSE SURFACES

237

the test preparation by 7i(i=l, 2,..k). Let C denote the total of the
observations from the blank dose. Now, the data, as shown in Table
7.11 can be used to fit the above relation by the usual method of partial
regression fitting.

TABLE 7.11

Doses and Data of a 2A:-|-1 Point Slope Ratio Assay for Fitting the
Partial Regression Equation

Doses

Total Response

xt

l- »

r o

•

l

0

0

•

0

0

• •

0

1
k

2
k
• *

1

0

y

Si

*5*2
•

•S*

Ti

Tk

Ci

■

V .. Hi:

, .

)

Validity Tests
While investigating the dose response relation the blank dose is not usually
considered. When the blank dose is taken in the assay a question arises,
viz., does the linearity of relation hold up to the zero dose? It is, therefore,
necessary to test if the relation y=a+bsxs+btxt holds up to the zero dose.
This provides one validity test. For this test the difference between d and
o' is tested where d is the estimate of a, the constant term in (7.9) when the
relation is fitted by including the blank dose and a' is the estimate of a
when the relation is fitted by omitting the observation from the blank dose.
This contrast is called the blank contrast. A general expression for this
contrast in terms of the dose total has been given afterwards.

Another fact to be verified is that whether the two lines intersect on the
response axis. For this the two lines are fitted individually ignoring the
blank dose and then their intercepts on the response axis are compared.
This provides another validity test. The corresponding contrast is called
intersection. The expression for this contrast in terms of the dose totals

has also been given below.

238

DESIGN AND ANALYSIS OF EXPERIMENTS

Blank contrast, L,B—k{k— 1) C—(2k—2)(S1-\-Ti)—(2k^~^)(St-\-Ti)

-(2k-S)(Sa+T3)+.. .+(fc-l)(&+2i)

, _ e • rik(k—\)(k2-\-k-\-\)
The divisor for finding its sum of squares is-2k+\-'

Intersection contrast=L/=(2A:—2)(S1—7\)+(2fc—5)(S2—T2)

+(2fc—8)(S3—r3)+ ...-(£-1) (Sk-Tk).

Its divisor is nk(k— 1).

Designs
We shall consider here the following three designs for symmetrical slope
ratio assays with 2k-f-l doses.

(i) Randomized block design.
(ii) Balanced incomplete block design with 2k+1 doses as treatments

and block size, say, kv

(iii) Modified balanced incomplete block designs.

The first two designs are the usual ones and can be obtained without
difficulty. The third design is obtained by first taking a balanced incomplete
block design taking the A: doses of the standard preparation as the treatments.
Let k' denote the block size of this initial design. The final assay design
is obtained by including in each block of the above design k' doses of the
test preparation. The rule for choosing these test preparation doses is that
if the dose st of the standard preparation is included in a block then the
dose ti is also included in the same block (i=l, 2,..., k). The blank dose
is included in each block. Here the doses of both the standard and test
preparations are arranged in the same order of magnitudes but not in
opposite orders as in parallel line assays. We shall now discuss the analysis
of these three designs in a general way.

Analysis
Let yui where one of i or j is zero, denote the observation in the /th block
coming from /th dose of the standard preparation and y'th dose of the test
preparation. y0o/ denotes the observation from the blank dose in the lth
block. Let further xsi and xtJ denote in general the variables representing
the doses of the standard and test preparations respectively.

We take the following model for the analysis:

Yiji—a-ybsXsiA-btXtiA-ri-j-eui (7.10)
where h denotes the effect of the /th block and em is the error component
assumed to be normally and independently distributed with a common
variance, as.

The details of estimation of these contrasts have been given by Das and
Kulkarni (1966) in a general way. We have given the final results for each
of the above three designs.

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

239

For any of the above designs we define

Qia—Si—(sum of the averages of the blocks containing the z'th dose of

standard preparation) (z=l, 2, . ..,k)

QiT=Ti—(sum of the averages of the blocks containing the z'th dose of test

preparation) (z'=l, 2, ..k).

The normal equations for estimating bs and bt after eliminating block effects

are then

Cib'+Cfr^l 2 iQis

K i=i

C26,+CA=4 2 iQiT.

K i=l

The solutions of the equations are given by

bs=v1 2 iQts-f v2 2 iQfT
i l

br=v2 2 iQis+v1 2 iQ,T
i i

The values of Cx, Ct, vx and v2 for the different designs are shown below.

Case 1 Randomized block design with r replications

C1=C1R=r(k-l)(5k2+5k+2)/\2k(2k+l)

C2=C2R=-r(k+iy/4(2k + l)

Vj—Vj^ =M(5k2+5k+2)l(k2+k+\)

v2=v2r = ?k(k+l)M/(k2 + k+l)

where M=3k/r(k+l)(2k+l).

Here CXR, C,,R, \\R and v.2R denote the values of Cx, C2, vx and va respectively
for the randomized block design.

Case 2 Balanced incomplete block design with parameters v=2fc+l,

k^r,^.

Cx=Cxb=ECR v1=v,6=v1«/£

C2=C2*=£C2* v2=v2b—v2R/E

where E is the efficiency factor of the balanced incomplete block design

and is given by

A(2fc+1)

E rkx

Case 3 Modified balanced incomplete block design with k’ as the block
size and r, the replication of the initial B.I.B. design.

C1=C1M=r (k+1) (5kk'+2k'+2)/l2k (2k'+l)

C2=C2M = -r(k + l) (3kk'+k+2k')/l2k (2fc' + l)

240

DESIGN AND ANALYSIS OF EXPERIMENTS

V\=ViM=M (5kk'+2k'+3?c+2)/(kk'+k+1)

v2*±v2m=M (3kk'+k+2k’)/(kk'+k+l).

Since bs and b, cannot be estimated independently, we cannot get their sum
of squares by adding their individual sum of squares.

The combined sum of squares of bs and b, is as below

s.s. (bs, b,)=~ 2 iQ,s+~ 2 iQ?

K /-i fC

with 2 degrees of freedom.

To get the estimates of the contrasts required for validity tests, first the
estimates of the effects of the blank dose c, st and U (i= 1,2..., k) have to be
obtained by following the method appropriate for the design.
For the randomized block and the balanced incomplete block designs,
these can be obtained in a straight forward manner. The modified
balanced incomplete block design belongs to the class of reinforced designs
(Das, 1958). The estimates of the dose effects from these designs are given
below:

2k' +1
r (2/c + l)-2(r-A)

2 (r-A) g01
r(2k+\) J

where r and A are the parameters of the initial B.I.B. design.

Si-tt

Sj-Tj
r

(2^ + 1) g0
r (2A:-hl)

where g, = g<s+g/r and g0 is the adjusted total of the blank dose.

The contrast for validity tests are estimated as linear functions of Qh
go. Si and 7). These functions are obtained by first replacing St by st and
Tt by tt (i=l, 2,.. .,k) in the formulae of the contrasts given earlier and
also by Finney (1964). Next, the estimates of st and U as obtained from
the above solutions are substituted in these contrasts of the dose
effects. The sum of squares due to a contrast is obtained by squaring the
contrast and then dividing the square by a divisor obtainable as indicated
below.

Let a contrast L be estimated as below:

L /0c+2 li ($/ + //).—tfogo+2 q, Qi%
i i

Then its divisor is qJo+2 2 q( l{.

i

Normally, the affected contrasts are functions of ($;+!,). The function L
has, therefore, been taken as above.

In modified balanced incomplete block designs all the contrasts of the
form L'm as defined in parallel line assays, are unaffected. They can, there¬
fore, be estimated from the unadjusted dose total. The intersection contrast
Li is also unaffected by the blocks.

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

241

The different steps in the analysis of a modified balanced incomplete

block design has been illustrated below through a 7-point assay.

Example 4: Bliss (1952, p. 568) has reported the data from a 9-point
slope ratio symmetrical assay on riboflavin content of yeast. The data
were collected by adopting a randomized block design with two replications.
For the present illustration we have omitted the observations from the
highest dose of each preparation. The remaining data have been taken as
if they resulted from a modified balanced* ncomplete block design from a
7-point assay in blocks of five units with two replications of each non¬
blank dose. Taking as the initial design the following balanced incomplete
block design

the final assay design was obtained as below.

v=b=3, r—k—2, X=1

Blocks

1 ij <&2 12 C

2 sx s3 t3 c

3 s2 s3 t2 t3 c

The observations from the original assay were fitted into the above design
maintaining the dose block relation. The observations of titer per tube
arranged according to this design are shown in the following table.
Originally, there were only two observations from the blank dose. But as
the present design requires three observations from the blank dose, the
third observation from this dose has been taken arbitrarily as 0.76.

The coded doses for each preparation have been taken as 1/3, 2/3

and 1.

TABLE 7.12

Data and Assumed Design as Example of a Modified B.I.B. Design

Blocks

Blank
c

Doses

Standard

*2

**3

h

Test

h

h

Total

1

2

3

0.72

0.78

0.76

2.15

—

2.30

4.35

4.05

—

.. „

6.10

5.60

2.35

—

2.45

4.40

4.70

—

—•

13.97

6.10

21.73

5.10

16.21

Total

2.26
C

4.45

Si

8.40
s2

11.70

s3

4.80

Tx

9.10
Ti

11.20
Tz

51.91
G

242

DESIGN AND ANALYSIS OF EXPERIMENT

Adjusted -8.122 -1.586 1.260 4.112 -1.236 1.960 3.612
Totals Q0 Qf Qts Q& Q/ Q2T Q/

estimated dose-2.901 -1.332 0.469 2.176 -1.157 0.819 1.926

effects

^2

^1

Total sum of squares=52.064

Block sum of squares=6.380

Adjusted dose sum of squares=c£?0+2 f, QiT

i i

=45.205

Error sum of squares=52.064— 45.205—6.380=0.479

l(Qls+2Qls+3Qas)=4A23

1

(0ir+222r+30sr)=4.5O7

The equations for finding the regression coefficients are given by

the solutions are

_81 _45'
112 112

81

\112 112/

£,=5.010

£,=5.037

Sum of squares due to regression coefficients is

4.423 £,-|-4.507 £,=44.861.

The contrasts for the validity tests for 7-point assay together with their
divisors and sums of squares are given in Table 7.13.

Contrasts and Divisors for Validity Tests and their Sum of Squares

TABLE 7.13

Unaffected contrasts Coefficients of dose total (,) contrast Divisor s.s.

C Si S2 Sa ^ r2 Tz val uc=2/,(S,—T,) 2„Z/,2

Intersection L\

0

4 1  —2  —4  —1

2  —3.10

Difference between
quadratics (Z.2')

Affected contrasts

0

1 —2

1  —1

2  —1

1.55

Blank ( Lb )

6  -4 —1

2  —4  —1

2  —0.53

Quadratic (£t)

0

1 —2

1

1  —2

1  —0.96

84

0.114

24

0.100

75
2

15
2

0.008

0.123:

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

243

The divisors for the affected contrasts have been obtained as below.

Lb — 6C—4(^4-tj — (s2-\- f2)+2 Cs3-W3)

e»-f Qi-Iq,+\q*

Hence the divisor

=6 X ^+2 [(-4) (-|)+(-Dx(-|)+2x|]

75
12

Again,

Qx-\ e.+| e3

Divisor =2(lx|+(-2)(-^ + lx|)

15
= 2 •

From Table 7.12 we get

Q0=-8.122, 01=01s-f 0lr=—2.822.

Similarly, 02—3.220 and 03=7.724

TABLE 7.14

Analysis of Variance for the Modified B.I.B. Design

Source of variation

d.f.

s.s.

m.s.

F.

Blocks

Regressions

Blank

Intersection

Quadratic

Diff. bet. Quadratics

Error

Total

2

2

1

1

1

1

6

6.380

44.861

0.008

0.114

0.123

0.100

0.479

14

52.064

22 430

280**

0.008

0.114

0.123

0.100

0.080

< 1

1 An.s

1.5 n.s

1.2 n.s

All the validity tests are satisfied as in the original data. The ratio of
the regression coefficients is

5.037
5.010

= 1.005

244

DESIGN AND ANALYSIS OF EXPERIMENTS

To obtain the relative potency this ratio has to be multiplied by the ratio
of the two highest doses of the two preparations included in the assay.

Q 1
v(5,)=v(Zu)=-jj2xO.08=0.058

cov (bs, bt)=zYT2X 0-08=0.032.

The fiducial limits of the estimated relalive potency can now be obtained
through Fieller’s theorem.

7.7 Response Surface Designs

7.7.1 Introduction

The objectives with which the factorial experiments are interpreted are
two fold. One objective consists of studying the main effects and interac¬
tions of the factors. In this approach it is postulated that the response
from a treatment combination is a function of the main effects and interac¬
tions of different factors. However, these assumptions are not adequate
when the factors in the experiment are quantitative in nature. The second
approach of interpretation of data from factorial experiments consists of
studying the relationship between the response as a dependent variate on
the factor levels. This approach helps to understand better how with the
change in the levels of application of a group of factors, the response
changes. A combination of the levels of the factors which leads to
certain optimum response can also be located through this approach.

In order to get the relation between the response and the factor levels
the treatment combinations have to be suitably chosen. The treatment
combinations of the ordinary full factorial need not be the best for fitting
the relation. It is, therefore, necessary to search for a suitable set of
treatment combinations by using which a stipulated relation can be fitted.
Such a set of treatment combinations is called a response surface design.
Actually the factor-response relationship is called response surface. These
surfaces can be linear, second degree and third degree polynomials, and
so on. We shall discuss here only the first and second degree surfaces,
construction of designs suitable for fitting them and methods of
interpretation of the data.

7.7.2 Linear Response Surface Designs

Let there be v factors each at s levels. Suppose we choose N treatment
combinations to form our design. Let Xt denote the ith factor and x,u be
the level of the ith factor in the uth treatment combination (i=l,..., v,
“=!,-• -’N)- Let denote the response obtained from the nth combination
of the factors. Assuming that, yu is linearly related with (xlu, x2u.xvu)

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

245

we have to find a design consisting of N points by using which the linear
surface relation can be fitted with some desirable properties.

Let ... -\-bvxYu-\-^u (7.11)

denote the relation where b0, bv... ,bv are the parameters of the surface
and eu is a random variable with zero mean and constant variance.

We shall apply the least squares method of estimation for fitting the
surface, (that is, for estimating the coefficients in the surface) by using the
observations collected through the following design consisting of N points:

x u»-

• ,*lv

XNi> • • • ,^-iVv

(7.12)

Applying the least squares technique the following normal equations are

obtained:

N N
M>0+^i 2 Xm d-• • • 4" bv 2 Xyu—^yu

fc=l u=l u

60 -bi Xw yu (7.13)

bn ^Xyu~\~b-± XXiu Xyji-f- • • • +bv 2)Xyu 2 Xvu yu

u

In all the above equations the summation is over the design points. One
of the purposes of choosing a suitable design is to simplify the solution of
the above normal equations. The other purpose is to increase the precision
of the estimates of the parameters b0, blt... ,bv.

As we have to fit a linear relation the minimum number of levels of
each of the factors is 2. There is a series of linear response surface
designs with each of the factors at two levels. For each factor first a
range of the levels is fixed. For a factor like nitrogen fertilizer a range
like 0 to 80 lbs. of nitrogen per acre may be fixed. In specific cases the
range has, however, to be fixed according to the prevailing conditions,
taking into account the experimenter’s demand and available resources.
Preferably the two extreme doses defining the range are taken for the
experiment and denoted by the codes -1 and 1 for each of the factors.
Each of the treatment combinations will, therefore, be of the iorm
/ , 1 _L.\ that is, consisting of only 4-1 and — 1 as elements.
To simplify the solution of the normal equations the design has to be so
obtained that all the following relations hold:

Li#=0 (i —1, 2,.. .,v)
u—l

2 Xiu xju— 0 (i^ji Uj 2,... v)
u-l

Under these conditions the normal equations reduce to

Nb0='Zyu

bi ^Xiif—^Xtu yu (,=2,.. .,v)

(7.14)

(7.15)

246

DESIGN AND ANALYSIS OF EXPERIMENTS

Hence the solutions of the normal equations are

ly. and 0=1. 2.V) (7.16)

Denoting the variance of yu by o2 and assuming that yv y2,... ,yv are
uncorrelated, we easily get the variance of bj as

V (b,)=o2/(2xiu*) (7.17)

Plackett and Burman (1946) gave a series of designs satisfying the above
conditions. They gave designs for all values of N which are multiples of
4 up to 100, except 92. (The design for TV—92 is now known.) For any
such value of N, they could get a design with the maximum of (TV—1)
factors. Thus their design matrix has N— 1 columns and JV rows. By
omitting say K, columns from the above design, we always get a design in
(N—K— 1) factors with N design points. The design matrix of these designs
(the Nx v matrix of treatment combinations) is called a Hadamard matrix.
There are various other methods of construction of linear response surface
designs. Two of the methods through which many of these designs may
be obtained have beeen described below.

One of the methods of construction of a linear response surface design
is to take a complete symmetrical factorial of the form 2V and then change
the origin of the doses to the middle of the range.

As this method often leads to a large number of design points, it is
necessary to evolve a method for reducing the number of points. Such a
method (see Das 1964) consists of first getting a confounded factorial
where no main effect and two factor interactions are confounded and then
choosing the principal block for the design. This block is then rewritten
by changing the origin and scale as indicated above.

7.7.3 Second Order Response Surface Designs

There are situations where a second degree response surface is more
suitable. Such a surface is written in general as below

y=b0+b1x1+b2x2+ .. .-\-bvxv+bllx12+b22x2*+...

+6yVxv2-(-612x1x2+Z>13x1X3+... +6y,v-iXy_jXy. (7.18)

The problem now is to choose a suitable design by using which the
above surface can be fitted without much involvement and further possessing
certain desirable properties.

Let us take the following design of N points for fitting the surface:

..Xy

■*n>

X21’

•*]2>  . . . ,Xjy

X22’ • . . . ,X%y

XN2 ■ • X^y

(7.19)

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

247

Let ylf y2,...yN be the N observations obtained from the above N points.
To obtain a fit of the surface through the method of least squares, we
get the following normal equations:

27=iY7>0+612x1+^22x2+ ... +6112x12+fc222x22-f... +7>122x1;t2+...

2x1_F=&02Xi4-7?12.x'i‘'-f b^2x^x2-\-... —|-~L • • • T-

• •• • • • ••• •••

2x1zy=b02x]J+b12x13+b22x12x2+ ... +bn2x1i+b^x12x22->r ... +

Z>122x12x2-|-...

'Lx1x2y=b02x1x2+b12x12x2+... +Z>n2x18x2+... +

22xx2x22+32x12^2^3 + •••• (7.20)

All the summations in the above expressions are over the design points.

In order to simplify the solution of the above normal equations, the
design points have to be so chosen that all sums like 2xif 2XiXj, Ixf-Xj,
2x,3, IXiXjXk, 'Zx? ■ xj ■ Xk, 2xt3Xj, 2xiXjXkX/ are equal to zero. That is, all
sums of products in which at least one of the x's is with an odd power
are zero.

The other simplifying conditions are given below:

(i) 2xj2=constant - 7VA2, say, that is same for each factor

(ii) 2xj4=constant=cAA4

(iii) 2xi2Xj2=constant=iVA4

where c, A2 and A4 are constants.
For a design satisfying the above conditions, the normal equations reduce
to the following:

2y=Nb0-\-N'\i (bu-\-ba2~\~ •.. +^v»)

2Xiy=N?i2bi (z —1,2,..., v)

2x{Xjy=N\bij (zV7=l, 2,..., v)

2x12y=N’A2b0JrcNXib11JrN'Xi (b22-\-b23-\- ... +7>yy)

2x22y--NX2b0-\-cN\b22+N‘\t • •. +6VV)

* i • ••• •••

2xy2y= N\2b0+cAA47jv»+iVA4 {bllJrb22+... +&y-i,v-i)

(1)
(2)

(3)

(4)

The equations at (2) and (3) provide the solution of bi and btj immediately.

To obtain the solutions of the other equations let us put

t>ll +^22"t" • • •

Now equation (1) becomes 2y=Nb0-\-N'\2B0 (5)

Again, summing all the equations at (4) we get

2 (2x/2j) = vNX2b0+cAA4 I?0+TV A4 (v— 1) B0
i

=vN\b0+N\ (c+ v— 1) B0

(6)

248

DESIGN AND ANALYSIS OF EXPERIMENTS

Solving the equations at (5) and (6) for b0 and B0 we get

._i) ^2^ (2xi2y)
°~ jy [a4 (c+v—1)—vA22]

l(2Xi2y)-vX2ly

0 A[A4(c+v-l)-vA22]

Now the equations at (4) can also be written as

Ix^y^NX^+ic— 1) N\bn+N\B0

2xz2y=N\b0 -f (c— 1) N\b22+NA4R0

and so on.
Substituting for b0 and B0 in the above equations we get

2x*y A2A4 (c-l)2y-S(2^)(A22-A4)

11 (c-l)JVA4 (c-l)AA4A

where A=A4 (c+v — 1)—vA2*.
In general,

h — 2x**y A2A4 (c —1) 2y-2(2,Xj2y) (A22—A4)

(c-1)WA"4 (c — 1) VA4A

We have thus got the solutions of all the parameters and we denote these

by b0, etc.

One of the purposes of response surface fitting is to estimate the
response at certain points of interest, like the point at which the response
is maximum. After a fit of the surface has been obtained, to get an
estimate of the response at a point what we have to do is to substitute the
point in the surface equation, i.e. the values of the variates x,- as given
for the point and then obtain the estimated value of y. If this estimate

is denoted by y, we have also to find the variance of y. If the point at
which the response is estimated is given by (x10, *20,..., xvo) and the

estimated response at this point is denoted by y0, then

Vo==£o + 6i*io+ . . . +Sn*102+ ... +b12Xl0x20+ . . .

(7.21)

7.7.4 Variance of Estimated Response

For finding .the variance of y0, we have to obtain the variance of and
covariances between the estimated surface parameters. Now from the
theory of least squares it follows that the variance of any parameter

estimate, say, bu, is given by a2 times the coefficient of Zxfy (i.e. the left
hand side expression in the normal equations obtained by differentiating

with respect to bu) in the solution of bu. Similarly, the covariance between
any two estimates, say, cov (bu, bjj) is a2 times the coefficient of lx/y in

the solution of bu or o2 times the coefficients of Ixfy in the solution of

bjj. Here c2 is the error variance.

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

249

Applying this principle we get the expressions for variance and covariances

as follows:

r//2\ A4(c+v—l)<r2 T,/£x a2
F(*»)=s—m-’V{bl)=Ia2

(7.22)

K(ft;)=<r*m4

V(b,t)=a* NXi ~(c_41)jva1a]
_z!_xr^
-1)7VA4X L  (c+v—2)-(v—1)A22 ]
(c

A A

Cov (b0, bn)=—(\<j*/Nk),

2

*">-(£-1)^A

Other covariances are zero.

An inspection of the variance of b0 shows that a necessary condition for
the existence of a second order design is A > 0. This actually leads to
the further condition that

W>v/(c+v-1). (7.23)

The variance of ,v0 is then given by

^(?o)=^A)+(2x/02) F(&+(W) F(ft)+(2*/02*;oa) V($u) •

+2 Cov (ft, hi) 2x,02+2 Cov (ft, ft;) (2*,02.*;o2) (7.24)

Putting 2Xio2—d'2, the above variance can be written as

V(yo)= V(ft)+ V(b.) d2-f (d4—2Zxi02xj02) Vfy+(lxi02xj02) X

V (%,])+2d2 Cov (b0, bu)+2 Cov (ft, bjj) (2xl02Xj02)

=V(b0)+d2 [F(ft)+2 Cov (ft, S«)]+d*F (ft)

+2x,o2xJ0z [F(ft;)-2F (b„)+2 Cov (ft,, ft;)].

(7.25)

Now the coefficient of 2x,o2v;o2 in the above expression is

V (ft;)—2F(ft/)+2 Cov (ft/, ft;)

_ g2 2g2[A4(cR-2)-(v-1)A22-(A22-A4)]

(c— 1) ./VA4A

-wr^mA ^(C+v-2)-(v-dv-v+aj

2a2

a2 2d2
iVA4 (c— 1) ATA4A

[A4(c+v-l)-vA22]

=(a2/N'\t) [1— (2A/(c— 1) A)], since A=A4(c-fv-l)—vA22

=(c—3) cr2/(c—1) JVA4.

250

DESIGN AND ANALYSIS OF EXPERIMENTS

Hence, the variance of y0 becomes

F(Jo)= V(bo)+d2[V&)+2 Cov(S0, b^nd'V(bti)

+(2xlo2Xjo2)[(c-3) o2/(c— 1) JVX4] (7.26)

From the above expression, it is clear that if c can be made equal to 3 by
a suitable choice of the design, the coefficient of 2x/02x/02 vanishes and the
variance becomes a function of d2 only, viz.,

V(yoy~=V(bo)+d* [V(pi)+2 Cov (%„%,)]+&) (7.27)

7.7.5 Rotatable Designs

A second degree response surface design will be calleda second order rotatable
design if in this design c=3 and all the other conditions enumerated earlier
hold. Formally a second order rotatable design can be defined as below.
A design is said to be a second order rotatable design if a second degree

surface of the form

y=b0+b1x1+b2x2+... +iHx<a+... +bijXiXj+...

of the response as obtained from the design points on the variates
*;(/=l, 2, ..., v) with some suitable origin and scale can be so fitted that
the variance of the estimate of the response from any treatment combina¬
tion is a function of the sums of squares of the levels of the factors in that
treatment combination (see Box and Hunter, 1957).

7.7.6 Analysis of Variance

After the surface has been fitted, it is necessary to obtain the analysis of
variance so as to test how good is the fit as also to obtain an estimate of
the error variance. The appropriate analysis of variance partitioning is
shown in Table 7.15.

TABLE 7.15

Analysis of Variance Table

Sources

d.f.

s.s.

Due to regression

coefficients

2,+^ i | b02y+2bi(lx{y)+2bii

J

(Z*<2jO+ 2 %ti($xixty)

1
1 —C.F. ^

Deviation from regression
or lack of fit

V'—2v—v. —1 (
c2

'Obtained by subtraction normally,
j TV'=Number of district treatment
[combinations.

Error

N—N'

Obtained independently adopting
methods according to the actual
design.

-1-

Total

N— 1

C.F.

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

251

7.7.7 Uses

One of the uses of the surface is to obtain the optimum dose combination
at which the response is either maximum or economically optimum. Spch
combinations are obtained by partially differentiating the surface relation
with respect to the x,'s and then equating such differentials to zero. There
will be v such equations, solving which the combination is obtained. For
obtaining the economical optimum dose combination the partial differentials
are equated to the price ratios px,/py where px, is the price per unit of the
jth input variate. In addition there are some other uses of the surface.
For example, with the help of such relations it is possible to investigate the
nature of the surface in specific ranges of the input variates x/s.

7.7.8 Construction

A full factorial of the series 3" or a suitable fraction of the same, in which
no interaction with less than 5 factors is confounded, will always provide a
second order response surface design when the origin is shifted to the
middle of the range of each factor and then a suitable scale change is
made. These designs are not rotatable but will have a value of 1.5 for c.

Construction of Second Order Rotatable Designs
There are several methods of construction of such designs. Several of
these methods have been described below.

Method I
Let there be v factors. Each of these factors is taken at a certain number
of levels. Some of these levels are denoted by one or more unknowns like
a, b, etc. Thus, we shall have treatment combinations like aao.. .b. We
shall not take all such combinations but several of them as the situation
demands. Next, another design 2V is taken. In this design each of the
factors is taken at levels +1 and —1.

Each of combinations of the unknown levels, a, b, o, etc. which have
been taken for constructing the design is then associated with each of the
combinations of the 2V design. The rule of association is that the corres¬
ponding entries in the two combinations, viz., one involving the unknowns
and the other coming from the 2V factorial are multiplied and the products
are written in the same order. This last combination obtained from the
products is a design point. Thus out of each combination involving the
unknowns without sign we shall get design points after association. For
example, if we have the combination aab involving the unknowns a and b,
we have first to take a 2s factorial written by the levels +1 and — 1 for
each factor. This factorial is

252

DESIGN AND ANALYSIS OF EXPERIMENTS

-1

-1

-1

-1

1

1

1

1

-1

-1

1

1

—1

-1

1

1

-1

1

-1

1

-1

1

-1

1

Now by associating the combination aab with each of the above combina¬
tions of the 23 factorial we get

—a

—a

—a

—a

a

a

a

a

—a

—a

a

a

—a

—a

a

a

-b

b

-b

b

-b

b

-b

b

These eight combinations are the design points.

If we take the combination oab instead of aab, we find that by the above

method of association we get the design points

0

0

0

0

0

0

o

0

—a

—a

a

a

—a

— a

a

a

-b

b

-b

b

-b

b

-b

b

It is seen that these eight points are not distinct but the last four are
repetitions of the first four. This has happened because by associating
+ 1 or —1 to zero we do not get different levels. Thus to get distinct
design points which is normally required, we have to associate a

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

253

combination of the unknowns with the 2P factorial in place of the 2V factorial
where p is the number of non-zero unknowns in the combination taken.
Thus with the combination oab we have to associate a 2a and not a 2s
factorial. /

This way of obtaining design points by associating with a 2p factorial
ensures that the sum of products of powers of xt's in which at least one Xi
is at an odd power, is zero. But this does not ensure that the other
conditions are satisfied.

A further criterion for choosing p in the 2p factorial when p is greater
than 4, is that for satisfying the above condition, we may also take a
fraction of 2p for which the defining contrasts must not involve any
interaction with less than five factors as no sum of products of the x/s is
of more than the fourth degree. Now for satisfying the other conditions
like 2*/2=jVA2 or 2xf=3or 2x,-2x/=we have to take some more
combinations of the unknowns* in such a manner that each factor gets a
chance to have the same set of levels.

For example, when we take the combination oab all the three factors
are at different levels. In order to ensure that each factor occurs at the
same set of levels we have to choose the following combinations, obtained
by cyclically changing the above levels of the three factors:

o

a

b

a

b

0

b

o

a

Next, by associating each of the above combinations with the 22 factorial
we get the following design points:

0

0

o

0

a

—a

—a

a

b

b

-b

-b

a

a

—a

—a

b

-b

b

-b

0

0

0

o

b

-b

b

-b

o

0

0

0

a

—a

a

—a

254

DESIGN AND ANALYSIS OF EXPERIMENT

It is easily seen that the above points satisfy each of the conditions
2Xf*=»constant, 2;q4=constant and 2x/2x/*=constant. For the above¬
combinations we find

2x,2=4(a2+b2), 2x,4=4(a4+Z>4) and 2x,2*;2=4a2 b\

In order to satisfy the condition that 2 */4=32 x? xj2 we require that

b2
or x2—3x+l=0 where x=-9.
a2

4 (u4-fZ>4)=3x4a262

This condition thus gives an equation involving two unknowns and one
of the unknowns can therefore be chosen so as to satisfy the above relation.
The other unknown can be fixed arbitrarily.

It will be seen that the condition Xj\2 > v/(v+2) which follows from
VV > v/(v+c—1) for the general response surface designs, is not
satisfied in the above design. As a matter of fact if all the points in a
design are equidistant from the origin as in this design, then the above
condition is not satisfied. As a remedy, a central point of the form (0, 0, 0)
is taken and the above condition then holds. Addition of such central
points does not disturb any other requirement.

Thus, by taking say “a” as 1 arbitrarily, then obtaining b from the
above equation and finally taking a central point we get a second order
rotatable design in 13 points with each factor occurring at the five levels

-1.62, -1, 0, 1, 1.62

In order to transform the above levels to actual levels first the range
of the levels of each factor is fixed. Let such ranges for a factor be R„
and Rm. Thus —b corresponds to the minimum Z?0and b corresponds to
Rm. As the coded doses are linear transforms of the real doses, we
assume that the coded dose, say, y is connected with the real dose, say x,
through the relation y=a+(3x. Now two points on the line, viz. (R0, —b)
and (Rm, b) are known. Hence substituting these two points in the
equation a and p can be obtained. Once the relation j=a+px is thus
established the other real doses corresponding to —a,o and a can easily
be obtained from it.

Method II: Central Composite Designs
The central composite designs are obtained by taking the following
combinations of the unknowns

a, a, a,..., a

b, o, o,..., o

o, b, o,..., o

o, o, b,..., o

o, o, o,..., b

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

255

Next a suitable fraction of the 2r factorials is associated with the first
combination. From each of the other v combinations like (b o.. .6), we
get the combinations, viz., (b o o.. .6) and (—b o.. .o). When v=4 we
have also to take a cental point. The values of a and b can be obtained
by using the condition

2Xi4 = 32x<2X;2

and fixing one of them arbitrarily.

For example, when v=5, we have the combinations

(a a a a a)

(b o o o o)

o b o o o

o o b o o

o o o b o

o o o o b

We shall associate a (1/2) (2s) fraction with the first combination. The
\ fraction is obtained by confounding the 5-factor interaction in 2s. This
design will have thus 16+10=26 design points.

Then 2x,4=16a4+2 b*

and 2x;txi2=16a4
Hence we have the equation

16o4+2Z>4=3 x 16a4

giving bl—l6a*

i.e. b=2a

Taking, a=l, we get 6=2 and hence the five levels are —2, —1, 0, 1 and 2.

Method III
Use of balanced incomplete block designs for construction of second order
rotatable designs (Das and Narasimhan, 1962).

First the incidence matrix of a balanced incomplete block design is
taken. The element 1 in it is replaced by an unknown a. From the rows
of this matrix involving 0 and the unknown a, we shall get b combinations.
Each of these combinations is then associated with 2* factorial or a suitable
fraction, say 2*, of it. We shall thus get 2 x,4=r 2* a4 (taking k=p when
a fractional factorial is used) and 2x,2x/=A 2* a4. It is now required

that

2 X/4=32 x,2 x;2. That is, r 2r a*=3A 2* a4 or r=3A.

It may happen that such a BIB design actuaUy exists. In that case
no further combinations need be taken excepting a central point, which is
necessary as all such points are at a distance equal to ka2 from the origin.

256

DESIGN AND ANALYSIS OF EXPERIMENTS

For example in the BIB design v=7, b—7, r=k=3, A=l, r=»3A.
Hence, from the incidence matrix of this design we can get the

following design. The incidence matrix is given by

1

0

0

0

1

0

1

1

1

0

0

0

1

0

0

1

1

0

0

0

1

1

0

1

1

0

0

0

0

1

0

1

1

0

0

<f

0

1

0

1

1

0

0

0

0

1

0

1

1

Replacing 1 by a we get the following seven  combinations of the unknown
level a\

a

a

0

0

a

a

0

0

a

0

0

0

0

a

0

a

0

0

0

a

From the first combination  we  get the  following  points by associating
with a 23 factorial:

a

a

a

a

0

a

0  —a

a  —a

0

a

a  — a

0  —a

—a

—a

a

a

0

a

0  —a

—a  - a

0

a

— a  — a

0  —a

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

Associating the 23 factorial with the other combinations as well, we shall
get in all 56 design points. These points along with the central point
(0 0 0 0 0 0 0 0) give a second order rotatable design in 57 points with
each facior at three levels —a, 0, a. In this design, we have:

2 Xi*=24a*

lxi2xj2=8a*

Hence the condition 2 xf=yixt2 x? is automatically satisfied. The
unknown “a” can now be fixed arbitrarily.

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

257

If however, the relation r=3A does not hold in a BIB design, we have

to take further combinations of another unknown 6 as below.

If r < 3X, we have to take the combinations

b 0 0 ... 0

0 b 0 ... 0

0 0 b ... 0

0 0 0 ... b

For example in the design v=6=3, r—k=2, A=l, we have r < 3A.

The incidence matrix of this design is given by

1 1 0

0 1 1

1 0 1

Hence unknown combinations are

a a 0

0 a a

a 0 a

These combinations with the further three combinations

6 0 0

0 6 0

0 0 6

will give a design in three factors with 18 points.

The values of the unknowns have to be fixed in this case by using the

relation 2 *i4=32 xf xf.

If again r > 3X, the combination (6, 6,..., 6) has to be taken along
with the combinations obtained from the incidence matrix of the BIB
design.

For example, in the design v=5, 6=10, r=4, k=2, X=1 we have

r > 3X.

Hence along with the 10 combinations obtained from the BIB design,

we have to take the further combination

(6 6 6 6 6)

From the last combination we shall get 16 design points as we have

to use a half fraction of 25 for association.

258

DESIGN AND ANALYSIS OF EXPERIMENTS

The total number of points in this design will thus be

(4 x 10)+16 = 56

Here, again the restriction 2 x,-4=32 x? xf has to be used for determining

one of the unknown levels.

When we have obtained a design in v factors by any of the above
methods, we can always obtain a design in v—s factors by omitting any
s columns of the design matrix.

In addition to the above methods there are several other convenient
methods for the construction of such designs. For details the reader is
referred to the references mentioned at the end of this chapter.

EXERCISES

1. At Technical Development Establishment Laboratories, Kanpur, an experiment
was conducted during 1964 to estimate the potency of flaxedil. Two groups of
eight rabbits were taken and allotted at random to the two preparations. One
[Lg per c.c. solution was injected at the rate of .4 c.c. per minute. Injection was
stopped as soon as there was a head drop and the corresponding dose was
observed for each rabbit. Figures given below are the head drop doses.

Standard
preparation

Test
preparation

1.
2.

3.

4.

5.

6.

7.

8.

840

350

420

400

540

600

560

550

(yg)
580

500

570

700

800

600

550

470

Estimate the potency of the test preparation of flaxedil relative to the standard
one together with its fiducial limits assuming that (1) tolerance is normally
distributed and (2) log-tolerance is normally distributed.

2. For the investigation of linearizing transformation of dose and response of the
stimulus “Gonadothorpic hormone” an experiment was conducted at the Central
Drug Laboratory, Calcutta during the year 1956-57. Immature rats of 30-40
grams weight were taken and injected with hormone doses of some specified
dilution for five consecutive days. The rats were killed on the sixth day and the
organs (uterus) were weighed. Four doses of a standard hormone preparation
were each tried on a batch of six rats, and the weights of uterus, so observed,
are given below:

Doses (iv)

Weight of uterus  (gm.)

2.5

5.0

7.5

12.5

18,  12,  13,
15,  14,  20
34,  40,  42,  50,  38,  28
35,  40,  39,  42,  45,  47
56,  50,  44,  40,  41,  50

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

259

Find metametric transformations for dose and response so that the relations
between the metameters is linear.

3. A 4-point parallel line assay on pituitary extracts in uterus of rats was conducted
at the Central Drug Laboratory, Calcutta in the year 1972. The effect studied
was the contraction of a horn of rats uterus. A horn of uterus of a rat was
suspended in a bath containing a solution of the following composition: (Nad,
9.0 gm/L, KC1, 0.42 gm/L, CaCl2, 0.12 gm/L, NaHC03, 0.5 gm/L, Dextrose,
0.25 gm/L, MgCl2, 0.0025 gm/L and water 1000 ml.). The bath was maintained
at a temperature of 32°C. A dose was then added to the bath and the maximum
contraction of the uterus was measured on a kymograph. For the other doses
also, the same horn was used after washing and giving rest. Each dose was
tested four times. The effect of each dose expressed as the height of contraction
of uterus in m.m. are given below:

Responses in m.m.

(0.01 of standard)

33.0

35.0

35.0

34.0

S2 (0.02 of standard)

46.0

43.0

44.0

44.0

Ti (0.01 of test)

Tg (0.02 of test)

36.0

37.0

36.0

35.0

46.0

44.0

45.0

46.0

Assuming that the response is linearly related to log dose, estimate the potency
of the test preparation with its fiducial limits after applying necessary validity
tests.
An experiment on rats was conducted at the Central Drugs Laboratory, Calcutta
during 1963 in assaying the potency of corticotrophi (ACTH). Fortyeight rats
nearly of the same age and weight were taken and made into six equal groups
at random. Morphine sulphate or hydrocortisone was first injected to the rats
and after an interval of two to three hours the Requisite dose of the drug was
injected. After a certain specified interval the adrenal glands of the rats were
taken out and ascorbic acid contents was estimated. The observations in regard
to ascorbic acid were expressedas mg/100 gram of the adrenal gland and are as
given below:

Standard dose Test dose

Si

s2

s3

Ti

T%

t3

. 25 mu.

.50 mu.

1.0 mu.

.25 mu.

.50 mu.

1 .Omu.

298.7

280.5

279.2

240.5

362.1

304.0

233.8

304.6

259.7

250.1

193.5

259.2

256.7

228.1

272.2

284.1

230.4

228.1

199.1

216.9

201.8

238.8

225.1

189.8

274.5

252.5

245.5

206.1

325.7

339.4

210.4

247.0

176.7

231.2

252.5

219.2

218.2

222.1

189.6

210.0

212.6

209.7

223.6

171.4

189 3

172.9

168.0

190.7

Estimate the potency of the test preparation with its fiducial limits after applying
the necessary validity test.

260

DESIGN AND ANALYSIS OF EXPERIMENTS

5. For estimating the riboflavin content of malt the following common zero 5-points
slope-ratio assay was designed. At each dose four tubes for the riboflavin content
of malt were tested. The dosages tried were:
(i) Control or blanks
(ii) 0.10 gg and 0.20 [xg of riboflavin as two doses of standard preparations

(denoted by Xs) and

(iii) 0.025 fig and 0.050 [xg of malt as two doses of test preparation (denoted

by XT).

The response measured as titers in milliliters0. IN (NaOH) are given below:

Control

Standard preparation

Test preparation

*5-0
*,=0

1.90

2.25

2 00

2.20

.lOgg *,=0.20 (xg

*,=o

*,=0

 o

I
I

4.85

5.00

5.25

4.90

*

 o

I
I

*,=0.025 fxg *,=0.050 txg

8.35

8.20

7.95

7.80

4.00

4.40

4.50

4.10

6.05

6.20

6.10

6.10

Assuming that the relationship between dosage and response is linear, estimate
the riboflavin content of malt through the estimation of its relative pontency
after applying the necessary validity tests. Find the fiducial limits of the estimate.

6. Consider the problem of estimating the parameters in the equation

y = Po + Pl*i+ $2X2 + Pl2-*l*2 + [}llxl2 + P22*22 + Pll2*l2-*2»

using a design that would have the fewest number of observations and the standard
errors of estimates as nearly equal as possible.
Set up the design (may be non-orthogonal) specifying the location of each experi¬
mental unit relative to coordinates (0, 0) of (at-,, x2).

7. Fit a second order response surface in three variables to the following data and
compute the stationary point of the response system. The levels of the variables
are coded.

*i

—1
1
—1
1
—1

1
—1

1
•—2
2

0

0

0
0
0

*2

—1
—1
1
1
—1
—1
1

1
0

0
—2
2
0
0
0

*3

—1
—1
—1
—1
1
1
1

1
0
0
0
0
—2
2
0

y

50
46
29
47
49
52
51
36
45
52

49
55
37

42
44

DESIGNS FOR BIO-ASSAYS AND RESPONSE SURFACES

261

8. The following are the design matrix and vector of responses of a 22 factorial

design used to fit a planar response function.
(a) Estimate the first order response function and plot lines of constant response

in the (xj, x2) plane.

(b) Provide an analysis of variance table showing significance tests on each

coefficient:

*1

-1

—1

1

1

—1

—1

1

1

0

0

0

0

A'2

-1

-1

—1

—1

1

1

1

1

0

0

0

y= r 54.7

50.3

59.7

60.3

63.7

64.0

67.5

69.2

61.5

62.3

62.0

0 _

61.9 _

9. A simplex design in two variables is used to measure the effect of the variables
on a single response. The following represent the design matrix and the vector
of observations.

“ x2 y

1.0

0.5

-0.5

—1.0

-0.5

0.5

0

0

0

0

96.5

0.88

79.7

0.88

76.4

0

55.4

-0.88

63.2

-0.88

78.9

0

0

0

98.6

94-6

94.4 _

(a) Estimate the response function and determine the stationary point.
(b) Plot contour of constant response in two dimensions.
(c) Perform an analysis of variance including the sources of variation due to:

linear terms, quadratic terms and lack-of-fit.

REFERENCES

1. Anderson, V.L. and Mclean R.A. (1974). Design of Experiments, A Realistic

Approach, Marcel Dekker, Inc., New York.

262 DESIGN AND ANALYSIS OF EXPERIMENTS

2. Buss, C.I. (1952). The Statistics of Bio-Assay with Special Reference to Vitamins
(reprinted with addition from vitamin methods) Vol. II, Academic Press,

New York.

3. Box, G.F. and Hunter, J.S. (1957). “Multifactor experimental design for

exploring response surfaces”, Ann. Math. Stat. 28, 195-241.

4. Das, M.N. (1957). “Bio-assays with non-orthogonal data”. Jour. Inc. Soc.

Agri. Stat., 9, 67-81.

5. Das, M.N. (1958). “Reinforced incomplete block designs”. Jour. Ind. Soc.

Agri. Stat., 10, 73-77.

6. Das M.N. (1958). “Circular designs”. Jour. Ind. Soc. Agri. Stat., 12, 45-56.
7. Das, M.N. (1964). “A somewhat alternative approach for construction of sym¬
metrical designs and obtaining maximum number of factors”. Cal. Stat.
Assoc. Bull. 13.

8. Das, M.N. and Kulkarni, G.A. (1966). “Incomplete block designs for bio-

assays”. Biometrics, 22, 706-29.

9. Das, M.N. and Mehta, J.S. (1968). “Asymmetric rotatable designs and ortho¬

gonal transformations”. Technometrics, 10, 313-22.

10. Das, M.N. and Narasimhan, V.L. (1962). “Construction of rotatable designs

through B.I.B. designs”. Ann. Math. Stat., 33, 1421-39.

11. Das, M.N. and Nigam, A.K. (1966). “On a method of construction of rotatable
designs with smaller number of points controlling the number of levels”. Cal.
Stat. Ass. Bull., 15, 147-57.

12. Draper, N.R. (1960a). “Second order rotatable designs in four or more

dimensions”. Ann. Math. Stat., 31, 23-33.

13. Draper, N.R. (1960b). “Third order rotatable designs in three dimensions”.

Ann. Math. Stat., 31, 865-74.

14. Draper, N.R. (1960c). “A third order rotatable design in four dimensions”.

Ann. Math. Stat. 31, 875-77.

15. Draper, N.R. (1961). “Missing values in response surface designs”. Techno¬

metrics, 3, 389-98.

16. Finney, D.J. (1964). Statistical Methods in Biological Assays, 2nd ed., Griffin,

London.

17. Fisher, R.A. and Yates, F. (1963). Statistical Tables for Biological, Agricultural

and Medical Research, 6th ed., Oliver and Boyd, Edinburgh.

18. Gardiner, D.A., Grandage, A.H.E. and Hader, RJ. (1959). “Third order
rotatable designs for exploring response surface”. Ann. Math, Stat., 30,
1082-96.

19. Herzberg, A.M. (1966). “Cylindrically rotatable designs”. Ann. Math. Stat.,

37, 242-74.

20. Herzberg, A.M. (1967). “Cylindrically rotatable designs of types 1, 2 and 3”.

Ann. Math. Stat., 38, 167-76.

21. John, P. W.M. (1971). Statistical Design and Analysis of Experiments, Macmillan,

New York.

22. Myers, R.H. (1971). Response Surface Methodology, Allyn and Bacon, Inc.,

Boston.

23. Plackett, R.L. and Burman, J.P. (1946). “The designs of optimum multi-

factorial experiments”. Biometrika, 33, 305-25.

24. Raghavarao, D. (1963). “Construction of second order rotatable designs

through incomplete block designs”. J. Ind. Stat. Ns\s., 1, 221-25.

25. Tocher, K.D. (1952). “The design and analysis of block experiments”. Jour.

Roy. Stat. Soc., 13, 14, 45-100.

26. Tyagi, B.N. (1964). “On construction of second and third order rotatable
designs through pair-wise balanced and doubly balanced designs”. Cal. Stat.
zDj. Bull., 13, 150-62.

CHAPTER 8

Analysis of Covariance and
Transformation

8.1 Analysis of Covariance

We have seen that the devices of local control, confounding and increase
in the number of replications are adopted to increase the precision of the
estimates of treatment contrasts. Analysis of covariance is another device
with the same objective. This technique can be applied when observations
on one or more correlated variables are available from each of the experi¬
mental units in a design, along with the observations on the variate under
study. These additional variates are called ancillary or concomitant
variates. It is necessary that these variates are associated with the variate
under study.

The rationale behind the technique is as follows. Let x denote an
ancillary variate and y, the variate under study. When y and x are
associated, a part of the variance of y is due to the variation in x oyer the
experimental units. So, had the variate x been constant over the units,
there would have been a corresponding reduction in the variance of y.
The purpose of analysis of covariance is to effect such reduction in the
estimate of the variance of y by analytical means when the observations
on the x-variate are available along with the observations on the y-variate.
Basically, what is done is, to estimate the relationship between x and y,
taking x as the independent variate, after eliminating the effects of blocks
and treatments and then obtain the values of y as expected from this
relation corresponding to each of the values of x. These expected values
of y are then analyzed to get the error variance of y.

For the purpose of the present chapter we shall assume that the relation

between x and y is linear and the values of x are not subject to error.

For the application of this technique it is necessary that the x-variate
is not affected by the experimental treatments, otherwise a part of the
treatment effect gets eliminated along with the elimination of the effect of
the x-variate.

This technique will be discussed in Section 8.2 with the help of an

appropriate model.

8.2 Analysis of Covariance for Randomized Block Designs

An appropriate model for this analysis for a two-way classified data of k

264

DESIGN AND ANALYSIS OF EXPERIMENTS

treatments collected from r blocks of a randomized block design is

Yu=y. -+ ti+bj+bxu+eij,
where Yu is the observation (random) variable i—l,..k, 7=1,. •• » r;
corresponding to the observation yu from the ith treatment intheyth block,
jx, t, and bj are the fixed effects of the general mean, ith treatment andyth
block respectively; xu is the observation on the ancillary variate corres¬
ponding to yu, b is the regression coefficient of y on x; e,-/s are the error
components which are assumed to be normally and independently distributed
with zero mean and a constant variance a2.

Let lyu=Ti, 2 yu=Bj,

j >
2 Xu=Thx), YXij—Bju:),
) I
2 Ti=G and 2 T,(X)=GX.
i I

By applying the technique of least squares as discussed in Chapters 1 and 2
the estimates of the fixed effects along with the regression coefficient are as
shown below:

bGx
- ny‘J bvXti __G~b
\—i>
rk

rk

7_ Tj—bTux)
ti— r>

T _Bj-bBj^x) ~
b,=—^

S xuyij
ij

v \Ti(X) v BjB](X)

f/—2 —-2-p--  GGx
rk

T2

Hx)

2 xJj — 2
u •' i r

~B*n m ,Gi
rk

(8.1)

Exy
eTx

say.

The error sum of squares adjusted for the variation of x is obtained by

substituting the above estimates in

and is given by

2 (yu —bj - bxu)2
ij

E=2(yu-y.-

u

-ti—bj—bxij)2

(8.2)

rr2 n2 /^»2
Y-H+Tk-~bE- 'xy-
The degrees of
freedom of the adjusted error sum of squares is
(r-1) (k-1)-1.
This has been reduced by one degree of freedom from
that in the randomized block design because the estimation of error variance
here, is subject to one more restriction imposed for estimating b.

i

For obtaining the adjusted treatment sum of squares we make the
hypothesis that all the treatment effects are zero. The error sum of squares
for this hypothetical model comes out as below:

ANALYSIS.OF COVARIANCE AND TRANSFORMATION

265

Adjusted error sum of squares on the hypothesis

yn .v

E^yu'—^—b'E'xy

i) k

^here E’xy^2 xu y,j-2

& XX ij i K

and 4=2V‘2%.‘

y A:

The adjusted treatment sum of squares is now Ex—E with k—l degrees of
freedom.

The various calculations needed for the covariance analysis are shown in

the following tables.

In Table 8.2 Txx, Txy and Tyy stand for the sum of squares for x, sum of
products of x and y and sum of squares for y, respectively, in the “treatment
line” of Table 8.1.

From Table 8.2 the mean square for the adjusted treatment and error
sums of squares are obtained. The hypothesis of equal treatment effects
is tested by F-test where F is the ratio of these two mean squares.

The estimates and the variance of different treatment contrasts are

obtained as below.

for i=l,..., k.

=yt—y—b(xi—x), (say)

Estimate of any contrast 2 Ut{ is then given by

i

2 lit,=2 li{yi~bXi)

(8.4)

r - 2 (2/,*,)>
F(2/,r,)=o* 2 —

i L / r

]

because V(b)=p-.

_ (j*

In particular,

(8.5)

and <j2 is estimated by the error mean square obtainable from Table 8.2 as

Em=

E
(r—1)(*— i)-r

(8.6)

_ It is seen that the variance of the estimate of the difference between any
pair of treatments is not constant, as we get in analysis of variance of this
design. Sometimes to make the critical difference (C.D.) a constant for
each pair of treatments, (xt—xm)2 in the above variance of if
replaced by T^/fJc— 1), the treatment mean square for the x-variate.

266

DESIGN AND ANALYSIS OF EXPERIMENTS

ANALYSIS OF COVARIANCE AND TRANSFORMATION

267

8.3 Analysis of Covariance of Completely Randomized and

Latin Square Designs

For both these designs the technique is exactly the same as the one
developed for the randomized block designs. The procedure indicated
for randomized block design holds, as a matter of fact, for any design
once the treatment and the error sum of squares for the x-variate, the
sums of products for the two variates and the sum of squares of the
j-variate are obtained according to the appropriate analysis of variance
of the design. For these two designs or rather for any orthogonal design
the following table (8.3) is first prepared. Only the treatment and error
sums of squares have been shown in the table, as these alone are needed.

Estimate of treatment effects

U=yt—y -b (xt—x)

— f /i2 ^

(8.7)

8.4 Analysis of Covariance of Non-Orthogonal Data in

Two-Way Classification

When the data are non-orthogonal, the technique of covariance can be
developed just like the analysis of variance of non-orthogonal data discussed
in Chapter 1. The readers are referred to Das (1953, 1956) for further
details about this method.

First the data of the x-character and the ^-character are analyzed
separately according to the method of. analysis of variance of non-
orthogonal two-way data. For the covariance portion, the unadjusted
sum of products are obtained by the ordinary method as discussed in
randomized block design and is also shown in Table 8.4. The adjusted
sum of products is obtained from 2 tiQt(x) where ti is the estimate of the

t

/th, treatment and Qi(x) is the adjusted total of the corresponding treatment
obtained from the x-variate. Further details are given in Table 8.4.

The data and notations,are assumed to be the same as in analysis of
variance of non-orthogonal data presented in Chapter 1. The two factors
of classification have been called blocks and treatments. The totals
Tt(x), etc., correspond to Bj, Tt, etc., excepting that the former are

obtained from the x-variate and the latter from the ^-variate.

268

DESIGN AND ANALYSIS OF EXPERIMENTS

ea e

u
O
.0 w z
« 2

C/5

E

-d

■4*
>1

s
»3

l

1
ts

5S

,bq
>-Cj
|
»s
h!T
II
ha

hI *
halha
II
I-CJ

y
y
E

4

X

^3

ha
1
hT

£

»>

8

s?

/—S
*—«•

1

'w'

(N

-*
f
“a

>»
X

ii»
1

ss
ha
II
—4
ha

x
X  X

1

>>

U4

X

X
X
ha
U
X

*3
+

a

t
+

CO
■*-*

c |

u

O

3 O

1/3

1 1
to 1
E ^ +
tS o S
u u E
H W W

© U. tH

ANALYSIS OF COVARIANCE AND TRANSFORMATION

269

4
.
8

E
L
B
A
T

270

DESIGN AND ANALYSIS OF EXPERIMENTS

TABLE 8.5

Adjusted Sums of Squares

Sources of variation

SxX

Sxy

Syy

b

Actfusted s.s.

d.f.

Treatment

Txx

Txy

Tyy

Ei-E

m. -1

Error

Exx

EXy

Eyy

Treatment+error

E’xx

E’xy

E’yy

- Exy
Os=s'Er~
JZxx

r, E'*>
b ~ E’xx

E=Eyy—~bExy n..' -m.—n.j

E1=E'yy-b'E'xy n.

The estimate of any treatment contrast 2//f/ is given by

2lii,='Zl,(iKy)-btt{x)) (8.8)
i i

where t{(,) and *«*) denote the estimates of the ith treatment effect
obtained by using respectively the y and x variates. The variance of
2 U U can be obtained by the method indicated earlier in connection with

the analysis of variance of non-orthogonal data in Chapter 1.

Actually

f (2 htj(x))2)

hh)=°21,q,+ 1 Ex—\ (8.9)

where the qfs are obtained as indicated in Chapter 1.

8 4.1 Analysis of Covariance of Non-Orthogonal Designs

The analysis of covariance of non-orthogonal designs follows directly
from the above results of analysis of non-orthogonal data. The main new
thing in the covariance analysis of non-orthogonal data is the finding of
the adjusted treatment sum of products from 2 ttQnX) or 2/,(je)Q/. The

rest of the procedure is straight-forward as in randomized block designs.
Further once the variance covariance table is obtained from an analysis
appropriate for the design, the rest of the procedure is the same as for
orthogonal or non-orthogonal data.

For example, the variance covariance table for the analysis of any

incomplete block design is as given below.

ANALYSIS OF COVARIANCB AND TRANSFORMATION

271

S
J
Q
«

15.

S o o
J9

6
.
8

E
L
B
A
T

%
w=s

X
W=>

X
M

£
II
c?
i C*
w-

CD
* >—

w-
B
3
<5
I'i*
W'

«!
I!
H V—'
<5
v—'
ic:
W

W*

eg
3
eg

w-

eg

w->

I
-o

I

«s
'w'
1
■*-*
§

2
m

el
v-/
|
+-*
§
-O d
>»
«

C/5

J

d
.2 o
a
2
3
Cfi

M

+
I
o
I

d 4>
e
c3
<u

o
o
5

o
fi
w

O
H

H
CO

a
.o

!
o

§
s
o
CO

272

DESIGN AND ANALYSIS OF EXPERIMENTS

8.5 Analysis of Covariance with Two Ancillary Variates

If ancillary data are available from each experimental plot for more than
one ancillary variate and each of them is linearly related to the variate y
under study, then the covariance technique can be extended to eliminate
the portion of variation in y which is due to the ancillary variables. We
shall discuss here the case of two ancillary variables denoted by x and z.
The data from a randomized block design with k treatments and r repli¬
cations have been analyzed. This technique can be modified to suit other
designs exactly as in one ancillary variate.

We take the following model:

Ytj={*+tt-f-b)+PiX/;++eu

where (jl, tt, bj and etj have the same meaning as in the model for one
ancillary variate, xtj, ztj are the observations corresponding to ytj from the
x and z ancillary variates respectively; and p2 are the partial regression
coefficients of y on x and z respectively.

Let

2 yu—G, 2 Xij=Gx, 2 zi)=Gz
U U U

2 yu—Bj, 2 xij=Bj(X), 2 zi)=Bj(z)
1 I i

2 yu—Ti, 2 xtj = Tl{X), 2 zlj=Tiiz).

Let further the corrected sums of squares and products for x, z and y

variates be denoted as shown

Block s.s. (x) =BXX

Treatment s.s. (x) =TXX

Error s.s. (x) =EXX

Block s.s. (z) =Bzz

Treatment s.s. (z) —Tzz

Block s.s. (y) =Byy

Treatment s.s. (y) —Tyy

Block s.p. (xz)=Bxz

Treatment s.p. (xz)—Txz

Block s.p. (xy)—Bxy

Treatment s.p. (xy)=Txy

Block s.p. (zy)=Bzy

Treatment s.p. (zy)=Txy

Error s.s. (z) =Etz

Error s.s. (y) —Eyy

Error s.p. (xz)=Exz

Error s.p. (xy)=Exy

Error s.p. (zy)=Ezy

By the method of least squares the estimates of the fixed constants and

the regression coefficients are given by

, — G — Gx , — Gg

where , =^. * and

{*—y -PiX—(J*z

ANALYSIS OF COVARIANCE AND TRANSFORMATION

273

where yx =—, and (i=l, 2,..., k)

where & and jf8 are obtained by solving the following two equations:

$\Exx “I- $2,Exz — Exy

$lExz 4" Q^Ezz — Ezy.

(8.10)

Now, the adjusted error sum of squares is obtained from

E—Eyy Pi Exy-QyEzy.

This has (r— l)(fc— 1)—2 degrees of freedom.
To get the adjusted treatment sum of square, similar calculations are made
from the model

ytj—+bj+Pi*i_/++eu
under the hypothesis that the treatment effects are zero. Adding the
various error and treatment sums of squares and products we can get
E'xx, E’zx, E'yy, E'Xy, E'zy and E'xz where £'**=£**+Txx and soon for the
others.
Now the error sum of squares for the hypothesis is obtained from

Ey—E'yy-P jE Xy P 2E Zy

with r(k— 1)—2 degrees of freedom where p'x and p'2 are obtained from
the following equations

$\E'xx + $\E,xz=E'xy (8-11)

V^E’xz+ViEzz^E'xz.

The adjusted treatment sum of squares is obtained from Ex—E with k—1
degrees of freedom.

The hypothesis of equal treatment effects can be tested by the F-test
where F is based on the mean squares corresponding to the error and
treatment adjusted sums of squares.
Estimate of U—tm is given by

ti-tm=yx-ym—Pi(x, - xm) - p2(z,—? m)

vor (ti—tm) = ~~ *">)2 v (Pi)+(2/—Zm)2 v (P2)

-j-2 (jf/ —Xm) {Zi Zm) COV (Pi, P2)

where

EzzO2

V®i)-ExxEzz-Exz2 *

V^)=sExxEzz-E^’ C0V (Pl’Pa) EzxEzz-Exz2 •

o2 is estimated by the error mean square E/(r—l)(k—l)—2.

-ExzO2

(8.12)

274

DESIGN AND ANALYSIS OF EXPERIMENTS

8.6 Covariance and Analysis of Experiments with Missing Observations

In Chapter 3 while discussing analysis of experiments with missing observa¬
tions we mentioned that the covariance technique can be conveniently
applied for the analysis of such data. Application of this technique can
avoid the difficulty due to non-orthogonality of data, but at the same time
the solution of a set of simultaneous equations with as many unknowns as
the number of missing observations cannot be avoided.The method has been
discussed below.

Let one observation be missing in any design including the incomplete
block designs. The missing observation is taken as zero. The number of
missing observation per plot in different plots is taken as the ancillary
variate x. The x-variate takes the value unity in the plot of missing
observations and zero elsewhere. We have, now, for each plot an obser¬
vation of the variate under study and a value 1 or 0 of the ancillary variate x.
The technique of analysis of covariance with one ancillary variate can now
be applied for the analysis of the design as discussed earlier. This analysis
gives the correct error and treatment sums of square.

If there are two missing observations, a separate ancillary variate is
defined for each missing observation. Let the plots of the missing obser¬
vations be numbered as plot 1 and plot 2 in any order. Let xx be the
variate defined for plot 1 and xa for plot 2. Then xx takes the value 1 in
plot 1 and zero in all other plots and xa takes the value 1 in plot 2 and
zero in all other plots. If there be more than two missing observations, as
many ancillary variates as the number of missing observations are defined
likewise.

There will be, then, as many partial regression coefficients as the number
of missing observations. To estimate these coefficients it is required to
solve an equal number of simultaneous equations.

For example, let two observations be missing in a randomized block
design with r blocks and k treatments. Let these observations belong to
different blocks and different treatments. For the sake of simplicity and
without any loss of generality, let the first missing plot correspond to the
ancillary variate * which belongs to the block denoted by bmx and to the
treatment, denoted by tmi. Similarly, let the second missing plot corres¬
ponding to the ancillary variate z, belong to the block denoted by and
to the treatment tmt. The sums of squares and products for the error and
treatment lines which are required for writing the equations of the partial
regression coefficients, are shown below:

ANALYSIS OF COVARIANCE AND TRANSFORMATION

275

Treatment

r 1 I
J *X =-r
r rk

T _J 1
** r rk

T   1
X2 rk

rp Tm\ G

Ixy—-r
r rk

rp 7m, G
zv“ r ~7k

Error

Error+Treatment

p 1 1 1 , 1
r k v rk

E _i 1 1.1

p _ (Tm i Bmi
Ex'>—y—+—-  rk)

p _ (Tm% Bmt

rkJ

E’xx= I-p
k

•£»*=0

p, BmL

E

F, _Bmt

** T

Tyy, Eyy and E'yy are obtained as usual for the design. The equation foi
the partial regression coefficients can now be written and solved as indicated
earlier. The rest of the analysis can also be completed likewise.
. Estimate of the difference between two treatments effects, one of which
is affected, is shown below.

U tm—yi ymi Pi(xi xmj) P2(zi—zmi)

=yi-ym+f-1.

v (Ji~Tm)~a2 + _ El
r%(ExxEzz

:~EX/)}

=-124- — (r—0(^—1) )
r 1 ^ (r—1)2 (/t—1)2_ i J*

These are obtained after substituting the values of Exx, etc. as given above.

—Tmi Jm,'f"

Pi-P

v (7m -Tm )=2*+ ™\E**+E"+2Exti
1 1 '* r + r*\ Exx Ezz-E*2 )

(8.13)

(8.14)

r y^rk-r-k)'

8.7 Transformations

We have seen that the main technique for the analysis of the data collected
from various designs is the method of analysis of variance. This method
is applicable to data which satisfy the following assumptions:

276

DESIGN AND ANALYSIS OF EXPERIMENTS

(1) The effects of blocks, treatments and error are additive
(2) The variance of the observations is constant
(3) The observations are distributed independently
(4) The observations have a normal distribution.
There are certain types of data where all these assumptions are not
satisfied. For example, when the data are in the form of percentages of,
say, seeds that germinate in a plot, the number of rare insects present in
soil samples or the number of particular types of impurities ini milk sample,
the assumption that the variance is constant for the different observations
does not hold good. In the first case above the observations have binomial
distribution and hence the variance, which depends on the unknown
percentage, is not a constant. In the other two cases the observations have

a Poisson distribution.

The method of analysis discussed earlier is not, therefore, applicable to

these and other similar cases.

In such cases a non-linear transformation of the observations may
improve matters in the sense that the transformed observations satisfy the
assumptions 1—4, above. In some cases of multiple regression problems
transformation of independent as well as dependent variables might be
desirable to produce the simplest possible regression model in the trans¬
formed variables. It may be mentioned that in regression problems
transformation of the independent variable can be applied without affecting
the constancy of variance and normality of the distributions of the
dependent variables.

In all cases we are primarily concerned in finding a transformation
which will guarantee the assumptions 1—4, above. No transformation
may be expected to work perfectly and it is this fact more than any other
that involves extensive computations to fit a computationally awkward
transformation.

A class of transformations to stabilize the variance where the variance
of a variable is a function of its expected value, can be obtained as follows.

Let X denote a variate such that

v(X)=flm)

where m is the mean of X and f(m) denotes a function of m.

Let X be transformed to a function F(X). It is known that the

approximate variance of F(X) is given by approximately equal)

Putting this variance equal to a constant, say, c2, we get

Jn other words, F(X)= f —~L=z dX.

J Vf(x)

ANALYSIS OF COVARIANCE AND TRANSFORMATION

277

Thus since/(m) is known, the transformation F(T) can be obtained such
that the approximate variance of F(X) is constant.

For example if A" is a binomial random variable with parameters (n, P)

then the transformed variable is given by

cdx

x(l - x)
n

=sin“1 f*
v n

when c is chosen suitably. The asymptotic variance of the transformed

variable is —. Anscombe (1948) proved that a slightly better transforma-

4 n

tion is

F(x)=sm~1

.v-1-3/8
5T+3/4

which has asymptotic variance .

1

Similarly, if X is a Poisson random variable then the transformation
Y=\/X stabilizes the variance. Again, Anscombe (1948) noted that a
slightly better transformation is ^X+3/Sin, the sense that it has approxi¬
mate (asymptotic) variance smaller than that of \/X. Following Bartlett
(1936) we list below some transformations that have been found to have
practical value in the case of random variables whose variance is a function

of its mean value m.

TABLE 8.7

Table of Suitable Transformation of the Random Variable X with Mean m

and with Variance which is a Function/(m)

Variance/(m)

Transformations

Approximate variance

1. A2m2 (A constant)

2. A2m2 (1 —m)2

3. (1 — m2)2/n—1

4. m+A2m2

log* (X), log* (JV+1)
logjo (X), logio (■X'+l)
log e (x)/(l —X)

£loge(l+ *)/(!-*)

A-1 sin /r1 (AVX)

A2

A2

1 In— 3

1/4

Another transformation that proves useful is the tanh-' transformation
of the sample correlation coefficient. It is known that the asymptotic
variance of the sample correlation coefficient r based on a random sa p
of size n from a bivariate population is (1 -Ps)2/" where Pis the population

correlation coefficient.

278

DESIGN AND ANALYSIS OF EXPERIMENTS

It then follows that the transformed variable

F(r)= [ YjlSjL-tanh-» r
' J (1-/*)

choosing c=\/y/n it has a constant asymptotic variance which is equal to

c2= -
2 1
n'

For the purpose of analysis the data are first transformed appropriately
and then the transformed data are analyzed according to the design. For
example, if the data correspond to binomial proportion then these are
transformed by sin-1 \/p. The values of sin-1 y/p for different p have
been tabulated by Fisher and Yates (1948). For this transformation it is

necessary that if />=-, then n should be the same for all the observations,

otherwise the variance does not remain constant.

The inferences in regard to different hypotheses can be drawn from
the analysis of the transformed data. The different averages of the
original data which are needed for a meaningful interpretation are
obtained by the inverse transformation of the averages obtained from the
transformed data.

EXERCISES

1. (One way classification, covariance model). Let Yu, /=],..t, j=l,.. r be

independently normally distributed with mean

E( Yij)=+ 0xt- j

V(Yii) = <5 2

where x,/s are observed fixed quantities, n is a constant, «,• is the ith treatment
etiect, 0 is the regression coefficient.

(i) Find the maximum likelihood estimator 0 of 0, o2 of a2.

(u) Find the distribution of 0, a2 and show that they are statistically independent
(m) Find the confidence interval of a2 w|th confidence coefficient 1-a.
(iv) Test the hypothesis /70; 0—0.
(v) Test the hypothesis H0 : a1==... =«(.

2. If the relation between an ancillary variate x and the study variate y is quad¬
ratic, deduce the computational procedure of the analysis of covariance for
adjusting y for x.

3 . Obtain the computational procedure for the analysis of covariance of a B.I B

design with one missing observation.

4. With a view to making a selection for high yielding hybrid maize, a varietal trial
was conducted in 1966 at the Vivekananda Laboratory in Almora, Uttar Pradesh
The trial was laid out in randomized block design with four replications At the
time of harvest the number of plants harvested for recording the yield were also
noted. The data obtained are given below;

Grain yield (in lb.) and the number of plants (given in parentheses) harvested ner
plot (48'x 12') are given below. y

ANALYSIS OF COVARIANCE AND TRANSFORMATION

279

Varieties Replication 1 Replication 2 Replication 3 Replication 4

1.  U.S.

13  48.25

(227)

2.  N.C.  27  99.50

(248)

3.

Ind.  816A  43.50

(249)

4.  V.L.  21  52.50

5.  V.L.  23  83.31

(264)

(271)

6.  V.L.  36  65.31

(269)

7.  V.L.

6  44.19

(218)

8.

T.

41  39.50

(252)

56.25

(226)

85.50

(218)

48.34

(259)

37.50

(140)

54.50

(234)

78.50

(217)

58.50

(256)

48.50

(270)

43.50

(252)

40.20

(248)

65.25

(263)

61.13

(259)

57.50

(256)

73.00

(261)

66.06

(194)

68.50

(260)

52.88

(239)

36.25

(103)

54.00

(259)

46.69

(214)

35.50

(237)

26.50

(230)

59.50

(226)

37.13

(241)

Analyze the yield data by using information about the number of plants harvested
and draw conclusions. Calculate the gain in efficiency as a result of using addi¬
tional information of the number of plants harvested. Give the standard error
of the difference of the means of varieties N.C. 27 and V.L. 23 after adjusting the
means for the unequal number of plants harvested.

5. Let X be a Poisson variate with mean m. Expanding y/7+b in powers of
(*—I*) — t obtain first a few terms of the mean and variance of y/x+b. Hence
show that the choice of 6=3/8^ makes the asymptotic (for large (jl) variance of
y/x+b smaller than that of ^x.

REFERENCES

♦ _

1. Anscombe, F.J. (1948). “The transformation of Poisson, binomial and negative-

binomial data.” Biometrika, 35, 246-54.

2. Bartlett, M.S. (1937). “Some examples of statistical methods of research in

agriculture and applied biology.” J. Roy. Stat. Soc. Suppl., 4, 137-83.

3. Bartlett, M.S. (1936). “The square root transformation in analysis of variance.”

J. Roy. Stat. Soc. Suppl., 3, 68-78.

4. Bartlett, M.S. (1947). “The use of transformations.” Biometrics, 3, 39-52.
5. Box, G.E.P. and Cox, D.R. (1964). “An analysis of transformations (with

Discussion).” Jour. Royal Stat. Soc., (B), 211-52.

6. Box, G.E.P. and Tiao, G.C. (1972). Bayesian Inference in Statistical Analysis,

Addison-Wesley Publishing Company.

7. Cochran, W.G. (1943). “Analysis of variance for percentages based on unequal

numbers.” Jour. Amer. Stat. Assoc., 38, 287-301.

8. Das, M.N. (1953). “Analysis of covariance in two-way classifications with

disproportionate cell frequencies”. Jour. Ind. Soc. Agri. Stat., 5,161-76.

9. Das, M.N. (1956). “Analysis of covariance of incomplete block designs with or

without missing observations.” Jour. Ind. Soc. Agri. Stat., 8, 76-83.

10. Fisher, R.A. and Yates, M. (1948). Statistical Tables for Biological, Agricultural

and Medical Research, Oliver and Boyd, Edinburg.

11. Rao, C.R. (1965). Linear Statistical Inference and its Application, Wiley, New

York.

CHAPTER 9

Weighing Designs

9.1 Introduction

Yates (1935) showed that if several light objects are weighed in groups
rather than individually as customary and next the weights of the indiyidua
objects are estimated by the method of least squares, then the precision ol
the estimates increases quite considerably. In the scheme suggested y
Yates the objects are always placed on the same pan in a chemica
balance or on a single pan in a spring balance. Hotelling (1944) showe
that Yates’ scheme can be improved by distributing the objects on both
the pans in a chemical balance. In this case the precision of the
estimates of the weight of the objects increases further. Yates illustrated
the technique by providing a scheme for weighing seven objects in eight
weighings and showed that the variance is £ times of that obtainable from
the customary method when correction for the needle deviating from zero
position when the pans are empty, is needed. By modifying the scheme
of Xates s0 as to place each individual weighing the group of objects
as in Yates scheme on one pan and the remaining objects on the other pan
and then balancing by placing suitable weight on one of the pans,
Hotelling showed that the variance of the estimate of the weights of
individual objects becomes half of that obtainable from the Yates scheme
for seven objects. In the scheme of Hotelling eight objects were taken
instead of seven, the extra object being placed always on the same pan
together with the others as indicated earlier.

Following Yates and Hotelling several authors provided methods of
construction and analysis of such designs, together with investigation of
the precision of such designs. Prominent among them are the works of
Banerjee (1948, 1949, 1950), Kempthome (1949), Kishen (1945), Mood
(1946), Raghavarao( 1959, 1960), Dey(1969, 1971) and others.

9.2 Definition

A weighing design can be formally defined as below. Given p objects to
be weighed in groups in N weighings a weighing design consists of N
groupings of the p objects, such that in each grouping the p objects are
made into three sets of sizes n„ «2 and n0 and while weighing, the set of
size n, is placed on one pan, say, the left one, that of size «a on the oth ^

"WEIGHING DESIGNS

281

pan and the third of size nn is omitted from the weighing. There will thus
be one weighing for each of the N groupings.

As indicated earlier there are two types of balances, the chemical
balance and the spring balance. In chemical balance the objects can be
placed either on one pan or on both for each weighing. In spring balance
there is only one pan for placing the objects. If the objects are placed on
•one pan only, say^ the right one in a chemical balance, then n2~0 and
n0=p—n1. If the objects are distributed on the two pans, then n0=0 and
n1=p—n2. In Spring balance n2 is always zero and n0=p—n1. When the
objects are placed on one pan only in a chemical balance, we shall call
the weighings one pan weighing and the design one pan design. If,
again, the objects are distributed over both the pans, we shall call the
corresponding designs two pan designs. Evidently, the spring balance
designs are one pan designs just like the chemical balance design when
the objects are placed on one pan only. Instead of classifying the
weighing design as chemical balance and spring balance designs we shall
classify them as one pan and two pan designs.

As the weights of individual objects have to be estimated by the
method of least squares, the groupings involved in a weighing design are
to satisfy certain conditions to make the weights estimable. Thus,
construction problems arise for obtaining the groups, both for ensuring
estimability and increase of precision.

9.3 Method of Estimation

In a weighing the observation consists of the weight which is required for
balancing. In one pan weighing the balancing weight is always placed
on the same pan. But in two pan weighing the balancing weight may
occur on any of the two pans, depending on the distribution of the
objects on the two pans. Let us denote the observation from 7th weighing
by Y] (7=1, 2,..., N) and the weight of ithobject by w* (i=l,2, 3,...,p).
The model for estimation of the weight is as below:

Yj=2 0{jwi~\-€ (7—1> 2,..., N)

where aj, takes the values +1, -1, or 0 according as the ith object is on
the left pan, right pan or does not occur in the 7th weighing and e is the
error component having a constant variance, a2.

In a two pan weighing if the balancing weight is placed on the right
pan then the observation consists of this weight as such. If the
balancing weight occurs on the left pan, the observation then consists of
minus one time the balancing weight. Thus, Yt denotes an observation

mcludngieast estimates cf the weight of the objects can be

obtained by the usual method when N^p.

282

DESIGN AND ANALYSIS OF EXPERIMENTS

Using matrix notation the model can be written as

Y=AW+E

where Y is the vector of the observation written as a column, A is the
Nxp matrix;

an

an

dp 1 '
\

#22 • • •

#p2

alN

#2 N • • •

•

apN / /

f

W is the column vector of the weight of the objects and E is the vector
of the error component in the different observations.
The least squares estimates of W are given by

fV^CA'A)-1 (A'Y)

Var. (Wi) is o2 times the zth element in the diagonal of (A'A)-1.
The method has been illustrated through several series of designs

presented in sections 9.4 and 9.5.

9.4 Incomplete Block Designs as Weighing Designs

All incomplete block designs provide a type of grouping of v objects into
b groups. Most of these designs can be used as weighing designs, in
which the treatments are taken to correspond to the objects for weighing
and the contents of a block as the objects for weighing together in a
weighing. Several series of weighing designs corresponding to known
series of incomplete block designs have been discussed below.

9.4.1 One Pan Weighing Design from B.I.B. Designs

A balanced incomplete block designs has b blocks. The contents of each
of these blocks can be taken as the groups for a one pan design.
Denoting the parameters of a B.I.B. design by v, b, r, k and A as usual,
we have, thus, for such weighing designs

ni=k, p=v, N=b, «2=0, n0=v—k

The model for such designs is

Yj—2 au w/+e for the yth weighing

where otj=0 if the zth object is not taken in y'th weighing

= 1 otherwise

The normal equations from the least squares theory are as below:

rWj+A 2 wj=Ti (z= 1, 2,.. ,,v)

(9.1)

WEIGHING DESIGNS

283

where Tt is the sum of the observations from those weighings in which
the ith object occurs.

The equation (9.1) can be written as

(r-A) w(+A 2 Wj=Tj (9.2)

Adding (9.2) over i we get

(vA+r—A) 2 w/=2 Tj

That is, 2 since vA+r—\=rk.

-Thus, "<=^{ *H£'} (9.3)

It can be shown that

2 Ti=kG

where G is the total of all the observations.

Thus, we get

«r^(r'-T) <9-4>

The coefficient of T) in the solution of wi at (9.3) gives the variance

✓s

of wt, because this coefficient occupies the diagonal position in the ith row
of (A'A)-1

Accordingly, Var. (w/)=^^ '

In some balances the pointer needle does not settle on the zero position
when both the pans are empty. Such balances are said to need zero
correction and an observation from a weighing on it is said to be biased.
If for a one pan design the estimate of weight comes out as a < contrast
among the observations, this bias which is constant in all the weighings
in a balance, gets automatically eliminated and hence no separate
correction for zero bias is needed.

As the estimate at (9.4) is not a contrast it is not free from any

possible bias.

9.4.2 Some Variations of Balanced Incomplete Block Design

In addition to the b weighings corresponding to the b blocks of a B.I.B.
design one more weighing with all the objects on one pan is taken. Let
the observation from this additional weighing be denoted by R.

The normal equations for this design are

(r-fl)wH-(A-H) 2 wj = Ti (i=1.2,..-., v) (9.5)

j* i

where Tt is the sum of the observations from those weighings which involve
the zth object including R.

284

DESIGN AND ANALYSIS OF EXPERIMENTS

The equation (9.5) can be written as

(r-A) (9.6)

Adding this equation over i we get

{v (A1)—J-/"—A} 2 vv/=2 Tt

From (9.6) (9-7)

It can be shown that 27’i=A:G+vJRwhere Gis the total of b observations

corresponding to the b blocks of the B.I.B. design.

Thus, wi

Tr

(A+l) (kG+vR) 1
1
v+rk

Var(wO=^{l-t£jfc}-

This estimate is again not a contrast.

9.4.3 Estimate of Weight as Contrast of Observations

The estimate at (9.7) can be modified as discussed below in order to make

it a contrast.

Considering only the b observations corresponding to the b blocks of

a B.I.B. design, we have seen in section 9.4.1 that r2 wj=G.

✓s

Again, we have 2 wj=R.

„ a G+cR
From the above zwj——~—

where c is an unknown constant.

Substituting this estimate of 2 wj in (9.6) we get

, .s - U (A+l) (G+cR) )
(r-A) ».,=|r,-—-f

(9.8)

By equating the sum of the coefficients of observations to zero we solve

for c, giving c=(v—r—1)1 k. Substituting this value of c in (9.8) we get

A
Wi

kG—i

(9.9)

* ro2 J. k r+k 1

v<w')“(7--W

The estimate at (9.8) though a contrast, is not the least square estimate.
Its variance is greater than the variance of the estimate at (9.7) which is
the least squares estimate.

By taking the B.I.B. design with

v=b=7, r=k=3, A=l,

WEIGHING DESIGNS

285

along with an extra weighing involving all the objects, we get the design
used by Yates (1935) as illustration. The estimate provided by Yates
follows from that at (9.9). Thus, the estimate suggested by Yates is not
the least squares estimate, but it has the advantage that it is free from
zero bias.

It would be noticed that for a B.I.B. design without the extra weighing
involving all the objects the expression for the estimate of weight and that
for the inter-block estimate of B.I.B designs are the same. In both these
situations the same model is used.

9.4.4 Reinforced Incomplete Block Designs as Weighing Designs

Das (1958), introduced the reinforced incomplete block designs. These
are incomplete block designs augmented by including in every block some
extra treatments and then taking some more blocks in each of which all
the treatments are present. Such designs can also be used as weighing
designs, excepting that only one extra object is to be taken to be weighed
in every weighing along with the other objects corresponding to the
contents of the blocks of the original incomplete block design. One more
extra weighing involving all the objects is also taken. We shall call such
designs reinforced weighing designs.

The normal equations for the estimation of the weights from these

designs are

(6+1) J+(r+l) 2 wj=S (9.10)

(r+1) J+(r+l) w/+(A+l)2 wj—Tt (i=»l, 2,.. .,v) (9.11)

where s denotes the weight of the extra object and 5 in the sum of all the

(6 + 1) observations.

Equation (9.11) can be written as

(r+1)s+(r—A) W/+(A+1) 2 = (9.12)

Adding these equations over i

v(r+l) 5+{r(X+l)+r—A} 2 w,=^T, (9.13)

Solving the equations at (9.10) and (9.13) for s and 2 wj we get

^ (v+rk) S'—(r+1) 2 7)
‘S_" (b—r)(v—k)

(6+1) 2 Ti—v (r+1) S

and Iwj- (b-r)(y-k)

Substituting the values of s and 2 wj in (9.11) and simplifying we get

^ Tt (r+fc+1—v)2 Ti—k (r+l)_S'

r(y—k)%

286

DESIGN AND ANALYSIS OF EXPERIMENTS

Var.

r+k-\-\—v)
f r(v-Ar)2 f

Var. (j)=o2

iy+rk)
(b-r) (v-k)

It is seen that for the series of original B.I.B. designs having parameters

v=4A-|-3, r=k=2h-\-\, A, Var. (s) is greater than Var. (w,) even though
the extra object is involved in b+1 weighings which is larger than the
number of weighings in which other objects are involved, viz. (r+1).
This seems to be contrary to expectation.

9.5 Two Pan Weighing Designs from B.I.B. Designs

Each block of a B.I.B. design indicates k objects. Let these objects be
placed on the left pan and the remaining (v—k) objects be placed on the
right pan. Next, balancing is made and the balancing weight is the
observation corresponding to this block. For b blocks we get b such
observations. Such a scheme of weighing is called two pan weighing.
The two sets of objects for each weighing are obtained one from a block
of B.I.B. design and the other from its complementary block.

The normal equations for this scheme are

bwi+(b-4r f 4A) 2 wj=T, (/= 1, 2,...,v) (9.14)

where T\ is the sum of the observations from those weighings in which the
ith object is involved, minus the sum of the remaining observations.

These equations can also be written as

4(r-A) w,-f(6-4r+4A) 2 Wj=Ti

(9.15)

Adding such equations over i we get

that is

since

and

(v(6—4r+4A)+4(r-A)}2 wj=2Ti

v * 2T,

bv—4 (r—A)(v—1)

G
“(2 r-by

2 T,=(2k-v) G

6v—4(r—A) (v-l)=(2A:_v) (2r-b)

Substituting for 2 wj in(9.15)

A 1
Wi—~.

4 (r—A)

(b—4r4r4'K) 2 Tj 1
( bv—4 (r—A) (v— 1 )j

1
4 (/—A)

jT _(b-4r+4\) G\
X 2 r-b l

WEIGHING DESIGNS

287

A)=4<^d  l-

6—4r+4A 4A 1
-2k)\

(b-2r) (v-

It will be seen that no estimation of the weight is possible for such
B.I.B. designs with v=2k, as estimate of 2 w} is not possible. If, however,
an extra weight involving all the objects be taken, the estimates are available
for all B.I.B. designs. The normal equations in this situation are

that is,

giving

(6+1) w,+(6-4r+4A+l) 2 Wj=T,

4 (r-A) vv,+(6-4r+4A+l) 2 wj=Tt

_1_
(r-X)
1
4 (r-A)

(6—4r+4A+l) 2 7))
(v—rk) (6—2r)+ v j

(6—4r+4A+l) {(2k—v) G + vR}
(v—2k) (6—2r)+v

Var. (w,)=

4 (r-A)

(6 —4r+4A4-1) )
(v—2k) (6-2r)+vJ

9.5.1 Reinforced B.I.B. Designs for Two Pan Weighing Designs

We have already discussed one pan reinforced designs using B.I.B. designs.
These designs can also be used for two pan weighing designs. One
extra object is taken in each weighing and is placed on the same pan every
time. Further, one more weighing involving all the (v+1) objects is taken.

The normal equations for these designs are

(6+1) j+(2r—6+1) 2 wj=S

(2r-6+l) S+(6 + l) w/+(6—4r+4A+l) 2 wj=Ti (j=\, 2,.. .,v)

where S is the sum of all the observations and s is the effect of the extra
treatment.

That is, (6+1) £+(2r~6+l) 2 wj=S

(2r—6+1) j+4 (r—A) hv+(6—4r+4A+l) 2 wj=lT,

Adding (9.17) over i,

(9.16)

(9.17)

v(2r—6+1) j+{v(6—4r+4A+l)+4 (r-A)} 2 wj=Ti

(9.18)

Solving for s and 2 wj from the equations (9.16) and (9.18)

- {(v-2k) (6 —2r)+v} 5*—(2r—6+1) 2 T,
s=
(6+1) {(v—2k)(b—2r)+v}—v(2r—6+1)2

v ;,r_(6+1) 2 Ti — v (2r—6+1) S

J (6+1) {(v-2k) (6—2r)+vj— v(2r — 6+1 f

Substituting for s and 2 wj in equation (9.17)

I

288

DESIGN AND ANALYSIS OF EXPERIMENTS

Wf-  4 (r—A) {

Tt-— 2T“

(2r-b+l) {(v-2k) (b -2r)+v} S-(2r-fr-t-l) 2 Tt

(b—4r+4X+l) {(^-+-1) Tt v (2r b-\-l) 5}^
' A" 3

where

A =0+1) {(v—2k) 0-2r)+v}-v (2r-b + lf

=4 (b-r) (v—k)

Var. (wt)

4 (r

f, , fr + n»-(t + l) J-D1
}
+ (*-'■) (»-*)

Var. (j1)

a2 {(v-2fc) (6-2r+v>
4 0-r) (v k)

9.5.2 Reinforced B.I.B. Designs with Parameters

v=b=4X+3, r=k=2X+1, X

Substituting the parameters of the B.I.B. desings of the series v=6=4X+3,
r_£_-2X+l, X in the results obtained in Section 9.5.1 we get the estimate

of vvj as

/v T, __ Tt
w,~4 (r-X) 4(X+1)

since for this series 2r-b+l=0 and &-4r+4X + l=0,

- S

4 (X+l)

2

v(»,)='’W=4^pjy-

It will be seen that for this series of designs the estimates, wt are con¬

A

trasts, but not s. Even though vv/’s are contrasts, zero bias, if any, is not
eliminated automatically from the estimate because the bias does not occur
with the same sign in all the observations. As in a two pan design the
balancing weight is put on any of the pans depending on the weights of
the individual objects, the bias does not remain constant in the different
weighings but changes sign. If in a biased balance the weight of an object
is observed as w+B when placed on the left pan, it will be observed as
w—B when placed on the right pan. Here w is the true weight of the
object and B stands for the bias. One way out of this difficulty is to take
a known weight which is big enough so that when it is put always on the
same pan, say, the left pan, the balancing weight always comes on the

other pan. In this situation the estimates w.-’s are unbiased but not s
which has to be adjusted for the extra known weight and possible bias in

the balance.

For these series of designs the variance of any of the weights is g2/N.
As for this series of designs the number of objects is equal to the number

WEIGHING DESIGNS

289

of weighings, it is not possible to get the estimate of error from it. To get
the estimate of error variance, the designs may be repeated.

When 4A+3 is a prime or a prime power, a method of construction of
such designs has been given by Bose (1939). For other cases these designs
can be obtained from Plackett and Burman (1946). These designs are also
provided by the Hadamard matrices by taking the objects corresponding to
+1 on one pan and those with — 1 on the other.

9.6 Two Associate P.B.I.B. Designs as One Pan Weighing Designs

Two associate P.B.I.B. designs with b ^ v can be used as one pan weighing
design just as in the B.I.B. designs.

Denoting the parameters of the P.B.I.B. designs as usual, the normal

equations for such designs are

5,(vv/)-f fy=Ti (/=1, 2,.. .,v)

(9.19)

Adding these equations over the first associate treatments (objects) we

get

n^Wi+S^Wi) (r+XLp111+'h2pn1)+ S£w() (A 1p11t+'KaPn*)**S1(Tt) (9.20)

By adding all the normal equations and simplifying, it can be shown

that

2 m-w+S,

where G is the total of all the observations.

Substituting ^^(>Vf) for S2 (w;) in (9.20) we get

(wi)—S1 (T,)-j (A^+A^a2) (9.21,)

where

and

^11— nl\ ^iPll ^iPli

■Si2==r+Ai Pn+\Pii-\ Pn~K Pn

Eliminating S2 (w,) from equation (9.19) we get

(r—A2) wi+S1 (wt) (A,-A2) =7)-:

(9.22)

Solving for wt from equations (9.21) and (9.22)

(Aj—A,) Bn-{r±A*) B12

v(vv/)=—-  {r-\) Bn-(\-\) Bn

This variance is the same for all the estimates.

290

DESIGN AND ANALYSIS OF EXPERIMENTS

9.7 Weighing Designs from Truncated Incomplete B.I.B. Designs

If from the different blocks of a B.I.B. design a number of treatments,
say, q is omitted, the design now has v—q treatments, b blocks, r replica¬
tions but unequal block sizes. Such designs can also be used as weighing
designs. The estimates for such designs will, however, have correspon¬
ding changes. For example, for the series of designs presented in 9.4.1
the normal equations at 9.2 when added over /which now varies as

(/ = 1, 2,..., v—#) becomes

{(v—9) A+r—A} 2 w,=2 7/

From this the estimate of wt comes out as

A
Wt

1
r-A

2 T, {
rk—vq j

Similar modifications are needed for the other series of designs also. It

has to be kept in mind that while estimating 2 wj the summation of the
normal equations is to be taken over the existing v—q treatments
(objects) As a result the forms of the estimates will change.

Through this device the number of weighings can be increased relative
to the number of objects. As such when symmetrical B.I.B. designs are
used, error d.f. can be obtained through such truncation.

9.8 Efficiency

Considerable literature on efficiency of weighing designs is available
(Banerjee, 1975). It appears that the importance of efficiency on the part
of weighing designs is less than that for designs for biological experi¬
ments. The errors in weighing designs can be reduced considerably by
laboratory refinement of the balances, while such reduction of error is
not possible for biological experiments. However, Hotelling (1944)
showed that the minimum variance attainable for N weighing through
the technique of group weighing is a2/A. We have seen that for
the series of reinforced B.I.B. designs with parameters v=6=4A+3,
r—k=2k+l, A this minimum variance could be reached. Further since
the operation of weighing is neither very costly nor time consuming, loss
of efficiency can be made good by increasing the number of observations.

REFERENCES

1. Banerjee, K.S. (1948). “Weighing designs and balanced incomplete blocks.”

Ann. Math. St at., 19, 394-99. ,

WEIGHING DESIGNS

291

2. Banerjee, K.S. (1949). “On certain aspects of spring balance designs.” Sankhya,

9, 367-76.

3. Banerjee, K.S. (1950). “How balanced incomplete block designs may be made
to furnish orthogonal estimates in weighing designs.” Biometrika, 37, 50-58.

4. Banerjee, K.S. (1975). Weighing Designs. Marcel Dekker, New York.
5. Bose, R.C. (1939). “On the construction of balanced incomplete block designs.”

Ann. Eugenics, 9, 353-99.

6. Das, M.N. (1958). “Reinforced incomplete block design.” Jour. Ind. Soc.

Agri. Stat., 10, 73.

7. Dey, A. (1969). “A note on weighing designs. Ann. Inst. Stat, Math., 21,

343-46.

8. Dey, A, (1971). “On some chemical balance weighing designs.” Aust. J. Stat.,

13, No. 3, 137-41.

9. Hotelling, H. (1944). “Some improvements in weighing and other experimental

techniques.” Ann. Math. Stat., 15, 297-306.

10. Kempthorne, O. (1949). “The factorial approach to the weighing problem.”

Ann. Math. Stat., 19, 238-48.

11. Kishen, K. (1945). “On the design of experiments for weighing and making

other types of measurements.” Ann. Math. Stat., 16, 294-300.

12. Mood, A.M. (1946). “On Hotelling’s weighing problem.” Ann. Math. Stat.,

17, 432-46.

13. Plackett, R.L. and Burman, J.P. (1946). “The design of optimum multifactorial

experiments.” Biometrika, 33, 305-25.

14. Raghavarao, D. (1959). “Some optimum weighing designs.” Am. Math. Stat.,

30, 295-303.

15. Raghavarao. D. (1960). “Some aspects of weighing designs.” Ann. Math.

Stat., 31, 878—84.

16. Yates, F. (1935). “Complex experiments.” J. Roy. Stat. Soc. Suppl., 2,

181-247.

Index

accuracy, 3
additivity, 17
adjusted sum of squares, 37

totals, 36

affine resolvable designs, 161
alias, 108, 109
analytical dillusion assay, 217
analysis of covariance, 44, 108, 109, 263
analysis of variance, 8, 10, 50, 54, 59, 82,

105, 166, 173, 183, 185

ancillary variate, 263
A-optimum, 198
association, matrix, 179

scheme, 177

assumptions, analysis of variance, 43,276
asymmetrical factorials, 120

analysis of, 133
balance in, 122
confounding, 120

balanced data, 42
B.I.B. designs, 153, 156

analysis of, 166
construction of, 158
efficiency, 167, 168
tinter-clock analysis, 168
parameters, 156
parametric relations, 157
randomization, 154
repeated designs, 158
symmetrical design, 158

bar diagram, 22, 23
bias, 7
binary designs, 155
bio-assays, 78

designs, 217, 219
direct assays, 218
indirect assays, 220
standard preparation, 220
test preparation, 227

central composite designs, 254
circulant design, 212
circular design, 154
classification of data, 17

m-\yay, 19

one-way, 19
two-way, 19

comparative dillusion assay, 218
complementary design, 165
completely rendomized design, 48

analysis of, 50
design, 48

concomitant variate, 44
confounding, 86, 95
partial, 87, 95
total, 87, 95

connected design, 155
contrast, 10, 11

analysis of variance, 10
maximum number, 12
method of writing, 12
orthogonal, 11
sum of squares, 11
control treatment, 80
correction term, 25
critical difference, 22, 56
cyclic design, 182

defining contrast, 108
degrees of freedom, 5, 18, 21
direct assay, 218
dose response relation, 221
dual design, 166
Duncan’s test, 23, 56

efficiency factor, 167, 168, 176
E-optimum, 199
error control, 37, 10
estimation,

maximum likelihood method, 3
theory of, 3

experiment, principal, 3, 7
experimental error, 8
experimental units, 2
groupings of, 3,10

factor of asymmetry, 123
factorial experiments, 78, 79

analysis of, 82, 105
asymmetrical, 79
confounding, 86, 95

294

construction of, 97
designs for, 80
mixed, 79
symmetrical, 79
2n-factorial, 80
3n-factorial, 91
4»-factorial, 96
fiducial limits, 219
Fieller’s theorem, 219
fractional factorial, 107

analysis of, 113

generalized interaction, 89,97
generating blocks,

from key block, 102

Golai’s field, 84, 160

minimum function, 84
primitive root, 84
Graeco latin square, 62
group divisible, 181

hypothesis, 3, 4

null, 4
test of, 3

incomplete block design, 152
increment factor, 110
industrial experiment, 2^
inference, 3
initial block, 162, 164
interactions, 78, 82

contrast, 81
effects, 79
generalized, 89, 97
higher order, 82

inter-block analysis, 168, 186

key block, 89

latin square design, 48

analysis of, 59
missing observations, 71
missing row, 69
orthogonal, 63
randomization of, 58
repeated, 61

latin square type design, 181, 182
latice design, 154, 172

analysis of, 173
construction of, 173
cubic, 154, 173
efficiency, 176
square, 172
least squares, 3
level code, 80

INDEX

in asymmetrical factorial, 123

local control, 10, 50, 53

main effects, 78

contrast for, 78

main plot treatment, 144
maximum likelihood method, 17
maximum number of factors, 103, 104
mean, 3
mean squares, 13
measures of variation, 13
method of difference, 162
minimum function, 84
missing observations, 56, 64, 71

covariance analysis, 274

mixed model, 16
models, 16
fixed, 16
mixed, 16
random, 16

module, 83

element of, 83

multiple range test, 23, 33

non-orthogonal data, 26

analysis of, 35
co-variance analysis, 267, 272

one-way classified data, 19

analysis, 19
error, 19
precision, 22

optimality of designs, 198
orthogonal array, 210, 211
orthogonal data, 26
orthogonal latin squares, 63, 205

construction of, 206
Euler’s conjecture, 205
falsity of ruler’s conjecture, 211
maximum number, 205
of order 3m+l»=, 212
of order 14, 213
of order 26, 214

pairwise balanced designs, 209
parallel line assays, 222, 224

analysis of, 226
design for, 229
symmetrical, 224

parameters, 3, 4

estimation of, 3

P.B.I.B. designs, 154, 176
analysis of, 183, 185
association matrix, 179

INDEX

association scheme, 177
classification of, 180
efficiency of, 186
incidence matrix, 166
parametric relation, 178

pilot experiment, 9
precision of,

comparisons, 3
experiments, 8
primitive root, 84
principal block, 89
probabilities, 4
pseudo factors, 123

quasi-factorial designs, 154

random model, 16
random number table, 49
randomization, 3, 7, 48, 53
randomized block designs, 48, 52

analysis of, 54
blocks, 52
missing observations, 56, 64

reinforced designs, 154, 285
relative potency, 217, 219
replication, 3, 7
reparametrized treatments, 134
resolvable designs, 161
response surfacfe designs, 244

linear designs, 244
second order designs, 246
variance of, 248
rotatable designs, 250
construction of, 251

sampling distribution, 4
sign test, 81, 82
significance levels, 4

1 per cent, 4
5 per cent, 4

slope ratio assays, 223, 236

analysis of, 238
blank contrast, 237
design for, 238
intersection contrast, 237
modified design, 239

split-plot design, 143
analysis of, 144
main plots, 144
sub plots, 144

variance of treatment, 147
standard error, 10
standard preparation, 207
statistic, 4

295

statistical tables, 4
Student-Newman test, 23, 33
sub plot treatment, 144
sub standard square, 205, 206
symmetrical B.I.B. design, 158

test preparation, 217
test statistics, 4

Duncan’s test, 23, 26
F-test, 5, 6
multiple range, 23, 33
one sample t-test, 5
one tailed test, 6
sensitivity of, 8, 9
Student Newman test, 23, 33
t-test, 5
two tailed test, 6
variance ratio list, 5
testing of hypothesis, 3,4
three-way classified data

analysis of, 34

tolerance, 218

distribution of, 218
log distribution, 218, 220

transformation of data, 44, 275, 278
transformation of dose, 221, 222

linearizing, 222, 223

treatment combinations, 80

writing of, 80

treatments, 2, 8, 152
triangular designs, 181

two-way classified data, 26, 27
analysis of, 26, 27
interaction, 27
orthogonal, 26
proportionate frequency, 27

validity of experiments, 3,7
validity test, 223, 237
variance, 3

error, 7, 8

varietal trials, 78, 152

weight for interblock estimate, 189
weighing designs, 280

definition, 280
efficiency of, 290
from B.I.B. design, 282
from P.B.I.B. designs, 289
method of estimation, 281
one-pan design, 282
two-pan design, 286

Yates’ algorithm, 105
Youden squares, 172


