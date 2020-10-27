# This code is to analysise the male and female comparison in top 5 countries with hight suicide rates
# catplot (for categorical data) from Seaborn library is used for visualisation 

# ========= Import the packages =========
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

# Importing Customised Common Data Reader Class
sys.path.append(os.path.abspath('..'))
from common_lib.data_reader import SuicideDataReader, SuicideProcessedData

# ========= Getting Data =========

# Use common Data Reader Class to load data
data_reader = SuicideDataReader()

# Load Suicide Rate data
suicide_rate_data = data_reader.read_data(SuicideProcessedData.SUICIDE_RATES, tidy=True)
#print(suicide_rate_data)


# ========= Prepare Data =========

# Find Top 5 countries of highest suicide rate in 'all_age' and "both sexes"
# And Male/ Female - Age distribution 
top_5_suicide_rate_bothsex = suicide_rate_data[(suicide_rate_data['sex'] == 'Both sexes' ) & (suicide_rate_data['age_range'] == 'all_age' )].nlargest(5, 'suicide_rate')
#print(top_5_suicide_rate_bothsex)

suicide_rate_separatesex = suicide_rate_data[(suicide_rate_data['sex'] != 'Both sexes') & (suicide_rate_data['age_range'] == 'all_age' )]
#print(suicide_rate_separatesex)

## Get the countries names of top 5 highest suicide rate
top_5_country_names = top_5_suicide_rate_bothsex['country'].to_list()

## Filtering out Male/Female records belongs to the hightest countries.
top5_suicide_rate = suicide_rate_separatesex[suicide_rate_separatesex['country'].isin(top_5_country_names)]
print("top5_suicide_rate",top5_suicide_rate.head())


# ========= plotting graph =========

sns.set_style("whitegrid")
gg = sns.catplot(data = top5_suicide_rate, kind="bar", x="country", y="suicide_rate",hue="sex", palette="husl", alpha=.9, height=5, ci=None)
gg.despine(left=True).set_ylabels("Suicide rate")
plt.title("Top 5 Countries with Highest Suicide Rate")
plt.show()

