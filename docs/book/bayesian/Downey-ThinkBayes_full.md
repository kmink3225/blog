O'REILLY®
R


<figure>

Second
Edition

</figure>


Think
Bayes

Bayesian Statistics in Python


<figure>
</figure>


Allen B. Downey

<!-- PageBreak -->

O'REILLY®
®


# Think Bayes

If you know how to program, you're ready to tackle Bayesian
statistics. With this book, you'll learn how to solve statistical
problems with Python code instead of mathematical
formulas, using discrete probability distributions rather than
continuous mathematics. Once you get the math out of the
way, the Bayesian fundamentals will become clearer and
you'll begin to apply these techniques to real-world problems.

Bayesian statistical methods are becoming more common and
more important, but there aren't many resources available to
help beginners. Based on undergraduate classes taught by
author Allen B. Downey, this book's computational approach
helps you get a solid start.

· Use your programming skills to learn and understand
Bayesian statistics

· Work with problems involving estimation, prediction,
decision analysis, evidence, and Bayesian hypothesis testing

· Get started with simple examples, using coins, dice, and a
bowl of cookies

· Learn computational methods for solving real-world
problems

Allen B. Downey is a professor of computer science at Olin College
of Engineering. He's taught at Wellesley College, Colby College, and
UC Berkeley. Allen has a PhD in computer science from UC Berkeley
and master's and bachelor's degrees from MIT. He's the author of
Think Python, Think Stats, and Think DSP (all from O'Reilly), and a
blog, Probably Overthinking It.

"Allen B. Downey once
again turns a 200-year-
old math theorem into
an interesting book
combining informative
reading with practical
examples. This is one
of the best applied
introductions to Bayes's
theorem that you will
find."

-Ravin Kumar
Data Scientist

"Allen takes an effective
approach by curating
unique examples and
diverse applications.
Bayesian ideas are no
longer a niche interest,
but a growing area for
problem-solving."

-Thomas Nield

Founder of Nield Consulting Group and
author of Getting Started with SQL

MATH

Twitter: @oreillymedia
facebook.com/oreilly

US $49.99
CAN $65.99

<!-- PageFooter="ISBN: 978-1-492-08946-9" -->

54999

<!-- PageNumber="9" -->

781492 089469

<!-- PageBreak -->

<!-- PageHeader="SECOND EDITION" -->


# Think Bayes Bayesian Statistics in Python

Allen B. Downey

Beijing . Boston . Farnham · Sebastopol . Tokyo


<figure>

O'REILLY®

</figure>


<!-- PageBreak -->

Think Bayes
by Allen B. Downey
Copyright @ 2021 Allen B. Downey. All rights reserved.
Printed in the United States of America.
Published by O'Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472.

O'Reilly books may be purchased for educational, business, or sales promotional use. Online editions are
also available for most titles (http://oreilly.com). For more information, contact our corporate/institutional
sales department: 800-998-9938 or corporate@oreilly.com.


<table>
<tr>
<td>Acquisitions Editor: Jessica Haberman</td>
<td>Indexer: Sue Klefstad</td>
</tr>
<tr>
<td>Development Editor: Michele Cronin</td>
<td>Interior Designer: David Futato</td>
</tr>
<tr>
<td>Production Editor: Kristen Brown</td>
<td>Cover Designer: Karen Montgomery</td>
</tr>
<tr>
<td>Copyeditor: O'Reilly Production Services</td>
<td>Illustrator: Allen B. Downey</td>
</tr>
<tr>
<td>Proofreader: Stephanie English</td>
<td></td>
</tr>
</table>


September 2013:
First Edition
May 2021:
Second Edition

Revision History for the Second Edition
2021-05-18: First Release

See http://oreilly.com/catalog/errata.csp?isbn=9781492089469 for release details.

The O'Reilly logo is a registered trademark of O'Reilly Media, Inc. Think Bayes, the cover image, and
related trade dress are trademarks of O'Reilly Media, Inc.

The views expressed in this work are those of the author, and do not represent the publisher's views.
While the publisher and the author have used good faith efforts to ensure that the information and
instructions contained in this work are accurate, the publisher and the author disclaim all responsibility
for errors or omissions, including without limitation responsibility for damages resulting from the use of
or reliance on this work. Use of the information and instructions contained in this work is at your own
risk. If any code samples or other technology this work contains or describes is subject to open source
licenses or the intellectual property rights of others, it is your responsibility to ensure that your use
thereof complies with such licenses and/or rights.

Think Bayes is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 Inter-
national License. The author maintains an online version at https://greenteapress.com/wp/think-bayes.

<!-- PageFooter="978-1-492-08946-9 [LSI]" -->
<!-- PageBreak -->


## Table of Contents


<table>
<tr>
<th>Preface.</th>
<th>ix ☒</th>
</tr>
<tr>
<td>1. Probability.</td>
<td rowspan="2">1</td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td>Linda the Banker</td>
<td>1</td>
</tr>
<tr>
<td>Probability</td>
<td>2</td>
</tr>
<tr>
<td>Fraction of Bankers</td>
<td>3</td>
</tr>
<tr>
<td>The Probability Function</td>
<td>4</td>
</tr>
<tr>
<td>Political Views and Parties</td>
<td>4</td>
</tr>
<tr>
<td>Conjunction</td>
<td>5</td>
</tr>
<tr>
<td>Conditional Probability</td>
<td>6</td>
</tr>
<tr>
<td>Conditional Probability Is Not Commutative</td>
<td>7</td>
</tr>
<tr>
<td>Condition and Conjunction</td>
<td>8</td>
</tr>
<tr>
<td>Laws of Probability</td>
<td>8</td>
</tr>
<tr>
<td>Theorem 1</td>
<td>9</td>
</tr>
<tr>
<td>Theorem 2</td>
<td>10</td>
</tr>
<tr>
<td>Theorem 3</td>
<td>10</td>
</tr>
<tr>
<td>The Law of Total Probability</td>
<td>11</td>
</tr>
<tr>
<td>Summary</td>
<td>13</td>
</tr>
<tr>
<td>Exercises</td>
<td>14</td>
</tr>
<tr>
<td>2. Bayes's Theorem.</td>
<td>17</td>
</tr>
<tr>
<td>The Cookie Problem</td>
<td>17</td>
</tr>
<tr>
<td>Diachronic Bayes</td>
<td>19</td>
</tr>
<tr>
<td>Bayes Tables</td>
<td>20</td>
</tr>
<tr>
<td>The Dice Problem</td>
<td>22</td>
</tr>
<tr>
<td>The Monty Hall Problem</td>
<td>23</td>
</tr>
<tr>
<td>Summary</td>
<td>25</td>
</tr>
<tr>
<td>Exercises</td>
<td>26</td>
</tr>
</table>


<!-- PageNumber="iii" -->
<!-- PageBreak -->


<table>
<tr>
<td>3. Distributions.</td>
<td>29</td>
</tr>
<tr>
<td>Distributions</td>
<td>29</td>
</tr>
<tr>
<td>Probability Mass Functions</td>
<td>29</td>
</tr>
<tr>
<td>The Cookie Problem Revisited</td>
<td>32</td>
</tr>
<tr>
<td>101 Bowls</td>
<td>34</td>
</tr>
<tr>
<td>The Dice Problem</td>
<td>38</td>
</tr>
<tr>
<td>Updating Dice</td>
<td>39</td>
</tr>
<tr>
<td>Summary</td>
<td>40</td>
</tr>
<tr>
<td>Exercises</td>
<td>41</td>
</tr>
<tr>
<td>4. Estimating Proportions.</td>
<td>43</td>
</tr>
<tr>
<td>The Euro Problem</td>
<td>43</td>
</tr>
<tr>
<td>The Binomial Distribution</td>
<td>44</td>
</tr>
<tr>
<td>Bayesian Estimation</td>
<td>47</td>
</tr>
<tr>
<td>Triangle Prior</td>
<td>49</td>
</tr>
<tr>
<td>The Binomial Likelihood Function</td>
<td>51</td>
</tr>
<tr>
<td>Bayesian Statistics</td>
<td>52</td>
</tr>
<tr>
<td>Summary</td>
<td>53</td>
</tr>
<tr>
<td>Exercises</td>
<td>54</td>
</tr>
<tr>
<td>5. Estimating Counts.</td>
<td>57</td>
</tr>
<tr>
<td>The Train Problem</td>
<td>57</td>
</tr>
<tr>
<td>Sensitivity to the Prior</td>
<td>60</td>
</tr>
<tr>
<td>Power Law Prior</td>
<td>61</td>
</tr>
<tr>
<td>Credible Intervals</td>
<td>63</td>
</tr>
<tr>
<td>The German Tank Problem</td>
<td>64</td>
</tr>
<tr>
<td>Informative Priors</td>
<td>65</td>
</tr>
<tr>
<td>Summary</td>
<td>66</td>
</tr>
<tr>
<td>Exercises</td>
<td>66</td>
</tr>
<tr>
<td>6. Odds and Addends.</td>
<td>69</td>
</tr>
<tr>
<td>Odds</td>
<td>69</td>
</tr>
<tr>
<td>Bayes's Rule</td>
<td>70</td>
</tr>
<tr>
<td>Oliver's Blood</td>
<td>71</td>
</tr>
<tr>
<td>Addends</td>
<td>73</td>
</tr>
<tr>
<td>Gluten Sensitivity</td>
<td>76</td>
</tr>
<tr>
<td>The Forward Problem</td>
<td>77</td>
</tr>
<tr>
<td>The Inverse Problem</td>
<td>78</td>
</tr>
<tr>
<td>Summary</td>
<td>80</td>
</tr>
<tr>
<td>More Exercises</td>
<td>81</td>
</tr>
</table>


<!-- PageNumber="iv Table of Contents" -->
<!-- PageBreak -->


<table>
<tr>
<td colspan="2">7. Minimum, Maximum, and Mixture.</td>
<td>83</td>
</tr>
<tr>
<td colspan="2">Cumulative Distribution Functions</td>
<td>83</td>
</tr>
<tr>
<td colspan="2">Best Three of Four</td>
<td>86</td>
</tr>
<tr>
<td></td>
<td>Maximum</td>
<td>88</td>
</tr>
<tr>
<td colspan="2">Minimum</td>
<td>89</td>
</tr>
<tr>
<td colspan="2">Mixture</td>
<td>90</td>
</tr>
<tr>
<td colspan="2">General Mixtures</td>
<td>93</td>
</tr>
<tr>
<td colspan="2">Summary</td>
<td>96</td>
</tr>
<tr>
<td colspan="2">Exercises</td>
<td>97</td>
</tr>
<tr>
<td colspan="2">8. Poisson Processes.</td>
<td>99</td>
</tr>
<tr>
<td colspan="2">The World Cup Problem</td>
<td>99</td>
</tr>
<tr>
<td colspan="2">The Poisson Distribution</td>
<td>100</td>
</tr>
<tr>
<td colspan="2">The Gamma Distribution</td>
<td>101</td>
</tr>
<tr>
<td colspan="2">The Update</td>
<td>103</td>
</tr>
<tr>
<td colspan="2">Probability of Superiority</td>
<td>105</td>
</tr>
<tr>
<td colspan="2">Predicting the Rematch</td>
<td>106</td>
</tr>
<tr>
<td colspan="2">The Exponential Distribution</td>
<td>108</td>
</tr>
<tr>
<td colspan="2">Summary</td>
<td>110</td>
</tr>
<tr>
<td colspan="2">Exercises</td>
<td>110</td>
</tr>
<tr>
<td colspan="2">9. Decision Analysis.</td>
<td>113</td>
</tr>
<tr>
<td colspan="2">The Price Is Right Problem</td>
<td>113</td>
</tr>
<tr>
<td colspan="2">The Prior</td>
<td>114</td>
</tr>
<tr>
<td colspan="2">Kernel Density Estimation</td>
<td>115</td>
</tr>
<tr>
<td colspan="2">Distribution of Error</td>
<td>116</td>
</tr>
<tr>
<td colspan="2">Update</td>
<td>118</td>
</tr>
<tr>
<td colspan="2">Probability of Winning</td>
<td>120</td>
</tr>
<tr>
<td></td>
<td>Decision Analysis</td>
<td>122</td>
</tr>
<tr>
<td></td>
<td>Maximizing Expected Gain</td>
<td>124</td>
</tr>
<tr>
<td colspan="2">Summary</td>
<td>126</td>
</tr>
<tr>
<td></td>
<td>Discussion</td>
<td>126</td>
</tr>
<tr>
<td colspan="2">More Exercises</td>
<td>127</td>
</tr>
<tr>
<td colspan="2">10. Testing.</td>
<td>129</td>
</tr>
<tr>
<td></td>
<td>Estimation</td>
<td>129</td>
</tr>
<tr>
<td></td>
<td>Evidence</td>
<td>131</td>
</tr>
<tr>
<td></td>
<td>Uniformly Distributed Bias</td>
<td>132</td>
</tr>
<tr>
<td colspan="2">Bayesian Hypothesis Testing</td>
<td>134</td>
</tr>
<tr>
<td colspan="2">Bayesian Bandits</td>
<td>134</td>
</tr>
<tr>
<td colspan="2">Prior Beliefs</td>
<td>135</td>
</tr>
<tr>
<td colspan="2">The Update</td>
<td>136</td>
</tr>
</table>


<!-- PageFooter="Table of Contents" -->
<!-- PageNumber="V" -->
<!-- PageBreak -->


<table>
<tr>
<td>Multiple Bandits</td>
<td>137</td>
</tr>
<tr>
<td>Explore and Exploit</td>
<td>138</td>
</tr>
<tr>
<td>The Strategy</td>
<td>140</td>
</tr>
<tr>
<td>Summary</td>
<td>142</td>
</tr>
<tr>
<td>More Exercises</td>
<td>142</td>
</tr>
<tr>
<td>11. Comparison.</td>
<td>145</td>
</tr>
<tr>
<td>Outer Operations</td>
<td>145</td>
</tr>
<tr>
<td>How Tall Is A?</td>
<td>147</td>
</tr>
<tr>
<td>Joint Distribution</td>
<td>148</td>
</tr>
<tr>
<td>Visualizing the Joint Distribution</td>
<td>149</td>
</tr>
<tr>
<td>Likelihood</td>
<td>151</td>
</tr>
<tr>
<td>The Update</td>
<td>152</td>
</tr>
<tr>
<td>Marginal Distributions</td>
<td>153</td>
</tr>
<tr>
<td>Conditional Posteriors</td>
<td>156</td>
</tr>
<tr>
<td>Dependence and Independence</td>
<td>157</td>
</tr>
<tr>
<td>Summary</td>
<td>158</td>
</tr>
<tr>
<td>Exercises</td>
<td>158</td>
</tr>
<tr>
<td>12. Classification.</td>
<td>161</td>
</tr>
<tr>
<td>Penguin Data</td>
<td>161</td>
</tr>
<tr>
<td>Normal Models</td>
<td>163</td>
</tr>
<tr>
<td>The Update</td>
<td>164</td>
</tr>
<tr>
<td>Naive Bayesian Classification</td>
<td>166</td>
</tr>
<tr>
<td>Joint Distributions</td>
<td>168</td>
</tr>
<tr>
<td>Multivariate Normal Distribution</td>
<td>170</td>
</tr>
<tr>
<td>A Less Naive Classifier</td>
<td>172</td>
</tr>
<tr>
<td>Summary</td>
<td>173</td>
</tr>
<tr>
<td>Exercises</td>
<td>173</td>
</tr>
<tr>
<td>13. Inference.</td>
<td>175</td>
</tr>
<tr>
<td>Improving Reading Ability</td>
<td>175</td>
</tr>
<tr>
<td>Estimating Parameters</td>
<td>177</td>
</tr>
<tr>
<td>Likelihood</td>
<td>178</td>
</tr>
<tr>
<td>Posterior Marginal Distributions</td>
<td>180</td>
</tr>
<tr>
<td>Distribution of Differences</td>
<td>181</td>
</tr>
<tr>
<td>Using Summary Statistics</td>
<td>184</td>
</tr>
<tr>
<td>Update with Summary Statistics</td>
<td>186</td>
</tr>
<tr>
<td>Comparing Marginals</td>
<td>187</td>
</tr>
<tr>
<td>Summary</td>
<td>188</td>
</tr>
<tr>
<td>Exercises</td>
<td>189</td>
</tr>
</table>


<!-- PageFooter="Table of Contents" -->
<!-- PageNumber="vi" -->
<!-- PageBreak -->


<table>
<tr>
<td colspan="2">14. Survival Analysis.</td>
<td>191</td>
</tr>
<tr>
<td colspan="2">The Weibull Distribution</td>
<td>191</td>
</tr>
<tr>
<td colspan="2">Incomplete Data</td>
<td>194</td>
</tr>
<tr>
<td colspan="2">Using Incomplete Data</td>
<td>196</td>
</tr>
<tr>
<td colspan="2">Light Bulbs</td>
<td>199</td>
</tr>
<tr>
<td colspan="2">Posterior Means</td>
<td>201</td>
</tr>
<tr>
<td colspan="2">Posterior Predictive Distribution</td>
<td>202</td>
</tr>
<tr>
<td colspan="2">Summary</td>
<td>204</td>
</tr>
<tr>
<td colspan="2">Exercises</td>
<td>204</td>
</tr>
<tr>
<td colspan="2">15. Mark and Recapture.</td>
<td>207</td>
</tr>
<tr>
<td colspan="2">The Grizzly Bear Problem</td>
<td>207</td>
</tr>
<tr>
<td colspan="2">The Update</td>
<td>209</td>
</tr>
<tr>
<td colspan="2">Two-Parameter Model</td>
<td>211</td>
</tr>
<tr>
<td colspan="2">The Prior</td>
<td>212</td>
</tr>
<tr>
<td colspan="2">The Update</td>
<td>213</td>
</tr>
<tr>
<td colspan="2">The Lincoln Index Problem</td>
<td>215</td>
</tr>
<tr>
<td colspan="2">Three-Parameter Model</td>
<td>217</td>
</tr>
<tr>
<td colspan="2">Summary</td>
<td>220</td>
</tr>
<tr>
<td colspan="2">Exercises</td>
<td>221</td>
</tr>
<tr>
<td colspan="2">16. Logistic Regression.</td>
<td>223</td>
</tr>
<tr>
<td colspan="2">Log Odds</td>
<td>223</td>
</tr>
<tr>
<td colspan="2">The Space Shuttle Problem</td>
<td>226</td>
</tr>
<tr>
<td colspan="2">Prior Distribution</td>
<td>229</td>
</tr>
<tr>
<td colspan="2">Likelihood</td>
<td>230</td>
</tr>
<tr>
<td colspan="2">The Update</td>
<td>231</td>
</tr>
<tr>
<td colspan="2">Marginal Distributions</td>
<td>232</td>
</tr>
<tr>
<td colspan="2">Transforming Distributions</td>
<td>233</td>
</tr>
<tr>
<td colspan="2">Predictive Distributions</td>
<td>235</td>
</tr>
<tr>
<td></td>
<td>Empirical Bayes</td>
<td>237</td>
</tr>
<tr>
<td colspan="2">Summary</td>
<td>238</td>
</tr>
<tr>
<td colspan="2">More Exercises</td>
<td>238</td>
</tr>
<tr>
<td colspan="2">17. Regression.</td>
<td>241</td>
</tr>
<tr>
<td></td>
<td>More Snow?</td>
<td>241</td>
</tr>
<tr>
<td></td>
<td>Regression Model</td>
<td>243</td>
</tr>
<tr>
<td colspan="2">Least Squares Regression</td>
<td>244</td>
</tr>
<tr>
<td colspan="2">Priors</td>
<td>245</td>
</tr>
<tr>
<td colspan="2">Likelihood</td>
<td>246</td>
</tr>
<tr>
<td colspan="2">The Update</td>
<td>247</td>
</tr>
<tr>
<td colspan="2">Marathon World Record</td>
<td>250</td>
</tr>
</table>


<!-- PageFooter="Table of Contents" -->
<!-- PageNumber="vii" -->
<!-- PageBreak -->


<table>
<tr>
<td>The Priors</td>
<td>252</td>
</tr>
<tr>
<td>Prediction</td>
<td>254</td>
</tr>
<tr>
<td>Summary</td>
<td>255</td>
</tr>
<tr>
<td>Exercises</td>
<td>255</td>
</tr>
<tr>
<td>18. Conjugate Priors.</td>
<td>257</td>
</tr>
<tr>
<td>The World Cup Problem Revisited</td>
<td>257</td>
</tr>
<tr>
<td>The Conjugate Prior</td>
<td>258</td>
</tr>
<tr>
<td>What the Actual?</td>
<td>260</td>
</tr>
<tr>
<td>Binomial Likelihood</td>
<td>261</td>
</tr>
<tr>
<td>Lions and Tigers and Bears</td>
<td>263</td>
</tr>
<tr>
<td>The Dirichlet Distribution</td>
<td>264</td>
</tr>
<tr>
<td>Summary</td>
<td>266</td>
</tr>
<tr>
<td>Exercises</td>
<td>267</td>
</tr>
<tr>
<td>19. MCMC.</td>
<td>269</td>
</tr>
<tr>
<td>The World Cup Problem</td>
<td>269</td>
</tr>
<tr>
<td>Grid Approximation</td>
<td>270</td>
</tr>
<tr>
<td>Prior Predictive Distribution</td>
<td>270</td>
</tr>
<tr>
<td>Introducing PyMC3</td>
<td>271</td>
</tr>
<tr>
<td>Sampling the Prior</td>
<td>272</td>
</tr>
<tr>
<td>When Do We Get to Inference?</td>
<td>274</td>
</tr>
<tr>
<td>Posterior Predictive Distribution</td>
<td>275</td>
</tr>
<tr>
<td>Happiness</td>
<td>276</td>
</tr>
<tr>
<td>Simple Regression</td>
<td>277</td>
</tr>
<tr>
<td>Multiple Regression</td>
<td>280</td>
</tr>
<tr>
<td>Summary</td>
<td>282</td>
</tr>
<tr>
<td>Exercises</td>
<td>283</td>
</tr>
<tr>
<td>20. Approximate Bayesian Computation.</td>
<td>287</td>
</tr>
<tr>
<td>The Kidney Tumor Problem</td>
<td>287</td>
</tr>
<tr>
<td>A Simple Growth Model</td>
<td>288</td>
</tr>
<tr>
<td>A More General Model</td>
<td>289</td>
</tr>
<tr>
<td>Simulation</td>
<td>291</td>
</tr>
<tr>
<td>Approximate Bayesian Computation</td>
<td>294</td>
</tr>
<tr>
<td>Counting Cells</td>
<td>295</td>
</tr>
<tr>
<td>Cell Counting with ABC</td>
<td>298</td>
</tr>
<tr>
<td>When Do We Get to the Approximate Part?</td>
<td>299</td>
</tr>
<tr>
<td>Summary</td>
<td>302</td>
</tr>
<tr>
<td>Exercises</td>
<td>303</td>
</tr>
<tr>
<td>Index.</td>
<td>305</td>
</tr>
</table>


<!-- PageNumber="viii Table of Contents" -->
<!-- PageBreak -->

<!-- PageHeader="Preface" -->

The premise of this book, and the other books in the Think $X$ series, is that if you
know how to program, you can use that skill to learn other topics.

Most books on Bayesian statistics use math notation and present ideas using mathe-
matical concepts like calculus. This book uses Python code and discrete approxima-
tions instead of continuous mathematics. As a result, what would be an integral in a
math book becomes a summation, and most operations on probability distributions
are loops or array operations.

I think this presentation is easier to understand, at least for people with programming
skills. It is also more general, because when we make modeling decisions, we can
choose the most appropriate model without worrying too much about whether the
model lends itself to mathematical analysis.

Also, it provides a smooth path from simple examples to real-world problems.


### Who Is This Book For?

To start this book, you should be comfortable with Python. If you are familiar with
NumPy and pandas, that will help, but I'll explain what you need as we go. You don't
need to know calculus or linear algebra. You don't need any prior knowledge of
statistics.

In Chapter 1, I define probability and introduce conditional probability, which is the
foundation of Bayes's theorem. Chapter 3 introduces the probability distribution,
which is the foundation of Bayesian statistics.

In later chapters, we use a variety of discrete and continuous distributions, including
the binomial, exponential, Poisson, beta, gamma, and normal distributions. I will
explain each distribution when it is introduced, and we will use SciPy to compute
them, so you don't need to know about their mathematical properties.

<!-- PageNumber="ix" -->
<!-- PageBreak -->


### Modeling

Most chapters in this book are motivated by a real-world problem, so they involve
some degree of modeling. Before we can apply Bayesian methods (or any other analy-
sis), we have to make decisions about which parts of the real-world system to include
in the model and which details we can abstract away.

For example, in Chapter 8, the motivating problem is to predict the winner of a soc-
cer (football) game. I model goal-scoring as a Poisson process, which implies that a
goal is equally likely at any point in the game. That is not exactly true, but it is proba-
bly a good enough model for most purposes.

I think it is important to include modeling as an explicit part of problem solving
because it reminds us to think about modeling errors (that is, errors due to simplifi-
cations and assumptions of the model).

Many of the methods in this book are based on discrete distributions, which makes
some people worry about numerical errors. But for real-world problems, numerical
errors are almost always smaller than modeling errors.

Furthermore, the discrete approach often allows better modeling decisions, and I
would rather have an approximate solution to a good model than an exact solution to
a bad model.


#### Working with the Code

Reading this book will only get you so far; to really understand it, you have to work
with the code. The original form of this book is a series of Jupyter notebooks. After
you read each chapter, I encourage you to run the notebook and work on the exerci-
ses. If you need help, my solutions are available.

There are several ways to run the notebooks:

· If you have Python and Jupyter installed, you can download the notebooks and
run them on your computer.

· If you don't have a programming environment where you can run Jupyter note-
books, you can use Colab, which lets you run Jupyter notebooks in a browser
without installing anything.

To run the notebooks on Colab, start from this landing page, which has links to all of
the notebooks.

If you already have Python and Jupyter, you can download the notebooks as a ZIP
file.

<!-- PageFooter="Preface" -->
<!-- PageNumber="$X$ ☒" -->
<!-- PageBreak -->

This book is here to help you get your job done. In general, if example code is offered
with this book, you may use it in your programs and documentation. You do not
need to contact us for permission unless you're reproducing a significant portion of
the code. For example, writing a program that uses several chunks of code from this
book does not require permission. Selling or distributing examples from O'Reilly
books does require permission. Answering a question by citing this book and quoting
example code does not require permission. Incorporating a significant amount of
example code from this book into your product's documentation does require per-
mission.

We appreciate, but generally do not require, attribution. An attribution usually
includes the title, author, publisher, and ISBN. For example: "Think Bayes, Second
Edition, by Allen B. Downey (O'Reilly). Copyright 2021 Allen B. Downey,
978-1-492-08946-9."

If you feel your use of code examples falls outside fair use or the permission given
above, feel free to contact O'Reilly Media at permissions@oreilly.com.


#### Installing Jupyter

If you don't have Python and Jupyter already, I recommend you install Anaconda,
which is a free Python distribution that includes all the packages you'll need. I found
Anaconda easy to install. By default it installs files in your home directory, so you
don't need administrator privileges. You can download Anaconda from this site.

Anaconda includes most of the packages you need to run the code in this book. But
there are a few additional packages you need to install.

To make sure you have everything you need (and the right versions), the best option
is to create a Conda environment. Download this Conda environment file and run
the following commands to create and activate an environment called ThinkBayes2:

conda env create -f environment. yml
conda activate ThinkBayes2

If you don't want to create an environment just for this book, you can install what you
need using Conda. The following commands should get everything you need:

conda install python jupyter pandas scipy matplotlib
pip install empiricaldist

If you don't want to use Anaconda, you will need the following packages:

· Jupyter to run the notebooks, https://jupyter.org;

· NumPy for basic numerical computation, https://numpy.org;

· SciPy for scientific computation, https://scipy.org;

<!-- PageFooter="Preface" -->
<!-- PageNumber="xi" -->
<!-- PageBreak -->

· pandas for working with data, https://pandas.pydata.org;

· matplotlib for visualization, https://matplotlib.org;

· empiricaldist for representing distributions, https://pypi.org/project/empiricaldist.

Although these are commonly used packages, they are not included with all Python
installations, and they can be hard to install in some environments. If you have trou-
ble installing them, I recommend using Anaconda or one of the other Python distri-
butions that include these packages.


### Conventions Used in This Book

The following typographical conventions are used in this book:

Italic

Indicates URLs, email addresses, filenames, and file extensions.

Bold

Indicates new and key terms.

Constant width

Used for program listings, as well as within paragraphs to refer to program ele-
ments such as variable or function names, databases, data types, environment
variables, statements, and keywords.


### O'Reilly Online Learning


#### O'REILLY® $\left( B \right.$

For more than 40 years, O'Reilly Media has provided technol-
ogy and business training, knowledge, and insight to help
companies succeed.

Our unique network of experts and innovators share their knowledge and expertise
through books, articles, and our online learning platform. O'Reilly's online learning
platform gives you on-demand access to live training courses, in-depth learning
paths, interactive coding environments, and a vast collection of text and video from
O'Reilly and 200+ other publishers. For more information, visit http://oreilly.com.

<!-- PageFooter="Preface" -->
<!-- PageNumber="xii" -->
<!-- PageBreak -->


### How to Contact Us

Please address comments and questions concerning this book to the publisher:

O'Reilly Media, Inc.
1005 Gravenstein Highway North
Sebastopol, CA 95472
800-998-9938 (in the United States or Canada)
707-829-0515 (international or local)
707-829-0104 (fax)

We have a web page for this book, where we list errata, examples, and any additional
information. You can access this page at https://oreil.ly/thinkBayes2e.

Email bookquestions@oreilly.com to comment or ask technical questions about this
book.

For news and information about our books and courses, visit http://oreilly.com.

Find us on Facebook: http://facebook.com/oreilly

Follow us on Twitter: http://twitter.com/oreillymedia

Watch us on YouTube: http://youtube.com/oreillymedia


#### Contributor List

If you have a suggestion or correction, please send email to downey@allendow-
ney.com. If I make a change based on your feedback, I will add you to the contributor
list (unless you ask to be omitted).

If you include at least part of the sentence the error appears in, that makes it easy for
me to search. Page and section numbers are fine, too, but not as easy to work with.
Thanks!

· First, I have to acknowledge David Mackay's excellent book, Information Theory,
Inference, and Learning Algorithms, which is where I first came to understand
Bayesian methods. With his permission, I use several problems from his book as
examples.

· Several examples and exercises in the second edition are borrowed, with permis-
sion, from Cameron Davidson-Pilon and one exercise from Rasmus Bååth.

· This book also benefited from my interactions with Sanjoy Mahajan, especially in
Fall 2012, when I audited his class on Bayesian Inference at Olin College.

<!-- PageFooter="Preface" -->
<!-- PageNumber="xiii" -->
<!-- PageBreak -->

· Many examples in this book were developed in collaboration with students in my
Bayesian Statistics classes at Olin College. In particular, the Red Line example
started as a class project by Brendan Ritter and Kai Austin.

· I wrote parts of this book during project nights with the Boston Python User
Group, so I would like to thank them for their company and pizza.

· Jasmine Kwityn and Dan Fauxsmith at O'Reilly Media proofread the first edition
and found many opportunities for improvement.

· Linda Pescatore found a typo and made some helpful suggestions.

· Tomasz Miasko sent many excellent corrections and suggestions.

· For the second edition, I want to thank Michele Cronin and Kristen Brown at
O'Reilly Media and the technical reviewers Ravin Kumar, Thomas Nield, Josh
Starmer, and Junpeng Lao.

· I am grateful to the developers and contributors of the software libraries this
book is based on, especially Jupyter, NumPy, SciPy, pandas, PyMC, ArviZ, and
Matplotlib.

Other people who spotted typos and errors include Greg Marra, Matt Aasted, Marcus
Ogren, Tom Pollard, Paul A. Giannaros, Jonathan Edwards, George Purkins, Robert
Marcus, Ram Limbu, James Lawry, Ben Kahle, Jeffrey Law, Alvaro Sanchez, Olivier
Yiptong, Yuriy Pasichnyk, Kristopher Overholt, Max Hailperin, Markus Dobler, Brad
Minch, Allen Minch, Nathan Yee, Michael Mera, Chris Krenn, and Daniel Vianna.

<!-- PageFooter="Preface" -->
<!-- PageNumber="xiv" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 1 Probability" -->

The foundation of Bayesian statistics is Bayes's theorem, and the foundation of Bayes's
theorem is conditional probability.

In this chapter, we'll start with conditional probability, derive Bayes's theorem, and
demonstrate it using a real dataset. In the next chapter, we'll use Bayes's theorem to
solve problems related to conditional probability. In the chapters that follow, we'll
make the transition from Bayes's theorem to Bayesian statistics, and I'll explain the
difference.


#### Linda the Banker

To introduce conditional probability, I'll use an example from a famous experiment
by Tversky and Kahneman, who posed the following question:

Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy.
As a student, she was deeply concerned with issues of discrimination and social justice,
and also participated in anti-nuclear demonstrations. Which is more probable?

1\. Linda is a bank teller.

2\. Linda is a bank teller and is active in the feminist movement.

Many people choose the second answer, presumably because it seems more consistent
with the description. It seems uncharacteristic if Linda is just a bank teller; it seems
more consistent if she is also a feminist.

But the second answer cannot be "more probable", as the question asks. Suppose we
find 1,000 people who fit Linda's description and 10 of them work as bank tellers.
How many of them are also feminists? At most, all 10 of them are; in that case, the
two options are equally probable. If fewer than 10 are, the second option is less proba-
ble. But there is no way the second option can be more probable.

<!-- PageNumber="1" -->
<!-- PageBreak -->

If you were inclined to choose the second option, you are in good company. The biol-
ogist Stephen J. Gould wrote:

I am particularly fond of this example because I know that the [second] statement is
least probable, yet a little homunculus in my head continues to jump up and down,
shouting at me, "but she can't just be a bank teller; read the description."

If the little person in your head is still unhappy, maybe this chapter will help.


##### Probability

At this point I should provide a definition of "probability", but that turns out to be
surprisingly difficult. To avoid getting stuck before we start, we will use a simple defi-
nition for now and refine it later: A probability is a fraction of a finite set.

For example, if we survey 1,000 people, and 20 of them are bank tellers, the fraction
that work as bank tellers is 0.02 or 2%. If we choose a person from this population at
random, the probability that they are a bank teller is 2%. By "at random" I mean that
every person in the dataset has the same chance of being chosen.

With this definition and an appropriate dataset, we can compute probabilities by
counting. To demonstrate, I'll use data from the General Social Survey (GSS).

I'll use pandas to read the data and store it in a DataFrame.

import pandas as pd

gss = pd. read_csv('gss_bayes.csv', index_col=0)
gss. head()


<table>
<tr>
<th></th>
<th>year</th>
<th>age</th>
<th>sex</th>
<th>polviews</th>
<th>partyid</th>
<th>indus 10</th>
</tr>
<tr>
<td colspan="7">caseid</td>
</tr>
<tr>
<td>1</td>
<td>1974</td>
<td>21.0</td>
<td>1</td>
<td>4.0</td>
<td>2.0</td>
<td>4970.0</td>
</tr>
<tr>
<td>2</td>
<td>1974</td>
<td>41.0</td>
<td>1</td>
<td>5.0</td>
<td>0.0</td>
<td>9160.0</td>
</tr>
<tr>
<td>5</td>
<td>1974</td>
<td>58.0</td>
<td>2</td>
<td>6.0</td>
<td>1.0</td>
<td>2670.0</td>
</tr>
<tr>
<td>6</td>
<td>1974</td>
<td>30.0</td>
<td>1</td>
<td>5.0</td>
<td>4.0</td>
<td>6870.0</td>
</tr>
<tr>
<td>7</td>
<td>1974</td>
<td>48.0</td>
<td>1</td>
<td>5.0</td>
<td>4.0</td>
<td>7860.0</td>
</tr>
</table>


The DataFrame has one row for each person surveyed and one column for each vari-
able I selected.

<!-- PageFooter="Chapter 1: Probability" -->
<!-- PageNumber="2" -->
<!-- PageBreak -->

The columns are

· caseid: Respondent id (which is the index of the table).

· year: Year when the respondent was surveyed.

· age: Respondent's age when surveyed.

· sex: Male or female.

· polviews: Political views on a range from liberal to conservative.

· partyid: Political party affiliation: Democratic, Republican, or independent.

· indus10: Code for the industry the respondent works in.

Let's look at these variables in more detail, starting with indus10.


##### Fraction of Bankers

The code for "Banking and related activities" is 6870, so we can select bankers like
this:

banker = (gss['indus10'] == 6870)
banker . head()

caseid

1
False

2
False

5
False

6
True

7
False

Name: indus10, dtype: bool

The result is a pandas Series that contains the Boolean values True and False.

If we use the sum function on this Series, it treats True as 1 and False as 0, so the
total is the number of bankers:

banker.sum()

728

In this dataset, there are 728 bankers.

To compute the fraction of bankers, we can use the mean function, which computes
the fraction of True values in the $\mathrm { S e r } \mathrm { i e s } :$

banker.mean()

0.014769730168391155

About 1.5% of the respondents work in banking, so if we choose a random person
from the dataset, the probability they are a banker is about 1.5%.

<!-- PageFooter="Fraction of Bankers" -->
<!-- PageNumber="3" -->
<!-- PageBreak -->


#### The Probability Function

I'll put the code from the previous section in a function that takes a Boolean Series
and returns a probability:

def $\mathrm { p r o b } \left( \mathrm { A } \right) :$
"""Computes the probability of a proposition, A. """
return A. mean()

So we can compute the fraction of bankers like this:

prob(banker)

0.014769730168391155

Now let's look at another variable in this dataset. The values of the column $\sec x$ are
encoded like this:

1
Male

2
Female

So we can make a Boolean Series that is True for female respondents and False
otherwise:

$$= \left( g s s \left[ ^ { \prime } s e x ^ { \prime } \right] = = 2 \right)$$

And use it to compute the fraction of respondents who are women:

prob(female)

0.5378575776019476

The fraction of women in this dataset is higher than in the adult US population
because the GSS doesn't include people living in institutions like prisons and military
housing, and those populations are more likely to be male.


#### Political Views and Parties

The other variables we'll consider are polviews, which describes the political views of
the respondents, and partyid, which describes their affiliation with a political party.

The values of polviews are on a seven-point scale:

1
Extremely liberal

2
Liberal

3
Slightly liberal

4
Moderate

5
Slightly conservative

6
Conservative

7
Extremely conservative

I'll define liberal to be True for anyone whose response is "Extremely liberal",
"Liberal", or "Slightly liberal":

<!-- PageFooter="Chapter 1: Probability" -->
<!-- PageNumber="4" -->
<!-- PageBreak -->

liberal = (gss['polviews' ] <= 3)

Here's the fraction of respondents who are liberal by this definition:

prob(liberal)

0.27374721038750255

If we choose a random person in this dataset, the probability they are liberal is about
27%.

The values of partyid are encoded like this:

0
Strong democrat

1
Not strong democrat

2
Independent, near democrat

3
Independent

4
Independent, near republican

5
Not strong republican

6
Strong republican

7
Other party

I'll define democrat to include respondents who chose "Strong democrat" or "Not
strong democrat":

$$= \left( g s s \left[ ^ { \prime } \text { partyid } ^ { \prime } \right] < = 1 \right)$$

And here's the fraction of respondents who are Democrats, by this definition:

prob(democrat)

0.3662609048488537


##### Conjunction

Now that we have a definition of probability and a function that computes it, let's
move on to conjunction.

"Conjunction" is another name for the logical and operation. If you have two proposi-
tions, $A$ and B, the conjunction $A$ and B is True if both $A$ and B are True, and False
otherwise.

If we have two Boolean Series, we can use the & operator to compute their conjunc-
tion. For example, we have already computed the probability that a respondent is a
banker:

prob(banker)

0.014769730168391155

And the probability that they are a Democrat:

$$\mathrm { p r o b } \left( \mathrm { d e m o c r a t } \right)$$

0.3662609048488537

<!-- PageFooter="Conjunction 5" -->
<!-- PageBreak -->

Now we can compute the probability that a respondent is a banker and a Democrat:

prob(banker & democrat)

0.004686548995739501

As we should expect, prob(banker & democrat) is less than prob(banker ), because
not all bankers are Democrats.

We expect conjunction to be commutative; that is, A & B should be the same as B &
A. To check, we can also compute prob(democrat & banker):

prob(democrat & banker)

0.004686548995739501

As expected, they are the same.


##### Conditional Probability

Conditional probability is a probability that depends on a condition, but that might
not be the most helpful definition. Here are some examples:

· What is the probability that a respondent is a Democrat, given that they are
liberal?

· What is the probability that a respondent is female, given that they are a banker?

· What is the probability that a respondent is liberal, given that they are female?

Let's start with the first one, which we can interpret like this: "Of all the respondents
who are liberal, what fraction are Democrats?"

We can compute this probability in two steps:

1\. Select all respondents who are liberal.

2\. Compute the fraction of the selected respondents who are Democrats.

To select liberal respondents, we can use the bracket operator, [ ], like this:

selected = democrat[liberal]

selected contains the values of democrat for liberal respondents, so $\mathrm { p r o b } \left( \mathrm { s e l e c t e d } \right)$
is the fraction of liberals who are Democrats:

prob(selected)

0.5206403320240125

A little more than half of liberals are Democrats. If that result is lower than you
expected, keep in mind:

<!-- PageFooter="Chapter 1: Probability" -->
<!-- PageNumber="6" -->
<!-- PageBreak -->

1\. We used a somewhat strict definition of "Democrat", excluding independents
who "lean" Democratic.

2\. The dataset includes respondents as far back as 1974; in the early part of this
interval, there was less alignment between political views and party affiliation,
compared to the present.

Let's try the second example, "What is the probability that a respondent is female,
given that they are a banker?" We can interpret that to mean, "Of all respondents who
are bankers, what fraction are female?"

Again, we'll use the bracket operator to select only the bankers and prob to compute
the fraction that are female:

$$s e l e c t e d = f e m a l e \left[ b a n k e r \right]$$

prob(selected)
0.7706043956043956

About 77% of the bankers in this dataset are female.

Let's wrap this computation in a function. I'll define conditional to take two
Boolean Series, proposition and given, and compute the conditional probability of
proposition conditioned on given:

def conditional(proposition, given):
return prob(proposition[given])

We can use conditional to compute the probability that a respondent is liberal given
that they are female:

conditional(liberal, given=female)
0.27581004111500884

About 28% of female respondents are liberal.

I included the keyword, given, along with the parameter, female, to make this
expression more readable.


##### Conditional Probability Is Not Commutative

We have seen that conjunction is commutative; that is, $\mathrm { p r o b } \left( A 8 B \right)$ is always equal
to $\mathrm { p r o b } \left( B 8 A \right) .$

But conditional probability is not commutative; that is, conditional(A, B) is not the
same as conditional(B, A).

That should be clear if we look at an example. Previously, we computed the probabil-
ity a respondent is female, given that they are a banker.

<!-- PageFooter="Conditional Probability Is Not Commutative" -->
<!-- PageNumber="7" -->
<!-- PageBreak -->

conditional(female, given=banker)

0.7706043956043956

The result shows that the majority of bankers are female. That is not the same as the
probability that a respondent is a banker, given that they are female:

conditional(banker, given=female)
0.02116102749801969

Only about 2% of female respondents are bankers.

I hope this example makes it clear that conditional probability is not commutative,
and maybe it was already clear to you. Nevertheless, it is a common error to confuse
conditional(A, B) and conditional(B, A). We'll see some examples later.


##### Condition and Conjunction

We can combine conditional probability and conjunction. For example, here's the
probability a respondent is female, given that they are a liberal Democrat:

conditional(female, given=liberal & democrat)
0.576085409252669

About 57% of liberal Democrats are female.

And here's the probability they are a liberal female, given that they are a banker:
conditional(liberal & female, given=banker)
0.17307692307692307

About 17% of bankers are liberal women.


##### Laws of Probability

In the next few sections, we'll derive three relationships between conjunction and
conditional probability:

· Theorem 1: Using a conjunction to compute a conditional probability.

· Theorem 2: Using a conditional probability to compute a conjunction.

· Theorem 3: Using conditional(A, B) to compute conditional(B, A).

Theorem 3 is also known as Bayes's theorem.

I'll write these theorems using mathematical notation for probability:

· $P \left( A \right)$ is the probability of proposition $A .$

<!-- PageFooter="Chapter 1: Probability" -->
<!-- PageNumber="8" -->
<!-- PageBreak -->

· $P \left( A \quad a n d \quad B \right)$ is the probability of the conjunction of $A$ and $B ,$ that is, the probabil-
ity that both are true.

· $P \left( A | B \right)$ is the conditional probability of $A$ given that $B$ is true. The vertical line
between $A$ and $B$ is pronounced "given".

With that, we are ready for Theorem 1.


#### Theorem 1

What fraction of bankers are female? We have already seen one way to compute the
answer:

1\. Use the bracket operator to select the bankers, then

2\. Use mean to compute the fraction of bankers who are female.

We can write these steps like this:

female[banker ]. mean()
0.7706043956043956

Or we can use the conditional function, which does the same thing:

conditional(female, given=banker)
0.7706043956043956

But there is another way to compute this conditional probability, by computing the
ratio of two probabilities:

1\. The fraction of respondents who are female bankers, and

2\. The fraction of respondents who are bankers.

In other words: of all the bankers, what fraction are female bankers? Here's how we
compute this ratio:

prob(female & banker) / prob(banker)

0.7706043956043956

The result is the same. This example demonstrates a general rule that relates condi-
tional probability and conjunction. Here's what it looks like in math notation:

$$P \left( A | B \right) = \frac { P \left( A \text { and } B \right) } { P \left( B \right) }$$

And that's Theorem 1.

<!-- PageFooter="Laws of Probability" -->
<!-- PageNumber="9" -->
<!-- PageBreak -->


#### Theorem 2

If we start with Theorem 1 and multiply both sides by $P \left( B \right) ,$ we get Theorem 2:

$$P \left( A \quad a n d \quad B \right) = P \left( B \right) P \left( A | B \right)$$

This formula suggests a second way to compute a conjunction: instead of using the &
operator, we can compute the product of two probabilities.

Let's see if it works for liberal and democrat. Here's the result using &:

prob(liberal & democrat)

0.1425238385067965

And here's the result using Theorem 2:

$$\mathrm { p r o b } \left( \mathrm { d e m o c r a t } \right) * \mathrm { c o n d i t i o n a l } \left( \mathrm { l i b e r a l } , \mathrm { d e m o c r a t } \right)$$

0.1425238385067965

They are the same.


#### Theorem 3

We have established that conjunction is commutative. In math notation, that means:

$$P \left( A \quad a n d \quad B \right) = P \left( B \quad a n d \quad A \right)$$

If we apply Theorem 2 to both sides, we have:

$$P \left( B \right) P \left( A | B \right) = P \left( A \right) P \left( B | A \right)$$

Here's one way to interpret that: if you want to check $A$ and $B ,$ you can do it in either
order:

1\. You can check $B$ first, then $A$ conditioned on $B ,$ or

2\. You can check $A$ first, then $B$ conditioned on $A .$

If we divide through by $P \left( B \right) ,$ we get Theorem 3:

$$P \left( A | B \right) = \frac { P \left( A \right) P \left( B | A \right) } { P \left( B \right) }$$

And that, my friends, is Bayes's theorem.

<!-- PageFooter="Chapter 1: Probability" -->
<!-- PageNumber="10" -->
<!-- PageBreak -->

To see how it works, let's compute the fraction of bankers who are liberal, first using
conditional:

conditional(liberal, given=banker)
0.2239010989010989

Now using Bayes's theorem:

prob(liberal) * conditional(banker, liberal) / prob(banker)
0.2239010989010989

They are the same.


##### The Law of Total Probability

In addition to these three theorems, there's one more thing we'll need to do Bayesian
statistics: the law of total probability. Here's one form of the law, expressed in mathe-
matical notation:

$$P \left( A \right) = P \left( B _ { 1 } \text { and } A \right) + P \left( B _ { 2 } \text { and } A \right)$$

In words, the total probability of $A$ is the sum of two possibilities: either $B _ { 1 }$ and $A$ are
true or $B _ { 2 }$ and $A$ are true. But this law applies only if $B _ { 1 }$ and $B _ { 2 }$ are:

· Mutually exclusive, which means that only one of them can be true, and

· Collectively exhaustive, which means that one of them must be true.

As an example, let's use this law to compute the probability that a respondent is a
banker. We can compute it directly like this:

prob(banker)

0.014769730168391155

So let's confirm that we get the same thing if we compute male and female bankers
separately.

In this dataset all respondents are designated male or female. Recently, the GSS Board
of Overseers announced that they will add more inclusive gender questions to the
survey (you can read more about this issue, and their decision, at https://oreil.ly/
$\left. o n K 2 P \right) .$

We already have a Boolean Series that is True for female respondents. Here's the
complementary Series for male respondents:

$$= \left( g s s \left[ ^ { \prime } s e x ^ { \prime } \right] = = 1 \right)$$

Now we can compute the total probability of banker like this:

<!-- PageFooter="Laws of Probability" -->
<!-- PageNumber="11" -->
<!-- PageBreak -->

prob(male & banker) + prob(female & banker)

0.014769730168391155

Because $\mathrm { m a l e }$ and female are mutually exclusive and collectively exhaustive (MECE),
we get the same result we got by computing the probability of banker directly.

Applying Theorem 2, we can also write the law of total probability like this:

$$P \left( A \right) = P \left( B _ { 1 } \right) P \left( A | B _ { 1 } \right) + P \left( B _ { 2 } \right) P \left( A | B _ { 2 } \right)$$

And we can test it with the same example:

$$\left( \mathrm { p r o b } \left( \mathrm { m a l e } \right) ^ { * } \mathrm { c o n d i t i o n a l } \left( \mathrm { b a n k e r } , \mathrm { g i v e n } = \mathrm { m a l e } \right) + \right.$$
$$\left. \mathrm { p r o b } \left( \mathrm { f e m a l e } \right) * \mathrm { c o n d i t t i o n a l } \left( \mathrm { b a n k e r } , \mathrm { g i v e n } = \mathrm { f e m a l e } \right) \right)$$

0.014769730168391153

When there are more than two conditions, it is more concise to write the law of total
probability as a summation:

$$P \left( A \right) = \sum _ { i } P \left( B _ { i } \right) P \left( A | B _ { i } \right)$$

Again, this holds as long as the conditions $B _ { i }$ are mutually exclusive and collectively
exhaustive. As an example, let's consider polviews, which has seven different values:

$B = g s s \left[ ^ { \prime } p o l v i e w s ^ { \prime } \right]$
B. value_counts() . sort_index()

1.0

1442

2.0

5808

3.0

6243

4.0

18943

5.0

7940

6.0

7319

7.0

1595

Name: polviews, dtype: int64

On this scale, 4.0 represents "Moderate". So we can compute the probability of a
moderate banker like this:

$i = 4$

$$\left. \mathrm { p r o b } \left( B = = i \right) * \text { conditional \left(banker, } B = = i \right)$$

0.005822682085615744

<!-- PageFooter="Chapter 1: Probability" -->
<!-- PageNumber="12" -->
<!-- PageBreak -->

And we can use sum and a generator expression to compute the summation:

$$\sin \left( \mathrm { p r o b } \left( B = = i \right) * \text { conditional } \left( \text { banker } , B = = i \right) \right.$$

for i in range(1, 8))
0.014769730168391157

The result is the same.

In this example, using the law of total probability is a lot more work than computing
the probability directly, but it will turn out to be useful, I promise.


##### Summary

Here's what we have so far:

Theorem 1 gives us a way to compute a conditional probability using a conjunction:

$$P \left( A | B \right) = \frac { P \left( A \text { and } B \right) } { P \left( B \right) }$$

Theorem 2 gives us a way to compute a conjunction using a conditional probability:

$$P \left( A \quad a n d \quad B \right) = P \left( B \right) P \left( A | B \right)$$

Theorem 3, also known as Bayes's theorem, gives us a way to get from $P \left( A | B \right)$ to
$P \left( B | A \right) ,$ or the other way around:

$$P \left( A | B \right) = \frac { P \left( A \right) P \left( B | A \right) } { P \left( B \right) }$$

The Law of Total Probability provides $a$ way to compute probabilities by adding up
the pieces:

$$P \left( A \right) = \sum _ { i } P \left( B _ { i } \right) P \left( A | B _ { i } \right)$$

At this point you might ask, "So what?" If we have all of the data, we can compute any
probability we want, any conjunction, or any conditional probability, just by count-
ing. We don't have to use these formulas.

And you are right, if we have all of the data. But often we don't, and in that case, these
formulas can be pretty useful-especially Bayes's theorem. In the next chapter, we'll
see how.

<!-- PageFooter="Summary" -->
<!-- PageNumber="13" -->
<!-- PageBreak -->


## Exercises


### Exercise 1-1.

Let's use the tools in this chapter to solve a variation of the Linda problem.

Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy.
As a student, she was deeply concerned with issues of discrimination and social justice,
and also participated in anti-nuclear demonstrations. Which is more probable?

1\. Linda is a banker.

2\. Linda is a banker and considers herself a liberal Democrat.

To answer this question, compute

· The probability that Linda is a female banker,

· The probability that Linda is a liberal female banker, and

· The probability that Linda is a liberal female banker and a Democrat.


### Exercise 1-2.

Use conditional to compute the following probabilities:

· What is the probability that a respondent is liberal, given that they are a
Democrat?

· What is the probability that a respondent is a Democrat, given that they are
liberal?

Think carefully about the order of the arguments you pass to conditional.


### Exercise 1-3.

There's a famous quote about young people, old people, liberals, and conservatives
that goes something like:

If you are not a liberal at 25, you have no heart. If you are not a conservative at 35, you
have no brain.

Whether you agree with this proposition or not, it suggests some probabilities we can
compute as an exercise. Rather than use the specific ages 25 and 35, let's define young
and old as under 30 or over 65:

$$= \left( g s s \left[ ^ { \prime } \text { age } ^ { \prime } \right] < 3 0 \right)$$

prob(young)
0.19435991073240008

<!-- PageFooter="Chapter 1: Probability" -->
<!-- PageNumber="14" -->
<!-- PageBreak -->

$o l d = \left( g s s \left[ ^ { \prime } a g e ^ { \prime } \right] > = 6 5 \right)$
prob(old)

0.17328058429701765

For these thresholds, I chose round numbers near the 20th and 80th percentiles.
Depending on your age, you may or may not agree with these definitions of "young"
and "old".

I'll define conservative as someone whose political views are "Conservative",
"Slightly Conservative", or "Extremely Conservative".

conservative = (gss['polviews' ] >= 5)
prob(conservative)
0.3419354838709677

Use prob and conditional to compute the following probabilities:

· What is the probability that a randomly chosen respondent is a young liberal?

· What is the probability that a young person is liberal?

· What fraction of respondents are old conservatives?

· What fraction of conservatives are old?

For each statement, think about whether it is expressing a conjunction, a conditional
probability, or both.

For the conditional probabilities, be careful about the order of the arguments. If your
answer to the last question is greater than 30%, you have it backwards!

<!-- PageFooter="Exercises" -->
<!-- PageNumber="15" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 2" -->


## Bayes's Theorem

In the previous chapter, we derived Bayes's theorem:

$$P \left( A | B \right) = \frac { P \left( A \right) P \left( B | A \right) } { P \left( B \right) }$$

As an example, we used data from the General Social Survey and Bayes's theorem to
compute conditional probabilities. But since we had the complete dataset, we didn't
really need Bayes's theorem. It was easy enough to compute the left side of the equa-
tion directly, and no easier to compute the right side.

But often we don't have a complete dataset, and in that case Bayes's theorem is more
useful. In this chapter, we'll use it to solve several more challenging problems related
to conditional probability.


### The Cookie Problem

We'll start with a thinly disguised version of an urn problem:

Suppose there are two bowls of cookies.

· Bowl 1 contains 30 vanilla cookies and 10 chocolate cookies.

· Bowl 2 contains 20 vanilla cookies and 20 chocolate cookies.

Now suppose you choose one of the bowls at random and, without looking, choose a
cookie at random. If the cookie is vanilla, what is the probability that it came from
Bowl 1?

What we want is the conditional probability that we chose from Bowl 1 given that we
got a vanilla cookie, $P \left( B _ { 1 } | V \right) .$

<!-- PageNumber="17" -->
<!-- PageBreak -->

But what we get from the statement of the problem is:

· The conditional probability of getting a vanilla cookie, given that we chose from
Bowl 1, $P \left( V | B _ { 1 } \right)$ and

· The conditional probability of getting a vanilla cookie, given that we chose from
Bowl 2, $P \left( V | B _ { 2 } \right) .$

Bayes's theorem tells us how they are related:

$$P \left( B _ { 1 } | V \right) = \frac { P \left( B _ { 1 } \right) P \left( V | B _ { 1 } \right) } { P \left( V \right) }$$

The term on the left is what we want. The terms on the right are:

· $P \left( B _ { 1 } \right) ,$ the probability that we chose Bowl 1, unconditioned by what kind of
cookie we got. Since the problem says we chose a bowl at random, we assume
$P \left( B _ { 1 } \right) = 1 / 2 .$

· $P \left( V | B _ { 1 } \right) ,$ the probability of getting a vanilla cookie from Bowl 1, which is $3 / 4 .$

· $P \left( V \right) ,$ the probability of drawing a vanilla cookie from either bowl.

To compute $P \left( V \right) ,$ we can use the law of total probability:

$$P \left( V \right) = P \left( B _ { 1 } \right) P \left( V | B _ { 1 } \right) + P \left( B _ { 2 } \right) P \left( V | B _ { 2 } \right)$$

Plugging in the numbers from the statement of the problem, we have:

$$P \left( V \right) = \left( 1 / 2 \right) \left( 3 / 4 \right) + \left( 1 / 2 \right) \left( 1 / 2 \right) = 5 / 8$$

We can also compute this result directly, like this:

· Since we had an equal chance of choosing either bowl and the bowls contain the
same number of cookies, we had the same chance of choosing any cookie.

· Between the two bowls there are 50 vanilla and 30 chocolate cookies, so
$P \left( V \right) = 5 / 8 .$

Finally, we can apply Bayes's theorem to compute the posterior probability of Bowl 1:

$$P \left( B _ { 1 } | V \right) = \left( 1 / 2 \right) \left( 3 / 4 \right) / \left( 5 / 8 \right) = 3 / 5$$

<!-- PageFooter="Chapter 2: Bayes's Theorem" -->
<!-- PageNumber="18" -->
<!-- PageBreak -->

This example demonstrates one use of Bayes's theorem: it provides a way to get from
$P \left( B | A \right)$ to $P \left( A | B \right) .$ This strategy is useful in cases like this where it is easier to com-
pute the terms on the right side than the term on the left.


#### Diachronic Bayes

There is another way to think of Bayes's theorem: it gives us a way to update the prob-
ability of a hypothesis, $H ,$ given some body of data, $D .$

This interpretation is "diachronic", which means "related to change over time"; in this
case, the probability of the hypotheses changes as we see new data.

Rewriting Bayes's theorem with $H$ and $D$ yields:

$$P \left( H | D \right) = \frac { P \left( H \right) P \left( D | H \right) } { P \left( D \right) }$$

In this interpretation, each term has a name:

· $P \left( H \right)$ is the probability of the hypothesis before we see the data, called the prior
probability, or just prior.

· $P \left( H | D \right)$ is the probability of the hypothesis after we see the data, called the
posterior.

· $P \left( D | H \right)$ is the probability of the data under the hypothesis, called the likelihood.

· $P \left( D \right)$ is the total probability of the data, under any hypothesis.

Sometimes we can compute the prior based on background information. For exam-
ple, the Cookie Problem specifies that we choose a bowl at random with equal
probability.

In other cases the prior is subjective; that is, reasonable people might disagree, either
because they use different background information or because they interpret the
same information differently.

The likelihood is usually the easiest part to compute. In the Cookie Problem, we are
given the number of cookies in each bowl, so we can compute the probability of the
data under each hypothesis.

Computing the total probability of the data can be tricky. It is supposed to be the
probability of seeing the data under any hypothesis at all, but it can be hard to nail
down what that means.

Most often we simplify things by specifying a set of hypotheses that are:

<!-- PageFooter="Diachronic Bayes" -->
<!-- PageNumber="19" -->
<!-- PageBreak -->

· Mutually exclusive, which means that only one of them can be true, and

· Collectively exhaustive, which means one of them must be true.

When these conditions apply, we can compute $P \left( D \right)$ using the law of total probability.
For example, with two hypotheses, $H _ { 1 }$ and $H _ { 2 } :$

$$P \left( D \right) = P \left( H _ { 1 } \right) P \left( D | H _ { 1 } \right) + P \left( H _ { 2 } \right) P \left( D | H _ { 2 } \right)$$

And more generally, with any number of hypotheses:

$$P \left( D \right) = \sum _ { i } P \left( H _ { i } \right) P \left( D | H _ { i } \right)$$

The process in this section, using data and a prior probability to compute a posterior
probability, is called a Bayesian update.


#### Bayes Tables

A convenient tool for doing a Bayesian update is a Bayes table. You can write a Bayes
table on paper or use a spreadsheet, but in this section I'll use a pandas DataFrame.

First I'll make an empty DataFrame with one row for each hypothesis:

import pandas as pd

table = pd. DataFrame(index=[ 'Bowl 1', 'Bowl 2'])

Now I'll add a column to represent the priors:

table['prior' $\left. \right] = 1 / 2 ,$ $1 / 2$
table

prior


<table>
<tr>
<td>Bowl 1</td>
<td>0.5</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.5</td>
</tr>
</table>


And a column for the likelihoods:

table['likelihood' ] = 3/4, $1 / 2$
table

prior
likelihood


<table>
<tr>
<td>Bowl 1</td>
<td>0.5</td>
<td>0.75</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.5</td>
<td>0.50</td>
</tr>
</table>


<!-- PageFooter="Chapter 2: Bayes's Theorem" -->
<!-- PageNumber="20" -->
<!-- PageBreak -->

Here we see a difference from the previous method: we compute likelihoods for both
hypotheses, not just Bowl 1:

· The chance of getting a vanilla cookie from Bowl 1 is $3 / 4 .$

· The chance of getting a vanilla cookie from Bowl 2 is $1 / 2 .$

You might notice that the likelihoods don't add up to 1. That's OK; each of them is a
probability conditioned on a different hypothesis. There's no reason they should add
up to 1 and no problem if they don't.

The next step is similar to what we did with Bayes's theorem; we multiply the priors
by the likelihoods:

$$\mathrm { t a b l e } \left[ ^ { \prime } \mathrm { u n n o r m } ^ { \prime } \right] = \mathrm { t a b l e } \left[ ^ { \prime } \mathrm { p r } i o r ^ { \prime } \right] * \mathrm { t a b l e } \left[ ^ { \prime } l i k e l i h o o d ^ { \prime } \right]$$

table


<table>
<tr>
<th></th>
<th>prior</th>
<th>likelihood</th>
<th>unnorm</th>
</tr>
<tr>
<td>Bowl 1</td>
<td>0.5</td>
<td>0.75</td>
<td>0.375</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.5</td>
<td>0.50</td>
<td>0.250</td>
</tr>
</table>


I call the result unnorm because these values are the "unnormalized posteriors". Each
of them is the product of a prior and a likelihood

$$P \left( B _ { i } \right) P \left( D | B _ { i } \right)$$

which is the numerator of Bayes's theorem. If we add them up, we have

$$P \left( B _ { 1 } \right) P \left( D | B _ { 1 } \right) + P \left( B _ { 2 } \right) P \left( D | B _ { 2 } \right)$$

which is the denominator of Bayes's theorem, $P \left( D \right) .$

So we can compute the total probability of the data like this:

$$\mathrm { p r o b } _ { - } d a t a = t a b l e \left[ ^ { \prime } \text { unnorm } ^ { \prime } \right] . s u m \left( \right)$$

prob_data
0.625

Notice that we get $5 / 8 ,$ which is what we got by computing $P \left( D \right)$ directly.

And we can compute the posterior probabilities like this:

table['posterior' ] = table['unnorm' ] / prob_data
table

<!-- PageFooter="Bayes Tables" -->
<!-- PageNumber="21" -->
<!-- PageBreak -->


<table>
<tr>
<th></th>
<th>prior</th>
<th>likelihood</th>
<th>unnorm</th>
<th>posterior</th>
</tr>
<tr>
<td>Bowl 1</td>
<td>0.5</td>
<td>0.75</td>
<td>0.375</td>
<td>0.6</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.5</td>
<td>0.50</td>
<td>0.250</td>
<td>0.4</td>
</tr>
</table>


The posterior probability for Bowl 1 is 0.6, which is what we got using Bayes's theo-
rem explicitly. As a bonus, we also get the posterior probability of Bowl 2, which is
0.4.

When we add up the unnormalized posteriors and divide through, we force the pos-
teriors to add up to 1. This process is called "normalization", which is why the total
probability of the data is also called the "normalizing constant".


#### The Dice Problem

A Bayes table can also solve problems with more than two hypotheses. For example:

Suppose I have a box with a 6-sided die, an 8-sided die, and a 12-sided die. I choose
one of the dice at random, roll it, and report that the outcome is a 1. What is the prob-
ability that I chose the 6-sided die?

In this example, there are three hypotheses with equal prior probabilities. The data is
my report that the outcome is a 1.

If I chose the 6-sided die, the probability of the data is 1/6. If I chose the 8-sided die,
the probability is $1 / 8 ,$ and if I chose the 12-sided die, it's $1 / 1 2 .$

Here's a Bayes table that uses integers to represent the hypotheses:

table2 = pd. DataFrame(index=[6, 8, 12])

I'll use fractions to represent the prior probabilities and the likelihoods. That way
they don't get rounded off to floating-point numbers.


##### from fractions import Fraction

table2['prior'] = Fraction(1, 3)
table2['likelihood'] = Fraction(1, 6), Fraction(1, 8), Fraction(1, 12)
table2

prior
likelihood


<table>
<tr>
<td>6</td>
<td>$1 / 3$</td>
<td>$1 / 6$</td>
</tr>
<tr>
<td>8</td>
<td>$1 / 3$</td>
<td>$1 / 8$</td>
</tr>
<tr>
<td>12</td>
<td>$1 / 3$</td>
<td>$1 / 1 2$</td>
</tr>
</table>


Once you have priors and likelihoods, the remaining steps are always the same, so I'll
put them in a function:

<!-- PageFooter="Chapter 2: Bayes's Theorem" -->
<!-- PageNumber="22" -->
<!-- PageBreak -->

def update(table) :

Compute the posterior probabilities.
table['unnorm' ] = table['prior' ] * table['likelihood' ]
prob_data = table['unnorm' ]. sum()
table[ 'posterior' ] = table['unnorm' ] / prob_data
return prob_data

And call it like this:

$$p r o b \_ d a t a = u p d a t e \left( t a b l e 2 \right)$$


<table>
<caption>Here is the final Bayes table: table2</caption>
<tr>
<th></th>
<th>prior</th>
<th>likelihood</th>
<th>unnorm</th>
<th>posterior</th>
</tr>
<tr>
<td>6</td>
<td>$1 / 3$</td>
<td>1/6</td>
<td>$1 / 1 8$</td>
<td>$4 / 9$</td>
</tr>
<tr>
<td>8</td>
<td>$1 / 3$</td>
<td>$1 / 8$</td>
<td>$1 / 2 4$</td>
<td>$1 / 3$</td>
</tr>
<tr>
<td>12</td>
<td>$1 / 3$</td>
<td>$1 / 1 2$</td>
<td>1/36</td>
<td>$2 / 9$</td>
</tr>
</table>


The posterior probability of the 6-sided die is 4/9, which is a little more than the
probabilities for the other dice, $3 / 9$ and 2/9. Intuitively, the 6-sided die is the most
likely because it had the highest likelihood of producing the outcome we saw.


#### The Monty Hall Problem

Next we'll use a Bayes table to solve one of the most contentious problems in
probability.

The Monty Hall Problem is based on a game show called Let's Make a Deal. If you are
a contestant on the show, here's how the game works:

· The host, Monty Hall, shows you three closed doors-numbered 1, 2, and 3-and
tells you that there is a prize behind each door.

· One prize is valuable (traditionally a car), the other two are less valuable (tradi-
tionally goats).

· The object of the game is to guess which door has the car. If you guess right, you
get to keep the car.

Suppose you pick Door 1. Before opening the door you chose, Monty opens Door 3
and reveals a goat. Then Monty offers you the option to stick with your original
choice or switch to the remaining unopened door.

To maximize your chance of winning the car, should you stick with Door 1 or switch
to Door 2?

<!-- PageFooter="The Monty Hall Problem" -->
<!-- PageNumber="23" -->
<!-- PageBreak -->

To answer this question, we have to make some assumptions about the behavior of
the host:

1\. Monty always opens a door and offers you the option to switch.

2\. He never opens the door you picked or the door with the car.

3\. If you choose the door with the car, he chooses one of the other doors at random.

Under these assumptions, you are better off switching. If you stick, you win $1 / 3$ of the
time. If you switch, you win $2 / 3$ of the time.

If you have not encountered this problem before, you might find that answer surpris-
ing. You would not be alone; many people have the strong intuition that it doesn't
matter if you stick or switch. There are two doors left, they reason, so the chance that
the car is behind Door A is 50%. But that is wrong.

To see why, it can help to use a Bayes table. We start with three hypotheses: the car
might be behind Door 1, 2, or 3. According to the statement of the problem, the prior
probability for each door is 1/3.

table3 = pd. DataFrame(index=[ 'Door 1', 'Door 2', 'Door 3'])
table3['prior'] = Fraction(1, 3)
table3

prior


<table>
<tr>
<td>Door 1</td>
<td>1/3</td>
</tr>
<tr>
<td>Door 2</td>
<td>1/3</td>
</tr>
<tr>
<td>Door 3</td>
<td>1/3</td>
</tr>
</table>


The data is that Monty opened Door 3 and revealed a goat. So let's consider the prob-
ability of the data under each hypothesis:

· If the car is behind Door 1, Monty chooses Door 2 or 3 at random, so the proba-
bility he opens Door 3 is $1 / 2 .$

. If the car is behind Door 2, Monty has to open Door 3, so the probability of the
data under this hypothesis is 1.

· If the car is behind Door 3, Monty does not open it, so the probability of the data
under this hypothesis is 0.

Here are the likelihoods:

table3['likelihood'] = Fraction(1, 2), 1, 0
table3

<!-- PageFooter="Chapter 2: Bayes's Theorem" -->
<!-- PageNumber="24" -->
<!-- PageBreak -->


<table>
<tr>
<th></th>
<th>prior</th>
<th>likelihood</th>
</tr>
<tr>
<td>Door 1</td>
<td>1/3</td>
<td>$1 / 2$</td>
</tr>
<tr>
<td>Door 2</td>
<td>1/3</td>
<td>1</td>
</tr>
<tr>
<td>Door 3</td>
<td>1/3</td>
<td>0</td>
</tr>
</table>


Now that we have priors and likelihoods, we can use update to compute the posterior
probabilities:

update(table3)
table3


<table>
<tr>
<th></th>
<th>prior</th>
<th>likelihood</th>
<th>unnorm</th>
<th>posterior</th>
</tr>
<tr>
<td>Door 1</td>
<td>1/3</td>
<td>$1 / 2$</td>
<td>1/6</td>
<td>$1 / 3$</td>
</tr>
<tr>
<td>Door 2</td>
<td>1/3</td>
<td>1</td>
<td>$1 / 3$</td>
<td>$2 / 3$</td>
</tr>
<tr>
<td>Door 3</td>
<td>1/3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>


After Monty opens Door 3, the posterior probability of Door 1 is $1 / 3 ;$ the posterior
probability of Door 2 is 2/3. So you are better off switching from Door 1 to Door 2.

As this example shows, our intuition for probability is not always reliable. Bayes's the-
orem can help by providing a divide-and-conquer strategy:

1\. First, write down the hypotheses and the data.

2\. Next, figure out the prior probabilities.

3\. Finally, compute the likelihood of the data under each hypothesis.

The Bayes table does the rest.


#### Summary

In this chapter we solved the Cookie Problem using Bayes's theorem explicitly and
using a Bayes table. There's no real difference between these methods, but the Bayes
table can make it easier to compute the total probability of the data, especially for
problems with more than two hypotheses.

Then we solved the Dice Problem, which we will see again in the next chapter, and
the Monty Hall Problem, which you might hope you never see again.

If the Monty Hall Problem makes your head hurt, you are not alone. But I think it
demonstrates the power of Bayes's theorem as a divide-and-conquer strategy for solv-
ing tricky problems. And I hope it provides some insight into why the answer is what
it is.

<!-- PageFooter="Summary" -->
<!-- PageNumber="25" -->
<!-- PageBreak -->

When Monty opens a door, he provides information we can use to update our belief
about the location of the car. Part of the information is obvious. If he opens Door 3,
we know the car is not behind Door 3. But part of the information is more subtle.
Opening Door 3 is more likely if the car is behind Door 2, and less likely if it is
behind Door 1. So the data is evidence in favor of Door 2. We will come back to this
notion of evidence in future chapters.

In the next chapter we'll extend the Cookie Problem and the Dice Problem, and take
the next step from basic probability to Bayesian statistics.

But first, you might want to work on the exercises.


### Exercises


#### Exercise 2-1.

Suppose you have two coins in a box. One is a normal coin with heads on one side
and tails on the other, and one is a trick coin with heads on both sides. You choose a
coin at random and see that one of the sides is heads. What is the probability that you
chose the trick coin?


#### Exercise 2-2.

Suppose you meet someone and learn that they have two children. You ask if either
child is a girl and they say yes. What is the probability that both children are girls?

Hint: Start with four equally likely hypotheses.


#### Exercise 2-3.

There are many variations of the Monty Hall Problem. For example, suppose Monty
always chooses Door 2 if he can, and only chooses Door 3 if he has to (because the car
is behind Door 2).

If you choose Door 1 and Monty opens Door 2, what is the probability the car is
behind Door 3?

If you choose Door 1 and Monty opens Door 3, what is the probability the car is
behind Door 2?


#### Exercise 2-4.

M&M's are small candy-coated chocolates that come in a variety of colors.
Mars, Inc., which makes M&M's, changes the mixture of colors from time to time. In
1995, they introduced blue M&M's.

<!-- PageFooter="Chapter 2: Bayes's Theorem" -->
<!-- PageNumber="26" -->
<!-- PageBreak -->

· In 1994, the color mix in a bag of plain M&M's was 30% Brown, 20% Yellow, 20%
Red, 10% Green, 10% Orange, 10% Tan.

· In 1996, it was 24% Blue, 20% Green, 16% Orange, 14% Yellow, 13% Red, 13%
Brown.

Suppose a friend of mine has two bags of M&M's, and he tells me that one is from
1994 and one from 1996. He won't tell me which is which, but he gives me one M&M
from each bag. One is yellow and one is green. What is the probability that the yellow
one came from the 1994 bag?

Hint: The trick to this question is to define the hypotheses and the data carefully.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="27" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 3" -->


## Distributions

In the previous chapter we used Bayes's theorem to solve a Cookie Problem; then we
solved it again using a Bayes table. In this chapter, at the risk of testing your patience,
we will solve it one more time using a Pmf object, which represents a "probability
mass function". I'll explain what that means, and why it is useful for Bayesian
statistics.

We'll use Pmf objects to solve some more challenging problems and take one more
step toward Bayesian statistics. But we'll start with distributions.


### Distributions

In statistics a distribution is a set of possible outcomes and their corresponding
probabilities. For example, if you toss a coin, there are two possible outcomes with
approximately equal probability. If you roll a 6-sided die, the set of possible outcomes
is the numbers 1 to 6, and the probability associated with each outcome is $1 / 6 .$

To represent distributions, we'll use a library called empiricaldist. An "empirical"
distribution is based on data, as opposed to a theoretical distribution. We'll use this
library throughout the book. I'll introduce the basic features in this chapter and we'll
see additional features later.


### Probability Mass Functions

If the outcomes in a distribution are discrete, we can describe the distribution with a
probability mass function, or PMF, which is a function that maps from each possible
outcome to its probability.

<!-- PageNumber="29" -->
<!-- PageBreak -->

empiricaldist provides a class called $\mathrm { P m f }$ that represents a probability mass func-
tion. To use Pmf you can import it like this:


#### from empiricaldist import Pmf

The following example makes a Pmf that represents the outcome of a coin toss.

coin = Pmf()

coin[ 'heads' ] = 1/2
$$\mathrm { c o i n } \left[ ^ { \prime } \tan ^ { \prime } \right] = 1 / 2$$

coin


##### probs


<table>
<tr>
<td>heads</td>
<td>0.5</td>
</tr>
<tr>
<td>tails</td>
<td>0.5</td>
</tr>
</table>


Pmf creates an empty Pmf with no outcomes. Then we can add new outcomes using
the bracket operator. In this example, the two outcomes are represented with strings,
and they have the same probability, 0.5.

You can also make a Pmf from a sequence of possible outcomes.

The following example uses Pmf . from_seq to make a Pmf that represents a 6-sided
die.

$$= P m f . f r o m _ { - } s e q \left( \left[ 1 , 2 , 3 , 4 , 5 , 6 \right] \right)$$
die


###### probs

1
0.166667

2
0.166667

3
0.166667

4
0.166667

5
0.166667

6

0.166667

In this example, all outcomes in the sequence appear once, so they all have the same
probability, $1 / 6 .$

More generally, outcomes can appear more than once, as in the following example:

letters = Pmf. from_seq(list('Mississippi'))
letters

<!-- PageFooter="Chapter 3: Distributions" -->
<!-- PageNumber="30" -->
<!-- PageBreak -->


###### probs


<table>
<tr>
<td>M</td>
<td>0.090909</td>
</tr>
<tr>
<td>i</td>
<td>0.363636</td>
</tr>
<tr>
<td>p</td>
<td>0.181818</td>
</tr>
<tr>
<td>s</td>
<td>0.363636</td>
</tr>
</table>


The letter M appears once out of 11 characters, so its probability is $1 / 1 1 .$ The letter $i$
appears 4 times, so its probability is $4 / 1 1 .$

Since the letters in a string are not outcomes of a random process, I'll use the more
general term "quantities" for the letters in the $\mathrm { P m f } .$

The Pmf class inherits from a pandas Series, so anything you can do with a Series,
you can also do with a Pmf.

For example, you can use the bracket operator to look up a quantity and get the cor-
responding probability:

letters['s']

0.36363636363636365

In the word "Mississippi", about 36% of the letters are "s".

However, if you ask for the probability of a quantity that's not in the distribution, you
get a KeyError.

You can also call a Pmf as $\mathrm { i f }$ it were a function, with a letter in parentheses:

$$\mathrm { l e t t e r s } \left( ^ { \prime } s ^ { \prime } \right)$$

0.36363636363636365

If the quantity is in the distribution, the results are the same. But if it is not in the
distribution, the result is 0, not an error:

letters('t')
0

With parentheses, you can also provide a sequence of quantities and get a sequence of
probabilities:

$$\mathrm { d i e } \left( \left[ 1 , 4 , 7 \right] \right)$$

array([0.16666667, 0.16666667, 0.
1)

The quantities in a Pmf can be strings, numbers, or any other type that can be stored
in the index of a pandas Series. If you are familiar with pandas, that will help you
work with Pmf objects. But I will explain what you need to know as we go along.

<!-- PageFooter="Probability Mass Functions" -->
<!-- PageNumber="31" -->
<!-- PageBreak -->


## The Cookie Problem Revisited

In this section I'll use a Pmf to solve the Cookie Problem from "The Cookie Problem"
on page 17. Here's the statement of the problem again:

Suppose there are two bowls of cookies.

· Bowl 1 contains 30 vanilla cookies and 10 chocolate cookies.

· Bowl 2 contains 20 vanilla cookies and 20 chocolate cookies.

Now suppose you choose one of the bowls at random and, without looking, choose a
cookie at random. If the cookie is vanilla, what is the probability that it came from
Bowl 1?

Here's a Pmf that represents the two hypotheses and their prior probabilities:

prior = Pmf. from_seq(['Bowl 1', 'Bowl 2'])
prior


### probs


<table>
<tr>
<td>Bowl 1</td>
<td>0.5</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.5</td>
</tr>
</table>


This distribution, which contains the prior probability for each hypothesis, is called-
wait for it-the prior distribution.

To update the distribution based on new data (the vanilla cookie), we multiply the
priors by the likelihoods. The likelihood of drawing a vanilla cookie from Bowl 1 is
$3 / 4$ and the likelihood for Bowl 2 is $1 / 2 .$

likelihood_vanilla = [0.75, 0.5]
posterior = prior * likelihood_vanilla
posterior


<table>
<tr>
<th></th>
<th>probs</th>
</tr>
<tr>
<td>Bowl 1</td>
<td>0.375</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.250</td>
</tr>
</table>


The result is the unnormalized posteriors; that is, they don't add up to 1. To make
them add up to 1, we can use normalize, which is a method provided by Pmf:

posterior.normalize()

0.625

The return value from normalize is the total probability of the data, which is $5 / 8 .$

<!-- PageFooter="Chapter 3: Distributions" -->
<!-- PageNumber="32" -->
<!-- PageBreak -->

posterior, which contains the posterior probability for each hypothesis, is called-
wait now-the posterior distribution.


#### posterior

probs

Bowl 1 0.6

Bowl 2
0.4

From the posterior distribution we can select the posterior probability for Bowl 1:

posterior( 'Bowl 1')
0.6

And the answer is 0.6.

One benefit of using Pmf objects is that it is easy to do successive updates with more
data. For example, suppose you put the first cookie back (so the contents of the bowls
don't change) and draw again from the same bowl. If the second cookie is also vanilla,
we can do a second update like this:

posterior *= likelihood_vanilla
posterior.normalize()
posterior

probs


<table>
<tr>
<td>Bowl 1</td>
<td>0.692308</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.307692</td>
</tr>
</table>


Now the posterior probability for Bowl 1 is almost 70%. But suppose we do the same
thing again and get a chocolate cookie.

Here are the likelihoods for the new data:

likelihood_chocolate = [0.25, 0.5]

And here's the update:

posterior *= likelihood_chocolate
posterior.normalize()
posterior


#### probs


<table>
<tr>
<td>Bowl 1</td>
<td>0.529412</td>
</tr>
<tr>
<td>Bowl 2</td>
<td>0.470588</td>
</tr>
</table>


<!-- PageFooter="The Cookie Problem Revisited" -->
<!-- PageNumber="33" -->
<!-- PageBreak -->

Now the posterior probability for Bowl 1 is about 53%. After two vanilla cookies and
one chocolate, the posterior probabilities are close to 50/50.


### 101 Bowls

Next let's solve a Cookie Problem with 101 bowls:

· Bowl 0 contains 0% vanilla cookies,

· Bowl 1 contains 1% vanilla cookies,

· Bowl 2 contains 2% vanilla cookies,

and so on, up to

· Bowl 99 contains 99% vanilla cookies, and

· Bowl 100 contains all vanilla cookies.

As in the previous version, there are only two kinds of cookies, vanilla and chocolate.
So Bowl 0 is all chocolate cookies, Bowl 1 is 99% chocolate, and so on.

Suppose we choose a bowl at random, choose a cookie at random, and it turns out to
be vanilla. What is the probability that the cookie came from Bowl x, for each value of
$x ?$

To solve this problem, I'll use np. arange to make an array that represents 101
hypotheses, numbered from 0 to 100:

import numpy as np

hypos = np. arange (101)

We can use this array to make the prior distribution:

prior = Pmf(1, hypos)
prior.normalize()
101

As this example shows, we can initialize a Pmf with two parameters. The first parame-
ter is the prior probability; the second parameter is a sequence of quantities.

In this example, the probabilities are all the same, so we only have to provide one of
them; it gets "broadcast" across the hypotheses. Since all hypotheses have the same
prior probability, this distribution is uniform.

Here are the first few hypotheses and their probabilities:

prior.head()

<!-- PageFooter="Chapter 3: Distributions" -->
<!-- PageNumber="34" -->
<!-- PageBreak -->


#### probs

0
0.009901

1
0.009901

2

0.009901

The likelihood of the data is the fraction of vanilla cookies in each bowl, which we
can calculate using hypos:

likelihood_vanilla = hypos/100
likelihood_vanilla[ : 5]
array([0. , 0.01, 0.02, 0.03, 0.04])

Now we can compute the posterior distribution in the usual way:

posterior1 = prior * likelihood_vanilla
posterior1.normalize()
posterior1. head()


#### probs

0
0.000000

1
0.000198

2
0.000396

The following figure shows the prior distribution and the posterior distribution after
one vanilla cookie:


<figure>

Posterior after one vanilla cookie

0.0200

prior

0.0175

posterior

0.0150

0.0125

$\sum _ { n = 1 } ^ { 4 } 0 . 0 1 0 0$

0.0075

0.0050

0.0025

0.0000

0

20

40

60

80

100

Bowl $\#$

</figure>


<!-- PageFooter="101 Bowls" -->
<!-- PageNumber="35" -->
<!-- PageBreak -->

The posterior probability of Bowl 0 is 0 because it contains no vanilla cookies. The
posterior probability of Bowl 100 is the highest because it contains the most vanilla
cookies. In between, the shape of the posterior distribution is a line because the likeli-
hoods are proportional to the bowl numbers.

Now suppose we put the cookie back, draw again from the same bowl, and get
another vanilla cookie. Here's the update after the second cookie:

posterior2 = posterior1 * likelihood_vanilla
posterior2.normalize()

And here's what the posterior distribution looks like:


<figure>

Posterior after two vanilla cookies

0.030

posterior

0.025

0.020

PMF

0.015

0.010

0.005

0.000

0

20

40

60

80

100

Bowl $\#$

</figure>


After two vanilla cookies, the high-numbered bowls have the highest posterior proba-
bilities because they contain the most vanilla cookies; the low-numbered bowls have
the lowest probabilities.

But suppose we draw again and get a chocolate cookie. Here's the update:

likelihood_chocolate = 1 - hypos/100

posterior3 = posterior2 * likelihood_chocolate
posterior3.normalize()

<!-- PageFooter="Chapter 3: Distributions" -->
<!-- PageNumber="36" -->
<!-- PageBreak -->

And here's the posterior distribution:


<figure>

Posterior after 2 vanilla, 1 chocolate

0.0175

posterior

0.0150

0.0125

$0 . 0 0 7 5$

0.0050

0.0025

0.0000

0

20

40

60

80

100

Bowl $\#$

</figure>


Now Bowl 100 has been eliminated because it contains no chocolate cookies. But the
high-numbered bowls are still more likely than the low-numbered bowls, because we
have seen more vanilla cookies than chocolate.

In fact, the peak of the posterior distribution is at Bowl 67, which corresponds to the
fraction of vanilla cookies in the data we've observed, 2/3.

The quantity with the highest posterior probability is called the MAP, which stands
for "maximum a posteori probability", where "a posteori" is unnecessary Latin for
"posterior".

To compute the MAP, we can use the Series method idxmax:

posterior3. idxmax()
67

Or Pmf provides a more memorable name for the same thing:

posterior3.max_prob()
67

As you might suspect, this example isn't really about bowls; it's about estimating pro-
portions. Imagine that you have one bowl of cookies. You don't know what fraction of
cookies are vanilla, but you think it is equally likely to be any fraction from 0 to 1. If
you draw three cookies and two are vanilla, what proportion of cookies in the bowl
do you think are vanilla? The posterior distribution we just computed is the answer
to that question.

We'll come back to estimating proportions in the next chapter. But first let's use a Pmf
to solve the Dice Problem.

<!-- PageFooter="101 Bowls" -->
<!-- PageNumber="37" -->
<!-- PageBreak -->


## The Dice Problem

In the previous chapter we solved the Dice Problem using a Bayes table. Here's the
statement of the problem:

Suppose I have a box with a 6-sided die, an 8-sided die, and a 12-sided die.

I choose one of the dice at random, roll it, and report that the outcome is a 1.

What is the probability that I chose the 6-sided die?

Let's solve it using a Pmf. I'll use integers to represent the hypotheses:

hypos = [6, 8, 12]

We can make the prior distribution like this:

$$p r i o r = P m f \left( 1 / 3 , h y p o s \right)$$
prior

probs

6

0.333333

8
0.333333

12
0.333333

As in the previous example, the prior probability gets broadcast across the hypothe-
ses. The Pmf object has two attributes:

· qs contains the quantities in the distribution;

· ps contains the corresponding probabilities.

prior.qs
array([ 6, 8, 12])

prior.ps
array([0.33333333, 0.33333333, 0.33333333])

Now we're ready to do the update. Here's the likelihood of the data for each
hypothesis:

likelihood1 = 1/6, 1/8, 1/12

And here's the update:

posterior = prior * likelihood1
posterior.normalize()
posterior

<!-- PageFooter="Chapter 3: Distributions" -->
<!-- PageNumber="38" -->
<!-- PageBreak -->


<table>
<tr>
<th></th>
<th>probs</th>
</tr>
<tr>
<td>6</td>
<td>0.444444</td>
</tr>
<tr>
<td>8</td>
<td>0.333333</td>
</tr>
<tr>
<td>12</td>
<td>0.222222</td>
</tr>
</table>


The posterior probability for the 6-sided die is $4 / 9 .$

Now suppose I roll the same die again and get a 7. Here are the likelihoods:

likelihood2 = 0, $1 / 8 ,$ 1/12

The likelihood for the 6-sided die is 0 because it is not possible to get a 7 on a 6-sided
die. The other two likelihoods are the same as in the previous update.

Here's the update:

posterior *= likelihood2
posterior.normalize()
posterior

probs

6

0.000000

8
0.692308

12
0.307692

After rolling a 1 and a 7, the posterior probability of the 8-sided die is about 69%.


### Updating Dice

The following function is a more general version of the update in the previous
section:

def update_dice(pmf, data):
"""Update pmf based on new data. ""'
hypos = pmf.qs
likelihood = 1 / hypos
impossible = (data > hypos)
likelihood[impossible] = 0
pmf *= likelihood
pmf.normalize()

The first parameter is a Pmf that represents the possible dice and their probabilities.
The second parameter is the outcome of rolling a die.

The first line selects quantities from the Pmf that represent the hypotheses. Since the
hypotheses are integers, we can use them to compute the likelihoods. In general, $\mathrm { i f }$
there are n sides on the die, the probability of any possible outcome is $1 / n .$

<!-- PageFooter="Updating Dice" -->
<!-- PageNumber="39" -->
<!-- PageBreak -->

However, we have to check for impossible outcomes! If the outcome exceeds the
hypothetical number of sides on the die, the probability of that outcome is 0.

impossible is a Boolean Series that is True for each impossible outcome. I use it as
an index into likelihood to set the corresponding probabilities to 0.

Finally, I multiply pmf by the likelihoods and normalize.

Here's how we can use this function to compute the updates in the previous section. I
start with a fresh copy of the prior distribution:

$$p \eta f = p r i o r . c o p y \left( \right)$$

pmf

probs

6

0.333333

8

0.333333

12

0.333333

And use update_dice to do the updates:

update_dice(pmf, 1)
update_dice(pmf, 7)
pmf

probs

6

0.000000

8
0.692308

12

0.307692

The result is the same. We will see a version of this function in the next chapter.


#### Summary

This chapter introduces the empiricaldist module, which provides Pmf, which we
use to represent a set of hypotheses and their probabilities.

empiricaldist is based on pandas; the Pmf class inherits from the pandas $\mathrm { S e r i e s }$
class and provides additional features specific to probability mass functions. We'll use
Pmf and other classes from empiricaldist throughout the book because they sim-
plify the code and make it more readable. But we could do the same things directly
with pandas.

<!-- PageFooter="Chapter 3: Distributions" -->
<!-- PageNumber="40" -->
<!-- PageBreak -->

We use a Pmf to solve the Cookie Problem and the Dice Problem, which we saw in the
previous chapter. With a Pmf it is easy to perform sequential updates with multiple
pieces of data.

We also solved a more general version of the Cookie Problem, with 101 bowls rather
than two. Then we computed the MAP, which is the quantity with the highest poste-
rior probability.

In the next chapter, I'll introduce the Euro Problem, and we will use the binomial dis-
tribution. And, at last, we will make the leap from using Bayes's theorem to doing
Bayesian statistics.

But first you might want to work on the exercises.


## Exercises


### Exercise 3-1.

Suppose I have a box with a 6-sided die, an 8-sided die, and a 12-sided die. I choose
one of the dice at random, roll it four times, and get 1, 3, 5, and 7. What is the proba-
bility that I chose the 8-sided die?

You can use the update_dice function or do the update yourself.


### Exercise 3-2.

In the previous version of the Dice Problem, the prior probabilities are the same
because the box contains one of each die. But suppose the box contains 1 die that is 4-
sided, 2 dice that are 6-sided, 3 dice that are 8-sided, 4 dice that are 12-sided, and 5
dice that are 20-sided. I choose a die, roll it, and get a 7. What is the probability that I
chose an 8-sided die?

Hint: To make the prior distribution, call Pmf with two parameters.


### Exercise 3-3.

Suppose I have two sock drawers. One contains equal numbers of black and white
socks. The other contains equal numbers of red, green, and blue socks. Suppose I
choose a drawer at random, choose two socks at random, and I tell you that I got a
matching pair. What is the probability that the socks are white?

For simplicity, let's assume that there are so many socks in both drawers that remov-
ing one sock makes a negligible change to the proportions.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="41" -->
<!-- PageBreak -->


### Exercise 3-4.


#### Here's a problem from Bayesian Data Analysis:

Elvis Presley had a twin brother (who died at birth). What is the probability that Elvis
was an identical twin?

Hint: In 1935, about $2 / 3$ of twins were fraternal and $1 / 3$ were identical.

<!-- PageFooter="Chapter 3: Distributions" -->
<!-- PageNumber="42" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 4" -->


# Estimating Proportions

In the previous chapter we solved the 101 Bowls Problem, and I admitted that it is
not really about guessing which bowl the cookies came from; it is about estimating
proportions.

In this chapter, we take another step toward Bayesian statistics by solving the Euro
Problem. We'll start with the same prior distribution, and we'll see that the update is
the same, mathematically. But I will argue that it is a different problem, philosophi-
cally, and use it to introduce two defining elements of Bayesian statistics: choosing
prior distributions, and using probability to represent the unknown.


# The Euro Problem

In Information Theory, Inference, and Learning Algorithms, David Mackay poses this
problem:

A statistical statement appeared in The Guardian on Friday January 4, 2002:

When spun on edge 250 times, a Belgian one-euro coin came up heads 140 times and tails
110. "It looks very suspicious to $m e ,$ said Barry Blight, a statistics lecturer at the London
School of Economics. "If the coin were unbiased, the chance of getting a result as extreme
as that would be less than 7%."

But do these data give evidence that the coin is biased rather than fair?

To answer that question, we'll proceed in two steps. First we'll use the binomial distri-
bution to see where that 7% came from; then we'll use Bayes's theorem to estimate the
probability that this coin comes up heads.

<!-- PageNumber="43" -->
<!-- PageBreak -->


# The Binomial Distribution

Suppose I tell you that a coin is "fair", that is, the probability of heads is 50%. If you
spin it twice, there are four outcomes: HH, $\mathrm { H T } ,$ $T H ,$ and $\mathrm { T T } .$ All four outcomes have the
same probability, 25%.

If we add up the total number of heads, there are three possible results: 0, 1, or 2. The
probabilities of 0 and 2 are 25%, and the probability of 1 is 50%.

More generally, suppose the probability of heads is $p$ and we spin the coin $n$ times.
The probability that we get a total of $k$ heads is given by the binomial distribution:

$$\binom { n } { k } p ^ { k } \left( 1 - p \right) ^ { n - k }$$

for any value of $k$ from 0 to $n$ n, including both. The term $\binom { n } { k }$ is the binomial coeffi-
cient, usually pronounced "n choose $\mathrm { k } .$

We could evaluate this expression ourselves, but we can also use the SciPy function
binom.pmf. For example, if we flip a coin $n = 2$ times and the probability of heads is
$p = 0 . 5 ,$ here's the probability of getting $k = 1$ heads:

from scipy. stats import binom

$n = 2$
$P = 0 . 5$
$k = 1$
binom.pmf(k, n, p)
0.5

Instead of providing a single value for $k ,$ we can also call binom. pmf with an array of
values:

import numpy as np

$$k s = n p . a r a n g e \left( n + 1 \right)$$

$p s = b i n o m . p m f \left( k s , n , p \right)$
ps
$\mathrm { a r r a y } \left( \left[ 0 . 2 5 , 0 . 5 , 0 . 2 5 \right] \right)$

The result is a NumPy array with the probability of 0, 1, or 2 heads. If we put these
probabilities in a Pmf, the result is the distribution of $\mathrm { k }$ for the given values of $n$ and $\mathrm { p } .$

<!-- PageFooter="Chapter 4: Estimating Proportions" -->
<!-- PageNumber="44" -->
<!-- PageBreak -->

Here's what it looks like:

from empiricaldist import Pmf
$p m f \_ k = P m f \left( p s , k s \right)$
pmf_k


## probs

0

0.25

1 0.50

2

0.25

The following function computes the binomial distribution for given values of n and
p and returns a Pmf that represents the result:

def $m a k e \_ b i n o m i a l \left( n , p \right) :$
"""Make a binomial Pmf. """

$$k s = n p . a r a n g e \left( n + 1 \right)$$
ps = binom.pmf(ks,

return Pmf(ps, ks)

Here's what it looks like with $n = 2 5 0$ and $p = 0 . 5 :$

pmf_k = make_binomial(n=250, $\left. p = 0 . 5 \right)$

Binomial distribution


<figure>

0.05

$n = 2 5 0 ,$ $p = 0 . 5$

0.04

0.03

PMF

0.02

0.01

0.00

0

50

100

150

200

250

Number of heads (k)

</figure>


The most likely quantity in this distribution is 125:
pmf_k.max_prob()
125

<!-- PageFooter="The Binomial Distribution" -->
<!-- PageNumber="45" -->
<!-- PageBreak -->

But even though it is the most likely quantity, the probability that we get exactly 125
heads is only about 5%:

$$p m f \_ k \left[ 1 2 5 \right]$$

0.05041221314731537

In MacKay's example, we got 140 heads, which is even less likely than 125:

pmf_k[140]
0.008357181724917673

In the article Mackay quotes, the statistician says, "If the coin were unbiased the
chance of getting a result as extreme as that would be less than 7%."

We can use the binomial distribution to check his math. The following function takes
a PMF and computes the total probability of quantities greater than or equal to
threshold:

def prob_ge(pmf, threshold):
"""Probability of quantities greater than threshold. """
ge = (pmf.qs >= threshold)
total = pmf[ge].sum()
return total

Here's the probability of getting 140 heads or more:

prob_ge(pmf_k, 140)
0.033210575620022706

Pmf provides a method that does the same computation:

pmf_k.prob_ge(140)
0.033210575620022706

The result is about 3.3%, which is less than the quoted 7%. The reason for the differ-
ence is that the statistician includes all outcomes "as extreme as" 140, which includes
outcomes less than or equal to 110.

To see where that comes from, recall that the expected number of heads is 125. $I f \quad w e$
get 140, we've exceeded that expectation by 15. And if we get 110, we have come up
short by 15.

<!-- PageFooter="Chapter 4: Estimating Proportions" -->
<!-- PageNumber="46" -->
<!-- PageBreak -->

7% is the sum of both of these "tails", as shown in the following figure:


<figure>

Binomial distribution

0.05

$n = 2 5 0 ,$ $p = 0 . 5$

0.04

0.03

PMF

0.02

0.01

0.00

0

50

100

150

200

250

Number of heads (k)

</figure>


Here's how we compute the total probability of the left tail:

pmf_k.prob_le(110)
0.033210575620022706

The probability of outcomes less than or equal to 110 is also 3.3%, so the total proba-
bility of outcomes "as extreme" as 140 is 6.6%.

The point of this calculation is that these extreme outcomes are unlikely if the coin is
fair.

That's interesting, but it doesn't answer Mackay's question. Let's see if we can.


# Bayesian Estimation

Any given coin has some probability of landing heads up when spun on edge; I'll call
this probability x. It seems reasonable to believe that $x$ depends on physical character-
istics of the coin, like the distribution of weight. If a coin is perfectly balanced, we
expect $x$ to be close to 50%, but for a lopsided coin, $x$ might be substantially different.
We can use Bayes's theorem and the observed data to estimate $x$ x.

For simplicity, I'll start with a uniform prior, which assumes that all values $o f \quad x \quad a r e$
equally likely. That might not be a reasonable assumption, so we'll come back and
consider other priors later.

<!-- PageFooter="Bayesian Estimation" -->
<!-- PageNumber="47" -->
<!-- PageBreak -->

We can make a uniform prior like this:

hypos = np. linspace(0, 1, 101)
prior = Pmf(1, hypos)

hypos is an array of equally spaced values between 0 and 1.

We can use the hypotheses to compute the likelihoods, like this:

likelihood_heads = hypos
likelihood_tails = 1 - hypos

I'll put the likelihoods for heads and tails in a dictionary to make it easier to do the
update:

likelihood = {
'H': likelihood_heads,
'T': likelihood_tails
}

To represent the data, I'll construct a string with $\mathrm { H }$ repeated 140 times and T repeated
110 times:

dataset = 'H' * 140 + 'T' * 110

The following function does the update:

def update_euro(pmf, dataset):
"""Update pmf with a given sequence of $H$ and T. """
for data in dataset:
pmf *= likelihood[data]

pmf.normalize()

The first argument is a Pmf that represents the prior. The second argument is a
sequence of strings. Each time through the loop, we multiply pmf by the likelihood of
one outcome, $H$ for heads or T for tails.

Notice that normalize is outside the loop, so the posterior distribution only gets nor-
malized once, at the end. That's more efficient than normalizing it after each
spin (although we'll see later that it can also cause problems with floating-point
arithmetic).

Here's how we use update_euro:

posterior = prior. copy()
update_euro(posterior, dataset)

<!-- PageFooter="Chapter 4: Estimating Proportions" -->
<!-- PageNumber="48" -->
<!-- PageBreak -->

And here's what the posterior looks like:


<figure>

Posterior distribution of $x$

0.12

140 heads out of 250

0.10

Probability

0.08

0.06

0.04

0.02

0.00

0.0

0.2

0.8

1.0

$P r o p o r t i o n \quad o f \quad h e a d s \left( x \right)$
☒

</figure>


This figure shows the posterior distribution of x, which is the proportion of heads for
the coin we observed.

The posterior distribution represents our beliefs $a b o u t \quad x$ after seeing the data. It indi-
cates that values less than 0.4 and greater than 0.7 are unlikely; values between 0.5
and 0.6 are the most likely.

In fact, the most likely value for $x$ is 0.56, which is the proportion of heads in the
dataset, $1 4 0 / 2 5 0 .$

posterior.max_prob()
0.56


## Triangle Prior

So far we've been using a uniform prior:

uniform = Pmf(1, hypos, name='uniform')
uniform.normalize()

But that might not be a reasonable choice based on what we know about coins. I can
believe that if a coin is lopsided, $x$ might deviate substantially from 0.5, but it seems
unlikely that the Belgian Euro coin is so imbalanced that $x$ is 0.1 or 0.9.

It might be more reasonable to choose a prior that gives higher probability to values
of $x$ near 0.5 and lower probability to extreme values.

<!-- PageFooter="Triangle Prior" -->
<!-- PageNumber="49" -->
<!-- PageBreak -->

As an example, let's try a triangle-shaped prior. Here's the code that constructs it:

$$r a m p _ { - } u p = n p . a r a n g e \left( 5 \theta \right)$$

ramp_down = np. arange(50, -1, -1)
$a = n p .$ append (ramp_up, ramp_down)
triangle = Pmf(a, hypos, name='triangle')
triangle.normalize()
2500

arange returns a NumPy array, so we can use np. append to append ramp_down to the
end of ramp_up. Then we use a and hypos to make a Pmf.

The following figure shows the result, along with the uniform prior:


<figure>

Uniform and triangle prior distributions

0.0200

0.0175

0.0150

Probability

0.0125

0.0100

0.0075

0.0050

0.0025

0.0000

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of heads (x)
☒

</figure>


Now we can update both priors with the same data:

update_euro(uniform, dataset)
update_euro(triangle, dataset)

<!-- PageFooter="Chapter 4: Estimating Proportions" -->
<!-- PageNumber="50" -->
<!-- PageBreak -->

Here are the posteriors:


<figure>

Posterior distributions

0.12

0.10

Probability

0.08

0.06

0.04

0.02

0.00

0.0

0.2

0.8

1.0

$P r o p o r t i o n \quad o f \quad h e a d s \left( x \right)$
☒

</figure>


The differences between the posterior distributions are barely visible, and so small
they would hardly matter in practice.

And that's good news. To see why, imagine two people who disagree angrily about
which prior is better, uniform or triangle. Each of them has reasons for their prefer-
ence, but neither of them can persuade the other to change their mind.

But suppose they agree to use the data to update their beliefs. When they compare
their posterior distributions, they find that there is almost nothing left to argue about.

This is an example of swamping the priors: with enough data, people who start with
different priors will tend to converge on the same posterior distribution.


# The Binomial Likelihood Function

So far we've been computing the updates one spin at a time, so for the Euro Problem
we have to do 250 updates.

A more efficient alternative is to compute the likelihood of the entire dataset at once.
For each hypothetical value of $x$ x, we have to compute the probability of getting 140
heads out of 250 spins.

Well, we know how to do that; this is the question the binomial distribution answers.
If the probability of heads is $p ,$ the probability of $k$ heads in n spins is:

$$\binom { n } { k } p ^ { k } \left( 1 - p \right) ^ { n - k }$$

<!-- PageFooter="The Binomial Likelihood Function" -->
<!-- PageNumber="51" -->
<!-- PageBreak -->

And we can use SciPy to compute it. The following function takes a Pmf that repre-
sents a prior distribution and a tuple of integers that represent the data:

from scipy. stats import binom

def update_binomial(pmf, data):
"""Update pmf using the binomial distribution. """
k, $n = d a t a$
xs = pmf. qs
likelihood = binom.pmf(k, n, xs)
pmf *= likelihood
pmf.normalize()

The data are represented with a tuple of values for $\mathrm { k }$ and n, rather than a long string
of outcomes. Here's the update:

uniform2 = Pmf(1, hypos, name='uniform2')
data = 140, 250
update_binomial(uniform2, data)

We can use allclose to confirm that the result is the same as in the previous section
except for a small floating-point round-off.

np.allclose(uniform, uniform2)

True

But this way of doing the computation is much more efficient.


## Bayesian Statistics

You might have noticed similarities between the Euro Problem and the 101 Bowls
Problem in "101 Bowls" on page 34. The prior distributions are the same, the likeli-
hoods are the same, and with the same data, the results would be the same. But there
are two differences.

The first is the choice of the prior. With 101 bowls, the uniform prior is implied by
the statement of the problem, which says that we choose one of the bowls at random
with equal probability.

In the Euro Problem, the choice of the prior is subjective; that is, reasonable people
could disagree, maybe because they have different information about coins or because
they interpret the same information differently.

Because the priors are subjective, the posteriors are subjective, too. And some people
find that problematic.

The other difference is the nature of what we are estimating. In the 101 Bowls Prob-
lem, we choose the bowl randomly, so it is uncontroversial to compute the probability
of choosing each bowl. In the Euro Problem, the proportion of heads is a physical

<!-- PageFooter="Chapter 4: Estimating Proportions" -->
<!-- PageNumber="52" -->
<!-- PageBreak -->

property of a given coin. Under some interpretations of probability, that's a problem
because physical properties are not considered random.

As an example, consider the age of the universe. Currently, our best estimate is 13.80
billion years, but it might be off by 0.02 billion years in either direction.

Now suppose we would like to know the probability that the age of the universe is
actually greater than 13.81 billion years. Under some interpretations of probability,
we would not be able to answer that question. We would be required to say some-
thing like, "The age of the universe is not a random quantity, so it has no probability
of exceeding a particular value."

Under the Bayesian interpretation of probability, it is meaningful and useful to treat
physical quantities as if they were random and compute probabilities about them.

In the Euro Problem, the prior distribution represents what we believe about coins in
general and the posterior distribution represents what we believe about a particular
coin after seeing the data. So we can use the posterior distribution to compute proba-
bilities about the coin and its proportion of heads.

The subjectivity of the prior and the interpretation of the posterior are key differences
between using Bayes's theorem and doing Bayesian statistics.

Bayes's theorem is a mathematical law of probability; no reasonable person objects to
it. But Bayesian statistics is surprisingly controversial. Historically, many people have
been bothered by its subjectivity and its use of probability for things that are not
random.

If you are interested in this history, I recommend Sharon Bertsch McGrayne's book,
The Theory That Would Not Die.


## Summary

In this chapter I posed David Mackay's Euro Problem and we started to solve it.
Given the data, we computed the posterior distribution for x, the probability a Euro
coin comes up heads.

We tried two different priors, updated them with the same data, and found that the
posteriors were nearly the same. This is good news, because it suggests that if two
people start with different beliefs and see the same data, their beliefs tend to converge.

This chapter introduces the binomial distribution, which we used to compute the
posterior distribution more efficiently. And I discussed the differences between
applying Bayes's theorem, as in the 101 Bowls Problem, and doing Bayesian statistics,
as in the Euro Problem.

<!-- PageFooter="Summary" -->
<!-- PageNumber="53" -->
<!-- PageBreak -->

However, we still haven't answered Mackay's question: "Do these data give evidence
that the coin is biased rather than fair?" I'm going to leave this question hanging a
little longer; we'll come back to it in Chapter 10.

In the next chapter, we'll solve problems related to counting, including trains, tanks,
and rabbits.

But first you might want to work on these exercises.


# Exercises


## Exercise 4-1.

In Major League Baseball (MLB), most players have a batting average between .200
and .330, which means that their probability of getting a hit is between 0.2 and 0.33.

Suppose a player appearing in their first game gets 3 hits out of 3 attempts. What is
the posterior distribution for their probability of getting a hit?


## Exercise 4-2.

Whenever you survey people about sensitive issues, you have to deal with social
desirability bias, which is the tendency of people to adjust their answers to show
themselves in the most positive light. One way to improve the accuracy of the results
is randomized response.

As an example, suppose you want to know how many people cheat on their taxes. If
you ask them directly, it is likely that some of the cheaters will lie. You can get a more
accurate estimate if you ask them indirectly, like this: Ask each person to flip a coin
and, without revealing the outcome,

· If they get heads, they report YES.

· If they get tails, they honestly answer the question, "Do you cheat on your taxes?"

If someone says YES, we don't know whether they actually cheat on their taxes; they
might have flipped heads. Knowing this, people might be more willing to answer
honestly.

Suppose you survey 100 people this way and get 80 YESes and 20 NOs. Based on this
data, what is the posterior distribution for the fraction of people who cheat on their
taxes? What is the most likely quantity in the posterior distribution?

<!-- PageFooter="Chapter 4: Estimating Proportions" -->
<!-- PageNumber="54" -->
<!-- PageBreak -->


## Exercise 4-3.

Suppose you want to test whether a coin is fair, but you don't want to spin it hundreds
of times. So you make a machine that spins the coin automatically and uses computer
vision to determine the outcome.

However, you discover that the machine is not always accurate. Specifically, suppose
the probability is $y = 0 . 2$ that an actual heads is reported as tails, or actual tails
reported as heads.

If we spin a coin 250 times and the machine reports 140 heads, what is the posterior
distribution of $x ?$ What happens as you vary the value of y?


### Exercise 4-4.

In preparation for an alien invasion, the Earth Defense League (EDL) has been work-
ing on new missiles to shoot down space invaders. Of course, some missile designs
are better than others; let's assume that each design has some probability of hitting an
alien ship, x.

Based on previous tests, the distribution of $\mathrm { X }$ in the population of designs is approxi-
mately uniform between 0.1 and 0.4.

Now suppose the new ultra-secret Alien Blaster 9000 is being tested. In a press con-
ference, an EDL general reports that the new design has been tested twice, taking two
shots during each test. The results of the test are confidential, so the general won't say
how many targets were hit, but they report: "The same number of targets were hit in
the two tests, so we have reason to think this new design is consistent."

Is this data good or bad? That is, does it increase or decrease your estimate of $x$ for
the Alien Blaster 9000?

<!-- PageFooter="Exercises" -->
<!-- PageNumber="55" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 5" -->


# Estimating Counts

In the previous chapter we solved problems that involve estimating proportions. In
the Euro Problem, we estimated the probability that a coin lands heads up, and in the
exercises, you estimated a batting average, the fraction of people who cheat on their
taxes, and the chance of shooting down an invading alien.

Clearly, some of these problems are more realistic than others, and some are more
useful than others.

In this chapter, we'll work on problems related to counting, or estimating the size of a
population. Again, some of the examples will seem silly, but some of them, like the
German Tank Problem, have real applications, sometimes in life and death situations.


# The Train Problem


## I found the Train Problem in Frederick Mosteller's Fifty Challenging Problems in Probability with Solutions:

A railroad numbers its locomotives in order 1 .. N. One day you see a locomotive with
the number 60. Estimate how many locomotives the railroad has.

Based on this observation, we know the railroad has 60 or more locomotives. But
how many more? To apply Bayesian reasoning, we can break this problem into two
steps:

· What did we know about $N$ before we saw the data?

· For any given value of $N ,$ what is the likelihood of seeing the data (a locomotive
with number 60)?

<!-- PageNumber="57" -->
<!-- PageBreak -->

The answer to the first question is the prior. The answer to the second is the
likelihood.

We don't have much basis to choose a prior, so we'll start with something simple and
then consider alternatives. Let's assume that $N$ is equally likely to be any value from 1
to 1000.

Here's the prior distribution:

import numpy as np
from empiricaldist import Pmf

hypos = np. arange(1, 1001)
prior = Pmf(1, hypos)

Now let's figure out the likelihood of the data. In a hypothetical fleet of $N$ locomo-
tives, what is the probability that we would see number 60? If we assume that we are
equally likely to see any locomotive, the chance of seeing any particular one is $1 / N .$

Here's the function that does the update:

def update_train(pmf, data):
"""Update pmf based on new data.
hypos = pmf.qs
likelihood = 1 / hypos
impossible = (data > hypos)
likelihood[impossible] = 0
pmf *= likelihood
pmf.normalize()

This function might look familiar; it is the same as the update function for the Dice
Problem in the previous chapter. In terms of likelihood, the Train Problem is the
same as the Dice Problem.

Here's the update:

data = 60
posterior = prior . copy()
update_train(posterior, data)

<!-- PageFooter="Chapter 5: Estimating Counts" -->
<!-- PageNumber="58" -->
<!-- PageBreak -->

Here's what the posterior looks like:


<figure>

Posterior distribution

0.006

Posterior after train 60

0.005

0.004

$\sum _ { n = 1 } ^ { 4 }$

0.003

0.002

0.001

0.000

0

200

400

600

800

1000

Number of trains

</figure>


Not surprisingly, all values of $N$ below 60 have been eliminated.

The most likely value, if you had to guess, is 60.

posterior.max_prob()
60

That might not seem like a very good guess; after all, what are the chances that you
just happened to see the train with the highest number? Nevertheless, if you want to
maximize the chance of getting the answer exactly right, you should guess 60.

But maybe that's not the right goal. An alternative is to compute the mean of the pos-
terior distribution. Given a set of possible quantities, $q _ { i ^ { 2 } }$ and their probabilities, $p _ { i }$ the
mean of the distribution is:

$$m e a n = \sum _ { i } p _ { i } q _ { i }$$

Which we can compute like this:

$$\mathrm { n p } . \mathrm { s u m } \left( \mathrm { p o s t e r i o r } . \mathrm { p s } * \mathrm { p o s t e r i o r } . \mathrm { q s } \right)$$

333.41989326370776

Or we can use the method provided by Pmf:

posterior.mean()
333.41989326370776

<!-- PageFooter="The Train Problem" -->
<!-- PageNumber="59" -->
<!-- PageBreak -->

The mean of the posterior is 333, so that might be a good guess if you want to mini-
mize error. If you played this guessing game over and over, using the mean of the
posterior as your estimate would minimize the mean squared error over the long run.


# Sensitivity to the Prior

The prior I used in the previous section is uniform from 1 to 1000, but I offered no
justification for choosing a uniform distribution or that particular upper bound. We
might wonder whether the posterior distribution is sensitive to the prior. With so lit-
tle data-only one observation-it is.

This table shows what happens as we vary the upper bound:


<table>
<tr>
<th></th>
<th>Posterior mean</th>
</tr>
<tr>
<td>Upper bound</td>
<td></td>
</tr>
<tr>
<td>500</td>
<td>207.079228</td>
</tr>
<tr>
<td>1000</td>
<td>333.419893</td>
</tr>
<tr>
<td>2000</td>
<td>552.179017</td>
</tr>
</table>


As we vary the upper bound, the posterior mean changes substantially. So that's bad.
When the posterior is sensitive to the prior, there are two ways to proceed:

· Get more data.

· Get more background information and choose a better prior.

With more data, posterior distributions based on different priors tend to converge.
For example, suppose that in addition to train 60 we also see trains 30 and 90.

Here's how the posterior means depend on the upper bound of the prior, when we
observe three trains:


## Posterior mean


<table>
<tr>
<td colspan="2">Upper bound</td>
</tr>
<tr>
<td>500</td>
<td>151.849588</td>
</tr>
<tr>
<td>1000</td>
<td>164.305586</td>
</tr>
<tr>
<td>2000</td>
<td>171.338181</td>
</tr>
</table>


The differences are smaller, but apparently three trains are not enough for the poste-
riors to converge.

<!-- PageFooter="Chapter 5: Estimating Counts" -->
<!-- PageNumber="60" -->
<!-- PageBreak -->


# Power Law Prior

If more data are not available, another option is to improve the priors by gathering
more background information. It is probably not reasonable to assume that a train-
operating company with 1,000 locomotives is just as likely as a company with only 1.

With some effort, we could probably find a list of companies that operate locomotives
in the area of observation. Or we could interview an expert in rail shipping to gather
information about the typical size of companies.

But even without getting into the specifics of railroad economics, we can make some
educated guesses. In most fields, there are many small companies, fewer medium-
sized companies, and only one or two very large companies.

In fact, the distribution of company sizes tends to follow a power law, as Robert Axtell
reports in Science.

This law suggests that if there are 1,000 companies with fewer than 10 locomotives,
there might be 100 companies with 100 locomotives, 10 companies with 1,000, and
possibly one company with 10,000 locomotives.

Mathematically, a power law means that the number of companies with a given size,
$N ,$ is proportional to $\left( 1 / N \right) ^ { \alpha } ,$ where $\alpha$ is a parameter that is often near 1.

We can construct a power law prior like this:

$a l p h a = 1 . 0$
$p s = h y p o s ^ { * * } \left( - a l p h a \right)$
$p o w e r = P m f \left( p s , h y p o s , \right.$ name='power law')
power. normalize()

For comparison, here's the uniform prior again:

hypos = np. arange(1, 1001)
uniform = Pmf(1, hypos, name='uniform')
uniform.normalize()
1000

<!-- PageFooter="Power Law Prior" -->
<!-- PageNumber="61" -->
<!-- PageBreak -->

Here's what a power law prior looks like, compared to the uniform prior:


<figure>

Prior distributions

0.12

0.10

0.08

$\sum _ { n = 1 } ^ { 4 }$

0.06

0.04

0.02

0.00

0

250

500

750

1000

1250

1500

1750

2000

Number of trains

</figure>


Here's the update for both priors:

dataset = [60]
update_train(uniform, dataset)
update_train(power, dataset)

And here are the posterior distributions:


<figure>

Posterior distributions

0.0175

0.0150

0.0125

0.0100

$0 . 0 0 7 5$

0.0050

0.0025

0.0000

0

250

500

750

1000

1250

1500

1750

2000

Number of trains

</figure>


The power law gives less prior probability to high values, which yields lower posterior
means, and less sensitivity to the upper bound.

Here's how the posterior means depend on the upper bound when we use a power law
prior and observe three trains:

<!-- PageFooter="Chapter 5: Estimating Counts" -->
<!-- PageNumber="62" -->
<!-- PageBreak -->

Posterior mean


## Upper bound


<table>
<tr>
<td>500</td>
<td>130.708470</td>
</tr>
<tr>
<td>1000</td>
<td>133.275231</td>
</tr>
<tr>
<td>2000</td>
<td>133.997463</td>
</tr>
</table>


Now the differences are much smaller. In fact, with an arbitrarily large upper bound,
the mean converges on 134.

So the power law prior is more realistic, because it is based on general information
about the size of companies, and it behaves better in practice.


# Credible Intervals

So far we have seen two ways to summarize a posterior distribution: the value with
the highest posterior probability (the MAP) and the posterior mean. These are both
point estimates, that is, single values that estimate the quantity we are interested in.

Another way to summarize a posterior distribution is with percentiles. If you have
taken a standardized test, you might be familiar with percentiles. For example, if your
score is the 90th percentile, that means you did as well as or better than 90% of the
people who took the test.

If we are given a value, x, we can compute its percentile rank by finding all values
less than or equal to x and adding up their probabilities.

Pmf provides a method that does this computation. So, for example, we can compute
the probability that the company has less than or equal to 100 trains:

power . prob_le(100)
0.2937469222495771

With a power law prior and a dataset of three trains, the result is about 29%. So 100
trains is the 29th percentile.

Going the other way, suppose we want to compute a particular percentile; for exam-
ple, the median of a distribution is the 50th percentile. We can compute it by adding
up probabilities until the total exceeds 0.5. Here's a function that does it:

def quantile(pmf, prob):
"""Compute a quantile with the given prob. """
total = 0
for q, p in pmf. items():
total $+ = p$
if total >= prob:
return q
return np. nan

<!-- PageFooter="Credible Intervals" -->
<!-- PageNumber="63" -->
<!-- PageBreak -->

The loop uses items, which iterates the quantities and probabilities in the distribu-
tion. Inside the loop we add up the probabilities of the quantities in order. When the
total equals or exceeds prob, we return the corresponding quantity.

This function is called quantile because it computes a quantile rather than a percen-
tile. The difference is the way we specify prob. If prob is a percentage between 0 and
100, we call the corresponding quantity a percentile. If prob is a probability between 0
and 1, we call the corresponding quantity a quantile.

Here's how we can use this function to compute the 50th percentile of the posterior
distribution:

quantile(power, 0.5)

113

The result, 113 trains, is the median of the posterior distribution.

Pmf provides a method called quantile that does the same thing. We can call it like
this to compute the 5th and 95th percentiles:

power. quantile([0.05, 0.95])
array([ 91., 243.])

The result is the interval from 91 to 243 trains, which implies:

· The probability is 5% that the number of trains is less than or equal to 91.

· The probability is 5% that the number of trains is greater than 243.

Therefore the probability is 90% that the number of trains falls between 91 and 243
(excluding 91 and including 243). For this reason, this interval is called a 90% credi-
ble interval.

Pmf also provides credible_interval, which computes an interval that contains the
given probability.

power.credible_interval(0.9)

array([ 91., 243.])


# The German Tank Problem

During World War II, the Economic Warfare Division of the American Embassy in
London used statistical analysis to estimate German production of tanks and other
equipment.

The Western Allies had captured $\log$ books, inventories, and repair records that
included chassis and engine serial numbers for individual tanks.

<!-- PageFooter="Chapter 5: Estimating Counts" -->
<!-- PageNumber="64" -->
<!-- PageBreak -->

Analysis of these records indicated that serial numbers were allocated by manufac-
turer and tank type in blocks of 100 numbers, that numbers in each block were used
sequentially, and that not all numbers in each block were used. So the problem of esti-
mating German tank production could be reduced, within each block of 100 num-
bers, to a form of the Train Problem.

Based on this insight, American and British analysts produced estimates substantially
lower than estimates from other forms of intelligence. And after the war, records
indicated that they were substantially more accurate.

They performed similar analyses for tires, trucks, rockets, and other equipment,
yielding accurate and actionable economic intelligence.

The German Tank Problem is historically interesting; it is also a nice example of real-
world application of statistical estimation.

For more on this problem, see this Wikipedia page and Ruggles and Brodie, “An
Empirical Approach to Economic Intelligence in World War $\mathrm { I I } ^ { \mathrm { P } } ,$ Journal of the Ameri-
can Statistical Association, March 1947, available in the CIA's online reading room.


## Informative Priors

Among Bayesians, there are two approaches to choosing prior distributions. Some
recommend choosing the prior that best represents background information about
the problem; in that case the prior is said to be informative. The problem with using
an informative prior is that people might have different information or interpret it
differently. So informative priors might seem arbitrary.

The alternative is a so-called uninformative prior, which is intended to be as unre-
stricted as possible, to let the data speak for itself. In some cases you can identify a
unique prior that has some desirable property, like representing minimal prior infor-
mation about the estimated quantity.

Uninformative priors are appealing because they seem more objective. But I am gen-
erally in favor of using informative priors. Why? First, Bayesian analysis is always
based on modeling decisions. Choosing the prior is one of those decisions, but it is
not the only one, and it might not even be the most subjective. So even if an uninfor-
mative prior is more objective, the entire analysis is still subjective.

Also, for most practical problems, you are likely to be in one of two situations: either
you have a lot of data or not very much. If you have a lot of data, the choice of the
prior doesn't matter; informative and uninformative priors yield almost the same
results. If you don't have much data, using relevant background information (like the
power law distribution) makes a big difference.

<!-- PageFooter="Informative Priors" -->
<!-- PageNumber="65" -->
<!-- PageBreak -->

And if, as in the German Tank Problem, you have to make life and death decisions
based on your results, you should probably use all of the information at your dis-
posal, rather than maintaining the illusion of objectivity by pretending to know less
than you do.


# Summary

This chapter introduced the Train Problem, which turns out to have the same likeli-
hood function as the Dice Problem, and which can be applied to the German Tank
Problem. In all of these examples, the goal is to estimate a count, or the size of a
population.

In the next chapter, I'll introduce "odds" as an alternative to probabilities, and Bayes's
rule as an alternative form of Bayes's theorem. We'll compute distributions of sums
and products, and use them to estimate the number of members of Congress who are
corrupt, among other problems.

But first, you might want to work on these exercises.


# Exercises


## Exercise 5-1.

Suppose you are giving a talk in a large lecture hall and the fire marshal interrupts
because they think the audience exceeds 1,200 people, which is the safe capacity of the
room.

You think there are fewer then 1,200 people, and you offer to prove it. It would take
too long to count, so you try an experiment:

· You ask how many people were born on May 11 and two people raise their
hands.

· You ask how many were born on May 23 and 1 person raises their hand.

· Finally, you ask how many were born on August 1, and no one raises their hand.

How many people are in the audience? What is the probability that there are more
than 1,200 people? Hint: Remember the binomial distribution.


## Exercise 5-2.

I often see rabbits in the garden behind my house, but it's not easy to tell them apart,
so I don't really know how many there are.

<!-- PageFooter="Chapter 5: Estimating Counts" -->
<!-- PageNumber="66" -->
<!-- PageBreak -->

Suppose I deploy a motion-sensing camera trap that takes a picture of the first rabbit
it sees each day. After three days, I compare the pictures and conclude that two of
them are the same rabbit and the other is different.

How many rabbits visit my garden?

To answer this question, we have to think about the prior distribution and the likeli-
hood of the data:

· I have sometimes seen four rabbits at the same time, so I know there are at least
that many. I would be surprised if there were more than 10. So, at least as a start-
ing place, I think a uniform prior from 4 to 10 is reasonable.

· To keep things simple, let's assume that all rabbits who visit my garden are
equally likely to be caught by the camera trap in a given day. Let's also assume it is
guaranteed that the camera trap gets a picture every day.


## Exercise 5-3.

Suppose that in the criminal justice system, all prison sentences are either 1, 2, or 3
years, with an equal number of each. One day, you visit a prison and choose a pris-
oner at random. What is the probability that they are serving a 3-year sentence? What
is the average remaining sentence of the prisoners you observe?


### Exercise 5-4.

If I chose a random adult in the US, what is the probability that they have a sibling?
To be precise, what is the probability that their mother has had at least one other
child?

This article from the Pew Research Center provides some relevant data.


### Exercise 5-5.

The Doomsday argument is "a probabilistic argument that claims to predict the num-
ber of future members of the human species given an estimate of the total number of
humans born so far."

Suppose there are only two kinds of intelligent civilizations that can happen in the
universe. The "short-lived" kind go extinct after only 200 billion individuals are born.
The "long-lived" kind survive until 2,000 billion individuals are born. And suppose
that the two kinds of civilization are equally likely. Which kind of civilization do you
think we live in?

<!-- PageFooter="Exercises" -->
<!-- PageNumber="67" -->
<!-- PageBreak -->

The Doomsday argument says we can use the total number of humans born so far as
data. According to the Population Reference Bureau, the total number of people who
have ever lived is about 108 billion.

Since you were born quite recently, let's assume that you are, in fact, human being
number 108 billion. If $N$ is the total number who will ever live and we consider you to
be a randomly-chosen person, it is equally likely that you could have been person 1,
or $N ,$ or any number in between. So what is the probability that you would be number
108 billion?

Given this data and dubious prior, what is the probability that our civilization will be
short-lived?

<!-- PageFooter="Chapter 5: Estimating Counts" -->
<!-- PageNumber="68" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 6" -->


# Odds and Addends

This chapter presents a new way to represent a degree of certainty, odds, and a new
form of Bayes's theorem, called Bayes's rule. Bayes's rule is convenient if you want to
do a Bayesian update on paper or in your head. It also sheds light on the important
idea of evidence and how we can quantify the strength of evidence.

The second part of the chapter is about "addends", that is, quantities being added, and
how we can compute their distributions. We'll define functions that compute the dis-
tribution of sums, differences, products, and other operations. Then we'll use those
distributions as part of a Bayesian update.


## Odds

One way to represent a probability is with a number between 0 and 1, but that's not
the only way. If you have ever bet on a football game or a horse race, you have proba-
bly encountered another representation of probability, called odds.

You might have heard expressions like "the odds are three to one", but you might not
know what that means. The odds in favor of an event are the ratio of the probability
it will occur to the probability that it will not.

The following function does this calculation:

def odds(p):
return p / (1-p)

For example, if my team has a 75% chance of winning, the odds in their favor are
three to one, because the chance of winning is three times the chance of losing:

$\mathrm { o d d s } \left( 0 . 7 5 \right)$
3.0

<!-- PageNumber="69" -->
<!-- PageBreak -->

You can write odds in decimal form, but it is also common to write them as a ratio of
integers. So "three to one" is sometimes written 3:1.

When probabilities are low, it is more common to report the odds against rather
than the odds in favor. For example, if my horse has a 10% chance of winning, the
odds in favor are 1:9:

$$\mathrm { o d d s } \left( \theta . 1 \right)$$

0.11111111111111112

But in that case it would be more common to say that the odds against are 9: 1:

$$\mathrm { o d d s } \left( 0 . 9 \right)$$

9.000000000000002

Given the odds in favor, in decimal form, you can convert to probability like this:

def prob(o):
$r e t u r n \quad o / \left( 0 + 1 \right)$

For example, if the odds are $3 / 2 ,$ the corresponding probability is $3 / 5 :$

prob(3/2)
0.6

Or if you represent odds with a numerator and denominator, you can convert to
probability like this:

def prob2(yes, no):
return yes / (yes + no)
prob2(3, 2)
0.6

Probabilities and odds are different representations of the same information; given
either one, you can compute the other. But some computations are easier when we
work with odds, as we'll see $i n$ the next section, and some computations are even eas-
ier with log odds, which we'll see later.


## Bayes's Rule

So far we have worked with Bayes's theorem in the "probability form":

$$P \left( H | D \right) = \frac { P \left( H \right) P \left( D | H \right) } { P \left( D \right) }$$

Writing $\mathrm { o d d s } \left( A \right)$ for odds in favor of $A ,$ we can express Bayes's theorem in "odds
form":

<!-- PageFooter="Chapter 6: Odds and Addends" -->
<!-- PageNumber="70" -->
<!-- PageBreak -->

$$\mathrm { o d d s } \left( A | D \right) = \mathrm { o d d s } \left( A \right) \frac { P \left( D | A \right) } { P \left( D | B \right) }$$

This is Bayes's rule, which says that the posterior odds are the prior odds times the
likelihood ratio. Bayes's rule is convenient for computing a Bayesian update on paper
or in your head. For example, let's go back to the Cookie Problem:

Suppose there are two bowls of cookies. Bowl 1 contains 30 vanilla cookies and 10
chocolate cookies. Bowl 2 contains 20 of each. Now suppose you choose one of the
bowls at random and, without looking, select a cookie at random. The cookie is vanilla.
What is the probability that it came from Bowl 1?

The prior probability is 50%, so the prior odds are 1. The likelihood ratio is $\frac { 3 } { 4 } / \frac { 1 } { 2 } ,$ or
$3 / 2 .$ So the posterior odds are $3 / 2 ,$ which corresponds to probability $3 / 5 .$

prior_odds = 1
likelihood_ratio = (3/4) / (1/2)
post_odds = prior_odds * likelihood_ratio
post_odds
1.5

post_prob = prob(post_odds)
post_prob
0.6

If we draw another cookie and it's chocolate, we can do another update:

likelihood_ratio $= \left( 1 / 4 \right) / \left( 1 / 2 \right)$
post_odds *= likelihood_ratio
post_odds
0.75

And convert back to probability:

post_prob = prob(post_odds)
post_prob
0.42857142857142855


## Oliver's Blood

I'll use Bayes's rule to solve another problem from Mackay's Information Theory,
Inference, and Learning Algorithms:

Two people have left traces of their own blood at the scene of a crime. A suspect,
Oliver, is tested and found to have type $O ^ { \cdot }$ blood. The blood groups of the two traces
are found to be of type ${ } ^ { \mathfrak{c} } O$ (a common type in the local population, having frequency
60%) and of type 'AB' (a rare type, with frequency 1%). Do these data [the traces found
at the scene] give evidence in favor of the proposition that Oliver was one of the people
[who left blood at the scene]?

<!-- PageFooter="Oliver's Blood" -->
<!-- PageNumber="71" -->
<!-- PageBreak -->

To answer this question, we need to think about what it means for data to give evi-
dence in favor of (or against) a hypothesis. Intuitively, we might say that data favor a
hypothesis if the hypothesis is more likely in light of the data than it was before.

In the Cookie Problem, the prior odds are 1, which corresponds to probability 50%.
The posterior odds are $3 / 2 ,$ or probability 60%. So the vanilla cookie is evidence in
favor of Bowl 1.

Bayes's rule provides a way to make this intuition more precise. Again:

$$\mathrm { o d d s } \left( A | D \right) = \mathrm { o d d s } \left( A \right) \frac { P \left( D | A \right) } { P \left( D | B \right) }$$

Dividing through by $\mathrm { o d d s } \left( A \right) ,$ we get:

$$\frac { \mathrm { o d d s } \left( A | D \right) } { \mathrm { o d d s } \left( A \right) } = \frac { P \left( D | A \right) } { P \left( D | B \right) }$$

The term on the left is the ratio of the posterior and prior odds. The term on the right
is the likelihood ratio, also called the Bayes factor.

If the Bayes factor is greater than 1, that means that the data were more likely under $A$
than under $B .$ And that means that the odds are greater, in light of the data, than they
were before.

If the Bayes factor is less than 1, that means the data were less likely under $A$ than
under $B ,$ so the odds in favor of $A$ go down.

Finally, if the Bayes factor is exactly 1, the data are equally likely under either hypoth-
esis, so the odds do not change.

Let's apply that to the problem at hand. If Oliver is one of the people who left blood at
the crime scene, he accounts for the ${ } ^ { \mathfrak{c} } O ^ { \flat }$ sample; in that case, the probability of the
data is the probability that a random member of the population has type 'AB' blood,
which is 1%.

If Oliver did not leave blood at the scene, we have two samples to account for. If we
choose two random people from the population, what is the chance of finding one
with type ${ } ^ { \mathfrak{c} } O ^ { \flat }$ and one with type 'AB'? Well, there are two ways it might happen:

· The first person might have $O ^ { \flat }$ and the second 'AB',

· Or the first person might have 'AB' and the second 'O'.

The probability of either combination is (0.6)(0.01), which is 0.6%, so the total proba-
bility is twice that, or 1.2%. So the data are a little more likely if Oliver is not one of
the people who left blood at the scene.

<!-- PageFooter="Chapter 6: Odds and Addends" -->
<!-- PageNumber="72" -->
<!-- PageBreak -->

We can use these probabilities to compute the likelihood ratio:

$l i k e 1 = 0 . 0 1$
$l i k e 2 = 2 * 0 . 6 * 0 . 0 1$

likelihood_ratio = like1 / like2
likelihood_ratio
0.8333333333333334

Since the likelihood ratio is less than 1, the blood tests are evidence against the
hypothesis that Oliver left blood at the scence.

But it is weak evidence. For example, if the prior odds were 1 (that is, 50% probabil-
ity), the posterior odds would be 0.83, which corresponds to a probability of 45%:

post_odds = 1 * like1 / like2
prob(post_odds)
0.45454545454545453

So this evidence doesn't "move the needle" very much.

This example is a little contrived, but it demonstrates the counterintuitive result that
data consistent with a hypothesis are not necessarily in favor of the hypothesis.

If this result still bothers you, this way of thinking might help: the data consist of a
common event, type 'O' blood, and a rare event, type 'AB' blood. If Oliver accounts
for the common event, that leaves the rare event unexplained. If Oliver doesn't
account for the 'O' blood, we have two chances to find someone in the population
with 'AB' blood. And that factor of two makes the difference.


### Exercise 6-1.

Suppose that based on other evidence, your prior belief in Oliver's guilt is 90%. How
much would the $b l o o d$ evidence in this section change your beliefs? What if you ini-
tially thought there was only a 10% chance of his guilt?


## Addends

The second half of this chapter is about distributions of sums and results of other
operations. We'll start with a Forward Problem, where we are given the inputs and
compute the distribution of the output. Then we'll work on Inverse Problems, where
we are given the outputs and we compute the distribution of the inputs.

As a first example, suppose you roll two dice and add them up. What is the distribu-
tion of the sum? I'll use the following function to create a Pmf that represents the pos-
sible outcomes of a die:

<!-- PageFooter="Addends" -->
<!-- PageNumber="73" -->
<!-- PageBreak -->

import numpy as np
from empiricaldist import Pmf

def make_die(sides):
outcomes = np. arange(1, sides+1)
die = Pmf(1/sides, outcomes)
return die

On a 6-sided die, the outcomes are 1 through 6, all equally likely.

$= \text { make } _ { - } d i e \left( 6 \right)$


<figure>

0.16

0.14

0.12

0.10

PMF

0.08

0.06

0.04

0.02

0.00

1

2

3

4

5

6

Outcome

</figure>


If we roll two dice and add them $u p ,$ there are 11 possible outcomes, 2 through 12,
but they are not equally likely. To compute the distribution of the sum, we have to
enumerate the possible outcomes.

And that's how this function works:

def $a d d \_ d i s t \left( p m f 1 , \right.$ pmf2):
""Compute the distribution of a sum.'
$r e s = P m f \left( \right)$
for q1, p1 in pmf1. items():
for q2, p2 in pmf2. items():
$q = q 1 + q 2$
p = p1 * p2
$r e s \left[ q \right] = r e s \left( q \right) + p$

return res

The parameters are Pmf objects representing distributions.

The loops iterate though the quantities and probabilities in the Pmf objects. Each time
through the loop q gets the sum of a pair of quantities, and p gets the probability of
the pair. Because the same sum might appear more than once, we have to add up the
total probability for each sum.

<!-- PageFooter="Chapter 6: Odds and Addends" -->
<!-- PageNumber="74" -->
<!-- PageBreak -->

Notice a subtle element of this line:

$$r e s \left[ q \right] = r e s \left( q \right) + p$$

I use parentheses on the right side of the assignment, which returns 0 if q does not
appear yet in res. I use brackets on the left side of the assignment to create or update
an element in res; using parentheses on the left side would not work.

Pmf provides add_dist, which does the same thing. You can call it as a method, like
this:

$$\mathrm { t w i c e } = \mathrm { d i e . a d d \_ d i s t } \left( \mathrm { d i e } \right)$$

Or as a function, like this:

twice = Pmf. add_dist(die, die)

And here's what the result looks like:


<figure>

0.16

0.14

0.12

0.10

PMF

0.08

0.06

0.04

0.02

0.00

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

Outcome

</figure>


If we have a sequence of Pmf objects that represent dice, we can compute the distribu-
tion of the sum like this:

def $\mathrm { a d d } _ { - } \mathrm { d i s t } _ { - } \mathrm { s e q } \left( \mathrm { s e q } \right)$ :
"""Compute Pmf of the sum of values from seq. """
$\mathrm { t o t a l } = \mathrm { s e q } \left[ 0 \right]$
for other in seq[1: ]:
total = total. add_dist(other)
return total

As an example, we can make a list of three dice like this:

$$d i c e = \left[ d i e \right] * 3$$

And we can compute the distribution of their sum like this:

$$\mathrm { t h r i c e } = \mathrm { a d d } _ { - } \mathrm { d i s t } _ { - } \mathrm { s e q } \left( \mathrm { d i c e } \right)$$

<!-- PageFooter="Addends" -->
<!-- PageNumber="75" -->
<!-- PageBreak -->

The following figure shows what these three distributions look like:

· The distribution of a single die is uniform from 1 to 6.

· The sum of two dice has a triangle distribution between 2 and 12.

· The sum of three dice has a bell-shaped distribution between 3 and 18.


<figure>

Distributions of sums

0.16

once

twice

0.14

thrice

0.12

0.10

PMF

0.08

0.06

0.04

0.02

0.00

0

3

6

9

12

15

18

Outcome

</figure>


As an aside, this example demonstrates the Central Limit Theorem, which says that
the distribution of a sum converges on a bell-shaped normal distribution, at least
under some conditions.


## Gluten Sensitivity

In 2015 I read a paper that tested whether people diagnosed with gluten sensitivity
(but not celiac disease) were able to distinguish gluten flour from non-gluten flour in
a blind challenge (you can read the paper here).

Out of 35 subjects, 12 correctly identified the gluten flour based on resumption of
symptoms while they were eating it. Another 17 wrongly identified the gluten-free
flour based on their symptoms, and 6 were unable to distinguish.

The authors conclude, "Double-blind gluten challenge induces symptom recurrence
in just one-third of patients."

This conclusion seems odd to me, because if none of the patients were sensitive to
gluten, we would expect some of them to identify the gluten flour by chance. So here's
the question: based on this data, how many of the subjects are sensitive to gluten and
how many are guessing?

<!-- PageFooter="Chapter 6: Odds and Addends" -->
<!-- PageNumber="76" -->
<!-- PageBreak -->

We can use Bayes's theorem to answer this question, but first we have to make some
modeling decisions. I'll assume:

· People who are sensitive to gluten have a 95% chance of correctly identifying glu-
ten flour under the challenge conditions, and

· People who are not sensitive have a 40% chance of identifying the gluten flour by
chance (and a 60% chance of either choosing the other flour or failing to distin-
guish).

These particular values are arbitrary, but the results are not sensitive to these choices.
I will solve this problem in two steps. First, assuming that we know how many sub-
jects are sensitive, I will compute the distribution of the data. Then, using the likeli-
hood of the data, I will compute the posterior distribution of the number of sensitive
patients.

The first is the Forward Problem; the second is the Inverse Problem.


## The Forward Problem

Suppose we know that 10 of the 35 subjects are sensitive to gluten. That means that
25 are not:

$n = 3 5$
num_sensitive = 10
num_insensitive = n - num_sensitive

Each sensitive subject has a 95% chance of identifying the gluten flour, so the number
of correct identifications follows a binomial distribution.

I'll use make_binomial, which we defined in "The Binomial Distribution" on page 44,
to make a Pmf that represents the binomial distribution:

from utils import make_binomial

dist_sensitive = make_binomial(num_sensitive, 0.95)
dist_insensitive = make_binomial(num_insensitive, 0.40)

The results are the distributions for the number of correct identifications in each
group.

Now we can use add_dist to compute the distribution of the total number of correct
identifications:

$$= \text { Pnf } _ { - }$$

<!-- PageFooter="The Forward Problem" -->
<!-- PageNumber="77" -->
<!-- PageBreak -->

Here are the results:


<figure>

Gluten sensitivity

0.6

sensitive

insensitive

0.5

total

0.4

$\sum _ { n = 1 } ^ { 4 }$

0.3

0.2

0.1

0.0

0

5

10

15

20

25

30

35

Number of correct identifications

</figure>


We expect most of the sensitive subjects to identify the gluten flour correctly. Of the
25 insensitive subjects, we expect about 10 to identify the gluten flour by chance. So
we expect about 20 correct identifications in total.

This is the answer to the Forward Problem: given the number of sensitive subjects, we
can compute the distribution of the data.


## The Inverse Problem

Now let's solve the Inverse Problem: given the data, we'll compute the posterior distri-
bution of the number of sensitive subjects.

Here's how. I'll loop through the possible values of num_sensitive and compute the
distribution of the data for each:

import pandas as pd

table = pd. DataFrame()
for num_sensitive in range(0, n+1):
num_insensitive = n - num_sensitive
dist_sensitive = make_binomial(num_sensitive, 0.95)
dist_insensitive = make_binomial(num_insensitive, 0.4)
dist_total = Pmf. add_dist(dist_sensitive, dist_insensitive)
table[num_sensitive] = dist_total

The loop enumerates the possible values of num_sensitive. For each value, it com-
putes the distribution of the total number of correct identifications, and stores the
result as a column in a pandas DataFrame.

<!-- PageFooter="Chapter 6: Odds and Addends" -->
<!-- PageNumber="78" -->
<!-- PageBreak -->

The following figure shows selected columns from the DataFrame, corresponding to
different hypothetical values of num_sensitive:


<figure>

Gluten sensitivity

0.25

$n u m \_ s e n s i t i v e = 0$

$n u m \_ s e n s i t i v e = 1 0$

0.20

$n u m \_ s e n s i t i v e = 2 0$

$n u m \_ s e n s i t i v e = 3 0$

0.15

PMF

0.10

0.05

0.00

0

5

10

15

20

25

30

35

Number of correct identifications

</figure>


Now we can use this table to compute the likelihood of the data:

likelihood1 = table. loc[ 12]

loc selects a row from the DataFrame. The row with index 12 contains the probability
of 12 correct identifications for each hypothetical value of num_sensitive. And that's
exactly the likelihood we need to do a Bayesian update.

I'll use a uniform prior, which implies that I would be equally surprised by any value
of num_sensitive:

hypos = np. arange(n+1)
prior = Pmf(1, hypos)

And here's the update:

posterior1 = prior * likelihood1
posterior1.normalize()

For comparison, I also compute the posterior for another possible outcome, 20 cor-
rect identifications:

likelihood2 = table. loc[20]
posterior2 = prior * likelihood2
posterior2.normalize()

The following figure shows posterior distributions of num_sensitive based on the
actual data, 12 correct identifications, and the other possible outcome, 20 correct
identifications.

<!-- PageFooter="The Inverse Problem" -->
<!-- PageNumber="79" -->
<!-- PageBreak -->


<figure>

Posterior distributions

posterior with 12 correct

posterior with 20 correct

0.20

0.15

$\sum _ { n = 1 } ^ { 1 1 }$

0.10

0.05

0.00

0

5

10

15

20

25

30

35

Number of sensitive subjects

</figure>


With 12 correct identifications, the most likely conclusion is that none of the $s u b j e c t s$
are sensitive to gluten. If there had been 20 correct identifications, the most likely
conclusion would be that 11-12 of the subjects were sensitive.

posterior1.max_prob()

0

posterior2.max_prob()

11


### Summary

This chapter presents two topics that are almost unrelated except that they make the
title of the chapter catchy.

The first part of the chapter is about Bayes's rule, evidence, and how we can quantify
the strength of evidence using a likelihood ratio or Bayes factor.

The second part is about $a d d _ { - } d i s t ,$ which computes the distribution of a sum. We
can use this function to solve Forward and Inverse Problems; that is, given the
parameters of a system, we can compute the distribution of the data or, given the
data, we can compute the distribution of the parameters.

In the next chapter, we'll compute distributions for minimums and maximums, and
use them to solve more Bayesian problems. But first you might want to work on these
exercises.

<!-- PageFooter="Chapter 6: Odds and Addends" -->
<!-- PageNumber="80" -->
<!-- PageBreak -->


## More Exercises


### Exercise 6-2.

Let's use Bayes's rule to solve the Elvis problem from Chapter 3:

Elvis Presley had a twin brother who died at birth. What is the probability that Elvis
was an identical twin?

In 1935, about $2 / 3$ of twins were fraternal and $1 / 3$ were identical. The question con-
tains two pieces of information we can use to update this prior.

· First, Elvis's twin was also male, which is more likely if they were identical twins,
with a likelihood ratio of 2.

· Also, Elvis's twin died at birth, which is more likely if they were identical twins,
with a likelihood ratio of 1.25.

If you are curious about where those numbers come from, I wrote a blog post about
it.


### Exercise 6-3.

The following is an interview question that appeared on glassdoor.com, attributed to
Facebook:

You're about to get on a plane to Seattle. You want to know if you should bring an
umbrella. You call 3 random friends of yours who live there and ask each independ-
ently if it's raining. Each of your friends has a $2 / 3$ chance of telling you the truth and a
$1 / 3$ chance of messing with you by lying. All 3 friends tell you that "Yes" it is raining.
What is the probability that it's actually raining in Seattle?

Use Bayes's rule to solve this problem. As a prior you can assume that it rains in Seat-
tle about 10% of the time.

This question causes some confusion about the differences between Bayesian and fre-
quentist interpretations of probability; if you are curious about this point, I wrote a
blog article about it.


#### Exercise 6-4.

According to the CDC, people who smoke are about 25 times more likely to develop
lung cancer than nonsmokers.

Also according to the CDC, about 14% of adults in the US are smokers. If you learn
that someone has lung cancer, what is the probability they are a smoker?

<!-- PageFooter="More Exercises" -->
<!-- PageNumber="81" -->
<!-- PageBreak -->


### Exercise 6-5.

In Dungeons & Dragons, the amount of damage a goblin can withstand is the sum of
two 6-sided dice. The amount of damage you inflict with a short sword is determined
by rolling one 6-sided die. A goblin is defeated if the total damage you inflict is
greater than or equal to the amount it can withstand.

Suppose you are fighting a goblin and you have already inflicted 3 points of damage.
What is your probability of defeating the goblin with your next successful attack?

Hint: You can use Pmf. add_dist to add a constant amount, like 3, to a Pmf and
Pmf . sub_dist to compute the distribution of remaining points.


### Exercise 6-6.

Suppose I have a box with a 6-sided die, an 8-sided die, and a 12-sided die. I choose
one of the dice at random, roll it twice, multiply the outcomes, and report that the
product is 12. What is the probability that I chose the 8-sided die?

Hint: Pmf provides a function called mul_dist that takes two Pmf objects and returns
a Pmf that represents the distribution of the product.


### Exercise 6-7.

Betrayal at House on the Hill is a strategy game in which characters with different
attributes explore a haunted house. Depending on their attributes, the characters roll
different numbers of dice. For example, if attempting a task that depends on knowl-
edge, Professor Longfellow rolls 5 dice, Madame Zostra rolls 4, and Ox Bellows rolls
3. Each die yields 0, 1, or 2 with equal probability.

If a randomly chosen character attempts a task three times and rolls a total of 3 on the
first attempt, 4 on the second, and 5 on the third, which character do you think it
was?


### Exercise 6-8.

There are 538 members of the United States Congress.

Suppose we audit their investment portfolios and find that 312 of them outperform
the market. Let's assume that an honest member of Congress has only a 50% chance
of outperforming the market, but a dishonest member who trades on inside informa-
tion has a 90% chance. How many members of Congress are honest?

<!-- PageFooter="Chapter 6: Odds and Addends" -->
<!-- PageNumber="82" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 7" -->


# Minimum, Maximum, and Mixture

In the previous chapter we computed distributions of sums. In this chapter, we'll
compute distributions of minimums and maximums, and use them to solve both For-
ward and Inverse Problems.

Then we'll look at distributions that are mixtures of other distributions, which will
turn out to be particularly useful for making predictions.

But we'll start with a powerful tool for working with distributions, the cumulative dis-
tribution function.


## Cumulative Distribution Functions

So far we have been using probability mass functions to represent distributions. A
useful alternative is the cumulative distribution function, or CDF.

As an example, I'll use the posterior distribution from the Euro Problem, which we
computed in "Bayesian Estimation" on page 47.

Here's the uniform prior we started with:

import numpy as np
from empiricaldist import Pmf

hypos = np. linspace(0, 1, 101)
pmf = Pmf(1, hypos)
data = 140, 250

And here's the update:

<!-- PageNumber="83" -->
<!-- PageBreak -->


### from scipy. stats import binom

def update_binomial(pmf, data) :
"""Update pmf using the binomial distribution. ""'
k, n = data
XS = pmf. qs
likelihood = binom.pmf(k, n, xs)
☒

$^ { * } = l i k e l i h o$
pmf.normalize()

update_binomial(pmf, data)

The CDF is the cumulative sum of the PMF, so we can compute it like this:

$$c u m u l a t i v e = p m f . c u m s u m \left( \right)$$

Here's what it looks like, along with the PMF:


<figure>

Posterior distribution for the Euro problem

1.0

CDF

$P M F$

0.8

Probability

0.6

0.4

0.2

0.0

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of heads (x)
☒

</figure>


The range of the CDF is always from 0 to 1, in contrast with the PMF, where the max-
imum can be any probability.

The result from cumsum is a pandas Series, so we can use the bracket operator to
select an element:

cumulative[0.61]

0.9638303193984253

The result is about 0.96, which means that the total probability of all quantities less
than or equal to 0.61 is 96%.

<!-- PageFooter="Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageNumber="84" -->
<!-- PageBreak -->

To go the other way-to look up a probability and get the corresponding quantile-
we can use interpolation:

from scipy. interpolate import interp1d

ps = cumulative. values
qs = cumulative. index

interp = interp1d(ps, qs)
interp(0.96)
array(0.60890171)

The result is about 0.61, so that confirms that the 96th percentile of this distribution
is 0.61.

empiricaldist provides a class called Cdf that represents a cumulative distribution
function. Given a Pmf, you can compute a $\mathrm { C d f }$ like this:

$$c d f = p n f . m a k e _ { - } c d f \left( \right)$$

make_cdf uses np. cumsum to compute the cumulative sum of the probabilities.

You can use brackets to select an element from a Cdf:

cdf[0.61]
0.9638303193984253

But if you look up a quantity that's not in the distribution, you get a KeyError.

To avoid this problem, you can call a Cdf as a function, using parentheses. If the argu-
ment does not appear in the Cdf, it interpolates between quantities.

$$\mathrm { c d f } \left( 0 . 6 1 5 \right)$$

array(0.96383032)

Going the other way, you can use quantile to look up a cumulative probability and
get the corresponding quantity:

$$\mathrm { c d f } . \text { quantile } \left( 0 . 9 6 3 8 3 0 3 \right)$$

array(0.61)

Cdf also provides credible_interval, which computes a credible interval that con-
tains the given probability:

cdf.credible_interval(0.9)

array([0.51, 0.61])

<!-- PageFooter="Cumulative Distribution Functions" -->
<!-- PageNumber="85" -->
<!-- PageBreak -->

CDFs and PMFs are equivalent in the sense that they contain the same information
about the distribution, and you can always convert from one to the other. Given a
Cdf, you can get the equivalent Pmf like this:

$$\mathrm { p m f } = \mathrm { c d f } . \mathrm { m a k e } \_ \mathrm { p m f } \left( \right)$$

make_pmf uses np.diff to compute differences between consecutive cumulative
probabilities.

One reason Cdf objects are useful is that they compute quantiles efficiently. Another
is that they make it easy to compute the distribution of a maximum or minimum, as
we'll see in the next section.


## Best Three of Four

In Dungeons & Dragons, each character has six attributes: strength, intelligence, wis-
dom, dexterity, constitution, and charisma.

To generate a new character, players roll four 6-sided dice for each attribute and add
up the best three. For example, if I roll for strength and get 1, 2, 3, 4 on the dice, my
character's strength would be the sum of 2, 3, and 4, which is 9.

As an exercise, let's figure out the distribution of these attributes. Then, for each char-
acter, we'll figure out the distribution of their best attribute.

I'll import two functions from the previous chapter: make_die, which makes a Pmf
that represents the outcome of rolling a die, and add_dist_seq, which takes a
sequence of Pmf objects and computes the distribution of their sum.

Here's a Pmf that represents a 6-sided die and a sequence with three references to it:

from utils import make_die

$d i e = \text { nake } _ { - } d i e \left( 6 \right)$
$d i c e = \left[ d i e \right] * 3$

And here's the distribution of the sum of three dice:

from utils import add_dist_seq
pmf_3d6 = add_dist_seq(dice)

<!-- PageFooter="Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageNumber="86" -->
<!-- PageBreak -->

Here's what it looks like:


<figure>

Distribution of attributes

0.12

0.10

0.08

$\sum _ { n = 1 } ^ { 1 1 }$

0.06

0.04

0.02

0.00

4

6

8

10

12

14

16

18

Outcome

</figure>


If we roll four dice and add up the best three, computing the distribution of the sum
is a bit more complicated. I'll estimate the distribution by simulating 10,000 rolls.

First I'll create an array of random values from 1 to 6, with 10,000 rows and 4
columns:

$$n = 1 0 0 0 0$$

a = np.random.randint(1, 7, size=(n, 4))

To find the best three outcomes in each row, I'll use sort with $a \times i s = 1 ,$ which sorts the
rows in ascending order:

$$a \cdot \mathrm { s o r t } \left( a x i s = 1 \right)$$

Finally, I'll select the last three columns and add them up:

$$t = a \left[ : , 1 : \right] . \sin \left( a \times i s = 1 \right)$$

Now $\mathrm { t }$ is an array with a single column and 10,000 rows. We can compute the PMF of
the values in t like this:

$$\mathrm { p n f } _ { - } \mathrm { b e s t 3 } = \mathrm { P i n f } . \mathrm { f r o m } _ { - } \mathrm { s e q } \left( t \right)$$

<!-- PageFooter="Best Three of Four" -->
<!-- PageNumber="87" -->
<!-- PageBreak -->

The following figure shows the distribution of the sum of three dice, pmf_3d6, and the
distribution of the best three out of four, pmf_best3:


<figure>
<figcaption>Distribution of attributes</figcaption>

sum of 3 dice

0.12

best 3 of 4

0.10

0.08

PMF

0.06

0.04

0.02

0.00

4

6

8

10

12

14

16

18

Outcome

</figure>


As you might expect, choosing the best three out of four tends to yield higher values.

Next we'll find the distribution for the maximum of six attributes, each the sum of the
best three of four dice.


### Maximum

To compute the distribution of a maximum or minimum, we can make good use of
the cumulative distribution function. First, I'll compute the Cdf of the best three of
four distribution:

$$\mathrm { c d f } _ { - } \mathrm { b e s t 3 } = \mathrm { p r i f } _ { - } \mathrm { b e s t 3 } . \mathrm { m a k e } _ { - } \mathrm { c d f } \left( \right)$$

Recall that $\mathrm { c d f } \left( x \right)$ is the sum of probabilities for quantities less than or equal to x.
☒
Equivalently, it is the probability that a random value chosen from the distribution is
less than or equal to x.

Now suppose I draw 6 values from this distribution. The probability that all 6 of them
are less than or equal to $\mathrm { x }$ is $\mathrm { c d f } \left( x \right)$ raised to the 6th power, which we can compute
like this:

cdf_best3 ** 6

<!-- PageFooter="Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageNumber="88" -->
<!-- PageBreak -->

If all 6 values are less than or equal to x, that means that their maximum is less than
or equal to x. So the result is the CDF of their maximum. We can convert it to a $\mathrm { C d f }$
object, like this:


#### from empiricaldist import Cdf

$$\mathrm { c d f } _ { - } \mathrm { m a x } 6 = \mathrm { c d f } \left( \mathrm { c d f } _ { - } \mathrm { b e s t 3 } ^ { * * } 6 \right)$$

The following figure shows the CDFs for the three distributions we have computed.


<figure>

Distribution of attributes

1.0

sum of 3 dice

best 3 of 4 dice

0.8

$m a x \quad o f \quad 6 \quad a t t r i b u t e s$

0.6

CDF

0.4

0.2

0.0

4

6

8

10

12

14

16

18

Outcome

</figure>


Cdf provides max_dist, which does the same computation, so we can also compute
the Cdf of the maximum like this:

cdf_max_dist6 = cdf_best3.max_dist(6)

In the next section we'll find the distribution of the minimum. The process is similar,
but a little more complicated. See if you can figure it out before you go on.


### Minimum

In the previous section we computed the distribution of a character's best attribute.
Now let's compute the distribution of the worst.

To compute the distribution of the minimum, we'll use the complementary CDF,
which we can compute like this:

$$\mathrm { p r o b } _ { - } g t = 1 - \text { cdf } _ { - }$$

As the variable name suggests, the complementary CDF is the probability that a value
from the distribution is greater than x. If we draw 6 values from the distribution, the
probability that all 6 exceed $x$ is:

$$\mathrm { p r o b } _ { - } g t 6 = p r o b _ { - } g t ^ { * * } 6$$

<!-- PageFooter="Minimum" -->
<!-- PageNumber="89" -->
<!-- PageBreak -->

If all 6 exceed x, that means their minimum exceeds x, so prob_gt6 is the comple-
mentary CDF of the minimum. And that means we can compute the CDF of the min-
imum like this:

$$\mathrm { p r o b } _ { - } \mathrm { l e 6 } = 1 - \mathrm { p r o b } _ { - } g \mathrm { t 6 }$$

The result is a pandas Series that represents the CDF of the minimum of six
attributes. We can put those values in a $\mathrm { C d f }$ object like this:

$$\mathrm { c d f } _ { - } \mathrm { m i n 6 } = \mathrm { c d f } \left( \mathrm { p r o b } _ { - } \mathrm { l e 6 } \right)$$

Here's what it looks like, along with the distribution of the maximum:


<figure>
<figcaption>Minimum and maximum of $\sin$ attributes</figcaption>

1.0

minimum of 6

maximum of 6

0.8

0.6

CDF

0.4

0.2

0.0

4

6

8

10

12

14

16

18

Outcome

</figure>


Cdf provides $\mathrm { m i n } _ { - } \mathrm { d i s t } ,$ which does the same computation, so we can also compute
the Cdf of the minimum like this:

cdf_min_dist6 = cdf_best3.min_dist(6)

And we can confirm that the differences are small:

np.allclose(cdf_min_dist6, cdf_min6)

True

In the exercises at the end of this chapter, you'll use distributions of the minimum
and maximum to do Bayesian inference. But first we'll see what happens when we
mix distributions.


## Mixture

In this section I'll show how we can compute a distribution that is a mixture of other
distributions. I'll explain what that means with some simple examples; then, more
usefully, we'll see how these mixtures are used to make predictions.

<!-- PageFooter="Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageNumber="90" -->
<!-- PageBreak -->

Here's another example inspired by Dungeons & Dragons:

· Suppose your character is armed with a dagger in one hand and a short sword in
the other.

· During each round, you attack a monster with one of your two weapons, chosen
at random.

· The dagger causes one 4-sided die of damage; the short sword causes one 6-sided
die of damage.

What is the distribution of damage you inflict in each round?

To answer this question, I'll make a Pmf to represent the 4-sided and 6-sided dice:

$$d 4 = \text { make } _ { - } d i e \left( 4 \right)$$
$$d 6 = \text { make } _ { - } d i e \left( 6 \right)$$

Now, let's compute the probability you inflict 1 point of damage.

· If you attacked with the dagger, it's $1 / 4 .$

· If you attacked with the short sword, it's $1 / 6 .$

Because the probability of choosing either weapon is $1 / 2 ,$ the total probability is the
average:

$$p r o b \_ 1 = \left( d 4 \left( 1 \right) + d 6 \left( 1 \right) \right) / 2$$

prob_1

$$0 . 2 0 8 3 3 3 3 3 3 3 3 3 3 3 3 3 1$$

For the outcomes 2, 3, and 4, the probability is the same, but for 5 and 6, it's different,
because those outcomes are impossible with the 4-sided die.

$$p r o b \_ 6 = \left( d 4 \left( 6 \right) + d 6 \left( 6 \right) \right) / 2$$
prob_6

$$0 . 0 8 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3$$

To compute the distribution of the mixture, we could loop through the possible out-
comes and compute their probabilities.

But we can do the same computation using the + operator:

$$m i x 1 = \left( d 4 + d 6 \right) / 2$$

Here's what the mixture of these distributions looks like:

<!-- PageFooter="Mixture" -->
<!-- PageNumber="91" -->
<!-- PageBreak -->


<figure>

Mixture of one 4-sided and one 6-sided die

0.200

0.175

0.150

0.125

$0 . 1 0 0$

0.075

0.050

0.025

0.000

1

2

3

4

5

6

Outcome

</figure>


Now suppose you are fighting three monsters:

· One has a club, which causes one 4-sided die of damage.

· One has a mace, which causes one 6-sided die.

· And one has a quarterstaff, which also causes one 6-sided die.

Because the melee is disorganized, you are attacked by one of these monsters each
round, chosen at random. To find the distribution of the damage they inflict, we can
compute a weighted average of the distributions, like this:

$$m i x 2 = \left( d 4 + 2 ^ { * } d 6 \right) / 3$$

This distribution is a mixture of one 4-sided die and two 6-sided dice. Here's what it
looks like:


<figure>
<figcaption>Mixture of one 4-sided and two 6-sided die</figcaption>

0.200

0.175

0.150

0.125

PMF

0.100

0.075

0.050

0.025

0.000

1

2

3

4

5

6

Outcome

</figure>


<!-- PageFooter="Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageNumber="92" -->
<!-- PageBreak -->

In this section we used the + operator, which adds the probabilities in the distribu-
tions, not to be confused with Pmf . add_dist, which computes the distribution of the
sum of the distributions.

To demonstrate the difference, I'll use Pmf . add_dist to compute the distribution of
the total damage done per round, which is the sum of the two mixtures:

$$= \text { Pnf } . \text { dist } \left( n i \times 1 , m i \times 2 \right)$$

And here's what it looks like:


<figure>
<figcaption>Total damage inflicted by both parties</figcaption>

0.16

0.14

0.12

0.10

PMF

0.08

0.06

0.04

0.02

0.00

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

Outcome

</figure>


## General Mixtures

In the previous section we computed mixtures in an ad hoc way. Now we'll see a more
general solution. In future chapters, we'll use this solution to generate predictions for
real-world problems, not just role-playing games. But if you'll bear with me, we'll
continue the previous example for one more section.

Suppose three more monsters join the combat, each of them with a battle axe that
causes one 8-sided die of damage. Still, only one monster attacks per round, chosen at
random, so the damage they inflict is a mixture of:

· One 4-sided die,

· Two 6-sided dice, and

· Three 8-sided dice.

<!-- PageFooter="General Mixtures" -->
<!-- PageNumber="93" -->
<!-- PageBreak -->

I'll use a Pmf to represent a randomly chosen monster:

$$h y p o s = \left[ 4 , 6 , 8 \right]$$

counts = [1,2,3]
pmf_dice = Pmf(counts, hypos)
pmf_dice.normalize()
pmf_dice

probs

4
0.166667

6
0.333333

8
0.500000

This distribution represents the number of sides on the die we'll roll and the proba-
bility of rolling each one. For example, one of the six monsters has a dagger, so the
probability is $1 / 6$ that we roll a 4-sided die.

Next I'll make a sequence of Pmf objects to represent the dice:

$$= \left[ \text { make } _ { - } \text { die } \left( \text { sides } \right) \text { for sides in hypos } \right]$$

To compute the distribution of the mixture, I'll compute the weighted average of the
dice, using the probabilities in pmf_dice as the weights.

To express this computation concisely, it is convenient to put the distributions into a
pandas DataFrame:

import pandas as pd

pd. DataFrame(dice)


<table>
<tr>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
</tr>
<tr>
<td>0.250000</td>
<td>0.250000</td>
<td>0.250000</td>
<td>0.250000</td>
<td>NaN</td>
<td>NaN</td>
<td>NaN</td>
<td>NaN</td>
</tr>
<tr>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>NaN</td>
<td>NaN</td>
</tr>
<tr>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125</td>
<td>0.125</td>
</tr>
</table>


The result is a DataFrame with one row for each distribution and one column for each
possible outcome. Not all rows are the same length, so pandas fills the extra spaces
with the special value NaN, which stands for "not a number". We can use fillna to
replace the NaN values with 0:

pd. DataFrame(dice) . fillna(0)


<table>
<tr>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
</tr>
<tr>
<td>0.250000</td>
<td>0.250000</td>
<td>0.250000</td>
<td>0.250000</td>
<td>0.000000</td>
<td>0.000000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>0.166667</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125000</td>
<td>0.125</td>
<td>0.125</td>
</tr>
</table>


<!-- PageFooter="Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageNumber="94" -->
<!-- PageBreak -->

The next step is to multiply each row by the probabilities in pmf_dice, which turns
out to be easier if we transpose the matrix so the distributions run down the columns
rather than across the rows:

$$d f = p d . D a t a F r a m e \left( d i c e \right) . f i l l n a \left( 0 \right) . t r a n s p o s e \left( \right)$$

Now we can multiply by the probabilities in pmf_dice:

$$d f * = p n f _ { - } d i c e . p s$$

$d f$


<table>
<tr>
<td>1</td>
<td>0.041667</td>
<td>0.055556</td>
<td>0.0625</td>
</tr>
<tr>
<td>2</td>
<td>0.041667</td>
<td>0.055556</td>
<td>0.0625</td>
</tr>
<tr>
<td>3</td>
<td>0.041667</td>
<td>0.055556</td>
<td>0.0625</td>
</tr>
<tr>
<td>4</td>
<td>0.041667</td>
<td>0.055556</td>
<td>0.0625</td>
</tr>
<tr>
<td>5</td>
<td>0.000000</td>
<td>0.055556</td>
<td>0.0625</td>
</tr>
<tr>
<td>6</td>
<td>0.000000</td>
<td>0.055556</td>
<td>0.0625</td>
</tr>
<tr>
<td>7</td>
<td>0.000000</td>
<td>0.000000</td>
<td>0.0625</td>
</tr>
<tr>
<td>8</td>
<td>0.000000</td>
<td>0.000000</td>
<td>0.0625</td>
</tr>
</table>


And add up the weighted distributions:

$\mathrm { d f } . \mathrm { s u m } \left( \mathrm { a x } i \mathrm { s } = 1 \right)$

The argument $a \times i s = 1$ means we want to sum across the rows. The result is a pandas
Series.

Putting it all together, here's a function that makes a weighted mixture of
distributions:

def make_mixture(pmf, pmf_seq):
"""Make a mixture of distributions. """
df = pd. DataFrame(pmf_seq) . fillna(0). transpose()
df *= np. array(pmf)
$= \mathrm { d f } . \sin \left( a x i s = 1 \right)$
return Pmf(total)

The first parameter is a Pmf that maps from each hypothesis to a probability. The sec-
ond parameter is a sequence of Pmf objects, one for each hypothesis. We can call it
like this:

$$\mathrm { m i x } = \mathrm { m a k e } _ { - } \mathrm { m i x t u r e } \left( \mathrm { p m f } _ { - } \mathrm { d i c e } , \mathrm { d i c e } \right)$$

<!-- PageFooter="General Mixtures" -->
<!-- PageNumber="95" -->
<!-- PageBreak -->

And here's what it looks like:


<figure>

Distribution of damage with three different weapons

0.16

mixture

0.14

0.12

0.10

PMF

0.08

0.06

0.04

0.02

0.00

1

2

3

4

5

6

7

8

Outcome

</figure>


In this section I used pandas so that make_mixture is concise, efficient, and hopefully
not too hard to understand. In the exercises at the end of the chapter, you'll have a
chance to practice with mixtures, and we will use make_mixture again in the next
chapter.


### Summary

This chapter introduces the Cdf object, which represents the cumulative distribution
function (CDF).

A Pmf and the corresponding Cdf are equivalent in the sense that they contain the
same information, so you can convert from one to the other. The primary difference
between them is performance: some operations are faster and easier with a Pmf; oth-
ers are faster with a Cdf.

In this chapter we used Cdf objects to compute distributions of maximums and mini-
mums; these distributions are useful for inference if we are given a maximum or min-
imum as data. You will see some examples in the exercises, and in future chapters. We
also computed mixtures of distributions, which we will use in the next chapter to
make predictions.

But first you might want to work on these exercises.

<!-- PageFooter="Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageNumber="96" -->
<!-- PageBreak -->


## Exercises


### Exercise 7-1.

When you generate a Dungeons & Dragons character, instead of rolling dice, you can
use the "standard array" of attributes, which is 15, 14, 13, 12, 10, and 8. Do you think
you are better off using the standard array or (literally) rolling the dice?

Compare the distribution of the values in the standard array to the distribution we
computed for the best three out of four:

· Which distribution has higher mean? Use the mean method.

· Which distribution has higher standard deviation? Use the std method.

· The lowest value in the standard array is 8. For each attribute, what is the proba-
bility of getting a value less than 8? If you roll the dice six times, what's the proba-
bility that at least one of your attributes is less than 8?

· The highest value in the standard array is 15. For each attribute, what is the prob-
ability of getting a value greater than 15? If you roll the dice six times, what's the
probability that at least one of your attributes is greater than 15?


### Exercise 7-2.

Suppose you are fighting three monsters:

· One is armed with a short sword that causes one 6-sided die of damage,

· One is armed with a battle axe that causes one 8-sided die of damage, and

· One is armed with a bastard sword that causes one 10-sided die of damage.

One of the monsters, chosen at random, attacks you and does 1 point of damage.

Which monster do you think it was? Compute the posterior probability that each
monster was the attacker.

If the same monster attacks you again, what is the probability that you suffer 6 points
of damage?

Hint: Compute a posterior distribution as we have done before and pass it as one of
the arguments to make_mixture.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="97" -->
<!-- PageBreak -->


### Exercise 7-3.

Henri Poincaré was a French mathematician who taught at the Sorbonne around
1900. The following anecdote about him is probably fiction, but it makes an interest-
ing probability problem.

Supposedly Poincaré suspected that his local bakery was selling loaves of bread that
were lighter than the advertised weight of 1 kg, so every day for a year he bought a
loaf of bread, brought it home and weighed it. At the end of the year, he plotted the
distribution of his measurements and showed that it fit a normal distribution with
mean 950 g and standard deviation 50 g. He brought this evidence to the bread
police, who gave the baker a warning.

For the next year, Poincaré continued to weigh his bread every day. At the end of the
year, he found that the average weight was 1000 g, just as it should be, but again he
complained to the bread police, and this time they fined the baker.

Why? Because the shape of the new distribution was asymmetric. Unlike the normal
distribution, it was skewed to the right, which is consistent with the hypothesis that
the baker was still making 950 g loaves, but deliberately giving Poincaré the heavier
ones.

To see whether this anecdote is plausible, let's suppose that when the baker sees Poin-
caré coming, he hefts $n$ loaves of bread and gives Poincaré the heaviest one.
How many loaves would the baker have to heft to make the average of the maximum
1000 g?

<!-- PageNumber="98 Chapter 7: Minimum, Maximum, and Mixture" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 8" -->


## Poisson Processes

This chapter introduces the Poisson process, which is a model used to describe events
that occur at random intervals. As an example of a Poisson process, we'll model goal-
scoring in soccer, which is American English for the game everyone else calls "foot-
ball". We'll use goals scored in a game to estimate the parameter of a Poisson process;
then we'll use the posterior distribution to make predictions.

And we'll solve the World Cup Problem.


## The World Cup Problem

In the 2018 FIFA World Cup final, France defeated Croatia 4 goals to 2. Based on this
outcome:

1\. How confident should we be that France is the better team?

2\. If the same teams played again, what is the chance France would win again?

To answer these questions, we have to make some modeling decisions.

· First, I'll assume that for any team against another team there is some unknown
goal-scoring rate, measured in goals per game, which I'll denote with the Python
variable lam or the Greek letter $\lambda ,$ pronounced "lambda".

· Second, I'll assume that a goal is equally likely during any minute of a game. So,
in a 90-minute game, the probability of scoring during any minute is $\lambda / 9 0 .$

· Third, I'll assume that a team never scores twice during the same minute.

Of course, none of these assumptions is completely true in the real world, but I think
they are reasonable simplifications. As George Box said, "All models are wrong; some
are useful" (https://oreil.ly/oeTQU).

<!-- PageNumber="99" -->
<!-- PageBreak -->

In this case, the model is useful because if these assumptions are true, at least roughly,
the number of goals scored in a game follows a Poisson distribution, at least roughly.


## The Poisson Distribution

If the number of goals scored in a game follows a Poisson distribution with a goal-
scoring rate, $\lambda ,$ the probability of scoring $k$ goals is

$$\lambda ^ { k } \exp \left( - \lambda \right) / k !$$

for any non-negative value of $k .$

$\mathrm { S c i P y }$ provides a poisson object that represents a Poisson distribution. We can create
one with $\lambda = 1 . 4$ like this:

from scipy. stats import poisson

lam = 1.4
dist = poisson(lam)
type(dist)
scipy. stats ._ distn_infrastructure.rv_frozen

The result is an object that represents a "frozen" random variable and provides pmf,
which evaluates the probability mass function of the Poisson distribution.

k = 4
dist.pmf(k)
0.039471954028253146

This result implies that if the average goal-scoring rate is 1.4 goals per game, the
probability of scoring 4 goals in a game is about 4%.

We'll use the following function to make a Pmf that represents a Poisson distribution:

from empiricaldist import Pmf

def make_poisson_pmf(lam, qs):
"""Make a Pmf of a Poisson distribution. """
ps = poisson(lam) . pmf (qs)
pmf = Pmf(ps, qs)
pmf.normalize()
return pmf

make_poisson_pmf takes as parameters the goal-scoring rate, lam, and an array of
quantities, qs, where it should evaluate the Poisson PMF. It returns a Pmf object.

<!-- PageFooter="Chapter 8: Poisson Processes" -->
<!-- PageNumber="100" -->
<!-- PageBreak -->

For example, here's the distribution of goals scored for $l a m = 1 . 4 ,$ computed for values
of $k$ from 0 to 9:

import numpy as np

$l a m = 1 . 4$
goals = np. arange(10)
pmf_goals = make_poisson_pmf(lam, goals)

And here's what it looks like:


<figure>

Distribution of goals scored

0.35

Poisson distribution with $\lambda = 1 . 4$

0.30

0.25

$0 . 2 0$

0.15

0.10

0.05

0.00

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

Number of goals

</figure>


The most likely outcomes are 0, 1, and 2; higher values are possible but increasingly
unlikely. Values above 7 are negligible. This distribution shows that $\mathrm { i f }$ we know the
goal-scoring rate, we can predict the number of goals.

Now let's turn it around: given a number of goals, what can we say about the goal-
scoring rate?

To answer that, we need to think about the prior distribution of lam, which represents
the range of possible values and their probabilities before we see the score.


## The Gamma Distribution

If you have ever seen a soccer game, you have some information about lam. In most
games, teams score a few goals each. In rare cases, a team might score more than 5
goals, but they almost never score more than 10.

Using data from previous World Cups, I estimate that each team scores about 1.4
goals per game, on average. So I'll set the mean of lam to be 1.4.

<!-- PageFooter="The Gamma Distribution" -->
<!-- PageNumber="101" -->
<!-- PageBreak -->

For a good team against a bad one, we expect lam to be higher; for a bad team against
a good one, we expect it to be lower.

To model the distribution of goal-scoring rates, I'll use a gamma distribution, which I
chose because:

1\. The goal scoring rate is continuous and non-negative, and the gamma distribu-
tion is appropriate for this kind of quantity.

2\. The gamma distribution has only one parameter, alpha, which is the mean. So
it's easy to construct a gamma distribution with the mean we want.

3\. As we'll see, the shape of the gamma distribution is a reasonable choice, given
what we know about soccer.

And there's one more reason, which I will reveal in Chapter 18.

SciPy provides gamma, which creates an object that represents a gamma distribution.
And the gamma object provides provides pdf, which evaluates the probability density
function (PDF) of the gamma distribution.

Here's how we use it:

from scipy. stats import gamma

$a l p h a = 1 . 4$
qs = np. linspace(0, 10, 101)
ps = gamma(alpha) . pdf (qs)

The parameter, alpha, is the mean of the distribution. The qs are possible values of
lam between 0 and 10. The ps are probability densities, which we can think of as
unnormalized probabilities.

To normalize them, we can put them in a Pmf and call normalize:

from empiricaldist import Pmf

prior = Pmf(ps, qs)
prior.normalize()

<!-- PageFooter="Chapter 8: Poisson Processes" -->
<!-- PageNumber="102" -->
<!-- PageBreak -->

The result is a discrete approximation of a gamma distribution. Here's what it looks
like:


<figure>

$\lambda$

0.05

prior

0.04

PMF

0.03

0.02

0.01

0.00

0

2

8

10

$\begin{array}{} { 4 } \\ { \text { Goal scoring rate \left(lam\right) } } \end{array}$

</figure>


This distribution represents our prior knowledge about goal scoring: lam is usually
less than 2, occasionally as high as 6, and seldom higher than that.

As usual, reasonable people could disagree about the details of the prior, but this is
good enough to get started. Let's do an update.


## The Update

Suppose you are given the goal-scoring rate, $\lambda ,$ and asked to compute the probability
of scoring a number of goals, $k .$ That is precisely the question we answered by com-
puting the Poisson PMF.

For example, if $\lambda$ is 1.4, the probability of scoring 4 goals in a game is:

$$\tan = 1 . 4$$

$k = 4$
poisson(lam). pmf (4)
0.039471954028253146

Now suppose we are have an array of possible values for $\lambda$ we can compute the likeli-
hood of the data for each hypothetical value of lam, like this:

$$l a m s = p r i o r . q s$$

$k = 4$
likelihood = poisson(lams) . pmf (k)

And that's all we need to do the update. To get the posterior distribution, we multiply
the prior by the likelihoods we just computed and normalize the result.

<!-- PageFooter="The Update" -->
<!-- PageNumber="103" -->
<!-- PageBreak -->

The following function encapsulates these steps:

def update_poisson(pmf, data):
"""Update Pmf with a Poisson likelihood. """
$k = d a t a$
lams = pmf. qs
likelihood = poisson(lams) . pmf (k)
pmf *= likelihood
pmf.normalize()

The first parameter is the prior; the second is the number of goals.

In the example, France scored 4 goals, so I'll make a copy of the prior and update it
with the data:

$$f r a n c e = p r i o r . c o p y \left( \right)$$

update_poisson(france, 4)

Here's what the posterior distribution looks like, along with the prior:


<figure>
<figcaption>Posterior distribution for France</figcaption>

0.05

prior

France posterior

0.04

PMF

0.03

0.02

0.01

0.00

0

2

4

6

8

10

$\left( \mathrm { l a m } \right)$

</figure>


The data, $k = 4 ,$ makes us think higher values of lam are more likely and lower values
are less likely. So the posterior distribution is shifted to the right.

Let's do the same for Croatia:

$$c r o a t i a = p r i o r . c o p y \left( \right)$$

update_poisson(croatia, 2)

And here are the results:

<!-- PageFooter="Chapter 8: Poisson Processes" -->
<!-- PageNumber="104" -->
<!-- PageBreak -->


<figure>

Posterior distribution for Croatia

0.05

prior

Croatia posterior

0.04

$\sum _ { n = 1 } ^ { 1 1 }$

0.03

0.02

0.01

0.00

0

2

4

6

8

10

Goal scoring rate (lam)

</figure>


Here are the posterior means for these distributions:

print(croatia.mean(), france.mean())

$$1 . 6 9 9 9 7 6 5 8 6 6 7 5 5 2 2 5 \quad 2 . 6 9 9 7 7 2 3 9 3 3 4 2 3 0 8$$

The mean of the prior distribution is about 1.4. After Croatia scores 2 goals, their
posterior mean is 1.7, which is near the midpoint of the prior and the data. Likewise
after France scores 4 goals, their posterior mean is 2.7.

These results are typical of a Bayesian update: the location of the posterior distribu-
tion is a compromise between the prior and the data.


## Probability of Superiority

Now that we have a posterior distribution for each team, we can answer the first
question: How confident should we be that France is the better team?

In the model, "better" means having a higher goal-scoring rate against the opponent.
We can use the posterior distributions to compute the probability that a random
value drawn from France's distribution exceeds a value drawn from Croatia's.

One way to do that is to enumerate all pairs of values from the two distributions,
adding up the total probability that one value exceeds the other:

def prob_gt(pmf1, pmf2):
"""Compute the probability of superiority. """
total = 0
for q1, p1 in pmf1. items():
for q2, p2 in pmf2. items():
if q1 > q2:
total += p1 * p2
return total

<!-- PageFooter="Probability of Superiority" -->
<!-- PageNumber="105" -->
<!-- PageBreak -->

This is similar to the method we use in "Addends" on page 73 to compute the distri-
bution of a sum. Here's how we use it:

prob_gt(france, croatia)

0.7499366290930155

Pmf provides a function that does the same thing:

Pmf. $p r o b \_ g t \left( f r a n c e , \right.$ croatia)

0.7499366290930174

The results are slightly different because Pmf. prob_gt uses array operators rather
than for loops.

Either way, the result is close to 75%. So, on the basis of one game, we have moderate
confidence that France is actually the better team.

Of course, we should remember that this result is based on the assumption that the
goal-scoring rate is constant. In reality, if a team is down by one goal, they might play
more aggressively toward the end of the game, making them more likely to score, but
also more likely to give up an additional goal.

As always, the results are only as good as the model.


## Predicting the Rematch

Now we can take on the second question: If the same teams played again, what is the
chance Croatia would win? To answer this question, we'll generate the "posterior pre-
dictive distribution", which is the number of goals we expect a team to score.

If we knew the goal-scoring rate, lam, the distribution of goals would be a Poisson
distribution with parameter lam. Since we don't know lam, the distribution of goals is
a mixture of a Poisson distributions with different values of lam.

First I'll generate a sequence of Pmf objects, one for each value of lam:

$$\mathrm { p r i f } _ { - } \mathrm { s e q } = \left[ \mathrm { m a k e } \_ \mathrm { p o i s s o n } \_ \mathrm { p m f } \left( \mathrm { l a m } , \mathrm { g o a l s } \right) \right.$$
for lam in prior.qs]

The following figure shows what these distributions look like for a few values of lam.

<!-- PageFooter="Chapter 8: Poisson Processes" -->
<!-- PageNumber="106" -->
<!-- PageBreak -->


<figure>

0.3

$\lambda = 1 . 0$

$\lambda = 2 . 0$

0.2

$\sum _ { n = 1 } ^ { 1 1 }$

0.2

$\sum _ { n = 1 } ^ { 1 1 }$

0.1

0.1

0.0

0.0

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

Number of goals

Number of goals

0.2

$\lambda = 3 . 0$

0.2

$\lambda = 4 . 0$

PMF

PMF

0.1

0.1

0.0

0.0

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

Number of goals

Number of goals

</figure>


The predictive distribution is a mixture of these Pmf objects, weighted with the poste-
rior probabilities. We can use make_mixture from "General Mixtures" on page 93 to
compute this mixture:


### from utils import make_mixture

pred_france = make_mixture(france, pmf_seq)

Here's the predictive distribution for the number of goals France would score in a
rematch:


<figure>
<figcaption>Posterior predictive distribution</figcaption>

France

0.20

0.15

$\sum _ { n = 1 } ^ { 4 }$

0.10

0.05

0.00

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

Number of goals

</figure>


This distribution represents two sources of uncertainty: we don't know the actual
value of lam, and even if we did, we would not know the number of goals in the next
game.

<!-- PageFooter="Predicting the Rematch" -->
<!-- PageNumber="107" -->
<!-- PageBreak -->

Here's the predictive distribution for Croatia:

$$\mathrm { p r e d } _ { - } \mathrm { c r o a t i a } = \mathrm { m a k e } _ { - } \mathrm { m i x t u r e } \left( \mathrm { c r o a t i a } , \mathrm { p m f } _ { - } \mathrm { s e q } \right)$$

We can use these distributions to compute the probability that France wins, loses, or
ties the rematch:

$$w i n = P m f . p r o b \_ g t \left( p r e d _ { - } f r a n c e , p r e d _ { - } c r o a t i a \right)$$

win

0.5703522415934519
lose = Pmf . prob_lt(pred_france, pred_croatia)
lose

0.26443376257235873

tie = Pmf. prob_eq(pred_france, pred_croatia)
tie

0.16521399583418947

Assuming that France wins half of the ties, their chance of winning the rematch is
about 65%:

$$w i n + t i e / 2$$

0.6529592395105466

This is a bit lower than their probability of superiority, which is 75%. And that makes
sense, because we are less certain about the outcome of a single game than we are
about the goal-scoring rates. Even if France is the better team, they might lose the
game.


## The Exponential Distribution

As an exercise at the end of this notebook, you'll have a chance to work on the follow-
ing variation on the World Cup Problem:

In the 2014 FIFA World Cup, Germany played Brazil in a semifinal match. Germany
scored after 11 minutes and again at the 23 minute mark. At that point in the match,
how many goals would you expect Germany to score after 90 minutes? What was the
probability that they would score 5 more goals (as, in fact, they did)?

In this version, notice that the data is not the number of goals in a fixed period of
time, but the time between goals.

To compute the likelihood of data like this, we can take advantage of the theory of
Poisson processes again. If each team has a constant goal-scoring rate, we expect the
time between goals to follow an exponential distribution.

If the goal-scoring rate is $\lambda ,$ the probability of seeing an interval between goals of $t$ is
proportional to the PDF of the exponential distribution:

<!-- PageFooter="Chapter 8: Poisson Processes" -->
<!-- PageNumber="108" -->
<!-- PageBreak -->

1 exp $\left( - \lambda t \right)$

Because $t$ is a continuous quantity, the value of this expression is not a probability; it
is a probability density. However, it is proportional to the probability of the data, so
we can use it as a likelihood in a Bayesian update.

SciPy provides expon, which creates an object that represents an exponential distribu-
tion. However, it does not take lam as a parameter in the way you might expect, which
makes it awkward to work with. Since the PDF of the exponential distribution is so
easy to evaluate, I'll use my own function:

def expo_pdf(t, lam):
"""Compute the PDF of the exponential distribution. """
return lam * np. exp(-lam * t)

To see what the exponential distribution looks like, let's assume again that lam is 1.4;
we can compute the distribution of t like this:

lam = 1.4
qs = np. linspace(0, 4, 101)
ps = expo_pdf(qs, lam)
pmf_time = Pmf(ps, qs)
pmf_time.normalize()
25.616650745459093

And here's what it looks like:


<figure>

Distribution of time between goals

exponential $w i t h \quad A = 1 . 4$

0.05

0.04

PMF

0.03

0.02

0.01

0.00

0.0

0.5

1.0

1.5

2.0

2.5

3.0

3.5

4.0

Time between goals (games)

</figure>


It is counterintuitive, but true, that the most likely time to score a goal is immediately.
After that, the probability of each successive interval is a little lower.

With a goal-scoring rate of 1.4, it is possible that a team will take more than one game
to score a goal, but it is unlikely that they will take more than two games.

<!-- PageFooter="The Exponential Distribution" -->
<!-- PageNumber="109" -->
<!-- PageBreak -->


### Summary

This chapter introduces three new distributions, so it can be hard to keep them
straight. Let's review:

· If a system satisfies the assumptions of a Poisson model, the number of events in
a period of time follows a Poisson distribution, which is a discrete distribution
with integer quantities from 0 to infinity. In practice, we can usually ignore low-
probability quantities above a finite limit.

· Also under the Poisson model, the interval between events follows an exponen-
tial distribution, which is a continuous distribution with quantities from 0 to
infinity. Because it is continuous, it is described by a probability density function
(PDF) rather than a probability mass function (PMF). But when we use an expo-
nential distribution to compute the likelihood of the data, we can treat densities
as unnormalized probabilities.

· The Poisson and exponential distributions are parameterized by an event rate,
denoted $\lambda$ or lam.

· For the prior distribution of $\lambda ,$ I used a gamma distribution, which is a continu-
ous distribution with quantities from 0 to infinity, but I approximated it with a
discrete, bounded PMF. The gamma distribution has one parameter, denoted $\alpha$
or alpha, which is also its mean.

I chose the gamma distribution because the shape is consistent with our background
knowledge about goal-scoring rates. There are other distributions we could have
used; however, we will see in Chapter 18 that the gamma distribution can be a partic-
ularly good choice.

But we have a few things to do before we get there, starting with these exercises.


## Exercises


### Exercise 8-1.

Let's finish the exercise we started:

In the 2014 FIFA World Cup, Germany played Brazil in a semifinal match. Germany
scored after 11 minutes and again at the 23 minute mark. At that point in the match,
how many goals would you expect Germany to score after 90 minutes? What was the
probability that they would score 5 more goals (as, in fact, they did)?

<!-- PageFooter="Chapter 8: Poisson Processes" -->
<!-- PageNumber="110" -->
<!-- PageBreak -->

Here are the steps I recommend:

1\. Starting with the same gamma prior we used in the previous problem, compute
the likelihood of scoring a goal after 11 minutes for each possible value of lam.
Don't forget to convert all times into games rather than minutes.

2\. Compute the posterior distribution of lam for Germany after the first goal.

3\. Compute the $\mathrm { l i k e l i h o o d }$ of scoring another goal after 12 more minutes and $d \alpha$
another update. Plot the prior, posterior after one goal, and posterior after two
goals.

4\. Compute the posterior predictive distribution of goals Germany might score
during the remaining time in the game, 90-23 minutes. Note: You will have to
think about how to generate predicted goals for a fraction of a game.

5\. Compute the probability of scoring 5 or more goals during the remaining time.


### Exercise 8-2.

Returning to the first version of the World Cup Problem, suppose France and Croatia
play a rematch. What is the probability that France scores first?


### Exercise 8-3.

In the 2010-11 National Hockey League (NHL) Finals, my beloved Boston Bruins
played a best-of-seven championship series against the despised Vancouver Canucks.
Boston lost the first two games 0-1 and 2-3, then won the next two games 8-1 and
4-0. At this point in the series, what is the probability that Boston will win the next
game, and what is their probability of winning the championship?

To choose a prior distribution, I got some statistics from http://www.nhl.com, specifi-
cally the average goals per game for each team in the 2010-11 season. The distribu-
tion is well modeled by a gamma distribution with mean 2.8.

In what ways do you think the outcome of these games might violate the assumptions
of the Poisson model? How would these violations affect your predictions?

<!-- PageFooter="Exercises" -->
<!-- PageNumber="111" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 9" -->


# Decision Analysis

This chapter presents a problem inspired by the game show The Price is Right. It is a
silly example, but it demonstrates a useful process called Bayesian decision analysis.

As in previous examples, we'll use data and prior distribution to compute a posterior
distribution; then we'll use the posterior distribution to choose an optimal strategy in
a game that involves bidding.

As part of the solution, we will use kernel density estimation (KDE) to estimate the
prior distribution, and a normal distribution to compute the likelihood of the data.

And at the end of the chapter, I pose a related problem you can solve as an exercise.


# The Price Is Right Problem

On November 1, 2007, contestants named Letia and Nathaniel appeared on The Price
is Right, an American television game show. They competed in a game called "The
Showcase", where the objective is to guess the price of a collection of prizes. The con-
testant who comes closest to the actual price, without going over, wins the prizes.

Nathaniel went first. His showcase included a dishwasher, a wine cabinet, a laptop
computer, and a car. He bid $26,000.

Letia's showcase included a pinball machine, a video arcade game, a pool table, and a
cruise of the Bahamas. She bid $21,500. The actual price of Nathaniel's showcase was
$25,347. His bid was too high, so he lost. The actual price of Letia's showcase was
$21,578.

She was only off by $78, so she won her showcase and, because her bid was off by less
than 250, she also won Nathaniel's showcase.

For a Bayesian thinker, this scenario suggests several questions:

<!-- PageNumber="113" -->
<!-- PageBreak -->

1\. Before seeing the prizes, what prior beliefs should the contestants have about the
price of the showcase?

2\. After seeing the prizes, how should the contestants update those beliefs?

3\. Based on the posterior distribution, what should the contestants bid?

The third question demonstrates a common use of Bayesian methods: decision
analysis.

This problem is inspired by an example in Cameron Davidson-Pilon's book, Probabl-
istic Programming and Bayesian Methods for Hackers.


## The Prior

To choose a prior distribution of prices, we can take advantage of data from previous
episodes. Fortunately, fans of the show keep detailed records.

For this example, I downloaded files containing the price of each showcase from the
2011 and 2012 seasons and the bids offered by the contestants.

The following function reads the data and cleans it up a little:

import pandas as pd

def read_data(filename) :
"""Read the showcase price data. """
df = pd.read_csv(filename, index_col=0, skiprows=[1])
return df . dropna() . transpose()

I'll read both files and concatenate them:

df2011 = read_data( ' showcases. 2011.csv' )
df2012 = read_data(' showcases. 2012. csv')

$$d f = p d . c o n c a t \left( \left[ d f 2 0 1 1 , d f 2 0 1 2 \right] , i g n o r e _ { - } i n d e x = T r u e \right)$$

Here's what the dataset looks like:

df.head(3)


<table>
<tr>
<th></th>
<th>Showcase 1</th>
<th>Showcase 2</th>
<th>Bid 1</th>
<th>Bid 2</th>
<th>Difference 1</th>
<th>Difference 2</th>
</tr>
<tr>
<td colspan="2">0 50969.0</td>
<td>45429.0</td>
<td>42000.0</td>
<td>34000.0</td>
<td>8969.0</td>
<td>11429.0</td>
</tr>
<tr>
<td colspan="2">1 21901.0</td>
<td>34061.0</td>
<td>14000.0</td>
<td>59900.0</td>
<td>7901.0</td>
<td>-25839.0</td>
</tr>
<tr>
<td colspan="2">2 32815.0</td>
<td>53186.0</td>
<td>32000.0</td>
<td>45000.0</td>
<td>815.0</td>
<td>8186.0</td>
</tr>
</table>


The first two columns, Showcase 1 and Showcase 2, are the values of the showcases
in dollars. The next two columns are the bids the contestants made. The last two $c o l -$
umns are the differences between the actual values and the bids.

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="114" -->
<!-- PageBreak -->


# Kernel Density Estimation

This dataset contains the prices for 313 previous showcases, which we can think of as
a sample from the population of possible prices.

We can use this sample to estimate the prior distribution of showcase prices. One way
to do that is kernel density estimation (KDE), which uses the sample to estimate a
smooth distribution. If you are not familiar with KDE, you can read about it online.

SciPy provides gaussian_kde, which takes a sample and returns an object that repre-
sents the estimated distribution.

The following function takes sample, makes a KDE, evaluates it at a given sequence of
quantities, qs, and returns the result as a normalized PMF.

from scipy.stats import gaussian_kde
from empiricaldist import Pmf

def kde_from_sample(sample, qs):
"""Make a kernel density estimate from a sample. """
$k d e = g a u s s i a n \_ k d e \left( s a m p l e \right)$
$p s = k d e \left( q s \right)$
$p \eta f = P m f \left( p s \right. ,$ qs)
pmf.normalize()
return pmf

We can use it to estimate the distribution of values for Showcase 1:

import numpy as np

qs = np. linspace(0, 80000, 81)
prior1 = kde_from_sample(df['Showcase 1'], qs)

Here's what it looks like:


<figure>

Prior distribution of showcase value

0.06

Prior 1

0.05

0.04

PMF

0.03

0.02

0.01

0.00

0

10000 20000 30000 40000 50000 60000 70000 80000
Showcase value ($)

</figure>


<!-- PageFooter="Kernel Density Estimation" -->
<!-- PageNumber="115" -->
<!-- PageBreak -->


## Exercise 9-1.

Use this function to make a Pmf that represents the prior distribution for Showcase 2,
and plot it.


# Distribution of Error

To update these priors, we have to answer these questions:

· What data should we consider and how should we quantify it?

· Can we compute a likelihood function? That is, for each hypothetical price, can
we compute the conditional likelihood of the data?

To answer these questions, I will model each contestant as a price-guessing instru-
ment with known error characteristics. In this model, when the contestant sees the
prizes, they guess the price of each prize and add up the prices. Let's call this total
guess.

Now the question we have to answer is, "If the actual price is price, what is the likeli-
hood that the contestant's guess would be guess?"

Equivalently, if we define error = guess - price, we can ask, "What is the likeli-
hood that the contestant's guess is off by error?"

To answer this question, I'll use the historical data again. For each showcase in the
dataset, let's look at the difference between the contestant's bid and the actual price:

$$= d f ^ { \prime } \left[ B ^ { \prime } i d ^ { \prime } 1 \right] - d f \left[ ^ { \prime } \text { Showcase } 1 ^ { \prime } \right]$$
$$\left. d i f f 2 = d f ^ { \prime } B i d 2 ^ { \prime } \right] - d f \left[ ^ { \prime } \text { showcase } 2 ^ { \prime } \right]$$

To visualize the distribution of these differences, we can use KDE again:

qs = np. linspace(-40000, 20000, 61)

$$\mathrm { k d e } _ { - } d i f f 1 = k d e _ { - } f r o n _ { - } s a m p l e \left( s a m p l e _ { - } d i f f _ { 1 } , q s \right)$$
$$\mathrm { k d e } _ { - } d i f f _ { 2 } = k d e _ { - } f r o m _ { - } s a m p l e \left( s a m p l e _ { - } d i f f _ { 2 } , q s \right)$$

Here's what these distributions look like:

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="116" -->
<!-- PageBreak -->


<figure>

Difference between bid and actual value

0.07

Diff 1

0.06

$D i f f \quad 2$

0.05

0.04

$\sum _ { n = 1 } ^ { 1 1 }$

0.03

0.02

0.01

0.00

-40000

-30000

-20000

-10000

0

10000

20000

Difference in value ($)

</figure>


It looks like the bids are too low more often than too high, which makes sense.
Remember that under the rules of the game, you lose if you overbid, so contestants
probably underbid to some degree deliberately.

For example, if they guess that the value of the showcase is $40,000, they might bid
$36,000 to avoid going over.

It looks like these distributions are well modeled by a normal distribution, so we can
summarize them with their mean and standard deviation.

For example, here is the mean and standard deviation of Diff for Player 1:

$$\mathrm { m e a n } _ { - } d i f f 1 = \mathrm { s a m p l e } _ { - } d i f f _ { 1 } . \mathrm { m e a n } \left( \right)$$
$$\mathrm { s t d } _ { - } d i f f _ { 1 } = s a m p l e _ { - } d i f f _ { 1 } . s t d \left( \right)$$

print(mean_diff1, std_diff1)

-4116.3961661341855 6899.909806377117

Now we can use these differences to model the contestant's distribution of errors.
This step is a little tricky because we don't actually know the contestant's guesses; we
only know what they bid.

So we have to make some assumptions:

· I'll assume that contestants underbid because they are being strategic, and that on
average their guesses are accurate. In other words, the mean of their errors is 0.

· But I'll assume that the spread of the differences reflects the actual spread of their
errors. So, I'll use the standard deviation of the differences as the standard devia-
tion of their errors.

<!-- PageFooter="Distribution of Error" -->
<!-- PageNumber="117" -->
<!-- PageBreak -->

Based on these assumptions, I'll make a normal distribution with parameters 0 and
std_diff1. SciPy provides an object called norm that represents a normal distribution
with the given mean and standard deviation:

from scipy. stats import norm

error_dist1 = norm(0, std_diff1)

The result is an object that provides pdf, which evaluates the probability density
function of the normal distribution.

For example, here is the probability density of $e r r o r = - \quad 1 0 0 ,$ based on the distribution
of errors for Player 1:

error $= - \quad 1 0 0$
error_dist1.pdf(error)
5.781240564008691e-05

By itself, this number doesn't mean very much, because probability densities are not
probabilities. But they are proportional to probabilities, so we can use them as likeli-
hoods in a Bayesian update, as we'll see in the next section.


# Update

Suppose you are Player 1. You see the prizes in your showcase and your guess for the
total price is $23,000.

From your guess I will subtract away each hypothetical price in the prior distribution;
the result is your error under each hypothesis.

guess1 = 23000
$$\mathrm { e r r o r 1 } = \mathrm { g u e s s 1 } - \mathrm { p r i o r 1 } . \mathrm { q s }$$

Now suppose we know, based on past performance, that your estimation error is well
modeled by error_dist1. Under that assumption we can compute the likelihood of
your error under each hypothesis:

likelihood1 = error_dist1.pdf(error1)

The result is an array of likelihoods, which we can use to update the prior:

posterior1 = prior1 * likelihood1
posterior1.normalize()

Here's what the posterior distribution looks like:

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="118" -->
<!-- PageBreak -->


<figure>

Prior and posterior distribution of showcase value

Prior 1

0.08

Posterior 1

0.06

$\sum _ { n = 1 } ^ { 1 1 }$

0.04

0.02

0.00

0

10000

20000

30000

40000

50000

60000

70000

80000

Showcase value ($)

</figure>


Because your initial guess is in the lower end of the range, the posterior distribution
has shifted to the left. We can compute the posterior mean to see by how much:

prior1.mean(), posterior1.mean()

(30299.488817891375, 26192.024002392536)

Before you saw the prizes, you expected to see a showcase with a value close to
$30,000. After making a guess of $23,000, you updated the prior distribution. Based
on the combination of the prior and your guess, you now expect the actual price to be
about $26,000.


## Exercise 9-2.

Now suppose you are Player 2. When you see your showcase, you guess that the total
price is $38,000.

Use diff2 to construct a normal distribution that represents the distribution of your
estimation errors.

Compute the likelihood of your guess for each actual price and use it to update
prior2.

Plot the posterior distribution and compute the posterior mean. Based on the prior
and your guess, what do you expect the actual price of the showcase to be?

<!-- PageFooter="Update" -->
<!-- PageNumber="119" -->
<!-- PageBreak -->


# Probability of Winning

Now that we have a posterior distribution for each player, let's think about strategy.

First, from the point of view of Player 1, let's compute the probability that Player 2
overbids. To keep it simple, I'll use only the performance of past players, ignoring the
value of the showcase.

The following function takes a sequence of past bids and returns the fraction that
overbid.

def prob_overbid(sample_diff) :
"""Compute the probability of an overbid. """
return np. mean(sample_diff > 0)

Here's an estimate for the probability that Player 2 overbids:

prob_overbid(sample_diff2)
0.29073482428115016

Now suppose Player 1 underbids by $5,000. What is the probability that Player 2
underbids by more?

The following function uses past performance to estimate the probability that a player
underbids by more than a given amount, diff:

def prob_worse_than(diff, sample_diff):
"""Probability opponent diff is worse than given diff. """
return np. mean(sample_diff < diff)

Here's the probability that Player 2 underbids by more than $5,000:

prob_worse_than(-5000, sample_diff2)
0.38338658146964855

And here's the probability they underbid by more than $10,000:

prob_worse_than(-10000, sample_diff2)
0.14376996805111822

We can combine these functions to compute the probability that Player 1 wins, given
the difference between their bid and the actual price:

def compute_prob_win(diff, sample_diff):
"""Probability of winning for a given diff. """
\# if you overbid you lose
if diff > 0:
return 0
\# if the opponent overbids, you win
p1 = prob_overbid(sample_diff)

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="120" -->
<!-- PageBreak -->

\# or if their bid is worse than yours, you win
p2 = prob_worse_than(diff, sample_diff)

\# p1 and p2 are mutually exclusive, so we can add them
return p1 + p2

Here's the probability that you win, given that you underbid by $5,000:

compute_prob_win(-5000, sample_diff2)
0.6741214057507987

Now let's look at the probability of winning for a range of possible differences:

XS = np. linspace(-30000, 5000, 121)
ys = [compute_prob_win(x, sample_diff2)
for x in xs]

Here's what it looks like:


<figure>

Player 1

1.0

0.8

Probability of winning

0.6

0.4

0.2

0.0

-30000 -25000 -20000 -15000 -10000 -5000

0

5000

Difference between bid and actual price ($)

</figure>


If you underbid by $30,000, the chance of winning is about 30%, which is mostly the
chance your opponent overbids.

As your bids gets closer to the actual price, your chance of winning approaches 1.
And, of course, if you overbid, you lose (even if your opponent also overbids).


## Exercise 9-3.

Run the same analysis from the point of view of Player 2. Using the sample of differ-
ences from Player 1, compute:

1\. The probability that Player 1 overbids.

2\. The probability that Player 1 underbids by more than $5,000.

<!-- PageFooter="Probability of Winning" -->
<!-- PageNumber="121" -->
<!-- PageBreak -->

3\. The probability that Player 2 wins, given that they underbid by $5,000.

Then plot the probability that Player 2 wins for a range of possible differences
between their bid and the actual price.


# Decision Analysis

In the previous section we computed the probability of winning, given that we have
underbid by a particular amount.

In reality the contestants don't know how much they have underbid by, because they
don't know the actual price.

But they do have a posterior distribution that represents their beliefs about the actual
price, and they can use that to estimate their probability of winning with a given bid.

The following function takes a possible bid, a posterior distribution of actual prices,
and a sample of differences for the opponent.

It loops through the hypothetical prices in the posterior distribution and, for each
price:

1\. Computes the difference between the bid and the hypothetical price,

2\. Computes the probability that the player wins, given that difference, and

3\. Adds up the weighted sum of the probabilities, where the weights are the proba-
bilities in the posterior distribution.

def total_prob_win(bid, posterior, sample_diff):
"""Computes the total probability of winning with a given bid.

bid: your bid
posterior: Pmf of showcase value
sample_diff: sequence of differences for the opponent

returns: probability of winning

total = 0
for price, prob in posterior. items():
diff = bid - price
total += prob * compute_prob_win(diff, sample_diff)
return total

This loop implements the law of total probability:

$$P \left( w i n \right) = \sum _ { p r i c e } P \left( p r i c e \right) P \left( w i n | p r i c e \right)$$

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="122" -->
<!-- PageBreak -->

Here's the probability that Player 1 wins, based on a bid of $25,000 and the posterior
distribution posterior1:

total_prob_win(25000, posterior1, sample_diff2)
0.4842210945439812

Now we can loop through a series of possible bids and compute the probability of
winning for each one:

$$b i d s = p o s t e r i o r 1 . q s$$

$$= \left[ \text { total } _ { - } \right] \text { prob } _ { - }$$

for bid in bids]

$\mathrm { p r o b } _ { - } \mathrm { w i t n } _ { - } \mathrm { s e r } i \mathrm { e s } = \mathrm { p d } . \mathrm { S e r } i \mathrm { e s } \left( \mathrm { p r o b s } \right) ,$ index=bids)

Here are the results:


<figure>

Optimal bid: probability of winning

0.6

Player 1

0.5

Probability of winning

0.4

0.3

0.2

0.1

0.0

0

10000

20000

30000

40000

50000

60000

70000

80000

Bid ($)

</figure>


And here's the bid that maximizes Player 1's chance of winning:

prob_win_series. idxmax()
21000.0
prob_win_series.max()
0.6136807192359474

Recall that your guess was $23,000. Using your guess to compute the posterior distri-
bution, the posterior mean is about $26,000. But the bid that maximizes your chance
of winning is $21,000.

<!-- PageFooter="Decision Analysis" -->
<!-- PageNumber="123" -->
<!-- PageBreak -->


## Exercise 9-4.

Do the same analysis for Player 2.


# Maximizing Expected Gain

In the previous section we computed the bid that maximizes your chance of winning.
And if that's your goal, the bid we computed is optimal.

But winning isn't everything. Remember that if your bid is off by $250 or less, you
win both showcases. So it might be a good idea to increase your bid a little: it increa-
ses the chance you overbid and lose, but it also increases the chance of winning both
showcases.

Let's see how that works out. The following function computes how much you will
win, on average, given your bid, the actual price, and a sample of errors for your
opponent.

def compute_gain(bid, price, sample_diff):
"""Compute expected gain given a bid and actual price. """
diff = bid - price
prob = compute_prob_win(diff, sample_diff)

\# if you are within 250 dollars, you win both showcases
if -250 <= diff <= 0:
return 2 * price * prob
else:
return price * prob

For example, if the actual price is $35,000 and you bid $30,000, you will win about
$23,600 worth of prizes on average, taking into account your probability of losing,
winning one showcase, or winning both.

compute_gain(30000, 35000, sample_diff2)
23594.249201277955

In reality we don't know the actual price, but we have a posterior distribution that
represents what we know about it. By averaging over the prices and probabilities in
the posterior distribution, we can compute the expected gain for a particular bid.

In this context, "expected" means the average over the possible showcase values,
weighted by their probabilities.

def expected_gain(bid, posterior, sample_diff):
"""Compute the expected gain of a given bid. """
total = 0
for price, prob in posterior. items():
total += prob * compute_gain(bid, price, sample_diff)
return total

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="124" -->
<!-- PageBreak -->

For the posterior we computed earlier, based on a guess of $23,000, the expected gain
for a bid of $21,000 is about $16,900:

expected_gain(21000, posterior1, sample_diff2)
16923.59933856512

But can we do any better?

To find out, we can loop through a range of bids and find the one that maximizes
expected gain:

bids = posterior1.qs
gains = [expected_gain(bid, posterior1, sample_diff2) for bid in bids]
expected_gain_series = pd. Series(gains, index=bids)

Here are the results:


<figure>

Optimal bid: expected gain

17500

Player 1

15000

Expected gain ($)

12500

10000

7500

5000

2500

0

0

10000 20000 30000 40000 50000 60000 70000 80000
Bid ($)

</figure>


Here is the optimal bid:

expected_gain_series. idxmax()
22000.0

With that bid, the expected gain is about $17,400:

expected_gain_series.max()
17384.899584430797

Recall that your initial guess was $23,000. The bid that maximizes the chance of win-
ning is $21,000. And the bid that maximizes your expected gain is $22,000.

<!-- PageFooter="Maximizing Expected Gain" -->
<!-- PageNumber="125" -->
<!-- PageBreak -->


## Exercise 9-5.

Do the same analysis for Player 2.


# Summary

There's a lot going on this this chapter, so let's review the steps:

1\. First we used KDE and data from past shows to estimate prior distributions for
the values of the showcases.

2\. Then we used bids from past shows to model the distribution of errors as a nor-
mal distribution.

3\. We did a Bayesian update using the distribution of errors to compute the likeli-
hood of the data.

4\. We used the posterior distribution for the value of the showcase to compute the
probability of winning for each possible bid, and identified the bid that maximi-
zes the chance of winning.

5\. Finally, we used probability of winning to compute the expected gain for each
possible bid, and identified the bid that maximizes expected gain.

Incidentally, this example demonstrates the hazard of using the word "optimal"
without specifying what you are optimizing. The bid that maximizes the chance of
winning is not generally the same as the bid that maximizes expected gain.


# Discussion

When people discuss the pros and cons of Bayesian estimation, as contrasted with
classical methods sometimes called "frequentist", they often claim that in many cases
Bayesian methods and frequentist methods produce the same results.

In my opinion, this claim is mistaken because Bayesian and frequentist method pro-
duce different kinds of results:

· The result of frequentist methods is usually a single value that is considered to be
the best estimate (by one of several criteria) or an interval that quantifies the pre-
cision of the estimate.

· The result of Bayesian methods is a posterior distribution that represents all pos-
sible outcomes and their probabilities.

Granted, you can use the posterior distribution to choose a "best" estimate or com-
pute an interval. And in that case the result might be the same as the frequentist
estimate.

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="126" -->
<!-- PageBreak -->

But doing so discards useful information and, in my opinion, eliminates the primary
benefit of Bayesian methods: the posterior distribution is more useful than a single
estimate, or even an interval.

The example in this chapter demonstrates the point. Using the entire posterior distri-
bution, we can compute the bid that maximizes the probability of winning, or the bid
that maximizes expected gain, even if the rules for computing the gain are compli-
cated (and nonlinear).

With a single estimate or an interval, we can't do that, even if they are "optimal" in
some sense. In general, frequentist estimation provides little guidance for decision-
making.

If you hear someone say that Bayesian and frequentist methods produce the same
results, you can be confident that they don't understand Bayesian methods.


# More Exercises


## Exercise 9-6.

When I worked in Cambridge, Massachusetts, I usually took the subway to South Sta-
tion and then a commuter train home to Needham. Because the subway was unpre-
dictable, I left the office early enough that I could wait up to 15 minutes and still catch
the commuter train.

When I got to the subway stop, there were usually about 10 people waiting on the
platform. If there were fewer than that, I figured I just missed a train, so I expected to
wait a little longer than usual. And if there there more than that, I expected another
train soon.

But if there were a lot more than 10 passengers waiting, I inferred that something was
wrong, and I expected a long wait. In that case, I might leave and take a taxi.

We can use Bayesian decision analysis to quantify the analysis I did intuitively. Given
the number of passengers on the platform, how long should we expect to wait? And
when should we give up and take a taxi?

My analysis of this problem is in redline. ipynb, which is in the repository for this
book. Click here to run this notebook on Colab.


### Exercise 9-7.

This exercise is inspired by a true story. In 2001, I created Green Tea Press to publish
my books, starting with Think Python. I ordered 100 copies from a short-run printer
and made the book available for sale through a distributor.

<!-- PageFooter="More Exercises" -->
<!-- PageNumber="127" -->
<!-- PageBreak -->

After the first week, the distributor reported that 12 copies were sold. Based on that
report, I thought I would run out of copies in about 8 weeks, so I got ready to order
more. My printer offered me a discount if I ordered more than 1,000 copies, so I went
a little crazy and ordered 2,000.

A few days later, my mother called to tell me that her copies of the book had arrived.
Surprised, I asked how many. She said 10.

It turned out I had sold only two books to non-relatives. And it took a lot longer than
I expected to sell 2,000 copies.

The details of this story are unique, but the general problem is something almost
every retailer has to figure out. Based on past sales, how do you predict future sales?
And based on those predictions, how do you decide how much to order and when?

Often the cost of a bad decision is complicated. If you place a lot of small orders
rather than one big one, your costs are likely to be higher. If you run out of inventory,
you might lose customers. And if you order too much, you have to pay the various
costs of holding inventory.

So, let's solve a version of the problem I faced. It will take some work to set up the
problem; the details are in the notebook for this chapter.

<!-- PageFooter="Chapter 9: Decision Analysis" -->
<!-- PageNumber="128" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 10" -->


# Testing

In "The Euro Problem" on page 43 I presented a problem from David Mackay's book,
Information Theory, Inference, and Learning Algorithms:

A statistical statement appeared in The Guardian on Friday, January 4, 2002:

When spun on edge 250 times, a Belgian one-euro coin came up heads 140 times and tails
110. "It looks very suspicious to me," said Barry Blight, a statistics lecturer at the London
School of Economics. "If the coin were unbiased, the chance of getting a result as extreme
as that would be less than 7%."

But do these data give evidence that the coin is biased rather than fair?

We started to answer this question in Chapter 4; to review, our answer was based on
these modeling decisions:

· If you spin a coin on edge, there is some probability, x, that it will land heads up.

· The value of $x$ varies from one coin to the next, depending on how the coin is
balanced and possibly other factors.

Starting with a uniform prior distribution for x, we updated it with the given data,
140 heads and 110 tails. Then we used the posterior distribution to compute the most
likely value of $x ,$ the posterior mean, and a credible interval.

But we never really answered Mackay's question: "Do these data give evidence that
the coin is biased rather than fair?"

In this chapter, finally, we will.


## Estimation

Let's review the solution to the Euro Problem from "The Binomial Likelihood Func-
tion" on page 51. We started with a uniform prior:

<!-- PageNumber="129" -->
<!-- PageBreak -->

import numpy as np
from empiricaldist import Pmf

xs = np. linspace(0, 1, 101)
uniform = Pmf(1, xs)

And we used the binomial distribution to compute the probability of the data for
each possible value of x:

from scipy. stats import binom

k, $n = 1 4 0 ,$ 250
likelihood = binom.pmf(k, n, xs)

We computed the posterior distribution in the usual way:

posterior = uniform * likelihood
posterior.normalize()

And here's what it looks like:


<figure>

Posterior distribution of $x$

0.12

140 heads out of 250

0.10

Probability

0.08

0.06

0.04

0.02

0.00

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of heads $\left( x \right)$
☒

</figure>


Again, the posterior mean is about 0.56, with a 90% credible interval from 0.51 to
0.61:

print(posterior.mean(),
posterior.credible_interval(0.9))

0.5595238095238095 [0.51 0.61]

The prior mean was 0.5, and the posterior mean is 0.56, so it seems like the data is
evidence that the coin is biased.

But, it turns out not to be that simple.

<!-- PageFooter="Chapter 10: Testing" -->
<!-- PageNumber="130" -->
<!-- PageBreak -->


# Evidence

In "Oliver's Blood" on page 71, I said that data are considered evidence in favor of a
hypothesis, $A ,$ if the data are more likely under $A$ than under the alternative, $B ;$ that is
if

$$P \left( D | A \right) > P \left( D | B \right)$$

Furthermore, we can quantify the strength of the evidence by computing the ratio of
these likelihoods, which is known as the Bayes factor and often denoted $K :$

$$K = \frac { P \left( D | A \right) } { P \left( D | B \right) }$$

So, for the Euro Problem, let's consider two hypotheses, fair and biased, and com-
pute the likelihood of the data under each hypothesis.

If the coin is fair, the probability of heads is 50%, and we can compute the probability
of the data (140 heads out of 250 spins) using the binomial distribution:

$$k = 1 4 0$$
$$n = 2 5 0$$

like_fair = binom.pmf(k, n, p=0.5)
like_fair
0.008357181724917673

That's the probability of the data, given that the coin is fair.

But if the coin is biased, what's the probability of the data? That depends on what
"biased" means. If we know ahead of time that "biased" means the probability of
heads is 56%, we can use the binomial distribution again:

like_biased = binom.pmf(k, n, p=0.56)
like_biased
0.05077815959517949

Now we can compute the likelihood ratio:

$$K = l i k e _ { - } \text { biased } / l i k e _ { - }$$

6.075990838368387

The data are about 6 times more likely if the coin is biased, by this definition, than if
it is fair.

But we used the data to define the hypothesis, which seems like cheating. To be fair,
we should define "biased" before we see the data.

<!-- PageFooter="Evidence 131" -->
<!-- PageBreak -->


# Uniformly Distributed Bias

Suppose "biased" means that the probability of heads is anything except 50%, and all
other values are equally likely.

We can represent that definition by making a uniform distribution and removing
50%:

biased_uniform = uniform.copy()
biased_uniform[0.5] = 0
biased_uniform.normalize()

To compute the total probability of the data under this hypothesis, we compute the
conditional probability of the data for each value of x:

xs = biased_uniform. qs
likelihood = binom.pmf(k, n, xs)

Then multiply by the prior probabilities and add up the products:

like_uniform = np. sum(biased_uniform * likelihood)
like_uniform
0.0039004919277704267

So that's the probability of the data under the "biased uniform" hypothesis.

Now we can compute the likelihood ratio of the data under the fair and biased uni
form hypotheses:

$$K = l i k e _ { - } f a i r / l i k e _ { - } u n i f o r n$$

K

2.1425968518013954

The data are about two times more likely if the coin is fair than if it is biased, by this
definition of "biased".

To get a sense of how strong that evidence is, we can apply Bayes's rule. For example,
if the prior probability is 50% that the coin is biased, the prior odds are 1, so the pos-
terior odds are about 2.1 to 1 and the posterior probability is about 68%.

prior_odds = 1
posterior_odds = prior_odds * K
posterior_odds
2.1425968518013954

def prob(o):
return o / (o+1)
posterior_probability = prob(posterior_odds)
posterior_probability
0.6817918278551125

<!-- PageFooter="Chapter 10: Testing" -->
<!-- PageNumber="132" -->
<!-- PageBreak -->

Evidence that "moves the needle" from 50% to 68% is not very strong.

Now suppose "biased" doesn't mean every value of $x$ is equally likely. Maybe values
near 50% are more likely and values near the extremes are less likely. We could use a
triangle-shaped distribution to represent this alternative definition of "biased":

ramp_up = np . arange (50)
ramp_down = np. arange(50, -1, -1)
a = np. append(ramp_up, ramp_down)

$$= \mathrm { P n f } \left( a , x s , \text { nane } = ^ { \prime } t r i a n g l e ^ { \prime } \right)$$

triangle.normalize()

As we did with the uniform distribution, we can remove 50% as a possible value of x
(but it doesn't make much difference if we skip this detail):

$$b i a s e d \_ t r i a n g l e = t r i a n g l e . c o p y \left( \right)$$

biased_triangle[0.5] = 0
biased_triangle.normalize()

Here's what the triangle prior looks like, compared to the uniform prior:


<figure>

Uniform and triangle prior distributions

0.0200

\- uniform prior

0.0175

triangle prior

0.0150

0.0125

0.0100

$0 . 0 0 7 5$

0.0050

0.0025

0.0000

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of heads $\left( x \right)$
☒

</figure>


Exercise 10-1.

Now compute the total probability of the data under this definition of "biased" and
compute the Bayes factor, compared with the fair hypothesis. Is the data evidence that
the coin is biased?

<!-- PageFooter="Uniformly Distributed Bias" -->
<!-- PageNumber="133" -->
<!-- PageBreak -->


## Bayesian Hypothesis Testing

What we've done so far in this chapter is sometimes called "Bayesian hypothesis test-
$\mathrm { i n g } ^ { 2 }$ in contrast with statistical hypothesis testing.

In statistical hypothesis testing, we compute a p-value, which is hard to define con-
cisely, and use it to determine whether the results are "statistically significant", which
is also hard to define concisely.

The Bayesian alternative is to report the Bayes factor, $K ,$ which summarizes the
strength of the evidence in favor of one hypothesis or the other.

Some people think it is better to report $K$ than a posterior probability because $K$ does
not depend on a prior probability. But as we saw in this example, $K$ often depends on
a precise definition of the hypotheses, which can be just as controversial as a prior
probability.

In my opinion, Bayesian hypothesis testing is better because it measures the strength
of the evidence on a continuum, rather that trying to make a binary determination.
But it doesn't solve what I think is the fundamental problem, which is that hypothesis
testing is not asking the question we really care about.

To see why, suppose you test the coin and decide that it is biased after all. What can
you do with this answer? In my opinion, not much. In contrast, there are two ques-
tions I think are more useful (and therefore more meaningful):

· Prediction: Based on what we know about the coin, what should we expect to
happen in the future?

· Decision-making: Can we use those predictions to make better decisions?

At this point, we've seen a few examples of prediction. For example, in Chapter 8 we
used the posterior distribution of goal-scoring rates to predict the outcome of soccer
games.

And we've seen one previous example of decision analysis: In Chapter 9 we used the
distribution of prices to choose an optimal bid on The Price is Right.

So let's finish this chapter with another example of Bayesian decision analysis, the
Bayesian Bandit strategy.


# Bayesian Bandits

If you have ever been to a casino, you have probably seen a slot machine, which is
sometimes called a "one-armed bandit" because it has a handle like an arm and the
ability to take money like a bandit.

<!-- PageFooter="Chapter 10: Testing" -->
<!-- PageNumber="134" -->
<!-- PageBreak -->

The Bayesian Bandit strategy is named after one-armed bandits because it solves a
problem based on a simplified version of a slot machine.

Suppose that each time you play a slot machine, there is a fixed probability that you
win. And suppose that different machines give you different probabilities of winning,
but you don't know what the probabilities are.

Initially, you have the same prior belief about each of the machines, so you have no
reason to prefer one over the others. But if you play each machine a few times, you
can use the results to estimate the probabilities. And you can use the estimated proba-
bilities to decide which machine to play next.

At a high level, that's the Bayesian Bandit strategy. Now let's see the details.


# Prior Beliefs

If we know nothing about the probability of winning, we can start with a uniform
prior:

xs = np. linspace(0, 1, 101)

$$= \mathrm { P i f } \left( 1 , x s \right)$$
$$\mathrm { p r i o r } . \mathrm { n o r m a l i z e } \left( \right)$$

Supposing we are choosing from four slot machines, I'll make four copies of the
prior, one for each machine:

beliefs = [prior.copy() for i in $\left. r a n g e \left( 4 \right) \right]$

Here's what the prior distributions look $\mathrm { l i k } \epsilon$ for the four machines:

$\mathrm { p l o t } \left( \mathrm { b e l i e f s } \right)$


<figure>

Machine 0

Machine 1

PDF

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

Machine 2

Machine 3

PDF

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

Probability of winning

Probability of winning

</figure>


<!-- PageFooter="Prior Beliefs" -->
<!-- PageNumber="135" -->
<!-- PageBreak -->


# The Update

Each time we play a machine, we can use the outcome to update our beliefs. The fol-
lowing function does the update.

likelihood = {
'W' : XS,
'L': 1 - XS
}
def update(pmf, data):
"""Update the probability of winning. ""
pmf *= likelihood[data]
pmf.normalize()

This function updates the prior distribution in place. pmf is a Pmf that represents the
prior distribution of x, which is the probability of winning.

data is a string, either W if the outcome is a win or L if the outcome is a loss.

The likelihood of the data is either xs or 1-xs, depending on the outcome.

Suppose we choose a machine, play 10 times, and win once. We can compute the pos-
terior distribution of $x ,$ based on this outcome, like this:

bandit = prior.copy()

for outcome in 'WLLLLLLLLL':
update(bandit, outcome)

Here's what the posterior looks like:


<figure>

Posterior distribution, nine losses, one win

0.04

0.03

吕 0.02

0.01

0.00

0.0

0.2

0.4

0.6

0.8

1.0

Probability of winning

</figure>


<!-- PageFooter="Chapter 10: Testing" -->
<!-- PageNumber="136" -->
<!-- PageBreak -->


# Multiple Bandits

Now suppose we have four machines with these probabilities:

actual_probs = [0.10, 0.20, 0.30, 0.40]

Remember that as a player, we don't know these probabilities.

The following function takes the index of a machine, simulates playing the machine
once, and returns the outcome, Wor L.

from collections import Counter

\# count how many times we've played each machine
counter = Counter()

def play(i):
"""Play machine i.

i: index of the machine to play

returns: string 'W' or 'L'
counter [i] += 1
p = actual_probs [i]
if np.random.random() < p:
return 'W'
else:
return 'L'

counter is a Counter, which is a kind of dictionary we'll use to keep track of how
many times each machine is played.

Here's a test that plays each machine 10 times:

for i in range(4):
for _ in range(10):
outcome = play(i)
update(beliefs[i], outcome)

Each time through the inner loop, we play one machine and update our beliefs.

<!-- PageFooter="Multiple Bandits" -->
<!-- PageNumber="137" -->
<!-- PageBreak -->

Here's what our posterior beliefs look like:


<figure>

Machine 0

Machine 1

PDF

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

Machine 3

$\frac { u } { a }$

Machine 2

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

Probability of winning

Probability of winning

</figure>


Here are the actual probabilities, posterior means, and 90% credible intervals:


<table>
<tr>
<th></th>
<th>Actual P(win)</th>
<th>Posterior mean</th>
<th>Credible interval</th>
</tr>
<tr>
<td>0</td>
<td>0.1</td>
<td>0.250</td>
<td>[0.08, 0.47]</td>
</tr>
<tr>
<td>1</td>
<td>0.2</td>
<td>0.250</td>
<td>[0.08, 0.47]</td>
</tr>
<tr>
<td>2</td>
<td>0.3</td>
<td>0.500</td>
<td>[0.27, 0.73]</td>
</tr>
<tr>
<td>3</td>
<td>0.4</td>
<td>0.417</td>
<td>[0.2, 0.65]</td>
</tr>
</table>


We expect the credible intervals to contain the actual probabilities most of the time.


# Explore and Exploit

Based on these posterior distributions, which machine do you think we should play
next? One option would be to choose the machine with the highest posterior mean.

That would not be a bad idea, but it has a drawback: since we have only played each
machine a few times, the posterior distributions are wide and overlapping, which
means we are not sure which machine is the best; if we focus on one machine too
soon, we might choose the wrong machine and play it more than we should.

To avoid that problem, we could go to the other extreme and play all machines
equally until we are confident we have identified the best machine, and then play it
exclusively.

That's not a bad idea either, but it has a drawback: while we are gathering data, we are
not making good use of it; until we're sure which machine is the best, we are playing
the others more than we should.

<!-- PageFooter="Chapter 10: Testing" -->
<!-- PageNumber="138" -->
<!-- PageBreak -->

The Bayesian Bandits strategy avoids both drawbacks by gathering and using data at
the same time. In other words, it balances exploration and exploitation.

The kernel of the idea is called Thompson sampling: when we choose a machine, we
choose at random so that the probability of choosing each machine is proportional to
the probability that it is the best.

Given the posterior distributions, we can compute the "probability of superiority" for
each machine.

Here's one way to do it. We can draw a sample of 1,000 values from each posterior
distribution, like this:

$$s a m p l e s = n p . a r r a y \left( \left[ b . c h o i c e \left( 1 0 0 0 \right) \right. \right.$$
for b in beliefs])

samples. shape
(4, 1000)

The result has 4 rows and 1,000 columns. We can use argmax to find the index of the
largest value in each column:

indices = np. argmax(samples, axis=0)
indices. shape

(1000,)

The Pmf of these indices is the fraction of times each machine yielded the highest
values:

$$\mathrm { p m f } = \mathrm { P n f } . \mathrm { f r o m } _ { - } \mathrm { s e q } \left( i \mathrm { n d i c e s } \right)$$

probs

0
0.048

1
0.043

2
0.625

3
0.284

These fractions approximate the probability of superiority for each machine. So we
could choose the next machine by choosing a value from this Pmf.

pmf.choice()

1

But that's a lot of work to choose a single value, and it's not really necessary, because
there's a shortcut.

<!-- PageFooter="Explore and Exploit" -->
<!-- PageNumber="139" -->
<!-- PageBreak -->

If we draw a single random value from each posterior distribution and select the
machine that yields the highest value, it turns out that we'll select each machine in
proportion to its probability of superiority.

That's what the following function does.

def choose(beliefs) :
"""Use Thompson sampling to choose a machine.

Draws a single sample from each distribution.

returns: index of the machine that $\mathrm { y i e l d e d }$ the highest value
ps = [b. choice() for b in beliefs]
return np . argmax (ps)

This function chooses one value from the posterior distribution of each machine and
then uses argmax to find the index of the machine that yielded the highest value.

Here's an example:

choose(beliefs)
3


# The Strategy

Putting it all together, the following function chooses a machine, plays once, and
updates beliefs:

def choose_play_update(beliefs) :
"""Choose a machine, play it, and update beliefs. """

\# choose a machine
machine = choose(beliefs)
\# play it
outcome = play(machine)
\# update beliefs
update(beliefs[machine], outcome)

To test it out, let's start again with a fresh set of beliefs and an empty Counter:

beliefs = [prior.copy() for i in range(4)]
counter = Counter()

<!-- PageFooter="Chapter 10: Testing" -->
<!-- PageNumber="140" -->
<!-- PageBreak -->

If we run the bandit algorithm 100 times, we can see how beliefs gets updated:

$$n u n _ { - } p l a y s = 1 0 0$$

for i in range(num_plays):
choose_play_update(beliefs)

$\mathrm { p l o t } \left( \mathrm { b e l i e f s } \right)$


<figure>

Machine 0

Machine 1

PDF

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

Machine 2

Machine 3

PDF

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

Probability of winning

Probability of winning

</figure>


The following table summarizes the results:


<table>
<tr>
<th></th>
<th>Actual P(win)</th>
<th>Posterior mean</th>
<th>Credible interval</th>
</tr>
<tr>
<td>0</td>
<td>0.1</td>
<td>0.107</td>
<td>[0.0, 0.31]</td>
</tr>
<tr>
<td>1</td>
<td>0.2</td>
<td>0.269</td>
<td>[0.14, 0.42]</td>
</tr>
<tr>
<td>2</td>
<td>0.3</td>
<td>0.293</td>
<td>[0.18, 0.41]</td>
</tr>
<tr>
<td>3</td>
<td>0.4</td>
<td>0.438</td>
<td>[0.3, 0.58]</td>
</tr>
</table>


The credible intervals usually contain the actual probabilities of winning. The esti-
mates are still rough, especially for the lower-probability machines. But that's a fea-
ture, not a bug: the goal is to play the high-probability machines most often. Making
the estimates more precise is a means to that end, but not an end itself.

More importantly, let's see how many times each machine got played:


<table>
<tr>
<th></th>
<th>Actual P(win)</th>
<th>Times played</th>
</tr>
<tr>
<td>0</td>
<td>0.1</td>
<td>7</td>
</tr>
<tr>
<td>1</td>
<td>0.2</td>
<td>24</td>
</tr>
<tr>
<td>2</td>
<td>0.3</td>
<td>39</td>
</tr>
<tr>
<td>3</td>
<td>0.4</td>
<td>30</td>
</tr>
</table>


<!-- PageFooter="The Strategy" -->
<!-- PageNumber="141" -->
<!-- PageBreak -->

If things go according to plan, the machines with higher probabilities should get
played more often.


## Summary

In this chapter we finally solved the Euro Problem, determining whether the data
support the hypothesis that the coin is fair or biased. We found that the answer
depends on how we define "biased". And we summarized the results using a Bayes
factor, which quantifies the strength of the evidence.

But the answer wasn't satisfying because, in my opinion, the question wasn't interest-
ing. Knowing whether the coin is biased is not useful unless it helps us make better
predictions and better decisions.

As an example of a more interesting question, we looked at the One-Armed Bandit
problem and a strategy for solving it, the Bayesian Bandit algorithm, which tries to
balance exploration and exploitation, that is, gathering more information and making
the best use of the information we have.

As an exercise, you'll have a chance to explore adaptive strategies for standardized
testing.

Bayesian bandits and adaptive testing are examples of Bayesian decision theory,
which is the idea of using a posterior distribution as part of a decision-making pro-
cess, often by choosing an action that minimizes the costs we expect on average (or
maximizes a benefit).

The strategy we used in "Maximizing Expected Gain" on page 124 to bid on The Price
is Right is another example.

These strategies demonstrate what I think is the biggest advantage of Bayesian meth-
ods over classical statistics. When we represent knowledge in the form of probability
distributions, Bayes's theorem tells us how to change our beliefs as we get more data,
and Bayesian decision theory tells us how to make that knowledge actionable.


## More Exercises


### Exercise 10-2.

Standardized tests like the SAT are often used as part of the admission process at col-
leges and universities. The goal of the SAT is to measure the academic preparation of
the test-takers; if it is accurate, their scores should reflect their actual ability in the
domain of the test.

Until recently, tests like the SAT were taken with paper and pencil, but now students
have the option of taking the test online. In the online format, it is possible for the

<!-- PageFooter="Chapter 10: Testing" -->
<!-- PageNumber="142" -->
<!-- PageBreak -->

test to be "adaptive", which means that it can choose each question based on respon-
ses to previous questions.

If a student gets the first few questions right, the test can challenge them with harder
questions. If they are struggling, it can give them easier questions. Adaptive testing
has the potential to be more "efficient", meaning that with the same number of ques-
tions an adaptive test could measure the ability of a tester more precisely.

To see whether this is true, we will develop a model of an adaptive test and quantify
the precision of its measurements.

Details of this exercise are in the notebook.

<!-- PageFooter="More Exercises" -->
<!-- PageNumber="143" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 11" -->


# Comparison

This chapter introduces joint distributions, which are an essential tool for working
with distributions of more than one variable.

We'll use them to solve a silly problem on our way to solving a real problem. The silly
problem is figuring out how tall two people are, given only that one is taller than the
other. The real problem is rating chess players (or participants in other kinds of com-
petition) based on the outcome of a game.

To construct joint distributions and compute likelihoods for these problems, we will
use outer products and similar operations. And that's where we'll start.


## Outer Operations

Many useful operations can be expressed as the "outer product" of two sequences, or
another kind of "outer" operation. Suppose you have sequences like $x$ and y:

$$x = \left[ 1 , 3 , 5 \right]$$ ☒

y = [2, 4]

The outer product of these sequences is an array that contains the product of every
pair of values, one from each sequence. There are several ways to compute outer
products, but the one I think is the most versatile is a "mesh grid".

NumPy provides a function called meshgrid that computes a mesh grid. If we give it
two sequences, it returns two arrays:

import numpy as np

X, Y = np.meshgrid(x, y)
☒

The first array contains copies of $x$ arranged in rows, where the number of rows is the
length of $y :$

<!-- PageNumber="145" -->
<!-- PageBreak -->

$X$
☒

array([[1, 3, 5],
[1, 3,5]])

The second array contains copies of $y$ arranged in columns, where the number of col-
umns is the length of $x :$

$\mathrm { Y }$

array([[2, 2, 2],
[4, 4,4]])

Because the two arrays are the same size, we can use them as operands for arithmetic
functions like multiplication:

X * Y
☒ ☒

array([[ 2, 6, 10],
[ 4, 12, 20]])

This is result is the outer product of x and $y .$ We can see that more clearly if we put it
in a DataFrame:

import pandas as pd

df = pd. DataFrame(X * Y, columns=x, index=y)
☒ ☒

df
1 3
5
2 2 6 10
4 4 12 20

The values from $x$ appear as column names; the values from $y$ appear as row labels.
Each element is the product of a value from $x$ and a value from $y$ y.

We can use mesh grids to compute other operations, like the outer sum, which is an
array that contains the sum of elements from $x$ and elements from $y :$

$X + Y$
☒

array([[3, 5, 7],
[5,7,9]])

We can also use comparison operators to compare elements from $\mathrm { X }$ with elements
from $y :$

$X > Y$
☒

array([[False, True, True],
[False, False, True]])

The result is an array of Boolean values.

<!-- PageFooter="Chapter 11: Comparison" -->
<!-- PageNumber="146" -->
<!-- PageBreak -->

It might not be obvious yet why these operations are useful, but we'll see examples
soon. With that, we are ready to take on a new Bayesian problem.


# How Tall Is A?

Suppose I choose two people from the population of adult males in the US; I'll call
them A and B. If we see that $A$ is taller than B, how tall is $A ?$

To answer this question:

1\. I'll use background information about the height of men in the US to form a
prior distribution of height,

2\. I'll construct a joint prior distribution of height for A and B (and I'll explain what
that is),

3\. Then I'll update the prior with the information that $\mathrm { A }$ is taller, and

4\. From the joint posterior distribution I'll extract the posterior distribution of
height for $A .$

In the US the average height of male adults is 178 cm and the standard deviation is
7.7 cm. The distribution is not exactly normal, because nothing in the real world is,
but the normal distribution is a pretty good model of the actual distribution, so we
can use it as a prior distribution for $A$ and B.

Here's an array of equally-spaced values from 3 standard deviations below the mean
to 3 standard deviations above (rounded up a little):

$m e a n = 1 7 8$
qs = np. arange(mean-24, mean+24, 0.5)

SciPy provides a function called norm that represents a normal distribution with a
given mean and standard deviation, and provides $\mathrm { p d f } ,$ which evaluates the probability
density function (PDF) of the normal distribution:

from scipy. stats import norm

$s t d = 7 . 7$

$$p s = n o r m \left( m e a n , s t d \right) . p d f \left( q s \right)$$

Probability densities are not probabilities, but if we put them in a Pmf and normalize
it, the result is a discrete approximation of the normal distribution.

from empiricaldist import Pmf

prior = Pmf(ps, qs)
prior.normalize()

Here's what it looks like:

<!-- PageFooter="How Tall Is A?" -->
<!-- PageNumber="147" -->
<!-- PageBreak -->


<figure>

Approximate distribution of height for men in U.S.

0.025

0.020

0.015

PDF

0.010

0.005

0.000

160

170

180

190

200

Height in cm

</figure>


This distribution represents what we believe about the heights of $A$ and $\mathrm { B }$ before we
take into account the data that $A$ is taller.


# Joint Distribution

The next step is to construct a distribution that represents the probability of every
pair of heights, which is called a joint distribution. The elements of the joint distribu-
tion are

$$P \left( A _ { x } \text { and } B _ { y } \right)$$

which is the probability that $A$ is $x$ cm tall and $B$ is $y \quad c m \quad t a l l ,$ for all values of $x$ and $y .$

At this point all we know about $A$ and $\mathrm { B }$ is that they are male residents of the US, so
their heights are independent; that is, knowing the height of $A$ provides no additional
information about the height of $B .$

In that case, we can compute the joint probabilities like this:

$$P \left( A _ { x } \text { and } B _ { y } \right) = P \left( A _ { x } \right) P \left( B _ { y } \right)$$

Each joint probability is the product of one element from the distribution $o f \quad x$ and
one element from the distribution of $y .$

So if we have Pmf objects that represent the distribution of height for $\mathrm { A }$ and B, we can
compute the joint distribution by computing the outer product of the probabilities in
each Pmf.

<!-- PageFooter="Chapter 11: Comparison" -->
<!-- PageNumber="148" -->
<!-- PageBreak -->

The following function takes two Pmf objects and returns a DataFrame that represents
the joint distribution.

def make_joint(pmf1, pmf2):
"""Compute the outer product of two Pmfs. """
X, Y = np.meshgrid(pmf1, pmf2)
☒
return pd. DataFrame(X * Y, columns=pmf1.qs, index=pmf2.qs)
☒ ☒

The column names in the result are the quantities from pmf1; the row labels are the
quantities from pmf2.

In this example, the prior distributions for $A$ and $B$ are the same, so we can compute
the joint prior distribution like this:

joint = make_joint(prior, prior)
joint. shape
(96, 96)

The result is a DataFrame with possible heights of $\mathrm { A }$ along the columns, heights of $\mathrm { B }$
along the rows, and the joint probabilities as elements.

If the prior is normalized, the joint prior is also normalized.

joint. to_numpy() . sum()
1.0

To add up all of the elements, we convert the DataFrame to a NumPy array before
calling sum. Otherwise, DataFrame. sum would compute the sums of the columns and
return a Series.


# Visualizing the Joint Distribution

The following function uses pcolormesh to plot the joint distribution.

import matplotlib.pyplot as plt

def $\mathrm { p l o t } \_ \mathrm { j o i n t } \left( \mathrm { j o i n t } \right. ,$ $\left. \mathrm { c m a p } = { } ^ { \prime } B \text { lues } ^ { \prime } \right) :$
"""Plot a joint distribution with a color mesh. """
vmax = joint. to_numpy().max() * 1.1
plt.pcolormesh(joint. columns, joint. index, joint,
cmap=cmap,
$\mathrm { v i n a x } = \mathrm { v i n a x } ,$
$^ { \prime }$

plt.colorbar()

decorate(xlabel='A height in cm',

$$^ { \prime } B ^ { \prime }$$

<!-- PageFooter="Visualizing the Joint Distribution" -->
<!-- PageNumber="149" -->
<!-- PageBreak -->

Here's what the joint prior distribution looks like:


<figure>

Joint prior distribution of height for A and B

200

0.0007

0.0006

190

B height in cm

0.0005

180

0.0004

0.0003

170

0.0002

160

0.0001

160

170

180

190

200

$\mathrm { A }$ height in cm

</figure>


As you might expect, the probability is highest (darkest) near the mean and drops off
farther from the mean.

Another way to visualize the joint distribution is a contour plot:

def plot_contour(joint):
"""Plot a joint distribution with a contour. """
plt.contour(joint.columns, joint. index, joint,
linewidths=2)
decorate(xlabel='A height in cm',
ylabel='B height in cm')


<figure>
<figcaption>Joint prior distribution of height for $A$ and $B$</figcaption>

200

190

B height in cm

180

170

160

160

170

180

190

200

A height in cm

</figure>


Each line represents a level of equal probability.

<!-- PageFooter="Chapter 11: Comparison" -->
<!-- PageNumber="150" -->
<!-- PageBreak -->


# Likelihood

Now that we have a joint prior distribution, we can update it with the data, which is
that $A$ is taller than $B .$

Each element in the joint distribution represents a hypothesis about the heights of $\mathrm { A }$
and B. To compute the likelihood of every pair of quantities, we can extract the col-
umn names and row labels from the prior, like this:

$$x = j o i n t . c o l u m n s$$

y = joint. index

And use them to compute a mesh grid:

X, Y = np.meshgrid(x, y)
☒

$X$ contains copies of the quantities in x, which are possible heights for $A .$ Y contains
copies of the quantities in $y ,$ which are possible heights for B. If we compare $X$ and $\mathrm { Y } ,$
the result is a Boolean array:

$$A \_ t a l l e r = \left( X > Y \right)$$
$$A _ { - }$$
$$\mathrm { d t v o e } \left( ^ { \prime } b o o l ^ { \prime } \right)$$ ☒

To compute likelihoods, I'll use np. where to make an array with 1 where A_taller is
True and 0 elsewhere:

$a = n p .$ where(A_taller, 1, 0)

To visualize this array of likelihoods, I'll put in a DataFrame with the values of $\mathrm { X }$ as
column names and the values of $y$ as row labels:

$$l i k e l i h o o d = p d . D a t a F r a m e \left( a , i n d e x = x , c o l u m n s = y \right)$$

Here's what it looks like:

<!-- PageFooter="Likelihood" -->
<!-- PageNumber="151" -->
<!-- PageBreak -->


<figure>

$L i k e l i h o o d \quad o f \quad A > B$

200

1.0

190

0.8

B height in cm

180

0.6

170

0.4

0.2

160

0.0

160

170

180

190

200

$\mathrm { A }$ height in cm

</figure>


The likelihood of the data is 1 where $X > Y$ and 0 elsewhere.


# The Update

We have a prior, we have a likelihood, and we are ready for the update. As usual, the
unnormalized posterior is the product of the prior and the likelihood.

posterior = joint * likelihood

I'll use the following function to normalize the posterior:

def normalize(joint):
"""Normalize a joint distribution. """
prob_data = joint. to_numpy() . sum()
joint /= prob_data
return prob_data

normalize(posterior)

And here's what it looks like:

<!-- PageFooter="Chapter 11: Comparison" -->
<!-- PageNumber="152" -->
<!-- PageBreak -->


<figure>

Joint posterior distribution of height for $A$ and $B$

200

0.0014

190

0.0012

B height in cm

0.0010

180

0.0008

0.0006

170

0.0004

160

0.0002

0.0000

160

170

180

190

200

A height in cm

</figure>


All pairs where B is taller than A have been eliminated. The rest of the posterior looks
the same as the prior, except that it has been renormalized.


# Marginal Distributions

The joint posterior distribution represents what we believe about the heights of $A$ and
B given the prior distributions and the information that $A$ is taller.

From this joint distribution, we can compute the posterior distributions for $A$ and B.
To see how, let's start with a simpler problem.

Suppose we want to know the probability that $A$ is 180 cm tall. We can select the col-
umn from the joint distribution where $x = 1 8 0 :$

column = posterior [180]
column.head()

154.0
0.000010

154.5
0.000013

155.0
0.000015

155.5
0.000019

156.0

0.000022

Name: 180.0, dtype: float64

This column contains posterior probabilities for all cases where $x = 1 8 0 ;$ if we add
them up, we get the total probability that $A$ is 180 cm tall.

column.sum()
0.03017221271570807

It's about 3%.

<!-- PageFooter="Marginal Distributions" -->
<!-- PageNumber="153" -->
<!-- PageBreak -->

Now, to get the posterior distribution of height for $A ,$ we can add $u p$ all of the col-
umns, like this:

$\mathrm { c o l u m } _ { - } \mathrm { s u n s } = \text { poster } i o r . s u n \left( a \times i s = 0 \right)$
column_sums . head()


<table>
<tr>
<td>154.0</td>
<td>$0 . 0 0 0 0 0 0 e + 0 0$</td>
</tr>
<tr>
<td>154.5</td>
<td>$1 . 0 1 2 2 6 0 e - 0 7$</td>
</tr>
<tr>
<td>155.0</td>
<td>$2 . 7 3 6 1 5 2 e - \theta$</td>
</tr>
<tr>
<td>155.5</td>
<td>$5 . 5 3 2 5 1 9 e - 0 7$</td>
</tr>
<tr>
<td>156.0</td>
<td>$9 . 9 1 5 6 5 0 e - 0 7$</td>
</tr>
<tr>
<td colspan="2">dtype: float64</td>
</tr>
</table>


The argument $a \times i s = 0$ means we want to add up the columns.

The result is a Series that contains every possible height for $A$ and its probability. In
other words, it is the distribution of heights for A.

We can put it in a Pmf like this:

$$A = P i f \left( C O U U P I _ { - } S U ^ { \prime } \right.$$

When we extract the distribution of a single variable from a joint distribution, the
result is called a marginal distribution. The name comes from a common visualiza-
tion that shows the joint distribution in the middle and the marginal distributions in
the margins.

Here's what the marginal distribution for $A$ looks like:


<figure>

Posterior distribution for $A$

0.030

Posterior for A

0.025

0.020

PDF

0.015

0.010

0.005

0.000

T

T

T

T

T

160

170

180

190

200

Height in cm

</figure>


<!-- PageFooter="Chapter 11: Comparison" -->
<!-- PageNumber="154" -->
<!-- PageBreak -->

Similarly, we can get the posterior distribution of height for $B$ by adding up the rows
and putting the result in a Pmf:

$$r o w _ { - } s u m s = p o s t e r i o r . s u m \left( a x i s = 1 \right)$$
$$\mathrm { m a r g i n a l } _ { m } B = \mathrm { P i n f } \left( r o w _ { - } s u m s \right)$$

Here's what it looks like:

Posterior distribution for $B$


<figure>

0.030

Posterior for B

0.025

0.020

PDF

0.015

0.010

0.005

0.000

160

170

180

190

200

Height in cm

</figure>


Let's put the code from this section in a function:

def marginal(joint, axis):
"""Compute a marginal distribution. """
return Pmf(joint. sum(axis=axis))

marginal takes as parameters a joint distribution and an axis number:

· If $a \times i s = 0 ,$ it returns the marginal of the first variable (the one on the x-axis);

· If $a \times i s = 1 ,$ it returns the marginal of the second variable (the one on the $y$ y-axis).

So we can compute both marginals like this:

marginal_A = marginal(posterior, axis=0)
marginal_B = marginal(posterior, axis=1)

Here's what they look like, along with the prior:

<!-- PageFooter="Marginal Distributions" -->
<!-- PageNumber="155" -->
<!-- PageBreak -->


<figure>

Prior and posterior distributions for $A$ and $B$

0.030

Prior

Posterior for A

Posterior for B

0.025

0.020

PDF

0.015

0.010

0.005

0.000

160

170

180

190

200

Height in cm

</figure>


As you might expect, the posterior distribution for $A$ is shifted to the right and the
posterior distribution for $B$ is shifted to the left.

We can summarize the results by computing the posterior means:

prior.mean()
177.99516026921506

print(marginal_A.mean(), marginal_B.mean())
182.3872812342168 173.6028600023339

Based on the observation that $A$ is taller than B, we are inclined to believe that $\mathrm { A }$ is a
little taller than average, and $B$ is a little shorter.

Notice that the posterior distributions are a little narrower than the prior. We can
quantify that by computing their standard deviations:

prior.std()

7.624924796641578
print(marginal_A.std(), marginal_B.std())
6.270461177645469 6.280513548175111

The standard deviations of the posterior distributions are a little smaller, which
means we are more certain about the heights of $A$ and B after we compare them.


# Conditional Posteriors

Now suppose we measure $A$ and find that he is 170 cm tall. What does that tell us
about B?

<!-- PageFooter="Chapter 11: Comparison" -->
<!-- PageNumber="156" -->
<!-- PageBreak -->

In the joint distribution, each column corresponds to a possible height for $\mathrm { A } .$ We can
select the column that corresponds to height 170 cm like this:

$$c o l u m n \_ 1 7 0 = p o s t e r i o r \left[ 1 7 0 \right]$$

The result is a Series that represents possible heights for $B$ and their relative likeli-
hoods. These likelihoods are not normalized, but we can normalize them like this:

$$B = P m f \left( c o l u m n _ { - } 1 7 0 \right)$$

cond_B.normalize()

0.004358061205454471

Making a Pmf copies the data by default, so we can normalize cond_B without affect-
ing column_170 or posterior. The result is the conditional distribution of height for
B given that $A$ is 170 cm tall.

Here's what it looks like:


<figure>

Prior, posterior and conditional distribution for B

0.10

Prior

Posterior for B

0.08

Conditional posterior for B

0.06

PDF

0.04

0.02

0.00

160

170

180

190

200

Height in cm

</figure>


The conditional posterior distribution is cut off at 170 cm, because we have estab-
lished that $B$ is shorter than A, and A is 170 cm.


# Dependence and Independence

When we constructed the joint prior distribution, I said that the heights of $A$ and $B$
were independent, which means that knowing one of them provides no information
about the other. In other words, the conditional probability $P \left( A _ { x } | B _ { y } \right)$ is the same as
the unconditional probability $P \left( A _ { x } \right) .$

But in the posterior distribution, $A$ and $B$ are not independent. If we know that $A$ is
taller than $B ,$ and we know how tall $A$ is, that gives us information about $B .$

<!-- PageFooter="Dependence and Independence" -->
<!-- PageNumber="157" -->
<!-- PageBreak -->

The conditional distribution we just computed demonstrates this dependence.


# Summary

In this chapter we started with the "outer" operations, like outer product, which we
used to construct a joint distribution.

In general, you cannot construct a joint distribution from two marginal distributions,
but in the special case where the distributions are independent, you can.

We extended the Bayesian update process and applied it to a joint distribution. Then
from the posterior joint distribution we extracted marginal posterior distributions
and conditional posterior distributions.

As an exercise, you'll have a chance to apply the same process to a problem that's a
little more difficult and a lot more useful, updating a chess player's rating based on
the outcome of a game.


# Exercises


## Exercise 11-1.

Based on the results of the previous example, compute the posterior conditional dis-
tribution for $\mathrm { A }$ given that B is 180 cm.

Hint: Use loc to select a row from a DataFrame.


## Exercise 11-2.

Suppose we have established that $A$ is taller than B, but we don't know how tall B is.
Now we choose a random woman, $\mathrm { C } ,$ and find that she is shorter than $A$ by at least 15
cm. Compute posterior distributions for the heights of $A$ and $C$ C.

The average height for women in the US is 163 cm; the standard deviation is 7.3 cm.


## Exercise 11-3.

The Elo rating system is a way to quantify the skill level of players for games like
chess.

It is based on a model of the relationship between the ratings of players and the out-
come of a game. Specifically, if $R _ { A }$ is the rating of player $\mathrm { A }$ and $R _ { B }$ is the rating of
player B, the probability that $A$ beats $B$ is given by the logistic function:

<!-- PageFooter="Chapter 11: Comparison" -->
<!-- PageNumber="158" -->
<!-- PageBreak -->

$$P \left( A \text { beats } B \right) = \frac { 1 } { 1 + 1 0 ^ { \left( R _ { B } - R _ { A } \right) / 4 0 0 } }$$

The parameters 10 and 400 are arbitrary choices that determine the range of the rat-
ings. In chess, the range is from 100 to 2,800.

Notice that the probability of winning depends only on the difference in rankings. As
an example, if $R _ { A }$ exceeds $R _ { B }$ by 100 points, the probability that $A$ wins is:

$1 / \left( 1 + 1 0 * * \left( - 1 0 0 / 4 0 0 \right) \right)$

0.6400649998028851

Suppose A has a current rating of 1,600, but we are not sure it is accurate. We could
describe their true rating with a normal distribution with mean 1,600 and standard
deviation 100, to indicate our uncertainty.

And suppose B has a current rating of 1,800, with the same level of uncertainty.

Then $A$ and $B$ play and $A$ wins. How should we update their ratings?

<!-- PageFooter="Exercises" -->
<!-- PageNumber="159" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 12 Classification" -->

Classification might be the most well-known application of Bayesian methods, made
famous in the 1990s as the basis of the first generation of spam filters.

In this chapter, I'll demonstrate Bayesian classification using data collected and made
available by Dr. Kristen Gorman at the Palmer Long-Term Ecological Research Sta-
tion in Antarctica (see Gorman, Williams, and Fraser, "Ecological Sexual Dimor-
phism and Environmental Variability within a Community of Antarctic Penguins
(Genus Pygoscelis)", March 2014). We'll use this data to classify penguins by species.


# Penguin Data

I'll use pandas to load the data into a DataFrame:

import pandas as pd

df = pd.read_csv('penguins_raw.csv')
df. shape
(344, 17)

The dataset contains one row for each penguin and one column for each variable.

Three species of penguins are represented in the dataset: Adélie, Chinstrap and
Gentoo.

The measurements we'll use are:

<!-- PageNumber="161" -->
<!-- PageBreak -->

· Body Mass in grams (g).

· Flipper Length in millimeters (mm).

· Culmen Length in millimeters.

· Culmen Depth in millimeters.

If you are not familiar with the word "culmen", it refers to the top margin of the beak.
These measurements will be most useful for classification if there are substantial dif-
ferences between species and small variation within species. To see whether that is
true, and to what degree, I'll plot cumulative distribution functions (CDFs) of each
measurement for each species.

The following function takes the DataFrame and a column name. It returns a dictio-
nary that maps from each species name to a Cdf of the values in the column named
colname.

def make_cdf_map(df, colname, by='Species2' ):
"""Make a CDF for each species. """
cdf_map = {}
grouped = df. groupby(by) [colname]
for species, group in grouped:
cdf_map[species] = Cdf. from_seq(group, name=species)
return cdf_map

Here's what the distributions look like for culmen length:


<figure>

1.0

Adelie

Chinstrap

. . . Gentoo

0.8

0.6

CDF

0.4

0.2

0.0

35

40

45

50

55

60

Culmen Length (mm)

</figure>


It looks like we can use culmen length to identify Adélie penguins, but the distribu-
tions for the other two species almost entirely overlap.

Here are the distributions for flipper length:

<!-- PageFooter="Chapter 12: Classification" -->
<!-- PageNumber="162" -->
<!-- PageBreak -->


<figure>

1.0

Adelie

Chinstrap

Gentoo

0.8

0.6

$\frac { 4 } { 8 }$

0.4

0.2

0.0

170

180

190

200

210

220

230

Flipper Length (mm)

</figure>


Using flipper length, we can distinguish Gentoo penguins from the other two species.
So with just these two features, it seems like we should be able to classify penguins
with some accuracy.

All of these CDFs show the sigmoid shape characteristic of the normal distribution; I
will take advantage of that observation in the next section.


## Normal Models

Let's use these features to classify penguins. We'll proceed in the usual Bayesian way:

1\. Define a prior distribution with the three possible species and a prior probability
for each,

2\. Compute the likelihood of the data for each hypothetical species, and then

3\. Compute the posterior probability of each hypothesis.

To compute the likelihood of the data under each hypothesis, I'll use the data to esti-
mate the parameters of a normal distribution for each species.

The following function takes a DataFrame and a column name; it returns a dictionary
that maps from each species name to a norm object.

norm is defined in SciPy; it represents a normal distribution with a given mean and
standard deviation.

from scipy. stats import norm

def make_norm_map(df, colname, by='Species2'):
"Make a map from species to norm object."
norm_map = {}

<!-- PageFooter="Normal Models" -->
<!-- PageNumber="163" -->
<!-- PageBreak -->

grouped = df . groupby(by) [colname]
for species, group in grouped:
mean = group. mean()
std = group. std()
norm_map[species] = norm(mean, std)
return norm_map

For example, here's the dictionary of norm objects for flipper length:

flipper_map = make_norm_map(df, 'Flipper Length (mm)')
flipper_map. keys()
dict_keys(['Adelie', 'Chinstrap', 'Gentoo'])

Now suppose we measure a penguin and find that its flipper is 193 cm. What is the
probability of that measurement under each hypothesis?

The norm object provides $\mathrm { p d f } ,$ which computes the probability density function
(PDF) of the normal distribution. We can use it to compute the likelihood of the
observed data in a given distribution.

$$d a t a = 1 9 3$$

flipper_map[ 'Adelie' ] . pdf (data)
0.054732511875530694

The result is a probability density, so we can't interpret it as a probability. But it is
proportional to the likelihood of the data, so we can use it to update the prior.

Here's how we compute the likelihood of the data in each distribution:

hypos = flipper_map. keys()
likelihood = [flipper_map[hypo]. pdf(data) for hypo in hypos]
likelihood

[0.054732511875530694, 0.05172135615888162, 5.8660453661990634e-05]
Now we're ready to do the update.


# The Update

As usual I'll use a Pmf to represent the prior distribution. For simplicity, let's assume
that the three species are equally likely.

from empiricaldist import Pmf

$$p r i o r = P m f \left( 1 / 3 , h y p o s \right)$$

prior

<!-- PageFooter="Chapter 12: Classification" -->
<!-- PageNumber="164" -->
<!-- PageBreak -->


## probs


<table>
<tr>
<td>Adelie</td>
<td>0.333333</td>
</tr>
<tr>
<td>Chinstrap</td>
<td>0.333333</td>
</tr>
<tr>
<td>Gentoo</td>
<td>0.333333</td>
</tr>
</table>


Now we can do the update in the usual way:

posterior = prior * likelihood
posterior.normalize()
posterior


<table>
<tr>
<th></th>
<th>probs</th>
</tr>
<tr>
<td>Adelie</td>
<td>0.513860</td>
</tr>
<tr>
<td>Chinstrap</td>
<td>0.485589</td>
</tr>
<tr>
<td>Gentoo</td>
<td>0.000551</td>
</tr>
</table>


A penguin with a 193 mm flipper is unlikely to be a Gentoo, but might be either an
Adélie or a Chinstrap (assuming that the three species were equally likely before the
measurement).

The following function encapsulates the steps we just ran. It takes a Pmf representing
the prior distribution, the observed data, and a map from each hypothesis to the dis-
tribution of the feature.

def update_penguin(prior, data, norm_map):
"""Update hypothetical species. """
hypos = prior. qs
likelihood = [norm_map[hypo]. pdf(data) for hypo in hypos]
posterior = prior * likelihood
posterior.normalize()
return posterior

The return value is the posterior distribution.

Here's the previous example again, using update_penguin:

posterior1 = update_penguin(prior, 193, flipper_map)
posterior1

probs


<table>
<tr>
<td>Adelie</td>
<td>0.513860</td>
</tr>
<tr>
<td>Chinstrap</td>
<td>0.485589</td>
</tr>
<tr>
<td>Gentoo</td>
<td>0.000551</td>
</tr>
</table>


As we saw in the CDFs, flipper length does not distinguish strongly between Adélie
and Chinstrap penguins.

<!-- PageFooter="The Update" -->
<!-- PageNumber="165" -->
<!-- PageBreak -->

But culmen length can make this distinction, so let's use it to do a second round of
classification. First we estimate distributions of culmen length for each species like
this:

$$c u l m e n \_ m a p = m a k e \_ n o r m \_ m a p \left( d f , C u l m e n \quad L e n g t h \left( m m \right) \right)$$

Now suppose we see a penguin with culmen length 48 mm. We can use this data to
update the prior:

posterior2 = update_penguin(prior, 48, culmen_map)
posterior2

probs


<table>
<tr>
<td>Adelie</td>
<td>0.001557</td>
</tr>
<tr>
<td>Chinstrap</td>
<td>0.474658</td>
</tr>
<tr>
<td>Gentoo</td>
<td>0.523785</td>
</tr>
</table>


A penguin with culmen length 48 mm is about equally likely to be a Chinstrap or a
Gentoo.

Using one feature at a time, we can often rule out one species or another, but we gen-
erally can't identify species with confidence. We can do better using multiple features.


# Naive Bayesian Classification

To make it easier to do multiple updates, I'll use the following function, which takes a
prior Pmf, a sequence of measurements and a corresponding sequence of dictionaries
containing estimated distributions.

def update_naive(prior, data_seq, norm_maps):
"""Naive Bayesian classifier

prior: Pmf
data_seq: sequence of measurements

norm_maps: sequence of maps from species to distribution

returns: Pmf representing the posterior distribution

posterior = prior. copy()
for data, norm_map in zip(data_seq, norm_maps):
posterior = update_penguin(posterior, data, norm_map)
return posterior

It performs a series of updates, using one variable at a time, and returns the posterior
Pmf. To test it, I'll use the same features we looked at in the previous section: culmen
length and flipper length.

colnames = ['Flipper Length (mm)', 'Culmen Length (mm)']
norm_maps = [flipper_map, culmen_map]

<!-- PageFooter="Chapter 12: Classification" -->
<!-- PageNumber="166" -->
<!-- PageBreak -->

Now suppose we find a penguin with flipper length 193 mm and culmen length 48.
Here's the update:

data_seq = 193, 48
posterior = update_naive(prior, data_seq, norm_maps)
posterior

probs


<table>
<tr>
<td>Adelie</td>
<td>0.003455</td>
</tr>
<tr>
<td>Chinstrap</td>
<td>0.995299</td>
</tr>
<tr>
<td>Gentoo</td>
<td>0.001246</td>
</tr>
</table>


It is almost certain to be a Chinstrap:

posterior.max_prob()
'Chinstrap'

We can loop through the dataset and classify each penguin with these two features:

import numpy as np

df['Classification' $\left. \right] = n p . n a n$

for i, row in df. iterrows():

$$\mathrm { d a t a } \mathrm { s e q } = r o w \left[ c o l n a m e s \right]$$

posterior = update_naive(prior, data_seq, norm_maps)
df . loc[i, 'Classification'] = posterior. max_prob()

This loop adds a column called Classification to the DataFrame; it contains the
species with the maximum posterior probability for each penguin.

So let's see how many we got right:

valid = df['Classification' ].notna()
valid.sum()
342
same = df['Species2' ] == df['Classification' ]
same. sum()
324

There are 344 penguins in the dataset, but two of them are missing measurements, so
we have 342 valid cases. Of those, 324 are classified correctly, which is almost 95%:

same.sum() / valid.sum()
0.9473684210526315

The following function encapsulates these steps.

<!-- PageFooter="Naive Bayesian Classification" -->
<!-- PageNumber="167" -->
<!-- PageBreak -->

def accuracy(df) :
"Compute the accuracy of classification. ""
valid = df['Classification' ]. notna()
same = df[' Species2'] == df['Classification']
return same. sum() / valid.sum()

The classifier we used in this section is called "naive" because it ignores correlations
between the features. To see why that matters, I'll make a less naive classifier: one that
takes into account the joint distribution of the features.


# Joint Distributions

I'll start by making a scatter plot of the data:

import matplotlib. pyplot as plt

def scatterplot(df, var1, var2):
"""Make a scatter plot. """
grouped = df . groupby ( ' Species2')
for species, group in grouped:
plt.plot(group[var1], group[var2],
label=species, lw=0, alpha=0.3)
decorate(xlabel=var1, ylabel=var2)

Here's a scatter plot of culmen length and flipper length for the three species:

var1 = 'Flipper Length (mm)'
var2 = 'Culmen Length (mm)'
scatterplot(df, var1, var2)


<figure>

60

55

Culmen Length (mm)

50

45

40

Adelie

35

· Chinstrap

A Gentoo

170

180

190

200

210

220

230

Flipper Length (mm)

</figure>


<!-- PageFooter="Chapter 12: Classification" -->
<!-- PageNumber="168" -->
<!-- PageBreak -->

Within each species, the joint distribution of these measurements forms an oval
shape, at least roughly. The orientation of the ovals is along a diagonal, which indi-
cates that there is a correlation between culmen length and flipper length.

If we ignore these correlations, we are assuming that the features are independent. To
see what that looks like, I'll make a joint distribution for each species assuming
independence.

The following function makes a discrete Pmf that approximates a normal distribution.

def make_pmf_norm(dist, sigmas=3, n=101):
"""Make a Pmf approximation to a normal distribution. """
mean, std = dist.mean(), dist.std()
low = mean - sigmas * std
high = mean + sigmas * std
qs = np. linspace(low, high, n)
ps = dist.pdf(qs)
$p m f = P m f \left( p s , q s \right)$
pmf.normalize()
return pmf

We can use it, along with make_joint, to make a joint distribution of culmen length
and flipper length for each species:

from utils import make_joint

joint_map = {}
for species in hypos:
pmf1 = make_pmf_norm(flipper_map[species])
pmf2 = make_pmf_norm(culmen_map[species])
joint_map[species] = make_joint(pmf1, pmf2)

The following figure compares a scatter plot of the data to the contours of the joint
distributions, assuming independence.


<figure>

60

55

50

45

40

35

Adelie

· Chinstrap

A Gentoo

T

180

190

200

210

220

T
230

</figure>


<!-- PageFooter="Joint Distributions" -->
<!-- PageNumber="169" -->
<!-- PageBreak -->

The contours of a joint normal distribution form ellipses. In this example, because
the features are uncorrelated, the ellipses are aligned with the axes. But they are not
well aligned with the data.

We can make a better model of the data, and use it to compute better likelihoods,
with a multivariate normal distribution.


# Multivariate Normal Distribution

As we have seen, a univariate normal distribution is characterized by its mean and
standard deviation.

A multivariate normal distribution is characterized by the means of the features and
the covariance matrix, which contains variances, which quantify the spread of the
features, and the covariances, which quantify the relationships among them.

We can use the data to estimate the means and covariance matrix for the population
of penguins. First I'll select the columns we want:

features = df[[var1, var2]]

And compute the means:

mean = features. mean()
mean


<table>
<tr>
<td>Flipper Length (mm)</td>
<td>200.915205</td>
</tr>
<tr>
<td>Culmen Length (mm)</td>
<td>43.921930</td>
</tr>
<tr>
<td>dtype: float64</td>
<td></td>
</tr>
</table>


We can also compute the covariance matrix:

cov = features. cov()
COV


<table>
<tr>
<th></th>
<th>Flipper Length (mm)</th>
<th>Culmen Length (mm)</th>
</tr>
<tr>
<td>Flipper Length (mm)</td>
<td>197.731792</td>
<td>50.375765</td>
</tr>
<tr>
<td>Culmen Length (mm)</td>
<td>50.375765</td>
<td>29.807054</td>
</tr>
</table>


The result is a DataFrame with one row and one column for each feature. The
elements on the diagonal are the variances; the elements off the diagonal are
covariances.

By themselves, variances and covariances are hard to interpret. We can use them to
compute standard deviations and correlation coefficients, which are easier to inter-
pret, but the details of that calculation are not important right now.

Instead, we'll pass the covariance matrix to multivariate_normal, which is a SciPy
function that creates an object that represents a multivariate normal distribution.

<!-- PageFooter="Chapter 12: Classification" -->
<!-- PageNumber="170" -->
<!-- PageBreak -->

As arguments it takes a sequence of means and a covariance matrix:

from scipy. stats import multivariate_normal

multinorm = multivariate_normal(mean, cov)

The following function makes a multivariate_normal object for each species.

def make_multinorm_map(df, colnames):
"""Make a map from each species to a multivariate normal. """
multinorm_map = {}
grouped = df . groupby ( ' Species2')
for species, group in grouped:
features = group[colnames]
mean = features. mean()
cov = features. cov()
multinorm_map[species] = multivariate_normal(mean, cov)
return multinorm_map

Here's how we make this map for the first two features, flipper length and culmen
length:

$$\mathrm { m u l t i n o r m } _ { - } \mathrm { m a p } = \mathrm { m a k e } _ { - } \mathrm { m u l t i n o r m } _ { - } \mathrm { m a p } \left( \mathrm { d f } , \mathrm { \left[ v a r 1 , \right. } \mathrm { \left. v a r 2 \right] } \right)$$

The following figure shows a scatter plot of the data along with the contours of the
multivariate normal distribution for each species:


<figure>

60

55

50

45

40

35

Adelie

· Chinstrap

A Gentoo

180

190

200

210

220

230

</figure>


Because the multivariate normal distribution takes into account the correlations
between features, it is a better model for the data. And there is less overlap in the
contours of the three distributions, which suggests that they should yield better
classifications.

<!-- PageFooter="Multivariate Normal Distribution" -->
<!-- PageNumber="171" -->
<!-- PageBreak -->


# A Less Naive Classifier

In a previous section we used update_penguin to update a prior Pmf based on
observed data and a collection of norm objects that model the distribution of observa-
tions under each hypothesis. Here it is again:

def update_penguin(prior, data, norm_map):
"""Update hypothetical species. ""
hypos = prior. qs
likelihood = [norm_map[hypo].pdf(data) for hypo in hypos]
posterior = prior * likelihood
posterior.normalize()
return posterior

Last time we used this function, the values in norm_map were norm objects, but it also
works if they are multivariate_normal objects.

We can use it to classify a penguin with flipper length 193 and culmen length 48:

$d a t a = 1 9 3 ,$ 48
update_penguin(prior, data, multinorm_map)


<table>
<tr>
<th></th>
<th>probs</th>
</tr>
<tr>
<td>Adelie</td>
<td>0.002740</td>
</tr>
<tr>
<td>Chinstrap</td>
<td>0.997257</td>
</tr>
<tr>
<td>Gentoo</td>
<td>0.000003</td>
</tr>
</table>


A penguin with those measurements is almost certainly a Chinstrap.

Now let's see if this classifier does any better than the naive Bayesian classifier. I'll
apply it to each penguin in the dataset:

df['Classification' ] = np. nan

for i, row in df. iterrows():
data = row[colnames]
posterior = update_penguin(prior, data, multinorm_map)
df . loc[i, 'Classification'] = posterior. idxmax()

And compute the accuracy:

accuracy(df)

0.9532163742690059

It turns out to be only a little better: the accuracy is 95.3%, compared to 94.7% for the
naive Bayesian classifier.

<!-- PageFooter="Chapter 12: Classification" -->
<!-- PageNumber="172" -->
<!-- PageBreak -->


# Summary

In this chapter, we implemented a naive Bayesian classifier, which is "naive" in the
sense that it assumes that the features it uses for classification are independent.

To see how bad that assumption is, we also implemented a classifier that uses the
multivariate normal distribution to model the joint distribution of the features, which
includes their dependencies.

In this example, the non-naive classifier is only marginally better. In one way, that's
disappointing. After all that work, it would have been nice to see a bigger improve-
ment. But in another way, it's good news. In general, a naive Bayesian classifier is eas-
ier to implement and requires less computation. If it works nearly as well as a more
complex algorithm, it might be a good choice for practical purposes.

Speaking of practical purposes, you might have noticed that this example isn't very
useful. If we want to identify the species of a penguin, there are easier ways than
measuring its flippers and beak.

But there are scientific uses for this type of classification. One of them is the subject of
the research paper we started with: sexual dimorphism, that is, differences in shape
between male and female animals.

In some species, like angler fish, males and females look very different. In other spe-
cies, like mockingbirds, they are difficult to tell apart. And dimorphism is worth
studying because it provides insight into social behavior, sexual selection, and
evolution.

One way to quantify the degree of sexual dimorphism in a species is to use a classifi-
cation algorithm like the one in this chapter. If you can find a set of features that
makes it possible to classify individuals by sex with high accuracy, that's evidence of
high dimorphism.

As an exercise, you can use the dataset from this chapter to classify penguins by sex
and see which of the three species is the most dimorphic.


# Exercises


## Exercise 12-1.

In my example I used culmen length and flipper length because they seemed to pro-
vide the most power to distinguish the three species. But maybe we can do better by
using more features.

<!-- PageFooter="Summary" -->
<!-- PageNumber="173" -->
<!-- PageBreak -->

Make a naive Bayesian classifier that uses all four measurements in the dataset: cul-
men length and depth, flipper length, and body mass. Is it more accurate than the
model with two features?


## Exercise 12-2.

One of the reasons the penguin dataset was collected was to quantify sexual dimor-
phism in different penguin species, that is, physical differences between male and
female penguins. One way to quantify dimorphism is to use measurements to classify
penguins by sex. If a species is more dimorphic, we expect to be able to classify them
more accurately.

As an exercise, pick a species and use a Bayesian classifier (naive or not) to classify
the penguins by sex. Which features are most useful? What accuracy can you achieve?

<!-- PageFooter="Chapter 12: Classification" -->
<!-- PageNumber="174" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 13" -->


# Inference

Whenever people compare Bayesian inference with conventional approaches, one of
the questions that comes up most often is something like, "What about p-values?"
And one of the most common examples is the comparison of two groups to see if
there is a difference in their means.

In classical statistical inference, the usual tool for this scenario is a Student's t-test,
and the result is a p-value. This process is an example of null hypothesis significance
testing.

A Bayesian alternative is to compute the posterior distribution of the difference
between the groups. Then we can use that distribution to answer whatever questions
we are interested in, including the most likely size of the difference, a credible interval
that's likely to contain the true difference, the probability of superiority, or the proba-
bility that the difference exceeds some threshold.

To demonstrate this process, I'll solve a problem borrowed from a statistical textbook:
evaluating the effect of an educational "treatment" compared to a control.


## Improving Reading Ability

We'll use data from a PhD dissertation in educational psychology written in 1987,
which was used as an example in a statistics textbook from 1989 and published on
DASL, a web page that collects data stories.

<!-- PageNumber="175" -->
<!-- PageBreak -->

Here's the description from DASL:

An educator conducted an experiment to test whether new directed reading activities
in the classroom will help elementary school pupils improve some aspects of their
reading ability. She arranged for a third grade class of 21 students to follow these activ-
ities for an 8-week period. A control classroom of 23 third graders followed the same
curriculum without the activities. At the end of the 8 weeks, all students took a Degree
of Reading Power (DRP) test, which measures the aspects of reading ability that the
treatment is designed to improve.

The dataset is available here. I'll use pandas to load the data into a DataFrame:

import pandas as pd

df = pd. read_csv('drp_scores. csv' , skiprows=21, delimiter='\t')
df. head(3)

Treatment
Response


<table>
<tr>
<td>0 Treated</td>
<td>24</td>
</tr>
<tr>
<td>1 Treated</td>
<td>43</td>
</tr>
<tr>
<td>2 Treated</td>
<td>58</td>
</tr>
</table>


The Treatment column indicates whether each student was in the treated or control
group. The Response is their score on the test.

I'll use groupby to separate the data for the Treated and Control groups:

grouped = df . groupby ('Treatment' )
responses = {}

for name, group in grouped:
$\mathrm { r e s p o n s e s } \left[ \mathrm { n a n e } \right] = \mathrm { g r o u p } \left[ ^ { \prime } \mathrm { R e s p o n s e } ^ { \prime } \right]$

Here are CDFs of the scores for the two groups and summary statistics:

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="176" -->
<!-- PageBreak -->


<figure>

Distributions of test scores

1.0

Control

Treated

0.8

0.6

CDF

0.4

0.2

0.0

10

20

30

40

50

60

70

80

Score

</figure>


There is overlap between the distributions, but it looks like the scores are higher in
the treated group. The distribution of scores is not exactly normal for either group,
but it is close enough that the normal model is a reasonable choice.

So I'll assume that in the entire population of students (not just the ones in the
experiment), the distribution of scores is well modeled by a normal distribution with
unknown mean and standard deviation. I'll use mu and sigma to denote these
unknown parameters, and we'll do a Bayesian update to estimate what they are.


## Estimating Parameters

As always, we need a prior distribution for the parameters. Since there are two
parameters, it will be a joint distribution. I'll construct it by choosing marginal distri-
butions for each parameter and computing their outer product.

As a simple starting place, I'll assume that the prior distributions for mu and sigma
are uniform. The following function makes a Pmf object that represents a uniform
distribution.


### from empiricaldist import Pmf

def make_uniform(qs, name=None, ** options):
"""Make a Pmf that represents a uniform distribution. """
pmf = Pmf(1.0, qs, ** options)
pmf.normalize()
if name:
pmf . index. name = name
return pmf

<!-- PageFooter="Estimating Parameters" -->
<!-- PageNumber="177" -->
<!-- PageBreak -->

make_uniform takes as parameters:

· An array of quantities, qs, and

· A string, name, which is assigned to the index so it appears when we display the
Pmf.

Here's the prior distribution for mu:

import numpy as np

qs = np. linspace(20, 80, num=101)
prior_mu = make_uniform(qs, name='mean')

I chose the lower and upper bounds by trial and error. I'll explain how when we look
at the posterior distribution.

Here's the prior distribution for sigma:

qs = np. linspace(5, 30, num=101)
prior_sigma = make_uniform(qs, name='std')

Now we can use make_joint to make the joint prior distribution:

from utils import make_joint
prior = make_joint(prior_mu, prior_sigma)

And we'll start by working with the data from the control group:

data = responses['Control' ]
data. shape
(23,)

In the next section we'll compute the likelihood of this data for each pair of parame-
ters in the prior distribution.


## Likelihood

We would like to know the probability of each score in the dataset for each hypotheti-
cal pair of values, mu and sigma. I'll do that by making a 3-dimensional grid with val-
ues of mu on the first axis, values of sigma on the second axis, and the scores from the
dataset on the third axis:

mu_mesh, sigma_mesh, data_mesh = np.meshgrid(
prior. columns, prior. index, data)

mu_mesh . shape
(101, 101, 23)

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="178" -->
<!-- PageBreak -->

Now we can use norm. pdf to compute the probability density of each score for each
hypothetical pair of parameters:

from scipy. stats import norm

$= \mathrm { n o r } n \left( n u _ { - } \right. ,$ sigma_mesh) .pdf(data_mesh)
densities . shape

(101, 101, 23)

The result is a 3-D array. To compute likelihoods, I'll multiply these densities along
axis=2, which is the axis of the data:

$$l i k e l i h o o d = d e n s i t i e s . p r o d \left( a x i s = 2 \right)$$

likelihood. shape
(101, 101)

The result is a 2-D array that contains the likelihood of the entire dataset for each
hypothetical pair of parameters.

We can use this array to update the prior, like this:

from utils import normalize

posterior = prior * likelihood
normalize(posterior)
posterior . shape
(101, 101)

The result is a DataFrame that represents the joint posterior distribution.

The following function encapsulates these steps.

def update_norm(prior, data):
"""Update the prior based on data. """
mu_mesh, sigma_mesh, data_mesh = np. meshgrid(
prior.columns, prior. index, data)

densities = norm(mu_mesh, sigma_mesh).pdf(data_mesh)
likelihood = densities. prod(axis=2)

posterior = prior * likelihood
normalize(posterior)

return posterior

Here are the updates for the control and treatment groups:

data = responses[ 'Control']
posterior_control = update_norm(prior, data)
data = responses[ ' Treated' ]
posterior_treated = update_norm(prior, data)

<!-- PageFooter="Likelihood" -->
<!-- PageNumber="179" -->
<!-- PageBreak -->

And here's what they look like:


<figure>

Joint posterior distributions of mu and sigma

30

Standard deviation (sigma)

25

20

Control

15

Treated

10

5

20

30

40

50

60

70

80

Mean (mu)

</figure>


Along the x-axis, it looks like the mean score for the treated group is higher. Along
the y-axis, it looks like the standard deviation for the treated group is lower.

If we think the treatment causes these differences, the data suggest that the treatment
increases the mean of the scores and decreases their spread. We can see these differ-
ences more clearly by looking at the marginal distributions for mu and sigma.


## Posterior Marginal Distributions

I'll use marginal, which we saw in "Marginal Distributions" on page 153, to extract
the posterior marginal distributions for the population means:

from utils import marginal

pmf_mean_control = marginal(posterior_control, 0)
pmf_mean_treated = marginal(posterior_treated, 0)

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="180" -->
<!-- PageBreak -->

Here's what they look like:


<figure>

Posterior distributions of mu

Control

Treated

0.08

0.06

$P D F$

0.02

0.00

20

30

40

50

60

70

80

Population mean (mu)

</figure>


In both cases the posterior probabilities at the ends $\mathrm { o f }$ the range are near zero, which
means that the bounds we chose for the prior distribution are wide enough.

Comparing the marginal distributions for the two groups, it looks like the population
mean in the treated group is higher. We can use $\mathrm { p r o b } \_ \mathrm { g t }$ to compute the probability
of superiority:

Pmf . prob_gt(pmf_mean_treated, pmf_mean_control)

0.980479025187326

There is a 98% chance that the mean in the treated group is higher.


## Distribution of Differences

To quantify the magnitude of the difference between groups, we can use sub_dist to
compute the distribution of the difference:

$$\mathrm { p m f } _ { - } \mathrm { d i f } f = \mathrm { P n f } _ { - } \mathrm { s u b } _ { - } \mathrm { d i s t } \left( \mathrm { p n f } _ { - } \mathrm { m e a n } _ { - } \mathrm { t r e a t e d } , \mathrm { p r f } _ { - } \mathrm { m e a n } _ { - } \mathrm { c o n t r o l } \right)$$

There are two things to be careful about when you use methods like sub_dist. The
first is that the result usually contains more elements than the original Pmf. In this
example, the original distributions have the same quantities, so the size increase is
moderate.

len(pmf_mean_treated), len(pmf_mean_control), len(pmf_diff)

(101, 101, 879)

In the worst case, the size of the result can be the product of the sizes of the originals.

<!-- PageFooter="Distribution of Differences" -->
<!-- PageNumber="181" -->
<!-- PageBreak -->

The other thing to be careful about is plotting the Pmf. In this example, if we plot the
distribution of differences, the result is pretty noisy:


<figure>

Posterior distribution of difference in mu

0.04

0.03

PDF

0.02

0.01

0.00

-60

-40

-20

0

20

40

60

Difference in population means

</figure>


There are two ways to work around that limitation. One is to plot the CDF, which
smooths out the noise:

$$\mathrm { c d f } _ { - } \mathrm { d i f f } \mathrm { f } = \mathrm { p m f } _ { - } \mathrm { d i f f } _ { \mathrm { e } } \mathrm { m a k e } _ { - } \mathrm { c d f } \left( \right)$$


<figure>

Posterior distribution of difference in mu

1.0

0.8

0.6

$\frac { 4 } { 8 }$

0.4

0.2

0.0

-60

-40

-20

0

20

40

$6 0$

Difference in population means

</figure>


The other option is to use kernel density estimation (KDE) to make a smooth
approximation of the PDF on an equally-spaced grid, which is what this function
does:

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="182" -->
<!-- PageBreak -->

from scipy. stats import gaussian_kde

def kde_from_pmf(pmf, n=101):
"""Make a kernel density estimate for a PMF. """
kde = gaussian_kde(pmf.qs, weights=pmf.ps)
qs = np. linspace(pmf.qs.min(), pmf.qs.max(), n)
ps = kde. evaluate(qs)
$p m f = P m f \left( p s , q s \right)$
pmf.normalize()
return pmf

kde_from_pmf takes as parameters a Pmf and the number of places to evaluate the
KDE.

It uses gaussian_kde, which we saw in "Kernel Density Estimation" on page 115,
passing the probabilities from the Pmf as weights. This makes the estimated densities
higher where the probabilities in the Pmf are higher.

Here's what the kernel density estimate looks like for the Pmf of differences between
the groups:

$$\mathrm { k d e } _ { - } \mathrm { d i f f } = \mathrm { k d e } _ { - } \mathrm { f r o m } _ { - } \mathrm { p n f } \left( \mathrm { p m f } _ { - } \mathrm { d i f f } \right)$$


<figure>

Posterior distribution of difference in mu

0.08

0.06

PDF

0.04

0.02

0.00

-60

-40

-20

0

20

40

60

Difference in means

</figure>


The mean of this distribution is almost 10 points on a test where the mean is around
45, so the effect of the treatment seems to be substantial:

pmf_diff.mean()
9.954413088940848

<!-- PageFooter="Distribution of Differences" -->
<!-- PageNumber="183" -->
<!-- PageBreak -->

We can use credible_interval to compute a 90% credible interval:

pmf_diff.credible_interval(0.9)

array([ 2.4, 17.4])

Based on this interval, we are pretty sure the treatment improves test scores by 2 to 17
points.


### Using Summary Statistics

In this example the dataset is not very big, so it doesn't take too long to compute the
probability of every score under every hypothesis. But the result is a 3-D array; for
larger datasets, it might be too big to compute practically.

Also, with larger datasets the likelihoods get very small, sometimes so small that we
can't compute them with floating-point arithmetic. That's because we are computing
the probability of a particular dataset; the number of possible datasets is astronomi-
cally big, so the probability of any of them is very small.

An alternative is to compute a summary of the dataset and compute the likelihood
of the summary. For example, if we compute the mean and standard deviation of the
data, we can compute the likelihood of those summary statistics under each
hypothesis.

As an example, suppose we know that the actual mean of the population, $\mu ,$ is 42 and
the actual standard deviation, $\sigma ,$ is 17.

$$m u = 4 2$$

sigma = 17

Now suppose we draw a sample from this distribution with sample size $n = 2 0 ,$ and
compute the mean of the sample, which I'll call m, and the standard deviation of the
sample, which I'll call s.

And suppose it turns out that:

$n = 2 0$
$m = 4 1$
$S = 1 8$

The summary statistics, m and s, are not too far from the parameters $\mu$ and o, so it
seems like they are not too unlikely.

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="184" -->
<!-- PageBreak -->

To compute their likelihood, we will take advantage of three results from mathemati-
cal statistics:

· Given $\mu$ and $\sigma ,$ the distribution of $m$ is normal with parameters $\mu$ and $\sigma / \sqrt { n }$

· The distribution of $\mathcal{S}$ is more complicated, but if we compute the transform
$t = n s ^ { 2 } / \sigma ^ { 2 } ,$ the distribution of $t$ is chi-squared with parameter $n \quad -$ 1; and

· According to Basu's theorem, m and s are independent.

So let's compute the likelihood of m and s given $\mu$ and o.

First I'll create a norm object that represents the distribution of m:

$$\mathrm { d i s t } _ { - } \eta = n o r m \left( n u , s i g m a / n p . s q r t \left( n \right) \right)$$

This is the "sampling distribution of the mean". We can use it to compute the likeli-
hood of the observed value of m, which is 41.

$$l i k e 1 = d i s t _ { - } n . p d f \left( n \right)$$

like1

$$0 . 1 0 1 3 7 9 1 5 1 3 8 4 9 7 3 7 2$$

Now let's compute the likelihood of the observed value of s, which is 18. First, we
compute the transformed value t:

$$t = n * s ^ { * * } 2 / s i g m a ^ { * * 2 }$$

t
22.422145328719722

Then we create a chi2 object to represent the distribution of t:

from scipy. stats import chi2

$$\mathrm { d i s t } _ { - } s = \mathrm { c h i } 2 \left( n - 1 \right)$$

Now we can compute the likelihood of t:

$l i k e 2 = d i s t _ { - } s . p d f \left( t \right)$
like2
0.04736427909437004

Finally, because m and s are independent, their joint likelihood is the product of their
likelihoods:

$$l i k e = l i k e 1 * l i k e 2$$

like

0.004801750420548287

Now we can compute the likelihood of the data for any values $\mathrm { o f } \mu$ and o, which we'll
use in the next section to do the update.

<!-- PageFooter="Using Summary Statistics" -->
<!-- PageNumber="185" -->
<!-- PageBreak -->


# Update with Summary Statistics

Now we're ready to do an update. I'll compute summary statistics for the two groups:

$s u m m a r y =$

for name, response in responses. items():
summary[ name] = len(response), response. mean(), response.std()


## summary

{'Control': (23, 41.52173913043478, 17.148733229699484),
'Treated' : (21, 51.476190476190474, 11.00735684721381)}

The result is a dictionary that maps from group name to a tuple that contains the
sample size, n, the sample mean, m, and the sample standard deviation s, for each
group.

I'll demonstrate the update with the summary statistics from the control group:

n, m, s = summary[ 'Control']

I'll make a mesh with hypothetical values of mu on the x-axis and values of sigma on
the $y$ y-axis:

mus, sigmas = np.meshgrid(prior.columns, prior. index)
mus . shape

(101, 101)

Now we can compute the likelihood of seeing the sample mean, $m$ m, for each pair of
parameters:

like1 = norm(mus, sigmas/np.sqrt(n)).pdf(m)

like1. shape

(101, 101)

And we can compute the likelihood of the sample standard deviation, s, for each pair
of parameters:

$$= n * s ^ { * * 2 } / s ^ { i g m a s * * 2 }$$

like2 = chi2(n-1).pdf(ts)
like2. shape

(101, 101)

Finally, we can do the update with both likelihoods:

$$\mathrm { p o s t e r } i o r _ { - } \mathrm { c o n t r o l } 2 = \mathrm { p r i o r } * l i k e 1 * l i k e 2$$

To compute the posterior distribution for the treatment group, I'll put the previous
steps in a function:

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="186" -->
<!-- PageBreak -->

def update_norm_summary(prior, data) :
"""Update a normal distribution using summary statistics. """
n, m, $s = d a t a$
mu_mesh, sigma_mesh = np.meshgrid(prior.columns, prior. index)
like1 = norm(mu_mesh, sigma_mesh/np.sqrt(n)).pdf(m)
like2 = chi2(n-1).pdf(n * s ** 2 / sigma_mesh ** 2)

posterior = prior * like1 * like2
normalize(posterior)


## return posterior

Here's the update for the treatment group:

$$\mathrm { d a t a } = \mathrm { s u m a r y } \left[ ^ { \prime } \mathrm { T r e a t e d } ^ { \prime } \right]$$
$$p o s t e r i o r \_ t r e a t e d 2 = u p d a t e \_ n o r m \_ s u m m a r y \left( p r i o r , d a t a \right)$$

And here are the results:


<figure>

Joint posterior distributions of mu and sigma

30

Standard deviation (sigma)

25

20

Control

15

Treated

10

5

20

30

40

50

60

70

80

Mean (mu)

</figure>


Visually, these posterior joint distributions are similar to the ones we computed using
the entire dataset, not just the summary statistics. But they are not exactly the same,
as we can see by comparing the marginal distributions.


# Comparing Marginals

Again, let's extract the marginal posterior distributions:

from utils import marginal

pmf_mean_control2 = marginal(posterior_control2, 0)
pmf_mean_treated2 = marginal(posterior_treated2, 0)

<!-- PageFooter="Comparing Marginals" -->
<!-- PageNumber="187" -->
<!-- PageBreak -->

And compare them to results we got using the entire dataset (the dashed lines):


<figure>

Posterior distributions of mu

Control

Treated

0.08

0.06

$P D F$

0.02

0.00

20

30

40

50

60

70

80

Population mean

</figure>


The posterior distributions based on summary statistics are similar to the posteriors
we computed using the entire dataset, but in both cases they are shorter and a little
wider.

That's because the update with summary statistics is based on the implicit assumption
that the distribution of the data is normal. But it's not; as a result, when we replace the
dataset with the summary statistics, we lose some information about the true distri-
bution of the data. With less information, we are less certain about the parameters.


## Summary

In this chapter we used a joint distribution to represent prior probabilities for the
parameters of a normal distribution, mu and sigma. And we updated that distribution
two ways: first using the entire dataset and the normal PDF; then using summary sta-
tistics, the normal PDF, and the chi-square PDF. Using summary statistics is compu-
tationally more efficient, but it loses some information in the process.

Normal distributions appear in many domains, so the methods in this chapter are
broadly applicable. The exercises at the end of the chapter will give you a chance to
apply them.

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="188" -->
<!-- PageBreak -->


# Exercises


## Exercise 13-1.

Looking again at the posterior joint distribution of $\mathrm { m u }$ and sigma, it seems like the
standard deviation of the treated group might be lower; if so, that would suggest that
the treatment is more effective for students with lower scores.

But before we speculate too much, we should estimate the size of the difference and
see whether it might actually be 0.

Extract the marginal posterior distributions of sigma for the two groups. What is the
probability that the standard deviation is higher in the control group?

Compute the distribution of the difference in sigma between the two groups. What is
the mean of this difference? What is the 90% credible interval?


## Exercise 13-2.

An effect size is a statistic intended to quantify the magnitude of a phenomenon. If
the phenomenon is a difference in means between two groups, a common way to
quantify it is Cohen's effect size, denoted $d .$

If the parameters for Group 1 are $\left( \mu _ { 1 } , \sigma _ { 1 } \right) ,$ and the parameters for Group 2 are
$\left( \mu _ { 2 } , \sigma _ { 2 } \right) ,$ Cohen's effect size is

$$d = \frac { \mu _ { 1 } - \mu _ { 2 } } { \left( \sigma _ { 1 } + \sigma _ { 2 } \right) / 2 }$$

Use the joint posterior distributions for the two groups to compute the posterior dis-
tribution for Cohen's effect size.


## Exercise 13-3.

This exercise is inspired by a question that appeared on Reddit.

An instructor announces the results of an exam like this: "The average score on this
exam was 81. Out of 25 students, 5 got more than 90, and I am happy to report that
no one failed (got less than 60)."

Based on this information, what do you think the standard deviation of scores was?

You can assume that the distribution of scores is approximately normal. And let's
assume that the sample mean, 81, is actually the population mean, so we only have to
estimate sigma.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="189" -->
<!-- PageBreak -->

Hint: To compute the probability of a score greater than 90, you can use norm.sf,
which computes the survival function, also known as the complementary CDF, or
$1 - \cot \left( x \right) .$

Exercise 13-4.

The Variability Hypothesis is the observation that many physical traits are more vari-
able among males than among females, in many species.

It has been a subject of controversy since the early 1800s, which suggests an exercise
we can use to practice the methods in this chapter. Let's look at the distribution of
heights for men and women in the U.S. and see who is more variable.

I used 2018 data from the CDC's Behavioral Risk Factor Surveillance System
(BRFSS), which includes self-reported heights from 154,407 men and 254,722
women.

Here's what I found:

· The average height for men is 178 cm; the average height for women is 163 cm.
So men are taller on average; no surprise there.

· For men the standard deviation is 8.27 cm; for women it is 7.75 cm. So in abso-
lute terms, men's heights are more variable.

But to compare variability between groups, it is more meaningful to use the coeffi-
cient of variation (CV), which is the standard deviation divided by the mean. It is a
dimensionless measure of variability relative to scale.

For men CV is 0.0465; for women it is 0.0475. The coefficient of variation is higher
for women, so this dataset provides evidence against the Variability Hypothesis. But
we can use Bayesian methods to make that conclusion more precise.

Use these summary statistics to compute the posterior distribution of mu and sigma
for the distributions of male and female height. Use Pmf. div_dist to compute poste-
rior distributions of CV. Based on this dataset and the assumption that the distribu-
tion of height is normal, what is the probability that the coefficient of variation is
higher for men? What is the most likely ratio of the CVs and what is the 90% credible
interval for that ratio?

<!-- PageFooter="Chapter 13: Inference" -->
<!-- PageNumber="190" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 14" -->


# Survival Analysis

This chapter introduces "survival analysis", which is a set of statistical methods used
to answer questions about the time until an event. In the context of medicine it is lit-
erally about survival, but it can be applied to the time until any kind of event, or
instead of time it can be about space or other dimensions.

Survival analysis is challenging because the data we have are often incomplete. But as
we'll see, Bayesian methods are particularly good at working with incomplete data.

As examples, we'll consider two applications that are a little less serious than life and
death: the time until light bulbs fail and the time until dogs in a shelter are adopted.
To describe these "survival times", we'll use the Weibull distribution.


## The Weibull Distribution

The Weibull distribution is often used in survival analysis because it is a good model
for the distribution of lifetimes for manufactured products, at least over some parts of
the range.

SciPy provides several versions of the Weibull distribution; the one we'll use is called
weibull_min. To make the interface consistent with our notation, I'll wrap it in a
function that takes as parameters $\lambda ,$ which mostly affects the location or "central ten-
dency" of the distribution, and $k ,$ which affects the shape.

from scipy. stats import weibull_min

def weibull_dist(lam, k):
return weibull_min(k, scale=lam)

<!-- PageNumber="191" -->
<!-- PageBreak -->

As an example, here's a Weibull distribution with parameters $\lambda = 3$ and $k = 0 . 8 :$

$l a m = 3$
$k = 0 . 8$

$$\arctan l d i s t = w e i b u l l _ { - } d i s t \left( l a n , k \right)$$

The result is an object that represents the distribution. Here's what the Weibull CDF
looks like with those parameters:


<figure>
<figcaption>CDF of a Weibull distribution</figcaption>

0.8

0.6

CDF

0.4

0.2

0.0

0

2

4

6

8

10

12

Duration in time

</figure>


actual_dist provides rvs, which we can use to generate a random sample from this
distribution:

data = actual_dist.rvs(10)
data

array([0.80497283, 2.11577082, 0.43308797, 0.10862644, 5.17334866,
3.25745053, 3.05555883, 2.47401062, 0.05340806, 1.08386395])

So, given the parameters of the distribution, we can generate a sample. Now let's see if
we can go the other way: given the sample, we'll estimate the parameters.

Here's a uniform prior distribution for $\lambda :$

from utils import make_uniform

lams = np. linspace(0.1, 10.1, num=101)
prior_lam = make_uniform(lams, name=' lambda')

And a uniform prior for $k :$

$$k s = n p . l i n s p a c e \left( 0 . 1 , 5 . 1 , n u m = 1 0 1 \right)$$
$$k = \text { nake } _ { - } \text { unifor } \left( k s , \text { name } = { } ^ { \prime } k ^ { \prime } \right)$$

I'll use make_joint to make a joint prior distribution for the two parameters:

<!-- PageFooter="Chapter 14: Survival Analysis" -->
<!-- PageNumber="192" -->
<!-- PageBreak -->

from utils import make_joint

prior = make_joint(prior_lam, prior_k)

The result is a DataFrame that represents the joint prior, with possible values of $\lambda$
across the columns and values of $k$ down the rows.

Now I'll use meshgrid to make a 3-D mesh with $\lambda$ on the first axis $\left( a \times i s = 0 \right) ,$ $k$ on the
second axis (axis=1), and the data on the third axis $\left( a x i s = 2 \right) :$

lam_mesh, k_mesh, data_mesh = np.meshgrid(
prior.columns, prior. index, data)

Now we can use weibull_dist to compute the PDF of the Weibull distribution for
each pair of parameters and each data point:

densities = weibull_dist(lam_mesh, k_mesh).pdf(data_mesh)
densities. shape
(101, 101, 10)

The likelihood of the data is the product of the probability densities along $a \times i s = 2 .$

likelihood = densities. prod(axis=2)
likelihood. sum()
2.0938302958838208e-05

Now we can compute the posterior distribution in the usual way:

from utils import normalize

posterior = prior * likelihood
normalize(posterior)

The following function encapsulates these steps. It takes a joint prior distribution and
the data, and returns a joint posterior distribution:

def update_weibull(prior, data):
"""Update the prior based on data. """
lam_mesh, k_mesh, data_mesh = np.meshgrid(
prior.columns, prior. index, data)

densities = weibull_dist(lam_mesh, k_mesh).pdf(data_mesh)
likelihood = densities. prod(axis=2)

posterior = prior * likelihood
normalize(posterior)

return posterior

Here's how we use it:

posterior = update_weibull(prior, data)

And here's a contour plot of the joint posterior distribution:

<!-- PageFooter="The Weibull Distribution" -->
<!-- PageNumber="193" -->
<!-- PageBreak -->


<figure>

Posterior joint distribution of Weibull parameters

5

4

3

$\rightharpoonup$

2

1

2

4

6

8

10

$\mathrm { l a m b d a }$

</figure>


It looks like the range of likely values for $\lambda$ is about 1 to 4, which contains the actual
value we used to generate the data, 3. And the range for $k$ is about 0.5 to 1.5, which
contains the actual value, 0.8.


## Incomplete Data

In the previous example we were given 10 random values from a Weibull distribu-
tion, and we used them to estimate the parameters (which we pretended we didn't
know).

But in many real-world scenarios, we don't have complete data; in particular, when
we observe a system at a point in time, we generally have information about the past,
but not the future.

As an example, suppose you work at a dog shelter and you are interested in the time
between the arrival of a new dog and when it is adopted. Some dogs might be snap-
ped up immediately; others might have to wait longer. The people who operate the
shelter might want to make inferences about the distribution of these residence times.

Suppose you monitor arrivals and departures over 8 weeks, and 10 dogs arrive during
that interval. I'll assume that their arrival times are distributed uniformly, so I'll gen-
erate random values like this:

start = np.random. uniform(0, 8, size=10)
start

array([0.78026881, 6.08999773, 1.97550379, 1.1050535 , 2.65157251,
0.66399652, 5.37581665, 6.45275039, 7.86193532, 5.08528588])

Now let's suppose that the residence times follow the Weibull distribution we used in
the previous example. We can generate a sample from that distribution like this:

<!-- PageFooter="Chapter 14: Survival Analysis" -->
<!-- PageNumber="194" -->
<!-- PageBreak -->

duration = actual_dist.rvs(10)
duration


<table>
<tr>
<td>array([0.80497283,</td>
<td>2.11577082,</td>
<td>0.43308797,</td>
<td>0.10862644,</td>
<td>5.17334866,</td>
</tr>
<tr>
<td>3.25745053,</td>
<td>3.05555883,</td>
<td>2.47401062,</td>
<td>0.05340806,</td>
<td>1.08386395])</td>
</tr>
</table>


I'll use these values to construct a DataFrame that contains the arrival and departure
times for each dog, called start and end:

import pandas as pd

d = dict(start=start, end=start+duration)
obs = pd. DataFrame(d)

For display purposes, I'll sort the rows of the DataFrame by arrival time:

obs = obs. sort_values(by='start', ignore_index=True)
obs


<table>
<tr>
<th></th>
<th>start</th>
<th>end</th>
</tr>
<tr>
<td>0</td>
<td>0.663997</td>
<td>3.921447</td>
</tr>
<tr>
<td>1</td>
<td>0.780269</td>
<td>1.585242</td>
</tr>
<tr>
<td>2</td>
<td>1.105053</td>
<td>1.213680</td>
</tr>
<tr>
<td>3</td>
<td>1.975504</td>
<td>2.408592</td>
</tr>
<tr>
<td>4</td>
<td>2.651573</td>
<td>7.824921</td>
</tr>
<tr>
<td>5</td>
<td>5.085286</td>
<td>6.169150</td>
</tr>
<tr>
<td>6</td>
<td>5.375817</td>
<td>8.431375</td>
</tr>
<tr>
<td>7</td>
<td>6.089998</td>
<td>8.205769</td>
</tr>
<tr>
<td>8</td>
<td>6.452750</td>
<td>8.926761</td>
</tr>
<tr>
<td>9</td>
<td>7.861935</td>
<td>7.915343</td>
</tr>
</table>


Notice that several of the lifelines extend past the observation window of 8 weeks. So
if we observed this system at the beginning of Week 8, we would have incomplete
information. Specifically, we would not know the future adoption times for Dogs 6, 7,
and 8.

I'll simulate this incomplete data by identifying the lifelines that extend past the
observation window:

$$= \text { obs } \left[ ^ { \prime } \text { end } \right] > 8$$

censored is a Boolean Series that is True for lifelines that extend past Week 8.

Data that is not available is sometimes called "censored" in the sense that it is hidden
from us. But in this case it is hidden because we don't know the future, not because
someone is censoring it.

<!-- PageFooter="Incomplete Data" -->
<!-- PageNumber="195" -->
<!-- PageBreak -->

For the lifelines that are censored, I'll modify end to indicate when they are last
observed and status to indicate that the observation is incomplete:

obs. loc[censored, 'end'] = 8
obs. loc[censored, 'status' ] = 0

Now we can plot a "lifeline" for each dog, showing the arrival and departure times on
a time line:


<figure>

Lifelines showing censored and uncensored observations

0

2

Dog index

4

6

8

1

2

3

4

5

6

7

8

$\mathrm { T i r }$ (weeks)

</figure>


And I'll add one more column to the table, which contains the duration of the
observed parts of the lifelines:

$$\mathrm { o b s } \left\lceil ^ { \prime } T ^ { \prime } \right\rceil = \mathrm { o b s } \left[ ^ { \prime } \mathrm { e n d } ^ { \prime } \right] - \mathrm { o b s } \left[ ^ { \prime } \mathrm { s t a r } t ^ { \prime } \right]$$

What we have simulated is the data that would be available at the beginning of
Week 8.


### Using Incomplete Data

Now, let's see how we can use both kinds of data, complete and incomplete, to infer
the parameters of the distribution of residence times.

First I'll split the data into two sets: data1 contains residence times for dogs whose
arrival and departure times are known; data2 contains incomplete residence times
for dogs who were not adopted during the observation interval.

data1 = obs. loc[~censored, 'T']
data2 = obs. loc[censored, 'T']

For the complete data, we can use update_weibull, which uses the PDF of the Wei-
bull distribution to compute the likelihood of the data.

$$p o s t e r i o r 1 = u p d a t e \_ w e i b u l l \left( p r i o r , d a t a 1 \right)$$

<!-- PageFooter="Chapter 14: Survival Analysis" -->
<!-- PageNumber="196" -->
<!-- PageBreak -->

For the incomplete data, we have to think a little harder. At the end of the observation
interval, we don't know what the residence time will be, but we can put a lower bound
on it; that is, we can say that the residence time will be greater than T.

And that means that we can compute the likelihood of the data using the survival
function, which is the probability that a value from the distribution exceeds T.

The following function is identical to update_weibull except that it uses sf, which
computes the survival function, rather than pdf.

def update_weibull_incomplete(prior, data):
"""Update the prior using incomplete data. """
lam_mesh, k_mesh, data_mesh = np.meshgrid(
prior.columns, prior. index, data)

\# evaluate the survival function
probs = weibull_dist(lam_mesh, k_mesh).sf(data_mesh)
likelihood = probs. prod(axis=2)

posterior = prior * likelihood
normalize(posterior)


#### return posterior

Here's the update with the incomplete data:

posterior2 = update_weibull_incomplete(posterior1, data2)

And here's what the joint posterior distribution looks like after both updates:


<figure>

Posterior joint distribution, incomplete data

5

4

3

$\rightharpoonup$

2

1

2

4

6

8

10

$\mathrm { l a m b d }$

</figure>


Compared to the previous contour plot, it looks like the range of likely values for $\lambda$ is
substantially wider. We can see that more clearly by looking at the marginal
distributions.

<!-- PageFooter="Using Incomplete Data" -->
<!-- PageNumber="197" -->
<!-- PageBreak -->

posterior_lam2 = marginal(posterior2, 0)
posterior_k2 = marginal(posterior2, 1)

Here's the posterior marginal distribution for $\lambda$ compared to the distribution we got
using all complete data:


<figure>

Marginal posterior distribution of $\mathrm { l a m b d a }$

All complete

0.05

Some censored

0.04

PDF

0.03

0.02

0.01

0.00

0

2

4

6

8

10

$\mathrm { l a m b d } \widehat { \mathrm { c } }$

</figure>


The distribution with some incomplete data is substantially wider.

As an aside, notice that the posterior distribution does not come all the way to 0 on
the right side. That suggests that the range of the prior distribution is not wide
enough to cover the most likely values for this parameter. If I were concerned about
making this distribution more accurate, I would go back and run the update again
with a wider prior.

Here's the posterior marginal distribution for $k :$


<figure>
<figcaption>Posterior marginal distribution of $k$</figcaption>

0.08

All complete

Some censored

0.06

PDF

0.04

0.02

0.00

0

1

2

3

4

5

$k$

</figure>


<!-- PageFooter="Chapter 14: Survival Analysis" -->
<!-- PageNumber="198" -->
<!-- PageBreak -->

In this example, the marginal distribution is shifted to the left when we have incom-
plete data, but it is not substantially wider.

In summary, we have seen how to combine complete and incomplete data to estimate
the parameters of a Weibull distribution, which is useful in many real-world scenarios
where some of the data are censored.

In general, the posterior distributions are wider when we have incomplete data,
because less information leads to more uncertainty.

This example is based on data I generated; in the next section we'll do a similar analy-
sis with real data.


### Light Bulbs

In 2007 researchers ran an experiment to characterize the distribution of lifetimes for
light bulbs. Here is their description of the experiment:

An assembly of 50 new Philips (India) lamps with the rating 40 W, 220 V (AC) was
taken and installed in the horizontal orientation and uniformly distributed over a lab
area $1 1 m \times 7 m .$

The assembly was monitored at regular intervals of 12 h to look for failures. The
instants of recorded failures were [recorded] and a total of 32 data points were
obtained such that even the last bulb failed.

We can load the data into a DataFrame like this:

$$d f = p d \cdot r e a d _ { - } c s v \left( ^ { \prime } l a m p s . c s v ^ { \prime } , i n d e x _ { - } c o l = 0 \right)$$

$\mathrm { d f } . \mathrm { h e a d } \left( \right)$

hf $K$


<table>
<tr>
<th>i</th>
<th colspan="3"></th>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>50</td>
</tr>
<tr>
<td>1</td>
<td>840</td>
<td>2</td>
<td>48</td>
</tr>
<tr>
<td>2</td>
<td>852</td>
<td>1</td>
<td>47</td>
</tr>
<tr>
<td>3</td>
<td>936</td>
<td>1</td>
<td>46</td>
</tr>
<tr>
<td>4</td>
<td>960</td>
<td>1</td>
<td>45</td>
</tr>
</table>


Column h contains the times when bulbs failed in hours; Column f contains the
number of bulbs that failed at each time. We can represent these values and frequen-
cies using a Pmf, like this:

<!-- PageFooter="Light Bulbs" -->
<!-- PageNumber="199" -->
<!-- PageBreak -->

<!-- PageHeader="from empiricaldist import Pmf" -->

pmf_bulb = Pmf(df['f']. to_numpy(), df['h'])
pmf_bulb.normalize()
50

Because of the design of this experiment, we can consider the data to be a representa-
tive sample from the distribution of lifetimes, at least for light bulbs that are lit
continuously.

Assuming that these data are well modeled by a Weibull distribution, let's estimate the
parameters that fit the data. Again, I'll start with uniform priors for $\lambda$ and $k :$

lams = np. linspace(1000, 2000, num=51)

$$\left. \mathrm { p r i o r } _ { - } l a n = \text { make_uniform\left(lams, name= lambda^{\prime } \right) }$$
$$k s = n p . l i n s p a c e \left( 1 , 1 0 , n u m = 5 1 \right)$$
$$k = \text { nake } _ { - } \text { uniform } \left( k s , \text { name } = { } ^ { \prime } k ^ { \prime } \right)$$

For this example, there are 51 values in the prior distribution, rather than the usual
101. That's because we are going to use the posterior distributions to do some compu-
tationally intensive calculations. They will run faster with fewer values, but the results
will be less precise.

As usual, we can use make_joint to make the prior joint distribution:

$$\mathrm { p r i o r } \_ \mathrm { b u l b } = \mathrm { m a k e } \_ \mathrm { j o i n t } \left( \mathrm { p r i o r } \_ l a m , \mathrm { p r i o r } \_ \mathrm { k } \right)$$

Although we have data for 50 light bulbs, there are only 32 unique lifetimes in the
dataset. For the update, it is convenient to express the data in the form of 50 lifetimes,
with each lifetime repeated the given number of times. We can use $n p .$ repeat to
transform the data:

data_bulb = np. repeat(df['h' ], df['f'])
len(data_bulb)
50

Now we can use update_weibull to do the update:

posterior_bulb = update_weibull(prior_bulb, data_bulb)

<!-- PageFooter="Chapter 14: Survival Analysis" -->
<!-- PageNumber="200" -->
<!-- PageBreak -->

Here's what the posterior joint distribution looks like:


<figure>

Joint posterior distribution, light bulbs

10

9

8

7

6

$\rightharpoonup$

5

4

3

2

${ } _ { 1 0 0 0 } ^ { 1 + }$

1200

1400

1600

1800

2000

lambda

</figure>


To summarize this joint posterior distribution, we'll compute the posterior mean
lifetime.


## Posterior Means

To compute the posterior mean of a joint distribution, we'll make a mesh that con-
tains the values of $\lambda$ and $k :$

lam_mesh, k_mesh = np.meshgrid(
prior_bulb.columns, prior_bulb. index)

Now for each pair of parameters we'll use weibull_dist to compute the mean:

means = weibull_dist(lam_mesh, k_mesh).mean()
means . shape
(51, 51)

The result is an array with the same dimensions as the joint distribution.

Now we need to weight each mean with the corresponding probability from the joint
posterior:

prod = means * posterior_bulb

Finally we compute the sum of the weighted means:

prod. to_numpy() . sum()
1412.7242774305005

Based on the posterior distribution, we think the mean lifetime is about 1,413 hours.

<!-- PageFooter="Posterior Means" -->
<!-- PageNumber="201" -->
<!-- PageBreak -->

The following function encapsulates these steps:

def joint_weibull_mean(joint):
"""Compute the mean of a joint distribution of Weibulls. """
lam_mesh, k_mesh = np.meshgrid(
joint. columns, joint. index)
means = weibull_dist(lam_mesh, k_mesh).mean()
prod = means * joint
return prod. to_numpy ( ) . sum()


# Posterior Predictive Distribution

Suppose you install 100 light bulbs of the kind in the previous section, and you come
back to check on them after 1,000 hours. Based on the posterior distribution we just
computed, what is the distribution of the number of bulbs you find dead?

If we knew the parameters of the Weibull distribution for sure, the answer would be a
binomial distribution.

For example, if we know that $\lambda = 1 5 5 0$ and $k = 4 . 2 5 ,$ we can use weibull_dist to
compute the probability that a bulb dies before you return:

$\tan = 1 5 5 0$
$k = 4 . 2 5$
$t = 1 0 0 0$

$\mathrm { p r o b } _ { - } \mathrm { d e a d }$ = weibull_dist(lam, k).cdf(t)
prob_dead
0.14381685899960547

If there are 100 bulbs and each has this probability of dying, the number of dead
bulbs follows a binomial distribution.

from utils import $m a k e \_ b i n o m i a l$

$n = 1 0 0$
$p = p r o b _ { - } d e a d$
dist_num_dead = make_binomial(n, p)

But that's based on the assumption that we know $\lambda$ and $k ,$ and we don't. Instead, we
have a posterior distribution that contains possible values of these parameters and
their probabilities.

So the posterior predictive distribution is not a single binomial; instead it is a mixture
of binomials, weighted with the posterior probabilities.

We can use make_mixture to compute the posterior predictive distribution.

It doesn't work with joint distributions, but we can convert the DataFrame that repre-
sents a joint distribution to a Series, like this:

<!-- PageFooter="Chapter 14: Survival Analysis" -->
<!-- PageNumber="202" -->
<!-- PageBreak -->

posterior_series = posterior_bulb. stack()
posterior_series. head()

$k$
lambda

1.0


<table>
<tr>
<td>1000.0</td>
<td>8.146763e-25</td>
</tr>
<tr>
<td>1020.0</td>
<td>1.210486e-24</td>
</tr>
<tr>
<td>1040.0</td>
<td>1.738327e-24</td>
</tr>
<tr>
<td>1060.0</td>
<td>2.418201e-24</td>
</tr>
<tr>
<td>1080.0</td>
<td>3.265549e-24</td>
</tr>
</table>


dtype: float64

The result is a Series with a MultiIndex that contains two "levels": the first level
contains the values of k; the second contains the values of lam.

With the posterior in this form, we can iterate through the possible parameters and
compute a predictive distribution for each pair:

pmf_seq = []
for (k, lam) in posterior_series. index:
prob_dead = weibull_dist(lam, k).cdf(t)
pmf = make_binomial(n, prob_dead)
pmf_seq . append (pmf)

Now we can use make_mixture, passing as parameters the posterior probabilities in
posterior_series and the sequence of binomial distributions in pmf_seq:

from utils import make_mixture

post_pred = make_mixture(posterior_series, pmf_seq)

Here's what the posterior predictive distribution looks like, compared to the binomial
distribution we computed with known parameters:

Posterior predictive distribution


<figure>

known parameters

0.10

unknown parameters

0.08

PMF

0.06

0.04

0.02

0.00

0

20

40

60

80

100

Number of dead bulbs

</figure>


The posterior predictive distribution is wider because it represents our uncertainty
about the parameters as well as our uncertainty about the number of dead bulbs.

<!-- PageFooter="Posterior Predictive Distribution" -->
<!-- PageNumber="203" -->
<!-- PageBreak -->


## Summary

This chapter introduces survival analysis, which is used to answer questions about
the time until an event, and the Weibull distribution, which is a good model for "life-
times" (broadly interpreted) in a number of domains.

We used joint distributions to represent prior probabilities for the parameters of the
Weibull distribution, and we updated them three ways: knowing the exact duration of
a lifetime, knowing a lower bound, and knowing that a lifetime fell in a given interval.

These examples demonstrate a feature of Bayesian methods: they can be adapted to
handle incomplete, or "censored", data with only small changes. As an exercise, you'll
have a chance to work with one more type of censored data, when we are given an
upper bound on a lifetime.

The methods in this chapter work with any distribution with two parameters. In the
exercises, you'll have a chance to estimate the parameters of a two-parameter gamma
distribution, which is used to describe a variety of natural phenomena.

And in the next chapter we'll move on to models with three parameters!


# Exercises


## Exercise 14-1.

Using data about the lifetimes of light bulbs, we computed the posterior distribution
from the parameters of a Weibull distribution, $\lambda$ and $k ,$ and the posterior predictive
distribution for the number of dead bulbs, out of 100, after 1,000 hours.

Now suppose you do the experiment: You install 100 light bulbs, come back after
1,000 hours, and find 20 dead light bulbs. Update the posterior distribution based on
this data. How much does it change the posterior mean?


## Exercise 14-2.

In this exercise, we'll use one month of data to estimate the parameters of $a$ distribu-
tion that describes daily rainfall in Seattle. Then we'll compute the posterior predic-
tive distribution for daily rainfall and use it to estimate the probability of a rare event,
like more than 1.5 inches of rain in a day.

According to hydrologists, the distribution of total daily rainfall (for days with rain) is
well modeled by a two-parameter gamma distribution.

When we worked with the one-parameter gamma distribution in "The Gamma Dis-
tribution" on page 101, we used the Greek letter a for the parameter.

<!-- PageFooter="Chapter 14: Survival Analysis" -->
<!-- PageNumber="204" -->
<!-- PageBreak -->

For the two-parameter gamma distribution, we will use $k$ for the "shape parameter",
which determines the shape of the distribution, and the Greek letter $\theta$ or theta for
the "scale parameter".

I suggest you proceed in the following steps:

1\. Construct a prior distribution for the parameters of the gamma distribution.
Note that $k$ and $\theta$ must be greater than 0.

2\. Use the observed rainfalls to update the distribution of parameters.

3\. Compute the posterior predictive distribution of rainfall, and use it to estimate
the probability of getting more than 1.5 inches of rain in one day.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="205" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 15" -->


# Mark and Recapture

This chapter introduces "mark and recapture" experiments, in which we sample indi-
viduals from a population, mark them somehow, and then take a second sample from
the same population. Seeing how many individuals in the second sample are marked,
we can estimate the size of the population.

Experiments like this were originally used in ecology, but turn out to be useful in
many other fields. Examples in this chapter include software engineering and
epidemiology.

Also, in this chapter we'll work with models that have three parameters, so we'll
extend the joint distributions we've been using to three dimensions.

But first, grizzly bears.


## The Grizzly Bear Problem

In 1996 and 1997 researchers deployed bear traps in locations in British Columbia
and Alberta, Canada, in an effort to estimate the population of grizzly bears. They
describe the experiment in this article.

The "trap" consists of a lure and several strands of barbed wire intended to capture
samples of hair from bears that visit the lure. Using the hair samples, the researchers
use DNA analysis to identify individual bears.

During the first session, the researchers deployed traps at 76 sites. Returning 10 days
later, they obtained 1,043 hair samples and identified 23 different bears. During a sec-
ond 10-day session they obtained 1,191 samples from 19 different bears, where 4 of
the 19 were from bears they had identified in the first batch.

<!-- PageNumber="207" -->
<!-- PageBreak -->

To estimate the population of bears from this data, we need a model for the probabil-
ity that each bear will be observed during each session. As a starting place, we'll make
the simplest assumption, that every bear in the population has the same (unknown)
probability of being sampled during each session.

With these assumptions we can compute the probability of the data for a range of
possible populations.

As an example, let's suppose that the actual population of bears is 100.

After the first session, 23 of the 100 bears have been identified. During the second
session, if we choose 19 bears at random, what is the probability that 4 of them were
previously identified?

I'll define:

· $N :$ actual population size, 100.

· $K :$ number of bears identified in the first session, 23.

· $n :$ number of bears observed in the second session, 19 in the example.

· $k :$ number of bears in the second session that were previously identified, 4.

For given values of $N ,$ $K ,$ and n, the probability of finding $k$ previously-identified
bears is given by the hypergeometric distribution:

$$\binom { K } { k } \binom { N - K } { n - k } / \binom { N } { n }$$

where the binomial coefficient, $\binom { K } { k } ,$ is the number of subsets of size $k$ we can choose
from a population of size $K .$

To understand why, consider:

· The denominator, $\binom { N } { n } ,$ is the number of subsets of $n$ we could choose from a
population of $N$ bears.

· The numerator is the number of subsets that contain $k$ bears from the previously
identified $K$ and $n \quad - \quad k$ from the previously unseen $N \quad - \quad K .$

SciPy provides hypergeom, which we can use to compute this probability for a range
of values of $k :$

import numpy as np

from scipy. stats import hypergeom

$N = 1 0 0$
$K = 2 3$
$n = 1 9$

<!-- PageFooter="Chapter 15: Mark and Recapture" -->
<!-- PageNumber="208" -->
<!-- PageBreak -->

ks = np . arange(12)
ps = hypergeom(N, K, n).pmf(ks)

The result is the distribution of $k$ with given parameters $N ,$ $K ,$ and $n .$ Here's what it
looks like:


<figure>

Hypergeometric distribution of $k$ (known population 100)

0.20

0.15

PMF

0.10

0.05

0.00

0

2

4

6

8

10

Number of bears observed twice

</figure>


The most likely value of $k$ is 4, which is the value actually observed in the experiment.
That suggests that $N = 1 0 0$ is a reasonable estimate of the population, given this data.

We've computed the distribution of $k$ given $N ,$ $K ,$ and $n$ n. Now let's go the other way:
given $K ,$ n, and $k ,$ how can we estimate the total population, $N ?$


### The Update

As a starting place, let's suppose that, prior to this study, an expert estimates that the
local bear population is between 50 and 500, and equally likely to be any value in that
range.

I'll use make_uniform to make a uniform distribution of integers in this range:

import numpy as np
from utils import make_uniform

qs = np.arange(50, 501)
prior_N = make_uniform(qs, name='N' )
prior_N. shape
(451,)

So that's our prior.

<!-- PageFooter="The Update" -->
<!-- PageNumber="209" -->
<!-- PageBreak -->

To compute the likelihood of the data, we can use hypergeom with constants K and n,
and a range of values of $N :$

$$N s = p r i o r \_ N . q s$$
$$K = 2 3$$
$$n = 1 9$$

$k = 4$
likelihood = hypergeom(Ns, K, n).pmf(k)

We can compute the posterior in the usual way:

posterior_N = prior_N * likelihood
posterior_N.normalize()
0.07755224277106727

And here's what it looks like:


<figure>

Posterior distribution of $N$

0.007

0.006

0.005

0.004

PDF

0.003

0.002

0.001

0.000

100

200

300

400

500

Population of bears (N)

</figure>


The most likely value is 109:

posterior_N.max_prob()

109

But the distribution is skewed to the right, so the posterior mean is substantially
higher:

posterior_N.mean()
173.79880627085637

And the credible interval is quite wide:

posterior_N.credible_interval(0.9)
array([ 77., 363.])

<!-- PageFooter="Chapter 15: Mark and Recapture" -->
<!-- PageNumber="210" -->
<!-- PageBreak -->

This solution is relatively simple, but it turns out we can do a little better if we model
the unknown probability of observing a bear explicitly.


## Two-Parameter Model

Next we'll try a model with two parameters: the number of bears, N, and the probabil-
ity of observing a bear, p.

We'll assume that the probability is the same in both rounds, which is probably rea-
sonable in this case because it is the same kind of trap in the same place.

We'll also assume that the probabilities are independent; that is, the probability a bear
is observed in the second round does not depend on whether it was observed in the
first round. This assumption might be less reasonable, but for now it is a necessary
simplification.

Here are the counts again:

$$K = 2 3$$

$$n = 1 9$$

$k = 4$

For this model, I'll express the data in a notation that will make it easier to generalize
to more than two rounds:

· k10 is the number of bears observed in the first round but not the second,

· $k 0 1$ is the number of bears observed in the second round but not the first, and

· k11 is the number of bears observed in both rounds.

Here are their values:

$$k 1 0 = 2 3 \quad - \quad 4$$
$$k \theta 1 = 1 9 - 4$$

k11 = 4

Suppose we know the actual values of $N$ and p. We can use them to compute the likeli-
hood of this data.

For example, suppose we know that $N = 1 0 0$ and $p = 0 . 2 .$ We can use $N$ to compute k00,
which is the number of unobserved bears:

$N = 1 0 0$

$= k \theta 1 + k 1 0 + k 1 1$
k00 = N - observed
k00
62

<!-- PageFooter="Two-Parameter Model" -->
<!-- PageNumber="211" -->
<!-- PageBreak -->

For the update, it will be convenient to store the data as a list that represents the num-
ber of bears in each category:

x = [k00, k01, k10, k11]
☒
$X$
☒

[62, 15, 19, 4]

Now, if we know $p = 0 . 2 ,$ we can compute the probability a bear falls in each category.
For example, the probability of being observed in both rounds is $\mathrm { p } ^ { * } \mathrm { p } ,$ and the proba-
bility of being unobserved in both rounds is $\mathrm { q } ^ { * } \mathrm { q }$ (where $\left. q = 1 - p \right) .$

$P = 0 . 2$
$q = 1 - p$
$y = \left[ q ^ { * } q \right. ,$ $\mathrm { q } ^ { * } \mathrm { p } , \mathrm { p } ^ { * } ,$ p*p]
$y$
[0.6400000000000001,
0.16000000000000003,
0.16000000000000003,
0.04000000000000001]

Now the probability of the data is given by the multinomial distribution:

$$\frac { N ! } { \Pi x _ { i } ! } \prod y _ { i } ^ { x _ { i } }$$

where $N$ is actual population, $x$ is a sequence with the counts in each category, and $y$
is a sequence of probabilities for each category.

SciPy provides multinomial, which provides pmf, which computes this probability.
Here is the probability of the data for these values of $N$ and p:

from scipy. stats import multinomial

likelihood = multinomial.pmf(x, N, y)
☒

likelihood
0.0016664011988507257

That's the likelihood if we know $N$ and p, but of course we don't. So we'll choose prior
distributions for $N$ and $\mathrm { p } ,$ and use the likelihoods to update it.


## The Prior

We'll use prior_N again for the prior distribution of $N ,$ and a uniform prior for the
probability of observing a bear, $\mathrm { p } :$

$$q s = n p . l i n s p a c e \left( 0 , 0 . 9 9 , n u m = 1 0 0 \right)$$
$$p r i o r \_ p = m a k e \_ u n i f o r m \left( q s , n a m e = p \right)$$

<!-- PageFooter="Chapter 15: Mark and Recapture" -->
<!-- PageNumber="212" -->
<!-- PageBreak -->

We can make a joint distribution in the usual way:

from utils import make_joint

joint_prior = make_joint(prior_p, prior_N)
joint_prior . shape
(451, 100)

The result is a pandas DataFrame with values of N down the rows and values of $\mathrm { p }$
across the columns. However, for this problem it will be convenient to represent the
prior distribution as a 1-D Series rather than a 2-D DataFrame. We can convert from
one format to the other using stack:


### from empiricaldist import Pmf

joint_pmf = Pmf(joint_prior. stack())
joint_pmf. head(3)


<table>
<tr>
<th></th>
<th>probs</th>
</tr>
<tr>
<td>N</td>
<td>$d$</td>
</tr>
<tr>
<td rowspan="3">50</td>
<td>0.00 0.000022</td>
</tr>
<tr>
<td>0.01 0.000022</td>
</tr>
<tr>
<td>0.02 0.000022</td>
</tr>
</table>


The result is a Pmf whose index is a MultiIndex. A MultiIndex can have more than
one column; in this example, the first column contains values of $N$ and the second col-
umn contains values of $\mathrm { p } .$

The Pmf has one row (and one prior probability) for each possible pair of parameters
$N$ and p. So the total number of rows is the product of the lengths of prior_N and
prior_p.

Now we have to compute the likelihood of the data for each pair of parameters.


# The Update

To allocate space for the likelihoods, it is convenient to make a copy of joint_pmf:
$= \mathrm { j o i n t } _ { - } \mathrm { c o p y } \left( \mathrm { \left. \right) } \right.$

As we loop through the pairs of parameters, we compute the likelihood of the data as
in the previous section, and then store the result as an element of likelihood:

$$= k \theta 1 + k 1 \theta + k 1 1$$

for $N ,$ p in joint_pmf . index:

$$k \theta \theta = N - \text { observed }$$

x = [k00, k01, k10, k11]

<!-- PageFooter="The Update" -->
<!-- PageNumber="213" -->
<!-- PageBreak -->

$q = 1 - p$
y = [q\*q, q\*p, $\mathrm { p } ^ { * } \mathrm { q } ,$ p*p]
likelihood[N, p] = multinomial.pmf(x, N, y)
☒

Now we can compute the posterior in the usual way:

posterior_pmf = joint_pmf * likelihood
posterior_pmf.normalize()

We'll use plot_contour again to visualize the joint posterior distribution. But
remember that the posterior distribution we just computed is represented as a Pmf,
which is a Series, and plot_contour expects a DataFrame.

Since we used stack to convert from a DataFrame to a Series, we can use unstack to
go the other way:

joint_posterior = posterior_pmf. unstack()

And here's what the result looks like:


<figure>

Joint posterior distribution of N and p

500

450

400

350

300

$Z$

250

200

150

100

50

0.0

0.2

0.4

0.6

0.8

$p$

</figure>


The most likely values of $N$ are near 100, as in the previous model. The most likely
values of $\mathrm { p }$ are near 0.2.

The shape of this contour indicates that these parameters are correlated. If $\mathrm { p }$ is near
the low end of the range, the most likely values of $\mathrm { N }$ are higher; if $\mathrm { p }$ is near the high
end of the range, $N$ is lower.

Now that we have a posterior DataFrame, we can extract the marginal distributions in
the usual way:

from utils import marginal

posterior2_p = marginal(joint_posterior, 0)
posterior2_N = marginal(joint_posterior, 1)

<!-- PageFooter="Chapter 15: Mark and Recapture" -->
<!-- PageNumber="214" -->
<!-- PageBreak -->

Here's the posterior distribution for N based on the two-parameter model, along with
the posterior we got using the one-parameter (hypergeometric) model:


<figure>

Posterior marginal distribution of $N$

0.010

one-parameter model

two-parameter model

0.008

0.006

PDF

0.004

0.002

0.000

100

400

500

$\begin{array}{} { 2 0 0 } \\ { \text { Population of bears } \left( N \right) } \end{array}$

</figure>


With the two-parameter model, the mean is a little lower and the 90% credible inter-
val is a little narrower.


# The Lincoln Index Problem

In an excellent blog post, John D. Cook wrote about the Lincoln index, which is a way
to estimate the number of errors in a document (or program) by comparing results
from two independent testers. Here's his presentation of the problem:

Suppose you have a tester who finds 20 bugs in your program. You want to estimate
how many bugs are really in the program. You know there are at least 20 bugs, and if
you have supreme confidence in your tester, you may suppose there are around 20
bugs. But maybe your tester isn't very good. Maybe there are hundreds of bugs. How
can you have any idea how many bugs there are? There's no way to know with one
tester. But if you have two testers, you can get a good idea, even if you don't know how
skilled the testers are.

Suppose the first tester finds 20 bugs, the second finds 15, and they find 3 in com-
mon; how can we estimate the number of bugs?

This problem is similar to the Grizzly Bear Problem, so I'll represent the data in the
same way:

$$k 1 0 = 2 0 \quad - \quad 3$$
$$k \theta 1 = 1 5 - 3$$

$k 1 1 = 3$

But in this case it is probably not reasonable to assume that the testers have the same
probability of finding a bug. So I'll define two parameters, $p \theta$ for the probability that

<!-- PageFooter="The Lincoln Index Problem" -->
<!-- PageNumber="215" -->
<!-- PageBreak -->

the first tester finds a bug, and p1 for the probability that the second tester finds a
bug.

I will continue to assume that the probabilities are independent, which is like assum-
ing that all bugs are equally easy to find. That might not be a good assumption, but
let's stick with it for now.

As an example, suppose we know that the probabilities are 0.2 and 0.15.

po, $p 1 = 0 . 2 ,$ 0.15

We can compute the array of probabilities, $y ,$ like this:

def compute_probs(p0, p1):
"""Computes the probability for each of 4 categories. """
$q \theta = 1 - p 0$
$q 1 = 1 - p 1$
return $\left[ q \theta ^ { * } q 1 \right. ,$ q0\*p1, $p \theta ^ { * } q 1 ,$ po\*p1]
y = compute_probs(p0, p1)
$y$

[0.68, 0.12, 0.17, 0.03]

With these probabilities, there is a 68% chance that neither tester finds the bug and a
3% chance that both do.

Pretending that these probabilities are known, we can compute the posterior distribu-
tion for $N .$ Here's a prior distribution that's uniform from 32 to 350 bugs:

qs = np.arange(32, 350, step=5)

$$N = \text { make } _ { - } \text { uniform } \left( q s , \text { name } = { } ^ { \prime } N ^ { \prime } \right)$$

prior_N. head(3)

probs

N

32
0.015625

37
0.015625

42
0.015625

I'll put the data in an array, with 0 as a place-keeper for the unknown value k00:

data = np.array([0, k01, k10, k11])

And here are the likelihoods for each value of $N ,$ with ps as a constant:

$= \mathrm { p r i o r } _ { - } \mathrm { N . c o p y } \left( \right)$

$$\mathrm { o b s e r v e d } = \mathrm { d a t a } . \mathrm { s u m } \left( \right)$$
$$x = \mathrm { d a t a } . \mathrm { c o p y } \left( \right)$$

for N in prior_N.qs:

<!-- PageFooter="Chapter 15: Mark and Recapture" -->
<!-- PageNumber="216" -->
<!-- PageBreak -->

x[0] = N - observed
☒
likelihood[N] = multinomial.pmf(x, N, y)
☒

We can compute the posterior in the usual way:

posterior_N = prior_N * likelihood
posterior_N.normalize()
0.0003425201572557094

And here's what it looks like:


<figure>

Posterior marginal distribution of n with known p1, $p 2$

0.14

0.12

0.10

0.08

PMF

0.06

0.04

0.02

0.00

$5 0$

100

150

200

250

300

350

Number of bugs (N)

</figure>


With the assumption that p0 and p1 are known to be 0.2 and 0.15, the posterior
mean is 102 with 90% credible interval (77, 127). But this result is based on the
assumption that we know the probabilities, and we don't.


# Three-Parameter Model

What we need is a model with three parameters: $N ,$ p0, and p1. We'll use prior_N
again for the prior distribution of N, and here are the priors for p0 and p1:

qs = np. linspace(0, 1, num=51)

$$\mathrm { p r i o r } _ { - } \mathrm { p \theta } = \mathrm { m a k e } _ { - } \mathrm { u n i f o r m } \left( \mathrm { q s } , \mathrm { n a m e } = ^ { \prime } \mathrm { p \theta } ^ { \prime } \right)$$
$$p r i o r \_ p 1 = m a k e \_ u n i f o r m \left( q s , n a m e = p 1 \right)$$

Now we have to assemble them into a joint prior with three dimensions. $I ^ { \prime } \Pi$ start by
putting the first two into a DataFrame:

$$\mathrm { j o i n t 2 } = \mathrm { m a k e \_ j o i n t } \left( \mathrm { p r i o r } \_ \mathrm { p \theta } , \mathrm { p r i o r } \_ \mathrm { N } \right)$$

joint2. shape
(64, 51)

<!-- PageFooter="Three-Parameter Model" -->
<!-- PageNumber="217" -->
<!-- PageBreak -->

Now I'll stack them, as in the previous example, and put the result in a Pmf:

joint2_pmf = Pmf(joint2.stack())
joint2_pmf. head(3)


<table>
<tr>
<th></th>
<th></th>
<th>probs</th>
</tr>
<tr>
<td colspan="2">N p0</td>
<td></td>
</tr>
<tr>
<td rowspan="2">32</td>
<td colspan="2">0.00 0.000306</td>
</tr>
<tr>
<td>0.02</td>
<td>0.000306</td>
</tr>
<tr>
<td></td>
<td>0.04</td>
<td>0.000306</td>
</tr>
</table>


We can use make_joint again to add in the third parameter:

joint3 = make_joint(prior_p1, joint2_pmf)
joint3. shape

(3264, 51)

The result is a DataFrame with values of $N$ and $\mathrm { p 0 }$ in a MultiIndex that goes down the
rows and values of p1 in an index that goes across the columns.

Now I'll apply stack again:

joint3_pmf = Pmf(joint3.stack())
joint3_pmf. head(3)

probs


<table>
<tr>
<th>N</th>
<th>p0</th>
<th>p1</th>
<th></th>
</tr>
<tr>
<td rowspan="3">32</td>
<td rowspan="2">0.0</td>
<td colspan="2">0.00 0.000006</td>
</tr>
<tr>
<td colspan="2">0.02 0.000006</td>
</tr>
<tr>
<td></td>
<td colspan="2">0.04 0.000006</td>
</tr>
</table>


The result is a Pmf with a three-column MultiIndex containing all possible triplets of
parameters.

The number of rows is the product of the number of values in all three priors, which
is almost 170,000:

joint3_pmf . shape
(166464,)

That's still small enough to be practical, but it will take longer to compute the likeli-
hoods than in the previous examples.

<!-- PageFooter="Chapter 15: Mark and Recapture" -->
<!-- PageNumber="218" -->
<!-- PageBreak -->

Here's the loop that computes the likelihoods; it's similar to the one in the previous
section:

likelihood = joint3_pmf. copy()
observed = data. sum()
x = data.copy()

for N, p0, p1 in joint3_pmf.index:
x[0] = N - observed
y = compute_probs(p0, p1)
likelihood[N, po, p1] = multinomial.pmf(x, $\left. N , y \right)$
☒

We can compute the posterior in the usual way:

posterior_pmf = joint3_pmf * likelihood
posterior_pmf.normalize()
8.941088283758206e-06

Now, to extract the marginal distributions, we could unstack the joint posterior as we
did in the previous section. But Pmf provides a version of marginal that works with a
Pmf rather than a DataFrame. Here's how we use it to get the posterior distribution for
N:

posterior_N = posterior_pmf.marginal(0)

And here's what it looks like:


<figure>

Posterior marginal distributions of $N$

0.06

0.05

0.04

PDF

0.03

0.02

0.01

0.00

50

100

150

200

250

300

350

Number of bugs (N)

</figure>


105.7656173219623

The posterior mean is 105 bugs, which suggests that there are still many bugs the test-
ers have not found.

<!-- PageFooter="Three-Parameter Model" -->
<!-- PageNumber="219" -->
<!-- PageBreak -->

Here are the posteriors for p0 and p1:


<figure>

Posterior marginal distributions of p1 and p2

0.10

$p l$

$p 2$

0.08

$\frac { 1 } { 6 } 0 . 0 6$

0.04

0.02

0.00

0.0

0.2

0.4

0.6

0.8

1.0

Probability of finding a bug

</figure>


Comparing the posterior distributions, the tester who found more bugs probably has
a higher probability of finding bugs. The posterior means are about 23% and 18%.
But the distributions overlap, so we should not be too sure.

This is the first example we've seen with three parameters. As the number of parame-
ters increases, the number of combinations increases quickly. The method we've been
using so far, enumerating all possible combinations, becomes impractical if the num-
ber of parameters is more than 3 or 4.

However, there are other methods that can handle models with many more parame-
ters, as we'll see in Chapter 19.


## Summary

The problems in this chapter are examples of mark and recapture experiments, which
are used in ecology to estimate animal populations. They also have applications in
engineering, as in the Lincoln Index Problem. And in the exercises you'll see that they
are used in epidemiology, too.

This chapter introduces two new probability distributions:

· The hypergeometric distribution is a variation of the binomial distribution in
which samples are drawn from the population without replacement.

· The multinomial distribution is a generalization of the binomial distribution
where there are more than two possible outcomes.

Also in this chapter, we saw the first example of a model with three parameters. We'll
see more in subsequent chapters.

<!-- PageFooter="Chapter 15: Mark and Recapture" -->
<!-- PageNumber="220" -->
<!-- PageBreak -->


# Exercises


## Exercise 15-1.

In an excellent paper, Anne Chao explains how mark and recapture experiments are
used in epidemiology to estimate the prevalence of a disease in a human population
based on multiple incomplete lists of cases.

One of the examples in that paper is a study "to estimate the number of people who
were infected by hepatitis in an outbreak that occurred in and around $a$ college in
northern Taiwan from April to July 1995."

Three lists of cases were available:

1\. 135 cases identified using a serum test.

2\. 122 cases reported by local hospitals.

3\. 126 cases reported on questionnaires collected by epidemiologists.

In this exercise, we'll use only the first two lists; in the next exercise we'll bring in the
third list.

Make a joint prior and update it using this data, then compute the posterior mean of
N and a 90% credible interval.


## Exercise 15-2.

Now let's do the version of the problem with all three lists. Here's the data from
Chou's paper:


<table>
<caption>Hepatitis A virus list</caption>
<tr>
<th>P</th>
<th>Q</th>
<th>E</th>
<th>Data</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
<td>k111 =28</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>0 ☒</td>
<td>k110 =21</td>
</tr>
<tr>
<td>1</td>
<td>0 ☒</td>
<td>1</td>
<td>k101 =17</td>
</tr>
<tr>
<td>1</td>
<td>0 ☒</td>
<td>0 ☒</td>
<td>k100 =69</td>
</tr>
<tr>
<td>0 ☒</td>
<td>1</td>
<td>1</td>
<td>k011 =18</td>
</tr>
<tr>
<td>0 ☒</td>
<td>1</td>
<td>0 ☒</td>
<td>k010 =55</td>
</tr>
<tr>
<td>0 ☒</td>
<td>0 ☒</td>
<td>1</td>
<td>k001 =63</td>
</tr>
<tr>
<td>0 ☒</td>
<td>0 ☒</td>
<td>0 ☒</td>
<td>k000 $= ? ?$</td>
</tr>
</table>


Write a loop that computes the likelihood of the data for each pair of parameters,
then update the prior and compute the posterior mean of N. How does it compare to
the results using only the first two lists?

<!-- PageFooter="Exercises" -->
<!-- PageNumber="221" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 16" -->


# Logistic Regression

This chapter introduces two related topics: log odds and logistic regression.

In "Bayes's Rule" on page 70, we rewrote Bayes's theorem in terms of odds and
derived Bayes's rule, which can be a convenient way to do a Bayesian update on paper
or in your head. In this chapter, we'll look at Bayes's rule on a logarithmic scale, which
provides insight into how we accumulate evidence through successive updates.

That leads directly to logistic regression, which is based on a linear model of the rela-
tionship between evidence and the log odds of a hypothesis. As an example, we'll use
data from the Space Shuttle to explore the relationship between temperature and the
probability of damage to the O-rings.

As an exercise, you'll have a chance to model the relationship between a child's age
when they start school and their probability of being diagnosed with attention deficit
hyperactivity disorder (ADHD).


## Log Odds

When I was in grad school, I signed up for a class on the Theory of Computation. On
the first day of class, I was the first to arrive. A few minutes later, another student
arrived.

At the time, about 83% of the students in the computer science program were male,
so I was mildly surprised to note that the other student was female.

When another female student arrived a few minutes later, I started to think I was in
the wrong room. When a third female student arrived, I was confident I was in the
wrong room. And as it turned out, I was.

<!-- PageNumber="223" -->
<!-- PageBreak -->

I'll use this anecdote to demonstrate Bayes's rule on a logarithmic scale and show how
it relates to logistic regression.

Using $H$ to represent the hypothesis that I was in the right room, and $F$ to represent
the observation that the first other student was female, we can write Bayes's rule like
this:

$$O \left( H | F \right) = O \left( H \right) \frac { P \left( F | H \right) } { P \left( F | n o t H \right) }$$

Before I saw the other students, I was confident I was in the right room, so I might
assign prior odds of 10:1 in favor:

$$O \left( H \right) = 1 0$$

If I was in the right room, the likelihood of the first female student was about 17%. If
I was not in the right room, the likelihood of the first female student was more like
50%:

$$\frac { P \left( F | H \right) } { P \left( F | n o t H \right) } = 1 7 / 5 0$$

So the likelihood ratio is close to $1 / 3 .$ Applying Bayes's rule, the posterior odds were

$$O \left( H | F \right) = 1 0 / 3$$

After two students, the posterior odds were

$$O \left( H | F F \right) = 1 0 / 9$$

And after three students:

$$O \left( H | F F F \right) = 1 0 / 2 7$$

At that point, I was right to suspect I was in the wrong room.

The following table shows the odds after each $\mathrm { u p d a t e } ,$ the corresponding probabili-
ties, and the change in probability after each step, expressed in percentage points.

<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="224" -->
<!-- PageBreak -->


<table>
<tr>
<th></th>
<th>odds</th>
<th>prob</th>
<th>prob diff</th>
</tr>
<tr>
<td>prior</td>
<td>10.000000</td>
<td>0.909091</td>
<td>--</td>
</tr>
<tr>
<td>1 student</td>
<td>3.333333</td>
<td>0.769231</td>
<td>-13.986014</td>
</tr>
<tr>
<td>2 students</td>
<td>1.111111</td>
<td>0.526316</td>
<td>-24.291498</td>
</tr>
<tr>
<td>3 students</td>
<td>0.370370</td>
<td>0.270270</td>
<td>-25.604552</td>
</tr>
</table>


Each update uses the same likelihood, but the changes in probability are not the
same. The first update decreases the probability by about 14 percentage points, the
second by 24, and the third by 26. That's normal for this kind of update, and in fact
it's necessary; if the changes were the same size, we would quickly get into negative
probabilities.

The odds follow a more obvious pattern. Because each update multiplies the odds by
the same likelihood ratio, the odds form a geometric sequence. And that brings us to
consider another way to represent uncertainty: log odds, which is the logarithm of
odds, usually expressed using the natural log (base e).

Adding log odds to the table:


<table>
<tr>
<th></th>
<th>odds</th>
<th>prob</th>
<th>prob diff</th>
<th>log odds</th>
<th>log odds diff</th>
</tr>
<tr>
<td>prior</td>
<td>10.000000</td>
<td>0.909091</td>
<td>--</td>
<td>2.302585</td>
<td>--</td>
</tr>
<tr>
<td>1 student</td>
<td>3.333333</td>
<td>0.769231</td>
<td>-13.986014</td>
<td>1.203973</td>
<td>-1.098612</td>
</tr>
<tr>
<td>2 students</td>
<td>1.111111</td>
<td>0.526316</td>
<td>-24.291498</td>
<td>0.105361</td>
<td>-1.098612</td>
</tr>
<tr>
<td>3 students</td>
<td>0.370370</td>
<td>0.270270</td>
<td>-25.604552</td>
<td>-0.993252</td>
<td>-1.098612</td>
</tr>
</table>


You might notice:

· When probability is greater than 0.5, odds are greater than 1, and log odds are
positive.

· When probability is less than 0.5, odds are less than 1, and log odds are negative.

You might also notice that the log odds are equally spaced. The change in $\log \mathrm { o d d s }$
after each update is the logarithm of the likelihood ratio.

np. log(1/3)

-1.0986122886681098

That's true in this example, and we can show that it's true in general by taking the log
of both sides of Bayes's rule:

$$\log O \left( H | F \right) = \log O \left( H \right) + \log \frac { P \left( F | H \right) } { P \left( F | n o t H \right) }$$

<!-- PageFooter="Log Odds" -->
<!-- PageNumber="225" -->
<!-- PageBreak -->

On a log odds scale, a Bayesian update is additive. So if $F ^ { x }$ means that $x$ female stu-
dents arrive while I am waiting, the posterior $\log \mathrm { o d d s }$ that I am in the right room are:

$$\log O \left( H | F ^ { x } \right) = \log O \left( H \right) + x \log \frac { P \left( F | H \right) } { P \left( F | n o t H \right) }$$

This equation represents a linear relationship between the log likelihood ratio and the
posterior log odds.

In this example the linear equation is exact, but even when it's not, it is common to
use a $l i n e a r$ function to model the relationship between an explanatory variable, $x ,$
and a dependent variable expressed in log odds, like this:

$$\log O \left( H | x \right) = \beta _ { 0 } + \beta _ { 1 } x$$

where $\beta _ { 0 }$ and $\beta _ { 1 }$ are unknown parameters:

· The intercept, $\beta _ { 0 ^ { 2 } } ,$ is the $\log$ odds of the hypothesis when $x$ is 0.

· The slope, $\beta _ { 1 } ,$ is the $\log$ of the likelihood ratio.

This equation is the basis of logistic regression.


# The Space Shuttle Problem

As an example of logistic regression, I'll solve a problem from Cameron Davidson-
Pilon's book, Bayesian Methods for Hackers. He writes:

On January 28, 1986, the twenty-fifth flight of the US space shuttle program ended in
disaster when one of the rocket boosters of the shuttle Challenger exploded shortly
after lift-off, killing all 7 crew members. The presidential commission on the accident
concluded that it was caused by the failure of an O-ring in a field joint on the rocket
booster, and that this failure was due to a faulty design that made the O-ring unaccept-
ably sensitive to a number of factors including outside temperature. Of the previous 24
flights, data were available on failures of O-rings on 23 (one was lost at sea), and these
data were discussed on the evening preceding the Challenger launch, but unfortunately
only the data corresponding to the 7 flights on which there was a damage incident were
considered important and these were thought to show no obvious trend.

The dataset is originally from this paper, but also available from Davidson-Pilon.

<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="226" -->
<!-- PageBreak -->

Here are the first few rows:


<table>
<tr>
<th></th>
<th>Date</th>
<th>Temperature</th>
<th>Damage</th>
</tr>
<tr>
<td>0</td>
<td>1981-04-12</td>
<td>66</td>
<td>0</td>
</tr>
<tr>
<td>1</td>
<td>1981-11-12</td>
<td>70</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>1982-03-22</td>
<td>69</td>
<td>0</td>
</tr>
<tr>
<td>4</td>
<td>1982-01-11</td>
<td>68</td>
<td>0</td>
</tr>
<tr>
<td>5</td>
<td>1983-04-04</td>
<td>67</td>
<td>0</td>
</tr>
</table>


The columns are:

· Date: The date of launch,

· Temperature: Outside temperature in Fahrenheit (F), and

· Damage: 1 if there was a damage incident and 0 otherwise.

There are 23 launches in the dataset, 7 with damage incidents.

The following figure shows the relationship between damage and temperature:


<figure>

Damage to O-Rings vs Temperature

1.0

☒

☒

☒
data

0.8

Probability of damage

0.6

0.4

0.2

0.0

55

60

65

70

75

80

Outside temperature $\left( \deg F \right)$

</figure>


When the outside temperature was below 65 degrees F, there was always damage to
the O-rings. When the temperature was above 65 degrees F, there was usually no
damage.

Based on this figure, it seems plausible that the probability of damage is related to
temperature. If we assume this probability follows a logistic model, we can write

$$\log O \left( H | x \right) = \beta _ { 0 } + \beta _ { 1 } x$$

<!-- PageFooter="The Space Shuttle Problem" -->
<!-- PageNumber="227" -->
<!-- PageBreak -->

where $H$ is the hypothesis that the O-rings will be damaged, $x$ is temperature, and $\beta _ { 0 }$
and $\beta _ { 1 }$ are the parameters we will estimate. For reasons I'll explain soon, I'll define $x$
to be temperature shifted by an offset so its mean is 0:

offset =
$$\mathrm { d a t a } \left[ ^ { \prime } x ^ { \prime } \right] = \mathrm { d a t a } \left[ ^ { \prime } \right.$$ ☒

70.0

And for consistency I'll create a copy of the Damage columns called y:

$\mathrm { d a t a } \left[ ^ { \prime } y ^ { \prime } \right] = d a t a \left[ ^ { \prime } \text { Damage } ^ { \prime } \right]$

Before doing a Bayesian update, I'll use statsmodels to run a conventional (non-
Bayesian) logistic regression:

import statsmodels. formula. api as smf

formula = 'y ~ x'
results = smf. logit(formula, data=data).fit(disp=False)
results . params

Intercept
-1.208490

x
☒
-0.232163
dtype: float64

results contains a "point estimate" for each parameter, that is, a single value rather
than a posterior distribution.

The intercept is about -1.2, and the estimated slope is about -0.23. To see what these
parameters mean, I'll use them to compute probabilities for a range of temperatures.
Here's the range:

inter = results . params[ ' Intercept' ]

$$\begin{array}{} { \text { slope } = \text { results.params } \left[ x ^ { \prime } \right] } \\ { x s = \text { no. aranae } \left( 5 3 . 8 3 \right) - \text { offset } } \end{array}$$ ☒

We can use the logistic regression equation to compute log odds:

$$\log _ { - } \mathrm { o d d s } = \text { inter } + \text { slope } * x s$$ ☒

And then convert to probabilities:

$$\mathrm { o d d s } = \text { np.exp\left(log_odds\right) }$$
$$p s = o d d s / \left( o d d s + 1 \right)$$

Converting log odds to probabilities is a common enough operation that it has a
name, expit, and SciPy provides a function that computes it:

from scipy. special import expit

ps = expit(inter + slope * xs)

<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="228" -->
<!-- PageBreak -->

Here's what the logistic model looks like with these estimated parameters:


<figure>

Damage to O-Rings vs Temperature

1.0

model

data

0.8

Probability of damage

0.6

0.4

0.2

0.0

55

60

65

70

75

80

Outside temperature (deg F)

</figure>


At low temperatures, the probability of damage is high; at high temperatures, it drops
off to near 0.

But that's based on conventional logistic regression. Now we'll do the Bayesian
version.


# Prior Distribution

I'll use uniform distributions for both parameters, using the point estimates from the
previous section to help me choose the upper and lower bounds:

from utils import make_uniform

qs = np. linspace(-5, 1, num=101)
prior_inter = make_uniform(qs, 'Intercept')
qs = np. linspace(-0.8, 0.1, num=101)
prior_slope = make_uniform(qs, 'Slope')

We can use make_joint to construct the joint prior distribution:

from utils import make_joint

joint = make_joint(prior_inter, prior_slope)

The values of intercept run across the columns, and the values of slope run down
the rows.

For this problem, it will be convenient to "stack" the prior so the parameters are levels
in a MultiIndex:

<!-- PageFooter="Prior Distribution" -->
<!-- PageNumber="229" -->
<!-- PageBreak -->

<!-- PageHeader="from empiricaldist import Pmf" -->

joint_pmf = Pmf(joint. stack())
joint_pmf . head()

probs


<table>
<tr>
<th>Slope</th>
<th>Intercept</th>
</tr>
<tr>
<td rowspan="3">-0.8</td>
<td>-5.00 0.000098</td>
</tr>
<tr>
<td>-4.94 0.000098</td>
</tr>
<tr>
<td>-4.88 0.000098</td>
</tr>
</table>


joint_pmf is a Pmf with two levels in the index, one for each parameter. That makes it
easy to loop through possible pairs of parameters, as we'll see in the next section.


## Likelihood

To do the update, we have to compute the likelihood of the data for each possible pair
of parameters.

To make that easier, I'm going to group the data by temperature, x, and count the
number of launches and damage incidents at each temperature:

$$= \text { data. groupby } \left( { } ^ { \prime } x ^ { \prime } \right) \left[ { } ^ { \prime } y ^ { \prime } \right] . a g g \left( \left[ { } ^ { \prime } c o u n t ^ { \prime } , s u m ^ { \prime } \right] \right)$$ ☒

grouped . head()


<table>
<tr>
<th></th>
<th>count</th>
<th>sum</th>
</tr>
<tr>
<td>$X$ ☒</td>
<td></td>
<td></td>
</tr>
<tr>
<td>-17.0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>-13.0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>-12.0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>-7.0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>-4.0</td>
<td>1</td>
<td>0</td>
</tr>
</table>


The result is a DataFrame with two columns: count is the number of launches at each
temperature; sum is the number of damage incidents. To be consistent with the
parameters of the binomial distributions, I'll assign them to variables named ns and
ks:

$$n s = g r o u p e d \left[ ^ { \prime } c o u n t ^ { \prime } \right]$$
$$k s = g r o u p e d \left[ ^ { \prime } s u m ^ { \prime } \right]$$

To compute the likelihood of the data, let's assume temporarily that the parameters
we just estimated, slope and inter, are correct.

<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="230" -->
<!-- PageBreak -->

We can use them to compute the probability of damage at each launch temperature,
like this:

$$\begin{array}{} { x s = \text { grouped. index } } \\ { n s = \text { exnit } \left( i n t e r + s l o p e * x s \right) } \end{array}$$

ps contains the probability of damage for each launch temperature, according to the
model.

Now, for each temperature we have ns, ps, and ks; we can use the binomial distribu-
tion to compute the likelihood of the data.

from scipy. stats import binom

likes = binom.pmf(ks, ns, ps)
likes

array([0.93924781, 0.85931657, 0.82884484, 0.60268105, 0.56950687,
0.24446388, 0.67790595, 0.72637895, 0.18815003, 0.8419509 ,
0.87045398, 0.15645171, 0.86667894, 0.95545945, 0.96435859,
0.97729671])

Each element of likes is the probability of seeing k damage incidents in n launches if
the probability of damage is p. The likelihood of the whole dataset is the product of
this array:

$$\mathrm { l i k e s } . \mathrm { p r o d } \left( \right)$$

0.0004653644508250066

That's how we compute the likelihood of the data for a particular pair of parameters.
Now we can compute the likelihood of the data for all possible pairs:

$l i k e l i h o o d = j o i n t \_ p m f . c o p y \left( \right)$
for slope, inter in joint_pmf. index:
ps = expit(inter + slope * xs)
likes = binom.pmf(ks, ns, ps)
likelihood[slope, inter] = likes. prod()

To initialize likelihood, we make a copy of joint_pmf, which is a convenient way to
make sure that likelihood has the same type, index, and data type as joint_pmf.

The loop iterates through the parameters. For each possible pair, it uses the logistic
model to compute ps, computes the likelihood of the data, and assigns the result to a
row in likelihood.


## The Update

Now we can compute the posterior distribution in the usual way:

posterior_pmf = joint_pmf * likelihood
posterior_pmf.normalize()

<!-- PageFooter="The Update" -->
<!-- PageNumber="231" -->
<!-- PageBreak -->

If we unstack the posterior Pmf we can make a contour plot of the joint posterior
distribution:


<figure>

Joint posterior distribution

0.1

0.0

-0.1

-0.2

Slope

-0.3

-0.4

-0.5

-0.6

-0.7

-0.8

-5

-4

-3

-2

-1

0

1

Intercept

</figure>


The ovals in the contour plot are aligned along a diagonal, which indicates that there
is some correlation between slope and inter in the posterior distribution.

But the correlation is weak, which is one of the reasons we subtracted off the mean
launch temperature when we computed $x$ x; centering the data minimizes the correla-
tion between the parameters.


### Exercise 16-1.

To see why this matters, go back and set offset=60 and run the analysis again. The
slope should be the same, but the intercept will be different. And if you plot the joint
distribution, the contours you get will be elongated, indicating stronger correlation
between the estimated parameters.

In theory, this correlation is not a problem, but in practice it is. With uncentered data,
the posterior distribution is more spread out, so it's harder to cover with the joint
prior distribution. Centering the data maximizes the precision of the estimates; with
uncentered data, we have to do more computation to get the same precision.


# Marginal Distributions

Finally, we can extract the marginal distributions:

from utils import marginal

marginal_inter = marginal(joint_posterior, 0)
marginal_slope = marginal(joint_posterior, 1)

<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="232" -->
<!-- PageBreak -->

Here's the posterior distribution of inter:


<figure>

Posterior marginal distribution of intercept

intercept

0.035

0.030

0.025

PDF

0.020

0.015

0.010

0.005

0.000

-5

-4

-3

-2

-1

0

1

Intercept

</figure>


And here's the posterior distribution of slope:


<figure>

Posterior marginal distribution of slope

0.030

slope

0.025

0.020

PDF

0.015

0.010

0.005

0.000

-0.8

-0.6

-0.4

-0.2

0.0

Slope

</figure>


# Transforming Distributions

Let's interpret these parameters. Recall that the intercept is the log odds of the
hypothesis when $x$ is 0, which is when temperature is about 70 degrees F (the value of
offset). So we can interpret the quantities in marginal_inter as log odds.

To convert them to probabilities, I'll use the following function, which transforms the
quantities in a Pmf by applying a given function:

<!-- PageFooter="Transforming Distributions" -->
<!-- PageNumber="233" -->
<!-- PageBreak -->

def transform(pmf, func):
"""Transform the quantities in a Pmf. """
ps = pmf. ps
qs = func(pmf.qs)
return Pmf(ps, qs, copy=True)

If we call transform and pass expit as a parameter, it transforms the log odds in
marginal_inter into probabilities and returns the posterior distribution of inter
expressed in terms of probabilities:

$$\mathrm { m a r g i n a l } \_ \mathrm { p r o b s } = \mathrm { t r a n s f o r m } \left( \mathrm { m a r g i n a l } _ { - } \mathrm { i n t e r } , \mathrm { e x p i t t } \right)$$

Pmf provides a transform method that does the same thing:

$$\mathrm { m a r g i n a l } \_ \mathrm { p r o b s } = \mathrm { m a r g i n a l } _ { - } \mathrm { i n t e r } . \mathrm { t r a n s f o r m } \left( \mathrm { e x p i t } \right)$$

Here's the posterior distribution for the probability of damage at 70 degrees F:


<figure>

Posterior marginal distribution of probabilities

0.035

0.030

0.025

PDF

0.020

0.015

0.010

0.005

0.000

0.0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

Probability of damage at 70 deg F

</figure>


The mean of this distribution is about 22%, which is the probability of damage at 70
degrees $\mathrm { F } ,$ according to the model.

This result shows the second reason I defined $x$ to be zero when temperature is 70
degrees F; this way, the intercept corresponds to the probability of damage at a rele-
vant temperature, rather than 0 degrees F.

Now let's look more closely at the estimated slope. In the logistic model, the parame-
ter $\beta _ { 1 }$ is the $\log$ of the likelihood ratio.

So we can interpret the quantities in marginal_slope as log likelihood ratios, and we
can use exp to transform them to likelihood ratios (also known as Bayes factors):

marginal_lr = marginal_slope. transform(np.exp)

<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="234" -->
<!-- PageBreak -->

The result is the posterior distribution of likelihood ratios; here's what it looks like:


<figure>

Posterior marginal distribution of likelihood ratios

0.030

0.025

0.020

PDF

0.015

0.010

0.005

0.000

0.5

0.6

1.0

1.1

$\begin{array}{} { 0 . 7 } & { 0 . 8 } & { 0 . 9 } \\ { \text { Likelihood ratio of } 1 } & { \text { deg } F } \end{array}$

</figure>


The mean of this distribution is about 0.75, which means that each additional degree
Fahrenheit provides evidence against the possibility of damage, with a likelihood
ratio (Bayes factor) of 0.75.

Notice:

· I computed the posterior mean of the probability of damage at 70 degrees $\mathrm { F }$ by
transforming the marginal distribution of the intercept to the marginal distribu-
tion of probability, and then computing the mean.

· I computed the posterior mean of the likelihood ratio by transforming the
marginal distribution of slope to the marginal distribution of likelihood ratios,
and then computing the mean.

This is the correct order of operations, as opposed to computing the posterior means
first and then transforming them.


# Predictive Distributions

In the logistic model, the parameters are interpretable, at least after transformation.
But often what we care about are predictions, not parameters. In the Space Shuttle
Problem, the most important prediction is, "What is the probability of O-ring dam-
age if the outside temperature is 31 degrees F?"

To make that prediction, I'll draw a sample of parameter pairs from the posterior
distribution:

sample = posterior_pmf . choice(101)

<!-- PageFooter="Predictive Distributions" -->
<!-- PageNumber="235" -->
<!-- PageBreak -->

The result is an array of 101 tuples, each representing a possible pair of parameters. I
chose this sample size to make the computation fast. Increasing it would not change
the results much, but they would be a little more precise.

To generate predictions, I'll use a range of temperatures from 31 degrees $\mathrm { F }$ (the tem-
perature when the Challenger launched) to 82 degrees $\mathrm { F }$ (the highest observed tem-
perature):

temps = np. arange(31, 83)
xs = temps - offset

The following loop uses xs and the sample of parameters to construct an array $\mathrm { o f } p \mathrm { r } e$
dicted probabilities:

pred = np.empty((len(sample), len(xs)))

for i, (slope, inter) in enumerate(sample):
pred[i] = expit(inter + slope * xs)

The result has one column for each value in xs and one row for each element of
sample.

In each column, I'll compute the median to quantify the central tendency and a 90%
credible interval to quantify the uncertainty.

np. percentile computes the given percentiles; with the argument $a \times i s = 0 ,$ it com-
putes them for each column:

low, median, high = np. percentile(pred, [5, 50, 95], axis=0)

The results are arrays containing predicted probabilities for the lower bound of the
90% CI, the median, and the upper bound of the CI.

Here's what they look like:


<figure>
<figcaption>Damage to O-Rings vs Temperature</figcaption>

1.0

0.8

Probability of damage

0.6

0.4

0.2

logistic model

0.0

data

30

40

50

60

70

80

Outside temperature (deg F)

</figure>


<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="236" -->
<!-- PageBreak -->

According to these results, the probability of damage to the O-rings at 80 degrees $\mathrm { F }$ is
near 2%, but there is some uncertainty about that prediction; the upper bound of the
CI is around 10%.

At 60 degrees $\mathrm { F } ,$ the probability of damage is near 80%, but the CI is even wider, from
48% to 97%.

But the primary goal of the model is to predict the probability of damage at 31
degrees F, and the answer is at least 97%, and more likely to be more than 99.9%.

One conclusion we might draw is this: if the people responsible for the Challenger
launch had taken into account all of the data, and not just the seven damage inci-
dents, they could have predicted that the probability of damage at 31 degrees F was
nearly certain. If they had, it seems likely they would have postponed the launch.

At the same time, if they considered the previous figure, they might have realized that
the model makes predictions that extend far beyond the data. When we extrapolate
like that, we have to remember not just the uncertainty quantified by the model,
which we expressed as a credible interval; we also have to consider the possibility that
the model itself is unreliable.

This example is based on a logistic model, which assumes that each additional degree
of temperature contributes the same amount of evidence in favor of (or against) the
possibility of damage. Within a narrow range of temperatures, that might be a rea-
sonable assumption, especially if it is supported by data. But over a wider range, and
beyond the bounds of the data, reality has no obligation to stick to the model.


## Empirical Bayes

In this chapter I used statsmodels to compute the parameters that maximize the
probability of the data, and then used those estimates to choose the bounds of the
uniform prior distributions. It might have occurred to you that this process uses the
data twice, once to choose the priors and again to do the update. If that bothers you,
you are not alone. The process I used is an example of what's called the Empirical
Bayes method, although I don't think that's a particularly good name for it.

Although it might seem problematic to use the data twice, in these examples, it is not.
To see why, consider an alternative: instead of using the estimated parameters to
choose the bounds of the prior distribution, I could have used uniform distributions
with much wider ranges. In that case, the results would be the same; the only differ-
ence is that I would spend more time computing likelihoods for parameters where
the posterior probabilities are negligibly small.

<!-- PageFooter="Empirical Bayes" -->
<!-- PageNumber="237" -->
<!-- PageBreak -->

So you can think of this version of Empirical Bayes as an optimization that minimizes
computation by putting the prior distributions where the likelihood of the data is
worth computing. This optimization doesn't affect the results, so it doesn't "double-
count" the data.


# Summary

So far we have seen three ways to represent degrees of confidence in a hypothesis:
probability, odds, and log odds. When we write Bayes's rule in terms of log odds, a
Bayesian update is the sum of the prior and the likelihood; in this sense, Bayesian sta-
tistics is the arithmetic of hypotheses and evidence.

This form of Bayes's theorem is also the foundation of logistic regression, which we
used to infer parameters and make predictions. In the Space Shuttle Problem, we
modeled the relationship between temperature and the probability of damage, and
showed that the Challenger disaster might have been predictable. But this example is
also a warning about the hazards of using a model to extrapolate far beyond the data.

In the exercises below you'll have a chance to practice the material in this chapter,
using log odds to evaluate a political pundit and using logistic regression to model
diagnosis rates for attention deficit hyperactivity disorder (ADHD).

In the next chapter we'll move from logistic regression to linear regression, which we
will use to model changes over time in temperature, snowfall, and the marathon
world record.


# More Exercises


## Exercise 16-2.

Suppose a political pundit claims to be able to predict the outcome of elections, but
instead of picking a winner, they give each candidate a probability of winning. With
that kind of prediction, it can be hard to say whether it is right or wrong.

For example, suppose the pundit says that Alice has a 70% chance of beating Bob, and
then Bob wins the election. Does that mean the pundit was wrong?

One way to answer this question is to consider two hypotheses:

· $H :$ The pundit's algorithm is legitimate; the probabilities it produces are correct in
the sense that they accurately reflect the candidates' probabilities of winning.

· not H: The pundit's algorithm is bogus; the probabilities it produces are random
values with a mean of 50%.

<!-- PageFooter="Chapter 16: Logistic Regression" -->
<!-- PageNumber="238" -->
<!-- PageBreak -->

If the pundit says Alice has a 70% chance of winning, and she does, that provides evi-
dence in favor of $\mathrm { H }$ with likelihood ratio 70/50.

If the pundit says Alice has a 70% chance of winning, and she loses, that's evidence
against $H$ with a likelihood ratio of 50/30.

Suppose we start with some confidence in the algorithm, so the prior odds are 4 to 1.
And suppose the pundit generates predictions for three elections:

· In the first election, the pundit says Alice has a 70% chance of winning and she
does.

· In the second election, the pundit says Bob has a 30% chance of winning and he
does.

· In the third election, the pundit says Carol has a 90% chance of winning and she
does.

What is the log likelihood ratio for each of these outcomes? Use the log-odds form of
Bayes's rule to compute the posterior log odds for $\mathrm { H }$ after these outcomes. In total, do
these outcomes increase or decrease your confidence in the pundit?

If you are interested in this topic, you can read more about it in this blog post.


## Exercise 16-3.

An article in the New England Journal of Medicine reports results from a study that
looked at the diagnosis rate of attention deficit hyperactivity disorder (ADHD) as a
function of birth month: "Attention Deficit-Hyperactivity Disorder and Month of
School Enrollment".

They found that children born in June, July, and August were substantially more
likely to be diagnosed with ADHD, compared to children born in September, but
only in states that use a September cutoff for children to enter kindergarten. In these
states, children born in August start school almost a year younger than children born
in September. The authors of the study suggest that the cause is "age-based variation
in behavior that may be attributed to ADHD rather than to the younger age of the
children".

Use the methods in this chapter to estimate the probability of diagnosis as a function
of birth month. The notebook for this chapter provides the data and some sugges-
tions for getting started.

<!-- PageFooter="More Exercises" -->
<!-- PageNumber="239" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 17" -->


# Regression

In the previous chapter we saw several examples of logistic regression, which is based
on the assumption that the likelihood of an outcome, expressed in the form of log
odds, is a linear function of some quantity (continuous or discrete).

In this chapter we'll work on examples of simple linear regression, which models the
relationship between two quantities. Specifically, we'll look at changes over time in
snowfall and the marathon world record.

The models we'll use have three parameters, so you might want to review the tools we
used for the three-parameter model in Chapter 15.


## More Snow?

I am under the impression that we don't get as much snow around here as we used to.
By "around here" I mean Norfolk County, Massachusetts, where I was born, grew up,
and currently live. And by "used to" I mean compared to when I was young, like in
1978 when we got 27 inches of snow and I didn't have to go to school for a couple of
weeks.

Fortunately, we can test my conjecture with data. Norfolk County happens to be the
location of the Blue Hill Meteorological Observatory, which keeps the oldest continu-
ous weather record in North America.

Data from this and many other weather stations is available from the National Oce-
anic and Atmospheric Administration (NOAA). I collected data from the Blue Hill
Observatory from May 11, 1967 to May 11, 2020.

<!-- PageNumber="241" -->
<!-- PageBreak -->

We can use pandas to read the data into DataFrame:

import pandas as pd

$$d f = p d \cdot r e a d _ { - } c s v \left( ^ { \prime } 2 2 3 9 \theta 7 5 . c s v ^ { \prime } , p a r s e _ { - } d a t e s = \left[ 2 \right] \right)$$

The columns we'll use are:

· DATE, which is the date of each observation,

· SNOW, which is the total snowfall in inches.

I'll add a column that contains just the year part of the dates:

$\mathrm { d f } \left[ ^ { \prime } \mathrm { Y E A R } ^ { \prime } \right] = \mathrm { d f } \left[ ^ { \prime } \mathrm { D A T E } ^ { \prime } \right] . \mathrm { d t } . \mathrm { y e a r }$

And use groupby to add up the total snowfall in each year:

$$= d f . g r o u p b y \left( ^ { \prime } Y E A R ^ { \prime } \right) \left[ ^ { \prime } S N o l v ^ { \prime } \right] . s u m \left( \right)$$

The following figure shows total snowfall during each of the complete years in my
lifetime:


<figure>

Total annual snowfall in Norfolk County, MA

140

☒
SNOW

☒

Total annual snowfall (inches)

120

☒

☒

☒

100

☒

☒

☒

☒

☒

☒

☒

80

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

60

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

40

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

☒

20

☒

☒

1970

1980

1990

2000

2010

2020

Year

</figure>


Looking at this plot, it's hard to say whether snowfall is increasing, decreasing, or
unchanged. In the last decade, we've had several years with more snow than 1978,
including 2015, which was the snowiest winter in the Boston area in modern history,
with a total of 141 inches.

This kind of question-looking at noisy data and wondering whether it is going up or
down-is precisely the question we can answer with Bayesian regression.

<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="242" -->
<!-- PageBreak -->


## Regression Model

The foundation of regression (Bayesian or not) is the assumption that a time series
like this is the sum of two parts:

1\. A linear function of time, and

2\. A series of random values drawn from a distribution that is not changing over
time.

Mathematically, the regression model is

$$y = a x + b +$$

where $y$ is the series of measurements (snowfall in this example), $x$ is the series of
times (years) and $\epsilon$ is the series of random values.

a and $b$ are the slope and intercept of the line through the data. They are unknown
parameters, so we will use the data to estimate them.

We don't know the distribution of e, so we'll make the additional assumption that it is
a normal distribution with mean 0 and unknown standard deviation, $\sigma .$

To see whether this assumption is reasonable, I'll plot the distribution of total snow-
fall and a normal model with the same mean and standard deviation.

Here's a Pmf object that represents the distribution of snowfall:

from empiricaldist import Pmf

pmf_snowfall = Pmf. from_seq(snow)

And here are the mean and standard deviation of the data:

mean, std = pmf_snowfall.mean(), pmf_snowfall.std()
mean, std
(64.19038461538462, 26.288021984395684)

I'll use the norm object from SciPy to compute the CDF of a normal distribution with
the same mean and standard deviation:

from scipy. stats import norm

dist = norm(mean, std)
qs = pmf_snowfall. qs

$$p s = d i s t . c d f \left( q s \right)$$

<!-- PageFooter="Regression Model" -->
<!-- PageNumber="243" -->
<!-- PageBreak -->

Here's what the distribution of the data looks like compared to the normal model:


<figure>

Normal model of variation in snowfall

1.0

model

data

0.8

0.6

$\frac { 4 } { 8 }$

0.4

0.2

0.0

20

40

60

80

100

120

140

Total snowfall (inches)

</figure>


We've had more winters below the mean than expected, but overall this looks like a
reasonable model.


## Least Squares Regression

Our regression model has three parameters: slope, intercept, and standard deviation
of e. Before we can estimate them, we have to choose priors. To help with that, I'll use
statsmodels to fit a line to the data by least squares regression.

First, I'll use reset_index to convert snow, which is a Series, to a DataFrame:

data = snow.reset_index()
data. head(3)

YEAR
SNOW


<table>
<tr>
<td>0</td>
<td>1968</td>
<td>44.7</td>
</tr>
<tr>
<td>1</td>
<td>1969</td>
<td>99.2</td>
</tr>
<tr>
<td>2</td>
<td>1970</td>
<td>66.8</td>
</tr>
</table>


The result is a DataFrame with two columns, YEAR and SNOW, in a format we can use
with statsmodels.

As we did in the previous chapter, I'll center the data by subtracting off the mean:

offset = data['YEAR' ]. mean() . round()
data[ 'x' ] = data['YEAR' ] - offset
☒
offset
1994.0

<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="244" -->
<!-- PageBreak -->

And I'll add a column to data so the dependent variable has a standard name:

$$\mathrm { d a t a } \left[ ^ { \prime } y ^ { \prime } \right] = \mathrm { d a t a } \left[ ^ { \prime } \mathrm { S N O W } ^ { \prime } \right]$$

Now, we can use statsmodels to compute the least squares fit to the data and esti-
mate slope and intercept:

import statsmodels. formula. api as smf

formula = 'y ~ x'
results = smf . ols(formula, data=data).fit()

results . params

Intercept
64.446325

x
☒
0.511880

dtype: float64

The intercept, about 64 inches, is the expected snowfall when $x = 0 ,$ which is the begin-
ning of 1994. The estimated slope indicates that total snowfall is increasing at a rate of
about 0.5 inches per year.

results also provides resid, which is an array of residuals, that is, the differences
between the data and the fitted line. The standard deviation of the residuals is an esti-
mate of sigma:

results.resid.std()

25.385680731210616

We'll use these estimates to choose prior distributions for the parameters.


### Priors

I'll use uniform distributions for all three parameters:

import numpy as np
from utils import make_uniform

qs = np. linspace(-0.5, 1.5, 51)
prior_slope = make_uniform(qs, 'Slope')

qs = np. linspace(54, 75, 41)
prior_inter = make_uniform(qs, 'Intercept')
qs = np. linspace(20, 35, 31)
prior_sigma = make_uniform(qs, 'Sigma')

I made the prior distributions different lengths for two reasons. First, if we make a
mistake and use the wrong distribution, it will be easier to catch the error if they are
all different lengths.

Second, it provides more precision for the most important parameter, slope, and
spends less computational effort on the least important, sigma.

<!-- PageFooter="Priors" -->
<!-- PageNumber="245" -->
<!-- PageBreak -->

In "Three-Parameter Model" on page 217 we made a joint distribution with three
parameters. I'll wrap that process in a function:

from utils import make_joint

def make_joint3(pmf1, pmf2, pmf3):
"""Make a joint distribution with three parameters. """
joint2 = make_joint(pmf2, pmf1).stack()
joint3 = make_joint(pmf3, joint2). stack()
return Pmf(joint3)

And use it to make a Pmf that represents the joint distribution of the three
parameters:

prior = make_joint3(prior_slope, prior_inter, prior_sigma)
prior.head(3)

probs


<table>
<tr>
<th>Slope</th>
<th>Intercept</th>
<th>Sigma</th>
</tr>
<tr>
<td rowspan="2">-0.5</td>
<td>54.0</td>
<td>20.0 0.000015</td>
</tr>
<tr>
<td></td>
<td>20.5 0.000015</td>
</tr>
<tr>
<td></td>
<td></td>
<td>21.0 0.000015</td>
</tr>
</table>


The index of Pmf has three columns, containing values of slope, inter, and sigma, in
that order.

With three parameters, the size of the joint distribution starts to get big. Specifically,
it is the product of the lengths of the prior distributions. In this example, the prior
distributions have 51, 41, and 31 values, so the length of the joint prior is 64,821.


#### Likelihood

Now we'll compute the likelihood of the data. To demonstrate the process, let's
assume temporarily that the parameters are known.

$$i n t e r = 6 4$$
$$s l o p e = 0 . 5 1$$

$s i g m a = 2 5$

I'll extract the $x s$ and ys from data as Series objects:

$$x s = \mathrm { d a t a } \left[ ^ { \prime } x ^ { \prime } \right]$$
$$y s = \mathrm { d a t a } \left[ \begin{array}{} { 1 } & { y } \end{array} \right]$$ ☒ ☒

And compute the "residuals", which are the differences between the actual values, $y s ,$
and the values we expect based on slope and inter:

expected = slope * xs + inter
resid = ys - expected

<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="246" -->
<!-- PageBreak -->

According to the model, the residuals should follow a normal distribution with mean
0 and standard deviation sigma. So we can compute the likelihood of each residual
value using norm from SciPy:

$$d e n s i t i e s = n o r m \left( 0 , s i g m a \right) . p d f \left( r e s i d \right)$$

The result is an array of probability densities, one for each element of the dataset;
their product is the likelihood of the data.

$$= \mathrm { d e n s i t i e s . p r o d } \left( \right)$$

likelihood

1.3551948769061074e-105

As we saw in the previous chapter, the likelihood of any particular dataset tends to be
small. If it's too small, we might exceed the limits of floating-point arithmetic. When
that happens, we can avoid the problem by computing likelihoods under a log trans-
form. But in this example that's not necessary.


#### The Update

Now we're ready to do the update. First, we need to compute the likelihood of the
data for each possible set of parameters:

likelihood = prior. copy()

for slope, inter, sigma in prior. index:
expected = slope * xs + inter
resid = ys - expected
densities = norm.pdf(resid, 0, sigma)
likelihood[slope, inter, sigma] = densities.prod()

This computation takes longer than many of the previous examples. We are
approaching the limit of what we can do with grid approximations.

Nevertheless, we can do the update in the usual way:

posterior = prior * likelihood
posterior.normalize()

The result is a Pmf with a three-level index containing values of slope, inter, and
sigma. To get the marginal distributions from the joint posterior, we can use
Pmf.marginal, which we saw in "Three-Parameter Model" on page 217:

posterior_slope = posterior.marginal(0)
posterior_inter = posterior.marginal(1)
posterior_sigma = posterior.marginal(2)

<!-- PageFooter="The Update" -->
<!-- PageNumber="247" -->
<!-- PageBreak -->

Here's the posterior distribution for sigma:


<figure>

Posterior marginal distribution of $o$

0.08

0.07

0.06

0.05

PDF

0.04

0.03

0.02

0.01

0.00

20

22

24

26

28

30

32

34

$o ,$ standard deviation of $\varepsilon$

</figure>


The most likely values for sigma are near 26 inches, which is consistent with our esti-
mate based on the standard deviation of the data.

However, to say whether snowfall is increasing or decreasing, we don't really care
about sigma. It is a "nuisance parameter", so-called because we have to estimate it as
part of the model, but we don't need it to answer the questions we are interested in.

Nevertheless, it is good to check the marginal distributions to make sure

· The location is consistent with our expectations, and

· The posterior probabilities are near 0 at the extremes of the range, which
indicates that the prior distribution covers all parameters with non-negligible
probability.

In this example, the posterior distribution of sigma looks fine.

<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="248" -->
<!-- PageBreak -->

Here's the posterior distribution of inter:


<figure>

Posterior marginal distribution of intercept

0.06

0.05

0.04

PDF

0.03

0.02

0.01

0.00

55

60

65

70

$7 5$

intercept (inches)

</figure>


The posterior mean is about 64 inches, which is the expected amount of snow during
the year at the midpoint of the range, 1994.

And finally, here's the posterior distribution of slope:


<figure>

Posterior marginal distribution of slope

0.06

0.05

0.04

PDF

0.03

0.02

0.01

0.00

-0.50

-0.25

0.00

0.25

0.50

0.75

1.00

1.25

1.50

Slope (inches per year)

</figure>


The posterior mean is about 0.51 inches, which is consistent with the estimate we got
from least squared regression.

The 90% credible interval is from 0.1 to 0.9, which indicates that our uncertainty
about this estimate is pretty high. In fact, there is still a small posterior probability
(about 2%) that the slope is negative.

<!-- PageFooter="The Update" -->
<!-- PageNumber="249" -->
<!-- PageBreak -->

However, it is more likely that my conjecture was wrong: we are actually getting more
snow around here than we used to, increasing at a rate of about a half-inch per year,
which is substantial. On average, we get an additional 25 inches of snow per year than
we did when I was young.

This example shows that with slow-moving trends and noisy data, your instincts can
be misleading.

Now, you might suspect that I overestimate the amount of snow when I was young
because I enjoyed it, and underestimate it now because I don't. But you would be
mistaken.

During the Blizzard of 1978, we did not have a snowblower and my brother and I had
to shovel. My sister got a pass for no good reason. Our driveway was about 60 feet
long and three cars wide near the garage. And we had to shovel Mr. Crocker's drive-
way, too, for which we were not allowed to accept payment. Furthermore, as I recall it
was during this excavation that I accidentally hit my brother with a shovel on the
head, and it bled a lot because, you know, scalp wounds.

Anyway, the point is that I don't think I overestimate the amount of snow when I was
young because I have fond memories of it.


##### Marathon World Record

For many running events, if you plot the world record pace over time, the result is a
remarkably straight line. People, including me, have speculated about possible rea-
sons for this phenomenon.

People have also speculated about when, if ever, the world record time for the mara-
thon will be less than two hours. (Note: In 2019, Eliud Kipchoge ran the marathon
distance in under two hours, which is an astonishing achievement that I fully appreci-
ate, but for several reasons it did not count as a world record.)

So, as a second example of Bayesian regression, we'll consider the world record pro-
gression for the marathon (for male runners), estimate the parameters of a linear
model, and use the model to predict when a runner will break the two-hour barrier.

In the notebook for this chapter, you can see how I loaded and cleaned the data. The
result $i s \quad a$ DataFrame that contains the following columns (and additional informa-
tion we won't use):

· date, which is a pandas Timestamp representing the date when the world record
was broken, and

· speed, which records the record-breaking pace in mph.

<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="250" -->
<!-- PageBreak -->

Here's what the results look like, starting in 1970:


<figure>

13.0

12.8

Speed (mph)

☒

☒

12.6

☒

12.4

☒

☒

12.2

☒

☒

☒ ☒

World record speed

$1 9 7 0$

1980

1990

2000

2010

2020

Date

</figure>


The data points fall approximately on a line, although it's possible that the slope is
increasing.

To prepare the data for regression, I'll subtract away the approximate midpoint of the
time interval, 1995:

offset = pd. to_datetime('1995')
timedelta = table['date'] - offset

When we subtract two Timestamp objects, the result is a "time delta", which we can
convert to seconds and then to years:

data['x'] = timedelta.dt. total_seconds() / 3600 / 24 / 365.24
☒

As in the previous example, I'll use least squares regression to compute point esti-
mates for the parameters, which will help with choosing priors:

import statsmodels. formula. api as smf

$= ^ { \prime } y \sim x ^ { \prime }$
results = smf. ols(formula, data=data).fit()
results . params

Intercept
12.460507

x
☒
0.015464
dtype: float64

The estimated intercept is about 12.5 mph, which is the interpolated world record
pace for 1995. The estimated slope is about 0.015 mph per year, which is the rate the
world record pace is increasing, according to the model.

<!-- PageFooter="Marathon World Record" -->
<!-- PageNumber="251" -->
<!-- PageBreak -->

Again, we can use the standard deviation of the residuals as a point estimate for
sigma:

results.resid.std()
0.04139961220193225

These parameters give us a good idea where we should put the prior distributions.


#### The Priors

Here are the prior distributions I chose for slope, intercept, and sigma:

qs = np. linspace(0.012, 0.018, 51)
prior_slope = make_uniform(qs, 'Slope')
qs = np. linspace(12.4, 12.5, 41)
prior_inter = make_uniform(qs, 'Intercept')
qs = np. linspace(0.01, 0.21, 31)
prior_sigma = make_uniform(qs, 'Sigma')

And here's the joint prior distribution:

prior = make_joint3(prior_slope, prior_inter, prior_sigma)
prior. head()

probs


<table>
<tr>
<th>Slope</th>
<th>Intercept</th>
<th>Sigma</th>
<th></th>
</tr>
<tr>
<td rowspan="2">0.012</td>
<td>12.4</td>
<td>0.010000</td>
<td>0.000015</td>
</tr>
<tr>
<td></td>
<td colspan="2">0.016667 0.000015</td>
</tr>
<tr>
<td></td>
<td></td>
<td colspan="2">0.023333 0.000015</td>
</tr>
</table>


Now we can compute likelihoods as in the previous example:

$x s = \mathrm { d a t a } \left[ ^ { \prime } x ^ { \prime } \right]$
☒
$y s = \mathrm { d a t a } \left[ \begin{array}{} { 1 } & { y } \end{array} \right]$
☒
$l i k e l i h o o d = p r i o r . c o p y \left( \right)$

for slope, inter, sigma in prior. index:
expected = slope * xs + inter
resid = ys - expected
densities = norm.pdf(resid, 0, sigma)
likelihood[slope, inter, sigma] = densities. prod()
Now we can do the update in the usual way:

posterior = prior * likelihood
posterior.normalize()
And unpack the marginals:

<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="252" -->
<!-- PageBreak -->

posterior_slope = posterior.marginal(0)
posterior_inter = posterior.marginal(1)
posterior_sigma = posterior.marginal(2)

Here's the posterior distribution of inter:

Posterior marginal distribution of intercept


<figure>

0.08

0.06

PDF

0.04

0.02

0.00

12.40

$1 2 . 4 2$

12.44

12.46

12.48

12.50

intercept

</figure>


The posterior mean is about 12.5 mph, which is the world record marathon pace the
model predicts for the midpoint of the date range, 1994.

And here's the posterior distribution of slope:

Posterior marginal distribution of slope


<figure>

0.07

0.06

0.05

0.04

PDF

0.03

0.02

0.01

0.00

0.012

0.013

0.014

0.015

0.016

0.017

0.018

Slope

</figure>


The posterior mean is about 0.015 mph per year, or 0.15 mph per decade.

That's interesting, but it doesn't answer the question we're interested in: when will
there be a two-hour marathon? To answer that, we have to make predictions.

<!-- PageFooter="The Priors" -->
<!-- PageNumber="253" -->
<!-- PageBreak -->


# Prediction

To generate predictions, I'll draw a sample from the posterior distribution of parame-
ters, then use the regression equation to combine the parameters with the data.

Pmf provides choice, which we can use to draw a random sample with replacement,
using the posterior probabilities as weights:

$$s a m p l e = p o s t e r i o r . c h o i c e \left( 1 0 1 \right)$$

The result is an array of tuples. Looping through the sample, we can use the regres-
sion equation to generate predictions for a range of $x s :$

xs = np. arange(-25, 50, 2)
pred = np.empty((len(sample), len(xs)))

for i, (slope, inter, sigma) in enumerate(sample):
epsilon = norm(0, sigma).rvs(len(xs))
pred[i] = inter + slope * xs + epsilon

Each prediction is an array with the same length as xs, which I store as a row in pred.
So the result has one row for each sample and one column for each value of x.

We can use percentile to compute the 5th, 50th, and 95th percentiles in each
column:

low, median, high = np. percentile(pred, [5, 50, 95], axis=0)

To show the results, I'll plot the median of the predictions as a line and the 90% credi-
ble interval as a shaded area:


<figure>

World record speed

13.2

13.0

Speed (mph)

12.8

12.6

12.4

12.2

12.0

1970

1980

1990

2000

2010

2020

2030

2040

Date

</figure>


<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="254" -->
<!-- PageBreak -->

The dashed line shows the two-hour marathon pace, which is 13.1 miles per hour.
Visually we can estimate that the prediction line hits the target pace between 2030
and 2040.

To make this more precise, we can use interpolation to see when the predictions cross
the finish line. SciPy provides interp1d, which does linear interpolation by default.

from scipy. interpolate import interp1d

future = np. array([interp1d(high, xs)(13.1),
interp1d(median, xs)(13.1),

$$\left. \left. i n t e r p 1 d \left( l o w , x s \right) \left( 1 3 . 1 \right) \right] \right)$$

The median prediction is 2036, with a 90% credible interval from 2032 to 2043. So
there is about a 5% chance we'll see a two-hour marathon before 2032.


## Summary

This chapter introduces Bayesian regression, which is based on the same model as
least squares regression; the difference is that it produces a posterior distribution for
the parameters rather than point estimates.

In the first example, we looked at changes in snowfall in Norfolk County, Massachu-
setts, and concluded that we get more snowfall now than when I was young, contrary
to my expectation.

In the second example, we looked at the progression of world record pace for the
men's marathon, computed the joint posterior distribution of the regression parame-
ters, and used it to generate predictions for the next 20 years.

These examples have three parameters, so it takes a little longer to compute the likeli-
hood of the data. With more than three parameters, it becomes impractical to use
grid algorithms.

In the next few chapters, we'll explore other algorithms that reduce the amount of
computation we need to do a Bayesian update, which makes it possible to use models
with more parameters.

But first, you might want to work on these exercises.


# Exercises


## Exercise 17-1.

I am under the impression that it is warmer around here than it used to be. In this
exercise, you can put my conjecture to the test.

<!-- PageFooter="Summary" -->
<!-- PageNumber="255" -->
<!-- PageBreak -->

We'll use the same dataset we used to model snowfall; it also includes daily low and
high temperatures in Norfolk County, Massachusetts, during my lifetime. The details
are in the notebook for this chapter.

1\. Use statsmodels to generate point estimates for the regression parameters.

2\. Choose priors for slope, intercept, and sigma based on these estimates, and use
make_joint3 to make a joint prior distribution.

3\. Compute the likelihood of the data and compute the posterior distribution of the
parameters.

4\. Extract the posterior distribution of slope. How confident are we that tempera-
ture is increasing?

5\. Draw a sample of parameters from the posterior distribution and use it to gener-
ate predictions up to 2067.

6\. Plot the median of the predictions and a 90% credible interval along with the
observed data.

Does the model fit the data well? How much do we expect annual average tempera-
tures to increase over my (expected) lifetime?

<!-- PageFooter="Chapter 17: Regression" -->
<!-- PageNumber="256" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 18 Conjugate Priors" -->

In the previous chapters we have used grid approximations to solve a variety of prob-
lems. One of my goals has been to show that this approach is sufficient to solve many
real-world problems. And I think it's a good place to start because it shows clearly
how the methods work.

However, as we saw in the previous chapter, grid methods will only get you so far.
As we increase the number of parameters, the number of points in the grid grows
(literally) exponentially. With more than 3-4 parameters, grid methods become
impractical.

So, in the remaining three chapters, I will present three alternatives:

1\. In this chapter, we'll use conjugate priors to speed up some of the computations
we've already done.

2\. In the next chapter, I'll present Markov chain Monte Carlo (MCMC) methods,
which can solve problems with tens of parameters, or even hundreds, in a rea-
sonable amount of time.

3\. And in the last chapter, we'll use Approximate Bayesian Computation (ABC) for
problems that are hard to model with simple distributions.

We'll start with the World Cup Problem.


# The World Cup Problem Revisited

In Chapter 8, we solved the World Cup Problem using a Poisson process to model
goals in a soccer game as random events that are equally likely to occur at any point
during a game.

<!-- PageNumber="257" -->
<!-- PageBreak -->

We used a gamma distribution to represent the prior distribution of $\lambda ,$ the goal-
scoring rate. And we used a Poisson distribution to compute the probability of $k ,$ the
number of goals scored.

Here's a gamma object that represents the prior distribution:

from scipy. stats import gamma

alpha = 1.4
dist = gamma(alpha)

And here's a grid approximation:

import numpy as np
from utils import pmf_from_dist
lams = np. linspace(0, 10, 101)
prior = pmf_from_dist(dist, lams)

Here's the likelihood of scoring 4 goals for each possible value of lam:

from scipy. stats import poisson
k = 4
likelihood = poisson(lams). pmf (k)

And here's the update:

posterior = prior * likelihood
posterior.normalize()
0.05015532557804499

So far, this should be familiar. Now we'll solve the same problem using the conjugate
prior.


# The Conjugate Prior

In "The Gamma Distribution" on page 101, I presented three reasons to use a gamma
distribution for the prior and said there was a fourth reason I would reveal later. Well,
now is the time.

The other reason I chose the gamma distribution is that it is the "conjugate prior" of
the Poisson distribution, so-called because the two distributions are connected or
coupled, which is what "conjugate" means.

In the next section I'll explain how they are connected, but first I'll show you the con-
sequence of this connection, which is that there is a remarkably simple way to com-
pute the posterior distribution.

<!-- PageFooter="Chapter 18: Conjugate Priors" -->
<!-- PageNumber="258" -->
<!-- PageBreak -->

However, to demonstrate it, we have to switch from the one-parameter version of the
gamma distribution to the two-parameter version. Since the first parameter is called
alpha, you might guess that the second parameter is called beta.

The following function takes alpha and beta and makes an object that represents a
gamma distribution with those parameters:

def make_gamma_dist(alpha, beta):
"""Makes a gamma object. """
dist = gamma(alpha, scale=1/beta)
dist. alpha = alpha
dist.beta = beta
return dist

Here's the prior distribution with $a l p h a = 1 . 4$ again and $\mathrm { b e t a = } 1 :$

$a l p h a = 1 . 4$
$b e t a = 1$

prior_gamma = make_gamma_dist(alpha, beta)
prior_gamma.mean()
1.4

Now I claim without proof that we can do a Bayesian update with $k$ goals just by
making a gamma distribution with parameters $\mathrm { a l p h a + k }$ and beta+1:

def update_gamma(prior, data):
"""Update a gamma prior.
k, $t = d a t a$
alpha = prior. alpha + k
beta = prior.beta + t
return make_gamma_dist(alpha, beta)

Here's how we update it with $k = 4$ goals in $t = 1$ game:

data = 4, 1
posterior_gamma = update_gamma(prior_gamma, data)

After all the work we did with the grid, it might seem absurd that we can do a Baye-
sian update by adding two pairs of numbers. So let's confirm that it works.

I'll make a Pmf with a discrete approximation of the posterior distribution:

posterior_conjugate = pmf_from_dist(posterior_gamma, lams)

The following figure shows the result along with the posterior we computed using the
grid algorithm:

<!-- PageFooter="The Conjugate Prior" -->
<!-- PageNumber="259" -->
<!-- PageBreak -->


<figure>

Posterior distribution

0.035

grid posterior

conjugate posterior

0.030

0.025

$\sum _ { n = 1 } ^ { 1 1 }$

0.020

0.015

0.010

0.005

0.000

0

2

4

6

8

10

Goal scoring rate (lam)

</figure>


They are the same other than small differences due to floating-point approximations.


## What the Actual?

To understand how that works, we'll write the PDF of the gamma prior and the PMF
of the Poisson likelihood, then multiply them together, because that's what the Baye-
sian update does. We'll see that the result is a gamma distribution, and we'll derive its
parameters.

Here's the PDF of the gamma prior, which is the probability density for each value of
2, given parameters $\alpha$ and $\beta :$

$$\lambda ^ { \alpha - 1 } e ^ { - \lambda \beta }$$

I have omitted the normalizing factor; since we are planning to normalize the poste-
rior distribution anyway, we don't really need it.

Now suppose a team scores $k$ goals in $t$ games. The probability of this data is given by
the PMF of the Poisson distribution, which is a function of $k$ with $\lambda$ and $t$ as
parameters:

$$\lambda ^ { k } e ^ { - \lambda t }$$

Again, I have omitted the normalizing factor, which makes it clearer that the gamma
and Poisson distributions have the same functional form. When we multiply them
together, we can pair up the factors and add up the exponents. The result is the
unnormalized posterior distribution,

<!-- PageFooter="Chapter 18: Conjugate Priors" -->
<!-- PageNumber="260" -->
<!-- PageBreak -->

$$\lambda ^ { \alpha - 1 + k } e ^ { - \lambda \left( \beta + t \right) }$$

which we can recognize as an unnormalized gamma distribution with parameters
$\alpha + k$ and $\beta + t .$

This derivation provides insight into what the parameters of the posterior distribu-
tion mean: $\alpha$ reflects the number of events that have occurred; $\beta$ reflects the elapsed
time.


# Binomial Likelihood

As a second example, let's look again at the Euro Problem. When we solved it with a
grid algorithm, we started with a uniform prior:

from utils import make_uniform

xs = np. linspace(0, 1, 101)
uniform = make_uniform(xs, 'uniform')

We used the binomial distribution to compute the likelihood of the data, which was
140 heads out of 250 attempts:

from scipy. stats import binom

k, $n = 1 4 0 ,$ 250
xs = uniform. qs
likelihood = binom.pmf(k, n, xs)

Then we computed the posterior distribution in the usual way:

posterior = uniform * likelihood
posterior.normalize()

We can solve this problem more efficiently using the conjugate prior of the binomial
distribution, which is the beta distribution.

The beta distribution is bounded between 0 and 1, so it works well for representing
the distribution of a probability like x. It has two parameters, called alpha and beta,
that determine the shape of the distribution.

SciPy provides an object called beta that represents a beta distribution. The following
function takes alpha and beta and returns a new beta object:

import scipy. stats

def $m a k e \_ b e t a \left( a l p h a , \right.$ beta):
"""Makes a beta object. """
dist = scipy. stats.beta(alpha, beta)
dist. alpha = alpha
dist.beta = beta
return dist

<!-- PageFooter="Binomial Likelihood" -->
<!-- PageNumber="261" -->
<!-- PageBreak -->

It turns out that the uniform distribution, which we used as a prior, is the beta distri-
bution with parameters $a l p h a = 1$ and $\mathrm { b e t a } = 1 .$ So we can make a beta object that rep-
resents a uniform distribution, like this:

$$a l p h a = 1$$
$$b e t a = 1$$

prior_beta = make_beta(alpha, beta)

Now let's figure out how to do the update. As in the previous example, we'll write the
PDF of the prior distribution and the PMF of the likelihood function, and multiply
them together. We'll see that the product has the same form as the prior, and we'll
derive its parameters.

Here is the PDF of the beta distribution, which is a function of $x$ with $\alpha$ and $\beta$ as
parameters:

$$x ^ { \alpha - 1 } \left( 1 - x \right) ^ { \beta - 1 }$$

Again, I have omitted the normalizing factor, which we don't need because we are
going to normalize the distribution after the update.

And here's the PMF of the binomial distribution, which is a function of $k$ with $n$ and $x$
as parameters:

$$x ^ { k } \left( 1 - x \right) ^ { n - k }$$

Again, I have omitted the normalizing factor. Now when we multiply the beta prior
and the binomial likelihood, the result is

$$x ^ { \alpha - 1 + k } \left( 1 - x \right) ^ { \beta - 1 + n - k }$$

which we recognize as an unnormalized beta distribution with parameters $\alpha + k$ and
$\beta + n - k .$

So if we observe $k$ successes in n trials, we can do the update by making a beta distri-
bution with parameters $a l p h a + k$ and $\mathrm { b e t a + n - k } .$ That's what this function does:

def update_beta(prior, data):
"""Update a beta distribution. """
$k ,$ $n = d a t a$
$a l p h a = p r i o r . a l p h a + k$
beta = prior.beta + n - k
return make_beta(alpha, beta)

<!-- PageFooter="Chapter 18: Conjugate Priors" -->
<!-- PageNumber="262" -->
<!-- PageBreak -->

Again, the conjugate prior gives us insight into the meaning of the parameters; $\alpha$ is
related to the number of observed successes; $\beta$ is related to the number of failures.

Here's how we do the update with the observed data:

data = 140, 250
posterior_beta = update_beta(prior_beta, data)

To confirm that it works, I'll evaluate the posterior distribution for the possible values
of xs and put the results in a Pmf:

posterior_conjugate = pmf_from_dist(posterior_beta, xs)

And we can compare the posterior distribution we just computed with the results
from the grid algorithm:


<figure>

Posterior distribution of $x$

0.12

grid posterior

conjugate posterior

0.10

Probability

0.08

0.06

0.04

0.02

0.00

0.0

0.2

0.4

0.6

0.8

1.0

Proportion of heads $\tau _ { \mathrm { t } }$
☒

</figure>


They are the same other than small differences due to floating-point approximations.
The examples so far are problems we have already solved, so let's try something new.


## Lions and Tigers and Bears

Suppose we visit a wild animal preserve where we know that the only animals are
lions and tigers and bears, but we don't know how many of each there are. During the
tour, we see three lions, two tigers, and one bear. Assuming that every animal had an
equal chance to appear in our sample, what is the probability that the next animal we
see is a bear?

To answer this question, we'll use the data to estimate the prevalence of each species,
that is, what fraction of the animals belong to each species. If we know the prevalen-
ces, we can use the multinomial distribution to compute the probability of the data.

<!-- PageFooter="Lions and Tigers and Bears" -->
<!-- PageNumber="263" -->
<!-- PageBreak -->

For example, suppose we know that the fraction of lions, tigers, and bears is 0.4, 0.3,
and 0.3, respectively.

In that case the probability of the data is:

from scipy. stats import multinomial

data = 3, 2, 1
$n = n p \cdot s u n \left( d a t a \right)$
$p s = 0 . 4 ,$ 0.3, 0.3

multinomial.pmf(data, n, ps)
0.10368

Now, we could choose a prior for the prevalences and do a Bayesian update using the
multinomial distribution to compute the probability of the data.

But there's an easier way, because the multinomial distribution has a conjugate prior:
the Dirichlet distribution.


# The Dirichlet Distribution

The Dirichlet distribution is a multivariate distribution, like the multivariate normal
distribution we used in "Multivariate Normal Distribution" on page 170 to describe
the distribution of penguin measurements.

In that example, the quantities in the distribution are pairs of flipper length and cul-
men length, and the parameters of the distribution are a vector of means and a matrix
of covariances.

In a Dirichlet distribution, the quantities are vectors of probabilities, x, and the
parameter is a vector, $\alpha .$

An example will make that clearer. SciPy provides a dirichlet object that represents
a Dirichlet distribution. Here's an instance with $\alpha = 1 , 2 , 3 :$

from scipy. stats import dirichlet

alpha = 1, 2, 3
dist = dirichlet(alpha)

Since we provided three parameters, the result is a distribution of three variables.
Suppose we draw a random value from this distribution, like this:

dist.rvs()
array([[0.46414019, 0.16853117, 0.36732863]])

The result is an array of three values. They are bounded between 0 and 1, and they
always add up to 1, so they can be interpreted as the probabilities of a set of outcomes
that are mutually exclusive and collectively exhaustive.

<!-- PageFooter="Chapter 18: Conjugate Priors" -->
<!-- PageNumber="264" -->
<!-- PageBreak -->

Let's see what the distributions of these values look like. I'll draw 1,000 random vec-
tors from this distribution, like this:

$$\mathrm { s a m p l e } = \mathrm { d i s t } . \mathrm { r v s } \left( 1 0 0 0 \right)$$

The result is an array with 1,000 rows and three columns. I'll compute the Cdf of the
values in each column:

from empiricaldist import Cdf

cdfs = [Cdf. from_seq(col)
for col in sample. transpose()]

The result is a list of Cdf objects that represent the marginal distributions of the three
variables. Here's what they look like:


<figure>

1.0

Column 0

Column 1

Column 2

0.8

0.6

0.4

0.2

0.0

0.0

0.2

0.4

0.6

0.8

1.0

</figure>


Column 0, which corresponds to the lowest parameter, contains the lowest probabili-
ties. Column 2, which corresponds to the highest parameter, contains the highest
probabilities.

As it turns out, these marginal distributions are beta distributions. The following
function takes a sequence of parameters, alpha, and computes the marginal distribu-
tion of variable i:

def marginal_beta(alpha, i):
"""Compute the ith marginal of a Dirichlet distribution. """
return make_beta(alpha[i], total-alpha[i])

$$\mathrm { t o t a l } = \mathrm { n p } . \mathrm { s u n } \left( \mathrm { a l p h a } \right)$$

We can use it to compute the marginal distribution for the three variables:

$$\mathrm { m a r g i n a l s } = \left[ \text { marginal } _ { - } \text { beta\left(alpha, i\right) } \right.$$

for i in range(len(alpha))]

<!-- PageFooter="The Dirichlet Distribution" -->
<!-- PageNumber="265" -->
<!-- PageBreak -->

The following plot shows the CDF of these distributions as gray lines and compares
them to the CDFs of the samples:


<figure>

1.0

Column 0

Column 1

. . . $C o l u m n \quad 2$

0.8

0.6

0.4

0.2

0.0

0.0

0.2

0.4

0.6

0.8

1.0

</figure>


This confirms that the marginals of the Dirichlet distribution are beta distributions.
And that's useful because the Dirichlet distribution is the conjugate prior for the mul-
tinomial likelihood function.

If the prior distribution is Dirichlet with parameter vector alpha and the data is a
vector of observations, data, the posterior distribution is Dirichlet with parameter
vector $a l p h a + d a t a .$

As an exercise at the end of this chapter, you can use this method to solve the Lions
and Tigers and Bears problem.


## Summary

After reading this chapter, if you feel like you've been tricked, I understand. It turns
out that many of the problems in this book can be solved with just a few arithmetic
operations. So why did we go to all the trouble of using grid algorithms?

Sadly, there are only a few problems we can solve with conjugate priors; in fact, this
chapter includes most of the ones that are useful in practice.

For the vast majority of problems, there is no conjugate prior and no shortcut to
compute the posterior distribution. That's why we need grid algorithms and the
methods in the next two chapters, Approximate Bayesian Computation (ABC) and
Markov chain Monte Carlo methods (MCMC).

<!-- PageFooter="Chapter 18: Conjugate Priors" -->
<!-- PageNumber="266" -->
<!-- PageBreak -->


# Exercises


## Exercise 18-1.

In the second version of the World Cup Problem, the data we use for the update is
not the number of goals in a game, but the time until the first goal. So the probability
of the data is given by the exponential distribution rather than the Poisson
distribution.

But it turns out that the gamma distribution is also the conjugate prior of the expo-
nential distribution, so there is a simple way to compute this update, too. The PDF of
the exponential distribution is a function of $t$ with $\lambda$ as a parameter:

$$\lambda e ^ { - \lambda t }$$

Multiply the PDF of the gamma prior by this likelihood, confirm that the result is an
unnormalized gamma distribution, and see if you can derive its parameters.

Write a few lines of code to update prior_gamma with the data from this version of
the problem, which was a first goal after 11 minutes and a second goal after an addi-
tional 12 minutes.


## Exercise 18-2.

For problems like the Euro Problem where the likelihood function is binomial, we
can do a Bayesian update with just a few arithmetic operations, but only if the prior is
a beta distribution.

If we want a uniform prior, we can use a beta distribution with $a l p h a = 1$ and $b e t a = 1 .$
But what can we do if the prior distribution we want is not a beta distribution? For
example, in "Triangle Prior" on page 49 we also solved the Euro Problem with a trian-
gle prior, which is not a beta distribution.

In these cases, we can often find a beta distribution that is a good-enough approxima-
tion for the prior we want. See if you can find a beta distribution that fits the triangle
prior, then update it using update_beta.

Use pmf_from_dist to make a Pmf that approximates the posterior distribution and
compare it to the posterior we just computed using a grid algorithm. How big is the
largest difference between them?

<!-- PageFooter="Exercises" -->
<!-- PageNumber="267" -->
<!-- PageBreak -->


## Exercise 18-3.

3Blue1Brown is a YouTube channel about math; if you are not already aware of it, I
recommend it highly. In this video the narrator presents this problem:

You are buying a product online and you see three sellers offering the same product at
the same price. One of them has a 100% positive rating, but with only 10 reviews.
Another has a 96% positive rating with 50 total reviews. And yet another has a 93%
positive rating, but with 200 total reviews.

Which one should you buy from?

Let's think about how to model this scenario. Suppose each seller has some unknown
probability, x, of providing satisfactory service and getting a positive rating, and we
want to choose the seller with the highest value of x.

This is not the only model for this scenario, and it is not necessarily the best. An
alternative would be something like item response theory, where sellers have varying
ability to provide satisfactory service and customers have varying difficulty of being
satisfied.

But the first model has the virtue of simplicity, so let's see where it gets us.

1\. As a prior, I suggest a beta distribution with $a l p h a = 8$ and $b e t a = 2 .$ What does this
prior look like and what does it imply about sellers?

2\. Use the data to update the prior for the three sellers and plot the posterior distri-
butions. Which seller has the highest posterior mean?

3\. How confident should we be about our choice? That is, what is the probability
that the seller with the highest posterior mean actually has the highest value of $x ?$

4\. Consider a beta prior with $a l p h a = 0 . 7$ and $b e t a = 0 . 5 .$ What does this prior look
like and what does it imply about sellers?

5\. Run the analysis again with this prior and see what effect it has on the results.


### Exercise 18-4.

Use a Dirichlet prior with parameter vector alpha = [1, 1, 1] to solve the Lions
and Tigers and Bears problem:

Suppose we visit a wild animal preserve where we know that the only animals are lions
and tigers and bears, but we don't know how many of each there are.

During the tour, we see three lions, two tigers, and one bear. Assuming that every ani-
mal had an equal chance to appear in our sample, estimate the prevalence of each
species.

What is the probability that the next animal we see is a bear?

<!-- PageFooter="Chapter 18: Conjugate Priors" -->
<!-- PageNumber="268" -->
<!-- PageBreak -->

<!-- PageHeader="CHAPTER 19" -->

MCMC

For most of this book we've been using grid methods to approximate posterior distri-
butions. For models with one or two parameters, grid algorithms are fast and the
results are precise enough for most practical purposes. With three parameters, they
start to be slow, and with more than three they are usually not practical.

In the previous chapter we saw that we can solve some problems using conjugate pri-
ors. But the problems we can solve this way tend to be the same ones we can solve
with grid algorithms.

For problems with more than a few parameters, the most powerful tool we have is
MCMC, which stands for "Markov chain Monte Carlo". In this context, "Monte
Carlo" refers to methods that generate random samples from a distribution. Unlike
grid methods, MCMC methods don't try to compute the posterior distribution; they
sample from it instead.

It might seem strange that you can generate a sample without ever computing the dis-
tribution, but that's the magic of MCMC.

To demonstrate, we'll start by solving the World Cup Problem. Yes, again.


# The World Cup Problem

In Chapter 8 we modeled goal scoring in football (soccer) as a Poisson process char-
acterized by a goal-scoring rate, denoted 1.

We used a gamma distribution to represent the prior distribution of $\lambda ,$ then we used
the outcome of the game to compute the posterior distribution for both teams.

To answer the first question, we used the posterior distributions to compute the
"probability of superiority" for France.

<!-- PageNumber="269" -->
<!-- PageBreak -->

To answer the second question, we computed the posterior predictive distributions
for each team, that is, the distribution of goals we expect in a rematch.

In this chapter we'll solve this problem again using PyMC3, which is a library that
provide implementations of several MCMC methods. But we'll start by reviewing the
grid approximation of the prior and the prior predictive distribution.


# Grid Approximation

As we did in "The Gamma Distribution" on page 101 we'll use a gamma distribution
with parameter $\alpha = 1 . 4$ to represent the prior:

from scipy. stats import gamma

$a l p h a = 1 . 4$
$\mathrm { p r i o r } _ { - } \mathrm { d i s t } = \mathrm { g a m n a } \left( \mathrm { a l p h a } \right)$

I'll use linspace to generate possible values for $\lambda ,$ and pmf_from_dist to compute a
discrete approximation of the prior:

import numpy as np
from utils import pmf_from_dist
lams = np. linspace(0, 10, 101)
prior_pmf = pmf_from_dist(prior_dist, lams)

We can use the Poisson distribution to compute the likelihood of the data; as an
example, we'll use 4 goals:

from scipy. stats import poisson

data = 4
likelihood = poisson. pmf(data, lams)

Now we can do the update in the usual way:

posterior = prior_pmf * likelihood
posterior.normalize()
0.05015532557804499

Soon we will solve the same problem with PyMC3, but first it will be useful to intro-
duce something new: the prior predictive distribution.


# Prior Predictive Distribution

We have seen the posterior predictive distribution in previous chapters; the prior pre-
dictive distribution is similar except that (as you might have guessed) it is based on
the prior.

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="270" -->
<!-- PageBreak -->

To estimate the prior predictive distribution, we'll start by drawing a sample from the
prior:

$$s a m p l e \_ p r i o r = p r i o r \_ d i s t . r v s \left( 1 0 0 0 \right)$$

The result is an array of possible values for the goal-scoring rate, $\lambda$ . For each value in
sample_prior, I'll generate one value from a Poisson distribution:

from scipy. stats import poisson

sample_prior_pred = poisson. rvs(sample_prior)

sample_prior_pred is a sample from the prior predictive distribution. To see what it
looks like, we'll compute the PMF of the sample:


## from empiricaldist import Pmf

pmf_prior_pred = Pmf. from_seq(sample_prior_pred)

And here's what it looks like:


<figure>

Prior Predictive Distribution

0.35

0.30

0.25

$\sum _ { n = 1 } ^ { 4 }$

0.20

0.15

0.10

0.05

0.00

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

11

12

Number of goals

</figure>


One reason to compute the prior predictive distribution is to check whether our
model of the system seems reasonable. In this case, the distribution of goals seems
consistent with what we know about World Cup football.

But in this chapter we have another reason: computing the prior predictive distribu-
tion is a first step toward using MCMC.


# Introducing PyMC3

PyMC3 is a Python library that provides several MCMC methods. To use PyMC3, we
have to specify a model of the process that generates the data. In this example, the
model has two steps:

<!-- PageFooter="Introducing PyMC3" -->
<!-- PageNumber="271" -->
<!-- PageBreak -->

· First we draw a goal-scoring rate from the prior distribution,

· Then we draw a number of goals from a Poisson distribution.

Here's how we specify this model in PyMC3:

import pymc3 as pm

with pm. Model() as model:
lam = pm. Gamma('lam', alpha=1.4, beta=1.0)
goals = pm. Poisson( 'goals', lam)

After importing pymc3, we create a Model object named model.

If you are not familiar with the with statement in Python, it is a way to associate a
block of statements with an object. In this example, the two indented statements are
associated with the new Model object. As a result, when we create the distribution
objects, Gamma and Poisson, they are added to the Model.

Inside the with statement:

· The first line creates the prior, which is a gamma distribution with the given
parameters.

· The second line creates the prior predictive, which is a Poisson distribution with
the parameter lam.

The first parameter of Gamma and Poisson is a string variable name.


## Sampling the Prior

PyMC3 provides a function that generates samples from the prior and prior predic-
tive distributions. We can use a with statement to run this function in the context of
the model:

with model:
trace = pm. sample_prior_predictive(1000)

The result is a dictionary-like object that maps from the variables, $l a m$ and goals, to
the samples. We can extract the sample of lam like this:

sample_prior_pymc = trace['lam' ]
sample_prior_pymc . shape
(1000,)

The following figure compares the CDF of this sample to the CDF of the sample we
generated using the gamma object from SciPy:

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="272" -->
<!-- PageBreak -->


<figure>

Prior distribution

1.0

SciPy sample

PyMC3 sample

0.8

0.6

CDF

0.4

0.2

0.0

0

2

4

6

8

Goals per game (1)

</figure>


The results are similar, which confirms that the specification of the model is correct
and the sampler works as advertised.

From the trace we can also extract goals, which is a sample from the prior predictive
distribution:

sample_prior_pred_pymc = trace['goals' ]
sample_prior_pred_pymc. shape
(1000,)

And we can compare it to the sample we generated using the poisson object from
SciPy.

Because the quantities in the posterior predictive distribution are discrete (number of
goals) I'll plot the CDFs as step functions:


<figure>
<figcaption>Prior Predictive Distribution</figcaption>

1.0

SciPy sample

PyMC3 sample

0.9

0.8

PMF

0.7

0.6

0.5

0.4

0

2

4

6

8

10

12

Number of goals

</figure>


<!-- PageFooter="Sampling the Prior" -->
<!-- PageNumber="273" -->
<!-- PageBreak -->

Again, the results are similar, so we have some confidence we are using PyMC3 right.


# When Do We Get to Inference?

Finally, we are ready for actual inference. We just have to make one small change.
Here is the model we used to generate the prior predictive distribution:

with pm. Model() as model:
lam = pm. Gamma('lam', alpha=1.4, beta=1.0)
goals = pm. Poisson('goals', lam)

And here is the model we'll use to compute the posterior distribution:

with pm. Model() as model2:

$$l a m = p m . \text { Gama } \left( ^ { \prime } l a m ^ { \prime } , a l p h a = 1 . 4 , b e t a = 1 . 0 \right)$$
$$\mathrm { q o a l s } = \text { pn.Poisson } \left( ^ { \prime } \text { goals } ^ { \prime } , \text { lam, observed=4 } \right)$$

The difference is that we mark goals as observed and provide the observed data, 4.

And instead of calling sample_prior_predictive, we'll call sample, which is under-
stood to sample from the posterior distribution of lam:

options = dict(return_inferencedata=False)

with model2:
trace2 = pm.sample(500, ** options)

Although the specification of these models is similar, the sampling process is very dif-
ferent. I won't go into the details of how PyMC3 works, but here are a few things you
should be aware of:

· Depending on the model, PyMC3 uses one of several MCMC methods; in this
example, it uses the No U-Turn Sampler (NUTS), which is one of the most effi-
cient and reliable methods we have.

· When the sampler starts, the first values it generates are usually not a representa-
tive sample from the posterior distribution, so these values are discarded. This
process is called "tuning".

· Instead of using a single Markov chain, PyMC3 uses multiple chains. Then we
can compare results from multiple chains to make sure they are consistent.

Although we asked for a sample of 500, PyMC3 generated two samples of 1,000, dis-
carded half of each, and returned the remaining 1,000. From trace2 we can extract a
sample from the posterior distribution, like this:

$$s a m p l e \_ p o s t \_ p y m c = t r a c e 2 \left[ l a m \right]$$

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="274" -->
<!-- PageBreak -->

And we can compare the CDF of this sample to the posterior we computed by grid
approximation:


<figure>

Posterior $\mathrm { d i s t r i b u t i o n }$

1.0

posterior grid

PyMC3 sample

0.8

0.6

CDF

0.4

0.2

0.0

0

2

4

6

8

10

Goals per game $\left( \lambda \right)$

</figure>


The results from PyMC3 are consistent with the results from the grid approximation.


## Posterior Predictive Distribution

Finally, to sample from the posterior predictive distribution, we can use sample_pos
terior_predictive:

with model2:
post_pred = pm. sample_posterior_predictive(trace2)

The result is a dictionary that contains a sample of goals:

sample_post_pred_pymc = post_pred[ 'goals' ]

I'll also generate a sample from the posterior distribution we computed by grid
approximation:

sample_post = posterior . sample(1000)

$$\mathrm { s a m p l e } _ { - } \mathrm { p o s t } _ { - } \mathrm { p r e d } = \mathrm { p o i s s o n } \left( \mathrm { s a m p l e } _ { - } \mathrm { p o s t } \right) . \mathrm { r v s } \left( \right)$$

And we can compare the two samples:

<!-- PageFooter="Posterior Predictive Distribution" -->
<!-- PageNumber="275" -->
<!-- PageBreak -->


<figure>

Posterior Predictive Distribution

1.0

grid sample

PyMC3 sample

0.8

$\sum _ { n = 1 } ^ { 1 1 }$

0.6

0.4

0.2

0

2

4

6

8

10

12

14

Number of goals

</figure>


Again, the results are consistent. So we've established that we can compute the same
results using a grid approximation or PyMC3.

But it might not be clear why. In this example, the grid algorithm requires less com-
putation than MCMC, and the result is a pretty good approximation of the posterior
distribution, rather than a sample.

However, this is a simple model with just one parameter. In fact, we could have solved
it with even less computation, using a conjugate prior. The power of PyMC3 will be
clearer with a more complex model.


## Happiness

Recently I read "Happiness and Life Satisfaction" by Esteban Ortiz-Ospina and Max
Roser, which discusses (among many other things) the relationship between income
and happiness, both between countries, within countries, and over time. It cites the
"World Happiness Report", which includes results of a multiple regression analysis
that explores the relationship between happiness and six potentially predictive
factors:

· Income as represented by per capita GDP

· Social support

· Healthy life expectancy at birth

· Freedom to make life choices

· Generosity

· Perceptions of corruption

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="276" -->
<!-- PageBreak -->

The dependent variable is the national average of responses to the "Cantril ladder
question" used by the Gallup World Poll:

Please imagine a ladder with steps numbered from zero at the bottom to 10 at the top.

The top of the ladder represents the best possible life for you and the bottom of the
ladder represents the worst possible life for you. On which step of the ladder would
you say you personally feel you stand at this time?

I'll refer to the responses as "happiness", but it might be more precise to think of them
as a measure of satisfaction with quality of life.

In the next few sections we'll replicate the analysis in this report using Bayesian
regression.

We can use pandas to read the data into a DataFrame:

import pandas as pd

filename = 'WHR20_DataForFigure2. 1.xls'
df = pd.read_excel(filename)

The DataFrame has one row for each of 153 countries and one column for each of 20
variables.

The column called 'Ladder score' contains the measurements of happiness we will
try to predict.

score = df[' Ladder score']


## Simple Regression

To get started, let's look at the relationship between happiness and income as repre-
sented by gross domestic product (GDP) per person.

The column named 'Logged GDP per capita' represents the natural logarithm of
GDP for each country, divided by population, corrected for purchasing power parity
(PPP):

log_gdp = df['Logged GDP per capita']

The following figure is a scatter plot of score versus log_gdp, with one marker for
each country:

<!-- PageFooter="Simple Regression" -->
<!-- PageNumber="277" -->
<!-- PageBreak -->


<figure>

8

7

Happiness ladder score

6

5

4

3

7

8

9

10

11

Log GDP per capita at PPP

</figure>


It's clear that there is a relationship between these variables: people in countries with
higher GDP generally report higher levels of happiness.

We can use linregress from SciPy to compute a simple regression of these variables:
from scipy. stats import linregress

result = linregress(log_gdp, score)

And here are the results:


<table>
<tr>
<td>Slope</td>
<td>0.717738</td>
</tr>
<tr>
<td>Intercept</td>
<td>-1.198646</td>
</tr>
</table>


The estimated slope is about 0.72, which suggests that an increase of one unit in log-
GDP, which is a factor of $e \approx 2 . 7$ in GDP, is associated with an increase of 0.72 units
on the happiness ladder.

Now let's estimate the same parameters using PyMC3. We'll use the same regression
model as in "Regression Model" on page 243,

$$y = a x + b +$$

where $y$ is the dependent variable (ladder score), $x$ is the predictive variable (log
GDP) and $\epsilon$ is a series of values from a normal distribution with standard deviation o.

a and $b$ are the slope and intercept of the regression line. They are unknown parame-
ters, so we will use the data to estimate them.

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="278" -->
<!-- PageBreak -->

The following is the PyMC3 specification of this model:

$$x _ { - } d a t a = \log _ { - } g d p$$
$$y _ { - } d a t a = s c o r e$$

$$a = p m . \text { Uniform } \left( ^ { \prime } a ^ { \prime } , \theta , 4 \right)$$

with pm. Model() as model3:
$b = p n . \text { Uniform } \left( b ^ { \prime } , - 4 , 4 \right)$
sigma = pm. Uniform('sigma', 0, 2)

$$y _ { - } e s t = a * x _ { - } d a t a + b$$

$y = p m . \text { Normal } \left( ^ { \prime } y ^ { \prime } \right. ,$

$$m u = y _ { - } e s t , s d = s i g m a ,$$
$$\mathrm { o b s e r v e d } = y _ { - }$$

The prior distributions for the parameters a, b, and sigma are uniform with ranges
that are wide enough to cover the posterior distributions.

y_est is the estimated value of the dependent variable, based on the regression equa-
tion. And $y$ is a normal distribution with mean y_est and standard deviation sigma.
Notice how the data are included in the model:

· The values of the predictive variable, x_data, are used to compute y_est.

· The values of the dependent variable, $y _ { - } d a t a ,$ are provided as the observed val-
ues of y.

Now we can use this model to generate a sample from the posterior distribution:

with model3:
trace3 = pm.sample(500, ** options)

When you run the sampler, you might get warning messages about "divergences" and
the "acceptance probability". You can ignore them for now.

The result is an object that contains samples from the joint posterior distribution of a,
b, and sigma.

ArviZ provides plot_posterior, which we can use to plot the posterior distributions
of the parameters. Here are the posterior distributions of slope, a, and intercept, b:

import arviz as az

with model3:
az. plot_posterior(trace3, var_names=['a', 'b']);

<!-- PageFooter="Simple Regression" -->
<!-- PageNumber="279" -->
<!-- PageBreak -->


<figure>

a

b

mean=0.72

$m e a n = - \quad 1 . 2$

$9 4 H D I$

$9 4 H D I$

0.63

0.8

-21

-0.53

0.60

0.65

0.70

0.75

0.80

0.85

-2.5

-2.0

-1.5

-1.0

-0.5

0.0

</figure>


The graphs show the distributions of the samples, estimated by KDE, and 94% credi-
ble intervals. In the figure, "HDI" stands for "highest-density interval".

The means of these samples are consistent with the parameters we estimated with
linregress.

The simple regression model has only three parameters, so we could have used a grid
algorithm. But the regression model in the happiness report has six predictive vari-
ables, so it has eight parameters in total, including the intercept and sigma.

It is not practical to compute a grid approximation for a model with eight parameters.
Even a coarse grid, with 20 points along each dimension, would have more than 25
billion points. And with 153 countries, we would have to compute almost 4 trillion
likelihoods.

But PyMC3 can handle a model with eight parameters comfortably, as we'll see in the
next section.


# Multiple Regression

Before we implement the multiple regression model, I'll select the columns we need
from the DataFrame:

columns = [' Ladder score',
'Logged GDP per capita',
'Social support',
'Healthy life expectancy',
'Freedom to make life choices',
'Generosity',
'Perceptions of corruption']

subset = df[columns]

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="280" -->
<!-- PageBreak -->

The predictive variables have different units: log-GDP is in log-dollars, life expect-
ancy is in years, and the other variables are on arbitrary scales. To make these factors
comparable, I'll standardize the data so that each variable has mean 0 and standard
deviation 1.

$$s t a n d a r d i z e d = \left( s u b s e t \quad - \quad s u b s e t . m e a n \left( \right) \right) / s u b s e t . s t d \left( \right)$$

Now let's build the model. I'll extract the dependent variable:

$$y _ { - } d a t a = s t a n d a r d i z e d \left[ ^ { \prime } L a d d e r s c o r e ^ { \prime } \right]$$

And the dependent variables:

$$x 1 = s t a n d a r d i z e d \left[ c o l u m n s \left[ 1 \right] \right]$$
$$x 2 = s t a n d a r d i z e d \left[ c o l u m n s \left[ 2 \right] \right]$$
$$x 3 = s t a n d a r d i z e d \left[ c o l u m n s \left[ 3 \right] \right]$$
$$x 4 = s t a n d a r d i z e d \left[ c o l u m n s \left[ 4 \right] \right]$$
$$x 5 = s t a n d a r d i z e d \left[ c o l u m n s \left[ 5 \right] \right]$$
$$x 6 = s t a n d a r d i z e d \left[ c o l u m n s \left[ 6 \right] \right]$$

And here's the model. b0 is the intercept; b1 through b6 are the parameters associated
with the predictive variables:

with pm. Model() as model4:

$h \theta = 0 m . \text { Uniform } \left( { } ^ { \prime } b \theta ^ { \prime } \right. ,$ -4, 4)

$$b 1 = p n . \text { Uniform } \left( { } ^ { \prime } b 1 ^ { \prime } , - 4 , 4 \right)$$
$$b 2 = p m . \text { Uniform } \left( { } ^ { \prime } b 2 ^ { \prime } , - 4 , 4 \right)$$

$b 3 = p m . U n i f o r m \left( b 3 , \right.$ -4, 4)
b4 = pm. Uniform('b4', -4, 4)
$b 5 = p n . \text { Uniform } \left( { } ^ { \prime } b 5 ^ { \prime } \right. ,$ -4, 4)
b6 = pm. Uniform('b6', -4, 4)
$s i g m a = p m .$ Uniform( 'sigma', 0, 2)
$y _ { - } e s t = b \theta + b 1 ^ { * } x 1 + b 2 ^ { * } x 2 + b 3 ^ { * } x 3 + b 4 ^ { * } x 4 + b 5 ^ { * } x 5 + b 6 ^ { * } x 6$
$y = p m . \text { Normal } \left( ^ { \prime } y ^ { \prime } \right. ,$
mu=y_est, sd=sigma,

$$\mathrm { o b s e r v e d } = y _ { - }$$

We could express this model more concisely using a vector of predictive variables and
a vector of parameters, but I decided to keep it simple.

Now we can sample from the joint posterior distribution:

with model4:
trace4 = pm. sample(500, ** options)

From trace4 we can extract samples from the posterior distributions of the parame-
ters and compute their means:

param_names = ['b1', 'b3', 'b3', 'b4', 'b5', 'b6']

means = [trace4[ name] .mean()
for name in param_names]

<!-- PageFooter="Multiple Regression" -->
<!-- PageNumber="281" -->
<!-- PageBreak -->

We can also compute 94% credible intervals (between the 3rd and 97th percentiles):

def credible_interval(sample) :
"""Compute 94% credible interval. """
$c i =$ np.percentile(sample, [3, 97])
return np. round(ci, 3)

cis = [credible_interval(trace4[name])
for name in param_names]

The following table summarizes the results:


<table>
<tr>
<th></th>
<th>Posterior mean</th>
<th>94% CI</th>
</tr>
<tr>
<td>Logged GDP per capita</td>
<td>0.246</td>
<td>[0.077, 0.417]</td>
</tr>
<tr>
<td>Social support</td>
<td>0.224</td>
<td>[0.064, 0.384]</td>
</tr>
<tr>
<td>Healthy life expectancy</td>
<td>0.224</td>
<td>[0.064, 0.384]</td>
</tr>
<tr>
<td>Freedom to make life choices</td>
<td>0.190</td>
<td>[0.094, 0.291]</td>
</tr>
<tr>
<td>Generosity</td>
<td>0.055</td>
<td>[-0.032, 0.139]</td>
</tr>
<tr>
<td>Perceptions of corruption</td>
<td>-0.098</td>
<td>[-0.194, -0.002]</td>
</tr>
</table>


It looks like GDP has the strongest association with happiness (or satisfaction), fol-
lowed by social support, life expectancy, and freedom.

After controlling for those other factors, the parameters of the other factors are sub-
stantially smaller, and since the CI for generosity includes 0, it is plausible that gener-
osity is not substantially related to happiness, at least as they were measured in this
study.

This example demonstrates the power of MCMC to handle models with more than a
few parameters. But it does not really demonstrate the power of Bayesian regression.

If the goal of a regression model is to estimate parameters, there is no great advantage
to Bayesian regression compared to conventional least squares regression.

Bayesian methods are more useful if we plan to use the posterior distribution of the
parameters as part of a decision analysis process.


# Summary

In this chapter we used PyMC3 to implement two models we've seen before: a Pois-
son model of goal-scoring in soccer and a simple regression model. Then we imple-
mented a multiple regression model that would not have been possible to compute
with a grid approximation.

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="282" -->
<!-- PageBreak -->

MCMC is more powerful than grid methods, but that power comes with some
disadvantages:

· MCMC algorithms are fiddly. The same model might behave well with some pri-
ors and less well with others. And the sampling process often produces warnings
about tuning steps, divergences, "r-hat statistics", acceptance rates, and effective
samples. It takes some expertise to diagnose and correct these issues.

· I find it easier to develop models incrementally using grid algorithms, checking
intermediate results along the way. With PyMC3, it is not as easy to be confident
that you have specified a model correctly.

For these reasons, I recommend a model development process that starts with grid
algorithms and resorts to MCMC if necessary. As we saw in the previous chapters,
you can solve a lot of real-world problems with grid methods. But when you need
MCMC, it is useful to have a grid algorithm to compare to (even if it is based on a
simpler model).

All of the models in this book can be implemented in PyMC3, but some of them are
easier to translate than others. In the exercises, you will have a chance to practice.


# Exercises


## Exercise 19-1.

As a warm-up, let's use PyMC3 to solve the Euro Problem. Suppose we spin a coin
250 times and it comes up heads 140 times. What is the posterior distribution of $x ,$
the probability of heads?

For the prior, use a beta distribution with parameters $\alpha = 1$ and $\beta = 1 .$

See the PyMC3 documentation for the list of continuous distributions.


## Exercise 19-2.

Now let's use PyMC3 to replicate the solution to the Grizzly Bear Problem in "The
Grizzly Bear Problem" on page 207, which is based on the hypergeometric
distribution.

I'll present the problem with slightly different notation, to make it consistent with
PyMC3.

Suppose that during the first session, $k = 2 3$ bears are tagged. During the second ses-
sion, $n = 1 9$ bears are identified, of which $x = 4$ had been tagged.

Estimate the posterior distribution of $N ,$ the number of bears in the environment.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="283" -->
<!-- PageBreak -->

For the prior, use a discrete uniform distribution from 50 to 500.

See the PyMC3 documentation for the list of discrete distributions.

Note: HyperGeometric was added to PyMC3 after version 3.8, so you might need to
update your installation to do this exercise.


## Exercise 19-3.

In "The Weibull Distribution" on page 191 we generated a sample from a Weibull dis-
tribution with $\lambda = 3$ and $k = 0 . 8 .$ Then we used the data to compute a grid approxima-
tion of the posterior distribution of those parameters.

Now let's do the same with PyMC3.

For the priors, you can use uniform distributions as we did in Chapter 14, or you
could use HalfNormal distributions provided by PyMC3.

Note: The Weibull class in PyMC3 uses different parameters than SciPy. The parame-
ter alpha in PyMC3 corresponds to $k ,$ and beta corresponds to ).

data = [0.80497283, 2.11577082, 0.43308797, 0.10862644, 5.17334866,
3. 25745053, 3.05555883, 2.47401062, 0.05340806, 1.08386395]


## Exercise 19-4.

In "Improving Reading Ability" on page 175 we used data from a reading test to esti-
mate the parameters of a normal distribution.

Make a model that defines uniform prior distributions for mu and sigma and uses the
data to estimate their posterior distributions.


## Exercise 19-5.

In "The Lincoln Index Problem" on page 215 we used a grid algorithm to solve the
Lincoln Index Problem as presented by John D. Cook:

Suppose you have a tester who finds 20 bugs in your program. You want to estimate
how many bugs are really in the program. You know there are at least 20 bugs, and if
you have supreme confidence in your tester, you may suppose there are around 20
bugs. But maybe your tester isn't very good. Maybe there are hundreds of bugs. How
can you have any idea how many bugs there are? There's no way to know with one
tester. But if you have two testers, you can get a good idea, even if you don't know how
skilled the testers are.

Suppose the first tester finds 20 bugs, the second finds 15, and they find 3 in com-
mon; use PyMC3 to estimate the number of bugs.

<!-- PageFooter="Chapter 19: MCMC" -->
<!-- PageNumber="284" -->
<!-- PageBreak -->

Note: This exercise is more difficult that some of the previous ones. One of the chal-
lenges is that the data includes k00, which depends on $N :$

k00 = N - num_seen

So we have to construct the data as part of the model. To do that, we can use
pm.math. stack, which makes an array:

data = pm.math.stack((k00, k01, k10, k11))
Finally, you might find it helpful to use pm. Multinomial.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="285" -->
<!-- PageBreak -->

<!-- PageBreak -->

<!-- PageHeader="CHAPTER 20" -->


# Approximate Bayesian Computation

This chapter introduces a method of last resort for the most complex problems,
Approximate Bayesian Computation (ABC). I say it is a last resort because it usually
requires more computation than other methods, so if you can solve a problem any
other way, you should. However, for the examples in this chapter, ABC is not just easy
to implement; it is also efficient.

The first example is my solution to a problem posed by a patient with a kidney tumor.
I use data from a medical journal to model tumor growth, and use simulations to esti-
mate the age of a tumor based on its size.

The second example is a model of cell counting, which has applications in biology,
medicine, and zymurgy (beer-making). Given a cell count from a diluted sample, we
estimate the concentration of cells.

Finally, as an exercise, you'll have a chance to work on a fun sock-counting problem.


## The Kidney Tumor Problem

I am a frequent reader and occasional contributor to the online statistics forum at
http://reddit.com/r/statistics. In November 2011, I read the following message:

"I have Stage IV Kidney Cancer and am trying to determine if the cancer formed
before I retired from the military. ... Given the dates of retirement and detection is it
possible to determine when there was a 50/50 chance that I developed the disease? Is it
possible to determine the probability on the retirement date? My tumor was 15.5 cm x
15 cm at detection. Grade II.

I contacted the author of the message to get more information; I learned that veterans
get different benefits if it is "more likely than not" that a tumor formed while they
were in military service (among other considerations). So I agree to help him answer
his question.

<!-- PageNumber="287" -->
<!-- PageBreak -->

Because renal tumors grow slowly, and often do not cause symptoms, they are some-
times left untreated. As a result, doctors can observe the rate of growth for untreated
tumors by comparing scans from the same patient at different times. Several papers
have reported these growth rates.

For my analysis I used data from a paper by Zhang et al. They report growth rates in
two forms:

· Volumetric doubling time, which is the time it would take for a tumor to double
in size.

· Reciprocal doubling time (RDT), which is the number of doublings per year.

The next section shows how we work with these growth rates.


## A Simple Growth Model

We'll start with a simple model of tumor growth based on two assumptions:

· Tumors grow with a constant doubling time, and

· They are roughly spherical in shape.

And I'll define two points in time:

· t1 is when my correspondent retired.

· t2 is when the tumor was detected.

The time between t1 and t2 was about 9.0 years. As an example, let's assume that the
diameter of the tumor was 1 cm at t1, and estimate its size at t2.

I'll use the following function to compute the volume of a sphere with a given
diameter:

import numpy as np

def calc_volume(diameter ) :
"""Converts a diameter to a volume. ""'
factor = 4 * np.pi / 3
return factor * (diameter/2.0) ** 3

Assuming that the tumor is spherical, we can compute its volume at t1:

$d 1 = 1$
v1 = calc_volume(d1)
v1
0.5235987755982988

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="288" -->
<!-- PageBreak -->

The median volume doubling time reported by Zhang et al. is 811 days, which corre-
sponds to an RDT of 0.45 doublings per year:

median_doubling_time = 811
rdt = 365 / median_doubling_time
rdt
0.45006165228113443

We can compute the number of doublings that would have happened in the interval
between t1 and t2:

interval = 9.0

$$d o u b l i n g s = i n t e r v a l * r d t$$

doublings
4.05055487053021

Given $\mathrm { v 1 }$ and the number of doublings, we can compute the volume at t2:

$$v 2 = v 1 * 2 ^ { * * } d o u b l i n g s$$

v2
8.676351488087187

The following function computes the diameter of a sphere with the given volume:

def calc_diameter (volume) :
"""Converts a volume to a diameter. """
factor = 3 / np.pi / 4
return 2 * (factor * volume) ** (1/3)

So we can compute the diameter of the tumor at t2:

d2 = calc_diameter(v2)
d2
2.5494480788327483

If the diameter of the tumor was 1 cm at t1, and it grew at the median rate, the diam-
eter would be about 2.5 cm at t2.

This example demonstrates the growth model, but it doesn't answer the question my
correspondent posed.


## A More General Model

Given the size of a tumor at time of diagnosis, we would like to know the distribution
of its age. To find it, we'll run simulations of tumor growth to get the distribution of
size conditioned on age. Then we'll compute the distribution of age conditioned on
size.

<!-- PageFooter="A More General Model" -->
<!-- PageNumber="289" -->
<!-- PageBreak -->

The simulation starts with a small tumor and runs these steps:

1\. Choose a value from the distribution of growth rates.

2\. Compute the size of the tumor at the end of an interval.

3\. Repeat until the tumor exceeds the maximum relevant size.

So the first thing we need is the distribution of growth rates.

Using the figures in the paper by Zhange et al., I created an array, rdt_sample, that
contains estimated values of RDT for the 53 patients in the study.

Again, RDT stands for "reciprocal doubling time", which is in doublings per year. So
if $r d t = 1 ,$ a tumor would double in volume in one year. If $r d t = 2 ,$ it would double
twice; that is, the volume would quadruple. And if $r d t = - \quad 1 ,$ it would halve in volume.

We can use the sample of RDTs to estimate the PDF of the distribution:

from utils import kde_from_sample

qs = np. linspace(-2, 6, num=201)
$\mathrm { p m f } _ { - } \mathrm { r d t } = \mathrm { k d e } _ { - } \mathrm { f r o m } _ { - } \mathrm { s a m p l e } \left( \mathrm { r d t } _ { - } \mathrm { s a m p l e } , \mathrm { q s } \right)$

Here's what it looks like:


<figure>

Distribution of growth rates

0.0200

rdts

0.0175

0.0150

0.0125

PDF

0.0100

0.0075

0.0050

0.0025

0.0000

-2

-1

0

1

2

3

4

5

6

Reciprocal doubling time (RDT)

</figure>


In the next section we will use this distribution to simulate tumor growth.

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="290" -->
<!-- PageBreak -->


## Simulation

Now we're ready to run the simulations. Starting with a small tumor, we'll simulate a
series of intervals until the tumor reaches a maximum size.

At the beginning of each simulated interval, we'll choose a value from the distribution
of growth rates and compute the size of the tumor at the end.

I chose an interval of 245 days (about 8 months) because that is the median time
between measurements in the data source.

For the initial diameter I chose 0.3 cm, because carcinomas smaller than that are less
likely to be invasive and less likely to have the blood supply needed for rapid growth
(see this page on carcinoma). For the maximum diameter I chose 20 cm.


<table>
<tr>
<td>interval = 245 / 365</td>
<td># year</td>
</tr>
<tr>
<td>min_diameter = 0.3</td>
<td># cm</td>
</tr>
<tr>
<td>max_diameter = 20</td>
<td>$\# c m$</td>
</tr>
</table>


I'll use calc_volume to compute the initial and maximum volumes:

v0 = calc_volume(min_diameter)
vmax = calc_volume(max_diameter)
v0, vmax
(0.014137166941154066, 4188.790204786391)

The following function runs the simulation:

import pandas as pd

def simulate_growth(pmf_rdt):
"""Simulate the growth of a tumor.
age = 0
volume = v0
$r e s = \left[ \right]$

while True:
res. append( (age, volume))
if volume > vmax:
break
$r d t = p n f _ { - } r d t . c h o i c e \left( \right)$
age += interval
$d o u b l i n g s = r d t$ * interval
volume *= 2 ** doublings

$= \left[ ^ { \prime } \mathrm { a g e } ^ { \prime } , ^ { \prime } \text { volume } ^ { \prime } \right]$
sim = pd. DataFrame(res, columns=columns)
sim['diameter' ] = calc_diameter(sim[ 'volume' ])
return sim

<!-- PageFooter="Simulation" -->
<!-- PageNumber="291" -->
<!-- PageBreak -->

simulate_growth takes as a parameter a Pmf that represents the distribution of RDT.
It initializes the age and volume of the tumor, then runs a loop that simulates one
interval at a time.

Each time through the loop, it checks the volume of the tumor and exits if it exceeds
vmax.

Otherwise it chooses a value from pmf_rdt and updates age and volume. Since rdt is
in doublings per year, we multiply by interval to compute the number of doublings
during each interval.

At the end of the loop, simulate_growth puts the results in a DataFrame and com-
putes the diameter that corresponds to each volume.

Here's how we call this function:

$$s i n = s i m u l a t e \_ g r o w t h \left( p m f _ { - } r d t \right)$$

Here are the results for the first few intervals:

sim.head(3)


<table>
<tr>
<th></th>
<th>age</th>
<th>volume</th>
<th>diameter</th>
</tr>
<tr>
<td>0</td>
<td>0.000000</td>
<td>0.014137</td>
<td>0.300000</td>
</tr>
<tr>
<td>1</td>
<td>0.671233</td>
<td>0.014949</td>
<td>0.305635</td>
</tr>
<tr>
<td>2</td>
<td>1.342466</td>
<td>0.019763</td>
<td>0.335441</td>
</tr>
</table>


And the last few intervals:

sim.tail(3)


<table>
<tr>
<th></th>
<th>age</th>
<th>volume</th>
<th>diameter</th>
</tr>
<tr>
<td>43</td>
<td>28.863014</td>
<td>1882.067427</td>
<td>15.318357</td>
</tr>
<tr>
<td>44</td>
<td>29.534247</td>
<td>2887.563277</td>
<td>17.667603</td>
</tr>
<tr>
<td>45</td>
<td>30.205479</td>
<td>4953.618273</td>
<td>21.149883</td>
</tr>
</table>


To show the results graphically, I'll run 101 simulations:

$s i n s = \left[ s i m u l a t e \_ g r o w t h \left( p n f _ { - } r d t \right) \right.$ for _ in range(101)]

And plot the results:

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="292" -->
<!-- PageBreak -->


<figure>

20

10

Diameter (cm, log scale)

5

2

1

0.5

0.2

0

10

20

30

40

Tumor age (years)

</figure>


In this figure, each thin, solid line shows the simulated growth of a tumor over time,
with diameter on a log scale. The dotted lines are at 4, 8, and 16 cm.

By reading across the dotted lines, you can get a sense of the distribution of age at
each size. For example, reading across the top line, we see that the age of a 16 cm
tumor might be as low 10 years or as high as 40 years, but it is most likely to be
between 15 and 30.

To compute this distribution more precisely, we can interpolate the growth curves to
see when each one passes through a given size. The following function takes the
results of the simulations and returns the age when each tumor reached a given
diameter:

from scipy. interpolate import interp1d

def interpolate_ages(sims, diameter):
"""Estimate the age when each tumor reached a given size. """
ages = [ ]
for sim in sims:
interp = interp1d(sim['diameter' ], sim['age'])
age = interp(diameter)
ages . append ( float (age))

return ages

We can call this function like this:

from empiricaldist import Cdf

ages = interpolate_ages(sims, 15)
cdf = Cdf . from_seq(ages)
print(cdf.median(), cdf.credible_interval(0.9))
22.31854530374061 [13.47056554 34.49632276]

<!-- PageFooter="Simulation" -->
<!-- PageNumber="293" -->
<!-- PageBreak -->

For a tumor 15 cm in diameter, the median age is about 22 years, the 90% credible
interval is between 13 and 34 years, and the probability that it formed less than 9
years ago is less than 1%:

1 - cdf(9.0)

0.9900990099009901

But this result is based on two modeling decisions that are potentially problematic:

· In the simulations, growth rate during each interval is independent of previous
growth rates. In reality it is plausible that tumors that have grown quickly in the
past are likely to grow quickly in the future. In other words, there is probably a
serial correlation in growth rate.

· To convert from linear measure to volume, we assume that tumors are approxi-
mately spherical.

In additional experiments, I implemented a simulation that chooses growth rates with
serial correlation; the effect is that the fast-growing tumors grow faster and the slow-
growing tumors grow slower. Nevertheless, with moderate correlation (0.5), the prob-
ability that a 15 cm tumor is less than 9 years old is only about 1%.

The assumption that tumors are spherical is probably fine for tumors up to a few cen-
timeters, but not for a tumor with linear dimensions $1 5 . 5 \times 1 5 c m .$ If, as seems likely,
a tumor this size is relatively flat, it might have the same volume as a 6 cm sphere. But
even with this smaller volume and correlation 0.5, the probability that this tumor is
less than 9 years old is about 5%.

So even taking into account modeling errors, it is unlikely that such a large tumor
could have formed after my correspondent retired from military service.


## Approximate Bayesian Computation

At this point you might wonder why this example is in a book about Bayesian statis-
tics. We never defined a prior distribution or did a Bayesian update. Why not?
Because we didn't have to.

Instead, we used simulations to compute ages and sizes for a collection of hypotheti-
cal tumors. Then, implicitly, we used the simulation results to form a joint distribu-
tion of age and size. If we select a column from the joint distribution, we get a
distribution of size conditioned on age. If we select a row, we get a distribution of age
conditioned on size.

So this example is like the ones we saw in Chapter 1: if you have all of the data, you
don't need Bayes's theorem; you can compute probabilities by counting.

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="294" -->
<!-- PageBreak -->

This example is a first step toward Approximate Bayesian Computation (ABC). The
next example is a second step.


## Counting Cells

This example comes from this blog post, by Cameron Davidson-Pilon. In it, he mod-
els the process biologists use to estimate the concentration of cells in a sample of liq-
uid. The example he presents is counting cells in a "yeast slurry", which is a mixture
of yeast and water used in brewing beer.

There are two steps in the process:

· First, the slurry is diluted until the concentration is low enough that it is practical
to count cells.

· Then a small sample is put on a hemocytometer, which is a specialized micro-
scope slide that holds a fixed amount of liquid on a rectangular grid.

The cells and the grid are visible in a microscope, making it possible to count the cells
accurately.

As an example, suppose we start with a yeast slurry with an unknown concentration
of cells. Starting with a 1 mL sample, we dilute it by adding it to a shaker with 9 mL of
water and mixing well. Then we dilute it again, and then a third time. Each dilution
reduces the concentration by a factor of 10, so three dilutions reduces the concentra-
tion by a factor of 1,000.

Then we add the diluted sample to the hemocytometer, which has a capacity of
0.0001 mL spread over a $5 \times 5$ grid. Although the grid has 25 squares, it is standard
practice to inspect only a few of them, say 5, and report the total number of cells in
the inspected squares.

This process is simple enough, but at every stage there are sources of error:

· During the dilution process, liquids are measured using pipettes that introduce
measurement error.

· The amount of liquid in the hemocytometer might vary from the specification.

· During each step of the sampling process, we might select more or less than the
average number of cells, due to random variation.

Davidson-Pilon presents a PyMC model that describes these errors. I'll start by repli-
cating his model; then we'll adapt it for ABC.

Suppose there are 25 squares in the grid, we count 5 of them, and the total number of
cells is 49:

<!-- PageFooter="Counting Cells" -->
<!-- PageNumber="295" -->
<!-- PageBreak -->

total_squares = 25
squares_counted = 5
yeast_counted = 49

Here's the first part of the model, which defines the prior distribution of yeast_conc,
which is the concentration of yeast we're trying to estimate.

shaker 1_vol is the actual volume of water in the first shaker, which should be 9 mL,
but might be higher or lower, with standard deviation 0.05 mL. $s h a k e r 2 \_ v o l$ and
shaker 3_vol are the volumes in the second and third shakers.

import pymc3 as pm
billion = 1e9

with pm. Model() as model:
yeast_conc = pm. Normal( "yeast conc",
mu=2 * billion, sd=0.4 * billion)
shaker1_vol = pm. Normal("shaker1 vol",

$$\left. m u = 9 . 0 , s d = 0 . 0 5 \right)$$
$$s h a k e r 2 \_ v o l = p m . N o r m a l \left( s h a k e r 2 \quad v o l , \right.$$
$$\left. m u = 9 . 0 , s d = 0 . 0 5 \right)$$
$$3 _ { - } \text { vol } = \text { prormal } \left( { } ^ { \prime \prime } \text { shaker } 3 \text { vol } ^ { \prime \prime } \right. ,$$
$$\left. m u = 9 . 0 , s d = 0 . 0 5 \right)$$

Now, the sample drawn from the yeast slurry is supposed to be 1 mL, but might be
more or less. And similarly for the sample from the first shaker and from the second
shaker. The following variables model these steps:

with model:

$$\mathrm { y e a s t } \_ \mathrm { s l u r r y } \_ \mathrm { v o l } = \mathrm { p m } . \mathrm { N o r m a l } \left( ^ { \prime \prime } \mathrm { y e a s t } \mathrm { s l u r r y } \mathrm { v o l } ^ { \mathrm { n } } , \right. ,$$
$$1 \text { to shaker } 2 \text { vol } = \text { pn } . \text { Normal } \left( ^ { \prime \prime } \text { shaker } 1 \text { to shaker } 2 ^ { \prime \prime } \right. ,$$
mu=1.0, sd=0.01)

mu=1.0, sd=0.01)
shaker2_to_shaker3_vol = pm. Normal("shaker2 to shaker3",
mu=1.0, sd=0.01)

Given the actual volumes in the samples and in the shakers, we can compute the
effective dilution, final_dilution, which should be 1,000, but might be higher or
lower.

with model:

dilution_shaker1 = (yeast_slurry_vol /
(yeast_slurry_vol + shaker1_vol))
dilution_shaker2 = (shaker1_to_shaker2_vol /
(shaker1_to_shaker2_vol + shaker2_vol))
dilution_shaker3 = (shaker2_to_shaker3_vol /
(shaker2_to_shaker3_vol + shaker3_vol))

final_dilution = (dilution_shaker1 *
dilution_shaker2 *
dilution_shaker3)

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="296" -->
<!-- PageBreak -->

The next step is to place a sample from the third shaker in the chamber of the hemo-
cytomer. The capacity of the chamber should be 0.0001 mL, but might vary; to
describe this variance, we'll use a gamma distribution, which ensures that we don't
generate negative values:

with model:

$$\mathrm { c h a m b e r } _ { - } \mathrm { v o l } = \mathrm { p n } . \mathrm { G a m m a } \left( ^ { \prime \prime } \mathrm { c h a m b e r } _ { - } \mathrm { v o l } ^ { \prime \prime } , \right. ,$$
$$\left. m u = 0 . 0 0 0 1 , s d = 0 . 0 0 0 1 / 2 0 \right)$$

On average, the number of cells in the chamber is the product of the actual concen-
tration, final dilution, and chamber volume. But the actual number might vary; we'll
use a Poisson distribution to model this variance:

with model:

$$y e a s t \_ i n \_ c h a m b e r = p m . P o i s s o n \left( y e a s t \quad i n \quad c h a m b e r , \right.$$
$$\left. m u = y e a s t \_ c o n c * f i n a l \_ d i l u t i o n * c h a m b e r \_ v o l \right)$$

Finally, each cell in the chamber will be in one of the squares we count with probabil-
ity p=squares_counted/total_squares. So the actual count follows a binomial
distribution:

with model:
count = pm. Binomial( "count",
n=yeast_in_chamber,
p=squares_counted/total_squares,
observed=yeast_counted)

With the model specified, we can use sample to generate a sample from the posterior
distribution:

$$\mathrm { o p t i o n s } = \mathrm { d i c t } \left( \mathrm { r e t u r n } _ { - } \mathrm { i n f e r e n c e d a t a } = \mathrm { F a l s e } \right)$$

with model:
trace = pm. sample(1000, ** options)

And we can use the sample to estimate the posterior distribution of yeast_conc and
compute summary statistics:

posterior_sample = trace['yeast conc' ] / billion
cdf_pymc = Cdf . from_seq(posterior_sample)
print(cdf_pymc.mean(), cdf_pymc.credible_interval(0.9))
2.26789764737366 [1.84164524 2.70290741]

The posterior mean is about 2.3 billion cells per mL, with a 90% credible interval
from 1.8 and 2.7.

So far we've been following in Davidson-Pilon's footsteps. And for this problem, the
solution using MCMC is sufficient. But it also provides an opportunity to demon-
strate ABC.

<!-- PageFooter="Counting Cells" -->
<!-- PageNumber="297" -->
<!-- PageBreak -->


## Cell Counting with ABC

The fundamental idea of ABC is that we use the prior distribution to generate a sam-
ple of the parameters, and then simulate the system for each set of parameters in the
sample.

In this case, since we already have a PyMC model, we can use sample_prior_predic
tive to do the sampling and the simulation:

with model:

$$\mathrm { p r i o r } \_ \mathrm { s a m p l e } = \mathrm { p m } . \mathrm { s a m p l e } \_ \mathrm { p r i o r } \_ \mathrm { p r e d i c t i v e } \left( 1 0 0 0 0 \right)$$

The result is a dictionary that contains samples from the prior distribution of the
parameters and the prior predictive distribution of count:

$$c o u n t = p r i o r \_ s a m p l e \left[ c o u n t \right]$$
print(count.mean())

39.9847

Now, to generate a sample from the posterior distribution, we'll select only the ele-
ments in the prior sample where the output of the simulation, count, matches the
observed data, 49:

$$= \left( \mathrm { c o u n t } = = 4 9 \right)$$

mask. sum()
251

We can use mask to select the values of yeast_conc for the simulations that yield the
observed data:

posterior_sample2 = prior_sample['yeast conc' ][mask] / billion

And we can use the posterior sample to estimate the CDF of the posterior
distribution:

cdf_abc = Cdf. from_seq(posterior_sample2)
print(cdf_abc.mean(), cdf_abc.credible_interval(0.9))
2.2635057237709755 [1.85861977 2.68665897]

The posterior mean and credible interval are similar to what we got with MCMC.
Here's what the distributions look like:

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="298" -->
<!-- PageBreak -->


<figure>

Posterior distribution

1.0

MCMC

ABC

0.8

0.6

CDF

0.4

0.2

0.0

1.50

1.75

2.00

2.25

2.50

2.75

3.00

3.25

Yeast concentration (cells/mL)

</figure>


The distributions are similar, but the results from ABC are noisier because the sample
size is smaller.


# When Do We Get to the Approximate Part?

The examples so far are similar to Approximate Bayesian Computation, but neither of
them demonstrates all of the elements of ABC. More generally, ABC is characterized
by:

1\. A prior distribution of parameters.

2\. A simulation of the system that generates the data.

3\. A criterion for when we should accept that the output of the simulation matches
the data.

The kidney tumor example was atypical because we didn't represent the prior distri-
bution of age explicitly. Because the simulations generate a joint distribution of age
and size, we were able to get the marginal posterior distribution of age directly from
the results.

The yeast example is more typical because we represented the distribution of the
parameters explicitly. But we accepted only simulations where the output matches the
data exactly.

The result is approximate in the sense that we have a sample from the posterior distri-
bution rather than the posterior distribution itself. But it is not approximate in the
sense of Approximate Bayesian Computation, which typically accepts simulations
where the output matches the data only approximately.

<!-- PageFooter="When Do We Get to the Approximate Part?" -->
<!-- PageNumber="299" -->
<!-- PageBreak -->

To show how that works, I will extend the yeast example with an approximate match-
ing criterion.

In the previous section, we accepted a simulation if the output is precisely 49 and
rejected it otherwise. As a result, we got only a few hundred samples out of 10,000
simulations, so that's not very efficient.

We can make better use of the simulations if we give "partial credit" when the output
is close to 49. But how close? And how much credit?

One way to answer that is to back up to the second-to-last step of the simulation,
where we know the number of cells in the chamber, and we use the binomial distribu-
tion to generate the final count.

If there are n cells in the chamber, each has a probability $\mathrm { p }$ of being counted, depend-
ing on whether it falls in one of the squares in the grid that get counted.

We can extract n from the prior sample, like this:

n = prior_sample['yeast in chamber' ]
n. shape
(10000,)

And compute p like this:

p = squares_counted/total_squares
p
0.2

Now here's the idea: we'll use the binomial distribution to compute the likelihood of
the data, yeast_counted, for each value of n and the fixed value of $\mathrm { p } :$

from scipy. stats import binom

likelihood = binom(n, p).pmf(yeast_counted). flatten()

When the expected count, $n ^ { * } p ,$ is close to the actual count, likelihood is relatively
high; when it is farther away, likelihood is lower.

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="300" -->
<!-- PageBreak -->

The following is a scatter plot of these likelihoods versus the expected counts:


<figure>

0.06

0.05

Likelihood

0.04

0.03

0.02

0.01

0.00

10

20

30

40

50

60

70

Expected count (number of cells)

</figure>


We can't use these likelihoods to $d o \quad a$ Bayesian update because they are incomplete;
that is, each likelihood is the probability of the data given n, which is the result of a
single simulation.

But we can use them to weight the results of the simulations. Instead of requiring the
output of the simulation to match the data exactly, we'll use the likelihoods to give
partial credit when the output is close.

Here's how: I'll construct a Pmf that contains yeast concentrations as quantities and
the likelihoods as unnormalized probabilities.

qs = prior_sample['yeast conc' ] / billion
ps = likelihood
posterior_pmf = Pmf(ps, qs)

In this Pmf, values of yeast_conc that yield outputs close to the data map to higher
probabilities. If we sort the quantities and normalize the probabilities, the result is an
estimate of the posterior distribution.

posterior_pmf.sort_index(inplace=True)
posterior_pmf.normalize()

print(posterior_pmf.mean(), posterior_pmf.credible_interval(0.9))

2.271401984584812 [1.85333758 2.71299385]

<!-- PageFooter="When Do We Get to the Approximate Part?" -->
<!-- PageNumber="301" -->
<!-- PageBreak -->

The posterior mean and credible interval are similar to the values we got from
MCMC. And here's what the posterior distributions look like:


<figure>

Posterior distribution

1.0

$M C M C$

$A B C 2$

0.8

0.6

CDF

0.4

0.2

0.0

1.50

1.75

2.00

2.25

2.50

2.75

3.00

3.25

Yeast concentration (cells/mL)

</figure>


The distributions are similar, but the results from MCMC are a little noisier. In this
example, ABC is more efficient than MCMC, requiring less computation to generate
a better estimate of the posterior distribution. But that's unusual; usually ABC
requires a lot of computation. For that reason, it is generally a method of last resort.


## Summary

In this chapter we saw two examples of Approximate Bayesian Computation (ABC),
based on simulations of tumor growth and cell counting.

The definitive elements of ABC are:

1\. A prior distribution of parameters.

2\. A simulation of the system that generates the data.

3\. A criterion for when we should accept that the output of the simulation matches
the data.

ABC is particularly useful when the system is too complex to model with tools like
PyMC. For example, it might involve a physical simulation based on differential equa-
tions. In that case, each simulation might require substantial computation, and many
simulations might be needed to estimate the posterior distribution.

Next, you'll have a chance to practice with one more example.

<!-- PageFooter="Chapter 20: Approximate Bayesian Computation" -->
<!-- PageNumber="302" -->
<!-- PageBreak -->


# Exercises


## Exercise 20-1.

This exercise is based on a blog post by Rasmus Bååth, which is motivated by a tweet
from Karl Broman, who wrote:

That the first 11 socks in the laundry are distinct suggests that there are a lot of socks.

Suppose you pull 11 socks out of the laundry and find that no two of them make a
matched pair. Estimate the number of socks in the laundry.

To solve this problem, we'll use the model Bååth suggests, which is based on these
assumptions:

· The laundry contains some number of pairs of socks, n_pairs, plus some num-
ber of odd (unpaired) socks, n_odds.

· The pairs of socks are different from each other and different from the unpaired
socks; in other words, the number of socks of each type is either 1 or 2, never
more.

We'll use the prior distributions Bååth suggests, which are:

· The number of socks follows a negative binomial distribution with mean 30 and
standard deviation 15.

· The proportion of socks that are paired follows a beta distribution with parame-
ters $a l p h a = 1 5$ and beta=2.

In the notebook for this chapter, I'll define these priors. Then you can simulate the
sampling process and use ABC to estimate the posterior distributions.

<!-- PageFooter="Exercises" -->
<!-- PageNumber="303" -->
<!-- PageBreak -->

<!-- PageBreak -->

Index


<table>
<tr>
<th>Symbols</th>
<th>transposing DataFrame matrix, 95</th>
</tr>
<tr>
<td>[] (bracket operator), 6</td>
<td>triangle-shaped prior, 49</td>
</tr>
<tr>
<td>probability mass functions, 30</td>
<td>weighted mixture of distributions, 95</td>
</tr>
<tr>
<td>| (given), 9</td>
<td>ArviZ plot_posterior, 279</td>
</tr>
<tr>
<td>$+ \left( p \mathrm { l u s } \right)$ versus Pmf.add_dist(), 93</td>
<td>Axtell, Robert, 61</td>
</tr>
<tr>
<td>A</td>
<td>B</td>
</tr>
<tr>
<td>age of the universe, 53</td>
<td>Basu's theorem, 185</td>
</tr>
<tr>
<td>Anaconda distribution of Python, xi</td>
<td>Bayes factor, 72, 131, 134, 234</td>
</tr>
<tr>
<td>Approximate Bayesian Computation (ABC)</td>
<td>Bayes tables</td>
</tr>
<tr>
<td>about, 287, 299</td>
<td>Cookie Problem, 20-22</td>
</tr>
<tr>
<td>counting cells via ABC, 298-302</td>
<td>Dice Problem, 22</td>
</tr>
<tr>
<td>counting cells via MCMC, 295-297</td>
<td>Monty Hall Problem, 23-25</td>
</tr>
<tr>
<td>Kidney Tumor Problem</td>
<td>Bayesian Bandit strategy</td>
</tr>
<tr>
<td>ABC aspect, 294</td>
<td>about, 134</td>
</tr>
<tr>
<td>about, 287, 299</td>
<td>multiple bandits, 137</td>
</tr>
<tr>
<td>growth model, general, 289</td>
<td>prior beliefs, 135</td>
</tr>
<tr>
<td>growth model, simple, 288</td>
<td>strategy put together, 140</td>
</tr>
<tr>
<td>simulation of growth, 291-294</td>
<td>testing, 140</td>
</tr>
<tr>
<td>arrays</td>
<td>update, 136</td>
</tr>
<tr>
<td>coin tossed twice, 44</td>
<td>which machine to play, 138</td>
</tr>
<tr>
<td>DataFrame converted to NumPy array, 149</td>
<td>Bayesian decision analysis</td>
</tr>
<tr>
<td>meshgrid function</td>
<td>bandit strategy (see Bayesian Bandit strat-</td>
</tr>
<tr>
<td>comparison operators, 146, 151</td>
<td>egy)</td>
</tr>
<tr>
<td>joint distribution construction, 148</td>
<td>instead of hypothesis testing, 134</td>
</tr>
<tr>
<td>likelihood of height of person, 151</td>
<td>Price Is Right Problem</td>
</tr>
<tr>
<td>outer product, 145, 148</td>
<td>about, 113</td>
</tr>
<tr>
<td>outer sum, 146</td>
<td>decision analysis, 122</td>
</tr>
<tr>
<td>3-dimensional for reading ability, 178</td>
<td>distribution of errors, 116-118</td>
</tr>
<tr>
<td>normal distribution of height, 147</td>
<td>kernel density estimation, 115, 116</td>
</tr>
<tr>
<td>np.repeat function, 200</td>
<td>maximizing expected gain, 124</td>
</tr>
<tr>
<td>np.where function, 151</td>
<td>modeling, 116</td>
</tr>
<tr>
<td>parentheses versus brackets, 75</td>
<td>prior, 114</td>
</tr>
<tr>
<td>3-dimensional to 2-dimensional, 179</td>
<td>probability of winning, 120</td>
</tr>
</table>


<!-- PageNumber="305" -->
<!-- PageBreak -->


<table>
<tr>
<th>update, 118</th>
<th>derivation of, 8-10</th>
</tr>
<tr>
<th>questions to ask, 134</th>
<th>diachronic Bayes, 19</th>
</tr>
<tr>
<td>Bayesian estimation in Euro Problem, 47-51</td>
<td>example of use, 11</td>
</tr>
<tr>
<td>Bayesian hypothesis testing</td>
<td>gluten sensitivity, 76</td>
</tr>
<tr>
<td>Bayesian Bandit strategy, 140</td>
<td>Forward Problem, 77</td>
</tr>
<tr>
<td>decision analysis instead, 134</td>
<td>Inverse Problem, 78</td>
</tr>
<tr>
<td>Euro Problem</td>
<td>bears (see Grizzly Bear Problem)</td>
</tr>
<tr>
<td>about, 129</td>
<td>beta distribution, 261</td>
</tr>
<tr>
<td>about previous solution, 129-131</td>
<td>Dirichlet distribution marginals as, 266</td>
</tr>
<tr>
<td>binomial distribution, 46, 130</td>
<td>SciPy beta function, 261</td>
</tr>
<tr>
<td>modeling, 131</td>
<td rowspan="2">bidding strategy (see Price Is Right Problem) binomial distribution, 44</td>
</tr>
<tr>
<td>modeling triangle-shaped bias, 133</td>
</tr>
<tr>
<td>modeling uniform bias, 132</td>
<td>beta distribution, 261</td>
</tr>
<tr>
<td>statistical versus, 134</td>
<td>Dirichlet distribution marginals as, 266</td>
</tr>
<tr>
<td>Bayesian Methods for Hackers (Davidson-</td>
<td>SciPy beta function, 261</td>
</tr>
<tr>
<td>Pilon), 114, 226</td>
<td>binomial coefficient, 44</td>
</tr>
<tr>
<td>Bayesian regression (see linear regression)</td>
<td>hypergeometric distribution, 208</td>
</tr>
<tr>
<td>Bayesian statistics versus Bayes's theorem, 53</td>
<td>conjugate prior of, 261</td>
</tr>
<tr>
<td>Bayesian updates, 20</td>
<td>Euro Problem tested, 46, 130</td>
</tr>
<tr>
<td>about, 19, 260</td>
<td>gluten sensitivity, 76</td>
</tr>
<tr>
<td>Bayes tables for, 20-22</td>
<td>Forward Problem, 77</td>
</tr>
<tr>
<td>Bayesian logistic regression, 231</td>
<td>Inverse Problem, 78</td>
</tr>
<tr>
<td>dictionary for ease, 48</td>
<td>light bulb dead bulb prediction, 202</td>
</tr>
<tr>
<td>gamma distribution for, 259-261</td>
<td>SciPy binomial function, 44</td>
</tr>
<tr>
<td>How Tall Is Person A, 152</td>
<td>binomial likelihood function, 51, 129</td>
</tr>
<tr>
<td>log odds, 224</td>
<td>conjugate priors, 261</td>
</tr>
<tr>
<td>update additive, 226</td>
<td>blood type problem, 71-73</td>
</tr>
<tr>
<td>Pmf objects for, 33</td>
<td>Boolean Series</td>
</tr>
<tr>
<td>Bayesian Bandit strategy, 136</td>
<td>conjunctions, 5</td>
</tr>
<tr>
<td>classification of penguin data, 164-168</td>
<td>impossible outcomes, 40</td>
</tr>
<tr>
<td>Cookie Problem, 33</td>
<td>incomplete data, 195</td>
</tr>
<tr>
<td>Dice Problem, 39</td>
<td>summing, 3</td>
</tr>
<tr>
<td>World Cup Problem, 103</td>
<td>probability function, 4</td>
</tr>
<tr>
<td>posterior distribution location, 105</td>
<td>Box, George, 99</td>
</tr>
<tr>
<td>Price Is Right Problem, 118</td>
<td rowspan="3">bracket operator ([]), 6 probability mass functions, 30 bugs in program (see Lincoln Index Problem)</td>
</tr>
<tr>
<td>reading improvement groups, 177-180</td>
</tr>
<tr>
<td>summary statistics, 186 snow amounts, 247</td>
</tr>
<tr>
<td>wrong classroom, 224</td>
<td>C</td>
</tr>
<tr>
<td>update additive, 226</td>
<td rowspan="2">cancer (see Kidney Tumor Problem) Cantril ladder question on happiness, 277</td>
</tr>
<tr>
<td>Bayes's rule</td>
</tr>
<tr>
<td>about, 223</td>
<td>CDF (see cumulative distribution function)</td>
</tr>
<tr>
<td>Bayes's theorem in odds form, 70</td>
<td>Cdf objects</td>
</tr>
<tr>
<td>Cookie Problem, 71, 72</td>
<td>about, 86, 88</td>
</tr>
<tr>
<td>Oliver's Blood, 71-73</td>
<td>classification of penguin data, 162</td>
</tr>
<tr>
<td>wrong classroom, 224, 225</td>
<td>complementary CDF, 89</td>
</tr>
<tr>
<td>Bayes's theorem, 10</td>
<td>distribution of differences, 182</td>
</tr>
<tr>
<td>Bayesian statistics versus, 53</td>
<td rowspan="2">distribution, maximum of six attributes, 88 max_dist function, 89</td>
</tr>
<tr>
<td>Cookie Problem, 17-19</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="306" -->
<!-- PageBreak -->


<table>
<tr>
<th>distribution, minimum of six attributes, 89 min_dist function, 90</th>
<th>Dirichlet distribution, 264 Euro Problem, 261</th>
</tr>
<tr>
<td>empiricaldist library for Cdf class, 85</td>
<td>World Cup Problem</td>
</tr>
<tr>
<td>Pmf object conversion, 86</td>
<td>gamma distribution for update, 258-261</td>
</tr>
<tr>
<td>reading improvement groups, 176</td>
<td>Poisson processes solution review, 257</td>
</tr>
<tr>
<td>Weibull distribution, 192-194</td>
<td>conjunctions, 5</td>
</tr>
<tr>
<td>censored data, 195</td>
<td>commutative property, 6, 10</td>
</tr>
<tr>
<td>centering data to minimize correlation, 232,</td>
<td>conditional probability and, 8</td>
</tr>
<tr>
<td>244</td>
<td>product of probabilities, 10</td>
</tr>
<tr>
<td>Central Limit Theorem, 76</td>
<td>relationship in math notation, 9</td>
</tr>
<tr>
<td>classification of penguin data</td>
<td>conditional probability computed via, 9</td>
</tr>
<tr>
<td>about, 161</td>
<td>contour plot</td>
</tr>
<tr>
<td>cumulative distribution functions, 162</td>
<td>joint distribution, 150</td>
</tr>
<tr>
<td>data description, 161</td>
<td>Grizzly Bear two-parameter model, 214</td>
</tr>
<tr>
<td>data source, 161</td>
<td>Weibull distribution, 193</td>
</tr>
<tr>
<td>joint distributions, 168</td>
<td>incomplete data, 197</td>
</tr>
<tr>
<td>scatter plot, 168</td>
<td>Cook, John D., 215</td>
</tr>
<tr>
<td>scatter plot compared to contours, 169</td>
<td>Cookie Problem</td>
</tr>
<tr>
<td>less naive Bayesian classifier, 172</td>
<td>Bayes tables, 20-22</td>
</tr>
<tr>
<td>loading into DataFrame, 161</td>
<td>Bayes's rule, 71</td>
</tr>
<tr>
<td>multivariate normal distribution, 170</td>
<td>Bayes's theorem, 17-19</td>
</tr>
<tr>
<td>normal models, 163, 169</td>
<td>likelihood, 19</td>
</tr>
<tr>
<td>update, 164-168</td>
<td>odds, 72</td>
</tr>
<tr>
<td>naive Bayesian classifier, 166</td>
<td>101 Bowls Problem, 34-37</td>
</tr>
<tr>
<td>coin fairness (see Euro Problem)</td>
<td>Euro Problem contrasted, 52</td>
</tr>
<tr>
<td>Colab to run Jupyter notebooks, x</td>
<td>Pmf objects, 29, 32-34</td>
</tr>
<tr>
<td>collectively exhaustive, 11</td>
<td>updated data, 33</td>
</tr>
<tr>
<td>gender as, 12</td>
<td>prior, 19</td>
</tr>
<tr>
<td>law of total probability, 11, 19</td>
<td>correlation minimized by centering data, 232,</td>
</tr>
<tr>
<td>commutative property</td>
<td>244</td>
</tr>
<tr>
<td>conditional probability, 7 conjunctions, 6, 10</td>
<td>count estimation (see counting cells; estimating counts)</td>
</tr>
<tr>
<td>company sizes following power law, 61</td>
<td>Counter function, 137</td>
</tr>
<tr>
<td>Conda environment for book code, xi</td>
<td>counting cells</td>
</tr>
<tr>
<td>conditional posteriors, 156</td>
<td>Approximate Bayesian Computation, 298</td>
</tr>
<tr>
<td>conditional probability</td>
<td>MCMC, 295</td>
</tr>
<tr>
<td>about, 6</td>
<td>covariance matrix, 170</td>
</tr>
<tr>
<td>commutative property, 7</td>
<td>credible intervals, 64, 249</td>
</tr>
<tr>
<td>computing, 6</td>
<td>credible_interval function, 64</td>
</tr>
<tr>
<td>conjunction to compute, 9</td>
<td>cumulative distribution function (CDF)</td>
</tr>
<tr>
<td>conjunctions and, 8</td>
<td>about, 83</td>
</tr>
<tr>
<td>conjunction as product of probabilities,</td>
<td>0 to 1 range, 84</td>
</tr>
<tr>
<td>10</td>
<td>Cdf objects (see Cdf objects)</td>
</tr>
<tr>
<td>relationship in math notation, 9</td>
<td>classification of penguin data, 162</td>
</tr>
<tr>
<td>Linda the Banker Problem, 1</td>
<td>complementary CDF, 89</td>
</tr>
<tr>
<td>probability function, 7</td>
<td>distribution as mix of distributions, 90-93</td>
</tr>
<tr>
<td>conjugate priors</td>
<td>general solution, 93-96</td>
</tr>
<tr>
<td>about, 258</td>
<td>distribution of differences, 182</td>
</tr>
<tr>
<td>animal preserve with three parameters, 263</td>
<td>empiricaldist for Cdf class, 85</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="307" -->
<!-- PageBreak -->


<table>
<tr>
<th>Euro Problem, 83</th>
<th>dictionaries</th>
</tr>
<tr>
<td>np.diff function, 86</td>
<td>classification of penguin data, 163</td>
</tr>
<tr>
<td>PMF conversion, 86</td>
<td>ease of updating, 48</td>
</tr>
<tr>
<td>reading improvement groups, 176</td>
<td>Dirichlet distribution, 264</td>
</tr>
<tr>
<td>Weibull distribution, 192-194</td>
<td>marginals as beta distributions, 266 discrete distributions and numerical errors, $x$</td>
</tr>
<tr>
<td>D</td>
<td>distribution objects, 272</td>
</tr>
<tr>
<td>data</td>
<td>distribution of differences, 181</td>
</tr>
<tr>
<td>classification of penguin data, 161-172</td>
<td>plotting, 182</td>
</tr>
<tr>
<td>data source, 161</td>
<td>distribution of errors, 116-118</td>
</tr>
<tr>
<td rowspan="2">data in hand, Bayes's theorem not needed, 294</td>
<td>distributions</td>
</tr>
<tr>
<td>about, 29</td>
</tr>
<tr>
<td>Empirical Bayes method data reused, 237</td>
<td>beta distribution, 261</td>
</tr>
<tr>
<td>empirical versus theoretical distributions, 29</td>
<td rowspan="2">Dirichlet distribution marginals as, 266 SciPy beta function, 261</td>
</tr>
<tr>
<td>evidence in favor of a hypothesis, 72, 131</td>
</tr>
<tr>
<td>Bayes factor, 72, 131, 134, 234</td>
<td rowspan="2">Cdf for maximum or minimum, 88-90 coin tossed twice, 44</td>
</tr>
<tr>
<td>evidence of biased coin, 43-52</td>
</tr>
<tr>
<td>Bayes's rule for, 132</td>
<td>company sizes following power law, 61</td>
</tr>
<tr>
<td>groupby for data into groups, 176, 230, 242</td>
<td>conditional distribution, 156</td>
</tr>
<tr>
<td>GSS (General Social Survey) dataset, 2-5, 7, 11</td>
<td>Cookie Problem 101 bowls of cookies, 34-37</td>
</tr>
<tr>
<td>incomplete data, 194-196</td>
<td>Pmf for, 32-34</td>
</tr>
<tr>
<td>called censored, 195</td>
<td>Pmf for updated data, 33</td>
</tr>
<tr>
<td>marginal distributions, 197 using, 196-199</td>
<td>cumulative distribution function 0 to 1 range, 84</td>
</tr>
<tr>
<td>informative versus uninformative prior, 65</td>
<td>about, 83</td>
</tr>
<tr>
<td>Price Is Right prices and bids, 114</td>
<td>classification of penguin data, 162</td>
</tr>
<tr>
<td>priors converging on same posterior, 51</td>
<td>complementary CDF, 89</td>
</tr>
<tr>
<td>summary statistics, 184</td>
<td>distribution of differences, 182</td>
</tr>
<tr>
<td>swamping the priors, 51</td>
<td>empiricaldist for Cdf class, 85</td>
</tr>
<tr>
<td>updating probability with new data, 19</td>
<td>(see also Cdf objects)</td>
</tr>
<tr>
<td>(see also Bayesian updates)</td>
<td>Euro Problem, 83</td>
</tr>
<tr>
<td>weather records, 241</td>
<td>np.diff function, 86</td>
</tr>
<tr>
<td>DataFrames (see pandas)</td>
<td>PMF conversion, 86</td>
</tr>
<tr>
<td>Davidson-Pilon, Cameron, 114, 226, 295</td>
<td>reading improvement groups, 176</td>
</tr>
<tr>
<td>decision analysis in Price Is Right, 122</td>
<td>Weibull distribution, 192-194</td>
</tr>
<tr>
<td>(see also Bayesian decision analysis)</td>
<td>Dirichlet distribution, 264</td>
</tr>
<tr>
<td>degree of certainty via odds, 69</td>
<td>discrete distributions, $\mathrm { X }$</td>
</tr>
<tr>
<td>(see also odds)</td>
<td>distribution as mix of distributions, 90-93</td>
</tr>
<tr>
<td>dependence and independence of heights, 157</td>
<td>general solution, 93-96</td>
</tr>
<tr>
<td>diachronic Bayes's theorem, 19</td>
<td>distribution of differences, 181</td>
</tr>
<tr>
<td>Dice Problem</td>
<td>plotting, 182</td>
</tr>
<tr>
<td>Bayes tables, 22</td>
<td>distribution of errors, 116-118</td>
</tr>
<tr>
<td>distribution of sums</td>
<td>empirical versus theoretical, 29</td>
</tr>
<tr>
<td>three dice, 75</td>
<td>exponential distribution, 108</td>
</tr>
<tr>
<td>two dice, 73-76</td>
<td>SciPy expon, 109</td>
</tr>
<tr>
<td>Dungeons &amp; Dragons best three, 86</td>
<td>gluten sensitivity, 76</td>
</tr>
<tr>
<td>Pmf to solve, 38-39</td>
<td>Forward Problem, 77</td>
</tr>
<tr>
<td>updating dice, 39</td>
<td>Inverse Problem, 78</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="308" -->
<!-- PageBreak -->


<table>
<tr>
<th>hypergeometric distribution, 208 joint distributions, 145, 148 (see also joint distributions)</th>
<th rowspan="2">Weibull distribution, 191-194 Dungeons &amp; Dragons dice rolls, 86 distribution as mix of distributions, 90-93 general solution, 93-96</th>
</tr>
<tr>
<th>kernel density estimation, 115</th>
</tr>
<tr>
<td rowspan="2">light bulb lifetime distribution, 199-202 dead bulb prediction, 202</td>
<td></td>
</tr>
<tr>
<td>E</td>
</tr>
<tr>
<td>marginal distributions, 154</td>
<td rowspan="3">Empirical Bayes method using data twice, 237 empiricaldist library, 29 Cdf class, 85</td>
</tr>
<tr>
<td>Dirichlet marginals as beta distributions,</td>
</tr>
<tr>
<td>266</td>
</tr>
<tr>
<td>incomplete data, 197</td>
<td>installation, xi</td>
</tr>
<tr>
<td>joint distributions to, 153-156</td>
<td>Pmf class, 30</td>
</tr>
<tr>
<td>logistic regression, Bayesian, 232 Pmf marginal function, 219 reading improvement, 180 reading improvement compared, 187 snow amounts, 247</td>
<td>errors in document or program (see Lincoln Index Problem) estimating counts counting cells via ABC, 298-302 counting cells via MCMC, 295-297</td>
</tr>
<tr>
<td>median as 50th percentile, 63 Poisson distribution, 100, 103</td>
<td>data in hand, Bayes's theorem not needed, 294</td>
</tr>
<tr>
<td>gamma distribution as conjugate prior, 258</td>
<td>German Tank Problem, 64 Train Problem, 57-60</td>
</tr>
<tr>
<td>probability of superiority, 105</td>
<td>credible intervals, 63</td>
</tr>
<tr>
<td>posterior distribution, 33, 35 (see also posterior distribution)</td>
<td>power law prior, 61 sensitivity to the prior, 60</td>
</tr>
<tr>
<td>predictive distributions</td>
<td>estimating proportions</td>
</tr>
<tr>
<td>posterior, 106, 202, 235-237, 254</td>
<td>Euro Problem</td>
</tr>
<tr>
<td>prior, 270</td>
<td>about, 43</td>
</tr>
<tr>
<td>prior distribution, 32, 34</td>
<td>Bayesian estimation, 47-51</td>
</tr>
<tr>
<td>(see also prior distribution) probability mass functions, 29</td>
<td>Bayesian statistics versus Bayes's theo- rem, 53</td>
</tr>
<tr>
<td>Bayesian updates, 260</td>
<td>binomial distribution, 44</td>
</tr>
<tr>
<td>CDF conversion, 86 coin toss, 30</td>
<td>binomial likelihood function, 51 modeling, 44, 129</td>
</tr>
<tr>
<td>empiricaldist library for Pmf class, 30 (see also Pmf objects)</td>
<td>101 Bowls Problem, 34-37, 52 Euro Problem</td>
</tr>
<tr>
<td>outcomes appearing more than once, 30</td>
<td>about, 43</td>
</tr>
<tr>
<td>sequence of possible outcomes, 30</td>
<td>Bayesian estimation, 47-51</td>
</tr>
<tr>
<td>random samples from (see MCMC (Markov chain Monte Carlo))</td>
<td>binomial distribution, 44 binomial coefficient, 44</td>
</tr>
<tr>
<td>sampling distribution of the mean, 185</td>
<td>conjugate prior of, 261</td>
</tr>
<tr>
<td>sums of three dice, 75, 86 sums of two dice, 73-76</td>
<td>SciPy binomial function, 44 unbiased coin results tested, 46</td>
</tr>
<tr>
<td>Weibull distribution, 191-194 light bulb dead bulb prediction, 202 weighted distributions, 94</td>
<td>binomial likelihood function, 51, 129 conjugate prior of binomial distribution, 261</td>
</tr>
<tr>
<td>dog shelter adoption</td>
<td>cumulative distribution function, 83</td>
</tr>
<tr>
<td>about, 191</td>
<td>modeling, 44, 129, 131</td>
</tr>
<tr>
<td>incomplete data, 194-196 called censored, 195 using, 196-199</td>
<td>101 Bowls Problem contrasted, 52 random versus nonrandom quantities, 52 testing</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="309" -->
<!-- PageBreak -->


<table>
<tr>
<th>about, 129 modeling, 131</th>
<th rowspan="2">two-parameter model, 213 wild animal preserve, 263 groupby for data into groups, 176, 230, 242 GSS (General Social Survey) dataset, 2-5, 7, 11</th>
</tr>
<tr>
<td>modeling triangle-shaped bias, 133 modeling uniform bias, 132 solution review, 129-131</td>
</tr>
<tr>
<td>exponential distribution, 108</td>
<td>$H$</td>
</tr>
<tr>
<td>probability density function of, 109</td>
<td rowspan="3">happiness about, 276 multiple regression via PyMC3 library, 280</td>
</tr>
<tr>
<td>SciPy expon, 109</td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td>F</td>
<td>simple regression, 277</td>
</tr>
<tr>
<td>False value summed, 3</td>
<td rowspan="2">PyMC3 library, 278 SciPy linregress function, 278</td>
</tr>
<tr>
<td>Fifty Challenging Problems in Probability with</td>
</tr>
<tr>
<td>Solutions (Mosteller), 57</td>
<td rowspan="2">Happiness and Life Satisfaction (Ortiz-Ospina and Roser), 276</td>
</tr>
<tr>
<td>floating-point rounding avoided, 22</td>
</tr>
<tr>
<td>Forward Problem of gluten sensitivity distribu-</td>
<td rowspan="2">How Tall Is Person A about, 147</td>
</tr>
<tr>
<td>tion, 77</td>
</tr>
<tr>
<td>fraction of items</td>
<td>B height from A, 156</td>
</tr>
<tr>
<td>probability function computing, 4</td>
<td>independence of A and B, 157</td>
</tr>
<tr>
<td>Series of Boolean values, 3</td>
<td>joint distribution construction, 148</td>
</tr>
<tr>
<td>fractions to avoid floating-point rounding, 22</td>
<td>likelihood, 151 marginal distributions, 153-156</td>
</tr>
<tr>
<td>G</td>
<td>plotting joint distribution, 149</td>
</tr>
<tr>
<td>Gallup World Poll on happiness, 277</td>
<td rowspan="2">prior distribution of height, 147 update, 152</td>
</tr>
<tr>
<td>gamma distribution</td>
</tr>
<tr>
<td>about, 102</td>
<td>hypergeometric distribution, 208</td>
</tr>
<tr>
<td>Bayesian updates via, 259-261</td>
<td>SciPy hypergeom function, 208</td>
</tr>
<tr>
<td>conjugate priors, 258</td>
<td>hypotheses</td>
</tr>
<tr>
<td>goal-scoring rate, 101</td>
<td>any number of</td>
</tr>
<tr>
<td>SciPy gamma function, 102</td>
<td>Cookie Problem with 101 bowls, 34-37</td>
</tr>
<tr>
<td>generator expressions, 13</td>
<td>law of total probability, 20</td>
</tr>
<tr>
<td>German Tank Problem, 64</td>
<td>evidence in favor of, 72, 131</td>
</tr>
<tr>
<td>given (|), 9</td>
<td>Bayes factor, 72, 131, 134, 234</td>
</tr>
<tr>
<td>gluten sensitivity distribution, 76</td>
<td>hypothesis testing, 134</td>
</tr>
<tr>
<td>Forward Problem, 77</td>
<td>(see also testing hypotheses)</td>
</tr>
<tr>
<td>Inverse Problem, 78</td>
<td>decision analysis instead, 134</td>
</tr>
<tr>
<td>goal scoring (see World Cup Problem)</td>
<td>three hypotheses</td>
</tr>
<tr>
<td>Gorman, Kristen, 161</td>
<td>Bayes tables, 22, 23-25</td>
</tr>
<tr>
<td>Gould, Stephen J., 2</td>
<td>coin tossed twice, 44</td>
</tr>
<tr>
<td>Grizzly Bear Problem</td>
<td>Monty Hall Problem, 23-25</td>
</tr>
<tr>
<td>about, 207</td>
<td>two hypotheses</td>
</tr>
<tr>
<td>estimating total population, 209</td>
<td>Bayes tables, 20-22</td>
</tr>
<tr>
<td>probability of observing a bear, 211-215</td>
<td rowspan="4">binomial distribution, 44 law of total probability, 20 updating probability with new data, 19 (see also Bayesian updates)</td>
</tr>
<tr>
<td>hypergeometric distribution, 208</td>
</tr>
<tr>
<td>modeling, 208</td>
</tr>
<tr>
<td>three-parameter model, 263</td>
</tr>
<tr>
<td>two-parameter model, 211-215</td>
<td></td>
</tr>
<tr>
<td>plotting, 210</td>
<td>I</td>
</tr>
<tr>
<td>two-parameter model, 214</td>
<td>incomplete data, 194-196</td>
</tr>
<tr>
<td>update, 209</td>
<td>called censored, 195</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="310" -->
<!-- PageBreak -->


<table>
<tr>
<th>marginal distributions, 197 using, 196-199</th>
<th>reading ability improvement, 177 3-dimensional, 217</th>
</tr>
<tr>
<th>independence and dependence of heights, 157</th>
<th>Jupyter notebooks</th>
</tr>
<tr>
<td>indus 10 industry code, 3</td>
<td>about running notebooks, $\mathrm { X }$</td>
</tr>
<tr>
<td>inference</td>
<td>installing Jupyter, xi</td>
</tr>
<tr>
<td>p-values, 175</td>
<td></td>
</tr>
<tr>
<td>reading ability improvement</td>
<td>K</td>
</tr>
<tr>
<td>about, 175</td>
<td rowspan="2">kernel density estimation (KDE), 115, 116 distribution of differences plotted, 182</td>
</tr>
<tr>
<td>data into DataFrame, 176</td>
</tr>
<tr>
<td>distribution of differences, 181</td>
<td>SciPy gaussian_kde function, 115, 182</td>
</tr>
<tr>
<td>groupby for data into groups, 176</td>
<td>Kidney Tumor Problem</td>
</tr>
<tr>
<td>likelihood, 178</td>
<td>about, 287, 299</td>
</tr>
<tr>
<td>likelihood summary statistics, 184 marginal distributions, 180 marginal distributions compared, 187 prior distribution, 177</td>
<td rowspan="2">Approximate Bayesian Computation, 294 growth model, general, 289 growth model, simple, 288 simulation of growth, 291-294</td>
</tr>
<tr>
<td>probability of superiority, 181</td>
</tr>
<tr>
<td>update, 177-180 update with summary statistics, 186 statistical versus Bayesian, 175</td>
<td>L law of total probability, 11</td>
</tr>
<tr>
<td>Information Theory, Inference, and Learning</td>
<td rowspan="2">Cookie Problem, 18 Price Is Right decision analysis, 122</td>
</tr>
<tr>
<td>Algorithms (MacKay), xiii, 43, 71, 129</td>
</tr>
<tr>
<td>installing Jupyter, xi</td>
<td>total probability of the data, 19</td>
</tr>
<tr>
<td>Inverse Problem of gluten sensitivity distribu- tion, 78</td>
<td>least squares regression marathon world record, 251 snow amounts, 244</td>
</tr>
<tr>
<td>J</td>
<td>light bulb failure time</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>joint distributions</td>
<td>$d e a d \quad b u l b \quad p r e d i c t i o n , 2 0 2$</td>
</tr>
<tr>
<td>about, 145, 148</td>
<td>distribution of lifetimes, 199-202</td>
</tr>
<tr>
<td>constructing, 148</td>
<td>incomplete data, 194-196</td>
</tr>
<tr>
<td>How Tall Is Person A about, 147</td>
<td>called censored, 195 using, 196-199</td>
</tr>
<tr>
<td>B height from A, 156</td>
<td>Weibull distribution, 191-194</td>
</tr>
<tr>
<td>independence of A and B, 157</td>
<td>likelihood, 19</td>
</tr>
<tr>
<td>joint distribution construction, 148</td>
<td>Bayes tables</td>
</tr>
<tr>
<td>likelihood, 151</td>
<td>three hypotheses, 22, 23-25</td>
</tr>
<tr>
<td>marginal distributions, 153-156</td>
<td>two hypotheses, 20-22</td>
</tr>
<tr>
<td>plotting joint distribution, 149 prior distribution of height, 147 update, 152</td>
<td>Bayesian logistic regression, 230 binomial likelihood function, 51, 129 classification of penguin data, 163</td>
</tr>
<tr>
<td>marginal distributions from, 153-156 outer operations, 145</td>
<td>computing for entire dataset at once, 51 dictionary to hold, 48</td>
</tr>
<tr>
<td>comparison operators, 146, 151</td>
<td rowspan="2">Grizzly Bear with two parameters, 213 How Tall Is Person A, 151 B height from A, 156</td>
</tr>
<tr>
<td>joint distribution construction, 148 outer product, 145</td>
</tr>
<tr>
<td>outer sum, 146</td>
<td rowspan="2">likelihood ratios as Bayes factors, 234 posterior odds, 71</td>
</tr>
<tr>
<td>plotting, 149</td>
</tr>
<tr>
<td>contour of Pmf Series, 214 scatter plot of penguin data, 168</td>
<td>reading ability improvement, 178 snow amounts, 246</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="311" -->
<!-- PageBreak -->


<table>
<tr>
<th>summary statistics for larger datasets, 184, 247</th>
<th>logistic regression, non-Bayesian, 228 modeling, 237</th>
</tr>
<tr>
<td>time between goals, 108</td>
<td>modeling, logistic model, 227, 237</td>
</tr>
<tr>
<td>too small for floating-point arithmetic, 184, 247</td>
<td>predictions about O-rings, 235-237 statsmodels for non-Bayesian, 228</td>
</tr>
<tr>
<td>Train Problem, 57</td>
<td></td>
</tr>
<tr>
<td>uniform prior, 47, 129</td>
<td>M</td>
</tr>
<tr>
<td>wrong classroom, 224</td>
<td>MacKay, David, xiii, 43, 71, 129</td>
</tr>
<tr>
<td>Lincoln Index Problem, 215-217 modeling three parameters, 217 modeling two testers, 215</td>
<td>MAP as highest posterior probability, 37 coin tossed twice, 45 computing, 37</td>
</tr>
<tr>
<td>Linda the Banker Problem, 1</td>
<td>marathon world record</td>
</tr>
<tr>
<td>linear regression</td>
<td>about, 250</td>
</tr>
<tr>
<td>about, 242</td>
<td>least squares regression, 251</td>
</tr>
<tr>
<td>least squares regression</td>
<td>likelihoods, 252</td>
</tr>
<tr>
<td>marathon world record, 251 snow amounts, 244 marathon world record, 250</td>
<td>marginal distributions, 252 prediction of time-barrier broken, 254 priors, 252</td>
</tr>
<tr>
<td>mathematical model, 243</td>
<td>marginal distributions, 154</td>
</tr>
<tr>
<td>residuals, 245 SciPy linregress function, 278</td>
<td>Dirichlet distribution marginals as beta dis- tributions, 266</td>
</tr>
<tr>
<td>snow amounts, 241-250</td>
<td>incomplete data, 197</td>
</tr>
<tr>
<td>likelihood, 246</td>
<td rowspan="3">joint distributions to, 153-156 logistic regression, Bayesian, 232 Pmf marginal function, 219 reading ability improvement, 180</td>
</tr>
<tr>
<td>priors, 245</td>
</tr>
<tr>
<td>residuals, 245, 246 update, 247</td>
</tr>
<tr>
<td>locomotive count estimation, 57-60</td>
<td></td>
</tr>
<tr>
<td>log odds</td>
<td>comparing, 187 snow amounts, 247</td>
</tr>
<tr>
<td>about, 225, 241</td>
<td rowspan="2">mark and recapture experiments about, 207</td>
</tr>
<tr>
<td>explanatory and dependent variables, 226</td>
</tr>
<tr>
<td>probabilities from, 228, 233</td>
<td rowspan="2">Grizzly Bear Problem about, 207</td>
</tr>
<tr>
<td>SciPy expit function, 228, 231, 233</td>
</tr>
<tr>
<td>Space Shuttle Problem, 231, 233 wrong classroom, 223-226</td>
<td>estimating total population, 209 modeling, 208</td>
</tr>
<tr>
<td>logical AND (see conjunctions)</td>
<td rowspan="2">modeling two parameters, 211-215 update, 209</td>
</tr>
<tr>
<td>logistic regression</td>
</tr>
<tr>
<td>about, 223, 241</td>
<td>update with two parameters, 213</td>
</tr>
<tr>
<td>$$l i k e l i h o o d , 2 3 0$$</td>
<td>hypergeometric distribution, 208 Lincoln Index Problem, 215-217</td>
</tr>
<tr>
<td>marginal distributions, 232 prior distribution, 229</td>
<td>modeling three parameters, 217 modeling two testers, 215</td>
</tr>
<tr>
<td>transforming distributions, 233 update, 231</td>
<td>Markov chain (see MCMC (Markov chain Monte Carlo))</td>
</tr>
<tr>
<td>Empirical Bayes method, 237</td>
<td rowspan="2">mathematical notation for probability, 8 Bayes's theorem, 10, 70</td>
</tr>
<tr>
<td>log odds, 223-226</td>
</tr>
<tr>
<td>predictive distributions, 235-237</td>
<td rowspan="3">conditional probability and conjunctions, 9 conjunctions as commutative, 10 law of total probability, 11</td>
</tr>
<tr>
<td>Space Shuttle Problem</td>
</tr>
<tr>
<td>about, 226</td>
</tr>
<tr>
<td>logistic regression, Bayesian, 229-232</td>
<td>power law, 61</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="312" -->
<!-- PageBreak -->


<table>
<tr>
<th>regression model, 243</th>
<th>joint distribution construction, 148</th>
</tr>
<tr>
<td>matplotlib</td>
<td>outer sum, 146</td>
</tr>
<tr>
<td>installation, $\mathrm { x i }$</td>
<td>3-dimensional for reading ability, 178</td>
</tr>
<tr>
<td>joint distribution plotted, 149</td>
<td>Model object, 272</td>
</tr>
<tr>
<td>scatter plot, 168</td>
<td>modeling</td>
</tr>
<tr>
<td>matrix transposition, 95</td>
<td>about modeling errors, $\mathrm { X }$</td>
</tr>
<tr>
<td>maximizing expected gain, 124</td>
<td>all models wrong, 99</td>
</tr>
<tr>
<td>McGrayne, Sharon Bertsch, 53</td>
<td>8 parameters via PyMC3, 280</td>
</tr>
<tr>
<td>MCMC (Markov chain Monte Carlo)</td>
<td>Euro Problem, 44, 129, 131</td>
</tr>
<tr>
<td>about, 269</td>
<td>triangle-shaped bias, 133</td>
</tr>
<tr>
<td>happiness</td>
<td>uniform bias, 132</td>
</tr>
<tr>
<td>about, 276</td>
<td>gluten sensitivity distribution, 77</td>
</tr>
<tr>
<td>multiple regression, PyMC3 library, 280</td>
<td>Grizzly Bear Problem, 208</td>
</tr>
<tr>
<td>simple regression, 277</td>
<td>two-parameter model, 211-215</td>
</tr>
<tr>
<td>simple regression, PyMC3 library, 278</td>
<td>informative versus uninformative prior, 65</td>
</tr>
<tr>
<td>simple regression, SciPy linregress, 278</td>
<td>Kidney Tumor Problem</td>
</tr>
<tr>
<td>PyMC3 library, 271</td>
<td>growth model, general, 289</td>
</tr>
<tr>
<td>about, 274</td>
<td>growth model, simple, 288</td>
</tr>
<tr>
<td>inference, 274</td>
<td>Lincoln Index Problem</td>
</tr>
<tr>
<td>sampling the posterior predictive distri-</td>
<td>three parameters, 217</td>
</tr>
<tr>
<td>bution, 275</td>
<td>two testers, 215</td>
</tr>
<tr>
<td>sampling the prior, 272</td>
<td>Price Is Right Problem, 116</td>
</tr>
<tr>
<td>World Cup Problem, 269-276</td>
<td>Space Shuttle Problem, 237</td>
</tr>
<tr>
<td>gamma distribution prior, 270</td>
<td>logistic model, 227, 237</td>
</tr>
<tr>
<td>goal-scoring rate possible values, 270</td>
<td>3 parameters</td>
</tr>
<tr>
<td>inference, 274</td>
<td>Lincoln Index Problem, 217</td>
</tr>
<tr>
<td>Poisson process review, 269</td>
<td>simple regression via PyMC3, 278</td>
</tr>
<tr>
<td>predicting rematch, 275</td>
<td>snow amounts, 241</td>
</tr>
<tr>
<td>PyMC3 library, 271</td>
<td>wild animal preserve, 263</td>
</tr>
<tr>
<td>sampling the prior, 272</td>
<td>World Cup Problem, 99, 105</td>
</tr>
<tr>
<td>mean function</td>
<td>PyMC3, 271</td>
</tr>
<tr>
<td>centering data to minimize correlation, 232,</td>
<td>monster combat (see Dungeons &amp; Dragons)</td>
</tr>
<tr>
<td>244</td>
<td rowspan="2">Monte Carlo (see MCMC (Markov chain Monte Carlo))</td>
</tr>
<tr>
<td>fraction computed via, 3, 9</td>
</tr>
<tr>
<td>mean of posterior distribution, 59, 62</td>
<td>Monty Hall Problem via Bayes tables, 23-25</td>
</tr>
<tr>
<td>Bayesian updates and, 105</td>
<td>Mosteller, Frederick, 57</td>
</tr>
<tr>
<td>distribution skew, 210</td>
<td>MultiIndex</td>
</tr>
<tr>
<td>joint distributions, 201</td>
<td>Bayesian logistic regression, 229</td>
</tr>
<tr>
<td>multivariate normal distribution, 170</td>
<td>Pmf objects, 213, 218, 229</td>
</tr>
<tr>
<td>sampling distribution of the mean, 185</td>
<td>Series in pandas, 203, 213</td>
</tr>
<tr>
<td>mean squared error, 60</td>
<td>3-dimensional joint distribution, 218</td>
</tr>
<tr>
<td>MECE (mutually exclusive and collectively exhaustive), 12</td>
<td>multinomial distribution conjugate prior, 264 multinomial function in SciPy, 212, 219</td>
</tr>
<tr>
<td>median of distribution percentile, 63</td>
<td rowspan="2">multiple regression via PyMC3 library, 280 multivariate Dirichlet distribution, 264</td>
</tr>
<tr>
<td>mesh grids</td>
</tr>
<tr>
<td>comparison operators, 146</td>
<td>multivariate normal distribution, 170</td>
</tr>
<tr>
<td>height arrays, 151</td>
<td>mutually exclusive, 11</td>
</tr>
<tr>
<td>likelihood of height of person, 151 outer product, 145</td>
<td>law of total probability, 11, 19</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="313" -->
<!-- PageBreak -->


<table>
<tr>
<th>mutually exclusive and collectively exhaustive (MECE), 12</th>
<th>Cookie Problem, 72 Bayes's rule, 71 log odds</th>
</tr>
<tr>
<td>$\mathrm { N }$</td>
<td>about, 225, 241</td>
</tr>
<tr>
<td>NaN as not a number, 94</td>
<td rowspan="2">explanatory and dependent variables, 226</td>
</tr>
<tr>
<td>normal distribution</td>
</tr>
<tr>
<td>average height of male adults, 147</td>
<td rowspan="4">probabilities from, 228, 233 SciPy expit function, 228, 231, 233 Space Shuttle Problem, 231, 233 wrong classroom, 223-226</td>
</tr>
<tr>
<td>classification of penguin data, 163, 169</td>
</tr>
<tr>
<td>multivariate, 170</td>
</tr>
<tr>
<td>probability density as Pmf normalized, 147</td>
</tr>
<tr>
<td>reading improvement groups, 177</td>
<td rowspan="3">odds against an event, 70 odds in favor of an event, 69 Oliver's Blood, 71-73</td>
</tr>
<tr>
<td>SciPy norm function, 147, 163</td>
</tr>
<tr>
<td>probability density function, 147, 164</td>
</tr>
<tr>
<td>snow amounts, 243</td>
<td>probability from, 70</td>
</tr>
<tr>
<td>univariate, 170</td>
<td>Oliver's Blood, 71-73</td>
</tr>
<tr>
<td>update with summary statistics, 188</td>
<td>101 Bowls Problem, 34-37</td>
</tr>
<tr>
<td>normalization, 22</td>
<td rowspan="3">Euro Problem contrasted, 52 one-armed bandits (see Bayesian Bandit strat- egy)</td>
</tr>
<tr>
<td>joint posterior distribution, 152</td>
</tr>
<tr>
<td>normalizing constant, 22</td>
</tr>
<tr>
<td>outside of dataset loop, 48</td>
<td>Ortiz-Ospina, Esteban, 276</td>
</tr>
<tr>
<td>Pmf function, 32</td>
<td>outcomes</td>
</tr>
<tr>
<td>notebooks (Jupyter)</td>
<td>Dice Problem, 22</td>
</tr>
<tr>
<td>about running notebooks, $x$</td>
<td>distribution as set of possible, 29</td>
</tr>
<tr>
<td>installing Jupyter, xi</td>
<td rowspan="2">outcomes appearing more than once, 30 probability mass functions, 29</td>
</tr>
<tr>
<td>np alias for NumPy, 34</td>
</tr>
<tr>
<td>null hypothesis significance testing, 175</td>
<td>sequence of possible outcomes, 30</td>
</tr>
<tr>
<td>NumPy</td>
<td>impossible outcomes, 40</td>
</tr>
<tr>
<td>array of values, 44</td>
<td>outer operations, 145</td>
</tr>
<tr>
<td>DataFrame converted to, 149</td>
<td rowspan="3">comparison operators, 146 height arrays, 151 outer product, 145</td>
</tr>
<tr>
<td>meshgrid function outer operations, 145</td>
</tr>
<tr>
<td>normal distribution of height, 147</td>
</tr>
<tr>
<td>repeat function, 200</td>
<td rowspan="2">joint distribution construction, 148 outer sum, 146</td>
</tr>
<tr>
<td>triangle-shaped prior, 49</td>
</tr>
<tr>
<td>weighted mixture of distributions, 95 where function, 151</td>
<td>$P$</td>
</tr>
<tr>
<td>Cookie Problem with 101 bowls, 34-37</td>
<td>$P \left( A \right) , 8$</td>
</tr>
<tr>
<td>cumsum function, 84, 85</td>
<td>$P \left( A \quad a n d \quad B \right) ,$ 9</td>
</tr>
<tr>
<td>diff function, 86</td>
<td>$\mathrm { P } \left( \mathrm { A } \mid \mathrm { B } \right) ,$ 9</td>
</tr>
<tr>
<td>import as np, 34</td>
<td>$\mathrm { P } \left( \mathrm { B } \mid \mathrm { A } \right)$ to $\mathrm { P } \left( \mathrm { A } \mid \mathrm { B } \right)$ via Bayes's theorem, 19</td>
</tr>
<tr>
<td>installation, xi</td>
<td>p-values, 134, 175</td>
</tr>
<tr>
<td>mean of posterior distribution, 59</td>
<td>pandas</td>
</tr>
<tr>
<td></td>
<td>Bayes table in DataFrame</td>
</tr>
<tr>
<td>O</td>
<td>three hypotheses, 22</td>
</tr>
<tr>
<td>O-rings on shuttles (see Space Shuttle Problem) odds</td>
<td>two hypotheses, 20-22 data held by DataFrame, 2</td>
</tr>
<tr>
<td>about, 69</td>
<td>distribution as mix of distributions, 94</td>
</tr>
<tr>
<td>Bayes factor, 72</td>
<td rowspan="2">gluten sensitivity Inverse Problem, 78 light bulb lifetime data, 199</td>
</tr>
<tr>
<td>Bayes's rule, 70</td>
</tr>
<tr>
<td>Bayes's theorem in odds form, 70</td>
<td>penguin data, 161, 163</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="314" -->
<!-- PageBreak -->


<table>
<tr>
<th>reading ability improvement, 176</th>
<th>contour plot, 150, 214</th>
</tr>
<tr>
<td>summing row of DataFrame, 95</td>
<td>posterior distribution, 279</td>
</tr>
<tr>
<td>transposing rows and columns, 95</td>
<td>Grizzly Bear, 210</td>
</tr>
<tr>
<td>DataFrame converted from Series, 214</td>
<td>Grizzly Bear two-parameter model, 214</td>
</tr>
<tr>
<td>DataFrame converted to Series, 202, 213</td>
<td>scatter plot of penguin data, 168</td>
</tr>
<tr>
<td>installation, $\mathrm { x i }$</td>
<td>contours of joint distribution compared,</td>
</tr>
<tr>
<td>joint distribution in DataFrame, 149</td>
<td>169</td>
</tr>
<tr>
<td>converting to Series, 202</td>
<td>Weibull distribution, 193</td>
</tr>
<tr>
<td>3-dimensional joint distribution, 217</td>
<td>incomplete data, 197</td>
</tr>
<tr>
<td>NumPy array from DataFrame, 149</td>
<td>plus (+) versus Pmf.add_dist(), 93</td>
</tr>
<tr>
<td>outer product of DataFrame, 146</td>
<td>Pmf objects</td>
</tr>
<tr>
<td>read .csv file of data</td>
<td>about, 29, 31, 33</td>
</tr>
<tr>
<td>light bulb lifetime data, 199</td>
<td>add_dist function, 75</td>
</tr>
<tr>
<td>penguin data, 161</td>
<td>plus (+) operator versus, 93</td>
</tr>
<tr>
<td>Price Is Right Problem, 114</td>
<td>binomial likelihood function, 51, 129</td>
</tr>
<tr>
<td>reading ability, 176</td>
<td>Cdf object conversion, 86</td>
</tr>
<tr>
<td>snow amounts, 242</td>
<td>coin toss, 30</td>
</tr>
<tr>
<td>Series</td>
<td>coin tossed twice, 44</td>
</tr>
<tr>
<td>Boolean values, 3</td>
<td>Cookie Problem, 32-34</td>
</tr>
<tr>
<td>(see also Boolean Series)</td>
<td>101 bowls of cookies, 34-37</td>
</tr>
<tr>
<td>cumsum results, 84</td>
<td>updated data, 33</td>
</tr>
<tr>
<td>DataFrame converted from, 214</td>
<td>credible_interval function, 64</td>
</tr>
<tr>
<td>DataFrame converted to, 202, 213</td>
<td>Dice Problem, 38-39</td>
</tr>
<tr>
<td>DataFrame.sum function, 149</td>
<td>6-sided best three of four rolls, 86</td>
</tr>
<tr>
<td>MAP computation, 37</td>
<td>updating dice, 39</td>
</tr>
<tr>
<td>MultiIndex, 203, 213</td>
<td>distribution as mix of distributions, 90-93</td>
</tr>
<tr>
<td>Pmf class, 31</td>
<td>general solution, 93-96</td>
</tr>
<tr>
<td>penguin data classification</td>
<td>distribution of differences, 181</td>
</tr>
<tr>
<td>about, 161</td>
<td>plotting, 182</td>
</tr>
<tr>
<td>cumulative distribution functions, 162</td>
<td>distribution of sums of two dice, 73-76</td>
</tr>
<tr>
<td>data description, 161</td>
<td>empiricaldist library for Pmf class, 30</td>
</tr>
<tr>
<td>data source, 161</td>
<td>joint distribution construction, 148</td>
</tr>
<tr>
<td>joint distributions, 168</td>
<td>light bulb lifetimes, 199</td>
</tr>
<tr>
<td>scatter plot, 168</td>
<td>loop iterator items(), 64</td>
</tr>
<tr>
<td>scatter plot compared to contours, 169</td>
<td>marginal function, 219</td>
</tr>
<tr>
<td>less naive Bayesian classifier, 172</td>
<td>maximum posterior probability, 37</td>
</tr>
<tr>
<td>loading into DataFrame, 161</td>
<td>coin tossed twice, 45</td>
</tr>
<tr>
<td>multivariate normal distribution, 170</td>
<td>mean of posterior distribution, 59</td>
</tr>
<tr>
<td>normal models, 163, 169</td>
<td>MultiIndex, 213, 218, 229</td>
</tr>
<tr>
<td>update, 164-168</td>
<td>normal distribution of penguin data, 169</td>
</tr>
<tr>
<td>naive Bayesian classification, 166</td>
<td>normalize function, 32, 48</td>
</tr>
<tr>
<td>percentiles</td>
<td>outcomes appearing more than once, 30</td>
</tr>
<tr>
<td>marathon world record, 254</td>
<td>percentile rank, 63</td>
</tr>
<tr>
<td>summarizing posterior distribution, 63</td>
<td>Poisson distribution, 100</td>
</tr>
<tr>
<td>quantiles versus, 64</td>
<td>posterior predictive distribution, 106</td>
</tr>
<tr>
<td>physical quantities as random, 53</td>
<td>probability densities as normal distribution,</td>
</tr>
<tr>
<td>plotting</td>
<td>147</td>
</tr>
<tr>
<td>distribution of differences as noisy, 182</td>
<td>probability of superiority, 105, 181</td>
</tr>
<tr>
<td>joint distribution, 149</td>
<td>probability that threshold exceeded, 46</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="315" -->
<!-- PageBreak -->


<table>
<tr>
<th>prob_gt function, 106, 181</th>
<th>Dice Problem, 38</th>
</tr>
<tr>
<td>sequence of possible outcomes, 30</td>
<td rowspan="3">101 hypotheses, 34-37 two hypotheses, 32 two hypotheses, updated data, 33</td>
</tr>
<tr>
<td>triangle-shaped prior, 49</td>
</tr>
<tr>
<td>uniform prior for reading ability, 177</td>
</tr>
<tr>
<td>point estimates from non-Bayesian logistic regression, 228</td>
<td>posterior distribution, 33, 35 (see also posterior distribution)</td>
</tr>
<tr>
<td>Poisson distribution, 100, 103</td>
<td>posterior mean, 59, 62</td>
</tr>
<tr>
<td>gamma distribution as conjugate prior, 258</td>
<td>Bayesian updates and, 105</td>
</tr>
<tr>
<td>Poisson processes</td>
<td>distribution skew, 210</td>
</tr>
<tr>
<td>about, 99</td>
<td>joint distributions, 201</td>
</tr>
<tr>
<td>exponential distribution, 108</td>
<td>power law prior, 61</td>
</tr>
<tr>
<td>gamma distribution, 101</td>
<td>sensitivity to prior, 60</td>
</tr>
<tr>
<td>Poisson distribution, 100, 103</td>
<td>posterior odds, 71, 72</td>
</tr>
<tr>
<td>gamma distribution as conjugate prior,</td>
<td rowspan="3">subjective, 52 Train Problem, 59 power law prior, 62</td>
</tr>
<tr>
<td>258</td>
</tr>
<tr>
<td>poisson object in SciPy, 100</td>
</tr>
<tr>
<td>probability of superiority, 105</td>
<td>unnormalized, 21, 32</td>
</tr>
<tr>
<td>update, 103</td>
<td>normalization, 22, 32, 152</td>
</tr>
<tr>
<td>posterior distribution, 33, 35</td>
<td>power law prior, 61</td>
</tr>
<tr>
<td>Bayesian update, 105</td>
<td>predictive distributions</td>
</tr>
<tr>
<td>Euro Problem</td>
<td>posterior</td>
</tr>
<tr>
<td>Bayesian estimation, 49, 51, 130 cumulative distribution function, 83</td>
<td>light bulb lifetime, 202 marathon world record, 254</td>
</tr>
<tr>
<td>gluten sensitivity Inverse Problem, 79</td>
<td>Space Shuttle O-ring damage, 235-237</td>
</tr>
<tr>
<td>joint posterior distribution, 152</td>
<td>World Cup Problem, 106</td>
</tr>
<tr>
<td>posterior distributions from, 153</td>
<td>prior</td>
</tr>
<tr>
<td>mean of, 59, 62</td>
<td>World Cup Problem, 270</td>
</tr>
<tr>
<td>parameter meanings, 261</td>
<td>Price Is Right Problem</td>
</tr>
<tr>
<td>percentiles to summarize, 63</td>
<td>about, 113</td>
</tr>
<tr>
<td>plotting, 279</td>
<td>decision analysis, 122</td>
</tr>
<tr>
<td>Grizzly Bear, 210</td>
<td>distribution of errors, 116-118</td>
</tr>
<tr>
<td>Grizzly Bear two-parameter model, 214</td>
<td rowspan="3">kernel density estimation, 115, 116 maximizing expected gain, 124 modeling, 116</td>
</tr>
<tr>
<td>posterior predictive distribution</td>
</tr>
<tr>
<td>light bulb lifetime, 202</td>
</tr>
<tr>
<td>marathon world record, 254</td>
<td>prior, 114</td>
</tr>
<tr>
<td>Space Shuttle O-ring damage, 235-237</td>
<td>probability of winning, 120</td>
</tr>
<tr>
<td>World Cup Problem, 106</td>
<td>update, 118</td>
</tr>
<tr>
<td>sensitivity to the prior, 60</td>
<td>prior distribution, 32, 34</td>
</tr>
<tr>
<td>slot machine selection, 140</td>
<td>Bayesian logistic regression, 229</td>
</tr>
<tr>
<td>posterior probability, 19</td>
<td>classification of penguin data, 163</td>
</tr>
<tr>
<td>Bayes factor reported instead of, 134</td>
<td>different lengths for snow amounts, 245</td>
</tr>
<tr>
<td>Bayes tables</td>
<td>Empirical Bayes method, 237</td>
</tr>
<tr>
<td>three hypotheses, 22-25</td>
<td>informative prior, 65</td>
</tr>
<tr>
<td>two hypotheses, 20-22</td>
<td>Pmf for Dice Problem, 38</td>
</tr>
<tr>
<td>conditional posteriors, 156</td>
<td>Price Is Right Problem, 114</td>
</tr>
<tr>
<td>MAP as highest, 37</td>
<td>kernel density estimation, 115</td>
</tr>
<tr>
<td>coin tossed twice, 45</td>
<td>prior predictive distribution, 270</td>
</tr>
<tr>
<td>computing, 37</td>
<td>reading ability improvement, 177</td>
</tr>
<tr>
<td>Pmf</td>
<td>uninformative prior, 65</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="316" -->
<!-- PageBreak -->


<table>
<tr>
<th>prior probability, 19</th>
<th>Bayesian updates, 260</th>
</tr>
<tr>
<td>Bayes tables</td>
<td>gamma distribution, 102</td>
</tr>
<tr>
<td>three hypotheses, 22-25</td>
<td>norm object returning, 164</td>
</tr>
<tr>
<td>two hypotheses, 20-22</td>
<td>reading ability improvement, 179</td>
</tr>
<tr>
<td>Euro versus 101 Bowls Problems, 52</td>
<td>SciPy pdf function, 147</td>
</tr>
<tr>
<td>Pmf</td>
<td>time between goals, 108</td>
</tr>
<tr>
<td>Dice Problem, 38</td>
<td>probability mass functions (PMF)</td>
</tr>
<tr>
<td>101 hypotheses, 34-37</td>
<td>about, 29</td>
</tr>
<tr>
<td>two hypotheses, 32</td>
<td>Bayesian updates, 260</td>
</tr>
<tr>
<td>posterior odds, 71, 72</td>
<td>CDF conversion, 86</td>
</tr>
<tr>
<td>power law prior, 61</td>
<td>coin toss, 30</td>
</tr>
<tr>
<td>prior distribution, 32, 34</td>
<td>outcomes appearing more than once, 30</td>
</tr>
<tr>
<td>(see also prior distribution)</td>
<td>Pmf class (see Pmf objects)</td>
</tr>
<tr>
<td>prior odds, 72</td>
<td>sequence of possible outcomes, 30</td>
</tr>
<tr>
<td>sensitivity to the prior, 60</td>
<td>probability of superiority</td>
</tr>
<tr>
<td>subjective priors, 52</td>
<td>reading ability improvement, 181</td>
</tr>
<tr>
<td>swamping the priors, 51</td>
<td>World Cup Problem, 105</td>
</tr>
<tr>
<td>Train Problem, 57, 61</td>
<td>proportion estimation (see estimating propor-</td>
</tr>
<tr>
<td>triangle-shaped prior, 49</td>
<td>tions)</td>
</tr>
<tr>
<td>triangle-shaped bias, 133</td>
<td>PyMC3 library</td>
</tr>
<tr>
<td>uniform prior</td>
<td>about, 271, 274</td>
</tr>
<tr>
<td>Bayesian $\mathrm { R a n d i t } \mathrm { s t r a t e g y } ,$ 135</td>
<td>happiness, 276-282</td>
</tr>
<tr>
<td>beta distribution, 262</td>
<td>importing as pm, 272</td>
</tr>
<tr>
<td>Euro Problem, 47, 51, 129</td>
<td>inference, 274</td>
</tr>
<tr>
<td>gluten sensitivity Inverse Problem, 79</td>
<td>Model object, 272</td>
</tr>
<tr>
<td>reading ability improvement, 177</td>
<td>multiple regression, 280</td>
</tr>
<tr>
<td>Train Problem, 58</td>
<td>sampling the prior, 272</td>
</tr>
<tr>
<td>probability</td>
<td>simple regression, 278</td>
</tr>
<tr>
<td>counting to compute, 2, 294</td>
<td>World Cup Problem, 270-276</td>
</tr>
<tr>
<td>dataset size, 184</td>
<td>Python</td>
</tr>
<tr>
<td>defining, 2</td>
<td>about running notebooks, $\mathrm { X }$</td>
</tr>
<tr>
<td>log odds converted to, 228</td>
<td>Anaconda distribution, xi</td>
</tr>
<tr>
<td>mathematical notation for, 8</td>
<td>installation, xi</td>
</tr>
<tr>
<td>Bayes's theorem, 10, 70</td>
<td>PyMC3 library</td>
</tr>
<tr>
<td>conditional probability and conjunc-</td>
<td>about, 271, 274</td>
</tr>
<tr>
<td>tions, 9</td>
<td>happiness, $2 7 6 - 2 8 2$</td>
</tr>
<tr>
<td>conjunctions as commutative, 10</td>
<td>importing as pm, 272</td>
</tr>
<tr>
<td>law of total probability, 11</td>
<td>inference, 274</td>
</tr>
<tr>
<td>power law, 61</td>
<td>Model object, 272</td>
</tr>
<tr>
<td>regression model, 243</td>
<td>multiple regression, 280</td>
</tr>
<tr>
<td>odds as degree of certainty, 69</td>
<td>sampling the prior, 272</td>
</tr>
<tr>
<td>(see also odds)</td>
<td>simple regression, 278</td>
</tr>
<tr>
<td>probability from, 70, 228</td>
<td>World Cup Problem, 270-276</td>
</tr>
<tr>
<td>probability function returning, 4-5</td>
<td>with statement, 272</td>
</tr>
<tr>
<td>conditional probability function, 7</td>
<td></td>
</tr>
<tr>
<td>random versus nonrandom quantities, 52</td>
<td>Q</td>
</tr>
<tr>
<td>Bayesian interpretation of random, 53</td>
<td rowspan="2">quantiles Cdf objects to compute, 86</td>
</tr>
<tr>
<td>probability densities, 102, 109, 147</td>
</tr>
<tr>
<td>probability density function (PDF)</td>
<td>percentiles versus, 64</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="317" -->
<!-- PageBreak -->


<table>
<tr>
<th>R random distributions (see Poisson processes)</th>
<th>linregress function for simple regression, 278</th>
</tr>
<tr>
<td>random sampling, 2</td>
<td rowspan="3">multinomial function, 212, 219 multivariate_normal function, 170 norm function for normal distribution, 147,</td>
</tr>
<tr>
<td>from a distribution (see MCMC (Markov</td>
</tr>
<tr>
<td>chain Monte Carlo))</td>
</tr>
<tr>
<td>Thompson sampling, 139</td>
<td>163</td>
</tr>
<tr>
<td>random versus nonrandom quantities, 52</td>
<td>pdf function, 147, 164</td>
</tr>
<tr>
<td>physical quantities as random, 53</td>
<td>poisson object, 100</td>
</tr>
<tr>
<td>ratios of probabilities as odds, 69</td>
<td>Weibull distribution, 191</td>
</tr>
<tr>
<td>reading ability improvement</td>
<td>sequence of possible outcomes, 30</td>
</tr>
<tr>
<td>about, 175</td>
<td>6-sided dice</td>
</tr>
<tr>
<td>data into DataFrame, 176</td>
<td>best three of four rolls, 86</td>
</tr>
<tr>
<td>distribution of differences, 181</td>
<td>box of three dice, 22</td>
</tr>
<tr>
<td>likelihood, 178</td>
<td>Pmf to solve, 38-39</td>
</tr>
<tr>
<td>summary statistics, 184</td>
<td rowspan="2">distribution as mix of distributions, 90-93 general solution, 93-96</td>
</tr>
<tr>
<td>marginal distributions, 180</td>
</tr>
<tr>
<td>comparing, 187</td>
<td>slot machines (see Bayesian Bandit strategy)</td>
</tr>
<tr>
<td>prior distribution, 177</td>
<td>snow amounts</td>
</tr>
<tr>
<td>probability of superiority, 181</td>
<td>about, 241</td>
</tr>
<tr>
<td>update, 177-180</td>
<td>fond memories of, 250</td>
</tr>
<tr>
<td>summary statistics, 186</td>
<td>least squares regression, 244</td>
</tr>
<tr>
<td>regression, 243</td>
<td>likelihood, 246</td>
</tr>
<tr>
<td>(see also linear regression)</td>
<td>marginal distributions, 247</td>
</tr>
<tr>
<td>PyMC3 library for multiple regression, 280</td>
<td>normal distribution assumption, 243</td>
</tr>
<tr>
<td>PyMC3 library for simple regression, 278</td>
<td>priors, 245</td>
</tr>
<tr>
<td>SciPy linregress function for simple regres- sion, 278</td>
<td>regression model, 243 update, 247</td>
</tr>
<tr>
<td>residuals of regression, 245, 246, 252</td>
<td>soccer goal scoring (see World Cup Problem)</td>
</tr>
<tr>
<td>resources</td>
<td>Space Shuttle Problem</td>
</tr>
<tr>
<td>Anaconda distribution of Python, $\mathrm { x i }$</td>
<td>about, 226</td>
</tr>
<tr>
<td>book web page, xiii</td>
<td>logistic regression, Bayesian, 229-232</td>
</tr>
<tr>
<td>URL with links to all notebooks, x</td>
<td>logistic regression, non-Bayesian, 228</td>
</tr>
<tr>
<td>Roser, Max, 276</td>
<td>modeling, 237</td>
</tr>
<tr>
<td>rounding avoided with fractions, 22</td>
<td>logistic model, 227, 237 predictions about O-ring damage, 235-237</td>
</tr>
<tr>
<td>S</td>
<td>spam filters as classification, 161</td>
</tr>
<tr>
<td>sampling distribution of the mean, 185</td>
<td rowspan="2">stack function converting DataFrame to Series, 202, 213 Pmf with two levels in index, 229</td>
</tr>
<tr>
<td>sampling from a distribution (see MCMC</td>
</tr>
<tr>
<td>(Markov chain Monte Carlo))</td>
<td>standard deviation</td>
</tr>
<tr>
<td>SciPy</td>
<td>How Tall Is Person A, 147, 156</td>
</tr>
<tr>
<td>beta function for beta distribution, 261</td>
<td>normal distribution</td>
</tr>
<tr>
<td>binomial function, 44</td>
<td rowspan="3">classification of penguin data, 163 How Tall Is Person A, 147 multivariate, 170</td>
</tr>
<tr>
<td>binomial likelihood function, 51</td>
</tr>
<tr>
<td>expit function, 228, 231</td>
</tr>
<tr>
<td>exponential distribution, 109</td>
<td rowspan="2">Price Is Right Problem, 117 snow amounts, 243</td>
</tr>
<tr>
<td>gamma distribution function, 102</td>
</tr>
<tr>
<td>hypergeometric distribution function, 208 installation, $\mathrm { X i }$</td>
<td>univariate, 170</td>
</tr>
<tr>
<td>kernel density estimation, 115, 182</td>
<td></td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="318" -->
<!-- PageBreak -->


<table>
<tr>
<td>Pmf approximating normal distribution, 169</td>
<td>binomial distribution, 46, 130 modeling, 131</td>
</tr>
<tr>
<td>reading ability improvement, 179, 184, 186</td>
<td rowspan="2">modeling triangle-shaped bias, 133 modeling uniform bias, 132 solution review, 129-131</td>
</tr>
<tr>
<td>residuals as estimate of sigma, 245, 252 snow amounts, 243-248</td>
</tr>
<tr>
<td>sigma as nuisance parameter, 248</td>
<td>statistical versus Bayesian, 134</td>
</tr>
<tr>
<td>statistical versus Bayesian hypothesis testing,</td>
<td>theoretical versus empirical distributions, 29</td>
</tr>
<tr>
<td>134</td>
<td rowspan="2">The Theory That Would Not Die (McGrayne), 53</td>
</tr>
<tr>
<td>statistical versus Bayesian inference, 175</td>
</tr>
<tr>
<td>statistics (Bayesian) versus Bayes's theorem, 53</td>
<td>Thompson sampling, 139</td>
</tr>
<tr>
<td>statsmodels for non-Bayesian logistic regres-</td>
<td>time delta from Timestamps, 251</td>
</tr>
<tr>
<td>sion, 228</td>
<td>Timestamp objects, 251</td>
</tr>
<tr>
<td>Empirical Bayes method, 237</td>
<td>total probability of the data, 19</td>
</tr>
<tr>
<td>least squares regression</td>
<td>normalizing $\begin{array}{} { \text { constan } } \\ { 5 7 - 6 0 } \end{array} ,$ 22</td>
</tr>
<tr>
<td>marathon world record, 251</td>
<td>Train Problem,</td>
</tr>
<tr>
<td>snow amounts, 244</td>
<td>credible intervals, 63</td>
</tr>
<tr>
<td>Student's t-test, 175</td>
<td>power law prior, 61</td>
</tr>
<tr>
<td>summary statistics</td>
<td>sensitivity to the prior, 60</td>
</tr>
<tr>
<td>about, 184</td>
<td>transposing a matrix, 95</td>
</tr>
<tr>
<td>larger datasets, 184, 247</td>
<td>triangle-shaped prior, 49</td>
</tr>
<tr>
<td>likelihood of reading improvement, 184 sampling distribution of the mean, 185</td>
<td>True value summed, 3</td>
</tr>
<tr>
<td>update of reading improvement, 186</td>
<td>U</td>
</tr>
<tr>
<td>normal distribution assumption, 188</td>
<td>uniform prior</td>
</tr>
<tr>
<td>summing row of DataFrame, 95</td>
<td>Bayesian Bandit strategy, 135</td>
</tr>
<tr>
<td>sums as distributions</td>
<td>beta distribution, 262</td>
</tr>
<tr>
<td>probability of superiority, 105</td>
<td>Euro Problem, 47, 129</td>
</tr>
<tr>
<td>three dice, 75, 86</td>
<td>101 Bowls Problem contrasted, 52</td>
</tr>
<tr>
<td>two dice, 73-76 weighted sum of probabilities, 122</td>
<td>gluten sensitivity Inverse Problem, 79 reading ability improvement, 177</td>
</tr>
<tr>
<td>survival analysis</td>
<td>Train Problem, 58</td>
</tr>
<tr>
<td>about, 191</td>
<td rowspan="2">univariate normal distribution, 170 universe age, 53</td>
</tr>
<tr>
<td>incomplete data, 194-196</td>
</tr>
<tr>
<td>called censored, 195 using, 196-199</td>
<td>unstack function converting Series to Data- Frame, 214, 232</td>
</tr>
<tr>
<td>light bulb dead bulb prediction, 202</td>
<td rowspan="2">updates (see Bayesian updates) urn problem, 17</td>
</tr>
<tr>
<td>light bulb lifetime distribution, 199-202 Weibull distribution, 191-194</td>
</tr>
<tr>
<td>swamping the priors, 51</td>
<td>V</td>
</tr>
<tr>
<td>T</td>
<td>variances in covariance matrix, 170 visualizing (see plotting)</td>
</tr>
<tr>
<td>testers finding bugs in program (see Lincoln Index Problem)</td>
<td></td>
</tr>
<tr>
<td>testing hypotheses</td>
<td>W</td>
</tr>
<tr>
<td>Bayesian Bandit strategy, 140</td>
<td>weather data, 241</td>
</tr>
<tr>
<td>Bayesian versus statistical, 134</td>
<td>snow amounts, 241-250</td>
</tr>
<tr>
<td>decision analysis instead, 134</td>
<td>Weibull distribution, 191-194</td>
</tr>
<tr>
<td>Euro Problem</td>
<td>light bulb dead bulb prediction, 202</td>
</tr>
<tr>
<td>about, 129</td>
<td>weighted distributions, 94</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="319" -->
<!-- PageBreak -->


<table>
<tr>
<td>weighted sum of probabilities, 122</td>
<td>Poisson processes, 99</td>
</tr>
<tr>
<td>World Cup Problem</td>
<td>predicting rematch, 106</td>
</tr>
<tr>
<td>conjugate priors</td>
<td>probability of superiority, 105</td>
</tr>
<tr>
<td>gamma distribution for update, 258-261</td>
<td>time between goals, 108</td>
</tr>
<tr>
<td>Poisson processes solution review, 257</td>
<td>update, 103</td>
</tr>
<tr>
<td>MCMC via PyMC3, 270-276</td>
<td>World Happiness Report, 276</td>
</tr>
<tr>
<td>Poisson processes</td>
<td></td>
</tr>
<tr>
<td>goal-scoring rate, 101 number of goals given rate, 100, 103 poisson object in SciPy, 100</td>
<td>$Y$ yeast cells counted (see counting cells)</td>
</tr>
</table>


<!-- PageFooter="Index" -->
<!-- PageNumber="320" -->
<!-- PageBreak -->


# About the Author

Allen B. Downey is a Professor of Computer Science at Olin College of Engineering.
He has taught computer science at Wellesley College, Colby College and UC Berkeley.
He has a PhD in Computer Science from UC Berkeley and master's and bachelor's
degrees from MIT. He is the author of Think Python, Think Stats, Think DSP, and a
blog, Probably Overthinking It.


## Colophon

The animal on the cover of Think Bayes is a red striped mullet (Mullus surmuletus).
This species of goatfish can be found in the Mediterranean Sea, east North Atlantic
Ocean, and the Black Sea. Known for its distinct striped first dorsal fin, the red stri-
ped mullet is a favored delicacy in the Mediterranean-along with a related goatfish,
Mullus barbatus, which has a first dorsal fin that is not striped. However, the red stri-
ped mullet tends to be more prized and is said to taste similar to oysters.

There are stories of ancient Romans rearing the red striped mullet in ponds-attend-
ing to, caressing, and even teaching them to feed at the sound of a bell. These fish,
generally weighing in under two pounds even when farm-raised, were sometimes
sold for their weight in silver.

When left to the wild, red mullets are small bottom-feeding fish with a distinct dou-
ble beard-known as barbels-on their lower lip, which they use to probe the ocean
floor for food. Because the red striped mullet feeds on sandy and rocky bottoms at
shallower depths, its barbels are less sensitive than its deep water relative, the Mullus
barbatus.

Many of the animals on O'Reilly covers are endangered; all of them are important to
the world.

The cover illustration is by Karen Montgomery, based on a black and white engraving
from Meyers Kleines Lexicon. The cover fonts are Gilroy Semibold and Guardian
Sans. The text font is Adobe Minion Pro; the heading font is Adobe Myriad Con-
densed; and the code font is Dalton Maag's Ubuntu Mono.

<!-- PageBreak -->

O'REILLY
®


# There's much more where this came from.

Experience books, videos, live online
training courses, and more from O'Reilly
and our 200+ partners-all in one place.

Learn more at oreilly.com/online-learning
<!-- PageFooter="@2019 O'Reilly Media, Inc. O'Reilly is a registered trademark of O'Reilly Media, Inc. | 175" -->
