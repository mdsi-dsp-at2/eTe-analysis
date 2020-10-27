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

# Importing Customised Common Data Reader Class
sys.path.append(os.path.abspath('..'))
from common_lib.data_reader import SuicideDataReader, SuicideProcessedData, SuicideRawData

# ========= Getting Data =========

# Use common Data Reader Class to load data
data_reader = SuicideDataReader()

# Load Suicide Rate data
suicide_rate_data = data_reader.read_data(SuicideProcessedData.SUICIDE_RATES)
# print(suicide_rate_data)

# Load Human Resource data
hr_data = data_reader.read_data(SuicideRawData.HUMAN_RESOURCES)
#print(hr_dataframe.head())

# ========= Prepare Data =========

# Filter the suicide rate data for 
suicide_rate_dataframe = suicide_rate_data[["country", "all_age", "sex"]]

# Merge the two dataframes for plotting purpose
merged_dataframe = pd.merge(suicide_rate_dataframe, hr_data, on="country")
#print(merged_dataframe.head())

# ========= Plotting (1) =========
#Plotting to to visualise the association between Suicide rate of All age and Psychiatrists

# setting style
sns.set_style("darkgrid", {"axes.facecolor": ".9"})

# https://seaborn.pydata.org/tutorial/aesthetics.html
# https://seaborn.pydata.org/generated/seaborn.lmplot.html

plot_psy = sns.lmplot(data= merged_dataframe, x="psychiatrists", y= "all_age", palette="Set1", col="sex", hue="sex")
plot_psy.set_axis_labels("Psychiatrists 100,000 population", "Suicide Rate in All age")

# This is to adjust the axis and display the main title
# without it, seaborn"s facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
plot_psy.fig.suptitle("Global Psychiatrists Availability Vs Suicide Rate in 2016")
plt.show()



# ========= Plotting (2) =========
# Plotting to visualise the association between Suicide rate of All age and Nurses among Sexes

plot_nurses = sns.lmplot(data= merged_dataframe, x="nurses", y= "all_age", palette="Set1", col="sex", hue="sex") 
plot_nurses.set_axis_labels("Nurses per 100,000 population", "Suicide Rate in All Ages")

# This is to adjust the axis and display the main title
# without it, seaborn"s facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
plot_nurses.fig.suptitle("World Nurses Availability Vs Suicide Rate in 2016")

plt.show()

# ========= Plotting (3) =========
#Plotting to visualise the association between Suicide rate of All age and Psychiatrists among Sexes

plot_psy = sns.lmplot(data= merged_dataframe, x="psychologists", y= "all_age", palette="Set1", col="sex", hue="sex") 
plot_psy.set_axis_labels("Psychologists per 100,000 population", "Suicide Rate in All Ages")

# This is to adjust the axis and display the main title
# without it, seaborn"s facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
plot_psy.fig.suptitle("World Psychologists Availability Vs Suicide Rate in 2016")

plt.show()