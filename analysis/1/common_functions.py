import pandas as pd
  
def find_all_age_suicide_rate(dataframe):
    # Calculate the total suicide rate of all different ages
    dataframe["all_age"] = dataframe["80_above"]+ dataframe["70to79"] + dataframe["60to69"]+ dataframe["50to59"]+ dataframe["40to49"]+ dataframe["30to39"]+ dataframe["20to29"] + dataframe["10to19"]
    return dataframe

def pivot_longer_age_columns_to_one(dataframe):
    # Do Melting - Tranform/Combine the multiple  column names of different age groups into one column "Age"
    dataframe = pd.melt(dataframe, id_vars=["Country", "Sex"], value_vars=["80_above","70to79", "40to49", "30to39", "20to29", "10to19", "all_age"], var_name="Age",value_name="Suicide_rate")
    return dataframe
