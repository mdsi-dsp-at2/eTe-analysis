# This code is to analysise the male and female comparison in top 5 countries with hight suicide rates
# catplot (for categorical data) from Seaborn library is used for visualisation 

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing customised functions which handling data wrangling
import common_functions as cf

# ========= Getting Data =========
suicide_rate_data_filepath = os.path.join("..","..","processed_data", "crude_suicide_rates.csv")
suicide_rate_dataframe = pd.read_csv(suicide_rate_data_filepath, index_col=0)
#print(human_resource_dataframe.head())


# ========= Prepare Data =========
# Find the total suicide rate of all different ages
suicide_rate_dataframe = cf.find_all_age_suicide_rate(suicide_rate_dataframe)
#print(suicide_rate_dataframe.head())


# Do Melting - Tranform/Combine the multiple  column names of different age groups into one column "Age"
suicide_rate_pivot_longer_df = cf.pivot_longer_age_columns_to_one(suicide_rate_dataframe, True)
#print(suicide_rate_pivot_longer_df)

# Find Top 5 countries of highest suicide rate in "all_age" and "both sexes"
# And Male/ Female - Age distribution 
top_5_suicide_rate_bothsex = suicide_rate_pivot_longer_df[(suicide_rate_pivot_longer_df["Sex"] == "Both sexes" ) & (suicide_rate_pivot_longer_df["Age"] == "all_age" )].nlargest(5, "Suicide_rate")
suicide_rate_separatesex = suicide_rate_pivot_longer_df[suicide_rate_pivot_longer_df["Sex"] != "Both sexes"]

## Get the countries names of top 5 highest suicide rate
#print(top_5_suicide_rate_bothsex["Country"].to_list())
top_5_country_names = top_5_suicide_rate_bothsex["Country"].to_list()
## Filtering out Male/Female records belong to the hightest rate countries.
top5_suicide_rate = suicide_rate_separatesex[suicide_rate_separatesex["Country"].isin(top_5_country_names)]
#print("top5_suicide_rate",final_df.head())


# ========= plotting graph =========
sns.set_style("whitegrid")
gg = sns.catplot(data = top5_suicide_rate, kind="bar", x="Country", y="Suicide_rate",hue="Sex", palette="husl", alpha=.9, height=5, ci=None)
gg.despine(left=True).set_ylabels("Suicide rate")
plt.title("Top 5 Countries with Highest Suicide Rate")
plt.show()

