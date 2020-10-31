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
suicide_rate_data = data_reader.read_data(SuicideProcessedData.SUICIDE_RATES)
#print(suicide_rate_data)


# ========= Prepare Data =========

# Find Top 5 countries of highest suicide rate in 'all_age' and "both sexes"
# And Male/ Female - Age distribution 
top_5_suicide_rate_bothsex = suicide_rate_data[(suicide_rate_data['sex'] == "Both sexes")].nlargest(5, "all_age")
#print(top_5_suicide_rate_bothsex)

suicide_rate_tidy_data_both_sex = pd.melt(suicide_rate_data, id_vars=['country', 'sex'], var_name='age',value_name='suicide_rate')
suicide_rate_separatesex = suicide_rate_tidy_data_both_sex[(suicide_rate_tidy_data_both_sex['sex'] != 'Both sexes') & (suicide_rate_tidy_data_both_sex['age'] != 'all_age' )]

# ## Get the countries names of top 5 highest suicide rate
top_5_country_names = top_5_suicide_rate_bothsex['country'].to_list()

# ## Filtering out Male/Female records belongs to the hightest countries.
top5_suicide_rate = suicide_rate_separatesex[suicide_rate_separatesex['country'].isin(top_5_country_names)]
top5_suicide_rate


# ========= plotting graph =========

sns.set_style("whitegrid")
gg = sns.catplot(data = top5_suicide_rate, kind="bar", x="country", y="suicide_rate",hue="sex", palette="husl", alpha=.9, height=5, ci=None)
gg.despine(left=True).set_ylabels("Suicide Rate \n per 100,000 population")
plt.title("Top 5 Countries with Highest Suicide Rate \n in year 2016")
plt.show()

