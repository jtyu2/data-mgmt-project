## STATUS REPORT 

## TASK UPDATES

**Original plan**
| Date        | Tasks Done |
|------------|------------|
| 3.21 (wk 1–2) | Data acquisition – Access datasets via API, download, and store raw data |
| 3.28 (wk 3)   | Data quality assessment and cleaning – Identify missing/inconsistent values and address by supplementing with other sources or other strategies |
| 4.11 (wk 4–5) | Data integration and analysis – Summary statistics, charts, and visualizations |
| 5.2 (wk 6–9)  | Split writing for final submission deliverable |

An update on each of the tasks described on your project plan including references and links to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc).

## Summary
Our project’s scope has not changed much since the project plan, though we needed to adjust our timeline a bit. A couple pieces of feedback we received before milestone 2 informed us along the way, leading us to replace one of our datasets with a parallel one from the same source. This took some time, but allowed us to learn about OpenRefine in class, a tool we will use to clean and integrate our data. We also have a much more clear understanding of how much time to commit to this project, what strategy works best for us, and how we can effectively work together. These changes have allowed us to work well as a team and understand all of the steps we do. Although conclusions from our analysis are yet unclear, we feel confident in our ability to finish decisively by the due date.

## TASK OVERVIEW

**Task 1: Data acquisition**
This step is complete, unless we decide to add any more datasets. We already had a FRED API key from in-class assignments, and secured a U.S. Census key easily. The biggest unexpected step was being sure to add a “wait” period between queries. The FRED API has a query rate limit of 120 per minute, and we wanted to be sure that even if we added another FRED dataset to pull data from, we would be able to smoothly integrate them without errors.
The U.S. Census dataset we had targeted was on a different time scale than the FRED dataset, so we ended up using different but similar Census data that was also on a monthly scale rather than yearly. We were prepared to aggregate the monthly data into years, but wanted to make use of the granularity provided by the monthly FRED data.

**Task 2: Data quality assessment and cleaning**
This step is beginning, but we have a clear path and are confident it will not take long. We created more of the analytical pipeline in Python before cleaning in-depth so we could be confident we would not need to replace our datasets and waste the time we spent cleaning. Our next step is to put the raw exported data into OpenRefine to analyze what kind of issues the data have- missing values, type errors, etc, which we feel comfortable doing.

**Task 3: Data integration and analysis**
This step is nearly complete. Outside of summary statistics like mean, standard deviation, and quartiles, we constructed correlation graphs with different combinations of states and time scales. To our surprise, we have not found convincing correlation between the two statistics in the data we have explored, but we will do a lot of critical thinking about our methodology so we are sure of any relationships (or lack thereof) going into our final report.

**Task 4: Final report writing**
We have started writing about how our project addresses what we have learned in different class modules and feel prepared to tie our project to the course requirements.

## UPDATED TIMELINE

| Task | Due date | Progress |
| :--- | :--- | :--- |
| Data acquisition - Accessing datasets via API, downloading and storing raw data | COMPLETE | COMPLETE |
| Data quality assessment and cleaning - Identify missing/inconsistent values, address by supplementing with other sources or other strategies | 4/19 | STARTED |
| Data integration and analysis - summary stats, charts and visualizations | 4/30 | NEARLY COMPLETE |
| Split writing for final submission deliverable | 5.2 (wk 6-9) | STARTED |

We have updated our timeline to reflect how our progress has gone so far, and what we plan on completing and when in the future. As we have begun working in depth on our project we have a much better understanding of the datasets, the integration process, and overall workflow. We have been able to more accurately estimate how much time will be needed for each remaining task. Some tasks are further along while other still need more work so we feel this will help us ensure all components are completed. 

## Teammate reports

**Jonathan:** We mostly stuck to the project plan, though I ended up doing a bit more of the programming and Mehr about as much more of the status report writing. Using the datasets Mehr found and imported through the API, I set ourselves up to be able to clean the data well later while building out more of the analytical pipeline.

**Mehr:** Throughout the first few weeks of our project, I found the datasets and started completing modules 1 and 2. In module 1, I discussed how our project relates to the USGS Science Data Lifecycle model. This model goes through all the steps starting from planning to publishing which I felt exemplifies our project well. For module 2, I described what kind of files and data types we are working withI also began explaining what storage and organizational strategy we were using however, that is still in the works as I anticipated it to change as we discover more and work more with our datasets. 

