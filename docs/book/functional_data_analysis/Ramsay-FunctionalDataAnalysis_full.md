# Springer Series in Statistics

J.O. Ramsay
B.W. Silverman


# Functional Data Analysis


<figure>

S
1843

Springer

</figure>


<!-- PageBreak -->


## Springer Series in Statistics

Advisors:

P. Bickel, P. Diggle, S. Fienberg, K. Krickeberg,
I. Olkin, N. Wermuth, S. Zeger

<!-- PageFooter="Springer Science+Business Media, LLC" -->
<!-- PageBreak -->


## Springer Series in Statistics

Andersen/Borgan/Gill/Keiding: Statistical Models Based on Counting Processes.
Atkinson/Riani: Robust Diagnotstic Regression Analysis.

Berger: Statistical Decision Theory and Bayesian Analysis, 2nd edition.

Borg/Groenen: Modern Multidimensional Scaling: Theory and Applications

Brockwell/Davis: Time Series: Theory and Methods, 2nd edition.

Chan/Tong: Chaos: A Statistical Perspective.

Chen/Shao/Ibrahim: Monte Carlo Methods in Bayesian Computation.

David/Edwards: Annotated Readings in the History of Statistics.

Devroye/Lugosi: Combinatorial Methods in Density Estimation.

Efromovich: Nonparametric Curve Estimation: Methods, Theory, and Applications.

Eggermont/LaRiccia: Maximum Penalized Likelihood Estimation, Volume I:
Density Estimation.

Fahrmeir/Tutz: Multivariate Statistical Modelling Based on Generalized Linear
Models, 2nd edition.

Farebrother: Fitting Linear Relationships: A History of the Calculus of Observations
1750-1900.

Federer: Statistical Design and Analysis for Intercropping Experiments, Volume I:
Two Crops.

Federer: Statistical Design and Analysis for Intercropping Experiments, Volume II:
Three or More Crops.

Ghosh/Ramamoorthi: Bayesian Nonparametrics.

Glaz/Naus/Wallenstein: Scan Statistics.

Good: Permutation Tests: A Practical Guide to Resampling Methods for Testing
Hypotheses, 2nd edition.

Gouriéroux: ARCH Models and Financial Applications.

Gu: Smoothing Spline ANOVA Models.

Györfi/Kohler/Krzyżak/ Walk: A Distribution-Free Theory of Nonparametric
Regression.

Haberman: Advanced Statistics, Volume I: Description of Populations.
Hall: The Bootstrap and Edgeworth Expansion.

Härdle: Smoothing Techniques: With Implementation in S.

Harrell: Regression Modeling Strategies: With Applications to Linear Models,
Logistic Regression, and Survival Analysis

Hart: Nonparametric Smoothing and Lack-of-Fit Tests.

Hastie/Tibshirani/Friedman: The Elements of Statistical Learning: Data Mining,
Inference, and Prediction

Hedayat/Sloane/Stufken: Orthogonal Arrays: Theory and Applications.

Heyde: Quasi-Likelihood and its Application: A General Approach to Optimal
Parameter Estimation.

Huet/Bouvier/Gruet/Jolivet: Statistical Tools for Nonlinear Regression: A Practical
Guide with S-PLUS Examples.

Ibrahim/Chen/Sinha: Bayesian Survival Analysis.

Jolliffe: Principal Component Analysis.

Kolen/Brennan: Test Equating: Methods and Practices.

<!-- PageFooter="(continued after index)" -->
<!-- PageBreak -->

J.O. Ramsay

B. W. Silverman


## Functional Data Analysis

With 98 Figures


<figure>

S
Springer

</figure>


<!-- PageBreak -->

J.O. Ramsay
Department of Psychology
McGill University
Montreal, Quebec H3A 1B1
Canada

B.W. Silverman
Department of Mathematics
University of Bristol
University Walk
Bristol BS8 1TW, United Kingdom

Library of Congress Cataloging-in-Publication Data
Ramsay, J. O. (James O.)

Functional data analysis / J.O. Ramsay, B.W. Silverman.
p.
cm. - (Springer series in statistics)
Includes bibliographical references (p. - ) and index.
1\. Multivariate analysis I. Silverman, B. W., 1952-
II. Title. III. Series.
QA278.R36 1997
519.5-dc21
96-54279

Printed on acid-free paper.

ISBN 978-1-4757-7109-1
ISBN 978-1-4757-7107-7 (eBook)
DOI 10.1007/978-1-4757-7107-7

C 1997 Springer Science+Business Media New York
Originally published by Springer-Verlag New York, Inc. in 1997.
Softcover reprint of the hardcover 1st edition 1997

All rights reserved. This work may not be translated or copied in whole or in part without the
written permission of the publisher Springer Science+Business Media, LLC, except for brief
excerpts in connection with reviews or scholarly analysis. Use in connection with any form
of information storage and retrieval, electronic adaptation, computer software, or by similar
or dissimilar methodology now known or here-after developed is forbidden.

The use of general descriptive names, trade names, trademarks, etc., in this publication, even
if the former are not especially identified, is not to be taken as a sign that such names, as
understood by the Trade Marks and Merchandise Marks Act, may accordingly be used freely
by anyone.

987654
SPIN 11008835

<!-- PageFooter="springeronline.com" -->
<!-- PageBreak -->


## Preface

This book is a snapshot of a highly social and, therefore, decidedly
unpredictable process. The combined personal view of functional data
analysis that it presents has emerged over $a$ number of years of
research and contact, and has been greatly nourished by delightful
collaborations with many friends. We hope that readers will enjoy the
book as much as we have enjoyed writing it, whether they are our
colleagues as researchers or applied data analysts reading the book
as a research monograph, or students using it as a course text.

After some introductory material in Chapters 1 and 2, we discuss
aspects of smoothing methods in Chapters 3 and 4. Chapter 5 deals
with curve registration, the alignment of common characteristics of
a sample of curves. In the next three chapters, we turn to functional
principal components analysis, one of our main exploratory techniques.
In Chapters 9 to 11, problems that involve covariate information are
considered in various functional versions of the linear model. The
functional analogue of canonical correlation analysis in Chapter 12
explores the relationship between two functional variables treating
them symmetrically. Chapters 13 to 15 develop specifically functional
methods that exploit derivative information and the use of linear
differential operators. Our final chapter provides historical remarks
and some pointers to possible future developments.

Data arising in real applications are used throughout for both
motivation and illustration, showing how functional approaches allow

<!-- PageBreak -->

<!-- PageHeader="vi Preface" -->

us to see new things, especially by exploiting the smoothness of the
processes generating the data. The data sets exemplify the wide scope
of functional data analysis; they are drawn from growth analysis,
meteorology, biomechanics, equine science, economics, and medicine.
Some of these data sets, together with the software we have used to
analyse them, are available from a world-wide web site described at the
end of Chapter 1.

Many people have been of great help to us in our work on this
book. In particular we would like to thank Michal Abrahamowicz,
Philippe Besse, Darrell Bock, Jeremy Burn, Catherine Dalzell, Shelly
Feran, Randy Flanagan, Rowena Fowler, Theo Gasser, Mary Gauthier,
Vince Gracco, David Green, Nancy Heckman, Anouk Hoedeman, Steve
Hunka, Iain Johnstone, Alois Kneip, Wojtek Krzanowski, Xiaochun Li,
Duncan Murdoch, Kevin Munhall, Guy Nason, Richard Olshen, David
Ostry, Tim Ramsay, John Rice, Xiaohui Wang and Alan Wilson. We
gratefully acknowledge financial support from the Natural Science
and Engineering Research Council of Canada, the National Science
Foundation and the National Institute of Health of the USA, and the
British Engineering and Physical Sciences Research Council. Above all,
our thanks are due to the Royal Statistical Society Research Section; our
first contact was at a discussion meeting where one of us read a paper
and the other proposed the vote of thanks, not always an occasion that
leads to a meeting of minds!

November 1996

Jim Ramsay
Bernard Silverman

<!-- PageBreak -->


## Contents


### 1


<table>
<tr>
<th colspan="3">Introduction</th>
<th>1</th>
</tr>
<tr>
<td>1.1</td>
<td colspan="2">What are functional data?</td>
<td>1</td>
</tr>
<tr>
<td>1.2</td>
<td colspan="2">Some functional data analyses</td>
<td>3</td>
</tr>
<tr>
<td>1.3</td>
<td colspan="2">The goals of functional data analysis</td>
<td>8</td>
</tr>
<tr>
<td>1.4</td>
<td colspan="2">First steps in a functional data analysis</td>
<td>9</td>
</tr>
<tr>
<td></td>
<td>1.4.1</td>
<td>Data representation: smoothing and interpolation</td>
<td>9</td>
</tr>
<tr>
<td></td>
<td>1.4.2</td>
<td>Data registration or feature alignment</td>
<td>9</td>
</tr>
<tr>
<td></td>
<td>1.4.3</td>
<td>Data display</td>
<td>10</td>
</tr>
<tr>
<td>1.5</td>
<td colspan="2">Summary statistics for functional data</td>
<td>11</td>
</tr>
<tr>
<td></td>
<td>1.5.1</td>
<td>Mean and variance functions</td>
<td>11</td>
</tr>
<tr>
<td></td>
<td>1.5.2</td>
<td>Covariance and correlation functions</td>
<td>11</td>
</tr>
<tr>
<td></td>
<td>1.5.3</td>
<td>Cross-covariance and cross-correlation functions</td>
<td>13</td>
</tr>
<tr>
<td>1.6</td>
<td colspan="2">Exploring variability in more detail</td>
<td>16</td>
</tr>
<tr>
<td></td>
<td>1.6.1</td>
<td>Functional principal components analysis</td>
<td>16</td>
</tr>
<tr>
<td></td>
<td>1.6.2</td>
<td>Functional linear modelling</td>
<td>16</td>
</tr>
<tr>
<td></td>
<td>1.6.3</td>
<td>Functional canonical correlation</td>
<td>17</td>
</tr>
<tr>
<td>1.7</td>
<td colspan="2">Using derivatives in functional data analysis</td>
<td>18</td>
</tr>
<tr>
<td></td>
<td>1.7.1</td>
<td>Correlation plots for derivatives</td>
<td>18</td>
</tr>
<tr>
<td></td>
<td>1.7.2</td>
<td>Plotting pairs of derivatives</td>
<td>19</td>
</tr>
<tr>
<td></td>
<td>1.7.3</td>
<td>Principal differential analysis</td>
<td>20</td>
</tr>
<tr>
<td>1.8</td>
<td colspan="2">Concluding remarks</td>
<td>21</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="viii Contents" -->


### 2


<table>
<tr>
<td colspan="2">Notation and techniques</td>
<td>23</td>
</tr>
<tr>
<td>2.1</td>
<td>Introduction</td>
<td>23</td>
</tr>
<tr>
<td>2.2</td>
<td>General notation</td>
<td>24</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>2.2.1 Scalars, vectors, functions and matrices</td>
<td>24</td>
</tr>
<tr>
<td>2.2.2 Combining quantities</td>
<td>25</td>
</tr>
<tr>
<td>2.3</td>
<td>Inner products $\langle x , y \rangle \ldots .$</td>
<td>25</td>
</tr>
<tr>
<td></td>
<td>2.3.1 Some specific examples</td>
<td>25</td>
</tr>
<tr>
<td></td>
<td>2.3.2 General properties</td>
<td>27</td>
</tr>
<tr>
<td></td>
<td>2.3.3 Descriptive statistics in inner product notation</td>
<td>29</td>
</tr>
<tr>
<td></td>
<td>2.3.4 Some extended uses of inner product notation</td>
<td>30</td>
</tr>
<tr>
<td>2.4</td>
<td>Further aspects of inner product spaces</td>
<td>31</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>2.4.1 Projections</td>
<td>31</td>
</tr>
<tr>
<td>2.4.2 Quadratic optimization</td>
<td>32</td>
</tr>
<tr>
<td>2.5</td>
<td>The multivariate linear model</td>
<td>32</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>2.5.1 A transformation perspective</td>
<td>33</td>
</tr>
<tr>
<td>2.5.2 The least squares solution</td>
<td>33</td>
</tr>
<tr>
<td>2.6</td>
<td>Regularizing the multivariate linear model</td>
<td>34</td>
</tr>
<tr>
<td></td>
<td>2.6.1 Definition of regularization</td>
<td>34</td>
</tr>
<tr>
<td></td>
<td>2.6.2 Hard-edged constraints</td>
<td>35</td>
</tr>
<tr>
<td></td>
<td>2.6.3 Soft-edged constraints</td>
<td>35</td>
</tr>
<tr>
<td colspan="2">Representing functional data as smooth functions</td>
<td>37</td>
</tr>
<tr>
<td>3.1</td>
<td>Introduction</td>
<td>37</td>
</tr>
<tr>
<td></td>
<td>3.1.1 Observed functional data</td>
<td>37</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>3.1.2 Sampling and observational error</td>
<td>38</td>
</tr>
<tr>
<td>3.1.3 Linear smoothing</td>
<td>43</td>
</tr>
<tr>
<td>3.2</td>
<td>Basis function methods</td>
<td>44</td>
</tr>
<tr>
<td></td>
<td>3.2.1 Least squares fitting of basis expansions</td>
<td>44</td>
</tr>
<tr>
<td></td>
<td>3.2.2 Choosing a good basis</td>
<td>46</td>
</tr>
<tr>
<td></td>
<td>3.2.3 Fourier series</td>
<td>47</td>
</tr>
<tr>
<td></td>
<td>3.2.4 Polynomial bases</td>
<td>48</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>3.2.5 Regression spline bases</td>
<td>48</td>
</tr>
<tr>
<td>3.2.6 Wavelet bases</td>
<td>49</td>
</tr>
<tr>
<td>3.3</td>
<td>Smoothing by local weighting</td>
<td>51</td>
</tr>
<tr>
<td></td>
<td>3.3.1 Kernel functions</td>
<td>51</td>
</tr>
<tr>
<td></td>
<td>3.3.2 Kernel smoothing</td>
<td>52</td>
</tr>
<tr>
<td></td>
<td>3.3.3 Localized basis function estimators</td>
<td>54</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>3.3.4 Local polynomial smoothing</td>
<td>55</td>
</tr>
<tr>
<td>3.3.5 Choosing the bandwidth</td>
<td>55</td>
</tr>
<tr>
<td>3.4</td>
<td>Summary</td>
<td>56</td>
</tr>
</table>


### 3

<!-- PageBreak -->


<table>
<tr>
<th colspan="2"></th>
<th>Contents</th>
<th>ix</th>
</tr>
<tr>
<td colspan="2">4 The roughness penalty approach</td>
<td></td>
<td>57</td>
</tr>
<tr>
<td colspan="2">4.1 Introduction</td>
<td></td>
<td>57</td>
</tr>
<tr>
<td>4.2</td>
<td>Spline smoothing</td>
<td></td>
<td>58</td>
</tr>
<tr>
<td></td>
<td>4.2.1 Two competing objectives in function</td>
<td>estimation</td>
<td>58</td>
</tr>
<tr>
<td></td>
<td colspan="2">4.2.2 Estimating derivatives by spline smoothing</td>
<td>60</td>
</tr>
<tr>
<td></td>
<td>4.2.3 More general measures of fit</td>
<td></td>
<td>60</td>
</tr>
<tr>
<td colspan="2">4.2.4 More general roughness penalties</td>
<td></td>
<td>61</td>
</tr>
<tr>
<td>4.3</td>
<td>The regularized basis approach</td>
<td></td>
<td>62</td>
</tr>
<tr>
<td></td>
<td>4.3.1 Complementary bases</td>
<td></td>
<td>62</td>
</tr>
<tr>
<td></td>
<td>4.3.2 Specifying the roughness penalty</td>
<td></td>
<td>63</td>
</tr>
<tr>
<td></td>
<td>4.3.3 Some properties of the estimates</td>
<td></td>
<td>65</td>
</tr>
<tr>
<td></td>
<td>4.3.4 Relationship to the roughness penalty</td>
<td>approach</td>
<td>65</td>
</tr>
<tr>
<td colspan="2">5 The registration and display of functional data</td>
<td></td>
<td>67</td>
</tr>
<tr>
<td>5.1</td>
<td>Introduction</td>
<td></td>
<td>67</td>
</tr>
<tr>
<td>5.2</td>
<td>Shift registration</td>
<td></td>
<td>68</td>
</tr>
<tr>
<td></td>
<td>5.2.1 Types of alignment</td>
<td></td>
<td>68</td>
</tr>
<tr>
<td></td>
<td>5.2.2 Estimating the alignment</td>
<td></td>
<td>69</td>
</tr>
<tr>
<td colspan="2">5.2.3 Using the Newton-Raphson algorithm</td>
<td></td>
<td>71</td>
</tr>
<tr>
<td>5.3</td>
<td>Feature or landmark registration</td>
<td></td>
<td>73</td>
</tr>
<tr>
<td>5.4</td>
<td>More general transformations</td>
<td></td>
<td>79</td>
</tr>
<tr>
<td></td>
<td>5.4.1 Families of transformations</td>
<td></td>
<td>79</td>
</tr>
<tr>
<td></td>
<td>5.4.2 Fitting transformations using regularization</td>
<td></td>
<td>80</td>
</tr>
<tr>
<td></td>
<td>5.4.3 A regularized basis approach</td>
<td></td>
<td>81</td>
</tr>
<tr>
<td></td>
<td>5.4.4 Registering the height acceleration curves</td>
<td></td>
<td>82</td>
</tr>
<tr>
<td colspan="2">5.4.5 Some cautionary remarks</td>
<td></td>
<td>83</td>
</tr>
<tr>
<td colspan="2">6 Principal components analysis for functional data</td>
<td></td>
<td>85</td>
</tr>
<tr>
<td>6.1</td>
<td>Introduction</td>
<td></td>
<td>85</td>
</tr>
<tr>
<td>6.2</td>
<td>Defining functional PCA</td>
<td></td>
<td>86</td>
</tr>
<tr>
<td></td>
<td>6.2.1 PCA for multivariate data</td>
<td></td>
<td>86</td>
</tr>
<tr>
<td></td>
<td>6.2.2 Defining PCA for functional data</td>
<td></td>
<td>87</td>
</tr>
<tr>
<td></td>
<td>6.2.3 Defining an optimal empirical orthonormal</td>
<td>basis</td>
<td>90</td>
</tr>
<tr>
<td></td>
<td>6.2.4 PCA and eigenanalysis</td>
<td></td>
<td>90</td>
</tr>
<tr>
<td>6.3</td>
<td>Visualizing the results</td>
<td></td>
<td>92</td>
</tr>
<tr>
<td></td>
<td>6.3.1 Plotting perturbations of the mean</td>
<td></td>
<td>92</td>
</tr>
<tr>
<td></td>
<td>6.3.2 Plotting principal component scores</td>
<td></td>
<td>94</td>
</tr>
<tr>
<td></td>
<td>6.3.3 Rotating principal components</td>
<td></td>
<td>95</td>
</tr>
<tr>
<td>6.4</td>
<td>Computational methods for functional PCA</td>
<td></td>
<td>99</td>
</tr>
<tr>
<td></td>
<td>6.4.1 Discretizing the functions</td>
<td></td>
<td>99</td>
</tr>
<tr>
<td></td>
<td>6.4.2 Basis function expansion of the functions</td>
<td></td>
<td>100</td>
</tr>
<tr>
<td colspan="3">6.4.3 More general numerical quadrature</td>
<td>103</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="x Contents" -->


## 7


## 8

<!-- PageNumber="9" -->


<table>
<tr>
<td>6.5</td>
<td>Bivariate and multivariate PCA</td>
<td>105</td>
</tr>
<tr>
<td></td>
<td>6.5.1 Defining multivariate functional PCA</td>
<td>106</td>
</tr>
<tr>
<td></td>
<td>6.5.2 , Visualizing the results</td>
<td>107</td>
</tr>
<tr>
<td colspan="2">Regularized principal components analysis</td>
<td>111</td>
</tr>
<tr>
<td>7.1</td>
<td>Introduction</td>
<td>111</td>
</tr>
<tr>
<td>7.2</td>
<td>Smoothing by using roughness penalties</td>
<td>113</td>
</tr>
<tr>
<td>7.3</td>
<td>Estimating smoothed principal components</td>
<td>114</td>
</tr>
<tr>
<td>7.4</td>
<td>Finding the regularized PCA in practice</td>
<td>115</td>
</tr>
<tr>
<td></td>
<td>7.4.1 .1 The periodic case</td>
<td>116</td>
</tr>
<tr>
<td></td>
<td>7.4.2 4.2 The nonperiodic case</td>
<td>117</td>
</tr>
<tr>
<td>7.5</td>
<td>Choosing the smoothing parameter by cross-validation</td>
<td>118</td>
</tr>
<tr>
<td>7.6</td>
<td>An example: The pinch force data</td>
<td>120</td>
</tr>
<tr>
<td>7.7</td>
<td>Smoothing the data rather than the PCA</td>
<td>122</td>
</tr>
<tr>
<td>7.8</td>
<td>The procedure of Rice and Silverman</td>
<td>124</td>
</tr>
<tr>
<td colspan="2">Principal components analysis of mixed data</td>
<td>125</td>
</tr>
<tr>
<td>8.1</td>
<td>Introduction</td>
<td>125</td>
</tr>
<tr>
<td>8.2</td>
<td>General approaches to mixed data</td>
<td>126</td>
</tr>
<tr>
<td>8.3</td>
<td>The PCA of hybrid data</td>
<td>126</td>
</tr>
<tr>
<td></td>
<td>8.3.1 Combining function and vector spaces</td>
<td>126</td>
</tr>
<tr>
<td></td>
<td>8.3.2 Finding the principal components in practice</td>
<td>128</td>
</tr>
<tr>
<td></td>
<td>8.3.3 Incorporating smoothing</td>
<td>128</td>
</tr>
<tr>
<td></td>
<td>8.3.4 Balance between functional and vector variation</td>
<td>129</td>
</tr>
<tr>
<td>8.4</td>
<td>Combining registration and PCA</td>
<td>131</td>
</tr>
<tr>
<td></td>
<td>8.4.1 Expressing the observations as mixed data</td>
<td>131</td>
</tr>
<tr>
<td></td>
<td>8.4.2 Balancing temperature and time shift effects</td>
<td>131</td>
</tr>
<tr>
<td></td>
<td>8.4.3 Application to the weather data</td>
<td>132</td>
</tr>
<tr>
<td></td>
<td>8.4.4 Taking account of other effects</td>
<td>134</td>
</tr>
<tr>
<td>8.5</td>
<td>Separating out the vector component</td>
<td>136</td>
</tr>
<tr>
<td colspan="2">Functional linear models</td>
<td>139</td>
</tr>
<tr>
<td>9.1</td>
<td>Introduction</td>
<td>139</td>
</tr>
<tr>
<td>9.2</td>
<td>Functional linear models and functional ANOVA</td>
<td>140</td>
</tr>
<tr>
<td></td>
<td>9.2.1 Fitting the model</td>
<td>141</td>
</tr>
<tr>
<td></td>
<td>9.2.2 Assessing the fit</td>
<td>142</td>
</tr>
<tr>
<td>9.3</td>
<td>Force plate data for walking horses</td>
<td>145</td>
</tr>
<tr>
<td></td>
<td>9.3.1 Structure of the data</td>
<td>145</td>
</tr>
<tr>
<td></td>
<td>9.3.2 A functional linear model for the horse data</td>
<td>147</td>
</tr>
<tr>
<td></td>
<td>9.3.3 Effects and contrasts</td>
<td>149</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th></th>
<th>Contents</th>
<th>xi</th>
</tr>
<tr>
<td>9.4 Computational issues</td>
<td></td>
<td>152</td>
</tr>
<tr>
<td>9.4.1 The general model</td>
<td></td>
<td>152</td>
</tr>
<tr>
<td>9.4.2 Pointwise minimization</td>
<td></td>
<td>153</td>
</tr>
<tr>
<td>9.4.3 Using basis expansions</td>
<td></td>
<td>153</td>
</tr>
<tr>
<td>9.4.4 Incorporating regularization</td>
<td></td>
<td>154</td>
</tr>
<tr>
<td>9.5 General structure</td>
<td></td>
<td>155</td>
</tr>
<tr>
<td>10 Functional linear models for scalar responses</td>
<td></td>
<td>157</td>
</tr>
<tr>
<td>10.1 Introduction: Functions as predictors</td>
<td></td>
<td>157</td>
</tr>
<tr>
<td>10.2 A naïve approach: Functional interpolation</td>
<td></td>
<td>158</td>
</tr>
<tr>
<td>10.3 Regularization by discretizing the function</td>
<td></td>
<td>160</td>
</tr>
<tr>
<td>10.4 Regularization using basis functions</td>
<td></td>
<td>161</td>
</tr>
<tr>
<td>10.4.1 Re-expressing the model and data</td>
<td></td>
<td>161</td>
</tr>
<tr>
<td>10.4.2 Smoothing by basis truncation</td>
<td></td>
<td>162</td>
</tr>
<tr>
<td>10.4.3 Re-expressions with other bases</td>
<td></td>
<td>163</td>
</tr>
<tr>
<td>10.5 Regularization with roughness penalties</td>
<td></td>
<td>164</td>
</tr>
<tr>
<td>10.5.1 Penalizing the residual sum of squares</td>
<td></td>
<td>164</td>
</tr>
<tr>
<td>10.5.2 Connections with nonparametric regression</td>
<td></td>
<td>166</td>
</tr>
<tr>
<td>10.6 Computational aspects of regularization</td>
<td></td>
<td>168</td>
</tr>
<tr>
<td>10.6.1 Direct discretization and calculation</td>
<td></td>
<td>169</td>
</tr>
<tr>
<td>10.6.2 Full basis expansion</td>
<td></td>
<td>169</td>
</tr>
<tr>
<td>10.6.3 Restricting the basis expansion</td>
<td></td>
<td>170</td>
</tr>
<tr>
<td>10.7 The direct penalty method for computing B</td>
<td></td>
<td>170</td>
</tr>
<tr>
<td>10.7.1 Functional interpolation</td>
<td></td>
<td>170</td>
</tr>
<tr>
<td>10.7.2 The two-stage minimization process</td>
<td></td>
<td>171</td>
</tr>
<tr>
<td>10.7.3 Functional interpolation revisited</td>
<td></td>
<td>172</td>
</tr>
<tr>
<td>10.8 Cross-validation and regression diagnostics</td>
<td></td>
<td>174</td>
</tr>
<tr>
<td>10.9 Functional regression and integral equations</td>
<td></td>
<td>176</td>
</tr>
<tr>
<td>11 Functional linear models for functional responses</td>
<td></td>
<td>179</td>
</tr>
<tr>
<td>11.1 Introduction</td>
<td></td>
<td>179</td>
</tr>
<tr>
<td>11.2 Estimating $\beta$ by basis representations</td>
<td></td>
<td>180</td>
</tr>
<tr>
<td>11.3 Fitting the model by basis expansions</td>
<td></td>
<td>181</td>
</tr>
<tr>
<td>11.3.1 Some linear algebra preliminaries</td>
<td></td>
<td>181</td>
</tr>
<tr>
<td>11.3.2 Fitting the model without regularization</td>
<td></td>
<td>183</td>
</tr>
<tr>
<td>11.4 Regularizing the fit</td>
<td></td>
<td>184</td>
</tr>
<tr>
<td>11.4.1 Restricting the basis of the predictor</td>
<td>variable</td>
<td>184</td>
</tr>
<tr>
<td>11.4.2 Restricting the basis of the response</td>
<td>variable</td>
<td>185</td>
</tr>
<tr>
<td>11.4.3 Restricting both bases</td>
<td></td>
<td>187</td>
</tr>
<tr>
<td>11.5 Assessing goodness of fit</td>
<td></td>
<td>189</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="xii Contents" -->

11.6 Bivariate roughness penalties for B

193

11.7 Other linear models for functional data

194

11.7.1 More complicated covariate structures

194

11.7.2 The pointwise multivariate model

195

11.7.3 Spline smoothing and other evaluation models
195

11.7.4 Weighted and partial integral models
197


### 12 Canonical correlation and discriminant analysis 199

12.1 Introduction
199

12.1.1 The basic problem
199

12.1.2 Principles of classical CCA

200

12.1.3 The analysis as an eigenvalue problem

200

12.1.4 Subsidiary variates and their properties

201

201

12.1.5 CCA and the generalized eigenproblem

12.2 Functional canonical correlation analysis
202

12.2.1 Notation and assumptions

203

12.2.2 Estimating the leading canonical variates

205

202

12.2.3 Cross-validation and subsidiary variates

205

12.3 Application to the gait data

12.4 Application to the study of lupus nephritis

208

12.5 Why is regularization necessary?

210

12.6 Algorithmic considerations

211

12.6.1 Discretization and basis approaches
211

12.6.2 The roughness of the canonical variates
213

12.7 Penalized optimal scoring and discriminant analysis

214

12.7.1 The optimal scoring problem

214

12.7.2 The discriminant problem

215

12.7.3 The relationship with CCA

215

12.7.4 Applications
216


### 13 Differential operators in functional data analysis 217

13.1 Introduction
217

13.2 Two sets of data

218

13.2.1 The gross domestic product data

218

13.2.2 The melanoma data

219

13.3 Some roles for linear differential operators

220

13.3.1 Producing new functional observations

13.3.2 Regularizing or smoothing models

220

221

13.3.3 Partitioning variation

223

13.3.4 Defining solutions to problems

225

<!-- PageBreak -->


<table>
<tr>
<th></th>
<th>Contents</th>
<th>xiii</th>
</tr>
<tr>
<td>13.4 Some linear differential equation facts</td>
<td></td>
<td>227</td>
</tr>
<tr>
<td>13.4.1 Derivatives are rougher</td>
<td></td>
<td>227</td>
</tr>
<tr>
<td>13.4.2 Finding a LDO that annihilates known</td>
<td>functions</td>
<td>228</td>
</tr>
<tr>
<td>13.4.3 Finding the functions satisfying</td>
<td></td>
<td>230</td>
</tr>
<tr>
<td>13.5 Constraint functionals $B \quad \ldots .$</td>
<td></td>
<td>231</td>
</tr>
<tr>
<td>13.5.1 Some constraint examples</td>
<td></td>
<td>231</td>
</tr>
<tr>
<td>13.5.2 How $L$ and $B$ partition functions</td>
<td></td>
<td>232</td>
</tr>
<tr>
<td>13.5.3 Inner product defined by operators</td>
<td>and</td>
<td>233</td>
</tr>
<tr>
<td>13.6 The Green's function for $L$ and $B$</td>
<td></td>
<td>234</td>
</tr>
<tr>
<td>13.6.1 Solving a linear differential equation</td>
<td></td>
<td>234</td>
</tr>
<tr>
<td>13.6.2 The Green's function and the solution</td>
<td></td>
<td>235</td>
</tr>
<tr>
<td>13.6.3 A recipe for the Green's function</td>
<td></td>
<td>236</td>
</tr>
<tr>
<td>13.7 Reproducing kernels and Green's functions</td>
<td></td>
<td>237</td>
</tr>
<tr>
<td>13.7.1 The reproducing kernel for ker B</td>
<td></td>
<td>237</td>
</tr>
<tr>
<td>13.7.2 The reproducing kernel for ker L</td>
<td></td>
<td>238</td>
</tr>
<tr>
<td>14 Principal differential analysis</td>
<td></td>
<td>239</td>
</tr>
<tr>
<td>14.1 Introduction</td>
<td></td>
<td>239</td>
</tr>
<tr>
<td>14.1.1 The basic principle</td>
<td></td>
<td>239</td>
</tr>
<tr>
<td>14.1.2 The need for PDA</td>
<td></td>
<td>240</td>
</tr>
<tr>
<td>14.1.3 The relationship to PCA</td>
<td></td>
<td>242</td>
</tr>
<tr>
<td>14.1.4 Visualizing results</td>
<td></td>
<td>246</td>
</tr>
<tr>
<td>14.2 PDA techniques</td>
<td></td>
<td>247</td>
</tr>
<tr>
<td>14.2.1 PDA by pointwise minimization</td>
<td></td>
<td>248</td>
</tr>
<tr>
<td>14.2.2 PDA by basis expansions</td>
<td></td>
<td>249</td>
</tr>
<tr>
<td>14.2.3 Regularized PDA</td>
<td></td>
<td>251</td>
</tr>
<tr>
<td>14.2.4 Assessing fit</td>
<td></td>
<td>251</td>
</tr>
<tr>
<td>14.3 PDA of the pinch force data</td>
<td></td>
<td>252</td>
</tr>
<tr>
<td>15 More general roughness penalties</td>
<td></td>
<td>257</td>
</tr>
<tr>
<td>15.1 Introduction</td>
<td></td>
<td>257</td>
</tr>
<tr>
<td>15.1.1 General roughness penalties and L-splines</td>
<td></td>
<td>257</td>
</tr>
<tr>
<td>15.1.2 The lip movement data</td>
<td></td>
<td>258</td>
</tr>
<tr>
<td>15.1.3 The weather data</td>
<td></td>
<td>259</td>
</tr>
<tr>
<td>15.2 The optimal basis for spline smoothing</td>
<td></td>
<td>261</td>
</tr>
<tr>
<td>15.3 An $O \left( n \right)$ algorithm for L-spline smoothing</td>
<td></td>
<td>263</td>
</tr>
<tr>
<td>15.3.1 The need for a good algorithm</td>
<td></td>
<td>263</td>
</tr>
<tr>
<td>15.3.2 Setting up the smoothing procedure</td>
<td></td>
<td>264</td>
</tr>
<tr>
<td>15.3.3 The smoothing phase</td>
<td></td>
<td>265</td>
</tr>
<tr>
<td>15.3.4 The performance assessment phase</td>
<td></td>
<td>266</td>
</tr>
<tr>
<td>15.3.5 Other $O \left( n \right)$ algorithms</td>
<td></td>
<td>267</td>
</tr>
<tr>
<td>15.4 A compact support basis for L-splines</td>
<td></td>
<td>268</td>
</tr>
</table>


<!-- PageBreak -->


### xiv Contents


<table>
<tr>
<td colspan="2">15.5 Some case studies</td>
<td>269</td>
</tr>
<tr>
<td></td>
<td>15.5.1 The gross domestic product data</td>
<td>269</td>
</tr>
<tr>
<td></td>
<td>15.5.2 The melanoma data</td>
<td>271</td>
</tr>
<tr>
<td></td>
<td>15.5.3 GDP data with seasonal effects</td>
<td>271</td>
</tr>
<tr>
<td></td>
<td>15.5.4 Smoothing simulated human growth data</td>
<td>273</td>
</tr>
<tr>
<td colspan="2">16 Some perspectives on FDA</td>
<td>277</td>
</tr>
<tr>
<td>16.1</td>
<td>The context of functional data analysis</td>
<td>277</td>
</tr>
<tr>
<td></td>
<td>16.1.1 Replication and regularity</td>
<td>277</td>
</tr>
<tr>
<td></td>
<td>16.1.2 Some functional aspects elsewhere in statistics</td>
<td>278</td>
</tr>
<tr>
<td></td>
<td>16.1.3 Uses of derivative information</td>
<td>279</td>
</tr>
<tr>
<td></td>
<td>16.1.4 Functional analytic treatments</td>
<td>280</td>
</tr>
<tr>
<td colspan="2">16.2 Challenges for the future</td>
<td>281</td>
</tr>
<tr>
<td></td>
<td>16.2.1 Probability and inference</td>
<td>281</td>
</tr>
<tr>
<td></td>
<td>16.2.2 Asymptotic results</td>
<td>282</td>
</tr>
<tr>
<td></td>
<td>16.2.3 Multidimensional arguments</td>
<td>282</td>
</tr>
<tr>
<td></td>
<td>16.2.4 Practical methodology and applications</td>
<td>282</td>
</tr>
<tr>
<td></td>
<td>16.2.5 Back to the data!</td>
<td>283</td>
</tr>
<tr>
<td colspan="2">Appendix: Some algebraic and functional techniques</td>
<td>285</td>
</tr>
<tr>
<td>A.1</td>
<td>Matrix decompositions and generalized inverses</td>
<td>285</td>
</tr>
<tr>
<td></td>
<td>A.1.1 Singular value decompositions</td>
<td>285</td>
</tr>
<tr>
<td></td>
<td>A.1.2 Generalized inverses</td>
<td>286</td>
</tr>
<tr>
<td></td>
<td>A.1.3 The QR decomposition</td>
<td>287</td>
</tr>
<tr>
<td>A.2</td>
<td>Projections</td>
<td>287</td>
</tr>
<tr>
<td></td>
<td>A.2.1 Projection matrices</td>
<td>287</td>
</tr>
<tr>
<td></td>
<td>A.2.2 Finding an appropriate projection matrix</td>
<td>288</td>
</tr>
<tr>
<td></td>
<td>A.2.3 More general inner product spaces</td>
<td>288</td>
</tr>
<tr>
<td>A.3</td>
<td>Constrained maximization of a quadratic function</td>
<td>289</td>
</tr>
<tr>
<td></td>
<td>A.3.1 The finite-dimensional case</td>
<td>289</td>
</tr>
<tr>
<td></td>
<td>A.3.2 The problem in a more general space</td>
<td>290</td>
</tr>
<tr>
<td></td>
<td>A.3.3 Generalized eigenproblems</td>
<td>291</td>
</tr>
<tr>
<td colspan="2">References</td>
<td>293</td>
</tr>
<tr>
<td colspan="2">Index</td>
<td>303</td>
</tr>
</table>


<!-- PageBreak -->


## 1 Introduction


### 1.1 What are functional data?

Figure 1.1 provides a prototype for the type of data that we shall
consider. It shows the heights of 10 Swiss boys measured at a set of
29 ages in the Zurich Longitudinal Growth Study (Falkner, 1960). The
ages are not equally spaced; there are annual measurements from two
to 10 years, followed by biannually measured heights. Although great
care was taken in the measurement process, there is an uncertainty
or noise in height values with a standard deviation of about 5 mm.
Even though each record involves only 29 discrete values, these values
reflect a smooth variation in height that could be assessed, in principle,
as often as desired, and is therefore a height function. Thus, the data
consist of a sample of 10 functional observations $\mathrm { H e i g h t } _ { i } \left( t \right) .$

Moreover, there are features in this data too subtle to see in this type
of plot. For example, Gasser et al. (1984) detected a growth spurt prior
to puberty using some delicate and powerful data analysis tools. Figure
1.2 displays the acceleration curves $D ^ { 2 } \text { Height } _ { i } ,$ estimated from these
data by Ramsay, Bock and Gasser (1995) using a technique discussed
in Chapter 4. We use the notation $D$ for differentiation, as in

$$D ^ { 2 } \text { Height } = \frac { d ^ { 2 } \text { Height } } { d t ^ { 2 } }$$

<!-- PageBreak -->

<!-- PageNumber="2" -->
<!-- PageHeader="1. Introduction" -->


<figure>
<figcaption>FIGURE 1.1. The heights of 10 Swiss boys measured at 29 ages. The points indicate the unequally spaced ages of measurement.</figcaption>

200

Height (cm)

150

100

0

5

10

15

20

Age

</figure>


<figure>
<figcaption>FIGURE 1.2. The estimated accelerations of height for 10 Swiss boys, measured in centimetres per year per year. The heavy dashed line is the cross-sectional mean, and is a rather poor summary of the curves.</figcaption>

4

2

Height acceleration

0

-2

\+

-6

4

6

8

10

12

14

16

18

Age

</figure>


<!-- PageBreak -->

<!-- PageNumber="3" -->
<!-- PageHeader="1.2 Some functional data analyses" -->

In Figure 1.2 the pubertal growth spurt shows up as a pulse of strong
positive acceleration followed by sharp negative deceleration. But most
records also show a bump at around six years that is termed the mid-
spurt. We conclude that the variation from curve to curve can also be
profitably explained at the level of certain derivatives. The fact that
derivatives are of interest is further reason to think of the records as
functions, rather than vectors of observations in discrete time.

The ages themselves must also play an explicit role in our analysis,
because they are not equally spaced. Although it might be mildly
interesting to correlate heights at ages 9, 10 and 10.5, this would not
take account of the fact that we fully expect the correlation for two ages
separated by only half a year to be higher than that for a separation of
one year. Indeed, although in this particular example the ages at which
the observations are taken are nominally the same for each boy, there
is no real need for this to be so; in general, the points at which the
functions are observed may well vary from one record to another.

The replication of these height curves invites an exploration of the
ways in which the curves vary. This is potentially complex. For example,
the rapid growth during puberty is visible in all curves, but both the
timing and the intensity of pubertal growth differ from boy to boy.
Some type of principal components analysis would undoubtedly be
helpful, but we must adapt the procedure to take account of the
unequal age spacing and the smoothness of the underlying height
functions. One objective might be to separate variation in timing of
significant growth events, such as the pubertal growth spurt, from
variation in the intensity of growth.


### 1.2 Some functional data analyses

Data in many different fields come to us through a process naturally
described as functional. To turn to a completely different context,
consider Figure 1.3, where the mean monthly temperatures for four
Canadian weather stations are plotted. It also shows estimates of the
corresponding smooth temperature functions presumed to generate
the observations. Montreal, with the warmest summer temperature, has
a temperature pattern that appears to be nicely sinusoidal. Edmonton,
with the next warmest summer temperature, seems to have some
distinctive departures from sinusoidal variation that call for some
explanation. The marine climate of Prince Rupert is evident in the small
amount of annual variation in temperature, and Resolute has bitterly
cold but strongly sinusoidal temperature.

<!-- PageBreak -->

<!-- PageHeader="4 1. Introduction" -->


<figure>
<figcaption>FIGURE 1.3. Mean monthly temperatures for the Canadian weather stations. In descending order of the temperatures at the start of the year, the stations are Prince Rupert, Montreal, Edmonton, and Resolute.</figcaption>

Mean temperature (deg C)

-40 -30 -20 -10 0 10 20

0

2

4 6 8 10 1

12

Month

</figure>


One expects temperature to be primarily sinusoidal in character,
and certainly periodic over the annual cycle. There is some variation
in phase, because the coldest day of the year seems to be later in
Edmonton and Resolute. Consequently, a model of the form

$$\mathrm { T e m p } _ { i } \left( t \right) \approx c _ { i 1 } + c _ { i 2 } \sin \left( \pi t / 6 \right) + c _ { i 3 } \cos \left( \pi t / 6 \right)$$
(1.1)

should do rather nicely for these data, where $\mathrm { T e m p } _ { i }$ is the temperature
function for the $i$ ith weather station, and $\left( c _ { i 1 } , c _ { i 2 } , c _ { i 3 } \right)$ is a vector of three
parameters associated with that station.

In fact, there are clear departures from sinusoidal or simple harmonic
behaviour. One way to see this is to compute the function

$$= \left( \pi / 6 \right) ^ { 2 } D T e m p + D ^ { 3 } T e m p .$$

As we have already noted in Section 1.1, the notation $D ^ { m } \mathrm { T e m p }$
means "take the mth derivative of function Temp," and the notation
LTemp stands for the function which results from applying the linear
differential operator $L = \left( \pi / 6 \right) ^ { 2 } D + D ^ { 3 }$ to the function Temp. The
resulting function, LTemp, is often called a forcing function. Now, if $a$
temperature function is truly sinusoidal, then LTemp should be exactly
zero, as it would be for any function of the form (1.1). That is, it would
satisfy the homogeneous differential equation $L T e m p = 0 .$

<!-- PageBreak -->

<!-- PageNumber="5" -->
<!-- PageHeader="1.2 Some functional data analyses" -->


<figure>
<figcaption>FIGURE 1.4. The result of applying the differential operator $L = \left( \pi / 6 \right) ^ { 2 } D + D ^ { 3 }$ to the estimated temperature functions in Figure 1.3. If the variation in temperature were purely sinusoidal, these curves would be exactly zero.</figcaption>

20

L-Temperature

10

0

-10

-20

0

5

Month

10

15

</figure>


But Figure 1.4 indicates that the functions $L T e m p _ { i }$ display systematic
features that are especially strong in the spring and autumn months.
Put another way, temperature at a particular weather station can be
described as the solution of the nonhomogeneous differential equation
$L \mathrm { T e m p } = u ,$ where the forcing function $u$ can be viewed as input
from outside of the system, or an exogenous influence. Meteorologists
suggest, for example, that these spring and autumn effects are partly
due to the change in the reflectance of land when snow or ice melts,
and this would be consistent with the fact that the least sinusoidal
records are associated with continental stations well separated from
large bodies of water.

Here, the point is that we may often find it interesting to remove
effects of a simple character by applying a differential operator, rather
than simply subtracting them. This exploits the intrinsic smoothness
in the process, and long experience in the natural and engineering
sciences suggests that this may get closer to the underlying driving
forces at work than just adding and subtracting effects, as one routinely
does in multivariate data analysis.

Functional data are often multivariate in a different sense. Our third
example is in Figure 1.5. The Motion Analysis Laboratory at Children's

<!-- PageBreak -->

<!-- PageNumber="6" -->
<!-- PageHeader="1. Introduction" -->


<figure>
<figcaption>FIGURE 1.5. The angles in the sagittal plane formed by the hip and by the knee as 39 children go through a gait cycle. The interval $\left[ 0 , 1 \right]$ is a single cycle, and the dotted curves show the periodic extension of the data beyond either end of the cycle.</figcaption>

Hip angle (degrees)

60

40

20

0

0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2

Knee angle (degrees)

80

60

40

20

O

-0.2

0,0

0 0.2 0.4 0.6 0.8 1.0

1.2

Time (proportion of gait cycle)

</figure>


Hospital, San Diego, collected these data, which consist of the angles
formed by the hip and knee of each of 39 children over each child's
gait cycle. See Olshen et al. (1989) for full details. Time is measured
in terms of the individual gait cycle, so that every curve is given for
values of $t$ in $\left[ 0 , 1 \right] .$ The cycle begins and ends at the point where
the heel of the limb under observation strikes the ground. Both sets
of functions are periodic, and are plotted as dotted curves somewhat
beyond the interval for clarity. We see that the knee shows a two-phase
process, while the hip motion is single-phase. What is harder to see
is how the two joints interact; of course the figure does not indicate
which hip curve is paired with which knee curve, and among many other
things this example demonstrates the need for graphical ingenuity in
functional data analysis.

Figure 1.6 shows the gait cycle for a single child by plotting knee
angle against hip angle as time progresses round the cycle. The periodic
nature of the process implies that this forms a closed curve. Also shown
for reference purposes is the same relationship for the average across
the 39 children. Now we see an interesting feature: a cusp occurring

<!-- PageBreak -->

<!-- PageNumber="7" -->
<!-- PageHeader="1.2 Some functional data analyses" -->


<figure>
<figcaption>FIGURE 1.6. Solid line: The angles in the sagittal plane formed by the hip and by the knee for a single child plotted against each other. Dotted line: The corresponding plot for the average across children. The points indicate 20 equally spaced time points in the gait cycle, and the letters are plotted at intervals of one-fifth of the cycle, with A marking the heel strike.</figcaption>

80

Knee angle (degrees)

E

60

E

40

D

20

E

A

0

0

20

40

60

Hip angle (degrees)

</figure>


at the heel strike. The angular velocity is clearly visible in terms of
the spacing between numbers, and it varies considerably as the cycle
proceeds. The child whose gait is represented by the solid curve differs
from the average in two principal ways. First, the portion of the gait
pattern in the C-D part of the cycle shows an exaggeration of movement
relative to the average, and second, in the part of the cycle where the hip
is most bent, the amount by which the hip is bent is markedly less than
average; interestingly, this is not accompanied by any strong effect on
the knee angle. The overall shape of the cycle for the particular child
is rather different from the average. The exploration of variability in
these functional data must focus on features such as these.

Finally, in this introduction to types of functional data, we must not
forget that they may come to our attention as full-blown functions, so
that each record may consist of functions observed, for all practical
purposes, everywhere. Sophisticated on-line sensing and monitoring
equipment is now routinely used in research in medicine, seismology,
meteorology, physiology, and many other fields.

<!-- PageBreak -->

<!-- PageHeader="8 1. Introduction" -->


### 1.3 The goals of functional data analysis

The goals of functional data analysis are essentially the same as those
of any other branch of statistics. They include the following aims:

· to represent the data in ways that aid further analysis

· to display the data so as to highlight various characteristics

· to study important sources of pattern and variation among the
data

· to explain variation in an outcome or dependent variable by using
input or independent variable information

· to compare two or more sets of data with respect to certain types
of variation, where two sets of data can contain different sets
of replicates of the same functions, or different functions for a
common set of replicates.

Subsequent chapters explore each of these themes, and they are
introduced only briefly here.

Each of these activities can be conducted with techniques appropriate
to certain goals. Another way to characterize the strategy in a data
analysis is as exploratory, confirmatory, or predictive. In exploratory
mode, the questions put to the data tend to be rather open-ended
in the sense that one expects the right technique to reveal new and
interesting aspects of the data, as well as to shed to light on known
and obvious features. Exploratory investigations tend to consider only
the data at hand, with less concern for statements about larger issues
such as characteristics of populations or events not observed in the
data. Confirmatory analyses, on the other hand, tend to be inferential
and to be determined by specific questions about the data. Some type of
structure is assumed to be present in the data, and one wants to know
whether certain specific statements or hypotheses can be considered
confirmed by the data. The dividing line between exploratory and
confirmatory analyses tends to be the extent to which probability
theory is used, in the sense that most confirmatory analyses are
summarized by one or more probability statements. Predictive studies
are somewhat less common, and focus on using the data at hand to
make a statement about unobserved states, such as the future.

This book develops techniques that are mainly exploratory in nature.
The theory of probability associated with functional events is generally
regarded as an advanced topic, and might be seen by many readers
as inaccessibly technical. Nevertheless, some simple hypothesis tests

<!-- PageBreak -->

$$1 . 4 \quad F i r s t \quad s t e p s \quad i n \quad a \quad f u n c t i o n a l \quad d a t a \quad a n a l y s i s$$

are certainly possible, and are mentioned here and there. In general,
prediction is beyond our scope.


### 1.4 First steps in a functional data analysis


#### 1.4.1 Data representation: smoothing and interpolation

Assuming that a functional datum for replication $i$ arrives as a set
of discrete measured values, $\mathcal{Y} _ { i 1 } , \ldots , \mathcal{Y} _ { i n } ,$ the first task is to convert
these values to a function $x _ { i }$ with values $x _ { i } \left( t \right)$ computable for any
desired argument value $t .$ If the discrete values are assumed to be
errorless, then the process is interpolation, but if they have some
observational error that needs removing, then the conversion from
discrete data to functions may involve smoothing. Chapters 3 and 4
offer a survey of these procedures. The roughness penalty smoothing
method discussed in Chapter 4 will be used much more broadly in many
contexts throughout the book, not merely for the purpose of estimating
a function from a set of observed values.

The gait data in Figure 1.5 were converted to functions by the
simplest of interpolation schemes: joining each pair of adjacent
observations by a straight line segment. This approach would be
inadequate if we require derivative information. However, one might
perform a certain amount of smoothing while still respecting the
periodicity of the data by fitting a Fourier series to each record: A
constant plus three pairs of sine and cosine terms does a reasonable job
for these data. The growth data in Figure 1.1 and the temperature data
in Figure 1.3 were smoothed using polynomial smoothing splines, and
this more sophisticated technique also provides high quality derivative
information.


#### 1.4.2 Data registration or feature alignment

Figure 1.7 shows some biomechanical data. The curves in the figure are
twenty records of the force exerted on a meter during a brief pinch
by the thumb and forefinger. The subject was required to maintain a
certain background force on a force meter and then to squeeze the
meter aiming at a specified maximum value, returning afterwards to
the background level. The purpose of the experiment was to study
the neurophysiology of the thumb-forefinger muscle group. The data
were collected at the MRC Applied Psychology Unit, Cambridge, by
R. Flanagan; see Ramsay, Wang and Flanagan (1995).

<!-- PageBreak -->

<!-- PageNumber="10" -->
<!-- PageHeader="1. Introduction" -->


<figure>
<figcaption>FIGURE 1.7. Twenty recordings of the force exerted by the thumb and forefinger where a constant background force of two newtons was maintained prior to a brief impulse targeted to reach 10 newtons. Force was sampled 500 times per second.</figcaption>

12

10

8

Force (N)

9

4

2

0

0.0

0.05

0.10

0.15

0.20

0.25

0.30

Seconds

</figure>


These data illustrate a common problem in functional data analysis.
The start of the pinch is located arbitrarily in time, and a first step is to
align the records by some shift of the time axis. In Chapter 5 we take
up the question of how to estimate this shift, and how to go further
if necessary to estimate record-specific linear transformations of the
argument, or even nonlinear transformations.


#### 1.4.3 Data display

Displaying the results of a functional data analysis can be a challenge. of
the gait data in Figures 1.5 and 1.6, we have already seen that different
displays of data can bring out different features of interest, and that the
standard plot of $x \left( t \right)$ against $t$ is not necessarily the most informative.
It is impossible to be prescriptive about the best type of plot for a given
set of data or procedure, but we shall give illustrations of various ways
of plotting the results. These are intended to stimulate the reader's
imagination rather than to lay down rigid rules.

The methods we use do not include such sophistications as three (or
more) dimensional displays produced by rotating a structure in more
than two dimensions. Instead, we have confined ourselves to plots that

<!-- PageBreak -->

<!-- PageNumber="11" -->
<!-- PageHeader="1.5 Summary statistics for functional data" -->

can easily be produced in the statistical package S-PLUS (Statistical
Sciences, 1995), which we have used as the platform for virtually
all our analyses. More sophisticated displays can be informative, but
they are inaccessible to printed media. Nevertheless, the use of such
techniques in functional data display and analysis is an interesting
topic for research.


### 1.5 Summary statistics for functional data


#### 1.5.1 Mean and variance functions

The classical summary statistics for univariate data familiar to students
in introductory statistics classes apply equally to functional data. The
mean function with values

$$\bar { x } \left( t \right) = N ^ { - 1 } \sum _ { i = 1 } ^ { N } x _ { i } \left( t \right)$$

is the average of the functions pointwise across replications. Similarly
the variance function var has values

$$\mathrm { v a r } _ { X } \left( t \right) = \left( N - 1 \right) ^ { - 1 } \sum _ { i = 1 } ^ { N } \left[ x _ { i } \left( t \right) - \bar { x } \left( t \right) \right] ^ { 2 } ,$$

and the standard deviation function is the square root of the variance
function.

Figure 1.8 displays the mean and standard deviation functions
for the aligned pinch force data. We see that the mean force
looks remarkably like a number of probability density functions well
known to statisticians, and in fact the relationship to the lognormal
distribution has been explored by Ramsay, Wang and Flanagan (1995).
The standard deviation of force seems to be about 8% of the mean force
over most of the range of the data.


#### 1.5.2 Covariance and correlation functions

The covariance function summarizes the dependence of records across
different argument values, and is computed for all $t _ { 1 }$ and $t _ { 2 }$ by

$$\mathrm { c o v } _ { X } \left( t _ { 1 } , t _ { 2 } \right) = \left( N - 1 \right) ^ { - 1 } \sum _ { i = 1 } ^ { N } \left\{ x _ { i } \left( t _ { 1 } \right) - x \left( t _ { 1 } \right) \right\} \left\{ x _ { i } \left( t _ { 2 } \right) - x \left( t _ { 2 } \right) \right\} .$$

<!-- PageBreak -->

<!-- PageNumber="12" -->
<!-- PageHeader="1. Introduction" -->


<figure>
<figcaption>FIGURE 1.8. The mean and standard deviation functions for the 20 pinch force observations in Figure 1.7 after they were aligned or registered.</figcaption>

Force mean (N)

0 2 4 6 8 10 12

Force Std. Dev. (N)

0.0 0.2 0.4 0.6 0.8 1.0

0.0

0.10

0.20

0.30

0.0

0.10

0.20

0.30

Time (sec)

Time (sec)

</figure>


The associated correlation function is

$$\mathrm { c o r r } _ { X } \left( t _ { 1 } , t _ { 2 } \right) = \frac { \mathrm { c o v } _ { X } \left( t _ { 1 } , t _ { 2 } \right) } { \sqrt { \mathrm { v a r } _ { X } \left( t _ { 1 } \right) \mathrm { v a r } _ { X } \left( t _ { 2 } \right) } }$$ ☒

These are the functional analogues of the variance-covariance and
correlation matrices, respectively, in multivariate data analysis.

Figure 1.9 displays the correlation function of the pinch force data,
both as a surface over the plane of possible pairs of times $\left( t _ { 1 } , t _ { 2 } \right)$ and
also as a set of level contours.

Our experience with perspective and contour displays of correlation
suggests that not everyone encountering them for the first time finds
them easy to understand. Here is one strategy: The diagonal running
from lower left to upper right in the contour or from front to back in
the perspective plot of the surface contains the unit values that are
the correlations between identical or very close time values. Directions
perpendicular to this ridge of unit correlation indicate how rapidly the
correlation falls off as two argument values separate. For example, one
might locate a position along the unit ridge associated with argument
value $t ,$ and then moving perpendicularly from this point shows what
happens to the correlation between values at time pair $\left( t - \delta , t + \delta \right)$
as the perpendicular distance $\delta$ increases. In the case of the pinch
force data, we note that the correlation falls off slowly for values on
either side of the time 0.1 of maximum force, but declines much more
rapidly in the periods before and after the impulse. This suggests a
two-phase system, with fairly erratic uncoupled forces in the constant
background force phase, but with tightly connected forces during the

<!-- PageBreak -->

<!-- PageNumber="13" -->
<!-- PageHeader="1.5 Summary statistics for functional data" -->


<figure>
<figcaption>FIGURE 1.9. The left panel is a perspective plot of the bivariate correlation function values $r \left( t _ { 1 } , t _ { 2 } \right)$ for the pinch force data. The right panel shows the same surface by contour plotting. Time is measured in seconds.</figcaption>

0.05 0.10 0.15 0.20 0.25

0.6

00,0:4 8.6 0.8, 1

0.9 0.4

b:8.6

2

Corr.

0.4

0

D.2

012

T

0

1

0.2

$0 . 2 \_ 0 . 1$

11

0

£2

0:4

0:6

0.4

0.2

10.8.60042

0 10.6

0,1

Time

0.05 0.10 0.15 0.20 0.25
Time

</figure>


actual impulse. In fact, it is common to observe low correlations or
rapid fall-off when a system is in a resting or ballistic state free from
any outside input, but to show strong correlations, either positive and
negative, when exogenous influences apply.


#### 1.5.3 Cross-covariance and cross-correlation functions

In the case of the gait data discussed in Section 1.2, we had both hip
and knee angles measured through time. In general, if we have pairs
of observed functions $\left( x _ { i } , y _ { i } \right) ,$ the way in which these depend on one
another can be quantified by the cross-covariance function

$$\mathrm { c o v } _ { X , Y } \left( t _ { 1 } , t _ { 2 } \right) = \left( N - 1 \right) ^ { - 1 } \sum _ { i = 1 } ^ { N } \left\{ x _ { i } \left( t _ { 1 } \right) - x \left( t _ { 1 } \right) \right\} \left\{ y _ { i } \left( t _ { 2 } \right) - y \left( t _ { 2 } \right) \right\} .$$

or the cross-correlation function

$$\mathrm { c o r r } _ { X , Y } \left( t _ { 1 } , t _ { 2 } \right) = \frac { \mathrm { c o v } _ { X , Y } \left( t _ { 1 } , t _ { 2 } \right) } { \sqrt { \mathrm { v a r } _ { X } \left( t _ { 1 } \right) \mathrm { v a r } _ { Y } \left( t _ { 2 } \right) } }$$ ☒

Figure 1.10 displays the correlation and cross-correlation functions
for the gait data. In each of the four panels, $t _ { 1 }$ is plotted along the
horizontal axis and $t _ { 2 }$ along the vertical axis. The top left panel shows
a contour plot of the correlation function $\left( t _ { 1 } , t _ { 2 } \right)$ for the hip
angles alone, and the bottom right panel shows the corresponding
plot for the knee angles. The cross-correlation functions corrHip,Knee

<!-- PageBreak -->

<!-- PageNumber="14" -->
<!-- PageHeader="1. Introduction" -->


<figure>
<figcaption>FIGURE 1.10. Contour plots of the correlation and cross-correlation functions for the gait data. In each panel $t _ { 1 }$ is plotted on one axis and $t _ { 2 }$ on the other; the legends indicate which observations are being correlated against each other.</figcaption>

0.0 0.2 0.4 0,6 0.8 1.0

0.8

0.6

0.6/8

0.0 0.2 0.4 0,6 0,8 1.0

1

0:4

0.2

0-2

1

0.2

$0$

(04

9:4

0

20,2

0,2

0,6

$\stackrel { \subseteq } { = }$

Knee

0:4

0

5

1111

$9 3 ^ { 4 }$

0.2

$\left. B \right) 6$

11

014

De4

0

0.8

0.6

0:60.8

04

0.2

0:204

8.4

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Hip

Hip

0,0 0.2 0.4 0.8 1.0

0:40:0/2

00.2

0.0 0.2 0.4 0.6 0.8 1.0

6:4

0.2

G:6

0.2

$\frac { 8 } { 3 }$

g

04

Knee

-0,2

0,2

0,6

0,4

0:4 0:0.2

0

0.20/2 0.

1.06 0.4 0.2 82 048

1

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Knee

Knee

</figure>


and corrknee, Hip are plotted in the top right and bottom left panels
respectively; since, in general, $\mathrm { c o r r } _ { X , Y } \left( t _ { 1 } , t _ { 2 } \right) = \mathrm { c o r r } _ { Y , X } \left( t _ { 2 } , t _ { 1 } \right) ,$ these
are transposes of one another, in that each is the reflection of the other
about the main diagonal $t _ { 1 } = t _ { 2 } .$ Note that each axis is labelled by the
generic name of relevant data function, Hip or Knee, rather than by the
argument value $t _ { 1 }$ or $t _ { 2 } .$

In this figure, different patterns of variability are demonstrated by
the individual correlation functions $c o r r _ { H i p }$ and corrknee for the
hip and knee angles considered separately. The hips show positive
correlation throughout, so that if the hip angle is larger than average
at one point in the cycle it will have a tendency to be larger than
average everywhere. The contours on this plot are more or less parallel
to the main diagonal, implying that the correlation is approximately
a function of $t _ { 1 } - t _ { 2 }$ and that the variation of the hip angles can be
considered as an approximately stationary process.

On the other hand, the knee angles show behaviour that is clearly
nonstationary; the correlation between the angle at time 0.0 and time
0.3 is about 0.4, while that between times 0.3 and 0.6 is actually
negative. In the middle of the cycle the correlation falls away rapidy
as one moves away from the main diagonal, while at the ends of the
cycle there is much longer range correlation. The hip angles show a

<!-- PageBreak -->

<!-- PageNumber="15" -->
<!-- PageHeader="1.5 Summary statistics for functional data" -->


<figure>
<figcaption>FIGURE 1.11. Contour plots of the correlation and cross-correlation functions for 35 Canadian weather stations for temperature and log precipitation. The cross-correlation functions are those in the upper right and lower left panels.</figcaption>

Temp.

Temp .- Prec.

2 4 10 12

2 4 6 8 10 12

0.8

0.6

$\bar { \aleph } \bar { \mathfrak{G} }$

0.9

<0.2

0.6

$T e m p$

Prec

0.2

0.4

0.8

0.6

0/6 0/8

2 4 6 8 10 12

2 4 6 8 10 12

Temp

Temp

Prec .- Temp.

Prec.

2 4 6 8 10 12

0.8 0.6.2

2 4 6 8 10 12

0.8

0,9

Temp

0.6

Prec

77777

0.8 0.00420/4 60.8

.31

0.998735

0.9

2 4 6 8 10 12

2 4 6 8 10 12

Prec

Prec

</figure>


slight, but much less marked, departure from stationarity of the same
kind. These features may be related to the greater effect on the knee of
external factors such as the heel strike and the associated weight placed
on the joint, whereas the hip acts under much more even muscular
control throughout the cycle.

The ridge along the main diagonal of the cross-correlation plots
indicates that $H i p \left( t _ { 1 } \right)$ and Knee(t2) are most strongly correlated when
$t _ { 1 }$ and $t _ { 2 }$ are approximately equal, though the main ridge shows a slight
reverse $\mathrm { S }$ shape (in the orientation of the top right panel). The analysis
developed in Chapter 12 will elucidate the delays in the dependence of
one joint on the other. Apart from this, there are differences in the way
that the cross-correlations behave at different points of the cycle, but
the cross-correlation function does not make it clear what these mean
in terms of dependence between the functions.

Another example is provided by the Canadian weather data. Contour
plotting in Figure 1.11 shows the correlation functions between
temperature and log precipitation based on monthly data. The
correlation is high for both temperature and precipitation on either
side of the midsummer period, so that autumn weather tends to be
highly correlated with spring weather. By contrast, winter and summer
weather have a weaker correlation of around 0.5. The cross-correlations

<!-- PageBreak -->


### 16 1. Introduction

show that midsummer precipitation has a near zero correlation with
temperature at any point in the year, but that midwinter temperature
and midwinter precipitation are highly correlated. This is due to the
fact that, in continental weather stations, both measures tend to be
especially low in midwinter, whereas in marine stations, the tendency
is for both temperature and precipitation to be higher.


### 1.6 Exploring variability in more detail

The examples considered so far give a glimpse of ways in which the
variability of a set of functional data is interesting, but there is a need
for more detailed and sophisticated ways of investigating variability,
and these are a major theme of this book.


#### 1.6.1 Functional principal components analysis

Most sets of data display a small number of dominant or substantial
modes of variation, even after subtracting the mean function from each
observation. An approach to identifying and exploring these, set out in
Chapter 6, is to adapt the classical multivariate procedure of principal
components analysis to functional data. In Chapter 7, techniques
of smoothing or regularization are incorporated into the functional
principal components analysis itself, thereby demonstrating that
smoothing methods have a far wider rôle in functional data analysis
than merely in the initial step of converting discrete observations
to functional form. In Chapter 8, we show that functional principal
components analysis can be made more selective and informative by
considering specific types of variation in a special way. For example,
we shall see that estimating a small shift of time for each temperature
record and studying its variation will give a clearer understanding of
record-to-record temperature variability.


#### 1.6.2 Functional linear modelling

The classical techniques of linear regression, analysis of variance, and
linear modelling all investigate the way in which variability in observed
data can be accounted for by other known or observed variables. They
can all be placed within the framework of the general linear model

$$y = Z \beta + \epsilon$$
(1.2)

<!-- PageBreak -->

<!-- PageNumber="17" -->
<!-- PageHeader="1.6 Exploring variability in more detail" -->

where, in the simplest case, $y$ is typically a vector of observations, $\beta$ is
a parameter vector, $Z$ is a matrix that defines a linear transformation
from parameter space to observation space, and $\epsilon$ is an error vector
with mean zero. The design matrix Z incorporates observed covariates
or independent variables.

To extend these ideas to the functional context, we retain the basic
structure (1.2) but allow more general interpretations of the symbols
within it. For example, we might ask of the Canadian weather data:

· If each weather station is broadly categorized as being Atlantic,
Pacific, Continental or Arctic, in what way does the geographical
category characterize the detailed temperature profile Temp and
account for the different profiles observed? In Chapter 9 we
introduce a functional analysis of variance methodology, where
both the parameters and the observations become functions, but
the matrix Z remains the same as in the classical multivariate case.

· Could a temperature record Temp be used to predict the logarithm
of total annual precipitation? In Chapter 10 we extend the idea of
linear regression to the case where the independent variable, or
covariate, is a function, but the response variable (log total annual
precipitation in this case) is not.

· Can the temperature record Temp be used as a predictor of the
entire precipitation profile, not merely the total precipitation?
This requires a fully functional linear model, where all the terms
in the model have more general form than in the classical case.
This topic is considered in Chapter 11.


#### 1.6.3 Functional canonical correlation

How do two or more sets of records covary or depend on one another?
As we saw in the cross-correlation plots, this is a question to pose for
gait data, because relationships between record-to-record variation in
hip angle and knee angle seem likely.

The functional linear modelling framework approaches this question
by considering one of the sets of functional observations as a covariate
and the other as a response variable, but in many cases, such as the gait
data, it does not seem reasonable to impose this kind of asymmetry,
and we shall develop two rather different methods that treat both
sets of variables in an even-handed way. One method, described in
Section 6.5, essentially treats the pair $\left( \mathrm { H i p } _ { i } , \mathrm { K n e e } _ { i } \right)$ as a single vector-
valued function, and then extends the functional principal components

<!-- PageBreak -->


### 18 1. Introduction

approach to perform an analysis. Chapter 12 takes another approach,
a functional version of canonical correlation analysis, identifying
components of variability in each of the two sets of observations which
are highly correlated with one another.

For many of the methods we discuss, a naïve approach extending
the classical multivariate method will usually give reasonable results,
though regularization will often improve these. However, when a linear
predictor is based on a functional observation, and also in functional
canonical correlation analysis, regularization is not an optional extra
but is an intrinsic and necessary part of the analysis; the reasons are
discussed in Chapters 10, 11 and 12.


### 1.7 Using derivatives in functional data analysis

In Section 1.2 we have already had a taste of the ways in which
derivatives and linear differential operators are useful in functional
data analysis. The use of derivatives is important both in extending the
range of simple graphical exploratory methods, and in the development
of more detailed methodology. This is a theme that will be explored in
much more detail in Chapters 13, 14 and 15, but some preliminary
discussion is appropriate here.


#### 1.7.1 Correlation plots for derivatives

The growth curves considered in Section 1.1 illustrated the importance
of considering not only the original observations but also some
derivative estimated from them, in this case the second derivative
or acceleration. Once the acceleration curves are estimated, they can
be treated in just the same way as if they were the primary data.
For example, Figure 1.12 contains the contour plot of the correlation
function for the registered acceleration curves for the growth data. A
much tighter coupling of acceleration values is evident in the vicinity
of the two growth spurts. For example, there is a negative correlation
of about 0.5 between accelerations at the beginning and end of the
pubertal growth spurt, whose centre is at 14 years. These spurts tend
to have either large or shallow amplitudes, and sharp acceleration is
followed by sharp deceleration.

<!-- PageBreak -->

<!-- PageNumber="19" -->
<!-- PageHeader="1.7 Using derivatives in functional data analysis" -->


<figure>
<figcaption>FIGURE 1.12. A contour plot of the correlation surface for the acceleration in height of the boys in the Fels Growth Study after registration. The centre of the pubertal growth spurt is at 14 years, and that of the mid-spurt is at 6.5 years. These ages are indicated by the horizontal and vertical dashed lines.</figcaption>

18

0

00.5ft

16

0

c0

-0

5

14

-0.5

0

Age

12

0.5

10

0,5

8

0,5

m

6

0.5

\+

.1 0.50

0

0

0

4

6 8 10 12 14 16 18

Age

</figure>


#### 1.7.2 Plotting pairs of derivatives

Helpful clues to the processes giving rise to functional data can often
be found in the relationships between derivatives. For example, two
functions exhibiting simple derivative relationships are frequently
found as strong influences in functional data: the exponential function,
$f \left( t \right) = C _ { 1 } + C _ { 2 } e ^ { \alpha t } ,$ satisfies the differential equation

$$D f = - \alpha \left( f - C _ { 1 } \right)$$

and the sinusoid $f \left( t \right) = C _ { 1 } + C _ { 2 } \sin \left[ w \left( t - \tau \right) \right]$ with phase constant $T$
satisfies

$$D ^ { 2 } f = - w ^ { 2 } \left( f - C _ { 1 } \right) .$$

Plotting the first or second derivative against the function value
explores the possibility of demonstrating a linear relationship
corresponding to one of these differential equations. Of course, it is
usually not difficult to spot these types of functional variation by
plotting the data themselves. However, plotting the higher derivative
against the lower is often more informative, partly because it is easier
to detect departures from linearity than from other functional forms,
and partly because the differentiation may expose effects not easily
seen in the original functions.

<!-- PageBreak -->

<!-- PageHeader="20 1. Introduction" -->


<figure>
<figcaption>FIGURE 1.13. The left panel gives the annual variation in mean temperature at Montreal. The times of the mid-months are indicated by the first letters of the months. The right panel displays the relationship between the second derivative of temperature and temperature less its annual mean. Strictly sinusoidal or harmonic variation in temperature would imply a linear relationship.</figcaption>

Mean Temperature

-10 -5 0 5 10 15 20

\+

S

N

M

2nd Deriv.

O

-2

N

M

Y

4

0 2 4 6 8 10 12

-10 -5 0 5 10 15 20

Month

Temperature

</figure>


Consider, for example, the variation in mean temperature Temp at
Montreal displayed in the left panel of Figure 1.13. Casual inspection
does indeed suggest a strongly sinusoidal relationship between
temperature and month, but the right panel shows that things are
not so simple. Although there is a broadly linear relationship between
$- D ^ { 2 }$ and Temp after subtracting the mean annual temperature,
there is obviously an additional systematic trend, which is more evident
in the summer through winter months than in the spring. This plot
greatly enhances the small departures from sinusoidal behaviour, and
invites further attention.


#### 1.7.3 Principal differential analysis

Chapter 14 takes up the question, novel in functional data analysis, of
how to use derivative information in studying components of variation.
An approach called principal differential analysis identifies important
variance components by estimating a linear differential operator that
will annihilate them. Linear differential operators, whether estimated
from data or constructed from external modelling considerations,
also play an important part in developing regularization methods
more general than those in common use. Some of their aspects and
advantages will be discussed in Chapter 15.

<!-- PageBreak -->

<!-- PageNumber="21" -->
<!-- PageHeader="1.8 Concluding remarks" -->


### 1.8 Concluding remarks

The last chapter of the book, Chapter 16, includes a discussion of some
historical perspectives and bibliographic references not included in the
main part of our development.

In the course of the book, we shall describe a considerable number
of techniques and algorithms, to explain how the methodology we
develop can actually be used in practice. We shall also illustrate our
methodology on a variety of data sets drawn from various fields,
including where appropriate the examples we have already introduced
in this chapter. However, it is not our intention to provide a cook-book
for functional data analysis, and still less a software manual.

In broad terms, we have a grander aim: to encourage readers to think
about and understand functional data in a new way. The methods
we set out are hardly the last word in approaching the particular
problems, and we believe that readers will gain more benefit by using
the principles we have laid down than by following our own suggestions
to the letter. However, for those who would like access to the software
we have used ourselves, a selection is available on a world-wide web site
associated with the book. This web site will also be used to publicize
related and future work by the authors and others, and to make
available the data sets referred to in the book that we are permitted
to release publicly. Finally, it will contain a list of errors in the text!

The home page for the book is accessible through the publisher's
web site

$$h t t p : / / w w w . s p r i n g e r - n y . c o m$$

or, at the time of writing, through either of the authors' home pages

http://www.psych.mcgill.ca/faculty/ramsay.html

http://www.statistics.bristol.ac.uk/~bernard

and will be updated from time to time.

<!-- PageBreak -->


## 2 Notation and techniques


### 2.1 Introduction

This chapter reviews topics that are notational and conceptual
background to our main development of functional data analysis
beginning in Chapter 3. However, many readers may prefer to skip
straight to the next chapter and to refer back as necessary.

Further background review of useful techniques in linear and
matrix algebra is provided in the Appendix. Among these are matrix
decompositions, projections, and the constrained maximization of
quadratic forms. We make occasional use of these tools, which will in
any case be familiar to many readers, in our discussion of some of the
more technical and algorithmic aspects of functional data analysis.

A basic message of this book is the value of thinking of a functional
observation as a single datum rather than as a large set of data on its
own. Notation facilitating this way of thinking is set out in this chapter.
After some simple notational conventions in the next few pages, we
introduce inner product notation, $\langle x , y \rangle .$ Readers already familiar with
this powerful device may want to move along, but should nevertheless
be warned that we shall indulge ourselves in a few idiosyncracies.

Next we briefly review the extension to the functional setting of some
standard concepts in linear algebra covered in the Appendix.

We close the chapter with a discussion of the multivariate linear
model, to provide a useful link with some of the functional data analysis

<!-- PageBreak -->

<!-- PageNumber="24" -->
<!-- PageHeader="2. Notation and techniques" -->

techniques discussed later on, especially for readers familiar with
multivariate analysis. Particular attention is paid to design matrices not
of full column rank, pointing forward to the concept of regularization
discussed in detail in Chapter 4 and used repeatedly in later chapters
of the book.


### 2.2 General notation


#### 2.2.1 Scalars, vectors, functions and matrices

The reader should be warned that we try to use notation that brings
out the basic structure of what is being done, and that this may entail
the use of conventions a little unfamiliar at first sight. For example,
we do not usually bother to distinguish in our notation between scalar
quantities (numbers), vectors and functions. This means that a single
symbol $x$ can refer to a scalar, a vector with elements $x _ { i } ,$ or a function
with values $x \left( t \right) .$

If $x$ is a vector or function, its elements or values $x _ { i }$ or $x \left( t \right)$ are
usually scalars, but sometimes it is appropriate for the individual $x _ { i }$
or $x \left( t \right)$ to be a vector or function itself. The nervous reader should be
assured that this convention is used only to clarify, rather than confuse,
the discussion! In general, the context should always make clear when
a symbol refers to a scalar, vector or function.

We follow more standard convention, however, in using bold capitals
to refer to matrices, as in $X .$

It is often clearer to use longer strings of letters in a distinctive font
to denote quantities more evocatively than standard notation allows.
For example, we use names such as

· Temp for a temperature record,

· Knee for a knee angle,

· LMSSE for a squared-error fitting criterion for a linear model, and

· RSQ for a squared correlation measure.

We always use the notation $x ^ { \prime }$ for the transpose of a vector $x .$ Note
that ' is not used to denote differentiation. Instead, our notation for
the derivative of order $m$ of a function $x$ is $D ^ { m } x$ this produces cleaner
formulas than $d ^ { m } x / d t ^ { m } .$ It stresses that differentiation is an operator
that acts on a function $x$ to produce another function $D x .$ We also use
operators that act on functions in other ways, and it is convenient to
use a consistent notation.

<!-- PageBreak -->

<!-- PageNumber="25" -->
<!-- PageHeader="2.3 Inner products $\langle x , y \rangle$" -->


#### 2.2.2 Combining quantities

We want to define familiar descriptive statistics, such as the mean
vector and the variance-covariance matrix, in a way that works
equally well for multivariate and functional data. This emphasizes the
connections and similarities between multivariate and functional data
analysis in a way that helps the reader to draw on experience with
multivariate data. A pivotal role is played by inner product notation,
which we discuss in Section 2.3, after briefly considering addition.

An advance in mathematical notation occurs when we separate the
name for an operation from explicit instructions on how to carry it
out. Consider, for example, the operation +. Suppose one opens a
mathematics book at a random page and discovers the expression
$x + y .$ One might imagine that everyone would always mean the same
by $x + y ,$ but a moment's thought shows that computing the sum
can involve very different techniques depending on whether $x$ and
$y$ are real numbers, complex numbers, vectors, matrices of the same
dimensions or functions. What really counts is that we can assume that
any author who uses the symbol + means an operation obeying the
basic properties of addition, such as $x + y = y + x ,$ $\left( x + y \right) + z =$
$x + \left( y + z \right) ,$ $\left( x + y \right) z = x y + x z$ if multiplication is defined, and so
on. The author assumes that we ourselves can actually carry out the
operation involved, or in some exotic situations he furnishes us with
detailed instructions. The notation $x + y$ allows the basic structure of
addition to be assumed, almost subconsciously, leaving the details to
be supplied in any particular case, if necessary.


### 2.3 Inner products $\langle x , y \rangle$


#### 2.3.1 Some specific examples

We now discuss a generic notation for inner products, extending the
familiar idea of the inner product of two vectors $x$ and $y .$ Consider the
Euclidean inner product operation $x ^ { \prime } y ,$ where $x$ and $\mathcal{Y}$ are vectors of
the same length. The operation has the following simple properties:

Symmetry: $x ^ { \prime } y = y ^ { \prime } x$ for all $x$ and $y ,$

Positivity: $x ^ { \prime } x \geq 0$ for all $x ,$ with $x ^ { \prime } x = 0$ if and only if $x = 0 ,$ and

Bilinearity: for all real numbers a and $b ,$ $\left( a x + b y \right) ^ { \prime } z = a x ^ { \prime } z + b y ^ { \prime } z$
for all vectors $x ,$ $y$ and $z .$

<!-- PageBreak -->

<!-- PageNumber="26" -->
<!-- PageHeader="2. Notation and techniques" -->

Of course, these properties follow from the instructions implied in
the definition

$$x ^ { \prime } y = \sum _ { i } x _ { i } y _ { i } .$$
(2.1)

But it is important to note that the Euclidean inner product operation
is of critical importance in multivariate data analysis because of the
properties of symmetry, positivity and bilinearity, which can therefore
be considered fundamentally more significant than the definition (2.1)
itself.

This basic role of symmetry, positivity and bilinearity is further
emphasized when we realize that $x ^ { \prime } W y ,$ where $\mathrm { W }$ is a positive definite
matrix of appropriate order, also has these properties and, indeed,
can be used almost anywhere that we use $x ^ { \prime } y .$ So, for example, we
use $x ^ { \prime } \Sigma ^ { - 1 } y ,$ where $\Sigma$ is a population covariance matrix, to define the
multivariate normal distribution, to compute Mahalanobis distances,
to define generalized least squares estimates instead of ordinary least
squares, and many other useful things.

Now suppose that $x$ and $\mathcal{Y}$ are not vectors but rather functions with
values $x \left( t \right) .$ The natural functional counterpart to $x ^ { \prime } y$ is $\int x \left( t \right) y \left( t \right) d t ,$
replacing the sum in (2.1) by an integral. Again, we have an operation on
two functions $x \quad a n d \quad y$ that is denoted by presenting the instructions for
computing its value, but we know that this, too, is symmetric in $x$ and $\mathcal{Y} ,$
linear in either function, and satisfies the positivity requirement. The
same conclusions can be drawn for the operation $\int \cot \left( t \right) x \left( t \right) y \left( t \right) d t ,$
where $w$ is a strictly positive weight function, and indeed for the more
general operation $\int \int w \left( s , t \right) x \left( s \right) y \left( t \right) d s d t$ if $w$ is strictly positive-
definite, which simply means that the positivity requirement for the
inner product is satisfied.

It should be clear by now that we can achieve a great leap forward
in generality by using a common notation for these various real-
valued operations that is understood to imply symmetry, positivity and
bilinearity, without bothering with the details of the computation. We
call such an operation an inner product, and we use the generic notation
$\langle x , y \rangle$ for the inner product of $x$ and $\mathcal{Y} .$ The fundamental properties
of an inner product are

Symmetry: $\langle x , y \rangle = \langle y , x \rangle$ for all $x$ and $\mathcal{Y} ,$

Positivity: $\langle x , x \rangle \geq 0$ for all $x ,$ with $\langle x , x \rangle = 0$ if and only if $x = 0 ,$ and

Bilinearity: for all real numbers a and $b ,$ $\left( a x + b y , z \right) = a \left( x , z \right) +$
$\left. b y , z \right)$ for all vectors $x ,$ $\mathcal{Y}$ and z.

<!-- PageBreak -->

<!-- PageNumber="27" -->
<!-- PageHeader="2.3 Inner products $\langle x , y \rangle$" -->

Note that bilinearity in the second argument follows from symmetry
and bilinearity in the first.


#### 2.3.2 General properties: association, size, angle, distance

We can think of the inner product as defining a scalar measure of
association between pairs of quantities $x$ and $y .$ The symmetric nature
of the measure means that , as we would usually require, it is invariant
with respect to the order of the quantities. Bilinearity means that
changing the scale of either argument has the same scale effect on
the measure of association, and that the measure of association of
one quantity with the sum of two others is the sum of the individual
measures of association; these are both natural properties for a
measure of association to have.

Positivity means that the inner product of any $x$ with itself is
essentially a measure of its size. The positive square root of this size
measure is called the norm of $x ,$ written $\| x \| ,$ so that

$$| | x | | ^ { 2 } = \left( x , x \right)$$
(2.2)

with $\| x \| \geq 0 .$ In the special case where $x$ is an n-vector and the inner
product is the Euclidean inner product (2.1), the norm of $x$ is simply
the length of the vector measured in n-dimensional space. In the case
of a function $f ,$ a basic type of norm is $\| f \| = \sqrt { \int f ^ { 2 } } ,$ called its $L ^ { 2 }$ norm.
☒

Whatever inner product is used, the standard properties of inner
products lead to the following properties of the norm:

1\. $\| x \| \geq 0$ and $\| x \| = 0$ if and only if $x = 0 .$

2\. $\| a x \| = | a | \| x \|$ for all real numbers a.

3\. $\| x + y \| \leq \| x \| + \| y \| .$

From the properties of the inner product also follows the Cauchy-
Schwarz inequality,

$$| \langle x , y \rangle | \leq \| x \| \| y \| = \sqrt { \langle x , x \rangle \langle y , y \rangle } .$$

This inequality links the inner product with the derived size measure
or norm, and also leads to the cosine inequality,

$$- 1 \leq \langle x , y \rangle / \left( \| x \| \| y \| \right) \leq 1 .$$

The cosine inequality links the inner product to the geometrical
concept of angle; the angle between $x$ and $y$ can be defined as the

<!-- PageBreak -->

<!-- PageNumber="28" -->
<!-- PageHeader="2. Notation and techniques" -->

angle $\theta$ such that

$$\cos \theta = \frac { \langle x , y \rangle } { \| x \| \| y \| } .$$

Where $x$ and $y$ are n-vectors and the inner product is Euclidean inner
product, $\theta$ is the angle between $x$ and $y$ in the usual geometric sense.
Similarly, the cosine of the angle between two functions $f$ and $g$ can
be defined as $\int f g / \sqrt { \left( \int f ^ { 2 } \right) \left( \int g ^ { 2 } \right) } .$ The use of the cosine inequality to
justify the idea of the angle between two vectors or functions further
illuminates the notion that $\langle x , y \rangle$ is an association measure. Once we
have obtained a scale-invariant coefficient by dividing by $\| x \| \| y \| ,$ we
have a useful index of the extent to which $x$ and $y$ are measuring the
same thing.

The particular relation $\langle x , y \rangle = 0 ,$ called orthogonality, implies that $x$
and $y$ can be considered as being at right angles to one another. Because
of bilinearity, orthogonality remains unchanged under any rescaling
of either quantity. Orthogonality plays a key role in the operation of
projection that is discussed in Section 2.4.1.

From the inner product, we also derive a measure of distance between
$x \quad a n d \quad y$

$$d _ { x y } = | | x - y | | = \sqrt { \langle x - y , x - y \rangle }$$

that has extremely wide applications; again, in the Euclidean case,
distance corresponds to the usual geometric definition.

Thus, the simple algebraic properties of symmetry, positivity and
bilinearity of the inner product lead easily to very useful definitions
of the size of a quantity $x ,$ and of the angle and distance between
$x$ and $y .$ We can be confident that, no matter how we define $\langle x , y \rangle$
in a particular application, the essential characteristics of these three
measures remain unchanged.

The nature of the inner product depends on something more
fundamental about $x$ and $y :$ They are elements of a vector space in
which elements can be added or multiplied by real numbers to yield
new vectors, and in which addition distributes with respect to scalar
multiplication. The ensemble of a vector space and an associated inner
product is called an inner product space.

Finally, of the three properties, only symmetry and bilinearity are
really crucial. We can often get by with relaxing positivity to the weaker
condition that $\langle x , x \rangle \geq 0 ,$ so that $\langle x , x \rangle$ may be zero for some $x ^ { \prime } s$ that
are not themselves zero. Then the inner product is called a semi-inner
product and the norm a seminorm. Most properties of inner products
remain true for semi-inner products.

<!-- PageBreak -->

<!-- PageNumber="29" -->
<!-- PageHeader="2.3 Inner products $\langle x , y \rangle$" -->


#### 2.3.3 Descriptive statistics in inner product notation

As an example of how inner products can work for us, we consider
how standard descriptive statistics can be expressed in inner product
notation. Consider the space of possible univariate samples $x =$
$\left( x _ { 1 } , \ldots , x _ { N } \right)$ of size $N .$ Define the inner product to be the Euclidean
inner product

$$\langle x , y \rangle = \sum _ { i } x _ { i } y _ { i } = x ^ { \prime } y .$$

Let 1 indicate the vector of size $N$ all of whose elements are unity.
Then some familiar univariate descriptive statistics become

Mean: $\widetilde { x } = N ^ { - 1 } \langle x , 1 \rangle .$ Note that $\widetilde { \mathrm { x } } ,$ being a multiple of an inner product,
is a scalar and not a vector. The vector of length $N$ all of whose
elements are $\bar { x }$ is $\bar { x } 1 .$

Variance: $s _ { x } ^ { 2 } = N ^ { - 1 } \langle x - \overrightarrow { x } 1 , x - \overrightarrow { x } 1 \rangle = N ^ { - 1 } \| x - \overrightarrow { x } 1 \| ^ { 2 } .$

Covariance: $s _ { x y } = N ^ { - 1 } \langle x - \widetilde { x } 1 , y - \widetilde { y } 1 \rangle .$

Correlation: $r _ { x y } = s _ { x y } / \left( s _ { x } s _ { y } \right) .$

It is easy to show that the covariance $s _ { x y }$ is itself a semi-inner product
between $x$ and $\mathcal{Y} .$ Then it is an immediate consequence of the cosine
inequality that the correlation coefficient satisfies the well-known
correlation inequality

$$- 1 \leq r _ { x y } \leq 1 .$$

Now suppose we stop using the Euclidean inner product but instead
go for

$$\langle x , y \rangle = \sum _ { i } w _ { i } x _ { i } y _ { i } ,$$

where $w _ { i }$ is a nonnegative weight to be applied to observation $i .$ What
difference would this make? None at all, except of course we must
now divide by the constant $\sum _ { i } w _ { i }$ instead of $N$ in defining $\widetilde { \mathrm { x } } ,$ $s _ { x } ^ { 2 } ,$ and
$S _ { X } y .$ The essential characteristics of these statistics depend on the
characteristics of the inner product, not on precisely how it is defined.
Of course, the weighting affects the values of the statistics, but the
essential meanings of the various descriptive statistics, for example
as measures of location, scale and dependence, remain basically
unchanged.

We can generalize this idea further: Suppose that the sequence of
observations is known to be correlated, with covariance matrix $\Sigma .$
Then we can use $\langle x , y \rangle = x ^ { \prime } \Sigma ^ { - 1 } y$ to provide a basis for descriptive

<!-- PageBreak -->

<!-- PageNumber="30" -->
<!-- PageHeader="2. Notation and techniques" -->

statistics that compensate for the known covariance structure on the
observations.

Now consider these same statistics in the context of $x$ as a function
with values $x \left( t \right) ,$ where argument $t$ takes values within some real
interval such as $\left[ 0 , T \right] .$ Thus the index $i$ taking $N$ possible values has
been replaced by the index $t$ taking an infinity of values. Define the
inner product as

$$\langle x , y \rangle = \int _ { 0 } ^ { T } x \left( t \right) y \left( t \right) d t ,$$

where we assume that the functions are sufficiently well behaved that
the integral is always defined and finite. Then the various descriptive
statistics continue to be defined as above, except that we divide by
$\int _ { 0 } ^ { T } d t = T$ instead of $N$ and the vector 1 is replaced by the function
$1 = 1 \left( t \right)$ which takes the value of unity for all $t .$ In the functional case,
$\check { \mathrm { x } }$ becomes the mean level of the function $x ,$ $s _ { x } ^ { 2 }$ becomes a measure
of its variation about its mean level, and $S _ { X } y$ and $r _ { x y }$ measure the
correspondence between the variation of $x$ and $y .$ Moving to

$$\langle x , y \rangle = \int _ { 0 } ^ { T } \omega \left( t \right) x \left( t \right) y \left( t \right) d t$$

for some positive weight function $w$ and dividing by $\int w \left( t \right) d t$ really
would not change these interpretations in any essential way, except
that different parts of the range of $t$ would be regarded as of different
importance.

Finally, we note that even the divisors in these statistics can
be defined in inner product terms, meaning that our fundamental
descriptive statistics can be written in the unifying form

$$x = \left( x , 1 \right) / \| 1 \| ^ { 2 } ,$$
$$s _ { x } ^ { 2 } = \| x - \bar { x } 1 \| ^ { 2 } / \| 1 \| ^ { 2 } ,$$
and

$$s _ { x y } = \left( x - x 1 , y - y 1 \right) / \| 1 \| ^ { 2 } .$$


#### 2.3.4 Some extended uses of inner product notation

In this book, we take the somewhat unorthodox step of using inner
product notation to refer to certain linear operations that, strictly
speaking, do not fall within the rubric of inner products.

So far in our discussion, the result of an inner product has always
been a single real number. One way in which we extend our notation
is the following. Let $x = \left( x _ { 1 } , \ldots , x _ { m } \right) ^ { \prime }$ be a vector of length $m ,$ each
element of which is an element of some vector space, whether finite-
dimensional or functional. Then the notation $\langle x , y \rangle ,$ where $y$ is a single

<!-- PageBreak -->

<!-- PageNumber="31" -->
<!-- PageHeader="2.4 Further aspects of inner product spaces" -->

element of the same space, indicates the m-vector whose elements are
$\langle x _ { 1 } , y \rangle , \ldots , \langle x _ { m } , y \rangle .$ Furthermore, if $\mathcal{Y}$ is similarly a vector of length,
say, $n ,$ then the notation $\langle x , y ^ { \prime } \rangle$ defines the matrix with $m$ rows and
$n$ columns containing the values $\langle x _ { i } , y _ { j } \rangle ,$ $i = 1 , \ldots , m ,$ $j = 1 , \ldots , n .$
We use this convention only in situations where the context should
make clear whether $x \quad a n d / o r \quad y$ are vectors of elements of the space in
question.

In the functional context, we sometimes write

$$\langle z , \beta \rangle = \int z \left( s \right) \beta \left( s \right) d s$$

even when the functions $z$ and $\beta$ are not in the same space. We hope
that the context of this use of inner product notation will make clear
that a true inner product is not involved in this case. The alternative
would have been the use of different notation such as $\left( z , \beta \right) ,$ but we
considered that the possibilities of confusion justified avoiding this
convention.

An important property is that $\langle z , \beta \rangle$ is always a linear operator when
regarded as a function of either of its arguments; generally speaking,
$a$ linear operator on a function space is a mapping $A$ such that, for all
$f _ { 1 }$ and $f _ { 2 }$ in the space and for all scalars $a _ { 1 }$ and $a _ { 2 } ,$ $A \left( a _ { 1 } f _ { 1 } + a _ { 2 } f _ { 2 } \right) =$
$a _ { 1 } A f _ { 1 } + a _ { 2 } A f _ { 2 } .$


### 2.4 Further aspects of inner product spaces

We briefly review two further aspects of inner product spaces that are
useful in our later development. The first of these is the concept of
projection. This generalizes ideas about projection matrices which are
reviewed in detail in the Appendix. In the present discussion we do not
go into any great technical detail.


#### 2.4.1 Projections

Let $u _ { 1 } , \ldots , u _ { n }$ be any $n$ elements of our space, and let $U$ be the
subspace consisting of all possible linear combinations of the $u _ { i } .$ We
can characterize the subspace $U$ by using suitable vector notation. Let $u$
be the n-vector whose elements are the $u _ { 1 } , \ldots , u _ { n } .$ Then every member
of $U$ is of the form $u ^ { \prime } c$ for some real n-vector $c .$

Associated with the subspace $U$ is the orthogonal projection onto $U ,$
defined to be a linear operator $P$ with the following properties:

<!-- PageBreak -->

<!-- PageNumber="32" -->
<!-- PageHeader="2. Notation and techniques" -->

1\. For all $z ,$ the element $P z$ falls in $U ,$ and so is a linear combination
of the functions $u _ { 1 } , \ldots , u _ { n } .$

2\. If $\mathcal{Y}$ is in $U$ already, then $P y = y .$

3\. For all $z ,$ the residual $z \quad - \quad P z$ is orthogonal to all elements $v$ of $u .$

From the first two of these properties, it follows at once that $P P = P ^ { 2 } =$
$P .$ From the third property, it is easy to show that the operator $P$ maps
each element $z$ to its nearest point in $U ,$ distance being measured in
terms of the norm. This makes projections very important in statistical
contexts such as least squares estimation. We give a justification of this
property of orthogonal projections in Section A.2.3 of the Appendix,
where we also address the question of how to carry out the projection
$P$ in practice.


#### 2.4.2 Quadratic optimization

Some of our functional data analysis methodology require the solution
of $a$ particular kind of constrained optimization problem. Suppose that
$A$ is a linear operator on a function space satisfying the condition

$$\langle x , A y \rangle = \langle A x , y \rangle \text { for all } x \text { and } y .$$

Such an operator is called a self-adjoint operator.

Now consider the problem of maximizing $\langle x , A x \rangle$ subject to the
constraint $\| x \| = 1 .$ In Section A.3 of the Appendix, we set out results
relating this optimization problem to the eigenfunction/eigenvalue
problem $A u = \lambda u .$ We go on to consider the more general problem
of maximizing $\langle x , A x \rangle$ subject to a constraint on $\langle x , B x \rangle$ for a second
self-adjoint operator $B .$ We do not go into further detail here but refer
the reader to the Appendix.


### 2.5 The multivariate linear model

We now return to a more statistical topic. A review of the multivariate
linear model may be helpful, both to fix ideas and notation, and because
some of the essential concepts transfer to functional contexts without
much more than a change of notation. But a slight change of perspective
is helpful on what the design matrix means. Moreover, a notion used
repeatedly for functional data is regularization, which we introduce in
Section 2.6 within the multivariate context.

<!-- PageBreak -->

<!-- PageNumber="33" -->
<!-- PageHeader="2.5 The multivariate linear model" -->


#### 2.5.1 Linear models from a transformation perspective

Let $\mathrm { Y }$ be a $N \times p$ matrix of dependent variable observations, $Z$ be a $N \times q$
matrix, and $B$ be a $q \times p$ matrix. In classical terminology, $Z$ is the design
matrix and $B$ is a matrix of parameters.

The multivariate linear model is

$$Y = Z B + E .$$
(2.3)

At least at the population level, the rows of the disturbance or residual
matrix $\mathrm { E }$ are often thought of as independent samples from a common
population of p-variate observations with mean 0 and finite covariance
matrix $\Sigma .$

Although in many contexts it is appropriate to think of the columns
of $\mathrm { Z }$ as corresponding to variables, it is better for our purposes to take
the more general view that $Z$ represents a linear transformation that
maps matrices $B$ into matrices with the dimensions of $\mathrm { Y } .$ This can be
indicated by the notation

$$Z : R ^ { q \times p } \rightarrow R ^ { N \times p }$$

The space of all possible transformed values ZB then defines a subspace
of $R ^ { N \times p } ,$ denoted by $R \left( Z \right)$ and called the range space of $Z .$


#### 2.5.2 The least squares solution

When it is assumed that the rows of the disturbance matrix $\mathrm { E }$ are
independent, each with covariance matrix $\Sigma ,$ the natural inner product
to use in the observation space $R ^ { N \times p }$ is

$$\langle X , Y \rangle = \mathrm { t r a c e } X \Sigma ^ { - 1 } Y ^ { \prime } = \mathrm { t r a c e } Y ^ { \prime } X \Sigma ^ { - 1 }$$
(2.4)

for $X$ and $\mathrm { Y }$ in $R ^ { N \times p } .$ Then we measure the goodness of fit of any
parameter matrix $B$ to the observed data $\mathrm { Y }$ by the corresponding
squared norm

$$\mathrm { L M S S E } \left( B \right) = \| Y - Z B \| ^ { 2 } = \text { trace } \left( Y - Z B \right) ^ { \prime } \left( Y - Z B \right) \Sigma ^ { - 1 } .$$
(2.5)

For the moment, suppose that the matrix $Z$ is of full column rank,
or that $N \geq q$ and the columns of $\mathrm { Z }$ are independent. $\mathrm { A }$ central result
on the multivariate linear model is that the matrix $\widehat { \mathrm { B } }$ that minimizes
LMSSE (B) is given by

$$\widehat { B } = \left( Z ^ { \prime } Z \right) ^ { - 1 } Z ^ { \prime } Y .$$
(2.6)

The corresponding predictor of $\mathrm { Y }$ is given by

$$\widehat { \mathrm { Y } } = \mathrm { Z } \widehat { \mathrm { B } } = \mathrm { Z } \left( \mathrm { Z } ^ { \prime } \mathrm { Z } \right) ^ { - 1 } \mathrm { Z } ^ { \prime } \mathrm { Y } .$$
(2.7)

<!-- PageBreak -->

<!-- PageNumber="34" -->
<!-- PageHeader="2. Notation and techniques" -->

The matrix $\widehat { \mathrm { Y } }$ can be thought of as the matrix in the subspace $R \left( Z \right)$ that
minimizes $\| \mathrm { Y } - \widehat { \mathrm { Y } } \| ^ { 2 }$ over all possible approximations $\widehat { \mathrm { Y } } = \mathrm { Z B }$ falling in
$R \left( Z \right) .$

Note that the least squares estimator $\widehat { \mathrm { B } }$ and the best linear predictor
$\widehat { \mathrm { Y } }$ do not depend on the variance matrix $\Sigma ,$ even though the fitting
criterion LMSSE(B) does. It turns out that when the details of the
minimization of LMSSE(B) are carried through, the variance matrix $\Sigma$
cancels out. But if there are covariances among errors or residuals
across observations, contained in the variance-covariance matrix I, say,
then the inner product (2.4) becomes

$$\langle X , Y \rangle = \text { trace } Y ^ { \prime } \Gamma ^ { - 1 } X \Sigma ^ { - 1 } .$$

Using this inner product in the definition of goodness of fit, the
estimator of $B$ and the best predictor of $\mathrm { Y }$ become

$$\widehat { \mathrm { B } } = \left( \mathrm { Z } ^ { \prime } \Gamma ^ { - 1 } \mathrm { Z } \right) ^ { - 1 } \mathrm { Z } ^ { \prime } \Gamma ^ { - 1 } \mathrm { Y }$$
$$\widehat { \mathrm { Y } } = \mathrm { Z } \left( \mathrm { Z } ^ { \prime } \Gamma ^ { - 1 } \mathrm { Z } \right) ^ { - 1 } \mathrm { Z } ^ { \prime } \mathrm { T } ^ { - 1 } \mathrm { Y } .$$
and

Thus, the optimal solution does depend on how one treats errors across
observations.


### 2.6 Regularizing the multivariate linear model

One of the major themes of this book is regularization, and for readers
familiar with multivariate analysis, it may be helpful to introduce this
idea in the multivariate context first. Others, especially those who are
familiar with curve estimation already, may prefer to omit this section.

Now suppose that we are dealing with an underdetermined problem,
where $q > N$ and the matrix $\mathrm { z }$ is of full row rank $N .$ This means that
the range space $R \left( Z \right)$ is the whole of $R ^ { N \times p } .$


#### 2.6.1 Definition of regularization

Regularization involves attaching a penalty term to the basic squared-
error fitting criterion:

$$\mathrm { L M S S E } _ { \lambda } \left( B \right) = \| \mathrm { Y } - \mathrm { Z B } \| ^ { 2 } + \lambda \times \mathrm { P E N } \left( \mathrm { B } \right) .$$
(2.8)

The purpose of the penalty term $P E N \left( B \right)$ is to require that the estimated
value of $B$ not only yields a good fit in the sense of small $\| Y - Z B \| ^ { 2 } ,$
but also that some aspect of B captured in the function $P E N$ is kept
under control. The positive penalty parameter $\lambda$ quantifies the relative
importance of these two aims. If $\lambda$ is large, then we are particularly

<!-- PageBreak -->

<!-- PageNumber="35" -->
<!-- PageHeader="2.6 Regularizing the multivariate linear model" -->

concerned with keeping PEN(B) small, and getting a good fit to the
data is only of secondary importance. If $\lambda$ is small, then we are not
so concerned about the value of PEN(B).

One example of this type of regularization is the ridge regression
technique, often used to stabilize regression coefficient estimates in
the presence of highly collinear independent variables. In this case,
what is penalized is the size of the regression coefficients themselves,
in the sense that $P E N \left( B \right) = \mathrm { t r a c e } \left( B ^ { \prime } B \right) ,$ the sum of squares of the entries
of $B .$ The solution to the minimization of $\mathrm { L M S S E } _ { \lambda } \left( \mathrm { B } \right)$ is then

$$B = \left( Z ^ { \prime } Z + \lambda I \right) ^ { - 1 } Z ^ { \prime } Y .$$

As $\lambda$ approaches zero, $B$ approaches the least squares solution
described in Section 2.5, but as $\lambda$ grows, $B$ approaches zero. Thus, ridge
regression is said to shrink the solution towards zero.


#### 2.6.2 Hard-edged constraints

One way to obtain a well-determined problem is to place constraints on
the matrix $B .$ For example, consider the model where it is assumed that
the coefficients in each column of $B$ form a constant vector, so all we
have to do is to estimate a single number for each column. If we define
the $\left( q - 1 \right) \times q$ matrix $\mathrm { L }$ to have $L _ { i i } = 1$ and $L _ { i , i + 1 } = - 1$ for each $i ,$ and
all other entries zero, then our assumption about $B$ can be written as
the constraint

$$L B = 0 .$$
(2.9)

For the elements of $B$ to be identifiable from the observed data, the
design matrix $\mathrm { Z }$ has to satisfy the condition

$$Z 1 \neq 0 ,$$
(2.10)

where 1 is a vector of $q$ unities.

The transformation L reduces multiples of the vector 1 exactly
to zero. The identifiability condition (2.10) can be replaced by the
condition that the zero vector is the only q-vector $b$ such that both
$L b$ and $\mathrm { Z } b$ are zero. Equivalently, the matrix $\left[ \mathrm { Z } ^ { \prime } \mathrm { L } ^ { \prime } \right]$ is nonsingular.


#### 2.6.3 Soft-edged constraints

Instead of enforcing the hard-edged constraint $L B = 0 ,$ we may wish to
let the coefficients in any column of $B$ vary, but not more than really
necessary, by exploring compromises between the rank-one extreme
implied by (2.9) and a completely unconstrained underdetermined

<!-- PageBreak -->

<!-- PageNumber="36" -->
<!-- PageHeader="2. Notation and techniques" -->

fit. We might consider this a soft-edged constraint, and it can be
implemented by a suitable regularization procedure. If we define

$$P E N \left( B \right) = | | L B | | ^ { 2 } = \mathrm { t r a c e } \left( B ^ { \prime } L ^ { \prime } L B \right) ,$$
(2.11)

then the penalty $P E N \left( B \right)$ quantifies how far the matrix $B$ is from
satisfying the constraint $L B = 0 .$

The regularized estimate of $B ,$ obtained by minimizing the criterion
(2.8), now satisfies

$$\left( Z ^ { \prime } Z + \lambda L ^ { \prime } L \right) B = Z ^ { \prime } Y .$$
(2.12)

For any $\lambda > 0 ,$ a unique solution for $B$ requires the nonsingularity of the
matrix $\left[ Z ^ { \prime } L ^ { \prime } \right] ,$ precisely the condition for identifiability of the model
subject to the constraint (2.9).

In the limit as the parameter $\lambda \twoheadrightarrow \infty ,$ the penalized fitting criterion
(2.8) automatically enforces on $B$ the one-dimensional structure $L B = 0 .$
On the other hand, in the limit $\lambda \rightarrow 0 ,$ no penalty at all is applied,
and $B$ takes on whatever value results in minimizing the error sum
of squares to zero, because of the underdetermined character of the
problem. Thus, from the regularization perspective, the constrained
estimation problem $L B = 0$ that arises frequently in linear modelling
designs is simply an extreme case of the regularization process where
$\lambda \rightarrow \infty .$

We have concentrated on a one-dimensional constrained model,
corresponding to a $\left( q - 1 \right) \times q$ matrix $\mathrm { L } ,$ but of course the ideas can
be immediately extended to nonsingular $s \times q$ constraint matrices $\mathrm { L }$
that map a q-vector into a space of vectors of dimension $s \leq q .$
In this case, the constrained model is of dimension $q \quad - \quad s .$ Note also
that the specification of the matrix L corresponding to any particular
constrained model is not unique. If $L$ is specified differently the
regularized estimates are in general different.

Finally, we note in passing that Bayesian approaches to regression,
in which a multivariate normal prior distribution is proposed for $B ,$ can
also be expressed in terms of a penalized least squares problem of the
form (2.8). For further details see, for example, Kimeldorf and Wahba
(1970), Wahba (1978) or Silverman (1985).

<!-- PageBreak -->


## 3 Representing functional data as smooth functions


### 3.1 Introduction


#### 3.1.1 Observed functional data

The basic philosophy of functional data analysis is that we should
think of observed data functions as single entities, rather than merely a
sequence of individual observations. The term functional refers to the
intrinsic structure of the data rather than to their explicit form. But in
practice, functional data are usually observed and recorded discretely.
A record of a functional observation $x$ consists of $n$ pairs $\left( t _ { j } , y _ { j } \right) ,$ where
$\mathcal{Y} _ { j }$ is a recording or observation of $x \left( t _ { j } \right) ,$ a snapshot of the function at
argument value $t _ { j } .$

In this chapter, we consider some techniques for converting raw
functional data into true functional form. Since some observational
noise is part of most data, the functional representation of raw data
usually involves some smoothing, and so we review various smoothing
techniques. Special attention is given to estimating derivatives, since
these are important in many functional data analyses. In accordance
with the notational conventions we have already established, let $D ^ { m } x$
indicate the mth derivative of $a$ univariate function $x .$ The value of the
mth derivative for argument value $t$ is indicated by $D ^ { m } x \left( t \right) .$

What would it mean for a functional observation $x$ to be known in
true functional form? We do not mean that $x$ is actually recorded for

<!-- PageBreak -->

<!-- PageNumber="38" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

every value of $t ,$ because that would involve storing an uncountable
number of values! Rather, we mean that we posit the existence of a
function $x ,$ based on the given data, implying that, in principle, we can
evaluate $x$ at any point $t ,$ and in addition that we can evaluate any of
its derivatives $D ^ { m } x$ that exist at $t .$ But because only discrete values are
actually available, evaluating $x \left( t \right)$ and $D ^ { m } \left( t \right)$ at any arbitrary value $T$
will involve some form of interpolation or smoothing of these discrete
values.

In general, we are concerned with a collection of functional data,
rather than just a single function $x .$ Specifically, the record or
observation of the function $x _ { i }$ might consist of $n _ { i }$ pairs $\left( t _ { i j } , \mathcal{Y} _ { i j } \right) ,$
$j = 1 , \ldots , n _ { i } .$ It may be that the argument values $t _ { i j }$ are the same
value for each record, but they may also vary from record to record.
We conceptualize the problem as functional rather than multivariate
because it is assumed that functions $x _ { i }$ lie behind the data. In general,
we consider the reconstruction of the functional observations $x _ { i }$ one
by one. Therefore, in this chapter, we simplify notation and assume
that a single function $x$ is being observed.

It is always assumed that the range of values of interest for the
argument $t$ is a bounded interval $T ,$ and, implicitly or explicitly, that
$x$ satisfies reasonable continuity or smoothness conditions on $T .$
Without some conditions of this kind, it is impossible to draw any
inferences at all about values $x \left( t \right)$ for any points $t$ apart from actual
observation points. Sometimes the argument is cyclic, for instance
when $t$ is the time of year, and this means that the functions satisfy
periodic boundary conditions, where the function $x$ at the beginning of
the interval $T$ picks up smoothly from the values of $x$ at the end.


#### 3.1.2 Sampling and observational error

Smoothness, in the sense possessing of a certain number of derivatives,
is a property of the latent function $x ,$ and may not be at all obvious in
the raw data vector $y = \left( y _ { 1 } , \ldots , y _ { n } \right)$ because of observational error or
noise that may be imposed on the underlying signal by aspects of the
measurement process. In modelling terms, we write

$$y _ { j } = x \left( t _ { j } \right) + \epsilon _ { j }$$
(3.1)

where the disturbance, error, perturbation or otherwise exogenous
term $\epsilon _ { j }$ contributes a roughness to the raw data. One of the tasks in
representing the raw data as functions may be to attempt to filter out
this noise as efficiently as possible. In some cases we may pursue an
alternative strategy of leaving the noise in the data, and, instead, require

<!-- PageBreak -->

<!-- PageNumber="39" -->
<!-- PageHeader="3.1 Introduction" -->

smoothness of the results of our analysis, rather than of the data that
are analysed.

The standard statistical model for the $\epsilon _ { j }$ is that they are
independently distributed with zero mean and finite variance. It is also
convenient to assume that a constant variance $\sigma ^ { 2 }$ is common to these
distributions. But in special cases, we must take explicit account of
variance nonhomogeneity and covariances of the $\epsilon _ { j }$ for neighbouring
argument values. Finally, we should keep in mind the possibility that
errors or disturbances multiply rather than add, in which case it will
be more convenient to work with the logarithms of the data.

The sampling rate or resolution of the raw data is a key determinant
of what is possible in functional data analysis. The most important
aspect is an essentially local property of the data, the density of the
argument values $t _ { j }$ relative to the amount of curvature in the data,
rather than simply the number $n$ of argument values. Curvature at
argument $t$ is usually measured by the size $| D ^ { 2 } x \left( t \right) |$ of the second
derivative. Where curvature is high, it is essential to have enough points
to estimate the function effectively. What is enough? This depends on
the amount of error $\epsilon _ { j }$ when the error level is small and the curvature is
mild, as is the case for the Canadian temperature data in Figure 1.3, we
can get away with a low sampling rate. The human growth data in Figure
1.1 have moderately low error levels (about 0.3% of adult height), but the
curvature in the second derivative functions is fairly severe, so that the
sampling rate for these data is barely adequate for making inferences
about growth acceleration. The gait data in Figure 1.5 exhibit little error,
and thus the sampling rate of 20 values per cycle is sufficient for most
purposes.

Figure 3.1 provides an interesting example of functional data. The
letters "fda" were written on a flat surface by one of the authors. The
pen positions were recorded by an Optotrak system that gives the
position of an infrared-emitting diode in three-dimensional space 600
times per second. The $\mathrm { X }$ and $\mathrm { Y }$ position functions ScriptX and $\mathrm { S c r i p t } Y$
are plotted separately in Figure 3.2, and we can see that the error level
is too small to be visible. The total event took about 2.3 seconds, and
the plotted functions each have 1401 discrete values. This may seem
like a lot, but the curvature is rather high in places, and it turns out that,
even with the small error level, this level of resolution is important.

We shall investigate various ways in which the discrete observations
$\mathcal{Y} _ { j }$ can be represented by an appropriately smooth function $x ,$ paying
particular attention to estimating its derivative values. But first, some
words of caution about estimating derivatives directly from raw data.
Because the observed function looks reasonably smooth, one might be

<!-- PageBreak -->

<!-- PageNumber="40" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->


<figure>
<figcaption>FIGURE 3.1. $\mathrm { A }$ sample of handwriting in which the $X$ and $\mathrm { Y }$ coordinates are recorded 600 times per second.</figcaption>

20

0

-20

-40

-20

0

20

</figure>


<figure>
<figcaption>FIGURE 3.2. The $X$ and $\mathrm { Y }$ coordinates for the handwriting sample plotted separately. Note the strongly periodic component with from two to three cycles per second.</figcaption>

40

f

d

a

40

$f$

d

a

coordinate

20

Y coordinate

20

0

0

-20

-20

-40

-40

0.0

0.5

1.0

1.5

2.0

0.0

0.5

1.0

1.5

2.0

Time (sec)

Time (sec)

</figure>


<!-- PageBreak -->

<!-- PageNumber="41" -->
<!-- PageHeader="3.1 Introduction" -->


<figure>
<figcaption>FIGURE 3.3. The first and second central differences for the $X$ coordinate for the handwriting sample. The high sampling rate causes differencing to greatly magnify the influence of noise.</figcaption>

,
-3 -2 -1 0 1 2 3

X second difference/10000

O

X first difference/100

\-

0

7

N

0.0 0.5 1.0 1.5 2.0

0.0 0.5 1.0 1.5 2.0

Time (sec)

Time (sec)

</figure>


tempted to use the first forward difference $\left( y _ { j + 1 } - y _ { j } \right) / \left( t _ { j + 1 } - t _ { j } \right)$ or the
central difference $\left( y _ { j + 1 } - y _ { j - 1 } \right) / \left[ 2 \left( t _ { j + 1 } - t _ { j - 1 } \right) \right]$ to estimate $D x \left( t _ { j } \right) ,$ but
Figure 3.3 shows that the resulting derivative estimate for ScriptX is
rather noisy. The second difference estimate of $D ^ { 2 } \mathrm { S c r i p t } X$ assuming
equally spaced arguments,

$$D ^ { 2 } x \left( t _ { j } \right) \approx \left( y _ { j + 1 } + y _ { j - 1 } - 2 y _ { j } \right) / \left( \Delta t \right) ^ { 2 } ,$$

is shown in Figure 3.3 to be a disaster, displaying far too little signal
relative to the noise. The reason for this is the high sampling rate for
the data; taking differences between extremely close values magnifies
the influence of error enormously. Note also the cautions of Press et
al. (1992) on using simple differencing to estimate derivatives even
when functions are available analytically. Although a common practice,
derivative estimation by differencing is, in fact, seldom a good idea!

As a final word on observational error, we point out that the classical
model (3.1) could be replaced by a model

$$y _ { j } = x \left( t _ { j } \right) + \epsilon \left( t _ { j } \right) ,$$
(3.2)

where a noise function $\epsilon$ is added to the smooth signal $x$ and then
evaluated. We might assume that $\epsilon$ has the intuitive characteristics
of white noise: mean zero, constant variance, and covariance zero for
distinct argument values.

We may have a substantive reason to prefer the discrete noise model
(3.1) to the functional noise model (3.2). For example, the growth data

<!-- PageBreak -->

<!-- PageNumber="42" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

clearly have discrete or observational noise. From experiments, we
know that independent measurements of the same child at a fixed
time have a standard error of around 1.5 mm. On the other hand, the
temperature data are estimates of a mean function based on a sample
of about 30 annual functions, and can be reasonably viewed as having
no functional error, since the error in a temperature measurement is
a very small fraction of the variation in actual temperature, whether
taken over scales of minutes, days, or years. In any case, discrete data
do not offer any way of choosing between these models.

Although the techniques in this chapter are designed to filter out
observational error in the functions themselves, such error, whether
discrete or functional, is not the only model possible for the variation
from one functional observation to another. Noise can also affect one
or more derivatives. For example, the variation in the handwriting
data, where the observational error is, after all, a small fraction of
the signal, can be caused by variation in the forces applied to the
pen by muscle contractions. By Newton's Third Law these forces will
affect the position of the pen only indirectly through their effect on its
acceleration. Our plot of pen position in Figure 3.1 would look smooth
even if the acceleration were noisy, because integrating acceleration
twice to give position would inevitably smooth the noise but not
reduce it to zero. These considerations are particularly relevant to the
discussion in Chapters 13 to 15, where the use of linear differential
operators to analyse functional data is explored in detail. But generally
we need to keep in mind that some types of noise will appear smooth
at the level of observation.

Now we turn to a discussion of various smoothing methods designed
for direct observational error. Our goal is to give enough information
to those new to the topic to launch a functional data analysis. For more
complete treatments of this large and rapidly evolving field, many of
them concentrating on particular aspects and methods, we refer the
reader to sources such as Eubank (1988), Fan and Gijbels (1996), Green
and Silverman (1994), Härdle (1990), Hastie and Tibshirani (1990),
Simonoff (1996) and Wand and Jones (1995). One particular class of
methods, based on roughness penalties, plays a particular rôle in our
development of functional data analysis methods, and this is discussed
separately in Chapter 4.

Most of the methods we consider are linear smoothers, and it is useful
to discuss this general class of smoothers first of all.

<!-- PageBreak -->

<!-- PageNumber="43" -->
<!-- PageHeader="3.1 Introduction" -->


#### 3.1.3 Linear smoothing

A linear smoother estimates the function value $x \left( t \right)$ by a linear
combination of the discrete observations

$$\widehat { x } \left( t \right) = \sum _ { j = 1 } ^ { n } S _ { j } \left( t \right) \mathcal{Y} _ { j } .$$
(3.3)

The behaviour of the smoother at $t$ is determined by the weights $S _ { j } \left( t \right) .$
These weights do not depend only on the argument value $t$ at which the
function is to be estimated and on the particular within-record index
$j .$ In general, there is some kind of dependence on the whole pattern
of observation points $\left( t _ { 1 } , \ldots , t _ { n } \right) ,$ but this is not expressed explicitly in
the notation.

Linear smoothers can be represented in matrix form. Suppose we
have in mind a sequence $s _ { 1 } < s _ { 2 } < \ldots < s _ { m }$ of evaluation values in
$T$ at which the function $x$ is to be estimated. Note that the evaluation
values need not be the same as the observation values $t _ { j } .$ Write $\widehat { x }$ for
the m-vector of values $x \left( s _ { i } \right)$ and $y$ for the vector of observed data $\mathcal{Y} _ { j } .$
We can then write

$$\widehat { x } = S y$$
(3.4)

where $S _ { i j } = S _ { j } \left( s _ { i } \right) .$

Many widely used smoothers are linear. The linearity of a smoother
is a desirable feature for various reasons: The linearity property

$$S \left( a y + b z \right) = a S y + b S z$$

is important for working out various properties of the smooth
representation, and the simplicity of the smoother implies relatively
fast computation. On the other hand, some nonlinear smoothers may
be more adaptive to different behaviour in different parts of the range
of observation, and may be robust to outlying observations. Smoothing
by the thresholded wavelet transform, discussed in Section 3.2.6, is an
important example of a nonlinear smoothing method.

Speed of computation can be critical; a smoother useful for a few
hundred evaluation or data points can be completely impractical for
thousands. Smoothers that require of the order of $n ,$ abbreviated $O \left( n \right) ,$
operations to compute $n$ smoothed values $\widehat { x } \left( s _ { i } \right)$ are virtually essential
for large $n ,$ but linear smoothers that are less efficient computationally
may be highly desirable in other ways. If $S$ is band-structured, meaning
that only a small number $K$ of values on either side of its diagonal in any
row are nonzero, then $O \left( n \right)$ computation is assured. However, it is not
only for band-structured $\mathrm { S }$ that $O \left( n \right)$ computations are possible; see,

<!-- PageBreak -->

<!-- PageNumber="44" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

for example, the discussion of spline smoothing in Green and Silverman
(1994) and of L-spline smoothing in Chapter 15 of this book.


### 3.2 Basis function methods


#### 3.2.1 Least squares fitting of basis expansions

One of the most familiar smoothing procedures involves representing
the function by a linear combination of $K$ known basis functions $\phi _ { k } ,$

$$x \left( t \right) = \sum _ { k = 1 } ^ { K } c _ { k } \phi _ { k } \left( t \right) .$$
(3.5)

The degree to which the data $\mathcal{Y} _ { j }$ are smoothed, rather than exactly
reproduced or interpolated, is determined by the number $K$ of basis
functions. Assuming that the $n \times K$ matrix $\Phi = \left\{ \phi _ { k } \left( t _ { j } \right) \right\}$ of basis
function values at the observation points is of full rank, an exact
representation is generally possible when $K = n ,$ in the sense that we
can choose the coefficients $c _ { k }$ to yield $x \left( t _ { j } \right) = y _ { j }$ for each $j .$

The simplest linear smoother defined by a basis function expansion
is obtained if we determine the coefficients of the expansion $c _ { k }$ by
minimizing the least squares criterion

$$\mathrm { S M S S E } \left( \mathcal{Y} | C \right) = \sum _ { j = 1 } ^ { n } \left[ \mathcal{Y} _ { j } - \sum _ { k = 1 } ^ { K } c _ { k } \phi _ { k } \left( t _ { j } \right) \right] ^ { 2 } ,$$
(3.6)

or, in matrix terms,

$$\mathrm { S M S S E } \left( y | c \right) = \left( y - \Phi c \right) ^ { \prime } \left( y - \Phi c \right) = \| y - \Phi c \| ^ { 2 } ,$$

where the K-vector $c$ contains the coefficients $c _ { k } .$ This criterion is
minimized by the solution $c = \left( \Phi ^ { \prime } \Phi \right) ^ { - 1 } \Phi ^ { \prime } \mathcal{Y} .$

Assuming that the evaluation points are identical to the observation
points, the smoothing matrix $S$ is then given by

$$S = \Phi \left( \Phi ^ { \prime } \Phi \right) ^ { - 1 } \Phi ^ { \prime } .$$
(3.7)

The smoothing matrix $S$ in this case is an orthogonal projection matrix
since it is symmetric and satisfies the idempotency relation $S ^ { 2 } = S .$
Thus, a least squares basis function smoother is simply an orthogonal
projection of a record onto the space spanned by the columns of the
basis matrix $\Phi .$

<!-- PageBreak -->

<!-- PageNumber="45" -->
<!-- PageHeader="3.2 Basis function methods" -->

More generally, if the evaluation points $S _ { i }$ are not necessarily the
same as the observation points, define the matrix $m \times n$ matrix $\widetilde { \Phi }$ to
have elements $\phi _ { j } \left( s _ { i } \right) .$ Then the smoothing matrix is given by

$$S = \widetilde { \Phi } \left( \Phi ^ { \prime } \Phi \right) ^ { - 1 } \Phi ^ { \prime } .$$

We can extend the least squares criterion to the form

$$\mathrm { S M S S E } \left( y | c \right) = \left( y - \Phi c \right) ^ { \prime } W \left( y - \Phi c \right) = \| y - \Phi c \| _ { W } ^ { 2 } ,$$
(3.8)

where $\mathrm { W }$ is a known symmetric positive-definite matrix that allows for
unequal weighting of squares and products of residuals. This extension
can be important if we know that the variances of the disturbances
$\epsilon _ { j }$ are not constant, or that the disturbances are not independently
distributed in some known way. The estimates of the coefficients $c$
are then given by $\left( \Phi ^ { \prime } \mathrm { W } \Phi \right) ^ { - 1 } \Phi ^ { \prime } \mathrm { W y } .$ In the case where the evaluation
arguments and the data arguments are the same, the corresponding
smoothing matrix is then

$$S = \Phi \left( \Phi ^ { \prime } W \Phi \right) ^ { - 1 } \Phi ^ { \prime } W ,$$

and is still an orthogonal projection operator since WS is symmetric.
The mapping defined by $S$ is often said to be a projection in the metric
$\mathrm { W } .$

$\mathrm { A }$ central question is how to choose the order of the expansion $K .$
Since a least squares basis function expansion is essentially a multiple
regression problem, the large literature on selecting a good subset of
variables from a larger pool offers considerable guidance. Nevertheless,
the fact that $K$ can take only integer values implies that control over
smoothing may be comparatively crude. The sections on localized least
squares methods and smoothing splines in this chapter indicate how
finer control is possible.

When $n$ is large, efficient computation is critical. There are three
essential tasks in computing the estimates for general evaluation
points:

1\. Compute inner products, of which there are $K$ in $\Phi ^ { \prime } \mathcal{Y}$ and
$\left( + 1 \right) / 2$ in $\Phi ^ { \prime } \Phi .$

2\. Solve the linear system $\Phi ^ { \prime } \Phi c = \Phi ^ { \prime } \mathcal{Y} .$

3\. Compute the $m$ inner products $\widetilde { \Phi } \mathcal{C} ,$ where the matrix $\widetilde { \Phi }$ contains
the basis functions evaluated at the evaluation arguments.

Efficient and stable least squares algorithms can perform these
calculations or their equivalents in $O \left[ \left( n + m \right) K ^ { 2 } \right]$ operations, and this

<!-- PageBreak -->

<!-- PageNumber="46" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

is acceptable provided $K$ is small and fixed relative to $n$ and $m .$ But
for large $K$ it is extremely helpful, for both computational economy
and numerical stability, if the cross-product matrix $\Phi ^ { \prime } \Phi$ has a band
structure such that nonzero values appear only in a fixed and limited
number of positions on either side of the diagonal. A basis orthogonal
with respect to summation over $j$ is the extreme case because the cross-
product matrix is diagonal; the coefficients of the least squares fit are
then found by multiplying the data vector $y$ by an explicit $K \times n$ matrix,
without needing to solve any system of linear equations.

In the worst-case scenario, without a band structure and with $K$ and
$m$ of $O \left( n \right) ,$ the computation is $O \left( n ^ { 3 } \right) ,$ which is unacceptable for $n$
in the many hundreds. Thus efficient computation is essential for the
handwriting data $\left( n = 1 4 0 1 \right)$ and for the daily weather data.


#### 3.2.2 Choosing a good basis

A desirable characteristic of basis functions is that they have features
matching those known to belong to the functions being estimated.
Ideally, a basis should be chosen to achieve an excellent approximation
using a comparatively small value of $K ;$ not only does this imply less
computation, but the coefficients themselves can become interesting
descriptors of the data from a substantive point of view. Consequently,
certain classic off-the-rack bases may, in fact, be ill-advised in some
applications; there is no such thing as a good universal basis.

The choice of basis is particularly important for the derivative
estimate

$$D \widehat { x } \left( t \right) = \sum _ { k = 1 } ^ { K } c _ { k } D \phi _ { k } \left( t \right) .$$
(3.9)

Bases that work well for function estimation may give rather poor
derivative estimates. This is because an accurate representation of the
observations may force $\widehat { x }$ to have small but high-frequency oscillations
with horrible consequences for its derivatives. Put more positively, one
of the criteria for choosing a basis may be whether or not one or more
of the derivatives of the approximation behave reasonably.

Chapter 15 touches on tailoring a basis to fit a particular problem. For
now, we discuss some popular bases that are widely used in practice.

<!-- PageBreak -->

<!-- PageNumber="47" -->
<!-- PageHeader="3.2 Basis function methods" -->


#### 3.2.3 Fourier series

Perhaps the best known basis expansion is provided by the Fourier
series:

$$\widehat { x } \left( t \right) = c _ { 0 } + c _ { 1 } \sin w t + c _ { 2 } \cos w t + c _ { 3 } \sin 2 w t + c _ { 4 } \cos 2 w t + \ldots \left( 3 . 2 \right.$$

defined by the basis $\phi _ { 0 } \left( t \right) = 1 , \phi _ { 2 r - 1 } \left( t \right) = \sin r w t ,$ and $\phi _ { 2 r } \left( t \right) =$
$\cos r w t .$ This basis is periodic, and the parameter $w$ determines the
period $2 \pi / w ,$ which is equal to the length of the interval $T$ on which
we are working. If the values of $t _ { j }$ are equally spaced on $T ,$ then the
basis is orthogonal in the sense that the cross-product matrix $\Phi ^ { \prime } \Phi$ is
diagonal, and can be made equal to the identity by dividing the basis
functions by suitable constants, $\sqrt { n }$ for $j = 0$ and $\sqrt { n / 2 }$ for all other $j .$
☒ ☒

The Fast Fourier transform (FFT) makes it possible to find all the
coefficients extremely efficiently; when $n$ is a power of 2 and the
arguments are equally spaced, then we can find both the coefficients
$c _ { k }$ and all $n$ smooth values at $x \left( t _ { j } \right)$ in $O \left( n \log n \right)$ operations. This is
one of the features that has made Fourier series the traditional basis
of choice for long time series.

Derivative estimation is simple since

$$D \sin r w t = r w \cos r w t$$

and

$$D \cos r w t = - r w \sin r w t .$$

This implies that the Fourier expansion of $D x$ has coefficients

$$\left( 0 , - \infty c _ { 2 } , w c _ { 1 } , - 2 w c _ { 4 } , 2 w c _ { 3 } , \ldots \right)$$

and of $D ^ { 2 } x$ has coefficients

$$\left( 0 , - w ^ { 2 } c _ { 1 } , - w ^ { 2 } c _ { 2 } , - 4 w ^ { 2 } c _ { 3 } , - 4 w ^ { 2 } c _ { 4 } , \ldots \right) .$$

Similarly, we can find the Fourier expansions of higher derivatives
by multiplying individual coefficients by suitable powers of $r w ,$
with appropriate sign changes and interchanges of sine and cosine
coefficients.

The Fourier series is so familiar to statisticians and applied
mathematicians that it is worth stressing its limitations to emphasize
that, invaluable though it may often be, neither it nor any other basis
should be used uncritically. A Fourier series is especially useful for
extremely stable functions, meaning functions where there are no
strong local features and where the curvature tends to be of the same

<!-- PageBreak -->

<!-- PageNumber="48" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

order everywhere. Ideally, the periodicity of the Fourier series should
be reflected to some degree in the data, as is certainly the case for the
temperature and gait data. Fourier series generally yield expansions
which are uniformly smooth. But they are inappropriate to some degree
for data known or suspected to reflect discontinuities in the function
itself or in low-order derivatives. A Fourier series is like margarine:
It is cheap and you can spread it on practically anything, but don't
expect that the result will be exciting eating. Nevertheless, we find many
applications for Fourier series expansion in this book.


#### 3.2.4 Polynomial bases

The monomial basis $\phi _ { k } \left( t \right) = \left( t - w \right) ^ { k } , k = 0 , \ldots , K$ is also classic.
Unfortunately, it can yield a nearly singular cross-product matrix $\Phi ^ { \prime } \Phi ,$
and the shift parameter $w$ must be carefully chosen. However, if the
argument values $t _ { j }$ are equally spaced or can be chosen to exhibit a few
standard patterns, orthogonal polynomial expansions can be obtained,
implying $O \left[ \left( n + m \right) K \right]$ operations for all smooth values. Otherwise we
are condemned to contemplate $O \left[ \left( n + m \right) K ^ { 2 } \right]$ operations.

Like the Fourier series expansion, polynomials cannot exhibit very
local features without using a large $K .$ Moreover, polynomials tend to fit
well in the centre of the data but exhibit rather unattractive behaviour in
the tails. They are usually a poor basis for extrapolation or forecasting,
for example.

Although derivatives of polynomial expansions are simple to
compute, they are seldom satisfactory as estimators of the true
derivative because of the rapid localized oscillation typical of high-
order polynomial fits.


#### 3.2.5 Regression spline bases

It is safe to say that the Fourier and polynomial bases have tended to
be rather overused in applied work. Their inability to accommodate
local features led to the development of polynomial splines: functions
constructed by joining polynomials together smoothly at values $\tau _ { k }$
called knots. Let the number of these knots be indicated by $K _ { 1 } + 1 ,$ where
the two outside knots define the interval $T$ over which the estimation
is to take place, and $K _ { 1 } - 1$ is the number of interior knots. Between
two adjacent knots, a polynomial spline is a polynomial of fixed degree
$K _ { 2 } ,$ but at an interior knot, two adjacent polynomials are required to
match in the values of a fixed number of their derivatives, usually
chosen to be $K _ { 2 } - 1 .$ This implies that a spline of degree 0 is a step

<!-- PageBreak -->

<!-- PageNumber="49" -->
<!-- PageHeader="3.2 Basis function methods" -->

function discontinuous at knots, a spline of degree 1 is a polygonal
or piecewise linear function, and a spline of degree 2 is a piecewise
quadratic with continuous first derivative. A common choice of degree
is 3, or piecewise cubic. The continuity of the first two derivatives of a
cubic spline means that the curve is visually smooth. A classic reference
on polynomial splines, in general, and B-splines, in particular, is de Boor
(1978), and more recent references are Eubank (1988) and Green and
Silverman (1994).

Polynomial splines combine the easy computability of polynomials
with the capacity for changing local behaviour and great flexibility.
There are many ways to represent polynomial splines, but perhaps the
simplest conceptually is as a linear combination of the basis functions

$$\phi _ { k } \left( t \right) = \left( t - \tau _ { k } \right) _ { + } ^ { K _ { 2 } } ,$$

where $u _ { + }$ means $u$ if $u \geq 0$ and 0 otherwise, and where only the $K _ { 1 } - 1$
interior knot values are used. This is called the truncated power basis.
This basis must be augmented by the monomial basis $t ^ { k } ,$ $k = 0 , \ldots , K _ { 2 } .$
to produce a complete polynomial spline of order $K .$ The total number
of basis functions is $K = K _ { 1 } + K _ { 2 } ,$ or the degree of the piecewise
polynomial plus the number of interior knots.

Although the truncated power basis is still used in certain
applications, its tendency to produce nearly singular cross-product
matrices is a problem if there is more than a small number of knots. It is
much better in practice to use B-splines, which have compact support,
that is, are zero everywhere except over a finite interval. In the case
of cubic splines, each $B$ B-spline is a cubic spline with support on the
interval $\left[ T _ { k - 2 } , T _ { k + 2 } \right] ,$ and with shorter support at the ends. Compact
support implies both a band-structured cross-product matrix and $O \left( K \right)$
computation of all smoothing values.

There is a question as to where the knots $\tau _ { \ell }$ should be positioned.
Although some applications strongly suggest specific knot locations,
the choice may often be rather arbitrary, and users may complain
that there is comparatively little to go on. On the other hand, some
approaches capitalize on the free choice of knot location by beginning
with a dense set of knots and then eliminating unneeded knots by an
algorithmic procedure similar to variable selection techniques used in
multiple regression. See, for example, Friedman and Silverman (1989).


#### 3.2.6 Wavelet bases

We can construct a basis for all functions on $\left( - \infty , \infty \right)$ that are square-
integrable by choosing a suitable mother wavelet function $\psi$ and then

<!-- PageBreak -->

<!-- PageNumber="50" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

considering all dilations and translations of the form

$$\psi _ { j k } \left( t \right) = 2 ^ { j / 2 } \psi \left( 2 ^ { j } t - k \right)$$

for integers $j$ and $k .$ We construct the mother wavelet to ensure that the
basis is orthogonal, in the sense that the integral of the product of any
two distinct basis functions is zero. Typically, the mother wavelet has
compact support, and hence so do all the basis functions. The wavelet
basis idea is easily adapted to deal with functions defined on a bounded
interval, most simply if periodic boundary conditions are imposed.

The wavelet expansion of $a$ function $f$ gives a multiresolution analysis
in the sense that the coefficient of $\psi _ { j k }$ yields information about $f$
near position $2 ^ { - j } k$ on scale $2 ^ { - j } ,$ i.e. at frequencies near $c 2 ^ { j }$ for some
constant $c$ c. Thus, wavelets provide a systematic sequence of degrees
of locality. In contrast to Fourier series, wavelet expansions cope well
with discontinuities or rapid changes in behaviour; only those basis
functions whose support includes the region of discontinuity or other
bad behaviour are affected. This property, as well as a number of
more technical mathematical results, means that it is often reasonable
to assume that an observed function is well approximated by an
economical wavelet expansion with few nonzero coefficients, even if
it displays sharp local features.

Suppose a function $x$ is observed without error at $n = 2 ^ { M }$
regularly spaced points on an interval $T .$ Just as with the Fourier
transformation, there is a discrete wavelet transform (DWT) which
provides $n$ coefficients closely related to the wavelet coefficients
of the function $x .$ We can calculate the DWT and its inverse in
$O \left( n \right)$ operations, even faster than the $O \left( n \log n \right)$ of the FFT. As a
consequence, most estimators based on wavelets can be computed
extremely quickly, many of them in $O \left( n \right)$ operations.

Now suppose that the observations of $x$ are subject to noise. The fact
that many intuitively attractive classes of functions have economical
wavelet expansions leads to a simple nonlinear smoothing approach:
Construct the DWT of the noisy observations, and threshold it by
throwing away the small coefficients in the expansion and possibly
shrinking the large ones. The basic motivation of thresholding is
the notion that any small coefficient is entirely noise and does not
reflect any signal at all. This nonlinear thresholding has attractive and
promising theoretical properties (see, for example, Donoho, Johnstone,
Kerkyacharian and Picard, 1995), indicating that thresholded wavelet
estimators should adapt well to different degrees of smoothness and
regularity in the function being estimated.

<!-- PageBreak -->

<!-- PageNumber="51" -->
<!-- PageHeader="3.3 Smoothing by local weighting" -->

The development of wavelet bases is comparatively recent, and
only limited methodological experience is available at the time of
writing. They are obviously of considerable promise and have excellent
computational properties; perhaps their real practical strengths and
weaknesses have yet to be fully understood. For further reading, see
Chui (1992), Daubechies (1992), Press et al. (1992), Nason and Silverman
(1994), Donoho et al. (1995), Johnstone and Silverman (1997), and the
many references contained in these books and papers.


### 3.3 Smoothing by local weighting


#### 3.3.1 Kernel functions

For a smoothing method to make any sense at all, the value of
the function estimate at a point $t$ must be influenced mostly by
the observations near $t$ t. This feature is an implicit property of the
estimators we have considered so far. In this section, we consider
estimators where the local dependence is made more explicit by means
of local weight functions.

The localizing weights $w _ { j }$ are simply constructed by a location and
scale change of a kernel function with values $\mathrm { K e r n } \left( u \right) .$ This kernel
function is designed to have most of its mass concentrated close to 0,
and either to decay rapidly or to disappear entirely for $| u | \geq 1 .$ Three
commonly used kernels are


<table>
<tr>
<td>uniform:</td>
<td>Kern(u) = 0.5, $| u | \leq 1 ,$</td>
<td>0 otherwise ,</td>
</tr>
<tr>
<td>quadratic:</td>
<td>Kern(u) = 0.75(1 - u2),</td>
<td>0 otherwise, and</td>
</tr>
<tr>
<td>Gaussian:</td>
<td>$$\mathrm { K e r n } \left( u \right) = \left( 2 \pi \right) ^ { - 1 / 2 } \exp \left( - u ^ { 2 } / 2 \right) .$$</td>
<td></td>
</tr>
</table>


Then we define weight values

$$w _ { j } \left( t \right) = \mathrm { K e r n } \left( \frac { t _ { j } - t } { h } \right)$$
(3.11)

substantial values $w _ { j } \left( t \right)$ as a function of $j$ are now concentrated for
$t _ { j }$ in the vicinity of $t ,$ and the degree of concentration is controlled
by the size of $h .$ The concentration parameter $h$ is usually called the
bandwidth parameter, and small values imply that only observations
close to $t$ receive any weight, whereas large $h$ means that a wide-
sweeping average uses values even a considerable distance from $t .$

<!-- PageBreak -->

<!-- PageNumber="52" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->


#### 3.3.2 Kernel smoothing

The simplest and classic case of an estimator that makes use of local
weights is the kernel estimator. The estimate at a given point is a linear
combination of local observations,

$$\widehat { x } \left( t \right) = \sum _ { j } ^ { N } S _ { j } \left( t \right) y _ { j }$$
(3.12)

for suitably defined weight functions $S _ { j } .$ Classically, the Nadaraya-
Watson estimator (Nadaraya 1964, Watson 1964) is constructed by
using the weights

$$S _ { j } \left( t \right) = \frac { \mathrm { K e r n } \left[ \left( t _ { j } - t \right) / h \right] } { \sum _ { r } \mathrm { K e r n } \left[ \left( t _ { r } - t \right) / h \right] }$$
(3.13)

that is, the weight values $w _ { j } \left( t \right)$ normalized to have a unit sum.

However, it is not essential that the smoothing weight values $S _ { j } \left( t \right)$
sum exactly to one. The weights developed by Gasser and Müller (1979,
1984) are constructed as follows

$$S _ { j } \left( t \right) = h \int _ { \widetilde { t } _ { j - 1 } } ^ { \widetilde { t } _ { j } } \mathrm { K e r n } \left( \frac { u - t } { h } \right) d u .$$
(3.14)

where $\bar { t } _ { j } = \left( t _ { j + 1 } + t _ { j } \right) / 2 , 1 < j < n , \bar { t } _ { - 1 } = t _ { 1 }$ and $\widetilde { t } _ { n } = t _ { n } .$ These
weights are faster to compute, deal more sensibly with unequally
spaced arguments, and have good asymptotic properties.

The need for fast computation strongly favours the compact support
uniform and quadratic kernels, and the latter is the most efficient when
only function values are required and the true underlying function $x$
is twice-differentiable. The Gasser-Müller weights using the quadratic
kernel are given by

$$S _ { j } \left( t \right) = \frac { 1 } { 4 } \left[ \left\{ 3 r _ { j - 1 } \left( t \right) - r _ { j - 1 } ^ { 3 } \left( t \right) \right\} - \left\{ 3 r _ { j } \left( t \right) - r _ { j } ^ { 3 } \left( t \right) \right\} \right]$$

for $| t _ { j } - t | \leq h ,$ and 0 otherwise, with

$$r _ { j } \left( t \right) = \frac { t - \bar { t } _ { j } } { h } .$$
(3.15)

We need to take special steps if $t$ is within $h$ units of either $t _ { 1 }$ or $t _ { n }$
These measures can consist of simply extending the data beyond this
range in some reasonable way, making $h$ progressively smaller as these
limits are approached, or of sophisticated modifications of the basic
kernel function Kern. The problem that all kernel smoothing algorithms

<!-- PageBreak -->

<!-- PageNumber="53" -->
<!-- PageHeader="3.3 Smoothing by local weighting" -->


<figure>
<figcaption>FIGURE 3.4. The second derivative or acceleration of the coordinate functions for the handwriting data. Kernel smoothing was used with a bandwidth $h = 0 . 0 7 5 .$</figcaption>

5000

Acceleration

0

-5000

0.0

0.5

1.0

1.5

2.0

Time (sec)

</figure>


have near the limits of the data is one of their major weaknesses,
especially when $h$ is large relative to the sampling rate.

Estimating the derivative just by taking the derivative of the kernel
smooth is not usually a good idea, and, in any case, kernels such as
the uniform and quadratic are not differentiable. However, kernels
specifically designed to estimate a derivative of fixed order can be
constructed by altering the nature of kernel function Kern. For example,
a kernel $\mathrm { K e r n } \left( u \right)$ suitable for estimating the first derivative must be
zero near zero, positive above zero, and negative below, or it is a sort of
smeared-out version of the first central difference. The Gasser-Müller
weights for the estimation of the first derivative are

$$S _ { j } \left( t \right) = \frac { 1 5 } { 1 6 h } \left[ \left\{ r _ { j - 1 } ^ { 4 } \left( t \right) - 2 r _ { j - 1 } ^ { 2 } \left( t \right) \right\} - \left\{ r _ { j } ^ { 4 } \left( t \right) - 2 r _ { j } ^ { 2 } \left( t \right) \right\} \right]$$
(3.16)

and for the second derivative are

$$S _ { j } \left( t \right) = \frac { 1 0 5 } { 1 6 h ^ { 2 } } \left[ \left\{ 2 r _ { j - 1 } ^ { 3 } \left( t \right) - r _ { j - 1 } ^ { 5 } \left( t \right) - r _ { j - 1 } \left( t \right) \right\} - \left\{ 2 r _ { j } ^ { 3 } \left( t \right) - r _ { j } ^ { 5 } \left( t \right) - r _ { j } \left( t \right) \right\} \right]$$
(3.17)

for $| t _ { j } - t | \leq h$ and 0 otherwise. It is usual to need a somewhat larger
value of bandwidth $h$ to estimate derivatives than is required for the
function.

<!-- PageBreak -->

<!-- PageNumber="54" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

Figure 3.4 shows the estimated second derivative or acceleration
for the two handwriting coordinate functions. After inspection of the
results produced by a range of bandwidths, we settled on $h = 0 . 0 7 5 .$
This implies that any smoothed acceleration value is based on about
150 milliseconds of data and about 90 values of $\mathcal{Y} _ { j } .$


#### 3.3.3 Localized basis function estimators

The ideas of kernel estimators and basis function estimators can, in a
sense, be combined to yield localized basis function estimators, which
encompass a large class of function and derivative estimators. The
basic idea is to extend the least squares criterion (3.6) to give a local
measure of error as follows:

$$\mathrm { S M S S E } _ { t } \left( \mathcal{Y} | C \right) = \sum _ { j = 1 } ^ { n } w _ { j } \left( t \right) \left[ \mathcal{Y} _ { j } - \sum _ { k = 1 } ^ { K } c _ { k } \phi _ { k } \left( t _ { j } \right) \right] ^ { 2 } ,$$
(3.18)

where the weight functions $w _ { j }$ are constructed from the kernel function
using (3.11).

In matrix terms,

$$\mathrm { S M S S E } _ { t } \left( y | c \right) = \left( y - \Phi c \right) ^ { \prime } W \left( t \right) \left( y - \Phi c \right)$$
(3.19)

where $W \left( t \right)$ is a diagonal matrix containing the weight values $w _ { j } \left( t \right)$ in
its diagonal. Choosing the coefficients $c$ to minimize $\mathrm { S M S S E } _ { t }$ yields

$$c = \left[ \Phi ^ { \prime } W \left( t \right) \Phi \right] ^ { - 1 } \Phi ^ { \prime } W \left( t \right) y .$$

Substituting into the expansion $\widehat { x } \left( t \right) = \sum _ { k = 1 } ^ { K } c _ { k } \phi _ { k } \left( t \right)$ gives a linear
smoothing estimator of the form (3.3) with smoothing weight values
$S _ { j } \left( t \right)$ the elements of the vector

$$S \left( t \right) = W \left( t \right) \Phi \left[ \Phi ^ { \prime } W \left( t \right) \Phi \right] ^ { - 1 } \phi \left( t \right)$$
(3.20)

where $\phi \left( t \right)$ is the vector with elements $\phi _ { k } \left( t \right) .$

The weight values $w _ { j } \left( t \right)$ in (3.18) are designed to have substantially
nonzero values only for observations located close to the evaluation
argument $t$ at which the function is to be estimated. This implies that
only the elements in $S \left( t \right)$ in (3.20) associated with data arguments
values $t _ { j }$ close to the evaluation argument $t$ are substantially different
from zero. Consequently, $\widehat { \chi } \left( t \right)$ is essentially a linear combination only
of the observations $\mathcal{Y} _ { j }$ in the neighbourhood of $t .$

Since the basis has only to approximate a limited segment of the
data surrounding $t ,$ the basis can do a better job of approximating the

<!-- PageBreak -->

<!-- PageNumber="55" -->
<!-- PageHeader="3.3 Smoothing by local weighting" -->

local features of the data and, at the same time, we can expect to do
well with only a small number $K$ of basis functions. The computational
overhead for a single $t$ depends on the number of data argument values
$t _ { j }$ for which $w _ { j } \left( t \right)$ is nonzero, as well as on $K .$ Both of these are typically
small. However, the price we pay for this flexibility is that the expansion
must essentially be carried out anew for each evaluation point $t .$


#### 3.3.4 Local polynomial smoothing

It is interesting to note that the Nadaraya-Watson kernel estimate can
be obtained as a special case of the localized basis expansion method
by setting $K = 1$ and $\phi _ { i } \left( t \right) = 1 .$ A popular class of methods is obtained
by extending from a single basis function to a low-order polynomial
basis. Thus, we choose the estimated curve value $\widehat { x } \left( t \right)$ to minimize the
localized least squares criterion

$$\mathrm { S M S S E } _ { t } \left( \mathcal{Y} | C \right) = \sum _ { j = 1 } ^ { n } \mathrm { K e r n } _ { h } \left( t _ { j } , t \right) \left[ \mathcal{Y} _ { j } - \sum _ { \ell = 0 } ^ { L } c _ { \ell } \left( t - t _ { j } \right) ^ { \ell } \right] ^ { 2 } .$$
(3.21)

Setting $L = 0 ,$ we recover the Nadaraya-Watson estimate. For values of
$L \geq 1 ,$ the function value and $L$ of its derivatives can be estimated by
the corresponding derivatives of the locally fitted polynomial at $t .$ In
general, the value of L should be at least one and preferably two higher
than the highest order derivative required.

Local polynomial smoothing has a strong appeal; see, for example,
the detailed discussion provided by Fan and Gijbels (1996). Its
performance is superior in the region of the boundaries, and it adapts
well to unequally spaced argument values. Local linear expansions give
good results when we require only an estimate of the function value.
They can easily be adapted in various ways to suit special requirements,
such as robustness, monotonicity, and adaptive bandwidth selection.
The S-PLUS function lowess, based on work of Cleveland (1979),
incorporates a wide spectrum of valuable features.


#### 3.3.5 Choosing the bandwidth

In all the localized basis expansion methods we have considered, the
primary determinant of the degree of smoothing is the bandwidth
$h ,$ rather than the number of basis functions used. The bandwidth
controls the balance between two considerations, bias and variance in
the estimate. Small values of $h$ imply that the expected value of the
estimate $\widehat { x } \left( t \right)$ must be close to the true value $x \left( t \right) ,$ but the price we

<!-- PageBreak -->

<!-- PageNumber="56" -->
<!-- PageHeader="3. Representing functional data as smooth functions" -->

pay is in terms of the high variability of the estimate, since it is based
on comparatively few observations. On the other hand, variability can
always be decreased by increasing $h ,$ although this is inevitably at the
expense of higher bias, since the values used cover a region in which the
function's shape varies substantially. Mean squared error at $t ,$ which is
the sum of squared bias and variance, provides a composite measure
of performance.

There is a variety of data-driven automatic techniques for choosing
an appropriate value of $h ,$ usually motivated by the need to minimize
mean squared error across the estimated function. Unfortunately,
none of these can always be trusted, and the problem of designing
a reliable data-driven bandwidth selection algorithm continues to be
a subject of active research and considerable controversy. Our own
view is that trying out a variety of values of $h$ and inspecting the
consequences graphically remains a suitable means of resolving the
bandwidth selection problem for most practical problems.


### 3.4 Summary

Explicitly localized smoothing methods, such as kernel smoothing
and local polynomial smoothing, are easy to understand and have
excellent computational characteristics. The role of the bandwidth
parameter $h$ is obvious, and as a consequence it is even possible
to allow $h$ to adapt to curvature variation. On the negative side,
however, is the instability of these methods near the boundaries of the
interval, although local polynomial smoothing performs substantially
better than kernel smoothing in this regard. As with unweighted
basis function expansions, it is well worthwhile to consider matching
the choice of basis functions to known characteristics of the data,
especially in regions where the data are sparse or where they are
asymmetrically placed around the point $t$ of interest, for example near
the boundaries. The next chapter on the roughness penalty approach
looks at the main competitor to kernel and local polynomial methods,
namely spline smoothing.

<!-- PageBreak -->


## 4 The roughness penalty approach


### 4.1 Introduction

In this chapter we introduce a third option for approximating discrete
data by a function. The roughness penalty or regularization approach
retains the advantages of the basis function and local expansion
smoothing techniques developed in Chapter 3, but circumvents some of
their limitations. More importantly, it adapts gracefully to more general
functional data analysis problems that we consider in subsequent
chapters.

We saw that basis expansions work well if the basis functions have
the same essential characteristics as the process generating the data.
Thus, a Fourier basis is useful if the functions we observe are periodic
and do not exhibit fluctuations in any particular interval that are
much more rapid than those elsewhere. But basis expansions, on
the debit side, have clumsy discontinuous control over the degree
of smoothing, and can be expensive to compute if the basis exhibits
neither orthogonality nor local support.

Standard kernel smoothing and local polynomial fitting techniques,
on the other hand, are based on appealing, efficient and easily
understood algorithms that are fairly simple modifications of classic
statistical techniques. They offer continuous control of the smoothness
of the approximation, but they are seldom optimal solutions to an
explicit statistical problem, such as minimizing a measure of total

<!-- PageBreak -->

<!-- PageNumber="58" -->
<!-- PageHeader="4. The roughness penalty approach" -->

squared error, and their rather heuristic character makes extending
them to other smoothing situations difficult.

Like the basis expansion approach, roughness penalty methods are
based on an explicit statement of what a smooth representation of the
data is trying to do, but the need to have a smooth representation
is expressed explicitly at the level of the criterion being optimized.
Moreover, they can be applied to a much wider range of smoothing
problems than simply estimating a curve $x$ from observations of $x \left( t _ { i } \right)$
for certain points $t _ { i } .$ Green and Silverman (1994) discuss a variety of
statistical problems that can be approached using roughness penalties,
including those where the data's dependence on the underlying curve
is akin to the dependence on parameters in generalized linear models.
Here we extend still further the scope of roughness penalty methods by
discussing various functional data analysis contexts where roughness
penalties are an elegant way to introduce smoothing into the analysis.

Finally, recent developments in the computational aspects of
roughness penalty smoothing imply efficient $O \left( n \right)$ computation. These
methods share the capacity to smooth a large number observations
with kernel and local polynomial smoothing and with certain basis
function expansions.


### 4.2 Spline smoothing

Let us first consider how regularization works in the simplest
functional case when the goal is to estimate a function $x$ on the basis of
discrete and noisy observations in a vector $\mathcal{Y} .$ Readers familiar with the
multivariate linear model may wish to review the use of regularization
for estimating a parameter matrix, developed in Section 2.6.


#### 4.2.1 Two competing objectives in function estimation

The spline smoothing method estimates a curve $x$ from observations
$y _ { j } = x \left( t _ { j } \right) + \epsilon _ { j }$ by making explicit two possible aims in curve
estimation. On the one hand, we wish to ensure that the estimated curve
gives a good fit to the data, for example in terms of the residual sum
of squares $\sum _ { j } \left\{ y _ { j } - x \left( t _ { j } \right) \right\} ^ { 2 } .$ On the other hand, we do not wish the fit
to be too good if this results in a curve $x$ that is excessively 'wiggly' or
locally variable.

These competing aims can be seen, in some sense, as corresponding
to the two elements of the basic principle of statistics:

Mean squared error = Bias2 + Sampling variance

<!-- PageBreak -->

<!-- PageNumber="59" -->
<!-- PageHeader="4.2 Spline smoothing" -->

According to the error model $y _ { j } = x \left( t _ { j } \right) + \epsilon _ { j } ,$ a completely unbiased
estimate of the function value $x \left( t _ { j } \right)$ can be produced by a curve fitting
$\mathcal{Y} _ { j }$ exactly, since this observed value is itself an unbiassed estimate
of $x \left( t _ { j } \right) .$ But any such curve must have high variance, manifested in
the rapid local variation of the curve. In spline smoothing, as in other
smoothing methods, the mean square error comes somewhat closer to
capturing what we usually mean by poorness of estimation. It can often
be dramatically reduced by sacrificing some bias to reduce sampling
variance, and this is a key reason for imposing smoothness on the
estimated curve. By requiring that the estimate vary only gently from
one value to another, we are borrowing information from neighbouring
data values, thereby expressing our faith in the regularity of the
underlying function $x$ that we are trying to estimate.

In the basis function approach, we constrained $x$ to be a linear
combination of a small number $K$ of basis functions, and minimized
the residual sum of squares subject to this hard-edged constraint. The
philosophy of the roughness penalty method, on the other hand, is
to allow a larger class of functions $x$ but to quantify the rapid local
variation of $x$ and make an explicit trade-off between regularity and
goodness of fit to the data, which corresponds to an implicit trade-off
between variance and bias.

A popular measure of the roughness of a function is by its integrated
squared second derivative

$$P E N _ { 2 } \left( x \right) = \int \left\{ D ^ { 2 } x \left( s \right) \right\} ^ { 2 } d s = \| D ^ { 2 } x \| ^ { 2 } .$$
(4.1)

This assesses the total curvature in $x ,$ or alternatively, the degree to
which $x$ departs from a straight line. Consequently, highly variable
functions can be expected to yield high values of $P E N _ { 2 } \left( x \right)$ because their
second derivatives are large over much of the range of interest.

We can then define the penalized residual sum of squares by

$$P E N S S E _ { \lambda } \left( x | y \right) = \sum _ { j } \left\{ \mathcal{Y} _ { j } - x \left( t _ { j } \right) \right\} ^ { 2 } + \lambda \times P E N _ { 2 } \left( x \right) .$$
(4.2)

Our estimate of the function is obtained by finding the function $x$ that
minimizes $P E N S S E _ { \lambda } \left( x \right)$ over the space of functions $x$ for which $P E N _ { 2 } \left( x \right)$
is defined.

The parameter $\lambda$ is a smoothing parameter that measures the rate of
exchange between fit to the data, as measured by the residual sum of
squares, and variability of the function $x ,$ as quantified by $P E N _ { 2 } \left( x \right) .$ If
$\lambda$ is large, then functions which are not linear must incur a substantial
roughness penalty in $P E N S S E _ { \lambda } \left( x \right) .$ For this reason, as $\lambda \rightarrow \infty$ the fitted
curve $x$ approaches the standard linear regression to the observed data.

<!-- PageBreak -->

<!-- PageNumber="60" -->
<!-- PageHeader="4. The roughness penalty approach" -->

On the other hand, for small $\lambda$ the curve tends to become more
and more variable since there is less and less penalty placed on its
roughness, and as $\lambda \rightarrow 0$ the curve $x$ approaches an interpolant to
the data, satisfying $x \left( t _ { j } \right) = y _ { j }$ for all $\mathrm { j } .$ However, even in this limiting
case the interpolating curve is not arbitrarily variable; instead, it is the
smoothest twice-differentiable curve that exactly fits the data.

The curve $x$ resulting from the use of the roughness penalty $P E N _ { 2 } c a n$
be shown to be a cubic spline with knots at the data points $t _ { j } .$ Many
details of the method are discussed by Green and Silverman (1994),
and we discuss it only fairly superficially here, leaving a more detailed
discussion to our treatment of a wider class of splines in Chapter
15. Function $x$ can be found in $O \left( n \right)$ operations, for example using
the $S$ S-PLUS function smooth. spline, which also contains options for
choosing the smoothing parameter automatically from the data.


#### 4.2.2 Estimating derivatives by spline smoothing

Many functional data analyses call for the estimation of derivatives,
either because these are of direct interest, or because they play a role
in some other part of the analysis. The penalty (4.1) may not be suitable,
since it controls curvature in $x$ itself, and therefore only slope in the
derivative $D x .$ It does not require the second derivative $D ^ { 2 } x$ even to be
continuous, let alone smooth in any sense.

If the derivative of order $m$ is the highest required, one should
probably penalize two derivatives higher. For example, the estimate
of acceleration is better if we use

$$P E N _ { 4 } \left( x \right) = \int _ { T } \left\{ D ^ { 4 } x \left( s \right) \right\} ^ { 2 } d s = \| D ^ { 4 } x \| ^ { 2 }$$
(4.3)

in (4.2) since this controls the curvature in $D ^ { 2 } x .$ Ramsay (1996c)
developed an $O \left( n \right)$ algorithm for the polynomial smoothing spline
defined by penalizing $D ^ { m } x ,$ and installed an $S$ S-PLUS module called
Pspline in the Statlib library of $S$ S-PLUS functions. Statlib is accessible
on the Web at http://lib.stat.cmu.edu. The software is also
available through the home page for this book described in Section
1.8.


#### 4.2.3 More general measures of fit

There are aspects of the roughness penalty method that are really
useful in our treatment of functional data analysis. For example, instead
of quantifying fit to the data by the residual sum of squares, we can

<!-- PageBreak -->

<!-- PageNumber="61" -->
<!-- PageHeader="4.2 Spline smoothing" -->

penalize any criterion of fit by a roughness penalty. For instance, we
might have a model for the observed $\mathcal{Y} _ { j }$ for which the log likelihood of
$x$ can be written down. Subtracting $\lambda \times P E N _ { 2 } \left( x \right)$ from the log likelihood
and then finding the maximum allows smoothing to be introduced in
a wide range of statistical problems, not merely those in which error is
appropriately measured by a residual sum of squares. These extensions
of the roughness penalty method are a major theme of Green and
Silverman (1994).

In the functional data analysis context, we adopt this philosophy in
considering functional versions of several multivariate techniques. The
function estimated by these methods is expressed as the solution of a
maximization (or minimization) problem based on the given data. For
example, principal components are chosen to have maximum possible
variance subject to certain constraints. By penalizing this variance
using a roughness penalty term appropriately, the original aim of the
analysis can be traded off against the need to control the roughness of
the estimate. There are different ways of incorporating the roughness
penalty according to the context, but the overall idea remains the same:
Penalize whatever is the appropriate measure of goodness-of-fit to the
data for the problem under consideration.


#### 4.2.4 More general roughness penalties

The second extension of the roughness penalty method uses measures
of roughness other than $\| D ^ { 2 } x \| ^ { 2 } .$ We have already seen one reason
for this in Section 4.2.2, where the estimation of derivatives of $x$ was
considered. However, even if the function itself is of primary interest,
there are two related reasons for considering more general roughness
penalties. On the one hand, we may wish the class of functions with
zero roughness were wider than, or otherwise different from, those that
are of the form $a + b t .$ On the other hand, we may have in mind that,
locally at least, curves $x$ should ideally satisfy a particular differential
equation, and we may wish to penalize departure from this.

We can achieve both of these goals by replacing the second derivative
operator $D ^ { 2 }$ with a more general linear differential operator $L ,$ defined
as

$$L x = w _ { 0 } x + w _ { 1 } D x + \ldots + w _ { m - 1 } D ^ { m - 1 } x + D ^ { m } x ,$$

where the weights $w _ { j }$ may be either constants or functions $w _ { j } \left( t \right) .$ Then
we can define

$$P E N _ { L } \left( x \right) = \| L x \| ^ { 2 } ,$$

the integral of the square of $L x .$

<!-- PageBreak -->

<!-- PageNumber="62" -->
<!-- PageHeader="4. The roughness penalty approach" -->

For instance, if we were observing periodic data on an interval $\left[ 0 , 2 \pi \right]$
and there were some reason to suppose that simple harmonic motion
was a natural approximate model for the data, then we could define
$L x = D ^ { 2 } x + x .$ Or, as an alternative to prespecifying the differential
operator, we can use observed functional data to estimate the operator
$L .$ These ideas are developed further in Chapters 14 and 15.


### 4.3 The regularized basis approach

We now turn to a more general approach, of which spline smoothing
turns out to be a special case. So far we have used basis functions in
two essentially different ways. In Section 3.2, we forced the function
$x$ to lie in a relatively low dimensional space, defined in terms of a
suitable basis. On the other hand, in Section 3.3, we did not assume
that the whole function was in the span of a particular basis, but rather
we considered a local basis expansion at any given point. In this section,
we allow the function to have a higher dimensional basis expansion, but
use a roughness penalty in fitting the function to the observed data.


#### 4.3.1 Complementary bases

To develop our approach, suppose that we have two sets of basis
functions, $\phi _ { j } , j = 1 , \ldots , J$ and $\psi _ { k } , k = 1 , \ldots , K ,$ that complement
one another. Let functions $\phi _ { j }$ be small in number and chosen to
give reasonable account of the large-scale features of the data. The
complementary basis functions $\psi _ { k }$ will generally be much larger in
number, and are designed to catch local and other features not
representable by the $\phi _ { j } .$ Assume that any function $x$ of interest can
be expressed in terms of the two bases as

$$x \left( s \right) = \sum _ { j = 1 } ^ { J } d _ { j } \phi _ { j } \left( s \right) + \sum _ { k = 1 } ^ { K } c _ { k } \psi _ { k } \left( s \right) .$$
(4.4)

For example, for the Canadian temperature data, the first three
Fourier series functions with $w = \pi / 6$ would be a natural choice for
the $\phi _ { j } ,$ setting $J = 3$ and letting the $\phi$ basis be the functions

$$1 , \sin \left( w t \right) , \cos \left( w t \right) .$$

The appropriate choice for the $\psi _ { k }$ in this case would be the remaining
$K$ functions in an order $\left( J + K \right)$ Fourier series expansion. In the monthly
temperature data case, they could be the remaining nine Fourier series

<!-- PageBreak -->

<!-- PageNumber="63" -->
<!-- PageHeader="4.3 The regularized basis approach" -->

terms needed to represent the data exactly. Usually, as in the Fourier
case above, the bases $\left\{ \phi _ { j } \right\}$ and $\left\{ \psi _ { k } \right\}$ are mutually linearly independent,
and the expansion is unique, but this is not entirely essential to our
method.


#### 4.3.2 Specifying the roughness penalty

Let us now develop a roughness penalty for $x$ so that linear
combinations of the $\phi _ { j }$ are in effect completely smooth, in that they
contribute nothing to the roughness penalty. Then the roughness
penalty must depend only on the coefficients of the $\psi _ { k } .$ One way of
motivating this choice is by thinking of $x$ as the sum of two parts, an
'ultrasmooth' function $x _ { S } = \sum _ { j } d _ { j } \phi _ { j }$ and a function $x _ { R } = \sum _ { k } c _ { k } \psi _ { k } .$
Therefore we seek a measure $P E N \left( x _ { R } \right)$ of how rough, or in any other
way important, we would consider the function $x _ { R }$ expressed solely in
terms of the $\psi _ { k } .$ One possibility is simply to take the usual $L _ { 2 }$ norm of
$x _ { R } ,$ defining

$$P E N _ { 0 } \left( x _ { R } \right) = \int _ { T } x _ { R } \left( s \right) ^ { 2 } d s = \int _ { C } \left( c ^ { \prime } \psi \right) ^ { 2 } = \int _ { T } \left[ \sum _ { k = 1 } ^ { K } c _ { k } \psi _ { k } \left( s \right) \right] ^ { 2 } d s .$$

Another possibility is to take a certain order of derivative of the
expansion prior to squaring and integrating, just as we did for the
function $x$ itself in Section 4.2. For example, we might use

$$P E N _ { 2 } \left( x _ { R } \right) = \int \left( D ^ { 2 } x _ { R } \right) ^ { 2 } = \int _ { T } \left[ \sum _ { k = 1 } ^ { K } c _ { k } D ^ { 2 } \psi _ { k } \left( s \right) \right] ^ { 2 } d s$$

to assess the importance of $x _ { R }$ in terms of its total curvature, as
measured by its squared second derivative, or $P E N _ { 4 } \left( x _ { R } \right) = \int \left( c ^ { \prime } D ^ { 4 } \psi \right) ^ { 2 }$
to assess the curvature of its second derivative. More generally, we can
use any linear differential operator $L ,$ defining

$$P E N _ { L } \left( x _ { R } \right) = \int \left( L x _ { R } \right) ^ { 2 } = \int _ { T } \left[ \sum _ { k = 1 } ^ { K } c _ { k } L \psi _ { k } \left( s \right) \right] ^ { 2 } d s .$$

Of course, setting $L$ as the identity operator or the second derivative
operator yields $P E N _ { 0 }$ and $P E N _ { 2 }$ as special cases.

We can express these penalties in matrix terms as

$$P E N _ { L } \left( x _ { R } \right) = c ^ { \prime } R c$$

where the order $K$ symmetric matrix $\mathbb{R}$ contains elements

$$R _ { k l } = \int _ { T } L \psi _ { k } \left( s \right) L \psi _ { l } \left( s \right) d s = \langle L \psi _ { k } , L \psi _ { l } \rangle .$$

<!-- PageBreak -->

<!-- PageNumber="64" -->
<!-- PageHeader="4. The roughness penalty approach" -->

If computing the integrals proves difficult, a simple numerical
integration scheme, such as the trapezoidal rule applied to a fine mesh
of argument values, usually suffices, and then we can also estimate
derivatives numerically. Alternatively, we can specify $R$ directly as
any suitable symmetric non-negative definite matrix, without explicit
reference to the roughness of the function $x _ { R } .$

Now we consider a general function $x$ of the form (4.4), and simply
define the roughness of $x$ as

$$P E N \left( x \right) = c ^ { \prime } R c .$$

To express the penalized sum of squares, we need to express the
residual sum of squares in terms of the coefficient vectors $d$ and $c .$
Working just as in (3.6),

$$\sum _ { i } \left\{ y _ { i } - x \left( t _ { i } \right) \right\} ^ { 2 } = | | y - \Phi d - \Psi c | | ^ { 2 }$$

where the $n \times K$ matrix $\Psi$ has elements $\Psi _ { i k } = \psi _ { k } \left( t _ { i } \right) .$ We can now define
the composite smoothing criterion

$$P E N S S E _ { \lambda } \left( x | y \right) = | | y - \Phi d - \Psi c | | ^ { 2 } + \lambda c ^ { \prime } R c .$$
(4.5)

We can minimize this quadratic form in $d$ and $c$ to find the fitted
curve $x$ in terms of its expansion (4.4) as follows. The solution for $d$
for any fixed value of $c$ is given by

$$d = \left( \Phi ^ { \prime } \Phi \right) ^ { - 1 } \Phi ^ { \prime } \left( \mathcal{Y} - \Psi c \right)$$
(4.6)

and, consequently,

$$\Phi d = P _ { \phi } \left( y - \Psi c \right) ,$$

where the projection matrix $P _ { \phi } = \Phi \left( \Phi ^ { \prime } \Phi \right) ^ { - 1 } \Phi ^ { \prime } .$ In words, the $\phi$ basis
component of the fit is the conventional basis expansion of the residual
vector $y - \Psi c .$ Substitute this solution for $d$ into $\mathrm { P E N S S E } _ { \lambda } ,$ and define
the complementary projection $Q _ { \phi } = I - P _ { \phi } .$ Recalling that $\mathrm { Q } _ { \phi } \mathrm { Q } _ { \phi } = \mathrm { Q } _ { \phi } ,$
we arrive at the equation

$$c = \left( \Psi ^ { \prime } Q _ { \phi } \Psi + \lambda R \right) ^ { - 1 } \Psi ^ { \prime } Q _ { \phi } y .$$
(4.7)

Note that these calculations are for expository purposes only, and
that there are often more stable and economical ways of actually
computing a roughness penalty smooth. The published literature and
algorithms on roughness penalty smoothing provide further details.

<!-- PageBreak -->

<!-- PageNumber="65" -->
<!-- PageHeader="4.3 The regularized basis approach" -->


#### 4.3.3 Some properties of the estimates

The first term of (4.5) is identical in structure to the error sum
of squares criterion $Q \left( c \right)$ defined in (3.6), except that both sets of
basis functions are used in the expansion. The second term, however,
modifies the basis function expansion problem by penalizing the
roughness or size in some sense of the w-component of the expansion.

The size of the penalty on the w-component is controlled by the
smoothing parameter $\lambda .$ In the limit as $\lambda \rightarrow 0 ,$ no penalty whatsoever
is applied, and the estimates obtained by minimizing the criterion
$\mathrm { P E N S S E } _ { \lambda } ,$ revert to those obtained by an ordinary basis expansion in
the combined basis of $\phi _ { j }$ and $\psi _ { k } .$ At the other extreme, when $\lambda \rightarrow \infty ,$
the penalty is so severe that w-contribution to the roughness penalty
is forced to zero; if $R$ is strictly positive-definite, we obtain the basis
function estimate corresponding to the basis $\left\{ \phi _ { j } \right\}$ alone. If $\mathbb{R}$ is not
strictly positive-definite, then a contribution $x _ { R }$ from the $\left\{ \psi _ { k } \right\}$ basis is
allowed, provided that it satisfies $L x _ { R } \left( s \right) = 0$ for all $S$ s.

It is instructive to study the minimizing values of the coefficient
vectors $d$ and $c .$ The smoothing matrix then becomes

$$S _ { \lambda } = \mathrm { P } _ { \phi } + \mathrm { Q } _ { \psi , \lambda }$$

where

$$Q _ { \psi , \lambda } = \Psi \left( \Psi ^ { \prime } \mathrm { Q } _ { \phi } \Psi + \lambda \mathrm { R } \right) ^ { - 1 } \Psi ^ { \prime } \mathrm { Q } _ { \phi } .$$
(4.8)

From this we can see that $\mathrm { Q } _ { \mathfrak{C} } { } _ { , \lambda }$ is a kind of 'subprojection' matrix in
the metric of the projection $\mathrm { Q } _ { \phi }$ in that it has the structure of a true
projection except for a perturbation of $\Psi ^ { \prime } \mathrm { Q } _ { \phi } \Psi$ by $\lambda \mathbb{R} .$ This elaborates
the way in which the regularized basis approach provides a continuous
range of choices between low-dimensional basis expansion in terms of
the functions $\phi _ { j }$ and a high-dimensional expansion also making use of
the functions $\psi _ { k } .$


#### 4.3.4 Relationship to the roughness penalty approach

We conclude with some remarks about the connections between the
regularized basis method and the method discussed in Section 4.2.4
above. Firstly, to minimize the residual sum of squares penalized by
$\| L x \| ^ { 2 } ,$ we need not specify any functions at all in the $\phi _ { j }$ part of the
basis, but merely ensure that $\left\{ \psi _ { k } \right\}$ is a suitable basis for the functions
of interest. In the original spline smoothing context, with $L = D ^ { 2 } ,$
we can take the $\left\{ \psi _ { k } \right\}$ to be a B-spline basis with knots at the data
points, and, by using suitable methods of numerical linear algebra, we

<!-- PageBreak -->

<!-- PageNumber="66" -->
<!-- PageHeader="4. The roughness penalty approach" -->

can obtain a stable $O \left( n \right)$ algorithm for spline smoothing; this is the
approach of the S-PLUS function smooth. spline.

Secondly, if we wish to prescribe a particular ultrasmooth class $\mathcal{F} _ { 0 } ,$
the regularized basis approach allows us to choose basis functions $\phi _ { j }$
to span $\mathcal{F} _ { 0 } ,$ and then allow $R$ to be any appropriate strictly positive-
definite matrix. In this way, the choice of the ultrasmooth class is
decoupled from the way that roughness is measured.

<!-- PageBreak -->


## 5 The registration and display of functional data


### 5.1 Introduction

We can now assume that our observations are in functional form, and
proceed to consider methods for their analysis. In this chapter, we
consider aspects of the initial processing and display of functional data
that raise issues specific to the functional context. Our main emphasis
is on registration of the data, taking into account transformations of
observed functions $x$ that involve changes in the argument $t$ as well
as in the values $x \left( t \right)$ themselves. In the latter part of the chapter,
we consider various descriptive statistics and graphical displays of
functional data.

Figure 1.2 illustrates a problem that can frustrate even the simplest
analyses of replicated curves. Ten records of the acceleration in
children's height show, individually, the salient features of growth:
The large deceleration during infancy is followed by a rather complex
but small-sized acceleration phase during late childhood. Then the
dramatic acceleration-deceleration pulses of the pubertal growth spurt
finally give way to zero acceleration in adulthood. But the timing of
these salient features obviously varies from child to child, and ignoring
this timing variation in computing a cross-sectional mean function,
shown by the heavy dashed line in Figure 1.2, can result in an estimate
of average acceleration that does not resemble any of the observed
curves. In this case, the mean curve has less variation during the

<!-- PageBreak -->

<!-- PageNumber="68" -->
<!-- PageHeader="5. The registration and display of functional data" -->

pubertal phase than any single curve, and the duration of the mean
pubertal growth spurt is rather larger than that of any individual curve.

The need to transform curves by transforming their arguments,
which we call curve registration, can be motivated as follows. The rigid
metric of physical time may not be directly relevant to the internal
dynamics of many real-life systems. Rather, there can be a sort of
biological or meteorological time scale that can be nonlinearly related
to physical time, and can vary from case to case. Human growth, for
example, is the consequence of a complex sequence of hormonal events
that do not happen at the same rate for every child. Similarly, weather
is driven by ocean currents, reflectance changes in land surfaces, and
other factors timed differently for different spatial locations.

Put more abstractly, the values of two or more function values $x _ { i } \left( t _ { j } \right)$
can in principle differ because of two types of variation. The first is the
more familiar vertical variation, or range variation, caused by the fact
that $x _ { 1 } \left( t \right)$ and $x _ { 2 } \left( t \right)$ may simply differ at points of time $t$ at which they
are compared. But they may also exhibit domain variation in the sense
that functions $x _ { 1 }$ and $x _ { 2 }$ should not be compared at the same time $t$ t.
Instead, to compare the two functions, the time scale itself has to be
distorted or transformed. For instance, the intensity of the pubertal
growth spurts of two children should be compared at their respective
ages of peak velocity rather than at any fixed age.

We now look at several types of curve registration problems,
beginning with the problem of simply translating or shifting the values
of $t$ by a constant amount $\delta .$ Then we discuss landmark registration,
which involves transforming $t$ nonlinearly to line up important features
or landmarks for all curves. Finally, we look at a more general method
for curve registration.


### 5.2 Shift registration


#### 5.2.1 Types of alignment

The pinch force data illustrated in Figure 1.7 are an example of a
set of functional observations that must be aligned by shifting each
horizontally before any meaningful cross-curve analysis is possible.
This can happen because the time when the recording process begins is
arbitrary, and is unrelated to the beginning of the interesting segment
of the data, the period over which the measured squeeze actually takes
place.

<!-- PageBreak -->

<!-- PageNumber="69" -->
<!-- PageHeader="5.2 Shift registration" -->

Let the interval $T$ over which the functions are to be registered
be $\left[ T _ { 1 } , T _ { 2 } \right] .$ We also need to assume that each sample function $x _ { i }$ is
available for some region beyond each end of $T .$ The pinch force data,
for example, are observed for substantial periods both before and after
the force pulse that we wish to study. In the case of periodic data
such as the Canadian temperature records, this requirement is easily
met since one can wrap the function around by using the function's
behaviour at the opposing end of the interval.

We are actually interested in the values

$$x _ { i } ^ { * } \left( t \right) = x _ { i } \left( t + \delta _ { i } \right) ,$$

where the shift parameter $\delta _ { i }$ is chosen to align the curves appropriately.
For the pinch force data, the size of $\delta _ { i }$ is of no real interest, since it
merely measures the gap between the initialization of recording and
the beginning of a squeeze. Silverman (1995) refers to this situation, in
which a shift parameter must be accounted for but is of no real interest,
as a nuisance effects problem.

The Canadian temperature data present a curve alignment problem
of a somewhat different nature. As Figure 5.1 indicates, two
temperature records, such as those for St. John's, Newfoundland, and
Edmonton, Alberta, can differ noticeably in terms of the phase or timing
of key events, such as the lowest mean temperature and the timing
of spring and autumn. In this case, the shifts that would align these
two curves vertically are of intrinsic interest, and should be viewed as
a component of variation that needs careful description. It turns out
that continental stations such as Edmonton have seasons earlier than
marine stations such as St John's, because of the capacity of oceans
to store heat and to release it slowly. In fact, either station's weather
would have to be shifted by about three weeks to align the two.

When, as in the temperature data case, the shift is an important
feature of each curve, we characterize its estimation as a random effects
problem. Silverman (1995) also distinguishes a third and intermediate
fixed effects case in which the shift must be carried out initially, and
although not discarded completely once the the functions $x _ { i } ^ { * } ,$ have been
constructed, is nevertheless only of tangential interest.


#### 5.2.2 Estimating the alignment

The basic mechanics of estimating the shifts $\delta _ { i }$ are the same, whether
they are considered as nuisance or random effects. The differences
become important when we consider the analysis in subsequent
chapters, because in the random effects case (and, to some extent,

<!-- PageBreak -->

<!-- PageNumber="70" -->
<!-- PageHeader="5. The registration and display of functional data" -->


<figure>
<figcaption>FIGURE 5.1. Temperature records for two weather stations where the timing of the seasons differs.</figcaption>

20

Mean temperature (deg C)

10

0

-40 -30 -20 -10

St. John's
Edmonton

0

5

10

15

Month

</figure>


the fixed effects case) the $\delta _ { i }$ enter the analysis. However, for present
purposes we concentrate on the pinch force data as an example.

Estimating a shift or an alignment requires a criterion that defines
when several curves are properly registered. One possibility is to
identify a specific feature or landmark for a curve, and shift each curve
so that this feature occurs at a fixed time. The time of the maximum
of the smoothed pinch force is an obvious landmark. Note that this
might also be expressed as the time when the first derivative crosses
zero with negative slope. Landmarks are often more easily identifiable
at the level of some derivative.

However, registration by landmark or feature alignment has some
potentially undesirable aspects. The location of the feature may be
ambiguous for certain curves, and if the alignment is only of a
single point, variations in other regions may be ignored. For example,
if we were to register the two temperature curves by aligning the
midsummers, the midwinters might still remain seriously out of phase.

Instead, we can define a global registration criterion for identifying
shift $\delta _ { i }$ for curve $i$ as follows. First we estimate an overall mean function
$\widehat { \mu } \left( s \right)$ for $\sin T$ . If the individual functional observations $x _ { i }$ are smooth,
it usually suffices to estimate $\widehat { \mu }$ by the sample average $\mathfrak{K} .$ However, we
wish to be able to evaluate derivatives of $\widehat { \mu } ,$ and so more generally we
want to smooth the overall estimate using one of the methods described

<!-- PageBreak -->

<!-- PageNumber="71" -->
<!-- PageHeader="5.2 Shift registration" -->

in Chapters 3 and 4. We can now define our global registration criterion
by

$$R E C S S E = \sum _ { i = 1 } ^ { N } \int _ { T } \left[ x _ { i } \left( s + \delta _ { i } \right) - \widehat { \mu } \left( s \right) \right] ^ { 2 } d s$$
$$= \sum _ { i = 1 } ^ { N } \int _ { T } \left[ x _ { i } ^ { * } \left( s \right) - \widehat { \mu } \left( s \right) \right] ^ { 2 } d s .$$

(5.1)

Thus, our measure of curve alignment is the integrated or global sum
of squared vertical discrepancies between the shifted curves and the
sample mean curve.

The target function for transformation in (5.1) is the unregistered
cross-sectional estimated mean $\widehat { \mu } .$ But of course one of the goals
of registration is to produce a better estimate of this same mean
function. Therefore we expect to proceed iteratively. Beginning with the
unregistered cross-sectional estimated mean, argument values for each
curve are shifted so as to minimize REGSSE, then the estimated mean $\widehat { \mu }$
is updated by re-estimating it from the registered curves $x _ { i } ^ { * } ,$ and a new
iteration is then undertaken using this revised target. This procedure of
estimating a transformation by transforming to an iteratively updated
average is often referred to as the Procrustes method. In practice,
we have found that the process usually converges within one or two
iterations.

A change of variable for each integration results in an alternative
version of the criterion that may be more convenient for computational
purposes:

$$R E C S S E = \sum _ { i = 1 } ^ { N } \int _ { T _ { 1 } + \delta _ { i } } ^ { T _ { 2 } + \delta _ { i } } \left[ X _ { i } \left( s \right) - \widehat { \mu } \left( s - \delta _ { i } \right) \right] ^ { 2 } d s .$$
(5.2)


#### 5.2.3 Using the Newton-Raphson algorithm

We can estimate a specific shift parameter $\delta _ { i }$ iteratively by using
a modified Newton-Raphson algorithm for minimizing REGSSE. This
procedure requires derivatives of REGSSE with respect to the $\delta _ { i } .$ If
we assume that the differences between $x _ { i } ^ { * } ,$ and $\widehat { \mu }$ at the ends of the
interval can be ignored (this is exactly true in the periodic case, and
often approximately true in the nonperiodic case if the effects of real
interest are concentrated in the middle of the interval), then

$$\frac { \partial } { \partial \delta _ { i } } R E C S S E = - \int _ { T _ { 1 } + \delta _ { i } } ^ { T _ { 2 } + \delta _ { i } } \left\{ x _ { i } \left( s \right) - \widehat { \mu } \left( s - \delta _ { i } \right) \right\} D \widehat { \mu } \left( s - \delta _ { i } \right) d s$$

<!-- PageBreak -->

<!-- PageNumber="72" -->
<!-- PageHeader="5. The registration and display of functional data" -->

$$= \int _ { T } \left\{ \widehat { \mu } \left( s \right) - x _ { i } ^ { * } \left( s \right) \right\} D \widehat { \mu } \left( s \right) d s$$

and

$$\frac { \partial ^ { 2 } } { \partial \delta _ { i } ^ { 2 } } R E C S S E = - \int _ { T } \left\{ x _ { i } ^ { * } \left( s \right) - \widehat { \mu } \left( s \right) \right\} D ^ { 2 } \widehat { \mu } \left( s \right) d s$$
$$+ \int _ { T } \left\{ D \widehat { \mu } \left( s \right) \right\} ^ { 2 } d s .$$
(5.3)

The modified Newton-Raphson algorithm works as follows:

Step 0: Begin with some initial shift estimates $\delta _ { i } ^ { \left( 0 \right) } ,$ perhaps by
aligning with respect to some feature, or even $\delta _ { i } ^ { \left( 0 \right) } = 0 .$ But the
better the initial estimate, the faster and more reliably the algorithm
converges. Complete this step by estimating the average $\widehat { \mu }$ of the
shifted curves, using a method that allows the first two derivatives
of $\widehat { \mu }$ to give good estimates of the corresponding derivatives of the
population mean, such as local polynomial regression of degree four,
or roughness penalty smoothing with an integrated squared fourth
derivative penalty.

Step $v ,$ for $v = 1 , 2 , \ldots :$ Modify the estimate $\delta _ { i } ^ { \left( \nu - 1 \right) }$ on the previous
iteration by

$$\delta _ { i } ^ { \left( v \right) } = \delta _ { i } ^ { \left( v - 1 \right) } - \alpha \frac { \left( \partial / \partial \delta _ { i } \right) R E G S E } { \left( \partial ^ { 2 } / \partial \delta _ { i } ^ { 2 } \right) R E C S S E }$$

where $\alpha$ is a step-size parameter that can sometimes simply be set to
one. It is usual to drop the first term (5.3) in the second derivative of
REGSSE since it vanishes at the minimizing values, and convergence
without this term tends to be more reliable when current estimates are
substantially far from the minimizing values. Once the new shifts are
estimated, recompute the estimated average $\widehat { \mu }$ of the shifted curves.

Although the algorithm can in principle be iterated to convergence,
and although convergence is generally fast, we have found that a single
iteration is often sufficient with reasonable initial estimates. For the
pinch force data, we initially aligned the smoothed curves by locating
the maximum of each curve at 0.1 seconds. The shifts involved ranged
from -20 to 50 milliseconds. We then carried out a single Newton-
Raphson update $\left( v = 1 \right.$ above) where the range $T$ of integration was
from 23 to 251 milliseconds. The changes in the $\delta _ { i }$ ranged from -3 to
2 milliseconds, and after this update, a second iteration did not yield

<!-- PageBreak -->

<!-- PageNumber="73" -->
<!-- PageHeader="5.3 Feature or landmark registration" -->


<figure>
<figcaption>FIGURE 5.2. The pinch force curves aligned by minimizing the Procrustes criterion REGSSE.</figcaption>

12

10

8

Force

9

\+

2

0

0.0 0.05 0.10 0.15 0.20 0.25 0.30

Time (sec)

</figure>


any changes larger than a millisecond. The aligned curves are shown in
Figure 5.2.

Kneip and Engel (1988) use linear transformations of $t ,$ both
shift and scale changes, as part of a technique termed self-modeling
nonlinear regression that attempts to estimate both parametric and
nonparametric components of variation among several curves. Kneip
and Engel (1995) use such shift-scale transformations to identify
'shape-invariant features' of curves, which remain unaltered by these
changes in $t .$


### 5.3 Feature or landmark registration

A landmark or a feature of a curve is some characteristic that one can
associate with a specific argument value $t$ t. These are typically maxima,
minima, or zero crossings of curves, and may be identified at the level
of some derivatives as well as at the level of the curves themselves.

We now turn to the more general problem of estimating a
possibly nonlinear transformation $h _ { i }$ of $t ,$ and indicate how we can
use landmarks to estimate this transformation. Coincidentally, the
illustrative example we use shows how vector-valued functional data

<!-- PageBreak -->

<!-- PageNumber="74" -->
<!-- PageHeader="5. The registration and display of functional data" -->


<figure>
<figcaption>FIGURE 5.3. Twenty replications of "fda" written by one of the authors.</figcaption>

40

Y coordinate

Ida

20

0

-20

-40

-40

-20

0

20

40

X coordinate

</figure>


can be handled by obvious extensions of methods for scalar-valued
functions.

The landmark registration process requires, for each curve $x _ { i } ,$ the
identification of the argument values $t _ { i f } , f = 1 , \ldots , F$ associated with
each of $F$ features. The goal is to construct a transformation $h _ { i }$ for each
curve such that the registered curves with values

$$x ^ { * } \left( t \right) = x _ { i } \left[ h _ { i } \left( t \right) \right]$$

have more or less identical argument values for any given landmark.

For example, consider the 20 replications of the letters "fda" in
Figure 5.3. Each sample of handwriting was obtained by recording the
position of $a$ pen at a sampling rate of 600 times per second. There was
some preprocessing to make each script begin and end at times 0 and
2.3 seconds, and to compute coordinates at the same 1,401 equally-
spaced times. Each curve $x _ { i }$ in this situation is vector-valued, since two
spatial coordinates are involved, and we use $\mathrm { S c r i p t X } _ { i }$ and $\mathrm { S c r i p t Y } _ { i }$ to
designate the $X -$ and Y-coordinates, respectively.

Not surprisingly, there is some variation from observation to
observation, and one goal is to explore the nature of this variation.
But we want to take into account that variation in the "f," for example,
can be of two sorts. There is temporal variation because timing of the
top of the upper loop, for example, is variable. Although this type of
variation would not show up in the plots in Figure 5.3, it may still be

<!-- PageBreak -->

<!-- PageNumber="75" -->
<!-- PageHeader="5.3 Feature or landmark registration" -->


<figure>
<figcaption>FIGURE 5.4. The average length of the acceleration vector for the 20 handwriting samples. The characters identify the 15 features used for landmark registration.</figcaption>

RMS acceleration

1000 2000 3000 4000 5000

A

0

0.0

0.5

1.0

1.5

2.0

Time

</figure>


an important aspect of the way these curves vary. On the other hand,
there is variation in the way the shape of each letter is formed, and this
is obvious in the figure.

We estimated the accelerations or second derivatives of the two
coordinate functions $D ^ { 2 } \mathrm { S c r i p t } X _ { i }$ and $D ^ { 2 } S c r i p t Y _ { i }$ by the local
polynomial method described in Chapter 3. Figure 5.4 displays the
average length of the acceleration vector

$$\sqrt { \left( D ^ { 2 } \mathrm { S c r r i p t } X _ { i } \right) ^ { 2 } + \left( D ^ { 2 } S c r i p t Y _ { i } \right) ^ { 2 } }$$

and we note that there are 15 clearly identified maxima, indicating
points where the pen is changing direction. We also found that these
maxima were easily identifiable in each record, and we were able to
determine the values of $t _ { i f }$ corresponding to them by just clicking on
the appropriate points in a plot produced by $S$ S-PLUS. Figure 5.5 shows
the first curve with these 15 features labelled, and we can see that
landmarks labelled "4" and $A ^ { \prime \prime }$ mark the boundaries between letters.
Figure 5.6 plots the values of the landmark timings $t _ { i f }$ against the
corresponding timings $t _ { 0 f }$ for the mean function. We were interested
to see that the variability of the landmark timings was rather larger for
the initial landmarks than for the later ones, and we were surprised by
how small the variability was for all of them.

<!-- PageBreak -->

<!-- PageNumber="76" -->
<!-- PageHeader="5. The registration and display of functional data" -->

Record 1


<figure>
<figcaption>FIGURE 5.5. The first handwriting curve with the location of the 15 landmarks indicated by the characters used in Figure 5.4.</figcaption>

40

1

9

20

Y coordinate

$2$

75

0

3

4

8

A

-20

-40

2

-40

-20

0

20

40

$X \quad c o o r d i n a t e$

</figure>


<figure>
<figcaption>FIGURE 5.6. The timings of the landmarks for all 20 scripts plotted against the corresponding timings for the mean curve.</figcaption>

2.0

Registered time

1.5

f

d

!

a

1.0

0.5

0.0

0.0

0.5

1.0

1.5

2.0

Chronological time

</figure>


<!-- PageBreak -->

<!-- PageNumber="77" -->
<!-- PageHeader="5.3 Feature or landmark registration" -->

Record 1


<figure>
<figcaption>FIGURE 5.7. The time-warping function $h _ { 1 }$ estimated for the first record that registers its features with respect to the mean curve.</figcaption>

2.0

Transformed time

1.5

1.0

0.5

0.0

0.0

0.5

1.0

1.5

2.0

Time

</figure>


The identification of landmarks enabled us to compare the $X -$ and $\mathrm { Y }$
coordinate values for the 20 curves at the landmark times, but of course
we also wanted to make comparisons at arbitrary points between
landmarks. This required the computation of a function $h _ { i }$ for each
curve, called a time-warping function in the engineering literature, with
the properties

· $h _ { i } \left( 0 \right) = 0$

· $h _ { i } \left( 2 . 3 \right) = 2 . 3$

· $h _ { i } \left( t _ { 0 f } \right) = t _ { i f } , f = 1 , \ldots , 1 5$

· $h _ { i }$ is strictly monotonic: $s < t$ implies that $h _ { i } \left( s \right) < h _ { i } \left( t \right) .$

The values of the adjusted curves at time $t$ are $\mathrm { S c r i p t X } \left[ h _ { i } \left( t \right) \right]$ and
$\mathrm { S c r i p t Y } \left[ h _ { i } \left( t \right) \right] .$ In all the adjusted curves, the landmarks each occur at
the same time as in the mean function. In addition, the adjusted curves
are also more or less aligned between landmarks. In this application,
we merely used linear interpolation for time values between the points
$\left( t _ { 0 f } , t _ { i f } \right)$ (as well as (0,0) and (2.3,2.3)) to define the time-warping
function $h _ { i }$ for each curve. We introduce more sophisticated notions
in the next section. Figure 5.7 shows the warping function computed in
this manner for the first script record. Because $h _ { 1 }$ is below the diagonal

<!-- PageBreak -->

<!-- PageNumber="78" -->
<!-- PageHeader="5. The registration and display of functional data" -->


<figure>
<figcaption>FIGURE 5.8. The solid line is the mean of the registered "fda" curves, and the dashed line is the mean of the unregistered curves.</figcaption>

Y coordinate

Lda

20

0

-20

-30

-20

10

20

30

$X \quad c o o r d i n a t e$

</figure>


line in the region of "f," the aligned time $h _ { 1 } \left( t \right)$ is earlier than the actual
time of features, and hence the actual times for curve 1 are retarded
with respect to the mean curve.

We can now recompute the mean curve by averaging the registered
curves. The result is in Figure 5.8, shown along with the mean for the
unregistered data. Although the differences are not dramatic, as we
might expect given the mild curvature in $h _ { 1 } ,$ the upper and lower loops
of the "f" are now more pronounced, and do represent the original
curves substantially better.

Landmark registration has been studied in depth by Kneip and
Gasser (1992), and their paper contains various technical details on the
asymptotic behaviour of landmark estimates and warping functions
estimated from them. They refer to the process of averaging a set of
curves after registration as structural averaging, and their subsequent
papers on growth curves (Gasser et al., 1990, 1991a,b) are important
applications of this process.

For further information on the study of landmarks, the reader is
referred to Gasser and Kneip (1995), who refer to a landmark as
a 'structural feature', its location as a 'structural point', and to the
distribution of landmark locations along the $t$ axis as 'structural
intensity'. They have developed some useful tools for estimating
landmark distribution or structural intensity, and, indeed, the study

<!-- PageBreak -->

<!-- PageNumber="79" -->
<!-- PageHeader="5.4 More general transformations" -->

of the characteristics and distribution of curve characteristics is
an important part of functional data analysis in many applications.
Another source of much information on the study of landmarks and
their use in registration is Bookstein (1991).


### 5.4 More general transformations


#### 5.4.1 Families of transformations

In this section, we consider more general transformations and draw
together some of the ideas of Sections 5.2 and 5.3. Let an arbitrary
transformation of argument $t$ be indicated by $h \left( t \right) .$ The function $h$ has
the requirements of being strictly increasing or monotonic, and also
differentiable up to a certain order. The general registration problem is
one of estimating such an $h _ { i }$ for each curve $x _ { i } ,$ such that the registered
curves

$$x _ { i } ^ { * } \left( t \right) = x _ { i } \left[ h _ { i } \left( t \right) \right]$$

satisfy some criterion, such as having aligned local features or
minimizing a measure like REGSSE. Our discussion concentrates almost
exclusively on the minimization of criteria related to REGSSE, but
the ideas can be extended to other criteria of goodness of fit of a
transformed functional observation to an overall mean.

The transformation family $h$ may be parametric in character, an
example of which is the translation $h _ { i } \left( t \right) = t + \delta _ { i } ,$ or the linear
transformation $h _ { i } \left( t \right) = \left( t + \delta _ { i } \right) \beta _ { i } , \beta _ { i } > 0 .$ For each record i, let the
vector $Y _ { i }$ contain the parameters, such as $\delta _ { i }$ and $\beta _ { i } ,$ defining the
transformation, and let $h _ { i } \left( t \right)$ indicate the value of the transformation
for parameter vector value $Y _ { i } .$

In this case, the Procrustes method is defined as the iterative
minimization of

$$R E C S S E = \sum _ { i = 1 } ^ { N } \int _ { T } \left[ x _ { i } \left\{ h _ { i } \left( s \right) \right\} - \widehat { \mu } \left( s \right) \right] ^ { 2 } d s .$$
(5.4)

with $\widehat { \mu } \left( s \right)$ re-estimated from the curves $x _ { i } \left\{ h _ { i } \left( s \right) \right\}$ at each stage. The
Newton-Raphson update of the parameter estimates is defined as
above; the partial derivatives are

$$\frac { \partial } { \partial y _ { i q } } R E C S S E = \int _ { T } \left[ x _ { i } \left\{ h _ { i } \left( s \right) \right\} - \widehat { \mu } \left( s \right) \right] D x _ { i } \left[ h _ { i } \left( s \right) \right] \frac { \partial h _ { i } \left( s \right) } { \partial y _ { i q } } d s$$

<!-- PageBreak -->

<!-- PageNumber="80" -->
<!-- PageHeader="5. The registration and display of functional data" -->

and

$$\frac { \partial ^ { 2 } } { \partial y _ { i q } ^ { 2 } } R E C S S E = \int _ { T } \left[ x _ { i } \left\{ h _ { i } \left( s \right) \right\} - \widehat { \mu } \left( s \right) \right] D ^ { 2 } x _ { i } \left[ h _ { i } \left( s \right) \right] \frac { \partial ^ { 2 } h _ { i } \left( s \right) } { \partial y _ { i q } ^ { 2 } } d s$$
$$- \int _ { T } \left\{ D x _ { i } \left( h _ { i } \left( t ; y _ { i } \right) \right) \frac { \partial h _ { i } \left( s \right) } { \partial y _ { i q } } \right\} ^ { 2 } d s$$

The function $D x _ { i } \left[ h _ { i } \left( s \right) \right]$ is the derivative $d x _ { i } \left( t \right) / d t$ evaluated at
$t = h _ { i } \left( s \right) ,$ and similarly for $D ^ { 2 } x _ { i } \left[ h _ { i } \left( s \right) \right] .$ These values may usually
be estimated by a suitable interpolation or smoothing method. It is
often numerically more stable to approximate the second derivative of
REGSSE by dropping the first term on the right side of (5.5).


#### 5.4.2 Fitting transformations using regularization

Ramsay (1996b) and Ramsay and Li (1996) have developed the fitting
of a general and flexible family of warping functions $h _ { i }$ making use of
a regularization technique. The results are sketched here; for further
details see the original papers.

Suppose that the interval $T$ of interest is $\left[ 0 , T \right] ,$ and that the
transformation functions $h$ have integrable second derivative in
addition to being strictly increasing. Every such function can be
described by the homogeneous linear differential equation

$$D ^ { 2 } h = w D h$$
(5.6)

for some suitable weight function $w .$ To see this, note that a strictly
monotonic function has a nonzero derivative, a twice-differentiable
function has a second derivative, and therefore the weight function $w$
is trivially $D ^ { 2 } h / D h .$ The weight function $w \left( s \right)$ is a measure of relative
curvature of $h \left( s \right)$ in the sense that the conventional curvature measure
$D ^ { 2 } h \left( s \right)$ is assessed relative to the slope $D h .$

The differential equation (5.6) has the general solution

$$h \left( t \right) = C _ { 0 } + C _ { 1 } \int _ { 0 } ^ { t } \left[ \exp \int _ { 0 } ^ { u } w \left( v \right) d v \right] d u$$
$$= C _ { 0 } + C _ { 1 } \left( D ^ { - 1 } \exp D ^ { - 1 } w \right) \left( t \right)$$

(5.7)

where $D ^ { - 1 }$ is the integration operator (with lower limit of integration 0
and variable upper limit), and $C _ { 0 }$ and $C _ { 1 }$ are arbitrary constants. When
$w$ is constant, $h \left( t \right) = C _ { 0 } + C _ { 1 } \exp \left( w t \right) ,$ so that an exponential function
has constant relative curvature in this sense. A straight line is of course
implied by $w \left( s \right) = 0$ for all $s .$ In general, we impose the constraints

<!-- PageBreak -->

<!-- PageNumber="81" -->
<!-- PageHeader="5.4 More general transformations" -->

$h \left( 0 \right) = 0$ and $h \left( T \right) = T ,$ implying that

$$C _ { 0 } = 0 \text { and } C _ { 1 } = T / \left[ D ^ { - 1 } \exp D ^ { - 1 } w \left( T \right) \right]$$

and that the function $h$ depends only on the weight function $w .$

We can regularize or smooth the estimated warping functions $h _ { i }$ by
augmenting the criterion (5.4) as follows:

$$\mathrm { R E C S E } _ { \lambda } \left( h _ { 1 } , \ldots , h _ { n } \right) = \mathrm { R E C S E } + \lambda \sum _ { i } \int w _ { i } ^ { 2 } \left( t \right) d t ,$$
(5.8)

where $w _ { i } = D ^ { 2 } h _ { i } / D h _ { i } .$ Larger values of the smoothing parameter $\lambda$
shrink the relative curvature functions $w _ { i }$ to zero, and therefore shrink
the $h _ { i } \left( t \right)$ to $t .$


#### 5.4.3 A regularized basis approach

In principle, we could consider the minimization of $\mathrm { R E C S S E } _ { \lambda }$ without
any further constraints on the functions $h _ { i } ,$ but it is computationally
much simpler to restrict attention to a particular high-dimensional
family of transformations for which the minimization is tractable. To
this end, we can use a linear B-spline basis for $D ^ { - 1 } w .$

Beginning with a set of discrete break points $\tau _ { k } , k = 0 , \ldots , K$
satisfying $0 = \tau _ { 0 } < \tau _ { 1 } < \ldots < \tau _ { K } = T ,$ let

$$\Delta _ { k } = \tau _ { k + 1 } - \tau _ { k } , k = 0 , \ldots , K - 1 ,$$

and for notational simplicity let $\Delta _ { k }$ also indicate the interval $\left[ \tau _ { k } , \tau _ { k + 1 } \right) .$
Define $\mathrm { T r i a n g } _ { k }$ to be the triangle or 'hat' function

$$\mathrm { T r i a n g } _ { k } \left( t \right) = \left\{ \begin{array}{} { \left( t - \tau _ { k - 1 } \right) / \Delta _ { k - 1 } } & { \text { if } t \in \Delta _ { k - 1 } } \\ { \left( \tau _ { k + 1 } - t \right) / \Delta _ { k } } & { \text { if } t \in \Delta _ { k } } \\ { 0 } & { \text { otherwise } } \end{array} \right.$$
(5.9)

for $k = 1 , \ldots , K .$ (For $k = K$ there is no interval $\Delta _ { K }$ to worry about.)

For any particular weight function $w ,$ let $c _ { k } = D ^ { - 1 } w \left( \tau _ { k } \right) ,$ implying
$D ^ { - 1 } w = \sum _ { k = 1 } ^ { K } c _ { k } .$ In each interval $\Delta _ { k } ,$ the weight function $w$
takes the constant value $w _ { k } = \left( c _ { k + 1 } - c _ { k } \right) / \Delta _ { k } ,$ and so, if required, we
can calculate the penalty

$$\int _ { 0 } ^ { T } w \left( t \right) ^ { 2 } d t = \sum _ { k = 0 } ^ { K - 1 } \Delta _ { k } ^ { - 1 } \left( c _ { k + 1 } - c _ { k } \right) ^ { 2 } .$$

The integrals in (5.7) can be computed explicitly. For $t \in \Delta _ { k }$

$$h \left( t \right) = h \left( \tau _ { k } \right) + C _ { 1 } w _ { k } ^ { - 1 } \exp \left[ c _ { k } + w _ { k } \left( t - \tau _ { k } \right) \right]$$
$$D h \left( t \right) = C _ { 1 } \exp \left[ c _ { k } + w _ { k } \left( t - \tau _ { k } \right) \right] ,$$
and

(5.10)

<!-- PageBreak -->

<!-- PageNumber="82" -->
<!-- PageHeader="5. The registration and display of functional data" -->


<figure>
<figcaption>FIGURE 5.9. The left panel contains the estimated time warping functions $h _ { i }$ for the ten height acceleration curves in Figure 1.2. The right panel displays the registered curves.</figcaption>

Transformed age

4 6 8 10 12 14 16 18

Height acceleration

-6 -4 -2 0 2 4

4 6 8 10 12 14 16 18
Age

4 6 8 10 12 14 16 18
Transformed age

</figure>


where, as already indicated, $C _ { 1 }$ is a normalizing constant yielding
$h \left( T \right) = T .$

For any particular fitting criterion, we can estimate the coefficients $c _ { k }$
by a numerical procedure. Computation of the value $t$ corresponding
to $h \left( t \right) = z$ for a given $z$ is often required, in other words the value of
the inverse function $h ^ { - 1 } \left( z \right) .$ Evaluation of $h ^ { - 1 }$ is accomplished by first
identifying the interval $\Delta _ { k }$ such that $z = h \left( t \right) ,$ $t \in \Delta _ { k }$


#### 5.4.4 Registering the height acceleration curves

The ten acceleration functions in Figure 1.2 were registered by the
Procrustes method and the regularized basis expansion method as
set out in Section 5.4.3. The interval $T$ was taken to be $\left[ 4 , 1 8 \right]$ with
time measured in years. The break values $\tau _ { k }$ defining the monotonic
transformation family (5.10) were 4, 7, 10, 12, 14, 16 and 18 years,
and the curves were registered over the interval [4,18] using criterion
(5.8) with $\lambda = 0 . 0 0 1 .$ A single Procrustes iteration produced the
results displayed in Figure 5.9. The left panel displays the ten warping
functions $h _ { i } ,$ and the right panel shows the curve values $x _ { i } \left[ h _ { i } \left( t \right) \right] .$
Figure 5.10 compares the unregistered and registered cross-sectional
means. We see that the differences are substantial, and moreover that
the mean of the registered function tends to resemble most of the
sample curves much more closely.

<!-- PageBreak -->

<!-- PageNumber="83" -->
<!-- PageHeader="5.4 More general transformations" -->


<figure>
<figcaption>FIGURE 5.10. The cross-sectional means of the registered and unregistered height acceleration curves displayed in Figure 1.2.</figcaption>

Mean height acceleration

2

0

-2

\- Registered
Unregistered

4

4

6 8 10 12 14 16 18

Age

</figure>


#### 5.4.5 Some cautionary remarks

In general it is not clear that variation in the amplitude of curves
can be cleanly separated from the variation that the registration
process aims to account for. It is easy to construct examples where
a registration function $h$ that is allowed to be highly nonlinear can
remove variation that is clearly of an amplitude nature. This problem
of lack of identifiability of the two types of variation, horizontal and
vertical, is perhaps less of a concern if only linear transformations are
permitted, and is also not acute for landmark registration, where the
role of the transformation is only to align curve features.

But if flexible families of monotonic transformations such as those
described above are used in conjunction with a global fitting criterion
such as REGSSE, two pieces of practical advice are offered. First,
allow transformations to differ from linear only with caution. Second,
first remove amplitude effects that can be accounted for by vertical
shifts or scale changes before registration, by centering and possibly
rescaling curves. Alternatively, it may be wiser to register the first or
second derivatives of curves, as we have done with the growth curves,
rather than the curves themselves, because differences in centering are
automatically removed when derivatives are taken.

<!-- PageBreak -->


## 6 Principal components analysis for functional data


### 6.1 Introduction

For many reasons, principal components analysis (PCA) of functional
data is a key technique to consider. First, our own experience is that,
after the preliminary steps of registering and displaying the data, the
user wants to explore that data to see the features characterizing
typical functions. Some of these features are expected to be there,
for example the sinusoidal nature of temperature curves, but other
aspects may be surprising. Some indication of the complexity of the
data is also required, in the sense of how many types of curves and
characteristics are to be found. Principal components analysis serves
these ends admirably, and it is perhaps also for these reasons that it
was the first method to be considered in the early literature on FDA.

Just as for the corresponding matrices in the classical multivariate
case, the variance-covariance and correlation functions can be difficult
to interpret, and do not always give a fully comprehensible presentation
of the structure of the variability in the observed data directly. The same
is true, of course, for variance-covariance and correlation matrices
in classical multivariate analysis. A principal components analysis
provides a way of looking at covariance structure that can be much
more informative and can complement, or even replace altogether, a
direct examination of the variance-covariance function.

<!-- PageBreak -->

<!-- PageNumber="86" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->

PCA also offers an opportunity to consider some issues that reappear
in subsequent chapters. For example, we consider immediately how
PCA is defined by the notion of a linear combination of function
values, and why this notion, at the heart of most of multivariate data
analysis, requires some care in a functional context. A second issue is
that of regularization; for many data sets, PCA of functional data is
more revealing if some type of smoothness is required of the principal
components themselves. We consider this topic in detail in Chapter 7.


### 6.2 Defining functional PCA


#### 6.2.1 PCA for multivariate data

The central concept exploited over and over again in multivariate
statistics is that of taking a linear combination of variable values,

$$f _ { i } = \sum _ { j = 1 } ^ { p } \beta _ { j } x _ { i j } , i = 1 , \ldots , N$$
(6.1)

where $\beta _ { j }$ is a weighting coefficient applied to the observed values $x _ { i j }$
of the jth variable. We can express (6.1) somewhat more compactly by
using the inner product notation introduced in Chapter 2:

$$f _ { i } = \langle \beta , x _ { i } \rangle , i = 1 , \ldots , N$$
(6.2)

where $\beta$ is the vector $\left( \beta _ { 1 } , \ldots , \beta _ { p } \right) ^ { \prime }$ and $x _ { i }$ is the vector $\left( x _ { i 1 } , \ldots , x _ { i p } \right) ^ { \prime } .$

In the multivariate situation, we choose the weights so as to highlight
or display types of variation that are very strongly represented in
the data. Principal components analysis can be defined in terms of
the following stepwise procedure, which defines sets of normalized
weights that maximize variation in the $f _ { i } :$

1\. Find the weight vector $E _ { 1 } = \left( E _ { 1 1 } , \ldots , E _ { p 1 } \right) ^ { \prime }$ for which the linear
combination values

$$f _ { i 1 } = \sum _ { j } 5 j _ { 1 } x _ { i j } = \langle 5 _ { 1 } , x _ { i } \rangle$$

have the largest possible mean square $N ^ { - 1 } \sum _ { i } f _ { i 1 } ^ { 2 }$ subject to the
constraint

$$\sum _ { j } E _ { j 1 } ^ { 2 } = \| \sum _ { 1 } \| ^ { 2 } = 1 .$$

<!-- PageBreak -->

<!-- PageHeader="6.2 Defining functional PCA 87" -->

2\. Carry out second and subsequent steps, possibly up to a limit of
the number of variables $p .$ On the $m t h$ step, compute a new weight
vector $E m$ with components $j m$ and new values $f _ { i m } = \langle 5 m , x _ { i } \rangle .$
Thus, the values $f _ { i m }$ have maximum mean square, subject to the
constraint $\| F _ { m } \| ^ { 2 } = 1$ and the $m \quad - \quad 1$ additional constraint(s)

$$\sum _ { j } S _ { j k } E _ { j m } = \langle 5 k , S m \rangle = 0 , k < m .$$

The motivation for the first step is that by maximizing the mean
square, we are identifying the strongest and most important mode
of variation in the variables. The unit sum of squares constraint on
the weights is essential to make the problem well defined; without
it, the mean squares of the linear combination values could be made
arbitrarily large. On second and subsequent steps, we seek the most
important modes of variation again, but require the weights defining
them to be orthogonal to those identified previously, so that they are
indicating something new. Of course, the amount of variation measured
in terms of $N ^ { - 1 } \sum _ { i } f _ { i m } ^ { 2 }$ will decline on each step. At some point, usually
well short of the maximum index $p ,$ we expect to lose interest in modes
of variation thus defined.

The definition of principal components analysis does not actually
specify the weights uniquely; for example, it is always possible to
change the signs of all the values in any vector $E m$ without changing
the value of the variance that it defines.

The values of the linear combinations $f _ { i m }$ are called principal
component scores and are often of great help in describing what these
important components of variation mean in terms of the characteristics
of specific cases or replicates.

To be sure, the mean is $a$ very important aspect of the data, but we
already have an easy technique for identifying it. Therefore, we usually
subtract the mean for each variable from corresponding variable values
before doing PCA. When this is done, maximizing the mean square
of the principal component scores corresponds to maximizing their
sample variance.


#### 6.2.2 Defining PCA for functional data

How does PCA work in the functional context? The counterparts of
variable values are function values $x _ { i } \left( s \right) ,$ so that the discrete index $j$
in the multivariate context has been replaced by the continuous index
s. Summations over $j$ are replaced by integrations over $s$ to define the

<!-- PageBreak -->

<!-- PageNumber="88" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->

linear 'combinations'

$$f _ { i } = \int \beta \left( s \right) x _ { i } \left( s \right) d s = \langle \beta , x _ { i } \rangle .$$
(6.3)

The weights $\beta _ { j }$ now become a weight function with values $\beta \left( s \right) .$

In the first functional PCA step, the weight function $1$ is chosen
to maximize $N ^ { - 1 } \sum _ { i } f _ { i 1 } ^ { 2 } = N ^ { - 1 } \sum _ { i } \langle F _ { 1 } , x _ { i } \rangle ^ { 2 }$ subject to the continuous
analogue of the unit sum of squares constraint $\| E _ { 1 } \| ^ { 2 } = 1 .$ This time,
the notation $\| E _ { 1 } \| ^ { 2 }$ is used to mean the squared norm $\int E _ { 1 } \left( s \right) ^ { 2 } d s$ of the
function $\mathfrak{x} _ { 1 } .$

Postponing computational details until Section 6.4, now consider as
an illustration the upper left panel in Figure 6.1. This displays the
weight function $E _ { 1 }$ for the Canadian temperature data after the mean
across all 35 weather stations has been removed from each station's
monthly temperature record. Although $E _ { 1 }$ is positive throughout the
year, the weight placed on the winter temperatures is about four times
that placed on summer temperatures. This means that the greatest
variability between weather stations will be found by heavily weighting
winter temperatures, with only a light contribution from the summer
months; Canadian weather is most variable in the wintertime, in short.
Moreover, the percentage 89.3% at the top of the panel indicates that
this type of variation strongly dominates all other types of variation.
Weather stations for which the score $f _ { i 1 }$ is high will have much warmer
than average winters combined with warm summers, and the two
highest scores are in fact assigned to Vancouver and Victoria on the
Pacific Coast. To no one's surprise, the largest negative score goes to
Resolute in the High Arctic.

As for multivariate PCA, the weight function $E m$ is also required
to satisfy the orthogonality constraint(s) $\langle 5 k , 5 m \rangle = 0 ,$ $k < m$ on
subsequent steps. Each weight function has the task of defining the
most important mode of variation in the curves subject to each mode
being orthogonal to all modes defined on previous steps. Note again
that the weight functions are defined only to within a sign change.

The weight function $E _ { 2 }$ for the temperature data is displayed in the
upper right panel of Figure 6.1. Because it must be orthogonal to $\xi _ { 1 } ,$ we
cannot expect that it will define a mode of variation in the temperature
functions that will be as important as the first. In fact, this second mode
accounts for only 8.3% of the total variation, and consists of a positive
contribution for the winter months and a negative contribution for the
summer months, therefore corresponding to a measure of uniformity
of temperature through the year. On this component, one of the highest
scores $f _ { i 2 }$ goes to Prince Rupert, also on the Pacific coast, for which
there is comparatively low discrepancy between winter and summer.

<!-- PageBreak -->

<!-- PageNumber="89" -->
<!-- PageHeader="6.2 Defining functional PCA" -->


<figure>
<figcaption>FIGURE 6.1. The first four principal component curves of the Canadian temperature data estimated by two techniques. The points are the estimates from the discretization approach, and the curves are the estimates from the expansion of the data in terms of a 12-term Fourier series. The percentages indicate the amount of total variation accounted for by each principal component.</figcaption>

$P C \quad 1 \left( 8 9 . 3 \right)$

$P C \quad 2 \left( 8 . 3 \right)$

Value of PC curve

0.6 -0.2 0.2 0.6

Value of PC curve

0.6

0.2

-0.2

-0.6

0

2

4

6

8

10

12

0

2

4

6

8

10

12

Month

Month

$\mathrm { P C } 3 \left( 1 . 6 \% \right)$

$P C \quad 4 \left( 0 . 5 \right)$

Value of PC curve

0.6 -0.2 0.2 0.6

Value of PC curve

0.6

0.2

-0.2

0

2 4 6 8 10 12

-0.6

0 2 4 6 8 10 12

Month

Month

</figure>


Prairie stations such as Winnipeg, on the other hand, have hot summers
and very cold winters, and receive large negative second component
scores.

The third and fourth components account for small proportions of
the variation, since they are required to be orthogonal to the first two
as well as to each other. At this point they are difficult to interpret, but
we look at techniques for understanding them in Section 6.3.

Displays such as Figure 6.1 can remind one of the diagrams of modes
of vibration in a string fixed at both ends always found in introductory
physics texts. The first and dominant type is simple in structure and
resembles a single cycle of a sine wave. Subdominant or higher order
components are also roughly sinusoidal, but with more and more
cycles. With this analogy in mind, we find the term harmonics evocative
in referring to principal components of variation in curves in general.

<!-- PageBreak -->

<!-- PageNumber="90" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->


#### 6.2.3 Defining an optimal empirical orthonormal basis

There are several other ways to motivate PCA, and one is to define
the following problem: We want to find a set of exactly $K$ orthonormal
functions $E m$ so that the expansion of each curve in terms of these
basis functions approximates the curve as closely as possible. Since
these basis functions are orthonormal, it follows that the expansion
will be of the form

$$\widehat { x } _ { i } \left( t \right) = \sum _ { k = 1 } ^ { K } f _ { i k } S _ { k } \left( t \right)$$

where $f _ { i k } = \langle x _ { i } , E _ { k } \rangle .$ As a fitting criterion for an individual curve,
consider the integrated squared error

$$\| x _ { i } - \widehat { x } _ { i } \| ^ { 2 } = \int \left[ x \left( s \right) - \widehat { x } \left( s \right) \right] ^ { 2 } d s$$

and as a global measure of approximation

$$\mathrm { P C A S S E } = \sum _ { i = 1 } ^ { N } \| x _ { i } - \widehat { x } _ { i } \| ^ { 2 } .$$
(6.4)

The problem is then, more precisely, what choice of basis will minimize
the error criterion (6.4)?

The answer, it turns out, is precisely the same set of principal
component weight functions that maximize variance components as
defined above. For this reason, these functions $E m$ are referred to
in some fields as empirical orthonormal functions, because they are
determined by the data they are used to expand.


#### 6.2.4 PCA and eigenanalysis

In this section, we investigate another characterization of PCA, in terms
of the eigenanalysis of the variance-covariance function or operator.

Assume for this section that our observed values, $x _ { i j }$ in the
multivariate context and $x _ { i } \left( t \right)$ in the functional situation, result from
subtracting the mean variable or function values, so that their sample
means $N ^ { - 1 } \sum _ { i } x _ { i j } ,$ or cross-sectional means $N ^ { - 1 } \sum _ { i } x _ { i } \left( t \right) ,$ respectively,
are zero.

Texts on multivariate data analysis tend to define principal
components analysis as the task of finding the eigenvalues and
eigenvectors of the covariance or correlation matrix. The logic for this is
as follows. Let the $N \times p$ matrix $X$ contain the values $x _ { i j }$ and the vector
$E$ of length $p$ contain the weights for a linear combination. Then the

<!-- PageBreak -->

<!-- PageNumber="91" -->
<!-- PageHeader="6.2 Defining functional PCA" -->

mean square criterion for finding the first principal component weight
vector can be written as

$$\max _ { E ^ { \prime } \in 1 } N ^ { - 1 } S ^ { \prime } X ^ { \prime } X S$$
(6.5)

since the vector of principal component scores $f _ { i }$ can be written as $X E .$

Use the $p \times p$ matrix $\mathrm { V }$ to indicate the sample variance-covariance
matrix $\mathrm { V } = N ^ { - 1 } \mathrm { X } ^ { \prime } \mathrm { X } .$ (One may prefer to use a divisor of $N \quad - \quad 1$ to $N$ since
the means have been estimated, but it makes no essential difference
to the principal components analysis.) The criterion (6.5) can now be
expressed as

$$\max _ { E ^ { \prime } = 1 } \xi ^ { \prime } V E .$$

As explained in Section $A . 3 ,$ this maximization problem is now solved
by finding the solution with largest eigenvalue $\rho$ of the eigenvector
problem or eigenequation

$$V S = \rho S .$$
(6.6)

There is a sequence of different eigenvalue-eigenvector pairs $\left( \rho _ { j } , \xi _ { j } \right)$
satisfying this equation, and the eigenvectors $E _ { j }$ are orthogonal.
Because the mean of each column of $X$ is usually subtracted from
all values in that column as a preliminary to principal components
analysis, the rank of $X$ is $N \quad - \quad 1$ at most, and hence the $p \times p$ matrix
$\mathrm { V }$ has, at most, $\min \left\{ p , N - 1 \right\}$ nonzero eigenvalues $\rho _ { j } .$ For each $j ,$
the eigenvector $\mathfrak{z} _ { j }$ satisfies the maximization problem (6.5) subject to
the additional constraint of being orthogonal to all the eigenvectors
$E _ { 1 } , E _ { 2 } , \ldots , E _ { j - 1 }$ found so far. This is precisely what was required of
the principal components in the second step laid out in Section 6.2.1.
Therefore, as we have defined it, the multivariate PCA problem is
equivalent to the algebraic and numerical problem of solving the
eigenequation (6.6). Of course, there are standard computer algorithms
for doing this.

Appealing to the more general results set out in Section A.3.2, the
functional PCA problem leads to the eigenequation

$$\int v \left( s , t \right) E \left( t \right) d t = \langle v \left( s , \cdot \right) , E \rangle = \rho E \left( s \right)$$
(6.7)

where the covariance function $v$ is given by

$$v \left( s , t \right) = N ^ { - 1 } \sum _ { i = 1 } ^ { N } x _ { i } \left( s \right) x _ { i } \left( t \right) .$$
(6.8)

Again, note that we may prefer to use $N \quad - \quad 1$ to define the variance-
covariance function $v ;$ nothing discussed here changes in any essential
way.

<!-- PageBreak -->

<!-- PageNumber="92" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->

The left side of (6.7) is an integral transform $V$ of the weight function
$5$ with the kernel of the transform $v$ defined by

$$V S = \int v \left( \cdot , t \right) S \left( t \right) d t .$$
(6.9)

This integral transform is called the covariance operator $V$ because the
integral transform acts or operates on $5 .$ Therefore we may also express
the eigenequation directly as

$$V \xi = \rho F ,$$

where $5$ is now an eigenfunction rather than an eigenvector.

One important difference between the multivariate and functional
eigenanalysis problems concerns the maximum number of different
eigenvalue-eigenfunction pairs. The counterpart of the number of
variables $p$ in the multivariate case is the number of function values in
the functional case, and thus infinity. Provided the functions $x _ { i }$ are not
linearly dependent, the operator $V$ will have rank $N \quad - \quad 1 ,$ and there will
be $N \quad - \quad 1$ nonzero eigenvalues.

To summarize, in this section we find that principal components
analysis is defined as the search for a set of mutually orthogonal and
normalized weight functions $\xi _ { m } .$ Functional PCA can be expressed
as the problem of the eigenanalysis of the covariance operator $V ,$
defined by using the covariance function $\upsilon$ as the kernel of an integral
transform. The use of inner product notation is helpful here because
the same notation can be used whether the data are multivariate or
functional.

In Section 6.4 we discuss practical methods for actually computing
the eigenfunctions $E m ,$ but first we consider some aspects of the display
of principal components once they have been found.


### 6.3 Visualizing the results

The fact that interpreting the components is not always an entirely
straightforward matter is common to most functional PCA problems.
We now consider some techniques that may aid their interpretation.


#### 6.3.1 Plotting components as perturbations of the mean

A method found to be helpful is to examine plots of the overall
mean function and the functions obtained by adding and subtracting
a suitable multiple of the principal component function in question.

<!-- PageBreak -->

<!-- PageNumber="93" -->
<!-- PageHeader="6.3 Visualizing the results" -->


<figure>
<figcaption>FIGURE 6.2. The mean temperature curves and the effects of adding $\left( + \right)$ and subtracting (-) a suitable multiple of each PC curve.</figcaption>

PC 1 (89.3%)

PC 2 ( 8.3%)

Temperature (deg. C)

-20 -10 0 10 20

$\widehat { \mathcal{O} } \stackrel { \circ } { \sim }$ Temperature (deg.

-20 -10 0 10

0 2 4 6 8 10 12

0 2 4 6 8 10 12

Month

Month

$P C \quad 3 \left( 1 . 6 \right)$

$P C \quad 4 \left( 0 . 5 \right)$

Temperature (deg. C)

-20 -10 0 10 20

NA
Temperature (deg. C)

-20 -10 0 10 20

0 2 4 6 8 10 12

0

2 4 6 8 10 12

Month

Month

</figure>


Figure 6.2 shows such a plot for the temperature data. In each case,
the solid curve is the overall mean temperature, and the dotted and
dashed curves show the effects of adding and subtracting a multiple of
each principal component curve. This considerably clarifies the effects
of the first two components. We can now see that the third principal
component corresponds to a time shift effect combined with an overall
increase in temperature and in range between winter and summer. The
fourth corresponds to an effect whereby the onset of spring is later and
autumn ends earlier.

In constructing this plot, it is necessary to choose which multiple of
the principal component function to use. Define a constant $\mathcal{C}$ to be the
root-mean-square difference between $\widehat { \mu }$ and its overall time average,

$$C ^ { 2 } = T ^ { - 1 } \| \widehat { \mu } - \overrightarrow { \mu } \| ^ { 2 }$$
(6.10)

where

$$\check { \mu } = T ^ { - 1 } \int \widehat { \mu } \left( t \right) d t .$$

It is then appropriate to plot $\widehat { \mu }$ and $\widehat { \mu } \pm 0 . 2 C \widehat { y } _ { j } ,$ where we have chosen
the constant 0.2 to give easily interpretable results. Depending on
the overall behaviour of $\widehat { \mu } ,$ it may be helpful to adjust the value 0.2
subjectively. But for ease of comparison between the various modes
of variability, it is best to use the same constant for all the principal
component functions plotted in any particular case.

<!-- PageBreak -->

<!-- PageNumber="94" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->


<figure>
<figcaption>FIGURE 6.3. The hip angle observed in the gait cycles of 39 children, and the effect on the overall mean of adding and subtracting a suitable multiple of each of the first three principal component functions.</figcaption>

Original data curves

PC 1 (71.2% of variability)

Hip angle (degrees)

20 40 60

Hip angle (degrees)

60

40

20

O

0

0.0 0.2 0.4 0.6 0.8 1

1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of gait cycle

Proportion of gait cycle

PC 2 (11.5% of variability)

PC 3 (8.4% of variability)

Hip angle (degrees)

60

Hip angle (degrees)

60

40

40

20

20

D

0

.0 0.2 0.4 0.6 0.8 1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of gait cycle

Proportion of gait cycle

</figure>


In Figure 6.3, we consider the hip angles observed during the gait of
39 children, as plotted in Figure 1.5. The angles for a single cycle are
shown, along with the results of a functional PCA of these data. The
effect of the first principal component of variation is approximately to
add or subtract a constant to the angle throughout the gait cycle. The
second component corresponds roughly to a time shift effect, which is
not constant through the cycle. The third component corresponds to
a variation in the overall amplitude of the angle traced out during the
cycle.


#### 6.3.2 Plotting principal component scores

An important aspect of PCA is the examination of the scores $f _ { i m }$ of
each curve on each component. In Figure 6.4, each weather station is
identified by a four-letter abbreviation of its name given in Table 6.1.
The strings are positioned roughly according to the scores on the first
two principal components; some positions have been adjusted slightly
to improve legibility. The West Coast stations Vancouver (VANC),
Victoria (VICT) and Prince Rupert (PRUP) are in the upper right corner
because they have warmer winters than most stations (high on PC 1)
and less summer-winter temperature variation (high on PC 2). Resolute

<!-- PageBreak -->

<!-- PageNumber="95" -->
<!-- PageHeader="6.3 Visualizing the results" -->


<figure>
<figcaption>FIGURE 6.4. The scores of the weather stations on the first two principal components of temperature variation. The location of each weather station is shown by the four-letter abbreviation of its name assigned in Table 6.1.</figcaption>

RESO

15

PRUP

10

IQAL

SJNS

VICT

Component 2 Score

YARM

VANC

5

SYDN

CHUR

SHEF

HLFX

PGEOCHAR

CALG

0

INUV

WHITBEAV

SHERFRED

EDMO THUN LONDTRTO

?

KPSK QBEC
ARVI

KAML

YELL

MTRL

PALBREGI OTWA

-10

TPAS

DAWS

WINN

-60

-40

-20

0

20

Component 1 Score

</figure>


(RESO), on the other hand, has an extremely cold winter, but does
resemble the Pacific weather stations in having less summer/winter
variation than some Arctic cousins, such as Inuvik (INUV).


#### 6.3.3 Rotating principal components

In Section 6.2 we observed that the weight functions $E m$ can be viewed
as defining an orthonormal set of $K$ functions for expanding the curves
to minimize a summed integrated squared error criterion (6.4). For the
temperature data, for example, no set of four orthonormal functions
will do a better job of approximating the curves than those displayed
in Figure 6.1.

This does not mean, however, that there aren't other orthonormal
sets that will do just as well. In fact, if we now use $E$ to refer to the
vector-valued function $\left( \xi _ { 1 } , \ldots , \xi _ { K } \right) ^ { \prime } ,$ then an equally good orthonormal
set is defined by

$$\psi = \mathrm { T } \xi$$
(6.11)

where $\mathrm { T }$ is any orthonormal matrix of order $K ,$ meaning that $T ^ { \prime } T =$
$T T ^ { \prime } = I .$ From a geometrical perspective, the vector of functions $\psi$ is a
rigid rotation of $5 .$ Of course, after rotation, we can no longer expect
that $\psi _ { 1 }$ will define the largest component of variation. But the point is

<!-- PageBreak -->

<!-- PageNumber="96" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->


<table>
<caption>TABLE 6.1. The Canadian Weather Stations</caption>
<tr>
<td>Arvida, Que.</td>
<td>Kapuskasing, Ont.</td>
<td>St. John's, Nfld</td>
</tr>
<tr>
<td>Beaverlodge, B.C.</td>
<td>London, Ont.</td>
<td>Sydney, N.S.</td>
</tr>
<tr>
<td>Calgary, Alta.</td>
<td>Montreal, Que.</td>
<td>The Pas, Man.</td>
</tr>
<tr>
<td>Charlottetown, P.E.I.</td>
<td>Ottawa, Ont.</td>
<td>Thunder Bay, Ont.</td>
</tr>
<tr>
<td>Churchill, Man.</td>
<td>Prince Albert, Sask.</td>
<td>Toronto, Ont.</td>
</tr>
<tr>
<td>Dawson, Yukon</td>
<td>Prince George, B.C.</td>
<td>Vancouver, B.C.</td>
</tr>
<tr>
<td>Edmonton, Alta.</td>
<td>Prince Rupert, B.C.</td>
<td>Victoria, B.C.</td>
</tr>
<tr>
<td>Fredericton, N.B.</td>
<td>Quebec City, Que.</td>
<td>Whitehorse, Yukon</td>
</tr>
<tr>
<td>Halifax, N.S.</td>
<td>Regina, Sask.</td>
<td>Winnipeg, Man.</td>
</tr>
<tr>
<td>Inuvik, N.W.T.</td>
<td>Resolute, N.W.T.</td>
<td>Yarmouth, N.S.</td>
</tr>
<tr>
<td>Iqualuit, N.W.T.</td>
<td>Schefferville, Que.</td>
<td>Yellowknife, N.W.T.</td>
</tr>
<tr>
<td>Kamloops, B.C.</td>
<td>Sherbrooke, Que.</td>
<td></td>
</tr>
</table>


that the orthonormal basis functions $\psi _ { 1 } , \ldots , \psi _ { K }$ are just as effective at
approximating the original curves in $K$ dimensions as their unrotated
counterparts.

Can we find some rotated functions that are perhaps a little
easier to interpret? Here again, we can borrow a tool that has been
invaluable in multivariate analysis, VARIMAX rotation. Let $B$ be a
$K \times n$ matrix representing the first $K$ principal component functions
$\xi _ { 1 } , \ldots , \xi _ { K } .$ For the moment, suppose that $B$ has, as row $m ,$ the values
$E _ { m } \left( t _ { 1 } \right) , \ldots , E _ { m } \left( t _ { n } \right)$ for $n$ equally spaced argument values in the interval
$T$ . The corresponding matrix $\mathrm { A }$ of values of the rotated basis functions
$\psi = \mathrm { T } \mathrm { S }$ will be given by

$$A = T B .$$
(6.12)

The VARIMAX strategy for choosing the orthonormal rotation matrix
$\mathrm { T }$ is to maximize the variation in the values $a _ { m j } ^ { 2 }$ strung out as a single
vector. Since $\mathrm { T }$ is a rotation matrix, the overall sum of these squared
values will remain the same no matter what rotation we perform. In
algebraic terms

$$\sum _ { m } \sum _ { j } a _ { m j } ^ { 2 } = \text { trace } A ^ { \prime } A = \text { trace } B ^ { \prime } T ^ { \prime } T B = \text { trace } B ^ { \prime } B .$$

Therefore, maximizing the variance of the $a _ { m j } ^ { 2 }$ can happen only if
these values tend either to be relatively large or relatively near zero. The
values $a _ { m j }$ themselves are encouraged to be either strongly positive,
near zero, or strongly negative; in-between values are suppressed. This
clustering of information tends to make the components of variation
easier to interpret.

<!-- PageBreak -->

<!-- PageHeader="6.3 Visualizing the results 97" -->

There are fast and stable computational techniques for computing
the rotation matrix $\mathrm { T }$ that maximizes the VARIMAX criterion. A $C$
function for computing the VARIMAX rotation can be found through
the book's world-wide web page described in Section 1.8.

Figure 6.5 displays the VARIMAX rotation of the four principal
components for the temperature data. There, $n = 1 2$ equally spaced
time points $t _ { j }$ were used, and the variance of the squared values $\psi _ { m } ^ { 2 } \left( t _ { j } \right)$
was maximized with respect to $\mathrm { T } .$ The resulting rotated functions $\Psi m ,$
along with the percentages of variances that they account for, are now
quite different.

Collectively, the rotated functions $\psi _ { m }$ still account for a total of
99.7% of the variation, but they divide this variation in different
proportions. The VARIMAX rotation has suppressed medium-sized
values of $\psi _ { m }$ while preserving orthonormality. (Note that the rotated
component scores are no longer uncorrelated; however, the sum of
their variances is still the same, because $\mathrm { T }$ is a rotation matrix, and so
they may still be considered to partition the variability in the original
data.) The result is four functions that account for local variation in the
winter, summer, spring and autumn, respectively. Not only are these
functions much easier to interpret, but we see something new: although
winter variation remains extremely important, now spring variation
is clearly almost as important, about twice as important as autumn
variation and over three times as important as summer variation.

Another way of using the VARIMAX idea is to let $B$ contain the
coefficients for the expansion of each $\xi _ { m }$ in terms of a basis $\phi$ of
$n$ functions. Thus we rotate the coefficients of the basis expansion
of each $E m$ rather than rotating the values of the $E m$ themselves.
Figure 6.6 shows the results using a Fourier series expansion of the
principal components. The results are much more similar to the original
principal components displayed in Figure 6.2. The main difference is
in the first two components. The first rotated component function
in Figure 6.6 is much more constant than the original first principal
component, and corresponds almost entirely to a constant temperature
effect throughout the year. The general shape of the second component
is not changed very much, but it accounts for more of the variability,
having essentially taken on part of the variability in the first unrotated
component. Because the first component originally accounted for such
a large proportion, 89.3%, of the variability, it is not surprising that a
fairly small change in the shape of the second component results in
moving about 10% of the total variability from the first to the second
component. The third and fourth components are not enormously
affected by the VARIMAX rotation in the Fourier domain.

<!-- PageBreak -->

<!-- PageNumber="98" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->


<figure>
<figcaption>FIGURE 6.5. Weight functions rotated by applying the VARIMAX rotation criterion to weight function values, and plotted as positive and negative perturbations of the mean function.</figcaption>

Rot. PC 1 (40.5%)

Rot. PC 2 ( 9.5%)

Temperature (deg. C)

-20 -10 0 10 20

Temperature (deg. C)

-20 -10 0 10 20

***

0 2 4 6 8 10 12
Month

0

2

4

6

8

10

12

Month

Rot. PC 3 (32.5%)

Rot. PC 4 (17.6%)

Temperature (deg. C)

-20 -10 0 10 20

Temperature (deg. C)

-20 -10 0 10 20

0

2

4

6

8

10

12

0

2 4 6 8 10 1

12

Month

Month

</figure>


<figure>
<figcaption>FIGURE 6.6. Weight functions rotated by applying the VARIMAX rotation criterion to weight function coefficients, and plotted as positive and negative perturbations of the mean function.</figcaption>

Rot. PC 1 (78.4%)

Rot. PC 2 (18.4%)

Temperature (deg. C)

-20 -10 0 10 20

Temperature (deg. C)

-20 -10 0 10 20

0 2 4 6 8 10 12
Month

0

2

4

6

8

10

12

Month

Rot. PC 3 ( 2.0%)

Rot. PC 4 ( 1.0%)

Temperature (deg. C)

-20 -10 0 10 20

Temperature (deg. C)

-20 -10 0 10 20

0

2 4 6 8 10 12
Month

0

2

4

8 10

12

Month

</figure>


<!-- PageBreak -->

<!-- PageNumber="99" -->
<!-- PageHeader="6.4 Computational methods for functional PCA" -->

By no means is the VARIMAX criterion the only rotation criterion
available. References on factor analysis and multivariate statistics such
as Basilevsky (1994), Johnson and Wichern (1988), Mulaik (1972) and
Seber (1984) offer a number of other possibilities. Even from the
relatively brief discussion in this section, it is clear that much research
remains to be done on rotation schemes tailored more directly to the
functional context.


### 6.4 Computational methods for functional PCA

Now suppose that we have a set of $N$ curves $x _ { i } ,$ and that preliminary
steps such as curve registration and the possible subtraction of the
mean curve from each (curve centering) have been completed. Let
$v \left( s , t \right)$ be the sample covariance function of the observed data. In
this section, we consider possible strategies for approaching the
eigenanalysis problem in (6.7). In all cases, we convert the continuous
functional eigenanalysis problem to an approximately equivalent
matrix eigenanalysis task.


#### 6.4.1 Discretizing the functions

A simple approach is to discretize the observed functions $x _ { i }$ to a fine
grid of $n$ equally spaced values $s _ { j }$ that span the interval $T .$ This yields
an $N \times n$ data matrix $X$ that can be fed into a standard multivariate
principal components analysis program such as the $\mathrm { S }$ S-PLUS routine
prcomp. This produces eigenvalues and eigenvectors satisfying

$$\mathrm { V } u = \lambda u$$
(6.13)

for n-vectors $u .$

Notice that we may well have $n$ much larger than $N .$ Rather than
working with the $n \times n$ matrix $\mathrm { v } ,$ one possible approach to finding the
solutions of the eigenequation (6.13) is to work in terms of the SVD
UDW' of $X .$ The variance matrix satisfies $N V = U D ^ { 2 } U ^ { \prime } ,$ and hence the
nonzero eigenvalues of $\mathrm { V }$ are the squares of the singular values of $X ,$
and the corresponding eigenvectors are the columns of $\mathrm { U } .$ If we use
a standard PCA package, these steps, or corresponding ones, will be
carried out automatically in any case.

How do we transform the vector principal components back into
functional terms? The sample variance-covariance matrix $V = N ^ { - 1 } X ^ { \prime } X$
will have elements $v \left( s _ { j } , s _ { k } \right)$ where $v \left( s , t \right)$ is the sample covariance

<!-- PageBreak -->

<!-- PageNumber="100" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->

function. Given any function $,$ let $\widetilde { \mathrm { E } }$ be the n-vector of values $E \left( s _ { j } \right) .$
Let $w = T / n$ where $T$ is the length of the interval $T .$ Then, for each $s _ { j } ,$

$$V E \left( s _ { j } \right) = \int v \left( s _ { j } , s \right) 5 \left( s \right) d s \approx w \sum v \left( s _ { j } , s _ { k } \right) ,$$

so the functional eigenequation $V \xi = \rho$ has the approximate discrete
form

$$w V \widetilde { \xi } = \rho \widetilde { \xi } .$$

The solutions of this equation will correspond to those of (6.13), with
eigenvalues $\rho = w \lambda .$ The discrete approximation to the normalization
$\int E \left( s \right) ^ { 2 } d s = 1$ is $w \| \widetilde { \xi } \| ^ { 2 } = 1 ,$ so that we set $\widetilde { \xi } = w ^ { - 1 / 2 } u$ if $u$
is a normalized eigenvector of $\mathrm { V } .$ Finally, to obtain an approximate
eigenfunction $5$ from the discrete values $\widetilde { \mathrm { E } } ,$ we can use any convenient
interpolation method. If the discretization values $s _ { j }$ are closely spaced,
the choice of interpolation method will not usually have $a$ great effect.

The discretization approach is the earliest approach to functional
principal components analysis, used by Rao (1958, 1987) and Tucker
(1958), who applied multivariate principal components analysis
without modification to observed function values. We discuss the idea
of discretizing the integral in more detail in Section 6.4.3, but first we
consider an alternative approach that makes use of basis expansions.


#### 6.4.2 Basis function expansion of the functions

One way of reducing the eigenequation (6.7) to discrete or matrix
form is to express each function $x _ { i }$ as a linear combination of known
basis functions $\phi _ { k } .$ The number $K$ of basis functions used depends on
many considerations: How many discrete sampling points $n$ were in
the original data, whether some level of smoothing was to be imposed
by using $K < n ,$ how efficient or powerful the basis functions are
in reproducing the behaviour of the original functions, and so forth.
For the monthly temperature data, for example, it would be logical to
use a Fourier series basis orthonormal over the interval $\left[ 0 , 1 2 \right] ,$ with
$K = 1 2$ the maximum possible dimension of the basis for the monthly
temperature data, because only 12 sampling points are available per
curve. Actually, for these data, a value of $K$ as small as 7 would capture
most of the interesting variation in the original data, but there is little
point in reducing $K$ below the value of 12.

Now suppose that each function has basis expansion

$$x _ { i } \left( t \right) = \sum _ { k = 1 } ^ { K } c _ { i k } \phi _ { k } \left( t \right) .$$
(6.14)

<!-- PageBreak -->

<!-- PageNumber="101" -->
<!-- PageHeader="6.4 Computational methods for functional PCA" -->

We may write this more compactly by defining the vector-valued
function $x$ to have components $x _ { 1 } , \ldots , x _ { N } ,$ and the vector-valued
function $\phi$ to have components $\phi _ { 1 } , \ldots , \phi _ { K } .$ We may then express the
simultaneous expansion of all $N$ curves as

$$x = C \phi$$

where the coefficient matrix $\mathrm { C }$ is $N \times K .$ In matrix terms the variance-
covariance function is

$$v \left( s , t \right) = N ^ { - 1 } \phi \left( s \right) ^ { \prime } C ^ { \prime } C \phi \left( t \right)$$

remembering that $\phi \left( s \right) ^ { \prime }$ denotes the transpose of the vector $\phi \left( s \right)$ and
has nothing to do with differentiation.

Define the order $K$ symmetric matrix $W$ to have entries

$$w _ { k _ { 1 } , k _ { 2 } } = \int \phi _ { k _ { 1 } } \left( t \right) \phi _ { k _ { 2 } } \left( t \right) d t = \langle \phi _ { k _ { 1 } } , \phi _ { k _ { 2 } } \rangle$$

or, more compactly, $W = \int \phi ^ { \prime } \phi .$ For some choices of bases, $\mathrm { W }$ will be
readily available. For example, for the orthonormal Fourier series that
we might use for the temperature data, $W = I ,$ the order $K$ identity
matrix. In other cases, we may have to resort to numerical integration
to evaluate $\mathrm { W } .$

Now suppose that an eigenfunction $5$ for the eigenequation (6.7) has
an expansion

$$E \left( s \right) = \sum _ { k = 1 } ^ { K } b _ { k } \phi _ { k } \left( s \right)$$

or, in matrix notation, $F \left( s \right) = \phi \left( s \right) ^ { \prime } b .$ This yields

$$\int v \left( s , t \right) 5 \left( t \right) d t = \int N ^ { - 1 } \phi \left( s \right) ^ { \prime } C d \left( t \right) \phi \left( t \right) ^ { \prime } b d t$$
$$= \phi \left( s \right) ^ { \prime } N ^ { - 1 } C ^ { \prime } C W b .$$

Therefore the eigenequation (6.7) can be expressed as

$$\phi \left( s \right) ^ { \prime } N ^ { - 1 } C ^ { \prime } C W b = \rho \phi \left( s \right) ^ { \prime } b .$$

Since this equation must hold for all $s ,$ this implies the purely matrix
equation

$$N ^ { - 1 } C ^ { \prime } C W b = \rho b .$$

But note that $\| \xi \| = 1$ implies that $b ^ { \prime } W b = 1$ and, similarly, two
functions $\xi _ { 1 }$ and $E _ { 2 }$ will be orthogonal if and only if the corresponding
vectors of coefficients satisfy $b _ { 1 } ^ { \prime } W b _ { 2 } = 0 .$ To get the required principal

<!-- PageBreak -->

<!-- PageNumber="102" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->

components, we define $u = w ^ { 1 / 2 } b ,$ solve the equivalent symmetric
eigenvalue problem

$$N ^ { - 1 } W ^ { 1 / 2 } C ^ { \prime } C W ^ { 1 / 2 } u = p u$$

and compute $b = W ^ { - 1 / 2 } u$ for each eigenvector.

Two special cases deserve particular attention. As already mentioned,
if the basis is orthonormal, meaning that $W = I ,$ the functional
PCA problem finally reduces to the standard multivariate PCA of the
coefficient array $C ,$ and we need only carry out the eigenanalysis of the
order $K$ symmetric array $N ^ { - 1 } C ^ { \prime } C .$

As a rather different special case, particularly appropriate if the
number of observed functions is not enormous, we may also view
the observed functions $x _ { i }$ as their own basis expansions. In other
words, there are $N$ basis functions, and they happen to be the observed
functions. This implies, of course, that $\mathrm { C } = \mathrm { I } ,$ and now the problem
becomes one of the eigenanalysis of the symmetric matrix $N ^ { - 1 } W ,$ which
has entries

$$w _ { i j } = \int x _ { i } \left( t \right) x _ { j } \left( t \right) d t = \langle x _ { i } , x _ { j } \rangle .$$

As a rule, these entries will have to be computed by some quadrature
technique.

In every case, the maximum number of eigenfunctions that can
in principle be computed by the basis function approach is $K ,$ the
dimension of the basis. However, if the basis expansions have involved
any approximation of the observed functions, then it is not advisable to
use a basis expansion to $K$ terms to calculate more than a fairly small
proportion of $K$ eigenfunctions.

The results of both the strategies we have discussed are illustrated
in Figure 6.1, which shows the first four estimated eigenfunctions $E m$
of the centred temperature functions

$$x _ { i } = \mathrm { T e m p } _ { i } - \frac { 1 } { 3 5 } \sum _ { j } .$$

The smooth curves give the estimated eigenfunctions using the
complete 12-term Fourier series expansion. For comparison purposes,
the results of applying the discretization approach to the data are also
displayed as points indicating the values of the eigenvectors. There is
little discrepancy between the two sets of results. The proportions of
variances for the basis function analysis turn out to be identical to those
computed for the discretization approach. No attempt has been made
to interpolate the discretized values to give continuous eigenfunctions,

<!-- PageBreak -->

<!-- PageNumber="103" -->
<!-- PageHeader="6.4 Computational methods for functional PCA" -->

but if the Fourier series interpolation method were used, the results
would be identical to the results obtained by the basis method; this is
a consequence of special properties of Fourier series.


#### 6.4.3 More general numerical quadrature

The eigenequation (6.7) involves the integral $\int x _ { i } \left( s \right) 5 \left( s \right) d s ,$ and the
discretization strategy is to approximate this integral by a sum of
discrete values. Most schemes for numerical integration or quadrature
(Stoer and Bulirsch, 1980, is a good reference) involve an approximation
of the form

$$\int f \left( s \right) d s \approx \sum _ { j = 1 } ^ { n } w _ { j } f \left( s _ { j } \right)$$
(6.15)

and the method set out in Section 6.4.1 is a fairly crude special case. We
restrict our attention to linear quadrature schemes of the form (6.15).
There are three aspects of the approximation that can be manipulated
to meet various objectives:

· $n ,$ the number of discrete argument values $s _ { j }$

· $s _ { j } ,$ the argument values, called quadrature points

· $w _ { j } ,$ the weights, called quadrature weights, attached to each
function value in the sum.

A simple example is the trapezoidal rule, in which the interval of
integration is divided into $n \quad - \quad 1$ equal intervals, each of width $h .$ The $s _ { j }$
are the boundaries of the interval with $s _ { 1 }$ and $s _ { n }$ the lower and upper
limits of integration, respectively, and the approximation is

$$\int f \left( s \right) d s \approx h \left[ f \left( s _ { 1 } \right) / 2 + \sum _ { j = 2 } ^ { n - 1 } f \left( s _ { j } \right) + f \left( s _ { n } \right) / 2 \right] .$$
(6.16)

Note that the weights $w _ { j }$ are $h / 2 , h , \cdots , h , h / 2$ and that accuracy
is controlled simply by the choice of $n .$ The trapezoidal rule has
some important advantages: the original raw data are often collected
for equally spaced argument values, the weights are trivial, and
although the accuracy of the method is modest relative to other more
sophisticated schemes, it is often entirely sufficient for the objectives
at hand. The method we set out in Section 6.4.1 is similar to the
trapezoidal rule, and indeed if we use periodic boundary conditions, the
methods are the same, since the values $f \left( s _ { n } \right)$ and $f \left( s _ { 1 } \right)$ are identical.

Other techniques, Gaussian quadrature schemes for example, define
quadrature weights and points that yield much higher accuracy for

<!-- PageBreak -->

<!-- PageNumber="104" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->

fixed $n$ under suitable additional conditions on the integrand. Another
class of procedures chooses the quadrature points adaptively to
provide more resolution in regions of high integrand curvature; for
these to be relevant to the present discussion, we must choose the
quadrature points once for all the functions considered in the analysis.

Applying quadrature schemes of the type (6.15) to the operator $V$ in
(6.9), yields the discrete approximation

$$V E \approx V W$$
(6.17)

where, as in Section 6.4.1, the matrix $\mathrm { V }$ contains the values $v \left( s _ { j } , s _ { k } \right)$ of
the covariance function at the quadrature points, and $\widetilde { E }$ is an order $n$
vector containing values $E \left( s _ { j } \right) .$ The matrix $\mathrm { W }$ is a diagonal matrix with
diagonal values being the quadrature weights $w _ { j } .$

The approximately equivalent matrix eigenanalysis problem is then

$$= \rho$$

where the orthonormality requirement is now

$$= 1 \text { and } \widetilde { \xi } _ { m _ { 1 } } ^ { \prime } W _ { 5 m _ { 2 } } ^ { \prime } = 0 , m _ { 1 } * m _ { 2 } .$$

Since most quadrature schemes use positive weights, we can put the
approximate eigenequation in more standard form, analogous to the
calculations carried out in Section 6.4.2:

$$W ^ { 1 / 2 } V W ^ { 1 / 2 } u = \rho u$$

where $u = w ^ { 1 / 2 }$ and $u ^ { \prime } u = 1 .$ Then the whole procedure is as follows:

1\. Choose $n ,$ the $w _ { j } ,$ and the sj's.

2\. Compute the eigenvalues $\rho _ { m }$ and eigenvectors $u _ { m }$ of $W ^ { 1 / 2 } V W ^ { 1 / 2 } .$

3\. Compute

$$\widetilde { E } _ { m } = W ^ { - 1 / 2 } u _ { m } .$$

4\. If needed, use an interpolation technique to convert each vector
$\widetilde { E } _ { m }$ to a function $E m .$

If the number $n$ of quadrature points is less than the number of
curves $N ,$ we cannot recover more than $n$ approximate eigenfunctions.
However, many applications of PCA require only a small number of the
leading eigenfunctions, and any reasonably large $n$ will serve.

To illustrate the application of this discretizing approach, we analyse
the acceleration in human growth described in Chapter 1. Each

<!-- PageBreak -->

<!-- PageNumber="105" -->
<!-- PageHeader="6.5 Bivariate and multivariate PCA" -->


<figure>
<figcaption>FIGURE 6.7. The solid curve in each panel is the mean acceleration in height in cm/year2 for girls in the Zurich growth study. Each principal component is plotted in terms of its effect when added $\left( + \right)$ and subtracted $\left( - \right)$ from the mean curve.</figcaption>

PC 1 (31.2%)

PC 2 (20.9%)

PC 3 (17.5%)

-4 -3 -2 -1 0 1 2

-4 -3 -2 -1 0 1 2

-4 -3 -2 -1 0 1 2

4 6 8 10 12 14 16 18

4 6 8 10 12 14 16 18

4 6 8 10 12 14 16 18

</figure>


curve consists of 141 equally spaced values of acceleration in height
estimated for ages from 14 to 18 years, after spline smoothing and
registration by certain marker events. Full details of this process can
be found in Ramsay, Bock and Gasser (1995). The curves are for 112
girls who took part in the Zurich growth study (Falkner, 1960).

Figure 6.7 shows the first three eigenfunctions or harmonics plotted
as perturbations of the mean function. Essentially, the first principal
component reflects a general variation in the amplitude of the variation
in acceleration that is spread across the entire curve, but is particularly
marked during the pubertal growth spurt lasting from 10 to 16
years of age. The second component indicates variation in the size
of acceleration only from ages 4 to 6, and the third component, of
great interest to growth researchers, shows a variation in intensity of
acceleration in the prepubertal period around ages 5 to 9 years.


### 6.5 Bivariate and multivariate PCA

We often wish to study the simultaneous variation of more than one
function. The hip and knee angles described in Chapter 1 are an
example; to understand the total system, we want to know how hip
and knee angles vary jointly. Similarly, the handwriting data require
the study of the simultaneous variation of the $X$ and $\mathrm { Y }$ coordinates;
there would be little point in studying one coordinate at a time.

<!-- PageBreak -->

<!-- PageNumber="106" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->


#### 6.5.1 Defining multivariate functional $P C A$

For clarity of exposition, we discuss the extension of the PCA
idea to deal with bivariate functional data in the specific context
of the hip and knee data. Suppose that the observed hip angle
curves are $H i p _ { 1 } , H i p _ { 2 } , \ldots , H i p _ { n }$ and the observed knee angles are
Knee1, $\mathrm { K n e e } _ { 2 } , \ldots , \mathrm { K n e e } _ { n } .$ Let Hipmn and Kneemn be estimates of the
mean functions of the Hip and Knee processes. Define $v _ { H H }$ to be the
covariance operator of the $\mathrm { H i p } _ { i } ,$ $v _ { K K }$ that of the Kneei, $v _ { H K }$ to be the
cross-covariance function, and $v _ { K H } \left( t , s \right) = v _ { H K } \left( s , t \right) .$

$A$ typical principal component is now defined by a 2-vector $=$
$\left( 5 ^ { 4 } , 5 ^ { K } \right) ^ { \prime }$ of weight functions, with $5 ^ { H }$ denoting the variation in the
Hip curve and $5 ^ { K }$ that in the Knee curve. To proceed, we need to
define an inner product on the space of vector functions. The most
straightforward definition is simply to sum the inner products of the
two components. We define the inner product of $\xi _ { 1 }$ and $5 2$ to be

$$\langle E _ { 1 } , E _ { 2 } \rangle = \langle E _ { 1 } ^ { H } , E _ { 2 } ^ { H } \rangle + \langle E _ { 1 } ^ { K } , S _ { 2 } ^ { K } \rangle .$$
(6.18)

The corresponding squared norm $\| E \| ^ { 2 }$ is simply the sum of the squared
norms of the two component functions $5 ^ { H }$ and $5 ^ { K } .$

What all this amounts to, in effect, is stringing two (or more)
functions together to form a composite function. We do the same thing
with the data themselves: define $\mathrm { A n g l e s } _ { i } = \left( \mathrm { H i p } _ { i } , \mathrm { K n e e } _ { i } \right) .$ The weighted
linear combination (6.3) becomes

$$f _ { i } = \langle E , \text { Ang } 7 e s _ { i } \rangle = \langle E ^ { H } , H i p _ { i } \rangle + \langle E ^ { K } , K n e e _ { i } \rangle .$$
(6.19)

We now proceed exactly as in the univariate case, extracting solutions
of the eigenequation system $V S = \rho S ,$ which can be written out in full
detail as

$$\int v _ { H H } \left( s , t \right) S ^ { H } \left( t \right) d t + \int v _ { H K } \left( s , t \right) g ^ { K } \left( t \right) d t = \rho S ^ { H } \left( s \right)$$
$$\int v _ { K H } \left( s , t \right) S ^ { H } \left( t \right) d t + \int v _ { K K } \left( s , t \right) S ^ { K } \left( t \right) d t = \rho S ^ { K } \left( s \right) .$$
(6.20)

In practice, we carry out this calculation by replacing each function
$\mathrm { H i p } _ { i }$ and $\mathrm { K n e e } _ { i }$ with a vector of values at a fine grid of points or
coefficients in a suitable expansion. For each $i$ these vectors are
concatenated into a single long vector $Z _ { i }$ the covariance matrix of
the $Z _ { i }$ is a discretized version of the operator $V$ as defined in (6.6).
We carry out a standard principal components analysis on the vectors
$Z _ { i } ,$ and separate the resulting principal component vectors into the
parts corresponding to Hip and to Knee. The analysis is completed

<!-- PageBreak -->

<!-- PageNumber="107" -->
<!-- PageHeader="6.5 Bivariate and multivariate PCA" -->


<figure>
<figcaption>FIGURE 6.8. The mean hip and knee angle curves and the effects of adding and subtracting a multiple of each of the first two vector principal components.</figcaption>

Hip curve for PC 1

Knee curve for PC 1

Hip angle (degrees)

-20 0 20 40 60

Knee angle (degrees)

20 40 60 80

0

0.0 0.2 0.4 0.6 0.8 1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of gait cycle

Proportion of gait cycle

Hip curve for PC 2

Knee curve for PC 2

Hip angle (degrees)

20 40 60

Knee angle (degrees)

20 40 60 80

0

-20

O

0.0 0.2 0.4 0.6 0.8

1.0

0.0 0.2 0.4 0.6 0.8 1.

Proportion of gait cycle

Proportion of gait cycle

</figure>


by applying a suitable inverse transform to each of these parts if
necessary.

If the variability in one of the sets of curves is substantially greater
than that in the other, then it is advisable to consider downweighting
the corresponding term in the inner product (6.18), and making the
consequent changes in the remainder of the procedure. In the case
of the hip and knee data, however, both sets of curves have similar
amounts of variability and are measured in the same units (degrees)
and so there is no need to modify the inner product.


#### 6.5.2 Visualizing the results

In the bivariate case, the best way to display the result depends
on the particular context. In some cases it is sufficient to consider
the individual parts $5 _ { m } ^ { H }$ and $E K$ separately. An example of this is
given in Figure 6.8, which displays the first two principal components.
Because $\| E _ { m } ^ { H } \| ^ { 2 } + \| E _ { m } ^ { K } \| ^ { 2 } = 1$ by definition, calculating $\| E _ { m } ^ { H } \| ^ { 2 }$ gives the
proportion of the variability in the mth principal component accounted
for by variation in the hip curves.

For the first principal components, this measure indicates that 85%
of the variation is due to the hip curves, and this is borne out by
the presentation in Figure 6.8. The effect on the hip curves of the

<!-- PageBreak -->

<!-- PageNumber="108" -->
<!-- PageHeader="6. Principal components analysis for functional data" -->

first combined principal component of variation is virtually identical
to the first principal component curve extracted from the hip curves
considered alone. There is also little associated variation in the knee
curves, apart from a small associated increase in the bend of the knee
during the part of the cycle where all the weight is on the observed leg.
The main effect of the first principal component remains an overall
shift in the hip angle. This could be caused by an overall difference in
stance; some people stand up more straight than others and therefore
hold their trunks at a different angle from the legs through the gait
cycle. Alternatively, there may simply be variation in the angle of the
marker placed on the trunk.

For the second principal component, the contributions of both hip
and knee are important, with somewhat more of the variability (65%)
due to the knee than to the hip. We see that this principal component
is mainly a distortion in the timing of the cycle, again correlated with
the way in which the initial slight bend of the knee takes place. There
is some similarity to the second principal component found for the hip
alone, but this time there is very substantial interaction between the
two joints.

A particularly effective method for displaying principal components
in the bivariate case is to construct plots of one variable against
the other. Suppose we are interested in displaying the mth principal
component function. For equally spaced points $t$ in the time interval on
which the observations are taken, we indicate the position of the mean
function values (Hipmn(t), Kneemn(t)) by a dot in the $\left( x , y \right)$ plane,
and we join this dot by an arrow to the point $\left( H i p m n \left( t \right) + C E _ { m } ^ { H } \left( t \right) \right. ,$
$\left. \left( t \right) + C 5 _ { m } ^ { K } \left( t \right) \right) .$ We choose the constant $C$ to give clarity. Of
course, the sign of the principal component functions, and hence the
sense of the arrows, is arbitrary, and plots with all the arrows reversed
convey the same information.

This technique is displayed in Figure 6.9. The plot of the mean cycle
alone demonstrates the overall shape of the gait cycle in the hip-
knee plane. The portion of the plot between time points 11 and 19
(roughly the part where the foot is off the ground) is approximately
half an ellipse with axes inclined to the coordinate axes. The points
on the ellipse are roughly at equal angular coordinates - somewhat
closer together near the more highly curved part of the ellipse. This
demonstrates that in this part of the cycle, the joints are moving
roughly in simple harmonic motion but with different phases. During
the other part of the cycle, the hip angle is changing at a approximately
constant rate as the body moves forward with the leg approximately
straight, and the knee bends slightly in the middle.

<!-- PageBreak -->

<!-- PageNumber="109" -->
<!-- PageHeader="6.5 Bivariate and multivariate PCA" -->


<figure>
<figcaption>FIGURE 6.9. A plot of 20 equally spaced points in the average gait cycle, and the effects of adding a multiple of each of the first three principal component cycles in turn.</figcaption>

Mean curve (numbered along cycle)

PC 1 (44.5% of variability)

Knee angle (degrees)

80

14

15

0 20 40 60 80

16

Knee angle (degrees)

1

60

13

17

40

12

18

20

$1 1 ^ { 1 } \log _ { 8 } 7 ^ { 5 } 4 ^ { 3 } 2 ^ { 1 9 }$

O

-20

0

20

40

60

-20

0

20

40

60

Hip angle (degrees)

Hip angle (degrees)

PC 2 (19% of variability)

PC 3 (12.3% of variability)

Knee angle (degrees)

80

Knee angle (degrees)

0 20 40 60 80

$x ^ { 2 }$

60

$x$

1

$\nu ^ { \prime }$

40

I

1

20

0

-20

0

20 40 60

-20

0

20

40

60

Hip angle (degrees)

Hip angle (degrees)

</figure>


Now consider the effect of the first principal component of variation.
As we have already seen, this has little effect on the knee angle, and all
the arrows are approximately in the x-direction. The increase in the hip
angle due to this mode of variation is somewhat larger when the angle
itself is larger. This indicates that the effect contains an exaggeration
(or diminution) in the amount by which the hip joint is bent during the
cycle, and is also related to the overall angle between the trunk and the
legs.

The second principal component demonstrates an interesting effect.
There is little change during the first half of the cycle. However,
during the second half, individuals with high values of this principal
component would traverse roughly the same cycle but at a roughly
constant time ahead. Thus this component represents a uniform time
shift during the part of the cycle when the foot is off the ground.

A high score on the third component indicates two effects. There
is some time distortion in the first half of the cycle, and then a
shrinking of the overall cycle; an individual with a high score would
move slowly through the first part of the cycle, and then perform
simple harmonic motion of knee and hip joints with somewhat less
than average amplitude.

<!-- PageBreak -->


## 7 Regularized principal components analysis


### 7.1 Introduction

In this chapter, we discuss the application of smoothing to functional
principal components analysis. In Chapter 3 we have already seen
that smoothing methods are useful in functional data analysis in
preprocessing the data to obtain functional observations. The emphasis
in this chapter is somewhat different, in that we incorporate the
smoothing into the principal components analysis itself.

Our discussion provides a further insight into the way the method
of regularization, discussed in Chapter 4, can be used rather generally
in functional data analysis. As in Section 5.4.2, the basic idea is to put
into practice, in any particular context, the philosophy of combining a
measure of goodness-of-fit with a roughness penalty.

Consideration of the third component in Figure 6.1 indicates that
some smoothing may be appropriate when estimating functional
principal components. A more striking example is provided by the
pinch force data discussed in Section 1.4.2. Rather than smoothing
the data initially, consider the data in Figure 7.1, which consists of the
original records of the force exerted by the thumb and forefinger during
each of 20 brief squeezes or pinches. The observed records are not very
smooth, and consequently the principal component curves in Figure
7.2 show substantial variability. There is a clear need for smoothing or

<!-- PageBreak -->

<!-- PageNumber="112" -->
<!-- PageHeader="7. Regularized principal components analysis" -->


<figure>
<figcaption>FIGURE 7.1. The aligned original recordings of the force relative to a baseline value exerted during each of 20 brief pinches.</figcaption>

3000

Squeeze

2000

1000

0

0

20

40

60

80

100

Time

</figure>


<figure>
<figcaption>FIGURE 7.2. The first four principal component curves for the pinch force data without regularization.</figcaption>

3

2

Squeeze

1

0

-1

-2

0

20

40

60

80

100

Time

</figure>


<!-- PageBreak -->

<!-- PageNumber="113" -->
<!-- PageHeader="7.2 Smoothing by using roughness penalties" -->

regularizing of the estimated principal component curves, and we use
this data set to illustrate the methodology of this chapter.


### 7.2 Smoothing by using roughness penalties

The main approach of this chapter is based on a roughness penalty
idea, as discussed in Chapter 5. Suppose $\xi$ is a possible principal
component curve. As in standard spline smoothing, we usually penalize
the roughness of $5$ by its integrated squared second derivative over
the interval of interest, $P E N _ { 2 } \left( E \right) = \| D ^ { 2 } E \| ^ { 2 } .$ We define $\mathcal{S}$ as the space of
functions $5$ for which $\| D ^ { 2 } \xi \| ^ { 2 }$ makes sense, in other words those which
have continuous derivative and square-integrable second derivative,
and, in addition, satisfy any relevant boundary conditions for the
problem in hand, of which two examples are: (1) the periodicity of $5$
and $D E ,$ and (2) $\leq \left( 0 \right) = D E \left( 0 \right) = 0 .$

It is often useful to be able to express the roughness penalty in
an alternative form. To do this, we need to impose some additional
regularity conditions on the functions we are considering.

Suppose that $5$ has square-integrable derivatives up to degree four,
and also that $5$ satisfies one of the following two conditions:

· either $D ^ { 2 }$ and $D ^ { 3 }$ are zero at the ends of the interval $T$

· or the second and third derivatives of $5$ satisfy periodic boundary
conditions on $T$ because we require that functions in $\mathcal{S}$ be
periodic.

We call functions satisfying either of these conditions very smooth on
$T .$ The conditions are called natural and periodic boundary conditions,
respectively.

Suppose that $x$ is any function in $\mathcal{S}$ and that $5$ is very smooth.
For notational simplicity, assume that $T$ is the interval $T = \left[ 0 , T \right] .$
Integrate by parts twice to obtain

$$\langle D ^ { 2 } x , D ^ { 2 } S \rangle = \int _ { T } D ^ { 2 } x \left( s \right) D ^ { 2 } S \left( s \right) d s$$
$$= D x \left( T \right) D ^ { 2 } S \left( T \right) - D x \left( 0 \right) D ^ { 2 } S \left( 0 \right)$$
$$- \int _ { T } D x \left( s \right) D ^ { 3 } S \left( s \right) d s .$$

(7.1)

Under natural boundary conditions, $D ^ { 2 } S \left( T \right) = D ^ { 2 } E \left( 0 \right) = 0 ,$ so
the boundary terms in (7.1) are both zero; under periodic boundary
conditions, both $D x$ and $D ^ { 2 }$ are periodic on $\left[ 0 , 1 \right] ,$ implying that

$$D x \left( T \right) D ^ { 2 } S \left( T \right) = D x \left( 0 \right) D ^ { 2 } 5 \left( 0 \right)$$

<!-- PageBreak -->

<!-- PageNumber="114" -->
<!-- PageHeader="7. Regularized principal components analysis" -->

and the boundary terms cancel out. In either case, integrating by parts
and using the boundary conditions a second time, we obtain

$$\langle D ^ { 2 } x , D ^ { 2 } S \rangle = - \int _ { T } D x \left( s \right) D ^ { 3 } S \left( s \right) d s$$
$$= \left\{ x \left( T \right) D ^ { 3 } 5 \left( T \right) - x \left( 0 \right) D ^ { 3 } S \left( 0 \right) \right\} + \int _ { T } x \left( s \right) D ^ { 4 } 5 \left( s \right) d s$$
$$= \left( x , D ^ { 4 } \right) .$$
(7.2)

This immediately implies that the roughness penalty can be rewritten
as

$$\| D ^ { 2 } E \| ^ { 2 } = \langle E , D ^ { 4 } E \rangle$$
(7.3)

which will be a useful expression in our subsequent discussion. We
shall assume throughout that the PCA functions $5$ we are estimating
are very smooth.


### 7.3 Estimating smoothed principal components

Now consider the estimation of the leading principal component. In
an unsmoothed functional PCA as described in Chapter 6, we would
estimate this by maximizing $\left( , V \right)$ subject to $\| \xi \| ^ { 2 } = 1 .$ Here, $\left. , V E \right)$
is the sample variance of the principal component scores $\langle E , x _ { i } \rangle$ over
the observations $x _ { i } .$ As explained in Section 6.2.4, this maximization
problem is solved by finding the leading solution of the eigenfunction
equation $V \xi = \rho \xi .$

However, it may well be the case that maximizing this sample
variance is not our only aim. If we are incorporating smoothing into
our procedure, then we have another aim, to prevent the roughness
of the estimated principal component $5$ from being too large. The key
to the roughness penalty approach is to make explicit this possible
conflict. In the context of estimating a principal component function,
there is a tradeoff between maximizing the sample variance $\left( 5 , V E \right)$
and keeping the roughness penalty $P E N _ { 2 } \left( F \right)$ from becoming too large.
As usual in the roughness penalty method, the tradeoff is controlled
by a smoothing parameter $\lambda \geq 0$ which regulates the importance of the
roughness penalty term.

Given any possible principal component function $5$ with $\| \xi \| ^ { 2 } = 1 ,$
one way of penalizing the sample variance $\langle E , V \xi \rangle$ is to divide it by
$\left\{ 1 + \lambda \times \mathrm { P E N } _ { 2 } \left( \mathrm { E } \right) \right\} .$ This gives the penalized sample variance

$$P C A P S V = \frac { \langle E , V E \rangle } { \| F \| ^ { 2 } + \lambda \times P E N _ { 2 } \left( E \right) } .$$
(7.4)

<!-- PageBreak -->

<!-- PageNumber="115" -->
<!-- PageHeader="7.4 Finding the regularized PCA in practice" -->

Increasing the roughness of $E$ while maintaining $\lambda$ fixed decreases
PCAPSV, as defined in (7.4), since $P E N _ { 2 } \left( F \right)$ increases. Moreover, PCAPSV
reverts to the raw sample variance as $\lambda \twoheadrightarrow 0 .$ On the other hand, the
larger the value of $\lambda ,$ the more the penalized sample variance is affected
by the roughness of $.$ In the limit $\lambda \rightarrow \infty ,$ the component $E$ is forced
to be of the form $5 = a$ in the periodic case and $5 = a + b t$ in the
nonperiodic case, for some constants $a$ and $b .$

How is PCAPSV actually maximized? Making use of the relationship
(7.3), we have

$$P G A P S V = \frac { \langle E , V E \rangle } { \langle F , \left( I + \lambda D ^ { 4 } \right) S \rangle }$$

This expresses the penalized sample variance in the form considered in
Section A.3.3. By the results described there, the maximum of PCAPSV
is the eigenfunction $5$ in the leading solution of the eigenfunction
equation

$$V E = \rho \left( I + \lambda D ^ { 4 } \right) 5 .$$
(7.5)

Of course, it is usually of interest not merely to estimate the leading
principal component, but also to estimate the other components.
A good way of estimating these is to find all the eigenvalues $\rho$
and eigenfunctions $5$ of the equation (7.5). Suppose that $E _ { j }$ is the
eigenfunction corresponding to the $j$ jth largest eigenvalue. Since the
$\mathrm { I } _ { \mathrm { S } }$ will be used as estimates of principal component functions, we
rescale them to satisfy $\| F _ { j } \| ^ { 2 } = 1 .$

How can this procedure be interpreted? As noted in Section A.3.3,
the $\mathfrak{x} _ { j }$ maximizes the penalized variance (7.4) subject to $\| E \| ^ { 2 } = 1$
and a modified form of orthogonality to the previously estimated
components

$$\langle \xi _ { j } , \xi _ { k } \rangle + \lambda \langle D ^ { 2 } \xi _ { j } , D ^ { 2 } \xi _ { k } \rangle = 0 \mathrm { f o r } k = 1 , \ldots , j - 1 .$$
(7.6)

The use of the modified orthogonality condition (7.6) means that we
can find the estimates of all the required eigenfunctions by solving
the single generalized eigenproblem (7.5). Silverman (1996) provides a
detailed theoretical discussion of the advantages of this approach, and
a practical algorithm is set out in the next section.


### 7.4 Finding the regularized PCA in practice

In practice, the eigenproblem (7.5) is most easily solved by working in
terms of a suitable basis. First of all, consider the periodic case, for
which it is easy to set out an algorithm based on Fourier series.

<!-- PageBreak -->

<!-- PageNumber="116" -->
<!-- PageHeader="7. Regularized principal components analysis" -->


#### 7.4.1 The periodic case

Suppose, then, that $T$ is the interval $\left[ 0 , 1 \right]$ and that periodic boundary
conditions are valid for all the functions we are considering. In
particular, this means that the data $x _ { i } \left( s \right)$ themselves are periodic. Let
$\left\{ \phi _ { v } \right\}$ be the series of Fourier functions defined in (3.10). For each $j ,$
define $w _ { 2 j - 1 } = w _ { 2 j } = 2 \pi j .$ Given any periodic function $x ,$ we can
expand $x$ as a Fourier series with coefficients $c _ { v } = \langle x , \phi _ { v } \rangle ,$ so that

$$x \left( s \right) = \sum _ { v } c _ { v } \phi _ { v } \left( s \right) = c ^ { \prime } \phi \left( s \right) .$$

The operator $D ^ { 2 }$ has the useful property that, for each $\mathcal{V} ,$

$$D ^ { 2 } \phi _ { v } = - w _ { v } ^ { 2 } \phi _ { v } ,$$

meaning that we can also expand $D ^ { 2 } x$ as

$$D ^ { 2 } x \left( s \right) = - \sum _ { v } w _ { v } ^ { 2 } c _ { v } \phi _ { v } \left( s \right) .$$

Since the $\phi _ { \nu }$ are orthonormal, it follows that the roughness penalty
$\| D ^ { 2 } x \| ^ { 2 }$ can be written as a weighted sum of squares of the coefficients
$\mathcal{C} _ { \mathcal{V} } :$

$$\| D ^ { 2 } x \| ^ { 2 } = \langle - \sum _ { v } \omega _ { v } ^ { 2 } c _ { v } \phi _ { v } , - \sum _ { v } \omega _ { v } ^ { 2 } c _ { v } \phi _ { v } \rangle = \sum _ { v } \omega _ { v } ^ { 4 } c _ { v } ^ { 2 } .$$

Now proceed by expanding the data functions to sufficient terms
in the basis to approximate them closely. We can use a fast Fourier
transform on a finely discretized version of the observed data functions
do this efficiently. Denote by $c _ { i }$ the vector of Fourier coefficients of the
observation $x _ { i } \left( s \right) ,$ so that $x _ { i } \left( s \right) = c _ { i } ^ { \prime } \phi \left( s \right)$ where $\phi$ is the vector of basis
functions. Let $\mathrm { V }$ be the covariance matrix of the vectors $c _ { i } ,$ and let $S$ be
the diagonal matrix with entries

$$S _ { v v } = \left( 1 + \lambda \omega _ { v } ^ { 4 } \right) ^ { - 1 / 2 } .$$

The matrix $S$ then corresponds to a smoothing operator $S .$

Let $y$ be the vector of coefficients of any principal component curve
$5 ,$ or

$$E \left( s \right) = \sum _ { v } \mathcal{Y} _ { v } \phi _ { v } \left( s \right) = y ^ { \prime } \phi \left( s \right) .$$
(7.7)

In terms of Fourier coefficients, the equation (7.5) can be written

$$V y = \rho S ^ { - 2 } y$$
(7.8)

which can be rewritten

$$\left( S V S \right) \left( S ^ { - 1 } y \right) = \rho \left( S ^ { - 1 } y \right) .$$
(7.9)

<!-- PageBreak -->

<!-- PageNumber="117" -->
<!-- PageHeader="7.4 Finding the regularized PCA in practice" -->

The matrix SVS is the covariance matrix of the vectors $\mathrm { S c } _ { i } ,$ the Fourier
coefficient vectors of the original data smoothed by the application of
the smoothing operator $S .$

To find the solutions of (7.9), suppose that $u$ is an eigenvector of
SVS with eigenvalue $\rho .$ Finding the eigenvectors and eigenvalues of
SVS corresponds precisely to carrying out an unsmoothed PCA of
the smoothed data $\mathrm { S c } _ { i } .$ Then it is apparent that any multiple of $S u$
is a solution of (7.9) for the same $\rho .$ Because we require $\| y \| ^ { 2 } = 1 ,$
renormalize and set $y = S u / \| S u \| .$ The functional principal component
$5$ corresponding to $\mathcal{Y}$ is then computed from (7.7).

Putting these steps together gives the following procedure for
carrying out the smoothed principal component analysis of the original
data:

1\. Compute the coefficients $c _ { i }$ for the expansion of each sample
function $x _ { i }$ in terms of basis $\phi .$

2\. Operate on these coefficients by the smoothing operator $S .$

3\. Carry out a standard PCA on the resulting smoothed coefficient
vectors $\mathrm { S c } _ { i } .$

4\. Apply the smoothing operator $S$ to the resulting eigenvectors $u ,$
and renormalize so that the resulting vectors $\mathcal{Y}$ have unit norm.

5\. Compute the principal component function $5$ from (7.7).


#### 7.4.2 The nonperiodic case

Now turn to the nonperiodic case, where Fourier expansions are no
longer appropriate because of the boundary conditions. Suppose that
$\left\{ \phi _ { v } \right\}$ is a suitable basis for the space of smooth functions $\mathcal{S}$ on
$\left[ 0 , 1 \right] .$ Possible bases include $B$ B-splines on a fine mesh, or possibly
orthogonal polynomials up to some degree. In either case, we choose
the dimensionality of the basis to represent the functions $x _ { i } \left( s \right)$ well. $\mathrm { A s }$
in the discussion of the periodic case, let $c _ { i }$ be the vector of coefficients
of the data function $x _ { i } \left( s \right)$ in the basis $\left\{ \phi _ { v } \right\} .$ Let $\mathrm { v }$ be the covariance
matrix of the vectors $c _ { i } .$

Define $\mathrm { J }$ to be the matrix $\int \phi \phi ^ { \prime } ,$ whose elements are $\langle \phi _ { j } , \phi _ { k } \rangle$ and $K$
the matrix whose elements are $\langle D ^ { 2 } \phi _ { j } , D ^ { 2 } \phi _ { k } \rangle .$ The penalized sample
variance can be written as

$$P C A P S V = \frac { \langle F , V S \rangle } { \| \sum \| ^ { 2 } + \lambda \| D ^ { 2 } E \| ^ { 2 } } = \frac { y ^ { \prime } V y } { y ^ { \prime } J y + \lambda y ^ { \prime } K y }$$
(7.10)

<!-- PageBreak -->

<!-- PageNumber="118" -->
<!-- PageHeader="7. Regularized principal components analysis" -->

and the eigenequation corresponding to (7.5) is given by

$$V y = \rho \left( J + \lambda K \right) y .$$
(7.11)

Now perform a factorization $L L ^ { \prime } = J + \lambda K$ and define $S = L ^ { - 1 } .$ We
can find a suitable matrix L by an SVD or by the standard numerical
linear algebra technique called Cholesky factorization, in which case L
is a lower triangular matrix. The equation (7.11) can now be written as

$$\left( S V S ^ { \prime } \right) \left( L ^ { \prime } y \right) = \rho L ^ { \prime } y .$$

We can now work through the same stages as for the periodic case,
keeping careful track whether to use the matrix $S$ or $S ^ { \prime }$ at each stage.
The algorithm obtained is as follows:

1\. Expand the observed data $x _ { i }$ with respect to the basis $\phi$ to obtain
coefficient vectors $c _ { i } .$

2\. Solve $L d _ { i } = c _ { i }$ for each $i$ to find the vectors $S c _ { i } = d _ { i } .$

3\. Carry out a standard PCA on the coefficient vectors $d _ { i } .$

4\. Apply the smoothing operator $S ^ { \prime }$ to the resulting eigenvectors $u$
by solving $L ^ { \prime } y = u$ in each case, and renormalize so that the
resulting vectors $\mathcal{Y}$ have $y ^ { \prime } J y = 1 .$

5\. Transform back to find the principal component functions $\xi$ using
(7.7).

If we use a B-spline basis and define L by a Cholesky factorization,
then the matrices J, $K$ and $L$ are all band matrices, and by using
appropriate linear algebra routines, we can carry out all the calculations
extremely economically. Even in the full matrix case, especially if not
too many basis functions are used, the computations are reasonably
fast because $S$ never has to be found explicitly.


### 7.5 Choosing the smoothing parameter by cross-validation

We now turn from algorithmic considerations to the question of how to
choose the smoothing parameter $\lambda$ in practice. Although it is perfectly
adequate for many purposes to choose the smoothing parameter
subjectively, we can also use a cross-validation approach to choose
the amount of smoothing automatically. Some general remarks about

<!-- PageBreak -->

<!-- PageNumber="119" -->
<!-- PageHeader="7.5 Choosing the smoothing parameter by cross-validation" -->

the use of automatic methods for choosing smoothing parameters are
found in Section 3.1 of Green and Silverman (1994).

To consider how a cross-validation score could be calculated,
suppose that $x$ is an observation from the population. Then, by
the optimal basis property discussed in Section 6.2.3, the principal
components have the property that, for each $m ,$ an expansion in terms
of the functions $\xi _ { 1 } , \ldots , \mathfrak{x} _ { m }$ can explain more of the variation in $x$ than
any other collection of $m$ functions.

Now let $\mathrm { G }$ be the $m \times m$ matrix whose $\left( i , j \right)$ element is the inner
product $\langle 5 i , 5 j .$ Then the component of $x$ orthogonal to the subspace
spanned by $\xi _ { 1 } , \ldots , \xi _ { m }$ can be expressed as

$$\zeta _ { m } = x - \sum _ { i = 1 } ^ { m } \sum _ { j = 1 } ^ { m } \left( G ^ { - 1 } \right) _ { i j } \langle E _ { i } , x \rangle S _ { j } .$$

If we wish to consider the efficacy of the first $m$ components, then a
measure to consider is $E \| f _ { m } \| ^ { 2 }$ in order not to be tied to a particular
$m ,$ we can, for example, minimize $\sum _ { m } E \| l _ { m } \| ^ { 2 } .$ In both cases, we do not
have new observations $x$ to work with, and the usual cross-validation
paradigm has to be used, as follows:

1\. Subtract the overall mean from the observed data $x _ { i } .$

2\. For a given smoothing parameter $\lambda ,$ let $\mathrm { g } _ { j } ^ { \left[ i \right] } \left( \lambda \right)$ be the estimate of
$5 ;$ obtained from all the data except $x _ { i } .$

3\. Define $\zeta _ { m } ^ { \left[ i \right] } \left( \lambda \right)$ to be the component of $x _ { i }$ orthogonal to the
subspace spanned by $\left\{ E _ { j } ^ { \left[ i \right] } \left( \lambda \right) : j = 1 , \ldots , m \right\} .$

4\. Combine the $\zeta _ { m } ^ { \left[ i \right] } \left( \lambda \right)$ to obtain the cross-validation scores

$$C V _ { m } \left( \lambda \right) = \sum _ { i = 1 } ^ { n } \| \zeta _ { m } ^ { \left[ i \right] } \left( \lambda \right) \| ^ { 2 }$$
(7.12)

and hence

$$C V \left( \lambda \right) = \sum _ { m = 1 } ^ { \infty } C V _ { m } \left( \lambda \right) .$$
(7.13)

In practice, we would of course truncate the sum in (7.13) at some
convenient point. Indeed, given $n$ data curves, we can estimate
at most $n \quad - \quad 1$ principal components, and so the sum must be
truncated at $m = n \quad - \quad 1$ if not at a smaller value.

5\. Minimize $\mathrm { C V } \left( \lambda \right)$ to provide the choice of smoothing parameter.

Clearly there are other possible ways of combining the $\mathrm { C V } _ { m } \left( \lambda \right)$ to
produce a cross-validation score to account for more than one value
of $m ,$ but we restrict attention to $\mathrm { C V } \left( \lambda \right)$ as defined in (7.13).

<!-- PageBreak -->

<!-- PageNumber="120" -->
<!-- PageHeader="7. Regularized principal components analysis" -->


<figure>
<figcaption>FIGURE 7.3. The first four smoothed principal components for the pinch force data, smoothed by the method of Section 7.3. The smoothing parameter is chosen by cross-validation.</figcaption>

2

1234

Squeeze

0

T

vi

0

20

40

60

80

100

Time

</figure>


### 7.6 An example: The pinch force data

We can now apply the smoothing method to the unsmoothed
pinch force data. Figure 7.3 shows the effect of applying principal
components analysis using the method for smoothed PCA set out
above. We choose the smoothing parameter to minimize the score $\mathrm { C V } \left( \lambda \right)$
defined in Section 7.5. It was found satisfactory to calculate the cross-
validation score on a grid (on a logarithmic scale) of values of the
smoothing parameter $\lambda$ and pick out the minimum. The grid can be
quite coarse, since small changes in the numerical value of $\lambda$ do not
make very much difference to the smoothed principal components. For
this example, we calculated the cross-validation scores for $\lambda = 0$ and
$\lambda = 1 . 5 ^ { i - 1 }$ for $i = 1 , \ldots , 3 0 ,$ and we attained the minimum of $\mathrm { C V } \left( \lambda \right)$ by
setting $\lambda = 3 7 .$ The smoothing method achieves the aim of removing
the considerable roughness in the raw principal component curves in
Figure 7.2.

Figure 7.4 displays the effects on the mean curve of adding and
subtracting a multiple of each of the first four smoothed principal
components. The first component corresponds to an effect whereby the
shape of the impulse is not substantially changed, but its overall scale is
increased. The second component (with appropriate sign) corresponds

<!-- PageBreak -->

<!-- PageNumber="121" -->
<!-- PageHeader="7.6 An example: The pinch force data" -->


<figure>
<figcaption>FIGURE 7.4. The effect on the overall mean curve of adding and subtracting a suitable multiple of each of the first four smoothed principal component curves provided in Figure 7.3.</figcaption>

Principal component 1

Principal component 2

Squeeze

1000 2000 3000

Squeeze

1000 2000 3000

O

O

0

20

40

60

80

100

0

20

40

60

80

100

Time

Time

Principal component 3

Principal component 4

Squeeze

0 500 1500 2500

Squeeze

0 500 1500 2500

0

20

40

60

80

100

0

20

40

60

80

100

Time

Time

</figure>


roughly to a compression in the overall time scale during which the
squeeze takes place. Both of these effects were removed in the analysis
of Ramsay, Wang and Flanagan (1995) before any detailed analysis
was carried out. It is, however, interesting to note that they occur
as separate components and therefore are essentially uncorrelated
with one another, and with the effects found subsequently. The third
component corresponds to an effect whereby the main part takes place
more quickly but the tail after the main part is extended to the right. The
fourth component corresponds to a higher peak correlated with a tail-
off that is faster initially but subsequently slower than the mean. The
first and second effects are transparent in their interest, and the third
and fourth are of biomechanical interest in indicating how the system
compensates for departures from the (remarkably reproducible) overall
mean. The smoothing we have described makes the effects very much
clearer than they are in the raw principal component plot.

The estimated variances $\sigma ^ { 2 }$ indicate that the four components
displayed respectively explain 86.2%, 6.7%, 3.5% and 1.7% of the
variability in the original data, with 1.9% accounted for by the remaining
components. The individual principal component scores indicate that
there is one curve with a fairly extreme value of principal component 2

<!-- PageBreak -->

<!-- PageNumber="122" -->
<!-- PageHeader="7. Regularized principal components analysis" -->


<figure>
<figcaption>FIGURE 7.5. The pinch force data curves, smoothed by a roughness penalty method with the same smoothing parameter as used for the smoothed PCA, and with the baseline pressure subtracted.</figcaption>

3000

Squeeze

2000

1000

0

0

20

40

60

80

100

Time

</figure>


(corresponding to moving more quickly than average through the cycle)
but this curve is not unusual in other respects.


### 7.7 Smoothing the data rather than the PCA

In this section, we compare the method of regularized principal
components analysis with an approach akin to that discussed earlier in
the book. Instead of carrying out our smoothing step within the PCA,
we smooth the data first, and then carry out an unsmoothed PCA. This
approach to functional PCA was taken by Besse and Ramsay (1986),
Ramsay and Dalzell (1991) and Besse, Cardot and Ferraty (1997). Of
course, conceivably any smoothing method can be used to smooth
the data, but to make a reasonable comparison, we use a roughness
penalty smoother based on integrated squared second derivative. For
simplicity, let us restrict our attention to the case of periodic boundary
conditions.

Suppose that $x$ is a data curve, and that we regard $x$ as the sum of
a smooth curve and a noise process. We would obtain the roughness
penalty estimate of the smooth curve by minimizing

$$= \| x - g \| ^ { 2 } + \lambda \| D ^ { 2 } g \| ^ { 2 }$$

<!-- PageBreak -->

<!-- PageNumber="123" -->
<!-- PageHeader="7.7 Smoothing the data rather than the PCA" -->


<figure>
<figcaption>FIGURE 7.6. The first four principal component curves of the smoothed data as shown in Figure 7.5.</figcaption>

2

1

3

1

Squeeze

0

47

$\mathrm { N }$

0

20

40

60

80

100

Time

</figure>


over $g$ in S. $A s$ usual, $\lambda$ is a smoothing parameter that controls
the tradeoff between fidelity to the data and smoothing. This is a
generalization of the spline smoothing method discussed in Chapter
4 to the case of functional data.

Consider an expansion of $x$ and $g$ in terms of Fourier series as in
Section 7.4.1, and let $c$ and $d$ be the resulting vectors of coefficients.
Then

$$P E N R S S = \| c - d \| ^ { 2 } + \lambda \sum _ { v } w _ { v } ^ { 4 } d _ { v } ^ { 2 } ,$$

and hence the coefficients of the minimizing $g$ satisfy

$$d = S ^ { 2 } c$$
(7.14)

where $\mathrm { s }$ is as defined in Section 7.4.1. Note that this demonstrates that
the smoothing operator S used twice in the algorithm set out in Section
7.4.1 can be regarded as a half-spline-smooth, since $s ^ { 2 }$ is the operator
corresponding to classical spline smoothing.

Now let us consider the effect of smoothing the data by the operator
$s ^ { 2 }$ using the same smoothing parameter $\lambda = 3 7$ as in the construction
of Figures 7.3 and 7.4. The effect of this smoothing on the data
is illustrated in Figure 7.5. Figure 7.6 shows the first four principal
component curves of the smoothed data. Although the two methods do

<!-- PageBreak -->

<!-- PageNumber="124" -->
<!-- PageHeader="7. Regularized principal components analysis" -->

not give identical results, the differences between them are too small
to affect any interpretation.

However, this favourable comparison depends rather crucially on the
way in which the data curves are smoothed, and in particular on the
match between the smoothing level implied in (7.14) and the smoothing
level used for the PCA itself. For example, we tried smoothing the force
functions curves individually, selecting the smoothing parameters by
the generalized cross-validation approach used in the S-PLUS function
smooth. spline. The result was much less successful, in the sense that
the components were far less smooth. The reason appears to be that
this smoothing technique tended to choose much smaller values of the
smoothing parameter $\lambda .$

Kneip (1994) considers several aspects of an approach that first
smooths the data and then extracts principal components. Under a
model where the data are corrupted by a white noise error process, he
investigates the dependence of the quality of estimation of the principal
components on both sample size and sampling rate. In an application
based on economics data, he shows that smoothing is clearly beneficial
in a practical sense.


### 7.8 The procedure of Rice and Silverman

Another approach to the smoothing of functional PCA was set out
by Rice and Silverman (1991). They considered a stepwise procedure
incorporating the roughness penalty in a different way. Their proposal
requires a separate smoothing parameter $\lambda _ { j }$ for each principal
component. The principal components are estimated successively. The
estimate $5 _ { j } ^ { \dagger }$ of $\mathfrak{z} _ { j }$ being found by maximizing $\langle E , V E \rangle - \lambda _ { j } \| D ^ { 2 } E \| ^ { 2 }$ subject
to the conventional orthonormality conditions $\| \xi \| ^ { 2 } = 1$ and $\langle E , E _ { k } ^ { \dagger } \rangle = 0$
for $k = 1 , \ldots , j - 1 .$

This approach is computationally more complicated because a
separate eigenproblem has to be posed and solved for each principal
component; for more details, see the original paper. Theoretical results
in Pezzulli and Silverman (1993) and Silverman (1996) also suggest that
the procedure described in Section 7.2 is likely to be advantageous
under conditions somewhat milder than those for the Rice-Silverman
procedure.

<!-- PageBreak -->


## 8 Principal components analysis of mixed data


### 8.1 Introduction

It is a characteristic of statistical methodology that problems do not
always fall into neat categories. In the context of the methods discussed
in this book, we often have both a vector of data and an observed
function on each individual of interest. In this chapter, we consider
some ways of approaching such mixed data, extending the ideas of
PCA that we have already developed.

In Chapter 5 we have discussed one way in which mixed data
can arise. In certain cases, it is appropriate or desirable to register
the observed curves with one another, for example by shifting each
one in time or by adding a constant to each one. This procedure
yields mixed data: The vector of data consists of the parameters
of the transformation that best maps the observed function to the
overall mean, and the transformed function can be thought of as a
functional observation in its own right. The methods we discuss in
this chapter incorporate this registration process into the principal
components analysis, and we illustrate our methodology using the
Canadian temperature data as an example.

Of course, there are many other situations where we have numerical
observations as well as functional observations on the individuals of
interest, and the PCA methodology we set out can be easily generalized
to deal with them.

<!-- PageBreak -->

<!-- PageNumber="126" -->
<!-- PageHeader="8. Principal components analysis of mixed data" -->


### 8.2 General approaches to mixed data

Suppose that we observe a function $x _ { i }$ and a number (or a vector of
numbers) $\mathcal{Y} _ { i }$ for each individual in our sample, How might we use PCA
to analyse such data?

There are three different ways of viewing the $\mathcal{Y} _ { i } .$ First, it may be that
the $\mathcal{Y} _ { i }$ are simply nuisance parameters, of no real interest to us in the
analysis, for example corresponding to the time at which a recording
instrument is activated. In this case we would quite simply ignore them.
The $\mathcal{Y} _ { i }$ can be thought of as one of the features of almost all real data
sets that we choose not to include in the analysis.

On the other hand, both the functions $x _ { i }$ and the observations $\mathcal{Y} _ { i }$
may be of primary importance. This is the case to which we give
the most attention, from Section 8.3 onwards. Thus, we have hybrid
data $\left( x _ { i } , y _ { i } \right) ,$ and investigate to what extent our PCA methodology
can be extended to this situation. There is some connection with the
methodology described in Section 6.5 for bivariate curve data with
values $\left( x _ { i } \left( t \right) , y _ { i } \left( t \right) \right) ,$ though the data under present consideration
consist of pairs where only one component of the vector $\left( x _ { i } , y _ { i } \right)$ is
itself a function.

As a third and somewhat intermediate possibility, the $\mathcal{Y} _ { i }$ may be
of marginal importance, our central interest being in the functions
$x _ { i } .$ In this case, we could ignore the $y _ { i }$ initially and carry out a PCA
of the curves $x _ { i } \left( t \right)$ alone. Having done this, we could investigate the
connection between the scores on the principal component scores
and the variable(s) $\mathcal{Y} _ { i } .$ We could calculate the sample correlations
between the principal component scores and the components of the $\mathcal{Y} _ { i } .$
Alternatively or additionally, we could plot the $\mathcal{Y} _ { i }$ against the principal
component scores or use other methods for investigating dependence.
In this general approach, the $\mathcal{Y} _ { i }$ would not have been used in the first
part of the analysis itself; however, they would have played a key part in
interpreting the analysis. It would be interesting, for example, to notice
that a particular principal component of the $x _ { i }$ was highly correlated
with $\mathcal{Y} _ { i } .$ We develop this approach further in Section 8.5.


### 8.3 The PCA of hybrid data


#### 8.3.1 Combining function and vector spaces

Now suppose that our observations consist of pairs $\left( x _ { i } , y _ { i } \right) ,$ where $x _ { i }$
is a function on the interval $T$ and $\mathcal{Y} _ { i }$ is a vector of length $M .$ How

<!-- PageBreak -->

<!-- PageNumber="127" -->
<!-- PageHeader="8.3 The PCA of hybrid data" -->

would we define a principal component of variation of such data? A
typical principal component weight function would consist of a pair
$\left( 5 , v \right) ,$ where $v$ is an M-vector, and the principal component score of $a$
particular observation would then be the sum

$$\eta _ { i } = \langle x _ { i } , 5 \rangle + \langle y _ { i } , v \rangle = \int x _ { i } \left( s \right) 5 \left( s \right) d s + y _ { i } ^ { \prime } v .$$
(8.1)

Another way of saying this is that the principal component would be
made up of a functional part $5$ and a vector part $v ,$ corresponding to the
functional and vector (or numerical) parts of the original data. A typical
observation from the distribution of the data would be modelled as

$$\left( \begin{array}{} { x _ { i } } \\ { y _ { i } } \end{array} \right) = \sum _ { j } \eta _ { i j } \left( \begin{array}{} { 5 j } \\ { v _ { j } } \end{array} \right) .$$
(8.2)

where $\left( E _ { j } , v _ { j } \right)$ is the $j$ jth principal component weight and, as $j$ varies,
the vectors of principal component scores $\eta _ { i j } = \langle x _ { i } , E _ { j } \rangle + \langle y _ { i } , v _ { j } \rangle$ are
uncorrelated variables with mean zero.

This kind of hybrid data PCA can very easily be dealt with in our
general functional framework. Define $\mathcal{Z}$ to the space of pairs $z = \left( x , y \right) ,$
where $x$ is a smooth function and $\mathcal{Y}$ is a vector of length $M .$ Given any
two elements $z ^ { \left( 1 \right) } = \left( x ^ { \left( 1 \right) } , y ^ { \left( 1 \right) } \right)$ and $z ^ { \left( 2 \right) } = \left( x ^ { \left( 2 \right) } , y ^ { \left( 2 \right) } \right)$ of $Z ,$ define the
inner product

$$\langle z ^ { \left( 1 \right) } , z ^ { \left( 2 \right) } \rangle = \langle x ^ { \left( 1 \right) } , x ^ { \left( 2 \right) } \rangle + \langle y ^ { \left( 1 \right) } , y ^ { \left( 2 \right) } \rangle$$
(8.3)

where the inner product between the $x ^ { \prime } s$ is the usual functional inner
product $\int x ^ { \left( 1 \right) } x ^ { \left( 2 \right) } ,$ and the inner product of the $\mathcal{Y} ^ { \prime } s$ is the vector inner
product $y ^ { \left( 1 \right) ^ { \prime } } y ^ { \left( 2 \right) } .$ From (8.3) we can define the norm $\| z \| ^ { 2 } = \langle z , z \rangle$ of
$a n y \quad z \quad i n \quad Z .$

Now that we have defined an inner product and norm on $Z ,$ write $z _ { i }$
for the data pair $\left( x _ { i } , y _ { i } \right) .$ To find the leading principal component, we
wish to find $\left( = \left( , v \right) \right.$ in $Z$ to maximize the sample variance of the
$\langle 5 , z _ { i } \rangle$ subject to $| | \zeta | | ^ { 2 } = 1 .$ The $\langle \zeta , z _ { i } \rangle$ are of course exactly the same
as the quantities $\eta _ { i } = \int x _ { i } \left( s \right) 5 \left( s \right) d s + y _ { i } ^ { \prime } v$ specified in equation (8.1).

Subsequent principal components maximize the same sample
variance subject to the additional condition of orthogonality to the
principal components already found, orthogonality being defined by
the hybrid inner product (8.3). Principal components found in this way
yield principal component scores that are uncorrelated, just as for
conventional multivariate PCA.

The PCA of hybrid data is thus very easily specified in principle.
However, there are several important issues raised by this idea, and
we discuss these in the following sections.

<!-- PageBreak -->

<!-- PageNumber="128" -->
<!-- PageHeader="8. Principal components analysis of mixed data" -->


#### 8.3.2 Finding the principal components in practice

How do we carry out the constrained maximization of the sample
variance of the $\langle \zeta , z _ { i } \rangle$ in practice? Suppose that $\phi _ { k }$ is a basis of $K$
functions in which the functional parts $x _ { i }$ of the hybrid data $z _ { i }$ can
be well approximated. Given any element $z = \left( x , y \right)$ of $Z ,$ define the
K-vector $c$ to be the coefficients of $x$ relative to the basis $\phi _ { k } .$ Now let
$p = K + M ,$ and let $w$ be the p-vector

$$w = \left[ \begin{array}{} { c } \\ { y } \end{array} \right] .$$

Suppose that the basis $\phi _ { k }$ is an orthonormal basis, the Fourier
functions, for example. Then the inner product (8.3) of any two
elements $z ^ { \left( 1 \right) }$ and $z ^ { \left( 2 \right) }$ of $\mathcal{Z}$ is precisely equal to the ordinary vector inner
product $\langle w ^ { \left( 1 \right) } , w ^ { \left( 2 \right) } \rangle$ of the corresponding $p$ p-vectors of coefficients.
Thus, if we use this method of representing members of $Z$ by vectors,
we have a representation in which the vectors behave exactly as if
they were $p$ p-dimensional multivariate observations, with the usual
Euclidean inner product and norm. It follows that we can use standard
multivariate methods to find the PCA.

In summary, we can proceed as follows to carry out a PCA:

1\. For each $i ,$ let $c _ { i }$ be the vector of the first $K$ Fourier coefficients
of $x _ { i } .$

2\. Augment each $c _ { i }$ by $\mathcal{Y} _ { i }$ to form the p-vector $w _ { i } .$

3\. Carry out a standard PCA of the $w _ { i } ,$ by finding the eigenvalues
and eigenvectors of the matrix $N ^ { - 1 } \sum _ { i } w _ { i } w _ { i } ^ { \prime } .$

4\. If $u$ is any resulting eigenvector, the first $K$ elements of $u$ are
the Fourier coefficients of the functional part of the principal
component, and the remaining elements are the vector part.

Since the procedure we have set out is a generalization of ordinary
functional PCA, we may wish to incorporate some smoothing, and this
is discussed in the next section.


#### 8.3.3 Incorporating smoothing

To incorporate smoothing into our procedure, we can easily generalize
the smoothing methods discussed in Chapter 7. The key step in the
method is to define the roughness of an element $z = \left( x , y \right)$ of $Z .$ Let
us take the roughness of $z$ to be that of the functional part $x$ of z,

<!-- PageBreak -->

<!-- PageNumber="129" -->
<!-- PageHeader="8.3 The PCA of hybrid data" -->

without any reference to the vector part $y .$ To do this, define $D ^ { 2 } z$ to be
equal to the element $\left( D ^ { 2 } x , 0 \right)$ of $Z$ so that the roughness of $z$ can then
be written $\| D ^ { 2 } z \| ^ { 2 } ,$ just as in the ordinary functional case. The norm
is taken in $\mathcal{Z} ,$ but since the vector part of $D ^ { 2 } z$ is defined to be zero,
$\| D ^ { 2 } z \| ^ { 2 } = \| D ^ { 2 } x \| ^ { 2 }$ as required.

Once we have defined the roughness of $z ,$ we can proceed to carry
out a smoothed PCA using exactly the same ideas as in Chapter
7. The smoothed principal components are found by solving the
eigenequation

$$V \zeta = \rho \left( I + \lambda D ^ { 4 } \right) \zeta$$

for $\left( \right.$ in $Z ,$ and all the general ideas of Chapter 7 carry over. As
far as algorithms are concerned, the Fourier transform algorithm
for the periodic case requires slight modification. If $z$ is the vector
representation of an element $z ,$ then the first $K$ elements of $z$ refer
to the functional part, and so the roughness of $z$ is $\sum _ { k = 0 } ^ { K - 1 } \omega _ { k } ^ { 4 } z _ { k } ^ { 2 } ,$ rather
than allowing the sum to extend over all $k .$ It follows that the matrix
S used in the algorithm described in Section 7.4.1 must be modified to
have diagonal elements $\left( 1 + \lambda w _ { k } ^ { 4 } \right) ^ { - 1 / 2 }$ for $k < K ,$ and 1 for $K \leq k < p .$

Apart from this modification, and of course the modified procedures
for mapping between the function/vector and basis representations of
elements of $Z ,$ the algorithm is exactly the same as in Section 7.4.1.
Furthermore, the way in which we can apply cross-validation to choose
the smoothing parameter is the same as in Section 7.5.

To deal with the nonperiodic case, we modify the algorithm of Section
7.4.2 in the same way. The matrix J is a block diagonal matrix where
the first $K$ rows and columns have elements $\langle \phi _ { j } , \phi _ { k } \rangle$ and the last $M$
rows and columns are the identity matrix of order $M .$ The matrix K has
elements $\langle D ^ { 2 } \phi _ { j } , D ^ { 2 } \phi _ { k } \rangle$ in its first $K$ rows and columns, and zeroes
elsewhere.


#### 8.3.4 Balance between functional and vector variation

Readers who are familiar with PCA may have noted one potential
difficulty with the methodology set out above. The variations in the
functional and vector parts of a hybrid observation $z$ are really like
chalk and cheese: They are measured in units which are almost
inevitably not comparable, and therefore it may well not be appropriate
to weight them as we have. In the registration example, the functional
part consists of the difference between the pattern of temperature on
the transformed time scale and its population mean; the vector part is
made up of the parameters of the time transformation. Clearly, these
are not measured in directly compatible units!

<!-- PageBreak -->

<!-- PageNumber="130" -->
<!-- PageHeader="8. Principal components analysis of mixed data" -->

One way of noticing the effect of noncomparability is to consider
the construction of the inner product (8.3) on $Z ,$ which we defined by
adding the inner product of the two functional parts and that of the
two vector parts. In many problems, there is no intrinsic reason to give
these two inner products equal weight in the sum, and a more general
inner product we could consider is

$$\langle z ^ { \left( 1 \right) } , z ^ { \left( 2 \right) } \rangle = \langle x ^ { \left( 1 \right) } , x ^ { \left( 2 \right) } \rangle + C ^ { 2 } \langle y ^ { \left( 1 \right) } , y ^ { \left( 2 \right) } \rangle$$
(8.4)

for some suitably chosen constant $C .$ Often, the choice of $C$ (for
example $\left. C = 1 \right)$ is somewhat arbitrary, but we can make some remarks
that may guide its choice.

First, if the interval $T$ is of length $| T | ,$ then setting $C ^ { 2 } = | T |$ gives
the same weight to overall differences between $x ^ { \left( 1 \right) }$ and $x ^ { \left( 2 \right) }$ as to
differences of similar size in a single component of the vector part
$\mathcal{Y} .$ If the measurements are of cognate or comparable quantities, this
may well be a good method of choosing $C .$ On the other hand, setting
$C ^ { 2 } = | T | / M$ tends to weight differences in functional parts the same
as differences in all vector components.

Another approach, corresponding to the standard method of PCA
relative to correlation matrices, is to ensure that the overall variability
in the functional parts is given weight equal to that in the vector part.
To do this, we would set

$$C ^ { 2 } = \frac { \sum _ { i } \| x _ { i } - \bar { x } \| ^ { 2 } } { \sum _ { i } \| y _ { i } - \bar { y } \| ^ { 2 } }$$

taking the norm in the functional sense in the numerator, and in the
usual vector sense in the denominator.

Finally, in specific problems, there may be a particular rationale for
some other choice of constant $C ^ { 2 } ,$ an example of which is discussed in
Section 8.4.

Whatever the choice of $C ^ { 2 } ,$ the most straightforward algorithmic
approach is to construct the vector representation $z$ of any element
$z = \left( x , y \right)$ of $\mathcal{Z}$ to have last $M$ elements $C y ,$ rather than just $y .$ The
first $K$ elements are the coefficients of the representation of $x$ in an
appropriate basis, as before. With this modification, we can use the
algorithms set out above. Some care must be taken in interpreting the
results, however, because any particular principal component weight
function has to be combined with the data values using the inner
product (8.4) to get the corresponding principal component scores.

<!-- PageBreak -->

<!-- PageNumber="131" -->
<!-- PageHeader="8.4 Combining registration and PCA" -->


### 8.4 Combining registration and PCA


#### 8.4.1 Expressing the observations as mixed data

We now return to the special case of mixed data obtained by registering
a set of observed curves. For the moment, concentrate on data that may
be assumed to be periodic on $\left[ 0 , 1 \right] .$ We suppose that an observation
can be modelled as

$$x \left( t + \tau \right) = \mu \left( t \right) + \sum _ { j } \eta _ { j } \xi _ { j } \left( t \right)$$
(8.5)

for a suitable sequence of orthonormal functions $\mathfrak{z} _ { j } ,$ and where $\eta _ { j }$
are uncorrelated random variables with mean zero and variances $\sigma _ { j } ^ { 2 } .$
The model (8.5) differs from the usual PCA model in allowing for a
shift in time T as well as for the addition of multiples of the principal
component functions. Because of the periodicity, the shifted function
$x \left( t + \tau \right)$ may still be considered as a function on $\left[ 0 , 1 \right] .$

Given a data set $x _ { 1 } , \ldots , x _ { n } ,$ we can use the Procrustes approach
set out in Chapter 5 to obtain an estimate $\widehat { \mu }$ of $\mu$ and to give values
of the shifts $\tau _ { 1 } , \ldots , \tau _ { n }$ appropriate to each observation. Then we
can regard the data as pairs $z _ { i } = \left( \widetilde { x } _ { i } , \tau _ { i } \right) ,$ where the $\tau _ { i }$ are the
estimated values of the shift parameter and the $\widetilde { x } _ { i }$ are the shifted
mean-corrected temperature curves with values $x _ { i } \left( t + \tau _ { i } \right) - \widehat { \mu } \left( t \right) .$ Recall
that a consequence of the Procrustes fitting is that the $\widetilde { x } _ { i }$ satisfy the
orthogonality property

$$\langle \widetilde { x } _ { i } , D \widehat { \mu } \rangle = 0 .$$
(8.6)


#### 8.4.2 Balancing temperature and time shift effects

We can now consider the different approaches set out in Section 8.2 to
the analysis of the mixed data $z _ { i } .$ We do not discuss in any detail the
approach where the vector components are simply discarded, because
that reduces to the case of pure functional data already considered in
previous chapters. Anyway, it is clear that it would not be appropriate to
ignore the transformation parameters in the weather example, and so
we consider the approaches that take account of them in the analysis.

We consider mainly the methodology set out in Section 8.3, and seek
principal components $\left( 5 , v \right)$ that have two effects within the model
(8.5): the addition of the function $E$ to the overall mean $\widehat { \mu } ,$ together
with a contribution of $v$ to the time shift $T .$

In the special case of the registration data, there is a natural way
of choosing the constant $C ^ { 2 }$ that controls the balance between the

<!-- PageBreak -->

<!-- PageNumber="132" -->
<!-- PageHeader="8. Principal components analysis of mixed data" -->

functional and shift components in the inner product (8.4). Suppose
that $x$ is a function in the original data function space, and that
$z = \left( \widetilde { x } , \tau \right)$ is the corresponding pair in $Z ,$ so that

$$x \left( t \right) = \widehat { \mu } \left( t - \tau \right) + \widetilde { x } \left( t - \tau \right) .$$

Because of the orthogonality property (8.6), we can confine attention to
$\widetilde { \mathrm { x } }$ that are orthogonal to $\widehat { \mu } .$

To define a norm on $Z ,$ a requirement is that, at least to first order,

$$\| z \| ^ { 2 } \approx \| x - \widehat { \mu } \| ^ { 2 } = \int \left[ x \left( s \right) - \widehat { \mu } \left( s \right) \right] ^ { 2 } d s ,$$
(8.7)

the standard squared function norm for $x - \widehat { \mu } .$ This means that the
norm of any small perturbation of the mean function $\widehat { \mu }$ must the same,
whether it is specified in the usual function space setting as $x - \widehat { \mu } ,$ or
expressed as a pair $z$ in $Z ,$ consisting of a perturbation $\widetilde { \mathrm { x } }$ orthogonal
to $\widehat { \mu }$ and a time shift.

Suppose $\| \widetilde { x } \|$ and $T$ are small. If we let

$$C ^ { 2 } = \| D \widehat { \mu } \| ^ { 2 }$$
(8.8)

then, to first order in $\| \widetilde { x } \|$ and $T ,$

$$x \left( t \right) - \widehat { \mu } \left( t \right) \approx - \tau D \widehat { \mu } \left( t - \tau \right) + \widetilde { x } \left( t - \tau \right) .$$

By the orthogonality of $\widetilde { \mathrm { x } }$ and $D \widehat { \mu } ,$

$$\| z - \widehat { \mu } \| ^ { 2 } \approx \int \widetilde { x } ^ { 2 } \left( s \right) + C ^ { 2 } \tau ^ { 2 } \left( s \right) d s = \| \widetilde { x } \| ^ { 2 } + C ^ { 2 } \| \tau \| ^ { 2 } ,$$
(8.9)

as required.

With this calculation in mind, we perform our PCA of the pairs $\left( \widetilde { \mathrm { x } } _ { i } , \tau _ { i } \right)$
relative to the inner product (8.4) with $C ^ { 2 } = \| D \widehat { \mu } \| ^ { 2 } .$


#### 8.4.3 Application to the weather data

The application of this procedure to the Canadian temperature data
is set out in Figure 8.1. For each PC, it illustrates the effect on the
overall mean $\widehat { \mu }$ of adding and subtracting a suitable multiple of the
$E _ { j } .$ Note that $\widehat { \mu }$ is now the mean of the registered temperature curves,
not of the original curves. We use the same multiple of the PC curve in
each case, but of course it is no longer true that the square integral of
the PC curves is equal to one. In particular, the curve part of principal
component 3 yields much less variability about the mean curve than
the other principal components. In each case, the sign of the principal

<!-- PageBreak -->

<!-- PageNumber="133" -->
<!-- PageHeader="8.4 Combining registration and PCA" -->


<figure>
<figcaption>FIGURE 8.1. The mean Canadian temperature curve and the effects of adding and subtracting a suitable multiple of each PC curve, with the shift considered as a separate parameter.</figcaption>

Temperature (degrees C)

PC 1 (89.1% of variability)

PC 2 (8.2% of variability)

-20 -10 0 10 20

Temperature (degrees C)

20 -10 0 10 20

Shift 0 days
(0% of variability of this PC)

Shift 1.8 days

(10.7% of variability of this PC)

0.0 0.2 0.4 0.6 0.8 1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of annual cycle

Proportion of annual cycle

Temperature (degrees C)

PC 3 (1.9% of variability)

Temperature (degrees C)

PC 4 (0.5% of variability)

-20 -10 0 10 20

-20 -10 0 10 20

Shift 4.6 days
(71.7% of variability of this PC)

Shift 1.5 days

(7.5% of variability of this PC)

0.0 0.2 0.4 0.6 0.8 1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of annual cycle

Proportion of annual cycle

</figure>


component has been taken to make the shift positive; this is by no
means essential, but it leads to some simplicity of interpretation.

Each panel shows the shift part of the corresponding principal
component. We see that principal component 3 has a large shift
component. The percentage of variability of each principal component
due to the shift is worked out as $1 0 0 C ^ { 2 } v _ { j } ^ { 2 }$ with $C$ defined as in (8.8). A
principal component that is entirely shift would correspond to a shift
of ±5.4 days.

A comparison between Figure 8.1 and Figure 6.2 is instructive. First,
we see that the percentage of variation explained by each of the first
four principal components is very similar, but not identical, in the two
analyses. This is a consequence of using the inner product derived
in Section 8.4.2, which ensures approximate compatibility between
the quantification of variation caused simply by the addition of a
curve to the overall mean, and variation that also involves a time
shift. Because the shift component has been explicitly separated out,
less skill is needed to interpret the principal components. Principal
component 2 shows a small shift associated with a reduction of the
annual temperature range. The large shift in principal component 3 is
associated with a small increase in the midsummer temperature.

<!-- PageBreak -->

<!-- PageNumber="134" -->
<!-- PageHeader="8. Principal components analysis of mixed data" -->


#### 8.4.4 Taking account of other effects

In the temperature example, the shift effect is not necessarily the only
effect that can be extracted explicitly and dealt with separately in the
functional principal components analysis. We must also take account
of the overall annual average temperature for each weather station, and
we do this by extending the model (8.5) to a model of the form

$$x \left( t + \tau \right) - \theta = \alpha + \mu \left( t \right) + \sum _ { j } \eta _ { j }$$
(8.10)

where $\theta$ is an annual temperature effect with zero population mean.
The $\eta _ { j }$ are assumed to be uncorrelated random variables with mean
zero. The parameter $\alpha$ is the overall average temperature (averaged
both over time and over the population). For identifiability we assume
that $\int \mu \left( s \right) d s = 0 .$

The data we would use to fit such a model consist of triples
$\left( \check { x } _ { i } , \tau _ { i } , \theta _ { i } \right) ,$ where $\check { \mathrm { x } } _ { i }$ are the observed temperature curves registered to
one another by shifts $\tau _ { i } ,$ and with each curve modified by subtracting its
overall annual average $\widehat { \alpha } + \theta _ { i } .$ Here the number $\widehat { \alpha }$ is the time average of
all the temperatures observed at all weather stations, and the individual
$\theta _ { i }$ therefore sum to zero. Because the annual average $\widehat { \alpha } + \theta _ { i }$ has been
subtracted from each curve $\check { \mathrm { x } } _ { i } ,$ the curves $\check { \mathrm { x } } _ { i }$ each integrate to zero
as well as satisfying the orthogonality condition (8.6). The mean curve
$\widehat { \mu }$ is then an estimate of the mean of the registered curves $\check { x } _ { i _ { 1 } } ,$ most
straightforwardly the sample mean. In the hybrid data terms we have
set up, the functional part of each data point is the curve $\check { \mathrm { x } } ,$ whereas
the vector part is the 2-vector $\left( \tau _ { i } , \theta _ { i } \right) ^ { \prime } .$

To complete the specification of (8.10) as a hybrid data principal
components model, we regard T and $\theta$ as random variables which can
be expanded for the same $\eta _ { j } ,$ as

$$\tau = \sum _ { j } \eta _ { j } v _ { j } \text { and } \theta = \sum _ { j } \eta _ { j } u _ { j } ,$$

where the $\upsilon _ { j }$ and $u _ { j }$ are fixed quantities. Thus, the $j$ jth principal
component is characterized by a triple $\left( E _ { j } , v _ { j } , u _ { j } \right) ,$ constituting a
distortion of the mean curve by the addition of a multiple of $E _ { j } ,$ together
with shifts in time and in overall temperature by the same multiples of
$v _ { j }$ and $u _ { j } ,$ respectively.

Just as before, we carry out a PCA of the hybrid data $\left\{ \left( \check { x } _ { i } , \tau _ { i } , \theta _ { i } \right) \right\}$
with respect to a suitably chosen norm. To define the norm of a triple
$\left( x , \tau , \theta \right) ,$ consider the corresponding unregistered and uncorrected
curve $x ,$ defined by

$$x \left( t + \tau \right) = \widehat { \alpha } + \theta + \widehat { \mu } \left( t \right) + \check { x } \left( t \right) .$$

<!-- PageBreak -->

<!-- PageNumber="135" -->
<!-- PageHeader="8.4 Combining registration and PCA" -->


<figure>
<figcaption>FIGURE 8.2. The mean Canadian temperature curve and the effect of adding and subtracting a suitable multiple of each PC curve, with the shift and annual average temperature considered as separate parameters.</figcaption>

Temperature (degrees C)

PC 1 (89.1% of variability)

PC 2 (8.2% of variability)

-20 -10 0 10 20

Temperature (degrees C)

-20 -10 0 10 20

Shift 0 days
Temperature 0.92 degrees

Shift 1.8 days

(parameters 85.2% of variability)

Temperature -0.34 degrees

(parameters 22.5% of variability)

0.0

0.2

0.4

0.6

0.8

1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of annual cycle

Proportion of annual cycle

Temperature (degrees C)

PC 3 (1.9% of variability)

PC 4 (0.5% of variability)

-20 -10 0 10 20

Temperature (degrees C)

-20 -10 0 10 20

Shift 4.6 days

Temperature 0.14 degrees

Shift 1.5 days

(parameters 73.6% of variability)

Temperature -0.1 degrees

(parameters 8.4% of variability)

0.0

0.2

0.4

0.6

0.8

1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of annual cycle

Proportion of annual cycle

</figure>


Define $C _ { 1 } = \| D \widehat { \mu } \| ^ { 2 }$ and $C _ { 2 } = | T | .$ Assume that $\check { x }$ integrates to zero and
satisfies (8.6).

By arguments similar to those used previously, using the standard
square integral norm for $\check { x } ,$

$$\| x - \widehat { \mu } \| ^ { 2 } \approx \| \check { x } \| ^ { 2 } + C _ { 1 } ^ { 2 } \tau ^ { 2 } + C _ { 2 } ^ { 2 } \theta ^ { 2 } .$$

Thus an appropriate definition of the norm of the triple is given by

$$\| \left( \check { x } , \tau , \theta \right) \| ^ { 2 } = \| \check { x } \| ^ { 2 } + C _ { 1 } ^ { 2 } \tau ^ { 2 } + C _ { 2 } ^ { 2 } \theta ^ { 2 } .$$

In practice, a PCA with respect to this norm is carried out by the same
general approach as before. For each $i ,$ the function $\check { x } _ { i }$ is represented
by a vector $\check { c } _ { i }$ of its first $K$ Fourier coefficients. The vector is augmented
by the two values $C _ { 1 } \tau _ { i }$ and $C _ { 2 } \theta _ { i }$ to form the vector $z _ { i } .$ We then
carry out a standard PCA on the augmented vectors $z _ { i } .$ The resulting
principal component weight vectors are then unpacked into the parts
corresponding to $\mathrm { I } _ { \mathrm { S } } ^ { \mathrm { r } } ,$ $v _ { j }$ and $u _ { j } ,$ and the appropriate inverse transforms
applied-just dividing by $C _ { 1 }$ and $C _ { 2 }$ respectively in the case of the
shift and overall temperature effects, and applying an inverse Fourier
transform to the first $K$ components of the vector to find $\mathrm { g } _ { j } .$

Figure 8.2 shows the effect of this approach applied to the Canadian
temperature data. Notice that a component that was entirely variation

<!-- PageBreak -->

<!-- PageNumber="136" -->
<!-- PageHeader="8. Principal components analysis of mixed data" -->

in overall temperature would have a temperature effect of ±1 degree,
because time is scaled to make the cycle of unit length (with time
measured in years) so that $C _ { 2 } = 1 .$ Because each principal component
is scaled to have unit norm, the maximum possible value of $\left( C _ { 2 } u _ { i } \right) ^ { 2 }$ is
1, with equality if and only if the other components are zero. Similarly,
since $C _ { 1 } = 3 6 5 / 5 . 4 ,$ a component that was entirely a time shift would
have $v _ { i } = \pm 5 . 4 / 3 6 5$ years, i.e. ±5.4 days.

In each case in the figure, the proportions of variability due to the two
parametric effects, shift and overall average temperature, are combined
to give the percentage of variability due to the vector parameters.
Principal component 1 is almost entirely due to the variation in overall
temperature, with a small effect corresponding to a decrease in range
between summer and winter. (Recall that the dotted curve corresponds
to a positive multiple of the principal component curve $\xi _ { i } ,$ and the
dashed curve to a negative multiple.) Principal component 2 has some
shift component, a moderate negative temperature effect, and mainly
comprises the effect of a decreased annual temperature range. Within
this component, overall average temperature is positively associated
with increased range, whereas in component 1 the association was
negative. Principal component 1 accounts for a much larger proportion
of the variability in the original data, and a slightly different approach
in Section 8.5 shows that within the data as a whole, increased
overall temperature is negatively correlated with higher range between
summer and winter-colder places have more extreme temperatures.

Neither principal components 3 nor 4 contains much of an effect due
to overall temperature. As before, component 3 is very largely shift,
whereas component 4 corresponds to an effect unconnected to shift or
overall temperature.


### 8.5 Separating out the vector component

This section demonstrates the other procedure suggested in Section
8.2. We carry out a principal components analysis on the registered
curves $\check { x } _ { i }$ and then investigate the relationship between the resulting
principal component scores and the parameters $\tau _ { i }$ and $\theta _ { i }$ arising in
the registration process. Thus we analyse only the functional part of
the mixed data, and the vector part is only considered later.

The effect of doing this is demonstrated in Figure 8.3. Removing the
temperature and shift effects accounts for 79.2% of the variability in
the original data, and the percentages of variability explained by the
various principal components have been multiplied by 0.208, to make

<!-- PageBreak -->

<!-- PageNumber="137" -->
<!-- PageHeader="8.5 Separating out the vector component" -->


<figure>
<figcaption>FIGURE 8.3. Principal component analysis carried out on the Canadian temperature curves adjusted for time shift and for annual average temperature.</figcaption>

Temperature (degrees C)

PC 1 (19.2% of original variability)

PC 2 (1.1% of original variability)

10 20

Temperature (degrees C)

-20 -10 0 10 20

O

-10

Correlation with shift -0.31

-20

Correlation with temperature -0.76

Correlation with shift -0.55

Correlation with temperature 0.44

0.0

0.2

0.4

0.6

0.8

1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of annual cycle

Proportion of annual cycle

Temperature (degrees C)

PC 3 (0.3% of original variability)

PC 4 (0.1% of original variability)

10 20

Temperature (degrees C)

10 20

O

0

-10

Correlation with shift -0.49

-10

Correlation with temperature -0.19

Correlation with shift 0.01

-20

-20

Correlation with temperature 0.04

0.0

0.2

0.4

0.6

0.8

1.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of annual cycle

Proportion of annual cycle

</figure>


them express parts of the variability of the original data, rather than
the adjusted data. For each weather station, we have a shift and annual
average temperature as well as the principal component scores. Figure
8.3 shows the correlations between the score on the relevant principal
component and the two parameters estimated in the registration.

We see that the components 3 and 4 in this analysis account for
very little of the original variability and have no clear interpretation.
Component 1 corresponds to an increase in range between winter
and summer-the effect highlighted by component 2 in the previous
analysis. We see that this effect is strongly negatively correlated with
annual average temperature, and mildly negatively correlated with
shift. Component 2 corresponds approximately to component 4 in the
previous analysis, and is the effect whereby the length of summer is
lengthened relative to that of winter. This effect is positively correlated
with average temperature and negatively correlated with shift.

<!-- PageBreak -->


## 9 Functional linear models


### 9.1 Introduction

So far in this book, we have concentrated on analysing the variability
of a single functional variable, albeit one that may have a rather
complicated structure. In classical statistics, techniques such as linear
regression, the analysis of variance, and the general linear model all
approach the question of how variation in an observed variable may
be accounted for by other observed quantities. We now extend these
general ideas to the functional context.

Linear models can be functional in terms either of the dependent
variable, or of the linear mapping classically described by the design
matrix, or both. In all cases, the regression coefficients or parameters
are functions rather than just numbers. In this chapter, we introduce
some of the ideas of functional linear modelling by extending the
general linear model in one particular way, where only the parameters
and the dependent variable become functional, but the design matrix
remains as in the classical general linear model. We review further
extensions in Section 9.5 and in subsequent chapters.

<!-- PageBreak -->

<!-- PageNumber="140" -->
<!-- PageHeader="9. Functional linear models" -->


### 9.2 Functional linear models and functional analysis of variance

Consider the Canadian weather data introduced in Chapter 1. Monthly
means for temperature and precipitation are available for each of 35
weather stations distributed across the country, and we can use the
smoothing techniques of Chapter 3 to represent each 12-month record
as a smooth function. Thus, two periodic functions, Temp and Prec,
denoting temperature and the logarithm of precipitation, respectively,
are available for each station.

In this chapter we ask how much of the pattern of annual variation of
temperature is attributable to geographical area. Dividing Canada into
Atlantic, Continental, Pacific and Arctic meteorological zones, we want
to study the characteristic types of temperature patterns in each zone.
This is basically an analysis of variance problem with four treatment
groups. Multivariate analysis of variance (MANOVA) is the extension
of the ideas of analysis of variance to deal with problems where the
dependent variable is multivariate. Because our dependent variable
is the functional observation Temp, the methodology we need is a
functional analysis of variance, abbreviated FANOVA.

In formal terms, we have a number of stations in each group $g ,$ and
the model for the kth temperature function in the gth group, indicated
by $\mathrm { T e m p } _ { k g } ,$ is

$$\mathrm { T e m p } _ { k g } \left( t \right) = \mu \left( t \right) + \alpha _ { g } \left( t \right) + \epsilon _ { k g } \left( t \right) .$$
(9.1)

The function $\mu$ is the grand mean function, and therefore indicates the
average temperature profile across all of Canada. The terms $\alpha _ { g }$ are the
specific effects on temperature of being in climate zone $g .$ To be able
to identify them uniquely, we require that they satisfy the constraint

$$\sum _ { g } \alpha _ { g } \left( t \right) = 0 \text { for all } t .$$
(9.2)

The residual function $\epsilon _ { k g }$ is the unexplained variation specific to the
$k t h$ weather station within climate group $g .$

We can define $3 5 \times 5$ design matrix $Z$ for this model, with one row
for each individual weather station, as follows. Use the label $\left( k , g \right)$ for
the row corresponding to station $k$ in group $g ;$ this row has a one in
the first column, a one in column $g + 1 ,$ and zeroes in the rest. Write
$Z \left( k , g \right)$ for the 5-vector whose transpose is the $\left( k , g \right)$ row of Z.

We can then define $a$ corresponding set of five regression functions $\beta _ { j }$
by setting $\beta _ { 1 } = \mu ,$ $\beta _ { 2 } = \alpha _ { 1 } ,$ and so on to $\beta _ { 5 } = \alpha _ { 4 } ,$ so that the functional
vector $\beta = \left( \mu , \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 } \right) ^ { \prime } .$ In these terms, the model (9.1) has the

<!-- PageBreak -->

<!-- PageNumber="141" -->
<!-- PageHeader="9.2 Functional linear models and functional ANOVA" -->

equivalent formulation

$$\mathrm { T e m p } _ { k g } \left( t \right) = \sum _ { j = 1 } ^ { 5 } z _ { \left( k , g \right) j } \beta _ { j } \left( t \right) + \epsilon _ { k g } \left( t \right) = \langle z _ { \left( k , g \right) } , \beta \left( t \right) \rangle + \epsilon _ { k g } \left( t \right) \quad \left( 9 . 3 \right)$$

or, more compactly in matrix notation,

$$= Z \beta + \epsilon ,$$
(9.4)

where Temp is the vector containing the 35 temperature functions, $\epsilon$
is a vector of 35 residual functions, and $\beta$ is the 5-vector of parameter
functions. The design matrix $\mathrm { Z }$ has exactly the same structure as for the
corresponding univariate or multivariate one-way analysis of variance.
The only way in which (9.4) differs from the corresponding equations
in standard elementary textbooks on the general linear model is that
the parameter $\beta ,$ and hence the predicted observations $\mathrm { z } \beta ,$ are vectors
of functions rather than vectors of numbers.


#### 9.2.1 Fitting the model

If (9.4) were a standard general linear model, the standard least squares
criterion would say that $\beta$ should be chosen to minimize the residual
sum of squares, which can be written $- Z \beta | | ^ { 2 }$ in vector notation.
To extend the least squares principle to the functional case, we need
only reinterpret the squared norm in an appropriate way. The quantity
Temp $- Z \beta$ is now a vector of functions. The individual components
of $\mathrm { Z } \beta$ are the individual predictors $\langle z _ { \left( k , g \right) } , \beta \rangle ,$ and so the natural least
squares fitting criterion becomes

$$L M S S E \left( \beta \right) = \sum _ { g } \sum _ { k } \int \left[ T e m p _ { k g } \left( t \right) - \langle z _ { \left( k , g \right) } , \beta \left( t \right) \rangle \right] ^ { 2 } d t .$$
(9.5)

Minimizing $\mathrm { L M S S E } \left( \beta \right)$ subject to the constraint $\sum _ { 2 } ^ { 5 } \beta _ { j } = 0$ (equivalent
to $\left. \sum _ { 1 } ^ { 4 } \alpha _ { g } = 0 \right)$ gives the least squares estimates $\widehat { \beta }$ of the functional
parameters $\mu$ and $\alpha _ { g } .$ Section 9.4 contains some remarks about the
way LMSSE is minimized in practice.

Figure 9.1 displays the resulting estimated region effects $\alpha _ { g }$ for
the four climatic zones, and Figure 9.2 displays the composite effects
$\mu + \alpha _ { g } .$ We see that the region effects are more complex than the
constant or even sinusoidal effects that one might expect:

· The Atlantic stations appear to have a temperature around 5
degrees $C$ warmer than the Canadian average.

<!-- PageBreak -->

<!-- PageNumber="142" -->
<!-- PageHeader="9. Functional linear models" -->


<figure>
<figcaption>FIGURE 9.1. The region effects $\alpha _ { j }$ for the temperature functions in the functional analysis of variance model $\mathrm { T e m p } _ { i j } \left( t \right) = \mu \left( t \right) + \alpha _ { j } \left( t \right) + \epsilon _ { i j } \left( t \right) .$ Note that the effects are required to sum to 0 for all t.</figcaption>

Atlantic

Pacific

-20 -10 0 10

10

0

20 -10

0 2 4 6 8 10 12

0

2

4

6

8

10

12

Continental

Arctic

10

2

0

0

-10

-10

20

-20

0

2

4

6

8

10

12

0

2

4 6 8 10

12

</figure>


· The Pacific weather stations have a summer temperature close to
the Canadian average, but are much warmer in the winter.

· The Continental stations are slightly warmer than average in the
summer, but are colder in the winter by about 5 degrees $\mathrm { C } .$

· The Arctic stations are certainly colder than average, but even
more so in March than in January.


#### 9.2.2 Assessing the $f i t$

In estimating and plotting the individual regional temperature
effects, we have taken our first step towards achieving the goal of
characterizing the typical temperature pattern for weather stations in
each climate zone. We may wish to move on and not only confirm
that the total zone-specific effect $\alpha _ { g }$ is nonzero, but also investigate
whether this effect is substantial at a specific time $t .$ As in ordinary
analysis of variance, we look to summarize these issues in terms of
error sum of squares functions LMSSE, squared correlation functions
RSQ, and F-ratio functions FRATIO. It is the dependence of these
quantities on $t$ that makes the procedure different from the standard
multivariate case.

<!-- PageBreak -->

<!-- PageNumber="143" -->
<!-- PageHeader="9.2 Functional linear models and functional ANOVA" -->


<figure>
<figcaption>FIGURE 9.2. The estimated region temperature profiles $\mu + \alpha _ { j }$ for the temperature functions in the functional analysis of variance model (solid curves). The dashed curve is the Canadian mean function $\mu .$</figcaption>

Atlantic

Pacific

-30 -20 -10 0 10 20

-30 -20 -10 0 10 20

0

2

4

6

8

10

12

0

2

4

6

8

10

12

Continental

Arctic

-30 -20 -10 0 10 20

-30 -20 -10 0 10 20

0

2

4

6

8

10

12

0

2

4

6

8

10

12

</figure>


As in the multivariate linear model, the primary source of
information in investigating the importance of the zone effects $\alpha _ { g }$ is
the sum of squares function

$$S S E \left( t \right) = \sum _ { k , g } \left[ T e m p _ { k g } \left( t \right) - \left( Z \widehat { \beta } \right) _ { k g } \left( t \right) \right] ^ { 2 } .$$
(9.6)

This function can be compared to the error sum of squares function
based on using only the Canadian average $\widehat { \mu }$ as a model,

$$S S Y \left( t \right) = \sum _ { k g } \left[ T e m p _ { k g } \left( t \right) - \widehat { \mu } \left( t \right) \right] ^ { 2 }$$

and one way to make this comparison is by using the squared multiple
correlation function RSQ with values

$$R S Q \left( t \right) = \left[ S S Y \left( t \right) - \quad S S E \left( t \right) \right] / S S Y \left( t \right) .$$
(9.7)

Essentially, this function considers the drop in error sum of squares
produced by taking climate zone into effect relative to error sum of
squares without using climate zone information.

We can also compute the functional analogues of the quantities
entered into the ANOVA table for a univariate analysis. For example,

<!-- PageBreak -->

<!-- PageNumber="144" -->
<!-- PageHeader="9. Functional linear models" -->

the mean square for error function MSE has values

$$M S E = S S E / d f \left( e r r o r \right)$$

where df(error) is the degrees of freedom for error, or the sample size
$N$ less the number of mathematically independent functions $\beta _ { a }$ in the
model. In this problem, the zero sum restriction on the climate zone
effects $\alpha _ { g }$ implies that there are four degrees of freedom lost to the
model, or $d f \left( e r r o r \right) = 3 1 .$ Similarly, the mean square for regression
is the difference between SSY (or, more generally, whatever reference
model we employ that is a specialization of the model being assessed)
and SSE, divided by the difference between the degrees of freedom for
error for the two models. In this particular application, the reference
model uses one degree of freedom, so

$$M S R \left( t \right) = \frac { \mathrm { S S Y } \left( t \right) - \mathrm { S S E } \left( t \right) } { \mathrm { d f } \left( m o d e l \right) }$$

where $d f \left( m o d e l \right) = 3 .$ Finally, we can compute the $F$ F-ratio function,

$$= \frac { M S R } { M S E }$$
(9.8)

Figure 9.3 shows the two functions RSQ and FRATIO. We can see that
the squared correlation is relatively high and that the F-ratio is very
substantially above the 5% significance level of 2.92. It is interesting to
note that the differences between the climate zones are substantially
stronger in the spring and autumn, rather than in the summer and
winter as we might expect.

Basically, then, most of the statistical machinery available for
univariate analysis of variance is readily applicable to this functional
problem. We can consider, for example, contrast functions, post-hoc
multiple comparison functions, F-ratios associated with constrained
estimates of region effects, and so on, essentially because the
functional analysis of variance problem is really a univariate ANOVA
problem for each specific value of $t .$

One question not addressed in the discussion of this example is
an overall assessment of significance for the difference between the
climate zones, rather than an assessment for each individual time $t .$
Section 9.3.3 provides an approach to this question using simulation
in the context of a different example.

An application of functional analysis of variance can be found in
Ramsay, Munhall, Gracco and Ostry (1996), where variation in lip
movement during the production of four syllables is analysed at the
level of both position and acceleration. In the next section, we look at
another application with a rich structure.

<!-- PageBreak -->

<!-- PageNumber="145" -->
<!-- PageHeader="9.3 Force plate data for walking horses" -->


<figure>
<figcaption>FIGURE 9.3. The left panel contains the squared multiple correlation function RSQ and the right panel the corresponding F-ratio function FRATIO. The horizontal dotted line indicates the 5% significance level for the $F$ F-distribution with 3 and 31 degrees of freedom.</figcaption>

Squared Mult. Corr.

F-ratio

0.0 0.2 0.4 0.6 0.8 1.0

40

30

20

10

0

0

2

4 6 8 10

12

0

2

4

6

8

10

12

Month

Month

</figure>


### 9.3 Force plate data for walking horses

This section describes some interesting data on equine gait. The data
were collected by Dr. Alan Wilson of the Equine Sports Medicine Centre,
Bristol University, and his collaborators. Their kindness in allowing use
of the data is gratefully acknowledged. The data provide an opportunity
to discuss various extensions of our functional linear modelling and
analysis of variance methodology. For further details of this example,
see Wilson et al. (1996).


#### 9.3.1 Structure of the data

The basic structure of the data is as follows. It is of interest to study
the effects of various types of shoes, and various walking surfaces, on
the gait of a horse. One reason for this is simply biomechanical: The
horse is an animal particularly well adapted to walking and running,
and the study of its gait is of intrinsic scientific interest. Secondly, it is
dangerous to allow horses to race if they are lame or likely to go lame.
Careful study of their gait may produce diagnostic tests of incipient
lameness which do not involve any invasive investigations and may
detect injuries at a very early stage, before they become serious or
permanent. Thirdly, it is important to shoe horses to balance their gait,
and understanding the effects of different kinds of shoe is necessary
to do this. Indeed, once the normal gait of a horse is known, the

<!-- PageBreak -->

<!-- PageNumber="146" -->
<!-- PageHeader="9. Functional linear models" -->

measurements we describe can be used to test whether a blacksmith
has shod a horse correctly, and can therefore be used as an aid in the
training of farriers.

In this experiment, horses walk on to a plate about 1 metre square
set into the ground and equipped with meters at each corner measuring
the force in the vertical and the two horizontal directions. We consider
only the vertical force. During the period that the horse's hoof is on the
ground (the stance phase) the four measured vertical forces allow the
instrument to measure the point of resultant vertical force. The hoof
itself does not move during the stance phase, and the position of the
hoof is measured by dusting the plate with sawdust or is inferred from
the point of force at the end of the stride, when only the front tip of
the hoof is in contact with the ground.

The vertical force increases very rapidly at the beginning of the stance
phase but reduces more slowly at the end. Operationally, the stance
phase is defined as starting at the moment where the total vertical
force first reaches 30% of its maximum value and ending where it falls
to 8% of its maximum value. For each replication, the point of force is
computed for 100 time points equally spaced in this time interval.

$A$ typical functional observation is therefore a two-dimensional
function of time Force = (ForceX, ForceY) where $t$ varies from 0
to 1 during the stance phase, and ForceX(t) and $\mathrm { F o r c e Y } \left( t \right)$ are the
coordinates of the point of force at time $t .$ Here $Y$ is the direction
of motion of the horse, and $X$ measures distance in $a$ perpendicular
direction towards the body of the horse. Thus the coordinates are
defined as $\mathrm { i f }$ looking at the plate from above if a left foot is being
measured, but with the $X$ direction reflected if a right foot is being
measured.

The data set consists of 592 separate runs and involves 8 horses,
each of which has a number of measurements on both its right and left
forelimbs. The nine shoeing conditions are as follows: first, the horse
is observed unshod; it is then shod and observed again; then its shoe
is modified by the addition of various wedges, either building up its
toe or heel or building up one side or the other of its hoof. Not every
horse has every wedge applied. In the case of the toe and heel wedges,
the horse is observed immediately after the wedge is fitted and one day
later, after it has become accustomed to the shoe. Finally the wedges
are removed and the horse is observed with a normal shoe.

Figure 9.4 shows a typical (ForceX, ForceY) plot. This realization
is among the smoother curves obtained. The 100 points that are
equally spaced in time are marked on the curve, and the direction
of time is indicated by arrows (also evenly spaced in time). We can

<!-- PageBreak -->

<!-- PageNumber="147" -->
<!-- PageHeader="9.3 Force plate data for walking horses" -->


<figure>
<figcaption>FIGURE 9.4. A typical trace of the resultant point of force during the stance phase of a horse walking onto a force plate. One hundred points equally spaced in time are indicated on the curve. The arrows indicate the direction of time.</figcaption>

80

70

ForceY(t) (mm)

60

50

40

30

20

-35

-30

-25

-20

-15

ForceX(t) (mm)

</figure>


see, not surprisingly, that the point of force moves most rapidly near
the beginning and end of the stance phase. The accuracy of a point
measurement was about 1 mm in each direction.


#### 9.3.2 A functional linear model for the horse data

The aim of this experiment is to investigate the effects of various
shoeing conditions, and particularly to study the effects of the toe and
heel wedges, which change as the horse becomes accustomed to the
wedge. We fit a model of the form

$$= \mu + \alpha _ { i j } + \theta _ { k } + \epsilon _ { i j }$$
(9.9)

where all the terms are two-dimensional functions of $t ,$ $0 \leq t \leq 1$ 1. The
suffix $i j k l$ refers to the data collected for the $l$ Ith observed curve for
side $j$ of horse $i$ under condition $k .$

For any particular curve, use labels $x$ and $y$ where necessary to
denote the $x$ and $\mathcal{Y}$ coordinates of the vector function. The following
identifiability constraints are placed on the various effects, each valid
for all $t$ t:

$$\sum _ { i , j } \alpha _ { i j } \left( t \right) = \sum _ { k = 1 } ^ { 9 } \theta _ { k } \left( t \right) = 0 .$$
(9.10)

<!-- PageBreak -->

<!-- PageNumber="148" -->
<!-- PageHeader="9. Functional linear models" -->


<figure>
<figcaption>FIGURE 9.5. Estimate of the overall mean curve $\left( \mu _ { x } , \mu _ { y } \right)$ obtained from the 592 observed point of force curves using model (9.9).</figcaption>

40

30

ForceY(t) (mm)

20

10

0

-5

0

5

10

ForceX(t) (mm)

</figure>


We estimate the various effects by carrying out a separate general
linear model fit for each $t$ and for each of the $x$ and $y$ coordinates.
Since the data are observed at 100 discrete times in practice, each
$\mathrm { F o r c e } _ { i i l k l }$ corresponds to two vectors, each of length 100, one for the $x$
coordinates and one for the $y$ coordinates. The design matrix relating
the expected value of $\mathrm { F o r c e } _ { i j k l }$ to the various effects is the same for all
200 observed values, so although the procedure involves the fitting of
200 separate models, considerable economy of effort is possible. The
model (9.9) can be written as

$$= Z \beta + \epsilon$$
(9.11)

where Force and $\epsilon$ are both vectors of length 592, each of whose
elements is a two-dimensional function on $\left[ 0 , 1 \right] .$ The vector $\beta$ is $a$
vector of the 26 two-dimensional functions $\mu ,$ $\alpha _ { i j }$ and $\theta _ { k } ,$ and $Z$ is a
$5 9 2 \times 2 6$ design matrix relating the observations Force to the effects
$\beta .$ The identifiability constraints (9.10) are incorporated by augmenting
the matrix $\mathrm { Z }$ by additional rows corresponding to the constraints, and
by augmenting the data vector Force by zeroes. Standard theory of the
general linear model of course then gives as the estimator

$$\widehat { \beta } = \left( Z ^ { \prime } Z \right) ^ { - 1 } Z ^ { \prime } F o r c e .$$
(9.12)

<!-- PageBreak -->

<!-- PageNumber="149" -->
<!-- PageHeader="9.3 Force plate data for walking horses" -->


<figure>
<figcaption>FIGURE 9.6. The estimated residual variance in the $x$ coordinate (solid curve) and the $\mathcal{Y}$ coordinate (dotted curve) as the stance phase progresses.</figcaption>

120

Estimated residual variance

100

80

60

40

20

0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of stance time

</figure>


Figure 9.5 plots the estimated overall mean curve $\mu = \left( \mu _ { x } , \mu _ { y } \right)$
in the same way as Figure 9.4. Although the individual observations
are somewhat irregular, the overall mean is smooth, even though no
smoothing is incorporated into the procedure.

The general linear model fitted for each coordinate at each time
point allows the calculation of a residual sum of squares, and hence
an estimated residual variance, at each point. The residual variance
curves $\mathrm { M S E } _ { x }$ and $\mathrm { M S E } _ { \mathcal{Y} }$ for the $x$ and $y$ coordinates are plotted in
Figure 9.6. It is very interesting to note that the residual variances in the
two coordinates are approximately the same size, and vary in roughly
the same way, as the stance phase progresses.


#### 9.3.3 Effects and contrasts

We can now explain how the linear model can be used to investigate
various effects of interest. We concentrate on two specific effects,
corresponding to the application of the toe wedges, and illustrate how
various inferences can be drawn. In Figure 9.7, we plot the effects of
the toe wedge immediately after it has been applied and the following
day. The $x$ and $y$ coordinates of the relevant functions $\theta _ { k }$ are plotted
separately. It is interesting to note that the $\mathcal{Y}$ effects are virtually the
same in both cases: The application of the wedge has an immediate

<!-- PageBreak -->

<!-- PageNumber="150" -->
<!-- PageHeader="9. Functional linear models" -->


<figure>
<figcaption>FIGURE 9.7. The effects of the application of a toe wedge, $x$ coordinate in the lower panel and $y$ coordinate in the lower. Solid curves are the immediate effect, and dashed curves are the effect on the following day.</figcaption>

x effect (mm)

-2 0 2 4 6 8

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of stance phase

y effect (mm)

-2 0 2 4 6 8 10

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of stance phase

</figure>


effect on the way in which the point of force moves in the forward-
backward direction, and this pattern does not change appreciably as the
horse becomes accustomed to the wedge. The effect in the side-to-side
direction is rather different. Immediately after the wedge is applied,
the horse tends to put its weight to one side, but the following day
the effect becomes much smaller, and the weight is again placed in the
same lateral position as in the average stride.

To investigate the significance of this change, we now consider the
contrast between the two effects, which shows the expected difference
between the point of force function for a horse 24 hours after a toe
wedge has been applied and that immediately after applying the wedge.
Figure 9.8 shows the $x$ and $y$ coordinates of the difference of these
two effects. The standard error of this contrast is easily calculated.
Let $u$ be the vector such that the estimated contrast is the vector
function $\mathrm { C o n t r a s t } = u ^ { \prime } \widehat { \beta } ,$ so that the component of $u$ corresponding
to toe wedge 24 hours after application is $+ 1 ,$ that corresponding
to toe wedge immediately after application is -1, and all the other
components are zero. Define $a$ by $a ^ { 2 } = u ^ { \prime } \left( Z ^ { \prime } Z \right) ^ { - 1 } u .$ The squared
pointwise standard errors of the $x$ and $\mathcal{Y}$ coordinates of the estimated
contrasts are then $a ^ { 2 } M S E _ { x }$ and $a ^ { 2 } M S E _ { y } ,$ respectively. Plots of $2$ times
the relevant standard error are included in Figure 9.8. Because the

<!-- PageBreak -->

<!-- PageNumber="151" -->
<!-- PageHeader="9.3 Force plate data for walking horses" -->


<figure>
<figcaption>FIGURE 9.8. Solid curves are the differences between the effect of a toe wedge after 24 hours and its immediate effect. Dotted curves indicate plus and minus two estimated standard errors for the pointwise difference between the effects. The upper panel contains $x$ coordinates and the lower the $y$ coordinates.</figcaption>

x effect (mm)

-6 -4 -2 0 2 4

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of stance phase

y effect (mm)

-4 -2 0 2 4

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of stance phase

</figure>


degrees of freedom $\left( 5 9 2 - 2 6 + 2 \right)$ for residual variance are so large, these
plots indicate that pointwise $t$ tests at the 5% level would demonstrate
that the difference in the $\mathcal{Y}$ coordinate of the two toe wedge effects
is not significant, except possibly just above time 0.8, but that the $x$
coordinate is significantly different from zero for almost the whole
stance phase.

How should we account for the correlation in the tests at different
times in assessing the significance of any difference between the two
conditions? We can consider the summary statistics

$$M _ { x } = \sup _ { t } | \mathrm { C o n t r a s t } _ { x } \left( t \right) / a \sqrt { \mathrm { M S E } _ { x } \left( t \right) } |$$

and

$$M _ { y } = \sup _ { t } | \mathrm { C o n t r a s t } _ { y } \left( t \right) / a \sqrt { \mathrm { M S E } _ { y } \left( t \right) } | .$$

The values of these statistics for the data are $M _ { x } = 5 . 0 3$ and $M _ { y } = 2 . 0 1 .$
A permutation-based significance value for each of these statistics was
obtained by randomly permuting the observed toe wedge data for each
leg of each horse between the conditions immediately after fitting of
wedge and 24 hours after fitting of wedge, keeping the totals the same

<!-- PageBreak -->

<!-- PageNumber="152" -->
<!-- PageHeader="9. Functional linear models" -->

within each condition for each leg of each horse. The statistics $M _ { x }$ and
$M _ { y }$ were calculated for each random permutation of the data. In 1000
realizations, the largest value of $M _ { x }$ observed was 3.57, so the observed
difference in the $x$ direction of the two conditions is highly significant.
A total of 177 of the 1000 simulated $M _ { y }$ values exceeded the observed
value of 2.01, and so the estimated $p$ p-value of this observation was
0.177, showing no evidence that the $y$ coordinate of point of force
alters its time behaviour as the horse becomes accustomed to the
wedge.


### 9.4 Computational issues


#### 9.4.1 The general model

In this section, we set out methods for computing the least squares
estimates in the functional linear model. To be specific, we assume
that $Y$ is an N-vector of observations, with each element of some
appropriate functional form. The $q$ q-vector $\beta$ of parameters has
elements with the same functional form as the elements of $Y ;$ thus,
in the force-plate data example, the individual elements of both $Y$ and
$\beta$ were themselves two-dimensional functions. We assume that $\mathrm { Z }$ is an
$N \times q$ design matrix, and that the expected value of $Y \left( t \right)$ for each $t$ is
modelled as $\mathrm { Z } \beta \left( t \right) .$

Any linear constraints on the parameters $\beta ,$ such as the requirement
in the temperature data example that the individual climate zone
effects sum to zero, are expressed as $L \beta = 0$ for some suitable matrix
L with q columns. By using a technique such as the QR-decomposition,
described in Section A.1.3 of the Appendix, we may also say that

$$\beta = C \alpha$$
(9.13)

for some matrix $\mathrm { C } .$

Our aim is to minimize the least squares fitting criterion

$$L M S S E \left( \beta \right) = \int \| Y \left( t \right) - Z \beta \left( t \right) \| ^ { 2 } d t$$
(9.14)

subject to the constraint $L \beta \left( t \right) = 0$ for all $t .$ The norm in the
definition of LMSSE is an appropriate Euclidean vector norm. Assume
that the constraints assure the identifiability of the parameters. In
linear algebraic terms, this means that the rows of $Z$ are linearly
independent of the rows of $\mathrm { L } ,$ and that the augmented design matrix
constructed by putting the rows of $Z$ together with those of $\mathrm { L }$ is of full
column rank $q .$

<!-- PageBreak -->

<!-- PageNumber="153" -->
<!-- PageHeader="9.4 Computational issues" -->


#### 9.4.2 Pointwise minimization

Since there are no particular restrictions on the way in which $\beta \left( t \right)$
varies as a function of $t ,$ we can minimize $\mathrm { L M S S E } \left( \beta \right)$ by minimizing
$\| Y \left( t \right) - Z \beta \left( t \right) \| ^ { 2 }$ individually for each $t .$ Because the rows of $Z$ and
those of $\mathrm { L }$ are independent, we can compute the constrained minimum
of $\mathrm { L M S S E } \left( \beta \right)$ by finding the unconstrained minimum of the regularized
residual sum of squares

$$\| Y \left( t \right) - Z \beta \left( t \right) \| ^ { 2 } + \lambda \| L \beta \left( t \right) \| ^ { 2 }$$

for any convenient $\lambda > 0 .$ We can find $\widehat { \beta }$ by solving the equation

$$\left( Z ^ { \prime } Z + \lambda L ^ { \prime } L \right) \widehat { \beta } \left( t \right) = Z ^ { \prime } Y \left( t \right) .$$
(9.15)

The solution for $\widehat { \beta }$ does not depend on the actual value assigned to
$\lambda ,$ since for any positive value the incorporation of the penalty term
simply imposes the constraint $L \beta \left( t \right) = 0$ and does not affect the fit. The
value $\lambda = 1$ usually works, but can be varied if numerical instabilities
are encountered.

The most straightforward method of finding the function $\widehat { \beta }$ is to
find $\widehat { \beta } \left( t \right)$ from (9.15) for a suitable grid of values of $t ,$ and then
interpolate between these values. This was the technique used in both
the temperature and force plate examples, where the grid of values
was chosen to correspond with the discretization of the original data.
In the case of the temperature data, only 12 values of $t$ were used,
whereas a finer grid of 100 values was appropriate for the force plate
data. In either case, the fact that the same system of equations is solved
repeatedly in (9.15) makes for considerable economy of numerical
effort.


#### 9.4.3 Functional linear modelling with basis expansions

It is often more appropriate to store the observed functions and
parameters in basis expansion form, for example in terms of Fourier
series or $B$ B-splines. For example, it may be that the functions are well
approximated by a relatively short basis expansion. Another possibility
is that the different functions may have been observed at different sets
of times, and that a common basis expansion method has been used to
construct the functional observations.

Suppose that our basis is a K-vector $\phi$ of linearly independent
functions, and that the matrix $\mathrm { Y }$ gives the coefficients of the observed
vector $Y$ of functions, so that $Y = Y \phi .$ Thus, the $\left( j , k \right)$ element of the
matrix $\mathrm { Y }$ is the coefficient of $\phi _ { k }$ in the expansion of $Y _ { j } .$ Expand the

<!-- PageBreak -->

<!-- PageNumber="154" -->
<!-- PageHeader="9. Functional linear models" -->

estimated parameter vector $\widehat { \beta }$ in terms of the same basis, expressing
$\widehat { \beta } = \mathrm { B } \phi$ for a $q \times K$ matrix $B .$ We can now substitute into (9.16) to see
that $B$ satisfies the matrix system of linear equations

$$\left( Z ^ { \prime } Z + \lambda L ^ { \prime } L \right) B = Z ^ { \prime } Y .$$
(9.16)

This provides a simple alternative to the discretization strategy
described in Section 9.4.2.


#### 9.4.4 Incorporating regularization

So far, we have merely fitted the functional linear model without
imposing any regularity on the estimated parameter functions $\beta .$ This
normally suffices for problems where the observed functions $Y$ are
reasonably smooth. Indeed, the averaging implicit in the estimation
of $\beta$ from most models often leads to parameter functions that are
smoother than the original observed $Y .$

However, there may be cases where the observed functions are
so rough or rapidly varying that we wish to incorporate some
regularization into the fitting of the functional linear model, over and
above constraints imposed on the parameters. We comment very briefly
on two possible approaches to this issue.

One simple method is to use basis expansions with a relatively small
number of basis functions; this smooths the original observations
by projecting them onto the space spanned by the restricted basis
and hence automatically yields smoother estimates of the parameter
functions $\beta .$

Another possibility is to introduce a roughness penalty into the
measure of goodness of fit LMSSE. Thus, for example, we would define
$P E N _ { 2 } \left( \beta \right)$ to be $\sum _ { j } P E N _ { 2 } \left( \beta _ { j } \right) = \sum _ { j } \int \left( D ^ { 2 } \beta _ { j } \right) ^ { 2 } .$ Letting $\lambda \geq 0$ be a smoothing
parameter, we then define

$$\mathrm { L M S S E } _ { \lambda } \left( \beta \right) = \mathrm { L M S S E } \left( \beta \right) + \lambda \times \mathrm { P E N } _ { 2 } \left( \beta \right) .$$

Minimizing LMSSE subject to the constraint $L \beta = 0$ then give
regularized estimates of the parameters $\beta .$

Computationally, it is probably most straightforward to implement
this regularization procedure by using a basis expansion. Given a basis
$\phi ,$ define $\mathbb{R}$ to be the matrix $\int \left( D ^ { 2 } \phi \right) \left( D ^ { 2 } \phi \right) ^ { \prime }$ and let $\mathrm { J }$ be the matrix of
inner products $\langle \phi , \phi ^ { \prime } \rangle .$ As in Section 9.4.3, write $\beta = B \phi$ and $Y = Y \phi$
for suitable matrices of coefficients $\mathrm { Y }$ and $B .$ Then

$$\mathrm { L M S S E } _ { \lambda } \left( \beta \right) = \mathrm { t r a c e } \left( \mathrm { Y } - \mathrm { Z B } \right) \mathrm { J } \left( \mathrm { Y } - \mathrm { Z B } \right) ^ { \prime } + \lambda \mathrm { t r a c e } \mathrm { B R B } ^ { \prime } .$$
(9.17)

<!-- PageBreak -->

<!-- PageNumber="155" -->
<!-- PageHeader="9.5 General structure" -->

If $\beta$ is unconstrained, then $B$ satisfies the equation

$$\left( Z ^ { \prime } J Z + \lambda R \right) B = Z ^ { \prime } J Y .$$

Or, if $\beta$ is constrained, then from (9.13) $B = C A$ for some unknown
matrix $A ,$ and substituting this relationship in (9.17) yields

$$\left( C ^ { \prime } Z ^ { \prime } J Z C + \lambda C ^ { \prime } R C \right) A = C ^ { \prime } Z ^ { \prime } J Y .$$


### 9.5 General structure

We close this chapter by briefly discussing some other possible
functional linear modelling problems. The equation (9.4) developed in
this chapter looks exactly the same as the standard multivariate general
linear model. $A$ vector of parameters $\beta$ is mapped by a matrix $\mathrm { Z }$ into
a vector of predictors of the observations. In the examples we have
discussed, the key difference is that the parameters and the individual
observations are functions rather than just numbers.

We can step back and ask what is the general structure of these
problems. The matrix $Z$ defines a linear transformation from the
parameter space $B$ to the observation space $y ,$ such that for any $\beta$ in
$\mathbb{B} ,$ the prediction $\widehat { Y }$ of the observation $Y$ is equal to $\mathrm { Z } \beta .$ In the classical
general linear model, the members of the parameter space $B$ are vectors
$\beta .$ In the functional linear model (9.3) they are vector-valued functions
$\beta ,$ as are the members $Y$ of $y ,$ but the linear transformations considered
are all of the form $Z \beta$ for matrices $Z .$

In some circumstances, it is appropriate to consider more general
linear transformations $Z$ of the parameter space into the observation
space. In every case, we regard $Z$ as the model that gives the predicted
observations in terms of the parameters. In Chapter 10, we consider
problems where the observations $\mathcal{Y} _ { i }$ are scalars rather than functions,
but the parameters $\beta _ { j }$ are functional. Our example is the prediction of
total annual log precipitation from the annual pattern of temperature.
In this case, the model $Z$ is a linear mapping from a space of vector-
valued functions $\beta$ to an ordinary space of multivariate observations
$y .$

In Chapter 11 we return to problems where both the response $\mathcal{Y}$
and the parameter $\beta$ are functional. However, rather than consider
the relatively simple situation where $B$ is mapped to $y$ by a matrix
$Z$ of numbers, we look at problems where $Z$ is a much more general
functional operator.

<!-- PageBreak -->


## 10 Functional linear models for scalar responses


### 10.1 Introduction: Functions as predictors

In this chapter, we consider a linear model defined by a set of
functions, but where the response variable is scalar or multivariate.
This contrasts with Chapter 9, where the responses and the parameters
were functional, but, because of the finite and discrete covariate
information, the linear transformation from the parameter space to
the observation space was still specified by a design matrix $Z$ as in the
conventional multivariate general linear model.

We begin by recalling some aspects of ordinary linear regression.
Suppose $\mathcal{Y} _ { 1 } , \ldots , \mathcal{Y} _ { N }$ are observations of a response variable at values
$x _ { 1 } , \ldots , x _ { N }$ of a multivariate covariate $x$ of dimension $p .$ Linear
regression, of course, then fits a model of the form

$$y _ { i } = \alpha + \sum _ { j } \beta _ { j } x _ { i j } + \epsilon _ { i } = \alpha + \langle \beta , x _ { i } \rangle + \epsilon _ { i }$$
(10.1)

where $\epsilon _ { i }$ is a residual or disturbance term. The usual fitting method is
by least squares, estimating $\alpha$ and $\beta$ to minimize the residual sum of
squares

$$\mathrm { L M S S E } \left( \alpha , \beta \right) = \sum _ { i = 1 } ^ { N } \left( \mathcal{Y} _ { i } - \alpha - \langle \beta , x _ { i } \rangle \right) ^ { 2 } .$$
(10.2)

We can now consider a functional extension of linear regression,
where the prediction of the scalar values $\mathcal{Y} _ { i }$ is based on functions

<!-- PageBreak -->

<!-- PageNumber="158" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

$x _ { i } .$ This problem is of interest in its own right, and also raises issues
that become relevant when we consider more complicated problems
in subsequent chapters. For illustration, let us investigate to what
extent total annual precipitation for Canadian weather stations can be
predicted from the pattern of temperature variation through the year.
To this end, let $\mathcal{Y} _ { i }$ be the logarithm of total annual precipitation at
weather station $i ,$ and let $x _ { i } = \text { Temp } _ { i }$ be its temperature function. The
interval $T$ containing index $t$ is either $\left[ 0 , 1 2 \right]$ or [0,365], depending on
whether monthly or daily data, respectively, are involved.

To extend the idea of ordinary linear regression, we must replace the
parameter $\beta$ in equation (10.1) by a function $\beta ,$ so that the model takes
the form

$$y _ { i } = \alpha + \int _ { 0 } ^ { T } x _ { i } \left( s \right) \beta \left( s \right) d s + \epsilon _ { i } = \alpha + \langle x _ { i } , \beta \rangle + \epsilon _ { i } .$$
(10.3)

In classical linear regression it is usually assumed that the covariates
$x$ are observed without error; another way of expressing this
assumption is to say that the analysis is carried out conditional
on the covariates having the values actually observed. We shall
make a similar assumption when considering regression models with
functional covariates, and consider models based on the observed
covariate functions. It may be that these have been preprocessed to
obtain smooth covariates. For functional analytic reasons beyond the
scope of our present treatment, such smoothing will not alleviate the
need for regularization within the functional regression demonstrated
in the next section.


### 10.2 A naïve approach: Functional interpolation

We now attempt to proceed along the same lines as standard linear
regression, but we shall see that some modifications are needed to give
meaningful results. Suppose, naïvely, that we attempt to estimate the
parameters in (10.3) by minimizing the residual sum of squares, noting
that with the use of inner product notation, this is expressed as

$$\mathrm { L M S S E } \left( \alpha , \beta \right) = \sum _ { i = 1 } ^ { N } \left( \mathcal{Y} _ { i } - \alpha - \langle x _ { i } , \beta \rangle \right) ^ { 2 }$$
$$= \| y - \alpha - \langle x , \beta \rangle \| ^ { 2 }$$

(10.4)

where $x$ is the N-vector of covariate functions $\left( x _ { 1 } , \ldots , x _ { N } \right) ^ { \prime } .$

For the temperature and precipitation data, it turns out that we can
find a value $\alpha$ and a function $\beta$ which yield a residual sum of squares

<!-- PageBreak -->

<!-- PageNumber="159" -->
<!-- PageHeader="10.2 A naïve approach: Functional interpolation" -->


<figure>
<figcaption>FIGURE 10.1. The weight function $\beta$ that allows perfect prediction of log total annual precipitation from observed annual pattern of temperature.</figcaption>

20

Weight function

10

0

-10

-20

JF MAM J JAS OND

Time of year

</figure>


of zero, and hence a perfect fit in the model (10.3) with no error at
all! Not only is it somewhat counterintuitive that temperature patterns
can predict overall precipitation perfectly, but the estimated regression
coefficient function $\widehat { \beta }$ shown in Figure 10.1 does not seem to convey any
useful information.

A moment's reflection yields the reason for this perfect fit. Perhaps
we can most easily explain this by reference to the high-dimensional
multivariate problem presented by the daily data. Suppose $x _ { i j }$ is the
entry for the temperature at station $i$ on day $j ,$ and we wish to predict
$\mathcal{Y} _ { i }$ by

$$\widehat { \mathcal{Y} } _ { i } = \alpha + \sum _ { j = 1 } ^ { 3 6 5 } x _ { i j } \beta _ { j } , i = 1 , 2 , \ldots , 3 5 .$$

We can view this as a finely discretized version of the functional model
being considered. This is a system of 35 equations with 366 unknowns.
Even if the coefficient matrix is of full rank, there are still infinitely
many sets of solutions, all giving a perfect prediction of the observed
data.

Returning to the functional model (10.3), we now see that the
regression coefficient function $\beta$ is underdetermined on the basis of
any finite sample $\left( x _ { i } , y _ { i } \right) ,$ because, essentially, we have an infinite
number of parameters $\beta \left( s \right)$ and only a finite number of conditions

<!-- PageBreak -->

<!-- PageNumber="160" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

$y _ { i } = \alpha + \langle x _ { i } , \beta \rangle$ to satisfy. Usually it is possible to find $\widehat { \alpha }$ and $\widehat { \beta }$ to
reduce the residual sum of squares (10.4) to zero. Furthermore, if $\beta ^ { * }$
is any function satisfying $\langle x _ { i } , \beta ^ { * } \rangle = 0$ for $i = 1 , \ldots , N ,$ then adding $\beta ^ { * }$
to $\widehat { \beta }$ does not affect the value of the residual sum of squares.

Since the space of functions satisfying (10.3) is infinite-dimensional
no matter how large our sample size $N$ is, minimizing the residual
sum of squares cannot, of itself, produce a meaningful or consistent
estimator of the parameters $\beta$ in the model (10.3). Consequently, to
provide a good estimator or even just identify $\widehat { \beta }$ uniquely, we must use
some method of regularization, and this is discussed in the following
sections.


### 10.3 Regularization by discretizing the function

In the weather data example, a possible approach is to reduce
the number of unknowns in problem (10.2) by considering the
temperatures on a coarser time scale. It is unlikely that overall
precipitation is influenced by details of the temperature pattern from
day to day, and so, for example, we could investigate how the 12-vectors
of monthly average temperatures can be used to predict total annual
precipitation. If $X$ is the $3 5 \times 1 2$ matrix containing these values, we can
then fit a model of the form $\widehat { \mathcal{Y} } = \alpha + X \beta ,$ where $\widehat { \mathcal{Y} }$ is the vector of
values of $\log$ annual precipitation predicted by the model, and $\beta$ is a
12-vector of regression parameters. Since the number of parameters
to be estimated is now only 13, and thus less than the number of
observations $N = 3 5 ,$ we can use a standard multiple regression to
fit the model by least squares.

We can summarize the fit in terms of the conventional $R ^ { 2 } = 1 -$
SSE/SSY measure, and this is 0.84, indicating $a$ rather successful fit,
even taking into account 12 degrees of freedom in the model. The
corresponding F-ratio is 9.8 with 12 and 22 degrees of freedom, and
is significant at the 1% level. The standard error estimate is 0.34, as
opposed to the standard deviation of the dependent variable of 0.69.

Figure 10.2 presents the estimated regression function $\beta ,$ obtained
by interpolating the individual estimated coefficients $\widehat { \beta _ { j } }$ as marked on
the figure. It is not easy to interpret this function directly, although
it clearly places considerable emphasis on temperature in the months
of March, April, September and December. The lack of any very clear
interpretation indicates that this problem raises statistical questions
beyond the formal difficulty of fitting an underdetermined model.
Certainly, the model uses up a rather large proportion of the 35 degrees

<!-- PageBreak -->

<!-- PageNumber="161" -->
<!-- PageHeader="10.4 Regularization using basis functions" -->


<figure>
<figcaption>FIGURE 10.2. The regression function $\beta$ for the approximation of centred annual mean log precipitation by the temperature profiles for the Canadian weather stations.</figcaption>

0.4

$

M

M

Regression function

0.2

O

N

0.0

M

-0.2

D

F

Đ

F

-0.4

0

5

10

15

Month

</figure>


of freedom available in the data. Might it not be wise to impose even
more smoothness on $\beta ?$


### 10.4 Regularization using basis functions

To reduce the degrees of freedom in the model still further, we could
average over longer time periods than one month. This would introduce
a considerable degree of arbitrariness in terms of the starting point of
the year. A preferable approach for the periodic data we are considering
is to expand the temperature curves in a Fourier basis. Of course, we
can employ a similar approach for nonperiodic data using some other
suitable basis, and this is discussed in Section 10.4.3.


#### 10.4.1 Re-expressing the model and data: Fourier bases

Let $\phi _ { 0 } , \phi _ { 1 } , \ldots .$ be the Fourier basis given in (3.10) for $T = \left[ 0 , T \right] ,$ and let
$M$ be the largest number of these basis functions that we might propose
to use. For the monthly and daily temperature data, for example, $M$
would be 12 and 365, respectively. More generally, we may choose to

<!-- PageBreak -->

<!-- PageNumber="162" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

truncate the expansion at some suitably large $K$ that does not entail
any significant loss of information.

Now expand

$$x _ { i } = \sum _ { v } c _ { i v } \phi _ { v } = c _ { i } ^ { \prime } \phi$$
(10.5)

where $c _ { i \nu }$ is the Fourier coefficient for observation $i$ and basis function
$\phi _ { \nu } ,$ and at the same time let $b$ be the vector of Fourier coefficients of
the regression function $\beta ,$ implying that

$$\beta = \sum _ { v } b _ { v } \phi _ { v } = b ^ { \prime } \phi .$$
(10.6)

The Parseval identity for Fourier series states that

$$\langle x _ { i } , \beta \rangle = \sum _ { v } c _ { i v } b _ { v } .$$

We can further simplify notation by defining the $\left( M + \right.$ 1)-vector $\left( = \right.$
$\left( \alpha , b _ { 0 } , \ldots , b _ { M - 1 } \right) ^ { \prime }$ and defining the coefficient matrix $Z$ to be the $N \times$
$\left( M + 1 \right)$ matrix $Z = \left[ \begin{array}{} { 1 } & { C } \end{array} \right]$ where $\mathrm { C }$ contains the coefficients $c _ { i v } .$ Then
the model (10.1) becomes simply

$$= Z$$
(10.7)

and the least squares estimate of the augmented parameter vector $\left( \right.$ is
the solution of the equation

$$Z ^ { \prime } Z \widetilde { \xi } = Z ^ { \prime } y .$$
(10.8)


#### 10.4.2 Smoothing by basis truncation

One very natural method of regularization is to truncate the basis by
choosing a value $K < M ,$ and setting all but the first $K + 1$ coefficients $\zeta _ { v }$
to be zero in both (10.5) and (10.6). We can then fit $5$ by least squares,
and the problem is now a standard multiple regression problem. Once
the estimate of the weight function $\left( \right.$ is available, we can retrieve $\beta$
itself by substituting into (10.6), in practice by using an inverse fast
Fourier transform.

Figure 10.3 shows the result of carrying out this procedure for the
daily weather data with varying numbers $K$ of basis functions. The
choice $K = 1 2$ is intended to correspond to the same amount of
discretization as using monthly average data, and we can see that
the weight function is similarly uninformative. To obtain results more
likely to be meaningful, we have to use a much smaller number of
basis functions, and, by considering the graphs for $K = 4$ and $K = 3 ,$

<!-- PageBreak -->

<!-- PageNumber="163" -->
<!-- PageHeader="10.4 Regularization using basis functions" -->


<figure>
<figcaption>FIGURE 10.3. Estimated regression weight functions $\beta$ using $K = 1 2 , 5 , 4$ and 3 basis functions.</figcaption>

Weight function

-6 4 -2 0 2 4 6

WWW

Weight function

0.0 0.5 1.0

-1.0

0

100

200

300

0

100

200

300

Time (days)

12 basis functions

Time (days)

5 basis functions

0.8

Weight function

-0.2 0.0 0.2 0.4

0.4

Weight function

0.0

-0.4

0

100

200

300

0

100

200

300

Time (days)

4 basis functions

Time (days)

3 basis functions

</figure>


it appears that a predictor for high precipitation is relatively high
temperature towards the end of the year.

But the model complexity increases in discrete jumps as $K$ varies
from three to five, and we might want finer control. Also, to obtain
reasonable results, $\beta$ must be rigidly constrained to lie in a low-
dimensional parametric family, and we may worry that we are missing
important features in $\beta$ as a consequence. Section 10.5.1 develops a
more flexible approach making use of a roughness penalty method.


#### 10.4.3 Re-expressions with other bases

There is no need for us to restrict attention to Fourier bases. For most
bases it is not necessarily appropriate to reduce the dimensionality by
truncating the basis expansion; instead, the required dimensionality is
specified in advance. For example $B$ B-splines on a reasonably fine mesh
provide a good basis for expanding nonperiodic functions. But note that
using a coarse mesh to reduce the dimensionality does not correspond
to merely truncating the fine mesh expansion.

For any given $K ,$ suppose that $\phi = \left( \phi _ { 1 } , \ldots , \phi _ { K } \right) ^ { \prime }$ is a basis and that
regression function $\beta$ has the expansion

$$\beta = \sum _ { v = 1 } ^ { K } b _ { v } \phi _ { v } = b ^ { \prime } \phi .$$

<!-- PageBreak -->

<!-- PageNumber="164" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

Correspondingly, expand the covariates as

$$x _ { i } = \sum _ { v = 1 } ^ { K } c _ { i v } \phi _ { v } = c _ { i } ^ { \prime } \phi .$$

To allow for bases that are not necessarily orthonormal (such as $B -$
splines), define J to be the matrix $J = \int \phi \phi ^ { \prime }$ with entries

$$J _ { j k } = \int \phi _ { j } \left( s \right) \phi _ { k } \left( s \right) d s = \langle \phi _ { j } , \phi _ { k } \rangle .$$
(10.9)

Now

$$\langle x _ { i } , \beta \rangle = \sum _ { j = 1 } ^ { K } \sum _ { v = 1 } ^ { K } c _ { i j } J _ { j v } b _ { v } ,$$

and the coefficient matrix $\mathrm { Z }$ is now defined by $Z = \left[ \begin{array}{} { 1 } & { C J } \end{array} \right] .$ With this
modification, we can now proceed in the same way as for the Fourier
basis. This results as before in (10.7) and the estimate given by (10.8).


### 10.5 Regularization with roughness penalties


#### 10.5.1 Penalizing the residual sum of squares

The estimated function $\widehat { \beta }$ in Figure 10.1 illustrates that fidelity to
the observed data, as measured by the residual sum of squares, is
not the only aim of the estimation. The roughness penalty approach
makes explicit the complementary, possibly even conflicting, aim of
avoiding excessive local fluctuation in the estimated function. To this
end, given any periodic twice differentiable function $\beta ,$ we can define
the penalized residual sum of squares

$$\mathrm { P E N S S E } _ { \lambda } \left( \alpha , \beta \right) = \sum _ { i = 1 } ^ { N } \left[ \mathcal{Y} _ { i } - \alpha - \langle x _ { i } , \beta \rangle \right] ^ { 2 } + \lambda \int _ { T } \left[ D ^ { 2 } \beta \left( s \right) \right] ^ { 2 } d s$$

$$= \| y - \alpha - \langle x _ { i } , \beta \rangle \| ^ { 2 } + \lambda \| D ^ { 2 } \beta \| ^ { 2 } .$$
(10.10)

As in Chapter 4, the integrated squared second derivative or
curvature $\int \left( D ^ { 2 } \beta \right) ^ { 2 }$ quantifies the rapid variation in $\beta ,$ and the
smoothing parameter $\lambda > 0$ controls the trade-off between roughness
and infidelity to the observed data. Sections 10.6 and 10.7 discuss the
algorithmic aspects of minimizing (10.10).

Figure 10.4 illustrates the effect of varying the smoothing parameter.
For small values of $\lambda ,$ the estimate is too variable for us to draw any
meaningful conclusions. The feature of the model that is most sensitive

<!-- PageBreak -->

<!-- PageNumber="165" -->
<!-- PageHeader="10.5 Regularization with roughness penalties" -->


<figure>
<figcaption>FIGURE 10.4. Weight functions estimated for various values of the smoothing parameter.</figcaption>

Weight function
-3 -1012

Weight function

0.5

-0.5

JFMAMJ JASOND

JFMAMJ JASOND

Time of year
Smoothing parameter = 1

Time of year
Smoothing $p a r a m e t e r = 5 0$

Weight function

0.2 0.2 0.6

Weight function

0.0 0.04 0.08

JFMAMJ JASOND

JFMAMJ JASOND

Time of year
Smoothing $p a r a m e t e r = 2 0 0 0$

Time of year
Smoothing parameter = 1000000

</figure>


to the choice of $\lambda$ is the overall effect of the first eight months of the
year, in contrast to the effect mainly attributable to the months around
February and August. Ultimately, it is impossible to give a conclusive
answer to this question merely on the basis of a small data set. Section
10.7 discusses the behaviour of the estimate for very large $\lambda .$

We can choose the smoothing parameter $\lambda$ either subjectively or
by an automatic method such as cross-validation. To apply the cross-
validation paradigm in this context, let $\alpha _ { \lambda } ^ { \left( - j \right) }$ and $\beta _ { \lambda } ^ { \left( - j \right) }$ be the estimates
of $\alpha$ and $\beta$ obtained by minimizing the penalized residual sum of
squares based on all the data except $\left( x _ { i } , y _ { i } \right) .$ We can define the cross-
validation score as

$$C V \left( \lambda \right) = \sum _ { j = 1 } ^ { N } \left( y _ { j } - \alpha _ { \lambda } ^ { \left( - j \right) } - \langle x _ { j } , \beta _ { \lambda } ^ { \left( - j \right) } \rangle \right) ^ { 2 } ,$$
(10.11)

and minimizing $\mathrm { C V } \left( \lambda \right)$ over $\lambda$ gives an automatic choice of $\lambda .$ In practice,
there are efficient algorithms for calculating the cross-validation score,
and Section 10.8 discusses these.

Choosing A by cross-validation gives the curve $\widehat { \beta }$ shown in Figure 10.5,
and the $\lambda$ value is 650. The plot of the cross-validation score $\mathrm { C V } \left( \lambda \right)$ given
in Figure 10.6 would suggest that we might also tolerate values of $\lambda$ as
high as about 50,000.

<!-- PageBreak -->

<!-- PageNumber="166" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->


<figure>
<figcaption>FIGURE 10.5. The estimated weight function for predicting the log total annual precipitation from the daily temperature pattern. The estimate was constructed by the roughness penalty method, with the smoothing parameter $\lambda = 6 5 0$ chosen by cross-validation.</figcaption>

0.6

Weight function

0.4

0.2

0.0

-0.2

JF MAM J JAS OND

Time of year

</figure>


Higher precipitation is associated with higher temperatures in the
last three months of the year and with lower temperatures in spring and
early summer. In effect, the estimated regression function $\widehat { \beta }$ defines a
contrast between average temperatures in October to November and
average temperatures in the longer period February to July, so that
rainy stations have a relatively warm autumn and cool spring, relative
to the spring-autumn differential for the average station. In fact, this
situation is typical of weather stations in coastal regions, where the
influence of the sea is to retard the seasons, as we have already seen in
Chapter 5.

In Figure 10.7, we have plotted the observed values $\mathcal{Y} _ { i }$ against the
fitted values $\widehat { \mathcal{Y} } _ { i }$ obtained using this functional regression. This simple
regression diagnostic seems to confirm the model assumptions. Section
10.8 describes another diagnostic plot.


#### 10.5.2 Connections with nonparametric regression

Some connections with nonparametric regression, as discussed for
example by Green and Silverman (1994), may be instructive. In the
ordinary regression case, the assumption of linearity is sufficient to

<!-- PageBreak -->

<!-- PageNumber="167" -->
<!-- PageHeader="10.5 Regularization with roughness penalties" -->


<figure>
<figcaption>FIGURE 10.6. The cross-validation score function $\mathrm { C V } \left( \lambda \right)$ for fitting log annual precipitation by daily temperature variation. The logarithm of the smoothing parameter is taken to base 10. The minimum is at $\lambda = 6 5 0 ,$ and values lower than 500 or larger than 50,000 seem unreasonable.</figcaption>

Cross-validation score

7.5

7.0

6.5

6.0

0

1

2

3

4

5

6

log (base 10) of smoothing parameter

</figure>


<figure>
<figcaption>FIGURE 10.7. Observed values $\mathcal{Y} _ { i }$ of log annual precipitation plotted against the values $\widehat { \mathcal{Y} } _ { i }$ predicted by the functional regression model with the smoothing parameter chosen by cross-validation. The straight line on the figure is the graph observed value = predicted value.</figcaption>

Observed values

5.0 5.5 6.0 6.5 7.0 7.5

5.5

6.0

6.5

7.0

Predicted values

</figure>


<!-- PageBreak -->

<!-- PageNumber="168" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

ensure that a model of the form (10.1) can be fitted by least squares.
However, if we relax this assumption and consider the more general
model

$$y = g \left( x \right) +$$

for some function $g ,$ then a development parallel to that of Sections
10.2 to 10.5.1 can be set out, with the following features:

· We can find, in general, an infinite number of possible functions
$g$ that interpolate the observed data.

· All these interpolating curves yield zero residual sum of squares
$\sum _ { i } \left[ y _ { i } - g \left( x _ { i } \right) \right] ^ { 2 } .$

· In suitable circumstances, minimizing a penalized sum of squares

$$\sum _ { i } \left[ y _ { i } - g \left( x _ { i } \right) \right] ^ { 2 } + \lambda \| D ^ { 2 } g \| ^ { 2 }$$

can give a good estimate $\widetilde { g } .$ We can choose the smoothing
parameter $\lambda$ by $a$ suitable cross-validation approach.

· As $\lambda \rightarrow 0 ,$ $\widetilde { g }$ tends towards the smoothest interpolant to the data,
but when $\lambda \rightarrow \infty ,$ the limiting case is the ordinary linear regression
fit, $g \left( x _ { i } \right) = \alpha + \beta x _ { i } .$

A notable difference between functional regression and ordinary
regression is that in the functional regression case, the unconstrained
linear estimator interpolates the given data in the sense of predicting
them precisely, whereas in ordinary regression, it can only approximate
them as a rule. Thus, in the functional context, linearity no longer
requires a sacrifice in fitting power.


### 10.6 Computational aspects of regularization

In this section, we consider various approaches to calculating
functional regression weight functions and cross-validation scores.
The choice of which method is best often depends on the size of
the problem. Modern computing power means that for problems of
moderate size (in whatever respect), it is no longer necessary to be
unduly concerned with very fast computation, but some applications
involve large data sets and/or functions observed at very high sampling
rates. In both of these cases we must take care to avoid unnecessarily
burdensome computations.

<!-- PageBreak -->

<!-- PageNumber="169" -->
<!-- PageHeader="10.6 Computational aspects of regularization" -->


#### 10.6.1 Direct discretization and calculation

We can approximately minimize the penalized residual sum of squares
(10.10) by discretizing the covariate curves $x _ { i }$ and the parameter
function $\beta$ onto a fine grid. At the same time we can approximate the
roughness penalty $\lambda \| D ^ { 2 } \beta \| ^ { 2 }$ by a multiple of the sum of squares of
second differences, and the integrals $\int x _ { i } \beta$ by sums. The minimization
is then of a high-dimensional quadratic form, and can be carried out
by standard numerical methods.


#### 10.6.2 Full basis expansion

$A$ basis function approach has appeal because it is especially simple
to apply, and moreover some problems in any case suggest a
particular choice of basis. The periodic nature of the temperature and
precipitation data, for example, seems naturally to call for the use of
a Fourier series basis. Our first strategy is therefore to represent the
regularized fitting problem in terms of a basis function expansion, and
then to apply the concept of regularization to this representation.

Suppose that we expand the covariate functions $x _ { i }$ and the regression
function $\beta$ to $M$ terms relative to a basis functions $\phi _ { v } ,$ as in (10.5) and
(10.6) above. Define a matrix $K$ to have entries

$$K _ { j k } = \int D ^ { 2 } \phi _ { j } \left( s \right) D ^ { 2 } \phi _ { k } \left( s \right) d s = \langle D ^ { 2 } \phi _ { j } , D ^ { 2 } \phi _ { k } \rangle .$$
(10.12)

In the Fourier case, note that $K$ is diagonal, with diagonal elements $w _ { k } ^ { 4 }$
as in Section 7.4.1. In general, the penalized residual sum of squares
can be written

$$\mathrm { P E N S E } _ { \lambda } \left( \alpha , \beta \right) = \sum _ { i } \left( \mathcal{Y} _ { i } - \alpha - \sum _ { v } c _ { i v } b _ { v } \phi _ { v } \right) ^ { 2 } + \lambda \int \left\{ \sum _ { v } b _ { v } D ^ { 2 } \phi _ { v } \left( s \right) \right\} ^ { 2 } d s$$

$$= \| y - \alpha - C b \| ^ { 2 } + \lambda b ^ { \prime } K b .$$
(10.13)

As before, we deal with the additional parameter $\alpha$ by defining the
augmented vector $5 = \left( \alpha , b \right) ^ { \prime } ,$ and at the same time use $Z$ as the
$N \times \left( M + 1 \right)$ coefficient matrix [1 C] if we are using a Fourier basis; more
generally $Z = \left[ \begin{array}{} { 1 } & { C J } \end{array} \right] ,$ with $\mathrm { J }$ defined as in (10.9). Finally, let the penalty
matrix $K$ be augmented by attaching $a$ leading column and row of $M + 1$
zeros to yield $K _ { 0 } .$ In terms of these augmented arrays, the expression
(10.13) further simplifies to

$$\left( C \right) = \| y - Z \zeta \| ^ { 2 } + \lambda \zeta ^ { \prime } K _ { 0 } \zeta .$$
(10.14)

It follows that the minimizing value $\widehat { \xi }$ satisfies

$$\left( Z ^ { \prime } Z + \lambda K _ { 0 } \right) \widehat { \xi } = Z ^ { \prime } y .$$
(10.15)

<!-- PageBreak -->

<!-- PageNumber="170" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

If the number $M$ of basis functions is not too large, then we can solve
this equation directly to find $\widehat { \alpha }$ and $\widehat { \beta } ,$ but this may be prohibitive if $M$
is as large as 365, as it would be for the daily temperature data.


#### 10.6.3 Restricting the basis expansion

Typically, regularizing in this way produces a relatively smooth
function $\beta ,$ and in the Fourier case the diagonal entries of $K$ increase
rapidly. A useful approach is to work within a lower-dimensional
problem by using a moderate number $K$ of basis functions. In the
Fourier case, this corresponds to forcing the coefficients of $\widehat { \xi }$ beyond
some point $K + 1$ to be zero. This reduces the size of the system of
equations (10.15).

However, in contrast to Section 10.4.2, the idea is not to use $K$ as
a smoothing parameter. Instead, the regularization is still primarily
controlled by the parameter $\lambda ,$ and the dimension reduction is purely
a numerical device to reduce the computation without substantially
altering the actual result. In practice, values of $K$ around 20 or 30 give
good results, except possibly for very small values of the smoothing
parameter and very large data sets.


### 10.7 The direct penalty method for computing $\beta$

We now turn to a more direct way of using the roughness penalty
approach that computes $\widehat { \beta }$ direction without using basis functions. Our
first task is to show how we can set up this approach as a two-stage
process, firstly minimizing a simple quadratic expression to obtain
the vector of values $\widehat { \mathcal{Y} }$ approximating the data vector $\mathcal{Y} ,$ and secondly
computing the smoothest linear functional interpolant of these values.


#### 10.7.1 Functional interpolation

We have already seen that the observed data can, in general, be fitted
exactly by an infinite number of possible parameter choices $\left( \alpha , \beta \right) .$ In
some contexts, it may be of interest to define a functional interpolant
$\left( \widetilde { \alpha } , \widetilde { \beta } \right)$ to the given data by the smoothest parameter function choice
that fits the data exactly. In any case, we need to consider this problem
in defining the technique used to compute the estimate for $\beta$ in Figure
10.5. Therefore, we require that estimate $\left( \widetilde { \alpha } , \widetilde { \beta } \right)$ minimizes $\| D ^ { 2 } \beta \| ^ { 2 } ,$
subject to the $N$ constraints

$$y _ { i } = \widetilde { \alpha } + \langle x _ { i } , \widetilde { \beta } \rangle .$$
(10.16)

<!-- PageBreak -->

<!-- PageNumber="171" -->
<!-- PageHeader="10.7 The direct penalty method for computing $\beta$" -->

The functional interpolant is the limiting case of the regularized
estimator of Section 10.5.1 as $\lambda \twoheadrightarrow 0 .$ In fact, the curve $\widetilde { \beta }$ resulting from
interpolating the weather data is the curve shown in Figure 10.1.

We can consider this minimization problem (10.16) as a way of
quantifying the roughness or irregularity of the response vector $\mathcal{Y}$
relative to the observed functional covariates $x _ { i } .$ More generally, if
$z _ { 1 } , \ldots , z _ { N }$ is any sequence of values, then we can define the roughness
of $z$ relative to the functional covariates $x _ { i }$ as the roughness of the
smoothest function $\beta _ { z }$ such that

$$z _ { i } = \alpha _ { z } + \langle x _ { i } , \beta _ { z } \rangle$$

for all $i ,$ for some constant $\alpha _ { z } .$ This method of defining the roughness
of a variate $z _ { i }$ will be of considerable conceptual and practical use later.


#### 10.7.2 The two-stage minimization process

Section 10.7.3 shows that we can define an order $N$ matrix $\mathbb{R}$ such that
the roughness of a variate $z$ can be expressed as the quadratic form

$$\int \left[ D ^ { 2 } \beta \left( s \right) \right] ^ { 2 } d s = z ^ { \prime } R z .$$

Assuming this to be true for the moment, we can conceptualize the
solution of the smoothing problem by dividing the minimization of the
penalized residual sum of squares into two stages:

Stage 1: Find predicted values $\widehat { \mathcal{Y} }$ that minimize $\mathrm { P E N S S E } _ { \lambda } \left( \widehat { \mathcal{Y} } \right) = \sum _ { i } \left( \mathcal{Y} _ { i } - \right.$
$\left. \widehat { \mathcal{Y} } _ { i } \right) ^ { 2 } + \lambda \widehat { y } ^ { \prime } \mathrm { R } \widehat { \mathcal{Y} } ,$ the solution to which is

$$\widehat { \mathcal{Y} } = \left( I + \lambda R \right) ^ { - 1 } \mathcal{Y} .$$

Stage 2: Find the smoothest linear functional interpolant $\left( \alpha , \beta \right)$
satisfying

$$\widehat { \mathcal{Y} } _ { i } = \alpha + \int x _ { i } \left( s \right) \beta \left( s \right) d s .$$
(10.17)

The following argument shows this two stage-procedure indeed
minimizes $\mathrm { P E N S S E } _ { \lambda } \left( \alpha , \beta \right) .$ Write the minimization problem as one of
first minimizing $\mathrm { P E N S S E } _ { \lambda } \left( \alpha , \beta \right)$ as a function of $\left( \alpha , \beta \right)$ but with $\widehat { \mathcal{Y} }$ fixed,
and then minimizing the result with respect to $\widehat { \mathcal{Y} } .$ Formally, this is
expressed as

$$\min _ { \widehat { \jmath } } \left[ \min _ { \alpha , \beta } \left\{ \mathrm { P E N S S E } _ { \lambda } \left( \alpha , \beta \right) \right\} \right]$$
$$= \min _ { \widehat { \mathcal{Y} } } \left\{ \sum \left( \mathcal{Y} _ { i } - \widehat { \mathcal{Y} } _ { i } \right) ^ { 2 } + \lambda \min _ { \beta } \int \left[ D ^ { 2 } \beta \left( s \right) \right] ^ { 2 } d s \right\} ,$$
(10.18)

<!-- PageBreak -->

<!-- PageNumber="172" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

where the inner minimizations over $\alpha$ and $\beta$ are carried out keeping
fixed the values of the linear functionals $\widehat { \mathcal{Y} } _ { i } ,$ as defined in (10.17).

But according to our assumption, these inner minimizations yield
$\left( \alpha , \beta \right)$ as the smoothest functional interpolant to the variate $\widehat { \mathcal{Y} } ,$ so we
may now write the equation as

$$\mathrm { P E N S S E } _ { \lambda } \left( \alpha , \beta \right) = \min _ { \widehat { \mathcal{Y} } } \left\{ \sum \left( \mathcal{Y} _ { i } - \widehat { \mathcal{Y} } _ { i } \right) ^ { 2 } + \lambda \widehat { \mathcal{Y} } ^ { \prime } \mathrm { R } \widehat { \mathcal{Y} } \right\} .$$
(10.19)

For a moment setting aside the question of how $R$ is defined, one of
the advantages of the roughness penalty approach to regularization is
that it allows this conceptual division to be made, in a sense uncoupling
the two aspects of the smoothing procedure. However, it should not
be forgotten that the roughness penalty is used in constructing the
matrix $\mathbb{R} ,$ and so the functional nature of the covariates $x _ { i } ,$ and the
use of $\int \left( D ^ { 2 } \beta \right) ^ { 2 }$ to measure the variability of the regression coefficient
function $\beta ,$ are implicit in both stages set out above.

We can think of the two-stage procedure in two ways: first as
a practical algorithm in its own right, and second as an aid to
understanding and intuition. In subsequent chapters we shall see that
it has wider implications than those discussed here.

To use the algorithm in practice, it is necessary to derive the matrix
$R ,$ and we now show how to do this.


#### 10.7.3 Functional interpolation revisited

In this section, we present an algorithmic solution to the linear
functional interpolation problem presented in Stage 2 of the two-stage
procedure set out in Section 10.7.2. The aim is to find the smoothest
functional interpolant $\left( \widetilde { \alpha } , \widetilde { \beta } \right)$ to a specified N-vector $\widehat { \mathcal{Y} }$ relative to the
given covariates $x _ { i } ,$ $i = 1 , \ldots , N .$ For practical purposes, our algorithm
is suitable for the case where the sample size $N$ is moderate, and
matrix manipulations of $N \times N$ matrices do not present an unacceptable
computational burden.

Let the matrix Z be defined in terms of the functional covariates $x _ { i }$
as described in Section 10.4. In terms of basis expansions, we wish to
solve the problem

$$\min \left\{ \zeta ^ { \prime } R \zeta \right\} \text { subject to } Z \zeta = \widehat { \mathcal{Y} } .$$
(10.20)

First we define some more notation. By rotating the basis if necessary,
assume that the first $M _ { 0 }$ basis functions $\phi _ { v }$ span the space of all
functions $f$ with roughness $\int \left( D ^ { 2 } f \right) ^ { 2 } = 0 .$ In the Fourier case, this is true
without any rotation: The only periodic functions with zero roughness

<!-- PageBreak -->

<!-- PageNumber="173" -->
<!-- PageHeader="10.7 The direct penalty method for computing $\beta$" -->

are constants, so $M _ { 0 } = 1 ,$ and the basis $\phi$ consists of just the constant
function.

Let $\mathbb{K} _ { 2 }$ be the matrix obtained by removing the first $M _ { 0 }$ rows and
columns of $K .$ Then $\mathbb{K} _ { 2 }$ is strictly positive-definite, and the rows and
columns removed are all zeroes. In the Fourier case, $K _ { 2 }$ is diagonal.

Corresponding to the above partitioning, let $\mathrm { Z } _ { 1 }$ be the matrix of the
first $M _ { 0 } + 1$ columns of $Z ,$ and let $Z _ { 2 }$ be the remaining columns. Defining
$P$ to be the $N \times N$ projection matrix $P = I - Z _ { 1 } \left( Z _ { 1 } ^ { \prime } Z _ { 1 } \right) Z _ { 1 } ^ { \prime }$ permits us to
define $Z ^ { * } = P Z _ { 2 } .$ In the periodic case, $\mathrm { Z } _ { 1 }$ has columns $\left( 1 , \ldots , 1 \right)$ and
$\left( \widetilde { x } _ { 1 } , \ldots , \widetilde { x } _ { N } \right) ,$ where $\check { x } _ { i } = \int _ { T } x _ { i } \left( s \right) d s$ for each $i$ i. Thus $\mathrm { P }$ is the $N \times N$
matrix that projects any N-vector $z$ to its residuals from its linear
regression on $\widetilde { x } _ { i } .$

Continuing with this partitioning process, let $1$ be the vector of the
first $M _ { 0 } + 1$ components of $,$ and let $2$ be the remaining components
of $.$ Then, by multiplying both sides by $\mathrm { Z } ^ { \prime }$ the constraint

$$Z C = Z _ { 1 } C _ { 1 } + Z _ { 2 } C _ { 2 } = \widehat { y }$$

implies that

$$Z _ { 1 } ^ { \prime } Z _ { 1 } G _ { 1 } + Z _ { 1 } ^ { \prime } Z _ { 2 } G _ { 2 } = Z _ { 1 } ^ { \prime } \widehat { y } .$$
(10.21)

Solving for $1$ alone gives

$$G _ { 1 } = \left( Z _ { 1 } ^ { \prime } Z _ { 1 } \right) ^ { - 1 } Z _ { 1 } ^ { \prime } \left( \widehat { y } - Z _ { 2 } f _ { 2 } \right) \text { and } Z _ { 1 } G _ { 1 } = P \left( \widehat { y } - Z _ { 2 } Z _ { 2 } \right) .$$
(10.22)

In the periodic case, equation (10.22) indicates that $1$ is obtained
by linear regression of the values $\left( \widehat { \mathcal{Y} } - \mathrm { Z } _ { 2 } \beta _ { 2 } \right)$ on the vector with
components $\bar { x } _ { i } .$ Thus, once $2$ has been determined, we can find $5 1 .$

Now substitute the solution (10.22) for $\zeta _ { 1 }$ into the constraint (10.21)
and rearrange to show that we can find $5 2$ by solving the minimization
problem

$$\min _ { \zeta _ { 2 } } \left\{ \zeta _ { 2 } ^ { \prime } K _ { 2 } \zeta _ { 2 } \right\} \text { subject to } Z ^ { * } \zeta = \mathrm { P } \widehat { \mathcal{Y} }$$
(10.23)

using the fact that $\zeta ^ { \prime } K \zeta = \zeta _ { 2 } ^ { \prime } K _ { 2 } \zeta _ { 2 } .$

Let $R$ be defined as the Moore-Penrose $8$ g-inverse

$$R = \left( Z ^ { * } K _ { 2 } ^ { - 1 } Z ^ { * \prime } \right) ^ { + } .$$
(10.24)

The solution of the minimization (10.23) is then given by

$$G _ { 2 } = K _ { 2 } ^ { - 1 } Z ^ { * } { } ^ { \prime } R \widehat { y }$$
(10.25)

and the minimum value of the objective function $5 ^ { \prime } R S$ is therefore
given by

$$G ^ { \prime } R G = G _ { 2 } ^ { \prime } K _ { 2 } G _ { 2 } = \widehat { y } ^ { \prime } R Z ^ { * \prime } K _ { 2 } ^ { - 1 } K _ { 2 } K _ { 2 } ^ { - 1 } Z ^ { * } R j$$
$$= \widehat { y } ^ { \prime } R R ^ { + } R \widehat { y } = \widehat { y } ^ { \prime } R \widehat { y } .$$

(10.26)

<!-- PageBreak -->

<!-- PageNumber="174" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->

This is the assumption we made above in defining the two-step
procedure, and moreover we have now defined the matrix $R .$

We can sum up this discussion by setting out the following algorithm
for functional interpolation:

Step 1: Calculate matrices $P = I - Z _ { 1 } \left( Z _ { 1 } ^ { \prime } Z _ { 1 } \right) Z _ { 1 } ^ { \prime }$ and $Z ^ { * } = P Z _ { 2 } .$ In effect,
the columns of $\mathrm { z } ^ { * }$ are the residuals from a standard regression
of the corresponding columns of $\mathrm { Z } _ { 2 }$ on the design matrix $\mathrm { Z } _ { 1 } .$

Step 2: Compute $R$ as defined in (10.24) above.

Step 3: Compute $5 2$ from (10.24) and use (10.22) to find $5 1 .$

Of course, if all we require is the roughness of $,$ then we can find $\widehat { \mathcal{Y} } ^ { \prime } \mathrm { R } \widehat { \mathcal{Y} }$
from (10.24) without actually calculating $.$

Finally, returning to our two-stage technique for smoothing, we can
carry out the first step by solving the equation

$$\left( I + \lambda R \right) \widehat { y } = y .$$

Note that if $R$ is either diagonal (as for the Fourier basis) or band-
structured (as for the B-spline basis) the solution to this equation is
very cheap to compute, and hence trying out various values for $\lambda$ is
quite feasible.

If we are dealing with a large data set by truncating or restricting
the basis expansion to a reasonable dimensionality $K$ as described in
Section 10.6.3, then we wish in general only to assess the roughness of
variates of the form Zt for known $\left( \right.$ with $\zeta _ { j } = 0$ for $j > m .$ It is usually
more appropriate to calculate $5 ^ { \prime } R S$ directly for such variates directly
if necessary.


### 10.8 Cross-validation and regression diagnostics

We have already noted the possibility of choosing the smoothing
parameter $\lambda$ by cross-validation. Various economies are possible in
calculating the cross-validation score $\mathrm { C V } \left( \lambda \right)$ as defined in (10.11).

Let $S$ be the so-called hat matrix of the smoothing procedure which
maps the data values $\mathcal{Y}$ to their fitted values $\widehat { \mathcal{Y} }$ for any particular value
of $\lambda .$ $A$ calculation described, for example, in Section 3.2 of Green and
Silverman (1994), shows that the cross-validation score satisfies

$$C V \left( \lambda \right) = \sum _ { i = 1 } ^ { N } \left( \frac { y - \widehat { y } _ { i } } { 1 - S _ { i i } } \right) ^ { 2 }$$

<!-- PageBreak -->

<!-- PageNumber="175" -->
<!-- PageHeader="10.8 Cross-validation and regression diagnostics" -->

If $N$ is of moderate size and we are using the algorithm described in
Section 10.7, then the hat matrix satisfies

$$S = \left( I + \lambda R \right) ^ { - 1 } .$$

The calculation (10.24) of the symmetric matrix $R$ as a Moore-Penrose
g-inverse means that we have expressed $\mathbb{R}$ as $\mathrm { U d i a g } \left( \rho _ { 1 } , \rho _ { 2 } , \ldots \right) \mathrm { U } ^ { \prime } ,$ where
$\mathrm { U }$ is an orthogonal matrix and the $\rho _ { i }$ are the eigenvalues of $R .$ It follows
that the diagonal elements of $S$ are given by

$$S _ { i i } = \sum _ { j } \left( 1 + \lambda \rho _ { j } \right) ^ { - 1 } u _ { i j } ^ { 2 } .$$

If $N$ is large and we are considering an expansion in a moderate
number $K$ of basis functions, as in Section 10.6.3, then we can find
the diagonal elements of $\mathrm { S }$ directly from

$$S = Z \left( Z ^ { \prime } Z + \lambda R \right) ^ { - 1 } Z ^ { \prime } .$$

From S, we can also compute an indicator of the effective degrees
of freedom used up in the approximation. Either trace S or trace $S ^ { 2 }$
were recommended for this purpose by Buja, Hastie, and Tibshirani
(1989). For the fit in Figure 10.5, defined by minimizing the cross-
validation criterion, the effective degrees of freedom are estimated to
be trace $S = 6 . 8 .$

Another important use of the hat matrix $\mathrm { S }$ is in constructing various
regression diagnostics. The diagonal elements of the hat matrix are
often called leverage values; they determine the amount by which the
fitted value $\widehat { \mathcal{Y} } _ { i }$ is influenced by the particular observation $\mathcal{Y} _ { i } .$ If the
leverage value is particularly high, the fitted value needs to be treated
with some care. Two standard ways of assessing the regression fit
are to examine the raw residuals $y _ { i } - \widehat { y } _ { i }$ and the deleted residuals
$\left( \mathcal{Y} _ { i } - \widehat { \mathcal{Y} } _ { i } \right) / \left( 1 - S _ { i i } \right)$ the latter give the residual between $\mathcal{Y} _ { i }$ and the value
predicted from the data set with case $i$ deleted. We refer readers to
works on regression diagnostics such as Cook and Weisberg (1982).

Figure 10.8 shows a plot of deleted residuals against fitted values
for the log precipitation and temperature example, with the smoothing
parameter chosen by cross-validation. The three observations with
small predicted values have somewhat larger leverage values (around
0.4) than the others (generally in the range 0.1 to 0.2). This is not
surprising, given that they are somewhat isolated from the main part
of the data.

<!-- PageBreak -->

<!-- PageNumber="176" -->
<!-- PageHeader="10. Functional linear models for scalar responses" -->


<figure>
<figcaption>FIGURE 10.8. Deleted residuals from the fitted prediction of log annual precipitation from overall temperature pattern.</figcaption>

1.0

Deleted residuals

0.5

0.0

-0.5

-1.0

5.5

6.0

6.5

7.0

Predicted values

</figure>


### 10.9 Functional regression and integral equations

Functional interpolation and regression can be viewed as a different
formalization of a problem already considered in detail elsewhere,
reconstructing a curve given certain indirect observations. Suppose
that $g$ is a curve of interest, and that we have noisy observations of
a number of linear functionals $l _ { i } \left( g \right) .$ Such a problem was explored by
Engle, Granger, Rice and Weiss (1986); see also Section 4.7 of Green and
Silverman (1994). The problem involved reconstructing the effect of
temperature $t$ on electricity consumption, so that $g \left( t \right)$ is the expected
use of electricity per consumer on a day with average temperature $t$ t.
Various covariates were also considered, but these need not concern us
here.

Electricity bills are issued on various days and always cover the
previous 28 days. For bills issued on day $i ,$ the average consumption
(after correcting for covariates) would be modelled to satisfy

$$\frac { 1 } { 2 8 } E Y _ { i } = \langle \theta _ { i } , g \rangle$$

where $\theta _ { i }$ is the probability density function of temperature over the
previous 28 day period. By setting $x _ { i } = 2 8 \theta _ { i }$ and $\beta = g ,$ we see that

<!-- PageBreak -->

<!-- PageNumber="177" -->
<!-- PageHeader="10.9 Functional regression and integral equations" -->

this problem falls precisely into the functional regression context, and
indeed the method used by the original authors to solve it corresponds
precisely to the regularization method we have set out.

More generally, regularization is a very well known tool for solving
integral equations; see, for example, Section 12.3 of Delves and
Mohamed (1985).

<!-- PageBreak -->


## 11 Functional linear models for functional responses


### 11.1 Introduction

The aim of Chapter 10 was to predict a scalar response $y$ from a
functional covariate $x .$ We now consider a fully functional linear model
in which both the response $y$ and the covariate $x$ are functions.
For instance, in the Canadian weather example, we might wish to
investigate to what extent we can predict the complete log precipitation
profile LPrec of $a$ weather station from information in its complete
temperature profile Temp.

We assume that we have $N$ observed functions $\mathcal{Y} _ { i } ,$ each with
associated covariate function $x _ { i } .$ The $x _ { i }$ are functions on an interval
$T _ { X }$ and the $\mathcal{Y} _ { i }$ on an interval $T _ { Y } .$ There is no need for the intervals to be
the same. In this chapter, we use the notation $x$ and $y$ for the vectors
of functions with components being the functions $x _ { i }$ and $y _ { i } .$

When $\mathcal{Y} _ { i }$ is a function rather than a multivariate observation, the
usual linear model becomes

$$\widehat { \mathcal{Y} } _ { i } \left( t \right) = \alpha \left( t \right) + \int _ { T _ { X } } x _ { i } \left( s \right) \beta \left( s , t \right) d s$$
(11.1)

Clearly, the regression function $\beta$ must be a function of $t$ as well as
of $s ,$ but the principle of the linear effect of the covariates $x _ { i }$ on the
parameter function $\beta$ remains the same. We can interpret the regression
function $\beta$ for a fixed value of $t ,$ denoted by $\beta \left( \cdot , t \right) ,$ as the relative

<!-- PageBreak -->

<!-- PageNumber="180" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->

weights placed on temperature for all possible times to predict log
precipitation at time $t .$

The function $\alpha$ plays the part of the constant term in the standard
regression setup. One simple approach to the estimation of $\alpha$ is to
centre the observed $\mathcal{Y} _ { i }$ and the given $x _ { i }$ by subtracting their sample
average functions $\widetilde { \mathcal{Y} }$ and $\overrightarrow { x }$ and to consider the model as

$$\widehat { \mathcal{Y} } _ { t } \left( t \right) - \bar { \mathcal{Y} } \left( t \right) = \int _ { T _ { X } } x _ { i } ^ { * } \left( s \right) \beta \left( s , t \right) d s$$
(11.2)

where $x _ { i } ^ { * } = x _ { i } - x .$ This constrains the value of $\alpha \left( t \right)$ to be equal to
$\bar { \mathcal{Y} } \left( t \right) - \int \bar { x } \left( s \right) \beta \left( s , t \right)$ ds. Of course, on occasion we may wish to estimate
$\alpha$ in some other way, for example by incorporating some smoothing,
but we do not consider this possibility in any detail.

In whatever way we deal with $\alpha ,$ the fitting criterion in the present
context is the extension of the residual sum of squares LMSSE as defined
in (10.2) to assess lack of fit across the index $t$ as well as $i .$ A simple
measure that combines information across $t$ in $T _ { Y }$ is the integrated
squared residual

$$L M I S E = \| y - \widehat { y } \| ^ { 2 } = \sum _ { i = 1 } ^ { N } \int _ { T _ { Y } } \left[ y _ { i } \left( t \right) - \alpha \left( t \right) - \int _ { T _ { X } } x _ { i } \left( s \right) \beta \left( s , t \right) d s \right] ^ { 2 } d t .$$
(11.3)


### 11.2 Estimating $\beta$ by basis representations

In this section we obtain an expression for LMISE using basis functions
that can be used to fit the model (11.1) in practice. For the moment,
we use the special case (11.2) of the model, and centre the $x _ { i }$ and $\mathcal{Y} _ { i } ,$
writing $y _ { i } ^ { * } = y _ { i } - j .$ Expand the $x _ { i } ^ { * }$ in a basis $\phi _ { j }$ and the $\mathcal{Y} _ { i } ^ { * }$ in a basis
$\psi _ { k } ,$ to give

$$x _ { i } ^ { * } = \sum _ { j = 1 } ^ { J } c _ { i j } \phi _ { j } = c _ { i } ^ { \prime } \phi$$

and

$$y _ { i } ^ { * } = \sum _ { k = 1 } ^ { K } d _ { i k } \psi _ { k } = d _ { i } ^ { \prime } \psi ,$$

where $\phi$ and $\psi$ are the $J -$ and K-vectors of the respective basis
functions. We denote the matrices of coefficients by $C$ and $\mathrm { D } ,$ so that
we can write these expressions in the function form

$$x ^ { * } = C \phi$$

<!-- PageBreak -->

<!-- PageNumber="181" -->
<!-- PageHeader="11.3 Fitting the model by basis expansions" -->

and

$$\mathrm { y } ^ { * } = \mathrm { D } \psi .$$

We consider the expression of $\beta$ as a double expansion

$$\beta \left( s , t \right) = \sum _ { j = 1 } ^ { J } \sum _ { k = 1 } ^ { K } b _ { j k } \phi _ { j } \left( s \right) \psi _ { k } \left( t \right) = \phi \left( s \right) ^ { \prime } B \psi \left( t \right) ,$$
(11.4)

where $B$ is a $J \times K$ matrix of coefficients $b _ { j k } ,$ or, more compactly, as
$\beta = \phi ^ { \prime } B \psi .$ Define $\mathrm { J } _ { \phi }$ and $\mathrm { J } _ { \Psi }$ to be the matrices of inner products
between the elements of the $\phi$ and $\Psi$ bases, respectively. Thus,

$$J _ { \phi } = \int _ { T _ { X } } \phi \left( s \right) \phi \left( s \right) ^ { \prime } d s$$

and

$$J _ { \Psi } = \int _ { T _ { Y } } \psi \left( s \right) \psi \left( s \right) ^ { \prime } d s .$$

Substitute the basis expansions of $x _ { i }$ and $\beta$ into (11.1) to give

$$\widehat { y } ^ { * } \left( t \right) = \int \mathrm { C } \phi \left( s \right) \phi \left( s \right) ^ { \prime } \mathrm { B } \psi \left( t \right) d s = \mathrm { C J } _ { \phi } \mathrm { B } \psi \left( t \right) .$$

If we let $\widehat { \mathrm { D } }$ be the matrix of coefficients of the basis expansion of the
vector of predictors $\widehat { y } ^ { * }$ (corresponding to the matrix $\mathrm { D }$ for the vector
$\mathrm { y } ^ { * } ,$ we obtain the matrix form of the model

$$\widehat { \mathrm { D } } = \mathrm { C J } _ { \phi } \mathrm { B } .$$

Now we can get an expression for the integrated squared residual:

$$\| \widehat { \mathcal{Y} } _ { i } - \mathcal{Y} _ { i } \| ^ { 2 } = \| \widehat { \mathcal{Y} } _ { i } ^ { * } - \mathcal{Y} _ { i } ^ { * } \| ^ { 2 } = \left\{ \left( \widehat { \mathrm { D } } - \mathrm { D } \right) \mathrm { J } _ { \psi } \left( \widehat { \mathrm { D } } - \mathrm { D } \right) ^ { \prime } \right\} _ { i i }$$

and, finally,

$$\mathrm { L M L S E } \left( \mathrm { B } \right) = \mathrm { t r a c e } \left\{ \left( \mathrm { C J } _ { \phi } \mathrm { B } - \mathrm { D } \right) \mathrm { J } _ { \psi } \left( \mathrm { C J } _ { \phi } \mathrm { B } - \mathrm { D } \right) ^ { \prime } \right\} ,$$
(11.5)

a quadratic form in the unknown coefficient matrix $B .$ If the bases $\phi$
and $\psi$ are orthonormal, then of course the matrices $\mathrm { J } _ { \phi }$ and $\mathrm { J } _ { \Psi }$ are the
identity matrices of order $J$ and $K ,$ respectively, and the expression for
LMISE(B) simplifies accordingly.


### 11.3 Fitting the model by basis expansions


#### 11.3.1 Some linear algebra preliminaries

First of all let us consider the minimization of the quantity LMISE (B),
as given in (11.5). In the case where $\mathrm { J } _ { \phi }$ and $\mathrm { J } _ { \Psi }$ are identity matrices, the

<!-- PageBreak -->

<!-- PageNumber="182" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->


<figure>
<figcaption>FIGURE 11.1. The functional parameter function $\beta$ for the prediction of log precipitation from temperature, estimated direct from the data. The value $\beta \left( s , t \right)$ shows the influence of temperature at time $s$ on log precipitation at time $t$ t.</figcaption>

2000 4000

beta(s,t)

0

-4000-2000

300

t (64 basis functions used)

200

300

$\begin{array}{} { 1 0 0 } \\ { s \left( 6 4 \right. } \end{array}$ basis functions used)

200

100

</figure>


matrix $\mathbb{B}$ will minimize (11.5) if and only if

$$C ^ { \prime } C B = C ^ { \prime } D$$

so that

$$B = \left( C ^ { \prime } C \right) ^ { - } C ^ { \prime } D .$$
(11.6)

The matrix $B$ is easily found by using the SVD of $\mathrm { c } .$ Write $C = U \Delta _ { C } V ^ { \prime }$
where $\Delta _ { \mathcal{C} }$ is a diagonal matrix with strictly positive diagonal elements
and $\mathrm { U }$ and $\mathrm { V }$ have orthonormal columns. Then $C ^ { \prime } C = V \Delta _ { C } ^ { 2 } V ^ { \prime } ,$ and hence
the Moore-Penrose $g$ g-inverse of $C ^ { \prime } C$ is $V \Delta _ { C } ^ { - 2 } V ^ { \prime } .$ Substituting into (11.6)
gives

$$B = V \Delta _ { C } ^ { - 1 } U ^ { \prime } D .$$
(11.7)

In the example discussed in detail below, we use Fourier bases which
are orthonormal, and so we need not consider the case of more general
$\mathrm { J } \phi$ and $\mathrm { J } _ { \Psi } .$ For the more general case, the results corresponding to (11.6)
and (11.7) are notationally more complicated but are easily stated. We
require that

$$\mathrm { J } _ { \phi } \mathrm { C } ^ { \prime } \mathrm { C J } _ { \phi } \mathrm { B J } _ { \psi } = \mathrm { J } _ { \phi } \mathrm { C } ^ { \prime } \mathrm { D J } _ { \psi } .$$

<!-- PageBreak -->

<!-- PageNumber="183" -->
<!-- PageHeader="11.3 Fitting the model by basis expansions" -->

Provided $\mathrm { J } _ { \Psi }$ is nonsingular (i.e. the functions $\psi$ are not linearly
dependent), this implies that

$$\mathrm { J } _ { \phi } \mathrm { C } ^ { \prime } \mathrm { C J } _ { \phi } \mathrm { B } = \mathrm { J } _ { \phi } \mathrm { C } ^ { \prime } \mathrm { D }$$

so that $\mathrm { C }$ in (11.6) is replaced by $\mathrm { C J } _ { \phi } ,$ and $\mathrm { J } _ { \Psi }$ plays no role in defining
the coefficient matrix $B .$


#### 11.3.2 Fitting the model without regularization

We now apply this methodology to the data on Canadian climate,
considering the detailed data that give daily precipitation and
temperature. Because all the functions in this example are intrinsically
periodic, we can expand both the log precipitations and the
temperatures in Fourier series. We preprocessed the data by fitting a
Fourier series with 64 terms, applying a roughness penalty smoother
by tapering the series to eliminate very local variation. Therefore $C$ and
$D$ are $6 4 \times 3 5$ matrices, and $B$ as found by (11.7) is a $6 4 \times 6 4$ matrix.
Substituting into (11.4) gives the estimated function $\beta$ plotted in Figure
11.1.

We see that the function $\beta$ estimated by this method is extremely
variable. It is also the case that this $\beta$ gives perfect prediction of the
given data. Although this is superficially attractive, it does not make
physical sense: whatever influence temperature patterns may have on
precipitation patterns, it is naïve to imagine that the precipitation
pattern at a place can be entirely accounted for by its temperature
pattern.

The reason for this overfitting is an extension of the discussion in
Section 10.2 on functional interpolation. Let Temp be the vector of
observed covariate functions and LPrec the vector of observed log
precipitations. Consider any fixed $t .$ As in Section 10.2, we can find
a number $\alpha _ { t }$ and a function $\beta _ { t }$ such that, for all $i ,$

$$\mathrm { L P r e c } _ { i } \left( t \right) = \alpha _ { t } + \langle \mathrm { T e m p } _ { i } , \beta _ { t } \rangle$$

without any error. Writing $\alpha \left( t \right)$ for $\alpha _ { t } ,$ and $\beta \left( s , t \right)$ for $\beta _ { t }$ yields

$$L P r e c _ { i } \left( t \right) = \alpha \left( t \right) + \int _ { T _ { X } } T e m p _ { i } \left( s \right) \beta \left( s , t \right) d s$$

a perfect fit to the observed data. Just as in Chapter 10, we must
regularize the functional predictor variable. This is discussed in the
next section.

<!-- PageBreak -->

<!-- PageNumber="184" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->


<figure>
<figcaption>FIGURE 11.2. Perspective plot of estimated $\beta$ function truncating the basis for the temperature covariates to 7 terms.</figcaption>

3

N

$\frac { 5 } { 8 }$

6

1

R

300

t ( 64 basis functions used)

200

300

basis functions used)

200

100

100

s (7

</figure>


### 11.4 Regularizing the fit


#### 11.4.1 Restricting the basis of the predictor variable

Just as in the case of the prediction of a scalar response from a
functional predictor, $a$ natural approach is to truncate the basis $\phi$ in
which the predictors are expressed. Instead of expanding the $x _ { i } ^ { * } ,$ in
a series of length $J ,$ we choose some $J _ { 0 } < J$ and discard all but the
first $J _ { 0 }$ terms in the expansion of the $x _ { i } ^ { * } .$ Then $\mathrm { C }$ is an $n \times J _ { 0 }$ matrix,
and $B$ is $J _ { 0 } \times K .$ Otherwise, the numerical details are the same; there
is considerable computational economy because the complexity of the
SVD and of other matrix calculations is lessened by the reduction in
the sizes of the matrices involved.

We apply this approach to the weather data, setting $J _ { 0 } = 7 .$ Figure
11.2 shows the resulting estimated $\beta$ function. The resulting prediction
of the annual pattern of log precipitation at four selected stations
is demonstrated in Figure 11.3. In this figure, both the original data
and the predictions for log precipitation have their annual mean
subtracted, to highlight the pattern of precipitation rather than its
overall level. The precipitation pattern is quite well predicted except
for Edmonton, which therefore has a precipitation pattern different
from other weather stations with similar temperature profiles.

<!-- PageBreak -->

<!-- PageNumber="185" -->
<!-- PageHeader="11.4 Regularizing the fit" -->


<figure>
<figcaption>FIGURE 11.3. Original data (solid) and predictions (dashed) of log precipitation relative to annual mean for each of 4 weather stations. The prediction is carried out using an estimated $\beta$ function with the temperature covariate truncated to 7 terms.</figcaption>

Montreal

Edmonton

Log precipitation

1.0

Log precipitation

1.0

0.0

0.0

-1.0

-1.0

JFMAMJ JASOND

JFMAMJ JASON D

Time of year
(7 and 64 basis functions used)

Time of year
(7 and 64 basis functions used)

Prince Rupert

Resolute

Log precipitation

1.0

Log precipitation

1.0

0.0

0.0

-1.0

-1.0

JFMAMJ JASOND

JFMAMJ JASON D

Time of year

(7 and 64 basis functions used)

Time of year
(7 and 64 basis functions used)

</figure>


Although the plot of the estimated $\beta$ function demonstrates $a$ more
plausible influence of temperature pattern on precipitation pattern, it is
not easy to interpret. As a function of $t$ for any fixed $s$ it is irregular, and
this irregularity is easily explained. Because every Fourier coefficient
of log precipitation is allowed to be predicted by the temperature
covariate, the prediction contains frequency elements at all levels. By
the arguments given in Chapter 10, we expect that each individual
Fourier coefficient will be predicted sensibly as a scalar response.
However, in putting these together to give a functional prediction, the
high-frequency terms are given inappropriate weight. From a common-
sense point of view, we cannot expect overall temperature patterns to
affect a very high frequency aspect of log precipitation at all. To address
this difficulty, we consider the idea of restricting or truncating the $\psi$
basis in terms of which the functional response variable is expanded.


#### 11.4.2 Restricting the basis of the response variable

In this section, we consider the approach of truncating the $\psi$ basis,
allowing the prediction of only low-frequency aspects of the response
variable. In our example, this would correspond to the idea that

<!-- PageBreak -->

<!-- PageNumber="186" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->


<figure>
<figcaption>FIGURE 11.4. Perspective plot of estimated $\beta$ function truncating the basis for the log precipitations to 7 terms.</figcaption>

4000

$\frac { 8 } { 8 }$

-4000

300

t (7 basis functions used)

200

300

$\begin{array}{} { 1 0 0 } \\ { s \left( 6 4 \right. } \end{array}$ basis functions used)

200

100

</figure>


<figure>
<figcaption>FIGURE 11.5. Original data (solid) and predictions (dashed) of log precipitation relative to annual mean for each of four weather stations. The prediction is carried out using an estimated $\beta$ function with the basis for the log precipitations truncated to 7 terms.</figcaption>

Montreal

Edmonton

Log precipitation

1.0

Log precipitation

1.0

0.0

0.0

-1.0

-1.0

JFMAMJ JASOND

JFMAMJ JASOND

Time of year
(64 and 7 basis functions used)

Time of year
(64 and 7 basis functions used)

Prince Rupert

Resolute

Log precipitation

1.0

Log precipitation

1.0

0.0

0.0

-1.0

-1.0

JFMAMJ JASOND

JFMAMJ JASOND

Time of year
(64 and 7 basis functions used)

Time of year
(64 and 7 basis functions used)

</figure>


<!-- PageBreak -->

<!-- PageNumber="187" -->
<!-- PageHeader="11.4 Regularizing the fit" -->


<figure>
<figcaption>FIGURE 11.6. Perspective plot of estimated $\beta$ function truncating both bases to seven terms.</figcaption>

3

2

beta(s,t)

Z

0

~1

-2

R

300

1 (7 basis functions used)

200

300

s (7 basis functions used)

200

100

100

</figure>


the very fine detail of $\log$ precipitation could not be predicted from
temperature. For the moment, suppose that we do not truncate the $\phi$
basis, but that we allow only $K _ { 0 } = 7$ terms in the expansion of the
$\mathcal{Y} _ { i } ^ { * } ,$ with corresponding adjustments to the matrices $\mathrm { D }$ and $B .$ Figures
11.4 and 11.5 show the resulting $\beta$ functions and sample predictions.
The predictions are smooth, but otherwise very close to the original
data. The function $\beta$ is similar in overall character to the unsmoothed
function shown in Figure 11.1, except that it is smoother as a function
of $t .$ However, it is excessively rough as a function of $s .$ Thus, although
the predictions are aesthetically attractive as smooth functions, they
provide an optimistic assessment of the quality of the prediction, and
an implausible mechanism by which the prediction takes place.


#### 11.4.3 Restricting both bases

Sections 11.4.1 and 11.4.2 illustrated advantages in truncating both the
$\phi$ basis of the predictors and the $\psi$ basis of the responses to obtain
useful and sensible estimates. It should be stressed that the reason
for doing this is not the same in both cases. Truncating the $\phi$ basis
for the covariates is essential to avoid over-fitting, while the $w$ basis is
truncated to ensure that the predictions are smooth.

<!-- PageBreak -->

<!-- PageNumber="188" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->


<figure>
<figcaption>FIGURE 11.7. Contour plot of estimated $\beta$ function truncating both bases to seven terms.</figcaption>

D
2
F
$Z$ CT ZD C C D OO ZO

0

-1

2

2

0

0

$\stackrel { \sim } { = }$ basis functions used)

8

1

0

-1

0

0

-1

0

1

2

J

$F$

$M$

$A$

$M$

J

J

A

S

O

$N$

D

s (7 basis functions used)

</figure>


<figure>
<figcaption>FIGURE 11.8. Original data (solid) and predictions (dashed) of log precipitation relative to annual mean for each of four weather stations. The prediction is carried out using an estimated $\beta$ function with the both bases truncated to seven terms.</figcaption>

Montreal

$\mathrm { E d m o n t o n }$

Log precipitation

1.0

Log precipitation

1.0

0.0

0.0

-1.0

-1.0

JFMAMJ JASON D

JFMAMJ JASOND

Time of year
(7 and 7 basis functions used)

Time of year
(7 and 7 basis functions used)

Prince Rupert

Resolute

Log precipitation

1.0

Log precipitation

1.0

0.0

0.0

-1.0

-1.0

JFMAMJ JASOND

JFMAMJ JASOND

Time of year
(7 and 7 basis functions used)

Time of year
(7 and 7 basis functions used)

</figure>


<!-- PageBreak -->

<!-- PageNumber="189" -->
<!-- PageHeader="11.5 Assessing goodness of fit" -->


<figure>
<figcaption>FIGURE 11.9. Proportion of variance of log precipitation explained by a linear model based on daily temperature records. The prediction is carried out using an estimated $\beta$ function with both bases truncated to seven terms.</figcaption>

1.0

Proportion of variation explained

0.8

0.6

0.4

0.2

0.0

JFMAMJ JASOND

Time of year
(7 and 7 basis functions used)

</figure>


Let us combine these different reasons for truncating the bases,
and truncate both the predictor basis $\phi$ and the response basis
$w .$ Figures 11.6, 11.7 and 11.8 show the effects of truncating both
bases to seven terms. We can discern several aspects of the effect of
temperature on log precipitation. Temperature in February is negatively
associated with precipitation throughout the year. Temperature around
May is positively associated with precipitation in the summer months.
Temperature in September has a strong negative association with
precipitation in the autumn and winter, and finally, temperature in
December associates positively with precipitation throughout the year,
particularly with winter precipitation.


### 11.5 Assessing goodness of fit

There are various ways of assessing the fit of a functional linear
model as estimated in Section 11.4. An approach borrowed from
the conventional linear model is to consider the squared correlation
function

$$R ^ { 2 } \left( t \right) = 1 - \sum _ { i } \left\{ \widehat { y } _ { i } \left( t \right) - y _ { i } \left( t \right) \right\} ^ { 2 } / \sum _ { i } \left\{ y _ { i } \left( t \right) - \bar { y } \left( t \right) \right\} ^ { 2 } .$$

<!-- PageBreak -->

<!-- PageNumber="190" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->


<figure>
<figcaption>FIGURE 11.10. Histogram of individual proportions of variance $R _ { i } ^ { 2 }$ in log precipitation explained by a linear model based on daily temperature records. The prediction is carried out using an estimated $\beta$ function with both bases truncated to seven terms. The left-hand cell of the histogram includes all cases with negative $R _ { i } ^ { 2 }$ values.</figcaption>

12

10

8

6

\+

2

O

0.0

0.2

0.4

0.6

0.8

1.0

Proportions of variation explained

</figure>


If we require a single numerical measure of fit, then the average of $R ^ { 2 }$
over $t$ is useful, but using the entire function $R ^ { 2 }$ offers more detailed
information about the fit. Figure 11.9 plots the $R ^ { 2 }$ function for the fit to
the log precipitation data in Figure 11.6. The fit is generally reasonable,
and is particularly good in the first five months of the year.

$A$ complementary approach to goodness of fit is to consider an
overall $R ^ { 2 }$ measure for each individual functional datum, defined by

$$R _ { i } ^ { 2 } = 1 - \int \left\{ \widehat { \mathcal{Y} } _ { i } \left( t \right) - \mathcal{Y} _ { i } \left( t \right) \right\} ^ { 2 } d t / \int \left\{ y _ { i } \left( t \right) - \bar { \mathcal{Y} } \left( t \right) \right\} ^ { 2 } d t .$$

For the four particular stations plotted in Figure 11.8, for instance,
the values of $R _ { i } ^ { 2 }$ are 0.96, 0.67, 0.63 and 0.81 respectively, illustrating
that Montreal and Resolute are places whose precipitations fit closely
to those predicted by the model on the basis of their observed
temperature profiles; for Edmonton and Prince Rupert the fit is of
course still quite good in that the temperature pattern accounts for
over 60% of the variation of the log precipitation from the overall
population mean. However, Figure 11.8 demonstrates that the pattern
of precipitation, judged by comparing the predictions with the original
data after subtracting the annual mean for the individual places, is

<!-- PageBreak -->

<!-- PageNumber="191" -->
<!-- PageHeader="11.5 Assessing goodness of fit" -->


<figure>
<figcaption>FIGURE 11.11. Comparison, for log precipitation, between mean square prediction errors and mean square variation from overall mean of log precipitation. The prediction is carried out using an estimated $\beta$ function with both bases truncated to seven terms. The points for Montreal, Edmonton, Prince Rupert and Resolute are marked as $M ,$ $\mathrm { E } ,$ $P$ and R respectively. The points marked 0 yield negative $R _ { i } ^ { 2 }$ values. The lines $y = x$ and $y = 0 . 2 5 x$ are drawn on the plot as solid and dotted, respectively.</figcaption>

Residual mean square from prediction

1.0

0.8

P

0.6

Ø

$\mathrm { R }$

0.4

0.2

E

:

0.0

:

M

0

1

2

3

Mean square variation from overall mean

</figure>


predicted only moderately well for Resolute and is not well predicted
for Edmonton. Figure 11.10 displays a histogram of all 35 $R _ { i } ^ { 2 }$ values.
At most of the stations, the $R _ { i } ^ { 2 }$ value indicates reasonable or excellent
prediction, but for a small proportion the precipitation pattern is not at
all well predicted. Indeed, four stations (Dawson, Schefferville, Toronto
and Prince George) have negative $R _ { i } ^ { 2 }$ values, indicating that for these
places the population mean $\bar { \mathcal{Y} }$ actually gives a better fit to $\mathcal{Y} _ { i }$ than does
the predictor $\widehat { \mathcal{Y} } _ { i } .$

To investigate this effect further, we use Figure 11.11 to show a plot
of the residual mean square prediction error $\int \left( \widehat { \mathcal{Y} } _ { i } - \mathcal{Y} _ { i } \right) ^ { 2 }$ against the
mean square variation from the overall mean, $\int \left( y _ { i } - y \right) ^ { 2 } .$ The four
places with negative values of $R _ { i } ^ { 2 }$ are indicated by $0 ^ { \prime } s$ on the plot. Each
of the four places plotted in Figure 11.8 is indicated by the initial letter
of its name. For most places the predictor has about one quarter the
mean square error of the overall population mean, and for many places
the predictor is even better. The four places that yielded a negative
value of $R _ { i } ^ { 2 }$ did so because they were close (in three cases very close)

<!-- PageBreak -->

<!-- PageNumber="192" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->

to the overall population mean, not because the predictor did not work
well for them. To judge accuracy of prediction for an individual place,
it is clear that one needs to look a little further than just at the statistic
$R _ { i } ^ { 2 } .$

It is possible to conceive of an F-ratio function for the fit. Substituting
into equation (11.2), say, we have

$$\widehat { \mathcal{Y} } _ { i } \left( t \right) - \widetilde { \mathcal{Y} } \left( t \right) = \sum _ { j = 1 } ^ { J _ { 0 } } C _ { i j } \left( \sum _ { k = 1 } ^ { K _ { 0 } } B _ { j k } \psi _ { k } \left( t \right) \right) = \sum _ { j = 1 } ^ { J _ { 0 } } C _ { i j } \theta _ { j } \left( t \right) .$$

By analogy with the standard linear model, we can ascribe $K _ { 0 } - 1$ degrees
of freedom to the pointwise sum of squares $\sum _ { i } \left\{ \widehat { \mathcal{Y} } _ { i } \left( t \right) - \bar { \mathcal{Y} } \left( t \right) \right\} ^ { 2 }$ and
$n - K _ { 0 }$ degrees of freedom to the residual sum of squares $\sum _ { i } \left\{ y _ { i } \left( t \right) - \right.$
$\left. \widehat { \mathcal{Y} } _ { i } \left( t \right) \right\} ^ { 2 } .$ An F-ratio plot would be constructed by plotting

$$\mathrm { F R A T I O } \left( t \right) = \frac { \sum _ { i } \left\{ \widehat { \mathcal{Y} } _ { i } \left( t \right) - \bar { \mathcal{Y} } \left( t \right) \right\} ^ { 2 } / \left( K _ { 0 } - 1 \right) } { \sum _ { i } \left\{ \mathcal{Y} _ { i } \left( t \right) - \widehat { \mathcal{Y} } _ { i } \left( t \right) \right\} ^ { 2 } / \left( n - K _ { 0 } \right) } .$$

However, the parameters $\theta _ { j } \left( t \right)$ are not directly chosen to give the best
fit of $\widehat { \mathcal{Y} } _ { i } \left( t \right)$ to the observed $y _ { i } \left( t \right) ,$ and so the classical distribution
theory of the $F$ F-ratio could be used only as an approximation to the
distribution of $\mathrm { F R A T I O } \left( t \right)$ for each $t .$

Figure 11.12 plots the $F$ F-ratio for the fit to the log precipitation
data. The upper 5% and 1% points of the $F _ { 6 : 2 8 }$ distribution are given;
within this model, this indicates that the effect of daily temperature on
precipitation is highly significant overall.

We have not given much attention to the method by which the
truncation parameters $J _ { 0 }$ and $K _ { 0 }$ could be chosen in practice. For
many smoothing and regularization problems, the appropriate method
of choice is probably subjective. The different roles of $J _ { 0 }$ and $K _ { 0 }$
lead to different ways of considering their automatic choice, if one
is desired. The variable $J _ { 0 }$ corresponds to a number of terms in a
regression model, and so we could use a variable selection technique
from conventional regression, possibly adapted to give a functional
rather than a numerical criterion, to indicate a possible value. On the
other hand, $K _ { 0 }$ is more akin to a smoothing parameter in a smoothing
method, and so a method such as cross-validation might be a more
appropriate choice. These questions are interesting topics for future
investigation and research.

<!-- PageBreak -->

<!-- PageNumber="193" -->
<!-- PageHeader="11.6 Bivariate roughness penalties for $\beta$" -->


<figure>
<figcaption>FIGURE 11.12. A plot of the F-ratio function for the prediction of log precipitation from daily temperature data. The prediction is carried out using an estimated $\beta$ function with both bases truncated to seven terms. The horizontal lines show the upper 5% and 1% points of the $F _ { 6 : 2 8 }$ distribution.</figcaption>

25

20

F ratio

15

10

5

0

JF MAM J JASON D

Time of year

</figure>


### 11.6 Bivariate roughness penalties for $\beta$

Just as in other smoothing contexts, an obvious alternative to placing
restrictions on $\beta$ by truncating the basis expansion is to define a
roughness penalty $P E N \left( \beta \right)$ of some kind. We would then minimize
$\mathrm { L M I S E } \left( \beta \right) + \lambda \times \mathrm { P E N } \left( \beta \right) ,$ where $\mathrm { L M I S E } \left( \beta \right) = \mathrm { L M I S E }$ as defined in (11.1),
and $\alpha \left( t \right) = j \left( t \right) - \int \bar { x } \left( s \right) \beta \left( s , t \right) d s$ as in Section 11.1. As usual, $\lambda$ is a
smoothing parameter. The ideas of this section are very much tentative
suggestions for future research, and we provide only a brief discussion
of some possibilities.

A useful roughness penalty can be constructed by finding the integral
of the square of some differential operator acting on $\beta .$ One possibility
is to use a roughness penalty such as the thin plate spline penalty

$$P E N \left( \beta \right) = \int \int \left\{ \left( D _ { s } ^ { 2 } + 2 D _ { s } D _ { t } + D _ { t } ^ { 2 } \right) \beta \left( s , t \right) \right\} ^ { 2 } d s d t$$
(11.8)

discussed in Chapter 7 of Green and Silverman (1994), for example.
This penalty has the property that the only functions with roughness
zero are linear in $s$ and $t .$ It also has the property that the penalty is
isotropic: If the coordinates are rotated, the penalty is unaffected.

<!-- PageBreak -->

<!-- PageNumber="194" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->

We can impose periodic boundary conditions, such as those
appropriate for the Canadian climate example, by restricting attention
to functions whose values and derivatives obey the appropriate
periodic continuity conditions; we then consider the integrals in (11.8)
evaluated on the periodic version of the interval on which $s$ and $t$ lie.
In this case, the only functions with zero roughness are constant.

Because the arguments s and $t$ play different roles, there is no
particular need to use an isotropic roughness penalty such as (11.8).
Another possibility is to use a penalty such as ff $\left\{ \left( D _ { s } + D _ { t } \right) \beta \right\} ^ { 2 } ,$ which
is zero if $\beta$ is $a$ function of $s \quad - \quad t$ alone, corresponding to stationary
dependence of $\mathcal{Y}$ on $x .$

Probably the most straightforward, if not necessarily the most
economical, computational approach is to express any quadratic
roughness penalty as a quadratic form in the elements of $B ,$ where $B$
is the matrix of coefficients of the expansion (11.4) of $\beta$ in terms of
basis functions. The penalized integrated squared residual $\mathrm { L M I S E } \left( \beta \right) +$
$\lambda \times \mathrm { P E N } \left( \beta \right)$ is then itself a quadratic form in $B ,$ and can therefore
be minimized to find the estimate. The practical details, and the
numerical conditioning, depend somewhat on the particular bases
chosen. Another possible approach to the definition of a roughness
penalty is to construct the quadratic function of $B$ directly, and this
would provide a more immediate generalization of the truncated basis
function method.

It is possible to set out a cross-validation approach to the selection
of the smoothing parameter $\lambda ,$ based on repredicting each $\mathcal{Y} _ { i }$ by the
action of the covariate $x _ { i }$ on the function $\beta$ estimated from all the other
data. We obtain the cross-validation score by summing the integrated
squared prediction errors over all $i ,$ as usual. We can use a similar
approach within the basis truncation method in Section 11.4.


### 11.7 Other linear models for functional data

The functional linear models introduced in Chapters 9 and 10 and in
this chapter by no means exhaust the possibilities. In this section we
briefly review a few more that can be interesting in applications.


#### 11.7.1 More complicated covariate structures

In this chapter, we have concentrated for simplicity on the case where
the covariate function (in our example the temperature) is a single real-
valued function. In principle, it is easy to contemplate extending the

<!-- PageBreak -->

<!-- PageNumber="195" -->
<!-- PageHeader="11.7 Other linear models for functional data" -->

ideas to problems where there are vector covariate functions and/or
multivariate covariates. For example, if there were a pair of covariate
functions $\left( x _ { i } , z _ { i } \right)$ and a vector of covariates $\mathrm { w } _ { i }$ for each observed
function $\mathcal{Y} _ { i } ,$ the linear model would become

$$\widehat { \mathcal{Y} } _ { i } \left( t \right) = \alpha \left( t \right) + \int x _ { i } \left( s \right) \beta _ { 1 } \left( s , t \right) d s + \int z _ { i } \left( v \right) \beta _ { 2 } \left( v , t \right) d v + w _ { i } ^ { \prime } \beta _ { 3 } \left( t \right) ,$$

where $\beta _ { 1 }$ and $\beta _ { 2 }$ were suitable bivariate functions and $\beta _ { 3 }$ is a vector
of functions. We can expand the parameter functions $\beta$ in terms of
suitable bases, and basis truncation and roughness penalty ideas are
simply extended. Again, the full details of this approach need to be
worked out in the context of any particular application, and we shall
not discuss it in any detail.


#### 11.7.2 The pointwise multivariate model

An extension of the linear models considered in Chapter 9 is

$$y _ { i } \left( t \right) = \sum _ { j } ^ { q } z _ { i j } \left( t \right) \beta _ { j } \left( t \right) + \epsilon _ { i } \left( t \right) .$$
(11.9)

In vector/matrix form this model may be written

$$y \left( t \right) = Z \left( t \right) \beta \left( t \right) + \epsilon \left( t \right)$$

where the matrix $\mathrm { Z } \left( t \right)$ contains the entries $z _ { i j } \left( t \right) ,$ and the functional
vectors $\mathrm { y } ,$ $\beta$ and $\epsilon$ have the appropriate definitions.

This can be called a pointwise multivariate model, because when the
argument $t$ is fixed, the problem of estimating vector $\beta \left( t \right)$ is the familiar
one of ordinary least squares. The solution becomes

$$\widehat { \beta } \left( t \right) = \left[ Z \left( t \right) ^ { \prime } Z \left( t \right) \right] ^ { - 1 } Z \left( t \right) ^ { \prime } y \left( t \right) .$$
(11.10)

In practice we would evaluate $\widehat { \beta }$ only at a finite number of points $t ,$
and some form of interpolation would be used between these points. It
may also be desirable to regularize the estimate $\widehat { \beta }$ either by expanding
it in terms of a finite number of basis functions, or by attaching an
appropriate roughness penalty. These matters are taken up in Chapters
13 and 14, where this model is used to estimate the nonconstant weight
functions defining a linear differential operator.


#### 11.7.3 Spline smoothing and other evaluation models

In Section 10.5.2 we discussed some connections between the spline
smoothing technique described in Chapter 3 and functional linear

<!-- PageBreak -->

<!-- PageNumber="196" -->
<!-- PageHeader="11. Functional linear models for functional responses" -->

modelling. In fact, the spline smoothing model can be put directly into a
functional linear modelling context, by somewhat extending the models
dealt with in Chapter 10.

Let the dependent variable be a vector $\mathcal{Y} = \left( \mathcal{Y} _ { 1 } , \ldots , \mathcal{Y} _ { N } \right) ^ { \prime }$ of $N$ real
numbers, and let the model be

$$y _ { i } = \beta \left( t _ { i } \right) + \epsilon _ { i } .$$
(11.11)

Define the linear mapping

$$z _ { i } \left( \beta \right) = \beta \left( t _ { i } \right)$$

to transform any function $\beta$ to its value at $t _ { i } .$ In general, denote by $\delta _ { t }$
the evaluation functional that maps $a$ function $\beta$ to its value at $t ,$ or

$$\delta _ { t } \left( \beta \right) = \beta \left( t \right) .$$

If we use Dirac delta function notation then we can write $\delta _ { t } \left( \beta \right)$ in
inner product notation as $\langle \delta _ { t } , \beta \rangle .$ One way of considering this notation
is to think of the functional $\delta _ { t }$ as a delta-function centred at $t$ t. The
other is simply to regard the inner product notation as a way of writing
the effect of the functional $\delta _ { t }$ on the function $\beta .$

Either way, $z _ { i } = \delta _ { t _ { i } } ,$ so that the model (11.11) can be written as

$$y _ { i } = \langle z _ { i } , \beta \rangle + \epsilon _ { i } .$$
(11.12)

Compare this with the model given in equation (10.3); with the
exception of the constant term $\alpha$ the model is identical. By allowing
more general functionals than inner products with 'nice' functions $x _ { i } ,$
we have managed to put spline smoothing into a much more general
functional linear modelling framework.

Evaluation models are by no means restricted to simply evaluating
the function at sampling values for the argument. We may also consider

$$y _ { i } = D ^ { m } \beta \left( t _ { i } \right) + \epsilon _ { i }$$
(11.13)

where the model is the value of the derivative of order $m .$ Even more
generally, we might use

$$\mathcal{Y} _ { i } = w _ { 0 } \left( t _ { i } \right) \beta \left( t _ { i } \right) + w _ { 1 } \left( t _ { i } \right) D \beta \left( t _ { i } \right) + \ldots + D ^ { m } \beta \left( t _ { i } \right) + \epsilon _ { i }$$
$$= L \beta \left( t _ { i } \right) + \epsilon _ { i } .$$

Here $L$ is a linear differential operator of order $m$ defined by

$$L = w _ { 0 } I + w _ { 1 } D + \ldots + D ^ { m } = \sum _ { j = 0 } ^ { m } w _ { j } D ^ { j } ,$$
(11.14)

where the $w _ { j }$ are continuous weight functions and $I \beta = D ^ { 0 } \beta = \beta .$ If we
then define linear operators $z _ { i }$ to satisfy $\langle z _ { i } , \beta \rangle = L \beta \left( t _ { i } \right) ,$ we have the
model (11.12) again.

<!-- PageBreak -->

<!-- PageNumber="197" -->
<!-- PageHeader="11.7 Other linear models for functional data" -->


#### 11.7.4 Weighted and partial integral models

$A$ rather general functional linear model is given by

$$\widehat { \mathcal{Y} } _ { i } \left( t \right) = \int \omega _ { i } \left( s , t \right) z _ { i } \left( s \right) \beta \left( s , t \right) d s = \langle z _ { i } , \beta \left( \cdot , t \right) \rangle _ { w _ { i } \left( \cdot , t \right) }$$
(11.15)

where $w _ { i }$ is a known weight function, and where the notation $\langle \cdot , \cdot \rangle _ { w \left( \cdot , t \right) }$
means taking the inner product using the weight function $w \left( \cdot , t \right) .$

This setup includes the special case of the partial integral model

$$\widehat { \mathcal{Y} } _ { i } \left( t \right) = \int _ { 0 } ^ { t } z _ { i } \left( s \right) \beta \left( s , t \right) d s$$
(11.16)

for which

$$w \left( s , t \right) = \left\{ \begin{array}{} { 1 , } & { s \leq t } \\ { 0 , } & { s > t } \end{array} \right.$$
(11.17)

The partial integral model, for example, might be reasonable when we
know that the influence of independent variable function $z _ { i }$ extends
only backwards in time, as would be the case for nonperiodic processes.

In general, when the weight functions $w$ vary over argument $t ,$
the linear model must be solved pointwise, as is the case for the
pointwise multivariate model given above. Again, regularization and
basis expansion techniques can be brought into play to ensure that $\widehat { \beta }$
is sufficiently smooth and that the estimation problem is manageable.

<!-- PageBreak -->

<!-- PageNumber="12" -->


## Canonical correlation and discriminant analysis


### 12.1 Introduction


#### 12.1.1 The basic problem

Suppose we have observed pairs of functions $\left( X _ { i } , Y _ { i } \right) ,$ $i = 1 , \ldots , N ,$
such as the hip and knee angles for the gait cycles of a number of
children, as discussed in Section 6.5. We saw there how we can use
principal components analysis to examine the variability in the two
sets of curves taken together. In this chapter, we pursue a somewhat
different emphasis by considering canonical correlation analysis (CCA),
which seeks to investigate which modes of variability in the two sets of
curves are most associated with one another. Thus in the gait analysis
example, we might ask how variability in the knee angle cycle is related
to that in the hip angle.

First we review classical multivariate CCA; a fuller discussion can
be found in most multivariate analysis textbooks, such as Anderson
(1984). Then we go on to develop an approach to functional CCA, largely
based on the paper of Leurgans, Moyeed and Silverman (1993). The
application of the method to two sets of data is presented in Sections
12.3 and 12.4. There we see that some regularization is essential to
obtain meaningful results, for reasons discussed briefly in Section 12.5.
In Section 12.6, various algorithmic approaches and connections with
other FDA topics are explored.

<!-- PageBreak -->

<!-- PageNumber="200" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

Finally, in Section 12.7, we present some extensions of the ideas
of functional CCA to deal with problems of optimal scoring and
discriminant analysis. This is based on work of Hastie, Buja and
Tibshirani (1995).


#### 12.1.2 Principles of classical canonical correlation analysis

Suppose we have $n$ pairs of observed vectors $\left( x _ { i } , y _ { i } \right) ,$ each $x _ { i }$ being
a p-vector and each $\mathcal{Y} _ { i }$ being a q-vector. Write $\mathrm { V } _ { 1 1 }$ for the sample
variance matrix of the $x _ { i } ,$ and $V _ { 2 2 }$ for that of the $\mathcal{Y} _ { i } .$ Let $V _ { 1 2 }$ be the
$p \times q$ covariance matrix between the $x _ { i }$ and the $y _ { i } ,$ so that

$$V _ { 1 2 } = \frac { 1 } { n - 1 } \sum _ { i = 1 } ^ { n } \left( x _ { i } - x \right) \left( y _ { i } - y \right) ^ { \prime }$$
(12.1)

and let $V _ { 2 1 } = V _ { 1 2 } ^ { \prime } .$

The object of canonical correlation analysis is to reduce the
dimensionality of the data by finding the vectors $a$ and $b$ $\left( p - \right.$ and $q -$
vectors respectively) for which the linear combinations $a ^ { \prime } x _ { i }$ and $b ^ { \prime } y _ { i }$
are as highly correlated as possible. The canonical variates $a ^ { \prime } x _ { i }$ and
$b ^ { \prime } y _ { i }$ are the linear compounds of the original observations whose
variability is most closely related in terms of correlation. The vectors
$a$ and $b$ are called the canonical variate weight vectors.

Note that multiplying $a$ and/or $b$ by nonzero constants of the same
sign does not alter the correlation. If the constants are opposite in sign,
the correlation itself is reversed in sign but has the same magnitude. By
convention, we choose $a$ and $b ,$ implying that $\left\{ a ^ { \prime } x _ { i } \right\}$ and $\left\{ b ^ { \prime } y _ { i } \right\}$ both
have sample variance equal to 1, and the correlation $\rho$ between the $a ^ { \prime } x _ { i }$
and $b ^ { \prime } y _ { i }$ is positive.


#### 12.1.3 Expressing the analysis as an eigenvalue problem

How can we find a and $b ?$ The sample variances of $\left\{ a ^ { \prime } x _ { i } \right\}$ and $\left\{ b ^ { \prime } y _ { i } \right\}$ are
$a ^ { \prime } V _ { 1 1 } a$ and $b ^ { \prime } V _ { 2 2 } b$ respectively, and the sample covariance of the pairs
$\left( a ^ { \prime } x _ { i } , b ^ { \prime } y _ { i } \right)$ is $a ^ { \prime } V _ { 1 2 } b .$ Thus we find the canonical variates by solving
the optimization problem

$$\max a ^ { \prime } \mathrm { V } _ { 1 2 } b \text { subject to } a ^ { \prime } \mathrm { V } _ { 1 1 } a = b ^ { \prime } \mathrm { V } _ { 2 2 } b = 1 .$$
(12.2)

In Section 12.1.5 we show that this optimization problem can be
solved by computing the leading eigenvalue $\rho$ and corresponding

<!-- PageBreak -->

<!-- PageNumber="201" -->
<!-- PageHeader="12.1 Introduction" -->

eigenvector
$\left[ \begin{array}{} { a } \\ { b } \end{array} \right.$
of the generalized eigenvalue problem

$$\left[ \begin{array}{} { 0 } & { V _ { 1 2 } } \\ { V _ { 2 1 } } & { 0 } \end{array} \right] \left[ \begin{array}{} { a } \\ { b } \end{array} \right] = \rho \left[ \begin{array}{} { V _ { 1 1 } } & { 0 } \\ { 0 } & { V _ { 2 2 } } \end{array} \right] \left[ \begin{array}{} { a } \\ { b } \end{array} \right]$$
(12.3)

The resulting value of $\rho$ is the correlation between the variates $a ^ { \prime } x _ { i }$ and
$b ^ { \prime } y _ { i } .$ Note that the eigenvalues of (12.3) occur in pairs, because if
$\left[ \begin{array}{} { a } \\ { b } \end{array} \right.$

is an eigenvector with eigenvalue $\rho ,$ then
$\left[ \begin{array}{} { a } \\ { - b } \end{array} \right.$
is an eigenvector with
eigenvalue $- \rho .$


##### 12.1.4 Subsidiary variates and their properties

We can go on to solve equation (12.3) completely and find the $r =$
$\mathrm { r a n k } \left( \mathrm { V } _ { 1 2 } \right) \leq \min \left( p , q \right)$ strictly positive eigenvalues $\rho _ { 1 } \geq \ldots \geq$
$\rho _ { r }$ with corresponding eigenvectors $\left( a _ { 1 } , b _ { 1 } \right) , \ldots , \left( a _ { r } , b _ { r } \right) .$ The $\rho _ { j }$ are
called the canonical correlations of the model. The pairs $\left( a _ { j } , b _ { j } \right)$ are
the corresponding canonical variate weight vectors; the quantities
$\left( a _ { j } ^ { \prime } x _ { i } , b _ { j } ^ { \prime } y _ { i } \right)$ are the pairs of canonical variates, each having sample
correlation $\rho _ { j } .$ The canonical variates with the largest correlation $\rho _ { 1 } ,$ as
considered in Section 12.1.2, are called the leading canonical variates
if any confusion is possible.

Arguments from linear algebra found in most multivariate textbooks
show that if $j \neq k$ then both of the jth variates are uncorrelated with
both of the $k$ kth variates. This means that the canonical variates have
the following properties for $j \neq k ,$ where in each case the correlations
are the sample correlations as i takes the values $1 , \ldots , n :$

(a) $\mathrm { c o r r } \left( a _ { j } ^ { \prime } x _ { i } , a _ { k } ^ { \prime } x _ { i } \right) = a _ { j } ^ { \prime } V _ { 1 1 } a _ { k } = 0$

(b) $\mathrm { c o r r } \left( b _ { j } ^ { \prime } y _ { i } , b _ { k } ^ { \prime } y _ { i } \right) = b _ { j } ^ { \prime } v _ { 2 2 } b _ { k } = 0$

(c) $\mathrm { c o r r } \left( a _ { j } ^ { \prime } x _ { i } , b _ { k } ^ { \prime } y _ { i } \right) = a _ { j } ^ { \prime } V _ { 1 2 } b _ { k } = 0$

In fact, the canonical variates can be characterized successively by
maximizing $\mathrm { c o r r } \left( a _ { j } ^ { \prime } x _ { i } , b _ { j } ^ { \prime } y _ { i } \right)$ subject to the constraints that $a _ { j } ^ { \prime } V _ { 1 1 } a _ { k } =$
0 and $b _ { j } ^ { \prime } V _ { 2 2 } b _ { k } = 0$ for $k < j .$


##### 12.1.5 CCA and the generalized eigenproblem

In this section, we give a brief justification of the assertion that the
solutions of the generalized eigenequation (12.3) yields the solution of

<!-- PageBreak -->

<!-- PageNumber="202" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

the constrained optimization problem (12.4). Readers who are prepared
to take this on trust should skip straight to Section 12.2, where we begin
our discussion of the functional case.

Consider the problem obtained by weakening the constraint in (12.2)
to one on the sum of variances:

$$a ^ { \prime } V _ { 1 2 } b \text { subject to } a ^ { \prime } V _ { 1 1 } a + b ^ { \prime } V _ { 2 2 } b = 2 .$$
(12.4)

This may be written in block matrix form as

$$\max _ { a , b } \left\{ \left[ a ^ { \prime } b ^ { \prime } \right] \left[ \begin{array}{} { 0 } & { \mathrm { V } _ { 1 2 } } \\ { \mathrm { V } _ { 2 1 } } & { 0 } \end{array} \right] \left[ \begin{array}{} { a } \\ { b } \end{array} \right] \right\} \text { subject to }$$
$$\left[ \begin{array}{} { a ^ { \prime } b ^ { \prime } } \end{array} \right] \left[ \begin{array}{} { V _ { 1 1 } } & { 0 } \\ { 0 } & { V _ { 2 2 } } \end{array} \right] \left[ \begin{array}{} { a } \\ { b } \end{array} \right] = 2$$

(12.5)

By standard optimization arguments, the optimum is obtained by
solving the generalized eigenvalue problem (12.3), choosing $\rho$ to be
the largest eigenvalue, and then scaling
$\left[ \begin{array}{} { a } \\ { b } \end{array} \right.$
to satisfy the constraint

(12.5).
Now suppose
$$\left[ \begin{array}{} { a } \\ { b } \end{array} \right] \text { satisfies } \left( 1 2 . 3 \right) . \text { Then } V _ { 1 2 } b = \rho V _ { 1 1 } a , V _ { 2 1 } a =$$

$\rho \mathrm { V } _ { 2 2 } b$ and

$$\rho a ^ { \prime } V _ { 1 1 } a = a V _ { 1 2 } b = b ^ { \prime } V _ { 2 1 } a = \rho b ^ { \prime } V _ { 2 2 } b .$$
(12.6)

From (12.6) it follows that
$\left[ \begin{array}{} { a } \\ { b } \end{array} \right]$
satisfies the stronger constraint
$a ^ { \prime } V _ { 1 1 } a = b ^ { \prime } V _ { 2 2 } b = 1 ,$ and hence
$\begin{array}{} { a } \\ { b } \end{array}$
1
solves the original optimization
problem (12.2) as well as the weaker problem (12.4).

Two other useful properties follow from (12.6). Firstly, the variates
$a ^ { \prime } x _ { i }$ and $b ^ { \prime } y _ { i }$ have correlation $\rho ,$ as stated in Section 12.1.3. Secondly,
$a ^ { \prime } V _ { 1 1 } a = b ^ { \prime } V _ { 2 2 } b ,$ so whatever scaling is necessary to make the $a ^ { \prime } x _ { i }$
have variance one, the same scaling achieves this effect for the $b ^ { \prime } y _ { i } .$


### 12.2 Functional canonical correlation analysis


#### 12.2.1 Notation and assumptions

We now return to the functional case, which is our main concern.
As usual, assume that the $N$ observed pairs of data curves $\left( X _ { i } , Y _ { i } \right)$
are available for argument $t$ in some finite interval $T ,$ and that all
integrals are taken over $T .$ Assume that the population mean curves

<!-- PageBreak -->

<!-- PageNumber="203" -->
<!-- PageHeader="12.2 Functional canonical correlation analysis" -->

have been estimated and subtracted from the observed data curves, so
that sample variance and covariance functions are given as

$$v _ { 1 1 } \left( s , t \right) = N ^ { - 1 } \sum X _ { i } \left( s \right) X _ { i } \left( t \right) ,$$
$$v _ { 2 2 } \left( s , t \right) = N ^ { - 1 } \sum Y _ { i } \left( s \right) Y _ { i } \left( t \right) ,$$
and

$$v _ { 1 2 } \left( s , t \right) = N ^ { - 1 } \sum X _ { i } \left( s \right) Y _ { j } \left( t \right) .$$

As in Chapter 6 we define corresponding operators $V _ { 1 1 } ,$ $V _ { 2 2 }$ and $V _ { 1 2 } ,$
by writing $V _ { 1 1 } f$ for the function

$$V _ { 1 1 } f \left( s \right) = \int _ { T } v _ { 1 1 } \left( s , t \right) f \left( t \right) d t ,$$

and correspondingly for $V _ { 1 2 } ,$ $V _ { 2 2 } .$ Given functions $5$ and $\eta ,$ we define
$\mathrm { c c o r s q } \left( 5 , \eta \right)$ to be the sample squared correlation of $\langle E , X _ { i } \rangle$ and $\langle \eta , Y _ { i } \rangle ,$
and therefore

$$\mathrm { c c o r s q } \left( 5 , \eta \right) = \frac { \langle E , V _ { 1 2 } \eta \rangle ^ { 2 } } { \langle E , V _ { 1 1 } S \rangle \langle \eta , V _ { 2 2 } \eta \rangle } .$$

The use of a roughness penalty is central to our methodology.
As usual we quantify roughness by integrated squared curvature,
imposing periodic boundary conditions if appropriate. For functions $f$
and $g$ satisfying appropriate boundary conditions, we use the property

$$\langle D ^ { 2 } f , D ^ { 2 } g \rangle = \langle f , D ^ { 4 } g \rangle ,$$

derived in Section 7.2, and the consequential result that the integrated
squared curvature $\| D ^ { 2 } f \| ^ { 2 }$ can be written $\left( f , D ^ { 4 } f \right) .$


#### 12.2.2 Estimating the leading canonical variates

For the moment concentrate on the leading canonical variates. We
might imagine that the obvious way to proceed is simply to find
functions $5$ and $\eta$ that maximize $\mathrm { c c o r s q } \left( 5 , \eta \right) .$ This would be
equivalent to maximizing $\langle 5 , V _ { 1 2 } \eta \rangle$ subject to the constraints

$$\langle 5 , V _ { 1 1 } S \rangle = \langle \eta , V _ { 2 2 } \eta \rangle = 1 .$$
(12.7)

Both by considering an example and by referring to theoretical results,
we shall see later that such an approach breaks down and that
maximizing $\mathrm { c c o r s q } \left( 5 , \eta \right)$ does not give any meaningful information
about the data or the model. Instead, we must introduce some
appropriate smoothing.

A straightforward way of introducing smoothing is to modify the
constraints (12.7) by adding roughness penalty terms to give

$$\langle E , V _ { 1 1 } F \rangle + \lambda _ { 1 } \| D ^ { 2 } E \| ^ { 2 } = \langle \eta , V _ { 2 2 } \eta \rangle + \lambda _ { 2 } \| D ^ { 2 } \eta \| ^ { 2 } = 1$$

<!-- PageBreak -->

<!-- PageNumber="204" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

or, equivalently,

$$\langle E , \left( V _ { 1 1 } + \lambda _ { 1 } D ^ { 4 } \right) E \rangle = \langle \eta , \left( V _ { 2 2 } + \lambda _ { 2 } D ^ { 4 } \right) \eta \rangle = 1 ,$$
(12.8)

where $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are positive smoothing parameters.

The effect of introducing the roughness penalty terms into the
constraints is that, in evaluating particular candidates to be canonical
variates, we consider not only their variances, but also their roughness,
and compare a weighted sum of these two quantities with the
covariance term. The problem of maximizing the covariance $\langle 5 , V _ { 1 2 } \eta \rangle$
subject to the constraints (12.8) is equivalent to maximizing the
penalized squared sample correlation defined by

$$\mathrm { c c o r s q } _ { \left( \lambda _ { 1 } , \lambda _ { 2 } \right) } \left( \xi , \eta \right) = \frac { \langle \xi , V _ { 1 2 } \eta \rangle ^ { 2 } } { \left( \langle \xi , V _ { 1 1 } \xi \rangle + \lambda _ { 1 } \| D ^ { 2 } \xi \| ^ { 2 } \right) \left( \langle \eta , V _ { 2 2 } \eta \rangle + \lambda _ { 2 } \| D ^ { 2 } \eta \| ^ { 2 } \right) } .$$
(12.9)

We refer to this procedure as smoothed canonical correlation analysis.

The larger the values of $\lambda _ { 1 }$ and $\lambda _ { 2 } ,$ the more emphasis is placed on
the roughness penalty and the smaller will be the true correlation of
the variates found by smoothed CCA. A good choice of the smoothing
parameters is essential to give a pair of canonical variates with fairly
smooth weight functions and a correlation that is not unreasonably
low.

By an argument analogous to that set out for the multivariate case in
Section 12.1.3, the functions $\left( 5 , \eta \right)$ that maximize equation (12.9) are
the eigenfunctions corresponding to the largest positive eigenvalue $\rho$
of the system of operator equations

$$\left( \begin{array}{} { 0 } & { V _ { 1 2 } } \\ { V _ { 2 1 } } & { 0 } \end{array} \right) \left( \begin{array}{} { 5 } \\ { \eta } \end{array} \right) = \rho \left( \begin{array}{} V _ { 1 1 } + \lambda _ { 1 } D ^ { 4 } & 0 \\ 0 & V _ { 2 2 } + \lambda _ { 2 } D ^ { 4 } \end{array} \right) \left( \begin{array}{} \xi \\ \eta \end{array} \right) .$$
(12.10)

Some details of practical ways for dealing with this equation are given
in Section 12.6.

Generally, we have found it sufficient to consider the special case
where $\lambda _ { 1 } = \lambda _ { 2 } = \lambda ,$ and for the practical discussion of functional CCA
in the next two sections we confine attention to this case, using the
single subscript $\lambda$ where necessary. The extension to the more general
case is straightforward.

Our method of introducing smoothing or regularization is similar
to the technique of ridge regression, which is often used in image
processing and ill-posed problems to improve the conditioning of
covariance matrices corresponding to $V _ { 1 1 }$ and $V _ { 2 2 } .$ The technique of
ridge regression was applied to CCA by Vinod (1976).

<!-- PageBreak -->

<!-- PageNumber="205" -->
<!-- PageHeader="12.3 Application to the gait data" -->


#### 12.2.3 Cross-validation and subsidiary variates

The smoothing parameter $\lambda$ in the procedure set out can be chosen
subjectively. If we require an automatic procedure, a reasonable form
of cross-validation is as follows:

Let $\mathrm { c c o r s q } _ { \lambda } ^ { - i } \left( E , \eta \right)$ be the sample penalized squared correlation
calculated as in (12.9) but with the observation $\left( X _ { i } , Y _ { i } \right)$ omitted. Let
$\left( 5 _ { \lambda } ^ { \left( - i \right) } , \eta _ { \lambda } ^ { \left( - i \right) } \right)$ be the functions that maximize $\mathrm { c c o r s q } _ { \lambda } ^ { - i } \left( F , \eta \right) .$ The cross-
validation score for $\lambda$ is defined to be the squared correlation of the $N$
pairs of numbers

$$\left( \langle \xi _ { \lambda } ^ { \left( - i \right) } , X _ { i } \rangle , \langle \eta _ { \lambda } ^ { \left( - i \right) } , Y _ { i } \rangle \right)$$

for $i = 1 , \ldots , n .$ We then choose the value of $\lambda$ that maximizes this
correlation.

Throughout this section, we have concentrated on estimating
the leading canonical variates. Of course, the subsequent positive
eigenvalues and corresponding eigenfunctions of system (12.10) give
the subsidiary canonical correlations and their canonical variates.
These are orthogonal with respect to the penalized sample covariance
operators $V _ { 1 1 } + \lambda D ^ { 4 }$ and $V _ { 2 2 } + \lambda D ^ { 4 } ,$ rather than the raw sample
covariance operators as in the classical case. If we were particularly
interested in the ideal smoothing parameter for a subsidiary canonical
correlation, we could formulate a relevant cross-validation score.
However, our practical experience has shown us that, although cross-
validation works well for the leading canonical variate, its behaviour is
much more disappointing for subsequent canonical variates.


#### 12.3 Application to the gait data

We can now apply the canonical correlation analysis approach to the
gait data as discussed in Chapters 1 and 6, considering both the hip
and the knee angles.

Figure 12.1 shows functions $5$ and $\eta$ that maximize the unsmoothed
sample correlation ccorsq. The sample correlation achieved by these
functions is 1. The functions displayed in Figure 12.1 do not give any
meaningful information about the data and clearly demonstrate the
need for a technique involving smoothing. In Section 12.5, we explain
why this behaviour is not specific to this particular data set but is an
intrinsic property of CCA applied in the functional context.

In Figure 12.2, we see the leading smoothed canonical variates
$\xi _ { \lambda }$ and $\eta _ { \lambda }$ with the smoothing parameter $\lambda$ chosen by the cross-
validation method described in Section 12.2.3. Since the main interest

<!-- PageBreak -->

<!-- PageNumber="206" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->


<figure>
<figcaption>FIGURE 12.1. Unsmoothed canonical variate weight functions for the gait data that attain perfect correlation. Top panel: weight function for hip observations; bottom panel: weight function for knee observations.</figcaption>

~

Hip weight function

Why

\-

0

V

0.0

0.2

0.4

0.6

0.8

1.0

2

Knee weight function

MMMMM

\-

0

47

y

0.0

0.2

0.4

0.6

0.8

1.0

Time (proportion of gait cycle)

</figure>


<figure>
<figcaption>FIGURE 12.2. First pair of smoothed canonical variate weight functions for the gait data. Solid curve: weight function for hip observations; dotted curve: weight function for knee observations.</figcaption>

2

Value of weight function

L

0

L-

y

0.0

0.2

0.4

0.6

0.8

1.0

Time relative to cycle length

</figure>


<!-- PageBreak -->

<!-- PageNumber="207" -->
<!-- PageHeader="12.3 Application to the gait data" -->


<table>
<caption>TABLE 12.1. Smoothed and unsmoothed sample correlations for the first three pairs of smoothed canonical variates for the gait data.</caption>
<tr>
<th>Canonical variates</th>
<th colspan="2">Sample squared correlations $\mathrm { c c o r s q } _ { \lambda } \left( \mathrm { F a } , \eta _ { \lambda } \right)$ $\mathrm { c c o r s q } \left( F _ { \lambda } , \eta _ { \lambda } \right)$</th>
</tr>
<tr>
<td>First</td>
<td>0.755</td>
<td>0.810</td>
</tr>
<tr>
<td>Second</td>
<td>0.618</td>
<td>0.717</td>
</tr>
<tr>
<td>Third</td>
<td>0.141</td>
<td>0.198</td>
</tr>
</table>


<figure>
<figcaption>FIGURE 12.3. Second pair of smoothed canonical variate weight functions for the gait data. Solid curve: weight function for hip observations; dashed curve: weight function for knee observations.</figcaption>

2

Value of weight function

1

0

T

֏

0.0

0.2

0.4

0.6

0.8

1.0

Time relative to cycle length

</figure>


is in comparing the curves, they have been normalized to set the
integral of their squares equal to 1. Table 12.1 shows the values
of the smoothed and unsmoothed squared correlations, and also
includes corresponding values for the second and third pairs of
smoothed canonical variates, estimated with the same $\lambda .$ The broad
interpretation of these variates is that there is correlation between the
two measurements at any particular time. But it is interesting that the
extreme in the hip curve in the middle of the cycle occurs a little later
than that in the knee curve, whereas the order of the extremes near
the beginning of the cycle is reversed. This suggests that, in the middle
of the cycle, high variability from the norm in the hip follows that in
the knee; near the ends of the cycle, the effects occur in the opposite

<!-- PageBreak -->

<!-- PageNumber="208" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

order. This may indicate a physical propagation of errors caused by
the relevant strike of the heel at the beginning and in the middle of the
cycle.

Table 12.1 shows that the second pair of canonical variates is almost
as important as the first, and these are displayed in Figure 12.3, with
the same normalization as in Figure 12.2. The points at which the
second canonical variates cross the axis indicate conclusions similar to
those outlined with respect to the leading variates. In the middle of the
cycle the hip curve crosses zero considerably later than the knee curve,
whereas near the beginning of the cycle the hip curve crosses first. Put
another way, we could roughly transform both the first and the second
canonical variates to be identical for the hip and the knee by speeding
up the hip cycle relative to the knee cycle in the first half of the cycle,
and slowing it down in the second. The degree of smoothing chosen by
cross-validation appears to be quite heavy, and to test the sensitivity of
these conclusions, Leurgans, Moyeed and Silverman (1993) examined
the first two pairs of canonical variates estimated with a value of $\lambda$
reduced by a factor of 10. Though there was a little more variability in
the canonical variate curves, the broad features remained the same.

Table 12.1 shows that the values of the estimated correlations of the
third pair of canonical variates are small, and for our purposes can
be ignored. Scatterplots of the canonical variate scores $\left. \left( \langle l _ { 5 } ^ { \left( \right. } , X _ { i } \right) , \langle \eta , Y _ { i } \rangle \right)$
show that no particular curves have outlying scores for either of the
first two canonical variates.

In Section 6.5, we saw that the first principal component of variation
in the hip curves alone corresponded to an overall vertical shift in
the curves. If this shift were in any way correlated with a variation in
the knee curves, the hip canonical variate curves would be more like
constants than sine waves. Since this is not the case, we can see that
this vertical shift is a property of the hip curves alone, independent of
any variation in the knee angles.


#### 12.4 Application to the study of lupus nephritis

Buckheit, Olshen, Blouch and Myers (1997) applied functional CCA to
renal physiology, in the study of diffuse proliferative lupus nephritis,
and we present their results here as an illustration. The original paper
should be consulted for further details; we are extremely grateful to
Richard Olshen for his generosity in sharing and discussing this work
with us prior to its publication.

<!-- PageBreak -->

<!-- PageNumber="209" -->
<!-- PageHeader="12.4 Application to the study of lupus nephritis" -->


<figure>
<figcaption>FIGURE 12.4. Smoothed canonical variate weight functions for the lupus data, from Buckheit et al. (1997). Left panel: results of CCA applied to GFR and KUC with solid curve corresponding to GFR and dashed curve to KUC. Left panel: results of CCA applied to GFR and GOP with solid curve corresponding to GFR and dashed curve to GOP.</figcaption>

0.4

1

0.35

0.8

0.6

0.3

0.4

Standardized units

Standardized units

0.25

0.2

0.2

0

-0.2

0.15

-0.4

0.1

-0.6

0.05

0

20

40

60

-0.8

0

20

40

60

Months

Months

</figure>


They had available various measurements on a number of patients
over a 60 month period. These include the glomerular filtration
rate (GFR), the glomerular oncotic pressure (GOP) and the two-kidney
ultrafiltration coefficient (KUC). They focused on nine patients labelled
progressors, those whose kidney function, as measured by GFR was
clearly declining over the period of study. The GFR measure is currently
favoured by clinicians as an overall indicator of progressive glomerular
disease, a particular form of kidney degeneration, and therefore the
progressors are the group suffering long-term kidney damage, likely
to require eventual dialysis or transplantation. It is important to
understand the kidney filtration dynamics in this disease, and this is
facilitated by investigating the covariation between measured variables.

Within the progressor group, GFR and KUC tend to decrease
considerably over the 60 month period, whereas the GOP measure
increases somewhat. This contrasts with well-functioning kidneys,
where an increase in GOP would be counteracted by an increase in
KUC resulting in steady GFR. Functional smoothed CCA was applied to
explore variability and interaction effects in the progressor group. The
correlations between GFR and each of KUC and GOP were investigated.

<!-- PageBreak -->

<!-- PageNumber="210" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

Figure 12.4 shows the leading pairs of canonical variate weight
functions. It is interesting that the linear functional of GFR most highly
correlated with the other two variables is virtually the same in both
cases.

To interpret the figure, remember that all patients concerned show
an overall declining value of GFR. The U-shaped solid curves in the
figure therefore correspond to a canonical variate where a positive
value indicates a GFR record that starts at a value higher than average,
but then declines more rapidly than average in the first 40 months,
finally switching to a relatively less rapid decline in the last 20 months.

The left hand panel shows that this variate is correlated with a similar
effect for KUC, but the switch in rate happens earlier. This indicates not
only that strong decline of GFR is associated with strong decline of KUC
but also suggests that the pattern of GFR in some sense follows that
of KUC, raising the hope that KUC could be used to predict future GFR
behaviour. On the other hand, the right hand panel shows that this
aspect of GFR behaviour is correlated with an increase of GOP stronger
than average over the entire time period. Thus, patients with rapidly
increasing GOP are likely to be those whose GFR declines rapidly at first,
though there may be some reduction in the rate of decline after about
36 months.

In broad terms, the CCA gives insights broadly consistent with
those for the average behaviour of the sample as a whole. It is
interesting that the relationships between the variables are borne out
on an individual level, not merely on an average level. Furthermore
the detailed conclusions yielded by the CCA give important avenues
for future thought and investigation concerning the way in which
the variables interrelate. Of course, given the small sample size, any
conclusions must be relatively tentative unless supported by other
evidence.


### 12.5 Why is regularization necessary?

Apart from its importance as a practical method, canonical correlation
analysis of functional data has an interesting philosophical aspect. In
the principal components analysis context we have already seen that
appropriately applied smoothing may improve the estimation accuracy.
However, in most circumstances, we obtain reasonable estimates of the
population principal components even if no smoothing is applied. By
contrast, as we saw in the gait example, in the context of functional
CCA some regularization is absolutely essential to obtain meaningful

<!-- PageBreak -->

<!-- PageNumber="211" -->
<!-- PageHeader="12.6 Algorithmic considerations" -->

results. This is the same conclusion that we drew for the functional
regression context discussed in Chapter 10. But in the canonical
correlation case, the impact of smoothing is even more dramatic.

To understand the need for regularization, compare functional CCA
with standard multivariate CCA. A standard condition of classical CCA
is that $n > p + q + 1$ which ensures (with probability 1, under reasonable
conditions) that the sample covariance matrix $\mathrm { V } _ { 1 2 }$ of the $n$ vectors
$\left( x _ { i } , y _ { i } \right)$ is nonsingular (see Eaton and Perlman,1973). In the functional
case, $p$ and $q$ are essentially infinite, and so this condition cannot be
fulfilled.

Furthermore, consider a sample $X _ { 1 } , \ldots , X _ { N }$ of functional data, and
assume for the moment that the $N$ curves are linearly independent.
Now suppose that $z _ { 1 } , \ldots , z _ { N }$ is any real vector. By the results of Chapter
10, there is a functional interpolant $E$ such that, for some constant $\alpha _ { X } ,$
$z _ { i } = \alpha _ { X } + \langle E , X _ { i } \rangle$ for all $i .$ Now suppose we have a second sample of
curves $Y _ { i } ,$ which may be correlated with the $X _ { i }$ in some way, and again
are linearly independent. We can also find $a$ functional interpolant $\eta$
such that, for some constant $\alpha _ { Y } ,$ $z _ { i } = \alpha _ { Y } + \langle \eta , Y _ { i } \rangle$ for all $i$ i. This means
that the given values $z _ { i }$ can be predicted perfectly either from the $X _ { i }$
or from the $Y _ { i } .$

It follows that not only have we found functions $5$ and $\eta$ such
that $\mathrm { c c o r s q } \left( 5 , \eta \right) = 1 ,$ because the variates $\langle E , X _ { i } \rangle$ and $\langle \eta , Y _ { i } \rangle$ are
perfectly correlated, but that we can prescribe the values $z _ { i }$ taken by
the canonical variates to be whatever we please, up to a constant. In
particular, we could start with any function $,$ construct $z _ { i } = \langle 5 , X _ { i } \rangle ,$
and then find a function $\eta$ such that $\mathrm { c c o r s q } \left( 5 , \eta \right) = 1 .$ In this sense,
every possible function can arise as a canonical variate weight function
with perfect correlation!

Leurgans, Moyeed and Silverman (1993) discuss this result in greater
detail. They demonstrate that the assumption of linear independence
among the curves is a very mild one, and, by proving an appropriate
consistency result, they show that regularization indeed makes
meaningful estimates possible.


### 12.6 Algorithmic considerations


#### 12.6.1 Discretization and basis approaches

Just as in the case of functional regression discussed in Chapter
10, there are several ways of carrying out our method of smoothed
functional CCA numerically. For completeness, we present the

<!-- PageBreak -->

<!-- PageNumber="212" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

methodology for the general case of different parameters $\lambda _ { 1 }$ and $\lambda _ { 2 } .$
$\mathrm { A }$ direct approach is to set up a discrete version of the eigenequation
(12.10). Discretize the functions $\mathfrak{z}$ and $\eta$ and the covariance operators
$v _ { j k } \left( s , t \right)$ using $a$ fine grid, and replace the operator $D ^ { 4 }$ by a finite
difference approximation. System (12.10) then becomes a large linear
system whose leading eigenvalue and eigenvector are found by
standard numerical methods.

We can also use a basis for the functions $X _ { i }$ and $Y _ { i } ,$ and for the weight
functions $5$ and $\eta .$ Suppose that $\phi _ { 1 } , \phi _ { 2 } , \ldots , \phi _ { M }$ is a suitable basis as
in Sections 10.4.1 and 10.6.2. $\mathrm { A s }$ usual, define $\mathrm { K }$ to be the matrix with
entries $\langle D ^ { 2 } \phi _ { j } , D ^ { 2 } \phi _ { k } \rangle$ and $\mathrm { J }$ the matrix with entries $\langle \phi _ { j } , \phi _ { k } \rangle .$ If we use
a Fourier or other orthonormal basis, then $\mathrm { J }$ is the identity matrix.

Define $\mathrm { C }$ and $\mathrm { D }$ to be the matrices of coefficients of the basis
expansions of the $X _ { i }$ and $Y _ { i }$ respectively, meaning that

$$X _ { i } = \sum _ { v = 1 } ^ { M } c _ { i v } \phi _ { v }$$

and

$$Y _ { i } = \sum _ { v = 1 } ^ { M } d _ { i v } \phi _ { v }$$

up to the degree of approximation involved in any choice of the number
$M$ of basis functions considered. Write a and $b$ for the vectors of
coefficients of the basis expansions of the functions $5$ and $\eta .$

Define $M \times M$ covariance matrices $\widetilde { \mathrm { V } } _ { 1 1 } ,$ $\widetilde { \mathrm { V } } _ { 1 2 }$ and $\widetilde { \mathrm { V } } _ { 2 2 }$ to be the matrices
with $\left( v , p \right)$ entries

$$N ^ { - 1 } \sum _ { i } c _ { i v } c _ { i \rho } , N ^ { - 1 } \sum _ { i } c _ { i v } d _ { i \rho } , \text { and } N ^ { - 1 } \sum _ { i } d _ { i v } d _ { i \rho } ,$$

respectively, the sample variance and covariance matrices correspond-
ing to the basis expansions of the data. It is straightforward to show
that, in the basis expansion domain, we carry out the smoothed CCA
of the given data by solving the generalized eigenvalue problem

$$\left[ \begin{array}{} 0 & \mathrm { J } \widetilde { \mathrm { V } } _ { 1 2 } \mathrm { J } \\ \mathrm { J } \widetilde { \mathrm { V } } _ { 2 1 } \mathrm { J } & 0 \end{array} \right] \left[ \begin{array}{} a \\ b \end{array} \right] = \rho \left[ \begin{array}{} \mathrm { J } \widetilde { \mathrm { V } } _ { 1 1 } \mathrm { J } + \lambda _ { 1 } \mathrm { K } & 0 \\ 0 & \mathrm { J } \widetilde { \mathrm { V } } _ { 2 2 } \mathrm { J } + \lambda _ { 2 } \mathrm { K } \end{array} \right] \left[ \begin{array}{} a \\ b \end{array} \right] .$$

As in Chapter 10, we should choose the number of basis functions
$M$ large enough to ensure that the regularization is controlled by
the choice of the smoothing parameter(s) $\lambda$ rather than that of
dimensionality $M .$ Values of $M$ of around 20 should give good results
without imposing an excessive computational burden.

<!-- PageBreak -->

<!-- PageNumber="213" -->
<!-- PageHeader="12.6 Algorithmic considerations" -->


#### 12.6.2 The roughness of the canonical variates

A third algorithmic possibility is related to the idea of quantifying
of the roughness of a variate, as discussed in Section 10.5.1. Just as
in the case of functional regression, this idea is of both conceptual
and algorithmic value, and can be used to elucidate the regularization
method we propose for functional canonical correlation analysis.

Suppose $z _ { i } = \langle 5 , X _ { i } \rangle$ is a possible canonical variate. Let $R _ { X }$ be
the matrix $\mathrm { R }$ as derived in Section 10.7.3, implying that $z ^ { \prime } R _ { X } z$ is the
roughness of the smoothest functional interpolant to the values $z _ { i }$
with respect to the functional covariates $X _ { i } .$ It may be that this value is
equal to $| | D ^ { 2 } E | | ^ { 2 } ,$ or it may be that $z _ { i }$ can be obtained by integrating a
smoother function against the $X _ { i } .$ In any case, we can consider $z ^ { \prime } \mathrm { R } _ { X } z$
in its own right as a measure of the roughness of $z _ { i }$ as a variate based
on the $X _ { i } .$

Similarly, let $\mathbb{R} _ { Y }$ be a matrix such that the roughness of any variate
$w$ relative to the observed covariate functions $\left\{ Y _ { i } \right\}$ is $w ^ { \prime } \mathrm { R } _ { \mathrm { Y } } w .$ Our
smoothed canonical correlation method can then be recast as the
determination of variates $z$ and $w$ to maximize the sample covariance
of $z _ { i }$ and $w _ { i }$ subject to

$$\mathrm { v a r } \left\{ z _ { i } \right\} + \lambda _ { 1 } z ^ { \prime } \mathrm { R } _ { X } z = \mathrm { v a r } \left\{ w _ { i } \right\} + \lambda _ { 2 } w ^ { \prime } \mathrm { R } _ { Y } w = 1 .$$
(12.11)

Once we have found in this way a pair of canonical variates, the
corresponding weight functions are defined as the smoothest functions
$5$ and $\eta$ satisfying $z _ { i } = \langle 5 , X _ { i } \rangle$ and $w _ { i } = \langle \eta , Y _ { i } \rangle$ for all i. Since we are
concerned only with the variance and covariance of the $\left\{ z _ { i } \right\}$ and $\left\{ w _ { i } \right\} ,$
we can discard the constant terms in the functional interpolation.

As before, we can maximize the sample covariance of $\left\{ z _ { i } \right\}$ and $\left\{ w _ { i } \right\}$
subject to the constraints (12.11) by solving an eigenvalue problem.
Some care is necessary to deal with a slight complication caused by
the presence of the sample mean in the formula for variance and
covariance.

Assuming without loss of generality that the canonical variates have
sample mean zero, write the constrained maximization problem as that
of finding the maximum of $z ^ { \prime } w$ subject to the constraints

$$z ^ { \prime } z + \lambda _ { 1 } z ^ { \prime } R _ { X } z = w ^ { \prime } w + \lambda _ { 2 } w ^ { \prime } R _ { Y } w = 1$$
(12.12)

and the additional constraints

$$1 ^ { \prime } z = 1 ^ { \prime } w = 0 .$$
(12.13)

For the moment, neglect the constraint (12.13) and consider the
maximization of $z ^ { \prime } w$ subject only to the constraints (12.12). This

<!-- PageBreak -->

<!-- PageNumber="214" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

corresponds to the eigenvalue problem

$$\left[ \begin{array}{} { 0 } & { I } \\ { I } & { 0 } \end{array} \right] \left[ \begin{array}{} { z } \\ { w } \end{array} \right] = \rho \left[ \begin{array}{} { I + \lambda _ { 1 } R _ { X } } & { 0 } \\ { 0 } & { I + \lambda _ { 2 } R _ { Y } } \end{array} \right] \left[ \begin{array}{} { z } \\ { w } \end{array} \right] .$$
(12.14)

By premultiplying (12.14) by $\left[ z ^ { \prime } w ^ { \prime } \right]$ and taking the product of the
two expressions for $z ^ { \prime } w$ thus obtained, any solution of (12.14) satisfies

$$\left( z ^ { \prime } w \right) ^ { 2 } = \rho ^ { 2 } \left( z ^ { \prime } z + \lambda _ { 1 } z ^ { \prime } R _ { X } z \right) \left( w ^ { \prime } w + \lambda _ { 2 } w ^ { \prime } R _ { Y } w \right) \geq \rho ^ { 2 } \left( z ^ { \prime } z \right) \left( w ^ { \prime } w \right)$$

and so it is necessarily the case that $| \rho | \leq 1 .$ Since the smoothest
functional interpolant of the constant vector has roughness zero,
$R _ { X } 1 = R _ { Y } 1 = 0 ,$ and so the condition $z = w = 1$ yields the leading
solution of (12.14), with eigenvalue $\rho = 1 .$

The solution of (12.14) with the second largest eigenvalue maximizes
$z ^ { \prime } w$ subject to the constraint (12.12) and the additional constraint

$$1 ^ { \prime } \left( I + \lambda _ { 1 } R _ { X } \right) z = 1 ^ { \prime } \left( I + \lambda _ { 2 } R _ { Y } \right) w = 0 .$$
(12.15)

But since $R _ { X } 1 = R _ { Y } 1 = 0 ,$ the constraint (12.15) is precisely equivalent
to the constraint (12.13) that we temporarily neglected. It follows that
the second and subsequent eigensolutions of (12.14) are the canonical
variates we require, and automatically have sample mean zero; the
leading solution is a constant and should be ignored.


### 12.7 Penalized optimal scoring and discriminant analysis

Hastie, Buja and Tibshirani (1995) consider functional forms of the
multivariate techniques of optimal scoring and linear discriminant
analysis, making use of ideas closely related to the functional canonical
correlation analysis approach discussed in this chapter. We present a
brief overview of their work; see the original paper for further details.


#### 12.7.1 The optimal scoring problem

Assume that we have $N$ paired observations $\left( X _ { i } , y _ { i } \right)$ where each $X _ { i }$ is
a function, and each $\mathcal{Y} _ { i }$ is a category or class taking values in the set
$\left\{ 1 , 2 , \cdots , J \right\} .$ For notational convenience, we code each $\mathcal{Y} _ { i }$ as a J-vector
with value 1 in position $j$ if $y _ { i } = j ,$ and 0 elsewhere.

We aim to obtain $a$ function $\beta$ and a J-vector $\theta$ minimizing the
criterion

$$\mathrm { O S E R R } \left( \theta , \beta \right) = N ^ { - 1 } \sum _ { i = 1 } ^ { N } \left( \langle \beta , X _ { i } \rangle - \theta ^ { \prime } \mathcal{Y} _ { i } \right) ^ { 2 }$$

<!-- PageBreak -->

<!-- PageNumber="215" -->
<!-- PageHeader="12.7 Penalized optimal scoring and discriminant analysis" -->

subject to the normalization constraint $N ^ { - 1 } \sum _ { i } \left( \theta ^ { \prime } y _ { i } \right) ^ { 2 } = 1 .$ The idea
is to turn the categorical variable coded by the y-vectors into a
quantitative variable taking the values $\theta _ { j } .$ The $\theta _ { j }$ are the scores for
the various categories, chosen to give the best available prediction of $a$
linear property $\langle \beta , X \rangle$ of the observed functional data.

For any given $\theta ,$ the problem of finding the functions $\beta$ is the
functional regression problem discussed in Chapter 10. There we saw
that, without some regularization, it is usually possible to choose $\beta$ to
give perfect prediction of any specified values $\theta ^ { \prime } \mathcal{Y} _ { i } .$ This means that
we cannot choose an optimal score vector $\theta$ uniquely on the basis
of the observed data. To deal with this difficulty, Hastie et al. (1995)
introduced the penalized optimal scoring criterion

$$\mathrm { O S E R R } _ { \lambda } \left( \theta , \beta \right) = \mathrm { O S E R R } \left( \theta , \beta \right) + \lambda \times \mathrm { P E N } \left( \beta \right) ,$$

where $\lambda$ is a smoothing parameter and $P E N \left( \beta \right)$ a roughness penalty.


#### 12.7.2 The discriminant problem

The discriminant problem is similar to the optimal scoring problem.
Again, we have functional observations $X _ { i } ,$ each allocated to a category
in $\left\{ 1 , 2 , \ldots , J \right\} .$ For any proposed linear discriminant functional $\langle \beta , X _ { i } \rangle ,$
define $\theta _ { j }$ to be the average of the $\langle \beta , X _ { i } \rangle$ for all $X _ { i }$ falling in category
$j .$ For each fixed $\beta ,$ this value of $\theta$ minimizes the quantity $\mathrm { O S E R R } \left( \theta , \beta \right) ,$
which can then be re-interpreted as the within-class variance of the
$\langle \beta , X _ { i } \rangle .$ The between-class variance is simply the variance of the
discriminant class means $\theta ^ { \prime } y _ { i } ,$ defining the $J$ J-vectors $\mathcal{Y} _ { i }$ by the same
coding as above. Discriminant analysis aims to maximize the between-
class variance subject to a constraint on the within-class variance.

The roles of objective function and constraint are exchanged
in passing from optimal scoring to discriminant analysis, and
minimization is replaced by maximization. Also, primary attention
shifts from the score vector $\theta$ in optimal scoring to the discriminant
functional defined by the function $\beta$ in discriminant analysis. Hastie
et al. make the correspondence complete by proposing penalized
discriminant analysis where we maximize the raw between-class
variance subject to a penalized constraint on the within-class variance

$$\mathrm { O S E R R } \left( \theta , \beta \right) + \lambda \times \mathrm { P E N } \left( \beta \right) = 1 .$$


#### 12.7.3 The relationship with CCA

Simple modifications of arguments from multivariate analysis show
that the penalized optimal scoring and the penalized discriminant

<!-- PageBreak -->

<!-- PageNumber="216" -->
<!-- PageHeader="12. Canonical correlation and discriminant analysis" -->

analysis problems are both equivalent to the mixed functional-
multivariate canonical correlation analysis problem of maximizing the
covariance of $\langle E , X _ { i } \rangle$ and $\eta ^ { \prime } \mathcal{Y} _ { i }$ subject to the constraints

$$\mathrm { v a r } \left( \langle \xi , X _ { i } \rangle \right) + \lambda \times \mathrm { P E N } \left( \mathrm { S } \right) = \mathrm { v a r } \left( \eta ^ { \prime } \mathcal{Y} _ { i } \right) = 1 .$$
(12.16)

In the notation we have used for CCA, the weight corresponding to
the functional part $X _ { i }$ of the data is itself $a$ function $5 ,$ whereas the
vector part $\mathcal{Y} _ { i }$ is mapped to its canonical variate by a weight vector $\eta .$
Only the functional part $5$ is penalized for roughness in the constraints
(12.16).

This formulation gives rise to an eigenequation of the form (12.10)
but with no penalty attached to $V _ { 2 2 } .$ The numerical approaches we have
set out for CCA carry over to this case, with appropriate modifications
because only the $X _ { i }$ are functions.

To obtain the solutions $\left( \beta , \theta \right)$ of the discriminant and optimal scoring
problems, it is only necessary to rescale the estimated function $5$ and
vector $\eta$ appropriately. The subsidiary eigensolutions, as mentioned
in Section 12.2.3, are also interesting for these problems because they
yield estimates of vector-valued scores $\theta _ { j }$ and discriminants $\langle \beta , X _ { i } \rangle .$


#### 12.7.4 Applications

Hastie et al. present two fascinating applications of these techniques.
For speech recognition, the frequency spectra of digitized recordings
of various phonemes are used as data. A roughness penalty of the form
$P E N \left( \beta \right) = \int \left\{ D ^ { 2 } \beta \left( w \right) \right\} ^ { 2 } w \left( w \right) d w$ is used, with the weight function $w \left( w \right)$
chosen to place different emphasis on different frequencies $w .$

Their other application is the recognition of digits in handwritten
postal addresses and zip codes. In this case, the observations $X _ { i }$ are
functions of a bivariate argument $t ,$ defined in practice on $1 6 \times 1 6$ pixel
grid. The roughness penalty used is a discrete version of the Laplacian
penalty $\int \left[ V ^ { 2 } \beta \left( t \right) \right] ^ { 2 } d t .$

<!-- PageBreak -->


## 13 Differential operators in functional data analysis


### 13.1 Introduction

The derivatives of functional observations have played a strong
role from the beginning of this book. For example, for growth
curves and handwriting coordinate functions we chose to work with
acceleration directly, and for temperature profiles we considered
functions $\left( \pi / 6 \right) ^ { 2 } D T e m p + D ^ { 3 } T e m p .$ We used $D ^ { 2 } \beta$ to construct a measure
of curvature in an estimated regression function $\beta$ to regularize or
smooth the estimate, and applied this same principle in functional
principal components analysis, canonical correlation, and other types
of linear models. Thus, derivatives can be used both as the object of
inquiry and as tools for stabilizing solutions.

It is time to look more systematically at how derivatives might
be employed in FDA. Are there other ways of using derivatives,
for example? Can we use mixtures of derivatives instead of simple
derivatives? Can we extend models so that derivatives can be used
on either the covariate or response side? Can our smoothing and
regularization techniques be extended in useful ways? Are new
methods of analysis making explicit use of derivative information
possible?

The next two chapters explore these questions. But since certain
results drawn from the theory of differential equations are essential

<!-- PageBreak -->

<!-- PageNumber="218" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->


<figure>
<figcaption>FIGURE 13.1. The left panel shows the gross domestic product of the United States in trillion US$. The solid curve is a polynomial smoothing spline constructed with penalty the integrated squared fourth derivative, and the dotted curve is a purely exponential trend fit by least squares. The solid curve in the right panel is the estimated first derivative of GDP. The dashed curve in this panel is the value of the differential operator $L = - y \mathrm { G D P } + D C D P .$</figcaption>

7

US GDP (trillion $)

US GDP derivative

-0.1 0.0 0.1 0.2 0.3 0.4

6

5

\+

3

1980 1984 1988 1992

1980 1984 1988 1992

Year

Year

</figure>


to this enquiry, first of all we present and explain, without proof, some
essential preliminary results.

The central idea to be explored is that of a linear differential operator
$L ,$ which is a weighted combination of derivatives up to a specified order
$m :$

$$L = w _ { 0 } I + w _ { 1 } D + w _ { 2 } D ^ { 2 } + \ldots + D ^ { m }$$
(13.1)

where the $m$ coefficient functions $w _ { j } ,$ $j , j = 0 , \ldots , m - 1$ define the
operator. For brevity we make free use of the acronym LDO for linear
differential operator.

First, however, we introduce some data to illustrate these notions.


### 13.2 Two sets of data


#### 13.2.1 The gross domestic product data

The gross domestic product (GDP) of a country is the financial value
of all goods and services produced in that country, whether by the
private sector of the economy or by government. Like most economic
measures, GDP tends to exhibit a percentage change each year in
times of domestic and international stability. Although this change
can fluctuate considerably from year to year, over long periods the

<!-- PageBreak -->

<!-- PageNumber="219" -->
<!-- PageHeader="13.2 Two sets of data" -->

fluctuations tend to even out for most countries and the long-range
trend in GDP tends to be roughly exponential.

We obtained quarterly GDP values for 15 countries in the
Organization for Economic Cooperation and Development (OECD) for
the years 1980 through 1994 (OECD, 1995). The values for any country
are expressed in its own currency, and thus scales are not comparable
across countries. Also, there are strong seasonal effects in GDP values
reported by some countries, whereas others smooth them out before
reporting.

The left panel of Figure 13.1 displays the GDP of the United States.
The seasonal trend, if any, is hardly visible, and the solid line indicates a
smooth of the data using a penalty on $D ^ { 4 } G D P .$ It also shows a best fitting
exponential trend, $C \quad e x p \left( y t \right) ,$ with rate constant $y = 0 . 0 3 8 .$ Thus, over
this period the U.S .. economy tended to grow at about 4% per year.
The right panel displays the first derivative of GDP as a solid line. The
economy advanced especially rapidly in 1983, 1987 and 1993, but there
were slowdowns in 1981, 1985 and 1990.


#### 13.2.2 The melanoma data

Figure 13.2 presents age-adjusted melanoma incidences for 37 years
from the Connecticut Tumor Registry (Houghton et al., 1980).
Two types of trend are obvious: a steady linear increase and a
periodic component. The latter is related to sunspot activity and
the accompanying fluctuations in solar radiation. Two smooths of
these data are given: the solid line is a polynomial smoothing spline
penalizing the squared norm of the fourth derivative $D ^ { 4 } x$ with penalty
parameter chosen by minimizing generalized cross-validation, and the
dotted curve is a least squares fit of the function

$$x \left( t \right) = c _ { 1 } + c _ { 2 } t + c _ { 3 } \sin \left( \omega t \right) + c _ { 4 } \cos \left( \omega t \right) .$$
(13.2)

Clearly, this linear/periodic function fits the data well, but is there
additional variation to be estimated? The polynomial spline fit differs
slightly from this function, but a choice of differential operator $L$ to
define the penalty term that would be more natural than $L = D ^ { 4 }$ is

$$L x = w ^ { 2 } D ^ { 2 } x + D ^ { 4 } x$$

since, given the appropriate value for period $2 \pi / w ,$ functions in the
class (13.2) satisfy $L x = 0$ and would therefore receive zero penalty.

<!-- PageBreak -->

<!-- PageNumber="220" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->


<figure>
<figcaption>FIGURE 13.2. Age-adjusted incidences of melanoma for the years 1936 to 1972. The solid curve is the polynomial smoothing spline fit to the data penalizing the norm of the fourth derivative, with the smoothing parameter chosen by minimizing the GCV criterion. The dotted line is the fit of $x \left( t \right) = c _ { 1 } + c _ { 2 } t + c _ { 3 } \sin \left( w t \right) + c _ { 3 } \cos \left( w t \right)$ with $w = 0 . 6 5$ and coefficients estimated by least squares.</figcaption>

Melanoma per 100,000

\+

3

2

L

1940

$1 9 5 0$

1960

1970

</figure>


### 13.3 Some roles for linear differential operators


#### 13.3.1 Operators to produce new functional observations

Derivatives of various orders and mixtures of them are of immediate
interest in many applications. We have already noted that there is much
to be learned about human growth by examining acceleration profiles.
There is an analogy with mechanical systems; a version of Newton's
third law, $a \left( t \right) = F \left( t \right) / M ,$ asserts that the application of some force
$F \left( t \right)$ at time $t$ on an object with mass $M$ has an immediate impact on
acceleration $a \left( t \right) .$ However, it has only an indirect impact on velocity,
$v \left( t \right) = v _ { 0 } + M ^ { - 1 } \int _ { 0 } ^ { t } F \left( u \right) d u ,$ and an even less direct impact on what we
directly observe, namely position $s \left( t \right) = s _ { 0 } + v _ { 0 } t + M ^ { - 1 } \int _ { 0 } ^ { t } \int _ { 0 } ^ { u } F \left( z \right) d z .$
From the standpoint of mechanics, the world that we experience is two
integrals away from reality! The release of adrenal hormones during
puberty tends to play the role of the force function $F ,$ and so does a
muscle contraction with respect to the position of a limb or other part
of the body.

<!-- PageBreak -->

<!-- PageNumber="221" -->
<!-- PageHeader="13.3 Some roles for linear differential operators" -->

Consider another kind of growth, exponential growth or decay
exhibited by systems such as populations, radioactive particles and
economic indicators with arbitrary value $\alpha$ at the origin,

$$x \left( t \right) = \alpha e ^ { y t } .$$
(13.3)

If we take the ratio

$$\frac { D x } { x } = D \ln x = y ,$$

we can isolate the rate parameter $y ,$ and this can also be inspected by
plotting $D x$ against $x$ and computing the slope. Put yet another way,
an exponential growth process of this nature satisfies the simple linear
differential equation

$$y x = D x$$
(13.4)

or, alternatively, the linear homogeneous differential equation

$$- y x + D x = 0 .$$
(13.5)

If we define $L x$ to be $- y x + D x ,$ then we may say even more compactly
that $L x = 0$ implies exponential growth. When studying processes that
exhibit exponential growth or decay to some extent, it can therefore be
helpful to look at $L x$ defined in this way; the extent to which the result is
a nonzero function with substantial variation is a measure of departure
from exponential growth, just as the appearance of a nonzero phase in
$D ^ { 2 } x$ for a mechanical system indicates the application of a force.

For the GDP data, one of several techniques for estimating the
rate parameter $y$ is to fit model (13.3) to data by least squares.
This produces an estimate of 0.038 for the U.S. data displayed in
Figure 13.1, and the fitted exponential trend is shown there as the
dotted curve in the left panel. The right panel presents the values
of $L G D P = - \quad 0 . 0 3 8 \quad G D P + D G D P$ as the dashed curve. This function
indicates the periods of departure from exponential growth, and makes
the hypergrowth epochs in 1983, 1987 and 1993, and recessions in
1981 and 1990 even more apparent. Figure 13.3 shows the comparable
curves for the United Kingdom and Japan, and we note that the U.K. had
only one boom period with an uncertain recovery after the recession,
whereas Japan experienced a deep and late recession.


#### 13.3.2 Operators to regularize or smooth models

Although we have covered this topic elsewhere, we should still point
out that we may substitute $L x$ for $D ^ { 2 } x$ in any of the regularization
schemes covered so far. Why? The answer lies in the homogeneous

<!-- PageBreak -->

<!-- PageNumber="222" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->


<figure>
<figcaption>FIGURE 13.3. The solid curves are the derivatives of GDP of the United Kingdom and Japan estimated by smoothing splines penalizing for integrated squared fourth derivative. The dashed curves are the corresponding values of the differential operator $L = - \quad y x + D x .$</figcaption>

United Kingdom

30000

Japan

GDP derivative

5000 10000

GDP derivative

-10000 0 10000

0

1982 1986 1990 1994

1982 1986 1990 1994
Year

Year

</figure>


equation $L x = 0 ;$ functions satisfying this equation are deemed to be
hypersmooth in the sense that we choose to ignore any component of
variation of this form in calculating roughness or irregularity. In the
case of the operator $D ^ { 2 } ,$ linear trend is considered to be so smooth
that any function may have an arbitrary amount of it, since the penalty
term $\lambda \int \left( D ^ { 2 } x \right) ^ { 2 }$ is unaffected. On the other hand, suppose that we are
working with a process that has predominantly exponential growth
with rate parameter $y .$ In this case we may choose nonparametric
regression with the fitting criterion

$$P E N S S E _ { \lambda } \left( x \right) = n ^ { - 1 } \sum _ { j = 1 } ^ { n } \left[ y _ { j } - x \left( t _ { j } \right) \right] ^ { 2 } + \lambda \int \left[ - y x \left( t \right) + D x \left( t \right) \right] ^ { 2 } d t$$

to leave untouched any component of variation of this form.

More generally, suppose we observe a set of discrete data values
generated by the process

$$y _ { j } = x \left( t _ { j } \right) + \epsilon _ { j }$$

where, as in previous chapters, $x$ is some unobserved smooth function
that we wish to estimate by means of nonparametric regression, and
$\epsilon _ { j }$ is a disturbance or error assumed to be independently distributed
over $j$ and to have mean zero and finite variance. Moreover, suppose

<!-- PageBreak -->

<!-- PageNumber="223" -->
<!-- PageHeader="13.3 Some roles for linear differential operators" -->

that we employ the general smoothing criterion

$$P E N S S E _ { \lambda } \left( \widehat { x } \right) = n ^ { - 1 } \sum _ { j } \left[ y _ { j } - \widehat { x } \left( t _ { j } \right) \right] ^ { 2 } + \lambda \int \left( L \widehat { x } \right) ^ { 2 } \left( t \right) d t$$
(13.6)

for some differential operator $L .$ Then it is not difficult to show (see
Wahba, 1990) that, if we choose $\widehat { \mathrm { x } }$ to minimize $\mathrm { P E N S S E } _ { \lambda } ,$ then the
integrated squared bias

$$B i a s ^ { 2 } \left( \widehat { x } \right) = \int \left\{ E \widehat { x } \left( t \right) - x \left( t \right) \right\} ^ { 2 } d t$$ ☒

cannot exceed $\int L x \left( t \right) ^ { 2 } d t .$ This is rather useful, because if we choose
$L$ so that $L x = 0$ even approximately, the bias is sure to be small.

As a consequence, we can use a relatively larger value of the
smoothing parameter, leading to lower variance, without introducing
excessive bias. Also, we can achieve a small value of the integrated
mean squared error

$$E \left[ \widehat { x } \left( t \right) - x \left( t \right) \right] ^ { 2 } d t$$

since

$$\mathrm { I M S E } \left( \widehat { x } \right) = B i a s ^ { 2 } \left( \widehat { x } \right) + \mathrm { V a r } \left( \widehat { x } \right)$$ ☒ ☒

where

$$\mathrm { V a r } \left( \widehat { x } \right) = \int E \left\{ \widehat { x } \left( t \right) - E \left[ \widehat { x } \left( t \right) \right] \right\} ^ { 2 } d t .$$

Therefore we can conclude that, given any prior knowledge at all about
the predominant shape of $x ,$ it is worth choosing a linear differential
operator $L$ to annihilate functions having that shape. In the next two
chapters we show how to construct customized spline smoothers of
this type .

This insight about the role of $L$ in the regularization process also
leads to the following interesting question: Can we use the information
in $N$ replications $x _ { i }$ of functional observations such as growth or
temperature curves to estimate an operator $\underline { L }$ that comes close in some
sense to satisfying $L x _ { i } = 0 ? ,$ then we should certainly use this
information to improve on our smoothing techniques. This matter is
taken up in Chapter 15.


#### 13.3.3 Operators to partition variation

A central fact about linear differential operators $L$ of the form (13.1) of
degree $m$ is that, in general, there are $m$ linearly independent solutions

<!-- PageBreak -->

<!-- PageNumber="224" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->

$u _ { j }$ of the homogeneous equation $L u _ { j } = 0 .$ There is no unique way of
choosing these $m$ functions $u _ { j } ,$ but any choice is related by $a$ linear
transformation to any other choice. The set of all functions $z$ for which
$L z = 0$ is called the null space of $L ,$ and the functions $u _ { j }$ form a basis
for this space.

Consider, for example, the derivative operator $L = D ^ { m } :$ The
monomials $\left\{ 1 , t , \ldots t ^ { m - 1 } \right\}$ are a basis for the null space, as is the set
of $m$ polynomials formed by any nonsingular linear transformation of
these. Likewise the functions $\left\{ 1 , e ^ { y t } \right\}$ are a solution set for $- y D x +$
$D ^ { 2 } x = 0 ,$ and $\left\{ 1 , \sin w t , \cos w t \right\}$ were cited as the solution set or null
space functions for $L x = w ^ { 2 } D x + D ^ { 3 } x = 0$ in Chapter 1.

Thus, we can use linear differential operators $L$ to partition
functional variation in the sense that $L x$ splits $x$ into two parts, the
first consisting of whatever in $x$ is a linear combination of the null
space functions $u _ { j } ,$ and the second being whatever is orthogonal to
these functions. As we already know, this partitioning of variation is
just what happens with basis functions $\phi _ { k }$ and the projection operator
$P$ that expands $x$ as a linear combination of these basis functions. The
projection

$$P x = \widehat { x } = \sum _ { k = 1 } ^ { m } c _ { k } \phi _ { k }$$

splits any function $x$ into the component $\widehat { x }$ that is an optimal
combination of the basis functions in a least squares sense, and an
orthogonal residual component $x \quad - \quad x = \left( I \quad - \quad P \right) x .$ The complementary
projection operator $Q = I \quad - \quad P$ therefore satisfies the linear
homogeneous equation $Q \widehat { x } = 0 ,$ as well as the $m$ equations $Q \phi _ { k } = 0 .$
Thus the projection operator $Q$ and the differential operator $L$ appear
to have analogous properties.

But there are some important differences. First, projection does not
pay any attention to derivative information, whereas $L$ does. Second,
we have the closely related fact that $Q$ is chosen to make $Q x$ small,
whereas $L$ is chosen to make $L x$ small. Since $L x$ involves derivatives up
to order $m ,$ making $L x$ small inevitably means paying attention to the
size of $D ^ { m } x .$ If we think there is important information in derivatives
in some vague sense, it seems right to exploit this in splitting variation.

It is particularly easy to compare the two operators, differential and
projection, in situations where there is an orthonormal basis expansion
for the function space in question. Consider, for example, the space of
infinitely differentiable periodic functions defined on the interval $\left[ 0 , 1 \right]$
that would be natural for modelling our temperature and precipitation

<!-- PageBreak -->

<!-- PageNumber="225" -->
<!-- PageHeader="13.3 Some roles for linear differential operators" -->

records. A function $x$ has the Fourier expansion

$$x \left( t \right) = c _ { 0 } + \sum _ { k = 1 } ^ { \infty } \left[ c _ { 2 k - 1 } \sin \left( 2 \pi k t \right) + c _ { 2 k } \cos \left( 2 \pi k t \right) \right] .$$

Suppose our two operators $L$ and $Q$ are of order three and designed
to eliminate the first three terms of the expansion, that is, $a$ vertically
shifted sinusoidal variation of period one. Then,

$$Q x \left( t \right) = \sum _ { k = 2 } ^ { \infty } \left[ c _ { 2 k - 1 } \sin \left( 2 \pi k t \right) + c _ { 2 k } \cos \left( 2 \pi k t \right) \right] ,$$

whereas

$$L x = 4 \pi ^ { 2 } D x + D ^ { 3 } x$$
$$= \sum _ { k = 2 } ^ { \infty } 8 \pi ^ { 3 } k \left( k ^ { 2 } - 1 \right) \left[ - c _ { 2 k - 1 } \cos \left( 2 \pi k t \right) + c _ { 2 k } \sin \left( 2 \pi k t \right) \right] .$$

Note that applying $Q$ does not change the expansion beyond the third
term, whereas $L$ multiplies each successive pair of sines and cosines
by an ever-increasing factor proportional to $k \left( k ^ { 2 } - 1 \right) .$ Thus, $L$ actually
accentuates high-frequency variation whereas $Q$ leaves it untouched;
functions that are passed through $L$ are going to come out rougher
than those passing through $Q .$

The consequences for smoothing are especially important: If we
penalize the size of $| | L x | | ^ { 2 }$ in spline smoothing by minimizing the
criterion (13.6), the roughening action of $L$ means that high-frequency
components are forced to be smaller than they would be in the original
function, or than they would be if we penalized using $Q$ by using the
criterion

$$P E N S S E _ { \lambda } ^ { Q } \left( \widehat { x } \right) = n ^ { - 1 } \sum _ { j } \left[ y _ { j } - \widehat { x } \left( t _ { j } \right) \right] ^ { 2 } + \lambda \int \left( Q \widehat { x } \right) ^ { 2 } \left( t \right) d t .$$
(13.7)

But customizing a regularization process is only one reason for
splitting functional variation, and in Chapter 14 we look at a differential
operator analogue of principal components analysis, called principal
differential analysis, that can prove to be a valuable exploratory tool.


#### 13.3.4 Operators to define solutions to problems

Engineers and scientists find that differential equations in general and
linear differential equations in particular often provide elegant and
powerful tools for identifying the solution of a problem or stating a

<!-- PageBreak -->

<!-- PageNumber="226" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->

theory. For example, Newton might have defined his Third Law as the
solution of the equation

$$M D ^ { 2 } s = F$$

where $s$ is the position of a body with mass $M$ as a function of time.

For example, consider the simple but important problem of defining
an arbitrary function that is everywhere positive and at the same time
differentiable, with domain $t \geq 0 .$ One approach is to define it as the
solution of the equation

$$D x = w x$$

where the coefficient function $w$ is smooth enough to be integrated.
That a positive differentiable function satisfies this equation is clear;
since $x$ is positive and differentiable, we can take the ratio $D x / x ,$
and this is simply $w .$ Conversely, the general solution of the equation
$D x = w x$ is given by

$$x \left( t \right) = \beta \exp \left( \int _ { 0 } ^ { t } w \left( u \right) d u \right) .$$
(13.8)

where $\beta$ is an arbitrary positive constant. What we have achieved here
is to change a constrained problem, namely defining a positive function
$x ,$ into an unconstrained problem, that is computing $w .$ In general, it is
much easier to approximate unconstrained functions than constrained
ones.

Taking this one step further, the equation

$$D ^ { 2 } x = w D x$$

defines an arbitrary twice-differentiable monotonic function, as in
Section 5.4.2. As explained there, the solution to this equation is of
the form

$$x \left( t \right) = x _ { 0 } + \alpha \int _ { 0 } ^ { t } \exp \left( \int _ { 0 } ^ { u } w \left( z \right) d z \right) d u$$
(13.9)

where $x _ { 0 }$ and $\alpha$ are arbitrary constants with $\alpha \neq 0 .$ This provides the
general solution for $a$ twice-differentiable monotonic function, and at
the same time transforms the problem from estimating the constrained
function $x$ to estimating the unconstrained function $w .$ Note, too,
that this generalizes the equation for vertically-shifted exponential
growth $x \left( t \right) = x _ { 0 } + \alpha e ^ { \beta t }$ in an interesting way; the constant function
$w \left( t \right) = \beta$ yields this equation when substituted in (13.9), implying
that departures from constant behaviour of $w$ generalize exponential
growth patterns in the function $x .$

<!-- PageBreak -->

<!-- PageNumber="227" -->
<!-- PageHeader="13.4 Some linear differential equation facts" -->


### 13.4 Some linear differential equation facts

So far in this chapter, we have set the scene for the use of differential
operators in FDA. Now we move on to a more detailed discussion
of techniques and ideas that we use in this and the following
chapters. Readers familiar with the theory of linear ordinary differential
equations may wish to skip on to the next two chapters, and refer back
to this material only where necessary. In any case, it is far beyond the
scope of this book to offer even a cursory treatment of $a$ topic as rich
as the theory of differential equations, and there would be little point,
since there are many fine texts on the topic. Some of our favourites
that are also classics are Coddington (1989), Coddington and Levinson
(1955) and Ince (1956), and for advice on a wide range of practical
matters we recommend Press et al. (1992).


#### 13.4.1 Derivatives are rougher

First, it is useful to point out a few things of general importance. For
example, taking a derivative is generally a roughening operation, as we
have observed in the context of periodic functions. This means that $D x$
in general has rather more curvature and variability than $x .$ It is perhaps
unfortunate that our intuitions about functions are shaped by our early
exposure to polynomials, for which derivatives are smoother than the
original functions, and transcendental functions such as $e ^ { t }$ and $\sin t ,$
for which taking derivatives produces essentially no change in shape.
In fact, the general situation is more like the growth curve accelerations
in Figure 1.2, which are much more variable than the height curves in
Figure 1.1, or the result of applying the third order LDO to temperature
functions displayed in Figure 1.4.

By contrast, the operation of partial integration essentially reverses
the process of differentiation (except for the constant of integration).
It is convenient to use the notation $D ^ { - 1 } x$ for

$$D ^ { - 1 } x \left( t \right) = \int _ { t _ { 0 } } ^ { t } x \left( s \right) d s ,$$

relying on context to specify the lower limit of integration $t _ { 0 } .$ This
means, of course, that $D ^ { - 1 } D x = x .$ In fact, much of the theory of
LDO's can be simplified, at least informally, by using the notion that
various powers of $D ,$ such as $D ^ { 3 } ,$ $D ^ { - 2 }$ and so on, behave essentially
like polynomials, and can be factored in the same way. The partial
integration operator $D ^ { - 1 }$ is a smoothing operator in the sense that the
result has less variability and curvature in general.

<!-- PageBreak -->

<!-- PageNumber="228" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->


#### 13.4.2 Finding a LDO that annihilates known functions

We have already cited a number of examples where we had a set of
known functions $\left\{ u _ { 1 } , \ldots , u _ { m } \right\}$ and where at the same time we were
aware of the LDO $L$ that solved the homogeneous linear differential
equations $L u _ { j } = 0 , j = 1 , \ldots , m .$ However, suppose that we have the
$u _ { j }$ in mind but that the LDO that annihilates them is not obvious, and
we want to find it.

The process of identifying the LDO that sets $m$ linearly independent
functions to 0, as well as other aspects of working with LDO's, can be
exhibited through the following example. Suppose we are considering
an amplitude-modulated sinusoidal signal with fixed period $w .$ Such a
signal would be of the form

$$x \left( t \right) = c _ { 1 } A \left( t \right) \sin \left( w t \right) + c _ { 2 } A \left( t \right) \cos \left( w t \right) .$$
(13.10)

The function $A$ determines the amplitude pattern. If $A$ is regarded as
a known time-varying function, the constants $\mathcal{C} _ { 1 }$ and $c _ { 2 }$ determine the
overall size of the signal's amplitude and its phase.

For given $w$ and $A \left( t \right) ,$ our aim is to find a differential operator $L$
such that the null space of $L$ consists of all functions of the form 13.10.
Because these functions form a linear space of dimension two, we seek
an annihilating operator of order two, of the form

$$L x = w _ { 0 } x + w _ { 1 } D x + D ^ { 2 } .$$

The task is to estimate the two weight functions $w _ { 0 }$ and $w _ { 1 } .$

First, let us do a few things to streamline the notation. Define the
vector functions $u$ and $w$ as

$$u \left( t \right) = \left[ \begin{array}{} { A \left( t \right) \sin \left( w t \right) } \\ { A \left( t \right) \cos \left( w t \right) } \end{array} \right] \text { and } w \left( t \right) = \left[ \begin{array}{} { w _ { 0 } \left( t \right) } \\ { w _ { 1 } \left( t \right) } \end{array} \right]$$
(13.11)

Also, use $S \left( t \right)$ to stand for $\sin \left( \omega t \right)$ and $C \left( t \right)$ for $\cos \left( \omega t \right) .$ Then

$$u = \left[ \begin{array}{} { A S } \\ { A C } \end{array} \right]$$
(13.12)

The required differential operator $L$ satisfies the vector equation $L u =$
0.

Recall that the first and second derivatives of $\mathrm { S }$ are wC and $- w ^ { 2 } s ,$
respectively, and that those of $\mathrm { C }$ are $- \infty 5$ and $- w ^ { 2 } C ,$ respectively. And,
of course, the ever-important $S ^ { 2 } + C ^ { 2 } = 1 .$ Then the first two derivatives
of $u$ are, after a bit of simplification,

$$D u = \left[ \begin{array}{} { \left( D A \right) S + w A C } \\ { \left( D A \right) C - w A S } \end{array} \right]$$

<!-- PageBreak -->

<!-- PageNumber="229" -->
<!-- PageHeader="13.4 Some linear differential equation facts" -->

and

$$D ^ { 2 } u = \left[ \begin{array}{} { \left( D ^ { 2 } A \right) S + 2 w \left( D A \right) C - w ^ { 2 } A S } \\ { \left( D ^ { 2 } A \right) C - 2 w \left( D A \right) S - w ^ { 2 } A C } \end{array} \right]$$
(13.13)

By taking the second derivatives over to the other side of the
equation, the relationship $L u = 0$ can be expressed as follows:

$$w _ { 0 } u + w _ { 1 } D u = - D ^ { 2 } u$$
(13.14)

or, in matrix notation,

$$\left[ \begin{array}{} { u } & { D u } \end{array} \right] w = - D ^ { 2 } u .$$
(13.15)

This is a linear matrix equation for the unknown weight functions
$w _ { 0 }$ and $w _ { 1 } ,$ and its solution is simple provided that the matrix

$$W \left( t \right) = \left[ \begin{array}{} { u \left( t \right) } & { D u \left( t \right) } \end{array} \right]$$
(13.16)

is nowhere singular, or in other words that its determinant $| W \left( t \right) | d o e s$
not vanish for any value of the argument $t .$ This coefficient matrix,
which plays an important role in LDO theory, is called the Wronskian
matrix, and its determinant is called the Wronskian for the system.

In this example, substituting the specific functions $A S$ and $A C$ for $u _ { 1 }$
and $u _ { 2 }$ gives

$$W = \left[ \begin{array}{} { A S } & { \left( D A \right) S + w A C } \\ { A C } & { \left( D A \right) C - w A S } \end{array} \right]$$
(13.17)

Thus the Wronskian is

$$| W | = A S \left[ \left( D A \right) C - w A S \right] - A C \left[ \left( D A \right) S + w A C \right] = - \infty A ^ { 2 }$$
(13.18)

after some simplification. We have no worries about the singularity of
$\mathrm { W } \left( t \right) ,$ then, so long as the amplitude function $A \left( t \right)$ does not vanish.

The solutions for the weight functions are then given by

$$w = - W ^ { - 1 } D ^ { 2 } u .$$

This takes a couple of sheets of paper to work out, or preferably is
solved using symbolic computation software such as Maple (Char $e t$
al., 1991) or Mathematica (Wolfram, 1991). Considerable simplification
is possible because of the identity $S ^ { 2 } + C ^ { 2 } = 1 ,$ leading to

$$W = \left[ \begin{array}{} { w ^ { 2 } + 2 \left( D A / A \right) ^ { 2 } - D ^ { 2 } A / A } \\ { - 2 D A / A } \end{array} \right]$$
(13.19)

so that, for any function $x ,$

$$L x = \left\{ w ^ { 2 } + 2 \left( D A / A \right) ^ { 2 } - D ^ { 2 } A / A \right\} x - 2 \left\{ \left( D A \right) / A \right\} \left( D x \right) + D ^ { 2 } x .$$

<!-- PageBreak -->

<!-- PageNumber="230" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->

As we should expect, the weight coefficients in (13.19) are scale free in
the sense that multiplying $A \left( t \right)$ by any constant does not change them.

Consider two simple possibilities for amplitude modulation func-
tions. When $A \left( t \right)$ is a constant, both derivatives vanish, the operator
reduces to $L = w ^ { 2 } + D ^ { 2 }$ and $L x = 0$ is the equation for simple harmonic
motion. On the other hand, if $A \left( t \right) = e ^ { - \lambda t }$ so that the signal damps out
exponentially with rate $\lambda ,$ then things simplify to

$$w = \left[ \begin{array}{} { w ^ { 2 } + \lambda ^ { 2 } } \\ { 2 \lambda } \end{array} \right] \text { or } L x = \left( w ^ { 2 } + \lambda ^ { 2 } \right) + 2 \lambda D x + D ^ { 2 } x .$$
(13.20)

This is the equation for damped harmonic motion with a damping
coefficient $2 \lambda .$

The example illustrates the following general principles. First, the
order $m$ Wronskian matrix

$$\mathrm { W } \left( t \right) = \left[ \begin{array}{} u \left( t \right) & D u \left( t \right) & \ldots & D ^ { m - 1 } u \left( t \right) \end{array} \right]$$
(13.21)

must be invertible, so that its determinant must not vanish over the
range of $t$ being considered. There are ways of dealing with isolated
singularities, however, but these are beyond our present scope. Second,
finding the vector of weight functions $w = \left( w _ { 0 } \left( t \right) , \ldots , w _ { m - 1 } \left( t \right) \right) ^ { \prime }$ is
then a matter of solving the system of $m$ linear equations $W \left( t \right) w \left( t \right) =$
$- D ^ { m } u \left( t \right) ,$ again with the possible aid of symbolic computation
software.


#### 13.4.3 Finding the functions $u _ { j }$ satisfying $L u _ { j } = 0$

Now let us consider the problem converse to that discussed in Section
13.4.2. Given an LDO L of order $m ,$ we might wish to identify $m$ linearly
independent solutions $u _ { j }$ to the homogeneous equation $L x = 0 .$ We
can do this directly by elementary calculus in simple cases, but more
generally there is a variety of analytic and numerical approaches to
this problem. For full details, see a standard reference on numerical
methods, such as Stoer and Bulirsch (1980).

One particular numerical iterative procedure, Picard's algorithm, is
simple to implement and, in principle, guaranteed to converge. Define
the order $m$ matrix function $\mathrm { T }$ as 0 for all values of $t$ except for

$$T _ { j , j + 1 } \left( t \right) = 1 , j = 1 , \ldots , m - 1$$

and

$$T _ { m j } \left( t \right) = - w _ { j - 1 } \left( t \right) , j = 1 , \ldots , m .$$

<!-- PageBreak -->

<!-- PageNumber="231" -->
<!-- PageHeader="13.5 Constraint functionals $B$" -->

Initialize the order $m$ matrix function $\mathrm { U }$ as $U ^ { \left( 0 \right) } \left( t \right) = I .$ On iteration
$v \geq 1 ,$ $\mathrm { U } ^ { \left( v \right) }$ is updated as follows:

$$U ^ { \left( v \right) } \left( t \right) = I + \int _ { 0 } ^ { t } T \left( s \right) U ^ { \left( v - 1 \right) } \left( s \right) d s .$$
(13.22)

If we plot the results of each iteration, we discover that they converge
moving from left to right; on a particular iteration $\mathcal{V} ,$ the $u _ { j }$ have
converged up to some argument $t < T ,$ whereas the remainder or tails
of the functions are still varying, quite often wildly, from one iteration
to the next. This phenomenon is helpful in determining how long one
has to proceed to get total convergence, and can also be useful in
speeding up the algorithm.

Upon convergence, $\mathrm { U }$ contains the solution functions $u _ { j }$ in the first
row, and their successive derivatives in subsequent rows. We can
carry out the integration in (13.22) using the simple trapezoidal rule,
providing that the weight functions are available on a sufficiently fine
grid of argument values.


### 13.5 Constraint functionals $B$


#### 13.5.1 Some constraint examples

We have already noted that, in general, the space of solutions of the
linear differential equation $L x = 0$ is a function space of dimension $m ,$
called the null space of $L .$ We shall assume that the linearly independent
functions $u _ { 1 } , \ldots , u _ { m }$ form a basis of the null space.

Any specific solution of $L x = 0$ then requires $m$ additional pieces of
information about $x .$ For example, we can solve the equation $- y D x +$
$D ^ { 2 } x = 0 ,$ defining a shifted exponential, exactly provided that we are
able to specify that

$$x \left( 0 \right) = 0 \quad a n d \quad D x \left( 0 \right) = 1$$

in which case

$$x \left( t \right) = y ^ { - 1 } e ^ { y t } - 1 .$$

Alternatively, $x \left( 0 \right) = 1$ and $D x \left( 0 \right) = 0$ imply that $x _ { 0 } = 1$ and $\alpha = 0$ in
(13.3), or simply that $x = 1 .$

We introduce the notion of a constraint operator $B$ to specify the
$m$ pieces of information about $x$ that we require to identify a specific
function $x$ as the unique solution to $L x = 0 .$ This operator simply
evaluates $x$ or its derivatives in $m$ different ways. The most important

<!-- PageBreak -->

<!-- PageNumber="232" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->

example is the initial value operator used in the theory of ordinary
differential equations defined over an interval $T = \left[ 0 , T \right] ,$

Initial Operator:
$B _ { I } x = \left[ \begin{array}{} { x \left( 0 \right) } \\ { D x \left( 0 \right) } \\ { : } \\ { D ^ { m - 1 } x \left( 0 \right) } \end{array} \right]$
(13.23)

When $B _ { I } x$ is set to an m-vector, initial value constraints are defined.
In the example above, we considered the two cases $B _ { I } x = \left( 0 , 1 \right) ^ { \prime }$ and
$B _ { I } X = \left( 1 , 0 \right) ^ { \prime } ,$ implying the two solutions given there.

The following boundary value operator is also of great importance
in applications involving LDO's of even degree:

$$B o u n d a r y \quad O p e r a t o r : B B X =$$
(13.24)

Specifying $B _ { B } x = c$ gives the values of $x$ and its first $\left( m \quad - \quad 2 \right) / 2$
derivatives at both ends of the interval of interest.

The periodic constraint operator is defined by

$$\mathrm { P e r i o d i c } \mathrm { O p e r a t o r } = \left[ \begin{array}{} { x \left( T \right) - x \left( 0 \right) } \\ { D x \left( T \right) - D x \left( 0 \right) } \\ { : } \\ { D ^ { m - 1 } x \left( T \right) - D ^ { m - 1 } x \left( 0 \right) } \end{array} \right]$$
(13.25)

Functions satisfying $B _ { P } x = 0$ are periodic up to the derivative $D ^ { m - 1 }$
over $T ,$ and are said to obey periodic boundary conditions.


#### 13.5.2 How $L$ and $B$ partition functions

Whatever constraint operator we use, consider the problem of
expressing any particular function $x$ as a sum of two components $z$ and
$e ,$ such that $L z = 0$ and $B e = 0 .$ When can we carry out this partitioning
in a unique way? This happens if and only if $x = 0$ is the only function
satisfying both $B x = 0$ and $L x = 0 ,$ or, in algebraic notation,

$$\ker B \cap \ker L = 0 .$$
(13.26)

Thus, the two operators $B$ and $L$ complement each other; the equation
$L x = 0$ defines a space of functions $\ker L$ that is of dimension $m ,$ and

<!-- PageBreak -->

<!-- PageNumber="233" -->
<!-- PageHeader="13.5 Constraint functionals $B$" -->

within this space $B$ is a nonsingular transformation. Looking at it the
other way, the equation $B x = 0$ defines a space of functions $\ker B$ of
co-dimension $m ,$ within which $L$ is a one-to-one transformation.

Note that the condition (13.26) can break down. For example,
consider the operator $L = w ^ { 2 } I + D ^ { 2 }$ on the interval $\left[ 0 , T \right] .$ The
space $\ker L$ contains all linear combinations of sin wt and cos wt. If
$w = 2 \pi k / T$ for some integer $k$ and we use boundary constraints, all
multiples of sin wt satisfy $B _ { B } x = 0 ,$ and so the condition (13.26) is
violated. In this case, some functions-those that satisfy $x \left( 0 \right) = x \left( T \right)$
and $D x \left( 0 \right) = D x \left( T \right) - h a s$ infinitely many decompositions as $z + e$ with
$L z = B e = 0 ,$ wheras we will not be able to decompose others at all in
this way.

If we place constraints on the functions under consideration, periodic
boundary conditions for example, then the dimension of ker L may
be less than $m ,$ and $a$ lower dimensional constraint operator is
appropriate. For example, consider the operator $L = w ^ { 4 } I - D ^ { 4 }$ on
the interval $\left[ 0 , T \right] ,$ with $T$ a multiple of $2 \pi / w .$ Then the space of
functions satisfying $L u = 0$ and periodic boundary conditions is 2, and
is spanned by the functions $\sin \omega t$ and cos wt. To specify a function
completely, we would most simply give the values $x \left( 0 \right)$ and $D x \left( 0 \right) ,$ so
an appropriate operator $B$ is defined by $B x = \left( x \left( 0 \right) , D x \left( 0 \right) \right) ^ { \prime } .$ Then the
condition (13.26) is satisfied.


#### 13.5.3 The inner product defined by operators $L$ and $B$

All the functional data analysis techniques and tools in this book
depend on the notion of an inner product between two functions $x$
and $y .$ We have seen numerous examples where a careful choice of
inner product can produce useful results, especially in controlling
the roughness of estimated functions, such as functional principal
components or regression functions. In these and other examples, it is
important to use derivative information in defining an inner product.

Let us assume that the constraint operator is such that condition
(13.26) is satisfied. We can define $a$ large family of inner products as
follows:

$$\langle x , y \rangle _ { B , L } = \left( B x \right) ^ { \prime } \left( B y \right) + \int \left( L x \right) \left( t \right) \left( L y \right) \left( t \right) d t$$
(13.27)

with the corresponding norm

$$\| x \| _ { B , L } ^ { 2 } = \left( B x \right) ^ { \prime } \left( B x \right) + \int \left( L x \right) ^ { 2 } \left( t \right) d t .$$
(13.28)

<!-- PageBreak -->

<!-- PageNumber="234" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->

The condition (13.26) ensures that this is a norm; the only function
$x$ for which $| | x | | _ { B , L } = 0$ is zero itself, since this is the only function
simultaneously satisfying $B x = 0$ and $L x = 0 .$

In fact, this inner product works by splitting the function $x$ into two
parts:

$$x = z + e ,$$
$$z \in \ker L$$
where and $e \in \ker B .$

The first term in (13.28) simply measures the size of the component $z ,$
since $B e = 0$ and therefore $B x = B z ,$ whereas the second term depends
only on the size of the component $e$ since $L x = L e .$ The first term in
(13.27) is essentially an inner product for the m-dimensional subspace
in which $z$ lives and which is defined by $L z = 0 .$ The second term is
an inner product for the function space of codimension $m$ defined by
$B e = 0 .$ Thus, we can write

$$\| x \| _ { B , L } ^ { 2 } = \| z \| _ { B } ^ { 2 } + \| e \| _ { L } ^ { 2 } .$$

With this composite inner product in hand, that is with a particular
LDO $L$ and constraint operator $B$ in mind, we can go back and revisit
each of our functional data analytic techniques to see how they perform
with this inner product. This is the central point explored by Ramsay
and Dalzell (1991), to which we refer the reader for further discussion.


### 13.6 The Green's function for $L$ and $B$


#### 13.6.1 Solving a linear differential equation

Suppose that we want to reverse the effect of applying an mth order
LDO L, that is, we have a forcing function $f$ satisfying

$$L x = f$$
(13.29)

and we want to find $x .$ We can recognise that the solution is not unique;
if we add any linear combination of the functions $u _ { j }$ that span $\ker L$ to
a solution $x ,$ then this function also satisfies the equation. Throughout
this section, assume that the constraint operator $B$ satisfies (13.26).
Then, for any given vector $c ,$ the additional constraints

$$B x = c$$
(13.30)

uniquely specify $x .$ Can we be assured that a solution $x$ exists at all?
If we are using initial value constraints, then under mild regularity
conditions on $f ,$ there is indeed a solution.

<!-- PageBreak -->

<!-- PageNumber="235" -->
<!-- PageHeader="13.6 The Green's function for $L$ and $B$" -->

Let us assume, as is the case for initial value constraints, that the
space $\ker L$ is of dimension $m .$ Define the matrix $B$ in vector notation
by

$$B = B u ^ { \prime } \text { so that } B _ { i j } = \left( B u _ { j } \right) _ { i } .$$
(13.31)

Every $z$ in ker $L$ can be written as $\sum _ { j } a _ { j } u _ { j }$ for an m-vector of coefficients
a, and $B z = B a$ by the definition of $B .$ The conditions we have specified
ensure that $B$ is invertible. In passing we note that $\mathrm { i f }$ we find the
functions $u _ { j }$ by Picard's algorithm as outlined in Section 13.4.3, then $B$
is the identity.

Returning to our constrained problem, set the vector $a = B ^ { - 1 } c$ and
let $z = \sum _ { j } a _ { j } u _ { j } .$ Suppose $e$ satisfies $L e = f$ subject to $B e = 0 ;$ then
$x = z + e$ satisfies $L x = f$ subject to $B x = c .$ Therefore, if we can solve
the problem

$$L x = f \quad s u b j e c t \quad t o \quad x \quad i n \quad k e r \quad B ,$$
(13.32)

we can find a solution subject to the more general constraint $B x = c .$


#### 13.6.2 The Green's function and the solution

It can be shown that there exists a bivariate function $G \left( t ; s \right) ,$ called the
Green's function associated with the pair $\left( B , L \right) ,$ such that

$$x \left( t \right) = \int _ { T } G \left( t ; s \right) L x \left( s \right) d s \text { for } x \text { in } k e r B .$$
(13.33)

Thus the Green's function defines an integral transform $\mathcal{G} = \int G \left( t ; \cdot \right)$
that inverts the linear differential operator $L .$ Applying $\mathcal{G}$ to $L x$ gets us
back to $x$ itself, provided $B x = 0 .$

Furthermore, under mild regularity conditions, $\mathcal{G}$ is the inverse of $L$
in the other sense: If we apply $\mathcal{G}$ to a function $f$ and then $L$ to the result,
we recover the function $f .$ This means that if we set $x = G f ,$ then

$$x \left( t \right) = \int _ { T } G \left( t ; s \right) f \left( s \right) d s ,$$

and we have solved the equation $L x = f$ subject to $B x = 0 ,$ which is
what we set out to do.

Before giving a general recipe for computing the Green's function
$G ,$ let us look at a specific example. If our interval is $\left[ 0 , T \right]$ and our
constraint operator is the initial value constraint $B _ { I } x = x \left( 0 \right) ,$ then for
$L = D ,$

$$G _ { I } \left( t ; s \right) = 1 , s \leq t , \text { and } 0 .$$

where the subscript on $G$ is to remind us that this applies only for the
initial value constraint operator $B _ { I } .$

<!-- PageBreak -->

<!-- PageNumber="236" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->

This follows because

$$\int _ { 0 } ^ { T } G _ { I } \left( t ; s \right) D x \left( s \right) d s = \int _ { 0 } ^ { t } D x \left( s \right) d s = x \left( t \right) - x \left( 0 \right) .$$

Because of the initial value constraint $x \left( 0 \right) = 0 ,$ we finally have the
desired result (13.33).


#### 13.6.3 A recipe for the Green's function

We can now offer a recipe for constructing the Green's function for
any LDO $L$ of the form (13.1) and the initial value constraint $B _ { I }$ of the
corresponding order. First, compute the Wronskian matrix $\mathrm { W }$ defined
in (13.21). Second, define the functions $v _ { 1 } , \ldots , v _ { m }$ to be the elements
of the last row of $W ^ { - 1 } .$ Then, it turns out that

$$G _ { I } \left( t ; s \right) = \sum _ { j = 1 } ^ { m } u _ { j } \left( t \right) v _ { j } \left( s \right) = u \left( t \right) ^ { \prime } v \left( s \right) , s \leq t , \text { and } 0$$
(13.34)

where $v$ is the vector-valued function with components $v _ { j } .$

Let us see how this works for $L = - y D + D ^ { 2 } .$ The space $\ker L$ is
spanned by the two functions $u _ { 1 } \left( t \right) = 1$ and $u _ { 2 } \left( t \right) = \exp y t .$ The
Wronskian matrix is

$$W \left( t \right) = \left[ \begin{array}{} u _ { 1 } \left( t \right) & D u _ { 1 } \left( t \right) \\ u _ { 2 } \left( t \right) & D u _ { 2 } \left( t \right) \end{array} \right] = \left[ \begin{array}{} 1 & 0 \\ \mathrm { e x p } y t & y \mathrm { e x p } y t \end{array} \right]$$

and consequently

$$W ^ { - 1 } \left( t \right) = \left[ \begin{array}{} { 1 } & { 0 } \\ { - y ^ { - 1 } } & { y ^ { - 1 } } \end{array} \text { exp } - y t \right]$$

from which

$$v \left( s \right) = y ^ { - 1 } \left( - 1 , \exp - y s \right) ^ { \prime }$$

and finally

$$G _ { I } \left( t ; s \right) = y ^ { - 1 } \left( e ^ { y \left( t - s \right) } - 1 \right) , s \leq t ,$$
and 0 otherwise.
(13.35)

We can verify that this is the required Green's function by integrating
by parts.

We do not discuss in any detail the case of any constraint functions
$B$ other than initial value constraints. Under boundary or periodic
constraints, it may be that additional conditions are required on the
function $f$ or on the constraint values $c ,$ but nevertheless we can extend
the basic ideas of Green's functions. For details, we refer the reader to
Coddington and Levinson (1955), Roach (1982) or most other texts on
linear differential equations. For more details along the lines we present
in the following section, see Dalzell and Ramsay (1990).

<!-- PageBreak -->

<!-- PageNumber="237" -->
<!-- PageHeader="13.7 Reproducing kernels and Green's functions" -->


## 13.7 Reproducing kernels and Green's functions

A bivariate function called the reproducing kernel plays a central role
in the theory of spline functions. There are two to consider, one for
each of the function subspaces $\ker B$ and $\ker L .$ In the context of these
two subspaces, we shall explain what a reproducing kernel is, and show
how it can be constructed in these specific cases.


### 13.7.1 The reproducing kernel for $\ker B$

Consider, first, the subspace $\ker B$ consisting of functions that satisfy
$B x = 0 .$ The reproducing kernel for this subspace has a simple
relationship to the Green's function $G .$

Given any two functions $x$ and $y$ in $\ker B ,$ let us define the $L$ L-inner
product by

$$\langle x , y \rangle _ { L } = \langle L x , L y \rangle = \int L x \left( s \right) L y \left( s \right) d s .$$

Let $G _ { I }$ be the Green's function as defined in Section 13.6.3, and define
a function $k _ { 2 } \left( t , s \right)$ such that, for all $t$ t,

$$L k _ { 2 } \left( t , \cdot \right) = G _ { I } \left( t ; \cdot \right) \text { and } B k _ { 2 } \left( t , \cdot \right) = 0 .$$
(13.36)

By the defining properties of Green's functions, this means that

$$k _ { 2 } \left( t , s \right) = \int G _ { I } \left( s ; w \right) G _ { I } \left( t ; w \right) d w .$$
(13.37)

The function $k _ { 2 }$ has an interesting property. Suppose that $e$ is any
function in $\ker B ,$ and consider the L-inner product of $k _ { 2 } \left( t , \cdot \right)$ and $e$ e.
For all $t ,$

$$\langle k _ { 2 } \left( t , \cdot \right) , e \rangle _ { L } = \int L k _ { 2 } \left( t , s \right) L e \left( s \right) d s = \int G _ { I } \left( t ; s \right) L e \left( s \right) d s = e \left( t \right) \left( 1 3 . 3 8 \right)$$

by the key property (13.33) of Green's functions. Thus, in the space
$\ker B ,$ taking the $L$ L-inner product of $k _ { 2 }$ regarded as a function of its
second argument with any function $e$ yields the value of $e$ at the first
argument of $k _ { 2 } .$ Thus, taking the inner product with $k _ { 2 }$ reproduces the
function $e ,$ and $k _ { 2 }$ is called the reproducing kernel for this function
space and inner product.

Chapter 15 shows that the reproducing kernel is the key to the
important question, "Is there an optimal set of basis functions for
smoothing data?" To answer this question, we need to use the
important property

$$\langle k _ { 2 } \left( s , \cdot \right) , k _ { 2 } \left( t , \cdot \right) \rangle _ { L } = k _ { 2 } \left( s , t \right) ,$$
(13.39)

<!-- PageBreak -->

<!-- PageNumber="238" -->
<!-- PageHeader="13. Differential operators in functional data analysis" -->

which follows at once from (13.38) setting $e \left( \cdot \right) = k _ { 2 } \left( s , \cdot \right)$ and appealing
to the symmetry of the inner product.

We can put the expression (13.37) in a slightly more convenient form
for the purpose of calculation. Recall the definitions of the vector-
valued functions $u$ and $v$ in Section 13.6.3, and define the order $m$
symmetric matrix-valued function $F \left( s \right)$ as

$$F \left( s \right) = \int _ { 0 } ^ { s } v \left( w \right) v \left( w \right) ^ { \prime } d w .$$
(13.40)

Then, assuming that $s \leq t ,$ the formula (13.34) gives

$$k _ { 2 } \left( s , t \right) = \int _ { 0 } ^ { s } \left[ u \left( s \right) ^ { \prime } v \left( w \right) \right] \left[ v \left( w \right) ^ { \prime } u \left( t \right) \right] d w = u \left( s \right) ^ { \prime } F \left( s \right) u \left( t \right) \quad \left( 1 3 . 4 1 \right)$$

To deal with the case $s > t ,$ we use the property that $k _ { 2 } \left( s , t \right) = k _ { 2 } \left( t , s \right) .$


### 13.7.2 The reproducing kernel for $\ker L$

Now suppose that $f = \sum a _ { i } u _ { i }$ and $g = \sum b _ { i } u _ { i }$ are elements of $\ker L .$
We can consider the B-inner product on the finite-dimensional space
$\ker L ,$ defined by

$$\langle f , g \rangle _ { B } = \left( B f \right) ^ { \prime } B g = a ^ { \prime } B ^ { \prime } B b .$$

Define a function $k _ { 1 } \left( t , s \right)$ by

$$k _ { 1 } \left( t , s \right) = u \left( t \right) ^ { \prime } \left( B ^ { \prime } B \right) ^ { - 1 } u \left( s \right) .$$

Now it is easy to verify that, for any $f = \sum _ { i } a _ { i } u _ { i } ,$

$$\langle k _ { 1 } \left( t , \cdot \right) , f \rangle _ { B } = u \left( t \right) ^ { \prime } \left( B ^ { \prime } B \right) ^ { - 1 } B ^ { \prime } B a = u \left( t \right) ^ { \prime } a = a ^ { \prime } u \left( t \right) = f \left( t \right) .$$

So $k _ { 1 }$ is the reproducing kernel for the space ker L equipped with the
B-inner product.

Finally, we consider the space of more general functions $x$ equipped
with the inner product $\langle \cdot , \cdot \rangle _ { B , L }$ as defined in Section 13.5.3. It is easy to
check from the properties we have set out that the reproducing kernel
in this space is given by

$$k \left( s , t \right) = k _ { 1 } \left( s , t \right) + k _ { 2 } \left( s , t \right) .$$

<!-- PageBreak -->


## 14 Principal differential analysis


### 14.1 Introduction


#### 14.1.1 The basic principle

In this chapter we return to the problem that animated the development
of principal components analysis in Chapter 6: can we use our set of $N$
functional observations $x _ { i }$ to define a much smaller set of $m$ functions
$u _ { j }$ on the basis of which we can obtain efficient approximations of
these observed functions?

What changes here, however, is what we mean by efficient
approximation. In this chapter we consider the identification of a linear
differential operator

$$L = w _ { 0 } I + w _ { 1 } D + \ldots + w _ { m - 1 } D ^ { m - 1 } + D ^ { m }$$
(14.1)

that comes as close as possible to satisfying the homogeneous linear
differential equation $L x _ { i } = 0$ for each observation $x _ { i } .$ Thus, we seek a
differential equation model so that our data satisfy

$$D ^ { m } x _ { i } = - w _ { 0 } x _ { i } - w _ { 1 } D x _ { i } - \ldots - w _ { m - 1 } D ^ { m - 1 } x _ { i }$$

to the best possible degree of approximation.

The term principal differential analysis (abbreviated PDA) is used
for this methodology. This term was introduced in the paper Ramsay
(1996a), on which the treatment of the current chapter is based. The

<!-- PageBreak -->

<!-- PageNumber="240" -->
<!-- PageHeader="14. Principal differential analysis" -->


<figure>
<figcaption>FIGURE 14.1. Twenty records of the position of the centre of the lower lip during the uttering of the syllable "bob." These curves are the result of preliminary smoothing registration steps, and the time unit is arbitrary.</figcaption>

15

10

Position (mm)

5

0

?

-10

0.0

0.2

0.4

0.6

0.8

1.0

Time

</figure>


immediately obvious way of carrying out PDA is to adopt a least squares
approach to the fitting of the differential equation model. Since we wish
the operator $L$ to annihilate the given data functions $x _ { i }$ as nearly as
possible, we regard the function $L x _ { i }$ as the residual error from the fit
provided by the linear differential operator $L .$ As the fitting criterion,
the least squares approach then gives the sum of squared norms

$$S S E _ { P D A } \left( L \right) = \sum _ { i = 1 } ^ { N } \int \left[ L x _ { i } \left( t \right) \right] ^ { 2 } d t ,$$ ☒
(14.2)

which can be minimized over $L$ to find an estimate of the appropriate
LDO. Of course, the operator $L$ is defined by the m-vector $w$
of functions $\left( w _ { 0 } , \ldots , w _ { m - 1 } \right) ^ { \prime } ,$ and so $\mathrm { S S E } _ { \mathrm { P D A } } \left( L \right)$ depends on these
functions, and estimating $L$ is equivalent to estimating the $m$ weight
functions $w _ { i } .$


#### 14.1.2 The need for PDA

There are several reasons why a PDA can provide important
information about the data and the phenomenon under study.
Primarily, in many applications the differential equation $L x = 0$
offers an interesting and useful way of understanding the processes

<!-- PageBreak -->

<!-- PageNumber="241" -->
<!-- PageHeader="14.1 Introduction" -->

that generated the data. As an example to be used throughout this
chapter, consider the curves presented in Figure 14.1. These indicate
the movement of the centre of the lower lip as a single speaker
said the syllable "bob". The time interval has been arbitrarily set to
[0,1], although the actual syllable took about a third of a second. The
displayed curves are the result of considerable preprocessing, including
smoothing and the use of functional PCA to identify the direction in
which most of the motion was found. Details can be found in Ramsay,
Munhall, Gracco and Ostry (1996). In broad terms, we see that the lower
lip motion has three phases: an initial rapid opening, a sharp transition
to a relatively slow and nearly linear motion, and a final rapid closure.

Because the lower lip is part of a mechanical system, with certain
natural resonating frequencies and a stiffness or resistance to
movement, it seems appropriate to explore to what extent this motion
can be expressed in terms of a second order linear differential equation
of the type useful in analysing such systems,

$$L x _ { i } = w _ { 0 } x _ { i } + w _ { 1 } D x _ { i } + D ^ { 2 } x _ { i } = 0 .$$
(14.3)

Discussions of second-order mechanical systems can be found in most
applied texts on ordinary differential equations, such as Tenenbaum
and Pollard (1963).

The first coefficient $w _ { 0 }$ essentially reflects the position-dependent
force applied to the system at position $x .$ Coefficient values $w _ { 0 } > 0$
and $w _ { 1 } = 0$ correspond to a system with sinusoidal or harmonic
motion, with $w _ { 0 } ^ { 1 / 2 } / \left( 2 \pi \right)$ cycles per unit time and wavelength or period
$2 \pi w _ { 0 } ^ { - 1 / 2 }$ $w _ { 0 }$ is often called the spring constant. The second coefficient
$w _ { 1 }$ indicates influences on the system that are proportional to velocity
rather than position and are often internal or external frictional forces
or viscosity in mechanical systems.

The discriminant is defined as $d = \left( w _ { 1 } / 2 \right) ^ { 2 } - w _ { 0 }$ and is critical in
terms of its sign. When the discriminant is negative, the system is
underdamped, and it exhibits oscillation. When $d$ is positive, the system
is overdamped, and either decays to zero or grows exponentially, in
either case without oscillation. A critically damped system is one for
which $d = 0 ,$ and also exhibits nonoscillatory motion. When does the
system exhibit exponential growth or instability? Always if $w _ { 0 } < 0 ,$ and
when $w _ { 1 } < 0$ in the event that $w _ { 0 } > 0 .$ When $w _ { 0 } = w _ { 1 } = 0$ the system
is in linear motion, corresponding to $D ^ { 2 } x = 0 .$

Strictly speaking, these mechanical interpretations of the roles of the
coefficient functions $w _ { 0 }$ and $w _ { 1 }$ are appropriate only if these functions
are constants, but higher-order effects can be ignored if they do not

<!-- PageBreak -->

<!-- PageNumber="242" -->
<!-- PageHeader="14. Principal differential analysis" -->


<figure>
<figcaption>FIGURE 14.2. The two weight functions $w _ { 0 }$ and $w _ { 1 }$ estimated from the lip movement data.</figcaption>

WO

$W 1$

8

20

80

10

80

0

20

-10

0

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Time

Time

</figure>


vary too rapidly with $t .$ In that case the signs of $w _ { 0 } ,$ $w _ { 1 } ,$ and $d$ can be
viewed as describing the instantaneous state of the system.

The techniques we develop were used to obtain the weight functions
displayed in Figure 14.2. These are of rather limited help in interpreting
the system, but one does note that $w _ { 0 }$ is positive except for a brief
episode near the beginning, and near zero in the central portion
corresponding to the near-linear phase of lip movement. The two
solutions to the homogeneous differential equation $L u = 0$ defined
by these weight functions are shown in Figure 14.3.


#### 14.1.3 The relationship to PCA

Once we have found the operator $L ,$ in general we can define $m$
linearly independent functions $u _ { 1 } , \ldots , u _ { m }$ that span the null space of
L. Any function $x$ that satisfies $L x = 0$ can be expressed as a linear
combination of the $u _ { j } .$ Hence, since $L$ has been chosen to make the $L x _ { i }$
as small as possible, we would expect to obtain a good approximation of
the $x _ { i }$ by expanding them in terms of the $u _ { j } .$ This is closely reminiscent
of PCA, where the first $m$ principal component functions $E _ { j }$ form a good
m-dimensional set for approximating the given data. The spirit of the
approximation is rather different, however.

We can pursue the comparison between PCA and PDA by noting that
PCA can also be considered to involve the identification of a linear
operator, which we can denote by $Q ,$ such that the equation $Q x _ { i } = 0$
is solved as nearly as possible. To see this, recall from Chapter 6 that
one method of defining functional PCA is as the determination of $a$ set

<!-- PageBreak -->

<!-- PageNumber="243" -->
<!-- PageHeader="14.1 Introduction" -->

$U 1$

$U 2$


<figure>
<figcaption>FIGURE 14.3. Two solutions of the homogeneous differential equation $L u = 0$ estimated for the lip movement data.</figcaption>

1.0

-0.4 -0.2 0.0 0.2 0.4

0.5

0.0

-0.5

0.0 0.2 0.4 0.6 0.8 1.0

0.0

0.2

0.4

0.6

0.8

1.0

Time

Time

</figure>


of $m$ basis functions $\mathfrak{z} _ { j }$ to minimize the least squares criterion

$$S S E _ { P C A } = \sum _ { i = 1 } ^ { N } \int \left[ x _ { i } \left( t \right) - \sum _ { j = 1 } ^ { m } f _ { i j } S _ { j } \left( t \right) \right] ^ { 2 } d t$$
(14.4)

with respect both to the basis functions $E _ { j }$ and with respect to the
coefficients $f _ { i j }$ of the expansions of each observed function in terms of
these basis functions. Because the minimization of the fitting criterion
(14.4) is a least squares problem, we can think of PCA as a two-stage
process: first identify a set of $m$ orthonormal basis functions $\mathfrak{z} _ { j } ,$ and
then approximate any specific curve $x _ { i }$ by $\widehat { x } _ { i } = \sum _ { j = 1 } ^ { m } f _ { i j } .$ This second
basis expansion step, the projection of each of the observed functions
onto the m-dimensional space spanned by the basis functions $5 ,$ takes
place after determining the optimal basis for these expansions. Thus
$\widehat { x } _ { i }$ is the image of $x _ { i }$ resulting from applying a least squares fit.

Suppose we indicate this projection as $P _ { 5 } ,$ with the subscript
indicating that the nature of the projection depends on the basis
functions $\mathrm { I } _ { \mathrm { S } } ,$ so that $P _ { E } x _ { i } = \widehat { x } _ { i } .$ Associated with the projection $P _ { E }$ is
the complementary projection

$$Q _ { E } = I - P _ { E }$$

which produces as its result the residuals

$$Q _ { 5 } x _ { i } = x _ { i } - P _ { 5 } x _ { i } = x _ { i } - x _ { i } .$$

Using this concept, we can alternatively and equivalently define the
PCA problem in a way that is much more analogous to the problem

<!-- PageBreak -->

<!-- PageNumber="244" -->
<!-- PageHeader="14. Principal differential analysis" -->

of identifying the linear differential operator $L :$ in PCA, one seeks a
projection operator $Q _ { E }$ such that the residual sum of squares

$$S S E _ { P C A } = \sum _ { i = 1 } ^ { N } \int \left[ Q _ { E } x _ { i } \left( t \right) \right] ^ { 2 } d t$$
(14.5)

is minimized. Indeed, one might think of the first $m$ eigenfunctions
as the functional parameters defining the projection operator $Q _ { E } ,$ just
as the weight functions $w$ are the functional parameters of the $\mathrm { L D O } L$
in PDA. These eigenfunctions, and any linear combinations of them,
exactly satisfy the equation $Q _ { 5 } E _ { j } = 0 ,$ just as the $m$ functions $u _ { j }$
referred to above exactly satisfy the equation $L _ { w } u _ { j } = 0 ,$ where we now
add the subscript $w$ to $L$ to remind ourselves that $L$ is defined by the
vector $w$ of $m$ weight functions $w _ { j } .$

Principal differential analysis is defined, therefore, as the identifica-
tion of the operator $L _ { w }$ that minimizes the least squares criterion
$S S E _ { \text { PDA } } ,$ just as we can define PCA as the identification the projection
operator $Q _ { 5 }$ that minimizes the least squares criterion $\mathrm { S S E } _ { \mathrm { P C A } } .$

Since the basic structures of the least squares criteria (14.2) and (14.5)
are the same, clearly the only difference between the two criteria is in
terms of the actions represented by the two operators $L _ { w }$ and $Q _ { \xi } .$ Since
$Q _ { 5 } x$ is in the same vector space as $x ,$ the definition of the operator
identification problem as the minimization of $\| Q _ { 5 } x \| ^ { 2 }$ is also in the
same space, in the sense that we measure the performance of $Q _ { 5 }$ in the
same space as the functions $x$ to which it is applied.

On the other hand, $L _ { w }$ is a roughening transform in the sense that
$L _ { w } x$ has $m$ fewer derivatives than $x$ and is usually more variable. We
may want to penalize or otherwise manipulate $x$ at this rough level.
Put another way, it may be plausible to conjecture that the noise or
unwanted variational component in $x$ is found only at the rough level
$L _ { w } x .$ Thus, a second motivating factor for the use of $L _ { w }$ rather than
$Q _ { 5 }$ is that the PDA process explicitly takes account of the smoothness
of the data by first roughening the data before minimizing error, while
PCA does not.

As an example, imagine that we are analysing the trajectories $x _ { i }$ of
several rockets of the same type launched successively from some site.
We observe that not all trajectories are identical, and we conjecture
that some random process is at work that contributes variability to
our observations. Naïvely, we might look for that variability in the
trajectories themselves, but our friends in physics will be quick to
point out firstly that the major source of variability is probably in
the propulsion system, and secondly since the force that it applies
is proportional to acceleration, we ought to study the acceleration

<!-- PageBreak -->

<!-- PageNumber="245" -->
<!-- PageHeader="14.1 Introduction" -->

$D ^ { 2 } x _ { i }$ instead. Thus, if the function $x _ { i }$ is the trajectory along a specific
coordinate axis (straight up, for example), the systematic or errorless
trajectory should obey the law

$$f _ { i } \left( t \right) = M \left( t \right) D ^ { 2 } x _ { i } \left( t \right) ,$$

where $M \left( t \right)$ is the mass of the rocket at time $t .$ Alternatively,

$$- f _ { i } / M + D ^ { 2 } x _ { i } = 0 .$$

Taking a more empirical approach, however, we agree on the
compromise of looking for a second-order linear differential equation

$$L x = w _ { 0 } x + w _ { 1 } D x + D ^ { 2 } x$$

and, if our friends in physics are right, the systematic or errorless
component in the data should yield

$$w _ { 0 } x _ { i } = - f _ { i } / M \text { and } w _ { 1 } = 0 .$$

What we do understand, in any case, is that the sources of variability
are likely to be at the rough level $D ^ { 2 } x _ { i } ,$ rather than at the raw trajectory
level $x _ { i } .$

Returning to the lip position curves, we might reason that variation
in lip position from curve to curve is due to variation in the forces
resulting from muscle contraction, and that these forces have a direct
or proportional impact on the acceleration of the lip tissue, and thus
only indirectly on the position itself. In short, position is two derivatives
away from the action.

More generally, an important motivation for finding the operator
$L _ { w }$ is substantive: applications in the physical sciences, engineering,
biology and elsewhere often make extensive use of differential equation
models of the form

$$L x _ { i } = f _ { i } .$$

The result $f _ { i }$ is often called a forcing or impulse function, and in physical
science and engineering applications is often taken to indicate the
influence of exogenous agents on the system defined by $L x = 0 .$

Section 14.2 presents techniques for principal differential analysis,
along with some measures of fit to the data. We also take up the
possibility of regularizing or smoothing the estimated weight functions
$w _ { j } .$

<!-- PageBreak -->

<!-- PageNumber="246" -->
<!-- PageHeader="14. Principal differential analysis" -->


<figure>
<figcaption>FIGURE 14.4. The left panel displays the acceleration curves $D ^ { 2 } x _ { i }$ for the lip position data, and the right panel the forcing functions $L x _ { i } .$</figcaption>

Acceleration

Forcing functions

1000

1000

0

0

-1000

-1000

0.0

0.2

0.4

0.6

0.8

1.0

0.0

0.2

0.4

0.6

0.8

1.0

Time

Time

</figure>


#### 14.1.4 Visualizing results

One way to get a visual impression of how effective the differential
operator $L$ is at annihilating variation in the $x _ { i }$ is to plot the empirical
forcing functions $L x _ { i } .$ If these are small and mainly noise-like, we can
have some confidence that the equation represents the data well. As a
point of comparison, we can use the size of the $D ^ { m } x _ { i } ,$ since these are
the empirical forcing functions corresponding to $w _ { 0 } = \ldots = w _ { m - 1 } = 0 .$
Figure 14.4 shows the acceleration curves for the lip data in the left
panel, and the empirical forcing functions in the right. We see that
the forcing functions corresponding to $L$ are indeed much smaller in
magnitude, and more or less noise-like except for two bursts of signal
near the beginning and end of the time interval.

The value of the criterion $\mathrm { S S E } _ { \mathrm { P D A } }$ defined above is $6 . 0 6 \times 1 0 ^ { 6 } ,$ whereas
the same measure of the size of the $D ^ { 2 } x _ { i }$ is $4 0 . 6 7 \times 1 0 ^ { 6 } .$ If we call the
latter measure $\mathrm { S S Y } _ { \mathrm { P D A } } ,$ then we can also summarize these results in the
squared correlation measure

$$R S Q _ { p _ { D A } } = \left( S S Y _ { p _ { D A } } - S S E _ { p _ { D A } } \right) / S S Y _ { P D A }$$
(14.6)

whose value is 0.85 for this problem.

Although, strictly speaking, it is not the task of PDA to approximate
the original curves (this would be a job for PCA), we can nevertheless
wonder how well the two solution curves would serve this purpose.
Figure 14.5 shows the least squares approximation of the first two
curves in terms of the two solution functions in Figure 14.3, and we
see that the fit is fairly satisfactory.

<!-- PageBreak -->

<!-- PageNumber="247" -->
<!-- PageHeader="14.2 PDA techniques" -->


<figure>
<figcaption>FIGURE 14.5. The solid curves are the first two observed lip position functions, and the dashed lines are their approximations on the basis of the two solution functions in Figure 14.3.</figcaption>

Curve 1

Curve 2

10

10

Position (mm)

5

Position (mm)

5

0

0

-5

4?

0.0

0.2

0.4

0.6

0.8

1.0

0.0

0.2

0.4

0.6

0.8

1.0

Time

Time

</figure>


Finally, we return to the discriminant function $d = \left( w _ { 1 } / 2 \right) ^ { 2 } - w _ { 0 } ,$
presented in Figure 14.6, and its interpretation. This system is more
or less critically damped over the interval $0 . 5 \leq t \leq 0 . 7 5 ,$ suggesting
that its behaviour may be under external control. But in the vicinities
of $t = 0 . 2 5$ and $t = 0 . 8 5 ,$ the system is substantially underdamped, and
thus behaves locally like a spring. The period of the spring would be
around 30 to 40 msec, and this is in the range of values estimated in
studies of the mechanical properties of flaccid soft tissue. These results
suggest that the external input to lip motions tends to be concentrated
in the brief period near $t = 0 . 6 ,$ when the natural tendency for the lip
to close is retarded to allow the articulation of the vowel.


### 14.2 PDA techniques

Now we turn to two techniques for estimating the weight functions
$w _ { j }$ defining the linear differential operator that comes closest to
annihilating the observed functions in the sense of criterion (14.2).

Once the operator $L$ has been computed by estimating its weight
functions $w _ { j }$ by one of these methods, we may be interested in
computing a set of $m$ linearly independent basis functions $u _ { j }$ satisfying
$L u _ { j } = 0 .$ A variety of numerical techniques can be found in standard
references on numerical methods, such as Stoer and Bulirsch (1980).
The successive approximation or Picard's method, described in Chapter
13, works well in most situations.

<!-- PageBreak -->

<!-- PageNumber="248" -->
<!-- PageHeader="14. Principal differential analysis" -->


<figure>
<figcaption>FIGURE 14.6. The discriminant function $d = \left( w _ { 1 } / 2 \right) ^ { 2 } - w _ { 0 }$ for the second order differential equation describing lip position.</figcaption>

Discriminant

200

100

0

-100

-200

0.0

0.2

0.4

0.6

0.8

1.0

Time

</figure>


#### 14.2.1 PDA by pointwise minimization

The first approach yields a pointwise estimate of the weight functions
$w _ { j }$ computable by standard least squares estimation. Define the
pointwise fitting criterion

$$\mathrm { P S S E } _ { L } \left( t \right) = N ^ { - 1 } \sum _ { i } \left( L x _ { i } \right) ^ { 2 } \left( t \right) = N ^ { - 1 } \sum _ { i } \left[ \sum _ { j = 0 } ^ { m } w _ { j } \left( t \right) \left( D ^ { j } x _ { i } \right) \left( t \right) \right] ^ { 2 } \quad \left( 1 4 . 7 \right)$$

where, as above, $w _ { m } \left( t \right) = 1$ for all $t .$ If $t$ is regarded as fixed, the
following argument shows that this is simply a least squares fitting
criterion.

First define the m-dimensional coefficient vector as

$$w \left( t \right) = \left( w _ { 0 } \left( t \right) , \ldots , w _ { m - 1 } \left( t \right) \right) ^ { \prime } ,$$

the $N \times m$ pointwise design matrix as

$$Z \left( t \right) = \left\{ \left( D ^ { j } x _ { i } \right) \left( t \right) \right\} _ { i = 1 , \ldots , N ; j = 0 , \ldots , m - 1 }$$

and the N-dimensional dependent variable vector as

$$y \left( t \right) = \left\{ - \left( D ^ { m } x _ { i } \right) \left( t \right) \right\} _ { i = 1 , \ldots , N } .$$

We can express the fitting criterion (14.7) in matrix terms as

$$\mathrm { P S S E } _ { L } \left( t \right) = N ^ { - 1 } \left[ y \left( t \right) - Z \left( t \right) w \left( t \right) \right] ^ { \prime } \left[ y \left( t \right) - Z \left( t \right) w \left( t \right) \right] .$$

<!-- PageBreak -->

<!-- PageNumber="249" -->
<!-- PageHeader="14.2 PDA techniques" -->

Then, holding $t$ fixed, the least squares solution minimizing $\mathrm { P S S E } _ { L } \left( t \right)$
with respect to the values $w _ { j } \left( t \right)$ is

$$w \left( t \right) = \left[ Z \left( t \right) ^ { \prime } Z \left( t \right) \right] ^ { - 1 } Z \left( t \right) ^ { \prime } y \left( t \right) .$$
(14.8)

The existence of these pointwise values $w \left( t \right)$ depends on the
condition that the determinant of $Z \left( t \right) ^ { \prime } Z \left( t \right)$ is bounded away from zero
for all values of $t ,$ and it is wise to compute and display this determinant
as a routine part of the computation. Assuming that the determinant
is nonzero is equivalent to assuming that $Z \left( t \right)$ is of full column rank
for all $t .$

Of course, if $m$ is not large, then we can express the solution in closed
form. For example, for $m =$ 1,

$$w _ { 0 } \left( t \right) = - \sum _ { i } x _ { i } \left( t \right) \left( D x _ { i } \right) \left( t \right) / \sum _ { i } x _ { i } ^ { 2 } \left( t \right)$$
(14.9)

and the full-rank condition merely requires that, for each value of $t ,$
some $x _ { i } \left( t \right)$ be nonzero.

Some brief comments about the connections with Section 13.4 are
in order. There, we were concerned with finding a linear operator of
order $m$ that annihilated a set of exactly $m$ functions $u _ { i } .$ For this
to be possible, an important condition was the nonsingularity of the
Wronskian matrix values $\mathrm { W } \left( t \right)$ whose elements were $D ^ { j } u _ { i } \left( t \right) .$ We obtain
the matrix $\mathrm { Z } \left( t \right)$ from the functions $x _ { i }$ in the same way, but it is no longer
a square matrix, because $N > m$ in general. However, the condition that
$Z \left( t \right)$ is of full column rank is entirely analogous.


#### 14.2.2 PDA by basis expansions

The pointwise approach can pose problems in some applications. First,
solving the equation $L u = 0$ requires that the $w _ { j }$ be available at a
fine level of detail, with the required resolution depending on their
smoothness. Whether or not these functions are smooth depends in
turn on the smoothness of the derivatives $D ^ { j } x _ { i } .$ Since we often estimate
these derivatives by smoothing procedures that may not always yield
smooth estimates for higher order derivatives, the resolution we
require may be very fine indeed. But for larger orders $m ,$ computing the
functions $w _ { j }$ pointwise at a fine resolution level can be computationally
intensive, since we must solve a linear equation for every value of $t$
for which $w$ is required. This suggests the need for an approximate
solution which can be computed quickly and which is reasonably
regular or smooth.

<!-- PageBreak -->

<!-- PageNumber="250" -->
<!-- PageHeader="14. Principal differential analysis" -->

Second, it may be desirable to circumvent the restriction that the
rank of $Z$ be full, especially if the failure is highly localized within the
interval of integration. As a rule, an isolated singularity for $Z \left( t \right) ^ { \prime } Z \left( t \right)$
corresponds to an isolated singularity in one or more weight functions
$w _ { j } ,$ and it may be desirable to bypass these by using weight functions
sure to be sufficiently smooth. More generally, we may seek weight
functions smoother or more regular than those resulting from the
pointwise solution.

$A$ strategy for identifying smooth weight functions $w _ { j }$ is to
approximate them by using a fixed set of basis functions. Let $\phi _ { k } , k =$
$1 , \ldots , K$ be a set of $K$ such basis functions, and let $\phi$ denote the $K -$
dimensional vector function $\left( \phi _ { 1 } , \ldots , \phi _ { K } \right) ^ { \prime } .$ We may use standard basis
families such as polynomials, Fourier series, or $B$ B-spline functions with
a fixed knot sequence, or we may employ a set of basis functions
suggested by the application at hand. In any case, we assume that

$$w _ { j } \approx \sum _ { k } c _ { j k } \phi _ { k }$$
(14.10)

where the $m K$ coefficients $c _ { j k }$ define the approximations, and require
estimation from the data. Let the (mK)-vector $c$ contain these
coefficients, where index $k$ varies inside index $j .$

We can express or approximate the criterion $\mathrm { S S E } _ { \mathrm { P D A } } \left( L \right)$ in terms of $c$
as a quadratic form $\widehat { F } \left( c \right)$ that can be minimized by standard numerical
algebraic techniques. We have

$$\widehat { F } \left( c | x \right) = C + c ^ { \prime } R c + 2 c ^ { \prime } s$$
(14.11)

where the constant $C$ does not depend on $c ,$ and hence the estimate $\widehat { \mathcal{C} }$
is given by the solution of the equation $R c = - \quad s .$

The symmetric matrix $\mathbb{R}$ in (14.11) is of order $m K ,$ and consists of an
$m \times m$ array of $K \times K$ submatrices $\mathbb{R} _ { j k }$ of the form

$$R _ { j k } = N ^ { - 1 } \int \phi \left( t \right) \phi \left( t \right) ^ { \prime } \sum _ { i } D ^ { j } x _ { i } \left( t \right) D ^ { k } x _ { i } \left( t \right) d t .$$
(14.12)

for $0 \leq j ,$ $k \leq m - 1 .$ Similarly, the $\left( m K \right) - v e c t o r$ $\mathcal{S}$ contains $m$ subvectors
$s _ { j }$ each of length $K ,$ defined as

$$s _ { j } = N ^ { - 1 } \int \phi \left( t \right) \sum _ { i } D ^ { j } x _ { i } \left( t \right) D ^ { m } x _ { i } \left( t \right) d t .$$
(14.13)

for $j = 0 , \ldots , m - 1 .$

The integrals involved in these expressions often have to be evaluated
numerically. For example, it may suffice to use the trapezoidal rule over
a fine mesh of equally-spaced values of $t .$

<!-- PageBreak -->

<!-- PageNumber="251" -->
<!-- PageHeader="14.2 PDA techniques" -->


#### 14.2.3 Regularized PDA

The expansion of $w _ { j }$ in terms of a fixed number of basis functions
can be considered a type of regularization process in the sense that
we can use the number, choice and smoothness of the basis functions
$\phi _ { k }$ to ensure two potentially desirable features: a smooth or regular
variation in $w _ { j } ,$ and the closeness of the estimated $w _ { j }$ to some target
or hypothesized weight function $w _ { j } .$

An alternative type of regularization of $w _ { j } ,$ used repeatedly in this
book, is to attach penalty terms to the criterion (14.2). One version is

$$\mathrm { P E N S S E } _ { \mathrm { P D A } } \left( L \right) = N ^ { - 1 } \sum _ { i } \int L x _ { i } \left( t \right) ^ { 2 } d t + \sum _ { j = 0 } ^ { m - 1 } \lambda _ { j } \int w _ { j } \left( t \right) ^ { 2 } d t . \quad \left( 1 . 1 . 1 \right) .$$
(14.14)

The scalars $\lambda _ { j } ,$ control the roughness of the estimated weight functions.
Large values for all $\lambda _ { j }$ shrink all of the weight functions to 0, with
the result that the differential operator converges to $L = D ^ { m } ,$ and the
functions that satisfy $L x = 0$ are the polynomials of degree $m \quad - \quad 1$ or
less-an interesting analogy with spline smoothing with operator $D ^ { m } ,$
where the same functions are regarded as hypersmooth.

If we use the particular roughness penalty of (14.14), then
minimizing $\mathrm { P E N S S E } _ { \mathrm { P D A } } \left( L \right)$ is straightforward. One possibility is to
proceed pointwise, as in Section 14.2.1, adding the extra term
$w \left( t \right) ^ { \prime } \Lambda w \left( t \right)$ to $P S S E _ { L } \left( t \right) ,$ where $\Lambda = \mathrm { d i a g } \left( \lambda _ { 0 } , \ldots , \lambda _ { m - 1 } \right) .$ The resulting
estimates of the weight functions are given by

$$\widehat { w } \left( t \right) = \left[ Z \left( t \right) ^ { \prime } Z \left( t \right) + N \Lambda \right] ^ { - 1 } Z \left( t \right) ^ { \prime } y \left( t \right) .$$

Alternatively-whatever the roughness penalty-we can use a basis
expansion approach. We add an extra quadratic term to $\widehat { F } \left( c | x \right)$ in
(14.11), corresponding to the expression of the roughness penalty in
terms of the coefficients $c _ { j k } .$


#### 14.2.4 Assessing $f i t$

Since the objective of PDA is to minimize the norm ||Ly|| of the forcing
function associated with an estimated differential operator, and since
the quality of fit can vary over the domain $T ,$ it seems appropriate to
assess fit in terms of the pointwise error sum of squares $P S S E _ { L } \left( t \right)$ as
defined in (14.7). As in linear modelling, the logical baseline against
which we should compare $\mathrm { P S S E } _ { L }$ is the error sum of squares defined
by a theoretical model and its associated weight functions $w _ { j } :$

$$\mathrm { P S S E } _ { 0 } \left( t \right) = \sum _ { i } \left[ \sum _ { j = 0 } ^ { m - 1 } \omega _ { j } \left( t \right) \left( D ^ { j } \mathcal{Y} _ { i } \right) \left( t \right) + \left( D ^ { m } \mathcal{Y} _ { i } \right) \left( t \right) \right] ^ { 2 } .$$
(14.15)

<!-- PageBreak -->

<!-- PageNumber="252" -->
<!-- PageHeader="14. Principal differential analysis" -->


<figure>
<figcaption>FIGURE 14.7. Twenty recordings of the force exerted by the thumb and forefinger during $a$ brief squeeze of a force meter. The data have been preprocessed to register the functions and remove some shape variability, and the values displayed are for the 33 values $t = 0 . 4 \left( 0 . 0 5 \right) 2 . 0 .$</figcaption>

10

8

Force (N)

6

\*

2

O

0.5

1.0

1.5

2.0

Standardized time

</figure>


In the event that there is no theoretical model at hand, we may use
$w _ { j } = 0 ,$ so that the comparison is simply with the sum of squares of
the $D ^ { m } y _ { i } .$ From these loss functions, we may examine the pointwise
squared multiple correlation function

$$R S Q \left( t \right) = \frac { P S S E _ { 0 } \left( t \right) - P S S E _ { L } \left( t \right) } { P S S E _ { 0 } \left( t \right) }$$
(14.16)

and the pointwise $F$ F-ratio

$$\mathrm { F R A T I O } \left( t \right) = \frac { \left( P S S E _ { 0 } \left( t \right) - P S S E _ { L } \left( t \right) \right) / m } { P S S E _ { 0 } \left( t \right) / \left( N - m \right) }$$
(14.17)


### 14.3 PDA of the pinch force data

In this section we take up an example in which the estimated linear
differential operator is compared with a theoretically defined operator.
Further applications of these general ideas are considered in Chapter
15. The data in this example consisted of the 20 records of brief
force impulses exerted by the thumb and forefinger in the experiment
in motor physiology described in Section 1.4.2. For the purposes of

<!-- PageBreak -->

<!-- PageNumber="253" -->
<!-- PageHeader="14.3 PDA of the pinch force data" -->


<figure>
<figcaption>FIGURE 14.8. The left figure contains the data values for the first record (the points), the smoothing spline (solid curve), and the least squares fit by the model (14.18) (dotted curve). The right display shows the residuals arising from fitting the points by a spline function (the points) and the difference between the theoretical model and the spline (solid curve).</figcaption>

10

0.2

8

0.1

Force (N)

Force residual (N)

0.0

\+

-0.1

2

0

-0.2

0.5

1.0

1.5

2.0

0.5

1.0

1.5

2.0

Standardized time

Standardized time

</figure>


this discussion, the force impulses were preprocessed to transform
time linearly to a common metric and to remove some simple shape
variation. The resulting curves are displayed in Figure 14.7. Details of
the preprocessing stages can be found in Ramsay, Wang and Flanagan
(1995).

There are some theoretical considerations which suggest that the
model

$$y _ { i } \left( t \right) = C _ { i } \exp \left[ - \log ^ { 2 } t / \left( 2 \sigma ^ { 2 } \right) \right]$$
(14.18)

offers a good account of any specific force function. In this application,
the data were preprocessed to conform to a fixed shape parameter $\sigma ^ { 2 }$
of 0.05. Functions of the form (14.18) are annihilated by the differential
operator $L _ { 0 } = \left[ \left( t \sigma \right) ^ { - 1 } \log t \right] I + D .$ A goal of this analysis is to compare
this theoretical operator with the first order differential operator $L =$
$w _ { 0 } I + D$ estimated from the data, or to compare the theoretical weight
function $w _ { 0 } \left( t \right) = \left( t \sigma \right) ^ { - 1 } \log t$ with its empirical counterpart $w _ { 0 } .$

We spline smoothed the records, penalizing by the integral of the
square of the third derivative to get a smooth first derivative estimate.
It is clear from Figure 14.7 that the size of error variation is not constant
over time. Accordingly, we estimated the residuals in a first smoothing
step, and smoothed the logs of their standard deviations to estimate
the variation of the typical residual size over time. Then we took the

<!-- PageBreak -->

<!-- PageNumber="254" -->
<!-- PageHeader="14. Principal differential analysis" -->

WO


<figure>
<figcaption>FIGURE 14.9. The weight function estimated by the basis expansion method for the pinch force data is indicated by the solid line, the theoretical function by the dotted line, and the pointwise estimates by the dots.</figcaption>

10

O

·10

-20 -

8

?

0.5

1.0

1.5

2.0

Standardized time

</figure>


weights $\sigma _ { j } ^ { 2 }$ in the weighted spline smoothing criterion

$$P E N S S E _ { \lambda } \left( x | y \right) = \sum _ { j } \left\{ y _ { j } - x \left( t _ { j } \right) \right\} ^ { 2 } / \sigma _ { j } ^ { 2 } + \lambda \| D ^ { 3 } x \| ^ { 2 }$$
(14.19)

to be the squares of the exponential-transformed smooth values.
Finally, we re-smoothed the data to get the spline smoothing curves
and their derivatives.

Figure 14.8 displays the discrete data points, the smoothing function,
and also the theoretical function (14.18) fit by least squares for a single
record. The theoretical function fits very well, but in the right panel
we see that the discrepancy between the theoretical model and the
smoothing spline fit is itself smooth and of the same order as the
largest deviations of the points from this flexible spline fit. Although
this discordance between the model and the spline is less than 2% of
the size of the force itself, we are entitled to wonder if this theoretical
model can be improved.

We applied both the pointwise and basis expansion procedures for
estimating $w _ { 0 }$ to the smooth functions and their derivatives. The basis
used for the basis expansion procedure was

$$\phi \left( t \right) = \left( t ^ { - 1 } \log t , 1 , t - 1 , \left( t - 1 \right) ^ { 2 } \right) ^ { \prime } ,$$

<!-- PageBreak -->

<!-- PageNumber="255" -->
<!-- PageHeader="14.3 PDA of the pinch force data" -->


<figure>
<figcaption>FIGURE 14.10. The left panel displays the forcing or impulse functions $L y _ { i }$ produced by the theoretical operator, and the right panel shows the corresponding empirical operator functions.</figcaption>

Theoretical

Estimated

-6 -4 -2 0 2 4 6

-6 -4 -2 0 2 4 6

0.5 1.0 1.5 2.0

0.5

1.0

1.5

2.0

Standardized time

Standardized time

</figure>


<figure>
<figcaption>FIGURE 14.11. The solid line indicates the square root of the mean squared forcing function for the estimated operator, and the dotted line the same quantity for the theoretical operator.</figcaption>

3.0

RMSE of forcing functions

2.5

2.0

1.5

1.0

0.5

0.0

0.5

1.0

1.5

2.0

Standardized time

</figure>


<!-- PageBreak -->

<!-- PageNumber="256" -->
<!-- PageHeader="14. Principal differential analysis" -->

chosen after some experimentation; the first basis function was
suggested by the theoretical model, and the remaining polynomial
terms served to extend this model as required. Figure 14.9 shows
the theoretical, the pointwise, and the global estimates of the weight
functions. These are admittedly close to one another, at least in the
central ranges of adjusted time, but again we observe some slight but
consistent differences between the theoretical and empirical weight
functions.

However, the forcing functions $L y _ { i } ,$ displayed in Figure 14.10, show
a systematic trend for the theoretical operator, whereas the empirical
forcing functions exhibit much less pattern. Figure 14.11 displays
the root-mean-squares of the two sets of forcing functions, and this
permits us to see more clearly that the estimated operator is superior
in the periods just before and after the peak force, where it produces
a forcing function about half the size of its theoretical counterpart.
It seems appropriate to conclude that the estimated operator has
produced an important improvement in fit on either side of the time
of maximum force. Ramsay, Wang and Flanagan (1995) conjecture that
the discrepancy between the two forcing functions is due to drag or
viscosity in the thumb-forefinger joint.

<!-- PageBreak -->


## 15 More general roughness penalties


### 15.1 Introduction


#### 15.1.1 More general roughness penalties and L-splines

A theme central to this book has been the use of roughness penalties to
incorporate smoothing, whether in the context of using discrete data to
define a smooth function in Chapter 3, functional principal components
analysis in Chapter 7, or imposing regularity on estimated regression
functions in Chapter 10 or on canonical variate weight functions in
Chapter 12.

At the same time, the previous two chapters have dealt with
the mathematical properties of linear differential operators $L$ and
with techniques for estimating them from data. Principal differential
analysis provides a method of estimating low-dimensional functional
variation in a sense analogous to principal components analysis, but
by estimating an m-th order differential operator $L$ rather than a
projection.

Moreover, we have seen that by coupling $L$ with a suitable set of
constraints on the $m$ linearly independent functions $u _ { j }$ satisfying
$L u _ { j } = 0 ,$ we can partition the space of smooth functions into two parts.
This is achieved by defining a constraint operator $B$ such that $B u _ { j } \neq 0 ,$
and that the only function satisfying $B x = L x = 0$ is $x = 0 .$ Then any

<!-- PageBreak -->

<!-- PageNumber="258" -->
<!-- PageHeader="15. More general roughness penalties" -->

function $x$ having $m$ derivatives can be expressed uniquely as

$$x = u + e \quad w h e r e \quad L u = 0 \quad a n d \quad B e = 0 .$$
(15.1)

We might call this the partitioning principle.

It is time to put these two powerful ideas together, to see what
practical value there is in using the partitioning principle to define
a roughness penalty. We want to go beyond the standard practice of
defining roughness in terms of $L = D ^ { 2 } ,$ and even beyond the slightly
more general $L = D ^ { m } ,$ to consider what the advantages of using
an arbitrary operator $L$ might be, perhaps in conjunction with some
constraints captured in the companion operator $B .$ Specifically, when
the goal is smoothing the data, we propose using the criterion

$$= \sum _ { j } ^ { n } \left[ y _ { j } - x \left( t _ { j } \right) \right] ^ { 2 } + \lambda \times P E N _ { L } \left( x \right)$$ ☒ ☒
(15.2)

where

$$P E N _ { L } \left( x \right) = \int \left( L x \right) ^ { 2 } \left( t \right) d t .$$

We begin with some examples.


#### 15.1.2 The lip movement data

Consider the lip movement data introduced in Chapter 14.1.2 and
plotted in Figure 14.1. We are interested in how these trajectories,
all based on observations of a speaker saying "bob", vary from
one replication to another. But in the experiment, the syllable was
embedded in the phrase, "Say bob again," and it is clear that the lower
lip enters and leaves the period during which the syllable is being
formed at different heights. This is nuisance variation that we would
be happy to eliminate.

Moreover, there was particular interest in the acceleration or second
derivative of the lip, suggesting that we should penalize the fourth
derivative by spline smoothing with $L = D ^ { 4 } .$ Any cubic polynomial
trend in the records is ignored if we do that. Now we want to define the
shape component $u$ and endpoint component $e$ of each record $x$ so that
the behaviour of the record at the beginning and end of the interval of
observation (normalized to be $\left. \left[ 0 , 1 \right] \right)$ has minimal impact on the interior
and more interesting portion of the curve. One way of achieving this
objective is to require that shape components satisfy the constraints
$e \left( 0 \right) = D e \left( 0 \right) = 0$ and $e \left( 1 \right) = D e \left( 1 \right) = 0 .$ This means that the chosen
constraint operator is $B _ { E } ,$ defined as

$$B _ { E } x = \left[ x \left( 0 \right) , D x \left( 0 \right) , x \left( 1 \right) , D x \left( 1 \right) \right] ^ { \prime } ,$$
(15.3)

<!-- PageBreak -->

<!-- PageNumber="259" -->
<!-- PageHeader="15.1 Introduction" -->


<figure>
<figcaption>FIGURE 15.1. The right panel displays the 20 cubic polynomials $u$ that match the lip position and derivative values at 0 and 1 for the smoothed versions of the curves in Figure 14.1. The left panel shows the shape components $e$ that have zero endpoint positions and derivatives.</figcaption>

Shape component

End component

0

Position (mm)

4?

Position (mm)

2 4 6 8 10 12 14

-10

-15

-20

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Time

Time

</figure>


and the shape component $e$ satisfies $B _ { E } e = 0 .$

We now have our two linear operators $L = D ^ { 4 }$ and $B = B _ { E }$ in hand,
and they are complementary in the sense that ker B n ker $L = 0 .$ We can
therefore unambiguously split any lip position record $x$ into $x = u + e ,$
where $B e = 0 ,$ and $u ,$ a cubic polynomial because $L u = D ^ { 4 } u = 0 ,$ picks
up the endpoint variation by fitting the record's function and derivative
values at both 0 and 1. Figure 15.1 displays the endpoint and shape
components for all 20 records.


#### 15.1.3 The weather data

In the introduction we noted that a rather large part of the mean daily
or monthly temperature curve for any weather station can be captured
by the simple function

$$T \left( t \right) = c _ { 1 } + c _ { 2 } \sin \left( \pi t / 6 \right) + c _ { 3 } \cos \left( \pi t / 6 \right)$$
(15.4)

and the same may be said for the log precipitation profiles. Functions
of this form can be annihilated by the operator

$$L = \left( \pi / 6 \right) ^ { 2 } D + D ^ { 3 } .$$

We could propose smoothing data using the criterion (15.2), where

$$P E N _ { L } \left( x \right) = \int _ { 0 } ^ { 1 2 } \left( L x \right) ^ { 2 } \left( t \right) d t = \int _ { 0 } ^ { 1 2 } \left\{ \left( \pi / 6 \right) ^ { 2 } D x \left( t \right) + D ^ { 3 } x \left( t \right) \right\} ^ { 2 } d t$$ ☒

<!-- PageBreak -->

<!-- PageNumber="260" -->
<!-- PageHeader="15. More general roughness penalties" -->


<figure>
<figcaption>FIGURE 15.2. The solid cycles are the smoothed daily temperature and log precipitation data, plotted against each other, for two Canadian weather stations. The dotted curves are the estimated cycles based on strictly sinusoidal variation, taking the first three terms of the Fourier expansion of each observed temperature and log precipitation curve. Letters indicate the middle of each month.</figcaption>

Log average precipitation (mm)

1.0

O

S

Prince Rupert

0.5

$\oint$

0.0

Edmonton

-0.5

-20

-10

0

10

20

Average temperature (deg C)

</figure>


while paying attention to the periodic character of the data. What
would we gain from this? For one thing, as we have already noted in
Section 13.3.2, this procedure is likely to have considerable advantages
in estimating curves $x$ from raw data.

At the same time, the function LTemp in this example is interesting
in itself, and Ramsay and Dalzell (1991) refer to it as the harmonic
acceleration of temperature. By functional principal components and
linear regression analyses, they show that $L T e m p$ and the harmonic
acceleration of $\log$ precipitation contain a great deal of information
about the peculiarities of weather at any station. To identify the
component $e$ uniquely, though, we must choose a matching constraint
operator $B ,$ and for this application they chose

$$B x = \left[ \int x \left( t \right) d t , \int x \left( t \right) \sin \left( \pi t / 6 \right) d t , \int x \left( t \right) \cos \left( \pi t / 6 \right) d t \right] ^ { \prime }$$

corresponding to the first three Fourier coefficients of the observed
curves. The three functions $u _ { i }$ that span ker $B$ are then 1, $\sin \left( \pi t / 6 \right)$ and
$\cos \left( \pi t / 6 \right) .$ Given any curve $x ,$ the partition (15.1) is achieved by setting

<!-- PageBreak -->

<!-- PageNumber="261" -->
<!-- PageHeader="15.2 The optimal basis for spline smoothing" -->

the component $u$ to be the first three terms in the Fourier expansion
of $x .$

For two weather stations, the solid curves in Figure 15.2 show plots of
smoothed daily temperature against smoothed daily log precipitation
through the year. When plotted against one another, the shifted
sinusoidal components $u \left( t \right)$ for temperature and log precipitation for
each station become ellipses, shown as dotted curves.


### 15.2 The optimal basis for spline smoothing

In Section 3.2 we reviewed the classic technique of representing
functions by fitting a basis function expansion to the data. We took
pains to point out that not all bases are equal; a good basis consists
of functions which mimic the general features that we know apply to
the data, such as periodicity, asymptotic linearity, and so on. When we
get these features right, we can expect to do a good job with a smaller
number of basis functions.

We also pointed out that when the number $n$ of data points is
large, computing an expansion in $O \left( n \right)$ operations is critical, and to
achieve this, the basis functions should be nonzero only locally, or have
compact support. The $B$ B-spline basis is especially attractive from this
perspective.

In Section 4.1, we extended the basis function expansion concept
to employ a partitioned basis $\left( \phi , \psi \right)$ along with a penalty on the size
of the component expanded in terms of the basis functions $\psi .$ But
two properties, relevance to the data and convenience of computation,
remain essential.

We now bring these elements together. We use the partitioning
principle to define a set of basis functions that are optimal with
respect to smoothing. We then provide a recipe for an $O \left( n \right)$ smoothing
algorithm, and also show how the basis can be chosen to be of compact
support form to give the appropriate analogue of B-splines.

We begin with a theorem stating that the optimal basis for spline
smoothing in the context of operators $\left( B , L \right)$ is defined by the
reproducing kernel $k _ { 2 }$ defined in Chapter 13.

Optimal Basis Theorem: For any $\lambda > 0 ,$ the function $x$ minimizing the
spline smoothing criterion (15.2) defined by a linear differential operator
$L$ of order $m$ has the expansion

$$x \left( t \right) = \sum _ { j = 1 } ^ { m } d _ { j } u _ { j } \left( t \right) + \sum _ { i = 1 } ^ { n } c _ { i } k _ { 2 } \left( t _ { i } , t \right) .$$
(15.5)

<!-- PageBreak -->

<!-- PageNumber="262" -->
<!-- PageHeader="15. More general roughness penalties" -->

Equation (15.5) can be put a bit more compactly. As before, let
$u = \left( u _ { 1 } , \ldots , u _ { m } \right) ^ { \prime } .$ Define another vector function

$$\widetilde { k } \left( t \right) = \left\{ k _ { 2 } \left( t _ { 1 } , t \right) , k _ { 2 } \left( t _ { 2 } , t \right) , \ldots , k _ { 2 } \left( t _ { n } , t \right) \right\} ^ { \prime } .$$

Then the optimal basis theorem says that the function $x$ has to be of
the form $x = d ^ { \prime } u + c ^ { \prime } ,$ where $d$ is a vector of $m$ coefficients $d _ { j }$ and
$c$ is the corresponding vector of $n$ coefficients $c _ { i }$ in (15.5). We give a
proof of the optimal basis theorem, but as usual any reader prepared
to take this on trust should simply skip to the next section.

Proof: Suppose $x ^ { * }$ is any function having square-integrable derivatives
up to order $m .$ The strategy for the proof is to construct a function $\widetilde { \mathrm { x } }$ of
the form (15.5) such that $\mathrm { P E N S S E } \left( \widetilde { x } \right) \leq \mathrm { P E N S S E } \left( x ^ { * } \right)$ with equality only
if $\widetilde { x } = x ^ { * } .$ It follows at once that we need never look beyond functions
of the form (15.5) to minimize the spline smoothing criterion PENSSE.

First of all, write $x ^ { * } = u ^ { * } + e ^ { * }$ where $u ^ { * } \in \ker L$ and $e ^ { * } \in \ker B .$ Let
$\mathcal{K}$ be the subspace of ker $B$ spanned by the $n$ functions $k _ { 2 } \left( t _ { i } , \cdot \right) ,$ and let
$\widetilde { \varepsilon }$ be the projection of $e ^ { * }$ onto $K$ in the $L$ L-inner product, as defined in
Section 13.7. This means that $e ^ { * } = \widetilde { e } + e ^ { 1 } ,$ where $\widetilde { e } = c ^ { \prime } \widetilde { k }$ for some vector
$c ,$ and the residual $e ^ { \bot }$ in ker $B$ satisfies the orthogonality condition

$$\langle e , e ^ { \perp } \rangle _ { L } = \int \left( L e \right) \left( L e ^ { \perp } \right) = 0 \text { for all } e \text { in } x .$$
(15.6)

We now define our function $\widetilde { x } = u ^ { * } + \widetilde { e } ,$ so that $\widetilde { \mathrm { x } }$ is necessarily of the
required form (15.5), and $x ^ { * } - \widetilde { x }$ is equal to the residual $e ^ { \bot } .$

To show that $\mathrm { P E N S S E } \left( \widetilde { x } \right) \leq \mathrm { P E N S S E } \left( x ^ { * } \right) ,$ first note that for each $i ,$ by
the defining property of the reproducing kernel,

$$x ^ { * } \left( t _ { i } \right) - \widetilde { x } \left( t _ { i } \right) = e ^ { \bot } \left( t _ { i } \right) = \langle k _ { 2 } \left( t _ { i } , \cdot \right) , e ^ { \bot } \rangle _ { L } = 0$$

by property (15.6), since $k _ { 2 } \left( t _ { i } , \cdot \right)$ is a member of $\mathcal{K}$ and so is $L -$
orthogonal to $e ^ { 1 } .$

Therefore $x ^ { * }$ and $\widetilde { \mathrm { x } }$ agree at the arguments $t _ { i } ,$ and so

$$\mathrm { P E N S S E } \left( x ^ { * } \right) - \mathrm { P E N S S E } \left( \widetilde { x } \right) = \lambda \left\{ P E N _ { L } \left( x ^ { * } \right) - P E N _ { L } \left( \widetilde { x } \right) \right\}$$

the residual sum of squares of the $\mathcal{Y} _ { i }$ is the same about each of the two
functions $x ^ { * }$ and $\widetilde { \mathrm { x } } .$ Since $L x ^ { * } = L e ^ { * }$ and $L \widetilde { x } = L \widetilde { e } ,$ we have

$$P E N _ { L } \left( x ^ { * } \right) - P E N _ { L } \left( \widetilde { x } \right) = P E N _ { L } \left( e ^ { * } \right) - P E N _ { L } \left( \widetilde { e } \right)$$
$$= \langle \widetilde { e } + e ^ { \perp } , \widetilde { e } ^ { \perp } \rangle _ { L } - \langle \widetilde { e } , \widetilde { e } \rangle _ { L } = \langle e ^ { \perp } , e ^ { \perp } \rangle _ { L } + 2 \langle \widetilde { e } , e ^ { \perp } \rangle _ { L } = \langle e ^ { \perp } , e ^ { \perp } \rangle _ { L }$$

since $\widetilde { \varrho }$ is in $\mathscr{K}$ and, therefore, is L-orthogonal to $e ^ { 1 } .$ So $P E N _ { L } \left( e ^ { * } \right) \geq$
$P E N _ { L } \left( \widetilde { e } \right) ,$ and consequently $\mathrm { P E N S S E } \left( x ^ { * } \right) \geq \text { PENSSE } \left( \widetilde { x } \right) .$ Equality holds
only if $e ^ { \bot } \in \ker L$ since we already know that $e ^ { \bot } \in \ker B ,$ this implies
that $e ^ { 1 } = 0$ and that $x ^ { * } = \widetilde { x } ,$ completing the proof of the theorem.

<!-- PageBreak -->

<!-- PageNumber="263" -->
<!-- PageHeader="15.3 An $O \left( n \right)$ algorithm for L-spline smoothing" -->


### 15.3 An $O \left( n \right)$ algorithm for L-spline smoothing


#### 15.3.1 The need for a good algorithm

In principle, the optimal basis theorem should tell us exactly how
to proceed. Since we know that the required function has the form
$x = d ^ { \prime } u + c ^ { \prime } ,$ we need only express $P E N S S E \left( x \right)$ in terms of $c$ and $d$
and minimize to find the best values of $c$ and $d .$ How would this work
out?

Let $K$ be the matrix with values $k _ { 2 } \left( t _ { i } , t _ { j } \right) .$ From equation (13.39) it
follows that

$$P E N _ { L } \left( x \right) = \langle c ^ { \prime } \widetilde { k } , c ^ { \prime } \widetilde { k } \rangle _ { L } = c ^ { \prime } K c .$$

The vector of values $x \left( t _ { i } \right)$ is $U d + K c ,$ where $\mathrm { U }$ is the matrix with values
$u _ { j } \left( t _ { i } \right) .$ Hence, at least in principle, we can find $x$ by minimizing the
quadratic form

$$P E N S S E \left( x \right) = \left( y - U d - K c \right) ^ { \prime } \left( y - U d - K c \right) + \lambda c ^ { \prime } K c$$
(15.7)

to find the vectors $c$ and $d .$

Unfortunately, in practice the matrix $K$ is usually extremely badly
conditioned, that is to say, the ratio of its largest eigenvalue to
its smallest explodes. A practical consequence of this is that the
computations required to minimize the quadratic form (15.7) are likely
to be unstable or impossible.

Furthermore, in smoothing long sequences of observations, it is
crucial to devise a smoothing procedure requiring a number of
arithmetic operations that does not grow too quickly as the length
of the sequence increases. For example, the handwriting data has
$n = 1 4 0 1 ,$ and so an algorithm that was $O \left( n ^ { 2 } \right)$ would be impracticable
and an $O \left( n ^ { 3 } \right)$ algorithm virtually impossible with current computing
power. $B y$ adopting a somewhat different approach, we can set out an
algorithm that requires only $O \left( n \right)$ operations, and furthermore avoids
the numerical problems inherent in the direct minimization of (15.7).

The algorithm we use is based on the theoretical paper of Anselone
and Laurent (1967), but is also known as the Reinsch algorithm because
of the application to the cubic polynomial smoothing case $\left( L = D ^ { 2 } \right)$ by
Reinsch (1967, 1970). It was subsequently extended by Hutchison and
de Hoog (1985). We do not attempt a full exposition of the rationale
for this algorithm here, but Heckman and Ramsay (1996) and Ramsay,
Heckman and Silverman (1997) can be consulted for details.

The algorithm requires evaluations of two types of function that we
have already encountered:

<!-- PageBreak -->

<!-- PageNumber="264" -->
<!-- PageHeader="15. More general roughness penalties" -->

1\. $u _ { j } ,$ $i , j = 1 , \ldots , m :$ a set of $m$ linearly independent functions
satisfying $L u _ { j } = 0 ,$ that is, spanning $\ker L .$ As before, we refer
to these collectively as the vector-valued function $u .$

2\. $k _ { 2 } :$ the reproducing kernel function defined in Chapter 13 for the
subspace of functions $e$ satisfying $B _ { I } e = 0 ,$ where $B _ { I }$ is the initial
value constraint operator.

The functions $u$ and $k _ { 2 }$ are the user-supplied components of the
algorithm and are defined by the particular choice of operator $L$ used
in the smoothing application.

The algorithm splits into three phases:

1\. an initial setup phase that does not depend on the smoothing
parameter $\lambda ,$

2\. a smoothing phase in which we smooth the data, and

3\. a summary phase in which we compute performance measures
for the smooth.

This division of the task is of practical importance because we may want
to try smoothing with many values of $\lambda ,$ and do not want needlessly to
repeat either the initial setup phase or the final descriptive phase.


#### 15.3.2 Setting up the smoothing procedure

In the initial phase, we define two symmetric $\left( n - m \right) \times \left( n - m \right)$ band-
structured matrices $\mathrm { H }$ and $C ^ { \prime } C$ where $m$ is the order of the operator
$L .$ Both matrices are band-structured with band width at most $2 m + 1 ,$
which means that all entries more than $m$ positions away from the
main diagonal are zero. Because of symmetry, these band-structured
matrices require only $\left( n \quad - \quad m \right) \left( m + 1 \right)$ storage locations.

We start by explaining how to construct the matrix $\mathrm { C } .$ For each
$i = 1 , \ldots , n - m ,$ define the $\left( m + 1 \right) \times m$ matrix $\mathrm { U } ^ { \left( i \right) }$ to have $\left( I , j \right)$ element
$u _ { j } \left( t _ { i + l } \right) ,$ for $l = 0 , \ldots , m .$ Thus $\mathrm { U } ^ { \left( i \right) }$ is the submatrix of $\mathrm { U }$ consisting only
of rows $i ,$ $i + 1 , \ldots , i + l .$ Find the QR decomposition (as discussed in
Section A.1.3)

$$U ^ { \left( i \right) } = Q ^ { \left( i \right) } R ^ { \left( i \right) }$$

where $Q ^ { \left( i \right) }$ is square, of order $m + 1 ,$ and orthonormal, and $\mathrm { R } ^ { \left( i \right) }$ is
$\left( m + 1 \right) \times m$ and upper triangular. Let the vector $c ^ { \left( i \right) }$ be the last column
of $Q ^ { \left( i \right) }$ this vector is orthogonal to all the columns of $\mathrm { U } ^ { \left( i \right) } .$ In fact any
vector having this property will do, and in special cases the vector can

<!-- PageBreak -->

<!-- PageNumber="265" -->
<!-- PageHeader="15.3 An $O \left( n \right)$ algorithm for L-spline smoothing" -->

be found by some other method. For polynomial spline smoothing, for
instance, coefficients defining divided differences are used.

Now define the $n \times \left( n - m \right)$ matrix $C$ so that its $i$ ith column has
the $m + 1$ values $c ^ { \left( i \right) }$ starting in row $i ;$ elsewhere the matrix contains
zeroes. In practice, the argument sequence $t _ { 1 } , \ldots , t _ { n }$ is often equally
spaced, and in this case it frequently happens that all the coefficient
vectors $c ^ { \left( i \right) }$ are the same, and hence need be computed only once. The
band structure of $\mathrm { C }$ immediately implies that $C ^ { \prime } C$ has the required band
structure, and can be found in $O \left( n \right)$ operations for fixed $m .$

The other setup-phase matrix $\mathrm { H }$ is the $\left( n - m \right) \times \left( n - m \right)$ symmetric
matrix

$$H = C ^ { \prime } K C ,$$
(15.8)

where $\mathrm { K }$ is the matrix of values $k _ { 2 } \left( t _ { i } , t _ { j } \right) .$ It turns out that $\mathrm { H }$ is also
band-structured with band width $2 m \quad - \quad 1 .$ This is a consequence of
the expression (13.41) for the reproducing kernel, which yields the
following two-part expression:

$$k _ { 2 } \left( t _ { i } , t \right) = \left\{ \begin{array}{} { u \left( t _ { i } \right) ^ { \prime } F \left( t \right) u \left( t \right) } & { \text { for } t _ { i } \geq t } \\ { u \left( t _ { i } \right) ^ { \prime } F \left( t _ { i } \right) u \left( t \right) } & { \text { for } t _ { i } \leq t } \end{array} \right.$$
(15.9)

for a certain matrix function $F \left( t \right) .$ This implies that

$$K _ { i j } = \left\{ \text { UF } \left( t _ { j } \right) u \left( t _ { j } \right) \right\} _ { i } \text { for } i \geq j .$$
(15.10)

Suppose $k \geq j .$ Because $\mathrm { C } _ { i k }$ is zero for $i < k ,$

$$\left( C ^ { \prime } K \right) _ { k j } = \sum _ { i = k } ^ { n } C _ { i k } K _ { i j } = \sum _ { i = k } ^ { n } C _ { i k } \left\{ \text { UF } \left( t _ { j } \right) u \left( t _ { j } \right) \right\} _ { i } ,$$

substituting (15.10); notice that $i \geq j$ for all $i$ within the range of
summation $k \leq i \leq n .$ It follows that for $k \geq j$ we have

$$\left( C ^ { \prime } K \right) _ { k j } = \left\{ C ^ { \prime } U F \left( t _ { j } \right) u \left( t _ { j } \right) \right\} _ { i } = 0 .$$

So $C ^ { \prime } K$ is strictly upper-triangular. Because of the band structure of $\mathrm { C } ,$
the matrix $H = \left( C ^ { \prime } K \right) C$ has zero entries for positions $m$ or more below
the main diagonal, and by symmetry $\mathrm { H }$ has the stated band structure.


#### 15.3.3 The smoothing phase

The actual smoothing consists of two steps:

1\. Compute the $\left( n \quad - \right.$ m)-vector $z$ that solves

$$\left( H + \lambda C ^ { \prime } C \right) z = C ^ { \prime } y ,$$
(15.11)

where the vector $y$ contains the values to be smoothed.

<!-- PageBreak -->

<!-- PageNumber="266" -->
<!-- PageHeader="15. More general roughness penalties" -->

2\. Compute the vector of $n$ values $\widehat { \mathcal{Y} } _ { i } = x \left( t _ { i } \right)$ of the smoothing
function $x$ at the $n$ argument values using

$$\widehat { \mathcal{Y} } = \mathcal{Y} - \lambda C z .$$
(15.12)

Because of the band structure of $\left( H + \lambda C ^ { \prime } C \right)$ and of $\mathrm { C } ,$ both of
these steps can be computed in $O \left( n \right)$ operators, and references on
efficient matrix computation such as Golub and van Loan (1989) can
be consulted for details.


#### 15.3.4 The performance assessment phase

The vector of smoothed values $\widehat { \mathcal{Y} }$ and the original values $y$ that were
smoothed are related as follows:

$$\widehat { \mathcal{Y} } = \mathcal{Y} - \lambda C \left( H + \lambda C ^ { \prime } C \right) ^ { - 1 } C ^ { \prime } y$$
$$= \left\{ I - \lambda C \left( H + \lambda C ^ { \prime } C \right) ^ { - 1 } C ^ { \prime } \right\} \mathcal{Y} .$$

(15.13)

The matrix $S$ defined by

$$S = I - \lambda C \left( H + \lambda C ^ { \prime } C \right) ^ { - 1 } C ^ { \prime }$$
(15.14)

is often called the hat matrix, and in effect defines a linear
transformation that maps the unsmoothed data into its smooth image
by

$$\widehat { \mathcal{Y} } = S y .$$

Various measures of performance depend on the diagonal values in
S. Of these, the most popular are currently

$$C C V = S S E / \left( 1 - n ^ { - 1 } \text { trace } S \right) ^ { 2 }$$
(15.15)

where

$$S S E = \sum _ { i = 1 } ^ { n } \left[ y _ { i } - x \left( t _ { i } \right) \right] ^ { 2 } = \| y - \widehat { y } \| ^ { 2 }$$

and

$$C V = \sum _ { i = 1 } ^ { n } \left[ \left\{ y _ { i } - x \left( t _ { i } \right) \right\} / \left( 1 - s _ { i i } \right) \right] ^ { 2 }$$
(15.16)

where $S _ { i i }$ is the $i$ ith diagonal entry of S. Using methods developed by
Hutchison and de Hoog (1985), we can compute both measures GCV
and $\mathrm { C V }$ in $O \left( n \right)$ operations because of the band-structured nature of
the matrices defining $S ,$ One of the main applications of these two
criteria, both of which are types of discounted error sums of squares,

<!-- PageBreak -->

<!-- PageNumber="267" -->
<!-- PageHeader="15.3 An $O \left( n \right)$ algorithm for L-spline smoothing" -->

is as a guide for choosing the value of the smoothing parameter $\lambda .$ It is
relatively standard practice to look for the value that minimizes one of
these two criteria, just as various variable selection procedures attempt
to minimize discounted error sums of squares in standard regression
analysis. Interestingly, the GCV measure was originally introduced by
Craven and Wahba (1979) as an approximation to the $\mathrm { C V }$ criterion that
could be computed in $O \left( n \right)$ operations. Now $\mathrm { C V }$ is also available in
$n$ operations, but GCV still tends to be preferred in practice for other
reasons. For example, various simulation studies have indicated that
GCV tends to give a better choice of the smoothing parameter $\lambda ,$ possibly
because GCV makes use of smoothing itself by replacing the variable
values $1 - s _ { i i }$ with the average $1 - n ^ { - 1 } .$

Also of great value is a measure of the effective number of degrees
of freedom of the smoothing operation. Two measures are

$$D F _ { 1 } = \text { trace } S \text { and } D F _ { 2 } = \text { trace } S ^ { \prime } S = \text { trace } S ^ { 2 } .$$
(15.17)

These dimensionality measures were introduced and discussed by Buja
et al. (1989). It can be shown that, in the limit as $\lambda \rightarrow \infty ,$ both measures
become simply $m ,$ and similarly, as $\lambda \rightarrow 0 ,$ both measures converge to
$n .$ In between, they give slightly different impressions of how much of
the variation in the original unsmoothed data remains in the smoothed
version.


#### 15.3.5 Other $O \left( n \right)$ algorithms

There is an intimate connection between the theory of splines and
the theory of stochastic differential equations (Wahba, 1978, 1990,
Weinert, Byrd and Sidhu, 1980). This leads to the possibility of using
the Kalman filter, a technique widely used in engineering and other
fields for extracting an estimate of a signal from noisy data, to compute
a smoothing spline. Ansley, Kohn and Wong (1993), using a Kalman
filtering algorithm described in Ansley and Kohn (1989), give some
examples of computing an $\mathrm { L }$ L-spline in $O \left( n \right)$ operations. However,
except for fairly simple cases, this algorithm appears to be difficult
to implement, and its description involves substantial mathematical
detail. Nevertheless, we feel that it is important to call the reader's
attention to this stimulating literature on smoothing by state-space
methods.

<!-- PageBreak -->

<!-- PageNumber="268" -->
<!-- PageHeader="15. More general roughness penalties" -->


### 15.4 A compact support basis for L-splines

In this section our concern is the construction of compact support basis
functions from the reproducing kernel basis functions $k _ { 2 } \left( t _ { i } , \cdot \right) .$ A basis
made up of such functions may be useful for techniques such as the
regularized principal components analysis described in Section 7.4.1,
and has many numerical advantages, analogous to those of B-splines.

For any fixed $i = 1 , \ldots , n - 2 m ,$ consider the following sequence of
$2 m + 1$ basis functions based on the reproducing kernel:

$$k _ { 2 } \left( t _ { i + \ell } , \cdot \right) , \ell = 0 , \ldots , 2 m .$$

Let $b _ { l } ^ { \left( i \right) } , l = 0 , \ldots , 2 m$ be a corresponding sequence of weights defining
a new basis function

$$\psi _ { i } = \sum _ { \ell = 0 } ^ { 2 m } b _ { \ell } ^ { \left( i \right) } k _ { 2 } \left( t _ { i + \ell } , \cdot \right) .$$
(15.18)

The properties we seek are

$$\psi _ { i } \left( t \right) = 0 \text { for } t \leq t _ { i } , \text { and } \psi _ { i } \left( t \right) = 0 \text { for } t \geq t _ { i + 2 m } .$$

But from the first line of (15.9), the first of these is achieved $\mathrm { i f }$

$$\sum _ { \ell = 0 } ^ { 2 m } b _ { \ell } ^ { \left( i \right) } u _ { j _ { 1 } } \left( t _ { i + \ell } \right) = 0 , j _ { 1 } = 1 , \ldots , m$$
(15.19)

and, at the same time, the second line of (15.9) indicates that the second
property is satisfied if

$$\sum _ { \ell = 0 } ^ { 2 m } b _ { \ell } ^ { \left( i \right) } \left[ \sum _ { j _ { 1 } = 1 } ^ { m } u _ { j _ { 1 } } \left( t _ { i + \ell } \right) f _ { j _ { 1 } , j _ { 2 } } \left( t _ { i + \ell } \right) \right] = 0 , j _ { 2 } = 1 , \ldots , m$$
(15.20)

where $f _ { j _ { 1 } , j _ { 2 } } \left( t _ { i + l } \right)$ is entry $\left( j _ { 1 } , j _ { 2 } \right)$ of $\mathrm { F } \left( t _ { i + \ell } \right) .$

Now these are two sets of $m$ linear constraints on the $2 m + 1$
coefficients $b _ { \ell } ^ { \left( i \right) } ,$ and we know that, in general, we can always find a
coefficient vector $b ^ { \left( i \right) }$ satisfying them. The reason that there are only
$2 m$ constraints for $2 m + 1$ coefficients is that the linear constraints can
only define the vector $b ^ { \left( i \right) }$ up to a change of scale.

Let the $\left( 2 m + 1 \right) \times 2 m$ matrix $\mathrm { V } ^ { \left( i \right) }$ have in its first $m$ columns the
values $u _ { j _ { 1 } } \left( t _ { i + \ell } \right) ,$ $j _ { 1 } = 1 , \ldots , m ,$ and in its second set of $m$ columns the
values $\sum _ { j _ { 1 } = 1 } ^ { m } u _ { j _ { 1 } } \left( t _ { i + } g \right) f _ { j _ { 1 } , j _ { 2 } } \left( t _ { i + } p \right) ,$ $j _ { 2 } = 1 , \ldots , m .$ Then the constraints
(15.19) and (15.20) can be written in the matrix form

$$\left( b ^ { \left( i \right) } \right) ^ { \prime } V ^ { \left( i \right) } = 0 .$$

<!-- PageBreak -->

<!-- PageNumber="269" -->
<!-- PageHeader="15.5 Some case studies" -->

As in the calculation of the vectors $c ^ { \left( i \right) }$ in Section 15.3.2, the required
vector $b ^ { \left( i \right) }$ is simply the last column of the $Q$ matrix in the QR
decomposition of $\mathrm { V } ^ { \left( i \right) } .$

If the argument values are unequally spaced, this calculation of the
coefficient vectors $b ^ { \left( i \right) }$ must be carried out for each value of $i$ from 1
to $n \quad - \quad 2 m .$ However, in the frequently encountered case where the $t _ { i }$
values are equally spaced, only one coefficient calculation is required,
and the resulting set of coefficients $b$ serves for all $n \quad - \quad 2 m$ compact
support splines $\psi _ { i }$

Observant readers may note that we have lost $2 m$ basis functions
by this approach. We may deal with this difficulty in various ways.
One approach is to say that a little bit of fitting power has been lost,
but that, if $n$ is large, this may have little impact on the smoothing
function, and what little impact it has is at the ends of the interval.
Alternatively, however, we can use a technique employed in defining
polynomial $B$ B-splines, and add $m$ additional argument values at each
end of the interval. For computational convenience in the equally-
spaced argument case, we can simply make these a continuation of
the sequence in both directions. This augments the basis to retain the
full fitting power of the original reproducing kernel basis.


### 15.5 Some case studies


#### 15.5.1 The gross domestic product data

The gross domestic product data introduced in Chapter 13 share
with many economic indicators the overall tendency for exponential
growth. If we wish to smooth the deseasonalized GDP record of the
U.S. displayed in Figure 13.1, the operator $L = - y D + D ^ { 2 }$ annihilates
$u _ { 1 } \left( t \right) = 1$ and $u _ { 2 } \left( t \right) = e ^ { y t } ,$ so these are obvious choices for
the functions spanning $\ker L .$ A reasonable choice for the matching
constraint operator is simply $B _ { I } ,$ such that $B _ { I } u = \left\{ u \left( 0 \right) , D u \left( 0 \right) \right\} ^ { \prime } ,$
implying that the coefficients of $u _ { 1 }$ and $u _ { 2 }$ are specified by the initial
value and slope of the smoothed record.

In this case, we could estimate the parameter $y$ by estimating
the slope of the relationship between log GDP and time by ordinary
regression analysis. Another possibility is to fit all or part of the data
by nonlinear least squares regression using the two functions $u _ { 1 }$ and
$u _ { 2 } .$ To do this, we minimize the error sum of squares with respect to
the coefficients $c _ { 1 }$ and $c _ { 2 }$ of $c _ { 1 } u _ { 1 } + c _ { 2 } u _ { 2 }$ and with respect to $y$ which,
of course, determines $u _ { 2 } .$ Since for any fixed $y$ value, the minimizing

<!-- PageBreak -->

<!-- PageNumber="270" -->
<!-- PageHeader="15. More general roughness penalties" -->


<figure>
<figcaption>FIGURE 15.3. The line virtually interpolating the data indicates the spline smooth of the U.S. GDP data using $L = - 0 . 0 5 4 D + D ^ { 2 }$ and the minimum GCV value for smoothing parameter $\lambda .$ The dashed line, which is almost indistinguishable but does not quite interpolate the data so closely, indicates the L-spline fit corresponding to $D F _ { 1 } = 1 0 .$</figcaption>

7

6

US GDP (trillion $)

5

\+

3

1980

1982

1984

1986

1988

1990

1992

1994

Year

</figure>


values of the coefficients can be computed directly by linear least
squares, it makes sense to use $a$ one-dimensional minimization routine
such as Brent's method (Press et al., 1992) to find the optimal $y$ value;
for each new value of $y$ within the iterative method, a linear regression
is required to get the associated values of $c _ { 1 }$ and $c _ { 2 } .$ The resulting least
squares estimate of $y$ for the U.S. data, based on the values from 1980
to 1989 when the growth was more exponential, is 0.054.

Using this value of $y ,$ we used the method of Section 15.3 to find
the $\mathrm { L }$ L-smoothing spline shown in Figure 15.3. We minimized the GCV
criterion to obtain the value $\lambda = 0 . 0 5 3 .$ The $\mathrm { D F } _ { 1 }$ measure of equivalent
degrees of freedom was 39.6, so we purchased the excellent fit of the
spline at the price of a rather large number of degrees of freedom.

By comparison, the cubic smoothing spline that minimizes GCV
produces almost identical results in terms of GCV and $\mathrm { D F } _ { 1 }$ values.
Perhaps this is not surprising since the curve is only slightly more
exponential than linear. But the results are rather different when we
smooth with the fixed value of $D F _ { 1 } = 1 0 ,$ corresponding to $\lambda = 2 2 . 9 .$
The $\mathrm { L }$ L-spline fit using this more economical model is just barely visible
in Figure 15.3, and $G C V = 0 . 0 0 0 6 8 .$ The cubic polynomial spline with

<!-- PageBreak -->

<!-- PageNumber="271" -->
<!-- PageHeader="15.5 Some case studies" -->

$D F _ { 1 } = 1 0$ yields $G C V = 0 . 0 0 0 8 4 ,$ and its poorer fit reflects the fact that
some of its precious degrees of freedom were used up in fitting the
mild exponential trend.


#### 15.5.2 The melanoma data

These data, displayed in Figure 13.2, represent a more complex
relationship, with a cyclic effect superimposed on a linear development.
The interesting operator is

$$L = w ^ { 2 } D ^ { 2 } + D ^ { 4 }$$
(15.21)

for some appropriate constant $w ,$ since this would annihilate the four
functions

$$u \left( t \right) = \left( 1 , t , \sin w t , \cos w t \right) ^ { \prime } .$$

Using the techniques of Chapter 13, for $s \leq t$ the reproducing kernel is
given by

$$k _ { 2 } \left( s , t \right) = w ^ { - 7 } \left[ \left( w s \right) ^ { 2 } \left( w t / 2 - w s / 6 \right) - w t + w s + w t \cos w s \right.$$
$$+ \cos \cos \omega t - \sin \omega s - \sin \omega t + \sin \left( w t - \omega s \right)$$

$$\left. - \left( \sin w s \cos w t \right) / 2 + s \cos \left( w t - w s \right) / 2 \right] .$$
(15.22)

We estimated the parameter $w$ to be 0.650 by the nonlinear
least squares approach. This corresponds to a period of 9.66 years,
roughly the period of the sunspot cycle affecting solar radiation and
consequently melanoma. When we smooth the data with the spline
defined by the operator (15.21) and select $\lambda$ so as to minimize GCV,
it turns out that $\lambda$ becomes arbitrarily large, corresponding to a
parametric fit using only the basis functions $u ,$ consuming four degrees
of freedom, and yielding $G C V = 0 . 0 7 6 .$ The polynomial smoothing
spline with order $m = 4 ,$ displayed in Figure 13.2, is a minimum-
GCV estimate corresponding to $D F _ { 1 } = 1 2 . 0$ and $G C V = 0 . 0 9 5 .$ Thus,
polynomial spline smoothing required three times the degrees of
freedom to produce a fit that was still worse in GCV terms than the $\mathrm { L }$
spline smooth. Of the two methods of order four, the operator (15.21)
is much to be preferred to $L = D ^ { 4 } .$


#### 15.5.3 GDP data with seasonal effects

In the data provided by the U.S. and most other countries, the within-
year variation in GDP that is a normal aspect of most economies was
removed. But the data for Sweden, displayed in Figure 15.4, retains this

<!-- PageBreak -->

<!-- PageNumber="272" -->
<!-- PageHeader="15. More general roughness penalties" -->


<figure>
<figcaption>FIGURE 15.4. The gross domestic product for Sweden with seasonal variation. The solid line is the smooth using operator $L = \left( - y D + D ^ { 2 } \right) \left( w ^ { 2 } I + D ^ { 2 } \right) ,$ and the dashed line is the smooth for $L = D ^ { 4 } ,$ the smoothing parameter being determined by minimizing the GCV criterion in both cases.</figcaption>

400

350

Swedish GDP

300

250

200

150

1980

1982

1984

1986

1988

1990

1992

1994

Year

</figure>


seasonal variation. This suggests composing the operator $- y D + D ^ { 2 }$
used for the U.S. GDP data with the deseasonalizing operator $w ^ { 2 } I + D ^ { 2 }$
to obtain the composite operator of order four

$$L = \left( - y D + D ^ { 2 } \right) \left( w ^ { 2 } I + D ^ { 2 } \right) = - y w ^ { 2 } D + w ^ { 2 } D ^ { 2 } - y D ^ { 3 } + D ^ { 4 } .$$
(15.23)

This annihilates the four linearly independent functions given by the
components of

$$u \left( t \right) = \left( 1 , \exp y t , \sin w t , \cos w t \right) ^ { \prime } .$$

In this application we know that $w = 2 \pi$ for time measured in years,
and the nonlinear least squares estimate for $y$ was 0.078.

The minimum GCV L-spline for these data is the solid line in the
figure, and has $G C V = 1 4 2 . 9 , S S E = 5 2 9 8 ,$ and $D F _ { 1 } = 1 0 . 4 .$ This
fairly low-dimensional spline tracks both the seasonal and long-term
variation rather well. By contrast, the minimum GCV polynomial spline
corresponding to $L = D ^ { 4 }$ is shown by the dashed line, and has $G C V =$
193.8, $S S E = 8 1 6 9 ,$ and $D F _ { 1 } = 7 . 4 .$ As both the curve itself and the
GCV value indicate, the polynomial spline was completely unable to
model the seasonal variation, and treated it as noise. On the other
hand, reducing the smoothing parameter $\lambda$ to the point where SSE was

<!-- PageBreak -->

<!-- PageNumber="273" -->
<!-- PageHeader="15.5 Some case studies" -->

reduced to the same value as was attained for the L-spline required
$D F _ { 1 } = 2 8 . 2 ,$ or nearly three times the degrees of freedom. Again we see
that building the capacity to model important sources of variation into
the operator $L$ pays off handsomely.


#### 15.5.4 Smoothing simulated human growth data

One of the triumphs of nonparametric regression techniques has
been their capacity to uncover previously unsuspected aspects of
growth in skeletal height (Gasser, Müller, et al. 1984; Ramsay, Bock
and Gasser, 1995). In this illustration, spline smoothing with an
estimated differential operator was applied to simulated smoothing
data. The objective was to see whether estimating the smoothing
operator improves the estimation of the growth curve itself, and of
the acceleration function of stature, over an a priori 'off-the-rack'
smoother.

To investigate how the performance of the L-spline would compare in
practice with a polynomial spline, we simulated data to resemble actual
human growth curve records. We generated two samples. A training
sample of 100 records was analysed in a manner representative of
actual practice, and a validation sample of 1000 records was used to
see how these analyses would perform on data for which the analyses
were not tuned.

The simulated data for both the training and validation samples
consisted of growth records generated by using the triple logistic
parametric nine-parameter growth model proposed by Bock and
Thissen (1980). According to this model, height $h _ { i } \left( t \right)$ at age $t$ for
individual $i$ is

$$h _ { i } \left( t \right) = \sum _ { j = 1 } ^ { 3 } c _ { i j } / \left[ 1 + \exp \left( - a _ { i j } \left( t - b _ { i j } \right) \right) \right] .$$
(15.24)

Although not completely adequate to account for actual growth curves,
this model does capture their salient features rather well. The actual
number of parameters in the model turns out to be only eight, since the
parameter $a _ { i 1 }$ can be expressed as a function of the other parameters.

We generated each record by first sampling from a population of
coefficient vectors having a random distribution estimated from actual
data for males in the Fels Growth Study (Roche, 1992). We computed
the errorless growth curves (in cm) for the 41 age values ranging from 1
to 21 in half-yearly steps, and generated the simulated data by adding
independent normal error with mean 0 and standard deviation 0.5 to

<!-- PageBreak -->

<!-- PageNumber="274" -->
<!-- PageHeader="15. More general roughness penalties" -->


<figure>
<figcaption>FIGURE 15.5. The three weight functions $w _ { 0 } ,$ $w _ { 1 } ,$ and $w _ { 2 }$ for the operator $L = w _ { 0 } I + w _ { 1 } D + w _ { 2 } D ^ { 2 } + D ^ { 3 } .$ The points indicate the pointwise approximation, and the solid line indicates the basis function expansion.</figcaption>

-0.10 -0.05 0.0 0.05

WO

3.0

$W 1$

-3 -2 -1 0 1 2

W2

2.0

1.0

0.0

5

10

15

20

5

10

15

20

5

10

15

20

</figure>


these values. These simulated data had roughly the same variability as
actual growth measurements.

The first step was to use the training sample to estimate the L-spline
of third order that comes as near as possible to annihilating the curves.
To this end, the first analysis consisted of polynomial spline smoothing
of the simulated data to get estimates of the first three derivatives.
The smoothing operator used for this purpose was $D ^ { 5 } ,$ implying that
the smoothing splines were piecewise polynomials of degree nine. This
permitted us to control the roughness of the third derivative in much
the same way as a cubic smoothing spline controls the roughness of
the smoothing function itself. The smoothing parameter was chosen to
minimize the GCV criterion, and with this amount of replicated data, the
value of its minimum is sharply defined. Since our principal differential
analysis estimate of the operator $L$ required numerical integration, we
also obtained function and derivative estimates at 201 equally spaced
values 1(.1)21.

We estimated a third-order differential operator $L$ using both the
pointwise technique and the basis expansion approach described in
Chapter 14. For the latter approach, we used the 23 $B$ B-splines of order
four defined by placing knots at the integer values of age. Figure
15.5 displays the estimated weight functions $w _ { 0 } ,$ $w _ { 1 } ,$ and $w _ { 2 }$ for the
operator $L = w _ { 0 } I + w _ { 1 } D + w _ { 2 } D ^ { 2 } + D ^ { 3 } .$ Although these are difficult to
interpret, we can see that $w _ { 0 }$ is close to 0, suggesting that the operator
could be simplified by dropping the first term. On the other hand,

<!-- PageBreak -->

<!-- PageNumber="275" -->
<!-- PageHeader="15.5 Some case studies" -->


<figure>
<figcaption>FIGURE 15.6. The three solutions to the homogeneous equation $L u = 0$ corresponding to the linear differential operator $L$ estimated for the simulated human growth data.</figcaption>

4

$y _ { 2 }$

3

U3

₹

1

0

10

20

</figure>


$w _ { 1 }$ is close to one until age 15 when the growth function has strong
curvature as the pubertal growth spurt ends, and its variation after
age 15 helps the operator to deal with this. The acceleration weight $w _ { 2 }$
varies substantially over the whole range of ages.

Figure 15.6 shows the three solutions $u _ { j }$ to $L u = 0 ,$ computed by
Picard's method (13.22). Linear combinations of these three functions
can produce good approximations to actual growth curves.

The next step was to use the estimated functions $u _ { j }$ and the
techniques of Chapter 13 to estimate the Green's function $G$ and the
reproducing kernel $k _ { 2 }$ associated with this operator. We approximated
the integrals involved by applying the trapezoidal rule to the values at
the 201 equally spaced arguments.

Now we were ready to carry out the actual smoothing of the training
sample data by using the two techniques, L-spline and polynomial
spline smoothing, both of order three, just as one would in practice. For
both techniques, we relied on the GCV criterion to choose the smoothing
parameter. The polynomial smooth gave values of GCV, $\mathrm { D F } _ { 1 }$ and $\lambda$ of
487.9, 9.0 and 4.4, respectively, and the L-spline smooth produced
corresponding values of 348.2, 11.2 and 0.63.

How well would these two smoothing techniques approximate the
curves generating the data? To answer this question, we generated

<!-- PageBreak -->

<!-- PageNumber="276" -->
<!-- PageHeader="15. More general roughness penalties" -->


<figure>
<figcaption>FIGURE 15.7. The left panel displays root-mean-squared error (RMSE) as a function of age for the simulated growth data. The solid line is for smoothing by using the estimated differential operator $L ,$ and the dashed line is for polynomial smoothing with $L = D ^ { 3 } .$ The right panel shows these results for the estimated height acceleration.</figcaption>

Height RMSE

Acceleration RMSE

0.0 0.2 0.4 0.6 0.8 1.0

2.0

\- L-spline

Polyspline

1.5

1.0

0.5

0.0

5

10

15 20

5

10

15

20

Age

Age

</figure>


1,000 new simulated curves using the same generation process, and
applied the two smoothers using the training sample values of $\lambda .$ Since
we knew the values of the true curves, we could estimate the root-mean-
squared error criterion

$$\mathrm { R M S E } \left( t \right) = \sqrt { E \left\{ \widehat { x } \left( t \right) - x \left( t \right) \right\} ^ { 2 } }$$

by averaging the squared error across the 1,000 curves for a given
specific age $t ,$ and then taking the square root. This yielded the
two RMSE curves displayed in Figure 15.7. We see that the estimate
of both the growth curve itself and its acceleration by the L-spline
procedure is much better for all but the final adult period, where
the $\mathrm { L }$ L-spline estimate of the acceleration curve becomes rather noisy
and unstable. The improvement in the estimation of both curves is
especially impressive prior to and during the pubertal growth spurt.
The mean square error for the polynomial smooth is about four times
that of the L-spline smooth, so using the L-spline is roughly equivalent
to using the polynomial smooth with quadruple the sample size.

<!-- PageBreak -->


## 16 Some perspectives on FDA


### 16.1 The context of functional data analysis

We conclude this volume with some historical remarks and pointers
to bibliographic references which have not been included in the main
course of our development. Of course, we are acutely aware that many
branches of statistical science consider functional models and the
data that go with them. Functional data analysis has a long historical
shadow, extending at least back to the attempts of Gauss and Legendre
to estimate a comet's trajectory (Gauss, 1809; Legendre, 1805). So what
we offer here is perhaps little more than a list of personal inspirations.
In addition we suggest some directions for further research.


#### 16.1.1 Replication and regularity

Although we want to leave the question of exactly what constitutes FDA
soft around the edges, functional data problems as we have described
them have two general features: replication and regularity. These are
intimately related. Both permit the use of information from multiple
data values to identify patterns; replication implies summaries taken
across different observations, whereas regularity allows us to exploit
information across argument values.

Replication is closely bound up with the key concept of a functional
observation as a single entity, rather than a set of individual numbers or

<!-- PageBreak -->

<!-- PageNumber="278" -->
<!-- PageHeader="16. Some perspectives on FDA" -->

values. The availability of a sample of $N$ related functional observations
then leads to an interest in structure and variability in the data that
requires more than one observation to detect. This is in contrast
with much of the literature on nonparametric regression or curve
estimation, where the focus is on estimating a single curve.

Functional principal components analysis, regression analysis, and
canonical correlation, like their multivariate counterparts, characterize
variation in terms of features with stability across replicates. Likewise,
principal differential analysis and the use of an estimated linear
differential operator for smoothing presume a model structure that
belongs to the entire sample. Even curve registration aims to remove
one important source of inter-curve variation so as to render more
obvious the structure that remains.

Regularity implies that we exploit the smoothness of the processes
generating the data, even though these data usually come to us in
discrete form, and most of the analyses that we have considered
assume a certain number of derivatives. The roughness penalty
approach used throughout the book controls the size of derivatives
or mixtures of derivatives of the estimated functional parameters.
In this way we stabilize estimated principal components, regression
functions, monotonic transformations, canonical weight functions, and
linear differential operators.

Are there more general concepts of regularity that would aid FDA?
For example, wavelet approaches to smoothing, briefly discussed
in Section 3.2.6, are probably relevant, because of their ability to
accommodate notions of regularity that, nevertheless, allow certain
kinds of local misbehaviour.

Independent identically distributed observations are only one type of
regularity. For example, can we use the replication principle implicit in
stationary time series for the case where the values of the process are
functions, to define useful functional data analyses? Besse and Cardot
(1997) offer an interesting first step in this direction.


#### 16.1.2 Some functional aspects elsewhere in statistics

Analysis of variance is often concerned with within-replication
treatments. While an ANOVA design, as a rule, does not assume that
these treatments correspond to variation over time or some other
continuum, in practice this is often the case. Consequently texts on
ANOVA such as Maxwell and Delaney (1990) pay much attention to
topics that arise naturally when treatments correspond to events such
as days, related spatial positions, and so on. Modifications allowing for

<!-- PageBreak -->

<!-- PageNumber="279" -->
<!-- PageHeader="16.1 The context of functional data analysis" -->

a more complex correlational structure for the residuals, and the use of
contrasts to make inferences about linear, quadratic, and other types
of trend across treatments are examples.

Cognate to functional data analysis are fields such as longitudinal
data analysis (Diggle et al., 1994), analysis of repeated measurements
(Keselman and Keselman, 1993 and Lindsey, 1993) and growth curve
analysis. Two classic papers that use principal components analysis to
describe the modes of variation among replicated curves are Rao (1958)
and Tucker (1958); Rao (1987) offers a summary of his and others' work
on growth curves. Two more recent applications are Castro, Lawton and
Sylvestre (1986) and Grambsch et al. (1995).

But these and the many other studies of curve structure do not
give the regularity of the phenomena a primary role, giving the
emphasis more to replication. Likewise, empirical Bayes, hierarchical
linear model, or multilevel linear model approaches do treat functional
data in principle, with the added feature of using prior information,
but the nature of the prior structure tends to be multivariate rather
than functional. Nevertheless, we expect that further research will show
that the experience gained and the tools developed in these collateral
disciplines can be put to good use in FDA.


#### 16.1.3 Uses of derivative information

Two efforts stand out as path-breaking attempts to use derivative
information in data analysis. The first of these is a series of papers
on human growth data beginning with Largo et al. (1978) that focussed
on the shape of the acceleration function. By careful and innovative use
of smoothing techniques, spline and kernel, they were able to isolate
a hitherto ignored phenomenon, the so-called mid-spurt, or hump in
the acceleration curve that precedes the pubertal growth spurt and
occurs at around age seven to eight in almost all children of either
gender. These studies confirmed a principle that we have seen in many
of our own functional data analyses: exogenous influences and other
interesting events are often much more apparent in some order of
derivative than in the original curves.

On a somewhat more technical note, the thesis by Besse (1979) and
his subsequent papers (Besse and Ramsay, 1986; Besse, 1980 and 1988)
moved the French data analytic school into a new realm involving data
that take values in spaces of functions possessing a certain number of
derivatives. Besse's discussion of PCA in the context of observations
in Sobelev space was much inspired by Dauxois and Pousse (1976)
and the functional analytic approaches to spline smoothing by Atteia

<!-- PageBreak -->

<!-- PageNumber="280" -->
<!-- PageHeader="16. Some perspectives on FDA" -->

(1965). Ramsay and Dalzell (1991), who coined the term functional data
analysis, extended this line of work to linear models.


#### 16.1.4 Functional analytic treatments of statistical methods

One topic clearly within the scope of FDA is the description of statistical
methods using functional analysis. For example, principal components
analysis is a technique that lends itself naturally to many types of
generalization. The notion of the eigenanalysis of a symmetric matrix
was extended to integral operators with symmetric kernels in the last
century, and the Karhunen-Loève decomposition of more general linear
operators (Karhunen, 1947; Loève, 1945) is essentially the singular
value decomposition in a wider context.

Parzen's papers (1961, 1963) are classics, and have had a great
influence on the spline smoothing literature by calling attention to
the important role played by the reproducing kernel. Grenander
(1981) contributed further development, and Eaton (1983) provided a
systematic coverage of multivariate analysis using inner product space
notation. Stone (1987) also proposed a coordinate-free treatment, and
Small and McLeish (1994) give a more recent discussion of Hilbert space
methods in statistics.

Applied mathematicians and statisticians in France have been
particularly active in recasting procedures originally developed in
a conventional discrete or multivariate setting into a functional
analytic notational framework. Deville (1974) considered the PCA of
functional observations with values in $L ^ { 2 } .$ Cailliez and Pagès (1976)
wrote an influential textbook on multivariate statistics that was both
functional analytic in notation and coordinate-free in a geometrical
sense. This was a courageous attempt to present advanced concepts
to a mathematically unsophisticated readership, and it deserves to be
better known. Dauxois and Pousse (1976) produced a comprehensive
and sophisticated functional analytic exposition of PCA and CCA that
unhappily remains in unpublished form.

Although the exercise of expressing the usual matrix treatments
of multivariate methods in the more general language of functional
analysis is intrinsically interesting to those with a taste for
mathematical abstraction, it also defined directly the corresponding
methods for infinite-dimensional or functional data. Some facility in
functional analysis is a decided asset for certain aspects of research in
FDA, as it already is in many other branches of applied mathematics.

<!-- PageBreak -->

<!-- PageNumber="281" -->
<!-- PageHeader="16.2 Challenges for the future" -->


### 16.2 Challenges for the future

We now turn to a few areas where there is clearly need for further
research. These should be seen as a small selection of the wide range
of topics that a functional data analytic outlook opens up.


#### 16.2.1 Probability and inference

The presence of replication inevitably invites some consideration of
random functions and probability distributions on function spaces. Of
course, there is a large literature on stochastic processes and random
functions, but because of our emphasis on data analysis we have not
emphasized these topics in the present volume.

In passing, we note that functional observations can be random in a
rather interesting variety of ways. We pointed out in Section 15.3 that
the problem of spline smoothing is intimately related to the theory of
stochastic processes defined by the nonhomogenous linear differential
equation $L x = f$ where $L$ is a deterministic linear differential operator
and $f$ is white noise. Should we allow for some stochastic behaviour
or nonlinearity in $L ?$ Is white noise always an appropriate model for $f ?$
Should we look more closely at the behaviour of an estimate of $f$ in
defining smoothing criteria, functional data analyses, and diagnostic
analyses and displays, exploiting this estimate in ways analogous to
our use of residuals in regression analysis? There is a large literature
on such stochastic differential equations; see, for example Øksendal
(1995). Though stochastic differential equations are of great current
interest in financial mathematics, they have had relatively little impact
on statistics more generally. This seems like a way to go.

We discussed the extension of classical inferential tools, such as the
t-test or F-ratio, to the functional domain. We often need simulation
to assess the significance of statistics once we move beyond the
context of inference for a fixed argument value $t .$ For a rather different
approach to inference that incorporates both theoretical arguments
and simulation, see Fan and Lin (1996).

Because of the infinite-dimensional nature of functional variation,
the whole matter of extending conventional methods of inference-
whether parametric or nonparametric, Bayesian or frequentist-is one
that will require considerable thought before being well understood. We
consider that there is much to do before functional data analysis will
have an inferential basis as developed as that of multivariate statistics.

<!-- PageBreak -->

<!-- PageNumber="282" -->
<!-- PageHeader="16. Some perspectives on FDA" -->


#### 16.2.2 Asymptotic results

There is an impressive literature on the asymptotic and other
theoretical properties of smoothing methods. Although some would
argue that theoretical developments have not always had immediate
practical interest or relevance, there are many examples clearly directed
to practical concerns. For a recent paper in the smoothing literature that
addresses the issue of the positive interaction between theoretical and
practical research, see, for example, Donoho et al. (1995).

Some investigations of various asymptotic distributional aspects of
FDA are Dauxois et al. (1982), Besse (1991), Pousse (1992), Leurgans
et al. (1993), Pezzulli and Silverman (1993), Kneip (1994), Kneip and
Engel (1995), and Silverman (1996). Nevertheless, theoretical aspects
of FDA have not been researched in sufficient depth, and it is hoped
that appropriate theoretical developments will feed back into advances
in practical methodology.


#### 16.2.3 Multidimensional arguments

Although we have touched on multivariate functions of a single
argument $t ,$ coping with more than one dimension in the domain of our
functions has been mainly beyond our scope. However, of course there
is a rapidly growing number of fields where data are organized by space
instead of or as well as time. For example, consider the great quantities
of satellite and medical image data, where spatial dimensionality is two
or three and temporal dependence is also of growing importance.

There is a large and growing literature on spatial data analysis; see,
for example, Cressie (1991) and Ripley (1991). Likewise, smoothing over
two or more dimensions of variation is a subject of active research
(Scott, 1992). In particular, Wahba (1990) has pioneered the extension of
regularization techniques to multivariate arguments. In principle, there
is no conceptual difficulty in extending our own work on FDA to the case
of multivariate arguments by using the roughness penalties relevant to
tensor or thin-plate splines. Indeed, the paper by Hastie et al. (1995)
reviewed in Section 12.7 uses roughness penalty methods to address
a functional data analysis problem with a spatial argument. However,
there are questions about multivariate roughness penalty methods in
FDA that require further research.


#### 16.2.4 Practical methodology and applications

Clearly, much research is needed on numerical methods, as is evident
when one considers the work on something as basic as the pointwise

<!-- PageBreak -->

<!-- PageNumber="283" -->
<!-- PageHeader="16.2 Challenges for the future" -->

linear model underlying spline smoothing. We think that regularization
techniques will play a strong role, in part because they are so intuitively
appealing. But of course there are often simpler approaches that may
work more or less as well.

It is our hope that this book will give impetus to the wider
dissemination and use of FDA techniques. More important than any of
the detailed methodological issues raised in this chapter, the pressing
need is for the widespread use of functional data analytic techniques
in practice.


#### 16.2.5 Back to the data!

Finally, we say simply that the data that we have analysed, and our
colleagues who collected them, are ultimately responsible for our
understanding of functional data analysis. If what this book describes
is found to deserve a name for itself, it will be because, with each new
set of functional data, we have discovered challenges and invitations to
develop new methods. Statistics shows its finest aspects when exciting
data find existing statistical technology not entirely satisfactory. It
is this process that informs this book, and ensures that unforeseen
adventures in research await us all.

<!-- PageBreak -->


## Appendix Some algebraic and functional techniques

This appendix covers various topics involving matrix decompositions,
projections in vector and function spaces, and the constrained
maximization of certain quadratic forms through the solution of
appropriate eigenequations.


### A.1 Matrix decompositions and generalized inverses

We describe two important matrix decompositions, the singular value
decomposition and the QR decomposition. Both of these are standard
techniques in numerical linear algebra, and can be carried out within
packages such as $S$ S-PLUS and MATLAB (Mathworks, 1993). We do not
give any details of the way the decompositions are computed; for these
see, for example, Golub and Van Loan (1989) or the standard numerical
linear algebra package LINPACK (Dongarra et al., 1979).


#### A.1.1 Singular value decompositions

Suppose $Z$ is an $m \times n$ matrix. For many purposes it is useful to carry
out a singular value decomposition (SVD) of $Z .$ This expresses $Z$ as the
product of three matrices

$$Z = U D V ^ { \prime }$$
(A.1)

<!-- PageBreak -->

<!-- PageNumber="286" -->
<!-- PageHeader="A.1 Matrix decompositions and generalized inverses" -->

where, for some integer $q \leq \min \left( m , n \right) ,$

· $\mathrm { U }$ is $m \times q$ and $U ^ { \prime } U = I _ { q } ,$ where $\mathrm { I } _ { q }$ is the identity matrix of order $q$

· Dis a $q \times q$ diagonal matrix with strictly positive elements on the
diagonal

· $\mathrm { V }$ $n \times q$ and $\mathrm { V } ^ { \prime } \mathrm { V } = \mathrm { I } _ { \mathcal{U} } .$

The diagonal elements $d _ { 1 } , d _ { 2 } , \ldots , d _ { q }$ of $\mathrm { D }$ are called the singular
values of $Z ,$ and the SVD can always be carried out in such a way that
the diagonal elements $d _ { 1 } , d _ { 2 } , \ldots , d _ { q }$ satisfy

$$d _ { 1 } \geq d _ { 2 } \geq \ldots \geq d _ { q } > 0 .$$
(A.2)

In this case, the number $q$ is equal to the rank of the matrix $Z ,$ i.e. the
maximum number of linearly independent rows or columns of $Z .$

In the special case where $Z$ is square and symmetric, the requirement
that the diagonal elements of $\mathrm { D }$ are necessarily positive is usually
dropped, but the matrices $\mathrm { U }$ and $\mathrm { v }$ are chosen to be identical.
Furthermore we may allow $q \geq$ rank $\mathrm { Z } .$ Then the $d _ { i }$ include all
the nonzero eigenvalues of $\mathrm { Z } ,$ together with some or all of the zero
eigenvalues if there are any. We have

$$Z = U D U ^ { \prime } w i t h U U = I .$$
(A.3)

In addition, if $\mathrm { Z }$ is positive semi-definite (so that $x ^ { \prime } Z x \geq 0$ for all vectors
$\left. x \right)$ then

$$d _ { 1 } \geq d _ { 2 } \geq \ldots \geq d _ { q } \geq 0 .$$
(A.4)


#### A.1.2 Generalized inverses

Given any $m \times n$ matrix $Z ,$ define a generalized inverse or g-inverse of
$\mathrm { z }$ as any $n \times m$ matrix $\mathrm { Z } ^ { - }$ such that

$$Z Z ^ { - } Z = Z .$$
(A.5)

If $m = n$ and $Z$ is an invertible matrix, then it follows from (A.5) that
$\mathrm { Z } ^ { - 1 }$ is a g-inverse of $Z .$ Furthermore, by pre- and postmultiplying (A.5)
by $Z ^ { - 1 } ,$ we see that $Z ^ { - 1 }$ is the unique g-inverse of $\mathrm { z }$ in this case.

In the more general case, the matrix $\mathrm { Z } ^ { - }$ is not necessarily unique,
but a particular g-inverse, called the Moore-Penrose g-inverse $\mathrm { Z } ^ { + } ,$ can
always be calculated using the singular value decomposition (A.1) of
the matrix $\mathrm { Z } .$ Set

$$Z ^ { + } = V D ^ { - 1 } U ^ { \prime } .$$
(A.6)

It is easy to check that $Z ^ { + }$ is a g-inverse of $\mathrm { Z }$ and also that

$$Z ^ { + } Z Z ^ { + } = Z ^ { + } a n d Z Z ^ { + } = U U ^ { \prime } .$$
(A.7)

<!-- PageBreak -->

<!-- PageNumber="287" -->
<!-- PageHeader="A.2 Projections" -->


#### A.1.3 The QR decomposition

The QR decomposition of an $m \times n$ matrix $Z$ is a different decomposition
that yields the expression

$$Z = Q R$$

where $Q$ is an $m \times m$ orthogonal matrix (so that $Q ^ { \prime } Q = Q Q ^ { \prime } = I$ and $\mathbb{R}$
is an $m \times n$ upper-triangular matrix (so that $R _ { i j } = 0$ if $\left. i > j \right) .$

If $m > n$ then the last $\left( m \quad - \quad n \right)$ rows of $R$ will be zero, and each of
the last $\left( m \quad - \quad n \right)$ columns $x$ of $\mathrm { Q }$ will satisfy $x ^ { \prime } Z = 0 .$ Dropping these
rows and columns will yield a restricted $Q R$ decomposition $\mathrm { Z } = \mathrm { Q } _ { 1 } \mathrm { R } _ { 1 }$
where $\mathrm { R } _ { 1 }$ is an $n \times n$ upper-triangular matrix and $\mathrm { Q }$ is an $m \times n$ matrix
of orthonormal columns.


### A.2 Projections

In discussing the key concept of projection, first we consider projection
matrices in m-dimensional spaces, and then go on to consider more
general inner product spaces.


#### A.2.1 Projection matrices

Suppose that an $m \times m$ matrix $\mathbb{P}$ has the property that $P ^ { 2 } = P .$ Define
$\mathcal{P}$ to be the subspace of $R ^ { m }$ spanned by the columns of $\mathrm { P } .$ The matrix
$P$ is called a projection matrix onto the subspace $\mathcal{P} .$ The following two
properties, which are easily checked, give the reason for this definition:

1\. Every m-vector $z$ is mapped by $P$ into the subspace $\mathcal{P} .$

2\. If $z$ is already a linear combination of columns of $\mathrm { P } ,$ so that $z = P u$
for some vector $u ,$ then $P z = z .$

If $P$ is a symmetric matrix, then $P$ is called an orthogonal projection
matrix, and will have several nice properties. For example, for any
vector $z$ we have

$$\left( P z \right) ^ { \prime } \left\{ \left( I - P \right) z \right\} = z ^ { \prime } P ^ { \prime } \left( I - P \right) z = z ^ { \prime } \left( P z - P ^ { 2 } z \right) = 0 .$$

This means that the projected vector $\mathbb{P} z$ and the 'residual vector'
$z \quad - \quad P z$ are orthogonal to one another, in the usual Euclidean sense.
Furthermore, suppose that $\upsilon$ is any vector in $\mathcal{P} .$ Then, by a very similar
argument,

$$\upsilon ^ { \prime } \left( z - \mathrm { P } z \right) = \left( \mathrm { P } \upsilon \right) ^ { \prime } \left( \mathrm { I } - \mathrm { P } \right) z = \upsilon ^ { \prime } \mathrm { P } \left( \mathrm { I } - \mathrm { P } \right) z = 0 ,$$

<!-- PageBreak -->

<!-- PageNumber="288" -->
<!-- PageHeader="A.2 Projections" -->

so that the residual vector is orthogonal to all vectors in $\mathbb{P} .$

Suppose that $w$ is any vector in $\mathcal{P}$ other than $P z .$ Then $w \quad - \quad P z$ is also
in $\mathcal{P}$ and therefore is orthogonal to $z \quad - \quad P z .$ Defining $\langle x , y \rangle = x ^ { \prime } y$ and
$\| x \|$ to be the usual Euclidean inner product and norm,

$$\| z - w \| ^ { 2 } = \| z - \mathrm { P z } \| ^ { 2 } + \| \mathrm { P z } - w \| ^ { 2 } + 2 \langle z - \mathrm { P z } , \mathrm { P z } - w \rangle$$

$$= \| z - \mathrm { P z } \| ^ { 2 } + \| \mathrm { P z } - w \| ^ { 2 } > \| z - \mathrm { P z } \| ^ { 2 } .$$
(A.8)

This means that $P z$ is the point closest to $z$ in the subspace $\mathcal{P} .$ Thus
orthogonal projections onto a subspace have the property of mapping
each vector to the nearest point in the subspace.

More generally, if the inner product is $\langle x , y \rangle = x ^ { \prime } W y ,$ and if $\mathbb{P}$ is
a projection onto the space $P$ such that $\mathrm { W P }$ is symmetric, then $P$ is
orthogonal with respect to this inner product, meaning that $\left( P z , z \quad - \right.$
$P z \rangle = 0$ and $\langle v , z - p _ { z } \rangle = 0$ for all $v$ in $P .$


#### A.2.2 Finding an appropriate projection matrix

Now suppose we are not given a projection matrix, but instead we are
given a subspace $U$ of $R ^ { m } ,$ and we wish to find an orthogonal projection
matrix $\mathrm { P }$ that projects onto $u .$

Let $Z$ be any matrix whose columns are m-vectors that span
the subspace $U .$ There is no need for the columns to be linearly
independent. Define $\mathrm { P }$ by

$$P = Z Z ^ { - } .$$

It is straightforward to show that $\mathrm { P }$ is a projection onto the subspace
$U$ as required.

To get an orthogonal projection, define $\mathbb{P}$ using the Moore-Penrose
g-inverse $\mathrm { Z } ^ { + } .$ Then, in terms of the SVD of $Z ,$ $P = U U ^ { \prime } ,$ so that $P$ is $a$
symmetric matrix and hence an orthogonal projection.


#### A.2.3 Projections in more general inner product spaces

We can extend these ideas to projections in more general inner product
spaces as discussed in Section 2.4.1. As in that section, let $u _ { 1 } , \ldots , u _ { n }$ be
any $n$ elements of our space, and let $u$ be the n-vector whose elements
are $u _ { 1 } , \ldots , u _ { n } .$ Let $U$ be the subspace consisting of all possible linear
combinations $c ^ { \prime } u$ for real n-vectors $c .$ Suppose that $P$ is an orthogonal
projection onto $U$ as specified in Section 2.4.1. The proof that $P$ maps
each element $z$ to the nearest member $P z$ of $U$ is identical to the
argument given in (A.8) because that depends only on the defining
properties of an inner product and associated norm.

<!-- PageBreak -->

<!-- PageNumber="289" -->
<!-- PageHeader="A.3 Constrained maximization of a quadratic function" -->

How are we to find an orthogonal projection of this kind? Extend
our notation to define $K = \langle u , u ^ { \prime } \rangle$ as the symmetric $n \times n$ matrix
with elements $\langle u _ { i } , u _ { j } \rangle .$ The matrix $K$ is positive semi-definite since
$x ^ { \prime } K x = \langle x ^ { \prime } u , u ^ { \prime } x \rangle = \| x ^ { \prime } u \| ^ { 2 } \geq 0$ for any real n-vector $x ,$

Define the operator $P$ by

$$P z = u ^ { \prime } K ^ { + } \left( u , z \right)$$

for all $z .$ By definition $P z$ is a linear combination of the elements of
$u$ and hence is in $\mathcal{P} .$ We shall show that $P$ is an orthogonal projection
onto $P .$

If $\mathcal{Y}$ is in $\mathcal{P} ,$ then $y = u ^ { \prime } c$ for some real vector $c ,$ so that $P y =$
$u ^ { \prime } K ^ { + } K c ,$ and $y - P y = u ^ { \prime } d$ where $d = \left( I - K ^ { + } K \right) c .$ Therefore, since
$K K ^ { + } K = K ,$

$$| | y - P y | | ^ { 2 } = d ^ { \prime } K d = d ^ { \prime } \left( K - K K ^ { + } K \right) c = 0 ,$$

implying that $\| y - P y \| ^ { 2 } = 0$ and $P y = y .$

Finally, given any $v$ in $P ,$ and any $z ,$ use the property (A.7) to show
that

$$\langle P z - v , P z \rangle = \langle P \left( z - v \right) , P z \rangle = \langle z - v , u ^ { \prime } \rangle K ^ { + } K K ^ { + } \langle u , z \rangle$$
$$= \langle z - v , u ^ { \prime } \rangle K ^ { + } \langle u , z \rangle = \langle P z - v , z \rangle$$

and therefore that $\langle P z - v , z - P z \rangle = 0 ,$ completing the proof that $P$ is
the required orthogonal projection onto $P .$


### A.3 Constrained maximization of $a$ quadratic function


#### A.3.1 The finite-dimensional case

Suppose that $\mathrm { A }$ is a symmetric $p \times p$ matrix. An important result in
linear algebra concerns the constrained maximization problem

$$x ^ { \prime } \text { Ax for p-vectors } x \text { subject to } x ^ { \prime } x = 1 .$$
(A.9)

Let $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \ldots \geq \lambda _ { p }$ be the eigenvalues of $A ,$ and let $u _ { i }$ be the
corresponding eigenvectors, each normalized to have $\| u _ { i } \| = 1 .$ Let
$\mathrm { U }$ be the matrix whose columns are the eigenvectors $u _ { i }$ and let $\mathrm { D }$ be
the diagonal matrix with diagonal elements $\lambda _ { i } .$ Then $\mathrm { A } = \mathrm { U D U } ^ { \prime } ,$ and
$U U ^ { \prime } = U ^ { \prime } U = I .$

<!-- PageBreak -->

<!-- PageNumber="290" -->
<!-- PageHeader="A.3 Constrained maximization of a quadratic function" -->

Set $y = U ^ { \prime } x$ in (A.9), so that $x = U y$ and $x ^ { \prime } x = y ^ { \prime } U ^ { \prime } U y = y ^ { \prime } y ,$ so
the constraint $x ^ { \prime } x = 1$ is equivalent to $y ^ { \prime } y = 1 .$ Therefore, in terms of
$y ,$ the maximization problem (A.9) can be rewritten as

$$y ^ { \prime } D y \text { for } p \text { -vectors } y \text { subject to } y ^ { \prime } y = 1 .$$
(A.10)

This is clearly solved by setting $y$ to be the vector $\left( 1 , 0 , \ldots , 0 \right) ^ { \prime } ,$ so
that $x$ is the first column of $\mathrm { U } ,$ in other words the leading normalized
eigenvector $u _ { 1 }$ of $A .$

By an extension of this argument, we can characterize all the
eigenvectors of $\mathrm { A }$ as solutions of successive optimization problems.
The jth normalized eigenvector $u _ { j }$ solves the problem (A.9) subject to
the additional constraint of being orthogonal to all the solutions found
so far:

$\max x ^ { \prime } A x$ subject to and $x ^ { \prime } u _ { 1 } = x ^ { \prime } u _ { 2 } = \ldots = x ^ { \prime } u _ { j - 1 } = 0 .$
$$x ^ { \prime } x = 1$$
(A.11)

Setting $x = u _ { j }$ gives $x ^ { \prime } A x = \lambda _ { j } u _ { j } ^ { \prime } u _ { j } = \lambda _ { j } ,$ the jth eigenvalue.


#### A.3.2 The problem in a more general space

Now suppose we are working within a more general inner product
space. The role of a symmetric matrix is now played by a self-adjoint
linear operator $A ,$ that is one satisfying the condition

$$\langle x , A y \rangle = \langle A x , y \rangle \text { for all } x \text { and } y .$$

We shall assume that $A$ is a completely continuous (or compact)
symmetric transformation on a Hilbert space; there is no need at all
for the reader to understand what this means, but anyone interested
is referred to Riesz and Nagy (1956) or any other standard text on
functional analysis. The reader can always take it on trust that the
assumptions are satisfied when we appeal to the results of this section.

The problem

$$\max \langle x , A x \rangle \text { subject to } \| x \| = 1$$
(A.12)

corresponds to the maximization problem (A.9), and we can define
a sequence $u _ { j }$ as the solutions to the succession of optimization
problems

$\max \langle x , A x \rangle$ subject to $\| x \| = 1$ and $\langle x , u _ { i } \rangle = 0$ for $i < j .$ (A.13)

Under the conditions referred to above, these optimization problems
can be solved by considering the eigenfunction problem

$$A u = \lambda u$$

<!-- PageBreak -->

<!-- PageNumber="291" -->
<!-- PageHeader="A.3 Constrained maximization of a quadratic function" -->

and normalizing the eigenfunctions $u$ to satisfy $\| u \| = 1 .$ Suppose that
the eigenvalues are $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \ldots .$ with eigenfunctions $u _ { 1 } , u _ { 2 } , \ldots .$ Then
the leading eigenfunction $u _ { 1 }$ solves the optimization problem (A.12)
and the value of the maximum is $\lambda _ { 1 } .$ The successive eigenfunctions
$u _ { j }$ solve the constrained problem (A.13), and the maximum at the $j$ jth
stage is $\langle u _ { j } , A u _ { j } \rangle = \lambda _ { j } \| u _ { j } \| ^ { 2 } = \lambda _ { j } .$


#### A.3.3 Generalized eigenproblems

Sometimes we wish to modify the optimization problems we have
considered by introducing a positive-definite symmetric matrix $B$ or
self-adjoint operator $B$ into the constraints, replacing the constraint
$\| x \| = 1$ by $x ^ { \prime } B x = 1$ or, more generally, $\langle x , B x \rangle = 1 ,$ and similarly
defining orthogonality with respect to the matrix $B$ or operator $B .$

Consider the solutions of the generalized eigenproblem

$$A v = \rho B v .$$

and normalize the solutions to satisfy $\langle v , B v \rangle = 1 .$ Suppose that the
solutions are $v _ { 1 } , v _ { 2 } , \ldots ,$ with corresponding generalized eigenvalues
$\rho _ { 1 } \geq \rho _ { 2 } \geq \ldots .$ Under suitable conditions, which are always satisfied in
the finite-dimensional case, and are analogous to those noted above for
more general spaces, the leading generalized eigenvector or function
$\upsilon _ { 1 }$ solves the problem

$$\max \langle v , A v \rangle \text { subject to } \langle v , B v \rangle = 1 ,$$
(A.14)

and the maximizing value is equal to $\rho _ { 1 } .$ The jth generalized
eigenvector or function $\upsilon _ { j }$ solves the problem

$\max \langle v , A v \rangle$ subject to $\langle v , B v \rangle = 1$ and $\langle v , B v _ { i } \rangle = 0$ for $i < j$

and the maximizing value is $\rho _ { j } .$

Finally, we note that the problem of maximizing the ratio

$$\frac { \langle v , A v \rangle } { \langle v , B v \rangle }$$
(A.15)

for $v \neq 0$ is equivalent to that of maximizing $\langle v , A v \rangle$ subject to the
constraint $\langle v , B v \rangle = 1 .$ To see this, note that scaling any $v$ to satisfy
the constraint does not affect the value of the ratio (A.15), and so the
maximum of the ratio is unaffected by the imposition of the constraint.
Once the constraint is imposed, the denominator of (A.15) is equal to 1,
and so maximizing the ratio subject to $\langle \upsilon , B \upsilon \rangle = 1$ is exactly the same
as the original maximization problem (A.14).

<!-- PageBreak -->


## References

Anderson, T. W. (1984) An Introduction to Multivariate Statistical
Analysis. Second edition. New York: John Wiley & Sons.

Anselone, P. M. and Laurent, P. J. (1967) A general method for
the construction of interpolating or smoothing spline-functions.
Numerische Mathematik, 12, 66-82.

Ansley, C. F. and Kohn, R. (1990) Filtering and smoothing in state space
models with partially diffuse initial conditions. Journal of Time
Series Analysis, 11, 275-293.

Ansley, C. F., Kohn, R. and Wong, C .- M. (1993) Nonparametric spline
regression with prior information. Biometrika, 80, 75-88.

Atteia, M. (1965) Spline-fonctions généralisées. Comptes Rendus de
l'Académie des Sciences Série I: Mathématique, 261, 2149-2152.

Basilevsky, A. (1994) Statistical Factor Analysis and Related Methods.
New York: John Wiley & Sons.

Besse, P. (1979) Etude descriptive des processus: Approximation et
interpolation. Thèse de troisième cycle, Université Paul-Sabatier,
Toulouse.

Besse, P. (1980) Deux exemples d'analyses en composantes principales
filtrantes. Statistique et Analyse des Données, 3, 5-15.

<!-- PageBreak -->

<!-- PageHeader="294 References" -->

Besse, P. (1988) Spline functions and optimal metric in linear principal
component analysis. In J. L. A. van Rijkevorsel and J. de Leeuw (eds)
Component and Correspondence Analysis: Dimensional Reduction by
Functional Approximation. New York: John Wiley & Sons.

Besse, P. (1991) Approximation spline de l'analyse en composantes
principales d'une variable aléatoire hilbertienne. Annales de la
Faculté des Sciences de Toulouse, 12, 329-349.

Besse, P. and Ramsay, J. O. (1986) Principal components analysis of
sampled functions. Psychometrika, 51, 285-311.

Besse, P., Cardot, H. and Ferraty, F. (1997) Simultaneous non-
parametric regressions of unbalanced longitudinal data. Comput-
ational Statistics and Data Analysis, to appear.

Besse, P. and Cardot, H. (1997) Approximation spline de la prévision
d'un processus fonctionnel autorégressif d'ordre 1. Canadian
Journal of Statistics, to appear.

Bock, R. D. and Thissen, D. (1980) Statistical problems of fitting
individual growth curves. In F. E. Johnston, A. F. Roche and
C. Susanne (eds) Human Physical Growth and Maturation:
Methodologies and Factors. New York: Plenum.

Bookstein, F. L. (1991) Morphometric Tools for Landmark Data:
Geometry and Biology. Cambridge: Cambridge University Press.

Buckheit, J. B, Olshen, R. A., Blouch, K. and Myers, B. D. (1997) Modeling
of progressive glomerular injury in humans with lupus nephritis.
American Journal of Physiology, to appear.

Buja, A., Hastie, T. and Tibshirani, R. (1989) Linear smoothers and
additive models (with discussion). Annals of Statistics, 17, 453-555.

Caillez, F. and Pagès, J. P. (1976) Introduction à l'analyse des données.
Paris: SMASH.

Castro, P. E., Lawton, W. H. and Sylvestre, E. A. (1986) Principal
modes of variation for processes with continuous sample curves.
Technometrics, 28, 329-337.

Char, B. W., Geeddes, K. O., Gonnet, G. H., Leong, B. L., Monagan, M. B.
and Watt, S. M. (1991) MAPLE V Language Reference Manual. New
York: Springer.

Chui, C. K. (1992) An Introduction to Wavelets. San Diego: Academic
Press.

Cleveland, W. S. (1979) Robust locally weighted regression and smooth-
ing scatterplots. Journal of the American Statistical Association, 74,
829-836.

<!-- PageBreak -->

<!-- PageHeader="References 295" -->

Coddington, E. A. (1989) An Introduction to Ordinary Differential
Equations. New York: Dover.

Coddington, E. A. and Levinson, N. (1955) Theory of Ordinary
Differential Equations. New York: McGraw-Hill.

Cook, R. D. and Weisberg, S. (1982) Residuals and Influence in
Regression. New York: Chapman and Hall.

Craven, P. and Wahba, G. (1979) Smoothing noisy data with spline
functions: estimating the correct degree of smoothing by the
method of generalized cross-validation, Numerische Mathematik,
31, 377-403.

Cressie, N. (1991) Statistics for Spatial Data. New York: John Wiley &
Sons.

Dalzell, C. J. and Ramsay, J. O. (1990) Computing reproducing kernels
with arbitrary boundary constraints. SIAM Journal of Scientific
Computing, 14, 511-518.

Daubechies, I. (1992) Ten Lectures on Wavelets. CBMS-NSF Series in
Applied Mathematics, 61. Philadelphia: Society for Industrial and
Applied Mathematics.

Dauxois, $\mathrm { J } .$ and Pousse, A. (1976) Les analyses factorielles en calcul des
probabilité et en statistique: Essai d'étude synthétique. Thèse d'état,
Université Paul-Sabatier, Toulouse.

Dauxois, J., Pousse, A. and Romain, Y. (1982) Asymptotic theory for the
principal component analysis of a vector random function: some
applications to statistical inference. Journal of Multivariate Analysis,
12, 136-154.

de Boor, C. (1978) A Practical Guide to Splines. New York: Springer.

Delves, L. M. and Mohamed, J. L. (1985) Computational Methods for
Integral Equations. Cambridge: Cambridge University Press.

Deville, J. C. (1974) Méthodes statistiques et numériques de l'analyse
harmonique. Annales de L'INSEE, 15, 7-97.

Diggle, P. J., Liang, K .- Y. and Zeger, S. L. (1994) Analysis of Longitudinal
Data. New York: Oxford University Press.

Dongarra, J. J., Bunch, J. R., Moler, C. B. and Stewart, G. W. (1979)
LINPACK Users' Guide. Philadelphia: Society for Industrial and
Applied Mathematics.

Donoho, D. L., Johnstone, I. M., Kerkyacharian, G. and Picard, D. (1995)
Wavelet shrinkage: asymptopia? (with Discussion). Journal of the
Royal Statistical Society, Series B, 57, 301-369.

<!-- PageBreak -->

<!-- PageHeader="296 References" -->

Eaton, M. L. (1983) Multivariate Statistics: A Vector Space Approach. New
York: John Wiley & Sons.

Eaton, M. L. and Perlman, M. D. (1973) The non-singularity of
generalized sample covariance matrices. Annals of Statistics, 1, 710-
717.

Engle, R. F., Granger, C. W. J., Rice, J. A. and Weiss, A. (1986)
Semiparametric estimates of the relation between weather and
electricity sales. Journal of the American Statistical Association, 81,
310-320.

Eubank, R. L. (1988) Spline Smoothing and Nonparametric Regression.
New York: Marcel Dekker.

Falkner, F. (ed.) (1960) Child Development: An International Method of
Study. Basel: Karger.

Fan, J. and Gijbels, I. (1996) Local Polynomial Modelling and its
Applications. London: Chapman and Hall.

Fan, J. and Lin, S .- K. (1996) Tests of significance when data are curves.
Unpublished manuscript.

Friedman, J. H. and Silverman, B. W. (1989) Flexible parsimonious
smoothing and additive modeling (with Discussion and Response).
Journal of the American Statistical Association, 31, 1-39.

Gasser, T. and Kneip, A. (1995). Searching for structure in curve
samples. Journal of the American Statistical Association, 90, 1179-
1188.

Gasser, T., Kneip, A., Binding, A., Prader, A. and Molinari, L. (1991a)
The dynamics of linear growth in distance, velocity and acceleration.
Annals of Human Biology, 18, 187-205.

Gasser, T., Kneip, A., Ziegler, P., Largo, R., Molinari, L., and Prader, A.
(1991b) The dynamics of growth of height in distance, velocity and
acceleration. Annals of Human Biology, 18, 449-461.

Gasser, T., Kneip, A., Ziegler, P., Largo, $\mathbb{R} .$ and Prader, A. (1990) A method
for determining the dynamics and intensity of average growth.
Annals of Human Biology, 17, 459-474.

Gasser, T. and Müller, H .- G., (1979) Kernel estimation of regression
functions. In T. Gasser and M. Rosenblatt (eds) Smoothing
Techniques for Curve Estimation. Heidelberg: Springer, pp. 23-68.

Gasser, T. and Müller, H .- G., (1984) Estimating regression functions
and their derivatives by the kernel method. Scandinavian Journal
of Statistics, 11, 171-185.

<!-- PageBreak -->

<!-- PageHeader="References 297" -->

Gasser, T. , Müller, H .- G., Köhler, W., Molinari, L. and Prader, A. (1984).
Nonparametric regression analysis of growth curves. Annals of
Statistics, 12, 210-229.

Gauss, C. F. (1809) Theoria motus corporum celestium. Hamburg:
Perthes et Besser.

Golub, G. and Van Loan, C. F. (1989) Matrix Computations. Second
edition. Baltimore: Johns Hopkins University Press.

Grambsch, P. M., Randall, B. L. Bostick, R. M., Potter, J. D. and Louis, T.
A. (1995) Modeling the labeling index distribution: an application
of functional data analysis. Journal of the Americal Statistical
Association, 90, 813-821.

Green, P. J. and Silverman, B. W. (1994) Nonparametric Regression and
Generalized Linear Models: A Roughness Penalty Approach. London:
Chapman and Hall.

Greenhouse, S. W. and Geisser, S. (1959) On methods in the analysis of
profile data. Psychometrika, 24, 95-112.

Grenander, U. (1981) Abstract Inference. New York: John Wiley & Sons.
Härdle, W. (1990) Applied Nonparametric Regression. Cambridge:
Cambridge University Press.

Hastie, T. and Tibshirani, R. (1990) Generalized Additive Models. New
York: Chapman and Hall.

Hastie, T., Buja, A. and Tibshirani, R. (1995) Penalized discriminant
analysis. Annals of Statistics, 23, 73-102.

Heckman, N. and Ramsay, J. O (1996) Penalized regression with
model-based penalties. University of British Columbia: unpublished
manuscript.

Houghton, A. N., Flannery, J. and Viola, M. V. (1980) Malignant
melanoma in Connecticut and Denmark. International Journal of
Cancer, 25, 95-104.

Hutchison, M. F. and de Hoog, F. R. (1985) Smoothing noisy data with
spline functions. Numerische Mathematik, 47, 99-106.

Huynh, H. S. and Feldt, L. (1976) Estimation of the Box correction for
degrees of freedom from sample data in randomized block and split-
plot designs. Journal of Educational Statistics, 1, 69-82.

Ince, E. L. (1956) Ordinary Differential Equations. New York: Dover.

Johnson, R. A. and Wichern, D. A. (1988) Applied Multivariate Statistical
Analysis. Englewood Cliffs, N. J .: Prentice Hall.

<!-- PageBreak -->

<!-- PageHeader="298 References" -->

Johnstone, I. M. and Silverman, B. W. (1997) Wavelet threshold
estimators for data with correlated noise. Journal of the Royal
Statistical Society, Series B, 59, 319-351.

Karhunen, K. (1947) Über linear Methoden in der Warscheinlichkeits-
rechnung. Annales Academiae Scientiorum Fennicae, 37, 1-79.

Keselman, H. J. and Keselman, J. C. (1993) Analysis of repeated
measurements. In L. K. Edwards (ed.) Applied Analysis of Variance
in Behavioral Science. New York: Marcel Dekker, pp. 105-145.

Kimeldorf, G. S. and Wahba, G. (1970) A correspondence between
Bayesian estimation on stochastic processes and smoothing by
splines. Annals of Mathematical Statistics, 41, 495-502.

Kneip, A. (1994) Nonparametric estimation of common regressors for
similar curve data. Annals of Statistics, 22, 1386-1427.

Kneip, A. and Engel, J. (1995) Model estimation in nonlinear regression
under shape invariance. Annals of Statistics, 23, 551-570.

Kneip, A. and Gasser, T. (1988) Convergence and consistency results for
self-modeling nonlinear regression. Annals of Statistics, 16, 82-112.

Kneip, A. and Gasser, T. (1992) Statistical tools to analyze data
representing a sample of curves. Annals of Statistics, 20, 1266-1305.

Largo, R. H., Gasser, T., Prader, A., Stützle, W. and Huber, P. J. (1978)
Analysis of the adolescent growth spurt using smoothing spline
functions. Annals of Human Biology, 5, 421-434.

Legendre, A. M. (1805) Nouvelles méthodes pour la détermination des
orbites des comètes. Paris: Courcier.

Leurgans, S. E., Moyeed, R. A. and Silverman, B. W. (1993) Canonical
correlation analysis when the data are curves. Journal of the Royal
Statistical Society, Series B, 55, 725-740.

Lindsey, J. K. (1993) Models for Repeated Measurements. New York:
Oxford University Press.

Loève, M. (1945) Fonctions aléatoires de second ordre. Comptes Rendus
de l'Académie des Sciences, Série I: Mathématique, 220, 469.

MathWorks Inc. (1993) MATLAB Reference Guide. Natick, Mass .: The
MathWorks Inc.

Maxwell, S. E. and Delaney, H. D. (1990) Designing Experiments and
Analyzing Data: A Model Comparison Perspective. Belmont, Calif .:
Wadsworth.

Mulaik, S. A. (1972) The Foundations of Factor Analysis. New York:
McGraw-Hill.

<!-- PageBreak -->

<!-- PageNumber="299" -->
<!-- PageHeader="References" -->

Nadaraya, E. A. (1964) On estimating regression. Theory of Probability
and its Applications, 10, 186-190.

Nason, G. P. and Silverman, B. W. (1994) The discrete wavelet transform
in S. Journal of Computational and Graphical Statistics, 3, 163-191.

OECD (1995) Quarterly National Accounts, 3.

Øksendal, B. (1995) Stochastic Differential Equations: An Introduction
with Applications. New York: Springer.

Olshen, R. A., Biden, E., N., Wyatt, M. P. and Sutherland, D. H. (1989) Gait
analysis and the bootstrap. Annals of Statistics, 17, 1419-1440.

Parzen, E. (1961) An approach to time series analysis. Annals of
Mathematical Statistics, 32, 951-989.

Parzen, E. (1963) Probability density functionals and reproducing
kernel Hilbert spaces, In M. Rosenblatt (ed.) Proceedings of
the Symposium on Time Series Analysis. Providence, RI .: Brown
University, pp. 155-169.

Pezzulli, S. D. and Silverman, B. W. (1993) Some properties of smoothed
principal components analysis for functional data. Computational
Statistics, 8, 1-16.

Pousse, A. (1992) Etudes asymptotiques. In J .- J. Droesbeke, B.
Fichet and P. Tassi (eds) Modèles pour l'Analyse des Données
Multidimensionelles. Paris: Economica.

Press W. H., Teukolsky S. A., Vetterling W. T. and Flannery B. P.
(1992) Numerical Recipes in Fortran. Second edition. Cambridge:
Cambridge University Press.

Ramsay, J. O. (1982). When the data are functions. Psychometrika, 47,
379-396.

Ramsay, J. O. (1989) The data analysis of vector-valued functions.
In E. Diday (ed.) Data Analysis, Learning Symbolic and Numeric
Knowledge. Commack, N. Y .: Nova Science Publishers.

Ramsay, J. O. (1996a) Principal differential analysis: data reduction by
differential operators. Journal of the Royal Statistical Society, Series
B, 58, 495-508.

Ramsay, J. O. (1996b) Estimating smooth monotone functions. McGill
University: unpublished manuscript.

Ramsay, J. O. (1996c) Pspline: An S-PLUS module for polynomial spline
smoothing. Computer software in the statlib archive.

<!-- PageBreak -->

<!-- PageHeader="300 References" -->

Ramsay, J. O., Altman, N. and Bock, R. D. (1994) Variation in height
acceleration in the Fels growth data. Canadian Journal of Statistics,
22, 89-102.

Ramsay, J. O., Bock. R. D. and Gasser, T. (1995) Comparison of height
acceleration curves in the Fels, Zurich, and Berkeley growth data.
Annals of Human Biology, 22, 413-426.

Ramsay, J. O. and Dalzell, C. J. (1991) Some tools for functional data
analysis (with Discussion). Journal of the Royal Statistical Society,
Series B, 53, 539-572.

Ramsay, J. O, Heckman, N. and Silverman, B. W. (1997) Some general
theory for spline smoothing. Behavioral Research: Instrumentation,
Methods, and Computing, to appear.

Ramsay, J. O. and Li, X. (1996) Curve registration. McGill University,
unpublished manuscript.

Ramsay, J. O., Munhall, K., Gracco, V. L. and Ostry, D. J. (1996) Functional
data analyses of lip motion. Journal of the Acoustical Society of
America, 99, 3718-3727.

Ramsay, J. O., Wang, X. and Flanagan, R. (1995) A functional data
analysis of the pinch force of human fingers. Applied Statistics, 44,
17-30.

Rao, C. R. (1958) Some statistical methods for comparison of growth
curves. Biometrics, 14, 1-17.

Rao, C. R. (1987) Prediction in growth curve models (with discussion).
Statistical Science, 2, 434-471.

Reinsch, C. (1967) Smoothing by spline functions. Numerische
Mathematik, 10, 177-183.

Reinsch, C. (1970) Smoothing by spline functions II. Numerische
Mathematik, 16, 451-454.

Rice, J. A. and Silverman, B. W. (1991) Estimating the mean and
covariance structure nonparametrically when the data are curves.
Journal of the Royal Statistical Society, Series B, 53, 233-243.

Riesz, $F .$ and Nagy, B. Sz .- (1956) Functional Analysis. (Translated by L.
F. Boron.) London: Blackie.

Ripley, B. D. (1991) Statistical Inference for Spatial Processes. Cambridge:
Cambridge University Press.

Roach, G. F. (1982) Green's Functions. Second edition. Cambridge:
Cambridge University Press.

<!-- PageBreak -->

<!-- PageNumber="301" -->
<!-- PageHeader="References" -->

Roche, A. (1992) Growth, Maturation and Body Composition: The Fels
Longitudinal Study 1929-1991. Cambridge: Cambridge Press.

Scott, D. W. (1992) Multivariate Density Estimation. New York: John
Wiley & Sons.

Schumaker, L. (1981) Spline Functions: Basic Theory. New York: John
Wiley & Sons.

Seber, G. A. F. (1984) Multivariate Observations. New York: John Wiley
& Sons.

Silverman, B. W. (1985) Some aspects of the spline smoothing approach
to non-parametric regression curve fitting. Journal of the Royal
Statistical Society, Series B, 47, 1-52.

Silverman, B. W. (1994) Function estimation and functional data
analysis. In A. Joseph, F. Mignot, $F .$ Murat, $B .$ Prum and $R .$ Rentschler
(eds) First European Congress of Mathematics. Basel: Birkhäuser. Vol
II, pp 407-427.

Silverman, B. W. (1995). Incorporating parametric effects into
functional principal components analysis. Journal of the Royal
Statistical Society, Series B, 57, 673-689.

Silverman, B. W. (1996) Smoothed functional principal components
analysis by choice of norm. Annals of Statistics, 24, 1-24.

Simonoff, J. S. (1996) Smoothing Methods in Statistics. New York:
Springer.

Small, C. G. and McLeish, D. L. (1994) Hilbert Space Methods in
Probability and Statistical Inference. New York: John Wiley & Sons.

Statistical Sciences (1995) S-PLUS Guide to Statistical and Mathematical
Analysis, Version 3.3. Seattle: StatSci, a division of MathSoft, Inc.

Stoer, $\mathrm { J } .$ and Bulirsch, R. (1980) Introduction to Numerical Analysis. New
York: Springer.

Stone, M. (1987) Coordinate-Free Multivariable Statistics. Oxford:
Clarendon Press.

Tenenbaum, $M .$ and Pollard, H. (1963) Ordinary Differential Equations.
New York: Harper and Row.

Tucker, L. R. (1958) Determination of parameters of a functional
relationship by factor analysis. Psychometrika, 23, 19-23.

Vinod, H. D. (1976) Canonical ridge and econometrics of joint
production. Journal of Econometrics, 4, 147-166.

<!-- PageBreak -->

<!-- PageHeader="302 References" -->

Wahba, G. (1978) Improper priors, spline smoothing and the problem
of guarding against model errors in regression. Journal of the Royal
Statistical Society, Series B, 40, 364-372.

Wahba, G. (1990) Spline Models for Observational Data. Philadelphia:
Society for Industrial and Applied Mathematics.

Wand, M. P. and Jones, M. C. (1995) Kernel Smoothing. London:
Chapman and Hall.

Watson, G. S. (1964) Smooth regression analysis. Sankhya, Series A, 26,
101-116.

Weinert, H. L., Byrd, R. H. and Sidhu, G. S. (1980) A stochastic framework
for recursive computation of spline functions: Part II, smoothing
splines. Journal of Optimization Theory and Applications, 2, 255-
268.

Wilson, A. M., Seelig, T. J., Shield, R. A. and Silverman, B. W. (1996) The
effect of imposed foot imbalance on point of force application in the
equine. Technical report, Department of Veterinary Basic Sciences,
Royal Veterinary College.

Wolfram, S. (1991) Mathematica: A System for Doing Mathematics by
Computer. Second edition. Reading, Mass .: Addison-Wesley.

<!-- PageBreak -->

Index


<table>
<tr>
<th>alignment, see registration amplitude modulated sinusoid,</th>
<th>polynomial, 48 regression spline, 48-49</th>
</tr>
<tr>
<td>228-230</td>
<td>reproducing kernel, 261-262</td>
</tr>
<tr>
<td>ANOVA</td>
<td>wavelets, 49-51</td>
</tr>
<tr>
<td>functional, 140-155</td>
<td>Bayesian regression, 36</td>
</tr>
<tr>
<td>repeated measures, 278-279</td>
<td>between-class variance, 215</td>
</tr>
<tr>
<td>B-spline, 48-49, 163-164, 261</td>
<td>bilinearity for inner products, 26</td>
</tr>
<tr>
<td>band-structured matrix, 43, 264</td>
<td>boundary value operator, 232</td>
</tr>
<tr>
<td>bandwidth, see smoothing parameter</td>
<td>Brent's method, 270</td>
</tr>
<tr>
<td>basis functions</td>
<td>Canadian climate data,</td>
</tr>
<tr>
<td>B-spline, 163-164, 261</td>
<td>see climate data</td>
</tr>
<tr>
<td>choosing, 46</td>
<td>canonical correlation analysis</td>
</tr>
<tr>
<td>choosing number, 45-46</td>
<td>algorithmic considerations,</td>
</tr>
<tr>
<td>compact support, 268</td>
<td>211-214</td>
</tr>
<tr>
<td>Fourier series, 46, 100-102, 115-117, 123, 161-162, 225</td>
<td>canonical correlation, 201 canonical variate, 200 eigenequation, 200-202, 204,</td>
</tr>
<tr>
<td>general remarks, 44-51</td>
<td>212-214</td>
</tr>
<tr>
<td>in PDA, 249-251</td>
<td>functional formulation,</td>
</tr>
<tr>
<td>in linear model, 153-154,</td>
<td>202-204</td>
</tr>
<tr>
<td>180-189</td>
<td>general remarks, 17-18,</td>
</tr>
<tr>
<td>optimal, 261-265</td>
<td>199-200</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="304 Index" -->

canonical correlation analysis
incorporating smoothing, 204
linear discriminant analysis,
215-216
multivariate, 200-202
regularization, need for,
210-211

roughness penalties, 203-204,
213-214

subsidiary variates, 201, 205
canonical variate, 200
Cauchy-Schwarz inequality, 27
CCA, see canonical correlation
analysis

climate data, 3-5, 15-16, 17, 20,
70-71, 89-98, 131-137,
140-145, 159-167,
182-193, 259-261

compact support splines, 49
confirmatory data analysis, 8
constraint operator, 230-232
correlation

between functions, 11-13
between derivatives, 18-19
cross, 13-16
inequality, 29
cosine inequality, 27-28

covariance function, 11-13, 91
covariance operator, 92

cross-correlation function,
13-16
cross-covariance function, 13
cross-validation
for CCA, 205
for L-splines, 266
for linear models, 165-166,
174-176
for PCA, 118-119
cubic spline, 49
curve alignment, see registration
curve registration,
see registration

CV, see cross-validation
cycle plots, 7

D notation for differentiation,

24-25, 37
damping, 241, 247
data analysis
confirmatory, 8
exploratory, 8
data registration, see registration
degrees of freedom, 267
see also F-ratio function

deleted residuals, 175
derivatives

correlation plots for, 18-19
estimating, 41, 46-47
noise in, 42

notation, 24-25
plotting pairs of, 18-19
spline estimation, 60
use of, 18
see also principal differen-
tial analysis

differential equation

homogeneous, 221

linear, 227-231
references, 227
stochastic, 267, 281
differential operator, see linear
differential operator

direct penalty method
for linear models, 170-174

discriminant
for differential operators, 241,
247

analysis, 215-216
domain variation, 68

empirical forcing function, 246
errata, 21

<!-- PageBreak -->

<!-- PageNumber="305" -->
<!-- PageHeader="Index" -->


<table>
<tr>
<th>error, general remarks discrete, 38-39 functional, 41-42</th>
<th>generalized eigenproblem, 291 see also canonical correla- tion analysis</th>
</tr>
<tr>
<td>observational, 38-42</td>
<td>generalized inverse</td>
</tr>
<tr>
<td>Euclidean inner product, 25</td>
<td>definition, 286</td>
</tr>
<tr>
<td>evaluation functional, 196 evaluation values of a smooth,</td>
<td rowspan="2">goals of functional data analysis, 8-9 grand mean function, 140</td>
</tr>
<tr>
<td>43</td>
</tr>
<tr>
<td>exploratory data analysis, 8</td>
<td>Green's function, 234-238 gross domestic product data,</td>
</tr>
<tr>
<td>F-ratio function, 144, 192, 252</td>
<td>218-219, 269-273</td>
</tr>
<tr>
<td>factor analysis, 99</td>
<td>growth data, 1-3, 81-82, 105,</td>
</tr>
<tr>
<td>FANOVA, see linear model</td>
<td>273-276</td>
</tr>
<tr>
<td>feature alignment, see registration</td>
<td>handwriting data, 39-41, 53-54,</td>
</tr>
<tr>
<td>fixed effects, 69</td>
<td>74-78</td>
</tr>
<tr>
<td>force plate data, 145-152</td>
<td>hard-edged constraints, 35</td>
</tr>
<tr>
<td>forcing function, 4, 234, 245</td>
<td rowspan="2">harmonic acceleration, 260 harmonics, see principal compo-</td>
</tr>
<tr>
<td>Fourier series, see basis functions</td>
</tr>
<tr>
<td>FRATIO, definition, 144, 192, 252</td>
<td>nents analysis hat matrix, see smoothing</td>
</tr>
<tr>
<td>functional analysis, 280</td>
<td>matrix</td>
</tr>
<tr>
<td>functional interpolation, 158-160,</td>
<td rowspan="2">hip angles, see gait data home page, 21</td>
</tr>
<tr>
<td>172-174</td>
</tr>
<tr>
<td>functional principal components analysis, see principal com-</td>
<td>hybrid data, 126-130</td>
</tr>
<tr>
<td>ponents analysis</td>
<td>impulse function, see forcing</td>
</tr>
<tr>
<td>functions</td>
<td rowspan="2">function IMSE, definition, 223 initial processing, 9-11</td>
</tr>
<tr>
<td>notation for, 24</td>
</tr>
<tr>
<td>g-inverse, see generalized inverse</td>
<td rowspan="2">initial value operator, 232, 269 inner product</td>
</tr>
<tr>
<td>gait data, 5-7, 13-15, 17, 94,</td>
</tr>
<tr>
<td>106-109, 199, 205-208</td>
<td>defined by LDO, 233-234</td>
</tr>
<tr>
<td>GCV, see generalized cross-validation</td>
<td rowspan="2">definitions of descriptive statistics, 29-30</td>
</tr>
<tr>
<td>GDP, see gross domestic</td>
</tr>
<tr>
<td>product</td>
<td>Euclidean, 25</td>
</tr>
<tr>
<td>generalized cross-validation</td>
<td>for hybrid data, 127, 130</td>
</tr>
<tr>
<td>for gross domestic product</td>
<td>general properties, 27-29</td>
</tr>
<tr>
<td>data, 270, 272</td>
<td>in PCA, 106</td>
</tr>
<tr>
<td>for growth data, 274-275</td>
<td>notation, 23-27</td>
</tr>
<tr>
<td>for L-splines, 266</td>
<td>extensions, 30-31</td>
</tr>
<tr>
<td>for melanoma data, 271</td>
<td>integral equations, 176</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="306" -->
<!-- PageHeader="Index" -->

integral transform, 92
integrated value operator, 260
Internet, 21

Kalman filter, 267
kernel

Gaussian, 51
quadratic, 51

smoothing, 51-54
uniform, 51

knee angles, see gait data
knots, see spline

L-splines

assessing performance, 266
compact support basis for,
268-269
degrees of freedom, 267

general remarks, 61-62,
257-258

$O \left( n \right)$ algorithm, 263-268
optimal basis for, 261-262
landmark, 73
landmark alignment, see regis-
tration

LDO, see linear differential
operators

leverage values, 175

linear differential operators,
4-5, 61-62
compared with projection,
224

for new observations,
220-221

for smoothing, 221-223

in linear model, 196
inversion, 235

null space, 224
solutions to problems,
225-226
to annihilate functions,
228-230

to partition variation,
223-225, 232-233
weight functions, 218-219
linear discriminant analysis,
215-216

linear model

ANOVA, 140-155, 278-279

computation, 152-155
direct penalty method,
170-174
FRATIO function, 144, 192
functional interpolation,
158-159

general remarks, 16-17
grand mean function, 140
integral equations, 176
linear differential operators,
196
MSE function, 144
nonparametric regression,
166-168
pointwise multivariate, 195
regularization, 154
basis functions, 161-164
discretization, 160-161
roughness penalty,
161-164
restricting basis

both bases, 187-189
predictor, 184-185

response, 185-187

roughness penalties, 193-194
RSQ function, 143, 190
specific effect function, 140
spline smoothing, 195-196
SSE function, 143
weighted integrals, 197

LINPACK, 285

lip data, 240-248, 258-259

LMISE, definition, 18

LMSSE, definition, 33, 34, 154

<!-- PageBreak -->

<!-- PageNumber="307" -->
<!-- PageHeader="Index" -->


<table>
<tr>
<th>local polynomial smoothing, 55</th>
<th rowspan="3">operator notation, 25 optimal basis theorem, 261-262 optimal scoring, 214-215 OSERR, definition, 214-215</th>
</tr>
<tr>
<td>longitudinal data analysis, 279</td>
</tr>
<tr>
<td>lupus data, 208-210</td>
</tr>
<tr>
<td>MATLAB, 285</td>
<td></td>
</tr>
<tr>
<td>mean function, 11, 78</td>
<td></td>
</tr>
<tr>
<td>measures of association, 27</td>
<td></td>
</tr>
<tr>
<td>melanoma data, 219-220,</td>
<td>partitioning principle, 258</td>
</tr>
<tr>
<td>271-272</td>
<td>PCA, see principal components</td>
</tr>
<tr>
<td>mother wavelet, 49</td>
<td>analysis</td>
</tr>
<tr>
<td>MSE, definition, 144</td>
<td>PCAPSV, definition, 114</td>
</tr>
<tr>
<td>MSR, definition, 144</td>
<td rowspan="2">PDA, see principal differential analysis</td>
</tr>
<tr>
<td>multidimensional function</td>
</tr>
<tr>
<td>arguments, 282</td>
<td></td>
</tr>
<tr>
<td>multiresolution analysis,</td>
<td>PEN, definition, 59-61, 63, 193</td>
</tr>
<tr>
<td>see wavelets</td>
<td>penalized covariance, 205</td>
</tr>
<tr>
<td>multivariate functional data,</td>
<td>penalized discriminant analysis,</td>
</tr>
<tr>
<td>5-6, 17-18</td>
<td>215-216</td>
</tr>
<tr>
<td>in PCA, 105-107</td>
<td>penalized least squares, 154, 164,</td>
</tr>
<tr>
<td>multivariate linear model, 32-34</td>
<td>169</td>
</tr>
<tr>
<td></td>
<td>penalized optimal scoring, 215</td>
</tr>
<tr>
<td>natural boundary conditions, 113</td>
<td>penalized sample variance, 114</td>
</tr>
<tr>
<td>Newton-Raphson algorithm, 71</td>
<td rowspan="2">penalized squared correlation, 204</td>
</tr>
<tr>
<td>nonparametric regression,</td>
</tr>
<tr>
<td>166-168</td>
<td>penalized sum of squares, 59,</td>
</tr>
<tr>
<td>norm, definition, 27, 234</td>
<td>222-223, 225, 251</td>
</tr>
<tr>
<td>for hybrid data, 126-130</td>
<td>PENRSS, definition, 122</td>
</tr>
<tr>
<td>for multivariate functional</td>
<td>PENSSE, definition, 59, 64, 164,</td>
</tr>
<tr>
<td>data, 106</td>
<td>225, 251, 258</td>
</tr>
<tr>
<td>in PCA with registration, 132</td>
<td>periodic boundary conditions, 38,</td>
</tr>
<tr>
<td>notation</td>
<td>113, 232</td>
</tr>
<tr>
<td>differentiation, 24-25, 37</td>
<td rowspan="2">periodic constraint operator, 232</td>
</tr>
<tr>
<td>for functions, 24</td>
</tr>
<tr>
<td>for linear differential operator, 218</td>
<td>perturbations of mean, 92-94 Picard's algorithm, 230-231</td>
</tr>
<tr>
<td>for vectors, 24</td>
<td>pinch force data, 9-10, 12-13,</td>
</tr>
<tr>
<td>inner product, 23-27</td>
<td>69, 73, 112, 120-124,</td>
</tr>
<tr>
<td>operator, 25</td>
<td>252-256</td>
</tr>
<tr>
<td>nuisance effects, 69</td>
<td>polynomial, see basis functions</td>
</tr>
<tr>
<td>null space, see linear different-</td>
<td>positivity</td>
</tr>
<tr>
<td>ial operator</td>
<td>for inner product, 26</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="308 Index" -->


<table>
<tr>
<th>principal components analysis</th>
<th rowspan="2">QR decomposition, 264, 287 quadrature</th>
</tr>
<tr>
<td>component scores, 94-95</td>
</tr>
<tr>
<td>computational methods</td>
<td>Gaussian, 103</td>
</tr>
<tr>
<td>basis expansion, 100-103 discretization, 99-100 quadrature, 105 regularized nonperiodic, 117-118</td>
<td>points, 103 weights, 103 see also trapezoidal rule</td>
</tr>
<tr>
<td>regularized periodic, 116-117</td>
<td>random effects, 69</td>
</tr>
<tr>
<td>cross-validation, 118-119</td>
<td>range variation, 68</td>
</tr>
<tr>
<td>definition</td>
<td rowspan="3">registration general remarks, 9-10, 67-83</td>
</tr>
<tr>
<td>functional, 87-89</td>
</tr>
<tr>
<td>multivariate, 86-87</td>
</tr>
<tr>
<td>eigenequation, 91-92, 99-102,</td>
<td rowspan="2">landmark, 73-78 PCA, 131-136</td>
</tr>
<tr>
<td>115-118</td>
</tr>
<tr>
<td>empirical orthogonal basis,</td>
<td rowspan="2">Procrustes method, 71, 79 shift, 68-73, 131-136</td>
</tr>
<tr>
<td>90</td>
</tr>
<tr>
<td>functional multivariate, 105-107</td>
<td>regression spline, see basis func- tions, spline</td>
</tr>
<tr>
<td>general remarks, 16, 85-86</td>
<td>REGSSE, definition, 71, 81</td>
</tr>
<tr>
<td>harmonics, 89</td>
<td>regularization</td>
</tr>
<tr>
<td>plotting, 92-94</td>
<td>basis functions, 62-65</td>
</tr>
<tr>
<td>registration, 131-136</td>
<td>by imposing constraints,</td>
</tr>
<tr>
<td>rotation, 95-99</td>
<td>35-36</td>
</tr>
<tr>
<td>roughness penalties, 113-114</td>
<td>general remarks, 18</td>
</tr>
<tr>
<td>principal differential analysis</td>
<td>in CCA, 203-214</td>
</tr>
<tr>
<td>basis expansion method,</td>
<td>in functional linear model,</td>
</tr>
<tr>
<td>249-251</td>
<td>154, 160-170, 184-188</td>
</tr>
<tr>
<td>compared with PCA, 242-245 definition, 240</td>
<td>in multivariate linear model, 34-36</td>
</tr>
<tr>
<td>general remarks, 20 pointwise method, 248-249 roughness penalties, 251</td>
<td>in PCA, 111-124, 128-129 in PDA, 251</td>
</tr>
<tr>
<td>Procrustes method, 71, 79</td>
<td>monotone functions, 81</td>
</tr>
<tr>
<td>projection</td>
<td>spline smoothing, 58-62</td>
</tr>
<tr>
<td>definition, 31-32</td>
<td>see also L-splines</td>
</tr>
<tr>
<td>matrices, 287-289</td>
<td>relative curvature, 80</td>
</tr>
<tr>
<td>metric, 45</td>
<td>reproducing kernel, 237-238,</td>
</tr>
<tr>
<td>operator, 224</td>
<td>261-264, 268</td>
</tr>
<tr>
<td>orthogonal, 44</td>
<td>reproducing kernel matrix, 263</td>
</tr>
<tr>
<td>PSSE, definition, 248</td>
<td>ridge regression, 35</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="309" -->
<!-- PageHeader="Index" -->


<table>
<tr>
<th rowspan="2">RMSE, definition, 276 roughness penalty</th>
<th>smoothing parameter</th>
</tr>
<tr>
<th rowspan="2">choosing, general remarks, 55-56</th>
</tr>
<tr>
<td rowspan="2">basis function expression, 63-65</td>
</tr>
<tr>
<td rowspan="2">for regularized basis func- tions, 65</td>
</tr>
<tr>
<td>bivariate, 193-194</td>
</tr>
<tr>
<td rowspan="2">in CCA, 203-204, 213-214 in linear model, 161-164 in PCA, 113-114 spline smoothing, 58-62 see also regularization</td>
<td>in kernel smoothing, 51</td>
</tr>
<tr>
<td>in linear model, 164-166, 174-176 in CCA, 205 in PCA, 118-120 in spline smoothing, 59-60</td>
</tr>
<tr>
<td>RSQ, definition, 143, 246, 252</td>
<td>SMSSE, definition, 44, 54 soft-edged constraints, 36 software, 21 specific effect function, 140</td>
</tr>
<tr>
<td>S-PLUS, 11, 21, 285</td>
<td>spline</td>
</tr>
<tr>
<td>self-adjoint operator, 32</td>
<td>B-spline, 48-49</td>
</tr>
<tr>
<td>self-modeling regression, 72</td>
<td>cubic, 49</td>
</tr>
<tr>
<td>semi-inner product, 28-29</td>
<td>derivative estimate, 60</td>
</tr>
<tr>
<td>seminorm, 29</td>
<td>knots, 48-49</td>
</tr>
<tr>
<td>singular value decomposition</td>
<td>regression spline, 48-49</td>
</tr>
<tr>
<td>definition, 285-286</td>
<td>smoothing, 58-62</td>
</tr>
<tr>
<td>smoothing</td>
<td>truncated power basis, 49</td>
</tr>
<tr>
<td>basis function methods,</td>
<td>see also L-splines</td>
</tr>
<tr>
<td>44-51</td>
<td>spring constant, 241</td>
</tr>
<tr>
<td>degrees of freedom, 267</td>
<td>squared correlation function, 143,</td>
</tr>
<tr>
<td>general remarks, 43-44</td>
<td>189-190, 252</td>
</tr>
<tr>
<td>kernel, 51-54</td>
<td>squeeze force data, see pinch force</td>
</tr>
<tr>
<td>linear, 43</td>
<td>data</td>
</tr>
<tr>
<td>local basis, 54</td>
<td>SSE, definition, 143, 240, 243 SSY, definition, 143</td>
</tr>
<tr>
<td rowspan="2">local polynomial, 55 nonlinear, 50</td>
<td>structural average, 78</td>
</tr>
<tr>
<td>successive approximation, see</td>
</tr>
<tr>
<td>$O \left( n \right)$ algorithm, 43, 263-268 objectives, 58-59</td>
<td>Picard's method summary statistics, 11-16</td>
</tr>
<tr>
<td>spline, 58-62</td>
<td>SVD, see singular value decom-</td>
</tr>
<tr>
<td>see also regularization</td>
<td>position</td>
</tr>
<tr>
<td>smoothing matrix, 43-45,</td>
<td>symmetry</td>
</tr>
<tr>
<td>174-175</td>
<td>for inner products, 25</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="310" -->
<!-- PageHeader="Index" -->


<table>
<tr>
<th>time-warping function, 77</th>
<th>weather data, see climate data</th>
</tr>
<tr>
<td>transformations</td>
<td>weather stations, 96</td>
</tr>
<tr>
<td>general monotonic, 79-83</td>
<td>weight functions</td>
</tr>
<tr>
<td>shift, 68</td>
<td>estimated in PDA, 248-252</td>
</tr>
<tr>
<td>trapezoidal rule, 64, 103, 231,</td>
<td>linear differential operator,</td>
</tr>
<tr>
<td>251, 275</td>
<td>218-219</td>
</tr>
<tr>
<td>truncated power basis, see spline</td>
<td>in PCA, 88</td>
</tr>
<tr>
<td>two-stage minimization, 171-173</td>
<td>weight constants least squares, 45</td>
</tr>
<tr>
<td>variance function</td>
<td>linear differential operator,</td>
</tr>
<tr>
<td>definition 11</td>
<td>4-5</td>
</tr>
<tr>
<td>VARIMAX rotation, 96-99</td>
<td>within-class variance, 215 world-wide web, 21</td>
</tr>
<tr>
<td>warping function, 77</td>
<td>Wronskian function, 229</td>
</tr>
<tr>
<td>wavelets, 49-51</td>
<td>Wronskian matrix, 229</td>
</tr>
</table>


<!-- PageBreak -->


## Springer Series in Statistics (continued from p. ii)

Knottnerus: Sample Survey Theory: Some Pythagorean Perspectives.

Kotz/Johnson (Eds.): Breakthroughs in Statistics Volume I.

Kotz/Johnson (Eds.): Breakthroughs in Statistics Volume II.

Kotz/Johnson (Eds.): Breakthroughs in Statistics Volume III.

Küchler/Sørensen: Exponential Families of Stochastic Processes.
Le Cam: Asymptotic Methods in Statistical Decision Theory.
Le Cam/Yang: Asymptotics in Statistics: Some Basic Concepts, 2nd edition.

Liu: Monte Carlo Strategies in Scientific Computing.
Longford: Models for Uncertainty in Educational Testing.

Mielke/Berry: Permutation Methods: A Distance Function Approach.

Pan/Fang: Growth Curve Models and Statistical Diagnostics.

Parzen/Tanabe/Kitagawa: Selected Papers of Hirotugu Akaike.
Politis/Romano/Wolf: Subsampling.

Ramsay/Silverman: Applied Functional Data Analysis: Methods and Case Studies.

Ramsay/Silverman: Functional Data Analysis.

Rao/Toutenburg: Linear Models: Least Squares and Alternatives.

Reinsel: Elements of Multivariate Time Series Analysis, 2nd edition.

Rosenbaum: Observational Studies, 2nd edition.

Rosenblatt: Gaussian and Non-Gaussian Linear Time Series and Random Fields.

Särndal/Swensson/Wretman: Model Assisted Survey Sampling.

Schervish: Theory of Statistics.

Shao/Tu: The Jackknife and Bootstrap.

Simonoff: Smoothing Methods in Statistics.

Singpurwalla and Wilson: Statistical Methods in Software Engineering:
Reliability and Risk.

Small: The Statistical Theory of Shape.

Sprott: Statistical Inference in Science.

Stein: Interpolation of Spatial Data: Some Theory for Kriging.

Taniguchi/Kakizawa: Asymptotic Theory of Statistical Inference for Time Series.

Tanner: Tools for Statistical Inference: Methods for the Exploration of Posterior
Distributions and Likelihood Functions, 3rd edition.

van der Laan: Unified Methods for Censored Longitudinal Data and Causality.

van der Vaart/Wellner: Weak Convergence and Empirical Processes: With
Applications to Statistics.

Verbeke/Molenberghs: Linear Mixed Models for Longitudinal Data.

Weerahandi: Exact Statistical Methods for Data Analysis.

West/Harrison: Bayesian Forecasting and Dynamic Models, 2nd edition.
