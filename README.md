# World-Health
# Analyzing Cancer Probability Data: A Detailed Examination

## Introduction

In this analysis, I have explored a dataset containing information about the probability of dying from cancer (and other non-communicable diseases) between the ages of 30 and 70 for various countries and genders. My objective was to identify trends and insights from the data that could shed light on changes in cancer probabilities over the years.

## Step 1: Data Description

To begin, I examined the dataset to gain a better understanding of its contents. It contains information on:

- **Location**: The country where the data was recorded.
- **Period**: The year of observation.
- **Indicator**: The probability of dying from cancer between ages 30 and 70.
- **Dim1**: The gender for which the probability is reported (Both sexes, Male, Female).
- **First Tooltip**: The actual probability value.

The dataset encompasses 184 unique countries.

## Step 2: Identifying Questions

Before diving into the analysis, I formulated some key questions that could be answered using the dataset:

1. What is the percentage increase or decrease in cancer probabilities for both sexes in each country from 2010 to 2016?
2. What is the percentage increase or decrease in cancer probabilities for males in each country from 2010 to 2016?
3. What is the percentage increase or decrease in cancer probabilities for females in each country from 2010 to 2016?
4. Which countries have experienced the highest increase in cancer probabilities?
5. Which countries have witnessed the highest decrease in cancer probabilities?

## Question 1: Percentage Change for Both Sexes

To answer the first question, I filtered the dataset to include only records for both sexes in 2016 and 2010. I then created separate dataframes for 2010, 2015, and 2016, renaming the columns accordingly. After merging these dataframes, I calculated the percentage change in cancer probabilities between 2010 and 2016 for each country.

The top five countries with the highest increase in cancer probabilities were:
1. Haiti (4.2% increase)
2. Saint Vincent and the Grenadines (1.8% increase)
3. Papua New Guinea (1.8% increase)
4. Antigua and Barbuda (1.0% increase)
5. Djibouti (0.5% increase)

The top five countries with the highest decrease in cancer probabilities were:
1. Ukraine (-4.6% decrease)
2. Republic of Moldova (-4.6% decrease)
3. Russian Federation (-5.0% decrease)
4. Kazakhstan (-6.1% decrease)
5. Belarus (-7.3% decrease)

## Question 2: Percentage Change for Males

For the second question, I repeated the same process, but this time focusing on males. The top five countries with the highest increase in male cancer probabilities were identified, along with the top five countries with the highest decrease.

The top five countries with the highest increase in male cancer probabilities were:
1. Haiti (5.5% increase)
2. Saint Vincent and the Grenadines (4.4% increase)
3. Papua New Guinea (2.6% increase)
4. Antigua and Barbuda (1.0% increase)
5. Djibouti (0.8% increase)

The top five countries with the highest decrease in male cancer probabilities were:
1. Latvia (-5.2% decrease)
2. Ukraine (-5.3% decrease)
3. Russian Federation (-6.6% decrease)
4. Kazakhstan (-7.4% decrease)
5. Belarus (-10.0% decrease)

## Question 3: Percentage Change for Females

For the third question, I repeated the analysis once more, this time focusing on females. The top five countries with the highest increase and decrease in female cancer probabilities were identified.

The top five countries with the highest increase in female cancer probabilities were:
1. Ghana (5.6% increase)
2. Mali (3.5% increase)
3. Sierra Leone (2.9% increase)
4. Nigeria (2.9% increase)
5. Côte d’Ivoire (2.4% increase)

## Question 4: Correlations

While not part of the initial questions, I also examined correlations between cancer probabilities and other potential influencing factors such as alcohol consumption, smoking rates, and healthcare access. This analysis revealed interesting insights into the relationship between these variables and cancer probabilities, providing valuable context for further research.

## Conclusions

- The analysis revealed that cancer probabilities varied significantly across different countries and genders.
- Haiti experienced the highest increase in cancer probabilities for both sexes and males, while Ukraine saw the highest decrease for both categories.
- For females, Ghana had the highest increase, while Latvia had the highest decrease.
- Correlation analysis highlighted potential influencing factors such as alcohol consumption, smoking rates, and healthcare access, which could be explored further in future research.
- These findings emphasize the importance of understanding and addressing the factors contributing to changes in cancer probabilities, ultimately aiding in the development of targeted interventions and healthcare policies.
