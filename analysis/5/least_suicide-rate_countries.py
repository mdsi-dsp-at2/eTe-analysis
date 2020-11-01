# ========= Import the packages =========

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

# Importing Customised Common Data Reader Class
sys.path.append(os.path.abspath('..'))
from common_lib.data_reader import SuicideDataReader, SuicideProcessedData

# Set the plot color code
#%matplotlib inline 
sns.set(color_codes=True)

# ========= Getting Data =========

# Use common Data Reader Class to load data
data_reader = SuicideDataReader()

# Load Suicide Rate Tiday data done with Pivot Longer the rate of all age ranges
suicide_rate_data = data_reader.read_data(SuicideProcessedData.SUICIDE_RATES)
suicide_rate_data.head()

# ========= Prepare Data for plot (1) ========= #

# Filter for countries with female only 
suicide_rate_data_female = suicide_rate_data[suicide_rate_data["sex"] == "Female"]

# Sort the suicide rate of population in all ages inclusively
sort_female = suicide_rate_data_female.sort_values("all_age")
sort_female.head()

#=========== Plotting (1)==============#

Country = sort_female["country"].head(10) 
Total = sort_female["all_age"].head(10)
# Figure Size 
fig = plt.figure(figsize =(10, 7)) 
  
# Horizontal Bar Plot 
plt.barh(Country, Total) 
plt.title("Top 10 Countries with Least Female Suicide Rate in the world \n in 2016")
plt.ylabel("Countries")
plt.xlabel("Suicide Rate \n per 100,000 population")
plt.show() 

# ========= Prepare Data for Plot (2) ========= #

# Filter for countries with male only 
suicide_rate_data_male = suicide_rate_data[suicide_rate_data["sex"] == "Male"]
# Sort the suicide rate of population in all ages inclusively
sort_male = suicide_rate_data_male.sort_values("all_age")
sort_male.head()

#=========== Plotting (2)==============#

Country = sort_male["country"].head(10) 
Total = sort_male["all_age"].head(10)
# Figure Size 
fig = plt.figure(figsize =(10, 7)) 
  
# Horizontal Bar Plot 
plt.barh(Country, Total) 
plt.title("Top 10 Countries with Least Male Suicide Rates in the world \n in 2016")
plt.ylabel("Countries")
plt.xlabel("Suicide Rate \n per 100,000 population") 
plt.show() 

