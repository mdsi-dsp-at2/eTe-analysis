# This file focus on the data cleaning

import os
import pandas as pd

# ========= Clean crude_suicide_rates Data =========
# getting crude_suicide_rates Data
suicide_rates_data_filepath = os.path.join("raw_data", "crude_suicide_rates.csv")
suicide_rates_dataframe = pd.read_csv(suicide_rates_data_filepath)

# strip the column names
processed_suicide_rates_dataframe = suicide_rates_dataframe.rename(columns = lambda x: x.strip())

# strip the dataframe
processed_suicide_rates_dataframe["Country"] = processed_suicide_rates_dataframe["Country"].str.strip()
processed_suicide_rates_dataframe["Sex"] = processed_suicide_rates_dataframe["Sex"].str.strip()

# add the suicide rate of all age ranges and store in "all_age" column
processed_suicide_rates_dataframe["all_age"] = processed_suicide_rates_dataframe.iloc[:, 2:10].sum(axis=1)

# save the processed data to csv file
processed_suicide_rates_data_filepath = os.path.join("processed_data", "crude_suicide_rates.csv")
processed_suicide_rates_dataframe.to_csv(processed_suicide_rates_data_filepath, index = False)

# ========= Clean crude_suicide_rates Data =========
country_facilities_data_filepath = os.path.join("raw_data", "facilities.csv")
country_facilities_dataframe = pd.read_csv(country_facilities_data_filepath)

# remove space in the column names
processed_country_facilities_dataframe = country_facilities_dataframe.rename(columns = lambda x: x.replace(" ", ""))

# save the processed data to csv file
processed_country_facilities_data_filepath = os.path.join("processed_data", "facilities.csv")
processed_country_facilities_dataframe.to_csv(processed_country_facilities_data_filepath, index = False)