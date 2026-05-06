# Analyzing State-Level Unemployment and Median Household Income (2018-2022)

**Contributions:**
* Jonathan Yu [jtyu2]
* Mehr Bhatia [mehrbhatia]

Jonathan pushed all the final code to the GitHub, but the coding work was roughly split as follows:

* **Mehr**: 

    *  *Coding*: Data quality and cleaning (data_clean_merge), storage and organization, data integration
    * *README/report*: Summary, data profile, data quality, findings, and future work

* **Jonathan**: 
    * *Coding*: API keys + data fetching (data_fetch.py), analysis (analyze.py), Workflow automation, Metadata, 
    * *README/report*: Data cleaning, challenges, and reproducing 

All coding and README parts were ultimately completed collaboratively, especially debugging, editing, and proofreading.


---

### Summary
This project examines the relationship between state-level unemployment rates and median household income in the United States. Our motivation for this project is that unemployment and household income are both common measures of economic well-being but they both describe different parts of a state’s economic condition. Unemployment rates show the share of the labor force that is actively looking for work while median household income is more of a summary of the income level in a typical household. Looking at these indicators together can help show whether states with higher unemployment also have lower household income, or if their relationship is more complicated than that. 

The main research questions are what is the relationship between unemployment rates and median household income in the United States and how does it vary by state and time? To answer these questions this project uses two datasets. The first dataset is monthly employment-rate data collected from the Federal Reserve Bank of St. Louis FRED API. The second dataset is the median household income from the U.S. Census Bureau American Community Survey. These datasets can be integrated by state and year after cleaning their different schemas. 

The project follows a basic data lifecycle model: acquisition, storage, cleaning, integration, analysis, documentation, and preservation. Care is taken in storing raw data so that the original files remain unchanged and it is good for data integrity and reproducibility. The Python scripts clean both datasets, match state identifiers, aggregate monthly FRED values to annual averages, and join the two sources using state abbreviation and year.

The final dataset contains a merged set of FRED and U.S. Census data linking states and their corresponding unemployment rate and median income, on which the analysis code does some basic summary statistics and correlation analysis on. The final dataset includes variables such as state name, year, annual unemployment rate averages, and annual median household income values. Additional details regarding variable definitions, formats, and interpretations are documented within the project’s data dictionary to improve transparency and reusability. Please reference the data dictionary for details on how to interpret the variables of the final merged dataset.

Statistical analysis, including Pearson and Spearman correlation testing, revealed no significant linear or monotonic relationship between state-level unemployment and median household income.

Overall, this project shows how multiple datasets with different schemas and structures can be cleaned, standardized, integrated, and analyzed within a reproducible workflow. In addition to exploring economic relationships between unemployment and income, the project also highlights the importance of data quality assessment, reproducibility, workflow automation, and documentation when performing real-world data integration and analysis tasks.


---

### Data Profile
The first data set is the Fred state unemployment data and is located in the “data/raw/raw_fred_data.csv” folder in the repository. This dataset contains unemployment rate information for the U.S. states over time. It consists of 28,847 rows with 3 columns, “date”, “value”, and “state.” The date column contains the observation date for each unemployment measurement, while the value column represents the percent of unemployment for the corresponding state and date. The State column contains two-letter state abbreviations used to identify each state.

One important characteristic of this dataset is that it is collected at a monthly frequency. Unlike static datasets that only provide annual summaries, the FRED dataset includes changes in unemployment over time, allowing for much more trend analysis. This makes the dataset valuable for identifying economic fluctuations, seasonal unemployment changes, and broader labor market trends. However, the Census dataset only reports annual household income estimates, so the monthly unemployment data needed to be transformed by extracting the year from the date column in order to support integration between the two sources.

However, the dataset also presented several data quality concerns. Specifically, the missing observations could negatively affect analysis if not addressed properly. Missing values are especially problematic in time-series data because they may introduce bias into calculations or even distort the trends. During the cleaning process, these missing values were identified and handled before integration and visualization.

The second data set provides the annual median household income estimates for states in the United States and was collected from the Census Bureau API. The original dataset contains four columns including “NAME”, “B19013_001E”, “state”, and “Year.” The NAME column consists of full state names and the B19013_001E is the Census API variable that represents the estimated median household income. The state column contains state FIPS codes which are unique numeric or alphabetic codes that are used for geographic information. Finally, the Year column identifies the reporting year associated with each observation. 

The dataset is primarily composed of structured quantitative data. The income values are continuous numerical variables measured in dollars, making them suitable for statistical comparisons, trend analysis, and integration with other economic indicators. Unlike the unemployment dataset, the Census dataset did not contain missing values, which improved its reliability and reduced the need for extensive cleaning related to null observations. However, the dataset still had several readability and formatting issues that affected usability.

The two datasets used complement each other because they measure two different dimensions of economic conditions. The FRED dataset measures labor market performance through the unemployment rates, while the Census dataset measures economic well-being through household income. Although they originate from different organizations and use different schemas, they were able to be integrated after performing standardization and cleaning operations. For example, in the raw FRED dataset file, the unemployment measure is stored in a column called “value.” This column name is extremely vague and does not communicate what the numbers actually represent. Without documentation, users may not immediately recognize that the values correspond to unemployment percentages so, during cleaning this column is renamed to “Unemployment_Rate” so it is descriptive enough for reuse. During integration, the state abbreviations that were a part of the FRED dataset were mapped to full state names so they can match the Census dataset.  Additionally, the year attribute which was extracted from the unemployment dataset allowed for a consistent linkage between both sources. After cleaning and standardization, the datasets were merged into a single integrated dataset that allows comparative analysis between unemployment and income across states and over the years.

From a structural perspective, both datasets are tabular CSV files that can be easily processed using Python and Pandas. The datasets are relatively structured and machine-readable, making them appropriate for automated workflows and reproducible analysis pipelines. The unemployment dataset originates from a trusted government-affiliated source, so it has strong credibility and transparency regarding methodology and provenance. However, as with many economic datasets, the unemployment values may still be affected by reporting delays, revisions, or methodological changes over time. The median income dataset also has strong data provenance and reliability. The dataset is publicly available and intended for public research and analysis. It also is aggregated at the state level rather than tied to individual households, so there are no major privacy concerns involving personally identifiable information.

The project repository separates raw data from processed data to preserve provenance and maintain transparency throughout the data lifecycle. Raw files remain unchanged in the data/raw/ directory, while cleaned and integrated outputs are stored in data/processed/.

---

### Data Quality
A major component of this project involved assessing the quality, consistency, completeness, and usability of both datasets before integration and analysis. The project combines data from two different public sources including the FRED API and the U.S. Census Bureau API. This made it critical to identify structural differences, missing values, semantic inconsistencies, and formatting issues that could affect the accuracy of the final analysis. The overall quality assessment focused on completeness, consistency, validity, interpretability, and compatibility between datasets.

The Census dataset has no missing values in all of its four columns. The main issue that was associated with the dataset was the semantic clarity. The column B19013_001E is accurate as a Census API variable code but not as a descriptive label. This column is not meaningful to a reader without the external documentation and it can be difficult to interpret what the variable means. The file also stores the Census state FIPS code as an integer and not as the usual two-character strings which can cause formatting problems to arise. For example a value such as “01” can appear as just “1” if treated numerically. This matters because these FIPS codes are used as identifiers not as quantities. 

The FRED file has 28,847 rows with 48 missing values in the “value” column which was where the percentage of unemployment is contained. The missing values were limited compared to the full dataset but they still mattered because the analysis depends on averaging monthly values into annual state unemployment rates. The FRED file also had a vague column name “value” which can be misleading to the user. It was renamed to describe the actual measurement. The “date” column was stored as a string, so it needed conversion before extracting years or grouping by time was possible. Another issue was that the file did not include all expected state abbreviations. Georgia, Massachusetts, and Nebraska were not present in the FRED file, so the final merged dataset includes 48 states rather than all 51 possible states/DC units.

The biggest integration challenge that arose was the schema mismatch. The states had two-letter abbreviations such as “IL” in the FRED dataset while Census dataset identified the states using their full names such as “Illinois” and numeric FIPS codes. Therefore, the FRED state abbreviations were mapped into full state names. The join was then performed on the shared “State” abbreviation and “Year.” This linkage was appropriate because one row in the FRED dataset represents one state-year average and each Census row represents one state-year median income estimate. So, by both being in the same “units” we were able to compare the data and produce conclusions. 

The quality assessment also considered temporal compatibility. The FRED values are monthly, while the values in the Census data are annual. Directly joining the monthly unemployment rate observations to annual income would create many repeated income values and could distort the analysis. So the project takes the monthly values and calculates the annual averages before joining. This makes the units of analysis consistent relating to the time aspect. 

Finally, the analysis checks the reasonableness of outputs. The final merged data set consists of 192 rows. This is the result of multiplying the 48 states and jurisdictions by the 4 years analyzed (2018, 2019, 2021, and 2022). All in all, the overall data quality assessment confirmed that both datasets were sufficiently reliable and appropriate for the project’s research question. The unemployment dataset required more extensive cleaning due to missing values and formatting inconsistencies. The Census dataset mainly required semantic improvements and identifier standardization. After cleaning and integration, the combined dataset provided a consistent and trustworthy foundation for statistical analysis, scatter plot visualization, and correlation testing between unemployment rates and median household income across U.S. states.

---

### Data Cleaning

All data cleaning was handled by the script data_clean_merge.py. Firstly, column naming conventions were addressed by simple renaming to distinguish names further on once merging happens. For example, the FRED dataset’s “value” column was changed to “Unemployment_Rate”, which sticks around to the final dataset, and the Census dataset’s cryptic “B19013_001E” column was renamed to “Median_Income.” B19013_001E is a Census API variable code rather than a descriptive label. Without additional documentation, users may be unfamiliar with Census APIs and would likely struggle to interpret what the variable represents. During cleaning, this field was renamed to Median_Income to improve clarity and interpretability.

Secondly, the code extracts the “date” from the FRED dataset as a pandas datetime object to match temporal granularity between our datasets. Once the year was extracted, we could merge our monthly FRED data with the annual Census data. We used a simple average of monthly data points over a year, which we will discuss the pros and cons of later.

Another issue we faced with the Census data was type mismatch. The API returned all median income values as strings, which we had to coerce to floats for the sake of our correlation statistics. Non-numeric artifacts were turned into “N/A” values. 

Some final adjustments were made regarding state identification. We coerced the FIPS state codes back to two characters by padding with zeroes at the front. The FRED data used a two-letter abbreviation to identify states, while the Census data used the full name. We remedied this with a robust dictionary, mapping abbreviations to state names, to create a new “State_Name” column that resolved identifier mismatch. Similarly, the Census data occasionally included territories like Puerto Rico, not present in the FRED data. We made sure to only include states or districts that were present in our dictionary. 

Finally, we performed an inner join, merging on State name and year, and completed a final drop of null values to ensure the data was ready for analysis.

---

### Findings
After cleaning and integrating the FRED unemployment dataset with the Census median household income dataset, the final dataset was analyzed to explore the relationship between unemployment rates and median household income across the U.S. The final integrated dataset consists of 192 observations after preprocessing and cleaning. Each observation represented a state-year combination containing an unemployment rate and the corresponding household income value.
The analysis workflow uses python libraries to generate summary statistics, a scatter plot visualization and correlation analysis. The workflow was automated using Snakemake to improve reproducibility and ensure the entire process can be rerun consistently from data acquisition through visualization and statistical analysis. 

The summary statistics that were derived revealed important patterns within the combined dataset. The average unemployment rate across all observations was approximately 3.92%, with a minimum unemployment rate of 1.93% and a maximum of 7.35%. The median unemployment rate was about 3.83%, indicating that most of the states tended to cluster around relatively moderate unemployment levels during the analyzed years. For household income, the average median household income across observations was $67,514, while the median income value was around $65,660. The lowest observed median household income was $44,097, while the highest reached $101,027, showing there is substantial variation in economic conditions between states. 

To evaluate the relationship between unemployment and household income, the Pearson and Spearman correlation analyses were performed. The Pearson correlation coefficient is used to measure linear relationships between variables and it produced a correlation value of 0.049 with a p-value of 0.4991. This indicated an extremely weak positive linear relationship between unemployment rates and median household income, and the high p-value suggests that the relationship between the two variables is not statistically significant. 

The Spearman correlation coefficient is used to evaluate monotonic relationships between variables and it produced a value of -0.021 with a p-value of 0.7715. Similar to the Pearson result, this indicates an extremely weak relationship between unemployment rates and household income. The negative sign suggests a slight downward trend, but the correlation is close to zero meaning that it does not demonstrate a meaningful association between the two variables. 

The scatter plot visualization further supported the findings from the Pearson and Spearman correlation coefficient. While some states with higher unemployment rates appeared to have lower household incomes, the overall distribution of the points was very dispersed and did not have a strong apparent linear correlation. Instead of forming a clear upward or downward trend, the data points were scattered broadly across the graph, reinforcing the weak correlation values produced by the statistical analysis.  

One notable finding from this project was that the unemployment rates alone may not be strong predictors of median household income at the state level. Economic theory often suggests that higher unemployment is tied to lower economic well-being, however, the results indicate that the relationship is more complicated than initially expected. Other factors such as education levels, costs of living, industry specialization, etc. may have stronger effects on household income outcomes than unemployment rates by themselves. Therefore, the findings suggest that while unemployment rates and median household income may share some economic connections, unemployment alone does not strongly explain differences in household income across U.S. states within the analyzed time period. 


### Future Work
This project allowed us to gain valuable experience with the full data curation cycle. One of the biggest lessons learned throughout the project was that integrating datasets from different sources is often more difficult than expected, even when they appear to measure related concepts. Although both datasets focused on state-level economic indicators, they used different schemas, naming conventions, temporal structures, and geographic identifiers. There was a considerable amount of preprocessing and standardization required before the actual analysis could be performed. 

Another major lesson that was learned was the importance of reproducibility and workflow organization. Working through the workflow automation process highlights how reproducibility is not only important for academic research but also for environments where workflows need to be scalable and easy to understand.

The project also highlighted the importance of understanding the limitations of public datasets. Although government datasets are well-documented and reliable, they may still contain missing values, inconsistent formatting, or incomplete observations. For example, the unemployment dataset contained several missing unemployment rate values that required cleaning before the analysis could proceed and it took out some important data. In addition, some states failed during the API retrieval process, slightly reducing the number of final observations available for analysis. These issues reinforced the importance of validating datasets before drawing conclusions. 

One important limitation encountered during the project involved temporal granularity differences between the two datasets. The FRED data was reported monthly while the Census data was only available annually. Because of this, the unemployment data had to be aggregated into yearly averages before integration could happen. While this allowed the datasets to be combined, it also reduced some of the detail and variability contained in the original unemployment observations. In the future work, one improvement could be finding datasets with the same temporal granularity, for example, both monthly. Using datasets that are both reported monthly would allow for more precise comparisons and could potentially reveal short-term economic relationships that annual aggregation may not show. Monthly income datasets or alternative labor and economic indicators could improve the accuracy and depth of future analysis. 

Future versions of the project could also consider expanding beyond unemployment rates and household income by incorporating more economical and demographic variables. For example, they could include variables like poverty rates, educational attainment, inflation, and cost of living indices. These additional factors could help explain why some states maintain high household incomes despite having higher unemployment rates or why other states experience lower income levels even when unemployment is relatively low. In this project, we examined the relationship between unemployment and income and were not able to find a statistically significant relationship. So, by incorporating these other variables it could be possible to produce a more comprehensive understanding of economic well-being across states. 

Another area for future work involves expanding the statistical methods that were used in the analysis. This project primarily focuses on descriptive statistics, scatter plots, and correlation coefficients such as Pearson and Spearman correlations. These methods do prove to be useful for identifying basic relationships, however applying regression modeling or machine learning approaches could allow for a better understanding of the influence of multiple economic variables simultaneously. 

Overall, this project successfully demonstrated the integration and analysis of multiple public datasets while also revealing several opportunities for improvement and expansion. In the future, this foundation can be built upon by using datasets with matching temporal granularity, incorporating additional economic indicators, and applying more advanced statistical techniques to provide deeper insight into economic conditions across the United States. 


---

### Challenges
Our main challenges encountered during this project mainly revolved around API rate limiting, workflow support, and as mentioned, granularity mismatches.

Learning to work around API rate limits was not intuitive and took some digging to learn about. Querying FRED and Census APIs for data on 50 states concurrently across years risked triggering API limits or timeouts. We solved this by adding a half-second delay in our fetching loops, which is common practice in API workflows.

The main functionality of all of our scripts were first workshopped in a Jupyter notebook. This method allowed us to work on sections of code separately, while testing together as needed. This was “main.ipynb” in the root of our project until deletion before submission. Transferring this notebook to separate .py files proved a challenge. We did not consider how we would need to import libraries multiple times for each script, remove hardcoded variables, or make outputs flow from one script to another externally. After many Snakemake trials, we learned that every input and output had to be saved in an explicit, yet user-adjustable location so the workflow could run to completion. 

One central challenge we had to consider was the granularity mismatch between these two datasets. We wanted to make full use of the monthly data in our FRED dataset, So we ended up averaging the FRED data by the year to make the merge possible, but this methodology could be improved upon in another study, perhaps by changing it to find a matching monthly dataset or including more descriptive statistics about the spread and change of the monthly data before analyzing the relationship between annual averages.

Another challenge showing our priorities during this project was the COVID-19 pandemic’s presence in 2020, within the timespan of analysis in this project. Massive, unprecedented outliers existed in the dataset due to pandemic lockdowns, affecting both target datasets. We made the deliberate, methodical decision to exclude 2020 from the list of years that we queried the API for in order to aim for a better snapshot more representative of the macroeconomic state of the USA, but COVID-19’s impact reaches outside of the year 2020 and may still affect the analysis’s conclusion. 


### Reproducing
This project is built using Snakemake to ensure 100% reproducibility. To reproduce these results on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [YOUR_GITHUB_REPO_URL]
   cd [YOUR_REPO_NAME]
   
2. **Set up the environment:** Make sure you have Python installed. Install the required dependencies using pip:
   ```bash
   pip install pandas seaborn matplotlib scipy requests snakemake

3. **Configure API Keys:** 
* Obtain a free API key from FRED. Save the key in a text file named fred_apikey.txt in the root directory.
* Obtain a free API key from the U.S. Census Bureau. Save the key in a text file named census_apikey.txt in the root directory.

4. **Run the Pipeline:** Open your terminal or command prompt in the project root directory and execute:
    ``` bash
    python -m snakemake --cores 1
    
5. **View Results:** Snakemake will automatically fetch the data, clean it, merge it, and run the statistical analysis.

* The final outputs will be generated in the following locations by default:
    * results/summary_stats.txt: Contains descriptive statistics and correlation coefficients.
    * results/scatter_plot.png: A visual regression analysis of the data.

If curious, please view the merged dataset that analysis was conducted on in data/processed/.


**References**
* Federal Reserve Bank of St. Louis. (n.d.). Federal Reserve Economic Data (FRED) API. Retrieved from https://fred.stlouisfed.org/docs/api/fred/

* U.S. Census Bureau. (n.d.). American Community Survey (ACS) 1-Year Estimates API. Retrieved from https://www.census.gov/data/developers/data-sets/acs-1year.html

* Mölder, F., Jablonski, K. P., Letcher, B., Hall, M. B., Tomkins-Tinch, C. H., Sochat, V., ... & Köster, J. (2021). Sustainable data analysis with Snakemake. F1000Research, 10(33).

* McKinney, W. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).

* Waskom, M. L. (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021.

* Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., ... & SciPy 1.0 Contributors. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17, 261–272.

**LICENSING**:
Please view detailed licensing and redistribution info in the LICENSE file. 