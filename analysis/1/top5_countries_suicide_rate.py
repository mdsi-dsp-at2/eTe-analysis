# This code is the analysis on the top 5 countries with hight suicide rates
# It further attempts to explore their differences and similarity of suicide rates in different age groups
# barplot from Seaborn library is used for visualisation 

# ========= Import the packages =========

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Importing customised functions which handling data wrangling
import common_functions as cf

# ========= Getting Data =========

# Getting Data of crude suicide rate
suicide_rate_data_filepath = os.path.join("..", "..","processed_data", "crude_suicide_rates.csv")
suicide_rate_dataframe = pd.read_csv(suicide_rate_data_filepath, index_col=0)
#print(suicide_rate_dataframe.head())

# ========= Prepare Data =========

# Get the suicide rate of all different ages
suicide_rate_dataframe = cf.find_all_age_suicide_rate(suicide_rate_dataframe)
# print(suicide_rate_dataframe.head())

# Find Top 5 countries of highest suicide rate in "all_age" and "both sexes"
top_5_suicide_rate = suicide_rate_dataframe[suicide_rate_dataframe["Sex"] == "Both sexes"].nlargest(5, "all_age")
#print(top_5_suicide_rate.head())

# Do Melting - Tranform/Combine the multiple  column names of different age groups into one column "Age"
top_5_suicide_rate = cf.pivot_longer_age_columns_to_one(top_5_suicide_rate)
#print(top_5_suicide_rate_pivot_longer_df)


# ========= Plotting  =========

sns.set(color_codes=True)
plot_top5_country = sns.barplot(x="Country", y="Suicide_rate", hue="Age", data = top_5_suicide_rate)
plt.title("Top 5 Countries with Highest Suicide Rate")
plt.ylabel("Suicide rate per 100,000 population")
plt.show()