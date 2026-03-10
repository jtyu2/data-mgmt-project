## Analyzing the Relationship Between Unemployment Rates and Median Household Income in the US

## Overview: 
In this project, we have decided to analyze the relationship between unemployment rates and median household income across different states between the United States. For almost all households, economic conditions influence the income levels, and unemployment is a key factor of economic health. By integrating data from many sources that we found, our project aims to examine how changes in unemployment correlate with patterns in income over time and across different geographical regions. 
This project combines two datasets/ The first is the unemployment rate data from the Federal Reserve Economic Data API, also known as FRED. The second is the median household income data from the US Census Bureau. These data sets share many attributes that can be beneficial to our project such as geographic location (classified by state) and time period (by year), which allows them to be integrated into one data set for analysis. 
The workflow involves many different states of the data lifecycle, including data acquisition, integration, cleaning, etc. We will collect the data using API’s and publicly available datasets, store it in structured formats, and process it. The integrated dataset we will create will be analyzed to identify possible patterns and trends in income levels and unemployment. We will also produce visualizations that can illustrate the relationship between these variables. 
Overall, this project will allow us to apply practices that we have been taught in class including how to ethically handle data, how to integrate data from different sources, and include reproducible research. 

## Team Member roles: 
:) - Mehr Bhatia and Jonathan Yu

Mehr: Find reliable datasets, Access datasets through APIs, define directory structure, store datasets, data cleaning

Jonathan: Help fill missing values, work on initial data integration including summary stats

Mehr & Jonathan: Conduct analysis and create visualizations, document steps need to reproduce the analysis

## Research question
Throughout this project, we aim to answer the following questions:

What is the relationship between unemployment rates and median household income in the United States?

How does it vary by state and time?

These questions will be addressed through the integration and analysis of our datasets that capture economic indicators across many time periods and states. 


## Datasets

- **Unemployment Rate Data**
  - U.S. unemployment rate over time  
  - Source: Federal Reserve Economic Data (FRED)  
  - Access: API  
  - Fields available: State, date  

- **Median Household Income**
  - Source: U.S. Census Bureau  
  - Access: API or downloadable datasets  
  - Fields available: State, year (date)  

Both datasets are from trustworthy, widely used sources and can be merged and compared using **state** and potentially **date/year** fields.

---

## Timeline

| Date        | Tasks Done |
|------------|------------|
| 3.21 (wk 1–2) | Data acquisition – Access datasets via API, download, and store raw data |
| 3.28 (wk 3)   | Data quality assessment and cleaning – Identify missing/inconsistent values and address by supplementing with other sources or other strategies |
| 4.11 (wk 4–5) | Data integration and analysis – Summary statistics, charts, and visualizations |
| 5.2 (wk 6–9)  | Split writing for final submission deliverable |

After initial data acquisition and cleaning, the main analysis of the relationship between median household income and unemployment rate data will begin with several summary statistics and visualization techniques. Basic descriptive statistics like mean, median, and standard deviation will help us learn the shape of the datasets themselves, while scatterplots and a more in-depth regression analysis will help us visualize and hypothesize their potential relationships. 
Supplementing quantitative analysis with qualitative research will prove crucial to our conclusions. This is why we have left more time in our timeline to write our final report. Macroeconomic drivers and events will shape each of these datasets by themselves; comparing and contrasting how these events impact these groups will give us huge clues to their relationship. Quantitative analysis can show us how they are related, but qualitative research will help us think about why they are related. This approach will hopefully allow us to reach a holistic, verified conclusion on the relationship between these datasets, and make it easier to reach a conclusion than if we tried to do the analysis with only one part.

## Constraints:
Throughout our project we anticipate coming across several limitations. Firstly, the datasets may cover different time periods and/or have different reporting frequencies. This can cause some integration difficulties-  standardizing reporting dates would be difficult as we may lose some nuances in the seasonal nature of unemployment rate data. Making conclusions based on each state’s relationship to these statistics will also require careful handling, as we do not want to misrepresent any state in our analysis. The missing values may also be a constraint as it will need thorough data cleaning. We would like to avoid cleaning these values by dropping them, so we will have to think about imputation methods so our project still captures the relationship of these data over time accurately. There may be differences in naming conventions, such as abbreviated states rather than full names. We can include a short script to make this data usable. Finally, one of the biggest constraints that may be prevalent in our project is if there are issues in our datasets, we may not be able to find other datasets we can use in this project. The datasets we have currently come from government sources and have been collected for many years. This makes them reliable but it also means that finding alternative sources with the same credibility and accuracy may be a challenge.

## Gaps:
Our data is restricted to data in the United States, so our conclusions will have limited reach. Additionally, our team would love to integrate SQL into this project for data processing and analysis, so we will need to do our own research and learn along in class. These are two main gaps that stick out to us in terms of the scope and accuracy of the final result, as well as in our own knowledge. We hope to supplement through in-class learning and consultation.
