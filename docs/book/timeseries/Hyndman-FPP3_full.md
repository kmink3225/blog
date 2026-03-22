# Forecasting: Principles and Practice (3rd ed.)
**Rob J Hyndman and George Athanasopoulos**

---



---

# Forecasting: Principles and Practice (3rd ed)

_Rob J Hyndman and George Athanasopoulos_

Monash University, Australia  


# Preface[](index.html#preface)

[ Buy a print version ](buy-a-print-version.html)

Welcome to our online textbook on forecasting.

This textbook is intended to provide a comprehensive introduction to forecasting methods and to present enough information about each method for readers to be able to use them sensibly. We don’t attempt to give a thorough discussion of the theoretical details behind each method, although the references at the end of each chapter will fill in many of those details.

The book is written for three audiences: (1) people finding themselves doing forecasting in business when they may not have had any formal training in the area; (2) undergraduate students studying business; (3) MBA students doing a forecasting elective. We use it ourselves for masters students and third-year undergraduate students at Monash University, Australia.

For most sections, we only assume that readers are familiar with introductory statistics, and with high-school algebra. There are a couple of sections that also require knowledge of matrices, but these are flagged.

At the end of each chapter we provide a list of “further reading”. In general, these lists comprise suggested textbooks that provide a more advanced or detailed treatment of the subject. Where there is no suitable textbook, we suggest journal articles that provide more information.

We use R throughout the book and we intend students to learn how to forecast with R. R is free and available on almost every operating system. It is a wonderful tool for all statistical analysis, not just for forecasting. See the [Using R appendix](appendix-using-r.html#appendix-using-r) for instructions on installing and using R.

All R examples in the book assume you have loaded the `fpp3` package first:
    
    
    [](index.html#cb1-1)library(fpp3)
    
    
    #> ── Attaching packages ──────────────────────────────── fpp3 1.0.3 ──
    #> ✔ tibble      3.3.1     ✔ tsibble     1.2.0
    #> ✔ dplyr       1.2.0     ✔ tsibbledata 0.4.1
    #> ✔ tidyr       1.3.2     ✔ ggtime      0.2.0
    #> ✔ lubridate   1.9.5     ✔ feasts      0.5.0
    #> ✔ ggplot2     4.0.2     ✔ fable       0.5.0
    #> ── Conflicts ───────────────────────────────────── fpp3_conflicts ──
    #> ✖ lubridate::date()    masks base::date()
    #> ✖ dplyr::filter()      masks stats::filter()
    #> ✖ tsibble::intersect() masks base::intersect()
    #> ✖ tsibble::interval()  masks lubridate::interval()
    #> ✖ dplyr::lag()         masks stats::lag()
    #> ✖ tsibble::setdiff()   masks base::setdiff()
    #> ✖ tsibble::union()     masks base::union()

This will load the relevant data sets, and attach several packages as listed above. These include several [`tidyverse`](https://tidyverse.org) packages, and packages to handle time series and forecasting in a “tidy” framework.

The above output also shows the package versions we have used in compiling this edition of the book. Some examples in the book will not work with earlier versions of the packages.

Finally, the output lists some conflicts showing which function will be preferenced when a function of the same name is in multiple packages.

The book is different from other forecasting textbooks in several ways.

  * It is free and online, making it accessible to a wide audience.
  * It uses R, which is free, open-source, and extremely powerful software.
  * The online version is continuously updated. You don’t have to wait until the next edition for errors to be removed or new methods to be discussed. We will update the book frequently.
  * There are dozens of real data examples taken from our own consulting practice. We have worked with hundreds of businesses and organisations helping them with forecasting issues, and this experience has contributed directly to many of the examples given here, as well as guiding our general philosophy of forecasting.
  * We emphasise graphical methods more than most forecasters. We use graphs to explore the data, analyse the validity of the models fitted and present the forecasting results.


### Changes in the third edition[](index.html#changes-in-the-third-edition)

The most important change in edition 3 of the book is that we use the `tsibble` and `fable` packages rather than the `forecast` package. This allows us to integrate closely with the `tidyverse` collection of packages. As a consequence, we have replaced many examples to take advantage of the new facilities.

We have also added some new material on time series features, and reorganised the content so Chapters [2](graphics.html#graphics)–[4](features.html#features) discuss exploratory analysis of time series, before we introduce any forecasting methods. This is because we should first have a good understanding of our time series, their patterns and characteristics, before we attempt to build any models and produce any forecasts.

In the online version of the book, we have included some videos at the start of most sections. These are intended to complement the written material in each section. You can view the [entire playlist on YouTube](https://www.youtube.com/playlist?list=PLyCNZ_xXGzpm7W9jLqbIyBAiSO5jDwJeE).

Helpful readers of the earlier versions of the book let us know of any typos or errors they had found. These were updated immediately online. No doubt we have introduced some new mistakes, and we will correct them online as soon as they are spotted. Please continue to [let us know](https://github.com/orgs/OTexts/discussions/categories/error-report?discussions_q=) about such things.

If you have questions about using the R packages discussed in this book, or about forecasting in general, please ask on the [OTexts discussion forum](https://github.com/orgs/OTexts/discussions?discussions_q=).

Happy forecasting!

Rob J Hyndman and George Athanasopoulos

May 2021

* * *

To cite the online version of this book, please use the following:

> Hyndman, R.J., & Athanasopoulos, G. (2021) _Forecasting: principles and practice_ , 3rd edition, OTexts: Melbourne, Australia. OTexts.com/fpp3. Accessed on `<current date>`.

> This online version of the book was last updated on 22 March 2026.
> The print version of the book ([available from Amazon](buy-a-print-version.html)) was last updated on 31 May 2021.


---

# Chapter 1 Getting started[](intro.html#intro)

Forecasting has fascinated people for thousands of years, sometimes being considered a sign of divine inspiration, and sometimes being seen as a criminal activity. The Jewish prophet Isaiah wrote in about 700 BC

> _Tell us what the future holds, so we may know that you are gods._  
>  (Isaiah 41:23)

One hundred years later, in ancient Babylon, forecasters would foretell the future based on the appearance of a sheep’s liver. Around the same time, people wanting forecasts would journey to Delphi in Greece to consult the Oracle, who would provide her predictions while intoxicated by ethylene vapours. Forecasters had a tougher time under the emperor Constantius II, who issued a decree in AD357 forbidding anyone “to consult a soothsayer, a mathematician, or a forecaster … May curiosity to foretell the future be silenced forever.”[1](intro.html#fn1) A similar ban on forecasting occurred in England in 1824[2](intro.html#fn2) when “every person pretending or professing to tell fortunes” was “deemed a rogue and vagabond”. The punishment was up to three months’ imprisonment with hard labour!

The varying fortunes of forecasters arise because good forecasts can seem almost magical, while bad forecasts may be dangerous. Consider the following famous predictions about computing.

  * _I think there is a world market for maybe five computers._ (Chairman of IBM, 1943)
  * _Computers in the future may weigh no more than 1.5 tons._ (Popular Mechanics, 1949)
  * _There is no reason anyone would want a computer in their home._ (President, DEC, 1977)


The last of these was made only three years before IBM produced the first personal computer. Not surprisingly, you can no longer buy a DEC computer. Forecasting is obviously a difficult activity, and businesses that do it well have a big advantage over those whose forecasts fail.

In this book, we will explore the most reliable methods for producing forecasts. The emphasis will be on methods that are replicable and testable, and have been shown to work.

* * *

  1. [Codex Theodosianus 9.16.4](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/CTh09.html)[↩︎](intro.html#fnref1)

  2. [Vagrancy Act, 1824, Section 4](https://statutes.org.uk/site/the-statutes/nineteenth-century/5-geo-iv-c-83-vagrancy-act-1824/), [repealed in 1989](https://www.legislation.gov.uk/ukpga/Geo4/5/83#commentary-c554743).[↩︎](intro.html#fnref2)




---

## 1.1 What can be forecast?[](what-can-be-forecast.html#what-can-be-forecast)

Forecasting is required in many situations: deciding whether to build another power generation plant in the next five years requires forecasts of future demand; scheduling staff in a call centre next week requires forecasts of call volumes; stocking an inventory requires forecasts of stock requirements. Forecasts can be required several years in advance (for the case of capital investments), or only a few minutes beforehand (for telecommunication routing). Whatever the circumstances or time horizons involved, forecasting is an important aid to effective and efficient planning.

Some things are easier to forecast than others. The time of the sunrise tomorrow morning can be forecast precisely. On the other hand, tomorrow’s lotto numbers cannot be forecast with any accuracy. The predictability of an event or a quantity depends on several factors including:

  1. how well we understand the factors that contribute to it;
  2. how much data is available;
  3. how similar the future is to the past;
  4. whether the forecasts can affect the thing we are trying to forecast.


For example, short-term forecasts of residential electricity demand can be highly accurate because all four conditions are usually satisfied.

  1. We have a good idea of the contributing factors: electricity demand is driven largely by temperatures, with smaller effects for calendar variation such as holidays, and economic conditions.
  2. Several years of data on electricity demand are usually available, and many decades of data on weather conditions.
  3. For short-term forecasting (up to a few weeks), it is safe to assume that demand behaviour will be similar to what has been seen in the past.
  4. For most residential users, the price of electricity is not dependent on demand, and so the demand forecasts have little or no effect on consumer behaviour.


Provided we have the skills to develop a good model linking electricity demand and the key driver variables, the forecasts can be remarkably accurate.

On the other hand, when forecasting currency exchange rates, only one of the conditions is satisfied: there is plenty of available data. However, we have a limited understanding of the factors that affect exchange rates, the future may well be different to the past if there is a financial or political crisis in one of the countries, and forecasts of the exchange rate have a direct effect on the rates themselves. If there are well-publicised forecasts that the exchange rate will increase, then people will immediately adjust the price they are willing to pay and so the forecasts are self-fulfilling. In a sense, the exchange rates become their own forecasts. This is an example of the “efficient market hypothesis”. Consequently, forecasting whether the exchange rate will rise or fall tomorrow is about as predictable as forecasting whether a tossed coin will come down as a head or a tail. In both situations, you will be correct about 50% of the time, whatever you forecast. In situations like this, forecasters need to be aware of their own limitations, and not claim more than is possible.

Often in forecasting, a key step is knowing when something can be forecast accurately, and when forecasts will be no better than tossing a coin. Good forecasts capture the genuine patterns and relationships which exist in the historical data, but do not replicate past events that will not occur again. In this book, we will learn how to tell the difference between a random fluctuation in the past data that should be ignored, and a genuine pattern that should be modelled and extrapolated.

Many people wrongly assume that forecasts are not possible in a changing environment. Every environment is changing, and a good forecasting model captures the way in which things are changing. Forecasts rarely assume that the environment is unchanging. What is normally assumed is that _the way in which the environment is changing_ will continue into the future. That is, a highly volatile environment will continue to be highly volatile; a business with fluctuating sales will continue to have fluctuating sales; and an economy that has gone through booms and busts will continue to go through booms and busts. A forecasting model is intended to capture the way things move, not just where things are. As Abraham Lincoln said, “If we could first know where we are and whither we are tending, we could better judge what to do and how to do it”.

Forecasting situations vary widely in their time horizons, factors determining actual outcomes, types of data patterns, and many other aspects. Forecasting methods can be simple, such as using the most recent observation as a forecast (which is called the **naïve method**), or highly complex, such as neural nets and econometric systems of simultaneous equations. Sometimes, there will be no data available at all. For example, we may wish to forecast the sales of a new product in its first year, but there are obviously no data to work with. In situations like this, we use judgmental forecasting, discussed in Chapter [6](judgmental.html#judgmental). The choice of method depends on what data are available and the predictability of the quantity to be forecast.


---

## 1.2 Forecasting, goals and planning[](planning.html#planning)

Forecasting is a common statistical task in business, where it helps to inform decisions about the scheduling of production, transportation and personnel, and provides a guide to long-term strategic planning. However, business forecasting is often done poorly, and is frequently confused with planning and goals. They are three different things.

Forecasting
     is about predicting the future as accurately as possible, given all of the information available, including historical data and knowledge of any future events that might impact the forecasts. 
Goals
     are what you would like to have happen. Goals should be linked to forecasts and plans, but this does not always occur. Too often, goals are set without any plan for how to achieve them, and no forecasts for whether they are realistic. 
Planning
     is a response to forecasts and goals. Planning involves determining the appropriate actions that are required to make your forecasts match your goals. 

Forecasting should be an integral part of the decision-making activities of management, as it can play an important role in many areas of a company. Modern organisations require short-term, medium-term and long-term forecasts, depending on the specific application.

Short-term forecasts
     are needed for the scheduling of personnel, production and transportation. As part of the scheduling process, forecasts of demand are often also required. 
Medium-term forecasts
     are needed to determine future resource requirements, in order to purchase raw materials, hire personnel, or buy machinery and equipment. 
Long-term forecasts
     are used in strategic planning. Such decisions must take account of market opportunities, environmental factors and internal resources. 

An organisation needs to develop a forecasting system that involves several approaches to predicting uncertain events. Such forecasting systems require the development of expertise in identifying forecasting problems, applying a range of forecasting methods, selecting appropriate methods for each problem, and evaluating and refining forecasting methods over time. It is also important to have strong organisational support for the use of formal forecasting methods if they are to be used successfully.


---

## 1.3 Determining what to forecast[](determining-what-to-forecast.html#determining-what-to-forecast)

In the early stages of a forecasting project, decisions need to be made about what should be forecast. For example, if forecasts are required for items in a manufacturing environment, it is necessary to ask whether forecasts are needed for:

  1. every product line, or for groups of products?
  2. every sales outlet, or for outlets grouped by region, or only for total sales?
  3. weekly data, monthly data or annual data?


It is also necessary to consider the forecasting horizon. Will forecasts be required for one month in advance, for 6 months, or for ten years? Different types of models will be necessary, depending on what forecast horizon is most important.

How frequently are forecasts required? Forecasts that need to be produced frequently are better done using an automated system than with methods that require careful manual work.

It is worth spending time talking to the people who will use the forecasts to ensure that you understand their needs, and how the forecasts are to be used, before embarking on extensive work in producing the forecasts.

Once it has been determined what forecasts are required, it is then necessary to find or collect the data on which the forecasts will be based. The data required for forecasting may already exist. These days, a lot of data are recorded, and the forecaster’s task is often to identify where and how the required data are stored. The data may include sales records of a company, the historical demand for a product, or the unemployment rate for a geographic region. A large part of a forecaster’s time can be spent in locating and collating the available data prior to developing suitable forecasting methods.


---

## 1.4 Forecasting data and methods[](data-methods.html#data-methods)

The appropriate forecasting methods depend largely on what data are available.

If there are no data available, or if the data available are not relevant to the forecasts, then **qualitative forecasting** methods must be used. These methods are not purely guesswork—there are well-developed structured approaches to obtaining good forecasts without using historical data. These methods are discussed in Chapter [6](judgmental.html#judgmental).

**Quantitative forecasting** can be applied when two conditions are satisfied:

  1. numerical information about the past is available;
  2. it is reasonable to assume that some aspects of the past patterns will continue into the future.


There is a wide range of quantitative forecasting methods, often developed within specific disciplines for specific purposes. Each method has its own properties, accuracies, and costs that must be considered when choosing a specific method.

Most quantitative prediction problems use either time series data (collected at regular intervals over time) or cross-sectional data (collected at a single point in time). In this book we are concerned with forecasting future data, and we concentrate on the time series domain.

### Time series forecasting[](data-methods.html#time-series-forecasting)

Examples of time series data include:

  * Annual Google profits
  * Quarterly sales results for Amazon
  * Monthly rainfall
  * Weekly retail sales
  * Daily IBM stock prices
  * Hourly electricity demand
  * 5-minute freeway traffic counts
  * Time-stamped stock transaction data


Anything that is observed sequentially over time is a time series. In this book, we will only consider time series that are observed at regular intervals of time (e.g., hourly, daily, weekly, monthly, quarterly, annually). Irregularly spaced time series can also occur, but are beyond the scope of this book.

When forecasting time series data, the aim is to estimate how the sequence of observations will continue into the future. Figure [1.1](data-methods.html#fig:beer) shows the quarterly Australian beer production from 2000 to the second quarter of 2010.

Figure 1.1: Australian quarterly beer production: 2000Q1–2010Q2, with two years of forecasts. 

The blue lines show forecasts for the next two years. Notice how the forecasts have captured the seasonal pattern seen in the historical data and replicated it for the next two years. The dark shaded region shows 80% prediction intervals. That is, each future value is expected to lie in the dark shaded region with a probability of 80%. The light shaded region shows 95% prediction intervals. These prediction intervals are a useful way of displaying the uncertainty in forecasts. In this case the forecasts are expected to be accurate, and hence the prediction intervals are quite narrow.

The simplest time series forecasting methods use only information on the variable to be forecast, and make no attempt to discover the factors that affect its behaviour. Therefore they will extrapolate trend and seasonal patterns, but they ignore all other information such as marketing initiatives, competitor activity, changes in economic conditions, and so on.

Decomposition methods are helpful for studying the trend and seasonal patterns in a time series; these are discussed in Chapter [3](decomposition.html#decomposition). Popular time series models used for forecasting include exponential smoothing models and ARIMA models, discussed in Chapters [8](expsmooth.html#expsmooth) and [9](arima.html#arima) respectively.

### Predictor variables and time series forecasting[](data-methods.html#predictor-variables-and-time-series-forecasting)

Predictor variables are often useful in time series forecasting. For example, suppose we wish to forecast the hourly electricity demand (ED) of a hot region during the summer period. A model with predictor variables might be of the form \\[\begin{align*} \text{ED} = & f(\text{current temperature, strength of economy, population,}\\\ & \qquad\text{time of day, day of week, error}). \end{align*}\\] The relationship is not exact — there will always be changes in electricity demand that cannot be accounted for by the predictor variables. The “error” term on the right allows for random variation and the effects of relevant variables that are not included in the model. We call this an **explanatory model** because it helps explain what causes the variation in electricity demand.

Because the electricity demand data form a time series, we could also use a **time series model** for forecasting. In this case, a suitable time series forecasting equation is of the form \\[ \text{ED}_{t+1} = f(\text{ED}_{t}, \text{ED}_{t-1}, \text{ED}_{t-2}, \text{ED}_{t-3},\dots, \text{error}), \\] where \\(t\\) is the present hour, \\(t+1\\) is the next hour, \\(t-1\\) is the previous hour, \\(t-2\\) is two hours ago, and so on. Here, prediction of the future is based on past values of a variable, but not on external variables that may affect the system. Again, the “error” term on the right allows for random variation and the effects of relevant variables that are not included in the model.

There is also a third type of model which combines the features of the above two models. For example, it might be given by \\[ \text{ED}_{t+1} = f(\text{ED}_{t}, \text{current temperature, time of day, day of week, error}). \\] These types of **mixed models** have been given various names in different disciplines. They are known as dynamic regression models, panel data models, longitudinal models, transfer function models, and linear system models (assuming that \\(f\\) is linear). These models are discussed in Chapter [10](dynamic.html#dynamic).

An explanatory model is useful because it incorporates information about other variables, rather than only historical values of the variable to be forecast. However, there are several reasons a forecaster might select a time series model rather than an explanatory or mixed model. First, the system may not be understood, and even if it was understood it may be extremely difficult to measure the relationships that are assumed to govern its behaviour. Second, it is necessary to know or forecast the future values of the various predictors in order to be able to forecast the variable of interest, and this may be too difficult. Third, the main concern may be only to predict what will happen, not to know why it happens. Finally, the time series model may give more accurate forecasts than an explanatory or mixed model.

The model to be used in forecasting depends on the resources and data available, the accuracy of the competing models, and the way in which the forecasting model is to be used.


---

## 1.5 Some case studies[](case-studies.html#case-studies)

The following four cases are from our consulting practice and demonstrate different types of forecasting situations and the associated challenges that often arise.

#### Case 1[](case-studies.html#case-1)

The client was a large company manufacturing disposable tableware such as napkins and paper plates. They needed forecasts of each of hundreds of items every month. The time series data showed a range of patterns, some with trends, some seasonal, and some with neither. At the time, they were using their own software, written in-house, but it often produced forecasts that did not seem sensible. The methods that were being used were the following:

  1. average of the last 12 months data;
  2. average of the last 6 months data;
  3. prediction from a straight line regression over the last 12 months;
  4. prediction from a straight line regression over the last 6 months;
  5. prediction obtained by a straight line through the last observation with slope equal to the average slope of the lines connecting last year’s and this year’s values;
  6. prediction obtained by a straight line through the last observation with slope equal to the average slope of the lines connecting last year’s and this year’s values, where the average is taken only over the last 6 months.


They required us to tell them what was going wrong and to modify the software to provide more accurate forecasts. The software was written in COBOL, making it difficult to do any sophisticated numerical computation.

#### Case 2[](case-studies.html#case-2)

In this case, the client was the Australian federal government, which needed to forecast the annual budget for the Pharmaceutical Benefit Scheme (PBS). The PBS provides a subsidy for many pharmaceutical products sold in Australia, and the expenditure depends on what people purchase during the year. The total expenditure was around A$7 billion in 2009, and had been underestimated by nearly $1 billion in each of the two years before we were asked to assist in developing a more accurate forecasting approach.

In order to forecast the total expenditure, it is necessary to forecast the sales volumes of hundreds of groups of pharmaceutical products using monthly data. Almost all of the groups have trends and seasonal patterns. The sales volumes for many groups have sudden jumps up or down due to changes in what drugs are subsidised. The expenditures for many groups also have sudden changes due to cheaper competitor drugs becoming available.

Thus we needed to find a forecasting method that allowed for trend and seasonality if they were present, and at the same time was robust to sudden changes in the underlying patterns. It also needed to be able to be applied automatically to a large number of time series.

#### Case 3[](case-studies.html#case-3)

A large car fleet company asked us to help them forecast vehicle resale values. They purchase new vehicles, lease them out for three years, and then sell them. Better forecasts of vehicle sales values would mean better control of profits; understanding what affects resale values may allow leasing and sales policies to be developed in order to maximise profits.

At the time, the resale values were being forecast by a group of specialists. Unfortunately, they saw any statistical model as a threat to their jobs, and were uncooperative in providing information. Nevertheless, the company provided a large amount of data on previous vehicles and their eventual resale values.

#### Case 4[](case-studies.html#case-4)

In this project, we needed to develop a model for forecasting weekly air passenger traffic on major domestic routes for one of Australia’s leading airlines. The company required forecasts of passenger numbers for each major domestic route and for each class of passenger (economy class, business class and first class). The company provided weekly traffic data from the previous six years.

Air passenger numbers are affected by school holidays, major sporting events, advertising campaigns, competition behaviour, etc. School holidays often do not coincide in different Australian cities, and sporting events sometimes move from one city to another. During the period of the historical data, there was a major pilots’ strike during which there was no traffic for several months. A new cut-price airline also launched and folded. Towards the end of the historical data, the airline had trialled a redistribution of some economy class seats to business class, and some business class seats to first class. After several months, however, the seat classifications reverted to the original distribution.


---

## 1.6 The basic steps in a forecasting task[](basic-steps.html#basic-steps)

A forecasting task usually involves five basic steps.

Step 1: Problem definition.
     Often this is the most difficult part of forecasting. Defining the problem carefully requires an understanding of the way the forecasts will be used, who requires the forecasts, and how the forecasting function fits within the organisation requiring the forecasts. A forecaster needs to spend time talking to everyone who will be involved in collecting data, maintaining databases, and using the forecasts for future planning. 
Step 2: Gathering information.
     There are always at least two kinds of information required: (a) statistical data, and (b) the accumulated expertise of the people who collect the data and use the forecasts. Often, it will be difficult to obtain enough historical data to be able to fit a good statistical model. In that case, the judgmental forecasting methods of Chapter [6](judgmental.html#judgmental) can be used. Occasionally, old data will be less useful due to structural changes in the system being forecast; then we may choose to use only the most recent data. However, remember that good statistical models will handle evolutionary changes in the system; don’t throw away good data unnecessarily. 
Step 3: Preliminary (exploratory) analysis.
     Always start by graphing the data. Are there consistent patterns? Is there a significant trend? Is seasonality important? Is there evidence of the presence of business cycles? Are there any outliers in the data that need to be explained by those with expert knowledge? How strong are the relationships among the variables available for analysis? Various tools have been developed to help with this analysis. These are discussed in Chapters [2](graphics.html#graphics) and [3](decomposition.html#decomposition). 
Step 4: Choosing and fitting models.
     The best model to use depends on the availability of historical data, the strength of relationships between the forecast variable and any explanatory variables, and the way in which the forecasts are to be used. It is common to compare two or three potential models. Each model is itself an artificial construct that is based on a set of assumptions (explicit and implicit) and usually involves one or more parameters which must be estimated using the known historical data. We will discuss regression models (Chapter [7](regression.html#regression)), exponential smoothing methods (Chapter [8](expsmooth.html#expsmooth)), Box-Jenkins ARIMA models (Chapter [9](arima.html#arima)), Dynamic regression models (Chapter [10](dynamic.html#dynamic)), Hierarchical forecasting (Chapter [11](hierarchical.html#hierarchical)), and several advanced methods including neural networks and vector autoregression (Chapter [12](advanced.html#advanced)). 
Step 5: Using and evaluating a forecasting model.
     Once a model has been selected and its parameters estimated, the model is used to make forecasts. The performance of the model can only be properly evaluated after the data for the forecast period have become available. A number of methods have been developed to help in assessing the accuracy of forecasts. There are also organisational issues in using and acting on the forecasts. A brief discussion of some of these issues is given in Chapter [5](toolbox.html#toolbox). When using a forecasting model in practice, numerous practical issues arise such as how to handle missing values and outliers, or how to deal with short time series. These are discussed in Chapter [13](practical.html#practical). 


---

## 1.7 The statistical forecasting perspective[](perspective.html#perspective)

The thing we are trying to forecast is unknown (or we would not be forecasting it), and so we can think of it as a _random variable_. For example, the total sales for next month could take a range of possible values, and until we add up the actual sales at the end of the month, we don’t know what the value will be. So until we know the sales for next month, it is a random quantity.

Because next month is relatively close, we usually have a good idea what the likely sales values could be. On the other hand, if we are forecasting the sales for the same month next year, the possible values it could take are much more variable. In most forecasting situations, the variation associated with the thing we are forecasting will shrink as the event approaches. In other words, the further ahead we forecast, the more uncertain we are.

We can imagine many possible futures, each yielding a different value for the thing we wish to forecast. Plotted in black in Figure [1.2](perspective.html#fig:austa1) are the total international arrivals to Australia from 1980 to 2015. Also shown are ten possible futures from 2016–2025.

Figure 1.2: Total international visitors to Australia (1980-2015) along with ten possible futures. 

When we obtain a forecast, we are estimating the _middle_ of the range of possible values the random variable could take. Often, a forecast is accompanied by a **prediction interval** giving a _range_ of values the random variable could take with relatively high probability. For example, a 95% prediction interval contains a range of values which should include the actual future value with probability 95%.

Rather than plotting individual possible futures as shown in Figure [1.2](perspective.html#fig:austa1), we usually show these prediction intervals instead. Figure [1.3](perspective.html#fig:austa2) shows 80% and 95% intervals for the future Australian international visitors. The blue line is the average of the possible future values, which we call the **point forecasts**.

Figure 1.3: Total international visitors to Australia (1980–2015) along with 10-year forecasts and 80% and 95% prediction intervals. 

We will use the subscript \\(t\\) for time. For example, \\(y_t\\) will denote the observation at time \\(t\\). Suppose we denote all the information we have observed as \\(\mathcal{I}\\) and we want to forecast \\(y_t\\). We then write \\(y_{t} | \mathcal{I}\\) meaning “the random variable \\(y_{t}\\) given what we know in \\(\mathcal{I}\\)”. The set of values that this random variable could take, along with their relative probabilities, is known as the “probability distribution” of \\(y_{t} |\mathcal{I}\\). In forecasting, we call this the **forecast distribution**.

When we talk about the “forecast”, we usually mean the average value of the forecast distribution, and we put a “hat” over \\(y\\) to show this. Thus, we write the forecast of \\(y_t\\) as \\(\hat{y}_t\\), meaning the average of the possible values that \\(y_t\\) could take given everything we know.

It is often useful to specify exactly what information we have used in calculating the forecast. Then we will write, for example, \\(\hat{y}_{t|t-1}\\) to mean the forecast of \\(y_t\\) taking account of all previous observations \\((y_1,\dots,y_{t-1})\\). Similarly, \\(\hat{y}_{T+h|T}\\) means the forecast of \\(y_{T+h}\\) taking account of \\(y_1,\dots,y_T\\) (i.e., an \\(h\\)-step forecast taking account of all observations up to time \\(T\\)).


---

## 1.8 Exercises[](intro-exercises.html#intro-exercises)

  1. For cases 3 and 4 in Section [1.5](case-studies.html#case-studies), list the possible predictor variables that might be useful, assuming that the relevant data are available.

  2. For case 3 in Section [1.5](case-studies.html#case-studies), describe the five steps of forecasting in the context of this project.




---

## 1.9 Further reading[](intro-reading.html#intro-reading)

  * Armstrong ([2001](intro-reading.html#ref-Armstrong01)) covers the whole field of forecasting, with each chapter written by different experts. It is highly opinionated at times (and we don’t agree with everything in it), but it is full of excellent general advice on tackling forecasting problems.
  * Ord et al. ([2017](intro-reading.html#ref-Ord2017)) is a forecasting textbook covering some of the same areas as this book, but with a different emphasis and not focused around any particular software environment. It is written by three highly respected forecasters, with many decades of experience between them.


### Bibliography[](bibliography.html#bibliography)

Armstrong, J. S. (Ed.). (2001). _Principles of forecasting: A handbook for researchers and practitioners_. Kluwer Academic Publishers. [__](http://amazon.com/dp/0792379306?tag=otexts20)

Ord, J. K., Fildes, R., & Kourentzes, N. (2017). _Principles of business forecasting_ (2nd ed.). Wessex Press Publishing Co. [__](http://amazon.com/dp/0999064916?tag=otexts20)


---

# Chapter 2 Time series graphics[](graphics.html#graphics)

The first thing to do in any data analysis task is to plot the data. Graphs enable many features of the data to be visualised, including patterns, unusual observations, changes over time, and relationships between variables. The features that are seen in plots of the data must then be incorporated, as much as possible, into the forecasting methods to be used. Just as the type of data determines what forecasting method to use, it also determines what graphs are appropriate. But before we produce graphs, we need to set up our time series in R.


---

## 2.1 `tsibble` objects[](tsibbles.html#tsibbles)

A time series can be thought of as a list of numbers (the observations), along with some information about what times those numbers were recorded (the index). This information can be stored as a `tsibble` object in R.

### The index variable[](tsibbles.html#the-index-variable)

Suppose you have annual observations for the last few years:

Year | Observation  
---|---  
2015 | 123  
2016 | 39  
2017 | 78  
2018 | 52  
2019 | 110  
  
We turn this into a `tsibble` object using the `tsibble()` function:
    
    
    [](tsibbles.html#cb3-1)y <- tsibble(
    [](tsibbles.html#cb3-2)  Year = 2015:2019,
    [](tsibbles.html#cb3-3)  Observation = c(123, 39, 78, 52, 110),
    [](tsibbles.html#cb3-4)  index = Year
    [](tsibbles.html#cb3-5))

`tsibble` objects extend tidy data frames (`tibble` objects) by introducing temporal structure. We have set the time series `index` to be the `Year` column, which associates the measurements (`Observation`) with the time of recording (`Year`).

For observations that are more frequent than once per year, we need to use a time class function on the index. For example, suppose we have a monthly dataset `z`: 
    
    
    [](tsibbles.html#cb4-1)z
    [](tsibbles.html#cb4-2)#> # A tibble: 5 × 2
    [](tsibbles.html#cb4-3)#>   Month    Observation
    [](tsibbles.html#cb4-4)#>   <chr>          <dbl>
    [](tsibbles.html#cb4-5)#> 1 2019 Jan          50
    [](tsibbles.html#cb4-6)#> 2 2019 Feb          23
    [](tsibbles.html#cb4-7)#> 3 2019 Mar          34
    [](tsibbles.html#cb4-8)#> 4 2019 Apr          30
    [](tsibbles.html#cb4-9)#> 5 2019 May          25

This can be converted to a `tsibble` object using the following code:
    
    
    [](tsibbles.html#cb5-1)z |>
    [](tsibbles.html#cb5-2)  mutate(Month = yearmonth(Month)) |>
    [](tsibbles.html#cb5-3)  as_tsibble(index = Month)
    [](tsibbles.html#cb5-4)#> # A tsibble: 5 x 2 [1M]
    [](tsibbles.html#cb5-5)#>      Month Observation
    [](tsibbles.html#cb5-6)#>      <mth>       <dbl>
    [](tsibbles.html#cb5-7)#> 1 2019 Jan          50
    [](tsibbles.html#cb5-8)#> 2 2019 Feb          23
    [](tsibbles.html#cb5-9)#> 3 2019 Mar          34
    [](tsibbles.html#cb5-10)#> 4 2019 Apr          30
    [](tsibbles.html#cb5-11)#> 5 2019 May          25

First, the `Month` column is being converted from text to a monthly time object with `yearmonth()`. We then convert the data frame to a `tsibble` by identifying the `index` variable using `as_tsibble()`. Note the addition of “[1M]” on the first line indicating this is monthly data.

Other time class functions can be used depending on the frequency of the observations.

Frequency | Function  
---|---  
Annual | `start:end`  
Quarterly | `yearquarter()`  
Monthly | `yearmonth()`  
Weekly | `yearweek()`  
Daily | `as_date()`, `ymd()`  
Sub-daily | `as_datetime()`, `ymd_hms()`  
  
### The key variables[](tsibbles.html#the-key-variables)

A `tsibble` also allows multiple time series to be stored in a single object. Suppose you are interested in a dataset containing the fastest running times for women’s and men’s track races at the Olympics, from 100m to 10000m:
    
    
    [](tsibbles.html#cb6-1)olympic_running
    [](tsibbles.html#cb6-2)#> # A tsibble: 312 x 4 [4Y]
    [](tsibbles.html#cb6-3)#> # Key:       Length, Sex [14]
    [](tsibbles.html#cb6-4)#>     Year Length Sex    Time
    [](tsibbles.html#cb6-5)#>    <int>  <int> <chr> <dbl>
    [](tsibbles.html#cb6-6)#>  1  1896    100 men    12  
    [](tsibbles.html#cb6-7)#>  2  1900    100 men    11  
    [](tsibbles.html#cb6-8)#>  3  1904    100 men    11  
    [](tsibbles.html#cb6-9)#>  4  1908    100 men    10.8
    [](tsibbles.html#cb6-10)#>  5  1912    100 men    10.8
    [](tsibbles.html#cb6-11)#>  6  1916    100 men    NA  
    [](tsibbles.html#cb6-12)#>  7  1920    100 men    10.8
    [](tsibbles.html#cb6-13)#>  8  1924    100 men    10.6
    [](tsibbles.html#cb6-14)#>  9  1928    100 men    10.8
    [](tsibbles.html#cb6-15)#> 10  1932    100 men    10.3
    [](tsibbles.html#cb6-16)#> # ℹ 302 more rows

The summary above shows that this is a `tsibble` object, which contains 312 rows and 4 columns. Alongside this, “[4Y]” informs us that the interval of these observations is every four years. Below this is the key structure, which informs us that there are 14 separate time series in the `tsibble`. A preview of the first 10 observations is also shown, in which we can see a missing value occurs in 1916. This is because the Olympics were not held during World War I.

The 14 time series in this object are uniquely identified by the keys: the `Length` and `Sex` variables. The `distinct()` function can be used to show the categories of each variable or even combinations of variables:
    
    
    [](tsibbles.html#cb7-1)olympic_running |> distinct(Sex)
    [](tsibbles.html#cb7-2)#> # A tibble: 2 × 1
    [](tsibbles.html#cb7-3)#>   Sex  
    [](tsibbles.html#cb7-4)#>   <chr>
    [](tsibbles.html#cb7-5)#> 1 men  
    [](tsibbles.html#cb7-6)#> 2 women

### Working with `tsibble` objects[](tsibbles.html#working-with-tsibble-objects)

We can use `dplyr` functions such as `mutate()`, `filter()`, `select()` and `summarise()` to work with `tsibble` objects. To illustrate these, we will use the `PBS` tsibble containing sales data on pharmaceutical products in Australia.
    
    
    [](tsibbles.html#cb8-1)PBS
    [](tsibbles.html#cb8-2)#> # A tsibble: 67,596 x 9 [1M]
    [](tsibbles.html#cb8-3)#> # Key:       Concession, Type, ATC1, ATC2 [336]
    [](tsibbles.html#cb8-4)#>       Month Concession   Type    ATC1  ATC1_desc ATC2  ATC2_desc Scripts  Cost
    [](tsibbles.html#cb8-5)#>       <mth> <chr>        <chr>   <chr> <chr>     <chr> <chr>       <dbl> <dbl>
    [](tsibbles.html#cb8-6)#>  1 1991 Jul Concessional Co-pay… A     Alimenta… A01   STOMATOL…   18228 67877
    [](tsibbles.html#cb8-7)#>  2 1991 Aug Concessional Co-pay… A     Alimenta… A01   STOMATOL…   15327 57011
    [](tsibbles.html#cb8-8)#>  3 1991 Sep Concessional Co-pay… A     Alimenta… A01   STOMATOL…   14775 55020
    [](tsibbles.html#cb8-9)#>  4 1991 Oct Concessional Co-pay… A     Alimenta… A01   STOMATOL…   15380 57222
    [](tsibbles.html#cb8-10)#>  5 1991 Nov Concessional Co-pay… A     Alimenta… A01   STOMATOL…   14371 52120
    [](tsibbles.html#cb8-11)#>  6 1991 Dec Concessional Co-pay… A     Alimenta… A01   STOMATOL…   15028 54299
    [](tsibbles.html#cb8-12)#>  7 1992 Jan Concessional Co-pay… A     Alimenta… A01   STOMATOL…   11040 39753
    [](tsibbles.html#cb8-13)#>  8 1992 Feb Concessional Co-pay… A     Alimenta… A01   STOMATOL…   15165 54405
    [](tsibbles.html#cb8-14)#>  9 1992 Mar Concessional Co-pay… A     Alimenta… A01   STOMATOL…   16898 61108
    [](tsibbles.html#cb8-15)#> 10 1992 Apr Concessional Co-pay… A     Alimenta… A01   STOMATOL…   18141 65356
    [](tsibbles.html#cb8-16)#> # ℹ 67,586 more rows

This contains monthly data on Medicare Australia prescription data from July 1991 to June 2008. These are classified according to various concession types, and Anatomical Therapeutic Chemical (ATC) indexes. For this example, we are interested in the `Cost` time series (total cost of scripts in Australian dollars).

We can use the `filter()` function to extract the A10 scripts:
    
    
    [](tsibbles.html#cb9-1)PBS |>
    [](tsibbles.html#cb9-2)  filter(ATC2 == "A10")
    [](tsibbles.html#cb9-3)#> # A tsibble: 816 x 9 [1M]
    [](tsibbles.html#cb9-4)#> # Key:       Concession, Type, ATC1, ATC2 [4]
    [](tsibbles.html#cb9-5)#>       Month Concession   Type   ATC1  ATC1_desc ATC2  ATC2_desc Scripts   Cost
    [](tsibbles.html#cb9-6)#>       <mth> <chr>        <chr>  <chr> <chr>     <chr> <chr>       <dbl>  <dbl>
    [](tsibbles.html#cb9-7)#>  1 1991 Jul Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   89733 2.09e6
    [](tsibbles.html#cb9-8)#>  2 1991 Aug Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   77101 1.80e6
    [](tsibbles.html#cb9-9)#>  3 1991 Sep Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   76255 1.78e6
    [](tsibbles.html#cb9-10)#>  4 1991 Oct Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   78681 1.85e6
    [](tsibbles.html#cb9-11)#>  5 1991 Nov Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   70554 1.69e6
    [](tsibbles.html#cb9-12)#>  6 1991 Dec Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   75814 1.84e6
    [](tsibbles.html#cb9-13)#>  7 1992 Jan Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   64186 1.56e6
    [](tsibbles.html#cb9-14)#>  8 1992 Feb Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   75899 1.73e6
    [](tsibbles.html#cb9-15)#>  9 1992 Mar Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   89445 2.05e6
    [](tsibbles.html#cb9-16)#> 10 1992 Apr Concessional Co-pa… A     Alimenta… A10   ANTIDIAB…   97315 2.23e6
    [](tsibbles.html#cb9-17)#> # ℹ 806 more rows

This allows rows of the tsibble to be selected. Next we can simplify the resulting object by selecting the columns we will need in subsequent analysis.
    
    
    [](tsibbles.html#cb10-1)PBS |>
    [](tsibbles.html#cb10-2)  filter(ATC2 == "A10") |>
    [](tsibbles.html#cb10-3)  select(Month, Concession, Type, Cost)
    [](tsibbles.html#cb10-4)#> # A tsibble: 816 x 4 [1M]
    [](tsibbles.html#cb10-5)#> # Key:       Concession, Type [4]
    [](tsibbles.html#cb10-6)#>       Month Concession   Type           Cost
    [](tsibbles.html#cb10-7)#>       <mth> <chr>        <chr>         <dbl>
    [](tsibbles.html#cb10-8)#>  1 1991 Jul Concessional Co-payments 2092878
    [](tsibbles.html#cb10-9)#>  2 1991 Aug Concessional Co-payments 1795733
    [](tsibbles.html#cb10-10)#>  3 1991 Sep Concessional Co-payments 1777231
    [](tsibbles.html#cb10-11)#>  4 1991 Oct Concessional Co-payments 1848507
    [](tsibbles.html#cb10-12)#>  5 1991 Nov Concessional Co-payments 1686458
    [](tsibbles.html#cb10-13)#>  6 1991 Dec Concessional Co-payments 1843079
    [](tsibbles.html#cb10-14)#>  7 1992 Jan Concessional Co-payments 1564702
    [](tsibbles.html#cb10-15)#>  8 1992 Feb Concessional Co-payments 1732508
    [](tsibbles.html#cb10-16)#>  9 1992 Mar Concessional Co-payments 2046102
    [](tsibbles.html#cb10-17)#> 10 1992 Apr Concessional Co-payments 2225977
    [](tsibbles.html#cb10-18)#> # ℹ 806 more rows

The `select()` function allows us to select particular columns, while `filter()` allows us to keep particular rows.

Note that the index variable `Month`, and the keys `Concession` and `Type`, would be returned even if they were not explicitly selected as they are required for a tsibble (to ensure each row contains a unique combination of keys and index).

Another useful function is `summarise()` which allows us to combine data across keys. For example, we may wish to compute total cost per month regardless of the `Concession` or `Type` keys.
    
    
    [](tsibbles.html#cb11-1)PBS |>
    [](tsibbles.html#cb11-2)  filter(ATC2 == "A10") |>
    [](tsibbles.html#cb11-3)  select(Month, Concession, Type, Cost) |>
    [](tsibbles.html#cb11-4)  summarise(TotalC = sum(Cost))
    [](tsibbles.html#cb11-5)#> # A tsibble: 204 x 2 [1M]
    [](tsibbles.html#cb11-6)#>       Month  TotalC
    [](tsibbles.html#cb11-7)#>       <mth>   <dbl>
    [](tsibbles.html#cb11-8)#>  1 1991 Jul 3526591
    [](tsibbles.html#cb11-9)#>  2 1991 Aug 3180891
    [](tsibbles.html#cb11-10)#>  3 1991 Sep 3252221
    [](tsibbles.html#cb11-11)#>  4 1991 Oct 3611003
    [](tsibbles.html#cb11-12)#>  5 1991 Nov 3565869
    [](tsibbles.html#cb11-13)#>  6 1991 Dec 4306371
    [](tsibbles.html#cb11-14)#>  7 1992 Jan 5088335
    [](tsibbles.html#cb11-15)#>  8 1992 Feb 2814520
    [](tsibbles.html#cb11-16)#>  9 1992 Mar 2985811
    [](tsibbles.html#cb11-17)#> 10 1992 Apr 3204780
    [](tsibbles.html#cb11-18)#> # ℹ 194 more rows

The new variable `TotalC` is the sum of all `Cost` values for each month.

We can create new variables using the `mutate()` function. Here we change the units from dollars to millions of dollars:
    
    
    [](tsibbles.html#cb12-1)PBS |>
    [](tsibbles.html#cb12-2)  filter(ATC2 == "A10") |>
    [](tsibbles.html#cb12-3)  select(Month, Concession, Type, Cost) |>
    [](tsibbles.html#cb12-4)  summarise(TotalC = sum(Cost)) |>
    [](tsibbles.html#cb12-5)  mutate(Cost = TotalC/1e6)
    [](tsibbles.html#cb12-6)#> # A tsibble: 204 x 3 [1M]
    [](tsibbles.html#cb12-7)#>       Month  TotalC  Cost
    [](tsibbles.html#cb12-8)#>       <mth>   <dbl> <dbl>
    [](tsibbles.html#cb12-9)#>  1 1991 Jul 3526591  3.53
    [](tsibbles.html#cb12-10)#>  2 1991 Aug 3180891  3.18
    [](tsibbles.html#cb12-11)#>  3 1991 Sep 3252221  3.25
    [](tsibbles.html#cb12-12)#>  4 1991 Oct 3611003  3.61
    [](tsibbles.html#cb12-13)#>  5 1991 Nov 3565869  3.57
    [](tsibbles.html#cb12-14)#>  6 1991 Dec 4306371  4.31
    [](tsibbles.html#cb12-15)#>  7 1992 Jan 5088335  5.09
    [](tsibbles.html#cb12-16)#>  8 1992 Feb 2814520  2.81
    [](tsibbles.html#cb12-17)#>  9 1992 Mar 2985811  2.99
    [](tsibbles.html#cb12-18)#> 10 1992 Apr 3204780  3.20
    [](tsibbles.html#cb12-19)#> # ℹ 194 more rows

Finally, we will save the resulting tsibble for examples later in this chapter.
    
    
    [](tsibbles.html#cb13-1)PBS |>
    [](tsibbles.html#cb13-2)  filter(ATC2 == "A10") |>
    [](tsibbles.html#cb13-3)  select(Month, Concession, Type, Cost) |>
    [](tsibbles.html#cb13-4)  summarise(TotalC = sum(Cost)) |>
    [](tsibbles.html#cb13-5)  mutate(Cost = TotalC / 1e6) -> a10

At the end of this series of piped functions, we have used a right assignment (`->`), which is not common in R code, but is convenient at the end of a long series of commands as it continues the flow of the code.

### Read a csv file and convert to a tsibble[](tsibbles.html#read-a-csv-file-and-convert-to-a-tsibble)

Almost all of the data used in this book is already stored as `tsibble` objects. But most data lives in databases, MS-Excel files or csv files, before it is imported into R. So often the first step in creating a tsibble is to read in the data, and then identify the index and key variables.

For example, suppose we have the following quarterly data stored in a csv file (only the first 10 rows are shown). This data set provides information on the size of the prison population in Australia, disaggregated by state, gender, legal status and indigenous status. (Here, ATSI stands for Aboriginal or Torres Strait Islander.)

Date | State | Gender | Legal | Indigenous | Count  
---|---|---|---|---|---  
2005-03-01 | ACT | Female | Remanded | ATSI | 0  
2005-03-01 | ACT | Female | Remanded | Non-ATSI | 2  
2005-03-01 | ACT | Female | Sentenced | ATSI | 0  
2005-03-01 | ACT | Female | Sentenced | Non-ATSI | 5  
2005-03-01 | ACT | Male | Remanded | ATSI | 7  
2005-03-01 | ACT | Male | Remanded | Non-ATSI | 58  
2005-03-01 | ACT | Male | Sentenced | ATSI | 5  
2005-03-01 | ACT | Male | Sentenced | Non-ATSI | 101  
2005-03-01 | NSW | Female | Remanded | ATSI | 51  
2005-03-01 | NSW | Female | Remanded | Non-ATSI | 131  
  
We can read it into R, and create a tsibble object, by simply identifying which column contains the time index, and which columns are keys. The remaining columns are values — there can be many value columns, although in this case there is only one (`Count`). The original csv file stored the dates as individual days, although the data is actually quarterly, so we need to convert the `Date` variable to quarters.
    
    
    [](tsibbles.html#cb14-1)prison <- readr::read_csv("https://OTexts.com/fpp3/extrafiles/prison_population.csv")
    
    
    [](tsibbles.html#cb15-1)prison <- prison |>
    [](tsibbles.html#cb15-2)  mutate(Quarter = yearquarter(Date)) |>
    [](tsibbles.html#cb15-3)  select(-Date) |>
    [](tsibbles.html#cb15-4)  as_tsibble(key = c(State, Gender, Legal, Indigenous),
    [](tsibbles.html#cb15-5)             index = Quarter)
    [](tsibbles.html#cb15-6)
    [](tsibbles.html#cb15-7)prison
    [](tsibbles.html#cb15-8)#> # A tsibble: 3,072 x 6 [1Q]
    [](tsibbles.html#cb15-9)#> # Key:       State, Gender, Legal, Indigenous [64]
    [](tsibbles.html#cb15-10)#>    State Gender Legal    Indigenous Count Quarter
    [](tsibbles.html#cb15-11)#>    <chr> <chr>  <chr>    <chr>      <dbl>   <qtr>
    [](tsibbles.html#cb15-12)#>  1 ACT   Female Remanded ATSI           0 2005 Q1
    [](tsibbles.html#cb15-13)#>  2 ACT   Female Remanded ATSI           1 2005 Q2
    [](tsibbles.html#cb15-14)#>  3 ACT   Female Remanded ATSI           0 2005 Q3
    [](tsibbles.html#cb15-15)#>  4 ACT   Female Remanded ATSI           0 2005 Q4
    [](tsibbles.html#cb15-16)#>  5 ACT   Female Remanded ATSI           1 2006 Q1
    [](tsibbles.html#cb15-17)#>  6 ACT   Female Remanded ATSI           1 2006 Q2
    [](tsibbles.html#cb15-18)#>  7 ACT   Female Remanded ATSI           1 2006 Q3
    [](tsibbles.html#cb15-19)#>  8 ACT   Female Remanded ATSI           0 2006 Q4
    [](tsibbles.html#cb15-20)#>  9 ACT   Female Remanded ATSI           0 2007 Q1
    [](tsibbles.html#cb15-21)#> 10 ACT   Female Remanded ATSI           1 2007 Q2
    [](tsibbles.html#cb15-22)#> # ℹ 3,062 more rows

This tsibble contains 64 separate time series corresponding to the combinations of the 8 states, 2 genders, 2 legal statuses and 2 indigenous statuses. Each of these series is 48 observations in length, from 2005 Q1 to 2016 Q4.

For a tsibble to be valid, it requires a unique index for each combination of keys. The `tsibble()` or `as_tsibble()` function will return an error if this is not true.

### The seasonal period[](tsibbles.html#the-seasonal-period)

Some graphics and some models will use the seasonal period of the data. The seasonal period is the number of observations before the seasonal pattern repeats. In most cases, this will be automatically detected using the time index variable.

Some common periods for different time intervals are shown in the table below:

Data | Minute | Hour | Day | Week | Year  
---|---|---|---|---|---  
Quarters |  |  |  |  | 4  
Months |  |  |  |  | 12  
Weeks |  |  |  |  | 52  
Days |  |  |  | 7 | 365.25  
Hours |  |  | 24 | 168 | 8766  
Minutes |  | 60 | 1440 | 10080 | 525960  
Seconds | 60 | 3600 | 86400 | 604800 | 31557600  
  
For quarterly, monthly and weekly data, there is only one seasonal period — the number of observations within each year. Actually, there are not \\(52\\) weeks in a year, but \\(365.25/7 = 52.18\\) on average, allowing for a leap year every fourth year. Approximating seasonal periods to integers can be useful as many seasonal terms in models only support integer seasonal periods.

If the data is observed more than once per week, then there is often more than one seasonal pattern in the data. For example, data with daily observations might have weekly (period\\(=7\\)) or annual (period\\(=365.25\\)) seasonal patterns. Similarly, data that are observed every minute might have hourly (period\\(=60\\)), daily (period\\(=24\times60=1440\\)), weekly (period\\(=24\times60\times7=10080\\)) and annual seasonality (period\\(=24\times60\times365.25=525960\\)).

More complicated (and unusual) seasonal patterns can be specified using the `period()` function in the `lubridate` package.


---

## 2.2 Time plots[](time-plots.html#time-plots)

For time series data, the obvious graph to start with is a time plot. That is, the observations are plotted against the time of observation, with consecutive observations joined by straight lines. Figure [2.1](time-plots.html#fig:ansett) shows the weekly economy passenger load on Ansett airlines between Australia’s two largest cities.
    
    
    [](time-plots.html#cb16-1)melsyd_economy <- ansett |>
    [](time-plots.html#cb16-2)  filter(Airports == "MEL-SYD", Class == "Economy") |>
    [](time-plots.html#cb16-3)  mutate(Passengers = Passengers/1000)
    [](time-plots.html#cb16-4)autoplot(melsyd_economy, Passengers) +
    [](time-plots.html#cb16-5)  labs(title = "Ansett airlines economy class",
    [](time-plots.html#cb16-6)       subtitle = "Melbourne-Sydney",
    [](time-plots.html#cb16-7)       y = "Passengers ('000)")

Figure 2.1: Weekly economy passenger load on Ansett Airlines. 

We will use the `autoplot()` command frequently. It automatically produces an appropriate plot of whatever you pass to it in the first argument. In this case, it recognises `melsyd_economy` as a time series and produces a time plot.

The time plot immediately reveals some interesting features.

  * There was a period in 1989 when no passengers were carried — this was due to an industrial dispute.
  * There was a period of reduced load in 1992. This was due to a trial in which some economy class seats were replaced by business class seats.
  * A large increase in passenger load occurred in the second half of 1991.
  * There are some large dips in load around the start of each year. These are due to holiday effects.
  * There is a long-term fluctuation in the level of the series which increases during 1987, decreases in 1989, and increases again through 1990 and 1991.


Any model will need to take all these features into account in order to effectively forecast the passenger load into the future.

A simpler time series is shown in Figure [2.2](time-plots.html#fig:a10plot), using the `a10` data saved earlier.
    
    
    [](time-plots.html#cb17-1)autoplot(a10, Cost) +
    [](time-plots.html#cb17-2)  labs(y = "$ (millions)",
    [](time-plots.html#cb17-3)       title = "Australian antidiabetic drug sales")

Figure 2.2: Monthly sales of antidiabetic drugs in Australia. 

Here, there is a clear and increasing trend. There is also a strong seasonal pattern that increases in size as the level of the series increases. The sudden drop at the start of each year is caused by a government subsidisation scheme that makes it cost-effective for patients to stockpile drugs at the end of the calendar year. Any forecasts of this series would need to capture the seasonal pattern, and the fact that the trend is changing slowly.


---

## 2.3 Time series patterns[](tspatterns.html#tspatterns)

In describing these time series, we have used words such as “trend” and “seasonal” which need to be defined more carefully.

Trend
     A _trend_ exists when there is a long-term increase or decrease in the data. It does not have to be linear. Sometimes we will refer to a trend as “changing direction”, when it might go from an increasing trend to a decreasing trend. There is a trend in the antidiabetic drug sales data shown in Figure [2.2](time-plots.html#fig:a10plot). 
Seasonal
     A _seasonal_ pattern occurs when a time series is affected by seasonal factors such as the time of the year or the day of the week. Seasonality is always of a fixed and known period. The monthly sales of antidiabetic drugs (Figure [2.2](time-plots.html#fig:a10plot)) shows seasonality which is induced partly by the change in the cost of the drugs at the end of the calendar year. (Note that one series can have more than one seasonal pattern.) 
Cyclic
     A _cycle_ occurs when the data exhibit rises and falls that are not of a fixed frequency. These fluctuations are usually due to economic conditions, and are often related to the “business cycle”. The duration of these fluctuations is usually at least 2 years. 

Many people confuse cyclic behaviour with seasonal behaviour, but they are really quite different. If the fluctuations are not of a fixed frequency then they are cyclic; if the frequency is unchanging and associated with some aspect of the calendar, then the pattern is seasonal. In general, the average length of cycles is longer than the length of a seasonal pattern, and the magnitudes of cycles tend to be more variable than the magnitudes of seasonal patterns.

Many time series include trend, cycles and seasonality. When choosing a forecasting method, we will first need to identify the time series patterns in the data, and then choose a method that is able to capture the patterns properly.

The examples in Figure [2.3](tspatterns.html#fig:fourexamples) show different combinations of these components.

Figure 2.3: Four examples of time series showing different patterns. 

  1. The monthly housing sales (top left) show strong seasonality within each year, as well as some strong cyclic behaviour with a period of about 6–10 years. There is no apparent trend in the data over this period.
  2. The US treasury bill contracts (top right) show results from the Chicago market for 100 consecutive trading days in 1981. Here there is no seasonality, but an obvious downward trend. Possibly, if we had a much longer series, we would see that this downward trend is actually part of a long cycle, but when viewed over only 100 days it appears to be a trend.
  3. The Australian quarterly electricity production (bottom left) shows a strong increasing trend, with strong seasonality. There is no evidence of any cyclic behaviour here.
  4. The daily change in the Google closing stock price (bottom right) has no trend, seasonality or cyclic behaviour. There are random fluctuations which do not appear to be very predictable, and no strong patterns that would help with developing a forecasting model.




---

## 2.4 Seasonal plots[](seasonal-plots.html#seasonal-plots)

A seasonal plot is similar to a time plot except that the data are plotted against the individual “seasons” in which the data were observed. An example is given in Figure [2.4](seasonal-plots.html#fig:seasonplot1) showing the antidiabetic drug sales.
    
    
    [](seasonal-plots.html#cb18-1)a10 |>
    [](seasonal-plots.html#cb18-2)  gg_season(Cost, labels = "both") +
    [](seasonal-plots.html#cb18-3)  labs(y = "$ (millions)",
    [](seasonal-plots.html#cb18-4)       title = "Seasonal plot: Antidiabetic drug sales")

Figure 2.4: Seasonal plot of monthly antidiabetic drug sales in Australia. 

This is the same data as was shown earlier, but now the data from each year overlap. A seasonal plot allows the underlying seasonal pattern to be seen more clearly, and is especially useful in identifying years in which the pattern changes.

There is a large jump in sales in January each year. These are probably sales in late December as customers stockpile before the end of the calendar year, but the sales are not registered with the government until a week or two later. The graph also shows that there was an unusually small number of sales in March 2008 (most other years show an increase between February and March). The small number of sales in June 2008 is probably due to incomplete counting of sales at the time the data were collected.

### Multiple seasonal periods[](seasonal-plots.html#multiple-seasonal-periods)

Where the data has more than one seasonal pattern, the `period` argument can be used to select which seasonal plot is required. The `vic_elec` data contains half-hourly electricity demand for the state of Victoria, Australia. We can plot the daily pattern, weekly pattern or yearly pattern by specifying the `period` argument as shown in Figures [2.5](seasonal-plots.html#fig:multipleseasonplots1)–[2.7](seasonal-plots.html#fig:multipleseasonplots3).

In the first plot, the three days with 25 hours are when daylight saving ended in each year and so these days contained an extra hour. There were also three days with only 23 hours each (when daylight saving started) but these are hidden beneath all the other lines on the plot.
    
    
    [](seasonal-plots.html#cb19-1)vic_elec |> gg_season(Demand, period = "day") +
    [](seasonal-plots.html#cb19-2)  theme(legend.position = "none") +
    [](seasonal-plots.html#cb19-3)  labs(y="MWh", title="Electricity demand: Victoria")

Figure 2.5: Seasonal plot showing daily seasonal patterns for Victorian electricity demand. 
    
    
    [](seasonal-plots.html#cb20-1)vic_elec |> gg_season(Demand, period = "week") +
    [](seasonal-plots.html#cb20-2)  theme(legend.position = "none") +
    [](seasonal-plots.html#cb20-3)  labs(y="MWh", title="Electricity demand: Victoria")

Figure 2.6: Seasonal plot showing weekly seasonal patterns for Victorian electricity demand. 
    
    
    [](seasonal-plots.html#cb21-1)vic_elec |> gg_season(Demand, period = "year") +
    [](seasonal-plots.html#cb21-2)  labs(y="MWh", title="Electricity demand: Victoria")

Figure 2.7: Seasonal plot showing yearly seasonal patterns for Victorian electricity demand. 


---

## 2.5 Seasonal subseries plots[](subseries.html#subseries)

An alternative plot that emphasises the seasonal patterns is where the data for each season are collected together in separate mini time plots.
    
    
    [](subseries.html#cb22-1)a10 |>
    [](subseries.html#cb22-2)  gg_subseries(Cost) +
    [](subseries.html#cb22-3)  labs(
    [](subseries.html#cb22-4)    y = "$ (millions)",
    [](subseries.html#cb22-5)    title = "Australian antidiabetic drug sales"
    [](subseries.html#cb22-6)  )

Figure 2.8: Seasonal subseries plot of monthly antidiabetic drug sales in Australia. 

The blue horizontal lines indicate the means for each month. This form of plot enables the underlying seasonal pattern to be seen clearly, and also shows the changes in seasonality over time. It is especially useful in identifying changes within particular seasons. In this example, the plot is not particularly revealing; but in some cases, this is the most useful way of viewing seasonal changes over time.

### Example: Australian holiday tourism[](subseries.html#example-australian-holiday-tourism)

Australian quarterly vacation data provides an interesting example of how these plots can reveal information. First we need to extract the relevant data from the `tourism` tsibble. All the usual `tidyverse` wrangling verbs apply. To get the total visitor nights spent on Holiday by State for each quarter (i.e., ignoring Regions) we can use the following code. Note that we do not have to explicitly group by the time index as this is required in a `tsibble`.
    
    
    [](subseries.html#cb23-1)holidays <- tourism |>
    [](subseries.html#cb23-2)  filter(Purpose == "Holiday") |>
    [](subseries.html#cb23-3)  group_by(State) |>
    [](subseries.html#cb23-4)  summarise(Trips = sum(Trips))
    
    
    [](subseries.html#cb24-1)holidays
    [](subseries.html#cb24-2)#> # A tsibble: 640 x 3 [1Q]
    [](subseries.html#cb24-3)#> # Key:       State [8]
    [](subseries.html#cb24-4)#>    State Quarter Trips
    [](subseries.html#cb24-5)#>    <chr>   <qtr> <dbl>
    [](subseries.html#cb24-6)#>  1 ACT   1998 Q1  196.
    [](subseries.html#cb24-7)#>  2 ACT   1998 Q2  127.
    [](subseries.html#cb24-8)#>  3 ACT   1998 Q3  111.
    [](subseries.html#cb24-9)#>  4 ACT   1998 Q4  170.
    [](subseries.html#cb24-10)#>  5 ACT   1999 Q1  108.
    [](subseries.html#cb24-11)#>  6 ACT   1999 Q2  125.
    [](subseries.html#cb24-12)#>  7 ACT   1999 Q3  178.
    [](subseries.html#cb24-13)#>  8 ACT   1999 Q4  218.
    [](subseries.html#cb24-14)#>  9 ACT   2000 Q1  158.
    [](subseries.html#cb24-15)#> 10 ACT   2000 Q2  155.
    [](subseries.html#cb24-16)#> # ℹ 630 more rows

Time plots of each series show that there is strong seasonality for most states, but that the seasonal peaks do not coincide.
    
    
    [](subseries.html#cb25-1)autoplot(holidays, Trips) +
    [](subseries.html#cb25-2)  labs(y = "Overnight trips ('000)",
    [](subseries.html#cb25-3)       title = "Australian domestic holidays")

Figure 2.9: Time plots of Australian domestic holidays by state. 

To see the timing of the seasonal peaks in each state, we can use a season plot. Figure [2.10](subseries.html#fig:holidaysseason) makes it clear that the southern states of Australia (Tasmania, Victoria and South Australia) have strongest tourism in Q1 (their summer), while the northern states (Queensland and the Northern Territory) have the strongest tourism in Q3 (their dry season).
    
    
    [](subseries.html#cb26-1)gg_season(holidays, Trips) +
    [](subseries.html#cb26-2)  labs(y = "Overnight trips ('000)",
    [](subseries.html#cb26-3)       title = "Australian domestic holidays")

Figure 2.10: Season plots of Australian domestic holidays by state. 

The corresponding subseries plots are shown in Figure [2.11](subseries.html#fig:holidayssubseries).
    
    
    [](subseries.html#cb27-1)holidays |>
    [](subseries.html#cb27-2)  gg_subseries(Trips) +
    [](subseries.html#cb27-3)  labs(y = "Overnight trips ('000)",
    [](subseries.html#cb27-4)       title = "Australian domestic holidays")

Figure 2.11: Subseries plots of Australian domestic holidays by state. 

This figure makes it evident that Western Australian tourism has jumped markedly in recent years, while Victorian tourism has increased in Q1 and Q4 but not in the middle of the year.


---

## 2.6 Scatterplots[](scatterplots.html#scatterplots)

The graphs discussed so far are useful for visualising individual time series. It is also useful to explore relationships _between_ time series.

Figures [2.12](scatterplots.html#fig:edemand) and [2.13](scatterplots.html#fig:victemp) show two time series: half-hourly electricity demand (in Gigawatts) and temperature (in degrees Celsius), for 2014 in Victoria, Australia. The temperatures are for Melbourne, the largest city in Victoria, while the demand values are for the entire state.
    
    
    [](scatterplots.html#cb28-1)vic_elec |>
    [](scatterplots.html#cb28-2)  filter(year(Time) == 2014) |>
    [](scatterplots.html#cb28-3)  autoplot(Demand) +
    [](scatterplots.html#cb28-4)  labs(y = "GW",
    [](scatterplots.html#cb28-5)       title = "Half-hourly electricity demand: Victoria")

Figure 2.12: Half hourly electricity demand in Victoria, Australia, for 2014. 
    
    
    [](scatterplots.html#cb29-1)vic_elec |>
    [](scatterplots.html#cb29-2)  filter(year(Time) == 2014) |>
    [](scatterplots.html#cb29-3)  autoplot(Temperature) +
    [](scatterplots.html#cb29-4)  labs(
    [](scatterplots.html#cb29-5)    y = "Degrees Celsius",
    [](scatterplots.html#cb29-6)    title = "Half-hourly temperatures: Melbourne, Australia"
    [](scatterplots.html#cb29-7)  )

Figure 2.13: Half hourly temperature in Melbourne, Australia, for 2014. 

We can study the relationship between demand and temperature by plotting one series against the other.
    
    
    [](scatterplots.html#cb30-1)vic_elec |>
    [](scatterplots.html#cb30-2)  filter(year(Time) == 2014) |>
    [](scatterplots.html#cb30-3)  ggplot(aes(x = Temperature, y = Demand)) +
    [](scatterplots.html#cb30-4)  geom_point() +
    [](scatterplots.html#cb30-5)  labs(title="Electricity demand versus Temperature",
    [](scatterplots.html#cb30-6)       x = "Temperature (degrees Celsius)",
    [](scatterplots.html#cb30-7)       y = "Electricity demand (GW)")

Figure 2.14: Half-hourly electricity demand plotted against temperature for 2014 in Victoria, Australia. 

This scatterplot helps us to visualise the relationship between the variables. It is clear that high demand occurs when temperatures are high due to the effect of air-conditioning. But there is also a heating effect, where demand increases for very low temperatures.

### Correlation[](scatterplots.html#correlation)

It is common to compute _correlation coefficients_ to measure the strength of the linear relationship between two variables. The correlation between variables \\(x\\) and \\(y\\) is given by \\[ r = \frac{\sum (x_{t} - \bar{x})(y_{t}-\bar{y})}{\sqrt{\sum(x_{t}-\bar{x})^2}\sqrt{\sum(y_{t}-\bar{y})^2}}. \\] The value of \\(r\\) always lies between \\(-1\\) and \\(1\\) with negative values indicating a negative relationship and positive values indicating a positive relationship. The graphs in Figure [2.15](scatterplots.html#fig:corr) show examples of data sets with varying levels of correlation.

Figure 2.15: Examples of data sets with different levels of correlation. 

The correlation coefficient only measures the strength of the _linear_ relationship between two variables, and can sometimes be misleading. For example, the correlation for the electricity demand and temperature data shown in Figure [2.14](scatterplots.html#fig:edemand2) is 0.28, but the _non-linear_ relationship is stronger than that.

Figure 2.16: Each of these plots has a correlation coefficient of 0.82. Data from Anscombe ([1973](scatterplots.html#ref-Anscombe1973graphs)). 

The plots in Figure [2.16](scatterplots.html#fig:anscombe) all have correlation coefficients of 0.82, but they have very different relationships. This shows how important it is to look at the plots of the data and not simply rely on correlation values.

### Scatterplot matrices[](scatterplots.html#scatterplot-matrices)

When there are several potential predictor variables, it is useful to plot each variable against each other variable. Consider the eight time series shown in Figure [2.17](scatterplots.html#fig:vntimeplots), showing quarterly visitor numbers across states and territories of Australia.
    
    
    [](scatterplots.html#cb31-1)visitors <- tourism |>
    [](scatterplots.html#cb31-2)  group_by(State) |>
    [](scatterplots.html#cb31-3)  summarise(Trips = sum(Trips))
    [](scatterplots.html#cb31-4)visitors |>
    [](scatterplots.html#cb31-5)  ggplot(aes(x = Quarter, y = Trips)) +
    [](scatterplots.html#cb31-6)  geom_line() +
    [](scatterplots.html#cb31-7)  facet_grid(vars(State), scales = "free_y") +
    [](scatterplots.html#cb31-8)  labs(title = "Australian domestic tourism",
    [](scatterplots.html#cb31-9)       y= "Overnight trips ('000)")

Figure 2.17: Quarterly visitor nights for the states and territories of Australia. 

To see the relationships between these eight time series, we can plot each time series against the others. These plots can be arranged in a scatterplot matrix, as shown in Figure [2.18](scatterplots.html#fig:ScatterMatrixch2). (This plot requires the `GGally` package to be installed.)
    
    
    [](scatterplots.html#cb32-1)visitors |>
    [](scatterplots.html#cb32-2)  pivot_wider(values_from=Trips, names_from=State) |>
    [](scatterplots.html#cb32-3)  GGally::ggpairs(columns = 2:9)

Figure 2.18: A scatterplot matrix of the quarterly visitor nights in the states and territories of Australia. 

For each panel, the variable on the vertical axis is given by the variable name in that row, and the variable on the horizontal axis is given by the variable name in that column. There are many options available to produce different plots within each panel. In the default version, the correlations are shown in the upper right half of the plot, while the scatterplots are shown in the lower half. On the diagonal are shown density plots.

The value of the scatterplot matrix is that it enables a quick view of the relationships between all pairs of variables. In this example, mostly positive relationships are revealed, with the strongest relationships being between the neighbouring states located in the south and south east coast of Australia, namely, New South Wales, Victoria and South Australia. Some negative relationships are also revealed between the Northern Territory and other regions. The Northern Territory is located in the north of Australia famous for its outback desert landscapes visited mostly in winter. Hence, the peak visitation in the Northern Territory is in the July (winter) quarter in contrast to January (summer) quarter for the rest of the regions.

### Bibliography[](bibliography.html#bibliography)

Anscombe, F. J. (1973). Graphs in statistical analysis. _The American Statistician_ , _27_(1), 17–21. [__](https://doi.org/10.1080/00031305.1973.10478966)


---

## 2.7 Lag plots[](lag-plots.html#lag-plots)

Figure [2.19](lag-plots.html#fig:beerlagplot) displays scatterplots of quarterly Australian beer production (introduced in Figure [1.1](data-methods.html#fig:beer)), where the horizontal axis shows lagged values of the time series. Each graph shows \\(y_{t}\\) plotted against \\(y_{t-k}\\) for different values of \\(k\\).
    
    
    [](lag-plots.html#cb33-1)recent_production <- aus_production |>
    [](lag-plots.html#cb33-2)  filter(year(Quarter) >= 2000)
    [](lag-plots.html#cb33-3)recent_production |>
    [](lag-plots.html#cb33-4)  gg_lag(Beer, geom = "point") +
    [](lag-plots.html#cb33-5)  labs(x = "lag(Beer, k)")

Figure 2.19: Lagged scatterplots for quarterly beer production. 

Here the colours indicate the quarter of the variable on the vertical axis. The relationship is strongly positive at lags 4 and 8, reflecting the strong seasonality in the data. The negative relationship seen for lags 2 and 6 occurs because peaks (in Q4) are plotted against troughs (in Q2)


---

## 2.8 Autocorrelation[](acf.html#acf)

Just as correlation measures the extent of a linear relationship between two variables, autocorrelation measures the linear relationship between _lagged values_ of a time series.

There are several autocorrelation coefficients, corresponding to each panel in the lag plot. For example, \\(r_{1}\\) measures the relationship between \\(y_{t}\\) and \\(y_{t-1}\\), \\(r_{2}\\) measures the relationship between \\(y_{t}\\) and \\(y_{t-2}\\), and so on.

The value of \\(r_{k}\\) can be written as \\[ r_{k} = \frac{\sum\limits_{t=k+1}^T (y_{t}-\bar{y})(y_{t-k}-\bar{y})} {\sum\limits_{t=1}^T (y_{t}-\bar{y})^2}, \\] where \\(T\\) is the length of the time series. The autocorrelation coefficients make up the _autocorrelation function_ or ACF.

The autocorrelation coefficients for the beer production data can be computed using the `ACF()` function.
    
    
    [](acf.html#cb34-1)recent_production |> ACF(Beer, lag_max = 9)
    [](acf.html#cb34-2)#> # A tsibble: 9 x 2 [1Q]
    [](acf.html#cb34-3)#>        lag      acf
    [](acf.html#cb34-4)#>   <cf_lag>    <dbl>
    [](acf.html#cb34-5)#> 1       1Q -0.0530 
    [](acf.html#cb34-6)#> 2       2Q -0.758  
    [](acf.html#cb34-7)#> 3       3Q -0.0262 
    [](acf.html#cb34-8)#> 4       4Q  0.802  
    [](acf.html#cb34-9)#> 5       5Q -0.0775 
    [](acf.html#cb34-10)#> 6       6Q -0.657  
    [](acf.html#cb34-11)#> 7       7Q  0.00119
    [](acf.html#cb34-12)#> 8       8Q  0.707  
    [](acf.html#cb34-13)#> 9       9Q -0.0888

The values in the `acf` column are \\(r_1,\dots,r_9\\), corresponding to the nine scatterplots in Figure [2.19](lag-plots.html#fig:beerlagplot). We usually plot the ACF to see how the correlations change with the lag \\(k\\). The plot is sometimes known as a _correlogram_.
    
    
    [](acf.html#cb35-1)recent_production |>
    [](acf.html#cb35-2)  ACF(Beer) |>
    [](acf.html#cb35-3)  autoplot() + labs(title="Australian beer production")

Figure 2.20: Autocorrelation function of quarterly beer production. 

In this graph:

  * \\(r_{4}\\) is higher than for the other lags. This is due to the seasonal pattern in the data: the peaks tend to be four quarters apart and the troughs tend to be four quarters apart.
  * \\(r_{2}\\) is more negative than for the other lags because troughs tend to be two quarters behind peaks.
  * The dashed blue lines indicate whether the correlations are significantly different from zero (as explained in Section [2.9](wn.html#wn)).


### Trend and seasonality in ACF plots[](acf.html#trend-and-seasonality-in-acf-plots)

When data have a trend, the autocorrelations for small lags tend to be large and positive because observations nearby in time are also nearby in value. So the ACF of a trended time series tends to have positive values that slowly decrease as the lags increase.

When data are seasonal, the autocorrelations will be larger for the seasonal lags (at multiples of the seasonal period) than for other lags.

When data are both trended and seasonal, you see a combination of these effects. The `a10` data plotted in Figure [2.2](time-plots.html#fig:a10plot) shows both trend and seasonality. Its ACF is shown in Figure [2.21](acf.html#fig:acfa10). The slow decrease in the ACF as the lags increase is due to the trend, while the “scalloped” shape is due to the seasonality.
    
    
    [](acf.html#cb36-1)a10 |>
    [](acf.html#cb36-2)  ACF(Cost, lag_max = 48) |>
    [](acf.html#cb36-3)  autoplot() +
    [](acf.html#cb36-4)  labs(title="Australian antidiabetic drug sales")

Figure 2.21: ACF of monthly Australian antidiabetic drug sales. 


---

## 2.9 White noise[](wn.html#wn)

Time series that show no autocorrelation are called **white noise**. Figure [2.22](wn.html#fig:wnoise) gives an example of a white noise series.
    
    
    [](wn.html#cb37-1)set.seed(30)
    [](wn.html#cb37-2)y <- tsibble(sample = 1:50, wn = rnorm(50), index = sample)
    [](wn.html#cb37-3)y |> autoplot(wn) + labs(title = "White noise", y = "")

Figure 2.22: A white noise time series. 
    
    
    [](wn.html#cb38-1)y |>
    [](wn.html#cb38-2)  ACF(wn) |>
    [](wn.html#cb38-3)  autoplot() + labs(title = "White noise")

Figure 2.23: Autocorrelation function for the white noise series. 

For white noise series, we expect each autocorrelation to be close to zero. Of course, they will not be exactly equal to zero as there is some random variation. For a white noise series, we expect 95% of the spikes in the ACF to lie within \\(\pm 1.96/\sqrt{T}\\) where \\(T\\) is the length of the time series. It is common to plot these bounds on a graph of the ACF (the blue dashed lines above). If one or more large spikes are outside these bounds, or if substantially more than 5% of spikes are outside these bounds, then the series is probably not white noise.

In this example, \\(T=50\\) and so the bounds are at \\(\pm 1.96/\sqrt{50} = \pm 0.28\\). All of the autocorrelation coefficients lie within these limits, confirming that the data are white noise.


---

## 2.10 Exercises[](graphics-exercises.html#graphics-exercises)

  1. Explore the following four time series: `Bricks` from `aus_production`, `Lynx` from `pelt`, `Close` from `gafa_stock`, `Demand` from `vic_elec`.

     * Use `?` (or `help()`) to find out about the data in each series.
     * What is the time interval of each series?
     * Use `autoplot()` to produce a time plot of each series.
     * For the last plot, modify the axis labels and title.
  2. Use `filter()` to find what days corresponded to the peak closing price for each of the four stocks in `gafa_stock`.

  3. Download the file `tute1.csv` from [the book website](https://bit.ly/fpptute1), open it in Excel (or some other spreadsheet application), and review its contents. You should find four columns of information. Columns B through D each contain a quarterly series, labelled Sales, AdBudget and GDP. Sales contains the quarterly sales for a small company over the period 1981-2005. AdBudget is the advertising budget and GDP is the gross domestic product. All series have been adjusted for inflation.

     1. You can read the data into R with the following script:
            
            [](graphics-exercises.html#cb39-1)tute1 <- readr::read_csv("tute1.csv")
            [](graphics-exercises.html#cb39-2)View(tute1)

     2. Convert the data to time series
            
            [](graphics-exercises.html#cb40-1)mytimeseries <- tute1 |>
            [](graphics-exercises.html#cb40-2)  mutate(Quarter = yearquarter(Quarter)) |>
            [](graphics-exercises.html#cb40-3)  as_tsibble(index = Quarter)

     3. Construct time series plots of each of the three series
            
            [](graphics-exercises.html#cb41-1)mytimeseries |>
            [](graphics-exercises.html#cb41-2)  pivot_longer(-Quarter) |>
            [](graphics-exercises.html#cb41-3)  ggplot(aes(x = Quarter, y = value, colour = name)) +
            [](graphics-exercises.html#cb41-4)  geom_line() +
            [](graphics-exercises.html#cb41-5)  facet_grid(name ~ ., scales = "free_y")

Check what happens when you don’t include `facet_grid()`.

  4. The `USgas` package contains data on the demand for natural gas in the US.

     1. Install the `USgas` package.
     2. Create a tsibble from `us_total` with year as the index and state as the key.
     3. Plot the annual natural gas consumption by state for the New England area (comprising the states of Maine, Vermont, New Hampshire, Massachusetts, Connecticut and Rhode Island).
  5.      1. Download `tourism.xlsx` from [the book website](https://bit.ly/fpptourism) and read it into R using `readxl::read_excel()`.
     2. Create a tsibble which is identical to the `tourism` tsibble from the `tsibble` package.
     3. Find what combination of `Region` and `Purpose` had the maximum number of overnight trips on average.
     4. Create a new tsibble which combines the Purposes and Regions, and just has total trips by State.
  6. The `aus_arrivals` data set comprises quarterly international arrivals to Australia from Japan, New Zealand, UK and the US.

     * Use `autoplot()`, `gg_season()` and `gg_subseries()` to compare the differences between the arrivals from these four countries.
     * Can you identify any unusual observations?
  7. Monthly Australian retail data is provided in `aus_retail`. Select one of the time series as follows (but choose your own seed value):
         
         [](graphics-exercises.html#cb42-1)set.seed(12345678)
         [](graphics-exercises.html#cb42-2)myseries <- aus_retail |>
         [](graphics-exercises.html#cb42-3)  filter(`Series ID` == sample(aus_retail$`Series ID`,1))

Explore your chosen retail time series using the following functions:

`autoplot()`, `gg_season()`, `gg_subseries()`, `gg_lag()`,

`ACF() |> autoplot()`

Can you spot any seasonality, cyclicity and trend? What do you learn about the series?


  8. Use the following graphics functions: `autoplot()`, `gg_season()`, `gg_subseries()`, `gg_lag()`, `ACF()` and explore features from the following time series: “Total Private” `Employed` from `us_employment`, `Bricks` from `aus_production`, `Hare` from `pelt`, “H02” `Cost` from `PBS`, and `Barrels` from `us_gasoline`.

     * Can you spot any seasonality, cyclicity and trend?
     * What do you learn about the series?
     * What can you say about the seasonal patterns?
     * Can you identify any unusual years?
  9. The following time plots and ACF plots correspond to four different time series. Your task is to match each time plot in the first row with one of the ACF plots in the second row.

  10. The `aus_livestock` data contains the monthly total number of pigs slaughtered in Victoria, Australia, from Jul 1972 to Dec 2018. Use `filter()` to extract pig slaughters in Victoria between 1990 and 1995. Use `autoplot()` and `ACF()` for this data. How do they differ from white noise? If a longer period of data is used, what difference does it make to the ACF?

  11.      1. Use the following code to compute the daily changes in Google closing stock prices.
            
            [](graphics-exercises.html#cb43-1)dgoog <- gafa_stock |>
            [](graphics-exercises.html#cb43-2)  filter(Symbol == "GOOG", year(Date) >= 2018) |>
            [](graphics-exercises.html#cb43-3)  mutate(trading_day = row_number()) |>
            [](graphics-exercises.html#cb43-4)  update_tsibble(index = trading_day, regular = TRUE) |>
            [](graphics-exercises.html#cb43-5)  mutate(diff = difference(Close))

     2. Why was it necessary to re-index the tsibble?

     3. Plot these differences and their ACF.

     4. Do the changes in the stock prices look like white noise?




---

## 2.11 Further reading[](graphics-reading.html#graphics-reading)

  * W. S. Cleveland ([1993](graphics-reading.html#ref-Cleveland1993)) is a classic book on the principles of visualisation for data analysis. While it is more than 20 years old, the ideas are timeless.
  * Unwin ([2015](graphics-reading.html#ref-Unwin2015)) is a modern introduction to graphical data analysis using R. It does not have much information on time series graphics, but plenty of excellent general advice on using graphics for data analysis.


### Bibliography[](bibliography.html#bibliography)

Cleveland, W. S. (1993). _Visualizing data_. Hobart Press. [__](http://amazon.com/dp/0963488406?tag=otexts20)

Unwin, A. (2015). _Graphical data analysis with R_. Chapman; Hall/CRC. [__](http://amazon.com/dp/1498715230?tag=otexts20)


---

# Chapter 3 Time series decomposition[](decomposition.html#decomposition)

Time series data can exhibit a variety of patterns, and it is often helpful to split a time series into several components, each representing an underlying pattern category.

In Section [2.3](tspatterns.html#tspatterns) we discussed three types of time series patterns: trend, seasonality and cycles. When we decompose a time series into components, we usually combine the trend and cycle into a single **trend-cycle** component (often just called the **trend** for simplicity). Thus we can think of a time series as comprising three components: a trend-cycle component, a seasonal component, and a remainder component (containing anything else in the time series). For some time series (e.g., those that are observed at least daily), there can be more than one seasonal component, corresponding to the different seasonal periods.

In this chapter, we consider the most common methods for extracting these components from a time series. Often this is done to help improve understanding of the time series, but it can also be used to improve forecast accuracy.

When decomposing a time series, it is sometimes helpful to first transform or adjust the series in order to make the decomposition (and later analysis) as simple as possible. So we will begin by discussing transformations and adjustments.


---

## 3.1 Transformations and adjustments[](transformations.html#transformations)

Adjusting the historical data can often lead to a simpler time series. Here, we deal with four kinds of adjustments: calendar adjustments, population adjustments, inflation adjustments and mathematical transformations. The purpose of these adjustments and transformations is to simplify the patterns in the historical data by removing known sources of variation, or by making the pattern more consistent across the whole data set. Simpler patterns are usually easier to model and lead to more accurate forecasts.

### Calendar adjustments[](transformations.html#calendar-adjustments)

Some of the variation seen in seasonal data may be due to simple calendar effects. In such cases, it is usually much easier to remove the variation before doing any further analysis.

For example, if you are studying the total monthly sales in a retail store, there will be variation between the months simply because of the different numbers of trading days in each month, in addition to the seasonal variation across the year. It is easy to remove this variation by computing average sales per trading day in each month, rather than total sales in the month. Then we effectively remove the calendar variation.

### Population adjustments[](transformations.html#population-adjustments)

Any data that are affected by population changes can be adjusted to give per-capita data. That is, consider the data per person (or per thousand people, or per million people) rather than the total. For example, if you are studying the number of hospital beds in a particular region over time, the results are much easier to interpret if you remove the effects of population changes by considering the number of beds per thousand people. Then you can see whether there have been real increases in the number of beds, or whether the increases are due entirely to population increases. It is possible for the total number of beds to increase, but the number of beds per thousand people to decrease. This occurs when the population is increasing faster than the number of hospital beds. For most data that are affected by population changes, it is best to use per-capita data rather than the totals.

This can be seen in the `global_economy` dataset, where a common transformation of GDP is GDP per-capita.
    
    
    [](transformations.html#cb44-1)global_economy |>
    [](transformations.html#cb44-2)  filter(Country == "Australia") |>
    [](transformations.html#cb44-3)  autoplot(GDP/Population) +
    [](transformations.html#cb44-4)  labs(title= "GDP per capita", y = "$US")

Figure 3.1: Australian GDP per-capita. 

### Inflation adjustments[](transformations.html#inflation-adjustments)

Data which are affected by the value of money are best adjusted before modelling. For example, the average cost of a new house will have increased over the last few decades due to inflation. A $200,000 house this year is not the same as a $200,000 house twenty years ago. For this reason, financial time series are usually adjusted so that all values are stated in dollar values from a particular year. For example, the house price data may be stated in year 2000 dollars.

To make these adjustments, a price index is used. If \\(z_{t}\\) denotes the price index and \\(y_{t}\\) denotes the original house price in year \\(t\\), then \\(x_{t} = y_{t}/z_{t} * z_{2000}\\) gives the adjusted house price at year 2000 dollar values. Price indexes are often constructed by government agencies. For consumer goods, a common price index is the Consumer Price Index (or CPI).

This allows us to compare the growth or decline of industries relative to a common price value. For example, looking at aggregate annual “newspaper and book” retail turnover from `aus_retail`, and adjusting the data for inflation using CPI from `global_economy` allows us to understand the changes over time.
    
    
    [](transformations.html#cb45-1)print_retail <- aus_retail |>
    [](transformations.html#cb45-2)  filter(Industry == "Newspaper and book retailing") |>
    [](transformations.html#cb45-3)  group_by(Industry) |>
    [](transformations.html#cb45-4)  index_by(Year = year(Month)) |>
    [](transformations.html#cb45-5)  summarise(Turnover = sum(Turnover))
    [](transformations.html#cb45-6)aus_economy <- global_economy |>
    [](transformations.html#cb45-7)  filter(Code == "AUS")
    
    
    [](transformations.html#cb46-1)print_retail |>
    [](transformations.html#cb46-2)  left_join(aus_economy, by = "Year") |>
    [](transformations.html#cb46-3)  mutate(Adjusted_turnover = Turnover / CPI * 100) |>
    [](transformations.html#cb46-4)  pivot_longer(c(Turnover, Adjusted_turnover),
    [](transformations.html#cb46-5)               values_to = "Turnover") |>
    [](transformations.html#cb46-6)  mutate(name = factor(name,
    [](transformations.html#cb46-7)         levels=c("Turnover","Adjusted_turnover"))) |>
    [](transformations.html#cb46-8)  ggplot(aes(x = Year, y = Turnover)) +
    [](transformations.html#cb46-9)  geom_line() +
    [](transformations.html#cb46-10)  facet_grid(name ~ ., scales = "free_y") +
    [](transformations.html#cb46-11)  labs(title = "Turnover: Australian print media industry",
    [](transformations.html#cb46-12)       y = "$AU")

Figure 3.2: Turnover for the Australian print media industry in Australian dollars. The ‘Adjusted’ turnover has been adjusted for inflation using the CPI. 

By adjusting for inflation using the CPI, we can see that Australia’s newspaper and book retailing industry has been in decline much longer than the original data suggests. The adjusted turnover is in 2010 Australian dollars, as CPI is 100 in 2010 in this data set.

### Mathematical transformations[](transformations.html#mathematical-transformations)

If the data shows variation that increases or decreases with the level of the series, then a transformation can be useful. For example, a logarithmic transformation is often useful. If we denote the original observations as \\(y_{1},\dots,y_{T}\\) and the transformed observations as \\(w_{1}, \dots, w_{T}\\), then \\(w_t = \log(y_t)\\). Logarithms are useful because they are interpretable: changes in a log value are relative (or percentage) changes on the original scale. So if log base 10 is used, then an increase of 1 on the log scale corresponds to a multiplication of 10 on the original scale. If any value of the original series is zero or negative, then logarithms are not possible.

Sometimes other transformations are also used (although they are not so interpretable). For example, square roots and cube roots can be used. These are called **power transformations** because they can be written in the form \\(w_{t} = y_{t}^p\\).

A useful family of transformations, that includes both logarithms and power transformations, is the family of **Box-Cox transformations** ([Box & Cox, 1964](transformations.html#ref-BC64)), which depend on the parameter \\(\lambda\\) and are defined as follows: \\[\begin{equation} w_t = \begin{cases} \log(y_t) & \text{if $\lambda=0$}; \\\ (\text{sign}(y_t)|y_t|^\lambda-1)/\lambda & \text{otherwise}. \end{cases} \tag{3.1} \end{equation}\\] This is actually a modified Box-Cox transformation, discussed in Bickel & Doksum ([1981](transformations.html#ref-Bickel1981)), which allows for negative values of \\(y_t\\) provided \\(\lambda > 0\\).

The logarithm in a Box-Cox transformation is always a natural logarithm (i.e., to base \\(e\\)). So if \\(\lambda=0\\), natural logarithms are used, but if \\(\lambda\ne0\\), a power transformation is used, followed by some simple scaling.

If \\(\lambda=1\\), then \\(w_t = y_t-1\\), so the transformed data is shifted downwards but there is no change in the shape of the time series. For all other values of \\(\lambda\\), the time series will change shape.

Use the slider below to see the effect of varying \\(\lambda\\) to transform Australian quarterly gas production:

Figure 3.3: Box-Cox transformations applied to Australian quarterly gas production. 

A good value of \\(\lambda\\) is one which makes the size of the seasonal variation about the same across the whole series, as that makes the forecasting model simpler. In this case, \\(\lambda=0.10\\) works quite well, although any value of \\(\lambda\\) between 0.0 and 0.2 would give similar results.

The `guerrero` feature ([Guerrero, 1993](transformations.html#ref-Guerrero93)) can be used to choose a value of lambda for you. In this case it chooses \\(\lambda=0.11\\). (See the next chapter for discussion of the `features()` function.)
    
    
    [](transformations.html#cb47-1)lambda <- aus_production |>
    [](transformations.html#cb47-2)  features(Gas, features = guerrero) |>
    [](transformations.html#cb47-3)  pull(lambda_guerrero)
    [](transformations.html#cb47-4)aus_production |>
    [](transformations.html#cb47-5)  autoplot(box_cox(Gas, lambda)) +
    [](transformations.html#cb47-6)  labs(y = "",
    [](transformations.html#cb47-7)       title = latex2exp::TeX(paste0(
    [](transformations.html#cb47-8)         "Transformed gas production with $\\lambda$ = ",
    [](transformations.html#cb47-9)         round(lambda,2))))

Figure 3.4: Transformed Australian quarterly gas production with the \\(\lambda\\) parameter chosen using the Guerrero method. 

### Bibliography[](bibliography.html#bibliography)

Bickel, P. J., & Doksum, K. A. (1981). An analysis of transformations revisited. _Journal of the American Statistical Association_ , _76_(374), 296–311. [__](https://doi.org/10.1080/01621459.1981.10477649)

Box, G. E. P., & Cox, D. R. (1964). An analysis of transformations. _Journal of the Royal Statistical Society. Series B, Statistical Methodology_ , _26_(2), 211–252. [__](https://doi.org/10.1111/j.2517-6161.1964.tb00553.x)

Guerrero, V. M. (1993). Time-series analysis supported by power transformations. _Journal of Forecasting_ , _12_(1), 37–48. [__](https://doi.org/10.1002/for.3980120104)


---

## 3.2 Time series components[](components.html#components)

If we assume an additive decomposition, then we can write \\[ y_{t} = S_{t} + T_{t} + R_t, \\] where \\(y_{t}\\) is the data, \\(S_{t}\\) is the seasonal component, \\(T_{t}\\) is the trend-cycle component, and \\(R_t\\) is the remainder component, all at period \\(t\\). Alternatively, a multiplicative decomposition would be written as \\[ y_{t} = S_{t} \times T_{t} \times R_t. \\]

The additive decomposition is the most appropriate if the magnitude of the seasonal fluctuations, or the variation around the trend-cycle, does not vary with the level of the time series. When the variation in the seasonal pattern, or the variation around the trend-cycle, appears to be proportional to the level of the time series, then a multiplicative decomposition is more appropriate. Multiplicative decompositions are common with economic time series.

An alternative to using a multiplicative decomposition is to first transform the data until the variation in the series appears to be stable over time, then use an additive decomposition. When a log transformation has been used, this is equivalent to using a multiplicative decomposition on the original data because \\[ y_{t} = S_{t} \times T_{t} \times R_t \quad\text{is equivalent to}\quad \log y_{t} = \log S_{t} + \log T_{t} + \log R_t. \\]

### Example: Employment in the US retail sector[](components.html#example-employment-in-the-us-retail-sector)

We will look at several methods for obtaining the components \\(S_{t}\\), \\(T_{t}\\) and \\(R_{t}\\) later in this chapter, but first it is helpful to see an example. We will decompose the number of persons employed in retail as shown in Figure [3.5](components.html#fig:usretailemployment). The data shows the total monthly number of persons in thousands employed in the retail sector across the US since 1990.
    
    
    [](components.html#cb48-1)us_retail_employment <- us_employment |>
    [](components.html#cb48-2)  filter(year(Month) >= 1990, Title == "Retail Trade") |>
    [](components.html#cb48-3)  select(-Series_ID)
    [](components.html#cb48-4)autoplot(us_retail_employment, Employed) +
    [](components.html#cb48-5)  labs(y = "Persons (thousands)",
    [](components.html#cb48-6)       title = "Total employment in US retail")

Figure 3.5: Total number of persons employed in US retail. 

To illustrate the ideas, we will use the STL decomposition method, which is discussed in Section [3.6](stl.html#stl).
    
    
    [](components.html#cb49-1)dcmp <- us_retail_employment |>
    [](components.html#cb49-2)  model(stl = STL(Employed))
    [](components.html#cb49-3)components(dcmp)
    [](components.html#cb49-4)#> # A dable: 357 x 7 [1M]
    [](components.html#cb49-5)#> # Key:     .model [1]
    [](components.html#cb49-6)#> # :        Employed = trend + season_year + remainder
    [](components.html#cb49-7)#>    .model    Month Employed  trend season_year remainder season_adjust
    [](components.html#cb49-8)#>    <chr>     <mth>    <dbl>  <dbl>       <dbl>     <dbl>         <dbl>
    [](components.html#cb49-9)#>  1 stl    1990 Jan   13256. 13288.      -33.0      0.836        13289.
    [](components.html#cb49-10)#>  2 stl    1990 Feb   12966. 13269.     -258.     -44.6          13224.
    [](components.html#cb49-11)#>  3 stl    1990 Mar   12938. 13250.     -290.     -22.1          13228.
    [](components.html#cb49-12)#>  4 stl    1990 Apr   13012. 13231.     -220.       1.05         13232.
    [](components.html#cb49-13)#>  5 stl    1990 May   13108. 13211.     -114.      11.3          13223.
    [](components.html#cb49-14)#>  6 stl    1990 Jun   13183. 13192.      -24.3     15.5          13207.
    [](components.html#cb49-15)#>  7 stl    1990 Jul   13170. 13172.      -23.2     21.6          13193.
    [](components.html#cb49-16)#>  8 stl    1990 Aug   13160. 13151.       -9.52    17.8          13169.
    [](components.html#cb49-17)#>  9 stl    1990 Sep   13113. 13131.      -39.5     22.0          13153.
    [](components.html#cb49-18)#> 10 stl    1990 Oct   13185. 13110.       61.6     13.2          13124.
    [](components.html#cb49-19)#> # ℹ 347 more rows

The output above shows the components of an STL decomposition. The original data is shown (as `Employed`), followed by the estimated components. This output forms a “dable” or decomposition table. The header to the table shows that the `Employed` series has been decomposed additively.

The `trend` column (containing the trend-cycle \\(T_t\\)) follows the overall movement of the series, ignoring any seasonality and random fluctuations, as shown in Figure [3.6](components.html#fig:empltrend).
    
    
    [](components.html#cb50-1)components(dcmp) |>
    [](components.html#cb50-2)  as_tsibble() |>
    [](components.html#cb50-3)  autoplot(Employed, colour="gray") +
    [](components.html#cb50-4)  geom_line(aes(y=trend), colour = "#D55E00") +
    [](components.html#cb50-5)  labs(
    [](components.html#cb50-6)    y = "Persons (thousands)",
    [](components.html#cb50-7)    title = "Total employment in US retail"
    [](components.html#cb50-8)  )

Figure 3.6: Total number of persons employed in US retail: the trend-cycle component (orange) and the raw data (grey). 

We can plot all of the components in a single figure using `autoplot()`, as shown in Figure [3.7](components.html#fig:emplstl).
    
    
    [](components.html#cb51-1)components(dcmp) |> autoplot()

Figure 3.7: The total number of persons employed in US retail (top) and its three additive components. 

The three components are shown separately in the bottom three panels. These components can be added together to reconstruct the data shown in the top panel. Notice that the seasonal component changes over time, so that any two consecutive years have similar patterns, but years far apart may have different seasonal patterns. The remainder component shown in the bottom panel is what is left over when the seasonal and trend-cycle components have been subtracted from the data.

The grey bars to the left of each panel show the relative scales of the components. Each grey bar represents the same length but because the plots are on different scales, the bars vary in size. The large grey bar in the bottom panel shows that the variation in the remainder component is smallest compared to the variation in the data. If we shrank the bottom three panels until their bars became the same size as that in the data panel, then all the panels would be on the same scale.

### Seasonally adjusted data[](components.html#seasonally-adjusted-data)

If the seasonal component is removed from the original data, the resulting values are the “seasonally adjusted” data. For an additive decomposition, the seasonally adjusted data are given by \\(y_{t}-S_{t}\\), and for multiplicative data, the seasonally adjusted values are obtained using \\(y_{t}/S_{t}\\).

Figure [3.8](components.html#fig:empl-retail-sa) shows the seasonally adjusted number of persons employed.
    
    
    [](components.html#cb52-1)components(dcmp) |>
    [](components.html#cb52-2)  as_tsibble() |>
    [](components.html#cb52-3)  autoplot(Employed, colour = "gray") +
    [](components.html#cb52-4)  geom_line(aes(y=season_adjust), colour = "#0072B2") +
    [](components.html#cb52-5)  labs(y = "Persons (thousands)",
    [](components.html#cb52-6)       title = "Total employment in US retail")

Figure 3.8: Seasonally adjusted retail employment data (blue) and the original data (grey). 

If the variation due to seasonality is not of primary interest, the seasonally adjusted series can be useful. For example, monthly unemployment data are usually seasonally adjusted in order to highlight variation due to the underlying state of the economy rather than the seasonal variation. An increase in unemployment due to school leavers seeking work is seasonal variation, while an increase in unemployment due to an economic recession is non-seasonal. Most economic analysts who study unemployment data are more interested in the non-seasonal variation. Consequently, employment data (and many other economic series) are usually seasonally adjusted.

Seasonally adjusted series contain the remainder component as well as the trend-cycle. Therefore, they are not “smooth”, and “downturns” or “upturns” can be misleading. If the purpose is to look for turning points in a series, and interpret any changes in direction, then it is better to use the trend-cycle component rather than the seasonally adjusted data.


---

## 3.3 Moving averages[](moving-averages.html#moving-averages)

The classical method of time series decomposition originated in the 1920s and was widely used until the 1950s. It still forms the basis of many time series decomposition methods, so it is important to understand how it works. The first step in a classical decomposition is to use a moving average method to estimate the trend-cycle, so we begin by discussing moving averages.

### Moving average smoothing[](moving-averages.html#moving-average-smoothing)

A moving average of order \\(m\\) can be written as \\[\begin{equation} \hat{T}_{t} = \frac{1}{m} \sum_{j=-k}^k y_{t+j}, \tag{3.2} \end{equation}\\] where \\(m=2k+1\\). That is, the estimate of the trend-cycle at time \\(t\\) is obtained by averaging values of the time series within \\(k\\) periods of \\(t\\). Observations that are nearby in time are also likely to be close in value. Therefore, the average eliminates some of the randomness in the data, leaving a smooth trend-cycle component. We call this an **\\(m\\) -MA**, meaning a moving average of order \\(m\\).

For example, consider Figure [3.9](moving-averages.html#fig:aus-exports) which shows exports of goods and services for Australia as a percentage of GDP from 1960 to 2017. The data are also shown in Table [3.1](moving-averages.html#tab:aus-exports-tbl).
    
    
    [](moving-averages.html#cb53-1)global_economy |>
    [](moving-averages.html#cb53-2)  filter(Country == "Australia") |>
    [](moving-averages.html#cb53-3)  autoplot(Exports) +
    [](moving-averages.html#cb53-4)  labs(y = "% of GDP", title = "Total Australian exports")

Figure 3.9: Australian exports of goods and services: 1960–2017. 

Table 3.1: Annual Australian exports of goods and services: 1960–2017. Year | Exports | 5-MA  
---|---|---  
1960 | 12.99 |   
1961 | 12.40 |   
1962 | 13.94 | 13.46  
1963 | 13.01 | 13.50  
1964 | 14.94 | 13.61  
1965 | 13.22 | 13.40  
1966 | 12.93 | 13.25  
1967 | 12.88 | 12.66  
… | … | …  
2010 | 19.84 | 21.21  
2011 | 21.47 | 21.17  
2012 | 21.52 | 20.78  
2013 | 19.99 | 20.81  
2014 | 21.08 | 20.37  
2015 | 20.01 | 20.32  
2016 | 19.25 |   
2017 | 21.27 |   
  
In the last column of this table, a moving average of order 5 is shown, providing an estimate of the trend-cycle. The first value in this column is the average of the first five observations, 1960–1964; the second value in the 5-MA column is the average of the values for 1961–1965; and so on. Each value in the 5-MA column is the average of the observations in the five year window centred on the corresponding year. In the notation of Equation [(3.2)](moving-averages.html#eq:ma), column 5-MA contains the values of \\(\hat{T}_{t}\\) with \\(k=2\\) and \\(m=2k+1=5\\). There are no values for either the first two years or the last two years, because we do not have two observations on either side. Later we will use more sophisticated methods of trend-cycle estimation which do allow estimates near the endpoints.

This is easily computed using `slide_dbl()` from the `slider` package which applies a function to “sliding” time windows. In this case, we use the `mean()` function with a window of size 5.
    
    
    [](moving-averages.html#cb54-1)aus_exports <- global_economy |>
    [](moving-averages.html#cb54-2)  filter(Country == "Australia") |>
    [](moving-averages.html#cb54-3)  mutate(
    [](moving-averages.html#cb54-4)    `5-MA` = slider::slide_dbl(Exports, mean,
    [](moving-averages.html#cb54-5)                .before = 2, .after = 2, .complete = TRUE)
    [](moving-averages.html#cb54-6)  )

To see what the trend-cycle estimate looks like, we plot it along with the original data in Figure [3.10](moving-averages.html#fig:aus-exports-plot).
    
    
    [](moving-averages.html#cb55-1)aus_exports |>
    [](moving-averages.html#cb55-2)  autoplot(Exports) +
    [](moving-averages.html#cb55-3)  geom_line(aes(y = `5-MA`), colour = "#D55E00") +
    [](moving-averages.html#cb55-4)  labs(y = "% of GDP",
    [](moving-averages.html#cb55-5)       title = "Total Australian exports")

Figure 3.10: Australian exports (black) along with the 5-MA estimate of the trend-cycle (orange). 

Notice that the trend-cycle (in orange) is smoother than the original data and captures the main movement of the time series without all of the minor fluctuations. The order of the moving average determines the smoothness of the trend-cycle estimate. In general, a larger order means a smoother curve. Figure [3.11](moving-averages.html#fig:aus-exports-compare) shows the effect of changing the order of the moving average for the Australian exports data.

Figure 3.11: Different moving averages applied to the Australian exports data. 

Simple moving averages such as these are usually of an odd order (e.g., 3, 5, 7, etc.). This is so they are symmetric: in a moving average of order \\(m=2k+1\\), the middle observation, and \\(k\\) observations on either side, are averaged. But if \\(m\\) was even, it would no longer be symmetric.

### Moving averages of moving averages[](moving-averages.html#moving-averages-of-moving-averages)

It is possible to apply a moving average to a moving average. One reason for doing this is to make an even-order moving average symmetric.

For example, we might take a moving average of order 4, and then apply another moving average of order 2 to the results. In the following table, this has been done for the first few years of the Australian quarterly beer production data.
    
    
    [](moving-averages.html#cb56-1)beer <- aus_production |>
    [](moving-averages.html#cb56-2)  filter(year(Quarter) >= 1992) |>
    [](moving-averages.html#cb56-3)  select(Quarter, Beer)
    [](moving-averages.html#cb56-4)beer_ma <- beer |>
    [](moving-averages.html#cb56-5)  mutate(
    [](moving-averages.html#cb56-6)    `4-MA` = slider::slide_dbl(Beer, mean,
    [](moving-averages.html#cb56-7)                .before = 1, .after = 2, .complete = TRUE),
    [](moving-averages.html#cb56-8)    `2x4-MA` = slider::slide_dbl(`4-MA`, mean,
    [](moving-averages.html#cb56-9)                .before = 1, .after = 0, .complete = TRUE)
    [](moving-averages.html#cb56-10)  )

Table 3.2: A moving average of order 4 applied to the quarterly beer data, followed by a moving average of order 2. Quarter | Beer | 4-MA | 2x4-MA  
---|---|---|---  
1992 Q1 | 443.00 |  |   
1992 Q2 | 410.00 | 451.25 |   
1992 Q3 | 420.00 | 448.75 | 450.00  
1992 Q4 | 532.00 | 451.50 | 450.12  
1993 Q1 | 433.00 | 449.00 | 450.25  
1993 Q2 | 421.00 | 444.00 | 446.50  
… | … | … | …  
2009 Q1 | 415.00 | 430.00 | 428.88  
2009 Q2 | 398.00 | 430.00 | 430.00  
2009 Q3 | 419.00 | 429.75 | 429.88  
2009 Q4 | 488.00 | 423.75 | 426.75  
2010 Q1 | 414.00 |  |   
2010 Q2 | 374.00 |  |   
  
The notation “\\(2\times4\\)-MA” in the last column means a 4-MA followed by a 2-MA. The values in the last column are obtained by taking a moving average of order 2 of the values in the previous column. For example, the first two values in the 4-MA column are 451.25=(443+410+420+532)/4 and 448.75=(410+420+532+433)/4. The first value in the 2x4-MA column is the average of these two: 450.00=(451.25+448.75)/2.

When a 2-MA follows a moving average of an even order (such as 4), it is called a “centred moving average of order 4”. This is because the results are now symmetric. To see that this is the case, we can write the \\(2\times4\\)-MA as follows: \\[\begin{align*} \hat{T}_{t} &= \frac{1}{2}\Big[ \frac{1}{4} (y_{t-2}+y_{t-1}+y_{t}+y_{t+1}) + \frac{1}{4} (y_{t-1}+y_{t}+y_{t+1}+y_{t+2})\Big] \\\ &= \frac{1}{8}y_{t-2}+\frac14y_{t-1} + \frac14y_{t}+\frac14y_{t+1}+\frac18y_{t+2}. \end{align*}\\] It is now a weighted average of observations that is symmetric.

Other combinations of moving averages are also possible. For example, a \\(3\times3\\)-MA is often used, and consists of a moving average of order 3 followed by another moving average of order 3. In general, an even order MA should be followed by an even order MA to make it symmetric. Similarly, an odd order MA should be followed by an odd order MA.

### Estimating the trend-cycle with seasonal data[](moving-averages.html#estimating-the-trend-cycle-with-seasonal-data)

The most common use of centred moving averages is for estimating the trend-cycle from seasonal data. Consider the \\(2\times4\\)-MA: \\[ \hat{T}_{t} = \frac{1}{8}y_{t-2} + \frac14y_{t-1} + \frac14y_{t} + \frac14y_{t+1} + \frac18y_{t+2}. \\] When applied to quarterly data, each quarter of the year is given equal weight as the first and last terms apply to the same quarter in consecutive years. Consequently, the seasonal variation will be averaged out and the resulting values of \\(\hat{T}_t\\) will have little or no seasonal variation remaining. A similar effect would be obtained using a \\(2\times 8\\)-MA or a \\(2\times 12\\)-MA to quarterly data.

In general, a \\(2\times m\\)-MA is equivalent to a weighted moving average of order \\(m+1\\) where all observations take the weight \\(1/m\\), except for the first and last terms which take weights \\(1/(2m)\\). So, if the seasonal period is even and of order \\(m\\), we use a \\(2\times m\\)-MA to estimate the trend-cycle. If the seasonal period is odd and of order \\(m\\), we use a \\(m\\)-MA to estimate the trend-cycle. For example, a \\(2\times 12\\)-MA can be used to estimate the trend-cycle of monthly data with annual seasonality and a 7-MA can be used to estimate the trend-cycle of daily data with a weekly seasonality.

Other choices for the order of the MA will usually result in trend-cycle estimates being contaminated by the seasonality in the data.

### Example: Employment in the US retail sector[](moving-averages.html#example-employment-in-the-us-retail-sector-1)
    
    
    [](moving-averages.html#cb57-1)us_retail_employment_ma <- us_retail_employment |>
    [](moving-averages.html#cb57-2)  mutate(
    [](moving-averages.html#cb57-3)    `12-MA` = slider::slide_dbl(Employed, mean,
    [](moving-averages.html#cb57-4)                .before = 5, .after = 6, .complete = TRUE),
    [](moving-averages.html#cb57-5)    `2x12-MA` = slider::slide_dbl(`12-MA`, mean,
    [](moving-averages.html#cb57-6)                .before = 1, .after = 0, .complete = TRUE)
    [](moving-averages.html#cb57-7)  )
    [](moving-averages.html#cb57-8)us_retail_employment_ma |>
    [](moving-averages.html#cb57-9)  autoplot(Employed, colour = "gray") +
    [](moving-averages.html#cb57-10)  geom_line(aes(y = `2x12-MA`), colour = "#D55E00") +
    [](moving-averages.html#cb57-11)  labs(y = "Persons (thousands)",
    [](moving-averages.html#cb57-12)       title = "Total employment in US retail")

Figure 3.12: A 2x12-MA applied to the US retail employment series. 

Figure [3.12](moving-averages.html#fig:empl-MA) shows a \\(2\times12\\)-MA applied to the total number of persons employed in the US retail sector. Notice that the smooth line shows no seasonality; it is almost the same as the trend-cycle shown in Figure [3.6](components.html#fig:empltrend), which was estimated using a much more sophisticated method than a moving average. Any other choice for the order of the moving average (except for 24, 36, etc.) would have resulted in a smooth line that showed some seasonal fluctuations.

### Weighted moving averages[](moving-averages.html#weighted-moving-averages)

Combinations of moving averages result in weighted moving averages. For example, the \\(2\times4\\)-MA discussed above is equivalent to a weighted 5-MA with weights given by \\(\left[\frac{1}{8},\frac{1}{4},\frac{1}{4},\frac{1}{4},\frac{1}{8}\right]\\). In general, a weighted \\(m\\)-MA can be written as \\[ \hat{T}_t = \sum_{j=-k}^k a_j y_{t+j}, \\] where \\(k=(m-1)/2\\), and the weights are given by \\(\left[a_{-k},\dots,a_k\right]\\). It is important that the weights all sum to one and that they are symmetric so that \\(a_j = a_{-j}\\). The simple \\(m\\)-MA is a special case where all of the weights are equal to \\(1/m\\).

A major advantage of weighted moving averages is that they yield a smoother estimate of the trend-cycle. Instead of observations entering and leaving the calculation at full weight, their weights slowly increase and then slowly decrease, resulting in a smoother curve.


---

## 3.4 Classical decomposition[](classical-decomposition.html#classical-decomposition)

The classical decomposition method originated in the 1920s. It is a relatively simple procedure, and forms the starting point for most other methods of time series decomposition. There are two forms of classical decomposition: an additive decomposition and a multiplicative decomposition. These are described below for a time series with seasonal period \\(m\\) (e.g., \\(m=4\\) for quarterly data, \\(m=12\\) for monthly data, \\(m=7\\) for daily data with a weekly pattern).

In classical decomposition, we assume that the seasonal component is constant from year to year. For multiplicative seasonality, the \\(m\\) values that form the seasonal component are sometimes called the “seasonal indices”.

### Additive decomposition[](classical-decomposition.html#additive-decomposition)

Step 1
     If \\(m\\) is an even number, compute the trend-cycle component \\(\hat{T}_t\\) using a \\(2\times m\\)-MA. If \\(m\\) is an odd number, compute the trend-cycle component \\(\hat{T}_t\\) using an \\(m\\)-MA. 
Step 2
     Calculate the detrended series: \\(y_t - \hat{T}_t\\). 
Step 3
     To estimate the seasonal component for each season, simply average the detrended values for that season. For example, with monthly data, the seasonal component for March is the average of all the detrended March values in the data. These seasonal component values are then adjusted to ensure that they add to zero. The seasonal component is obtained by stringing together these monthly values, and then replicating the sequence for each year of data. This gives \\(\hat{S}_t\\). 
Step 4
     The remainder component is calculated by subtracting the estimated seasonal and trend-cycle components: \\(\hat{R}_t = y_t - \hat{T}_t - \hat{S}_t\\). 

Figure [3.13](classical-decomposition.html#fig:classical-empl) shows a classical decomposition of the total retail employment series across the US.
    
    
    [](classical-decomposition.html#cb58-1)us_retail_employment |>
    [](classical-decomposition.html#cb58-2)  model(
    [](classical-decomposition.html#cb58-3)    classical_decomposition(Employed, type = "additive")
    [](classical-decomposition.html#cb58-4)  ) |>
    [](classical-decomposition.html#cb58-5)  components() |>
    [](classical-decomposition.html#cb58-6)  autoplot() +
    [](classical-decomposition.html#cb58-7)  labs(title = "Classical additive decomposition of total
    [](classical-decomposition.html#cb58-8)                  US retail employment")

Figure 3.13: A classical additive decomposition of US retail employment. 

### Multiplicative decomposition[](classical-decomposition.html#multiplicative-decomposition)

A classical multiplicative decomposition is similar, except that the subtractions are replaced by divisions.

Step 1
     If \\(m\\) is an even number, compute the trend-cycle component \\(\hat{T}_t\\) using a \\(2\times m\\)-MA. If \\(m\\) is an odd number, compute the trend-cycle component \\(\hat{T}_t\\) using an \\(m\\)-MA. 
Step 2
     Calculate the detrended series: \\(y_t/ \hat{T}_t\\). 
Step 3
     To estimate the seasonal component for each season, simply average the detrended values for that season. For example, with monthly data, the seasonal index for March is the average of all the detrended March values in the data. These seasonal indexes are then adjusted to ensure that they add to \\(m\\). The seasonal component is obtained by stringing together these monthly indexes, and then replicating the sequence for each year of data. This gives \\(\hat{S}_t\\). 
Step 4
     The remainder component is calculated by dividing out the estimated seasonal and trend-cycle components: \\(\hat{R}_{t} = y_t /( \hat{T}_t \hat{S}_t)\\). 

### Comments on classical decomposition[](classical-decomposition.html#comments-on-classical-decomposition)

While classical decomposition is still widely used, it is not recommended, as there are now several much better methods. Some of the problems with classical decomposition are summarised below.

  * The estimate of the trend-cycle is unavailable for the first few and last few observations. For example, if \\(m=12\\), there is no trend-cycle estimate for the first six or the last six observations. Consequently, there is also no estimate of the remainder component for the same time periods.
  * The trend-cycle estimate tends to over-smooth rapid rises and falls in the data.
  * Classical decomposition methods assume that the seasonal component repeats from year to year. For many series, this is a reasonable assumption, but for some longer series it is not. For example, electricity demand patterns have changed over time as air conditioning has become more widespread. In many locations, the seasonal usage pattern from several decades ago had its maximum demand in winter (due to heating), while the current seasonal pattern has its maximum demand in summer (due to air conditioning). Classical decomposition methods are unable to capture these seasonal changes over time.
  * Occasionally, the values of the time series in a small number of periods may be particularly unusual. For example, the monthly air passenger traffic may be affected by an industrial dispute, making the traffic during the dispute different from usual. The classical method is not robust to these kinds of unusual values.




---

## 3.5 Methods used by official statistics agencies[](methods-used-by-official-statistics-agencies.html#methods-used-by-official-statistics-agencies)

Official statistics agencies (such as the US Census Bureau and the Australian Bureau of Statistics) are responsible for a large number of official economic and social time series. These agencies have developed their own decomposition procedures which are used for seasonal adjustment. Most of them use variants of the X-11 method, or the SEATS method, or a combination of the two. These methods are designed specifically to work with quarterly and monthly data, which are the most common series handled by official statistics agencies. They will not handle seasonality of other kinds, such as daily data, or hourly data, or weekly data. We will use the latest implementation of this group of methods known as “X-13ARIMA-SEATS”. For the methods discussed in this section, you will need to have installed the `seasonal` package in R.

### X-11 method[](methods-used-by-official-statistics-agencies.html#x-11-method)

The X-11 method originated in the US Census Bureau and was further developed by Statistics Canada. It is based on classical decomposition, but includes many extra steps and features in order to overcome the drawbacks of classical decomposition that were discussed in the previous section. In particular, trend-cycle estimates are available for all observations including the end points, and the seasonal component is allowed to vary slowly over time. X-11 also handles trading day variation, holiday effects and the effects of known predictors. There are methods for both additive and multiplicative decomposition. The process is entirely automatic and tends to be highly robust to outliers and level shifts in the time series. The details of the X-11 method are described in Dagum & Bianconcini ([2016](methods-used-by-official-statistics-agencies.html#ref-Dagum2016)).
    
    
    [](methods-used-by-official-statistics-agencies.html#cb59-1)x11_dcmp <- us_retail_employment |>
    [](methods-used-by-official-statistics-agencies.html#cb59-2)  model(x11 = X_13ARIMA_SEATS(Employed ~ x11())) |>
    [](methods-used-by-official-statistics-agencies.html#cb59-3)  components()
    [](methods-used-by-official-statistics-agencies.html#cb59-4)autoplot(x11_dcmp) +
    [](methods-used-by-official-statistics-agencies.html#cb59-5)  labs(title =
    [](methods-used-by-official-statistics-agencies.html#cb59-6)    "Decomposition of total US retail employment using X-11.")

Figure 3.14: A multiplicative decomposition of US retail employment using X-11. 

Compare this decomposition with the STL decomposition shown in Figure [3.7](components.html#fig:emplstl) and the classical decomposition shown in Figure [3.13](classical-decomposition.html#fig:classical-empl). The default approach for `X_13ARIMA_SEATS` shown here is a multiplicative decomposition, whereas the STL and classical decompositions shown earlier were additive; but it doesn’t make much difference in this case. The X-11 trend-cycle has captured the sudden fall in the data due to the 2007–2008 global financial crisis better than either of the other two methods (where the effect of the crisis has leaked into the remainder component). Also, the unusual observation in 1996 is now more clearly seen in the X-11 remainder component.

Figure [3.15](methods-used-by-official-statistics-agencies.html#fig:x11-seasadj) shows the trend-cycle component and the seasonally adjusted data, along with the original data. The seasonally adjusted data is very similar to the trend-cycle component in this example, so it is hard to distinguish them on the plot.
    
    
    [](methods-used-by-official-statistics-agencies.html#cb60-1)x11_dcmp |>
    [](methods-used-by-official-statistics-agencies.html#cb60-2)  ggplot(aes(x = Month)) +
    [](methods-used-by-official-statistics-agencies.html#cb60-3)  geom_line(aes(y = Employed, colour = "Data")) +
    [](methods-used-by-official-statistics-agencies.html#cb60-4)  geom_line(aes(y = season_adjust,
    [](methods-used-by-official-statistics-agencies.html#cb60-5)                colour = "Seasonally Adjusted")) +
    [](methods-used-by-official-statistics-agencies.html#cb60-6)  geom_line(aes(y = trend, colour = "Trend")) +
    [](methods-used-by-official-statistics-agencies.html#cb60-7)  labs(y = "Persons (thousands)",
    [](methods-used-by-official-statistics-agencies.html#cb60-8)       title = "Total employment in US retail") +
    [](methods-used-by-official-statistics-agencies.html#cb60-9)  scale_colour_manual(
    [](methods-used-by-official-statistics-agencies.html#cb60-10)    values = c("gray", "#0072B2", "#D55E00"),
    [](methods-used-by-official-statistics-agencies.html#cb60-11)    breaks = c("Data", "Seasonally Adjusted", "Trend")
    [](methods-used-by-official-statistics-agencies.html#cb60-12)  )

Figure 3.15: US retail employment: the original data (grey), the trend-cycle component (orange) and the seasonally adjusted data (barely visible in blue). 

It can be useful to use seasonal plots and seasonal sub-series plots of the seasonal component, to help us visualise the variation in the seasonal component over time. Figure [3.16](methods-used-by-official-statistics-agencies.html#fig:print-media3) shows a seasonal sub-series plot of the seasonal component from Figure [3.14](methods-used-by-official-statistics-agencies.html#fig:x11). In this case, there are only small changes over time.
    
    
    [](methods-used-by-official-statistics-agencies.html#cb61-1)x11_dcmp |>
    [](methods-used-by-official-statistics-agencies.html#cb61-2)  gg_subseries(seasonal)

Figure 3.16: Seasonal sub-series plot of the seasonal component from the X-11 method applied to total US retail employment. 

### SEATS method[](methods-used-by-official-statistics-agencies.html#seats-method)

“SEATS” stands for “Seasonal Extraction in ARIMA Time Series” (ARIMA models are discussed in Chapter [9](arima.html#arima)). This procedure was developed at the Bank of Spain, and is now widely used by government agencies around the world. The details are beyond the scope of this book. However, a complete discussion of the method is available in Dagum & Bianconcini ([2016](methods-used-by-official-statistics-agencies.html#ref-Dagum2016)).
    
    
    [](methods-used-by-official-statistics-agencies.html#cb62-1)seats_dcmp <- us_retail_employment |>
    [](methods-used-by-official-statistics-agencies.html#cb62-2)  model(seats = X_13ARIMA_SEATS(Employed ~ seats())) |>
    [](methods-used-by-official-statistics-agencies.html#cb62-3)  components()
    [](methods-used-by-official-statistics-agencies.html#cb62-4)autoplot(seats_dcmp) +
    [](methods-used-by-official-statistics-agencies.html#cb62-5)  labs(title =
    [](methods-used-by-official-statistics-agencies.html#cb62-6)    "Decomposition of total US retail employment using SEATS")

Figure 3.17: A decomposition of US retail employment obtained using SEATS. 

Figure [3.17](methods-used-by-official-statistics-agencies.html#fig:seats) shows the SEATS method applied to the total retail employment series across the US. The result is quite similar to that obtained using the X-11 method shown in Figure [3.14](methods-used-by-official-statistics-agencies.html#fig:x11).

The `X_13ARIMA_SEATS()` function calls the `seasonal` package which has many options for handling variations of X-11 and SEATS. See [the package website](https://bit.ly/seaspkg) for a detailed introduction to the options and features available.

### Bibliography[](bibliography.html#bibliography)

Dagum, E. B., & Bianconcini, S. (2016). _Seasonal adjustment methods and real time trend-cycle estimation_. Springer. [__](http://amazon.com/dp/3319318209?tag=otexts20)


---

## 3.6 STL decomposition[](stl.html#stl)

STL is a versatile and robust method for decomposing time series. STL is an acronym for “Seasonal and Trend decomposition using Loess”, while loess is a method for estimating nonlinear relationships. The STL method was developed by R. B. Cleveland et al. ([1990](stl.html#ref-Cleveland1990)), and later extended to handle multiple seasonal patterns by Bandara et al. ([2025](stl.html#ref-mstl)).

STL has several advantages over classical decomposition, and the SEATS and X-11 methods:

  * Unlike SEATS and X-11, STL will handle any type of seasonality, not only monthly and quarterly data.
  * The seasonal component is allowed to change over time, and the rate of change can be controlled by the user.
  * The smoothness of the trend-cycle can also be controlled by the user.
  * It can be robust to outliers (i.e., the user can specify a robust decomposition), so that occasional unusual observations will not affect the estimates of the trend-cycle and seasonal components. They will, however, affect the remainder component.


On the other hand, STL has some disadvantages. In particular, it does not handle trading day or calendar variation automatically, and it only provides facilities for additive decompositions.

A multiplicative decomposition can be obtained by first taking logs of the data, then back-transforming the components. Decompositions that are between additive and multiplicative can be obtained using a Box-Cox transformation of the data with \\(0<\lambda<1\\). A value of \\(\lambda=0\\) gives a multiplicative decomposition while \\(\lambda=1\\) gives an additive decomposition.

The best way to begin learning how to use STL is to see some examples and experiment with the settings. Figure [3.7](components.html#fig:emplstl) showed an example of an STL decomposition applied to the total US retail employment series. Figure [3.18](stl.html#fig:empl-stl2) shows an alternative STL decomposition where the trend-cycle is more flexible, the seasonal pattern is fixed, and the robust option has been used.
    
    
    [](stl.html#cb63-1)us_retail_employment |>
    [](stl.html#cb63-2)  model(
    [](stl.html#cb63-3)    STL(Employed ~ trend(window = 7) +
    [](stl.html#cb63-4)                   season(window = "periodic"),
    [](stl.html#cb63-5)    robust = TRUE)) |>
    [](stl.html#cb63-6)  components() |>
    [](stl.html#cb63-7)  autoplot()

Figure 3.18: Total US retail employment (top) and its three additive components obtained from a robust STL decomposition with flexible trend-cycle and fixed seasonality. 

The two main parameters to be chosen when using STL are the trend-cycle window `trend(window = ?)` and the seasonal window `season(window = ?)`. These control how rapidly the trend-cycle and seasonal components can change. Smaller values allow for more rapid changes. Both trend and seasonal windows should be odd numbers; trend window is the number of consecutive observations to be used when estimating the trend-cycle; season window is the number of consecutive years to be used in estimating each value in the seasonal component. Setting the seasonal window to be infinite is equivalent to forcing the seasonal component to be periodic `season(window='periodic')` (i.e., identical across years). This was the case in Figure [3.18](stl.html#fig:empl-stl2).

By default, the `STL()` function provides a convenient automated STL decomposition using a seasonal window of `season(window=11)` when there is a single seasonal period, and the trend window chosen automatically from the seasonal period. The default setting for monthly data is `trend(window=21)`. For multiple seasonal periods, the default seasonal windows are 11, 15, 19, etc., with larger windows corresponding to larger seasonal periods. This usually gives a good balance between overfitting the seasonality and allowing it to slowly change over time. But, as with any automated procedure, the default settings will need adjusting for some time series. In the example shown in Figure [3.7](components.html#fig:emplstl), the default trend window setting produces a trend-cycle component that is too rigid. As a result, signal from the 2008 global financial crisis has leaked into the remainder component, as can be seen in the bottom panel of Figure [3.7](components.html#fig:emplstl). Selecting a shorter trend window as in Figure [3.18](stl.html#fig:empl-stl2) improves this.

### Bibliography[](bibliography.html#bibliography)

Bandara, K., Hyndman, R. J., & Bergmeir, C. (2025). MSTL: A seasonal-trend decomposition algorithm for time series with multiple seasonal patterns. _International J Operational Research_ , _52_(1). [__](https://doi.org/10.1504/IJOR.2022.10048281)

Cleveland, R. B., Cleveland, W. S., McRae, J. E., & Terpenning, I. J. (1990). STL: A seasonal-trend decomposition procedure based on loess. _Journal of Official Statistics_ , _6_(1), 3–33. [__](http://bit.ly/stl1990)


---

## 3.7 Exercises[](decomposition-exercises.html#decomposition-exercises)

  1. Consider the GDP information in `global_economy`. Plot the GDP per capita for each country over time. Which country has the highest GDP per capita? How has this changed over time?

  2. For each of the following series, make a graph of the data. If transforming seems appropriate, do so and describe the effect.

     * United States GDP from `global_economy`.
     * Slaughter of Victorian “Bulls, bullocks and steers” in `aus_livestock`.
     * Victorian Electricity Demand from `vic_elec`.
     * Gas production from `aus_production`.
  3. Why is a Box-Cox transformation unhelpful for the `canadian_gas` data?

  4. What Box-Cox transformation would you select for your retail data (from Exercise 7 in Section [2.10](graphics-exercises.html#graphics-exercises))?

  5. For the following series, find an appropriate Box-Cox transformation in order to stabilise the variance. Tobacco from `aus_production`, Economy class passengers between Melbourne and Sydney from `ansett`, and Pedestrian counts at Southern Cross Station from `pedestrian`.

  6. Show that a \\(3\times5\\) MA is equivalent to a 7-term weighted moving average with weights of 0.067, 0.133, 0.200, 0.200, 0.200, 0.133, and 0.067.

  7. Consider the last five years of the Gas data from `aus_production`.
         
         [](decomposition-exercises.html#cb64-1)gas <- tail(aus_production, 5*4) |> select(Gas)

     1. Plot the time series. Can you identify seasonal fluctuations and/or a trend-cycle?
     2. Use `classical_decomposition` with `type=multiplicative` to calculate the trend-cycle and seasonal indices.
     3. Do the results support the graphical interpretation from part a?
     4. Compute and plot the seasonally adjusted data.
     5. Change one observation to be an outlier (e.g., add 300 to one observation), and recompute the seasonally adjusted data. What is the effect of the outlier?
     6. Does it make any difference if the outlier is near the end rather than in the middle of the time series?
  8. Recall your retail time series data (from Exercise 7 in Section [2.10](graphics-exercises.html#graphics-exercises)). Decompose the series using X-11. Does it reveal any outliers, or unusual features that you had not noticed previously?

  9. Figures [3.19](decomposition-exercises.html#fig:labour) and [3.20](decomposition-exercises.html#fig:labour2) show the result of decomposing the number of persons in the civilian labour force in Australia each month from February 1978 to August 1995.

Figure 3.19: Decomposition of the number of persons in the civilian labour force in Australia each month from February 1978 to August 1995. 

Figure 3.20: Seasonal component from the decomposition shown in the previous figure. 

     1. Write about 3–5 sentences describing the results of the decomposition. Pay particular attention to the scales of the graphs in making your interpretation.
     2. Is the recession of 1991/1992 visible in the estimated components?
  10. This exercise uses the `canadian_gas` data (monthly Canadian gas production in billions of cubic metres, January 1960 – February 2005).

     1. Plot the data using `autoplot()`, `gg_subseries()` and `gg_season()` to look at the effect of the changing seasonality over time.[3](decomposition-exercises.html#fn3)
     2. Do an STL decomposition of the data. You will need to choose a seasonal window to allow for the changing shape of the seasonal component.
     3. How does the seasonal shape change over time? [Hint: Try plotting the seasonal component using `gg_season()`.]
     4. Can you produce a plausible seasonally adjusted series?
     5. Compare the results with those obtained using SEATS and X-11. How are they different?


* * *

  3. The evolving seasonal pattern is possibly due to changes in the regulation of gas prices — thanks to Lewis Kirvan for pointing this out.[↩︎](decomposition-exercises.html#fnref3)




---

## 3.8 Further reading[](decomposition-reading.html#decomposition-reading)

  * A detailed modern discussion of the SEATS and X-11 methods is provided by Dagum & Bianconcini ([2016](decomposition-reading.html#ref-Dagum2016)).
  * R. B. Cleveland et al. ([1990](decomposition-reading.html#ref-Cleveland1990)) introduced STL, and still provides the best description of the algorithm.


### Bibliography[](bibliography.html#bibliography)

Cleveland, R. B., Cleveland, W. S., McRae, J. E., & Terpenning, I. J. (1990). STL: A seasonal-trend decomposition procedure based on loess. _Journal of Official Statistics_ , _6_(1), 3–33. [__](http://bit.ly/stl1990)

Dagum, E. B., & Bianconcini, S. (2016). _Seasonal adjustment methods and real time trend-cycle estimation_. Springer. [__](http://amazon.com/dp/3319318209?tag=otexts20)


---

# Chapter 4 Time series features[](features.html#features)

The `feasts` package includes functions for Feature Extraction And Statistics from Time Series (hence the name). We have already seen some time series features. For example, the autocorrelations discussed in Section [2.8](acf.html#acf) can be considered features of a time series — they are numerical summaries computed from the series. Another feature we saw in the last chapter was the Guerrero estimate of the Box-Cox transformation parameter — again, this is a number computed from a time series.

We can compute many different features on many different time series, and use them to explore the properties of the series. In this chapter we will look at some features that have been found useful in time series exploration, and how they can be used to uncover interesting information about your data. We will use Australian quarterly tourism as a running example (previously discussed in Section [2.5](subseries.html#subseries)).


---

## 4.1 Some simple statistics[](some-simple-statistics.html#some-simple-statistics)

Any numerical summary computed from a time series is a feature of that time series — the mean, minimum or maximum, for example. These can be computed using the `features()` function. For example, let’s compute the means of all the series in the Australian tourism data.
    
    
    [](some-simple-statistics.html#cb65-1)tourism |>
    [](some-simple-statistics.html#cb65-2)  features(Trips, list(mean = mean)) |>
    [](some-simple-statistics.html#cb65-3)  arrange(mean)
    [](some-simple-statistics.html#cb65-4)#> # A tibble: 304 × 4
    [](some-simple-statistics.html#cb65-5)#>    Region          State              Purpose   mean
    [](some-simple-statistics.html#cb65-6)#>    <chr>           <chr>              <chr>    <dbl>
    [](some-simple-statistics.html#cb65-7)#>  1 Kangaroo Island South Australia    Other    0.340
    [](some-simple-statistics.html#cb65-8)#>  2 MacDonnell      Northern Territory Other    0.449
    [](some-simple-statistics.html#cb65-9)#>  3 Wilderness West Tasmania           Other    0.478
    [](some-simple-statistics.html#cb65-10)#>  4 Barkly          Northern Territory Other    0.632
    [](some-simple-statistics.html#cb65-11)#>  5 Clare Valley    South Australia    Other    0.898
    [](some-simple-statistics.html#cb65-12)#>  6 Barossa         South Australia    Other    1.02 
    [](some-simple-statistics.html#cb65-13)#>  7 Kakadu Arnhem   Northern Territory Other    1.04 
    [](some-simple-statistics.html#cb65-14)#>  8 Lasseter        Northern Territory Other    1.14 
    [](some-simple-statistics.html#cb65-15)#>  9 Wimmera         Victoria           Other    1.15 
    [](some-simple-statistics.html#cb65-16)#> 10 MacDonnell      Northern Territory Visiting 1.18 
    [](some-simple-statistics.html#cb65-17)#> # ℹ 294 more rows

Here we see that the series with least average number of visits was “Other” visits to Kangaroo Island in South Australia.

Rather than compute one feature at a time, it is convenient to compute many features at once. A common short summary of a data set is to compute five summary statistics: the minimum, first quartile, median, third quartile and maximum. These divide the data into four equal-size sections, each containing 25% of the data. The `quantile()` function can be used to compute them.
    
    
    [](some-simple-statistics.html#cb66-1)tourism |> features(Trips, quantile)
    [](some-simple-statistics.html#cb66-2)#> # A tibble: 304 × 8
    [](some-simple-statistics.html#cb66-3)#>    Region         State           Purpose    `0%`  `25%`   `50%`  `75%` `100%`
    [](some-simple-statistics.html#cb66-4)#>    <chr>          <chr>           <chr>     <dbl>  <dbl>   <dbl>  <dbl>  <dbl>
    [](some-simple-statistics.html#cb66-5)#>  1 Adelaide       South Australia Busine…  68.7   134.   153.    177.   242.  
    [](some-simple-statistics.html#cb66-6)#>  2 Adelaide       South Australia Holiday 108.    135.   154.    172.   224.  
    [](some-simple-statistics.html#cb66-7)#>  3 Adelaide       South Australia Other    25.9    43.9   53.8    62.5  107.  
    [](some-simple-statistics.html#cb66-8)#>  4 Adelaide       South Australia Visiti… 137.    179.   206.    229.   270.  
    [](some-simple-statistics.html#cb66-9)#>  5 Adelaide Hills South Australia Busine…   0       0      1.26    3.92  28.6 
    [](some-simple-statistics.html#cb66-10)#>  6 Adelaide Hills South Australia Holiday   0       5.77   8.52   14.1   35.8 
    [](some-simple-statistics.html#cb66-11)#>  7 Adelaide Hills South Australia Other     0       0      0.908   2.09   8.95
    [](some-simple-statistics.html#cb66-12)#>  8 Adelaide Hills South Australia Visiti…   0.778   8.91  12.2    16.8   81.1 
    [](some-simple-statistics.html#cb66-13)#>  9 Alice Springs  Northern Terri… Busine…   1.01    9.13  13.3    18.5   34.1 
    [](some-simple-statistics.html#cb66-14)#> 10 Alice Springs  Northern Terri… Holiday   2.81   16.9   31.5    44.8   76.5 
    [](some-simple-statistics.html#cb66-15)#> # ℹ 294 more rows

Here the minimum is labelled `0%` and the maximum is labelled `100%`.


---

## 4.2 ACF features[](acf-features.html#acf-features)

Autocorrelations were discussed in Section [2.8](acf.html#acf). All the autocorrelations of a series can be considered features of that series. We can also summarise the autocorrelations to produce new features; for example, the sum of the first ten squared autocorrelation coefficients is a useful summary of how much autocorrelation there is in a series, regardless of lag.

We can also compute autocorrelations of the changes in the series between periods. That is, we “difference” the data and create a new time series consisting of the differences between consecutive observations. Then we can compute the autocorrelations of this new differenced series. Occasionally it is useful to apply the same differencing operation again, so we compute the differences of the differences. The autocorrelations of this double differenced series may provide useful information.

Another related approach is to compute seasonal differences of a series. If we had monthly data, for example, we would compute the difference between consecutive Januaries, consecutive Februaries, and so on. This enables us to look at how the series is changing between years, rather than between months. Again, the autocorrelations of the seasonally differenced series may provide useful information.

We discuss differencing of time series in more detail in Section [9.1](stationarity.html#stationarity).

The `feat_acf()` function computes a selection of the autocorrelations discussed here. It will return six or seven features:

  * the first autocorrelation coefficient from the original data;
  * the sum of squares of the first ten autocorrelation coefficients from the original data;
  * the first autocorrelation coefficient from the differenced data;
  * the sum of squares of the first ten autocorrelation coefficients from the differenced data;
  * the first autocorrelation coefficient from the twice differenced data;
  * the sum of squares of the first ten autocorrelation coefficients from the twice differenced data;
  * For seasonal data, the autocorrelation coefficient at the first seasonal lag is also returned.


When applied to the Australian tourism data, we get the following output.
    
    
    [](acf-features.html#cb67-1)tourism |> features(Trips, feat_acf)
    [](acf-features.html#cb67-2)#> # A tibble: 304 × 10
    [](acf-features.html#cb67-3)#>    Region       State Purpose     acf1 acf10 diff1_acf1 diff1_acf10 diff2_acf1
    [](acf-features.html#cb67-4)#>    <chr>        <chr> <chr>      <dbl> <dbl>      <dbl>       <dbl>      <dbl>
    [](acf-features.html#cb67-5)#>  1 Adelaide     Sout… Busine…  0.0333  0.131     -0.520       0.463     -0.676
    [](acf-features.html#cb67-6)#>  2 Adelaide     Sout… Holiday  0.0456  0.372     -0.343       0.614     -0.487
    [](acf-features.html#cb67-7)#>  3 Adelaide     Sout… Other    0.517   1.15      -0.409       0.383     -0.675
    [](acf-features.html#cb67-8)#>  4 Adelaide     Sout… Visiti…  0.0684  0.294     -0.394       0.452     -0.518
    [](acf-features.html#cb67-9)#>  5 Adelaide Hi… Sout… Busine…  0.0709  0.134     -0.580       0.415     -0.750
    [](acf-features.html#cb67-10)#>  6 Adelaide Hi… Sout… Holiday  0.131   0.313     -0.536       0.500     -0.716
    [](acf-features.html#cb67-11)#>  7 Adelaide Hi… Sout… Other    0.261   0.330     -0.253       0.317     -0.457
    [](acf-features.html#cb67-12)#>  8 Adelaide Hi… Sout… Visiti…  0.139   0.117     -0.472       0.239     -0.626
    [](acf-features.html#cb67-13)#>  9 Alice Sprin… Nort… Busine…  0.217   0.367     -0.500       0.381     -0.658
    [](acf-features.html#cb67-14)#> 10 Alice Sprin… Nort… Holiday -0.00660 2.11      -0.153       2.11      -0.274
    [](acf-features.html#cb67-15)#> # ℹ 294 more rows
    [](acf-features.html#cb67-16)#> # ℹ 2 more variables: diff2_acf10 <dbl>, season_acf1 <dbl>


---

## 4.3 STL Features[](stlfeatures.html#stlfeatures)

The STL decomposition discussed in Chapter [3](decomposition.html#decomposition) is the basis for several more features.

A time series decomposition can be used to measure the strength of trend and seasonality in a time series. Recall that the decomposition is written as \\[ y_t = T_t + S_{t} + R_t, \\] where \\(T_t\\) is the smoothed trend component, \\(S_{t}\\) is the seasonal component and \\(R_t\\) is a remainder component. For strongly trended data, the seasonally adjusted data should have much more variation than the remainder component. Therefore Var\\((R_t)\\)/Var\\((T_t+R_t)\\) should be relatively small. But for data with little or no trend, the two variances should be approximately the same. So we define the strength of trend as: \\[ F_T = \max\left(0, 1 - \frac{\text{Var}(R_t)}{\text{Var}(T_t+R_t)}\right). \\] This will give a measure of the strength of the trend between 0 and 1. Because the variance of the remainder might occasionally be even larger than the variance of the seasonally adjusted data, we set the minimal possible value of \\(F_T\\) equal to zero.

The strength of seasonality is defined similarly, but with respect to the detrended data rather than the seasonally adjusted data: \\[ F_S = \max\left(0, 1 - \frac{\text{Var}(R_t)}{\text{Var}(S_{t}+R_t)}\right). \\] A series with seasonal strength \\(F_S\\) close to 0 exhibits almost no seasonality, while a series with strong seasonality will have \\(F_S\\) close to 1 because Var\\((R_t)\\) will be much smaller than Var\\((S_{t}+R_t)\\).

These measures can be useful, for example, when you have a large collection of time series, and you need to find the series with the most trend or the most seasonality. These and other STL-based features are computed using the `feat_stl()` function.
    
    
    [](stlfeatures.html#cb68-1)tourism |>
    [](stlfeatures.html#cb68-2)  features(Trips, feat_stl)
    [](stlfeatures.html#cb68-3)#> # A tibble: 304 × 12
    [](stlfeatures.html#cb68-4)#>    Region         State          Purpose trend_strength seasonal_strength_year
    [](stlfeatures.html#cb68-5)#>    <chr>          <chr>          <chr>            <dbl>                  <dbl>
    [](stlfeatures.html#cb68-6)#>  1 Adelaide       South Austral… Busine…          0.464                  0.407
    [](stlfeatures.html#cb68-7)#>  2 Adelaide       South Austral… Holiday          0.554                  0.619
    [](stlfeatures.html#cb68-8)#>  3 Adelaide       South Austral… Other            0.746                  0.202
    [](stlfeatures.html#cb68-9)#>  4 Adelaide       South Austral… Visiti…          0.435                  0.452
    [](stlfeatures.html#cb68-10)#>  5 Adelaide Hills South Austral… Busine…          0.464                  0.179
    [](stlfeatures.html#cb68-11)#>  6 Adelaide Hills South Austral… Holiday          0.528                  0.296
    [](stlfeatures.html#cb68-12)#>  7 Adelaide Hills South Austral… Other            0.593                  0.404
    [](stlfeatures.html#cb68-13)#>  8 Adelaide Hills South Austral… Visiti…          0.488                  0.254
    [](stlfeatures.html#cb68-14)#>  9 Alice Springs  Northern Terr… Busine…          0.534                  0.251
    [](stlfeatures.html#cb68-15)#> 10 Alice Springs  Northern Terr… Holiday          0.381                  0.832
    [](stlfeatures.html#cb68-16)#> # ℹ 294 more rows
    [](stlfeatures.html#cb68-17)#> # ℹ 7 more variables: seasonal_peak_year <dbl>, seasonal_trough_year <dbl>,
    [](stlfeatures.html#cb68-18)#> #   spikiness <dbl>, linearity <dbl>, curvature <dbl>, stl_e_acf1 <dbl>,
    [](stlfeatures.html#cb68-19)#> #   stl_e_acf10 <dbl>

We can then use these features in plots to identify what type of series are heavily trended and what are most seasonal.
    
    
    [](stlfeatures.html#cb69-1)tourism |>
    [](stlfeatures.html#cb69-2)  features(Trips, feat_stl) |>
    [](stlfeatures.html#cb69-3)  ggplot(aes(x = trend_strength, y = seasonal_strength_year,
    [](stlfeatures.html#cb69-4)             col = Purpose)) +
    [](stlfeatures.html#cb69-5)  geom_point() +
    [](stlfeatures.html#cb69-6)  facet_wrap(vars(State))

Figure 4.1: Seasonal strength vs trend strength for all tourism series. 

Clearly, holiday series are most seasonal which is unsurprising. The strongest trends tend to be in Western Australia and Victoria. The most seasonal series can also be easily identified and plotted.
    
    
    [](stlfeatures.html#cb70-1)tourism |>
    [](stlfeatures.html#cb70-2)  features(Trips, feat_stl) |>
    [](stlfeatures.html#cb70-3)  filter(
    [](stlfeatures.html#cb70-4)    seasonal_strength_year == max(seasonal_strength_year)
    [](stlfeatures.html#cb70-5)  ) |>
    [](stlfeatures.html#cb70-6)  left_join(tourism, by = c("State", "Region", "Purpose"), multiple = "all") |>
    [](stlfeatures.html#cb70-7)  ggplot(aes(x = Quarter, y = Trips)) +
    [](stlfeatures.html#cb70-8)  geom_line() +
    [](stlfeatures.html#cb70-9)  facet_grid(vars(State, Region, Purpose))

Figure 4.2: The most seasonal series in the Australian tourism data. 

This shows holiday trips to the most popular ski region of Australia.

The `feat_stl()` function returns several more features other than those discussed above.

  * `seasonal_peak_year` indicates the timing of the peaks — which month or quarter contains the largest seasonal component. This tells us something about the nature of the seasonality. In the Australian tourism data, if Quarter 3 is the peak seasonal period, then people are travelling to the region in winter, whereas a peak in Quarter 1 suggests that the region is more popular in summer.
  * `seasonal_trough_year` indicates the timing of the troughs — which month or quarter contains the smallest seasonal component.
  * `spikiness` measures the prevalence of spikes in the remainder component \\(R_t\\) of the STL decomposition. It is the variance of the leave-one-out variances of \\(R_t\\).
  * `linearity` measures the linearity of the trend component of the STL decomposition. It is based on the coefficient of a linear regression applied to the trend component.
  * `curvature` measures the curvature of the trend component of the STL decomposition. It is based on the coefficient from an orthogonal quadratic regression applied to the trend component.
  * `stl_e_acf1` is the first autocorrelation coefficient of the remainder series.
  * `stl_e_acf10` is the sum of squares of the first ten autocorrelation coefficients of the remainder series.




---

## 4.4 Other features[](other-features.html#other-features)

Many more features are possible, and the `feasts` package computes only a few dozen features that have proven useful in time series analysis. It is also easy to add your own features by writing an R function that takes a univariate time series input and returns a numerical vector containing the feature values.

The remaining features in the `feasts` package, not previously discussed, are listed here for reference. The details of some of them are discussed later in the book.

  * `coef_hurst` will calculate the Hurst coefficient of a time series which is a measure of “long memory”. A series with long memory will have significant autocorrelations for many lags.
  * `feat_spectral` will compute the (Shannon) spectral entropy of a time series, which is a measure of how easy the series is to forecast. A series which has strong trend and seasonality (and so is easy to forecast) will have entropy close to 0. A series that is very noisy (and so is difficult to forecast) will have entropy close to 1.
  * `box_pierce` gives the Box-Pierce statistic for testing if a time series is white noise, and the corresponding p-value. This test is discussed in Section [5.4](diagnostics.html#diagnostics).
  * `ljung_box` gives the Ljung-Box statistic for testing if a time series is white noise, and the corresponding p-value. This test is discussed in Section [5.4](diagnostics.html#diagnostics).
  * The \\(k\\)th partial autocorrelation measures the relationship between observations \\(k\\) periods apart after removing the effects of observations between them. So the first partial autocorrelation (\\(k=1\\)) is identical to the first autocorrelation, because there is nothing between consecutive observations to remove. Partial autocorrelations are discussed in Section [9.5](non-seasonal-arima.html#non-seasonal-arima). The `feat_pacf` function contains several features involving partial autocorrelations including the sum of squares of the first five partial autocorrelations for the original series, the first-differenced series and the second-differenced series. For seasonal data, it also includes the partial autocorrelation at the first seasonal lag.
  * `unitroot_kpss` gives the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) statistic for testing if a series is stationary, and the corresponding p-value. This test is discussed in Section [9.1](stationarity.html#stationarity).
  * `unitroot_pp` gives the Phillips-Perron statistic for testing if a series is non-stationary, and the corresponding p-value.
  * `unitroot_ndiffs` gives the number of differences required to lead to a stationary series based on the KPSS test. This is discussed in Section [9.1](stationarity.html#stationarity)
  * `unitroot_nsdiffs` gives the number of seasonal differences required to make a series stationary. This is discussed in Section [9.1](stationarity.html#stationarity).
  * `var_tiled_mean` gives the variances of the “tiled means” (i.e., the means of consecutive non-overlapping blocks of observations). The default tile length is either 10 (for non-seasonal data) or the length of the seasonal period. This is sometimes called the “stability” feature.
  * `var_tiled_var` gives the variances of the “tiled variances” (i.e., the variances of consecutive non-overlapping blocks of observations). This is sometimes called the “lumpiness” feature.
  * `shift_level_max` finds the largest mean shift between two consecutive sliding windows of the time series. This is useful for finding sudden jumps or drops in a time series.
  * `shift_level_index` gives the index at which the largest mean shift occurs.
  * `shift_var_max` finds the largest variance shift between two consecutive sliding windows of the time series. This is useful for finding sudden changes in the volatility of a time series.
  * `shift_var_index` gives the index at which the largest variance shift occurs.
  * `shift_kl_max` finds the largest distributional shift (based on the Kulback-Leibler divergence) between two consecutive sliding windows of the time series. This is useful for finding sudden changes in the distribution of a time series.
  * `shift_kl_index` gives the index at which the largest KL shift occurs.
  * `n_crossing_points` computes the number of times a time series crosses the median.
  * `longest_flat_spot` computes the number of sections of the data where the series is relatively unchanging.
  * `stat_arch_lm` returns the statistic based on the Lagrange Multiplier (LM) test of Engle (1982) for autoregressive conditional heteroscedasticity (ARCH).
  * `guerrero` computes the optimal \\(\lambda\\) value for a Box-Cox transformation using the Guerrero method (discussed in Section [3.1](transformations.html#transformations)).




---

## 4.5 Exploring Australian tourism data[](exploring-australian-tourism-data.html#exploring-australian-tourism-data)

All of the features included in the `feasts` package can be computed in one line like this.
    
    
    [](exploring-australian-tourism-data.html#cb71-1)tourism_features <- tourism |>
    [](exploring-australian-tourism-data.html#cb71-2)  features(Trips, feature_set(pkgs = "feasts"))
    [](exploring-australian-tourism-data.html#cb71-3)tourism_features
    [](exploring-australian-tourism-data.html#cb71-4)#> # A tibble: 304 × 51
    [](exploring-australian-tourism-data.html#cb71-5)#>    Region         State          Purpose trend_strength seasonal_strength_year
    [](exploring-australian-tourism-data.html#cb71-6)#>    <chr>          <chr>          <chr>            <dbl>                  <dbl>
    [](exploring-australian-tourism-data.html#cb71-7)#>  1 Adelaide       South Austral… Busine…          0.464                  0.407
    [](exploring-australian-tourism-data.html#cb71-8)#>  2 Adelaide       South Austral… Holiday          0.554                  0.619
    [](exploring-australian-tourism-data.html#cb71-9)#>  3 Adelaide       South Austral… Other            0.746                  0.202
    [](exploring-australian-tourism-data.html#cb71-10)#>  4 Adelaide       South Austral… Visiti…          0.435                  0.452
    [](exploring-australian-tourism-data.html#cb71-11)#>  5 Adelaide Hills South Austral… Busine…          0.464                  0.179
    [](exploring-australian-tourism-data.html#cb71-12)#>  6 Adelaide Hills South Austral… Holiday          0.528                  0.296
    [](exploring-australian-tourism-data.html#cb71-13)#>  7 Adelaide Hills South Austral… Other            0.593                  0.404
    [](exploring-australian-tourism-data.html#cb71-14)#>  8 Adelaide Hills South Austral… Visiti…          0.488                  0.254
    [](exploring-australian-tourism-data.html#cb71-15)#>  9 Alice Springs  Northern Terr… Busine…          0.534                  0.251
    [](exploring-australian-tourism-data.html#cb71-16)#> 10 Alice Springs  Northern Terr… Holiday          0.381                  0.832
    [](exploring-australian-tourism-data.html#cb71-17)#> # ℹ 294 more rows
    [](exploring-australian-tourism-data.html#cb71-18)#> # ℹ 46 more variables: seasonal_peak_year <dbl>, seasonal_trough_year <dbl>,
    [](exploring-australian-tourism-data.html#cb71-19)#> #   spikiness <dbl>, linearity <dbl>, curvature <dbl>, stl_e_acf1 <dbl>,
    [](exploring-australian-tourism-data.html#cb71-20)#> #   stl_e_acf10 <dbl>, acf1 <dbl>, acf10 <dbl>, diff1_acf1 <dbl>,
    [](exploring-australian-tourism-data.html#cb71-21)#> #   diff1_acf10 <dbl>, diff2_acf1 <dbl>, diff2_acf10 <dbl>,
    [](exploring-australian-tourism-data.html#cb71-22)#> #   season_acf1 <dbl>, pacf5 <dbl>, diff1_pacf5 <dbl>, diff2_pacf5 <dbl>,
    [](exploring-australian-tourism-data.html#cb71-23)#> #   season_pacf <dbl>, zero_run_mean <dbl>, nonzero_squared_cv <dbl>, …

Provided the `urca` and `fracdiff` packages are installed, this gives 48 features for every combination of the three key variables (`Region`, `State` and `Purpose`). We can treat this tibble like any data set and analyse it to find interesting observations or groups of observations.

We’ve already seen how we can plot one feature against another (Section [4.3](stlfeatures.html#stlfeatures)). We can also do pairwise plots of groups of features. In Figure [4.3](exploring-australian-tourism-data.html#fig:seasonalfeatures), for example, we show all features that involve seasonality, along with the `Purpose` variable.
    
    
    [](exploring-australian-tourism-data.html#cb72-1)library(glue)
    [](exploring-australian-tourism-data.html#cb72-2)tourism_features |>
    [](exploring-australian-tourism-data.html#cb72-3)  select_at(vars(contains("season"), Purpose)) |>
    [](exploring-australian-tourism-data.html#cb72-4)  mutate(
    [](exploring-australian-tourism-data.html#cb72-5)    seasonal_peak_year = seasonal_peak_year +
    [](exploring-australian-tourism-data.html#cb72-6)      4*(seasonal_peak_year==0),
    [](exploring-australian-tourism-data.html#cb72-7)    seasonal_trough_year = seasonal_trough_year +
    [](exploring-australian-tourism-data.html#cb72-8)      4*(seasonal_trough_year==0),
    [](exploring-australian-tourism-data.html#cb72-9)    seasonal_peak_year = glue("Q{seasonal_peak_year}"),
    [](exploring-australian-tourism-data.html#cb72-10)    seasonal_trough_year = glue("Q{seasonal_trough_year}"),
    [](exploring-australian-tourism-data.html#cb72-11)  ) |>
    [](exploring-australian-tourism-data.html#cb72-12)  GGally::ggpairs(mapping = aes(colour = Purpose))

Figure 4.3: Pairwise plots of all the seasonal features for the Australian tourism data 

Here, the `Purpose` variable is mapped to colour. There is a lot of information in this figure, and we will highlight just a few things we can learn.

  * The three numerical measures related to seasonality (`seasonal_strength_year`, `season_acf1` and `season_pacf`) are all positively correlated.
  * The bottom left panel and the top right panel both show that the most strongly seasonal series are related to holidays (as we saw previously).
  * The bar plots in the bottom row of the `seasonal_peak_year` and `seasonal_trough_year` columns show that seasonal peaks in Business travel occur most often in Quarter 3, and least often in Quarter 1.


It is difficult to explore more than a handful of variables in this way. A useful way to handle many more variables is to use a dimension reduction technique such as principal components. This gives linear combinations of variables that explain the most variation in the original data. We can compute the principal components of the tourism features as follows.
    
    
    [](exploring-australian-tourism-data.html#cb73-1)library(broom)
    [](exploring-australian-tourism-data.html#cb73-2)pcs <- tourism_features |>
    [](exploring-australian-tourism-data.html#cb73-3)  select(-State, -Region, -Purpose) |>
    [](exploring-australian-tourism-data.html#cb73-4)  prcomp(scale = TRUE) |>
    [](exploring-australian-tourism-data.html#cb73-5)  augment(tourism_features)
    [](exploring-australian-tourism-data.html#cb73-6)pcs |>
    [](exploring-australian-tourism-data.html#cb73-7)  ggplot(aes(x = .fittedPC1, y = .fittedPC2, col = Purpose)) +
    [](exploring-australian-tourism-data.html#cb73-8)  geom_point() +
    [](exploring-australian-tourism-data.html#cb73-9)  theme(aspect.ratio = 1)

Figure 4.4: A plot of the first two principal components, calculated from the 48 features of the Australian quarterly tourism data. 

Each point on Figure [4.4](exploring-australian-tourism-data.html#fig:pca) represents one series and its location on the plot is based on all 48 features. The first principal component (`.fittedPC1`) is the linear combination of the features which explains the most variation in the data. The second principal component (`.fittedPC2`) is the linear combination which explains the next most variation in the data, while being uncorrelated with the first principal component. For more information about principal component dimension reduction, see Izenman ([2008](exploring-australian-tourism-data.html#ref-izenman2008)).

Figure [4.4](exploring-australian-tourism-data.html#fig:pca) reveals a few things about the tourism data. First, the holiday series behave quite differently from the rest of the series. Almost all of the holiday series appear in the top half of the plot, while almost all of the remaining series appear in the bottom half of the plot. Clearly, the second principal component is distinguishing between holidays and other types of travel.

The plot also allows us to identify anomalous time series — series which have unusual feature combinations. These appear as points that are separate from the majority of series in Figure [4.4](exploring-australian-tourism-data.html#fig:pca). There are four that stand out, and we can identify which series they correspond to as follows.
    
    
    [](exploring-australian-tourism-data.html#cb74-1)outliers <- pcs |>
    [](exploring-australian-tourism-data.html#cb74-2)  filter(.fittedPC1 > 10) |>
    [](exploring-australian-tourism-data.html#cb74-3)  select(Region, State, Purpose, .fittedPC1, .fittedPC2)
    [](exploring-australian-tourism-data.html#cb74-4)outliers
    [](exploring-australian-tourism-data.html#cb74-5)#> # A tibble: 4 × 5
    [](exploring-australian-tourism-data.html#cb74-6)#>   Region                 State             Purpose  .fittedPC1 .fittedPC2
    [](exploring-australian-tourism-data.html#cb74-7)#>   <chr>                  <chr>             <chr>         <dbl>      <dbl>
    [](exploring-australian-tourism-data.html#cb74-8)#> 1 Australia's North West Western Australia Business       13.4    -11.3  
    [](exploring-australian-tourism-data.html#cb74-9)#> 2 Australia's South West Western Australia Holiday        10.9      0.880
    [](exploring-australian-tourism-data.html#cb74-10)#> 3 Melbourne              Victoria          Holiday        12.3    -10.4  
    [](exploring-australian-tourism-data.html#cb74-11)#> 4 South Coast            New South Wales   Holiday        11.9      9.42
    [](exploring-australian-tourism-data.html#cb74-12)outliers |>
    [](exploring-australian-tourism-data.html#cb74-13)  left_join(tourism, by = c("State", "Region", "Purpose"), multiple = "all") |>
    [](exploring-australian-tourism-data.html#cb74-14)  mutate(Series = glue("{State}", "{Region}", "{Purpose}", .sep = "\n\n")) |>
    [](exploring-australian-tourism-data.html#cb74-15)  ggplot(aes(x = Quarter, y = Trips)) +
    [](exploring-australian-tourism-data.html#cb74-16)  geom_line() +
    [](exploring-australian-tourism-data.html#cb74-17)  facet_grid(Series ~ ., scales = "free") +
    [](exploring-australian-tourism-data.html#cb74-18)  labs(title = "Outlying time series in PC space")

Figure 4.5: Four anomalous time series from the Australian tourism data. 

We can speculate why these series are identified as unusual.

  * Holiday visits to the south coast of NSW is highly seasonal but has almost no trend, whereas most holiday destinations in Australia show some trend over time.
  * Melbourne is an unusual holiday destination because it has almost no seasonality, whereas most holiday destinations in Australia have highly seasonal tourism.
  * The north western corner of Western Australia is unusual because it shows an increase in business tourism in the last few years of data, but little or no seasonality.
  * The south western corner of Western Australia is unusual because it shows both an increase in holiday tourism in the last few years of data and a high level of seasonality.


### Bibliography[](bibliography.html#bibliography)

Izenman, A. J. (2008). _Modern multivariate statistical techniques: Regression, classification and manifold learning_. Springer. [__](http://amazon.com/dp/0387781889?tag=otexts20)


---

## 4.6 Exercises[](feast-exercises.html#feast-exercises)

  1. Write a function to compute the mean and standard deviation of a time series, and apply it to the `PBS` data. Plot the series with the highest mean, and the series with the lowest standard deviation.

  2. Use `GGally::ggpairs()` to look at the relationships between the STL-based features for the holiday series in the `tourism` data. Change `seasonal_peak_year` and `seasonal_trough_year` to factors, as shown in Figure [4.3](exploring-australian-tourism-data.html#fig:seasonalfeatures). Which is the peak quarter for holidays in each state?

  3. Use a feature-based approach to look for outlying series in the `PBS` data. What is unusual about the series you identify as “outliers”.




---

## 4.7 Further reading[](further-reading.html#further-reading)

  * The idea of using STL for features originated with Wang et al. ([2006](further-reading.html#ref-WangSH06)).
  * The features provided by the `feasts` package were motivated by their use in Hyndman et al. ([2015](further-reading.html#ref-cikm2015)) and Kang et al. ([2017](further-reading.html#ref-m3pca)).
  * The exploration of a set of time series using principal components on a large collection of features was proposed by Kang et al. ([2017](further-reading.html#ref-m3pca)).


### Bibliography[](bibliography.html#bibliography)

Hyndman, R. J., Wang, E., & Laptev, N. (2015). Large-scale unusual time series detection. _Proceedings of the IEEE International Conference on Data Mining_ , 1616–1619. [__](https://doi.org/10.1109/ICDMW.2015.104)

Kang, Y., Hyndman, R. J., & Smith-Miles, K. (2017). Visualising forecasting algorithm performance using time series instance spaces. _International Journal of Forecasting_ , _33_(2), 345–358. [__](https://doi.org/10.1016/j.ijforecast.2016.09.004)

Wang, X., Smith, K. A., & Hyndman, R. J. (2006). Characteristic-based clustering for time series data. _Data Mining and Knowledge Discovery_ , _13_(3), 335–364. [__](https://doi.org/10.1007/s10618-005-0039-x)


---

# Chapter 5 The forecaster’s toolbox[](toolbox.html#toolbox)

In this chapter, we discuss some general tools that are useful for many different forecasting situations. We will describe some benchmark forecasting methods, procedures for checking whether a forecasting method has adequately utilised the available information, techniques for computing prediction intervals, and methods for evaluating forecast accuracy.

Each of the tools discussed in this chapter will be used repeatedly in subsequent chapters as we develop and explore a range of forecasting methods.


---

## 5.1 A tidy forecasting workflow[](a-tidy-forecasting-workflow.html#a-tidy-forecasting-workflow)

The process of producing forecasts for time series data can be broken down into a few steps.

To illustrate the process, we will fit linear trend models to national GDP data stored in `global_economy`.

### Data preparation (tidy)[](a-tidy-forecasting-workflow.html#data-preparation-tidy)

The first step in forecasting is to prepare data in the correct format. This process may involve loading in data, identifying missing values, filtering the time series, and other pre-processing tasks. The functionality provided by `tsibble` and other packages in the `tidyverse` substantially simplifies this step.

Many models have different data requirements; some require the series to be in time order, others require no missing values. Checking your data is an essential step to understanding its features and should always be done before models are estimated.

We will model GDP per capita over time; so first, we must compute the relevant variable.
    
    
    [](a-tidy-forecasting-workflow.html#cb75-1)gdppc <- global_economy |>
    [](a-tidy-forecasting-workflow.html#cb75-2)  mutate(GDP_per_capita = GDP / Population)

### Plot the data (visualise)[](a-tidy-forecasting-workflow.html#plot-the-data-visualise)

As we have seen in Chapter [2](graphics.html#graphics), visualisation is an essential step in understanding the data. Looking at your data allows you to identify common patterns, and subsequently specify an appropriate model.

The data for one country in our example are plotted in Figure [5.1](a-tidy-forecasting-workflow.html#fig:swedengdp).
    
    
    [](a-tidy-forecasting-workflow.html#cb76-1)gdppc |>
    [](a-tidy-forecasting-workflow.html#cb76-2)  filter(Country == "Sweden") |>
    [](a-tidy-forecasting-workflow.html#cb76-3)  autoplot(GDP_per_capita) +
    [](a-tidy-forecasting-workflow.html#cb76-4)  labs(y = "$US", title = "GDP per capita for Sweden")

Figure 5.1: GDP per capita data for Sweden from 1960 to 2017. 

### Define a model (specify)[](a-tidy-forecasting-workflow.html#define-a-model-specify)

There are many different time series models that can be used for forecasting, and much of this book is dedicated to describing various models. Specifying an appropriate model for the data is essential for producing appropriate forecasts.

Models in `fable` are specified using model functions, which each use a formula (`y ~ x`) interface. The response variable(s) are specified on the left of the formula, and the structure of the model is written on the right.

For example, a linear trend model (to be discussed in Chapter [7](regression.html#regression)) for GDP per capita can be specified with
    
    
    [](a-tidy-forecasting-workflow.html#cb77-1)TSLM(GDP_per_capita ~ trend()).

In this case the model function is `TSLM()` (time series linear model), the response variable is `GDP_per_capita` and it is being modelled using `trend()` (a “special” function specifying a linear trend when it is used within `TSLM()`). We will be taking a closer look at how each model can be specified in their respective sections.

The special functions used to define the model’s structure vary between models (as each model can support different structures). The “Specials” section of the documentation for each model function lists these special functions and how they can be used.

The left side of the formula also supports the transformations discussed in Section [3.1](transformations.html#transformations), which can be useful in simplifying the time series patterns or constraining the forecasts to be between specific values (see Section [13.3](limits.html#limits)).

### Train the model (estimate)[](a-tidy-forecasting-workflow.html#train-the-model-estimate)

Once an appropriate model is specified, we next train the model on some data. One or more model specifications can be estimated using the `model()` function.

To estimate the model in our example, we use
    
    
    [](a-tidy-forecasting-workflow.html#cb78-1)fit <- gdppc |>
    [](a-tidy-forecasting-workflow.html#cb78-2)  model(trend_model = TSLM(GDP_per_capita ~ trend()))

This fits a linear trend model to the GDP per capita data for each combination of key variables in the tsibble. In this example, it will fit a model to each of the 263 countries in the dataset. The resulting object is a model table or a “mable”.
    
    
    [](a-tidy-forecasting-workflow.html#cb79-1)fit
    [](a-tidy-forecasting-workflow.html#cb79-2)#> # A mable: 263 x 2
    [](a-tidy-forecasting-workflow.html#cb79-3)#> # Key:     Country [263]
    [](a-tidy-forecasting-workflow.html#cb79-4)#>    Country             trend_model
    [](a-tidy-forecasting-workflow.html#cb79-5)#>    <fct>                   <model>
    [](a-tidy-forecasting-workflow.html#cb79-6)#>  1 Afghanistan              <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-7)#>  2 Albania                  <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-8)#>  3 Algeria                  <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-9)#>  4 American Samoa           <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-10)#>  5 Andorra                  <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-11)#>  6 Angola                   <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-12)#>  7 Antigua and Barbuda      <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-13)#>  8 Arab World               <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-14)#>  9 Argentina                <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-15)#> 10 Armenia                  <TSLM>
    [](a-tidy-forecasting-workflow.html#cb79-16)#> # ℹ 253 more rows

Each row corresponds to one combination of the key variables. The `trend_model` column contains information about the fitted model for each country. In later chapters we will learn how to see more information about each model.

### Check model performance (evaluate)[](a-tidy-forecasting-workflow.html#check-model-performance-evaluate)

Once a model has been fitted, it is important to check how well it has performed on the data. There are several diagnostic tools available to check model behaviour, and also accuracy measures that allow one model to be compared against another. Sections [5.8](accuracy.html#accuracy) and [5.9](distaccuracy.html#distaccuracy) go into further details.

### Produce forecasts (forecast)[](a-tidy-forecasting-workflow.html#produce-forecasts-forecast)

With an appropriate model specified, estimated and checked, it is time to produce the forecasts using `forecast()`. The easiest way to use this function is by specifying the number of future observations to forecast. For example, forecasts for the next 10 observations can be generated using `h = 10`. We can also use natural language; e.g., `h = "2 years"` can be used to predict two years into the future.

In other situations, it may be more convenient to provide a dataset of future time periods to forecast. This is commonly required when your model uses additional information from the data, such as exogenous regressors. Additional data required by the model can be included in the dataset of observations to forecast.
    
    
    [](a-tidy-forecasting-workflow.html#cb80-1)fit |> forecast(h = "3 years")
    [](a-tidy-forecasting-workflow.html#cb80-2)#> # A fable: 789 x 5 [1Y]
    [](a-tidy-forecasting-workflow.html#cb80-3)#> # Key:     Country, .model [263]
    [](a-tidy-forecasting-workflow.html#cb80-4)#>    Country        .model       Year
    [](a-tidy-forecasting-workflow.html#cb80-5)#>    <fct>          <chr>       <dbl>
    [](a-tidy-forecasting-workflow.html#cb80-6)#>  1 Afghanistan    trend_model  2018
    [](a-tidy-forecasting-workflow.html#cb80-7)#>  2 Afghanistan    trend_model  2019
    [](a-tidy-forecasting-workflow.html#cb80-8)#>  3 Afghanistan    trend_model  2020
    [](a-tidy-forecasting-workflow.html#cb80-9)#>  4 Albania        trend_model  2018
    [](a-tidy-forecasting-workflow.html#cb80-10)#>  5 Albania        trend_model  2019
    [](a-tidy-forecasting-workflow.html#cb80-11)#>  6 Albania        trend_model  2020
    [](a-tidy-forecasting-workflow.html#cb80-12)#>  7 Algeria        trend_model  2018
    [](a-tidy-forecasting-workflow.html#cb80-13)#>  8 Algeria        trend_model  2019
    [](a-tidy-forecasting-workflow.html#cb80-14)#>  9 Algeria        trend_model  2020
    [](a-tidy-forecasting-workflow.html#cb80-15)#> 10 American Samoa trend_model  2018
    [](a-tidy-forecasting-workflow.html#cb80-16)#> # ℹ 779 more rows
    [](a-tidy-forecasting-workflow.html#cb80-17)#> # ℹ 2 more variables: GDP_per_capita <dist>, .mean <dbl>

This is a forecast table, or “fable”. Each row corresponds to one forecast period for each country. The `GDP_per_capita` column contains the forecast distribution, while the `.mean` column contains the point forecast. The point forecast is the mean (or average) of the forecast distribution.

The forecasts can be plotted along with the historical data using `autoplot()` as follows.
    
    
    [](a-tidy-forecasting-workflow.html#cb81-1)fit |>
    [](a-tidy-forecasting-workflow.html#cb81-2)  forecast(h = "3 years") |>
    [](a-tidy-forecasting-workflow.html#cb81-3)  filter(Country == "Sweden") |>
    [](a-tidy-forecasting-workflow.html#cb81-4)  autoplot(gdppc) +
    [](a-tidy-forecasting-workflow.html#cb81-5)  labs(y = "$US", title = "GDP per capita for Sweden")

Figure 5.2: Forecasts of GDP per capita for Sweden using a simple trend model. 


---

## 5.2 Some simple forecasting methods[](simple-methods.html#simple-methods)

Some forecasting methods are extremely simple and surprisingly effective. We will use four simple forecasting methods as benchmarks throughout this book. To illustrate them, we will use quarterly Australian clay brick production between 1970 and 2004.
    
    
    [](simple-methods.html#cb82-1)bricks <- aus_production |>
    [](simple-methods.html#cb82-2)  filter_index("1970 Q1" ~ "2004 Q4") |>
    [](simple-methods.html#cb82-3)  select(Bricks)

The `filter_index()` function is a convenient shorthand for extracting a section of a time series.

### Mean method[](simple-methods.html#mean-method)

Here, the forecasts of all future values are equal to the average (or “mean”) of the historical data. If we let the historical data be denoted by \\(y_{1},\dots,y_{T}\\), then we can write the forecasts as \\[ \hat{y}_{T+h|T} = \bar{y} = (y_{1}+\dots+y_{T})/T. \\] The notation \\(\hat{y}_{T+h|T}\\) is a short-hand for the estimate of \\(y_{T+h}\\) based on the data \\(y_1,\dots,y_T\\).
    
    
    [](simple-methods.html#cb83-1)bricks |> model(MEAN(Bricks))

Figure 5.3: Mean (or average) forecasts applied to clay brick production in Australia. 

### Naïve method[](simple-methods.html#na%C3%AFve-method)

For naïve forecasts, we simply set all forecasts to be the value of the last observation. That is, \\[ \hat{y}_{T+h|T} = y_{T}. \\] This method works remarkably well for many economic and financial time series.
    
    
    [](simple-methods.html#cb84-1)bricks |> model(NAIVE(Bricks))

Figure 5.4: Naïve forecasts applied to clay brick production in Australia. 

Because a naïve forecast is optimal when data follow a random walk (see Section [9.1](stationarity.html#stationarity)), these are also called **random walk forecasts** and the `RW()` function can be used instead of `NAIVE`.

### Seasonal naïve method[](simple-methods.html#seasonal-na%C3%AFve-method)

A similar method is useful for highly seasonal data. In this case, we set each forecast to be equal to the last observed value from the same season (e.g., the same month of the previous year). Formally, the forecast for time \\(T+h\\) is written as \\[ \hat{y}_{T+h|T} = y_{T+h-m(k+1)}, \\] where \\(m=\\) the seasonal period, and \\(k\\) is the integer part of \\((h-1)/m\\) (i.e., the number of complete years in the forecast period prior to time \\(T+h\\)). This looks more complicated than it really is. For example, with monthly data, the forecast for all future February values is equal to the last observed February value. With quarterly data, the forecast of all future Q2 values is equal to the last observed Q2 value (where Q2 means the second quarter). Similar rules apply for other months and quarters, and for other seasonal periods.
    
    
    [](simple-methods.html#cb85-1)bricks |> model(SNAIVE(Bricks ~ lag("year")))

The `lag()` function is optional here as `bricks` is quarterly data and so a seasonal naïve method will need a one-year lag. However, for some time series there is more than one seasonal period, and then the required lag must be specified.

Figure 5.5: Seasonal naïve forecasts applied to clay brick production in Australia. 

### Drift method[](simple-methods.html#drift-method)

A variation on the naïve method is to allow the forecasts to increase or decrease over time, where the amount of change over time (called the **drift**) is set to be the average change seen in the historical data. Thus the forecast for time \\(T+h\\) is given by \\[ \hat{y}_{T+h|T} = y_{T} + \frac{h}{T-1}\sum_{t=2}^T (y_{t}-y_{t-1}) = y_{T} + h \left( \frac{y_{T} -y_{1}}{T-1}\right). \\] This is equivalent to drawing a line between the first and last observations, and extrapolating it into the future.
    
    
    [](simple-methods.html#cb86-1)bricks |> model(RW(Bricks ~ drift()))

Figure 5.6: Drift forecasts applied to clay brick production in Australia. 

### Example: Australian quarterly beer production[](simple-methods.html#example-australian-quarterly-beer-production)

Figure [5.7](simple-methods.html#fig:beerf) shows the first three methods applied to Australian quarterly beer production from 1992 to 2006, with the forecasts compared against actual values in the next 3.5 years.
    
    
    [](simple-methods.html#cb87-1)# Set training data from 1992 to 2006
    [](simple-methods.html#cb87-2)train <- aus_production |>
    [](simple-methods.html#cb87-3)  filter_index("1992 Q1" ~ "2006 Q4")
    [](simple-methods.html#cb87-4)# Fit the models
    [](simple-methods.html#cb87-5)beer_fit <- train |>
    [](simple-methods.html#cb87-6)  model(
    [](simple-methods.html#cb87-7)    Mean = MEAN(Beer),
    [](simple-methods.html#cb87-8)    `Naïve` = NAIVE(Beer),
    [](simple-methods.html#cb87-9)    `Seasonal naïve` = SNAIVE(Beer)
    [](simple-methods.html#cb87-10)  )
    [](simple-methods.html#cb87-11)# Generate forecasts for 14 quarters
    [](simple-methods.html#cb87-12)beer_fc <- beer_fit |> forecast(h = 14)
    [](simple-methods.html#cb87-13)# Plot forecasts against actual values
    [](simple-methods.html#cb87-14)beer_fc |>
    [](simple-methods.html#cb87-15)  autoplot(train, level = NULL) +
    [](simple-methods.html#cb87-16)  autolayer(
    [](simple-methods.html#cb87-17)    filter_index(aus_production, "2007 Q1" ~ .),
    [](simple-methods.html#cb87-18)    colour = "black"
    [](simple-methods.html#cb87-19)  ) +
    [](simple-methods.html#cb87-20)  labs(
    [](simple-methods.html#cb87-21)    y = "Megalitres",
    [](simple-methods.html#cb87-22)    title = "Forecasts for quarterly beer production"
    [](simple-methods.html#cb87-23)  ) +
    [](simple-methods.html#cb87-24)  guides(colour = guide_legend(title = "Forecast"))

Figure 5.7: Forecasts of Australian quarterly beer production. 

In this case, only the seasonal naïve forecasts are close to the observed values from 2007 onwards.

### Example: Google’s daily closing stock price[](simple-methods.html#example-googles-daily-closing-stock-price)

In Figure [5.8](simple-methods.html#fig:google2015), the non-seasonal methods are applied to Google’s daily closing stock price in 2015, and used to forecast one month ahead. Because stock prices are not observed every day, we first set up a new time index based on the trading days rather than calendar days.
    
    
    [](simple-methods.html#cb88-1)# Re-index based on trading days
    [](simple-methods.html#cb88-2)google_stock <- gafa_stock |>
    [](simple-methods.html#cb88-3)  filter(Symbol == "GOOG", year(Date) >= 2015) |>
    [](simple-methods.html#cb88-4)  mutate(day = row_number()) |>
    [](simple-methods.html#cb88-5)  update_tsibble(index = day, regular = TRUE)
    [](simple-methods.html#cb88-6)# Filter the year of interest
    [](simple-methods.html#cb88-7)google_2015 <- google_stock |> filter(year(Date) == 2015)
    [](simple-methods.html#cb88-8)# Fit the models
    [](simple-methods.html#cb88-9)google_fit <- google_2015 |>
    [](simple-methods.html#cb88-10)  model(
    [](simple-methods.html#cb88-11)    Mean = MEAN(Close),
    [](simple-methods.html#cb88-12)    `Naïve` = NAIVE(Close),
    [](simple-methods.html#cb88-13)    Drift = NAIVE(Close ~ drift())
    [](simple-methods.html#cb88-14)  )
    [](simple-methods.html#cb88-15)# Produce forecasts for the trading days in January 2016
    [](simple-methods.html#cb88-16)google_jan_2016 <- google_stock |>
    [](simple-methods.html#cb88-17)  filter(yearmonth(Date) == yearmonth("2016 Jan"))
    [](simple-methods.html#cb88-18)google_fc <- google_fit |>
    [](simple-methods.html#cb88-19)  forecast(new_data = google_jan_2016)
    [](simple-methods.html#cb88-20)# Plot the forecasts
    [](simple-methods.html#cb88-21)google_fc |>
    [](simple-methods.html#cb88-22)  autoplot(google_2015, level = NULL) +
    [](simple-methods.html#cb88-23)  autolayer(google_jan_2016, Close, colour = "black") +
    [](simple-methods.html#cb88-24)  labs(y = "$US",
    [](simple-methods.html#cb88-25)       title = "Google daily closing stock prices",
    [](simple-methods.html#cb88-26)       subtitle = "(Jan 2015 - Jan 2016)") +
    [](simple-methods.html#cb88-27)  guides(colour = guide_legend(title = "Forecast"))

Figure 5.8: Forecasts based on Google’s daily closing stock price in 2015. 

Sometimes one of these simple methods will be the best forecasting method available; but in many cases, these methods will serve as benchmarks rather than the method of choice. That is, any forecasting methods we develop will be compared to these simple methods to ensure that the new method is better than these simple alternatives. If not, the new method is not worth considering.


---

## 5.3 Fitted values and residuals[](residuals.html#residuals)

### Fitted values[](residuals.html#fitted-values)

Each observation in a time series can be forecast using all previous observations. We call these **fitted values** and they are denoted by \\(\hat{y}_{t|t-1}\\), meaning the forecast of \\(y_t\\) based on observations \\(y_{1},\dots,y_{t-1}\\) . We use these so often, we sometimes drop part of the subscript and just write \\(\hat{y}_t\\) instead of \\(\hat{y}_{t|t-1}\\). Fitted values almost always involve one-step forecasts (but see Section [13.8](training-test.html#training-test)).

Actually, fitted values are often not true forecasts because any parameters involved in the forecasting method are estimated using all available observations in the time series, including future observations. For example, if we use the mean method, the fitted values are given by \\[ \hat{y}_t = \hat{c} \\] where \\(\hat{c}\\) is the average computed over all available observations, including those at times _after_ \\(t\\). Similarly, for the drift method, the drift parameter is estimated using all available observations. In this case, the fitted values are given by \\[ \hat{y}_t = y_{t-1} + \hat{c} \\] where \\(\hat{c} = (y_T-y_1)/(T-1)\\). In both cases, there is a parameter to be estimated from the data. The “hat” above the \\(c\\) reminds us that this is an estimate. When the estimate of \\(c\\) involves observations after time \\(t\\), the fitted values are not true forecasts. On the other hand, naïve or seasonal naïve forecasts do not involve any parameters, and so fitted values are true forecasts in such cases.

### Residuals[](residuals.html#residuals-1)

The “residuals” in a time series model are what is left over after fitting a model. The residuals are equal to the difference between the observations and the corresponding fitted values: \\[ e_{t} = y_{t}-\hat{y}_{t}. \\]

If a transformation has been used in the model, then it is often useful to look at residuals on the transformed scale. We call these “**innovation residuals** ”. For example, suppose we modelled the logarithms of the data, \\(w_t = \log(y_t)\\). Then the innovation residuals are given by \\(w_t - \hat{w}_t\\) whereas the regular residuals are given by \\(y_t - \hat{y}_t\\). (See Section [5.6](ftransformations.html#ftransformations) for how to use transformations when forecasting.) If no transformation has been used then the innovation residuals are identical to the regular residuals, and in such cases we will simply call them “residuals”.

The fitted values and residuals from a model can be obtained using the `augment()` function. In the beer production example in Section [5.2](simple-methods.html#simple-methods), we saved the fitted models as `beer_fit`. So we can simply apply `augment()` to this object to compute the fitted values and residuals for all models.
    
    
    [](residuals.html#cb89-1)augment(beer_fit)
    [](residuals.html#cb89-2)#> # A tsibble: 180 x 6 [1Q]
    [](residuals.html#cb89-3)#> # Key:       .model [3]
    [](residuals.html#cb89-4)#>    .model Quarter  Beer .fitted .resid .innov
    [](residuals.html#cb89-5)#>    <chr>    <qtr> <dbl>   <dbl>  <dbl>  <dbl>
    [](residuals.html#cb89-6)#>  1 Mean   1992 Q1   443    436.   6.55   6.55
    [](residuals.html#cb89-7)#>  2 Mean   1992 Q2   410    436. -26.4  -26.4 
    [](residuals.html#cb89-8)#>  3 Mean   1992 Q3   420    436. -16.4  -16.4 
    [](residuals.html#cb89-9)#>  4 Mean   1992 Q4   532    436.  95.6   95.6 
    [](residuals.html#cb89-10)#>  5 Mean   1993 Q1   433    436.  -3.45  -3.45
    [](residuals.html#cb89-11)#>  6 Mean   1993 Q2   421    436. -15.4  -15.4 
    [](residuals.html#cb89-12)#>  7 Mean   1993 Q3   410    436. -26.4  -26.4 
    [](residuals.html#cb89-13)#>  8 Mean   1993 Q4   512    436.  75.6   75.6 
    [](residuals.html#cb89-14)#>  9 Mean   1994 Q1   449    436.  12.6   12.6 
    [](residuals.html#cb89-15)#> 10 Mean   1994 Q2   381    436. -55.4  -55.4 
    [](residuals.html#cb89-16)#> # ℹ 170 more rows

There are three new columns added to the original data:

  * `.fitted` contains the fitted values;
  * `.resid` contains the residuals;
  * `.innov` contains the “innovation residuals” which, in this case, are identical to the regular residuals.


Residuals are useful in checking whether a model has adequately captured the information in the data. For this purpose, we use innovation residuals.

If patterns are observable in the innovation residuals, the model can probably be improved. We will look at some tools for exploring patterns in residuals in the next section.


---

## 5.4 Residual diagnostics[](diagnostics.html#diagnostics)

A good forecasting method will yield innovation residuals with the following properties:

  1. The innovation residuals are uncorrelated. If there are correlations between innovation residuals, then there is information left in the residuals which should be used in computing forecasts.
  2. The innovation residuals have zero mean. If they have a mean other than zero, then the forecasts are biased.


Any forecasting method that does not satisfy these properties can be improved. However, that does not mean that forecasting methods that satisfy these properties cannot be improved. It is possible to have several different forecasting methods for the same data set, all of which satisfy these properties. Checking these properties is important in order to see whether a method is using all of the available information, but it is not a good way to select a forecasting method.

If either of these properties is not satisfied, then the forecasting method can be modified to give better forecasts. Adjusting for bias is easy: if the residuals have mean \\(m\\), then simply add \\(m\\) to all forecasts and the bias problem is solved. Fixing the correlation problem is harder, and we will not address it until Chapter [10](dynamic.html#dynamic).

In addition to these essential properties, it is useful (but not necessary) for the residuals to also have the following two properties.

  3. The innovation residuals have constant variance. This is known as “homoscedasticity”.
  4. The innovation residuals are normally distributed.


These two properties make the calculation of prediction intervals easier (see Section [5.5](prediction-intervals.html#prediction-intervals) for an example). However, a forecasting method that does not satisfy these properties cannot necessarily be improved. Sometimes applying a Box-Cox transformation may assist with these properties, but otherwise there is usually little that you can do to ensure that your innovation residuals have constant variance and a normal distribution. Instead, an alternative approach to obtaining prediction intervals is necessary. We will show how to deal with non-normal innovation residuals in Section [5.5](prediction-intervals.html#prediction-intervals).

### Example: Forecasting Google daily closing stock prices[](diagnostics.html#example-forecasting-google-daily-closing-stock-prices)

We will continue with the Google daily closing stock price example from Section [5.2](simple-methods.html#simple-methods). For stock market prices and indexes, the best forecasting method is often the naïve method. That is, each forecast is simply equal to the last observed value, or \\(\hat{y}_{t} = y_{t-1}\\). Hence, the residuals are simply equal to the difference between consecutive observations: \\[ e_{t} = y_{t} - \hat{y}_{t} = y_{t} - y_{t-1}. \\]

The following graph shows the Google daily closing stock price for trading days during 2015. The large jump corresponds to 17 July 2015 when the price jumped 16% due to unexpectedly strong second quarter results. (The `google_2015` object was created in Section [5.2](simple-methods.html#simple-methods).)
    
    
    [](diagnostics.html#cb90-1)autoplot(google_2015, Close) +
    [](diagnostics.html#cb90-2)  labs(y = "$US",
    [](diagnostics.html#cb90-3)       title = "Google daily closing stock prices in 2015")

Figure 5.9: Daily Google stock prices in 2015. 

The residuals obtained from forecasting this series using the naïve method are shown in Figure [5.10](diagnostics.html#fig:GSPresid). The large positive residual is a result of the unexpected price jump in July.
    
    
    [](diagnostics.html#cb91-1)aug <- google_2015 |>
    [](diagnostics.html#cb91-2)  model(NAIVE(Close)) |>
    [](diagnostics.html#cb91-3)  augment()
    [](diagnostics.html#cb91-4)autoplot(aug, .innov) +
    [](diagnostics.html#cb91-5)  labs(y = "$US",
    [](diagnostics.html#cb91-6)       title = "Residuals from the naïve method")

Figure 5.10: Residuals from forecasting the Google stock price using the naïve method. 
    
    
    [](diagnostics.html#cb92-1)aug |>
    [](diagnostics.html#cb92-2)  ggplot(aes(x = .innov)) +
    [](diagnostics.html#cb92-3)  geom_histogram() +
    [](diagnostics.html#cb92-4)  labs(title = "Histogram of residuals")

Figure 5.11: Histogram of the residuals from the naïve method applied to the Google stock price. The right tail seems a little too long for a normal distribution. 
    
    
    [](diagnostics.html#cb93-1)aug |>
    [](diagnostics.html#cb93-2)  ACF(.innov) |>
    [](diagnostics.html#cb93-3)  autoplot() +
    [](diagnostics.html#cb93-4)  labs(title = "Residuals from the naïve method")

Figure 5.12: ACF of the residuals from the naïve method applied to the Google stock price. The lack of correlation suggesting the forecasts are good. 

These graphs show that the naïve method produces forecasts that appear to account for all available information. The mean of the residuals is close to zero and there is no significant correlation in the residuals series. The time plot of the residuals shows that the variation of the residuals stays much the same across the historical data, apart from the one outlier, and therefore the residual variance can be treated as constant. This can also be seen on the histogram of the residuals. The histogram suggests that the residuals may not be normal — the right tail seems a little too long, even when we ignore the outlier. Consequently, forecasts from this method will probably be quite good, but prediction intervals that are computed assuming a normal distribution may be inaccurate.

A convenient shortcut for producing these residual diagnostic graphs is the `gg_tsresiduals()` function, which will produce a time plot, ACF plot and histogram of the residuals.
    
    
    [](diagnostics.html#cb94-1)google_2015 |>
    [](diagnostics.html#cb94-2)  model(NAIVE(Close)) |>
    [](diagnostics.html#cb94-3)  gg_tsresiduals()

Figure 5.13: Residual diagnostic graphs for the naïve method applied to the Google stock price. 

### Portmanteau tests for autocorrelation[](diagnostics.html#portmanteau-tests-for-autocorrelation)

In addition to looking at the ACF plot, we can also do a more formal test for autocorrelation by considering a whole set of \\(r_k\\) values as a group, rather than treating each one separately.

Recall that \\(r_k\\) is the autocorrelation for lag \\(k\\). When we look at the ACF plot to see whether each spike is within the required limits, we are implicitly carrying out multiple hypothesis tests, each one with a small probability of giving a false positive. When enough of these tests are done, it is likely that at least one will give a false positive, and so we may conclude that the residuals have some remaining autocorrelation, when in fact they do not.

In order to overcome this problem, we test whether the first \\(\ell\\) autocorrelations are significantly different from what would be expected from a white noise process. A test for a group of autocorrelations is called a **portmanteau test** , from a French word describing a suitcase or coat rack carrying several items of clothing.

One such test is the **Box-Pierce test** , based on the following statistic \\[ Q = T \sum_{k=1}^\ell r_k^2, \\] where \\(\ell\\) is the maximum lag being considered and \\(T\\) is the number of observations. If each \\(r_k\\) is close to zero, then \\(Q\\) will be small. If some \\(r_k\\) values are large (positive or negative), then \\(Q\\) will be large. We suggest using \\(\ell=10\\) for non-seasonal data and \\(\ell=2m\\) for seasonal data, where \\(m\\) is the period of seasonality. However, the test is not good when \\(\ell\\) is large, so if these values are larger than \\(T/5\\), then use \\(\ell=T/5\\)

A related (and more accurate) test is the **Ljung-Box test** , based on \\[ Q^* = T(T+2) \sum_{k=1}^\ell (T-k)^{-1}r_k^2. \\]

Again, large values of \\(Q^*\\) suggest that the autocorrelations do not come from a white noise series.

How large is too large? If the autocorrelations did come from a white noise series, then both \\(Q\\) and \\(Q^*\\) would have a \\(\chi^2\\) distribution with \\(\ell\\) degrees of freedom.[4](diagnostics.html#fn4).

In the following code, `lag`\\(=\ell\\).
    
    
    [](diagnostics.html#cb95-1)aug |> features(.innov, box_pierce, lag = 10)
    [](diagnostics.html#cb95-2)#> # A tibble: 1 × 4
    [](diagnostics.html#cb95-3)#>   Symbol .model       bp_stat bp_pvalue
    [](diagnostics.html#cb95-4)#>   <chr>  <chr>          <dbl>     <dbl>
    [](diagnostics.html#cb95-5)#> 1 GOOG   NAIVE(Close)    7.74     0.654
    [](diagnostics.html#cb95-6)
    [](diagnostics.html#cb95-7)aug |> features(.innov, ljung_box, lag = 10)
    [](diagnostics.html#cb95-8)#> # A tibble: 1 × 4
    [](diagnostics.html#cb95-9)#>   Symbol .model       lb_stat lb_pvalue
    [](diagnostics.html#cb95-10)#>   <chr>  <chr>          <dbl>     <dbl>
    [](diagnostics.html#cb95-11)#> 1 GOOG   NAIVE(Close)    7.91     0.637

For both \\(Q\\) and \\(Q^*\\), the results are not significant (i.e., the \\(p\\)-values are relatively large). Thus, we can conclude that the residuals are not distinguishable from a white noise series.

An alternative simple approach that may be appropriate for forecasting the Google daily closing stock price is the drift method. The `tidy()` function shows the one estimated parameter, the drift coefficient, measuring the average daily change observed in the historical data.
    
    
    [](diagnostics.html#cb96-1)fit <- google_2015 |> model(RW(Close ~ drift()))
    [](diagnostics.html#cb96-2)tidy(fit)
    [](diagnostics.html#cb96-3)#> # A tibble: 1 × 7
    [](diagnostics.html#cb96-4)#>   Symbol .model              term  estimate std.error statistic p.value
    [](diagnostics.html#cb96-5)#>   <chr>  <chr>               <chr>    <dbl>     <dbl>     <dbl>   <dbl>
    [](diagnostics.html#cb96-6)#> 1 GOOG   RW(Close ~ drift()) b        0.944     0.705      1.34   0.182

Applying the Ljung-Box test, we obtain the following result.
    
    
    [](diagnostics.html#cb97-1)augment(fit) |> features(.innov, ljung_box, lag=10)
    [](diagnostics.html#cb97-2)#> # A tibble: 1 × 4
    [](diagnostics.html#cb97-3)#>   Symbol .model              lb_stat lb_pvalue
    [](diagnostics.html#cb97-4)#>   <chr>  <chr>                 <dbl>     <dbl>
    [](diagnostics.html#cb97-5)#> 1 GOOG   RW(Close ~ drift())    7.91     0.637

As with the naïve method, the residuals from the drift method are indistinguishable from a white noise series.

* * *

  4. For the ARIMA models discussed in chapters [9](arima.html#arima) and [10](dynamic.html#dynamic), the degrees of freedom is adjusted to give better results.[↩︎](diagnostics.html#fnref4)




---

## 5.5 Distributional forecasts and prediction intervals[](prediction-intervals.html#prediction-intervals)

### Forecast distributions[](prediction-intervals.html#forecast-distributions)

As discussed in Section [1.7](perspective.html#perspective), we express the uncertainty in our forecasts using a probability distribution. It describes the probability of observing possible future values using the fitted model. The point forecast is the mean of this distribution. Most time series models produce normally distributed forecasts — that is, we assume that the distribution of possible future values follows a normal distribution. We will look at a couple of alternatives to normal distributions later in this section.

### Prediction intervals[](prediction-intervals.html#prediction-intervals-1)

A prediction interval gives an interval within which we expect \\(y_{t}\\) to lie with a specified probability. For example, assuming that distribution of future observations is normal, a 95% prediction interval for the \\(h\\)-step forecast is \\[ \hat{y}_{T+h|T} \pm 1.96 \hat\sigma_h, \\] where \\(\hat\sigma_h\\) is an estimate of the standard deviation of the \\(h\\)-step forecast distribution.

More generally, a prediction interval can be written as \\[ \hat{y}_{T+h|T} \pm c \hat\sigma_h \\] where the multiplier \\(c\\) depends on the coverage probability. In this book we usually calculate 80% intervals and 95% intervals, although any percentage may be used. Table [5.1](prediction-intervals.html#tab:pcmultipliers) gives the value of \\(c\\) for a range of coverage probabilities assuming a normal forecast distribution.

Table 5.1: Multipliers to be used for prediction intervals. Percentage | Multiplier  
---|---  
50 | 0.67  
55 | 0.76  
60 | 0.84  
65 | 0.93  
70 | 1.04  
75 | 1.15  
80 | 1.28  
85 | 1.44  
90 | 1.64  
95 | 1.96  
96 | 2.05  
97 | 2.17  
98 | 2.33  
99 | 2.58  
  
The value of prediction intervals is that they express the uncertainty in the forecasts. If we only produce point forecasts, there is no way of telling how accurate the forecasts are. However, if we also produce prediction intervals, then it is clear how much uncertainty is associated with each forecast. For this reason, point forecasts can be of almost no value without the accompanying prediction intervals.

### One-step prediction intervals[](prediction-intervals.html#one-step-prediction-intervals)

When forecasting one step ahead, the standard deviation of the forecast distribution can be estimated using the standard deviation of the residuals given by \\[\begin{equation} \hat{\sigma} = \sqrt{\frac{1}{T-K-M}\sum_{t=1}^T e_t^2}, \tag{5.1} \end{equation}\\] where \\(K\\) is the number of parameters estimated in the forecasting method, and \\(M\\) is the number of missing values in the residuals. (For example, \\(M=1\\) for a naive forecast, because we can’t forecast the first observation.)

For example, consider a naïve forecast for the Google stock price data `google_2015` (shown in Figure [5.8](simple-methods.html#fig:google2015)). The last value of the observed series is 758.88, so the forecast of the next value of the price is 758.88. The standard deviation of the residuals from the naïve method, as given by Equation [(5.1)](prediction-intervals.html#eq:sigma1), is 11.19. Hence, a 95% prediction interval for the next value of the GSP is \\[ 758.88 \pm 1.96(11.19) = [736.9, 780.8]. \\] Similarly, an 80% prediction interval is given by \\[ 758.88 \pm 1.28(11.19) = [744.5, 773.2]. \\]

The value of the multiplier (1.96 or 1.28) is taken from Table [5.1](prediction-intervals.html#tab:pcmultipliers).

### Multi-step prediction intervals[](prediction-intervals.html#multi-step-prediction-intervals)

A common feature of prediction intervals is that they usually increase in length as the forecast horizon increases. The further ahead we forecast, the more uncertainty is associated with the forecast, and thus the wider the prediction intervals. That is, \\(\sigma_h\\) usually increases with \\(h\\) (although there are some non-linear forecasting methods which do not have this property).

To produce a prediction interval, it is necessary to have an estimate of \\(\sigma_h\\). As already noted, for one-step forecasts (\\(h=1\\)), Equation [(5.1)](prediction-intervals.html#eq:sigma1) provides a good estimate of the forecast standard deviation \\(\sigma_1\\). For multi-step forecasts, a more complicated method of calculation is required. These calculations assume that the residuals are uncorrelated.

### Benchmark methods[](prediction-intervals.html#benchmark-methods)

For the four benchmark methods, it is possible to mathematically derive the forecast standard deviation under the assumption of uncorrelated residuals. If \\(\hat{\sigma}_h\\) denotes the standard deviation of the \\(h\\)-step forecast distribution, and \\(\hat{\sigma}\\) is the residual standard deviation given by [(5.1)](prediction-intervals.html#eq:sigma1), then we can use the expressions shown in Table [5.2](prediction-intervals.html#tab:sigmatable). Note that when \\(h=1\\) and \\(T\\) is large, these all give the same approximate value \\(\hat\sigma\\).

Table 5.2: Multi-step forecast standard deviation for the four benchmark methods, where \\(\sigma\\) is the residual standard deviation, \\(m\\) is the seasonal period, and \\(k\\) is the integer part of \\((h-1) /m\\) (i.e., the number of complete years in the forecast period prior to time \\(T+h\\)).  Benchmark method  |  \\(h\\)-step forecast standard deviation   
---|---  
Mean  |  \\(\hat\sigma_h = \hat\sigma\sqrt{1 + 1/T}\\)  
Naïve  |  \\(\hat\sigma_h = \hat\sigma\sqrt{h}\\)  
Seasonal naïve  |  \\(\hat\sigma_h = \hat\sigma\sqrt{k+1}\\)  
Drift  |  \\(\hat\sigma_h = \hat\sigma\sqrt{h(1+h/(T-1))}\\)  
  
Prediction intervals can easily be computed for you when using the `fable` package. For example, here is the output when using the naïve method for the Google stock price.
    
    
    [](prediction-intervals.html#cb98-1)google_2015 |>
    [](prediction-intervals.html#cb98-2)  model(NAIVE(Close)) |>
    [](prediction-intervals.html#cb98-3)  forecast(h = 10) |>
    [](prediction-intervals.html#cb98-4)  hilo()
    [](prediction-intervals.html#cb98-5)#> # A tsibble: 10 x 7 [1]
    [](prediction-intervals.html#cb98-6)#> # Key:       Symbol, .model [1]
    [](prediction-intervals.html#cb98-7)#>    Symbol .model         day
    [](prediction-intervals.html#cb98-8)#>    <chr>  <chr>        <dbl>
    [](prediction-intervals.html#cb98-9)#>  1 GOOG   NAIVE(Close)   253
    [](prediction-intervals.html#cb98-10)#>  2 GOOG   NAIVE(Close)   254
    [](prediction-intervals.html#cb98-11)#>  3 GOOG   NAIVE(Close)   255
    [](prediction-intervals.html#cb98-12)#>  4 GOOG   NAIVE(Close)   256
    [](prediction-intervals.html#cb98-13)#>  5 GOOG   NAIVE(Close)   257
    [](prediction-intervals.html#cb98-14)#>  6 GOOG   NAIVE(Close)   258
    [](prediction-intervals.html#cb98-15)#>  7 GOOG   NAIVE(Close)   259
    [](prediction-intervals.html#cb98-16)#>  8 GOOG   NAIVE(Close)   260
    [](prediction-intervals.html#cb98-17)#>  9 GOOG   NAIVE(Close)   261
    [](prediction-intervals.html#cb98-18)#> 10 GOOG   NAIVE(Close)   262
    [](prediction-intervals.html#cb98-19)#> # ℹ 4 more variables: Close <dist>, .mean <dbl>, `80%` <hilo>, `95%` <hilo>

The `hilo()` function converts the forecast distributions into intervals. By default, 80% and 95% prediction intervals are returned, although other options are possible via the `level` argument.

When plotted, the prediction intervals are shown as shaded regions, with the strength of colour indicating the probability associated with the interval. Again, 80% and 95% intervals are shown by default, with other options available via the `level` argument.
    
    
    [](prediction-intervals.html#cb99-1)google_2015 |>
    [](prediction-intervals.html#cb99-2)  model(NAIVE(Close)) |>
    [](prediction-intervals.html#cb99-3)  forecast(h = 10) |>
    [](prediction-intervals.html#cb99-4)  autoplot(google_2015) +
    [](prediction-intervals.html#cb99-5)  labs(title="Google daily closing stock price", y="$US" )

Figure 5.14: 80% and 95% prediction intervals for the Google closing stock price based on a naïve method. 

### Prediction intervals from bootstrapped residuals[](prediction-intervals.html#prediction-intervals-from-bootstrapped-residuals)

When a normal distribution for the residuals is an unreasonable assumption, one alternative is to use bootstrapping, which only assumes that the residuals are uncorrelated with constant variance. We will illustrate the procedure using a naïve forecasting method.

A one-step forecast error is defined as \\(e_t = y_t - \hat{y}_{t|t-1}\\). For a naïve forecasting method, \\(\hat{y}_{t|t-1} = y_{t-1}\\), so we can rewrite this as \\[ y_t = y_{t-1} + e_t. \\] Assuming future errors will be similar to past errors, when \\(t>T\\) we can replace \\(e_{t}\\) by sampling from the collection of errors we have seen in the past (i.e., the residuals). So we can simulate the next observation of a time series using \\[ y^*_{T+1} = y_{T} + e^*_{T+1} \\] where \\(e^*_{T+1}\\) is a randomly sampled error from the past, and \\(y^*_{T+1}\\) is the possible future value that would arise if that particular error value occurred. We use a * to indicate that this is not the observed \\(y_{T+1}\\) value, but one possible future that could occur. Adding the new simulated observation to our data set, we can repeat the process to obtain \\[ y^*_{T+2} = y_{T+1}^* + e^*_{T+2}, \\] where \\(e^*_{T+2}\\) is another draw from the collection of residuals. Continuing in this way, we can simulate an entire set of future values for our time series.

Doing this repeatedly, we obtain many possible futures. To see some of them, we can use the `generate()` function.
    
    
    [](prediction-intervals.html#cb100-1)fit <- google_2015 |>
    [](prediction-intervals.html#cb100-2)  model(NAIVE(Close))
    [](prediction-intervals.html#cb100-3)sim <- fit |> generate(h = 30, times = 5, bootstrap = TRUE)
    [](prediction-intervals.html#cb100-4)sim
    [](prediction-intervals.html#cb100-5)#> # A tsibble: 150 x 5 [1]
    [](prediction-intervals.html#cb100-6)#> # Key:       Symbol, .model, .rep [5]
    [](prediction-intervals.html#cb100-7)#>    Symbol .model         day .rep   .sim
    [](prediction-intervals.html#cb100-8)#>    <chr>  <chr>        <dbl> <chr> <dbl>
    [](prediction-intervals.html#cb100-9)#>  1 GOOG   NAIVE(Close)   253 1      756.
    [](prediction-intervals.html#cb100-10)#>  2 GOOG   NAIVE(Close)   254 1      749.
    [](prediction-intervals.html#cb100-11)#>  3 GOOG   NAIVE(Close)   255 1      751.
    [](prediction-intervals.html#cb100-12)#>  4 GOOG   NAIVE(Close)   256 1      750.
    [](prediction-intervals.html#cb100-13)#>  5 GOOG   NAIVE(Close)   257 1      754.
    [](prediction-intervals.html#cb100-14)#>  6 GOOG   NAIVE(Close)   258 1      754.
    [](prediction-intervals.html#cb100-15)#>  7 GOOG   NAIVE(Close)   259 1      758.
    [](prediction-intervals.html#cb100-16)#>  8 GOOG   NAIVE(Close)   260 1      763.
    [](prediction-intervals.html#cb100-17)#>  9 GOOG   NAIVE(Close)   261 1      759.
    [](prediction-intervals.html#cb100-18)#> 10 GOOG   NAIVE(Close)   262 1      748.
    [](prediction-intervals.html#cb100-19)#> # ℹ 140 more rows

Here we have generated five possible sample paths for the next 30 trading days. The `.rep` variable provides a new key for the tsibble. The plot below shows the five sample paths along with the historical data.
    
    
    [](prediction-intervals.html#cb101-1)google_2015 |>
    [](prediction-intervals.html#cb101-2)  ggplot(aes(x = day)) +
    [](prediction-intervals.html#cb101-3)  geom_line(aes(y = Close)) +
    [](prediction-intervals.html#cb101-4)  geom_line(aes(y = .sim, colour = as.factor(.rep)),
    [](prediction-intervals.html#cb101-5)    data = sim) +
    [](prediction-intervals.html#cb101-6)  labs(title="Google daily closing stock price", y="$US" ) +
    [](prediction-intervals.html#cb101-7)  guides(colour = "none")

Figure 5.15: Five simulated future sample paths of the Google closing stock price based on a naïve method with bootstrapped residuals. 

Then we can compute prediction intervals by calculating percentiles of the future sample paths for each forecast horizon. The result is called a **bootstrapped** prediction interval. The name “bootstrap” is a reference to pulling ourselves up by our bootstraps, because the process allows us to measure future uncertainty by only using the historical data.

This is all built into the `forecast()` function so you do not need to call `generate()` directly.
    
    
    [](prediction-intervals.html#cb102-1)fc <- fit |> forecast(h = 30, bootstrap = TRUE)
    [](prediction-intervals.html#cb102-2)fc
    [](prediction-intervals.html#cb102-3)#> # A fable: 30 x 5 [1]
    [](prediction-intervals.html#cb102-4)#> # Key:     Symbol, .model [1]
    [](prediction-intervals.html#cb102-5)#>    Symbol .model         day        Close .mean
    [](prediction-intervals.html#cb102-6)#>    <chr>  <chr>        <dbl>       <dist> <dbl>
    [](prediction-intervals.html#cb102-7)#>  1 GOOG   NAIVE(Close)   253 sample[5000]  759.
    [](prediction-intervals.html#cb102-8)#>  2 GOOG   NAIVE(Close)   254 sample[5000]  759.
    [](prediction-intervals.html#cb102-9)#>  3 GOOG   NAIVE(Close)   255 sample[5000]  758.
    [](prediction-intervals.html#cb102-10)#>  4 GOOG   NAIVE(Close)   256 sample[5000]  759.
    [](prediction-intervals.html#cb102-11)#>  5 GOOG   NAIVE(Close)   257 sample[5000]  759.
    [](prediction-intervals.html#cb102-12)#>  6 GOOG   NAIVE(Close)   258 sample[5000]  759.
    [](prediction-intervals.html#cb102-13)#>  7 GOOG   NAIVE(Close)   259 sample[5000]  759.
    [](prediction-intervals.html#cb102-14)#>  8 GOOG   NAIVE(Close)   260 sample[5000]  759.
    [](prediction-intervals.html#cb102-15)#>  9 GOOG   NAIVE(Close)   261 sample[5000]  759.
    [](prediction-intervals.html#cb102-16)#> 10 GOOG   NAIVE(Close)   262 sample[5000]  759.
    [](prediction-intervals.html#cb102-17)#> # ℹ 20 more rows

Notice that the forecast distribution is now represented as a simulation with 5000 sample paths. Because there is no normality assumption, the prediction intervals are not symmetric. The `.mean` column is the mean of the bootstrap samples, so it may be slightly different from the results obtained without a bootstrap.
    
    
    [](prediction-intervals.html#cb103-1)autoplot(fc, google_2015) +
    [](prediction-intervals.html#cb103-2)  labs(title="Google daily closing stock price", y="$US" )

Figure 5.16: Forecasts of the Google closing stock price based on a naïve method with bootstrapped residuals. 

The number of samples can be controlled using the `times` argument for `forecast()`. For example, intervals based on 1000 bootstrap samples can be sampled with:
    
    
    [](prediction-intervals.html#cb104-1)google_2015 |>
    [](prediction-intervals.html#cb104-2)  model(NAIVE(Close)) |>
    [](prediction-intervals.html#cb104-3)  forecast(h = 10, bootstrap = TRUE, times = 1000) |>
    [](prediction-intervals.html#cb104-4)  hilo()
    [](prediction-intervals.html#cb104-5)#> # A tsibble: 10 x 7 [1]
    [](prediction-intervals.html#cb104-6)#> # Key:       Symbol, .model [1]
    [](prediction-intervals.html#cb104-7)#>    Symbol .model      day        Close .mean            `80%`            `95%`
    [](prediction-intervals.html#cb104-8)#>    <chr>  <chr>     <dbl>       <dist> <dbl>           <hilo>           <hilo>
    [](prediction-intervals.html#cb104-9)#>  1 GOOG   NAIVE(Cl…   253 sample[1000]  760. [748.2, 770.8]80 [743.9, 777.6]95
    [](prediction-intervals.html#cb104-10)#>  2 GOOG   NAIVE(Cl…   254 sample[1000]  760. [743.9, 776.1]80 [734.1, 801.6]95
    [](prediction-intervals.html#cb104-11)#>  3 GOOG   NAIVE(Cl…   255 sample[1000]  760. [739.5, 781.7]80 [728.6, 809.0]95
    [](prediction-intervals.html#cb104-12)#>  4 GOOG   NAIVE(Cl…   256 sample[1000]  760. [736.7, 784.7]80 [723.4, 813.1]95
    [](prediction-intervals.html#cb104-13)#>  5 GOOG   NAIVE(Cl…   257 sample[1000]  760. [734.4, 787.2]80 [719.4, 819.7]95
    [](prediction-intervals.html#cb104-14)#>  6 GOOG   NAIVE(Cl…   258 sample[1000]  760. [731.5, 790.2]80 [717.8, 820.3]95
    [](prediction-intervals.html#cb104-15)#>  7 GOOG   NAIVE(Cl…   259 sample[1000]  761. [730.4, 793.0]80 [713.0, 826.3]95
    [](prediction-intervals.html#cb104-16)#>  8 GOOG   NAIVE(Cl…   260 sample[1000]  761. [726.2, 796.2]80 [706.3, 830.7]95
    [](prediction-intervals.html#cb104-17)#>  9 GOOG   NAIVE(Cl…   261 sample[1000]  761. [723.5, 800.2]80 [707.5, 841.0]95
    [](prediction-intervals.html#cb104-18)#> 10 GOOG   NAIVE(Cl…   262 sample[1000]  760. [719.2, 801.8]80 [701.9, 841.4]95

In this case, they are similar (but not identical) to the prediction intervals based on the normal distribution.

Use the slider below to see the effect of varying the number of bootstrap samples (`times`) on the forecast distribution:


---

## 5.6 Forecasting using transformations[](ftransformations.html#ftransformations)

Some common transformations which can be used when modelling were discussed in Section [3.1](transformations.html#transformations). When forecasting from a model with transformations, we first produce forecasts of the transformed data. Then, we need to reverse the transformation (or _back-transform_) to obtain forecasts on the original scale. For Box-Cox transformations given by [(3.1)](transformations.html#eq:boxcox), the reverse transformation is given by \\[\begin{equation} \tag{5.2} y_{t} = \begin{cases} \exp(w_{t}) & \text{if $\lambda=0$};\\\ \text{sign}(\lambda w_t+1)|\lambda w_t+1|^{1/\lambda} & \text{otherwise}. \end{cases} \end{equation}\\]

The `fable` package will automatically back-transform the forecasts whenever a transformation has been used in the model definition. The back-transformed forecast distribution is then a “transformed Normal” distribution.

### Prediction intervals with transformations[](ftransformations.html#prediction-intervals-with-transformations)

If a transformation has been used, then the prediction interval is first computed on the transformed scale, and the end points are back-transformed to give a prediction interval on the original scale. This approach preserves the probability coverage of the prediction interval, although it will no longer be symmetric around the point forecast.

The back-transformation of prediction intervals is done automatically when using the `fable` package, provided you have used a transformation in the model formula.

Transformations sometimes make little difference to the point forecasts but have a large effect on prediction intervals.

### Bias adjustments[](ftransformations.html#bias-adjustments)

One issue with using mathematical transformations such as Box-Cox transformations is that the back-transformed point forecast will not be the mean of the forecast distribution. In fact, it will usually be the median of the forecast distribution (assuming that the distribution on the transformed space is symmetric). For many purposes, this is acceptable, although the mean is usually preferable. For example, you may wish to add up sales forecasts from various regions to form a forecast for the whole country. But medians do not add up, whereas means do.

For a Box-Cox transformation, the back-transformed mean is given (approximately) by \\[\begin{equation} \tag{5.3} \hat{y}_{T+h|T} = \begin{cases} \exp(\hat{w}_{T+h|T})\left[1 + \frac{\sigma_h^2}{2}\right] & \text{if $\lambda=0$;}\\\ (\lambda \hat{w}_{T+h|T}+1)^{1/\lambda}\left[1 + \frac{\sigma_h^2(1-\lambda)}{2(\lambda \hat{w}_{T+h|T}+1)^{2}}\right] & \text{otherwise;} \end{cases} \end{equation}\\] where \\(\hat{w}_{T+h|T}\\) is the \\(h\\)-step forecast mean and \\(\sigma_h^2\\) is the \\(h\\)-step forecast variance on the transformed scale. The larger the forecast variance, the bigger the difference between the mean and the median.

The difference between the simple back-transformed forecast given by [(5.2)](ftransformations.html#eq:backtransform) and the mean given by [(5.3)](ftransformations.html#eq:backtransformmean) is called the **bias**. When we use the mean, rather than the median, we say the point forecasts have been **bias-adjusted**.

To see how much difference this bias-adjustment makes, consider the following example, where we forecast the average annual price of eggs using the drift method with a log transformation \\((\lambda=0)\\). The log transformation is useful in this case to ensure the forecasts and the prediction intervals stay positive.
    
    
    [](ftransformations.html#cb105-1)fc <- prices |>
    [](ftransformations.html#cb105-2)  filter(!is.na(eggs)) |>
    [](ftransformations.html#cb105-3)  model(RW(log(eggs) ~ drift())) |>
    [](ftransformations.html#cb105-4)  forecast(h = 50) |>
    [](ftransformations.html#cb105-5)  mutate(.median = median(eggs))
    [](ftransformations.html#cb105-6)fc |>
    [](ftransformations.html#cb105-7)  autoplot(prices |> filter(!is.na(eggs)), level = 80) +
    [](ftransformations.html#cb105-8)  geom_line(aes(y = .median), data = fc, linetype = 2, col = "blue") +
    [](ftransformations.html#cb105-9)  labs(title = "Annual egg prices",
    [](ftransformations.html#cb105-10)       y = "$US (in cents adjusted for inflation) ")

Figure 5.17: Forecasts of egg prices using the drift method applied to the logged data. The bias-adjusted mean forecasts are shown with a solid line, while the median forecasts are dashed. 

The dashed line in Figure [5.17](ftransformations.html#fig:biasadjust) shows the forecast medians while the solid line shows the forecast means. Notice how the skewed forecast distribution pulls up the forecast distribution’s mean; this is a result of the added term from the bias adjustment.

Bias-adjusted forecast means are automatically computed in the `fable` package. The forecast median (the point forecast prior to bias adjustment) can be obtained using the `median()` function on the distribution column.


---

## 5.7 Forecasting with decomposition[](forecasting-decomposition.html#forecasting-decomposition)

Time series decomposition (discussed in Chapter [3](decomposition.html#decomposition)) can be a useful step in producing forecasts.

Assuming an additive decomposition, the decomposed time series can be written as \\[ y_t = \hat{S}_t + \hat{A}_t, \\] where \\(\hat{A}_t = \hat{T}_t+\hat{R}_{t}\\) is the seasonally adjusted component. Or, if a multiplicative decomposition has been used, we can write \\[ y_t = \hat{S}_t\hat{A}_t, \\] where \\(\hat{A}_t = \hat{T}_t\hat{R}_{t}\\).

To forecast a decomposed time series, we forecast the seasonal component, \\(\hat{S}_t\\), and the seasonally adjusted component \\(\hat{A}_t\\), separately. It is usually assumed that the seasonal component is unchanging, or changing extremely slowly, so it is forecast by simply taking the last year of the estimated component. In other words, a seasonal naïve method is used for the seasonal component.

To forecast the seasonally adjusted component, any non-seasonal forecasting method may be used. For example, the drift method, or Holt’s method (discussed in Chapter [8](expsmooth.html#expsmooth)), or a non-seasonal ARIMA model (discussed in Chapter [9](arima.html#arima)), may be used.

### Example: Employment in the US retail sector[](forecasting-decomposition.html#example-employment-in-the-us-retail-sector-2)
    
    
    [](forecasting-decomposition.html#cb106-1)us_retail_employment <- us_employment |>
    [](forecasting-decomposition.html#cb106-2)  filter(year(Month) >= 1990, Title == "Retail Trade")
    [](forecasting-decomposition.html#cb106-3)dcmp <- us_retail_employment |>
    [](forecasting-decomposition.html#cb106-4)  model(STL(Employed ~ trend(window = 7), robust = TRUE)) |>
    [](forecasting-decomposition.html#cb106-5)  components() |>
    [](forecasting-decomposition.html#cb106-6)  select(-.model)
    [](forecasting-decomposition.html#cb106-7)dcmp |>
    [](forecasting-decomposition.html#cb106-8)  model(NAIVE(season_adjust)) |>
    [](forecasting-decomposition.html#cb106-9)  forecast() |>
    [](forecasting-decomposition.html#cb106-10)  autoplot(dcmp) +
    [](forecasting-decomposition.html#cb106-11)  labs(y = "Number of people",
    [](forecasting-decomposition.html#cb106-12)       title = "US retail employment")

Figure 5.18: Naïve forecasts of the seasonally adjusted data obtained from an STL decomposition of the total US retail employment. 

Figure [5.18](forecasting-decomposition.html#fig:print-media4) shows naïve forecasts of the seasonally adjusted US retail employment data. These are then “reseasonalised” by adding in the seasonal naïve forecasts of the seasonal component.

This is made easy with the `decomposition_model()` function, which allows you to compute forecasts via any additive decomposition, using other model functions to forecast each of the decomposition’s components. Seasonal components of the model will be forecast automatically using `SNAIVE()` if a different model isn’t specified. The function will also do the reseasonalising for you, ensuring that the resulting forecasts of the original data are obtained. These are shown in Figure [5.19](forecasting-decomposition.html#fig:print-media5).
    
    
    [](forecasting-decomposition.html#cb107-1)fit_dcmp <- us_retail_employment |>
    [](forecasting-decomposition.html#cb107-2)  model(stlf = decomposition_model(
    [](forecasting-decomposition.html#cb107-3)    STL(Employed ~ trend(window = 7), robust = TRUE),
    [](forecasting-decomposition.html#cb107-4)    NAIVE(season_adjust)
    [](forecasting-decomposition.html#cb107-5)  ))
    [](forecasting-decomposition.html#cb107-6)fit_dcmp |>
    [](forecasting-decomposition.html#cb107-7)  forecast() |>
    [](forecasting-decomposition.html#cb107-8)  autoplot(us_retail_employment)+
    [](forecasting-decomposition.html#cb107-9)  labs(y = "Number of people",
    [](forecasting-decomposition.html#cb107-10)       title = "US retail employment")

Figure 5.19: Forecasts of the total US retail employment data based on a naïve forecast of the seasonally adjusted data and a seasonal naïve forecast of the seasonal component, after an STL decomposition of the data. 

The prediction intervals shown in this graph are constructed in the same way as the point forecasts. That is, the upper and lower limits of the prediction intervals on the seasonally adjusted data are “reseasonalised” by adding in the forecasts of the seasonal component.

The ACF of the residuals, shown in Figure [5.20](forecasting-decomposition.html#fig:print-media5-resids), displays significant autocorrelations. These are due to the naïve method not capturing the changing trend in the seasonally adjusted series.
    
    
    [](forecasting-decomposition.html#cb108-1)fit_dcmp |> gg_tsresiduals()

Figure 5.20: Checking the residuals. 

In subsequent chapters we study more suitable methods that can be used to forecast the seasonally adjusted component instead of the naïve method.


---

## 5.8 Evaluating point forecast accuracy[](accuracy.html#accuracy)

### Training and test sets[](accuracy.html#training-and-test-sets)

It is important to evaluate forecast accuracy using genuine forecasts. Consequently, the size of the residuals is not a reliable indication of how large true forecast errors are likely to be. The accuracy of forecasts can only be determined by considering how well a model performs on new data that were not used when fitting the model.

When choosing models, it is common practice to separate the available data into two portions, **training** and **test** data, where the training data is used to estimate any parameters of a forecasting method and the test data is used to evaluate its accuracy. Because the test data is not used in determining the forecasts, it should provide a reliable indication of how well the model is likely to forecast on new data.

The size of the test set is typically about 20% of the total sample, although this value depends on how long the sample is and how far ahead you want to forecast. The test set should ideally be at least as large as the maximum forecast horizon required. The following points should be noted.

  * A model which fits the training data well will not necessarily forecast well.
  * A perfect fit can always be obtained by using a model with enough parameters.
  * Over-fitting a model to data is just as bad as failing to identify a systematic pattern in the data.


Some references describe the test set as the “hold-out set” because these data are “held out” of the data used for fitting. Other references call the training set the “in-sample data” and the test set the “out-of-sample data”. We prefer to use “training data” and “test data” in this book.

### Functions to subset a time series[](accuracy.html#functions-to-subset-a-time-series)

The `filter()` function is useful when extracting a portion of a time series, such as we need when creating training and test sets. When splitting data into evaluation sets, filtering the index of the data is particularly useful. For example,
    
    
    [](accuracy.html#cb109-1)aus_production |> filter(year(Quarter) >= 1995)

extracts all data from 1995 onward. Equivalently,
    
    
    [](accuracy.html#cb110-1)aus_production |> filter_index("1995 Q1" ~ .)

can be used.

Another useful function is `slice()`, which allows the use of indices to choose a subset from each group. For example,
    
    
    [](accuracy.html#cb111-1)aus_production |>
    [](accuracy.html#cb111-2)  slice(n()-19:0)

extracts the last 20 observations (5 years).

Slice also works with groups, making it possible to subset observations from each key. For example,
    
    
    [](accuracy.html#cb112-1)aus_retail |>
    [](accuracy.html#cb112-2)  group_by(State, Industry) |>
    [](accuracy.html#cb112-3)  slice(1:12)

will subset the first year of data from each time series in the data.

### Forecast errors[](accuracy.html#forecast-errors)

A forecast “error” is the difference between an observed value and its forecast. Here “error” does not mean a mistake, it means the unpredictable part of an observation. It can be written as \\[ e_{T+h} = y_{T+h} - \hat{y}_{T+h|T}, \\] where the training data is given by \\(\\{y_1,\dots,y_T\\}\\) and the test data is given by \\(\\{y_{T+1},y_{T+2},\dots\\}\\).

Note that forecast errors are different from residuals in two ways. First, residuals are calculated on the _training_ set while forecast errors are calculated on the _test_ set. Second, residuals are based on _one-step_ forecasts while forecast errors can involve _multi-step_ forecasts.

We can measure forecast accuracy by summarising the forecast errors in different ways.

### Scale-dependent errors[](accuracy.html#scale-dependent-errors)

The forecast errors are on the same scale as the data. Accuracy measures that are based only on \\(e_{t}\\) are therefore scale-dependent and cannot be used to make comparisons between series that involve different units.

The two most commonly used scale-dependent measures are based on the absolute errors or squared errors: \\[\begin{align*} \text{Mean absolute error: MAE} & = \text{mean}(|e_{t}|),\\\ \text{Root mean squared error: RMSE} & = \sqrt{\text{mean}(e_{t}^2)}. \end{align*}\\] When comparing forecast methods applied to a single time series, or to several time series with the same units, the MAE is popular as it is easy to both understand and compute. A forecast method that minimises the MAE will lead to forecasts of the median, while minimising the RMSE will lead to forecasts of the mean. Consequently, the RMSE is also widely used, despite being more difficult to interpret.

### Percentage errors[](accuracy.html#percentage-errors)

The percentage error is given by \\(p_{t} = 100 e_{t}/y_{t}\\). Percentage errors have the advantage of being unit-free, and so are frequently used to compare forecast performances between data sets. The most commonly used measure is: \\[ \text{Mean absolute percentage error: MAPE} = \text{mean}(|p_{t}|). \\] Measures based on percentage errors have the disadvantage of being infinite or undefined if \\(y_{t}=0\\) for any \\(t\\) in the period of interest, and having extreme values if any \\(y_{t}\\) is close to zero. Another problem with percentage errors that is often overlooked is that they assume the unit of measurement has a meaningful zero.[5](accuracy.html#fn5) For example, a percentage error makes no sense when measuring the accuracy of temperature forecasts on either the Fahrenheit or Celsius scales, because temperature has an arbitrary zero point.

They also have the disadvantage that they put a heavier penalty on negative errors than on positive errors. This observation led to the use of the so-called “symmetric” MAPE (sMAPE) proposed by Armstrong ([1978, p. 348](accuracy.html#ref-Armstrong85)), which was used in the M3 forecasting competition. It is defined by \\[ \text{sMAPE} = \text{mean}\left(200|y_{t} - \hat{y}_{t}|/(y_{t}+\hat{y}_{t})\right). \\] However, if \\(y_{t}\\) is close to zero, \\(\hat{y}_{t}\\) is also likely to be close to zero. Thus, the measure still involves division by a number close to zero, making the calculation unstable. Also, the value of sMAPE can be negative, so it is not really a measure of “absolute percentage errors” at all.

Hyndman & Koehler ([2006](accuracy.html#ref-HK06)) recommend that the sMAPE not be used. It is included here only because it is widely used, although we will not use it in this book.

### Scaled errors[](accuracy.html#scaled-errors)

Scaled errors were proposed by Hyndman & Koehler ([2006](accuracy.html#ref-HK06)) as an alternative to using percentage errors when comparing forecast accuracy across series with different units. They proposed scaling the errors based on the _training_ MAE from a simple forecast method.

For a non-seasonal time series, a useful way to define a scaled error uses naïve forecasts: \\[ q_{j} = \frac{\displaystyle e_{j}} {\displaystyle\frac{1}{T-1}\sum_{t=2}^T |y_{t}-y_{t-1}|}. \\] Because the numerator and denominator both involve values on the scale of the original data, \\(q_{j}\\) is independent of the scale of the data. A scaled error is less than one if it arises from a better forecast than the average one-step naïve forecast computed on the training data. Conversely, it is greater than one if the forecast is worse than the average one-step naïve forecast computed on the training data.

For seasonal time series, a scaled error can be defined using seasonal naïve forecasts: \\[ q_{j} = \frac{\displaystyle e_{j}} {\displaystyle\frac{1}{T-m}\sum_{t=m+1}^T |y_{t}-y_{t-m}|}. \\]

The _mean absolute scaled error_ is simply \\[ \text{MASE} = \text{mean}(|q_{j}|). \\] Similarly, the _root mean squared scaled error_ is given by \\[ \text{RMSSE} = \sqrt{\text{mean}(q_{j}^2)}, \\] where \\[ q^2_{j} = \frac{\displaystyle e^2_{j}} {\displaystyle\frac{1}{T-m}\sum_{t=m+1}^T (y_{t}-y_{t-m})^2}, \\] and we set \\(m=1\\) for non-seasonal data.

### Examples[](accuracy.html#examples)
    
    
    [](accuracy.html#cb113-1)recent_production <- aus_production |>
    [](accuracy.html#cb113-2)  filter(year(Quarter) >= 1992)
    [](accuracy.html#cb113-3)beer_train <- recent_production |>
    [](accuracy.html#cb113-4)  filter(year(Quarter) <= 2007)
    [](accuracy.html#cb113-5)
    [](accuracy.html#cb113-6)beer_fit <- beer_train |>
    [](accuracy.html#cb113-7)  model(
    [](accuracy.html#cb113-8)    Mean = MEAN(Beer),
    [](accuracy.html#cb113-9)    `Naïve` = NAIVE(Beer),
    [](accuracy.html#cb113-10)    `Seasonal naïve` = SNAIVE(Beer),
    [](accuracy.html#cb113-11)    Drift = RW(Beer ~ drift())
    [](accuracy.html#cb113-12)  )
    [](accuracy.html#cb113-13)
    [](accuracy.html#cb113-14)beer_fc <- beer_fit |>
    [](accuracy.html#cb113-15)  forecast(h = 10)
    [](accuracy.html#cb113-16)
    [](accuracy.html#cb113-17)beer_fc |>
    [](accuracy.html#cb113-18)  autoplot(
    [](accuracy.html#cb113-19)    aus_production |> filter(year(Quarter) >= 1992),
    [](accuracy.html#cb113-20)    level = NULL
    [](accuracy.html#cb113-21)  ) +
    [](accuracy.html#cb113-22)  labs(
    [](accuracy.html#cb113-23)    y = "Megalitres",
    [](accuracy.html#cb113-24)    title = "Forecasts for quarterly beer production"
    [](accuracy.html#cb113-25)  ) +
    [](accuracy.html#cb113-26)  guides(colour = guide_legend(title = "Forecast"))

Figure 5.21: Forecasts of Australian quarterly beer production using data up to the end of 2007. 

Figure [5.21](accuracy.html#fig:beeraccuracy) shows four forecast methods applied to the quarterly Australian beer production using data only to the end of 2007. The actual values for the period 2008–2010 are also shown. We compute the forecast accuracy measures for this period.
    
    
    [](accuracy.html#cb114-1)accuracy(beer_fc, recent_production)

Method | RMSE | MAE | MAPE | MASE  
---|---|---|---|---  
Drift method | 64.90 | 58.88 | 14.58 | 4.12  
Mean method | 38.45 | 34.83 | 8.28 | 2.44  
Naïve method | 62.69 | 57.40 | 14.18 | 4.01  
Seasonal naïve method | 14.31 | 13.40 | 3.17 | 0.94  
  
The `accuracy()` function will automatically extract the relevant periods from the data (`recent_production` in this example) to match the forecasts when computing the various accuracy measures.

It is obvious from the graph that the seasonal naïve method is best for these data, although it can still be improved, as we will discover later. Sometimes, different accuracy measures will lead to different results as to which forecast method is best. However, in this case, all of the results point to the seasonal naïve method as the best of these four methods for this data set.

To take a non-seasonal example, consider the Google stock price. The following graph shows the closing stock prices from 2015, along with forecasts for January 2016 obtained from three different methods.
    
    
    [](accuracy.html#cb115-1)google_fit <- google_2015 |>
    [](accuracy.html#cb115-2)  model(
    [](accuracy.html#cb115-3)    Mean = MEAN(Close),
    [](accuracy.html#cb115-4)    `Naïve` = NAIVE(Close),
    [](accuracy.html#cb115-5)    Drift = RW(Close ~ drift())
    [](accuracy.html#cb115-6)  )
    [](accuracy.html#cb115-7)
    [](accuracy.html#cb115-8)google_fc <- google_fit |>
    [](accuracy.html#cb115-9)  forecast(google_jan_2016)
    
    
    [](accuracy.html#cb116-1)google_fc |>
    [](accuracy.html#cb116-2)  autoplot(bind_rows(google_2015, google_jan_2016),
    [](accuracy.html#cb116-3)    level = NULL) +
    [](accuracy.html#cb116-4)  labs(y = "$US",
    [](accuracy.html#cb116-5)       title = "Google closing stock prices from Jan 2015") +
    [](accuracy.html#cb116-6)  guides(colour = guide_legend(title = "Forecast"))

Figure 5.22: Forecasts of the Google stock price for Jan 2016. 
    
    
    [](accuracy.html#cb117-1)accuracy(google_fc, google_stock)

Method | RMSE | MAE | MAPE | MASE  
---|---|---|---|---  
Drift method | 53.07 | 49.82 | 6.99 | 6.99  
Mean method | 118.03 | 116.95 | 16.24 | 16.41  
Naïve method | 43.43 | 40.38 | 5.67 | 5.67  
  
Here, the best method is the naïve method (regardless of which accuracy measure is used).

### Bibliography[](bibliography.html#bibliography)

Armstrong, J. S. (1978). _Long-range forecasting: From crystal ball to computer_. John Wiley & Sons. [__](http://amazon.com/dp/0471030023?tag=otexts20)

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. _International Journal of Forecasting_ , _22_(4), 679–688. [__](https://doi.org/10.1016/j.ijforecast.2006.03.001)

* * *

  5. That is, a percentage is valid on a ratio scale, but not on an interval scale. Only ratio scale variables have meaningful zeros.[↩︎](accuracy.html#fnref5)




---

## 5.9 Evaluating distributional forecast accuracy[](distaccuracy.html#distaccuracy)

The preceding measures all measure point forecast accuracy. When evaluating distributional forecasts, we need to use some other measures.

### Quantile scores[](distaccuracy.html#quantile-scores)

Consider the Google stock price example from the previous section. Figure [5.23](distaccuracy.html#fig:googlepi) shows an 80% prediction interval for the forecasts from the naïve method.
    
    
    [](distaccuracy.html#cb118-1)google_fc |>
    [](distaccuracy.html#cb118-2)  filter(.model == "Naïve") |>
    [](distaccuracy.html#cb118-3)  autoplot(bind_rows(google_2015, google_jan_2016), level=80)+
    [](distaccuracy.html#cb118-4)  labs(y = "$US",
    [](distaccuracy.html#cb118-5)       title = "Google closing stock prices")

Figure 5.23: Naïve forecasts of the Google stock price for Jan 2016, along with 80% prediction intervals. 

The lower limit of this prediction interval gives the 10th percentile (or 0.1 quantile) of the forecast distribution, so we would expect the actual value to lie below the lower limit about 10% of the time, and to lie above the lower limit about 90% of the time. When we compare the actual value to this percentile, we need to allow for the fact that it is more likely to be above than below.

More generally, suppose we are interested in the quantile forecast with probability \\(p\\) at future time \\(t\\), and let this be denoted by \\(f_{p,t}\\). That is, we expect the observation \\(y_t\\) to be less than \\(f_{p,t}\\) with probability \\(p\\). For example, the 10th percentile would be \\(f_{0.10,t}\\). If \\(y_{t}\\) denotes the observation at time \\(t\\), then the **Quantile Score** is \\[ Q_{p,t} = \begin{cases} 2(1 - p) \big(f_{p,t} - y_{t}\big), & \text{if $y_{t} < f_{p,t}$}\\\ 2p \big(y_{t} - f_{p,t}\big), & \text{if $y_{t} \ge f_{p,t}$} \end{cases} \\] This is sometimes called the “pinball loss function” because a graph of it resembles the trajectory of a ball on a pinball table. The multiplier of 2 is often omitted, but including it makes the interpretation a little easier. A low value of \\(Q_{p,t}\\) indicates a better estimate of the quantile.

The quantile score can be interpreted like an absolute error. In fact, when \\(p=0.5\\), the quantile score \\(Q_{0.5,t}\\) is the same as the absolute error. For other values of \\(p\\), the “error” \\((y_t - f_{p,t})\\) is weighted to take account of how likely it is to be positive or negative. If \\(p>0.5\\), \\(Q_{p,t}\\) gives a heavier penalty when the observation is greater than the estimated quantile than when the observation is less than the estimated quantile. The reverse is true for \\(p<0.5\\).

In Figure [5.23](distaccuracy.html#fig:googlepi), the one-step-ahead 10% quantile forecast (for 4 January 2016) is \\(f_{0.1,t} = 744.54\\) and the observed value is \\(y_t = 741.84\\). Then \\[ Q_{0.1,t} = 2(1-0.1) (744.54 - 741.84) = 4.86. \\] This is easily computed using `accuracy()` with the `quantile_score()` function:
    
    
    [](distaccuracy.html#cb119-1)google_fc |>
    [](distaccuracy.html#cb119-2)  filter(.model == "Naïve", Date == "2016-01-04") |>
    [](distaccuracy.html#cb119-3)  accuracy(google_stock, list(qs=quantile_score), probs=0.10)
    [](distaccuracy.html#cb119-4)#> # A tibble: 1 × 4
    [](distaccuracy.html#cb119-5)#>   .model Symbol .type    qs
    [](distaccuracy.html#cb119-6)#>   <chr>  <chr>  <chr> <dbl>
    [](distaccuracy.html#cb119-7)#> 1 Naïve  GOOG   Test   4.86

### Winkler Score[](distaccuracy.html#winkler-score)

It is often of interest to evaluate a prediction interval, rather than a few quantiles, and the Winkler score proposed by Winkler ([1972](distaccuracy.html#ref-Winkler1972)) is designed for this purpose. If the \\(100(1-\alpha)\\)% prediction interval at time \\(t\\) is given by \\([\ell_{\alpha,t}, u_{\alpha,t}]\\), then the Winkler score is defined as the length of the interval plus a penalty if the observation is outside the interval: \\[ W_{\alpha,t} = \begin{cases} (u_{\alpha,t} - \ell_{\alpha,t}) + \frac{2}{\alpha} (\ell_{\alpha,t} - y_t) & \text{if } y_t < \ell_{\alpha,t} \\\ (u_{\alpha,t} - \ell_{\alpha,t}) & \text{if } \ell_{\alpha,t} \le y_t \le u_{\alpha,t} \\\ (u_{\alpha,t} - \ell_{\alpha,t}) + \frac{2}{\alpha} (y_t - u_{\alpha,t}) & \text{if } y_t > u_{\alpha,t}. \end{cases} \\] For observations that fall within the interval, the Winkler score is simply the length of the interval. Thus, low scores are associated with narrow intervals. However, if the observation falls outside the interval, the penalty applies, with the penalty proportional to how far the observation is outside the interval.

Prediction intervals are usually constructed from quantiles by setting \\(\ell_{\alpha,t} = f_{\alpha/2,t}\\) and \\(u_{\alpha,t} = f_{1-\alpha/2,t}\\). If we add the corresponding quantile scores and divide by \\(\alpha\\), we get the Winkler score: \\[ W_{\alpha,t} = (Q_{\alpha/2,t} + Q_{1-\alpha/2,t})/\alpha. \\]

The one-step-ahead 80% interval shown in Figure [5.23](distaccuracy.html#fig:googlepi) for 4 January 2016 is [744.54, 773.22], and the actual value was 741.84, so the Winkler score is \\[ W_{\alpha,t} = (773.22 - 744.54) + \frac{2}{0.2} (744.54 - 741.84) = 55.68. \\] This is easily computed using `accuracy()` with the `winkler_score()` function:
    
    
    [](distaccuracy.html#cb120-1)google_fc |>
    [](distaccuracy.html#cb120-2)  filter(.model == "Naïve", Date == "2016-01-04") |>
    [](distaccuracy.html#cb120-3)  accuracy(google_stock,
    [](distaccuracy.html#cb120-4)    list(winkler = winkler_score), level = 80)
    [](distaccuracy.html#cb120-5)#> # A tibble: 1 × 4
    [](distaccuracy.html#cb120-6)#>   .model Symbol .type winkler
    [](distaccuracy.html#cb120-7)#>   <chr>  <chr>  <chr>   <dbl>
    [](distaccuracy.html#cb120-8)#> 1 Naïve  GOOG   Test     55.7

### Continuous Ranked Probability Score[](distaccuracy.html#continuous-ranked-probability-score)

Often we are interested in the whole forecast distribution, rather than particular quantiles or prediction intervals. In that case, we can average the quantile scores over all values of \\(p\\) to obtain the **Continuous Ranked Probability Score** or CRPS ([Gneiting & Katzfuss, 2014](distaccuracy.html#ref-Gneiting2014)).

In the Google stock price example, we can compute the average CRPS value for all days in the test set. A CRPS value is a little like a weighted absolute error computed from the entire forecast distribution, where the weighting takes account of the probabilities.
    
    
    [](distaccuracy.html#cb121-1)google_fc |>
    [](distaccuracy.html#cb121-2)  accuracy(google_stock, list(crps = CRPS))
    [](distaccuracy.html#cb121-3)#> # A tibble: 3 × 4
    [](distaccuracy.html#cb121-4)#>   .model Symbol .type  crps
    [](distaccuracy.html#cb121-5)#>   <chr>  <chr>  <chr> <dbl>
    [](distaccuracy.html#cb121-6)#> 1 Drift  GOOG   Test   33.5
    [](distaccuracy.html#cb121-7)#> 2 Mean   GOOG   Test   76.7
    [](distaccuracy.html#cb121-8)#> 3 Naïve  GOOG   Test   26.5

Here, the naïve method is giving better distributional forecasts than the drift or mean methods.

### Scale-free comparisons using skill scores[](distaccuracy.html#scale-free-comparisons-using-skill-scores)

As with point forecasts, it is useful to be able to compare the distributional forecast accuracy of several methods across series on different scales. For point forecasts, we used scaled errors for that purpose. Another approach is to use skill scores. These can be used for both point forecast accuracy and distributional forecast accuracy.

With skill scores, we compute a forecast accuracy measure relative to some benchmark method. For example, if we use the naïve method as a benchmark, and also compute forecasts using the drift method, we can compute the CRPS skill score of the drift method relative to the naïve method as \\[ \frac{\text{CRPS}_{\text{Naïve}} - \text{CRPS}_{\text{Drift}}}{\text{CRPS}_{\text{Naïve}}}. \\] This gives the proportion that the drift method improves over the naïve method based on CRPS. It is easy to compute using the `accuracy()` function.
    
    
    [](distaccuracy.html#cb122-1)google_fc |>
    [](distaccuracy.html#cb122-2)  accuracy(google_stock, list(skill = skill_score(CRPS)))
    [](distaccuracy.html#cb122-3)#> # A tibble: 3 × 4
    [](distaccuracy.html#cb122-4)#>   .model Symbol .type  skill
    [](distaccuracy.html#cb122-5)#>   <chr>  <chr>  <chr>  <dbl>
    [](distaccuracy.html#cb122-6)#> 1 Drift  GOOG   Test  -0.266
    [](distaccuracy.html#cb122-7)#> 2 Mean   GOOG   Test  -1.90 
    [](distaccuracy.html#cb122-8)#> 3 Naïve  GOOG   Test   0

Of course, the skill score for the naïve method is 0 because it can’t improve on itself. The other two methods have larger CRPS values than naïve, so the skills scores are negative; the drift method is 26.6% worse than the naïve method.

The `skill_score()` function will always compute the CRPS for the appropriate benchmark forecasts, even if these are not included in the `fable` object. When the data are seasonal, the benchmark used is the seasonal naïve method rather than the naïve method. To ensure that the same training data are used for the benchmark forecasts, it is important that the data provided to the `accuracy()` function starts at the same time as the training data.

The `skill_score()` function can be used with any accuracy measure. For example, `skill_score(MSE)` provides a way of comparing MSE values across diverse series. However, it is important that the test set is large enough to allow reliable calculation of the error measure, especially in the denominator. For that reason, MASE or RMSSE are often preferable scale-free measures for point forecast accuracy.

### Bibliography[](bibliography.html#bibliography)

Gneiting, T., & Katzfuss, N. (2014). Probabilistic forecasting. _Annual Review of Statistics and Its Application_ , _1_(1), 125–151. [__](https://doi.org/10.1146/annurev-statistics-062713-085831)

Winkler, R. L. (1972). A decision-theoretic approach to interval estimation. _Journal of the American Statistical Association_ , _67_(337), 187–191. [__](https://doi.org/10.1080/01621459.1972.10481224)


---

## 5.10 Time series cross-validation[](tscv.html#tscv)

A more sophisticated version of training/test sets is time series cross-validation. In this procedure, there are a series of test sets, each consisting of a single observation. The corresponding training set consists only of observations that occurred _prior_ to the observation that forms the test set. Thus, no future observations can be used in constructing the forecast. Since it is not possible to obtain a reliable forecast based on a small training set, the earliest observations are not considered as test sets.

The following diagram illustrates the series of training and test sets, where the blue observations form the training sets, and the orange observations form the test sets.

The forecast accuracy is computed by averaging over the test sets. This procedure is sometimes known as “evaluation on a rolling forecasting origin” because the “origin” at which the forecast is based rolls forward in time.

With time series forecasting, one-step forecasts may not be as relevant as multi-step forecasts. In this case, the cross-validation procedure based on a rolling forecasting origin can be modified to allow multi-step errors to be used. Suppose that we are interested in models that produce good \\(4\\)-step-ahead forecasts. Then the corresponding diagram is shown below.

In the following example, we compare the forecast accuracy obtained via time series cross-validation with the residual accuracy. The `stretch_tsibble()` function is used to create many training sets. In this example, we start with a training set of length `.init=3`, and increase the size of successive training sets by `.step=1`.
    
    
    [](tscv.html#cb123-1)# Time series cross-validation accuracy
    [](tscv.html#cb123-2)google_2015_tr <- google_2015 |>
    [](tscv.html#cb123-3)  stretch_tsibble(.init = 3, .step = 1) |>
    [](tscv.html#cb123-4)  relocate(Date, Symbol, .id)
    [](tscv.html#cb123-5)google_2015_tr
    [](tscv.html#cb123-6)#> # A tsibble: 31,875 x 10 [1]
    [](tscv.html#cb123-7)#> # Key:       Symbol, .id [250]
    [](tscv.html#cb123-8)#>    Date       Symbol   .id  Open  High   Low Close Adj_Close  Volume   day
    [](tscv.html#cb123-9)#>    <date>     <chr>  <int> <dbl> <dbl> <dbl> <dbl>     <dbl>   <dbl> <int>
    [](tscv.html#cb123-10)#>  1 2015-01-02 GOOG       1  526.  528.  521.  522.      522. 1447600     1
    [](tscv.html#cb123-11)#>  2 2015-01-05 GOOG       1  520.  521.  510.  511.      511. 2059800     2
    [](tscv.html#cb123-12)#>  3 2015-01-06 GOOG       1  512.  513.  498.  499.      499. 2899900     3
    [](tscv.html#cb123-13)#>  4 2015-01-02 GOOG       2  526.  528.  521.  522.      522. 1447600     1
    [](tscv.html#cb123-14)#>  5 2015-01-05 GOOG       2  520.  521.  510.  511.      511. 2059800     2
    [](tscv.html#cb123-15)#>  6 2015-01-06 GOOG       2  512.  513.  498.  499.      499. 2899900     3
    [](tscv.html#cb123-16)#>  7 2015-01-07 GOOG       2  504.  504.  497.  498.      498. 2065100     4
    [](tscv.html#cb123-17)#>  8 2015-01-02 GOOG       3  526.  528.  521.  522.      522. 1447600     1
    [](tscv.html#cb123-18)#>  9 2015-01-05 GOOG       3  520.  521.  510.  511.      511. 2059800     2
    [](tscv.html#cb123-19)#> 10 2015-01-06 GOOG       3  512.  513.  498.  499.      499. 2899900     3
    [](tscv.html#cb123-20)#> # ℹ 31,865 more rows

The `.id` column provides a new key indicating the various training sets. The `accuracy()` function can be used to evaluate the forecast accuracy across the training sets.
    
    
    [](tscv.html#cb124-1)# TSCV accuracy
    [](tscv.html#cb124-2)google_2015_tr |>
    [](tscv.html#cb124-3)  model(RW(Close ~ drift())) |>
    [](tscv.html#cb124-4)  forecast(h = 1) |>
    [](tscv.html#cb124-5)  accuracy(google_2015)
    [](tscv.html#cb124-6)# Training set accuracy
    [](tscv.html#cb124-7)google_2015 |>
    [](tscv.html#cb124-8)  model(RW(Close ~ drift())) |>
    [](tscv.html#cb124-9)  accuracy()

Evaluation method | RMSE | MAE | MAPE | MASE  
---|---|---|---|---  
Cross-validation | 11.27 | 7.26 | 1.19 | 1.02  
Training | 11.15 | 7.16 | 1.18 | 1.00  
  
As expected, the accuracy measures from the residuals are smaller, as the corresponding “forecasts” are based on a model fitted to the entire data set, rather than being true forecasts.

A good way to choose the best forecasting model is to find the model with the smallest RMSE computed using time series cross-validation.

### Example: Forecast horizon accuracy with cross-validation[](tscv.html#example-forecast-horizon-accuracy-with-cross-validation)

The `google_2015` subset of the `gafa_stock` data, plotted in Figure [5.9](diagnostics.html#fig:GSPautoplot), includes daily closing stock price of Google Inc from the NASDAQ exchange for all trading days in 2015.

The code below evaluates the forecasting performance of 1- to 8-step-ahead drift forecasts. The plot shows that the forecast error increases as the forecast horizon increases, as we would expect.
    
    
    [](tscv.html#cb125-1)google_2015_tr <- google_2015 |>
    [](tscv.html#cb125-2)  stretch_tsibble(.init = 3, .step = 1)
    [](tscv.html#cb125-3)fc <- google_2015_tr |>
    [](tscv.html#cb125-4)  model(RW(Close ~ drift())) |>
    [](tscv.html#cb125-5)  forecast(h = 8) |>
    [](tscv.html#cb125-6)  group_by(.id) |>
    [](tscv.html#cb125-7)  mutate(h = row_number()) |>
    [](tscv.html#cb125-8)  ungroup() |>
    [](tscv.html#cb125-9)  as_fable(response = "Close", distribution = Close)
    [](tscv.html#cb125-10)fc |>
    [](tscv.html#cb125-11)  accuracy(google_2015, by = c("h", ".model")) |>
    [](tscv.html#cb125-12)  ggplot(aes(x = h, y = RMSE)) +
    [](tscv.html#cb125-13)  geom_point()

Figure 5.24: RMSE as a function of forecast horizon for the drift method applied to Google closing stock prices. 


---

## 5.11 Exercises[](toolbox-exercises.html#toolbox-exercises)

  1. Produce forecasts for the following series using whichever of `NAIVE(y)`, `SNAIVE(y)` or `RW(y ~ drift())` is more appropriate in each case:

     * Australian Population (`global_economy`)
     * Bricks (`aus_production`)
     * NSW Lambs (`aus_livestock`)
     * Household wealth (`hh_budget`).
     * Australian takeaway food turnover (`aus_retail`).
  2. Use the Facebook stock price (data set `gafa_stock`) to do the following:

     1. Produce a time plot of the series.
     2. Produce forecasts using the drift method and plot them.
     3. Show that the forecasts are identical to extending the line drawn between the first and last observations.
     4. Try using some of the other benchmark functions to forecast the same data set. Which do you think is best? Why?
  3. Apply a seasonal naïve method to the quarterly Australian beer production data from 1992. Check if the residuals look like white noise, and plot the forecasts. The following code will help.
         
         [](toolbox-exercises.html#cb126-1)# Extract data of interest
         [](toolbox-exercises.html#cb126-2)recent_production <- aus_production |>
         [](toolbox-exercises.html#cb126-3)  filter(year(Quarter) >= 1992)
         [](toolbox-exercises.html#cb126-4)# Define and estimate a model
         [](toolbox-exercises.html#cb126-5)fit <- recent_production |> model(SNAIVE(Beer))
         [](toolbox-exercises.html#cb126-6)# Look at the residuals
         [](toolbox-exercises.html#cb126-7)fit |> gg_tsresiduals()
         [](toolbox-exercises.html#cb126-8)# Look a some forecasts
         [](toolbox-exercises.html#cb126-9)fit |> forecast() |> autoplot(recent_production)

What do you conclude?

  4. Repeat the previous exercise using the Australian Exports series from `global_economy` and the Bricks series from `aus_production`. Use whichever of `NAIVE()` or `SNAIVE()` is more appropriate in each case.

  5. Produce forecasts for the 7 Victorian series in `aus_livestock` using `SNAIVE()`. Plot the resulting forecasts including the historical data. Is this a reasonable benchmark for these series?

  6. Are the following statements true or false? Explain your answer.

     1. Good forecast methods should have normally distributed residuals.
     2. A model with small residuals will give good forecasts.
     3. The best measure of forecast accuracy is MAPE.
     4. If your model doesn’t forecast well, you should make it more complicated.
     5. Always choose the model with the best forecast accuracy as measured on the test set.
  7. For your retail time series (from Exercise 7 in Section [2.10](graphics-exercises.html#graphics-exercises)):

     1. Create a training dataset consisting of observations before 2011 using
            
            [](toolbox-exercises.html#cb127-1)myseries_train <- myseries |>
            [](toolbox-exercises.html#cb127-2)  filter(year(Month) < 2011)

     2. Check that your data have been split appropriately by producing the following plot.
            
            [](toolbox-exercises.html#cb128-1)autoplot(myseries, Turnover) +
            [](toolbox-exercises.html#cb128-2)  autolayer(myseries_train, Turnover, colour = "red")

     3. Fit a seasonal naïve model using `SNAIVE()` applied to your training data (`myseries_train`).
            
            [](toolbox-exercises.html#cb129-1)fit <- myseries_train |>
            [](toolbox-exercises.html#cb129-2)  model(SNAIVE())

     4. Check the residuals.
            
            [](toolbox-exercises.html#cb130-1)fit |> gg_tsresiduals()

Do the residuals appear to be uncorrelated and normally distributed?

     5. Produce forecasts for the test data
            
            [](toolbox-exercises.html#cb131-1)fc <- fit |>
            [](toolbox-exercises.html#cb131-2)  forecast(new_data = anti_join(myseries, myseries_train))
            [](toolbox-exercises.html#cb131-3)fc |> autoplot(myseries)

     6. Compare the accuracy of your forecasts against the actual values.
            
            [](toolbox-exercises.html#cb132-1)fit |> accuracy()
            [](toolbox-exercises.html#cb132-2)fc |> accuracy(myseries)

     7. How sensitive are the accuracy measures to the amount of training data used?

  8. Consider the number of pigs slaughtered in New South Wales (data set `aus_livestock`).

     1. Produce some plots of the data in order to become familiar with it.
     2. Create a training set of 486 observations, withholding a test set of 72 observations (6 years).
     3. Try using various benchmark methods to forecast the training set and compare the results on the test set. Which method did best?
     4. Check the residuals of your preferred method. Do they resemble white noise?
  9.      1. Create a training set for household wealth (`hh_budget`) by withholding the last four years as a test set.
     2. Fit all the appropriate benchmark methods to the training set and forecast the periods covered by the test set.
     3. Compute the accuracy of your forecasts. Which method does best?
     4. Do the residuals from the best method resemble white noise?
  10.      1. Create a training set for Australian takeaway food turnover (`aus_retail`) by withholding the last four years as a test set.
     2. Fit all the appropriate benchmark methods to the training set and forecast the periods covered by the test set.
     3. Compute the accuracy of your forecasts. Which method does best?
     4. Do the residuals from the best method resemble white noise?
  11. We will use the Bricks data from `aus_production` (Australian quarterly clay brick production 1956–2005) for this exercise.

     1. Use an STL decomposition to calculate the trend-cycle and seasonal indices. (Experiment with having fixed or changing seasonality.)
     2. Compute and plot the seasonally adjusted data.
     3. Use a naïve method to produce forecasts of the seasonally adjusted data.
     4. Use `decomposition_model()` to reseasonalise the results, giving forecasts for the original data.
     5. Do the residuals look uncorrelated?
     6. Repeat with a robust STL decomposition. Does it make much difference?
     7. Compare forecasts from `decomposition_model()` with those from `SNAIVE()`, using a test set comprising the last 2 years of data. Which is better?
  12. `tourism` contains quarterly visitor nights (in thousands) from 1998 to 2017 for 76 regions of Australia.

     1. Extract data from the Gold Coast region using `filter()` and aggregate total overnight trips (sum over `Purpose`) using `summarise()`. Call this new dataset `gc_tourism`.

     2. Using `slice()` or `filter()`, create three training sets for this data excluding the last 1, 2 and 3 years. For example, `gc_train_1 <- gc_tourism |> slice(1:(n()-4))`.

     3. Compute one year of forecasts for each training set using the seasonal naïve (`SNAIVE()`) method. Call these `gc_fc_1`, `gc_fc_2` and `gc_fc_3`, respectively.

     4. Use `accuracy()` to compare the test set forecast accuracy using MAPE. Comment on these.




---

## 5.12 Further reading[](basics-reading.html#basics-reading)

  * Ord et al. ([2017](basics-reading.html#ref-Ord2017)) provides further discussion of simple benchmark forecasting methods.
  * A review of forecast evaluation methods is given in Hyndman & Koehler ([2006](basics-reading.html#ref-HK06)), looking at the strengths and weaknesses of different approaches. This is the paper that introduced the MASE as a general-purpose forecast accuracy measure.
  * For a discussion of forecasting using STL, see Theodosiou ([2011](basics-reading.html#ref-Theodosiou2011)).
  * An excellent discussion of evaluating distributional forecast accuracy is provided by Gneiting & Katzfuss ([2014](basics-reading.html#ref-Gneiting2014)).


### Bibliography[](bibliography.html#bibliography)

Gneiting, T., & Katzfuss, N. (2014). Probabilistic forecasting. _Annual Review of Statistics and Its Application_ , _1_(1), 125–151. [__](https://doi.org/10.1146/annurev-statistics-062713-085831)

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. _International Journal of Forecasting_ , _22_(4), 679–688. [__](https://doi.org/10.1016/j.ijforecast.2006.03.001)

Ord, J. K., Fildes, R., & Kourentzes, N. (2017). _Principles of business forecasting_ (2nd ed.). Wessex Press Publishing Co. [__](http://amazon.com/dp/0999064916?tag=otexts20)

Theodosiou, M. (2011). Forecasting monthly and quarterly time series using STL decomposition. _International Journal of Forecasting_ , _27_(4), 1178–1195. [__](https://doi.org/10.1016/j.ijforecast.2010.11.002)


---

# Chapter 6 Judgmental forecasts[](judgmental.html#judgmental)

Forecasting using judgment is common in practice. In many cases, judgmental forecasting is the only option, such as when there is a complete lack of historical data, or when a new product is being launched, or when a new competitor enters the market, or during completely new and unique market conditions. For example, in December 2012, the Australian government was the first in the world to pass legislation that banned the use of company logos on cigarette packets, and required all cigarette packets to be a dark green colour. Judgment must be applied in order to forecast the effect of such a policy, as there are no historical precedents.

There are also situations where the data are incomplete, or only become available after some delay. For example, central banks include judgment when forecasting the current level of economic activity, a procedure known as nowcasting, as GDP is only available on a quarterly basis.

Research in this area[6](judgmental.html#fn6) has shown that the accuracy of judgmental forecasting improves when the forecaster has (i) important domain knowledge, and (ii) more timely, up-to-date information. A judgmental approach can be quick to adjust to such changes, information or events.

Over the years, the acceptance of judgmental forecasting as a science has increased, as has the recognition of its need. More importantly, the quality of judgmental forecasts has also improved, as a direct result of recognising that improvements in judgmental forecasting can be achieved by implementing well-structured and systematic approaches. It is important to recognise that judgmental forecasting is subjective and comes with limitations. However, implementing systematic and well-structured approaches can confine these limitations and markedly improve forecast accuracy.

There are three general settings in which judgmental forecasting is used: (i) there are no available data, so that statistical methods are not applicable and judgmental forecasting is the only feasible approach; (ii) data are available, statistical forecasts are generated, and these are then adjusted using judgment; and (iii) data are available and statistical and judgmental forecasts are generated independently and then combined. We should clarify that when data are available, applying statistical methods (such as those discussed in other chapters of this book), is preferable and should always be used as a starting point. Statistical forecasts are generally superior to generating forecasts using only judgment. For the majority of the chapter, we focus on the first setting where no data are available, and in the last section we discuss the judgmental adjustment of statistical forecasts. We discuss combining forecasts in Section [13.4](combinations.html#combinations).

### Bibliography[](bibliography.html#bibliography)

Lawrence, M., Goodwin, P., O’Connor, M., & Önkal, D. (2006). Judgmental forecasting: A review of progress over the last 25 years. _International Journal of Forecasting_ , _22_(3), 493–518. [__](https://doi.org/10.1016/j.ijforecast.2006.03.007)

* * *

  6. Lawrence et al. ([2006](judgmental.html#ref-Lawrence2006))[↩︎](judgmental.html#fnref6)




---

## 6.1 Beware of limitations[](judgmental-limitations.html#judgmental-limitations)

Judgmental forecasts are subjective, and therefore do not come free of bias or limitations.

Judgmental forecasts can be inconsistent. Unlike statistical forecasts, which can be generated by the same mathematical formulas every time, judgmental forecasts depend heavily on human cognition, and are vulnerable to its limitations. For example, a limited memory may render recent events more important than they actually are and may ignore momentous events from the more distant past; or a limited attention span may result in important information being missed; or a misunderstanding of causal relationships may lead to erroneous inferences. Furthermore, human judgment can vary due to the effect of psychological factors. One can imagine a manager who is in a positive frame of mind one day, generating forecasts that may tend to be somewhat optimistic, and in a negative frame of mind another day, generating somewhat less optimistic forecasts.

Judgment can be clouded by personal or political agendas, where targets and forecasts (as defined in Chapter [1](intro.html#intro)) are not segregated. For example, if a sales manager knows that the forecasts she generates will be used to set sales expectations (targets), she may tend to set these low in order to show a good performance (i.e., exceed the expected targets). Even in cases where targets and forecasts are well segregated, judgment may be plagued by optimism or wishful thinking. For example, it would be highly unlikely that a team working towards launching a new product would forecast its failure. As we will discuss later, this optimism can be accentuated in a group meeting setting. “Beware of the enthusiasm of your marketing and sales colleagues”[7](judgmental-limitations.html#fn7).

Another undesirable property which is commonly seen in judgmental forecasting is the effect of anchoring. In this case, the subsequent forecasts tend to converge or be close to an initial familiar reference point. For example, it is common to take the last observed value as a reference point. The forecaster is influenced unduly by prior information, and therefore gives this more weight in the forecasting process. Anchoring may lead to conservatism and undervaluing new and more current information, and thereby create a systematic bias.

### Bibliography[](bibliography.html#bibliography)

Fildes, R., & Goodwin, P. (2007b). Good and bad judgment in forecasting: Lessons from four companies. _Foresight: The International Journal of Applied Forecasting_ , _8_ , 5–10. 

* * *

  7. Fildes & Goodwin ([2007b](judgmental-limitations.html#ref-Fildes2007a))[↩︎](judgmental-limitations.html#fnref7)




---

## 6.2 Key principles[](judgmental-principles.html#judgmental-principles)

Using a systematic and well structured approach in judgmental forecasting helps to reduce the adverse effects of the limitations of judgmental forecasting, some of which we listed in the previous section. Whether this approach involves one individual or many, the following principles should be followed.

### Set the forecasting task clearly and concisely[](judgmental-principles.html#set-the-forecasting-task-clearly-and-concisely)

Care is needed when setting the forecasting challenges and expressing the forecasting tasks. It is important that everyone be clear about what the task is. All definitions should be clear and comprehensive, avoiding ambiguous and vague expressions. Also, it is important to avoid incorporating emotive terms and irrelevant information that may distract the forecaster. In the Delphi method that follows (see Section [6.3](delphimethod.html#delphimethod)), it may sometimes be useful to conduct a preliminary round of information gathering before setting the forecasting task.

### Implement a systematic approach[](judgmental-principles.html#implement-a-systematic-approach)

Forecast accuracy and consistency can be improved by using a systematic approach to judgmental forecasting involving checklists of categories of information which are relevant to the forecasting task. For example, it is helpful to identify what information is important and how this information is to be weighted. When forecasting the demand for a new product, what factors should we account for and how should we account for them? Should it be the price, the quality and/or quantity of the competition, the economic environment at the time, the target population of the product? It is worthwhile to devote significant effort and resources to put together decision rules that will lead to the best possible systematic approach.

### Document and justify[](judgmental-principles.html#document-and-justify)

Formalising and documenting the decision rules and assumptions implemented in the systematic approach can promote consistency, as the same rules can be implemented repeatedly. Also, requesting a forecaster to document and justify their forecasts leads to accountability, which can lead to reduced bias. Furthermore, formal documentation aids significantly in the systematic evaluation process that is suggested next.

### Systematically evaluate forecasts[](judgmental-principles.html#systematically-evaluate-forecasts)

Systematically monitoring the forecasting process can identify unforeseen irregularities. In particular, keep records of forecasts and use them to obtain feedback when the corresponding observations become available. Although you may do your best as a forecaster, the environment you operate in is dynamic. Changes occur, and you need to monitor these in order to evaluate the decision rules and assumptions. Feedback and evaluation help forecasters learn and improve their forecast accuracy.

### Segregate forecasters and users[](judgmental-principles.html#segregate-forecasters-and-users)

Forecast accuracy may be impeded if the forecasting task is carried out by users of the forecasts, such as those responsible for implementing plans of action about which the forecast is concerned. We should clarify again here (as in Section [1.2](planning.html#planning)), that forecasting is about predicting the future as accurately as possible, given all of the information available, including historical data and knowledge of any future events that may impact the forecasts. Forecasters and users should be clearly segregated. A classic case is that of a new product being launched. The forecast should be a reasonable estimate of the sales volume of a new product, which may differ considerably from what management expects or hopes the sales will be in order to meet company financial objectives. In this case, a forecaster may be delivering a reality check to the user.

It is important that forecasters communicate forecasts to potential users thoroughly. As we will see in Section [6.7](judgmental-adjustments.html#judgmental-adjustments), users may feel distant and disconnected from forecasts, and may not have full confidence in them. Explaining and clarifying the process and justifying the basic assumptions that led to the forecasts will provide some assurance to users.

The way in which forecasts may then be used and implemented will clearly depend on managerial decision making. For example, management may decide to adjust a forecast upwards (be over-optimistic), as the forecast may be used to guide purchasing and stock keeping levels. Such a decision may be taken after a cost-benefit analysis reveals that the cost of holding excess stock is much lower than that of lost sales. This type of adjustment should be part of setting goals or planning supply, rather than part of the forecasting process. In contrast, if forecasts are used as targets, they may be set low so that they can be exceeded more easily. Again, setting targets is different from producing forecasts, and the two should not be confused.

The example that follows comes from our experience in industry. It exemplifies two contrasting styles of judgmental forecasting — one that adheres to the principles we have just presented and one that does not.

### Example: Pharmaceutical Benefits Scheme (PBS)[](judgmental-principles.html#example-pharmaceutical-benefits-scheme-pbs)

The Australian government subsidises the cost of a wide range of prescription medicines as part of the PBS. Each subsidised medicine falls into one of four categories: concession copayments, concession safety net, general copayments, and general safety net. Each person with a concession card makes a concession copayment per PBS medicine ($5.80)[8](judgmental-principles.html#fn8), until they reach a set threshold amount labelled the concession safety net ($348). For the rest of the financial year, all PBS-listed medicines are free. Each general patient makes a general copayment per PBS medicine ($35.40) until the general safety net amount is reached ($1,363.30). For the rest of the financial year, they contribute a small amount per PBS-listed medicine ($5.80). The PBS forecasting process uses 84 groups of PBS-listed medicines, and produces forecasts of the medicine volume and the total expenditure for each group and for each of the four PBS categories, a total of 672 series. This forecasting process aids in setting the government budget allocated to the PBS, which is over $7 billion per year, or approximately 1% of GDP.

Figure 6.1: Process for producing PBS forecasts. 

Figure [6.1](judgmental-principles.html#fig:pbsdiagram) summarises the forecasting process. Judgmental forecasts are generated for new listings of medicines and for estimating the impact of new policies. These are shown by the green items. The pink items indicate the data used which were obtained from various government departments and associated authorities. The blue items show things that are calculated from the data provided. There were judgmental adjustments to the data to take account of new listings and new policies, and there were also judgmental adjustments to the forecasts. Because of the changing size of both the concession population and the total population, forecasts are produced on a per-capita basis, and then multiplied by the forecast population to obtain forecasts of total volume and expenditure per month.

One of us (Hyndman) was asked to evaluate the forecasting process a few years ago. We found that using judgment for new listings and new policy impacts gave better forecasts than using a statistical model alone. However, we also found that the forecasting accuracy and consistency could be improved through a more structured and systematic process, especially for policy impacts.

_Forecasting new listings:_ Companies who apply for their medicine to be added to the PBS are asked to submit detailed forecasts for various aspects of the medicine, such as projected patient numbers, market share of the new medicine, substitution effects, etc. The Pharmaceutical Benefits Advisory Committee provides guidelines describing a highly structured and systematic approach for generating these forecasts, and requires careful documentation for each step of the process. This structured process helps to reduce the likelihood and effects of deliberate self-serving biases. Two detailed evaluation rounds of the company forecasts are implemented by a sub-committee, one before the medicine is added to the PBS and one after it is added. Finally, comparisons of observations versus forecasts for some selected new listings are performed, 12 months and 24 months after the listings, and the results are sent back to the companies for comment.

_Policy impact forecasts:_ In contrast to the highly structured process used for new listings, there were no systematic procedures for policy impact forecasts. On many occasions, forecasts of policy impacts were calculated by a small team, and were often heavily reliant on the work of one person. The forecasts were not usually subject to a formal review process. There were no guidelines for how to construct judgmental forecasts for policy impacts, and there was often a lack of adequate documentation about how these forecasts were obtained, the assumptions underlying them, etc.

Consequently, we recommended several changes:

  * that guidelines for forecasting new policy impacts be developed, to encourage a more systematic and structured forecasting approach;
  * that the forecast methodology be documented in each case, including all assumptions made in forming the forecasts;
  * that new policy forecasts be made by at least two people from different areas of the organisation;
  * that a review of forecasts be conducted one year after the implementation of each new policy by a review committee, especially for new policies that have a significant annual projected cost or saving. The review committee should include those involved in generating the forecasts, but also others.


These recommendations reflect the principles outlined in this section.

* * *

  8. These are Australian dollar amounts published by the Australian government for 2012.[↩︎](judgmental-principles.html#fnref8)




---

## 6.3 The Delphi method[](delphimethod.html#delphimethod)

The Delphi method was invented by Olaf Helmer and Norman Dalkey of the Rand Corporation in the 1950s for the purpose of addressing a specific military problem. The method relies on the key assumption that forecasts from a group are generally more accurate than those from individuals. The aim of the Delphi method is to construct consensus forecasts from a group of experts in a structured iterative manner. A facilitator is appointed in order to implement and manage the process. The Delphi method generally involves the following stages:

  1. A panel of experts is assembled.
  2. Forecasting tasks/challenges are set and distributed to the experts.
  3. Experts return initial forecasts and justifications. These are compiled and summarised in order to provide feedback.
  4. Feedback is provided to the experts, who now review their forecasts in light of the feedback. This step may be iterated until a satisfactory level of consensus is reached.
  5. Final forecasts are constructed by aggregating the experts’ forecasts.


Each stage of the Delphi method comes with its own challenges. In what follows, we provide some suggestions and discussions about each one of these.[9](delphimethod.html#fn9)

### Experts and anonymity[](delphimethod.html#experts-and-anonymity)

The first challenge of the facilitator is to identify a group of experts who can contribute to the forecasting task. The usual suggestion is somewhere between 5 and 20 experts with diverse expertise. Experts submit forecasts and also provide detailed qualitative justifications for these.

A key feature of the Delphi method is that the participating experts remain anonymous at all times. This means that the experts cannot be influenced by political and social pressures in their forecasts. Furthermore, all experts are given an equal say and all are held accountable for their forecasts. This avoids the situation where a group meeting is held and some members do not contribute, while others dominate. It also prevents members exerting undue influence based on seniority or personality. There have been suggestions that even something as simple as the seating arrangements in a group setting can influence the group dynamics. Furthermore, there is ample evidence that a group meeting setting promotes enthusiasm and influences individual judgment, leading to optimism and overconfidence.[10](delphimethod.html#fn10)

A by-product of anonymity is that the experts do not need to meet as a group in a physical location. An important advantage of this is that it increases the likelihood of gathering experts with diverse skills and expertise from varying locations. Furthermore, it makes the process cost-effective by eliminating the expense and inconvenience of travel, and it makes it flexible, as the experts only have to meet a common deadline for submitting forecasts, rather than having to set a common meeting time.

### Setting the forecasting task in a Delphi[](delphimethod.html#setting-the-forecasting-task-in-a-delphi)

In a Delphi setting, it may be useful to conduct a preliminary round of information gathering from the experts before setting the forecasting tasks. Alternatively, as experts submit their initial forecasts and justifications, valuable information which is not shared between all experts can be identified by the facilitator when compiling the feedback.

### Feedback[](delphimethod.html#feedback)

Feedback to the experts should include summary statistics of the forecasts and outlines of qualitative justifications. Numerical data summaries and graphical representations can be used to summarise the experts’ forecasts.

As the feedback is controlled by the facilitator, there may be scope to direct attention and information from the experts to areas where it is most required. For example, the facilitator may direct the experts’ attention to responses that fall outside the interquartile range, and the qualitative justification for such forecasts.

### Iteration[](delphimethod.html#iteration)

The process of the experts submitting forecasts, receiving feedback, and reviewing their forecasts in light of the feedback, is repeated until a satisfactory level of consensus between the experts is reached. Satisfactory consensus does not mean complete convergence in the forecast value; it simply means that the variability of the responses has decreased to a satisfactory level. Usually two or three rounds are sufficient. Experts are more likely to drop out as the number of iterations increases, so too many rounds should be avoided.

### Final forecasts[](delphimethod.html#final-forecasts)

The final forecasts are usually constructed by giving equal weight to all of the experts’ forecasts. However, the facilitator should keep in mind the possibility of extreme values which can distort the final forecast.

### Limitations and variations[](delphimethod.html#limitations-and-variations)

Applying the Delphi method can be time consuming. In a group meeting, final forecasts can possibly be reached in hours or even minutes — something which is almost impossible to do in a Delphi setting. If it is taking a long time to reach a consensus in a Delphi setting, the panel may lose interest and cohesiveness.

In a group setting, personal interactions can lead to quicker and better clarifications of qualitative justifications. A variation of the Delphi method which is often applied is the “estimate-talk-estimate” method, where the experts can interact between iterations, although the forecast submissions can still remain anonymous. A disadvantage of this variation is the possibility of the loudest person exerting undue influence.

### The facilitator[](delphimethod.html#the-facilitator)

The role of the facilitator is of the utmost importance. The facilitator is largely responsible for the design and administration of the Delphi process. The facilitator is also responsible for providing feedback to the experts and generating the final forecasts. In this role, the facilitator needs to be experienced enough to recognise areas that may need more attention, and to direct the experts’ attention to these. Also, as there is no face-to-face interaction between the experts, the facilitator is responsible for disseminating important information. The efficiency and effectiveness of the facilitator can dramatically increase the probability of a successful Delphi method in a judgmental forecasting setting.

### Bibliography[](bibliography.html#bibliography)

Buehler, R., Messervey, D., & Griffin, D. (2005). Collaborative planning and prediction: Does group discussion affect optimistic biases in time estimation? _Organizational Behavior and Human Decision Processes_ , _97_(1), 47–63. [__](https://doi.org/10.1016/j.obhdp.2005.02.004)

Rowe, G. (2007). A guide to Delphi. _Foresight: The International Journal of Applied Forecasting_ , _8_ , 11–16. 

Rowe, G., & Wright, G. (1999). The Delphi technique as a forecasting tool: Issues and analysis. _International Journal of Forecasting_ , _15_(4), 353–375. [__](https://doi.org/10.1016/S0169-2070\(99\)00018-7)

* * *

  9. For further reading, refer to: Rowe ([2007](delphimethod.html#ref-Rowe2007)); Rowe & Wright ([1999](delphimethod.html#ref-RW99))[↩︎](delphimethod.html#fnref9)

  10. Buehler et al. ([2005](delphimethod.html#ref-Buehler2005))[↩︎](delphimethod.html#fnref10)




---

## 6.4 Forecasting by analogy[](analogies.html#analogies)

A useful judgmental approach which is often implemented in practice is forecasting by analogy. A common example is the pricing of a house through an appraisal process. An appraiser estimates the market value of a house by comparing it to similar properties that have sold in the area. The degree of similarity depends on the attributes considered. With house appraisals, attributes such as land size, dwelling size, numbers of bedrooms and bathrooms, and garage space are usually considered.

Even thinking and discussing analogous products or situations can generate useful (and sometimes crucial) information. We illustrate this point with the following example.[11](analogies.html#fn11)

### Example: Designing a high school curriculum[](analogies.html#example-designing-a-high-school-curriculum)

A small group of academics and teachers were assigned the task of developing a curriculum for teaching judgment and decision making under uncertainty for high schools in Israel. Each group member was asked to forecast how long it would take for the curriculum to be completed. Responses ranged between 18 and 30 months. One of the group members who was an expert in curriculum design was asked to consider analogous curricula developments around the world. He concluded that 40% of analogous groups he considered never completed the task. The rest took between 7 to 10 years. The Israel project was completed in 8 years.

Obviously, forecasting by analogy comes with challenges. We should aspire to base forecasts on multiple analogies rather than a single analogy, which may create biases. However, these may be challenging to identify. Similarly, we should aspire to consider multiple attributes. Identifying or even comparing these may not always be straightforward. As always, we suggest performing these comparisons and the forecasting process using a systematic approach. Developing a detailed scoring mechanism to rank attributes and record the process of ranking will always be useful.

### A structured analogy[](analogies.html#a-structured-analogy)

Alternatively, a structured approach comprising a panel of experts can be implemented, as was proposed by Green & Armstrong ([2007](analogies.html#ref-Green2007)). The concept is similar to that of a Delphi; however, the forecasting task is completed by considering analogies. First, a facilitator is appointed. Then the structured approach involves the following steps.

  1. A panel of experts who are likely to have experience with analogous situations is assembled.
  2. Tasks/challenges are set and distributed to the experts.
  3. Experts identify and describe as many analogies as they can, and generate forecasts based on each analogy.
  4. Experts list similarities and differences of each analogy to the target situation, then rate the similarity of each analogy to the target situation on a scale.
  5. Forecasts are derived by the facilitator using a set rule. This can be a weighted average, where the weights can be guided by the ranking scores of each analogy by the experts.


As with the Delphi approach, anonymity of the experts may be an advantage in not suppressing creativity, but could hinder collaboration. Green and Armstrong found no gain in collaboration between the experts in their results. A key finding was that experts with multiple analogies (more than two), and who had direct experience with the analogies, generated the most accurate forecasts.

### Bibliography[](bibliography.html#bibliography)

Green, K. C., & Armstrong, J. S. (2007). Structured analogies for forecasting. _International Journal of Forecasting_ , _23_(3), 365–376. [__](https://doi.org/10.1016/j.ijforecast.2007.05.005)

Kahneman, D., & Lovallo, D. (1993). Timid choices and bold forecasts: A cognitive perspective on risk taking. _Management Science_ , _39_(1), 17–31. [__](https://doi.org/10.1287/mnsc.39.1.17)

* * *

  11. This example is extracted from Kahneman & Lovallo ([1993](analogies.html#ref-Kahneman1993))[↩︎](analogies.html#fnref11)




---

## 6.5 Scenario forecasting[](scenarios.html#scenarios)

A fundamentally different approach to judgmental forecasting is scenario-based forecasting. The aim of this approach is to generate forecasts based on plausible scenarios. In contrast to the two previous approaches (Delphi and forecasting by analogy) where the resulting forecast is intended to be a likely outcome, each scenario-based forecast may have a low probability of occurrence. The scenarios are generated by considering all possible factors or drivers, their relative impacts, the interactions between them, and the targets to be forecast.

Building forecasts based on scenarios allows a wide range of possible forecasts to be generated and some extremes to be identified. For example it is usual for “best”, “middle” and “worst” case scenarios to be presented, although many other scenarios will be generated. Thinking about and documenting these contrasting extremes can lead to early contingency planning.

With scenario forecasting, decision makers often participate in the generation of scenarios. While this may lead to some biases, it can ease the communication of the scenario-based forecasts, and lead to a better understanding of the results.


---

## 6.6 New product forecasting[](new-products.html#new-products)

The definition of a new product can vary. It may be an entirely new product which has been launched, a variation of an existing product (“new and improved”), a change in the pricing scheme of an existing product, or even an existing product entering a new market.

Judgmental forecasting is usually the only available method for new product forecasting, as historical data are unavailable. The approaches we have already outlined (Delphi, forecasting by analogy and scenario forecasting) are all applicable when forecasting the demand for a new product.

Other methods which are more specific to the situation are also available. We briefly describe three such methods which are commonly applied in practice. These methods are less structured than those already discussed, and are likely to lead to more biased forecasts as a result.

### Sales force composite[](new-products.html#sales-force-composite)

In this approach, forecasts for each outlet/branch/store of a company are generated by salespeople, and are then aggregated. This usually involves sales managers forecasting the demand for the outlet they manage. Salespeople are usually closest to the interaction between customers and products, and often develop an intuition about customer purchasing intentions. They bring this valuable experience and expertise to the forecast.

However, having salespeople generate forecasts violates the key principle of segregating forecasters and users, which can create biases in many directions. It is common for the performance of a salesperson to be evaluated against the sales forecasts or expectations set beforehand. In this case, the salesperson acting as a forecaster may introduce some self-serving bias by generating low forecasts. On the other hand, one can imagine an enthusiastic salesperson, full of optimism, generating high forecasts.

Moreover a successful salesperson is not necessarily a successful nor well-informed forecaster. A large proportion of salespeople will have no or limited formal training in forecasting. Finally, salespeople will feel customer displeasure at first hand if, for example, the product runs out or is not introduced in their store. Such interactions will cloud their judgment.

### Executive opinion[](new-products.html#executive-opinion)

In contrast to the sales force composite, this approach involves staff at the top of the managerial structure generating aggregate forecasts. Such forecasts are usually generated in a group meeting, where executives contribute information from their own area of the company. Having executives from different functional areas of the company promotes great skill and knowledge diversity in the group.

This process carries all of the advantages and disadvantages of a group meeting setting which we discussed earlier. In this setting, it is important to justify and document the forecasting process. That is, executives need to be held accountable in order to reduce the biases generated by the group meeting setting. There may also be scope to apply variations to a Delphi approach in this setting; for example, the estimate-talk-estimate process described earlier.

### Customer intentions[](new-products.html#customer-intentions)

Customer intentions can be used to forecast the demand for a new product or for a variation on an existing product. Questionnaires are filled in by customers on their intentions to buy the product. A structured questionnaire is used, asking customers to rate the likelihood of them purchasing the product on a scale; for example, highly likely, likely, possible, unlikely, highly unlikely.

Survey design challenges, such as collecting a representative sample, applying a time- and cost-effective method, and dealing with non-responses, need to be addressed.[12](new-products.html#fn12)

Furthermore, in this survey setting we must keep in mind the relationship between purchase intention and purchase behaviour. Customers do not always do what they say they will. Many studies have found a positive correlation between purchase intentions and purchase behaviour; however, the strength of these correlations varies substantially. The factors driving this variation include the timings of data collection and product launch, the definition of “new” for the product, and the type of industry. Behavioural theory tells us that intentions predict behaviour if the intentions are measured just before the behaviour.[13](new-products.html#fn13) The time between intention and behaviour will vary depending on whether it is a completely new product or a variation on an existing product. Also, the correlation between intention and behaviour is found to be stronger for variations on existing and familiar products than for completely new products.

Whichever method of new product forecasting is used, it is important to thoroughly document the forecasts made, and the reasoning behind them, in order to be able to evaluate them when data become available.

### Bibliography[](bibliography.html#bibliography)

Groves, R. M., Fowler, F. J., Couper, M. P., Lepkowski, J. M., Singer, E., & Tourangeau, R. (2009). _Survey methodology_ (2nd ed). John Wiley & Sons. [__](http://amazon.com/dp/0470465468?tag=otexts20)

Randall, D. M., & Wolff, J. A. (1994). The time interval in the intention-behaviour relationship: Meta-analysis. _British Journal of Social Psychology_ , _33_(4), 405–418. [__](https://doi.org/10.1111/j.2044-8309.1994.tb01037.x)

* * *

  12. Groves et al. ([2009](new-products.html#ref-Groves2009))[↩︎](new-products.html#fnref12)

  13. Randall & Wolff ([1994](new-products.html#ref-RW94))[↩︎](new-products.html#fnref13)




---

## 6.7 Judgmental adjustments[](judgmental-adjustments.html#judgmental-adjustments)

In this final section, we consider the situation where historical data are available and are used to generate statistical forecasts. It is common for practitioners to then apply judgmental adjustments to these forecasts. These adjustments can potentially provide all of the advantages of judgmental forecasting which have been discussed earlier in this chapter. For example, they provide an avenue for incorporating factors that may not be accounted for in the statistical model, such as promotions, large sporting events, holidays, or recent events that are not yet reflected in the data. However, these advantages come to fruition only when the right conditions are present. Judgmental adjustments, like judgmental forecasts, come with biases and limitations, and we must implement methodical strategies in order to minimise them.

### Use adjustments sparingly[](judgmental-adjustments.html#use-adjustments-sparingly)

Practitioners adjust much more often than they should, and many times for the wrong reasons. By adjusting statistical forecasts, users of forecasts create a feeling of ownership and credibility. Users often do not understand or appreciate the mechanisms that generate the statistical forecasts (as they will usually have no training in this area). By implementing judgmental adjustments, users feel that they have contributed to and completed the forecasts, and they can now relate their own intuition and interpretations to these. The forecasts have become their own.

Judgmental adjustments should not aim to correct for a systematic pattern in the data that is thought to have been missed by the statistical model. This has been proven to be ineffective, as forecasters tend to read non-existent patterns in noisy series. Statistical models are much better at taking account of data patterns, and judgmental adjustments only hinder accuracy.

Judgmental adjustments are most effective when there is significant additional information at hand or strong evidence of the need for an adjustment. We should only adjust when we have important extra information which is not incorporated in the statistical model. Hence, adjustments seem to be most accurate when they are large in size. Small adjustments (especially in the positive direction promoting the illusion of optimism) have been found to hinder accuracy, and should be avoided.

### Apply a structured approach[](judgmental-adjustments.html#apply-a-structured-approach)

Using a structured and systematic approach will improve the accuracy of judgmental adjustments. Following the key principles outlined in Section [6.2](judgmental-principles.html#judgmental-principles) is vital. In particular, having to document and justify adjustments will make it more challenging to override the statistical forecasts, and will guard against unnecessary adjustments.

It is common for adjustments to be implemented by a panel (see the example that follows). Using a Delphi setting carries great advantages. However, if adjustments are implemented in a group meeting, it is wise to consider the forecasts of key markets or products first, as panel members will get tired during this process. Fewer adjustments tend to be made as the meeting goes on through the day.

### Example: Tourism Forecasting Committee (TFC)[](judgmental-adjustments.html#example-tourism-forecasting-committee-tfc)

Tourism Australia publishes forecasts for all aspects of Australian tourism twice a year. The published forecasts are generated by the TFC, an independent body which comprises experts from various government and industry sectors; for example, the Australian Commonwealth Treasury, airline companies, consulting firms, banking sector companies, and tourism bodies.

The forecasting methodology applied is an iterative process. First, model-based statistical forecasts are generated by the forecasting unit within Tourism Australia, then judgmental adjustments are made to these in two rounds. In the first round, the TFC Technical Committee[14](judgmental-adjustments.html#fn14) (comprising senior researchers, economists and independent advisers) adjusts the model-based forecasts. In the second and final round, the TFC (comprising industry and government experts) makes final adjustments. In both rounds, adjustments are made by consensus.

Figure 6.2: Long run annual forecasts for domestic visitor nights for Australia. We study regression models in Chapter [7](regression.html#regression), and ETS (ExponenTial Smoothing) models in Chapter [8](expsmooth.html#expsmooth). 

In 2008, we[15](judgmental-adjustments.html#fn15) analysed forecasts for Australian domestic tourism. We concluded that the published TFC forecasts were optimistic, especially for the long-run, and we proposed alternative model-based forecasts. We now have access to observed data up to and including 2011. In Figure [6.2](judgmental-adjustments.html#fig:tfc), we plot the published forecasts against the actual data. We can see that the published TFC forecasts have continued to be optimistic.

What can we learn from this example? Although the TFC clearly states in its methodology that it produces ‘forecasts’ rather than ‘targets’, could this be a case where these have been confused? Are the forecasters and users sufficiently well-segregated in this process? Could the iterative process itself be improved? Could the adjustment process in the meetings be improved? Could it be that the group meetings have promoted optimism? Could it be that domestic tourism should have been considered earlier in the day?

### Bibliography[](bibliography.html#bibliography)

Athanasopoulos, G., & Hyndman, R. J. (2008). Modelling and forecasting Australian domestic tourism. _Tourism Management_ , _29_(1), 19–31. [__](https://doi.org/10.1016/j.tourman.2007.04.009)

* * *

  14. Athanasopoulos was an observer on this technical committee for a few years.[↩︎](judgmental-adjustments.html#fnref14)

  15. Athanasopoulos & Hyndman ([2008](judgmental-adjustments.html#ref-austourism))[↩︎](judgmental-adjustments.html#fnref15)




---

## 6.8 Further reading[](judgmental-reading.html#judgmental-reading)

Many forecasting textbooks ignore judgmental forecasting altogether. Here are three which do cover it in some detail.

  * Chapter 11 of Ord et al. ([2017](judgmental-reading.html#ref-Ord2017)) provides an excellent review of some of the same topics as this chapter, but also includes using judgment to assessing forecast uncertainty, and forecasting using prediction markets.
  * Goodwin & Wright ([2009](judgmental-reading.html#ref-GW04)) is a book-length treatment of the use of judgment in decision making by two of the leading researchers in the field.
  * Kahn ([2006](judgmental-reading.html#ref-Kahn2006)) covers techniques for new product forecasting, where judgmental methods play an important role.


There have been some helpful survey papers on judgmental forecasting published in the last 20 years. We have found these three particularly helpful.

  * Fildes & Goodwin ([2007b](judgmental-reading.html#ref-Fildes2007a))
  * Fildes & Goodwin ([2007a](judgmental-reading.html#ref-Fildes2007))
  * Harvey ([2001](judgmental-reading.html#ref-Harvey2001))


Some helpful papers on individual judgmental forecasting methods are listed in the table below.

**Forecasting Method** | **Recommended papers**  
---|---  
Delphi | Rowe & Wright ([1999](judgmental-reading.html#ref-RW99))  
| Rowe ([2007](judgmental-reading.html#ref-Rowe2007))  
Adjustments | Sanders et al. ([2005](judgmental-reading.html#ref-Sanders2005))  
| Eroglu & Croxton ([2010](judgmental-reading.html#ref-Eroglu2010))  
| Franses & Legerstee ([2013](judgmental-reading.html#ref-Franses2013))  
Analogy | Green & Armstrong ([2007](judgmental-reading.html#ref-Green2007))  
Scenarios | Önkal et al. ([2013](judgmental-reading.html#ref-Onkal2012))  
Customer intentions | Morwitz et al. ([2007](judgmental-reading.html#ref-Morwitz2007))  
  
### Bibliography[](bibliography.html#bibliography)

Eroglu, C., & Croxton, K. L. (2010). Biases in judgmental adjustments of statistical forecasts: The role of individual differences. _International Journal of Forecasting_ , _26_(1), 116–133. [__](https://doi.org/10.1016/j.ijforecast.2009.02.005)

Fildes, R., & Goodwin, P. (2007a). Against your better judgment? How organizations can improve their use of management judgment in forecasting. _Interfaces_ , _37_(6), 570–576. [__](https://doi.org/10.1287/inte.1070.0309)

Fildes, R., & Goodwin, P. (2007b). Good and bad judgment in forecasting: Lessons from four companies. _Foresight: The International Journal of Applied Forecasting_ , _8_ , 5–10. 

Franses, P. H., & Legerstee, R. (2013). Do statistical forecasting models for SKU-level data benefit from including past expert knowledge? _International Journal of Forecasting_ , _29_(1), 80–87. [__](https://doi.org/10.1016/j.ijforecast.2012.05.008)

Goodwin, P., & Wright, G. (2009). _Decision analysis for management judgment_ (4th ed). John Wiley & Sons. [__](http://amazon.com/dp/0470714395?tag=otexts20)

Green, K. C., & Armstrong, J. S. (2007). Structured analogies for forecasting. _International Journal of Forecasting_ , _23_(3), 365–376. [__](https://doi.org/10.1016/j.ijforecast.2007.05.005)

Harvey, N. (2001). Improving judgment in forecasting. In J. S. Armstrong (Ed.), _Principles of forecasting: A handbook for researchers and practitioners_ (pp. 59–80). Kluwer Academic Publishers. [__](https://doi.org/10.1007/978-0-306-47630-3_4)

Kahn, K. B. (2006). _New product forecasting: An applied approach_. M.E. Sharp. [__](http://amazon.com/dp/0765616092?tag=otexts20)

Morwitz, V. G., Steckel, J. H., & Gupta, A. (2007). When do purchase intentions predict sales? _International Journal of Forecasting_ , _23_(3), 347–364. [__](https://doi.org/10.1016/j.ijforecast.2007.05.015)

Önkal, D., Sayım, K. Z., & Gönül, M. S. (2013). Scenarios as channels of forecast advice. _Technological Forecasting and Social Change_ , _80_(4), 772–788. [__](https://doi.org/10.1016/j.techfore.2012.08.015)

Ord, J. K., Fildes, R., & Kourentzes, N. (2017). _Principles of business forecasting_ (2nd ed.). Wessex Press Publishing Co. [__](http://amazon.com/dp/0999064916?tag=otexts20)

Rowe, G. (2007). A guide to Delphi. _Foresight: The International Journal of Applied Forecasting_ , _8_ , 11–16. 

Rowe, G., & Wright, G. (1999). The Delphi technique as a forecasting tool: Issues and analysis. _International Journal of Forecasting_ , _15_(4), 353–375. [__](https://doi.org/10.1016/S0169-2070\(99\)00018-7)

Sanders, N., Goodwin, P., Önkal, D., Gönül, M. S., Harvey, N., Lee, A., & Kjolso, L. (2005). When and how should statistical forecasts be judgmentally adjusted? _Foresight: The International Journal of Applied Forecasting_ , _1_(1), 5–23. 


---

# Chapter 7 Time series regression models[](regression.html#regression)

In this chapter we discuss regression models. The basic concept is that we forecast the time series of interest \\(y\\) assuming that it has a linear relationship with other time series \\(x\\).

For example, we might wish to forecast monthly sales \\(y\\) using total advertising spend \\(x\\) as a predictor. Or we might forecast daily electricity demand \\(y\\) using temperature \\(x_1\\) and the day of week \\(x_2\\) as predictors.

The **forecast variable** \\(y\\) is sometimes also called the regressand, dependent or explained variable. The **predictor variables** \\(x\\) are sometimes also called the regressors, independent or explanatory variables. In this book we will always refer to them as the “forecast” variable and “predictor” variables.


---

## 7.1 The linear model[](regression-intro.html#regression-intro)

### Simple linear regression[](regression-intro.html#simple-linear-regression)

In the simplest case, the regression model allows for a linear relationship between the forecast variable \\(y\\) and a single predictor variable \\(x\\): \\[ y_t = \beta_0 + \beta_1 x_t + \varepsilon_t. \\] An artificial example of data from such a model is shown in Figure [7.1](regression-intro.html#fig:SLRpop1). The coefficients \\(\beta_0\\) and \\(\beta_1\\) denote the intercept and the slope of the line respectively. The intercept \\(\beta_0\\) represents the predicted value of \\(y\\) when \\(x=0\\). The slope \\(\beta_1\\) represents the average predicted change in \\(y\\) resulting from a one unit increase in \\(x\\).

Figure 7.1: An example of data from a simple linear regression model. 

Notice that the observations do not lie on the straight line but are scattered around it. We can think of each observation \\(y_t\\) as consisting of the systematic or explained part of the model, \\(\beta_0+\beta_1x_t\\), and the random “error”, \\(\varepsilon_t\\). The “error” term does not imply a mistake, but a deviation from the underlying straight line model. It captures anything that may affect \\(y_t\\) other than \\(x_t\\).

### Example: US consumption expenditure[](regression-intro.html#example-us-consumption-expenditure)

Figure [7.2](regression-intro.html#fig:ConsInc) shows time series of quarterly percentage changes (growth rates) of real personal consumption expenditure, \\(y\\), and real personal disposable income, \\(x\\), for the US from 1970 Q1 to 2019 Q2.
    
    
    [](regression-intro.html#cb133-1)us_change |>
    [](regression-intro.html#cb133-2)  pivot_longer(c(Consumption, Income), names_to="Series") |>
    [](regression-intro.html#cb133-3)  autoplot(value) +
    [](regression-intro.html#cb133-4)  labs(y = "% change")

Figure 7.2: Percentage changes in personal consumption expenditure and personal income for the US. 

A scatter plot of consumption changes against income changes is shown in Figure [7.3](regression-intro.html#fig:ConsInc2) along with the estimated regression line

\\[ \hat{y}_t=0.54 + 0.27x_t. \\] (We put a “hat” above \\(y\\) to indicate that this is the value of \\(y\\) predicted by the model.)
    
    
    [](regression-intro.html#cb134-1)us_change |>
    [](regression-intro.html#cb134-2)  ggplot(aes(x = Income, y = Consumption)) +
    [](regression-intro.html#cb134-3)  labs(y = "Consumption (quarterly % change)",
    [](regression-intro.html#cb134-4)       x = "Income (quarterly % change)") +
    [](regression-intro.html#cb134-5)  geom_point() +
    [](regression-intro.html#cb134-6)  geom_smooth(method = "lm", se = FALSE)

Figure 7.3: Scatterplot of quarterly changes in consumption expenditure versus quarterly changes in personal income and the fitted regression line. 

The equation is estimated using the `TSLM()` function:
    
    
    [](regression-intro.html#cb135-1)us_change |>
    [](regression-intro.html#cb135-2)  model(TSLM(Consumption ~ Income)) |>
    [](regression-intro.html#cb135-3)  report()
    [](regression-intro.html#cb135-4)#> Series: Consumption 
    [](regression-intro.html#cb135-5)#> Model: TSLM 
    [](regression-intro.html#cb135-6)#> 
    [](regression-intro.html#cb135-7)#> Residuals:
    [](regression-intro.html#cb135-8)#>     Min      1Q  Median      3Q     Max 
    [](regression-intro.html#cb135-9)#> -2.5824 -0.2778  0.0186  0.3233  1.4223 
    [](regression-intro.html#cb135-10)#> 
    [](regression-intro.html#cb135-11)#> Coefficients:
    [](regression-intro.html#cb135-12)#>             Estimate Std. Error t value Pr(>|t|)    
    [](regression-intro.html#cb135-13)#> (Intercept)   0.5445     0.0540   10.08  < 2e-16 ***
    [](regression-intro.html#cb135-14)#> Income        0.2718     0.0467    5.82  2.4e-08 ***
    [](regression-intro.html#cb135-15)#> ---
    [](regression-intro.html#cb135-16)#> Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    [](regression-intro.html#cb135-17)#> 
    [](regression-intro.html#cb135-18)#> Residual standard error: 0.591 on 196 degrees of freedom
    [](regression-intro.html#cb135-19)#> Multiple R-squared: 0.147,   Adjusted R-squared: 0.143
    [](regression-intro.html#cb135-20)#> F-statistic: 33.8 on 1 and 196 DF, p-value: 2.4e-08

We will discuss how `TSLM()` computes the coefficients in Section [7.2](least-squares.html#least-squares).

The fitted line has a positive slope, reflecting the positive relationship between income and consumption. The slope coefficient shows that a one unit increase in \\(x\\) (a 1 percentage point increase in personal disposable income) results on average in 0.27 units increase in \\(y\\) (an average increase of 0.27 percentage points in personal consumption expenditure). Alternatively the estimated equation shows that a value of 1 for \\(x\\) (the percentage increase in personal disposable income) will result in a forecast value of \\(0.54 + 0.27 \times 1 = 0.82\\) for \\(y\\) (the percentage increase in personal consumption expenditure).

The interpretation of the intercept requires that a value of \\(x=0\\) makes sense. In this case when \\(x=0\\) (i.e., when there is no change in personal disposable income since the last quarter) the predicted value of \\(y\\) is 0.54 (i.e., an average increase in personal consumption expenditure of 0.54%). Even when \\(x=0\\) does not make sense, the intercept is an important part of the model. Without it, the slope coefficient can be distorted unnecessarily. The intercept should always be included unless the requirement is to force the regression line “through the origin”. In what follows we assume that an intercept is always included in the model.

### Multiple linear regression[](regression-intro.html#multiple-linear-regression)

When there are two or more predictor variables, the model is called a **multiple regression model**. The general form of a multiple regression model is \\[\begin{equation} y_t = \beta_{0} + \beta_{1} x_{1,t} + \beta_{2} x_{2,t} + \cdots + \beta_{k} x_{k,t} + \varepsilon_t, \tag{7.1} \end{equation}\\] where \\(y\\) is the variable to be forecast and \\(x_{1},\dots,x_{k}\\) are the \\(k\\) predictor variables. Each of the predictor variables must be numerical. The coefficients \\(\beta_{1},\dots,\beta_{k}\\) measure the effect of each predictor after taking into account the effects of all the other predictors in the model. Thus, the coefficients measure the _marginal effects_ of the predictor variables.

### Example: US consumption expenditure[](regression-intro.html#example-us-consumption-expenditure-1)

Figure [7.4](regression-intro.html#fig:MultiPredictors) shows additional predictors that may be useful for forecasting US consumption expenditure. These are quarterly percentage changes in industrial production and personal savings, and quarterly changes in the unemployment rate (as this is already a percentage). Building a multiple linear regression model can potentially generate more accurate forecasts as we expect consumption expenditure to not only depend on personal income but on other predictors as well.
    
    
    [](regression-intro.html#cb136-1)us_change |>
    [](regression-intro.html#cb136-2)  select(-Consumption, -Income) |>
    [](regression-intro.html#cb136-3)  pivot_longer(-Quarter) |>
    [](regression-intro.html#cb136-4)  ggplot(aes(Quarter, value, colour = name)) +
    [](regression-intro.html#cb136-5)  geom_line() +
    [](regression-intro.html#cb136-6)  facet_grid(name ~ ., scales = "free_y") +
    [](regression-intro.html#cb136-7)  guides(colour = "none") +
    [](regression-intro.html#cb136-8)  labs(y="% change")

Figure 7.4: Quarterly percentage changes in industrial production and personal savings and quarterly changes in the unemployment rate for the US over the period 1970Q1-2019Q2. 

Figure [7.5](regression-intro.html#fig:ScatterMatrix) is a scatterplot matrix of five variables. The first column shows the relationships between the forecast variable (consumption) and each of the predictors. The scatterplots show positive relationships with income and industrial production, and negative relationships with savings and unemployment. The strength of these relationships are shown by the correlation coefficients across the first row. The remaining scatterplots and correlation coefficients show the relationships between the predictors.
    
    
    [](regression-intro.html#cb137-1)us_change |>
    [](regression-intro.html#cb137-2)  GGally::ggpairs(columns = 2:6)

Figure 7.5: A scatterplot matrix of US consumption expenditure and the four predictors. 

### Assumptions[](regression-intro.html#assumptions)

When we use a linear regression model, we are implicitly making some assumptions about the variables in Equation [(7.1)](regression-intro.html#eq:lm).

First, we assume that the model is a reasonable approximation to reality; that is, the relationship between the forecast variable and the predictor variables satisfies this linear equation.

Second, we make the following assumptions about the errors \\((\varepsilon_{1},\dots,\varepsilon_{T})\\):

  * they have mean zero; otherwise the forecasts will be systematically biased.
  * they are not autocorrelated; otherwise the forecasts will be inefficient, as there is more information in the data that can be exploited.
  * they are unrelated to the predictor variables; otherwise there would be more information that should be included in the systematic part of the model.


It is also useful to have the errors being normally distributed with a constant variance \\(\sigma^2\\) in order to easily produce prediction intervals.

Another important assumption in the linear regression model is that each predictor \\(x\\) is not a random variable. If we were performing a controlled experiment in a laboratory, we could control the values of each \\(x\\) (so they would not be random) and observe the resulting values of \\(y\\). With observational data (including most data in business and economics), it is not possible to control the value of \\(x\\), we simply observe it. Hence we make this an assumption.


---

## 7.2 Least squares estimation[](least-squares.html#least-squares)

In practice, of course, we have a collection of observations but we do not know the values of the coefficients \\(\beta_0,\beta_1, \dots, \beta_k\\). These need to be estimated from the data.

The least squares principle provides a way of choosing the coefficients effectively by minimising the sum of the squared errors. That is, we choose the values of \\(\beta_0, \beta_1, \dots, \beta_k\\) that minimise \\[ \sum_{t=1}^T \varepsilon_t^2 = \sum_{t=1}^T (y_t - \beta_{0} - \beta_{1} x_{1,t} - \beta_{2} x_{2,t} - \cdots - \beta_{k} x_{k,t})^2. \\]

This is called **least squares** estimation because it gives the least value for the sum of squared errors. Finding the best estimates of the coefficients is often called “fitting” the model to the data, or sometimes “learning” or “training” the model. The line shown in Figure [7.3](regression-intro.html#fig:ConsInc2) was obtained in this way.

When we refer to the _estimated_ coefficients, we will use the notation \\(\hat\beta_0, \dots, \hat\beta_k\\). The equations for these will be given in Section [7.9](regression-matrices.html#regression-matrices).

The `TSLM()` function fits a linear regression model to time series data. It is similar to the `lm()` function which is widely used for linear models, but `TSLM()` provides additional facilities for handling time series.

### Example: US consumption expenditure[](least-squares.html#example-us-consumption-expenditure-2)

A multiple linear regression model for US consumption is \\[ y_t=\beta_0 + \beta_1 x_{1,t}+ \beta_2 x_{2,t}+ \beta_3 x_{3,t}+ \beta_4 x_{4,t}+\varepsilon_t, \\] where \\(y\\) is the percentage change in real personal consumption expenditure, \\(x_1\\) is the percentage change in real personal disposable income, \\(x_2\\) is the percentage change in industrial production, \\(x_3\\) is the percentage change in personal savings and \\(x_4\\) is the change in the unemployment rate.

The following output provides information about the fitted model. The first column of `Coefficients` gives an estimate of each \\(\beta\\) coefficient and the second column gives its standard error (i.e., the standard deviation which would be obtained from repeatedly estimating the \\(\beta\\) coefficients on similar data sets). The standard error gives a measure of the uncertainty in the estimated \\(\beta\\) coefficient.
    
    
    [](least-squares.html#cb138-1)fit_consMR <- us_change |>
    [](least-squares.html#cb138-2)  model(tslm = TSLM(Consumption ~ Income + Production +
    [](least-squares.html#cb138-3)                                    Unemployment + Savings))
    [](least-squares.html#cb138-4)report(fit_consMR)
    [](least-squares.html#cb138-5)#> Series: Consumption 
    [](least-squares.html#cb138-6)#> Model: TSLM 
    [](least-squares.html#cb138-7)#> 
    [](least-squares.html#cb138-8)#> Residuals:
    [](least-squares.html#cb138-9)#>     Min      1Q  Median      3Q     Max 
    [](least-squares.html#cb138-10)#> -0.9055 -0.1582 -0.0361  0.1362  1.1547 
    [](least-squares.html#cb138-11)#> 
    [](least-squares.html#cb138-12)#> Coefficients:
    [](least-squares.html#cb138-13)#>              Estimate Std. Error t value Pr(>|t|)    
    [](least-squares.html#cb138-14)#> (Intercept)   0.25311    0.03447    7.34  5.7e-12 ***
    [](least-squares.html#cb138-15)#> Income        0.74058    0.04012   18.46  < 2e-16 ***
    [](least-squares.html#cb138-16)#> Production    0.04717    0.02314    2.04    0.043 *  
    [](least-squares.html#cb138-17)#> Unemployment -0.17469    0.09551   -1.83    0.069 .  
    [](least-squares.html#cb138-18)#> Savings      -0.05289    0.00292  -18.09  < 2e-16 ***
    [](least-squares.html#cb138-19)#> ---
    [](least-squares.html#cb138-20)#> Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    [](least-squares.html#cb138-21)#> 
    [](least-squares.html#cb138-22)#> Residual standard error: 0.31 on 193 degrees of freedom
    [](least-squares.html#cb138-23)#> Multiple R-squared: 0.768,   Adjusted R-squared: 0.763
    [](least-squares.html#cb138-24)#> F-statistic:  160 on 4 and 193 DF, p-value: <2e-16

For forecasting purposes, the final two columns are of limited interest. The “t value” is the ratio of an estimated \\(\beta\\) coefficient to its standard error and the last column gives the p-value: the probability of the estimated \\(\beta\\) coefficient being as large as it is if there was no real relationship between consumption and the corresponding predictor. This is useful when studying the effect of each predictor, but is not particularly useful for forecasting.

### Fitted values[](least-squares.html#fitted-values-1)

Predictions of \\(y\\) can be obtained by using the estimated coefficients in the regression equation and setting the error term to zero. In general we write, \\[\begin{equation} \hat{y}_t = \hat\beta_{0} + \hat\beta_{1} x_{1,t} + \hat\beta_{2} x_{2,t} + \cdots + \hat\beta_{k} x_{k,t}. \tag{7.2} \end{equation}\\] Plugging in the values of \\(x_{1,t},\dots,x_{k,t}\\) for \\(t=1,\dots,T\\) returns predictions of \\(y_t\\) within the training set, referred to as _fitted values_. Note that these are predictions of the data used to estimate the model, not genuine forecasts of future values of \\(y\\).

The following plots show the actual values compared to the fitted values for the percentage change in the US consumption expenditure series. The time plot in Figure [7.6](least-squares.html#fig:usfitted1) shows that the fitted values follow the actual data fairly closely. This is verified by the strong positive relationship shown by the scatterplot in Figure [7.7](least-squares.html#fig:usfitted2).
    
    
    [](least-squares.html#cb139-1)augment(fit_consMR) |>
    [](least-squares.html#cb139-2)  ggplot(aes(x = Quarter)) +
    [](least-squares.html#cb139-3)  geom_line(aes(y = Consumption, colour = "Data")) +
    [](least-squares.html#cb139-4)  geom_line(aes(y = .fitted, colour = "Fitted")) +
    [](least-squares.html#cb139-5)  labs(y = NULL,
    [](least-squares.html#cb139-6)    title = "Percent change in US consumption expenditure"
    [](least-squares.html#cb139-7)  ) +
    [](least-squares.html#cb139-8)  scale_colour_manual(values=c(Data="black",Fitted="#D55E00")) +
    [](least-squares.html#cb139-9)  guides(colour = guide_legend(title = NULL))

Figure 7.6: Time plot of actual US consumption expenditure and predicted US consumption expenditure. 
    
    
    [](least-squares.html#cb140-1)augment(fit_consMR) |>
    [](least-squares.html#cb140-2)  ggplot(aes(x = Consumption, y = .fitted)) +
    [](least-squares.html#cb140-3)  geom_point() +
    [](least-squares.html#cb140-4)  labs(
    [](least-squares.html#cb140-5)    y = "Fitted (predicted values)",
    [](least-squares.html#cb140-6)    x = "Data (actual values)",
    [](least-squares.html#cb140-7)    title = "Percent change in US consumption expenditure"
    [](least-squares.html#cb140-8)  ) +
    [](least-squares.html#cb140-9)  geom_abline(intercept = 0, slope = 1)

Figure 7.7: Actual US consumption expenditure plotted against predicted US consumption expenditure. 

### Goodness-of-fit[](least-squares.html#goodness-of-fit)

A common way to summarise how well a linear regression model fits the data is via the coefficient of determination, or \\(R^2\\). This can be calculated as the square of the correlation between the observed \\(y\\) values and the predicted \\(\hat{y}\\) values. Alternatively, it can also be calculated as, \\[ R^2 = \frac{\sum(\hat{y}_{t} - \bar{y})^2}{\sum(y_{t}-\bar{y})^2}, \\] where the summations are over all observations. Thus, it reflects the proportion of variation in the forecast variable that is accounted for (or explained) by the regression model.

In simple linear regression, the value of \\(R^2\\) is also equal to the square of the correlation between \\(y\\) and \\(x\\) (provided an intercept has been included).

If the predictions are close to the actual values, we would expect \\(R^2\\) to be close to 1. On the other hand, if the predictions are unrelated to the actual values, then \\(R^2=0\\) (again, assuming there is an intercept). In all cases, \\(R^2\\) lies between 0 and 1.

The \\(R^2\\) value is used frequently, though often incorrectly, in forecasting. The value of \\(R^2\\) will never decrease when adding an extra predictor to the model and this can lead to over-fitting. There are no set rules for what is a good \\(R^2\\) value, and typical values of \\(R^2\\) depend on the type of data used. Validating a model’s forecasting performance on the test data is much better than measuring the \\(R^2\\) value on the training data.

### Example: US consumption expenditure[](least-squares.html#example-us-consumption-expenditure-3)

Figure [7.7](least-squares.html#fig:usfitted2) plots the actual consumption expenditure values versus the fitted values. The correlation between these variables is \\(r=0.877\\) hence \\(R^2= 0.768\\) (shown in the output above). In this case, the model does an excellent job as it explains 76.8% of the variation in the consumption data. Compare that to the \\(R^2\\) value of 0.15 obtained from the simple regression with the same data set in Section [7.1](regression-intro.html#regression-intro). Adding the three extra predictors has allowed a lot more of the variation in the consumption data to be explained.

### Standard error of the regression[](least-squares.html#standard-error-of-the-regression)

Another measure of how well the model has fitted the data is the standard deviation of the residuals, which is often known as the “residual standard error”. This is shown in the above output with the value 0.31.

It is calculated using \\[\begin{equation} \hat{\sigma}_e=\sqrt{\frac{1}{T-k-1}\sum_{t=1}^{T}{e_t^2}}, \tag{7.3} \end{equation}\\] where \\(k\\) is the number of predictors in the model. Notice that we divide by \\(T-k-1\\) because we have estimated \\(k+1\\) parameters (the intercept and a coefficient for each predictor variable) in computing the residuals.

The standard error is related to the size of the average error that the model produces. We can compare this error to the sample mean of \\(y\\) or with the standard deviation of \\(y\\) to gain some perspective on the accuracy of the model.

The standard error will be used when generating prediction intervals, discussed in Section [7.6](forecasting-regression.html#forecasting-regression).


---

## 7.3 Evaluating the regression model[](regression-evaluation.html#regression-evaluation)

The differences between the observed \\(y\\) values and the corresponding fitted \\(\hat{y}\\) values are the training-set errors or “residuals” defined as, \\[\begin{align*} e_t &= y_t - \hat{y}_t \\\ &= y_t - \hat\beta_{0} - \hat\beta_{1} x_{1,t} - \hat\beta_{2} x_{2,t} - \cdots - \hat\beta_{k} x_{k,t} \end{align*}\\] for \\(t=1,\dots,T\\). Each residual is the unpredictable component of the associated observation.

The residuals have some useful properties including the following two: \\[ \sum_{t=1}^{T}{e_t}=0 \quad\text{and}\quad \sum_{t=1}^{T}{x_{k,t}e_t}=0\qquad\text{for all $k$}. \\] As a result of these properties, it is clear that the average of the residuals is zero, and that the correlation between the residuals and the observations for the predictor variable is also zero. (This is not necessarily true when the intercept is omitted from the model.)

After selecting the regression variables and fitting a regression model, it is necessary to plot the residuals to check that the assumptions of the model have been satisfied. There are a series of plots that should be produced in order to check different aspects of the fitted model and the underlying assumptions. We will now discuss each of them in turn.

### ACF plot of residuals[](regression-evaluation.html#acf-plot-of-residuals)

With time series data, it is highly likely that the value of a variable observed in the current time period will be similar to its value in the previous period, or even the period before that, and so on. Therefore when fitting a regression model to time series data, it is common to find autocorrelation in the residuals. In this case, the estimated model violates the assumption of no autocorrelation in the errors, and our forecasts may be inefficient — there is some information left over which should be accounted for in the model in order to obtain better forecasts. The forecasts from a model with autocorrelated errors are still unbiased, and so they are not “wrong”, but they will usually have larger prediction intervals than they need to. Therefore we should always look at an ACF plot of the residuals.

### Histogram of residuals[](regression-evaluation.html#histogram-of-residuals)

It is always a good idea to check whether the residuals are normally distributed. As we explained earlier, this is not essential for forecasting, but it does make the calculation of prediction intervals much easier.

#### Example[](regression-evaluation.html#example)

Using the `gg_tsresiduals()` function introduced in Section [5.3](residuals.html#residuals), we can obtain all the useful residual diagnostics mentioned above.
    
    
    [](regression-evaluation.html#cb141-1)fit_consMR |> gg_tsresiduals()

Figure 7.8: Analysing the residuals from a regression model for US quarterly consumption. 
    
    
    [](regression-evaluation.html#cb142-1)augment(fit_consMR) |>
    [](regression-evaluation.html#cb142-2)  features(.innov, ljung_box, lag = 10)
    [](regression-evaluation.html#cb142-3)#> # A tibble: 1 × 3
    [](regression-evaluation.html#cb142-4)#>   .model lb_stat lb_pvalue
    [](regression-evaluation.html#cb142-5)#>   <chr>    <dbl>     <dbl>
    [](regression-evaluation.html#cb142-6)#> 1 tslm      18.9    0.0420

The time plot shows some changing variation over time, but is otherwise relatively unremarkable. This heteroscedasticity will potentially make the prediction interval coverage inaccurate.

The histogram shows that the residuals seem to be slightly skewed, which may also affect the coverage probability of the prediction intervals.

The autocorrelation plot shows a significant spike at lag 7, and a significant Ljung-Box test at the 5% level. However, the autocorrelation is not particularly large, and at lag 7 it is unlikely to have any noticeable impact on the forecasts or the prediction intervals. In Chapter [10](dynamic.html#dynamic) we discuss dynamic regression models used for better capturing information left in the residuals.

### Residual plots against predictors[](regression-evaluation.html#residual-plots-against-predictors)

We would expect the residuals to be randomly scattered without showing any systematic patterns. A simple and quick way to check this is to examine scatterplots of the residuals against each of the predictor variables. If these scatterplots show a pattern, then the relationship may be nonlinear and the model will need to be modified accordingly. See Section [7.7](nonlinear-regression.html#nonlinear-regression) for a discussion of nonlinear regression.

It is also necessary to plot the residuals against any predictors that are _not_ in the model. If any of these show a pattern, then the corresponding predictor may need to be added to the model (possibly in a nonlinear form).

#### Example[](regression-evaluation.html#example-1)

The residuals from the multiple regression model for forecasting US consumption plotted against each predictor in Figure [7.9](regression-evaluation.html#fig:resids) seem to be randomly scattered. Therefore we are satisfied with these in this case.
    
    
    [](regression-evaluation.html#cb143-1)us_change |>
    [](regression-evaluation.html#cb143-2)  left_join(residuals(fit_consMR), by = "Quarter") |>
    [](regression-evaluation.html#cb143-3)  pivot_longer(Income:Unemployment,
    [](regression-evaluation.html#cb143-4)               names_to = "regressor", values_to = "x") |>
    [](regression-evaluation.html#cb143-5)  ggplot(aes(x = x, y = .resid)) +
    [](regression-evaluation.html#cb143-6)  geom_point() +
    [](regression-evaluation.html#cb143-7)  facet_wrap(. ~ regressor, scales = "free_x") +
    [](regression-evaluation.html#cb143-8)  labs(y = "Residuals", x = "")

Figure 7.9: Scatterplots of residuals versus each predictor. 

### Residual plots against fitted values[](regression-evaluation.html#residual-plots-against-fitted-values)

A plot of the residuals against the fitted values should also show no pattern. If a pattern is observed, there may be “heteroscedasticity” in the errors which means that the variance of the residuals may not be constant. If this problem occurs, a transformation of the forecast variable such as a logarithm or square root may be required (see Section [3.1](transformations.html#transformations)).

#### Example[](regression-evaluation.html#example-2)

Continuing the previous example, Figure [7.10](regression-evaluation.html#fig:resids2) shows the residuals plotted against the fitted values. The random scatter suggests the errors are homoscedastic.
    
    
    [](regression-evaluation.html#cb144-1)augment(fit_consMR) |>
    [](regression-evaluation.html#cb144-2)  ggplot(aes(x = .fitted, y = .resid)) +
    [](regression-evaluation.html#cb144-3)  geom_point() + labs(x = "Fitted", y = "Residuals")

Figure 7.10: Scatterplots of residuals versus fitted values. 

### Outliers and influential observations[](regression-evaluation.html#outliers-and-influential-observations)

Observations that take extreme values compared to the majority of the data are called **outliers**. Observations that have a large influence on the estimated coefficients of a regression model are called **influential observations**. Usually, influential observations are also outliers that are extreme in the \\(x\\) direction.

There are formal methods for detecting outliers and influential observations that are beyond the scope of this textbook. As we suggested at the beginning of Chapter [2](graphics.html#graphics), becoming familiar with your data prior to performing any analysis is of vital importance. A scatter plot of \\(y\\) against each \\(x\\) is always a useful starting point in regression analysis, and often helps to identify unusual observations.

One source of outliers is incorrect data entry. Simple descriptive statistics of your data can identify minima and maxima that are not sensible. If such an observation is identified, and it has been recorded incorrectly, it should be corrected or removed from the sample immediately.

Outliers also occur when some observations are simply different. In this case it may not be wise for these observations to be removed. If an observation has been identified as a likely outlier, it is important to study it and analyse the possible reasons behind it. The decision to remove or retain an observation can be a challenging one (especially when outliers are influential observations). It is wise to report results both with and without the removal of such observations.

#### Example[](regression-evaluation.html#example-3)

Figure [7.11](regression-evaluation.html#fig:outlier) highlights the effect of a single outlier when regressing US consumption on income (the example introduced in Section [7.1](regression-intro.html#regression-intro)). In the left panel the outlier is only extreme in the direction of \\(y\\), as the percentage change in consumption has been incorrectly recorded as -4%. The orange line is the regression line fitted to the data which includes the outlier, compared to the black line which is the line fitted to the data without the outlier. In the right panel the outlier now is also extreme in the direction of \\(x\\) with the 4% decrease in consumption corresponding to a 6% increase in income. In this case the outlier is extremely influential as the orange line now deviates substantially from the black line.

Figure 7.11: The effect of outliers and influential observations on regression 

### Spurious regression[](regression-evaluation.html#spurious-regression)

More often than not, time series data are “non-stationary”; that is, the values of the time series do not fluctuate around a constant mean or with a constant variance. We will deal with time series stationarity in more detail in Chapter [9](arima.html#arima), but here we need to address the effect that non-stationary data can have on regression models.

For example, consider the two variables plotted in Figure [7.12](regression-evaluation.html#fig:spurious). These appear to be related simply because they both trend upwards in the same manner. However, air passenger traffic in Australia has nothing to do with rice production in Guinea.

Figure 7.12: Trending time series data can appear to be related, as shown in this example where air passengers in Australia are regressed against rice production in Guinea. 

Regressing non-stationary time series can lead to spurious regressions. The output of regressing Australian air passengers on rice production in Guinea is shown in Figure [7.13](regression-evaluation.html#fig:tslmspurious2). High \\(R^2\\) and high residual autocorrelation can be signs of spurious regression. Notice these features in the output below. We discuss the issues surrounding non-stationary data and spurious regressions in more detail in Chapter [10](dynamic.html#dynamic).

Cases of spurious regression might appear to give reasonable short-term forecasts, but they will generally not continue to work into the future.
    
    
    [](regression-evaluation.html#cb145-1)fit <- aus_airpassengers |>
    [](regression-evaluation.html#cb145-2)  filter(Year <= 2011) |>
    [](regression-evaluation.html#cb145-3)  left_join(guinea_rice, by = "Year") |>
    [](regression-evaluation.html#cb145-4)  model(TSLM(Passengers ~ Production))
    [](regression-evaluation.html#cb145-5)report(fit)
    [](regression-evaluation.html#cb145-6)#> Series: Passengers 
    [](regression-evaluation.html#cb145-7)#> Model: TSLM 
    [](regression-evaluation.html#cb145-8)#> 
    [](regression-evaluation.html#cb145-9)#> Residuals:
    [](regression-evaluation.html#cb145-10)#>    Min     1Q Median     3Q    Max 
    [](regression-evaluation.html#cb145-11)#> -5.945 -1.892 -0.327  1.862 10.421 
    [](regression-evaluation.html#cb145-12)#> 
    [](regression-evaluation.html#cb145-13)#> Coefficients:
    [](regression-evaluation.html#cb145-14)#>             Estimate Std. Error t value Pr(>|t|)    
    [](regression-evaluation.html#cb145-15)#> (Intercept)    -7.49       1.20   -6.23  2.3e-07 ***
    [](regression-evaluation.html#cb145-16)#> Production     40.29       1.34   30.13  < 2e-16 ***
    [](regression-evaluation.html#cb145-17)#> ---
    [](regression-evaluation.html#cb145-18)#> Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    [](regression-evaluation.html#cb145-19)#> 
    [](regression-evaluation.html#cb145-20)#> Residual standard error: 3.24 on 40 degrees of freedom
    [](regression-evaluation.html#cb145-21)#> Multiple R-squared: 0.958,   Adjusted R-squared: 0.957
    [](regression-evaluation.html#cb145-22)#> F-statistic:  908 on 1 and 40 DF, p-value: <2e-16
    
    
    [](regression-evaluation.html#cb146-1)fit |> gg_tsresiduals()

Figure 7.13: Residuals from a spurious regression. 


---

## 7.4 Some useful predictors[](useful-predictors.html#useful-predictors)

There are several useful predictors that occur frequently when using regression for time series data.

### Trend[](useful-predictors.html#trend)

It is common for time series data to be trending. A linear trend can be modelled by simply using \\(x_{1,t}=t\\) as a predictor, \\[ y_{t}= \beta_0+\beta_1t+\varepsilon_t, \\] where \\(t=1,\dots,T\\). A trend variable can be specified in the `TSLM()` function using the `trend()` special. In Section [7.7](nonlinear-regression.html#nonlinear-regression) we discuss how we can also model nonlinear trends.

### Dummy variables[](useful-predictors.html#dummy-variables)

So far, we have assumed that each predictor takes numerical values. But what about when a predictor is a categorical variable taking only two values (e.g., “yes” and “no”)? Such a variable might arise, for example, when forecasting daily sales and you want to take account of whether the day is a **public holiday** or not. So the predictor takes value “yes” on a public holiday, and “no” otherwise.

This situation can still be handled within the framework of multiple regression models by creating a “dummy variable” which takes value 1 corresponding to “yes” and 0 corresponding to “no”. A dummy variable is also known as an “indicator variable”.

A dummy variable can also be used to account for an **outlier** in the data. Rather than omit the outlier, a dummy variable removes its effect. In this case, the dummy variable takes value 1 for that observation and 0 everywhere else. An example is the case where a special event has occurred. For example when forecasting tourist arrivals to Brazil, we will need to account for the effect of the Rio de Janeiro summer Olympics in 2016.

If there are more than two categories, then the variable can be coded using several dummy variables (one fewer than the total number of categories). `TSLM()` will automatically handle this case if you specify a factor variable as a predictor. There is usually no need to manually create the corresponding dummy variables.

### Seasonal dummy variables[](useful-predictors.html#seasonal-dummy-variables)

Suppose that we are forecasting daily data and we want to account for the day of the week as a predictor. Then the following dummy variables can be created.

| \\(d_{1,t}\\) | \\(d_{2,t}\\) | \\(d_{3,t}\\) | \\(d_{4,t}\\) | \\(d_{5,t}\\) | \\(d_{6,t}\\)  
---|---|---|---|---|---|---  
Monday | 1 | 0 | 0 | 0 | 0 | 0  
Tuesday | 0 | 1 | 0 | 0 | 0 | 0  
Wednesday | 0 | 0 | 1 | 0 | 0 | 0  
Thursday | 0 | 0 | 0 | 1 | 0 | 0  
Friday | 0 | 0 | 0 | 0 | 1 | 0  
Saturday | 0 | 0 | 0 | 0 | 0 | 1  
Sunday | 0 | 0 | 0 | 0 | 0 | 0  
Monday | 1 | 0 | 0 | 0 | 0 | 0  
⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮  
  
Notice that only six dummy variables are needed to code seven categories. That is because the seventh category (in this case Sunday) is captured by the intercept, and is specified when the dummy variables are all set to zero.

Many beginners will try to add a seventh dummy variable for the seventh category. This is known as the “dummy variable trap”, because it will cause the regression to fail. There will be one too many parameters to estimate when an intercept is also included. The general rule is to use one fewer dummy variables than categories. So for quarterly data, use three dummy variables; for monthly data, use 11 dummy variables; and for daily data, use six dummy variables, and so on.

The interpretation of each of the coefficients associated with the dummy variables is that it is _a measure of the effect of that category relative to the omitted category_. In the above example, the coefficient of \\(d_{1,t}\\) associated with Monday will measure the effect of Monday on the forecast variable compared to the effect of Sunday. An example of interpreting estimated dummy variable coefficients capturing the quarterly seasonality of Australian beer production follows.

The `TSLM()` function will automatically handle this situation if you specify the special `season()`.

### Example: Australian quarterly beer production[](useful-predictors.html#example-australian-quarterly-beer-production-1)

Recall the Australian quarterly beer production data shown again in Figure [7.14](useful-predictors.html#fig:beeragain).
    
    
    [](useful-predictors.html#cb147-1)recent_production <- aus_production |>
    [](useful-predictors.html#cb147-2)  filter(year(Quarter) >= 1992)
    [](useful-predictors.html#cb147-3)recent_production |>
    [](useful-predictors.html#cb147-4)  autoplot(Beer) +
    [](useful-predictors.html#cb147-5)  labs(y = "Megalitres",
    [](useful-predictors.html#cb147-6)       title = "Australian quarterly beer production")

Figure 7.14: Australian quarterly beer production. 

We want to forecast the value of future beer production. We can model this data using a regression model with a linear trend and quarterly dummy variables, \\[ y_{t} = \beta_{0} + \beta_{1} t + \beta_{2}d_{2,t} + \beta_3 d_{3,t} + \beta_4 d_{4,t} + \varepsilon_{t}, \\] where \\(d_{i,t} = 1\\) if \\(t\\) is in quarter \\(i\\) and 0 otherwise. The first quarter variable has been omitted, so the coefficients associated with the other quarters are measures of the difference between those quarters and the first quarter.
    
    
    [](useful-predictors.html#cb148-1)fit_beer <- recent_production |>
    [](useful-predictors.html#cb148-2)  model(TSLM(Beer ~ trend() + season()))
    [](useful-predictors.html#cb148-3)report(fit_beer)
    [](useful-predictors.html#cb148-4)#> Series: Beer 
    [](useful-predictors.html#cb148-5)#> Model: TSLM 
    [](useful-predictors.html#cb148-6)#> 
    [](useful-predictors.html#cb148-7)#> Residuals:
    [](useful-predictors.html#cb148-8)#>    Min     1Q Median     3Q    Max 
    [](useful-predictors.html#cb148-9)#> -42.90  -7.60  -0.46   7.99  21.79 
    [](useful-predictors.html#cb148-10)#> 
    [](useful-predictors.html#cb148-11)#> Coefficients:
    [](useful-predictors.html#cb148-12)#>               Estimate Std. Error t value Pr(>|t|)    
    [](useful-predictors.html#cb148-13)#> (Intercept)   441.8004     3.7335  118.33  < 2e-16 ***
    [](useful-predictors.html#cb148-14)#> trend()        -0.3403     0.0666   -5.11  2.7e-06 ***
    [](useful-predictors.html#cb148-15)#> season()year2 -34.6597     3.9683   -8.73  9.1e-13 ***
    [](useful-predictors.html#cb148-16)#> season()year3 -17.8216     4.0225   -4.43  3.4e-05 ***
    [](useful-predictors.html#cb148-17)#> season()year4  72.7964     4.0230   18.09  < 2e-16 ***
    [](useful-predictors.html#cb148-18)#> ---
    [](useful-predictors.html#cb148-19)#> Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    [](useful-predictors.html#cb148-20)#> 
    [](useful-predictors.html#cb148-21)#> Residual standard error: 12.2 on 69 degrees of freedom
    [](useful-predictors.html#cb148-22)#> Multiple R-squared: 0.924,   Adjusted R-squared: 0.92
    [](useful-predictors.html#cb148-23)#> F-statistic:  211 on 4 and 69 DF, p-value: <2e-16

Note that `trend()` and `season()` are not standard functions; they are “special” functions that work within the `TSLM()` model formulae.

There is an average downward trend of -0.34 megalitres per quarter. On average, the second quarter has production of 34.7 megalitres lower than the first quarter, the third quarter has production of 17.8 megalitres lower than the first quarter, and the fourth quarter has production of 72.8 megalitres higher than the first quarter.
    
    
    [](useful-predictors.html#cb149-1)augment(fit_beer) |>
    [](useful-predictors.html#cb149-2)  ggplot(aes(x = Quarter)) +
    [](useful-predictors.html#cb149-3)  geom_line(aes(y = Beer, colour = "Data")) +
    [](useful-predictors.html#cb149-4)  geom_line(aes(y = .fitted, colour = "Fitted")) +
    [](useful-predictors.html#cb149-5)  scale_colour_manual(
    [](useful-predictors.html#cb149-6)    values = c(Data = "black", Fitted = "#D55E00")
    [](useful-predictors.html#cb149-7)  ) +
    [](useful-predictors.html#cb149-8)  labs(y = "Megalitres",
    [](useful-predictors.html#cb149-9)       title = "Australian quarterly beer production") +
    [](useful-predictors.html#cb149-10)  guides(colour = guide_legend(title = "Series"))

Figure 7.15: Time plot of beer production and predicted beer production. 
    
    
    [](useful-predictors.html#cb150-1)augment(fit_beer) |>
    [](useful-predictors.html#cb150-2)  ggplot(aes(x = Beer, y = .fitted,
    [](useful-predictors.html#cb150-3)             colour = factor(quarter(Quarter)))) +
    [](useful-predictors.html#cb150-4)  geom_point() +
    [](useful-predictors.html#cb150-5)  labs(y = "Fitted", x = "Actual values",
    [](useful-predictors.html#cb150-6)       title = "Australian quarterly beer production") +
    [](useful-predictors.html#cb150-7)  geom_abline(intercept = 0, slope = 1) +
    [](useful-predictors.html#cb150-8)  guides(colour = guide_legend(title = "Quarter"))

Figure 7.16: Actual beer production plotted against predicted beer production. 

### Intervention variables[](useful-predictors.html#intervention-variables)

It is often necessary to model interventions that may have affected the variable to be forecast. For example, competitor activity, advertising expenditure, industrial action, and so on, can all have an effect.

When the effect lasts only for one period, we use a “spike” variable. This is a dummy variable that takes value one in the period of the intervention and zero elsewhere. A spike variable is equivalent to a dummy variable for handling an outlier.

Other interventions have an immediate and permanent effect. If an intervention causes a level shift (i.e., the value of the series changes suddenly and permanently from the time of intervention), then we use a “step” variable. A step variable takes value zero before the intervention and one from the time of intervention onward.

Another form of permanent effect is a change of slope. Here the intervention is handled using a piecewise linear trend; a trend that bends at the time of intervention and hence is nonlinear. We will discuss this in Section [7.7](nonlinear-regression.html#nonlinear-regression).

### Trading days[](useful-predictors.html#trading-days)

The number of trading days in a month can vary considerably and can have a substantial effect on sales data. To allow for this, the number of trading days in each month can be included as a predictor.

An alternative that allows for the effects of different days of the week has the following predictors: \\[\begin{align*} x_{1} &= \text{number of Mondays in month;} \\\ x_{2} &= \text{number of Tuesdays in month;} \\\ & \vdots \\\ x_{7} &= \text{number of Sundays in month.} \end{align*}\\]

### Distributed lags[](useful-predictors.html#distributed-lags)

It is often useful to include advertising expenditure as a predictor. However, since the effect of advertising can last beyond the actual campaign, we need to include lagged values of advertising expenditure. Thus, the following predictors may be used. \\[\begin{align*} x_{1} &= \text{advertising for previous month;} \\\ x_{2} &= \text{advertising for two months previously;} \\\ & \vdots \\\ x_{m} &= \text{advertising for $m$ months previously.} \end{align*}\\]

It is common to require the coefficients to decrease as the lag increases, although this is beyond the scope of this book.

### Easter[](useful-predictors.html#easter)

Easter differs from most holidays because it is not held on the same date each year, and its effect can last for several days. In this case, a dummy variable can be used with value one where the holiday falls in the particular time period and zero otherwise.

With monthly data, if Easter falls in March then the dummy variable takes value 1 in March, and if it falls in April the dummy variable takes value 1 in April. When Easter starts in March and finishes in April, the dummy variable is split proportionally between months.

### Fourier series[](useful-predictors.html#fourier-series)

An alternative to using seasonal dummy variables, especially for long seasonal periods, is to use Fourier terms. Jean-Baptiste Fourier was a French mathematician, born in the 1700s, who showed that a series of sine and cosine terms of the right frequencies can approximate any periodic function. We can use them for seasonal patterns.

If \\(m\\) is the seasonal period, then the first few Fourier terms are given by \\[ x_{1,t} = \sin\left(\textstyle\frac{2\pi t}{m}\right), x_{2,t} = \cos\left(\textstyle\frac{2\pi t}{m}\right), x_{3,t} = \sin\left(\textstyle\frac{4\pi t}{m}\right), \\] \\[ x_{4,t} = \cos\left(\textstyle\frac{4\pi t}{m}\right), x_{5,t} = \sin\left(\textstyle\frac{6\pi t}{m}\right), x_{6,t} = \cos\left(\textstyle\frac{6\pi t}{m}\right), \\] and so on. If we have monthly seasonality, and we use the first 11 of these predictor variables, then we will get exactly the same forecasts as using 11 dummy variables.

With Fourier terms, we often need fewer predictors than with dummy variables, especially when \\(m\\) is large. This makes them useful for weekly data, for example, where \\(m\approx 52\\). For short seasonal periods (e.g., quarterly data), there is little advantage in using Fourier terms over seasonal dummy variables.

These Fourier terms are produced using the `fourier()` function. For example, the Australian beer data can be modelled like this.
    
    
    [](useful-predictors.html#cb151-1)fourier_beer <- recent_production |>
    [](useful-predictors.html#cb151-2)  model(TSLM(Beer ~ trend() + fourier(K = 2)))
    [](useful-predictors.html#cb151-3)report(fourier_beer)
    [](useful-predictors.html#cb151-4)#> Series: Beer 
    [](useful-predictors.html#cb151-5)#> Model: TSLM 
    [](useful-predictors.html#cb151-6)#> 
    [](useful-predictors.html#cb151-7)#> Residuals:
    [](useful-predictors.html#cb151-8)#>    Min     1Q Median     3Q    Max 
    [](useful-predictors.html#cb151-9)#> -42.90  -7.60  -0.46   7.99  21.79 
    [](useful-predictors.html#cb151-10)#> 
    [](useful-predictors.html#cb151-11)#> Coefficients:
    [](useful-predictors.html#cb151-12)#>                    Estimate Std. Error t value Pr(>|t|)    
    [](useful-predictors.html#cb151-13)#> (Intercept)        446.8792     2.8732  155.53  < 2e-16 ***
    [](useful-predictors.html#cb151-14)#> trend()             -0.3403     0.0666   -5.11  2.7e-06 ***
    [](useful-predictors.html#cb151-15)#> fourier(K = 2)C1_4   8.9108     2.0112    4.43  3.4e-05 ***
    [](useful-predictors.html#cb151-16)#> fourier(K = 2)S1_4 -53.7281     2.0112  -26.71  < 2e-16 ***
    [](useful-predictors.html#cb151-17)#> fourier(K = 2)C2_4 -13.9896     1.4226   -9.83  9.3e-15 ***
    [](useful-predictors.html#cb151-18)#> ---
    [](useful-predictors.html#cb151-19)#> Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    [](useful-predictors.html#cb151-20)#> 
    [](useful-predictors.html#cb151-21)#> Residual standard error: 12.2 on 69 degrees of freedom
    [](useful-predictors.html#cb151-22)#> Multiple R-squared: 0.924,   Adjusted R-squared: 0.92
    [](useful-predictors.html#cb151-23)#> F-statistic:  211 on 4 and 69 DF, p-value: <2e-16

The `K` argument to `fourier()` specifies how many pairs of sin and cos terms to include. The maximum allowed is \\(K=m/2\\) where \\(m\\) is the seasonal period. Because we have used the maximum here, the results are identical to those obtained when using seasonal dummy variables.

If only the first two Fourier terms are used (\\(x_{1,t}\\) and \\(x_{2,t}\\)), the seasonal pattern will follow a simple sine wave. A regression model containing Fourier terms is often called a **harmonic regression** because the successive Fourier terms represent harmonics of the first two Fourier terms.


---

## 7.5 Selecting predictors[](selecting-predictors.html#selecting-predictors)

When there are many possible predictors, we need some strategy for selecting the best predictors to use in a regression model.

A common approach that is _not recommended_ is to plot the forecast variable against a particular predictor and if there is no noticeable relationship, drop that predictor from the model. This is invalid because it is not always possible to see the relationship from a scatterplot, especially when the effects of other predictors have not been accounted for.

Another common approach which is also invalid is to do a multiple linear regression on all the predictors and disregard all variables whose \\(p\\)-values are greater than 0.05. To start with, statistical significance does not always indicate predictive value. Even if forecasting is not the goal, this is not a good strategy because the \\(p\\)-values can be misleading when two or more predictors are correlated with each other (see Section [7.8](causality.html#causality)).

Instead, we will use a measure of predictive accuracy. Five such measures are introduced in this section. They can be shown using the `glance()` function, here applied to the model for US consumption:
    
    
    [](selecting-predictors.html#cb152-1)glance(fit_consMR) |>
    [](selecting-predictors.html#cb152-2)  select(adj_r_squared, CV, AIC, AICc, BIC)
    [](selecting-predictors.html#cb152-3)#> # A tibble: 1 × 5
    [](selecting-predictors.html#cb152-4)#>   adj_r_squared    CV   AIC  AICc   BIC
    [](selecting-predictors.html#cb152-5)#>           <dbl> <dbl> <dbl> <dbl> <dbl>
    [](selecting-predictors.html#cb152-6)#> 1         0.763 0.104 -457. -456. -437.

We compare these values against the corresponding values from other models. For the CV, AIC, AICc and BIC measures, we want to find the model with the lowest value; for Adjusted \\(R^2\\), we seek the model with the highest value.

### Adjusted R\\(^2\\)[](selecting-predictors.html#adjusted-r2)

Computer output for a regression will always give the \\(R^2\\) value, discussed in Section [7.2](least-squares.html#least-squares). However, it is not a good measure of the predictive ability of a model. It measures how well the model fits the historical data, but not how well the model will forecast future data.

In addition, \\(R^2\\) does not allow for “degrees of freedom”. Adding _any_ variable tends to increase the value of \\(R^2\\), even if that variable is irrelevant. For these reasons, forecasters should not use \\(R^2\\) to determine whether a model will give good predictions, as it will lead to overfitting.

An equivalent idea is to select the model which gives the minimum sum of squared errors (SSE), given by \\[ \text{SSE} = \sum_{t=1}^T e_{t}^2. \\]

Minimising the SSE is equivalent to maximising \\(R^2\\) and will always choose the model with the most variables, and so is not a valid way of selecting predictors.

An alternative which is designed to overcome these problems is the adjusted \\(R^2\\) (also called “R-bar-squared”): \\[ \bar{R}^2 = 1-(1-R^2)\frac{T-1}{T-k-1}, \\] where \\(T\\) is the number of observations and \\(k\\) is the number of predictors. This is an improvement on \\(R^2\\), as it will no longer increase with each added predictor. Using this measure, the best model will be the one with the largest value of \\(\bar{R}^2\\). Maximising \\(\bar{R}^2\\) is equivalent to minimising the standard error \\(\hat{\sigma}_e\\) given in Equation [(7.3)](least-squares.html#eq:Regr-se).

Maximising \\(\bar{R}^2\\) works quite well as a method of selecting predictors, although it does tend to err on the side of selecting too many predictors.

### Cross-validation[](selecting-predictors.html#cross-validation)

Time series cross-validation was introduced in Section [5.10](tscv.html#tscv) as a general tool for determining the predictive ability of a model. For regression models, it is also possible to use classical leave-one-out cross-validation to select predictors ([Bergmeir et al., 2018](selecting-predictors.html#ref-BHK15)). This is faster and makes more efficient use of the data. The procedure uses the following steps:

  1. Remove observation \\(t\\) from the data set, and fit the model using the remaining data. Then compute the error (\\(e_{t}^*=y_{t}-\hat{y}_{t}\\)) for the omitted observation. (This is not the same as the residual because the \\(t\\)th observation was not used in estimating the value of \\(\hat{y}_{t}\\).)
  2. Repeat step 1 for \\(t=1,\dots,T\\).
  3. Compute the MSE from \\(e_{1}^*,\dots,e_{T}^*\\). We shall call this the **CV**.


Although this looks like a time-consuming procedure, there are fast methods of calculating CV, so that it takes no longer than fitting one model to the full data set. The equation for computing CV efficiently is given in Section [7.9](regression-matrices.html#regression-matrices). Under this criterion, the best model is the one with the smallest value of CV.

### Akaike’s Information Criterion[](selecting-predictors.html#akaikes-information-criterion)

A closely-related method is Akaike’s Information Criterion, which we define as \\[ \text{AIC} = T\log\left(\frac{\text{SSE}}{T}\right) + 2(k+2), \\] where \\(T\\) is the number of observations used for estimation and \\(k\\) is the number of predictors in the model. Different computer packages use slightly different definitions for the AIC, although they should all lead to the same model being selected. The \\(k+2\\) part of the equation occurs because there are \\(k+2\\) parameters in the model: the \\(k\\) coefficients for the predictors, the intercept and the variance of the residuals. The idea here is to penalise the fit of the model (SSE) with the number of parameters that need to be estimated.

The model with the minimum value of the AIC is often the best model for forecasting. For large values of \\(T\\), minimising the AIC is equivalent to minimising the CV value.

### Corrected Akaike’s Information Criterion[](selecting-predictors.html#corrected-akaikes-information-criterion)

For small values of \\(T\\), the AIC tends to select too many predictors, and so a bias-corrected version of the AIC has been developed, \\[ \text{AIC}_{\text{c}} = \text{AIC} + \frac{2(k+2)(k+3)}{T-k-3}. \\] As with the AIC, the AICc should be minimised.

### Schwarz’s Bayesian Information Criterion[](selecting-predictors.html#schwarzs-bayesian-information-criterion)

A related measure is Schwarz’s Bayesian Information Criterion (usually abbreviated to BIC, SBIC or SC): \\[ \text{BIC} = T\log\left(\frac{\text{SSE}}{T}\right) + (k+2)\log(T). \\] As with the AIC, minimising the BIC is intended to give the best model. The model chosen by the BIC is either the same as that chosen by the AIC, or one with fewer terms. This is because the BIC penalises the number of parameters more heavily than the AIC. For large values of \\(T\\), minimising BIC is similar to leave-\\(v\\)-out cross-validation when \\(v = T[1-1/(\log(T)-1)]\\).

### Which measure should we use?[](selecting-predictors.html#which-measure-should-we-use)

While \\(\bar{R}^2\\) is widely used, and has been around longer than the other measures, its tendency to select too many predictor variables makes it less suitable for forecasting.

Many statisticians like to use the BIC because it has the feature that if there is a true underlying model, the BIC will select that model given enough data. However, in reality, there is rarely, if ever, a true underlying model, and even if there was a true underlying model, selecting that model will not necessarily give the best forecasts (because the parameter estimates may not be accurate).

Consequently, we recommend that one of the AICc, AIC, or CV statistics be used, each of which has forecasting as their objective. If the value of \\(T\\) is large enough, they will all lead to the same model. In most of the examples in this book, we use the AICc value to select the forecasting model.

### Example: US consumption[](selecting-predictors.html#example-us-consumption)

In the multiple regression example for forecasting US consumption we considered four predictors. With four predictors, there are \\(2^4=16\\) possible models. Now we can check if all four predictors are actually useful, or whether we can drop one or more of them. All 16 models were fitted and the results are summarised in Table [7.1](selecting-predictors.html#tab:tblusMR). A “⬤” indicates that the predictor was included in the model. Hence the first row shows the measures of predictive accuracy for a model including all four predictors.

The results have been sorted according to the AICc. Therefore the best models are given at the top of the table, and the worst at the bottom of the table.

Table 7.1: All 16 possible models for forecasting US consumption with 4 predictors.  Income  |  Production  |  Savings  |  Unemployment  |  AdjR2  |  CV  |  AIC  |  AICc  |  BIC   
---|---|---|---|---|---|---|---|---  
⬤  |  ⬤  |  ⬤  |  ⬤  |  0.763  |  0.104  |  -456.6  |  -456.1  |  -436.9   
⬤  |  ⬤  |  ⬤  |  |  0.761  |  0.105  |  -455.2  |  -454.9  |  -438.7   
⬤  |  |  ⬤  |  ⬤  |  0.760  |  0.104  |  -454.4  |  -454.1  |  -437.9   
⬤  |  |  ⬤  |  |  0.735  |  0.114  |  -435.7  |  -435.5  |  -422.6   
⬤  |  ⬤  |  |  ⬤  |  0.366  |  0.271  |  -262.3  |  -262.0  |  -245.8   
|  ⬤  |  ⬤  |  ⬤  |  0.349  |  0.279  |  -257.1  |  -256.8  |  -240.7   
⬤  |  |  |  ⬤  |  0.345  |  0.276  |  -256.9  |  -256.6  |  -243.7   
⬤  |  ⬤  |  |  |  0.336  |  0.282  |  -254.2  |  -254.0  |  -241.0   
|  ⬤  |  ⬤  |  |  0.324  |  0.287  |  -250.7  |  -250.5  |  -237.5   
|  |  ⬤  |  ⬤  |  0.311  |  0.291  |  -246.9  |  -246.7  |  -233.7   
|  ⬤  |  |  ⬤  |  0.308  |  0.293  |  -246.1  |  -245.9  |  -232.9   
|  ⬤  |  |  |  0.276  |  0.304  |  -238.1  |  -238.0  |  -228.2   
|  |  |  ⬤  |  0.274  |  0.303  |  -237.4  |  -237.3  |  -227.5   
⬤  |  |  |  |  0.143  |  0.356  |  -204.6  |  -204.5  |  -194.7   
|  |  ⬤  |  |  0.061  |  0.388  |  -186.5  |  -186.4  |  -176.7   
|  |  |  |  0.000  |  0.409  |  -175.1  |  -175.0  |  -168.5   
  
The best model contains all four predictors. However, a closer look at the results reveals some interesting features. There is clear separation between the models in the first four rows and the ones below. This indicates that `Income` and `Savings` are both more important variables than `Production` and `Unemployment`. Also, the first three rows have almost identical values of CV, AIC and AICc. So we could possibly drop either the `Production` variable, or the `Unemployment` variable, and get similar forecasts. Note that `Production` and `Unemployment` are highly (negatively) correlated, as shown in Figure [7.5](regression-intro.html#fig:ScatterMatrix), so most of the predictive information in `Production` is also contained in the `Unemployment` variable.

### Best subset regression[](selecting-predictors.html#best-subset-regression)

Where possible, all potential regression models should be fitted (as was done in the example above) and the best model should be selected based on one of the measures discussed. This is known as “best subsets” regression or “all possible subsets” regression.

### Stepwise regression[](selecting-predictors.html#stepwise-regression)

If there are a large number of predictors, it is not possible to fit all possible models. For example, 40 predictors leads to \\(2^{40} >\\) 1 trillion possible models! Consequently, a strategy is required to limit the number of models to be explored.

An approach that works quite well is _backwards stepwise regression_ :

  * Start with the model containing all potential predictors.
  * Remove one predictor at a time. Keep the model if it improves the measure of predictive accuracy.
  * Iterate until no further improvement.


If the number of potential predictors is too large, then the backwards stepwise regression will not work and _forward stepwise regression_ can be used instead. This procedure starts with a model that includes only the intercept. Predictors are added one at a time, and the one that most improves the measure of predictive accuracy is retained in the model. The procedure is repeated until no further improvement can be achieved.

Alternatively for either the backward or forward direction, a starting model can be one that includes a subset of potential predictors. In this case, an extra step needs to be included. For the backwards procedure we should also consider adding a predictor with each step, and for the forward procedure we should also consider dropping a predictor with each step. These are referred to as _hybrid_ procedures.

It is important to realise that any stepwise approach is not guaranteed to lead to the best possible model, but it almost always leads to a good model. For further details see James et al. ([2021](selecting-predictors.html#ref-ISLR)).

### Beware of inference after selecting predictors[](selecting-predictors.html#beware-of-inference-after-selecting-predictors)

We do not discuss statistical inference of the predictors in this book (e.g., looking at \\(p\\)-values associated with each predictor). If you do wish to look at the statistical significance of the predictors, beware that _any_ procedure involving selecting predictors first will invalidate the assumptions behind the \\(p\\)-values. The procedures we recommend for selecting predictors are helpful when the model is used for forecasting; they are not helpful if you wish to study the effect of any predictor on the forecast variable.

### Bibliography[](bibliography.html#bibliography)

Bergmeir, C., Hyndman, R. J., & Koo, B. (2018). A note on the validity of cross-validation for evaluating autoregressive time series prediction. _Computational Statistics and Data Analysis_ , _120_ , 70–83. [__](https://doi.org/10.1016/j.csda.2017.11.003)

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). _An introduction to statistical learning: With applications in R_. Springer. [__](http://amazon.com/dp/1071614177?tag=otexts20)


---

## 7.6 Forecasting with regression[](forecasting-regression.html#forecasting-regression)

Recall that predictions of \\(y\\) can be obtained using \\[ \hat{y_t} = \hat\beta_{0} + \hat\beta_{1} x_{1,t} + \hat\beta_{2} x_{2,t} + \cdots + \hat\beta_{k} x_{k,t}, \\] which comprises the estimated coefficients and ignores the error in the regression equation. Plugging in the values of the predictor variables \\(x_{1,t},\dots,x_{k,t}\\) for \\(t=1,\dots,T\\) returns the fitted (training set) values of \\(y\\). What we are interested in here, however, is forecasting _future_ values of \\(y\\).

### Ex-ante versus ex-post forecasts[](forecasting-regression.html#ex-ante-versus-ex-post-forecasts)

When using regression models for time series data, we need to distinguish between the different types of forecasts that can be produced, depending on what is assumed to be known when the forecasts are computed.

**Ex-ante forecasts** are those that are made using only the information that is available in advance. For example, ex-ante forecasts for the percentage change in US consumption for quarters following the end of the sample, should only use information that was available _up to and including_ 2019 Q2. These are genuine forecasts, made in advance using whatever information is available at the time. Therefore in order to generate ex-ante forecasts, the model requires forecasts of the predictors. To obtain these we can use one of the simple methods introduced in Section [5.2](simple-methods.html#simple-methods) or more sophisticated pure time series approaches that follow in Chapters [8](expsmooth.html#expsmooth) and [9](arima.html#arima). Alternatively, forecasts from some other source, such as a government agency, may be available and can be used.

**Ex-post forecasts** are those that are made using later information on the predictors. For example, ex-post forecasts of consumption may use the actual observations of the predictors, once these have been observed. These are not genuine forecasts, but are useful for studying the behaviour of forecasting models.

The model from which ex-post forecasts are produced should not be estimated using data from the forecast period. That is, ex-post forecasts can assume knowledge of the predictor variables (the \\(x\\) variables), but should not assume knowledge of the data that are to be forecast (the \\(y\\) variable).

A comparative evaluation of ex-ante forecasts and ex-post forecasts can help to separate out the sources of forecast uncertainty. This will show whether forecast errors have arisen due to poor forecasts of the predictor or due to a poor forecasting model.

### Example: Australian quarterly beer production[](forecasting-regression.html#example-australian-quarterly-beer-production-2)

Normally, we cannot use actual future values of the predictor variables when producing ex-ante forecasts because their values will not be known in advance. However, the special predictors introduced in Section [7.4](useful-predictors.html#useful-predictors) are all known in advance, as they are based on calendar variables (e.g., seasonal dummy variables or public holiday indicators) or deterministic functions of time (e.g. time trend). In such cases, there is no difference between ex-ante and ex-post forecasts.
    
    
    [](forecasting-regression.html#cb153-1)recent_production <- aus_production |>
    [](forecasting-regression.html#cb153-2)  filter(year(Quarter) >= 1992)
    [](forecasting-regression.html#cb153-3)fit_beer <- recent_production |>
    [](forecasting-regression.html#cb153-4)  model(TSLM(Beer ~ trend() + season()))
    [](forecasting-regression.html#cb153-5)fc_beer <- forecast(fit_beer)
    [](forecasting-regression.html#cb153-6)fc_beer |>
    [](forecasting-regression.html#cb153-7)  autoplot(recent_production) +
    [](forecasting-regression.html#cb153-8)  labs(
    [](forecasting-regression.html#cb153-9)    title = "Forecasts of beer production using regression",
    [](forecasting-regression.html#cb153-10)    y = "megalitres"
    [](forecasting-regression.html#cb153-11)  )

Figure 7.17: Forecasts from the regression model for beer production. The dark shaded region shows 80% prediction intervals and the light shaded region shows 95% prediction intervals. 

### Scenario based forecasting[](forecasting-regression.html#scenario-based-forecasting)

In this setting, the forecaster assumes possible scenarios for the predictor variables that are of interest. For example, a US policy maker may be interested in comparing the predicted change in consumption when there is a constant growth of 1% and 0.5% respectively for income and savings with no change in the employment rate, versus a respective decline of 1% and 0.5%, for each of the four quarters following the end of the sample. The resulting forecasts are calculated below and shown in Figure [7.18](forecasting-regression.html#fig:ConsInc4). We should note that prediction intervals for scenario based forecasts do not include the uncertainty associated with the future values of the predictor variables. They assume that the values of the predictors are known in advance.
    
    
    [](forecasting-regression.html#cb154-1)fit_consBest <- us_change |>
    [](forecasting-regression.html#cb154-2)  model(
    [](forecasting-regression.html#cb154-3)    lm = TSLM(Consumption ~ Income + Savings + Unemployment)
    [](forecasting-regression.html#cb154-4)  )
    [](forecasting-regression.html#cb154-5)future_scenarios <- scenarios(
    [](forecasting-regression.html#cb154-6)  Increase = new_data(us_change, 4) |>
    [](forecasting-regression.html#cb154-7)    mutate(Income=1, Savings=0.5, Unemployment=0),
    [](forecasting-regression.html#cb154-8)  Decrease = new_data(us_change, 4) |>
    [](forecasting-regression.html#cb154-9)    mutate(Income=-1, Savings=-0.5, Unemployment=0),
    [](forecasting-regression.html#cb154-10)  names_to = "Scenario")
    [](forecasting-regression.html#cb154-11)
    [](forecasting-regression.html#cb154-12)fc <- forecast(fit_consBest, new_data = future_scenarios)
    
    
    [](forecasting-regression.html#cb155-1)us_change |>
    [](forecasting-regression.html#cb155-2)  autoplot(Consumption) +
    [](forecasting-regression.html#cb155-3)  autolayer(fc) +
    [](forecasting-regression.html#cb155-4)  labs(title = "US consumption", y = "% change")

Figure 7.18: Forecasting percentage changes in personal consumption expenditure for the US under scenario based forecasting. 

### Building a predictive regression model[](forecasting-regression.html#building-a-predictive-regression-model)

The great advantage of regression models is that they can be used to capture important relationships between the forecast variable of interest and the predictor variables. However, for ex ante forecasts, these models require future values of each predictor, which can be challenging. If forecasting each predictor is too difficult, we may use scenario-based forecasting instead, where we assume specific future values for all predictors.

An alternative formulation is to use as predictors their lagged values. Assuming that we are interested in generating a \\(h\\)-step ahead forecast we write \\[ y_{t+h}=\beta_0+\beta_1x_{1,t}+\dots+\beta_kx_{k,t}+\varepsilon_{t+h} \\] for \\(h=1,2\dots\\). The predictor set is formed by values of the \\(x\\)s that are observed \\(h\\) time periods prior to observing \\(y\\). Therefore when the estimated model is projected into the future, i.e., beyond the end of the sample \\(T\\), all predictor values are available.

Including lagged values of the predictors does not only make the model operational for easily generating forecasts, it also makes it intuitively appealing. For example, the effect of a policy change with the aim of increasing production may not have an instantaneous effect on consumption expenditure. It is most likely that this will happen with a lagging effect. We touched upon this in Section [7.4](useful-predictors.html#useful-predictors) when briefly introducing distributed lags as predictors. Several directions for generalising regression models to better incorporate the rich dynamics observed in time series are discussed in Section [10](dynamic.html#dynamic).

### Prediction intervals[](forecasting-regression.html#prediction-intervals-2)

With each forecast for the change in consumption in Figure [7.18](forecasting-regression.html#fig:ConsInc4), 95% and 80% prediction intervals are also included. The general formulation of how to calculate prediction intervals for multiple regression models is presented in Section [7.9](regression-matrices.html#regression-matrices). As this involves some advanced matrix algebra we present here the case for calculating prediction intervals for a simple regression, where a forecast can be generated using the equation, \\[ \hat{y}=\hat{\beta}_0+\hat{\beta}_1x. \\] Assuming that the regression errors are normally distributed, an approximate 95% prediction interval associated with this forecast is given by \\[\begin{equation} \hat{y} \pm 1.96 \hat{\sigma}_e\sqrt{1+\frac{1}{T}+\frac{(x-\bar{x})^2}{(T-1)s_x^2}}, \tag{7.4} \end{equation}\\] where \\(T\\) is the total number of observations, \\(\bar{x}\\) is the mean of the observed \\(x\\) values, \\(s_x\\) is the standard deviation of the observed \\(x\\) values and \\(\hat{\sigma}_e\\) is the standard error of the regression given by Equation [(7.3)](least-squares.html#eq:Regr-se). Similarly, an 80% prediction interval can be obtained by replacing 1.96 by 1.28. Other prediction intervals can be obtained by replacing the 1.96 with the appropriate value given in Table [5.1](prediction-intervals.html#tab:pcmultipliers). If the `fable` package is used to obtain prediction intervals, more exact calculations are obtained (especially for small values of \\(T\\)) than what is given by Equation [(7.4)](forecasting-regression.html#eq:Regr-pi).

Equation [(7.4)](forecasting-regression.html#eq:Regr-pi) shows that the prediction interval is wider when \\(x\\) is far from \\(\bar{x}\\). That is, we are more certain about our forecasts when considering values of the predictor variable close to its sample mean.

#### Example[](forecasting-regression.html#example-4)

The estimated simple regression line in the US consumption example is \\[ \hat{y}_t=0.54 + 0.27x_t. \\]

Assuming that for the next four quarters, personal income will increase by its historical mean value of \\(\bar{x}=0.73\\)%, consumption is forecast to increase by \\(0.74\\)% and the corresponding 80% and 95% prediction intervals are \\([-0.02, 1.5]\\) and \\([-0.42, 1.9]\\) respectively (calculated using R). If we assume an extreme increase of 12% in income, then the prediction intervals are considerably wider as shown in Figure [7.19](forecasting-regression.html#fig:conSimplePI).
    
    
    [](forecasting-regression.html#cb156-1)fit_cons <- us_change |>
    [](forecasting-regression.html#cb156-2)  model(TSLM(Consumption ~ Income))
    [](forecasting-regression.html#cb156-3)new_cons <- scenarios(
    [](forecasting-regression.html#cb156-4)  "Average increase" = new_data(us_change, 4) |>
    [](forecasting-regression.html#cb156-5)    mutate(Income = mean(us_change$Income)),
    [](forecasting-regression.html#cb156-6)  "Extreme increase" = new_data(us_change, 4) |>
    [](forecasting-regression.html#cb156-7)    mutate(Income = 12),
    [](forecasting-regression.html#cb156-8)  names_to = "Scenario"
    [](forecasting-regression.html#cb156-9))
    [](forecasting-regression.html#cb156-10)fcast <- forecast(fit_cons, new_cons)
    [](forecasting-regression.html#cb156-11)
    [](forecasting-regression.html#cb156-12)us_change |>
    [](forecasting-regression.html#cb156-13)  autoplot(Consumption) +
    [](forecasting-regression.html#cb156-14)  autolayer(fcast) +
    [](forecasting-regression.html#cb156-15)  labs(title = "US consumption", y = "% change")

Figure 7.19: Prediction intervals if income is increased by its historical mean of \\(0.73\\)% versus an extreme increase of 12%. 


---

## 7.7 Nonlinear regression[](nonlinear-regression.html#nonlinear-regression)

Although the linear relationship assumed so far in this chapter is often adequate, there are many cases in which a nonlinear functional form is more suitable. To keep things simple in this section we assume that we only have one predictor \\(x\\).

The simplest way of modelling a nonlinear relationship is to transform the forecast variable \\(y\\) and/or the predictor variable \\(x\\) before estimating a regression model. While this provides a non-linear functional form, the model is still linear in the parameters. The most commonly used transformation is the (natural) logarithm (see Section [3.1](transformations.html#transformations)).

A **log-log** functional form is specified as \\[ \log y=\beta_0+\beta_1 \log x +\varepsilon. \\] In this model, the slope \\(\beta_1\\) can be interpreted as an elasticity: \\(\beta_1\\) is the average percentage change in \\(y\\) resulting from a 1% increase in \\(x\\). Other useful forms can also be specified. The **log-linear** form is specified by only transforming the forecast variable and the **linear-log** form is obtained by transforming the predictor.

Recall that in order to perform a logarithmic transformation to a variable, all of its observed values must be greater than zero. In the case that variable \\(x\\) contains zeros, we use the transformation \\(\log(x+1)\\); i.e., we add one to the value of the variable and then take logarithms. This has a similar effect to taking logarithms but avoids the problem of zeros. It also has the neat side-effect of zeros on the original scale remaining zeros on the transformed scale.

There are cases for which simply transforming the data will not be adequate and a more general specification may be required. Then the model we use is \\[ y=f(x) +\varepsilon \\] where \\(f\\) is a nonlinear function. In standard (linear) regression, \\(f(x)=\beta_{0} + \beta_{1} x\\). In the specification of nonlinear regression that follows, we allow \\(f\\) to be a more flexible nonlinear function of \\(x\\), compared to simply a logarithmic or other transformation.

One of the simplest specifications is to make \\(f\\) **piecewise linear**. That is, we introduce points where the slope of \\(f\\) can change. These points are called **knots**. This can be achieved by letting \\(x_{1}=x\\) and introducing variable \\(x_{2}\\) such that \\[\begin{align*} x_{2} = (x-c)_+ &= \left\\{ \begin{array}{ll} 0 & \text{if } x < c\\\ x-c & \text{if } x \ge c. \end{array}\right. \end{align*}\\] The notation \\((x-c)_+\\) means the value \\(x-c\\) if it is positive and 0 otherwise. This forces the slope to bend at point \\(c\\). Additional bends can be included in the relationship by adding further variables of the above form.

Piecewise linear relationships constructed in this way are a special case of **regression splines**. In general, a linear regression spline is obtained using \\[ x_{1}= x \quad x_{2} = (x-c_{1})_+ \quad\dots\quad x_{k} = (x-c_{k-1})_+ \\] where \\(c_{1},\dots,c_{k-1}\\) are the knots (the points at which the line can bend). Selecting the number of knots (\\(k-1\\)) and where they should be positioned can be difficult and somewhat arbitrary. Some automatic knot selection algorithms are available, but are not widely used.

### Forecasting with a nonlinear trend[](nonlinear-regression.html#forecasting-with-a-nonlinear-trend)

In Section [7.4](useful-predictors.html#useful-predictors) fitting a linear trend to a time series by setting \\(x=t\\) was introduced. The simplest way of fitting a nonlinear trend is using quadratic or higher order trends obtained by specifying \\[ x_{1,t} =t,\quad x_{2,t}=t^2,\quad \dots. \\] However, it is not recommended that quadratic or higher order trends be used in forecasting. When they are extrapolated, the resulting forecasts are often unrealistic.

A better approach is to use the piecewise specification introduced above and fit a piecewise linear trend which bends at some point in time. We can think of this as a nonlinear trend constructed of linear pieces. If the trend bends at time \\(\tau\\), then it can be specified by simply replacing \\(x=t\\) and \\(c=\tau\\) above such that we include the predictors, \\[\begin{align*} x_{1,t} & = t \\\ x_{2,t} &= (t-\tau)_+ = \left\\{ \begin{array}{ll} 0 & \text{if } t < \tau\\\ t-\tau & \text{if } t \ge \tau \end{array}\right. \end{align*}\\] in the model. If the associated coefficients of \\(x_{1,t}\\) and \\(x_{2,t}\\) are \\(\beta_1\\) and \\(\beta_2\\), then \\(\beta_1\\) gives the slope of the trend before time \\(\tau\\), while the slope of the line after time \\(\tau\\) is given by \\(\beta_1+\beta_2\\). Additional bends can be included in the relationship by adding further variables of the form \\((t-\tau)_+\\) where \\(\tau\\) is the “knot” or point in time at which the line should bend.

### Example: Boston marathon winning times[](nonlinear-regression.html#example-boston-marathon-winning-times)

We will fit some trend models to the Boston marathon winning times for men. First we extract the men’s data and convert the winning times to a numerical value. The course was lengthened (from 24.5 miles to 26.2 miles) in 1924, which led to a jump in the winning times, so we only consider data from that date onwards.
    
    
    [](nonlinear-regression.html#cb157-1)boston_men <- boston_marathon |>
    [](nonlinear-regression.html#cb157-2)  filter(Year >= 1924) |>
    [](nonlinear-regression.html#cb157-3)  filter(Event == "Men's open division") |>
    [](nonlinear-regression.html#cb157-4)  mutate(Minutes = as.numeric(Time)/60)

The top panel of Figure [7.20](nonlinear-regression.html#fig:marathonLinear) shows the winning times since 1924. The time series shows a general downward trend as the winning times have been improving over the years. The bottom panel shows the residuals from fitting a linear trend to the data. The plot shows an obvious nonlinear pattern which has not been captured by the linear trend.

Figure 7.20: Fitting a linear trend to the Boston marathon winning times is inadequate 

Fitting an exponential trend (equivalent to a log-linear regression) to the data can be achieved by transforming the \\(y\\) variable so that the model to be fitted is, \\[ \log y_t=\beta_0+\beta_1 t +\varepsilon_t. \\] The fitted exponential trend and forecasts are shown in Figure [7.21](nonlinear-regression.html#fig:marathonNonlinear). Although the exponential trend does not seem to fit the data much better than the linear trend, it perhaps gives a more sensible projection in that the winning times will decrease in the future but at a decaying rate rather than a fixed linear rate.

The plot of winning times reveals three different periods. There is a lot of volatility in the winning times up to about 1950, with the winning times barely declining. After 1950 there is a clear decrease in times, followed by a flattening out after the 1980s, with the suggestion of an upturn towards the end of the sample. To account for these changes, we specify the years 1950 and 1980 as knots. We should warn here that subjective identification of knots can lead to over-fitting, which can be detrimental to the forecast performance of a model, and should be performed with caution.
    
    
    [](nonlinear-regression.html#cb158-1)fit_trends <- boston_men |>
    [](nonlinear-regression.html#cb158-2)  model(
    [](nonlinear-regression.html#cb158-3)    linear = TSLM(Minutes ~ trend()),
    [](nonlinear-regression.html#cb158-4)    exponential = TSLM(log(Minutes) ~ trend()),
    [](nonlinear-regression.html#cb158-5)    piecewise = TSLM(Minutes ~ trend(knots = c(1950, 1980)))
    [](nonlinear-regression.html#cb158-6)  )
    [](nonlinear-regression.html#cb158-7)fc_trends <- fit_trends |> forecast(h = 10)
    [](nonlinear-regression.html#cb158-8)
    [](nonlinear-regression.html#cb158-9)boston_men |>
    [](nonlinear-regression.html#cb158-10)  autoplot(Minutes) +
    [](nonlinear-regression.html#cb158-11)  geom_line(data = fitted(fit_trends),
    [](nonlinear-regression.html#cb158-12)            aes(y = .fitted, colour = .model)) +
    [](nonlinear-regression.html#cb158-13)  autolayer(fc_trends, alpha = 0.5, level = 95) +
    [](nonlinear-regression.html#cb158-14)  labs(y = "Minutes",
    [](nonlinear-regression.html#cb158-15)       title = "Boston marathon winning times")

Figure 7.21: Projecting forecasts from linear, exponential and piecewise linear trends for the Boston marathon winning times. 

Figure [7.21](nonlinear-regression.html#fig:marathonNonlinear) shows the fitted lines and forecasts from linear, exponential and piecewise linear trends. The best forecasts appear to come from the piecewise linear trend.


---

## 7.8 Correlation, causation and forecasting[](causality.html#causality)

### Correlation is not causation[](causality.html#correlation-is-not-causation)

It is important not to confuse correlation with causation, or causation with forecasting. A variable \\(x\\) may be useful for forecasting a variable \\(y\\), but that does not mean \\(x\\) is causing \\(y\\). It is possible that \\(x\\) _is_ causing \\(y\\), but it may be that \\(y\\) is causing \\(x\\), or that the relationship between them is more complicated than simple causality.

For example, it is possible to model the number of drownings at a beach resort each month with the number of ice-creams sold in the same period. The model can give reasonable forecasts, not because ice-creams cause drownings, but because people eat more ice-creams on hot days when they are also more likely to go swimming. So the two variables (ice-cream sales and drownings) are correlated, but one is not causing the other. They are both caused by a third variable (temperature). This is an example of “confounding” — where an omitted variable causes changes in both the response variable and at least one predictor variable.

We describe a variable that is not included in our forecasting model as a **confounder** when it influences both the response variable and at least one predictor variable. Confounding makes it difficult to determine what variables are _causing_ changes in other variables, but it does not necessarily make forecasting more difficult.

Similarly, it is possible to forecast if it will rain in the afternoon by observing the number of cyclists on the road in the morning. When there are fewer cyclists than usual, it is more likely to rain later in the day. The model can give reasonable forecasts, not because cyclists prevent rain, but because people are more likely to cycle when the published weather forecast is for a dry day. In this case, there is a causal relationship, but in the opposite direction to our forecasting model. The number of cyclists falls because there is rain forecast. That is, \\(y\\) (rainfall) is affecting \\(x\\) (cyclists).

It is important to understand that correlations are useful for forecasting, even when there is no causal relationship between the two variables, or when the causality runs in the opposite direction to the model, or when there is confounding.

However, often a better model is possible if a causal mechanism can be determined. A better model for drownings will probably include temperatures and visitor numbers and exclude ice-cream sales. A good forecasting model for rainfall will not include cyclists, but it will include atmospheric observations from the previous few days.

### Forecasting with correlated predictors[](causality.html#forecasting-with-correlated-predictors)

When two or more predictors are highly correlated it is always challenging to accurately separate their individual effects. Suppose we are forecasting monthly sales of a company for 2012, using data from 2000–2011. In January 2008, a new competitor came into the market and started taking some market share. At the same time, the economy began to decline. In your forecasting model, you include both competitor activity (measured using advertising time on a local television station) and the health of the economy (measured using GDP). It will not be possible to separate the effects of these two predictors because they are highly correlated.

Having correlated predictors is not really a problem for forecasting, as we can still compute forecasts without needing to separate out the effects of the predictors. However, it becomes a problem with scenario forecasting as the scenarios should take account of the relationships between predictors. It is also a problem if some historical analysis of the contributions of various predictors is required.

### Multicollinearity and forecasting[](causality.html#multicollinearity-and-forecasting)

A closely related issue is **multicollinearity** , which occurs when similar information is provided by two or more of the predictor variables in a multiple regression.

It can occur when two predictors are highly correlated with each other (that is, they have a correlation coefficient close to +1 or -1). In this case, knowing the value of one of the variables tells you a lot about the value of the other variable. Hence, they are providing similar information. For example, foot size can be used to predict height, but including the size of both left and right feet in the same model is not going to make the forecasts any better, although it won’t make them worse either.

Multicollinearity can also occur when a linear combination of predictors is highly correlated with another linear combination of predictors. In this case, knowing the value of the first group of predictors tells you a lot about the value of the second group of predictors. Hence, they are providing similar information.

An example of this problem is the dummy variable trap discussed in Section [7.4](useful-predictors.html#useful-predictors). Suppose you have quarterly data and use four dummy variables, \\(d_1\\), \\(d_2\\), \\(d_3\\) and \\(d_4\\). Then \\(d_4=1-d_1-d_2-d_3\\), so there is perfect correlation between \\(d_4\\) and \\(d_1+d_2+d_3\\).

In the case of perfect correlation (i.e., a correlation of +1 or -1, such as in the dummy variable trap), it is not possible to estimate the regression model.

If there is high correlation (close to but not equal to +1 or -1), then the estimation of the regression coefficients is computationally difficult. In fact, some software (notably Microsoft Excel) may give highly inaccurate estimates of the coefficients. Most reputable statistical software will use algorithms to limit the effect of multicollinearity on the coefficient estimates, but you do need to be careful. The major software packages such as R, SPSS, SAS and Stata all use estimation algorithms to avoid the problem as much as possible.

When multicollinearity is present, the uncertainty associated with individual regression coefficients will be large. This is because they are difficult to estimate. Consequently, statistical tests (e.g., t-tests) on regression coefficients are unreliable. (In forecasting we are rarely interested in such tests.) Also, it will not be possible to make accurate statements about the contribution of each separate predictor to the forecast.

Forecasts will be unreliable if the values of the future predictors are outside the range of the historical values of the predictors. For example, suppose you have fitted a regression model with predictors \\(x_1\\) and \\(x_2\\) which are highly correlated with each other, and suppose that the values of \\(x_1\\) in the training data ranged between 0 and 100. Then forecasts based on \\(x_1>100\\) or \\(x_1<0\\) will be unreliable. It is always a little dangerous when future values of the predictors lie much outside the historical range, but it is especially problematic when multicollinearity is present.

Note that if you are using good statistical software, if you are not interested in the specific contributions of each predictor, and if the future values of your predictor variables are within their historical ranges, there is nothing to worry about — multicollinearity is not a problem except when there is perfect correlation.


---

## 7.9 Matrix formulation[](regression-matrices.html#regression-matrices)

_Warning: this is a more advanced, optional section and assumes knowledge of matrix algebra._

Recall that multiple regression model can be written as \\[ y_{t} = \beta_{0} + \beta_{1} x_{1,t} + \beta_{2} x_{2,t} + \cdots + \beta_{k} x_{k,t} + \varepsilon_{t} \\] where \\(\varepsilon_{t}\\) has mean zero and variance \\(\sigma^2\\). This expresses the relationship between a single value of the forecast variable and the predictors.

It can be convenient to write this in matrix form where all the values of the forecast variable are given in a single equation. Let \\(\bm{y} = (y_{1},\dots,y_{T})'\\), \\(\bm{\varepsilon} = (\varepsilon_{1},\dots,\varepsilon_{T})'\\), \\(\bm{\beta} = (\beta_{0},\dots,\beta_{k})'\\) and \\[ \bm{X} = \left[ \begin{matrix} 1 & x_{1,1} & x_{2,1} & \dots & x_{k,1}\\\ 1 & x_{1,2} & x_{2,2} & \dots & x_{k,2}\\\ \vdots& \vdots& \vdots&& \vdots\\\ 1 & x_{1,T}& x_{2,T}& \dots& x_{k,T} \end{matrix}\right]. \\] Then \\[ \bm{y} = \bm{X}\bm{\beta} + \bm{\varepsilon} \\] where \\(\bm{\varepsilon}\\) has mean \\(\bm{0}\\) and variance \\(\sigma^2\bm{I}\\). Note that the \\(\bm{X}\\) matrix has \\(T\\) rows reflecting the number of observations and \\(k+1\\) columns reflecting the intercept which is represented by the column of ones plus the number of predictors.

### Least squares estimation[](regression-matrices.html#least-squares-estimation)

Least squares estimation is performed by minimising the expression \\(\bm{\varepsilon}'\bm{\varepsilon} = (\bm{y} - \bm{X}\bm{\beta})'(\bm{y} - \bm{X}\bm{\beta})\\). It can be shown that this is minimised when \\(\bm{\beta}\\) takes the value \\[ \hat{\bm{\beta}} = (\bm{X}'\bm{X})^{-1}\bm{X}'\bm{y}. \\] This is sometimes known as the “normal equation”. The estimated coefficients require the inversion of the matrix \\(\bm{X}'\bm{X}\\). If \\(\bm{X}\\) is not of full column rank then matrix \\(\bm{X}'\bm{X}\\) is singular and the model cannot be estimated. This will occur, for example, if you fall for the “dummy variable trap”, i.e., having the same number of dummy variables as there are categories of a categorical predictor, as discussed in Section [7.4](useful-predictors.html#useful-predictors).

The residual variance is estimated using \\[ \hat{\sigma}_e^2 = \frac{1}{T-k-1}(\bm{y} - \bm{X}\hat{\bm{\beta}})' (\bm{y} - \bm{X}\hat{\bm{\beta}}). \\]

### Fitted values and cross-validation[](regression-matrices.html#fitted-values-and-cross-validation)

The normal equation shows that the fitted values can be calculated using \\[ \bm{\hat{y}} = \bm{X}\hat{\bm{\beta}} = \bm{X}(\bm{X}'\bm{X})^{-1}\bm{X}'\bm{y} = \bm{H}\bm{y}, \\] where \\(\bm{H} = \bm{X}(\bm{X}'\bm{X})^{-1}\bm{X}'\\) is known as the “hat-matrix” because it is used to compute \\(\bm{\hat{y}}\\) (“y-hat”).

If the diagonal values of \\(\bm{H}\\) are denoted by \\(h_{1},\dots,h_{T}\\), then the cross-validation statistic can be computed using \\[ \text{CV} = \frac{1}{T}\sum_{t=1}^T [e_{t}/(1-h_{t})]^2, \\] where \\(e_{t}\\) is the residual obtained from fitting the model to all \\(T\\) observations. Thus, it is not necessary to actually fit \\(T\\) separate models when computing the CV statistic.

### Forecasts and prediction intervals[](regression-matrices.html#forecasts-and-prediction-intervals)

Let \\(\bm{x}^*\\) be a row vector containing the values of the predictors (in the same format as \\(\bm{X}\\)) for which we want to generate a forecast. Then the forecast is given by \\[ \hat{y} = \bm{x}^*\hat{\bm{\beta}}=\bm{x}^*(\bm{X}'\bm{X})^{-1}\bm{X}'\bm{y} \\] and the estimated forecast variance is given by \\[ \hat\sigma_e^2 \left[1 + \bm{x}^* (\bm{X}'\bm{X})^{-1} (\bm{x}^*)'\right]. \\] A 95% prediction interval can be calculated (assuming normally distributed errors) as \\[ \hat{y} \pm 1.96 \hat{\sigma}_e \sqrt{1 + \bm{x}^* (\bm{X}'\bm{X})^{-1} (\bm{x}^*)'}. \\] This takes into account the uncertainty due to the error term \\(\varepsilon\\) and the uncertainty in the coefficient estimates. However, it ignores any errors in \\(\bm{x}^*\\). Thus, if the future values of the predictors are uncertain, then the prediction interval calculated using this expression will be too narrow.


---

## 7.10 Exercises[](regression-exercises.html#regression-exercises)

  1. Half-hourly electricity demand for Victoria, Australia is contained in `vic_elec`. Extract the January 2014 electricity demand, and aggregate this data to daily with daily total demands and maximum temperatures.
         
         [](regression-exercises.html#cb159-1)jan14_vic_elec <- vic_elec |>
         [](regression-exercises.html#cb159-2)  filter(yearmonth(Time) == yearmonth("2014 Jan")) |>
         [](regression-exercises.html#cb159-3)  index_by(Date = as_date(Time)) |>
         [](regression-exercises.html#cb159-4)  summarise(
         [](regression-exercises.html#cb159-5)    Demand = sum(Demand),
         [](regression-exercises.html#cb159-6)    Temperature = max(Temperature)
         [](regression-exercises.html#cb159-7)  )

     1. Plot the data and find the regression model for Demand with temperature as a predictor variable. Why is there a positive relationship?

     2. Produce a residual plot. Is the model adequate? Are there any outliers or influential observations?

     3. Use the model to forecast the electricity demand that you would expect for the next day if the maximum temperature was \\(15^\circ \text{C}\\) and compare it with the forecast if the with maximum temperature was \\(35^\circ \text{C}\\). Do you believe these forecasts? The following R code will get you started:
            
            [](regression-exercises.html#cb160-1)jan14_vic_elec |>
            [](regression-exercises.html#cb160-2)  model(TSLM(Demand ~ Temperature)) |>
            [](regression-exercises.html#cb160-3)  forecast(
            [](regression-exercises.html#cb160-4)    new_data(jan14_vic_elec, 1) |>
            [](regression-exercises.html#cb160-5)      mutate(Temperature = 15)
            [](regression-exercises.html#cb160-6)  ) |>
            [](regression-exercises.html#cb160-7)  autoplot(jan14_vic_elec)

     4. Give prediction intervals for your forecasts.

     5. Plot Demand vs Temperature for all of the available data in `vic_elec` aggregated to daily total demand and maximum temperature. What does this say about your model?

  2. Data set `olympic_running` contains the winning times (in seconds) in each Olympic Games sprint, middle-distance and long-distance track events from 1896 to 2016.

     1. Plot the winning time against the year for each event. Describe the main features of the plot.
     2. Fit a regression line to the data for each event. Obviously the winning times have been decreasing, but at what _average_ rate per year?
     3. Plot the residuals against the year. What does this indicate about the suitability of the fitted lines?
     4. Predict the winning time for each race in the 2020 Olympics. Give a prediction interval for your forecasts. What assumptions have you made in these calculations?


  3. An elasticity coefficient is the ratio of the percentage change in the forecast variable (\\(y\\)) to the percentage change in the predictor variable (\\(x\\)). Mathematically, the elasticity is defined as \\((dy/dx)\times(x/y)\\). Consider the log-log model, \\[ \log y=\beta_0+\beta_1 \log x + \varepsilon. \\] Express \\(y\\) as a function of \\(x\\) and show that the coefficient \\(\beta_1\\) is the elasticity coefficient.

  4. The data set `souvenirs` concerns the monthly sales figures of a shop which opened in January 1987 and sells gifts, souvenirs, and novelties. The shop is situated on the wharf at a beach resort town in Queensland, Australia. The sales volume varies with the seasonal population of tourists. There is a large influx of visitors to the town at Christmas and for the local surfing festival, held every March since 1988. Over time, the shop has expanded its premises, range of products, and staff.

     1. Produce a time plot of the data and describe the patterns in the graph. Identify any unusual or unexpected fluctuations in the time series.
     2. Explain why it is necessary to take logarithms of these data before fitting a model.
     3. Fit a regression model to the logarithms of these sales data with a linear trend, seasonal dummies and a “surfing festival” dummy variable.
     4. Plot the residuals against time and against the fitted values. Do these plots reveal any problems with the model?
     5. Do boxplots of the residuals for each month. Does this reveal any problems with the model?
     6. What do the values of the coefficients tell you about each variable?
     7. What does the Ljung-Box test tell you about your model?
     8. Regardless of your answers to the above questions, use your regression model to predict the monthly sales for 1994, 1995, and 1996. Produce prediction intervals for each of your forecasts.
     9. How could you improve these predictions by modifying the model?
  5. The `us_gasoline` series consists of weekly data for supplies of US finished motor gasoline product, from 2 February 1991 to 20 January 2017. The units are in “million barrels per day”. Consider only the data to the end of 2004.

     1. Fit a harmonic regression with trend to the data. Experiment with changing the number Fourier terms. Plot the observed gasoline and fitted values and comment on what you see.
     2. Select the appropriate number of Fourier terms to include by minimising the AICc or CV value.
     3. Plot the residuals of the final model using the `gg_tsresiduals()` function and comment on these. Use a Ljung-Box test to check for residual autocorrelation.
     4. Generate forecasts for the next year of data and plot these along with the actual data for 2005. Comment on the forecasts.
  6. The annual population of Afghanistan is available in the `global_economy` data set.

     1. Plot the data and comment on its features. Can you observe the effect of the Soviet-Afghan war?
     2. Fit a linear trend model and compare this to a piecewise linear trend model with knots at 1980 and 1989.
     3. Generate forecasts from these two models for the five years after the end of the data, and comment on the results.
  7. _(For advanced readers following on from Section[7.9](regression-matrices.html#regression-matrices))_.

Using matrix notation it was shown that if \\(\bm{y}=\bm{X}\bm{\beta}+\bm{\varepsilon}\\), where \\(\bm{\varepsilon}\\) has mean \\(\bm{0}\\) and variance matrix \\(\sigma^2\bm{I}\\), the estimated coefficients are given by \\(\hat{\bm{\beta}}=(\bm{X}'\bm{X})^{-1}\bm{X}'\bm{y}\\) and a forecast is given by \\(\hat{y}=\bm{x}^*\hat{\bm{\beta}}=\bm{x}^*(\bm{X}'\bm{X})^{-1}\bm{X}'\bm{y}\\) where \\(\bm{x}^*\\) is a row vector containing the values of the predictors for the forecast (in the same format as \\(\bm{X}\\)), and the forecast variance is given by \\(\text{Var}(\hat{y})=\sigma^2 \left[1+\bm{x}^*(\bm{X}'\bm{X})^{-1}(\bm{x}^*)'\right].\\)

Consider the simple time trend model where \\(y_t = \beta_0 + \beta_1t\\). Using the following results, \\[ \sum^{T}_{t=1}{t}=\frac{1}{2}T(T+1),\quad \sum^{T}_{t=1}{t^2}=\frac{1}{6}T(T+1)(2T+1) \\] derive the following expressions:

     1. \\(\displaystyle\bm{X}'\bm{X}=\frac{1}{6}\left[ \begin{array}{cc} 6T & 3T(T+1) \\\ 3T(T+1) & T(T+1)(2T+1) \\\ \end{array} \right]\\)

     2. \\(\displaystyle(\bm{X}'\bm{X})^{-1}=\frac{2}{T(T^2-1)}\left[ \begin{array}{cc} (T+1)(2T+1) & -3(T+1) \\\ -3(T+1) & 6 \\\ \end{array} \right]\\)

     3. \\(\displaystyle\hat{\beta}_0=\frac{2}{T(T-1)}\left[(2T+1)\sum^T_{t=1}y_t-3\sum^T_{t=1}ty_t \right]\\)

\\(\displaystyle\hat{\beta}_1=\frac{6}{T(T^2-1)}\left[2\sum^T_{t=1}ty_t-(T+1)\sum^T_{t=1}y_t \right]\\)

     4. \\(\displaystyle\text{Var}(\hat{y}_{t})=\hat{\sigma}^2\left[1+\frac{2}{T(T-1)}\left(1-4T-6h+6\frac{(T+h)^2}{T+1}\right)\right]\\)




---

## 7.11 Further reading[](regression-reading.html#regression-reading)

There are countless books on regression analysis, but few with a focus on regression for time series and forecasting.

  * A good general and modern book on regression is Sheather ([2009](regression-reading.html#ref-Sheather09)).
  * Another general regression text full of excellent practical advice is Harrell ([2015](regression-reading.html#ref-RMS15)).
  * Ord et al. ([2017](regression-reading.html#ref-Ord2017)) provides a practical coverage of regression models for time series in Chapters 7–9, with a strong emphasis on forecasting.


### Bibliography[](bibliography.html#bibliography)

Harrell, F. E. (2015). _Regression modeling strategies: With applications to linear models, logistic and ordinal regression, and survival analysis_ (2nd ed). Springer. [__](http://amazon.com/dp/3319194240?tag=otexts20)

Ord, J. K., Fildes, R., & Kourentzes, N. (2017). _Principles of business forecasting_ (2nd ed.). Wessex Press Publishing Co. [__](http://amazon.com/dp/0999064916?tag=otexts20)

Sheather, S. J. (2009). _A modern approach to regression with R_. Springer. [__](http://amazon.com/dp/0387096078?tag=otexts20)


---

# Chapter 8 Exponential smoothing[](expsmooth.html#expsmooth)

Exponential smoothing was proposed in the late 1950s ([Brown, 1959](expsmooth.html#ref-Brown59); [Holt, 1957](expsmooth.html#ref-Holt57); [Winters, 1960](expsmooth.html#ref-Winters60)), and has motivated some of the most successful forecasting methods. Forecasts produced using exponential smoothing methods are weighted averages of past observations, with the weights decaying exponentially as the observations get older. In other words, the more recent the observation the higher the associated weight. This framework generates reliable forecasts quickly and for a wide range of time series, which is a great advantage and of major importance to applications in industry.

This chapter is divided into two parts. In the first part (Sections [8.1](ses.html#ses)–[8.4](taxonomy.html#taxonomy)) we present the mechanics of the most important exponential smoothing methods, and their application in forecasting time series with various characteristics. This helps us develop an intuition to how these methods work. In this setting, selecting and using a forecasting method may appear to be somewhat ad hoc. The selection of the method is generally based on recognising key components of the time series (trend and seasonal) and the way in which these enter the smoothing method (e.g., in an additive, damped or multiplicative manner).

In the second part of the chapter (Sections [8.5](ets.html#ets)–[8.7](ets-forecasting.html#ets-forecasting)) we present the statistical models that underlie exponential smoothing methods. These models generate identical point forecasts to the methods discussed in the first part of the chapter, but also generate prediction intervals. Furthermore, this statistical framework allows for genuine model selection between competing models.

### Bibliography[](bibliography.html#bibliography)

Brown, R. G. (1959). _Statistical forecasting for inventory control_. McGraw/Hill. 

Holt, C. C. (1957). _Forecasting seasonals and trends by exponentially weighted averages_ (ONR Memorandum No. 52). Carnegie Institute of Technology, Pittsburgh USA. Reprinted in the _International Journal of Forecasting_ , 2004. [__](https://doi.org/10.1016/j.ijforecast.2003.09.015)

Winters, P. R. (1960). Forecasting sales by exponentially weighted moving averages. _Management Science_ , _6_(3), 324–342. [__](https://doi.org/10.1287/mnsc.6.3.324)


---

## 8.1 Simple exponential smoothing[](ses.html#ses)

The simplest of the exponentially smoothing methods is naturally called **simple exponential smoothing** (SES)[16](ses.html#fn16). This method is suitable for forecasting data with no clear trend or seasonal pattern. For example, the data in Figure [8.1](ses.html#fig:7-oil) do not display any clear trending behaviour or any seasonality. (There is a decline in the last few years, which might suggest a trend. We will consider whether a trended method would be better for this series later in this chapter.) We have already considered the naïve and the average as possible methods for forecasting such data (Section [5.2](simple-methods.html#simple-methods)).
    
    
    [](ses.html#cb161-1)algeria_economy <- global_economy |>
    [](ses.html#cb161-2)  filter(Country == "Algeria")
    [](ses.html#cb161-3)algeria_economy |>
    [](ses.html#cb161-4)  autoplot(Exports) +
    [](ses.html#cb161-5)  labs(y = "% of GDP", title = "Exports: Algeria")

Figure 8.1: Exports of goods and services from Algeria from 1960 to 2017. 

Using the naïve method, all forecasts for the future are equal to the last observed value of the series, \\[ \hat{y}_{T+h|T} = y_{T}, \\] for \\(h=1,2,\dots\\). Hence, the naïve method assumes that the most recent observation is the only important one, and all previous observations provide no information for the future. This can be thought of as a weighted average where all of the weight is given to the last observation.

Using the average method, all future forecasts are equal to a simple average of the observed data, \\[ \hat{y}_{T+h|T} = \frac1T \sum_{t=1}^T y_t, \\] for \\(h=1,2,\dots\\). Hence, the average method assumes that all observations are of equal importance, and gives them equal weights when generating forecasts.

We often want something between these two extremes. For example, it may be sensible to attach larger weights to more recent observations than to observations from the distant past. This is exactly the concept behind simple exponential smoothing. Forecasts are calculated using weighted averages, where the weights decrease exponentially as observations come from further in the past — the smallest weights are associated with the oldest observations: \\[\begin{equation} \hat{y}_{T+1|T} = \alpha y_T + \alpha(1-\alpha) y_{T-1} + \alpha(1-\alpha)^2 y_{T-2}+ \cdots, \tag{8.1} \end{equation}\\] where \\(0 \le \alpha \le 1\\) is the smoothing parameter. The one-step-ahead forecast for time \\(T+1\\) is a weighted average of all of the observations in the series \\(y_1,\dots,y_T\\). The rate at which the weights decrease is controlled by the parameter \\(\alpha\\).

The table below shows the weights attached to observations for four different values of \\(\alpha\\) when forecasting using simple exponential smoothing. Note that the sum of the weights even for a small value of \\(\alpha\\) will be approximately one for any reasonable sample size.

| \\(\alpha=0.2\\) | \\(\alpha=0.4\\) | \\(\alpha=0.6\\) | \\(\alpha=0.8\\)  
---|---|---|---|---  
\\(y_{T}\\) | 0.2000 | 0.4000 | 0.6000 | 0.8000  
\\(y_{T-1}\\) | 0.1600 | 0.2400 | 0.2400 | 0.1600  
\\(y_{T-2}\\) | 0.1280 | 0.1440 | 0.0960 | 0.0320  
\\(y_{T-3}\\) | 0.1024 | 0.0864 | 0.0384 | 0.0064  
\\(y_{T-4}\\) | 0.0819 | 0.0518 | 0.0154 | 0.0013  
\\(y_{T-5}\\) | 0.0655 | 0.0311 | 0.0061 | 0.0003  
  
For any \\(\alpha\\) between 0 and 1, the weights attached to the observations decrease exponentially as we go back in time, hence the name “exponential smoothing”. If \\(\alpha\\) is small (i.e., close to 0), more weight is given to observations from the more distant past. If \\(\alpha\\) is large (i.e., close to 1), more weight is given to the more recent observations. For the extreme case where \\(\alpha=1\\), \\(\hat{y}_{T+1|T}=y_T\\), so the forecasts are equal to the naïve forecasts.

We present two equivalent forms of simple exponential smoothing, each of which leads to the forecast Equation [(8.1)](ses.html#eq:7-ses).

### Weighted average form[](ses.html#weighted-average-form)

The forecast at time \\(T+1\\) is equal to a weighted average between the most recent observation \\(y_T\\) and the previous forecast \\(\hat{y}_{T|T-1}\\): \\[ \hat{y}_{T+1|T} = \alpha y_T + (1-\alpha) \hat{y}_{T|T-1}, \\] where \\(0 \le \alpha \le 1\\) is the smoothing parameter. Similarly, we can write the fitted values as \\[ \hat{y}_{t+1|t} = \alpha y_t + (1-\alpha) \hat{y}_{t|t-1}, \\] for \\(t=1,\dots,T\\). (Recall that fitted values are simply one-step forecasts of the training data.)

The process has to start somewhere, so we let the first fitted value at time 1 be denoted by \\(\ell_0\\) (which we will have to estimate). Then \\[\begin{align*} \hat{y}_{2|1} &= \alpha y_1 + (1-\alpha) \ell_0\\\ \hat{y}_{3|2} &= \alpha y_2 + (1-\alpha) \hat{y}_{2|1}\\\ \hat{y}_{4|3} &= \alpha y_3 + (1-\alpha) \hat{y}_{3|2}\\\ \vdots\\\ \hat{y}_{T|T-1} &= \alpha y_{T-1} + (1-\alpha) \hat{y}_{T-1|T-2}\\\ \hat{y}_{T+1|T} &= \alpha y_T + (1-\alpha) \hat{y}_{T|T-1}. \end{align*}\\] Substituting each equation into the following equation, we obtain \\[\begin{align*} \hat{y}_{3|2} & = \alpha y_2 + (1-\alpha) \left[\alpha y_1 + (1-\alpha) \ell_0\right] \\\ & = \alpha y_2 + \alpha(1-\alpha) y_1 + (1-\alpha)^2 \ell_0 \\\ \hat{y}_{4|3} & = \alpha y_3 + (1-\alpha) [\alpha y_2 + \alpha(1-\alpha) y_1 + (1-\alpha)^2 \ell_0]\\\ & = \alpha y_3 + \alpha(1-\alpha) y_2 + \alpha(1-\alpha)^2 y_1 + (1-\alpha)^3 \ell_0 \\\ & ~~\vdots \\\ \hat{y}_{T+1|T} & = \sum_{j=0}^{T-1} \alpha(1-\alpha)^j y_{T-j} + (1-\alpha)^T \ell_{0}. \end{align*}\\] The last term becomes tiny for large \\(T\\). So, the weighted average form leads to the same forecast Equation [(8.1)](ses.html#eq:7-ses).

### Component form[](ses.html#component-form)

An alternative representation is the component form. For simple exponential smoothing, the only component included is the level, \\(\ell_t\\). (Other methods which are considered later in this chapter may also include a trend \\(b_t\\) and a seasonal component \\(s_t\\).) Component form representations of exponential smoothing methods comprise a forecast equation and a smoothing equation for each of the components included in the method. The component form of simple exponential smoothing is given by: \\[\begin{align*} \text{Forecast equation} && \hat{y}_{t+h|t} & = \ell_{t}\\\ \text{Smoothing equation} && \ell_{t} & = \alpha y_{t} + (1 - \alpha)\ell_{t-1}, \end{align*}\\] where \\(\ell_{t}\\) is the level (or the smoothed value) of the series at time \\(t\\). Setting \\(h=1\\) gives the fitted values, while setting \\(t=T\\) gives the true forecasts beyond the training data.

The forecast equation shows that the forecast value at time \\(t+1\\) is the estimated level at time \\(t\\). The smoothing equation for the level (usually referred to as the level equation) gives the estimated level of the series at each period \\(t\\).

If we replace \\(\ell_t\\) with \\(\hat{y}_{t+1|t}\\) and \\(\ell_{t-1}\\) with \\(\hat{y}_{t|t-1}\\) in the smoothing equation, we will recover the weighted average form of simple exponential smoothing.

The component form of simple exponential smoothing is not particularly useful on its own, but it will be the easiest form to use when we start adding other components.

### Flat forecasts[](ses.html#flat-forecasts)

Simple exponential smoothing has a “flat” forecast function: \\[ \hat{y}_{T+h|T} = \hat{y}_{T+1|T}=\ell_T, \qquad h=2,3,\dots. \\] That is, all forecasts take the same value, equal to the last level component. Remember that these forecasts will only be suitable if the time series has no trend or seasonal component.

### Optimisation[](ses.html#optimisation)

The application of every exponential smoothing method requires the smoothing parameters and the initial values to be chosen. In particular, for simple exponential smoothing, we need to select the values of \\(\alpha\\) and \\(\ell_0\\). All forecasts can be computed from the data once we know those values. For the methods that follow there is usually more than one smoothing parameter and more than one initial component to be chosen.

In some cases, the smoothing parameters may be chosen in a subjective manner — the forecaster specifies the value of the smoothing parameters based on previous experience. However, a more reliable and objective way to obtain values for the unknown parameters is to estimate them from the observed data.

In Section [7.2](least-squares.html#least-squares), we estimated the coefficients of a regression model by minimising the sum of the squared residuals (usually known as SSE or “sum of squared errors”). Similarly, the unknown parameters and the initial values for any exponential smoothing method can be estimated by minimising the SSE. The residuals are specified as \\(e_t=y_t - \hat{y}_{t|t-1}\\) for \\(t=1,\dots,T\\). Hence, we find the values of the unknown parameters and the initial values that minimise \\[\begin{equation} \text{SSE}=\sum_{t=1}^T(y_t - \hat{y}_{t|t-1})^2=\sum_{t=1}^Te_t^2. \tag{8.2} \end{equation}\\]

Unlike the regression case (where we have formulas which return the values of the regression coefficients that minimise the SSE), this involves a non-linear minimisation problem, and we need to use an optimisation tool to solve it.

### Example: Algerian exports[](ses.html#example-algerian-exports)

In this example, simple exponential smoothing is applied to forecast exports of goods and services from Algeria.
    
    
    [](ses.html#cb162-1)# Estimate parameters
    [](ses.html#cb162-2)fit <- algeria_economy |>
    [](ses.html#cb162-3)  model(ETS(Exports ~ error("A") + trend("N") + season("N")))
    [](ses.html#cb162-4)fc <- fit |>
    [](ses.html#cb162-5)  forecast(h = 5)

This gives parameter estimates \\(\hat\alpha=0.84\\) and \\(\hat\ell_0=39.5\\), obtained by minimising SSE over periods \\(t=1,2,\dots,58\\), subject to the restriction that \\(0\le\alpha\le1\\).

In Table [8.1](ses.html#tab:export-ses) we demonstrate the calculation using these parameters. The second last column shows the estimated level for times \\(t=0\\) to \\(t=58\\); the last few rows of the last column show the forecasts for \\(h=1\\) to \\(5\\)-steps ahead.

Table 8.1: Forecasting goods and services exports from Algeria using simple exponential smoothing. Year | Time | Observation | Level | Forecast  
---|---|---|---|---  
| \\(t\\) | \\(y_t\\) | \\(\ell_t\\) | \\(\hat{y}_{t\vert t-1}\\)  
1959 | 0 |  | 39.54 |   
1960 | 1 | 39.04 | 39.12 | 39.54  
1961 | 2 | 46.24 | 45.10 | 39.12  
1962 | 3 | 19.79 | 23.84 | 45.10  
1963 | 4 | 24.68 | 24.55 | 23.84  
1964 | 5 | 25.08 | 25.00 | 24.55  
1965 | 6 | 22.60 | 22.99 | 25.00  
1966 | 7 | 25.99 | 25.51 | 22.99  
1967 | 8 | 23.43 | 23.77 | 25.51  
| ⋮ | ⋮ | ⋮ | ⋮  
2014 | 55 | 30.22 | 30.80 | 33.85  
2015 | 56 | 23.17 | 24.39 | 30.80  
2016 | 57 | 20.86 | 21.43 | 24.39  
2017 | 58 | 22.64 | 22.44 | 21.43  
| \\(h\\) |  |  | \\(\hat{y}_{T+h\vert T}\\)  
2018 | 1 |  |  | 22.44  
2019 | 2 |  |  | 22.44  
2020 | 3 |  |  | 22.44  
2021 | 4 |  |  | 22.44  
2022 | 5 |  |  | 22.44  
  
The black line in Figure [8.2](ses.html#fig:ses) shows the data, which has a changing level over time.
    
    
    [](ses.html#cb163-1)fc |>
    [](ses.html#cb163-2)  autoplot(algeria_economy) +
    [](ses.html#cb163-3)  geom_line(aes(y = .fitted), col="#D55E00",
    [](ses.html#cb163-4)            data = augment(fit)) +
    [](ses.html#cb163-5)  labs(y="% of GDP", title="Exports: Algeria") +
    [](ses.html#cb163-6)  guides(colour = "none")

Figure 8.2: Simple exponential smoothing applied to exports from Algeria (1960–2017). The orange curve shows the one-step-ahead fitted values. 

The forecasts for the period 2018–2022 are plotted in Figure [8.2](ses.html#fig:ses). Also plotted are one-step-ahead fitted values alongside the data over the period 1960–2017. The large value of \\(\alpha\\) in this example is reflected in the large adjustment that takes place in the estimated level \\(\ell_t\\) at each time. A smaller value of \\(\alpha\\) would lead to smaller changes over time, and so the series of fitted values would be smoother.

The prediction intervals shown here are calculated using the methods described in Section [8.7](ets-forecasting.html#ets-forecasting). The prediction intervals show that there is considerable uncertainty in the future exports over the five-year forecast period. So interpreting the point forecasts without accounting for the large uncertainty can be very misleading.

* * *

  16. In some books it is called “single exponential smoothing”.[↩︎](ses.html#fnref16)




---

## 8.2 Methods with trend[](holt.html#holt)

### Holt’s linear trend method[](holt.html#holts-linear-trend-method)

Holt ([1957](holt.html#ref-Holt57)) extended simple exponential smoothing to allow the forecasting of data with a trend. This method involves a forecast equation and two smoothing equations (one for the level and one for the trend): \\[\begin{align*} \text{Forecast equation}&& \hat{y}_{t+h|t} &= \ell_{t} + hb_{t} \\\ \text{Level equation} && \ell_{t} &= \alpha y_{t} + (1 - \alpha)(\ell_{t-1} + b_{t-1})\\\ \text{Trend equation} && b_{t} &= \beta^*(\ell_{t} - \ell_{t-1}) + (1 -\beta^*)b_{t-1}, \end{align*}\\] where \\(\ell_t\\) denotes an estimate of the level of the series at time \\(t\\), \\(b_t\\) denotes an estimate of the trend (slope) of the series at time \\(t\\), \\(\alpha\\) is the smoothing parameter for the level, \\(0\le\alpha\le1\\), and \\(\beta^*\\) is the smoothing parameter for the trend, \\(0\le\beta^*\le1\\). (We denote this as \\(\beta^*\\) instead of \\(\beta\\) for reasons that will be explained in Section [8.5](ets.html#ets).)

As with simple exponential smoothing, the level equation here shows that \\(\ell_t\\) is a weighted average of observation \\(y_t\\) and the one-step-ahead training forecast for time \\(t\\), here given by \\(\ell_{t-1} + b_{t-1}\\). The trend equation shows that \\(b_t\\) is a weighted average of the estimated trend at time \\(t\\) based on \\(\ell_{t} - \ell_{t-1}\\) and \\(b_{t-1}\\), the previous estimate of the trend.

The forecast function is no longer flat but trending. The \\(h\\)-step-ahead forecast is equal to the last estimated level plus \\(h\\) times the last estimated trend value. Hence the forecasts are a linear function of \\(h\\).

### Example: Australian population[](holt.html#example-australian-population)
    
    
    [](holt.html#cb164-1)aus_economy <- global_economy |>
    [](holt.html#cb164-2)  filter(Code == "AUS") |>
    [](holt.html#cb164-3)  mutate(Pop = Population / 1e6)
    [](holt.html#cb164-4)autoplot(aus_economy, Pop) +
    [](holt.html#cb164-5)  labs(y = "Millions", title = "Australian population")

Figure 8.3: Australia’s population, 1960-2017. 

Figure [8.3](holt.html#fig:auspop) shows Australia’s annual population from 1960 to 2017. We will apply Holt’s method to this series. The smoothing parameters, \\(\alpha\\) and \\(\beta^*\\), and the initial values \\(\ell_0\\) and \\(b_0\\) are estimated by minimising the SSE for the one-step training errors as in Section [8.1](ses.html#ses).
    
    
    [](holt.html#cb165-1)fit <- aus_economy |>
    [](holt.html#cb165-2)  model(
    [](holt.html#cb165-3)    AAN = ETS(Pop ~ error("A") + trend("A") + season("N"))
    [](holt.html#cb165-4)  )
    [](holt.html#cb165-5)fc <- fit |> forecast(h = 10)

The estimated smoothing coefficient for the level is \\(\hat{\alpha} = 0.9999\\). The very high value shows that the level changes rapidly in order to capture the highly trended series. The estimated smoothing coefficient for the slope is \\(\hat{\beta}^* = 0.3267\\). This is relatively large suggesting that the trend also changes often (even if the changes are slight).

In Table [8.2](holt.html#tab:popholt) we use these values to demonstrate the application of Holt’s method.

Table 8.2: Forecasting Australian annual population using Holt’s linear trend method. Year | Time | Observation | Level | Slope | Forecast  
---|---|---|---|---|---  
| \\(t\\) | \\(y_t\\) | \\(\ell_t\\) |  | \\(\hat{y}_{t+1\mid t}\\)  
1959 | 0 |  | 10.05 | 0.22 |   
1960 | 1 | 10.28 | 10.28 | 0.22 | 10.28  
1961 | 2 | 10.48 | 10.48 | 0.22 | 10.50  
1962 | 3 | 10.74 | 10.74 | 0.23 | 10.70  
1963 | 4 | 10.95 | 10.95 | 0.22 | 10.97  
1964 | 5 | 11.17 | 11.17 | 0.22 | 11.17  
1965 | 6 | 11.39 | 11.39 | 0.22 | 11.39  
1966 | 7 | 11.65 | 11.65 | 0.23 | 11.61  
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮  
2014 | 55 | 23.50 | 23.50 | 0.37 | 23.52  
2015 | 56 | 23.85 | 23.85 | 0.36 | 23.87  
2016 | 57 | 24.21 | 24.21 | 0.36 | 24.21  
2017 | 58 | 24.60 | 24.60 | 0.37 | 24.57  
| \\(h\\) |  |  |  | \\(\hat{y}_{T+h\mid T}\\)  
2018 | 1 |  |  |  | 24.97  
2019 | 2 |  |  |  | 25.34  
2020 | 3 |  |  |  | 25.71  
2021 | 4 |  |  |  | 26.07  
2022 | 5 |  |  |  | 26.44  
2023 | 6 |  |  |  | 26.81  
2024 | 7 |  |  |  | 27.18  
2025 | 8 |  |  |  | 27.55  
2026 | 9 |  |  |  | 27.92  
2027 | 10 |  |  |  | 28.29  
  
### Damped trend methods[](holt.html#damped-trend-methods)

The forecasts generated by Holt’s linear method display a constant trend (increasing or decreasing) indefinitely into the future. Empirical evidence indicates that these methods tend to over-forecast, especially for longer forecast horizons. Motivated by this observation, Gardner & McKenzie ([1985](holt.html#ref-GarMacK1985)) introduced a parameter that “dampens” the trend to a flat line some time in the future. Methods that include a damped trend have proven to be very successful, and are arguably the most popular individual methods when forecasts are required automatically for many series.

In conjunction with the smoothing parameters \\(\alpha\\) and \\(\beta^*\\) (with values between 0 and 1 as in Holt’s method), this method also includes a damping parameter \\(0<\phi<1\\): \\[\begin{align*} \hat{y}_{t+h|t} &= \ell_{t} + (\phi+\phi^2 + \dots + \phi^{h})b_{t} \\\ \ell_{t} &= \alpha y_{t} + (1 - \alpha)(\ell_{t-1} + \phi b_{t-1})\\\ b_{t} &= \beta^*(\ell_{t} - \ell_{t-1}) + (1 -\beta^*)\phi b_{t-1}. \end{align*}\\] If \\(\phi=1\\), the method is identical to Holt’s linear method. For values between \\(0\\) and \\(1\\), \\(\phi\\) dampens the trend so that it approaches a constant some time in the future. In fact, the forecasts converge to \\(\ell_T+\phi b_T/(1-\phi)\\) as \\(h\rightarrow\infty\\) for any value \\(0<\phi<1\\). This means that short-run forecasts are trended while long-run forecasts are constant.

In practice, \\(\phi\\) is rarely less than 0.8 as the damping has a very strong effect for smaller values. Values of \\(\phi\\) close to 1 will mean that a damped model is not able to be distinguished from a non-damped model. For these reasons, we usually restrict \\(\phi\\) to a minimum of 0.8 and a maximum of 0.98.

### Example: Australian Population (continued)[](holt.html#example-australian-population-continued)

Figure [8.4](holt.html#fig:dampedtrend) shows the forecasts for years 2018–2032 generated from Holt’s linear trend method and the damped trend method.
    
    
    [](holt.html#cb166-1)aus_economy |>
    [](holt.html#cb166-2)  model(
    [](holt.html#cb166-3)    `Holt's method` = ETS(Pop ~ error("A") +
    [](holt.html#cb166-4)                       trend("A") + season("N")),
    [](holt.html#cb166-5)    `Damped Holt's method` = ETS(Pop ~ error("A") +
    [](holt.html#cb166-6)                       trend("Ad", phi = 0.9) + season("N"))
    [](holt.html#cb166-7)  ) |>
    [](holt.html#cb166-8)  forecast(h = 15) |>
    [](holt.html#cb166-9)  autoplot(aus_economy, level = NULL) +
    [](holt.html#cb166-10)  labs(title = "Australian population",
    [](holt.html#cb166-11)       y = "Millions") +
    [](holt.html#cb166-12)  guides(colour = guide_legend(title = "Forecast"))

Figure 8.4: Forecasting annual Australian population (millions) over 2018-2032. For the damped trend method, \\(\phi=0.90\\). 

We have set the damping parameter to a relatively low number \\((\phi=0.90)\\) to exaggerate the effect of damping for comparison. Usually, we would estimate \\(\phi\\) along with the other parameters. We have also used a rather large forecast horizon (\\(h=15\\)) to highlight the difference between a damped trend and a linear trend.

### Example: Internet usage[](holt.html#example-internet-usage)

In this example, we compare the forecasting performance of the three exponential smoothing methods that we have considered so far in forecasting the number of users connected to the internet via a server. The data is observed over 100 minutes and is shown in Figure [8.5](holt.html#fig:www-usage).
    
    
    [](holt.html#cb167-1)www_usage <- as_tsibble(WWWusage)
    [](holt.html#cb167-2)www_usage |> autoplot(value) +
    [](holt.html#cb167-3)  labs(x="Minute", y="Number of users",
    [](holt.html#cb167-4)       title = "Internet usage per minute")

Figure 8.5: Users connected to the internet through a server 

We will use time series cross-validation to compare the one-step forecast accuracy of the three methods.
    
    
    [](holt.html#cb168-1)www_usage |>
    [](holt.html#cb168-2)  stretch_tsibble(.init = 10) |>
    [](holt.html#cb168-3)  model(
    [](holt.html#cb168-4)    SES = ETS(value ~ error("A") + trend("N") + season("N")),
    [](holt.html#cb168-5)    Holt = ETS(value ~ error("A") + trend("A") + season("N")),
    [](holt.html#cb168-6)    Damped = ETS(value ~ error("A") + trend("Ad") +
    [](holt.html#cb168-7)                   season("N"))
    [](holt.html#cb168-8)  ) |>
    [](holt.html#cb168-9)  forecast(h = 1) |>
    [](holt.html#cb168-10)  accuracy(www_usage)
    [](holt.html#cb168-11)#> # A tibble: 3 × 10
    [](holt.html#cb168-12)#>   .model .type     ME  RMSE   MAE   MPE  MAPE  MASE RMSSE  ACF1
    [](holt.html#cb168-13)#>   <chr>  <chr>  <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl>
    [](holt.html#cb168-14)#> 1 Damped Test  0.288   3.69  3.00 0.347  2.26 0.663 0.636 0.336
    [](holt.html#cb168-15)#> 2 Holt   Test  0.0610  3.87  3.17 0.244  2.38 0.701 0.668 0.296
    [](holt.html#cb168-16)#> 3 SES    Test  1.46    6.05  4.81 0.904  3.55 1.06  1.04  0.803

Damped Holt’s method is best whether you compare MAE or RMSE values. So we will proceed with using the damped Holt’s method and apply it to the whole data set to get forecasts for future minutes.
    
    
    [](holt.html#cb169-1)fit <- www_usage |>
    [](holt.html#cb169-2)  model(
    [](holt.html#cb169-3)    Damped = ETS(value ~ error("A") + trend("Ad") +
    [](holt.html#cb169-4)                   season("N"))
    [](holt.html#cb169-5)  )
    [](holt.html#cb169-6)# Estimated parameters:
    [](holt.html#cb169-7)tidy(fit)
    [](holt.html#cb169-8)#> # A tibble: 5 × 3
    [](holt.html#cb169-9)#>   .model term  estimate
    [](holt.html#cb169-10)#>   <chr>  <chr>    <dbl>
    [](holt.html#cb169-11)#> 1 Damped alpha   1.000 
    [](holt.html#cb169-12)#> 2 Damped beta    0.997 
    [](holt.html#cb169-13)#> 3 Damped phi     0.815 
    [](holt.html#cb169-14)#> 4 Damped l[0]   90.4   
    [](holt.html#cb169-15)#> 5 Damped b[0]   -0.0173

The smoothing parameter for the slope is estimated to be almost one, indicating that the trend changes to mostly reflect the slope between the last two minutes of internet usage. The value of \\(\alpha\\) is very close to one, showing that the level reacts strongly to each new observation.
    
    
    [](holt.html#cb170-1)fit |>
    [](holt.html#cb170-2)  forecast(h = 10) |>
    [](holt.html#cb170-3)  autoplot(www_usage) +
    [](holt.html#cb170-4)  labs(x="Minute", y="Number of users",
    [](holt.html#cb170-5)       title = "Internet usage per minute")

Figure 8.6: Forecasting internet usage: comparing forecasting performance of non-seasonal methods. 

The resulting forecasts look sensible with decreasing trend, which flattens out due to the low value of the damping parameter (0.815), and relatively wide prediction intervals reflecting the variation in the historical data. The prediction intervals are calculated using the methods described in Section [8.7](ets-forecasting.html#ets-forecasting).

In this example, the process of selecting a method was relatively easy as both MSE and MAE comparisons suggested the same method (damped Holt’s). However, sometimes different accuracy measures will suggest different forecasting methods, and then a decision is required as to which forecasting method we prefer to use. As forecasting tasks can vary by many dimensions (length of forecast horizon, size of test set, forecast error measures, frequency of data, etc.), it is unlikely that one method will be better than all others for all forecasting scenarios. What we require from a forecasting method are consistently sensible forecasts, and these should be frequently evaluated against the task at hand.

### Bibliography[](bibliography.html#bibliography)

Gardner, E. S., & McKenzie, E. (1985). Forecasting trends in time series. _Management Science_ , _31_(10), 1237–1246. [__](https://doi.org/10.1287/mnsc.31.10.1237)

Holt, C. C. (1957). _Forecasting seasonals and trends by exponentially weighted averages_ (ONR Memorandum No. 52). Carnegie Institute of Technology, Pittsburgh USA. Reprinted in the _International Journal of Forecasting_ , 2004. [__](https://doi.org/10.1016/j.ijforecast.2003.09.015)


---

## 8.3 Methods with seasonality[](holt-winters.html#holt-winters)

Holt ([1957](holt-winters.html#ref-Holt57)) and Winters ([1960](holt-winters.html#ref-Winters60)) extended Holt’s method to capture seasonality. The Holt-Winters seasonal method comprises the forecast equation and three smoothing equations — one for the level \\(\ell_t\\), one for the trend \\(b_t\\), and one for the seasonal component \\(s_t\\), with corresponding smoothing parameters \\(\alpha\\), \\(\beta^*\\) and \\(\gamma\\). We use \\(m\\) to denote the period of the seasonality, i.e., the number of seasons in a year. For example, for quarterly data \\(m=4\\), and for monthly data \\(m=12\\).

There are two variations to this method that differ in the nature of the seasonal component. The additive method is preferred when the seasonal variations are roughly constant through the series, while the multiplicative method is preferred when the seasonal variations are changing proportional to the level of the series. With the additive method, the seasonal component is expressed in absolute terms in the scale of the observed series, and in the level equation the series is seasonally adjusted by subtracting the seasonal component. Within each year, the seasonal component will add up to approximately zero. With the multiplicative method, the seasonal component is expressed in relative terms (percentages), and the series is seasonally adjusted by dividing through by the seasonal component. Within each year, the seasonal component will sum up to approximately \\(m\\).

### Holt-Winters’ additive method[](holt-winters.html#holt-winters-additive-method)

The component form for the additive method is: \\[\begin{align*} \hat{y}_{t+h|t} &= \ell_{t} + hb_{t} + s_{t+h-m(k+1)} \\\ \ell_{t} &= \alpha(y_{t} - s_{t-m}) + (1 - \alpha)(\ell_{t-1} + b_{t-1})\\\ b_{t} &= \beta^*(\ell_{t} - \ell_{t-1}) + (1 - \beta^*)b_{t-1}\\\ s_{t} &= \gamma (y_{t}-\ell_{t-1}-b_{t-1}) + (1-\gamma)s_{t-m}, \end{align*}\\] where \\(k\\) is the integer part of \\((h-1)/m\\), which ensures that the estimates of the seasonal indices used for forecasting come from the final year of the sample. The level equation shows a weighted average between the seasonally adjusted observation \\((y_{t} - s_{t-m})\\) and the non-seasonal forecast \\((\ell_{t-1}+b_{t-1})\\) for time \\(t\\). The trend equation is identical to Holt’s linear method. The seasonal equation shows a weighted average between the current seasonal index, \\((y_{t}-\ell_{t-1}-b_{t-1})\\), and the seasonal index of the same season last year (i.e., \\(m\\) time periods ago).

The equation for the seasonal component is often expressed as \\[ s_{t} = \gamma^* (y_{t}-\ell_{t})+ (1-\gamma^*)s_{t-m}. \\] If we substitute \\(\ell_t\\) from the smoothing equation for the level of the component form above, we get \\[ s_{t} = \gamma^*(1-\alpha) (y_{t}-\ell_{t-1}-b_{t-1})+ [1-\gamma^*(1-\alpha)]s_{t-m}, \\] which is identical to the smoothing equation for the seasonal component we specify here, with \\(\gamma=\gamma^*(1-\alpha)\\). The usual parameter restriction is \\(0\le\gamma^*\le1\\), which translates to \\(0\le\gamma\le 1-\alpha\\).

### Holt-Winters’ multiplicative method[](holt-winters.html#holt-winters-multiplicative-method)

The component form for the multiplicative method is: \\[\begin{align*} \hat{y}_{t+h|t} &= (\ell_{t} + hb_{t})s_{t+h-m(k+1)} \\\ \ell_{t} &= \alpha \frac{y_{t}}{s_{t-m}} + (1 - \alpha)(\ell_{t-1} + b_{t-1})\\\ b_{t} &= \beta^*(\ell_{t}-\ell_{t-1}) + (1 - \beta^*)b_{t-1} \\\ s_{t} &= \gamma \frac{y_{t}}{(\ell_{t-1} + b_{t-1})} + (1 - \gamma)s_{t-m}. \end{align*}\\]

### Example: Domestic overnight trips in Australia[](holt-winters.html#example-domestic-overnight-trips-in-australia)

We apply Holt-Winters’ method with both additive and multiplicative seasonality[17](holt-winters.html#fn17) to forecast quarterly visitor nights in Australia spent by domestic tourists. Figure [8.7](holt-winters.html#fig:7-HW) shows the data from 1998–2017, and the forecasts for 2018–2020. The data show an obvious seasonal pattern, with peaks observed in the March quarter of each year, corresponding to the Australian summer.
    
    
    [](holt-winters.html#cb171-1)aus_holidays <- tourism |>
    [](holt-winters.html#cb171-2)  filter(Purpose == "Holiday") |>
    [](holt-winters.html#cb171-3)  summarise(Trips = sum(Trips)/1e3)
    [](holt-winters.html#cb171-4)fit <- aus_holidays |>
    [](holt-winters.html#cb171-5)  model(
    [](holt-winters.html#cb171-6)    additive = ETS(Trips ~ error("A") + trend("A") +
    [](holt-winters.html#cb171-7)                                                season("A")),
    [](holt-winters.html#cb171-8)    multiplicative = ETS(Trips ~ error("M") + trend("A") +
    [](holt-winters.html#cb171-9)                                                season("M"))
    [](holt-winters.html#cb171-10)  )
    [](holt-winters.html#cb171-11)fc <- fit |> forecast(h = "3 years")
    [](holt-winters.html#cb171-12)fc |>
    [](holt-winters.html#cb171-13)  autoplot(aus_holidays, level = NULL) +
    [](holt-winters.html#cb171-14)  labs(title="Australian domestic tourism",
    [](holt-winters.html#cb171-15)       y="Overnight trips (millions)") +
    [](holt-winters.html#cb171-16)  guides(colour = guide_legend(title = "Forecast"))

Figure 8.7: Forecasting domestic overnight trips in Australia using the Holt-Winters method with both additive and multiplicative seasonality. 

Table 8.3: Applying Holt-Winters’ method with additive seasonality for forecasting domestic tourism in Australia. Notice that the additive seasonal component sums to approximately zero. The smoothing parameters are \\(\alpha = 0.2620\\), \\(\beta^* = 0.1646\\), \\(\gamma = 0.0001\\) and RMSE \\(=0.4169\\). Quarter | Time | Observation | Level | Slope | Season | Forecast  
---|---|---|---|---|---|---  
| \\(t\\) | \\(y_t\\) | \\(\ell_t\\) | \\(b_t\\) | \\(s_t\\) | \\(\hat{y}_{t+1\vert t}\\)  
1997 Q1 | 0 |  |  |  | 1.5 |   
1997 Q2 | 1 |  |  |  | -0.3 |   
1997 Q3 | 2 |  |  |  | -0.7 |   
1997 Q4 | 3 |  | 9.8 | 0.0 | -0.5 |   
1998 Q1 | 4 | 11.8 | 9.9 | 0.0 | 1.5 | 11.3  
1998 Q2 | 5 | 9.3 | 9.9 | 0.0 | -0.3 | 9.7  
1998 Q3 | 6 | 8.6 | 9.7 | -0.0 | -0.7 | 9.2  
1998 Q4 | 7 | 9.3 | 9.8 | 0.0 | -0.5 | 9.2  
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮  
2017 Q1 | 80 | 12.4 | 10.9 | 0.1 | 1.5 | 12.3  
2017 Q2 | 81 | 10.5 | 10.9 | 0.1 | -0.3 | 10.7  
2017 Q3 | 82 | 10.5 | 11.0 | 0.1 | -0.7 | 10.3  
2017 Q4 | 83 | 11.2 | 11.3 | 0.1 | -0.5 | 10.6  
| \\(h\\) |  |  |  |  | \\(\hat{y}_{T+h\vert T}\\)  
2018 Q1 | 1 |  |  |  |  | 12.9  
2018 Q2 | 2 |  |  |  |  | 11.2  
2018 Q3 | 3 |  |  |  |  | 11.0  
2018 Q4 | 4 |  |  |  |  | 11.2  
2019 Q1 | 5 |  |  |  |  | 13.4  
2019 Q2 | 6 |  |  |  |  | 11.7  
2019 Q3 | 7 |  |  |  |  | 11.5  
2019 Q4 | 8 |  |  |  |  | 11.7  
2020 Q1 | 9 |  |  |  |  | 13.9  
2020 Q2 | 10 |  |  |  |  | 12.2  
2020 Q3 | 11 |  |  |  |  | 11.9  
2020 Q4 | 12 |  |  |  |  | 12.2  
Table 8.4: Applying Holt-Winters’ method with multiplicative seasonality for forecasting domestic tourism in Australia. Notice that the multiplicative seasonal component sums to approximately \\(m=4\\). The smoothing parameters are \\(\alpha = 0.2237\\), \\(\beta^* = 0.1360\\), \\(\gamma = 0.0001\\) and RMSE \\(=0.4122\\). Quarter | Time | Observation | Level | Slope | Season | Forecast  
---|---|---|---|---|---|---  
| \\(t\\) | \\(y_t\\) | \\(\ell_t\\) | \\(b_t\\) | \\(s_t\\) | \\(\hat{y}_{t+1\vert t}\\)  
1997 Q1 | 0 |  |  |  | 1.2 |   
1997 Q2 | 1 |  |  |  | 1.0 |   
1997 Q3 | 2 |  |  |  | 0.9 |   
1997 Q4 | 3 |  | 10.0 | -0.0 | 0.9 |   
1998 Q1 | 4 | 11.8 | 10.0 | -0.0 | 1.2 | 11.6  
1998 Q2 | 5 | 9.3 | 9.9 | -0.0 | 1.0 | 9.7  
1998 Q3 | 6 | 8.6 | 9.8 | -0.0 | 0.9 | 9.2  
1998 Q4 | 7 | 9.3 | 9.8 | -0.0 | 0.9 | 9.2  
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮  
2017 Q1 | 80 | 12.4 | 10.8 | 0.1 | 1.2 | 12.6  
2017 Q2 | 81 | 10.5 | 10.9 | 0.1 | 1.0 | 10.6  
2017 Q3 | 82 | 10.5 | 11.1 | 0.1 | 0.9 | 10.2  
2017 Q4 | 83 | 11.2 | 11.3 | 0.1 | 0.9 | 10.5  
| \\(h\\) |  |  |  |  | \\(\hat{y}_{T+h\vert T}\\)  
2018 Q1 | 1 |  |  |  |  | 13.3  
2018 Q2 | 2 |  |  |  |  | 11.2  
2018 Q3 | 3 |  |  |  |  | 10.8  
2018 Q4 | 4 |  |  |  |  | 11.1  
2019 Q1 | 5 |  |  |  |  | 13.8  
2019 Q2 | 6 |  |  |  |  | 11.7  
2019 Q3 | 7 |  |  |  |  | 11.3  
2019 Q4 | 8 |  |  |  |  | 11.6  
2020 Q1 | 9 |  |  |  |  | 14.4  
2020 Q2 | 10 |  |  |  |  | 12.2  
2020 Q3 | 11 |  |  |  |  | 11.7  
2020 Q4 | 12 |  |  |  |  | 12.1  
  
The applications of both methods (with additive and multiplicative seasonality) are presented in Tables [8.3](holt-winters.html#tab:tab75) and [8.4](holt-winters.html#tab:tab76) respectively. Because both methods have exactly the same number of parameters to estimate, we can compare the training RMSE from both models. In this case, the method with multiplicative seasonality fits the data slightly better.

The estimated components for both models are plotted in Figure [8.8](holt-winters.html#fig:fig-7-LevelTrendSeas). The small value of \\(\gamma\\) for the multiplicative model means that the seasonal component hardly changes over time. The small value of \\(\beta^{*}\\) means the slope component hardly changes over time (compare the vertical scales of the slope and level components).

Figure 8.8: Estimated components for the Holt-Winters method with additive and multiplicative seasonal components. 

### Holt-Winters’ damped method[](holt-winters.html#holt-winters-damped-method)

Damping is possible with both additive and multiplicative Holt-Winters’ methods. A method that often provides accurate and robust forecasts for seasonal data is the Holt-Winters method with a damped trend and multiplicative seasonality: \\[\begin{align*} \hat{y}_{t+h|t} &= \left[\ell_{t} + (\phi+\phi^2 + \dots + \phi^{h})b_{t}\right]s_{t+h-m(k+1)} \\\ \ell_{t} &= \alpha(y_{t} / s_{t-m}) + (1 - \alpha)(\ell_{t-1} + \phi b_{t-1})\\\ b_{t} &= \beta^*(\ell_{t} - \ell_{t-1}) + (1 - \beta^*)\phi b_{t-1} \\\ s_{t} &= \gamma \frac{y_{t}}{(\ell_{t-1} + \phi b_{t-1})} + (1 - \gamma)s_{t-m}. \end{align*}\\]

### Example: Holt-Winters method with daily data[](holt-winters.html#example-holt-winters-method-with-daily-data)

The Holt-Winters method can also be used for daily type of data, where the seasonal period is \\(m=7\\), and the appropriate unit of time for \\(h\\) is in days. Here we forecast pedestrian traffic at a busy Melbourne train station in July 2016.
    
    
    [](holt-winters.html#cb172-1)sth_cross_ped <- pedestrian |>
    [](holt-winters.html#cb172-2)  filter(Date >= "2016-07-01",
    [](holt-winters.html#cb172-3)         Sensor == "Southern Cross Station") |>
    [](holt-winters.html#cb172-4)  index_by(Date) |>
    [](holt-winters.html#cb172-5)  summarise(Count = sum(Count)/1000)
    [](holt-winters.html#cb172-6)sth_cross_ped |>
    [](holt-winters.html#cb172-7)  filter(Date <= "2016-07-31") |>
    [](holt-winters.html#cb172-8)  model(
    [](holt-winters.html#cb172-9)    hw = ETS(Count ~ error("M") + trend("Ad") + season("M"))
    [](holt-winters.html#cb172-10)  ) |>
    [](holt-winters.html#cb172-11)  forecast(h = "2 weeks") |>
    [](holt-winters.html#cb172-12)  autoplot(sth_cross_ped |> filter(Date <= "2016-08-14")) +
    [](holt-winters.html#cb172-13)  labs(title = "Daily traffic: Southern Cross",
    [](holt-winters.html#cb172-14)       y="Pedestrians ('000)")

Figure 8.9: Forecasts of daily pedestrian traffic at the Southern Cross railway station, Melbourne. 

Clearly the model has identified the weekly seasonal pattern and the increasing trend at the end of the data, and the forecasts are a close match to the test data.

### Bibliography[](bibliography.html#bibliography)

Holt, C. C. (1957). _Forecasting seasonals and trends by exponentially weighted averages_ (ONR Memorandum No. 52). Carnegie Institute of Technology, Pittsburgh USA. Reprinted in the _International Journal of Forecasting_ , 2004. [__](https://doi.org/10.1016/j.ijforecast.2003.09.015)

Winters, P. R. (1960). Forecasting sales by exponentially weighted moving averages. _Management Science_ , _6_(3), 324–342. [__](https://doi.org/10.1287/mnsc.6.3.324)

* * *

  17. Our implementation uses maximum likelihood estimation as described in Section [8.6](ets-estimation.html#ets-estimation) while Holt and Winters originally minimized the sum of squared errors. For multiplicative seasonality, this will lead to slightly different parameter estimates. Optimizing the sum of squared errors can be obtained by setting `opt_crit="mse"` in `ETS()`.[↩︎](holt-winters.html#fnref17)




---

## 8.4 A taxonomy of exponential smoothing methods[](taxonomy.html#taxonomy)

Exponential smoothing methods are not restricted to those we have presented so far. By considering variations in the combinations of the trend and seasonal components, nine exponential smoothing methods are possible, listed in Table [8.5](taxonomy.html#tab:taxonomy). Each method is labelled by a pair of letters (T,S) defining the type of ‘Trend’ and ‘Seasonal’ components. For example, (A,M) is the method with an additive trend and multiplicative seasonality; (A\\(_d\\),N) is the method with damped trend and no seasonality; and so on.

Table 8.5: A two-way classification of exponential smoothing methods.  Trend Component  |  Seasonal Component   
---|---  
|  N  |  A  |  M   
|  (None)  |  (Additive)  |  (Multiplicative)   
N (None)  |  (N,N)  |  (N,A)  |  (N,M)   
A (Additive)  |  (A,N)  |  (A,A)  |  (A,M)   
A\\(_d\\) (Additive damped)  |  (A\\(_d\\),N)  |  (A\\(_d\\),A)  |  (A\\(_d\\),M)   
  
Some of these methods we have already seen using other names:

Short hand | Method  
---|---  
(N,N) | Simple exponential smoothing  
(A,N) | Holt’s linear method  
(A\\(_d\\),N) | Additive damped trend method  
(A,A) | Additive Holt-Winters’ method  
(A,M) | Multiplicative Holt-Winters’ method  
(A\\(_d\\),M) | Holt-Winters’ damped method  
  
This type of classification was first proposed by Pegels ([1969](taxonomy.html#ref-Pegels1969)), who also included a method with a multiplicative trend. It was later extended by Gardner ([1985](taxonomy.html#ref-Gar1985)) to include methods with an additive damped trend and by J. W. Taylor ([2003](taxonomy.html#ref-Taylor2003)) to include methods with a multiplicative damped trend. We do not consider the multiplicative trend methods in this book as they tend to produce poor forecasts. See Hyndman et al. ([2008](taxonomy.html#ref-expsmooth08)) for a more thorough discussion of all exponential smoothing methods.

Table [8.6](taxonomy.html#tab:pegels) gives the recursive formulas for applying the nine exponential smoothing methods in Table [8.5](taxonomy.html#tab:taxonomy). Each cell includes the forecast equation for generating \\(h\\)-step-ahead forecasts, and the smoothing equations for applying the method.

Table 8.6:  Formulas for recursive calculations and point forecasts. In each case, \\(\ell_t\\) denotes the series level at time \\(t\\), \\(b_t\\) denotes the slope at time \\(t\\), \\(s_t\\) denotes the seasonal component of the series at time \\(t\\), and \\(m\\) denotes the number of seasons in a year; \\(\alpha\\), \\(\beta^*\\), \\(\gamma\\) and \\(\phi\\) are smoothing parameters, \\(\phi_h = \phi+\phi^2+\dots+\phi^{h}\\), and \\(k\\) is the integer part of \\((h-1)/m\\).  
  
### Bibliography[](bibliography.html#bibliography)

Gardner, E. S. (1985). Exponential smoothing: The state of the art. _Journal of Forecasting_ , _4_(1), 1–28. [__](https://doi.org/10.1002/for.3980040103)

Hyndman, R. J., Koehler, A. B., Ord, J. K., & Snyder, R. D. (2008). _Forecasting with exponential smoothing: The state space approach_. Springer-Verlag. [__](http://www.exponentialsmoothing.net)

Pegels, C. C. (1969). Exponential forecasting: Some new variations. _Management Science_ , _15_(5), 311–315. [__](https://doi.org/10.1287/mnsc.15.5.311)

Taylor, J. W. (2003). Exponential smoothing with a damped multiplicative trend. _International Journal of Forecasting_ , _19_(4), 715–725. [__](https://doi.org/10.1016/S0169-2070\(03\)00003-7)


---

## 8.5 Innovations state space models for exponential smoothing[](ets.html#ets)

In the rest of this chapter, we study the statistical models that underlie the exponential smoothing methods we have considered so far. The exponential smoothing methods presented in Table [8.6](taxonomy.html#tab:pegels) are algorithms which generate point forecasts. The statistical models in this section generate the same point forecasts, but can also generate prediction (or forecast) intervals. A statistical model is a stochastic (or random) data generating process that can produce an entire forecast distribution. We will also describe how to use the model selection criteria introduced in Chapter [7](regression.html#regression) to choose the model in an objective manner.

Each model consists of a measurement equation that describes the observed data, and some state equations that describe how the unobserved components or states (level, trend, seasonal) change over time. Hence, these are referred to as **state space models**.

For each method there exist two models: one with additive errors and one with multiplicative errors. The point forecasts produced by the models are identical if they use the same smoothing parameter values. They will, however, generate different prediction intervals.

To distinguish between a model with additive errors and one with multiplicative errors (and also to distinguish the models from the methods), we add a third letter to the classification of Table [8.5](taxonomy.html#tab:taxonomy). We label each state space model as ETS(\\(\cdot,\cdot,\cdot\\)) for (Error, Trend, Seasonal). This label can also be thought of as ExponenTial Smoothing. Using the same notation as in Table [8.5](taxonomy.html#tab:taxonomy), the possibilities for each component (or state) are: Error \\(=\\{\\)A,M\\(\\}\\), Trend \\(=\\{\\)N,A,A\\(_d\\}\\) and Seasonal \\(=\\{\\)N,A,M\\(\\}\\).

### ETS(A,N,N): simple exponential smoothing with additive errors[](ets.html#etsann-simple-exponential-smoothing-with-additive-errors)

Recall the component form of simple exponential smoothing: \\[\begin{align*} \text{Forecast equation} && \hat{y}_{t+1|t} & = \ell_{t}\\\ \text{Smoothing equation} && \ell_{t} & = \alpha y_{t} + (1 - \alpha)\ell_{t-1}. \end{align*}\\] If we re-arrange the smoothing equation for the level, we get the “error correction” form, \\[\begin{align*} \ell_{t} %&= \alpha y_{t}+\ell_{t-1}-\alpha\ell_{t-1}\\\ &= \ell_{t-1}+\alpha( y_{t}-\ell_{t-1})\\\ &= \ell_{t-1}+\alpha e_{t}, \end{align*}\\] where \\(e_{t}=y_{t}-\ell_{t-1}=y_{t}-\hat{y}_{t|t-1}\\) is the residual at time \\(t\\).

The training data errors lead to the adjustment of the estimated level throughout the smoothing process for \\(t=1,\dots,T\\). For example, if the error at time \\(t\\) is negative, then \\(y_t < \hat{y}_{t|t-1}\\) and so the level at time \\(t-1\\) has been over-estimated. The new level \\(\ell_t\\) is then the previous level \\(\ell_{t-1}\\) adjusted downwards. The closer \\(\alpha\\) is to one, the “rougher” the estimate of the level (large adjustments take place). The smaller the \\(\alpha\\), the “smoother” the level (small adjustments take place).

We can also write \\(y_t = \ell_{t-1} + e_t\\), so that each observation can be represented by the previous level plus an error. To make this into an innovations state space model, all we need to do is specify the probability distribution for \\(e_t\\). For a model with additive errors, we assume that residuals (the one-step training errors) \\(e_t\\) are normally distributed white noise with mean 0 and variance \\(\sigma^2\\). A short-hand notation for this is \\(e_t = \varepsilon_t\sim\text{NID}(0,\sigma^2)\\); NID stands for “normally and independently distributed”.

Then the equations of the model can be written as \\[\begin{align} y_t &= \ell_{t-1} + \varepsilon_t \tag{8.3}\\\ \ell_t&=\ell_{t-1}+\alpha \varepsilon_t. \tag{8.4} \end{align}\\] We refer to [(8.3)](ets.html#eq:ann-1a) as the _measurement_ (or observation) equation and [(8.4)](ets.html#eq:ann-2a) as the _state_ (or transition) equation. These two equations, together with the statistical distribution of the errors, form a fully specified statistical model. Specifically, these constitute an innovations state space model underlying simple exponential smoothing.

The term “innovations” comes from the fact that all equations use the same random error process, \\(\varepsilon_t\\). For the same reason, this formulation is also referred to as a “single source of error” model. There are alternative multiple source of error formulations which we do not present here.

The measurement equation shows the relationship between the observations and the unobserved states. In this case, observation \\(y_t\\) is a linear function of the level \\(\ell_{t-1}\\), the predictable part of \\(y_t\\), and the error \\(\varepsilon_t\\), the unpredictable part of \\(y_t\\). For other innovations state space models, this relationship may be nonlinear.

The state equation shows the evolution of the state through time. The influence of the smoothing parameter \\(\alpha\\) is the same as for the methods discussed earlier. For example, \\(\alpha\\) governs the amount of change in successive levels: high values of \\(\alpha\\) allow rapid changes in the level; low values of \\(\alpha\\) lead to smooth changes. If \\(\alpha=0\\), the level of the series does not change over time; if \\(\alpha=1\\), the model reduces to a random walk model, \\(y_t=y_{t-1}+\varepsilon_t\\). (See Section [9.1](stationarity.html#stationarity) for a discussion of this model.)

### ETS(M,N,N): simple exponential smoothing with multiplicative errors[](ets.html#etsmnn-simple-exponential-smoothing-with-multiplicative-errors)

In a similar fashion, we can specify models with multiplicative errors by writing the one-step-ahead training errors as relative errors \\[ \varepsilon_t = \frac{y_t-\hat{y}_{t|t-1}}{\hat{y}_{t|t-1}} \\] where \\(\varepsilon_t \sim \text{NID}(0,\sigma^2)\\). Substituting \\(\hat{y}_{t|t-1}=\ell_{t-1}\\) gives \\(y_t = \ell_{t-1}+\ell_{t-1}\varepsilon_t\\) and \\(e_t = y_t - \hat{y}_{t|t-1} = \ell_{t-1}\varepsilon_t\\).

Then we can write the multiplicative form of the state space model as \\[\begin{align*} y_t&=\ell_{t-1}(1+\varepsilon_t)\\\ \ell_t&=\ell_{t-1}(1+\alpha \varepsilon_t). \end{align*}\\]

### ETS(A,A,N): Holt’s linear method with additive errors[](ets.html#etsaan-holts-linear-method-with-additive-errors)

For this model, we assume that the one-step-ahead training errors are given by \\(\varepsilon_t=y_t-\ell_{t-1}-b_{t-1} \sim \text{NID}(0,\sigma^2)\\). Substituting this into the error correction equations for Holt’s linear method we obtain \\[\begin{align*} y_t&=\ell_{t-1}+b_{t-1}+\varepsilon_t\\\ \ell_t&=\ell_{t-1}+b_{t-1}+\alpha \varepsilon_t\\\ b_t&=b_{t-1}+\beta \varepsilon_t, \end{align*}\\] where for simplicity we have set \\(\beta=\alpha \beta^*\\).

### ETS(M,A,N): Holt’s linear method with multiplicative errors[](ets.html#etsman-holts-linear-method-with-multiplicative-errors)

Specifying one-step-ahead training errors as relative errors such that \\[ \varepsilon_t=\frac{y_t-(\ell_{t-1}+b_{t-1})}{(\ell_{t-1}+b_{t-1})} \\] and following an approach similar to that used above, the innovations state space model underlying Holt’s linear method with multiplicative errors is specified as \\[\begin{align*} y_t&=(\ell_{t-1}+b_{t-1})(1+\varepsilon_t)\\\ \ell_t&=(\ell_{t-1}+b_{t-1})(1+\alpha \varepsilon_t)\\\ b_t&=b_{t-1}+\beta(\ell_{t-1}+b_{t-1}) \varepsilon_t, \end{align*}\\]

where again \\(\beta=\alpha \beta^*\\) and \\(\varepsilon_t \sim \text{NID}(0,\sigma^2)\\).

### Other ETS models[](ets.html#other-ets-models)

In a similar fashion, we can write an innovations state space model for each of the exponential smoothing methods of Table [8.6](taxonomy.html#tab:pegels). Table [8.7](ets.html#tab:ssm) presents the equations for all of the models in the ETS framework.

Table 8.7:  State space equations for each of the models in the ETS framework.  


---

## 8.6 Estimation and model selection[](ets-estimation.html#ets-estimation)  
  
### Estimating ETS models[](ets-estimation.html#estimating-ets-models)

An alternative to estimating the parameters by minimising the sum of squared errors is to maximise the “likelihood”. The likelihood is the probability of the data arising from the specified model. Thus, a large likelihood is associated with a good model. For an additive error model, maximising the likelihood (assuming normally distributed errors) gives the same results as minimising the sum of squared errors. However, different results will be obtained for multiplicative error models. In this section, we will estimate the smoothing parameters \\(\alpha\\), \\(\beta\\), \\(\gamma\\) and \\(\phi\\), and the initial states \\(\ell_0\\), \\(b_0\\), \\(s_0,s_{-1},\dots,s_{-m+1}\\), by maximising the likelihood.

The possible values that the smoothing parameters can take are restricted. Traditionally, the parameters have been constrained to lie between 0 and 1 so that the equations can be interpreted as weighted averages. That is, \\(0< \alpha,\beta^*,\gamma^*,\phi<1\\). For the state space models, we have set \\(\beta=\alpha\beta^*\\) and \\(\gamma=(1-\alpha)\gamma^*\\). Therefore, the traditional restrictions translate to \\(0< \alpha <1\\), \\(0 < \beta < \alpha\\) and \\(0< \gamma < 1-\alpha\\). In practice, the damping parameter \\(\phi\\) is usually constrained further to prevent numerical difficulties in estimating the model. In the `fable` package, it is restricted so that \\(0.8<\phi<0.98\\).

Another way to view the parameters is through a consideration of the mathematical properties of the state space models. The parameters are constrained in order to prevent observations in the distant past having a continuing effect on current forecasts. This leads to some _admissibility_ constraints on the parameters, which are usually (but not always) less restrictive than the traditional constraints region ([Hyndman et al., 2008, pp. 149–161](ets-estimation.html#ref-expsmooth08)). For example, for the ETS(A,N,N) model, the traditional parameter region is \\(0< \alpha <1\\) but the admissible region is \\(0< \alpha <2\\). For the ETS(A,A,N) model, the traditional parameter region is \\(0<\alpha<1\\) and \\(0<\beta<\alpha\\) but the admissible region is \\(0<\alpha<2\\) and \\(0<\beta<4-2\alpha\\).

### Model selection[](ets-estimation.html#model-selection)

A great advantage of the ETS statistical framework is that information criteria can be used for model selection. The AIC, AIC\\(_{\text{c}}\\) and BIC, introduced in Section [7.5](selecting-predictors.html#selecting-predictors), can be used here to determine which of the ETS models is most appropriate for a given time series.

For ETS models, Akaike’s Information Criterion (AIC) is defined as \\[ \text{AIC} = -2\log(L) + 2k, \\] where \\(L\\) is the likelihood of the model and \\(k\\) is the total number of parameters and initial states that have been estimated (including the residual variance).

The AIC corrected for small sample bias (AIC\\(_\text{c}\\)) is defined as \\[ \text{AIC}_{\text{c}} = \text{AIC} + \frac{2k(k+1)}{T-k-1}, \\] and the Bayesian Information Criterion (BIC) is \\[ \text{BIC} = \text{AIC} + k[\log(T)-2]. \\]

Three of the combinations of (Error, Trend, Seasonal) can lead to numerical difficulties. Specifically, the models that can cause such instabilities are ETS(A,N,M), ETS(A,A,M), and ETS(A,A\\(_d\\),M), due to division by values potentially close to zero in the state equations. We normally do not consider these particular combinations when selecting a model.

Models with multiplicative errors are useful when the data are strictly positive, but are not numerically stable when the data contain zeros or negative values. Therefore, multiplicative error models will not be considered if the time series is not strictly positive. In that case, only the six fully additive models will be applied.

### Example: Domestic holiday tourist visitor nights in Australia[](ets-estimation.html#example-domestic-holiday-tourist-visitor-nights-in-australia)

We now employ the ETS statistical framework to forecast Australian holiday tourism over the period 2016–2019. We let the `ETS()` function select the model by minimising the AICc.
    
    
    [](ets-estimation.html#cb173-1)aus_holidays <- tourism |>
    [](ets-estimation.html#cb173-2)  filter(Purpose == "Holiday") |>
    [](ets-estimation.html#cb173-3)  summarise(Trips = sum(Trips)/1e3)
    [](ets-estimation.html#cb173-4)fit <- aus_holidays |>
    [](ets-estimation.html#cb173-5)  model(ETS(Trips))
    [](ets-estimation.html#cb173-6)report(fit)
    [](ets-estimation.html#cb173-7)#> Series: Trips 
    [](ets-estimation.html#cb173-8)#> Model: ETS(M,N,A) 
    [](ets-estimation.html#cb173-9)#>   Smoothing parameters:
    [](ets-estimation.html#cb173-10)#>     alpha = 0.3484 
    [](ets-estimation.html#cb173-11)#>     gamma = 1e-04 
    [](ets-estimation.html#cb173-12)#> 
    [](ets-estimation.html#cb173-13)#>   Initial states:
    [](ets-estimation.html#cb173-14)#>   l[0]    s[0]   s[-1]   s[-2] s[-3]
    [](ets-estimation.html#cb173-15)#>  9.727 -0.5376 -0.6884 -0.2934 1.519
    [](ets-estimation.html#cb173-16)#> 
    [](ets-estimation.html#cb173-17)#>   sigma^2:  0.0022
    [](ets-estimation.html#cb173-18)#> 
    [](ets-estimation.html#cb173-19)#>   AIC  AICc   BIC 
    [](ets-estimation.html#cb173-20)#> 226.2 227.8 242.9

The model selected is ETS(M,N,A) \\[\begin{align*} y_{t} &= (\ell_{t-1}+s_{t-m})(1 + \varepsilon_t)\\\ \ell_t &= \ell_{t-1} + \alpha(\ell_{t-1}+s_{t-m})\varepsilon_t\\\ s_t &= s_{t-m} + \gamma(\ell_{t-1}+s_{t-m}) \varepsilon_t. \end{align*}\\]

The parameter estimates are \\(\hat\alpha= 0.3484\\), and \\(\hat\gamma=0.0001\\). The output also returns the estimates for the initial states \\(\ell_0\\), \\(s_{0}\\), \\(s_{-1}\\), \\(s_{-2}\\) and \\(s_{-3}.\\) Compare these with the values obtained for the Holt-Winters method with additive seasonality presented in Table [8.3](holt-winters.html#tab:tab75).

Figure [8.10](ets-estimation.html#fig:MNAstates) shows the states over time, while Figure [8.12](ets-forecasting.html#fig:MNAforecasts) shows point forecasts and prediction intervals generated from the model. The small values of \\(\gamma\\) indicate that the seasonal states change very little over time.
    
    
    [](ets-estimation.html#cb174-1)components(fit) |>
    [](ets-estimation.html#cb174-2)  autoplot() +
    [](ets-estimation.html#cb174-3)  labs(title = "ETS(M,N,A) components")

Figure 8.10: Graphical representation of the estimated states over time. 

Because this model has multiplicative errors, the innovation residuals are not equivalent to the regular residuals (i.e., the one-step training errors). The innovation residuals are given by \\(\hat{\varepsilon}_t\\), while the regular residuals are defined as \\(y_t - \hat{y}_{t|t-1}\\). We can obtain both using the `augment()` function. They are plotted in Figure [8.11](ets-estimation.html#fig:MNAresiduals).

Figure 8.11: Residuals and one-step forecast errors from the ETS(M,N,A) model. 

### Bibliography[](bibliography.html#bibliography)

Hyndman, R. J., Koehler, A. B., Ord, J. K., & Snyder, R. D. (2008). _Forecasting with exponential smoothing: The state space approach_. Springer-Verlag. [__](http://www.exponentialsmoothing.net)


---

## 8.7 Forecasting with ETS models[](ets-forecasting.html#ets-forecasting)

Point forecasts can be obtained from the models by iterating the equations for \\(t=T+1,\dots,T+h\\) and setting all \\(\varepsilon_t=0\\) for \\(t>T\\).

For example, for model ETS(M,A,N), \\(y_{T+1} = (\ell_T + b_T )(1+ \varepsilon_{T+1}).\\) Therefore \\(\hat{y}_{T+1|T}=\ell_{T}+b_{T}.\\) Similarly, \\[\begin{align*} y_{T+2} &= (\ell_{T+1} + b_{T+1})(1 + \varepsilon_{T+2})\\\ &= \left[ (\ell_T + b_T) (1+ \alpha\varepsilon_{T+1}) + b_T + \beta (\ell_T + b_T)\varepsilon_{T+1} \right] (1 + \varepsilon_{T+2}). \end{align*}\\] Therefore, \\(\hat{y}_{T+2|T}= \ell_{T}+2b_{T},\\) and so on. These forecasts are identical to the forecasts from Holt’s linear method, and also to those from model ETS(A,A,N). Thus, the point forecasts obtained from the method and from the two models that underlie the method are identical (assuming that the same parameter values are used). ETS point forecasts constructed in this way are equal to the means of the forecast distributions, except for the models with multiplicative seasonality ([Hyndman et al., 2008](ets-forecasting.html#ref-expsmooth08)).

To obtain forecasts from an ETS model, we use the `forecast()` function from the `fable` package. This function will always return the means of the forecast distribution, even when they differ from these traditional point forecasts.
    
    
    [](ets-forecasting.html#cb175-1)fit |>
    [](ets-forecasting.html#cb175-2)  forecast(h = 8) |>
    [](ets-forecasting.html#cb175-3)  autoplot(aus_holidays)+
    [](ets-forecasting.html#cb175-4)  labs(title="Australian domestic tourism",
    [](ets-forecasting.html#cb175-5)       y="Overnight trips (millions)")

Figure 8.12: Forecasting Australian domestic overnight trips using an ETS(M,N,A) model. 

### Prediction intervals[](ets-forecasting.html#prediction-intervals-3)

A big advantage of the statistical models is that prediction intervals can also be generated — something that cannot be done using the point forecasting methods alone. The prediction intervals will differ between models with additive and multiplicative methods.

For most ETS models, a prediction interval can be written as \\[ \hat{y}_{T+h|T} \pm c \sigma_h \\] where \\(c\\) depends on the coverage probability, and \\(\sigma_h^2\\) is the forecast variance. Values for \\(c\\) were given in Table [5.1](prediction-intervals.html#tab:pcmultipliers). For ETS models, formulas for \\(\sigma_h^2\\) can be complicated; the details are given in Chapter 6 of Hyndman et al. ([2008](ets-forecasting.html#ref-expsmooth08)). In Table [8.8](ets-forecasting.html#tab:pitable) we give the formulas for the additive ETS models, which are the simplest.

Table 8.8: Forecast variance expressions for each additive state space model, where \\(\sigma^2\\) is the residual variance, \\(m\\) is the seasonal period, and \\(k\\) is the integer part of \\((h-1) /m\\) (i.e., the number of complete years in the forecast period prior to time \\(T+h\\)).  Model  |  Forecast variance: \\(\sigma_h^2\\)  
---|---  
(A,N,N)  |  \\(\sigma_h^2 = \sigma^2\big[1 + \alpha^2(h-1)\big]\\)  
(A,A,N)  |  \\(\sigma_h^2 = \sigma^2\Big[1 + (h-1)\big\\{\alpha^2 + \alpha\beta h + \frac16\beta^2h(2h-1)\big\\}\Big]\\)  
(A,A\\(_d\\),N)  |  \\(\sigma_h^2 = \sigma^2\biggl[1 + \alpha^2(h-1) + \frac{\beta\phi h}{(1-\phi)^2} \left\\{2\alpha(1-\phi) +\beta\phi\right\\}\\)  
|  \\(\mbox{} - \frac{\beta\phi(1-\phi^h)}{(1-\phi)^2(1-\phi^2)} \left\\{ 2\alpha(1-\phi^2)+ \beta\phi(1+2\phi-\phi^h)\right\\}\biggr]\\)  
(A,N,A)  |  \\(\sigma_h^2 = \sigma^2\Big[1 + \alpha^2(h-1) + \gamma k(2\alpha+\gamma)\Big]\\)  
(A,A,A)  |  \\(\sigma_h^2 = \sigma^2\Big[1 + (h-1)\big\\{\alpha^2 + \alpha\beta h + \frac16\beta^2h(2h-1)\big\\}\\)  
|  \\(\mbox{} + \gamma k \big\\{2\alpha+ \gamma + \beta m (k+1)\big\\} \Big]\\)  
(A,A\\(_d\\),A)  |  \\(\sigma_h^2 = \sigma^2\biggl[1 + \alpha^2(h-1) + \gamma k(2\alpha+\gamma)\\)  
|  \\(\mbox{} +\frac{\beta\phi h}{(1-\phi)^2} \left\\{2\alpha(1-\phi) + \beta\phi \right\\}\\)  
|  \\(\mbox{} - \frac{\beta\phi(1-\phi^h)}{(1-\phi)^2(1-\phi^2)} \left\\{ 2\alpha(1-\phi^2)+ \beta\phi(1+2\phi-\phi^h)\right\\}\\)  
|  \\(\mbox{} + \frac{2\beta\gamma\phi}{(1-\phi)(1-\phi^m)}\left\\{k(1-\phi^m) - \phi^m(1-\phi^{mk})\right\\}\biggr]\\)  
  
For a few ETS models, there are no known formulas for prediction intervals. In these cases, the `forecast()` function uses simulated future sample paths and computes prediction intervals from the percentiles of these simulated future paths.

### Bibliography[](bibliography.html#bibliography)

Hyndman, R. J., Koehler, A. B., Ord, J. K., & Snyder, R. D. (2008). _Forecasting with exponential smoothing: The state space approach_. Springer-Verlag. [__](http://www.exponentialsmoothing.net)


---

## 8.8 Exercises[](expsmooth-exercises.html#expsmooth-exercises)

  1. Consider the the number of pigs slaughtered in Victoria, available in the `aus_livestock` dataset.

     1. Use the `ETS()` function to estimate the equivalent model for simple exponential smoothing. Find the optimal values of \\(\alpha\\) and \\(\ell_0\\), and generate forecasts for the next four months.
     2. Compute a 95% prediction interval for the first forecast using \\(\hat{y} \pm 1.96s\\) where \\(s\\) is the standard deviation of the residuals. Compare your interval with the interval produced by R.
  2. Write your own function to implement simple exponential smoothing. The function should take arguments `y` (the time series), `alpha` (the smoothing parameter \\(\alpha\\)) and `level` (the initial level \\(\ell_0\\)). It should return the forecast of the next observation in the series. Does it give the same forecast as `ETS()`?

  3. Modify your function from the previous exercise to return the sum of squared errors rather than the forecast of the next observation. Then use the `optim()` function to find the optimal values of \\(\alpha\\) and \\(\ell_0\\). Do you get the same values as the `ETS()` function?

  4. Combine your previous two functions to produce a function that both finds the optimal values of \\(\alpha\\) and \\(\ell_0\\), and produces a forecast of the next observation in the series.

  5. Data set `global_economy` contains the annual Exports from many countries. Select one country to analyse.

     1. Plot the Exports series and discuss the main features of the data.
     2. Use an ETS(A,N,N) model to forecast the series, and plot the forecasts.
     3. Compute the RMSE values for the training data.
     4. Compare the results to those from an ETS(A,A,N) model. (Remember that the trended model is using one more parameter than the simpler model.) Discuss the merits of the two forecasting methods for this data set.
     5. Compare the forecasts from both methods. Which do you think is best?
     6. Calculate a 95% prediction interval for the first forecast for each model, using the RMSE values and assuming normal errors. Compare your intervals with those produced using R.
  6. Forecast the Chinese GDP from the `global_economy` data set using an ETS model. Experiment with the various options in the `ETS()` function to see how much the forecasts change with damped trend, or with a Box-Cox transformation. Try to develop an intuition of what each is doing to the forecasts.

[Hint: use a relatively large value of `h` when forecasting, so you can clearly see the differences between the various options when plotting the forecasts.]

  7. Find an ETS model for the Gas data from `aus_production` and forecast the next few years. Why is multiplicative seasonality necessary here? Experiment with making the trend damped. Does it improve the forecasts?

  8. Recall your retail time series data (from Exercise 7 in Section [2.10](graphics-exercises.html#graphics-exercises)).

     1. Why is multiplicative seasonality necessary for this series?
     2. Apply Holt-Winters’ multiplicative method to the data. Experiment with making the trend damped.
     3. Compare the RMSE of the one-step forecasts from the two methods. Which do you prefer?
     4. Check that the residuals from the best method look like white noise.
     5. Now find the test set RMSE, while training the model to the end of 2010. Can you beat the seasonal naïve approach from Exercise 7 in Section [5.11](toolbox-exercises.html#toolbox-exercises)?
  9. For the same retail data, try an STL decomposition applied to the Box-Cox transformed series, followed by ETS on the seasonally adjusted data. How does that compare with your best previous forecasts on the test set?

  10. Compute the total domestic overnight trips across Australia from the `tourism` dataset.

     1. Plot the data and describe the main features of the series.
     2. Decompose the series using STL and obtain the seasonally adjusted data.
     3. Forecast the next two years of the series using an additive damped trend method applied to the seasonally adjusted data. (This can be specified using `decomposition_model()`.)
     4. Forecast the next two years of the series using an appropriate model for Holt’s linear method applied to the seasonally adjusted data (as before but without damped trend).
     5. Now use `ETS()` to choose a seasonal model for the data.
     6. Compare the RMSE of the ETS model with the RMSE of the models you obtained using STL decompositions. Which gives the better in-sample fits?
     7. Compare the forecasts from the three approaches? Which seems most reasonable?
     8. Check the residuals of your preferred model.
  11. For this exercise use the quarterly number of arrivals to Australia from New Zealand, 1981 Q1 – 2012 Q3, from data set `aus_arrivals`.

     1. Make a time plot of your data and describe the main features of the series.
     2. Create a training set that withholds the last two years of available data. Forecast the test set using an appropriate model for Holt-Winters’ multiplicative method.
     3. Why is multiplicative seasonality necessary here?
     4. Forecast the two-year test set using each of the following methods: 
        * an ETS model;
        * an additive ETS model applied to a log transformed series;
        * a seasonal naïve method;
        * an STL decomposition applied to the log transformed data followed by an ETS model applied to the seasonally adjusted (transformed) data.
     5. Which method gives the best forecasts? Does it pass the residual tests?
     6. Compare the same four methods using time series cross-validation instead of using a training and test set. Do you come to the same conclusions?
  12.      1. Apply cross-validation techniques to produce 1 year ahead ETS and seasonal naïve forecasts for Portland cement production (from `aus_production`). Use a stretching data window with initial size of 5 years, and increment the window by one observation.
     2. Compute the MSE of the resulting \\(4\\)-step-ahead errors. Comment on which forecasts are more accurate. Is this what you expected?
  13. Compare `ETS()`, `SNAIVE()` and `decomposition_model(STL, ???)` on the following five time series. You might need to use a Box-Cox transformation for the STL decomposition forecasts. Use a test set of three years to decide what gives the best forecasts.

     * Beer and bricks production from `aus_production`.
     * Cost of drug subsidies for diabetes (`ATC2 == "A10"`) and corticosteroids (`ATC2 == "H02"`) from `PBS`.
     * Total food retailing turnover for Australia from `aus_retail`.
  14.      1. Use `ETS()` to select an appropriate model for the following series: total number of trips across Australia using `tourism`, the closing prices for the four stocks in `gafa_stock`, and the lynx series in `pelt`. Does it always give good forecasts?

     2. Find an example where it does not work well. Can you figure out why?

  15. Show that the point forecasts from an ETS(M,A,M) model are the same as those obtained using Holt-Winters’ multiplicative method.

  16. Show that the forecast variance for an ETS(A,N,N) model is given by \\[ \sigma^2\left[1+\alpha^2(h-1)\right]. \\]

  17. Write down 95% prediction intervals for an ETS(A,N,N) model as a function of \\(\ell_T\\), \\(\alpha\\), \\(h\\) and \\(\sigma\\), assuming normally distributed errors.




---

## 8.9 Further reading[](expsmooth-reading.html#expsmooth-reading)

  * Two articles by Ev Gardner ([Gardner, 1985](expsmooth-reading.html#ref-Gar1985), [2006](expsmooth-reading.html#ref-Gar2006)) provide a great overview of the history of exponential smoothing, and its many variations.
  * A full book treatment of the subject providing the mathematical details is given by Hyndman et al. ([2008](expsmooth-reading.html#ref-expsmooth08)).


### Bibliography[](bibliography.html#bibliography)

Gardner, E. S. (1985). Exponential smoothing: The state of the art. _Journal of Forecasting_ , _4_(1), 1–28. [__](https://doi.org/10.1002/for.3980040103)

Gardner, E. S. (2006). Exponential smoothing: The state of the art — Part II. _International Journal of Forecasting_ , _22_ , 637–666. [__](https://doi.org/10.1016/j.ijforecast.2006.03.005)

Hyndman, R. J., Koehler, A. B., Ord, J. K., & Snyder, R. D. (2008). _Forecasting with exponential smoothing: The state space approach_. Springer-Verlag. [__](http://www.exponentialsmoothing.net)


---

# Chapter 9 ARIMA models[](arima.html#arima)

ARIMA models provide another approach to time series forecasting. Exponential smoothing and ARIMA models are the two most widely used approaches to time series forecasting, and provide complementary approaches to the problem. While exponential smoothing models are based on a description of the trend and seasonality in the data, ARIMA models aim to describe the autocorrelations in the data.

Before we introduce ARIMA models, we must first discuss the concept of stationarity and the technique of differencing time series.


---

## 9.1 Stationarity and differencing[](stationarity.html#stationarity)

A stationary time series is one whose statistical properties do not depend on the time at which the series is observed.[18](stationarity.html#fn18) Thus, time series with trends, or with seasonality, are not stationary — the trend and seasonality will affect the value of the time series at different times. On the other hand, a white noise series is stationary — it does not matter when you observe it, it should look much the same at any point in time.

Some cases can be confusing — a time series with cyclic behaviour (but with no trend or seasonality) is stationary. This is because the cycles are not of a fixed length, so before we observe the series we cannot be sure where the peaks and troughs of the cycles will be.

In general, a stationary time series will have no predictable patterns in the long-term. Time plots will show the series to be roughly horizontal (although some cyclic behaviour is possible), with constant variance.

Figure 9.1: Which of these series are stationary? (a) Google closing stock price in 2015; (b) Daily change in the Google stock price in 2015; (c) Annual number of strikes in the US; (d) Monthly sales of new one-family houses sold in the US; (e) Annual price of a dozen eggs in the US (constant dollars); (f) Monthly total of pigs slaughtered in Victoria, Australia; (g) Annual total of Canadian Lynx furs traded by the Hudson Bay Company; (h) Quarterly Australian beer production; (i) Monthly Australian gas production. 

Consider the nine series plotted in Figure [9.1](stationarity.html#fig:stationary). Which of these do you think are stationary?

Obvious seasonality rules out series (d), (h) and (i). Trends and changing levels rules out series (a), (c), (e), (f) and (i). Increasing variance also rules out (i). That leaves only (b) and (g) as stationary series.

At first glance, the strong cycles in series (g) might appear to make it non-stationary. But these cycles are aperiodic — they are caused when the lynx population becomes too large for the available feed, so that they stop breeding and the population falls to low numbers, then the regeneration of their food sources allows the population to grow again, and so on. In the long-term, the timing of these cycles is not predictable. Hence the series is stationary.

### Differencing[](stationarity.html#differencing)

In Figure [9.1](stationarity.html#fig:stationary), note that the Google stock price was non-stationary in panel (a), but the daily changes were stationary in panel (b). This shows one way to make a non-stationary time series stationary — compute the differences between consecutive observations. This is known as **differencing**.

Transformations such as logarithms can help to stabilise the variance of a time series. Differencing can help stabilise the mean of a time series by removing changes in the level of a time series, and therefore eliminating (or reducing) trend and seasonality.

As well as the time plot of the data, the ACF plot is also useful for identifying non-stationary time series. For a stationary time series, the ACF will drop to zero relatively quickly, while the ACF of non-stationary data decreases slowly. Also, for non-stationary data, the value of \\(r_1\\) is often large and positive.
    
    
    [](stationarity.html#cb176-1)google_2015 <- gafa_stock |>
    [](stationarity.html#cb176-2)  filter(Symbol == "GOOG", year(Date) == 2015)
    
    
    [](stationarity.html#cb177-1)google_2015 |> ACF(Close) |>
    [](stationarity.html#cb177-2)  autoplot() + labs(subtitle = "Google closing stock price")
    [](stationarity.html#cb177-3)google_2015 |> ACF(difference(Close)) |>
    [](stationarity.html#cb177-4)  autoplot() + labs(subtitle = "Changes in Google closing stock price")

Figure 9.2: The ACF of the Google closing stock price in 2015 (left) and of the daily changes in Google closing stock price in 2015 (right). 
    
    
    [](stationarity.html#cb178-1)google_2015 |>
    [](stationarity.html#cb178-2)  mutate(diff_close = difference(Close)) |>
    [](stationarity.html#cb178-3)  features(diff_close, ljung_box, lag = 10)
    [](stationarity.html#cb178-4)#> # A tibble: 1 × 3
    [](stationarity.html#cb178-5)#>   Symbol lb_stat lb_pvalue
    [](stationarity.html#cb178-6)#>   <chr>    <dbl>     <dbl>
    [](stationarity.html#cb178-7)#> 1 GOOG      7.91     0.637

The ACF of the differenced Google stock price looks just like that of a white noise series. Only one autocorrelation is outside of the 95% limits, and the Ljung-Box \\(Q^*\\) statistic has a _p_ -value of 0.637 (for \\(h=10\\)). This suggests that the _daily change_ in the Google stock price is essentially a random amount which is uncorrelated with that of previous days.

### Random walk model[](stationarity.html#random-walk-model)

The differenced series is the _change_ between consecutive observations in the original series, and can be written as \\[ y'_t = y_t - y_{t-1}. \\] The differenced series will have only \\(T-1\\) values, since it is not possible to calculate a difference \\(y_1'\\) for the first observation.

When the differenced series is white noise, the model for the original series can be written as \\[ y_t - y_{t-1} = \varepsilon_t, \\] where \\(\varepsilon_t\\) denotes white noise. Rearranging this leads to the “random walk” model \\[ y_t = y_{t-1} + \varepsilon_t. \\] Random walk models are widely used for non-stationary data, particularly financial and economic data. Random walks typically have:

  * long periods of apparent trends up or down
  * sudden and unpredictable changes in direction.


The forecasts from a random walk model are equal to the last observation, as future movements are unpredictable, and are equally likely to be up or down. Thus, the random walk model underpins naïve forecasts, first introduced in Section [5.2](simple-methods.html#simple-methods).

A closely related model allows the differences to have a non-zero mean. Then \\[ y_t - y_{t-1} = c + \varepsilon_t\quad\text{or}\quad {y_t = c + y_{t-1} + \varepsilon_t}\: . \\] The value of \\(c\\) is the average of the changes between consecutive observations. If \\(c\\) is positive, then the average change is an increase in the value of \\(y_t\\). Thus, \\(y_t\\) will tend to drift upwards. However, if \\(c\\) is negative, \\(y_t\\) will tend to drift downwards.

This is the model behind the drift method, also discussed in Section [5.2](simple-methods.html#simple-methods).

### Second-order differencing[](stationarity.html#second-order-differencing)

Occasionally the differenced data will not appear to be stationary and it may be necessary to difference the data a second time to obtain a stationary series: \\[\begin{align*} y''_{t} &= y'_{t} - y'_{t - 1} \\\ &= (y_t - y_{t-1}) - (y_{t-1}-y_{t-2})\\\ &= y_t - 2y_{t-1} +y_{t-2}. \end{align*}\\] In this case, \\(y_t''\\) will have \\(T-2\\) values. Then, we would model the “change in the changes” of the original data. In practice, it is almost never necessary to go beyond second-order differences.

### Seasonal differencing[](stationarity.html#seasonal-differencing)

A seasonal difference is the difference between an observation and the previous observation from the same season. So \\[ y'_t = y_t - y_{t-m}, \\] where \\(m=\\) the number of seasons. These are also called “lag-\\(m\\) differences”, as we subtract the observation after a lag of \\(m\\) periods.

If seasonally differenced data appear to be white noise, then an appropriate model for the original data is \\[ y_t = y_{t-m}+\varepsilon_t. \\] Forecasts from this model are equal to the last observation from the relevant season. That is, this model gives seasonal naïve forecasts, introduced in Section [5.2](simple-methods.html#simple-methods).

The bottom panel in Figure [9.3](stationarity.html#fig:a10diff) shows the seasonal differences of the logarithm of the monthly scripts for A10 (antidiabetic) drugs sold in Australia. The transformation and differencing have made the series look relatively stationary.

Figure 9.3: Logs and seasonal differences of the A10 (antidiabetic) sales data. The logarithms stabilise the variance, while the seasonal differences remove the seasonality and trend. 

To distinguish seasonal differences from ordinary differences, we sometimes refer to ordinary differences as “first differences”, meaning differences at lag 1.

Sometimes it is necessary to take both a seasonal difference and a first difference to obtain stationary data. Figure [9.4](stationarity.html#fig:h02diff) plots Australian corticosteroid drug sales ($AUD) (top panel). Here, the data are first transformed using logarithms (second panel), then seasonal differences are calculated (third panel). The data still seem somewhat non-stationary, and so a further lot of first differences are computed (bottom panel).
    
    
    [](stationarity.html#cb179-1)PBS |>
    [](stationarity.html#cb179-2)  filter(ATC2 == "H02") |>
    [](stationarity.html#cb179-3)  summarise(Cost = sum(Cost)/1e6) |>
    [](stationarity.html#cb179-4)  transmute(
    [](stationarity.html#cb179-5)    `Sales ($million)` = Cost,
    [](stationarity.html#cb179-6)    `Log sales` = log(Cost),
    [](stationarity.html#cb179-7)    `Annual change in log sales` = difference(log(Cost), 12),
    [](stationarity.html#cb179-8)    `Doubly differenced log sales` =
    [](stationarity.html#cb179-9)                     difference(difference(log(Cost), 12), 1)
    [](stationarity.html#cb179-10)  ) |>
    [](stationarity.html#cb179-11)  pivot_longer(-Month, names_to="Type", values_to="Sales") |>
    [](stationarity.html#cb179-12)  mutate(
    [](stationarity.html#cb179-13)    Type = factor(Type, levels = c(
    [](stationarity.html#cb179-14)      "Sales ($million)",
    [](stationarity.html#cb179-15)      "Log sales",
    [](stationarity.html#cb179-16)      "Annual change in log sales",
    [](stationarity.html#cb179-17)      "Doubly differenced log sales"))
    [](stationarity.html#cb179-18)  ) |>
    [](stationarity.html#cb179-19)  ggplot(aes(x = Month, y = Sales)) +
    [](stationarity.html#cb179-20)  geom_line() +
    [](stationarity.html#cb179-21)  facet_grid(vars(Type), scales = "free_y") +
    [](stationarity.html#cb179-22)  labs(title = "Corticosteroid drug sales", y = NULL)

Figure 9.4: Top panel: Corticosteroid drug sales ($AUD). Other panels show the same data after transforming and differencing. 

There is a degree of subjectivity in selecting which differences to apply. The seasonally differenced data in Figure [9.3](stationarity.html#fig:a10diff) do not show substantially different behaviour from the seasonally differenced data in Figure [9.4](stationarity.html#fig:h02diff). In the latter case, we could have decided to stop with the seasonally differenced data, and not done an extra round of differencing. In the former case, we could have decided that the data were not sufficiently stationary and taken an extra round of differencing. Some formal tests for differencing are discussed below, but there are always some choices to be made in the modelling process, and different analysts may make different choices.

If \\(y'_t = y_t - y_{t-m}\\) denotes a seasonally differenced series, then the twice-differenced series is \\[\begin{align*} y''_t &= y'_t - y'_{t-1} \\\ &= (y_t - y_{t-m}) - (y_{t-1} - y_{t-m-1}) \\\ &= y_t -y_{t-1} - y_{t-m} + y_{t-m-1}\: \end{align*}\\] When both seasonal and first differences are applied, it makes no difference which is done first—the result will be the same. However, if the data have a strong seasonal pattern, we recommend that seasonal differencing be done first, because the resulting series will sometimes be stationary and there will be no need for a further first difference. If first differencing is done first, there will still be seasonality present.

Beware that applying more differences than required will induce false dynamics or autocorrelations that do not really exist in the time series. Therefore, do as few differences as necessary to obtain a stationary series.

It is important that if differencing is used, the differences are interpretable. First differences are the change between one observation and the next. Seasonal differences are the change between one year to the next. Other lags are unlikely to make much interpretable sense and should be avoided.

### Unit root tests[](stationarity.html#unit-root-tests)

One way to determine more objectively whether differencing is required is to use a _unit root test_. These are statistical hypothesis tests of stationarity that are designed for determining whether differencing is required.

A number of unit root tests are available, which are based on different assumptions and may lead to conflicting answers. In our analysis, we use the _Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test_ ([Kwiatkowski et al., 1992](stationarity.html#ref-KPSS92)). In this test, the null hypothesis is that the data are stationary, and we look for evidence that the null hypothesis is false. Consequently, small p-values (e.g., less than 0.05) suggest that differencing is required. The test can be computed using the `unitroot_kpss()` function.

For example, let us apply it to the Google stock price data.
    
    
    [](stationarity.html#cb180-1)google_2015 |>
    [](stationarity.html#cb180-2)  features(Close, unitroot_kpss)
    [](stationarity.html#cb180-3)#> # A tibble: 1 × 3
    [](stationarity.html#cb180-4)#>   Symbol kpss_stat kpss_pvalue
    [](stationarity.html#cb180-5)#>   <chr>      <dbl>       <dbl>
    [](stationarity.html#cb180-6)#> 1 GOOG        3.56        0.01

The KPSS test p-value is reported as a number between 0.01 and 0.1. If the actual p-value is less than 0.01, it is reported as 0.01; and if the actual p-value is greater than 0.1, it is reported as 0.1. In this case, the p-value is shown as 0.01 (and therefore it may be smaller than that), indicating that the null hypothesis is rejected. That is, the data are not stationary. We can difference the data, and apply the test again.
    
    
    [](stationarity.html#cb181-1)google_2015 |>
    [](stationarity.html#cb181-2)  mutate(diff_close = difference(Close)) |>
    [](stationarity.html#cb181-3)  features(diff_close, unitroot_kpss)
    [](stationarity.html#cb181-4)#> # A tibble: 1 × 3
    [](stationarity.html#cb181-5)#>   Symbol kpss_stat kpss_pvalue
    [](stationarity.html#cb181-6)#>   <chr>      <dbl>       <dbl>
    [](stationarity.html#cb181-7)#> 1 GOOG      0.0989         0.1

This time, the p-value is reported as 0.1 (and so it could be larger than that). We can conclude that the differenced data appear stationary.

This process of using a sequence of KPSS tests to determine the appropriate number of first differences is carried out using the `unitroot_ndiffs()` feature.
    
    
    [](stationarity.html#cb182-1)google_2015 |>
    [](stationarity.html#cb182-2)  features(Close, unitroot_ndiffs)
    [](stationarity.html#cb182-3)#> # A tibble: 1 × 2
    [](stationarity.html#cb182-4)#>   Symbol ndiffs
    [](stationarity.html#cb182-5)#>   <chr>   <int>
    [](stationarity.html#cb182-6)#> 1 GOOG        1

As we saw from the KPSS tests above, one difference is required to make the `google_2015` data stationary.

A similar feature for determining whether seasonal differencing is required is `unitroot_nsdiffs()`, which uses the measure of seasonal strength introduced in Section [4.3](stlfeatures.html#stlfeatures) to determine the appropriate number of seasonal differences required. No seasonal differences are suggested if \\(F_S<0.64\\), otherwise one seasonal difference is suggested.

We can apply `unitroot_nsdiffs()` to the monthly total Australian retail turnover.
    
    
    [](stationarity.html#cb183-1)aus_total_retail <- aus_retail |>
    [](stationarity.html#cb183-2)  summarise(Turnover = sum(Turnover))
    [](stationarity.html#cb183-3)aus_total_retail |>
    [](stationarity.html#cb183-4)  mutate(log_turnover = log(Turnover)) |>
    [](stationarity.html#cb183-5)  features(log_turnover, unitroot_nsdiffs)
    [](stationarity.html#cb183-6)#> # A tibble: 1 × 1
    [](stationarity.html#cb183-7)#>   nsdiffs
    [](stationarity.html#cb183-8)#>     <int>
    [](stationarity.html#cb183-9)#> 1       1
    [](stationarity.html#cb183-10)
    [](stationarity.html#cb183-11)aus_total_retail |>
    [](stationarity.html#cb183-12)  mutate(log_turnover = difference(log(Turnover), 12)) |>
    [](stationarity.html#cb183-13)  features(log_turnover, unitroot_ndiffs)
    [](stationarity.html#cb183-14)#> # A tibble: 1 × 1
    [](stationarity.html#cb183-15)#>   ndiffs
    [](stationarity.html#cb183-16)#>    <int>
    [](stationarity.html#cb183-17)#> 1      1

Because `unitroot_nsdiffs()` returns 1 (indicating one seasonal difference is required), we apply the `unitroot_ndiffs()` function to the seasonally differenced data. These functions suggest we should do both a seasonal difference and a first difference.

### Bibliography[](bibliography.html#bibliography)

Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root: How sure are we that economic time series have a unit root? _Journal of Econometrics_ , _54_(1-3), 159–178. [__](https://doi.org/10.1016/0304-4076\(92\)90104-Y)

* * *

  18. More precisely, if \\(\\{y_t\\}\\) is a **stationary** time series, then for all \\(s\\), the distribution of \\((y_t,\dots,y_{t+s})\\) does not depend on \\(t\\).[↩︎](stationarity.html#fnref18)




---

## 9.2 Backshift notation[](backshift.html#backshift)

The backward shift operator \\(B\\) is a useful notational device when working with time series lags: \\[ B y_{t} = y_{t - 1} \: . \\] (Some references use \\(L\\) for “lag” instead of \\(B\\) for “backshift”.) In other words, \\(B\\), operating on \\(y_{t}\\), has the effect of shifting the data back one period. Two applications of \\(B\\) to \\(y_{t}\\) shifts the data back two periods: \\[ B(By_{t}) = B^{2}y_{t} = y_{t-2}\: . \\] For monthly data, if we wish to consider “the same month last year,” the notation is \\(B^{12}y_{t}\\) = \\(y_{t-12}\\).

The backward shift operator is convenient for describing the process of _differencing_. A first difference can be written as \\[ y'_{t} = y_{t} - y_{t-1} = y_t - By_{t} = (1 - B)y_{t}\: . \\] So a first difference can be represented by \\((1 - B)\\). Similarly, if second-order differences have to be computed, then: \\[ y''_{t} = y_{t} - 2y_{t - 1} + y_{t - 2} = (1-2B+B^2)y_t = (1 - B)^{2} y_{t}\: . \\] In general, a \\(d\\)th-order difference can be written as \\[ (1 - B)^{d} y_{t}. \\]

Backshift notation is particularly useful when combining differences, as the operator can be treated using ordinary algebraic rules. In particular, terms involving \\(B\\) can be multiplied together.

For example, a seasonal difference followed by a first difference can be written as \\[\begin{align*} (1-B)(1-B^m)y_t &= (1 - B - B^m + B^{m+1})y_t \\\ &= y_t-y_{t-1}-y_{t-m}+y_{t-m-1}, \end{align*}\\] the same result we obtained earlier.


---

## 9.3 Autoregressive models[](AR.html#AR)

In a multiple regression model, introduced in Chapter [7](regression.html#regression), we forecast the variable of interest using a linear combination of predictors. In an autoregression model, we forecast the variable of interest using a linear combination of _past values of the variable_. The term _auto_ regression indicates that it is a regression of the variable against itself.

Thus, an autoregressive model of order \\(p\\) can be written as \\[ y_{t} = c + \phi_{1}y_{t-1} + \phi_{2}y_{t-2} + \dots + \phi_{p}y_{t-p} + \varepsilon_{t}, \\] where \\(\varepsilon_t\\) is white noise. This is like a multiple regression but with _lagged values_ of \\(y_t\\) as predictors. We refer to this as an **AR( \\(p\\)) model**, an autoregressive model of order \\(p\\).

Autoregressive models are remarkably flexible at handling a wide range of different time series patterns. The two series in Figure [9.5](AR.html#fig:arp) show series from an AR(1) model and an AR(2) model. Changing the parameters \\(\phi_1,\dots,\phi_p\\) results in different time series patterns. The variance of the error term \\(\varepsilon_t\\) will only change the scale of the series, not the patterns.

Figure 9.5: Two examples of data from autoregressive models with different parameters. Left: AR(1) with \\(y_t = 18 -0.8y_{t-1} + \varepsilon_t\\). Right: AR(2) with \\(y_t = 8 + 1.3y_{t-1}-0.7y_{t-2}+\varepsilon_t\\). In both cases, \\(\varepsilon_t\\) is normally distributed white noise with mean zero and variance one. 

For an AR(1) model:

  * when \\(\phi_1=0\\) and \\(c=0\\), \\(y_t\\) is equivalent to white noise;
  * when \\(\phi_1=1\\) and \\(c=0\\), \\(y_t\\) is equivalent to a random walk;
  * when \\(\phi_1=1\\) and \\(c\ne0\\), \\(y_t\\) is equivalent to a random walk with drift;
  * when \\(\phi_1<0\\), \\(y_t\\) tends to oscillate around the mean.


We normally restrict autoregressive models to stationary data, in which case some constraints on the values of the parameters are required.

  * For an AR(1) model: \\(-1 < \phi_1 < 1\\).
  * For an AR(2) model: \\(-1 < \phi_2 < 1\\), \\(\phi_1+\phi_2 < 1\\), \\(\phi_2-\phi_1 < 1\\).


When \\(p\ge3\\), the restrictions are much more complicated. The `fable` package takes care of these restrictions when estimating a model.


---

## 9.4 Moving average models[](MA.html#MA)

Rather than using past values of the forecast variable in a regression, a moving average model uses past forecast errors in a regression-like model, \\[ y_{t} = c + \varepsilon_t + \theta_{1}\varepsilon_{t-1} + \theta_{2}\varepsilon_{t-2} + \dots + \theta_{q}\varepsilon_{t-q}, \\] where \\(\varepsilon_t\\) is white noise. We refer to this as an **MA( \\(q\\)) model**, a moving average model of order \\(q\\). Of course, we do not _observe_ the values of \\(\varepsilon_t\\), so it is not really a regression in the usual sense.

Notice that each value of \\(y_t\\) can be thought of as a weighted moving average of the past few forecast errors (although the coefficients will not normally sum to one). However, moving average _models_ should not be confused with the moving average _smoothing_ we discussed in Chapter [3](decomposition.html#decomposition). A moving average model is used for forecasting future values, while moving average smoothing is used for estimating the trend-cycle of past values.

Figure 9.6: Two examples of data from moving average models with different parameters. Left: MA(1) with \\(y_t = 20 + \varepsilon_t + 0.8\varepsilon_{t-1}\\). Right: MA(2) with \\(y_t = \varepsilon_t- \varepsilon_{t-1}+0.8\varepsilon_{t-2}\\). In both cases, \\(\varepsilon_t\\) is normally distributed white noise with mean zero and variance one. 

Figure [9.6](MA.html#fig:maq) shows some data from an MA(1) model and an MA(2) model. Changing the parameters \\(\theta_1,\dots,\theta_q\\) results in different time series patterns. As with autoregressive models, the variance of the error term \\(\varepsilon_t\\) will only change the scale of the series, not the patterns.

It is possible to write any stationary AR(\\(p\\)) model as an MA(\\(\infty\\)) model. For example, using repeated substitution, we can demonstrate this for an AR(1) model: \\[\begin{align*} y_t &= \phi_1y_{t-1} + \varepsilon_t\\\ &= \phi_1(\phi_1y_{t-2} + \varepsilon_{t-1}) + \varepsilon_t\\\ &= \phi_1^2y_{t-2} + \phi_1 \varepsilon_{t-1} + \varepsilon_t\\\ &= \phi_1^3y_{t-3} + \phi_1^2\varepsilon_{t-2} + \phi_1 \varepsilon_{t-1} + \varepsilon_t\\\ &\text{etc.} \end{align*}\\] Provided \\(-1 < \phi_1 < 1\\), the value of \\(\phi_1^k\\) will get smaller as \\(k\\) gets larger. So eventually we obtain \\[ y_t = \varepsilon_t + \phi_1 \varepsilon_{t-1} + \phi_1^2 \varepsilon_{t-2} + \phi_1^3 \varepsilon_{t-3} + \cdots, \\] an MA(\\(\infty\\)) process.

The reverse result holds if we impose some constraints on the MA parameters. Then the MA model is called **invertible**. That is, we can write any invertible MA(\\(q\\)) process as an AR(\\(\infty\\)) process. Invertible models are not simply introduced to enable us to convert from MA models to AR models. They also have some desirable mathematical properties.

For example, consider the MA(1) process, \\(y_{t} = \varepsilon_t + \theta_{1}\varepsilon_{t-1}\\). In its AR(\\(\infty\\)) representation, the most recent error can be written as a linear function of current and past observations: \\[\varepsilon_t = \sum_{j=0}^\infty (-\theta_1)^j y_{t-j}.\\] When \\(|\theta_1| > 1\\), the weights increase as lags increase, so the more distant the observations the greater their influence on the current error. When \\(|\theta_1|=1\\), the weights are constant in size, and the distant observations have the same influence as the recent observations. As neither of these situations make much sense, we require \\(|\theta_1|<1\\), so the most recent observations have higher weight than observations from the more distant past. Thus, the process is invertible when \\(|\theta_1|<1\\).

The invertibility constraints for other models are similar to the stationarity constraints.

  * For an MA(1) model: \\(-1<\theta_1<1\\).
  * For an MA(2) model: \\(-1<\theta_2<1,~\\) \\(\theta_2+\theta_1 >-1,~\\) \\(\theta_1 -\theta_2 < 1\\).


More complicated conditions hold for \\(q\ge3\\). Again, the `fable` package will take care of these constraints when estimating the models.


---

## 9.5 Non-seasonal ARIMA models[](non-seasonal-arima.html#non-seasonal-arima)

If we combine differencing with autoregression and a moving average model, we obtain a non-seasonal ARIMA model. ARIMA is an acronym for AutoRegressive Integrated Moving Average (in this context, “integration” is the reverse of differencing). The full model can be written as \\[\begin{equation} y'_{t} = c + \phi_{1}y'_{t-1} + \cdots + \phi_{p}y'_{t-p} \+ \theta_{1}\varepsilon_{t-1} + \cdots + \theta_{q}\varepsilon_{t-q} + \varepsilon_{t}, \tag{9.1} \end{equation}\\] where \\(y'_{t}\\) is the differenced series (it may have been differenced more than once). The “predictors” on the right hand side include both lagged values of \\(y_t\\) and lagged errors. We call this an **ARIMA( \\(p, d, q\\)) model**, where

\\(p=\\) | order of the autoregressive part;  
---|---  
\\(d=\\) | degree of first differencing involved;  
\\(q=\\) | order of the moving average part.  
  
The same stationarity and invertibility conditions that are used for autoregressive and moving average models also apply to an ARIMA model.

Many of the models we have already discussed are special cases of the ARIMA model, as shown in Table [9.1](non-seasonal-arima.html#tab:arimaspecialcases).

Table 9.1: Special cases of ARIMA models. White noise | ARIMA(0,0,0) with no constant  
---|---  
Random walk | ARIMA(0,1,0) with no constant  
Random walk with drift | ARIMA(0,1,0) with a constant  
Autoregression | ARIMA(\\(p\\),0,0)  
Moving average | ARIMA(0,0,\\(q\\))  
  
Once we start combining components in this way to form more complicated models, it is much easier to work with the backshift notation. For example, Equation [(9.1)](non-seasonal-arima.html#eq:8-arima) can be written in backshift notation as \\[\begin{equation} \tag{9.2} \begin{array}{c c c c} (1-\phi_1B - \cdots - \phi_p B^p) & (1-B)^d y_{t} &= &c + (1 + \theta_1 B + \cdots + \theta_q B^q)\varepsilon_t\\\ {\uparrow} & {\uparrow} & &{\uparrow}\\\ \text{AR($p$)} & \text{$d$ differences} & & \text{MA($q$)}\\\ \end{array} \end{equation}\\]

Selecting appropriate values for \\(p\\), \\(d\\) and \\(q\\) can be difficult. However, the `ARIMA()` function from the `fable` package will do it for you automatically. In Section [9.7](arima-r.html#arima-r), we will learn how this function works, along with some methods for choosing these values yourself.

### Example: Egyptian exports[](non-seasonal-arima.html#example-egyptian-exports)

Figure [9.7](non-seasonal-arima.html#fig:egyptexports) shows Egyptian exports as a percentage of GDP from 1960 to 2017.
    
    
    [](non-seasonal-arima.html#cb184-1)global_economy |>
    [](non-seasonal-arima.html#cb184-2)  filter(Code == "EGY") |>
    [](non-seasonal-arima.html#cb184-3)  autoplot(Exports) +
    [](non-seasonal-arima.html#cb184-4)  labs(y = "% of GDP", title = "Egyptian exports")

Figure 9.7: Annual Egyptian exports as a percentage of GDP since 1960. 

The following R code selects a non-seasonal ARIMA model automatically.
    
    
    [](non-seasonal-arima.html#cb185-1)fit <- global_economy |>
    [](non-seasonal-arima.html#cb185-2)  filter(Code == "EGY") |>
    [](non-seasonal-arima.html#cb185-3)  model(ARIMA(Exports))
    [](non-seasonal-arima.html#cb185-4)report(fit)
    [](non-seasonal-arima.html#cb185-5)#> Series: Exports 
    [](non-seasonal-arima.html#cb185-6)#> Model: ARIMA(2,0,1) w/ mean 
    [](non-seasonal-arima.html#cb185-7)#> 
    [](non-seasonal-arima.html#cb185-8)#> Coefficients:
    [](non-seasonal-arima.html#cb185-9)#>          ar1      ar2      ma1  constant
    [](non-seasonal-arima.html#cb185-10)#>       1.6764  -0.8034  -0.6896    2.5623
    [](non-seasonal-arima.html#cb185-11)#> s.e.  0.1111   0.0928   0.1492    0.1161
    [](non-seasonal-arima.html#cb185-12)#> 
    [](non-seasonal-arima.html#cb185-13)#> sigma^2 estimated as 8.046:  log likelihood=-141.6
    [](non-seasonal-arima.html#cb185-14)#> AIC=293.1   AICc=294.3   BIC=303.4

This is an ARIMA(2,0,1) model: \\[ y_t = 2.56 \+ 1.68 y_{t-1} -0.80 y_{t-2} -0.69 \varepsilon_{t-1} \+ \varepsilon_{t}, \\] where \\(\varepsilon_t\\) is white noise with a standard deviation of \\(2.837 = \sqrt{8.046}\\). Forecasts from the model are shown in Figure [9.8](non-seasonal-arima.html#fig:egyptexportsf). Notice how they have picked up the cycles evident in the Egyptian economy over the last few decades.
    
    
    [](non-seasonal-arima.html#cb186-1)fit |> forecast(h=10) |>
    [](non-seasonal-arima.html#cb186-2)  autoplot(global_economy) +
    [](non-seasonal-arima.html#cb186-3)  labs(y = "% of GDP", title = "Egyptian exports")

Figure 9.8: Forecasts of Egyptian exports. 

### Understanding ARIMA models[](non-seasonal-arima.html#understanding-arima-models)

The `ARIMA()` function is useful, but anything automated can be a little dangerous, and it is worth understanding something of the behaviour of the models even when you rely on an automatic procedure to choose the model for you.

The constant \\(c\\) has an important effect on the long-term forecasts obtained from these models.

  * If \\(c=0\\) and \\(d=0\\), the long-term forecasts will go to zero.
  * If \\(c=0\\) and \\(d=1\\), the long-term forecasts will go to a non-zero constant.
  * If \\(c=0\\) and \\(d=2\\), the long-term forecasts will follow a straight line.
  * If \\(c\ne0\\) and \\(d=0\\), the long-term forecasts will go to the mean of the data.
  * If \\(c\ne0\\) and \\(d=1\\), the long-term forecasts will follow a straight line.
  * If \\(c\ne0\\) and \\(d=2\\), the long-term forecasts will follow a quadratic trend. (This is not recommended, and `fable` will not permit it.)


The value of \\(d\\) also has an effect on the prediction intervals — the higher the value of \\(d\\), the more rapidly the prediction intervals increase in size. For \\(d=0\\), the long-term forecast standard deviation will go to the standard deviation of the historical data, so the prediction intervals will all be essentially the same.

This behaviour is seen in Figure [9.8](non-seasonal-arima.html#fig:egyptexportsf) where \\(d=0\\) and \\(c\ne0\\). In this figure, the prediction intervals are almost the same width for the last few forecast horizons, and the final point forecasts are close to the mean of the data.

The value of \\(p\\) is important if the data show cycles. To obtain cyclic forecasts, it is necessary to have \\(p\ge2\\), along with some additional conditions on the parameters. For an AR(2) model, cyclic behaviour occurs if \\(\phi_1^2+4\phi_2<0\\) (as is the case for the Egyptian exports model). In that case, the average period of the cycles is[19](non-seasonal-arima.html#fn19) \\[ \frac{2\pi}{\text{arc cos}(-\phi_1(1-\phi_2)/(4\phi_2))}. \\]

### ACF and PACF plots[](non-seasonal-arima.html#acf-and-pacf-plots)

It is usually not possible to tell, simply from a time plot, what values of \\(p\\) and \\(q\\) are appropriate for the data. However, it is sometimes possible to use the ACF plot, and the closely related PACF plot, to determine appropriate values for \\(p\\) and \\(q\\).

Recall that an ACF plot shows the autocorrelations which measure the relationship between \\(y_t\\) and \\(y_{t-k}\\) for different values of \\(k\\). Now if \\(y_t\\) and \\(y_{t-1}\\) are correlated, then \\(y_{t-1}\\) and \\(y_{t-2}\\) must also be correlated. However, then \\(y_t\\) and \\(y_{t-2}\\) might be correlated, simply because they are both connected to \\(y_{t-1}\\), rather than because of any new information contained in \\(y_{t-2}\\) that could be used in forecasting \\(y_t\\).

To overcome this problem, we can use **partial autocorrelations**. These measure the relationship between \\(y_{t}\\) and \\(y_{t-k}\\) after removing the effects of lags \\(1, 2, 3, \dots, k - 1\\). So the first partial autocorrelation is identical to the first autocorrelation, because there is nothing between them to remove. Each partial autocorrelation can be estimated as the last coefficient in an autoregressive model. Specifically, \\(\alpha_k\\), the \\(k\\)th partial autocorrelation coefficient, is equal to the estimate of \\(\phi_k\\) in an AR(\\(k\\)) model. In practice, there are more efficient algorithms for computing \\(\alpha_k\\) than fitting all of these autoregressions, but they give the same results.

Figures [9.9](non-seasonal-arima.html#fig:egyptacf) and [9.10](non-seasonal-arima.html#fig:egyptpacf) shows the ACF and PACF plots for the Egyptian exports data shown in Figure [9.7](non-seasonal-arima.html#fig:egyptexports). The partial autocorrelations have the same critical values of \\(\pm 1.96/\sqrt{T}\\) as for ordinary autocorrelations, and these are typically shown on the plot as in Figure [9.10](non-seasonal-arima.html#fig:egyptpacf).
    
    
    [](non-seasonal-arima.html#cb187-1)global_economy |>
    [](non-seasonal-arima.html#cb187-2)  filter(Code == "EGY") |>
    [](non-seasonal-arima.html#cb187-3)  ACF(Exports) |>
    [](non-seasonal-arima.html#cb187-4)  autoplot()

Figure 9.9: ACF of Egyptian exports. 
    
    
    [](non-seasonal-arima.html#cb188-1)global_economy |>
    [](non-seasonal-arima.html#cb188-2)  filter(Code == "EGY") |>
    [](non-seasonal-arima.html#cb188-3)  PACF(Exports) |>
    [](non-seasonal-arima.html#cb188-4)  autoplot()

Figure 9.10: PACF of Egyptian exports. 

A convenient way to produce a time plot, ACF plot and PACF plot in one command is to use the `gg_tsdisplay()` function with `plot_type = "partial"`.

If the data are from an ARIMA(\\(p\\),\\(d\\),0) or ARIMA(0,\\(d\\),\\(q\\)) model, then the ACF and PACF plots can be helpful in determining the value of \\(p\\) or \\(q\\). If \\(p\\) and \\(q\\) are both positive, then the plots do not help in finding suitable values of \\(p\\) and \\(q\\).

The data may follow an ARIMA(\\(p\\),\\(d\\),0) model if the ACF and PACF plots of the differenced data show the following patterns:

  * the ACF is exponentially decaying or sinusoidal;
  * there is a significant spike at lag \\(p\\) in the PACF, but none beyond lag \\(p\\).


The data may follow an ARIMA(0,\\(d\\),\\(q\\)) model if the ACF and PACF plots of the differenced data show the following patterns:

  * the PACF is exponentially decaying or sinusoidal;
  * there is a significant spike at lag \\(q\\) in the ACF, but none beyond lag \\(q\\).


In Figure [9.9](non-seasonal-arima.html#fig:egyptacf), we see that there is a decaying sinusoidal pattern in the ACF, and in Figure [9.10](non-seasonal-arima.html#fig:egyptpacf) the PACF shows the last significant spike at lag 4. This is what you would expect from an ARIMA(4,0,0) model.
    
    
    [](non-seasonal-arima.html#cb189-1)fit2 <- global_economy |>
    [](non-seasonal-arima.html#cb189-2)  filter(Code == "EGY") |>
    [](non-seasonal-arima.html#cb189-3)  model(ARIMA(Exports ~ pdq(4,0,0)))
    [](non-seasonal-arima.html#cb189-4)report(fit2)
    [](non-seasonal-arima.html#cb189-5)#> Series: Exports 
    [](non-seasonal-arima.html#cb189-6)#> Model: ARIMA(4,0,0) w/ mean 
    [](non-seasonal-arima.html#cb189-7)#> 
    [](non-seasonal-arima.html#cb189-8)#> Coefficients:
    [](non-seasonal-arima.html#cb189-9)#>          ar1      ar2     ar3      ar4  constant
    [](non-seasonal-arima.html#cb189-10)#>       0.9861  -0.1715  0.1807  -0.3283    6.6922
    [](non-seasonal-arima.html#cb189-11)#> s.e.  0.1247   0.1865  0.1865   0.1273    0.3562
    [](non-seasonal-arima.html#cb189-12)#> 
    [](non-seasonal-arima.html#cb189-13)#> sigma^2 estimated as 7.885:  log likelihood=-140.5
    [](non-seasonal-arima.html#cb189-14)#> AIC=293.1   AICc=294.7   BIC=305.4

This model is only slightly worse than the ARIMA(2,0,1) model identified by `ARIMA()` (with an AICc value of 294.70 compared to 294.29).

We can also specify particular values of `pdq()` that `ARIMA()` can search for. For example, to find the best ARIMA model with \\(p\in\\{1,2,3\\}\\), \\(q\in\\{0,1,2\\}\\) and \\(d=1\\), you could use `ARIMA(y ~ pdq(p=1:3, d=1, q=0:2))`.

* * *

  19. arc cos is the inverse cosine function. You should be able to find it on your calculator. It may be labelled acos or cos\\(^{-1}\\).[↩︎](non-seasonal-arima.html#fnref19)




---

## 9.6 Estimation and order selection[](arima-estimation.html#arima-estimation)

### Maximum likelihood estimation[](arima-estimation.html#maximum-likelihood-estimation)

Once the model order has been identified (i.e., the values of \\(p\\), \\(d\\) and \\(q\\)), we need to estimate the parameters \\(c\\), \\(\phi_1,\dots,\phi_p\\), \\(\theta_1,\dots,\theta_q\\). When `fable` estimates the ARIMA model, it uses _maximum likelihood estimation_ (MLE). This technique finds the values of the parameters which maximise the probability of obtaining the data that we have observed. For ARIMA models, MLE is similar to the _least squares_ estimates that would be obtained by minimising \\[ \sum_{t=1}^T\varepsilon_t^2. \\] (For the regression models considered in Chapter [7](regression.html#regression), MLE gives exactly the same parameter estimates as least squares estimation.) Note that ARIMA models are much more complicated to estimate than regression models, and different software will give slightly different answers as they use different methods of estimation, and different optimisation algorithms.

In practice, the `fable` package will report the value of the _log likelihood_ of the data; that is, the logarithm of the probability of the observed data coming from the estimated model. For given values of \\(p\\), \\(d\\) and \\(q\\), `ARIMA()` will try to maximise the log likelihood when finding parameter estimates.

### Information Criteria[](arima-estimation.html#information-criteria)

Akaike’s Information Criterion (AIC), which was useful in selecting predictors for regression (see Section [7.5](selecting-predictors.html#selecting-predictors)), is also useful for determining the order of an ARIMA model. It can be written as \\[ \text{AIC} = -2 \log(L) + 2(p+q+k+1), \\] where \\(L\\) is the likelihood of the data, \\(k=1\\) if \\(c\ne0\\) and \\(k=0\\) if \\(c=0\\). Note that the last term in parentheses is the number of parameters in the model (including \\(\sigma^2\\), the variance of the residuals).

For ARIMA models, the corrected AIC can be written as \\[ \text{AICc} = \text{AIC} + \frac{2(p+q+k+1)(p+q+k+2)}{T-p-q-k-2}, \\] and the Bayesian Information Criterion can be written as \\[ \text{BIC} = \text{AIC} + [\log(T)-2](p+q+k+1). \\] Good models are obtained by minimising the AIC, AICc or BIC. Our preference is to use the AICc.

It is important to note that these information criteria tend not to be good guides to selecting the appropriate order of differencing (\\(d\\)) of a model, but only for selecting the values of \\(p\\) and \\(q\\). This is because the differencing changes the data on which the likelihood is computed, making the AIC values between models with different orders of differencing not comparable. So we need to use some other approach to choose \\(d\\), and then we can use the AICc to select \\(p\\) and \\(q\\).


---

## 9.7 ARIMA modelling in `fable`[](arima-r.html#arima-r)

### How does `ARIMA()` work?[](arima-r.html#how-does-arima-work)

The `ARIMA()` function in the `fable` package uses a variation of the Hyndman-Khandakar algorithm ([Hyndman & Khandakar, 2008](arima-r.html#ref-HK08)), which combines unit root tests, minimisation of the AICc and MLE to obtain an ARIMA model. The arguments to `ARIMA()` provide for many variations on the algorithm. What is described here is the default behaviour.

**Hyndman-Khandakar algorithm for automatic ARIMA modelling**  
  
  1. The number of differences \\(0 \le d\le 2\\) is determined using repeated KPSS tests. 

  
  
  2. The values of \\(p\\) and \\(q\\) are then chosen by minimising the AICc after differencing the data \\(d\\) times. Rather than considering every possible combination of \\(p\\) and \\(q\\), the algorithm uses a stepwise search to traverse the model space. 

  
  
  1. Four initial models are fitted: 
     * ARIMA\\((0,d,0)\\), 
     * ARIMA\\((2,d,2)\\), 
     * ARIMA\\((1,d,0)\\), 
     * ARIMA\\((0,d,1)\\). 
A constant is included unless \\(d=2\\). If \\(d \le 1\\), an additional model is also fitted: 
     * ARIMA\\((0,d,0)\\) without a constant. 

  
  
  2. The best model (with the smallest AICc value) fitted in step (a) is set to be the “current model”. 

  
  
  3. Variations on the current model are considered: 
     * vary \\(p\\) and/or \\(q\\) from the current model by \\(\pm1\\); 
     * include/exclude \\(c\\) from the current model. 
The best model considered so far (either the current model or one of these variations) becomes the new current model. 

  
  
  4. Repeat Step 2(c) until no lower AICc can be found. 

  
  
Figure 9.11: An illustrative example of the Hyndman-Khandakar stepwise search process 

Figure [9.11](arima-r.html#fig:ARMAgridsearch) illustrates diagrammatically how the Hyndman-Khandakar algorithm traverses the space of the ARMA orders, through an example. The grid covers combinations of ARMA(\\(p,q\\)) orders starting from the top-left corner with an ARMA(\\(0,0\\)), with the AR order increasing down the vertical axis, and the MA order increasing across the horizontal axis.

The orange cells show the initial set of models considered by the algorithm. In this example, the ARMA(2,2) model has the lowest AICc value amongst these models. This is called the “current model” and is shown by the black circle. The algorithm then searches over neighbouring models as shown by the blue arrows. If a better model is found then this becomes the new “current model”. In this example, the new “current model” is the ARMA(3,3) model. The algorithm continues in this fashion until no better model can be found. In this example the model returned is an ARMA(4,2) model.

The default procedure will switch to a new “current model” as soon as a better model is identified, without going through all the neighbouring models. The full neighbourhood search is done when `greedy=FALSE`.

The default procedure also uses some approximations to speed up the search. These approximations can be avoided with the argument `approximation=FALSE`. It is possible that the minimum AICc model will not be found due to these approximations, or because of the use of the stepwise procedure. A much larger set of models will be searched if the argument `stepwise=FALSE` is used. See the help file for a full description of the arguments.

### Modelling procedure[](arima-r.html#modelling-procedure)

When fitting an ARIMA model to a set of (non-seasonal) time series data, the following procedure provides a useful general approach.

  1. Plot the data and identify any unusual observations.
  2. If necessary, transform the data (using a Box-Cox transformation) to stabilise the variance.
  3. If the data are non-stationary, take first differences of the data until the data are stationary.
  4. Examine the ACF/PACF: Is an ARIMA(\\(p,d,0\\)) or ARIMA(\\(0,d,q\\)) model appropriate?
  5. Try your chosen model(s), and use the AICc to search for a better model.
  6. Check the residuals from your chosen model by plotting the ACF of the residuals, and doing a portmanteau test of the residuals. If they do not look like white noise, try a modified model.
  7. Once the residuals look like white noise, calculate forecasts.


The Hyndman-Khandakar algorithm only takes care of steps 3–5. So even if you use it, you will still need to take care of the other steps yourself.

The process is summarised in Figure [9.12](arima-r.html#fig:arimaflowchart).

Figure 9.12: General process for forecasting using an ARIMA model. 

### Portmanteau tests of residuals for ARIMA models[](arima-r.html#portmanteau-tests-of-residuals-for-arima-models)

With ARIMA models, more accurate portmanteau tests are obtained if the degrees of freedom of the test statistic are adjusted to take account of the number of parameters in the model. Specifically, we use \\(\ell - K\\) degrees of freedom in the test, where \\(\ell\\) is the number of lags used in the test, and \\(K\\) is the number of AR and MA parameters in the model. So for the non-seasonal models that we have considered so far, \\(K=p+q\\). The value of \\(K\\) is passed to the `ljung_box` function via the argument `dof`, as shown in the example below.

### Example: Central African Republic exports[](arima-r.html#example-central-african-republic-exports)

We will apply this procedure to the exports of the Central African Republic shown in Figure [9.13](arima-r.html#fig:caf).
    
    
    [](arima-r.html#cb190-1)global_economy |>
    [](arima-r.html#cb190-2)  filter(Code == "CAF") |>
    [](arima-r.html#cb190-3)  autoplot(Exports) +
    [](arima-r.html#cb190-4)  labs(title="Central African Republic exports",
    [](arima-r.html#cb190-5)       y="% of GDP")

Figure 9.13: Exports of the Central African Republic as a percentage of GDP. 

  1. The time plot shows some non-stationarity, with an overall decline. The improvement in 1994 was due to a new government which overthrew the military junta and had some initial success, before unrest caused further economic decline.

  2. There is no evidence of changing variance, so we will not do a Box-Cox transformation.

  3. To address the non-stationarity, we will take a first difference of the data. The differenced data are shown in Figure [9.14](arima-r.html#fig:caf2).
         
         [](arima-r.html#cb191-1)global_economy |>
         [](arima-r.html#cb191-2)  filter(Code == "CAF") |>
         [](arima-r.html#cb191-3)  gg_tsdisplay(difference(Exports), plot_type='partial')

Figure 9.14: Time plot and ACF and PACF plots for the differenced Central African Republic Exports. 

These now appear to be stationary.

  4. The PACF shown in Figure [9.14](arima-r.html#fig:caf2) is suggestive of an AR(2) model; so an initial candidate model is an ARIMA(2,1,0). The ACF suggests an MA(3) model; so an alternative candidate is an ARIMA(0,1,3).

  5. We fit both an ARIMA(2,1,0) and an ARIMA(0,1,3) model along with two automated model selections, one using the default stepwise procedure, and one working harder to search a larger model space.
         
         [](arima-r.html#cb192-1)caf_fit <- global_economy |>
         [](arima-r.html#cb192-2)  filter(Code == "CAF") |>
         [](arima-r.html#cb192-3)  model(arima210 = ARIMA(Exports ~ pdq(2,1,0)),
         [](arima-r.html#cb192-4)        arima013 = ARIMA(Exports ~ pdq(0,1,3)),
         [](arima-r.html#cb192-5)        stepwise = ARIMA(Exports),
         [](arima-r.html#cb192-6)        search = ARIMA(Exports, stepwise=FALSE))
         [](arima-r.html#cb192-7)
         [](arima-r.html#cb192-8)caf_fit |> pivot_longer(!Country, names_to = "Model name",
         [](arima-r.html#cb192-9)                         values_to = "Orders")
         [](arima-r.html#cb192-10)#> # A mable: 4 x 3
         [](arima-r.html#cb192-11)#> # Key:     Country, Model name [4]
         [](arima-r.html#cb192-12)#>   Country                  `Model name`         Orders
         [](arima-r.html#cb192-13)#>   <fct>                    <chr>               <model>
         [](arima-r.html#cb192-14)#> 1 Central African Republic arima210     <ARIMA(2,1,0)>
         [](arima-r.html#cb192-15)#> 2 Central African Republic arima013     <ARIMA(0,1,3)>
         [](arima-r.html#cb192-16)#> 3 Central African Republic stepwise     <ARIMA(2,1,2)>
         [](arima-r.html#cb192-17)#> 4 Central African Republic search       <ARIMA(3,1,0)>
         [](arima-r.html#cb192-18)glance(caf_fit) |> arrange(AICc) |> select(.model:BIC)
         [](arima-r.html#cb192-19)#> # A tibble: 4 × 6
         [](arima-r.html#cb192-20)#>   .model   sigma2 log_lik   AIC  AICc   BIC
         [](arima-r.html#cb192-21)#>   <chr>     <dbl>   <dbl> <dbl> <dbl> <dbl>
         [](arima-r.html#cb192-22)#> 1 search     6.52   -133.  274.  275.  282.
         [](arima-r.html#cb192-23)#> 2 arima210   6.71   -134.  275.  275.  281.
         [](arima-r.html#cb192-24)#> 3 arima013   6.54   -133.  274.  275.  282.
         [](arima-r.html#cb192-25)#> 4 stepwise   6.42   -132.  274.  275.  284.

The four models have almost identical AICc values. Of the models fitted, the full search has found that an ARIMA(3,1,0) gives the lowest AICc value, closely followed by the ARIMA(2,1,0) and ARIMA(0,1,3) — the latter two being the models that we guessed from the ACF and PACF plots. The automated stepwise selection has identified an ARIMA(2,1,2) model, which has the highest AICc value of the four models.

  6. The ACF plot of the residuals from the ARIMA(3,1,0) model shows that all autocorrelations are within the threshold limits, indicating that the residuals are behaving like white noise.
         
         [](arima-r.html#cb193-1)caf_fit |>
         [](arima-r.html#cb193-2)  select(search) |>
         [](arima-r.html#cb193-3)  gg_tsresiduals()

Figure 9.15: Residual plots for the ARIMA(3,1,0) model. 

A portmanteau test (setting \\(K = 3\\)) returns a large p-value, also suggesting that the residuals are white noise.
         
         [](arima-r.html#cb194-1)augment(caf_fit) |>
         [](arima-r.html#cb194-2)  filter(.model=='search') |>
         [](arima-r.html#cb194-3)  features(.innov, ljung_box, lag = 10, dof = 3)
         [](arima-r.html#cb194-4)#> # A tibble: 1 × 4
         [](arima-r.html#cb194-5)#>   Country                  .model lb_stat lb_pvalue
         [](arima-r.html#cb194-6)#>   <fct>                    <chr>    <dbl>     <dbl>
         [](arima-r.html#cb194-7)#> 1 Central African Republic search    5.75     0.569

  7. Forecasts from the chosen model are shown in Figure [9.16](arima-r.html#fig:caffc).
         
         [](arima-r.html#cb195-1)caf_fit |>
         [](arima-r.html#cb195-2)  forecast(h=5) |>
         [](arima-r.html#cb195-3)  filter(.model=='search') |>
         [](arima-r.html#cb195-4)  autoplot(global_economy)

Figure 9.16: Forecasts for the Central African Republic Exports. 

Note that the mean forecasts look very similar to what we would get with a random walk (equivalent to an ARIMA(0,1,0)). The extra work to include AR and MA terms has made little difference to the point forecasts in this example, although the prediction intervals are much narrower than for a random walk model.


### Understanding constants in R[](arima-r.html#understanding-constants-in-r)

A non-seasonal ARIMA model can be written as \\[\begin{equation} \tag{9.3} (1-\phi_1B - \cdots - \phi_p B^p)(1-B)^d y_t = c + (1 + \theta_1 B + \cdots + \theta_q B^q)\varepsilon_t, \end{equation}\\] or equivalently as \\[\begin{equation} \tag{9.4} (1-\phi_1B - \cdots - \phi_p B^p)(1-B)^d (y_t - \mu t^d/d!) = (1 + \theta_1 B + \cdots + \theta_q B^q)\varepsilon_t, \end{equation}\\] where \\(c = \mu(1-\phi_1 - \cdots - \phi_p )\\) and \\(\mu\\) is the mean of \\((1-B)^d y_t\\). The `fable` package uses the parameterisation of Equation [(9.3)](arima-r.html#eq:c) while most other R implementations use Equation [(9.4)](arima-r.html#eq:mu).

Thus, the inclusion of a constant in a non-stationary ARIMA model is equivalent to inducing a polynomial trend of order \\(d\\) in the forecasts. (If the constant is omitted, the forecasts include a polynomial trend of order \\(d-1\\).) When \\(d=0\\), we have the special case that \\(\mu\\) is the mean of \\(y_t\\).

By default, the `ARIMA()` function will automatically determine if a constant should be included. For \\(d=0\\) or \\(d=1\\), a constant will be included if it improves the AICc value. If \\(d>1\\) the constant is always omitted as a quadratic or higher order trend is particularly dangerous when forecasting.

The constant can be specified by including `0` or `1` in the model formula (like the intercept in `lm()`). For example, to automatically select an ARIMA model with a constant, you could use `ARIMA(y ~ 1 + ...)`. Similarly, a constant can be excluded with `ARIMA(y ~ 0 + ...)`.

### Plotting the characteristic roots[](arima-r.html#plotting-the-characteristic-roots)

_(This is a more advanced section and can be skipped if desired.)_

We can re-write Equation [(9.3)](arima-r.html#eq:c) as \\[\phi(B) (1-B)^d y_t = c + \theta(B) \varepsilon_t\\] where \\(\phi(B)= (1-\phi_1B - \cdots - \phi_p B^p)\\) is a \\(p\\)th order polynomial in \\(B\\) and \\(\theta(B) = (1 + \theta_1 B + \cdots + \theta_q B^q)\\) is a \\(q\\)th order polynomial in \\(B\\).

The stationarity conditions for the model are that the \\(p\\) complex roots of \\(\phi(B)\\) lie outside the unit circle, and the invertibility conditions are that the \\(q\\) complex roots of \\(\theta(B)\\) lie outside the unit circle. So we can see whether the model is close to invertibility or stationarity by a plot of the roots in relation to the complex unit circle.

It is easier to plot the inverse roots instead, as they should all lie _within_ the unit circle. This is easily done in R. For the ARIMA(3,1,0) model fitted to the Central African Republic Exports, we obtain Figure [9.17](arima-r.html#fig:armaroots).
    
    
    [](arima-r.html#cb196-1)gg_arma(caf_fit |> select(Country, search))

Figure 9.17: Inverse characteristic roots for the ARIMA(3,1,0) model fitted to the Central African Republic Exports. 

The three orange dots in the plot correspond to the roots of the polynomials \\(\phi(B)\\). They are all inside the unit circle, as we would expect because `fable` ensures the fitted model is both stationary and invertible. Any roots close to the unit circle may be numerically unstable, and the corresponding model will not be good for forecasting.

The `ARIMA()` function will never return a model with inverse roots outside the unit circle. Models automatically selected by the `ARIMA()` function will not contain roots close to the unit circle either. Consequently, it is sometimes possible to find a model with better AICc value than `ARIMA()` will return, but such models will be potentially problematic.

### Bibliography[](bibliography.html#bibliography)

Hyndman, R. J., & Khandakar, Y. (2008). Automatic time series forecasting: The forecast package for R. _Journal of Statistical Software_ , _27_(1), 1–22. [__](https://doi.org/10.18637/jss.v027.i03)


---

## 9.8 Forecasting[](arima-forecasting.html#arima-forecasting)

### Point forecasts[](arima-forecasting.html#point-forecasts)

Although we have calculated forecasts from the ARIMA models in our examples, we have not yet explained how they are obtained. Point forecasts can be calculated using the following three steps.

  1. Expand the ARIMA equation so that \\(y_t\\) is on the left hand side and all other terms are on the right.
  2. Rewrite the equation by replacing \\(t\\) with \\(T+h\\).
  3. On the right hand side of the equation, replace future observations with their forecasts, future errors with zero, and past errors with the corresponding residuals.


Beginning with \\(h=1\\), these steps are then repeated for \\(h=2,3,\dots\\) until all forecasts have been calculated.

The procedure is most easily understood via an example. We will illustrate it using a ARIMA(3,1,1) model which can be written as follows: \\[ (1-\hat{\phi}_1B -\hat{\phi}_2B^2-\hat{\phi}_3B^3)(1-B) y_t = (1+\hat{\theta}_1B)\varepsilon_{t}. \\] Then we expand the left hand side to obtain \\[ \left[1-(1+\hat{\phi}_1)B +(\hat{\phi}_1-\hat{\phi}_2)B^2 + (\hat{\phi}_2-\hat{\phi}_3)B^3 +\hat{\phi}_3B^4\right] y_t = (1+\hat{\theta}_1B)\varepsilon_{t}, \\] and applying the backshift operator gives \\[ y_t - (1+\hat{\phi}_1)y_{t-1} +(\hat{\phi}_1-\hat{\phi}_2)y_{t-2} + (\hat{\phi}_2-\hat{\phi}_3)y_{t-3} +\hat{\phi}_3y_{t-4} = \varepsilon_t+\hat{\theta}_1\varepsilon_{t-1}. \\] Finally, we move all terms other than \\(y_t\\) to the right hand side: \\[\begin{equation} \tag{9.5} y_t = (1+\hat{\phi}_1)y_{t-1} -(\hat{\phi}_1-\hat{\phi}_2)y_{t-2} - (\hat{\phi}_2-\hat{\phi}_3)y_{t-3} -\hat{\phi}_3y_{t-4} + \varepsilon_t+\hat{\theta}_1\varepsilon_{t-1}. \end{equation}\\] This completes the first step. While the equation now looks like an ARIMA(4,0,1), it is still the same ARIMA(3,1,1) model we started with. It cannot be considered an ARIMA(4,0,1) because the coefficients do not satisfy the stationarity conditions.

For the second step, we replace \\(t\\) with \\(T+1\\) in [(9.5)](arima-forecasting.html#eq:arima301f): \\[ y_{T+1} = (1+\hat{\phi}_1)y_{T} -(\hat{\phi}_1-\hat{\phi}_2)y_{T-1} - (\hat{\phi}_2-\hat{\phi}_3)y_{T-2} -\hat{\phi}_3y_{T-3} + \varepsilon_{T+1}+\hat{\theta}_1\varepsilon_{T}. \\] Assuming we have observations up to time \\(T\\), all values on the right hand side are known except for \\(\varepsilon_{T+1}\\), which we replace with zero, and \\(\varepsilon_T\\), which we replace with the last observed residual \\(e_T\\): \\[ \hat{y}_{T+1|T} = (1+\hat{\phi}_1)y_{T} -(\hat{\phi}_1-\hat{\phi}_2)y_{T-1} - (\hat{\phi}_2-\hat{\phi}_3)y_{T-2} -\hat{\phi}_3y_{T-3} + \hat{\theta}_1e_{T}. \\]

A forecast of \\(y_{T+2}\\) is obtained by replacing \\(t\\) with \\(T+2\\) in [(9.5)](arima-forecasting.html#eq:arima301f) . All values on the right hand side will be known at time \\(T\\) except \\(y_{T+1}\\) which we replace with \\(\hat{y}_{T+1|T}\\), and \\(\varepsilon_{T+2}\\) and \\(\varepsilon_{T+1}\\), both of which we replace with zero: \\[ \hat{y}_{T+2|T} = (1+\hat{\phi}_1)\hat{y}_{T+1|T} -(\hat{\phi}_1-\hat{\phi}_2)y_{T} - (\hat{\phi}_2-\hat{\phi}_3)y_{T-1} -\hat{\phi}_3y_{T-2}. \\]

The process continues in this manner for all future time periods. In this way, any number of point forecasts can be obtained.

### Prediction intervals[](arima-forecasting.html#prediction-intervals-4)

The calculation of ARIMA prediction intervals is more difficult, and the details are largely beyond the scope of this book. We will only give some simple examples.

The first prediction interval is easy to calculate. If \\(\hat{\sigma}\\) is the standard deviation of the residuals, then a 95% prediction interval is given by \\(\hat{y}_{T+1|T} \pm 1.96\hat{\sigma}\\). This result is true for all ARIMA models regardless of their parameters and orders.

Multi-step prediction intervals for ARIMA(0,0,\\(q\\)) models are relatively easy to calculate. We can write the model as \\[ y_t = \varepsilon_t + \sum_{i=1}^q \theta_i \varepsilon_{t-i}. \\] Then, the estimated forecast variance can be written as \\[ \hat\sigma_h^2 = \hat{\sigma}^2 \left[ 1 + \sum_{i=1}^{h-1} \hat{\theta}_i^2\right], \qquad\text{for $h=2,3,\dots$,} \\] where \\(\hat{\theta}_i=0\\) for \\(i>q\\), and a 95% prediction interval is given by \\(\hat{y}_{T+h|T} \pm 1.96\hat\sigma_h\\).

In Section [9.4](MA.html#MA), we showed that an AR(1) model can be written as an MA(\\(\infty\\)) model. Using this equivalence, the above result for MA(\\(q\\)) models can also be used to obtain prediction intervals for AR(1) models.

More general results, and other special cases of multi-step prediction intervals for an ARIMA(\\(p,d,q\\)) model, are given in more advanced textbooks such as Brockwell & Davis ([2016](arima-forecasting.html#ref-BDbook16)).

The prediction intervals for ARIMA models are based on assumptions that the residuals are uncorrelated and normally distributed. If either of these assumptions does not hold, then the prediction intervals may be incorrect. For this reason, always plot the ACF and histogram of the residuals to check the assumptions before producing prediction intervals.

If the residuals are uncorrelated but not normally distributed, then bootstrapped intervals can be obtained instead, as discussed in Section [5.5](prediction-intervals.html#prediction-intervals). This is easily achieved by simply adding `bootstrap=TRUE` in the `forecast()` function.

In general, prediction intervals from ARIMA models increase as the forecast horizon increases. For stationary models (i.e., with \\(d=0\\)) they will converge, so that prediction intervals for long horizons are all essentially the same. For \\(d\ge1\\), the prediction intervals will continue to grow into the future.

As with most prediction interval calculations, ARIMA-based intervals tend to be too narrow. This occurs because only the variation in the errors has been accounted for. There is also variation in the parameter estimates, and in the model order, that has not been included in the calculation. In addition, the calculation assumes that the historical patterns that have been modelled will continue into the forecast period.

### Bibliography[](bibliography.html#bibliography)

Brockwell, P. J., & Davis, R. A. (2016). _Introduction to time series and forecasting_ (3rd ed). Springer. [__](http://amazon.com/dp/3319298526?tag=otexts20)


---

## 9.9 Seasonal ARIMA models[](seasonal-arima.html#seasonal-arima)

So far, we have restricted our attention to non-seasonal data and non-seasonal ARIMA models. However, ARIMA models are also capable of modelling a wide range of seasonal data.

A seasonal ARIMA model is formed by including additional seasonal terms in the ARIMA models we have seen so far. It is written as follows:

ARIMA  |  \\(\underbrace{(p, d, q)}\\) |  \\(\underbrace{(P, D, Q)_{m}}\\)  
---|---|---  
|  \\({\uparrow}\\) |  \\({\uparrow}\\)  
|  Non-seasonal part  |  Seasonal part   
|  of the model  |  of the model   
  
where \\(m =\\) the seasonal period (e.g., number of observations per year). We use uppercase notation for the seasonal parts of the model, and lowercase notation for the non-seasonal parts of the model.

The seasonal part of the model consists of terms that are similar to the non-seasonal components of the model, but involve backshifts of the seasonal period. For example, an ARIMA(1,1,1)(1,1,1)\\(_{4}\\) model (without a constant) is for quarterly data (\\(m=4\\)), and can be written as \\[ (1 - \phi_{1}B)~(1 - \Phi_{1}B^{4}) (1 - B) (1 - B^{4})y_{t} = (1 + \theta_{1}B)~ (1 + \Theta_{1}B^{4})\varepsilon_{t}. \\]

The additional seasonal terms are simply multiplied by the non-seasonal terms.

### ACF/PACF[](seasonal-arima.html#acfpacf)

The seasonal part of an AR or MA model will be seen in the seasonal lags of the PACF and ACF. For example, an ARIMA(0,0,0)(0,0,1)\\(_{12}\\) model will show:

  * a spike at lag 12 in the ACF but no other significant spikes;
  * exponential decay in the seasonal lags of the PACF (i.e., at lags 12, 24, 36, …).


Similarly, an ARIMA(0,0,0)(1,0,0)\\(_{12}\\) model will show:

  * exponential decay in the seasonal lags of the ACF;
  * a single significant spike at lag 12 in the PACF.


In considering the appropriate seasonal orders for a seasonal ARIMA model, restrict attention to the seasonal lags.

The modelling procedure is almost the same as for non-seasonal data, except that we need to select seasonal AR and MA terms as well as the non-seasonal components of the model. The process is best illustrated via examples.

### Example: Monthly US leisure and hospitality employment[](seasonal-arima.html#example-monthly-us-leisure-and-hospitality-employment)

We will describe seasonal ARIMA modelling using monthly US employment data for leisure and hospitality jobs from January 2001 to September 2019, shown in Figure [9.18](seasonal-arima.html#fig:usemployment1).
    
    
    [](seasonal-arima.html#cb197-1)leisure <- us_employment |>
    [](seasonal-arima.html#cb197-2)  filter(Title == "Leisure and Hospitality",
    [](seasonal-arima.html#cb197-3)         year(Month) > 2000) |>
    [](seasonal-arima.html#cb197-4)  mutate(Employed = Employed/1000) |>
    [](seasonal-arima.html#cb197-5)  select(Month, Employed)
    [](seasonal-arima.html#cb197-6)autoplot(leisure, Employed) +
    [](seasonal-arima.html#cb197-7)  labs(title = "US employment: leisure and hospitality",
    [](seasonal-arima.html#cb197-8)       y="Number of people (millions)")

Figure 9.18: Monthly US leisure and hospitality employment, 2001-2019. 

The data are clearly non-stationary, with strong seasonality and a nonlinear trend, so we will first take a seasonal difference. The seasonally differenced data are shown in Figure [9.19](seasonal-arima.html#fig:usemployment2).
    
    
    [](seasonal-arima.html#cb198-1)leisure |>
    [](seasonal-arima.html#cb198-2)  gg_tsdisplay(difference(Employed, 12),
    [](seasonal-arima.html#cb198-3)               plot_type='partial', lag=36) +
    [](seasonal-arima.html#cb198-4)  labs(title="Seasonally differenced", y="")

Figure 9.19: Seasonally differenced Monthly US leisure and hospitality employment. 

These are also clearly non-stationary, so we take a further first difference in Figure [9.20](seasonal-arima.html#fig:usemployment3).
    
    
    [](seasonal-arima.html#cb199-1)leisure |>
    [](seasonal-arima.html#cb199-2)  gg_tsdisplay(difference(Employed, 12) |> difference(),
    [](seasonal-arima.html#cb199-3)               plot_type='partial', lag=36) +
    [](seasonal-arima.html#cb199-4)  labs(title = "Double differenced", y="")

Figure 9.20: Double differenced Monthly US leisure and hospitality employment. 

Our aim now is to find an appropriate ARIMA model based on the ACF and PACF shown in Figure [9.20](seasonal-arima.html#fig:usemployment3). The significant spike at lag 2 in the ACF suggests a non-seasonal MA(2) component. The significant spike at lag 12 in the ACF suggests a seasonal MA(1) component. Consequently, we begin with an ARIMA(0,1,2)(0,1,1)\\(_{12}\\) model, indicating a first difference, a seasonal difference, and non-seasonal MA(2) and seasonal MA(1) component. If we had started with the PACF, we may have selected an ARIMA(2,1,0)(0,1,1)\\(_{12}\\) model — using the PACF to select the non-seasonal part of the model and the ACF to select the seasonal part of the model. We will also include an automatically selected model. By setting `stepwise=FALSE` and `approximation=FALSE`, we are making R work extra hard to find a good model. This takes much longer, but with only one series to model, the extra time taken is not a problem.
    
    
    [](seasonal-arima.html#cb200-1)fit <- leisure |>
    [](seasonal-arima.html#cb200-2)  model(
    [](seasonal-arima.html#cb200-3)    arima012011 = ARIMA(Employed ~ pdq(0,1,2) + PDQ(0,1,1)),
    [](seasonal-arima.html#cb200-4)    arima210011 = ARIMA(Employed ~ pdq(2,1,0) + PDQ(0,1,1)),
    [](seasonal-arima.html#cb200-5)    auto = ARIMA(Employed, stepwise = FALSE, approx = FALSE)
    [](seasonal-arima.html#cb200-6)  )
    [](seasonal-arima.html#cb200-7)fit |> pivot_longer(everything(), names_to = "Model name",
    [](seasonal-arima.html#cb200-8)                     values_to = "Orders")
    [](seasonal-arima.html#cb200-9)#> # A mable: 3 x 2
    [](seasonal-arima.html#cb200-10)#> # Key:     Model name [3]
    [](seasonal-arima.html#cb200-11)#>   `Model name`                    Orders
    [](seasonal-arima.html#cb200-12)#>   <chr>                          <model>
    [](seasonal-arima.html#cb200-13)#> 1 arima012011  <ARIMA(0,1,2)(0,1,1)[12]>
    [](seasonal-arima.html#cb200-14)#> 2 arima210011  <ARIMA(2,1,0)(0,1,1)[12]>
    [](seasonal-arima.html#cb200-15)#> 3 auto         <ARIMA(2,1,0)(1,1,1)[12]>
    [](seasonal-arima.html#cb200-16)glance(fit) |> arrange(AICc) |> select(.model:BIC)
    [](seasonal-arima.html#cb200-17)#> # A tibble: 3 × 6
    [](seasonal-arima.html#cb200-18)#>   .model       sigma2 log_lik   AIC  AICc   BIC
    [](seasonal-arima.html#cb200-19)#>   <chr>         <dbl>   <dbl> <dbl> <dbl> <dbl>
    [](seasonal-arima.html#cb200-20)#> 1 auto        0.00142    395. -780. -780. -763.
    [](seasonal-arima.html#cb200-21)#> 2 arima210011 0.00145    392. -776. -776. -763.
    [](seasonal-arima.html#cb200-22)#> 3 arima012011 0.00146    391. -775. -775. -761.

The `ARIMA()` function uses `unitroot_nsdiffs()` to determine \\(D\\) (the number of seasonal differences to use), and `unitroot_ndiffs()` to determine \\(d\\) (the number of ordinary differences to use), when these are not specified. The selection of the other model parameters (\\(p,q,P\\) and \\(Q\\)) are all determined by minimizing the AICc, as with non-seasonal ARIMA models.

The three fitted models have similar AICc values, with the automatically selected model being a little better. Our second “guess” of ARIMA(2,1,0)(0,1,1)\\(_{12}\\) turned out to be very close to the automatically selected model of ARIMA(2,1,0)(1,1,1)\\(_{12}\\).

The residuals for the best model are shown in Figure [9.21](seasonal-arima.html#fig:usemployment5).
    
    
    [](seasonal-arima.html#cb201-1)fit |> select(auto) |> gg_tsresiduals(lag=36)

Figure 9.21: Residuals from the fitted ARIMA(2,1,0)(1,1,1)\\(_{12}\\) model. 

One small but significant spike (at lag 11) out of 36 is still consistent with white noise. To be sure, we use a Ljung-Box test, being careful to set the degrees of freedom to match the number of parameters in the model.
    
    
    [](seasonal-arima.html#cb202-1)augment(fit) |>
    [](seasonal-arima.html#cb202-2)  filter(.model == "auto") |>
    [](seasonal-arima.html#cb202-3)  features(.innov, ljung_box, lag=24, dof=4)
    [](seasonal-arima.html#cb202-4)#> # A tibble: 1 × 3
    [](seasonal-arima.html#cb202-5)#>   .model lb_stat lb_pvalue
    [](seasonal-arima.html#cb202-6)#>   <chr>    <dbl>     <dbl>
    [](seasonal-arima.html#cb202-7)#> 1 auto      16.6     0.680

The large p-value confims that the residuals are similar to white noise.

Thus, we now have a seasonal ARIMA model that passes the required checks and is ready for forecasting. Forecasts from the model for the next three years are shown in Figure [9.22](seasonal-arima.html#fig:usemployment7). The forecasts have captured the seasonal pattern very well, and the increasing trend extends the recent pattern. The trend in the forecasts is induced by the double differencing.
    
    
    [](seasonal-arima.html#cb203-1)forecast(fit, h=36) |>
    [](seasonal-arima.html#cb203-2)  filter(.model=='auto') |>
    [](seasonal-arima.html#cb203-3)  autoplot(leisure) +
    [](seasonal-arima.html#cb203-4)  labs(title = "US employment: leisure and hospitality",
    [](seasonal-arima.html#cb203-5)       y="Number of people (millions)")

Figure 9.22: Forecasts of monthly US leisure and hospitality employment using the ARIMA(2,1,0)(1,1,1)\\(_{12}\\) model. 80% and 95% prediction intervals are shown. 

### Example: Corticosteroid drug sales in Australia[](seasonal-arima.html#example-corticosteroid-drug-sales-in-australia)

For our second example, we will try to forecast monthly corticosteroid drug sales in Australia. These are known as H02 drugs under the Anatomical Therapeutic Chemical classification scheme.
    
    
    [](seasonal-arima.html#cb204-1)h02 <- PBS |>
    [](seasonal-arima.html#cb204-2)  filter(ATC2 == "H02") |>
    [](seasonal-arima.html#cb204-3)  summarise(Cost = sum(Cost)/1e6)
    [](seasonal-arima.html#cb204-4)h02 |>
    [](seasonal-arima.html#cb204-5)  mutate(log(Cost)) |>
    [](seasonal-arima.html#cb204-6)  pivot_longer(-Month) |>
    [](seasonal-arima.html#cb204-7)  ggplot(aes(x = Month, y = value)) +
    [](seasonal-arima.html#cb204-8)  geom_line() +
    [](seasonal-arima.html#cb204-9)  facet_grid(name ~ ., scales = "free_y") +
    [](seasonal-arima.html#cb204-10)  labs(y="", title="Corticosteroid drug scripts (H02)")

Figure 9.23: Corticosteroid drug sales in Australia (in millions of scripts per month). Logged data shown in bottom panel. 

Data from July 1991 to June 2008 are plotted in Figure [9.23](seasonal-arima.html#fig:h02). There is a small increase in the variance with the level, so we take logarithms to stabilise the variance.

The data are strongly seasonal and obviously non-stationary, so seasonal differencing will be used. The seasonally differenced data are shown in Figure [9.24](seasonal-arima.html#fig:h02b). It is not clear at this point whether we should do another difference or not. We decide not to, but the choice is not obvious.

The last few observations appear to be different (more variable) from the earlier data. This may be due to the fact that data are sometimes revised when earlier sales are reported late.
    
    
    [](seasonal-arima.html#cb205-1)h02 |> gg_tsdisplay(difference(log(Cost), 12),
    [](seasonal-arima.html#cb205-2)                     plot_type='partial', lag_max = 24)

Figure 9.24: Seasonally differenced corticosteroid drug sales in Australia (in millions of scripts per month). 

In the plots of the seasonally differenced data, there are spikes in the PACF at lags 12 and 24, but nothing at seasonal lags in the ACF. This may be suggestive of a seasonal AR(2) term. In the non-seasonal lags, there are three significant spikes in the PACF, suggesting a possible AR(3) term. The pattern in the ACF is not indicative of any simple model.

Consequently, this initial analysis suggests that a possible model for these data is an ARIMA(3,0,0)(2,1,0)\\(_{12}\\). We fit this model, along with some variations on it, and compute the AICc values shown in Table [9.2](seasonal-arima.html#tab:h02aicc).

Table 9.2: AICc values for various ARIMA models applied for H02 monthly script sales data. Model | AICc  
---|---  
ARIMA(3,0,1)(0,1,2)\\(_{12}\\) | -485.5  
ARIMA(3,0,1)(1,1,1)\\(_{12}\\) | -484.2  
ARIMA(3,0,1)(0,1,1)\\(_{12}\\) | -483.7  
ARIMA(3,0,1)(2,1,0)\\(_{12}\\) | -476.3  
ARIMA(3,0,0)(2,1,0)\\(_{12}\\) | -475.1  
ARIMA(3,0,2)(2,1,0)\\(_{12}\\) | -474.9  
ARIMA(3,0,1)(1,1,0)\\(_{12}\\) | -463.4  
  
Of these models, the best is the ARIMA(3,0,1)(0,1,2)\\(_{12}\\) model (i.e., it has the smallest AICc value). The innovation residuals from this model are shown in Figure [9.25](seasonal-arima.html#fig:h02res).
    
    
    [](seasonal-arima.html#cb206-1)fit <- h02 |>
    [](seasonal-arima.html#cb206-2)  model(ARIMA(log(Cost) ~ 0 + pdq(3,0,1) + PDQ(0,1,2)))
    [](seasonal-arima.html#cb206-3)fit |> gg_tsresiduals(lag_max=36)

Figure 9.25: Innovation residuals from the ARIMA(3,0,1)(0,1,2)\\(_{12}\\) model applied to the H02 monthly script sales data. 
    
    
    [](seasonal-arima.html#cb207-1)augment(fit) |>
    [](seasonal-arima.html#cb207-2)  features(.innov, ljung_box, lag = 24, dof = 6)
    [](seasonal-arima.html#cb207-3)#> # A tibble: 1 × 3
    [](seasonal-arima.html#cb207-4)#>   .model                                             lb_stat lb_pvalue
    [](seasonal-arima.html#cb207-5)#>   <chr>                                                <dbl>     <dbl>
    [](seasonal-arima.html#cb207-6)#> 1 ARIMA(log(Cost) ~ 0 + pdq(3, 0, 1) + PDQ(0, 1, 2))    23.7     0.166

There are a few significant spikes in the ACF, but the model passes the Ljung-Box test.

Next we will try using the automatic ARIMA algorithm. Running `ARIMA()` with all arguments left at their default values led to an ARIMA(2,1,0)(0,1,1)\\(_{12}\\) model. Running `ARIMA()` with `stepwise=FALSE` and `approximation=FALSE` gives an ARIMA(2,1,3)(0,1,1)\\(_{12}\\) model. All of these models will give almost the same forecasts, so it doesn’t matter much which one we use.

### Test set evaluation:[](seasonal-arima.html#test-set-evaluation)

We will compare some of the models fitted so far using a test set consisting of the last two years of data. Thus, we fit the models using data from July 1991 to June 2006, and forecast the script sales for July 2006 – June 2008. The results are summarised in Table [9.3](seasonal-arima.html#tab:h02search).

Table 9.3: RMSE values for various ARIMA models applied for H02 monthly script sales data over test set July 2006 – June 2008. .model | RMSE  
---|---  
ARIMA(3,0,1)(1,1,1)\\(_{12}\\) | 0.0619  
ARIMA(3,0,1)(0,1,2)\\(_{12}\\) | 0.0621  
ARIMA(2,1,1)(0,1,1)\\(_{12}\\) | 0.0622  
ARIMA(2,1,2)(0,1,1)\\(_{12}\\) | 0.0623  
ARIMA(2,1,4)(0,1,1)\\(_{12}\\) | 0.0627  
ARIMA(2,1,3)(0,1,1)\\(_{12}\\) | 0.0628  
ARIMA(3,0,1)(0,1,1)\\(_{12}\\) | 0.0630  
ARIMA(3,0,2)(0,1,1)\\(_{12}\\) | 0.0630  
ARIMA(2,1,0)(0,1,1)\\(_{12}\\) | 0.0630  
ARIMA(3,0,1)(0,1,3)\\(_{12}\\) | 0.0630  
ARIMA(3,0,3)(0,1,1)\\(_{12}\\) | 0.0633  
ARIMA(3,0,2)(2,1,0)\\(_{12}\\) | 0.0651  
ARIMA(3,0,1)(2,1,0)\\(_{12}\\) | 0.0653  
ARIMA(2,1,0)(1,1,0)\\(_{12}\\) | 0.0666  
ARIMA(3,0,1)(1,1,0)\\(_{12}\\) | 0.0666  
ARIMA(3,0,0)(2,1,0)\\(_{12}\\) | 0.0668  
  
The models chosen manually are close to the best model over this test set based on the RMSE values, while those models chosen automatically with `ARIMA()` are not far behind.

When models are compared using AICc values, it is important that all models have the same orders of differencing. However, when comparing models using a test set, it does not matter how the forecasts were produced — the comparisons are always valid. Consequently, in the table above, we can include some models with only seasonal differencing and some models with both first and seasonal differencing, while in the earlier table containing AICc values, we only compared models with seasonal differencing but no first differencing.

Sometimes it is not possible to find a model that passes all of the residual tests. In practice, we would normally use the best model we could find, even if it did not pass all of the tests.

Forecasts from the ARIMA(3,0,1)(0,1,2)\\(_{12}\\) model (which has the second lowest RMSE value on the test set, and the best AICc value amongst models with only seasonal differencing) are shown in Figure [9.26](seasonal-arima.html#fig:h02f).
    
    
    [](seasonal-arima.html#cb208-1)h02 |>
    [](seasonal-arima.html#cb208-2)  model(ARIMA(log(Cost) ~ 0 + pdq(3,0,1) + PDQ(0,1,2))) |>
    [](seasonal-arima.html#cb208-3)  forecast() |>
    [](seasonal-arima.html#cb208-4)  autoplot(h02) +
    [](seasonal-arima.html#cb208-5)  labs(y=" $AU (millions)",
    [](seasonal-arima.html#cb208-6)       title="Corticosteroid drug scripts (H02) sales")

Figure 9.26: Forecasts from the ARIMA(3,0,1)(0,1,2)\\(_{12}\\) model applied to the H02 monthly script sales data. 


---

## 9.10 ARIMA vs ETS[](arima-ets.html#arima-ets)

It is a commonly held myth that ARIMA models are more general than exponential smoothing. While linear exponential smoothing models are all special cases of ARIMA models, the non-linear exponential smoothing models have no equivalent ARIMA counterparts. On the other hand, there are also many ARIMA models that have no exponential smoothing counterparts. In particular, all ETS models are non-stationary, while some ARIMA models are stationary. Figure [9.27](arima-ets.html#fig:venn) shows the overlap between the two model classes.

Figure 9.27: The ETS and ARIMA model classes overlap with the additive ETS models having equivalent ARIMA forms. 

The ETS models with seasonality or non-damped trend or both have two unit roots (i.e., they need two levels of differencing to make them stationary). All other ETS models have one unit root (they need one level of differencing to make them stationary).

Table [9.4](arima-ets.html#tab:etsarima) gives the equivalence relationships for the two classes of models. For the seasonal models, the ARIMA parameters have a large number of restrictions.

Table 9.4: Equivalence relationships between ETS and ARIMA models.  ETS model  |  ARIMA model  |  Parameters   
---|---|---  
ETS(A,N,N)  |  ARIMA(0,1,1)  |  \\(\theta_1=\alpha-1\\)  
ETS(A,A,N)  |  ARIMA(0,2,2)  |  \\(\theta_1=\alpha+\beta-2\\)  
|  |  \\(\theta_2=1-\alpha\\)  
ETS(A,A\\(_d\\),N)  |  ARIMA(1,1,2)  |  \\(\phi_1=\phi\\)  
|  |  \\(\theta_1=\alpha+\phi\beta-1-\phi\\)  
|  |  \\(\theta_2=(1-\alpha)\phi\\)  
ETS(A,N,A)  |  ARIMA(0,1,\\(m\\))(0,1,0)\\(_m\\) |   
ETS(A,A,A)  |  ARIMA(0,1,\\(m+1\\))(0,1,0)\\(_m\\) |   
ETS(A,A\\(_d\\),A)  |  ARIMA(1,0,\\(m+1\\))(0,1,0)\\(_m\\) |   
  
The AICc is useful for selecting between models in the same class. For example, we can use it to select an ARIMA model between candidate ARIMA models[20](arima-ets.html#fn20) or an ETS model between candidate ETS models. However, it cannot be used to compare between ETS and ARIMA models because they are in different model classes, and the likelihood is computed in different ways. The examples below demonstrate selecting between these classes of models.

### Comparing `ARIMA()` and `ETS()` on non-seasonal data[](arima-ets.html#comparing-arima-and-ets-on-non-seasonal-data)

We can use time series cross-validation to compare ARIMA and ETS models. Let’s consider the Australian population from the `global_economy` dataset, as introduced in Section [8.2](holt.html#holt).
    
    
    [](arima-ets.html#cb209-1)aus_economy <- global_economy |>
    [](arima-ets.html#cb209-2)  filter(Code == "AUS") |>
    [](arima-ets.html#cb209-3)  mutate(Population = Population/1e6)
    [](arima-ets.html#cb209-4)
    [](arima-ets.html#cb209-5)aus_economy |>
    [](arima-ets.html#cb209-6)  slice(-n()) |>
    [](arima-ets.html#cb209-7)  stretch_tsibble(.init = 10) |>
    [](arima-ets.html#cb209-8)  model(
    [](arima-ets.html#cb209-9)    ETS(Population),
    [](arima-ets.html#cb209-10)    ARIMA(Population)
    [](arima-ets.html#cb209-11)  ) |>
    [](arima-ets.html#cb209-12)  forecast(h = 1) |>
    [](arima-ets.html#cb209-13)  accuracy(aus_economy) |>
    [](arima-ets.html#cb209-14)  select(.model, RMSE:MAPE)
    [](arima-ets.html#cb209-15)#> # A tibble: 2 × 5
    [](arima-ets.html#cb209-16)#>   .model              RMSE    MAE   MPE  MAPE
    [](arima-ets.html#cb209-17)#>   <chr>              <dbl>  <dbl> <dbl> <dbl>
    [](arima-ets.html#cb209-18)#> 1 ARIMA(Population) 0.194  0.0789 0.277 0.509
    [](arima-ets.html#cb209-19)#> 2 ETS(Population)   0.0774 0.0543 0.112 0.327

In this case the ETS model has higher accuracy on the cross-validated performance measures. Below we generate and plot forecasts for the next 5 years generated from an ETS model.
    
    
    [](arima-ets.html#cb210-1)aus_economy |>
    [](arima-ets.html#cb210-2)  model(ETS(Population)) |>
    [](arima-ets.html#cb210-3)  forecast(h = "5 years") |>
    [](arima-ets.html#cb210-4)  autoplot(aus_economy |> filter(Year >= 2000)) +
    [](arima-ets.html#cb210-5)  labs(title = "Australian population",
    [](arima-ets.html#cb210-6)       y = "People (millions)")

Figure 9.28: Forecasts from an ETS model fitted to the Australian population. 

### Comparing `ARIMA()` and `ETS()` on seasonal data[](arima-ets.html#comparing-arima-and-ets-on-seasonal-data)

In this case we want to compare seasonal ARIMA and ETS models applied to the quarterly cement production data (from `aus_production`). Because the series is relatively long, we can afford to use a training and a test set rather than time series cross-validation. The advantage is that this is much faster. We create a training set from the beginning of 1988 to the end of 2007 and select an ARIMA and an ETS model using the `ARIMA()` and `ETS()` functions.
    
    
    [](arima-ets.html#cb211-1)cement <- aus_production |>
    [](arima-ets.html#cb211-2)  select(Cement) |>
    [](arima-ets.html#cb211-3)  filter_index("1988 Q1" ~ .)
    [](arima-ets.html#cb211-4)train <- cement |> filter_index(. ~ "2007 Q4")

The output below shows the model selected and estimated by `ARIMA()`. The ARIMA model does well in capturing all the dynamics in the data as the residuals seem to be white noise.
    
    
    [](arima-ets.html#cb212-1)fit_arima <- train |> model(ARIMA(Cement))
    [](arima-ets.html#cb212-2)report(fit_arima)
    [](arima-ets.html#cb212-3)#> Series: Cement 
    [](arima-ets.html#cb212-4)#> Model: ARIMA(1,0,1)(2,1,1)[4] w/ drift 
    [](arima-ets.html#cb212-5)#> 
    [](arima-ets.html#cb212-6)#> Coefficients:
    [](arima-ets.html#cb212-7)#>          ar1      ma1   sar1     sar2     sma1  constant
    [](arima-ets.html#cb212-8)#>       0.8886  -0.2366  0.081  -0.2345  -0.8979     5.388
    [](arima-ets.html#cb212-9)#> s.e.  0.0842   0.1334  0.157   0.1392   0.1780     1.484
    [](arima-ets.html#cb212-10)#> 
    [](arima-ets.html#cb212-11)#> sigma^2 estimated as 11456:  log likelihood=-463.5
    [](arima-ets.html#cb212-12)#> AIC=941   AICc=942.7   BIC=957.4
    [](arima-ets.html#cb212-13)fit_arima |> gg_tsresiduals(lag_max = 16)

Figure 9.29: Residual diagnostic plots for the ARIMA model fitted to the quarterly cement production training data. 
    
    
    [](arima-ets.html#cb213-1)augment(fit_arima) |>
    [](arima-ets.html#cb213-2)  features(.innov, ljung_box, lag = 8, dof = 5)
    [](arima-ets.html#cb213-3)#> # A tibble: 1 × 3
    [](arima-ets.html#cb213-4)#>   .model        lb_stat lb_pvalue
    [](arima-ets.html#cb213-5)#>   <chr>           <dbl>     <dbl>
    [](arima-ets.html#cb213-6)#> 1 ARIMA(Cement)   0.783     0.853

The output below also shows the ETS model selected and estimated by `ETS()`. This model also does well in capturing all the dynamics in the data, as the residuals similarly appear to be white noise.
    
    
    [](arima-ets.html#cb214-1)fit_ets <- train |> model(ETS(Cement))
    [](arima-ets.html#cb214-2)report(fit_ets)
    [](arima-ets.html#cb214-3)#> Series: Cement 
    [](arima-ets.html#cb214-4)#> Model: ETS(M,N,M) 
    [](arima-ets.html#cb214-5)#>   Smoothing parameters:
    [](arima-ets.html#cb214-6)#>     alpha = 0.7534 
    [](arima-ets.html#cb214-7)#>     gamma = 1e-04 
    [](arima-ets.html#cb214-8)#> 
    [](arima-ets.html#cb214-9)#>   Initial states:
    [](arima-ets.html#cb214-10)#>  l[0]  s[0] s[-1] s[-2]  s[-3]
    [](arima-ets.html#cb214-11)#>  1695 1.031 1.045 1.011 0.9122
    [](arima-ets.html#cb214-12)#> 
    [](arima-ets.html#cb214-13)#>   sigma^2:  0.0034
    [](arima-ets.html#cb214-14)#> 
    [](arima-ets.html#cb214-15)#>  AIC AICc  BIC 
    [](arima-ets.html#cb214-16)#> 1104 1106 1121
    [](arima-ets.html#cb214-17)fit_ets |>
    [](arima-ets.html#cb214-18)  gg_tsresiduals(lag_max = 16)

Figure 9.30: Residual diagnostic plots for the ETS model fitted to the quarterly cement production training data. 
    
    
    [](arima-ets.html#cb215-1)augment(fit_ets) |>
    [](arima-ets.html#cb215-2)  features(.innov, ljung_box, lag = 8)
    [](arima-ets.html#cb215-3)#> # A tibble: 1 × 3
    [](arima-ets.html#cb215-4)#>   .model      lb_stat lb_pvalue
    [](arima-ets.html#cb215-5)#>   <chr>         <dbl>     <dbl>
    [](arima-ets.html#cb215-6)#> 1 ETS(Cement)    5.49     0.704

The output below evaluates the forecasting performance of the two competing models over the test set. In this case the ARIMA model seems to be the slightly more accurate model based on the test set RMSE, MAPE and MASE.
    
    
    [](arima-ets.html#cb216-1)# Generate forecasts and compare accuracy over the test set
    [](arima-ets.html#cb216-2)bind_rows(
    [](arima-ets.html#cb216-3)    fit_arima |> accuracy(),
    [](arima-ets.html#cb216-4)    fit_ets |> accuracy(),
    [](arima-ets.html#cb216-5)    fit_arima |> forecast(h = 10) |> accuracy(cement),
    [](arima-ets.html#cb216-6)    fit_ets |> forecast(h = 10) |> accuracy(cement)
    [](arima-ets.html#cb216-7)  ) |>
    [](arima-ets.html#cb216-8)  select(-ME, -MPE, -ACF1)
    [](arima-ets.html#cb216-9)#> # A tibble: 4 × 7
    [](arima-ets.html#cb216-10)#>   .model        .type     RMSE   MAE  MAPE  MASE RMSSE
    [](arima-ets.html#cb216-11)#>   <chr>         <chr>    <dbl> <dbl> <dbl> <dbl> <dbl>
    [](arima-ets.html#cb216-12)#> 1 ARIMA(Cement) Training  100.  79.9  4.37 0.546 0.582
    [](arima-ets.html#cb216-13)#> 2 ETS(Cement)   Training  103.  80.0  4.41 0.547 0.596
    [](arima-ets.html#cb216-14)#> 3 ARIMA(Cement) Test      216. 186.   8.68 1.27  1.26 
    [](arima-ets.html#cb216-15)#> 4 ETS(Cement)   Test      222. 191.   8.85 1.30  1.29

Below we generate and plot forecasts from the ARIMA model for the next 3 years.
    
    
    [](arima-ets.html#cb217-1)cement |>
    [](arima-ets.html#cb217-2)  model(ARIMA(Cement)) |>
    [](arima-ets.html#cb217-3)  forecast(h="3 years") |>
    [](arima-ets.html#cb217-4)  autoplot(cement) +
    [](arima-ets.html#cb217-5)  labs(title = "Cement production in Australia",
    [](arima-ets.html#cb217-6)       y = "Tonnes ('000)")

Figure 9.31: Forecasts from an ARIMA model fitted to all of the available quarterly cement production data since 1988. 

* * *

  20. As already noted, comparing information criteria is only valid for ARIMA models of the same orders of differencing.[↩︎](arima-ets.html#fnref20)




---

## 9.11 Exercises[](arima-exercises.html#arima-exercises)

  1. Figure [9.32](arima-exercises.html#fig:wnacfplus) shows the ACFs for 36 random numbers, 360 random numbers and 1,000 random numbers.

     1. Explain the differences among these figures. Do they all indicate that the data are white noise?

Figure 9.32: Left: ACF for a white noise series of 36 numbers. Middle: ACF for a white noise series of 360 numbers. Right: ACF for a white noise series of 1,000 numbers. 

     2. Why are the critical values at different distances from the mean of zero? Why are the autocorrelations different in each figure when they each refer to white noise?
  2. A classic example of a non-stationary series are stock prices. Plot the daily closing prices for Amazon stock (contained in `gafa_stock`), along with the ACF and PACF. Explain how each plot shows that the series is non-stationary and should be differenced.

  3. For the following series, find an appropriate Box-Cox transformation and order of differencing in order to obtain stationary data.

     1. Turkish GDP from `global_economy`.
     2. Accommodation takings in the state of Tasmania from `aus_accommodation`.
     3. Monthly sales from `souvenirs`.
  4. For the `souvenirs` data, write down the differences you chose above using backshift operator notation.

  5. For your retail data (from Exercise 7 in Section [2.10](graphics-exercises.html#graphics-exercises)), find the appropriate order of differencing (after transformation if necessary) to obtain stationary data.

  6. Simulate and plot some data from simple ARIMA models.

     1. Use the following R code to generate data from an AR(1) model with \\(\phi_{1} = 0.6\\) and \\(\sigma^2=1\\). The process starts with \\(y_1=0\\).
            
            [](arima-exercises.html#cb218-1)y <- numeric(100)
            [](arima-exercises.html#cb218-2)e <- rnorm(100)
            [](arima-exercises.html#cb218-3)for(i in 2:100)
            [](arima-exercises.html#cb218-4)  y[i] <- 0.6*y[i-1] + e[i]
            [](arima-exercises.html#cb218-5)sim <- tsibble(idx = seq_len(100), y = y, index = idx)

     2. Produce a time plot for the series. How does the plot change as you change \\(\phi_1\\)?

     3. Write your own code to generate data from an MA(1) model with \\(\theta_{1} = 0.6\\) and \\(\sigma^2=1\\).

     4. Produce a time plot for the series. How does the plot change as you change \\(\theta_1\\)?

     5. Generate data from an ARMA(1,1) model with \\(\phi_{1} = 0.6\\), \\(\theta_{1} = 0.6\\) and \\(\sigma^2=1\\).

     6. Generate data from an AR(2) model with \\(\phi_{1} =-0.8\\), \\(\phi_{2} = 0.3\\) and \\(\sigma^2=1\\). (Note that these parameters will give a non-stationary series.)

     7. Graph the latter two series and compare them.

  7. Consider `aus_airpassengers`, the total number of passengers (in millions) from Australian air carriers for the period 1970-2011.

     1. Use `ARIMA()` to find an appropriate ARIMA model. What model was selected. Check that the residuals look like white noise. Plot forecasts for the next 10 periods.
     2. Write the model in terms of the backshift operator.
     3. Plot forecasts from an ARIMA(0,1,0) model with drift and compare these to part a.
     4. Plot forecasts from an ARIMA(2,1,2) model with drift and compare these to parts a and c. Remove the constant and see what happens.
     5. Plot forecasts from an ARIMA(0,2,1) model with a constant. What happens?
  8. For the United States GDP series (from `global_economy`):

     1. if necessary, find a suitable Box-Cox transformation for the data;
     2. fit a suitable ARIMA model to the transformed data using `ARIMA()`;
     3. try some other plausible models by experimenting with the orders chosen;
     4. choose what you think is the best model and check the residual diagnostics;
     5. produce forecasts of your fitted model. Do the forecasts look reasonable?
     6. compare the results with what you would obtain using `ETS()` (with no transformation).
  9. Consider `aus_arrivals`, the quarterly number of international visitors to Australia from several countries for the period 1981 Q1 – 2012 Q3.

     1. Select one country and describe the time plot.
     2. Use differencing to obtain stationary data.
     3. What can you learn from the ACF graph of the differenced data?
     4. What can you learn from the PACF graph of the differenced data?
     5. What model do these graphs suggest?
     6. Does `ARIMA()` give the same model that you chose? If not, which model do you think is better?
     7. Write the model in terms of the backshift operator, then without using the backshift operator.
  10. Choose a series from `us_employment`, the total employment in different industries in the United States.

     1. Produce an STL decomposition of the data and describe the trend and seasonality.
     2. Do the data need transforming? If so, find a suitable transformation.
     3. Are the data stationary? If not, find an appropriate differencing which yields stationary data.
     4. Identify a couple of ARIMA models that might be useful in describing the time series. Which of your models is the best according to their AICc values?
     5. Estimate the parameters of your best model and do diagnostic testing on the residuals. Do the residuals resemble white noise? If not, try to find another ARIMA model which fits better.
     6. Forecast the next 3 years of data. Get the latest figures from <https://fred.stlouisfed.org/categories/11> to check the accuracy of your forecasts.
     7. Eventually, the prediction intervals are so wide that the forecasts are not particularly useful. How many years of forecasts do you think are sufficiently accurate to be usable?
  11. Choose one of the following seasonal time series: the Australian production of electricity, cement, or gas (from `aus_production`).

     1. Do the data need transforming? If so, find a suitable transformation.
     2. Are the data stationary? If not, find an appropriate differencing which yields stationary data.
     3. Identify a couple of ARIMA models that might be useful in describing the time series. Which of your models is the best according to their AIC values?
     4. Estimate the parameters of your best model and do diagnostic testing on the residuals. Do the residuals resemble white noise? If not, try to find another ARIMA model which fits better.
     5. Forecast the next 24 months of data using your preferred model.
     6. Compare the forecasts obtained using `ETS()`.
  12. For the same time series you used in the previous exercise, try using a non-seasonal model applied to the seasonally adjusted data obtained from STL. Compare the forecasts with those obtained in the previous exercise. Which do you think is the best approach?

  13. For the Australian tourism data (from `tourism`):

     1. Fit ARIMA models for each time series.
     2. Produce forecasts of your fitted models.
     3. Check the forecasts for the “Snowy Mountains” and “Melbourne” regions. Do they look reasonable?
  14. For your retail time series (Exercise 5 above):

     1. develop an appropriate seasonal ARIMA model;
     2. compare the forecasts with those you obtained in earlier chapters;
     3. Obtain up-to-date retail data from the [ABS website](https://bit.ly/absretail) (Cat 8501.0, Table 11), and compare your forecasts with the actual numbers. How good were the forecasts from the various models?
  15. Consider the number of Snowshoe Hare furs traded by the Hudson Bay Company between 1845 and 1935 (data set `pelt`).

     1. Produce a time plot of the time series.

     2. Assume you decide to fit the following model: \\[ y_t = c + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \phi_3 y_{t-3} + \phi_4 y_{t-4} + \varepsilon_t, \\] where \\(\varepsilon_t\\) is a white noise series. What sort of ARIMA model is this (i.e., what are \\(p\\), \\(d\\), and \\(q\\))?

     3. By examining the ACF and PACF of the data, explain why this model is appropriate.

     4. The last five values of the series are given below:

Year | 1931 | 1932 | 1933 | 1934 | 1935  
---|---|---|---|---|---  
Number of hare pelts | 19520 | 82110 | 89760 | 81660 | 15760  
  
The estimated parameters are \\(c = 30993\\), \\(\phi_1 = 0.82\\), \\(\phi_2 = -0.29\\), \\(\phi_3 = -0.01\\), and \\(\phi_4 = -0.22\\). Without using the `forecast()` function, calculate forecasts for the next three years (1936–1939).

     5. Now fit the model in R and obtain the forecasts using `forecast()`. How are they different from yours? Why?

  16. The population of Switzerland from 1960 to 2017 is in data set `global_economy`.

     1. Produce a time plot of the data.

     2. You decide to fit the following model to the series: \\[y_t = c + y_{t-1} + \phi_1 (y_{t-1} - y_{t-2}) + \phi_2 (y_{t-2} - y_{t-3}) + \phi_3( y_{t-3} - y_{t-4}) + \varepsilon_t\\] where \\(y_t\\) is the Population in year \\(t\\) and \\(\varepsilon_t\\) is a white noise series. What sort of ARIMA model is this (i.e., what are \\(p\\), \\(d\\), and \\(q\\))?

     3. Explain why this model was chosen using the ACF and PACF of the differenced series.

     4. The last five values of the series are given below.

Year | 2013 | 2014 | 2015 | 2016 | 2017  
---|---|---|---|---|---  
Population (millions) | 8.09 | 8.19 | 8.28 | 8.37 | 8.47  
  
The estimated parameters are \\(c = 0.0053\\), \\(\phi_1 = 1.64\\), \\(\phi_2 = -1.17\\), and \\(\phi_3 = 0.45\\). Without using the `forecast()` function, calculate forecasts for the next three years (2018–2020).

     5. Now fit the model in R and obtain the forecasts from the same model. How are they different from yours? Why?




---

## 9.12 Further reading[](arima-reading.html#arima-reading)

  * The classic text which popularised ARIMA modelling was Box & Jenkins ([1970](arima-reading.html#ref-BJ70)). The most recent edition is Box et al. ([2015](arima-reading.html#ref-BJRL15)), and it is still an excellent reference for all things ARIMA.
  * Brockwell & Davis ([2016](arima-reading.html#ref-BDbook16)) provides a good introduction to the mathematical background to the models.
  * The Hyndman-Khandakar algorithm for automatically selecting an ARIMA model is described in Hyndman & Khandakar ([2008](arima-reading.html#ref-HK08)).
  * Peña et al. ([2001](arima-reading.html#ref-PTT01)) describes some alternative automatic algorithms to the one used by `ARIMA()`.


### Bibliography[](bibliography.html#bibliography)

Box, G. E. P., & Jenkins, G. M. (1970). _Time series analysis: Forecasting and control_. Holden-Day. 

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). _Time series analysis: Forecasting and control_ (5th ed). John Wiley & Sons. [__](http://amazon.com/dp/1118675029?tag=otexts20)

Brockwell, P. J., & Davis, R. A. (2016). _Introduction to time series and forecasting_ (3rd ed). Springer. [__](http://amazon.com/dp/3319298526?tag=otexts20)

Hyndman, R. J., & Khandakar, Y. (2008). Automatic time series forecasting: The forecast package for R. _Journal of Statistical Software_ , _27_(1), 1–22. [__](https://doi.org/10.18637/jss.v027.i03)

Peña, D., Tiao, G. C., & Tsay, R. S. (Eds.). (2001). _A course in time series analysis_. John Wiley & Sons. [__](http://amazon.com/dp/047136164X?tag=otexts20)


---

# Chapter 10 Dynamic regression models[](dynamic.html#dynamic)

The time series models in the previous two chapters allow for the inclusion of information from past observations of a series, but not for the inclusion of other information that may also be relevant. For example, the effects of holidays, competitor activity, changes in the law, the wider economy, or other external variables, may explain some of the historical variation and may lead to more accurate forecasts. On the other hand, the regression models in Chapter [7](regression.html#regression) allow for the inclusion of a lot of relevant information from predictor variables, but do not allow for the subtle time series dynamics that can be handled with ARIMA models. In this chapter, we consider how to extend ARIMA models in order to allow other information to be included in the models.

In Chapter [7](regression.html#regression) we considered regression models of the form \\[ y_t = \beta_0 + \beta_1 x_{1,t} + \dots + \beta_k x_{k,t} + \varepsilon_t, \\] where \\(y_t\\) is a linear function of the \\(k\\) predictor variables (\\(x_{1,t},\dots,x_{k,t}\\)), and \\(\varepsilon_t\\) is usually assumed to be an uncorrelated error term (i.e., it is white noise). We considered tests such as the Ljung-Box test for assessing whether the resulting residuals were significantly correlated.

In this chapter, we will allow the errors from a regression to contain autocorrelation. To emphasise this change in perspective, we will replace \\(\varepsilon_t\\) with \\(\eta_t\\) in the equation. The error series \\(\eta_t\\) is assumed to follow an ARIMA model. For example, if \\(\eta_t\\) follows an ARIMA(1,1,1) model, we can write \\[\begin{align*} y_t &= \beta_0 + \beta_1 x_{1,t} + \dots + \beta_k x_{k,t} + \eta_t,\\\ & (1-\phi_1B)(1-B)\eta_t = (1+\theta_1B)\varepsilon_t, \end{align*}\\] where \\(\varepsilon_t\\) is a white noise series.

Notice that the model has two error terms here — the error from the regression model, which we denote by \\(\eta_t\\), and the error from the ARIMA model, which we denote by \\(\varepsilon_t\\). Only the ARIMA model errors are assumed to be white noise.


---

## 10.1 Estimation[](estimation.html#estimation)

When we estimate the parameters from the model, we need to minimise the sum of squared \\(\varepsilon_t\\) values. If we minimise the sum of squared \\(\eta_t\\) values instead (which is what would happen if we estimated the regression model ignoring the autocorrelations in the errors), then several problems arise.

  1. The estimated coefficients \\(\hat{\beta}_0,\dots,\hat{\beta}_k\\) are no longer the best estimates, as some information has been ignored in the calculation;
  2. Any statistical tests associated with the model (e.g., t-tests on the coefficients) will be incorrect.
  3. The AICc values of the fitted models are no longer a good guide as to which is the best model for forecasting.
  4. In most cases, the \\(p\\)-values associated with the coefficients will be too small, and so some predictor variables will appear to be important when they are not. This is known as “spurious regression”.


Minimising the sum of squared \\(\varepsilon_t\\) values avoids these problems. Alternatively, maximum likelihood estimation can be used; this will give similar estimates of the coefficients.

An important consideration when estimating a regression with ARMA errors is that all of the variables in the model must first be stationary. Thus, we first have to check that \\(y_t\\) and all of the predictors \\((x_{1,t},\dots,x_{k,t})\\) appear to be stationary. If we estimate the model when any of these are non-stationary, the estimated coefficients will not be consistent estimates (and therefore may not be meaningful). One exception to this is the case where non-stationary variables are co-integrated. If there exists a linear combination of the non-stationary \\(y_t\\) and the predictors that is stationary, then the estimated coefficients will be consistent.[21](estimation.html#fn21)

We therefore first difference the non-stationary variables in the model. It is often desirable to maintain the form of the relationship between \\(y_t\\) and the predictors, and consequently it is common to difference all of the variables if any of them need differencing. The resulting model is then called a “model in differences”, as distinct from a “model in levels”, which is what is obtained when the original data are used without differencing.

If all of the variables in the model are stationary, then we only need to consider an ARMA process for the errors. It is easy to see that a regression model with ARIMA errors is equivalent to a regression model in differences with ARMA errors. For example, if the above regression model with ARIMA(1,1,1) errors is differenced we obtain the model \\[\begin{align*} y'_t &= \beta_1 x'_{1,t} + \dots + \beta_k x'_{k,t} + \eta'_t,\\\ & (1-\phi_1B)\eta'_t = (1+\theta_1B)\varepsilon_t, \end{align*}\\] where \\(y'_t=y_t-y_{t-1}\\), \\(x'_{t,i}=x_{t,i}-x_{t-1,i}\\) and \\(\eta'_t=\eta_t-\eta_{t-1}\\), which is a regression model in differences with ARMA errors.

### Bibliography[](bibliography.html#bibliography)

Harris, R., & Sollis, R. (2003). _Applied time series modelling and forecasting_. John Wiley & Sons. [__](http://amazon.com/dp/0470844434?tag=otexts20)

* * *

  21. Forecasting with cointegrated models is discussed by Harris & Sollis ([2003](estimation.html#ref-Harris03)).[↩︎](estimation.html#fnref21)




---

## 10.2 Regression with ARIMA errors using `fable`[](regarima.html#regarima)

The function `ARIMA()` will fit a regression model with ARIMA errors if exogenous regressors are included in the formula. As introduced in Section [9.5](non-seasonal-arima.html#non-seasonal-arima), the `pdq()` special specifies the order of the ARIMA error model. If differencing is specified, then the differencing is applied to all variables in the regression model before the model is estimated. For example, the command
    
    
    [](regarima.html#cb219-1)ARIMA(y ~ x + pdq(1,1,0))

will fit the model \\(y_t' = \beta_1 x'_t + \eta'_t\\), where \\(\eta'_t = \phi_1 \eta'_{t-1} + \varepsilon_t\\) is an AR(1) error. This is equivalent to the model \\[ y_t = \beta_0 + \beta_1 x_t + \eta_t, \\] where \\(\eta_t\\) is an ARIMA(1,1,0) error. Notice that the constant term disappears due to the differencing. To include a constant in the differenced model, we would add `1` to the model formula.

The `ARIMA()` function can also be used to select the best ARIMA model for the errors. This is done by not specifying the `pdq()` special. Whether differencing is required is determined by applying a KPSS test to the residuals from the regression model estimated using ordinary least squares. If differencing is required, then all variables are differenced and the model re-estimated using maximum likelihood estimation. The final model will be expressed in terms of the original variables, even if it has been estimated using differenced variables.

The AICc is calculated for the final model, and this value can be used to determine the best predictors. That is, the procedure should be repeated for all subsets of predictors to be considered, and the model with the lowest AICc value selected.

### Example: US Personal Consumption and Income[](regarima.html#example-us-personal-consumption-and-income)

Figure [10.1](regarima.html#fig:usconsump) shows the quarterly changes in personal consumption expenditure and personal disposable income from 1970 to 2019 Q2. We would like to forecast changes in expenditure based on changes in income. A change in income does not necessarily translate to an instant change in consumption (e.g., after the loss of a job, it may take a few months for expenses to be reduced to allow for the new circumstances). However, we will ignore this complexity in this example and try to measure the instantaneous effect of the average change of income on the average change of consumption expenditure.
    
    
    [](regarima.html#cb220-1)us_change |>
    [](regarima.html#cb220-2)  pivot_longer(c(Consumption, Income),
    [](regarima.html#cb220-3)               names_to = "var", values_to = "value") |>
    [](regarima.html#cb220-4)  ggplot(aes(x = Quarter, y = value)) +
    [](regarima.html#cb220-5)  geom_line() +
    [](regarima.html#cb220-6)  facet_grid(vars(var), scales = "free_y") +
    [](regarima.html#cb220-7)  labs(title = "US consumption and personal income",
    [](regarima.html#cb220-8)       y = "Quarterly % change")

Figure 10.1: Percentage changes in quarterly personal consumption expenditure and personal disposable income for the USA, 1970 Q1 to 2019 Q2. 
    
    
    [](regarima.html#cb221-1)fit <- us_change |>
    [](regarima.html#cb221-2)  model(ARIMA(Consumption ~ Income))
    [](regarima.html#cb221-3)report(fit)
    [](regarima.html#cb221-4)#> Series: Consumption 
    [](regarima.html#cb221-5)#> Model: LM w/ ARIMA(1,0,2) errors 
    [](regarima.html#cb221-6)#> 
    [](regarima.html#cb221-7)#> Coefficients:
    [](regarima.html#cb221-8)#>          ar1      ma1     ma2  Income  intercept
    [](regarima.html#cb221-9)#>       0.7070  -0.6172  0.2066  0.1976     0.5949
    [](regarima.html#cb221-10)#> s.e.  0.1068   0.1218  0.0741  0.0462     0.0850
    [](regarima.html#cb221-11)#> 
    [](regarima.html#cb221-12)#> sigma^2 estimated as 0.3113:  log likelihood=-163
    [](regarima.html#cb221-13)#> AIC=338.1   AICc=338.5   BIC=357.8

The data are clearly already stationary (as we are considering percentage changes rather than raw expenditure and income), so there is no need for any differencing. The fitted model is \\[\begin{align*} y_t &= 0.595 + 0.198 x_t + \eta_t, \\\ \eta_t &= 0.707 \eta_{t-1} + \varepsilon_t -0.617 \varepsilon_{t-1} + 0.207 \varepsilon_{t-2},\\\ \varepsilon_t &\sim \text{NID}(0,0.311). \end{align*}\\]

We can recover estimates of both the \\(\eta_t\\) and \\(\varepsilon_t\\) series using the `residuals()` function.
    
    
    [](regarima.html#cb222-1)bind_rows(
    [](regarima.html#cb222-2)    `Regression residuals` =
    [](regarima.html#cb222-3)        as_tibble(residuals(fit, type = "regression")),
    [](regarima.html#cb222-4)    `ARIMA residuals` =
    [](regarima.html#cb222-5)        as_tibble(residuals(fit, type = "innovation")),
    [](regarima.html#cb222-6)    .id = "type"
    [](regarima.html#cb222-7)  ) |>
    [](regarima.html#cb222-8)  mutate(
    [](regarima.html#cb222-9)    type = factor(type, levels=c(
    [](regarima.html#cb222-10)      "Regression residuals", "ARIMA residuals"))
    [](regarima.html#cb222-11)  ) |>
    [](regarima.html#cb222-12)  ggplot(aes(x = Quarter, y = .resid)) +
    [](regarima.html#cb222-13)  geom_line() +
    [](regarima.html#cb222-14)  facet_grid(vars(type))

Figure 10.2: Regression residuals (\\(\eta_t\\)) and ARIMA residuals (\\(\varepsilon_t\\)) from the fitted model. 

It is the ARIMA estimated errors (the innovation residuals) that should resemble a white noise series.
    
    
    [](regarima.html#cb223-1)fit |> gg_tsresiduals()

Figure 10.3: The innovation residuals (i.e., the estimated ARIMA errors) are not significantly different from white noise. 
    
    
    [](regarima.html#cb224-1)augment(fit) |>
    [](regarima.html#cb224-2)  features(.innov, ljung_box, dof = 3, lag = 8)
    [](regarima.html#cb224-3)#> # A tibble: 1 × 3
    [](regarima.html#cb224-4)#>   .model                      lb_stat lb_pvalue
    [](regarima.html#cb224-5)#>   <chr>                         <dbl>     <dbl>
    [](regarima.html#cb224-6)#> 1 ARIMA(Consumption ~ Income)    5.21     0.391


---

## 10.3 Forecasting[](forecasting.html#forecasting)

To forecast using a regression model with ARIMA errors, we need to forecast the regression part of the model and the ARIMA part of the model, and combine the results. As with ordinary regression models, in order to obtain forecasts we first need to forecast the predictors. When the predictors are known into the future (e.g., calendar-related variables such as time, day-of-week, etc.), this is straightforward. But when the predictors are themselves unknown, we must either model them separately, or use assumed future values for each predictor.

### Example: US Personal Consumption and Income[](forecasting.html#example-us-personal-consumption-and-income-1)

We will calculate forecasts for the next eight quarters assuming that the future percentage changes in personal disposable income will be equal to the mean percentage change from the last forty years.
    
    
    [](forecasting.html#cb225-1)us_change_future <- new_data(us_change, 8) |>
    [](forecasting.html#cb225-2)  mutate(Income = mean(us_change$Income))
    [](forecasting.html#cb225-3)forecast(fit, new_data = us_change_future) |>
    [](forecasting.html#cb225-4)  autoplot(us_change) +
    [](forecasting.html#cb225-5)  labs(y = "Percentage change")

Figure 10.4: Forecasts obtained from regressing the percentage change in consumption expenditure on the percentage change in disposable income, with an ARIMA(1,0,2) error model. 

The prediction intervals for this model are narrower than if we had fitted an ARIMA model without covariates, because we are now able to explain some of the variation in the data using the income predictor.

It is important to realise that the prediction intervals from regression models (with or without ARIMA errors) do not take into account the uncertainty in the forecasts of the predictors. So they should be interpreted as being conditional on the assumed (or estimated) future values of the predictor variables.

### Example: Forecasting electricity demand[](forecasting.html#example-forecasting-electricity-demand)

Daily electricity demand can be modelled as a function of temperature. As can be observed on an electricity bill, more electricity is used on cold days due to heating and hot days due to air conditioning. The higher demand on cold and hot days is reflected in the U-shape of Figure [10.5](forecasting.html#fig:elecscatter), where daily demand is plotted versus daily maximum temperature.
    
    
    [](forecasting.html#cb226-1)vic_elec_daily <- vic_elec |>
    [](forecasting.html#cb226-2)  filter(year(Time) == 2014) |>
    [](forecasting.html#cb226-3)  index_by(Date = date(Time)) |>
    [](forecasting.html#cb226-4)  summarise(
    [](forecasting.html#cb226-5)    Demand = sum(Demand) / 1e3,
    [](forecasting.html#cb226-6)    Temperature = max(Temperature),
    [](forecasting.html#cb226-7)    Holiday = any(Holiday)
    [](forecasting.html#cb226-8)  ) |>
    [](forecasting.html#cb226-9)  mutate(Day_Type = case_when(
    [](forecasting.html#cb226-10)    Holiday ~ "Holiday",
    [](forecasting.html#cb226-11)    wday(Date) %in% 2:6 ~ "Weekday",
    [](forecasting.html#cb226-12)    TRUE ~ "Weekend"
    [](forecasting.html#cb226-13)  ))
    [](forecasting.html#cb226-14)
    [](forecasting.html#cb226-15)vic_elec_daily |>
    [](forecasting.html#cb226-16)  ggplot(aes(x = Temperature, y = Demand, colour = Day_Type)) +
    [](forecasting.html#cb226-17)  geom_point() +
    [](forecasting.html#cb226-18)  labs(y = "Electricity demand (GW)",
    [](forecasting.html#cb226-19)       x = "Maximum daily temperature")

Figure 10.5: Daily electricity demand versus maximum daily temperature for the state of Victoria in Australia for 2014. 

The data stored as `vic_elec_daily` includes total daily demand, daily maximum temperatures, and an indicator variable for if that day is a public holiday. Figure [10.6](forecasting.html#fig:electime) shows the time series of both daily demand and daily maximum temperatures. The plots highlight the need for both a non-linear and a dynamic model.
    
    
    [](forecasting.html#cb227-1)vic_elec_daily |>
    [](forecasting.html#cb227-2)  pivot_longer(c(Demand, Temperature)) |>
    [](forecasting.html#cb227-3)  ggplot(aes(x = Date, y = value)) +
    [](forecasting.html#cb227-4)  geom_line() +
    [](forecasting.html#cb227-5)  facet_grid(name ~ ., scales = "free_y") + ylab("")

Figure 10.6: Daily electricity demand and maximum daily temperature for the state of Victoria in Australia for 2014. 

In this example, we fit a quadratic regression model with ARMA errors using the `ARIMA()` function. The model also includes an indicator variable for if the day was a working day or not.
    
    
    [](forecasting.html#cb228-1)fit <- vic_elec_daily |>
    [](forecasting.html#cb228-2)  model(ARIMA(Demand ~ Temperature + I(Temperature^2) +
    [](forecasting.html#cb228-3)                (Day_Type == "Weekday")))
    [](forecasting.html#cb228-4)fit |> gg_tsresiduals()

Figure 10.7: Residuals diagnostics for a dynamic regression model for daily electricity demand with workday and quadratic temperature effects. 

The fitted model has an ARIMA(2,1,2)(2,0,0)[7] error, so there are 6 AR and MA coefficients.
    
    
    [](forecasting.html#cb229-1)augment(fit) |>
    [](forecasting.html#cb229-2)  features(.innov, ljung_box, dof = 6, lag = 14)
    [](forecasting.html#cb229-3)#> # A tibble: 1 × 3
    [](forecasting.html#cb229-4)#>   .model                                                     lb_stat lb_pvalue
    [](forecasting.html#cb229-5)#>   <chr>                                                        <dbl>     <dbl>
    [](forecasting.html#cb229-6)#> 1 "ARIMA(Demand ~ Temperature + I(Temperature^2) + (Day_Typ…    28.4  0.000404

There is clear heteroscedasticity in the residuals, with higher variance in January and February, and lower variance in May. The model also has some significant autocorrelation in the residuals, and the histogram of the residuals shows long tails. All of these issues with the residuals may affect the coverage of the prediction intervals, but the point forecasts should still be ok.

Using the estimated model we forecast 14 days ahead starting from Thursday 1 January 2015 (a non-work-day being a public holiday for New Years Day). In this case, we could obtain weather forecasts from the weather bureau for the next 14 days. But for the sake of illustration, we will use scenario based forecasting (as introduced in Section [7.6](forecasting-regression.html#forecasting-regression)) where we set the temperature for the next 14 days to a constant 26 degrees.
    
    
    [](forecasting.html#cb230-1)vic_elec_future <- new_data(vic_elec_daily, 14) |>
    [](forecasting.html#cb230-2)  mutate(
    [](forecasting.html#cb230-3)    Temperature = 26,
    [](forecasting.html#cb230-4)    Holiday = c(TRUE, rep(FALSE, 13)),
    [](forecasting.html#cb230-5)    Day_Type = case_when(
    [](forecasting.html#cb230-6)      Holiday ~ "Holiday",
    [](forecasting.html#cb230-7)      wday(Date) %in% 2:6 ~ "Weekday",
    [](forecasting.html#cb230-8)      TRUE ~ "Weekend"
    [](forecasting.html#cb230-9)    )
    [](forecasting.html#cb230-10)  )
    [](forecasting.html#cb230-11)forecast(fit, vic_elec_future) |>
    [](forecasting.html#cb230-12)  autoplot(vic_elec_daily) +
    [](forecasting.html#cb230-13)  labs(title="Daily electricity demand: Victoria",
    [](forecasting.html#cb230-14)       y="GW")

Figure 10.8: Forecasts from the dynamic regression model for daily electricity demand. All future temperatures have been set to 26 degrees, and the working day dummy variable has been set to known future values. 

The point forecasts look reasonable for the first two weeks of 2015. The slow down in electricity demand at the end of 2014 (due to many people taking summer vacations) has caused the forecasts for the next two weeks to show similarly low demand values.


---

## 10.4 Stochastic and deterministic trends[](stochastic-and-deterministic-trends.html#stochastic-and-deterministic-trends)

There are two different ways of modelling a linear trend. A _deterministic trend_ is obtained using the regression model \\[ y_t = \beta_0 + \beta_1 t + \eta_t, \\] where \\(\eta_t\\) is an ARMA process. A _stochastic trend_ is obtained using the model \\[ y_t = \beta_0 + \beta_1 t + \eta_t, \\] where \\(\eta_t\\) is an ARIMA process with \\(d=1\\). In the latter case, we can difference both sides so that \\(y_t' = \beta_1 + \eta_t'\\), where \\(\eta_t'\\) is an ARMA process. In other words, \\[ y_t = y_{t-1} + \beta_1 + \eta_t'. \\] This is similar to a random walk with drift (introduced in Section [9.1](stationarity.html#stationarity)), but here the error term is an ARMA process rather than simply white noise.

Although these models appear quite similar (they only differ in the number of differences that need to be applied to \\(\eta_t\\)), their forecasting characteristics are quite different.

### Example: Air transport passengers Australia[](stochastic-and-deterministic-trends.html#example-air-transport-passengers-australia)
    
    
    [](stochastic-and-deterministic-trends.html#cb231-1)aus_airpassengers |>
    [](stochastic-and-deterministic-trends.html#cb231-2)  autoplot(Passengers) +
    [](stochastic-and-deterministic-trends.html#cb231-3)  labs(y = "Passengers (millions)",
    [](stochastic-and-deterministic-trends.html#cb231-4)       title = "Total annual air passengers")

Figure 10.9: Total annual passengers (in millions) for Australian air carriers, 1970–2016. 

Figure [10.9](stochastic-and-deterministic-trends.html#fig:austa) shows the total number of passengers for Australian air carriers each year from 1970 to 2016. We will fit both a deterministic and a stochastic trend model to these data.

The deterministic trend model is obtained as follows:
    
    
    [](stochastic-and-deterministic-trends.html#cb232-1)fit_deterministic <- aus_airpassengers |>
    [](stochastic-and-deterministic-trends.html#cb232-2)  model(deterministic = ARIMA(Passengers ~ 1 + trend() +
    [](stochastic-and-deterministic-trends.html#cb232-3)                                pdq(d = 0)))
    [](stochastic-and-deterministic-trends.html#cb232-4)report(fit_deterministic)
    [](stochastic-and-deterministic-trends.html#cb232-5)#> Series: Passengers 
    [](stochastic-and-deterministic-trends.html#cb232-6)#> Model: LM w/ ARIMA(1,0,0) errors 
    [](stochastic-and-deterministic-trends.html#cb232-7)#> 
    [](stochastic-and-deterministic-trends.html#cb232-8)#> Coefficients:
    [](stochastic-and-deterministic-trends.html#cb232-9)#>          ar1  trend()  intercept
    [](stochastic-and-deterministic-trends.html#cb232-10)#>       0.9564   1.4151     0.9014
    [](stochastic-and-deterministic-trends.html#cb232-11)#> s.e.  0.0362   0.1972     7.0751
    [](stochastic-and-deterministic-trends.html#cb232-12)#> 
    [](stochastic-and-deterministic-trends.html#cb232-13)#> sigma^2 estimated as 4.343:  log likelihood=-100.88
    [](stochastic-and-deterministic-trends.html#cb232-14)#> AIC=209.77   AICc=210.72   BIC=217.17

This model can be written as \\[\begin{align*} y_t &= 0.901 + 1.415 t + \eta_t \\\ \eta_t &= 0.956 \eta_{t-1} + \varepsilon_t\\\ \varepsilon_t &\sim \text{NID}(0,4.343). \end{align*}\\]

The estimated growth in visitor numbers is 1.42 million people per year.

Alternatively, the stochastic trend model can be estimated.
    
    
    [](stochastic-and-deterministic-trends.html#cb233-1)fit_stochastic <- aus_airpassengers |>
    [](stochastic-and-deterministic-trends.html#cb233-2)  model(stochastic = ARIMA(Passengers ~ pdq(d = 1)))
    [](stochastic-and-deterministic-trends.html#cb233-3)report(fit_stochastic)
    [](stochastic-and-deterministic-trends.html#cb233-4)#> Series: Passengers 
    [](stochastic-and-deterministic-trends.html#cb233-5)#> Model: ARIMA(0,1,0) w/ drift 
    [](stochastic-and-deterministic-trends.html#cb233-6)#> 
    [](stochastic-and-deterministic-trends.html#cb233-7)#> Coefficients:
    [](stochastic-and-deterministic-trends.html#cb233-8)#>       constant
    [](stochastic-and-deterministic-trends.html#cb233-9)#>         1.4191
    [](stochastic-and-deterministic-trends.html#cb233-10)#> s.e.    0.3014
    [](stochastic-and-deterministic-trends.html#cb233-11)#> 
    [](stochastic-and-deterministic-trends.html#cb233-12)#> sigma^2 estimated as 4.271:  log likelihood=-98.16
    [](stochastic-and-deterministic-trends.html#cb233-13)#> AIC=200.31   AICc=200.59   BIC=203.97

This model can be written as \\(y_t-y_{t-1} = 1.419 + \varepsilon_t\\), or equivalently \\[\begin{align*} y_t &= y_0 + 1.419 t + \eta_t \\\ \eta_t &= \eta_{t-1} + \varepsilon_{t}\\\ \varepsilon_t &\sim \text{NID}(0,4.271). \end{align*}\\]

In this case, the estimated growth in visitor numbers is also 1.42 million people per year. Although the growth estimates are similar, the prediction intervals are not, as Figure [10.10](stochastic-and-deterministic-trends.html#fig:austaf) shows. In particular, stochastic trends have much wider prediction intervals because the errors are non-stationary.
    
    
    [](stochastic-and-deterministic-trends.html#cb234-1)aus_airpassengers |>
    [](stochastic-and-deterministic-trends.html#cb234-2)  autoplot(Passengers) +
    [](stochastic-and-deterministic-trends.html#cb234-3)  autolayer(fit_stochastic |> forecast(h = 20),
    [](stochastic-and-deterministic-trends.html#cb234-4)    colour = "#0072B2", level = 95) +
    [](stochastic-and-deterministic-trends.html#cb234-5)  autolayer(fit_deterministic |> forecast(h = 20),
    [](stochastic-and-deterministic-trends.html#cb234-6)    colour = "#D55E00", alpha = 0.65, level = 95) +
    [](stochastic-and-deterministic-trends.html#cb234-7)  labs(y = "Air passengers (millions)",
    [](stochastic-and-deterministic-trends.html#cb234-8)       title = "Forecasts from trend models")

Figure 10.10: Forecasts of annual passengers for Australian air carriers using a deterministic trend model (orange) and a stochastic trend model (blue). 

There is an implicit assumption with deterministic trends that the slope of the trend is not going to change over time. On the other hand, stochastic trends can change, and the estimated growth is only assumed to be the average growth over the historical period, not necessarily the rate of growth that will be observed into the future. Consequently, it is safer to forecast with stochastic trends, especially for longer forecast horizons, as the prediction intervals allow for greater uncertainty in future growth.


---

## 10.5 Dynamic harmonic regression[](dhr.html#dhr)

When there are long seasonal periods, a dynamic regression with Fourier terms is often better than other models we have considered in this book.[22](dhr.html#fn22)

For example, daily data can have annual seasonality of length 365, weekly data has seasonal period of approximately 52, while half-hourly data can have several seasonal periods, the shortest of which is the daily pattern of period 48.

Seasonal versions of ARIMA and ETS models are designed for shorter periods such as 12 for monthly data or 4 for quarterly data. The `ETS()` model restricts seasonality to be a maximum period of 24 to allow hourly data but not data with a larger seasonal period. The problem is that there are \\(m-1\\) parameters to be estimated for the initial seasonal states where \\(m\\) is the seasonal period. So for large \\(m\\), the estimation becomes almost impossible.

The `ARIMA()` function will allow a seasonal period up to \\(m=350\\), but in practice will usually run out of memory whenever the seasonal period is more than about 200. In any case, seasonal differencing of high order does not make a lot of sense — for daily data it involves comparing what happened today with what happened exactly a year ago and there is no constraint that the seasonal pattern is smooth.

So for such time series, we prefer a harmonic regression approach where the seasonal pattern is modelled using Fourier terms with short-term time series dynamics handled by an ARMA error.

The advantages of this approach are:

  * it allows any length seasonality;
  * for data with more than one seasonal period, Fourier terms of different frequencies can be included;
  * the smoothness of the seasonal pattern can be controlled by \\(K\\), the number of Fourier sin and cos pairs – the seasonal pattern is smoother for smaller values of \\(K\\);
  * the short-term dynamics are easily handled with a simple ARMA error.


The only real disadvantage (compared to a seasonal ARIMA model) is that the seasonality is assumed to be fixed — the seasonal pattern is not allowed to change over time. But in practice, seasonality is usually remarkably constant so this is not a big disadvantage except for long time series.

### Example: Australian eating out expenditure[](dhr.html#example-australian-eating-out-expenditure)

In this example we demonstrate combining Fourier terms for capturing seasonality with ARIMA errors capturing other dynamics in the data. For simplicity, we will use an example with monthly data. The same modelling approach using weekly data is discussed in Section [13.1](weekly.html#weekly).

We use the total monthly expenditure on cafes, restaurants and takeaway food services in Australia ($billion) from 2004 up to 2018 and forecast 24 months ahead. We vary \\(K\\), the number of Fourier sin and cos pairs, from \\(K=1\\) to \\(K=6\\) (which is equivalent to including seasonal dummies). Figure [10.11](dhr.html#fig:eatout) shows the seasonal pattern projected forward as \\(K\\) increases. Notice that as \\(K\\) increases the Fourier terms capture and project a more “wiggly” seasonal pattern and simpler ARIMA models are required to capture other dynamics. The AICc value is minimised for \\(K=6\\), with a significant jump going from \\(K=4\\) to \\(K=5\\), hence the forecasts generated from this model would be the ones used.
    
    
    [](dhr.html#cb235-1)aus_cafe <- aus_retail |>
    [](dhr.html#cb235-2)  filter(
    [](dhr.html#cb235-3)    Industry == "Cafes, restaurants and takeaway food services",
    [](dhr.html#cb235-4)    year(Month) %in% 2004:2018
    [](dhr.html#cb235-5)  ) |>
    [](dhr.html#cb235-6)  summarise(Turnover = sum(Turnover))
    [](dhr.html#cb235-7)
    [](dhr.html#cb235-8)fit <- model(aus_cafe,
    [](dhr.html#cb235-9)  `K = 1` = ARIMA(log(Turnover) ~ fourier(K=1) + PDQ(0,0,0)),
    [](dhr.html#cb235-10)  `K = 2` = ARIMA(log(Turnover) ~ fourier(K=2) + PDQ(0,0,0)),
    [](dhr.html#cb235-11)  `K = 3` = ARIMA(log(Turnover) ~ fourier(K=3) + PDQ(0,0,0)),
    [](dhr.html#cb235-12)  `K = 4` = ARIMA(log(Turnover) ~ fourier(K=4) + PDQ(0,0,0)),
    [](dhr.html#cb235-13)  `K = 5` = ARIMA(log(Turnover) ~ fourier(K=5) + PDQ(0,0,0)),
    [](dhr.html#cb235-14)  `K = 6` = ARIMA(log(Turnover) ~ fourier(K=6) + PDQ(0,0,0))
    [](dhr.html#cb235-15))
    [](dhr.html#cb235-16)
    [](dhr.html#cb235-17)fit |>
    [](dhr.html#cb235-18)  forecast(h = "2 years") |>
    [](dhr.html#cb235-19)  autoplot(aus_cafe, level = 95) +
    [](dhr.html#cb235-20)  facet_wrap(vars(.model), ncol = 2) +
    [](dhr.html#cb235-21)  guides(colour = "none", fill = "none", level = "none") +
    [](dhr.html#cb235-22)  geom_label(
    [](dhr.html#cb235-23)    aes(x = yearmonth("2007 Jan"), y = 4250,
    [](dhr.html#cb235-24)        label = paste0("AICc = ", format(AICc))),
    [](dhr.html#cb235-25)    data = glance(fit)
    [](dhr.html#cb235-26)  ) +
    [](dhr.html#cb235-27)  labs(title= "Total monthly eating-out expenditure",
    [](dhr.html#cb235-28)       y="$ billions")

Figure 10.11: Using Fourier terms and ARIMA errors for forecasting monthly expenditure on eating out in Australia. 

### Bibliography[](bibliography.html#bibliography)

Young, P. C., Pedregal, D. J., & Tych, W. (1999). Dynamic harmonic regression. _Journal of Forecasting_ , _18_ , 369–394. [__](https://doi.org/10.1002/\(SICI\)1099-131X\(199911\)18:6%3C369::AID-FOR748%3E3.0.CO;2-K)

* * *

  22. The term “dynamic harmonic regression” is also used for a harmonic regression with time-varying parameters ([Young et al., 1999](dhr.html#ref-DHR99)).[↩︎](dhr.html#fnref22)




---

## 10.6 Lagged predictors[](lagged-predictors.html#lagged-predictors)

Sometimes, the impact of a predictor that is included in a regression model will not be simple and immediate. For example, an advertising campaign may impact sales for some time beyond the end of the campaign, and sales in one month will depend on the advertising expenditure in each of the past few months. Similarly, a change in a company’s safety policy may reduce accidents immediately, but have a diminishing effect over time as employees take less care when they become familiar with the new working conditions.

In these situations, we need to allow for lagged effects of the predictor. Suppose that we have only one predictor in our model. Then a model which allows for lagged effects can be written as \\[ y_t = \beta_0 + \gamma_0x_t + \gamma_1 x_{t-1} + \dots + \gamma_k x_{t-k} + \eta_t, \\] where \\(\eta_t\\) is an ARIMA process. The value of \\(k\\) can be selected using the AICc, along with the values of \\(p\\) and \\(q\\) for the ARIMA error.

### Example: TV advertising and insurance quotations[](lagged-predictors.html#example-tv-advertising-and-insurance-quotations)

A US insurance company advertises on national television in an attempt to increase the number of insurance quotations provided (and consequently the number of new policies). Figure [10.12](lagged-predictors.html#fig:tvadvert) shows the number of quotations and the expenditure on television advertising for the company each month from January 2002 to April 2005.
    
    
    [](lagged-predictors.html#cb236-1)insurance |>
    [](lagged-predictors.html#cb236-2)  pivot_longer(Quotes:TVadverts) |>
    [](lagged-predictors.html#cb236-3)  ggplot(aes(x = Month, y = value)) +
    [](lagged-predictors.html#cb236-4)  geom_line() +
    [](lagged-predictors.html#cb236-5)  facet_grid(vars(name), scales = "free_y") +
    [](lagged-predictors.html#cb236-6)  labs(y = "", title = "Insurance advertising and quotations")

Figure 10.12: Numbers of insurance quotations provided per month and the expenditure on advertising per month. 

We will consider including advertising expenditure for up to four months; that is, the model may include advertising expenditure in the current month, and the three months before that. When comparing models, it is important that they all use the same training set. In the following code, we exclude the first three months in order to make fair comparisons.
    
    
    [](lagged-predictors.html#cb237-1)fit <- insurance |>
    [](lagged-predictors.html#cb237-2)  # Restrict data so models use same fitting period
    [](lagged-predictors.html#cb237-3)  mutate(Quotes = c(NA, NA, NA, Quotes[4:40])) |>
    [](lagged-predictors.html#cb237-4)  # Estimate models
    [](lagged-predictors.html#cb237-5)  model(
    [](lagged-predictors.html#cb237-6)    lag0 = ARIMA(Quotes ~ pdq(d = 0) + TVadverts),
    [](lagged-predictors.html#cb237-7)    lag1 = ARIMA(Quotes ~ pdq(d = 0) +
    [](lagged-predictors.html#cb237-8)                 TVadverts + lag(TVadverts)),
    [](lagged-predictors.html#cb237-9)    lag2 = ARIMA(Quotes ~ pdq(d = 0) +
    [](lagged-predictors.html#cb237-10)                 TVadverts + lag(TVadverts) +
    [](lagged-predictors.html#cb237-11)                 lag(TVadverts, 2)),
    [](lagged-predictors.html#cb237-12)    lag3 = ARIMA(Quotes ~ pdq(d = 0) +
    [](lagged-predictors.html#cb237-13)                 TVadverts + lag(TVadverts) +
    [](lagged-predictors.html#cb237-14)                 lag(TVadverts, 2) + lag(TVadverts, 3))
    [](lagged-predictors.html#cb237-15)  )

Next we choose the optimal lag length for advertising based on the AICc.
    
    
    [](lagged-predictors.html#cb238-1)glance(fit)
    [](lagged-predictors.html#cb238-2)#> # A tibble: 4 × 8
    [](lagged-predictors.html#cb238-3)#>   .model sigma2 log_lik   AIC  AICc   BIC ar_roots  ma_roots 
    [](lagged-predictors.html#cb238-4)#>   <chr>   <dbl>   <dbl> <dbl> <dbl> <dbl> <list>    <list>   
    [](lagged-predictors.html#cb238-5)#> 1 lag0    0.265   -28.3  66.6  68.3  75.0 <cpl [2]> <cpl [0]>
    [](lagged-predictors.html#cb238-6)#> 2 lag1    0.209   -24.0  58.1  59.9  66.5 <cpl [1]> <cpl [1]>
    [](lagged-predictors.html#cb238-7)#> 3 lag2    0.215   -24.0  60.0  62.6  70.2 <cpl [1]> <cpl [1]>
    [](lagged-predictors.html#cb238-8)#> 4 lag3    0.206   -22.2  60.3  65.0  73.8 <cpl [1]> <cpl [1]>

The best model (with the smallest AICc value) is `lag1` with two predictors; that is, it includes advertising only in the current month and the previous month. So we now re-estimate that model, but using all the available data.
    
    
    [](lagged-predictors.html#cb239-1)fit_best <- insurance |>
    [](lagged-predictors.html#cb239-2)  model(ARIMA(Quotes ~ pdq(d = 0) +
    [](lagged-predictors.html#cb239-3)              TVadverts + lag(TVadverts)))
    [](lagged-predictors.html#cb239-4)report(fit_best)
    [](lagged-predictors.html#cb239-5)#> Series: Quotes 
    [](lagged-predictors.html#cb239-6)#> Model: LM w/ ARIMA(1,0,2) errors 
    [](lagged-predictors.html#cb239-7)#> 
    [](lagged-predictors.html#cb239-8)#> Coefficients:
    [](lagged-predictors.html#cb239-9)#>          ar1     ma1     ma2  TVadverts  lag(TVadverts)  intercept
    [](lagged-predictors.html#cb239-10)#>       0.5123  0.9169  0.4591     1.2527          0.1464     2.1554
    [](lagged-predictors.html#cb239-11)#> s.e.  0.1849  0.2051  0.1895     0.0588          0.0531     0.8595
    [](lagged-predictors.html#cb239-12)#> 
    [](lagged-predictors.html#cb239-13)#> sigma^2 estimated as 0.2166:  log likelihood=-23.94
    [](lagged-predictors.html#cb239-14)#> AIC=61.88   AICc=65.38   BIC=73.7

The chosen model has ARIMA(1,0,2) errors. The model can be written as \\[ y_t = 2.155 + 1.253 x_t + 0.146 x_{t-1} + \eta_t, \\] where \\(y_t\\) is the number of quotations provided in month \\(t\\), \\(x_t\\) is the advertising expenditure in month \\(t\\), \\[ \eta_t = 0.512 \eta_{t-1} + \varepsilon_t + 0.917 \varepsilon_{t-1} + 0.459 \varepsilon_{t-2}, \\] and \\(\varepsilon_t\\) is white noise.

We can calculate forecasts using this model if we assume future values for the advertising variable. If we set the future monthly advertising to 8 units, we get the forecasts in Figure [10.13](lagged-predictors.html#fig:tvadvertf8).
    
    
    [](lagged-predictors.html#cb240-1)insurance_future <- new_data(insurance, 20) |>
    [](lagged-predictors.html#cb240-2)  mutate(TVadverts = 8)
    [](lagged-predictors.html#cb240-3)fit_best |>
    [](lagged-predictors.html#cb240-4)  forecast(insurance_future) |>
    [](lagged-predictors.html#cb240-5)  autoplot(insurance) +
    [](lagged-predictors.html#cb240-6)  labs(
    [](lagged-predictors.html#cb240-7)    y = "Quotes",
    [](lagged-predictors.html#cb240-8)    title = "Forecast quotes with future advertising set to 8"
    [](lagged-predictors.html#cb240-9)  )

Figure 10.13: Forecasts of monthly insurance quotes, assuming that the future advertising expenditure is 8 units in each future month. 


---

## 10.7 Exercises[](dynamic-exercises.html#dynamic-exercises)

  1. This exercise uses data set `LakeHuron` giving the level of Lake Huron from 1875–1972.

     1. Convert the data to a tsibble object using the `as_tsibble()` function.
     2. Fit a piecewise linear trend model to the Lake Huron data with a knot at 1920 and an ARMA error structure.
     3. Forecast the level for the next 30 years. Do you think the extrapolated linear trend is realistic?
  2. Repeat Exercise 4 from Section [7.10](regression-exercises.html#regression-exercises), but this time adding in ARIMA errors to address the autocorrelations in the residuals.

     1. How much difference does the ARIMA error process make to the regression coefficients?
     2. How much difference does the ARIMA error process make to the forecasts?
     3. Check the residuals of the fitted model to ensure the ARIMA process has adequately addressed the autocorrelations seen in the `TSLM` model.
  3. Repeat the daily electricity example, but instead of using a quadratic function of temperature, use a piecewise linear function with the “knot” around 25 degrees Celsius (use predictors `Temperature` & `Temp2`). How can you optimise the choice of knot?

The data can be created as follows.
         
         [](dynamic-exercises.html#cb241-1)vic_elec_daily <- vic_elec |>
         [](dynamic-exercises.html#cb241-2)  filter(year(Time) == 2014) |>
         [](dynamic-exercises.html#cb241-3)  index_by(Date = date(Time)) |>
         [](dynamic-exercises.html#cb241-4)  summarise(
         [](dynamic-exercises.html#cb241-5)    Demand = sum(Demand)/1e3,
         [](dynamic-exercises.html#cb241-6)    Temperature = max(Temperature),
         [](dynamic-exercises.html#cb241-7)    Holiday = any(Holiday)) |>
         [](dynamic-exercises.html#cb241-8)  mutate(
         [](dynamic-exercises.html#cb241-9)    Temp2 = I(pmax(Temperature-25,0)),
         [](dynamic-exercises.html#cb241-10)    Day_Type = case_when(
         [](dynamic-exercises.html#cb241-11)      Holiday ~ "Holiday",
         [](dynamic-exercises.html#cb241-12)      wday(Date) %in% 2:6 ~ "Weekday",
         [](dynamic-exercises.html#cb241-13)      TRUE ~ "Weekend"))

  4. This exercise concerns `aus_accommodation`: the total quarterly takings from accommodation and the room occupancy level for hotels, motels, and guest houses in Australia, between January 1998 and June 2016. Total quarterly takings are in millions of Australian dollars.

     1. Compute the CPI-adjusted takings and plot the result for each state
     2. For each state, fit a dynamic regression model of CPI-adjusted takings with seasonal dummy variables, a piecewise linear time trend with one knot at 2008 Q1, and ARIMA errors.
     3. Check that the residuals of the model look like white noise.
     4. Forecast the takings for each state to the end of 2017. (Hint: You will need to produce forecasts of the CPI first.)
     5. What sources of uncertainty have not been taken into account in the prediction intervals?
  5. We fitted a harmonic regression model to part of the `us_gasoline` series in Exercise 5 in Section [7.10](regression-exercises.html#regression-exercises). We will now revisit this model, and extend it to include more data and ARMA errors.

     1. Using `TSLM()`, fit a harmonic regression with a piecewise linear time trend to the full series. Select the position of the knots in the trend and the appropriate number of Fourier terms to include by minimising the AICc or CV value.
     2. Now refit the model using `ARIMA()` to allow for correlated errors, keeping the same predictor variables as you used with `TSLM()`.
     3. Check the residuals of the final model using the `gg_tsresiduals()` function and a Ljung-Box test. Do they look sufficiently like white noise to continue? If not, try modifying your model, or removing the first few years of data.
     4. Once you have a model with white noise residuals, produce forecasts for the next year.
  6. Electricity consumption is often modelled as a function of temperature. Temperature is measured by daily heating degrees and cooling degrees. Heating degrees is \\(18^\circ\\)C minus the average daily temperature when the daily average is below \\(18^\circ\\)C; otherwise it is zero. This provides a measure of our need to heat ourselves as temperature falls. Cooling degrees measures our need to cool ourselves as the temperature rises. It is defined as the average daily temperature minus \\(18^\circ\\)C when the daily average is above \\(18^\circ\\)C; otherwise it is zero. Let \\(y_t\\) denote the monthly total of kilowatt-hours of electricity used, let \\(x_{1,t}\\) denote the monthly total of heating degrees, and let \\(x_{2,t}\\) denote the monthly total of cooling degrees.

An analyst fits the following model to a set of such data: \\[y^*_t = \beta_1x^*_{1,t} + \beta_2x^*_{2,t} + \eta_t,\\] where \\[(1-\Phi_{1}B^{12} - \Phi_{2}B^{24})(1-B)(1-B^{12})\eta_t = (1+\theta_1 B)\varepsilon_t\\] and \\(y^*_t = \log(y_t)\\), \\(x^*_{1,t} = \sqrt{x_{1,t}}\\) and \\(x^*_{2,t}=\sqrt{x_{2,t}}\\).

     1. What sort of ARIMA model is identified for \\(\eta_t\\)?

     2. The estimated coefficients are

Parameter | Estimate | s.e. | \\(Z\\) | \\(P\\)-value  
---|---|---|---|---  
\\(\beta_1\\) | 0.0077 | 0.0015 | 4.98 | 0.000  
\\(\beta_2\\) | 0.0208 | 0.0023 | 9.23 | 0.000  
\\(\theta_1\\) | -0.5830 | 0.0720 | 8.10 | 0.000  
\\(\Phi_{1}\\) | -0.5373 | 0.0856 | -6.27 | 0.000  
\\(\Phi_{2}\\) | -0.4667 | 0.0862 | -5.41 | 0.000  
  
Explain what the estimates of \\(\beta_1\\) and \\(\beta_2\\) tell us about electricity consumption.

     3. Write the equation in a form more suitable for forecasting.
     4. Describe how this model could be used to forecast electricity demand for the next 12 months.
     5. Explain why the \\(\eta_t\\) term should be modelled with an ARIMA model rather than modelling the data using a standard regression package. In your discussion, comment on the properties of the estimates, the validity of the standard regression results, and the importance of the \\(\eta_t\\) model in producing forecasts.
  7. For the retail time series considered in earlier chapters:

     1. Develop an appropriate dynamic regression model with Fourier terms for the seasonality. Use the AICc to select the number of Fourier terms to include in the model. (You will probably need to use the same Box-Cox transformation you identified previously.)
     2. Check the residuals of the fitted model. Does the residual series look like white noise?
     3. Compare the forecasts with those you obtained earlier using alternative models.




---

## 10.8 Further reading[](dynamic-reading.html#dynamic-reading)

  * A detailed discussion of dynamic regression models is provided in Pankratz ([1991](dynamic-reading.html#ref-Pankratz91)).
  * A generalisation of dynamic regression models, known as “transfer function models”, is discussed in Box et al. ([2015](dynamic-reading.html#ref-BJRL15)).


### Bibliography[](bibliography.html#bibliography)

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). _Time series analysis: Forecasting and control_ (5th ed). John Wiley & Sons. [__](http://amazon.com/dp/1118675029?tag=otexts20)

Pankratz, A. E. (1991). _Forecasting with dynamic regression models_. John Wiley & Sons. [__](http://amazon.com/dp/0471615285?tag=otexts20)


---

# Chapter 11 Forecasting hierarchical and grouped time series[](hierarchical.html#hierarchical)

Time series can often be naturally disaggregated by various attributes of interest. For example, the total number of bicycles sold by a cycling manufacturer can be disaggregated by product type such as road bikes, mountain bikes and hybrids. Each of these can be disaggregated into finer categories. For example hybrid bikes can be divided into city, commuting, comfort, and trekking bikes; and so on. These categories are nested within the larger group categories, and so the collection of time series follows a hierarchical aggregation structure. Therefore we refer to these as “hierarchical time series”.

Hierarchical time series often arise due to geographic divisions. For example, the total bicycle sales can be disaggregated by country, then within each country by state, within each state by region, and so on down to the outlet level.

Alternative aggregation structures arise when attributes of interest are crossed rather than nested. For example, the bicycle manufacturer may be interested in attributes such as frame size, gender, price range, etc. Such attributes do not naturally disaggregate in a unique hierarchical manner as the attributes are not nested. We refer to the resulting time series of crossed attributes as “grouped time series”.

More complex structures arise when attributes of interest are both nested and crossed. For example, it would be natural for the bicycle manufacturer to be interested in sales by product type and also by geographic division. Then both the product groupings and the geographic hierarchy are mixed together. We introduce alternative aggregation structures in Section [11.1](hts.html#hts).

Forecasts are often required for all disaggregate and aggregate series, and it is natural to want the forecasts to add up in the same way as the data. For example, forecasts of regional sales should add up to forecasts of state sales, which should in turn add up to give a forecast for national sales.

In this chapter we discuss forecasting large collections of time series that aggregate in some way. The challenge is that we require forecasts that are **coherent** across the entire aggregation structure. That is, we require forecasts to add up in a manner that is consistent with the aggregation structure of the hierarchy or group that defines the collection of time series.


---

## 11.1 Hierarchical and grouped time series[](hts.html#hts)

### Hierarchical time series[](hts.html#hierarchical-time-series)

Figure [11.1](hts.html#fig:HierTree) shows a simple hierarchical structure. At the top of the hierarchy is the “Total”, the most aggregate level of the data. The \\(t\\)th observation of the Total series is denoted by \\(y_t\\) for \\(t=1,\dots,T\\). The Total is disaggregated into two series, which in turn are divided into three and two series respectively at the bottom level of the hierarchy. Below the top level, we use \\(y_{j,t}\\) to denote the \\(t\\)th observation of the series corresponding to node \\(j\\). For example, \\(\y{A}{t}\\) denotes the \\(t\\)th observation of the series corresponding to node A, \\(\y{AB}{t}\\) denotes the \\(t\\)th observation of the series corresponding to node AB, and so on.

Figure 11.1: A two level hierarchical tree diagram. 

In this small example, the total number of series in the hierarchy is \\(n=1+2+5=8\\), while the number of series at the bottom level is \\(m=5\\). Note that \\(n>m\\) in all hierarchies.

For any time \\(t\\), the observations at the bottom level of the hierarchy will sum to the observations of the series above. For example, \\[\begin{equation} y_{t}=\y{AA}{t}+\y{AB}{t}+\y{AC}{t}+\y{BA}{t}+\y{BB}{t}, \tag{11.1} \end{equation}\\] \\[\begin{equation} \y{A}{t}=\y{AA}{t}+\y{AB}{t}+\y{AC}{t}\qquad \text{and} \qquad \y{B}{t}=\y{BA}{t}+\y{BB}{t}. \tag{11.2} \end{equation}\\] Substituting [(11.2)](hts.html#eq:middlelevel) into [(11.1)](hts.html#eq:toplevel), we also get \\(y_{t}=\y{A}{t}+\y{B}{t}\\).

### Example: Australian tourism hierarchy[](hts.html#example-australian-tourism-hierarchy)

Australia is divided into six states and two territories, with each one having its own government and some economic and administrative autonomy. For simplicity, we refer to both states and territories as “states”. Each of these states can be further subdivided into regions as shown in Figure [11.2](hts.html#fig:ausmap) and Table [11.1](hts.html#tab:aus-states-tab). In total there are 76 such regions. Business planners and tourism authorities are interested in forecasts for the whole of Australia, for each of the states and territories, and also for the regions.

Figure 11.2: Australian states and tourism regions. 

Table 11.1: Australian tourism regions.  State  |  Region   
---|---  
Australian Capital Territory  |  Canberra   
New South Wales  |  Blue Mountains, Capital Country, Central Coast, Central NSW, Hunter, New England North West, North Coast NSW, Outback NSW, Riverina, Snowy Mountains, South Coast, Sydney, The Murray.   
Northern Territory  |  Alice Springs, Barkly, Darwin, Kakadu Arnhem, Katherine Daly, Lasseter, MacDonnell.   
Queensland  |  Brisbane, Bundaberg, Central Queensland, Darling Downs, Fraser Coast, Gold Coast, Mackay, Northern Outback, Sunshine Coast, Tropical North Queensland, Whitsundays.   
South Australia  |  Adelaide, Adelaide Hills, Barossa, Clare Valley, Eyre Peninsula, Fleurieu Peninsula, Flinders Ranges and Outback, Kangaroo Island, Limestone Coast, Murraylands, Riverland, Yorke Peninsula.   
Tasmania  |  East Coast, Hobart and the South, Launceston Tamar and the North, North West, Wilderness West.   
Victoria  |  Ballarat, Bendigo Loddon, Central Highlands, Central Murray, Geelong and the Bellarine, Gippsland, Goulburn, Great Ocean Road, High Country, Lakes, Macedon, Mallee, Melbourne, Melbourne East, Murray East, Peninsula, Phillip Island, Spa Country, Upper Yarra, Western Grampians, Wimmera.   
Western Australia  |  Australia’s Coral Coast, Australia’s Golden Outback, Australia’s North West, Australia’s South West, Experience Perth.   
  
The `tourism` tsibble contains data on quarterly domestic tourism demand, measured as the number of overnight trips Australians spend away from home. The key variables `State` and `Region` denote the geographical areas, while a further key `Purpose` describes the purpose of travel. For now, we will ignore the purpose of travel and just consider the geographic hierarchy. To make the graphs and tables simpler, we will recode `State` to use abbreviations.
    
    
    [](hts.html#cb242-1)tourism <- tsibble::tourism |>
    [](hts.html#cb242-2)  mutate(State = recode(State,
    [](hts.html#cb242-3)    `New South Wales` = "NSW",
    [](hts.html#cb242-4)    `Northern Territory` = "NT",
    [](hts.html#cb242-5)    `Queensland` = "QLD",
    [](hts.html#cb242-6)    `South Australia` = "SA",
    [](hts.html#cb242-7)    `Tasmania` = "TAS",
    [](hts.html#cb242-8)    `Victoria` = "VIC",
    [](hts.html#cb242-9)    `Western Australia` = "WA"
    [](hts.html#cb242-10)  ))

Using the `aggregate_key()` function, we can create the hierarchical time series with overnight trips in regions at the bottom level of the hierarchy, aggregated to states, which are aggregated to the national total. A hierarchical time series corresponding to the nested structure is created using a `parent/child` specification.
    
    
    [](hts.html#cb243-1)tourism_hts <- tourism |>
    [](hts.html#cb243-2)  aggregate_key(State / Region, Trips = sum(Trips))
    [](hts.html#cb243-3)tourism_hts
    [](hts.html#cb243-4)#> # A tsibble: 6,800 x 4 [1Q]
    [](hts.html#cb243-5)#> # Key:       State, Region [85]
    [](hts.html#cb243-6)#>    Quarter State        Region        Trips
    [](hts.html#cb243-7)#>      <qtr> <chr*>       <chr*>        <dbl>
    [](hts.html#cb243-8)#>  1 1998 Q1 <aggregated> <aggregated> 23182.
    [](hts.html#cb243-9)#>  2 1998 Q2 <aggregated> <aggregated> 20323.
    [](hts.html#cb243-10)#>  3 1998 Q3 <aggregated> <aggregated> 19827.
    [](hts.html#cb243-11)#>  4 1998 Q4 <aggregated> <aggregated> 20830.
    [](hts.html#cb243-12)#>  5 1999 Q1 <aggregated> <aggregated> 22087.
    [](hts.html#cb243-13)#>  6 1999 Q2 <aggregated> <aggregated> 21458.
    [](hts.html#cb243-14)#>  7 1999 Q3 <aggregated> <aggregated> 19914.
    [](hts.html#cb243-15)#>  8 1999 Q4 <aggregated> <aggregated> 20028.
    [](hts.html#cb243-16)#>  9 2000 Q1 <aggregated> <aggregated> 22339.
    [](hts.html#cb243-17)#> 10 2000 Q2 <aggregated> <aggregated> 19941.
    [](hts.html#cb243-18)#> # ℹ 6,790 more rows

The new `tsibble` now has some additional rows corresponding to state and national aggregations for each quarter. Figure [11.3](hts.html#fig:tourismStates) shows the aggregate total overnight trips for the whole of Australia as well as the states, revealing diverse and rich dynamics. For example, there is noticeable national growth since 2010 and for some states such as the ACT, New South Wales, Queensland, South Australia, and Victoria. There seems to be a significant jump for Western Australia in 2014.
    
    
    [](hts.html#cb244-1)tourism_hts |>
    [](hts.html#cb244-2)  filter(is_aggregated(Region)) |>
    [](hts.html#cb244-3)  autoplot(Trips) +
    [](hts.html#cb244-4)  labs(y = "Trips ('000)",
    [](hts.html#cb244-5)       title = "Australian tourism: national and states") +
    [](hts.html#cb244-6)  facet_wrap(vars(State), scales = "free_y", ncol = 3) +
    [](hts.html#cb244-7)  theme(legend.position = "none")

Figure 11.3: Domestic overnight trips from 1998 Q1 to 2017 Q4 aggregated by state. 
    
    
    [](hts.html#cb245-1)tourism_hts |>
    [](hts.html#cb245-2)  filter(State == "NT" | State == "QLD" |
    [](hts.html#cb245-3)         State == "TAS" | State == "VIC", is_aggregated(Region)) |>
    [](hts.html#cb245-4)  select(-Region) |>
    [](hts.html#cb245-5)  mutate(State = factor(State, levels=c("QLD","VIC","NT","TAS"))) |>
    [](hts.html#cb245-6)  gg_season(Trips) +
    [](hts.html#cb245-7)  facet_wrap(vars(State), nrow = 2, scales = "free_y")+
    [](hts.html#cb245-8)  labs(y = "Trips ('000)")

Figure 11.4: Seasonal plots for overnight trips for Queensland and the Northern Territory, and Victoria and Tasmania highlighting the contrast in seasonal patterns between northern and southern states in Australia. 

The seasonal pattern of the northern states, such as Queensland and the Northern Territory, leads to peak visits in winter (corresponding to Q3) due to the tropical climate and rainy summer months. In contrast, the southern states tend to peak in summer (corresponding to Q1). This is highlighted in the seasonal plots shown in Figure [11.4](hts.html#fig:seasonStates) for Queensland and the Northern Territory (shown in the left column) versus the most southern states of Victoria and Tasmania (shown in the right column).

Figure 11.5: Domestic overnight trips from 1998 Q1 to 2017 Q4 for some selected regions. 

The plots in Figure [11.5](hts.html#fig:tourismRegions) shows data for some selected regions. These help us visualise the diverse regional dynamics within each state, with some series showing strong trends or seasonality, some showing contrasting seasonality, while some series appear to be just noise.

### Grouped time series[](hts.html#grouped-time-series)

With grouped time series, the data structure does not naturally disaggregate in a unique hierarchical manner. Figure [11.6](hts.html#fig:GroupTree) shows a simple grouped structure. At the top of the grouped structure is the Total, the most aggregate level of the data, again represented by \\(y_t\\). The Total can be disaggregated by attributes (A, B) forming series \\(\y{A}{t}\\) and \\(\y{B}{t}\\), or by attributes (X, Y) forming series \\(\y{X}{t}\\) and \\(\y{Y}{t}\\). At the bottom level, the data are disaggregated by both attributes.

Figure 11.6: Alternative representations of a two level grouped structure. 

This example shows that there are alternative aggregation paths for grouped structures. For any time \\(t\\), as with the hierarchical structure, \\[\begin{equation*} y_{t}=\y{AX}{t}+\y{AY}{t}+\y{BX}{t}+\y{BY}{t}. \end{equation*}\\] However, for the first level of the grouped structure, \\[\begin{equation} \y{A}{t}=\y{AX}{t}+\y{AY}{t}\quad \quad \y{B}{t}=\y{BX}{t}+\y{BY}{t} \tag{11.3} \end{equation}\\] but also \\[\begin{equation} \y{X}{t}=\y{AX}{t}+\y{BX}{t}\quad \quad \y{Y}{t}=\y{AY}{t}+\y{BY}{t} \tag{11.4}. \end{equation}\\]

Grouped time series can sometimes be thought of as hierarchical time series that do not impose a unique hierarchical structure, in the sense that the order by which the series can be grouped is not unique.

### Example: Australian prison population[](hts.html#example-australian-prison-population)

In this example we consider the Australia prison population data introduced in Chapter [2](graphics.html#graphics). The top panel in Figure [11.7](hts.html#fig:prisongts) shows the total number of prisoners in Australia over the period 2005Q1–2016Q4. This represents the top-level series in the grouping structure. The panels below show the prison population disaggregated or grouped by (a) state (b) legal status (whether prisoners have already been sentenced or are in remand waiting for a sentence), and (c) gender. The three factors are crossed, but none are nested within the others.

Figure 11.7: Total Australian quarterly adult prison population, disaggregated by state, by legal status, and by gender. 

The following code, introduced in Section [2.1](tsibbles.html#tsibbles), builds a `tsibble` object for the prison data.
    
    
    [](hts.html#cb246-1)prison <- readr::read_csv("https://OTexts.com/fpp3/extrafiles/prison_population.csv") |>
    [](hts.html#cb246-2)  mutate(Quarter = yearquarter(Date)) |>
    [](hts.html#cb246-3)  select(-Date)  |>
    [](hts.html#cb246-4)  as_tsibble(key = c(Gender, Legal, State, Indigenous),
    [](hts.html#cb246-5)             index = Quarter) |>
    [](hts.html#cb246-6)  relocate(Quarter)

We create a grouped time series using `aggregate_key()` with attributes or groupings of interest now being crossed using the syntax `attribute1*attribute2` (in contrast to the `parent/child` syntax used for hierarchical time series). The following code builds a grouped tsibble for the prison data with crossed attributes: gender, legal status and state.
    
    
    [](hts.html#cb247-1)prison_gts <- prison |>
    [](hts.html#cb247-2)  aggregate_key(Gender * Legal * State, Count = sum(Count)/1e3)

Using `is_aggregated()` within `filter()` is helpful for exploring or plotting the main groups shown in the bottom panels of Figure [11.7](hts.html#fig:prisongts). For example, the following code plots the total numbers of female and male prisoners across Australia.
    
    
    [](hts.html#cb248-1)prison_gts |>
    [](hts.html#cb248-2)  filter(!is_aggregated(Gender), is_aggregated(Legal),
    [](hts.html#cb248-3)         is_aggregated(State)) |>
    [](hts.html#cb248-4)  autoplot(Count) +
    [](hts.html#cb248-5)  labs(y = "Number of prisoners ('000)")

Plots of other group combinations can be obtained in a similar way. Figure [11.8](hts.html#fig:prison1) shows the Australian prison population grouped by all possible combinations of two attributes at a time: state and gender, state and legal status, and legal status and gender. The following code will reproduce the first plot in Figure [11.8](hts.html#fig:prison1).

Figure 11.8: Australian adult prison population disaggregated by pairs of attributes. 
    
    
    [](hts.html#cb249-1)prison_gts |>
    [](hts.html#cb249-2)  filter(!is_aggregated(Gender), !is_aggregated(Legal),
    [](hts.html#cb249-3)         !is_aggregated(State)) |>
    [](hts.html#cb249-4)  mutate(Gender = as.character(Gender)) |>
    [](hts.html#cb249-5)  ggplot(aes(x = Quarter, y = Count,
    [](hts.html#cb249-6)             group = Gender, colour=Gender)) +
    [](hts.html#cb249-7)  stat_summary(fun = sum, geom = "line") +
    [](hts.html#cb249-8)  labs(title = "Prison population by state and gender",
    [](hts.html#cb249-9)       y = "Number of prisoners ('000)") +
    [](hts.html#cb249-10)  facet_wrap(~ as.character(State),
    [](hts.html#cb249-11)             nrow = 1, scales = "free_y") +
    [](hts.html#cb249-12)  theme(axis.text.x = element_text(angle = 90, hjust = 1))

Figure [11.9](hts.html#fig:prisonBTS) shows the Australian adult prison population disaggregated by all three attributes: state, legal status and gender. These form the bottom-level series of the grouped structure.

Figure 11.9: Bottom-level time series for the Australian adult prison population, grouped by state, legal status and gender. 

### Mixed hierarchical and grouped structure[](hts.html#mixed-hierarchical-and-grouped-structure)

Often disaggregating factors are both nested and crossed. For example, the Australian tourism data can also be disaggregated by the four purposes of travel: holiday, business, visiting friends and relatives, and other. This grouping variable does not nest within any of the geographical variables. In fact, we could consider overnight trips split by purpose of travel for the whole of Australia, and for each state, and for each region. We describe such a structure as a “nested” geographic hierarchy “crossed” with the purpose of travel. Using `aggregate_key()` this can be specified by simply combining the factors.
    
    
    [](hts.html#cb250-1)tourism_full <- tourism |>
    [](hts.html#cb250-2)  aggregate_key((State/Region) * Purpose, Trips = sum(Trips))

The `tourism_full` tsibble contains 425 series, including the 85 series from the hierarchical structure, as well as another 340 series obtained when each series of the hierarchical structure is crossed with the purpose of travel.

Figure 11.10: Australian domestic overnight trips from 1998 Q1 to 2017 Q4 disaggregated by purpose of travel. 

Figure 11.11: Australian domestic overnight trips over the period 1998 Q1 to 2017 Q4 disaggregated by purpose of travel and by state. 

Figures [11.10](hts.html#fig:mixed-purpose) and [11.11](hts.html#fig:mixed-state-purpose) show the aggregate series grouped by purpose of travel, and the series grouped by purpose of travel and state, revealing further rich and diverse dynamics across these series.


---

## 11.2 Single level approaches[](single-level.html#single-level)

Traditionally, forecasts of hierarchical or grouped time series involved selecting one level of aggregation and generating forecasts for that level. These are then either aggregated for higher levels, or disaggregated for lower levels, to obtain a set of coherent forecasts for the rest of the structure.

### The bottom-up approach[](single-level.html#the-bottom-up-approach)

A simple method for generating coherent forecasts is the “bottom-up” approach. This approach involves first generating forecasts for each series at the bottom level, and then summing these to produce forecasts for all the series in the structure.

For example, for the hierarchy of Figure [11.1](hts.html#fig:HierTree), we first generate \\(h\\)-step-ahead forecasts for each of the bottom-level series: \\[ \yhat{AA}{h},~~\yhat{AB}{h},~~\yhat{AC}{h},~~ \yhat{BA}{h}~~\text{and}~~\yhat{BB}{h}. \\] (We have simplified the previously used notation of \\(\hat{y}_{T+h|T}\\) for brevity.)

Summing these, we get \\(h\\)-step-ahead coherent forecasts for the rest of the series: \\[\begin{align*} \tilde{y}_{h} & =\yhat{AA}{h}+\yhat{AB}{h}+\yhat{AC}{h}+\yhat{BA}{h}+\yhat{BB}{h}, \\\ \ytilde{A}{h} & = \yhat{AA}{h}+\yhat{AB}{h}+\yhat{AC}{h}, \\\ \text{and}\quad \ytilde{B}{h} &= \yhat{BA}{h}+\yhat{BB}{h}. \end{align*}\\] (In this chapter, we will use the “tilde” notation to indicate coherent forecasts.)

An advantage of this approach is that we are forecasting at the bottom level of a structure, and therefore no information is lost due to aggregation. On the other hand, bottom-level data can be quite noisy and more challenging to model and forecast.

#### Example: Generating bottom-up forecasts[](single-level.html#example-generating-bottom-up-forecasts)

Suppose we want national and state forecasts for the Australian tourism data, but we aren’t interested in disaggregations using regions or the purpose of travel. So we first create a simple `tsibble` object containing only state and national trip totals for each quarter.
    
    
    [](single-level.html#cb251-1)tourism_states <- tourism |>
    [](single-level.html#cb251-2)  aggregate_key(State, Trips = sum(Trips))

We could generate the bottom-level state forecasts first, and then sum them to obtain the national forecasts.
    
    
    [](single-level.html#cb252-1)fcasts_state <- tourism_states |>
    [](single-level.html#cb252-2)  filter(!is_aggregated(State)) |>
    [](single-level.html#cb252-3)  model(ets = ETS(Trips)) |>
    [](single-level.html#cb252-4)  forecast()
    [](single-level.html#cb252-5)
    [](single-level.html#cb252-6)# Sum bottom-level forecasts to get top-level forecasts
    [](single-level.html#cb252-7)fcasts_national <- fcasts_state |>
    [](single-level.html#cb252-8)  summarise(value = sum(Trips), .mean = mean(value))

However, we want a more general approach that will work with all the forecasting methods discussed in this chapter. So we will use the `reconcile()` function to specify how we want to compute coherent forecasts.
    
    
    [](single-level.html#cb253-1)tourism_states |>
    [](single-level.html#cb253-2)  model(ets = ETS(Trips)) |>
    [](single-level.html#cb253-3)  reconcile(bu = bottom_up(ets)) |>
    [](single-level.html#cb253-4)  forecast()
    [](single-level.html#cb253-5)#> # A fable: 144 x 5 [1Q]
    [](single-level.html#cb253-6)#> # Key:     State, .model [18]
    [](single-level.html#cb253-7)#>    State  .model Quarter
    [](single-level.html#cb253-8)#>    <chr*> <chr>    <qtr>
    [](single-level.html#cb253-9)#>  1 ACT    ets    2018 Q1
    [](single-level.html#cb253-10)#>  2 ACT    ets    2018 Q2
    [](single-level.html#cb253-11)#>  3 ACT    ets    2018 Q3
    [](single-level.html#cb253-12)#>  4 ACT    ets    2018 Q4
    [](single-level.html#cb253-13)#>  5 ACT    ets    2019 Q1
    [](single-level.html#cb253-14)#>  6 ACT    ets    2019 Q2
    [](single-level.html#cb253-15)#>  7 ACT    ets    2019 Q3
    [](single-level.html#cb253-16)#>  8 ACT    ets    2019 Q4
    [](single-level.html#cb253-17)#>  9 ACT    bu     2018 Q1
    [](single-level.html#cb253-18)#> 10 ACT    bu     2018 Q2
    [](single-level.html#cb253-19)#> # ℹ 134 more rows
    [](single-level.html#cb253-20)#> # ℹ 2 more variables: Trips <dist>, .mean <dbl>

The `reconcile()` step has created a new “model” to produce bottom-up forecasts. The `fable` object contains the `ets` forecasts as well as the coherent `bu` forecasts, for the 8 states and the national aggregate. At the state level, these forecasts are identical, but the national `ets` forecasts will be different from the national `bu` forecasts.

For bottom-up forecasting, this is rather inefficient as we are not interested in the ETS model for the national total, and the resulting `fable` contains a lot of duplicates. But later we will introduce more advanced methods where we will need models for all levels of aggregation, and where the coherent forecasts are different from any of the original forecasts.

#### Workflow for forecasting aggregation structures[](single-level.html#workflow-for-forecasting-aggregation-structures)

The above code illustrates the general workflow for hierarchical and grouped forecasts. We use the following pipeline of functions.
    
    
    [](single-level.html#cb254-1)data |> aggregate_key() |> model() |>
    [](single-level.html#cb254-2)  reconcile() |> forecast()

  1. Begin with a `tsibble` object (here labelled `data`) containing the individual bottom-level series.
  2. Define in `aggregate_key()` the aggregation structure and build a `tsibble` object that also contains the aggregate series.
  3. Identify a `model()` for each series, at all levels of aggregation.
  4. Specify in `reconcile()` how the coherent forecasts are to be generated from the selected models.
  5. Use the `forecast()` function to generate forecasts for the whole aggregation structure.


### Top-down approaches[](single-level.html#top-down-approaches)

Top-down approaches involve first generating forecasts for the Total series \\(y_t\\), and then disaggregating these down the hierarchy.

Let \\(p_1,\dots,p_{m}\\) denote a set of disaggregation proportions which determine how the forecasts of the Total series are to be distributed to obtain forecasts for each series at the bottom level of the structure. For example, for the hierarchy of Figure [11.1](hts.html#fig:HierTree), using proportions \\(p_1,\dots,p_{5}\\) we get \\[ \ytilde{AA}{t}=p_1\hat{y}_t,~~~\ytilde{AB}{t}=p_2\hat{y}_t,~~~\ytilde{AC}{t}=p_3\hat{y}_t,~~~\ytilde{BA}{t}=p_4\hat{y}_t~~~\text{and}~~~~~~\ytilde{BB}{t}=p_5\hat{y}_t. \\] Once the bottom-level \\(h\\)-step-ahead forecasts have been generated, these are aggregated to generate coherent forecasts for the rest of the series.

Top-down forecasts can be generated using `top_down()` within the `reconcile()` function.

There are several possible top-down methods that can be specified. The two most common top-down approaches specify disaggregation proportions based on the historical proportions of the data. These performed well in the study of Gross & Sohl ([1990](single-level.html#ref-GroSoh1990)).

#### Average historical proportions[](single-level.html#average-historical-proportions)

\\[ p_j=\frac{1}{T}\sum_{t=1}^{T}\frac{y_{j,t}}{{y_t}} \\] for \\(j=1,\dots,m\\). Each proportion \\(p_j\\) reflects the average of the historical proportions of the bottom-level series \\(y_{j,t}\\) over the period \\(t=1,\dots,T\\) relative to the total aggregate \\(y_t\\).

This approach is implemented in the `top_down()` function by setting `method = "average_proportions"`.

#### Proportions of the historical averages[](single-level.html#proportions-of-the-historical-averages)

\\[ p_j={\sum_{t=1}^{T}\frac{y_{j,t}}{T}}\Big/{\sum_{t=1}^{T}\frac{y_t}{T}} \\] for \\(j=1,\dots,m\\). Each proportion \\(p_j\\) captures the average historical value of the bottom-level series \\(y_{j,t}\\) relative to the average value of the total aggregate \\(y_t\\).

This approach is implemented in the `top_down()` function by setting `method = "proportion_averages"`.

A convenient attribute of such top-down approaches is their simplicity. One only needs to model and generate forecasts for the most aggregated top-level series. In general, these approaches seem to produce quite reliable forecasts for the aggregate levels and they are useful with low count data. On the other hand, one disadvantage is the loss of information due to aggregation. Using such top-down approaches, we are unable to capture and take advantage of individual series characteristics such as time dynamics, special events, different seasonal patterns, etc.

#### Forecast proportions[](single-level.html#forecast-proportions)

Because historical proportions used for disaggregation do not take account of how those proportions may change over time, top-down approaches based on historical proportions tend to produce less accurate forecasts at lower levels of the hierarchy than bottom-up approaches. To address this issue, proportions based on forecasts rather than historical data can be used ([Athanasopoulos et al., 2009](single-level.html#ref-AthEtAl2009)).

Consider a one level hierarchy. We first generate \\(h\\)-step-ahead forecasts for all of the series. We don’t use these forecasts directly, and they are not coherent (they don’t add up correctly). Let’s call these “initial” forecasts. We calculate the proportion of each \\(h\\)-step-ahead initial forecast at the bottom level, to the aggregate of all the \\(h\\)-step-ahead initial forecasts at this level. We refer to these as the forecast proportions, and we use them to disaggregate the top-level \\(h\\)-step-ahead initial forecast in order to generate coherent forecasts for the whole of the hierarchy.

For a \\(K\\)-level hierarchy, this process is repeated for each node, going from the top to the bottom level. Applying this process leads to the following general rule for obtaining the forecast proportions: \\[ p_j=\prod^{K-1}_{\ell=0}\frac{\hat{y}_{j,h}^{(\ell)}}{\hat{S}_{j,h}^{(\ell+1)}} \\] where \\(j=1,2,\dots,m\\), \\(\hat{y}_{j,h}^{(\ell)}\\) is the \\(h\\)-step-ahead initial forecast of the series that corresponds to the node which is \\(\ell\\) levels above \\(j\\), and \\(\hat{S}_{j,h}^{(\ell)}\\) is the sum of the \\(h\\)-step-ahead initial forecasts below the node that is \\(\ell\\) levels above node \\(j\\) and are directly connected to that node. These forecast proportions disaggregate the \\(h\\)-step-ahead initial forecast of the Total series to get \\(h\\)-step-ahead coherent forecasts of the bottom-level series.

We will use the hierarchy of Figure [11.1](hts.html#fig:HierTree) to explain this notation and to demonstrate how this general rule is reached. Assume we have generated initial forecasts for each series in the hierarchy. Recall that for the top-level “Total” series, \\(\tilde{y}_{h}=\hat{y}_{h}\\), for any top-down approach. Here are some examples using the above notation:

  * \\(\hat{y}_{\text{A},h}^{(1)}=\hat{y}_{\text{B},h}^{(1)}=\hat{y}_{h}= \tilde{y}_{h}\\);
  * \\(\hat{y}_{\text{AA},h}^{(1)}=\hat{y}_{\text{AB},h}^{(1)}=\hat{y}_{\text{AC},h}^{(1)}= \hat{y}_{\text{A},h}\\);
  * \\(\hat{y}_{\text{AA},h}^{(2)}=\hat{y}_{\text{AB},h}^{(2)}= \hat{y}_{\text{AC},h}^{(2)}=\hat{y}_{\text{BA},h}^{(2)}= \hat{y}_{\text{BB},h}^{(2)}=\hat{y}_{h}= \tilde{y}_{h}\\);
  * \\(\Shat{AA}{h}{1} = \Shat{AB}{h}{1}= \Shat{AC}{h}{1}= \yhat{AA}{h}+\yhat{AB}{h}+\yhat{AC}{h}\\);
  * \\(\Shat{AA}{h}{2} = \Shat{AB}{h}{2}= \Shat{AC}{h}{2}= \Shat{A}{h}{1} = \Shat{B}{h}{1}= \hat{S}_{h}= \yhat{A}{h}+\yhat{B}{h}\\).


Moving down the farthest left branch of the hierarchy, coherent forecasts are given by \\[ \ytilde{A}{h} = \Bigg(\frac{\yhat{A}{h}}{\Shat{A}{h}{1}}\Bigg) \tilde{y}_{h} = \Bigg(\frac{\yhat{AA}{h}^{(1)}}{\Shat{AA}{h}{2}}\Bigg) \tilde{y}_{h} \\] and \\[ \ytilde{AA}{h} = \Bigg(\frac{\yhat{AA}{h}}{\Shat{AA}{h}{1}}\Bigg) \ytilde{A}{h} =\Bigg(\frac{\yhat{AA}{h}}{\Shat{AA}{h}{1}}\Bigg) \Bigg(\frac{\yhat{AA}{h}^{(1)}}{\Shat{AA}{h}{2}}\Bigg)\tilde{y}_{h}. \\] Consequently, \\[ p_1=\Bigg(\frac{\yhat{AA}{h}}{\Shat{AA}{h}{1}}\Bigg) \Bigg(\frac{\yhat{AA}{h}^{(1)}}{\Shat{AA}{h}{2}}\Bigg). \\] The other proportions can be obtained similarly.

This approach is implemented in the `top_down()` function by setting `method = "forecast_proportions"`. Because this approach tends to work better than other top-down methods, it is the default choice in the `top_down()` function when no `method` argument is specified.

One disadvantage of all top-down approaches, is that they do not produce unbiased coherent forecasts ([Hyndman et al., 2011](single-level.html#ref-HynEtAl2011)) even if the base forecasts are unbiased.

### Middle-out approach[](single-level.html#middle-out-approach)

The middle-out approach combines bottom-up and top-down approaches. Again, it can only be used for strictly hierarchical aggregation structures.

First, a “middle” level is chosen and forecasts are generated for all the series at this level. For the series above the middle level, coherent forecasts are generated using the bottom-up approach by aggregating the “middle-level” forecasts upwards. For the series below the “middle level”, coherent forecasts are generated using a top-down approach by disaggregating the “middle level” forecasts downwards.

This approach is implemented in the `middle_out()` function by specifying the appropriate middle level via the `level` argument and selecting the top-down approach with the `method` argument.

### Bibliography[](bibliography.html#bibliography)

Athanasopoulos, G., Ahmed, R. A., & Hyndman, R. J. (2009). Hierarchical forecasts for Australian domestic tourism. _International Journal of Forecasting_ , _25_ , 146–166. [__](https://doi.org/10.1016/j.ijforecast.2008.07.004)

Gross, C. W., & Sohl, J. E. (1990). Disaggregation methods to expedite product line forecasting. _Journal of Forecasting_ , _9_ , 233–254. [__](https://doi.org/10.1002/for.3980090304)

Hyndman, R. J., Ahmed, R. A., Athanasopoulos, G., & Shang, H. L. (2011). Optimal combination forecasts for hierarchical time series. _Computational Statistics and Data Analysis_ , _55_(9), 2579–2589. [__](https://doi.org/10.1016/j.csda.2011.03.006)


---

## 11.3 Forecast reconciliation[](reconciliation.html#reconciliation)

_Warning: the rest of this chapter is more advanced and assumes a knowledge of some basic matrix algebra._

### Matrix notation[](reconciliation.html#matrix-notation)

Recall that Equations [(11.1)](hts.html#eq:toplevel) and [(11.2)](hts.html#eq:middlelevel) represent how data, that adhere to the hierarchical structure of Figure [11.1](hts.html#fig:HierTree), aggregate. Similarly [(11.3)](hts.html#eq:middlelevelAB) and [(11.4)](hts.html#eq:middlelevelXY) represent how data, that adhere to the grouped structure of Figure [11.6](hts.html#fig:GroupTree), aggregate. These equations can be thought of as aggregation constraints or summing equalities, and can be more efficiently represented using matrix notation.

For any aggregation structure we construct an \\(n\times m\\) matrix \\(\bm{S}\\) (referred to as the “summing matrix”) which dictates the way in which the bottom-level series aggregate.

For the hierarchical structure in Figure [11.1](hts.html#fig:HierTree), we can write \\[ \begin{bmatrix} y_{t} \\\ \y{A}{t} \\\ \y{B}{t} \\\ \y{AA}{t} \\\ \y{AB}{t} \\\ \y{AC}{t} \\\ \y{BA}{t} \\\ \y{BB}{t} \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 1 & 1 \\\ 1 & 1 & 1 & 0 & 0 \\\ 0 & 0 & 0 & 1 & 1 \\\ 1 & 0 & 0 & 0 & 0 \\\ 0 & 1 & 0 & 0 & 0 \\\ 0 & 0 & 1 & 0 & 0 \\\ 0 & 0 & 0 & 1 & 0 \\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \y{AA}{t} \\\ \y{AB}{t} \\\ \y{AC}{t} \\\ \y{BA}{t} \\\ \y{BB}{t} \end{bmatrix} \\] or in more compact notation \\[\begin{equation} \bm{y}_t=\bm{S}\bm{b}_{t}, \tag{11.5} \end{equation}\\] where \\(\bm{y}_t\\) is an \\(n\\)-dimensional vector of all the observations in the hierarchy at time \\(t\\), \\(\bm{S}\\) is the summing matrix, and \\(\bm{b}_{t}\\) is an \\(m\\)-dimensional vector of all the observations in the bottom level of the hierarchy at time \\(t\\). Note that the first row in the summing matrix \\(\bm{S}\\) represents Equation [(11.1)](hts.html#eq:toplevel), the second and third rows represent [(11.2)](hts.html#eq:middlelevel). The rows below these comprise an \\(m\\)-dimensional identity matrix \\(\bm{I}_m\\) so that each bottom-level observation on the right hand side of the equation is equal to itself on the left hand side.

Similarly for the grouped structure of Figure [11.6](hts.html#fig:GroupTree) we write \\[ \begin{bmatrix} y_{t} \\\ \y{A}{t} \\\ \y{B}{t} \\\ \y{X}{t} \\\ \y{Y}{t} \\\ \y{AX}{t} \\\ \y{AY}{t} \\\ \y{BX}{t} \\\ \y{BY}{t} \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 1 \\\ 1 & 1 & 0 & 0 \\\ 0 & 0 & 1 & 1 \\\ 1 & 0 & 1 & 0 \\\ 0 & 1 & 0 & 1 \\\ 1 & 0 & 0 & 0 \\\ 0 & 1 & 0 & 0 \\\ 0 & 0 & 1 & 0 \\\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} \y{AX}{t} \\\ \y{AY}{t} \\\ \y{BX}{t} \\\ \y{BY}{t} \end{bmatrix}, \\] or \\[\begin{equation} \bm{y}_t=\bm{S}\bm{b}_{t}, \tag{11.6} \end{equation}\\] where the second and third rows of \\(\bm{S}\\) represent Equation [(11.3)](hts.html#eq:middlelevelAB) and the fourth and fifth rows represent [(11.4)](hts.html#eq:middlelevelXY).

### Mapping matrices[](reconciliation.html#mapping-matrices)

This matrix notation allows us to represent all forecasting methods for hierarchical or grouped time series using a common notation.

Suppose we forecast all series ignoring any aggregation constraints. We call these the **base forecasts** and denote them by \\(\hat{\bm{y}}_h\\) where \\(h\\) is the forecast horizon. They are stacked in the same order as the data \\(\bm{y}_t\\).

Then all coherent forecasting approaches for either hierarchical or grouped structures can be represented as[23](reconciliation.html#fn23) \\[\begin{equation} \tilde{\bm{y}}_h=\bm{S}\bm{G}\hat{\bm{y}}_h, \tag{11.7} \end{equation}\\] where \\(\bm{G}\\) is a matrix that maps the base forecasts into the bottom level, and the summing matrix \\(\bm{S}\\) sums these up using the aggregation structure to produce a set of **coherent forecasts** \\(\tilde{\bm{y}}_h\\).

The \\(\bm{G}\\) matrix is defined according to the approach implemented. For example if the bottom-up approach is used to forecast the hierarchy of Figure [11.1](hts.html#fig:HierTree), then \\[\bm{G}= \begin{bmatrix} 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0\\\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0\\\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\\ \end{bmatrix}. \\] Notice that \\(\bm{G}\\) contains two partitions. The first three columns zero out the base forecasts of the series above the bottom level, while the \\(m\\)-dimensional identity matrix picks only the base forecasts of the bottom level. These are then summed by the \\(\bm{S}\\) matrix.

If any of the top-down approaches were used then \\[ \bm{G}= \begin{bmatrix} p_1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\\ p_2 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\\ p_3 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\\ p_4 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\\ p_5 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\\ \end{bmatrix}. \\] The first column includes the set of proportions that distribute the base forecasts of the top level to the bottom level. These are then summed up by the \\(\bm{S}\\) matrix. The rest of the columns zero out the base forecasts below the highest level of aggregation.

For a middle out approach, the \\(\bm{G}\\) matrix will be a combination of the above two. Using a set of proportions, the base forecasts of some pre-chosen level will be disaggregated to the bottom level, all other base forecasts will be zeroed out, and the bottom-level forecasts will then be summed up the hierarchy via the summing matrix.

### Forecast reconciliation[](reconciliation.html#forecast-reconciliation)

Equation [(11.7)](reconciliation.html#eq:SG) shows that pre-multiplying any set of base forecasts with \\(\bm{S}\bm{G}\\) will return a set of coherent forecasts.

The traditional methods considered so far are limited in that they only use base forecasts from a single level of aggregation which have either been aggregated or disaggregated to obtain forecasts at all other levels. Hence, they use limited information. However, in general, we could use other \\(\bm{G}\\) matrices, and then \\(\bm{S}\bm{G}\\) combines and reconciles all the base forecasts in order to produce coherent forecasts.

In fact, we can find the optimal \\(\bm{G}\\) matrix to give the most accurate reconciled forecasts.

### The MinT optimal reconciliation approach[](reconciliation.html#the-mint-optimal-reconciliation-approach)

Wickramasuriya et al. ([2019](reconciliation.html#ref-Mint)) found a \\(\bm{G}\\) matrix that minimises the total forecast variance of the set of coherent forecasts, leading to the MinT (Minimum Trace) optimal reconciliation approach.

Suppose we generate coherent forecasts using Equation [(11.7)](reconciliation.html#eq:SG). First we want to make sure we have unbiased forecasts. If the base forecasts \\(\hat{\bm{y}}_h\\) are unbiased, then the coherent forecasts \\(\tilde{\bm{y}}_h\\) will be unbiased provided[24](reconciliation.html#fn24) \\(\bm{S}\bm{G}\bm{S}=\bm{S}\\). This provides a constraint on the matrix \\(\bm{G}\\). Interestingly, no top-down method satisfies this constraint, so all top-down approaches result in biased coherent forecasts.

Next we need to find the errors in our forecasts. Wickramasuriya et al. ([2019](reconciliation.html#ref-Mint)) show that the variance-covariance matrix of the \\(h\\)-step-ahead coherent forecast errors is given by \\[\begin{equation*} \bm{V}_h = \text{Var}[\bm{y}_{T+h}-\tilde{\bm{y}}_h]=\bm{S}\bm{G}\bm{W}_h\bm{G}'\bm{S}' \end{equation*}\\] where \\(\bm{W}_h=\text{Var}[(\bm{y}_{T+h}-\hat{\bm{y}}_h)]\\) is the variance-covariance matrix of the corresponding base forecast errors.

The objective is to find a matrix \\(\bm{G}\\) that minimises the error variances of the coherent forecasts. These error variances are on the diagonal of the matrix \\(\bm{V}_h\\), and so the sum of all the error variances is given by the trace of the matrix \\(\bm{V}_h\\). Wickramasuriya et al. ([2019](reconciliation.html#ref-Mint)) show that the matrix \\(\bm{G}\\) which minimises the trace of \\(\bm{V}_h\\) such that \\(\bm{S}\bm{G}\bm{S}=\bm{S}\\), is given by \\[ \bm{G}=(\bm{S}'\bm{W}_h^{-1}\bm{S})^{-1}\bm{S}'\bm{W}_h^{-1}. \\] Therefore, the optimally reconciled forecasts are given by \\[\begin{equation} \tag{11.8} \tilde{\bm{y}}_h=\bm{S}(\bm{S}'\bm{W}_h^{-1}\bm{S})^{-1}\bm{S}'\bm{W}_h^{-1}\hat{\bm{y}}_h. \end{equation}\\]

We refer to this as the MinT (or Minimum Trace) optimal reconciliation approach. MinT is implemented by `min_trace()` within the `reconcile()` function.

To use this in practice, we need to estimate \\(\bm{W}_h\\), the forecast error variance of the \\(h\\)-step-ahead base forecasts. This can be difficult, and so we provide four simplifying approximations that have been shown to work well in both simulations and in practice.

  1. Set \\(\bm{W}_h=k_h\bm{I}\\) for all \\(h\\), where \\(k_{h} > 0\\).[25](reconciliation.html#fn25) This is the most simplifying assumption to make, and means that \\(\bm{G}\\) is independent of the data, providing substantial computational savings. The disadvantage, however, is that this specification does not account for the differences in scale between the levels of the structure, or for relationships between series.

Setting \\(\bm{W}_h=k_h\bm{I}\\) in [(11.8)](reconciliation.html#eq:MinT) gives the ordinary least squares (OLS) estimator we introduced in Section [7.9](regression-matrices.html#regression-matrices) with \\(\bm{X}=\bm{S}\\) and \\(\bm{y}=\hat{\bm{y}}\\). Hence this approach is usually referred to as OLS reconciliation. It is implemented in `min_trace()` by setting `method = "ols"`.

  2. Set \\(\bm{W}_{h} = k_{h}\text{diag}(\hat{\bm{W}}_{1})\\) for all \\(h\\), where \\(k_{h} > 0\\), \\[ \hat{\bm{W}}_{1} = \frac{1}{T}\sum_{t=1}^{T}\bm{e}_{t}\bm{e}_{t}', \\] and \\(\bm{e}_{t}\\) is an \\(n\\)-dimensional vector of residuals of the models that generated the base forecasts stacked in the same order as the data.

This specification scales the base forecasts using the variance of the residuals and it is therefore referred to as the WLS (weighted least squares) estimator using _variance scaling_. The approach is implemented in `min_trace()` by setting `method = "wls_var"`.

  3. Set \\(\bm{W}_{h}=k_{h}\bm{\Lambda}\\) for all \\(h\\), where \\(k_{h} > 0\\), \\(\bm{\Lambda}=\text{diag}(\bm{S}\bm{1})\\), and \\(\bm{1}\\) is a unit vector of dimension \\(m\\) (the number of bottom-level series). This specification assumes that the bottom-level base forecast errors each have variance \\(k_{h}\\) and are uncorrelated between nodes. Hence each element of the diagonal \\(\bm{\Lambda}\\) matrix contains the number of forecast error variances contributing to each node. This estimator only depends on the structure of the aggregations, and not on the actual data. It is therefore referred to as _structural scaling_. Applying the structural scaling specification is particularly useful in cases where residuals are not available, and so variance scaling cannot be applied; for example, in cases where the base forecasts are generated by judgmental forecasting (Chapter [6](judgmental.html#judgmental)). The approach is implemented in `min_trace()` by setting `method = "wls_struct"`.

  4. Set \\(\bm{W}_h = k_h \bm{W}_1\\) for all \\(h\\), where \\(k_h>0\\). Here we only assume that the error covariance matrices are proportional to each other, and we directly estimate the full one-step covariance matrix \\(\bm{W}_1\\). The most obvious and simple way would be to use the sample covariance. This is implemented in `min_trace()` by setting `method = "mint_cov"`.

However, for cases where the number of bottom-level series \\(m\\) is large compared to the length of the series \\(T\\), this is not a good estimator. Instead we use a shrinkage estimator which shrinks the sample covariance to a diagonal matrix. This is implemented in `min_trace()` by setting `method = "mint_shrink"`.


In summary, unlike any other existing approach, the optimal reconciliation forecasts are generated using all the information available within a hierarchical or a grouped structure. This is important, as particular aggregation levels or groupings may reveal features of the data that are of interest to the user and are important to be modelled. These features may be completely hidden or not easily identifiable at other levels.

For example, consider the Australian tourism data introduced in Section [11.1](hts.html#hts), where the hierarchical structure followed the geographic division of a country into states and regions. Some areas will be largely summer destinations, while others may be winter destinations. We saw in Figure [11.4](hts.html#fig:seasonStates) the contrasting seasonal patterns between the northern and the southern states. These differences will be smoothed at the country level due to aggregation.

### Bibliography[](bibliography.html#bibliography)

Hyndman, R. J., Ahmed, R. A., Athanasopoulos, G., & Shang, H. L. (2011). Optimal combination forecasts for hierarchical time series. _Computational Statistics and Data Analysis_ , _55_(9), 2579–2589. [__](https://doi.org/10.1016/j.csda.2011.03.006)

Panagiotelis, A., Athanasopoulos, G., Gamakumara, P., & Hyndman, R. J. (2021). Forecast reconciliation: A geometric view with new insights on bias correction. _International Journal of Forecasting_ , _37_(1), 343–359. [__](https://doi.org/10.1016/j.ijforecast.2020.06.004)

Wickramasuriya, S. L., Athanasopoulos, G., & Hyndman, R. J. (2019). Optimal forecast reconciliation for hierarchical and grouped time series through trace minimization. _Journal of the American Statistical Association_ , _114_(526), 804–819. [__](https://doi.org/10.1080/01621459.2018.1448825)

* * *

  23. Actually, some recent nonlinear reconciliation methods require a slightly more complicated equation. This equation is for general linear reconciliation methods.[↩︎](reconciliation.html#fnref23)

  24. This “unbiasedness preserving” constraint was first introduced in Hyndman et al. ([2011](reconciliation.html#ref-HynEtAl2011)). Panagiotelis et al. ([2021](reconciliation.html#ref-PanEtAl2020_Geometry)) show that this is equivalent to \\(\bm{S}\bm{G}\\) being a projection matrix onto the \\(m\\)-dimensional coherent subspace for which the aggregation constraints hold.[↩︎](reconciliation.html#fnref24)

  25. Note that \\(k_{h}\\) is a proportionality constant. It does not need to be estimated or specified here as it gets cancelled out in [(11.8)](reconciliation.html#eq:MinT).[↩︎](reconciliation.html#fnref25)




---

## 11.4 Forecasting Australian domestic tourism[](tourism.html#tourism)

We will compute forecasts for the Australian tourism data that was described in Section [11.1](hts.html#hts). We use the data up to the end of 2015 as a training set, withholding the final two years (eight quarters, 2016Q1–2017Q4) as a test set for evaluation. The code below demonstrates the full workflow for generating coherent forecasts using the bottom-up, OLS and MinT methods.
    
    
    [](tourism.html#cb255-1)tourism_full <- tourism |>
    [](tourism.html#cb255-2)  aggregate_key((State/Region) * Purpose, Trips = sum(Trips))
    [](tourism.html#cb255-3)
    [](tourism.html#cb255-4)fit <- tourism_full |>
    [](tourism.html#cb255-5)  filter(year(Quarter) <= 2015) |>
    [](tourism.html#cb255-6)  model(base = ETS(Trips)) |>
    [](tourism.html#cb255-7)  reconcile(
    [](tourism.html#cb255-8)    bu = bottom_up(base),
    [](tourism.html#cb255-9)    ols = min_trace(base, method = "ols"),
    [](tourism.html#cb255-10)    mint = min_trace(base, method = "mint_shrink")
    [](tourism.html#cb255-11)  )

Here, `fit` contains the `base` ETS model (discussed in Chapter [8](expsmooth.html#expsmooth)) for each series in `tourism_full`, along with the three methods for producing coherent forecasts as specified in the `reconcile()` function.
    
    
    [](tourism.html#cb256-1)fc <- fit |> forecast(h = "2 years")

Passing `fit` into `forecast()` generates base and coherent forecasts across all the series in the aggregation structure. Figures [11.12](tourism.html#fig:tourism-states) and [11.13](tourism.html#fig:tourism-purpose) plot the four point forecasts for the overnight trips for the Australian total, the states, and the purposes of travel, along with the actual observations of the test set.
    
    
    [](tourism.html#cb257-1)fc |>
    [](tourism.html#cb257-2)  filter(is_aggregated(Region), is_aggregated(Purpose)) |>
    [](tourism.html#cb257-3)  autoplot(
    [](tourism.html#cb257-4)    tourism_full |> filter(year(Quarter) >= 2011),
    [](tourism.html#cb257-5)    level = NULL
    [](tourism.html#cb257-6)  ) +
    [](tourism.html#cb257-7)  labs(y = "Trips ('000)") +
    [](tourism.html#cb257-8)  facet_wrap(vars(State), scales = "free_y")

Figure 11.12: Forecasts of overnight trips for Australia and its states over the test period 2016Q1–2017Q4. 
    
    
    [](tourism.html#cb258-1)fc |>
    [](tourism.html#cb258-2)  filter(is_aggregated(State), !is_aggregated(Purpose)) |>
    [](tourism.html#cb258-3)  autoplot(
    [](tourism.html#cb258-4)    tourism_full |> filter(year(Quarter) >= 2011),
    [](tourism.html#cb258-5)    level = NULL
    [](tourism.html#cb258-6)  ) +
    [](tourism.html#cb258-7)  labs(y = "Trips ('000)") +
    [](tourism.html#cb258-8)  facet_wrap(vars(Purpose), scales = "free_y")

Figure 11.13: Forecasts of overnight trips by purpose of travel over the test period 2016Q1–2017Q4. 

To make it easier to see the differences, we have included only the last five years of the training data, and have omitted the prediction intervals. In most panels, the increase in overnight trips, especially in the second half of the test set, is higher than what is predicted by the point forecasts. This is particularly noticeable for the mainland eastern states of ACT, New South Wales, Queensland and Victoria, and across all purposes of travel.

The accuracy of the forecasts over the test set can be evaluated using the `accuracy()` function. We summarise some results in Table [11.2](tourism.html#tab:tourism-evaluation) using RMSE and MASE.

Table 11.2: Accuracy of forecasts for Australian overnight trips over the test set 2016Q1–2017Q4.  |  RMSE  |  MASE   
---|---|---  
|  Base  |  Bottom-up  |  MinT  |  OLS  |  Base  |  Bottom-up  |  MinT  |  OLS   
Total  |  1720.72  |  3071.11  |  2157.55  |  1803.51  |  1.53  |  3.17  |  2.09  |  1.63   
Purpose  |  533.02  |  802.68  |  586.45  |  513.18  |  1.33  |  2.32  |  1.51  |  1.25   
State  |  306.85  |  417.21  |  329.74  |  294.66  |  1.40  |  1.88  |  1.45  |  1.27   
Regions  |  52.64  |  55.13  |  47.40  |  46.95  |  1.13  |  1.18  |  1.02  |  1.00   
Bottom  |  19.38  |  19.38  |  17.97  |  18.32  |  0.98  |  0.98  |  0.94  |  1.02   
All series  |  45.96  |  55.28  |  45.61  |  43.19  |  1.04  |  1.08  |  0.98  |  1.03   
  
The scales of the series at different levels of aggregation are quite different, due to aggregation. Hence, we need to be cautious when comparing or calculating scale dependent error measures, such as the RMSE, across levels as the aggregate series will dominate. Therefore, we compare error measures across each level of aggregation, before providing the error measures across all the series in the bottom-row. Notice, that the RMSE increases as we go from the bottom level to the aggregate levels above.

The following code generates the accuracy measures for the aggregate series shown in the first row of the table. Similar code is used to evaluate forecasts for other levels.
    
    
    [](tourism.html#cb259-1)fc |>
    [](tourism.html#cb259-2)  filter(is_aggregated(State), is_aggregated(Purpose)) |>
    [](tourism.html#cb259-3)  accuracy(
    [](tourism.html#cb259-4)    data = tourism_full,
    [](tourism.html#cb259-5)    measures = list(rmse = RMSE, mase = MASE)
    [](tourism.html#cb259-6)  ) |>
    [](tourism.html#cb259-7)  group_by(.model) |>
    [](tourism.html#cb259-8)  summarise(rmse = mean(rmse), mase = mean(mase))
    [](tourism.html#cb259-9)#> # A tibble: 4 × 3
    [](tourism.html#cb259-10)#>   .model  rmse  mase
    [](tourism.html#cb259-11)#>   <chr>  <dbl> <dbl>
    [](tourism.html#cb259-12)#> 1 base   1721.  1.53
    [](tourism.html#cb259-13)#> 2 bu     3071.  3.17
    [](tourism.html#cb259-14)#> 3 mint   2158.  2.09
    [](tourism.html#cb259-15)#> 4 ols    1804.  1.63

Reconciling the base forecasts using OLS and MinT results in more accurate forecasts compared to the bottom-up approach. This result is commonly observed in applications as reconciliation approaches use information from all levels of the structure, resulting in more accurate coherent forecasts compared to the older traditional methods which use limited information. Furthermore, reconciliation usually improves the incoherent base forecasts for almost all levels.


---

## 11.5 Reconciled distributional forecasts[](rec-prob.html#rec-prob)

So far we have only discussed the reconciliation of point forecasts. However, we are usually also interested in the forecast distributions so that we can compute prediction intervals.

Panagiotelis et al. ([2023](rec-prob.html#ref-PanEtAl2020_Probabilistic)) present several important results for generating reconciled probabilistic forecasts. We focus here on two fundamental results that are implemented in the `reconcile()` function.

  1. If the base forecasts are normally distributed, i.e., \\[ \hat{\bm{y}}_h\sim N(\hat{\bm\mu}_h,\hat{\bm\Sigma}_h), \\] then the reconciled forecasts are also normally distributed, \\[ \tilde{\bm{y}}_h \sim N(\bm{S}\bm{G}\hat{\bm{\mu}}_h,\bm{S}\bm{G}\hat{\bm{\Sigma}}_{h}\bm{G}'\bm{S}'). \\]

  2. If it is unreasonable to assume normality for the base forecasts, we can use bootstrapping. Bootstrapped prediction intervals were introduced in Section [5.5](prediction-intervals.html#prediction-intervals). The same idea can be used here. We can simulate future sample paths from the model(s) that produce the base forecasts, and then reconcile these sample paths. Coherent prediction intervals can be computed from the reconciled sample paths.

Suppose that \\((\hat{\bm{y}}_h^{[1]},\dots,\hat{\bm{y}}_h^{[B]})\\) are a set of \\(B\\) simulated sample paths, generated independently from the models used to produce the base forecasts. Then \\((\bm{S}\bm{G}\hat{\bm{y}}_h^{[1]},\dots,\bm{S}\bm{G}\hat{\bm{y}}_h^{[B]})\\) provides a set of reconciled sample paths, from which percentiles can be calculated in order to construct coherent prediction intervals.

To generate bootstrapped prediction intervals in this way, we simply set `bootstrap = TRUE` in the `forecast()` function.


### Bibliography[](bibliography.html#bibliography)

Panagiotelis, A., Gamakumara, P., Athanasopoulos, G., & Hyndman, R. J. (2023). Probabilistic forecast reconciliation: Properties, evaluation and score optimisation. _European J Operational Research_ , _306_(2), 693–706. [__](https://doi.org/10.1016/j.ejor.2022.07.040)


---

## 11.6 Forecasting Australian prison population[](prison.html#prison)

Returning to the Australian prison population data (Section [11.1](hts.html#hts)), we will compare the forecasts from bottom-up and MinT methods applied to base ETS models, using a test set comprising the final two years or eight quarters 2015Q1–2016Q4 of the available data.
    
    
    [](prison.html#cb260-1)fit <- prison_gts |>
    [](prison.html#cb260-2)  filter(year(Quarter) <= 2014) |>
    [](prison.html#cb260-3)  model(base = ETS(Count)) |>
    [](prison.html#cb260-4)  reconcile(
    [](prison.html#cb260-5)    bottom_up = bottom_up(base),
    [](prison.html#cb260-6)    MinT = min_trace(base, method = "mint_shrink")
    [](prison.html#cb260-7)  )
    [](prison.html#cb260-8)fc <- fit |> forecast(h = 8)
    
    
    [](prison.html#cb261-1)fc |>
    [](prison.html#cb261-2)  filter(is_aggregated(State), is_aggregated(Gender),
    [](prison.html#cb261-3)         is_aggregated(Legal)) |>
    [](prison.html#cb261-4)  autoplot(prison_gts, alpha = 0.7, level = 90) +
    [](prison.html#cb261-5)  labs(y = "Number of prisoners ('000)",
    [](prison.html#cb261-6)       title = "Australian prison population (total)")

Figure 11.14: Forecasts for the total Australian quarterly adult prison population for the period 2015Q1–2016Q4. 

Figure [11.14](prison.html#fig:prisonforecasts-aggregate) shows the three sets of forecasts for the aggregate Australian prison population. The base and bottom-up forecasts from the ETS models seem to underestimate the trend over the test period. The MinT approach combines information from all the base forecasts in the aggregation structure; in this case, the base forecasts at the top level are adjusted upwards.

The MinT reconciled prediction intervals are much tighter than the base forecasts, due to MinT being based on an estimator that minimizes variances. The base forecast distributions are also incoherent, and therefore carry with them the extra uncertainty of the incoherency error.

We exclude the bottom-up forecasts from the remaining plots in order to simplify the visual exploration. However, we do revisit their accuracy in the evaluation results presented later.

Figures [11.15](prison.html#fig:prisonforecasts-State)–[11.17](prison.html#fig:prisonforecasts-bottom) show the MinT and base forecasts at various levels of aggregation. To make it easier to see the effect, we only show the last five years of training data. In general, MinT adjusts the base forecasts in the direction of the test set, hence improving the forecast accuracy. There is no guarantee that MinT reconciled forecasts will be more accurate than the base forecasts for every series, but they will be more accurate on average (see [Panagiotelis et al., 2021](prison.html#ref-PanEtAl2020_Geometry)).
    
    
    [](prison.html#cb262-1)fc |>
    [](prison.html#cb262-2)  filter(
    [](prison.html#cb262-3)    .model %in% c("base", "MinT"),
    [](prison.html#cb262-4)    !is_aggregated(State), is_aggregated(Legal),
    [](prison.html#cb262-5)    is_aggregated(Gender)
    [](prison.html#cb262-6)  ) |>
    [](prison.html#cb262-7)  autoplot(
    [](prison.html#cb262-8)    prison_gts |> filter(year(Quarter) >= 2010),
    [](prison.html#cb262-9)    alpha = 0.7, level = 90
    [](prison.html#cb262-10)  ) +
    [](prison.html#cb262-11)  labs(title = "Prison population (by state)",
    [](prison.html#cb262-12)       y = "Number of prisoners ('000)") +
    [](prison.html#cb262-13)  facet_wrap(vars(State), scales = "free_y", ncol = 4) +
    [](prison.html#cb262-14)  theme(axis.text.x = element_text(angle = 90, hjust = 1))

Figure 11.15: Forecasts for the Australian quarterly adult prison population, disaggregated by state. 

Figure [11.15](prison.html#fig:prisonforecasts-State) shows forecasts for each of the eight states. There is a general upward trend during the test set period across all the states. However, there appears to be a relatively large and sudden surge in New South Wales and Tasmania, which means the test set observations are well outside the upper bound of the forecast intervals for both these states. Because New South Wales is the state with the largest prison population, this surge will have a substantial impact on the total. In contrast, Victoria shows a substantial dip in 2015Q2–2015Q3, before returning to an upward trend. This dip is not captured in any of the Victorian forecasts.

Figure 11.16: Forecasts for the Australian quarterly adult prison population, disaggregated by legal status and by gender. 

Figure 11.17: Forecasts for bottom-level series the Australian quarterly adult prison population, disaggregated by state, by legal status and by gender. 

Figure [11.17](prison.html#fig:prisonforecasts-bottom) shows the forecasts for some selected bottom-level series of the Australian prison population. The four largest states are represented across the columns, with legal status and gender down the rows. These allow for some interesting analysis and observations that have policy implications. The large increase observed across the states during the 2015Q1–2016Q4 test period appears to be driven by large increases in the remand prison population. These increases seem to be generally missed by both forecasts. In contrast to the other states, for New South Wales there is also a substantial increase in the sentenced prison population. In particular, the increase in numbers of sentenced males in NSW contributes substantially to the rise in state and national prison numbers.

Using the `accuracy()` function, we evaluate the forecast accuracy across the grouped structure. The code below evaluates the forecast accuracy for only the top-level national aggregate of the Australian prison population time series. Similar code is used for the rest of the results shown in Table [11.3](prison.html#tab:tab-crime-evaluation).
    
    
    [](prison.html#cb263-1)fc |>
    [](prison.html#cb263-2)  filter(is_aggregated(State), is_aggregated(Gender),
    [](prison.html#cb263-3)         is_aggregated(Legal)) |>
    [](prison.html#cb263-4)  accuracy(data = prison_gts,
    [](prison.html#cb263-5)           measures = list(mase = MASE,
    [](prison.html#cb263-6)                           ss = skill_score(CRPS)
    [](prison.html#cb263-7)                           )
    [](prison.html#cb263-8)           ) |>
    [](prison.html#cb263-9)  group_by(.model) |>
    [](prison.html#cb263-10)  summarise(mase = mean(mase), sspc = mean(ss) * 100)
    [](prison.html#cb263-11)#> # A tibble: 3 × 3
    [](prison.html#cb263-12)#>   .model     mase  sspc
    [](prison.html#cb263-13)#>   <chr>     <dbl> <dbl>
    [](prison.html#cb263-14)#> 1 MinT      0.895  76.8
    [](prison.html#cb263-15)#> 2 base      1.72   55.9
    [](prison.html#cb263-16)#> 3 bottom_up 1.84   33.5

Table [11.3](prison.html#tab:tab-crime-evaluation) summarises the accuracy of the base, bottom-up and the MinT reconciled forecasts over the 2015Q1–2016Q4 test period across each of the levels of the grouped aggregation structure as well as all the levels.

Table 11.3: Accuracy of Australian prison population forecasts for different groups of series.  |  MASE  |  Skill Score (CRPS)   
---|---|---  
|  Base  |  Bottom-up  |  MinT  |  Base  |  Bottom-up  |  MinT   
Total  |  1.72  |  1.84  |  0.90  |  55.91  |  33.46  |  76.80   
State  |  2.12  |  1.88  |  1.78  |  6.40  |  24.10  |  22.46   
Legal status  |  2.89  |  2.68  |  2.32  |  22.22  |  50.27  |  45.23   
Gender  |  0.89  |  1.76  |  0.91  |  68.98  |  27.49  |  71.06   
Bottom  |  2.23  |  2.23  |  2.06  |  0.93  |  0.93  |  -3.23   
All series  |  2.19  |  2.16  |  1.96  |  6.70  |  11.29  |  8.69   
  
We use scaled measures because the numbers of prisoners vary substantially across the groups. The MASE gives a scaled measure of point-forecast accuracy (see Section [5.8](accuracy.html#accuracy)), while the CRPS skill score gives a scaled measure of distributional forecast accuracy (see Section [5.9](distaccuracy.html#distaccuracy)). A low value of MASE indicates a good forecast, while a high value of the skill score indicates a good forecast.

The results show that the MinT reconciled forecasts improve on the accuracy of the base forecasts and are also more accurate than the bottom-up forecasts. As the MinT optimal reconciliation approach uses information from all levels in the structure, it generates more accurate forecasts than the traditional approaches (such as bottom-up) which use limited information.

### Bibliography[](bibliography.html#bibliography)

Panagiotelis, A., Athanasopoulos, G., Gamakumara, P., & Hyndman, R. J. (2021). Forecast reconciliation: A geometric view with new insights on bias correction. _International Journal of Forecasting_ , _37_(1), 343–359. [__](https://doi.org/10.1016/j.ijforecast.2020.06.004)


---

## 11.7 Exercises[](hierarchical-exercises.html#hierarchical-exercises)

  1. Consider the `PBS` data which has aggregation structure `ATC1/ATC2 * Concession * Type`.

     1. Produce plots of the aggregated Scripts data by `Concession`, `Type` and `ATC1`.
     2. Forecast the PBS Scripts data using ETS, ARIMA and SNAIVE models, applied to all but the last three years of data.
     3. Reconcile each of the forecasts using MinT.
     4. Which type of model works best on the test set?
     5. Does the reconciliation improve the forecast accuracy?
     6. Why doesn’t the reconciliation make any difference to the SNAIVE forecasts?
  2. Repeat the `tourism` example from Section [11.4](tourism.html#tourism), but also evaluate the forecast distribution accuracy using CRPS skill scores. Which method does best on this measure?

  3. Repeat the `prison` example from Section [11.6](prison.html#prison), but using a bootstrap to generate the forecast distributions rather than assuming normality. Does it make much difference to the CRPS skill scores?




---

## 11.8 Further reading[](hierarchical-reading.html#hierarchical-reading)

There are no other textbooks which cover hierarchical forecasting in any depth, so interested readers will need to tackle the original research papers for further information.

  * Gross & Sohl ([1990](hierarchical-reading.html#ref-GroSoh1990)) provide a good introduction to the top-down approaches.
  * A recent survey of forecast reconciliation is provided by Athanasopoulos et al. ([2020](hierarchical-reading.html#ref-macrohts)).
  * The reconciliation methods were developed in a series of papers. The later papers summarise previous results and present the most general theory: Wickramasuriya et al. ([2019](hierarchical-reading.html#ref-Mint)), Panagiotelis et al. ([2021](hierarchical-reading.html#ref-PanEtAl2020_Geometry)), Panagiotelis et al. ([2023](hierarchical-reading.html#ref-PanEtAl2020_Probabilistic)).
  * Athanasopoulos et al. ([2017](hierarchical-reading.html#ref-AthEtAl2017)) extends the reconciliation approach to deal with temporal hierarchies.
  * The tourism example is discussed in more detail in Athanasopoulos et al. ([2009](hierarchical-reading.html#ref-AthEtAl2009)), Wickramasuriya et al. ([2019](hierarchical-reading.html#ref-Mint)), and Kourentzes & Athanasopoulos ([2019](hierarchical-reading.html#ref-KouAth2019)).


### Bibliography[](bibliography.html#bibliography)

Athanasopoulos, G., Ahmed, R. A., & Hyndman, R. J. (2009). Hierarchical forecasts for Australian domestic tourism. _International Journal of Forecasting_ , _25_ , 146–166. [__](https://doi.org/10.1016/j.ijforecast.2008.07.004)

Athanasopoulos, G., Gamakumara, P., Panagiotelis, A., Hyndman, R. J., & Affan, M. (2020). Hierarchical forecasting. In P. Fuleky (Ed.), _Macroeconomic forecasting in the era of big data_ (pp. 689–719). Springer. [__](https://doi.org/10.1007/978-3-030-31150-6_21)

Athanasopoulos, G., Hyndman, R. J., Kourentzes, N., & Petropoulos, F. (2017). Forecasting with temporal hierarchies. _European Journal of Operational Research_ , _262_(1), 60–74. [__](https://doi.org/10.1016/j.ejor.2017.02.046)

Gross, C. W., & Sohl, J. E. (1990). Disaggregation methods to expedite product line forecasting. _Journal of Forecasting_ , _9_ , 233–254. [__](https://doi.org/10.1002/for.3980090304)

Kourentzes, N., & Athanasopoulos, G. (2019). Cross-temporal coherent forecasts for Australian tourism. _Annals of Tourism Research_ , _75_ , 393–409. [__](https://doi.org/10.1016/j.annals.2019.02.001)

Panagiotelis, A., Athanasopoulos, G., Gamakumara, P., & Hyndman, R. J. (2021). Forecast reconciliation: A geometric view with new insights on bias correction. _International Journal of Forecasting_ , _37_(1), 343–359. [__](https://doi.org/10.1016/j.ijforecast.2020.06.004)

Panagiotelis, A., Gamakumara, P., Athanasopoulos, G., & Hyndman, R. J. (2023). Probabilistic forecast reconciliation: Properties, evaluation and score optimisation. _European J Operational Research_ , _306_(2), 693–706. [__](https://doi.org/10.1016/j.ejor.2022.07.040)

Wickramasuriya, S. L., Athanasopoulos, G., & Hyndman, R. J. (2019). Optimal forecast reconciliation for hierarchical and grouped time series through trace minimization. _Journal of the American Statistical Association_ , _114_(526), 804–819. [__](https://doi.org/10.1080/01621459.2018.1448825)


---

# Chapter 12 Advanced forecasting methods[](advanced.html#advanced)

In this chapter, we briefly discuss several more advanced forecasting methods that build on the models discussed in earlier chapters.


---

## 12.1 Complex seasonality[](complexseasonality.html#complexseasonality)

So far, we have mostly considered relatively simple seasonal patterns such as quarterly and monthly data. However, higher frequency time series often exhibit more complicated seasonal patterns. For example, daily data may have a weekly pattern as well as an annual pattern. Hourly data usually has three types of seasonality: a daily pattern, a weekly pattern, and an annual pattern. Even weekly data can be challenging to forecast as there are not a whole number of weeks in a year, so the annual pattern has a seasonal period of \\(365.25/7\approx 52.179\\) on average. Most of the methods we have considered so far are unable to deal with these seasonal complexities.

We don’t necessarily want to include all of the possible seasonal periods in our models — just the ones that are likely to be present in the data. For example, if we have only 180 days of data, we may ignore the annual seasonality. If the data are measurements of a natural phenomenon (e.g., temperature), we can probably safely ignore any weekly seasonality.

Figure [12.1](complexseasonality.html#fig:calls) shows the number of calls to a North American commercial bank per 5-minute interval between 7:00am and 9:05pm each weekday over a 33 week period. The lower panel shows the first four weeks of the same time series. There is a strong daily seasonal pattern with period 169 (there are 169 5-minute intervals per day), and a weak weekly seasonal pattern with period \\(169 \times 5=845\\). (Call volumes on Mondays tend to be higher than the rest of the week.) If a longer series of data were available, we may also have observed an annual seasonal pattern.
    
    
    [](complexseasonality.html#cb264-1)bank_calls |>
    [](complexseasonality.html#cb264-2)  fill_gaps() |>
    [](complexseasonality.html#cb264-3)  autoplot(Calls) +
    [](complexseasonality.html#cb264-4)  labs(y = "Calls",
    [](complexseasonality.html#cb264-5)       title = "Five-minute call volume to bank")

Figure 12.1: Five-minute call volume handled on weekdays between 7:00am and 9:05pm in a large North American commercial bank. Top panel: data from 3 March – 24 October 2003. Bottom panel: first four weeks of data. 

Apart from the multiple seasonal periods, this series has the additional complexity of missing values between the working periods.

### STL with multiple seasonal periods[](complexseasonality.html#stl-with-multiple-seasonal-periods)

The `STL()` function is designed to deal with multiple seasonality. It will return multiple seasonal components, as well as a trend and remainder component. In this case, we need to re-index the tsibble to avoid the missing values, and then explicitly give the seasonal periods.
    
    
    [](complexseasonality.html#cb265-1)calls <- bank_calls |>
    [](complexseasonality.html#cb265-2)  mutate(t = row_number()) |>
    [](complexseasonality.html#cb265-3)  update_tsibble(index = t, regular = TRUE)
    
    
    [](complexseasonality.html#cb266-1)calls |>
    [](complexseasonality.html#cb266-2)  model(
    [](complexseasonality.html#cb266-3)    STL(sqrt(Calls) ~ season(period = 169) +
    [](complexseasonality.html#cb266-4)                      season(period = 5*169),
    [](complexseasonality.html#cb266-5)        robust = TRUE)
    [](complexseasonality.html#cb266-6)  ) |>
    [](complexseasonality.html#cb266-7)  components() |>
    [](complexseasonality.html#cb266-8)  autoplot() + labs(x = "Observation")

Figure 12.2: STL decomposition with multiple seasonality for the call volume data. 

There are two seasonal patterns shown, one for the time of day (the third panel), and one for the time of week (the fourth panel). To properly interpret this graph, it is important to notice the vertical scales. In this case, the trend and the weekly seasonality have wider bars (and therefore relatively narrower ranges) compared to the other components, because there is little trend seen in the data, and the weekly seasonality is weak.

The decomposition can also be used in forecasting, with each of the seasonal components forecast using a seasonal naïve method, and the seasonally adjusted data forecast using ETS.

The code is slightly more complicated than usual because we have to add back the time stamps that were lost when we re-indexed the tsibble to handle the periods of missing observations. The square root transformation used in the STL decomposition has ensured the forecasts remain positive.
    
    
    [](complexseasonality.html#cb267-1)# Forecasts from STL+ETS decomposition
    [](complexseasonality.html#cb267-2)my_dcmp_spec <- decomposition_model(
    [](complexseasonality.html#cb267-3)  STL(sqrt(Calls) ~ season(period = 169) +
    [](complexseasonality.html#cb267-4)                    season(period = 5*169),
    [](complexseasonality.html#cb267-5)      robust = TRUE),
    [](complexseasonality.html#cb267-6)  ETS(season_adjust ~ season("N"))
    [](complexseasonality.html#cb267-7))
    [](complexseasonality.html#cb267-8)fc <- calls |>
    [](complexseasonality.html#cb267-9)  model(my_dcmp_spec) |>
    [](complexseasonality.html#cb267-10)  forecast(h = 5 * 169)
    [](complexseasonality.html#cb267-11)
    [](complexseasonality.html#cb267-12)# Add correct time stamps to fable
    [](complexseasonality.html#cb267-13)fc_with_times <- bank_calls |>
    [](complexseasonality.html#cb267-14)  new_data(n = 7 * 24 * 60 / 5) |>
    [](complexseasonality.html#cb267-15)  mutate(time = format(DateTime, format = "%H:%M:%S")) |>
    [](complexseasonality.html#cb267-16)  filter(
    [](complexseasonality.html#cb267-17)    time %in% format(bank_calls$DateTime, format = "%H:%M:%S"),
    [](complexseasonality.html#cb267-18)    wday(DateTime, week_start = 1) <= 5
    [](complexseasonality.html#cb267-19)  ) |>
    [](complexseasonality.html#cb267-20)  mutate(t = row_number() + max(calls$t)) |>
    [](complexseasonality.html#cb267-21)  left_join(fc, by = "t") |>
    [](complexseasonality.html#cb267-22)  as_fable(response = "Calls", distribution = Calls)
    [](complexseasonality.html#cb267-23)
    [](complexseasonality.html#cb267-24)# Plot results with last 3 weeks of data
    [](complexseasonality.html#cb267-25)fc_with_times |>
    [](complexseasonality.html#cb267-26)  fill_gaps() |>
    [](complexseasonality.html#cb267-27)  autoplot(bank_calls |> tail(14 * 169) |> fill_gaps()) +
    [](complexseasonality.html#cb267-28)  labs(y = "Calls",
    [](complexseasonality.html#cb267-29)       title = "Five-minute call volume to bank")

Figure 12.3: Forecasts of the call volume data using an STL decomposition with the seasonal components forecast using a seasonal naïve method, and the seasonally adjusted data forecast using ETS. 

### Dynamic harmonic regression with multiple seasonal periods[](complexseasonality.html#dynamic-harmonic-regression-with-multiple-seasonal-periods)

With multiple seasonalities, we can use Fourier terms as we did in earlier chapters (see Sections [7.4](useful-predictors.html#useful-predictors) and [10.5](dhr.html#dhr)). Because there are multiple seasonalities, we need to add Fourier terms for each seasonal period. In this case, the seasonal periods are 169 and 845, so the Fourier terms are of the form \\[ \sin\left(\frac{2\pi kt}{169}\right), \quad \cos\left(\frac{2\pi kt}{169}\right), \quad \sin\left(\frac{2\pi kt}{845}\right), \quad \text{and} \quad \cos\left(\frac{2\pi kt}{845}\right), \\] for \\(k=1,2,\dots\\). As usual, the `fourier()` function can generate these for you.

We will fit a dynamic harmonic regression model with an ARIMA error structure. The total number of Fourier terms for each seasonal period could be selected to minimise the AICc. However, for high seasonal periods, this tends to over-estimate the number of terms required, so we will use a more subjective choice with 10 terms for the daily seasonality and 5 for the weekly seasonality. Again, we will use a square root transformation to ensure the forecasts and prediction intervals remain positive. We set \\(D=d=0\\) in order to handle the non-stationarity through the regression terms, and \\(P=Q=0\\) in order to handle the seasonality through the regression terms.
    
    
    [](complexseasonality.html#cb268-1)fit <- calls |>
    [](complexseasonality.html#cb268-2)  model(
    [](complexseasonality.html#cb268-3)    dhr = ARIMA(sqrt(Calls) ~ PDQ(0, 0, 0) + pdq(d = 0) +
    [](complexseasonality.html#cb268-4)                  fourier(period = 169, K = 10) +
    [](complexseasonality.html#cb268-5)                  fourier(period = 5*169, K = 5)))
    [](complexseasonality.html#cb268-6)
    [](complexseasonality.html#cb268-7)fc <- fit |> forecast(h = 5 * 169)
    [](complexseasonality.html#cb268-8)
    [](complexseasonality.html#cb268-9)# Add correct time stamps to fable
    [](complexseasonality.html#cb268-10)fc_with_times <- bank_calls |>
    [](complexseasonality.html#cb268-11)  new_data(n = 7 * 24 * 60 / 5) |>
    [](complexseasonality.html#cb268-12)  mutate(time = format(DateTime, format = "%H:%M:%S")) |>
    [](complexseasonality.html#cb268-13)  filter(
    [](complexseasonality.html#cb268-14)    time %in% format(bank_calls$DateTime, format = "%H:%M:%S"),
    [](complexseasonality.html#cb268-15)    wday(DateTime, week_start = 1) <= 5
    [](complexseasonality.html#cb268-16)  ) |>
    [](complexseasonality.html#cb268-17)  mutate(t = row_number() + max(calls$t)) |>
    [](complexseasonality.html#cb268-18)  left_join(fc, by = "t") |>
    [](complexseasonality.html#cb268-19)  as_fable(response = "Calls", distribution = Calls)
    
    
    [](complexseasonality.html#cb269-1)# Plot results with last 3 weeks of data
    [](complexseasonality.html#cb269-2)fc_with_times |>
    [](complexseasonality.html#cb269-3)  fill_gaps() |>
    [](complexseasonality.html#cb269-4)  autoplot(bank_calls |> tail(14 * 169) |> fill_gaps()) +
    [](complexseasonality.html#cb269-5)  labs(y = "Calls",
    [](complexseasonality.html#cb269-6)       title = "Five-minute call volume to bank")

Figure 12.4: Forecasts from a dynamic harmonic regression applied to the call volume data. 

This is a large model, containing 33 parameters: 4 ARMA coefficients, 20 Fourier coefficients for period 169, and 8 Fourier coefficients for period 845. Not all of the Fourier terms for period 845 are used because there is some overlap with the terms of period 169 (since \\(845=5\times169\\)).

### Example: Electricity demand[](complexseasonality.html#example-electricity-demand)

One common application of such models is electricity demand modelling. Figure [12.5](complexseasonality.html#fig:elecdemand) shows half-hourly electricity demand (MWh) in Victoria, Australia, during 2012–2014, along with temperatures (degrees Celsius) for the same period for Melbourne (the largest city in Victoria).
    
    
    [](complexseasonality.html#cb270-1)vic_elec |>
    [](complexseasonality.html#cb270-2)  pivot_longer(Demand:Temperature, names_to = "Series") |>
    [](complexseasonality.html#cb270-3)  ggplot(aes(x = Time, y = value)) +
    [](complexseasonality.html#cb270-4)  geom_line() +
    [](complexseasonality.html#cb270-5)  facet_grid(rows = vars(Series), scales = "free_y") +
    [](complexseasonality.html#cb270-6)  labs(y = "")

Figure 12.5: Half-hourly electricity demand and corresponding temperatures in 2012–2014, Victoria, Australia. 

Plotting electricity demand against temperature (Figure [12.6](complexseasonality.html#fig:elecdemand2)) shows that there is a nonlinear relationship between the two, with demand increasing for low temperatures (due to heating) and increasing for high temperatures (due to cooling).
    
    
    [](complexseasonality.html#cb271-1)elec <- vic_elec |>
    [](complexseasonality.html#cb271-2)  mutate(
    [](complexseasonality.html#cb271-3)    DOW = wday(Date, label = TRUE),
    [](complexseasonality.html#cb271-4)    Working_Day = !Holiday & !(DOW %in% c("Sat", "Sun")),
    [](complexseasonality.html#cb271-5)    Cooling = pmax(Temperature, 18)
    [](complexseasonality.html#cb271-6)  )
    [](complexseasonality.html#cb271-7)elec |>
    [](complexseasonality.html#cb271-8)  ggplot(aes(x=Temperature, y=Demand, col=Working_Day)) +
    [](complexseasonality.html#cb271-9)  geom_point(alpha = 0.6) +
    [](complexseasonality.html#cb271-10)  labs(x="Temperature (degrees Celsius)", y="Demand (MWh)")

Figure 12.6: Half-hourly electricity demand for Victoria, plotted against temperatures for the same times in Melbourne, the largest city in Victoria. 

We will fit a regression model with a piecewise linear function of temperature (containing a knot at 18 degrees), and harmonic regression terms to allow for the daily seasonal pattern. Again, we set the orders of the Fourier terms subjectively, while using the AICc to select the order of the ARIMA errors.
    
    
    [](complexseasonality.html#cb272-1)fit <- elec |>
    [](complexseasonality.html#cb272-2)  model(
    [](complexseasonality.html#cb272-3)    ARIMA(Demand ~ PDQ(0, 0, 0) + pdq(d = 0) +
    [](complexseasonality.html#cb272-4)          Temperature + Cooling + Working_Day +
    [](complexseasonality.html#cb272-5)          fourier(period = "day", K = 10) +
    [](complexseasonality.html#cb272-6)          fourier(period = "week", K = 5) +
    [](complexseasonality.html#cb272-7)          fourier(period = "year", K = 3))
    [](complexseasonality.html#cb272-8)  )

Forecasting with such models is difficult because we require future values of the predictor variables. Future values of the Fourier terms are easy to compute, but future temperatures are, of course, unknown. If we are only interested in forecasting up to a week ahead, we could use temperature forecasts obtained from a meteorological model. Alternatively, we could use scenario forecasting (Section [6.5](scenarios.html#scenarios)) and plug in possible temperature patterns. In the following example, we have used a repeat of the last two days of temperatures to generate future possible demand values.
    
    
    [](complexseasonality.html#cb273-1)elec_newdata <- new_data(elec, 2*48) |>
    [](complexseasonality.html#cb273-2)  mutate(
    [](complexseasonality.html#cb273-3)    Temperature = tail(elec$Temperature, 2 * 48),
    [](complexseasonality.html#cb273-4)    Date = lubridate::as_date(Time),
    [](complexseasonality.html#cb273-5)    DOW = wday(Date, label = TRUE),
    [](complexseasonality.html#cb273-6)    Working_Day = (Date != "2015-01-01") &
    [](complexseasonality.html#cb273-7)                   !(DOW %in% c("Sat", "Sun")),
    [](complexseasonality.html#cb273-8)    Cooling = pmax(Temperature, 18)
    [](complexseasonality.html#cb273-9)  )
    [](complexseasonality.html#cb273-10)fc <- fit |>
    [](complexseasonality.html#cb273-11)  forecast(new_data = elec_newdata)
    [](complexseasonality.html#cb273-12)
    [](complexseasonality.html#cb273-13)fc |>
    [](complexseasonality.html#cb273-14)  autoplot(elec |> tail(10 * 48)) +
    [](complexseasonality.html#cb273-15)  labs(title="Half hourly electricity demand: Victoria",
    [](complexseasonality.html#cb273-16)       y = "Demand (MWh)", x = "Time [30m]")

Figure 12.7: Forecasts from a dynamic harmonic regression model applied to half-hourly electricity demand data. 

Although the short-term forecasts look reasonable, this is a crude model for a complicated process. The residuals, plotted in Figure [12.8](complexseasonality.html#fig:elecdemand5), demonstrate that there is a lot of information that has not been captured with this model.
    
    
    [](complexseasonality.html#cb274-1)fit |> gg_tsresiduals()

Figure 12.8: Residual diagnostics for the dynamic harmonic regression model. 

More sophisticated versions of this model which provide much better forecasts are described in Hyndman & Fan ([2010](complexseasonality.html#ref-HF2010)) and Fan & Hyndman ([2012](complexseasonality.html#ref-FH2012)).

### Bibliography[](bibliography.html#bibliography)

Fan, S., & Hyndman, R. J. (2012). Short-term load forecasting based on a semi-parametric additive model. _IEEE Transactions on Power Systems_ , _27_(1), 134–141. [__](https://doi.org/10.1109/TPWRS.2011.2162082)

Hyndman, R. J., & Fan, S. (2010). Density forecasting for long-term peak electricity demand. _IEEE Transactions on Power Systems_ , _25_(2), 1142–1153. [__](https://doi.org/10.1109/TPWRS.2009.2036017)


---

## 12.2 Prophet model[](prophet.html#prophet)

A recent proposal is the Prophet model, available via the `fable.prophet` package. This model was introduced by Facebook ([S. J. Taylor & Letham, 2018](prophet.html#ref-prophet)), originally for forecasting daily data with weekly and yearly seasonality, plus holiday effects. It was later extended to cover more types of seasonal data. It works best with time series that have strong seasonality and several seasons of historical data.

Prophet can be considered a nonlinear regression model (Chapter [7](regression.html#regression)), of the form \\[ y_t = g(t) + s(t) + h(t) + \varepsilon_t, \\] where \\(g(t)\\) describes a piecewise-linear trend (or “growth term”), \\(s(t)\\) describes the various seasonal patterns, \\(h(t)\\) captures the holiday effects, and \\(\varepsilon_t\\) is a white noise error term.

  * The knots (or changepoints) for the piecewise-linear trend are automatically selected if not explicitly specified. Optionally, a logistic function can be used to set an upper bound on the trend.
  * The seasonal component consists of Fourier terms of the relevant periods. By default, order 10 is used for annual seasonality and order 3 is used for weekly seasonality.
  * Holiday effects are added as simple dummy variables.
  * The model is estimated using a Bayesian approach to allow for automatic selection of the changepoints and other model characteristics.


We illustrate the approach using two data sets: a simple quarterly example, and then the electricity demand data described in the previous section.

### Example: Quarterly cement production[](prophet.html#example-quarterly-cement-production)

For the simple quarterly example, we will repeat the analysis from Section [9.10](arima-ets.html#arima-ets) in which we compared an ARIMA and ETS model, but we will add in a prophet model for comparison.
    
    
    [](prophet.html#cb275-1)library(fable.prophet)
    [](prophet.html#cb275-2)cement <- aus_production |>
    [](prophet.html#cb275-3)  filter(year(Quarter) >= 1988)
    [](prophet.html#cb275-4)train <- cement |>
    [](prophet.html#cb275-5)  filter(year(Quarter) <= 2007)
    [](prophet.html#cb275-6)fit <- train |>
    [](prophet.html#cb275-7)  model(
    [](prophet.html#cb275-8)    arima = ARIMA(Cement),
    [](prophet.html#cb275-9)    ets = ETS(Cement),
    [](prophet.html#cb275-10)    prophet = prophet(Cement ~ season(period = 4, order = 2,
    [](prophet.html#cb275-11)                                    type = "multiplicative"))
    [](prophet.html#cb275-12)  )

Note that the seasonal term must have the `period` fully specified for quarterly and monthly data, as the default values assume the data are observed at least daily.
    
    
    [](prophet.html#cb276-1)fc <- fit |> forecast(h = "2 years 6 months")
    [](prophet.html#cb276-2)fc |> autoplot(cement)

Figure 12.9: Prophet compared to ETS and ARIMA on the Cement production data, with a 10-quarter test set. 

In this example, the Prophet forecasts are worse than either the ETS or ARIMA forecasts.
    
    
    [](prophet.html#cb277-1)fc |> accuracy(cement)
    [](prophet.html#cb277-2)#> # A tibble: 3 × 10
    [](prophet.html#cb277-3)#>   .model  .type    ME  RMSE   MAE   MPE  MAPE  MASE RMSSE  ACF1
    [](prophet.html#cb277-4)#>   <chr>   <chr> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl>
    [](prophet.html#cb277-5)#> 1 arima   Test  -161.  216.  186. -7.71  8.68  1.27  1.26 0.387
    [](prophet.html#cb277-6)#> 2 ets     Test  -171.  222.  191. -8.07  8.85  1.30  1.29 0.579
    [](prophet.html#cb277-7)#> 3 prophet Test  -176.  248.  215. -8.36  9.89  1.47  1.44 0.698

### Example: Half-hourly electricity demand[](prophet.html#example-half-hourly-electricity-demand)

We will fit a similar model to the dynamic harmonic regression (DHR) model from the previous section, but this time using a Prophet model. For daily and sub-daily data, the default periods are correctly specified, so that we can simply specify the period using a character string as follows.
    
    
    [](prophet.html#cb278-1)fit <- elec |>
    [](prophet.html#cb278-2)  model(
    [](prophet.html#cb278-3)    prophet(Demand ~ Temperature + Cooling + Working_Day +
    [](prophet.html#cb278-4)            season(period = "day", order = 10) +
    [](prophet.html#cb278-5)            season(period = "week", order = 5) +
    [](prophet.html#cb278-6)            season(period = "year", order = 3))
    [](prophet.html#cb278-7)  )
    [](prophet.html#cb278-8)fit |>
    [](prophet.html#cb278-9)  components() |>
    [](prophet.html#cb278-10)  autoplot()

Figure 12.10: Components of a Prophet model fitted to the Victorian electricity demand data. 

Figure [12.10](prophet.html#fig:prophetelec) shows the trend and seasonal components of the fitted model.

The model specification is very similar to the DHR model in the previous section, although the result is different in several important ways. The Prophet model adds a piecewise linear time trend which is not really appropriate here as we don’t expect the long term forecasts to continue to follow the downward linear trend at the end of the series.

There is also substantial remaining autocorrelation in the residuals,
    
    
    [](prophet.html#cb279-1)fit |> gg_tsresiduals()

Figure 12.11: Residuals from the Prophet model for Victorian electricity demand. 

The prediction intervals would be narrower if the autocorrelations were taken into account.
    
    
    [](prophet.html#cb280-1)fc <- fit |>
    [](prophet.html#cb280-2)  forecast(new_data = elec_newdata)
    
    
    [](prophet.html#cb281-1)fc |>
    [](prophet.html#cb281-2)  autoplot(elec |> tail(10 * 48)) +
    [](prophet.html#cb281-3)  labs(x = "Date", y = "Demand (MWh)")

Figure 12.12: Two day forecasts from the Prophet model for Victorian electricity demand. 

Prophet has the advantage of being much faster to estimate than the DHR models we have considered previously, and it is completely automated. However, it rarely gives better forecast accuracy than the alternative approaches, as these two examples have illustrated.

### Bibliography[](bibliography.html#bibliography)

Taylor, S. J., & Letham, B. (2018). Forecasting at scale. _The American Statistician_ , _72_(1), 37–45. [__](https://doi.org/10.1080/00031305.2017.1380080)


---

## 12.3 Vector autoregressions[](VAR.html#VAR)

One limitation of the models that we have considered so far is that they impose a unidirectional relationship — the forecast variable is influenced by the predictor variables, but not vice versa. However, there are many cases where the reverse should also be allowed for — where all variables affect each other. In Section [10.2](regarima.html#regarima), the changes in personal consumption expenditure (\\(C_t\\)) were forecast based on the changes in personal disposable income (\\(I_t\\)). However, in this case a bi-directional relationship may be more suitable: an increase in \\(I_t\\) will lead to an increase in \\(C_t\\) and vice versa.

An example of such a situation occurred in Australia during the Global Financial Crisis of 2008–2009. The Australian government issued stimulus packages that included cash payments in December 2008, just in time for Christmas spending. As a result, retailers reported strong sales and the economy was stimulated. Consequently, incomes increased.

Such feedback relationships are allowed for in the vector autoregressive (VAR) framework. In this framework, all variables are treated symmetrically. They are all modelled as if they all influence each other equally. In more formal terminology, all variables are now treated as “endogenous”. To signify this, we now change the notation and write all variables as \\(y\\)s: \\(y_{1,t}\\) denotes the \\(t\\)th observation of variable \\(y_1\\), \\(y_{2,t}\\) denotes the \\(t\\)th observation of variable \\(y_2\\), and so on.

A VAR model is a generalisation of the univariate autoregressive model for forecasting a vector of time series.[26](VAR.html#fn26) It comprises one equation per variable in the system. The right hand side of each equation includes a constant and lags of all of the variables in the system. To keep it simple, we will consider a two variable VAR with one lag. We write a 2-dimensional VAR(1) model as \\[\begin{align} y_{1,t} &= c_1+\phi _{11,1}y_{1,t-1}+\phi _{12,1}y_{2,t-1}+\varepsilon_{1,t} \tag{12.1}\\\ y_{2,t} &= c_2+\phi _{21,1}y_{1,t-1}+\phi _{22,1}y_{2,t-1}+\varepsilon_{2,t}, \tag{12.2} \end{align}\\] where \\(\varepsilon_{1,t}\\) and \\(\varepsilon_{2,t}\\) are white noise processes that may be contemporaneously correlated. The coefficient \\(\phi_{ii,\ell}\\) captures the influence of the \\(\ell\\)th lag of variable \\(y_i\\) on itself, while the coefficient \\(\phi_{ij,\ell}\\) captures the influence of the \\(\ell\\)th lag of variable \\(y_j\\) on \\(y_i\\).

If the series are stationary, we forecast them by fitting a VAR to the data directly (known as a “VAR in levels”). If the series are non-stationary, we take differences of the data in order to make them stationary, then fit a VAR model (known as a “VAR in differences”). In both cases, the models are estimated equation by equation using the principle of least squares. For each equation, the parameters are estimated by minimising the sum of squared \\(\varepsilon_{i,t}\\) values.

The other possibility, which is beyond the scope of this book and therefore we do not explore here, is that the series may be non-stationary but cointegrated, which means that there exists a linear combination of them that is stationary. In this case, a VAR specification that includes an error correction mechanism (usually referred to as a vector error correction model) should be included, and alternative estimation methods to least squares estimation should be used.[27](VAR.html#fn27)

Forecasts are generated from a VAR in a recursive manner. The VAR generates forecasts for _each_ variable included in the system. To illustrate the process, assume that we have fitted the 2-dimensional VAR(1) model described in Equations [(12.1)](VAR.html#eq:var1a)–[(12.2)](VAR.html#eq:var1b), for all observations up to time \\(T\\). Then the one-step-ahead forecasts are generated by \\[\begin{align*} \hat y_{1,T+1|T} &=\hat{c}_1+\hat\phi_{11,1}y_{1,T}+\hat\phi_{12,1}y_{2,T} \\\ \hat y_{2,T+1|T} &=\hat{c}_2+\hat\phi _{21,1}y_{1,T}+\hat\phi_{22,1}y_{2,T}. \end{align*}\\] This is the same form as [(12.1)](VAR.html#eq:var1a)–[(12.2)](VAR.html#eq:var1b), except that the errors have been set to zero and parameters have been replaced with their estimates. For \\(h=2\\), the forecasts are given by \\[\begin{align*} \hat y_{1,T+2|T} &=\hat{c}_1+\hat\phi_{11,1}\hat y_{1,T+1|T}+\hat\phi_{12,1}\hat y_{2,T+1|T}\\\ \hat y_{2,T+2|T}&=\hat{c}_2+\hat\phi_{21,1}\hat y_{1,T+1|T}+\hat\phi_{22,1}\hat y_{2,T+1|T}. \end{align*}\\] Again, this is the same form as [(12.1)](VAR.html#eq:var1a)–[(12.2)](VAR.html#eq:var1b), except that the errors have been set to zero, the parameters have been replaced with their estimates, and the unknown values of \\(y_1\\) and \\(y_2\\) have been replaced with their forecasts. The process can be iterated in this manner for all future time periods.

There are two decisions one has to make when using a VAR to forecast, namely how many variables (denoted by \\(K\\)) and how many lags (denoted by \\(p\\)) should be included in the system. The number of coefficients to be estimated in a VAR is equal to \\(K+pK^2\\) (or \\(1+pK\\) per equation). For example, for a VAR with \\(K=5\\) variables and \\(p=3\\) lags, there are 16 coefficients per equation, giving a total of 80 coefficients to be estimated. The more coefficients that need to be estimated, the larger the estimation error entering the forecast.

In practice, it is usual to keep \\(K\\) small and include only variables that are correlated with each other, and therefore useful in forecasting each other. Information criteria are commonly used to select the number of lags to be included. Care should be taken when using the AICc as it tends to choose large numbers of lags; instead, for VAR models, we often use the BIC instead. A more sophisticated version of the model is a “sparse VAR” (where many coefficients are set to zero); another approach is to use “shrinkage estimation” (where coefficients are smaller).

A criticism that VARs face is that they are atheoretical; that is, they are not built on some economic theory that imposes a theoretical structure on the equations. Every variable is assumed to influence every other variable in the system, which makes a direct interpretation of the estimated coefficients difficult. Despite this, VARs are useful in several contexts:

  1. forecasting a collection of related variables where no explicit interpretation is required;
  2. testing whether one variable is useful in forecasting another (the basis of Granger causality tests);
  3. impulse response analysis, where the response of one variable to a sudden but temporary change in another variable is analysed;
  4. forecast error variance decomposition, where the proportion of the forecast variance of each variable is attributed to the effects of the other variables.


### Example: A VAR model for forecasting US consumption[](VAR.html#example-a-var-model-for-forecasting-us-consumption)
    
    
    [](VAR.html#cb282-1)fit <- us_change |>
    [](VAR.html#cb282-2)  model(
    [](VAR.html#cb282-3)    aicc = VAR(vars(Consumption, Income)),
    [](VAR.html#cb282-4)    bic = VAR(vars(Consumption, Income), ic = "bic")
    [](VAR.html#cb282-5)  )
    [](VAR.html#cb282-6)fit
    [](VAR.html#cb282-7)#> # A mable: 1 x 2
    [](VAR.html#cb282-8)#>               aicc              bic
    [](VAR.html#cb282-9)#>            <model>          <model>
    [](VAR.html#cb282-10)#> 1 <VAR(5) w/ mean> <VAR(1) w/ mean>
    
    
    [](VAR.html#cb283-1)glance(fit)
    [](VAR.html#cb283-2)#> # A tibble: 2 × 6
    [](VAR.html#cb283-3)#>   .model sigma2        log_lik   AIC  AICc   BIC
    [](VAR.html#cb283-4)#>   <chr>  <list>          <dbl> <dbl> <dbl> <dbl>
    [](VAR.html#cb283-5)#> 1 aicc   <dbl [2 × 2]>   -373.  798.  806.  883.
    [](VAR.html#cb283-6)#> 2 bic    <dbl [2 × 2]>   -408.  836.  837.  869.

A VAR(5) model is selected using the AICc (the default), while a VAR(1) model is selected using the BIC. This is not unusual — the BIC will always select a model that has fewer parameters than the AICc model as it imposes a stronger penalty for the number of parameters.
    
    
    [](VAR.html#cb284-1)fit |>
    [](VAR.html#cb284-2)  augment() |>
    [](VAR.html#cb284-3)  ACF(.innov) |>
    [](VAR.html#cb284-4)  autoplot()

Figure 12.13: ACF of the residuals from the two VAR models. A VAR(5) model is selected by the AICc, while a VAR(1) model is selected using the BIC. 

We see that the residuals from the VAR(1) model (`bic`) have significant autocorrelation for Consumption, while the VAR(5) model has effectively captured all the information in the data.

The forecasts generated by the VAR(5) model are plotted in Figure [12.14](VAR.html#fig:VAR5).
    
    
    [](VAR.html#cb285-1)fit |>
    [](VAR.html#cb285-2)  select(aicc) |>
    [](VAR.html#cb285-3)  forecast() |>
    [](VAR.html#cb285-4)  autoplot(us_change |> filter(year(Quarter) > 2010))

Figure 12.14: Forecasts for US consumption and income generated from a VAR(5) model. 

### Bibliography[](bibliography.html#bibliography)

Athanasopoulos, G., Poskitt, D. S., & Vahid, F. (2012). Two canonical VARMA forms: Scalar component models vis-à-vis the echelon form. _Econometric Reviews_ , _31_(1), 60–83. [__](https://doi.org/10.1080/07474938.2011.607088)

Hamilton, J. D. (1994). _Time series analysis_. Princeton University Press, Princeton. [__](http://amazon.com/dp/0691042896?tag=otexts20)

Lütkepohl, H. (2007). General-to-specific or specific-to-general modelling? An opinion on current econometric terminology. _Journal of Econometrics_ , _136_(1), 234–319. [__](https://doi.org/10.1016/j.jeconom.2005.11.014)

* * *

  26. A more flexible generalisation would be a Vector ARMA process. However, the relative simplicity of VARs has led to their dominance in forecasting. Interested readers may refer to Athanasopoulos et al. ([2012](VAR.html#ref-AthEtAl2012)).[↩︎](VAR.html#fnref26)

  27. Interested readers should refer to Hamilton ([1994](VAR.html#ref-Ham1994)) and Lütkepohl ([2007](VAR.html#ref-Lut2007)).[↩︎](VAR.html#fnref27)




---

## 12.4 Neural network models[](nnetar.html#nnetar)

Artificial neural networks are forecasting methods that are based on simple mathematical models of the brain. They allow complex nonlinear relationships between the response variable and its predictors.

### Neural network architecture[](nnetar.html#neural-network-architecture)

A neural network can be thought of as a network of “neurons” which are organised in layers. The predictors (or inputs) form the bottom layer, and the forecasts (or outputs) form the top layer. There may also be intermediate layers containing “hidden neurons”.

Figure 12.15: A simple neural network equivalent to a linear regression. 

The simplest networks contain no hidden layers and are equivalent to linear regressions. Figure [12.15](nnetar.html#fig:nnet1) shows the neural network version of a linear regression with four predictors. The coefficients attached to these predictors are called “weights”. The forecasts are obtained by a linear combination of the inputs. The weights are selected in the neural network framework using a “learning algorithm” that minimises a “cost function” such as the MSE. Of course, in this simple example, we can use linear regression which is a much more efficient method of training the model.

Once we add an intermediate layer with hidden neurons, the neural network becomes non-linear. A simple example is shown in Figure [12.16](nnetar.html#fig:nnet2).

Figure 12.16: A neural network with four inputs and one hidden layer with three hidden neurons. 

This is known as a _multilayer feed-forward network_ , where each layer of nodes receives inputs from the previous layers. The outputs of the nodes in one layer are inputs to the next layer. The inputs to each node are combined using a weighted linear combination. The result is then modified by a nonlinear function before being output. For example, the inputs into each hidden neuron in Figure [12.16](nnetar.html#fig:nnet2) are combined linearly to give \\[ z_j = b_j + \sum_{i=1}^4 w_{i,j} x_i. \\] In the hidden layer, this is then modified using a nonlinear function such as a sigmoid, \\[ s(z) = \frac{1}{1+e^{-z}}, \\] to give the input for the next layer. This tends to reduce the effect of extreme input values, thus making the network somewhat robust to outliers.

The parameters \\(b_1,b_2,b_3\\) and \\(w_{1,1},\dots,w_{4,3}\\) are “learned” (or estimated) from the data. The values of the weights are often restricted to prevent them from becoming too large. The parameter that restricts the weights is known as the “decay parameter”, and is often set to be equal to 0.1.

The weights take random values to begin with, and these are then updated using the observed data. Consequently, there is an element of randomness in the predictions produced by a neural network. Therefore, the network is usually trained several times using different random starting points, and the results are averaged.

The number of hidden layers, and the number of nodes in each hidden layer, must be specified in advance. Usually, these would be selected using cross-validation.

### Neural network autoregression[](nnetar.html#neural-network-autoregression)

With time series data, lagged values of the time series can be used as inputs to a neural network, just as we used lagged values in a linear autoregression model (Chapter [9](arima.html#arima)). We call this a neural network autoregression or NNAR model.

In this book, we only consider feed-forward networks with one hidden layer, and we use the notation NNAR(\\(p,k\\)) to indicate there are \\(p\\) lagged inputs and \\(k\\) nodes in the hidden layer. For example, a NNAR(9,5) model is a neural network with the last nine observations \\((y_{t-1},y_{t-2},\dots,y_{t-9}\\)) used as inputs for forecasting the output \\(y_t\\), and with five neurons in the hidden layer. A NNAR(\\(p,0\\)) model is equivalent to an ARIMA(\\(p,0,0\\)) model, but without the restrictions on the parameters to ensure stationarity.

With seasonal data, it is useful to also add the last observed values from the same season as inputs. For example, an NNAR(3,1,2)\\(_{12}\\) model has inputs \\(y_{t-1}\\), \\(y_{t-2}\\), \\(y_{t-3}\\) and \\(y_{t-12}\\), and two neurons in the hidden layer. More generally, an NNAR(\\(p,P,k\\))\\(_m\\) model has inputs \\((y_{t-1},y_{t-2},\dots,y_{t-p},y_{t-m},y_{t-2m},\dots,y_{t-Pm})\\) and \\(k\\) neurons in the hidden layer. A NNAR(\\(p,P,0\\))\\(_m\\) model is equivalent to an ARIMA(\\(p,0,0\\))(\\(P\\),0,0)\\(_m\\) model but without the restrictions on the parameters that ensure stationarity.

The `NNETAR()` function fits an NNAR(\\(p,P,k\\))\\(_m\\) model. If the values of \\(p\\) and \\(P\\) are not specified, they are selected automatically. For non-seasonal time series, the default is the optimal number of lags (according to the AIC) for a linear AR(\\(p\\)) model. For seasonal time series, the default values are \\(P=1\\) and \\(p\\) is chosen from the optimal linear model fitted to the seasonally adjusted data. If \\(k\\) is not specified, it is set to \\(k=(p+P+1)/2\\) (rounded to the nearest integer).

When it comes to forecasting, the network is applied iteratively. For forecasting one step ahead, we simply use the available historical inputs. For forecasting two steps ahead, we use the one-step forecast as an input, along with the historical data. This process proceeds until we have computed all the required forecasts.

### Example: Sunspots[](nnetar.html#example-sunspots)

The surface of the sun contains magnetic regions that appear as dark spots. These affect the propagation of radio waves, and so telecommunication companies like to predict sunspot activity in order to plan for any future difficulties. Sunspots follow a cycle of length between 9 and 14 years. In Figure [12.17](nnetar.html#fig:sunspotnnetar), forecasts from an NNAR(9,5) are shown for the next 30 years. We have used a square root transformation to ensure the forecasts stay positive.
    
    
    [](nnetar.html#cb286-1)sunspots <- sunspot.year |> as_tsibble()
    [](nnetar.html#cb286-2)fit <- sunspots |>
    [](nnetar.html#cb286-3)  model(NNETAR(sqrt(value)))
    [](nnetar.html#cb286-4)fit |>
    [](nnetar.html#cb286-5)  forecast(h = 30) |>
    [](nnetar.html#cb286-6)  autoplot(sunspots) +
    [](nnetar.html#cb286-7)  labs(x = "Year", y = "Counts", title = "Yearly sunspots")

Figure 12.17: Forecasts from a neural network with nine lagged inputs and one hidden layer containing five neurons. 

Here, the last 9 observations are used as predictors, and there are 5 neurons in the hidden layer. The cyclicity in the data has been modelled well. We can also see the asymmetry of the cycles has been captured by the model, where the increasing part of the cycle is steeper than the decreasing part of the cycle. This is one difference between a NNAR model and a linear AR model — while linear AR models can model cyclicity, the modelled cycles are always symmetric.

### Prediction intervals[](nnetar.html#prediction-intervals-5)

Unlike most of the methods considered in this book, neural networks are not based on a well-defined stochastic model, and so it is not straightforward to derive prediction intervals for the resultant forecasts. However, we can still compute prediction intervals using simulation where future sample paths are generated using bootstrapped residuals (as described in Section [5.5](prediction-intervals.html#prediction-intervals)).

The neural network fitted to the sunspot data can be written as \\[ y_t = f(\bm{y}_{t-1}) + \varepsilon_t \\] where \\(\bm{y}_{t-1} = (y_{t-1},y_{t-2},\dots,y_{t-9})'\\) is a vector containing lagged values of the series, and \\(f\\) is a neural network with 5 hidden nodes in a single layer. The error series \\(\\{\varepsilon_t\\}\\) is assumed to be homoscedastic (and possibly also normally distributed).

We can simulate future sample paths of this model iteratively, by randomly generating a value for \\(\varepsilon_t\\), either from a normal distribution, or by resampling from the historical values. So if \\(\varepsilon^*_{T+1}\\) is a random draw from the distribution of errors at time \\(T+1\\), then \\[ y^*_{T+1} = f(\bm{y}_{T}) + \varepsilon^*_{T+1} \\] is one possible draw from the forecast distribution for \\(y_{T+1}\\). Setting \\(\bm{y}_{T+1}^* = (y^*_{T+1}, y_{T}, \dots, y_{T-7})'\\), we can then repeat the process to get \\[ y^*_{T+2} = f(\bm{y}^*_{T+1}) + \varepsilon^*_{T+2}. \\] In this way, we can iteratively simulate a future sample path. By repeatedly simulating sample paths, we build up knowledge of the distribution for all future values based on the fitted neural network.

Here is a simulation of 9 possible future sample paths for the sunspot data. Each sample path covers the next 30 years after the observed data.
    
    
    [](nnetar.html#cb287-1)fit |>
    [](nnetar.html#cb287-2)  generate(times = 9, h = 30) |>
    [](nnetar.html#cb287-3)  autoplot(.sim) +
    [](nnetar.html#cb287-4)  autolayer(sunspots, value) +
    [](nnetar.html#cb287-5)  theme(legend.position = "none")

Figure 12.18: Future sample paths for the annual sunspot data. 

If we do this many times, we can get a good picture of the forecast distributions. This is how the `forecast()` function produces prediction intervals for NNAR models. The `times` argument in `forecast()` controls how many simulations are done (default 1000). By default, the errors are drawn from a normal distribution. The `bootstrap` argument allows the errors to be “bootstrapped” (i.e., randomly drawn from the historical errors).


---

## 12.5 Bootstrapping and bagging[](bootstrap.html#bootstrap)

### Bootstrapping time series[](bootstrap.html#bootstrapping-time-series)

In the preceding section, and in Section [5.5](prediction-intervals.html#prediction-intervals), we bootstrap the residuals of a time series in order to simulate future values of a series using a model.

More generally, we can generate new time series that are similar to our observed series, using another type of bootstrap.

First, the time series is transformed if necessary, and then decomposed into trend, seasonal and remainder components using STL. Then we obtain shuffled versions of the remainder component to get bootstrapped remainder series. Because there may be autocorrelation present in an STL remainder series, we cannot simply use the re-draw procedure that was described in Section [5.5](prediction-intervals.html#prediction-intervals). Instead, we use a “blocked bootstrap”, where contiguous sections of the time series are selected at random and joined together. These bootstrapped remainder series are added to the trend and seasonal components, and the transformation is reversed to give variations on the original time series.

Consider the quarterly cement production in Australia from 1988 Q1 to 2010 Q2. First we check, see Figure [12.19](bootstrap.html#fig:cementstl) that the decomposition has adequately captured the trend and seasonality, and that there is no obvious remaining signal in the remainder series.
    
    
    [](bootstrap.html#cb288-1)cement <- aus_production |>
    [](bootstrap.html#cb288-2)  filter(year(Quarter) >= 1988) |>
    [](bootstrap.html#cb288-3)  select(Quarter, Cement)
    [](bootstrap.html#cb288-4)cement_stl <- cement |>
    [](bootstrap.html#cb288-5)  model(stl = STL(Cement))
    [](bootstrap.html#cb288-6)cement_stl |>
    [](bootstrap.html#cb288-7)  components() |>
    [](bootstrap.html#cb288-8)  autoplot()

Figure 12.19: STL decomposition of quarterly Australian cement production. 

Now we can generate several bootstrapped versions of the data. Usually, `generate()` produces simulations of the future from a model. But here we want simulations for the period of the historical data. So we use the `new_data` argument to pass in the original data so that the same time periods are used for the simulated data. We will use a block size of 8 to cover two years of data.
    
    
    [](bootstrap.html#cb289-1)cement_stl |>
    [](bootstrap.html#cb289-2)  generate(new_data = cement, times = 10,
    [](bootstrap.html#cb289-3)           bootstrap_block_size = 8) |>
    [](bootstrap.html#cb289-4)  autoplot(.sim) +
    [](bootstrap.html#cb289-5)  autolayer(cement, Cement) +
    [](bootstrap.html#cb289-6)  guides(colour = "none") +
    [](bootstrap.html#cb289-7)  labs(title = "Cement production: Bootstrapped series",
    [](bootstrap.html#cb289-8)       y="Tonnes ('000)")

Figure 12.20: Ten bootstrapped versions of quarterly Australian cement production (coloured), along with the original data (black). 

### Bagged forecasts[](bootstrap.html#bagged-forecasts)

One use for these bootstrapped time series is to improve forecast accuracy. If we produce forecasts from each of the additional time series, and average the resulting forecasts, we get better forecasts than if we simply forecast the original time series directly. This is called “bagging” which stands for “**b** ootstrap **agg** regatin**g** ”.

We demonstrate the idea using the `cement` data. First, we simulate many time series that are similar to the original data, using the block-bootstrap described above.
    
    
    [](bootstrap.html#cb290-1)sim <- cement_stl |>
    [](bootstrap.html#cb290-2)  generate(new_data = cement, times = 100,
    [](bootstrap.html#cb290-3)           bootstrap_block_size = 8) |>
    [](bootstrap.html#cb290-4)  select(-.model, -Cement)

For each of these series, we fit an ETS model. A different ETS model may be selected in each case, although it will most likely select the same model because the series are similar. However, the estimated parameters will be different, so the forecasts will be different even if the selected model is the same. This is a time-consuming process as there are a large number of series.
    
    
    [](bootstrap.html#cb291-1)ets_forecasts <- sim |>
    [](bootstrap.html#cb291-2)  model(ets = ETS(.sim)) |>
    [](bootstrap.html#cb291-3)  forecast(h = 12)
    [](bootstrap.html#cb291-4)ets_forecasts |>
    [](bootstrap.html#cb291-5)  update_tsibble(key = .rep) |>
    [](bootstrap.html#cb291-6)  autoplot(.mean) +
    [](bootstrap.html#cb291-7)  autolayer(cement, Cement) +
    [](bootstrap.html#cb291-8)  guides(colour = "none") +
    [](bootstrap.html#cb291-9)  labs(title = "Cement production: bootstrapped forecasts",
    [](bootstrap.html#cb291-10)       y="Tonnes ('000)")

Figure 12.21: Forecasts of 100 bootstrapped series obtained using ETS models. 

Finally, we average these forecasts for each time period to obtain the “bagged forecasts” for the original data.
    
    
    [](bootstrap.html#cb292-1)bagged <- ets_forecasts |>
    [](bootstrap.html#cb292-2)  summarise(bagged_mean = mean(.mean))
    [](bootstrap.html#cb292-3)cement |>
    [](bootstrap.html#cb292-4)  model(ets = ETS(Cement)) |>
    [](bootstrap.html#cb292-5)  forecast(h = 12) |>
    [](bootstrap.html#cb292-6)  autoplot(cement) +
    [](bootstrap.html#cb292-7)  autolayer(bagged, bagged_mean, col = "#D55E00") +
    [](bootstrap.html#cb292-8)  labs(title = "Cement production in Australia",
    [](bootstrap.html#cb292-9)       y="Tonnes ('000)")

Figure 12.22: Comparing bagged ETS forecasts (the average of 100 bootstrapped forecasts in orange) and ETS applied directly to the data (in blue). 

Bergmeir et al. ([2016](bootstrap.html#ref-baggedETS)) show that, on average, bagging gives better forecasts than just applying `ETS()` directly. Of course, it is slower because a lot more computation is required.

### Bibliography[](bibliography.html#bibliography)

Bergmeir, C., Hyndman, R. J., & Benítez, J. M. (2016). Bagging exponential smoothing methods using STL decomposition and Box-Cox transformation. _International Journal of Forecasting_ , _32_(2), 303–312. [__](https://doi.org/10.1016/j.ijforecast.2015.07.002)


---

## 12.6 Exercises[](advanced-exercises.html#advanced-exercises)

  1. Compare STL and Dynamic Harmonic Regression forecasts for one of the series in the `pedestrian` data set.

     1. Try modifying the order of the Fourier terms to minimize the AICc value.
     2. Check the residuals for each model. Do they capture the available information in the data?
     3. Which of the two sets of forecasts are best? Explain.
  2. Consider the weekly data on US finished motor gasoline products supplied (millions of barrels per day) (series `us_gasoline`):

     1. Fit a dynamic harmonic regression model to these data. How does it compare to the regression model you fitted in Exercise 5 in Section [7.10](regression-exercises.html#regression-exercises)?
     2. Check the residuals from both models and comment on what you see.
     3. Could you model these data using any of the other methods we have considered in this book? Explain why/why not.
  3. Experiment with using `NNETAR()` on your retail data and other data we have considered in previous chapters.




---

## 12.7 Further reading[](advanced-reading.html#advanced-reading)

  * The Prophet model is described in S. J. Taylor & Letham ([2018](advanced-reading.html#ref-prophet)).
  * Pfaff ([2008](advanced-reading.html#ref-Pfaff2008)) provides a book-length overview of VAR modelling and other multivariate time series models.
  * A current survey of the use of recurrent neural networks for forecasting is provided by Hewamalage et al. ([2021](advanced-reading.html#ref-HBB2021rnn)).
  * Bootstrapping for time series is discussed in Lahiri ([2003](advanced-reading.html#ref-Lahiri2013)).
  * Bagging for time series forecasting is relatively new. Bergmeir et al. ([2016](advanced-reading.html#ref-baggedETS)) is one of the few papers which addresses this topic.


### Bibliography[](bibliography.html#bibliography)

Bergmeir, C., Hyndman, R. J., & Benítez, J. M. (2016). Bagging exponential smoothing methods using STL decomposition and Box-Cox transformation. _International Journal of Forecasting_ , _32_(2), 303–312. [__](https://doi.org/10.1016/j.ijforecast.2015.07.002)

Hewamalage, H., Bergmeir, C., & Bandara, K. (2021). Recurrent neural networks for time series forecasting: Current status and future directions. _International Journal of Forecasting_ , _37_(1), 388–427. [__](https://doi.org/10.1016/j.ijforecast.2020.06.008)

Lahiri, S. N. (2003). _Resampling methods for dependent data_. Springer Science & Business Media. [__](http://amazon.com/dp/0387009280?tag=otexts20)

Pfaff, B. (2008). _Analysis of integrated and cointegrated time series with R_. Springer Science & Business Media. [__](http://amazon.com/dp/0387759662?tag=otexts20)

Taylor, S. J., & Letham, B. (2018). Forecasting at scale. _The American Statistician_ , _72_(1), 37–45. [__](https://doi.org/10.1080/00031305.2017.1380080)


---

# Chapter 13 Some practical forecasting issues[](practical.html#practical)

In this final chapter, we address many practical issues that arise in forecasting, and discuss some possible solutions.


---

## 13.1 Weekly, daily and sub-daily data[](weekly.html#weekly)

Weekly, daily and sub-daily data can be challenging for forecasting, although for different reasons.

### Weekly data[](weekly.html#weekly-data)

Weekly data is difficult to work with because the seasonal period (the number of weeks in a year) is both large and non-integer. The average number of weeks in a year is 52.18. Most of the methods we have considered require the seasonal period to be an integer. Even if we approximate it by 52, most of the methods will not handle such a large seasonal period efficiently.

The simplest approach is to use an STL decomposition along with a non-seasonal method applied to the seasonally adjusted data (as discussed in Chapter [3](decomposition.html#decomposition)). Here is an example using weekly data on US finished motor gasoline products supplied (in millions of barrels per day) from February 1991 to May 2005.
    
    
    [](weekly.html#cb293-1)my_dcmp_spec <- decomposition_model(
    [](weekly.html#cb293-2)  STL(Barrels),
    [](weekly.html#cb293-3)  ETS(season_adjust ~ season("N"))
    [](weekly.html#cb293-4))
    [](weekly.html#cb293-5)us_gasoline |>
    [](weekly.html#cb293-6)  model(stl_ets = my_dcmp_spec) |>
    [](weekly.html#cb293-7)  forecast(h = "2 years") |>
    [](weekly.html#cb293-8)  autoplot(us_gasoline) +
    [](weekly.html#cb293-9)  labs(y = "Millions of barrels per day",
    [](weekly.html#cb293-10)       title = "Weekly US gasoline production")

Figure 13.1: Forecasts for weekly US gasoline production using an STL decomposition with an ETS model for the seasonally adjusted data. 

An alternative approach is to use a dynamic harmonic regression model, as discussed in Section [10.5](dhr.html#dhr). In the following example, the number of Fourier terms was selected by minimising the AICc. The order of the ARIMA model is also selected by minimising the AICc, although that is done within the `ARIMA()` function. We use `PDQ(0,0,0)` to prevent `ARIMA()` trying to handle the seasonality using seasonal ARIMA components.
    
    
    [](weekly.html#cb294-1)gas_dhr <- us_gasoline |>
    [](weekly.html#cb294-2)  model(dhr = ARIMA(Barrels ~ PDQ(0, 0, 0) + fourier(K = 6)))
    
    
    [](weekly.html#cb295-1)gas_dhr |>
    [](weekly.html#cb295-2)  forecast(h = "2 years") |>
    [](weekly.html#cb295-3)  autoplot(us_gasoline) +
    [](weekly.html#cb295-4)  labs(y = "Millions of barrels per day",
    [](weekly.html#cb295-5)       title = "Weekly US gasoline production")

Figure 13.2: Forecasts for weekly US gasoline production using a dynamic harmonic regression model. 

The fitted model has 6 pairs of Fourier terms and can be written as \\[ y_t = bt + \sum_{j=1}^{6} \left[ \alpha_j\sin\left(\frac{2\pi j t}{52.18}\right) + \beta_j\cos\left(\frac{2\pi j t}{52.18}\right) \right] + \eta_t \\] where \\(\eta_t\\) is an ARIMA(0,1,1) process. Because \\(\eta_t\\) is non-stationary, the model is actually estimated on the differences of the variables on both sides of this equation. There are 12 parameters to capture the seasonality, while the total number of degrees of freedom is 14 (the other two coming from the MA parameter and the drift parameter).

The STL approach is preferable when the seasonality changes over time. The dynamic harmonic regression approach is preferable if there are covariates that are useful predictors as these can be added as additional regressors.

### Daily and sub-daily data[](weekly.html#daily-and-sub-daily-data)

Daily and sub-daily (such as hourly) data are challenging for a different reason — they often involve multiple seasonal patterns, and so we need to use a method that handles such complex seasonality.

Of course, if the time series is relatively short so that only one type of seasonality is present, then it will be possible to use one of the single-seasonal methods we have discussed in previous chapters (e.g., ETS or a seasonal ARIMA model). But when the time series is long enough so that some of the longer seasonal periods become apparent, it will be necessary to use STL, dynamic harmonic regression or Prophet, as discussed in Section [12.1](complexseasonality.html#complexseasonality).

However, these methods only allow for regular seasonality. Capturing seasonality associated with moving events such as Easter, Eid, or the Chinese New Year is more difficult. Even with monthly data, this can be tricky as the festivals can fall in either March or April (for Easter), in January or February (for the Chinese New Year), or at any time of the year (for Eid).

The best way to deal with moving holiday effects is to include dummy variables in the model. This can be done within the `ARIMA()` or `prophet()` functions, for example, but not within `ETS()`. In fact, `prophet()` has a `holiday()` special to easily incorporate holiday effects.


---

## 13.2 Time series of counts[](counts.html#counts)

All of the methods discussed in this book assume that the data have a continuous sample space. But often data comes in the form of counts. For example, we may wish to forecast the number of customers who enter a store each day. We could have \\(0, 1, 2, \dots\\), customers, but we cannot have 3.45693 customers.

In practice, this rarely matters provided our counts are sufficiently large. If the minimum number of customers is at least 100, then the difference between a continuous sample space \\([100,\infty)\\) and the discrete sample space \\(\\{100,101,102,\dots\\}\\) has no perceivable effect on our forecasts. However, if our data contains small counts \\((0, 1, 2, \dots)\\), then we need to use forecasting methods that are more appropriate for a sample space of non-negative integers.

Such models are beyond the scope of this book. However, there is one simple method which gets used in this context, that we would like to mention. It is “Croston’s method”, named after its British inventor, John Croston, and first described in Croston ([1972](counts.html#ref-Croston72)). Actually, this method does not properly deal with the count nature of the data either, but it is used so often, that it is worth knowing about it.

With Croston’s method, we construct two new series from our original time series by noting which time periods contain zero values, and which periods contain non-zero values. Let \\(q_i\\) be the \\(i\\)th non-zero quantity, and let \\(a_i\\) be the time between \\(q_{i-1}\\) and \\(q_i\\). Croston’s method involves separate simple exponential smoothing forecasts on the two new series \\(a\\) and \\(q\\). Because the method is usually applied to time series of demand for items, \\(q\\) is often called the “demand” and \\(a\\) the “inter-arrival time”.

If \\(\hat{q}_{i+1|i}\\) and \\(\hat{a}_{i+1|i}\\) are the one-step forecasts of the \\((i+1)\\)th demand and inter-arrival time respectively, based on data up to demand \\(i\\), then Croston’s method gives \\[\begin{align} \hat{q}_{i+1|i} & = (1-\alpha_q)\hat{q}_{i|i-1} + \alpha_q q_i, \tag{13.1}\\\ \hat{a}_{i+1|i} & = (1-\alpha_a)\hat{a}_{i|i-1} + \alpha_a a_i. \tag{13.2} \end{align}\\] The smoothing parameters \\(\alpha_a\\) and \\(\alpha_q\\) take values between 0 and 1. Let \\(j\\) be the time for the last observed positive observation. Then the \\(h\\)-step ahead forecast for the demand at time \\(T+h\\), is given by the ratio \\[ \hat{y}_{T+h|T} = \hat{q}_{j+1|j}/\hat{a}_{j+1|j}. \\] There are no algebraic results allowing us to compute prediction intervals for this method, because the method does not correspond to any statistical model ([Shenstone & Hyndman, 2005](counts.html#ref-SH05)). Forecasts obtained from Croston’s method are also known to be biased ([Syntetos & Boylan, 2001](counts.html#ref-SB01)).

The `CROSTON()` function produces forecasts using Croston’s method. The two smoothing parameters \\(\alpha_a\\) and \\(\alpha_q\\) are estimated from the data. This is different from the way Croston envisaged the method being used. He would simply use \\(\alpha_a=\alpha_q=0.1\\), and set \\(a_0\\) and \\(q_0\\) to be equal to the first observation in each of the series.

### Example: Pharmaceutical sales[](counts.html#example-pharmaceutical-sales)

Figure [13.3](counts.html#fig:j06) shows the numbers of scripts sold each month for immune sera and immunoglobulin products in Australia. The data contain small counts, with many months registering no sales at all, and only small numbers of items sold in other months.
    
    
    [](counts.html#cb296-1)j06 <- PBS |>
    [](counts.html#cb296-2)  filter(ATC2 == "J06") |>
    [](counts.html#cb296-3)  summarise(Scripts = sum(Scripts))
    [](counts.html#cb296-4)
    [](counts.html#cb296-5)j06 |> autoplot(Scripts) +
    [](counts.html#cb296-6)  labs(y="Number of scripts",
    [](counts.html#cb296-7)       title = "Sales for immune sera and immunoglobulins")

Figure 13.3: Numbers of scripts sold for Immune sera and immunoglobulins on the Australian Pharmaceutical Benefits Scheme. 

Tables [13.1](counts.html#tab:j06table) and [13.2](counts.html#tab:j06table2) shows the first 10 non-zero demand values, with their corresponding inter-arrival times.

Table 13.1: The first 10 non-zero demand values. Month | Scripts  
---|---  
1991 Jul | 1  
1991 Aug | 1  
1991 Sep | 1  
1991 Oct | 0  
1991 Nov | 0  
1991 Dec | 1  
1992 Jan | 3  
1992 Feb | 1  
1992 Mar | 1  
1992 Apr | 1  
1992 May | 1  
1992 Jun | 1  
Table 13.2: The first 10 non-zero demand values shown as demand and inter-arrival series. \\(i\\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10  
---|---|---|---|---|---|---|---|---|---|---  
\\(q_i\\) | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 1 | 1  
\\(a_i\\) |  | 1 | 1 | 3 | 1 | 1 | 1 | 1 | 1 | 1  
  
In this example, the smoothing parameters are estimated to be \\(\alpha_a = 0.08\\), \\(\alpha_q = 0.71\\), \\(\hat{q}_{1|0}=4.17\\), and \\(\hat{a}_{1|0}=3.52\\). The final forecasts for the two series are \\(\hat{q}_{T+1|T} = 2.419\\) and \\(\hat{a}_{T+1|T} = 2.484\\). So the forecasts are all equal to \\(\hat{y}_{T+h|T} = 2.419/2.484 = 0.974\\).

In practice, `fable` does these calculations for you:
    
    
    [](counts.html#cb297-1)j06 |>
    [](counts.html#cb297-2)  model(CROSTON(Scripts)) |>
    [](counts.html#cb297-3)  forecast(h = 6)
    [](counts.html#cb297-4)#> # A fable: 6 x 4 [1M]
    [](counts.html#cb297-5)#> # Key:     .model [1]
    [](counts.html#cb297-6)#>   .model              Month Scripts .mean
    [](counts.html#cb297-7)#>   <chr>               <mth>  <dist> <dbl>
    [](counts.html#cb297-8)#> 1 CROSTON(Scripts) 2008 Jul  0.9735 0.974
    [](counts.html#cb297-9)#> 2 CROSTON(Scripts) 2008 Aug  0.9735 0.974
    [](counts.html#cb297-10)#> 3 CROSTON(Scripts) 2008 Sep  0.9735 0.974
    [](counts.html#cb297-11)#> 4 CROSTON(Scripts) 2008 Oct  0.9735 0.974
    [](counts.html#cb297-12)#> 5 CROSTON(Scripts) 2008 Nov  0.9735 0.974
    [](counts.html#cb297-13)#> 6 CROSTON(Scripts) 2008 Dec  0.9735 0.974

The `Scripts` column repeats the mean rather than provide a full distribution, because there is no underlying stochastic model.

Forecasting models that deal more directly with the count nature of the data, and allow for a forecasting distribution, are described in Christou & Fokianos ([2015](counts.html#ref-christou2015count)).

### Bibliography[](bibliography.html#bibliography)

Christou, V., & Fokianos, K. (2015). On count time series prediction. _Journal of Statistical Computation and Simulation_ , _85_(2), 357–373. [__](https://doi.org/10.1080/00949655.2013.823612)

Croston, J. D. (1972). Forecasting and stock control for intermittent demands. _Operational Research Quarterly_ , _23_(3), 289–303. [__](https://doi.org/10.2307/3007885)

Shenstone, L., & Hyndman, R. J. (2005). Stochastic models underlying Croston’s method for intermittent demand forecasting. _Journal of Forecasting_ , _24_(6), 389–402. [__](https://doi.org/10.1002/for.963)

Syntetos, A. A., & Boylan, J. E. (2001). On the bias of intermittent demand estimates. _International Journal of Production Economics_ , _71_ , 457–466. [__](https://doi.org/10.1016/S0925-5273\(00\)00143-2)


---

## 13.3 Ensuring forecasts stay within limits[](limits.html#limits)

It is common to want forecasts to be positive, or to require them to be within some specified range \\([a,b]\\). Both of these situations are relatively easy to handle using transformations.

### Positive forecasts[](limits.html#positive-forecasts)

To impose a positivity constraint, we can simply work on the log scale. For example, consider the real price of a dozen eggs (1900-1993; in cents) shown in Figure [13.4](limits.html#fig:positiveeggs). Because of the log transformation, the forecast distributions are constrained to stay positive, and so they will become progressively more skewed as the mean decreases.
    
    
    [](limits.html#cb298-1)egg_prices <- prices |> filter(!is.na(eggs))
    [](limits.html#cb298-2)egg_prices |>
    [](limits.html#cb298-3)  model(ETS(log(eggs) ~ trend("A"))) |>
    [](limits.html#cb298-4)  forecast(h = 50) |>
    [](limits.html#cb298-5)  autoplot(egg_prices) +
    [](limits.html#cb298-6)  labs(title = "Annual egg prices",
    [](limits.html#cb298-7)       y = "$US (in cents adjusted for inflation) ")

Figure 13.4: Forecasts for the price of a dozen eggs, constrained to be positive using a log transformation. 

### Forecasts constrained to an interval[](limits.html#forecasts-constrained-to-an-interval)

To see how to handle data constrained to an interval, imagine that the egg prices were constrained to lie within \\(a=50\\) and \\(b=400\\). Then we can transform the data using a scaled logit transform which maps \\((a,b)\\) to the whole real line: \\[ y = \log\left(\frac{x-a}{b-x}\right), \\] where \\(x\\) is on the original scale and \\(y\\) is the transformed data. To reverse the transformation, we will use \\[ x = \frac{(b-a)e^y}{1+e^y} + a. \\] This is not a built-in transformation, so we will need to first setup the transformation functions.
    
    
    [](limits.html#cb299-1)scaled_logit <- function(x, lower = 0, upper = 1) {
    [](limits.html#cb299-2)  log((x - lower) / (upper - x))
    [](limits.html#cb299-3)}
    [](limits.html#cb299-4)inv_scaled_logit <- function(x, lower = 0, upper = 1) {
    [](limits.html#cb299-5)  (upper - lower) * exp(x) / (1 + exp(x)) + lower
    [](limits.html#cb299-6)}
    [](limits.html#cb299-7)my_scaled_logit <- new_transformation(
    [](limits.html#cb299-8)                    scaled_logit, inv_scaled_logit)
    [](limits.html#cb299-9)egg_prices |>
    [](limits.html#cb299-10)  model(
    [](limits.html#cb299-11)    ETS(my_scaled_logit(eggs, lower = 50, upper = 400)
    [](limits.html#cb299-12)          ~ trend("A"))
    [](limits.html#cb299-13)  ) |>
    [](limits.html#cb299-14)  forecast(h = 50) |>
    [](limits.html#cb299-15)  autoplot(egg_prices) +
    [](limits.html#cb299-16)  labs(title = "Annual egg prices",
    [](limits.html#cb299-17)       y = "$US (in cents adjusted for inflation) ")

Figure 13.5: Forecasts for the price of a dozen eggs, constrained to be lie between 50 and 400 cents US. 

The bias-adjustment is automatically applied here, and the prediction intervals from these transformations have the same coverage probability as on the transformed scale, because quantiles are preserved under monotonically increasing transformations.

The prediction intervals lie above 50 due to the transformation. As a result of this artificial (and unrealistic) constraint, the forecast distributions have become extremely skewed.


---

## 13.4 Forecast combinations[](combinations.html#combinations)

An easy way to improve forecast accuracy is to use several different methods on the same time series, and to average the resulting forecasts. Over 50 years ago, John Bates and Clive Granger wrote a famous paper ([Bates & Granger, 1969](combinations.html#ref-BatesGranger1969)), showing that combining forecasts often leads to better forecast accuracy. Twenty years later, Clemen ([1989](combinations.html#ref-Clemen89)) wrote

> The results have been virtually unanimous: combining multiple forecasts leads to increased forecast accuracy. In many cases one can make dramatic performance improvements by simply averaging the forecasts.

While there has been considerable research on using weighted averages, or some other more complicated combination approach, using a simple average has proven hard to beat ([Wang et al., 2023](combinations.html#ref-combinations)).

Here is an example using monthly revenue from take-away food in Australia, from April 1982 to December 2018. We use forecasts from the following models: ETS, STL-ETS, and ARIMA; and we compare the results using the last 5 years (60 months) of observations.
    
    
    [](combinations.html#cb300-1)auscafe <- aus_retail |>
    [](combinations.html#cb300-2)  filter(stringr::str_detect(Industry, "Takeaway")) |>
    [](combinations.html#cb300-3)  summarise(Turnover = sum(Turnover))
    [](combinations.html#cb300-4)train <- auscafe |>
    [](combinations.html#cb300-5)  filter(year(Month) <= 2013)
    [](combinations.html#cb300-6)STLF <- decomposition_model(
    [](combinations.html#cb300-7)  STL(log(Turnover) ~ season(window = Inf)),
    [](combinations.html#cb300-8)  ETS(season_adjust ~ season("N"))
    [](combinations.html#cb300-9))
    [](combinations.html#cb300-10)cafe_models <- train |>
    [](combinations.html#cb300-11)  model(
    [](combinations.html#cb300-12)    ets = ETS(Turnover),
    [](combinations.html#cb300-13)    stlf = STLF,
    [](combinations.html#cb300-14)    arima = ARIMA(log(Turnover))
    [](combinations.html#cb300-15)  ) |>
    [](combinations.html#cb300-16)  mutate(combination = (ets + stlf + arima) / 3)
    [](combinations.html#cb300-17)cafe_fc <- cafe_models |>
    [](combinations.html#cb300-18)  forecast(h = "5 years")

Notice that we form a combination in the `mutate()` function by simply taking a linear function of the estimated models. This very simple syntax will automatically handle the forecast distribution appropriately by taking account of the correlation between the forecast errors of the models that are included. However, to keep the next plot simple, we will omit the prediction intervals.
    
    
    [](combinations.html#cb301-1)cafe_fc |>
    [](combinations.html#cb301-2)  autoplot(auscafe |> filter(year(Month) > 2008),
    [](combinations.html#cb301-3)           level = NULL) +
    [](combinations.html#cb301-4)  labs(y = "$ billion",
    [](combinations.html#cb301-5)       title = "Australian monthly expenditure on eating out")

Figure 13.6: Point forecasts from various methods applied to Australian monthly expenditure on eating out. 
    
    
    [](combinations.html#cb302-1)cafe_fc |>
    [](combinations.html#cb302-2)  accuracy(auscafe) |>
    [](combinations.html#cb302-3)  arrange(RMSE)
    [](combinations.html#cb302-4)#> # A tibble: 4 × 10
    [](combinations.html#cb302-5)#>   .model      .type     ME  RMSE   MAE    MPE  MAPE  MASE RMSSE  ACF1
    [](combinations.html#cb302-6)#>   <chr>       <chr>  <dbl> <dbl> <dbl>  <dbl> <dbl> <dbl> <dbl> <dbl>
    [](combinations.html#cb302-7)#> 1 combination Test    8.09  41.0  31.8  0.401  2.19 0.776 0.790 0.747
    [](combinations.html#cb302-8)#> 2 arima       Test  -25.4   46.2  38.9 -1.77   2.65 0.949 0.890 0.786
    [](combinations.html#cb302-9)#> 3 stlf        Test  -36.9   64.1  51.7 -2.55   3.54 1.26  1.23  0.775
    [](combinations.html#cb302-10)#> 4 ets         Test   86.5  122.  101.   5.51   6.66 2.46  2.35  0.880

ARIMA does particularly well with this series, while the combination approach does even better (based on most measures including RMSE and MAE). For other data, ARIMA may be quite poor, while the combination approach is usually not far off, or better than, the best component method.

### Forecast combination distributions[](combinations.html#forecast-combination-distributions)

The `cafe_fc` object contains forecast distributions, from which any prediction interval can usually be computed. Let’s look at the intervals for the first period.
    
    
    [](combinations.html#cb303-1)cafe_fc |> filter(Month == min(Month))
    [](combinations.html#cb303-2)#> # A fable: 4 x 4 [1M]
    [](combinations.html#cb303-3)#> # Key:     .model [4]
    [](combinations.html#cb303-4)#>   .model         Month
    [](combinations.html#cb303-5)#>   <chr>          <mth>
    [](combinations.html#cb303-6)#> 1 ets         2014 Jan
    [](combinations.html#cb303-7)#> 2 stlf        2014 Jan
    [](combinations.html#cb303-8)#> 3 arima       2014 Jan
    [](combinations.html#cb303-9)#> 4 combination 2014 Jan
    [](combinations.html#cb303-10)#> # ℹ 2 more variables: Turnover <dist>, .mean <dbl>

The first three are a mixture of normal and transformed normal distributions. The package does not yet combine such diverse distributions, so the `combination` output is simply the mean instead.

However, if we work with simulated sample paths, it is possible to create forecast distributions for the combination forecast as well.
    
    
    [](combinations.html#cb304-1)cafe_futures <- cafe_models |>
    [](combinations.html#cb304-2)  # Generate 1000 future sample paths
    [](combinations.html#cb304-3)  generate(h = "5 years", times = 1000) |>
    [](combinations.html#cb304-4)  # Compute forecast distributions from future sample paths
    [](combinations.html#cb304-5)  as_tibble() |>
    [](combinations.html#cb304-6)  group_by(Month, .model) |>
    [](combinations.html#cb304-7)  summarise(
    [](combinations.html#cb304-8)    dist = distributional::dist_sample(list(.sim))
    [](combinations.html#cb304-9)  ) |>
    [](combinations.html#cb304-10)  ungroup() |>
    [](combinations.html#cb304-11)  # Create fable object
    [](combinations.html#cb304-12)  as_fable(index = Month, key = .model,
    [](combinations.html#cb304-13)           distribution = dist, response = "Turnover")
    
    
    [](combinations.html#cb305-1)# Forecast distributions for h=1
    [](combinations.html#cb305-2)cafe_futures |> filter(Month == min(Month))
    [](combinations.html#cb305-3)#> # A fable: 4 x 3 [1M]
    [](combinations.html#cb305-4)#> # Key:     .model [4]
    [](combinations.html#cb305-5)#>      Month .model              dist
    [](combinations.html#cb305-6)#>      <mth> <chr>             <dist>
    [](combinations.html#cb305-7)#> 1 2014 Jan arima       sample[1000]
    [](combinations.html#cb305-8)#> 2 2014 Jan combination sample[1000]
    [](combinations.html#cb305-9)#> 3 2014 Jan ets         sample[1000]
    [](combinations.html#cb305-10)#> 4 2014 Jan stlf        sample[1000]

Now all four models, including the combination, are stored as empirical distributions, and we can plot prediction intervals for the combination forecast, as shown in Figure [13.7](combinations.html#fig:auscafecombPI).
    
    
    [](combinations.html#cb306-1)cafe_futures |>
    [](combinations.html#cb306-2)  filter(.model == "combination") |>
    [](combinations.html#cb306-3)  autoplot(auscafe |> filter(year(Month) > 2008)) +
    [](combinations.html#cb306-4)  labs(y = "$ billion",
    [](combinations.html#cb306-5)       title = "Australian monthly expenditure on eating out")

Figure 13.7: Prediction intervals for the combination forecast of Australian monthly expenditure on eating out. 

To check the accuracy of the 95% prediction intervals, we can use a Winkler score (defined in Section [5.9](distaccuracy.html#distaccuracy)).
    
    
    [](combinations.html#cb307-1)cafe_futures |>
    [](combinations.html#cb307-2)  accuracy(auscafe, measures = interval_accuracy_measures,
    [](combinations.html#cb307-3)    level = 95) |>
    [](combinations.html#cb307-4)  arrange(winkler)
    [](combinations.html#cb307-5)#> # A tibble: 4 × 5
    [](combinations.html#cb307-6)#>   .model      .type winkler pinball scaled_pinball
    [](combinations.html#cb307-7)#>   <chr>       <chr>   <dbl>   <dbl>          <dbl>
    [](combinations.html#cb307-8)#> 1 combination Test     427.    17.8          0.217
    [](combinations.html#cb307-9)#> 2 stlf        Test     590.    29.4          0.358
    [](combinations.html#cb307-10)#> 3 ets         Test     712.    22.6          0.276
    [](combinations.html#cb307-11)#> 4 arima       Test     760.    36.9          0.450

Lower is better, so the `combination` forecast is again better than any of the component models.

### Bibliography[](bibliography.html#bibliography)

Bates, J. M., & Granger, C. W. J. (1969). The combination of forecasts. _Operational Research Quarterly_ , _20_(4), 451–468. [__](https://doi.org/10.1057/jors.1969.103)

Clemen, R. (1989). Combining forecasts: A review and annotated bibliography. _International Journal of Forecasting_ , _5_(4), 559–583. [__](https://doi.org/10.1016/0169-2070\(89\)90012-5)

Wang, X., Hyndman, R. J., Li, F., & Kang, Y. (2023). Forecast combinations: An over 50-year review. _International J Forecasting_ , _39_(4), 1518–1547. [__](https://doi.org/10.1016/j.ijforecast.2022.11.005)


---

## 13.5 Prediction intervals for aggregates[](aggregates.html#aggregates)

A common problem is to forecast the aggregate of several time periods of data, using a model fitted to the disaggregated data. For example, we may have monthly data but wish to forecast the total for the next year. Or we may have weekly data, and want to forecast the total for the next four weeks.

If the point forecasts are means, then adding them up will give a good estimate of the total. But prediction intervals are more tricky due to the correlations between forecast errors.

A general solution is to use simulations. Here is an example using ETS models applied to Australian take-away food sales, assuming we wish to forecast the aggregate revenue in the next 12 months.
    
    
    [](aggregates.html#cb308-1)fit <- auscafe |>
    [](aggregates.html#cb308-2)  # Fit a model to the data
    [](aggregates.html#cb308-3)  model(ETS(Turnover))
    [](aggregates.html#cb308-4)futures <- fit |>
    [](aggregates.html#cb308-5)  # Simulate 10000 future sample paths, each of length 12
    [](aggregates.html#cb308-6)  generate(times = 10000, h = 12) |>
    [](aggregates.html#cb308-7)  # Sum the results for each sample path
    [](aggregates.html#cb308-8)  as_tibble() |>
    [](aggregates.html#cb308-9)  group_by(.rep) |>
    [](aggregates.html#cb308-10)  summarise(.sim = sum(.sim)) |>
    [](aggregates.html#cb308-11)  # Store as a distribution
    [](aggregates.html#cb308-12)  summarise(total = distributional::dist_sample(list(.sim)))

We can compute the mean of the simulations, along with prediction intervals:
    
    
    [](aggregates.html#cb309-1)futures |>
    [](aggregates.html#cb309-2)  mutate(
    [](aggregates.html#cb309-3)    mean = mean(total),
    [](aggregates.html#cb309-4)    pi80 = hilo(total, 80),
    [](aggregates.html#cb309-5)    pi95 = hilo(total, 95)
    [](aggregates.html#cb309-6)  )
    [](aggregates.html#cb309-7)#> # A tibble: 1 × 4
    [](aggregates.html#cb309-8)#>           total   mean             pi80             pi95
    [](aggregates.html#cb309-9)#>          <dist>  <dbl>           <hilo>           <hilo>
    [](aggregates.html#cb309-10)#> 1 sample[10000] 19212. [18307, 20134]80 [17846, 20639]95

As expected, the mean of the simulated data is close to the sum of the individual forecasts.
    
    
    [](aggregates.html#cb310-1)forecast(fit, h = 12) |>
    [](aggregates.html#cb310-2)  as_tibble() |>
    [](aggregates.html#cb310-3)  summarise(total = sum(.mean))
    [](aggregates.html#cb310-4)#> # A tibble: 1 × 1
    [](aggregates.html#cb310-5)#>    total
    [](aggregates.html#cb310-6)#>    <dbl>
    [](aggregates.html#cb310-7)#> 1 19212.


---

## 13.6 Backcasting[](backcasting.html#backcasting)

Sometimes it is useful to “backcast” a time series — that is, forecast in reverse time. Although there are no in-built R functions to do this, it is easy to implement by creating a new time index.

Suppose we want to extend our Australian takeaway to the start of 1981 (the actual data starts in April 1982).
    
    
    [](backcasting.html#cb311-1)backcasts <- auscafe |>
    [](backcasting.html#cb311-2)  mutate(reverse_time = rev(row_number())) |>
    [](backcasting.html#cb311-3)  update_tsibble(index = reverse_time) |>
    [](backcasting.html#cb311-4)  model(ets = ETS(Turnover ~ season(period = 12))) |>
    [](backcasting.html#cb311-5)  forecast(h = 15) |>
    [](backcasting.html#cb311-6)  mutate(Month = auscafe$Month[1] - (1:15)) |>
    [](backcasting.html#cb311-7)  as_fable(index = Month, response = "Turnover",
    [](backcasting.html#cb311-8)    distribution = "Turnover")
    [](backcasting.html#cb311-9)backcasts |>
    [](backcasting.html#cb311-10)  autoplot(auscafe |> filter(year(Month) < 1990)) +
    [](backcasting.html#cb311-11)  labs(title = "Backcasts of Australian food expenditure",
    [](backcasting.html#cb311-12)       y = "$ (billions)")

Figure 13.8: Backcasts for Australian monthly expenditure on cafés, restaurants and takeaway food services using an ETS model. 

Most of the work here is in re-indexing the `tsibble` object and then re-indexing the `fable` object.


---

## 13.7 Very long and very short time series[](long-short-ts.html#long-short-ts)

### Forecasting very short time series[](long-short-ts.html#forecasting-very-short-time-series)

We often get asked how _few_ data points can be used to fit a time series model. As with almost all sample size questions, there is no easy answer. It depends on the _number of model parameters to be estimated and the amount of randomness in the data_. The sample size required increases with the number of parameters to be estimated, and the amount of noise in the data.

Some textbooks provide rules-of-thumb giving minimum sample sizes for various time series models. These are misleading and unsubstantiated in theory or practice. Further, they ignore the underlying variability of the data and often overlook the number of parameters to be estimated as well. There is, for example, no justification for the magic number of 30 often given as a minimum for ARIMA modelling. The only theoretical limit is that we need more observations than there are parameters in our forecasting model. However, in practice, we usually need substantially more observations than that.

Ideally, we would test if our chosen model performs well out-of-sample compared to some simpler approaches. However, with short series, there is not enough data to allow some observations to be withheld for testing purposes, and even time series cross validation can be difficult to apply. The AICc is particularly useful here, because it is a proxy for the one-step forecast out-of-sample MSE. Choosing the model with the minimum AICc value allows both the number of parameters and the amount of noise to be taken into account.

What tends to happen with short series is that the AICc suggests simple models because anything with more than one or two parameters will produce poor forecasts due to the estimation error. We will fit an ARIMA model to the annual series from the M3-competition with fewer than 20 observations. First we need to create a tsibble, containing the relevant series.
    
    
    [](long-short-ts.html#cb312-1)m3totsibble <- function(z) {
    [](long-short-ts.html#cb312-2)  bind_rows(
    [](long-short-ts.html#cb312-3)    as_tsibble(z$x) |> mutate(Type = "Training"),
    [](long-short-ts.html#cb312-4)    as_tsibble(z$xx) |> mutate(Type = "Test")
    [](long-short-ts.html#cb312-5)  ) |>
    [](long-short-ts.html#cb312-6)    mutate(
    [](long-short-ts.html#cb312-7)      st = z$st,
    [](long-short-ts.html#cb312-8)      type = z$type,
    [](long-short-ts.html#cb312-9)      period = z$period,
    [](long-short-ts.html#cb312-10)      description = z$description,
    [](long-short-ts.html#cb312-11)      sn = z$sn
    [](long-short-ts.html#cb312-12)    ) |>
    [](long-short-ts.html#cb312-13)    as_tibble()
    [](long-short-ts.html#cb312-14)}
    [](long-short-ts.html#cb312-15)short <- Mcomp::M3 |>
    [](long-short-ts.html#cb312-16)  subset("yearly") |>
    [](long-short-ts.html#cb312-17)  purrr::map_dfr(m3totsibble) |>
    [](long-short-ts.html#cb312-18)  group_by(sn) |>
    [](long-short-ts.html#cb312-19)  mutate(n = max(row_number())) |>
    [](long-short-ts.html#cb312-20)  filter(n <= 20) |>
    [](long-short-ts.html#cb312-21)  ungroup() |>
    [](long-short-ts.html#cb312-22)  as_tsibble(index = index, key = c(sn, period, st))

Now we can apply an ARIMA model to each series.
    
    
    [](long-short-ts.html#cb313-1)short_fit <- short |>
    [](long-short-ts.html#cb313-2)  model(arima = ARIMA(value))

Of the 152 series, 21 had models with zero parameters (white noise and random walks), 86 had models with one parameter, 31 had models with two parameters, 13 had models with three parameters, and only 1 series had a model with four parameters.

### Forecasting very long time series[](long-short-ts.html#forecasting-very-long-time-series)

Most time series models do not work well for very long time series. The problem is that real data do not come from the models we use. When the number of observations is not large (say up to about 200) the models often work well as an approximation to whatever process generated the data. But eventually we will have enough data that the difference between the true process and the model starts to become more obvious. An additional problem is that the optimisation of the parameters becomes more time consuming because of the number of observations involved.

What to do about these issues depends on the purpose of the model. A more flexible and complicated model could be used, but this still assumes that the model structure will work over the whole period of the data. A better approach is usually to allow the model itself to change over time. ETS models are designed to handle this situation by allowing the trend and seasonal terms to evolve over time. ARIMA models with differencing have a similar property. But dynamic regression models do not allow any evolution of model components.

If we are only interested in forecasting the next few observations, one simple approach is to throw away the earliest observations and only fit a model to the most recent observations. Then an inflexible model can work well because there is not enough time for the relationships to change substantially.

For example, we fitted a dynamic harmonic regression model to 26 years of weekly gasoline production in Section [13.1](weekly.html#weekly). It is, perhaps, unrealistic to assume that the seasonal pattern remains the same over nearly three decades. So we could simply fit a model to the most recent years instead.


---

## 13.8 Forecasting on training and test sets[](training-test.html#training-test)

Typically, we compute one-step forecasts on the training data (the “fitted values”) and multi-step forecasts on the test data. However, occasionally we may wish to compute multi-step forecasts on the training data, or one-step forecasts on the test data.

### Multi-step forecasts on training data[](training-test.html#multi-step-forecasts-on-training-data)

We normally define fitted values to be one-step forecasts on the training set (see Section [5.3](residuals.html#residuals)), but a similar idea can be used for multi-step forecasts. We will illustrate the method using an ARIMA model for the Australian take-away food expenditure. The last five years are used for a test set, and the forecasts are plotted in Figure [13.9](training-test.html#fig:isms).
    
    
    [](training-test.html#cb314-1)training <- auscafe |> filter(year(Month) <= 2013)
    [](training-test.html#cb314-2)test <- auscafe |> filter(year(Month) > 2013)
    [](training-test.html#cb314-3)cafe_fit <- training |>
    [](training-test.html#cb314-4)  model(ARIMA(log(Turnover)))
    [](training-test.html#cb314-5)cafe_fit |>
    [](training-test.html#cb314-6)  forecast(h = 60) |>
    [](training-test.html#cb314-7)  autoplot(auscafe) +
    [](training-test.html#cb314-8)  labs(title = "Australian food expenditure",
    [](training-test.html#cb314-9)       y = "$ (billions)")

Figure 13.9: Forecasts from an ARIMA model fitted to the Australian monthly expenditure on cafés, restaurants and takeaway food services. 

The `fitted()` function has an `h` argument to allow for \\(h\\)-step “fitted values” on the training set. Figure [13.10](training-test.html#fig:isms2) is a plot of 12-step (one year) forecasts on the training set. Because the model involves both seasonal (lag 12) and first (lag 1) differencing, it is not possible to compute these forecasts for the first few observations.
    
    
    [](training-test.html#cb315-1)fits12 <- fitted(cafe_fit, h = 12)
    [](training-test.html#cb315-2)training |>
    [](training-test.html#cb315-3)  autoplot(Turnover) +
    [](training-test.html#cb315-4)  autolayer(fits12, .fitted, col = "#D55E00") +
    [](training-test.html#cb315-5)  labs(title = "Australian food expenditure",
    [](training-test.html#cb315-6)       y = "$ (billions)")

Figure 13.10: Twelve-step fitted values from an ARIMA model fitted to the Australian café training data. 

### One-step forecasts on test data[](training-test.html#one-step-forecasts-on-test-data)

It is common practice to fit a model using training data, and then to evaluate its performance on a test data set. The way this is usually done means the comparisons on the test data use different forecast horizons. In the above example, we have used the last sixty observations for the test data, and estimated our forecasting model on the training data. Then the forecast errors will be for 1-step, 2-steps, …, 60-steps ahead. The forecast variance usually increases with the forecast horizon, so if we are simply averaging the absolute or squared errors from the test set, we are combining results with different variances.

One solution to this issue is to obtain 1-step errors on the test data. That is, we still use the training data to estimate any parameters, but when we compute forecasts on the test data, we use all of the data preceding each observation (both training and test data). So our training data are for times \\(1,2,\dots,T-60\\). We estimate the model on these data, but then compute \\(\hat{y}_{T-60+h|T-61+h}\\), for \\(h=1,\dots,T-1\\). Because the test data are not used to estimate the parameters, this still gives us a “fair” forecast.

Using the same ARIMA model used above, we now apply the model to the test data.
    
    
    [](training-test.html#cb316-1)cafe_fit |>
    [](training-test.html#cb316-2)  refit(test) |>
    [](training-test.html#cb316-3)  accuracy()
    [](training-test.html#cb316-4)#> # A tibble: 1 × 10
    [](training-test.html#cb316-5)#>   .model              .type    ME  RMSE   MAE    MPE  MAPE  MASE RMSSE    ACF1
    [](training-test.html#cb316-6)#>   <chr>               <chr> <dbl> <dbl> <dbl>  <dbl> <dbl> <dbl> <dbl>   <dbl>
    [](training-test.html#cb316-7)#> 1 ARIMA(log(Turnover… Trai… -2.49  20.5  15.4 -0.169  1.06 0.236 0.259 -0.0502

Note that model is not re-estimated in this case. Instead, the model obtained previously (and stored as `cafe_fit`) is applied to the `test` data. Because the model was not re-estimated, the “residuals” obtained here are actually one-step forecast errors. Consequently, the results produced from the `accuracy()` command are actually on the test set (despite the output saying “Training set”). This approach can be used to compare one-step forecasts from different models.


---

## 13.9 Dealing with outliers and missing values[](missing-outliers.html#missing-outliers)

Real data often contains missing values, outlying observations, and other messy features. Dealing with them can sometimes be troublesome.

### Outliers[](missing-outliers.html#outliers)

Outliers are observations that are very different from the majority of the observations in the time series. They may be errors, or they may simply be unusual. (See Section [7.3](regression-evaluation.html#regression-evaluation) for a discussion of outliers in a regression context.) None of the methods we have considered in this book will work well if there are extreme outliers in the data. In this case, we may wish to replace them with missing values, or with an estimate that is more consistent with the majority of the data.

Simply replacing outliers without thinking about why they have occurred is a dangerous practice. They may provide useful information about the process that produced the data, which should be taken into account when forecasting. However, if we are willing to assume that the outliers are genuinely errors, or that they won’t occur in the forecasting period, then replacing them can make the forecasting task easier.

Figure [13.11](missing-outliers.html#fig:ahoutlier) shows the number of visitors to the Adelaide Hills region of South Australia. There appears to be an unusual observation in 2002 Q4.
    
    
    [](missing-outliers.html#cb317-1)tourism |>
    [](missing-outliers.html#cb317-2)  filter(
    [](missing-outliers.html#cb317-3)    Region == "Adelaide Hills", Purpose == "Visiting"
    [](missing-outliers.html#cb317-4)  ) |>
    [](missing-outliers.html#cb317-5)  autoplot(Trips) +
    [](missing-outliers.html#cb317-6)  labs(title = "Quarterly overnight trips to Adelaide Hills",
    [](missing-outliers.html#cb317-7)       y = "Number of trips")

Figure 13.11: Number of overnight trips to the Adelaide Hills region of South Australia. 

One useful way to find outliers is to apply `STL()` to the series with the argument `robust=TRUE`. Then any outliers should show up in the remainder series. The data in Figure [13.11](missing-outliers.html#fig:ahoutlier) have almost no visible seasonality, so we will apply STL without a seasonal component by setting `period=1`.
    
    
    [](missing-outliers.html#cb318-1)ah_decomp <- tourism |>
    [](missing-outliers.html#cb318-2)  filter(
    [](missing-outliers.html#cb318-3)    Region == "Adelaide Hills", Purpose == "Visiting"
    [](missing-outliers.html#cb318-4)  ) |>
    [](missing-outliers.html#cb318-5)  # Fit a non-seasonal STL decomposition
    [](missing-outliers.html#cb318-6)  model(
    [](missing-outliers.html#cb318-7)    stl = STL(Trips ~ season(period = 1), robust = TRUE)
    [](missing-outliers.html#cb318-8)  ) |>
    [](missing-outliers.html#cb318-9)  components()
    [](missing-outliers.html#cb318-10)ah_decomp |> autoplot()

Figure 13.12: STL decomposition of visitors to the Adelaide Hills region of South Australia, with no seasonal component. 

In the above example the outlier was easy to identify. In more challenging cases, using a boxplot of the remainder series would be useful. We can identify as outliers those that are greater than 1.5 interquartile ranges (IQRs) from the central 50% of the data. If the remainder was normally distributed, this would show 7 in every 1000 observations as “outliers”. A stricter rule is to define outliers as those that are greater than 3 interquartile ranges (IQRs) from the central 50% of the data, which would make only 1 in 500,000 normally distributed observations to be outliers. This is the rule we prefer to use.
    
    
    [](missing-outliers.html#cb319-1)outliers <- ah_decomp |>
    [](missing-outliers.html#cb319-2)  filter(
    [](missing-outliers.html#cb319-3)    remainder < quantile(remainder, 0.25) - 3*IQR(remainder) |
    [](missing-outliers.html#cb319-4)    remainder > quantile(remainder, 0.75) + 3*IQR(remainder)
    [](missing-outliers.html#cb319-5)  )
    [](missing-outliers.html#cb319-6)outliers
    [](missing-outliers.html#cb319-7)#> # A dable: 1 x 9 [1Q]
    [](missing-outliers.html#cb319-8)#> # Key:     Region, State, Purpose, .model [1]
    [](missing-outliers.html#cb319-9)#> # :        Trips = trend + remainder
    [](missing-outliers.html#cb319-10)#>   Region      State Purpose .model Quarter Trips trend remainder season_adjust
    [](missing-outliers.html#cb319-11)#>   <chr>       <chr> <chr>   <chr>    <qtr> <dbl> <dbl>     <dbl>         <dbl>
    [](missing-outliers.html#cb319-12)#> 1 Adelaide H… Sout… Visiti… stl    2002 Q4  81.1  11.1      70.0          81.1

This finds the one outlier that we suspected from Figure [13.11](missing-outliers.html#fig:ahoutlier). Something similar could be applied to the full data set to identify unusual observations in other series.

### Missing values[](missing-outliers.html#missing-values)

Missing data can arise for many reasons, and it is worth considering whether the missingness will induce bias in the forecasting model. For example, suppose we are studying sales data for a store, and missing values occur on public holidays when the store is closed. The following day may have increased sales as a result. If we fail to allow for this in our forecasting model, we will most likely under-estimate sales on the first day after the public holiday, but over-estimate sales on the days after that. One way to deal with this kind of situation is to use a dynamic regression model, with dummy variables indicating if the day is a public holiday or the day after a public holiday. No automated method can handle such effects as they depend on the specific forecasting context.

In other situations, the missingness may be essentially random. For example, someone may have forgotten to record the sales figures, or the data recording device may have malfunctioned. If the timing of the missing data is not informative for the forecasting problem, then the missing values can be handled more easily.

Finally, we might remove some unusual observations, thus creating missing values in the series.

Some methods allow for missing values without any problems. For example, the naïve forecasting method continues to work, with the most recent non-missing value providing the forecast for the future time periods. Similarly, the other benchmark methods introduced in Section [5.2](simple-methods.html#simple-methods) will all produce forecasts when there are missing values present in the historical data. The `fable` functions for ARIMA models, dynamic regression models and NNAR models will also work correctly without causing errors. However, other modelling functions do not handle missing values including `ETS()` and `STL()`.

When missing values cause errors, there are at least two ways to handle the problem. First, we could just take the section of data after the last missing value, assuming there is a long enough series of observations to produce meaningful forecasts. Alternatively, we could replace the missing values with estimates. To do this, we first fit an ARIMA model to the data containing missing values, and then use the model to interpolate the missing observations.

We will replace the outlier identified in Figure [13.12](missing-outliers.html#fig:stlahdecomp) by an estimate using an ARIMA model.
    
    
    [](missing-outliers.html#cb320-1)ah_miss <- tourism |>
    [](missing-outliers.html#cb320-2)  filter(
    [](missing-outliers.html#cb320-3)    Region == "Adelaide Hills",
    [](missing-outliers.html#cb320-4)    Purpose == "Visiting"
    [](missing-outliers.html#cb320-5)  ) |>
    [](missing-outliers.html#cb320-6)  # Remove outlying observations
    [](missing-outliers.html#cb320-7)  anti_join(outliers) |>
    [](missing-outliers.html#cb320-8)  # Replace with missing values
    [](missing-outliers.html#cb320-9)  fill_gaps()
    [](missing-outliers.html#cb320-10)ah_fill <- ah_miss |>
    [](missing-outliers.html#cb320-11)  # Fit ARIMA model to the data containing missing values
    [](missing-outliers.html#cb320-12)  model(ARIMA(Trips)) |>
    [](missing-outliers.html#cb320-13)  # Estimate Trips for all periods
    [](missing-outliers.html#cb320-14)  interpolate(ah_miss)
    [](missing-outliers.html#cb320-15)ah_fill |>
    [](missing-outliers.html#cb320-16)  # Only show outlying periods
    [](missing-outliers.html#cb320-17)  right_join(outliers |> select(-Trips))
    [](missing-outliers.html#cb320-18)#> # A tsibble: 1 x 9 [?]
    [](missing-outliers.html#cb320-19)#> # Key:       Region, State, Purpose [1]
    [](missing-outliers.html#cb320-20)#>   Region      State Purpose Quarter Trips .model trend remainder season_adjust
    [](missing-outliers.html#cb320-21)#>   <chr>       <chr> <chr>     <qtr> <dbl> <chr>  <dbl>     <dbl>         <dbl>
    [](missing-outliers.html#cb320-22)#> 1 Adelaide H… Sout… Visiti… 2002 Q4  8.50 stl     11.1      70.0          81.1

The `interpolate()` function uses the ARIMA model to estimate any missing values in the series. In this case, the outlier of 81.1 has been replaced with 8.5. The resulting series is shown in Figure [13.13](missing-outliers.html#fig:replacement-plot).

The `ah_fill` data could now be modeled with a function that does not allow missing values.
    
    
    [](missing-outliers.html#cb321-1)ah_fill |>
    [](missing-outliers.html#cb321-2)  autoplot(Trips) +
    [](missing-outliers.html#cb321-3)  autolayer(ah_fill |> filter_index("2002 Q3"~"2003 Q1"),
    [](missing-outliers.html#cb321-4)    Trips, colour="#D55E00") +
    [](missing-outliers.html#cb321-5)  labs(title = "Quarterly overnight trips to Adelaide Hills",
    [](missing-outliers.html#cb321-6)       y = "Number of trips")

Figure 13.13: Number of overnight trips to the Adelaide Hills region of South Australia with the 2002Q4 outlier being replaced using an ARIMA model for interpolation. 


---

## 13.10 Further reading[](further-reading-1.html#further-reading-1)

So many diverse topics are discussed in this chapter, that it is not possible to point to specific references on all of them. The last chapter in Ord et al. ([2017](further-reading-1.html#ref-Ord2017)) also covers “Forecasting in practice” and discusses other issues that might be of interest to readers.

### Bibliography[](bibliography.html#bibliography)

Ord, J. K., Fildes, R., & Kourentzes, N. (2017). _Principles of business forecasting_ (2nd ed.). Wessex Press Publishing Co. [__](http://amazon.com/dp/0999064916?tag=otexts20)


---

# Appendix: Using R[](appendix-using-r.html#appendix-using-r)

This book uses R and is designed to be used with R. R is free, available on almost every operating system, and there are thousands of add-on packages to do almost anything you could ever want to do. We recommend you use R with RStudio.

### Installing R and RStudio[](appendix-using-r.html#installing-r-and-rstudio)

  1. [Download and install R.](https://cran.r-project.org/)
  2. [Download and install RStudio.](https://bit.ly/rstudiodownload)
  3. Run RStudio. On the “Packages” tab, click on “Install” and install the package `fpp3` (make sure “install dependencies” is checked).


That’s it! You should now be ready to go.

### R examples in this book[](appendix-using-r.html#r-examples-in-this-book)

We provide R code for most examples in shaded boxes like this:
    
    
    [](appendix-using-r.html#cb322-1)# Load required packages
    [](appendix-using-r.html#cb322-2)library(fpp3)
    [](appendix-using-r.html#cb322-3)
    [](appendix-using-r.html#cb322-4)# Plot one time series
    [](appendix-using-r.html#cb322-5)aus_retail |>
    [](appendix-using-r.html#cb322-6)  filter(`Series ID`=="A3349640L") |>
    [](appendix-using-r.html#cb322-7)  autoplot(Turnover)
    [](appendix-using-r.html#cb322-8)
    [](appendix-using-r.html#cb322-9)# Produce some forecasts
    [](appendix-using-r.html#cb322-10)aus_retail |>
    [](appendix-using-r.html#cb322-11)  filter(`Series ID`=="A3349640L") |>
    [](appendix-using-r.html#cb322-12)  model(ETS(Turnover)) |>
    [](appendix-using-r.html#cb322-13)  forecast(h = "2 years")

These examples assume that you have the `fpp3` package loaded as shown above. This needs to be done at the start of every R session, but it won’t be included in our examples.

Sometimes we assume that the R code that appears earlier in the same chapter of the book has also been run; so it is best to work through the R code in the order provided within each chapter.

### Getting started with R[](appendix-using-r.html#getting-started-with-r)

If you have never previously used R, please work through the first section (chapters 1-8) of [“R for Data Science”](https://r4ds.hadley.nz) by Garrett Grolemund and Hadley Wickham. While this does not cover time series or forecasting, it will get you used to the basics of the R language, and the `tidyverse` packages. The [Coursera R Programming](https://www.coursera.org/learn/r-programming) course is also highly recommended.

You will learn how to use R for forecasting using the exercises in this book.


---

# Appendix: For instructors[](appendix-for-instructors.html#appendix-for-instructors)

### Solutions to exercises[](appendix-for-instructors.html#solutions-to-exercises)

Solutions to exercises are password protected and only available to instructors. Please [complete this request form](https://goo.gl/forms/nJsXgojZlGPhZ6uu1). You will need to provide evidence that you are an instructor and not a student (e.g., a link to a university website listing you as a member of faculty). Please also use your university email address on the form.

  * Chapter 1 [qmd](https://OTexts.com/fpp3/solutions/Chapter1.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter1.html)
  * Chapter 2 [qmd](https://OTexts.com/fpp3/solutions/Chapter2.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter2.html)
  * Chapter 3 [qmd](https://OTexts.com/fpp3/solutions/Chapter3.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter3.html)
  * Chapter 4 [qmd](https://OTexts.com/fpp3/solutions/Chapter4.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter4.html)
  * Chapter 5 [qmd](https://OTexts.com/fpp3/solutions/Chapter5.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter5.html)
  * Chapter 7 [qmd](https://OTexts.com/fpp3/solutions/Chapter7.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter7.html)
  * Chapter 8 [qmd](https://OTexts.com/fpp3/solutions/Chapter8.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter8.html)
  * Chapter 9 [qmd](https://OTexts.com/fpp3/solutions/Chapter9.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter9.html)
  * Chapter 10 [qmd](https://OTexts.com/fpp3/solutions/Chapter10.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter10.html)
  * Chapter 11 [qmd](https://OTexts.com/fpp3/solutions/Chapter11.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter11.html)
  * Chapter 12 [qmd](https://OTexts.com/fpp3/solutions/Chapter12.qmd) [html](https://OTexts.com/fpp3/solutions/Chapter12.html)


The qmd files use [this theme](https://OTexts.com/fpp3/solutions/fpp3.scss).

### Slides[](appendix-for-instructors.html#slides)

[The slides used in the embedded videos](https://github.com/robjhyndman/fpp3_slides) are available via github. You are welcome to adapt these slides for your own purposes.

### Past exams[](appendix-for-instructors.html#past-exams)

Here are three exams written by the authors for our own forecasting courses:

  * [Sample exam 1](https://OTexts.com/fpp3/solutions/sample_exam_1.pdf)
  * [Sample exam 2](https://OTexts.com/fpp3/solutions/sample_exam_2.pdf)
  * [Sample exam 3](https://OTexts.com/fpp3/solutions/sample_exam_3.pdf)


### Python resources[](appendix-for-instructors.html#python-resources)

For those teaching using Python, there is now a [Python edition of “ _Forecasting Principles and Practice_ ”](https://OTexts.com/fpppy).


---

# Appendix: Reviews[](appendix-reviews.html#appendix-reviews)

  * [Amazon reviews](http://www.amazon.com/Forecasting-principles-practice-Rob-Hyndman/product-reviews/0987507109/?tag=otexts-21)
  * [Review from Sandro Saitta in Swiss Analytics, April 2015, p.5. Republished at Data Mining Research.](https://OTexts.com/fpp2/extrafiles/SwissAnalytics201501.pdf)
  * [Review from Steve Miller on Information Management, April 2015](https://web.archive.org/web/20200220174633/https://www.information-management.com/opinion/business-analytics-and-forecasting-revisited)
  * [Review from Stephan Kolassa in Foresight, Fall 2010.](extrafiles/Kolassa-review.pdf)


### Testimonials from fellow educators[](appendix-reviews.html#testimonials-from-fellow-educators)

_Added August 2020_

> “This book is an essential resource for students and practitioners alike. It takes a fresh look on important time series and forecasting concepts. The illustration of theoretical concepts in R is invaluable: it not only helps readers gain hands-on experience but also makes learning the material more fun. I enjoyed teaching from the book, and my students loved the class!”

> “This text provides a wonderful overview of time series methods for the practitioner. Indeed it is an excellent book for training MBAs and MSBAs in the basics of using Time Series models which served as an elective class in both programs. The examples are easy to follow and the R-scripts work well and are effective. The explanation of the methods is clear and concise. I’m sure it helped me win a teaching award!”

> “I have been teaching financial econometrics for over 10 years and FPP is one of the best applied books I have come across. It encapsulates a sound introduction to time series forecasting, capturing the statistical principles via coherent “learning by doing” processes in the R language. Feedback from former students suggests it is always a useful reference for them as they start their career in data analytics and financial forecasting. Finally, the authors are very approachable and have provided fantastic help and guidance on teaching time series forecasting.”

> “The text is a great resource as at provides a hands on approach to learning forecasting. I wish more texts would follow this format and philosophy.”

> “This is a great online textbook. I used several sections for my own course which introduces forecasting techniques for time series in the energy field, and I found the material, including the examples and exercises, extremely helpful. Thank you for the great effort of compiling this resource!”

> “This book provides students with little knowledge of mathematics or statistics with an understanding of forecasting methods through an accessible, well-written and practice-oriented presentation. This book is a must for my students following a Master in Business Administration.”

> “I use this textbook for a short workshop course on forecasting for practitioners, and the structure of the book - overview of topics followed by examples in R really helps my students understand concepts well. Highly recommended.”

> “After having been introduced to the world of forecasting myself as a student with the book ‘Forecasting: methods and applications’ (Makridakis, Wheelwright & Hyndman, 1998), I have been using the successor ‘Forecasting Principles & Practice’ of Rob Hyndman and George Athanasopoulos for master students in Business Engineering and Business Administration for many years now. It is a very accessible book, which is very easy to use due to its online format, and it is always kept up to date. The students very much appreciate the seamless intertwining of the theory, the many examples and the applications in R. The book is ideal to introduce students to the most important forecasting techniques through interesting examples, with a healthy balance between theoretical depth and relevant applications.”

> “I chose it as a prescribed text book for the Business Forecasting course, which is a core course for Masters of Information Technology and Analytics program in our Business School. Excellent book IMHO.”

> “The book covers basic forecasting tools, like exponential smoothing, and more complex forecasting methods. All with practical R examples such that the students after the course are well prepared for a future in practical forecasting. The book is also very well received by the students.”

> “This book is a great support for students and teachers. With its focus on forecasting and the practical applications in R it is indispensable for business students at our university. And the integration with tidyverse is highly appreciated. Thank You!”

### Testimonials from practitioners and students[](appendix-reviews.html#testimonials-from-practitioners-and-students)

  * Practitioner, August 2020.

> The book allows someone like me, a complete beginner in forecasting, to learn, gain confidence, and practice skills that are not only valuable, but greatly interesting. Within the realm of forecasting, I’m not sure where I’d be without this wonderful resource made available to the public.

  * [ETC3550, Applied forecasting](https://handbook.monash.edu/2020/units/ETC3550?year=2020) student, Semester 1, 2020.

> Forecasting: Principles and Practice was a pleasant surprise right from the beginning. It is very rare to have such plentiful amount of information available for free within the University environment. Allowing students such as myself to gain free access is something that encourages individuals to read through and learn more about the subject. Furthermore, the easy to use online format made this one of (if not) the most accessible University textbook I’ve read. Moreover, the practicality and hands on approach with direct examples (and real-world data) reinforces concepts in an enjoyable way. Being able to show the applications of what you are learning interested me to delve deeper and foster a curious attitude towards each topic. I also appreciated the concise nature which allowed me to read without feeling overloaded or exhausted. Overall, a fantastic resource for those with even the slightest interest in forecasting and data science.

  * [ETF3231, Business forecasting](https://handbook.monash.edu/2020/units/ETF3231?year=2020) student, Semester 1, 2020.

> The textbook used in the Business forecasting course is an online book that contains all the materials seen in class. The course content is based on slides but the book is a good additional support. It has been very useful for me to be able to reiterate certain points that I had less understood during the lecture. Moreover, the book is very well constructed, and the content well explained with practical examples, as seen in the course, which made my study very smooth. Finally, the exercises practised during the tutorials are from the textbook. I would recommend everyone to browse the book for the more complicated points of the material!




---

# Bibliography[](bibliography.html#bibliography)

Anscombe, F. J. (1973). Graphs in statistical analysis. _The American Statistician_ , _27_(1), 17–21. [__](https://doi.org/10.1080/00031305.1973.10478966)

Armstrong, J. S. (1978). _Long-range forecasting: From crystal ball to computer_. John Wiley & Sons. [__](http://amazon.com/dp/0471030023?tag=otexts20)

Armstrong, J. S. (Ed.). (2001). _Principles of forecasting: A handbook for researchers and practitioners_. Kluwer Academic Publishers. [__](http://amazon.com/dp/0792379306?tag=otexts20)

Athanasopoulos, G., Ahmed, R. A., & Hyndman, R. J. (2009). Hierarchical forecasts for Australian domestic tourism. _International Journal of Forecasting_ , _25_ , 146–166. [__](https://doi.org/10.1016/j.ijforecast.2008.07.004)

Athanasopoulos, G., Gamakumara, P., Panagiotelis, A., Hyndman, R. J., & Affan, M. (2020). Hierarchical forecasting. In P. Fuleky (Ed.), _Macroeconomic forecasting in the era of big data_ (pp. 689–719). Springer. [__](https://doi.org/10.1007/978-3-030-31150-6_21)

Athanasopoulos, G., & Hyndman, R. J. (2008). Modelling and forecasting Australian domestic tourism. _Tourism Management_ , _29_(1), 19–31. [__](https://doi.org/10.1016/j.tourman.2007.04.009)

Athanasopoulos, G., Hyndman, R. J., Kourentzes, N., & Petropoulos, F. (2017). Forecasting with temporal hierarchies. _European Journal of Operational Research_ , _262_(1), 60–74. [__](https://doi.org/10.1016/j.ejor.2017.02.046)

Athanasopoulos, G., Poskitt, D. S., & Vahid, F. (2012). Two canonical VARMA forms: Scalar component models vis-à-vis the echelon form. _Econometric Reviews_ , _31_(1), 60–83. [__](https://doi.org/10.1080/07474938.2011.607088)

Bandara, K., Hyndman, R. J., & Bergmeir, C. (2025). MSTL: A seasonal-trend decomposition algorithm for time series with multiple seasonal patterns. _International J Operational Research_ , _52_(1). [__](https://doi.org/10.1504/IJOR.2022.10048281)

Bates, J. M., & Granger, C. W. J. (1969). The combination of forecasts. _Operational Research Quarterly_ , _20_(4), 451–468. [__](https://doi.org/10.1057/jors.1969.103)

Bergmeir, C., Hyndman, R. J., & Benítez, J. M. (2016). Bagging exponential smoothing methods using STL decomposition and Box-Cox transformation. _International Journal of Forecasting_ , _32_(2), 303–312. [__](https://doi.org/10.1016/j.ijforecast.2015.07.002)

Bergmeir, C., Hyndman, R. J., & Koo, B. (2018). A note on the validity of cross-validation for evaluating autoregressive time series prediction. _Computational Statistics and Data Analysis_ , _120_ , 70–83. [__](https://doi.org/10.1016/j.csda.2017.11.003)

Bickel, P. J., & Doksum, K. A. (1981). An analysis of transformations revisited. _Journal of the American Statistical Association_ , _76_(374), 296–311. [__](https://doi.org/10.1080/01621459.1981.10477649)

Box, G. E. P., & Cox, D. R. (1964). An analysis of transformations. _Journal of the Royal Statistical Society. Series B, Statistical Methodology_ , _26_(2), 211–252. [__](https://doi.org/10.1111/j.2517-6161.1964.tb00553.x)

Box, G. E. P., & Jenkins, G. M. (1970). _Time series analysis: Forecasting and control_. Holden-Day. 

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). _Time series analysis: Forecasting and control_ (5th ed). John Wiley & Sons. [__](http://amazon.com/dp/1118675029?tag=otexts20)

Brockwell, P. J., & Davis, R. A. (2016). _Introduction to time series and forecasting_ (3rd ed). Springer. [__](http://amazon.com/dp/3319298526?tag=otexts20)

Brown, R. G. (1959). _Statistical forecasting for inventory control_. McGraw/Hill. 

Buehler, R., Messervey, D., & Griffin, D. (2005). Collaborative planning and prediction: Does group discussion affect optimistic biases in time estimation? _Organizational Behavior and Human Decision Processes_ , _97_(1), 47–63. [__](https://doi.org/10.1016/j.obhdp.2005.02.004)

Christou, V., & Fokianos, K. (2015). On count time series prediction. _Journal of Statistical Computation and Simulation_ , _85_(2), 357–373. [__](https://doi.org/10.1080/00949655.2013.823612)

Clemen, R. (1989). Combining forecasts: A review and annotated bibliography. _International Journal of Forecasting_ , _5_(4), 559–583. [__](https://doi.org/10.1016/0169-2070\(89\)90012-5)

Cleveland, R. B., Cleveland, W. S., McRae, J. E., & Terpenning, I. J. (1990). STL: A seasonal-trend decomposition procedure based on loess. _Journal of Official Statistics_ , _6_(1), 3–33. [__](http://bit.ly/stl1990)

Cleveland, W. S. (1993). _Visualizing data_. Hobart Press. [__](http://amazon.com/dp/0963488406?tag=otexts20)

Croston, J. D. (1972). Forecasting and stock control for intermittent demands. _Operational Research Quarterly_ , _23_(3), 289–303. [__](https://doi.org/10.2307/3007885)

Dagum, E. B., & Bianconcini, S. (2016). _Seasonal adjustment methods and real time trend-cycle estimation_. Springer. [__](http://amazon.com/dp/3319318209?tag=otexts20)

Eroglu, C., & Croxton, K. L. (2010). Biases in judgmental adjustments of statistical forecasts: The role of individual differences. _International Journal of Forecasting_ , _26_(1), 116–133. [__](https://doi.org/10.1016/j.ijforecast.2009.02.005)

Fan, S., & Hyndman, R. J. (2012). Short-term load forecasting based on a semi-parametric additive model. _IEEE Transactions on Power Systems_ , _27_(1), 134–141. [__](https://doi.org/10.1109/TPWRS.2011.2162082)

Fildes, R., & Goodwin, P. (2007a). Against your better judgment? How organizations can improve their use of management judgment in forecasting. _Interfaces_ , _37_(6), 570–576. [__](https://doi.org/10.1287/inte.1070.0309)

Fildes, R., & Goodwin, P. (2007b). Good and bad judgment in forecasting: Lessons from four companies. _Foresight: The International Journal of Applied Forecasting_ , _8_ , 5–10. 

Franses, P. H., & Legerstee, R. (2013). Do statistical forecasting models for SKU-level data benefit from including past expert knowledge? _International Journal of Forecasting_ , _29_(1), 80–87. [__](https://doi.org/10.1016/j.ijforecast.2012.05.008)

Gardner, E. S. (1985). Exponential smoothing: The state of the art. _Journal of Forecasting_ , _4_(1), 1–28. [__](https://doi.org/10.1002/for.3980040103)

Gardner, E. S. (2006). Exponential smoothing: The state of the art — Part II. _International Journal of Forecasting_ , _22_ , 637–666. [__](https://doi.org/10.1016/j.ijforecast.2006.03.005)

Gardner, E. S., & McKenzie, E. (1985). Forecasting trends in time series. _Management Science_ , _31_(10), 1237–1246. [__](https://doi.org/10.1287/mnsc.31.10.1237)

Gneiting, T., & Katzfuss, N. (2014). Probabilistic forecasting. _Annual Review of Statistics and Its Application_ , _1_(1), 125–151. [__](https://doi.org/10.1146/annurev-statistics-062713-085831)

Goodwin, P., & Wright, G. (2009). _Decision analysis for management judgment_ (4th ed). John Wiley & Sons. [__](http://amazon.com/dp/0470714395?tag=otexts20)

Green, K. C., & Armstrong, J. S. (2007). Structured analogies for forecasting. _International Journal of Forecasting_ , _23_(3), 365–376. [__](https://doi.org/10.1016/j.ijforecast.2007.05.005)

Gross, C. W., & Sohl, J. E. (1990). Disaggregation methods to expedite product line forecasting. _Journal of Forecasting_ , _9_ , 233–254. [__](https://doi.org/10.1002/for.3980090304)

Groves, R. M., Fowler, F. J., Couper, M. P., Lepkowski, J. M., Singer, E., & Tourangeau, R. (2009). _Survey methodology_ (2nd ed). John Wiley & Sons. [__](http://amazon.com/dp/0470465468?tag=otexts20)

Guerrero, V. M. (1993). Time-series analysis supported by power transformations. _Journal of Forecasting_ , _12_(1), 37–48. [__](https://doi.org/10.1002/for.3980120104)

Hamilton, J. D. (1994). _Time series analysis_. Princeton University Press, Princeton. [__](http://amazon.com/dp/0691042896?tag=otexts20)

Harrell, F. E. (2015). _Regression modeling strategies: With applications to linear models, logistic and ordinal regression, and survival analysis_ (2nd ed). Springer. [__](http://amazon.com/dp/3319194240?tag=otexts20)

Harris, R., & Sollis, R. (2003). _Applied time series modelling and forecasting_. John Wiley & Sons. [__](http://amazon.com/dp/0470844434?tag=otexts20)

Harvey, N. (2001). Improving judgment in forecasting. In J. S. Armstrong (Ed.), _Principles of forecasting: A handbook for researchers and practitioners_ (pp. 59–80). Kluwer Academic Publishers. [__](https://doi.org/10.1007/978-0-306-47630-3_4)

Hewamalage, H., Bergmeir, C., & Bandara, K. (2021). Recurrent neural networks for time series forecasting: Current status and future directions. _International Journal of Forecasting_ , _37_(1), 388–427. [__](https://doi.org/10.1016/j.ijforecast.2020.06.008)

Holt, C. C. (1957). _Forecasting seasonals and trends by exponentially weighted averages_ (ONR Memorandum No. 52). Carnegie Institute of Technology, Pittsburgh USA. Reprinted in the _International Journal of Forecasting_ , 2004. [__](https://doi.org/10.1016/j.ijforecast.2003.09.015)

Hyndman, R. J., Ahmed, R. A., Athanasopoulos, G., & Shang, H. L. (2011). Optimal combination forecasts for hierarchical time series. _Computational Statistics and Data Analysis_ , _55_(9), 2579–2589. [__](https://doi.org/10.1016/j.csda.2011.03.006)

Hyndman, R. J., & Fan, S. (2010). Density forecasting for long-term peak electricity demand. _IEEE Transactions on Power Systems_ , _25_(2), 1142–1153. [__](https://doi.org/10.1109/TPWRS.2009.2036017)

Hyndman, R. J., & Khandakar, Y. (2008). Automatic time series forecasting: The forecast package for R. _Journal of Statistical Software_ , _27_(1), 1–22. [__](https://doi.org/10.18637/jss.v027.i03)

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. _International Journal of Forecasting_ , _22_(4), 679–688. [__](https://doi.org/10.1016/j.ijforecast.2006.03.001)

Hyndman, R. J., Koehler, A. B., Ord, J. K., & Snyder, R. D. (2008). _Forecasting with exponential smoothing: The state space approach_. Springer-Verlag. [__](http://www.exponentialsmoothing.net)

Hyndman, R. J., Wang, E., & Laptev, N. (2015). Large-scale unusual time series detection. _Proceedings of the IEEE International Conference on Data Mining_ , 1616–1619. [__](https://doi.org/10.1109/ICDMW.2015.104)

Izenman, A. J. (2008). _Modern multivariate statistical techniques: Regression, classification and manifold learning_. Springer. [__](http://amazon.com/dp/0387781889?tag=otexts20)

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). _An introduction to statistical learning: With applications in R_. Springer. [__](http://amazon.com/dp/1071614177?tag=otexts20)

Kahn, K. B. (2006). _New product forecasting: An applied approach_. M.E. Sharp. [__](http://amazon.com/dp/0765616092?tag=otexts20)

Kahneman, D., & Lovallo, D. (1993). Timid choices and bold forecasts: A cognitive perspective on risk taking. _Management Science_ , _39_(1), 17–31. [__](https://doi.org/10.1287/mnsc.39.1.17)

Kang, Y., Hyndman, R. J., & Smith-Miles, K. (2017). Visualising forecasting algorithm performance using time series instance spaces. _International Journal of Forecasting_ , _33_(2), 345–358. [__](https://doi.org/10.1016/j.ijforecast.2016.09.004)

Kourentzes, N., & Athanasopoulos, G. (2019). Cross-temporal coherent forecasts for Australian tourism. _Annals of Tourism Research_ , _75_ , 393–409. [__](https://doi.org/10.1016/j.annals.2019.02.001)

Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root: How sure are we that economic time series have a unit root? _Journal of Econometrics_ , _54_(1-3), 159–178. [__](https://doi.org/10.1016/0304-4076\(92\)90104-Y)

Lahiri, S. N. (2003). _Resampling methods for dependent data_. Springer Science & Business Media. [__](http://amazon.com/dp/0387009280?tag=otexts20)

Lawrence, M., Goodwin, P., O’Connor, M., & Önkal, D. (2006). Judgmental forecasting: A review of progress over the last 25 years. _International Journal of Forecasting_ , _22_(3), 493–518. [__](https://doi.org/10.1016/j.ijforecast.2006.03.007)

Lütkepohl, H. (2007). General-to-specific or specific-to-general modelling? An opinion on current econometric terminology. _Journal of Econometrics_ , _136_(1), 234–319. [__](https://doi.org/10.1016/j.jeconom.2005.11.014)

Morwitz, V. G., Steckel, J. H., & Gupta, A. (2007). When do purchase intentions predict sales? _International Journal of Forecasting_ , _23_(3), 347–364. [__](https://doi.org/10.1016/j.ijforecast.2007.05.015)

Önkal, D., Sayım, K. Z., & Gönül, M. S. (2013). Scenarios as channels of forecast advice. _Technological Forecasting and Social Change_ , _80_(4), 772–788. [__](https://doi.org/10.1016/j.techfore.2012.08.015)

Ord, J. K., Fildes, R., & Kourentzes, N. (2017). _Principles of business forecasting_ (2nd ed.). Wessex Press Publishing Co. [__](http://amazon.com/dp/0999064916?tag=otexts20)

Panagiotelis, A., Athanasopoulos, G., Gamakumara, P., & Hyndman, R. J. (2021). Forecast reconciliation: A geometric view with new insights on bias correction. _International Journal of Forecasting_ , _37_(1), 343–359. [__](https://doi.org/10.1016/j.ijforecast.2020.06.004)

Panagiotelis, A., Gamakumara, P., Athanasopoulos, G., & Hyndman, R. J. (2023). Probabilistic forecast reconciliation: Properties, evaluation and score optimisation. _European J Operational Research_ , _306_(2), 693–706. [__](https://doi.org/10.1016/j.ejor.2022.07.040)

Pankratz, A. E. (1991). _Forecasting with dynamic regression models_. John Wiley & Sons. [__](http://amazon.com/dp/0471615285?tag=otexts20)

Pegels, C. C. (1969). Exponential forecasting: Some new variations. _Management Science_ , _15_(5), 311–315. [__](https://doi.org/10.1287/mnsc.15.5.311)

Peña, D., Tiao, G. C., & Tsay, R. S. (Eds.). (2001). _A course in time series analysis_. John Wiley & Sons. [__](http://amazon.com/dp/047136164X?tag=otexts20)

Pfaff, B. (2008). _Analysis of integrated and cointegrated time series with R_. Springer Science & Business Media. [__](http://amazon.com/dp/0387759662?tag=otexts20)

Randall, D. M., & Wolff, J. A. (1994). The time interval in the intention-behaviour relationship: Meta-analysis. _British Journal of Social Psychology_ , _33_(4), 405–418. [__](https://doi.org/10.1111/j.2044-8309.1994.tb01037.x)

Rowe, G. (2007). A guide to Delphi. _Foresight: The International Journal of Applied Forecasting_ , _8_ , 11–16. 

Rowe, G., & Wright, G. (1999). The Delphi technique as a forecasting tool: Issues and analysis. _International Journal of Forecasting_ , _15_(4), 353–375. [__](https://doi.org/10.1016/S0169-2070\(99\)00018-7)

Sanders, N., Goodwin, P., Önkal, D., Gönül, M. S., Harvey, N., Lee, A., & Kjolso, L. (2005). When and how should statistical forecasts be judgmentally adjusted? _Foresight: The International Journal of Applied Forecasting_ , _1_(1), 5–23. 

Sheather, S. J. (2009). _A modern approach to regression with R_. Springer. [__](http://amazon.com/dp/0387096078?tag=otexts20)

Shenstone, L., & Hyndman, R. J. (2005). Stochastic models underlying Croston’s method for intermittent demand forecasting. _Journal of Forecasting_ , _24_(6), 389–402. [__](https://doi.org/10.1002/for.963)

Syntetos, A. A., & Boylan, J. E. (2001). On the bias of intermittent demand estimates. _International Journal of Production Economics_ , _71_ , 457–466. [__](https://doi.org/10.1016/S0925-5273\(00\)00143-2)

Taylor, J. W. (2003). Exponential smoothing with a damped multiplicative trend. _International Journal of Forecasting_ , _19_(4), 715–725. [__](https://doi.org/10.1016/S0169-2070\(03\)00003-7)

Taylor, S. J., & Letham, B. (2018). Forecasting at scale. _The American Statistician_ , _72_(1), 37–45. [__](https://doi.org/10.1080/00031305.2017.1380080)

Theodosiou, M. (2011). Forecasting monthly and quarterly time series using STL decomposition. _International Journal of Forecasting_ , _27_(4), 1178–1195. [__](https://doi.org/10.1016/j.ijforecast.2010.11.002)

Unwin, A. (2015). _Graphical data analysis with R_. Chapman; Hall/CRC. [__](http://amazon.com/dp/1498715230?tag=otexts20)

Wang, X., Hyndman, R. J., Li, F., & Kang, Y. (2023). Forecast combinations: An over 50-year review. _International J Forecasting_ , _39_(4), 1518–1547. [__](https://doi.org/10.1016/j.ijforecast.2022.11.005)

Wang, X., Smith, K. A., & Hyndman, R. J. (2006). Characteristic-based clustering for time series data. _Data Mining and Knowledge Discovery_ , _13_(3), 335–364. [__](https://doi.org/10.1007/s10618-005-0039-x)

Wickramasuriya, S. L., Athanasopoulos, G., & Hyndman, R. J. (2019). Optimal forecast reconciliation for hierarchical and grouped time series through trace minimization. _Journal of the American Statistical Association_ , _114_(526), 804–819. [__](https://doi.org/10.1080/01621459.2018.1448825)

Winkler, R. L. (1972). A decision-theoretic approach to interval estimation. _Journal of the American Statistical Association_ , _67_(337), 187–191. [__](https://doi.org/10.1080/01621459.1972.10481224)

Winters, P. R. (1960). Forecasting sales by exponentially weighted moving averages. _Management Science_ , _6_(3), 324–342. [__](https://doi.org/10.1287/mnsc.6.3.324)

Young, P. C., Pedregal, D. J., & Tych, W. (1999). Dynamic harmonic regression. _Journal of Forecasting_ , _18_ , 369–394. [__](https://doi.org/10.1002/\(SICI\)1099-131X\(199911\)18:6%3C369::AID-FOR748%3E3.0.CO;2-K)
