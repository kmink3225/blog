<!-- PageHeader="Texts in Statistical Science" -->


# Extending the Linear Model with R

Generalized Linear,
Mixed Effects and
Nonparametric Regression
Models


<figure>

15

10

5

0

-20 -15 -10 -5

-3 -2 -1 0 1 2 3

</figure>


<figure>

15

10

5

&

0

-20 -15 -10

15

20

25

30

35

40

</figure>


Julian J. Faraway


<figure>

Taylor & Francis
Taylor & Francis Group

CRC

</figure>


Also available as a printed book
see title verso for ISBN details

<!-- PageBreak -->

CHAPMAN & HALL/CRC
Texts in Statistical Science Series
Series Editors

Bradley P.Carlin, University of Minnesota, USA
Chris Chatfield, University of Bath, UK
Martin Tanner, Northwestern University, USA
Jim Zidek, University of British Columbia, Canada

Analysis of Failure and Survival Data
Peter J.Smith

The Analysis and Interpretation of Multivariate Data for Social Scientists
David J.Bartholomew, Fiona Steele, Irini Moustaki, and Jane Galbraith

The Analysis of Time Series-An Introduction, Sixth Edition
Chris Chatfield

Applied Bayesian Forecasting and Time Series Analysis
A.Pole, M.West and J.Harrison

Applied Nonparametric Statistical Methods, Third Edition
P.Sprent and N.C.Smeeton

Applied Statistics-Handbook of GENSTAT Analysis
E.J.Snell and H.Simpson

Applied Statistics-Principles and Examples
D.R.Cox and E.J.Snell

Bayes and Empirical Bayes Methods for Data Analysis, Second Edition
Bradley P.Carlin and Thomas A.Louis

Bayesian Data Analysis, Second Edition
Andrew Gelman, John B.Carlin, Hal S.Stern, and Donald B.Rubin

Beyond ANOVA-Basics of Applied Statistics
R.G.Miller, Jr.

<!-- PageBreak -->


## Computer-Aided Multivariate Analysis, Fourth Edition A.A.Afifi and V.A.Clark

A Course in Categorical Data Analysis
T.Leonard

A Course in Large Sample Theory
T.S.Ferguson

Data Driven Statistical Methods
P.Sprent

Decision Analysis-A Bayesian Approach
J.Q.Smith

Elementary Applications of Probability Theory, Second Edition
H.C.Tuckwell

Elements of Simulation
B.J.T.Morgan

Epidemiology-Study Design and Data Analysis, Second Edition
M.Woodward

Essential Statistics, Fourth Edition
D.A.G.Rees

Extending the Linear Model with R: Generalized Linear, Mixed Effects and
Nonparametric Regression Models
Julian J.Faraway

A First Course in Linear Model Theory
Nalini Ravishanker and Dipak K.Dey

Interpreting Data-A First Course in Statistics
A.J.B.Anderson

An Introduction to Generalized Linear Models, Second Edition
A.J.Dobson

Introduction to Multivariate Analysis
C.Chatfield and A.J.Collins

Introduction to Optimization Methods and Their Applications in Statistics
B.S.Everitt

<!-- PageBreak -->


## Large Sample Methods in Statistics P.K.Sen and J.da Motta Singer

Linear Models with $\mathrm { R }$
Julian J.Faraway

Markov Chain Monte Carlo-Stochastic Simulation for Bayesian Inference
D.Gamerman

Mathematical Statistics
K.Knight

Modeling and Analysis of Stochastic Systems
V.Kulkarni

Modelling Binary Data, Second Edition
D.Collett

Modelling Survival Data in Medical Research, Second Edition
D.Collett

Multivariate Analysis of Variance and Repeated Measures-A Practical Approach
for Behavioural Scientists
D.J.Hand and C.C.Taylor

Multivariate Statistics-A Practical Approach
B.Flury and H.Riedwyl

Practical Data Analysis for Designed Experiments
B.S. Yandell

Practical Longitudinal Data Analysis
D.J.Hand and M.Crowder

Practical Statistics for Medical Research
D.G.Altman

Probability-Methods and Measurement
A.O'Hagan

Problem Solving-A Statistician's Guide, Second Edition
C.Chatfield

Randomization, Bootstrap and Monte Carlo Methods in Biology, Second Edition
B.F.J.Manly

<!-- PageBreak -->


## Readings in Decision Analysis S.French

Sampling Methodologies with Applications
Poduri S.R.S.Rao

Spatial Data Analysis
Oliver Schabenberger and Carol A.Gotway

Statistical Analysis of Reliability Data
M.J.Crowder, A.C.Kimber, T.J.Sweeting, and R.L.Smith

Statistical Methods for Spatial Data Analysis
Oliver Schabenberger and Carol A.Gotway

Statistical Methods for SPC and TQM
D.Bissell

Statistical Methods in Agriculture and Experimental Biology, Second Edition
R.Mead, R.N.Curnow, and A.M.Hasted

Statistical Process Control-Theory and Practice, Third Edition
G.B. Wetherill and D.W.Brown

Statistical Theory, Fourth Edition
B.W.Lindgren

Statistics for Accountants
S.Letchford

Statistics for Epidemiology
Nicholas P.Jewell

Statistics for Technology-A Course in Applied Statistics, Third Edition
C.Chatfield

Statistics in Engineering-A Practical Approach
A. V.Metcalfe

Statistics in Research and Development, Second Edition
R.Caulcutt

Survival Analysis Using S-Analysis of Time-to-Event Data
Mara Tableman and Jong Sung Kim

<!-- PageBreak -->


## The Theory of Linear Models B.Jørgensen

Texts in Statistical Science

<!-- PageBreak -->

Extending the Linear Model with
R
Generalized Linear, Mixed Effects and Nonparametric Regression
Models

Julian J.Faraway


<figure>

CH
Chapman & Hall/CRC
Taylor & Francis Group

</figure>


Boca Raton London New York

<!-- PageBreak -->

Published in 2006 by Chapman & Hall/CRC Taylor & Francis Group 6000 Broken Sound
Parkway NW, Suite 300 Boca Raton, FL 33487-2742

C 2006 by Taylor & Francis Group, LLC

Chapman & Hall/CRC is an imprint of Taylor & Francis Group
This edition published in the Taylor & Francis e-Library, 2006.
" To purchase your own copy of this or any of Taylor & Francis or Routledge's collection of
thousands of eBooks please go to http://www.ebookstore.tandf.co.uk/."

No claim to original U.S. Government works

ISBN 0-203-49228-5 Master e-book ISBN

ISBN 0-203-62105-0 (Adobe e-Reader Format)
International Standard Book Number-10:1-58488-424-X (Print Edition) (Hardcover)
International Standard Book Number-13:978-1-58488-424-8 (Print Edition) (Hardcover)

Library of Congress Card Number 2005054822

This book contains information obtained from authentic and highly regarded sources. Reprinted
material is quoted with permission, and sources are indicated. A wide variety of references are
listed. Reasonable efforts have been made to publish reliable data and information, but the author
and the publisher cannot assume responsibility for the validity of all materials or for the
consequences of their use.

No part of this book may be reprinted, reproduced, transmitted, or utilized in any form by any
electronic, mechanical, or other means, now known or hereafter invented, including photocopying,
microfilming, and recording, or in any information storage or retrieval system, without written
permission from the publishers.

For permission to photocopy or use material electronically from this work, please access
http://www.copyright.com/ (http://www.copyright.com/) or contact the Copyright Clearance
Center, Inc. (CCC) 222 Rosewood Drive, Danvers, MA 01923, 978-750-8400. CCC is a not-for-
profit organization that provides licenses and registration for a variety of users. For organizations
that have been granted a photocopy license by the CCC, a separate system of payment has been
arranged.

Trademark Notice: Product or corporate names may be trademarks or registered trademarks, and
are used only for identification and explanation without intent to infringe.


## Library of Congress Cataloging-in-Publication Data

Faraway, Julian James. Extending the linear model with R: generalized linear, mixed effects and
nonparametric regression models/Julian J.Faraway. p. cm .- (Texts in statistical science) Includes
bibliographical references and index. ISBN 1-58488-424-X 1. Analysis of variance. 2. Regression
analysis. 3. R (Computer program languages)-Mathematical models. I. Title. II. Series.
QA279.F368 2006 519.5-dc22 2005054822


<figure>

informa
Taylor & Francis Group
is the Academic Division of Informa ple.

</figure>


<!-- PageBreak -->

Visit the Taylor & Francis Web site at http://www.taylorandfrancis.com and the CRC Press
Web site at http://www.crcpress.com

<!-- PageBreak -->


## Preface

Linear models are central to the practice of statistics. They are part of the core knowledge
expected of any applied statistician. Linear models are the foundation of a broad range of
statistical methodologies; this book is a survey of techniques that grow from a linear
model. Our starting point is the regression model with response $y$ and predictors $x _ { 1 } , \ldots x _ { p }$
The model takes the form:

$$y = \beta _ { 0 } + \beta _ { 1 x 1 } + \ldots + \beta _ { P } x _ { p } + c$$

where $\&$ is normally distributed. This book presents three extensions to this framework.
The first generalizes the $y$ part; the second, the & part; and the third, the $x$ part of the linear
model.

Generalized Linear Models: The standard linear model cannot handle nonnormal
responses, $\mathcal{Y} ,$ such as counts or proportions. This motivates the development of
generalized linear models that can represent categorical, binary and other response types.

Mixed Effect Models: Some data has a grouped, nested or hierarchical structure.
Repeated measures, longitudinal and multilevel data consist of several observations taken
on the same individual or group. This induces a correlation structure in the error, E.
Mixed effect models allow the modeling of such data.

Nonparametric Regression Models: In the linear model, the predictors, x, are
combined in a linear way to model the effect on the response. Sometimes this linearity is
insufficient to capture the structure of the data and more flexibility is required. Methods
such as additive models, trees and neural networks allow a more flexible regression
modeling of the response that combine the predictors in a nonparametric manner.

This book aims to provide the reader with a well-stocked toolbox of statistical
methodologies. A practicing statistician needs to be aware of and familiar with the basic
use of a broad range of ideas and techniques. This book will be a success if the reader is
able to recognize and get started on a wide range of problems. However, the breadth
comes at the expense of some depth. Fortunately, there are book-length treatments of
topics discussed in every chapter of this book, so the reader will know where to go next if
needed.

$R$ is a free software environment for statistical computing and graphics. It runs on a
wide variety of platforms including the Windows, Linux and Macintosh operating
systems. Although there are several excellent statistical packages, only $\mathrm { R }$ is both free and
possesses the power to perform the analyses demonstrated in this book. While it is
possible in principle to learn statistical methods from purely theoretical expositions, I
believe most readers learn best from the demonstrated interplay of theory and practice.
The data analysis of real examples is woven into this book and all the $\mathrm { R }$ commands
necessary to reproduce the analyses are provided.

Prerequisites: Readers should possess some knowledge of linear models. The first
chapter provides a review of these models. This book can be viewed as a sequel to Linear

<!-- PageBreak -->

Models with $R ,$ Faraway (2004). Even so there are plenty of other good books on linear
models such as Draper and Smith (1998) or Weisberg (2005), that would provide ample
grounding. Some knowledge of likelihood theory is also very useful. An outline is
provided in Appendix $\mathrm { A } ,$ but this may be insufficient for those who have never seen it
before. A general knowledge of statistical theory is also expected concerning such topics
as hypothesis tests or confidence intervals. Even so, the emphasis in this text is on
application, so readers without much statistical theory can still learn something here.

This is not a book about learning R, but the reader will inevitably pick up the language
by reading through the example data analyses. Readers completely new to R will benefit
from studying an introductory book such as Dalgaard (2002) or one of the many tutorials
available for free at the $\mathrm { R }$ website. Even so, the book should be intelligible to a reader
without prior knowledge of R just by reading the text and output. R skills can be further
developed by modifying the examples in this book, trying the exercises and studying the
help pages for each command as needed. There is a large amount of detailed $\mathrm { h e l p }$ on the
commands available within the software and there is no point in duplicating that here.
Please refer to Appendix B for details on obtaining and installing $R$ along with the
necessary add-on packages and data necessary for running the examples in this text. S-
plus derives from the same $\mathrm { S }$ language as $\mathrm { R } ,$ so many of the commands in this book will
work. However, there are some differences in the syntax and the availability of add-on
packages, so not everything here will work in S-plus.

The website for this book is at www.stat.Isa.umich.edu/~faraway/ELM where data
described in this book appears. Updates and errata will also appear there.

Thanks to the builders of $\mathrm { R }$ without whom this book would not have been possible.

<!-- PageBreak -->


## Contents


<table>
<tr>
<th colspan="2">Preface</th>
<th>ix</th>
</tr>
<tr>
<td>1</td>
<td>Introduction</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>Binomial Data</td>
<td>28</td>
</tr>
<tr>
<td>3</td>
<td>Count Regression</td>
<td>61</td>
</tr>
<tr>
<td>4</td>
<td>Contingency Tables</td>
<td>76</td>
</tr>
<tr>
<td>5</td>
<td>Multinomial Data</td>
<td>106</td>
</tr>
<tr>
<td>6</td>
<td>Generalized Linear Models</td>
<td>126</td>
</tr>
<tr>
<td>7</td>
<td>Other GLMs</td>
<td>149</td>
</tr>
<tr>
<td>8</td>
<td>Random Effects</td>
<td>169</td>
</tr>
<tr>
<td>9</td>
<td>Repeated Measures and Longitudinal Data</td>
<td>203</td>
</tr>
<tr>
<td>10</td>
<td>Mixed Effect Models for Nonnormal Responses</td>
<td>221</td>
</tr>
<tr>
<td>11</td>
<td>Nonparametric Regression</td>
<td>232</td>
</tr>
<tr>
<td>12</td>
<td>Additive Models</td>
<td>254</td>
</tr>
<tr>
<td colspan="2">13 Trees</td>
<td>278</td>
</tr>
<tr>
<td colspan="2">14 Neural Networks</td>
<td>296</td>
</tr>
<tr>
<td colspan="2">A Likelihood Theory</td>
<td>307</td>
</tr>
<tr>
<td colspan="2">B $R$ Information</td>
<td>316</td>
</tr>
<tr>
<td></td>
<td>Bibliography</td>
<td>318</td>
</tr>
<tr>
<td></td>
<td>Index</td>
<td>324</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageBreak -->


## CHAPTER 1 Introduction

This book is about extending the linear model methodology using $\mathrm { R }$ statistical software.
Before setting off on this journey, it is worth reviewing both linear models and $\mathrm { R } .$ We
shall not attempt a detailed description of linear models; the reader is advised to consult
texts such as Faraway (2004), Draper and Smith (1998) or Weisberg (2005). However,
we will review the main points. Also, we do not intend this as a self-contained
introduction to $\mathrm { R }$ as this may be found in books such as Dalgaard (2002) or Maindonald
and Braun (2003) or from guides obtainable from the R website. Even so, a reader
unfamiliar with $R$ should be able to follow the analysis to follow and learn a little R in the
process without further preparation.

Let's consider an example. The 2000 United States Presidential election generated
much controversy, particularly in the state of Florida where there were some difficulties
with the voting machinery. In Meyer (2002), data on voting in the state of Georgia is
presented and analyzed. Let's take a look at this data using $R .$ Please refer to Appendix B
for details on obtaining and installing $R$ along with the necessary addon packages and
data for running the examples in this text. R commands are typed at the command
prompt: >. We start by loading the package of datasets that are used in this book:

$$> \mathrm { l i b r a r y } \left( \mathrm { f a r a w a y } \right)$$

Please remember that every time you want to access a dataset specific to this book, you
will need to type the library (faraway) command. Since you might start a new session at
any point in this book, in future we will simply assume that you type this first. If you
forget, you will receive an error message notifying you that the data could not be found.

Next we load the dataset with the Georgia voting information:

$$\mathrm { d a t a } \left( \mathrm { g a v o t e } \right)$$
\>

The data command loads the particular dataset into R. In $\mathrm { R } ,$ the object containing the data
is called a dataframe. In most installations of $\mathrm { R } ,$ this data step will be unnecessary as the
datasets will be silently accessed using a process called lazy loading. However, we will
retain this command throughout this book as a marker to indicate that we intend to use a
particular dataset in $\mathrm { R } .$ Rather than typing the command, you might regard it as a
reminder to consult the help page for the dataset. We can obtain definitions of the
variables and more information about the dataset using the help command:

$$> \mathrm { h e l p } \left( \mathrm { g a v o t e } \right)$$

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 2

You can use the help command to learn more about any of the commands we use. For
example, to learn about the quantile command:

$$> \mathrm { h e l p } \left( \mathrm { q u a n t i l e } \right)$$

If you do not already know or guess the name of the command you need, use:

$$> \mathrm { h e l p . s e a r c h } \left( ^ { \prime \prime } \mathrm { q u a n t i l e s } ^ { \prime \prime } \right)$$

to learn about all commands that refer to quantiles. More generally, use:

\> help.start ()

to browse through the documentation.

We can examine the contents of the dataframe simply by typing its name:

\> gavote


<table>
<tr>
<th></th>
<th>equip</th>
<th>econ</th>
<th>perAA</th>
<th>rural</th>
<th>atlanta</th>
<th>gore</th>
<th>bush</th>
</tr>
<tr>
<td>APPLING</td>
<td>LEVER</td>
<td>poor</td>
<td>0.182</td>
<td>rural</td>
<td>notAtlanta</td>
<td>2093</td>
<td>3940</td>
</tr>
<tr>
<td>ATKINSON</td>
<td>LEVER</td>
<td>poor</td>
<td>0.230</td>
<td>rural</td>
<td>notAtlanta</td>
<td>821</td>
<td>1228</td>
</tr>
</table>


. ...

We have deleted most of the output although this dataset is small enough to be
comfortably examined in its entirety. Sometimes, we simply want to look at the first few
cases. The head command is useful for this:

\> head (gavote)


<table>
<tr>
<th colspan="3">equip</th>
<th>econ</th>
<th>perAA</th>
<th>rural</th>
<th>atlanta</th>
<th>gore</th>
<th>bush</th>
</tr>
<tr>
<td colspan="2">other</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>APPLING</td>
<td></td>
<td>LEVER</td>
<td>poor</td>
<td>0.182</td>
<td>rural</td>
<td>notAtlanta</td>
<td colspan="2">2093</td>
</tr>
<tr>
<td>3940</td>
<td colspan="2">66</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td colspan="2">ATKINSON</td>
<td>LEVER</td>
<td>poor</td>
<td>0.230</td>
<td>rural</td>
<td>notAtlanta</td>
<td colspan="2">821</td>
</tr>
<tr>
<td>1228</td>
<td colspan="2">22</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td colspan="2">BACON</td>
<td>LEVER</td>
<td>poor</td>
<td>0.131</td>
<td>rural</td>
<td>notAtlanta</td>
<td colspan="2">956</td>
</tr>
<tr>
<td>2010</td>
<td colspan="2">29</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td colspan="2">BAKER</td>
<td>os-CC</td>
<td>poor</td>
<td>0.476</td>
<td>rural</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td colspan="3">notAtlanta 893</td>
<td>615</td>
<td>11</td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td colspan="2">BALDWIN</td>
<td>LEVER</td>
<td>middle</td>
<td>0.359</td>
<td>rural</td>
<td>notAtlanta</td>
<td colspan="2">5893</td>
</tr>
<tr>
<td>6041</td>
<td colspan="2">192</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>BANKS</td>
<td></td>
<td>LEVER</td>
<td>middle</td>
<td>0.024</td>
<td>rural</td>
<td>notAtlanta</td>
<td colspan="2">1220</td>
</tr>
<tr>
<td colspan="2">3202 111</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</table>


<table>
<tr>
<th></th>
<th>votes</th>
<th>ballots</th>
</tr>
<tr>
<td>APPLING</td>
<td>6099</td>
<td>6617</td>
</tr>
<tr>
<td>ATKINSON</td>
<td>2071</td>
<td>2149</td>
</tr>
<tr>
<td>BACON</td>
<td>2995</td>
<td>3347</td>
</tr>
<tr>
<td>BAKER</td>
<td>1519</td>
<td>1607</td>
</tr>
<tr>
<td>BALDWIN</td>
<td>12126</td>
<td>12785</td>
</tr>
<tr>
<td>BANKS</td>
<td>4533</td>
<td>4773</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Introduction 3" -->

The cases in this dataset are the counties of Georgia and the variables are (in order) the
type of voting equipment used, the economic level of the county, the percentage of
African Americans, whether the county is rural or urban, whether the county is part of the
Atlanta metropolitan area, the number of voters for $A l$ Gore, the number of voters for
George Bush, the number of voters for other candidates, the number of votes cast, and
ballots issued.

A potential voter goes to the polling station where it is determined whether he or she is
registered to vote. If so, a ballot is issued. However, a vote is not recorded if the person
fails to vote for President, votes for more than one candidate or the equipment fails to
record the vote. For example, we can see that in Appling county, 6617-6099=518 ballots
did not result in votes for President. This is called the undercount. The purpose of our
analysis will be to determine what factors affect the undercount. We will not attempt a
full and conclusive analysis here because our main purpose is to illustrate the use of
linear models and $\mathrm { R } .$ The reader is invited to fill in some of the gaps in the analysis.

Initial data analysis: The first stage in any data analysis should be an initial graphical
and numerical look at the data. A compact numerical overview is:

\> summary (gavote)


<table>
<tr>
<th>equip</th>
<th>econ</th>
<th colspan="2">perAA</th>
<th>rural</th>
</tr>
<tr>
<td>LEVER : 74</td>
<td>middle : 69</td>
<td>Min.</td>
<td>:0.000</td>
<td>rural : 117</td>
</tr>
<tr>
<td>OS-CC: 44</td>
<td>poor : 72</td>
<td colspan="2">1st Qu. : 0.112</td>
<td>urban: 42</td>
</tr>
<tr>
<td>OS-PC: 22</td>
<td>rich : 18</td>
<td colspan="2">Median :0.233</td>
<td></td>
</tr>
<tr>
<td>PAPER: 2</td>
<td></td>
<td colspan="2">Mean :0.243</td>
<td></td>
</tr>
<tr>
<td>PUNCH : 17</td>
<td rowspan="2"></td>
<td colspan="2" rowspan="2">3rd Qu. :0.348 Max. :0.765</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>


atlanta

Atlanta
: 15
notAtlanta: 144


<table>
<tr>
<th colspan="2">gore</th>
<th colspan="2">bush</th>
</tr>
<tr>
<td>Min. :</td>
<td>249</td>
<td colspan="2">Min. : 271</td>
</tr>
<tr>
<td>1st Qu. :</td>
<td>1386</td>
<td>1st Qu. :</td>
<td>1804</td>
</tr>
<tr>
<td>Median</td>
<td>: 2326</td>
<td>Median :</td>
<td>3597</td>
</tr>
<tr>
<td>Mean</td>
<td>: 7020</td>
<td>Mean :</td>
<td>8929</td>
</tr>
<tr>
<td>3rd Qu.</td>
<td>: 4430</td>
<td>3rd Qu. :</td>
<td>7468</td>
</tr>
<tr>
<td>Max.</td>
<td>:154509</td>
<td colspan="2">Max. :140494</td>
</tr>
</table>


other
votes
ballots


<table>
<tr>
<td>Min.</td>
<td>: 5</td>
<td>Min.</td>
<td>: 832</td>
<td>Min. :</td>
<td>881</td>
</tr>
<tr>
<td>1st Qu.</td>
<td>: 30</td>
<td>1st Qu.</td>
<td>: 3506</td>
<td>1st Qu. :</td>
<td>3694</td>
</tr>
<tr>
<td>Median</td>
<td>: 86</td>
<td>Median</td>
<td>: 6299</td>
<td>Median :</td>
<td>6712</td>
</tr>
<tr>
<td>Mean</td>
<td>: 382</td>
<td>Mean</td>
<td>: 16331</td>
<td>Mean :</td>
<td>16927</td>
</tr>
<tr>
<td>3rd Qu.</td>
<td>: 210</td>
<td colspan="2">3rd Qu. : 11846</td>
<td>3rd Qu. :</td>
<td>12251</td>
</tr>
<tr>
<td>Max.</td>
<td>: 7920</td>
<td colspan="2">Max. :263211</td>
<td>Max. :</td>
<td>280975</td>
</tr>
</table>


For the categorical variables, we get a count of the number of each type that occur. We
notice, for example, that only two counties used a paper ballot. This will make it difficult
to estimate the effect of this particular voting method on the undercount. For the
numerical variables, we have six statistics that are sufficient to get a rough idea of the
distributions. In particular, we notice that the number of ballots cast ranges over orders of
magnitudes. This suggests that we should consider the relative, rather than the absolute,
undercount. We create this new relative undercount variable, where we specify the
variables using the dataframe$variable syntax:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 4

\> gavote$undercount <- (gavote$ballots-
gavote$votes) /gavote$ballots
> summary (gavote$undercount)


<table>
<tr>
<th>Min.</th>
<th>1st Qu.</th>
<th>Median</th>
<th>Mean</th>
<th>3rd Qu.</th>
<th>Max.</th>
</tr>
<tr>
<td>0.0000</td>
<td>0.0278</td>
<td>0.0398</td>
<td>0.0438</td>
<td>0.0565</td>
<td>0.1880</td>
</tr>
</table>


We see that the undercount ranges from zero up to as much as 19%. The mean across
counties is 4.38%. Note that this is not the same thing as the overall relative under-count
which is:

\> sum (gavote$ballots-gavote$votes) /sum (gavote$ballots)
[1] 0.03518

Graphical summaries are also valuable in gaining an understanding of the data.
Considering just one variable at a time, histograms are a well-known way of examining
the distribution of a variable:

\>
hist (gavote$undercount, main="Undercount", xlab="Percent
Undercount")

The plot is shown in the left panel of Figure 1.1. A histogram is a fairly crude estimate


<figure>
<figcaption>Figure 1.1 Histogram of the undercount is shown on the left and $a$ density estimate with a data rug is shown on the right.</figcaption>

Undercount

Undercount

20

50

Frequency

15

Density

30

10

10

5

\-

0

0.00 0.05 0.10 0.15 0.20

0.00 0.05 0.10 0.15 0.20
$N = 1 5 9$ Bandwidth = 0.006989

Percent Undercount

</figure>


of the density of the variable that is sensitive to the choice of bins. A kernel density
estimate can be viewed as a smoother version of a histogram that is also a superior
estimate of the density. We have added a "rug" to our display that makes it possible to
discern the individual data points:

\> plot (density (gavote$undercount) , main="Undercount")

<!-- PageBreak -->

<!-- PageHeader="Introduction 5" -->

\> rug (gavote$undercount)

We can see that the distribution is slightly skewed and that there are two outliers in the
right tail of the distribution. Such plots are invaluable in detecting mistakes or unusual
points in the data. Categorical variables can also be graphically displayed. The pie chart
is a popular method. We demonstrate this on the types of voting equipment:

$$> p i e \left( t a b l e \left( g a v o t e e q u i p \right) , c o l = g r a y \left( 0 : 4 / 4 \right) \right)$$

The plot is shown in the first panel of Figure 1.2. We have used shades of gray for the
slices of the pie because this is a monochrome book. If you omit the col argument, you
will see a color plot by default. Of course, a color plot is usually preferable, but bear in
mind that most photocopying machines and many laser printers are black and white only,
so a good greyscale plot is still needed. An alternative plot is a Pareto chart which is
simply a bar plot with categories in descending order of frequency:

$$> \text { barplot \left(sort \left(table \left(gavotefequip\right) } \prime ,$$

decreasing=TRUE) , las=2)

The plot is shown in the second panel of Figure 1.2. The $\mathrm { l a s } = 2$ argument means that the
bar labels are printed vertically as opposed to horizontally, ensuring that there is enough
room for them to be seen. The Pareto chart (or just a bar plot) is superior to the pie chart
because the size of the categories are easier to comprehend in the former plot.

Two dimensional plots are also very helpful. A scatterplot is the obvious way to depict
two quantitative variables. Let's see how the proportion voting for Gore relates to the
proportion of African Americans:

\> gavote$pergore <- gavote$gore/gavote$votes
> plot (pergore ~ perAA, gavote, xlab="Proportion
African American",

ylab="Proportion for Gore")

The plot, seen in the first panel of Figure 1.3, shows a strong correlation between these
variables. This is an ecological correlation because the data points are aggregated across
counties. The plot, in and of itself, does not prove that individual African Americans
were more likely to vote for Gore, although we know this to be true from other sources.
We could also compute the proportion of voters for Bush, but this is, not surprisingly,
strongly negatively correlated with the proportion of voters for Gore. We do not need
both variables as the one explains the other. We will use the proportion for Gore in the
analysis to follow although one could just as well replace this with the proportion for
Bush. We will not consider the proportion for other voters as this has little effect on our
conclusions. The reader may wish to verify this.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 6" -->


<figure>
<figcaption>Figure 1.2 Pie chart of the voting equipment frequencies is shown on the left and a Pareto chart on the right.</figcaption>

LEVER

70

60

50

40

PUNCH

30

OS-CC

PAPER

20

☐

☐
PUNCH

$O S - P C$

10

0

$\frac { \pi } { 2 }$

OS-CC

$\frac { 8 } { 8 }$

PAPER

</figure>


Side-by-side boxplots are a good way of displaying the relationship between
qualitative and quantitative variables:

\> plot (undercount ~ equip, gavote, xlab=" ", las=3)

The plot, shown in the second panel of Figure 1.3, shows no major differences in
undercount for the different types of equipment. Two outliers are visible for the optical
scan-precinct count (OS-PC) method. Plots of two qualitative variables are generally not
worthwhile unless both variables have more than three or four levels. The xtabs ()
function is useful for compiling cross-tabulations:

\> xtabs (~ atlanta + rural, gavote)
rural


<table>
<tr>
<th>atlanta</th>
<th>rural</th>
<th>urban</th>
</tr>
<tr>
<td>Atlanta</td>
<td>1</td>
<td>14</td>
</tr>
<tr>
<td>notAtlanta</td>
<td>116</td>
<td>28</td>
</tr>
</table>


We see that just one county in the Atlanta area is classified as rural.

Correlations are the standard way of numerically summarizing the relationship

<!-- PageBreak -->

<!-- PageNumber="7" -->
<!-- PageHeader="Introduction" -->


<figure>
<figcaption>Figure 1.3 A scatterplot plot of proportions of Gore voters and African Americans by county is shown on the left. Boxplots showing the distribution of the undercount by voting equipment are shown on the right.</figcaption>

0.8

0

0

Proportion for Gore

00 $0 0$

0.15

0

0.6

80%

undercount

0.10

0

0

0.4

0.05

0.2

000

0

0.00

0.0

0.2

0.4

0.6

LEVER

OS-CC

OS-PC

PAPER

PUNCH

Proportion African American

</figure>


between quantitative variables. However, not all the variables in our dataframe are
quantitative or immediately of interest. First we construct $a$ vector using $c \left( \right)$ of length
three which contains the indices of the variables of interest. We select these columns
from the dataframe and compute the correlation. The syntax for selecting rows and/or
columns is dataframe [rows, columns] where rows and/or columns are vectors of indices.
In this case, we want all the rows, so we omit that part of the construction:

\> nix <- c (3,10,11,12)
> cor (gavote [, $\left. n i x \right]$ )


<table>
<tr>
<th></th>
<th>perAA</th>
<th>ballots</th>
<th>undercount</th>
<th>pergore</th>
</tr>
<tr>
<td>perAA</td>
<td>1.000000</td>
<td>0.027732</td>
<td colspan="2">0.22969 0.921652</td>
</tr>
<tr>
<td>ballots</td>
<td>0.027732</td>
<td>1.000000</td>
<td colspan="2">$- 0 . 1 5 5 1 7$ 0.095617</td>
</tr>
<tr>
<td>undercount</td>
<td></td>
<td>0.229687-0.155172</td>
<td colspan="2">1.00000 0.218765</td>
</tr>
<tr>
<td>pergore</td>
<td>0.921652</td>
<td>0.095617</td>
<td>0.21877</td>
<td>1.000000</td>
</tr>
</table>


We see some mild correlation between some of the variables except for the Gore-
African Americans correlation which we know is large from the previous plot.

Defining a linear model: We shall try to describe this data with a linear model which
takes the form:

$$Y = \beta _ { 0 } + \beta _ { 1 } X _ { 1 } + \beta _ { 2 } X _ { 2 } + \ldots + \beta _ { p - 1 } X _ { p - 1 } + \varepsilon$$

where $\beta _ { i } , i = 0 , 1 , 2 , \ldots , p - 1$ are unknown parameters. $\beta _ { 0 }$ is called the intercept term. The
response is $Y$ and the predictors are $X _ { 1 } , \ldots , X _ { p - 1 } .$ The predictors may be the original
variables in the dataset or transformations or combinations of them. The error &
represents the difference between what is explained by the systematic part of the model

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 8" -->

and what is observed. & may include measurement error although it is often due to the
effect of unincluded or unmeasured variables.

The regression equation is more conveniently written as:
$y = X \beta + c$

where, in terms of $y = \left( y _ { 1 } , \ldots , y _ { n } \right) ^ { T }$ $\mathrm { e } = \left( \varepsilon _ { 1 } , \ldots , \varepsilon _ { \mathrm { n } } \right) ^ { T }$ $\beta = \left( \beta _ { 0 } , \ldots , \beta _ { p - 1 } \right) T$ and:
$$X = \left( \begin{array}{} 1 & x _ { 1 1 } & x _ { 1 2 } & \ldots , y _ { n } ^ { \prime } & x = \left( \varepsilon _ { 1 , n - 1 } \right) ^ { I } , \beta = \left( \beta _ { 0 } \right. \\ 1 & x _ { 1 1 } & x _ { 1 2 } & \ldots & x _ { 1 , p - 1 } \\ 1 & x _ { 2 1 } & x _ { 2 2 } & \ldots & x _ { 2 , p - 1 } \\ \vdots & & & \vdots & \\ 1 & x _ { n 1 } & x _ { n 2 } & \ldots & x _ { n , p - 1 } \end{array} \right) ,$$ ☒

The column of ones incorporates the intercept term. The least squares estimate of $\beta ,$
$\beta _ { \mathrm { m i n i m i z e s } } :$

$$\sum e _ { i } ^ { 2 } = e ^ { T } e = \left( y - X \beta \right) ^ { T } \left( y - X \beta \right)$$

Differentiating with respect to
$$\begin{array}{} { \text { and setting to zero, we find that } \widehat { \beta } _ { \text { satisfies: } } } \\ { X ^ { T } X \beta = X ^ { T } y } \end{array} :$$

These are called the normal equations.

Fitting a linear model: Linear models in $R$ are fit using the 1m command. For
example, suppose we model the undercount as the response and the proportions of Gore
voters and African Americans as predictors:

\> lmod <- 1m(undercount ~ pergore+perAA, gavote)

This corresponds to the linear model formula:

undercount=Bo+Bipergore+B2perAA+&

R uses the Wilkinson-Rogers notation of Wilkinson and Rogers (1973). For a straight-
forward linear model, such as here, we see that it corresponds to just dropping the
parameters from the mathematical form. The intercept is included by default.

We can obtain the least squares estimates of , called the regression coefficients, $\dot { \beta } _ { b y } :$

\> coef(lmod)


<table>
<tr>
<th>(Intercept)</th>
<th>pergore</th>
<th>perAA</th>
</tr>
<tr>
<td>0.032376</td>
<td>0.010979</td>
<td>0.028533</td>
</tr>
</table>


The construction of the least squares estimates do not require any assumptions about &. If
we are prepared to assume that the errors are at least independent and have equal
variance, then the Gauss-Markov theorem tells us that the least squares estimates are the
best linear unbiased estimates. Although it is not necessary, we might further assume that
the errors are normally distributed, we might compute the maximum likelihood estimate

<!-- PageBreak -->

<!-- PageHeader="Introduction 9" -->

(MLE) of ß (see Appendix A for more MLEs). For the linear models, these MLEs are
identical with the least squares estimates. However, we shall find that, in some of the
extension of linear models considered later in this book, an equivalent notion to least
squares is not suitable and that likelihood methods must be used. This issue does not arise
with the standard linear model.

The predicted or fitted values are $\widehat { y } = X \widehat { \beta } _ { \mathrm { w } }$
☒
while the residuals are
$e = y - X \beta = y - y .$
☒
We can compute these as:

\> predict (lmod)
APPLING ATKINSON
BACON
BAKER
BALDWIN
BANKS
0.041337 0.043291 0.039618 0.052412 0.047955 0.036016
. . .
> residuals(lmod)
APPLING
ATKINSON
BACON
BAKER
BALDWIN
0.0369466 -0.0069949 0.0655506 0.0023484 0.0035899
. . .

where the ellipsis indicates that (much of) the output has been omitted.

It is useful to have some notion of how well the model fits the data. The residual sum
of squares (RSS) is $\mathbb{H} ^ { T }$ 8.This can be computed as:

\> deviance(lmod)
[1] 0.09325

The term deviance is a more general measure of fit than RSS, which we will meet again
in chapters to follow. For linear models, the deviance is the RSS.

The degrees of freedom for a linear model is the number of cases minus the number of
coefficients or:

\> df.residual(lmod)
[1] 156
> nrow(gavote) - length(coef(lmod))
[1] 156

Let the variance of the error be $\sigma ^ { 2 } ,$ then $\sigma$ is estimated by the residual standard error
computed from
☒
/(RSS/df)
*For our example, this works out to be:

\> sqrt (deviance (lmod) / df.residual (lmod))
[1] 0.024449

Although several useful regression quantities are stored in the 1m model object (which
we called lmod in this instance), we can compute several more using the summary
command on the model object. For example:

\> lmodsum <- summary(lmod)
> lmodsum$sigma

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 10" -->

[1] 0.024449

R is an object-oriented language. One important feature of such a language is that generic
functions, such as summary, recognize the type of object being passed to it and behave
appropriately. We used summary for dataframes above and now for linear models,
residuals is another generic function and we shall see how it can be applied to many
model types and return appropriately defined residuals.

The deviance measures how well the model fits in an absolute sense, but it does not
tell us how well the model fits in a relative sense. The popular choice is $R ^ { 2 } ,$ called the
coefficient of determination or percentage of variance explained:

$$R ^ { 2 } = 1 - \frac { \sum \left( \ddot { y } _ { i } - y _ { i } \right) ^ { 2 } } { \sum \left( y _ { i } - \bar { y } \right) ^ { 2 } } = 1 - \frac { R S S } { T S S }$$

where $= \sum \left( y _ { i } - y \right) ^ { 2 }$ and stands for total sum of squares. This can be most
conveniently extracted as:

\> lmodsum$r.squared
[1] 0.053089

We see that $R ^ { 2 }$ is only about 5% which indicates that this particular model does not fit so
well. An appreciation of what constitutes a good value of $R ^ { 2 }$ varies according to the
application. Another way to think of $R ^ { 2 }$ is the (squared) correlation between the predicted
values and the response:

$$> c o r \left( p r e d i c t \left( I m o d \right) , g a v o t e u n d e r c o u n t \right) ^ 2$$
[1] 0.053089

$R ^ { 2 }$ suffers as a criterion for choosing models among those available because it can never
decrease when you add a new predictor to the model. This means that it will favor the
largest models. The adjusted $R ^ { 2 }$ makes allowance for the fact a larger model also uses
more parameters. It is defined as:

$$R _ { a } ^ { 2 } = 1 - \frac { R S S / \left( n - p \right) } { T S S / \left( n - 1 \right) }$$

Adding a predictor will only increase
$R _ { a i f } ^ { 2 }$
it has some predictive value. Furthermore,
minimizing $\widehat { \sigma } ^ { 2 } \text { means maximizing } R _ { \mathrm { a o v e r } } ^ { 2 }$ a set of possible linear models. The value can
be extracted as:

\> lmodsum$adj.r.squared
[1] 0.040949

One advantage of $\mathrm { R }$ over many statistical packages is that we can extract all these
quantities individually for subsequent calculations in a convenient way. However, if we
simply want to see the regression output printed in a readable way, we use the summary:

<!-- PageBreak -->

<!-- PageNumber="11" -->
<!-- PageHeader="Introduction" -->

\> summary(lmod)

Residuals:
Min
1Q
Median
3Q
Max
-0.04601 -0.01500 -0.00354 0.01178 0.14244

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>0.0324</td>
<td>0.0128</td>
<td>2.54</td>
<td>0.012</td>
</tr>
<tr>
<td>pergore</td>
<td>0.0110</td>
<td>0.0469</td>
<td>0.23</td>
<td>0.815</td>
</tr>
<tr>
<td>perAA</td>
<td>0.0285</td>
<td>0.0307</td>
<td>0.93</td>
<td>0.355</td>
</tr>
</table>


Residual standard error: 0.0244 on 156 degrees of
freedom
Multiple R-Squared: 0.0531, Adjusted R-squared: 0.0409
F-statistic: 4.37 on 2 and 156 DF, p-value: 0.0142

We have already separately computed many of the quantities given above.

Qualitative predictors: The addition of qualitative variables requires the introduction
of dummy variables. Two-level variables are easy to code; consider the rural/urban
indicator variable. We can code this using a dummy variable $d :$

$$d = \left\{ \begin{array}{} { 0 } & { \text { nural } } \\ { 1 } & { \text { urban } } \end{array} \right.$$ ☒

This is the default coding used in R. Zero is assigned to the level which is first
alphabetically, unless something is done to change this (perhaps using the relevel
command). If we add this variable to our model, it would now be:

$$c o u n t = \beta _ { 0 } + \beta _ { 1 } p e r g o r e + \beta _ { 2 } p e r A A + \beta _ { 3 } d + 8$$

So ß3 would now represent the difference between the undercount in an urban county and
a rural county. Codings other than 0-1 could be used although the interpretation of the
associated parameter would not be quite as straightforward.

A more extensive use of dummy variables is needed for factors with $k > 2$ levels. Let $B$
be an $n \times k$ dummy variable matrix where $B _ { i j } = 1$ if case $\dot { l }$ falls in class $j$ and is zero
otherwise. The coding is determined by a contrast matrix $C$ which has dimension $k \times \left( k - \right.$
1). The contribution of the factor to the model matrix $X$ is then given by $B C .$

Consider the voting equipment, which is a five-level factor. The default choice for $R$ is
treatment coding. The contrast matrix, $C$ that describes this coding, where the columns
represent the dummy variables and the rows represent the levels, is:

\> contr.treatment (5)
2 3 4 5
10000
21000
30100
40010
50001

This treats level one (LEVER in this example) as the standard level to which all other
levels are compared. Each parameter for the dummy variable then represents the

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 12" -->

difference between the given level and the first level. Other codings, which define
different $C$ matrices, are used, such as Helmert or sum contrasts, but the treatment coding
is generally the easiest to interpret.

Interactions between variables can be added to the model by taking the columns of the
model matrix $X$ that correspond to the two variables. Call these submatrices A and $B$
having $r$ and $s$ columns, respectively. We then form a new matrix by multiplying every
column of $A$ elementwise with every column of $B .$ This new matrix will have rs columns
with typical element $a _ { i j } b _ { i k }$ where $\mathrm { i } = 1 , \ldots , n , j = 1 , \ldots , r$ and $k = 1 , \ldots , s .$

Interpretation: Let's add some qualitative variables to the model to see how the
terms can be interpreted. We have centered the pergore and perAA terms by their means
for reasons that will become clear:

\> gavote$cpergore <- gavote$pergore -
mean (gavote$pergore)
> gavote$cperAA <- gavote$perAA - mean (gavote$perAA)

\> Imodi <- Im (undercount ~ cperAA+cpergore*ruralteguip,
gavote)

\> summary(lmodi)

Coefficients:


<table>
<tr>
<th></th>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>Pr ( &gt; | t | )</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>(Intercept)</td>
<td></td>
<td>0.04330</td>
<td></td>
<td>0.00284</td>
<td>15.25</td>
<td>&lt; 2e-</td>
</tr>
<tr>
<td>16</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>cperAA</td>
<td></td>
<td>0.02826</td>
<td></td>
<td>0.03109</td>
<td>0.91</td>
<td>0.364</td>
</tr>
<tr>
<td>8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>cpergore</td>
<td></td>
<td>0.00824</td>
<td></td>
<td>0.05116</td>
<td>0.16</td>
<td>0.872</td>
</tr>
<tr>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ruralurban</td>
<td></td>
<td>-0.01864</td>
<td></td>
<td>0.00465</td>
<td>-4.01</td>
<td></td>
</tr>
<tr>
<td>0.000096</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$e q u i p o s -$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>0.00648</td>
<td>0.00468</td>
<td></td>
<td>1.39</td>
<td>0.1681</td>
<td></td>
</tr>
<tr>
<td>$\mathrm { e g u i p o s }$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>0.01564</td>
<td colspan="2">0.00583</td>
<td>2.68</td>
<td>0.0081</td>
<td></td>
</tr>
<tr>
<td>eguipPAPER</td>
<td></td>
<td>-0.00909</td>
<td></td>
<td>0.01693</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.54 0.5920</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>eguipPUNCH</td>
<td></td>
<td>0.01415</td>
<td></td>
<td>0.00678</td>
<td>2.09</td>
<td>0.038</td>
</tr>
<tr>
<td>7</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">cpergore: ruralurban 0.23 0.8205</td>
<td>-0.00880</td>
<td></td>
<td>0.03872</td>
<td>-</td>
<td></td>
</tr>
</table>


Residual standard error: 0.0233 on 150 degrees of
freedom
Multiple R-Squared: 0.17, Adjusted R-squared: 0.125
F-statistic: 3.83 on 8 and 150 DF, p-value: 0.0004

Consider a rural county which has an average proportion of Gore voters and an average
proportion of African Americans where lever machines are used for voting. Because rural
and lever are the reference levels for the two qualitative variables, there is no contribution
to the predicted undercount from these terms. Furthermore, because we have centered the
two quantitative variables at their mean values, these terms also do not enter into the
prediction. Notice the worth of the centering because otherwise we would need to set

<!-- PageBreak -->

<!-- PageNumber="13" -->
<!-- PageHeader="Introduction" -->

these variables to zero to get them to drop out of the prediction equation; zero is not a
typical value for these predictors. Given that all the other terms are dropped, the predicted
undercount is just given by the intercept, which is 4.33%.

The interpretation of the coefficients can now be made relative to this baseline. We see
that, with all other predictors unchanged, except using optical scan with precinct count
(OS-PC), the predicted undercount increases by 1.56%. The other equipment methods
can be similarly interpreted. Notice that we need to be cautious about the interpretation.
Given two counties with the same values of the predictors, except having different voting
equipment, we would predict the undercount to be 1.56% higher for the OS-PC county
compared to the lever county. However, we would not go so far as to say that if we went
to a county with lever equipment and changed it to OS-PC that this would cause the
undercount to increase by 1.56%.

With all other predictors held constant, we would predict the undercount to increase
by 2.83% going from a county with no African Americans to all African American.
Sometimes a one-unit change in a predictor is too large or too small, prompting a
rescaling of the interpretation. For example, we might predict a 0.283% increase in the
undercount for a 10% increase in the proportion of African Americans. Of course, this
interpretation should not be taken too literally. We already know that the proportion of
African Americans and Gore voters is strongly correlated so that an increase in the
proportion of one would lead to an increase in the proportion of the other. This is the
problem of collinearity which makes interpretation of regression coefficients more
difficult. Furthermore, the proportion of African Americans is likely to be associated with
other socioeconomic variables which might also be related to the undercount. This further
hinders the possibility of a causal conclusion.

The interpretation of the rural and per go re cannot be done separately as there is an
interaction term between these two variables. We see that for an average number of Gore
voters, we would predict a 1.86%-lower undercount in an urban county compared to a
rural county. In a rural county, we predict a 0.08% increase in the undercount as the
proportion of Gore voters increases by 10%. In an urban county, we predict a (0.00824-
$\left. 0 . 0 0 8 8 0 \right) ^ { * } 1 0 = - 0 . 0 0 5 6 \%$ increase in the undercount as the proportion of Gore voters
increases by 10%. Since the increase is by a negative amount, this is actually a decrease.
This illustrates the potential pitfalls in interpreting the effect of a predictor in the presence
of an interaction. We cannot give a simple stand-alone interpretation of the effect of the
proportion of Gore voters. The effect is to increase the undercount in rural counties and to
decrease it, if only very slightly, in urban counties.

Hypothesis testing: We often wish to determine the significance of one, some or all
of the predictors in a model. If we assume that the errors are independent and identically
normally distributed, there is a very general testing procedure that may be used. Suppose
we compare two models, a larger model $\Omega$ and a smaller model $@$ contained within that
can be represented as a linear restriction on the parameters of the larger model. Most
often, the predictors in @ are just a subset of the predictors in $\Omega .$

Now suppose that the dimension (or number of parameters) of $\Omega$ is $p$ and the
dimension of $\mathrm { c o }$ is $q ,$ then, assuming that the smaller model $\mathrm { G }$ is correct, the F-statistic is

$$F = \frac { \left( R S S _ { 0 } - R S S _ { \Omega } \right) / \left( p - q \right) } { R S S _ { \Omega } / \left( n - p \right) } \sim F _ { P ^ { - q , R - p } }$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 14" -->

Thus we would reject the null hypothesis that the smaller model is correct if $F >$
$F _ { P - q , n - p } ^ { \left( q \right) }$

For example, we might compare the two linear models we have fit so far. The smaller
model has just pergore and perAA while the larger model adds rural and equip along with
an interaction. We may compute the F-test as:

\> anova(lmod,lmodi)
Analysis of Variance $T a b l e$
Model 1: undercount ~ pergore + perAA
Model 2: undercount ~ cperAA + cpergore * rural + equip
Res. Df RSS Df Sum of Sg F Pr (>F)
1 156 0.0932
2 150 0.0818
6
0.0115 3.51 0.0028

It does not matter that the variables have been centered in the larger model but not in the
smaller model, because the centering makes no difference to the RSS. The p-value here is
small indicating the null hypothesis of preferring the smaller model should be rejected.

One common F-test is the comparison of the current model to the null model, which is
the model with no predictors and just an intercept term. This corresponds to the question
of whether any of the variables have predictive value. For the larger model above, we can
see that this F-statistic is 3.83 on 8 and 150 degrees of freedom with a p-value of 0.0004.
We can see clearly that at least some of the predictors have some significance.

Another common need is to test specific predictors in the model. It is possible to use
the general F-testing method: fit a model with the predictor and without the predictor and
compute the F-statistic. It is important to know what other predictors are also included in
the models and the results may differ if these are also changed. An alternative approach is
to use a t-statistic for testing the hypothesis:

$$t _ { i } = \ddot { \beta } _ { i } / s e \left( \ddot { \beta } _ { i } \right)$$

and check for significance using a t-distribution with $n - p$ degrees of freedom. This
approach will produce exactly the same p-value as the F-testing method. For example, in
the larger model above, the test for the significance of the proportion of African
Americans gives a p-value of 0.3648. This indicates that this predictor is not statistically
significant after adjusting for the effect of the other predictors on the response.

We would usually avoid using the t-tests for the levels of qualitative predictors with
more than two levels. For example, if we were interested in testing the effects of the
various voting equipment, we would need to fit a model without this predictor and
compute the corresponding F-test. A comparison of all models with one predictor less
than the larger model may be obtained conveniently as:

\> dropl (lmodi, $\left. \mathrm { t e s t } = { } ^ { \mathrm { \prime \prime } } \mathrm { F } ^ { \mathrm { \prime \prime } } \right)$
Single term deletions
Model :

undercount ~ cperAA + cpergore * rural + equip
Df Sum of Sq RSS AIC F value Pr
(F)
<none>
0.081775 -1186

<!-- PageBreak -->

<!-- PageNumber="15" -->
<!-- PageHeader="Introduction" -->


<table>
<tr>
<td>cperAA</td>
<td></td>
<td>1 0.000451</td>
<td>0.082226 -</td>
</tr>
<tr>
<td>1187</td>
<td>0.83</td>
<td colspan="2">0.365</td>
</tr>
<tr>
<td>equip</td>
<td></td>
<td colspan="2">4 0.005444 0.087219 -</td>
</tr>
<tr>
<td>1184</td>
<td colspan="2">2.50 0.045</td>
<td></td>
</tr>
<tr>
<td colspan="2">cpergore : rural</td>
<td colspan="2">1 0.000028 0.081804 -</td>
</tr>
<tr>
<td>1188</td>
<td colspan="3">0.05 0.821</td>
</tr>
</table>


We see that the equipment is barely statistically significant in that the p-value is just less
than the traditional 5% significance level. You will also notice that only the interaction
term cpergore: rural is considered and not the corresponding main effects terms, cpergore
and rural. This demonstrates respect for the hierarchy principle which demands that all
lower-order terms corresponding to an interaction be retained in the model. In this case,
we see that the interaction is not significant, but a further step would now be necessary to
test the main effects.

There are numerous difficulties with interpreting the results of hypothesis tests and the
reader is advised to avoid taking the results too literally before understanding these
problems.

Confidence intervals for $\beta$ may be constructed using:

$$\dot { \beta } _ { i } = t _ { n - p } ^ { \left( \alpha / 2 \right) } s e \left( \ddot { \beta } _ { i } \right)$$

where $t _ { n - p } ^ { \left( \alpha ; 2 \right) }$ is the upper $\alpha / 2 ^ { t h }$ quantile of a t distribution with n-p degrees of freedom. A
convenient way of computing the 95% confidence intervals in $R$ is:

\> confint(lmodi)


<table>
<tr>
<th></th>
<th>2.5 %</th>
<th>97.5 %</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>0.03768844</td>
<td>0.0489062</td>
</tr>
<tr>
<td>cperAA</td>
<td>-0.03317106</td>
<td>0.0896992</td>
</tr>
<tr>
<td>cpergore</td>
<td>-0.09284293</td>
<td>0.1093166</td>
</tr>
<tr>
<td>ruralurban</td>
<td>-0.02782090</td>
<td>-0.0094523</td>
</tr>
<tr>
<td>equipos-CC</td>
<td>-0.00276464</td>
<td>$0 . 0 1 5 7 2 9 6$</td>
</tr>
<tr>
<td>equipos-PC</td>
<td>0.00412523</td>
<td>0.0271540</td>
</tr>
<tr>
<td>equipPAPER</td>
<td>-0.04253684</td>
<td>0.0243528</td>
</tr>
<tr>
<td>equipPUNCH</td>
<td>0.00074772</td>
<td>$0 . 0 2 7 5 5 1 5$</td>
</tr>
<tr>
<td>cpergore : ruralurban</td>
<td>-0.08529909</td>
<td>$0 . 0 6 7 7 0 0 2$</td>
</tr>
</table>


Confidence intervals have a duality with the corresponding $t$ t-tests in that if the p-value is
greater than 5%, zero will fall in the interval and vice versa. Confidence intervals give a
range of plausible values for the parameter and are more useful for judging the size of the
effect of the predictor than a p-value which merely indicates statistical significance, not
necessarily practical significance. These intervals are individually correct, but there is not
a 95% chance that the true parameter values fall in all the intervals. This problem of
multiple comparisons is particularly acute for the voting equipment, where five levels
leads to 10 possible pairwise comparisons, more than just the four shown here.

Diagnostics: The validity of the inference depends on the assumptions concerning the
linear model. One part of these assumptions is that the systematic form of the model
$E Y = X \beta$ is correct; we have included all the right variables and transformed and combined

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 16" -->

them correctly. Another set of assumptions concerns the random part of the model: &. We
require that the errors have equal variance, be uncorrelated and have a normal
distribution. We are also interested in detecting points, called outliers, that are unusual in
that they do not fit the model that seems adequate for the rest of the data. Ideally, we
would like each case to have an equal contribution to the fitted model; yet sometimes a
few points have a much larger effect than others. Such points are called influential.

Diagnostic methods can be graphical or numerical. We generally prefer graphical
methods because they tend to be more versatile and informative. It is virtually impossible
to verify that a given model is exactly correct. The purpose of the diagnostics is more to
check whether the model is not grossly wrong. Indeed, a successful data analyst should
pay more attention to avoiding big mistakes than optimizing the fit.

A collection of four useful diagnostics can be simply obtained with:

\> plot (lmodi)

as can be seen in Figure 1.4. The plot in the upper-left panel shows the residuals plotted
against the fitted values. The plot can be used to detect lack of fit. If the residuals show
some curvilinear trend, this is a sign that some change to the model is required, often a
transformation of one of the variables. In this instance, there is no sign of such a problem.
The plot is also used to check the constant variance assumption on the errors. In this case,
it seems the variance is roughly constant as the fitted values vary. Assuming symmetry of
the errors, we can effectively double the resolution by plotting the absolute value of the
residuals against the fitted values. As it happens $| \widetilde { E } | _ { \mathrm { t e n d s } }$ to be rather skewed and is better
to use $\sqrt { 8 }$ VE.Such a plot is shown in the lower-left panel, confirming what we have already
☒
observed about the constancy of the variance. Notice that a few larger residuals have
been labeled.

The residuals can be assessed for normality using $a \quad Q Q \quad p l o t .$ This compares the residuals

to "ideal" normal observations. We plot the sorted residuals against
$\Phi ^ { - 1 } \left( \frac { i } { n + 1 } \right) _ { \text { for } i = 1 , \ldots , } ,$
n. This can be seen in the upper-right panel of Figure 1.4. In this plot, the points follow a
linear trend (except for one or two cases), indicating that normality is a reasonable
assumption. If we observe a curve, this indicates skewness, suggesting a possible
transformation of the response, while two tails of points diverging from linearity would
indicate a long-tailed error, suggesting that we should consider robust fitting methods.
Particularly for larger datasets, the normality assumption is not crucial, as the inference
will be approximately correct in spite of the nonnormality. Only a clear deviation from
normality should necessarily spur some action to change the model.

The Cook statistics are a popular influence diagnostic because they reduce the
information to a single value for each case. They are defined as:

$$D _ { i } = \frac { \left( j - j _ { \left( i \right) } \right) ^ { T } \left( j - j _ { \left( i \right) } \right) } { p \delta ^ { 2 } }$$

<!-- PageBreak -->

<!-- PageNumber="17" -->
<!-- PageHeader="Introduction" -->


<figure>
<figcaption>Figure 1.4 Diagnostics obtained from plotting the model object.</figcaption>

0.15

Residuals vs Fitted

Normal $Q - Q \quad p l o t$

DENHILLO

0

EINHEIO

0.10

RANDOLPHO

\+

MANDONO

Residuals

Standardized residuals

0.05

BACONO

BACONO

0

\+

0

0

Q

2

0

0.00

Q

0

0

80

0

00

00

0

-0.05

Q

0

0

0.02

0.03

0.04

0.05

0.06

0.07

1

0

1

2

Fitted values

Theoretical Quantilos

Scale-Location plot

Cook's distance plot

BỆNHLIO

0.25

ViStandardized residuaisl

2.0

RANDOLPHO

20

BACOND

0

Cook's distance

0

15

00

0

0

RANDOLPH

G

0

0

0

0

0

.10

0

0

0

0

0

0

¢

0

MARION

D

$\Phi _ { _ { \Phi } }$

0

0

0.0

OD

0.02 0.03 0.04 0.05 0.06 0.07

0

50

100

Fitted values

150

Obs. number

</figure>


They represent a scaled measure of the change in the fit if the single case is dropped from
the dataset. An index plot of the Cook statistics for the current model is given in the
lower-right panel of Figure 1.4. We can see that there are a couple of cases that stick out
and we should investigate more closely the influence of these points. We can pick out the
top two influential cases with:

\> gavote[cooks.distance(lmodi) > 0.1,]
equip econ perAA rural
atlanta gore bush

other votes
BEN. HILL OS-PC poor 0.282 rural notAtlanta 2234

2381
46 4661

RANDOLPH OS-PC poor 0.527 rural notAtlanta 1381
1174
14 2569


<table>
<tr>
<th></th>
<th>ballots</th>
<th>undercount</th>
<th>pergore</th>
<th>cpergore</th>
<th>cperAA</th>
</tr>
<tr>
<td>BEN. HILL</td>
<td>5741</td>
<td colspan="2">0.18812 0.47930</td>
<td>0.070975</td>
<td>0.039019</td>
</tr>
<tr>
<td>RANDOLPH</td>
<td>3021</td>
<td>0.14962</td>
<td>0.53756</td>
<td>0.129241</td>
<td>0.284019</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 18" -->

Notice how we can select a subset of a dataframe using a logical expression. Here we ask
for all rows in the dataframe that have Cook statistics larger than 0.1. We see that these
are the same two counties that stuck out in the boxplots seen in Figure 1.3.

The fitted values can be written as
$X \stackrel { n } { \beta } = X \left( X ^ { T } X \right) ^ { - 1 } X ^ { T } y = H y$ the hat-
matrix $H = X \left( X ^ { T } X \right) ^ { - 1 } X ^ { T } .$ $h _ { i } = H _ { i i }$ are called leverages and are useful diagnostics. For
example, since var $\widehat { \mathrm { e } } _ { \mathrm { i } } = \mathrm { \sigma } ^ { 2 } \left( 1 - h _ { \mathrm { i } } \right) _ { \mathrm { r } _ { \mathrm { a } } }$ large leverage, $h _ { i } ,$ will tend to make var $\widehat { \mathrm { e } } _ { \mathrm { i s m a l l } } .$
The fit will be "forced" close to $\mathcal{Y} _ { i } .$ It is useful to examine the leverages to determine
which cases have the power to be influential. Points on the boundary of the predictor
space will have the most leverage.

A useful technique for judging whether some cases in a set of positive observations
are unusually extreme is the half-normal plot. Here we plot the sorted values against
$\Phi ^ { - 1 } \left( \frac { n + i } { 2 n + 1 } \right) _ { \text { which } }$
represent the quantiles of the upper half of a standard normal
distribution. We are usually not looking for a straight line relationship since we do not
necessarily expect a positive normal distribution for quantities like the leverages. We are
looking for outliers, which will be apparent as points that diverge substantially from the
rest of the data. Here is the half-normal plot of the leverages:

$$> \mathrm { h a l f n o r m } \left( \mathrm { i n f l u e n c e } \left( \mathrm { I m o d i } \right) \mathrm { S h a t } \right)$$

The plot, seen in the left panel of Figure 1.5, shows two points with much higher leverage
than the rest. These points are:

\> gavote[influence(lmodi)$hat>0.3,]


<table>
<tr>
<th></th>
<th>equip</th>
<th>econ</th>
<th>perAA</th>
<th>rural</th>
<th>atlanta</th>
<th>gore bush</th>
</tr>
<tr>
<td>other</td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>MONTGOMERY</td>
<td>PAPER</td>
<td>poor</td>
<td>0.243</td>
<td colspan="2">rural notAtlanta</td>
<td>1013</td>
</tr>
<tr>
<td>1465 31</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>TALIAFERRO</td>
<td>PAPER</td>
<td>poor</td>
<td>0.596</td>
<td>rural</td>
<td></td>
<td></td>
</tr>
<tr>
<td>notAtlanta</td>
<td>556</td>
<td>271</td>
<td>5</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>votes</td>
<td colspan="4">ballots undercount pergore</td>
<td>cpergore</td>
</tr>
<tr>
<td>MONTGOMERY</td>
<td>2509</td>
<td></td>
<td>2573</td>
<td colspan="2">0.024874 0.40375</td>
<td>-0.0045753</td>
</tr>
<tr>
<td>TALIAFERRO</td>
<td>832</td>
<td></td>
<td>881</td>
<td>0.055619</td>
<td>0.66827</td>
<td>0.2599475</td>
</tr>
</table>


These are the only two counties that use a paper ballot, so they will be the only cases that
determine the coefficient for paper. This is sufficient to give them high leverage as the
remaining predictor values are all unremarkable. Note that these counties were not
identified as influential-having high leverage alone is not necessarily enough to be
influential.

Partial residual plots display $\ddot { \mathrm { E } } + \ddot { \beta } _ { \mathrm { i } } x _ { \mathrm { i } }$ $x _ { i }$ ¡. To see the motivation, look at the
response with the predicted effect of the other $X$ removed:

$$y - \sum _ { j \neq i } x _ { j } \beta _ { j } = \widehat { y } + \widehat { E } - \sum _ { j \neq i } x _ { j } \beta _ { j } = x _ { i } \beta _ { i } +$$

The partial residual plot for cperAA is shown in the right panel of Figure 1.5:

<!-- PageBreak -->

<!-- PageHeader="Introduction" -->
<!-- PageNumber="19" -->

\> termplot(lmodi,partial=TRUE,terms=1)

The line is the least squares fit to the data on this plot as well as having the same


<figure>
<figcaption>Figure 1.5 Half-normal plot of the leverages is shown on the left and $a$ partial residual plot for the proportion of African Americans is shown on the right.</figcaption>

0.0 0.1 0.2 0.3 0.4 0.5

1033

0.10

Sorted Data

Partial for cperAA

0.05

0

0.00

-0.05

0.0 0.5 1.0 1.5 2.0 2.5

-0.2 0.0 0.2 0.

Half-normal quantiles

cperAA

</figure>


slope as the cperAA term in the current model. This plot gives us a snapshot of the
marginal relationship between this predictor and the response. In this case, we see a linear
relationship indicating that it is not worthwhile seeking transformations. Furthermore,
there is no sign that a few points are having undue influence on the relationship.

Robust regression: Least squares works well when there are normal errors, but
performs poorly for long-tailed errors. We have identified a few potential outliers in the
current model. One approach is to simply eliminate the outliers from the dataset and then
proceed with least squares. This approach is satisfactory when we are convinced that the
outliers represent truly incorrect observations, but even then, detecting such cases is not
always easy as multiple outliers can mask each other. However, in other cases, outliers
are real observations. Sometimes, removing these cases simply creates other outliers. A
generally better approach is to use a robust alternative to least squares that downweights
the effect of larger errors. The Huber method is the default choice of the rlm function,
which is part of the MASS package of Venables and Ripley (2002):

\> library (MASS)
> rlmodi <- rlm (undercount ~
cperAA+cpergore*rural+equip, gavote)
> summary (rlmodi)
Coefficients:


<table>
<tr>
<th></th>
<th>Value</th>
<th>Std. Error</th>
<th>t value</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>0.041</td>
<td>0.002</td>
<td>17.866</td>
</tr>
<tr>
<td>cperAA</td>
<td>0.033</td>
<td>0.025</td>
<td>1.290</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 20" -->


<table>
<tr>
<td>cpergore</td>
<td>-0.008</td>
<td>0.042</td>
<td>-0.197</td>
</tr>
<tr>
<td>ruralurban</td>
<td>-0.017</td>
<td>0.004</td>
<td>-4.406</td>
</tr>
<tr>
<td>$e q u i p o s - C C$</td>
<td>0.007</td>
<td>0.004</td>
<td>1.802</td>
</tr>
<tr>
<td>equipos-PC</td>
<td>0.008</td>
<td>0.005</td>
<td>1.695</td>
</tr>
<tr>
<td>equipPAPER</td>
<td>-0.006</td>
<td>0.014</td>
<td>-0.427</td>
</tr>
<tr>
<td>equipPUNCH</td>
<td>0.017</td>
<td>0.006</td>
<td>3.072</td>
</tr>
<tr>
<td>cpergore: ruralurban</td>
<td colspan="2">0.007 0.032</td>
<td>0.230</td>
</tr>
</table>


Residual standard error: 0.0172 on 150 degrees of
freedom

Inferential methods are more difficult to apply when robust estimation methods are used,
hence there is less in this output than for the corresponding 1m output above. The most
interesting change is that the coefficient for OS-PC is now about half the size. Recall that,
using the treatment coding, this represents the difference between OS-PC and the
reference lever method. There is some fluctuation in the other coefficients, but not
enough to change our impression of the important effects. The robust fit here has reduced
the effect of the two outlying counties.

Weighted least squares: The sizes of the counties in this dataset vary greatly with the
number of ballots cast in each county ranging from 881 to 280,975. We might expect the
proportion of undercounted votes to be more variable in smaller counties than larger
ones. Since the responses from the larger counties might be more precise, one might think
they should count for more in the fitting of the model. This effect can be achieved by the
use of weighted least squares where we attempt to minimize $\sum w _ { i } E _ { i } ^ { 2 }$ . The appropriate
choice for the weights $w _ { i }$ is to set them to be inversely proportional to var $y _ { i } .$

Now var $y$ for a binomial proportion is inversely proportional to the group size, in this
case, the number of ballots. This suggests setting the weights proportional to the number
of ballots:

\> wlmodi <- lm(undercount ~
cperAA+cpergore*rural+equip,
gavote, weights=ballots)

This results in a fit that is substantially different from the unweighted fit. It is dominated
by the data from a few large counties.

However, the variation in the response is likely to be caused by more than just
binomial variation due to the number of ballots. There are likely to be other variables that
affect the response $\mathrm { i n } c$ way that is not proportional to ballot size. Consider the relative
size of these effects. Even for the smallest county, assuming an average undercount rate,
the standard deviation using the binomial is:

$$> s q r t \left( 0 . 0 3 5 * \left( 1 - 0 . 0 3 5 \right) / 8 8 1 \right)$$

[1] 0.0061917

which is much smaller than the residual standard error of 0.0233. The effects will be
substantially smaller for other counties. So since the other sources of variation dominate,
we would recommend leaving this particular model unweighted.

<!-- PageBreak -->

<!-- PageHeader="Introduction 21" -->

Transformation: Models can sometimes be improved by transforming the variables.
Ideas for transformations can come from several sources. One method is to search
through a family of possible transformations looking for the best fit. An example of this
approach is the Box-Cox method of selecting a transformation on the response variable.
Alternatively, the diagnostic plots for the current model can suggest transformations that
might improve the fit or ameliorate an apparent violations of the assumptions. In other
situations, transformations may be motivated by theories concerning the relationship
between the variables or to aid the interpretation of the model.

For this dataset, transformation of the response is problematic for both technical and
interpretational reasons. The minimum undercount is exactly zero which precludes
directly applying some popular transformations such as the log or inverse. An arbitrary
fix for this problem is to add a small amount (say 0.005 here) to the response which
would enable the use of all power transformations. The application of the Box-Cox
method, using the boxcox function from the MASS package, suggests a square root
transformation of the response. However, it is difficult to give an interpre-tation to the
regression coefficients with this transformation on the response. Other than no
transformation at all, a logged response does allow a simple interpretation. For an
untransformed response, the coefficients represent addition to the undercount whereas for
a logged response, the coefficients can be interpreted as multiplying the response. So we
see that, although transformations of the response might sometimes improve the fit, they
can lead to difficulties with interpretation and so should be applied with care. Another
point to consider is that if the untransformed response was normally distributed, it will
not be so after transformation. This suggests considering nonnormal, continuous
responses as seen in Section 7.1, for example.

Transformations of the predictors are less problematic. Let's first consider the
proportion of African Americans predictor in the current model. Polynomials provide a
commonly used family of transformations. The use of orthogonal polynomials is
recommended as these a more numerically stable and make it easier to select the correct
degree:

\> plmodi <- 1m (undercount ~
poly (cperAA, 4) +cpergore*rural+equip, gavote)
> summary (plmodi)
Coefficients:


<table>
<tr>
<th></th>
<th colspan="4">Estimate Std. Error t value</th>
</tr>
<tr>
<th>Pr (&gt;|t|)</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th>(Intercept)</th>
<th>0.04346</th>
<th>0.00288</th>
<th>15.12</th>
<th>&lt; 2e-</th>
</tr>
<tr>
<td>16</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>poly (cperAA,</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>4)1 0.05226</td>
<td>0.06939</td>
<td>0.75 0.4526</td>
<td></td>
<td></td>
</tr>
<tr>
<td>poly (cperAA, 4) 2</td>
<td>-0.00299</td>
<td>0.02613</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.11 0.9091</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>poly (cperAA, 4) 3</td>
<td>-0.00536</td>
<td>0.02427</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.22 0.8254</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>poly (cperAA, 4) 4</td>
<td>-0.01651</td>
<td>0.02420</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.68 0.4961</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>cpergore 6</td>
<td>0.01315</td>
<td>0.05693</td>
<td>0.23</td>
<td>0.817</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 22" -->


<table>
<tr>
<th>ruralurban</th>
<th></th>
<th>-0.01913</th>
<th>0.00474</th>
<th>-4.03</th>
<th></th>
</tr>
<tr>
<td>0.000088</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipos-</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>CC</td>
<td>0.00644</td>
<td>0.00472</td>
<td>1.36</td>
<td>0.1746</td>
<td></td>
</tr>
<tr>
<td colspan="2" rowspan="2">equipos- PC 0.01559</td>
<td rowspan="2">0.00588</td>
<td rowspan="2">2.65</td>
<td></td>
<td></td>
</tr>
<tr>
<td>0.0089</td>
<td></td>
</tr>
<tr>
<td>equipPAPER</td>
<td colspan="2">-0.01027</td>
<td>0.01720</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td colspan="2">0.60 0.5514</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipPUNCH</td>
<td></td>
<td>0.01405</td>
<td>0.00687</td>
<td>2.05</td>
<td>0.042</td>
</tr>
<tr>
<td colspan="2">5</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">cpergore : ruralurban -0.01054</td>
<td>0.04136</td>
<td>-</td>
<td></td>
</tr>
</table>


0.25 0.7993

Residual standard error: 0.0235 on 147 degrees of
freedom

Multiple R-Squared: 0.173, Adjusted R-squared: 0.111
F-statistic: 2.79 on 11 and 147 DF, p-value: 0.00254

The hierarchy principle requires that we avoid eliminating lower-order terms of a variable
when high-order terms are still in the model. From the output, we see that the fourth-
order term is not significant and can be eliminated. With standard polynomials, the
elimination of one term would cause a change in the values of the remaining coefficients.
The advantage of the orthogonal polynomials is that the coefficients for the lower-order
terms do not change as we change the maximum degree of the model. Here we see that
all the terms of cperAA are not significant and all can be removed. Some insight into the
relationship may be gained by plotting the fit on top of the partial residuals:

$$> t e r m p l o t \left( p l m o d i , p a r t i a l = T R U E , t e r m s = 1 \right)$$

The plot, seen in the first panel of Figure 1.6, shows that the quartic polynomial is not so
different from a constant fit, explaining the lack of significance.

Polynomial fits become less attractive with higher-order terms. The fit is not local in
the sense that a point in one part of the range of the variable affects the fit across the
whole range. Furthermore, polynomials tend to have rather oscillatory fits and extrapolate
poorly. A more stable fit can be had using splines, which are piecewise polynomials.
Various types of splines are available and they typically have the local fit and stable
extrapolation properties. We demonstrate the use of cubic B-splines here:

\> library (splines)
> blmodi <- lm(undercount ~ cperAA+bs (cpergore,
4) +rural+equip, gavote)

Because the spline fit for cperAA was very similar to orthogonal polynomials, we
consider cpergore here for some variety. Notice that we have eliminated the interaction
with rural for simplicity. The complexity of the B-spline fit may be controlled by
specifying the degrees of freedom. We have used four here. The nature of the fit can be
seen in the second panel of Figure 1.6:

\> termplot (blmodi, partial=TRUE, terms=2)

<!-- PageBreak -->

<!-- PageHeader="Introduction" -->
<!-- PageNumber="23" -->


<figure>
<figcaption>Figure 1.6 Partial fits using orthogonal polynomials for cperAA (shown on the $\left. l e f t \right)$ and cubic B-splines for cpergore (shown on the right).</figcaption>

Partial for poly(cperAA, 4)

0.10

Partial for bs(cpergore, 4)

0.10

0.05

0.05

0.00

0.00

-0.05

-0.05

-0.2

0.0

0.2

0.4

-0.2

0.0 0.1 0.2 0.3

cperAA

cpergore

</figure>


We see that the curved fit is not much different from a constant.

Variable selection: One theoretical view of the problem of variable selection is that
one subset of the available variables represents the correct model for the data and that any
method should be judged by its success in identifying this correct model. While this may
be a tempting world in which to test competing variable selection methods, it seems
unlikely to match with reality. Even if we believe that $a$ correct model even exists, it is
more than likely that we will not have recorded all the relevant variables or not have
chosen the correct transformations or functional form for the model amongst the set we
choose to consider. We might then retreat from the initial goal and hope to identify the
best model from the available set. Even then, we would need to define what is meant by
best.

Linear modeling serves two broad goals. Some build linear models for the purposes of
prediction-they expect to observe new $X$ and wish to predict $y ,$ along with measures of
uncertainty in the prediction. Prediction performance is improved by removing variables
that contribute little or nothing to the model. We can define a criterion for prediction
performance and search for the model that optimizes that criterion. One such criterion is
the adjusted $R ^ { 2 }$ previously mentioned. The regsubsets function in the leaps package
implements this search. For problems involving a moderate number of variables, it is
possible to exhaustively search all possible models for the best. As the number of
variables increases, exhaustive search become prohibitive and various stepwise methods
must be used to search the model space. The implementation also has the disadvantage
that it can only be applied to quantitative predictors.

Another popular criterion is the Akaike Information Criterion or AIC defined as:
$\mathrm { A I C } = - 2$ maximum log likelihood+2p

where $p$ is the number of parameters. This criterion has the advantage of generality and
can be applied far beyond normal linear models. The step command implements a

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 24" -->

stepwise search strategy through the space of possible models. It does allow qualitative
variables and respects the hierarchy principle. We start by defining a rather large model:

$$> b i g l m < - \quad I m \left( u n d e r c o u n t \sim \left( e q u i p + e c o n + r u r a l + a t l a n t a \right) \right.$$
$$\left. \left( \mathrm { e q u i p } + \mathrm { e c o n } + \mathrm { r u r a l } + \mathrm { a t l a n t a } \right) * \left( \mathrm { p e r A A A + p e r g o r e } \right) , \mathrm { g a r o t e } \right)$$
^2+

This model includes up to all two-way interactions between the qualitative variables
along with all two-way interaction between a qualitative and a quantitative variable. $\mathrm { A l l }$
main effects are included. The step command sequentially eliminates terms to minimize
the $\mathrm { A I C } :$

$$> \mathrm { s m a l } \mathrm { l m } < - \mathrm { s t e p } \left( \mathrm { b i g l m } _ { \prime } \mathrm { t r a c e } = \mathrm { F } \right)$$

The resulting model includes interactions between equip and econ, econ and perAA, and
rural and perAA, together with the associated main effects. The $\mathrm { t r a c e } = \mathrm { F }$ arguments blocks
the large amount of intermediate model information that we would otherwise see.

Linear modeling is also used to try to understand the relationship between the
variables-we want to develop an explanation for the data. For this dataset, we are much
more interested in explanation than prediction. However, the two goals are not mutually
exclusive and often the same methods are used for variable selection in both cases. Even
so, when explanation is the goal, it may be unwise to rely on completely automated
variable selection methods. For example, the proportion of voters for Gore was
eliminated from the model by the AIC-based step method and yet we know this variable
to be strongly correlated with the proportion of African Americans which is in the model.
It would be rash to conclude that the latter variable is important and the former is not-
the two are intertwined. Researchers interested in explaining the relationship may prefer a
more manual variable selection approach that takes into account background information
and is geared toward the substantive questions of interest.

The other major class of variable selection methods is based on testing. We can use $F -$
tests to compare larger models with smaller nested models. $A$ stepwise testing approach
can then be applied to select a model. The consensus $v i e w$ among statisticians is that this
is an inferior method to variable selection compared to the criterion-based methods.
Nevertheless, testing-based methods are still useful, particularly when under manual
control. They have the advantage of applicability across a wide class of models where
tests have been developed. They allow the user to respect restrictions of hierarchy and
situations where certain variables must be included for explanatory purposes. Let's
compare the AlC-selected models above to models with one fewer term:

\> dropl (smallm, $\left. \mathrm { t e s t } = { } ^ { \mathrm { \prime \prime } } \mathrm { F } ^ { \mathrm { \prime \prime } } \right)$
Single term deletions
Model:

undercount ~ equip + econ + rural + perAA + equip : econ
\+ equip : perAA +
rural : perAA
Df Sum of Sq
RSS
AIC F value Pr (F)
<none>
0.0536 -1231

<!-- PageBreak -->

<!-- PageHeader="Introduction 25" -->


<table>
<tr>
<td>equip : econ</td>
<td>6</td>
<td>0.0075 0.0612 -1222</td>
<td>3.25 0.0051</td>
</tr>
<tr>
<td>equip : perAA</td>
<td>4</td>
<td>0.0068 0.0605 -1220</td>
<td>4.43 0.0021</td>
</tr>
<tr>
<td>rural : perAA</td>
<td>1</td>
<td>0.0010 0.0546 -1230</td>
<td>2.65 0.1060</td>
</tr>
</table>


We see that the rural: perAA can be dropped. A subsequent test reveals that rural can also
be removed. This gives us a final model of:

\> finalm <- 1m (undercount~equip + econ + perAA +
equip: econ
\+ equip : perAA, gavote)
\> summary (finalm)


<table>
<tr>
<th>Coefficients:</th>
<th colspan="2">(2 not</th>
<th>defined</th>
<th></th>
<th>because of</th>
<th>singularities)</th>
<th></th>
</tr>
<tr>
<th></th>
<th colspan="2"></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>Pr (&gt;|t|)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>(Intercept)</td>
<td></td>
<td></td>
<td>0.04187</td>
<td></td>
<td>0.00503</td>
<td>8.33</td>
<td>6.5e-</td>
</tr>
<tr>
<td>14</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipos-CC</td>
<td></td>
<td></td>
<td>-0.01133</td>
<td></td>
<td>0.00737</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1.54 0.12670</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipos-</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>PC</td>
<td colspan="2">0.00858</td>
<td>0.01118</td>
<td></td>
<td>0.77</td>
<td>0.44429</td>
<td></td>
</tr>
<tr>
<td>equipPAPER</td>
<td></td>
<td></td>
<td>-0.05843</td>
<td></td>
<td>0.03701</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1.58 0.11669</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipPUNCH</td>
<td></td>
<td></td>
<td>-0.01575</td>
<td></td>
<td>0.01875</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.84 0.40218</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>econpoor</td>
<td></td>
<td></td>
<td>0.02027</td>
<td></td>
<td>0.00553</td>
<td>3.67</td>
<td>0.0003</td>
</tr>
<tr>
<td>5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>econrich</td>
<td></td>
<td></td>
<td>-0.01697</td>
<td></td>
<td>0.01239</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1.37 0.17313</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>perAA</td>
<td></td>
<td></td>
<td>-0.04204</td>
<td></td>
<td>0.01659</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>2.53 0.01239</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipos-CC:</td>
<td colspan="2">econpoor</td>
<td>-0.01096</td>
<td></td>
<td>0.00988</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1.11 0.26922</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipos-</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>PC: econpoor</td>
<td>0.04838</td>
<td></td>
<td>0.01380</td>
<td></td>
<td>3.51</td>
<td>0.00061</td>
<td></td>
</tr>
<tr>
<td>equipPAPER :</td>
<td colspan="2">econpoor</td>
<td>NA</td>
<td></td>
<td>NA</td>
<td>NA</td>
<td>N</td>
</tr>
<tr>
<td>A</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipPUNCH :</td>
<td colspan="2">econpoor</td>
<td>-0.00356</td>
<td></td>
<td>0.01243</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.29 0.77492</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipos-</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>CC: econrich</td>
<td>0.00228</td>
<td></td>
<td>0.01538</td>
<td></td>
<td>0.15</td>
<td>0.88246</td>
<td></td>
</tr>
<tr>
<td>equipOS-PC:econrich</td>
<td colspan="2"></td>
<td>-0.01332</td>
<td></td>
<td>0.01705</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.78 0.43615</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipPAPER:</td>
<td>econrich</td>
<td></td>
<td>NA</td>
<td></td>
<td>NA</td>
<td>NA</td>
<td>N</td>
</tr>
<tr>
<td>A</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>equipPUNCH :</td>
<td>econrich</td>
<td></td>
<td>0.02003</td>
<td></td>
<td>0.02200</td>
<td>0.91</td>
<td>0.36405</td>
</tr>
<tr>
<td>equipos-CC :</td>
<td>perAA</td>
<td></td>
<td>0.10725</td>
<td></td>
<td>0.03286</td>
<td>3.26</td>
<td>0.00138</td>
</tr>
<tr>
<td>equipOS-PC:perAA</td>
<td></td>
<td></td>
<td>-0.00591</td>
<td></td>
<td>0.04341</td>
<td>-0.14</td>
<td>0.89198</td>
</tr>
<tr>
<td>equipPAPER :</td>
<td>perAA</td>
<td></td>
<td>0.12914</td>
<td></td>
<td>0.08181</td>
<td>1.58</td>
<td>0.11668</td>
</tr>
<tr>
<td>equipPUNCH :</td>
<td>perAA</td>
<td></td>
<td>0.08685</td>
<td></td>
<td>0.04650</td>
<td>1.87</td>
<td>0.06388</td>
</tr>
</table>


Residual standard error: 0.02 on 141 degrees of freedom
Multiple R-Squared: 0.428, Adjusted R-squared: 0.359
F-statistic: 6.2 on 17 and 141 DF, p-value: 1.32e-10

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 26" -->

Because there are only two paper-using counties, there is insufficient data to estimate the
interaction terms involving paper. This model output is difficult to interpret because of
the interaction terms.

Conclusion: Let's attempt an interpretation of this final model. Certainly we should
explore more models and check more diagnostics, so our conclusions can only be
tentative. The reader is invited to investigate other possibilities.

To interpret interactions, it is often helpful to construct predictions for all the levels of
the variables involved. Here we generate all combinations of equip and econ for a median
proportion of perAA:

\> pdf <- data. frame (econ=rep (levels (gavote$econ) , 5) ,
equip=rep (levels (gavote$equip) , rep (3,5) ),perAA=0.233)

We now compute the predicted undercount for all 15 combinations and display the result
in a table:

\> pp <- predict (finalm, new=pdf)
> xtabs (round (pp, 3) ~ econ + equip, pdf)
equip


<table>
<tr>
<th>econ</th>
<th>LEVER</th>
<th>OS-CC</th>
<th>OS-PC</th>
<th>PAPER</th>
<th>PUNCH</th>
</tr>
<tr>
<td>middle</td>
<td>0.032</td>
<td>0.046</td>
<td>0.039</td>
<td>0.004</td>
<td>0.037</td>
</tr>
<tr>
<td>poor</td>
<td>0.052</td>
<td>0.055</td>
<td>0.108</td>
<td>0.024</td>
<td>0.053</td>
</tr>
<tr>
<td>rich</td>
<td>0.015</td>
<td>0.031</td>
<td>0.009</td>
<td>-0.013</td>
<td>0.040</td>
</tr>
</table>


We can see that the undercount is lower in richer counties and higher in poorer counties.
The amount of difference depends on the voting system. Of the three most commonly
used voting methods, the LEVER method seems best. It is hard to separate the two
optical scan methods, but there is clearly a problem with the precinct count in poorer
counties, which is partly due to the two outliers we observed earlier. We notice one
impossible prediction-a negative undercount in rich paper-using counties, but given the
absence of such data (there were no such counties), we are not too disturbed.

We use the same approach to investigate the relationship between the proportion of
African Americans and the voting equipment. We set the proportion of African
Americans at three levels-the first quartile, the median and the third quartile and then
compute the predicted undercount for all types of voting equipment. We set the econ
variable to middle:

\> pdf <-
data. frame (econ=rep ("middle", 15) , equip=rep (levels (gavot
e$equip) ,
rep (3,5) ) , perAA=rep (c (.11, 0.23,0.35) ,5))
> pp <- predict (finalm, new=pdf)

We create a three-level factor for the three levels of perAA to aid the construction of the
table:

\> propAA <- gl (3,1, 15, labels=c ("low", "medium", "high") )
> xtabs (round (pp, 3) ~ propAA + equip, pdf)

<!-- PageBreak -->

<!-- PageNumber="27" -->
<!-- PageHeader="Introduction" -->

equip


<table>
<tr>
<th>propAA</th>
<th>LEVER</th>
<th>OS-CC</th>
<th>OS-PC</th>
<th>PAPER</th>
<th>PUNCH</th>
</tr>
<tr>
<td>$1 \circ w$</td>
<td>0.037</td>
<td>0.038</td>
<td>0.045</td>
<td>-0.007</td>
<td>0.031</td>
</tr>
<tr>
<td>medium</td>
<td>0.032</td>
<td>0.046</td>
<td>0.039</td>
<td>0.003</td>
<td>0.036</td>
</tr>
<tr>
<td>high</td>
<td>0.027</td>
<td>0.053</td>
<td>0.034</td>
<td>0.014</td>
<td>0.042</td>
</tr>
</table>


We see that the effect of the proportion of African Americans on the undercount is
mixed. High proportions are associated with higher undercounts for OS-CC and PUNCH
and associated with lower undercounts for LEVER and OS-PC.

In summary, we have found that the economic status of a county is the clearest factor
determining the proportion of undercounted votes, with richer counties having lower
undercounts. The type of voting equipment and the proportion of African Americans do
have some impact on the response, but the direction of the effects are not simply stated.
We would like to emphasize again that this dataset deserves further analysis before any
definitive conclusions are drawn.


## Exercises

Since this is a review chapter, it is best to consult the recommended background texts for
specific questions on linear models. However, it is worthwhile gaining some practice
using $\mathrm { R }$ on some real data. Your data analysis should consist of:

· An initial data analysis that explores the numerical and graphical characteristics of the
data.

· Variable selection to choose the best model.

. An exploration of transformations to improve the fit of the model.

· Diagnostics to check the assumptions of your model.

· Some predictions of future observations for interesting values of the predictors.

· An interpretation of the meaning of the model with respect to the particular area of
application.

There is always some freedom in deciding which methods to use, in what order to apply
them, and how to interpret the results. So there may not be one clear right answer and
good analysts may come up with different models.

Here are some datasets which should provide some good practice at building linear
models:

1\. The swiss data-use Fertility as the response.

2\. The rock data-use perm as the response.

3\. The mtcars data-use mpg as the response.

4\. The attitude data-use rating as the response.

5\. The prostate data-use lpsa as the response.

6\. The teengamb data-use gamble as the response.

<!-- PageBreak -->


## CHAPTER 2 Binomial Data


### 2.1 Challenger Disaster Example

In January 1986, the space shuttle Challenger exploded shortly after launch. An
investigation was launched into the cause of the crash and attention focused on the rubber
O-ring seals in the rocket boosters. At lower temperatures, rubber becomes more brittle
and is a less effective sealant. At the time of the launch, the temperature was 31ºF. Could
the failure of the O-rings have been predicted? In the 23 previous shuttle missions for
which data exists, some evidence of damage due to blow by and erosion was recorded on
some O-rings. Each shuttle had two boosters, each with three O-rings. For each mission,
we know the number of O-rings out of six showing some damage and the launch
temperature. This is a simplification of the problem-see Dalal, Fowlkes, and Hoadley
(1989) for more details.

Let's start our analysis with R. For help in obtaining $R$ and installing the necessary
add-on packages and datasets, please see Appendix B. First we load the data. To do this,
you will first need to load the faraway package using the library command as seen in
here. You will need to do this in every session that you run examples from this book. If
you forget, you will receive a warning message about the data not being found. We then
plot the proportion of damaged O-rings against temperature in Figure 2.1:

\> library (faraway)
> data (orings)

\> plot (damage/6 ~ temp, orings, xlim=c (25, 85) , $y l i m =$
$c \left( 0 , 1 \right)$ ,
xlab="Temperature", ylab="Prob of damage")

We are interested in how the probability of failure in a given O-ring is related to the
launch temperature and predicting that probability when the temperature is $3 1 ^ { \circ } F .$ A naive
approach, based on linear models, simply fits a line to this data:

$$> I m o d < - \quad I m \left( d a m a g e / 6 \sim t e m p , o r i n g s \right)$$

\> abline(lmod)

The fit is shown in Figure 2.1. There are several problems with this approach. Most
obviously from the plot, it can predict probabilities greater than one or less than zero.
One might suggest truncating predictions outside the range to zero or one as appropriate,
but it does not seem credible that these probabilities would be exactly zero or one, in this
particular example or many others.

<!-- PageBreak -->

<!-- PageNumber="29" -->
<!-- PageHeader="Binomial data" -->

We might consider the number of damage incidents to be binomially distributed. For a
linear model, we require the errors to be approximately normally distributed for accurate
inference. However, for a binomial with only six trials, the normal approx-


<figure>
<figcaption>Figure 2.1 Damage to O-rings in 23 space shuttle missions as a function of launch temperature. Least squares $f i t$ line is shown.</figcaption>

1.0

0.8

0

Prob of damage

0.6

0.4

0.2

0

0

0

0.0

30

40

50

60

70

80

Temperature

</figure>


imation is too much of a stretch. Furthermore, the variance of a binomial variable is not
constant which violates another crucial assumption of the linear model.

The standard linear model is clearly not directly suitable here. Although, we could use
transformation and weighting to correct some of these problems, it is better to develop a
model that is directly suited for binomial data.


### 2.2 Binomial Regression Model

Suppose the response variable $Y _ { i }$ for $i = 1 , \ldots , n _ { i }$ is binomially distributed $B \left( n _ { i } , p _ { i } \right)$ so that:

$$P \left( Y _ { i } = y _ { i } \right) = \left( \begin{array}{} { n _ { i } } \\ { y _ { i } } \end{array} \right) p _ { i } ^ { y _ { i } } \left( 1 - p _ { i } \right) ^ { n _ { i } - y _ { i } }$$

We further assume that the $Y _ { i }$ are independent. The individual trials that compose the
response $Y _ { i }$ are all subject to the same $q$ predictors $\left( x _ { \mathrm { i l } } , \ldots , x _ { i q } \right) .$ The group of trials is
known as a covariate class. We need a model that describes the relationship of $x _ { 1 } , \ldots , x _ { q }$
to $p .$ Following the linear model approach, we construct a linear predictor:

$\eta _ { i } = \beta _ { 0 } + \beta _ { 1 } x _ { i 1 } + \ldots + \beta _ { q } x _ { i q }$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 30" -->

Since the linear predictor can accommodate quantitative and qualitative predictors with
the use of dummy variables and also allows for transformations and combinations of the
original predictors, it is very flexible and yet retains interpretability. This notion that we
can express the effect of the predictors on the response solely through the linear predictor
is important. The idea can be extended to models for other types of response and is one of
the defining features of the wider class of generalized linear models (GLMs) discussed in
Chapter 6.

We have already seen above that setting $\eta _ { i } = p _ { i }$ is not appropriate because we require
$0 \leq p \leq 1 .$ Instead we shall use a link function $\mathrm { g }$ such that $\eta i = g \left( p _ { i } \right) .$ For this application, we
shall need $g$ to be monotone and be such that $0 \leq g ^ { - 1 } \left( \eta \right) \leq 1$ for any n. There are three
common choices:

1\. Logit: $\eta = \log \left( p / \left( 1 - p \right) \right) .$

2\. Probit: $\eta = \Phi ^ { - 1 } \left( p \right)$ where $\Phi ^ { - 1 }$ is the inverse normal cumulative distribution function.

3\. Complementary $\log - \log : \eta = \log \left( - \log \left( 1 - p \right) \right) .$

The idea of the link function is also one of the central ideas of generalized linear models.
It is used to link the linear predictor to the mean of the response in the wider class of
models.

We will compare these three choices of link function later, but first we estimate the
parameters of the model. We shall use the method of maximum likelihood; see Appendix
$\mathrm { A }$ for a brief introduction to this method. The log-likelihood is given by:

$$I \left( \beta \right) = \sum _ { i = 1 } ^ { n } \left[ y _ { i } \eta _ { i } - n _ { i } \log \left( 1 + e _ { i } ^ { \eta } \right) + \log \left( \begin{array}{} n _ { i } \\ y _ { i } \end{array} \right) \right]$$

We can maximize this to obtain the maximum likelihood estimates $\widehat { \beta } _ { \mathrm { a n d } }$ use the standard
theory to obtain approximate standard errors. An algorithm to perform the maximization
will be discussed in Chapter 6.

We use $R$ to estimate the regression parameters for the Challenger data:

\> logitmod <- glm (cbind (damage, 6-damage) ~ temp,
family=binomial, orings)
> summary (logitmod)
Deviance Residuals:


<table>
<tr>
<th>Min</th>
<th>1Q</th>
<th>Median</th>
<th>3Q</th>
<th>Max</th>
</tr>
<tr>
<td>-0.953</td>
<td>-0.735</td>
<td>-0.439</td>
<td>-0.208</td>
<td>1.957</td>
</tr>
</table>


Coefficients :


<table>
<tr>
<th></th>
<th>Estimate</th>
<th colspan="2">Std. Error z</th>
<th>value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>11.6630</td>
<td colspan="2">3.2963</td>
<td>3.54</td>
<td></td>
</tr>
<tr>
<td>temp</td>
<td>-0.2162</td>
<td>0.0532</td>
<td></td>
<td>-4.07</td>
<td>$4 . 8 e - 0 5$</td>
</tr>
</table>


(Dispersion parameter for binomial family taken to be
1)

Null deviance: 38.898 on 22 degrees of freedom
Residual deviance: 16.912 on 21 degrees of freedom
AIC: 33.67

Number of Fisher Scoring iterations: 6

<!-- PageBreak -->

<!-- PageHeader="Binomial data" -->
<!-- PageNumber="31" -->

For binomial response data, we need two pieces of information about the response
values-y and n. In $\mathrm { R } ,$ one way of doing this is to form a two-column matrix with the first
column representing the number of "successes" $y$ and the second column the number of
"failures" n-y. We have specified that the response is binomially distributed. The default
choice of link is the logit-other choices need to be specifically stated as we shall see
shortly. This default choice is sometimes called logistic regression. The regression
coefficients are given in the output - Bo = 11.6and $\ddot { \beta } _ { 1 } = - 0 . 2 1 6 _ { \mathrm { a l o n g } }$ with the
respective standard errors. The rest of the output will be explained shortly.

We show the logit fit to the data as seen in Figure 2.2:

\> plot (damage/6 ~ temp, orings, xlim=c (25, 85) ,
ylim=c (0,1),
xlab="Temperature", ylab="Prob of damage")
> x <- seq (25, 85,1)

$$> 1 \text { ines } \left( x , \text { ilogit } \left( 1 1 . 6 6 3 0 - 0 . 2 1 6 2 ^ { * } x \right) \right)$$

Notice how the logit fit tends asymptotically toward zero and one at high and low
temperatures, respectively. The fitted values never actually reach zero or one, so the
model never predicts anything to completely certain or completely impossible. Now


<figure>
<figcaption>Figure 2.2 Logit (solid line) and probit (dashed line) fits to the Challenger data</figcaption>

1.0

0.8

0

Prob of damage

0.6

0.4

0.2

8

0

O

0

0.0

COOOO 00 00 00 0

1

30

40

50

60

70

80

Temperature

</figure>


compare this to the probit fit:

\> probitmod <- glm (cbind (damage, 6-damage) ~ temp,
family=binomial (link=probit) , orings)

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 32

\> summary (probitmod)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>5.5915</td>
<td>1.7105</td>
<td>3.27</td>
<td>0.0011</td>
</tr>
<tr>
<td>temp</td>
<td>-0.1058</td>
<td>0.0266</td>
<td>-3.98</td>
<td>6.8e-05</td>
</tr>
</table>


(Dispersion parameter for binomial family taken to be
1)
Null deviance: 38.898 on 22 degrees of freedom
Residual deviance: 18.131 on 21 degrees of freedom
AIC: 34.89

Although the coefficients seem quite different, the fits are similar, particularly in the
range of the data, as seen in Figure 2.2:

$$> 1 \text { ines } \left( x , \text { pnorm } \left( 5 . 5 9 1 5 - 0 . 1 0 5 8 ^ { * } x \right) , 1 t y = 2 \right)$$

We can predict the response at $3 1 ^ { \circ } F$ for both models:

\> ilogit (11.6630-0.2162\*31)
[1] 0.99304
> pnorm (5.5915-0.1058\*31)
[1] 0.9896

We see a very high probability of damage with either model although we still need to
develop some inferential techniques before we leap to conclusions.


### 2.3 Inference

Consider two models, a larger model with $/$ parameters and likelihood $L _ { I }$ and a smaller
model with $s$ parameters and likelihood $L _ { S }$ where the smaller model represents a linear
subspace (a linear restriction on the parameters) of the larger model. Likelihood methods
suggest the likelihood ratio statistic:

$$2 \log \frac { L _ { 4 } } { L _ { 5 } }$$
(2.1)

as an appropriate test statistic for comparing the two models. Now suppose we choose a
saturated larger model-such a model typically has as many parameters as cases and has
fitted values $\widehat { p } _ { i } = y _ { i } / n _ { i }$ a case, the test statistic becomes:

$$D = 2 \sum _ { i = 1 } ^ { n } \left\{ y _ { i } \log y _ { i } / \widehat { y } _ { i } + \left( n _ { i } - y _ { i } \right) \log \left( n _ { i } - y _ { i } \right) / \left( n _ { i } - j _ { i } \right) \right\}$$

where $\widehat { \mathcal{Y} _ { i } }$ are the fitted values from the smaller model. Now since the saturated model fits
as well as any model can fit, the deviance $D$ measures how close the (smaller) model
comes to perfection. Thus deviance is a measure of goodness of $f i t .$ In the output for the

<!-- PageBreak -->

<!-- PageNumber="33" -->
<!-- PageHeader="Binomial data" -->

models above, the Residual deviance is the deviance for the current model while the Null
deviance is the deviance for a model with no predictors and just an intercept term.

Provided that $Y$ is truly binomial and that the $n _ { i }$ are relatively large, the deviance is
approximately $x ^ { 2 }$ distributed with n-l degrees of freedom if the model is correct. Thus we
can use the deviance to test whether the model is an adequate fit. For the logit model of
the Challenger data, we may compute:

\> pchisq (deviance (logitmod) ,
df.residual (logitmod) , lower=FALSE)
[1] 0.71641

Since this p-value is well in excess of 0.05, we may conclude that this model fits
sufficiently well. Of course, this does not mean that this model is correct or that a simpler
model might not also fit adequately. Even so, for the null model:

$$> p c h i s q \left( 3 8 . 9 , 2 2 , l o w e r = F A L S E \right)$$

[1] 0.014489

we see that the fit is inadequate, so we cannot ascribe the response to simple variation not
dependent on any predictor. Note that a $x ^ { 2 }$ Xdvariable has mean d and standard deviation
$\sqrt { 2 d } s o$ that it is often possible to quickly judge whether a deviance is large or small
without explicitly computing the p-value. If the deviance is far in excess of the degrees of
freedom, the null hypothesis can be rejected.

The $x ^ { 2 }$ distribution is only an approximation that becomes more accurate as the $n _ { i }$
increase. For the case, $n _ { i } = 1 ,$ when $y _ { i } = 0$ or 1, in other words, a binary response, the
deviance reduces to:

$$- 2 \sum _ { i = 1 } ^ { n } \left\{ \widehat { p } _ { i } \log i t \left( \widehat { p } _ { i } \right) + \log \left( 1 - \widehat { p } _ { i } \right) \right.$$

For a deviance to measure fit, it has to compare the fitted values $\widehat { p } _ { i }$ the $\mathrm { d a t a } y _ { i } ,$ but here
we have only a function of $\widetilde { P } _ { \mathrm { f } } \cdot \mathrm { T h u s }$ this deviance does not assess goodness of fit and
furthermore, it is not even approximately $x ^ { 2 }$ distributed. Other methods must be used to
judge goodness of fit for binary data-for example, the Hosmer-Lemeshow test described
in Hosmer and Lemeshow (2000).

The approximation is very poor for small $n _ { i } .$ Although it is not possible to say exactly
how large ni should be for an adequate approximation, $n \geq 5$ has often been suggested.
Permutation or bootstrap methods might be considered as an alternative.

We can also use the deviance to compare two nested models. The test statistic in (2.1)

becomes DS-DL. This test statistic is asymptotically distributed $x _ { 1 - s } ^ { 2 }$ 4-s*assuming that the
smaller model is correct and the distributional assumptions hold. We can use this to test
the significance of temperature by computing the difference in the deviances between the
model with and without temperature. The model without temperature is just the null
model and the difference in degrees of freedom or parameters is one:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 34" -->

\>
$$p c h i s q \left( 3 8 . 9 - 1 6 . 9 , 1 , l o w e r = F A L S E \right)$$

[1] 2.7265e-06

Since the p-value is so small, we conclude that the effect of launch temperature is
statistically significant. An alternative to this test is the z-value, which is $\beta / s e \left( \widehat { \beta } \right) \text { , here } -$
4.07 with a p-value of 4.8e-05. In contrast to the normal (Gaussian) linear model, these
two statistics are not identical. In this particular example, there is no practical difference,
but in some cases, especially with sparse data, the standard errors can be overestimated
and so the z-value is too small and the significance of an effect could be missed. This is
known as the Hauck-Donner effect-see Hauck and Donner (1977). So the deviance-
based test is preferred.

Again, there are concerns with the accuracy of the approximation, but the test
involving differences of deviances is generally more accurate than the goodness of fit test
involving a single deviance.

Confidence intervals for the regression parameters may be constructed using normal
approximations for the parameter estimates. A $1 0 0 \left( 1 - \alpha \right) \%$ confidence interval for $\beta _ { i }$
would be:

$$\ddot { \beta } _ { i } \pm z ^ { \alpha / 2 } s e \left( \dot { \beta } _ { i } \right)$$

where $z ^ { \alpha } / ^ { 2 }$ is a quantile from the normal distribution. Thus a 95% confidence interval for
$\beta _ { 1 }$ in our model would be:

$$> c \left( - 0 . 2 1 6 2 - 1 . 9 6 * 0 . 0 5 3 2 , - 0 . 2 1 6 2 + 1 . 9 6 * 0 . 0 5 3 2 \right)$$

[1] -0.32047 -0.11193

It is also possible to construct a profile likelihood-based confidence interval:

\> library (MASS)
> confint (logitmod)


<table>
<tr>
<th colspan="3">Waiting for profiling to be done ...</th>
</tr>
<tr>
<th></th>
<th>2.5 %</th>
<th>97.5 %</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>5.57543</td>
<td>18.73812</td>
</tr>
<tr>
<td>temp</td>
<td>-0.33267</td>
<td>-0.12018</td>
</tr>
</table>


It is important to load the MASS package or the default confint method for ordinary
linear models will be used (which will not be quite right). The profile likelihood method
is generally preferable for the same Hauck-Donner reasons discussed above although it is
more work to compute.

Although we have only computed results for the logit link, the same methods would
apply for the probit or any other link.

<!-- PageBreak -->

<!-- PageNumber="35" -->
<!-- PageHeader="Binomial data" -->


### 2.4 Tolerance Distribution

Suppose that students answers questions on a test and that a specific student has an
aptitude $T .$ A particular question might have difficulty $d _ { i }$ and the student will get the
answer correct only if $T > d _ { i } .$ Now if we consider $d _ { i }$ fixed and $T \sim N \left( \mu , \sigma 2 \right) ,$ then the
probability that a randomly selected student will get the answer wrong is:

$p _ { i } = P \left( T \leq d _ { i } \right) = \Phi \left( \left( d _ { i } - \mu \right) / \sigma \right)$

So

$$\Phi ^ { - 1 } \left( p _ { i } \right) = - \mu / \sigma + d _ { i } / \sigma$$

If we set $\beta _ { 0 } = - \mu / \sigma$ and $\beta _ { 1 } = 1 / \sigma ,$ we now have a probit regression model. So we see that the
probit link can be naturally motivated by the existence of a normally distributed tolerance
distribution $T .$ The term arose from toxicity studies where the aptitude of the subject
would be replaced with the tolerance of the insect.

The logit model arises from a logistically distributed tolerance distribution. The
logistic and normal density are very similar in the mid-range, but differ more in a relative
sense in the tails. The complementary log-log is similarly associated with an extreme
value distribution.


### 2.5 Interpreting Odds

Odds are sometimes a better scale than probability to represent chance. They arose as a
way to express the payoffs for bets. An evens bet means that the winner gets paid an
equal amount to that staked. $A \quad 3 - 1$ against bet would pay $3 for every $1 bet while a 3-1
on bet would pay only $1 for every $3 bet. If these bets are fair in the sense that a bettor
would break even in the long-run average, then we can make a correspondence to
probability. $\mathrm { L e t } p$ be the probability and $o$ be the odds, where we represent 3-1 against as
$1 / 3$ and 3-1 on as 3, then the following relationships hold:

$$\frac { p } { 1 - p } = o \quad p = \frac { o } { 1 + o }$$

One mathematical advantage of odds is that they are unbounded above which makes
them more convenient for some modeling purposes.

Odds also form the basis of a subjective assessment of probability. Some probabilities
are determined from considerations of symmetry or long-term frequencies, but such
information is often unavailable. Individuals may determine their subjective probability
for events by considering what odds they would be prepared to offer on the outcome.
Under this theory, other potential persons would be allowed to place bets for or against
the event occurring. Thus the individual would be forced to make an honest assessment
of probability to avoid financial loss.

If we have two covariates $x _ { 1 }$ and $x _ { 2 } ,$ then the logistic regression model is:

$$\log \left( \mathrm { o d d s } \right) = \log \left( \frac { p } { 1 - p } \right) = \beta _ { 0 } + \beta _ { 1 } x _ { 1 } + \beta _ { 2 } x _ { 2 }$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 36" -->

Now $\beta _ { 1 }$ can be interpreted as follows: a unit increase in $x _ { 1 }$ with $x _ { 2 }$ held fixed increases the
log-odds of success by $\beta _ { 1 }$ or increases the odds of success by a factor of exp $\beta _ { 1 } .$ Of
course, the usual interpretational difficulties regarding causation apply as in standard
regression. No such simple interpretation exists for other links such as the probit.

An alternative notion to odds-ratio is relative risk. Suppose the probability of
"success" in the presence of some condition is $p _ { 1 }$ and $p _ { 2 }$ in its absence. The relative risk is
$P _ { 1 } / P _ { 2 } .$ For rare outcomes, the relative risk and the o dds ratio will be very similar, but for
larger probabilities, there may be substantial differences. There is some debate over
which is the more intuitive way of expressing the effect of some condition.

Consider the data shown in Table 2.1 from a study on infant respiratory disease,
namely the proportions of children developing bronchitis or pneumonia in their first year
of life by type of feeding and sex, which may be found in Payne (1987):


<table>
<caption>Table 2.1 Incidence of respiratory disease in infants to the age of 1 year.</caption>
<tr>
<th></th>
<th>Bottle Only</th>
<th>Some Breast with Supplement</th>
<th>Breast Only</th>
</tr>
<tr>
<td>Boys</td>
<td>$7 7 / 4 5 8$</td>
<td>$1 9 / 1 4 7$</td>
<td>$4 7 / 4 9 4$</td>
</tr>
<tr>
<td>Girls</td>
<td>48/384</td>
<td>$1 6 / 1 2 7$</td>
<td>$3 1 / 4 6 4$</td>
</tr>
</table>


We can recover the layout above with the proportions as follows:

\> data (babyfood)
> xtabs (disease/ (disease+nondisease) ~sex+food,
babyfood)

food

sex
Bottle
Breast
Suppl
Boy 0.16812 0.095142 0.12925
Girl 0.12500 0.066810 0.12598

Fit and examine the model:

\> mdl <- glm (cbind (disease, nondisease) ~ sex+food,
family=binomial,
babyfood)

\> summary (mdl)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate Std.</th>
<th>Error</th>
<th>z value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-1.613</td>
<td>0.112</td>
<td>-14.35</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>sexGirl</td>
<td>-0.313</td>
<td>0.141</td>
<td>-2.22</td>
<td>0.027</td>
</tr>
<tr>
<td>foodBreast</td>
<td>-0.669</td>
<td>0.153</td>
<td>-4.37</td>
<td>1.2e-05</td>
</tr>
<tr>
<td>foodSuppl</td>
<td>-0.173</td>
<td>0.206</td>
<td>-0.84</td>
<td>0.401</td>
</tr>
</table>


(Dispersion parameter for binomial family taken to be
1)


<table>
<tr>
<td>Null deviance:</td>
<td>26.37529</td>
<td>on</td>
<td>5</td>
<td>degrees of freedom</td>
</tr>
<tr>
<td>Residual deviance:</td>
<td>0.72192</td>
<td>on</td>
<td>2</td>
<td>degrees of freedom</td>
</tr>
<tr>
<td>AIC: 40.24</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="37" -->
<!-- PageHeader="Binomial data" -->

The $x ^ { 2 }$ approximation can be expected to be accurate here due to the large covariate class
sizes. Is there a sex-by-food interaction? Notice that a model with the interaction effect
would be saturated with deviance and degrees of freedom zero, so we can look at the
residual deviance of this model to test for an interaction effect. A deviance of 0.72 is not
at all large for two degrees of freedom, so we may conclude that there is no evidence of
an interaction effect. This means that we may interpret the main effects separately.

We can test for the significance of the main effects:

\> dropl (mdl, test="Chi")
Single term deletions
Model:


<table>
<tr>
<th colspan="6">cbind (disease, nondisease) ~ sex + food</th>
</tr>
<tr>
<th colspan="3">Df Deviance</th>
<th>AIC</th>
<th>LRT</th>
<th>Pr (Chi)</th>
</tr>
<tr>
<td colspan="3">&lt;none&gt; 0.7</td>
<td>40.2</td>
<td></td>
<td></td>
</tr>
<tr>
<td>sex</td>
<td>1</td>
<td>5.7</td>
<td>43.2</td>
<td>5.0</td>
<td>0.026</td>
</tr>
<tr>
<td>food</td>
<td colspan="2">2 20.9</td>
<td>56.4</td>
<td>20.2</td>
<td>4.2e-05</td>
</tr>
</table>


The drop1 function tests each predictor relative to the full. We see that both predictors are
significant in this sense. Now consider the interpretation of the coefficients, starting with
the effect of breast feeding:

\> exp (-0.669)
[1] 0.51222

We see that breast feeding reduces the odds of respiratory disease to 51% of that for
bottle feeding. We could compute a confidence interval by figuring the standard error on
the odds scale; however, we get better coverage properties by computing the interval on
the log-odds scale and then transforming the endpoints as follows:

\> exp(c (-0.669-1.96\*0.153, -0.669+1.96\*0.153))
[1] 0.37951 0.69134

Notice that the interval is asymmetric about the estimated effect of 0.512. Confidence
intervals can also be computed using profile likelihood methods:

\> library (MASS)
> exp (confint (mdl) )

Waiting for profiling to be done ...


<table>
<tr>
<th></th>
<th>2.5 %</th>
<th>97.5 %</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>0.15920</td>
<td>0.24743</td>
</tr>
<tr>
<td>sexGirl</td>
<td>0.55362</td>
<td>0.96292</td>
</tr>
<tr>
<td>foodBreast</td>
<td>0.37819</td>
<td>0.68952</td>
</tr>
<tr>
<td>foodSuppl</td>
<td>0.55552</td>
<td>1.24643</td>
</tr>
</table>


which gives a slightly wider interval. This latter result is usually more reliable although it
makes little difference for this data.

As an aside, note that for small values of &, we have:

$\log \left( x \left( 1 + \varepsilon \right) \right) = \log x + \log \left( 1 + \varepsilon \right) \approx \log x + \varepsilon$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 38" -->

This approximation is reasonable for values $- 0 . 2 5 < < 0 . 2 5 .$ So, for example, given the
observed supplement coefficient of-0.173, we can approximate the reduction in odds as
about 17% relative to bottle feeding. The exact figure is:

\> 1exp (-0.173)
[1] 0.15886

that is about 16%. So the approximation is only good for a quick sense of the effect, but
an exact calculation is necessary for results that will be presented to others.

Here we see that breast-fed and to a lesser extent supplement-fed babies are less
vulnerable to respiratory disease. We also see that boys are more vulnerable than girls.
We should be careful about making any general conclusions from this data without
knowing how it was collected. In particular, the decision to breast feed is almost certainly
related to other socioeconomic factors and we would need to investigate whether it is
these rather than the breast feeding that is responsible for the reduction in the incidence
of respiratory disease.


#### 2.6 Prospective and Retrospective Sampling

In prospective sampling, the predictors are fixed and then the outcome is observed. In
other words, in the infant respiratory disease example shown in Table 2.1, we would
select a sample of newborn girls and boys whose parents had chosen a particular method
of feeding and then monitor them for their first year. This is also called a cohort study.

In retrospective sampling, the outcome is fixed and then the predictors are observed.
Typically, we would find infants coming to a doctor with a respiratory disease in the first
year and then record their sex and method of feeding. We would also obtain a sample of
respiratory disease-free infants and record their information. How these samples are
obtained is important-we require that the probability of inclusion in the study is
independent of the predictor values. This is also called a case-control study.

Since the question of interest is how the predictors affect the response, prospective
sampling seems to be required. Let's focus on just boys who are breast or bottle fed. The
data we need is:

\> babyfood [c (1,3) , ]


<table>
<tr>
<th></th>
<th>disease</th>
<th>nondisease</th>
<th>sex</th>
<th>food</th>
</tr>
<tr>
<td>1</td>
<td>77</td>
<td>381</td>
<td>Boy</td>
<td>Bottle</td>
</tr>
<tr>
<td>3</td>
<td>47</td>
<td>447</td>
<td>Boy</td>
<td>Breast</td>
</tr>
</table>


· Given the infant is breast fed, the log-odds of having a respiratory disease are
$\log 4 7 / 4 4 7 = - 2 . 2 5$

· Given the infant is bottle fed, the log-odds of having a respiratory disease are $\log$
$7 7 / 3 8 1 = - \quad 1 . 6 0$

The difference between these two log-odds, $\Delta = - 1 . 6 0 - - 2 . 2 5 = 0 . 6 5 ,$ represents the
increased risk of respiratory disease incurred by bottle feeding relative to breast feeding.
This is the log-odds ratio.

<!-- PageBreak -->

<!-- PageNumber="39" -->
<!-- PageHeader="Binomial data" -->

Now suppose that this had been a retrospective study-we could compute the log-odds
of feeding type given respiratory disease status and then find the difference. Notice that
this would give the same result because:

$$\Delta = \log 7 7 / 4 7 - \log 3 8 1 / 4 4 7 = \log 7 7 / 3 8 1 - \log 4 7 / 4 4 7 = 0 . 6 5$$

This shows that a retrospective design is as effective as a prospective design for
estimating $\Delta .$

Retrospective designs are cheaper, faster and more efficient, so it is convenient that
the same result may be obtained from the prospective study. This manipulation is not
possible for other links. The downside to retrospective studies is that they are typically
less reliable than prospective studies. Retrospective studies rely on historical records
which may be of unknown accuracy and completeness. They may also rely on the
memory of the subject which may be unreliable.

In most practical situations, we will also need to account for the effects of covariates
$X .$ Let $\pi _ { 0 }$ be the probability that an individual is included in the study if they do not have
the disease, while let $\pi _ { 1 }$ be the probability of inclusion if they do have the disease. For a
prospective study, $\pi _ { 0 } = \pi _ { 1 }$ because we have no knowledge of the outcome, while for a
retrospective study typically $\pi _ { 1 }$ is much greater than $\pi _ { 0 } .$ Suppose that for given $x ,$ $p ^ { * } \left( x \right)$ is
the conditional probability that an individual has the disease given that he or she was
included in the study, while $p \left( x \right)$ is the unconditional probability that he or she has the
disease as we would obtain from a prospective study. Now by Bayes theorem:

$$p ^ { * } \left( x \right) = \frac { \pi _ { 1 } p \left( x \right) } { \pi _ { 1 } p \left( x \right) + \pi _ { 0 } \left( 1 - p \left( x \right) \right) }$$

which can be rearranged to show that:

$$\log i t \left( p ^ { * } \left( x \right) \right) = \log \frac { \pi _ { 1 } } { \pi _ { 0 } } + \log i t \left( p \left( x \right) \right)$$

So the only difference between the retrospective and the prospective study would be the
difference in the intercept: $\log \left( \pi _ { 1 } / \pi _ { 0 } \right) .$ Generally $\pi _ { 1 } / \pi _ { 0 }$ would not be known, so we would
not be able to estimate $\beta _ { 0 } ,$ but knowledge of the other $\beta$ would be most important since
this can be used to assess the relative effect of the covariates. We could not, however,
estimate the absolute effect. This does not work for other links such as the probit.


#### 2.7 Choice of Link Function

We must choose a link function to specify a binomial regression model. It is usually not
possible to make this choice based on the data alone. For regions of moderate p, that is
not close to zero or one, the link functions we have proposed are quite similar and so a
very large amount of data would be necessary to distinguish between them. Larger
differences are apparent in the tails, but for very small $p ,$ one needs a very large amount

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 40" -->

of data to obtain just a few successes, making it expensive to distinguish between link
functions in this region. So usually, the choice of link function is made based on
assumptions derived from physical knowledge or simple convenience. We now look at
some of the advantages and disadvantages of the three proposed link functions and what
motivates the choice.

Bliss (1935) analyzed some data on the numbers of insects dying at different levels of
insecticide concentration. We fit all three link functions:

\> $d a t a$ (bliss)
> bliss


<table>
<tr>
<th></th>
<th>dead</th>
<th>alive conc</th>
</tr>
<tr>
<td>1</td>
<td>2</td>
<td>28 0</td>
</tr>
<tr>
<td>2</td>
<td>8</td>
<td>22 1</td>
</tr>
<tr>
<td>3</td>
<td>15</td>
<td>15 2</td>
</tr>
<tr>
<td>4</td>
<td>23</td>
<td>7 3</td>
</tr>
<tr>
<td>5</td>
<td>27</td>
<td>3 4</td>
</tr>
</table>


\> modl <- glm (cbind (dead, alive) ~ conc,
family=binomial, data=bliss)
> modp <- glm (cbind (dead, alive) ~ conc,
family=binomial (link=probit) ,
data=bliss)
> modc <- glm (cbind (dead, alive) ~ conc,
family=binomial (link=cloglog) ,
data=bliss)

We start by considering the fitted values:

\> fitted(modl)
1
3
4
5
0.089172 0.238323 0.500000 0.761677 0.910828
2

or from predict (modl, type="response"). These are constructed using linear predictor, n:

\> coef (modl) [1]+coef (modl) [2]*bliss$conc
[1] -2.3238 -1.1619 0.0000 1.1619 2.3238

Alternatively, these values may be obtained from modl$linear.predictors or predict
(modl). The fitted values are then:


<table>
<tr>
<th colspan="2">&gt; ilogit (modl$lin)</th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
</tr>
<tr>
<td>0.089172</td>
<td>0.238323</td>
<td>0.500000</td>
<td>0.761677</td>
<td>0.910828</td>
</tr>
</table>


Notice the need to distinguish between predictions in the scale of the response and the
link. Now compare the logit, probit and complementary log-log fits:

\> cbind (fitted (modl) , fitted (modp), fitted (modc))
[,1]
[,2]
[,3]
1 0.089172 0.084242 0.12727

<!-- PageBreak -->

<!-- PageHeader="Binomial data" -->
<!-- PageNumber="41" -->

2 0.238323 0.244873 0.24969
3 0.500000 0.498272 0.45459
4 0.761677 0.752396 0.72177
5 0.910828 0.914411 0.93277

These are not very different, but now look at a wider range:

\> x <- seq (-2,8,0.2)
> pl <- ilogit (modl$coef [1] +modl$coef [2] *x)
> pp <- pnorm (modp$coef [1] +modp$coef [2] *x)
> pc <- 1-exp (-exp ( (modc$coef [1] +modc$coef [2] *x) ))
> plot (x, pl, type="1", ylab="Probability", xlab="Dose")
> lines (x, pp, lty=2)
> lines (x, pc, lty=5)


<figure>
<figcaption>Figure 2.3 Probit, logit and complementary log-log compared. The fitted probabilities are shown on the left. The logit fit is shown with a solid line, the probit is shown by a dotted line and the complementary log-log by a dashed line. In the central plot, the ratio of probit to logit probabilities in both tails is shown. The lower tail ratio is given by the solid line while the upper tail ratio is given by the dotted line. In the plot on the right the same information is shown for the ratio of the complementary log-log to the logit. The data range from 0 to 4. We see that the links are similar in this range</figcaption>

0

1.0

3.0

A

₡

2.5

5

Probability

D

0

₪

Ratio

0

Ratio

5

"

0

"

0

9

0

N

0

0.5

0

0

D

2

0

Z

4

G

.

0

2

4

U

H

L

0

\#

4

2

Doso

Dos

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 42" -->

and only begin to diverge as $w e$
extrapolate.

The lines in the left panel of Figure 2.3 do not seem very different, but look at the relative
differences:

\> matplot (x, cbind $\left( p p / p l , \right.$ (1-pp) / (1-
pl) ) , type="1", xlab="Dose", ylab="Ratio")
> matplot (x, cbind $\left( p c / p l , \right.$ (1-pc) / (1-
pl) ) , type="1", xlab="Dose", ylab="Ratio")

as they appear in the second and third panels of Figure 2.3. We see that the probit and
logit differ substantially in the tails. The same phenomenon is observed for the
complementary log-log. This is problematic since the former plot indicates it would be
difficult to distinguish between the two using the data we have. This is an issue in trials
of potential carcinogens and other substances that must be tested for possible harmful
effects on humans. Some substances are highly poisonous in that their effects become
immediately obvious at doses that might normally be experienced in the environment. It
is not difficult to detect such substances. However, there are other substances whose
harmful effects only become apparent at large dosages where the observed probabilities
are sufficiently larger than zero to become estimable without immense sample sizes. In
order to estimate the probability of a harmful effect at a low dose, it would be necessary
to select an appropriate link function and yet the data for high dosages will be of little
help in doing this. As Paracelsus (1493-1541) said, "All substances are poisons; there is
none which is not a poison. The right dose differentiates a poison."

A good example of this problem is asbestos. Information regarding the harmful effects
of asbestos derives from historical studies of workers in industries exposed to very high
levels of asbestos dust. However, we would like to know the risk to individuals exposed
to low levels of asbestos dust such as those found in old buildings. It is virtually
impossible to accurately determine this risk. We cannot accurately measure exposure or
outcome. This is not to argue that nothing should be done, but that decisions should be
made in recognition of the uncertainties.

In summary, the default choice is the logit link. There are three advantages: it leads to
simpler mathematics due the intractability of $\Phi$ it is easier to interpret using odds and it
allows easier analysis of retrospectively sampled data.


### 2.8 Estimation Problems

Estimation using the Fisher scoring algorithm, described in Section 6.2, is usually fast.
However, difficulties can sometimes arise. When convergence fails, it is sometimes due
to a problem exhibited by the following dataset. Urinary androsterone (androgen) and
etiocholanolone (estrogen) values were recorded from 26 healthy males by Margolese
(1970). The data were also analyzed by Hand (1981). We start by plotting the data as
shown in Figure 2.4:

<!-- PageBreak -->

<!-- PageHeader="Binomial data" -->
<!-- PageNumber="43" -->

\> data (hormone)
> plot (estrogen ~
androgen, data=hormone, pch=as . character (orientation) )

We now fit a binomial model to see if the orientation can be predicted from the two
hormone values. Notice that when the response is binary, we can use it directly as the
response variable in the glm function:

\> modl <- glm (orientation ~ estrogen + androgen,
hormone, family=binomial)
Warning messages:

1: Algorithm did not converge in: glm. fit (x = X, y = Y,
weights = weights, start = start, etastart =
etastart,

2: fitted probabilities numerically 0 or 1 occurred in:
glm.fit(x = X, y = Y, weights = weights, start =
start,
etastart = etastart,

We see that there were problems with the convergence. A look at the summary reveals
further evidence:

\> summary (modl)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
<th>Pr (&gt; | z| )</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-84.5</td>
<td>136095.1</td>
<td>-0.00062</td>
<td>1</td>
</tr>
<tr>
<td>$\mathrm { e s t r o g e n }$</td>
<td>-90.2</td>
<td>75911.0</td>
<td>-0.00119</td>
<td>1</td>
</tr>
</table>


<figure>
<figcaption>Figure 2.4 Levels of androgen and estrogen for 15 homosexual (g) and 11 heterosexual (s) males. Solid line shows predictions from g 1m fit that</figcaption>

g

9

LO

4

9

9

g

estrogen

g

g

g

S

3

9

9

S

g

9

S

S

S

ON

OD

S

S

S

g

S

T

1

1

1.5

2.0

2.5

3.0

3.5

4.0

4.5

androgen

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 44" -->

correspond to $p = 1 / 2 .$ The dotted line is
equivalent from brlr.

androgen
100.9
92755.6
0.00109
1

(Dispersion parameter for binomial family taken to be
1)

Null deviance: 3.5426e+01
on 25
degrees of

freedom

Residual deviance: 2.3229e-09
on 23
degrees of

freedom

AIC: 6

Number of Fisher Scoring iterations: 25

Notice that the residual deviance is extremely small indicating a very good fit and yet
none of the predictors are significant due to the high standard errors. We see that the
maximum default number of iterations (25) has been reached. A look at the data reveals
the reason for this. We see that the two groups are linearly separable so that a perfect fit
is possible. We can compute the line separating the groups by finding the line that
corresponds to $p = 1 / 2$ which is when the logit is zero:

$$> a b l i n e \left( - 8 4 . 5 / 9 0 . 2 , 1 0 0 . 9 / 9 0 . 2 \right)$$

We suffer from an embarrassment of riches in this example-we can fit the data
perfectly. Unfortunately, this results in unstable estimates of the parameters and their
standard errors and would (probably falsely) suggest that perfect predictions can be
made. An alternative fitting approach might be considered in such cases called exact
logistic regression. See Cox (1970) and the work of Cyrus Mehta, for example: Mehta
and Patel (1995). Currently, there are no comprehensive packages for such exact methods
in $R ,$ although it is available in products such as LogExactO.

An alternative to exact methods is the bias reduction method of Firth (1993). For the
MLE, $E \widehat { \beta } \neq \beta _ { \mathrm { a n d } }$
indeed a sensible unbiased estimator would be difficult to ob-

tain. Firth's method removes the $O \left( 1 / n \right)$ term from the asymptotic bias of estimated
coefficients. These estimates have the advantage of always being finite:

\> library (brlr)
> modb <- brlr (orientation ~ estrogen + androgen,
hormone,
family=binomial)
> summary (modb)

Coefficients:


<table>
<tr>
<th></th>
<th>Value</th>
<th>Std. Error</th>
<th>t value</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-3.650</td>
<td>2.910</td>
<td>-1.254</td>
</tr>
<tr>
<td>estrogen</td>
<td>-3.586</td>
<td>1.499</td>
<td>-2.393</td>
</tr>
<tr>
<td>androgen</td>
<td>4.074</td>
<td>1.621</td>
<td>2.513</td>
</tr>
</table>


Deviance: 3.70

Penalized deviance:
4.184

Residual df: 23

<!-- PageBreak -->

<!-- PageNumber="45" -->
<!-- PageHeader="Binomial data" -->

We can see that this results in significant predictors which we expect given Figure 2.4.
Although the fit appears, judging from the coefficients, to be different from the glm
result, it is effectively very close as we can see by plotting the line corresponding to
$p = 1 / 2 :$

$$> a b l i n e \left( - 3 . 6 5 / 3 . 5 8 6 , 4 . 0 7 4 / 3 . 5 8 6 , l t y = 2 \right)$$

Instability in parameter estimation will also occur in datasets that approach linear
separability. Care will be needed in such cases.


### 2.9 Goodness of Fit

The deviance is one measure of how well the model fits the data, but there are
alternatives. The Pearson's $X ^ { 2 }$ statistic takes the general form:

$$X ^ { 2 } = \sum _ { i = 1 } ^ { n } \frac { \left( O _ { i } - E _ { i } \right) ^ { 2 } } { E _ { i } }$$ ☒

where $O _ { i }$ is the observed counts and $E _ { i }$ are the expected counts for case $i .$ For a binomial
response, we count the number of successes for which $0 _ { i } = y _ { i }$ while $E _ { i } = \pi _ { i } j _ { i } ^ { 2 }$ failures
for which $O _ { i } = n _ { i } - y _ { i }$ and $E _ { i } = n _ { i } \left( 1 - \check { p } _ { i } \right) _ { \text { whicl } }$ results in:

$$X ^ { 2 } = \sum _ { i = 1 } ^ { n } \frac { \left( y _ { i } - n _ { i } \right) ^ { 2 } } { n _ { i } \beta _ { i } \left( 1 - \widehat { p } _ { i } \right) }$$ ☒

If we define Pearson residuals as:

$$r _ { i } ^ { P } = \left( y _ { i } - n _ { i } p _ { i } \right) / \sqrt { v a r j _ { i } }$$

which can be viewed as a type of standardized residual, then $X ^ { 2 } = \sum _ { i = 1 } ^ { n } \left( r _ { i } ^ { P } \right) ^ { 2 }$ the
Pearson's $X ^ { 2 }$ is analogous to the residual sum of squares used in normal linear models.

The Pearson $X ^ { 2 }$ will typically be close in size to the deviance and can be used in the
same manner. Alternative versions of the hypothesis tests $d e s c r i b e d$ above might use the
$X ^ { 2 }$ in place of the deviance with the same approximate null distributions.
☒

However, some care is necessary because the model is fit to minimize the deviance
and not the Pearson's $X ^ { 2 } .$ This means that it is possible, although unlikely, that the $X ^ { 2 }$
could increase as a predictor is added to the model. $X ^ { 2 }$ can be computed like this:

\> modl <- glm (cbind (dead, alive) ~ conc,
family=binomial, data=bliss)
> sum (residuals (modi, type="pearson") ^2)
[1] 0.36727
> deviance(modl)
[1] 0.37875

As can be seen, there is little difference here between $X ^ { 2 }$ and the deviance.

<!-- PageBreak -->

$$E x t e n d i n g \quad t h e \quad l i n e a r \quad m o d e l \quad w i t h \quad R \quad 4 6$$

The proportion of variance explained or $R ^ { 2 }$ is a popular measure of fit for normal
linear models. We might consider applying the same concept to binomial regression
models by using the proportion of deviance explained. However, a better statistic is due
to Naglekerke (1991):

$$R ^ { 2 } = \frac { 1 - \left( L _ { 0 } / L \right) ^ { 2 / n } } { 1 - L _ { 0 } ^ { 2 / n } } = \frac { 1 - \exp \left( \left( D - D _ { n u l l } \right) / n \right) } { 1 - e x p \left( - D _ { n u l } / n \right) }$$

where $n$ is the number of binary observations and $L _ { 0 }$ the maximized likelihood under
the null. The numerator can be seen as a ratio of the relative likelihood with the $1 / n$
power having the effect of a geometric mean on the observations. The denominator
simply normalizes so that $0 \leq R ^ { 2 } \leq 1 .$ For example, for the Bliss insect data, the $R ^ { 2 }$ is:

$$> \left( 1 - \exp \left( \left( m o d 1 \text { sdev-modl } S n u l l \right) / 1 5 0 \right) \right) / \left( 1 - e \times p \left( - \right. \right.$$

[1] 0.99532

Notice that we have used $n = 1 5 0$ as there are 5 covariate class with 30 observations each.
We can see that this is a very good fit.


### 2.10 Prediction and Effective Doses

Sometimes we wish to predict the outcome for given values of the covariates. For binary
data this will mean estimating the probability of success. For given covariates $x _ { 0 } ,$
$\dot { \bar { \eta } } = x _ { 0 } \dot { \bar { \beta } } _ { \mathrm { w i t } }$ variance given by $x _ { 0 } ^ { T } \left( X ^ { T } W X \right) ^ { - 1 } x _ { 0 } .$ Approximate confidence intervals
may be obtained using a normal approximation. To get an answer in the probability scale,
it will be necessary to transform back using the inverse of the link function. We predict
the response for the insect data:

\> data (bliss)
> modl <- glm (cbind (dead, alive) ~ conc,
family=binomial, data=bliss)
> lmodsum <- summary(modl)

We show how to predict the response at dose of 2.5:

\> x0 <- c (1, 2.5)
> eta0 <- sum (x0*coef (modl) )
> ilogit (eta0)
[1] 0.64129

A 64% predicted chance of death at this dose-now compute a 95% confidence interval
(CI) for this probability. First, extract the variance matrix of the coefficients:

\> (cm <- lmodsum$cov.unsealed)

<!-- PageBreak -->

<!-- PageNumber="47" -->
<!-- PageHeader="Binomial data" -->


<table>
<tr>
<th></th>
<th>(Intercept)</th>
<th>conc</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>0.174630</td>
<td>-0.065823</td>
</tr>
<tr>
<td>conc</td>
<td>-0.065823</td>
<td>0.032912</td>
</tr>
</table>


The standard error on the logit scale is then:

$$> \text { se } < - \text { sqrt } \left( t \left( x 0 \right) \text { o } * \frac { 0 } { 0 } \text { cm } \frac { 0 } { 0 } * \frac { 0 } { 0 } \times 0 \right)$$

so the CI on the probability scale is:

\> ilogit (c(eta0-1.96\*se, eta0+1.96\*se) )
[1] 0.53430 0.73585

A more direct way of obtaining the same result is:

\> predict (modi, newdata=data. frame (conc=2.5) , se=T)
$fit
[1] 0.58095
$se. fit
[1] 0.2263
> ilogit(c(0.58095-1.96\*0.2263, 0.58095+1.96\*0.2263))
[1] 0.53430 0.73585

Note that in contrast to the linear regression situation, there is no distinction possible
between confidence intervals for a future observation and those for the mean response.
Now we try predicting the response probability at the low dose of -5:

\> x0 <- c (1,-5)
> se <- sqrt (t (x0) %\*% cm %\*% x0)
> eta0 <- sum (x0\*1mod$coef)
> ilogit (c(eta0-1.96\*se, eta0+1.96*se) )
[1] 2.3577e-05 3.6429e-03

This is not a wide interval in absolute terms, but in relative terms, it certainly is. The
upper limit is about 100 times larger than the lower limit.

Logistic regression models have been widely used for classification purposes.
Depending on whether $\ddot { P }$ greater or less than 0.5, the case may be classified as a
success or failure. In cases where the losses due to misclassification are not symmetrical,
such as in disease diagnosis, critical values other than 0.5 should be used. Another
example is in credit scoring. When financial institutions decide whether to make a loan, it
is helpful to estimate the probability that a given borrower will default. $\mathrm { A }$ logistic
regression model is one way in which this probability can be estimated using past
financial data.

When there is a single (continuous) covariate or when other covariates are held fixed,
we sometimes wish to estimate the value of $x$ corresponding to a chosen $p .$ For example
we may wish to determine which dose, $x ,$ will lead to a probability of success $p .$ ED50
stands for the effective dose for which there will be a 50% chance of success. When the

<!-- PageBreak -->


## Extending the linear model with $R$ 48

objective is to kill the subjects or determine toxicity, as when using insecticides, the term
LD50 would be used. LD stands for lethal dose. Other percentiles are also of interest. For
a logit link, we can set $p = 1 / 2$ and then solve for $x$ to find:

$$\widetilde { \mathrm { E D 5 0 } } = - \widetilde { \beta } _ { 0 } / \widetilde { \beta } _ { 1 }$$

Using the Bliss data, the LD50 is:

$$> \left( l d 5 0 < - \quad - \quad 1 m o d c o e f \left[ 1 \right] / 1 m o d c o e f \left[ 2 \right] \right)$$

(Intercept)
2

To determine the standard error, we can use the delta method. The general expression for
the variance of $g \left( \theta \right)$ for multivariate $\theta$ is given by

$$g \left( \widehat { \theta } \right) \approx g ^ { \prime } \left( \widehat { \theta } \right) ^ { T } \mathrm { v a r } \widehat { \theta } g ^ { \prime } \left( \widehat { \theta } \right)$$ ☒

which, in this example, works out as:

\> dr <- c(-1/lmod$coef[2],lmod$coef[1]/lmod$coef[2]^2)
> sqrt (dr %\*% lmodsum$cov. un %\*% dr) [, ]
[1] 0.17844

So the 95% CI is given by:

$$> c \left( 2 - 1 . 9 6 * 0 . 1 7 8 , 2 + 1 . 9 6 * 0 . 1 7 8 \right)$$

[1] 1.6511 2.3489

Other levels may be considered-the effective dose $x _ { p }$ for probability of success $p$ is:

$$x _ { p } = \frac { \log i \left( p \right) - \beta _ { 0 } } { \beta _ { 1 } }$$

So, for example:

\> ed90 <- (logit(0.9)-lmod$coef[1])/lmod$coef[2]
> ed90
(Intercept)
3.8911

More conveniently, we may use the dose. $p$ function in the MASS package:

\> library (MASS)
> dose.p(lmod,p=c(0.5,0.9))
Dose
SE
p = 0.5:2.0000 0.17844
p = 0.9:3.8911 0.34499

<!-- PageBreak -->

<!-- PageHeader="Binomial data 49" -->


### 2.11 Overdispersion

If the binomial GLM model specification is correct, we expect that the residual deviance
will be approximately distributed $x ^ { 2 }$ with the appropriate degrees of freedom. Sometimes,
we observe a deviance that is much larger than would be expected if the model were
correct. We must then determine which aspect of the model specification is incorrect.

The most common explanation is that we have the wrong structural form for the
model. We have not included the right predictors or we have not transformed or
combined them in the correct way. We have a number of ways of determining the
importance of potential additional predictors and diagnostics for determining better
transformations-see Section 6.4. Suppose, however, that we are able to exclude this
explanation. This is difficult to achieve, but when we have only one or two predictors, it
is feasible to explore the model space quite thoroughly and be sure that there is not a
plausible superior model formula.

Another common explanation for a large deviance is the presence of a small number
of outliers. Fortunately, these are easily checked using diagnostic methods explained
more fully in Section 6.4. When larger numbers of points are identified as outliers, they
become unexceptional, and we might more reasonably conclude that there is something
amiss with the error distribution.

Sparse data can also lead to large deviances. In the extreme case of a binary response,
the deviance is not even approximately $x ^ { 2 } .$ In situations where the group sizes are simply
small, the approximation is poor. Because we cannot judge the fit using the deviance, we
shall exclude this case from further consideration in this section.

Having excluded these other possibilities, we might explain a large deviance by
deficiencies in the random part of the model. A binomial distribution for $Y$ arises when
the probability of success $p$ is independent and identical for each trial within the group. If
the group size is m, then var $Y = m p \left( 1 - p \right)$ if the binomial assumptions are correct.
However, the assumptions are broken, the variance may be greater. This is
overdispersion. In rarer cases, the variance is less and underdispersion results.

There are two main ways that overdispersion can arise-the independent or identical
assumptions can be violated. We look at the constant $p$ assumption first. It is easy to see
how there may be some unexplained heterogeneity within a group that might lead to
some variation in $p .$ For example, in the shuttle disaster case study of Section 2.1, the
position of the O-ring on the booster rocket may have some effect on the failure
probability. Yet this variable was not recorded and so we cannot include it as a predictor.
Heterogeneity can also result from clustering. Suppose a population is divided into
clusters, so that when you take a sample, you actually get a sample of clusters. This
would be common in epidemiological applications.

Let the sample size be $m ,$ the cluster size be $k$ and the number of clusters be $l = m / k .$ Let
the number of successes in cluster $i$ be $Z _ { i } \sim B \left( k , p _ { i } \right) .$ Now suppose that $p _ { i }$ is a random
variable such that $E p a p$ and var $p _ { i } = \tau ^ { 2 } p \left( 1 - p \right) .$ Let the total number of successes be
$Y = Z _ { 1 + \cdots } + Z _ { I } .$ Then:

$$E Y = \sum E Z = \sum _ { i = 1 } ^ { I } k p = m p$$

as in the standard case, but:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 50" -->

$$Y = \sum v a r Z _ { i } = \sum \left\{ E \left( v a r \left( Z _ { i } | p _ { i } \right) \right) + v a r \left( E \left( Z _ { i } | p _ { i } \right) \right) \right\} = 1 + \left( k - 1 \right) \tau ^ { 2 } m p \left( 1 - p \right)$$
var

So $Y$ is overdispersed since $1 + \left( k - 1 \right) \tau ^ { 2 } \geq 1 .$ Notice that in the sparse case, $m = 1 ,$ and this
problem cannot arise.

Overdispersion can also result from dependence between trials. If the response has a
common cause, say a disease is influenced by genes, the responses will tend to be
positively correlated. For example, subjects in human or animal trials may be influenced
in their response by other subjects. If the food supply is limited, the probability of
survival of an animal may be increased by the death of others. This circumstance would
result in underdispersion.

The simplest approach for modeling overdispersion is to introduce an additional
dispersion parameter, $\sigma ^ { 2 } .$ In the standard binomial case $\sigma ^ { 2 } = \phi = 1$ 1.We now let $\sigma ^ { 2 }$ vary
and estimate using the data. Notice the similarity to linear regression. The dispersion
parameter may be estimated using:

$$6 ^ { 2 } = \frac { x ^ { 2 } } { n - p }$$

Using the deviance in place of the Pearson's $X ^ { 2 }$ is not recommended as it may not be
consistent. The estimation of $\beta$ is unaffected since $\sigma ^ { 2 }$ does not change the mean response
but:

$$\mathrm { v a r } \beta = 6 ^ { 2 } \left( x ^ { T } W x \right) ^ { - 1 }$$

So we need to scale up the standard errors by a factor of $\mathfrak{F} .$

We cannot use the difference in deviances when comparing models, because the test
statistic will be distributed $\sigma ^ { 2 } x ^ { 2 } .$ Since $\sigma ^ { 2 }$ is not known and must be estimated in the
overdispersion situation, an F-statistic must be used:

$$F = \frac { \left( D _ { \text { small } } - D _ { l a r g e } \right) / \left( d f _ { \text { small } } - d f _ { l a r g e } \right) } { \dot { \sigma } ^ { 2 } }$$

This statistic is only an approximately $\mathrm { F }$ distributed, in contrast to the Gaussian case.

This dispersion parameter method is only appropriate when the covariate classes are
roughly equal in size. If not, more sophisticated methods should be used. One such
approach uses the beta-binomial distribution where we assume that p follows a beta
distribution. This approach is discussed in Williams (1982) and Crowder (1978) and can
be implemented using the aod package in $\mathrm { R } .$

In Manly (1978), an experiment is reported where boxes of trout eggs were buried at
five different stream locations and retrieved at four different times, specified by the
number of weeks after the original placement. The number of surviving eggs was
recorded. The box was not returned to the stream. The data is also analyzed by Hinde and
Demetrio (1988). We can construct a tabulation of the data by:

\> data (troutegg)
> ftable (xtabs (cbind (survive, total)
location+period, troutegg) )

<!-- PageBreak -->

<!-- PageNumber="51" -->
<!-- PageHeader="Binomial data" -->


<table>
<tr>
<td colspan="3"></td>
<td colspan="2"></td>
<td>survive</td>
<td>total</td>
</tr>
<tr>
<td colspan="3">location $\mathrm { p e r i o d }$</td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>4</td>
<td></td>
<td></td>
<td></td>
<td>89</td>
<td>94</td>
</tr>
<tr>
<td></td>
<td>7</td>
<td></td>
<td></td>
<td></td>
<td>94</td>
<td>98</td>
</tr>
<tr>
<td></td>
<td>8</td>
<td></td>
<td colspan="2"></td>
<td>77</td>
<td>86</td>
</tr>
<tr>
<td></td>
<td>11</td>
<td></td>
<td colspan="2"></td>
<td>141</td>
<td>155</td>
</tr>
<tr>
<td>2</td>
<td>4</td>
<td></td>
<td colspan="2"></td>
<td>106</td>
<td>108</td>
</tr>
<tr>
<td></td>
<td>7</td>
<td></td>
<td></td>
<td></td>
<td>91</td>
<td>106</td>
</tr>
<tr>
<td></td>
<td>8</td>
<td></td>
<td></td>
<td></td>
<td>87</td>
<td>96</td>
</tr>
<tr>
<td></td>
<td>11</td>
<td></td>
<td colspan="2"></td>
<td>104</td>
<td>122</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td></td>
<td colspan="2"></td>
<td>119</td>
<td>123</td>
</tr>
<tr>
<td></td>
<td>7</td>
<td></td>
<td colspan="2"></td>
<td>100</td>
<td>130</td>
</tr>
<tr>
<td></td>
<td>8</td>
<td></td>
<td colspan="2"></td>
<td>88</td>
<td>119</td>
</tr>
<tr>
<td></td>
<td>11</td>
<td></td>
<td colspan="2"></td>
<td>91</td>
<td>125</td>
</tr>
<tr>
<td>4</td>
<td>4</td>
<td></td>
<td colspan="2"></td>
<td>104</td>
<td>104</td>
</tr>
<tr>
<td></td>
<td>7</td>
<td></td>
<td colspan="2"></td>
<td>80</td>
<td>97</td>
</tr>
<tr>
<td></td>
<td>8</td>
<td></td>
<td colspan="2"></td>
<td>67</td>
<td>99</td>
</tr>
<tr>
<td></td>
<td>11</td>
<td></td>
<td colspan="2">111</td>
<td>132</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>4</td>
<td></td>
<td colspan="2">49</td>
<td>93</td>
<td></td>
</tr>
<tr>
<td></td>
<td>7</td>
<td></td>
<td colspan="2">11</td>
<td>113</td>
<td></td>
</tr>
<tr>
<td></td>
<td>8</td>
<td></td>
<td colspan="2">18</td>
<td>88</td>
<td></td>
</tr>
<tr>
<td></td>
<td>11</td>
<td></td>
<td colspan="2">0</td>
<td>138</td>
<td></td>
</tr>
</table>


Notice that in one case, all the eggs survive, while in another, none of the eggs survive.
We now fit a binomial GLM for the two main effects:

\> bmod <- glm (cbind (survive, total-survive)
location+period,
family=binomial, troutegg)
> bmod
Coefficients :
(Intercept)
location2
location3

~

ocation5
4.636
-0.417

location4
l

-1.242
\-

0.951
-4.614
period8
period11

period7
-2.170
-2.326
-2.450

Degrees of Freedom: 19 Total

(i.e. Null) ; 12 Residual

Null Deviance:
1020

Residual Deviance: 64.5 AIC: 157

The deviance of 64.5 on 12 degrees of freedom seems to show that this model does not
fit. Before we conclude that there is overdispersion, we need to eliminate other potential
explanations. With about 100 eggs in each box, we have no problem with sparseness, but
we do need to check for outliers and look at the model formula. $A$ half-normal plot of the
residuals is a good way to check for outliers:

halfnorm (residuals (bmod) )

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 52" -->

The half-normal plot is shown in the left panel of Figure 2.5. No single outlier is
apparent. Perhaps one can discern a larger number of residuals which seem to follow a
more dispersed distribution than the rest.

We can also check whether the predictors are correctly expressed by plotting the
empirical logits. These are defined as:

$$\log \left( \frac { y + 1 / 2 } { m - y + 1 / 2 } \right)$$

The halves are added to prevent infinite values for groups consisting of all successes or
failures. We now construct an interaction plot of the empirical logits:


<figure>
<figcaption>Figure 2.5 Diagnostic plots for the trout egg model. A half-normal plot of the residuals is shown on the left and an interaction plot of the empirical logits is shown on the right.</figcaption>

15

₪

0

₦

₸

0

7

00

05

1.0

1.5

20

4

7

0

11

Hat-normal quintilas

Period

</figure>


\> elogits <-
log ( (troutegg$survive+0.5) / (troutegg$total-
troutegg$survive+0.5))
>
with (troutegg, interaction. plot (period, location, elogits)
)

Interaction plots are always difficult to interpret conclusively, but there is no obvious sign
of large interactions. So there is no evidence that the linear model is inadequate. We do
not have any outliers and the functional form of the model appears to be suitable, but the
deviance is still larger than should be expected. Having eliminated these more obvious
causes as the source of the problem, we may now put the blame on overdispersion.

<!-- PageBreak -->

<!-- PageNumber="53" -->
<!-- PageHeader="Binomial data" -->

Possible reasons for the overdispersion include inhomogeneous trout eggs, variation in
the experimental procedures or unknown variables affecting survival.

We can estimate the dispersion parameter as:

$$> \left( s i g m a 2 < - s u m \left( r e s s i d u a l s \left( b m o d , t y p e = ^ { \prime \prime } p e a r s o n ^ { \prime \prime } \right) \wedge 2 \right) / 1 2 \right.$$

We see that this is substantially larger than one as it would be in the standard binomial
GLM. We can now make F-tests on the predictors using:

\> drop1 (bmod, scale=sigma2, test="F")
Single term deletions
scale:
5.3303


<table>
<tr>
<th></th>
<th>Df</th>
<th>Deviance</th>
<th>AIC</th>
<th>F value</th>
<th>$\mathrm { P r } \left( \mathrm { F } \right)$</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td></td>
<td>64</td>
<td>157</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">location 4</td>
<td>914</td>
<td>308</td>
<td>39.5</td>
<td>8.1e-07</td>
</tr>
<tr>
<td colspan="2">period 3</td>
<td>229</td>
<td>182</td>
<td>10.2</td>
<td>0.0013</td>
</tr>
</table>


Warning message:

F test assumes quasibinomial family in:
dropl. glm (bmod, scale = sigma2, test = "F")

We see that both terms are clearly significant. It is necessary to specify the scale
argument using the estimated value of $\sigma ^ { 2 } .$ If this argument is omitted, the deviance will be
used in the estimation of the dispersion parameter. For this particular dataset, it makes
very little difference, but in some cases, using the deviance to estimate the dispersion
gives inconsistent results. The warning message reminds us that the use of free dispersion
parameter results in a model that is no longer a true binomial GLM, but rather what is
known as a quasi-binomial GLM. More on such models may be found in Section 7.4.

No goodness of fit test is possible because we have a free dispersion parameter. We
can use the dispersion parameter to scale up the estimates of the standard error as in:

\> summary (bmod, dispersion=sigma2 )
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>z value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>4.636</td>
<td></td>
<td>0.649</td>
<td>7.14</td>
<td>9.5e-13</td>
</tr>
<tr>
<td>location2</td>
<td>-0.417</td>
<td></td>
<td>0.568</td>
<td>-0.73</td>
<td>0.463</td>
</tr>
<tr>
<td>$l o c a t i o n 3$</td>
<td>-1.242</td>
<td></td>
<td>0.507</td>
<td>-2.45</td>
<td>0.014</td>
</tr>
<tr>
<td>$l o c a t i o n 4$</td>
<td>-0.951</td>
<td></td>
<td>0.528</td>
<td>-1.80</td>
<td>0.072</td>
</tr>
<tr>
<td>$l o c a t i o n 5$</td>
<td>-4.614</td>
<td></td>
<td>0.578</td>
<td>-7.99</td>
<td>$1 . 4 e - 1 5$</td>
</tr>
<tr>
<td>$\mathrm { p e r i o d } 7$</td>
<td>-2.170</td>
<td></td>
<td>0.550</td>
<td>-3.94</td>
<td>8.1e-05</td>
</tr>
<tr>
<td>period8</td>
<td>-2.326</td>
<td></td>
<td>0.561</td>
<td>-4.15</td>
<td>$3 . 4 e - 0 5$</td>
</tr>
<tr>
<td>period11</td>
<td>-2.450</td>
<td></td>
<td>0.540</td>
<td>-4.53</td>
<td>$5 . 8 e - 0 6$</td>
</tr>
</table>


### 2.12 Matched Case-Control Studies

In a case-control study, we try to determine the effect of certain risk factors on the
outcome. We understand that there are other confounding variables that may affect the

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 54" -->

outcome. One approach to dealing with these is to measure or record them, include them
in the logistic regression model as appropriate and thereby control for their effect. But
this method requires that we model these confounding variables with the correct
functional form. This may be difficult. Also, making an appropriate adjustment is
problematic when the distribution of the confounding variables is quite different in the
cases and controls. So we might consider an alternative where the confounding variables
are explicitly adjusted for in the design.

In a matched case-control study, we match each case (diseased person, defective
object, success, etc.) with one or more controls that have the same or similar values of
some set of potential confounding variables. For example, if we have a 56-year-old,
Hispanic male case, we try to match him with some number of controls who are also 56-
year-old Hispanic males. This group would be called a matched set. Obviously, the more
confounding variables one specifies, the more difficult it will be to make the matches.
Loosening the matching requirements, for example, accepting controls who are 50-60
years old might be necessary. Matching also gives us the possibility of adjusting for
confounders that are difficult to measure. For example, suppose we suspect an
environmental effect on the outcome. However, it is difficult to measure exposure,
particularly when we may not know which substances are relevant. We could match
subjects based on their place of residence or work. This would go some way to adjusting
for the environmental effects.

Matched case-control studies also have some disadvantages apart from the difficulties
of forming the matched sets. One loses the possibility of discovering the effects of the
variables used to determine the matches. For example, if we match on sex, we will not be
able to investigate a sex effect. Furthermore, the data will likely be far from a random
sample of the population of interest. So although relative effects may be found, it may be
difficult to generalize to the population.

Sometimes, cases are rare but controls are readily available. A1: $M$ design has $M$
controls for each case. $M$ is typically small and can even vary in size from matched set to
matched set due to difficulties in finding matching controls and missing values. Each
additional control yields a diminished return in terms of increased efficiency in
estimating risk factors-it is usually not worth exceeding $M = 5 .$

For individual $i$ in the $j ^ { t h }$ matched set, we also observe a covariate vector $x _ { i j }$ which will
include the risk factors of interest plus any other variables that we may wish to adjust for,
but were unable for various reasons to include among the criteria used to match the sets.
It is important that the decision to include a subject in the study be independent of the
risk factors as in the unmatched case-control studies. Suppose we have $n$ matched sets
and that we take $i = 0$ to represent the case and $i = 1 , \ldots , M$ to represent the controls. We
propose a logistic regression model of the following form:

$\log \mathrm { i t } \left( p _ { j } \left( x _ { i j } \right) \right) = \alpha _ { j } + \beta ^ { T } x _ { i j }$

The $\alpha _ { j }$ models the effect of the confounding variables in the $j ^ { t h }$ matched set. Given a
matched $\sec t$ of $M + 1$ subjects known to have one case and $M$ controls, the conditional
probability of the observed outcome, or, in other words, that subject $i = 0$ is the case and
the rest are controls is:

<!-- PageBreak -->

<!-- PageNumber="55" -->
<!-- PageHeader="Binomial data" -->

$$\frac { \exp \beta ^ { T } x _ { 0 j } } { \sum _ { i = 0 } ^ { M } \exp \beta ^ { T } x _ { i j } }$$

Notice that $\alpha _ { j }$ cancels out in this expression. We may then form the conditional likelihood
for the model by taking the product over all the matched sets:

$$L \left( \beta \right) = \prod _ { j = 1 } ^ { n } \left\{ 1 + \sum _ { i = 1 } ^ { M } \exp \left[ \beta ^ { T } \left( x _ { i j } - x _ { 0 j } \right) \right] \right\} ^ { - 1 }$$

We may now employ standard likelihood methods to make inference-see Breslow
(1982) for details. The likelihood takes the same form as that used for the proportional
hazards model used in survival analysis. This is convenient because we may use software
developed for those models as we demonstrate below. Since the as are not estimated, we
cannot make predictions about individuals, but only make statements about the relative
risks as measured by the Bs. This same restriction also applies to the unmatched model,
so this is nothing new.

In Le (1998), a matched case-control study is presented concerning the association
between x-rays and childhood acute myeloid leukemia. The sets are matched on age, race
and county of residence. For the most part, there is only one control for each case, but
there are a few instances of two controls. We start with a look at the data:

\> data (amlxray)
> head (amlxray)
ID disease Sex downs age Mray MupRay MlowRay Fray
Cray CnRay
1


<table>
<tr>
<td>7004</td>
<td></td>
<td>1</td>
<td>F</td>
<td>no</td>
<td></td>
<td>0</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>n</td>
</tr>
<tr>
<td>o</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>7004</td>
<td></td>
<td>0</td>
<td>F</td>
<td>no</td>
<td>0</td>
<td></td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>n</td>
</tr>
<tr>
<td>o</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>7006</td>
<td></td>
<td>1</td>
<td>M</td>
<td>no</td>
<td>6</td>
<td></td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>ye</td>
</tr>
<tr>
<td>s</td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>4</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>7006</td>
<td></td>
<td>0</td>
<td>M</td>
<td>no</td>
<td>6</td>
<td></td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>ye</td>
</tr>
<tr>
<td>s</td>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>7009</td>
<td></td>
<td>1</td>
<td>F</td>
<td>no</td>
<td>8</td>
<td></td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>n</td>
</tr>
<tr>
<td>o</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>7009</td>
<td></td>
<td>0</td>
<td>F</td>
<td>no</td>
<td>8</td>
<td></td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>n</td>
</tr>
<tr>
<td>o</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


Only the age is presented here as one of the matching variables. In the three sets shown
here, we see that both subjects have the same age and the first is the case and the second
is the control. The other variables are risk factors of interest.

<!-- PageBreak -->


## Extending the linear model with $R$ 56

Down syndrome is known to be a risk factor. There are only seven such subjects in the
dataset:

\> amlxray [amlxray$downs == "yes", 1 : 4]


<table>
<tr>
<th></th>
<th>ID</th>
<th>disease</th>
<th>Sex</th>
<th>downs</th>
</tr>
<tr>
<td>7</td>
<td>7010</td>
<td>1</td>
<td>M</td>
<td>yes</td>
</tr>
<tr>
<td>17</td>
<td>7018</td>
<td>1</td>
<td>$\bar { E }$</td>
<td>yes</td>
</tr>
<tr>
<td>78</td>
<td>7066</td>
<td>1</td>
<td>F</td>
<td>$\mathrm { y e s }$</td>
</tr>
<tr>
<td>88</td>
<td>7077</td>
<td>1</td>
<td>M</td>
<td>yes</td>
</tr>
<tr>
<td>173</td>
<td>7146</td>
<td>1</td>
<td>F</td>
<td>yes</td>
</tr>
<tr>
<td>196</td>
<td>7176</td>
<td>1</td>
<td>F</td>
<td>yes</td>
</tr>
<tr>
<td>210</td>
<td>7189</td>
<td>1</td>
<td>F</td>
<td>$\mathrm { y e s }$</td>
</tr>
</table>


We see that all seven subjects are cases. If we include this variable in the regression, its
coefficient is infinite. Given this and the prior knowledge, it is simplest to exclude all
these subjects and their associated matched subjects:

$$> \left( \mathrm { i i } < - \mathrm { w h i c h } \left( \mathrm { a m l x i c y s i d o w n s } = = ^ { \prime \prime } \mathrm { y e s } ^ { \prime \prime } \right) \right)$$

[1] 7 17 78 88 173 196 210

\> ramlxray <- amlxray[-c (ii, ii+1) , ]

The variables Mray, MupRay and MlowRay record whether the mother has ever had an
x-ray, ever had an upper body x-ray and ever had a lower body x-ray, respectively. These
variables are closely associated, so we will pick just Mray for now and investigate the
others more closely if indicated. We will also use CnRay, a four-level ordered factor
grouping the number of x-rays that the child has received in preference to Cray which
merely indicates whether the child has ever had an x-ray.

The clogit function fits a conditional logit model. Since the $\mathrm { l i k e l i h o o d }$ is identical with
that from a proportional hazards model, it may be found in the survival package. The
matched sets must designated by the strata function:

\> library (survival)
> cmod <- clogit (disease ~
Sex+Mray+Fray+CnRay+strata (ID) , ramlxray)
> summary (cmod)


<table>
<tr>
<th></th>
<th>coef exp</th>
<th>(coef)</th>
<th>se (coef)</th>
<th>z</th>
<th>p</th>
</tr>
<tr>
<td>$\mathrm { S e x M }$</td>
<td>0.156</td>
<td>1.17</td>
<td>0.386</td>
<td colspan="2">0.405 0.6900</td>
</tr>
<tr>
<td>Mrayyes</td>
<td>0.228</td>
<td>1.26</td>
<td>0.582</td>
<td>0.391</td>
<td>0.7000</td>
</tr>
<tr>
<td>Frayyes</td>
<td>0.693</td>
<td>2.00</td>
<td>0.351</td>
<td>1.974</td>
<td>0.0480</td>
</tr>
<tr>
<td>CnRay . L</td>
<td>1.941</td>
<td>6.96</td>
<td>0.621</td>
<td>3.127</td>
<td>0.0018</td>
</tr>
<tr>
<td>CnRay . Q</td>
<td>-0.248</td>
<td>0.78</td>
<td>0.582</td>
<td colspan="2">-0.426 0.6700</td>
</tr>
<tr>
<td>CnRay . C</td>
<td>-0.580</td>
<td>0.56</td>
<td>0.591</td>
<td>-0.982</td>
<td>0.3300</td>
</tr>
</table>


exp (coef)

exp (-coef)

lower
. 95
upper . 95


<table>
<tr>
<td>SexM</td>
<td>1.17</td>
<td>0.855</td>
<td>0.549</td>
<td>2.49</td>
</tr>
<tr>
<td>Mrayyes</td>
<td>1.26</td>
<td>0.796</td>
<td>0.401</td>
<td>3.93</td>
</tr>
<tr>
<td>Frayyes</td>
<td>2.00</td>
<td>0.500</td>
<td>1.005</td>
<td>3.98</td>
</tr>
<tr>
<td>CnRay . L</td>
<td>6.96</td>
<td>0.144</td>
<td>2.063</td>
<td>23.51</td>
</tr>
<tr>
<td>CnRay . Q</td>
<td>0.78</td>
<td>1.281</td>
<td>0.249</td>
<td>2.44</td>
</tr>
<tr>
<td>CnRay. C</td>
<td>0.56</td>
<td>1.786</td>
<td>0.176</td>
<td>1.78</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="57" -->
<!-- PageHeader="Binomial data" -->

Rsquare= 0.089
(max possible= 0.499)
Likelihood ratio test= 20.9 on 6 df, p=0.00192
Wald test
= 14.5 on 6 df, p=0.0246
Score (logrank) test = 18.6 on 6 df, p=0.0049

The overall tests for significance of the predictors indicate that at least some of the
variables are significant. We see that Sex and whether the mother had an x-ray are not
significant. There seems little point in investigating the other x-ray variables associated
with the mother. An x-ray on the father is marginally significant. However, the x-ray on
the child has the clearest effect. Because this is an ordered factor, we have used linear,
quadratic and cubic contrasts. Only the linear effect is significant.

The second table of coefficients gives us information helpful for interpreting the size
of the effects. We see that the father having had an x-ray doubles the odds of the disease.
The interpretation of the number of x-rays of the child is more difficult to interpret
because of the coding. Since we have found only a linear effect, we convert CnRay to the
numerical values 1-4 using unclass. We also drop the insignificant predictors:

\> cmodr <- clogit (disease ~
Fray+unclass (CnRay) +strata (ID) , ramlxray)
> summary (cmodr)


<table>
<tr>
<th></th>
<th>coef exp</th>
<th>(coef)</th>
<th colspan="2">se (coef) z p</th>
</tr>
<tr>
<td>Frayyes</td>
<td>0.670</td>
<td>1.96</td>
<td>0.344 1.95</td>
<td>0.05100</td>
</tr>
<tr>
<td>unclass (CnRay)</td>
<td>0.814</td>
<td>2.26</td>
<td>0.237 3.44</td>
<td>0.00058</td>
</tr>
<tr>
<td></td>
<td colspan="4">exp (coef) exp (-coef) lower .95 upper .95</td>
</tr>
<tr>
<td>Frayyes</td>
<td>1.96</td>
<td></td>
<td>0.512 0.996</td>
<td>3.84</td>
</tr>
<tr>
<td>unclass (CnRay)</td>
<td>2.26</td>
<td></td>
<td>0.443 1.419</td>
<td>3.59</td>
</tr>
</table>


The codes for Cnray are 1=none, $2 = 1$ or 2 x-rays, $3 = 3$ or 4 x-rays and $4 = 5$ or more x-
rays. We see that the odds of the disease increase by a factor of 2.26 as we move between
adjacent categories. Notice that the father's x-ray variable is now just insignificant in this
regression underlining its borderline status.

An incorrect analysis of this data ignores the matching structure and simply uses a
binomial GLM:

\> gmod <- glm (disease ~
Fraytunclass (CnRay) , family=binomial, ramlxray)
> summary (gmod)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>z value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-1.162</td>
<td></td>
<td>0.301</td>
<td>-3.86</td>
<td>0.00011</td>
</tr>
<tr>
<td>Frayyes</td>
<td>0.500</td>
<td colspan="2">0.308</td>
<td>1.63</td>
<td>0.10405</td>
</tr>
<tr>
<td>unclass (CnRay)</td>
<td>0.601</td>
<td></td>
<td>0.177</td>
<td>3.39</td>
<td>0.00071</td>
</tr>
</table>


The results are somewhat different.

Although we have found an effect due to x-rays of the child, we cannot conclude the
effect is causal. After all, subjects only have x-rays when something is wrong, so it is
quite possible that the x-rays are linked to some unknown causal factor.

Other examples of matched data may be found in Section 4.3.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 58" -->

Further Reading: See books by Collett (2003), Hosmer and Lemeshow (2000), Cox
(1970), Harrell (2001), Menard (2002), Christensen (1997) and Kleinbaum and Klein
(2002).


### Exercises

1\. The question concerns data from a case-control study of esophageal cancer in Ileet-
Vilaine, France. The data is distributed with $\mathrm { R }$ and may be obtained along with a
description of the variables by:

$$> \mathrm { d a t a } \left( \mathrm { e s o p h } \right)$$

\> help (esoph)

(a) Fit a binomial GLM with interactions between all three predictors. Use backward
elimination to simplify the model as far as is reasonable.

(b) All three factors are ordered and so special contrasts have been used appropriate
for ordered factors involving linear, quadratic and cubic terms. Further
simplification of the model is possible by eliminating some of these terms. Use the
unclass function to convert some or all factors to a numerical representation and
show how the model may be simplified.

(c) Does your final model fit the data? Is the test you make accurate for this data?

(d) Check for outliers in your final model.

(e) What is the predicted effect of moving one category higher in alcohol
consumption?

(f) Compute a 95% confidence interval for this predicted effect.

(g) Bearing in mind that this is a case-control study, what can be said about the
predicted probability that a 25-year-old who does not smoke or drink will get
esophageal cancer?

2\. The dataset wbcd comes from a study of breast cancer in Wisconsin. There are 681
cases of potentially cancerous tumors of which 238 are actually malignant.
Determining whether a tumor is really malignant is traditionally determined by an
invasive surgical procedure. The purpose of this study was to determine whether a
new procedure called fine needle aspiration, which draws only a small sample of
tissue, could be effective in determining tumor status.

(a) Fit a binomial regression with Class as the response and the other nine variables as
predictors. Report the residual deviance and associated degrees of freedom. Can
this information be used to determine if this model fits the data? Explain.

(b) Use AIC as the criterion to determine the best subset of variables. (Use the step
function.)

(c) Use the reduced model to predict the outcome for a new patient with predictor
variables 1, 1, 3, 2, 1, 1, 4, 1, 1 (same order as above). Give a confidence interval
for your prediction.

<!-- PageBreak -->

<!-- PageHeader="Binomial data 59" -->

(d) Suppose that a cancer is classified as benign if $p > 0 . 5$ and malignant if $p < 0 . 5 .$
Compute the number of errors of both types that will be made if this method is
applied to the current data with the reduced model.

(e) Suppose we change the cutoff to 0.9 so that $p < 0 . 9$ is classified as malignant and
$p > 0 . 9$ as benign. Compute the number of errors in this case. Discuss the issues in
determining the cutoff.

(f) It is usually misleading to use the same data to fit a model and test its predictive
ability. To investigate this, split the data into two parts-assign every third
observation to a test set and the remaining two thirds of the data to a training set.
Use the training set to determine the model and the test set to assess its predictive
performance. Compare the outcome to the previously obtained results.

3\. The National Institute of Diabetes and Digestive and Kidney Diseases conducted a
study on 768 adult female Pima Indians living near Phoenix. The purpose of the study
was to investigate factors related to diabetes. The data may be found in the the dataset
pima.

(a) Perform simple graphical and numerical summaries of the data. Can you find any
obvious irregularities in the data? If you do, take appropriate steps to correct the
problems.

(b) Fit a model with the result of the diabetes test as the response and all the other
variables as predictors. Can you tell whether this model fits the data?

(c) What is the difference in the odds of testing positive for diabetes for a woman with
a BMI at the first quartile compared with a woman at the third quartile, assuming
that all other factors are held constant? Give a confidence interval for this
difference.

(d) Do women who test positive have higher diastolic blood pressures? Is the diastolic
blood pressure significant in the regression model? Explain the distinction between
the two questions and discuss why the answers are only apparently contradictory.

(e) Perform diagnostics on the regression model, reporting any potential violations and
any suggested improvements to the model.

(f) Predict the outcome for a woman with predictor values 1, 99, 64, 22, 76, 27, 0.25,
25 (same order as in the dataset). Give a confidence interval for your prediction.

4\. Aflatoxin B1 was fed to lab animals at various doses and the number responding with
liver cancer recorded. The data may be found in the dataset af latoxin.

(a) Build a model to predict the occurrence of liver cancer. Compute the ED50 level.

(b) Discuss the extrapolation properties of your chosen model for low doses.

5\. A study was conducted to determine the effectiveness of a new teaching method in
economics. The data may be found in the dataset spector. Write a report on how well
the new method works.

6\. Incubation temperature can affect the sex of turtles. An experiment was conducted
with three independent replicates for each temperature and the number of male and
female turtles born was recorded and can be found in the turtle dataset. Check for
evidence of overdispersion in a binomial model for the sex of the turtle.

<!-- PageBreak -->


## Extending the linear model with $R$ 60

7\. The infert dataset from the survival package presents data from a study of infertility
after spontaneous and induced abortion. Analyze and report on the factors related to
infertility based on this data.

<!-- PageBreak -->


## CHAPTER 3 Count Regression

When the response is a count (a positive integer), we can use a count regression model to
explain this response in terms of the given predictors. Sometimes, the total count is
bounded, in which case a binomial response regression should probably be used. In other
cases, the counts might be sufficiently large that a normal approximation is justified so
that a normal linear model may be used. We shall consider two distributions for counts.
The Poisson and, less commonly, the negative binomial.


### 3.1 Poisson Regression

If $Y$ is Poisson with mean $\mu > 0 ,$ then:

$$P \left( Y = y \right) = \frac { e ^ { 4 } \mu ^ { y } } { y ! } , \quad y = 0 , 1 , 2 , \ldots ,$$

Now EY=var $Y = \mu .$ The Poisson distribution arises naturally in several ways:

1\. If the count is some number out of some possible total, then the response would be
more appropriately modeled as a binomial. However, for small success probabilities
and large totals, the Poisson is a good approximation and can be applied. For example,
in modeling the incidence of rare forms of cancer, the number of people affected is a
small proportion of the population in a given geographical area. A Poisson regression
model can be used in preference to a binomial. If $\mu = n p$ while $n \rightarrow \infty ,$ then $B \left( n , p \right)$ is
well approximated by Pois(u). Also, for small $p ,$ note that $\mathrm { l o g i t } \left( p \right) \approx \log p ,$ so that the
use of the Poisson with a log link is comparable to the binomial with a logit link.

2\. Suppose the probability of occurrence of an event in a given time interval is
proportional to the length of that time interval and independent of the occurrence of
other events. Then the number of events in any specified time interval will be Poisson
distributed. Examples include modeling the number of incoming telephone calls to a
service center or the number of earthquakes. However, in any real application, the
assumptions are likely to be violated. For example, the rate of incoming telephone
calls is likely to vary with the time of day while the timing of earthquakes are unlikely
to be completely independent. Nevertheless, a good approximation may be sufficient.

3\. Poisson distributions also arise naturally when the time between events is independent
and identically exponentially distributed. We count the number of events in a given
time period. This is effectively equivalent to the previous case, since the exponential
distribution between events will result from the assumption of constant and
independent probability of occurrence of an event in an interval.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 62" -->

If the count is the number falling into some level of a given category, then a multinomial
response model or categorical data analysis should be used. For example, if we have
counts of how many people have type O, A, B or AB blood and are interested in how that
relates to race and gender, then a straight Poisson regression model will not be
appropriate. We will see later that the Poisson distribution still comes into play in
Chapter 5.

An important result concerning Poisson random variables is that their sum is also
Poisson. Specifically, suppose that $Y i \sim P o i s \left( \mu _ { i } \right)$ for $i = 1 ,$ $2 , \ldots .$ and are independent, then
$\Sigma _ { i } \mathrm { Y } _ { i } \sim P o i s \left( \Sigma _ { i } \mu _ { i } \right) .$ This is useful because sometimes we have access only to the aggregated
data. If we assume the individual-level data is Poisson, then so is the summed data and
Poisson regression can still be applied.

For 30 Galápagos Islands, we have a count of the number of species of tortoise found
on each island and the number that are endemic to that island. We also have five
geographic variables for each island. The data was presented by Johnson and Raven
(1973) and also appear in Weisberg (2005). We have filled in a few missing values that
appeared in the original dataset for simplicity. We model the number of species using
normal linear regression:

$$\begin{array}{} { > \text { data } \left( g a l a \right) } \\ { > g a l a < - g a l a r . - 2 1 } \end{array}$$

We throw out the Endemics variable (which falls in the second column of the dataframe)
since we won't be using it in this analysis. We fit a linear regression and look at the
residual vs. fitted plot:

\> modl <- 1m (Species ~ . , gala)
>

plot (predict (modl) , residuals (modl) , xlab="Fitted", ylab="
Residuals")


<figure>
<figcaption>Figure 3.1 Residual-fitted plots for the Galápagos dataset. The plot on the left is for a model with the original</figcaption>

Residuals

100

50

Residuals

2

00

00

-100

₩

0

0

100

200

300 400

5

10

15

20

Fitted

Fitted

</figure>


<!-- PageBreak -->

<!-- PageNumber="63" -->
<!-- PageHeader="Count regression" -->


## response while that on the right is for the square-root transformed response.

We see clear evidence of nonconstant variance in left panel of Figure 3.1. Some
experimentation (or the use of the Box-Cox method) reveals that a square-root
transformation is best:

$$> \mathrm { m o d t } < - 1 m \left( \mathrm { s q r t } \left( \mathrm { S p e c i e s } \right) \sim . , \mathrm { g a l a } \right)$$

\>

plot (predict (modt) , residuals (modt) , xlab="Fitted", ylab="
Residuals")

We now see in the right panel of Figure 3.1 that the nonconstant variance problem has
been cleared up. Let's take a look at the fit:

\> summary (modt)

Coefficients :


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>3.391924</td>
<td>0.871268</td>
<td>3.89</td>
<td>0.00069</td>
</tr>
<tr>
<td>Area</td>
<td>-0.001972</td>
<td>0.001020</td>
<td>-1.93</td>
<td>0.06508</td>
</tr>
<tr>
<td>Elevation</td>
<td>0.016478</td>
<td>0.002441</td>
<td>6.75</td>
<td>5.5e-07</td>
</tr>
<tr>
<td>Nearest</td>
<td>0.024933</td>
<td>0.047950</td>
<td>0.52</td>
<td>0.60784</td>
</tr>
<tr>
<td>Scruz</td>
<td>-0.013483</td>
<td>0.009798</td>
<td>-1.38</td>
<td>0.18151</td>
</tr>
<tr>
<td>Adjacent</td>
<td>-0.003367</td>
<td>0.000805</td>
<td>-4.18</td>
<td>0.00033</td>
</tr>
</table>


Residual standard error: 2.77 on 24 degrees of freedom
Multiple R-Squared: 0.783,
Adjusted R-squared:
0.737
F-statistic: 17.3 on 5 and 24 degrees of $\mathrm { f r e e d o m } ,$ $p -$
$\mathrm { v a l u e } :$ 2.87e-07

We see a fairly good fit $\left( R ^ { 2 } = 0 . 7 8 \right)$ considering the nature of the variables. However, we
achieved this fit at the cost of transforming the response. This makes interpretation more
difficult. Furthermore, some of the response values are quite small (single digits) which
makes us question the validity of the normal approximation. This model may be
adequate, but perhaps we can do better. We develop a Poisson regression model:

Suppose we have count responses $Y _ { i }$ that we wish to model in terms of $\mathrm { a }$ vector of
predictors $X _ { i } .$ Now if $Y _ { i } \sim P o i s \left( \mu _ { i } \right) ,$ we need some way to link the $\mu _ { i }$ to the $x _ { i } .$ We use a
linear combination of the $x _ { i }$ to form the linear predictor $\eta _ { i } = x _ { i } ^ { r }$ P.Since we require that
$\mu _ { t } \geq 0 ,$ we can ensure this by using a log link function, that is:

$$\log \mu _ { i } = \eta _ { i } = x _ { i } ^ { T } \beta$$

So, as with the binomial regression models of the previous chapter, this models also has a
linear predictor and a link function.

Now, the log-likelihood is:

$$I \left( \beta \right) = \sum _ { i = 1 } ^ { n } \left( y _ { i } x _ { i } ^ { T } \beta - e x p \left( x _ { i } ^ { T } \beta \right) - \log y _ { i } ! \right)$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 64" -->

Differentiating with respect to $\beta$ gives the MLE as the solution to:

$$\sum _ { i = 1 } ^ { n } \left( y _ { i } - \exp \left( x _ { i } ^ { T } \beta \right) \right) x _ { j } = 0 \quad \forall j$$

which can be more compactly written as:

$$X ^ { T } y = X ^ { T }$$

The normal equations for the least squares estimate of $\beta$ in normal linear models take the
same form when we set $\widehat { \mu } = X \widehat { \beta }$ equations for $\beta$ for a binomial regression with a
logit link also take the same form. This would not be true for other link functions. The
link function having this property is known as the canonical link.

However, there is no explicit formula for $\dot { \beta } _ { \mathrm { f o r } }$ the Poisson (or binomial) regression
and we must resort to numerical methods to find a solution. We fit the Poisson regression
model to the Galápagos data:

\> modp <- glm (Species ~ . , family=poisson, gala)
> summary (modp)
Deviance Residuals:


<table>
<tr>
<th>Min</th>
<th>1Q</th>
<th>Median</th>
<th>3Q</th>
<th>Max</th>
</tr>
<tr>
<td>-8.275</td>
<td>-4.497</td>
<td>-0.944</td>
<td>1.917</td>
<td>10.185</td>
</tr>
</table>


Coefficients :


<table>
<tr>
<th></th>
<th colspan="2">Estimate Std. Error z</th>
<th>value Pr (&gt; | z | )</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>$3 . 1 5 4 8 0 7 9$</td>
<td>0.0517495</td>
<td>60.96 &lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>Area</td>
<td>-0.0005799</td>
<td>$0 . 0 0 0 0 2 6 3$</td>
<td>-22.07 &lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>Elevation</td>
<td colspan="2">0.0035406 0.0000874</td>
<td>40.51 &lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>Nearest</td>
<td>0.0088256</td>
<td>0.0018213</td>
<td>4.85 0.0000013</td>
</tr>
<tr>
<td>Scruz</td>
<td>-0.0057094</td>
<td>0.0006256</td>
<td>-9.13 &lt; 2e-16</td>
</tr>
<tr>
<td>Adjacent</td>
<td>-0.0006630</td>
<td>0.0000293</td>
<td>-22.61 &lt; 2e-16</td>
</tr>
</table>


(Dispersion parameter for poisson family taken to be 1)
Null deviance: 3510.73 on 29 degrees of freedom
Residual deviance: 716.85 on 24 degrees of freedom
AIC: 889.7

Number of Fisher Scoring iterations: 5

Using the same arguments as for binomial regression, we develop a deviance for the
Poisson regression:

$$D = 2 \sum _ { i = 1 } ^ { n } \left( y _ { i } \log \left( y _ { i } / \widehat { \mu } _ { i } \right) - \left( y _ { i } - \widehat { \mu } _ { i } \right) \right)$$

This Poisson deviance is also known as the G-statistic.

The same asymptotic inference may be employed as for the binomial model. We can
judge the goodness of fit of a proposed model by checking the deviance of the model
against a $x ^ { 2 }$ distribution with degrees of freedom equal to that of the model. We can
compare nested models by taking the difference of the deviances and comparing to a $x ^ { 2 }$
distribution with degrees of freedom equal to the difference in the number of parameters
for the two models. We can test the significance of individual predictors and construct

<!-- PageBreak -->

<!-- PageNumber="65" -->
<!-- PageHeader="Count regression" -->

confidence intervals for $\beta$ using the standard errors, $s e \left( \dot { \beta } \right) ,$ although, as before, it is better
to use profile likelihood methods.

An alternative and perhaps better-known goodness of fit measure is the Pearson's $X ^ { 2 }$
statistic:

$$X ^ { 2 } = \sum _ { i = 1 } ^ { n } \frac { \left( y _ { i } - \widehat { \mu } _ { i } \right) ^ { 2 } } { \widehat { \mu } _ { i } }$$

In this example, we see that the residual deviance is 717 on 24 degrees of freedom which
indicates an ill-fitting model if the Poisson is the correct model for the response. We
check the residuals to see if the large deviance can be explained by an outlier:

\> halfnorm (residuals (modp) )


<figure>
<figcaption>Figure 3.2 Half-normal plot of the residuals of the Poisson model is shown on the left and the relationship between the mean and variance is shown on the right. A line representing mean equal to variance is also shown.</figcaption>

10

11

10

27

0

Sorted Data

(y-6)2

0

4

2

2

0

0

0

0

0

0.0

0.5

1.0

1.5

2.0

2.5

3.5

4.5

5.5

Half-normal quantiles

$\underline { { \mu } }$

</figure>


The half-normal plot of the residuals shown in Figure 3.2 shows no outliers. It could be
that the structural form of the model needs some improvement, but some experimentation
with different forms for the predictors will reveal that there is little scope for
improvement. Furthermore, the proportion of deviance explained by this model, 1-
$7 1 7 / 3 5 1 0 = 0 . 7 9 6 ,$ is about the same as in the linear model above.

For a Poisson distribution, the mean is equal to the variance. Let's investigate this
relationship for this model. It is difficult to estimate the variance for a given value of the
mean, but $\left( y - i \right) ^ { 2 }$ does serve as a crude approximation. We plot this estimated variance
against the mean, as seen in the second panel of Figure 3.2:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 66" -->

\> plot (log (fitted (modp) ) , log ( (gala$Species-
fitted (modp) )^2),
xlab=expression (hat (mu) ) , ylab=expression ( (y-
hat (mu) )^2))
> abline $\left( 0 , 1 \right)$

We see that the variance is proportional to, but larger than, the mean. When the variance
assumption of the Poisson regression model is broken but the link function and choice of
predictors is correct, the estimates of $\beta$ are consistent, but the standard errors will be
wrong. We cannot determine which predictors are statistically significant in the above
model using the output we have.

The Poisson distribution has only one parameter and so is not very flexible for
empirical fitting purposes. We can generalize by allowing ourselves a dispersion
parameter. Over- or underdispersion can occur in Poisson models. For example, suppose
the Poisson response $Y$ has rate $\lambda$ which is itself a random variable. The tendency to fail
for a machine may vary from unit to unit even though they are the same model. We can
model this by letting $\lambda$ be gamma distributed with $E \hbar = \mu$ and var $A = \mu / \phi$ $Y$ is
negative binomial with mean $E Y = \mu .$ The mean is the same as the Poisson, but the
variance var
$Y = \mu \left( 1 + \phi \right) / \phi _ { \text { which } }$ is not equal to $\mu .$ In this case, overdispersion would
occur.

If we know the specific mechanism, as in the above example, we could model the
response as a negative binomial or other more flexible distribution. If the mechanism is
not known, we can introduce a dispersion parameter @such that var $Y = \phi E Y = \phi \mu .$
$\phi = 1 _ { i s }$ the regular Poisson regression case, while $\phi > 1 _ { \text { is } }$ overdispersion and $\phi < 1 _ { \text { is } }$
underdispersion.

The dispersion parameter may be estimated using:

$$\ddot { \phi } = \frac { X ^ { 2 } } { n - p } = \frac { \sum \left( y _ { i } - \widehat { p } _ { i } \right) ^ { 2 } / \widehat { B } _ { i } } { n - p }$$

We estimate the dispersion parameter in our example by:

$$\left. \left( r e s i d u a l s \left( m o d p , t y p e = ^ { \prime \prime } p e a r s o n ^ { \prime \prime } \right) ^ { \wedge } 2 \right) / n o d p s d f . r e s \right)$$
[1] 31.749

We can then adjust the standard errors and so forth in the summary as follows:

\> summary (modp, dispersion=dp)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>z value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>3.154808</td>
<td></td>
<td>0.291590</td>
<td>10.82</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>Area</td>
<td>-0.000580</td>
<td></td>
<td>0.000148</td>
<td>-3.92</td>
<td>8.9e-05</td>
</tr>
<tr>
<td>Elevation</td>
<td>0.003541</td>
<td></td>
<td>0.000493</td>
<td>7.19</td>
<td>6.5e-13</td>
</tr>
<tr>
<td>Nearest</td>
<td>0.008826</td>
<td></td>
<td>0.010262</td>
<td>0.86</td>
<td>0.39</td>
</tr>
<tr>
<td>Scruz</td>
<td>-0.005709</td>
<td></td>
<td>0.003525</td>
<td>-1.62</td>
<td>0.11</td>
</tr>
<tr>
<td>Adjacent</td>
<td>-0.000663</td>
<td></td>
<td>0.000165</td>
<td>-4.01</td>
<td>6.0e-05</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Count regression 67" -->


<table>
<tr>
<th>(Dispersion parameter</th>
<th>for</th>
<th>poisson</th>
<th></th>
<th>family taken</th>
<th>to be</th>
</tr>
<tr>
<td>31.749)</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>Null deviance: 3510.73</td>
<td></td>
<td>on</td>
<td>29</td>
<td colspan="2">degrees of freedom</td>
</tr>
<tr>
<td>Residual deviance: 716.85</td>
<td></td>
<td>on</td>
<td>24</td>
<td>degrees of</td>
<td>freedom</td>
</tr>
<tr>
<td>AIC: 889.7</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</table>


Notice that the estimation of the dispersion and the regression parameters is independent,
so choosing a dispersion other than one has no effect on the regression parameter
estimates. Notice also that there is some similarity in which variables are picked out as
significant and which not when compared with the linear regression model.

When comparing Poisson models with overdispersion, an F-test rather than a $x ^ { 2 }$ test
should be used. As in normal linear models, the variance, or dispersion parameter in this
case, needs to be estimated. This requires the use of the F-test. So to test the significance
of each of the predictors relative to the full model, use:

\> dropl (modp, test="F")
Single term deletions
Model:


<table>
<tr>
<th>Species ~</th>
<th>Area Df</th>
<th>+ Elevation Deviance</th>
<th>AIC</th>
<th colspan="2">+ Nearest + Scruz + Adjacent F value $\mathbb{P} _ { \Sigma } \left( E \right)$</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td></td>
<td>717</td>
<td>890</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Area</td>
<td>1</td>
<td>1204</td>
<td>1375</td>
<td>16.32</td>
<td>0.00048</td>
</tr>
<tr>
<td>Elevation</td>
<td>1</td>
<td>2390</td>
<td>2560</td>
<td>56.00</td>
<td>1e-07</td>
</tr>
<tr>
<td>Nearest</td>
<td>1</td>
<td>739</td>
<td>910</td>
<td colspan="2">0.76 0.39336</td>
</tr>
<tr>
<td>Scruz</td>
<td>1</td>
<td>814</td>
<td>984</td>
<td colspan="2">3.24 $0 . 0 8 4 4 4$</td>
</tr>
<tr>
<td>Adjacent</td>
<td>1</td>
<td>1341</td>
<td>1512</td>
<td colspan="2">20.91 0.00012</td>
</tr>
</table>

Warning message:

F test assumes quasipoisson family in: dropl. glm (modp,
$\left. \mathrm { t e s t } = { } ^ { \mathrm { \prime \prime } } \mathrm { F } ^ { \mathrm { \prime \prime } } \right)$


The z-statistics from the summary () are less reliable and so the F-test is preferred. In this
example, there is little practical difference between the two.


### 3.2 Rate Models

The number of events observed may depend on a size variable that determines the
number of opportunities for the events to occur. For example, if we record the number of
burglaries reported in different cities, the observed number will depend on the number of
households in these cities. In other cases, the size variable may be time. For example, if
we record the number of customers served by a sales worker, we must take account of the
differing amounts of time worked.

Sometimes, it is possible to analyze such data using a binomial response model. For
the burglary example above, we might model the number of burglaries out of the number
of households. However, if the proportional is small, the Poisson approximation to the
binomial is effective. Furthermore, in some examples, the total number of potential cases
may not be known exactly. The modeling of rare diseases illustrates this issue as we may
know the number of cases but not have precise population data. Sometimes, the binomial

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 68" -->

model simply cannot be used. In the burglary example, some households may be affected
more than once. In the customer service example, the size variable is not a count. An
alternative approach is to model the ratio. However, there are often difficulties with
normality and unequal variance when taking this approach, particularly if the counts are
small.

In Purott and Reeder (1976), some data is presented from an experiment conducted to
determine the effect of gamma radiation on the numbers of chromosomal abnormalities
(ca) observed. The number (cells), in hundreds of cells exposed in each run, differs. The
dose amount (doseamt) and the rate (doserate) at which the dose is applied are the
predictors of interest. We may format the data for observation like this:

\> data (dicentric)
> round (xtabs (ca/cells ~ doseamt+doserate,
dicentric) , 2)
doserate

doseamt
0.1
0.25

0.5
1
1.5

2
2.5

3

4

1

0.05
0.05

0.07

0.07

0.06
06 0.
0.07

.07

0.07
0
0.07

2.5 0.16 0.28 0.29 0.32 0.38 0.41 0.41 0.37 0.44
5 0.48 0.82 0.90 0.88 1.23 1.32 1.34 1.24 1.43

We can plot the data as seen in the first panel of Figure 3.3:

\>
with (dicentric, interaction. plot (doseamt, doserate, ca/cel
ls) )

We might try modeling the rate directly. We see that the effect of the dose rate may be
multiplicative, so we log this variable in the following model:


<figure>
<figcaption>Figure 3.3 Chromosomal abnormalities rate response is shown on the left and a residuals vs. fitted plot of a linear model fit to these data is shown on the right.</figcaption>

doserate

0

\+

0

1.2

0.05

.

0

2.5

0

19

0

2

0

0.8

J

Residuals

0

0

1.5

0.05

0

0

5

1

10

0

0

0\.

-0.15

0.0

¢

\#

2.5

5

0.0

04

0.0

1.2

Finod

dosamt

</figure>


<!-- PageBreak -->

<!-- PageHeader="Count regression 69" -->

\> lmod <- lm(ca/cells ~ log(doserate)*factor(doseamt),
dicentric)
> summary(lmod)$adj
[1] 0.98444

As can be seen from the adjusted $R ^ { 2 } ,$ this model fits well. However, a look at the
diagnostics reveals a problem, as seen in the second panel of Figure 3.3:

\> plot(residuals(lmod) ~
fitted(lmod),xlab="Fitted",ylab="Residuals")
> abline (h=0)

We might prefer an approach that directly models the count response. We need to use the
log of the number of cells because we expect this to have a multiplicative effect on the
response:

\> dicentric$dosef <- factor (dicentric$doseamt)
> pmod <- glm(ca ~ log (cells) +log (doserate) *dosef,
family=poisson, dicentric)
> summary (pmod)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
<th></th>
</tr>
<tr>
<td rowspan="2">$\mathrm { P r } \left( > | z | \right)$ (Intercept)</td>
<td rowspan="2">-2.7653</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>0.3812</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>7.25 $4 e - 1 3$</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\log \left( \mathrm { c e l l s } \right)$</td>
<td>1.0025</td>
<td>0.0514</td>
<td>19.52</td>
<td>&lt;2</td>
</tr>
<tr>
<td>$e - 1 6$</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>log (doserate)</td>
<td rowspan="2">0.0720</td>
<td rowspan="2">0.0355</td>
<td rowspan="2">2.03</td>
<td rowspan="2">0.0</td>
</tr>
<tr>
<td>4240</td>
</tr>
<tr>
<td>$\mathrm { d o s e f 2 } . 5$</td>
<td>1.6298</td>
<td>0.1027</td>
<td>15.87</td>
<td>&lt;2</td>
</tr>
<tr>
<td>e-16</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\mathrm { d o s e f } 5$</td>
<td>2.7667</td>
<td>0.1229</td>
<td>22.52</td>
<td>&lt;2</td>
</tr>
<tr>
<td>e-16</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>log (doserate) :dosef2.5 0087</td>
<td>0.1611</td>
<td>0.0484</td>
<td>3.33</td>
<td>0.0</td>
</tr>
<tr>
<td>log (doserate) : dosef5</td>
<td>0.1932</td>
<td>0.0430</td>
<td>4.49</td>
<td>7</td>
</tr>
</table>


e-06
(Dispersion parameter for poisson family taken to be 1)
Null deviance: 916.127 on 26 degrees of freedom
Residual deviance: 21.748 on 20 degrees of freedom
AIC: 211.2

We can relate this Poisson model with a log link back to a linear model for the ratio
response:

$$\log \left( \mathrm { c a / c e l l s } \right) = \mathrm { X \beta }$$

This can be rearranged as

$\log c a = \log c e l l s + X \beta$

<!-- PageBreak -->


## Extending the linear model with R 70

We are using log cells as a predictor. Checking above, we can see that the coefficient of
1.0025 is very close to one. This suggests fitting a model with the coefficient fixed as
one. In this manner, we are modeling the rate of chromosomal abnormalities while still
maintaining the count response for the Poisson model. This is known as a rate model. We
fix the coefficient as one by using an offset. Such a term on the predictor side of the
model equation has no parameter attached:

\> rmod <- glm(ca ~ offset
(log (cells) ) +log (doserate) *dosef,
family=poisson, dicentric)
> summary (rmod)
Coefficients:


<table>
<tr>
<th colspan="2">Estimate Std.</th>
<th>Error</th>
<th>z</th>
</tr>
<tr>
<td colspan="2">value $P r \left( > | z | \right)$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>(Intercept)</td>
<td>-2.7467</td>
<td>0.0343</td>
<td>-</td>
</tr>
<tr>
<td>80.16 $< 2 e - 1 6$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>log (doserate) 0.04130</td>
<td>0.0718</td>
<td>0.0352</td>
<td>2.04</td>
</tr>
<tr>
<td colspan="2">dosef2.5 1.6254 &lt; 2e-16</td>
<td>0.0495</td>
<td>32.86</td>
</tr>
<tr>
<td>dosef5 &lt; 2e-16</td>
<td>2.7611</td>
<td>0.0435</td>
<td>63.49</td>
</tr>
<tr>
<td>log (doserate) : dosef2.5 0.00084</td>
<td>0.1612</td>
<td>0.0483</td>
<td>3.34</td>
</tr>
<tr>
<td>log (doserate) : dosef5</td>
<td>0.1935</td>
<td>0.0424</td>
<td>4.56</td>
</tr>
</table>

(Dispersion parameter for poisson family taken to be 1)
Null deviance:
4753.00
on 26 degrees of freedom


0.0000051

Residual deviance:
21.75
2
on 21 degrees of freedom
AIC: 209.2

Not surprisingly, the coefficients are only slightly different from the previous model. We
see from the residual deviance that the model fits well. Previous analyses have posited a
quadratic effect in dose; indeed, the observed coefficients speak against a purely linear
effect. However, given that we have only three dose levels, we can hardly check whether
quadratic is appropriate. Given the significant interaction effect, we can see that the effect
of the dose rate is different depending on the overall dose. We can see that the
combination of a high dose, delivered quickly, has a greater combined effect than the
main effect estimates would suggest. More on the analysis of this data may be found in
Frome and DuFrain (1986).


### 3.3 Negative Binomial

Given a series of independent trials, each with probability of success $p ,$ let $\mathrm { Z }$ be the
number of trials until the $k ^ { t h }$ success. Then:

$$P \left( Z = z \right) = \left( \begin{array}{} { z - 1 } \\ { k - 1 } \end{array} \right) p ^ { k } \left( 1 - p \right) ^ { z - k } \quad z = k , k + 1 , \ldots$$

<!-- PageBreak -->

<!-- PageNumber="71" -->
<!-- PageHeader="Count regression" -->

The negative binomial can arise naturally in several ways. One can envision a system that
can withstand $k$ hits. The probability of a hit in a given time period is $p .$ The negative
binomial also arises from the generalization of the Poisson where the parameter $2$ is
gamma distributed. The negative binomial also comes up as a limiting distribution for urn
schemes that can be used to model contagion.

We get a more convenient parameterization if we let $\mathrm { Y } = Z - k$ and $p = \left( 1 + \alpha \right) ^ { - 1 }$ so that:

$$P \left( Y = y \right) = \left( \begin{array}{} { y + k - 1 } \\ { k - 1 } \end{array} \right) \frac { \alpha ^ { y } } { \left( 1 + \alpha \right) ^ { y + k } } , \quad y = 0 , 1 , 2 , \ldots .$$

then $E Y = \mu = k 0$ and var $Y = k \alpha + k \alpha ^ { 2 } = \mu + \mu ^ { 2 } / k .$

The log-likelihood is then:

$$\sum _ { i = 1 } ^ { n } \left( y _ { i } \log \frac { \alpha } { 1 + \alpha } - k \log \left( 1 + \alpha \right) + \sum _ { j = 0 } ^ { y _ { - 1 } } \log \left( j + k \right) - \log y _ { i } ! \right)$$

The most convenient way to link the mean response $\mu$ to a linear combination of the
predictors $X$ is:

$$\pi = x ^ { T } \beta = \log \frac { \alpha } { 1 + \alpha } = \log \frac { \mu } { \mu + k }$$

We can regard $k$ as fixed and determined by the application or as an additional parameter
to be estimated. More on regression models for negative binomial responses may found
in Cameron and Trivedi (1998) and Lawless (1987).

Consider this example. ATT ran an experiment varying five factors relevant to a
wave-soldering procedure for mounting components on printed circuit boards. The
response variable, skips, is a count of how many solder skips appeared to a visual
inspection. The data comes from Comizzoli, Landwehr, and Sinclair (1990). We start
with a Poisson regression:

\> data (solder)
> modp <- glm (skips ~ . , family=poisson, data=solder)
> deviance (modp)
[1] 1829
> df.residual (modp)
[1] 882

We see that the full model has a residual deviance of 1829 on 882 degrees of freedom.
This is not a good fit. Perhaps including interaction terms will improve the fit:

\> modp2 <- glm(skips ~ (Opening +Solder + Mask +
PadType + Panel) ^2 ,
family=poisson, data=solder)
> deviance (modp2)
[1] 1068.8
>
pchisq (deviance (modp2) , df.residual (modp2) , lower=FALSE)

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 72" -->

[1] 1.1307e-10

The fit is improved but not enough to conclude that the model fits. We could try adding
more interactions but that would make interpretation increasingly difficult. $A$ check for
outliers reveals no problem.

An alternative model for counts is the negative binomial. The functions for fitting
come from the MASS package-see Venables and Ripley (2002) for more details. We
can specify the link parameter $k .$ Here we choose $k = 1$ to demonstrate the method,
although there is no substantive motivation from this application to use this value:

\> library (MASS)
> modn <- glm (skips ~ . , negative. binomial (1) , solder)
> modn
Coefficients:


<table>
<tr>
<th>(Intercept) MaskA3</th>
<th>OpeningM</th>
<th colspan="3">Openings</th>
<th>SolderThin</th>
</tr>
<tr>
<td>-</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>1.6993</td>
<td>0.5085</td>
<td colspan="3">1.9997</td>
<td>1.0489</td>
</tr>
<tr>
<td>. 6571</td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr>
<td>MaskA6</td>
<td>MaskB3</td>
<td></td>
<td colspan="2">MaskB6</td>
<td>PadTypeD6</td>
</tr>
<tr>
<td>PadTypeD7</td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr>
<td>2.5265</td>
<td>1.2726</td>
<td></td>
<td colspan="2">2.0803</td>
<td>-</td>
</tr>
<tr>
<td>0.4612</td>
<td>0.0161</td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>PadTypeL4</td>
<td>PadTypeL6</td>
<td></td>
<td colspan="2">PadTypeL7</td>
<td>PadTypeL8</td>
</tr>
<tr>
<td>PadTypeL9</td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr>
<td>0.4688</td>
<td>-0.4711</td>
<td></td>
<td colspan="2">-0.2949</td>
<td>-</td>
</tr>
<tr>
<td>0.0849</td>
<td>-0.5213</td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>PadTypeW4</td>
<td>PadTypeW9</td>
<td></td>
<td colspan="2">Panel</td>
<td></td>
</tr>
<tr>
<td>-0.1425</td>
<td>-1.4836</td>
<td></td>
<td></td>
<td>0.1693</td>
<td></td>
</tr>
<tr>
<td>Degrees of</td>
<td>Freedom: 899</td>
<td colspan="4">Total (i.e. Null) ; 882</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Null Deviance: 1740</td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td colspan="2">Residual Deviance: 559</td>
<td colspan="3">AIC: 3880</td>
<td></td>
</tr>
</table>


0

We could experiment with different values of $k ,$ but there is a more direct way of
achieving this by allowing the parameter $k$ to vary and be estimated using maximum
likelihood in:

\> modn <- glm.nb (skips ~ . , solder)
> summary (modn)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-1.4225</td>
<td>0.1427</td>
<td>-9.97</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>OpeningM</td>
<td>0.5029</td>
<td>0.0798</td>
<td>6.31</td>
<td>$2 . 9 e - 1 0$</td>
</tr>
<tr>
<td>Openings</td>
<td>1.9132</td>
<td>0.0715</td>
<td>26.75</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>$\mathrm { S o l d e r T h i r }$</td>
<td>0.9393</td>
<td>0.0536</td>
<td>17.52</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>MaskA3</td>
<td>0.5898</td>
<td>0.0965</td>
<td>6.11</td>
<td>$9 . 9 e - 1 0$</td>
</tr>
<tr>
<td>MaskA6</td>
<td>2.2673</td>
<td>0.1018</td>
<td>22.27</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>MaskB3</td>
<td>1.2110</td>
<td>0.0964</td>
<td>12.57</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>MaskB6</td>
<td>1.9904</td>
<td>0.0922</td>
<td>21.58</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="73" -->
<!-- PageHeader="Count regression" -->


<table>
<tr>
<td>PadTypeD6</td>
<td>-0.4659</td>
<td>0.1124</td>
<td>-4.15</td>
<td>$3 . 4 e - 0 5$</td>
</tr>
<tr>
<td>PadTypeD7</td>
<td>-0.0331</td>
<td>0.1067</td>
<td>-0.31</td>
<td>0.75611</td>
</tr>
<tr>
<td>PadTypeL4</td>
<td>0.3827</td>
<td>0.1026</td>
<td>3.73</td>
<td>0.00019</td>
</tr>
<tr>
<td>PadTypeL6</td>
<td>-0.5784</td>
<td>0.1141</td>
<td>-5.07</td>
<td>4.0e-07</td>
</tr>
<tr>
<td>PadTypeL7</td>
<td>-0.3666</td>
<td>0.1109</td>
<td>-3.30</td>
<td>0.00095</td>
</tr>
<tr>
<td>PadTypeL8</td>
<td>-0.1589</td>
<td>0.1082</td>
<td>-1.47</td>
<td>0.14199</td>
</tr>
<tr>
<td>PadTypeL9</td>
<td>-0.5660</td>
<td>0.1139</td>
<td>-4.97</td>
<td>6.8e-07</td>
</tr>
<tr>
<td>PadTypeW4</td>
<td>-0.2004</td>
<td>0.1087</td>
<td>-1.84</td>
<td>0.06526</td>
</tr>
<tr>
<td></td>
<td>-1.5646</td>
<td>0.1362</td>
<td>-11.49</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>$P a n e l$</td>
<td>0.1637</td>
<td>0.0314</td>
<td>5.21</td>
<td>$1 . 8 e - 0 7$</td>
</tr>
</table>


(Dispersion parameter for Negative Binomial (4.3972)
family taken to be 1)

Null $\mathrm { d e v i a n c e } :$ $4 0 4 3 . 3$ on 899 degrees of freedom
Residual deviance: 1008.3 on 882 degrees of freedom
AIC: 3683

Number of $F i s h e r$ Scoring iterations: 1

Theta :
4.397
Std. Err .:
0.495
2 x log-likelihood: - 3645.309

We see that $k = 4 . 3 9 7 w i t h$ a standard error of 0.495. We can compare negative
binomial models using the usual inferential techniques.

Further Reading: See books by Cameron and Trivedi (1998) and Agresti (2002).


## Exercises

1\. The dataset discoveries lists the numbers of "great" inventions and scientific
discoveries in each year from 1860 to 1959. Has the discovery rate remained constant
over time?

2\. The salmonella data was collected in a salmonella reverse mutagenicity assay. The
predictor is the dose level of quinoline and the response is the numbers of revertant
colonies of TA98 salmonella observed on each of three replicate plates. Show that a
Poisson GLM is inadequate and that some overdispersion must be allowed for. Do not
forget to check out other reasons for a high deviance.

3\. The ships dataset found in the MASS package gives the number of damage incidents
and aggregate months of service for different types of ships broken down by year of
construction and period of operation. Develop a model for the rate of incidents,
describing the effect of the important predictors.

4\. The dataset af rica gives information about the number of military coups in subSaharan
Africa and various political and geographical information. Develop a simple but well-
fitting model for the number of coups. Give an interpretation of the effect of the
variables you include in your model on the response.

5\. The dvisits data comes from the Australian Health Survey of 1977-78 and consist of
5190 single adults where young and old have been oversampled.

(a) Build a Poisson regression model with doctorco as the response and sex, age,
agesq, income, levyplus, freepoor, freerepa, illness, actdays, hscore, chcond1 and

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 74" -->

chcond2 as possible predictor variables. Considering the deviance of this model,
does this model fit the data?

(b) Plot the residuals and the fitted values-why are there lines of observations on the
plot?

(c) Use backward elimination with a critical p-value of 5% to reduce the model as
much as possible. Report your model.

(d) What sort of person would be predicted to visit the doctor the most under your
selected model?

(e) For the last person in the dataset, compute the predicted probability distribution for
their visits to the doctor, i.e., give the probability they visit 0,1,2, etc. times.

(f) Fit a comparable (Gaussian) linear model and graphically compare the fits.
Describe how they differ.

6\. Components are attached to an electronic circuit card assembly by a wave-soldering
process. The soldering process involves baking and preheating the circuit card and
then passing it through a solder wave by conveyor. Defects arise during the process.
The design is $2 ^ { 7 - 3 }$ with three replicates. The data is presented in the dataset
wavesolder. Assuming that the replicates are independent, analyze the data. Write a
report on the analysis that summarizes the substantive conclusions and includes the
highlights of your analysis.

7\. The dataset esdcomp was recorded on 44 doctors working in an emergency service at a
hospital to study the factors affecting the number of complaints received. Build a
model for the number of complaints received and write a report on your conclusions.

<!-- PageBreak -->

<!-- PageBreak -->


## CHAPTER 4 Contingency Tables

A contingency table is used to show cross-classified categorical data on two or more
variables. The variables can be nominal or ordinal. A nominal variable has categories
with no natural ordering; for example, consider the automotive companies Ford, General
Motors and Toyota. An ordering could be imposed using some criterion like sales, but
there is nothing inherent in the categories that makes any particular ordering obvious. An
ordinal variable does have a natural default ordering. For example, a disease might be
recorded as absent, mild or severe. The five-point Likert scale ranging through strongly
disagree, disagree, neutral, agree and strongly agree is another example.

An interval scale is an ordinal variable that has categories with a distance measure.
This is often the result of continuous data that has been discretized into intervals. For
example, age groups 0-18, 18-34, 34-55 and 55+ might be used to record age
information. If the intervals are relatively wide, then methods for ordinal data can be used
where the additional information about the intervals may be useful in the modeling. If the
intervals are quite narrow, then we could replace interval response with the midpoint of
the interval and then use continuous data methods. One could argue that all so-called
continuous data is of this form, because such data cannot be measured with arbitrary
precision. Height might be given to the nearest centimeter, for example.


### 4.1 Two-by-Two Tables

The data shown in Table 4.1 were collected as part of a quality improvement study at a
semiconductor factory. A sample of wafers was drawn and cross-classified according to
whether a particle was found on the die that produced the wafer and whether the wafer
was good or bad. More details on the study may be found in Hall (1994). The data might
have arisen under several possible sampling schemes:


<table>
<caption>Table 4.1 Study of the relationship between wafer quality and the presence of particles on the wafer.</caption>
<tr>
<th>Quality</th>
<th>No Particles</th>
<th>Particles</th>
<th>Total</th>
</tr>
<tr>
<td>Good</td>
<td>320</td>
<td>14</td>
<td>334</td>
</tr>
<tr>
<td>Bad</td>
<td>80</td>
<td>36</td>
<td>116</td>
</tr>
<tr>
<td>Total</td>
<td>400</td>
<td>50</td>
<td>450</td>
</tr>
</table>


1\. We observed the manufacturing process for a certain period of time and observed 450
wafers. The data were then cross-classified. We could use a Poisson model.

<!-- PageBreak -->

<!-- PageNumber="77" -->
<!-- PageHeader="Contingency tables" -->

2\. We decided to sample 450 wafers. The data were then cross-classified. We could use a
multinomial model.

3\. We selected 400 wafers without particles and 50 wafers with particles and then
recorded the good or bad outcome. We could use a binomial model.

4\. We selected 400 wafers without particles and 50 wafers with particles that also
included, by design, 334 good wafers and 116 bad ones. We could use hypergeometric
model.

The first three sampling schemes are all plausible. The fourth scheme seems less likely in
this example, but we include it for completeness. Such a scheme is more attractive when
one level of each variable is relatively rare and we choose to oversample both levels to
ensure some representation.

The main question of interest concerning these data is whether the presence of
particles on the wafer affects the quality outcome. We shall see that all four sampling
schemes lead to exactly the same conclusion. First, let's set up the data in a convenient
form for analysis:

\> y <- c (320, 14, 80, 36)
> particle <- gl (2, 1, 4, labels=c ("no", "yes") )
> quality <- gl (2, 2, labels=c ("good", "bad") )
> wafer <- data. frame (y, particle, quality)
> wafer


<table>
<tr>
<th></th>
<th>y</th>
<th>particle</th>
<th>quality</th>
</tr>
<tr>
<td>1</td>
<td>320</td>
<td>no</td>
<td>good</td>
</tr>
<tr>
<td>2</td>
<td>14</td>
<td>yes</td>
<td>good</td>
</tr>
<tr>
<td>3</td>
<td>80</td>
<td colspan="2">no bad</td>
</tr>
<tr>
<td>4</td>
<td>36</td>
<td colspan="2">yes bad</td>
</tr>
</table>


We will need the data in this form with one observation per line for our model fitting, but
usually we prefer to observe it table form:

\> (ov <- xtabs (y ~ quality+particle) )
particle
quality no
yes
good 320
14
bad 80 36


#### Poisson Model

Suppose we assume that the process is observed for some period of time and we count the
number of occurrences of the possible outcomes. It would be natural to view these
outcomes occurring at different rates and that we could form Poisson model for these
rates. Suppose we fit an additive model:

\> modl <- glm(y ~ particle+quality, poisson)
> summary(modl)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
<th>Pr (&gt; | z | )</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>5.6934</td>
<td>0.0572</td>
<td>99.54</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>particleyes</td>
<td>-2.0794</td>
<td>0.1500</td>
<td>-13.86</td>
<td>&lt;2e-16</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="78" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->


<table>
<tr>
<td>qualitybad -1.0576</td>
<td>0.1078 -9.81 &lt;2e-16</td>
</tr>
<tr>
<td colspan="2">(Dispersion parameter for poisson family taken to be 1)</td>
</tr>
<tr>
<td>Null deviance: 474.10</td>
<td>on 3 degrees of freedom</td>
</tr>
<tr>
<td>Residual deviance: 54.03</td>
<td>on 1 degrees of freedom</td>
</tr>
</table>


The null model, which suggests all four outcomes occur at the same rate, does not fit
because the deviance of 474.1 is very large for three degrees of freedom. The additive
model, with a deviance of 54.03 is clearly an improvement over this. We might also want
to test the significance of the individual predictors. We could use the z-values, but it is
better to use the likelihood ratio test based on the differences in the deviance (not that it
matters much for this particular dataset):

\> dropl (modl, test="Chi")
Single term deletions
Model:
y ~ particle + quality


<table>
<tr>
<th>Df</th>
<th>Deviance</th>
<th>AIC</th>
<th>LRT</th>
<th></th>
</tr>
<tr>
<td>$< \mathrm { n o n e } >$</td>
<td>54</td>
<td>84</td>
<td></td>
<td></td>
</tr>
<tr>
<td>particle 1</td>
<td>364</td>
<td>392</td>
<td>310</td>
<td>$< 2 e - 1 6$</td>
</tr>
<tr>
<td>quality 1</td>
<td>164</td>
<td>192</td>
<td>110</td>
<td>$< 2 e - 1 6$</td>
</tr>
</table>


We see that both predictors are significant relative to the full model. By examining the
coefficients, we see that wafers with particles occur at a significantly higher rate than
wafers without particles. Similarly, we see that bad-quality wafers occur at a significantly
higher rate than good-quality wafers.

The model coefficients are closely related to the marginal totals in the table. The
maximum likelihood estimates satisfy:

$$X ^ { T } y = X ^ { T }$$

where the $X ^ { T } y$ is, in this example:

$$> \left( t \left( \mathrm { m o d e l } . \mathrm { m a t r i x } \left( \mathrm { m o d } 1 \right) \right) \stackrel { \circ } { \circ } \star \mathrm { o y } \right) \left[ _ { \prime } , \right]$$
$$\left( \mathrm { I n t e r c e p t } \right) \mathrm { p a r t i c l e y e s } \mathrm { q u a l i t y b a d }$$

450
50
116

So we see that the fitted values, $\dot { I } _ { t , a r c }$ a function of marginal totals. This fact is exploited
in an alternative fitting method known as iterative proportional fitting. The glm function
in $\mathrm { R } ,$ however, uses Fisher scoring, described in Section 6.2. In any case, the log-
likelihood (ignoring any terms not involving $\mu$ is:

$$\log L = \sum _ { i } y _ { i } \log u _ { i }$$

which is maximized to obtain the fit.

The analysis so far has told us nothing about the relationship between the presence of
particles and the quality of the wafer. The additive model posits:

$$\log \mu = \gamma + \alpha _ { i } + \beta _ { j }$$

<!-- PageBreak -->

<!-- PageNumber="79" -->
<!-- PageHeader="Contingency tables" -->

where a represents the particle effect and $\beta$ represents the quality outcome and $\dot { l } ,$ $j = 1 , 2 .$ $\gamma$
is the intercept term. Due to the log link, the predicted rate for the response in any cell in
the table is formed from the product of the rates for the corresponding levels of the two
predictors. There is no interaction term and so good- or bad-quality outcomes occur
independently of whether a particle was found on the wafer. This model has a deviance of
54.03 on one degree of freedom and so does not fit the data.

The addition of an interaction term would saturate the model and so would have zero
deviance and degrees of freedom. So an hypothesis comparing the models with and
without interaction would use a test statistic of 54.03 on one degree of freedom. The
hypothesis of no interaction would be rejected.


#### Multinomial Model

Suppose we assume that the total sample size was fixed at 450 and that the frequency of
the four possible outcomes was recorded. In these circumstances, it is natural to use a
multinomial distribution to model the response. Let $y _ { i j }$ be the observed response in cell (i,
$\left. j \right)$ and let $p _ { i j }$ be the probability that an observation falls in that cell and $\mathrm { l e t } n$ $n$ be the sample
size. The probability of the observed response under the multinomial is then:

$$\frac { n ! } { \text { II: } \Pi _ { j } y _ { i j } } \prod _ { i } \prod _ { j } p _ { i j } ^ { y _ { i j } }$$

Now the $p _ { i j }$ will be linked to the predictor information according to the model we choose.
To estimate the parameters, we would maximize the log-likelihood:

$$\log L = \sum _ { i } \sum _ { j } y _ { i j } \log p _ { i j }$$

where terms not $\mathrm { i n v o l v i n g } p _ { i }$ are ignored. Notice that this takes essentially the same form
as for the Poisson model above.

The main hypothesis of interest is whether the quality and presence of a particle on the
wafer are independent. Let $p _ { i }$ for $i = 1 , 2$ be the probabilities of the two quality outcomes
and $p _ { j }$ for $j = 1 , 2$ be the probability of the two particle categories. Let $P _ { \dot { y } }$ be the probability
of a particular joint outcome. Under independence, $p _ { i j } = p _ { i } p _ { j } .$ Using the fact that
probabilities must sum to one, the maximum likelihood estimates are:

$$\widehat { p } _ { i } = \sum _ { j } y _ { i j } / n$$
$$\ddot { p } _ { j } = \sum _ { i } y _ { i j } / n$$
and

We can compute these for the wafer data as, respectively:

\> (pp <- prop. table ( xtabs (y ~ particle) ) )
particle
no yes
0.88889 0.11111
> (qp <- prop. table ( xtabs (y ~ quality) ) )
quality
good bad
0.74222 0.25778

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 80" -->

The fitted values are then
$\widehat { \mu } _ { i j } = n p _ { i } p _ { j } = \sum _ { i } y _ { i j } \sum _ { j } y _ { i j } / n$
or:

\> (fv <- outer (qp,pp) *450)
particle
quality
no
yes
good
296.89 37.111
bad 103.11 12.889

To test the fit, we compare this model against the saturated model, for which $\ddot { \mathrm { H } } _ { \mathrm { P } } = \mathrm { y } _ { \mathrm { i } j }$ .So
the deviance is:

$$2 \sum \sum _ { j } y _ { i j } \log \left( y _ { i j } / \mu _ { i j } \right)$$

which computes to:

$$> 2 ^ { \star } \sin \left( o v ^ { \star } \log \left( o v / f v \right) \right)$$

[1] 54.03

which is the same deviance we observed in the Poisson model. So we see that the test for
independence in the multinomial model coincides with the test for no interaction in the
Poisson model. The latter test is easier to execute in $\mathrm { R } ,$ so we shall usually take that
approach.

This connection between the Poisson and multinomial is no surprise due to the
following result. Let $Y _ { 1 } , \ldots , Y _ { \mathrm { k } }$ be independent Poisson random variables with means $\lambda _ { 1 , \cdots } .$
$\lambda _ { k } ,$ then the joint distribution of $Y _ { 1 } , \ldots , Y _ { k } | \Sigma _ { i } \mathrm { Y } _ { i } = n$ is multinomial with probabilities
$p _ { i } = \lambda _ { i } / 2 _ { i } \lambda _ { i } .$

One alternative to the deviance is the Pearson $X ^ { 2 }$ statistic:

$$X ^ { 2 } = \sum _ { i , j } \frac { \left( y _ { i j } - \widehat { \mu } _ { i j } \right) ^ { 2 } } { \widehat { \mu } _ { i j } }$$

which takes the value:

$> \mathrm { s u m } \left( \quad \left( o v - f v \right) ^ { \wedge } 2 / f v \right)$
[1] 62.812

Yates' continuity correction subtracts 0.5 from $y _ { i j } - i _ { i j }$ Hijwhen this value is positive and
adds 0.5 when it is negative. This gives superior results for small samples. This
correction is implemented in:

\> prop. test (ov)
2-sample test for equality of proportions with
continuity correction

data: ov
X-squared = 60.124, df = 1, p-value = 8.907e-15

<!-- PageBreak -->

<!-- PageNumber="81" -->
<!-- PageHeader="Contingency tables" -->

The deviance-based test is preferred to the Pearson's $X ^ { 2 } .$


#### Binomial

It would also be natural to view the presence of the particle as affecting the quality of
wafer. We would view the quality as the response and the particle status as a predictor.
We might fix the number of wafers with no particles at 400 and the number with particles
as 50 and then observe the outcome. We could then use a binomial model for the
response for both groups. Let's see what happens:

\> (m <- matrix (y, nrow=2) )
[, 1] [,2]
[1,] 320 80
[2,]
14
36
> deviance (modb)
[1] 54.03

\> modb <- glm (m ~ 1, family=binomial)

We fit the null model which suggests that the probability of the response is the same in
both the particle and no particle group. This hypothesis of homogeneity corresponds
exactly to the test of independence and the deviance is exactly the same.

For larger contingency tables, where there are more than two rows (or columns), we
can use a multinomial model for each row. This model is more accurately called a
product multinomial model to distinguish it from the unrestricted multinomial model
introduced above.


#### Hypergeometric

The remaining case is where both marginal totals are fixed. This situation is rather less
common in practice, but does suggest a more accurate test for independence. This
sampling scheme can arise when classifying objects into one of two types when the true
proportions of each type are known in advance. For example, suppose you are given 10
true or false statements and told that 5 are true and 5 are false. You are asked to sort the
statements into true and false. We can generate a two-by-two table of the correct
classification against the observed classification generated. Under the hypergeometric
distribution and the assumption of independence, the probability of the observed table is:

$$\frac { \left( y _ { 1 1 } + y _ { 1 2 } \right) ! \left( y _ { 1 1 } + y _ { 2 1 } \right) ! \left( y _ { 1 2 } + y _ { 2 2 } \right) ! \left( y _ { 2 1 } + y _ { 2 2 } \right) ! } { y _ { 1 1 } ! y _ { 1 2 } ! y _ { 2 1 } ! y _ { 2 2 } ! n ! }$$

If we fix any number in the table, say $y _ { 1 1 } ,$ the remaining three numbers are completely
determined because the row and column totals are known. There is a limited number of
values which $y _ { 1 1 }$ can possibly take and we can compute the probability of all these
outcomes. Specifically, we can compute the total probability of all outcomes more
extreme than the one observed. This method is called Fisher's exact test. We may
execute it as follows:

\> fisher. test (ov)

Fisher's Exact Test for Count Data
data: ov

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 82

p-value = 2.955e-13
alternative hypothesis: true odds ratio is not equal to
1

95 percent confidence interval:
5.0906 21.5441

sample estimates :
odds ratio
10.213

Notice that the odds ratio, which is $\log \left( y _ { 1 1 } y _ { 2 2 } \right) / \left( y _ { 1 2 } y _ { 2 1 } \right) ,$ takes the value:

\> (320\*36) / (14\*80)
[1] 10.286

and is a measure of the association for which an exact confidence interval may be
calculated as we see in the output.

Fisher's test is attractive because the null distribution for the deviance and Pearson's
$x ^ { 2 }$ test statistics is only approximately $x ^ { 2 }$ distributed. This approximation is particularly
suspect for tables with small counts making an exact method valuable. The Fisher test
becomes more difficult to compute for larger tables and some approximations may be
necessary. However, for larger tables, the $x ^ { 2 }$ approximation will tend to be very accurate.


### 4.2 Larger Two-Way Tables

Snee (1974) presents data on 592 students cross-classified by hair and eye color.

\> data (haireye)
> haireye

y eye hair
5 green BLACK

1
2
29 green BROWN
. . etc. .
16
7 brown BLOND

The data is more conveniently displayed using:

\> (ct <- xtabs (y ~ hair + eye, haireye) )
eye


<table>
<tr>
<th>hair</th>
<th>green</th>
<th>hazel</th>
<th>blue</th>
<th>brown</th>
</tr>
<tr>
<td>BLACK</td>
<td>5</td>
<td>15</td>
<td>20</td>
<td>68</td>
</tr>
<tr>
<td>BROWN</td>
<td>29</td>
<td>54</td>
<td>84</td>
<td>119</td>
</tr>
<tr>
<td>RED</td>
<td>14</td>
<td>14</td>
<td>17</td>
<td>26</td>
</tr>
<tr>
<td>BLOND</td>
<td>16</td>
<td>10</td>
<td>94</td>
<td>7</td>
</tr>
</table>


We can execute the usual Pearson's $x ^ { 2 }$ test for independence as:

\>
summary (ct)

<!-- PageBreak -->

<!-- PageHeader="Contingency tables" -->
<!-- PageNumber="83" -->

Call: xtabs ( formula = y ~ hair + eye, data = haireye)
Number of cases in table: 592

Number of factors: 2

Test for independence of all factors:
Chisq = 138, df = 9, p-value = 2.3e-25

where we see that hair and eye color are clearly not independent.

One option for displaying contingency table data is the dotchart:

\> dotchart (ct)

which may be seen in the first panel of Figure 4.1. The mosaic plot, described in Hartigan
and Kleiner (1981), divides the plot region according to the frequency of each level in a
recursive manner:

$$> m o s a i c p l o t \left( c t , c o l o r = T R U E , m a i n = N U L L , l a s = 1 \right)$$

In the plot shown in the second panel of Figure 4.1, the area is first divided according to
the frequency of hair color. Within each hair color, the area is then divided according to
the frequency of eye color. A different plot could be constructed by reversing the order of
hair and eye in the xtabs command above. We can now readily see the frequency of
various outcomes. We see, for example, that brown hair and brown


<figure>
<figcaption>Figure 4.1 Dotchart and Mosaic Plot</figcaption>

green

BLOND

0

BLACK

BHOWN

HED

RED

0

BROWN

0

BLACK

0

hazel

BLOND

0

RED

0

BROWN

BLACK

0

0

eye

blue

BLOND

0

RED

0

BROWN

0

BLACK

0

brown

BLOND

0

RED

BROWN

0

0

BLACK

0

I

I

I

I

I

hair

30

40

60

100

</figure>


eyes is the most common combination while green eyes and black hair is the least
common.

Now we fit the Poisson GLM:

\> modc <- glm(y ~ hair+eye, family=poisson, haireye)

\> summary (modc)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>z value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>2.458</td>
<td></td>
<td>0.152</td>
<td>16.14</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>hair BROWN</td>
<td>0.974</td>
<td></td>
<td>0.113</td>
<td>8.62</td>
<td>$< 2 e - 1 6$</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 84" -->


<table>
<tr>
<td>hairRED</td>
<td>-0.419</td>
<td>0.153</td>
<td>-2.75</td>
<td>0.006</td>
</tr>
<tr>
<td>hairBLOND</td>
<td>0.162</td>
<td>0.131</td>
<td>1.24</td>
<td>0.216</td>
</tr>
<tr>
<td>eyehazel</td>
<td>0.374</td>
<td>0.162</td>
<td>2.30</td>
<td>0.021</td>
</tr>
<tr>
<td>eyeblue</td>
<td>1.212</td>
<td>0.142</td>
<td>8.51</td>
<td>$< 2 e - 1 6$</td>
</tr>
<tr>
<td>eyebrown</td>
<td>1.235</td>
<td>0.142</td>
<td>8.69</td>
<td>$< 2 e - 1 6$</td>
</tr>
</table>

(Dispersion parameter for poisson family taken to be 1)
Null deviance: 453.31 on 15 degrees of freedom
Residual deviance: 146.44 on 9 degrees of freedom
AIC: 241.0


We see that most of the levels of hair and $e y e$ color show up as significantly different
from the reference levels of black hair and green eyes. But this merely indicates that there
are higher numbers of people with some hair colors than others and some eye colors than
others. We already know this. We are more interested in the relationship between hair
and eye color. The deviance of 146.44 on nine degrees freedom shows that they are
clearly dependent. This does not tell us how they are dependent. To study this, we can
use a kind of residual analysis for contingency tables called correspondence analysis.

Compute the Pearson residuals rp and write them in the matrix form $R _ { i j } ,$ where $i =$
$1 , \ldots , r$ and $j = 1 , \ldots , c ,$ according to the structure of the data. Perform the singular value
decomposition:

$$R _ { r \times c } = U _ { r \times v } D _ { w \times w } V _ { w \times c } ^ { T }$$

where $r$ is the number of rows, $c$ is the number of columns and $w = \min \left( r , c \right) .$ $U$ and $V$ are
called the right and left singular vectors, respectively. $D$ is a diagonal matrix with sorted
elements $d _ { i } ,$ called singular values. Another way of writing this is:

$$R _ { i j } = \sum _ { k = 1 } ^ { w } U _ { i k } d _ { k } V _ { j k }$$

As with eigendecompositions, it is not uncommon for the first few singular values to be
much larger than the rest. Suppose that the first two dominate so that:

$R _ { i j } \approx U _ { i 1 } d _ { 1 } V _ { j 1 } + U _ { i 2 } d _ { 2 } V _ { j 2 }$

We usually absorb the $d s$ into $U$ and $V$ for plotting purposes so that we can assess the
relative contribution of the components. Thus:

$$R _ { i j } \approx \left( U _ { i 1 } \sqrt { d _ { 1 } } \right) \times \left( V _ { j 1 } \sqrt { d _ { 1 } } \right) + \left( U _ { i 2 } \sqrt { d _ { 2 } } \right) \times \left( V _ { i 2 } \sqrt { d _ { 2 } } \right)$$
$$\equiv U _ { i 1 } V _ { j 1 } + U _ { i 2 } V _ { j 2 }$$

where in the latter expression we have redefined the $U s$ and $V s$ to include the $\sqrt { d } .$

The two-dimensional correspondence plot displays $U _ { i 2 }$ against $U _ { i 1 }$ and $V _ { j 2 }$ against $V _ { j 1 }$
on the same graph. So the points on the plot will either represent a row level (U) or a
column level $\left( V \right) .$ We compute the plot for the hair and eye color data:

$$\left. > z < - \text { xtabs \left(res iduals \left(mode, type=npearson^{\prime\prime } \right) \sim \text { hairteye } } ,$$
$$\begin{array}{} { \text { nal reye } } \\ { > \text { svalz } < - \text { sva } \left( z , 2 , 2 \right) } \end{array}$$

<!-- PageBreak -->

<!-- PageNumber="85" -->
<!-- PageHeader="Contingency tables" -->

\> leftsv <- svdzu %\*% diag (sqrt (svdz$d [1:2]) )
> rightsv <- svdz$v %\*% diag (sqrt (svdz$d[1:2]))
> 11 <- 1.1*max (abs (rightsv) , abs (leftsv) )
> plot (rbind (leftsv, rightsv) , asp=1, xlim=c (-
11, 11) , ylim=c (-11, 11) ,
xlab="SVl",ylab="SV2",type="n")
> abline (h=0, v=0)
> text (leftsv, dimnames (z) [ [1] ] )
> text (rightsv, dimnames (z) [ [2] ] )

The plot is shown in Figure 4.2. The correspondence analysis plot can be interpreted in
light of the following observations:

. $\sum d _ { i } ^ { 2 } = p _ { \text { earson } ^ { \prime } S } X ^ { 2 }$ is called the inertia. When $= C ,$ are the eigenvalues of $R .$
$d _ { i } ^ { 2 }$

. Look for large values of $| U i |$ indicating that the row $\dot { l }$ profile is different. For example,
the point for blonds in Figure 4.2 is far from the origin indicating that the distribution
of eye colors within this group of people is not typical. In contrast, we see that the
point for people with brown hair is close to the origin, indicating an eye color
distribution that is close to the overall average. The same type of observation is true
for the columns, $| V j | .$ Points distant from the origin mean that the level associated with
the column $j$ profile is different in some way.

· If row and column levels appear close together on the plot and far from the
origin, we can see that there will be a large positive residual associated with this
particular combination indicating a strong positive association. For example, we
see that blue eyes and blond hair occur close together on the plot and far from the
origin indicating a strong association. On the other hand, if the two points are
situated diametrically apart on either side of the origin, we may expect a large
negative residual indicating a strong negative association. For example, there are
relatively fewer people with blond hair and brown eyes than would be expected
under independence.

· If points representing two rows or two column levels are close together, this indicates
that the two levels will have a similar pattern of association. In some cases, one might
consider combining the two levels. For example, people with hazel or green eyes have
similar hair color distributions and we might choose to combine these two categories.

· Because the distance between points is of interest, it is important that the plot is scaled
so that the visual distance is proportionately correct. This does not happen
automatically, because the default behavior of plots is to fill the plot region out to the
specified aspect ratio.

There are several competing ways to construct contingency tables. See Venables and
Ripley (2002) who provide the function corresp in the MASS package. See also Blasius
and Greenacre (1998) for a survey of methods for visualizing categorical data.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 86" -->


<figure>
<figcaption>Figure 4.2 Correspondence analysis for hair-eye combinations. Hair colors are given in upper-case letters and eye colors are given in lower-case letters.</figcaption>

2

₪

BLACK

1

brown

$\frac { n } { n }$

blue
BLOND

0

BROWN

=
T

hazel

RED green

-2

-3

3

-2

-1

0

1

2

3

SV1

</figure>


### 4.3 Matched Pairs

In the typical two-way contingency tables, we display accumulated information about
two categorical measures on the same object. In matched pairs, we observe one measure
on two matched objects.

In Stuart (1955), data on the vision of a sample of women is presented. The left and
right eye performance is graded into four categories:

\> data (eyegrade)
> (ct <- xtabs (y ~ right+left, eyegrade) )
left

<!-- PageBreak -->

<!-- PageNumber="87" -->
<!-- PageHeader="Contingency tables" -->


<table>
<tr>
<th>right</th>
<th>best</th>
<th>second</th>
<th>third</th>
<th>worst</th>
</tr>
<tr>
<td>$b e s t$</td>
<td>1520</td>
<td>266</td>
<td>124</td>
<td>66</td>
</tr>
<tr>
<td>$\mathrm { s e c o n d }$</td>
<td>234</td>
<td>1512</td>
<td>432</td>
<td>78</td>
</tr>
<tr>
<td>third</td>
<td>117</td>
<td>362</td>
<td>1772</td>
<td>205</td>
</tr>
<tr>
<td>worst</td>
<td>36</td>
<td>82</td>
<td>179</td>
<td>492</td>
</tr>
</table>


If we check for independence:

\> summary (ct)
Call: xtabs ( formula = y ~ right + left, data =
eyegrade)

Number of cases in table: 7477
Number of factors: 2
Test for independence of all factors:
Chisq = 8097, df = 9, p-value = 0

We are not surprised to find strong evidence of dependence. A more interesting
hypothesis for such matched pair data is symmetry. Is $p _ { i j } = p _ { i j }$ We can fit such a model by
defining a factor where the levels represent the symmetric pairs for the off-diagonal
elements. There is only one observation for each level down the diagonal:


<table>
<tr>
<th colspan="4">&gt; (symfac &lt;- factor (apply (eyegrade [ , 2 : 3] , 1, function (x) paste (sort (x), collapse="-") ) ) )</th>
</tr>
<tr>
<th>[1] best-best worst</th>
<th>best-second</th>
<th>best-third</th>
<th>best-</th>
</tr>
<tr>
<td>[5] best-second worst</td>
<td>second-second</td>
<td>second-third</td>
<td>second-</td>
</tr>
<tr>
<td>[9] best-third worst</td>
<td>second-third</td>
<td>third-third</td>
<td>third-</td>
</tr>
<tr>
<td>[13] best-worst worst</td>
<td>second-worst</td>
<td>third-worst</td>
<td>worst-</td>
</tr>
<tr>
<td colspan="2">10 Levels: best-best best-second worst-worst</td>
<td>best-third</td>
<td></td>
</tr>
</table>


We now fit this model:

\> mods <- glm(y ~ symfac, eyegrade, family=poisson)
> c (deviance (mods) , df. residual (mods) )
[1] 19.249
6.000
> pchisq (deviance (mods) , df. residual (mods) , lower=F)
[1] 0.0037629

Here, we see evidence of a lack of symmetry. It is worth checking the residuals:

\> round (xtabs (residuals (mods) ~ right+left,
eyegrade) , 3)
left


<table>
<tr>
<th>right</th>
<th>best</th>
<th>second</th>
<th>third</th>
<th>worst</th>
</tr>
<tr>
<td>best</td>
<td>0.000</td>
<td>1.001</td>
<td>0.317</td>
<td>2.008</td>
</tr>
<tr>
<td>second</td>
<td>-1.023</td>
<td>0.000</td>
<td>1.732</td>
<td>-0.225</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 88" -->


<table>
<tr>
<td>third</td>
<td>-0.320 -1.783</td>
<td>0.000</td>
<td>0.928</td>
</tr>
<tr>
<td>worst</td>
<td>-2.219 0.223</td>
<td>-0.949</td>
<td>0.000</td>
</tr>
</table>


We see that the residuals above the diagonal are mostly positive, while they are mostly
negative below the diagonal. So there are generally more poor left, good right eye
combinations than the reverse. Furthermore, we can compute the marginals:

\> margin. table (ct, 1)
right
best second third
worst
1976 2256 2456
789
> margin.table (ct, 2)
left


<table>
<tr>
<th>best</th>
<th>second</th>
<th>third</th>
<th>worst</th>
</tr>
<tr>
<td>1907</td>
<td>2222</td>
<td>2507</td>
<td>841</td>
</tr>
</table>


We see that there are somewhat more poor left eyes and good right eyes, so perhaps
marginal homogeneity does not hold here. The assumption of symmetry implies marginal
homogeneity (the reverse is not necessarily true). We may observe data where there is a
difference in the frequencies of the levels of the rows and columns, but still be interested
in symmetry. Suppose we set:

$P _ { i j } = \alpha _ { i } \beta _ { j } \gamma _ { i j }$

where $\gamma _ { i j } = \gamma _ { j i } .$ This will allow for some symmetry while allowing for different marginals.
This is the quasi-symmetry model. Now:

$\log E Y _ { i j } = \log n p _ { i j } = \log n + \log \alpha _ { i } + \log \beta _ { j } + \log \gamma _ { i j }$

So we can fit this model using:

\> modq <- glm(y ~ right+left+symfac, eyegrade,
family=poisson)
> pchisq (deviance (modq) , df. residual (modq) , lower=F)
[1] 0.06375

We see that this model does fit. It can be shown that marginal homogeneity together with
quasi-symmetry implies symmetry. One can test for marginal homogeneity by comparing
the symmetry and quasi-symmetry models:

\> anova (mods, modq, test="Chi")
Analysis of Deviance Table
Model 1: y ~ symfac
Model 2: y ~ right + left + symfac
Resid. Df Resid. Dev Df Deviance P (> | Chi| )
1
6
19.25
2

3
7.27
3
11.98
0.01

So we find evidence of a lack of marginal homogeneity. This test is only appropriate if
quasi-symmetry already holds.

<!-- PageBreak -->

<!-- PageNumber="89" -->
<!-- PageHeader="Contingency tables" -->

When we examine the data here, we do see that many people do have symmetric
vision. These entries lie down the diagonal. We might ask whether there is independence
between left and right eyes among those people whose vision is not symmetric. This is
the quasi-independence hypothesis and we can test it by omitting the data from the
diagonal:

\> modqi <- glm(y ~ right+left, eyegrade,
family=poisson,
subset =- c (1, 6, 11, 16) )
> pchisq (deviance (modqi) , df. residual (modqi) , lower=F)
[1] 4.4118e-41

This model does not fit. This is not surprising since we can see that the entries adjacent to
the diagonal are larger than those further away. The difference in vision between the two
eyes is likely to be smaller than expected under independence.


### 4.4 Three-Way Contingency Tables

In Appleton, French, and Vanderpump (1996), a 20-year follow-up study on the effects of
smoking is presented. In the period 1972-74, a larger study, which also considered other
issues, categorized women into smokers and nonsmokers and according to their age
group. In the follow-up, the researchers recorded whether the subjects were dead or still
alive. Only smokers or women who had never smoked are presented here. Relatively few
smokers quit and these women have been excluded from the data. The cause of death is
not reported here. Here is the data:

\> data (femsmoke)
> femsmoke


<table>
<tr>
<th></th>
<th>y</th>
<th>smoker</th>
<th>dead</th>
<th>age</th>
</tr>
<tr>
<td>1</td>
<td>2</td>
<td>yes</td>
<td>yes</td>
<td>18-24</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>no</td>
<td>yes</td>
<td>18-24</td>
</tr>
<tr>
<td>3</td>
<td>3</td>
<td>yes</td>
<td>yes</td>
<td>25-34</td>
</tr>
<tr>
<td>. . . 28</td>
<td>0</td>
<td>no</td>
<td>no</td>
<td>75+</td>
</tr>
</table>


We can combine the data over age groups to produce:

\> (ct <- xtabs (y ~ smoker+dead, femsmoke) )
dead
smoker yes no
yes 139 443
no 230 502

We can compute the proportions of dead and alive for smokers and nonsmokers:

\> prop. table (ct, 1)
dead

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 90


<table>
<tr>
<th>smoker</th>
<th>yes</th>
<th>no</th>
</tr>
<tr>
<td>yes</td>
<td>0.23883</td>
<td>0.76117</td>
</tr>
<tr>
<td>no</td>
<td>0.31421</td>
<td>0.68579</td>
</tr>
</table>


We see that 76% of smokers have survived for 20 years while only 69% of nonsmokers
have survived. Thus smoking appears to have a beneficial effect on longevity. We can
check the significance of this difference:

\> summary (ct)
Call: xtabs ( formula = y ~ smoker + dead, data =
femsmoke)
Number of cases in table: 1314
Number of factors: 2
Test for independence of all factors:
Chisq = 9.1, df = 1, p-value = 0.0025

So the difference cannot be reasonably ascribed to chance variation. However, if we
consider the relationship within a given age group, say 55-64:

\> (cta <- xtabs (y ~ smoker+dead, femsmoke,
subset= (age == "55-64") ) )
dead
smoker yes no
yes 51 64
no

40
81
\> prop. table (cta, 1)
dead
smoker yes no
yes 0.44348 0.55652
no 0.33058 0.66942

We see that 56% of the smokers have survived compared to 67% of the nonsmokers. This
advantage to nonsmokers holds throughout all the age groups. Thus the marginal
association where we add over the age groups is different from the conditional
association observed within age groups. Data where this effect is observed are an
example of Simpson's paradox. The paradox is named after Simpson (1951), but dates
back to Yule (1903).

Let's see why the effect occurs here:

\> prop. table (xtabs (y ~ smokertage, femsmoke) , 2)
age
smoker 18-24 25-34 35-44 45-54 55-64 65-
74 75+
yes 0.47009 0.44128 0.47391 0.62500 0.48729 0.21818
0.16883
no 0.52991 0.55872 0.52609 0.37500 0.51271 0.78182
0.83117

<!-- PageBreak -->

<!-- PageNumber="91" -->
<!-- PageHeader="Contingency tables 9" -->

We see that smokers are more concentrated in the younger age groups and younger
people are more likely to live for another 20 years. This explains why the marginal table
gave an apparent advantage to smokers which is, in fact, illusory because once we control
for age, we see that smoking has a negative effect on longevity.

It is interesting to note that the dependence in the 55-64 age group is not statistically
significant:

\> fisher. test (cta)

Fisher's Exact Test for Count Data
data: cta

p-value = 0.08304
alternative hypothesis: true odds ratio is not equal to
1
95 percent confidence interval:
0.92031 2.83340

sample estimates :
odds ratio
1.6103

However, this is just a subset of the data. Suppose we compute the odds ratios in all the
age groups:

\> ct3 <- xtabs (y ~ smoker+dead+age, femsmoke)
> apply (ct3, 3, function (x)
(x [1, 1 ] *x [2, 2] ) / (x [1, 2] *x [2,1] ) )
18-24 25-34 35-44 45-54 55-64 65-74
75+
2.30189 0.75372 2.40000 1.44175 1.61367 1.14851
$N a N$

We see that there is some variation in the odds ratio, but they are all greater than one with
the exception of the 25-34 age group. We could test for independence in each $2 \times 2$ table,
but it is better to use a combined test. The Mantel-Haenszel test is designed to test
independence in $2 \times 2$ tables across $K$ strata. It only makes sense to use this test if the
relationship is similar in each stratum. For this data, the observed odds ratios do not vary
greatly, so the use of the test is justified.

Let the entries in the $2 \times 2 \times K$ table be $y _ { i j k } .$ If we assume a hypergeometric distribution
in each $2 \times 2$ table, then $y _ { 1 1 k }$ is sufficient for each table given that we assume that the
marginal totals for each table carry no information. The Mantel-Haenszel statistic is:

$$\frac { \left( | \sum _ { k } y _ { 1 | k } - \sum _ { k } E y _ { 1 1 k } | - 1 / 2 \right) ^ { 2 } } { \sum _ { k } \text { var } y _ { 1 1 k } }$$

where the expectation and variance are computed under the null hypothesis of
independence in each stratum. The statistic is approximately $Z _ { 1 } ^ { 2 }$ distributed under the null,
although it is possible to make an exact calculation for smaller datasets. The statistic as
stated above is due to Mantel and Haenszel (1959), but a version without the half
continuity correction was published by Cochran (1954). For this reason, it is sometimes
known as the Cochran-Mantel-Haenszel statistic.

We compute the statistic for the data here:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 92

\> mantelhaen.test (ct3, exact=TRUE)

Exact conditional test of independence in 2 x 2
x k
tables
data: ct3
S = 139, p-value = 0.01591
alternative hypothesis: true common odds ratio is not
equal to 1

95 percent confidence interval:
1.0689 2.2034
sample estimates :
common odds ratio
1.5303

We used the exact method in preference to the approximation. We see that $a$ statistically
significant association is revealed once we combine the information across strata.

Now let's consider a linear models approach to investigating how three factors
interact. Let $p _ { i j k }$ be the probability that an observation falls into the $\left( i , j , k \right)$ cell. Let $p _ { i }$ be
the marginal probability that the observation falls into the $i ^ { t h }$ cell of the first variable, $p _ { j }$
be the marginal probability that the observation falls into the $j ^ { t h }$ cell of the second
variable and $p _ { k }$ be the marginal probability that the observation falls into the $k ^ { t h }$ cell of the
third variable.

Mutual Independence: If all three variables are independent, then:

$P _ { i j k } = P _ { i } P _ { j } P _ { k }$

Now $E Y _ { i j k } = n p _ { i j k }$ SO:

$$\log E Y _ { i j k } = \log n + \log p _ { i } + \log p _ { j } + \log p _ { k }$$

So the main effects-only model corresponds to mutual independence. The coding we use
will determine exactly how the parameters relate to the margin totals of the table although
typically we will not be especially interested in these. Since independence is the simplest
possibility, this model is the null model in an investigation of this type. The model log
$E Y _ { i j k } = \mu$ would suggest that all the cells have equal probability. It is rare that such a model
would have any interest so the model above makes for a more appropriate null.

We can test for independence using the Pearson's $x ^ { 2 }$ test:

\> summary (ct3)
Call: xtabs ( formula = y ~ smoker + dead + age, data =
femsmoke)
Number of cases in table: 1314
Number of factors: 3
Test for independence of all factors:
Chisq = 791, df = 19, p-value = 2.1e-155

We can also fit the appropriate linear model:

\> modi <- glm(y ~ smoker + dead + age, femsmoke,
family=poisson)

<!-- PageBreak -->

<!-- PageNumber="93" -->
<!-- PageHeader="Contingency tables" -->

\> c (deviance (modi) , df. residual (modi) )
[1] 735 19

Although the statistics for the two tests are somewhat different, in either case, we see a
very large value for the degrees of freedom. We conclude that this model does not fit the
data.

We can show that the coefficients of this model correspond to the marginal
proportions. For example, consider the smoker factor:

\> (coefsmoke <- exp (c (0, coef (modi) [2] ) ))
smokerno
1.0000
1.2577
> coefsmoke/ sum (coefsmoke)
smokerno
0.44292
0.55708

We see that these are just the marginal proportions for the smokers and nonsmokers in
the data:

\> prop. table (xtabs (y ~ smoker, femsmoke) )
smoker
yes
no
0.44292 0.55708

This just serves to emphasize the point that the main effects of the model just convey
information that we already know and is not the main interest of the study.

Joint Independence: Let $p _ { i j }$ be the (marginal) probability that the observation falls
into a $\left( i , j , \cdot \right)$ cell where any value of the third variable is acceptable. Now suppose that
the first and second variable are dependent, but jointly independent of the third. Then:

$P _ { i j k } = P _ { i j } P _ { k }$

We can represent this as:

$$\log E Y _ { i j k } = \log n + \log p _ { i j } + \log p k$$

Using the hierarchy principle, we would also include the main effects corresponding to
the interaction term log $p _ { i j } .$ So the log-linear model with just one interaction term
corresponds to joint independence. The specific interaction term tells us which pair of
variables is dependent. For example, we fit a model that says age is jointly independent
smoking and life status:

\> modj <- glm (y ~ smoker*dead + age, femsmoke,
family=poisson)
> c (deviance (modj) , df. residual (modj) )
[1] 725.8 18.0

Although this represents a small improvement over the mutual independence model, the
deviance is still very high for the degrees of freedom and it is clear that this model does

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 94" -->

not fit the data. There are two other joint independence models that have the two other
interaction terms. These models also fit badly.

Conditional Independence: Let $p _ { i j | k }$ be the probability that an observation falls in cell
(i,j,.) given that we know the third variable takes the value $k .$ Now suppose we assert that
the first and second variables are independent given the value of the third variable, then:

$P _ { i j } | _ { k } = P _ { i } | _ { k } P _ { j } | _ { k }$

which leads to:

$P _ { i j k } = P _ { i k } P _ { j k } | P _ { k }$

This results in the model:

$$\log E Y _ { i j k } = \log n + \log p i k + \log p _ { j k } - \log p _ { k }$$

Again, using the hierarchy principle, we would also include the main effects
corresponding to the interaction terms and we would have model with main effects and
two interaction terms. The minus for the log $p _ { k }$ term is irrelevant. The nature of the
conditional independence can be determined by observing which of one of the three
possible two-way interactions does not appear in the model.

The most plausible conditional independence model for our data is:

\> modc <- glm(y ~ smoker\*age + age\*dead, femsmoke,
[1] 8.327 7.000

$$> c \left( d e v i a n c e \left( m o d e \right) , d f . r e s i d u a l \left( m o d e \right) \right)$$

We see that the deviance is only slightly larger than the degrees of freedom indicating a
fairly good fit. This indicates that smoking is independent of life status given age.
However, bear in mind that we do have some zeroes and other small numbers in the table
and so there is some doubt as to the accuracy of the $x ^ { 2 }$ approximation here. It is generally
better to compare models rather than assess the goodness of fit.

Uniform Association: We might consider a model with all three-way interactions:

$$\log E Y _ { i j k } = \log n + \log p _ { i } + \log p _ { j } + \log p _ { k } + \log p _ { i j } + \log p _ { i k } + \log P _ { j k } P _ { j k }$$

The model has no three-way interaction and so it is not saturated. There is no simple
interpretation in terms of independence. Consider our example:

$$> \text { modu } < - \text { glm } \left( y \sim \left( \text { smoker } + \text { age+aead } \right) ^ { \wedge } 2 , \text { femsmoke } _ { \prime } \right. ,$$
family=poisson)

Now we compute the fitted values and determine the odds ratios for each age group based
on these fitted values:

\> ctf <- xtabs (fitted (modu) ~ smoker+dead+age,
femsmoke)
> apply (ctf, 3, function $\left( x \right)$
$\left. \left( x \left[ 1 , 1 \right] * x \left[ 2 , 2 \right] \right) / \left( x \left[ 1 , 2 \right] * x \left[ 2 , 1 \right] \right) \right)$

<!-- PageBreak -->

<!-- PageNumber="95" -->
<!-- PageHeader="Contingency tables" -->

18-24 25-34 35-44 45-54 55-64 65-74

75+

1.5333
1.5333
1.5333
1.5333
1.5333

1.5333

1.5333

We see that the odds ratio is the same for every age group. Thus the uniform association
model asserts that for every level of one variable, we have the same association for the
other two variables.

The information may also be extracted from the coefficients of the fit. Consider the
log-odds ratio for smoking and life status for a given age group:

$\log \left( E Y _ { 1 1 k } E Y _ { 2 2 k } \right) / \left( E Y _ { 1 2 k } E Y _ { 2 1 k } \right)$

This will be precisely the coefficient for the smoking and life-status term. We extract
this:

\> exp (coef (modu) [ ' smokernordeadno' ] )
smokerno : deadno
1.5333

We see that this is exactly the log-odds ratio we found above. The other interaction terms
may be interpreted similarly.

Model Selection: Log-linear models are hierarchical, so it makes sense to start with
the most complex model and see how far it can be reduced. We can use analysis of
deviance to compare models. We start with the saturated model:

\> modsat <- glm(y ~ smoker\*age\*dead, femsmoke,
family=poisson)
> dropl (modsat, $\mathrm { t e s t } = { } ^ { \mathrm { \prime \prime } } \mathrm { C h } \mathrm { i } ^ { \mathrm { \prime \prime } } { } ^ { \mathrm { \prime \prime } }$
Single term deletions
Model :
y ~ smoker * age * dead


<table>
<tr>
<th></th>
<th>Df</th>
<th>Deviance</th>
<th>AIC</th>
<th>LRT</th>
<th>Pr (Chi)</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td colspan="2">3.0e-10</td>
<td>190.2</td>
<td colspan="2"></td>
</tr>
<tr>
<td>smoker : age : dead</td>
<td>6</td>
<td>2.4</td>
<td>180.6</td>
<td>2.4</td>
<td>0.88</td>
</tr>
</table>


We see that the three-way interaction term may be dropped. Now we consider dropping
the two-way terms:

\> dropl (modu, test="Chi")
Single term deletions
Model:
y ~ (smoker + age + dead) ^2


<table>
<tr>
<th></th>
<th>Df</th>
<th>Deviance</th>
<th>AIC</th>
<th>LRT</th>
<th>Pr (Chi)</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td></td>
<td>2</td>
<td>181</td>
<td></td>
<td></td>
</tr>
<tr>
<td>smoker : age</td>
<td>6</td>
<td>93</td>
<td>259</td>
<td>90</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>smoker : dead</td>
<td>1</td>
<td>8</td>
<td>185</td>
<td>6</td>
<td>0.015</td>
</tr>
<tr>
<td>age : dead</td>
<td>6</td>
<td>632</td>
<td>798</td>
<td>630</td>
<td>&lt;2e-16</td>
</tr>
</table>


Two of the interaction terms are strongly significant, but the smoker: dead term is only
just statistically significant. This term corresponds to the test for conditional

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 96" -->

independence of smoking and life status given age group. We see that the conditional
independence does not hold. This tests the same hypothesis as the Mantel-Haenszel test
above. In this case the p-values for the two tests are very similar.

Binomial Model: For some three-way tables, it may be reasonable to regard one
variable as the response and the other two as predictors. In this example, we could view
life status as the response. Since this variable has only two levels, we can model it using a
binomial GLM. For more than two levels, a multinomial model would be required.

We construct a binomial response model:

\> ybin <- matrix (femsmoke$y, ncol=2)
> modbin <- glm(ybin ~ smoker*age, femsmoke [1:14, ],
family=binomial)

This model is saturated, so we investigate a simplification:

\> dropl (modbin, test="Chi")
Single term deletions
Model:

ybin ~ smoker * age


<table>
<tr>
<th></th>
<th>Df</th>
<th>Deviance</th>
<th>AIC</th>
<th>LRT</th>
<th>(Chi)</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td></td>
<td>5.3e-10</td>
<td>75.0</td>
<td></td>
<td></td>
</tr>
<tr>
<td>smoker : age</td>
<td>6</td>
<td>2.4</td>
<td>65.4</td>
<td>2.4</td>
<td>0.88</td>
</tr>
</table>


We see that the interaction term may be dropped, but now we check if we may drop
further terms:

\> modbinr <- glm(ybin ~ smokertage, femsmoke [1:14, ],
family=binomial)
> dropl (modbinr, test="Chi")
Single term deletions
Model:
ybin ~ smoker + age


<table>
<tr>
<th></th>
<th>Df</th>
<th>Deviance</th>
<th>AIC</th>
<th>LRT</th>
<th>Pr (Chi)</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td></td>
<td>2</td>
<td>65</td>
<td></td>
<td></td>
</tr>
<tr>
<td>smoker</td>
<td>1</td>
<td>8</td>
<td>69</td>
<td>6</td>
<td>0.015</td>
</tr>
<tr>
<td>age</td>
<td>6</td>
<td>632</td>
<td>683</td>
<td>630</td>
<td>&lt;2e-16</td>
</tr>
</table>


We see that both main effect terms are significant, so no further simplification is possible.
This model is effectively equivalent to the uniform association model above. Check the
deviances:

\> deviance (modu)
[1] 2.3809
> deviance (modbinr)
[1] 2.3809

We see that they are identical. We can extract the same odds ratio from the parameter
estimates as above:

<!-- PageBreak -->

<!-- PageNumber="97" -->
<!-- PageHeader="Contingency tables" -->

\> exp (-coef (modbinr) [2])
smokerno
1.5333

The change in sign is simply due to which outcome is considered a success in the
binomial GLM. So we can identify the binomial GLM with a corresponding Poisson
GLM and the numbers we will obtain will be identical. We would likely prefer the
binomial analysis where one factor can clearly be identified as the response and we
would prefer the Poisson GLM approach when the relationship between the variables is
more symmetric. However, there is one important difference between the two
approaches. The null model for the binomial GLM:

\> modbinull <- glm(ybin ~ 1, femsmoke [1:14, ],
family=binomial)
> deviance (modbinull)
[1] 641.5

is associated with this two-way interaction model for the Poisson GLM:

\> modj <- glm(y ~ smoker*age + dead, femsmoke,
family=poisson)
> deviance (modj)
[1] 641.5

So the binomial model implicitly assumes an association between smoker and age. In this
particular dataset, there are more younger smokers than older ones, so the association is
present. However, what if there was no association? One could argue that the Poisson
GLM approach would be superior because it would allow us to drop this term and
achieve a simpler model. On the other hand, one could argue that if the relationship
between the response and the two predictors is the main subject of interest, then we lose
little by conditioning out the marginal combined effect of age and smoking status,
whether it is significant or not.

Correspondence Analysis: We cannot directly apply the correspondence analysis
method described above for two-way tables. However, we could combine two of the
factors into a single factor by considering all possible combinations of the two level. To
make the choice of which two levels to combine, we would pick the pair whose
association is least interesting to us. We could apply this to the smoking dataset here, but
because there are only two levels of smoking and life status, the plot is not very
interesting.


### 4.5 Ordinal Variables

Some variables have a natural order. One can use the methods for nominal variables
described earlier in this chapter, but more information can extracted by taking advantage
of the structure of the data. Sometimes one might identify a particular ordinal variable as
the response. In such cases, the methods of Section 5.3 can be used. However, sometimes

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $R$ 98" -->

one is simply interested in modeling the association between ordinal variables. Here the
use of scores can be helpful.

Consider a two-way table where both variables are ordinal. We may assign scores $u _ { i }$
and $v _ { j }$ to the rows and columns such that $u _ { 1 } \leq u _ { 2 } \leq \ldots \leq u _ { I }$ and $v _ { 1 } \leq v _ { 2 } \leq \ldots \leq v _ { j } .$ The assignment
of scores requires some judgment. If you have no particular preference, even spacing
allows for the simplest interpretation. If you have an interval scale, for example, 0-10
years old, 10-20 years old, 20-40 years old and so on, midpoints are often used. It is a
good idea to check that the inference is robust to the assignment of scores by trying some
alternative choices. If your qualitative conclusions are changed, this is an indication that
you cannot make any strong finding.

Now fit the linear-by-linear association model:

$$\log E Y _ { i j } = \log \mu _ { i j } = \log n p _ { i j } = \log n + \alpha _ { i } + \beta _ { j } + \gamma _ { u i } v _ { j }$$

So $\gamma = 0$ means independence while $\gamma$ represents the amount of association and can be
positive or negative. $\gamma$ is rather like an (unscaled) correlation coefficient. Consider
underlying (latent) continuous variables which are discretized by the cutpoints $u _ { i }$ and $v _ { j }$
We can then identify $\gamma$ with the correlation coefficient of the latent variables

Consider an example drawn from a subset of the 1996 American National Election
Study (Rosenstone, Kinder, and Miller (1997)). Considering just the data on party
affiliation and level of education, we can construct a two-way table:

\> data (nes96)
> xtabs ( ~ PID + educ, nes96)
educ


<table>
<tr>
<th>PID</th>
<th>MS</th>
<th>HSdrop</th>
<th>HS</th>
<th>Coll</th>
<th>CCdeg</th>
<th>BAdeg</th>
<th>MAdeg</th>
</tr>
<tr>
<td>strDem</td>
<td>5</td>
<td>19</td>
<td>59</td>
<td>38</td>
<td>17</td>
<td>40</td>
<td>22</td>
</tr>
<tr>
<td>$\mathrm { w e a k } \mathrm { k D e m }$</td>
<td>4</td>
<td>10</td>
<td>49</td>
<td>36</td>
<td>17</td>
<td>41</td>
<td>23</td>
</tr>
<tr>
<td>indDem</td>
<td>1</td>
<td>4</td>
<td>28</td>
<td>15</td>
<td>13</td>
<td>27</td>
<td>20</td>
</tr>
<tr>
<td>indind</td>
<td>0</td>
<td>3</td>
<td>12</td>
<td>9</td>
<td>3</td>
<td>6</td>
<td>4</td>
</tr>
<tr>
<td>$i n d R e p$</td>
<td>2</td>
<td>7</td>
<td>23</td>
<td>16</td>
<td>8</td>
<td>22</td>
<td>16</td>
</tr>
<tr>
<td>$\mathrm { w e a k R e } \mathcal{D}$</td>
<td>0</td>
<td>5</td>
<td>35</td>
<td>40</td>
<td>15</td>
<td>38</td>
<td>17</td>
</tr>
<tr>
<td>strRep</td>
<td>1</td>
<td>4</td>
<td>42</td>
<td>33</td>
<td>17</td>
<td>53</td>
<td>25</td>
</tr>
</table>


Both variables are ordinal in this example. We need to convert this to a dataframe with
one count per line to enable model fitting.

\> (partyed <- as.data. frame. table (xtabs ( ~ PID + educ,
nes96)))
.etc ....


<table>
<tr>
<th></th>
<th>PID</th>
<th>educ</th>
<th>Freq</th>
</tr>
<tr>
<td>1</td>
<td>strDem</td>
<td>MS</td>
<td>5</td>
</tr>
<tr>
<td>2</td>
<td>weakDem</td>
<td>MS</td>
<td>4</td>
</tr>
<tr>
<td>3</td>
<td>indDem</td>
<td>MS</td>
<td>1</td>
</tr>
</table>


If we fit a nominal-by-nominal model, we find no evidence against independence:

\> nomod <- glm (Freq ~ PID + educ, partyed, family=
poisson)

<!-- PageBreak -->

<!-- PageHeader="Contingency tables 99" -->

\> pchisq (deviance (nomod) , df . residual (nomod) , lower=F)
[1] 0.26961

However, we can take advantage of the ordinal structure of both variables and define
some scores. As there seems to be no strong reason to the contrary, we assign evenly
spaced scores: one to seven for both PID and educ:

$$> \mathrm { p a r t y e d s o p I D } < - \mathrm { u n c l a s s } \left( \mathrm { p a r t y e d } \mathrm { s p l } \right)$$
$$> \mathrm { p a r t y e d s o e d u c } < - \mathrm { u n c l a s s } \left( \mathrm { p a r t y e d s e d u c } \right)$$

Now fit the linear-by-linear association model and compare to the independence model:

\> ormod <- glm (Freq ~ PID + educ + I (oPID*oeduc) ,
partyed,
family= poisson)
> anova (nomod, ormod, test="Chi")
Analysis of Deviance Table
Model 1: Freq ~ PID + educ
Model 2: Freq ~ PID + educ + I (OPID * oeduc)


<table>
<tr>
<th></th>
<th>Resid. Df</th>
<th>Resid. Dev</th>
<th>Df</th>
<th>Deviance</th>
<th>P(&gt;|Chi|)</th>
</tr>
<tr>
<td>1</td>
<td>36</td>
<td>40.7</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>35</td>
<td>30.6</td>
<td>1</td>
<td>10.2</td>
<td>0.0014</td>
</tr>
</table>


We see that there is some evidence of an association. So we see that using the ordinal
information gives us more power to detect an association. We can examine $\widehat { \gamma }$

\> summary (ormod) $coef [ ' I (oPID * oeduc) ' , ]
Estimate Std. Error
z value
Pr(>|z|)
0.0287446 0.0090617 3.1720850 0.0015135

We see that $\widehat { \gamma } _ { \mathrm { i s } }$ 0.0287. The p-value here can also be used to test the significance of the
association although, as a Wald test, it is less reliable than the likelihood ratio test we
used first. We see that $\mathfrak{f}$ Yis positive, which, given the way that we have assigned the
scores, mean that a higher level of education is associated with a greater probability of
tending to the Republican end of the spectrum.

Just to check the robustness of the assignment of the scores, it is worth trying some
different choices. For example, suppose we choose scores so that there is more of a
distinction between Democrats and Independents as well as Independents and
Republicans. Our assignment of scores for apid below achieves this. Another idea might
be that people who complete high school or less are not different; that those who go to
college, but do not get a BA degree are not different and that those who get a BA or
higher are not different. My assignment of scores in aedu achieves this:

\> apid <- c (1, 2, 5, 6, 7, 10, 11)
> aedu <- c (1, 1, 1, 2, 2, 3, 3)
> ormoda <- glm(Freq ~ PID + educ +
I(apid[oPID]*aedu[oeduc]),

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 100" -->

partyed, family= poisson)
\> anova (nomod, ormoda, test="Chi")
Analysis of Deviance Table
Model 1: Freq ~ PID + educ
Model 2: Freq ~ PID + educ + I (apid [ OPID] *
aedu [oeduc ] )


<table>
<tr>
<th></th>
<th>Resid. Df</th>
<th>Resid.</th>
<th>Dev</th>
<th>Df</th>
<th>Deviance</th>
<th>P(&gt;|Chi|)</th>
</tr>
<tr>
<td>1</td>
<td>36</td>
<td></td>
<td>40.7</td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>2</td>
<td>35</td>
<td></td>
<td>30.9</td>
<td>1</td>
<td colspan="2">9.8 0.0017</td>
</tr>
</table>


The numerical outcome is slightly different, but the result is still significant. Some
experimentation with other plausible choices indicates that we can be fairly confident
about the association here.

The association parameter may be interpreted in terms of log-odds. For example,
consider the log-odds ratio for adjacent entries in both rows and columns:

$$\log \frac { A i j k + 1 , j + 1 } { H _ { i , j + 1 } } = i \left( u _ { i + 1 } - u _ { i } \right) \left( v _ { j + 1 } - v _ { j } \right)$$

For evenly spaced scores, these log-odds ratios will all be equal. For our example, where
the scores are spaced one apart, the log-odds ratio is $\gamma .$ To illustrate this point, consider
the fitted values under the linear-by-linear association model:

\> round (xtabs (predict (ormod, type="response") ~ PID +
educ, partyed) , 2)
educ


<table>
<tr>
<th>PID</th>
<th>MS</th>
<th>HSdrop</th>
<th>HS</th>
<th>Coll</th>
<th>CCdeg</th>
<th>BAdeg</th>
<th>MAdeg</th>
</tr>
<tr>
<td>strDem</td>
<td>3.58</td>
<td>13.36</td>
<td>59.22</td>
<td>41.34</td>
<td>18.34</td>
<td>42.46</td>
<td>21.71</td>
</tr>
<tr>
<td>weakDem</td>
<td>2.92</td>
<td>11.22</td>
<td>51.20</td>
<td>36.78</td>
<td>16.80</td>
<td>40.02</td>
<td>21.06</td>
</tr>
<tr>
<td>indDem</td>
<td>1.59</td>
<td>6.27</td>
<td>29.45</td>
<td>21.78</td>
<td>10.23</td>
<td>25.09</td>
<td>13.59</td>
</tr>
<tr>
<td>indind</td>
<td>0.49</td>
<td>2.00</td>
<td>9.65</td>
<td>7.34</td>
<td>3.55</td>
<td>8.96</td>
<td>5.00</td>
</tr>
<tr>
<td>indRep</td>
<td>1.12</td>
<td>4.71</td>
<td>23.41</td>
<td>18.33</td>
<td>9.13</td>
<td>23.70</td>
<td>13.60</td>
</tr>
<tr>
<td>weakRep</td>
<td>1.61</td>
<td>6.95</td>
<td>35.59</td>
<td>28.68</td>
<td>14.69</td>
<td>39.28</td>
<td>23.19</td>
</tr>
<tr>
<td>strRep</td>
<td>1.69</td>
<td>7.49</td>
<td>39.48</td>
<td>32.74</td>
<td>17.26</td>
<td>47.49</td>
<td>28.85</td>
</tr>
</table>


Now compute log-odds ratio for, say, the lower two-by-two table:

\> log(39.28\*28.85/ (47.49\*23.19) )
[1] 0.028585

We see this is, but for rounding, equal to Y-

It is always worth examining the residuals to check if there is more structure than the
model suggests. We use the raw response residuals (the unscaled difference between
observed and expected) because we would like to see effects which are large in an
absolute sense.

\> round (xtabs (residuals (ormod, type="response") ~ PID +
educ, partyed) , 2)
educ

<!-- PageBreak -->

<!-- PageNumber="101" -->
<!-- PageHeader="Contingency tables" -->


<table>
<tr>
<th>PID</th>
<th>MS</th>
<th>HSdrop</th>
<th>HS</th>
<th>Coll</th>
<th>CCdeg</th>
<th>BAdeg</th>
<th>MAdeg</th>
</tr>
<tr>
<td>strDem</td>
<td>1.42</td>
<td>5.64</td>
<td>-0.22</td>
<td>-3.34</td>
<td>-1.34</td>
<td>-2.46</td>
<td>0.29</td>
</tr>
<tr>
<td>weakDem</td>
<td>1.08</td>
<td>-1.22</td>
<td>-2.20</td>
<td>-0.78</td>
<td>0.20</td>
<td>0.98</td>
<td>1.94</td>
</tr>
<tr>
<td>indDem</td>
<td>-0.59</td>
<td>-2.27</td>
<td>-1.45</td>
<td>-6.78</td>
<td>2.77</td>
<td>1.91</td>
<td>6.41</td>
</tr>
<tr>
<td>indind</td>
<td>-0.49</td>
<td>1.00</td>
<td>2.35</td>
<td>1.66</td>
<td>-0.55</td>
<td>-2.96</td>
<td>-1.00</td>
</tr>
<tr>
<td>indRep</td>
<td>0.88</td>
<td>2.29</td>
<td>-0.41</td>
<td>-2.33</td>
<td>-1.13</td>
<td>-1.70</td>
<td>2.40</td>
</tr>
<tr>
<td>weakRep</td>
<td>-1.61</td>
<td>-1.95</td>
<td>-0.59</td>
<td>11.32</td>
<td>0.31</td>
<td>-1.28</td>
<td>-6.19</td>
</tr>
<tr>
<td>$\mathrm { s t r R e } \mathrm { r }$</td>
<td>-0.69</td>
<td>-3.49</td>
<td>2.52</td>
<td>0.26</td>
<td>-0.26</td>
<td>5.51</td>
<td>-3.85</td>
</tr>
</table>


We do see some indications of remaining structure. For example, we see many more
weak Republicans with some college than expected while fewer Republicans with
master's degrees or higher. There may not be a monotone relationship between party
affiliation and educational level.

To investigate this effect, we might consider an ordinal-by-nominal model where we
now treat education as a nominal variable. This is called a column effects model because
the columns (which are the education levels here) are not assigned scores and we will
estimate their effect instead. A row effects model is effectively the same model except
with the roles of the variables reversed. The model takes the form:

$$\log E Y _ { i j } = \log \mu _ { i j } = \log n p _ { i j } = \log n + a _ { i } + \beta _ { j } + u _ { i } \gamma _ { j }$$

where the $\gamma _ { j }$ are called the column effects. Equality of the $\gamma _ { j \mathrm { S } }$ corresponds to the
hypothesis of independence. We fit this model for our data:

\> cmod <- glm (Freq ~ PID + educ + educ : oPID, partyed,
family= poisson)

We can compare this to the independence model:

\> anova (nomod, cmod, test="Chi")
Analysis of Deviance Table
Model 1: Freq ~ PID + educ

Model 2: Freq ~ PID + educ + educ : oPID
Resid. Df Resid. Dev Df Deviance P(>|Chi|)

36
40.7

1
2

30
22.8 6
18.0
0.0063

We find that the column-effects model is preferred. Now examine the fitted coefficients,
looking at just the interaction terms as the main effects have no particular interest:

\> summary (cmod) $coef [14 : 19, ]


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
</tr>
<tr>
<td>Pr $\left( > | z | \right)$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>educMS:oPID</td>
<td>-0.3122169</td>
<td>0.154051</td>
<td>-2.026710</td>
</tr>
<tr>
<td>0.042692</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>educHSdrop:oPID</td>
<td>-0.1944513</td>
<td>0.077228</td>
<td>-2.517891</td>
</tr>
<tr>
<td>0.011806</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>educHS:oPID</td>
<td>-0.0553470</td>
<td>0.048196</td>
<td>-1.148384</td>
</tr>
<tr>
<td>0.250810</td>
<td colspan="2"></td>
<td></td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="102" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->


<table>
<tr>
<td>educColl:oPID</td>
<td>0.0044605</td>
<td>0.050603</td>
<td>0.088147</td>
</tr>
<tr>
<td>0.929760</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>educCCdeg:oPID</td>
<td>-0.0086994</td>
<td>0.060667</td>
<td>-0.143395</td>
</tr>
<tr>
<td>0.885978</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>educBAdeg:oPID</td>
<td>0.0345539</td>
<td>0.048782</td>
<td>0.708330</td>
</tr>
<tr>
<td>0.478740</td>
<td></td>
<td colspan="2"></td>
</tr>
</table>


The last coefficient, educMAdeg: oPID, is not identifiable and so this may be taken as
zero. If there was really a monotone trend in the effect of educational level on party
affiliation, we would expect these coefficients to be monotone. However, we can see that
they are not. However, if we compare this to the linear-by-linear association model:

\> anova (ormod, cmod, test="Chi")
Analysis of Deviance Table
Model 1: Freq ~ PID + educ + I (oPID * oeduc)
Model 2: Freq ~ PID + educ + educ : oPID


<table>
<tr>
<th></th>
<th>Resid.</th>
<th>Df</th>
<th>Resid. Dev</th>
<th>Df</th>
<th>Deviance</th>
<th>P(&gt;|Chi|)</th>
</tr>
<tr>
<td>1</td>
<td></td>
<td>35</td>
<td>30.57</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td></td>
<td>30</td>
<td>22.76</td>
<td>5</td>
<td>7.81</td>
<td>0.17</td>
</tr>
</table>


We see that the simpler linear-by-linear association is preferred to the more complex
column-effects model. Nevertheless, if the linear-by-linear association were a good fit,
we would expect the observed column-effect coefficients to be roughly evenly spaced.
Looking at these coefficients, we observe that for high school and above, the coefficients
are not significantly different from zero while for the lowest two categories, there is some
difference. This suggests an alternate assignment of scores for education:

\> aedu <- 0 (1, 1, 2, 2, 2, 2, 2)
> ormodb <- glm(Freq ~ PID + educ + I
(oPID*aedu[oeduc]),
partyed, family= poisson)
> deviance (ormodb)
[1] 28.451
> deviance (ormod)
[1] 30.568

We see that the deviance of this model is even lower than our original model. This gives
credence to the view that whether a person finishes high school or not is the determining
factor in party affiliation. However, since we used the data itself to assign the scores and
come up with this hypothesis, we would be tempting fate to then use the data again to test
this hypothesis.

The use of scores can be helpful in reducing the complexity of models for categorical
data with ordinal variables. It is especially useful in higher dimensional tables where a
reduction in the number of parameters is particularly welcome. The use of scores can also
sharpen our ability to detect associations.

Further Reading: See books by Agresti (2002), Bishop, Fienberg, and Holland
(1975), Haberman (1977), Le (1998), Leonard (2000), Powers and Xie (2000), Santner
and Duffy (1989) and Simonoff (2003).

<!-- PageBreak -->

<!-- PageNumber="103" -->
<!-- PageHeader="Contingency tables" -->


## Exercises

1\. The dataset parstum contains cross-classified data on marijuana usage by college
students as it relates to the alcohol and drug usage of the parents. Analyze the data as
if both factors were nominal. Redo the analysis treating both factors as ordinal.
Contrast the results.

2\. The dataset melanoma gives data on a sample of patients suffering from melanoma
(skin cancer) cross-classified by the type of cancer and the location on the body.
Determine whether the type and location are independent. Examine the residuals to
determine whether any dependence can be ascribed to particular type/location
combinations.

3\. Data on social mobility of men in the UK may be found in cmob. A sample of men
aged 45-64 was drawn from the 1971 census and 1981 census and the social class of
the man was recorded at each timepoint. The classes are I=professional,
II=semiprofessional, IIIN=skilled nonmanual, HIM=skilled manual, $I V = s e m i s k i l l e d ,$
$\mathrm { V } = \mathrm { u n s k i l l e d } .$

(a) Check for symmetry, quasi-symmetry, marginal homogeneity and quasi-
independence.

(b) Develop a score-based model. Find some good-fitting scores.

4\. The dataset death contains data on murder cases in Florida in 1977. The data is cross-
classified by the race (black or white) of the victim, of the defendant and whether the
death penalty was given.

(a) Consider the frequency with which the death penalty is applied to black and white
defendants, both marginally and conditionally, with respect to the race of the
victim. Is this an example of Simpson's paradox? Are the observed differences in
the frequency of application of the death penalty statistically significant?

(b) Determine the most appropriate dependence model between the variables.

(c) Fit a binomial regression with death penalty as the response and show the
relationship to your model in the previous question.

5\. The dataset sex fun comes from a questionnaire from 91 couples in the Tucson,
Arizona, area. Subjects answered the question "Sex is fun for me and my partner". The
possible answers were "never or occasionally", "fairly often", "very often" and
"almost always".

(a) Check for symmetry, quasi-symmetry, marginal homogeneity and quasi-
independence.

(b) Develop a score-based model. Find some good-fitting scores.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 104" -->

6\. The dataset suicide contains one year of suicide data from the United Kingdom cross-
classified by sex, age and method.

(a) Determine the most appropriate dependence model between the variables.

(b) Collapse the sex and age of the subject into a single six-level factor containing all
combinations of sex and age. Conduct a correspondence analysis and give an
interpretation of the plot.

(c) Repeat the correspondence analysis separately for males and females. Does this
analysis reveal anything new compared to the combined analysis in the previous
question?

7\. A student newspaper conducted a survey of student opinions about the Vietnam War in
May 1967. Responses were classified by sex, year in the program and one of four
opinions. The survey was voluntary. The data may be found in the dataset uncviet.

(a) Conduct an analysis of the patterns of dependence in the data assuming that all
variables are nominal.

(b) Assign scores to the year and opinion and fit an appropriate model. Interpret the
trends in opinion over the years. Check the sensitivity of your conclusions to the
assignment of the scores.

8\. The dataset HairEyeColor contains the same data analyzed in this chapter as haireye.
Repeat the analysis in the text for each sex and make a comparison of the conclusions.

9\. A sample of psychiatry patients were cross-classified by their diagnosis and whether a
drug treatment was prescribed. The data may be found in drugpsy. Is the chance that
drugs will be prescribed constant across diagnoses?

10\. The UCBadmissions dataset presents data on applicants to graduate school at
Berkeley for the six largest departments in 1973 classified by admission and sex.

(a) Show that this provides an example of Simpson's paradox.

(b) Determine the most appropriate dependence model between the variables.

(c) Fit a binomial regression with admissions status as the response and show the
relationship to your model in the previous question.

<!-- PageBreak -->

<!-- PageBreak -->


## CHAPTER 5 Multinomial Data

The multinomial distribution is an extension of the binomial to the situation where the
response can take more than two values. Let $Y _ { i }$ be a random variable that takes one of a
finite number of values, 1, $2 , \ldots , J .$ Let $p _ { i j } = P \left( Y _ { i } = j \right)$ so $\sum _ { j = 1 } ^ { J } p _ { i j } = 1 .$
As with binary data
(the case where $J =$ 2), we may encounter both grouped and ungrouped data. Let $Y _ { \dot { y } }$ be the
number of observations falling into category $j$ for group or individual $i$ and let $n _ { i } = \sum _ { j } Y _ { i j }$
For ungrouped data, $n _ { i } = 1$ and one and only one of $\mathcal{Y} _ { i 1 } , \ldots , Y _ { i J }$ is equal to one and the rest
are zero. The $Y _ { i j } ,$ conditional on the total $n _ { i } ,$ follow a multinomial distribution:

$$P \left( Y _ { i 1 } = y _ { i 1 } , \ldots , Y _ { i J } = y _ { i J } \right) = \frac { n _ { i } } { y _ { i 1 } ! \cdots y _ { i J } ! } p _ { i 1 } ^ { y _ { i 1 } } \cdots p _ { i J } ^ { y _ { i j } }$$

We must also distinguish between nominal multinomial data where there is no natural
order to the categories and ordinal multinomial data where there is an order. The
multinomial logit model is intended for nominal data. It can be used for ordinal data, but
the information about order will not be used.


### 5.1 Multinomial Logit Model

As with the binomial logit model, we must find a way to link the probabilities $p _ { \dot { y } }$ to the
predictors $x _ { i } ,$ while ensuring that the probabilities are restricted between zero and one.
We can use a similar idea:

$$\eta _ { i j } = x _ { i } ^ { T } \beta _ { j } = \log \frac { p _ { i j } } { p _ { i 1 } } , \quad j = 2 , \ldots , J$$

We must obey the constraint that $\sum _ { i = 1 } ^ { J } p _ { i j } = 1$ 1,so it is convenient to declare one of the
categories as the baseline, say, $j = 1 .$ So we set
$p _ { i 1 } = 1 - \sum _ { j = 2 } ^ { J } p _ { i j }$ have:

$$p _ { i j } = \frac { e x p \left( \eta _ { i j } \right) } { 1 + \sum _ { j = 2 } ^ { J } e x p \left( \eta _ { i j } \right) }$$

Note that $\eta _ { i 1 } = 0 .$ We may estimate the parameters of this model using maximum
likelihood and then use the standard methods of inference.

Consider an example drawn from a subset of the 1996 American National Election
Study (Rosenstone, Kinder, and Miller (1997)). For simplicity, we consider only the age,
education level and income group of the respondents. Our response will be party
identification of the respondent: Democrat, Independent or Republican. The original data

<!-- PageBreak -->

<!-- PageNumber="107" -->
<!-- PageHeader="Multinomial data" -->

involved more than three categories; we collapse this to three, again for simplicity of the
presentation.

\> data (nes96)
> SPID <- nes96$PID
> levels (sPID) <-

c ( "Democrat", "Democrat", "Independent", "Independent",
"Independent", "Republican", "Republican")

\> summary (sPID)
Democrat Independent Republican
380
239
325

\> inca <-
c (1. 5, 4, 6, 8, 9. 5, 10 . 5, 11. 5, 12 . 5, 13. 5, 14. 5, 16, 18 . 5, 21, 23 .
5,
27.5, 32.5, 37.5, 42.5, 47.5, 55, 67.5, 82.5, 97.5, 115)
> nincome <- inca [unclass (nes96$income) ]
> summary (nincome)


<table>
<tr>
<th>Min.</th>
<th>1st Qu.</th>
<th>Median</th>
<th>Mean</th>
<th>3rd Qu.</th>
<th>Max.</th>
</tr>
<tr>
<td>1.5</td>
<td>23.5</td>
<td>37.5</td>
<td>46.6</td>
<td>67.5</td>
<td>115.0</td>
</tr>
</table>


\> table (nes96$educ)


<table>
<tr>
<th>MS</th>
<th>HSdrop</th>
<th>HS</th>
<th>Coll</th>
<th>CCdeg</th>
<th>BAdeg</th>
<th>MAdeg</th>
</tr>
<tr>
<td>13</td>
<td>52</td>
<td>248</td>
<td>187</td>
<td>90</td>
<td>227</td>
<td>127</td>
</tr>
</table>


The income variable in the original data was an ordered factor with income ranges. We
have converted this to a numeric variable by taking the midpoint of each range.

Let's start with a graphical look at the relationship between the predictors and the
response. The response is at the individual level and so we need to group the data just to
get a sense of how the party identification is associated with the predictors. We cut the
age and income predictors into seven levels and used the approximate midpoints of the
ranges to label the groups:

\>
matplot (prop. table (table (nes96$educ, sPID) , 1) , type="1",
xlab="Education", ylab="Proportion", lty=c (1, 2, 5) )
\> cutinc <- cut (nincome, 7)
> il <- c (8, 26, 42, 58, 74, 90, 107)
> matplot (il, prop.table
(table (cutinc, sPID) , 1) , lty=c (1, 2, 5) ,
type="1", ylab="Proportion", xlab="Income")
> cutage <- cut (nes 96$age, 7)
> al <- c (24, 34, 44, 54, 65, 75, 85)
>
matplot(al,prop.table(table(cutage,sPID),1),lty=c(1,2,5
) ,
type="1", ylab="Proportion", xlab="Age")

The plots are shown in Figure 5.1. We see that proportion of Democrats falls with
educational status, reaching a plateau for the college educated. We see the proportion of
Republicans rising with educational level and reaching a similar plateau. As income
increases, we observe an increase in the proportion of Republicans and Independents and

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 108" -->

a decrease in the proportion of Democrats. The relationship of party to age is not clear.
This is cross-sectional rather than longitudinal data, so we cannot say anything about
what might happen to an individual with, for example, increasing income. We can only
expect to make conclusions about the relative probability of party affiliations for different
individuals with different incomes.

We might ask whether the trends we see in the observed proportions are statistically
significant. We need to model the data to answer this question. We fit a multinomial logit
model. The multinom function is part of the nnet package described in Venables and
Ripley (2002):

library (nnet)


<figure>
<figcaption>Figure 5.1 Relationship between party affiliation and education, age and income. Democrats are shown with solid line, Republicans with a dashed line and Independents with a dotted line. Education is categorized into seven levels described in the text. Income is in thousands of dollars.</figcaption>

020 055 0.30 035 0.40 045 050 05

06

0.45

0.40

Proportion

04

Proportion

Proportion

35

20

?

0.20

H

5

20

40

00

100

30 40 50 00 70 00

Education

</figure>


\> mmod <- multinom (sPID ~ age + educ + nincome, nes96)
\# weights: 30 (18 variable)

initial value 1037.090001

iter 10 value 990.568608

$\mathrm { i t } \mathrm { e r }$ 20 value 984.319052

final value 984.166272
converged

The program uses the optimization method from the neural net trainer in nnet to compute
the maximum likelihood, but there is no deeper connection to neural networks.

<!-- PageBreak -->

<!-- PageNumber="109" -->
<!-- PageHeader="Multinomial data" -->

We can select which variables to include in the model based the $\mathrm { A I C }$ criterion using a
step wise search method (output edited to show only the decision information):


<table>
<tr>
<th colspan="3">&gt; mmodi &lt;- step (mmod)</th>
</tr>
<tr>
<th></th>
<th>Df</th>
<th>AIC</th>
</tr>
<tr>
<td>- educ</td>
<td>6</td>
<td>1996.5</td>
</tr>
<tr>
<td>- age</td>
<td>16</td>
<td>2003.6</td>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td>18</td>
<td>2004.3</td>
</tr>
<tr>
<td>- nincome</td>
<td>16</td>
<td>2045.9</td>
</tr>
<tr>
<td></td>
<td>Df</td>
<td>AIC</td>
</tr>
<tr>
<td>- age</td>
<td>4</td>
<td>1993.4</td>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td>6</td>
<td>1996.5</td>
</tr>
<tr>
<td>- nincome</td>
<td>4</td>
<td>2048.9</td>
</tr>
<tr>
<td></td>
<td>Df</td>
<td>AIC</td>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td>4</td>
<td>1993.4</td>
</tr>
<tr>
<td>- nincome</td>
<td>2</td>
<td>2045.3</td>
</tr>
</table>


At the first stage of the search, we see that omitting education would be the best option to
reduce the AIC criterion. At the next step, age is removed resulting in a model with only
income.

We can also use the standard likelihood methods to derive a test to compare nested
models. For example, we can fit a model without education and then compare the
deviances:

\> mmode <- multinom (sPID ~ age + nincome, nes96)
> deviance (mmode) - deviance (mmod)
[1] 16.206
> pchisq (16.206, mmod$edf-mmode$edf, lower=F)
[1] 0.18198

We see that education is not significant relative to the full model. This may seem
somewhat surprising given the plot in Figure 5.1, but the large differences between
proportions of Democrats and Republicans occur for groups with low education which
represent only a small number of people.

We can obtain predicted values for specified values of income. For example, suppose
we pick the midpoints of the income groups we selected for the earlier plot:

\> predict (mmodi, $d a t a .$ frame (nincome=il) , type="probs")


<table>
<tr>
<th></th>
<th>Democrat</th>
<th>Independent</th>
<th>Republican</th>
</tr>
<tr>
<td>1</td>
<td>0.55663</td>
<td>0.19552</td>
<td>0.24786</td>
</tr>
<tr>
<td>2</td>
<td>0.48049</td>
<td>0.22546</td>
<td>0.29405</td>
</tr>
<tr>
<td>3</td>
<td>0.41343</td>
<td>0.25094</td>
<td>0.33564</td>
</tr>
<tr>
<td>4</td>
<td>0.34939</td>
<td>0.27432</td>
<td>0.37629</td>
</tr>
<tr>
<td>5</td>
<td>0.29033</td>
<td>0.29486</td>
<td>0.41481</td>
</tr>
<tr>
<td>6</td>
<td>0.23758</td>
<td>0.31211</td>
<td>0.45031</td>
</tr>
<tr>
<td>7</td>
<td>0.18917</td>
<td>0.32668</td>
<td>0.48415</td>
</tr>
</table>


We see that the probability of being Republican or Independent increases with income.
The default form just gives the most probable category:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 110

\> predict (mmodi, data. frame (nincome=il) )
[1]
Democrat
Democrat
Democrat
Republican
Republican

[6] Republican Republican

We may also examine the coefficients to gain an understanding of the relationship
between the predictor and the response:

\> summary (mmodi)
Coefficients:


<table>
<tr>
<th></th>
<th>(Intercept)</th>
<th>nincome</th>
</tr>
<tr>
<td>Independent</td>
<td>-1.17493</td>
<td>0.016087</td>
</tr>
<tr>
<td>Republican</td>
<td>-0.95036</td>
<td>0.017665</td>
</tr>
</table>


Std. Errors:


<table>
<tr>
<th></th>
<th>(Intercept)</th>
<th>nincome</th>
</tr>
<tr>
<td>Independent</td>
<td>0.15361</td>
<td>0.0028497</td>
</tr>
<tr>
<td>Republican</td>
<td>0.14169</td>
<td>0.0026525</td>
</tr>
<tr>
<td colspan="3">Residual Deviance: 1985.4</td>
</tr>
</table>


AIC: 1993.4

The intercept terms model the probabilities of the party identification for an income of
zero. We can see the relationship from this calculation:

\> cc <- c (0,-1.17493, -0.95036)
> exp (cc) / sum (exp (cc))
[1] 0.58982 0.18216 0.22802
> predict (mmodi, data. frame (nincome=0) , type="probs")
Democrat Independent Republican
0.58982
0.18216
0.22802

The slope terms represent the log-odds of moving from the baseline category of
Democrat to Independent and Republican, respectively, for a unit change of $1000 in
income. We can see more explicitly what this means by predicting probabilities for
incomes $1000 apart and then computing the log-odds:

\> (pp <-
predict (mmodi, data. frame (nincome=c (0, 1) ) , type="probs") )


<table>
<tr>
<th></th>
<th>Democrat</th>
<th>Independent</th>
<th>Republican</th>
</tr>
<tr>
<td>1</td>
<td>0.58982</td>
<td colspan="2">0.18216 0.22802</td>
</tr>
<tr>
<td>2</td>
<td>0.58571</td>
<td colspan="2">0.18382 0.23047</td>
</tr>
</table>


\> log(pp[1,1]*pp[2,2]/(pp[l,2]*pp[2,l]))
[1] 0.016087
> log (pp [1, 1 ] *pp [2, 3] / (pp[1, 3] *pp [2,1] ) )
[1] 0.017665

Log-odds can be difficult to interpret particularly with many predictors and interactions.
Sometimes, computing predicted probabilities for a selected range of predictors can
provide better intuition.

<!-- PageBreak -->

<!-- PageNumber="111" -->
<!-- PageHeader="Multinomial data" -->

It is possible to fit a multinomial logit model using a Poisson GLM. Recall that
independent Poisson variates conditional on their total are multinomial as described in
Section 3.1. We can exploit this fact by declaring a factor that has a level for each
multinomial observation in the data; we call this the response factor. We then treat the
individual components of the multinomial response as Poisson responses. For ungrouped
data, such as the current example, this means that one response will be one and the rest
zero.

We set up these variables, also illustrating what happens with the first four
individuals:

\> SPID [1 : 4]
[1] Republican Democrat Democrat
Democrat
Levels: Democrat Independent Republican
> cm <- diag (3) [unclass (sPID) , ]
> cm [1:4,]
[, 1] [,2] [,3]

1
$\left[ 2 , \right]$
1
0
[4,]
0
1
0

[1,]
[3,]
1

0
0
0

0
0
\> y <- as.numeric (t (cm) )
> resp. factor <- $g l \left( 9 4 4 , 3 \right)$

The three Poisson responses correspond to the different affiliations so we need to label
which is which:

$$> \text { cat. factor } < - \text { gl } \left( 3 , 1 , 3 * 9 4 4 , \text { labels } = c \left( ^ { \text { n } } D ^ { \prime \prime } , ^ { \prime \prime } I ^ { \prime \prime } \right. \right. ,$$
"R") )

We also need to replicate the predictor:

$$> r n i n c o m e < - \quad r e p \left( n i n c o m e , e a c h = 3 \right)$$

Now examine the form of the reorganized data:

\> head (data. frame (y, resp. factor, cat. factor, rnincome) )


<table>
<tr>
<th></th>
<th>y resp.</th>
<th>factor</th>
<th>cat. factor</th>
<th>rnincome</th>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
<td>D</td>
<td>1.5</td>
</tr>
<tr>
<td>2</td>
<td>0</td>
<td>1</td>
<td>I</td>
<td>1.5</td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>1</td>
<td>R</td>
<td>1.5</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>2</td>
<td>D</td>
<td>1.5</td>
</tr>
<tr>
<td>5</td>
<td>0</td>
<td>2</td>
<td>I</td>
<td>1.5</td>
</tr>
<tr>
<td>6</td>
<td>0</td>
<td>2</td>
<td>R</td>
<td>1.5</td>
</tr>
</table>


As with the contingency table models, the null model has only main effects:

\> nullmod <- glm(y ~ resp. factor + cat. factor,
family=poisson)

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 112" -->

The effect of income is modeled with an interaction with party affiliation:

\> glmod <- glm (y ~ resp. factor + cat. factor +
cat. factor : rnincome,
family=poisson)

We find that the deviance is the same as the multinomial model above:

\> deviance (glmod)
[1] 1985.4
> deviance (mmodi)
[1] 1985.4

The coefficients also correspond:

\> coef (glmod) [c (1, 945 : 949) ]
(Intercept)
cat.factorl
cat
. factorR
-0.5119613
-1.1749375
-
0.9503621
cat. factorD: rnincome cat. factorI : rnincome
cat. factorR: rnincome
-0.0176645
-

0.0015777
\> coef (mmodi)

NA


<table>
<tr>
<th></th>
<th>(Intercept)</th>
<th>nincome</th>
</tr>
<tr>
<td>Independent</td>
<td>-1.17493</td>
<td>0.016087</td>
</tr>
<tr>
<td>Republican</td>
<td>-0.95036</td>
<td>0.017665</td>
</tr>
</table>


The parameterization is slightly different for the Poisson GLM. Because only two
interaction parameters are identifiable, the last one, being inestimable, is not estimated.
This has the effect of making Republicans the reference level rather than Democrats as in
the multinomial model. We see that the sign of the Republican-Democrat contrast is
reversed and that we may obtain the Independent-Democrat contrast from the Poisson
GLM by computing:

\> 0.016087-0.017665
[1] -0.001578

So we may obtain the same results using the Poisson GLM, but the multinom function is
more transparent. However, the point is that the multinomial logit can be view as a GLM-
type model, which allows us to apply all the common methodology developed for GLMs.

<!-- PageBreak -->

<!-- PageNumber="113" -->
<!-- PageHeader="Multinomial data" -->


### 5.2 Hierarchical or Nested Responses

Consider the following data collected by Lowe, Roberts, and Lloyd (1971) by way of
McCullagh and Nelder (1989) concerning live births with deformations of the central
nervous system in south Wales:

\> data (cns)

\> cns


<table>
<tr>
<th></th>
<th>Area</th>
<th>NoCNS</th>
<th>An</th>
<th>Sp</th>
<th>Other</th>
<th>Water</th>
<th>Work</th>
</tr>
<tr>
<td>1</td>
<td>Cardiff</td>
<td>4091</td>
<td>5</td>
<td>9</td>
<td>5</td>
<td>110</td>
<td>NonManual</td>
</tr>
<tr>
<td>2</td>
<td>Newport</td>
<td>1515</td>
<td>1</td>
<td>7</td>
<td>0</td>
<td>100</td>
<td>NonManual</td>
</tr>
<tr>
<td>3</td>
<td>Swansea</td>
<td>2394</td>
<td>9</td>
<td>5</td>
<td>0</td>
<td>95</td>
<td>NonManual</td>
</tr>
<tr>
<td>4</td>
<td>GlamorganE</td>
<td>3163</td>
<td>9</td>
<td>14</td>
<td>3</td>
<td>42</td>
<td>NonManual</td>
</tr>
<tr>
<td>5</td>
<td>GlamorganW</td>
<td>1979</td>
<td>5</td>
<td>10</td>
<td>1</td>
<td>39</td>
<td>NonManual</td>
</tr>
<tr>
<td>6</td>
<td>GlamorganC</td>
<td>4838</td>
<td>11</td>
<td>12</td>
<td>2</td>
<td>161</td>
<td>NonManual</td>
</tr>
<tr>
<td>7</td>
<td>MonmouthV</td>
<td>2362</td>
<td>6</td>
<td>8</td>
<td>4</td>
<td>83</td>
<td>NonManual</td>
</tr>
<tr>
<td>8</td>
<td>MonmouthOther</td>
<td>1604</td>
<td>3</td>
<td>6</td>
<td>0</td>
<td>122</td>
<td>NonManual</td>
</tr>
<tr>
<td>9</td>
<td>Cardiff</td>
<td>9424</td>
<td>31</td>
<td>33</td>
<td>14</td>
<td>110</td>
<td>Manual</td>
</tr>
<tr>
<td>10</td>
<td>Newport</td>
<td>4610</td>
<td>3</td>
<td>15</td>
<td>6</td>
<td>100</td>
<td>Manual</td>
</tr>
<tr>
<td>11</td>
<td>Swansea</td>
<td>5526</td>
<td>19</td>
<td>30</td>
<td>4</td>
<td>95</td>
<td>Manual</td>
</tr>
<tr>
<td>12</td>
<td>GlamorganE</td>
<td>13217</td>
<td>55</td>
<td>71</td>
<td>19</td>
<td>42</td>
<td>Manual</td>
</tr>
<tr>
<td>13</td>
<td>GlamorganW</td>
<td>8195</td>
<td>30</td>
<td>44</td>
<td>10</td>
<td>39</td>
<td>Manual</td>
</tr>
<tr>
<td>14</td>
<td>GlamorganC</td>
<td>7803</td>
<td>25</td>
<td>28</td>
<td>12</td>
<td>161</td>
<td>Manual</td>
</tr>
<tr>
<td>15</td>
<td>MonmouthV</td>
<td>9962</td>
<td>36</td>
<td>37</td>
<td>13</td>
<td>83</td>
<td>Manual</td>
</tr>
<tr>
<td>16</td>
<td>MonmouthOther</td>
<td>3172</td>
<td>8</td>
<td>13</td>
<td>3</td>
<td>122</td>
<td>Manual</td>
</tr>
</table>


NoCNS indicates no central nervous system(CNS) malformation. An denotes
anencephalus while Sp denotes spina bifida and Other represents other malformations.
Water is water hardness and the subjects are categorized by the type of work performed
by the parents. We might consider a multinomial response with four categories. However,
we can see that most births suffer no malformation and so this category dominates the
other three. It is better to consider this as a hierarchical response as depicted in Figure
5.2. Now consider the multinomial $l i k e l i h o o d$ for the $i ^ { t h }$ observation which is proportional
to:

$$p _ { i 1 } ^ { y _ { i 1 } } p _ { i 2 } ^ { y _ { i 2 } } p _ { i 3 } ^ { y _ { i 3 } } p _ { i 4 } ^ { y _ { 4 } }$$

Define $p _ { i c } = p _ { i 2 } + p _ { i 3 } + p _ { i 4 }$ which is probability of a birth with some kind of CNS
malformation. We can then write the likelihood as:

$$p _ { i 1 } ^ { y _ { 1 } } p _ { i k } ^ { y _ { 2 } + y _ { i 3 } + y _ { i 4 } } \times \left( \frac { p _ { i 2 } } { p _ { i i } } \right) ^ { y _ { i 2 } } \left( \frac { p _ { i 3 } } { p _ { i i } } \right) ^ { y _ { i 3 } } \left( \frac { p _ { i 4 } } { p _ { i c } } \right) ^ { y _ { i 4 } }$$

The first part of the product is now a binomial likelihood for a CNS vs. NoCNS response.
The second part of the product is now a multinomial likelihood for the three CNS
categories conditional of the presence of CNS. For example, $p _ { i 2 } / p _ { i c }$ is the conditional
probability of an anencephalus birth given that a malformation has occurred for the $i ^ { t h }$
observation. We can now separately develop a binomial model for whether malformation
occurs and a multinomial model for the type of malformation.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 114" -->


<figure>
<figcaption>Figure 5.2 Hierarchical response for birth types.</figcaption>

Births

No CNS

$\sqrt { 5 }$

$A n$

$S p$

Other

</figure>


We start with the binomial model. First we accumulate the number of CNS births and
plot the data with the response on the logit scale as shown in the first panel of Figure 5.3:

\> cns$CNS <- cns$An+cns$Sp+cns$Other

\> plot(log(CNS/NoCNS) ~ Water, cns,
$p c h = a s .$ character (Work) )


<figure>
<figcaption>Figure 5.3 The first plot shows the empirical logits for the proportion of CNS births related to water hardness and profession $\left( M = M a n u a l , \right.$ $\left. N = N o n m a n u a l \right) .$ The second is a half- normal plot of the residuals of the chosen model</figcaption>

log(CNS/NoCNS)

-5.4 -5.2 -5.0 -4.8 -4.6

M

4
0.0 0.5 1.0 1.5 2.0 2.5

10

M

$M$

NN

$M$

M

M

Sorted Data

N

$M$

14

0

N

000

N

$N$

N

0000000000

N

40 60 80 1

100

140

0.0

0.5

1.0

1.5

Water

Half-normal quantiles

</figure>


<!-- PageBreak -->

<!-- PageNumber="115" -->
<!-- PageHeader="Multinomial data" -->

We observe that the proportion of CNS births falls with increasing water hardness and is
higher for manual workers. We observe one observation (manual, Newport) that may be
an outlier. Notice that the Area is confounded with the Water hardness, so we cannot put
both these predictors in our model. We try them both and compare:

\> binmodw <- glm (cbind (CNS, NoCNS) ~ Water + Work, cns,
family=binomial)
> binmoda <- glm (cbind (CNS, NoCNS) ~ Area + Work, cns,
family=binomial)
> anova (binmodw, binmoda, test="Chi")
Analysis of Deviance Table
Model 1: cbind (CNS, NoCNS) ~ Water + Work
Model 2: cbind (CNS, NoCNS) ~ Area + Work


<table>
<tr>
<th></th>
<th>Resid. Df</th>
<th>Resid.</th>
<th>Dev</th>
<th>Df</th>
<th>Deviance</th>
<th>P(&gt;|Chi|)</th>
</tr>
<tr>
<td>1</td>
<td>13</td>
<td></td>
<td>12.36</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>7</td>
<td colspan="2">3.08</td>
<td>6</td>
<td>9.29</td>
<td>0.16</td>
</tr>
</table>


One can view this test as a check for linear trend in the effect of water hardness. We find
that the simpler model using Water is acceptable. $A$ check for an interaction effect
revealed nothing significant although a look at the residuals is worthwhile:

$$> \mathrm { h a l f n o r m } \left( \mathrm { r e s i d u a l s } \left( \mathrm { b i n m o d w } \right) \right)$$

In the second plot of Figure 5.3, we see an outlier corresponding to Newport manual
workers. This case deserves closer examination. Finally, a look at the chosen model:

\> summary (binmodw)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>z value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-4.432580</td>
<td colspan="3">0.089789 -49.37</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>Water</td>
<td>-0.003264</td>
<td colspan="2">0.000968</td>
<td>-3.37</td>
<td>0.00075</td>
</tr>
<tr>
<td>WorkNonManual</td>
<td>-0.339058</td>
<td></td>
<td>0.097094</td>
<td>-3.49</td>
<td>0.00048</td>
</tr>
<tr>
<td colspan="6">(Dispersion parameter for binomial family taken to be</td>
</tr>
<tr>
<td>1)</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">Null deviance: 41.047</td>
<td></td>
<td colspan="2">on 15 degrees of</td>
<td>freedom</td>
</tr>
<tr>
<td colspan="2">Residual deviance: 12.363</td>
<td colspan="3">on 13 degrees of</td>
<td>freedom</td>
</tr>
<tr>
<td>AIC: 102.5</td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
</table>


The residual deviance is close to the degrees of freedom indicating a reasonable fit to the
data. We see that since:

\> exp (-0.339058)
[1] 0.71244

births to nonmanual workers have a 29% lower chance of CNS malformation. Water
hardness ranges from about 40 to 160. So a difference of 120 would decrease the odds of
CNS malformation by about 32%.

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 116

Now consider a multinomial model for the three malformation types conditional on a
malformation having occurred. As this data is grouped, in contrast to the nes96 example,
it is most convenient to present the response as a matrix:

$$> \mathrm { c m m o d } < - \mathrm { m u l t i n o m } \left( \mathrm { c b i n d } \left( \mathrm { A n } _ { \prime } , \mathrm { S p } _ { \prime } , \mathrm { O t h e r } \right) \sim \mathrm { W a t e r } + \mathrm { W o r k } _ { \prime } \right. ,$$

cns)

We find that neither predictor has much effect:

\> nmod <- step (cmmod)


<table>
<tr>
<th></th>
<th>Df</th>
<th>AIC</th>
</tr>
<tr>
<td>- Water</td>
<td>4</td>
<td>1381.1</td>
</tr>
<tr>
<td>- $\mathrm { W o r k }$</td>
<td>4</td>
<td>1381.2</td>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td>6</td>
<td>1383.5</td>
</tr>
<tr>
<td></td>
<td>Df</td>
<td>AIC</td>
</tr>
<tr>
<td>- $\mathrm { W o r k }$</td>
<td>2</td>
<td>1378.5</td>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td>4</td>
<td>1381.1</td>
</tr>
</table>


which leaves us with a null final model:

\> nmod
Coefficients :

(Intercept)
$\mathrm { S p }$
0.28963
Other
-0.98083
Residual Deviance: 1374.5

The fitted proportions are:

\> cc <- c (0,0.28963, -0.98083)
> names (cc) <- c ("An", "Sp", "Other")
> exp (cc) / sum (exp (cc) )
An
Sp Other
0.36888 0.49279 0.13833

So we find that water hardness and parents' profession are related to the probability of a
malformed birth, but that they have no effect on the type of malformation.

Observe that if we fit a multinomial logit model to all four categories:

\> multinom (cbind (NoCNS, An, Sp, Other) ~ Water + Work,
cns)
Coefficients :


<table>
<tr>
<th></th>
<th>(Intercept)</th>
<th>Water</th>
<th>WorkNonManual</th>
</tr>
<tr>
<td>An</td>
<td>-5.4551</td>
<td>-0.00290884</td>
<td>-0.36388</td>
</tr>
<tr>
<td>Sp</td>
<td>-5.0710</td>
<td>-0.00432305</td>
<td>-0.24359</td>
</tr>
<tr>
<td>Other</td>
<td>-6.5947</td>
<td>-0.00051358</td>
<td>-0.64219</td>
</tr>
</table>


Residual Deviance: 9391

AIC: 9409

<!-- PageBreak -->

<!-- PageNumber="117" -->
<!-- PageHeader="Multinomial data" -->

We find that both Water and Work are significant, but that the fact that they do not
distinguish the type of malformation is not easily discovered from this model.


### 5.3 Ordinal Multinomial Responses

Suppose we have $J$ ordered categories and that for individual $i ,$ with ordinal response $Y _ { i } ,$
$p _ { i j } = P \left( Y _ { i } = j \right)$ for $j = 1 , \ldots , J .$ With an ordered response, it is often easier to work with the
cumulative probabilities, $\gamma _ { \mathrm { i j } } = P \left( Y _ { i } \leq j \right) .$ The cumulative probabilities are increasing and
invariant to combining adjacent categories. Furthermore, $\gamma _ { i } = 1 ,$ so we need only model $J -$
1 probabilities.

As usual, we must link the $\gamma \mathrm { s }$ to the $c o v a r i a t e s \quad x .$ We will consider three possibilities
which all take the form:

$$g \left( r _ { i j } \right) = \theta _ { j } - x _ { i } ^ { T } \beta$$

We will consider three possibilities for the link function $\mathrm { g } :$ the logit, the probit and the
complementary log-log. Notice that we have explicitly specified the intercepts, $\theta _ { j } ,$ so that
the vector $x _ { i }$ not include an intercept. Furthermore, ß does not depend on j so that we
assume that the predictors have a uniform effect on the response categories in a sense that
we will shortly make clear.

Suppose that $Z _ { i }$ is some unobserved continuous variable that might be thought of as
the real underlying latent response. We only observe a discretized version of $Z _ { i }$ in the
form of $Y _ { i }$ where $Y _ { i } = j$ is observed if $\theta _ { j - 1 } < Z _ { i } \leq \theta _ { j } .$ Further suppose that $Z _ { i } - \beta ^ { T } x _ { i }$ has
distribution $F$ then:

$$P \left( Y _ { i } \leq j \right) = P \left( Z _ { i } \leq \theta _ { j } \right) = P \left( Z _ { i } - \beta ^ { T } x _ { i } \leq \theta _ { j } - \beta ^ { T } x _ { i } \right) = F \left( \theta _ { j } - \beta ^ { T } x _ { i } \right)$$

Now if, for example, $F$ follows the logistic distribution, where $F \left( x \right) = e ^ { x } / \left( 1 + e ^ { x } \right) ,$ then:

$$\gamma _ { i j } = \frac { e x p \left( \theta _ { j } - \beta ^ { T } x _ { i } \right) } { 1 + e x p \left( \theta _ { j } - \beta ^ { T } x _ { i } \right) }$$

and so we would have a logit model for the cumulative probabilities $\gamma _ { i } .$ Choosing the
normal distribution for the latent variable leads to a probit model while the choice of an
extreme value distribution leads to the complementary $\log - \log .$ This latent variable
explanation for the model is displayed in Figure 5.4. Notice that $\mathrm { i f } \beta > 0 ,$ as $x _ { i }$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 11" -->


<figure>
<figcaption>Figure 5.4 Latent variable view of an ordered multinomial response. Here, four discrete response can occur, depending on the position of $Z$ relative to the cutpoints $\theta j .$ As $x$ changes, the cutpoints will move together to change the relative probabilities of the four responses.</figcaption>

$\theta _ { 1 }$

$\theta _ { 2 }$

$\theta _ { 3 }$

</figure>


grid moves $a s \quad x \quad c h a n g e s$

increases, $P \left( Y _ { i } = J \right)$ will also increase. This explains the use of the minus sign in the
definition of the model because it allows for the more intuitive interpretation of the sign
of B.

Proportional Odds Model: Let $\gamma _ { i } \left( x _ { i } \right) = P \left( Y _ { i } \leq J | x _ { i } \right)$ then the proportional odds model,
which uses the logit link, is:

$$\log \frac { \gamma _ { j } \left( x _ { i } \right) } { 1 - \gamma _ { j } \left( x _ { i } \right) } = \theta _ { j } - \beta ^ { T } x _ { i } , \quad j = 1 , \ldots , J - 1$$

It is so called because the relative odds for $y \leq j$ comparing $x _ { 1 }$ and $x _ { 2 }$ are:

$$\left( \frac { \gamma _ { j } \left( x _ { 1 } \right) } { 1 - \gamma _ { j } \left( x _ { 1 } \right) } \right) / \left( \frac { \gamma _ { j } \left( x _ { 2 } \right) } { 1 - \gamma _ { j } \left( x _ { 2 } \right) } \right) = \exp \left( - \beta ^ { T } \left( x _ { 1 } - x _ { 2 } \right) \right)$$

This does not $d e p e n d \quad o n \quad j .$ Of course, the assumption of proportional odds does need to
be checked for a given dataset.

Returning to the nes96 dataset, suppose we assume that Independents fall somewhere
between Democrats and Republicans. We would then have an ordered multinomial

<!-- PageBreak -->

<!-- PageNumber="119" -->
<!-- PageHeader="Multinomial data" -->

response. We can then fit this using the polr function from the MASS library described in
Venables and Ripley (2002):

\> library (MASS)
> pomod <- polr (sPID ~ age + educ + nincome, nes96)

The deviance and number of parameters for this model are:

$$> c \left( d e v i a n c e \left( p o m o d \right) , p o m o d e d f \right)$$

[1] 1984.2 10.0

which can be compared to the corresponding multinomial logit model:

\> c (deviance (mmod) , mmod$edf)
[1] 1968.3
18.0

The proportional odds model uses fewer parameters, but does not fit quite as well.
Typically, the output from the proportional odds model is easier to interpret. We may use
an AlC-based variable selection method:

\> pomodi <- step (pomod)
Start: AIC= 2004.2
SPID ~ age + educ + nincome
Df AIC

\- educ
6 2003

<none>
2004
- age
1 2004

\- nincome
1 2039
Step: AIC= 2002.8
SPID ~ age + nincome
Df AIC

\- age
1 2001

<none>
2003
- nincome 1 2047
Step: AIC= 2001.4
SPID ~ nincome


<table>
<tr>
<th></th>
<th>Df AIC</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td>2001</td>
</tr>
<tr>
<td>- nincome</td>
<td>1 2045</td>
</tr>
</table>


Thus we finish with a model including just income as we did with the earlier multinomial
model. We could also use a likelihood ratio test to compare the models:

\> deviance (pomodi) -deviance (pomod)
[1] 11.151
> pchisq (11. 151, pomod$edf-pomodi$edf, lower=F)
[1] 0.13217

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 120

We see that the simplification to just income is justifiable. We can check the proportional
odds assumption by computing the observed odds proportions with respect to, in this
case, income levels. We have computed the log-odds difference between $\gamma _ { 1 }$ and $\gamma _ { 2 } :$

\> pim <- prop. table (table (nincome, sPID) , 1)
> logit (pim [, 1] ) -logit (pim [, 1] +pim [, 2] )


<table>
<tr>
<th>1.5</th>
<th>4</th>
<th>6</th>
<th>8</th>
<th>9.5</th>
<th>10.5</th>
</tr>
<tr>
<td>11.5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>-0.90079</td>
<td>-2.06142</td>
<td>-0.75769</td>
<td>-1.00330</td>
<td>-2.30259</td>
<td>-0.30830 -</td>
</tr>
<tr>
<td>0.79851</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>12.5</td>
<td>13.5</td>
<td>14.5</td>
<td>16</td>
<td>18.5</td>
<td>21</td>
</tr>
<tr>
<td>23.5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>-1.89712</td>
<td>-1.25276</td>
<td>-1.17865</td>
<td>-0.41285</td>
<td>-0.35424</td>
<td>-1.51413 -</td>
</tr>
<tr>
<td>1.65345</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>27.5</td>
<td>32.5</td>
<td>37.5</td>
<td>42.5</td>
<td>47.5</td>
<td>55</td>
</tr>
<tr>
<td>67.5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>-0.74678</td>
<td>-0.52252</td>
<td>-0.92326</td>
<td>-1.02962</td>
<td>-0.82198</td>
<td>-1.42760 -</td>
</tr>
<tr>
<td>1.18261</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>82.5</td>
<td>97.5</td>
<td>115</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>-0.98676</td>
<td>-1.48292</td>
<td>-1.70660</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


It is questionable whether these can be considered sufficiently constant, but at least there
is no trend. Now consider the interpretation of the fitted coefficients:

\> summary (pomodi)
Coefficients:
Value Std. Error t value
nincome 0.013120 0.0019708 6.6572
Intercepts :


<table>
<tr>
<th></th>
<th>Value Std. Error</th>
<th>t value</th>
</tr>
<tr>
<td>Democrat | Independent</td>
<td>0.209 0.112</td>
<td>1.863</td>
</tr>
<tr>
<td>Independent | Republican</td>
<td>1.292 0.120</td>
<td>10.753</td>
</tr>
<tr>
<td colspan="2">Residual Deviance: 1995.36 AIC: 2001.36</td>
<td></td>
</tr>
</table>


We can say that the odds of moving from Democrat to Independent/Republican category
(or from Democrat/Independent to Republican) increase by a factor of $\exp \left( 0 . 0 1 3 1 2 0 \right) =$
1.0132 as income increases by one unit ($1000). Notice that the log-odds are similar to
those obtained in the multinomial logit model. The intercepts correspond to the $\theta _ { j } .$ So for
an income of $0, the predicted probability of being a Democrat is:

\> ilogit (0.209)
[1] 0.55206

while that of being an Independent is:

\> ilogit (1.292) -ilogit (0.209)
[1] 0.23242

<!-- PageBreak -->

<!-- PageNumber="121" -->
<!-- PageHeader="Multinomial data" -->

with the remainder being Republicans. We can compute predicted values:

\> predict (pomodi, $\mathrm { d a t a } .$ frame (nincome=il, row. names=il) ,
type="probs")


<table>
<tr>
<th></th>
<th>Democrat</th>
<th>Independent</th>
<th>Republican</th>
</tr>
<tr>
<td>8</td>
<td>0.52602</td>
<td>0.24011</td>
<td>0.23387</td>
</tr>
<tr>
<td>26</td>
<td>0.46705</td>
<td>0.25415</td>
<td>0.27880</td>
</tr>
<tr>
<td>42</td>
<td>0.41535</td>
<td>0.26176</td>
<td>0.32290</td>
</tr>
<tr>
<td>58</td>
<td>$0 . 3 6 5 4 4$</td>
<td>0.26418</td>
<td>0.37038</td>
</tr>
<tr>
<td>74</td>
<td>0.31827</td>
<td>0.26122</td>
<td>$0 . 4 2 0 5 1$</td>
</tr>
<tr>
<td>90</td>
<td>$0 . 2 7 4 5 5$</td>
<td>0.25311</td>
<td>0.47234</td>
</tr>
<tr>
<td>107</td>
<td>0.23242</td>
<td>0.23954</td>
<td>0.52804</td>
</tr>
</table>


Notice how the probability of being a Democrat uniformly decreases with income while
that for being a Republican uniformly increases as income increases, but that the middle
category of Independent increases then decreases. This type of behavior can be expected
from the latent variable representation of the model.

We can illustrate the latent variable interpretation of proportional odds by computing
the cutpoints for incomes of $0, $50,000 and $100,000:

\> x <- seq (-4,4,by=0.05)
> $\mathrm { o l o t } \left( x \right. ,$ dlogis (x) , type="1")
> abline (v=c (0.209,1.292) )
> abline $\left( v = c \left( 0 . 2 0 9 , 1 . 2 9 2 \right) - 5 0 ^ { * } \right.$ -50\*0.013120, 1ty=2)
> abline(v=c(0.209,1.292)-100\*0.013120,lty=5)

The plot is shown in Figure 5.5.

Ordered Probit Model: If the latent variable $Z i$ has a standard normal distribution,
then:

$$\Phi ^ { - 1 } \left( \gamma _ { j } \left( x _ { i } \right) \right) = 0 , - \beta ^ { T } x _ { i } j = 1 , \ldots , J - 1$$

Applying this model to the nes96 data, we find:

\> opmod <- polr (sPID ~ nincome, method="probit")
> summary (opmod)
Coefficients:


<table>
<tr>
<th>Value</th>
<th>Std. Error</th>
<th>t value</th>
</tr>
<tr>
<td>nincome 0.008182</td>
<td>0.0012078</td>
<td>6.7745</td>
</tr>
</table>


Intercepts :


<table>
<tr>
<th></th>
<th>Value Std. Error</th>
<th>t value</th>
</tr>
<tr>
<td>Democrat | Independent</td>
<td>0.128 0.069</td>
<td>1.851</td>
</tr>
<tr>
<td>Independent | Republican</td>
<td>0.798 0.072</td>
<td>11.040</td>
</tr>
</table>


Residual Deviance: 1994.89
AIC: 2000.89

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 122" -->


<figure>
<figcaption>Figure 5.5 Solid lines represent an income of $0, dotted lines are for $50,000 and dashed lines are for $100,000. Probability of being $a$ Democrat is given by the area lying to the left of the leftmost of each pair of lines, while the probability of being a Republican is given by the area to the right of the rightmost of the pair. Independents are represented by the area in between.</figcaption>

0.05 0.10 0.15 0.20 0.25

Density

-4

-2

0

2

4

</figure>


The deviance is similar to the logit version of this model, but the coefficients appear to be
different. However, if we compute the same predictions:

\> dems <- pnorm(0.128-i1\*0.008182)
> demind <- pnorm(0.798-i1\*0.008182)
> cbind (dems, demind-dems, 1-demind)
dems


<table>
<tr>
<td>[1,]</td>
<td>0.52494</td>
<td>0.24315</td>
<td>0.23192</td>
</tr>
<tr>
<td>[2,]</td>
<td>0.46624</td>
<td></td>
<td></td>
</tr>
<tr>
<td>[3,]</td>
<td></td>
<td>0.26058</td>
<td>0.32479</td>
</tr>
<tr>
<td>[4,]</td>
<td>0.36446</td>
<td>0.26236</td>
<td>0.37318</td>
</tr>
<tr>
<td>[5,]</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>[6,]</td>
<td>0.27147</td>
<td>0.25310</td>
<td>0.47543</td>
</tr>
<tr>
<td>[7,]</td>
<td>0.22739</td>
<td>0.24173</td>
<td>0.53088</td>
</tr>
</table>


We see that the predicted values are very similar to those seen for the logit. If the
coefficients are appropriately rescaled, they are also very similar.

Proportional Hazards Model: A concept of hazard was developed in insurance
applications. When issuing a life insurance policy, the insurer is interested in the

<!-- PageBreak -->

<!-- PageNumber="123" -->
<!-- PageHeader="Multinomial data" -->

probability that the person will die during the term of the policy given that they are alive
now. This is not the same as the unconditional probability of death during the same time
period. In other words, for example, we want to know the chance that a 55-year-old man
will die in the next year, given that he is alive and aged 55. The unconditional probability
that a man will die aged 55 is not particular useful for the purposes of insurance.

Suppose we use the complementary log-log in place of the logit above, that is:
$\log \left( - \log \left( 1 - \gamma _ { j } \left( x _ { i } \right) \right) \right) = \theta _ { j } + \beta ^ { T } x _ { i }$

Then the hazard of category $\dot { J }$ is the probability of falling in category $j$ given that your

category is greater than $j :$
$$H a z a r d \left( j \right) = P \left( Y _ { i } = j | Y _ { i } \geq j \right) = \frac { P \left( Y _ { i } = j \right) } { P \left( Y _ { i } \geq j \right) } = \frac { p _ { j } } { 1 - \gamma _ { i , j - 1 } } = \frac { \gamma _ { i j } - \gamma _ { i , j - 1 } } { 1 - \gamma _ { t , j - 1 } }$$

These hazards are then proportional across categories as $x$ varies. The corresponding
latent variable distribution is the extreme value:

$F \left( x \right) = 1 - \exp \left( - \exp \left( x \right) \right)$

The extreme value distribution is not symmetric like the logistic and normal and so there
seems little justification for applying it to the nes96 data, but the command is:

$$> \text { polr } \left( s P I D \sim n i n c o m e _ { \prime } , m e t h o d = ^ { \prime \prime } c l o g l o g ^ { \prime \prime } \right)$$

Generalization: The proportional hazards and odds models can be generalized by
allowing $\beta$ to vary that is

$$\log \frac { \gamma _ { j } \left( x \right) } { 1 - \gamma _ { j } \left( x \right) } = 0 _ { j } - \beta _ { j } ^ { T } x \quad j = 1 , \ldots , k - 1$$

but this loses the proportionality property.

Further Reading: For more on the analysis of ordered categorical data see the books
by Agresti (1984), Clogg and Shihadeh (1994), Powers and Xie (2000) and Simonoff
(2003).


### Exercises

1\. This hsb data was collected as a subset of the High School and Beyond study
conducted by the National Education Longitudinal Studies program of the National
Center for Education Statistics. The variables are gender; race; socioeconomic status;
school type; chosen high school program type; scores on reading, writing, math,
science, and social studies. We want to determine which factors are related to the
choice of the type of program-academic, vocational, or general-that the students
pursue in high school. The response is multinomial with three levels.

(a) Fit a trinomial response model with the other relevant variables as predictors
(untransformed).

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 124" -->

(b) Use backward elimination to reduce the model to one where all predictors are
statistically significant. Give an interpretation of the resulting model.

(c) For the student with id 99, compute the predicted probabilities of the three possible
choices.

2\. Data were collected from 39 students in a University of Chicago MBA class and
may be found in the dataset happy.

(a) Build a model for the level of happiness as a function of the other variables.

(b) Interpret the parameters of your chosen model.

(c) Predict the happiness distribution for subject whose parents earn $30,000 a year,
who is lonely, not sexually active and has no job.

3\. A student newspaper conducted a survey of student opinions about the Vietnam War in
May 1967. Responses were classified by sex, year in the program and one of four
opinions. The survey was voluntary. The data may be found in the dataset uncviet.

(a) Treat the opinion as the response and the sex and year as predictors. Build a
proportional odds model, giving an interpretation to the estimates.

(b) If you completed the analysis of this same dataset as a question in the previous
chapter, compare and contrast the results of the two analyses.

4\. The pneumo data gives the number of coal miners classified by radiological
examination into one of three categories of pneumonoconiosis and by the number of
years spent working at the coal face divided into eight categories.

(a) Treating the pneumonoconiosis status as response variable as nominal, build a
model for predicting the frequency of the three outcomes in terms of length of
service and use it to predict the outcome for a miner with 25 years of service.

(b) Repeat the analysis with the pneumonoconiosis status being treated as ordinal.

(c) Now treat the response variable as hierarchical with top level indicating whether
the miner has the disease and the second level indicating, given they have the
disease, whether they have a moderate or severe case.

(d) Compare the three analyses.

5\. The debt data arise from a large postal survey on the psychology of debt. The
frequency of credit card use is a three-level factor ranging from never, through
occasionally to regularly. Build a model for predicting credit card use as a function of
the other variables. Write a report describing the nature of the effect of the predictors
on the response.

6\. The National Youth Survey collected a sample of 11-17 year-olds with 117 boys and
120 girls, asking questions about marijuana usage. The data may be found in pot use.
This data is actually longitudinal-the same boys and girls are followed for five years.
However, for the purposes of this question, imagine that the data is cross-sectional,
that is, a different sample of boys and girls are sampled each year. Build a model for
the different levels of marijuana usage, describing the trend over time and the
difference between the sexes.

<!-- PageBreak -->

<!-- PageBreak -->


## CHAPTER 6 Generalized Linear Models

In previous chapters, we have seen how to model a binomial or Poisson response.
Multinomial response models can often be recast as Poisson responses and the standard
linear model with a normal (Gaussian) response is already familiar. Although these
models each have their distinctive characteristics, we observe some common features in
all of them that we can abstract to form the generalized linear model (GLM). By
developing a theory and constructing general methods for GLMs, we can are able to
tackle a wider range of data with different types of response variables. GLMs were
introduced by Nelder and Wedderburn (1972) while McCullagh and Nelder (1989)
provides a book-length treatment.


### 6.1 GLM Definition

A GLM is defined by specifying two components. The response should be a member of
the exponential family distribution and the link function describes how the mean of the
response and a linear combination of the predictors are related.

Exponential family: In a GLM the distribution of $Y$ is from the exponential family of
distributions which take the general form:

$$f \left( y | \theta , \phi \right) = \exp \left[ \frac { y \theta - b \left( \theta \right) } { a \left( \phi \right) } + c \left( y , \phi \right) \right]$$

The $\theta$ is called the canonical parameter and represents the location while $\phi$ "is called the
dispersion parameter and represents the scale. We may define various members of the
family by specifying the functions a, $b ,$ and c. The most commonly used examples are:

1\. Normal or Gaussian:

$$f \left( y | \theta , \phi \right) = \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left[ - \frac { \left( y - \mu \right) ^ { 2 } } { 2 \sigma ^ { 2 } } \right]$$
$$= \exp \left[ \frac { y \mu - \mu ^ { 2 } / 2 } { \sigma ^ { 2 } } - \frac { 1 } { 2 } \left( \frac { y ^ { 2 } } { \sigma ^ { 2 } } + \log \left( 2 \pi \sigma ^ { 2 } \right) \right) \right]$$

So we can write $\theta = \mu$ , $\phi = \sigma ^ { 2 }$ , $a \left( \phi \right) = \phi ,$ $b \left( \theta \right) = \theta ^ { 2 } / 2$
$c \left( y , \phi \right) = - \left( y ^ { 2 } / \phi + \log \left( 2 \pi \phi \right) \right) / 2 .$

2\. Poisson:

<!-- PageBreak -->

<!-- PageHeader="Generalized linear models 127" -->

$$f \left( y | \theta , \phi \right) = e ^ { - y } | x ^ { y } / y !$$
$$= \mathrm { e x p } \left( y \log \mu - \mu - \log y ! \right)$$

So we can write $\theta = \log \left( \mu \right) ,$ $\widehat { \varphi } \equiv 1 ,$ $a \left( \phi \right) = 1 ,$ $b \left( 0 \right) = \mathrm { e x p } \left( \theta \right) _ { a n d }$
$c \left( y , \phi \right) = - \log y ! .$

3\. Binomial:

$$f \left( y | \theta , \phi \right) = \left( \begin{array}{} { n } \\ { y } \end{array} \right) x ^ { n } \left( 1 - \mu \right) ^ { n - y }$$
$$= \exp \left( y \log \mu + \left( n - y \right) \log \left( 1 - \mu \right) + \log \binom { n } { y } \right.$$
$$= \mathrm { e x p } \left( y \log \frac { \mu } { 1 - \mu } + n \log \left( 1 - \mu \right) + \log \left( \begin{array}{} { n } \\ { y } \end{array} \right) \right.$$

So we
$\theta = \log \frac { \mu } { 1 - \mu } , { } _ { b \left( \theta \right) = - n \log \left( 1 - \mu \right) = n \log \left( 1 + e x p \theta \right) \text { and } c \left( y , \phi \right) } =$
$\log \left( n \right) .$

The gamma and inverse Gaussian are other lesser-used members of the exponential
family that are covered in Chapter 7. Notice that in the normal density, the parameter is
free (as it is also for the gamma density) while for the Poisson and binomial it is fixed at
one. This is because the Poisson and binomial are one parameter families while the
normal and gamma have two parameters. In fact, some authors reserve the term
exponential family distribution for cases where $\phi _ { \mathrm { i s } }$ not used, while using the term
exponential dispersion family for cases where it is. This has important consequences for
the analysis.

Some other densities, such as the negative binomial and the Weibull distribution, are
not members of the exponential family, but they are sufficiently close that the GLM can
be fit with some modifications. It is also possible to fit distributions that are not in the
exponential family using the GLM-style approach, but there are some additional
complications.

The exponential family distributions have mean and variance:

$$E Y = \mu = b ^ { \prime } \left( \theta \right)$$
$$Y = b ^ { \prime \prime } \left( 0 \right) a \left( \phi \right)$$
var

The mean is a function of 0 only while the variance is a product of functions of the
location and the scale. $b ^ { \prime \prime } \left( \theta \right)$ is called the variance function and describes how the
variance relates to the mean.

In the Gaussian case, $b ^ { \prime \prime } \left( \theta \right) = 1$ and so the variance is independent of the mean. For
other distributions, this is not true, making the Gaussian case exceptional. We can
introduce weights by setting:

$$a \left( \phi \right) = \phi / w$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 128" -->

where $w$ is a known weight that varies between observations.

Link function: Let us suppose we may express the effect of the predictors on the
response through a linear predictor:

$\eta = \beta _ { 0 } + \beta _ { 1 } x _ { 1 } + \ldots + \beta _ { p } x _ { p } = x ^ { T } \beta$

The link function, $g ,$ describes how the mean response, $E Y = \mu ,$ is linked to the covariates
through the linear predictor:

$\eta = \mathrm { g } \left( \mu \right)$

In principle, any monotone continuous and differentiable function will do, but there are
some convenient and common choices for the standard GLMs.

In the Gaussian linear model, the identity link, $\eta = \mu$ is the obvious selection, but
another choice would give $y = g ^ { - 1 } \left( x ^ { T } \beta \right) + \varepsilon .$ This does not correspond directly to a transform
on the response: $g \left( y \right) = x ^ { T } \beta + \varepsilon$ as, for example, in a Box-Cox type transformation. In a
GLM, the link function is assumed known whereas in a single index model, $g$ is
estimated.

For the Poisson GLM, the mean $\mu$ must be positive so $\eta = \mu$ will not work conveniently
since $\eta$ can be negative. The standard choice is $\mu = e ^ { \eta }$ so that $\eta = \log \mu$ which ensures $\mu > 0 .$
This log link means that additive effects of $x$ lead to multiplicative effects on $\mu .$

For the binomial GLM, let $p$ be the probability of success and let this be our $\mu$ if we
define the response as the proportion rather than the count. This requires that $0 \leq p \leq 1 .$
There are several commonly used ways to ensure this: the logistic, probit and
complementary log-log links. These are discussed in detail in Chapter 2.

The canonical link has $\mathrm { g }$ such that $\eta = \mathrm { g } \left( \mu \right) = 0 ,$ the canonical parameter of the
exponential family distribution. This means that $g \left( b ^ { \prime } \left( \theta \right) \right) = 0 .$ The canonical links for the
common GLMs are shown in Table 6.1. If a canonical link is used, $X ^ { T } Y$ is


<table>
<caption>Table 6.1 Canonical links for $G L M s .$</caption>
<tr>
<th>Family</th>
<th>Link</th>
<th>Variance Function</th>
</tr>
<tr>
<td>Normal</td>
<td>$\eta = \mu$</td>
<td>1</td>
</tr>
<tr>
<td>Poisson</td>
<td>$\eta = \log \mu$</td>
<td>$\mu$</td>
</tr>
<tr>
<td>Binomial</td>
<td>$\eta = \log \left( \mu / \left( 1 - \mu \right) \right)$</td>
<td>$\mu \left( 1 - \mu \right)$</td>
</tr>
<tr>
<td>Gamma</td>
<td>$\eta = \mu ^ { - 1 }$</td>
<td>$\mu ^ { 2 }$</td>
</tr>
<tr>
<td>Inverse Gaussian</td>
<td>$\eta = \mu ^ { - 2 }$</td>
<td>$\mu ^ { 3 }$</td>
</tr>
</table>


sufficient for $\beta .$ The canonical link is mathematically and computationally convenient and
is often the natural choice of link. However, one is not required to use the canonical link
and sometimes context may compel another choice.

<!-- PageBreak -->

<!-- PageNumber="129" -->
<!-- PageHeader="Generalized linear models" -->


### 6.2 Fitting a GLM

The parameters, ß, of a GLM can be estimated using maximum likelihood. The log-
likelihood for single observation, where $a _ { i } \left( \phi \right) = \phi / w _ { i } { } _ { i s } :$

$$\log L \left( \theta _ { i } , \phi ; y _ { i } \right) = w _ { i } \left[ \frac { y _ { i } \theta _ { i } - b \left( \theta _ { i } \right) } { \phi } \right] + c \left( y _ { i } , \phi \right)$$

So for independent observations, the log-likelihood will be $\sum _ { i } \log L \left( \theta _ { i } , \phi ; y _ { i } \right) ,$ 0:y;).Sometimes
we can maximize this analytically and find an exact solution for the MLE $\widetilde { \beta } _ { \mathrm { r b u t } }$ the
Gaussian GLM is the only common case where this is possible. Typically, we must use
numerical optimization. By applying the Newton-Raphson method with Fisher scoring,
McCullagh and Nelder (1989) show that the optimization is equivalent to iteratively
reweighted least squares (IRWLS).

The procedure can be understood intuitively by analogy to the procedure for the
Gaussian linear model $Y = X \beta + \varepsilon .$ Suppose var $Y \propto f \left( \ddot { \eta } \right)$ $\widehat { \mathrm { y } } = \widehat { \eta } = \mathrm { X } \widehat { \beta } _ { \cdot \mathrm { W } \mathrm { e } }$ would
use weights w; where $w _ { i } ^ { - 1 } = f \left( \widehat { \eta } \right)$ Since the weights are a function of $\widehat { \beta } _ { \mathrm { a n } }$ iterative
fitting procedure would be needed. We might set the weights all equal to one, estimate P.
$\widehat { \beta } _ { \mathrm { r a n d } \mathrm { s } } .$

We can use a similar idea to fit a GLM. Roughly speaking, we want to regress $g \left( y \right)$ on
$X$ with weights inversely proportional to var $g \left( y \right) .$ However, $g \left( y \right)$ might not make sense in
some cases-for example, in the binomial GLM. So we linearize $g \left( y \right)$ as follows: Let
$\eta = g \left( \mu \right)$ and $\mu = E Y .$ Now do a one-step expansion:

$$g \left( y \right) \approx g \left( \mu \right) + \left( y - \mu \right) g ^ { \prime } \left( \mu \right)$$
$$= \eta + \left( y - \mu \right) \frac { d \eta } { d \mu }$$
$$\equiv z$$

and

$$z = \left( \frac { d \eta } { d \mu } \right) ^ { 2 } V \left( \ddot { a } \right) = \frac { 1 } { w }$$

So the IRWLS procedure would be:

1\. Set initial estimates $\mathfrak{f} _ { 1 0 \mathrm { a n d } }$

2\. Form the "adjusted dependent variable" $z _ { 0 } = i _ { 0 } + \left( y - i _ { 0 } \right) \frac { d \eta } { d \mu } | _ { i _ { 0 } }$

3\. Form the weights
$w _ { 0 } ^ { - 1 } = \left( \frac { d \eta } { d \mu } \right) ^ { 2 } | _ { \ddot { \eta } _ { 0 } } V \left( \dot { \mu } _ { 0 } \right) .$

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 130

4\. Reestimate ß to get $\dot { \eta } _ { 1 }$

5\. Iterate steps 2-3-4 until convergence.

Notice that the fitting procedure uses only $\eta = g \left( \mu \right)$ and $V \left( \mu \right) ,$ but requires no further
knowledge of the distribution of y. This point will be important later in Section 7.4.
Estimates of variance may be obtained from:

$$\mathrm { v a r } \left( \widehat { \beta } \right) = \left( X ^ { T } W X \right) ^ { - 1 }$$

which is comparable to the form used in weighted least squares with the exception that
the weights are now a function of the response for a GLM.

Let's implement the procedure explicitly to understand how the fitting algorithm
works. We use the Bliss data from Section 2.7 to illustrate this. Here is the fit we are
trying to match:

\> data (bliss)
> modl <- glm (cbind (dead, alive) ~ conc,
family=binomial, bliss)
> summary (modl) $coef


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
<th>$\mathbb{P} \underline { r } \left( > | z | \right)$</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-2.3238</td>
<td>0.41789</td>
<td>-5.5608</td>
<td>2.6854e-08</td>
</tr>
<tr>
<td>conc</td>
<td>1.1619</td>
<td>0.18142</td>
<td>6.4046</td>
<td></td>
</tr>
</table>


For a binomial response, we have:

n =
$$\mathrm { o g } \frac { \mu } { 1 - \mu } \quad \frac { d \eta } { d \mu } = \frac { 1 } { \mu \left( 1 - \mu \right) } \quad V \left( \mu \right) = \mu \left( 1 - \mu \right) / n \quad w = n \mu \left( 1 - \mu \right)$$

where the variance is computed with the understanding that $y$ is the proportion not the
count. We use $y$ for our initial guess for $\widehat { \mu } _ { \mathrm { w h i c h } }$ works here because none of the
observed proportions are zero or one:

\> y <- bliss$dead/30; mu <- y
> eta <- logit (mu)
> z <- eta + (y-mu) / (mu* (1-mu) )
> w <- 30\*mu\* (1-mu)

\> Imod <- 1m (z ~ conc, weights=w, bliss)
> coef(lmod)

(Intercept)
conc
-2.3025
1.1536

It is interesting how close these initial estimates are to the converged values given above.
This is not uncommon. Even so, to get a more precise result, iteration is necessary. We do
five iterations here:

\> for (i in 1:5) {
\+ eta <- lmod$fit
\+ mu <- ilogit (eta)
\+ z <- eta + (y-mu) / (mu* (1-mu) )

<!-- PageBreak -->

<!-- PageNumber="131" -->
<!-- PageHeader="Generalized linear models" -->

\+ w <- 30\*mu\* (1-mu)
\+ lmod <- 1m(z ~ bliss$conc, weights=w)
\+ cat(i,coef(lmod),"\n")
\+ }


<table>
<tr>
<td>1</td>
<td>-2.3237</td>
<td>1.1618</td>
</tr>
<tr>
<td>2</td>
<td>-2.3238</td>
<td>1.1619</td>
</tr>
<tr>
<td>3</td>
<td>-2.3238</td>
<td>1.1619</td>
</tr>
<tr>
<td>4</td>
<td>-2.3238</td>
<td>1.1619</td>
</tr>
<tr>
<td>5</td>
<td>-2.3238</td>
<td>1.1619</td>
</tr>
</table>


We can see that convergence is fast in this case. The Fisher scoring iterations referred to
in the output record the number of iterations. In most cases, the convergence is rapid. If
there is a failure to converge, this is often a sign of some problem with the model
specification or unusual feature of the data. An example of such a problem with the
estimation may be seen in Section 2.8. A look at the final (weighted) linear model reveals
that:

\> summary(lmod)

Coefficients:

Estimate Std. Error t value Pr $\left( > | t | \right)$
(Intercept)
-2.3238

0.1462
-15.9 0.00054
conc
1.1619
0.0635
18.3
0.00036

Residual standard error: 0.35 on 3 degrees of freedom

The standard errors are not correct and can be computed (rather inefficiently) as follows:

\> xm <- model.matrix(lmod)
> wm <- diag (w)
> sqrt (diag (solve (t (xm) %\*% wm %\*% xm) ) )
[1] 0.41787 0.18141

Now var(B) = (X"WX)" because $\phi = I _ { f o r }$ the binomial model but in the Gaussian
linear model $\mathrm { v a r } \left( \widetilde { \beta } \right) = \left( X ^ { T } W X \right) ^ { - 1 }$ get the correct standard errors from the Im fit,
☒
we need to scale out the $\widehat { \mathrm { d } } _ { \mathrm { a s } }$ follows:

\> summary(lmod)$coef[,2]/summary(Imod)$sigma
(Intercept)
conc

0.41789
0.18142

These calculations are shown for illustration purposes only and are done more efficiently
and reliably by the glm function.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 132" -->


### 6.3 Hypothesis Tests

When considering the choice of model for some data, we should define the range of
possibilities. The null model is the smallest model we will entertain while the full or
saturated model is the most complex.

The null model represents the situation where there is no relation between the
predictors and the response. Usually this means we fit a common mean $\mu$ for $\mathrm { a l l } \nu ,$ that is,
one parameter only. For the Gaussian GLM, this is the model $y = \mu + c .$ For some
contingency table models, there will be additional parameters that represent row or
column totals or other such constraints. In these cases, the null model will have more than
one parameter.

In the saturated model, the data is explained exactly. Typically, we need to use $n$
parameters for $n$ data points. This can often be achieved by fitting a sufficiently high-
order polynomial or by treating the numerical values of quantitative predictors as codes,
thereby changing them into qualitative predictors. If enough interactions are included, the
model will be saturated. This model tells us no more than the data itself and is usually
uninformative.

A statistical model describes how we partition the data into systematic structure and
random variation. The null model represents one extreme where the data is represented
entirely as random variation, while the saturated or full model represents the data as
being entirely systematic.

The full model does give us a measure of how well any model could possibly fit and
so we might consider the difference between the log-likelihood for the full model,
$l \left( y , \phi | y \right)$ that for the model under consideration, $l \left( i l , \phi | y \right) ,$ oly),expressed as a likelihood
ratio statistic:

$$2 \left( I \left( y , \phi | y \right) - I \left( \widehat { \mu } , \phi | y \right) \right)$$

Provided that the observations are independent and for an exponential family distribution,
when $a _ { i } \left( \phi \right) = \phi / w _ { i }$ simplifies to:

$$\sum _ { i } 2 w _ { i } \left( y _ { i } \left( \widetilde { \theta } _ { i } - \widehat { \theta } _ { i } \right) - b \left( \widetilde { \theta } _ { i } \right) + b \left( \widehat { \theta } _ { i } \right) \right) / \phi$$

where $\widetilde { \theta } _ { \mathrm { a r e } }$ the estimates under the full (saturated) model and $\ddot { \theta } _ { \mathrm { a r e } }$ the estimates under
the model of interest. The above can be written simply as $D \left( y , \widetilde { M } \right) /$ $D \left( y , \widetilde { \mu } \right) _ { i s }$
called the deviance and $D \left( y , \widetilde { \mu } \right) / \phi _ { 1 S }$ called the scaled deviance. Deviances for the
common GLMs are shown in Table 6.2.


<table>
<tr>
<th>GLM</th>
<th>Deviance</th>
</tr>
<tr>
<td>Gaussian</td>
<td>$\sum _ { i } \left( y _ { i } - \widehat { \mu } _ { i } \right) ^ { 2 }$</td>
</tr>
<tr>
<td>Poisson</td>
<td>$$2 \sum _ { i } \left[ y _ { i } \log \left( y _ { i } / A _ { i } \right) - \left( y _ { i } - i _ { i } \right) \right]$$</td>
</tr>
<tr>
<td>Binomial</td>
<td>$$2 \sum _ { i } \left[ y _ { i } \log \left( y _ { i } / \widehat { \mu } _ { i } \right) + \left( m - y _ { i } \right) \log \left( \left( m - y _ { i } \right) / \left( m - j _ { i } \right) \right) \right]$$</td>
</tr>
<tr>
<td>Gamma</td>
<td>$$2 \sum _ { i } \left[ - \log \left( y / i \right) + \left( y - i \right) / A \right]$$</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="133" -->
<!-- PageHeader="Generalized linear models" -->

Inverse Gaussian

$$\sum \left( y - i \right) ^ { 2 } / \left( i ^ { 2 } y \right)$$

Table 6.2 For the binomial $y i \sim B \left( m , p _ { i } \right)$ and $\mu i =$
mpi that is $\mu$ is the count and not proportion in this
formula. For the Poisson, the deviance is known as
the G-statistic. The second term $\sum _ { i } \left( y _ { i } - i _ { i } \right)$ usually
zero if an intercept term is used in the model.

Pearson's $X ^ { 2 }$ statistic:

$$X ^ { 2 } = \sum _ { i } \frac { \left( y _ { i } - i _ { 1 } \right) ^ { 2 } } { V \left( a _ { i } \right) }$$

where $V \left( \widehat { H } \right) = \mathrm { v a r } \left( \widehat { \mu } \right)$ an alternative measure of discrepancy that is sometimes used in
place of the deviance.

There are two main types of hypothesis test we shall employ. The goodness of fit test
simply asks whether the current model fits the data. The other type of test compares two
nested models where the smaller model represents a linear restriction on the parameters
of the larger model. The goodness of fit test can be viewed as model comparison test if
we identify the smaller model with the model of interest and the larger model with the
full or saturated model.

For the goodness of fit test, we use the fact that, under certain conditions, provided the
model is correct, the scaled Deviance and the Pearson's $X ^ { 2 }$ statistic are both
asymptotically $x ^ { 2 }$ with degrees of freedom equal to the number of identifiable parameters.
For GLMs such as the Gaussian, we usually do not know the value of the dispersion
parameter, $\Phi$ 9,and so this test cannot be used. For the binomial and the Poisson, $\phi = 1$ 1,
and so the test is practical. However, the accuracy of the asymptotic approximation is
dubious for smaller datasets. For a binary, that is a 0-1 response, the approximation is
worthless.

For comparing a larger model, $\Omega ,$ to a smaller nested model, @ the difference in the
scaled deviances, $D _ { 0 } - D _ { \Omega }$ is asymptotically $x ^ { 2 }$ with degrees of freedom equal to the
difference in the number of identifiable parameters in the two models. For the Gaussian
model and other models where the dispersion $\Phi$ "is usually not known, this test cannot be
directly used. However, if we insert an estimate of $\Phi _ { \mathrm { W e } }$ may compute an F-statistic of the
form:

$$\frac { \left( D _ { 6 0 } - D _ { \Omega } \right) / \left( d f _ { 0 } - d f _ { \Omega } \right) } { 6 }$$

where $\ddot { \phi } = X ^ { 2 } / \left( n - p \right)$ a good estimate of the dispersion. For the Gaussian model,
$\dot { \phi } = R S S _ { \Omega } / d f _ { \Omega }$ the resulting F-statistic has an exact $F$ distribution for the null. For
other GLMs with free dispersion parameters, the statistic is only approximately F
distributed.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 134" -->

For every GLM except the Gaussian, an approximate null distribution must be used
whose accuracy may be in doubt particularly for smaller samples. However, the
approximation is better when comparing models than for the goodness of fit statistic.

Let's consider the possible tests on the Bliss insect data:

\> summary (modl)

Coefficients :

Estimate Std. Error z value $\mathbb{P} \underline { r } \left( > | z | \right)$
(Intercept)
-2.324

0.418

-5.56 2.7e-08

conc
1.162

0.181

6.40
$1 . 5 e - 1 0$
(Dispersion parameter for binomial family taken to be
1)

Null deviance: 64.76327 on 4 degrees of freedom
Residual deviance: 0.37875 on 3 degrees of freedom

We are able to make a goodness of fit test by examining the size of the residual deviance
compared to its degrees of freedom:

$$> 1 - \mathrm { p c h i s q } \left( \text { deviance } \left( \text { modi } \right) , \text { df . residual } \left( \text { modi } \right) \right)$$
[1] 0.9446

where we see the p-value is large indicating no evidence of a lack of fit. As with lack of
fit tests for Gaussian linear models, this outcome does not mean that this model is correct
or that no better models exist. We can also quickly see that the null model would be
inadequate for the data since the null deviance of 64.7 is very large for four degrees of
freedom.

We can also test for the significance of the linear concentration term by comparing the
current model to the null model:

\> anova (modl, test="Chi")
Analysis of Deviance Table
Model: binomial, link: logit
Terms added sequentially (first to last)
Df Deviance Resid. Df Resid. Dev P (> | Chi| )


<table>
<tr>
<td>NULL</td>
<td></td>
<td>4</td>
<td>64.8</td>
<td></td>
</tr>
<tr>
<td>conc 1</td>
<td>64.4</td>
<td>3</td>
<td>0.4</td>
<td>le-15</td>
</tr>
</table>


We see that the concentration term is clearly significant. We can also fit and test a more
complex model:

\> mod12 <- glm(cbind (dead, alive) ~ conc+I (conc^2) ,
family=binomial, bliss)
> anova (mod1, mod12, test="Chi")


<table>
<tr>
<th></th>
<th>Resid. Df</th>
<th>Resid. Dev</th>
<th>Df</th>
<th>Deviance</th>
<th>P(&gt;|Chi|)</th>
</tr>
<tr>
<td>1</td>
<td>3</td>
<td>0.379</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>0.195</td>
<td>1</td>
<td>0.183</td>
<td>0.669</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Generalized linear models 135" -->

We can see that there is no need for a quadratic term in the model. The same information
could be extracted with:

$$> \text { anova } \left( m o d 1 2 , t e s t = ^ { \prime \prime } C h i ^ { \prime \prime } \right)$$

We may also take a Wald test approach. We may use the standard error of the parameter
estimates to construct a z-statistic of the form $\ddot { \beta } / \mathrm { s e } \left( \ddot { \beta } \right)$ has an asymptotically norma
null distribution. For the Bliss data, for the concentration term, we have
$z = 1 . 1 6 2 / 0 . 1 8 1 = 6 . 4 0 .$ Thus the (approximate) p-value for the Wald test of the
concentration parameter being equal to zero is $1 . 5 e ^ { - 1 0 }$ and thus we clearly reject the null
here. Remember that this is again only an approximate test except in the special case of
the Gaussian GLM where the z-statistic is the t-statistic and has an exact t-distribution.
The difference of deviances test is preferred to the Wald test due, in part, to the problem
noted by Hauck and Donner (1977).


### 6.4 GLM Diagnostics

As with standard linear models, it is important to check the adequacy of the
assumptions that support the GLM. The diagnostic methods for GLMs mirror those used
for Gaussian linear models. However, some adaptations are necessary and, depending on
the type of GLM, not all diagnostic methods will be applicable.

Residuals: Residuals represent the difference between the data and the model and are
essential to explore the adequacy of the model. In the Gaussian case, the residuals are
$\dot { E } = y - i$ P.These are called response residuals for GLMs, but since the variance of the
response is not constant for most GLMs, some modification is necessary. We would like
residuals for GLMs to be defined such that they can be used in a similar way as in the
Gaussian linear model.

The Pearson residual is comparable to the standardized residuals used for linear
models and is defined as:

$$r _ { P } = \frac { y - \widehat { \mu } } { \sqrt { V \left( \widehat { \mu } \right) } }$$

where $\mathrm { V } \left( \mu \right) = b ^ { \prime \prime } \left( \theta \right) .$ These are just a rescaling of $y - \widehat { y }$ -P.Notice that $\sum r _ { P } ^ { 2 } = X ^ { 2 }$
and hence
the name. Pearson residuals can be skewed for nonnormal responses.

The deviance residuals are defined by analogy to Pearson residuals. The Pearson
residual was $r _ { P }$ such that
$\sum r _ { P } ^ { 2 } = X ^ { 2 }$
*so we set the deviance residual as $r _ { D }$ such that
$\sum r _ { D } ^ { 2 } = \text { Deviance } = \sum d _ { i }$
Thus:

$$r _ { D } = s i g n \left( y - i \right) \sqrt { d }$$

For example, in the Poisson:

$$r _ { D } = s i g n \left( y - i \right) \left[ 2 \left( y \log y / \widehat { \mu } - y + \widehat { \mu } \right) \right] ^ { 1 / 2 }$$

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 136

Let's examine the types of residuals available to us using the Bliss data. We can obtain
the deviance residuals as:

\> residuals (modl)
[1] -0.451015 0.359696 0.000000 0.064302 -0.204493

These are the default choice of residuals. The Pearson residuals are:

\> residuals (modl, "pearson")
1
2
3
4
5
-0.432523 0.364373 0.000000 0.064147 -0.208107

which are just slightly different from the deviance residuals. The response residuals are:

\> residuals (modl, "response")
1
2
3

4
5
-0.0225051 0.0283435 0.0000000 0.0049898 -0.0108282

which is just the response minus the fitted value:

\> bliss$dead/30 - fitted (modl)
1
2
3
4
5
-0.0225051 0.0283435 0.0000000 0.0049898 -0.0108282

Finally, the so-called working residuals are:

\> residuals (modl, "working")
1
2

-0.277088 0.156141 0.000000 0.027488 -0.133320

\> modl$residuals

3
4
5
1
2
3
4
5

-0.277088 0.156141 0.000000 0.027488 -0.133320

Note that it is important to use the residuals () function to get the deviance residuals
which are most likely what is needed for diagnostic purposes. Using $residuals gives the
working residuals which is not usually needed for diagnostics. We can now identify the
working residuals as a by-product of the IRWLS fitting procedure:

\> residuals(lmod)
1
2
3
4
01

-2.7709e-01 1.5614e-01 -3.8463e-16 2.7488e-02 -1.3332e-
5

Leverage and influence: For a linear model, $y =$ Hy,where $H$ is the hat matrix that
projects the data onto the fitted values. The leverages hi are given by the diagonal of $H$
and represent the potential of the point to influence the fit. They are solely a function of $X$

<!-- PageBreak -->

<!-- PageHeader="Generalized linear models 137" -->

and whether they are in fact influential will also depend on $\mathrm { y } .$ Leverages are somewhat
different for GLMs. The IRWLS algorithm used to fit the GLM uses weights, w. These
weights are just part of the IRWLS algorithm and are not user assigned. However, these
do affect the leverage. We form a matrix $W = \mathrm { d i a g } \left( w \right)$ and the hat matrix is:

$H = W ^ { 1 / 2 } X \left( X ^ { \Gamma } W X \right) ^ { - 1 } X ^ { T } W ^ { 1 / 2 }$

We extract the diagonal elements of $H$ to get the leverages hi. A large value of hi
indicates that the fit may be sensitive to the response at case $i$ i. Large leverages typically
mean that the predictor values are unusual in some way. One important difference from
the linear model case is that the leverages are no longer just $a$ function of $X$ and now
depend on the response through the weights $W .$ The leverages may be calculated as:

\> influence (mod1) $hat

$$\begin{array}{} { 1 } & { 2 } & { 3 } & { 4 } & { 4 } & { 5 } \\ { 0 . 4 2 5 5 0 } & { 0 . 4 1 3 3 1 } & { 0 . 3 2 2 3 8 } & { 0 . 4 1 3 3 1 } & { 0 . 4 2 5 5 0 } \end{array}$$

$A s$ in the linear model case, we might choose to studentize the residuals as follows:

$$r _ { 5 D } = \frac { r _ { D } } { \sqrt { \dot { \beta } \left( 1 - h _ { l } \right) } }$$ ☒

or compute jacknife residuals representing the difference between the observed response
for case $i$ and that predicted from the data with case $i$ excluded, scaled appropriately.
These are expensive to compute exactly and so an approximation due to

Williams (1987) can be used:

$$\mathrm { s i g n } \left( y - i \right) \mathrm { s q r i } \left( 1 - h _ { i } \right) r _ { 5 D } ^ { 2 } + h _ { i } r _ { 5 P } ^ { 2 }$$

where $r _ { S P } = r _ { P } / \sqrt { 1 - h _ { i } }$ Hi.These may be computed as:
☒

\> rstudent(modl)

$$\begin{array}{} { 1 } & { 2 } & { 3 } & { 4 } & { 4 } & { 5 } & { 5 } & { 5 } & { 5 } \\ { - 0 . 5 8 4 7 8 6 } & { 0 . 4 7 2 1 3 5 } & { 0 . 0 0 0 0 0 0 } & { 0 . 0 8 3 8 6 6 } & { - 0 . 2 7 1 8 3 5 } & { } & { } \end{array}$$

Outliers may be detected by observing particularly large jacknife residuals.

Leverage only measures the potential to affect the fit whereas measures of influence
more directly assess the effect of each case on the fit. We can examine the change in the
fit from omitting a case by looking at the changes in the coefficients:


<table>
<tr>
<th colspan="3">&gt; influence (mod1) $coef</th>
</tr>
<tr>
<th></th>
<th>(Intercept)</th>
<th>conc</th>
</tr>
<tr>
<td>1</td>
<td>-0.2140015</td>
<td>0.0806635</td>
</tr>
<tr>
<td>2</td>
<td>0.1556719</td>
<td>-0.0470873</td>
</tr>
<tr>
<td>3</td>
<td>0.0000000</td>
<td>0.0000000</td>
</tr>
<tr>
<td>4</td>
<td>-0.0058417</td>
<td>0.0084177</td>
</tr>
<tr>
<td>5</td>
<td>0.0492639</td>
<td>-0.0365734</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 138" -->

Alternatively, we can examine the Cook statistics:

$$D _ { i } = \frac { \left( \widehat { \beta } _ { \left( i \right) } - \widehat { \beta } \right) ^ { T } \left( X ^ { T } W X \right) \left( \widehat { \beta } _ { \left( i \right) } - \widehat { \beta } \right) } { p \widehat { \phi } }$$

which may be calculated as:

\> cooks. distance (modi)
1
2
3
4
5
0.1205927 0.0797100 0.0000000 0.0024704 0.0279174

We can see that the biggest change would occur by omitting the first observation.
However, since this is a very small dataset with just five observations, we would not
contemplate dropping cases. In any event, we see that the change in the coefficients
would not qualitatively change the conclusion.

Model diagnostics: We may divide diagnostic methods into two types. Some methods
are designed to detect single cases or small groups of cases that do not fit the pattern of
the rest of the data. Outlier detection is an example of this. Other methods are designed to
check the assumptions of the model. These methods can be subdivided into those that
check the structural form of the model, such as the choice and transformation of the
predictors, and those that check the stochastic part of the model, such as the nature of the
variance about the mean response. Here, we focus on methods for checking the
assumptions of the model.

For linear models, the plot of residuals against fitted values is probably the single most
valuable graphic. For GLMs, we must decide on the appropriate scale for the fitted
values. Usually, it is better to plot the linear predictors $\widehat { \eta } _ { \mathrm { r a t h e r } }$ than the predicted
responses $\widehat { \mu }$ ".We revisit the model for Galápagos data first presented in Section 3.1.
Consider first a plot using "presented in the first panel of Figure 6.1:

\> data (gala)
> gala <- gala [, -2]
> modp <- glm (Species ~ . , family=poisson, gala)
> plot (residuals (modp) ~ predict
(modp, type="response") ,
xlab=expression (hat (mu) ) , ylab="Deviance residuals")

<!-- PageBreak -->

<!-- PageNumber="139" -->
<!-- PageHeader="Generalized linear models" -->


<figure>
<figcaption>Figure 6.1 Residual vs. fitted plots for the Galápagos model. The first uses fitted values in the scale of the response while the second uses fitted values in the scale of the linear predictor. The third plot uses response residuals while the first two use deviance residuals.</figcaption>

01

0

10

0

0

0

0

0

0

0

9

0

001

Devance residuals

H

9

0

Deviance residushy

¢

Response residuals

0

0

0

0

0

0

0

9

0

0

0

o

0

L

00

0

0

0

0

0

0

0

·

¢

0

₩

9

0

0

0

0

a

0

0

0

0

0

0

4:00

0

0

0

0

05

0

b

5

0

0

001-

0

0

0

o

0

0

¢

0

0

350

25

!!

1

35

4.5

1

25

3.5

4.5

5.5

1

</figure>


There are just a few islands with a large predicted number of species while most
predicted response values are small. This makes it difficult to see the relationship
between the residuals and the fitted values because most of the points are compressed on
the left of the display. Now we try plotting "1:

$$p l o t \left( r e s i d u a l s \left( m o d p \right) \sim p r e d i c t \left( m o d p , t y p e = ^ { \prime \prime } l i n k ^ { \prime \prime } \right) , \right. ,$$
$$\left. x l a b = e x p r e s s i o n \left( h a t \left( e t a \right) \right) , y l a b = ^ { \prime \prime } D e v i a n c e r e s i d u a l s ^ { \prime \prime } \right)$$

Now the points, shown in the second panel of Figure 6.1, are more evenly spaced in the
horizontal direction. We are looking for two main features in such a plot. Is there any
nonlinear relationship between the predicted values and the residuals? If so, this would be
an indication of a lack of fit that might be rectified by a change in the model. For a linear
model, we might consider a transformation of the response, but this is usually impractical
for a GLM since it would change the assumed distribution of the response. We might also
consider a change to the link function, but often this is undesirable since there a few
choices of link function that lead to easily interpretable models. It is best if a change in
the choice of predictors or transformations on these predictors can be made since this
involves the least disruption to the GLM. For this particular $p l o t ,$ there is no evidence of
nonlinearity.

The variance of the residuals with respect to the fitted values should also be inspected.
The assumptions of the GLM would require constant variance in the plot and, in this
case, this appears to be the case. A violation of this assumption would prompt a change in
the model. We might consider a change in the variance function $V \left( \mu \right) ,$ but this would

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 140" -->

involve abandoning the Poisson GLM since this specifies a particular form for the
variance function. We would need to use a quasi-likelihood GLM described in Section
7.4. Alternatively, we could employ a different GLM for a count response such as the
negative binomial. Finally, we might use weights if we could identify some feature of the
data that would suggest a suitable choice.

For all GLMs but the Gaussian, we have a nonconstant variance function. However,
by using deviance residuals, we have already scaled out the variance function and so,
provided the variance function is correct, we do expect to see constant variance in the
plot. If we use response residuals, that is $y = i l _ { 1 a s }$ seen in the third panel of Figure 6.1:

$$> \text { plot } \left( \text { residuals } \left( \text { modp } _ { \prime } \text { type } = ^ { \prime \prime } \text { response } ^ { \prime \prime } \right) \sim \text { predict } \right.$$
$$\left. x l a b = e x p r e s s i o n \left( h a t \left( e t a \right) \right) , y l a b = n ^ { \prime } R e s p o n s e r e s i d u a l s ^ { \prime \prime } \right)$$
(modp, type="link") ,

We see a pattern of increasing variation consistent with the Poisson.

In some cases, plots of the residuals are not particularly helpful. For a binary response,
the residual can only take two possible values for given predicted response. This is the
most extreme situation, but similar discreteness can occur for binomial responses with
small group sizes and Poisson responses that are small. Plots of residuals in these cases
tend to show curved lines of points corresponding to the limited number of observed
responses. Such artifacts can obscure the main purpose of the plot. Difficulties arise for
binomial data where the covariate classes have very different sizes. Points on plots may
represent just a few or a large number of individuals.

Investigating the nature of the relationship between the predictors and the response is
another primary objective of diagnostic plots. Even before a model is fit to the data, we
might simply plot the response against the predictors. For the Galápagos data, consider a
plot of the number of species against the area of the island shown in the first panel of
Figure 6.2:

\>
$$\mathrm { p l o t } \left( \mathrm { S p e c i e s } \sim \mathrm { A r e a } _ { \prime } \mathrm { g a l a } \right)$$

We see that both variables have skewed distributions. We start with a log transformation
on the predictor as seen in the second panel of Figure 6.2:

$$> \mathrm { p l o t } \left( \mathrm { S p e c i e s } \sim \mathrm { l o g } \left( \mathrm { A r e a } \right) , \mathrm { g a l a } \right)$$

We see a curvilinear relationship between the predictor and the response. However, the
default Poisson GLM uses a log link which we need to take into account. To allow for the
choice of link function, we can plot the linearized response:

$$z = \eta + \left( y - \mu \right) \frac { d \eta } { d \mu }$$

as we see in the third panel of Figure 6.2:

$$> z < - \quad p r e d i c t \left( m o d p \right) + \left( g a l a S p e c i e s - m u \right) / m u$$

<!-- PageBreak -->

<!-- PageHeader="Generalized linear models" -->
<!-- PageNumber="141" -->

\> plot (z ~ log (Area) , gala, ylab="Linearized Response")


<figure>
<figcaption>Figure 6.2 Plots of the number of species against area for the Galápagos data. The first plot clearly shows $a$ need for transformation, the second shows the advantage of using logged area, while the third shows the value of using the linearized response.</figcaption>

9

0

0

5

0

0

0

8

0

0

0

0

0

¥

0

¢

0

0

0

0

0

=

0

0

¢

0

¢

0

D

0

M

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

D

0

0

O

0

9

9

N

0

0

1000

2000

3000

4000

4

S

0

4

5

6

\-

"

0

.

4

.

Ama

</figure>


We now see a linear relationship suggesting that no further transformation of area is
necessary. Notice that we used the current model in the computation of z. Some might
prefer to use an initial guess here to avoid presuming the choice of model. For this
dataset, we find that a log transformation of all the predictors is helpful:

\> modpl <- glm (Species ~ log (Area) + log (Elevation) +
log (Nearest) +
log (Scruz+0.1) + log (Adjacent), family=poisson, gala)
> c (deviance (modp) , deviance (modpl) )
[1] 716.85 359.12

We see that this results in a substantial reduction in the deviance.

The disadvantage of simply examining the raw relationship between the response and
the other predictors is that it fails to take into account the effect of the other predictors.
Partial residual plots are used for linear models to make allowance for the effect of the
other predictors while focusing on the relationship of interest. These can be adapted for
use in GLMs by plotting $z - \bar { \widehat { \eta } } + \beta _ { j } x _ { j } \text { versus } x _ { j } .$ The interpretation is the same as in the
linear model case. We compute the partial residual plot for the (now logged) area, as
shown in the first panel of Figure 6.3:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 142" -->

\> mu <- predict (modpl, type="response")
> u <- (gala$Species-mu) /mu + coef (modpl)
[2] *log (gala$Area)
> plot (u ~ log (Area) , gala, ylab="Partial Residual")
> abline (0, coef (modpl) [2] )

In this plot, we see no reason for concern. There is no nonlinearity indicating a need to
transform nor are there any obvious outliers or influential points. Partial residuals can
also be obtained from residuals (., type="partial") although an offset will be necessary if
you want the regression line displayed correctly on the plot.

One can search for good transformations of the predictors in nongraphical ways.
Polynomials terms or spline functions of the predictors can be experimented with, but
generalized additive models, described in Chapter 12, offer a more direct way to discover
some good transformations.

The link function is a fundamental assumption of the GLM. Quite often the choice of
link function is set by the characteristics of the response, such as positivity, or by ease of
interpretation, as with logit link for binomial GLMs. It is often difficult to contemplate
alternatives. Nevertheless, it is worth checking to see whether the link assumption is not
grossly wrong. Before doing this, it is important to eliminate other simpler violations of
the assumptions that are more easily rectified such as outliers


<figure>
<figcaption>Figure 6.3 A partial residual plot for $\log \left( A r e a \right)$ is shown on the left while $a$ diagnostic for the link function is shown on the right.</figcaption>

4

Linearized Response

0

2

Partial Residual

5

0

$\varpi$

4

0

-1

2

-2

20 2 4 6 8

2

3

4

5

$6$

$\log \left( A r a a \right)$

Linear predictor

</figure>


or transformations of the predictors. After these concerns have been eliminated, one can
check the link assumption by making a plot of the linearized response $z$ against linear
predictor 11.An example of this is shown in the second panel of Figure 6.3:

\> z <- predict (modpl) + (gala$Species-mu) /mu
> plot (z ~ predict (modpl) , xlab="Linear predictor",
ylab="Linearized Response")

<!-- PageBreak -->

<!-- PageNumber="143" -->
<!-- PageHeader="Generalized linear models" -->

In this case, we see no indication of a problem.

An alternative approach to checking the link function is to propose a family of link
functions of which the current choice is a member. $\mathrm { A }$ range of links can then be fit and
compared to the current choice. The approach is analogous to the Box-Cox method used
for linear models. Alternative choices are easier to explore within the quasi-likelihood
framework described in Section 7.4.


### Unusual Points

We have already described the raw material of residuals, leverage and influence measures
that can be used to check for points that do not fit the model or influence the fit unduly.
Let's now see how to use graphical methods to examine these quantities.

The Q-Q plot of the residuals is the standard way to check the normality assumption
on the errors typically made for a linear model. For a GLM, we do not expect the
residuals to be normally distributed, but we are still interested in detecting outliers. For
this purpose, it is better to use a half-normal plot that compares the sorted absolute
residuals and the quantiles of the half-normal distribution:

$$\Phi ^ { - 1 } \left( \frac { n + i } { 2 n + 1 } \right) \quad i = 1 , \ldots , n$$

The residuals are not expected to be normally distributed, so we are not looking for an
approximate straight line. We only seek outliers which may be identified as points off the
trend. $A$ half-normal plot is better for this purpose because in a sense the resolution of the
plot is doubled by having all the points in one tail.

Since we are more specifically interested in outliers, we should plot the jacknife
residuals. $\mathrm { A n }$ example for the Galápagos model is shown in the first panel of Figure 6.4:

\> halfnorm (rstudent (modpl) )


<figure>
<figcaption>Figure 6.4 Half-normal plots of the jacknife residuals on the left and the leverages on the right.</figcaption>

13

0.8

25

8

22

Sorted Data

Sorted Data

0.6

16

0.4

¥

2

2

0

0

0.0

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

Half-normal quantiles

Hall-normal quantiles

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 144" -->

We see no sign of outliers in the plot. The half-normal plot is also useful for positive-
valued diagnostics such as the leverages and the Cook statistics. $\mathrm { A }$ look at the leverages is
shown in the second panel of Figure 6.4:

\> gali <- influence (modpl)
> halfnorm (gali$hat)

There is some indication that case 25, Santa Cruz island, may have some leverage. The
predictor Scruz is the distance from Santa Cruz island which is zero for this case. This
posed a problem for making the log transformation and explains why we added 0.1 to this
variable. However, there is some indication that this inelegant fix may be causing some
difficulty.

Moving on to influence, a half-normal plot of the Cook statistics is shown in the first
panel of Figure 6.5:

$$> \mathrm { h a l f n o r m } \left( \mathrm { c o o k s } . \mathrm { d i s t a n c e } \left( \mathrm { m o d } \mathrm { p } \right) \right)$$

Again we have some indication that Santa Cruz island is influential. We can examine the
change in the fitted coefficients. For example, consider the change in the Scruz
coefficient as shown in the second panel of Figure 6.5:

$$> \text { plot \left(gal iscoef } \left[ , 5 \right] , \text { ylab= ^{\prime\prime } \text { Change in } } \sin \text { Scruz }$$

coef", xlab="Case no.")

We see a substantial change for case 25. If we compare the full fit to a model without this
case, we find:

\> modplr <- glm(Species ~ log (Area) + log (Elevation) +
log (Nearest)
\+ log (Scruz+0.1) + log (Adjacent) , family=poisson,
gala, subset =- 25)
\> cbind (coef (modpl) , coef (modplr) )


<table>
<tr>
<td>(Intercept)</td>
<td>3.287941</td>
<td>3.050699</td>
</tr>
<tr>
<td>log (Area)</td>
<td>0.348445</td>
<td>0.334530</td>
</tr>
<tr>
<td>log (Elevation)</td>
<td>0.036421</td>
<td>0.059603</td>
</tr>
<tr>
<td>log (Nearest)</td>
<td>-0.040644</td>
<td>-0.052548</td>
</tr>
<tr>
<td>log (Scruz + 0.1)</td>
<td>-0.030045</td>
<td>0.015919</td>
</tr>
<tr>
<td>log (Adjacent)</td>
<td>-0.089014</td>
<td>-0.088516</td>
</tr>
</table>


We see a sign change for the Scruz coefficient. This is interesting since in the full model,
the coefficient is more than twice the standard error way from zero indicating some
significance. A simple solution is to add a larger amount, say 0.5, to Scruz.

Other than this user-introduced anomaly, we find no difficulty. Using our earlier
discovery of the log transformation, some variable selection and allowing for remaining
overdispersion, our final model is:

<!-- PageBreak -->

<!-- PageNumber="145" -->
<!-- PageHeader="Generalized linear models" -->


<figure>
<figcaption>Figure 6.5 Half-normal plot of the Cook statistics is shown on the left and an index plot of the change in the Scruz coefficient is shown on the right.</figcaption>

2 3 4 5 1

25

0.02

0

Sorted Data

Change in Scruz coef

27

0.00

0

-0.02

0

1

-0.04

0

0

0.0 0.5 1.0 1.5 2.0 0 5

10

15

20 25 30

Half-normal quantiles

Case no.

</figure>


$$\left[ , 2 \right]$$

\> modpla <- glm (Species ~ log (Area) +log (Adjacent) ,
family=poisson, gala)
> dp <-
sum (residuals (modpla, type="pearson") ^2) /modpla$df.res
> summary (modpla, dispersion=dp)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>z value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>3.2767</td>
<td colspan="2">0.1794 18.26</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>log (Area)</td>
<td>0.3750</td>
<td colspan="2">0.0326 11.50</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>log (Adjacent)</td>
<td>-0.0957</td>
<td colspan="2">0.0249 -3.85</td>
<td>0.00012</td>
</tr>
</table>


(Dispersion parameter for poisson family taken to be
16.527)

Null deviance: 3510.73 on 29 degrees of freedom
Residual deviance: 395.54 on 27 degrees of freedom

Notice that the deviance is much lower and the elevation variable is not used when
compared with our model choice in Section 3.1.

This example concerned a Poisson GLM. Diagnostics for binomial GLMs are similar,
but see Pregibon (1981) and Collett (2003) for more details.

Further Reading: The canonical book on GLMs is McCullagh and Nelder (1989).
Other books include Dobson (1990), Lindsey (1997), Myers, Montgomery, and Vining
(2002), Gill (2001) and Fahrmeir and Tutz (2001). For a Bayesian perspective, see Dey,
Ghosh, and Mallick (2000).

<!-- PageBreak -->

<!-- PageNumber="146" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->


### Exercises

1\. Consider the or ings data from Chapter 2. Suppose that, in spite of all the drawbacks,
we insist on fitting a model with an identity link, but with the binomial variance. Show
how this may be done using a quasi family model using the glm function. (You will
need need to consult the help pages for quasi and $\mathrm { g l m }$ and in particular you will need
to set good starting values for beta-if it doesn't work at the first attempt, try different
values.) Describe how the fitted model differs from the standard logistic regression
and give the predicted response at a temperature of 31ºF.

2\. Fit the orings data with a binomial response and a logit link as in Chapter 2.

(a) Construct the appropriate test statistic for testing the effect of the temperature.
State the appropriate null distribution and give the p-value.

(b) Generate data under the null distribution for the previous test. Use the rbinom
function with the average proportion of damaged O-rings. Recompute the test
statistic and compute the p-value.

(c) Repeat the process of the previous question 1000 times, saving the test statistic
each time. Compare the empirical distribution of these simulated test statistics with
the nominal null distribution stated in the first part of this question. Compare the
critical values for a 5% level test computed using these two methods.

3\. Fit the orings data with a binomial response and a logit link as in Chapter 2.

(a) Construct the appropriate test statistic for testing the effect of the temperature.
State the appropriate null distribution and give the p-value.

(b) Generate a random permutation of the responses using sample and recompute the
test statistic and compute the p-value.

(c) Repeat the process of the previous question 1000 times, saving the test statistic
each time. Compare the empirical distribution of these permuted data test statistics
with the nominal null distribution stated in the first part of this question. Compare
the critical values for a 5% level test computed using these two methods.

4\. Data is generated from the exponential distribution with $f \left( y \right) = 2 \exp \left( - \lambda y \right)$ where
$\lambda ,$ $y > 0 .$

(a) Identify the specific form of $\theta , \phi , a \left( \right)$ $c \left( \right)$ for the exponential distribution.

(b) What is the canonical link and variance function for a GLM with a response
following the exponential distribution?

(c) Identify a practical difficulty that may arise when using the canonical link in this
instance.

(d) When comparing nested models in this case, should an $F$ or $x ^ { 2 }$ test be used?
Explain.

(e) Express the deviance in this case in terms of the responses $y i$ and the fitted values
$\widehat { \mu } _ { i }$

5\. The Conway-Maxwell-Poisson distribution has probability function:

$$P \left( Y = y \right) = \frac { i y } { \left( y ! \right) ^ { v } } \frac { 1 } { Z \left( A , v \right) } \quad y = 0 , 1 , 2 , \ldots$$

<!-- PageBreak -->

<!-- PageNumber="147" -->
<!-- PageHeader="Generalized linear models" -->

where

$$Z \left( \lambda , v \right) = \sum _ { i = 0 } ^ { \infty } \frac { \lambda ^ { i } } { \left( i ! \right) ^ { v } }$$

Place this in exponential family form, identifying all the relevant components
necessary for use in a GLM.

<!-- PageBreak -->

<!-- PageBreak -->


## CHAPTER 7 Other GLMs

The binomial, Gaussian and Poisson GLMs are by far the most commonly used, but there
are a number of less popular GLMs which are useful for particular types of data. The
gamma and inverse Gaussian are intended for continuous, skewed responses. In some
cases, we are interested in modeling both the mean and the dispersion of the response and
so we present dual GLMs for this purpose. The quasi-GLM is a model that is useful for
nonstandard responses where we are unwilling to specify the distribution but can state the
link and variance functions.


### 7.1 Gamma GLM

The density of the gamma distribution is usually given by:

$$f \left( y \right) = \frac { 1 } { \Gamma \left( v \right) } h ^ { v } y ^ { v - 1 } e ^ { - h y } \quad y > 0$$

where $v$ describes the shape and $\lambda$ describes the scale of the distribution. However, for the
purposes of a GLM, it is convenient to reparameterize by putting $\lambda = v / \mu$ to get:

$$f \left( y \right) = \frac { 1 } { \Gamma \left( v \right) } \left( \frac { v } { \mu } \right) ^ { v } y ^ { v - 1 } e ^ { - \left( \frac { v v } { \mu } \right) } \quad y > 0$$ ☒

Now $E Y = \mu$ and var $Y = \mu ^ { 2 } / v = \left( E Y \right) ^ { 2 } / v .$ The dispersion parameter is $\phi = v ^ { - 1 }$ .Here we plot a
gamma density with three different values of the shape parameter $v$ (the scale parameter
would just have a multiplicative effect) as seen in Figure 7.1:

$$> x < - \mathrm { s e q } \left( 0 , 8 , b y = 0 . 1 \right)$$

\>
plot (x, dgamma (x, 0. 75) , type="1", ylab="", xlab="", ylim=c (0
, 1.25),
$\left. X a X S = { } ^ { \prime \prime } j ^ { \prime \prime } , y a X S = { } ^ { \prime \prime } j ^ { \prime \prime \prime } \right)$
\>
plot (x, dgamma (x, 1.0) , type="1", ylab="", xlab="", ylim=c (0,
1.25),
$\left. x a x s = 1 ^ { \prime \prime } , y a x s = ^ { \prime \prime } j ^ { \prime \prime } \right)$
\>
plot (x, dgamma (x, 2.0) , type="1", ylab="", xlab="", ylim=c (0,
1.25),
xaxs="i", yaxs="i")

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 150" -->

The gamma distribution can arise in various ways. The sum of $v$ independent and
identically distributed exponential random variables with rate $\lambda$ has a gamma distribution.
The $x ^ { 2 }$ distribution is a special case of the gamma where $\lambda = 1 / 2$ and $v = d f / 2 .$

The canonical parameter is $- 1 / \mu ,$ so the canonical link is $\eta = - 1 / \mu .$ However, we
typically remove the minus (which is fine provided we take account of this in any
derivations) and just use the inverse link. We also have $b \left( \theta \right) = \log \left( 1 / \mu \right) = - \log \left( - \theta \right)$


<figure>
<figcaption>Figure 7.1 The gamma density explored. In the first panel $v = 0 . 7 5$ and we see that the density is unbounded $a t$ zero. In the second panel, $v = 1$ which is the exponential density. In the third panel, $v = 2$ and we see $a$ skewed distribution.</figcaption>

₪

W

₼

0

\#

W

0

L

2

1

"

0

.

0

0

2

4

6

8

$\widetilde { \complement }$

2

4

5

8

0

2

4

0

5

</figure>


and so $b ^ { \prime \prime } \left( \theta \right) = u ^ { 2 }$ is the variance function. The (unscaled) deviance is:

$$D \left( y , \widetilde { \mu } \right) = - 2 \sum \left\{ \log y _ { i } / \widetilde { \mu } _ { i } - \left( y _ { i } - \widetilde { \mu } _ { i } \right) / \widetilde { \mu } _ { i } \right\}$$

The utility of the gamma GLM arises in two different ways. Certainly, if we believe the
response to have a gamma distribution, the model is clearly applicable. However, the
model can also be useful in other situations where we may be willing to speculate on the
relationship between the mean and the variance of the response but are not sure about the
distribution. Indeed, it is possible to grasp the mean to variance relationship from
graphical displays with relatively small datasets, while assertions about the response
distribution would require a lot more data.

In the Gaussian linear model, var $Y$ is constant as a function of the mean response.
This is a fundamental assumption necessary for the optimality of least squares. However,
sometimes contextual knowledge of the data or diagnostics show that var $Y$ is
nonconstant. When the form of nonconstancy is known exactly, then weighted least
squares can be used. In practice, however, the form is often not known exactly.
Alternatively, transformation of $Y$ may lead to a constant variance model. The difficulty
here is that while the original scale $Y$ may be meaningful, log $Y$ or $\sqrt { Y } ,$ for example, may

<!-- PageBreak -->

<!-- PageNumber="149" -->
<!-- PageHeader="Other GLMs" -->

not. An example is where a sum of the $Y \mathrm { s }$ may be of interest. In such a case,
transformation would be a hindrance.

If var $Y \propto E Y$ EY,then $\sqrt { Y }$ is the variance stabilizing transform. If one wants to avoid a
transformation, a GLM approach can be used. When $Y$ has a Poisson distribution, then
var $Y \propto E Y$ EY,suggesting the use of a Poisson GLM. Now one might object that the
Poisson is a distribution for discrete data, which would seem to disallow its use for
continuous responses. However, fitting a GLM only depends on the mean and variance of
a distribution; the other moments are not used. This is important because it indicates that
we need specify nothing more than the mean and variance. The distribution could be
discrete or continuous and it would make no difference.

For some data, we might expect the standard deviation to increase linearly with the
response. If so, the coefficient of variation, SD $Y / E Y ,$ would be constant and var
$Y \propto \left( E Y \right) ^ { 2 } .$ For example, measurements of larger objects $d o$ tend to have more error
than smaller ones.

If we wanted to apply a Gaussian linear model, the log transform is indicated. This
would imply a lognormal distribution for the original response. Alternatively, if $Y \sim$
gamma, then var $Y \propto \left( E Y \right) ^ { 2 }$ +so a gamma GLM is also appropriate in this situation. In a
few cases, one may have some knowledge concerning the true distribution of the
response which would drive the choice. However, in many cases, it would be difficult to
distinguish between these two options on the basis of the data alone and the choice would
be driven by the purpose and desired interpretation of the model.

There are three common choices of link function:

1\. The canonical link is $\eta = \mu ^ { - 1 } .$ Since-o $- \infty < \eta < \infty ,$ the link does not guarantee $\mu > 0$ which
could cause problems and might require restrictions on $\beta$ or on the range of possible
predictor values. On the other hand the reciprocal link has some advantages. The
Michaelis-Menten model has:

$$E y = \mu = \frac { \alpha _ { 0 } x } { 1 + \alpha _ { 1 } x }$$

which can be represented after some reexpression as:

$$\eta = \alpha _ { 1 } / \alpha _ { 0 } + 1 / \left( \alpha _ { 0 } x \right) = u ^ { - 1 }$$

As $x$ increases, $\eta \rightarrow \alpha _ { 1 } / \alpha _ { 0 } ,$ which means that the mean $\mu$ will be bounded. The
inverse link can be useful in such situations where we know the mean response to
be bounded.

2\. The log link, $\eta = \log \mu ,$ should be used when the effect of the predictors is suspected to
be multiplicative on the mean. When the variance is small, this approach is similar to a
Gaussian model with a logged response.

3\. The linear link, $\eta = \mu ,$ is useful for modeling sums of squares or variance components
which are $x ^ { 2 } .$ This is a special case of the gamma.

The general GLM procedures apply to the analysis and fitting. To estimate the dispersion,
McCullagh and Nelder (1989) recommend the use of:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 152" -->

$$\widetilde { \phi } = \frac { 1 } { \widehat { v } } = \frac { X ^ { 2 } } { n - p }$$

The maximum likelihood estimator and the usual estimator, $D / \left( n - p \right) ,$ are both sensitive to
unusually small values of the response and are not consistent estimates of the coefficient
of variation when the gamma distribution assumption does not hold.

Myers and Montgomery (1997) present data from a step in the manufacturing process
for semiconductors. Four factors are believed to influence the resistivity of the wafer and
so a full factorial experiment with two levels of each factor was run. Previous experience
led to the expectation that resistivity would have a skewed distribution and so the need
for transformation was anticipated. We start with a look at the data:

\> data (wafer)
> summary (wafer)
x1
x2
x3

-: 8
-: 8
-: 8
+: 8 +:8 +:8 +:8 1st Qu. : 201

-: 8

x4
Min.

resist
:166

Median
: 214
Mean
: 229
3rd Qu. : 259
Max.
:340

The application of the Box-Cox method or past experience suggests the use of a log
transformation on the response. We fit the full model and then reduce it using AlC-based
model selection:

\> 11mdl <- Im(log (resist) ^ .^2, wafer)
> rlmdl <- step(llmdl)
> summary (rlmdl)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>5.3111</td>
<td>0.0476</td>
<td>111.53</td>
<td>$4 . 7 e - 1 4$</td>
</tr>
<tr>
<td>$x 1 +$</td>
<td>0.2009</td>
<td>0.0476</td>
<td>4.22</td>
<td>0.00292</td>
</tr>
<tr>
<td>$x 2 +$</td>
<td>-0.2107</td>
<td>0.0476</td>
<td>-4.43</td>
<td>0.00221</td>
</tr>
<tr>
<td>$x 3 +$</td>
<td>0.4372</td>
<td>0.0673</td>
<td>6.49</td>
<td>0.00019</td>
</tr>
<tr>
<td>$4 +$</td>
<td>0.0354</td>
<td>0.0476</td>
<td>0.74</td>
<td>0.47892</td>
</tr>
<tr>
<td>$x 1 + : x 3 +$</td>
<td>-0.1562</td>
<td>0.0673</td>
<td>-2.32</td>
<td>0.04896</td>
</tr>
<tr>
<td>$x 2 + : x 3 +$</td>
<td>-0.1782</td>
<td>0.0673</td>
<td>-2.65</td>
<td>0.02941</td>
</tr>
<tr>
<td>$x 3 + : x 4 +$</td>
<td>-0.1830</td>
<td>0.0673</td>
<td>-2.72</td>
<td>0.02635</td>
</tr>
<tr>
<td colspan="5">Residual standard error: 0.0673 on 8 degrees of freedom</td>
</tr>
</table>


$\mathrm { M u l t i p l e }$ R-Squared: 0.947, Adjusted R-squared: 0.901
F-statistic: 20.5 on 7 and 8 DF, p-value: 0.000165

We find a model with three two-way interactions, all with x3.

Now we fit the corresponding gamma GLM and again select the model using the AIC
criterion. Note that the family must be specified as Gamma rather than gamma to avoid
confusion with the $\Gamma$ function. We use the log link to be consistent with the linear model.
This must be specified as the default is the inverse link:

<!-- PageBreak -->

<!-- PageNumber="151" -->
<!-- PageHeader="Other GLMs" -->

\> gmdl <- glm (resist ~ . ^2, family=Gamma (link=log) ,
wafer)
> rgmdl <- step (gmdl)
> summary (rgmdl)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>5.3120</td>
<td>0.0476</td>
<td>111.68</td>
<td>4.6e-14</td>
</tr>
<tr>
<td>$x 1 +$</td>
<td>0.2003</td>
<td>0.0476</td>
<td>4.21</td>
<td>0.00295</td>
</tr>
<tr>
<td>$\times 2 +$</td>
<td>-0.2110</td>
<td>0.0476</td>
<td>-4.44</td>
<td>0.00218</td>
</tr>
<tr>
<td>$\times 3 +$</td>
<td>0.4367</td>
<td>0.0673</td>
<td>6.49</td>
<td>0.00019</td>
</tr>
<tr>
<td>$\times 4 +$</td>
<td>0.0354</td>
<td>0.0476</td>
<td>0.74</td>
<td>0.47836</td>
</tr>
<tr>
<td>$x 1 + : x 3 +$</td>
<td>-0.1555</td>
<td>0.0673</td>
<td>-2.31</td>
<td>0.04957</td>
</tr>
<tr>
<td>$x 2 + : x 3 +$</td>
<td>-0.1763</td>
<td>0.0673</td>
<td>-2.62</td>
<td>0.03064</td>
</tr>
<tr>
<td>$\times 3 + : \times 4 +$</td>
<td>-0.1819</td>
<td>0.0673</td>
<td>-2.70</td>
<td>0.02687</td>
</tr>
</table>

(Dispersion parameter for Gamma family taken to be
0.0045249)


Null deviance: 0.697837 on 15 degrees of freedom
Residual deviance: 0.036266 on 8 degrees of freedom
AIC: 139.2

In this case, we see that the coefficients are remarkably similar to the linear model with
the logged response. Even the standard errors are almost identical and the square root of
the dispersion corresponds to the residual standard error of the linear model:

\> sqrt (0.0045249)
[1] 0.067267

The maximum likelihood estimate of $\Phi _ { \mathrm { m a y } }$ be computed using the MASS package:

\> library (MASS)
> gamma.dispersion (rgmdl)
[1] 0.0022657

We see that this gives a substantially smaller estimate, which would suggest smaller
standard errors. However, it is not consistent with our experience with the Gaussian
linear model in this example.

In this example, because the value of $\mathrm { v } = 1 / \phi$ large (221), the gamma distribution
is well approximated by a normal. Similarly, for the logged response linear model, a
lognormal distribution with a small variance $\left( \sigma = 0 . 0 6 7 3 \right.$ is also very well approximated
by a normal. For this reason, there is not much to distinguish these two models. The
gamma GLM has the advantage of modeling the response directly while the lognormal
has the added convenience of working with a standard linear model.

Let us examine another example where there is more distinction between the two
approaches. In Hallin and Ingenbleek (1983) data on payments for insurance claims for
various areas of Sweden in 1977 are presented. The data is further subdivided by mileage
driven, the bonus from not having made previous claims and the type of car. We have
information on the number of insured, measured in policy-years, within each of these
groups. Since we expect that the total amount of the claims for a group will be

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 154

proportionate to the number of insured, it makes sense to treat the log of the number
insured as an offset for similar reasons to those in Section 3.2. Attention has been
restricted to data from Zone 1. After some model selection, a gamma GLM of the
following form was found:

\> data (motorins)
> motori <- motorins [motorins$Zone == 1, ]
> gl <- glm(Payment ~
offset (log (Insured) ) +as. numeric (Kilometres) +
Make+Bonus , family=Gamma (link=log), motori)
> summary (gl)
Coefficients :


<table>
<tr>
<th colspan="3"></th>
<th colspan="2">Estimate Std.</th>
<th colspan="3">Error t value</th>
</tr>
<tr>
<th colspan="2">Pr (&gt;|t|)</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="3">(Intercept)</th>
<th></th>
<th>6.5273</th>
<th>0.1777</th>
<th>36.72</th>
<th>&lt;</th>
</tr>
<tr>
<td>2e-16</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="4">as. numeric (Kilometres)</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>0.1201</td>
<td></td>
<td>0.0311</td>
<td>3.85</td>
<td>0.00014</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make2</td>
<td></td>
<td></td>
<td colspan="2">0.4070</td>
<td>0.1782</td>
<td>2.28</td>
<td>0.0</td>
</tr>
<tr>
<td>2313</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make3</td>
<td></td>
<td></td>
<td></td>
<td>0.1553</td>
<td>0.1796</td>
<td>0.87</td>
<td>0.3</td>
</tr>
<tr>
<td>8767</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make4</td>
<td></td>
<td></td>
<td></td>
<td>-0.3439</td>
<td>0.1915</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1.80</td>
<td colspan="2">0.07355</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make5</td>
<td></td>
<td></td>
<td></td>
<td>0.1447</td>
<td>0.1810</td>
<td>0.80</td>
<td>0.4</td>
</tr>
<tr>
<td>2473</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make 6</td>
<td></td>
<td></td>
<td></td>
<td>-0.3456</td>
<td>0.1782</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1.94</td>
<td colspan="2">0.05352</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make 7</td>
<td></td>
<td></td>
<td></td>
<td>0.0614</td>
<td>0.1824</td>
<td>0.34</td>
<td>0.7</td>
</tr>
<tr>
<td>3689</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make8</td>
<td></td>
<td></td>
<td></td>
<td>0.7504</td>
<td>0.1873</td>
<td>4.01</td>
<td></td>
</tr>
<tr>
<td colspan="3">0.000079</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make 9</td>
<td></td>
<td></td>
<td></td>
<td>0.0320</td>
<td>0.1782</td>
<td>0.18</td>
<td>0.8</td>
</tr>
<tr>
<td>5778</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bonus</td>
<td></td>
<td></td>
<td></td>
<td>-0.2007</td>
<td>0.0215</td>
<td>-9.33</td>
<td>&lt;</td>
</tr>
</table>


2e-16
(Dispersion parameter for Gamma family taken to be
0.55597)
Null deviance: 238.97 on 294 degrees of freedom
Residual deviance: 155.06 on 284 degrees of freedom
AIC: 7168

In comparison, the lognormal model, where we have used the glm function for
compatibility, looks like this:

\> 11g <- glm (log (Payment) ~
offset (log (Insured) ) +as. numeric (Kilometres) +
Make+Bonus, family=gaussian , motori)
> summary (11g)
Coefficients:

<!-- PageBreak -->

<!-- PageHeader="Other GLMs 153" -->


<table>
<tr>
<th colspan="8">Estimate Std. Error t value</th>
</tr>
<tr>
<th colspan="2">Pr $\left( > | t | \right)$</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2">(Intercept)</th>
<th></th>
<th>6.51403</th>
<th></th>
<th>0.18634</th>
<th>34.96</th>
<th>&lt;</th>
</tr>
<tr>
<td>2e-16</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">as .numeric (Kilometres)</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>0.05713</td>
<td>0.03265</td>
<td>1.75</td>
<td colspan="2">0.0813</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make2</td>
<td></td>
<td></td>
<td colspan="2">0.36387</td>
<td>0.18686</td>
<td>1.95</td>
<td>0.</td>
</tr>
<tr>
<td>0525</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make3</td>
<td></td>
<td></td>
<td>0.00692</td>
<td></td>
<td>0.18824</td>
<td>0.04</td>
<td>0.</td>
</tr>
<tr>
<td>9707</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make4</td>
<td></td>
<td></td>
<td>-0.54786</td>
<td></td>
<td>0.20076</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>2.73</td>
<td>0.0067</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make5</td>
<td></td>
<td></td>
<td>-0.02179</td>
<td></td>
<td>0.18972</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>0.11</td>
<td>0.9087</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make 6</td>
<td></td>
<td></td>
<td>-0.45881</td>
<td></td>
<td>0.18686</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>2.46</td>
<td>0.0147</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make 7</td>
<td></td>
<td></td>
<td>-0.32118</td>
<td></td>
<td>0.19126</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1.68</td>
<td>0.0942</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make8</td>
<td></td>
<td></td>
<td>0.20958</td>
<td></td>
<td>0.19631</td>
<td>1.07</td>
<td>0.</td>
</tr>
<tr>
<td>2866</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Make9</td>
<td></td>
<td></td>
<td>0.12545</td>
<td></td>
<td>0.18686</td>
<td>0.67</td>
<td>0.</td>
</tr>
<tr>
<td>5025</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bonus</td>
<td></td>
<td></td>
<td>-0.17806</td>
<td></td>
<td>0.02254</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>7.90</td>
<td>6.2e-14</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

(Dispersion parameter for gaussian family taken to be
0.61102)

Null deviance: 238.56 on 294 degrees of freedom
Residual deviance: 173.53 on 284 degrees of freedom
AIC: 704.6


Notice that there are now important differences between the two models. We see that
mileage class given by Kilometers is statistically significant in the gamma GLM, but not
in the lognormal model. Some of the coefficients are quite different. For example, we see
that for make 8, relative to the reference level of make 1, there are $\mathrm { e x p } \left( 0 . 7 5 0 4 \right) = 2 . 1 1 7 8$
times as much payment when using the gamma GLM, while the comparable figure for
the lognormal model is $\mathrm { e x p } \left( 0 . 2 0 9 5 8 \right) = 1 . 2 3 3 2 .$

These two models are not nested and have different distributions for the response,
which makes direct comparison problematic. The AIC criterion, which is minus twice the
maximized likelihood plus twice the number of parameters, has often been used as a way
to choose between models. Smaller values are preferred. However, when computing a
likelihood, it is common practice to discard parts that are not functions of the parameters.
This has no consequence when models with same distribution for the response are
compared since the parts discarded will be equal. For responses with different
distributions, it is essential that all parts of the likelihood be retained. The large difference
in $\mathrm { A I C }$ for these two models indicate that this precaution was not taken. Nevertheless, we
note that the null deviance for both models is almost the same while the residual deviance
is smaller for the gamma GLM. This improvement relative to the null indicates that the
gamma GLM should be preferred here. Note that purely numerical comparisons such as
this are risky and that some attention to residual diagnostics, scientific context and
interpretation is necessary.

<!-- PageBreak -->

<!-- PageNumber="156" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->

We compare the shapes of the distributions for the response using the dispersion
estimates from the two models, as seen in Figure 7.2:

$> x < - \mathrm { s e q } \left( 0 , 5 , b y = 0 . 0 5 \right)$
\>

plot(x,dgamma(x,1/0.55597,scale=0.55597),type="l",ylab=
,
xlab="", yaxs="i", ylim=c (0, 1) )
\> plot (x, dlnorm (x, meanlog =- 0.30551, sdlog=sqrt (0.55597) )
,type="l",
ylab="", xlab="", yaxs="i", ylim=c (0, 1) )


<figure>
<figcaption>Figure 7.2 Gamma density for observed shape of $1 / 0 . 5 5 5 9 7$ is shown on the left and lognormal density for an observed SD on the log scale v0.61102 The means have been set to one in both cases.</figcaption>

1.0

1.0

0.8

0.6

"

=

0.2

0.2

0.0

0

1

2

3

4

5

0

1 2 3 4

5

</figure>


We see the greater peakedness of the lognormal indicating more small payments which
are balanced by more large payments. The lognormal thus has higher kurtosis.

We may also make predictions from both models. Here is a plausible value of the
predictors:

\> x0 <-
data. frame (Make="1", Kilometres=1, Bonus=1, Insured=100)

and here is predicted response for the gamma GLM:

\> predict (gl, new=x0, $\mathrm { s e } = \mathbb{T} ,$ type="response")
$fit
[1] 63061
$se. fit
[1] 9711.5

<!-- PageBreak -->

<!-- PageNumber="155" -->
<!-- PageHeader="Other GLMs" -->

For the lognormal, we have:

\> predict (11g, new=x0, $\mathrm { s e } = \mathbb{T} ,$ type="response")
$fit
[1] 10.998
$se. fit
[1] 0.16145

so that the corresponding values on the original scale would be:

$$> c \left( e x p \left( 1 0 . 9 9 8 \right) , e x p \left( 1 0 . 9 9 8 \right) * 0 . 1 6 1 4 5 \right)$$

[1] 59754.5 9647.4

where we have used the delta method to estimate the standard error on the original scale.


### 7.2 Inverse Gaussian GLM

The density of an inverse Gaussian random variable, $Y \sim I G \left( \mu , \lambda \right)$ is:

$f \left( y | \mu , \lambda \right) = \left( \lambda / 2 \pi y ^ { 3 } \right) ^ { 1 / 2 } \exp \left[ - \lambda \left( y - \mu \right) ^ { 2 } / 2 \mu ^ { 2 } y \right] y , \mu , \lambda > 0$

The mean is $\mu$ and the variance is $u ^ { 3 } / \lambda .$ The canonical link is $\eta = 1 / \mu ^ { 2 }$ and the variance
function is $V \left( \mu \right) = \mu ^ { 3 } .$ The deviance is given by:

$$D = \sum _ { i } \left( y _ { i } - \widehat { \mu } _ { i } \right) ^ { 2 } / \left( \mu _ { i } ^ { 2 } y _ { i } \right)$$

Plots of the inverse Gaussian density for a range of values of the shape parameter, $\lambda ,$ are
shown in Figure 7.3:

\> library (SuppDists)
> x <- seq (0,8,by=0.1)
>
plot(x,dinvGauss(x,1,0.5),type="l",ylab="",xlab="",ylim
=c (0,1.5),
xaxs="i", yaxs="i")
\>
plot(x,dinvGauss(x,1,1),type="l",ylab="",xlab="",ylim=c
(0,1.5),
xaxs="i", yaxs="i")
\>
plot(x,dinvGauss(x,1,5),type="l",ylab="",xlab="",ylim=c
(0,1.5),

<!-- PageBreak -->

<!-- PageNumber="158" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->


<figure>
<figcaption>Figure 7.3 Inverse Gaussian densities for $\lambda = 0 . 5$ on the left, $\lambda = 1$ in the middle and $2 = 5$ on the right. $\mu = 1$ in all three cases.</figcaption>

21 01 00 00 10 20

00 02 04 06 08 1.0 1.2 1.4

00 02 04 06 08 10 12 14

0

1

2

J

4

0

4

1

3

4

5

0

1

$\widetilde { \mathbb{E} }$

3

4

·

</figure>


The case of $\mu = 1$ is known as the Wald distribution. The inverse Gaussian has found
application in the modeling of lifetime distributions with nonmonotone failure rates and
in the first passage times of Brownian motions with drift. See Seshadri (1993) for a book-
length treatment.

Notice that the variance function for the inverse Gaussian $\mathrm { G I } M$ increases more
rapidly with the mean than the gamma GLM, making it suitable for data where this
occurs.

In Whitmore (1986), some sales data on a range of products is presented for the
projected, $x i ,$ and actual, $\mathcal{Y} _ { i } ,$ sales for $i = 1 , \ldots ,$ 20. We consider a model, $y _ { i } = \beta x _ { i }$ where $\beta$
would represent the relative bias in the projected sales. Since the sales vary over $\mathrm { a }$ wide
range from small to large, a normal error would be unreasonable because $\bar { Y }$ is positive
and violations of this constraint could easily occur. We start with a look at the normal
model:

\> data (cpd)

\> lmod <- lm(actual ~ projected-1,cpd)
> summary(lmod)
Coefficients:
Estimate Std. Error t value $\mathbb{P} _ { \Sigma } \left( > | t | \right)$

projected
0.9940
0.0172
57.9
$< 2 e - 1 6$
\> plot (actual ~ projected, cpd)
> abline(lmod)

Now consider the inverse Gaussian GLM where we must specify an identity link because
we have $y _ { i } = \beta x _ { i } :$

\> igmod <- glm (actual ~ projected-1,
family=inverse. gaussian (link="identity"), cpd)
> summary (igmod)
Coefficients:

Estimate Std. Error t value $\Pr \left( > | t | \right)$

<!-- PageBreak -->

<!-- PageHeader="Other GLMs" -->
<!-- PageNumber="157" -->


<table>
<tr>
<td>projected 1.1036</td>
<td></td>
<td>0.0614</td>
<td></td>
<td colspan="3">18.0 2.2e-13</td>
</tr>
<tr>
<td>(Dispersion parameter</td>
<td>for</td>
<td></td>
<td></td>
<td></td>
<td>inverse.gaussian</td>
<td>family taken</td>
</tr>
<tr>
<td>to be 0.00017012)</td>
<td colspan="6"></td>
</tr>
<tr>
<td>Null deviance:</td>
<td></td>
<td colspan="2">Inf on</td>
<td colspan="3">20 degrees of freedom</td>
</tr>
<tr>
<td>Residual deviance:</td>
<td>0.0030616</td>
<td></td>
<td>on</td>
<td></td>
<td>19 degrees</td>
<td>of freedom</td>
</tr>
<tr>
<td colspan="2">&gt; abline (igmod, lty=2)</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</table>


We see that there is a clear difference in the estimates of the slope. The fits are shown in
the first panel of Figure 7.4. We should check the diagnostics on the inverse Gaussian
GLM:

\> plot (residuals (igmod) ~
log (fitted (igmod) ) , ylab="Deviance residuals",
xlab=expression (log (hat (mu) ) ) )
> abline (h=0)

We see in the second panel of Figure 7.4 that the variance of the residuals is decreasing
with error indicating that the inverse Gaussian variance function is too strong for this
data. We have used $\log \left( \check { \mu } \right) _ { \mathrm { s o } }$ that the points are more evenly spread horizontally making
it easier, in this case, to see the variance relationship. $A$ gamma GLM is a better choice
here. In Whitmore (1986), a different variance function is used, but we do not pursue this
here as this would not be a GLM.


<figure>
<figcaption>Figure 7.4 Projected and actual sales are shown for 20 products on the left. The linear model fit is shown as a solid line and the inverse Gaussian GLM fit is shown with a dotted line. A residual- fitted plot for the inverse Gaussian GLM is shown on the right.</figcaption>

0

5000

Deviance residuals

0.02

actual

3000

0.00

1000

-0.02

0

0

1000

3000

5000

5

6

7

8

projected

$\log \left( \frac { x } { 2 } \right)$

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 160" -->


### 7.3 Joint Modeling of the Mean and Dispersion

All models we have considered so far have modeled the mean response $\mu = E Y$ where the
variance takes a known form: var $Y _ { i } = \phi V \left( \mu _ { i } \right) _ { \text { where } }$ the dispersion parameter $\Phi$ the
variance in the Gaussian model, the squared coefficient of variation in the gamma model
and one in the binomial and Poisson models. We can generalize a little to allowing
weights by letting $\phi \equiv \phi _ { i } = \phi w _ { i }$ the weights are known.

In this section, we are interested in examples where Orvaries with the covariates $X .$
This is a particular issue that arises in industrial experiments. We wish to manufacture an
item with a target mean or optimized response. We set the predictors to produce items as
close as possible to the target mean or to optimize the mean. This requires a model for the
mean. We would also prefer that the variance of the response be small at the chosen value
of the predictors for production. So we need to model the variance as a function of the
predictors.

We take, as an example, an experiment to determine which recipe will most reliably
produce the best cake. The data comes from Box, Bisgaard, and Fung (1988) and is
shown in Table 7.1. The objective is to bake a cake reliably no matter how incompetent
the cook. For this data, we can see, by examination, that a response of 6.8 is possible for
lower flour and shortening content and higher egg content, if the temperature is on the
high side and the cooking time on the short side. However, we cannot be sure that the
consumer will be able to set the temperature and cooking time correctly. Perhaps their
oven is not correctly calibrated or they are just incompetent. If they happen to bake the
cake for longer than the set time, they will produce a cake with a 3.5 rating. They will
blame the product and not themselves and not buy that mix again. If on the other hand we
produce the mix with high flour and eggs and low shortening, the worst the customer can
do is a 5.2 and will do better than that for other combinations of time and temperature.

Here we need a combination of a high mean with respect to the design factors, flour, eggs
and shortening, and a low variance with respect to the environmental factors, temperature
and time. In this example, the answer is easily seen by inspection, but usually more
formal model fitting methods will be needed.

Joint Model Specification: We use the standard GLM approach for the mean:

$$E Y _ { i } = \mu _ { i } \quad \eta _ { i } = g \left( \mu _ { i } \right) = \sum _ { j } x _ { i j } \beta _ { j } \quad \text { var } Y _ { i } = \phi _ { i } V \left( \mu _ { i } \right) \quad w _ { i } = 1 / \phi _ { i }$$

Now the dispersion, $\phi _ { i }$ no longer considered fixed. Suppose we find an estimate, $d _ { i } ,$ of
the dispersion and model it using a gamma GLM:

$$E d _ { i } = \phi _ { i } \quad \xi _ { i } = \log \left( \phi _ { i } \right) = \sum _ { j } z _ { i j } \gamma _ { j }$$

var di = To?

Notice the connection between the two models. The model for the mean produce the
response for the model for the dispersion, which in turn produces the weights for the
mean model. In principle, something other than a gamma GLM could be used for the
dispersion although since we wish to model a strictly positive, continuous and typically

<!-- PageBreak -->

<!-- PageNumber="159" -->
<!-- PageHeader="Other GLMs" -->

skewed dispersion, the gamma is the obvious choice. The dispersion predictors, $Z$ are
usually a subset of the mean model predictors $X .$


<table>
<tr>
<th colspan="9">Design Vars Environmental Vars</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>$\mathrm { T }$</th>
<th>0</th>
<th>−</th>
<th>+</th>
<th>−</th>
<th>+</th>
</tr>
<tr>
<td>$F$</td>
<td>S</td>
<td>$E$</td>
<td>$t$</td>
<td>0</td>
<td>−</td>
<td>−</td>
<td>+</td>
<td>+</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td></td>
<td>6.7</td>
<td>3.4</td>
<td>5.4</td>
<td>4.1</td>
<td>3.8</td>
</tr>
<tr>
<td>−</td>
<td>−</td>
<td>−</td>
<td></td>
<td>3.1</td>
<td>1.1</td>
<td>5.7</td>
<td>6.4</td>
<td>1.3</td>
</tr>
<tr>
<td>+</td>
<td>−</td>
<td>−</td>
<td></td>
<td>3.2</td>
<td>3.8</td>
<td>4.9</td>
<td>4.3</td>
<td>2.1</td>
</tr>
<tr>
<td>−</td>
<td>+</td>
<td>−</td>
<td></td>
<td>5.3</td>
<td>3.7</td>
<td>5.1</td>
<td>6.7</td>
<td>2.9</td>
</tr>
<tr>
<td>+</td>
<td>+</td>
<td>−</td>
<td></td>
<td>4.1</td>
<td>4.5</td>
<td>6.4</td>
<td>5.8</td>
<td>5.2</td>
</tr>
<tr>
<td>−</td>
<td>−</td>
<td>+</td>
<td></td>
<td>6.3</td>
<td>4.2</td>
<td>6.8</td>
<td>6.5</td>
<td>3.5</td>
</tr>
<tr>
<td>+</td>
<td>−</td>
<td>+</td>
<td></td>
<td>6.1</td>
<td>5.2</td>
<td>6.0</td>
<td>5.9</td>
<td>5.7</td>
</tr>
<tr>
<td>−</td>
<td>+</td>
<td>+</td>
<td></td>
<td>3.0</td>
<td>3.1</td>
<td>6.3</td>
<td>6.4</td>
<td>3.0</td>
</tr>
<tr>
<td>+</td>
<td>+</td>
<td>+</td>
<td></td>
<td>4.5</td>
<td>3.9</td>
<td>5.5</td>
<td>5.0</td>
<td>5.4</td>
</tr>
</table>


Table 7.1 $F = F l o u r ,$ S=Shortening, $E = E g g s ,$
$T = O v e n$ temperature and $t = B a k i n g$ time. "+"
indicates a higher-than-normal setting while "-"
indicates $a$ lower-than-normal setting. "0"
indicates the standard setting.

For unreplicated experiments, $r _ { P a n d } ^ { 2 } r _ { D a r e } ^ { 2 }$ two possible choices for $d _ { i } .$ If replications
are available, then a more direct estimate of dispersion would be possible. For more
details on the formulation, estimation and inference for these kinds of model see
McCullagh and Nelder (1989), Box and Meyer (1986), Bergman and Hynen (1997) and
Nelder, Lee, Bergman, Hynen, Huele, and Engel (1998).

In the last three citations, data from a welding-strength experiment was analyzed.
There were nine two-level factors and 16 unreplicated runs. Previous analyses have
differed on which factors are significant for the mean. We found that two factors, Drying
and Material, were apparently strongly significant, while the significance of others,
including Preheating, was less clear. We fit a linear model for the mean using these three
predictors:

\> data (weldstrength)

\> lmod <- lm(Strength ~ Drying + Material + Preheating,
weldstrength)

\> summary(lmod)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>t value</th>
<th>Pr (&gt;|t|)</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>43.625</td>
<td></td>
<td>0.262</td>
<td>166.25</td>
<td>&lt; 2e-16</td>
</tr>
</table>


<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 162


<table>
<tr>
<td>Drying</td>
<td>2.150</td>
<td>0.262</td>
<td>8.19</td>
<td>2.9e-06</td>
</tr>
<tr>
<td>Material</td>
<td>-3.100</td>
<td>0.262</td>
<td>-11.81</td>
<td>5.8e-08</td>
</tr>
<tr>
<td>Preheating</td>
<td>-0.375</td>
<td>0.262</td>
<td>-1.43</td>
<td>0.18</td>
</tr>
<tr>
<td colspan="5">Residual standard error: 0.525 on 12 degrees of freedom</td>
</tr>
<tr>
<td colspan="5">$\mathrm { M u l t i p l e }$ R-Squared: 0.946, Adjusted R-squared: 0.932</td>
</tr>
<tr>
<td colspan="5">F-statistic: 69.6 on 3 and 12 DF, $p - v a l u e :$ $7 . 3 9 e - 0 8$</td>
</tr>
</table>


Following a suggestion of Smyth, Huele, and Verbyla (2001), we use the squared
studentized residuals, $\left( y _ { i } - j _ { i } \right) ^ { 2 } / \left( 1 - h _ { i } \right) _ { n }$ the response in the dispersion with a gamma
GLM using a log-link and weights of $1 - h _ { i } .$ Again, we follow the suggestion of some
previous authors as to which predictors are important for modeling the dispersion:

\> h <- influence(lmod)$hat
> d <- residuals(lmod)^2/(1-h)
> gmod <- glm (d ~ Method+Preheating,
family=Gamma (link=log) ,
weldstrength, $\left. \mathrm { w e i g h t s } = 1 - h \right)$

Now feedback the estimated weights to the linear model:

\> w <- 1/ fitted (gmod)
> lmod <- lm(Strength ~ Drying + Material + Preheating,
weldstrength, weights=w)

We now iterate until convergence, where we find that:

\> summary(lmod)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>43.825</td>
<td>0.108</td>
<td colspan="2">406.83 &lt; 2e-16</td>
</tr>
<tr>
<td>Drying</td>
<td>1.869</td>
<td>0.045</td>
<td colspan="2">41.53 2.5e-14</td>
</tr>
<tr>
<td>Material</td>
<td>-3.234</td>
<td>0.108</td>
<td colspan="2">-30.03 1.2e-12</td>
</tr>
<tr>
<td>Preheating</td>
<td>-0.239</td>
<td>0.101</td>
<td>-2.35</td>
<td>0.036</td>
</tr>
</table>


Residual standard error: 1 on 12 degrees of freedom
Multiple R-Squared: 0.995, Adjusted R-squared: 0.994
F-statistic: 877 on 3 and 12 DF, p-value: 2.56e-14

We note that Preheating is now significant in contrast to the initial mean model fit. The
output for the dispersion model is:

\> summary (gmod)

Coefficients:

Estimate Std. Error t value $\mathbb{P} \underline { r } \left( > | t | \right)$
(Intercept)
-3.064
0.356

-8.60 0.0000010

Material
-3.037
0.413
-7.35 0.0000056

Preheating
2.904

0.413 7.03 0.0000089

Null deviance: 57.919 on 15 degrees of freedom
0.50039)

<!-- PageBreak -->

<!-- PageNumber="161" -->
<!-- PageHeader="Other GLMs" -->
<!-- PageHeader="Residual deviance: 20.943 on 13 degrees of freedom" -->

The standard errors are not correct in this output and further calculation, described in
Smyth, Huele, and Verbyla (2001), would be necessary. This would result in somewhat
larger standard errors (about twice the size), but the two factors would still be significant.


## 7.4 Quasi-Likelihood

Suppose that we are able to specify the link and variance functions of the model for some
new type of data, but that we do not have a strong idea about the appropriate
distributional form for the response. For example, suppose that we specify an identity
link and constant variance. This would be typical in the standard regression setting. We
can use least squares to estimate the regression parameters. If we want to do some
inference, then formally we need to assume a Gaussian distribution for the errors (or
equivalently, the response). We know that the inference is fairly robust to nonnormality
especially as the sample size gets larger. The important part of the model specification is
the link and variance; the outcome is less sensitive to the distribution of the response.

The same effect holds for other GLMs. Provided we have a larger sample, the results
are not sensitive to smaller deviations from the distributional assumptions. The link,
variance and independence assumptions are far more important. Now suppose that we
were to specify a link and variance function combination that does not correspond to any
of the standard GLMs. An examination of the fitting procedure for GLMs reveals that
$\mathrm { o n l y }$ the link and variance functions are used and no distributional assumptions are
necessary. This opens up new modeling possibilities because one might well be able to
suggest reasonable link and variance functions but not know a suitable distribution.

Computation of $\widehat { \beta } _ { \mathrm { a n c } }$ standard errors is often not enough and some form of inference
is required. To compute a deviance, we need a likelihood and to compute a likelihood we
need a distribution. At this point, we need a suitable substitute for a likelihood that can be
computed without assuming a distribution.

Let $Y _ { i }$ have mean $\mu _ { i }$ and variance $\Phi V \left( \mu _ { i } \right) _ { \cdot \mathrm { W } _ { \mathrm { e } } }$ assume that $Y _ { i }$ are independent. We
define a score, $U _ { i } :$

$$U _ { i } = \frac { Y _ { i } - \mu _ { i } } { \phi V \left( \mu _ { i } \right) }$$

Now:

$$E U _ { i } = 0$$

$$U _ { i } = \frac { 1 } { \phi V \left( H _ { i } \right) }$$
$$- E \frac { \partial U _ { i } } { \partial \mu _ { i } } = - E \frac { - \phi V \left( \mu _ { i } \right) - \left( Y _ { i } - \mu _ { i } \right) \phi V ^ { \prime } \left( \mu _ { i } \right) } { \left[ \phi V \left( \mu _ { i } \right) \right] ^ { 2 } } = \frac { 1 } { \phi V \left( \mu _ { i } \right) }$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 164" -->

These properties are shared by the derivative of the log-likelihood, $l ^ { \prime } .$ This suggests that
we can use $U$ in place of $l ^ { \prime } .$ So we define:

$$Q _ { i } = \int _ { y _ { i } } ^ { \mu _ { i } } \frac { y _ { i } - t } { \phi V \left( t \right) } d t$$

The intent is that $Q$ should behave like the log-likelihood. We then define the log quasi-
likelihood for all $n$ observations as:

$$Q = \sum _ { i = 1 } ^ { n } Q _ { i }$$

The usual asymptotic properties expected of maximum likelihood estimators also hold for
quasi-likelihood-based estimators as may be seen in McCullagh (1983).

Notice that the quasi-likelihood depends directly only on the variance function and
that the choice of distribution also determines only the variance function. So the choice of
variance function is associated with the random structure of the model while the link
function determines the relationship with the systematic part of the model.

For the variance functions associated with the members of the exponential family
distribution, the quasi-likelihood corresponds exactly to the log-likelihood. However,
there is an advantage to using the quasi-likelihood approach for models with variance
functions corresponding to the binomial and Poisson distribution. The regular GLMs
assume $\phi = \mathrm { I } _ { \mathrm { w h e r e a s } }$ the corresponding quasi-binomial and quasi-Poisson GLMs allow
for the dispersion $\Phi _ { \mathrm { t o } }$ be a free parameter which is useful in modeling overdispersion.
One curious possibility is that some choices of $\mathrm { V } \left( \mu \right)$ may not correspond to a known, or
even any, distribution.

$\widehat { \beta } _ { \mathrm { i s } }$ obtained by maximizing $Q .$ Everything proceeds as in the standard GLMs except
for the estimation of "since the likelihood approach is not reliable here. We recommend:

$$\ddot { \Phi } = \frac { X ^ { 2 } } { n - p }$$

Although quasi-likelihood estimators are attractive because they require fewer
assumptions, they are generally less efficient than the corresponding regular likelihood-
based estimator. So if you have information about the distribution, you are advised to use
it.

The inferential procedures are similar to those for standard GLMs. Recall that the
regular deviance for a model is formed from the difference in log-likelihoods for the
model and the saturated model:

$$D \left( y , i t \right) = - 2 \phi \sum _ { i } \left( l \left( \widehat { \mu } _ { i } | y _ { i } \right) - I \left( y _ { i } | y _ { i } \right) \right)$$

so by analogy the quasi-deviance is $- 2 0 2 b e c a u s e$ the contribution from the saturated
model is zero. The $\Phi _ { \mathrm { c a n c e l s } } ,$ so the quasi-deviance is just:

<!-- PageBreak -->

<!-- PageNumber="163" -->
<!-- PageHeader="Other GLMs" -->

$$Q = - 2 \sum _ { i } \int _ { y _ { i } } ^ { H _ { i } } \frac { y _ { i } - t } { V \left( t \right) } d t$$

In Allison and Cicchetti (1976), data on the sleep behavior of 62 mammals is presented.
Suppose we are interested in modeling the proportion of sleep spent dreaming as a
function of the other predictors: the weight of the body and the brain, the lifespan, the
gestation period and the three constructed indices measuring vulnerability to predation,
exposure while sleeping and overall danger:

\> data (mammalsleep)
> mammalsleep$pdr <- with (mammalsleep, dream/sleep)
> summary (mammalsleep$pdr)


<table>
<tr>
<th>Min.</th>
<th>1st Qu.</th>
<th>Median</th>
<th>Mean</th>
<th>3rd Qu.</th>
<th>Max.</th>
<th>NA'S</th>
</tr>
<tr>
<td>0.000</td>
<td>0.118</td>
<td>0.176</td>
<td>0.186</td>
<td>0.243</td>
<td>0.462</td>
<td>14.000</td>
</tr>
</table>


We notice that the proportion of time spent dreaming varies from zero up to almost half
the time. $A$ normal model seems inappropriate while transformations are problematic. We
attempt to model the proportion response directly. A logit link seems sensible since the
response is restricted between zero and one. Furthermore, we might expect the variance
to be greater for moderate values of the proportion $\mu$ and less as $\mu$ approaches zero or one
because of the nature of the measurements. This suggests a variance function of the
approximate form $\mu \left( 1 - \mu \right) .$ This corresponds to the binomial GLM with the canonical logit
link and yet the response is not binomial. We propose a quasi-binomial:

\> modl <- glm (pdr ~
log (body) +log (brain) +log (lifespan) +log (gestation)
+predation+exposure+danger,
family=quasibinomial, mammalsleep)

where we have logged many of the predictors because of skewness. Since we now have a
free dispersion parameter, we must use F-tests to compare models:

\> dropl (modl, test="F")
Single term deletions


<table>
<tr>
<th></th>
<th colspan="2">Df Deviance</th>
<th colspan="2">value (F)</th>
</tr>
<tr>
<td>&lt;none&gt;</td>
<td></td>
<td>1.57</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$l o g \left( b o d y \right)$</td>
<td>1</td>
<td>1.78</td>
<td>4.51</td>
<td>0.041</td>
</tr>
<tr>
<td>log (brain)</td>
<td>1</td>
<td>1.59</td>
<td>0.33</td>
<td>0.568</td>
</tr>
<tr>
<td>$\log \left( 1 1 \text { fespan } \right)$</td>
<td>-1</td>
<td>1.65</td>
<td>1.79</td>
<td>0.189</td>
</tr>
<tr>
<td>$\log \left( \mathrm { q e s t a t i o n } \right.$</td>
<td>1</td>
<td>1.62</td>
<td>1.15</td>
<td>0.292</td>
</tr>
<tr>
<td>predation</td>
<td>1</td>
<td>1.57</td>
<td>0.10</td>
<td>0.749</td>
</tr>
<tr>
<td>exposure</td>
<td>1</td>
<td>1.58</td>
<td>0.32</td>
<td>0.575</td>
</tr>
<tr>
<td>danger</td>
<td>1</td>
<td>1.58</td>
<td>0.31</td>
<td>0.579</td>
</tr>
</table>


We might eliminate predation as the least significant variable. Further sequential
backward elimination results in:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 166

\> modl <- glm (pdr ~ log (body) +log (lifespan) +danger,
family=quasibinomial, mammalsleep )
> summary (modl)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr (&gt; |t|)</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-0.4932</td>
<td>0.2913</td>
<td>-1.69</td>
<td>0.09796</td>
</tr>
<tr>
<td>log (body)</td>
<td>0.1463</td>
<td>0.0384</td>
<td>3.81</td>
<td>0.00046</td>
</tr>
<tr>
<td>log (lifespan)</td>
<td>-0.2866</td>
<td>0.1080</td>
<td>-2.65</td>
<td>0.01126</td>
</tr>
<tr>
<td>danger</td>
<td>-0.1732</td>
<td>0.0600</td>
<td>-2.89</td>
<td>0.00615</td>
</tr>
</table>


(Dispersion parameter for quasibinomial family taken to
be 0.040654)

Null deviance: 2.5088 on 44 degrees of freedom
Residual deviance: 1.7321 on 41 degrees of freedom

AIC: NA

Notice that the dispersion parameter is far less than the default value of one that we
would see for a binomial. Furthermore, the AIC is not calculated since we do not have a
true likelihood. We see that the proportion of time spent dreaming increases for heavier
mammals that live less time and live in less danger. Notice that the relatively large
residual deviance compared to the null deviance indicates that this is not a particularly
well-fitting model.

The usual diagnostics should be performed. Here are two selected plots that have some
interest:

\> ll <- row.names(na.omit(mammalsleept,c(1,6,10,11)]))

\> halfnorm(cooks.distance(modi),labs=ll)

\> plot (predict (modl) , residuals (modl, type="pearsonn) ,
xlab="Linear Predictor", ylab="Pearson Residuals")


<figure>
<figcaption>Figure 7.5 A half-normal plot of the Cook statistics is shown on the left and a plot of the Pearson residuals against the fitted linear predictors is shown on the right.</figcaption>

0.2 0.3 0.4 0.5

Asian.ele

0.0

0.4

Sorted Data

Pearson Residuals

0.2

0.0

0.1

Echidna

0.0

-0.4

0.0

0.5

1.0

1.5

2.0

-2.0

-1.5

-1.0

Half-normal quantiles

Linear Predictor

</figure>


<!-- PageBreak -->

<!-- PageNumber="165" -->
<!-- PageHeader="Other GLMs" -->

In the first panel of Figure 7.5, we see that the Asian elephant is quite influential and a fit
without this case should be considered. In the second panel, we see that a pattern of
constant variation indicating that our choice of variance function was reasonable. We
used the Pearson residuals because these explicitly normalize the raw residuals using the
variance function making the check more transparent. Even so, the deviance residuals
would have served the same purpose.


### Exercises

1\. The relationship between corn yield (bushels per acre) and nitrogen (pounds per acre)
fertilizer application were studied in Wisconsin. The data may be found in cornnit.

(a) Using (Gaussian) linear model methods, represent the relationship between the
yield response and the nitrogen predictor. You will need to find appropriate
transformations for the data. Present a quantitative interpretation for the effect of
nitrogen fertilizer on yield.

(b) Now develop a GLM for the data that does not (explicitly) transform the response.
Describe quantitatively the relationship between the response and the predictor and
compare it to the linear model you found in the previous question.

2\. An experiment was conducted as part of an investigation to combat the effects of
certain toxic agents. The survival time of rats depended on the type of poison used and
the treatment applied. The data is found in rats.

(a) Construct a linear model for the data bearing in mind that some transformation of
the response may be necessary and that the possibility of interactions needs to be
considered. Interpret the effects of the poisons.

(b) Build an inverse Gaussian GLM for this data. Select an appropriate link function
and perform diagnostics to verify your choices. Interpret the effects of the poisons.

3\. Components are attached to an electronic circuit card assembly by a wave-soldering
process. The soldering process involves baking and preheating the circuit card and
then passing it through a solder wave by conveyor. Defects arise during the process.
Design is 27-3 with 3 replicates. The data is found in wavesolder. Build a pair of
models for the mean and dispersion in the number of defects. Investigate which factors
are significant in the two models.

4\. Data were collected from 39 students in a University of Chicago MBA class and
presented in happy. Happiness was measured on a 10 point scale. The response could
be viewed as ordinal, but a quasi-likelihood approach is also possible. Build a quasi-
GLM selecting appropriate link and variance functions. Interpret the effect of the
predictors.

5\. The leafblotch data shows the percentage leaf area affected by leaf blotch on 10
varieties of barley at nine different sites. The data comes from Wedderburn (1974).
The data is analyzed in McCullagh and Nelder (1989), which motivates the following
questions:

(a) Fit a quasi-GLM with a logit link and a $\mu \left( 1 - \mu \right)$ variance function. Construct a
diagnostic plot that shows that this is not a good choice of variance function.

<!-- PageBreak -->

<!-- PageNumber="168" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->

(b) A better variance function is $\mu ^ { 2 } \left( 1 - \mu \right) ^ { 2 }$ and yet this is not one of the available
choices in $\mathrm { R } .$ However, the effect may be obtained by the appropriate use of
weighting. Define weights as a function $\mathrm { o f } \mu$ that, when used in conjunction with a
variance function of $\mu \left( 1 - \mu \right) ,$ achieve the effect of a $\mu ^ { 2 } \left( 1 - \mu \right) ^ { 2 }$ variance function.
Note that some iteration will be required in the fitting.

(c) Reprogram $R$ to allow for $a \mu ^ { 2 } \left( 1 - \mu \right) ^ { 2 }$ function. (This is more challenging.)

6\. One hundred twenty-five fruitflies were divided randomly into five groups of 25 each.
The response was the longevity of the fruitfly in days. One group was kept solitary,
while another was kept individually with a virgin female each day. Another group was
given eight virgin females per day. As an additional control the fourth and fifth groups
were kept with one or eight pregnant females per day. Pregnant fruitflies will not
mate. The thorax length of each male was measured as this was known to affect
longevity. The data is presented in fruitfly.

Show how a gamma GLM may be used to model the lifetimes as a function of the
predictors. Interpret your chosen model.

7\. The truck data concerns an experiment to optimize the production of leaf springs for
trucks. $A$ heat treatment is designed so that the free height of the spring should come
as close to eight inches as possible. We can vary five factors at two levels each. A $2 ^ { 5 - 1 }$
fractional factorial experiment with three replicates was carried out. The data comes
from Pignatiello and Ramberg (1985). McCullagh and Nelder (1989) recommended a
Gaussian linear model for the mean response and gamma model for the variance. Fit
these models using $\mathrm { R }$ and use them to select the best combination of factors given the
purpose of the experiment.

<!-- PageBreak -->


## CHAPTER 8 Random Effects

Grouped data arise in almost all areas of statistical application. Sometimes the grouping
structure is simple, where each case belongs to single group and there is only one
grouping factor. More complex datasets have a hierarchical or nested structure or include
longitudinal or spatial elements. All such data share the common feature of correlation of
observations within the same group and so analyses that assume independence of the
observations will be inappropriate. The use of random effects is one common and
convenient way to model such grouping structure.

A fixed effect is an unknown constant that we try to estimate from the data. Fixed
effect parameters are commonly used in linear and generalized linear models as we have
presented them earlier in this book. In contrast, a random effect is a random variable. It
does not make sense to estimate a random effect; instead, we try to estimate the
parameters that describe the distribution of this random effect.

Consider an experiment to investigate the effect of several drug treatments on a
sample of patients. Typically, we are interested in specific drug treatments and so we
would treat the drug effects as fixed. However, it makes most sense to treat the patient
effects as random. It is often reasonable to treat the patients as being randomly selected
from a larger collection of patients whose characteristics we would like estimate.
Furthermore, we are not particularly interested in these specific patients, but in the whole
population of patients. $A$ random effects approach to modeling effects is more ambitious
in the sense that it attempts to say something about the wider population beyond the
particular sample. Blocking factors can often be viewed as random effects, because these
often arise as a random sample of those blocks potentially available.

There is some judgment required in deciding when to use fixed and when to use
random effects. Sometimes the choice is clear, but in other cases, reasonable statisticians
may differ. In some analyses, random effects are used simply to induce a certain
correlation structure in the data and there is sense in which the chosen levels represent a
sample from a population. Gelman (2005) remarks on the variety of definitions for
random effects and proposes a particular straightforward solution to the dilemma of
whether to use fixed or random effects-he recommends always using random effects.

A mixed effects model has both fixed and random effects. A simple example of such a
model would be a two-way analysis of variance (ANOVA):

$$y _ { i j k } = \mu + \tau _ { i } + v _ { j } + 8 _ { i j k }$$

where the $\mu$ and $\tau _ { i }$ are fixed effects and the error, $\varepsilon _ { i i k }$ and the random effects $v _ { j }$ are
independent and identically distributed $N \left( 0 , \sigma ^ { 2 } \right)$ and $N \left( 0 , \sigma _ { v } ^ { 2 } \right)$ ~(0,o;),respectively.

We would want to estimate the $\tau _ { i }$ and test the hypothesis $H _ { 0 } : \tau _ { i } = 0 \forall i _ { \text { while } }$ we
would estimate $\sigma _ { \mathrm { v a n d } } ^ { 2 }$ test $H _ { 0 } : \sigma _ { v } ^ { 2 } = 0$ 0.Notice the difference: we need to estimate and

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 170" -->

test several fixed effect parameters while we need only estimate and test a single random
effect parameter.

In the following sections, we consider estimation and inference for mixed-effect
models and then illustrate the application to several common designs.


### 8.1 Estimation

This is not as simple as it was for fixed effects models, where least squares is an easily
applied method with many good properties. Let's start with the simplest possible random
effects model: a one-way ANOVA design with a factor at a levels:

$$y _ { i j } = \mu + \alpha _ { i } + e _ { i j } \quad i = 1 , \ldots , a \quad j = 1 , \ldots , n$$

where the as and $E s$ have mean zero, but $\sigma _ { t } ^ { 2 } .$ These
variances are known as the variance components. Notice that this induces a correlation
between observations at the same level equal to:

$$p = \frac { \sigma _ { a } ^ { 2 } } { \sigma _ { a } ^ { 2 } + \sigma _ { E } ^ { 2 } }$$

This is known as the intraclass correlation coefficient (ICC). In the limiting case when
there is no variation between the levels, $\sigma _ { a } = 0$ so then $\rho = 0 .$ Alternatively, when the
variation between the levels is much larger than that within the levels, the value of $\rho$ will
approach 1. This illustrates how random effects generate correlations between
observations.

For simplicity, let there be an equal number of observations $n$ per level. We can
decompose the variation as follows:

$$\sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \left( y _ { i j } - \bar { y } _ { n } \right) ^ { 2 } = \sum _ { i = 1 } ^ { a } \sum _ { j = 1 } ^ { n } \left( y _ { i j } - \bar { y } _ { i } \right) ^ { 2 } + \sum _ { i = 1 } ^ { a } \sum _ { j = 1 } ^ { n } \left( \bar { y } _ { i } - \bar { y } _ { n } \right) ^ { 2 }$$

or $S S T = S S E + S S A .$ SSE is the residual sum of squares, SST is the total sum of squares
(corrected for the mean) and SSA is the sum of squares due to a. These quantities are
often displayed in an ANOVA table along with the degrees of freedom associated with
each sum of squares. Dividing through by the respective degrees of freedom, we obtain
the mean squares, MSE and MSA. Now we find that:

$E \left( S S E \right) = a \left( n - 1 \right) \sigma _ { t } ^ { 2 } ,$

$$E \left( S S A \right) = \left( a - 1 \right) \left( n \sigma _ { a } ^ { 2 } + \sigma _ { E } ^ { 2 } \right)$$

which suggests using the estimators:

$$\overrightarrow { \sigma } _ { \mathrm { E } } ^ { 2 } = \mathrm { S S E } / \left( a \left( n - 1 \right) \right) = \mathrm { M S E } ,$$
$$d _ { a } ^ { 2 } = \frac { \mathrm { S S A } / \left( a - 1 \right) - \mathrm { G } _ { \mathrm { f } } ^ { 2 } } { n } = \frac { M S A - M S E } { n }$$

This method of estimating variance components can be used for more complex designs.
The ANOVA table is constructed, the expected mean squares calculated and the variance
components obtained by solving the resulting equations. These estimators are known as

<!-- PageBreak -->

<!-- PageNumber="171" -->
<!-- PageHeader="Random effects" -->

ANOVA estimators. These were the first estimators developed for variance components.
They have the advantage of taking explicit forms suitable for hand calculation which was
important in precomputing days, but they have a number of disadvantages:

1\. The estimates can take negative values. For example, in our situation above, if
$M S A < M S E$ then $\widehat { \sigma } _ { \mathfrak{a} } ^ { 2 } < 0$ 0.This is rather embarrassing since variances cannot be
negative. Various fixes have been proposed, but these all take away from the original
simplicity of the estimation method.

2\. A balanced design has an equal number of observations per cell, where cell is defined
as the finest subdivision of the data according to the factors. In such circumstances,
the ANOVA decomposition into sums of squares is unique. For unbalanced data, this
is not true and we must choose which ANOVA decomposition to use which will in
turn affect the estimation of the variance components. Various rules have been
suggested about how the decomposition should be done, but none of these have
universal appeal.

3\. The need for complicated algebraic calculations. Formulae for the simpler models are
easy to find and coded in software. More complex models will require difficult and
opaque constructions.

We would like a method that would avoid negative variances, work unambiguously for
unbalanced data and that can be applied in a transparent and straightforward manner.
Maximum likelihood (ML) estimation satisfies these requirements. This does require that
we assume some distribution for the errors and the random effects. The usual assumption
is normality; ML would work for other distributions, but these are almost never
considered.

For a fixed effect model with normal errors, we can write:

$y = X \beta + \varepsilon$ or $y \sim N \left( X \beta , \sigma ^ { 2 } I \right)$

where $X$ is an $n \times p$ model matrix and $\beta$ is a vector of length $p .$ We can generalize to a
mixed effect model with a vector $\gamma$ of $q$ random effects with associated model matrix $\mathrm { Z }$
which has dimension $n \times q .$ Then we can model the response y, given the value of the
random effects as:

$y = X \beta + Z \gamma + 8$ or yly~N(XB+Zy,o2I)

If we further assume that the random effects $\gamma \sim N \left( 0 , \sigma ^ { 2 } D \right)$ then var y=var $Z \gamma ^ { + }$ var
$8 = \sigma ^ { 2 } Z D Z ^ { T } + \sigma ^ { 2 } I$ and we can write the unconditional distribution of y as:

$y \sim N \left( X \beta , \sigma ^ { 2 } \left( I + Z D Z ^ { T } \right) \right)$

If we knew $D \mathrm { i }$ then we could estimate $\beta$ using generalized least squares; see, for example,
Chapter 6 in Faraway (2004). However, the estimation of the variance components, $D ,$ is
often one purpose of the analysis. Standard maximum likelihood is one method of
estimation that can be used here. If we let $V = I + Z D Z ^ { I } ,$ then the joint density for the
response is:

$$\frac { 1 } { 2 \pi ^ { n / 2 } | \sigma ^ { 2 } V | ^ { 1 / 2 } } e ^ { - \frac { 1 } { 2 \sigma ^ { 2 } } \left( y - X \beta \right) ^ { T } V ^ { - 1 } \left( y - X \beta \right) }$$

<!-- PageBreak -->

$$l \left( \beta , \sigma , D | y \right) = - \frac { n } { 2 } \log 2 \pi - \frac { 1 } { 2 } \log | \sigma ^ { 2 } V | - \frac { 1 } { 2 \sigma ^ { 2 } } \left( y - X \beta \right) ^ { T } V ^ { - 1 } \left( y - X \beta \right)$$
$$\begin{array}{} { \text { Extending the linear model with } R \quad 1 7 2 } \end{array}$$
so that the log-likelihood for the data is:

This can be optimized to find maximum likelihood estimates of $\beta ,$ $\sigma ^ { 2 }$ and $D .$ This is
straightforward in principle, but there may be difficulties in practice. More complex
models involving larger numbers of random effects parameters can be difficult to
estimate. One particular problem is that the variance cannot be negative so the MLE for
the variance might be zero. This causes difficulties in the optimization when the
unrestricted MLE has a maximum that is negative. This forces us to set that variance
estimate to be zero where the derivative of the likelihood will not be zero. This
complicates the numerical calculation.

Standard errors can obtained using the usual large sample theory for maximum
likelihood estimates. The variance can be estimated using the inverse of the negative
second derivative of the log-likelihood evaluated at the MLE.

MLEs have some drawbacks. One particular problem is that they are biased. For
example, consider an i.i.d. sample of normal data $x _ { 1 } , \ldots , x _ { n }$ then the MLE is:

$$6 ^ { 2 } = \frac { \sum _ { i = 1 } ^ { n } \left( x _ { i } - x \right) ^ { 2 } } { n }$$

$A$ denominator of $n - 1$ is needed for an unbiased estimator. Similar problems occur with
the estimation of variance components. Given that the number of levels of a factor may
not be large, the bias of the MLE of the variance component associated with that factor
may be quite large. Restricted maximum likelihood (REML) estimators are an attempt to
get round this problem. The idea is to take a linear combination of the response, $k ,$ such
that $k ^ { T } X = 0 .$ We then have:

$k ^ { T } y \sim N \left( 0 , K ^ { T } V K \right)$

We can then proceed to maximize the likelihood based on $k ^ { T } y$ which does not involve any
of the fixed effect parameters. Once the random effect parameters have been estimated, it
is simple enough to obtain the fixed effect parameter estimates. REML generally
produces less biased estimates. For balanced data, the REML estimates are usually the
same as the ANOVA estimates.

We illustrate the fitting methods using some data from an experiment to test the paper
brightness depending on a shift operator described in Sheldon (1960). We start with a
fixed effects one-way ANOVA:

\> data (pulp)
> op <- options (contrasts=c ("contr. sum",
"contr . poly") )
> lmod <- aov(bright ~ operator, pulp)
> summary(lmod)


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq F</th>
<th>value</th>
<th>Pr (&gt;F)</th>
</tr>
<tr>
<td>operator</td>
<td>3</td>
<td>1.340</td>
<td>0.447</td>
<td>4.2</td>
<td>0.023</td>
</tr>
<tr>
<td>Residuals</td>
<td>16</td>
<td>1.700</td>
<td>0.106</td>
<td></td>
<td></td>
</tr>
</table>


\> coef(lmod)

<!-- PageBreak -->

<!-- PageNumber="173" -->
<!-- PageHeader="Random effects" -->


<table>
<tr>
<th>(Intercept)</th>
<th>operatorl</th>
<th>operator2</th>
<th>operators</th>
</tr>
<tr>
<td>60.40</td>
<td>-0.16</td>
<td>-0.34</td>
<td>0.22</td>
</tr>
</table>


\> options (op)

We have specified sum contrasts here instead of the default treatment contrasts to make
the later connection to the corresponding random effects clearer. The aov function is just
a wrapper for the standard 1m function that produces results more appropriate for
ANOVA models. We see that the operator effect is significant with a p-value of 0.023.
The estimate of $\sigma ^ { 2 }$ is 0.106 and the estimated overall mean is 60.4. For sum contrasts,
$\Sigma \alpha _ { i } = 0 ,$ so we can calculate the effect for the fourth operator as $0 . 1 6 + 0 . 3 4 - 0 . 2 2 = 0 . 2 8 .$

Turning to the random effects model, we can compute the variance of the operator
effects, $\sigma _ { a } ^ { 2 }$ using the formula above as:

\> $\left( 0 . 4 4 7 - 0 . 1 0 6 \right) / 5$
[1] 0.0682

Now we demonstrate the maximum likelihood estimators. The original $\mathrm { R }$ package for
fitting mixed effects models was nlme as described in Pinheiro and Bates (2000). More
recently, Bates (2005) introduced an improved version with the package lme4 which we
shall use here:

\> library (Ime4)
> mmod <- lmer (bright ~ 1+ (1 | operator) , pulp)
> summary (mmod)

Linear mixed-effects model fit by REML
Formula: bright ~ 1 + (1 | operator)
Data: pulp

AIC
BIG logLik deviance REMLdeviance

24.626 27.613 -9.3131

16.637
18.626

Random effects:


<table>
<tr>
<th colspan="2">Groups Name</th>
<th>Variance Std. Dev.</th>
</tr>
<tr>
<td colspan="2">operator (Intercept)</td>
<td>0.0681 0.261</td>
</tr>
<tr>
<td colspan="2">Residual</td>
<td>0.1062 0.326</td>
</tr>
<tr>
<td>#</td>
<td>of obs: 20, groups :</td>
<td>operator, 4</td>
</tr>
</table>


Fixed effects:
Estimate Std. Error DF t value $\mathrm { P r } \left( > | t | \right)$

(Intercept)
60.400
0.149 19
404
<2e-16

The model has fixed and random effects components. The fixed effect here is just the
intercept represented by the first 1 in the model formula. The random effect is
represented by (1|operator) indicating that the data is grouped by operator and the 1
indicating that the random effect is constant within each group. The parentheses are
necessary to ensure that expression is parsed in the correct order.

The default fitting method is REML. We see that this gives identical estimates to the
ANOVA method above $- 6 ^ { 2 } = 0 . 1 0 6 ,$ $\widehat { \sigma } _ { \mathrm { f r } } ^ { 2 } = 0 . 0 6 8$ and $\widehat { \mu } = 6 0 . 4$ unbalanced
designs, the REML and ANOVA estimators are not necessarily identical. The standard

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 174" -->

deviations are simply the square roots of the variances and not estimates of the
uncertainty in the variances.

The maximum likelihood estimates may also be computed:

\> smod <- lmer (bright ~ 1+ (1 | operator) , pulp,
method="ML")
> summary ( smod)
Linear mixed-effects model fit by maximum likelihood
Formula: bright ~ 1 + (1 | operator)
Data: pulp

AIC
BIG
logLik deviance REMLdeviance
22.512 25.499 -8.2558
16.512
18.738

Random effects:


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>operator</td>
<td>(Intercept)</td>
<td>0.0482</td>
<td>0.219</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td>0.1118</td>
<td>0.334</td>
</tr>
<tr>
<td colspan="4"># of obs: 20, groups : operator, 4 Fixed effects:</td>
</tr>
</table>


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>DF</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>60.400</td>
<td></td>
<td>0.129</td>
<td>19</td>
<td>467</td>
<td>&lt;2e-16</td>
</tr>
</table>


As can be seen, the between-subjects variance, 0.0482, is smaller than with the REML
method. Because the total variance is partitioned, this means the withinsubjects variance,
0.1118, is larger than before.


### 8.2 Inference

Using standard likelihood theory, we may derive a test to compare two nested
hypotheses, $H _ { 0 }$ and $H _ { 1 } ,$ by computing the likelihood ratio test statistic:

$$2 \left( l \left( \widehat { \beta } _ { 1 } , \widehat { \sigma } _ { 1 } , \widehat { D } _ { 1 } | y \right) - l \left( \widehat { \beta } _ { 0 } , \widehat { \sigma } _ { 0 } , \widehat { D } _ { 0 } | y \right) \right)$$

where $\widehat { \beta } _ { 0 } , \widehat { \sigma } _ { 0 } , \widehat { D } _ { 0 } { } _ { \mathrm { a r } } { } _ { \mathrm { e } }$ the MLEs of the parameters under the null hypothesis and
$\widehat { \beta } _ { \mathrm { l } } ,$ $\widehat { \mathbb{G} } _ { 1 } ,$ $\widehat { D } _ { \mathrm { l a r } }$ the MLEs of the parameters under the alternative hypothesis.

The null distribution of this test statistic is approximately chi-squared with degrees of
freedom equal to difference in the dimensions of the two parameters spaces (the
difference in the number of parameters when the models are identifiable).

Unfortunately, this test is only approximate and requires several assumptions-see a
text such as Cox and Hinkley (1974) for more details. One crucial assumption is that the
parameters under the null are not on the boundary of the parameter space. Since we are
often interested in testing hypotheses about the random effects that take the form
$H _ { 0 } : \ddot { \sigma } ^ { 2 } = 0 , \text { this } a$ real concern. Furthermore, even if the conditions are met, the $x ^ { 2 }$
approximation is sometimes poor.

Testing the fixed effects: If you plan to use the likelihood ratio test to compare two
nested models that differ only in their fixed effects, you cannot use the REML estimation
method. The reason is that REML estimates the random effects by considering linear

<!-- PageBreak -->

<!-- PageNumber="175" -->
<!-- PageHeader="Random effects" -->

combinations of the data that remove the fixed effects. If these fixed effects are changed,
the likelihoods of the two models will not be directly comparable. Use ordinary
maximum likelihood in this situation if you also wish to use the likelihood ratio test.

The p-values generated by the likelihood ratio test for fixed effects are approximate
and unfortunately tend to be too small, thereby sometimes overstating the importance of
some effects. We may use bootstrap methods to find more accurate p-values for the
likelihood ratio test. The usual bootstrap approach is nonparametric in that no distribution
is assumed. Since we are willing to assume normality for the er-rors and the random
effects, we can use a technique called the parametric bootstrap. We generate data under
the null model using the fitted parameter estimates. We compute the likelihood ratio
statistic for this generated data. We repeat this many times and use this to judge the
significance of the observed test statistic. This approach will be demonstrated below.

An alternative approach is to condition on the estimated values of the random effect
parameters and then use standard F- or t-tests. This assumes that the covariance of the
random part of the model, $D ,$ is equal to its estimated value and proceeds as one would
for generalized least squares.

Testing the random effects: In most cases, a test of random effects will involve a
hypothesis of the form $H _ { 0 } : \sigma ^ { 2 } = 0 .$ The standard derivation of the asymptotic $x ^ { 2 }$
distribution for the likelihood ratio statistic depends on the null hypothesis lying in the
interior of the parameter space. This assumption is broken when we test if a variance is
zero. The null distribution in these circumstances is unknown in general and we must
resort to numerical methods if we wish for precise testing. If you do use the $x ^ { 2 }$
distribution with the usual degrees of freedom, then the test will tend to be
conservative-the p-values will tend to be larger than they should be. This means that if
you observe a significant effect using the $x ^ { 2 }$ approximation, you can be fairly confident
that it is actually significant. Small, but not significant, p-values might spur one to use
more accurate, but time-consuming, bootstrap methods.

Expected mean squares: Another method of hypothesis testing is based on the sums
of squares found in the ANOVA decompositions. These tests are sometimes more
powerful than their likelihood ratio test equivalents. However, the correct derivation of
these tests usually requires extensive tedious algebra that must be recalculated for each
type of model. Furthermore, the tests cannot be used (at least without complex and
unsatisfactory adjustments) when the experiment is unbalanced.

Now let's demonstrate these methods on the pulp data. The fixed effect analysis shows
that the operator effects are statistically significant with a p-value of 0.023. A random
effects analysis using the expected mean squares approach yields exactly the same $F -$
statistic for the one-way ANOVA.

We can also employ the likelihood ratio approach. Because we are testing the random
effects, we can use either ML or REML. For fixed effects, we must use ML. In this
example, the only fixed effect is the mean and there is no interest in testing that. We first
fit the null model:

$$> \mathrm { n u l l m o d } < - 1 \mathrm { m } \left( \mathrm { b r i g h t } \sim 1 , \mathrm { p u l p } \right)$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 176" -->

As there are no random effects in this model, we must use 1m. For models of the same
class, we could use anova to compute the LRT and its p-value. Here, we need to compute
this directly:

\> as.numeric (2* (logLik (smod) -logLik (nullmod) ) )
[1] 2.5684

\> pchisq (2.5684, 1, lower=FALSE)
[1] 0.10902

The p-value is now well above the 5% significance level. We have used the MLE here-
using REML produces a slightly different result, but still above 5%. We cannot say that
this result is necessarily wrong, but the use of the $x ^ { 2 }$ approximation does cause us to
doubt the result.

We can use the parametric bootstrap approach to obtain a more accurate p-value. We
need to estimate the probability, given that the null hypothesis is true, of observing an
LRT of 2.5684 or greater. Under the null hypothesis, $y \sim N \left( \mu , \sigma ^ { 2 } \right) .$ A simulation approach
would generate data under this model, fit the null and alternative models and then
compute the LRT. The process would be repeated a large number of times and the
proportion of LRTs exceeding the observed value of 2.5684 would be used to estimate
the p-value. In practice, we do not know the true values of $\mu$ and a, but we can use the
estimated values; this distinguishes the parametric bootstrap from the simulation
approach. We can simulate responses under the null: under the null:

$$> y < - \quad s i m u l a t e \left( n u l l m o d \right)$$

Now taking the data we generate, we fit both the null and alternative models and then
compute the LRT. We repeat the process 1000 times:

\> lrstat <- numeric(1000)
> for (i in 1:1000) {
y <- unlist (simulate (nullmod) )
bnull <- 1m (y ~ 1)
balt <- lmer (y 1 + (1 | operator) , pulp, method="ML")
lrstat [i] <- as. numeric (2* (logLik (bait) -
logLik (bnull) ) )
}

We may examine the distribution of the bootstrapped LRTs. We compute the proportion
that are close to zero:

\> mean (lrstat < 0.00001)
[1] 0.7

The LRT clearly does not have a $x ^ { 2 }$ distribution. There is some discussion of this matter
in Stram and Lee (1994), who propose a 50:50 mixture of a $x ^ { 2 }$ and a mass at zero.
Unfortunately, as we can see, the relative proportions of these two components vary from
case to case. Crainiceanu and Ruppert (2004) give a more complete solution to the one-

<!-- PageBreak -->

<!-- PageNumber="177" -->
<!-- PageHeader="Random effects" -->

way ANOVA problem, but there is no general and exact result for this and more complex
problems. The parametric bootstrap may be the simplest approach. The method we have
used above is transparent and could be computed much more efficiently if speed is an
issue.

Our estimate p-value is:

\> mean (lrstat > 2.5684)
[1] 0.02

We should compute the standard error for this estimate by:

\> sqrt (0.02*0.98/1000)
[1] 0.0044272

So we can be fairly sure it is under 5%. If in doubt, do some more replications to make
sure; this only costs computer time. As it happens, this p-value is close to the fixed
effects p-value.

In this example, the random and fixed effect tests gave similar outcomes. However,
the hypotheses in random and fixed effects are intrinsically different. To generalize
somewhat, it is easier to conclude there is an effect in a fixed effects model since the
conclusion applies only to the levels of the factor used in the experiment, while for
random effects, the conclusion extends to levels of the factor not considered. Since the
range of the random effect conclusions is greater, the evidence necessarily has to be
stronger.


### 8.3 Predicting Random Effects

In a fixed effects model, the effects are represented by parameters and it makes sense to
estimate them. For example, in the one-way ANOVA model:

$y _ { i j } = \mu + \alpha _ { i } + \varepsilon _ { i j }$

We can calculate i-We do need to resolve the identifiability problem with the as and the
$\mu ,$ but once we decide on this, the meaning of the @sis clear enough. We can then
proceed to make further inference such as multiple comparisons of these levels.

In a model with random effects, the as are no longer parameters, but random variables.
Using the standard normal assumption:

$$\alpha _ { i } \sim N \left( 0 , \sigma _ { \alpha } ^ { 2 } \right)$$

It does not makes sense to estimate the a's because they are random variables. So instead,
we might think about the expected values. However:

$$E \alpha _ { i } = 0 \quad \forall i$$

which is clearly not very interesting. If one looks at this from a Bayesian point of view,
as described in, for example, Gelman, Carlin, Stern, and Rubin (2003), we have a prior

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 178

density on the as and $E \alpha _ { i } = 0$ is just the prior mean. Let $f$ represent density, then the
posterior density for $\alpha$ is given by:

$$f \left( \alpha _ { i } | y \right) = f \left( y | \alpha _ { i } \right) f \left( \alpha _ { i } \right)$$

We can then find the posterior mean, denoted by $\widehat { \mathrm { d } } _ { \mathrm { a s } } :$

$E \left( \alpha _ { i } | y \right) = \int a _ { i } f \left( \alpha _ { i } | y \right) d \alpha _ { i }$

For the general case, this works out to be:

$$a = D Z ^ { T } V ^ { - 1 } \left( y - X \beta \right)$$

Now a purely Bayesian approach would specify the parameters of the prior and we could
simply compute this. We take an empirical Bayes point of view and substitute the MLEs
into $D ,$ $V$ and $\beta$ to obtain the predicted random effects. These may be computed as:

\> ranef (mmod) $operator
(Intercept)


<table>
<tr>
<td>a</td>
<td>-0.12194</td>
</tr>
<tr>
<td>b</td>
<td>-0.25912</td>
</tr>
<tr>
<td>c</td>
<td>0.16767</td>
</tr>
<tr>
<td>d</td>
<td>0.21340</td>
</tr>
</table>


The predicted random effects are related to the fixed effects. We can show these for all
operators as:

\> (cc <- model.tables(lmod))
Tables of effects
operator
operator
a b c d
-0.16 -0.34 0.22 0.28

and then compute the ratio to the random effects as:

\> cc [ [1] ] $operator/ranef (mmod) $operator
X. Intercept.


<table>
<tr>
<td>a</td>
<td>1.3121</td>
</tr>
<tr>
<td>b</td>
<td>1.3121</td>
</tr>
<tr>
<td>c</td>
<td>1.3121</td>
</tr>
<tr>
<td>d</td>
<td>1.3121</td>
</tr>
</table>


We see that the predicted random effects are exactly in proportion to the fixed effects.
Typically, the predicted random effects are smaller and could be viewed as a type of
shrinkage estimate.

Suppose we wish to predict a new value. If the prediction is to be made for a new
operator or unknown operator, the best we can do is give $\widehat { \mu } = 6 0 . 4 _ { \mathrm { I f } }$ we know the

<!-- PageBreak -->

<!-- PageHeader="Random effects" -->
<!-- PageNumber="179" -->

operator, then we can combine this with our fixed effects to produce what are known as
the best linear unbiased predictors (BLUPs) as follows:

\> fixef (mmod) +ranef (mmod) $operator
X. Intercept.


<table>
<tr>
<td>a</td>
<td>60.278</td>
</tr>
<tr>
<td>b</td>
<td>60.141</td>
</tr>
<tr>
<td>c</td>
<td>60.568</td>
</tr>
<tr>
<td>d</td>
<td>60.613</td>
</tr>
</table>


This means that we have more than one type of residual depending on what fitted values
we use. The default predicted values and residuals are from the outermost level of
grouping. The usual diagnostic plots are still worthwhile:

\> qqnorm (resid (mmod) , main="")
>
plot (fitted (mmod) , resid (mmod) , xlab="Fitted", ylab="Resid
uals")
\> abline (0,0)

The plots are shown in Figure 8.1 and indicate no particular problems. Random effects
models are particular sensitive to outliers, depending as they do on variance components,
which can be substantially inflated by unusual points. The QQ plot is one way to pick out
outliers. We also need the normality for the testing. The residual-fitted plot is also
important because we made the assumption that the error variance was constant.

If we had more than four groups, we could also look at the normality of the group
level effects and check for constant variance also. With so few groups, it is not possible
to do this. Also note that there is no point thinking about multiple comparisons. These are
for comparing selected levels of a factor. For a random effect, the levels were randomly
selected, so such comparisons have little value.


<figure>
<figcaption>Figure 8.1 Diagnostic plots for the one-way random effects model.</figcaption>

0.4

0.4

Sample Quantiles

0.2

Residuals

0.2

0.0

$d ^ { 0 }$

0.0

0

-0.4

-0.4

2

-1

0

1

2

60.2

60.4

60.6

Theoretical Quantiles

Fitted

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 180" -->


### 8.4 Blocks as Random Effects

Blocks are properties of the experimental units. The blocks are either clearly defined by
the conditions of the experiment or they are formed with the judgment of the
experimenter. Sometimes, blocks represent groups of runs completed in the same period
of time. Typically, we are not interested in the block effects specifically, but must
account for their effect. It is therefore natural to treat blocks as random effects.

We illustrate with an experiment to compare four processes, $A ,$ $B ,$ $C$ and $\mathrm { D } ,$ for the
production of penicillin. These are the treatments. The raw material, corn steep liquor, is
quite variable and can only be made in blends sufficient for four runs. Thus a randomized
complete block design is suggested by the nature of the experimental units. The data
comes from Box, Hunter, and Hunter (1978). We start with the fixed effects analysis:

\> $\mathrm { d a t a }$ (penicillin)
> summary (penicillin)

treat
blend
yield

A : 5
Blend1 : 4
Min. : 77

B : 5
Blend2: 4 1st Qu. : 81

C : 5
Blend3: 4 Median : 87

D: 5
Blend4 : 4 Mean
: 86

Blend5: 4 3rd Qu. : 89
Max.
: 97
\> op <- options (contrasts=c ("contr. sum", "contr . poly")
> lmod <- aov(yield ~ blend + treat, penicillin)
> summary(lmod)


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq F</th>
<th>value</th>
<th>Pr (&gt;F)</th>
</tr>
<tr>
<td>blend</td>
<td>4</td>
<td>264.0</td>
<td>66.0</td>
<td>3.50</td>
<td>0.041</td>
</tr>
<tr>
<td>treat</td>
<td>3</td>
<td>70.0</td>
<td>23.3</td>
<td>1.24</td>
<td>0.339</td>
</tr>
<tr>
<td>Residuals</td>
<td>12</td>
<td>226.0</td>
<td>18.8</td>
<td></td>
<td></td>
</tr>
</table>


\> coef(lmod)


<table>
<tr>
<th>(Intercept)</th>
<th>blend1</th>
<th>blend2</th>
<th>blend3</th>
<th>blend</th>
</tr>
<tr>
<td>4</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>86</td>
<td>6</td>
<td>-3</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>1 2</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>treat1</td>
<td>treat2</td>
<td>treat3</td>
<td></td>
<td></td>
</tr>
<tr>
<td>-2</td>
<td>-1</td>
<td>3</td>
<td></td>
<td></td>
</tr>
</table>


From this we see that there is no significant difference between the treatments, but there
is between the blends. Now let's fit the data with a mixed model, where we have fixed
treatment effects, but random blend effects. This seems natural since the blends we use
can be viewed as having been selected from some notional population of blends.

\> mmod <- lmer (yield ~ treat + (1 |blend), penicillin)
> summary (mmod)
Linear mixed-effects model fit by REML
Formula: yield ~ treat + (1 | blend)
Data: penicillin
AIC
BIG
logLik deviance REMLdeviance
118.60 124.58 -53.301
117.28
106.60

<!-- PageBreak -->

<!-- PageNumber="181" -->
<!-- PageHeader="Random effects" -->

Random effects:


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>blend</td>
<td>(Intercept)</td>
<td>11.8</td>
<td>3.43</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td>18.8</td>
<td>4.34</td>
</tr>
<tr>
<td># of obs:</td>
<td>20, groups:</td>
<td>blend, 5</td>
<td></td>
</tr>
</table>


Fixed effects:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>DF</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>86.00</td>
<td></td>
<td>1.82</td>
<td>16</td>
<td>47.34</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>treat1</td>
<td>-2.00</td>
<td></td>
<td>1.68</td>
<td>16</td>
<td>-1.19</td>
<td>0.251</td>
</tr>
<tr>
<td>treat2</td>
<td>-1.00</td>
<td></td>
<td>1.68</td>
<td>16</td>
<td>-0.59</td>
<td>0.560</td>
</tr>
<tr>
<td>treat3</td>
<td>3.00</td>
<td></td>
<td>1.68</td>
<td>16</td>
<td>1.78</td>
<td>0.093</td>
</tr>
<tr>
<td colspan="2">&gt; options (op)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


We notice a few connections. The residual variance is the same in both cases: 18.8. This
is because we have a balanced design and so REML is equivalent to the ANOVA
estimator. The treatment effects are also the same as is the overall mean. The BLUPs for
the random effects are:

\> ranef (mmod) $blend


<table>
<tr>
<th></th>
<th>(Intercept)</th>
</tr>
<tr>
<td>Blendl</td>
<td>4.28788</td>
</tr>
<tr>
<td>Blend2</td>
<td>-2.14394</td>
</tr>
<tr>
<td>Blend3</td>
<td>-0.71465</td>
</tr>
<tr>
<td>Blend4</td>
<td>1.42929</td>
</tr>
<tr>
<td>Blend5</td>
<td>-2.85859</td>
</tr>
</table>


which, as with the one-way ANOVA, are a shrunken version of the corresponding fixed
effects. The usual diagnostics show nothing amiss.

We can test the significance of the fixed effects in two ways. We can use the ANOVA
method, where we assume that the random effect parameters take their estimated values:

\> anova (mmod)
Analysis of Variance Table
Df Sum Sq Mean Sq Denom F value Pr (>F)
treat 3 70.0 23.3
16.0
1.24
0.33

The result is identical with the fixed effects analysis above.

We can also test for a treatment effect using the maximum-likelihood ratio method:

\> amod <- lmer (yield ~ treat + (1 |blend) , penicillin,
method="ML")
> nmod <- lmer (yield ~ 1 + (1 |blend), penicillin,
method="ML")
> anova (amod, nmod)
Data: penicillin
Models :
nmod: yield 1 + (1 | blend)
amod: yield ~ treat + (1 | blend)
Df
AIC
BIG logLik Chisq Chi Df Pr (>Chisq)
nmod 3 127.3 130.3 -60.7

<!-- PageBreak -->

<!-- PageNumber="182" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->

amod 6 129.3 135.3 -58.6 4.05
3
0.26

Notice that we needed to use the ML method because comparison of models with
different fixed effects is not valid when REML is used. This is because in the REML
method, the likelihood of linear combination not involving the fixed effects parameters is
maximized. When comparing models with different fixed effects, the linear combinations
will be different and the obtained maximum likelihoods will not be comparable. The
qualitative outcome of the test is the same as before, but the test itself is numerically
different.

We can improve the accuracy with the parametric bootstrap approach. We can
generate a response from the null model and use this to compute the LRT. We repeat this
1000 times, saving the LRT each time:

\> lrstat <- numeric(1000)
> for (i in 1:1000) {
ryield <- unlist (simulate (nmod) )
nmodr <- lmer (ryield 1 + (1 |blend) , penicillin,
method="ML")
amodr <- lmer (ryield ~ treat + (1 |blend), penicillin,
method="ML")
lrstat [i] <- 2* (logLik (amodr) -logLik (nmodr) )
}

Under the standard likelihood theory, the LRT here should have a $x _ { 3 } ^ { 2 }$ distribution. We can
do a QQ plot to check this:

\>
plot (qchisq ( (1:1000) /1001, 3) , sort (lrstat) , xlab=expressi
on (chi [3]^2)
ylab="Simulated LRT")
\> abline(0,l)

As can be seen in the first panel of Figure 8.2, the approximation is not particularly good.
We can compute our estimated p-value as:

\> mean (Irstat > 4.05)
[1] 0.336

which is much closer to the F-test result than the $x _ { 3 } ^ { 2 } - b a s e d$ approximation.

We can also test the significance of the blends. As with a fixed effects analysis, we are
typically not directly interested in size of the blocking effects. Once having

<!-- PageBreak -->

<!-- PageNumber="183" -->
<!-- PageHeader="Random effects" -->


<figure>
<figcaption>Figure 8.2 Bootstrapped LRTapproximations to the $x ^ { 2 }$ distribution. $Q Q$ plots of the test statistics for the fixed effects are shown on the left and for the random effects on the right.</figcaption>

20

15

Simulated LRT

15

Simulated LRT

10

0

10

5

5

0

0

$\dot { \mathfrak{o} }$

5

$x _ { 3 } ^ { 2 }$

10

15

0

2

4

6

E

$x _ { 1 } ^ { 2 }$

</figure>


decided to design the experiment with blocks, we must retain them in the model.
However, we may wish to examine the blocking effects for information useful for the
design of future experiments. We can fit the model with and without random effects and
compute the LRT:

\> rmod <- Imer (yield ~ treat + (1 |blend) , penicillin)
> nlmod <- lm(yield ~ treat, penicillin)
> 2x (logLik (rmod) -logLik (nlmod, REML=TRUE) )
[1] 2.7629

We need to specify the nondefault REML option for null model to ensure that the LRT is
computed correctly. Now we perform the parametric bootstrap much as before:

\> lrstatf <- numeric(1000)

\> for (i in 1:1000) {
ryield <- unlist (simulate (nlmod) )
nlmodr <- lm(ryield ~ treat, penicillin)
rmodr <- lmer (ryield ~ treat + (1 |blend), penicillin)
lrstatf [i] <- 2* (logLik (rmodr) -logLik (nlmodr,
REML=TRUE) )
}

Again, the distribution is far from $Z _ { 1 } ^ { 2 }$ is clear when we examine the proportion of
generated LRTs which are close to zero:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 184

\> mean (lrstatf < 0.00001)
[1] 0.551

Notice that this proportion is different from that observed for the one-way ANOVA
illustrating the difficulty in finding a good approximation for the null distribution in such
cases. We can also check the distribution of the nonzero LRTs:

\> cs <- Irstatf[lrstatf > 0.00001]
> ncs <- length (cs)
>
plot (qchisq ( (1 :ncs) / (ncs+1) , 1) , sort (cs) , xlab=expression
(chi [1]^2) ,
ylab="Simulated LRT")
\> abline (0,l)

We see in the right panel of Figure 8.2 that the distribution is close to $\mathbb{X} _ { 1 } ^ { 2 }$ for the
tail. We can compute the estimated p-value as:

$$> m e a n \left( l r s t a t f > 2 . 7 6 2 9 \right)$$

[1] 0.043

So we find a significant blend effect. The p-value is close to that observed for the fixed
effects analysis. Given that the p-value is close to 5%, we might wish to increase the
number of bootstrap samples to increase our confidence in the result.

In this example, we saw no major advantage in modeling the blocks as random effects,
so we might prefer to use the fixed effects analysis as it is simpler to execute. However,
in subsequent analyses, we shall see that the use of random effects will be mandatory as
equivalent results may not obtained from a purely fixed effects analysis.


## 8.5 Split Plots

Split plot designs originated in agriculture, but occur frequently in other settings. As the
name implies, main plots are split into several subplots. The main plot is treated with a
level of one factor while the levels of some other factor are allowed to vary with the
subplots. The design arises as a result of restrictions on a full randomization. For
example, a field may be divided into four subplots. It may be possible to plant different
varieties in the subplots, but only one type of irrigation may be used for the whole field.
Note the distinction between split plots and blocks. Blocks are features of the
experimental units which we have the option to take advantage of in the experimental
design. Split plots impose restrictions on what assignments of factors are possible. They
impose requirements on the design that prevent a complete randomization. Split plots
often arise in nonagricultural settings when one factor is easy to change while another
factor takes much more time to change. If the experimenter must do all runs for each
level of the hard-to-change factor consecutively, a split-plot design results with the hard-
to-change factor representing the whole plot factor.

<!-- PageBreak -->

<!-- PageNumber="185" -->
<!-- PageHeader="Random effects" -->

Consider the following example. In an agricultural field trial, the objective was to
determine the effects of two crop varieties and four different irrigation methods. Eight
fields were available, but only one type of irrigation may be applied to each field. The
fields may be divided into two parts with a different variety planted in each half. The
whole plot factor is the method of irrigation, which should be randomly assigned to the
fields. Within each field, the variety is randomly assigned. Here is a summary of the data:

\> data (irrigation)
> summary (irrigation)


<table>
<tr>
<th></th>
<th>field</th>
<th>irrigation</th>
<th>variety $\mathrm { y i e l d }$</th>
</tr>
<tr>
<td>£1:2</td>
<td>11 : 4</td>
<td>v1 : 8</td>
<td>Min. :34.8</td>
</tr>
<tr>
<td>$2 : 2$</td>
<td>12:4</td>
<td>$v 2 : 8$</td>
<td>1st Qu. : 37.6</td>
</tr>
<tr>
<td>$3 : 2$</td>
<td>13:4</td>
<td>Median :</td>
<td>40.1</td>
</tr>
<tr>
<td>£4:2</td>
<td>14:4</td>
<td>Mean :</td>
<td>40.2</td>
</tr>
<tr>
<td>$5 : 2$</td>
<td></td>
<td>3rd Qu. :</td>
<td>42.7</td>
</tr>
<tr>
<td>$6 : 2$</td>
<td></td>
<td>Max. :</td>
<td>47.6</td>
</tr>
<tr>
<td colspan="4">$\left( O t h e r \right) : 4$</td>
</tr>
</table>


The irrigation and variety are fixed effects, but the field is clearly a random effect. We
must also consider the interaction between field and variety, which is necessarily also a
random effect because one of the two components is random. The fullest model that we
might consider is:

$$y _ { i j k } = \mu + i _ { i } + v _ { j } + \left( i v \right) _ { i j } + f _ { k } + \left( v f \right) _ { j k } + e _ { i j k }$$

$\mu ,$ $\dot { l } _ { i } ,$ $v _ { j } , \left( i v \right) _ { i j }$ are fixed effects, the rest are random having variances
$\sigma _ { f } ^ { 2 } ,$ $\sigma _ { v f } ^ { 2 }$
vfand $\sigma _ { E } ^ { 2 } \cdot \text { Note }$
that we have no $\left( i f \right) _ { i k }$ term in this model. It would not be possible to estimate such an
effect since only one type of irrigation is used on a given field; the factors are not
crossed.

We may fit this model as follows:

\> lmod <- lmer (yield ~ irrigation * variety +
(1 | field) + (1 | field: variety) ,
data=irrigation)
> logLik(lmod)
'log Lik. ' -22.697 $\left( d f = 1 1 \right)$

A simpler model omits the variety by field interaction random effect:

$$y _ { i j k } = \mu + i _ { i } + v _ { j } + \left( i v \right) _ { i j } + f _ { k } + x _ { i j k }$$

\> Imodr <- Imer (yield ~ irrigation * variety +
(1 | field) , data=irrigation)
> logLik(lmodr)
'log Lik. ' -22.697 (df=10)

We see that although the model is simpler, the likelihood is the same. The reason for this
is that it is not possible to distinguish the variety within field variation from the error

<!-- PageBreak -->

<!-- PageNumber="186" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->

variation. We would need more than one observation per variety within each field for us
to separate these two variabilities. Now examine the output of the last model:

\> summary(lmodr)

Linear mixed-effects model fit by REML
Formula: yield ~ irrigation * variety + (1 | field)
Data: irrigation
AIC
BIG
logLik deviance REMLdeviance

65.395 73.121 -22.697

68.609
45.395

Random effects:


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>field</td>
<td>(Intercept)</td>
<td>16.20</td>
<td>4.02</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td>2.11</td>
<td>1.45</td>
</tr>
</table>


\# of obs: 16, groups: field, 8
Fixed effects:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>DF</th>
<th>t</th>
</tr>
<tr>
<td>value $\mathrm { P r } \left( > | t | \right)$</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>(Intercept)</td>
<td>38.50</td>
<td></td>
<td colspan="2">3.03 8</td>
<td>12.73</td>
</tr>
<tr>
<td>0.0000014</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>irrigationi2</td>
<td>1.20</td>
<td>4.28</td>
<td colspan="2">8 0.28</td>
<td>0.79</td>
</tr>
<tr>
<td>irrigationi3</td>
<td>0.70</td>
<td>4.28</td>
<td colspan="2">8 0.16</td>
<td>0.87</td>
</tr>
<tr>
<td>$\mathrm { i r r i g a t i o n i 4 }$</td>
<td>3.50</td>
<td>4.28</td>
<td colspan="2">8 0.82</td>
<td>0.44</td>
</tr>
<tr>
<td>varietyv2</td>
<td>0.60</td>
<td>1.45</td>
<td colspan="2">8 0.41</td>
<td>0.69</td>
</tr>
<tr>
<td>irrigationi2: varietyv2</td>
<td>-0.40</td>
<td>2.05</td>
<td colspan="2">8 -0.19</td>
<td>0.85</td>
</tr>
<tr>
<td>irrigationiS: varietyv2</td>
<td>-0.20</td>
<td>2.05</td>
<td colspan="2">8 -0.10</td>
<td>0.92</td>
</tr>
<tr>
<td>irrigationi4: varietyv2</td>
<td>1.20</td>
<td>2.05</td>
<td colspan="2">8 0.58</td>
<td>0.57</td>
</tr>
</table>


We can see that the largest variance component is that due to the field effect: $\widehat { \sigma } _ { f } = 4 . 0 2$
with $\dot { \sigma } _ { \mathrm { e } } = 1 . 4 5 . \mathrm { w } _ { \mathrm { e } }$ can check the fixed effects for significance:

\> anova(lmodr)
Analysis of Variance Table


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq</th>
<th>Denom</th>
<th>F value</th>
<th></th>
</tr>
<tr>
<td>Pr (&gt;F)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>irrigation</td>
<td>3</td>
<td rowspan="2">2.45</td>
<td rowspan="2">0.82</td>
<td>8.00</td>
<td rowspan="2">0.39</td>
<td rowspan="2">0.</td>
</tr>
<tr>
<td>76</td>
<td></td>
<td></td>
</tr>
<tr>
<td>variety</td>
<td>1</td>
<td>2.25</td>
<td>2.25</td>
<td>8.00</td>
<td>1.07</td>
<td>0.</td>
</tr>
</table>


33

irrigation: variety
3
1.55
0.52
8.00
0.25
0.86

So we see there is no evidence for a fixed effect for either irrigation or variety or their
interaction. We should check the diagnostic plots to make sure there is nothing amiss:

\>
plot (fitted (lmodr) , resid (lmodr) , xlab="Fitted", ylab="Res
iduals")
\> qqnorm (resid (lmodr) , main="")

<!-- PageBreak -->

<!-- PageNumber="187" -->
<!-- PageHeader="Random effects" -->


<figure>
<figcaption>Figure 8.3 Diagnostic plots for the split plot example.</figcaption>

1.0

1.0

Residuals

0.5

Sample Quantiles

0.5

0.0

0.0

0.5

-0.5

$0 ^ { 0 }$

-1.0

-1.0

0 000

36 38 40 42 44 46

-2

-1

0

1

2

Fitted

Theoretical Quantiles

</figure>


We can see in Figure 8.3 that there is no problem with the nonconstant variance, but that
the residuals indicate a short-tailed distribution. This type of divergence from normality
is unlikely to cause any major problems with the estimation and inference.

Sometimes analysts ignore the split-plot variable as in:

\> mod <- lm(yield ~ irrigation * variety,
data=irrigation)
> anova (mod)
Analysis of Variance Table

Response: yield


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum</th>
<th>Sq</th>
<th>Mean Sq</th>
<th>F value</th>
<th></th>
</tr>
<tr>
<td>irrigation</td>
<td>3</td>
<td></td>
<td>40.2</td>
<td>13.4</td>
<td>0.73</td>
<td>0.56</td>
</tr>
<tr>
<td>variety</td>
<td>1</td>
<td colspan="2">2.2</td>
<td>2.2</td>
<td>0.12</td>
<td>0.73</td>
</tr>
<tr>
<td>irrigation: variety</td>
<td>3</td>
<td colspan="2">1.6</td>
<td colspan="2">0.5 0.03</td>
<td>0.99</td>
</tr>
<tr>
<td>Residuals</td>
<td>8</td>
<td>146.5</td>
<td></td>
<td>18.3</td>
<td></td>
<td></td>
</tr>
</table>


The results will not be the same. This last model is incorrect because it fails to take into
account the restrictions on the randomization introduced by the fields and the additional
variability thereby induced.


## 8.6 Nested Effects

When the levels of one factor vary only within the levels of another factor, that factor is
said to be nested. For example, when measuring the performance of workers at several
different job locations, if the workers only work at one location, the workers are nested
within the locations. If the workers work at more than one location, then the workers are
crossed with locations.

Here is an example to illustrate nesting. Consistency between laboratory tests is
important and yet the results may depend on who did the test and where the test was

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 188" -->

performed. In an experiment to test levels of consistency, a large jar of dried egg powder
was divided up into a number of samples. Because the powder was homogenized, the fat
content of the samples is the same, but this fact is withheld from the laboratories. Four
samples were sent to each of six laboratories. Two of the samples were labeled as $G$ and
two as $H ,$ although in fact they were identical. The laboratories were instructed to give
two samples to two different technicians. The technicians were then instructed to divide
their samples into two parts and measure the fat content of each. So each laboratory
reported eight measures, each technician four measures, that is, two replicated measures
on each of two samples. The data comes from Bliss (1967):

\> data (eggs)
> summary (eggs)


<table>
<tr>
<th>Fat</th>
<th>Lab</th>
<th>Technician</th>
<th>Sample</th>
</tr>
<tr>
<td>Min. :0.060</td>
<td>I : 8</td>
<td>$o n e : 2 4$</td>
<td>G:24</td>
</tr>
<tr>
<td>1st Qu :0.307</td>
<td>II : 8</td>
<td>two : 24</td>
<td>H: 24</td>
</tr>
<tr>
<td>Median :0.370</td>
<td>III : 8</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mean : 0.388</td>
<td>IV : 8</td>
<td></td>
<td></td>
</tr>
<tr>
<td>3rd Qu. :0.430</td>
<td>V : 8</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Max. :0.800</td>
<td>VI : 8</td>
<td></td>
<td></td>
</tr>
</table>


Although the technicians have been labeled "one" and "two," they are two different
people in each lab. Thus the technician factor is nested within laboratories. Furthermore,
even though the samples are labeled"H" and "G," these are not the same samples across
the technicians and the laboratories. Hence we have samples nested within technicians.
Technicians and samples should be treated as random effects since we may consider
these as randomly sampled. If the labs were specifically selected, then they should be
taken a fixed effects. If, however, they were randomly selected from those available, then
they should be treated as random effects. If the purpose of the study is come to some
conclusion about consistency across laboratories, the latter approach is advisable.

For the purposes of this analysis, we will treat labs as random. So all our effects
(except the grand mean) are random. The model is:

$y _ { i j k l } = \mu + L _ { i } + T _ { i j } + S _ { i j k } + 8 _ { i j k l }$

This can be fit using:

\> cmod <- Imer (Fat 1 + (1 | Lab) + (1 | Lab : Technician) +
(1 | Lab : Technician : Sample) , data=eggs)
> summary (cmod)
Linear mixed-effects model fit by REML
Formula: Fat ~ 1 + (1 | Lab) + (1 | Lab: Technician) +
(1
| Lab : Technician : Sample)
Data: eggs

AIC
BIG logLik deviance REMLdeviance
-54.235 -44.879 32.118 -68.703
-64.235

Random effects:


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>Lab : Technician : Sample</td>
<td>(Intercept)</td>
<td>0.00306</td>
<td>0.0554</td>
</tr>
<tr>
<td>Lab : Technician</td>
<td>(Intercept)</td>
<td>0.00698</td>
<td>0.0835</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="189" -->
<!-- PageHeader="Random effects" -->

Lab (Intercept)
0.00592
0.0769

Residual
0.00720
0.0848

\# of obs: 48, groups: Lab: Technician : Sample, 24;
Lab: Technician, 12; Lab, 6
Fixed effects:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>DF</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>0.388</td>
<td></td>
<td>0.043</td>
<td>47</td>
<td>9.02</td>
<td>$8 e - 1 2$</td>
</tr>
</table>


So we have $\widetilde { \sigma } _ { L } = 0 . 0 7 7 ,$ $\ddot { \mathrm { o } } _ { T } = 0 . 0 8 4 ,$ $\widehat { \sigma } _ { S } = 0 . 0 5 5 _ { a n d }$ $\widehat { \sigma } _ { \mathrm { e } } = 0 . 0 8 5$ all four variance
components are of a similar magnitude. The lack of consistency in measures of fat
content can be ascribed to variance between labs, variance between technicians, variance
in measurement due to different labeling and just plain measurement error. We can see if
the model can be simplified by removing the lowest level of the variance components:

\> cmodr <- Imer (Fat ~ 1 + (1 | Lab) + (1 | Lab : Technician) ,
data=eggs)
> anova (cmod, cmodr)
Data: eggs
Models:
cmodr: Fat ~ 1 + (1 | Lab) + (1 | Lab: Technician)
cmod: Fat ~ 1 + (1 | Lab) + (1 | Lab: Technician) +
(1 | Lab : Technician : Sample)


<table>
<tr>
<th></th>
<th>Df AIC</th>
<th>BIG</th>
<th>logLik</th>
<th>Chisq Chi</th>
<th>Df</th>
<th>Pr (&gt;Chisq)</th>
</tr>
<tr>
<td colspan="2">cmodr 4 -59.1</td>
<td>-51.6</td>
<td>33.5</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">cmod 5 -58.7</td>
<td>-49.3</td>
<td>34.4</td>
<td>1.6</td>
<td>1</td>
<td>0.21</td>
</tr>
</table>


We see that we cannot reject $H _ { 0 } : \sigma _ { 5 } ^ { 2 } = 0$ =".However, we know that this p-value is con-
servative and the true value will be somewhat lower. An examination of the reduced
model is interesting:

\> VarCorr (cmodr)


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>Lab: Technician</td>
<td>(Intercept)</td>
<td>0.00800</td>
<td>0.0895</td>
</tr>
<tr>
<td>Lab</td>
<td>(Intercept)</td>
<td>0.00592</td>
<td>0.0769</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td>0.00924</td>
<td>0.0961</td>
</tr>
</table>


The variation due to samples has been absorbed into the other components.

As before, it is worth checking the accuracy of these p-values. We generate data under
the null model and compute the LRT 1000 times:

\> lrstat <- numeric(1000)

\> for (i in 1:1000) {
rFat <- unlist (simulate (cmodr) )
nmod <- lmer (rFat ~ 1 + (1 | Lab) + (11
Lab: Technician) , data=eggs)
amod <- lmer (rFat ~ 1 + (1 | Lab) + (11 Lab: Technician)
+
(1 | Lab : Technician : Sample) , data=eggs)
lrstat[i] <- 2* (logLik (amod) -logLik (nmod) )

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 190" -->

}

As before, we can see that the LRT does not have a null $x ^ { 2 }$ distribution because, in this
case, 55% of the generated LRTs are close to zero:

\> mean (lrstat < 0.00001)
[1] 0.55

We can estimate the p-value as:

\> 2* (logLik (cmod) -logLik (cmodr) )
[1] 1.6034
> mean (Irstat > 1.6034)
[1] 0.092

So we can reasonably say that the variation due to samples can be ignored. We may now
test the significance of the variation between technicians. Using the same method above,
this is found to be significant.


## 8.7 Crossed Effects

Effects are said to be crossed when they are not nested. In full factorial designs, effects
are completely crossed because every level of one factor occurs with every level of
another factor. However, in some other designs, crossing is less-than-complete. Even if
just two levels of two factors occur in all four combinations, the factors are crossed. An
example of less than complete crossing is a latin square design, where there is one
treatment factor and two blocking factors. Although not all combinations of factors occur,
the blocking factors are not nested. When at least some crossing occurs, methods for
nested designs cannot be used. We consider a latin square example.

In an experiment reported by Davies (1954), four materials, $\mathrm { A } ,$ B, $C$ and $\mathrm { D } ,$ were fed
into a wear-testing machine. The response is the loss of weight in 0.1 mm over the testing
period. The machine could process four samples at a time and past experience indicated
that there were some differences due to the position of these four samples. Also some
differences were suspected from run to run. $A$ fixed effects analysis of this dataset may
be found in Faraway (2004). Four runs were made. The latin square structure of the
design may be observed:

\> data (abrasion)
> matrix (abrasion$material, 4, 4)


<table>
<tr>
<td>[1,] [, 1]</td>
<td>"A" </td>
<td>"D" </td>
<td>"B" </td>
</tr>
<tr>
<td>[2,] "D"</td>
<td>"B"</td>
<td></td>
<td>"A"</td>
</tr>
<tr>
<td>[3,] "B"</td>
<td>"D"</td>
<td>"A"</td>
<td>"C"</td>
</tr>
<tr>
<td>[4,] "A"</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


A fixed effects analysis of the data reveals:

<!-- PageBreak -->

<!-- PageNumber="191" -->
<!-- PageHeader="Random effects" -->

\> lmod <- aov(wear ~ material + run + position,
abrasion)

\> summary(lmod)


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq</th>
<th>F value</th>
<th></th>
</tr>
<tr>
<td>material</td>
<td>3</td>
<td>4622</td>
<td>1540</td>
<td>25.15</td>
<td>0.00085</td>
</tr>
<tr>
<td>run</td>
<td>3</td>
<td>986</td>
<td>329</td>
<td>5.37</td>
<td>0.03901</td>
</tr>
<tr>
<td>position</td>
<td>3</td>
<td>1468</td>
<td>489</td>
<td>7.99</td>
<td>0.01617</td>
</tr>
<tr>
<td>Residuals</td>
<td>6</td>
<td>367</td>
<td>61</td>
<td></td>
<td></td>
</tr>
</table>


All the effects are significant. However, we might regard the run and position as random
effects. The appropriate model is then:

\> mmod <- lmer(wear ~ material + (1|run) +
(1 | position) , abrasion)
> anova (mmod)
Analysis of Variance Table
Df Sum Sq Mean Sq Denom F value
Pr (>F)
material
3
4621
1540
12
25.1 0.000018
> summary (mmod)

Linear mixed-effects model fit by REML
Formula: wear ~ material + (1 | run) + (1 | position)
Data: abrasion

AIC
BIG
logLik MLdeviance REMLdeviance

114.26 119.66 -50.128
120.43
100.26

Random effects:


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>run</td>
<td>(Intercept)</td>
<td>66.9</td>
<td>8.18</td>
</tr>
<tr>
<td>position</td>
<td>(Intercept)</td>
<td>107.1</td>
<td>10.35</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td>61.2</td>
<td>7.83</td>
</tr>
<tr>
<td># of obs:</td>
<td>16, groups:</td>
<td colspan="2">run, 4; position, 4</td>
</tr>
</table>


Fixed effects:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>DF</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>265.75</td>
<td></td>
<td>7.67</td>
<td>12</td>
<td>34.66</td>
<td>2.1e-13</td>
</tr>
<tr>
<td>materials</td>
<td>-45.75</td>
<td></td>
<td>5.53</td>
<td>12</td>
<td>-8.27</td>
<td></td>
</tr>
<tr>
<td>materialC</td>
<td>-24.00</td>
<td></td>
<td>5.53</td>
<td>12</td>
<td>-4.34</td>
<td></td>
</tr>
<tr>
<td>materialD</td>
<td>-35.25</td>
<td></td>
<td>5.53</td>
<td>12</td>
<td>-6.37</td>
<td>$3 . 6 e - 0 5$</td>
</tr>
</table>


The lmer function is able to recognize that the run and position effects are crossed and
fits the model appropriately. The F-test for the fixed effects is almost the same as the
corresponding fixed effects analysis. The only difference is that the fixed effects analysis
uses a denominator degrees of freedom of six while the random effects analysis is made
conditional on the estimated random effects parameters which results in 12 degrees of
freedom. The difference is not crucial here.

The significance of the random effects could be tested using the parametric bootstrap
method. However, since the design of this experiment has already restricted the
randomization to allow for these effects, there is no motivation to make these tests since
we will not modify the analysis of this current experiment.

The fixed effects analysis was somewhat easier to execute, but the random effects
analysis has the advantage of producing estimates of the variation in the blocking factors

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 192" -->

which will be more useful in future studies. Fixed effects estimates of the run effect for
this experiment are only useful for the current study.


## 8.8 Multilevel Models

Multilevel models is a term used for models for data with hierarchical structure. The term
is most commonly used in the social sciences. We can use the methodology we have
already developed to fit some of these models.

We take as our example some data from the Junior School Project collected from
primary (U.S. term is elementary) schools in inner London. The data is described in detail
in Mortimore, Sammons, Stoll, Lewis, and Ecob (1988) and a subset is analyzed
extensively in Goldstein (1995).

The variables in the data are the school, the class within the school (up to four),
gender, social class of the father (I=1; $I I = 2 ;$ III nonmanual=3; III manual=4; $I V = 5 ;$ $V = 6 ;$
Long-term unemployed=7; Not currently employed=8; Father absent=9), raven's test in
year 1, student id number, english test score, mathematics test score and school year
(coded 0, 1, and 2 for years one, two and three). So there are up to three measures per
student. The data was obtained from the Multilevel Models project at
http://www.ioe.ac.uk/multilevel/.

We shall take as our response the math test score result from the final year and try to
model this as a function of gender, social class and the Raven's test score from the first
year which might be taken as a measure of ability when entering the school. We subset
the data to ignore the math scores from the first two years:

\> data (jsp)

$$> j s p r < - \quad j s p \left[ j s p y e a r = = 2 , \right]$$

We start with two plots of the data. Due to the discreteness of the score results, it is
helpful to jitter (add small random perturbations) the scores to avoid overprinting:

\> plot (jitter (math) ~jitter (raven) , data=jspr, xlab="Raven
score",
ylab="Math score")
> boxplot (math ~ social, data=jspr, xlab="Social
class", ylab="Math score")

In Figure 8.4, we can see the positive correlation between the Raven's test score and the
final math score. The maximum math score was 40 which reduces the variability at the
upper end of the scale. We also see how the math scores tend to decline with social class.

One possible approach to analyzing these data is multiple regression. For example, we
could fit:

<!-- PageBreak -->

<!-- PageHeader="Random effects" -->
<!-- PageNumber="193" -->


<figure>
<figcaption>Figure 8.4 Plots of the Junior School Project data.</figcaption>

10 15 20 25 30 35 40

$\bigoplus _ { i }$

7

₸

₸

"

₸

F

T

F

₸

.

35

30

\#

Math score

Math score

25

-....

L

20

0

000 1

15

0

000

10

000

1

o

0

8

\-

5

5

0

0

5

10 15 20 25 30 35

1 2 3 4 5 6 7 8

9

Raven score

Social class

</figure>


\> glin <- 1m (math ~ raven\*gender\*social, jspr)
> anova (glin)

Analysis of Variance Table

Response: math


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq</th>
<th>F value</th>
<th></th>
</tr>
<tr>
<td>raven</td>
<td>1</td>
<td>11481</td>
<td>11481</td>
<td>368.06</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>gender</td>
<td>1</td>
<td>44</td>
<td>44</td>
<td>1.41</td>
<td>0.2347</td>
</tr>
<tr>
<td>social</td>
<td>8</td>
<td>779</td>
<td>97</td>
<td>3.12</td>
<td>0.0017</td>
</tr>
<tr>
<td>raven : gender</td>
<td>1</td>
<td>0.01145</td>
<td>0.01145</td>
<td>0.00037</td>
<td>0.9847</td>
</tr>
<tr>
<td>raven : social</td>
<td>8</td>
<td>583</td>
<td>73</td>
<td>2.33</td>
<td>0.0175</td>
</tr>
<tr>
<td>gender : social</td>
<td>8</td>
<td>450</td>
<td>56</td>
<td>1.80</td>
<td>0.0727</td>
</tr>
<tr>
<td>raven : gender : social</td>
<td>8</td>
<td>235</td>
<td>29</td>
<td>0.94</td>
<td>0.4824</td>
</tr>
<tr>
<td>$\mathrm { R e s i d u a l s }$</td>
<td>917</td>
<td>28603</td>
<td>31</td>
<td></td>
<td></td>
</tr>
</table>


It would seem that gender effects can be removed entirely, giving us:

\> glin <- 1m (math ~ raven*social, jspr)

\> anova (glin)

Analysis of Variance Table

Response: math


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq</th>
<th>F value</th>
<th></th>
</tr>
<tr>
<td>raven</td>
<td>1</td>
<td>11481</td>
<td>11481</td>
<td>365.72</td>
<td></td>
</tr>
<tr>
<td>social</td>
<td>8</td>
<td>778</td>
<td>97</td>
<td>3.10</td>
<td>0.0019</td>
</tr>
<tr>
<td>raven : social</td>
<td>8</td>
<td>564</td>
<td>71</td>
<td>2.25</td>
<td>0.0222</td>
</tr>
<tr>
<td>Residuals</td>
<td>935</td>
<td>29351</td>
<td>31</td>
<td></td>
<td></td>
</tr>
</table>


This is a fairly large dataset, so even small effects can be significant. Even though the
raven: social term is significant at the 5% level, we remove it to simplify interpretation:

\> glin <- 1m (math ~ raven+social, jspr)

\>
summary (glin)

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 194

Coefficients :


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>t value</th>
<th>Pr $\left( > | t | \right)$</th>
</tr>
<tr>
<td colspan="2">(Intercept) 17.0248</td>
<td></td>
<td>1.3745</td>
<td>12.39</td>
<td>$< 2 e - 1 6$</td>
</tr>
<tr>
<td>raven</td>
<td>0.5804</td>
<td></td>
<td>0.0326</td>
<td>17.83</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>social2</td>
<td>0.0495</td>
<td></td>
<td>1.1294</td>
<td>0.04</td>
<td>0.965</td>
</tr>
<tr>
<td>social3</td>
<td>-0.4289</td>
<td></td>
<td>1.1957</td>
<td>-0.36</td>
<td>0.720</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 4$</td>
<td>-1.7745</td>
<td></td>
<td>1.0599</td>
<td>-1.67</td>
<td>0.094</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 5$</td>
<td>-0.7823</td>
<td></td>
<td>1.1892</td>
<td>-0.66</td>
<td>0.511</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 6$</td>
<td>-2.4937</td>
<td></td>
<td>1.2609</td>
<td>-1.98</td>
<td>0.048</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 7$</td>
<td>-3.0485</td>
<td></td>
<td>1.2907</td>
<td>-2.36</td>
<td>0.018</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 8$</td>
<td>-3.1175</td>
<td></td>
<td>1.7749</td>
<td>-1.76</td>
<td>0.079</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 9$</td>
<td>-0.6328</td>
<td></td>
<td>1.1273</td>
<td>-0.56</td>
<td>0.575</td>
</tr>
</table>

Residual standard error: 5.63 on 943 degrees of freedom
Multiple R-Squared: 0.291, Adjusted R-squared: 0.284
F-statistic: 42.9 on 9 and 943 DF, $p - v a l u e :$ $< 2 e - 1 6$


We see that the final math score is strongly related to the entering Raven score and that
the math scores of the lower social classes are lower, even after adjustment for the
entering score. Of course, any regression analysis requires more investigation than this;
there are diagnostics and transformations to be considered and more. However, even if
we were to do this, there would still be a problem with this analysis: We are assuming
that the 953 students in the dataset are independent observations. This is not a tenable
assumption as the students come from 50 different schools. The number coming from
each school varies:


<figure>

\> table $\left( j \sin p r s c h o o l \right)$
1 2 3 9 10 11 12 13 14 15 16 17 18 19
20 21
26
11
14
24
26
18
11
27
21
0
11
23
22
13
7
16
6 18

14 13 28

22 23 24 25 26 27 28 29 30 31 32 33 3

34
35
36

37
38
39

40
41
42
14 18 21 14 20 22 15 13 27 35 23 44 27 16 28 17 12 14
10 10 41
44 45 46 47 48 49 50
5 11 15 33 63 22 14

</figure>


It is highly likely that students in the same school (and perhaps) class will show some
dependence. So we have somewhat less than 953 independent cases worth of information.
Any analysis that pretends these are independent is likely to overstate the significance of
the results. Furthermore, the analysis above tells us nothing about the variation between
and within schools. People will certainly be interested in this. We could aggregate the
results across schools but this would lose information and expose us to the dangers of an
ecological regression.

We need an analysis that uses the individual-level information, but also reflects the
grouping in the data. Our first model has fixed effects representing all interactions
between raven, social and gender with random effects for the school and the class nested
within the school:

<!-- PageBreak -->

<!-- PageNumber="195" -->
<!-- PageHeader="Random effects" -->

\> mmod <- lmer (math ~
raven\*social\*gender+ (1 | school) + (1 | school : class) ,
data=jspr)
> anova (mmod)
Analysis of Variance Table


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq</th>
<th>Denom</th>
<th>F value</th>
</tr>
<tr>
<td>$\mathbb{P} \underline { r } \left( > \mathrm { F } \right)$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>raven</td>
<td>1</td>
<td>10218</td>
<td>10218</td>
<td>917</td>
<td>374.40</td>
</tr>
<tr>
<td>$< 2 e - 1 6$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>social</td>
<td>8</td>
<td>616</td>
<td>77</td>
<td>917</td>
<td>2.82</td>
</tr>
<tr>
<td>0.0043</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>gender</td>
<td>1</td>
<td>22</td>
<td>22</td>
<td>917</td>
<td>0.79</td>
</tr>
<tr>
<td>0.3738</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>raven : social</td>
<td>8</td>
<td>577</td>
<td rowspan="2">72</td>
<td rowspan="2">917</td>
<td>2.64</td>
</tr>
<tr>
<td>0.0072</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>raven : gender</td>
<td rowspan="2">1</td>
<td rowspan="2">2</td>
<td rowspan="2">2</td>
<td rowspan="2">917</td>
<td rowspan="2">0.09</td>
</tr>
<tr>
<td>0.7639</td>
</tr>
<tr>
<td>social : gender</td>
<td rowspan="2">8</td>
<td rowspan="2">275</td>
<td rowspan="2">34</td>
<td rowspan="2">917</td>
<td rowspan="2">1.26</td>
</tr>
<tr>
<td>0.2605</td>
</tr>
<tr>
<td>raven : social : gender 0.5524</td>
<td>8</td>
<td>187</td>
<td>23</td>
<td>917</td>
<td>0.86</td>
</tr>
</table>


Again, it seems that gender is not important and so we simplify to:

\> jspr$craven <- jspr$raven-mean (jspr$raven)
> mmod <- lmer (math ~ craven*social+ (1 | school) +
(1 | school : class) , jspr)
> summary (mmod)
Linear mixed-effects model fit by REML
Formula: math ~ craven * social + (1 | school) + (1 |
school : class)

Data: jspr

AIC
BIG
logLik deviance REMLdeviance

5963.2 6065.2
-2960.6
5907.4
5921.2

Random effects:


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>school: class</td>
<td>(Intercept)</td>
<td>1.18</td>
<td>1.08</td>
</tr>
<tr>
<td>school</td>
<td>(Intercept)</td>
<td>3.15</td>
<td>1.77</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td>27.14</td>
<td>5.21</td>
</tr>
<tr>
<td colspan="4"># of obs: 953, groups: school:class, 90; school, 48</td>
</tr>
</table>


Fixed effects:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>DF</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>31.9112</td>
<td>1.1955</td>
<td>935</td>
<td>26.69</td>
<td>$< 2 e - 1 6$</td>
</tr>
<tr>
<td>craven</td>
<td>0.6058</td>
<td>0.1885</td>
<td>935</td>
<td>3.21</td>
<td>0.0014</td>
</tr>
<tr>
<td>social2</td>
<td>0.0236</td>
<td>1.2722</td>
<td>935</td>
<td>0.02</td>
<td>0.9852</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 3$</td>
<td>-0.6307</td>
<td>1.3089</td>
<td>935</td>
<td>-0.48</td>
<td>0.6300</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 4$</td>
<td>-1.9670</td>
<td>1.1971</td>
<td>935</td>
<td>-1.64</td>
<td>0.1007</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 5$</td>
<td>-1.3585</td>
<td>1.3002</td>
<td>935</td>
<td>-1.04</td>
<td>0.2964</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 6$</td>
<td>-2.2687</td>
<td>1.3737</td>
<td>935</td>
<td>-1.65</td>
<td>0.0990</td>
</tr>
<tr>
<td>social7</td>
<td>-2.5518</td>
<td>1.4055</td>
<td>935</td>
<td>-1.82</td>
<td>0.0698</td>
</tr>
<tr>
<td>$\mathrm { s o c i a l } 8$</td>
<td>-3.3950</td>
<td>1.8014</td>
<td>935</td>
<td>-1.88</td>
<td>0.0598</td>
</tr>
<tr>
<td>$\sec i a l g$</td>
<td>-0.8313</td>
<td>1.2535</td>
<td>935</td>
<td>-0.66</td>
<td>0.5074</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="196" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->


<table>
<tr>
<td>craven : social2</td>
<td>-0.1321</td>
<td>0.2058</td>
<td>935</td>
<td>-0.64</td>
<td>0.5212</td>
</tr>
<tr>
<td>craven : social3</td>
<td>-0.2243</td>
<td>0.2189</td>
<td>935</td>
<td>-1.02</td>
<td>0.3057</td>
</tr>
<tr>
<td>craven : social4</td>
<td>0.0358</td>
<td>0.1949</td>
<td>935</td>
<td>0.18</td>
<td>0.8542</td>
</tr>
<tr>
<td>craven : social5</td>
<td>-0.1503</td>
<td>0.2089</td>
<td>935</td>
<td>-0.72</td>
<td>0.4719</td>
</tr>
<tr>
<td>craven : social6</td>
<td>-0.0386</td>
<td>0.2326</td>
<td>935</td>
<td>-0.17</td>
<td>0.8682</td>
</tr>
<tr>
<td>$\mathrm { c r a v e n } : \mathrm { s o c i a l } 7$</td>
<td>0.3983</td>
<td>0.2318</td>
<td>935</td>
<td>1.72</td>
<td>0.0861</td>
</tr>
<tr>
<td>craven : social8</td>
<td>0.2560</td>
<td>0.2615</td>
<td>935</td>
<td>0.98</td>
<td>0.3279</td>
</tr>
<tr>
<td>craven : social9</td>
<td>-0.0810</td>
<td>0.2055</td>
<td>935</td>
<td>-0.39</td>
<td>0.6935</td>
</tr>
</table>


We centered the Raven score about its overall mean. This means that we can interpret the
social effects as the predicted differences from social class one at the mean Raven score.
If we did not do this, these parameter estimates would represent differences for raven=0
which is not very useful. We can see the math score is strongly related to the entering
Raven score. We see that for the same entering score, the final math score tends to be
lower as social class goes down. Note that class 9 here is when the father is absent and
class 8 is not necessarily worse than 7, so this factor is not entirely ordinal. We also see
the most substantial variation at the individual level with smaller amounts of variation at
the school and class level.

We check the standard diagnostics first:

\>
qqnorm (resid (mmod) , main="")
\>

plot (fitted (mmod) , resid (mmod) , xlab="Fitted", ylab="Resid
uals")


<figure>
<figcaption>Figure 8.5 Diagnostic plots for the Junior Schools Project model.</figcaption>

-20 -15 -10 -5 0 5 10 1!

=

10

Sample Quantiles

5

Residuals

0

-20 -15 -10 -5

-3 -2 -1 0 1 2 3

15 20 25 30 35 40
Fitted

Theoretical Quantiles

</figure>


In Figure 8.5, we see that the residuals are close to normal, but there is a clear decrease in
the variance with an increase in the fitted values. This is due to the reduced variation in
higher scores already observed. We might consider a transformation of the response to
remove this effect.

<!-- PageBreak -->

<!-- PageNumber="197" -->
<!-- PageHeader="Random effects" -->

We can also check the assumption of normally distributed random effects. We can do
this at the school and class level:

\> qqnorm (ranef (mmod) $school [ [1] ], main="School effects")
> qqnorm (ranef (mmod) $"school : class" [ [1] ] , main="Class
effects")

We see approximate normality in both cases with some evidence of short tails for the
school effects. It is interesting to look at the sorted school effects:

$$> a d j s c o r e s < - \quad r a n e f \left( m m o d \right) s c h o o l \left[ \left[ 1 \right] \right]$$

These represent a ranking of the schools adjusted for the quality of the intake and the
social class of the students. The difference between the best and the worst is about 5
points on the math test. Of course, we must recognize that there is variability in these
estimated effects before making any decisions about the relative strengths of


<figure>
<figcaption>Figure 8.6 QQ plots of the random effects at the school and class levels.</figcaption>

School effects

Class effects

Sample Quantiles

Sample Quantiles

-1.5 -1.0 -0.5 0.0 0.5 1.0

0

-1

-2

-1

0

1

2

-2 -1 0 1 2

Theoretical Quantiles

Theoretical Quantiles

</figure>


these schools. Compare this with an unadjusted ranking that simply takes the average
score achieved by the school, centered by the overall average:

$$r a w s c o r e s < - \quad c o e f \left( 1 m \left( m a t h \sim s c h o o l - 1 , j s p r \right) \right)$$
\>

\> rawscores <- rawscores-mean (rawscores)

We compare these two measures of school quality in Figure 8.7:

\> plot (rawscores, adjscores)
> sint <- c (9,14,29)
>
text (rawscores [sint] , adjscores [sint]+0.2, c ("9", "15", "30
") )

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 198" -->

School 10 is listed but has no students hence the need to adjust the labeling. There are
some interesting differences. School 15 looks best on the raw scores but after adjustment,
it drops to 15th place. This is a school that apparently performs well, but when the quality
of the incoming students is considered, its performance is not so impressive. School 30
illustrates the other side of the coin. This school looks average on the raw scores, but is
doing quite well given the ability of the incoming students. School 9 is actually doing a
poor job despite raw scores that look quite good.

It is also worth plotting the residuals and the random effects against the predictors. We
would be interested in finding any inhomogeneity or signs of structure that might lead to
an improved model.

Compositional effects: Fixed effect predictors in this example so far have been at the
lowest level, the student, but it is not improbable that factors at the school or class level
might be important predictors of success in the math test. We can construct some such
predictors from the individual-level information; such factors are called compositional
effects. For example, the average entering score for a school might be an important
predictor. The ability of one's fellow students may have an impact on future
achievement. We construct this variable:

\> schraven <- lm(raven ~ school, jspr)$fit

and insert it into our model:


<figure>
<figcaption>Figure 8.7 Raw and adjusted school- quality measures. Three selected schools are marked.</figcaption>

2

30

adjscores

15

-2

8

6 -4 -2 0 2 4

rawscores

</figure>


<!-- PageBreak -->

<!-- PageNumber="199" -->
<!-- PageHeader="Random effects" -->

\> mmodc <- lmer(math ~
craven\*social+schraven\*social+ (1 | school) +
(1 | school : class) , jspr)
> anova (mmodc)
Analysis of Variance Table


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean</th>
<th>Sq</th>
<th>Denom</th>
<th>F value</th>
<th>Pr</th>
</tr>
<tr>
<td>craven</td>
<td>1</td>
<td>10166</td>
<td></td>
<td>10166</td>
<td>926</td>
<td>373.23</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>social</td>
<td>8</td>
<td>610</td>
<td></td>
<td>76</td>
<td>926</td>
<td>2.80</td>
<td>0.0045</td>
</tr>
<tr>
<td>schraven</td>
<td>1</td>
<td>5</td>
<td></td>
<td>5</td>
<td>926</td>
<td>0.18</td>
<td>0.6699</td>
</tr>
<tr>
<td>craven : social</td>
<td>8</td>
<td>561</td>
<td></td>
<td>70</td>
<td>926</td>
<td>2.58</td>
<td>0.0088</td>
</tr>
<tr>
<td>social : schraven</td>
<td>8</td>
<td>166</td>
<td></td>
<td>21</td>
<td>926</td>
<td>0.76</td>
<td>0.6353</td>
</tr>
</table>


We see that this new effect is not significant. We are not constrained to taking means. We
might consider various quantiles or measures of spread as potential compositional
variables.

Much remains to be investigated with this dataset. We have only used the simplest of
error structures and we should investigate whether the random effects may also depend
on some of the other covariates.

Further Reading: The classical approach to random effects can be found in many
older books such as Snedecor and Cochran (1989) or Scheffeé (1959). More recent books
such as Searle, Casella, and McCulloch (1992) also focus on the ANOVA approach. A
wide range of models are explicitly considered in Milliken and Johnson (1992).
Multilevel models are covered in Goldstein (1995) and Raudenbush and Bryk (2002).
The predecessor to the Ime4 package was nlme which is described in Pinheiro and Bates
(2000), but the book still contains much general material of interest.


## Exercises

1\. Use the pulp dataset for this question.

(a) Analyze the data as a fixed effects model. Is the operator significant?

(b) Analyze the data with operator as a random effect. What are the estimated
variances?

(c) Compute confidence intervals for these variances.

(d) Compute the intraclass correlation coefficient.

(e) Determine the significance of the operator effect using a likelihood ratio test taking
care to compute the p-value accurately.

2\. The coagulat ion dataset comes from a study of blood coagulation times. Twenty-four
animals were randomly assigned to four different diets and the samples were taken in
a random order.

(a) A new animal is assigned to diet D. Predict the blood coagulation time for this
animal along with an estimate of the variability in this prediction.

(b) $A$ new diet is given to a new animal. Predict the blood coagulation time for this
animal along with an estimate of the variability in this prediction.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 200" -->

(c) A new diet is given to the first animal in the dataset. Predict the blood coagulation
time for this animal along with an estimate of the variability in this prediction. You
may assume that the effects of the initial diet for this animal have washed out.

3\. The eggprod dataset concerns an experiment where six pullets were placed into each of
12 pens. Four blocks were formed from groups of three pens based on location. Three
treatments were applied. The number of eggs produced was recorded.

(a) Fit a model for the number of eggs produced with the treatments as fixed effects
and the blocks as random effects. Describe the estimated differences between the
treatments.

(b) Test for the significance of the treatment. Compute the p-value using both the $x ^ { 2 }$
distribution and resampling methods.

4\. Data on the cutoff times of lawnmowers may be found in the dataset lawn. 3 machines
were randomly selected from those produced by manufacturers $A$ and $B .$ Each
machine was tested twice at low speed and high speed.

(a) Fit a mixed effects model with manufacturer and speed as main effects along with
their interaction and machine nested in manufacturer as random effects. Write
down the formula for the model. In the summary output for the model, you will
find that fixed manufacturer effect has zero degrees of freedom. Explain why this is
so (check your model formula).

(b) Show why the manufacturer term may be removed from the fixed effect part of the
model.

(c) Determine if the manufacturer term can be removed from the random part of the
model.

5\. A number of growers supply broccoli to a food processing plant. The plant instructs
the growers to pack the broccoli into standard-size boxes. There should be 18 clusters
of broccoli per box and each cluster should weigh between 1.33 and 1.5 pounds.
Because the growers use different varieties and methods of cultivation, there is some
variation in the cluster weights. The plant manager selected three growers at random
and then four boxes at random supplied by these growers. Three clusters were selected
from each box. The data may be found in the broccoli dataset. The weight in grams of
the cluster is given. Estimate and test the variance components.

6\. An experiment was conducted to select the supplier of raw materials for production of
a component. The breaking strength of the component was the objective of interest.
Four suppliers were considered. The four operators can only produce one component
each per day. A latin square design is used and the data is presented in breaking.

(a) Explain why it would be natural to treat the operators and days as random effects
but the suppliers as fixed effects.

(b) Build a model to predict the breaking strength. Describe the variation from
operator to operator and from day to day.

(c) Test the significance of the supplier effect.

(d) Is there a significant difference between the operators?

(e) For the best choice of supplier, predict what proportion of components produced in
the future will have a breaking strength exceeding 900.

<!-- PageBreak -->

<!-- PageHeader="Random effects" -->
<!-- PageNumber="201" -->

7\. An experiment was conducted to optimize the manufacture of semiconductors. The
semicond data has the resistance recorded on the wafer as the response. The
experiment was conducted during four different time periods denoted by ET and three
different wafers during each period. The position on the wafer is a factor with levels 1
to 4. The Grp variable is a combination of ET and wafer. Analyze the data as a split
plot experiment where ET and position are considered as fixed effects. Since the
wafers are different in experimental time periods, the Grp variable should be regarded
as the block or group variable. Determine the best model for the data and check all
appropriate diagnostics.

8\. Redo the Junior Schools Project data analysis in the text with the final year English
score as the response. Highlight any differences from the analysis of the final year
Math scores.

9\. An experiment was conducted to determine the effect of recipe and baking temperature
on chocolate cake quality. Fifteen batches of cake mix for each recipe were prepared.
Each batch was sufficient for six cakes. Each of the six cakes was baked at a different
temperature which was randomly assigned. Several measures of cake quality were
recorded of which breaking angle was just one. The dataset is presented as choccake.

Build an appropriate model for the data and write a report on the analysis.

<!-- PageBreak -->

<!-- PageBreak -->


## CHAPTER 9 Repeated Measures and Longitudinal Data

In repeated measures designs, there are several individuals and measurements are taken
repeatedly on each individual. When these repeated measurements are taken over time, it
is called a longitudinal study or, in some applications, a panel study. Typically various
covariates concerning the individual are recorded and the interest centers on how the
response depends on the covariates over time. Often it is reasonable to believe that the
response of each individual has several components: a fixed effect, which is a function of
the covariates; a random effect, which expresses the variation between individuals; and
an error, which is due to measurement or unrecorded variables.

Suppose each individual has response $y _ { i } ,$ a vector of length $n _ { i }$ which is modeled
conditionally on the random effects $\gamma i$ as:

$$y _ { i } | \gamma _ { i } \sim N \left( X _ { i } \beta + Z _ { i } \gamma _ { i } , \sigma ^ { 2 } \Lambda _ { i } \right)$$

Notice this is very similar to the model used in the previous chapter with the exception of
allowing the errors to have a more general covariance ai. As before, we assume that the
random effects $\gamma i \sim N \left( 0 , \sigma ^ { 2 } D \right)$ so that:

$$y _ { i } \sim N \left( X _ { i } B , \Sigma _ { i } \right)$$

where
$\Sigma _ { i } = \sigma ^ { 2 } \left( A _ { i } + Z _ { i } D Z _ { i } ^ { T } \right)$
"Now suppose we have $M$ individuals and we can assume
the errors and random effects between individuals are uncorrelated, then we can combine
the data as:

$$y = \left[ \begin{array}{} { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { M } } \end{array} \right] \quad X = \left[ \begin{array}{} { X _ { 1 } } \\ { X _ { 2 } } \\ { X _ { M } } \end{array} \right] \quad \quad \quad Y = \left[ \begin{array}{} { \gamma _ { 1 } } \\ { T _ { 2 } } \\ { x _ { 1 } } \end{array} \right]$$

and $\widetilde { D } = d i a g \left( D , D , \ldots , D \right) , _ { Z = d i a g \left( Z _ { 1 } , Z _ { 2 } , \ldots , Z _ { M } \right) , \Sigma = d i a g \left( 2 \right) } ,$ $\Sigma = \mathrm { d i a g } \left( \Sigma _ { 1 } , \Sigma _ { 2 } , \ldots , \Sigma _ { M } \right) ,$ and
$\Lambda = d i a g \left( \Lambda _ { 1 } , \Lambda _ { 2 } , \ldots , \Lambda _ { M } \right) .$ Now we can write the model simply as

$$y \sim N \left( X \beta , \Sigma \right) \quad \Sigma = \sigma ^ { 2 } \left( A + Z D Z ^ { T } \right)$$

The log-likelihood for the data is then computed as above and estimation, testing,
standard errors and confidence intervals all follow using standard likelihood theory as
before. In fact, there is no strong distinction between the methodology used in this and
the previous chapter.

Of course, this general structure encompasses a wide range of possible models for
different types of data. We explore some of these in the following three examples:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 204


### 9.1 Longitudinal Data

The Panel Study of Income Dynamics (PSID), begun in 1968, is a longitudinal study of a
representative sample of U.S. individuals described in Hill (1992). The study is
conducted at the Survey Research Center, Institute for Social Research, University of
Michigan, and is still continuing. There are currently 8700 households in the study and
many variables are measured. We chose to analyze a random subset of this data,
consisting of 85 heads of household who were aged 25-39 in 1968 and had complete data
for at least 11 of the years between 1968 and 1990. The variables included were annual
income, gender, years of education and age in 1968:

\> data (psid)
> head (psid)


<table>
<tr>
<th></th>
<th>age</th>
<th>educ</th>
<th>sex</th>
<th>income</th>
<th>year</th>
<th>person</th>
</tr>
<tr>
<td>1</td>
<td>31</td>
<td>12</td>
<td>M</td>
<td>6000</td>
<td>68</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>31</td>
<td>12</td>
<td>M</td>
<td>5300</td>
<td>69</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>31</td>
<td>12</td>
<td>M</td>
<td>5200</td>
<td>70</td>
<td>1</td>
</tr>
<tr>
<td>4</td>
<td>31</td>
<td>12</td>
<td>M</td>
<td>6900</td>
<td>71</td>
<td>1</td>
</tr>
<tr>
<td>5</td>
<td>31</td>
<td>12</td>
<td>M</td>
<td>7500</td>
<td>72</td>
<td>1</td>
</tr>
<tr>
<td>6</td>
<td>31</td>
<td>12</td>
<td>M</td>
<td>8000</td>
<td>73</td>
<td>1</td>
</tr>
</table>


Now plot the data:

\> library (lattice)
> xyplot (income ~ year | person, psid, type="1",
subset= (person < 21) , strip=FALSE)

The first 20 subjects are shown in Figure 9.1. We see that some individuals have a slowly
increasing income, typical of someone in steady employment in the same job. Other
individuals have more erratic incomes. We can also show how the incomes vary by sex.
Income is more naturally considered on a log-scale:

$$> x y p l o t \left( l o g \left( i n c o m e + 1 0 0 \right) \sim y e a r | s e x , p s i d , t y p e = 1 \right)$$

See Figure 9.2. We added $100 to the income of each subject to remove the effect of
some subjects having very low incomes for short periods of time. These cases distorted
the plots without the adjustment. We see that men's incomes are generally higher and less
variable while women's incomes are more variable, but are perhaps increasing more
quickly. We could fit a line to each subject starting with the first:

\> lmod <- 1m(log(income) ~ I(year-78),
subset= (person == 1), psid)
> coef(lmod)
(Intercept) I (year - 78)
9.399957
0.084267

<!-- PageBreak -->

<!-- PageHeader="Repeated measures and longitudinal data" -->
<!-- PageNumber="205" -->

We have centered the predictor at the median value so that the intercept will represent the
predicted log income in 1978 and not the year 1900 which would be nonsense. We now
fit a line for all the subjects and plot the results:

\> slopes <- numeric (85) ; intercepts <- numeric (85)
> for (i in 1:85) {
lmod <- 1m(log(income) ~ I(year-78),

subset= (person == i), psid)
intercepts[i] <- coef(lmod)[1]
slopes[i] <- coef(lmod)[2]
}


<figure>
<figcaption>Figure 9.1 The first 20 subjects in the PSID data. Income is shown over time.</figcaption>

70 80 90

70 80 90

80000

60000

40000

20000

80000

0

60000

income

40000

20000

0

80000

60000

40000

$\begin{array}{} { 2 0 0 0 0 } \\ { 0 } \end{array}$

80000

$0$

60000

40000

20000

0

70 80 90

70 80 90

70 80 90

year

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 206" -->


<figure>
<figcaption>Figure 9.2 Income change in the PSID data grouped by sex.</figcaption>

70

75

80

85

90

$F$

M

log(income + 100)

12

10

8

6

70

75

80

85

90

year

</figure>


\> plot (intercepts, slopes, xlab="Intercept", ylab="Slope")
> psex <- psid$sex [match (1: 85, psid$person) ]

\> boxplot (split (slopes, psex) )

See Figure 9.3. We can simply compare the income growth rates for men and women:


<figure>
<figcaption>Figure 9.3 Slopes and intercepts for the individual income growth relationships are shown on the left. A comparison of income growth rates by sex is shown on the right.</figcaption>

0.3

0

0.3

0

0.2

2

Slope

0

0.1

0

0.1

0

0

0.0

0.0

8

7

8 9 10 11

F

M

Intercept

</figure>


\> t. test (slopes [psex == "M" ] , slopes [psex == "F" ] )
Welch Two Sample t-test
data: slopes [psex == "M"] and slopes [psex == "F"]
t = - 2.3786, df = 56.736, p-value = 0.02077
alternative hypothesis: true difference in means is not
equal to 0

<!-- PageBreak -->

<!-- PageNumber="207" -->
<!-- PageHeader="Repeated measures and longitudinal data" -->

95 percent confidence interval:
-0.0591687 -0.0050773
sample estimates :
mean of x mean of y
0.056910 0.089033

We see that women have a significantly higher growth rate than men. We can also
compare the incomes at the intercept (which is 1978):

\> t. test (intercepts [psex == "M"] , intercepts [psex == "F" ] ) )
Welch Two Sample t-test
data: intercepts [psex == "M"] and intercepts [psex ==
"F"]
t = 8.2199, df = 79.719, p-value = 3.065e-12
alternative hypothesis: true difference in means is not
equal to 0
95 percent confidence interval:
0.87388 1.43222
sample estimates :
mean of x mean of y
9.3823 8.2293

We see that men have significantly higher incomes.

This is an example of a response feature analysis. It requires choosing an important
characteristic. We have chosen two here: the slope and the intercept. For many datasets,
this is not an easy choice and at least some information is lost by doing this.

Response feature analysis is attractive because of its simplicity. By extracting a
univariate response for each individual, we are able to use a wide array of well-known
statistical techniques. However, it is not the most efficient use of the data as all the
additional information besides the chosen response feature is discarded. Notice that
having additional data on each subject would be of limited value.

Suppose that the income change over time can be partly predicted by the subject's age,
sex and educational level. We do not expect a perfect fit. The variation may be
partitioned into two components. Clearly there are other factors that will affect a subject's
income. These factors may cause the income to be generally higher or lower or they may
cause the income to grow at a faster or slower rate. We can model this variation with a
random intercept and slope, respectively, for each subject. We also expect that there will
be some year-to-year variation within each subject. For simplicity, let us initially assume
that this error is homogeneous and uncorrelated, that is, $A _ { i } = I .$ We also center the year to
aid interpretation as before. We may express these notions in the model:

\> library(lme4)
> psid$cyear <- psid$year-78
> mmod <- 1mer (log (income) ~ cyear*sex
tageteduc+ (cyear | person) , psid)

This model can be written as:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 208" -->

$$\mathrm { l o g \left( i n c o m e \right) } _ { i j } = \mu + \beta _ { \mathrm { y } } \mathrm { y e a r } _ { i } + \beta _ { \mathrm { s S } } \mathrm { s e x } _ { j } + \beta _ { \mathrm { y s } } \mathrm { s e x } _ { j } \times \mathrm { y } _ { \mathrm { e } } \mathrm { e d u c } _ { j } + \beta _ { \mathrm { a } } \mathrm { a g e } _ { j }$$
$$+ \quad \gamma _ { j } ^ { 0 } + \gamma _ { j } ^ { 1 } \text { ycar } _ { i } + \varepsilon _ { i j }$$

where $i$ indexes the year and $j$ indexes the individual. We have:

$$\left( \begin{array}{} { \pi } \\ { \pi } \end{array} \right) \sim N \left( 0 , \sigma ^ { 2 } D \right)$$

The model summary is:

\> summary (mmod)

Linear mixed-effects model fit by REML

Formula: log (income) ~ cyear * sex + age + educ +
(cyear | person)

Data: psid

AIC
BIG
logLik MLdeviance REMLdeviance

3839.8 3893.9 -1909.9

3785.6
3819.8

Random effects:

Groups Name

Variance
Std. Dev. Corr

person
(Intercept)
0.2817

0.531

cyear
0.0024

0.049

0.187

Residual

0.4673

0.684

\# of obs: 1661, groups: person, 85

Fixed effects:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>DF</th>
<th>t value</th>
<th>$\mathrm { P r } \left( > | t | \right)$</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>6.6742</td>
<td>0.5433</td>
<td>1655</td>
<td>12.28</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>cyear</td>
<td>0.0853</td>
<td>0.0090</td>
<td>1655</td>
<td>9.48</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>$\mathrm { s e x M }$</td>
<td>1.1503</td>
<td>0.1213</td>
<td>1655</td>
<td>9.48</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>age</td>
<td>0.0109</td>
<td>0.0135</td>
<td>1655</td>
<td>0.81</td>
<td>0.419</td>
</tr>
<tr>
<td>educ</td>
<td>0.1042</td>
<td>0.0214</td>
<td>1655</td>
<td>4.86</td>
<td>0.0000013</td>
</tr>
<tr>
<td>cyear : sexM</td>
<td>-0.0263</td>
<td>0.0122</td>
<td>1655</td>
<td>-2.15</td>
<td>0.032</td>
</tr>
</table>


Let's start with the fixed effects. We see that income increases about 10% for each
additional year of education. We see that age does not appear to be significant. For
females, the reference level in this example, income increases about 8.5% a year, while
for men, it increases about $8 . 5 - 2 . 6 = 5 . 9 a \quad y e a r .$ We see that, for this data, the incomes of
men are exp(1.15) = 3.16 times higher.

We know the mean for males and females, but individuals will vary about this. The
standard deviation for the intercept and slope are 0.28 and 0.0024 $\sigma \sqrt { D _ { 1 1 } }$ and $\sigma \sqrt { D _ { 2 2 } }$
respectively. These have a correlation of 0.19 $\left( \cot \left( \gamma ^ { 0 } , \gamma ^ { 1 } \right) \right) .$ Finally, there is some
additional variation in the measurement not so far accounted for having standard
deviation of 0.46 $\left( s d \left( s _ { i j k } \right) \right) .$ We see that the variation in increase in income is relatively
small while the variation in overall income between individuals is quite large.
Furthermore, given the large residual variation, there is a large year-to-year variation in
incomes.

There is a wider range of possible diagnostic plots that can be made with longitudinal
data than with a standard linear model. In addition to the usual residuals, there are

<!-- PageBreak -->

<!-- PageNumber="209" -->
<!-- PageHeader="Repeated measures and longitudinal data" -->

random effects to be examined. We may wish to break the residuals down by sex as seen
in the QQ plots in Figure 9.4:

$$> \mathrm { q q m a t h } \left( \sim \mathrm { r e s i d } \left( \mathrm { m m o d } \right) \quad | \quad \mathrm { s e x } _ { \prime } \quad \mathrm { p s i d } \right)$$


<figure>
<figcaption>Figure 9.4 QQ plots by sex.</figcaption>

-2

0

2

$F$

$\bar { M }$

2

0

0

resid(mmod)

0

-2

-4

0

-6

O

0

I

1

-2

0

2

qnorm

</figure>


We see that the residuals are not normally distributed, but have a long tail for the lower
incomes. We should consider changing the log transformation on the response.
Furthermore, we see that there is greater variance in the female incomes. This suggests a
modification to the model. We can make the same plot broken down by subject although
there will be rather too many plots to be useful.

Plots of residuals and fitted values are also valuable. We have broken education into
three levels: less than high school, high school or more than high school:

\> xyplot (resid (mmod) ~ fitted (mmod)
|

cut (educ, c (0, 8.5, 12.5,20) ) ,
psid, layout=c(3,l),xlab="Fitted",ylab="Residuals")

See Figure 9.5. Again, we can see evidence that a different response transformation
should be considered.

Plots of the random effects would also be useful here.


### 9.2 Repeated Measures

The acuity of vision for seven subjects was tested. The response is the lag in milliseconds
between a light flash and a response in the cortex of the eye. Each eye is tested at four
different powers of lens. An object at the distance of the second number appears to be at
distance of the first number. The data is given in Table 9.1. The data comes from
Crowder and Hand (1990) and was also analyzed by Lindsey (1999).

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 210" -->


<figure>
<figcaption>Figure 9.5 Residuals vs. fitted plots for three levels of education: less than high school on the left, high school in the middle and more than high school on the right.</figcaption>

6 7 8 9 10 11

(0.8.5]

(8.5.12.5]

(12.5.20]

2

Residuals

8

6 7 8 9 10 11

6 7 8 9 10 11

Fitted

</figure>


We start by making some plots of the data. We create a numerical variable
representing the power to complement the existing factor so that we can see how the
acuity changes with increasing power:

\> data (vision)
> vision$npower <- rep (1:4,14)
>
xyplot (acuity~npower | subject, vision, $= ^ { n } 1 ^ { n } ,$ groups=eye
lty=1:2, layout=c (4, 2) )
,

See Figure 9.6. There is no apparent trend or difference between right and left eyes.

feet.

However, individual #6 appears anomalous with a large difference between the eyes. It
also seems likely that the third measurement on the left eye is in error for this individual.

<!-- PageBreak -->

<!-- PageHeader="Repeated measures and longitudinal data 211" -->


<figure>
<figcaption>Figure 9.6 Visual acuity profiles. The left eye is shown as a solid line and the right as $a$ dashed line. Four powers of lens are displayed where $1 = 6 / 6 ,$ $2 = 6 / 1 8 ,$ $3 = 6 / 3 6$ and $4 = 6 / 6 0 .$</figcaption>

1.0 2.0 3.0 4.0

5

6

7

125

120

115

110

105

100

acuity

95

1

2

3

4

125

120

115

110

105

100

95

1.0 2.0 3.0 4.0

1.0 2.0 3.0 4.0

npower

</figure>


<table>
<tr>
<th>6/6</th>
<th colspan="7">Power 6/18 6/36 6/60 6/6 $6 / 1 8$ 6/36 $6 / 6 0$ Left Right</th>
</tr>
<tr>
<td>116</td>
<td>119</td>
<td>116</td>
<td>124</td>
<td>120</td>
<td>117</td>
<td>114</td>
<td>122</td>
</tr>
<tr>
<td>110</td>
<td>110</td>
<td>114</td>
<td>115</td>
<td>106</td>
<td>112</td>
<td>110</td>
<td>110</td>
</tr>
<tr>
<td>117</td>
<td>118</td>
<td>120</td>
<td>120</td>
<td>120</td>
<td>120</td>
<td>120</td>
<td>124</td>
</tr>
<tr>
<td>112</td>
<td>116</td>
<td>115</td>
<td>113</td>
<td>115</td>
<td>116</td>
<td>116</td>
<td>119</td>
</tr>
<tr>
<td>113</td>
<td>114</td>
<td>114</td>
<td>118</td>
<td>114</td>
<td>117</td>
<td>116</td>
<td>112</td>
</tr>
<tr>
<td>119</td>
<td>115</td>
<td>94</td>
<td>116</td>
<td>100</td>
<td>99</td>
<td>94</td>
<td>97</td>
</tr>
<tr>
<td>110</td>
<td>110</td>
<td>105</td>
<td>118</td>
<td>105</td>
<td>105</td>
<td>115</td>
<td>115</td>
</tr>
</table>


Table 9.1 Visual acuity of seven
subjects measured in milliseconds of
lag in responding to a light flash. The
power of the lens causes an object six
feet distant to appear at a distance of
6, 18, 36 or 60

We must now decide how to model the data. The power is a fixed effect. In the model
below, we have treated it as a nominal factor, but we could try fitting it in a quantitative
manner. The subjects should be treated as random effects. Since we do not believe there

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 212

is any consistent right-left eye difference between individuals, we should treat the eye
factor as nested within subjects. We start with this model:

$$l m e r \left( a c u i t y \sim p o w e r + \left( 1 | s u b j e c t \right) + \left( 1 | s u b j e c t : e y e \right) , v i s i o n \right)$$

Note that if we did believe there was a consistent left vs. right eye effect, we would have
used crossed random effects, putting (11 eye) in place of (11 subject: eye).

We can write this (nested) model as:

$y _ { i j k } = \mu + P _ { j } + s _ { i } + e _ { i k } + 8 _ { i j k }$

where $i = 1 , \ldots , 7$ runs over individuals, $j = 1 , \ldots , 4$ runs over power and $k = 1 ,$ 2 runs over
eyes. The $p _ { j }$ term is a fixed effect, but the remaining terms are random. Let
$s _ { i } \sim N \left( 0 , \sigma _ { s } ^ { 2 } \right) ,$ $e _ { i k } \sim N \left( 0 , \sigma _ { e } ^ { 2 } \right) _ { a n d } e _ { i j k } \sim N \left( 0 , \sigma ^ { 2 } \Sigma \right) _ { \text { where } }$ we take $\Sigma = I .$ The summary
output is:

\> summary (mmod)

Linear mixed-effects model fit by REML
Formula: acuity ~ power + (1 | subject) + (1 |
subject : eye)

Data: vision

AIC
BIG
logLik MLdeviance REMLdeviance
342.71 356.89 -164.35
339.22
328.71

Random effects:

Groups
Name

Variance Std. Dev.

subject: eye (Intercept) 10.3
3.21
subject
(Intercept) 21.5

4.64
Residual
16.6
4.07

\# of obs: 56, groups: subject: eye, 14; subject, 7
Fixed effects:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>DF</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>112.643</td>
<td></td>
<td>2.235</td>
<td>52</td>
<td>50.40</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>power6/18</td>
<td>0.786</td>
<td></td>
<td>1.540</td>
<td>52</td>
<td>0.51</td>
<td>0.612</td>
</tr>
<tr>
<td>power6/36</td>
<td>-1.000</td>
<td></td>
<td>1.540</td>
<td>52</td>
<td>-0.65</td>
<td>0.519</td>
</tr>
<tr>
<td>power6/60</td>
<td>3.286</td>
<td></td>
<td>1.540</td>
<td>52</td>
<td>2.13</td>
<td>0.038</td>
</tr>
</table>


We see that the estimated standard deviation for subjects is 4.64 and that for eyes for a
given subject is 3.21. The residual standard deviation is 4.07. The random effects
structure we have used here induces a correlation between measurements on the same
subject and another between measurements on the same eye. We can compute these two
correlations respectively as:

\> 4.64^2/(4.64^2+3.21^2+4.07^2)
[1] 0.44484
> (4.64^2+3.21^2) / (4.64^2+3.21^2+4.07^2)
[1] $0 . 6 5 7 7 4$

<!-- PageBreak -->

<!-- PageNumber="213" -->
<!-- PageHeader="Repeated measures and longitudinal data" -->

As we might expect, there is a stronger correlation between observations on the same eye
than between the left and right eyes of the same individual.

We can check for a power effect:

\> anova (mmod)
Analysis of Variance Table


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean</th>
<th>Sq</th>
<th>Denom</th>
<th>F value</th>
<th>Pr (&gt;F)</th>
</tr>
<tr>
<td>power</td>
<td>3</td>
<td>140.8</td>
<td></td>
<td>46.9</td>
<td>52.0</td>
<td>2.83</td>
<td>0.048</td>
</tr>
</table>


We see the result is just significant at the 5% level. We might expect some trend in acuity
with power, but the estimated effects do not fit with this trend. While acuity is greatest at
the highest power, 6/60, it is lowest for the second highest power, 6/36. A look at the data
makes one suspect the measurement made on the left eye of the sixth subject at this
power. If we omit this observation and refit the model, we find:

\> mmodr <-
lmer (acuity~power+ (1 | subject) + (1 | subject : eye) ,
vision, subset =- 43)
> anova (mmodr)
Analysis of Variance Table
Df Sum Sq Mean Sq Denom F value Pr (>F)
power 3 89.2
29.7 51.0
3.6 0.020
> summary (mmodr)
Fixed effects :


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>DF</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>112.643</td>
<td></td>
<td>1.880</td>
<td>51</td>
<td>59.91</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>power6/18</td>
<td>0.786</td>
<td></td>
<td>1.087</td>
<td>51</td>
<td>0.72</td>
<td>0.4731</td>
</tr>
<tr>
<td>power6/36</td>
<td>0.521</td>
<td></td>
<td>1.114</td>
<td>51</td>
<td>0.47</td>
<td>$0 . 6 4 1 8$</td>
</tr>
<tr>
<td>power6/60</td>
<td>3.286</td>
<td></td>
<td>1.087</td>
<td>51</td>
<td>3.02</td>
<td>0.0039</td>
</tr>
</table>


Now the power effect is significant, but it appears this is due to an effect at the highest
power only. We can test the hypothesis that the highest power has a higher acuity than
the average of the first three levels by using Helmert contrasts:

\> op <- options (contrasts=c ("contr. helmert",
"contr . poly") )
> mmodr <-
lmer (acuity~power+ (1 | subject) + (1 | subject : eye) , vision, su
bset =- 43)
> summary (mmodr)
Fixed effects :


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>DF</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>113.7911</td>
<td>1.7596</td>
<td>51</td>
<td>64.67</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>powerl</td>
<td>0.3929</td>
<td>0.5436</td>
<td>51</td>
<td>0.72</td>
<td>0.4731</td>
</tr>
<tr>
<td>power2</td>
<td>0.0428</td>
<td>0.3242</td>
<td>51</td>
<td>0.13</td>
<td>0.8954</td>
</tr>
<tr>
<td>power3</td>
<td>0.7125</td>
<td>0.2228</td>
<td>51</td>
<td>3.20</td>
<td>0.0024</td>
</tr>
</table>


\> options (op)

The Helmert contrast matrix is

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 214" -->


<table>
<tr>
<th>&gt;</th>
<th colspan="2">contr.helmert (4) [, 1] [,2] [,3]</th>
</tr>
<tr>
<td>1</td>
<td>-1 -1</td>
<td>-1</td>
</tr>
<tr>
<td>2</td>
<td>1 -1</td>
<td>-1</td>
</tr>
<tr>
<td>3</td>
<td>0 2</td>
<td>-1</td>
</tr>
<tr>
<td>4</td>
<td>0 0</td>
<td>3</td>
</tr>
</table>


We can see that the third contrast (column) represents the difference between the average
of the first three levels and the fourth level, scaled by a factor of three. In the output, we
can see that this is statistically significant while the other two contrasts are not.

We finish with some diagnostic plots. The residuals and fitted values and the QQ plot
of random effects for the eyes are shown in Figure 9.7:

\> plot (resid (mmodr) ~
fitted (mmodr) , xlab="Fitted", ylab="Residuals")
> abline $\left( h = 0 \right)$
> qqnorm (ranef (mmodr) $"subject : eye" [ [1] ] , main="")


<figure>
<figcaption>Figure 9.7 Residuals vs. fitted plot is shown on the left and a QQ plot of the random effects for the eyes is shown on the right.</figcaption>

5

4

Residuals

Sample Quantiles

2

O

-5

2

100 105 110 115 120

0

1

Fitted

Theoretical Quantiles

</figure>


The outlier corresponds to the right eye of subject #6. For further analysis, we should
consider dropping subject #6. There are only seven subjects altogether, so we would
certainly regret losing any data, but this may be unavoidable. Ultimately, we may need
more data to make definite conclusions.


### 9.3 Multiple Response Multilevel Models

In Section 8.8, we analyzed some data from the Junior Schools Project. In addition to a
math test, students also took a test in English. Although it would be possible to analyze
the English test results in the same way that we analyzed the math scores, additional

<!-- PageBreak -->

<!-- PageNumber="215" -->
<!-- PageHeader="Repeated measures and longitudinal data" -->

information may be obtained from analyzing them simultaneously. Hence we view the
data as having a bivariate response with English and math scores for each student. The
student is a nested factor within the class which is in turn nested within the school. We
express the multivariate response for each individual by introducing an additional level of
nesting at the individual level. So we might view this as just another nested model except
that there is a fixed subject effect associated with this lowest level of nesting.

We set up the data in a format with one test score per line with an indicator subject
identifying which type of test was taken. We scale the English and math test scores by
their maximum possible values, 40 and 100, respectively, to aid comparison:

\> data (jsp)

\> jspr <- jsp[jsp$year == 2, ]

\> mjspr <- data. frame (rbind (jspr [, 1 : 6] , jspr [, 1 : 6] ),
subject=factor (rep (c("english", "math") , c (953, 953) ) ) ,
score=c (jspr$english/100, jspr$math/40) )

We can examine the relationship between subject, gender and scores, as seen in Figure
9.8:


<figure>
<figcaption>Figure 9.8 Scores on test compared to raven score for subjects and genders.</figcaption>

10

20

30

1

girl

girl

english

math

1.0

0.8

0

0.6

0.4

0

0

0.2

0

0.0

score

boy

boy

english

math

1.0

0.8

0

0

0

0.6

0.4

0.2

0

0

0.0

1

10

20

30

raven

</figure>


\> xyplot (score ~ raven | subject*gender, mjspr)

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 216

We now fit a model for the data that includes all the variables of interest that incorporates
some of the interactions that we suspect might be present:

\> mjspr$craven <- mjspr$raven-mean (mjspr$raven)
> mmod <- lmer (score ~
subject\*gender+craven\*subject+social+
(1 | school) + (1 | school : class) + (1 | school : class : id) , mjspr
)

The model being fit for school $i ,$ class $j ,$ student $k$ in subject l is:
scorejkisubject/+genderk+ravenk+socialk+(subject×gender) Ik+
(raven×subject) [k+school;+class;+studentk+&ijkl

where the Raven score has been mean centered and school, class and student are random
effects with the other terms, apart from &, being fixed effects. The test on the fixed effects
reveals:

\> anova (mmod)

Analysis of Variance Table


<table>
<tr>
<th></th>
<th>Df</th>
<th>Sum Sq</th>
<th>Mean Sq</th>
<th>Denom</th>
<th>F value</th>
<th></th>
</tr>
<tr>
<td>subject</td>
<td>1</td>
<td>54</td>
<td>54</td>
<td>1892</td>
<td>3953.67</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>gender</td>
<td>1</td>
<td>0.101</td>
<td>0.101</td>
<td>1892</td>
<td>7.46</td>
<td>0.0064</td>
</tr>
<tr>
<td>craven</td>
<td>1</td>
<td>6</td>
<td>6</td>
<td>1892</td>
<td>444.63</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>social</td>
<td>8</td>
<td>1</td>
<td>0.088</td>
<td>1892</td>
<td>6.47</td>
<td>2.5e-08</td>
</tr>
<tr>
<td>subject : gender</td>
<td>1</td>
<td>0.384</td>
<td>0.384</td>
<td>1892</td>
<td>28.23</td>
<td></td>
</tr>
<tr>
<td>subject : craven</td>
<td>1</td>
<td>0.217</td>
<td>0.217</td>
<td>1892</td>
<td>15.99</td>
<td>6.6e-05</td>
</tr>
</table>


Both interactions are significant so no simplifications are indicated for this model. We
might consider adding additional fixed effects, but we shall attempt to interpret only this
model for now. The summary output:

\> summary (mmod)

Linear mixed-effects model fit by REML
Formula: score ~ subject * gender + craven * subject +
social + (1 | school) +
(1 | school: class) + (1 | school : class : id)
Data: mjspr

AIC
BIG logLik MLdeviance REMLdeviance
-1705.6 -1605.6 870.79
-1846.3
-1741.6

Random effects:


<table>
<tr>
<th>Groups</th>
<th>Name</th>
<th>Variance</th>
<th>Std. Dev.</th>
</tr>
<tr>
<td>school:class:id</td>
<td>(Intercept)</td>
<td>0.010252</td>
<td>0.1013</td>
</tr>
<tr>
<td>school : class</td>
<td>(Intercept)</td>
<td>0.000582</td>
<td>0.0241</td>
</tr>
<tr>
<td>school</td>
<td>(Intercept)</td>
<td>0.002231</td>
<td>0.0472</td>
</tr>
<tr>
<td>Residual</td>
<td></td>
<td>0.013592</td>
<td>0.1166</td>
</tr>
</table>


\# of obs: 1906, groups: school: class:id, 953;
school:class, 90; school, 48
Fixed effects:

<!-- PageBreak -->

<!-- PageNumber="217" -->
<!-- PageHeader="Repeated measures and longitudinal data" -->


<table>
<tr>
<th colspan="3"></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>DF t</th>
</tr>
<tr>
<td colspan="3">value $\mathrm { P r } \left( > | \mathrm { t } | \right)$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">(Intercept)</td>
<td>0.441578</td>
<td>0.026459</td>
<td></td>
</tr>
<tr>
<td>1892</td>
<td colspan="2">16.69 &lt; 2e-16</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">subjectmath</td>
<td>0.366565</td>
<td>0.007710</td>
<td></td>
</tr>
<tr>
<td></td>
<td colspan="2">$< 2 e - 1 6$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">gendergirl</td>
<td>0.063351</td>
<td>0.010254</td>
<td></td>
</tr>
<tr>
<td>1892</td>
<td colspan="2">6.18 7 $9 e - 1 0$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">craven</td>
<td>0.017390</td>
<td>0.000925</td>
<td></td>
</tr>
<tr>
<td>1892</td>
<td colspan="2">18.81 &lt; 2e-16</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">$\mathrm { s o c i a l } 2$</td>
<td>0.013754</td>
<td>0.027230</td>
<td></td>
</tr>
<tr>
<td>1892</td>
<td colspan="2">0.51 0.6136</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">$\mathrm { s o c i a l } 3$</td>
<td>-0.020768</td>
<td>0.028972</td>
<td>1892 -</td>
</tr>
<tr>
<td>0.72</td>
<td colspan="2">0.4736</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">social4</td>
<td>-0.070708</td>
<td>0.025868</td>
<td>1892 -</td>
</tr>
<tr>
<td></td>
<td colspan="2">$2 . 7 3 \quad 0 . 0 0 6 3$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">social5</td>
<td>-0.050474</td>
<td>0.028818</td>
<td>1892 -</td>
</tr>
<tr>
<td>1.75</td>
<td colspan="2">0.0800</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">social6</td>
<td>-0.087852</td>
<td>0.030672</td>
<td>1892 -</td>
</tr>
<tr>
<td>2.86</td>
<td colspan="2">0.0042</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">social7</td>
<td>-0.099408</td>
<td>0.031607</td>
<td>1892 -</td>
</tr>
<tr>
<td>3.15</td>
<td colspan="2">0.0017</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">social8</td>
<td></td>
<td>-0.081623</td>
<td>0.042352</td>
<td>1892 -</td>
</tr>
<tr>
<td></td>
<td colspan="2">$1 . 9 3 \quad 0 . 0 5 4 1$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3"></td>
<td>-0.047337</td>
<td>0.027445</td>
<td>1892 -</td>
</tr>
<tr>
<td colspan="3">1.72 0.0847</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">subjectmath : gendergirl</td>
<td>-0.059194</td>
<td>0.010706</td>
<td>1892 -</td>
</tr>
<tr>
<td colspan="3">5.53 3.7e-08</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">subjectmath : craven</td>
<td>-0.003720</td>
<td>0.000930</td>
<td>1892 -</td>
</tr>
<tr>
<td>4.00</td>
<td colspan="2">6.6e-05</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


Starting with the fixed effects, we see that the math subject scores were about 37% higher
than the English scores. This may just reflect the grading scale and difficulty of the test
and so perhaps nothing in particular should be concluded from this except, of course, that
it is necessary to have this term in the model to control for this difference. Since gender
has a significant interaction with subject, we must interpret these terms together. We see
that on the English test, which is the reference level, girls score 6.5% higher than boys.
On the math test, the difference is 6.5-5.9=0.6% which is negligible. We see that the
scores are strongly related to the entering Raven score although the relation is slightly
less strong for math than English (slope is 0.0179 for English but $0 . 0 1 7 9 - 0 . 0 0 3 7 = 0 . 0 1 4 2$
for math). We also see the declining performance as we move down the social class scale
as we found in the previous analysis.

Moving to the random effects, we see that standard deviation of the residual error in
the math scores was 59% of that observed in the English scores. Perhaps this can be
ascribed to the greater ease of consistent grading of math assignments or perhaps just
greater variation is to be expected in English performance. The correlation between the
English and math scores after adjusting for the other effects is also of interest. The last
two terms in the model, $s t u d e n t _ { k } + g _ { i j k l } ,$ represent a $2 \times 2$ covariance matrix for the residual
scores for the two tests. We can compute the correlation as:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 218

$$> 0 . 1 0 1 3 ^ { \wedge } 2 / \left( 0 . 1 0 1 3 ^ { \wedge } 2 + 0 . 1 1 6 6 ^ { \wedge } 2 \right)$$

[1] 0.43013

giving a moderate positive correlation between the scores. Various diagnostic plots can
be made. An interesting one is:

\> xyplot (residuals (mmod) ~

$$| \text { subject min } \mathrm { s p r } _ { \prime } \mathrm { p c } _ { \prime } \mathrm { p c h } _ { \bullet } ^ { \prime } \mathrm { n t e d } _ { \bullet } ^ { \prime } ,$$
$$\left. x l a b = { } ^ { \prime \prime } F i t e d ^ { \prime \prime } , y l a b = { } ^ { \prime \prime } R e s i d u a l s ^ { \prime \prime } \right)$$

as seen in Figure 9.9. There is somewhat greater variance in the verbal scores. The
truncation effect of the maximum score is particularly visible for the math scores.


<figure>
<figcaption>Figure 9.9 Residuals vs. fitted plot broken down by type of test.</figcaption>

0.0 0.2 0.4 0.6 0.8 1.0

english

math

0.3

Residuals

0.2

0.1

0.0

-0.1

-0.2

-0.3

0.0 0.2 0.4 0.6 0.8 1.0

Fitted

</figure>


Further Reading: Longitudinal data analysis is explicitly covered in books by Verbeke
and Molenberghs (2000), Fitzmaurice, Laird, and Ware (2004), Diggle, Heagerty, Liang,
and Zeger (2002) and Frees (2004). Books stating repeated measures in the title, such as
Lindsey (1999), cover much the same material.


### Exercises

1\. The ratdrink data consist of five weekly measurements of body weight for 27 rats. The
first 10 rats are on a control treatment while seven rats have thyroxine added to their
drinking water. Ten rats have thiouracil added to their water. Build a model for the rat
weights that shows the effect of the treatment.

2\. Data on housing prices in 36 metropolitan statistical areas (MSAs) over nine years
from 1986-94 were collected and can be found in the dataset hprice. Find a good
model for the data. Explain the effect of the predictors on housing prices. It is not
necessary to present every part of your analysis. Present a compact description of how
you found your model in five pages or less.

<!-- PageBreak -->

<!-- PageHeader="Repeated measures and longitudinal data 219" -->

3\. The nepali data is a subset from public health study on Nepalese children. Develop a
model for the weight of the child as he or she ages. You may use mage, lit, died,
gender and alive (but not ht) as predictors. Show how you developed your model and
interpret your final model.

4\. The attenu data gives peak accelerations measured at various observation stations for
23 earthquakes in California. The data has been used by various workers to estimate
the attenuating affect of distance on ground acceleration.

(a) Model the $\log$ of the acceleration as a function of the log of the distance while
taking account of the magnitude of the quake.

(b) Predict how the acceleration varied for an earthquake of magnitude 7.5. Express
quantitatively the uncertainty in this prediction.

(c) Predict how the acceleration varied for the first event where only one observation
was available.

5\. The sleepstudy data found in the Matrix package, which is loaded with Ime4, describes
the reaction times of subjects who are progressively sleep deprived. Form a model for
the reaction times and describe the variation between individuals.

<!-- PageBreak -->

<!-- PageBreak -->


## CHAPTER 10 Mixed Effect Models for Nonnormal Responses


### 10.1 Generalized Linear Mixed Models

Generalized linear mixed models (GLMM) combine the ideas of generalized linear
models with the random effects modeling ideas of the previous two chapters. The
response is a random variable, $Y _ { \dot { \nu } } ,$ taking observed values, $y _ { i }$ for $i = 1 , \ldots , n ,$ and follows an
exponential family distribution as defined in Chapter 6:

$$f \left( y _ { i } | \theta _ { i } , \phi \right) = \exp \left[ \frac { y _ { i } \theta _ { i } - b \left( \theta _ { i } \right) } { a \left( \phi \right) } + c \left( y , \phi \right) \right]$$

Let $E Y _ { i } = \mu _ { i }$ and let this be connected to the linear predictor $\eta _ { i }$ using the link function $g$ by
$\eta _ { i } = g \left( \mu _ { i } \right) .$ Suppose for simplicity that we use the canonical link for $\mathrm { g }$ so that we may make
the direct connection that $\theta _ { i } = \mu _ { i } .$

Now let the random effects, $\gamma ,$ have distribution $h \left( \gamma | V \right)$ for parameters $V .$ The fixed
effects are $\beta .$ Conditional on the random effects, $\gamma :$

$$\theta _ { i } = x _ { i } ^ { T } \beta + z _ { i } ^ { T } r$$

where $x _ { i }$ and $z _ { i }$ are the corresponding rows from the design matrices, $X$ and $Z ,$ for the
respective fixed and random effects. Now the likelihood may be written as:

$$L \left( \beta , \phi , V | y \right) = \prod _ { i = 1 } ^ { n } \int f \left( y _ { i } | \beta _ { i } , \phi , \gamma \right) h \left( \gamma | V \right) d Y$$

Typically the random effects are assumed normal: $\gamma \sim N \left( 0 , D \right) .$ However, unless $f$ is also
normal, the integral remains in the likelihood, which becomes difficult to compute,
particularly if the random effects structure is complicated.

A variety of approaches are available to approximating the likelihood using theoretical
or numerical methods. $A$ Bayesian approach is also possible. See Sinha (2004) for a
recent approach that also contains a survey of past approaches. We investigate the issues
through an example.

An experiment was conducted to study the effects of surface and vision on balance.
The balance of subjects were observed for two different surfaces and for restricted and
unrestricted vision. Balance was assessed qualitatively on an ordinal four-point scale
based on observation by the experimenter. Forty subjects were studied, twenty males and
twenty females ranging in age from 18 to 38, with heights given in cm and weights in kg.
The subjects were tested while standing on foam or a normal surface and with their eyes
closed or open or with a dome placed over their head. Each subject was tested twice in

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 222

each of the surface and eye combinations for a total of 12 measures per subject. The data
comes from Steele (1998) via the Australasian Data and Story Library (OzDASL).

For the purposes of this analysis, we will reduce the response to a two-point scale:
whether the subject was judged completely stable or not. We start by defining this
response:

\> data (ctsib)
> ctsib$stable <- ifelse (ctsib$CTSIB == 1,1,0)
> summary (ctsib)


<table>
<tr>
<th></th>
<th>Subject</th>
<th></th>
<th>Sex</th>
<th></th>
<th></th>
<th>Age</th>
<th></th>
<th>Height</th>
</tr>
<tr>
<td colspan="2">Weight</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Min.</td>
<td>:</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1.0</td>
<td>female:</td>
<td>240</td>
<td>Min.</td>
<td>:18.0</td>
<td></td>
<td>Min.</td>
<td>: 142</td>
<td>Min.</td>
</tr>
<tr>
<td colspan="2">: 44.2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1st Qu</td>
<td>.: 10.8</td>
<td>male</td>
<td>: 240</td>
<td>1st</td>
<td>Qu</td>
<td>.: 21.8</td>
<td>1st</td>
<td></td>
</tr>
<tr>
<td>Qu .: 167</td>
<td>1st</td>
<td>Qu .:</td>
<td>60.7</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Median</td>
<td>:20.5</td>
<td></td>
<td></td>
<td>Median</td>
<td></td>
<td>:25.5</td>
<td>Median</td>
<td></td>
</tr>
<tr>
<td>:173</td>
<td>Median</td>
<td>: 68.0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mean</td>
<td>:20.5</td>
<td></td>
<td></td>
<td>Mean</td>
<td></td>
<td>:26.8</td>
<td>Mean</td>
<td>: 172</td>
</tr>
<tr>
<td colspan="3">Mean : 71.1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">3rd Qu .: 30.3</td>
<td></td>
<td></td>
<td>3rd</td>
<td>Qu</td>
<td>.: 33.0</td>
<td>3rd</td>
<td></td>
</tr>
<tr>
<td>Qu .: 180</td>
<td>3rd</td>
<td>Qu .:</td>
<td>83.5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Max.</td>
<td>: 40.0</td>
<td></td>
<td></td>
<td>Max.</td>
<td></td>
<td>:38.0</td>
<td>Max.</td>
<td>:190</td>
</tr>
<tr>
<td>Max.</td>
<td colspan="2">: 102.0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


<table>
<tr>
<th>Surface</th>
<th>Vision</th>
<th>CTSIB</th>
<th>stable</th>
</tr>
<tr>
<td>foam: 240</td>
<td>$c l o s e d : 1 6 0$</td>
<td>Min. :1.00</td>
<td>Min. : 0.000</td>
</tr>
<tr>
<td>norm: 240</td>
<td>dome :160</td>
<td>1st Qu. : 2.00</td>
<td>1st Qu. : 0.000</td>
</tr>
<tr>
<td></td>
<td>open :160</td>
<td>Median :2.00</td>
<td>Median :0.000</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Mean :1.92</td>
<td>Mean :0.238</td>
</tr>
<tr>
<td></td>
<td></td>
<td>3rd Qu. : 2.00</td>
<td>3rd Qu .: 0.000</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Max. : 4.00</td>
<td>Max. :1.000</td>
</tr>
</table>


We could fit a binomial GLM ignoring the subject information entirely:

\> gf <- glm (stable
Sex+Age+Height+Weight+Surface+Vision, binomial, data=ctsi
b)
> summary (gf)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error z</th>
<th>value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>7.27745</td>
<td>3.80399</td>
<td>1.91</td>
<td>0.05573</td>
</tr>
<tr>
<td>Sexmale</td>
<td>1.40158</td>
<td>0.51623</td>
<td>2.72</td>
<td>0.00663</td>
</tr>
<tr>
<td>Age</td>
<td>0.00252</td>
<td>0.02431</td>
<td>0.10</td>
<td>0.91739</td>
</tr>
<tr>
<td>Height</td>
<td>-0.09641</td>
<td>0.02684</td>
<td>-3.59</td>
<td>0.00033</td>
</tr>
<tr>
<td>Weight</td>
<td>0.04350</td>
<td>0.01800</td>
<td>2.42</td>
<td>0.01567</td>
</tr>
<tr>
<td>Surfacenorm</td>
<td>3.96752</td>
<td>0.44718</td>
<td>8.87</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>Visiondome</td>
<td>0.36375</td>
<td>0.38322</td>
<td>0.95</td>
<td>0.34252</td>
</tr>
<tr>
<td>Visionopen</td>
<td>3.18750</td>
<td>0.41600</td>
<td>7.66</td>
<td>1.8e-14</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="223" -->
<!-- PageHeader="Mixed effect models for nonnormal responses" -->

However, there may be a significant subject effect. We could try including a fixed subject
factor:

\> gfs <- glm(stable
Sex+Age+Height+Weight+Surface+Vision+factor (Subject),
binomial, data=ctsib)
> anova (gf, gfs, test="Chi")
Analysis of Deviance Table


<table>
<tr>
<th></th>
<th>Resid. Df</th>
<th>Resid.</th>
<th>Dev</th>
<th>Df</th>
<th>Deviance P (&gt; | Chi|)</th>
</tr>
<tr>
<td>1</td>
<td>472</td>
<td></td>
<td>295</td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>437</td>
<td></td>
<td>121</td>
<td>35</td>
<td>174 2.5e-20</td>
</tr>
</table>


We see strong evidence for a significant subject effect. However, when we examine the
summary for this model, we see problems with identifiability and separability which
prompt the use of bias-reduced logistic regression, as described in Section 2.8:

\> library (brlr)
> modbr <- brlr (stable ~
Sex+Age+Height+Weight+Surface+Vision+
factor (Subject) , data=ctsib)
> summary (modbr)
Coefficients:


<table>
<tr>
<th></th>
<th>Value</th>
<th>Std. Error</th>
<th>t value</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-44.619</td>
<td>50.432</td>
<td>-0.885</td>
</tr>
<tr>
<td>$\mathrm { S e x m a l e }$</td>
<td>0.538</td>
<td>3.060</td>
<td>0.176</td>
</tr>
<tr>
<td>Age</td>
<td>-0.223</td>
<td>0.137</td>
<td>-1.625</td>
</tr>
<tr>
<td>Height</td>
<td>0.335</td>
<td>0.351</td>
<td>0.953</td>
</tr>
<tr>
<td>Weight</td>
<td>-0.255</td>
<td>0.186</td>
<td>-1.370</td>
</tr>
<tr>
<td>Surfacenorm</td>
<td>6.150</td>
<td>0.734</td>
<td>8.378</td>
</tr>
<tr>
<td>Visiondome</td>
<td>0.635</td>
<td>0.489</td>
<td>1.300</td>
</tr>
<tr>
<td>Visionopen</td>
<td>5.043</td>
<td>0.687</td>
<td>7.344</td>
</tr>
</table>


We find that the subject-specific variables, sex, age, height and weight, are no longer
significant. This is because these predictors are constant for a given subject. We cannot
completely unconfound these effects from the subject effects.

There are variety of ways of fitting GLMMs in R. We demonstrate the Penalized
Quasi-Likelihood method implemented in the MASS package:

\> library (MASS)
> gg <- glmmPQL (stable ^
Sex+Age+Height+Weight+Surface+Vision,
random="1 | Subject, family=binomial, data=ctsib)
> summary (gg)
Random effects:
Formula: "1 | Subject
(Intercept) Residual
StdDev:
3.0608 0.59062

Variance function:
Structure: fixed weights
Formula: ~ invwt

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 224" -->

Fixed effects: stable ~ Sex + Age + Height + Weight +
Surface + Vision


<table>
<tr>
<th></th>
<th>Value</th>
<th>Std. Error</th>
<th>DF</th>
<th>t-value</th>
<th>p-value</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>15.5716</td>
<td>13.4985</td>
<td>437</td>
<td>1.1536</td>
<td>0.2493</td>
</tr>
<tr>
<td>$\mathrm { S e x m a l } \mathrm { e }$</td>
<td>3.3554</td>
<td>1.7526</td>
<td>35</td>
<td>1.9145</td>
<td>0.0638</td>
</tr>
<tr>
<td>Age</td>
<td>-0.0066</td>
<td>0.0820</td>
<td>35</td>
<td>-0.0810</td>
<td>0.9359</td>
</tr>
<tr>
<td>Height</td>
<td>-0.1908</td>
<td>0.0920</td>
<td>35</td>
<td>-2.0736</td>
<td>0.0455</td>
</tr>
<tr>
<td>Weight</td>
<td>0.0695</td>
<td>0.0629</td>
<td>35</td>
<td>1.1051</td>
<td>0.2766</td>
</tr>
<tr>
<td>Surfacenorm</td>
<td>7.7241</td>
<td>0.5736</td>
<td>437</td>
<td>13.4666</td>
<td>0.0000</td>
</tr>
<tr>
<td>Visiondome</td>
<td>0.7265</td>
<td>0.3259</td>
<td>437</td>
<td>2.2289</td>
<td>0.0263</td>
</tr>
<tr>
<td>Visionopen</td>
<td>6.4853</td>
<td>0.5440</td>
<td>437</td>
<td>11.9220</td>
<td>0.0000</td>
</tr>
</table>


The fit falls somewhere between the two above from the point of view of effect
significance. Notice how there are more degrees of freedom for the experimental factors
which do vary within individuals. This is expected. Compared to the fixed effect subject
modeling, rather less of the variation is attributed to the GLMM. Here the SD for subjects
is 3.06 while the SD of the subject effects from the GLM is:

$$s d \left( c o e f \left( m o d b r \right) \left[ 9 : 4 3 \right] \right)$$
\>

[1] 4.4407

This model can also be fit using the lmer function from the Ime4 package. Estimation of
GLMMs is an active area of research and further study of the best methods of estimation
is necessary.


### 10.2 Generalized Estimating Equations

The advantage of the quasi-likelihood approach compared to GLMs was that we did not
need to specify the distribution of the response. We only needed to give the link function
and the variance. We can adapt this approach for repeated measures and/or longitudinal
studies. Let $Y _ { i }$ be a vector of random variables representing the responses on a given
individual and let $E Y _ { i } = \mu _ { i }$ which is then linked to the linear predictor $\eta = X \beta$ in some
appropriate way. Let:

var $Y _ { i } \equiv \mathrm { v a r } \left( Y _ { i } ; \beta , \alpha \right)$

where a represents parameters that model the correlation structure within individuals. The
parameters, $\beta ,$ may then be estimated setting the (multivariate) score function to zero and
solving:

$$\sum _ { i } \left( \frac { \partial \mu _ { i } } { \partial \beta } \right) ^ { T } \text { var } \left( Y _ { i } \right) ^ { - 1 } \left( Y _ { i } - \mu _ { i } \right) = 0$$

These equations can be regarded as the multivariate analogue of those used for the quasi-
likelihood models described in Section 7.4. Since var $Y$ also depends on $\alpha ,$ we substitute
any consistent estimate of a in this equation and still obtain an estimate as asymptotically

<!-- PageBreak -->

<!-- PageNumber="225" -->
<!-- PageHeader="Mixed effect models for nonnormal responses" -->

efficient as if a were known. A similar set of equations can be derived representing the
score with respect to $\alpha ,$ which may be similarly solved.

These are called generalized estimating equations (GEE). Note that no specification of
the distribution has been necessary which makes the fitting and specification much
simpler. The estimates of ß are consistent even if the variance is misspecified.

We reanalyze the stability dataset:

\> data (ctsib)
> ctsib$stable <- ifelse (ctsib$CTSIB==l, 1, 0)
> library (gee)
> gg <- gee (stable ~
Sex+Age+Height+Weight+Surface+Vision, id=Subject,
family=binomial, data=ctsib, corstr="exchangeable", scale.
fix=TRUE)

We have specified the same fixed effects as in the corresponding GLMM earlier. The
grouping variable is specified by the id argument. Only simple groups are allowed while
nested grouping variables cannot be accommodated easily in this function. We must
choose the correlation structure within each group. If we choose no correlation, then the
problem reduces to a standard GLM. Several choices are available. For this data, it seems
reasonable to assume that any pair of observations from the same subject have the same
correlation. This is known as an exchangeable correlation or equivalently, compound
symmetry. We have chosen to fix the scale parameter at the default value of 1 to ensure
maximum compatibility with the GLMM fit. Otherwise, there would not be a strong
reason to fix this. Let us now examine the output:

\> summary (gg)


<table>
<tr>
<td>Model :</td>
<td></td>
</tr>
<tr>
<td>Link:</td>
<td>Logit</td>
</tr>
<tr>
<td>Variance to Mean Relation:</td>
<td>Binomial</td>
</tr>
<tr>
<td>Correlation Structure:</td>
<td>Exchangeable</td>
</tr>
<tr>
<td>Coefficients:</td>
<td></td>
</tr>
</table>


<table>
<tr>
<td></td>
<td colspan="2">Estimate Naive S.E.</td>
<td colspan="2">Naive z Robust S.E.</td>
</tr>
<tr>
<td>Robust z</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>(Intercept)</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>8.602874</td>
<td>5.199006</td>
<td>1.65472</td>
<td>5.911263</td>
<td>1.45534</td>
</tr>
<tr>
<td>Sexmale</td>
<td>1.641080</td>
<td>0.701444</td>
<td>2.33957</td>
<td>0.902840 1</td>
</tr>
<tr>
<td>. 81769</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Age</td>
<td>-0.011842</td>
<td>0.033022</td>
<td>-0.35862</td>
<td>0.047986 -</td>
</tr>
<tr>
<td>0.24679</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Height</td>
<td>-0.102020</td>
<td>0.036315</td>
<td>-2.80933</td>
<td>0.042336 -</td>
</tr>
<tr>
<td>2.40976</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Weight</td>
<td>0.043655</td>
<td>0.024630</td>
<td>1.77242</td>
<td>0.033964 1</td>
</tr>
<tr>
<td>.28534</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5">Surfacenorm</td>
</tr>
<tr>
<td>3.917254</td>
<td>0.412501</td>
<td>9.49636</td>
<td>0.566333</td>
<td>6.91687</td>
</tr>
<tr>
<td>Visiondome</td>
<td>0.358961</td>
<td>0.335804</td>
<td>1.06896</td>
<td>0.404175 0</td>
</tr>
<tr>
<td>. 88813</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Visionopen</td>
<td>3.180126</td>
<td>0.377109</td>
<td>8.43292</td>
<td>0.460365 6</td>
</tr>
<tr>
<td>. 90783</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 226" -->

Estimated Scale Parameter: 1
Number of Iterations: 4
Working Correlation


<table>
<tr>
<th>[,1]</th>
<th>[,2]</th>
<th>[,3]</th>
<th>$\left[ , 4 \right]$</th>
<th>$\left[ , 5 \right]$</th>
<th>$\left[ , 6 \right]$</th>
</tr>
<tr>
<td>[,7]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>[1,] 1.00000</td>
<td>0.21389</td>
<td>0.21389</td>
<td>0.21389</td>
<td>0.21389</td>
<td>0.21389</td>
</tr>
<tr>
<td>0.21389</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>[2,] 0.21389</td>
<td>1.00000</td>
<td>0.21389</td>
<td>0.21389</td>
<td>0.21389</td>
<td>0.21389</td>
</tr>
<tr>
<td>0.21389</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>[3,] 0.21389</td>
<td>0.21389</td>
<td>1.00000</td>
<td>0.21389</td>
<td>0.21389</td>
<td>0.21389</td>
</tr>
<tr>
<td>0.21389</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>[4,] 0.21389</td>
<td>0.21389</td>
<td>0.21389</td>
<td>1.00000</td>
<td>0.21389</td>
<td>0.21389</td>
</tr>
<tr>
<td>0.21389</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


.. rest deleted ...

We can see from the working correlation that the estimated correlation between
observations on the same subject is 0.21. The naive standard errors are based on the
assumption that the proposed correlation structure is correct. However, GEE has the
property that even if this structure is incorrect, the fixed effect estimates are still
consistent. Nevertheless, the naive standard errors may be improved by the use of a
sandwich estimator. This gives us the robust standard errors given above. These are
typically, but not always, larger than the naive standard errors. The robust SEs should be
used in practice. We see from the robust z-statistics that the height, surface and vision
factors are significant. This corresponds to the result from GLMM.

There is one clear difference with the GLMM output: the estimates for the GLMM are
about half the size of the GLMM Bs. This is to be expected. GLMMs model the data at
the subject or individual level. The correlation between the measurements on the
individual is generated by the random effect. Thus the $\beta \mathrm { s }$ for the GLMM represent the
effect on an individual. A GEE models the data at the population level. The $\beta \mathrm { s }$ for a GEE
represent the effect of the predictors averaged across all individuals with the same
predictor values. GEEs do not use random effects but model the correlation at the
marginal or correlation level.

Let's consider another GEE example. We have data from a clinical trial of 59
epileptics. For a baseline, patients were observed for 8 weeks and the number of seizures
recorded. The patients were then randomized to treatment by the drug Progabide (31
patients) or to the placebo group (28 patients). They were observed for four 2-week
periods and the number of seizures recorded. The data have been ana-lyzed by many
authors including Thall and Vail (1990), Breslow and Clayton (1993) and Diggle,
Heagerty, Liang, and Zeger (2002). Does Progabide reduce the rate of seizures? Take a
look at the first two patients:

\> data (epilepsy)

\> epilepsy [1 : 10, ]


<table>
<tr>
<th></th>
<th>seizures</th>
<th>id</th>
<th>treat</th>
<th>expind</th>
<th>timeadj</th>
<th>age</th>
</tr>
<tr>
<td>1</td>
<td>11</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>8</td>
<td>31</td>
</tr>
<tr>
<td>2</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>31</td>
</tr>
<tr>
<td>3</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>31</td>
</tr>
<tr>
<td>4</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>31</td>
</tr>
<tr>
<td>5</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>31</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageNumber="227" -->
<!-- PageHeader="Mixed effect models for nonnormal responses" -->


<table>
<tr>
<td>6</td>
<td>11</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>8</td>
<td>30</td>
</tr>
<tr>
<td>7</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>30</td>
</tr>
<tr>
<td>8</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>30</td>
</tr>
<tr>
<td>9</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>30</td>
</tr>
<tr>
<td>10</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>30</td>
</tr>
</table>


Both were not treated (treat=0). The expind indicates the baseline period by 0 and the
treatment period by 1. The length of these time periods is recorded in timeadj. We now
compute the mean number of seizures per week broken down by the treatment and
baseline vs. experimental period:

$>$

with (epilepsy, by (seizures/timeadj, list (treat, expind) , me
an) )
: 0
: 0

[1] 3.8482
: 1
: 0

[1] 3.9556
: 0

: 1

[1] 4.3036
: 1
: 1

[1] 3.9839

We can tabulate this in Table 10.1.


<table>
<caption>Table 10.1 Seizures per week in epilepsy patients.</caption>
<tr>
<th></th>
<th>Baseline</th>
<th>Experiment</th>
</tr>
<tr>
<td>Placebo</td>
<td>3.85</td>
<td>4.30</td>
</tr>
<tr>
<td>Treatment</td>
<td>3.96</td>
<td>3.98</td>
</tr>
</table>


We see that the rate of seizures in the treatment group actually increases during the
period in which the drug was taken. The rate of seizures also increases even more in the
placebo group. Perhaps some other factor is causing the rate of seizures to increase
during the treatment period and the drug is actually having a beneficial effect. Now we
make some plots to show the difference between the treatment and the control. The first
plot shows the difference between the two groups during the experimental period only:

\> y <- matrix (epilepsy$seizures, nrow=5)
> matplot (1 : 4, sqrt (y [-
1,]),type="1",lty=epilepsy$treat[5*(1:59)]+1,
xlab="Period", ylab="Sqrt (Seizures) ")

<!-- PageBreak -->

<!-- PageNumber="228" -->
<!-- PageHeader="Extending the linear model with $\mathrm { R }$" -->


<figure>
<figcaption>Figure 10.1 Square root of seizures per 2-week period with treatment group shown as solid lines and the placebo group shown as dotted lines is shown in the plot on the left. The mean seizures per week is shown compared with the seizures per week during the baseline period is shown on the right where + indicates treated group.</figcaption>

10

6

\+

8

LO

Sqrt(Seizures)

sqrt(Experiment seizures)

"

A

A

9

1

3

\+

4

\+

4

4

2

A

\+

\+

2

\+

A

0

0

\+

1.0

2.0

3.0

4.0

1.0 2.0 3.0 4.0

Period

sqrt(Baseline seizures)

</figure>


We compare the two groups in the left panel of Figure 10.1 and find little to choose
between them. The square-root transform is used to stabilize the variance; this is often
used with count data. Now we compare the average seizure rate to the baseline for the
two groups:

$$> m y < - \quad a p p l y \left( y \left[ - 1 , \right] , 2 , m e a n \right) / 2$$

\> plot (sqrt (epilepsy$seizures [epilepsy$expind ==
0]/8) , sqrt (my) ,
pch=epilepsy$treat [5* (1:59) ] +2, xlab="sqrt (Baseline
seizures) ",

$$y l a b = { } ^ { \prime \prime } \mathrm { s q r t } \left( E x p e r i m e n t s e i z u r e s \right) ^ { \prime \prime }$$

\> abline (0,l)

A treatment effect, if one exists, is not readily apparent. Now we fit the GEE model. An
offset is necessary to account for the differing lengths of the baseline and treatment
periods being 8 and 2 weeks, respectively. Patient #49 is unusual because of the high rate
of seizures observed. We exclude this point. An AR(1) model for the correlation structure
is most natural since consecutive measurements will be more correlated than
measurements separated in time.

<!-- PageBreak -->

<!-- PageNumber="229" -->
<!-- PageHeader="Mixed effect models for nonnormal responses" -->

\> g <- gee (seizures
~offset (log (timeadj ) ) +expind+treat+I (expind*treat) ,
id, family=poisson, corstr="AR-
M", Mv=1, data=epilepsy, subset= (id != 49) )
> summary (g)
Coefficients:


<table>
<tr>
<th></th>
<th></th>
<th></th>
<th>Estimate</th>
<th>Naive</th>
<th>S.E.</th>
<th colspan="2">Naive z</th>
<th>Robust</th>
</tr>
<tr>
<td colspan="3">S.E. Robust z</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>(Intercept)</td>
<td></td>
<td></td>
<td>1.320377</td>
<td>0.10354</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>12.75176</td>
<td></td>
<td>0.16065</td>
<td>8.21872</td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr>
<td>expind</td>
<td></td>
<td></td>
<td>0.142777</td>
<td>0.13932</td>
<td></td>
<td colspan="2">1.02482</td>
<td>0.</td>
</tr>
<tr>
<td colspan="3">10769 1.32578</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>treat</td>
<td></td>
<td></td>
<td>-0.079402</td>
<td>0.14682</td>
<td>-</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>0.54083</td>
<td></td>
<td>0.19716</td>
<td>-0.40273</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>I (expind</td>
<td colspan="3">* treat) -0.377546</td>
<td>0.21774</td>
<td>-</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1.73396</td>
<td></td>
<td>0.16839</td>
<td>-2.24210</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">Estimated Scale</td>
<td>Parameter:</td>
<td>10.687</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Number of</td>
<td></td>
<td>Iterations:</td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3">Working Correlation</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>[,1]</td>
<td>[,2]</td>
<td>[,3]</td>
<td>[,4]</td>
<td></td>
<td>[,5]</td>
<td></td>
<td></td>
</tr>
<tr>
<td>[1] 1.00000</td>
<td></td>
<td>0.61854</td>
<td>0.38259</td>
<td>0.23665</td>
<td>0.14637</td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>[2,] 0.61854</td>
<td></td>
<td>1.00000</td>
<td>0.61854</td>
<td>0.38259</td>
<td>0.23665</td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>[3,] 1 0.38259</td>
<td></td>
<td>0.61854</td>
<td>1.00000</td>
<td>0.61854</td>
<td>0.38259</td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>[4,] 0.23665</td>
<td></td>
<td>0.38259</td>
<td>0.61854</td>
<td>1.00000</td>
<td>0.61854</td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>[5,] 0.14637</td>
<td></td>
<td>0.23665</td>
<td>0.38259</td>
<td>0.61854</td>
<td>1.00000</td>
<td colspan="2"></td>
<td></td>
</tr>
</table>


The drug does barely have a significant effect. The dispersion parameter is estimated as
10.687. This means that if we did not account for the overdispersion, the standard errors
would be much larger. The AR(1) correlation structure can be seen in the working
correlation where adjacent measurements have 0.62 correlation.

Further analysis would involve an investigation of alternative correlation structures,
the age covariate and any trend during the experimental period. The analysis of this
dataset is discussed in Diggle, Heagerty, Liang, and Zeger (2002).

Further Reading: McCulloch and Searle (2002) have some coverage of GLMMs as
well as more material on GLMs. Hardin and Hilbe (2003) give a book-length treatment of
GEEs. Diggle, Heagerty, Liang, and Zeger (2002) discuss both topics.


#### Exercises

1\. The ohio data concern 536 children from Steubenville, Ohio and were taken as part of
a study on the effects of air pollution. Children were in the study for four years from
age seven to ten. The response was whether they wheezed or not. The variables are:

resp an indicator of wheeze status $\left( 1 = y e s , 0 = n o \right)$
id an identifier for the child
age 7 yrs =- 2, 8 yrs =- 1, $9 \quad y r s = 0 ,$ $1 0 \quad y r s = 1$
smoke an indicator of maternal smoking at the first year of the study $\left( 1 = \mathrm { s m o k e r } \right. ,$
$\left. 0 = n o n s m o k e r \right)$

(a) Fit an appropriate GEE model and determine the effects of age and maternal
smoking on wheezing.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 230" -->

(b) In your model, what indicates that a child who already wheezes is likely to
continue to wheeze?

(c) What is the predicted probability that a 7 year-old with a smoking mother,
wheezes?

(d) Repeat your analysis using a GLM where you assume that the observations are
independent, that is, each single response value represents a different child.
Indicate how the conclusions would differ and which results should be preferred.

(e) Sum the number of times wheezing is recorded for a child over the four
measurements and model this as a function of the smoking status of the mother.
This can be achieved as follows:

\> nohio <- reshape (ohio, idvar ="id", direction="wide",
timevar="age", v. names="resp")
> nohio <- data. frame (smoke=nohio$smoke,
wheeze=apply (nohio [ , 3 : 6] , 1, sum) )

Now determine the effect of smoking. Compare this result to the previous analyses and
discuss which is preferable.

2\. The National Youth Survey collected a sample of 11-17 year-olds, 117 boys and 120
girls, asking questions about marijuana usage. The data is presented in potuse.

(a) Condense the levels of the response into whether the person did or did not use
marijuana that year. Build a model for marijuana usage over the time period that
takes account of sex differences.

(b) In your model, what describes correlation between marijuana usage one year and
the next for a particular individual?

(c) What is the difference between boys and girls?

(d) Compute the predicted probability of usage by boys over time.

(e) Can you model the original three-level response in R?

3\. Components are attached to an electronic circuit card assembly by a wave-soldering
process. The soldering process involves baking and preheating the circuit card and
then passing it through a solder wave by conveyor. Defects arise during the process.
The design is $2 ^ { 7 - 3 }$ with three replicates and the data is found in wave solder. Assuming
that the responses for each run are in time order, analyze the data. Is there any
evidence of an effect due to the time order?

4\. The nitrofen data in boot package come from an experiment to measure the
reproductive toxicity of the pesticide nitrofen on a species of zooplankton called
Ceriodaphnia dubia. Each animal produced three broods in which the number of live
offspring was recorded. Fifty animals in total were used and divided into five batches.
Each batch was treated in a solution with a different concentration of the pesticide.
Build a model for the number of live offspring produced in the successive broods.
Your model should describe how this number changes and is related within a
given animal and how this relates to the concentration of pesticide.

5\. The toenail data comes from a multicenter study comparing two oral treatments for
toenail infection. Patients were evaluated for the degree of separation of the nail.

<!-- PageBreak -->

<!-- PageNumber="231" -->
<!-- PageHeader="Mixed effect models for nonnormal responses" -->

Patients were randomized into two treatments and were followed over seven visits:
four in the first year and yearly thereafter. The patients have not been treated prior to
the first visit so this should be regarded as the baseline.

Analyze the data to determine the difference between the two treatments and the
progression of the infection over time.

<!-- PageBreak -->


## CHAPTER 11 Nonparametric Regression

The generalized linear model was an extension of the linear model $y = X \beta + 8$ to allow the
responses $y$ from the exponential family. The mixed effect models allowed for a much
more general treatment of &. We now switch our attention to the linear predictor $\eta = X \beta .$
We want to make this more flexible. There are a wide variety of available methods, but it
is best to start with simple regression. The methods developed here form part of the
solution to the multiple predictor problem.

We start with a simple regression problem. Given fixed $x _ { 1 } , \ldots , x _ { n } ,$ we observe $y _ { 1 } , \ldots , y _ { n }$
where:

$$y _ { i } = f \left( x _ { i } \right) + c _ { i }$$

where the $\&$ are $i . i . d .$ and have mean zero and unknown variance $\sigma ^ { 2 } .$ The problem is to
estimate the function $f .$

A parametric approach is to assume that $f \left( x \right)$ belong to a parametric family of
functions: $f \left( x | \beta \right) .$ So $\mathrm { f }$ is known up to a finite number of parameters. Some examples are:

$f \left( x | \beta \right) = \beta _ { 0 } + \beta _ { 1 } x$

$$f \left( x | \beta \right) = \beta _ { 0 } + \beta _ { 1 } x + \beta _ { 2 } x ^ { 2 }$$
$$f \left( x | \beta \right) = \beta _ { 0 } + \beta _ { 1 } x ^ { \beta 2 }$$

The parametric approach is quite flexible because we are not constrained to just linear
predictors as in the first model of the three above. We can add many different types of
terms such as polynomials and other functions of the variable to achieve flexible fits.
Nonlinear models, such as the third case above, are also parametric in nature.
Nevertheless, no matter what finite parametric family we specify, it will always exclude
many plausible functions.

The nonparametric approach is to choose $f$ from some smooth family of functions.
Thus the range of potential fits to the data is much larger than the parametric approach.
We do need to make some assumptions about f-that it has some degree of smoothness
and continuity, for example, but these restrictions are far less limiting than the parametric
way.

The parametric approach has the advantage that it is more efficient if the model is
correct. If you have good information about the appropriate model family, you should
prefer a parametric model. Parameters may also have intuitive interpretations.
Nonparametric models do not have a formulaic way of describing the relationship
between the predictors and the response; this often needs to be done graphically. This
relates to another advantage of parametric models in that they reduce information
necessary for prediction; you can write down the model formula, typically in a com-pact
form. Nonparametric models are less easily communicated on paper. Parametric models
also enable easy utilization of past experience.

<!-- PageBreak -->

<!-- PageNumber="233" -->
<!-- PageHeader="Nonparametric regression" -->

The nonparametric approach is more flexible. In modeling new data, one often has
very little idea of an appropriate form for the model. We do have a number of heuristic
tools using diagnostic plots to help search for this form, but it would be easier to let the
modeling approach take care of this search. Another disadvantage of the parametric
approach is that one can easily choose the wrong form for the model and this results in
bias. The nonparametric approach assumes far less and so is less liable to make bad
mistakes. The nonparametric approach is particularly useful when little past experience is
available

For our examples we will use three datasets, one real (data on Old Faithful) and two
simulated, called exa and exb. The data comes from Härdle (1991). The reason we use
simulated data is to see how well the estimates match the true function (which cannot
usually be known for real data). We plot the data in the first three panels of Figure 11.1,
using a line to mark the true function where known. For exa, the true function is
$f \left( x \right) = \sin ^ { 3 } \left( 2 \pi x ^ { 3 } \right) .$ For exb, it is constant zero, that is, $f \left( x \right) = 0 :$

\> data (exa)

\> plot (y ~x, exa, main="Example A", pch=" . ")
> lines (m ~ x, exa)
> data (exb)

\> plot (y ~ x, exb, main="Example B", pch=".")
> lines (m ~ x, exb)
> data (faithful)
> plot (waiting ~duration, faithful, main="old
Faithful", pch=". ")

We now examine several widely used nonparametic regression estimators, also known as
smoothers.


<figure>
<figcaption>Figure 11.1 Data examples. Example A has varying amounts of curvature, two optima and a point of inflexion. Example $B$ has two outliers. The Old Faithful provides the challenges of real data.</figcaption>

Example A

Example $B$

Old Faithful

2

₿
0.0 0.5 1.0 1.5

8 10

5

B

5

5

waiting

4

49

₪

.

6

0.0 0.2 0.4 00 0.0 1.0

0.0

0.2

0.4

0.6

0.0

1.0

1.5 25 3.5 4:

\*

$x$

duration

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 234" -->


### 11.1 Kernel Estimators

In its simplest form, this is just a moving average estimator. More generally, our estimate
$\mathrm { o f } f ,$ called $\int _ { 2 } ^ { 2 } \left( x \right) :$

$$w _ { j } = K \left( \frac { x - x _ { j } } { A } \right) / \lambda$$
$\widehat { f } _ { \lambda } \left( x \right) = \frac { 1 } { m } \sum _ { j = 1 } ^ { n } K \left( \frac { x - x _ { j } } { \lambda } \right) Y _ { j } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } w _ { j } Y _ { j } ,$ where

$K$ is a kernel where $\int K = 1 .$ The moving average kernel is rectangular, but smoother
kernels can give better results, $\widehat { A }$ is called the bandwidth, window width or smoothing
parameter. It controls the smoothness of the fitted curve.

If the xs are spaced very unevenly, then this estimator can give poor results. This
problem is somewhat ameliorated by the Nadaraya-Watson estimator:

$$f _ { A } \left( x \right) = \frac { \sum _ { j = 1 } ^ { n } w _ { j } Y _ { j } } { \sum _ { j = 1 } ^ { n } w _ { j } }$$

We see that this estimator simply modifies the moving average estimator so that it is a
true weighted average where the weights for each $y$ will sum to one.

It is worth understanding the basic asymptotics of kernel estimators. The optimal
choice of 2, gives:

$$M S E \left( x \right) = E \left( f \left( x \right) - A _ { A } \left( x \right) \right) ^ { 2 } = O \left( n ^ { - 4 / 5 } \right)$$

MSE stands for mean squared error and we see that this decreases at a rate propor-tional
to $n ^ { - 4 / 5 }$ with the sample size. Compare this to the typical parametric estimator where
$\mathrm { M S E } \left( x \right) = O \left( n ^ { - 1 } \right) ,$ but this only holds when the parametric model is correct. So the kernel
estimator is less efficient. Indeed, the relative difference between the MSEs becomes
substantial as the sample size increases. However, if the parametric model is incorrect,
the MSE will be $O \left( 1 \right)$ and the fit will not improve past a cer-tain point even with
unlimited data. The advantage of the nonparametic approach is the protection against
model specification error. Without assuming much stronger restrictions on $f ,$
nonparametric estimators cannot do better than $O \left( n ^ { - 4 / 5 } \right) .$

The implementation of a kernel estimator requires two choices: the kernel and the
smoothing parameter. For the choice of kernel, smoothness and compactness are
desirable. We prefer smoothness to ensure that the resulting estimator is smooth, so for
example, the uniform kernel will give stepped-looking fit that we may wish to avoid. We
also prefer a compact kernel because this ensures that only data, local to the point at
which $f$ is estimated, is used in the fit. This means that the Gaussian kernel is less
desirable, because although it is light in the tails, it is not zero, meaning in principle that
the contribution of every point to the fit must be computed. The optimal choice under
some standard assumptions is the Epanechnikov kernel:

$$K \left( x \right) = \left\{ \begin{array}{} { \frac { 3 } { 4 } \left( 1 - x ^ { 2 } \right) } & { | x | < 1 } \\ { 0 } & { \text { otherwise } } \end{array} \right.$$

<!-- PageBreak -->

<!-- PageNumber="235" -->
<!-- PageHeader="Nonparametric regression" -->

This kernel has the advantage of some smoothness, compactness and rapid computa-tion.
This latter feature is important for larger datasets, particularly when resampling
techniques like bootstrap are being used. Even so, any sensible choice of kernel will
produce acceptable results, so the choice is not crucially important.

The choice of smoothing parameter $\lambda$ is critical to the performance of the estimator
and far more important than the choice of kernel. If the smoothing parameter is too small,
the estimator will be too rough; but if it is too large, important features will be smoothed
out.

We demonstrate the Nadaraya-Watson estimator next for a variety of choices of
bandwidth on the Old Faithful data shown in Figure 11.2. We use the ksmooth function
which is part of the $R$ base package. This function lacks many useful features that can be
found in some other packages, but it is adequate for simple use. The default uses a
uniform kernel, which is somewhat rough. We have changed this to the normal kernel:

\> plot (waiting ~duration,
faithful, main="bandwidth=0.1", pch=".")
>
lines (ksmooth (faithful$duration, faithful$waiting, "norma
l",0.1))

\> plot (waiting ~duration,
faithful, main="bandwidth=0. 5", pch=".")
>
lines (ksmooth (faithful$duration, faithful$waiting, "norma
l",0.5))

\> plot (waiting ~duration,
faithful, main="bandwidth=2", pch=".")
>
lines (ksmooth (faithful$duration, faithful$waiting, "norma
1", 2) )


<figure>
<figcaption>Figure 11.2 Nadaraya-Watson kernel smoother with a normal kernel for three different bandwidths on the Old Faithful data.</figcaption>

$b a n d w i d t h = 0 . 1$

$b a n d w i d t h = 0 . 5$

$b a n d w i d t h = 2$

90

90

90

80

80

80

waiting

70

waiting

70

waiting

70

3

00

S

50

50

8

1.5 2.5 3.5 4.5

1.5

2.5

3.5

4.5

1.5 2.5 3.5 42

4.5

duration

duration

duration

</figure>


<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 236" -->

The central plot in Figure 11.2 is the best choice of the three. Since we do not know the
true function relating waiting time and duration, we can only speculate, but it does seem
reasonable to expect that this function is quite smooth. The fit on the left does not seem
plausible since we would not expect the mean waiting time to vary so much as a function
of duration. On the other hand, the plot on the right is even smoother than the plot in the
middle. It is not so easy to choose between these. Another consideration is that the eye
can always visualize additional smoothing, but it is not so easy to imagine what a less
smooth fit might look like. For this reason, we recommend picking the least smooth fit
that does not show any implausible fluctuations. Of the three plots shown, the middle plot
seems best. Smoothers are often used as a graphical aid in interpreting the relationship
between variables. In such cases, visual selection of the amount of smoothing is effective
because the user can employ background knowledge to make an appropriate choice and
avoid serious mistakes.

You can choose $\lambda$ interactively using this subjective method. Plot $f _ { A } \left( x \right)$ a range of
different $\lambda$ and pick the one that looks best as we have done above. You may need to
iterate the choice of $\lambda$ to focus your decision. Knowledge about what the true relationship
might look like can be readily employed.

In cases where the fitted curve will be used to make numerical predictions of future
values, the choice of the amount of smoothing has an immediate effect on the outcome.
Even here subjective methods may be used. If this method of selecting the amount of
smoothing seems disturbingly subjective, we should also understand that the selection of
a family of parametric models for the same data would also involve a great deal of
subjective choice although this is often not explicitly recognized. Statistical modeling
requires us to use our knowledge of what general forms of relationship might be
reasonable. It is not possible to determine these forms from the data in an entirely
objective manner. Whichever methodology you use, some subjective decisions will be
necessary. It is best to accept this and be honest about what these decisions are.

Even so, automatic methods for selecting the amount of smoothing are also useful.
Selecting the amount of smoothing using subjective methods requires time and effort.
When a large number of smooths are necessary, some automation is desirable. In other
cases, the statistician will want to avoid the explicit appearance of subjectivity in the
choice. Cross-validation (CV) is a popular general-purpose method. The criterion is:

$$C V \left( \lambda \right) = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left( y _ { j } - \widehat { f } _ { \lambda \left( j \right) } \left( x _ { j } \right) \right) ^ { 2 }$$

where (j) indicates that point $j$ is left out of the fit. We pick the $\lambda$ that minimizes this
criterion. True cross-validation is computationally expensive, so an approximation to it,
known as generalized cross-validation or GCV, is sometimes used. There are also many
other methods of automatically selecting the $\lambda .$

Our practical experience has been that automatic methods, such as $\mathrm { C V } ,$ often work
well, but sometimes produce estimates that are clearly at odds with the amount of
smoothing that contextual knowledge would suggest. For this reason, we are unwilling to
trust automatic methods completely We recommend using them as a starting point for a
possible interactive exploration of the appropriate amount of smoothing if time permits.

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression" -->
<!-- PageNumber="237" -->

They are also useful when a very large numbers of smooths are needed such as in the
additive modeling approach described in Chapter 12.

When smoothing is used to determine whether f has certain features such as multiple
maximums (called bump hunting) or monotonicity, special methods are necessary to
choose the amount of smoothing since this choice will determine the outcome of the
investigation.

The sm library, described in Bowman and Azzalini (1997), allows the computation of
the cross-validated choice of bandwidth. For example, we find the $C V$ choice of
bandwidth for the Old Faithful and plot the result:

\> library (sm)
> hm <-

hcv (faithful$duration, faithful$waiting, display="lines")
\>
sm. regression (faithful$duration, faithful$waiting, $h = h m ,$
xlab="duration", ylab="waiting")


<figure>
<figcaption>Figure 11.3 The cross-validation criterion shown as a function of the smoothing parameter is shown in the first panel. The minimum occurs at $a$ value of 0.424. The second panel shows the kernel estimate with this value of the smoothing parameter.</figcaption>

15000

90

13000

80

CV

waiting

70

11000

60

9000

50

0.2

0.4

0.6

0.8

1.5

2.5

3.5

4.5

$h$

duration

</figure>


We see the criterion plotted in the first panel of Figure 11.3. Notice that the function is
quite flat in the region of the minimum indicating that a wide range of choices will
produce acceptable results. The resulting choice of fit is shown in the second panel of the
figure. The sm package uses a Gaussian kernel where the smoothing parameter is the
standard deviation of the kernel.

We repeat the exercise for Example $\mathrm { A }$ the plots are shown in Figure 11.4:

$$> \mathrm { h m } < - \mathrm { h c v } \left( \mathrm { e x a } \mathrm { s } _ { \mathrm { X } _ { \prime } } \mathrm { e x a } \mathrm { s } _ { \mathrm { Y } } , \mathrm { d i s p } \mathrm { l a y } = { } ^ { \mathrm { n } } \mathrm { l } \mathrm { i n e s } ^ { \prime \prime } \right)$$

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 238

$$> \text { sm. regress ion } \left( \in \times a \stackrel { \text { s } } { \mapsto } x , \text { exa } \stackrel { s } { \leftrightarrow } y _ { \prime } = h m _ { r } \times \text { lab } = ^ { \prime \prime } x ^ { \prime } , y ^ { \prime } \text { ab } = ^ { \prime \prime } y ^ { \prime \prime } \right.$$


### For Example B:

\> hm <- hcv (exb$x, exb$y, display="lines")
hcv: boundary of search area reached.
Try readjusting hstart and hend.
hstart: 0.014122
hend : 0.28244


<table>
<tr>
<th></th>
<th>h</th>
<th>CV</th>
</tr>
<tr>
<td>[1,]</td>
<td>0.014122</td>
<td>171.47</td>
</tr>
<tr>
<td>[2,]</td>
<td>0.021665</td>
<td>190.99</td>
</tr>
<tr>
<td>[3,]</td>
<td>0.033237</td>
<td>219.87</td>
</tr>
<tr>
<td>[4]</td>
<td>0.050990</td>
<td>242.99</td>
</tr>
<tr>
<td>[5,]</td>
<td>0.078226</td>
<td></td>
</tr>
<tr>
<td>[6,]</td>
<td>0.120008</td>
<td></td>
</tr>
<tr>
<td>[7,]</td>
<td></td>
<td></td>
</tr>
<tr>
<td>[8,]</td>
<td>0.282445</td>
<td>288.48</td>
</tr>
</table>


we find that the $\mathrm { C V }$ choice is at the lower boundary of suggested bandwidths. We can
look at a smaller range:


<figure>
<figcaption>Figure 11.4 Cross-validation selection of smoothing for Example A. The cross-validation criterion is shown on left the minimum is at $h = 0 . 0 2 2 .$ The fit from this choice of $h$ is shown on the right.</figcaption>

55

\-
0.0 0.5 1.0 1.5

50

45

0

CV

40

y

35

30

-1.0

25

0.05 0.10 0.15 0.20

0.0 0.2 0.4 0.6 0.8 1.0

h

$x$

</figure>


\> hm <- hcv (exb$x, exb$y, display="lines", hstart=0.005)

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression 239" -->

However, bandwidths this small represent windows that include only a single point,
making cross-validation impractical. Choosing such a small bandwidth as in:

\>
$$\mathrm { s m } . \mathrm { r e g r e s s i o n } \left( \mathrm { e x b } \stackrel { \mathrm { d } } { \mathrm { e } } \mathrm { x } , \mathrm { e x b } \stackrel { \mathrm { e } } { \mathrm { e } } \mathrm { y } , \mathrm { h } = 0 . 0 0 5 \right)$$

gives us a dramatic undersmooth because the regression exactly fits the data.

$$1 1 . 2 \quad S p l i n e s$$

Smoothing Splines: The model is $y _ { i } = f \left( x _ { i } \right) + c _ { i } ,$ so in the spirit of least squares, we might
choose $\ddot { f }$ to minimize the MSE: $\frac { 1 } { n } \sum \left( y _ { i } - f \left( x _ { i } \right) \right) ^ { 2 }$ solution is $f \left( x _ { i } \right) = y _ { i \cdot T h i s }$ is a
"join $\overrightarrow { f }$ the dots" regression that is almost certainly too rough. Instead, suppose we choose
☒
to minimize a modified least squares criterion:

$$\frac { 1 } { n } \sum \left( Y _ { i } - f \left( x _ { i } \right) \right) ^ { 2 } + \lambda \int \left[ f ^ { \prime \prime } \left( x \right) \right] ^ { 2 } d x$$

where $\lambda > 0$ is the smoothing parameter and $\int \left[ f ^ { \prime \prime } \left( x \right) \right] ^ { 2 } d x$ is a roughness penalty. When $f$ is
rough, the penalty is large, but when $f$ is smooth, the penalty is small. Thus the two parts
of the criterion balance fit against smoothness. This is the smoothing spline fit.

For this choice of roughness penalty, the solution is of a particular form: $\ddot { f }$ a cubic
spline. This means that $\ddot { f }$ a piecewise cubic polynomial in each interval $\left( x _ { i } , x _ { i } + 1 \right)$
(assuming that the $x _ { i }$ are sorted). It has the property that $\ddot { f } ,$ fand $\mathrm { f } ^ { \prime }$ $\widetilde { f } ^ { \prime \prime }$ continuous.
Given that we know the form of the solution, the estimation is reduced to the parametric
problem of estimating the coefficients of the polynomials. This can be done in a
numerically efficient way.

Several variations on the basic theme are possible. Other choices of roughness penalty
can be considered, where penalties on higher-order derivatives lead to fits with more
continuous derivatives. We can also use weights by inserting them in the sum of squares
part of the criterion. This feature is useful when smoothing splines are means to an end
for some larger procedure that requires weighting. A robust version can be developed by
modifying the sum of squares criterion to:

$$\sum p \left( y _ { i } - f \left( x _ { i } \right) \right) + 2 \int \left[ f ^ { \prime \prime } \left( x \right) \right] ^ { 2 } d x$$

where $p \left( x \right) = | x |$ is one possible choice.

In $\mathrm { R } ,$ cross-validation is used to select the smoothing parameter by default. We show
this default choice of smoothing for our three test cases:

lines (smooth. spline (faithful$duration, faithful$waiting)
)
\> plot (y ~ x, exa, pch=".")
> plot (waiting ~ duration, faithful, pch=".")
>

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 240" -->

\> lines (exa$x, exa$m)
> lines(smooth.spline(exa$x,exa$y),lty=2)
> plot (y "x, exb, pch=".")
> lines (exb$x, exb$m)
> lines (smooth. spline (exb$x, $\left. e x b y \right)$ , $\left. 1 t y = 2 \right)$


<figure>
<figcaption>Figure 11.5 Smoothing spline fits. For Examples A and $B ,$ the true function is shown as solid and the spline fit as dotted.</figcaption>

8

7-

50

A

1.5

25

35

45 00 02 04 00 00 10 00 02 04 06 00
I

1.0

duration

1

</figure>


The fits may be seen in Figure 11.5. The fit for the Old Faithful data looks reasonable.
The fit for Example A does a good job of tracking the hills and valleys but overfits in the
smoother region. The default choice of smoothing parameter given by $\mathrm { C V }$ is a disaster for
Example $\mathrm { B }$ as the data is just interpolated. This illustrates the danger of blindly relying on
automatic bandwidth selection methods.

Regression Splines: Regression splines differ from smoothing splines in the fol-
lowing way: For regression splines, the knots of the B-splines used for the basis are
typically much smaller in number than the sample size. The number of knots chosen
controls the amount of smoothing. For smoothing splines, the observed unique $x$ values
are the knots and $\lambda$ is used to control the smoothing. It is arguable whether the regression
spline method is parametric or nonparametric, because once the knots are chosen, a
parametric family has been specified with a finite number of parameters. It is the freedom
to choose the number of knots that makes the method nonparametric. One of the desirable
characteristics of a nonparametric regression estimator is that it should be consistent for
smooth functions. This can be achieved for regression splines if the number of knots is
allowed to increase at an appropriate rate with the sample size.

We demonstrate some regression splines here. We use piecewise linear splines in this
example, which are constructed and plotted as follows:

$$> \mathrm { r h s } < - \mathrm { f u n c t i o n } \left( \mathrm { x } _ { \prime } \mathrm { c } \right) \mathrm { i f } \mathrm { e l s e } \left( \mathrm { x } > c _ { \prime } \mathrm { x - c } _ { \prime } 0 \right)$$

\> curve (rhs (x,0.5), 0,1)

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression 241" -->

where the spline is shown in the first panel of Figure 11.6. Now we define some knots for
Example A:

\> knots <- 0:9/10
> knots

[1] 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9

and compute a design matrix of splines with knots at these points for each x:

$$> \mathrm { d m } < - \mathrm { o u t e r } \left( \mathrm { e x a } \widehat { \varphi } \mathrm { x } _ { \prime } \mathrm { k n o t s } _ { \prime } \mathrm { r h s } \right)$$

\> matplot(exa$x,dm,type="l",col=l)

where the basis functions are shown in the second panel of Figure 11.6. Now we


<figure>
<figcaption>Figure 11.6 One basis function for linear regression splines shown on the left and the complete set shown on the right.</figcaption>

0.5

1.0

0.4

0.8

0.5) $\frac { x } { 2 } .$

----------------------------

0.3

0.6

dm

0.2

0.4

0.1

0.2

0.0

0.0

0.0

0.2

0.4

0.6

0.8

1.0

.0 0.2 0.4 0.6 0.8 1.0

$x$

exa$x

</figure>


compute and display the regression fit:

\> g <- lm(exa$y ~ dm)
> plot (y ~ x, exa, pch=" . ", xlab="x", ylab="y")
> lines (exa$x, predict (g) )

where the plot is shown in the first panel of Figure 11.7. Because the basis functions are
piecewise linear, the fit is also piecewise linear. A better fit may be obtained by adjusting
the knots so that they are denser in regions of greater curvature:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 242" -->

\> newknots <-
c (0, 0.5, 0. 6, 0. 65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95)
> dmn <- outer (exa$x, newknots, rhs)
> gn <- lm(exa$y ~ dmn)
> plot (y "x, exa, pch=" . ", xlab="x", ylab="y")
> lines (exa$x, predict (gn) )

where the plot is shown in the second panel of Figure 11.7. We obtain a better fit


<figure>
<figcaption>Figure 11.7 Evenly spaced knots $\widehat { J } \widehat { l } t$ shown on the left and knots spread relative to the curvature on the right.</figcaption>

1.5

1.5

1.0

1.0

0.5

0.5

y

0.0

y

0.0

-1.0

-1.0

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

$x$

$x$

</figure>


but only by using our knowledge of the true curvature. This knowledge would not be
available for real data, so more practical methods place the knots adaptive according to
the estimated curvature.

One can achieve a smoother fit by using higher-order splines. The bs () function can
be used to generate the appropriate spline basis. The default is cubic B-splines. We
display 12 cubic B-splines evenly spaced on the [0, 1] interval. The splines close to the
boundary take a different form as seen in the first panel of Figure 11.8:

\> library (splines)
>

matplot (bs (seq(0,1,length=1000) , df=12) , type="1", ylab=""
, col=1)

We can now use least squares to determine the coefficients. We then display the fit as
seen in the second panel of Figure 11.8:

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression 243" -->


<figure>
<figcaption>Figure 11.8 A cubic B-spline basis is shown in the left panel and the resulting fit to the Exam-ple A data is shown in the right panel.</figcaption>

0.0 0.2 0.4 0.6 0.8 1.0

1.0

y

0.0

-1.0

0

200

400

600

800

1000

10.0 0.2 0.4 0.6 0.8 1.

$x$

</figure>


\> sml <- 1m(y ~bs (x,12) , exa)
> plot (y "x, exa, pch=".")
> lines (m ~ x, exa)
> lines (predict (sml) ~x, exa, lty=2)

We see a smooth fit, but again we could do better by placing more knots at the points of
high curvature and fewer in the flatter regions.


### 11.3 Local Polynomials

Both the kernel and spline methods have been relatively vulnerable to outliers as seen by
their performance on Example B. The fits can be improved with some manual
intervention, either to remove the outliers or to increase the smoothing parameters.
However, smoothing is frequently just a small part of an analysis and so we might wish
to avoid giving each smooth individual attention. Furthermore, habitual removal of
outliers is an ad hoc strategy that is better replaced with a method that deals with long-
tailed errors gracefully. The local polynomial method combines robustness ideas from
linear regression and local fitting ideas from kernel methods.

First we select a window. We then fit a polynomial to the data in that window using
robust methods. The predicted response $\mathrm { a t }$ the middle of the window is the fitted value.
We then simply slide the window over the range of the data, repeating the fitting process
as the window moves. The most well-known implementation of this type of smoothing is
called lowess or loess and is due to Cleveland (1979).

As with any smoothing method, there are choices to be made. We need to choose the
order of the polynomial fit. A quadratic allows us to capture peaks and valleys in the
function. However, a linear term also performs well and is the default choice in the loess
function. As with most smoothers, it is important to pick the window width well. The

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 244" -->

default choice takes three quarters of the data and may not be a good choice as we shall
see below.

For the Old Faithful data, the default choice is satisfactory, as seen in the first panel of
Figure 11.9:

\> plot (waiting ~duration, faithful, pch=".")
> f <- loess (waiting ~duration, faithful)
> i <- order (faithful$duration)
> lines (f$x[i], f$fitted[i])

For Example $A ,$ the default choice is too large. The choice that minimizes the integrated
squared error between the estimated and true function requires a span (proportion of the
range) of 0.22. Both fits are seen in the middle panel of Figure 11.9:

$$> \mathrm { p l o t } \left( y ^ { \sim } x _ { \prime } \text { exa } _ { \prime } \text { pch= } ^ { \prime \prime } . ^ { \prime \prime } \right)$$
$$> l i n e s \left( e x a x , e x a m , l t y = 1 \right)$$

\> f <- loess (y ~x, exa)
> lines (f$x, f$fitted, lty=2)
> f <- loess (y ~x, exa, span=0.22)
> lines (f$x, f$fitted, lty=5)

In practice, the true function is, of course, unknown and we would need to select the span
ourselves, but this optimal choice does at least show how well loess can do in the best of
circumstances. The fit is similar to that for smoothing splines.

For Example $B ,$ the optimal choice of span is one (that is all the data). This is not
surprising since the true function is a constant and so maximal smoothing is desired. We
can see that the robust qualities of loess prevent the fit from becoming too distorted by
the two outliers even with the default choice of smoothing span:

\> plot (y ~ x, exb, pch=".")
> f <- loess (y "x, exb)
> lines (f$x, f$fitted, lty=2)

\> f <- loess (y ~ x, exb, span=1)
> lines (f$x, f$fitted, lty=5)
> lines (exb$x, exb$m)


### 11.4 Wavelets

Regression splines are an example of a basis function approach to fitting. $\mathrm { W } e$
approximate the curve by a family of basis functions, $\phi _ { i } \left( x \right)$ that $f \left( x \right) = \sum _ { i } c _ { i } \phi _ { i } \left( x \right) .$
Thus the fit requires estimating the coefficients, Ci. The choice of basis functions will
determine the properties of the fitted curve. The estimation of $\mathcal{C} _ { i }$ is particularly easy if the
basis functions are orthogonal.

Examples of orthogonal bases are orthogonal polynomials and the Fourier basis. The
disadvantage of both these families is that the basis functions are not compactly
supported so that the fit of each basis function depends on the whole data. This means

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression 245" -->

that these fits lack the desirable local fit properties that we have seen in previously
discussed smoothing methods. Although Fourier methods are popular for some
applications, they are not typically used for general-purpose smoothing.

Cubic B-splines are compactly supported, but they are not orthogonal. Wavelets have
the advantage that they are compactly supported and can be defined so as to possess the
orthogonality property. They also possess the multiresolution property


<figure>
<figcaption>Figure 11.9 Loess smoothing: Old Faithful data is shown in the left panel with the default amount of smoothing. Example A data is shown in the middle and $B$ in the right panel. The true function is shown as a solid line along with the default choice (dotted) and respective optimal amounts of smoothing (dashed) are also shown.</figcaption>

₪

8

0

0

8

0

M

CIACH

00

M

CA

D

0

2

15

45

0

0

05

0.4

0.5

1.0

0.0

2

0.4

0.0

1.0

duration

I

$\mathbb{K}$

</figure>


which allows them to fit the grosser features of the curve while focusing on the finer
detail where necessary.

We begin with the simplest type of wavelet: the Haar basis. The mother wavelet for
the Haar family is defined on the interval $\left[ 0 , 1 \right)$ as:

$$w \left( x \right) = \left\{ \begin{array}{} { 1 } & { x \leq 1 / 2 } \\ { - 1 } & { x > 1 / 2 } \end{array} \right.$$

We generate the members of family by dilating and translating this function. The next
two members of the family are defined on $\left[ 0 , 1 / 2 \right)$ and $\left[ 1 / 2 , 1 \right)$ by rescaling the mother
wavelet to these two intervals. The next four members are defined on the quarter intervals
in the same way. We can index the family members by $\mathrm { l e v e l } j$ and within the level by $k$ so
that each function will be defined on the interval $\left[ k / 2 ^ { j } , \left( k + 1 \right) / 2 ^ { j } \right)$ and takes the form:

$h _ { n } \left( x \right) = 2 ^ { j / 2 } w \left( 2 ^ { j } x - k \right)$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 246" -->

where $n = 2 ^ { j } + k$ and $0 \leq k \leq 2 ^ { j } .$ We can see by simply plotting these functions that they are
orthogonal. There are also orthonormal, because they integrate to 1. Furthermore, they
have a local basis where the support becomes narrower as the level is increased.
Computing the coefficients is particularly quick because of these properties.

Wavelet fitting can be implemented using the wavethresh package. The first step is to
make the wavelet decomposition. We will illustrate this with Example $A :$

\> library (wavethresh)

$$> \mathrm { w d s } < - \mathrm { w d } \left( \mathrm { e x a } \mathrm { S y } _ { \prime } , \mathrm { f i l t e r } . \mathrm { n u m b e r } = \mathrm { l } \right)$$

The filter number specifies the complexity of the family. The Haar basis is the sim-plest
available but is not the default choice. We can now show the mother wavelet and wavelet
coefficients:

\> draw (wds, main="")
> plot (wds, main="")


<figure>
<figcaption>Figure 11.10 Haar mother wavelet and wavelet coefficients from decomposition for Example A.</figcaption>

1.0

0.5

Resolution Level

7 6 5 4 3 2 1

v(x)

-1.0 -0.5 0.0

$\cdot ^ { \mathrm { i l } } \cdot \mathrm { i } ^ { - } ! ! ^ { - } ! ! ! ^ { \cdots } ! ^ { ! } ! ^ { ! } ! ! ^ { ! } ! ^ { ! ! } ! ^ { ! ! \ldots _ { 1 + i } ! ! ! \cdot \lrcorner ! ! ! } ! ! ! ^ { ! } ! ^ { ! i _ { ! } \cdot \bar { \mathfrak{n} } _ { i } \cdot \bar { \mathfrak{h} } } ! ! ! ! ^ { ! i } ! ^ { ! } ! ^ { ! } ! ! ! ! !$

0.0 0.2 0.4 0.6 0.8 1.0

T

0

32

64

96

128

$x$

Translate
Haar wavelet

Haar wavelet

</figure>


We can see the Haar mother wavelet in the left panel of Figure 11.10. We see the wavelet
decomposition in the right panel.

Suppose we wanted to compress the data into a more compact format. Smoothing can
be viewed as a form of compression because it retains the important features of the data
while discarding some of the finer detail. The smooth is described in terms of the fitted
coefficients which are fewer than the number of data points. The method would be called
lossy since some information about the original data is lost.

For example, suppose we want to smooth the data extensively. We could throw away
all the coefficients of level four or higher and then reconstruct the function as follows:

$$> \mathrm { w t d } < - \text { threshold \left(wds, policy icy= manual walue=9999\right) }$$

<!-- PageBreak -->


## Nonparametric regression 247

Only level-three and higher coefficients are retained. There are only $2 ^ { 3 } = 8$ of these. The
thresholding here applies to level four and higher only by default. Any coefficient less
than 9999 in absolute value is set to zero-that is, all of them in this case. The wr
reverses the wavelet transform. We now plot the result as seen in the first panel of Figure
11.11:

\> plot (y "x, exa, pch=".")

\> lines (m ~ x, exa)

\> lines(fd ~ x, exa, lty=5, lwd=2)

We see that the fit consists of eight constant fits; we expect this since Haar basis is
piecewise constant and we have thrown away the higher-order parts leaving just eight
coefficients.


<figure>
<figcaption>Figure 11.11 Thresholding and inverting the transform. In the left panel all level-four and above coefficients are zeroed. In the right, the coefficients are thresholded using the default method. The true function is shown as a solid line and the estimate as $a$ dashed line.</figcaption>

1.0

1.0

y

0.0

y

0.0

-1.0

-1.0

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

x

$x$

</figure>


Instead of simply throwing away higher-order coefficients, we could zero out only the
small coefficients. We choose the threshold using the default method:

\> wtd2 <- threshold (wds)
> fd2 <- wr (wtd2)

Now we plot the result as seen in the second panel of Figure 11.11.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 248" -->

\> plot (y ~x, exa, pch=".")
> lines (m x, exa)

$$> 1 \text { ines } \left( f d 2 ^ { \sim } x _ { \prime } \text { exa } _ { \prime } 1 t y = 5 , \text { lwd } = 2 \right)$$

Again, we see a piecewise constant fit, but now the segments are of varying lengths.
Where the function is relatively flat, we do not need the detail from the higher-order
terms. Where the function is more variable, the finer detail is helpful.

We could view the thresholded coefficients as a compressed version of the original
data (or signal). Some information has been lost in the compression, but the thresholding
algorithm ensures that we tend to keep the detail we need, while throwing away noisier
elements.

Even so, the fit is not particularly good because the fit is piecewise constant. We
would like to use continuous basis functions while retaining the orthogonality and
multiresolution properties. Families of such functions were discovered recently and
described in Daubechies (1991). We illustrate the default form on our data:

\> wds <- wd (exa$y)

\> draw (wds, main="")

\> plot (wds, main="")

The mother wavelet takes an unusual form. The function is not explicitly defined, but is
implicitly computed from the method for making the wavelet decomposition. Now we try
the default thresholding and reconstruct the fit:

\> wtd <- threshold (wds)
> fd <- wr (wtd)
> plot (y ~ x, exa, pch=".")
> lines (m "x, exa)
> lines (fd ~ x, exa, lty=2)

We can see the fit in Figure 11.13. Although the fit follows the true function quite well,
there is still some roughness.

Example A does not illustrate the true strengths of the wavelet approach which is not
well suited to smoothly varying functions with the default choice of wavelet. It comes
into its own on functions with discontinuities and higher dimensions such as two-
dimensional image data.


### 11.5 Other Methods

Nearest Neighbor: In this method, we set $f _ { A } \left( x \right) =$ of $2$ nearest neighbors of x.
We let the window width vary to accommodate the same number of points. We need to
pick the number of neighbors to be used; cross-validation can be used for this purpose.

Variable Bandwidth: When the true $f$ varies a lot, a small bandwidth is good, but
where it is smooth, a large bandwidth is preferable. This motivates this estimator, suitable
for evenly spaced data:

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression 249" -->


<figure>
<figcaption>Figure 11.12 Mother wavelet is shown in the left panel-the Daubechies orthonormal compactly supported wavelet $N = 2$ from the extremal phase family. The right panel shows the wavelet coefficients.</figcaption>

1.0

Resolution Level

1
2
5
7 6 5 4321

$v \left( x \right)$

0.0

$1 ^ { \text { III } _ { k ^ { 2 } t } } t ^ { s _ { 1 } = t _ { 1 } \ldots s _ { t } } 1 ^ { \text { FI } _ { t } } { } ^ { \text { FJ } } t ^ { \text { HJ } } \cdot { } _ { k ^ { 2 } t ^ { 2 \ldots } } \text { if } I _ { k } \text { H. } ^ { \text { HL } } { } _ { t } { } ^ { \text { HL } } { } ^ { \text { gr } } I ^ { * } { } ^ { t } { } ^ { t } .$

-1.0

-1.0 -0.5 0.0 0.5 1.0 1.5

0 $3 2$ 64 96 128

$X$

Translate

Daub cmpct on ext. phase $N = 2$

Daub cmpct on ext. phase N=2

</figure>


$$f _ { A \left( x \right) } \left( x \right) = \frac { 1 } { \lambda \left( x \right) } \sum _ { i = 1 } ^ { n } K \left( \frac { x - x _ { j } } { \lambda \left( x \right) } \right) y _ { i } :$$

This is an appealing idea in principle, but it is not easy to execute in practice, because it
requires prior knowledge of the relative smoothness of the function across the range of
the data. A pilot estimate may be used, but it has been difficult to make this work in
practice.

Running Medians: Nonparametric regression is more robust than parametric regression
in a model sense, but that does not mean that it is robust to outliers. Local averaging-
based methods are sensitive to outliers, so medians can be useful. We let $N \left( x , \lambda \right) = \left\{ i : x _ { i } \right.$ is
one of the 2-nearest neighbors of $x$ then:

$$f _ { k } \left( x \right) = \text { median } \left\{ Y _ { i } \text { such thar } i \in N \left( x , \lambda \right) \right\}$$

This method is robust to outliers, but produces a rough-looking fit. One might want to
smooth again using another method. This is called twicing.

Others: The construction of alternate smoothing methods has long been a popular
topic of interest for statisticians and researchers in other fields. Because no definitive
solution is possible, this has encouraged the development of a wide range of methods.
Some are intended for general use while others are customized for a particular
application.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 250" -->


<figure>
<figcaption>Figure 11.13 Daubechies wavelet $N = 2$ thresholded $\widehat { f l } l$ to the Example A data.</figcaption>

1.0

11

y

0.0

-1.0

0.0 0.2 0.4 0.6 0.8 1.0

$X$

</figure>


### 11.6 Comparison of Methods

In the univariate case, we can describe three situations. When there is very little noise,
interpolation (or at most, very mild smoothing) is the best way to recover the relation
between $x$ and $y .$ When there is a moderate amount of noise, nonparametric methods are
most effective. There is enough noise to make smoothing worthwhile but also enough
signal to justify a flexible fit. When the amount of noise becomes larger, parametric
methods become relatively more attractive. There is insufficient signal to justify anything
more than a simple model.

It is not reasonable to claim that any one smoother is better than the rest. The best
choice of smoother will depend on the characteristics of the data and knowledge about
the true underlying relationship. The choice will also depend on whether the fit is to be
made automatically or with human intervention. When only a single dataset is being
considered, it's simple enough to craft the fit and intervene if a particular method
produces unreasonable results. If a large number of datasets are to be fit automatically,
then human intervention in each case may not be feasible. In such cases, a reliable and
robust smoother may be needed.

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression 251" -->

We think the loess smoother makes a good all-purpose smoother. It is robust to
outliers and yet can produce smooth fits. When you are confident that no outliers are
present, smoothing splines is more efficient than local polynomials.


## 11.7 Multivariate Predictors

Given $\mathrm { X } _ { 1 } , \ldots , \mathrm { X }$ where $x \in R ^ { p } ,$ we observe:

$y _ { i } = f \left( x \right) + \varepsilon _ { i } i = 1 , \ldots n$

Many of the methods discussed previously extend naturally to higher dimensions, for
example, the Nadaraya-Watson estimator becomes:

$$f _ { h } \left( x \right) = \frac { \sum _ { j = 1 } ^ { n } K \left( \frac { x - x _ { j } } { k } \right) Y _ { j } } { \sum _ { j = 1 } ^ { n } K \left( \frac { x - x _ { j } } { k } \right) }$$

where the kernel $K$ is typically spherically symmetric. The spline idea can be used with
the introduction of thin plate splines and local polynomials can be naturally extended.

We can illustrate kernel smoothing in two dimensions:

\> data (savings)
> y <- savings$sr
> x <- cbind (savings$pop15, savings$ddpi)
>
sm. regression (x, y, h=c (1,1) , xlab="pop15", ylab="growth", z
lab="savings rate")
\>
sm. regression (x, y, h=c (5, 5) , xlab="pop15", ylab="growth", z
lab="savings rate")

Developing such estimators is not so difficult but there are problems: Because
nonparametric fits are quite complex, we need to visualize them to make sense of them
and yet this cannot be done easily for more than two predictors. Most nonparametric
regression methods rely on local smoothing; local averaging is the crudest exam-ple of
this. However, to maintain a stable average we need sufficient points in the window. For
data in high dimensions, the window will need to be wide to capture sufficient points to
average. You need an extremely large number of points to cover a high-dimensional
space to high density. This is known as the "curse of dimension-ality," a term coined by
Bellman (1961). In truth, it should not be called a curse, but rather a blessing, since
information on additional variables should have some value, even if it is inconvenient.
Our challenge is to make use of this information. Nonpara-

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 252" -->


<figure>
<figcaption>Figure 11.14 Smoothing savings rate as a function growth and population under 15. Plot on the left is too rough while that on the right seems about $r i g h t .$</figcaption>

savings rate

Savings rate

growin

growin

pop15

$\widetilde { \mathrm { p o p } }$

</figure>


metric regression fits are hard to interpret in higher dimensions where visualization is
difficult. Simply extending the one-dimensional method is not effective.

The methods we describe in the following chapters impose additional restrictions on
the fitted function to make the problem feasible and the results easier to interpret.

Further Reading: For a general review of smoothing methods, see Simonoff (1996).
For books on specific methods of smoothing, see Loader (1999), Wahba (1990), Bowman
and Azzalini (1997), Wand and Jones (1995) and Eubank (1988). The application of
nonparametric regression to the goodness of fit problem may be found in Hart (1997).


## Exercises

We have introduced kernel smoothers, splines, local polynomials, wavelets and other
smoothing methods in this chapter. Apply these methods to the following datasets. You
must choose the amount of smoothing you think is appropriate. Compare the fits from the
methods. Comment on the features of the fitted curves. Comment on the advantage of the
nonparametric approach compared to a parametric one for the data and, in particular,
whether the nonparametric fit reveals structure that a parametric approach would miss.

1\. The dataset teengamb concerns a study of teenage gambling in Britain. Take the
variables gamble as the response and income as the predictor. Does a transformation
of the data before smoothing help?

2\. The dataset us wages is drawn as a sample from the Current Population Survey in
1988\. Predict the wage from the years of education. Compute the mean wage for each
number of years of education and compare the result to the smoothed fit. Take the
square root of the absolute value of the residuals from your chosen fit and smooth
these as a function of educ.

<!-- PageBreak -->

<!-- PageHeader="Nonparametric regression" -->
<!-- PageNumber="253" -->

3\. The dataset prostate is from a study of 97 men with prostate cancer who were due to
receive a radical prostatectomy. Predict the 1 weight using the age. How do the
methods deal with the outlier?

4\. The dataset divusa contains data on divorces in the United States from 1920 to 1996.
Predict divorce from year. Predict military from year. There really were more military
personnel during the Second World War, so these points are not outliers. How well do
the different smoothers respond to this?

5\. The aatemp data comes from the U.S. Historical Climatology network. They are the
annual mean temperatures (in degrees Fahrenheit) in Ann Arbor, Michigan, going
back about 150 years. Fit a smooth to the temperature as a function of year. Does the
smooth help determine whether the temperature is changing over time?

<!-- PageBreak -->


## CHAPTER 12 Additive Models

Suppose we have a response $y$ and predictors $x _ { 1 } , \ldots , x _ { p } .$ A linear model takes the form:

$$y = \beta _ { 0 } + \sum _ { j = 1 } ^ { P } \beta _ { j } X _ { j } + e$$

We can include transformations and combinations of the predictors among the $x s ,$ so this
model can be very flexible. However, it can often be difficult to find a good model, given
the wide choice of transformations available. We can try a systematic approach of fitting
a family of transformations. For example, we can try polynomials of the predictors, but
particularly if we include interactions, the number of terms becomes very large, perhaps
greater than the sample size. Alternatively, we can use more interactive and graphical
approaches that reward intuition over brute force. However, this requires some skill and
effort on the part of the analyst. It is easy to miss important structure; a particular
difficulty is that the methods only consider one variable at a time, when the secret to
finding good transformations may require that variable be considered simultaneously.

We might try a nonparametric approach by fitting:
$y = f \left( x _ { 1 } , \ldots , x _ { p } \right) + \varepsilon$

This avoids the necessity of parametric assumptions about the form of the function f, but
for $p$ bigger than two or three, it is simply impractical to fit such models due to large
sample size requirements, as discussed at the end of the previous chapter.

A good compromise between these extremes is the additive model:

$$y = \beta _ { 0 } + \sum _ { j = 1 } ^ { p } f _ { j } \left( X _ { j } \right) + e$$

where the $f _ { j }$ are smooth arbitrary functions. Additive models were introduced by Stone
(1985).

Additive models are more flexible than the linear model, but still interpretable since
the functions $f _ { j }$ can be plotted to give a sense of the marginal relationship between the
predictor and the response. Of course, many linear models discovered during a data
analysis take an additive form where the transformations are determined in an ad hoc
manner by the analyst. The advantage of the additive model approach is that the best
transformations are determined simultaneously and without parametric assumptions
regarding their form.

In its basic form, the additive model will do poorly when strong interactions exist. In
this case we might consider adding terms like $f _ { i j } \left( x _ { i } x _ { j } \right)$ or even $f _ { i j } \left( x _ { i } , x _ { j } \right)$ if there is sufficient

<!-- PageBreak -->

<!-- PageHeader="Additive models 255" -->

data. Categorical variables can be easily accommodated within the model using the usual
regression approach. For example:

$$y = \beta _ { 0 } + \sum _ { j = 1 } ^ { p } f _ { j } \left( X _ { j } \right) + Z \gamma + \varepsilon$$

where $Z$ is the design matrix for the variables that will not be modeled additively, where
some may be quantitative and others qualitative. The $\gamma$ are the associated regression
parameters. We can also have an interaction between a factor and a continuous predictor
by fitting a different function for each level of that factor. For example, we might have
$f _ { m a l e }$ and $f _ { f e m a l e }$

There are at least three ways of fitting additive models in R. The gam package
originates from the work of Hastie and Tibshirani (1990). The mgcv package is part of
the recommended suite that comes with the default installation of $R$ and is based on
methods described in Wood (2000). The gam package allows more choice in the
smoothers used while the mgcv package has an automatic choice in the amount of
smoothing as well as wider functionality. The gss package of Gu (2002) takes a spline-
based approach.

The fitting algorithm depends on the package used. The backfitting algorithm is used
in the gam package. It works as follows:

1\. We initialize by setting $\beta _ { 0 } = \bar { y } _ { \mathrm { a n d } } f _ { j } \left( x \right) = \widetilde { \beta } _ { j } x _ { \mathrm { w h e r e } } \widetilde { \beta } _ { \mathrm { i s } }$ some initial estimate, such
as the least squares, for $j = 1 , \ldots p .$

2\. We cycle $j = 1 , \ldots , p ,$ $1 \ldots , p ,$ 1, ...

$$f _ { j } = S \left( x _ { j } , y - \beta _ { 0 } - \sum _ { i \neq j } f _ { i } \left( X _ { i } \right) \right)$$

where $S \left( x , y \right)$ means the smooth on the data $\left( x , y \right) .$ The choice of $S$ is left open to
the user. It could be a nonparametric smoother like splines or loess, or it could be
a parametric fit, say linear or polynomial. We can even use different smoothers on
different predictors with differing amounts of smoothing.

The algorithm is iterated until convergence. Hastie and Tibshirani (1990) show that
convergence is assured under some rather loose conditions. The term $y - \beta _ { 0 } - \Sigma _ { i \neq j } f _ { i } \left( x _ { j } \right)$ is a
partial residual-the result of fitting everything except $x j ,$ making the connection to linear
model diagnostics.

The mgcv package employs a penalized smoothing spline approach. Suppose we
represent $f _ { j } \left( x \right) = \sum _ { i } \left[ \beta _ { i } \phi _ { i } \left( x \right) \right] _ { f _ { O } }$ a family of spline basis functions, $\phi _ { i }$ Di-We impose a
penalty $\int \left[ f _ { j } ^ { \prime \prime } \left( x \right) \right] ^ { 2 } d x$ which can be written in the form $\beta _ { j } ^ { T } S _ { j } \beta _ { j } ,$ for a suitable matrix $S _ { j }$
that depends on the choice of basis. We then maximize:

$$\log L \left( \beta \right) - \sum _ { j } A _ { j } \beta _ { j } ^ { T } S _ { j } \beta _ { j } ,$$

where $L \left( \beta \right)$ is likelihood with respect to $\beta$ and the $\lambda _ { j } \mathrm { s }$ control the amount of smoothing for
each variable. GCV is used select the $\lambda _ { \check { J } } \mathrm { s } .$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 256" -->


### 12.1 Additive Models Using the gam Package

We use data from a study of the relationship between atmospheric ozone concentration,
$O _ { 3 }$ and other meteorological variables in the Los Angeles Basin in 1976. To simplify
matters, we will reduce the predictors to just three: temperature measured at E1 Monte,
temp, inversion base height at LAX, ibh, and inversion top temperature at LAX, ibt. A
number of cases with missing variables have been removed for simplicity. The data were
first presented by Breiman and Friedman (1985). First we fit a simple linear model for
reference purposes:

\> data (ozone)
> olm <- 1m(03 ~temp + ibh + ibt, ozone)
> summary (olm)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-7.727982</td>
<td>1.621662</td>
<td>-4.77</td>
<td>0.0000028</td>
</tr>
<tr>
<td>temp</td>
<td>0.380441</td>
<td>0.040158</td>
<td>9.47</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>ibh</td>
<td>-0.001186</td>
<td>0.000257</td>
<td>-4.62</td>
<td>0.0000055</td>
</tr>
<tr>
<td>ibt</td>
<td>-0.005821</td>
<td>0.010179</td>
<td>-0.57</td>
<td>0.57</td>
</tr>
</table>


Residual standard error: 4.75 on 326 degrees of freedom
Multiple R-Squared: 0.652,
Adjusted R-squared: 0.649
F-statistic: 204 on 3 and 326 DF, p-value: < 2e-16

Note that ibt is not significant in this model. One task among others in a regression
analysis is to find the right transforms on the predictors. Additive models can help here.
We fit an additive model using the a Gaussian response as the default.

\> library (gam)
> amgam <- gam (03 ~ 10 (temp) + lo (ibh) + lo (ibt) ,
data=ozone)
> summary (amgam)
(Dispersion Parameter for gaussian family taken to be
18.664)

Null Deviance: 21115 on 329 degrees of freedom
Residual Deviance: 5935.1 on 318 degrees of freedom
AIC: 1916.0

Number of Local Scoring Iterations: 2
DF for Terms and F-values for Nonparametric Effects
Df Npar Df Npar F
Pr (F)


<table>
<tr>
<td>(Intercept)</td>
<td>1.0</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>lo (temp)</td>
<td>1.0</td>
<td>2.5</td>
<td>7.45</td>
<td>0.00025</td>
</tr>
<tr>
<td>lo (ibh)</td>
<td>1.0</td>
<td>2.9</td>
<td>7.62</td>
<td>0.000082</td>
</tr>
<tr>
<td>lo (ibt)</td>
<td>1.0</td>
<td>2.7</td>
<td>7.84</td>
<td>0.000099</td>
</tr>
</table>


We have used the loess smoother here by specifying lo in the model formula for all three
predictors. Compared to the linear model, the $R ^ { 2 }$ is:

\> 1-5935.1/21115
[1] 0.71892

<!-- PageBreak -->

<!-- PageHeader="Additive models" -->
<!-- PageNumber="257" -->

So the fit is a little better. However, the loess fit does use more degrees of freedom. We
can compute the equivalent degrees of freedom by an analogy to linear models. For linear
smoothers, the relationship between the observed and fitted values may be written as
$\widehat { y } = P y .$ The trace of $P$ then estimates the effective number of parameters. For example, in
linear regression, the projection matrix is $X \left( X ^ { T } X \right) ^ { - 1 } X ^ { T }$ whose trace is equal to the rank of
$X$ or the number of identifiable parameters. This notion can be used to obtain the degrees
of freedom for additive models.

The gam package uses a score test for the predictors. However, the p-values are only
approximate at best and should be viewed with some skepticism. It is generally better to
fit the model without the predictor of interest and then construct the F-test:

\> amgamr <- gam (03 ~ lo (temp) + lo (ibh) , data=ozone)
> anova (amgamr, amgam, test="F")
Analysis of Deviance Table
Model 1:03 ~ lo (temp) + lo (ibh)
Model 2:03 ~ lo (temp) + lo (ibh) + lo (ibt)


<table>
<tr>
<th></th>
<th>Resid. Df</th>
<th>Resid.</th>
<th>Dev</th>
<th>Df</th>
<th>Deviance</th>
<th>F</th>
<th>Pr (&gt;F)</th>
</tr>
<tr>
<td>1</td>
<td>321.67</td>
<td colspan="2">6045</td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr>
<td>2</td>
<td>318.00</td>
<td colspan="2">5935</td>
<td>3.66</td>
<td>109</td>
<td colspan="2">1.6 0.18</td>
</tr>
</table>


Again the p-value is an approximation, but we can see there is some evidence that ibt is
not significant. We now examine the fit:

\> plot (amgam, $r e s i d u a l s = T R U E ,$ se=TRUE, pch=". ")


<figure>
<figcaption>Figure 12.1 Transformations on the predictors chosen by the gam fit on the ozone data. Partial residuals and approximate 95% pointwise confidence bands are shown.</figcaption>

2

S

9

0

9

6

$\frac { 5 } { 3 }$

5

$\frac { 5 } { 5 }$

0

0

4

30 40 50 60 70 80 00

0

1000

3000

5000

0

50

150

250

temp

M

</figure>


We see the transformations chosen in Figure 12.1. For ibt, a constant function would fit
between the confidence bands. This reinforces the conclusion that this predictor is not
significant. For temperature, we can see a change in the slope around $6 0 ^ { \circ } ,$ while for ibh,
there is a clear maximum. The partial residuals allow us to check for outliers or

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 258

influential points. We see no such problems here. However, the use of the loess smoother
is recommended where such problems arise and is perhaps the best feature of the gam
package relative to the other options.


### 12.2 Additive Models Using mgcv

Another method of fitting additive models is provided by the mgcv package of Wood
(2000). We demonstrate its use on the same data. Splines are the only choice of smoother,
but the appropriate amount of smoothing is internally chosen by default. In contrast, the
gam package relies on the user to select this. There are advantages and disadvantages to
automatic smoothing selection. On the positive side, it avoids the work and subjectivity
of making the selection by hand, but on the negative side, automatic selection can fail and
human intervention may sometimes be necessary. We follow a similar analysis:

\> library (mgcv)
> ammgcv <- gam (03 ~ s (temp) +s (ibh) +s (ibt), data=ozone)
Parametric coefficients:
Estimate
std. err.
t

ratio
Pr (>|t|)

(Intercept)
11.776
0.2382
49.44
$< 2 e - 1 6$

Approximate significance of smooth terms:

edf
chi.sq
p-value
s (temp)
3.386
88.047
$< 2 e - 1 6$
s (ibh)
4.174

37.559

4.28e-07

s (ibt)
2.112

4.2263

0.134

R-sq. (adj) = 0.708
Deviance explained = 71.7%

GCV score = 19.346
Scale est. = 18.72
$n = 3 3 0$

We see that the $R ^ { 2 }$ is similar to the gam fit. We also have additional information
concerning the significance of the predictors. We can also examine the transformations
used:

plot (ammgcv)

The chosen transformations are again similar. We see that ibt does not appear to be
significant. We might also be interested in whether there really is a change in the trend
for temperature. We test this by fitting a model with a linear term in temperature and then
make the F-test:

\> aml <- gam (03 ~s (temp) +s (ibh), data=ozone)
> am2 <- gam (03 ~ temp+s (ibh), data=ozone)
> anova (am2, am1, test="F")
Analysis of Deviance Table
Model 1:03 ~ temp + s (ibh)
Model 2:03 ~ s (temp) + s (ibh)
Resid. Df Resid. Dev
Df Deviance
F $\Pr \left( > \mathrm { E } \right)$

1
323.67
6950

<!-- PageBreak -->

<!-- PageNumber="259" -->
<!-- PageHeader="Additive models" -->

2

320.97

6054

2.70

896 17.6

<!-- PageHeader="$8 e - 1 0$" -->


<figure>
<figcaption>Figure 12.2 Transformation functions for the model fit by mgcv. Note how the same scale has been deliberately used on all three plots. This allows us to easily compare the relative contribution of each variable.</figcaption>

8

2

SÌ

15

2

01

01

011245

1

0

0

0

1

0

0

0

"

30

40

50

70

60

0

1000

3000

5000

0

50

150

200

5

</figure>


The p-value is only approximate, but it certainly seems there really is a change in the
trend.

You can also do bivariate transformations with mgcv. For example, suppose we
suspect that there is an interaction between temperature and IBH. We can fit a model with
this term:

\> amint <- gam(03 ~ s (temp, ibh) +s (ibt), data=ozone)
> summary (amint)
Parametric coefficients:

Estimate
std. err.
t

ratio
Pr (>|t|)

(Intercept)
11.776
0.2409

48.88
<2e-16
Approximate significance of smooth terms:
edf
chi.sq
p-value
s (temp, ibh)
6.346
<2e-16
2.917
120.46
36.081
1.57e-07
Deviance explained =
71%
s (ibt)
R-sq. (adj) = 0.702
GCV score = 19.767

Scale est. = 19.152
$n = 3 3 0$

We compare this to the previous additive model:

\> anova (ammgcv, amint, test="F")
Analysis of Deviance Table
Model 1:03 ~ s (temp) + s (ibh) + s (ibt)
Model 2:03 ~s (temp, ibh) + s (ibt)

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 260" -->


<table>
<tr>
<th></th>
<th>Resid. Df</th>
<th>Resid.</th>
<th>Dev</th>
<th>Df</th>
<th>Deviance</th>
<th>F Pr (&gt;F)</th>
</tr>
<tr>
<td>1</td>
<td>319.327</td>
<td></td>
<td>5978</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>319.737</td>
<td></td>
<td>6124</td>
<td>-0.409</td>
<td>-146</td>
<td>19.0 0.0014</td>
</tr>
</table>


We see that the supposedly more complex model with the bivariate fit actually fits worse
than the model with univariate functions. This is because fewer degrees of freedom have
been used to fit the bivariate function than the two corresponding univariate functions. In
spite of the output p-value, we suspect that there is no interaction effect, because the
fitting algorithm is able to fit the bivariate function so simply. We now graphically
examine the fit as seen in Figure 12.3:

\> plot (amint)

\> vis. gam (amint, theta =- 45, color="gray")


<figure>
<figcaption>Figure 12.3 The bivariate contour plot for temperature and ibh is shown in the left panel. The middle panel shows the univariate transformation on ibt while the right panel shows a perspective view of the information on the left panel.</figcaption>

lindar predictor

0

50

150

250

</figure>


Given that the contours appear almost parallel and the perspective view looks like it
could be constructed with piece of paper rippled in one direction, we conclude that there
is no significant interaction. One interesting side effect is that ibt is now significant.

One use for additive models is as an exploratory tool for standard parametric
regression modeling. We can use the fitted functions to help us find suitable simple
transformations of the predictors. One idea here is to model the temp and ibh effects
using piecewise linear regression (also known as "broken stick" or segmented
regression). We define the right and left "hockey-stick" functions:

\>
$$\mathrm { r h s } < - \mathrm { f u n c t i o n } \left( \mathrm { x } _ { \prime } \mathrm { c } \right) \mathrm { i f } \mathrm { e l s e } \left( \mathrm { x } > \mathrm { c } _ { \prime } \mathrm { x - c } _ { \prime } 0 \right)$$

<!-- PageBreak -->

<!-- PageNumber="261" -->
<!-- PageHeader="Additive models" -->

\> lhs <- function(x, c) ifelse(x < c, c-x, 0)

and now fit a parametric model using cutpoints of 60 and 1000 for temp and ibh,
respectively. We pick the cutpoints using the plots:

\> olm2 <- 1m(03
rhs(temp,60)+lhs(temp,60)+rhs(ibh,1000)+lhs(ibh, 1000)
,
ozone)
> summary (olm2)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>11.603832</td>
<td>0.622651</td>
<td>18.64</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>rhs (temp, 60)</td>
<td>0.536441</td>
<td>0.033185</td>
<td>16.17</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
<tr>
<td>lhs (temp, 60)</td>
<td>-0.116173</td>
<td>0.037866</td>
<td>-3.07</td>
<td>0.0023</td>
</tr>
<tr>
<td>rhs (ibh, 1000)</td>
<td>-0.001486</td>
<td>0.000198</td>
<td>-7.49</td>
<td>6.7e-13</td>
</tr>
<tr>
<td>lhs (ibh, 1000)</td>
<td>-0.003554</td>
<td>0.001314</td>
<td>-2.71</td>
<td>0.0072</td>
</tr>
</table>


Residual standard error: 4.34 on 325 degrees of freedom
Multiple R-Squared: 0.71,
Adjusted R-squared:
0.706
F-statistic:
199 on 4 and 325 degrees of
freedom,
$p - v a l u e$ :
0

Compare this model to the first linear model we fit to this data. The fit is better and about
as good as the additive model fit. It is unlikely we could have discovered these
transformation without the help of the intermediate additive models. Furthermore, the
linear model has the advantage that we can write the prediction formula in a compact
form.

We can use additive models for building a linear model as above, but they can be used
for inference in their own right. For example, we can predict new values with standard
error:

\> predict (ammgcv, data.frame (temp=60, ibh=2000, ibt=100),
se=T)
$fit
[1] 11.013
$se. fit
[1] 0.97278

If we try to make predictions for predictor values outside the original range of the data,
we will need to linearly extrapolate the spline fits. This is dangerous for all the usual
reasons:

\> predict (ammgcv, data.frame (temp=120, ibh=2000, ibt=100) ,
$\left. s e = T \right)$
$fit
[1] 35.511
$se. fit
[1] 5.7261

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 262

We see that the standard error is much larger although this likely does not fully reflect the
uncertainty.

We should also check the usual diagnostics:

\> plot (predict (ammgcv) , residuals
(ammgcv) , xlab="Predicted", ylab="Residuals")
> qqnorm (residuals (ammgcv) , main="")

We can see in Figure 12.4 that although the residuals look normal, there is some
nonconstant variance.

Now let's see the model for the full dataset. We found that the ibh and ibt terms were
insignificant and so we removed them:

\> amred <- gam (03 ~
s (vh) +s (wind) +s (humidity) +s (temp) +s (dpg) +
s (vis) +s (doy) , data=ozone)
> summary (amred)

Approximate significance of smooth terms:


<table>
<tr>
<th></th>
<th>edf</th>
<th>chi.sq</th>
<th>p-value</th>
</tr>
<tr>
<td>$s \left( v h \right)$</td>
<td>1</td>
<td>20.497</td>
<td>0.00000852</td>
</tr>
<tr>
<td>s (wind)</td>
<td>1</td>
<td>6.5571</td>
<td>0.0109</td>
</tr>
<tr>
<td>s (humidity)</td>
<td>1</td>
<td>14.608</td>
<td>0.00016</td>
</tr>
<tr>
<td>s (temp)</td>
<td>5.769</td>
<td>87.825</td>
<td>$7 . 3 6 e - 1 5$</td>
</tr>
<tr>
<td>s (dpg)</td>
<td>3.312</td>
<td>59.782</td>
<td>$1 . 2 6 e - 1 1$</td>
</tr>
<tr>
<td>s (vis)</td>
<td>2.219</td>
<td>20.731</td>
<td>0.00006</td>
</tr>
<tr>
<td>s (doy)</td>
<td>4.074</td>
<td>106.69</td>
<td>$< 2 e - 1 6$</td>
</tr>
</table>


<figure>
<figcaption>Figure 12.4 Residuals plots for the additive model.</figcaption>

0

10

0

0

0

0

10

0

Residuals

Sample Quantiles

5

0

5

0

O

0

5

-10

8

8

0

-10

0

0

5

10

15

20

25

3

-2 -1 0 1 2 3

Predicted

Theoretical Quantiles

</figure>


R-sq. (adj) = 0.793
Deviance explained = 80.5%
Scale est. = 13.285
n = 330

GCV score = 14.113

<!-- PageBreak -->

<!-- PageNumber="263" -->
<!-- PageHeader="Additive models" -->

We will compare this to the results of different modeling approaches that we will present
later. We can see that we achieve a good fit with an $R ^ { 2 }$ of 80.5%, but at the cost of using
effectively 19.4 parameters including the intercept.

Also for future reference, here is the linear model with all insignificant terms
removed:

\> alm <- 1m(03 ~vis+doy+ibt+humidity+temp, data=ozone)
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std.</th>
<th>Error</th>
<th>t</th>
<th>value</th>
<th></th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-10.01786</td>
<td></td>
<td>1.65306</td>
<td></td>
<td>-6.06</td>
<td>3.8e-09</td>
</tr>
<tr>
<td>vis</td>
<td>-0.00820</td>
<td></td>
<td>0.00369</td>
<td></td>
<td>-2.22</td>
<td>0.027</td>
</tr>
<tr>
<td>doy</td>
<td>-0.01020</td>
<td></td>
<td>0.00245</td>
<td></td>
<td>-4.17</td>
<td>3.9e-05</td>
</tr>
<tr>
<td>ibt</td>
<td>0.03491</td>
<td></td>
<td>0.00671</td>
<td></td>
<td>5.21</td>
<td>$3 . 4 e - 0 7$</td>
</tr>
<tr>
<td>humidity</td>
<td>0.08510</td>
<td></td>
<td>$0 . 0 1 4 3 5$</td>
<td></td>
<td>5.93</td>
<td>$7 . 7 e - 0 9$</td>
</tr>
<tr>
<td>temp</td>
<td>0.23281</td>
<td></td>
<td>0.03607</td>
<td colspan="2">6.45</td>
<td>4.0e-10</td>
</tr>
<tr>
<td colspan="3">Residual standard error:</td>
<td>4.43 on</td>
<td colspan="3">324 degrees of freedom</td>
</tr>
<tr>
<td colspan="3">Multiple R-Squared: 0.699,</td>
<td></td>
<td colspan="3">Adjusted R-squared:</td>
</tr>
<tr>
<td>0.694</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr>
<td>F-statistic:</td>
<td>150 on</td>
<td>5 and</td>
<td colspan="2">324 DF,</td>
<td colspan="2">p-value:</td>
</tr>
</table>


We can see that the fit is substantially worse, but uses only six parameters. Of course, we
may be able to improve this fit with some manual data analysis. We could look for good
transformations and check for outliers and influential points. However, since we want to
compare different modeling techniques, we want to avoid making subjective
interventions for the sake of a fair comparison.


### 12.3 Generalized Additive Models

In generalized linear models:

$$\eta = X \beta \quad E Y = \mu \quad g \left( \mu \right) = \eta \quad V a r \left( Y \right) * V \left( \mu \right)$$

The approach is readily extended to additive models to form generalized additive models
(GAM). The fitting process is different in the mgcv and gam packages. The mgcv
package takes a likelihood approach, so the implementation of the fitting algorithm is
conceptually straightforward. The gam package uses a backfitting approach as described
below.

Recalling the GLM fitting method described in Section 6.2, the iterative reweighted
least squares (IRWLS) fitting algorithm starts $z _ { 0 } = \widehat { \eta } _ { 0 } + \left( y - \widehat { \mu } _ { 0 } \right) \frac { d \eta } { d t } | _ { \widehat { \eta } _ { 0 } }$ from some reasonable $\mu _ { 0 } ,$ forms the

“adjusted

dependent

variate"

weights

$w _ { 0 } ^ { - 1 } = \left( \frac { d \eta } { d \mu } \right) ^ { 2 } | _ { \widetilde { \eta } _ { 0 } } V \left( \widehat { \mu } _ { 0 } \right) _ { I }$
then regresses $z$ on $X$ using weights $w$ using weighted least
squares to get "11The process is repeated until convergence.

In generalized additive models the linear predictor becomes:

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 264" -->

$$\beta _ { 0 } + \sum _ { j = 1 } ^ { p } f _ { j } \left( X _ { j } \right)$$

and we just add an iteration step to estimate the $f _ { j } \mathrm { s } .$ There are two levels of iteration: the
GLM part where $z$ and $w$ are computed and the additive model part. We need to use a
smoother that understands weights like loess or splines.

The ozone data has a response with relatively small integer values. Furthermore, the
diagnostic plot in Figure 12.4 shows nonconstant variance. This suggests that a Poisson
response might be suitable. We fit this using the mgcv package:

\> gammgcv <- gam (03 ^
s (temp) +s (ibh) +s (ibt) , family=poisson,
scale =- 1, data=ozone)
> summary (gammgcv)

Parametric coefficients:

Estimate
std. err.
t

ratio Pr (>|t|)

(Intercept)
2.2927
0.02304

99.51
$< 2 e - 1 6$

Approximate significance of smooth terms:

edf
chi.sq
p-value

s (temp)

3.803

79.802

8.19e-15

s (ibh)

3.779

48.471

$2 . 5 9 e - 0 9$

s (ibt)

1.422

0.94684

0.465

R-sq. (adj) = 0.712

Deviance explained = 72.9%

GCV score = 1.5025

Scale est. = 1.4569
$n = 3 3 0$

We have set scale =- 1 because negative values for this parameter indicate that the
dispersion should be estimated rather than fixed at one. Since we do not truly believe the
response is Poisson, it seems wise to allow for overdispersion. The default of not
specifying scale would fix the dispersion at one. We see that the estimated dispersion is
indeed somewhat bigger than one. We see that IBT is not significant. We can check the
transformations on the predictors as seen in Figure 12.5:

\> plot (gammgcv, residuals=TRUE)


<figure>
<figcaption>Figure 12.5 Transformation on the predictors for the Poisson GAM.</figcaption>

\-

\-

\-

0

e

s(temp,4,49)

s(bh,4,47)

N

s(bt,1.78)

2

--

O

O

O

30

40 50 60 70 80 9

0

1000

3000

5000

0

50

150

250

temp

ich

</figure>


<!-- PageBreak -->

<!-- PageNumber="265" -->
<!-- PageHeader="Additive models" -->

We see that the selected transformations are quite similar to those observed previously.


### 12.4 Alternating Conditional Expectations

In the additive model:

$$y = \alpha + \sum _ { j = 1 } ^ { p } f _ { j } \left( X _ { j } \right) + e$$

but in the transform both sides (TBS) model:

$$\theta \left( y \right) = \alpha + \sum _ { j = 1 } ^ { p } f _ { j } \left( X _ { j } \right) + \varepsilon$$

For example, $y = e ^ { x _ { 1 } + \sqrt { x _ { 2 } } }$
cannot be modeled well by additive models, but can $\mathrm { i f }$ we
transform both sides:
$\log y = x _ { 1 } + \sqrt { x _ { 2 } }$
This fits within the transform-both-sides (TBS)
model framework. A more complicated alternative approach would be nonlinear
regression. One particular way of fitting TBS models is alternating conditional
expectation (ACE) which is designed to minimize $\Sigma _ { i } \left( \theta \left( y _ { i } \right) - \Sigma f _ { j } \left( x _ { i j } \right) \right) 2 .$ Distractingly, this
can be trivially minimized by setting $\theta = f = 0 = 0$ for all $j .$ To avoid this solution, we impose
the restriction that the variance of $\theta \left( y \right)$ be one. The fitting proceeds using the following
algorithm:

1\. Initialize:

$$\theta \left( y \right) = \frac { y - \bar { y } } { S D \left( y \right) } \quad f _ { j } = \widehat { \beta } _ { j } x _ { j } \quad j = 1 , \ldots p$$

2\. Cycle:

$$f _ { j } = S \left( x _ { j } , \theta \left( y \right) - \sum _ { i \neq j } f _ { i } \left( x _ { i } \right) \right)$$
$$\theta = S \left( y , \sum _ { j } f _ { j } \left( x _ { j } \right) \right)$$

Renormalize at the end of each cycle:

$$\theta \left( y \right) - \frac { \theta \left( y \right) - \theta \left( y \right) } { \sin \left( \theta \left( y \right) \right) }$$

We repeat until convergence. ACE is comparable to the additive model, except now we
allow transformation of the response as well. In principle, you can use any reasonable
smoother $S ,$ but the original smoother used was the supersmoother. This cannot be easily
changed in the $R$ software implementation.

For our example, we start with the same three predictors in the ozone data:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 266

\> x <- ozone [, c ("temp", "ibh", "ibt") ]
> library (acepack)
> acefit <- ace (x, ozone$03)

Note that the ace function interface is quite rudimentary as we must give it the $X$ matrix
explicitly. The function returns the components ty which contains $\theta \left( y \right)$ and tx which is a
matrix whose columns contain the $f _ { j } \left( x _ { j } \right) .$ We can get a sense of how well these
transformations work by fitting a linear model that uses the transformed variables:

\> summary(lm(acefit$ty ~ acefit$tx))

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>9.2e-18</td>
<td>0.0290</td>
<td>3.2e-16</td>
<td>1.0000</td>
</tr>
<tr>
<td>acefit$txtemp</td>
<td>0.9676</td>
<td>0.0509</td>
<td>19.01</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>acefit$txibh</td>
<td>1.1801</td>
<td>0.1360</td>
<td>8.68</td>
<td>2.2e-16</td>
</tr>
<tr>
<td>acefit$txibt</td>
<td>1.3712</td>
<td>0.5123</td>
<td>2.68</td>
<td>0.0078</td>
</tr>
</table>


Residual standard error: 0.527 on 326 degrees of
freedom
Multiple R-Squared: 0.726,
Adjusted R-squared:
0.723
F-statistic: 288 on 3 and 326 degrees of
freedom,
p-value :
0

All three transformed predictors are strongly significant and the fit is superior to the
original model. The $R ^ { 2 }$ for the comparable additive model was 0.703. So the additional
transformation of the response did improve the fit. Now we examine the transforms on
the response and the three predictors:

\> plot (ozone$03, acefit$ty, xlab="03",
ylab=expression (theta (03) ) )
> plot (x [, 1] , acefit$tx [, 1] , xlab="temp", ylab="f (temp) ")
> plot $\left( x \left[ , 2 \right] \right.$ , acefit$tx [, 2] , xlab="ibh", ylab="f (ibh) ")
> plot (x [, 3] , acefit$tx [, 3] , xlab="ibt", ylab="f (ibt) ")

See Figure 12.6. The transform on the response is close to, but not quite, linear. The
transformations on temp and ibh are similar to those found by the additive model. The
transformation for ibt looks implausibly rough in some parts.

Now let's see how we do on the full data:

\> x <- ozone [, -1]
> acefit <- ace (x, ozone$03)

<!-- PageBreak -->

<!-- PageNumber="267" -->
<!-- PageHeader="Additive models" -->


<figure>
<figcaption>Figure 12.6 ACE transformations: the first panel shows the transformation on the response while the remaining three show the transformations on the predictors.</figcaption>

₩

4

4

0

D

0

\-

1

5

9

00

0

4

5

.

0

!

\-

1

0

0

10

30

70

0

4000

0

1 100 200 200

5

</figure>


\>summary(lm(acefit$ty ~ acefit$tx)]

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>-5.8e-17</td>
<td>0.0225</td>
<td>-2.6e-15</td>
<td>1.0000</td>
</tr>
<tr>
<td>acefit$txvh</td>
<td>1.1715</td>
<td>0.3852</td>
<td>3.04</td>
<td>0.0026</td>
</tr>
<tr>
<td>acefit$txwind</td>
<td>1.0739</td>
<td>0.4047</td>
<td>2.65</td>
<td>0.0084</td>
</tr>
<tr>
<td>acefit$txhumidity</td>
<td>0.6515</td>
<td>0.2455</td>
<td>2.65</td>
<td>0.0084</td>
</tr>
<tr>
<td>acefit$txtemp</td>
<td>0.9163</td>
<td>0.1236</td>
<td>7.41</td>
<td>1.le-12</td>
</tr>
<tr>
<td>acefit$txibh</td>
<td>1.3510</td>
<td>0.4370</td>
<td>3.09</td>
<td>0.0022</td>
</tr>
<tr>
<td>acefit$txdpg</td>
<td>1.3217</td>
<td>0.1672</td>
<td>7.91</td>
<td>4.4e-14</td>
</tr>
<tr>
<td>acefit$txibt</td>
<td>0.9256</td>
<td>0.1967</td>
<td>4.70</td>
<td>$3 . 8 e - 0 6$</td>
</tr>
<tr>
<td>acefit$txvis</td>
<td>1.3864</td>
<td>0.2303</td>
<td>6.02</td>
<td>$4 . 8 e - 0 9$</td>
</tr>
<tr>
<td>acefit$txdoy</td>
<td>1.2837</td>
<td>0.1097</td>
<td>11.70</td>
<td>&lt; $2 e - 1 6$</td>
</tr>
</table>


$\mathrm { R e s i d u a l }$ standard error: 0.409 on 320 degrees of
freedom
$\mathrm { M u l t i p l e }$ R-Squared: 0.838,
Adjusted R-squared:
0.833

F-statistic: 184 on 9 and 320 degrees of
freedom,
p-value:
0

$A$ very good fit, but we must be cautious. Notice that all the predictors are strongly
significant. This might be a reflection of reality or it could just be that the ACE model is
overfitting the data by using implausible transformations as seen on the ibt variable
above.

ACE can be useful in searching for good transformations while building a linear
model. We might examine the fitted transformations as seen in Figure 12.6 to suggest
appropriate parametric forms. More caution is necessary if the model is to be used in its
own right, because of the tendency to overfit.

An alternative view of ACE is to consider the problem of choosing 0 and $f _ { j }$ such that
$\theta \left( Y \right)$ and $\Sigma _ { j } f _ { j } \left( X _ { j } \right)$ are maximally correlated. ACE solves this problem. For this reason,
ACE can be viewed as a correlation method rather than a regression method.

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 268

The canonical correlation method is an ancestor to ACE. Given two sets of random
variables $X _ { 1 } , \ldots X _ { m }$ and $Y _ { 1 } , \ldots Y _ { n } ,$ we find unit vectors $a$ and $b$ such that:
$\mathrm { c o r r } \left( a ^ { T } X , b ^ { T } Y \right)$

is maximized. One generalization of canonical correlation is to allow some the $X s$ and
Y's s to be power transforms of the original variables; this results in a parametric form of
ACE. For example:

\> y <- cbind (ozone$03, ozone$03^2, sqrt (ozone$03) )
> x <- ozone [, c ("temp", "ibh", "ibt") ]
> cancor (x, y)
$cor
[1] 0.832346 0.217517 0.016908
$xcoef

[1,] -3.4951e-03 3.6335e-03 -6.7913e-03
[2,] 1.3667e-05 -5.2054e-05 -5.2243e-06
[3,] 1.6744e-04 -1.7384e-03 1.2436e-03
$ycoef
[,1]
[,2]
[,3]


<table>
<tr>
<th></th>
<th>[,1]</th>
<th>$\left[ , 2 \right]$</th>
<th>[,3]</th>
</tr>
<tr>
<td>[1,]</td>
<td>-0.00390830</td>
<td>-0.00539076</td>
<td>-0.1802230</td>
</tr>
<tr>
<td>[2,]</td>
<td>0.00009253</td>
<td>-0.00044172</td>
<td>0.0022167</td>
</tr>
<tr>
<td>[3,]</td>
<td>-0.03928664</td>
<td>0.12068982</td>
<td>0.7948130</td>
</tr>
</table>


We see that it is possible to obtain a correlation of 0.832 by taking particular linear
$O 3$ $O 3 ^ { 2 }$

combinations of and $\left. \sqrt { \left( \right. } 0 3 \right) _ { w i }$ the three predictors. The other two orthogonal
combinations are not of interest to us here. Remember that $R ^ { 2 }$ is the correlation squared in
a simple linear model and $0 . 8 3 2 ^ { 2 } = 0 . 6 9 2 ,$ so this is not a particularly competitive fit.

There are some oddities about ACE. For a single predictor, ACE is symmetric in $X$
and $Y ,$ which is not the usual situation in regression. Furthermore, ACE does not
necessarily reproduce the true model. Consider the population form of the problem and
take $Y = X + \&$ and $\& \sim N \left( 0 , 1 \right)$ and $X \sim U \left( 0 , 1 \right) ,$ then $E \left( Y | X \right) = X$ but $E \left( X | Y \right) \neq Y$ which is not
what one might expect, because $f$ and $0$ will not both be identity transformations as the
model might suggest.


### 12.5 Additivity and Variance Stabilization

Additivity and variance stabilization (AVAS) is another TBS model and is quite similar
to ACE. We choose the $f _ { j }$ to optimize the fit, but we also want constant variance for the
response:

$$\left. \mathrm { v a r } \left[ \theta \left( Y \right) \right] \sum _ { j = 1 } ^ { P } f _ { j } \left( X _ { j } \right) \right] = \mathrm { c o n s t a n t }$$

So we choose the $f _ { j }$ to get a good additive fit and choose the $\theta$ to get constant variance.

<!-- PageBreak -->

<!-- PageHeader="Additive models 269" -->

Here is how the method of fitting 0 works: Suppose $V a r \left( Y \right) \equiv V \left( Y \right)$ is not constant. We
transform to constancy by:

$$\theta \left( t \right) = \int _ { 0 } ^ { t } \frac { d \mu } { \sqrt { V \left( \mu \right) } }$$

We use data to estimate $V \left( y \right) ,$ then get 0. The purpose of the $\mathrm { A V A S }$ method is to obtain
additivity and variance stabilization and not necessarily to produce the best possible fit.
We demonstrate its application on the ozone data:

$$> a v a s f i t < - \quad a v a s \left( x , o z o n e 0 3 \right)$$

Plot the transformations selected:

\> plot (ozone$03, avasfit$ty,
$a b = 1 0 3 ^ { n } ,$ ylab=expression (theta (03) ) )
> plot (x [, 1] , avasfit$tx [, 1] , $\left. x \right] a b = { } ^ { \prime \prime } t e m p ^ { r } ,$ ylab="f (temp) ")
> plot $\left( x \left[ , 2 \right] \right.$ , avasfit$tx [, 2] , xlab="ibh", ylab="f (ibh) ")
> plot $\left( x \left[ , 3 \right] \right.$ , $\mathrm { a v a s } \text { fit } S t x \left[ , 3 \right]$ , xlab="ibt", $\left. y l a b = ^ { \prime \prime } f \left( \text { ibt } \right) ^ { \prime \prime } \right)$


<figure>
<figcaption>Figure 12.7 AVAS transformations- the first panel shows the transformation on the response while the remaining three show the transformations on the predictors.</figcaption>

C

₦

0

$\stackrel { \mathrm { r e } } { \cdot }$

1

0

0

0

4

0

\-

1

0

.

0

₼

I

$

9

5

E

\+

A

H

1

0

2

!

D

0

10 20 $2 0$

30

50

70

\*

i

1

0

4000

0

100

temp

5

</figure>


See Figure 12.7. It would be convenient if the transformation on the response matched a
simple functional form. We see if this is possible. We need to sort the response to get the
line plots to work:

\> i <- order (ozone$03)
>

plot (ozone$03 [i] , avasfit$ty[i], type="1", xlab="03", ylab=
expression (theta (03) ]
\> gs <- lm (avasfit$ty[i] ~ sqrt (ozone$03[i]))
> lines (ozone$03 [i] , gs$fit, lty=2)
> gl <- lm(avasfit$ty[i] ~ log(ozone$03[i]))
> lines (ozone$03 [i], gl$fit, lty=5)

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 270

See the;eft panel of Figure 12.8. We have shown the square-root fit as a dotted line and
log fit as a dashed line. Neither one fits well across the whole range. Now look at the
overall fit:

\> lmod <- lm (avasfit$ty avasfit$tx)

\> summary(lmod)

Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std</th>
<th>Error t</th>
<th>value</th>
<th>Pr</th>
</tr>
<tr>
<td>(Intercept)</td>
<td>2.87e-07</td>
<td></td>
<td>3.10e-02</td>
<td>9.3e-06</td>
<td>1.000</td>
</tr>
<tr>
<td>avasfit$txtemp</td>
<td>9.02e-01</td>
<td></td>
<td>7.50e-02</td>
<td>12.02</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>avasfit$txibh</td>
<td>7.98e-01</td>
<td></td>
<td>1.09e-01</td>
<td>7.33</td>
<td>1.8e-12</td>
</tr>
<tr>
<td>avasfit$txibt</td>
<td>5.69e-01</td>
<td></td>
<td>2.39e-01</td>
<td>2.38</td>
<td>0.018</td>
</tr>
</table>


Residual standard error: 0.563 on 326 degrees of
freedom
Multiple R-Squared: 0.687,
Adjusted R-squared:

0.684

F-statistic:
238 on 3 and 326 degrees of
freedom,
p-value:
0


<figure>
<figcaption>Figure 12.8 The left panel checks for simple fits to the $A V A S$ transformation on the response given by the solid line. The $\log f i t$ is given by the dashed line while the square-root fit is given by the dotted line. The right panel shows the residuals vs. fitted values plot for the $A V A S$ model.</figcaption>

ON

1.0

1

e(03)

Residuals

0.0

O

T

-1.0

2

9

-2.0

0

10

20

30

-1.5

-0.5

0.5

1.5

O3

Fitted

</figure>


The fit is not so good, but check the diagnostics:

\> plot (predict (lmod), residuals

$$\left. \left( \mathrm { l m o d } \right) , \mathrm { x l a b } = ^ { \mathrm { n } } \mathrm { E i t e d } ^ { \mathrm { n } } , \mathrm { y l a b } = ^ { \mathrm { n } } \mathrm { R e s i d u a l s } ^ { \prime \prime } \right)$$

<!-- PageBreak -->

<!-- PageNumber="271" -->
<!-- PageHeader="Additive models" -->

The plot is shown in the right panel of Figure 12.8.

AVAS does not optimize the fit; it trades some of the optimality in order to obtain
constant variance. Whether this is a good trade depends on how much relative value you
put on the accuracy of point predictions and accurate estimation of the standard error of
prediction. In other words, is it more important to try to be right or to know how much
you are wrong? The choice will depend on the application.


### 12.6 Generalized Additive Mixed Models

The generalized additive mixed model (GAMM) manages to combine the three major
themes of this book. The response can be nonnormal from the exponential family of
distributions. The error structure can allow for grouping and hierarchical arrangements in
the data. Finally we can allow for smooth transformations of the response. We
demonstrate this method on the epilepsy data from Section 10.2:

\> data (epilepsy)
> egamm <- gamm (seizures ~treat*expind+s (age) ,
family=poisson,
random=list(id="1) , data=epilepsy, subset=(id != 49) )
> summary (egamm$gam)

Parametric coefficients:

Estimate std. err.
t

ratio
Pr (>|t|)


<table>
<tr>
<td>(Intercept)</td>
<td>3.1607</td>
<td>0.1435</td>
<td>22.02</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>treat</td>
<td>-0.010368</td>
<td>0.2001</td>
<td>-0.05182</td>
<td>0.959</td>
</tr>
<tr>
<td>expind</td>
<td>-1.2745</td>
<td>0.07574</td>
<td>-16.83</td>
<td>&lt;2e-16</td>
</tr>
<tr>
<td>treat : expind</td>
<td>-0.30238</td>
<td>0.1126</td>
<td>-</td>
<td></td>
</tr>
</table>


2.684
0.00769

Approximate significance of smooth terms:
edf
chi.sq
p-value

s (age)
1.014
0.30698
0.586

R-sq. (adj) = 0.328 Scale est. = 2.5754 n = 290

We see that the age effect is not significant. Again the interaction effect is significant
which shows, in this case, a beneficial effect for the drug. We would like to use an offset
here for compatibility with the previous analysis.


### 12.7 Multivariate Adaptive Regression Splines

Multivariate adaptive regression splines (MARS) were introduced by Friedman (1991).
We wish to find a model of the form:

$$f \left( x \right) = \sum _ { j = 1 } ^ { k } c _ { j } B _ { j } \left( x \right)$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 272" -->

where the basis functions, $B _ { j } \left( x \right) ,$ are formed from products of terms of the form
$\left[ \pm \left( x _ { i } - t \right) \right] _ { + } ^ { q }$
"The []+ denotes taking the positive part. For $q = 1 ,$ this is sometimes called a
hockey-stick function and can be seen in the right panel of Figure 11.6. The $q = 1$ case is
the most common choice and one might think this results in a piecewise linear fit, as in
Section 11.2. However, the fit is more flexible than this. Consider the product of two
hockey-stick functions in one dimension; this forms a quadratic shape. Furthermore, if we
form the product of terms in two or more variables, we have an interaction term.

The model building proceeds iteratively. We start with no basis functions. We then
search over all variables and possible knotpoints $t$ to find the one basis function that
produces the best fit to the data. We now repeat this process to find the next best basis
function addition given that the first basis function is already included in the model. We
might impose rules on what new basis functions are included. For example, we might
disallow interactions or only allow two-way interactions. This will enhance
interpretability, possibly at the cost of fit. The number of basis functions added
determines the overall smoothness of the fit. We can use cross-validation to determine
how many basis functions are enough.

When interactions are disallowed, the MARS approach will be a type of additive
model. The MARS model building will be iterative, in contrast to the fit using the gam
function of the mgcv package that fits and determines overall smoothness in one step. If a
strictly additive model is all that is needed, the mgcv approach will typically be more
effective. The MARS approach will have a relative advantage when interactions are
considered, particularly when there are a larger number of variables. Here there will be a
large number of potential interactions that cannot be simultaneously entertained. The
iterative approach of MARS will be more appropriate here.

We apply the MARS method to the ozone dataset. The mda library needs to be
installed and loaded:

\> library (mda)

$$\begin{array}{} { > \text { data } \left( 0 \text { zone } \right) } \\ { > a < - \text { mars } \left( \text { ozone } \left[ , - 1 \right] , \text { ozone } \left[ , 1 \right] \right) } \end{array}$$

The interface is quite rudimentary. The default choice allows only additive (first-order)
predictors and chooses the model size using a GCV criterion. The basis functions can be
used as predictors in a linear regression model:

\> summary(lm(ozone[,1] ~ a$x-1))

Coefficients:


<table>
<tr>
<th></th>
<th></th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>$a ^ { 5 } \times 1$</td>
<td>8.99345</td>
<td>0.80456</td>
<td>11.18</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>$a \sin 2$</td>
<td>0.24607</td>
<td>0.05326</td>
<td>4.62</td>
<td>5.6e-06</td>
</tr>
<tr>
<td>$a 5 \times 3$</td>
<td>-0.00300</td>
<td>0.00108</td>
<td>-2.79</td>
<td>0.00561</td>
</tr>
<tr>
<td>$a \leq x 4$</td>
<td>0.04784</td>
<td>0.01722</td>
<td>2.78</td>
<td>0.00580</td>
</tr>
<tr>
<td>$a 5 \times 5$</td>
<td>-0.11358</td>
<td>0.02316</td>
<td>-4.90</td>
<td>$1 . 5 e - 0 6$</td>
</tr>
<tr>
<td>$a \leq x 6$</td>
<td>-0.10105</td>
<td>0.01423</td>
<td>-7.10</td>
<td>$8 . l e - 1 2$</td>
</tr>
<tr>
<td>$a \sin 7$</td>
<td>0.02482</td>
<td>0.00568</td>
<td>4.37</td>
<td>$1 . 7 e - 0 5$</td>
</tr>
<tr>
<td>$a 5 \times 8$</td>
<td>0.01752</td>
<td>0.00471</td>
<td>3.72</td>
<td>0.00024</td>
</tr>
<tr>
<td>$a 5 \times 9$</td>
<td>-0.09178</td>
<td>0.02082</td>
<td>-4.41</td>
<td>1.4e-05</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageHeader="Additive models" -->
<!-- PageNumber="273" -->

a$x10 -0.13890
0.02302
-6.03

4.4e-09

a$x11 -0.55358

0.17375

-3.19

0.00159

a$x12 0.02970

0.01074

2.77

0.00602

Residual standard error: 3.64 on 318 degrees of freedom

Multiple R-Squared: 0.937,

Adjusted R-squared:

0.935

F-statistic: 395 on 12 and 318 degrees of
freedom,
p-value :
0

The fit is very good in terms of $R ^ { 2 } ,$ but the model size is also larger. It is also an additive
model, so we can reasonably compare it to the additive model presented at the end of
Section 12.2. That model had an adjusted $R ^ { 2 } \text { of } 7 9 . 3 \%$ using 19.4 parameters.

Let's reduce the model size to that used for previous models. The parameter nk
controls the maximum number of model terms:

\> a <- mars (ozone [,-1] , ozone [, 1] , nk=7)
> summary(lm(ozone[,1] ~ a$x-1))
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th>Pr</th>
</tr>
<tr>
<td>a$x1</td>
<td>12.663482</td>
<td>0.751400</td>
<td>16.85</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>a$x2</td>
<td>0.483948</td>
<td>0.029735</td>
<td>16.28</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td>a$x3</td>
<td>-0.096484</td>
<td>0.043102</td>
<td>-2.24</td>
<td>0.026</td>
</tr>
<tr>
<td>a$x4</td>
<td>-0.001420</td>
<td>0.000199</td>
<td>-7.13</td>
<td>6.8e-12</td>
</tr>
<tr>
<td>a$x5</td>
<td>-0.002100</td>
<td>0.001086</td>
<td>-1.93</td>
<td>0.054</td>
</tr>
<tr>
<td>a$x6</td>
<td>-0.012421</td>
<td>0.002784</td>
<td>-4.46</td>
<td>$1 . l e - 0 5$</td>
</tr>
<tr>
<td>a$x7</td>
<td>-0.108042</td>
<td>0.020666</td>
<td>-5.23</td>
<td>3.le-07</td>
</tr>
</table>


Residual standard error: 4.16 on 323 degrees of freedom
Multiple R-Squared: 0.916,
Adjusted R-squared:
0.915
F-statistic: 506 on 7 and 323 degrees of
freedom,
p-value:
0

This fit is worse, but remember we are disallowing any interaction terms. Now let's allow
second-order (two-way) interaction terms, nk was chosen to get the same model size as
before:

\> a <- mars (ozone [,-1] , ozone [, 1] , nk=10, degree=2)
> summary (lm (ozone [, 1] ~ a$x-1) )
Coefficients:


<table>
<tr>
<th></th>
<th>Estimate</th>
<th>Std. Error</th>
<th>t value</th>
<th></th>
</tr>
<tr>
<td colspan="2">a$x1 12.090698</td>
<td>0.647896</td>
<td>18.66</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td colspan="2">a$x2 0.574349</td>
<td>0.031756</td>
<td>18.09</td>
<td>&lt; 2e-16</td>
</tr>
<tr>
<td colspan="2">a$x3 -0.119057</td>
<td>0.041274</td>
<td>-2.88</td>
<td>0.0042</td>
</tr>
<tr>
<td colspan="2">a$x4 -0.001149</td>
<td>0.000163</td>
<td>-7.05</td>
<td>1.le-11</td>
</tr>
<tr>
<td colspan="2">a$x5 -0.008251</td>
<td>0.001380</td>
<td>-5.98</td>
<td>6.0e-09</td>
</tr>
<tr>
<td colspan="2">a$x6 -0.012828</td>
<td>0.002656</td>
<td>-4.83</td>
<td>2.le-06</td>
</tr>
<tr>
<td>a$x7</td>
<td>-0.102334</td>
<td>0.019730</td>
<td>-5.19</td>
<td>3.8e-07</td>
</tr>
</table>


Residual standard error: 3.97 on 323 degrees of freedom
Multiple R-Squared: 0.924,
Adjusted R-squared:
0.922

<!-- PageBreak -->


## Extending the linear model with R 274

F-statistic: 560 on 7 and 323 DF, p-value: < 2e-16

This is a good fit. Compare this with an additive model approach. Since there are nine
predictors, this would mean 36 possible two-way interaction terms. Such a model would
be complex to estimate and interpret. In contrast, the MARS approach reduces the
complexity by carefully selecting the interaction terms.

Now let's see how the terms enter into the model. We can examine the actual form of
the basis functions. Start by examining the indicator matrix:

\> a$factor [a$selected. terms, ]


<table>
<tr>
<th></th>
<th>vh</th>
<th>wind</th>
<th>humidity</th>
<th>temp</th>
<th>ibh</th>
<th>dpg</th>
<th>ibt</th>
<th>vis</th>
<th>doy</th>
</tr>
<tr>
<td>[1,]</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
</tr>
<tr>
<td>$\left[ 2 \right]$</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>1</td>
<td>0 ☐</td>
<td>0</td>
<td>0 ☐</td>
<td>☐</td>
<td>0 0 ☐</td>
</tr>
<tr>
<td>$3 , 1$</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>-1</td>
<td>0 ☐</td>
<td>0</td>
<td>0</td>
<td>0 ☐</td>
<td>0 ☐</td>
</tr>
<tr>
<td>$\left[ 4 , \right]$</td>
<td>0</td>
<td>0</td>
<td>☐ 0</td>
<td>0 ☐</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0 ☐</td>
</tr>
<tr>
<td>[5,]</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0 ☐</td>
</tr>
<tr>
<td>$6 , 1$</td>
<td>0</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0 ☐</td>
<td>0</td>
<td>0</td>
<td>0 ☐</td>
<td>1</td>
</tr>
<tr>
<td>[7,]</td>
<td>0</td>
<td>0 ☐</td>
<td>☐</td>
<td>0 0 ☐</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0 ☐</td>
<td>-1</td>
</tr>
</table>


The first term, given by the first row, is the intercept and involves no variables. The sixth
and seventh involve just doy. The "1" indicates a right hockey stick and $^ { < c } - 1 ^ { \text { , 2 } }$ a left
hockey stick. The ibh term just has the right hockey stick. Depicting the effect of doy and
ibh just requires plotting the transformation as a function of the predictor:

\>
plot (ozone [ , 6] , a$x [ , 4] * a$coef [4] , xlab="ibh", ylab="Contr
ibution of ibh")
\>

$$\left( 0 z \text { one } \left[ , 1 0 \right] , a \stackrel { * } { \mapsto } x \left[ , 7 \right] ^ { * } \text { as } 0 \text { coef } \left[ 7 \right] + a \stackrel { \text { s } } { \mapsto } x \left[ , 6 \right] ^ { * } \text { a } \text { Scoef } \left[ 6 \right] , x \right]$$

$b = { } ^ { n } D a y ^ { \prime \prime } ,$
ylab="Contribution of day")

Temperature and humidity have an interaction so we must combine all terms involving
these. Our approach is to compute the predicted value of the response over a grid of
values where temperature and humidity are varied while holding the other predictors at
their median values. The interaction is displayed as a contour plot and a three-dimensionl
plot of the surface:

\> humidity <- seq (10,100, len=20)
> temp <- seq (20,100, len=20)
> medians <- apply (ozone, 2, median)
> pdf <- matrix (medians, $n r o w = 4 0 0 ,$ ncol=10, $\left. \mathrm { b y r o w = } \mathbb{T} \right)$
> pdf [,4] <- rep (humidity, 20)

\> pdf [,5] <- rep (temp, rep (20,20))
> pdf <- as.data. frame (pdf)
> names (pdf) <- names (medians)
> z <- predict. mars (a, pdf [,-1] )
> zm <- matrix (z, ncol=20, nrow=20)

<!-- PageBreak -->

<!-- PageNumber="275" -->
<!-- PageHeader="Additive models" -->

\>
contour (humidity, temp, zm, xlab="Humidity", ylab="Temperat
ure")
\> persp (humidity, temp, zm,
xlab="Humidity", ylab="Temperature",
zlab="Ozone", theta =- 30)

Now check the diagnostics:

\> qqnorm (a$res, main="")
> plot (a$fit, a$res, xlab="Fitted", ylab="Residuals")

These plots show no problem with normality, but some indication of nonconstant
variance. See the bottom two panels of Figure 12.9.

It is interesting to compare the MARS approach to the univariate version as
demonstrated in Figure 11.7. There we used a moderate number of knots in just one
dimension while MARS gets by with just a few knots in higher dimensions. The key is to
choose the right knots. MARS can be favorably compared to linear regression: it has
additional flexibility to find nonlinearity in the predictors in higher dimensions. MARS
can also be favorably compared to the tree method discussed in the next chapter: it allows
for continuous fits but still maintains good interpretability.

Further Reading: Hastie and Tibshirani (1990) provide the original overview of
additive modeling, while Wood (2006) gives a more recent introduction. Gu (2002)
presents another approach to the problem. Green and Silverman (1993) show the link to
GLMs. Hastie, Tibshirani, and Friedman (2001) discuss additive models as part of larger
review and compare them to competitive methods.


### Exercises

1\. The fat data gives percentage of body fat, age, weight, height, and 10 body
circumference measurements, such as the abdomen, are recorded for 252 men. Body
fat is estimated through an underwater weighing technique, but this is inconvenient to
use widely. Develop an additive model that allows the estimation of body fat for men
using only a scale and a measuring tape. Your model should predict %body fat
according to Siri. You may not use Brozek's %body fat, density or fat free weight as
predictors.

2\. Find a good model for volume in terms of girth and height using the trees data. We
might expect that $\mathrm { V o l u m e } = c ^ { * }$ Height * Girth2 suggesting a logarithmic transformation
on all variables to achieve a linear model. What models do the ACE and AVAS
procedures suggest for this data?

3\. Refer to the pima dataset described in Question 3 of Chapter 2. First take care to deal
with the clearly mistaken observations for some variables.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 276" -->


<figure>
<figcaption>Figure 12.9 Contribution of predictors in the $M A R S$ model and diagnostics.</figcaption>

0

5

\-

1

İ

Contribution of ith

Contribution of dary

N

₦

0

8

-4

0

0

0

1000

2000

3000

4000

5000

50

100

150

200

250

300

350

40

Day

100

L

Temperature

auozo

60

4

Temperature

40

Humidity

A

20

40

80

$1 0 0$

Humidity

00

0

0

0

0

10

10

0

0

0

Y

0

0

0

0

4

0

0

0

0

o

000

00

Sample Cuantos

5

0

000

0

0

0

0

0

0

Residuals

0

@

0

0

4

0

0

0

0

0

00

Q

90

0

0

¢

0

00

0

0

0

0

0

-10

0

.

0

0

0

0

0

3

2

m

1

0

1

2

3

5

10

15

20

Theoretical Quantiles

25

Fitted

</figure>


(a) Fit a generalized additive model with the result of the diabetes test as the response
and all the other variables as predictors.

(b) Perform diagnostics on your model, reporting any potential violations.

(c) Predict the outcome for a woman with predictor values 1, 99, 64, 22, 76, 27, 0.25,
25 (same order as in dataset). How certain is this prediction?

(d) If you completed the logistic regression analysis of the data earlier, compare the
two analyses.

<!-- PageBreak -->

<!-- PageHeader="Additive models 277" -->

4\. The dvisits data comes from the Australian Health Survey of 1977-78 and consist of
5190 single adults where young and old have been oversampled.

(a) Build a generalized additive model with doctorco as the response and sex, age,
agesq, income, levyplus, freepoor, freerepa, illness, actdays, hscore, chcond1 and
chcond2 as possible predictor variables. Select an appropriate size for your model.

(b) Check the diagnostics.

(c) What sort of person would be predicted to visit the doctor the most under your
selected model?

(d) For the last person in the dataset, compute the predicted probability distribution for
their visits to the doctor, i.e., give the probability they visit 0,1, 2 etc. times.

(e) If you have previously completed the analysis of this data in the exercises for
Chapter 3, compare the results.

5\. Use the additive model approach to reanalyze the mot or ins data introduced in Section
7.1. For compatibility with the previous analysis, restrict yourself to data from zone
one. Try both a Gaussian additive model with a logged response and a gamma GAM
for the untransformed response. Compare your analysis to the gamma GLM analysis
in the text.

6\. The ethanol dataset in the lattice package presents data from ethanol fuel burned in a
single-cylinder engine. The emissions of nitrogen oxides should be considered as the
response and engine compression and equivalence ratio as the predictors. Study the
example plots given on the help page for ethanol that reveal the relationship between
the variables.

· Apply the additive model approach to the data.

· Try the MARS approach.

Did either approach reveal the structure that seems apparent in the plots?

<!-- PageBreak -->


## CHAPTER 13 Trees


### 13.1 Regression Trees

Regression trees are similar to additive models in that they represent a compromise
between the linear model and the completely nonparametric approach. Tree methodology
has roots in both the statistics and computer science literature. A precursor to current
methodology was CHAID developed by Morgan and Sonquist (1963) although the book
by Breiman, Friedman, Olshen, and Stone (1984) introduced the main ideas to statistics.
Concurrently, tree methodology was developed in machine learning starting in the
1970s-see Quinlan (1993) for an overview.

Most statistical work starts from the specification of a model. The model says how we
believe the data is generated and contains both a systematic and a random component.
The model is not completely specified and so we use the data to select a particular model
by either estimating parameters or perhaps by fitting functions, as in our recent
nonparametric approaches. Clearly this strategy has been effective in a wide range of
situations. However, the insistence on specifying a model, right from the start, does limit
statistics. It is often difficult to specify a model, particularly for larger and more complex
datasets. Furthermore, it is often impractical to develop inferential methods for more
complex statistical models.

Tukey (1977) advocated exploratory data analysis (EDA) in his book. Graphical and
descriptive statistics can sometimes make the message of the data very clear or at least
suggest a suitable form for the model. However, EDA is not a complete solution and
sometimes we need definite predictions or conclusions.

Regression trees are an example of a statistical method that is best described by the
algorithm used in their construction. One can uncover the implicit model underlying
regression trees, but the algorithm is the true starting point. Any method of analysis
should ultimately be judged on whether it successfully predicts or explains something.
Statistical models may achieve this, but algorithmically based methods are also
competitive. The distinction between algorithm based and model-based methods is
discussed in Breiman (2001b). In the computer science literature, tree methodology has
been applied to decision tree problems where there is no stochastic structure and we
simply want to build a rule for making the correct decision.

We use the recursive partitioning regression algorithm:

1\. Consider all partitions of the region of the predictors into two regions where the
division is parallel to one of the axes. In other words, we partition a single predictor by
choosing a point along the range of that predictor to make the split. It does not matter
exactly where we make the split between two adjacent points so there will be at most
$\left( n - 1 \right) p$ partitions to consider.

<!-- PageBreak -->

<!-- PageNumber="Trees 279" -->

2\. For each partition, we take the mean of the response in that partition. We then
compute:

$$R S S \left( p a r t i t i o n \right) = R S S \left( p a r t _ { 1 } \right) + R S S \left( p a r t _ { 2 } \right)$$

We then choose the partition that minimizes the residual sum of squares (RSS).
We do need to consider many partitions, but the computations on each partition
are simple, so that fit can be accomplished without excessive effort.

3\. We now subpartition the partitions in a recursive manner. We only allow partitions
within existing partitions and not across them. This means that the partitioning can be
represented using a tree. There is no restriction preventing us from splitting the same
variables consecutively.

For categorical predictors, it is possible to split on the levels of the factor. For an ordered
factors with $\mathrm { I }$ levels, there are only $L - 1$ possible splits. For an unordered factor, there are
$2 ^ { L - 1 } - 1$ possible splits. Although, this is a large number of possibilities as L grows, there
is a way to limit the number that need to be considered. Notice that there is no point in
monotonely transforming a quantitative predictor as this will have no effect on the
partitioning algorithm. Transforming the response will make a difference because it will
change the computation of the RSS.

Missing values can be handled quite easily by tree methods. When we construct the
tree, we may encounter missing values for a predictor when we are considering a split on
that variable. We may simply exclude such points from the computation provided we
weight appropriately. This approach is suitable for data where the observations are
missing in a noninformative manner. If we believe the fact of being missing express some
information, we might choose to treat missingness as an additional level of a factor. For
continuous predictors, we could discretize the data into ranges so that it becomes a factor
and then add missingness as an additional level. When we wish to predict the response
for a new value with missing values, we can drop the prediction down through the tree
until the missing values prevent us from going further. We can then use the mean value
for that internal node. An alternative is to use surrogate splits, described below.

Tree models are well suited to finding interactions. If we split on one variable and then
split on another variable within the partitions of the first variable, we are finding an
interaction between these two variables. As we construct further splits within splits, we
are finding higher and higher order interactions. This may be a disadvantage as true high-
order interactions are not common in reality. The MARS method discussed in Section
12.7 counteracts this by limiting the amount of interaction.

Trees are quite popular because the structure is easier for nontechnical people to
understand. The term CART stands for Classification and Regression Trees and is also
the name of a commercial software product.

We apply the regression tree methodology to study the relationship between
atmospheric ozone concentration and meteorology in the Los Angeles Basin in 1976. A
number of cases with missing variables have been removed for simplicity. The data were
first presented by Breiman and Friedman (1985). We wish to predict the ozone level from
the other predictors. We read in the data and summarize numerically and graphically:

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 280

\> data (ozone)
> summary (ozone)
> pairs (ozone, pch=". ")

The plots (not shown) reveal several nonlinear relationships indicating that a linear
regression might not be appropriate without the addition of some transformations. Now
fit a tree:

\> library (rpart)
> (roz <- rpart (03 ~ . , ozone) )
n= 330
node), split, n, deviance, Yval
\* denotes terminal node
1\) root 330 21115.00 11.7760
2\) temp< 67.5 214
4114.30 7.4252

4\) ibh>=3573.5 108
689.63 $5 . 1 4 8 1$ *

5\) ibh< 3573.5 106

2294.10 9.7453

10\) dpg< - 9.5 35
$3 6 2 . 6 9$ 6.4571 *

11\) dpg> =- 9.5 71
1366.50 11.3660

22\) ibt< 159 40
287.90 9.0500 *

23\) ibt>=159 31
587.10 14.3550 *

3\) temp>=67.5 116
5478.40 19.8020

6\) ibt< 226.5 55
1276.80 15.9450

12\) humidity< 59.5 10

167.60 10.8000 *

13\) humidity>=59.5 45
785.64 17.0890
\*

7\) ibt>=226.5 61

2646.30 23.2790

14\) $d o y > = 3 0 6 . 5$ 8
398.00 16.0000 *

15\) doy< 306.5 53

30\) vis>=55 36

1760.50 24.3770
1149.90 22.9440 *

31\) vis< 55 17
380.12 27.4120 *

We see that the first split (nodes 2 and 3) is on temperature, 214 observations have
temperatures less than 67.5 with a mean response value of 7.4, whereas 116 observations
have temperatures greater than 67.5 with a mean response value of 20. The total RSS has
been reduced from 21,000 to $4 1 0 0 + 5 5 0 0 = 9 6 0 0 .$ Although the relevant information can be
gleaned from the text-based output, a graphical display is nicer as in Figure 13.1. In the
first version of the plot, the depth of the branches is proportional to the reduction in error
due to the split. The disadvantage is that the labels can be hard to read in lower parts of
the tree where the reduction in error is much smaller. The second version of the plot uses
a uniform spacing to allow more room for labeling:

\> plot (roz, margin =. 10)
> text (roz)
> plot (roz, compress=T, uniform=T, branch=0. 4, margin =. 10)
> text (roz)

We see that the first split on temperature produces a large reduction in the RSS. Some of
the subsequent splits do not do much. The immediate message is that high

<!-- PageBreak -->

<!-- PageNumber="Trees 281" -->


<figure>

btx : 26.5

\-

-25

17

81

2

27

</figure>


<figure>
<figcaption>Figure 13.1 Tree model for the ozone data. On the left, the depth of the branches is proportional to the improvement in fit. On the right, the depth is held constant to improve readability. If the logical condition at a node is true, follow the branch to the left.</figcaption>

copy -95 humidhy/ 50.5 doyl-306.5

5.1

65

17

0.1

14

23

27

</figure>


temperatures are associated with high ozone levels. A regression tree is a regression
model, so diagnostics are called for:

\> plot (predict (roz) , residuals (roz) ,
xlab="Fitted", ylab="Residuals")
> qqnorm (residuals (roz) )

See Figure 13.2. There are no visible problems here. If nonconstant variance is observed,
one might consider transforming the response. Trees are also somewhat sensitive to
outliers as they are based on local means. Outliers may be observed in the QQ plot, but,
as with linear models, they may conceal themselves and be influential on the fit. Suppose
we wanted to predict the response for a new value-for example the median value in the
dataset:

\> (x0 <- apply (ozone [,-1] , 2, median) )
vh

67.5
120.0
wind
humidity
5760.0

temp
5.0
ibh
dpg

64.0

ibt
vis

62.0
2112.5

24.0
1

doy
205.5

\> predict (roz, data.frame (t (x0)))
1
14.355

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 282" -->

You should be able to verify this prediction by following the splits down through the tree
shown in Figure 13.1.


<figure>
<figcaption>Figure 13.2 Residuals and fitted values for the tree model of the Ozone data are shown in the left panel. $A \quad Q Q \quad p l o t$ of the residuals is shown in the right panel.</figcaption>

15

0

15

10

00

0

XxxxXXXX000000000 00

0

Residuals

000000000000

0 0 00 000 00

0 0 000

000000000009

00000000000000

CO 0000000000

Sample Quantiles

10

5

0

0

-5

5

0

8

-10

8º

8

-10

0

0

5

10

15

20

25

3

2

-1

0

1

2

3

Fitted

Theoretical Quantiles

</figure>


### 13.2 Tree Pruning

The recursive partitioning algorithm describes how to grow the tree, but what is the
optimal size for the tree? The default form of rpart does restrict the size of the tree, but
some intervention is probably necessary to select the best tree size.

One possibility, called a greedy strategy, is to keep partitioning until the reduction in
overall cost (RSS for this type of tree) is not reduced by more than &. However, it is
difficult to set $\&$ in a sensible way. Furthermore, a greedy strategy may stop too soon. For
example, consider data laid out in Table 13.1: Neither the horizontal nor

$x _ { 2 }$

1

2

2

1

$x _ { 1 }$

Table 13.1 There are four data points arranged in $a$
square. The number shows the value of $y$ at that
point.

the vertical split will improve the fit at all. Both splits are required to get a better fit.
However, this drawback is common to most tree-growing strategies as looking more than
one step ahead greatly increases the number of splits that must be considered.

<!-- PageBreak -->

<!-- PageNumber="Trees 283" -->

Nevertheless, it does illustrate the point that the incremental improvements due to each
expansion of the tree may not necessarily be always decreasing.

The observed RSS for a tree will be an underestimate of how well the tree will make
predictions. This phenomenon is common to most models. One generic method of
obtaining a better estimate of predictive ability is cross-validation $\left( \mathrm { C V } \right) .$

For a given tree, leave out one observation, recalculate the tree and use that tree to
predict the left-out observation. For regression, this criterion would be:

$$\sum _ { j = 1 } ^ { n } \left( y _ { j } - j _ { \left( j \right) } \left( x _ { j } \right) \right) ^ { 2 }$$

where $f _ { \left( j \right) } \left( x _ { j } \right) _ { \text { denotes } }$ the predicted value of the tree given the input $x _ { i }$ when case $j$ is not
used in the construction of the tree. For other types of tree, a different criterion would be
used. For classification problems, it might be the deviance. $\mathrm { C V }$ is a more realistic
estimate of how the tree will perform in practice. Leave-out-one cross-validation is
computationally expensive for trees so usually k-fold cross-validation is used. The data is
randomly divided into $k$ roughly equal parts and the remainder is used to predict those
left out. As well as being less expensive computationally than the full leave-out-one
method, it may even work better. One drawback is that the partition is random so that
repeating the method will give different numerical results.

However, there may be very many possible trees if we consider all subsets of a large
tree; cross-validation would just be too expensive. We need a method to reduce the set of
trees to be considered to just those that are worth considering. This is where cost-
complexity pruning is useful. We define a cost-complexity function for trees:

$$C C \left( T r e e \right) = \sum _ { \text { terminindars: } } R S S _ { i } + \lambda \text { \left(number of terminal riodes\right) }$$

If $2$ is large, then the tree that minimizes this cost will be small and vice versa. We can
determine the best tree of any given size by growing a large tree and then pruning it back.
Given a tree of size $n ,$ we can determine the best tree of size $n - 1$ by considering all the
possible ways of combining adjacent nodes. We pick the one that increases the fit
criterion by the least amount. The strategy is akin to backward elimination in linear
regression variable selection except that it can be shown that it generates the optimal
sequence of trees of a given size.

We now use cross-validation to select from this sequence of trees. By default, rpart
selects a tree size that may not be large enough to include all those trees we might want to
consider. We force it to consider a larger tree and then examine the cross-validation
criterion for all the subtrees. The parameter cp plays a similar role to the smoothing
parameter in nonparametric regression and is defined as the ratio of $2$ to the RSS of the
root tree (a tree with no branches). When we call rpart initially, it computes the whole
sequence of trees and we merely need to use functions like printcp to examine the
intermediate possibilities:

\> roze <- rpart (03
., ozone, cp=0.001)
> printcp (roze)
CP nsplit rel error xerror
xstd

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 284" -->

1
0.54570

0

1.000

1.015 0.0771

2

0.07366

1

0.454

0.486 0.0416

3

0.05354

2

0.381

0.411 0.0383

4

0.02676

3

0.327

0.385 0.0358

5

0.02328

4

0.300

0.387 0.0364

6

0.01532

6

0.254

0.377 0.0363

7

0.01091

7

0.239

0.372 0.0364

8

0.00707

8

0.228

0.376 0.0391

9 0.00599

9

0.221

0.375 0.0402

10 0.00497

12

0.203

0.372 0.0408

11 0.00319

17

0.179

0.380 0.0415

12 0.00222

19

0.172

0.378 0.0416

13 0.00144

23

0.164

0.382 0.0420

14 0.00113

24

0.162

0.378 0.0420

15 0.00100

26

0.160

0.379 0.0422

In this table, we see the value of the cp parameter, the number of splits in the tree, the
RSS of the tree divided by the RSS of the null tree, xerror denotes the cross-validated
error which is also scaled by the RSS of the null tree. Since the partition of the data into
10 parts is random, this CV error is also random, which makes the given standard error
useful. The random division also means that if you repeat this command, you will not get
exactly the same answer. We can select the size of the tree by minimizing the value of
xerror and selecting the corresponding value of CP:

$$> \mathrm { r o z } \mathrm { r } < - \mathrm { p r u n e } . \mathrm { r p a r t } \left( \mathrm { r o z e } , 0 . 0 1 0 9 1 \right)$$

This selected tree turns out to be the same as the default choice in this instance. Another
strategy for selecting the tree size is to select the smallest tree with a CV error within one
standard error of the minimum-in this case, $0 . 3 7 2 + 0 . 0 3 6 = 0 . 4 0 8 .$ So we would take the
two-split tree. We can illustrate this by plotting the $\mathrm { C V }$ error and a line showing one
standard deviation above this value as shown in Figure 13.3:

\> plotcp $\left( \mathrm { r o z } \right)$


<figure>
<figcaption>Figure 13.3 Cross-validation plot for ozone tree model.</figcaption>

1

2

3

4

5

6

7

8

9

X-val Relative Error

0.2 0.4 0.6 0.8 1.0 1.2

$

¢

¢

¢

¢

¢

\+

¢

@

Inf

0.2 0.063 0.038 0.025 0.023 0.019 0.013 0.01

cp

</figure>


<!-- PageBreak -->

<!-- PageNumber="Trees 285" -->

You can get some fancier output by:

$$> \mathrm { p o s t } \left( \mathrm { r o z } _ { \prime } \mathrm { f i l e n a n e } = ^ { \prime \prime } \right)$$

If you do not specify the filename, nothing will appear on-screen, but you will find a file
called roz.ps in the directory from which you started R. See Figure 13.4: Let's compare
the result to the earlier linear regression. We achieved an $R ^ { 2 }$ of about 70% using only six
parameters in the previous chapter. We can select a tree with five splits and hence
effectively six parameters and compare them:

\> rozr <- prune.rpart (roz, 0.0154)
> 1-sum (residuals (rozr) ^2) /sum ( (ozone$03-
mean (ozone$03) ) ^2)
[1] 0.74603

We see that the tree model achieved a better fit than the equivalent linear model. Of
course, it would be a mistake to generalize from this, but it is a good demonstration of the
value of trees. $A$ tree fit is piecewise constant over the regions defined by the partitions,
so one might not expect a particularly good fit. However, we can see from this example
that it can outperform linear regression.


### 13.3 Classification Trees

Trees can be used for several different types of response data. For the regression tree, we
computed the mean within each partition. This is just the null model for a regression. We
can extend the tree method to other types of response by fitting an appropriate null model
on each partition. For example, we can extend the idea to binomial, multinomial, Poisson
and survival data by using a deviance, instead of the RSS, as a criterion.

Classification trees work similarly to regression trees except the residual sum of
squares is no longer a suitable criterion for splitting the nodes. The splits should divide
the observations within a node so that the class types within a split are mostly of one kind
(or failing that, just few kinds). We can measure the purity of the node with several
possible measures. Let $n _ { i k }$ be the number of observations of type $k$ within terminal node $i$
and $p _ { i k }$ be the observed proportion of type $k$ within node $i$ i. Let $D _ { i }$ be the measure for node
i so that the total measure is $\Sigma D _ { i }$ ¡. There are several choices for $D _ { i } :$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 2" -->
<!-- PageNumber="286" -->

$$E n d p o i n t = 0 3$$


<figure>
<figcaption>Figure 13.4 Final tree model for the ozone data.</figcaption>

12.0
$n = 3 3 0$
☒

temp.67.5

temp 67.5

7.4
$n = 2 1 4$
☒

20.0
$n = 1 1 6$
☒

ibh>3673.5

ibt<226.5

ibh<3573.5

ibt>226.5

5.1
$n = 1 0 8$

9.7
$n = 1 0 6$
☒

16.0
$n = 5 5$
☒

23.0
$n = 6 1$
☒

$d p g 4 - 9 . 5$

humidity<59 5

doy>306.5

dpg =- 9.5

humidity>59.5

doy<306.5

6.5
$n = 3 5$

11.0
$n = 7 1$

11.0

16.0
$n = 8$

24.0
$n = 5 3$
☒

17.0

$n = 1 0$

$n = 4 5$

ibt<159

vis:55

ibt> $1 5 9$

vis $55

9.1

14.0

23.0
$= 3 6$

27.0
$n = 1 7$

$n = 4 0$

$n = 3 1$

</figure>


### 1. Deviance:

$$D _ { i } = - 2 \sum _ { k } n _ { i k } \log p _ { i k }$$

<!-- PageBreak -->

<!-- PageNumber="Trees 287" -->

2\. Entropy:

$$D _ { i } = - 2 \sum _ { k } p _ { i k } \log p _ { i k }$$

3\. Gini index:

$$D _ { i } = 1 - \sum _ { k } p _ { i k } ^ { 2 }$$

All these measures share the characteristic that they are minimized when all members of
the node are of the same type. The rpart function uses the Gini index by default.

We illustrate the classification tree method in a problem involving the identification of
the sex and species of an historical specimen of kangaroo. We have some training data
consisting of 148 cases with the following variables: there are three possible species,
Giganteus, Melanops and Fuliginosus, the sex of the animal and 18 skull measurements.
The data were published in Andrews and Herzberg (1985). The historical specimen is
from the Rijksmuseum van Natuurlijkee in Leiden which had the following skull
measurements in the same order as in the data:

1115 NA 748 182 NA NA 178 311 756 226 NA NA NA 48 1009
NA 204 593

We have a choice in how we model the response. One possibility is to form a six-level
response representing all possible combinations of sex and species. Another approach is
to form separate trees for identifying the sex and the species. We take the latter approach
below, focusing on the the species. This choice is motivated by the belief that different
features are likely to discriminate the sex and the species so that attempting to model
them both in the same tree might result in a larger, more complex tree that might be less
powerful than two smaller trees. Even so, it would be worth trying the first approach
although we shall not do so here. We start by reading in and specifying the museum case:

\> data (kanga)
> x0 <- c (1115, NA, 748, 182, NA, NA, 178, 311, 756,
226, NA, NA, NA, 48, 1009, NA, 204, 593)

We have missing values for the case to be classified. We have two options. We can build
a tree model that will classify if there are missing values in the input or we can build a
tree model that uses only variables that are observed. If we believe that the missing
values were in some way informative, the first choice would be fine. In this particular
case, that does not seem plausible, so the latter approach is preferred. However, if we
want to build a model that could be used for future unspecified cases, then we would
have to deal directly with the missing values. For this special purpose situation, where we
want to classify one particular kangaroo, this is not a concern.

We exclude all variables that are missing in the test case. We drop sex since we will
not be modeling it yet. We form a convenient data frame:

$$> \mathrm { k a n g a } < - \mathrm { k a n g a } \left[ , c \left( T _ { \prime } , F _ { \prime } ! \text { is.na } \left( x 0 \right) \right) \right]$$

\> kanga [1 : 2, ]

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 288

species basilar. length palate. length palate.width
squamosal . depth
1


<table>
<tr>
<td>giganteus</td>
<td>1312</td>
<td>882</td>
<td>NA</td>
</tr>
<tr>
<td>180</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td rowspan="2">1439</td>
<td rowspan="2">985</td>
<td rowspan="2">230</td>
</tr>
<tr>
<td>giganteus</td>
</tr>
</table>


150

lacrymal. width zygomatic. width orbital. width
foramina. length
1

394

782

249

88

2

416

824

233

100

mandible. length mandible. depth ramus.height

10861

179

591

11582

181

643

We still have missing values in the training set. We have a number of options:

1\. Build a tree model that discretizes the predictors into factors and then treats missing
values as another level of the factors. This might be appropriate if we think missing
values are informative in some way. Information would be lost in the discretization.
For this data, we have no reason to believe that the data is not missing at random and
furthermore we have already decided to ignore the missing values in the test case.

2\. Fill in or estimate the missing values and then build a tree. We could use missing data
fill-in methods as used in other regression problems. This is not easy to implement and
there are concerns about the bias caused by such methods.

3\. The tree-fitting algorithm can handle missing values naturally. If a value for some case
is not available, then it is simply excluded from the criterion. When we want to
classify a new case with missing values, we follow the tree down until we reach a split
which involves a missing value in our new case and take the majority verdict in that
node. A more complicated approach is to allow a second-choice variable for splitting
at a node called a surrogate split. Information on the surrogate splits may be obtained
by using the summary command on the tree object.

4\. Leave out the missing cases entirely.


### We first check where the missing values occur:

\> apply (kanga, 2, function (x) sum (is.na (x)))
species basilar. length palate. length
palate.width
0
1
1
24
squamosal. depth lacrymal. width zygomatic. width
orbital.width
1

0
1
0
foramina. length mandible. length mandible. depth
ramus . height

<!-- PageBreak -->

<!-- PageNumber="Trees 289" -->

0

0

12

0

We observe that the majority of missing values occur in just two variables: mandible
length and palate width. Suppose we throw out those variables and then remove the
remaining missing cases. We compute the pairwise correlation of these variables with the
other variables.

\> round (cor (kanga [ , -
1] , use="pairwise. complete. obs") [ , c (3, $\left. \left. \left. 9 \right) \right] , 2 \right)$
palate.width mandible. length


<table>
<tr>
<td>basilar. length</td>
<td>0.77</td>
<td>0.98</td>
</tr>
<tr>
<td>palate. length</td>
<td>0.81</td>
<td>0.98</td>
</tr>
<tr>
<td>palate. width</td>
<td>1.00</td>
<td>0.81</td>
</tr>
<tr>
<td>squamosal . depth</td>
<td>0.69</td>
<td>0.80</td>
</tr>
<tr>
<td>lacrymal. width</td>
<td>0.77</td>
<td>0.92</td>
</tr>
<tr>
<td>zygomatic. width</td>
<td>0.78</td>
<td>0.92</td>
</tr>
<tr>
<td>orbital.width</td>
<td>0.12</td>
<td>0.25</td>
</tr>
<tr>
<td>foramina. length</td>
<td>0.19</td>
<td>0.23</td>
</tr>
<tr>
<td>mandible. length</td>
<td>0.81</td>
<td>1.00</td>
</tr>
<tr>
<td>mandible.depth</td>
<td>0.62</td>
<td>0.85</td>
</tr>
<tr>
<td>ramus . height</td>
<td>0.73</td>
<td>0.94</td>
</tr>
</table>


We see that these two variables are highly correlated with other variables in the data. We
claim that there is not much additional information in these two variables and we can
reasonably discard them. We do this and then remove the remaining missing cases:

\> newko <- na.omit (kanga [, -c (4, 10) ])
> dim (newko)
[1] 144 10

After excluding these two variables, we only lose four cases more by throwing out all the
missing value cases. Alternatively, suppose we just throw out the missing value cases on
the original data:

\> dim (na.omit (kanga) )
[1] 112 12

We would lose 36 cases by simply throwing out all the missing values. Removing a
combination of variables and cases seems a better choice for this data.

We should also plot the data to see how the classes separate. An example of such a
plot is:

\> plot (foramina. length ~ zygomatic. width, data=newko,
pch=substring (species, 1, 1) )

We see in the left panel of Figure 13.5 that the classes do not separate well, at least for
these two variables. We now fit a classification tree as follows: Because the response

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 290" -->


<figure>
<figcaption>Figure 13.5 Historical kangaroo tree model. The left panel shows the three species, m=melanops, g=giganteus and f=fuliginosus, as they vary with two of the measurements. The right panel shows the chosen tree.</figcaption>

140

foramina.length

120

mm

100

m

80

L

m

60

f

m

700

800

900

1000

1100

zygomatic.width

</figure>


is a factor, classification rather than regression is automatically used. Gini's index is the
default choice of criterion. Here we specify a smaller value of the complexity parameter
$c p$ than the default, so that larger trees are also considered:

\> kt <- rpart (species
., data=newko, cp=0.001)
> printcp (kt)
Root node error: 95/144 =0.66
$n = 1 4 4$


<table>
<tr>
<th>CP</th>
<th>nsplit</th>
<th>rel error</th>
<th>xerror</th>
<th>xstd</th>
</tr>
<tr>
<td>1 0.1789</td>
<td>0</td>
<td>1.000</td>
<td>1.105</td>
<td>0.0561</td>
</tr>
<tr>
<td>2 0.1053</td>
<td>1</td>
<td>0.821</td>
<td>0.979</td>
<td>0.0604</td>
</tr>
<tr>
<td>3 0.0500</td>
<td>2</td>
<td>0.716</td>
<td>0.874</td>
<td>0.0624</td>
</tr>
<tr>
<td>4 0.0211</td>
<td>6</td>
<td>0.516</td>
<td>0.800</td>
<td>0.0631</td>
</tr>
<tr>
<td>5 0.0105</td>
<td>7</td>
<td>0.495</td>
<td>0.853</td>
<td>0.0627</td>
</tr>
<tr>
<td>6 0.0010</td>
<td>8</td>
<td>0.484</td>
<td>0.905</td>
<td>0.0620</td>
</tr>
</table>


The cross-validated error (expressed in relative terms in the rel error column) reaches a
minimum for the six-split tree. We select this tree:

\> ktp <- prune (kt, cp=0.0211)
> ktp
n= 144
node), split, n, loss, Yval, (Yprob)
\* denotes terminal node
1\) root 144 95 fuliginosus (0.340278 0.333333 0.326389)
2\) zygomatic.w>=923 37 13 fuliginosus (0.648649
0.162162 0.189189)

<!-- PageBreak -->

<!-- PageNumber="Trees 291" -->

3\) zygomatic.w< 923 107 65 giganteus (0.233645
0.392523 0.373832)

6\) zygomatic.w>=901 16 3 giganteus (0.125000
0.812500 0.062500) *

7\) zygomatic.w< 901 91 52 melanops (0.252747
0.318681 0.428571)

14\) foramina.1< 98.5 58 33 melanops (0.362069
0.206897 0.431034)

28\) lacrymal.w< 448.5 50 29 fuliginosus (0.420000
0.240000 0.340000)

56\) ramus.h>=628.5 33 14 fuliginosus (0.575758
0.181818 0.242424) *
57\) ramus.h< 628.5 17 8 melanops (0.117647

0.352941 0.529412) *

29\) lacrymal.w>=448.5 8 0 melanops (0.000000
0.000000 1.000000) *

15\) foramina.1>=98.5 33 16 giganteus (0.060606
0.515152 0.424242)
30\) squamosal.d< 182.5 26 10 giganteus (0.076923
0.615385 0.307692)

31\) squamosal.d>=182.5 7 1 melanops (0.000000
0.142857 0.857143) *

\> plot (ktp, compress=T,
uniform=T, branch=0.4, margin=0.1)
> text (ktp)

This tree is not particularly successful as the relative error is estimated as 80% of just
guessing the species. Some of the terminal nodes are quite pure, for example, #29 and
#31, while others retain much uncertainty, for example, $\# 5 6$ and $\# 5 7 .$ We now compute
the misclassification error:

\> (tt <- table (actual=newko$species,
predicted=predict (ktp, type="class") ) )
predicted


<table>
<tr>
<th>actual</th>
<th>fuliginosus</th>
<th>giganteus</th>
<th>melanops</th>
</tr>
<tr>
<td>fuliginosus</td>
<td>43</td>
<td>4</td>
<td>2</td>
</tr>
<tr>
<td>giganteus</td>
<td>12</td>
<td>29</td>
<td>7</td>
</tr>
<tr>
<td>melanops</td>
<td>15</td>
<td>9</td>
<td>23</td>
</tr>
</table>


\> 1-sum (diag (tt) ) /sum (tt)
[1] 0.34028

We see that the error rate is 34%. We might hope to do better. We see that we can
generally correctly identify fuliginosus, but we are more likely to be in error in
distinguishing melanops and giganteus.

A look at the left panel of Figure 13.5 explains why we may have difficulty in
classification. Any single measure will reflect mostly the overall size of the skull. For
example, suppose we wanted to distinguish male human skulls from female human
skulls. Most interesting measures will correlate strongly with size. If we just use one
measure, then the rule will likely be: if the measure is small, then pick male; if it is large

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 292" -->

pick, female. This cannot be expected to work particularly well. There is something about
the relative dimensions of the skulls that ought be more informative.

One possibility is to allow splits on linear combinations of variables. This is allowed
in some classification tree software implementations. An alternative idea is to apply the
method to the principal component scores rather than the raw data. Principal components
(PC) seek out the main directions of variation in the data and might generate more
effective predictors for classification in this example:

\> pck <- princomp (newko [, -1] )
> pcdf <- data.frame (species=newko$species, pck$scores)
> kt <- rpart (species ., pcdf, cp=0.001)
> printcp (kt)
Root node error: 95/144 =0.66
n= 144


<table>
<tr>
<th>CP</th>
<th>nsplit</th>
<th colspan="2">rel error</th>
<th>xerror</th>
<th>xstd</th>
</tr>
<tr>
<td>1 0.4000</td>
<td>0</td>
<td colspan="2">1.000</td>
<td>1.126</td>
<td>0.0552</td>
</tr>
<tr>
<td>2 0.1789</td>
<td>1</td>
<td></td>
<td>0.600</td>
<td>0.621</td>
<td>0.0621</td>
</tr>
<tr>
<td>3 0.0421</td>
<td>2</td>
<td></td>
<td>0.421</td>
<td>0.558</td>
<td>0.0609</td>
</tr>
<tr>
<td>4 0.0105</td>
<td>3</td>
<td colspan="2">0.379</td>
<td>0.568</td>
<td>0.0612</td>
</tr>
<tr>
<td>5 0.0010</td>
<td>5</td>
<td colspan="2">0.358</td>
<td>0.589</td>
<td>0.0616</td>
</tr>
</table>


We find a significantly smaller relative CV error (0.558). Before we can predict the test
case, we need to do some work to remove the missing values, unused variables and apply
the principal component transformation:

\> nx0 <- x0 [! is.na (x0) ]
> nx0 <- nx0 [-c(3, 9) ]
> nx0 <- (nx0-pck$center) /pck$scale
> nx0 %*% pck$loadings
Comp.1 Comp.2 Comp.3 Comp.4 Comp.5

Comp.6 Comp.7
[1,] 499.93 -74.834 -37.632 23.169 3.9564 16.584 -
54.017
Comp.8 Comp.9
[1,] -35.995 -16.705

Our chosen tree is:

\> ktp <- prune.rpart (kt, 0.0421)
> ktp
n= 144
node), split, n, loss, Yval, (Yprob)
\* denotes terminal node
1\) root 144 95 fuliginosus (0.340278 0.333333 0.326389)
2\) Comp.2< - 15.126 49 8 fuliginosus (0.836735
0.040816 0.122449) *

3\) Comp.2> =- 15.126 95 49 giganteus (0.084211
0.484211 0.431579)
6\) Comp.4> =- 9.513 63 24 giganteus (0.111111
0.619048 0.269841)

<!-- PageBreak -->

<!-- PageNumber="Trees 293" -->

12\) Comp.3> =- 18.996 55 17 giganteus (0.090909
0.690909 0.218182) *
13\) Comp.3< - 18.996 8 3 melanops (0.250000
0.125000 0.625000) *
7\) Comp.4< - 9.513 32 8 melanops (0.031250
0.218750 0.750000) *

It is interesting that the first PC is not used. Typically, the first PC represents an overall
average or total size. Other PCs represent contrasts between variables which would
describe shape features in this case. We see that the test case is classified as fuliginosus,
which agrees with the experts. We can also compute the error rate as before:

\> (tt <-
table (newko$species, predict (ktp, type="class") ) )
fuliginosus giganteus melanops


<table>
<tr>
<td>fuliginosus</td>
<td>41</td>
<td>5</td>
<td>3</td>
</tr>
<tr>
<td>giganteus</td>
<td>2</td>
<td>38</td>
<td>8</td>
</tr>
<tr>
<td>melanops</td>
<td>6</td>
<td>12</td>
<td>29</td>
</tr>
</table>


\> 1-sum (diag (tt) ) /sum(tt)
[1] 0.25

We see that the error rate has been reduced to 25%. It would be worth considering other
combinations of predictors in an attempt to reduce the error rate further.

Further Reading: Breiman, Friedman, Olshen, and Stone (1984) is the classic book
on trees. Ripley (1996) and Hastie, Tibshirani, and Friedman (2001) also discuss trees
and compare them to other methods. See also the random forests method described in
Breiman (2001a) that results in more stable assessments of the effects of predictors.


## Exercises

1\. Four hundred three African Americans were interviewed in a study to understand the
prevalence of obesity, diabetes, and other cardiovascular risk factors in central
Virginia. Data is presented in diabetes. Build a regression tree-based model for
predicting glycosolated hemoglobin in terms of the other relevant variables. Interpret
your model. Use the model to predict the glycosolated hemoglobin for a subject with:

id chol stab.glu hdl ratio location age gender
1004 213 72 58 3.3 Buckingham 56 female
height weight frame bp.1s bp.1d bp.2s bp.2d waist hip
64
131 medium
108
55
NA
NA
30 40

time.ppn
720

Glycosolated hemoglobin greater than 7.0 is usually taken as a positive diagnosis
of diabetes. Now build a classification tree for the diagnosis of diabetes and
compare your model to the corresponding regression tree.

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 294" -->

2\. Refer to the pima dataset described in Question 3 of Chapter 2. First take care to deal
with the clearly mistaken observations for some variables.

(a) Fit a tree model with the result of the diabetes test as the response and all the other
variables as predictors.

(b) Perform diagnostics on your model, reporting any potential violations.

(c) Predict the outcome for a woman with predictor values 1, 99, 64, 22, 76, 27, 0.25,
25 (same order as in dataset). How certain is this prediction?

(d) If you completed the logistic regression analysis of the data earlier, compare the
two analyses.

3\. The dataset wbcd is described in Question 2 of Chapter 2.

(a) Fit a tree model with Class as the response and the other nine variables as
predictors.

(b) Use the model to predict the outcome for a new patient with predictor variables 1,
1, 3, 2, 1, 1,4, 1, 1 (same order as above).

(c) Suppose that a cancer is classified as benign $i f \quad p > 0 . 5$ and malignant $i f \quad p < 0 . 5 .$
Compute the number of errors of both types that will be made $\mathrm { i f }$ this method is
applied to the current data with the reduced model.

(d) Suppose we change the cutoff to 0.9 so that $p < 0 . 9$ is classified as malignant and
$p > 0 . 9$ as benign. Compute the number of errors in this case. Discuss the issues in
determining the cutoff.

(e) It is usually misleading to use the same data to fit a model and test its predictive
ability. To investigate this, split the data into two parts and assign every third
observation to a test set and the remaining two thirds of the data to a training set.
Use the training set to determine the model and the test set to assess its predictive
performance. Compare the outcome to the previously obtained results.

(f) If you completed the logistic regression analysis of the data earlier, compare the
two analyses.

4\. The dataset uswages is drawn as a sample from the Current Population Survey in 1988.

(a) Build a tree regression model to predict wage.

(b) Check the diagnostics of your model.

(c) Use your model to predict the wage of a subject with predictor characteristics 12,
33, 0, 1, 0, 0, 0, 1, 0 where the values occur in the same order as in the data frame.

(d) Conduct a quick linear model analysis and compare the results with the tree model.
In particular, what do the two models say about the relationship between the
predictors and the response?

5\. The dvisits data comes from the Australian Health Survey of 1977-78 and con-sist of
5190 single adults where young and old have been oversampled.

(a) Build a Poisson tree model with doctorco as the response and sex, age, agesq,
income, levyplus, freepoor, freerepa, illness, actdays, hscore, chcond1 and chcond2
as possible predictor variables. Consult the rpart documentation for how to specify
a Poisson response.

(b) Check the diagnostics.

<!-- PageBreak -->

<!-- PageNumber="Trees 295" -->

(c) What sort of person would be predicted to visit the doctor the most under your
selected model?

(d) For the last person in the dataset, compute the predicted probability distribution for
their visits to the doctor, i.e., give the probability they visit 0, 1, 2 etc. times.

(e) If you have previously completed the analysis of this data in the exercises for
Chapter 3, compare the results.

<!-- PageBreak -->


## CHAPTER 14 Neural Networks

Neural networks (NN) were originally developed as an attempt to emulate the human
brain. The brain has about $1 . 5 \times 1 0 ^ { 1 0 }$ neurons each with 10 to $1 0 ^ { 4 }$ connections called
synapses. The speed of messages between neurons is about 100 m/sec which is much
slower than CPU speed. Given that our fastest reaction time is around 100 ms and neuron
computation time is 1-10 ms, then the number of steps must be less than 100. This is
inconceivable small for a sequential computation, even in machine code; therefore, the
brain must be computing in parallel.

The original idea behind neural networks was to use a computer-based model of the
human brain to perform complex tasks. We can recognize people in fractions of a second,
but this task is difficult for computers. So why not make software more like the human
brain?

Despite the promise, there are some drawbacks. The brain model of connected
neurons, first suggested by McCulloch and Pitts (1943), is too simplistic given more
recent research. There are also more controversial philosophical questions about how any
algorithmic computation can mimic some of the functions of the brain. This is discussed
in Penrose (1989). For these and other reasons, the methodology is more properly called
artificial neural nets. As with artificial intelligence, the promise of NNs is not matched by
the reality of their performance. Arnold Schwarzenegger's brain in The Terminator was
powered by a neural net, but the true accomplishments of NNs are much more modest.
Nevertheless, they can be useful as we shall see.

NNs are used for various purposes. They can be used as biological models, which was
the original motivation. They can also be used as a hardware implementation for adaptive
control. But the area of application we are interested in is data analysis. There are NN
models that rival the regression, classification and clustering methods normally used by
statisticians.

A perceptron is a model of a neuron and is the basic building block of a neural
network as depicted in Figure 14.1. The output $x _ { 0 } ,$ is determined from inputs $x _ { i } :$

$$x _ { 0 } = f _ { 0 } \left( \sum _ { i n p u r s i } w _ { i } x _ { i } \right)$$

where $f _ { o }$ is called the activation function. Standard choices include the identity, logistic
and indicator functions. The $w _ { i }$ are weights. The NN learns the weights from the data. $A$
statistician would prefer to say that the NN estimates the parameters from the data. Thus
$N N$ terminology differs from statistical usage in ways that can be confusing.

<!-- PageBreak -->

<!-- PageNumber="297" -->
<!-- PageHeader="Neural networks" -->


<figure>
<figcaption>Figure 14.1 A perceptron.</figcaption>

Inputs

Output

</figure>


### 14.1 Statistical Models as NNs

Three common statistical models are analogous to the single perceptron NN. For multiple
linear regression:

$$y = \sum _ { i } w _ { i } x _ { i }$$

So here $f _ { 0 }$ is the identity function. We can define $x _ { 1 } = 1$ to get an intercept term. The NN
alternative is to attach a weight, called a bias, to each neuron:

$f \left( x \right) = x + \theta$

A statistician would call the bias 0 an intercept.

Logistic regression also fits easily within this framework if we define $f _ { o }$ as the logistic
function. Of course, such an NN is not exactly equivalent to the corresponding statistical
model unless that NN is fit in a very particular way.

Linear discriminant analysis is used to classify a binary response. Suppose there are
two groups encoded by $y = 0$ or $y = 1 .$ In this case $f _ { 0 }$ is the indicator function. Again the NN
and and statistical approach are not exactly equivalent unless the same fitting procedures
are used.

Other common statistical models can be approximated by adding more neurons
Multivariate multiple linear regression with a bivariate response is $Y = X \beta + \varepsilon$ where $\bar { Y } ,$ $X ,$
B, & are all matrices and is depicted as an NN in Figure 14.2: Polynomial regression can
be mimicked by using different activation function and more than one layer of neurons as
seen in the second panel of Figure 14.2.


### 14.2 Feed-Forward Neural Network with One Hidden Layer

The feed-forward neural network with one hidden layer is the most common choice for
regression-like modeling applications. It takes the form:

$$y _ { 0 } = \phi _ { 0 } \left( \sum _ { h } w _ { h o } 0 _ { h } \left( \sum _ { i } w _ { i h } x _ { i } \right) \right)$$

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with R 298" -->

The activation functions for the hidden layer, "/ are almost always logistic. If identity
functions are used for the hidden layer and for the output, the resulting NN is quite
similar to the partial least squares approach of Wold, Ruhe, Wold, and Dunn (1984). We
will set one of our inputs to be constant at one so as to allow for an intercept/bias term.
The choice of output activation function depends on the nature of


<figure>
<figcaption>Figure $1 4 . 2 \quad N N$ equivalents of multivariate linear regression (shown on the top) and polynomial regression (shown on the bottom).</figcaption>

$x _ { 1 }$

$\mathrm { y } _ { \mathrm { I } }$

$x _ { 2 }$

$x _ { 3 }$

$\mathrm { y } _ { 2 }$

1

$X$

$y$

$X$

2

$X$

</figure>


the response. For continuous unrestricted output, an identity function is appropriate while
for response bounded between zero and one, such as a binomial proportion, a logistic
function should be used. We show the feed-forward NN in Figure 14.3.

<!-- PageBreak -->

<!-- PageNumber="299" -->
<!-- PageHeader="Neural networks" -->


<figure>
<figcaption>Figure 14.3 Feed-forward neural network with one hidden layer.</figcaption>

$x _ { 1 }$

$\mathrm { y } _ { \mathrm { l } }$

$x _ { 2 }$

$y _ { 2 }$

</figure>


Sometimes a direct connection between the inputs and outputs is added called a skiplayer
connection. More complexity can be added using more layers or feedbacks although this
not always beneficial to the practical performance of the NN.

NNs can be elaborated to perform as universal approximators. This has been shown by
authors such as Hornik, Stinchcombe, and White (1989). However, these results are of
little practical value when confronted with a finite amount of data subject to noise. We
must use the data estimate the parameters of the model or, in NN-speak, use the data to
train the network. The weights $w$ are chosen to minimize a criterion, such as:

$$E = \sum \left( y - j \right) ^ { 2 }$$

where $y$ is the observed output and $\widehat { \mathcal{Y} }$ is the predicted output. A different criterion would
be more suitable for categorical responses.

NN researchers have developed different methods of estimation motivated by brain
models of learning. These methods have generally not compared well with the numerical
analysis-based approaches which are generally faster and more reliable. Nevertheless, in
all but the most simple NNs, the criterion is a complicated function of the parameters.
The function often has many local minima making it difficult to find the true minimum.
$A$ statistician, with no pretensions to mimicking brain functions, would be inclined to use
standard methods of numerical analysis such as quasiNewton methods, conjugate
gradients or simulated annealing. The nnet function in R uses the BFGS method, as
described in Fletcher (1987).


### 14.3 NN Application

We apply the NN method to the ozone data analyzed in previous chapters. The nnet
package, due to Venables and Ripley (2002), must be loaded first:

\> library (nnet)

\> data (ozone)

<!-- PageBreak -->


## Extending the linear model with $\mathrm { R }$ 300

We start with just three variables for simplicity of exposition as in previous analyses. We
fit a feed-forward NN with one hidden layer containing two units with a linear output
unit:

\> nnmdl <- nnet (03 ~ temp + ibh + ibt, ozone, size=2,
linout=T)
\# weights: 11
initial value 65447.874069
final value 21115.406061
converged

The RSS of 21,115 is equal to $\sum _ { i } \left( y _ { i } - y \right) ^ { 2 }$ the fit is not any better than the null
model. If you repeat this, your result may differ slightly because of the random starting
point of the algorithm, but you will likely get a similar result. The problem lies with the
initial selection of weights. It is hard to do this well when the variables have very
different scales. The solution is to rescale the data to have zero mean and unit variance:

$$> s x < - \quad s c a l e \left( o z o n e \right)$$

Because a random starting point is used, the algorithm will not necessarily converge to
the same solution if the fitting is repeated. Now we try refitting the model. We repeat this
100 times because of the random starting point. Here we find the best fit of the 100
attempts:

\> bestrss <- 10000
> for (i in 1:100) {
nnmdl <- nnet(03 ~ temp + ibh + ibt, sx, size=2,
linout=T, trace=F)
cat (nnmdl$value, "\n")
if (nnmdl$value < bestrss) {
bestnn <- nnmdl
bestrss <- nnmdl$value
} }
> bestnn$value
[1] 88.031

The criterion function has 11 parameters or weights and has multiple minima. The
problem is that we can never really know whether we have found the true minimum. $\mathrm { A l l }$
we can do is keep trying and stop if we do not find anything better after some number of
attempts. The best strategy is not clear, although one can do better than the simple
approach we have used above. Examine the estimated weights:

\> summary (bestnn)
a 3-2-1 network with 11 weights
options were-linear output units
b->h1 i1->h1 i2->h1 i3->h1
1.12 -0.98 0.84 0.29
b->h2 i1->h2 12->h2 i3->h2

<!-- PageBreak -->

<!-- PageHeader="Neural networks 301" -->


<table>
<tr>
<td>137.89</td>
<td>-74.74</td>
<td>240.66</td>
<td>137.89</td>
</tr>
<tr>
<td>b-&gt;o</td>
<td>h1-&gt;o</td>
<td colspan="2">h2-&gt;o</td>
</tr>
<tr>
<td>2.59</td>
<td>-4.41</td>
<td>0.67</td>
<td></td>
</tr>
</table>


The notation i2->h1, for example, refers to the link between the second input variable and
the first hidden neuron, b refers to the bias, which takes a constant value of one. We see
that there is one skip-layer connection, $b - > o ,$ from the bias to the output.

NNs have some drawbacks relative to competing statistical models. The parameters of
an NN are uninterpretable whereas they often have some meaning in statistical models.
Furthermore, NNs are not based on a probability model that expresses the structure and
variation. As a consequence, there are no standard errors. It is possible to graft some
statistical inference onto this NN model, but it is not easy. The bootstrap is a possible
way of implementing this. The $R ^ { 2 }$ for the fit is:

$$> 1 - 8 8 . 0 3 / \sin \left( \left( s x \left[ , 1 \right] - m e a n \left( s x \left[ , 1 \right] \right) \right) \quad 2 \right)$$

[1] 0.73243

which is very similar to the additive model fit for these predictors.

Although the NN weights may be difficult to interpret, we can get some sense of the
effect of the predictors by observing the marginal effect of changes in one or more
predictor as other predictors are held fixed. Here, we vary each predictor individually
while keeping the other predictors fixed at their mean values. Because the data has been
centered and scaled for the NN fitting, we need to restore the original scales. The fits are
shown in Figure 14.4:

\> ozmeans <- attributes (sx) $"scaled: center"
> ozscales <- attributes (sx) $"scaled : scale"
> xx <- expand.grid(temp=seq (-3, 3,0.1) , ibh=0, ibt=0)
> plot (xx$temp*ozscales [ 'temp' ] +ozmeans [ ' temp ' ] ,
predict (bestnn, new=xx) \*ozscales [ ' 03 ' ] +ozmeans [ ' 03 ' ] ,
xlab="Temp", ylab="03")
> xx <- expand.grid(temp=0, ibh=seq(-3,3,0.1), ibt=0)
> plot (xx$ibh\*ozscales ['ibh' ] +ozmeans [ ' ibh' ] ,
predict (bestnn, new=xx) \*ozscales [ ' 03' ] +ozmeans [ ' 03 ' ] ,
xlab="IBH", ylab="03")
> xx <- expand.grid(temp=0, ibh=0, ibt=seq(-3, 3, 0 .1) )
> plot (xx$ibt\*ozscales ['ibt' ] +ozmeans [ 'ibt' ] ,
predict (bestnn, new=xx) *ozscales [ ' 03' ] +ozmeans [ ' 03 ' ] ,
xlab="IBT", ylab="03")

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 302" -->


<figure>
<figcaption>Figure 14.4 Marginal effects of predictors for the $N N \quad f i t .$ Other predictors are held fixed at their mean values.</figcaption>

0000000000000900600000600

CL

A

5

R

₫

8g

89

0

10

\#

\-

20

00

00

100

2000

Q

$\begin{array}{} { \text { Sicap } } \\ { \text { Ifiti } } \end{array}$

0

100

200

300 40

Temp

BT

</figure>


We see some surprising discontinuities in the plots which do not seem consistent with
what we might expect for the effect of these predictors. If we examine the weights for
this NN above, we see several large values. Consider that all the variables have been
scaled to mean zero and variance one. Products formed using the large weights will vary
substantially. The situation is analogous to the collinearity problem in linear regression
where unreasonably large regression coefficients are often seen. The NN is choosing
extreme weights in order to optimize the fit, but the predictions will be unstable,
especially for extrapolations.

We can use a penalty function, as with smoothing splines, to obtain a more stable fit.
Instead of minimizing $E ,$ we minimize:

$$E + 2 \sum _ { i } w _ { i } ^ { 2 }$$

In NN terms, this is known as weight decay. The idea is similar to ridge regression. Let's
try $2 = 0 . 0 0 1$ for 100 NN model fits:

\> bestrss <- 10000

\> for (i in 1:100) {
nnmdl <- nnet (03 ~ temp+ibh+ibt, sx,
size=2, linout=T,
decay=0. 001, trace=F)
cat (nnmdl$value, "\n")
if (nnmdl$value < bestrss) {
bestnn <- nnmdl
bestrss <- nnmdl$value
} }

\> bestnn$value

[1] 92.055

<!-- PageBreak -->

<!-- PageNumber="303" -->
<!-- PageHeader="Neural networks" -->

The value of the best RSS is somewhat larger than before. We expect this since weight
decay sacrifices some fit to the current data to obtain a more stable result. We repeat the
assessment of the marginal effects as before and display the results in Figure 14.5:

\> xx <- expand.grid(temp=seq(-3, 3,0.1), ibh=0, ibt=0)
> plot (xx$temp*ozscales [ 'temp' ] +ozmeans [ ' temp' ] ,
predict (bestnn, new=xx) \*ozscales [ ' 03 ' ] +ozmeans [ ' 03 ' ] ,
xlab="Temp", ylab="03")
> xx <- expand.grid(temp=0, ibh=seq(-3,3,0.1), ibt=0)
> plot (xx$ibh\*ozscales [ ' ibh' ] +ozmeans [ ' ibh ' ] ,
predict (bestnn, new=xx) \*ozscales [ ' 03' ] +ozmeans [ ' 03 ' ] ,
xlab="IBH", ylab="03")
> xx <- expand.grid(temp=0, ibh=0, ibt=seq (-3, 3,0.1) )
> plot (xx$ibt\*ozscales ['ibt' ] +ozmeans ['ibt' ] ,
predict (bestnn, new=xx) *ozscales [' 03' ] +ozmeans [
'03'], xlab="IBT", ylab="03")


<figure>
<figcaption>Figure 14.5 Marginal effects of predictors for the $N N \quad f i t$ with weight decay. Other predictors are held fixed $a t$ their mean values.</figcaption>

ச

8

Q

₪

0

8

0

2

5

2

0

8

8

$8$

000000009
0

4

.

.

0

2

9

D

0

0

\-

9

5

100

-2000 0 2:00

0000

0

100 200 300 401

$\mathrm { r e } = \varphi$

IBH

BT

</figure>


We see that the fits are now plausibly smooth. Note that ibh is strictly positive in practice
so the strange behavior for negative values is irrelevant. Compare these plots to Figure
12.2. The shapes are similar for temperature and ibh. The ibt plot looks quite different
although we have no way to assess the significance of any of the terms in the NN fit.

NNs have interactions built in so one should also look at these. We could produce
analogous plots to those in Figure 14.5 by varying two predictors at a time.

Now let's look at the full dataset. We use four hidden units because there are now
more inputs.

\> bestrss <- 10000
> for (i in 1:100) {
nnmdl <- nnet (03 ~ . , sx, size=4, linout=T, trace=F)

<!-- PageBreak -->

<!-- PageHeader="Extending the linear model with $\mathrm { R }$ 304" -->

cat (nnmdl$value, $\left. \mathfrak{n} \setminus \mathbb{T} ^ { \prime \prime } \right)$
if (nnmdl$value < bestrss)
bestnn <- nnmdl
bestrss <- nnmdl$value
} }
\> 1-bestnn$value/sum ( (sx [,1]-mean (sx[,1] ))^2)
[1] 0.85063

The fit is good and there may be better minimum than we have found and increasing the
number of hidden units would always improve the fit. The fit can be compared to those in
previous chapters. The $R ^ { 2 }$ for the linear and tree model fits was substantially smaller, but
these approaches place a premium on simplicity and interpretability. The fit for the
corresponding additive model was better, but not quite as good as the NN. But the
additive model also has the interpretability that the NN lacks. Finally, the MARS model
fit better and was also interpretable.

Of course, it would be rash to draw firm conclusions from just one dataset.
Furthermore, the value of the modeling approaches needs to be judged within the context
of the particular problem. If explanation is the main goal of the data analysis, NNs are not
a good choice. If prediction is the objective, we cannot judge just by the fit to the data we
have now. It is more important how the model performs on future observations. We do
not have fresh data here as we have used it all to fit the data. Some studies have withheld
data for use in testing the prediction performance of the models considered. NNs have
been generally competitive in these studies but by no means dominant.


### 14.4 Conclusion

NNs, as presented here, are a controlled flexible class of nonlinear regression models. By
adding more hidden units we can control the complexity of the model in a measured way
from relatively simple models up to models suitable for large datasets with complex
structure. NNs are also attractive because they require less expertise to use successfully
compared to statistical models. Nevertheless the user must still pay attention to basic
statistical issues involving transformation and scaling of the data and outliers and
influential points. See Faraway and Chatfield (1998) for an example of the application of
neural networks and how they compare with statistical methods.

NNs are generally good for prediction but bad for understanding. The NN weights are
almost uninterpretable. Although one can gain some insight from plotting the marginal
effect of predictors, the NN inevitably introduces complex interactions that often do not
reflect reality. Furthermore, without careful control, the NN can easily overfit the data
resulting in overoptimistic predictions.

NNs are quite effective for large complex datasets compared to statistical methods
where the burden of developing an appropriate sampling model can sometimes slow or
even block progress. NNs do lack good statistical theory for inference, diagnostics and
model selection. Of course, they were not developed with these statistical considerations
in mind, but experience shows that such issues are often important.

<!-- PageBreak -->

<!-- PageNumber="305" -->
<!-- PageHeader="Neural networks" -->

NNs can outperform their statistical competitors for some problems provided they are
carefully used. However, one should not be fooled by the evocative name, as NNs are just
another tool in the box.

Further Reading: See Ripley (1996), Bishop (1995), Haykin (1998), Neal (1996) and
Hertz, Krogh, and Palmer (1991) for more on NNs.


### Exercises

This book has covered a wide range of statistical methods. For some datasets, only one
method may be applicable, but for some others, we have a wide variety of choices. For
continuous, binary or even count response data with some number of predictors, we can
choose between:

1\. Generalized linear models

2\. Generalized additive models and associated methods

3\. Trees

4\. Neural networks

These methods have their strengths and weaknesses. It is not possible to claim that any
one method dominates. Even so, we might hope to intuit what method might work well
for a particular dataset. One way to gain an understanding of the relative value of these
datasets is by the use of case studies. We want to make two sorts of comparisons:

Quantitative Does one method fit or predict better than another? Unfortunately, adding
complexity to a model does tend to make it fit the current data better, but is no reliable
indication of whether it will predict future data well. One way to avoid this problem is to
reserve a portion of the data for testing your chosen model. $A$ random subset of the data
is selected and put to one side. The remaining data is used to select and fit the model. The
model is then used to predict the response in the test set.

Qualitative Sometimes the purpose of a statistical analysis is to gain an understanding of
the relationship between the variables. A good numerical fit to the data is then not helpful
unless it can be intuitively understood. Judging the success of a method in this sense is
necessarily more subjective.

Several of the datasets we have already used in previous exercises are suitable for case
studies comparing the performance of the competing methods. We recommend the
following datasets for this purpose: diabetes, pima, wbcd, uswages, dvisits, fat and
motorins.

<!-- PageBreak -->

<!-- PageBreak -->


## APPENDIX A Likelihood Theory

This appendix is just an overview of the likelihood theory used in this book. For greater
detail or a more gentle introduction, the reader is advised to consult a book on theoretical
statistics such as Cox and Hinkley (1974), Bickel and Doksum (1977) or Rice (1998).


### A.1 Maximum Likelihood

Consider $n$ independent discrete random variables, $Y _ { 1 } , \ldots , Y _ { n } ,$ with probability distribution
function $f \left( y | \theta \right)$ where $\theta$ is the, possibly vector-valued, parameter. Suppose we observe
$y = \left( y _ { 1 } , \ldots , y _ { n } \right) ^ { I } ,$ then we define the likelihood as:

$$P \left( Y = y \right) = \prod _ { i = 1 } ^ { n } f \left( y _ { i } | \theta \right) = L \left( \theta | y \right)$$

So the likelihood is a function of the parameter(s) given the data and is the probability of
the observed data given a specified value of the parameter(s).

For continuous random variables, $Y _ { 1 } , \ldots .$ , $Y _ { n } ,$ with probability density function $f \left( y | \theta \right) ,$ we
recognize that, in practice, we can only measure or observe data with limited precision.
We may record $y _ { i } ,$ but this effectively indicates an observation in the range $\left[ y _ { i } ^ { I } , y _ { i } ^ { H } \right] _ { S O }$ that:

$$P \left( Y _ { i } = y _ { i } \right) = P \left( y _ { i } ^ { l } \leq y _ { i } ^ { y } \leq y _ { i } ^ { y } \right) = \int _ { y _ { i } ^ { j } } ^ { y _ { i } ^ { j } } f \left( u | \theta \right) d u \approx f \left( y _ { i } | \theta \right) \delta _ { i }$$

where o; = yf- y.We can now write the likelihood as:

$$L \left( \theta | y \right) \approx \prod _ { i = 1 } ^ { n } f \left( y _ { i } | \theta \right) \prod _ { i = 1 } ^ { n }$$

Now provided that $\delta _ { i }$ is relatively small and does not depend on 0, we may ignore it and
the likelihood is the same as in the discrete case.

As an example, suppose that $Y$ is binomially distributed $B \left( n , p \right) .$ The likelihood is:

$$L \left( p | y \right) = \left( \begin{array}{} { n } \\ { y } \end{array} \right) p ^ { y } \left( 1 - p \right) ^ { n - y }$$

The maximum likelihood estimate (MLE) is the value of the parameter(s) that gives the
largest probability to the observed data, or in other words, maximizes the likelihood
function. The value at which the maximum occurs, $\widehat { \theta } _ { \mathrm { s i s } }$ the maximum likelihood

<!-- PageBreak -->

<!-- PageHeader="Appendix A 308" -->

estimate. In most cases, it is easier to maximize the log of likelihood function,
$l \left( \theta | \mathrm { y } \right) = \log L \left( \theta | y \right) .$ Since $\log$ is a monotone increasing function, the maximum occurs at the
same ê.

In a few cases, we can find an exact analytical solution for $\widehat { \mathfrak{g} }$ 0.For the binomial, we
have the log-likelihood:

$$l \left( p | y \right) = \log \left( \begin{array}{} { n } \\ { y } \end{array} \right) + y \log p + \left( n - y \right) \log \left( 1 - p \right)$$

The score function, $u \left( \theta \right) ,$ is the derivative of the log-likelihood with respect to the
parameters. For this example, we have:

$$u \left( p \right) = \frac { d l \left( p | y \right) } { d p } = \frac { y } { p } - \frac { n - y } { 1 - p }$$

We can find the maximum likelihood estimate $\ddot { P } _ { b }$ solving $u \left( p \right) = 0 .$ We get $\widehat { p } = y / n _ { \cdot \mathrm { W } _ { \mathrm { C } } }$
should also verify that this stationary point actually represents a maximum.

Usually we want more than an estimate; some measure of the uncertainty in the
estimate is valuable. This can be obtained via the Fisher information which is:

$$I \left( \theta \right) = \mathrm { v a r } u \left( \theta \right) = - E \frac { \partial ^ { 2 } I \left( \theta \right) } { \partial \theta \partial \theta ^ { T } }$$

If there is more than one parameter, $I \left( \theta \right)$ will be a matrix. The information at $\widetilde { \mathfrak{g} }$ the
second derivative at the maximum. Large values indicate high curvature so that the
maximum is well defined and even close alternatives will have much lower likelihood.
This would indicate a high level of confidence in the estimate. One can show that the
variance of $\ddot { \theta } _ { c a n }$ be estimated by:

$$\mathrm { v a r } \left( \ddot { \theta } \right) = I ^ { - 1 } \left( \ddot { \theta } \right)$$

under mild conditions. Sometimes it is difficult to compute the expected value of the
matrix of second derivatives. As an alternative, the observed, rather than expected, value
at $\ddot { \theta } _ { \mathrm { m a v } }$ be used instead. For the binomial example this gives:

$$p = \widetilde { p } \left( 1 - \dot { p } \right) / n$$

We illustrate these concepts by plotting the log-likelihood for two binomial datasets: one
where $n = 2 5 ,$ $y = 1 0$ and another where $n = 5 0 ,$ $y = 2 0 .$ We construct the log-likelihood
function:

$$> \log 1 i k < - \text { function } \left( p , y , n \right) \text { lchoose } \left( n , y \right) + y ^ { * } 1 0 g \left( p \right) +$$
$\left( n - y \right) * \log \left( 1 - p \right)$

For ease of presentation, we normalize by subtracting the log-likelihood at the maximum
likelihood estimate:

<!-- PageBreak -->

<!-- PageHeader="Appendix A 309" -->

\> nloglik <- function (p, y, n) loglik (p, y, n) -
$\mathrm { l o g l i k } \left( y / n , y , n \right)$

Now plot the two log-likelihoods, as seen in Figure A.1:

$$> p r < - \quad s e q \left( 0 . 0 5 , 0 . 9 5 , b y = 0 . 0 1 \right)$$

\>
matplot (pr, cbind (nloglik (pr, 10,25) , nloglik (pr, 20,50) ),t
ype="1",

$$\left. x l a b = ^ { \prime \prime } p ^ { \prime \prime } , y l a b = ^ { \prime \prime } l o g - l i k e l i h o o d ^ { \prime \prime } \right)$$

We see that the maximum occurs at $p = 0 . 4$ in each case at a value of zero because of the
normalization. For the larger sample, we see greater curvature and hence more
information.


<figure>
<figcaption>Figure $A .$ 1 Normalized binomial log- likelihood for $n = 2 5 ,$ $y = 1 0$ shown with $a$ solid line and $n = 5 0 ,$ $y = 2 0$ shown with $a$ dotted line.</figcaption>

0

-10

log-likelihood

-30

-50

0.2

0.4

0.6

0.8

$p$

</figure>


<!-- PageBreak -->

<!-- PageHeader="Appendix A 310" -->

Examples where likelihood can be maximized explicitly are confined to simple cases.
Typically, numerical optimization is necessary. The Newton-Raphson method is the most
well-known technique. Let $\theta _ { 0 }$ be an initial guess at 0, then we update using:

$\theta _ { 1 } = \theta _ { 0 } - H ^ { - 1 } \left( \theta _ { 0 } \right) u \left( \theta _ { 0 } \right)$

where $H$ is the Hessian matrix of second derivatives:

$$H \left( \theta \right) = \frac { \partial ^ { 2 } l \left( \theta \right) } { \partial \theta \partial \theta ^ { T } }$$

We iterate this method, putting $\theta _ { 1 }$ in place of $\theta _ { 0 }$ and so on, until the procedure (hopefully)
converges. This method works well provided the log-likelihood is smooth and convex
around the maximum and that the initial value is reasonably close. In less well-behaved
cases, several things can go wrong:

· The likelihood has multiple maxima. The maximum that Newton-Raphson finds will
depend on the choice of initial estimate. If you are aware that multiple maxima may
exist, it is advisable to try multiple starting values to search for the overall maximum.
The number and choice of these starting values is problematic. Such problems are
common in fitting neural networks, but rare for generalized linear models.

· The maximum likelihood may occur at the boundary of the parameter space. This
means that perhaps
$u \left( 6 \right) \neq 0 ,$
which will confuse the Newton-Raphson method.
Mixed effect models have several variance parameters. In some cases, these are
maximized at zero, which causes difficulties in the numerical optimization.

· The likelihood has a large number of parameters and is quite flat in the neighborhood of
the maximum. The Newton-Raphson method may take a long time to converge.

The Fisher scoring method replaces $H$ with -I and sometimes gives superior re-sults.
This method is used in fitting GLMs and is equivalent to iteratively reweighted least
squares.

A minimization function that uses a Newton-type method is available in $R .$ We
demonstrate its use for likelihood maximization. Note that we need to minimize $- l$
because nlm minimizes, not maximizes:

\> f <- function (x) -loglik (x, 10,25)
> mm <- nlm (f, 0.5, hessian=T)

We use a starting value of 0.5 and find the optimum at:

\> mm$estimate
[1] 0.4

The inverse of the Hessian at the optimum is equal to the standard estimate of the
variance:

$$> c \left( 1 / m m s h e s s i a n , 0 . 4 ^ { * } \left( 1 - 0 . 4 \right) / 2 5 \right)$$

[1] 0.0096016 0.0096000

<!-- PageBreak -->

<!-- PageHeader="Appendix A 311" -->

Of course, this calculation is not necessary for the binomial, but it is useful for cases
where exact calculation is not possible.

$$A . 2 \quad H y p o t h e s i s \quad T e s t i n g$$

Consider two nested models, a larger model $\Omega$ and a smaller model @. Let $\widehat { \theta } _ { \mathrm { f a b e } }$ the
maximum likelihood estimate under the larger model, while $\ddot { \theta } _ { \mathrm { c o l } }$ the correspond-ing
value when 0 is restricted to the range proscribed by the smaller model. The likelihood
ratio test statistic is:

$$2 \log \left( L \left( \widehat { \theta } _ { 0 } \right) / L \left( \widehat { \theta } _ { \Omega } \right) \right) = 2 \left( l \left( \widehat { \theta } _ { 0 } \right) - l \left( \widehat { \theta } _ { \Omega } \right) \right)$$

Under some regularity conditions, this statistic is asymptotically distributed $x ^ { 2 }$ with
degrees of freedom equal to the difference in the number of identifiable parameters in the
two models. The approximation may not be good for small samples and may fail entirely
if the regularity conditions are broken. For example, if the smaller model places some
parameters on the boundary of the parameter space, the $x ^ { 2 }$ may not be valid. This can
happen in mixed effects models when testing whether a particular variance component is
$z e r o .$

The Wald test may be used to test hypotheses of the form $H _ { 0 } : \theta = \theta _ { 0 }$ and the test statistic
takes the form:

$$\left( \theta - \theta _ { 0 } \right) ^ { T } I \left( \theta \right) \left( \widehat { \theta } - \theta _ { 0 } \right)$$

Under the null, the test statistic has approximately a $x ^ { 2 }$ distribution with degrees of
freedom equal to the number of parameters being tested. Quite often, one does not wish
to test all the parameters and the Wald test is confined to a subset. In particular, if we test
only one parameter, $H _ { 0 } :$ $\theta i = \theta i 0 ,$ the square root of the Wald test statistic is simply:

$$z = \frac { \widehat { \theta } _ { i } - \theta _ { i 0 } } { s e \left( \widehat { \theta } _ { i } \right) }$$

This is asymptotically normal. For a Gaussian linear model, these are the t-statistics and
have an exact $t$ t-distribution, but for generalized linear and other models, the normal
approximation must suffice.

The score test of the hypothesis $H _ { 0 } : \theta = \theta _ { 0 }$ uses the statistic:

$u \left( \theta _ { 0 } \right) ^ { T } \Gamma ^ { 1 } \left( \theta _ { 0 } \right) u \left( \theta _ { 0 } \right)$

and is asymptotically $x ^ { 2 }$ distributed with degrees of freedom equal to the number of
parameters being tested.

There is no uniform advantage to any of these three tests. The score test does not
require finding the maximum likelihood estimate, while the likelihood ratio test needs
this computation to be done for both models. The Wald test needs just one maximum
likelihood estimate. However, although the likelihood ratio test requires more
information, the extra work is often rewarded. Although the likelihood ratio test is not

<!-- PageBreak -->

<!-- PageHeader="Appendix A 312" -->

always the best, it has been shown to be superior in a wide range of situations. Unless one
has indications to the contrary or the computation is too burdensome, the likelihood ratio
test is the recommended choice.

These test methods can be inverted to produce confidence intervals. To compute a
$1 0 0 \left( 1 - \alpha \right) \%$ confidence interval for 0, we calculate the range of hypothesized $\theta _ { 0 }$ such that
$H _ { 0 } : \theta _ { 0 } = 0$ would not be rejected at the a level. The computation is simple for the single-
parameter Wald test where the confidence interval for $\theta _ { i }$ is:

$$\ddot { \theta } _ { i } \pm z ^ { 1 - \alpha / 2 } s e \left( \dot { \theta } _ { i } \right)$$

where $z$ is the appropriate quantile of the normal distribution. The computation is trickier
for the likelihood ratio test. If we are interested in a confidence interval for a single
parameter $\theta _ { i } ,$ we will need to compute the log-likelihood for a range of $\theta _ { i }$ with the other $\theta$
set to the maximizing values. This is known as the profile likelihood for $\theta _ { i } .$ Once this is
computed as $l _ { i } \left( \theta _ { i } | y \right) ,$ the confidence interval is:

$$\left\{ \theta _ { i } : 2 \left( I \left( \widehat { \theta } _ { i } | y \right) - I \left( \theta _ { i } | y \right) \right) < x _ { i } ^ { 1 - \alpha } \right\}$$

As an example, this type of calculation is used in the computation of the confidence
interval for the transformation parameter used in the Box-Cox method.

We can illustrate this by considering a binomial dataset where $n = 1 0 0$ and $y = 4 0 .$ We
plot the normalized log-likelihood in Figure A.2 where we have drawn a horizontal line
at half the distance of the 0.95 quantile of $x _ { 1 } ^ { 2 }$ below the maximum:

$$> p r < - \quad s e q \left( 0 . 2 5 , 0 . 5 5 , b y = 0 . 0 1 \right)$$

\>
plot (pr, nloglik (pr, 40, 100) , type="1", xlab="p", ylab="log-
likelihood")
\> abline $\left( h = - \quad q c h i s q \left( 0 . 9 5 , 1 \right) / 2 \right)$

All $p$ that have a likelihood above the line are contained within a 95% confidence interval
for $p .$ We can compute the range by solving for the points of intersection:

\> g <- function (x) nloglik (x, 40, 100) +qchisq (0.95,1)
/2
> uniroot (g, c (0.45,0.55) ) $root

<!-- PageBreak -->

<!-- PageHeader="Appendix A 313" -->


<figure>
<figcaption>Figure A.2 Likelihood ratio test-based confidence intervals for binomial $p .$</figcaption>

0

T

log-likelihood

-5 -4 -3 -2

0.25

0.35

0.45

0.55

$p$

</figure>


[1] 0.49765
\> uniroot (g, c (0.25, 0.35) ) $root
[1] 0.30743
> abline (v=c (0.49765, 0.30743) )

The confidence interval is (0.307,0.498) as is indicated by the vertical lines on the plot.
We can compute the Wald test-based interval as:

\> se <- sqrt $\left( 0 . 4 ^ { * } \left( 1 - 0 . 4 \right) / 1 0 0 \right)$
> cv <- qnorm (0.975)
> c (0.4-cv\*se, 0.4+cv\*se)
[1] 0.30398 0.49602

which is very similar, but not identical, to the LRT-based intervals.

Suppose we are interested in the hypothesis, $H _ { 0 } : p = 0 . 5 .$ The LRT and p-value are:

\> (Irstat <- 2* (loglik (0.4, 40, 100) -loglik (0.5, 40,
100)))
[1] 4.0271
> pchisq (Irstat, 1, lower=F)
[1] 0.044775

<!-- PageBreak -->

<!-- PageHeader="Appendix A 314" -->

So the null is barely rejected at the 5% level. The Wald test gives:

\> (z <- (0.5-0.4) /se)
[1] 2.0412
> 2*pnorm (z, lower=F)
[1] 0.041227

Again, not very different from the LRT. The score test takes more effort to compute. The
observed information is:

$$\frac { - d ^ { 2 } l \left( p | y \right) } { d p ^ { 2 } } = \frac { y } { p ^ { 2 } } + \frac { n - y } { \left( 1 - p \right) ^ { 2 } }$$

We compute the score and information at $p = 0 . 5$ and then form the test and get the $p -$
value:

\> (sc <- 40/0.5- (100-40) / (1-0.5))
[1] -40
[1] 400
> (score.test <- 40*40/400)
[1] 4
> pchisq (4,1, lower=F)
[1] 0.0455

\> (obsinf <- 40/0.5^2+(100-40) / (1-0.5)^2)

The outcome is again slightly different from the previous two tests. Asymptotically, the
three tests agree. We have a moderate size sample in the example, so there is little
difference. More substantial differences could be expected for smaller sample sizes.

<!-- PageBreak -->

<!-- PageBreak -->


## APPENDIX B $R$ Information

R may be obtained from the $R$ project website at http://www.r-project.org/.

This book uses some functions and data that are not part of base R. You may wish to
download these extras from the $\mathrm { R }$ website. The additional packages used are:

faraway, mgcv, acepack, mda, brlr, sm, wavethresh,
SuppDists, Ime4

MASS, rpart and nnet are part of the "recommended" R installation; you will have these
already unless you choose a nonstandard installation. Use the command:

\> library ()

within $R$ to see what packages you have. Under Windows, to install the additional
packages, choose the "Install packages from CRAN" menu option. You must have a
network connection for this to work-if you are working offline, you may use the "Install
packages from local zip file" menu option provided you have already obtained the
necessary packages. Under other operating systems, such as Macintosh or Linux, the
installation procedure differs. Consult the $R$ website for details.

I have collected the data and functions that I have used in this book as an $R$ package
called faraway that you may obtain from CRAN or the book website at
www.stat.Isa.umich.edu/~faraway/ELM. The functions defined are:


<table>
<tr>
<td>halfnorm</td>
<td>Half normal plot</td>
</tr>
<tr>
<td>logit</td>
<td>logit transformation</td>
</tr>
<tr>
<td>ilogit</td>
<td>inverse logit transformation</td>
</tr>
</table>


Where add-on packages are needed in the text, you will find the appropriate library
command. However, I have assumed that the faraway library is always loaded. You can
add a line reading library (faraway) to your Rprofile file if you expect to use this package
in every session. Otherwise, you will need to remember to type it each time.

I set the following options to achieve the output seen in this book:

$$> o p t i o n s \left( d i g i t s = 5 , s h o w . s i g n i f . s t a r s = F A L S E \right)$$

The digits=5 reduces the number of digits shown when printing numbers from the default
of seven. Note that this does not reduce the precision with which these numbers are
internally stored. One might take this further as anything more than two or three
significant digits in a displayed table is usually unnecessary and more importantly,

<!-- PageBreak -->

<!-- PageHeader="Appendix B 317" -->

distracting. I have also edited the output in the text to remove extraneous output or to
improve the formatting.

The code and output shown in this book were generated under $\mathrm { R }$ version 2.2.0. $R$ is
regularly updated and improved, so more recent versions may show some differences in
the output.

Getting Started with R: R requires some effort to learn. Such effort will be repaid
with increased productivity. Free introductory guides to $R$ may be obtained from the $R$
project website at http://www.r-project.org/. Introductory books have been written by
Dalgaard (2002), Verzani (2004) and Maindonald and Braun (2003). Venables and
Ripley (2002) also have an introduction to $R$ along with more advanced material. Fox
(2002) is intended as a companion to a standard regression text. You may also find
Becker, Chambers, and Wilks (1998) and Chambers and Hastie (1991) to be useful
references to the $\mathrm { S }$ language. Ripley and Venables (2000) wrote a more advanced text on
programming in S or $R .$

While running $\mathrm { R }$ you can get help about a particular command; for example, if you
want help about the boxplot command, just type help (boxplot). If you do not know what
the name of the command that you want to use, then type:

$$> \mathrm { h e l p . s t a r t } \left( \right)$$

and then browse. You will be able to pick up the language from the examples in the text
and from the help pages.

<!-- PageBreak -->


## Bibliography

Agresti, A. (1984). Analysis of Ordinal Categorical Data. New York: Wiley.

Agresti, A. (2002). Categorical Data Analysis (2 ed.). New York: John Wiley.

Allison, T. and D.Cicchetti (1976). Sleep in mammals: Ecological and constitutional correlates.
Science 194, 732-734.

Andrews, D. and A.Herzberg (1985). Data: A Collection of Problems from Many Fields for the
Student and Research Worker. New York: Springer-Verlag.

Appleton, D., J.French, and M.Vanderpump (1996). Ignoring a covariate: An example of
Simpson's paradox. American Statistician 50, 340-341.

Bates, D. (2005, May). Fitting linear mixed models in R. R News 5(1), 27-30.

Becker, R., J.Chambers, and A. Wilks (1998). The New S Language: A Programming Environment
for Data Analysis and Graphics (revised ed.). Boca Raton, FL: CRC Press.

Bellman, R. (1961). Adaptive Control Processes: A Guided Tour. Princeton, NJ: Princeton
University Press.

Bergman, B. and A.Hynen (1997). Dispersion effects from unreplicated designs in the $2 ^ { k - P }$ series.
Technometrics 39, 191-198.

Bickel, P. and K.Doksum (1977). Mathematical Statistics: Basic Ideas and Selected Topics. San
Francisco: Holden Day.

Bishop, C. (1995). Neural Networks for Pattern Recognition. Oxford: Clarendon Press.

Bishop, Y., S.Fienberg, and P.Holland (1975). Discrete Multivariate Analysis: Theory and
Practice. Cambridge, MA: MIT Press.

Blasius, J. and M.Greenacre (1998). Visualization of Categorical Data. San Diego: Academic
Press.

Bliss, C.I. (1935). The calculation of the dose-mortality curve. Annals of Applied Biology 22, 134-
167.

Bliss, C.I. (1967). Statistics in Biology. New York: McGraw Hill.

Bowman, A. and A.Azzalini (1997). Applied Smoothing Techniques for Data Analysis: The Kernel
Approach with S-Plus Illustrations. Oxford: Oxford University Press.

Box, G. and R.Meyer (1986). Dispersion effects from fractional designs. Technometrics 28, 19-27.

Box, G.P., S.Bisgaard, and C.Fung (1988). An explanation and critique of Taguchi's contributions
to quality engineering. Quality and Reliability Engineering International 4, 123-131.

Box, G.P., W.G.Hunter, and J.S.Hunter (1978). Statistics for Experimenters. New York: Wiley.

Breiman, L. (2001a). Random forests. Machine Learning 45, 5-32.

Breiman, L. (2001b). Statistical modeling: The two cultures (with comments and a rejoinder by the
author). Statistical Science 16, 199-231.

Breiman, L., J.Friedman, R.Olshen, and C.Stone (1984). Classification and Regression Trees. Boca
Raton, FL: Chapman & Hall.

Breiman, L. and J.H.Friedman (1985). Estimating optimal transformations for multiple regression
and correlation. Journal of the American Statistical Association 80, 580-598.

Breslow, N. (1982). Covariance adjustment of relative-risk estimates in matched studies.
Biometrics 38, 661-672.

Breslow, N.E. and D.G.Clayton (1993). Approximate inference in generalized linear mixed models.
Journal of the American Statistical Association 88, 9-25.

Cameron, A. and P.Trivedi (1998). Regression Analysis of Count Data. Cambridge: Cambridge
University Press.

<!-- PageBreak -->

<!-- PageNumber="319" -->
<!-- PageHeader="Bibliography" -->

Chambers, J. and T.Hastie (1991). Statistical Models in S. London: Chapman & Hall.

Christensen, R. (1997). Log-Linear Models and Logistic Regression (2 ed.). New York: Springer.

Cleveland, W. (1979). Robust locally weighted regression and smoothing scatter-plots. Journal of
the American Statistical Association 74, 829-836.

Clogg, C. and E.Shihadeh (1994). Statistical Models for Ordinal Variables. Thousands Oaks, CA:
Sage.

Cochran, W. (1954). Some methods of strengthening the common $x ^ { 2 }$ tests. Biometrics 10, 417-451.

Collett, D. (2003). Modelling Binary Data (2 ed.). London: Chapman & Hall.

Comizzoli, R.B., J.M.Landwehr, and J.D.Sinclair (1990). Robust materials and processes: Key to
reliability. AT&T Technical Journal 69(6), 113-128.

Cox, D. (1970). Analysis of Binary Data. London: Spottiswoode, Ballantyne and Co.

Cox, D. and D.Hinkley (1974). Theoretical Statistics. London: Chapman & Hall/CRC.

Crainiceanu, C. and D.Ruppert (2004). Likelihood ratio tests in linear mixed models with one
variance component. Journal of the Royal Statistical Society, Series B 66, 165-185.

Crowder, M. (1978). Beta-binomial anova for proportions. Applied Statistics 27, 34-37.

Crowder, M.J. and D.J.Hand (1990). Analysis of Repeated Measures. London: Chapman & Hall.

Dalal, S., E.Fowlkes, and B.Hoadley (1989). Risk analysis of the space shuttle: Pre-Challenger
prediction of failure. Journal of the American Statistical Association 84, 945-957.

Dalgaard, P. (2002). Introductory Statistics with R. New York: Springer.

Daubechies, I. (1991). Ten Lectures on Wavelets. Philadelphia: SIAM.

Davies, O. (1954). The Design and Analysis of Industrial Experiments. New York: Wiley.

Dey, D., S.Ghosh, and B.Mallick (2000). Generalized Linear Models: A Bayesian Perspective.
New York: Marcel Dekker.

Diggle, P.J., P.Heagerty, K.Y.Liang, and S.L.Zeger (2002). Analysis of Longitudinal Data (2 ed.).
Oxford: Oxford University Press.

Dobson, A. (1990). An Introduction to Generalized Linear Models. London: Chapman and Hall.

Draper, N. and H.Smith (1998). Applied Regression Analysis (3rd ed.). New York: Wiley.

Eubank, R. (1988). Spline Smoothing and Nonparametric Regression. New York: Marcel Dekker.

Fahrmeir, L. and G.Tutz (2001). Multivariate Statistical Modelling Based on Generalized Linear
Models. New York: Springer.

Faraway, J. (2004). Linear Models with R. Boca Raton, FL: Chapman & Hall/CRC.

Faraway, J. and C.Chatfield (1998). Time series forecasting with neural networks: A case study.
Applied Statistics 47, 231-250.

Firth, D. (1993). Bias reduction of maximum likelihood estimates. Biometrika 80, 27-38.

Fitzmaurice, G., N.Laird, and J.Ware (2004). Applied Longitudinal Analysis. Hoboken, NJ: Wiley-
Interscience.

Fletcher, R. (1987). Practical Methods of Optimization (2 ed.). Chichester, UK: John Wiley.

Fox, J. (2002). An R and S-plus Companion to Applied Regression. Thousand Oaks, CA: Sage.

Frees, E. (2004). Longitudinal and Panel Data: Analysis and Applications in the Social Sciences.
Cambridge: Cambridge University Press.

Friedman, J. (1991). Multivariate adaptive regression splines (with discussion). Annals of Statistics
19, 1-141.

Frome, E. and R.DuFrain (1986). Maximum likelihood estimation for cytogenic dose-response
curves. Biometrics 42, 73-84.

Gelman, A. (2005). Analysis of variance-why it is more important than ever (with discussion).
Annals of Statistics 33, 1-53.

Gelman, A., J.Carlin, H.Stern, and D.Rubin (2003). Bayesian Data Analysis (2 ed.). Chapman &
Hall/CRC.

Gill, J. (2001). Generalized Linear Models: A Unified Approach. Thousand Oaks, CA: Sage.

Goldstein, H. (1995). Multilevel Statistical Models (2 ed.). London: Arnold.

Green, P. and B.Silverman (1993). Nonparametric Regression and Generalized Linear Models: A
Roughness Penalty Approach. London: Chapman & Hall.

<!-- PageBreak -->

<!-- PageNumber="320" -->
<!-- PageHeader="Bibliography" -->

Gu, C. (2002). Smoothing Spline ANOVA Models. New York: Springer Verlag.

Haberman, S. (1977). The Analysis of Frequency Data. Chicago, IL: University of Chicago Press.
Hall, S. (1994). Analysis of defectivity of semiconductor wafers by contigency table. Proceedings
of the Institute of Environmental Sciences 1, 177-183.

Hallin, M. and J .- F.Ingenbleek (1983). The Swedish automobile portfolio in 1977. A statistical
study. Scandinavian Actuarial Journal 83, 49-64.

Hand, D. (1981). Discrimination and Classification. Chichester, UK: Wiley.

Hardin, J. and J.Hilbe (2003). Generalized Estimating Equations. Boca Raton, FL: Chapman &
Hall/CRC Press.

Härdle, W. (1991). Smoothing Techniques with Implementation in S. New York: Springer.

Harrell, F. (2001). Regression Modelling Strategies. New York: Springer Verlag.

Hart, J. (1997). Nonparametric Smoothing and Lack-of-Fit Tests. New York: Springer.

Hartigan, J. and B.Kleiner (1981). Mosaics for contingency tables. In W.Eddy (Ed.), Computer
Science and Statistics: Proceedings of the 13th Symposium on the Interface, pp. 268-273.
Springer Verlag.

Hastie, T. and R.Tibshirani (1990). Generalized Additive Models. London: Chapman & Hall.

Hastie, T., R.Tibshirani, and J.Friedman (2001). The Elements of Statistical Learning: Data
Mining, Inference, and Prediction. New York: Springer.

Hauck, W. and A.Donner (1977). Wald's test as applied to hypotheses in logit analysis. Journal of
the American Statistical Association 72, 851-853.

Haykin, S. (1998). Neural Networks: A Comprehensive Foundation (2 ed.). Prentice Hall.

Hertz, J., A.Krogh, and R.Palmer (1991). Introduction to the Theory of Neural Computation.
Redwood City, CA: Addison-Wesley.

Hill, M.S. (1992). The Panel Study of Income Dynamics: A User's Guide. Newbury Park, CA:
Sage.

Hinde, J. and C.Demetrio (1988). Overdispersion: Models and estimation. Computational Statistics
and Data Analysis 27, 151-170.

Hornik, K., M.Stinchcombe, and H. White (1989). Multilayer feedforward networks are universal
approximators. Neural Networks 2, 359-366.

Hosmer, D. and S.Lemeshow (2000). Applied Logistic Regression (2 ed.). New York: Wiley.

Johnson, M.P. and P.H.Raven (1973). Species number and endemism: The Galápagos archipelago
revisited. Science 179, 893-895.

Kleinbaum, D.G. and M.Klein (2002). Logistic Regression: A Self-Learning Text. New York:
Springer.

Lawless, J. (1987). Negative binomial and mixed poisson regression. Canadian Journal of
Statistics 15, 209-225.

Le, C.T. (1998). Applied Categorical Data Analysis. Newbury Park, CA: Wiley.

Leonard, T. (2000). A Course in Categorical Data Analysis. Boca Raton, FL: Chapman &
Hall/CRC Press.

Lindsey, J.K. (1997). Applying Generalized Linear Models. New York: Springer.

Lindsey, J.K. (1999). Models for Repeated Measurements (2 ed.). Oxford: Oxford University Press.

Loader, C. (1999). Local Regression and Likelihood. New York: Springer.

Lowe, C., C.Roberts, and S.Lloyd (1971). Malformations of the central nervous system and
softness of local water supplies. British Medical Journal 15, 357-361.

Maindonald, J. and J.Braun (2003). Data Analysis and Graphics Using R. Cambridge, UK:
Cambridge University Press.

Manly, B. (1978). Regression models for proportions with extraneous variance. Biometrie-
Praximetrie 18, 1-18.

Mantel, N. and W.Haenszel (1959). Statistical aspects of the analysis of data from retrospective
studies of disease. Journal of the National Cancer Institute 22, 719-748.

Margolese, M. (1970). Homosexuality: A new endocrine correlate. Hormones and Behavior 1,
151-155.

<!-- PageBreak -->

<!-- PageNumber="321" -->
<!-- PageHeader="Bibliography" -->

McCullagh, P. (1983). Quasi-likelihood functions. Annals of Statistics 11, 59-67.

McCullagh, P. and J.Nelder (1989). Generalized Linear Models (2 ed.). London: Chapman & Hall.
McCulloch, C. and S.Searle (2002). Generalized, Linear, and Mixed Models. New York: Wiley.

McCulloch, W. and W.Pitts (1943). A logical calculus of ideas immanent in neural activity.
Bulletin of Mathematical Biophysics 5, 115-133.

Mehta, C. and N.Patel (1995). Exact logistic regression: theory and examples. Statistics in
Medicine 14, 2143-2160.

Menard, S. (2002). Applied Logistic Regression Analysis (2 ed.). Thousands Oaks, CA: Sage.
Meyer, M. (2002). Uncounted votes: Does voting equipment matter? Chance 15(4), 33-38.

Milliken, G.A. and D.E.Johnson (1992). Analysis of Messy Data, Volume 1. New York: Van
Nostrand Reinhold.

Morgan, J. and J.Sonquist (1963). Problems in the analysis of survey data, and a proposal. Journal
of the American Statistical Association 58, 415-434.

Mortimore, P., P.Sammons, L.Stoll, D.Lewis, and R.Ecob (1988). School Matters. Wells, UK:
Open Books.

Myers, R. and D.Montgomery (1997). A tutorial on generalized linear models. Journal of Quality
Technology 29, 274-291.

Myers, R., D.Montgomery, and G.Vining (2002). Generalized Linear Models: With Applications in
Engineering and the Sciences. New York: Wiley.

Naglekerke, N. (1991). A note on a general definition of the coefficient of determination.
Biometrika 78, 691-692.

Neal, R. (1996). Bayesian Learning for Neural Networks. New York: Springer-Verlag.

Nelder, J., Y.Lee, B.Bergman, A.Hynen, A.Huele, and J.Engel (1998). Letter to editor: Joint
modeling of mean and dispersion. Technometrics 40, 168-175.

Nelder, J. and R. Wedderburn (1972). Generalized linear models. Journal of the Royal Statistical
Society, Series A (132), 370-384.

Payne, C. (Ed.) (1987). The GLIM System Release 3.77 Manual (2 ed.). Oxford: Numerical
Algorithms Group.

Penrose, R. (1989). The Emperor's New Mind: Concerning Computers, Minds, and the Laws of
Physics. Oxford: Oxford University Press.

Pignatiello, J.J. and J.S.Ramberg (1985). Contribution to discussion of offline quality control,
parameter design and the Taguchi method. Journal of Quality Technology 17, 198-206.

Pinheiro, J.C. and D.M.Bates (2000). Mixed-Effects Models in S and S-PLUS. New York: Springer.

Powers, D. and Y.Xie (2000). Statistical Methods for Categorical Data Analysis. San Diego, CA:
Academic Press.

Pregibon, D. (1981). Logistic regression diagnostics. Annals of Statistics 9, 705-724.

Purott, R. and E.Reeder (1976). The effect of changes in dose rate on the yield of chromosome
aberrations in human lymphocytes exposed to gamma radiation. Mutation Research 35, 431-
444.

Quinlan, J. (1993). C4.5: Programs for Machine Learning. San Mateo, CA: Mor-gan Kaufman.

Raudenbush, S. and A.Bryk (2002). Hierarchical Linear Models: Applications and Data Analysis
Methods (2 ed.). Thousand Oaks, CA: Sage.

Rice, J. (1998). Mathematical Statistics and Data Analysis. Monterey, CA: Brooks Cole.

Ripley, B. (1996). Pattern Recognition and Neural Networks. Cambridge, UK: Cambridge
University Press.

Ripley, B. and W.Venables (2000). S Programming. New York: Springer-Verlag.

Rosenstone, S.J., D.R.Kinder, and W.E.Miller (1997). American National Elec-tion Study. Ann
Arbor, MI: Inter-university Consortium for Political and So-cial Research.

Santner, T. and D.Duffy (1989). The Statistical Analysis of Discrete Data. New York: Springer.
Scheffeé, H. (1959). The Analysis of Variance. New York: Wiley.

Searle, S., G.Casella, and C.McCulloch (1992). Variance Components. New York: Wiley.
Seshadri, V. (1993). The Inverse Gaussian Distribution. Oxford: Clarendon.

<!-- PageBreak -->

<!-- PageNumber="322" -->
<!-- PageHeader="Bibliography" -->

Sheldon, F. (1960). Statistical techniques applied to production situations. Indus-trial and
Engineering Chemistry 52, 507-509.

Simonoff, J. (1996). Smoothing Methods in Statistics. New York: Springer.

Simonoff, J. (2003). Analyzing Categorical Data. New York: Springer.

Simpson, E. (1951). The interpretation of interaction in contingency tables. Jour-nal of the Royal
Statistical Society, Series $B$ (13), 238-241.

Sinha, S. (2004). Robust analysis of generalized linear mixed models. JASA 99, 451-460.

Smyth, G., F.Huele, and A. Verbyla (2001). Exact and approximate reml for heteroscedastic
regression. Statistical Modelling: An International Journal 1, 161-175.

Snedecor, G. and W.Cochran (1989). Statistical Methods (8 ed.). Ames, IA: Iowa State University
Press.

Snee, R. (1974). Graphical display of two-way contingency tables. American Statistician 28, 9-12.

Steele, R. (1998). Effect of surface and vision on balance. Ph. D. thesis, Depart-ment of
Physiotherapy, University of Queensland.

Stone, C. (1985). Additive regression and other nonparametric models. Annals of Statistics 13,
689-705.

Stram, D. and J.Lee (1994). Variance components testing in the longitudinal mixed-effects model.
Biometrics 50, 1171-1179.

Stuart, A. (1955). A test for homogeneity of the marginal distributions in a twoway classification.
Biometrika 42, 412-416.

Thall, P.F. and S.C.Vail (1990). Some covariance models for longitudinal count data with
overdispersion. Biometrics 46, 657-671.

Tukey, J. (1977). Exploratory Data Analysis. New York: Addison Wesley.

Venables, W. and B.Ripley (2002). Modern Applied Statistics with S (4 ed.). New York: Springer.

Verbeke, G. and G.Molenberghs (2000). Linear Mixed Models for Longitudinal Data. New York:
Springer.

Verzani, J. (2004). Using R for Introductory Statistics. Boca Raton, FL: Chapman & Hall/CRC.

Wahba, G. (1990). Spline Models for Observational Data. Philadelphia: SIAM.

Wand, M. and M.Jones (1995). Kernel Smoothing. London: Chapman & Hall.

Wedderburn, R.W.M. (1974). Quasilikelihood functions, generalized linear mod-els and the Gauss-
Newton method. Biometrika 61, 439-441.

Weisberg, S. (2005). Applied Linear Regression (3 ed.). New York: Wiley.

Whitmore, G. (1986). Inverse Gaussian ratio estimation. Applied Statistics 35, 8-15.

Wilkinson, G. and C.Rogers (1973). Symbolic description of factorial models for the analysis of
variance. Applied Statistics 22, 392-399.

Williams, D. (1982). Extra-binomial variation in logistic linear models. Applied Statistics 31, 144-
148.

Williams, D. (1987). Generalized linear model diagnostics using the deviance and single case
deletions. Applied Statistics 36, 181-191.

Wold, S., A.Ruhe, H.Wold, and W.Dunn (1984). The collinearity problem in lin-ear regression:
The partial least squares (pls) approach to generalized inverses. SIAM Journal on Scientific and
Statistical Computing 5, 735-743.

Wood, S. (2000). Modelling and smoothing parameter estimation with multiple quadratic penalties.
Journal of the Royal Statistal Society, Series B 62, 413-428.

Wood, S. (2006). An Introduction to Generalized Additive Models with R. Boca Raton, FL: CRC
Press.

Yule, G. (1903). Notes on the theory of association of attributes in statistics. Biometrika 2, 121-
134.

<!-- PageBreak -->

<!-- PageBreak -->


## Index

ACE, see alternating conditional expectations
activation function, 269
additive models, 231
additivity and variance stabilization, 244
adjusted dependent variable, 118, 240
aggregated data, 56
AIC, 21, 138
Akaike Information Criterion, see AIC
alternating conditional expectations, 241
ANOVA estimator, 154
AR, see autoregressive errors
autoregressive errors, 207, 208
$\mathrm { A V A S } ,$ see additivity and variance stabilization

B-splines, 20, 219
backfitting, 232
backward elimination, 258
Bayes Theorem, 35
beta distribution, 45
bias, 270
binary response, 30
binomial deviance, 29
binomial distribution, 26, 116
blocks, 153, 163
BLUP, 162
bootstrap, 30, 158
Box-Cox transformation, 18, 117, 129, 138, 283

canonical correlation, 244
canonical link, 57
canonical parameter, 115
CART, 254
case-control study, 34
CHAID, 253
classification, 42
classification trees, 261
Cochran-Mantel-Haenszel, 83
coefficient of determination, 8
coefficient of variation, 136
cohort study, 34
collinearity, 11, 274
column effects, 91
complementary log-log, 27, 107, 111

<!-- PageBreak -->

<!-- PageNumber="Index 325" -->

compositional effects, 179
compound symmetry, 204
conditional independence, 85
confidence interval, 30, 283
consistency, 45, 204
contingency table, 69
continuity correction, 83
contrast matrix, 10
contrasts, 10, 51
controls, 48
Cook statistics, 15, 125
correspondence analysis, 76
cost-complexity, 258
count regression, 55
cross-validation, 215, 247, 257
crossed effects, 170, 172
curse of dimensionality, 228
cutpoint, 89, 110, 237

datasets
abrasion, 173
amlxray, 49
babyfood, 32
bliss, 36, 41, 118
cns, 103
cpd, 143
ctsib, 202, 204
dicentric, 61
eggs, 170
epilepsy, 206, 247
esoph, 52
exa, 212
exb, 212
eyegrade, 79
faithful, 212
femsmoke, 81
gala, 56, 126
gavote, 1
haireye, 75
hormone, 38
irrigation, 168
jsp, 174, 195
kanga, 262
mammalsleep, 149
motorins, 140
nes96, 89, 98
orings, 25
ozone, 233, 248, 255, 272
penicillin, 164
psid, 186
pulp, 157

<!-- PageBreak -->

<!-- PageHeader="Index 326" -->

savings, 228
solder, 64
troutegg, 46
vision, 191
wafer, 138
weldstrength, 146
degrees of freedom, 8
delta method, 43
deviance, 8, 29, 120
deviance residuals, 123
diagnostics, 123
discriminant analysis, 270
dispersion parameter, 60, 115
dotchart, 75
dummy variable, 9

ED50, 42
effective dose, 42
eigenvalue, 77
empirical logits, 47
entropy, 261
Epanechnikov kernel, 213
exact logistic regression, 39
exchangeable, 204
expected mean squares, 159
exponential dispersion family, 116
exponential family, 115
extrapolation, 20, 274
extreme value distribution, 31

factor, 10
factorial design, 137, 172
feed-forward neural network, 270
Fisher information, 280
Fisher scoring, 117, 282
Fisher's exact test, 74
fitted values, 7
fixed effects, 153
F-statistic, 121
F-test, 12
full model, 120

GAM, see generalized additive models
GAMM, see generalized additive mixed models
gamma distribution, 116, 135
gamma GLM, 135
Gaussian distribution, 115
GCV, see generalized cross-validation
GEE, see generalized estimating equations
generalized additive mixed models, 246
generalized additive models, 240

<!-- PageBreak -->

<!-- PageNumber="Index 327" -->

generalized cross-validation, 215
generalized estimating equations, 204
generalized least squares, 155, 159
generalized linear mixed models, 201
generalized linear model, 115
Gini index, 261
GLM, see generalized linear model
GLMM, see generalized linear mixed models
goodness of fit, 29, 121
greedy strategy, 257
grouped data, 153
G-statistic, 58

half-normal plot, 59, 129
hat matrix, 16, 124
Hauck-Donner effect, 30
hazard, 111
Helmert contrasts, 194
Hessian matrix, 281
hierarchical response, 103
homogeneity, 74
hypergeometric distribution, 70, 74
hypothesis tests, 12, 120

independence, 72
indicator variable, see dummy variable
inertia, 77
influence, 14, 124
interaction, 10
intercept, 6
interval scale, 69
intraclass correlation coefficient, 154
inverse Gaussian distribution, 116
inverse Gaussian GLM, 142
iteratively reweighted least squares, 117

jacknife residuals, 124
joint independence, 85

kernel estimator, 213
knots, 218

latent variable, 107
latin square, 172
LD50, 42
lethal dose, 42
leverage, 16, 124
likelihood, 279
likelihood ratio statistic, 29, 120, 282
linear model, 1

<!-- PageBreak -->

<!-- PageHeader="Index 328" -->

linear predictor, 26
linear separability, 39
linear-by-linear association, 89
linearized response, 128
link function, 27, 36, 116
local polynomials, 221
loess, 221, 233
log-odds ratio, 35
logistic distribution, 31, 107
logistic regression, 28
logit, 27
lognormal distribution, 139
longitudinal data, 185

machine learning, 253
Mantel-Haenszel, 83
marginal homogeneity, 80
MARS, see multivariate adaptive regression splines
matched pairs, 79
matched case-control study, 48
matched set, 48
maximum likelihood, 279
Michaelis-Menten, 137
missing values, 254
mixed effects, 153
mosaic plot, 75
moving average, 213
multilevel models, 174, 195
multinomial distribution, 97
multinomial logit, 97
multivariate adaptive regression splines, 247
multivariate smoothing, 228
mutual independence, 84

Nadaraya-Watson estimator, 213
Naglekerke's $R ^ { 2 } ,$ 41
nearest neighbor, 226
negative binomial, 55, 63, 116
nested effects, 170
nested response, 103
neural network, 99, 269
Newton-Raphson, 117, 281
nominal variable, 69
nonconstant variance, 56
nonnested models, 140
nonparametric regression, 211
normal distribution, 115
normal equation, 7
null deviance, 29
null model, 120

<!-- PageBreak -->

<!-- PageHeader="Index 329" -->

object-oriented language, 8
observed information, 285
odds, 31
odds ratio, 32, 74, 83
offset, 63, 139, 207
one-way ANOVA, 154
ordinal multinomial response, 106
ordinal variable, 69, 88
orthogonal polynomials, 19, 222
outliers, 4, 5, 129
overdispersion, 43, 60

packages, 287

MASS, 18, 31, 34, 43, 65, 108, 139, 203
SuppDists, 142
acepack, 242
brlr, 40, 203
faraway, 1, 25
gam, 233
gee, 204

lattice, 186

lme4, 157
mda, 248
mgcv, 235
nnet, 99, 272

rpart, 255
sm, 216
splines, 20, 220
survival, 51
wavethresh, 223

panel data, 185
parameters, 6
parametric bootstrap, 159
partial residual plot, 16, 128

partial residuals, 232
Pearson residuals, 40, 76, 123
Pearson's $X ^ { 2 } ,$ 40, 58, 120
penalized quasi-likelihood, 203

penalized smoothing splines, 232
perceptron, 269
permutation, 30, 132
piecewise linear, 219

Poisson deviance, 58
Poisson distribution, 55, 115

Poisson regression, 55
predicted values, 7
prediction, 41
principal components, 265
prior density, 161
probit, 27, 106
product multinomial, 74

<!-- PageBreak -->

<!-- PageHeader="Index 330" -->

profile likelihood, 31, 283
projection matrix, 234
proportional hazards model, 111
proportional odds model, 108
prospective sampling, 34

QQ plot, 14
quasi-binomial, 148
quasi-deviance, 148
quasi-independence, 81
quasi-likelihood, 147, 204
quasi-Poisson, 148
quasi-symmetry, 80

R, 287
random effects, 153
randomization, 167
randomized block design, 163
rate model, 61
recursive partitioning, 253
regression splines, 218
regression trees, 253
relative risk, 32
REML, see restricted maximum likelihood
repeated measures, 185
residual deviance, 29
residual sum of squares, 8
residuals, 7, 123
response feature analysis, 189
response residuals, 123
restricted maximum likelihood, 156

retrospective sampling, 34
robust smoothing, 218, 221
roughness penalty, 217
row effects, 91
$R ^ { 2 } ,$ 8
running median, 226

saturated model, 29, 120
scaled deviance, 120
score function, 280
score test, 283
scores, 89
shrinkage, 162
Simpson's paradox, 82
simulation, 160
singular value decomposition, 76
skip-layer, 271
smoothing, 212
smoothing parameter, 213
smoothing spline, 217

<!-- PageBreak -->

<!-- PageHeader="Index 331" -->

splines, 217
split-plot design, 167
square-root transformation, 56
studentized residuals, 124
sufficient, 117
sum contrasts, 157
symmetry, 79

TBS, see transform both sides
thin plate splines, 228
tolerance distribution, 31
transform both sides, 241
treatment coding, 10
tree pruning, 257
trees, 253
t-statistic, 12
t-test, 12
twicing, 227

unbalanced data, 155
underdispersion, 59
uniform association, 86

variable bandwidth, 226
variance function, 116

Wald distribution, 142
Wald test, 122, 282
wavelets, 222
Weibull distribution, 116
weight decay, 274
weights, 116
working residuals, 124

Yates' continuity correction, 73

<!-- PageBreak -->


