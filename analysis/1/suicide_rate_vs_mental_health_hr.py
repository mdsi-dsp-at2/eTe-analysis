# Association of Suicide Rate with Mental Health Care
# Suicide is a complex issue and therefore suicide prevention efforts require coordination and 
# collaboration among multiple sectors of society, including the health sector and other sectors 
# such as education, labour, agriculture, business, justice, law, defense, politics, and the media.
# These efforts must be comprehensive and integrated as no single approach alone can make an impact on an issue as complex as suicide.
# This analysis is trying to discover the association between the availability of workforce, human resources in mental health care sector with the suicide rate in the countries.

# ========= Import the packages =========
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Importing customised functions which handling data wrangling
import common_functions as cf

# ========= Getting Data =========

suicide_rate_data_filepath = os.path.join('..','..','processed_data', 'crude_suicide_rates.csv')
suicide_rate_dataframe = pd.read_csv(suicide_rate_data_filepath, index_col=0)
#print(suicide_rate_dataframe.head())

hr_data_filepath = os.path.join('..','..','raw_data', 'human_resources.csv')
hr_dataframe = pd.read_csv(hr_data_filepath, index_col=0)
#print(hr_dataframe.head())

# ========= Prepare Data =========
suicide_rate_dataframe = cf.find_all_age_suicide_rate(suicide_rate_dataframe)
#print(suicide_rate_dataframe.head())

# Filter the suicide rate data for 
suicide_rate = suicide_rate_dataframe[['Country', 'all_age', 'Sex']]

# Merge the two dataframes for plotting purpose
merged_dataframe = pd.merge(suicide_rate, hr_dataframe, on='Country')
print(merged_dataframe.head())

# ========= Plotting (1) =========
#Plotting to to visualise the association between Suicide rate of All age and Psychiatrists

# setting style
sns.set_style('darkgrid', {'axes.facecolor': '.9'})

# https://seaborn.pydata.org/tutorial/aesthetics.html
# https://seaborn.pydata.org/generated/seaborn.lmplot.html

plot_psy = sns.lmplot(data= merged_dataframe, x='Psychiatrists', y= 'all_age', palette='Set1', col='Sex', hue='Sex')
plot_psy.set_axis_labels('Psychiatrists 100,000 population', 'Suicide Rate in All age')

# This is to adjust the axis and display the main title
# without it, seaborn's facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
plot_psy.fig.suptitle('Global Psychiatrists Availability Vs Suicide Rate in 2016')
plt.show()



# ========= Plotting (2) =========
# Plotting to visualise the association between Suicide rate of All age and Nurses among Sexes

plot_nurses = sns.lmplot(data= merged_dataframe, x='Nurses', y= 'all_age_suicide_rate', palette='Set1', col='Sex', hue='Sex') 
plot_nurses.set_axis_labels('Nurses per 100,000 population', 'Suicide Rate in All Ages')

# This is to adjust the axis and display the main title
# without it, seaborn's facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
plot_nurses.fig.suptitle('World Nurses Availability Vs Suicide Rate in 2016')

plt.show()

# ========= Plotting (3) =========
#Plotting to visualise the association between Suicide rate of All age and Psychiatrists among Sexes

plot_psy = sns.lmplot(data= merged_dataframe, x='Psychologists', y= 'all_age_suicide_rate', palette='Set1', col='Sex', hue='Sex') 
plot_psy.set_axis_labels('Psychologists per 100,000 population', 'Suicide Rate in All Ages')

# This is to adjust the axis and display the main title
# without it, seaborn's facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
plot_psy.fig.suptitle('World Psychologists Availability Vs Suicide Rate in 2016')

plt.show()