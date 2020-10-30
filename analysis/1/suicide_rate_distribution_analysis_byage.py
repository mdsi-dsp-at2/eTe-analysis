# This analysis is to investigate the suicide rate distribution by Age
# The main visualisation feature is Seaborn FacetGrid

# ========= Import the packages =========
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Importing Customised Common Data Reader Class
sys.path.append(os.path.abspath('..'))
from common_lib.data_reader import SuicideDataReader, SuicideProcessedData

# ========= Getting Data =========

# Use common Data Reader Class to load data
data_reader = SuicideDataReader()

# Load Suicide Rate Tiday data done with Pivot Longer the rate of all age ranges
suicide_rate_dataframe = data_reader.read_data(SuicideProcessedData.SUICIDE_RATES, tidy=True)
# print(suicide_rate_dataframe.head(10))


# ========= plotting graph =========

# Plotting is to visualise the suicide rate distribution in FacetGrid
sns.set_style("ticks")

age_plot = sns.FacetGrid(suicide_rate_dataframe, hue="sex", col="age_range", col_wrap=4)
age_plot.map(sns.barplot,"sex", "suicide_rate", order=["Male", "Female"])

age_plot.set_axis_labels("", "Suicide Rate \n (per 100.000 population)")

# This is to adjust the axis and display the main title
# without it, seaborn's facet titles and the main title are overlapped
plt.subplots_adjust(top=0.9)
age_plot.fig.suptitle("Suicide Rate Distribution Analysis by Age")
plt.show()
