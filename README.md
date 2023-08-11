# Hate_Crime

## Purpose
Hate crimes represent a concerning and complex challenge for communities and societies at large. These incidents can have far-reaching consequences, affecting not only the immediate victims but also the broader social fabric. As we delve into the intricate world of hate crime analysis, it becomes evident that comprehending the underlying factors and connections is of paramount importance. In this context, the focus of our investigation is on the intricate interplay between offender race and victim attributes – two fundamental dimensions that shape the landscape of hate crimes.

## Exploring Hypotheses:
To better understand the mechanics of hate crimes, we pose two primary hypotheses:

### Null Hypothesis:  
The victim attribute does not influence the race of the offender when committing a crime

### Alternate:
The race of the offender race does influence the victim's attribute when committing a crime

### Methodology:
The analysis utilizes a comprehensive dataset encompassing hate crime incidents. We employ various statistical techniques, including data visualization, chi-square tests, and logistic regression, to uncover patterns, correlations, and dependencies. Through these methodologies, we aim to provide empirical evidence to support or challenge our hypotheses.

# Exploratory Data Analysis on Hate Crime Database

The foundation for this analysis is the FBI Hate Crimes in the USA (1991-2020) dataset, accessible at https://www.kaggle.com/datasets/jonathanrevere/fbi-hate-crimes-in-usa-19912020?select=Hate+Crimes+in+NC+1991-2020.csv.

To undertake a comprehensive examination, this analysis required merging individual datasets for each state into a cohesive representation of hate crimes in the entire USA.

Our initial dataset consisted of 29 columns and 429,968 rows. However, in order to focus our analysis, we refined our scope by selecting 8 key columns from this dataset. The data cleaning process involved excluding columns with limited values that did not contribute to our analytical objectives.

Through this exploratory process, we aimed to gain an in-depth understanding of hate crime patterns and their underlying factors. Our refined dataset enabled us to direct our analysis toward meaningful insights that highlight correlations and trends in hate crime occurrences.



![Hate_Crime_Overtime](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/US%20Hate%20Crime%20over%20time.png)

# Statistical Analysis and testing
Hate Crime Severity by Year:

Created a bar graph that visualized hate crime severity distribution over the years.

![SEVERITY_DISTRIBUTION](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Severity%20Overtime.png)

This graph provided an overview of how hate crime severity has changed over time.

Hate Crime Severity by Offender Race:


![SEVERITY_by_OFFENDER_RACE](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Total%20incidents%20by%20offender.png)


Generated a stacked bar graph that depicted hate crime severity distribution by offender race.
This graph highlighted how different offender races were associated with varying levels of offense severity.

Hate Crime Bias Description by Offender Race:

![hate_crime_by_offender_race](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Hate%20Crime%20by%20Offender%20Race%20and%20Year.png)

![American_Indian_by Bias_desc_by_offender](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/American%20Indian.png)
![blackafricanamerican_by Bias_desc_by_offender](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Black_African%20American.png)
![Multiple__by Bias_desc_by_offender](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Multiple.png)
![White_Indian_by Bias_desc_by_offender](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/White.png)
![Unnknown_Indian_by Bias_desc_by_offender](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Unknown.png)
![Asian_Indian_by Bias_desc_by_offender](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/asian.png)


Utilized stacked bar graphs to showcase the distribution of bias descriptions (victim attributes) based on offender race.
These graphs illustrated how different offender races were associated with different types of bias descriptions.

Hypothesis Testing - Chi-Square Test of Independence:
![Chi_results](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/CHI%20Squared.PNG)

Formulated null and alternative hypotheses to investigate the relationship between offender race and bias description.
Conducted a Chi-Square test to determine if there was a significant association between the two categorical variables.
Based on the obtained p-value, you rejected the null hypothesis, suggesting that offender race and bias description are not independent.

Logistic Regression Model Coefficients:


![Coefficients](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/COEF.png)


Employed a logistic regression model to analyze the relationship between various factors and the likelihood of hate crimes.
Interpreted the coefficients of the model, identifying which factors had a significant impact on the prediction of hate crimes.


Relative Crimes per Capita Heatmaps:
![Relative_crimes_per_capita_by_offender](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/relative%20Crimes%20per%20capita%20by%20offender%20race%20and%20year.png)

![relative_crimes_per_capita_by_Population_group](https://github.com/Chris-Vicks/Hate_Crime/blob/main/img/Relative%20crime%20per%20capita.png)

Created heatmaps to visualize the relative crimes per capita by population group and offender race over the years.
These heat maps provided insights into the distribution of hate crimes within different demographic groups.

# Conclusion:
In conclusion, this comprehensive analysis delved into the intricate dynamics of hate crime patterns and the underlying factors that influence them. The findings from this analysis provide valuable insights that can contribute to a better understanding of the complex problems of hate crimes. Here's a breakdown of the key takeaways and implications:

1. Understanding Hate Crime Patterns:
The analysis successfully unearthed patterns and trends in hate crime incidents over the years. By visualizing hate crime severity by year, we gained a clear perspective on how the severity of these offenses has evolved. This understanding enables us to track shifts in societal sentiments and respond effectively.

2. Significance of Offender Race:
Through the exploration of hate crime severity by offender race, we unveiled critical insights into the role of offender identity in shaping the intensity of offenses. The stacked bar graphs vividly displayed how different offender races correlate with varying degrees of severity, shedding light on potential motivations and biases.

3. Impact of Victim Attributes:
The analysis further highlighted the intricate connection between offender race and victim attributes (bias descriptions). By investigating bias descriptions by offender race, we revealed how certain racial and ethnic groups may be disproportionately affected by specific types of hate crimes. This understanding is crucial for devising targeted interventions and community support.

4. Validation through Hypothesis Testing:
The null hypothesis testing underscored the interplay between offender race and bias descriptions. The rejection of the null hypothesis demonstrates that there is a significant correlation between these variables. This insight challenges assumptions and guides us to examine deeper factors influencing hate crime dynamics.

5. Influence on Policy and Community Efforts:
The implications of this analysis extend beyond data interpretation. The insights gained hold the potential to guide policy-making, law enforcement strategies, and community outreach initiatives. By recognizing trends and associations, policymakers can tailor interventions that address specific challenges within diverse communities.

6. A Catalyst for Change:
This analysis serves as a catalyst for ongoing research and advocacy against hate crimes. It lays the foundation for future investigations into the motivations behind hate crimes, the role of media, and potential measures to mitigate their occurrence. By sharing these findings, we empower communities to take informed actions against prejudice and discrimination.

In essence, this analysis offers a data-driven perspective on hate crime dynamics that goes beyond mere numbers. It is a call to action, urging us to collectively challenge bias, work towards tolerance, and create safer spaces for all. As we move forward, these insights can help us build a society where diversity is celebrated, and hate crimes become relics of the past.
