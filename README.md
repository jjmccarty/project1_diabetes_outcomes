# Project 1 - Outcomes in the evaluation of Diabetes Risk

Diabetes has notably increased in prevalence across the United States over the last decade, most notably type II diabetes which typically manifests in adulthood and is differentiated from type I diabetes which is a genetic condition.  Type I is characterized by the bodies inability to produce insulin, where as type II diabetes may be insuffient insulin production or the body developing an inability to properly process insulin and manage glucose levels.  

This work evaluates several factors within a specific population of females Pima India backgrounds to attempt some degree of prediction of diabetes risk based on those factors.  The Pima indians are concentrated in Arizona and have demonstrated higher than average rates of diabetes. The onset of this rise does appear to coincide with lifestyle changes pushed on the population (Reference via NIH https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4418458/)

### Team

The following team members were all original contributors to project
- Casandra Murray
- Armando Zamora
- Jessica McCarty
- Evelyn Browning

## Data Sources
Data sources for this analysis come from existing publicly available sources on Kaggel https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset.  This data was pulled down as ```diabetes.csv``` in the existing project. 

When evaluating the data we did find there were several values listed as 0 for some bio indicators, most prevalent being glucose and insulin levels.  This could mean that data was simply not collected, or there were issues with the collections such as values taken in a non-fasted state.  

To adjust for these values several options were considered including
1. Leave the existing values with 0 indicators (no change to the data)
2. Provide a value for the data based on the mean of existing values
3. Remove the data from the data set.

When evaluating options 1 and 2 we determined the best path was to use the mean of existing values for the 0 value placements.  The reliability of the model was not significantly impacted by the adjustment.

Estimated accuracy of the models when compared were .74 and .78 respectively. 

We did not chose to remove these values from the dataset, as many of the other bio markers were still relevant and important to the model.  


## Data Processing

Options have been provided to allow for modification of the existing dataset and alternate data cleaning options.  All data processing is contained in the ```data_outcomes.py``` script and the critical function for returning data is the ```data_outcomes.getDiabetesDataframe()``` function.

Two current options are available for retrieving data:

1. ```data_outcomes.getDiabetesDataframe()``` returns data with no cleaning adjustment to the data set
2. ```data_outcomes.getDiabetesDataframe```(submeanaszero=True) returns the data with 0 values substituted with the mean of values for the dataset

This mechanism allows for additional data cleaning options and testing to occur through a simply parameter change should future values be considered. 

## Data Outcomes

All data outcomes are processed in the ```data_outcomes_notebook.ipynb```. 

The current notebook utilized a cleaned (mean substiuted for zero values).

The model uses logistic regression to provide a predictive basis for potential diabetes risk.  Each of these values are evaluated for several potential outcomes including

1. Pregnancies vs. Glucose
2. BMI vs. Age
3. BMI vs. Skin Thickness
4. Blood Pressure vs. BMI
5. Blood Pressure vs. Age
6. Glucose vs. Insulin
7. Famiiy History vs. Age
8. Family History vs. Blood Pressuce
9. Family History vs. BMI

While other variants of the data are possible, these values utilized due to time constraints. 

## Outcomes/Conclusions

Current high level outcomes suggest that certains factors such as Blood Pressure and BMI are predictive for diabetes risk especially compounded by age.  Surprisingly family history did not appear to be as important and indicator for diabetes risk suggesting that directionally lifestyle factors are more impactful on type II diabetes risk over genetic factors. 
