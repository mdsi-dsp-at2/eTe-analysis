# This file focus on the analyzing the top suicide rate of different countries
# 1. Find out the top 5 countries with highest youth suicide rate 

import os
import math
import pandas as pd
import matplotlib.pyplot as plt

# ========= Getting Data =========
suicide_rates_data_filepath = os.path.join("processed_data", "crude_suicide_rates.csv")
suicide_rates_dataframe = pd.read_csv(suicide_rates_data_filepath)

print(suicide_rates_dataframe)

country_facilities_data_filepath = os.path.join("processed_data", "facilities.csv")
country_facilities_dataframe = pd.read_csv(country_facilities_data_filepath)

print(country_facilities_dataframe)



# ========= Prepare Data =========
# join country facilities to suicde rate data
suicide_rates_facilities_dataframe = suicide_rates_dataframe.merge(country_facilities_dataframe, how="left", left_on="Country", right_on="Country")

# Sorting and pick the first 5
top_five_youth_suicide_rates_dataframe = suicide_rates_facilities_dataframe.sort_values(by=["10to19"], ascending=False).head(5)

# print the results
print(top_five_youth_suicide_rates_dataframe)

# ========= plot graph =========
top_suicide_rates_country_dataframe = suicide_rates_facilities_dataframe[suicide_rates_facilities_dataframe["10to19"] > 10].sort_values(by=["10to19"], ascending=False)

# top suicide rate plot
plt.figure(figsize=(20,10))
plt.bar(top_suicide_rates_country_dataframe["Country"], top_suicide_rates_country_dataframe["10to19"])
plt.title("Top five suicide rate countries")
plt.xlabel("Country")
plt.ylabel("Suicide Rate (%)")
plt.xticks(rotation=90)
plt.show()

# plot the suicide rate vs different facilities for analysis
ALL_SEX = top_suicide_rates_country_dataframe["Sex"].unique()
ALL_AGE_RANGES = ["80_above", "70to79", "60to69", "50to59", "40to49", "30to39", "20to29", "10to19"]
ALL_FACILITIES = ["Mental_hospitals", "health_units", "outpatient_facilities", "day_treatment", "residential_facilities"]

for sex in ALL_SEX:
	for age_range in ALL_AGE_RANGES:
		plt.figure(figsize=(20,10))
		fig, axs = plt.subplots(nrows=2, ncols=3, constrained_layout=True)
		fig.figsize=(20,10)
		facilities_index = 0	# use for control the location of the plot
		for facility in ALL_FACILITIES:
			x_index = math.floor(facilities_index / 3)
			y_index = facilities_index % 3
			print("Index : {0} {1}".format(x_index, y_index))
			subplot = axs[x_index, y_index]
			subplot.scatter(suicide_rates_facilities_dataframe[suicide_rates_facilities_dataframe["Sex"] == sex][age_range], suicide_rates_facilities_dataframe[suicide_rates_facilities_dataframe["Sex"] == sex][facility])
			subplot.set_title("{0}".format(facility))
			#subplot.xlabel("{0} {1} suicide Rate (%)".format(sex, age_range))
			#subplot.ylabel("{0}".format(facility))
			plt.suptitle("{0} {1} vs different facilities".format(sex, age_range))
			facilities_index = facilities_index + 1

		plt.show()



