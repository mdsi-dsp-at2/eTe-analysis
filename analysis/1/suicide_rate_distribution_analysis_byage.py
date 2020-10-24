# This analysis is to investigate the suicide rate distribution by Age
# The main visualisation feature is Seaborn FacetGrid
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing customised functions which handling data wrangling
import common_functions as cf

# ========= Getting Data =========
suicide_rate_data_filepath = os.path.join("..","..","processed_data", "crude_suicide_rates.csv")
suicide_rate_dataframe = pd.read_csv(suicide_rate_data_filepath, index_col=0)
print(suicide_rate_dataframe.head())

# ========= Prepare Data =========
# Calculate the total suicide rate of all different ages
suicide_rate_dataframe = cf.find_all_age_suicide_rate(suicide_rate_dataframe)
#print(suicide_rate_dataframe.head())

# Do Melting - Tranform/Combine the multiple  column names of different age groups into one column "Age"
suicide_rate_pivot_longer_df = cf.pivot_longer_age_columns_to_one(suicide_rate_dataframe)
#print(suicide_rate_pivot_longer_df)

# ========= plotting graph =========
# Plotting the suicide rate distribution in FacetGrid
sns.set_style("dark")
g = sns.FacetGrid(suicide_rate_pivot_longer_df, col="Age", col_wrap=3)
g.map_dataframe(plt.hist, x="Suicide_rate")
g.set_axis_labels("", "Suicide Rate")
# This is to adjust the axis and display the main title
# without it, seaborn"s facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Suicide Rate Distribution Analysis by Age")
plt.show()
