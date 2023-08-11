# Hate_Crime

## Purpose
Hate crimes represent a concerning and complex challenge for communities and societies at large. These incidents can have far-reaching consequences, affecting not only the immediate victims but also the broader social fabric. As we delve into the intricate world of hate crime analysis, it becomes evident that comprehending the underlying factors and connections is of paramount importance. In this context, the focus of our investigation is on the intricate interplay between offender race and victim attributes – two fundamental dimensions that shape the landscape of hate crimes.

## Exploring Hypotheses:
To better understand the mechanics of hate crimes, we pose two primary hypotheses:

### Null Hypothesis:  
The victim attribute does not matter to the race of the offender when  committing a crime

### Alternate:
The race of the offender race affects the victim's attribute when committing a crime

### Methodology:
Our analysis utilizes a comprehensive dataset encompassing hate crime incidents. We employ various statistical techniques, including data visualization, chi-square tests, and logistic regression, to uncover patterns, correlations, and dependencies. Through these methodologies, we aim to provide empirical evidence to support or challenge our hypotheses.

# EDA into Hate Crime Database
The database for this analysis is from the FBI Hate Crimes in the USA (1991-2020) at https://www.kaggle.com/datasets/jonathanrevere/fbi-hate-crimes-in-usa-19912020?select=Hate+Crimes+in+NC+1991-2020.csv. 

This dataset had an individual dataset for each state, so from there all the CSV files had to be joined to complete an overall analysis of the USA.
Through this, we wanted to familiarize ourselves with the structure of the database. This dataset began with 29 columns and 429,968 rows.  After cleaning the data I only used 8 columns for the analysis.



![Hate_Crime_Overtime](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/US%20Hate%20Crime%20over%20time.png)

# Statistical Analysis and testing
Hate Crime Severity by Year:

Created a bar graph that visualized hate crime severity distribution over the years.
![SEVERITY_DISTRIBUTION](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Severity%20Overtime.png)
This graph provided an overview of how hate crime severity has changed over time.

Hate Crime Severity by Offender Race:
![]()
Generated a stacked bar graph that depicted hate crime severity distribution by offender race.
This graph highlighted how different offender races were associated with varying levels of offense severity.
Hate Crime Bias Description by Offender Race:

Utilized stacked bar graphs to showcase the distribution of bias descriptions (victim attributes) based on offender race.
These graphs illustrated how different offender races were associated with different types of bias descriptions.
Hypothesis Testing - Chi-Square Test of Independence:

Formulated null and alternative hypotheses to investigate the relationship between offender race and bias description.
Conducted a Chi-Square test to determine if there was a significant association between the two categorical variables.
Based on the obtained p-value, you rejected the null hypothesis, suggesting that offender race and bias description are not independent.
Logistic Regression Model Coefficients:

Employed a logistic regression model to analyze the relationship between various factors and the likelihood of hate crimes.
Interpreted the coefficients of the model, identifying which factors had a significant impact on the prediction of hate crimes.
Relative Crimes per Capita Heatmaps:

Created heatmaps to visualize the relative crimes per capita by population group and offender race over the years.
These heatmaps provided insights into the distribution of hate crimes within different demographic groups.


