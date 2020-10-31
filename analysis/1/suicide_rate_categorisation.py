# Suicide Rate Distribution Across Countries
#This analysis aims to discover how the world is severly experiencing suicide
#The suicide rates categorised into four ranges - 0-100, 100-200, 200-300, 300-400, >400
#The plots attempt to illustrate how many countries are in each range of suicide rate.

# ========= Import the packages =========
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Importing Customised Common Data Reader Class
sys.path.append(os.path.abspath('..'))
from common_lib.data_reader import SuicideDataReader, SuicideProcessedData

# ========= Getting Data ===========

# Use common Data Reader Class to load data
data_reader = SuicideDataReader()

# Load Suicide Rate Tiday data done with Pivot Longer the rate of all age ranges
suicide_rate_data = data_reader.read_data(SuicideProcessedData.SUICIDE_RATES)
suicide_rate_data.head()


# ========= Prepare Data ============

#This function serves to categorise (discretize)  the continuous variable value - 'suicide rate'
# Binning into 4 ranges of suicide rate
def suicide_rate_classification(rate):
    #rate = data[['all_age']]
    if (rate > 0 and rate <= 100):
        return "0-100"
    elif (rate > 100 and rate <=200):
        return "100-200"
    elif (rate >200 and rate <= 300):
        return "200-300"
    elif (rate > 300 and rate <= 400):
        return "300-400"
    else :
        return ">400"

# ====== Prepare Data for Plot (1) ======

# Filter the data for Both Sex only
suicide_rate_allage_bothsex = suicide_rate_data[suicide_rate_data["sex"] == "Both sexes"][["country", "sex", "all_age"]]
    
# Trigger the discretization function and store the result into the new column "suicide_rate_class"   
suicide_rate_allage_bothsex = suicide_rate_allage_bothsex.\
    assign(suicide_rate_class = lambda x: x["all_age"].map(lambda y: suicide_rate_classification(y)))
print(suicide_rate_allage_bothsex)

#=========== Plotting (1)==============#

# The plot to visualise how many countries are in each range of suicide rate
sns.countplot(x="suicide_rate_class", data=suicide_rate_allage_bothsex, color="c")
plt.title("Suicide Rate Distribution in the Countries in 2016")
plt.ylabel("Number of Countries")
plt.xlabel("Suicide Rate Ranges \n per 100,000 population")
plt.show()

# ====== Prepare Data for Plot (2) ======

# Filter the data for male and female only 
suicide_rate_cat_by_sex = suicide_rate_data[suicide_rate_data['sex'] != 'Both sexes'][["country", "sex", "all_age"]]
# Trigger the discretization function to bin the suicide rate
suicide_rate_cat_by_sex = suicide_rate_cat_by_sex.assign(suicide_rate_class = lambda x: x["all_age"].map(lambda y: suicide_rate_classification(y)))
print(suicide_rate_cat_by_sex)

#=========== Plotting (2)==============#

# The plot is to visualise and compare the variation of number of counties in Male-Female distribution of suicide rates 

rate_bin_list=["0-100", "100-200", "200-300", "300-400", ">400"]

##https://seaborn.pydata.org/tutorial/categorical.html
sns.catplot(x="suicide_rate_class", hue="sex", kind="count", data=suicide_rate_cat_by_sex, order=rate_bin_list)
plt.title("Suicide Rate Distribution in the Countries by Sex \n in 2016")
plt.ylabel("Number of Countries")
plt.xlabel("Suicide Rate Ranges \n per 100,000 population")
plt.show()